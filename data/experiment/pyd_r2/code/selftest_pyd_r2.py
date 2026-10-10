"""
selftest_pyd_r2.py — U-PYD, etapa P1: selftest de modelos, política,
validador, reglas de comparación y generación del perfil r2.

Grupos:
  G1  listas y matriz contra los módulos sellados (perfil v3_b54) y el catálogo r2;
  G2  política: sha256, pasos, alias y parámetros provisionales;
  G3  valores reales de N1 (diseño U-LISTAS-NOMAP, sección g), cada uno con su
      modo esperado según la política;
  G4  reglas de comparación por sentido, negación, compuestas, adyacencia
      (con «capital mínimo» como negativo), precedencia, sin marcador y la raíz
      «super-» (con «Superintendencia» como negativo);
  G5  los cuatro casos de control obligatorios (L-ESQ-R2 §1.3.3 y §1.5);
  G6  control de BKL-0038 y marca de no verificada por E3;
  G7  mención en dos niveles y omisiones (P-b3, P-b4, P-e2);
  G8  modelos: invariantes de marcas y claves cerradas;
  G10 calibración P3 (decisiones de la autora sobre P2): raíces, formas nuevas,
      «al», «factor» solo desde tramo o título, «igual», h = 2, largo 11, lista
      JSON en omisiones, y los casos pedidos (los cuatro de control están en G5);
  G9  tool schema generado: regeneración idéntica, un elemento válido pasa y uno
      con un valor fuera de lista queda marcado, no descartado;
  G11 predicado derivado `remite_a` (enmienda 1 al mandato de U-R2-CODIGO, con la
      enmienda 2 de L-ESQ-R2): fuera de las listas de E1, firma de 56, lista de
      `alcance` e invariantes de la arista; tool schema y política sin cambio;
  G12 lo que agrega el ensamblado (decisión 3 sobre el FRENO R3 de U-R2-CODIGO):
      marcas del nodo, base y tabla del elemento de umbral, calificador y
      relaciones del esqueleto; la entidad de E1 sigue sin admitir las marcas;
  G13 U-PROMPT-R2, P3: la forma r2 completa (tramo de evidencia simple y de
      dos segmentos, término literal, Comunicacion derivada, límite relativo,
      otras_propiedades de la relación, source y destino) y lo que pasó por E3
      (vistos_e3, no_verificada_e3 por E3, establecida_en derivada);
  G14 U-PROMPT-R2, P3b-2: el tramo en orden de lectura del mini-chunk a mitad de
      oración (h), la Comunicacion desde el tramo verificado (l), la modalidad
      clasificada y la marca de la copia de la nota de E3 que llega a la entidad;
  G15 U-R2-CODIGO-2, C2: cuantías nuevas (c: «hs.», «hábil» en singular, «o más»
      entre el paréntesis y la unidad, ordinal con marcador), alcance de la
      negación, «o no» e «igual o superior» (i), comparador pegado sobre el
      coeficiente (j), «más del» y «menos del» (enmienda 5 a L-ESQ-R2),
      marcador del encabezado en un tramo compuesto (k) y plazo sin marcador
      (m, enmienda 3 a L-ESQ-R2; con «maximo_asumido», la regla anterior de r2a).
  G16 U-PROMPT-R2, P3c-2: el tramo de la omisión contra el texto propio y el heredado,
      con su contador (g), y el contador de las omisiones meta_normativo con marca, con
      las siete clases de la enmienda 7 a L-ESQ-R2 (corrección del FRENO P3c-2) y la
      modalidad del prefijo en tres subclases: opción, consejo y forma.
Con la enmienda 3 a L-ESQ-R2 (C2 de U-R2-CODIGO-2, punto m), los casos que
esperaban un plazo sin marcador con máximo inclusivo y `comparacion_asumida`
esperan `no_determinada`, con la regla `sin_marcador_plazo` y sin la marca.

Solo lectura: no escribe archivos. Lee E0 de la tanda 0 (con sha256 de N1),
la lectura de `limita` y el ejemplo del préstamo. Salida determinística.

Uso (desde la raíz del repo):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/pyd_r2/code/selftest_pyd_r2.py
"""

from __future__ import annotations

import csv
import json
import sys
from collections import OrderedDict
from pathlib import Path

AQUI = Path(__file__).resolve().parent
if str(AQUI) not in sys.path:
    sys.path.insert(0, str(AQUI))
import modelos_r2 as M  # noqa: E402
import reglas_comparacion as RC  # noqa: E402
import validador_r2 as V  # noqa: E402
import generar_r2 as G  # noqa: E402
from pydantic import ValidationError  # noqa: E402

REPO = M.REPO
E0 = REPO / "data" / "experiment" / "reextraccion_v2" / "e0_chunking" / "salida_tanda0"
E0_SHA = {  # reports/u_listas_nomap/n1_inventario.json, entradas.e0_<to>.sha256
    "cap": "1931138dac0a107a69a7ff6312400f00465b991d52135457735beeb3e442c825",
    "cla": "98808886a406d8321c678836a55f92eea983d594d95358dd21ceb537487ac0b1",
    "ext": "cbcd1a86f55ea49110610587873881c68c13a9d7975d3fd5e465f26302be2d12",
    "ric": "fafebb82e07b34191b60022c1c179ea7d2213fd1f5d5f3a408b518c836c94c0d",
}
LECTURA_LIMITA = REPO / "reports" / "u_umbral" / "lectura_limita" / "lectura_limita_30.csv"
EJEMPLO_PRESTAMO = REPO / "docs" / "tesis" / "figuras" / "ejemplo_prestamo_datos.json"
POLITICA_SHA_ESPERADO = None  # se informa; el freno la registra
# Generación sellada de U-PYD (57a8dd2, manifest_generados_r2.json): sha256 de
# modelos_r2.py con que se generaron tool schema y enums, y de lo generado. El
# agregado de `remite_a` (U-R2-CODIGO) cambia el sha de modelos_r2.py y no lo
# generado; generados/ no se regenera (fuera de las escrituras autorizadas).
MODELOS_SHA_GENERACION_57A8DD2 = "43ae09fbaa429bea8406e1c5021c408ce495f826511cf6dcf6e9c273db5d639c"
TOOL_SCHEMA_SHA_57A8DD2 = "307d2b788c5ba855a502522b171c39ba1a6b2d56850e1a4e3c8c8a2bb5068da4"
ENUMS_SHA_57A8DD2 = "abd197ac8bbb818f680dc80d1b9c9df3e1f1f733fce3fd46b35e7440e7ce4241"
# Generación vigente (U-PROMPT-R2, P2): modelos_r2.py con las decisiones 15 a 17 del mandato (tramo de
# evidencia por entidad salvo el TextoOrdenado; TextoOrdenado sin properties y Comunicacion solo con codigo;
# Definicion.termino literal; otras_propiedades en relaciones; source y destino en la omisión). Los enums no
# cambian: son los de 57a8dd2. U-PROMPT-R2, P3: los modelos del elemento validado, del nodo y de la arista (tramo en
# la procedencia, no_verificada_e3 por lo que pasó por E3, establecida_en derivada) cambian el sha de modelos_r2.py
# y no lo generado: el manifiesto se regenera con el sha nuevo (decisión 13).
MODELOS_SHA_GENERACION_P2 = "9a3fe3ec929342d2dc4d00c4235af0dadf7bceb2d867e0b692c0ab111621e964"
MODELOS_SHA_GENERACION = "e67f15ae13dd5419ea0ce1a08dbef63c86cbdf9c269772a0b02a4e27b4c3a2ca"
TOOL_SCHEMA_SHA_GENERACION = "0c391f2b23bb7c94ec2606bd0315f3e4589c16a3571eaaa210a27babaa0f8ba2"
POLITICA_SHA_DECISION_10 = "82e8752aea1d6ad869d6023d303c0af45182dd9333753681787d7a581ef6d00b"

RES: "OrderedDict[str, list]" = OrderedDict()


def chequear(grupo: str, nombre: str, cond: bool, detalle: str = "") -> None:
    RES.setdefault(grupo, []).append((nombre, bool(cond), detalle))


def cargar_chunks() -> dict:
    out = {}
    for to, sha in E0_SHA.items():
        p = E0 / f"chunks_{to}.json"
        s = M.sha256_archivo(p)
        if s != sha:
            raise SystemExit(f"E0 {to}: sha256 {s[:12]}… distinto del de N1 — se frena")
        for c in json.loads(p.read_text(encoding="utf-8")):
            out[c["id"]] = c
    return out


def ent(lid, tipo, label, punto, props=None, **extra):
    d = {"local_id": lid, "type": tipo, "label": label, "punto": punto}
    if props is not None:
        d["properties"] = props
    d.update(extra)
    return d


def rel(pred, punto, **kw):
    d = {"predicate": pred, "punto": punto}
    d.update(kw)
    return d


def cont(res, campo, trat):
    return res["contadores"].get(campo, {}).get(trat, 0)


def motivos(res):
    return res["metricas"]["rechazos_por_motivo"]


def una(texto, desc=None, titulo=None, i=0):
    cs = RC.analizar(texto, desc, titulo)
    return cs[i] if len(cs) > i else None


# ------------------------------------------------------------------------- #
def g1_listas():
    g = "G1 listas y matriz"
    sys.path.insert(0, str(REPO / "data" / "experiment" / "reextraccion_v2" / "e1_extractor"))
    import perfil_e1  # noqa: PLC0415
    import prompt_e1  # noqa: PLC0415
    esq = perfil_e1.perfil("v3_b54").esquema
    import prompt_congelado as pc  # noqa: PLC0415 — en el path vía el perfil v3
    chequear(g, "9 tipos = ENTITY_TYPES_CONGELADO", M.TIPOS_ENTIDAD == tuple(pc.ENTITY_TYPES_CONGELADO))
    chequear(g, "13 predicados = PREDICATES_CONGELADO", M.PREDICADOS == tuple(pc.PREDICATES_CONGELADO))
    chequear(g, "predicados de sujeto = SUJETO_PREDICATES", M.PREDICADOS_SUJETO == tuple(pc.SUJETO_PREDICATES))
    chequear(g, "Obligacion.tipo = OBLIGACION_TIPO_CONGELADO (6)",
             M.OBLIGACION_TIPO == tuple(pc.OBLIGACION_TIPO_CONGELADO))
    chequear(g, "matriz congelada = DOMAIN_RANGE_CONGELADO",
             {p: (set(d), set(r)) for p, (d, r) in M.FIRMAS_CONGELADAS.items()} == pc.DOMAIN_RANGE_CONGELADO)
    tipos = M.TIPOS_ENTIDAD + (M.TIPO_SUJETO,)
    nuevas = [(s, p, t) for s in tipos for p in M.PREDICADOS for t in tipos
              if M.firma_r2(s, p, t) and not M.firma_congelada(s, p, t)]
    perdidas = [(s, p, t) for s in tipos for p in M.PREDICADOS for t in tipos
                if M.firma_congelada(s, p, t) and not M.firma_r2(s, p, t)]
    chequear(g, "matriz r2 = congelada + 2 firmas de condicion_de",
             sorted((p, s, t) for s, p, t in nuevas) == sorted(M.AMPLIACION_R2), str(nuevas))
    chequear(g, "matriz r2 no pierde firmas", perdidas == [])
    chequear(g, "firma congelada igual a pc.firma_valida en 10×13×10",
             all(M.firma_congelada(s, p, t) == pc.firma_valida(s, p, t)
                 for s in tipos for p in M.PREDICADOS for t in tipos))
    n1 = json.loads((REPO / "reports" / "u_listas_nomap" / "n1_inventario.json").read_text(encoding="utf-8"))
    l3 = n1["listas"]["v3"]
    chequear(g, "Restriccion.tipo = lista v3 de N1, sin valor nuevo", list(M.RESTRICCION_TIPO) == l3["Restriccion.tipo"])
    chequear(g, "Comunicacion.tipo = lista v3 de N1 + «externa»",
             list(M.COMUNICACION_TIPO) == l3["Comunicacion.tipo"] + ["externa"])
    chequear(g, "comparacion: 7 valores", len(M.COMPARACION) == 7 and "no_determinada" in M.COMPARACION)
    chequear(g, "frecuencia: 6 valores", M.FRECUENCIA == ("diaria", "semanal", "mensual", "trimestral",
                                                          "semestral", "anual"))
    chequear(g, "omisión: 5 categorías", len(M.CATEGORIA_OMISION) == 5
             and "relacion_sin_predicado" in M.CATEGORIA_OMISION)
    chequear(g, "unidad: porcentaje, moneda, días, meses, años, veces y UVA", len(M.UNIDAD) == 7)
    chequear(g, "catálogo r2: 110 vigentes y 5 lápidas", len(M.SUJETOS_R2) == 110 and len(M.SUJETOS_R2_LAPIDAS) == 5)
    chequear(g, "bloque v3 (102) ⊂ catálogo r2", set(esq.sujetos_catalogo_set) <= M.SUJETOS_R2_SET
             and len(esq.sujetos_catalogo_set) == 102)
    chequear(g, "nombre del tool = prompt_e1.NOMBRE_TOOL", M.NOMBRE_TOOL_R2 == prompt_e1.NOMBRE_TOOL)
    claves_v3 = {t: tuple(c) for t, c in l3["claves"].items()}
    ok = all(set(M.CLAVES_R2[t]) - {"umbrales"} | set(M.CLAVES_HEREDADAS_V3.get(t, ())) == set(claves_v3[t])
             for t in M.TIPOS_ENTIDAD)
    chequear(g, "claves r2 + heredadas de v3 − umbrales = claves v3 de N1", ok)


def g2_politica():
    g = "G2 política"
    pol = V.Politica()
    chequear(g, "sha256 de la política = sha256 del archivo", pol.sha256 == M.sha256_archivo(V.POLITICA))
    chequear(g, "fuente L-ESQ-R2 = versión firmada 4ef7650 (66c4a1b9…)",
             pol.d["fuentes"]["enmienda_l_esq_r2"]["sha256_version_firmada"].startswith("66c4a1b9")
             and pol.d["fuentes"]["enmienda_l_esq_r2"]["commit_firma"] == "4ef7650")
    chequear(g, "alias de tipo: solo Restriction → Restriccion", pol.alias_tipo == {"Restriction": "Restriccion"})
    chequear(g, "alias semántico: solo exceptua_restriccion → exceptua",
             pol.alias_pred == {"exceptua_restriccion": "exceptua"})
    chequear(g, "sin renombres de claves (heredadas v3 conservadas, no renombradas)",
             pol.d["campos"]["claves"]["heredadas_v3"] == {"Restriccion": ["umbral"], "Obligacion": ["plazo"]})
    modos = {c: pol.d["campos"][c].get("si_no_resuelve") for c in V.Politica.PASOS_CONOCIDOS}
    chequear(g, "modos: tipos y predicados rechazan; Obligacion.tipo normaliza; Restriccion, Comunicacion y "
                "frecuencia registran",
             modos == {"tipo_entidad": "rechazar", "predicado": "rechazar", "Obligacion.tipo": "normalizar",
                       "Restriccion.tipo": "registrar", "Comunicacion.tipo": "registrar",
                       "Obligacion.frecuencia": "registrar"}, str(modos))
    chequear(g, "padre sugerido sin mención: se descarta el padre y la relación se acepta",
             pol.d["campos"]["padre_sugerido"]["si_sin_mencion"].startswith("descartar_padre"))
    chequear(g, "otras_propiedades declarado en la política de claves",
             "otras_propiedades" in pol.d["campos"]["claves"])
    chequear(g, "holgura de la mención = 2 (decisión) y largo mínimo de omisión = 11 (provisional)",
             pol.holgura == 2 and "decisión" in pol.d["parametros"]["mencion_holgura_tokens"]["estado"]
             and pol.largo_min_omision == 11
             and "provisional" in pol.d["parametros"]["omision_largo_minimo_tokens"]["estado"])
    chequear(g, "límite declarado de la mención (presencia, no pertenencia; 6 de 63) en la política",
             "6 de las 63" in pol.d["campos"]["sujeto_mencion"]["limite_declarado"])
    try:
        import tempfile  # noqa: PLC0415
        d = json.loads(V.POLITICA.read_text(encoding="utf-8"))
        d["campos"]["predicado"]["pasos"].append("distancia_de_edicion")
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "pol.json"
            p.write_text(json.dumps(d), encoding="utf-8")
            V.Politica(p)
        chequear(g, "un paso desconocido en la política frena", False)
    except RuntimeError:
        chequear(g, "un paso desconocido en la política frena", True)


def g3_valores_n1(ch):
    g = "G3 valores reales de N1"
    c = ch["cla::5.1.1.1"]
    pt = "5.1.1.1"
    to = ent("to", "TextoOrdenado", "Clasificación de deudores", pt)

    # tipos de entidad
    r = V.validar({"entities": [to, ent("e1", "Restriction", "Tope", pt, {"descripcion": "x", "tipo": "limite_cuantitativo"}),
                                ent("e2", "Recomendacion", "Recomendación de buenas prácticas", pt, {"descripcion": "y"})],
                   "relations": [rel("establecida_en", pt, source="e1", target="to"),
                                 rel("establecida_en", pt, source="e2", target="to")]}, c, forma="v3")
    e1 = [x for x in r["entidades"] if x["local_id"] == "e1"]
    chequear(g, "«Restriction» → Restriccion, normalizado por alias, original guardado",
             e1 and e1[0]["type"] == "Restriccion" and e1[0]["originales"].get("type") == "Restriction"
             and cont(r, "tipo_entidad", "normalizado_alias") == 1)
    chequear(g, "«Restriction»: su relación se recupera (no queda colgante)",
             any(x["source"] == "e1" for x in r["relaciones"]))
    om = [x for x in r["omisiones"] if x["categoria"] == "fuera_de_tipos"]
    chequear(g, "«Recomendacion» → rechazo type_invalido + omisión fuera_de_tipos (P-e3)",
             motivos(r).get("type_invalido") == 1 and len(om) == 1 and "Recomendacion" in om[0]["nota"]
             and om[0]["origen"] == "validador_p_e3")
    chequear(g, "«Recomendacion»: su relación se rechaza con registro (ref_colgante)",
             motivos(r).get("ref_colgante") == 1)

    # predicados
    base = [to, ent("e1", "Restriccion", "Tope", pt, {"descripcion": "x", "tipo": "limite_cuantitativo"}),
            ent("e2", "Excepcion", "Salvo", pt, {"descripcion": "y"})]
    casos = [("establec\nida_en", "establecida_en", "normalizado_forma", ("e1", "to")),
             ("establec ida_en", "establecida_en", "normalizado_forma", ("e1", "to")),
             ("exceptua_restriccion", "exceptua", "normalizado_alias", ("e2", "e1"))]
    for crudo, esperado, trat, (s, t) in casos:
        r = V.validar({"entities": base, "relations": [rel(crudo, pt, source=s, target=t)]}, c, forma="v3")
        ok = (len(r["relaciones"]) == 1 and r["relaciones"][0]["predicate"] == esperado
              and r["relaciones"][0]["originales"].get("predicate") == crudo and cont(r, "predicado", trat) == 1)
        chequear(g, f"predicado {crudo!r} → {esperado} ({trat})", ok)
    r = V.validar({"entities": base + [ent("e3", "Operacion", "Operar", pt, {"tipo": "op"})],
                   "relations": [rel("aplicaA", pt, source="e1", sujeto_id="Sujeto_cliente")]}, c, forma="v3")
    chequear(g, "predicado 'aplicaA' → aplica_a (camelCase, forma)",
             len(r["relaciones"]) == 1 and r["relaciones"][0]["predicate"] == "aplica_a"
             and cont(r, "predicado", "normalizado_forma") == 1)
    for crudo in ("estableci_en", "establecia_en"):
        r = V.validar({"entities": base, "relations": [rel(crudo, pt, source="e1", target="to")]}, c, forma="v3")
        chequear(g, f"predicado {crudo!r} → rechazo (sin distancia de edición)",
                 motivos(r).get("predicado_invalido") == 1 and not r["relaciones"])

    # Restriccion.tipo
    for valor in ("limite_temporal", "obligacion_cualitativa"):
        r = V.validar({"entities": [to, ent("e1", "Restriccion", "Plazo", pt, {"descripcion": "x", "tipo": valor})],
                       "relations": []}, c, forma="v3")
        e = r["entidades"][1]
        chequear(g, f"Restriccion.tipo {valor!r} → registrado sin cambiar, con marca",
                 e["properties"]["tipo"] == valor and e["fuera_de_lista"] == ["tipo"]
                 and cont(r, "Restriccion.tipo", "registrado_fuera_de_lista") == 1)

    # Comunicacion.tipo (valores reales del crudo; N1 y escaneo del crudo de P1)
    casos_com = [
        ({"codigo": "Decreto-2921/70", "tipo": "Decreto", "numero": 2921}, "Decreto 2.921/70", "externa", "externa_por_valor"),
        ({"codigo": "LEY-25506", "tipo": "LEY", "numero": 25506}, "Ley 25.506", "externa", "externa_por_valor"),
        ({"codigo": "CNV-1.003/24", "tipo": "Resolución", "numero": 1003}, "Res. CNV 1.003/24", "externa", "externa_por_valor"),
        ({"codigo": "RES-92/21", "tipo": "MINISTERIAL"}, "Res. 92/21", "externa", "externa_por_codigo_o_label"),
        ({"codigo": "", "tipo": "", "numero": ""}, "Res. Gral. 2.345/07", "externa", "externa_por_codigo_o_label"),
        ({"codigo": "", "tipo": ""}, "Capitales mínimos entidades financieras", "", "registrado_fuera_de_lista"),
        ({"codigo": "ICMECMA-3.2.1", "tipo": "referencia", "numero": 0}, "COM ICMECMA punto 3.2.1", "referencia",
         "registrado_fuera_de_lista"),
        ({"codigo": "SEFyC", "tipo": "normas"}, "Com. SEFyC", "normas", "registrado_fuera_de_lista"),
    ]
    for props, label, esperado, trat in casos_com:
        r = V.validar({"entities": [to, ent("e1", "Comunicacion", label, pt, props)], "relations": []}, c, forma="v3")
        e = r["entidades"][1]
        tipo_ok = e["properties"].get("tipo", "") == esperado
        marca_ok = (e["fuera_de_lista"] == ["tipo"]) == (trat == "registrado_fuera_de_lista")
        chequear(g, f"Comunicacion.tipo {props['tipo']!r} ({label}) → {esperado or 'ausente'} ({trat})",
                 tipo_ok and marca_ok and cont(r, "Comunicacion.tipo", trat) == 1
                 and e["originales"].get("tipo") == props["tipo"], json.dumps(e["properties"], ensure_ascii=False))
    r = V.validar({"entities": [to, ent("e1", "Comunicacion", "Com. A 7825", pt, {"codigo": "A-7825", "tipo": "otro",
                                                                                  "numero": "7825"})],
                   "relations": []}, c, forma="v3")
    e = r["entidades"][1]
    chequear(g, "Comunicacion.tipo 'otro' con código «A-7825» → A, derivado del código (caso sintético)",
             e["properties"]["tipo"] == "A" and cont(r, "Comunicacion.tipo", "derivado_de_codigo_o_label") == 1)
    chequear(g, "Comunicacion.numero '7825' → 7825 entero, con contador y original",
             e["properties"]["numero"] == 7825 and e["originales"]["numero"] == "7825"
             and cont(r, "valores", "numero_string_a_entero") == 1)

    # claves
    r = V.validar({"entities": [to,
                                ent("e1", "Obligacion", "Informar", pt, {"descripcion": "x", "tipo": "otra",
                                                                        "plazo_o_frecuencia": "mensual",
                                                                        "plazo": "10 días", "umbral": "5%"}),
                                ent("e2", "Potestad", "Podrá", pt, {"descripcion": "y", "umbral": "2%", "tipo": "x"}),
                                ent("e3", "Restriccion", "Tope", pt, {"descripcion": "z", "tipo": "limite_cuantitativo",
                                                                     "umbral": "30%"}),
                                ent("e4", "Operacion", "Op", pt, {"tipo": "t", "etapa": "otorgamiento"})],
                   "relations": []}, c, forma="v3")
    E = {x["local_id"]: x for x in r["entidades"]}
    chequear(g, "Obligacion.plazo_o_frecuencia → properties_no_definidas, sin renombrar",
             E["e1"]["properties_no_definidas"].get("plazo_o_frecuencia") == "mensual"
             and "frecuencia" not in E["e1"]["properties"])
    chequear(g, "Obligacion.umbral → properties_no_definidas", E["e1"]["properties_no_definidas"].get("umbral") == "5%")
    chequear(g, "Obligacion.plazo (v3) → campos_heredados_v3", E["e1"]["campos_heredados_v3"] == {"plazo": "10 días"})
    chequear(g, "Potestad.umbral y Potestad.tipo → properties_no_definidas (L-ESQ-R2 §1.3, decisión 5)",
             E["e2"]["properties_no_definidas"] == {"umbral": "2%", "tipo": "x"})
    chequear(g, "Restriccion.umbral (v3) → campos_heredados_v3", E["e3"]["campos_heredados_v3"] == {"umbral": "30%"})
    chequear(g, "Operacion.etapa → properties_no_definidas", E["e4"]["properties_no_definidas"] == {"etapa": "otorgamiento"})
    chequear(g, "ninguna entidad se rechaza por una clave", len(r["entidades"]) == 5 and not r["rechazos"])

    # Obligacion.tipo
    for valor in ("evaluacion", "obtención_de_datos", "pago"):
        r = V.validar({"entities": [to, ent("e1", "Obligacion", "Deber", pt, {"descripcion": "x", "tipo": valor})],
                       "relations": []}, c, forma="v3")
        e = r["entidades"][1]
        chequear(g, f"Obligacion.tipo {valor!r} → «otra», original guardado",
                 e["properties"]["tipo"] == "otra" and e["originales"]["tipo"] == valor
                 and cont(r, "Obligacion.tipo", "normalizado_a_otra") == 1)

    # sujetos y padre (relaciones reales del crudo)
    c7 = ch["ext::7.3.2"]
    r = V.validar({"entities": [ent("to", "TextoOrdenado", "Exterior y cambios", "7.3.2"),
                                ent("e1", "Obligacion", "Deber", "7.3.2", {"descripcion": "x", "tipo": "otra"})],
                   "relations": [rel("aplica_a", "7.3.2", source="e1",
                                     sujeto_propuesto="No residentes distintos del importador del exterior",
                                     sujeto_propuesto_padre_sugerido="Sujeto_acreedor_del_exterior")]}, c7, forma="v3")
    x = r["relaciones"][0] if r["relaciones"] else {}
    chequear(g, "padre fuera del catálogo r2 (Sujeto_acreedor_del_exterior, lápida) → anulado, original guardado",
             x.get("padre_sugerido") is None and x.get("padre_sugerido_crudo") == "Sujeto_acreedor_del_exterior"
             and cont(r, "padre_sugerido", "fuera_de_catalogo_anulado") == 1)
    c10 = ch["ext::10.4.2.7"]
    r = V.validar({"entities": [ent("to", "TextoOrdenado", "Exterior y cambios", "10.4.2.7"),
                                ent("e1", "Restriccion", "Tope", "10.4.2.7", {"descripcion": "x", "tipo": "prohibicion"})],
                   "relations": [rel("aplica_a", "10.4.2.7", source="e1", sujeto_id="Sujeto_persona_juridica",
                                     sujeto_propuesto="Organizaciones empresariales con participación mayoritaria "
                                                      "del Estado Nacional",
                                     sujeto_propuesto_padre_sugerido="Sujeto_persona_juridica")]}, c10, forma="v3")
    x = r["relaciones"][0] if r["relaciones"] else {}
    chequear(g, "relación con ambos campos (ext::10.4.2.7) → sujeto_id como sugerencia y propuesto como mención",
             x.get("sujeto_id_modelo") == "Sujeto_persona_juridica"
             and (x.get("sujeto_mencion_modelo") or x.get("sujeto_mencion", "")).startswith("Organizaciones")
             and x.get("mencion_verificada") in ("exacta", "tokens", "no") and cont(r, "sujeto", "ambos_campos") == 1,
             f"mencion_verificada={x.get('mencion_verificada')}")
    c11 = ch["ric::11.1.4"]
    r = V.validar({"entities": [ent("to", "TextoOrdenado", "Régimen informativo contable", "11.1.4"),
                                ent("e13", "Obligacion", "Deber", "11.1.4", {"descripcion": "x", "tipo": "otra"})],
                   "relations": [rel("aplica_a", "11.1.4", source="e13", sujeto_id="Sujeto_banco",
                                     sujeto_propuesto_padre_sugerido="Sujeto_entidad_financiera")]}, c11, forma="v3")
    x = r["relaciones"][0] if r["relaciones"] else {}
    chequear(g, "padre sin propuesto (ric::11.1.4, relación 15) → relación aceptada con su sujeto_id, padre "
                "descartado con contador y original",
             not r["rechazos"] and x.get("sujeto_id_modelo") == "Sujeto_banco" and x.get("padre_sugerido") is None
             and x.get("padre_sugerido_crudo") == "Sujeto_entidad_financiera"
             and cont(r, "padre_sugerido", "sin_mencion_descartado") == 1)
    c9 = ch["ext::9.1.2"]
    r = V.validar({"entities": [ent("to", "TextoOrdenado", "Exterior y cambios", "9.1.2"),
                                ent("e1", "Operacion", "Op", "9.1.2", {"tipo": "t"})],
                   "relations": [rel("ejecuta", "9.1.2", source_sujeto={"sujeto_id": "Sujeto_entidad_financiera"},
                                     target="e1")]}, c9, forma="v3")
    chequear(g, "relación sin ninguno de los campos (ext::9.1.2) → rechazo con registro",
             motivos(r).get("sujeto_extremo_ausente") == 1 and not r["relaciones"]
             and cont(r, "campos_del_item_relacion", "a_campos_no_definidos") == 1)
    r = V.validar({"entities": [to, ent("e1", "Obligacion", "Deber", pt, {"descripcion": "x", "tipo": "otra"})],
                   "relations": [rel("aplica_a", pt, source="e1", sujeto_id="Sujeto_inexistente")]}, c, forma="v3")
    x = r["relaciones"][0] if r["relaciones"] else {}
    chequear(g, "sujeto_id fuera del catálogo → relación conservada y pendiente id_fuera_de_catalogo (P-a3)",
             x.get("sujeto_id_modelo") is None and x.get("originales", {}).get("sujeto_id") == "Sujeto_inexistente"
             and r["pendientes_no_mapeados"] and r["pendientes_no_mapeados"][0]["motivo"] == "id_fuera_de_catalogo")

    # omisiones
    r = V.validar({"entities": [to], "relations": [], "omisiones_no_prosa": "\n"}, c, forma="v3")
    chequear(g, "omisiones_no_prosa = '\\n' → vacío equivale a ausente, contado",
             r["omisiones"] == [] and r["adaptacion_v3"].get("omisiones_string_vacio") == 1)
    r = V.validar({"entities": [to], "relations": [], "omisiones_no_prosa": ["\n", "tabla de tasas: no extraída"]},
                  c, forma="v3")
    chequear(g, "omisiones_no_prosa con un string vacío y uno no vacío → una omisión sin categoría ni tramo",
             len(r["omisiones"]) == 1 and r["omisiones"][0]["categoria"] is None
             and r["omisiones"][0]["tramo"] is None and r["adaptacion_v3"].get("omision_v3_string_vacio") == 1)
    r = V.validar({"entities": [to], "relations": [], "omisiones_no_prosa": "tabla de ponderadores"}, c, forma="v3")
    chequear(g, "omisiones_no_prosa string no vacío → lista de un elemento (P-a10)",
             len(r["omisiones"]) == 1 and r["adaptacion_v3"].get("omisiones_string_a_lista_de_uno") == 1)

    # frecuencia
    for valor, esperado, trat in (("mensualmente", "mensual", "normalizado_desde_tramo"),
                                  ("trimestral", "trimestral", "en_lista"),
                                  ("mensual y trimestral", "mensual y trimestral", "registrado_fuera_de_lista"),
                                  ("periódicamente", "periódicamente", "registrado_fuera_de_lista")):
        r = V.validar({"entities": [to, ent("e1", "Obligacion", "Informar", pt,
                                            {"descripcion": "x", "tipo": "reporte_al_supervisor", "frecuencia": valor})],
                       "relations": []}, c, forma="v3")
        e = r["entidades"][1]
        chequear(g, f"Obligacion.frecuencia {valor!r} → {esperado!r} ({trat})",
                 e["properties"]["frecuencia"] == esperado and cont(r, "Obligacion.frecuencia", trat) == 1
                 and (("frecuencia" in e["fuera_de_lista"]) == (trat == "registrado_fuera_de_lista")))


def g4_reglas():
    g = "G4 reglas de comparación"
    casos = [
        # (tramo, comparación esperada, regla esperada)
        ("que superen el 5%", "minimo_estricto", "simple:raiz_super"),
        ("cuando excedan el 10%", "minimo_estricto", "simple:raiz_exced"),
        ("por un importe superior al 3%", "minimo_estricto", "simple:raiz_super"),
        ("en más de 30 días", "minimo_estricto", "simple:mas_de"),
        ("por montos mayores a $ 1.000", "minimo_estricto", "simple:mayor"),
        ("por un monto mayor al 5%", "minimo_estricto", "simple:mayor"),
        ("en mayor medida, el 5%", "no_determinada", "sin_marcador"),
        ("el menor entre 1 año y el plazo residual", "no_determinada", "sin_marcador_plazo"),
        ("el límite inferior del 3%", "no_determinada", "sin_marcador"),
        ("a tasas inferiores al 2%", "maximo_estricto", "simple:inferior"),
        ("en menos de 90 días", "maximo_estricto", "simple:menos_de"),
        ("por importes menores a USD 200", "maximo_estricto", "simple:menor"),
        ("no podrá superar el 5%", "maximo_inclusivo", "negacion:raiz_super"),
        ("no podrán ser superiores al 3%", "maximo_inclusivo", "negacion:raiz_super"),
        ("sin exceder el 20%", "maximo_inclusivo", "negacion:raiz_exced"),
        ("no podrá ya nunca superar el 1%", "maximo_inclusivo", "negacion:raiz_super"),
        # U-R2-CODIGO-2, C2, punto i: «ningún» niega (antes, «no» a cuatro palabras quedaba fuera de alcance)
        ("no podrá en ningún caso superar el 1%", "maximo_inclusivo", "negacion:raiz_super"),
        ("no inferior al 8%", "minimo_inclusivo", "negacion:inferior"),
        ("no menos de 180 días", "minimo_inclusivo", "negacion:menos_de"),
        ("no más de 2 veces", "maximo_inclusivo", "negacion:mas_de"),
        ("igual o superior al 10%", "minimo_inclusivo", "compuesta:igual_o_superior"),
        ("igual o mayor a 2 veces", "minimo_inclusivo", "compuesta:igual_o_superior"),
        ("igual o inferior al 5%", "maximo_inclusivo", "compuesta:igual_o_inferior"),
        ("igual o menor a 30 días", "maximo_inclusivo", "compuesta:igual_o_inferior"),
        ("como máximo 30 días", "maximo_inclusivo", "compuesta:como_maximo"),
        ("en 30 días como máximo", "maximo_inclusivo", "compuesta:como_maximo"),
        ("hasta el 25%", "maximo_inclusivo", "compuesta:hasta"),
        ("dentro de los 10 días hábiles", "maximo_inclusivo", "compuesta:dentro_de"),
        ("al menos 2 años", "minimo_inclusivo", "compuesta:al_menos"),
        ("como mínimo el 50%", "minimo_inclusivo", "compuesta:como_minimo"),
        ("vida promedio mínima 2 años", "minimo_inclusivo", "compuesta:adyacencia_minimo"),
        ("un máximo del 40%", "maximo_inclusivo", "compuesta:adyacencia_maximo"),
        ("montos máximos de $ 500.000", "maximo_inclusivo", "compuesta:adyacencia_maximo"),
        ("plazo mínimo de 10 días hábiles", "minimo_inclusivo", "compuesta:adyacencia_minimo"),
        ("un mínimo de 3 meses", "minimo_inclusivo", "compuesta:un_minimo_de"),
        ("la exigencia de capital mínimo de las entidades será de $ 12.000", "no_determinada", "sin_marcador"),
        ("la Superintendencia de Entidades Financieras fijará el 5%", "no_determinada", "sin_marcador"),
        ("la Superintendencia podrá fijar un plazo de 30 días", "no_determinada", "sin_marcador_plazo"),
        ("aplicará un ponderador de riesgo del 2 %", "coeficiente", "coeficiente"),
        ("un ponderador del 100% a las exposiciones que no superen", "coeficiente", "coeficiente"),
        ("no sea igual o superior al 30%", "maximo_estricto", "negacion:igual_o_superior"),
        ("en un plazo de 30 días", "no_determinada", "sin_marcador_plazo"),
        ("el 5% del total", "no_determinada", "sin_marcador"),
    ]
    for tramo, comp, regla in casos:
        c = una(tramo)
        chequear(g, f"{tramo!r} → {comp} ({regla})", c is not None and c.comparacion == comp and c.regla == regla,
                 "" if c is None else f"{c.comparacion} {c.regla}")
    c = una("en un plazo de 30 días")
    chequear(g, "plazo sin marcador: no_determinada, sin comparacion_asumida (enmienda 3)",
             c.comparacion == "no_determinada" and c.comparacion_asumida is False)
    c = una("el 5% del total")
    chequear(g, "otra cuantía sin marcador: no_determinada, sin comparacion_asumida", c.comparacion_asumida is False)
    # adyacencia: un marcador fuera del tramo (en la descripción) no cuenta
    c = una("el 5%", "Las entidades que superen el 5% deberán informar.")
    chequear(g, "adyacencia: el marcador en la descripción, fuera del tramo, no cuenta", c.comparacion == "no_determinada")
    largo = "las financiaciones que superen en conjunto y por cada uno de los deudores del grupo económico el 5%"
    c = una(largo)
    chequear(g, f"adyacencia: un marcador a más de {RC.VENTANA_ANTES} palabras de la cuantía no cuenta",
             c.comparacion == "no_determinada", f"{c.comparacion} {c.regla}")
    c = una("el 5%", None, "Ponderadores de riesgo.")
    chequear(g, "coeficiente desde el título del punto", c.comparacion == "coeficiente" and c.fuente_marcador == "titulo")
    c = una("el 5%", "Se aplicará un ponderador del 5%.")
    chequear(g, "coeficiente («ponderador») desde la descripción",
             c.comparacion == "coeficiente" and c.fuente_marcador == "descripcion")
    c = una("el 5%", "Se aplicará un factor de conversión del 5%.")
    chequear(g, "«factor» desde la descripción no cuenta (calibración P3)", c.comparacion == "no_determinada")
    cs = RC.analizar("el menor entre 1 año y el plazo residual, con un plazo mínimo de 10 días hábiles")
    chequear(g, "dos cuantías en un tramo: cada una con su ventana; «el menor entre 1 año» sin marcador, "
                "plazo no_determinada y sin comparacion_asumida (enmienda 3)",
             len(cs) == 2 and cs[1].comparacion == "minimo_inclusivo" and cs[0].regla == "sin_marcador_plazo"
             and cs[0].comparacion == "no_determinada" and cs[0].comparacion_asumida is False)
    chequear(g, "precedencia: «no inferior a» (negación) sobre «inferior a» (simple)",
             una("no inferior al 8%").comparacion == "minimo_inclusivo"
             and una("inferior al 8%").comparacion == "maximo_estricto")
    chequear(g, "precedencia: «igual o superior» (compuesta) sobre «superior» (simple)",
             una("igual o superior al 10%").comparacion == "minimo_inclusivo")
    # U-R2-CODIGO-2, C2, punto j: el comparador pegado a la cuantía pisa al coeficiente; sin comparador pegado,
    # el coeficiente sigue primero
    chequear(g, "precedencia: comparador pegado a la cuantía sobre coeficiente (punto j); sin él, coeficiente "
                "sobre negación",
             una("el ponderador no podrá superar el 50%").comparacion == "maximo_inclusivo"
             and una("el ponderador del 50% no podrá superarse").comparacion == "coeficiente")
    chequear(g, "precedencia: negación sobre compuesta",
             una("hasta que no superen el 5%").regla == "negacion:raiz_super")
    chequear(g, "«Superintendencia», «superficie» y «supervisión» no son marcadores de la raíz super-",
             all(una(t).regla == "sin_marcador" for t in ("la Superintendencia fijará el 5%",
                                                          "una superficie del 5%", "la supervisión del 5%")))
    chequear(g, "«excedente» no es marcador de la raíz exced-", una("el excedente del 5%").regla == "sin_marcador")
    # cuantías: valor y unidad
    cs = RC.analizar("365 (trescientos sesenta y cinco) días corridos")
    chequear(g, "cuantía con texto entre paréntesis: 365 días corridos",
             len(cs) == 1 and cs[0].valor == "365" and cs[0].unidad == "dias" and cs[0].dias_tipo == "corridos")
    cs = RC.analizar("el 30% (treinta por ciento) de los ingresos")
    chequear(g, "cuantía repetida entre paréntesis se cuenta una vez", len(cs) == 1 and cs[0].valor == "30")
    cs = RC.analizar("USD 200 mensuales y $ 1.500.000 y 2 millones de pesos y 10.000 UVA")
    chequear(g, "montos: moneda con código y UVA",
             [(x.valor, x.unidad, x.moneda) for x in cs] == [("200", "moneda", "USD"), ("1500000", "moneda", "ARS"),
                                                              ("2000000", "moneda", "ARS"), ("10000", "uva", None)],
             str([(x.valor, x.unidad, x.moneda) for x in cs]))
    cs = RC.analizar("dentro de las 48 horas")
    chequear(g, "unidad fuera de lista (horas): marcada, sin descartar",
             len(cs) == 1 and cs[0].unidad == "horas" and cs[0].fuera_de_lista == ["unidad"]
             and M.ElementoUmbral.model_validate(RC.elemento_umbral(cs[0], "dentro de las 48 horas")) is not None)
    chequear(g, "«igual al» y «equivalente al» pegados dan igual; «será del» no",
             una("igual al 5%").comparacion == "igual" and una("equivalente al 5%").comparacion == "igual"
             and una("será del 5%").comparacion == "no_determinada")


def g5_control(ch):
    g = "G5 casos de control"
    datos = json.loads(EJEMPLO_PRESTAMO.read_text(encoding="utf-8"))["textos"]["cla::5.1.1.1"]
    c0 = ch["cla::5.1.1.1"]
    chequear(g, "préstamo: texto de E0 del ejemplo = texto de E0 de cla::5.1.1.1 (sha256_propio)",
             datos["sha256_propio"] == c0["sha256_propio"] and datos["texto_campo"] == c0["texto"])
    tramo = "superen el equivalente a dos veces el importe de referencia establecido en el punto 3.7."
    chequear(g, "préstamo: el tramo es subcadena normalizada del texto de E0",
             V.verificar_tramo(tramo, c0["texto"], 0)[0] == "exacta")
    cs = RC.analizar(tramo, c0["texto"], c0["titulo"])
    x = cs[0] if cs else None
    chequear(g, "préstamo → mínimo estricto, valor 2, unidad «veces», base «importe de referencia establecido "
                "en el punto 3.7»",
             len(cs) == 1 and x.comparacion == "minimo_estricto" and x.valor == "2" and x.unidad == "veces"
             and x.base == "importe de referencia establecido en el punto 3.7",
             "" if x is None else f"{x.comparacion} {x.valor} {x.unidad} {x.base!r}")
    cs = RC.analizar(c0["texto"], c0["texto"], c0["titulo"])
    chequear(g, "préstamo sobre el texto completo de E0: el mismo resultado",
             len(cs) == 1 and cs[0].comparacion == "minimo_estricto"
             and cs[0].base == "importe de referencia establecido en el punto 3.7")
    filas = {r["n_sorteo"]: r for r in csv.DictReader(open(LECTURA_LIMITA, encoding="utf-8-sig"))}
    control = [("9", "cap::2.8.3.2", "no deberá superar el 0,2%", "0.2", "maximo_inclusivo"),
               ("21", "cap::2.12.2.3", "no excedan, al momento de los acuerdos, del 30%", "30", "maximo_inclusivo"),
               ("15", "cap::4.3.3.1", "con un plazo mínimo de 10 días hábiles", "10", "minimo_inclusivo")]
    for fila, cid, tramo, valor, comp in control:
        f = filas[fila]
        c = ch[cid]
        chequear(g, f"fila {fila}: chunk {cid} = el de la lectura", f["chunk_ids"] == cid)
        chequear(g, f"fila {fila}: el tramo está en el texto de E0 y en la descripción",
                 V.verificar_tramo(tramo, c["texto"], 0)[0] == "exacta"
                 and V.verificar_tramo(tramo, f["restriccion_descripcion"], 0)[0] == "exacta")
        cs = RC.analizar(tramo, f["restriccion_descripcion"], c["titulo"])
        x = [y for y in cs if y.valor == valor]
        chequear(g, f"fila {fila} → {comp} (tramo)", len(x) == 1 and x[0].comparacion == comp,
                 "" if not x else f"{x[0].comparacion} {x[0].regla}")
        cs = RC.analizar(f["restriccion_descripcion"], f["restriccion_descripcion"], c["titulo"])
        x = [y for y in cs if y.valor == valor]
        chequear(g, f"fila {fila} → {comp} (descripción completa, camino de r2a)",
                 len(x) == 1 and x[0].comparacion == comp, "" if not x else f"{x[0].comparacion} {x[0].regla}")
        if fila == "15":
            uno = [y for y in cs if y.valor == "1" and y.unidad == "anios"]
            chequear(g, "fila 15: «el menor entre 1 año» queda sin marcador, plazo no_determinada y sin "
                        "comparacion_asumida (enmienda 3)",
                     len(uno) == 1 and uno[0].regla == "sin_marcador_plazo" and uno[0].comparacion == "no_determinada"
                     and uno[0].comparacion_asumida is False)
        if fila == "21":
            chequear(g, "fila 21: no dispara coeficiente (ni tramo, ni descripción, ni título del punto)",
                     all(y.regla != "coeficiente" for y in cs))


def g6_bkl_e3(ch):
    g = "G6 BKL-0038 y no verificada E3"
    c = ch["cla::5.1.1.1"]
    pt = "5.1.1.1"
    to = ent("to", "TextoOrdenado", "Clasificación de deudores", pt)
    op = ent("op", "Operacion", "Créditos", pt, {"tipo": "credito"})
    casos = [("prohibicion", "limita", "incoherente"), ("limite_cuantitativo", "limita", "coherente"),
             ("prohibicion", "prohibe", "coherente"), ("limite_cualitativo", "prohibe", "incoherente"),
             ("limite_temporal", "limita", "coherente"), ("obligacion_cualitativa", "limita", "no_evaluable")]
    for tipo, pred, esperado in casos:
        r = V.validar({"entities": [to, op, ent("e1", "Restriccion", "R", pt, {"descripcion": "x", "tipo": tipo})],
                       "relations": [rel(pred, pt, source="e1", target="op")]}, c, forma="v3")
        x = r["relaciones"][0] if r["relaciones"] else {}
        chequear(g, f"Restriccion {tipo} --{pred}--> : {esperado}, sin rechazar",
                 x.get("coherencia_tipo_predicado") == esperado and not r["rechazos"])
    cond = ent("c1", "Condicion", "Si supera", pt, {"descripcion": "cuando superen"})
    pot = ent("p1", "Potestad", "Podrá", pt, {"descripcion": "podrá"})
    ob = ent("o1", "Obligacion", "Deberá", pt, {"descripcion": "deberá", "tipo": "otra"})
    de = ent("d1", "Definicion", "Def", pt, {"termino": "t", "descripcion": "d"})
    r = V.validar({"entities": [to, op, cond, pot, ob, de],
                   "relations": [rel("condicion_de", pt, source="c1", target="op"),
                                 rel("condicion_de", pt, source="c1", target="p1"),
                                 rel("condicion_de", pt, source="c1", target="o1"),
                                 rel("condicion_de", pt, source="c1", target="d1")]}, c, forma="v3")
    marcas = {(x["target"]): x["no_verificada_e3"] for x in r["relaciones"]}
    chequear(g, "condicion_de → Operacion y → Potestad: aceptadas con no_verificada_e3",
             marcas.get("op") is True and marcas.get("p1") is True)
    chequear(g, "condicion_de → Obligacion (firma congelada): sin la marca", marcas.get("o1") is False)
    chequear(g, "condicion_de → Definicion: fuera de la matriz r2, rechazo firma_invalida",
             "d1" not in marcas and motivos(r).get("firma_invalida") == 1)
    try:
        M.RelacionR2(source="c1", target="op", predicate="condicion_de", punto=pt, provenance=M.Provenance(),
                     tipo_source="Condicion", tipo_target="Operacion", no_verificada_e3=False)
        chequear(g, "modelo: una firma nueva sin la marca no valida", False)
    except ValidationError:
        chequear(g, "modelo: una firma nueva sin la marca no valida", True)


def g7_mencion_omision(ch):
    g = "G7 mención y omisiones"
    c = ch["cla::5.1.1.1"]
    pt = "5.1.1.1"
    to = ent("to", "TextoOrdenado", "Clasificación de deudores", pt)
    ob = ent("e1", "Obligacion", "Incluir", pt, {"descripcion": "x", "tipo": "otra"})
    casos = [("del cliente", "Sujeto_cliente", "exacta"),
             ("cliente periódicos", "Sujeto_cliente", "tokens"),
             ("evolución del cliente", None, "no"),
             ("empresas no financieras emisoras", None, "no"),
             (None, "Sujeto_cliente", "ausente")]
    for mencion, sid, nivel in casos:
        kw = {"source": "e1"}
        if mencion is not None:
            kw["sujeto_mencion"] = mencion
        if sid is not None:
            kw["sujeto_id"] = sid
        r = V.validar({"entities": [to, ob], "relations": [rel("aplica_a", pt, **kw)]}, c, forma="r2")
        x = r["relaciones"][0] if r["relaciones"] else {}
        chequear(g, f"mención {mencion!r} → {nivel}, relación aceptada", x.get("mencion_verificada") == nivel,
                 str(x.get("mencion_verificada")))
        if nivel == "tokens":
            lit = x.get("sujeto_mencion")
            chequear(g, f"mención {mencion!r}: tramo literal mínimo del texto y la del modelo guardada",
                     x.get("sujeto_mencion_modelo") == mencion and lit != mencion
                     and V.verificar_tramo(lit, c["texto"], 0)[0] == "exacta", repr(lit))
        if nivel == "no":
            chequear(g, "mención no verificada y sin sugerencia → pendiente mencion_no_verificada",
                     r["pendientes_no_mapeados"] and r["pendientes_no_mapeados"][0]["motivo"] == "mencion_no_verificada")
    lejos = "ingresos cartera"   # «ingresos» y «cartera» están a más de 2 + holgura tokens
    r = V.validar({"entities": [to, ob], "relations": [rel("aplica_a", pt, source="e1", sujeto_mencion=lejos)]},
                  c, forma="r2")
    chequear(g, "mención con tokens dispersos más allá de la ventana → no (aceptada)",
             r["relaciones"] and r["relaciones"][0]["mencion_verificada"] == "no")
    chequear(g, "verificar_tramo sin tope de ventana (holgura None) acepta los tokens dispersos",
             V.verificar_tramo(lejos, V.texto_completo(c), None)[0] == "tokens")
    chequear(g, "R-NORM: une el corte por guion «pro-\\nductiva»",
             V.verificar_tramo("actividad productiva", c["texto"], 0)[0] == "exacta")
    oms = [{"categoria": "tabla", "tramo": "importe de referencia establecido en el punto 3.7", "nota": "n"},
           {"categoria": "formula", "tramo": "importe referencia", "nota": "n"},
           {"categoria": "meta_normativo", "tramo": "texto que no está en el punto", "nota": "n"},
           {"categoria": "otra_cosa", "tramo": "cartera comercial", "nota": "n"},
           {"categoria": "meta_normativo", "tramo": "cartera", "nota": "n"},
           {"categoria": "tabla", "tramo": "Los créditos de esta clase que superen el equivalente a dos veces el "
                                           "importe de referencia", "nota": "n"}]
    r = V.validar({"entities": [to], "relations": [], "omisiones": oms}, c, forma="r2")
    O = r["omisiones"]
    chequear(g, "omisión con tramo literal → exacta; tabla en chunk sin marca → señal de tabla no detectada",
             O[0]["tramo_verificado"] == "exacta" and O[0]["senal_tabla_no_detectada"] is True)
    chequear(g, "omisión con tramo por tokens → tramo literal mínimo y el del modelo guardado",
             O[1]["tramo_verificado"] == "tokens" and O[1]["tramo_modelo"] == "importe referencia"
             and O[1]["tramo"] == "importe de\nreferencia")
    chequear(g, "omisión con tramo ajeno al texto → no, conservada", O[2]["tramo_verificado"] == "no" and len(O) == 6)
    chequear(g, "categoría fuera de lista → registrada con marca", O[3]["fuera_de_lista"] == ["categoria"]
             and O[3]["categoria"] == "otra_cosa")
    chequear(g, f"tramo de menos de {V.politica_default().largo_min_omision} tokens → tramo_corto, sin rechazo "
                "(1 y 9 tokens marcados; 15 tokens no)",
             O[4]["tramo_corto"] is True and O[0]["tramo_corto"] is True and O[5]["tramo_corto"] is False
             and not r["rechazos"])
    chequear(g, "el tramo de prueba del heredado: no está en el texto propio y sí en el completo (con P3c, g, la "
                "omisión lo verifica: G16)",
             V.verificar_tramo("Categorías de carteras", c["texto"], 0)[0] == "no"
             and V.verificar_tramo("Categorías de carteras", V.texto_completo(c), 0)[0] == "exacta")


def g10_calibracion(ch):
    g = "G10 calibración P3"
    casos = [
        ("por lo menos 180 días", "minimo_inclusivo", "compuesta:por_lo_menos"),
        ("deberá permanecer en esta categoría por lo menos 180 días", "minimo_inclusivo", "compuesta:por_lo_menos"),
        ("180 días por lo menos", "minimo_inclusivo", "compuesta:por_lo_menos"),
        ("30 días o más", "minimo_inclusivo", "compuesta:o_mas"),
        ("el 5 % o más de", "minimo_inclusivo", "compuesta:o_mas"),
        ("30 días o menos", "maximo_inclusivo", "compuesta:o_menos"),
        ("no superaba USD 500.000", "maximo_inclusivo", "negacion:raiz_super"),
        ("el monto total adeudado no superaba USD 500.000", "maximo_inclusivo", "negacion:raiz_super"),
        ("no excedía el 3%", "maximo_inclusivo", "negacion:raiz_exced"),
        ("cuando superaren el 5%", "minimo_estricto", "simple:raiz_super"),
        ("sea menor o igual al equivalente a USD 500.000", "maximo_inclusivo", "compuesta:menor_o_igual"),
        ("inferior o igual al 2%", "maximo_inclusivo", "compuesta:menor_o_igual"),
        ("mayor o igual al 10%", "minimo_inclusivo", "compuesta:mayor_o_igual"),
        ("superior o igual al 10%", "minimo_inclusivo", "compuesta:mayor_o_igual"),
        ("no sea menor o igual al 5%", "minimo_estricto", "negacion:menor_o_igual"),
        ("inferior al 2%", "maximo_estricto", "simple:inferior"),
        ("mayor al 5%", "minimo_estricto", "simple:mayor"),
        ("menores al 10%", "maximo_estricto", "simple:menor"),
        ("la supervisión dispondrá de 30 días", "no_determinada", "sin_marcador_plazo"),
        ("la Superintendencia, la superficie, el superávit y el excedente del 5%", "no_determinada", "sin_marcador"),
        ("Multa equivalente al 4% del valor rechazado", "igual", "igual:equivalente_a"),
        ("La deducción será equivalente al 100% del valor", "igual", "igual:equivalente_a"),
        ("Límite máximo equivalente a USD 100", "no_determinada", "sin_marcador"),
        ("a razón de un máximo mensual equivalente al 10%", "no_determinada", "sin_marcador"),
        ("Multa equivalente al 4% del valor rechazado con mínimo $100 y máximo $50.000", "igual",
         "igual:equivalente_a"),
        ("El cliente no supere, en el mes calendario en el conjunto de las entidades y por el conjunto de los "
         "conceptos señalados, el equivalente a USD 200", "no_determinada", "sin_marcador"),
        ("el límite del 25%", "no_determinada", "sin_marcador"),
        ("un tope de $ 1.000", "no_determinada", "sin_marcador"),
        ("un máximo general del 25%", "no_determinada", "sin_marcador"),
        ("entre el 10% y el 20%", "no_determinada", "sin_marcador"),
        ("se empleará un factor de 15%", "coeficiente", "coeficiente"),
    ]
    for tramo, comp, regla in casos:
        c = una(tramo)
        chequear(g, f"{tramo!r} → {comp} ({regla})", c is not None and c.comparacion == comp and c.regla == regla,
                 "" if c is None else f"{c.comparacion} {c.regla}")
    c = una("la supervisión dispondrá de 30 días")
    chequear(g, "«supervisión … 30 días»: plazo sin marcador, no_determinada y sin comparacion_asumida (enmienda 3)",
             c.comparacion == "no_determinada" and c.comparacion_asumida is False)
    # «hasta» temporal no excluye «igual»; desde C2 de U-R2-CODIGO-2 (punto c), el ordinal tras «hasta el» es una
    # cuantía (36 meses, máximo inclusivo) y el 10% es la segunda
    t = ("A partir del segundo y hasta el trigésimo sexto mes, la exigencia mensual será equivalente al 10% del "
         "promedio")
    c0, c1 = una(t), una(t, i=1)
    chequear(g, f"{t!r} → 36 meses, maximo_inclusivo (compuesta:hasta); 10% → igual (igual:equivalente_a)",
             c0 is not None and (c0.valor, c0.unidad, c0.comparacion, c0.regla) == ("36", "meses", "maximo_inclusivo",
                                                                                 "compuesta:hasta")
             and c1 is not None and (c1.comparacion, c1.regla) == ("igual", "igual:equivalente_a"))
    # «factor» tomado de la descripción: los dos falsos positivos reales de P2.
    sha_kg = {"diez": "dd42d6d9c0c8379da90ec4ed4e4659157a960a0d1ceaf8af5a008bdd9cad9010",
              "r1": "0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a"}
    rutas = {"diez": "data/experiment/reextraccion_v2/corpus_tanda0/ens_diez/r1/kg.json",
             "r1": "data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json"}
    frases = {"diez": ("factor igual a 4", "5%", "minimo_estricto", "simple:raiz_super"),
              "r1": ("por el factor correspondiente", "cinco días hábiles", "no_determinada", "sin_marcador_plazo")}
    for gr, (frase, cuantia, comp, regla) in frases.items():
        p = REPO / rutas[gr]
        if M.sha256_archivo(p) != sha_kg[gr]:
            chequear(g, f"grafo {gr} con el sha256 de N1", False)
            continue
        kg = json.loads(p.read_text(encoding="utf-8"))
        nodos = [n for n in kg["nodes"] if frase in ((n.get("properties") or {}).get("descripcion") or "")]
        ok = bool(nodos)
        for n in nodos:
            d = n["properties"]["descripcion"]
            cid = next((pv.get("chunk_id") for pv in n.get("provenances") or [] if pv.get("chunk_id")), None)
            titulo = ch[cid]["titulo"] if cid in ch else None
            cs = [x for x in RC.analizar(d, d, titulo) if x.texto == cuantia]
            ok = ok and len(cs) == 1 and cs[0].comparacion == comp and cs[0].regla == regla
        chequear(g, f"«factor» de la descripción ({gr}, «{frase}»): {cuantia} → {comp}, no coeficiente "
                    f"({len(nodos)} nodos)", ok)
    # Omisiones: string con forma de lista JSON (caso real de r1 L0r, cap::7.3::intro).
    c = ch["cla::5.1.1.1"]
    to = ent("to", "TextoOrdenado", "Clasificación de deudores", "5.1.1.1")
    r = V.validar({"entities": [to], "relations": [], "omisiones_no_prosa": '["tabla de tasas", "fórmula del cálculo"]'},
                  c, forma="v3")
    chequear(g, "omisiones_no_prosa string con forma de lista JSON → dos omisiones (decodificada)",
             len(r["omisiones"]) == 2 and r["adaptacion_v3"].get("omisiones_string_lista_json_decodificada") == 1)
    r = V.validar({"entities": [to], "relations": [], "omisiones_no_prosa": "[tabla: no extraída"}, c, forma="v3")
    chequear(g, "string que no es una lista JSON válida → lista de uno (P-a10)",
             len(r["omisiones"]) == 1 and r["adaptacion_v3"].get("omisiones_string_a_lista_de_uno") == 1)


def g8_modelos():
    g = "G8 modelos"
    base = dict(tramo="el 5%", valor="5", unidad="porcentaje", comparacion="no_determinada")
    chequear(g, "ElementoUmbral válido", M.ElementoUmbral(**base) is not None)
    for campo, valor in (("comparacion", "tope"), ("unidad", "horas")):
        try:
            M.ElementoUmbral(**{**base, campo: valor})
            chequear(g, f"ElementoUmbral: {campo} fuera de lista sin marca no valida", False)
        except ValidationError:
            chequear(g, f"ElementoUmbral: {campo} fuera de lista sin marca no valida", True)
        x = M.ElementoUmbral(**{**base, campo: valor, "fuera_de_lista": [campo]})
        chequear(g, f"ElementoUmbral: {campo} fuera de lista con marca se conserva", getattr(x, campo) == valor)
    try:
        M.ElementoUmbral(**{**base, "comparacion_asumida": True})
        chequear(g, "comparacion_asumida fuera de un plazo no valida", False)
    except ValidationError:
        chequear(g, "comparacion_asumida fuera de un plazo no valida", True)
    prov = M.Provenance(to="cla", archivo="a.pdf", punto="1", rol_documental="punto_propio")
    try:
        M.EntidadR2(local_id="e1", type="Restriccion", label="R", punto="1", provenance=prov,
                    properties={"descripcion": "x", "plazo_o_frecuencia": "m"})
        chequear(g, "EntidadR2: clave fuera de la definición en properties no valida (LN-2)", False)
    except ValidationError:
        chequear(g, "EntidadR2: clave fuera de la definición en properties no valida (LN-2)", True)
    try:
        M.EntidadR2(local_id="e1", type="Restriccion", label="R", punto="1", provenance=prov,
                    properties={"descripcion": "x", "tipo": "limite_temporal"})
        chequear(g, "EntidadR2: Restriccion.tipo fuera de lista sin marca no valida (LN-1)", False)
    except ValidationError:
        chequear(g, "EntidadR2: Restriccion.tipo fuera de lista sin marca no valida (LN-1)", True)
    try:
        M.OmisionR2(categoria=None, tramo=None, origen="e1", tramo_verificado="ausente")
        chequear(g, "OmisionR2: sin categoría y sin marca, fuera del crudo v3, no valida", False)
    except ValidationError:
        chequear(g, "OmisionR2: sin categoría y sin marca, fuera del crudo v3, no valida", True)
    n = M.NodoR2(id="Restriccion_x", type="Restriccion", label="R",
                 properties={"descripcion": "x", "tipo": "limite_cuantitativo",
                             "umbrales": [RC.elemento_umbral(RC.analizar("no podrá superar el 5%")[0],
                                                             "no podrá superar el 5%", "descripcion")]})
    chequear(g, "NodoR2 con la lista de umbrales en properties", n.properties["umbrales"][0]["comparacion"]
             == "maximo_inclusivo")
    try:
        M.AristaR2(source="a", target="b", relation="limita")
        chequear(g, "AristaR2 limita sin coherencia_tipo_predicado no valida", False)
    except ValidationError:
        chequear(g, "AristaR2 limita sin coherencia_tipo_predicado no valida", True)


def g9_tool_schema(ch):
    g = "G9 tool schema"
    import jsonschema  # noqa: PLC0415
    cont = G.contenidos()
    for nombre, b in cont.items():
        p = G.GENERADOS / nombre
        chequear(g, f"{nombre}: regenerado = archivo en generados/", p.exists() and p.read_bytes() == b)
    man = json.loads((G.GENERADOS / "manifest_generados_r2.json").read_text(encoding="utf-8"))
    chequear(g, "manifest: sha256 de la política vigente y de modelos_r2 de la generación vigente (U-PROMPT-R2 P3)",
             man["politica"]["sha256"] == M.sha256_archivo(V.POLITICA)
             and man["modelos"]["sha256"] == MODELOS_SHA_GENERACION)
    ts = json.loads(cont["tool_schema_r2.json"])
    sch = ts["input_schema"]
    jsonschema.Draft202012Validator.check_schema(sch)
    chequear(g, "input_schema es JSON Schema válido (draft 2020-12)", True)
    rel_items = sch["properties"]["relations"]["items"]["properties"]
    chequear(g, "sujeto_id: enum = catálogo r2 (110), sin sujeto_propuesto; sujeto_mencion presente",
             rel_items["sujeto_id"]["enum"] == list(M.SUJETOS_R2) and "sujeto_propuesto" not in rel_items
             and "sujeto_mencion" in rel_items)
    chequear(g, "omisiones obligatoria, con categoría del enum de cinco", "omisiones" in sch["required"]
             and sch["properties"]["omisiones"]["items"]["properties"]["categoria"]["enum"] == list(M.CATEGORIA_OMISION))
    tipos_items = [x["properties"]["type"]["const"] for x in sch["properties"]["entities"]["items"]["anyOf"]]
    chequear(g, "una forma de entidad por tipo (9), con umbrales en los cuatro tipos",
             tipos_items == list(M.TIPOS_ENTIDAD)
             and [t for t, x in zip(tipos_items, sch["properties"]["entities"]["items"]["anyOf"])
                  if "umbrales" in x["properties"]] == [t for t in M.TIPOS_ENTIDAD if t in M.TIPOS_CON_UMBRALES])
    chequear(g, "otras_propiedades en las 9 formas de entidad: objeto de strings, opcional",
             all(x["properties"].get("otras_propiedades") == {"additionalProperties": {"type": "string"},
                                                              "description": M._DESC_OTRAS, "type": "object"}
                 and "otras_propiedades" not in x["required"]
                 for x in sch["properties"]["entities"]["items"]["anyOf"]))
    formas = {x["properties"]["type"]["const"]: x for x in sch["properties"]["entities"]["items"]["anyOf"]}
    chequear(g, "properties conocidas de cada tipo, cerradas (additionalProperties false), salvo el TextoOrdenado",
             all(x["properties"]["properties"].get("additionalProperties") is False
                 for t, x in formas.items() if t != "TextoOrdenado"))
    chequear(g, "decisión 16: el TextoOrdenado no lleva properties; la Comunicacion solo codigo",
             "properties" not in formas["TextoOrdenado"]["properties"]
             and list(formas["Comunicacion"]["properties"]["properties"]["properties"]) == ["codigo"])
    chequear(g, "decisión 15: tramo obligatorio en los 8 tipos que no son TextoOrdenado, y ausente en él",
             all("tramo" in x["required"] and x["properties"]["tramo"]["type"] == "string"
                 for t, x in formas.items() if t != "TextoOrdenado")
             and "tramo" not in formas["TextoOrdenado"]["properties"])
    chequear(g, "decisión 16: Definicion.termino copiado tal cual",
             "tal cual" in formas["Definicion"]["properties"]["properties"]["properties"]["termino"]["description"])
    rel_props = sch["properties"]["relations"]["items"]["properties"]
    om_props = sch["properties"]["omisiones"]["items"]["properties"]
    chequear(g, "decisión 17: otras_propiedades en las relaciones; source y destino opcionales en la omisión",
             rel_props.get("otras_propiedades", {}).get("type") == "object"
             and "otras_propiedades" not in sch["properties"]["relations"]["items"].get("required", [])
             and {"source", "destino"} <= set(om_props)
             and not {"source", "destino"} & set(sch["properties"]["omisiones"]["items"].get("required", [])))
    c = ch["cla::5.1.1.1"]
    pt = "5.1.1.1"
    valido = {
        "entities": [
            {"local_id": "to", "type": "TextoOrdenado", "label": "Clasificación de deudores", "punto": pt},
            {"local_id": "e1", "type": "Restriccion", "label": "Consumo sobre dos veces el importe", "punto": pt,
             "tramo": "superen el equivalente a dos veces el importe de referencia establecido en el punto 3.7.",
             "properties": {"descripcion": "Los créditos de esta clase que superen el equivalente a dos veces el "
                                           "importe de referencia se incluirán en la cartera comercial.",
                            "tipo": "limite_cuantitativo"},
             "umbrales": [{"tramo": "superen el equivalente a dos veces el importe de referencia establecido en el "
                                    "punto 3.7."}]}],
        "relations": [{"predicate": "establecida_en", "punto": pt, "source": "e1", "target": "to"},
                      {"predicate": "aplica_a", "punto": pt, "source": "e1", "sujeto_mencion": "del cliente",
                       "sujeto_id": "Sujeto_cliente"}],
        "omisiones": []}
    v = jsonschema.Draft202012Validator(sch)
    chequear(g, "elemento válido: pasa el JSON Schema", v.is_valid(valido))
    chequear(g, "elemento válido: pasa SalidaE1R2", M.SalidaE1R2.model_validate(valido) is not None)
    r = V.validar(valido, c, forma="r2")
    chequear(g, "elemento válido: el validador lo acepta entero, sin marcas ni rechazos",
             not r["rechazos"] and len(r["entidades"]) == 2 and len(r["relaciones"]) == 2
             and all(not x["fuera_de_lista"] and not x["properties_no_definidas"] for x in r["entidades"])
             and r["relaciones"][1]["mencion_verificada"] == "exacta")
    umb = r["entidades"][1]["umbrales_tramos"]
    els = [M.ElementoUmbral.model_validate(RC.elemento_umbral(x, umb[0], "e1")) for x in RC.analizar(umb[0])]
    chequear(g, "el tramo del umbral produce un ElementoUmbral válido (mínimo estricto)",
             len(els) == 1 and els[0].comparacion == "minimo_estricto")
    otras = json.loads(json.dumps(valido))
    otras["entities"][1]["otras_propiedades"] = {"destinatario": "BCRA", "tipo": "x"}
    chequear(g, "otras_propiedades: el elemento pasa el JSON Schema", v.is_valid(otras))
    r = V.validar(otras, c, forma="r2")
    e = r["entidades"][1] if len(r["entidades"]) > 1 else {}
    chequear(g, "otras_propiedades → properties_no_definidas con contador; una clave definida del tipo va a "
                "campos_no_definidos; nada se rechaza",
             e.get("properties_no_definidas") == {"destinatario": "BCRA"}
             and {k: x for k, x in (e.get("campos_no_definidos") or {}).items() if k != "tramo"}
             == {"otras_propiedades.tipo": "x"}
             and cont_(r, "claves", "otras_propiedades_a_properties_no_definidas") == 1 and not r["rechazos"])
    # Desde P3 de U-PROMPT-R2, validador_r2 lee el tramo de evidencia (decisión 15): campo conocido, verificado,
    # con su marca en la procedencia (casos en G13).
    chequear(g, "tramo de evidencia (P3): campo conocido, verificado en la procedencia, sin rechazo",
             "tramo" not in (e.get("campos_no_definidos") or {})
             and e.get("provenance", {}).get("tramo_verificado") == "exacta" and not r["rechazos"])
    clave_extra = json.loads(json.dumps(valido))
    clave_extra["entities"][1]["properties"]["destinatario"] = "BCRA"
    chequear(g, "clave no prevista dentro de properties: el JSON Schema la rechaza", not v.is_valid(clave_extra))
    r = V.validar(clave_extra, c, forma="r2")
    e = r["entidades"][1] if len(r["entidades"]) > 1 else {}
    chequear(g, "clave no prevista dentro de properties: el validador la registra, no la descarta",
             e.get("properties_no_definidas") == {"destinatario": "BCRA"} and not r["rechazos"])
    fuera = json.loads(json.dumps(valido))
    fuera["entities"][1]["properties"]["tipo"] = "limite_temporal"
    chequear(g, "valor fuera de lista (Restriccion.tipo limite_temporal): el JSON Schema lo rechaza",
             not v.is_valid(fuera))
    r = V.validar(fuera, c, forma="r2")
    e = r["entidades"][1] if len(r["entidades"]) > 1 else {}
    chequear(g, "valor fuera de lista: el validador lo conserva marcado, no lo descarta",
             e.get("properties", {}).get("tipo") == "limite_temporal" and e.get("fuera_de_lista") == ["tipo"]
             and len(r["relaciones"]) == 2 and not r["rechazos"])
    fuera2 = json.loads(json.dumps(valido))
    fuera2["relations"][0]["predicate"] = "establec ida_en"
    chequear(g, "predicado fuera de lista: el JSON Schema lo rechaza", not v.is_valid(fuera2))
    r = V.validar(fuera2, c, forma="r2")
    chequear(g, "predicado fuera de lista: el validador lo normaliza por forma con contador",
             len(r["relaciones"]) == 2 and cont_(r, "predicado", "normalizado_forma") == 1)


def cont_(res, campo, trat):
    return cont(res, campo, trat)


def g11_remite_a():
    g = "G11 remite_a"
    import hashlib  # noqa: PLC0415
    chequear(g, "remite_a fuera de los 13 predicados de E1", "remite_a" not in M.PREDICADOS
             and len(M.PREDICADOS) == 13 and M.PREDICADOS_DERIVADOS == ("remite_a",))
    chequear(g, "remite_a fuera de la matriz congelada y de la r2",
             "remite_a" not in M.FIRMAS_CONGELADAS and "remite_a" not in M.FIRMAS_R2)
    tipos = M.TIPOS_ENTIDAD + (M.TIPO_SUJETO,)
    firmas = [(s, t) for s in tipos for t in tipos if M.firma_derivada(s, "remite_a", t)]
    chequear(g, "56 firmas: 7 tipos de contenido → 7 tipos de contenido o TextoOrdenado",
             len(firmas) == 56 and {s for s, _ in firmas} == set(M.TIPOS_CONTENIDO)
             and {t for _, t in firmas} == set(M.TIPOS_CONTENIDO) | {"TextoOrdenado"})
    chequear(g, "Comunicacion y Sujeto fuera de la firma, como origen y como destino",
             not any(x in ("Comunicacion", M.TIPO_SUJETO) for f in firmas for x in f))
    prov = M.Provenance(to="cla", archivo="a.pdf", punto="5.1.1.1", rol_documental="punto_propio")
    try:
        M.RelacionR2(source="e1", target="e2", predicate="remite_a", punto="5.1.1.1", provenance=prov,
                     tipo_source="Condicion", tipo_target="Definicion")
        chequear(g, "RelacionR2 no admite remite_a (E1 no lo emite)", False)
    except ValidationError:
        chequear(g, "RelacionR2 no admite remite_a (E1 no lo emite)", True)
    ok = {"alcance": "interna", "destino": "cla::3.7",
          "evidencia": "dos veces el importe de referencia establecido en el punto 3.7"}
    a = M.AristaR2(source="Condicion_x", target="Definicion_y", relation="remite_a", provenance=prov,
                   provenances=[prov], properties=ok)
    chequear(g, "AristaR2 remite_a con alcance, destino y evidencia valida", a.properties == ok)
    chequear(g, "AristaR2 remite_a a un texto ordenado entero valida",
             M.AristaR2(source="Condicion_x", target="TextoOrdenado_t", relation="remite_a",
                        properties={"alcance": "to_entero", "destino": "cap::TO",
                                    "evidencia": "normas sobre Capitales mínimos"}) is not None)
    malas = {
        "alcance fuera de la lista": dict(properties={**ok, "alcance": "cruzada"}),
        "sin evidencia": dict(properties={k: v for k, v in ok.items() if k != "evidencia"}),
        "evidencia vacía": dict(properties={**ok, "evidencia": " "}),
        "to_entero con destino de punto": dict(properties={**ok, "alcance": "to_entero"}),
        "interna con destino de texto ordenado": dict(properties={**ok, "destino": "cla::TO"}),
        "clase de la cita en properties": dict(properties={**ok, "clase": "interna"}),
        "via en properties": dict(properties={**ok, "via": "nodos_del_punto"}),
        "con rol_fuente": dict(properties=ok, rol_fuente="referencia_cruzada"),
        "con no_verificada_e3": dict(properties=ok, no_verificada_e3=True),
        "con sujeto_mencion": dict(properties=ok, sujeto_mencion="las entidades"),
        "con metodo_resolucion": dict(properties=ok, metodo_resolucion="R1_label_exacto"),
        "con mencion_verificada": dict(properties=ok, mencion_verificada="exacta"),
    }
    for nombre, kw in malas.items():
        try:
            M.AristaR2(source="Condicion_x", target="Definicion_y", relation="remite_a", **kw)
            chequear(g, f"AristaR2 remite_a {nombre} no valida", False)
        except ValidationError:
            chequear(g, f"AristaR2 remite_a {nombre} no valida", True)
    try:
        M.AristaR2(source="TextoOrdenado_t", target="Comunicacion_c", relation="referencia", properties={})
        chequear(g, "AristaR2 referencia sin properties de remisión sigue valida", True)
    except ValidationError:
        chequear(g, "AristaR2 referencia sin properties de remisión sigue valida", False)
    cont = G.contenidos()
    chequear(g, "tool schema de E1 byte a byte el de la generación vigente (U-PROMPT-R2 P2)",
             hashlib.sha256(cont["tool_schema_r2.json"]).hexdigest() == TOOL_SCHEMA_SHA_GENERACION)
    chequear(g, "enums r2 byte a byte los de 57a8dd2 (remite_a no entra a las listas de E1)",
             hashlib.sha256(cont["enums_r2.json"]).hexdigest() == ENUMS_SHA_57A8DD2)
    chequear(g, "politica_campos_r2.json con el sha de la decisión 10",
             M.sha256_archivo(V.POLITICA) == POLITICA_SHA_DECISION_10)
    ts = json.loads(cont["tool_schema_r2.json"])
    chequear(g, "el tool schema no menciona remite_a", "remite_a" not in json.dumps(ts))


def g12_ensamblado():
    g = "G12 ensamblado r2"
    import hashlib  # noqa: PLC0415
    sys.path.insert(0, str(REPO / "data" / "experiment" / "grafo_v2" / "code"))
    import schema  # noqa: PLC0415  (módulo sellado: solo import)
    chequear(g, "relaciones del esqueleto = schema.RELACIONES_ESQUELETO",
             M.RELACIONES_ESQUELETO == tuple(schema.RELACIONES_ESQUELETO))
    chequear(g, "esqueleto y padre_sugerido: firma Sujeto → Sujeto y nada más",
             all(M.firma_esqueleto("Sujeto", r, "Sujeto") for r in M.RELACIONES_SUJETO_A_SUJETO)
             and not any(M.firma_esqueleto(a, r, b) for r in M.RELACIONES_SUJETO_A_SUJETO
                         for a, b in (("Operacion", "Sujeto"), ("Sujeto", "Operacion"))))
    chequear(g, "firma_arista reúne la matriz r2, remite_a y el esqueleto",
             M.firma_arista("Condicion", "condicion_de", "Operacion")
             and M.firma_arista("Condicion", "remite_a", "Definicion")
             and M.firma_arista("Sujeto", "subclase_de", "Sujeto")
             and not M.firma_arista("Sujeto", "remite_a", "Sujeto"))
    for r in M.RELACIONES_SUJETO_A_SUJETO:
        chequear(g, f"AristaR2 {r} valida", M.AristaR2(source="Sujeto_a", target="Sujeto_b", relation=r,
                                                         rol_fuente="esqueleto") is not None)
    try:
        M.AristaR2(source="Sujeto_a", target="Sujeto_b", relation="subclase_de", metodo_resolucion="R1_label_exacto")
        chequear(g, "esqueleto con marca de E1 no valida", False)
    except ValidationError:
        chequear(g, "esqueleto con marca de E1 no valida", True)
    chequear(g, "calificador en una arista de sujeto valida",
             M.AristaR2(source="Obligacion_a", target="Sujeto_entidad_financiera", relation="aplica_a",
                        mencion_verificada="exacta", sujeto_mencion="entidades del grupo A",
                        calificador="del grupo a").calificador == "del grupo a")
    try:
        M.AristaR2(source="Condicion_a", target="Operacion_b", relation="condicion_de", calificador="x")
        chequear(g, "calificador fuera de una arista de sujeto no valida", False)
    except ValidationError:
        chequear(g, "calificador fuera de una arista de sujeto no valida", True)
    marcas = {"cola_humana": "true", "cola_chunks": ["cla::3.5.1"], "estado_e3": "cola_humana",
              "colision_cross_to": "true"}
    n = M.NodoR2(id="Operacion_x", type="Operacion", label="O", properties={"descripcion": "d", **marcas})
    chequear(g, "NodoR2 admite las marcas de cola y de colisión, como en los grafos sellados",
             all(n.properties[k] == v for k, v in marcas.items()))
    for nombre, props in (("cola_humana sin estado_e3", {"descripcion": "d", "cola_humana": "true",
                                                         "cola_chunks": ["c"]}),
                          ("colision_cross_to distinto de «true»", {"descripcion": "d", "colision_cross_to": "si"})):
        try:
            M.NodoR2(id="Operacion_x", type="Operacion", label="O", properties=props)
            chequear(g, f"NodoR2: {nombre} no valida", False)
        except ValidationError:
            chequear(g, f"NodoR2: {nombre} no valida", True)
    prov = M.Provenance(to="cla", archivo="a.pdf", punto="1", rol_documental="punto_propio")
    try:
        M.EntidadR2(local_id="e1", type="Operacion", label="O", punto="1", provenance=prov,
                    properties={"descripcion": "d", "cola_humana": "true"})
        chequear(g, "EntidadR2 (salida de E1) no admite las marcas del ensamblado", False)
    except ValidationError:
        chequear(g, "EntidadR2 (salida de E1) no admite las marcas del ensamblado", True)
    base = RC.elemento_umbral(RC.analizar("superen dos veces el importe de referencia establecido en el punto 3.7")[0],
                              "dos veces", "descripcion")
    e = M.ElementoUmbral.model_validate({**base, "base_destino": "cla::3.7", "base_via": "remision",
                                         "verificado_en_tabla": False})
    chequear(g, "ElementoUmbral con la base resuelta y la verificación en tabla",
             e.base_destino == "cla::3.7" and e.base_via == "remision" and e.verificado_en_tabla is False)
    chequear(g, "ElementoUmbral con la marca de base no resuelta",
             M.ElementoUmbral.model_validate({**base, "base_no_resuelta": True}).base_no_resuelta)
    for nombre, extra in (("base_destino sin base_via", {"base_destino": "cla::3.7"}),
                          ("base_no_resuelta con destino", {"base_destino": "cla::3.7", "base_via": "remision",
                                                            "base_no_resuelta": True}),
                          ("base_via fuera de la lista", {"base_destino": "cla::3.7", "base_via": "otra"})):
        try:
            M.ElementoUmbral.model_validate({**base, **extra})
            chequear(g, f"ElementoUmbral: {nombre} no valida", False)
        except ValidationError:
            chequear(g, f"ElementoUmbral: {nombre} no valida", True)
    sin_base = RC.elemento_umbral(RC.analizar("no podrá superar el 5%")[0], "5%", "descripcion")
    try:
        M.ElementoUmbral.model_validate({**sin_base, "base_no_resuelta": True})
        chequear(g, "ElementoUmbral: base_no_resuelta sin base no valida", False)
    except ValidationError:
        chequear(g, "ElementoUmbral: base_no_resuelta sin base no valida", True)
    cont = G.contenidos()
    chequear(g, "tool schema de E1 el de la generación vigente y enums los de 57a8dd2",
             hashlib.sha256(cont["tool_schema_r2.json"]).hexdigest() == TOOL_SCHEMA_SHA_GENERACION
             and hashlib.sha256(cont["enums_r2.json"]).hexdigest() == ENUMS_SHA_57A8DD2)
    js = json.dumps(json.loads(cont["tool_schema_r2.json"]))
    chequear(g, "el tool schema no menciona las marcas del ensamblado",
             not any(k in js for k in M.MARCAS_NODO + ("base_destino", "verificado_en_tabla", "calificador",
                                                       "subclase_de")))


def g13_forma_r2(ch):
    """U-PROMPT-R2, P3: la lectura de la forma r2 completa y lo que pasó por E3."""
    g = "G13 forma r2 (P3)"
    item, no_item, c5, c37 = ch["ext::4.8.6.1"], ch["ext::1.1"], ch["cla::5.1.1.1"], ch["cla::3.7"]
    pi = "4.8.6.1"

    def r2(ents, rels=(), oms=(), c=item, **kw):
        return V.validar({"entities": list(ents), "relations": list(rels), "omisiones": list(oms)}, c, forma="r2", **kw)

    def prov(res, lid):
        return next((e["provenance"] for e in res["entidades"] if e["local_id"] == lid), {})

    to = ent("to", "TextoOrdenado", "TO", pi)
    # Decisión 15: tramo simple.
    casos = [("exacta", "no deberá tenerse en cuenta a los efectos de la confección", "exacta"),
             ("reordenado (tokens)", "en cuenta no deberá tenerse", "tokens"),
             ("ausente del texto", "las entidades financieras deberán informar al BCRA", "no")]
    for nombre, t, esperado in casos:
        r = r2([to, ent("o", "Obligacion", "O", pi, {"descripcion": "d"}, tramo=t)])
        p = prov(r, "o")
        chequear(g, f"tramo {nombre} → {esperado}, en la procedencia", p.get("tramo_verificado") == esperado
                 and ("tramo_modelo" in p) == (esperado == "tokens") and not r["rechazos"])
    r = r2([ent("o", "Obligacion", "O", "5.1.1.1", {"descripcion": "d"},
                tramo="a la evolución de su actividad productiva o comercial")], c=c5)
    chequear(g, "tramo con corte de palabra por guion en el texto («pro-\\nductiva») → exacta",
             prov(r, "o").get("tramo_verificado") == "exacta")
    r = r2([to, ent("o", "Obligacion", "O", pi, {"descripcion": "d"}, tramo="  ")])
    chequear(g, "tramo vacío → ausente, sin tramo en la procedencia y sin rechazo",
             prov(r, "o").get("tramo_verificado") == "ausente" and "tramo" not in prov(r, "o") and not r["rechazos"])
    r = r2([ent("to", "TextoOrdenado", "TO", pi, tramo="x")])
    chequear(g, "TextoOrdenado: sin tramo en la procedencia; un tramo emitido va a campos_no_definidos",
             "tramo_verificado" not in prov(r, "to") and r["entidades"][0]["campos_no_definidos"] == {"tramo": "x"})
    r = r2([ent("p", "Potestad", "P", "4.8.6", {"descripcion": "d"},
                tramo="complementariamente será aplicable lo siguiente")])
    chequear(g, "entidad anclada en un ancestro con tramo del heredado → exacta, contada aparte",
             prov(r, "p").get("tramo_verificado") == "exacta"
             and cont(r, "tramo_entidad", "solo_heredado:entidad_anclada_en_ancestro") == 1)
    r = r2([ent("c", "Condicion", "C", pi, {"descripcion": "d"},
                tramo="En el caso de que un cliente haya concretado una operación de venta")])
    chequear(g, "Condicion de un ítem con tramo del encabezado → exacta, contada como heredado_compuesto",
             prov(r, "c").get("tramo_verificado") == "exacta"
             and cont(r, "tramo_entidad", "solo_heredado:heredado_compuesto") == 1)
    # Tramo de dos segmentos (R11 y R30; diseño §8.2).
    enc = ("un cliente haya concretado una operación de venta con obligación de recompra utilizando los bonos "
           "BOPREAL adquiridos en una suscripción primaria")
    it = "la venta de los títulos en el origen de la operación no deberá tenerse en cuenta"
    r = r2([to, ent("o", "Obligacion", "O", pi, {"descripcion": "d"}, tramo=f"{enc} […] {it}")])
    chequear(g, "compuesto en un ítem: encabezado repartido en dos bloques heredados y el ítem → exacta; el nivel "
                "de cada segmento al registro",
             prov(r, "o").get("tramo_verificado") == "exacta" and prov(r, "o").get("tramo") == f"{enc} […] {it}"
             and cont(r, "tramo_compuesto", "encabezado.exacta") == 1 and cont(r, "tramo_compuesto", "item.exacta") == 1)
    r = r2([to, ent("o", "Obligacion", "O", pi, {"descripcion": "d"}, tramo=f"{it} [...] {it}")])
    chequear(g, "compuesto con el primer segmento copiado del texto propio → no (el encabezado no está en el "
                "heredado); se admite «[...]»",
             prov(r, "o").get("tramo_verificado") == "no" and cont(r, "tramo_compuesto", "encabezado.no") == 1)
    r = r2([to, ent("o", "Obligacion", "O", pi, {"descripcion": "d"}, tramo=f"{enc} […] {it} […] {it}")])
    chequear(g, "dos separadores → no", prov(r, "o").get("tramo_verificado") == "no"
             and cont(r, "tramo_compuesto", "dos_o_mas_separadores") == 1)
    r = r2([ent("o", "Obligacion", "O", "1.1", {"descripcion": "d"},
                tramo="Disposiciones generales […] En todas las operaciones de cambio")], c=no_item)
    chequear(g, "compuesto fuera de un ítem: cada segmento contra el texto completo, contado aparte",
             prov(r, "o").get("tramo_verificado") == "exacta" and cont(r, "tramo_compuesto", "fuera_de_item") == 1)
    # Decisión 16: término literal y Comunicacion derivada.
    r = r2([ent("d", "Definicion", "Importe de referencia", "3.7",
                {"termino": "Importe de referencia", "descripcion": "x"}, tramo="Importe de referencia")], c=c37)
    r_no = r2([ent("d", "Definicion", "D", "3.7", {"termino": "monto de corte", "descripcion": "x"}, tramo="x")],
              c=c37)
    chequear(g, "Definicion.termino verificado con su marca: exacta y no",
             prov(r, "d").get("termino_verificado") == "exacta" and prov(r_no, "d").get("termino_verificado") == "no")
    r = r2([ent("a", "Comunicacion", "Com. A 7825", pi, {"codigo": "A 7825"}, tramo="x"),
            ent("b", "Comunicacion", "Ley de Entidades", pi, {"codigo": "Ley 21.526"}, tramo="x"),
            ent("c", "Comunicacion", "Com. B 1.234", pi, {"codigo": "Comunicación B 1.234"}, tramo="x")])
    p = {e["local_id"]: e for e in r["entidades"]}
    # U-OMISIONES-COD, grupo H (v7 firmada en c90d3d9; decisión 1 de la nota del 10/10/2026 al pie): reemplaza al caso de
    # P3b-2, punto l, que afirmaba que con la forma r2 el tipo no se deriva del código. El tramo verificado sigue
    # primero (los casos con tramo, en G14); si no da el tipo, sale del código o de la etiqueta.
    chequear(g, "Comunicacion con tramo sin verificar: el tipo sale del código (H reemplaza a P3b, l): A, externa y B, "
                "con el número del código",
             [p[x]["properties"] for x in "abc"] == [{"codigo": "A 7825", "tipo": "A", "numero": 7825},
                                                     {"codigo": "Ley 21.526", "tipo": "externa"},
                                                     {"codigo": "Comunicación B 1.234", "tipo": "B", "numero": 1234}]
             and cont(r, "Comunicacion.tramo", "tramo_no_verificado") == 3
             and cont(r, "Comunicacion.tipo", "derivado_del_codigo_sin_tramo:sin_valor_del_modelo") == 2
             and cont(r, "Comunicacion.tipo", "externa_por_codigo_sin_tramo:sin_valor_del_modelo") == 1)
    chequear(g, "Comunicacion sin derivar: sin originales ni marcas",
             not any(p[x]["originales"] or p[x]["fuera_de_lista"] for x in "abc"))
    # Decisión 21: límite relativo.
    rel_t = "no podrá exceder el nivel alcanzado durante el mes anterior"
    r = r2([ent("r", "Restriccion", "R", pi, {"descripcion": "d", "tipo": "limite_cuantitativo"}, tramo="x",
                umbrales=[{"tramo": rel_t}])])
    u = r["entidades"][0]["properties"].get("umbrales") or [{}]
    chequear(g, "límite relativo: elemento sin valor, máximo inclusivo por la negación, con su base",
             len(u) == 1 and "valor" not in u[0] and u[0].get("comparacion") == "maximo_inclusivo"
             and u[0].get("base") == "nivel alcanzado durante el mes anterior"
             and r["entidades"][0]["umbrales_tramos"] == [rel_t]
             and M.PropsRestriccion.model_validate(r["entidades"][0]["properties"]) is not None)
    r = r2([ent("r", "Restriccion", "R", pi, {"descripcion": "d"}, tramo="x",
                umbrales=[{"tramo": "hasta el 5% de la RPC"}, {"tramo": rel_t}])])
    chequear(g, "con una cuantía en la misma entidad: el relativo se arma y se cuenta el límite declarado del "
                "ensamblado", cont(r, "umbrales", "limite_relativo_con_cuantias_en_la_entidad") == 1
             and len(r["entidades"][0]["properties"]["umbrales"]) == 1)
    r = r2([ent("r", "Restriccion", "R", pi, {"descripcion": "d"}, tramo="x",
                umbrales=[{"tramo": "hasta el 5% de la RPC"}])])
    chequear(g, "solo cuantías: ningún elemento en properties (lo arma el ensamblado, par A)",
             "umbrales" not in r["entidades"][0]["properties"])
    # Decisión 17.
    ents = [to, ent("o", "Obligacion", "O", pi, {"descripcion": "d"}, tramo="x"),
            ent("op", "Operacion", "Op", pi, tramo="x")]
    r = r2(ents, [rel("condiciona", pi, source="o", target="op", otras_propiedades={"plazo_relativo": "previo"}),
                  rel("establecida_en", pi, source="o", target="to", otras_propiedades="x")])
    rr = {x["predicate"]: x for x in r["relaciones"]}
    chequear(g, "otras_propiedades de la relación → properties_no_definidas; un valor que no es objeto → "
                "campos_no_definidos", rr["condiciona"].get("properties_no_definidas") == {"plazo_relativo": "previo"}
             and rr["establecida_en"]["campos_no_definidos"] == {"otras_propiedades": "x"}
             and "properties_no_definidas" not in rr["establecida_en"])
    r = r2(ents, oms=[{"categoria": "relacion_sin_predicado", "tramo": "según el punto 3", "nota": "remite_a",
                       "source": "o", "destino": "zz"},
                      {"categoria": "tabla", "tramo": "cuadro", "source": "o"}])
    o1, o2 = r["omisiones"]
    chequear(g, "relacion_sin_predicado con source y destino; en otra categoría van a campos_no_definidos",
             (o1.get("source"), o1.get("destino")) == ("o", "zz") and "source" not in o2
             and o2["campos_no_definidos"] == {"source": "o"}
             and cont(r, "omisiones", "relacion_sin_predicado.source:entidad_aceptada") == 1
             and cont(r, "omisiones", "relacion_sin_predicado.destino:sin_entidad_aceptada") == 1
             and cont(r, "omisiones", "relacion_sin_predicado.con_nota") == 1)
    # Lo que pasó por E3 (nota del 04/10/2026).
    ents = [to, ent("c", "Condicion", "C", pi, {"descripcion": "d"}, tramo="x"),
            ent("op", "Operacion", "Op", pi, tramo="x"), ent("o", "Obligacion", "O", pi, {"descripcion": "d"}, tramo="x")]
    rels = [rel("condicion_de", pi, source="c", target="op"), rel("establecida_en", pi, source="o", target="to"),
            rel("aplica_a", pi, source="o", sujeto_mencion="los marcianos")]
    libre = r2(ents, rels)
    chequear(g, "forma r2 sin vistos_e3: la firma nueva lleva la marca (regla de la forma v3)",
             libre["relaciones"][0]["no_verificada_e3"] is True and "paso_por_e3" not in libre["relaciones"][0])
    r = r2(ents, rels, vistos_e3={"entidades": [0, 1, 2, 3], "relaciones": [0]})
    chequear(g, "con vistos_e3: las relaciones que E3 no vio (1 y 2) no entran y quedan en no_vistos_e3",
             len(r["entidades"]) == 4 and len(r["relaciones"]) == 1
             and [x["elemento"] for x in r["no_vistos_e3"]] == ["relations[1]", "relations[2]"]
             and r["metricas"]["no_vistos_e3"] == 2)
    chequear(g, "con vistos_e3: la condicion_de → Operacion que vio E3 entra sin no_verificada_e3",
             r["relaciones"][0]["no_verificada_e3"] is False and r["relaciones"][0]["paso_por_e3"] is True
             and r["entidades"][1]["paso_por_e3"] is True)
    chequear(g, "la relación de sujeto que E3 no vio no deja fila en el registro de no mapeados",
             r["pendientes_no_mapeados"] == [] and len(libre["pendientes_no_mapeados"]) == 1)
    r = r2(ents, rels, vistos_e3={"entidades": [0, 1, 2], "relaciones": [0, 1, 2]})
    chequear(g, "con vistos_e3: la entidad que E3 no vio no entra, y sus relaciones quedan colgantes",
             [e["local_id"] for e in r["entidades"]] == ["to", "c", "op"]
             and [x["elemento"] for x in r["no_vistos_e3"]] == ["entities[3]"]
             and r["metricas"]["rechazos_por_motivo"] == {"ref_colgante": 2})
    try:
        V.validar({"entities": [], "relations": []}, item, forma="v3", vistos_e3={"entidades": [], "relaciones": []})
        chequear(g, "vistos_e3 con la forma v3: error", False)
    except ValueError:
        chequear(g, "vistos_e3 con la forma v3: error", True)
    # Modelos: invariantes nuevos.
    base = dict(source="c", target="op", predicate="condicion_de", punto=pi, provenance=M.Provenance(),
                tipo_source="Condicion", tipo_target="Operacion")

    def invalido(f) -> bool:
        try:
            f()
            return False
        except ValidationError:
            return True
    chequear(g, "RelacionR2: con paso_por_e3, la marca es por E3 (pasó y marcada, o no pasó y sin marca: no valida)",
             invalido(lambda: M.RelacionR2(**base, no_verificada_e3=True, paso_por_e3=True))
             and invalido(lambda: M.RelacionR2(**base, no_verificada_e3=False, paso_por_e3=False))
             and M.RelacionR2(**base, no_verificada_e3=False, paso_por_e3=True) is not None)
    chequear(g, "OmisionR2: source fuera de relacion_sin_predicado no valida",
             invalido(lambda: M.OmisionR2(categoria="tabla", origen="e1", tramo_verificado="ausente", source="o")))
    chequear(g, "Provenance: tramo sin verificación, o tramo_modelo sin «tokens», no valida",
             invalido(lambda: M.Provenance(tramo="x")) and invalido(
                 lambda: M.Provenance(tramo="x", tramo_verificado="exacta", tramo_modelo="y"))
             and M.Provenance(tramo="x", tramo_verificado="tokens", tramo_modelo="y") is not None)
    der = dict(source="Obligacion_x", target="TextoOrdenado_y", relation="establecida_en",
               rol_fuente=M.ROL_FUENTE_DERIVADA_DE_PROCEDENCIA)
    chequear(g, "establecida_en derivada de la procedencia: declarada por rol_fuente; sin marcas de E1",
             M.AristaR2(**der) is not None and invalido(lambda: M.AristaR2(**der, no_verificada_e3=True))
             and invalido(lambda: M.AristaR2(**{**der, "relation": "aplica_a"}))
             and invalido(lambda: M.AristaR2(**der, properties_no_definidas={"a": "b"})))
    chequear(g, "AristaR2: properties_no_definidas solo en una relación de E1",
             M.AristaR2(source="a", target="b", relation="condiciona", properties_no_definidas={"k": "v"}) is not None
             and invalido(lambda: M.AristaR2(source="a", target="b", relation="remite_a",
                                             properties={"alcance": "interna", "destino": "x::1", "evidencia": "e"},
                                             properties_no_definidas={"k": "v"})))


def g14_p3b(ch):
    """U-PROMPT-R2, P3b-2: h, l, la modalidad y la marca de la copia de la nota de E3."""
    g = "G14 forma r2 (P3b)"
    pol = V.politica_default()

    def r2(ents, c, **kw):
        return V.validar({"entities": list(ents), "relations": [], "omisiones": []}, c, forma="r2", **kw)

    def prov(res, lid):
        return next((e["provenance"] for e in res["entidades"] if e["local_id"] == lid), {})

    def nd(res, lid):
        return next((e.get("properties_no_definidas") or {} for e in res["entidades"] if e["local_id"] == lid), {})
    # h: mini-chunk que empieza a mitad de la oración de su última línea de títulos.
    mini = ch["cap::2.2.3::intro"]
    t = "otorgadas por sucursales y subsidiarias locales de entidades"
    r = r2([ent("o", "Obligacion", "O", "2.2.3", {"descripcion": "d"}, tramo=t)], mini)
    chequear(g, "h: tramo que cruza del título al cuerpo → exacta en orden de lectura, contado aparte",
             V.verificar_tramo(t, V.texto_completo(mini), pol.holgura)[0] != "exacta"
             and prov(r, "o").get("tramo_verificado") == "exacta"
             and cont(r, "tramo_entidad", "orden_de_lectura:exacta") == 1
             and not any(k.startswith("solo_heredado") for k in r["contadores"].get("tramo_entidad", {})))
    no_mitad = json.loads(json.dumps(mini))
    no_mitad["texto"] = "S" + no_mitad["texto"][1:]
    r = r2([ent("o", "Obligacion", "O", "2.2.3", {"descripcion": "d"}, tramo=t)], no_mitad)
    chequear(g, "h: si el texto empieza en mayúscula no es a mitad de oración: sin orden de lectura",
             prov(r, "o").get("tramo_verificado") != "exacta"
             and not any(k.startswith("orden_de_lectura") for k in r["contadores"].get("tramo_entidad", {})))
    # l: Comunicacion desde el tramo verificado.
    c12 = ch["ric::12.1.1"]
    sint = json.loads(json.dumps(c12))
    sint["texto"] += ("\nSegún el art. 39 inc. d) de la Ley 21.526 y las Comunicaciones “A” 5867, 5926 y 5970.")
    r = r2([ent("a", "Comunicacion", "Com. A 5831", "12.1.1", {"codigo": "A 5831"}, tramo="Comunicación “A” 5831"),
            ent("e", "Comunicacion", "Com. A 1111", "12.1.1", {"codigo": "A 1111"}, tramo="Comunicación “A” 5831")], c12)
    p = {e["local_id"]: e["properties"] for e in r["entidades"]}
    chequear(g, "l: Comunicación nombrada en el tramo → su letra; el número del código, controlado contra el tramo",
             p["a"] == {"codigo": "A 5831", "tipo": "A", "numero": 5831}
             and p["e"] == {"codigo": "A 1111", "tipo": "A", "numero": 1111}
             and cont(r, "Comunicacion.tramo", "comunicacion_en_tramo") == 2
             and cont(r, "Comunicacion.tipo", "derivado_del_tramo:sin_valor_del_modelo") == 2
             and cont(r, "Comunicacion.numero", "tramo_coincide") == 1
             and cont(r, "Comunicacion.numero", "tramo_no_coincide") == 1)
    r = r2([ent("l", "Comunicacion", "Com. A 39", "12.1.1", {"codigo": "A-39"},
                tramo="art. 39 inc. d) de la Ley 21.526"),
            ent("n", "Comunicacion", "Com. A 5926", "12.1.1", {"codigo": "A 5926"},
                tramo="Comunicaciones “A” 5867, 5926 y 5970")], sint)
    p = {e["local_id"]: e["properties"] for e in r["entidades"]}
    chequear(g, "l: una ley escrita como «A-39» es «externa», sin número (caso de ctacte::12.10.2)",
             p["l"] == {"codigo": "A-39", "tipo": "externa"} and cont(r, "Comunicacion.tramo", "norma_externa_en_tramo") == 1)
    chequear(g, "l: Comunicaciones en una enumeración → la letra; el número del código está en la enumeración",
             p["n"] == {"codigo": "A 5926", "tipo": "A", "numero": 5926}
             and cont(r, "Comunicacion.numero", "tramo_coincide") == 1)
    r = r2([ent("s", "Comunicacion", "Com. A 5831", "12.1.1", {"codigo": "A 5831"},
                tramo="las posiciones entre marzo y diciembre")], c12)
    # U-OMISIONES-COD, grupo H (decisión 1 de la nota del 10/10/2026 al pie de la v7): reemplaza al caso de P3b (l) «tramo
    # verificado sin norma → no se deriva»: el tramo no da el tipo y el tipo sale del código.
    chequear(g, "l y H: tramo verificado sin norma → el tipo sale del código, contado",
             r["entidades"][0]["properties"] == {"codigo": "A 5831", "tipo": "A", "numero": 5831}
             and cont(r, "Comunicacion.tramo", "tramo_sin_norma") == 1
             and cont(r, "Comunicacion.tipo", "derivado_del_codigo_sin_tramo:sin_valor_del_modelo") == 1)
    # La modalidad copiada, clasificada en código.
    chequear(g, "modalidad: lista cerrada (recomendación, consecuencia, no clasificada)",
             V.clasificar_modalidad("modalidad", "se recomienda") == "recomendacion"
             and V.clasificar_modalidad("modalidad", "buenas prácticas") == "recomendacion"
             and V.clasificar_modalidad("consecuencia", "dará lugar a la aplicación de sanciones")
             == "consecuencia_de_incumplimiento"
             and V.clasificar_modalidad("modalidad", "en lo posible") == "no_clasificada"
             and V.clasificar_modalidad("modalidad", ["x"]) == "no_clasificada")
    r = r2([ent("a", "Obligacion", "A", "12.1.1", {"descripcion": "d"}, tramo="x",
                otras_propiedades={"modalidad": "se recomienda"}),
            ent("b", "Obligacion", "B", "12.1.1", {"descripcion": "d"}, tramo="x",
                otras_propiedades={"consecuencia": "dará lugar a la aplicación de sanciones"}),
            ent("c", "Obligacion", "C", "12.1.1", {"descripcion": "d"}, tramo="x",
                otras_propiedades={"modalidad": "en lo posible", "modalidad_clasificada": "recomendacion"})], c12)
    chequear(g, "modalidad: properties_no_definidas.modalidad_clasificada junto al tramo copiado",
             nd(r, "a") == {"modalidad": "se recomienda", "modalidad_clasificada": "recomendacion"}
             and nd(r, "b") == {"consecuencia": "dará lugar a la aplicación de sanciones",
                                "modalidad_clasificada": "consecuencia_de_incumplimiento"}
             and nd(r, "c") == {"modalidad": "en lo posible", "modalidad_clasificada": "no_clasificada"}
             and cont(r, "modalidad_clasificada", "recomendacion") == 1
             and cont(r, "modalidad_clasificada", "no_clasificada") == 1)
    chequear(g, "modalidad: la clave que pone el código, escrita por el modelo, va a campos_no_definidos",
             r["entidades"][2]["campos_no_definidos"] == {"properties_no_definidas.modalidad_clasificada": "recomendacion"})
    # La marca de la copia de la nota de E3 (ratchet_e3, por runner_corpus.vistos_por_e3).
    ents = [ent("to", "TextoOrdenado", "TO", "12.1.1"), ent("o", "Obligacion", "O", "12.1.1", {"descripcion": "d"},
                                                            tramo="x")]
    marcas = {"copia_nota_e3": [{"indice_crudo": 1, "local_id": "o", "type": "Obligacion",
                                 "campos": {"descripcion": ["a b c d e"]}}]}
    r = r2(ents, c12, vistos_e3={"entidades": [0, 1], "relaciones": [], "marcas": marcas})
    sin = r2(ents, c12, vistos_e3={"entidades": [0, 1], "relaciones": []})
    chequear(g, "copia de la nota: la marca llega a la entidad y a marcas_e3 de la validación",
             nd(r, "o") == {"copia_nota_e3": {"descripcion": ["a b c d e"]}} and nd(r, "to") == {}
             and r["marcas_e3"] == marcas and cont(r, "marcas_e3", "copia_nota_e3") == 1)
    chequear(g, "sin marcas: ni la clave en la entidad ni marcas_e3",
             nd(sin, "o") == {} and "marcas_e3" not in sin)


def g16_p3c(ch):
    """U-PROMPT-R2, P3c-2: el tramo de la omisión contra el texto propio y el heredado (g) y el contador de las
    omisiones `meta_normativo` con marca (decisión 2 de la autora sobre el FRENO P3c-1; siete clases desde la
    corrección del FRENO P3c-2)."""
    g = "G16 omisiones (P3c)"
    pol = V.politica_default()
    c = ch["cla::5.1.1.1"]
    pt = "5.1.1.1"
    to = ent("to", "TextoOrdenado", "Clasificación de deudores", pt)

    def r2(oms, chunk=c):
        return V.validar({"entities": [to], "relations": [], "omisiones": list(oms)}, chunk, forma="r2")
    her = "Categorías de carteras"
    r = r2([{"categoria": "meta_normativo", "tramo": her, "nota": "n"}])
    chequear(g, "g: tramo que solo está en el heredado → verifica, contado como tramo_solo_heredado",
             V.verificar_tramo(her, c["texto"], pol.holgura)[0] == "no"
             and r["omisiones"][0]["tramo_verificado"] == "exacta" and cont(r, "omisiones", "tramo_solo_heredado") == 1)
    r = r2([{"categoria": "tabla", "tramo": "importe de referencia establecido en el punto 3.7", "nota": "n"},
            {"categoria": "formula", "tramo": "importe referencia", "nota": "n"}])
    chequear(g, "g: un tramo que verifica en el texto propio no cambia (exacta y tokens) ni se cuenta aparte",
             r["omisiones"][0]["tramo_verificado"] == "exacta" and r["omisiones"][1]["tramo_verificado"] == "tokens"
             and r["omisiones"][1]["tramo"] == "importe de\nreferencia"
             and cont(r, "omisiones", "tramo_solo_heredado") == 0)
    r = r2([{"categoria": "meta_normativo", "tramo": "texto que no está en el punto", "nota": "n"}])
    chequear(g, "g: un tramo ajeno al texto propio y al heredado sigue en no, sin contador",
             r["omisiones"][0]["tramo_verificado"] == "no" and "tramo_solo_heredado" not in r["contadores"]["omisiones"]
             and "tramo_orden_de_lectura" not in r["contadores"]["omisiones"])
    mini = ch["cap::2.2.3::intro"]
    t = "otorgadas por sucursales y subsidiarias locales de entidades"
    r = r2([{"categoria": "meta_normativo", "tramo": t, "nota": "n"}], mini)
    chequear(g, "g: en un mini-chunk a mitad de oración, el tramo que cruza del título al cuerpo verifica en el "
                "orden de lectura",
             r["omisiones"][0]["tramo_verificado"] == "exacta" and cont(r, "omisiones", "tramo_orden_de_lectura") == 1)
    # Contador de meta_normativo con marca: cuenta y no rechaza; solo la categoría meta_normativo.
    oms = [{"categoria": "meta_normativo", "tramo": "Las entidades financieras deben:", "nota": "n"},
           {"categoria": "meta_normativo", "tramo": "cuando normas legales determinen cursos de acción", "nota": "n"},
           {"categoria": "meta_normativo", "tramo": "Este requisito no será de aplicación para", "nota": "n"},
           {"categoria": "meta_normativo", "tramo": "la Superintendencia podrá exigir medidas", "nota": "n"},
           {"categoria": "meta_normativo", "tramo": "Los coeficientes aumentan con el tamaño del indicador", "nota": "n"},
           {"categoria": "fuera_de_tipos", "tramo": "las entidades deberán informar", "nota": "n"},
           {"categoria": "meta_normativo", "tramo": "Salvo cuando se trate de operaciones propias", "nota": "n"}]
    r = r2(oms)
    om = r["contadores"]["omisiones"]
    chequear(g, "marca: 5 de las 6 meta_normativo traen marca; fuera_de_tipos no se cuenta; nada se rechaza",
             om.get("meta_normativo_con_marca") == 5 and len(r["omisiones"]) == 7 and not r["rechazos"], str(om))
    chequear(g, "marca: por clase, deber 1, facultad 1, condición 2 y excepción 2",
             (om.get("meta_normativo_con_marca:deber"), om.get("meta_normativo_con_marca:facultad"),
              om.get("meta_normativo_con_marca:condicion"), om.get("meta_normativo_con_marca:excepcion"))
             == (1, 1, 2, 2), str(om))
    chequear(g, "marca: palabra entera, sin tildes ni mayúsculas («Salvo», «será»), y no por subcadena",
             V.marcas_meta_normativo("SALVO lo dispuesto") == ["excepcion"]
             and V.marcas_meta_normativo("la salvedad del punto") == []
             and V.marcas_meta_normativo("cuyos debentures") == [])
    # Corrección del FRENO P3c-2: las siete clases de la enmienda 7. Un caso por clase nueva y uno que no marca.
    oms = [{"categoria": "meta_normativo", "tramo": "las entidades no podrán cobrar esa comisión", "nota": "n"},
           {"categoria": "meta_normativo", "tramo": "La categoría abarca los préstamos de cualquier monto", "nota": "n"},
           {"categoria": "meta_normativo", "tramo": "el informe se remitirá mediante el sistema de transmisión",
            "nota": "n"},
           {"categoria": "meta_normativo", "tramo": "Con el objetivo de fortalecer la transparencia del sistema",
            "nota": "n"}]
    r = r2(oms)
    om = r["contadores"]["omisiones"]
    chequear(g, "marca (siete clases): prohibición, alcance y modalidad, una cada una; la finalidad no marca; nada se "
                "rechaza",
             om.get("meta_normativo_con_marca") == 3 and not r["rechazos"]
             and (om.get("meta_normativo_con_marca:prohibicion"), om.get("meta_normativo_con_marca:alcance"),
                  om.get("meta_normativo_con_marca:modalidad")) == (1, 1, 1)
             and "meta_normativo_con_marca:facultad" not in om, str(om))
    chequear(g, "marca: «no podrán» y «no deberán» cuentan como prohibición, no como facultad ni deber; «podrán» solo, "
                "como facultad",
             V.marcas_meta_normativo("no podrán cobrar") == ["prohibicion"]
             and V.marcas_meta_normativo("no deberán superar") == ["prohibicion"]
             and V.marcas_meta_normativo("podrán cobrar") == ["facultad"])
    chequear(g, "marca: la aplicación negada es excepción y no alcance; la afirmada, alcance",
             V.marcas_meta_normativo("no se aplica a las cajas") == ["excepcion"]
             and V.marcas_meta_normativo("se aplica a las cajas") == ["alcance"])
    # Modalidad del prefijo (decisión posterior al commit de P3c-2): subclases opción, consejo y forma. Un caso por
    # subclase y uno de finalidad con «mediante».
    fin_mediante = "Con el fin de promover la estabilidad mediante una mejor gestión del riesgo"
    oms = [{"categoria": "meta_normativo", "tramo": "el cálculo se hará indistintamente sobre saldos diarios o promedio",
            "nota": "n"},
           {"categoria": "meta_normativo", "tramo": "Es recomendable que la entidad documente sus procedimientos",
            "nota": "n"},
           {"categoria": "meta_normativo", "tramo": "la comunicación se cursará por escrito al domicilio constituido",
            "nota": "n"},
           {"categoria": "meta_normativo", "tramo": fin_mediante, "nota": "n"}]
    r = r2(oms)
    om = r["contadores"]["omisiones"]
    chequear(g, "modalidad: opción 1, consejo 1 y forma 2 (la del medio y la finalidad con «mediante»); la clase cuenta "
                "las 4; nada se rechaza",
             (om.get("meta_normativo_con_marca:modalidad"), om.get("meta_normativo_con_marca:modalidad.opcion"),
              om.get("meta_normativo_con_marca:modalidad.consejo"), om.get("meta_normativo_con_marca:modalidad.forma"))
             == (4, 1, 1, 2) and om.get("meta_normativo_con_marca") == 4 and not r["rechazos"], str(om))
    chequear(g, "modalidad: la finalidad con «mediante» cae solo en la subclase forma, sin otra clase",
             V.marcas_meta_normativo(fin_mediante) == ["modalidad"] and V.subclases_modalidad(fin_mediante) == ["forma"])
    chequear(g, "modalidad: las marcas de opción y de consejo caen en su subclase («concurrentemente», «a opción del», "
                "«cualquiera de», «se aconseja», «buena práctica»)",
             all(V.subclases_modalidad(t) == ["opcion"] for t in ("que cumplan concurrentemente ambos requisitos",
                                                                   "a opción del cliente", "cualquiera de los dos"))
             and all(V.subclases_modalidad(t) == ["consejo"] for t in ("se aconseja revisarlo", "una buena práctica")))


def g15_c2():
    """U-R2-CODIGO-2, C2: puntos c, i, j, k y m de reglas_comparacion."""
    g = "G15 U-R2-CODIGO-2 C2"
    # c: cuantías nuevas
    cs = RC.analizar("Informar, dentro de las 24 hs. hábiles siguientes a la recepción")
    chequear(g, "c «hs.»: «24 hs. hábiles» es una cuantía de 24 horas (fuera de lista), máximo inclusivo por «dentro de»",
             len(cs) == 1 and (cs[0].texto, cs[0].valor, cs[0].unidad, cs[0].fuera_de_lista, cs[0].comparacion)
             == ("24 hs.", "24", "horas", ["unidad"], "maximo_inclusivo"))
    cs = RC.analizar("deberá efectuarse hasta el quinto día hábil posterior al vencimiento de cada período")
    chequear(g, "c ordinal: «hasta el quinto día hábil» → 5 días hábiles, máximo inclusivo",
             len(cs) == 1 and (cs[0].valor, cs[0].unidad, cs[0].dias_tipo, cs[0].comparacion, cs[0].regla)
             == ("5", "dias", "habiles", "maximo_inclusivo", "compuesta:hasta"))
    casos = [("dentro del tercer mes siguiente", ("3", "meses", "maximo_inclusivo", "compuesta:dentro_de")),
             ("a más tardar el décimo día hábil", ("10", "dias", "maximo_inclusivo", "compuesta:a_mas_tardar")),
             ("hasta el trigésimo sexto mes", ("36", "meses", "maximo_inclusivo", "compuesta:hasta"))]
    for t, esp in casos:
        c = una(t)
        chequear(g, f"c ordinal con marcador: {t!r} → {esp}",
                 c is not None and (c.valor, c.unidad, c.comparacion, c.regla) == esp,
                 "" if c is None else f"{c.valor} {c.unidad} {c.comparacion} {c.regla}")
    chequear(g, "c ordinal sin marcador no es cuantía («a partir del octavo mes», «el segundo mes anterior»)",
             RC.analizar("a partir del octavo mes") == [] and RC.analizar("al último día del segundo mes anterior") == [])
    cs = RC.analizar("activos que en conjunto superen el 25 % de la RPC registrada al último día del segundo mes "
                     "anterior")
    chequear(g, "c: la base del 25 % de cap::6.11 no se corta en el ordinal",
             len(cs) == 1 and cs[0].base == "RPC registrada al último día del segundo mes anterior", str(cs and cs[0].base))
    c = una("con un plazo de un día hábil")
    chequear(g, "c «hábil» en singular fija dias_tipo y entra al tramo",
             c is not None and (c.texto, c.dias_tipo) == ("un día hábil", "habiles"))
    c = una("bienes con 180 (ciento ochenta) o más días corridos")
    chequear(g, "c «o más» entre el paréntesis y la unidad: 180 días corridos, mínimo inclusivo (compuesta:o_mas)",
             c is not None and (c.valor, c.unidad, c.dias_tipo, c.comparacion, c.regla)
             == ("180", "dias", "corridos", "minimo_inclusivo", "compuesta:o_mas"))
    # i: alcance de la negación e «igual o superior»
    casos = [("El cliente no ha utilizado este mecanismo por un monto superior al equivalente de USD 36.000",
              "maximo_inclusivo", "negacion:raiz_super"),
             ("sin haber incurrido en atrasos superiores a 31 días", "maximo_inclusivo", "negacion:raiz_super"),
             ("las operaciones no podrán tener un plazo de pago que exceda a los 360 días corridos",
              "maximo_inclusivo", "negacion:raiz_exced"),
             ("En ningún caso el registro del cheque podrá demorarse más de 15 días corridos", "maximo_inclusivo",
              "negacion:mas_de"),
             ("la deuda del sector privado no financiero en la entidad prestamista (por todo concepto) más el importe "
              "solicitado exceda del 2,5 %", "minimo_estricto", "simple:raiz_exced"),
             ("no se aplica a la entidad y, en el conjunto, superen el 5%", "minimo_estricto", "simple:raiz_super"),
             ("cuyo endeudamiento sea equivalente o superior al 1 %", "minimo_inclusivo", "compuesta:igual_o_superior"),
             ("cuyas financiaciones igualen o superen el 1 %", "minimo_inclusivo", "compuesta:igual_o_superior"),
             ("que no igualen o superen el 1 %", "maximo_estricto", "negacion:igual_o_superior")]
    for t, comp, regla in casos:
        c = una(t)
        chequear(g, f"i {t!r} → {comp} ({regla})", c is not None and (c.comparacion, c.regla) == (comp, regla),
                 "" if c is None else f"{c.comparacion} {c.regla}")
    # i, «o no» (enmienda 5, punto 1.d): no es una negación, a ninguna distancia; caso de control cap::6.2.2.3
    d6223 = ("El ponderador de riesgo de los instrumentos a tasa variable dependerá de que el cupón de renta del "
             "período en curso –o, de no estar disponible aún, el último que se hubiera pagado– represente o no un "
             "rendimiento menor a 3 % anual.")
    casos = [(d6223, d6223, "maximo_estricto", "simple:menor"),
             ("se imputarán a escalas de vencimientos divididas en 15 o 13 bandas temporales, según que el cupón del "
              "instrumento sea, o no, menor a 3 %.", None, "maximo_estricto", "simple:menor"),
             ("según que el cupón no sea menor a 3 %", None, "minimo_inclusivo", "negacion:menor")]
    for t, desc, comp, regla in casos:
        c = [x for x in RC.analizar(t, desc) if x.valor == "3"]
        chequear(g, f"i «o no» {t[-60:]!r} → {comp} ({regla})",
                 len(c) == 1 and (c[0].comparacion, c[0].regla) == (comp, regla),
                 "" if not c else f"{c[0].comparacion} {c[0].regla}")
    # «más del» y «menos del» (enmienda 5, punto 3.b); «o más del total» sigue por «o más»
    casos = [("para más del 5% de la posición de titulización", "minimo_estricto", "simple:mas_de"),
             ("que individualmente representen menos del 10 % del CO", "maximo_estricto", "simple:menos_de"),
             ("no menos del 50% de los clientes", "minimo_inclusivo", "negacion:menos_de"),
             ("cuando concentren el 40 % o más del total", "minimo_inclusivo", "compuesta:o_mas")]
    for t, comp, regla in casos:
        c = una(t)
        chequear(g, f"«más del»/«menos del» {t!r} → {comp} ({regla})",
                 c is not None and (c.comparacion, c.regla) == (comp, regla),
                 "" if c is None else f"{c.comparacion} {c.regla}")
    # j: comparador pegado a la cuantía
    casos = [("Las previsiones no superarán el 1,25% de los activos ponderados por riesgo", "maximo_inclusivo"),
             ("recibir un ponderador de riesgo igual o inferior a 50% para cada exposición", "maximo_inclusivo"),
             ("El ponderador resultante estará sujeto a un mínimo de 15% para los tramos", "minimo_inclusivo"),
             ("se le haya aplicado un aforo de al menos el 20%", "minimo_inclusivo"),
             ("se aplicará un ponderador de riesgo del 2 % a la exposición", "coeficiente"),
             ("con previsiones iguales o mayores al 50% del saldo pendiente. Ponderador: 50%", "minimo_inclusivo")]
    for t, comp in casos:
        c = una(t)
        chequear(g, f"j {t!r} → {comp}", c is not None and c.comparacion == comp,
                 "" if c is None else f"{c.comparacion} {c.regla}")
    t = "con previsiones iguales o mayores al 50% del saldo pendiente. Ponderador: 50%"
    cs = RC.analizar(t, t)
    chequear(g, "j con la descripción como fuente del coeficiente (camino de r2a): la primera cuantía, con comparador "
                "pegado, mínimo inclusivo; la segunda («Ponderador: 50%»), coeficiente",
             len(cs) == 2 and cs[0].comparacion == "minimo_inclusivo" and cs[1].comparacion == "coeficiente")
    c = una("aplicar el 5%", "Las exposiciones se ponderan por riesgo.")
    chequear(g, "j sin comparador en el tramo, el coeficiente de la descripción sigue", c.comparacion == "coeficiente")
    # k: tramo compuesto
    t = "deberán observar los siguientes límites mínimos: […] multiplicar 6% por los activos ponderados por riesgo"
    cs = RC.analizar(t)
    chequear(g, "k tramo de dos segmentos: la cuantía del ítem toma «mínimos» del final del encabezado",
             len(cs) == 1 and (cs[0].comparacion, cs[0].regla, cs[0].fuente_marcador)
             == ("minimo_inclusivo", "encabezado:compuesta:adyacencia_minimo", "encabezado"),
             "" if not cs else f"{cs[0].comparacion} {cs[0].regla}")
    cs = RC.analizar("deberán observar los siguientes límites mínimos: multiplicar 6% por los APR")
    chequear(g, "k sin el separador « […] », el «:» corta la cláusula y la cuantía queda sin marcador",
             len(cs) == 1 and cs[0].comparacion == "no_determinada")
    cs = RC.analizar("los siguientes conceptos: […] que superen el 6% de los APR")
    chequear(g, "k el marcador propio del ítem manda sobre el encabezado",
             len(cs) == 1 and cs[0].regla == "simple:raiz_super")
    cs = RC.analizar("los siguientes límites mínimos: […] el 6% […] y el 8%")
    chequear(g, "k con dos o más separadores no se lee el encabezado", all(c.comparacion == "no_determinada" for c in cs))
    # m: plazo sin marcador
    c = una("en un plazo de 30 días")
    chequear(g, "m plazo sin marcador: no_determinada, regla sin_marcador_plazo, sin comparacion_asumida",
             (c.comparacion, c.regla, c.comparacion_asumida) == ("no_determinada", "sin_marcador_plazo", False))
    c = RC.analizar("en un plazo de 30 días", plazo_sin_marcador="maximo_asumido")[0]
    chequear(g, "m con «maximo_asumido» (fase r2a), la regla anterior: máximo inclusivo con comparacion_asumida",
             (c.comparacion, c.regla, c.comparacion_asumida) == ("maximo_inclusivo", "sin_marcador_plazo", True))
    c = una("el 5% del total")
    chequear(g, "m otra cuantía sin marcador: no_determinada, regla sin_marcador", (c.comparacion, c.regla)
             == ("no_determinada", "sin_marcador"))
    try:
        RC.analizar("en 30 días", plazo_sin_marcador="otro")
        chequear(g, "m un valor desconocido de plazo_sin_marcador frena", False)
    except ValueError:
        chequear(g, "m un valor desconocido de plazo_sin_marcador frena", True)
    el = RC.elemento_umbral(una("en un plazo de 30 días"), "30 días")
    chequear(g, "m el elemento valida con ElementoUmbral (comparacion_asumida en False)",
             M.ElementoUmbral.model_validate(el) is not None and el["comparacion_asumida"] is False)


def g17_omisiones_cod(ch):
    """U-OMISIONES-COD (v7 firmada en c90d3d9), grupo B, ítem f, y grupo H: la mención de sujeto con las contracciones
    y el tipo de la Comunicacion desde el código, con la marca `tipo_no_derivable`."""
    g = "G17 U-OMISIONES-COD (f y H)"
    c = ch["cla::5.1.1.1"]
    pt = "5.1.1.1"
    # f: «del» → «de el» y «al» → «a el», solo con contracciones (la llamada de la mención de sujeto).
    for men, texto in (("el cuentacorrentista", "Obligaciones del cuentacorrentista."),
                       ("el Comité de auditoría", "Las funciones del Comité de auditoría son las siguientes."),
                       ("el cliente", "Se requerirá al cliente la documentación.")):
        chequear(g, f"f: «{men}» contra «{texto}» → exacta con contracciones; sin ellas, como antes",
                 V.verificar_tramo(men, texto, 2, contracciones=True)[0] == "exacta"
                 and V.verificar_tramo(men, texto, 2)[0] != "exacta")
    chequear(g, "f: una mención ausente del texto sigue en «no» con contracciones",
             V.verificar_tramo("el directorio", "Obligaciones del cuentacorrentista.", 2, contracciones=True)[0] == "no")
    chequear(g, "f: la expansión conserva el span de la contracción (literal del nivel «tokens»)",
             V.verificar_tramo("cuentacorrentista el obligaciones", "Obligaciones del cuentacorrentista.", None,
                               contracciones=True)[1] == "Obligaciones del cuentacorrentista")
    sint = dict(c, texto="Obligaciones del cuentacorrentista.", herencia=[])
    to = ent("to", "TextoOrdenado", "Clasificación de deudores", pt)
    ob = ent("e1", "Obligacion", "Informar", pt, {"descripcion": "x", "tipo": "otra"})
    r = V.validar({"entities": [to, ob], "relations": [rel("aplica_a", pt, source="e1",
                                                           sujeto_mencion="el cuentacorrentista")]}, sint, forma="r2")
    x = r["relaciones"][0] if r["relaciones"] else {}
    chequear(g, "f: la mención de sujeto «el cuentacorrentista» verifica contra «Obligaciones del cuentacorrentista»",
             x.get("mencion_verificada") == "exacta" and x.get("sujeto_mencion") == "el cuentacorrentista",
             str(x.get("mencion_verificada")))
    ob_t = ent("e1", "Obligacion", "Informar", pt, {"descripcion": "x", "tipo": "otra"}, tramo="el cuentacorrentista")
    r = V.validar({"entities": [to, ob_t], "relations": []}, sint, forma="r2")
    pe = next((e["provenance"] for e in r["entidades"] if e["local_id"] == "e1"), {})
    chequear(g, "f: el tramo de una entidad no usa las contracciones (solo la mención)", pe.get("tramo_verificado") != "exacta",
             str(pe.get("tramo_verificado")))
    # H: el tipo desde el código cuando el tramo no lo da, y la marca en el resto.
    def r2(ents, c_=c):
        return V.validar({"entities": list(ents), "relations": [], "omisiones": []}, c_, forma="r2")
    r = r2([ent("x1", "Comunicacion", "Decreto 28/23", pt, {"codigo": "Decreto 28/23"}, tramo="x"),
            ent("x2", "Comunicacion", "Dec. 386 del 10.7.03", pt, {"codigo": "Dec. 386 del 10.7.03"}, tramo="x"),
            ent("x3", "Comunicacion", "Código Civil y Comercial de la Nación",
                pt, {"codigo": "Código Civil y Comercial de la Nación"}, tramo="x"),
            ent("x4", "Comunicacion", "Decisión Mercosur", pt, {"codigo": "Decisión Mercosur"}, tramo="x"),
            ent("x5", "Comunicacion", "Disposición N° 6/19", pt, {"codigo": "Disposición N° 6/19"}, tramo="x"),
            ent("x6", "Comunicacion", "Comunicación A-7000", pt, {"codigo": "A-7000"}, tramo="x")])
    p = {e["local_id"]: e for e in r["entidades"]}
    chequear(g, "H: normas externas por el código (léxico de la política más dec, código, decisión y disposición) y "
                "«A-7000» → A con su número",
             all(p[f"x{i}"]["properties"].get("tipo") == "externa" for i in range(1, 6))
             and p["x6"]["properties"] == {"codigo": "A-7000", "tipo": "A", "numero": 7000}
             and cont(r, "Comunicacion.tipo", "externa_por_codigo_sin_tramo:sin_valor_del_modelo") == 5,
             str([p[f"x{i}"]["properties"] for i in range(1, 7)]))
    r = r2([ent("y1", "Comunicacion", "Punto 3.1", pt, {"codigo": "punto 3.1"}, tramo="x"),
            ent("y2", "Comunicacion", "Capitales mínimos", pt, {"codigo": "Capitales mínimos de las entidades financieras"},
                tramo="x")])
    p = {e["local_id"]: e for e in r["entidades"]}
    chequear(g, "H: remisión a un punto y nombre de un TO → sin tipo, con la marca tipo_no_derivable, contada",
             all(p[y]["properties"].get("tipo") is None and (p[y].get("properties_no_definidas") or {}).get(
                 "tipo_no_derivable") is True for y in ("y1", "y2"))
             and cont(r, "Comunicacion.tipo", "tipo_no_derivable") == 2)
    r = r2([ent("z", "Comunicacion", "Com. A 7825", pt, {"codigo": "A 7825", "tipo_no_derivable": True}, tramo="x")])
    z = r["entidades"][0]
    chequear(g, "H: la marca tipo_no_derivable es del código: si la escribe el modelo va a campos no definidos",
             "properties_no_definidas.tipo_no_derivable" in z.get("campos_no_definidos", {})
             and z["properties"].get("tipo") == "A", str(z.get("campos_no_definidos")))
    sint_com = dict(c, texto="Según lo previsto en la Comunicación “B” 5831.", herencia=[])
    r = r2([ent("t", "Comunicacion", "Com. A 1111", pt, {"codigo": "A 1111"}, tramo="Comunicación “B” 5831")], sint_com)
    chequear(g, "H, negativo: con el tramo verificado que nombra la Comunicación, el tramo manda y no el código",
             r["entidades"][0]["properties"].get("tipo") == "B"
             and cont(r, "Comunicacion.tipo", "derivado_del_tramo:sin_valor_del_modelo") == 1
             and cont(r, "Comunicacion.tipo", "derivado_del_codigo_sin_tramo:sin_valor_del_modelo") == 0,
             str(r["entidades"][0]["properties"]))


def main() -> int:
    ch = cargar_chunks()
    g1_listas()
    g2_politica()
    g3_valores_n1(ch)
    g4_reglas()
    g5_control(ch)
    g6_bkl_e3(ch)
    g7_mencion_omision(ch)
    g8_modelos()
    g9_tool_schema(ch)
    g10_calibracion(ch)
    g11_remite_a()
    g12_ensamblado()
    g13_forma_r2(ch)
    g14_p3b(ch)
    g15_c2()
    g16_p3c(ch)
    g17_omisiones_cod(ch)
    total = ok = 0
    print(f"política: {V.POLITICA.relative_to(REPO)}  sha256 {V.politica_default().sha256}")
    for grupo, filas in RES.items():
        n_ok = sum(1 for _, b, _ in filas if b)
        total += len(filas)
        ok += n_ok
        print(f"{grupo}: {n_ok}/{len(filas)}")
        for nombre, b, det in filas:
            if not b:
                print(f"   FALLA  {nombre}  [{det}]")
    print(f"TOTAL: {ok}/{total}")
    return 0 if ok == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
