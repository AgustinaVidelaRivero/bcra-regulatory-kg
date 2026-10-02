"""U-R2-CODIGO — selftest de la versión e0-r2 de E0 (tablas), sin API.

Vive en data/experiment/r2_codigo/ y no en e0_chunking/, para no tocar la
garantía estructural de B5.8.3 (selftest_b583.py:76, A3: e0_lib no conoce a
e0_tablas), que este selftest comprueba en S1. Usa el PDF real de Capitales
mínimos para la geometría de celdas (pdfplumber) y, para el verificador de
umbrales, celdas literales de tablas_<to>.json de la E0 e0-r2 de la tanda 0
(con su página) y textos de nodos de KG-Tanda0-Desarrollo-r1 y de
KG-Reextraído-r1.

Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/r2_codigo/selftest_e0r2.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import pdfplumber

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[2]
E0DIR = REPO / "data" / "experiment" / "reextraccion_v2" / "e0_chunking"
sys.path.insert(0, str(E0DIR))
sys.path.insert(0, str(AQUI))
import correr_e0 as C  # noqa: E402
import e0_tablas as e0t  # noqa: E402
import verificacion_tablas as VT  # noqa: E402

PDF_CAP = REPO / "data" / "experiment" / "subset" / "TO_capitales_minimos_actual.pdf"
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

    ok = sum(1 for _, b, _ in RESULTADOS if b)
    print(f"\nSELFTEST e0-r2: {ok}/{len(RESULTADOS)} PASS")
    return 0 if ok == len(RESULTADOS) else 1


if __name__ == "__main__":
    sys.exit(main())
