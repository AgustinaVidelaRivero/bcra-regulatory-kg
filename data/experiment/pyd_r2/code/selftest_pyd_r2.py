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
      con un valor fuera de lista queda marcado, no descartado.

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
        ("el menor entre 1 año y el plazo residual", "maximo_inclusivo", "sin_marcador_plazo"),
        ("el límite inferior del 3%", "no_determinada", "sin_marcador"),
        ("a tasas inferiores al 2%", "maximo_estricto", "simple:inferior"),
        ("en menos de 90 días", "maximo_estricto", "simple:menos_de"),
        ("por importes menores a USD 200", "maximo_estricto", "simple:menor"),
        ("no podrá superar el 5%", "maximo_inclusivo", "negacion:raiz_super"),
        ("no podrán ser superiores al 3%", "maximo_inclusivo", "negacion:raiz_super"),
        ("sin exceder el 20%", "maximo_inclusivo", "negacion:raiz_exced"),
        ("no podrá ya nunca superar el 1%", "maximo_inclusivo", "negacion:raiz_super"),
        ("no podrá en ningún caso superar el 1%", "minimo_estricto", "simple:raiz_super"),
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
        ("la Superintendencia podrá fijar un plazo de 30 días", "maximo_inclusivo", "sin_marcador_plazo"),
        ("aplicará un ponderador de riesgo del 2 %", "coeficiente", "coeficiente"),
        ("un ponderador del 100% a las exposiciones que no superen", "coeficiente", "coeficiente"),
        ("no sea igual o superior al 30%", "maximo_estricto", "negacion:igual_o_superior"),
        ("en un plazo de 30 días", "maximo_inclusivo", "sin_marcador_plazo"),
        ("el 5% del total", "no_determinada", "sin_marcador"),
    ]
    for tramo, comp, regla in casos:
        c = una(tramo)
        chequear(g, f"{tramo!r} → {comp} ({regla})", c is not None and c.comparacion == comp and c.regla == regla,
                 "" if c is None else f"{c.comparacion} {c.regla}")
    c = una("en un plazo de 30 días")
    chequear(g, "plazo sin marcador lleva comparacion_asumida", c.comparacion_asumida is True)
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
                "plazo con máximo inclusivo y comparacion_asumida",
             len(cs) == 2 and cs[1].comparacion == "minimo_inclusivo" and cs[0].regla == "sin_marcador_plazo"
             and cs[0].comparacion == "maximo_inclusivo" and cs[0].comparacion_asumida is True)
    chequear(g, "precedencia: «no inferior a» (negación) sobre «inferior a» (simple)",
             una("no inferior al 8%").comparacion == "minimo_inclusivo"
             and una("inferior al 8%").comparacion == "maximo_estricto")
    chequear(g, "precedencia: «igual o superior» (compuesta) sobre «superior» (simple)",
             una("igual o superior al 10%").comparacion == "minimo_inclusivo")
    chequear(g, "precedencia: coeficiente sobre negación",
             una("el ponderador no podrá superar el 50%").comparacion == "coeficiente")
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
            chequear(g, "fila 15: «el menor entre 1 año» queda sin marcador, plazo con máximo inclusivo y "
                        "comparacion_asumida",
                     len(uno) == 1 and uno[0].regla == "sin_marcador_plazo" and uno[0].comparacion_asumida is True)
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
    chequear(g, "la verificación del tramo de omisión usa solo el texto propio (no el heredado)",
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
        ("la supervisión dispondrá de 30 días", "maximo_inclusivo", "sin_marcador_plazo"),
        ("la Superintendencia, la superficie, el superávit y el excedente del 5%", "no_determinada", "sin_marcador"),
        ("Multa equivalente al 4% del valor rechazado", "igual", "igual:equivalente_a"),
        ("La deducción será equivalente al 100% del valor", "igual", "igual:equivalente_a"),
        ("Límite máximo equivalente a USD 100", "no_determinada", "sin_marcador"),
        ("a razón de un máximo mensual equivalente al 10%", "no_determinada", "sin_marcador"),
        ("A partir del segundo y hasta el trigésimo sexto mes, la exigencia mensual será equivalente al 10% del "
         "promedio", "igual", "igual:equivalente_a"),
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
    chequear(g, "«supervisión … 30 días»: plazo sin marcador, con comparacion_asumida", c.comparacion_asumida is True)
    # «factor» tomado de la descripción: los dos falsos positivos reales de P2.
    sha_kg = {"diez": "dd42d6d9c0c8379da90ec4ed4e4659157a960a0d1ceaf8af5a008bdd9cad9010",
              "r1": "0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a"}
    rutas = {"diez": "data/experiment/reextraccion_v2/corpus_tanda0/ens_diez/r1/kg.json",
             "r1": "data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json"}
    frases = {"diez": ("factor igual a 4", "5%", "minimo_estricto", "simple:raiz_super"),
              "r1": ("por el factor correspondiente", "cinco días hábiles", "maximo_inclusivo", "sin_marcador_plazo")}
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
    chequear(g, "manifest: sha256 de la política y de modelos_r2 vigentes",
             man["politica"]["sha256"] == M.sha256_archivo(V.POLITICA)
             and man["modelos"]["sha256"] == M.sha256_archivo(AQUI / "modelos_r2.py"))
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
    chequear(g, "properties conocidas de cada tipo, cerradas (additionalProperties false)",
             all(x["properties"]["properties"].get("additionalProperties") is False
                 for x in sch["properties"]["entities"]["items"]["anyOf"]))
    c = ch["cla::5.1.1.1"]
    pt = "5.1.1.1"
    valido = {
        "entities": [
            {"local_id": "to", "type": "TextoOrdenado", "label": "Clasificación de deudores", "punto": pt,
             "properties": {"materia": "Clasificación de deudores", "archivo": "TO_clasificacion_deudores_actual.pdf",
                            "version": "actual"}},
            {"local_id": "e1", "type": "Restriccion", "label": "Consumo sobre dos veces el importe", "punto": pt,
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
             and e.get("campos_no_definidos") == {"otras_propiedades.tipo": "x"}
             and cont_(r, "claves", "otras_propiedades_a_properties_no_definidas") == 1 and not r["rechazos"])
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
