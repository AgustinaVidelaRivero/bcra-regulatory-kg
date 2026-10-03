"""U-R2-CODIGO — selftest de la versión e0-r2 de E0 (tablas), sin API.

Vive en data/experiment/r2_codigo/ y no en e0_chunking/, para no tocar la
garantía estructural de B5.8.3 (selftest_b583.py:76, A3: e0_lib no conoce a
e0_tablas), que este selftest comprueba en S1. Usa el PDF real de Capitales
mínimos para la geometría de celdas (pdfplumber) y, para el verificador de
umbrales, celdas literales de tablas_<to>.json de la E0 e0-r2 de la tanda 0
(con su página) y textos de nodos de KG-Tanda0-Desarrollo-r1 y de
KG-Reextraído-r1. S13 y S14 (K-a′ y K-b) usan PDFs de la partición del corpus
escalado (escalado_prep/pdfs).

Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/r2_codigo/selftest_e0r2.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import subprocess

import pdfplumber

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[2]
E0DIR = REPO / "data" / "experiment" / "reextraccion_v2" / "e0_chunking"
sys.path.insert(0, str(E0DIR))
sys.path.insert(0, str(AQUI))
import correr_e0 as C  # noqa: E402
import e0_lib as E0  # noqa: E402
import e0_tablas as e0t  # noqa: E402
import verificacion_tablas as VT  # noqa: E402

SUBSET = REPO / "data" / "experiment" / "subset"
PDF_CAP = SUBSET / "TO_capitales_minimos_actual.pdf"
PDFS_K = {"cap": PDF_CAP, "ext": SUBSET / "TO_exterior_cambios_actual.pdf",
          "ric": SUBSET / "TO_regimen_informativo_contable_mensual_actual.pdf",
          "pro": SUBSET / "TO_proteccion_usuarios_servicios_financieros_actual.pdf"}
CONSERVADAS_K = {"cap": ["AAA A+ BBB+ BB+"],
                 "ext": ["0202.30.00.111D, 0202.30.00.115M, 0202.30.00.117R;",
                         "0202.30.00.118U, 0202.30.00.121G, 0202.30.00.124N,"],
                 "ric": ["CONSOLIDACIÓN", "COD CASOS"], "pro": []}
# K-a′ y K-b (complemento final de U-R2-CODIGO), sobre PDFs de la partición
# (escalado_prep/pdfs): (TO, página, líneas que e0-r2 quita de la zona, líneas
# que conserva). ri_rcl p. 1 es el caso en que la línea de sección sigue
# cerrando el encabezado después de un renglón numerado con minúsculas.
CASOS_K_AB = [
    ("ri_rml", 28,
     ["REGIMEN INFORMATIVO CONTABLE MENSUAL",
      "B.C.R.A. 5.EFECTIVO MINIMO Y APLICACIÓN DE RECURSOS (R.I.-E.M.-A.R.)", "Sección 1. Efectivo mínimo"],
     ["1.11. Metodología para determinar la retribución de los saldos de las cuentas abiertas en el",
      "B.C.R.A.", "CUENTAS EN PESOS"]),
    ("nmaeef", 33,
     ["NORMAS MÍNIMAS SOBRE AUDITORÍAS EXTERNAS", "B.C.R.A. PARA ENTIDADES FINANCIERAS"],
     ["ANEXO III",
      "6. Revisión de la razonable consolidación de los estados financieros de filiales en el exterior al",
      "cierre del período correspondiente, de acuerdo con las normas del B.C.R.A. y basándose en los"]),
    ("snp_cheq", 12,
     ["SISTEMA NACIONAL DE PAGOS", "CHEQUES Y OTROS INSTRUMENTOS COMPENSABLES", "B.C.R.A.",
      "Sección 3. Instrucciones operativas.", "3.INSTRUCCIONES OPERATIVAS."],
     ["En la primera parte de este capítulo (punto 3.1) se desarrollan los mecanismos de presentación,"]),
    ("snp_dd", 28,
     ["SISTEMA NACIONAL DE PAGOS- DÉBITOS DIRECTOS", "B.C.R.A.", "Sección 6. Transacciones y mensajes.",
      "6. TRANSACCIONES Y MENSAJES."],
     ["6.1. Introducción."]),
    ("ri_rcl", 1,
     ["REGIMEN INFORMATIVO CONTABLE MENSUAL", "B.C.R.A.", "21. Ratio de Cobertura de Liquidez",
      "Sección 1. Instrucciones Generales"],
     ["1.1. Alcance"]),
]
# descarte histórico de esas páginas (sin los tres renglones de pie), igual al de HEAD 92b45d6
HIST_K_AB = {
    "ri_rml": ["REGIMEN INFORMATIVO CONTABLE MENSUAL",
               "B.C.R.A. 5.EFECTIVO MINIMO Y APLICACIÓN DE RECURSOS (R.I.-E.M.-A.R.)", "Sección 1. Efectivo mínimo"],
    "nmaeef": ["NORMAS MÍNIMAS SOBRE AUDITORÍAS EXTERNAS", "B.C.R.A. PARA ENTIDADES FINANCIERAS", "ANEXO III"],
    "snp_cheq": ["SISTEMA NACIONAL DE PAGOS", "CHEQUES Y OTROS INSTRUMENTOS COMPENSABLES", "B.C.R.A.",
                 "Sección 3. Instrucciones operativas.", "3.INSTRUCCIONES OPERATIVAS."],
    "snp_dd": ["SISTEMA NACIONAL DE PAGOS- DÉBITOS DIRECTOS", "B.C.R.A.", "Sección 6. Transacciones y mensajes.",
               "6. TRANSACCIONES Y MENSAJES."],
    "ri_rcl": ["REGIMEN INFORMATIVO CONTABLE MENSUAL", "B.C.R.A."],
}
# chunks de la escalera de e0-r2: ids presentes, ids ausentes, chunk y frase que debe contener
ESPERADO_CHUNKS_K = {
    "ri_rml": (["ri_rml::1.11", "ri_rml::1.10.4"], [], "ri_rml::1.11", "CUENTAS EN PESOS"),
    "nmaeef": (["nmaeef::S11::chapeau_seccion"], [], "nmaeef::S11::chapeau_seccion",
               "6. Revisión de la razonable consolidación de los estados financieros"),
    "snp_cheq": ([f"snp_cheq::{p}" for p in ("3.1.2.3", "3.1.2.4", "3.1.2.5", "3.1.3.1", "3.1.3.2",
                                             "3.1.4.1", "3.1.4.2")], [], None, None),
    "snp_dd": (["snp_dd::6.2.6"], ["snp_dd::S6::cierre"], "snp_dd::6.2.6",
               "Este código se asigna para identificar el tipo de registro"),
}
RESULTADOS: list[tuple[str, bool, str]] = []


def check(nombre: str, ok: bool, detalle: str = "") -> None:
    RESULTADOS.append((nombre, ok, detalle))
    print(f"  [{'PASS' if ok else 'FAIL'}] {nombre}" + (f" — {detalle}" if detalle else ""))


def tabla_real(pdf, pagina: int, indice: int, tid: str, origen: str = "e0_tablas") -> dict:
    """Tabla lógica de un segmento, armada como la arma correr_e0, con la
    geometría de celdas de la página."""
    page = pdf.pages[pagina - 1]
    tb = page.find_tables()[indice]
    seg = {"pagina": pagina, "indice_en_pagina": indice, "filas": tb.extract(),
           "filas_encabezado_repetido": []}
    seg["_geometria"] = (C._geometria_segmento(page, seg)
                         if any(c is None for f in seg["filas"] for c in f) else {})
    return {"id": tid, "origen": origen, "segmentos": [seg]}


def tabla_fija(tid: str, filas: list[list], modo: str) -> dict:
    return {"id": tid, "segmentos": [{"filas": filas, "filas_encabezado_repetido": []}],
            "serializacion": {"modo": modo}}


def nodo(label: str, descripcion: str, umbral: str | None = None) -> dict:
    props = {"descripcion": descripcion}
    if umbral:
        props["umbral"] = umbral
    return {"id": label, "label": label, "properties": props}


BLOQUE_CAP_1_2 = (
    "[TABLA cap::tabla000 | página 4 | e0_tablas | columnas]\n"
    "Rótulo: -En millones de pesos-\n"
    "Columnas: Bancos | Restantes entidades (salvo Cajas de Crédito Cooperativas)\n"
    "Fila 1: Bancos = 5.000 | Restantes entidades (salvo Cajas de Crédito Cooperativas) = 2.500\n"
    "[FIN TABLA cap::tabla000]")

# celdas literales de tablas_<to>.json (E0 e0-r2 de la tanda 0)
T000 = tabla_fija("cap::tabla000", [["Bancos", "Restantes entidades\n(salvo Cajas de Crédito Cooperativas)"],
                                    ["-En millones de pesos-", None], ["5.000", "2.500"]], "columnas")   # p. 4
T038 = tabla_fija("cap::tabla038", [["Categoría", "Tramo de BI\n(en miles de millones de euros*)",
                                     "Coeficientes marginales de BI\n(α)\ni"],
                                    ["1", "≤ 1", "12%"], ["2", "1 < BI ≤ 30", "15%"],
                                    ["3", ">30", "18%"]], "columnas")                                   # p. 150
T040 = tabla_fija("cap::tabla040", [["Período", "CCF"], ["01/01/25 al 30/06/25", "0%"],
                                    ["01/07/25 al 31/12/25", "5%"]], "columnas")                        # p. 177
T001 = tabla_fija("cap::tabla001", [["Calificación asignada", "Valor de “k”"], ["1", "1"], ["2", "1,03"],
                                    ["3", "1,08"], ["4", "1,13"], ["5", "1,19"]], "columnas")            # p. 7
ENC_POND = ["Calificación", "AAA\nhasta\nAA-", "A+\nhasta\nA-", "BBB+\nhasta\nBBB-", "BB+\nhasta\nB-",
            "Inferior a\nB-", "No\ncalificado"]
T2F001 = tabla_fija("cap::tabla2f001", [ENC_POND, ["Ponderador\nde riesgo", "0%", "20%", "50%", "100%",
                                                   "150%", "100%"]], "columnas")                        # p. 23
T2F004 = tabla_fija("cap::tabla2f004", [ENC_POND, ["Ponderador\nde riesgo", "20%", "30%", "50%", "100%",
                                                   "150%", "50%"]], "columnas")                         # p. 24
CMP = "36\n\n70300000 - [{} * ( ERC(n-1) + ... + ERC(n-36)) / 36]\n1"
R015 = tabla_fija("ric::tabla015", [["Ent idad", "%", "Partida", "Cómputo"],
                                    ["A", "20", "36000001", CMP.format("0.20")],
                                    ["B", "17", None, CMP.format("0.17")],
                                    ["C", "14", "36000004", CMP.format("0.14")]], "columnas")            # p. 23
POLCRE = {"segmentos": [{"filas": [[None, "emisoras de tarjetas de crédito y/o compra como los otros "
                                           "proveedores no financieros"],
                                     ["de crédito) no deberán financiar en cuotas las compras de sus "
                                      "clientes –personas humanas y", None],
                                     ["jurídicas– de:", None]]}]}                                       # p. 5


def main() -> int:
    print("S1. Garantía estructural de B5.8.3 (A3)")
    check("S1 e0_lib.py no menciona e0_tablas",
          "e0_tablas" not in (E0DIR / "e0_lib.py").read_text(encoding="utf-8"))

    with pdfplumber.open(str(PDF_CAP)) as pdf:
        print("S2. Bloque literal de cap::1.2 (p. 4, PDF real)")
        t = tabla_real(pdf, 4, 1, "cap::tabla000")
        b = C.armar_bloque(t, e0t)
        check("S2 bloque de cap::1.2 literal", b.get("bloque") == BLOQUE_CAP_1_2, b.get("bloque", "")[:80])
        check("S2 V1 del bloque de cap::1.2", b["v1"]["ok"])

        print("S3. E — propagación de celda combinada (cap::tabla035, p. 119)")
        t35 = tabla_real(pdf, 119, 1, "cap::tabla035")
        b35 = C.armar_bloque(t35, e0t)
        check("S3 dos celdas propagadas con la marca de la fila 2",
              b35["celdas_propagadas"] == 2 and b35["bloque"].count("⟨combinada con fila 2⟩") == 2,
              str(b35["celdas_propagadas"]))
        check("S3 V1 con propagación", b35["v1"]["ok"])

        print("S4. G — combinación horizontal (cap::tabla032, p. 108)")
        t32 = tabla_real(pdf, 108, 1, "cap::tabla032")
        b32 = C.armar_bloque(t32, e0t)
        check("S4 el 15 % abarca los cinco plazos",
              "Fila 5: " in b32["bloque"]
              and "col2 = 100% | col3 = 15% ⟨abarca hasta col7⟩" in b32["bloque"])
        check("S4 V1 con marcas de alcance", b32["v1"]["ok"])

        print("S5. G-RECUADRO")
        check("S5 positivo: recuadro de prosa de polcre::1.5",
              C.fraccion_recuadro(POLCRE) >= C.FRAC_RECUADRO_PROSA, str(C.fraccion_recuadro(POLCRE)))
        check("S5 negativo: tabla de cap::1.2",
              C.fraccion_recuadro(T000) < C.FRAC_RECUADRO_PROSA, str(C.fraccion_recuadro(T000)))

        print("S6. R-TC2 (p. 23 de Capitales mínimos)")
        p23 = pdf.pages[22]
        tbs = p23.find_tables()
        alto = float(p23.height)
        check("S6 positivo: cuadro de ponderadores (índice 2)",
              C.pasa_rtc2(tbs[2].extract(), tbs[2].bbox, alto, e0t))
        check("S6 negativo: banner «B.C.R.A.» de dos filas (índice 0)",
              tbs[0].extract()[0][0] == "B.C.R.A."
              and not C.pasa_rtc2(tbs[0].extract(), tbs[0].bbox, alto, e0t))

        print("S7. V1 rechaza tres mutaciones")
        inv = BLOQUE_CAP_1_2.replace("= 5.000", "= X").replace("= 2.500", "= 5.000").replace("= X", "= 2.500")
        check("S7 inversión de dos valores (cap::1.2)",
              not C.armar_bloque(t, e0t, bloque_externo=inv)["v1"]["ok"])
        sin_marca = b35["bloque"].replace(" ⟨combinada con fila 2⟩", "", 1)
        check("S7 marca de combinada borrada (cap::tabla035)",
              sin_marca != b35["bloque"]
              and not C.armar_bloque(t35, e0t, bloque_externo=sin_marca)["v1"]["ok"])
        perdido = b35["bloque"].replace("= 0,25%", "= 0,2%", 1)
        check("S7 carácter perdido (cap::tabla035)",
              perdido != b35["bloque"]
              and not C.armar_bloque(t35, e0t, bloque_externo=perdido)["v1"]["ok"])

    print("S8. verificacion_tablas — las dos marcas de cap::1.2")
    n_bancos = nodo("Exigencia capital mínimo 2.500 M$ bancos",
                    "Los bancos (salvo Cajas de Crédito Cooperativas) deberán mantener un capital "
                    "mínimo de 2.500 millones de pesos", "2.500 millones de pesos")
    n_rest = nodo("Exigencia capital mínimo 5.000 M$ entidades residuales",
                  "Las restantes entidades (salvo Bancos y Cajas de Crédito Cooperativas) deberán "
                  "mantener un capital mínimo de 5.000 millones de pesos", "5.000 millones de pesos")
    check("S8 marca: bancos con 2.500", VT.verificar_nodo(n_bancos, [T000])["marca"])
    check("S8 marca: restantes entidades con 5.000", VT.verificar_nodo(n_rest, [T000])["marca"])

    print("S9. verificacion_tablas — falsos positivos de las versiones 1 a 3 (sin marca)")
    casos_neg = [
        ("v1: coeficiente marginal de la categoría 1 = 12 % (cap::7.1.2)", T038,
         nodo("Coeficientes marginales (α) — categoría 1",
              "Para las entidades incluidas en la categoría 1 (BI igual o inferior al equivalente en "
              "pesos de €1.000 millones), el coeficiente marginal es del 12%")),
        ("v2: raíz de «No calificado» frente a «calificación» (cap::2.12.2.5)", T2F001,
         nodo("Ponderador riesgo A+-A-", "Ponderador de riesgo 20% para calificaciones de A+ hasta A-",
              "20%")),
        ("v3: fragmentos de fechas de «Período» (cap::12.2)", T040,
         nodo("Conversión mediante CCF — grupo 2 (01/01/25 a 31/12/25)",
              "deberán convertir los compromisos … mediante la aplicación de los CCF de acuerdo con el "
              "siguiente cronograma: 01/01/25 al 30/06/25 CCF 0%; 01/07/25 al 31/12/25 CCF 5%")),
        ("v3: código de partida tomado como cantidad (ric::5.1.3.2)", R015,
         nodo("Informar reducción exigencia en partida 36000001",
              "Se informará la correspondiente reducción de exigencia en la partida 36000001 … "
              "Cálculo para Grupo A: 70300000 - [0.20 * (ERC(n-1) + ... + ERC(n-36)) / 36]")),
        ("v3: tabla de «k» por calificación (cap::2.1, r1)", T001,
         nodo("Factor k según calificación SEFYC",
              "k: factor vinculado a la calificación asignada a la entidad según la evaluación "
              "efectuada por la SEFYC, teniendo en cuenta la siguiente escala: Calificación 1 → k=1; "
              "Calificación 2 → k=1,03; Calificación 3 → k=1,08; Calificación 4 → k=1,13; "
              "Calificación 5 → k=1,19.")),
    ]
    for nombre, tabla, n in casos_neg:
        check("S9 " + nombre, not VT.verificar_nodo(n, [tabla])["marca"])

    print("S10. verificacion_tablas — inversión sintética fuera de cap::1.2 (cap::tabla2f004)")
    n_inv = nodo("Ponderador AAA", "Exposiciones AAA hasta AA-: ponderador 30%", "30%")
    r = VT.verificar_nodo(n_inv, [T2F004])
    check("S10 marca: 30 % pertenece a «A+ hasta A-», el nodo nombra «AAA hasta AA-»", r["marca"],
          str([v["veredicto"] for v in r["valores"]]))

    print("S11. K — encabezados de página en mayúsculas (cap, ext, ric, pro; PDF real)")
    for to, pdf in PDFS_K.items():
        paginas = E0.extraer_lineas(pdf)
        roles = E0.clasificar_paginas(paginas)
        rep = E0.titulos_mayusculas_repetidos(paginas, roles)
        cons = [l.texto for l in C.lineas_conservadas_k(paginas, roles, rep)]
        check(f"S11 {to}: conserva {CONSERVADAS_K[to] or 'ninguna línea'}", cons == CONSERVADAS_K[to],
              str(cons))
        if to == "pro":
            l26 = [l.texto for l in paginas[25][:5]
                   if "".join(l.texto.split()) == "PROTECCIÓNDELOSUSUARIOSDESERVICIOSFINANCIEROS"]
            check("S11 pro::3.1.3 (p. 26): el título con «SERVI CIOS» se repite sin espacios y se descarta",
                  l26 == ["PROTECCIÓN DE LOS USUARIOS DE SERVI CIOS FINANCIEROS"]
                  and "".join(l26[0].split()) in rep)

    print("S12. M — guarda de salida de e0-r2")

    def _aborta(*a, **k):   # si la guarda no actuara, nada llega a escribirse
        raise RuntimeError("selftest: la guarda de salida no actuó")

    original = C.E0.extraer_lineas
    C.E0.extraer_lineas = _aborta
    try:
        for nombre in ("salida", "salida_enm01", "salida_tanda0"):
            try:
                C.correr(E0DIR / nombre, version_e0=C.VERSION_E0_R2)
                check(f"S12 e0-r2 se niega a escribir en {nombre}", False)
            except ValueError as e:
                check(f"S12 e0-r2 se niega a escribir en {nombre}", "no escribe" in str(e))
            except RuntimeError as e:
                check(f"S12 e0-r2 se niega a escribir en {nombre}", False, str(e))
    finally:
        C.E0.extraer_lineas = original
    r = subprocess.run([sys.executable, "-B", str(E0DIR / "correr_e0.py"), "--version-e0", "e0-r2"],
                       capture_output=True, text=True, env={**__import__("os").environ,
                                                            "PYTHONDONTWRITEBYTECODE": "1"})
    check("S12 sin --salida, e0-r2 sale con error de argumentos",
          r.returncode == 2 and "exige --salida" in r.stderr, r.stderr.strip()[-80:])

    print("S13. K-a′ y K-b — encabezado forzado y títulos de sección numerados (partición; PDF real)")
    pdfs_part = REPO / "data" / "experiment" / "escalado_prep" / "pdfs"
    paginas_k: dict[str, list] = {}
    for to, pag, quitar, conservar in CASOS_K_AB:
        paginas = paginas_k.setdefault(to, E0.extraer_lineas(pdfs_part / f"{to}.pdf"))
        rep = E0.titulos_mayusculas_repetidos(paginas, E0.clasificar_paginas(paginas))
        lineas = paginas[pag - 1]
        cont, desc, _ = E0.separar_encabezado_pie(lineas, mayusculas_repetidas=rep, pie_desde_version=True)
        t_cont = [l.texto.strip() for l in cont]
        t_desc = [l.texto.strip() for l in desc]
        _, hist, _ = E0.separar_encabezado_pie(lineas)
        check(f"S13 {to} p. {pag}: e0-r2 quita {len(quitar)} y conserva {len(conservar)} líneas de la zona",
              all(q in t_desc for q in quitar) and all(c in t_cont for c in conservar)
              and not any(c in t_desc for c in conservar),
              f"descartadas {[t[:40] for t in t_desc]}")
        check(f"S13 {to} p. {pag}: el descarte histórico no cambia",
              [l.texto.strip() for l in hist][-len(HIST_K_AB[to]):] == HIST_K_AB[to]
              and len(hist) == 3 + len(HIST_K_AB[to]),
              str([l.texto[:40] for l in hist]))

    def _l(i: int, t: str) -> E0.Linea:
        return E0.Linea(pagina=1, top=10.0 * i, x0=50.0, texto=t, ngaps=0,
                        ultimo_numerico=False, primer_codigo=False)

    sint = [_l(0, "TÍTULO DEL TO"), _l(1, "B.C.R.A."), _l(2, "1. DATOS GENERALES"), _l(3, "Texto del punto.")]
    rep_sint = {"TÍTULODELTO", "B.C.R.A."}
    c_vig, _, _ = E0.separar_encabezado_pie(sint, mayusculas_repetidas=rep_sint)
    c_sr, _, _ = E0.separar_encabezado_pie(sint, mayusculas_repetidas=rep_sint, labels_preservables=set())
    check("S13 K-b (sintético): fuera del modo sin raíz, «1. DATOS GENERALES» se descarta",
          [l.texto for l in c_vig] == ["Texto del punto."], str([l.texto for l in c_vig]))
    check("S13 K-b (sintético): en el modo sin raíz decide labels_preservables y la línea queda",
          [l.texto for l in c_sr] == ["1. DATOS GENERALES", "Texto del punto."], str([l.texto for l in c_sr]))
    sint2 = [_l(0, "TÍTULO DEL TO"), _l(1, "1.4. Plazo para presentar ante el"), _l(2, "B.C.R.A."),
             _l(3, "la información.")]
    c2, _, _ = E0.separar_encabezado_pie(sint2, mayusculas_repetidas=rep_sint)
    c2h, _, _ = E0.separar_encabezado_pie(sint2)
    check("S13 K-a′ (sintético): «B.C.R.A.» después de un renglón numerado con minúsculas es texto",
          [l.texto for l in c2] == ["1.4. Plazo para presentar ante el", "B.C.R.A.", "la información."]
          and [l.texto for l in c2h] == [l.texto for l in c2], str([l.texto for l in c2]))

    print("S14. K-a′ y K-b — chunks de la escalera de e0-r2 en los cuatro TOs afectados (PDF real)")
    ids_k: dict[str, dict[str, str]] = {}
    for to, paginas in paginas_k.items():
        if to not in ESPERADO_CHUNKS_K:
            continue
        res, *_ = C.escalera_e0_r2(to, f"{to}.pdf", paginas, E0.clasificar_paginas(paginas))
        res.reasignaciones_continuidad = E0.aplicar_continuidad_enumeracion(res)
        E0.corregir_fronteras_intra_palabra(res)
        ids_k[to] = {c["id"]: c["texto"] for c in E0.construir_chunks(res)}
    for to, (presentes, ausentes, chunk_texto, frase) in ESPERADO_CHUNKS_K.items():
        ids = ids_k[to]
        check(f"S14 {to}: {len(presentes)} ids presentes, {len(ausentes)} ausentes"
              + (f", «{frase[:30]}…» en {chunk_texto}" if chunk_texto else ""),
              all(i in ids for i in presentes) and not any(i in ids for i in ausentes)
              and (chunk_texto is None or frase in ids.get(chunk_texto, "")),
              f"faltan {[i for i in presentes if i not in ids]}, sobran {[i for i in ausentes if i in ids]}")

    ok = sum(1 for _, b, _ in RESULTADOS if b)
    print(f"\nSELFTEST e0-r2: {ok}/{len(RESULTADOS)} PASS")
    return 0 if ok == len(RESULTADOS) else 1


if __name__ == "__main__":
    sys.exit(main())
