#!/usr/bin/env python3
"""selftest_regression_kg.py — selftest de scripts/regression_kg.py (U-B2.1 fase 2, pieza g).

Solo stdlib; fixtures sintéticos mínimos escritos acá. Cubre:
  - por cada forma de test (F1 nodo presente/ausente, F2 ancla presente, F3
    valor de propiedad, F4 arista presente/ausente, F5 rank en buscar_nodos)
    un caso que pasa y un contraejemplo;
  - el adaptador sobre un nodo gen 2 y uno gen 3, incluidas la cuarentena
    booleana y la cadena "true";
  - la política de cuarentena en sus dos valores (T7 y BKL-0019);
  - la exclusión de rol_fuente cuarentena_laudada en T4 (decisión 8);
  - la ambigüedad de E4-a6 con un resolvedor sintético;
  - un caso de regresión contra una fixture sintética que devuelve código de
    salida distinto de 0 (computar_regresion + main end-to-end con --solo);
  - U-R2-CODIGO, R5: scripts/remisiones.py (las dos formas, firma y alcance),
    R-T4, R-T5, R-E4a8, BKL-0028 con los tres ids esperados, BKL-0006 y
    BKL-0023 con la lista de umbrales, el test del ejemplo cla::5.1.1.1,
    LN-1 a LN-8 y los censos (con el control sobre las 105 relaciones de la
    lectura de la matriz).

Uso: PYTHONDONTWRITEBYTECODE=1 python3 scripts/selftest_regression_kg.py
"""
from __future__ import annotations

import sys

sys.dont_write_bytecode = True

import hashlib
import json
import tempfile
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parent))
import regression_kg as RK  # noqa: E402

OK, FAIL = [], []


def caso(nombre: str, cond: bool, detalle: str = "") -> None:
    (OK if cond else FAIL).append(f"{nombre}{(' — ' + detalle) if detalle else ''}")


# --------------------------------------------------------------------------- #
# Fixtures sintéticos                                                          #
# --------------------------------------------------------------------------- #
CAP_PDF = "TO_capitales_minimos_actual.pdf"
CLA_PDF = "TO_clasificacion_deudores_actual.pdf"


def nodo_gen2(id_, tipo, label, props=None, location="Sección 1. Punto 1.2. Exigencia básica.", extra=None, rol_fuente=None):
    n = {"id": id_, "type": tipo, "label": label, "properties": props or {},
         "provenance": {"source_doc": CAP_PDF, "location": location}}
    if extra:
        n["additional_provenance"] = extra
    if rol_fuente:
        n["rol_fuente"] = rol_fuente
    return n


def nodo_gen3(id_, tipo, label, props=None, punto="1.2", archivo=CAP_PDF, to="cap"):
    p = {"to": to, "archivo": archivo, "punto": punto, "rol_documental": "punto_propio"}
    return {"id": id_, "type": tipo, "label": label, "properties": props or {}, "provenance": p, "provenances": [p]}


def arista(s, r, t, rol_fuente=None, props=None, gen=2):
    e = {"source": s, "relation": r, "target": t}
    e["provenance"] = {"source_doc": CAP_PDF, "location": "Punto 1.2."} if gen == 2 else {"to": "cap", "archivo": CAP_PDF, "punto": "1.2"}
    if rol_fuente:
        e["rol_fuente"] = rol_fuente
    if props:
        e["properties"] = props
    return e


CATALOGO = {"version": "9.9-sintetico",
            "clases": [{"id": "Sujeto_sujeto", "label": "Sujetos", "nivel": "clase", "alias": []},
                       {"id": "Sujeto_banco", "label": "Bancos", "nivel": "clase", "alias": ["Banco"]},
                       {"id": "Sujeto_contraparte", "label": "Contrapartes", "nivel": "clase", "alias": []}],
            "roles": [{"id": "Sujeto_rol_x", "label": "Rol X", "nivel": "rol", "miembros": ["Sujeto_banco"]}]}


class IndiceFalso:
    """Retriever mínimo con la interfaz de harness.GraphIndex.buscar_nodos."""

    def __init__(self, orden):
        self.orden = orden

    def buscar_nodos(self, consulta, limite=10):
        return {"consulta": consulta, "resultados": [{"id": i} for i in self.orden[:limite]]}


def ctx_sintetico(grafo, politica="laudada", **kw):
    cat = RK.Catalogo(CATALOGO, "sintetico", "0" * 64)
    return RK.Contexto(grafo, cat, 2, politica, **kw)


# --------------------------------------------------------------------------- #
# 1. Adaptador de provenance                                                   #
# --------------------------------------------------------------------------- #
n2 = nodo_gen2("Restriccion_x", "Restriccion", "Exigencia básica bancos", {"umbral": "5.000 millones de pesos", "cuarentena": True},
               extra=[{"source_doc": CLA_PDF, "location": "Punto 6.5.2. Con seguimiento especial."}])
n3 = nodo_gen3("Restriccion_y", "Restriccion", "Exigencia básica bancos", {"umbral": "5.000 millones de pesos", "cuarentena": "true"})
caso("adaptador gen2: anclas desde location «Punto 1.2.» + additional_provenance",
     RK.anclas(n2) == {(CAP_PDF, "1.2"), (CLA_PDF, "6.5.2")}, str(RK.anclas(n2)))
caso("adaptador gen3: anclas desde provenances[].archivo/punto", RK.anclas(n3) == {(CAP_PDF, "1.2")}, str(RK.anclas(n3)))
caso("adaptador: formato detectado gen2 / gen3", RK.formato_provenance(n2["provenance"]) == 2 and RK.formato_provenance(n3["provenance"]) == 3)
caso("adaptador: provenances() nunca usa solo provenance[0]", len(RK.provenances(n2)) == 2 and len(RK.provenances(n3)) == 1)
caso("adaptador: cuarentena booleana True → True", RK.cuarentena_bool(True) is True)
caso("adaptador: cuarentena cadena \"true\" → True", RK.cuarentena_bool("true") is True and RK.cuarentena_bool("True") is True)
caso("adaptador: cuarentena \"false\" / None / False → False", RK.cuarentena_bool("false") is False and RK.cuarentena_bool(None) is False and RK.cuarentena_bool(False) is False)
caso("adaptador: detectar_generacion", RK.detectar_generacion({"nodes": [n2], "edges": []}) == 2 and RK.detectar_generacion({"nodes": [n3], "edges": []}) == 3)

# --------------------------------------------------------------------------- #
# 2. Formas F1–F5, caso que pasa y contraejemplo                               #
# --------------------------------------------------------------------------- #
G = RK.Grafo({"nodes": [n2, n3, nodo_gen2("TextoOrdenado_cap", "TextoOrdenado", "CapMin", {"archivo": CAP_PDF}),
                        nodo_gen2("Excepcion_c", "Excepcion", "Cajas exceptuadas", {"descripcion": "Las cajas de crédito cooperativas están exceptuadas"})],
              "edges": [arista("Restriccion_x", "establecida_en", "TextoOrdenado_cap"), arista("Excepcion_c", "exceptua", "Restriccion_x")]})
# F1 nodo presente / ausente (direccionamiento por archivo, punto, tipo, cadena)
caso("F1 pasa: nodo presente por (archivo, punto, tipo, cadena)", len(G.buscar("Restriccion", "TO_capitales", "1.2", contiene=["exigencia basica"])) == 2)
caso("F1 contraejemplo: cadena ausente → sin nodo", G.buscar("Restriccion", "TO_capitales", "1.2", contiene=["restantes entidades"]) == [])
caso("F1 contraejemplo: tipo distinto → sin nodo", G.buscar("Obligacion", "TO_capitales", "1.2", contiene=["exigencia basica"]) == [])
caso("F1: no_contiene excluye", G.buscar("Restriccion", "TO_capitales", "1.2", contiene=["bancos"], no_contiene=["exigencia"]) == [])
caso("F1: acentos y mayúsculas normalizados", len(G.buscar(None, "TO_capitales", "1.2", contiene=["EXIGENCIA BÁSICA"])) == 2)
# F2 ancla presente
caso("F2 pasa: ancla (archivo, punto) presente en cualquier provenance", RK.con_ancla(n2, "TO_clasificacion", "6.5.2"))
caso("F2 pasa: prefijo_punto acepta 6.5.2 para 6.5", RK.con_ancla(n2, "TO_clasificacion", "6.5", prefijo_punto=True))
caso("F2 contraejemplo: punto ausente", not RK.con_ancla(n2, "TO_capitales", "1.3") and not RK.con_ancla(n3, "TO_exterior", "1.2"))
caso("F2 contraejemplo: 1.2 no es prefijo de 1.25", not RK.con_ancla(n2, "TO_capitales", "1", prefijo_punto=False))
# F3 valor de propiedad (BKL-0023 sobre grafo sintético: pasa / contraejemplo / sin umbral → no_aplicable)
frase = "Las compañías financieras que realicen, en forma directa, operaciones de comercio exterior deberán observar"
g_ok = RK.Grafo({"nodes": [nodo_gen2("R1", "Restriccion", "Compañías", {"descripcion": frase, "umbral": "5.000 millones de pesos"})], "edges": []})
g_mal = RK.Grafo({"nodes": [nodo_gen2("R1", "Restriccion", "Compañías", {"descripcion": frase, "umbral": "2.500 millones de pesos"})], "edges": []})
g_sin = RK.Grafo({"nodes": [nodo_gen2("R1", "Restriccion", "Compañías", {"descripcion": frase})], "edges": []})
caso("F3 pasa: umbral 5.000 → resuelto", RK.t_bkl_0023(ctx_sintetico(g_ok))["estado"] == "resuelto")
caso("F3 contraejemplo: umbral 2.500 → persiste", RK.t_bkl_0023(ctx_sintetico(g_mal))["estado"] == "persiste")
caso("F3: sin umbral → no_aplicable (no PASS vacuo)", RK.t_bkl_0023(ctx_sintetico(g_sin))["estado"] == "no_aplicable")
caso("F3: sin nodo → no_aplicable", RK.t_bkl_0023(ctx_sintetico(RK.Grafo({"nodes": [], "edges": []})))["estado"] == "no_aplicable")
# F4 arista presente / ausente
caso("F4 pasa: arista por id destino", G.arista("Restriccion_x", "establecida_en", tgt="TextoOrdenado_cap"))
caso("F4 pasa: arista por tipo destino", G.arista("Restriccion_x", "establecida_en", tgt_type="TextoOrdenado"))
caso("F4 contraejemplo: relación ausente", not G.arista("Restriccion_x", "aplica_a", tgt_type="Sujeto"))
caso("F4 contraejemplo: destino de otro tipo", not G.arista("Restriccion_x", "establecida_en", tgt_type="Sujeto"))
# F5 rank en buscar_nodos (retriever sintético con la interfaz de GraphIndex)
idx = IndiceFalso(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"])
caso("F5 pasa: rank 1-based del primer id objetivo", RK.rank_de(idx, "q", {"c", "k"}, 10) == 3)
caso("F5 contraejemplo: objetivo fuera de la ventana pedida → None", RK.rank_de(idx, "q", {"m"}, 10) is None)
caso("F5: el limite declarado ≥ rank esperado lo hace visible (bancos 13)", RK.rank_de(idx, "q", {"m"}, 13) == 13)
caso("F5: tope 50 del harness", RK.rank_de(idx, "q", {"m"}, 500) == 13)
filas = RK.evaluar_consultas(idx, [("q", {"o1": RK._obj({"c"}, 3), "o2": RK._obj({"m"}, 13, limite=13), "o3": RK._obj({"z"}, None), "o4": RK._obj({"b"}, None)}, "sint")])
o = {x["objetivo"]: x for x in filas[0]["objetivos"]}
caso("F5: coincide_sellado con rank numérico", o["o1"]["coincide_sellado"] and o["o1"]["en_ventana"])
caso("F5: limite 13 declarado → en ventana y coincide", o["o2"]["coincide_sellado"] and o["o2"]["en_ventana"] and filas[0]["limite_pedido"] == 13)
caso("F5: esperado None = fuera del top-10 → coincide si ausente", o["o3"]["coincide_sellado"] and not o["o3"]["en_ventana"])
caso("F5 contraejemplo: esperado None pero rank 2 → no coincide", not o["o4"]["coincide_sellado"])
ok_rk, n_f, n_c = RK.alcanzabilidad_ok(filas)
caso("F5: alcanzabilidad cuenta solo objetivos con rank sellado numérico", ok_rk and n_c == 2 and n_f == 0)
filas2 = RK.evaluar_consultas(idx, [("q", {"o1": RK._obj({"m"}, 1)}, "sint")])
caso("F5 contraejemplo: objetivo fuera de ventana → alcanzabilidad falla", RK.alcanzabilidad_ok(filas2) == (False, 1, 1))

# --------------------------------------------------------------------------- #
# 3. Política de cuarentena en sus dos valores (T7 y BKL-0019)                 #
# --------------------------------------------------------------------------- #
CAT_IDS = frozenset(["Sujeto_sujeto", "Sujeto_banco", "Sujeto_contraparte", "Sujeto_rol_x"])


def g_politica(rel, cuarentena=True, target="Sujeto_contraparte"):
    return RK.Grafo({"nodes": [nodo_gen2("Sujeto_contraparte", "Sujeto", "Contrapartes", {"nivel": "clase"}),
                               nodo_gen2("Sujeto_propuesto_inversor", "Sujeto", "Inversor", {"nivel": "propuesto", "cuarentena": cuarentena}),
                               nodo_gen2("Sujeto_ajeno", "Sujeto", "Ajeno", {"nivel": "instancia"}) if target == "Sujeto_ajeno" else nodo_gen2("Sujeto_banco", "Sujeto", "Bancos", {"nivel": "clase"})],
                     "edges": [arista("Sujeto_propuesto_inversor", rel, target, rol_fuente="cuarentena_laudada" if rel == "subclase_de" else "cuarentena_flaggeada")]})


r = RK.t7_cuarentena(g_politica("subclase_de"), CAT_IDS, "laudada")
caso("T7 laudada: subclase_de desde propuesto a catálogo → pasa", r["pass"], str(r["malos"]))
r = RK.t7_cuarentena(g_politica("subclase_de"), CAT_IDS, "flaggeada")
caso("T7 flaggeada: subclase_de desde propuesto → falla", not r["pass"] and r["malos"] == [("Sujeto_propuesto_inversor", "subclase_de desde propuesto")])
r = RK.t7_cuarentena(g_politica("padre_sugerido"), CAT_IDS, "flaggeada")
caso("T7 flaggeada: padre_sugerido a catálogo → pasa (41/41 en r1)", r["pass"] and r["n_padre_sugerido"] == 1)
r = RK.t7_cuarentena(g_politica("padre_sugerido", cuarentena="true"), CAT_IDS, "flaggeada")
caso("T7: cuarentena cadena \"true\" (gen 3) → pasa", r["pass"])
r = RK.t7_cuarentena(g_politica("subclase_de", cuarentena=True), CAT_IDS, "laudada")
caso("T7: cuarentena booleana True (gen 2) → pasa (sin los 11 falsos FAIL)", r["pass"])
r = RK.t7_cuarentena(g_politica("subclase_de", cuarentena="false"), CAT_IDS, "laudada")
caso("T7 contraejemplo: cuarentena \"false\" → «sin cuarentena=true»", not r["pass"] and ("Sujeto_propuesto_inversor", "sin cuarentena=true") in r["malos"])
r = RK.t7_cuarentena(g_politica("padre_sugerido", target="Sujeto_ajeno"), CAT_IDS, "flaggeada")
caso("T7 contraejemplo: padre_sugerido fuera de catálogo + Sujeto fuera de catálogo", not r["pass"] and len(r["malos"]) == 1 and r["sujetos_fuera_catalogo_no_propuestos"] == ["Sujeto_ajeno"])
r = RK.t7_cuarentena(g_politica("subclase_de", target="Sujeto_ajeno"), CAT_IDS, "laudada")
caso("T7 laudada contraejemplo: subclase_de a id fuera de catálogo → falla", not r["pass"])
caso("T7: sin Sujetos → no_aplicable (vacuo)", RK.t_t7(ctx_sintetico(RK.Grafo({"nodes": [n2], "edges": []})))["estado"] == "no_aplicable")
# BKL-0019 con las dos políticas sobre un sujeto de C4 localizado por label
g19 = RK.Grafo({"nodes": [nodo_gen2("Sujeto_contraparte", "Sujeto", "Contrapartes", {"nivel": "clase"}),
                          nodo_gen2("Sujeto_propuesto_inv", "Sujeto", "Inversor", {"nivel": "propuesto", "cuarentena": True})],
                "edges": [arista("Sujeto_propuesto_inv", "subclase_de", "Sujeto_contraparte", rol_fuente="cuarentena_laudada")]})
caso("BKL-0019 laudada: subclase_de presente en todos los presentes → resuelto", RK.t_bkl_0019(ctx_sintetico(g19, "laudada"))["estado"] == "resuelto")
caso("BKL-0019 flaggeada: sin padre_sugerido → persiste", RK.t_bkl_0019(ctx_sintetico(g19, "flaggeada"))["estado"] == "persiste")
caso("BKL-0019: ninguno de los 8 presente → no_aplicable", RK.t_bkl_0019(ctx_sintetico(RK.Grafo({"nodes": [], "edges": []})))["estado"] == "no_aplicable")

# --------------------------------------------------------------------------- #
# 4. T4: exclusión de rol_fuente cuarentena_laudada (decisión 8)               #
# --------------------------------------------------------------------------- #
REL = ("subclase_de", "miembro_de", "instancia_de", "parte_de")
esq_nodos = [nodo_gen2("Sujeto_sujeto", "Sujeto", "Sujetos", {"nivel": "clase"}, rol_fuente="esqueleto"),
             nodo_gen2("Sujeto_banco", "Sujeto", "Bancos", {"nivel": "clase"}, rol_fuente="esqueleto"),
             nodo_gen2("Sujeto_contraparte", "Sujeto", "Contrapartes", {"nivel": "clase"}, rol_fuente="esqueleto"),
             nodo_gen2("Sujeto_rol_x", "Sujeto", "Rol X", {"nivel": "rol"}, rol_fuente="esqueleto"),
             nodo_gen2("Sujeto_propuesto_inversor", "Sujeto", "Inversor", {"nivel": "propuesto", "cuarentena": True})]
esq_aristas = [arista("Sujeto_banco", "subclase_de", "Sujeto_sujeto", rol_fuente="esqueleto"),
               arista("Sujeto_contraparte", "subclase_de", "Sujeto_sujeto", rol_fuente="esqueleto"),
               arista("Sujeto_banco", "miembro_de", "Sujeto_rol_x", rol_fuente="esqueleto")]
laudada = arista("Sujeto_propuesto_inversor", "subclase_de", "Sujeto_contraparte", rol_fuente="cuarentena_laudada")
ref = RK.Grafo({"nodes": esq_nodos, "edges": esq_aristas + [laudada]}, "ref", "r" * 64)
v = RK.t4_paridad(ref, ref, REL)
caso("T4: la referencia excluye cuarentena_laudada (4 relaciones de esqueleto → 3 triplas)", v["aristas_esqueleto_referencia"] == 3 and v["aristas_excluidas_referencia_cuarentena_laudada"] == 1)
caso("T4: la referencia pasa contra sí misma (KG-Refinado 90 → 82)", v["pass"] and v["aristas_esqueleto_en_grafo"] == 3 and v["aristas_excluidas_grafo_cuarentena_laudada"] == 1)
g_r1 = RK.Grafo({"nodes": esq_nodos, "edges": esq_aristas}, "g", "g" * 64)
caso("T4: grafo sin la laudada pasa igual (r1: 82)", RK.t4_paridad(g_r1, ref, REL)["pass"])
g_falta = RK.Grafo({"nodes": esq_nodos, "edges": esq_aristas[:2]}, "g", "g" * 64)
v = RK.t4_paridad(g_falta, ref, REL)
caso("T4 contraejemplo: falta una tripla de esqueleto → falla", not v["pass"] and v["faltan_triplas"] == [("Sujeto_banco", "miembro_de", "Sujeto_rol_x")])
g_sobra = RK.Grafo({"nodes": esq_nodos, "edges": esq_aristas + [arista("Sujeto_rol_x", "parte_de", "Sujeto_sujeto")]}, "g", "g" * 64)
caso("T4 contraejemplo: tripla de esqueleto de más (no laudada) → falla por conteo", not RK.t4_paridad(g_sobra, ref, REL)["pass"])
g_sin_nodo = RK.Grafo({"nodes": esq_nodos[1:], "edges": esq_aristas[:2]}, "g", "g" * 64)
caso("T4 contraejemplo: falta un nodo de esqueleto", RK.t4_paridad(g_sin_nodo, ref, REL)["faltan_nodos"] == ["Sujeto_sujeto"])
# R-T4 (U-R2-CODIGO, R5.a): el esqueleto esperado es el de build_skeleton sobre el catálogo
SK = ({n["id"] for n in esq_nodos[:4]}, {(e["source"], e["relation"], e["target"]) for e in esq_aristas})
ctx4 = ctx_sintetico(g_r1, esqueleto_catalogo=SK, relaciones_esqueleto=REL)
caso("T4 (R-T4) vía Contexto: esqueleto igual al del catálogo → resuelto", RK.t_t4(ctx4)["estado"] == "resuelto")
caso("T4 (R-T4): la laudada se excluye del grafo bajo prueba (KG-Refinado)",
     RK.t_t4(ctx_sintetico(ref, esqueleto_catalogo=SK, relaciones_esqueleto=REL))["estado"] == "resuelto")
v = RK.t4_esqueleto_catalogo(g_falta, SK[0], SK[1], REL)
caso("T4 (R-T4) contraejemplo: falta una tripla del catálogo → falla", not v["pass"] and v["faltan_triplas"] == [["Sujeto_banco", "miembro_de", "Sujeto_rol_x"]])
v = RK.t4_esqueleto_catalogo(g_sobra, SK[0], SK[1], REL)
caso("T4 (R-T4) contraejemplo: tripla de esqueleto de más → falla (sobran)", not v["pass"] and v["sobran_triplas"] == [["Sujeto_rol_x", "parte_de", "Sujeto_sujeto"]])
caso("T4 (R-T4) contraejemplo: falta un nodo del catálogo", RK.t4_esqueleto_catalogo(g_sin_nodo, SK[0], SK[1], REL)["faltan_nodos"] == ["Sujeto_sujeto"])
caso("T4: grafo sin ninguna arista de esqueleto → no_aplicable", RK.t_t4(ctx_sintetico(RK.Grafo({"nodes": esq_nodos, "edges": []}, "g", "g" * 64), esqueleto_catalogo=SK, relaciones_esqueleto=REL))["estado"] == "no_aplicable")

# --------------------------------------------------------------------------- #
# 5. T5 por (ancla origen, ancla destino, evidencia) e I3–I5                   #
# --------------------------------------------------------------------------- #
muestra = [{"n": 1, "source_ancla": "cap::1.2", "target_ancla": "cla::6.5.2", "destino": "cla::6.5.2", "target_type": "Obligacion",
            "evidencia_verbatim": "ver punto 6.5.2"}]
src = nodo_gen3("Ex", "Excepcion", "Origen", punto="1.2")
tgt = nodo_gen3("Ob", "Obligacion", "Destino", punto="6.5.2", archivo=CLA_PDF, to="cla")
tgt_d = nodo_gen3("De", "Definicion", "Destino definición", punto="6.5.2", archivo=CLA_PDF, to="cla")


def g_t5(rel="referencia", ev="ver punto 6.5.2", destino="cla::6.5.2", target="Ob", rol="referencia_cruzada"):
    return RK.Grafo({"nodes": [src, tgt, tgt_d], "edges": [arista("Ex", rel, target, rol_fuente=rol,
                                                                   props={"evidencia": ev, "destino": destino}, gen=3)]})


caso("T5 (R-T5) pasa: referencia por anclas, destino, tipo y número de punto", RK.t_t5(ctx_sintetico(g_t5(), muestra30=muestra))["estado"] == "resuelto")
r5 = RK.t_t5(ctx_sintetico(g_t5(ev="según el punto 6.5.2. de estas normas"), muestra30=muestra))
caso("T5 (R-T5) pasa con otra evidencia que nombra el mismo punto (no verbatim)", r5["estado"] == "resuelto" and r5["valores"]["presentes_verbatim"] == 0)
caso("T5 (R-T5) lee remite_a (perfil r2) con la función de remisiones",
     RK.t_t5(ctx_sintetico(g_t5(rel="remite_a", rol=None), muestra30=muestra))["estado"] == "resuelto")
caso("T5 (R-T5) contraejemplo: evidencia sin el número de punto → persiste",
     RK.t_t5(ctx_sintetico(g_t5(ev="ver el anexo"), muestra30=muestra))["estado"] == "persiste")
caso("T5 (R-T5) contraejemplo: destino distinto → persiste",
     RK.t_t5(ctx_sintetico(g_t5(destino="cla::6.5"), muestra30=muestra))["estado"] == "persiste")
r5 = RK.t_t5(ctx_sintetico(g_t5(target="De"), muestra30=muestra))
caso("T5 (R-T5) contraejemplo: destino de otro tipo → persiste, presente sin tipo",
     r5["estado"] == "persiste" and r5["valores"]["fallas"][0]["presente_sin_tipo"] and r5["valores"]["presentes_rt5_sin_tipo"] == 1)
caso("T5 (R-T5): una referencia sin rol_fuente referencia_cruzada no es remisión",
     RK.t_t5(ctx_sintetico(g_t5(rol=None), muestra30=muestra))["estado"] == "no_aplicable")
caso("T5: sin remisiones con evidencia → no_aplicable", RK.t_t5(ctx_sintetico(G, muestra30=muestra))["estado"] == "no_aplicable")
g_dup = RK.Grafo({"nodes": [n2, dict(n2)], "edges": [arista("Restriccion_x", "referencia", "Restriccion_x")] * 2})
caso("I3 contraejemplo: ids y triplas duplicados → persiste", RK.t_i3(ctx_sintetico(g_dup))["estado"] == "persiste")
caso("I3 pasa", RK.t_i3(ctx_sintetico(G))["estado"] == "resuelto")
caso("I4 pasa", RK.t_i4(ctx_sintetico(G))["estado"] == "resuelto")
caso("I4 contraejemplo: arista colgante → persiste", RK.t_i4(ctx_sintetico(RK.Grafo({"nodes": [n2], "edges": [arista("Restriccion_x", "referencia", "nadie")]})))["estado"] == "persiste")
caso("I5 pasa (gen 2 con solo `provenance`, gen 3 con `provenances`)", RK.t_i5(ctx_sintetico(G))["estado"] == "resuelto")
caso("I5 contraejemplo: nodo sin provenance → persiste", RK.t_i5(ctx_sintetico(RK.Grafo({"nodes": [{"id": "x", "type": "Obligacion", "label": "x", "properties": {}}], "edges": []})))["estado"] == "persiste")

# --------------------------------------------------------------------------- #
# 6. E4-a6 con un resolvedor sintético (ambigüedad)                            #
# --------------------------------------------------------------------------- #
def e4_stub(respuestas: dict, ambiguas: int = 0):
    class R:
        @staticmethod
        def resolver_label(label, padre, idx):
            return respuestas.get(label, (None, "sin_match_en_catalogo", []))
    idx = {("label_exacto", "k%d" % i): "__AMBIGUO__" for i in range(ambiguas)}
    return {"r1_e4": R, "e2_lib": None, "r1_comun": None, "indice": idx}


g6 = RK.Grafo({"nodes": [nodo_gen2("Sujeto_banco", "Sujeto", "Bancos", {"nivel": "clase", "alias_resueltos": ["Banco comercial"]}),
                         nodo_gen2("Sujeto_propuesto_z", "Sujeto", "Zeta", {"nivel": "propuesto", "cuarentena": True})], "edges": []})
ctx6 = ctx_sintetico(g6, e4=e4_stub({"Banco comercial": ("Sujeto_banco", "resuelto_por_alias_exacto", [("alias_exacto", "Sujeto_banco")]),
                                     "Zeta": (None, "ambiguo", [("label_exacto", "Sujeto_banco"), ("id_slug", "Sujeto_contraparte")])}))
caso("E4-a6 pasa: alias_resueltos re-resuelve a su portador; propuesto ambiguo sigue en cuarentena", RK.t_e4_a6(ctx6)["estado"] == "resuelto")
ctx6b = ctx_sintetico(g6, e4=e4_stub({"Banco comercial": (None, "ambiguo", [("alias_exacto", "Sujeto_banco"), ("id_slug", "Sujeto_contraparte")])}, ambiguas=1))
caso("E4-a6 contraejemplo: alias resuelto que re-resuelve ambiguo → persiste", RK.t_e4_a6(ctx6b)["estado"] == "persiste")
caso("E4-a1 contraejemplo: propuesto resoluble por label_exacto no resuelto → persiste",
     RK.t_e4_a1(ctx_sintetico(g6, e4=e4_stub({"Zeta": ("Sujeto_banco", "resuelto_por_label_exacto", [("label_exacto", "Sujeto_banco")])})))["estado"] == "persiste")
caso("E4-a1 pasa: sin propuestos resolubles", RK.t_e4_a1(ctx_sintetico(g6, e4=e4_stub({})))["estado"] == "resuelto")
caso("E4-a1: sin propuestos → no_aplicable", RK.t_e4_a1(ctx_sintetico(G, e4=e4_stub({})))["estado"] == "no_aplicable")

# --------------------------------------------------------------------------- #
# 7. Regresión contra fixture sintética (código de salida ≠ 0)                 #
# --------------------------------------------------------------------------- #
items = [{"id": "I3", "estado": "resuelto"}, {"id": "I4", "estado": "resuelto"}, {"id": "T1", "estado": "persiste"}, {"id": "T2", "estado": "resuelto"}]
esp = {"items": {"I3": {"estado": "resuelto"}, "I4": {"estado": "persiste", "evidencia": "sint:1"}, "T1": {"estado": "persiste"}, "T2": {"estado": None}, "T3": {"estado": "resuelto"}}}
reg = RK.computar_regresion(items, esp)
caso("regresión: estado medido ≠ esperado cuenta como regresión", reg["n_regresiones"] == 1 and reg["regresiones"][0]["item"] == "I4" and reg["regresiones"][0]["evidencia_del_esperado"] == "sint:1")
caso("regresión: «persiste» esperado no es fallo; null = NO VERIFICADA no computa", "T1" not in [x["item"] for x in reg["regresiones"]] and reg["no_verificadas"] == ["T2"] and reg["sin_medido"] == ["T3"])
caso("regresión: código de salida 1 con regresión, 0 sin ella", RK.codigo_salida(reg) == 1 and RK.codigo_salida({"n_regresiones": 0}) == 0 and RK.codigo_salida(None) == 0)
rk_m = {"consultas_coinciden_sellado": 26, "objetivos_coinciden_sellado": 75}
reg2 = RK.computar_regresion(items, {"items": {"I3": {"estado": "resuelto"}}, "ranks_sellados": {"consultas": 27, "objetivos": 75}}, rk_m)
caso("regresión: ranks sellados esperados que no coinciden → regresión RANKS_SELLADOS", reg2["n_regresiones"] == 1 and reg2["regresiones"][0]["item"] == "RANKS_SELLADOS")
caso("partición declarada 46 = 19 / 23 / 4, 15 retriever, grupos 12/12/12/10; ítems del perfil r2 aparte",
     RK.verificar_particion() == {"items": 46, "convertibles": 19, "con_condicion": 23, "no_convertibles": 4, "retriever": 15,
                                  "por_grupo": {"i-BKL": 12, "i-RT": 12, "ii": 12, "iii": 10},
                                  "items_r2": ["RT-C6-5", "EJ-cla-5.1.1.1", "LN-1", "LN-2", "LN-3", "LN-4", "LN-5", "LN-6", "LN-7", "LN-8"]})
ids = [t["id"] for t in RK.TESTS]
caso("los 4 no convertibles tienen estado fijo no_aplicable", all(RK.TESTS[ids.index(i)]["fn"](None)["estado"] == "no_aplicable" for i in ("BKL-0026", "BKL-0027", "I1", "I2")))
caso("los cinco verificado sin evento de aplicación llevan la nota", all(RK.NOTA_SIN_APLICACION in RK.TESTS[ids.index(i)]["nota"] for i in ("BKL-0007", "BKL-0026", "BKL-0027", "BKL-0028", "BKL-0029")))
caso("todo test declara forma, direccionamiento y evidencia con path", all(t["forma"] and t["direccionamiento"] and (":" in t["evidencia"] or t["evidencia"].startswith("reports/")) for t in RK.TESTS))

# End-to-end: main() con kg y fixture sintéticos → código de salida 1
with tempfile.TemporaryDirectory(prefix="selftest_regression_kg_") as tmp:
    tmp = Path(tmp)
    kg_path = tmp / "kg_sintetico.json"
    kg_path.write_text(json.dumps({"nodes": [n2, nodo_gen2("TextoOrdenado_cap", "TextoOrdenado", "CapMin", {"archivo": CAP_PDF})],
                                   "edges": [arista("Restriccion_x", "establecida_en", "TextoOrdenado_cap")]}, ensure_ascii=False), encoding="utf-8")
    cat_path = tmp / "catalogo_sintetico.json"
    cat_path.write_text(json.dumps(CATALOGO), encoding="utf-8")
    sha = hashlib.sha256(kg_path.read_bytes()).hexdigest()
    fx = tmp / "esperado_sintetico.json"
    fx.write_text(json.dumps({"estado_esperado": {"sintetico": {"kg_sha256": sha, "generacion": 2, "politica_cuarentena": "laudada",
                                                               "items": {"I3": {"estado": "resuelto"}, "I4": {"estado": "persiste", "evidencia": "sint"}, "I5": {"estado": None}}}}}), encoding="utf-8")
    base = ["--kg", str(kg_path), "--generacion", "2", "--catalogo", str(cat_path), "--politica-cuarentena", "laudada", "--solo", "I3,I4,I5"]
    import io, contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = RK.main(base + ["--esperado", str(fx), "--out", str(tmp / "salida.md")])
    caso("end-to-end: regresión contra fixture sintética → código de salida 1", rc == 1, f"rc={rc}")
    caso("end-to-end: --out escribe .md y .json", (tmp / "salida.md").exists() and (tmp / "salida.json").exists())
    sal = json.loads((tmp / "salida.json").read_text(encoding="utf-8"))
    caso("end-to-end: la salida registra la regresión I4 y la NO VERIFICADA I5", sal["regresion"]["n_regresiones"] == 1 and sal["regresion"]["no_verificadas"] == ["I5"])
    with contextlib.redirect_stdout(buf):
        rc0 = RK.main(base)
    caso("end-to-end: sin --esperado no computa regresión → 0", rc0 == 0 and not (tmp / "otra.md").exists())
    fx.write_text(json.dumps({"estado_esperado": {"sintetico": {"kg_sha256": sha, "generacion": 2, "politica_cuarentena": "laudada",
                                                               "items": {"I3": {"estado": "resuelto"}, "I4": {"estado": "resuelto"}}}}}), encoding="utf-8")
    with contextlib.redirect_stdout(buf):
        rc_ok = RK.main(base + ["--esperado", str(fx)])
    caso("end-to-end: fixture coincidente → 0", rc_ok == 0)
    fx.write_text(json.dumps({"linea_de_base_observada": {"sintetico": {"kg_sha256": sha, "items": {"I4": {"estado": "persiste"}}}}}), encoding="utf-8")
    with contextlib.redirect_stdout(buf):
        rc_lb = RK.main(base + ["--esperado", str(fx)])
    caso("end-to-end: entrada de línea de base observada no computa regresión → 0", rc_lb == 0)
    fx.write_text(json.dumps({"estado_esperado": {"sintetico": {"kg_sha256": sha, "generacion": 2, "politica_cuarentena": "flaggeada", "items": {"I4": {"estado": "persiste"}}}}}), encoding="utf-8")
    with contextlib.redirect_stdout(buf):
        rc_p = RK.main(base + ["--esperado", str(fx)])
    caso("end-to-end: parámetros distintos de la fixture → no computa, código 2", rc_p == 2)
    try:
        with contextlib.redirect_stdout(buf):
            RK.main(["--kg", str(kg_path), "--generacion", "3", "--catalogo", str(cat_path), "--politica-cuarentena", "laudada", "--solo", "I3"])
        caso("end-to-end: --generacion contradice el formato detectado → SystemExit", False)
    except SystemExit:
        caso("end-to-end: --generacion contradice el formato detectado → SystemExit", True)

# --------------------------------------------------------------------------- #
# RT-C6-5 (U-R2-CODIGO, R4.d): la cláusula de mutuales como test de persistencia
PRO_PDF = "TO_proteccion_usuarios_servicios_financieros_actual.pdf"
_n1 = "excepto que se trate de asociaciones mutuales o cooperativas"
g_c6_sin = RK.Grafo({"nodes": [nodo_gen3("Ex1", "Excepcion", "Mutuales", {"descripcion": _n1}, punto="1.1.2.5",
                                         archivo=PRO_PDF, to="pro")], "edges": []})
g_c6_con = RK.Grafo({"nodes": [nodo_gen3("Ex1", "Excepcion", "Mutuales",
                                         {"descripcion": _n1 + ", por las financiaciones que otorguen"},
                                         punto="1.1.2.5", archivo=PRO_PDF, to="pro")], "edges": []})
caso("RT-C6-5: N1 sin la cláusula → persiste", RK.t_rt_c6_5(ctx_sintetico(g_c6_sin))["estado"] == "persiste")
caso("RT-C6-5: N1 con la cláusula → resuelto", RK.t_rt_c6_5(ctx_sintetico(g_c6_con))["estado"] == "resuelto")
caso("RT-C6-5: sin N1 → no_aplicable", RK.t_rt_c6_5(ctx_sintetico(RK.Grafo({"nodes": [], "edges": []})))["estado"] == "no_aplicable")
caso("RT-C6-5 es ítem del perfil r2, fuera de la partición del inventario",
     RK.convertibilidad("RT-C6-5") == "perfil r2" and "RT-C6-5" not in RK.CON_CONDICION)

# --------------------------------------------------------------------------- #
# U-R2-CODIGO, R5: remisiones, R-E4a8, BKL-0028, umbrales, ejemplo, LN, censos #
# --------------------------------------------------------------------------- #
import remisiones as REM  # noqa: E402

e_ref = {"relation": "referencia", "rol_fuente": "referencia_cruzada", "properties": {"destino": "cap::1.2", "evidencia": "punto 1.2"}}
e_rem = {"relation": "remite_a", "properties": {"alcance": "interna", "destino": "cap::1.2", "evidencia": "punto 1.2"}}
caso("remisiones: reconoce las dos formas", REM.es_remision(e_ref) and REM.es_remision(e_rem)
     and REM.forma_remision(e_ref) == "referencia" and REM.forma_remision(e_rem) == "remite_a")
caso("remisiones: referencia TextoOrdenado→Comunicacion (sin rol_fuente) no es remisión",
     not REM.es_remision({"relation": "referencia", "properties": {}}) and REM.forma_remision({"relation": "aplica_a"}) is None)
caso("remisiones: firma de remite_a (7 tipos de contenido; destino también TextoOrdenado)",
     REM.firma_remite_a_ok("Condicion", "Definicion") and REM.firma_remite_a_ok("Potestad", "TextoOrdenado")
     and not REM.firma_remite_a_ok("Sujeto", "Obligacion") and not REM.firma_remite_a_ok("Obligacion", "Comunicacion")
     and len(REM.TIPOS_CONTENIDO) * (len(REM.TIPOS_CONTENIDO) + 1) == 56)
caso("remisiones: alcance esperado (to_entero / interna / externa)",
     REM.alcance_esperado("cap::TO", "cap", True) == "to_entero" and REM.alcance_esperado("cap::1.2", "cap", False) == "interna"
     and REM.alcance_esperado("cla::3.7", "cap", False) == "externa" and REM.alcance_esperado(None, "cap", False) is None)

# R-E4a8: la tabla junto al kg.json bajo prueba
with tempfile.TemporaryDirectory(prefix="selftest_e4a8_") as tmp8:
    tmp8 = Path(tmp8)
    g8 = {"nodes": [nodo_gen3("Sujeto_banco", "Sujeto", "Bancos", {"nivel": "clase", "alias_resueltos": ["Banca"]})], "edges": []}
    (tmp8 / "kg.json").write_text(json.dumps(g8), encoding="utf-8")
    G8 = RK.Grafo.desde_ruta(tmp8 / "kg.json")
    caso("E4-a8 (R-E4a8): sin e4_propuestos.json junto al kg.json → no_aplicable", RK.t_e4_a8(ctx_sintetico(G8))["estado"] == "no_aplicable")
    (tmp8 / "e4_propuestos.json").write_text(json.dumps([{"id_propuesto": "Sujeto_propuesto_banca", "resuelto_a": "Sujeto_banco",
                                                           "label": "Banca", "estado": "resuelto"}]), encoding="utf-8")
    caso("E4-a8 (R-E4a8): la tabla del propio ensamblado → resuelto", RK.t_e4_a8(ctx_sintetico(G8))["estado"] == "resuelto")
    (tmp8 / "e4_propuestos.json").write_text(json.dumps([{"id_propuesto": "Sujeto_propuesto_banca", "resuelto_a": "Sujeto_banco",
                                                           "label": "Bancario", "estado": "resuelto"}]), encoding="utf-8")
    caso("E4-a8 (R-E4a8) contraejemplo: alias no registrado en el id resuelto → persiste", RK.t_e4_a8(ctx_sintetico(G8))["estado"] == "persiste")

# BKL-0028: los tres ids «del exterior» esperados, sin contar el del banco central
CAT28 = {"version": "3.1", "clases": [{"id": i, "label": i, "nivel": "clase", "alias": []} for i in
                                     ("Sujeto_entidad_financiera", "Sujeto_banco", "Sujeto_entidad_cambiaria",
                                      "Sujeto_entidad_financiera_del_exterior", "Sujeto_banco_del_exterior",
                                      "Sujeto_entidad_cambiaria_del_exterior", "Sujeto_banco_central_del_exterior")], "roles": []}
g28 = RK.Grafo({"nodes": [nodo_gen3("Sujeto_banco_del_exterior", "Sujeto", "Bancos del exterior", {"nivel": "clase"})], "edges": []})
r28 = RK.t_bkl_0028(RK.Contexto(g28, RK.Catalogo(CAT28, "c", "0" * 64), 3, "flaggeada"))
caso("BKL-0028: tres ids esperados en el catálogo, sin alias del exterior y presentes → resuelto; no cuenta el banco central",
     r28["estado"] == "resuelto" and "Sujeto_banco_central_del_exterior" not in r28["valores"]["ids_separados_del_exterior"])
CAT28b = dict(CAT28, clases=[c for c in CAT28["clases"] if c["id"] != "Sujeto_entidad_cambiaria_del_exterior"])
r28b = RK.t_bkl_0028(RK.Contexto(g28, RK.Catalogo(CAT28b, "c", "0" * 64), 3, "flaggeada"))
caso("BKL-0028 contraejemplo: falta uno de los tres (el del banco central no lo reemplaza) → persiste", r28b["estado"] == "persiste")

# BKL-0006 y BKL-0023 con la lista de umbrales (L-ESQ-R2 §1.5)
def um(valor):
    return [{"tramo": "x", "valor": valor, "unidad": "moneda", "moneda": "ARS", "comparacion": "minimo_inclusivo", "tramo_verificado": "exacta"}]


def g23(valor):
    return RK.Grafo({"nodes": [nodo_gen3("R", "Restriccion", "c3", {"descripcion": "compañías financieras que realicen, en forma directa, "
                                                                    "operaciones de comercio exterior", "umbrales": um(valor)})], "edges": []})


caso("BKL-0023 (lista): valor normalizado 5000000000 ARS → resuelto", RK.t_bkl_0023(ctx_sintetico(g23("5000000000")))["estado"] == "resuelto")
caso("BKL-0023 (lista) contraejemplo: 2500000000 → persiste", RK.t_bkl_0023(ctx_sintetico(g23("2500000000")))["estado"] == "persiste")
g06 = RK.Grafo({"nodes": [nodo_gen3("Rb", "Restriccion", "Exigencia básica bancos", {"descripcion": "exigencia básica bancos", "umbrales": um("5000000000")}),
                          nodo_gen3("Rr", "Restriccion", "Exigencia básica restantes entidades",
                                    {"descripcion": "exigencia básica restantes entidades", "umbrales": um("2500000000")})], "edges": []})
caso("BKL-0006 (lista): bancos 5.000 / restantes 2.500 desde el valor normalizado → resuelto", RK.t_bkl_0006(ctx_sintetico(g06, indice=IndiceFalso([])))["estado"] == "resuelto")
g06i = RK.Grafo({"nodes": [nodo_gen3("Rb", "Restriccion", "Exigencia básica bancos", {"descripcion": "exigencia básica bancos", "umbrales": um("2500000000")}),
                           nodo_gen3("Rr", "Restriccion", "Exigencia básica restantes entidades",
                                     {"descripcion": "exigencia básica restantes entidades", "umbrales": um("5000000000")})], "edges": []})
caso("BKL-0006 (lista) contraejemplo: tabla invertida → persiste", RK.t_bkl_0006(ctx_sintetico(g06i, indice=IndiceFalso([])))["estado"] == "persiste")

# Test del ejemplo cla::5.1.1.1
def n_cla(nid, tipo, punto="5.1.1.1", props=None):
    return nodo_gen3(nid, tipo, nid, props or {}, punto=punto, archivo=CLA_PDF, to="cla")


def ar3(s_, r, t, props=None, **extra):
    e = arista(s_, r, t, props=props, gen=3)
    e.update(extra)
    return e


elem = [{"tramo": "dos veces", "valor": "2", "unidad": "veces", "comparacion": "minimo_estricto", "base_destino": "cla::3.7"}]
g_ej = {"nodes": [n_cla("Op", "Operacion"), n_cla("C1", "Condicion", props={"umbrales": elem}), n_cla("C2", "Condicion"),
                  n_cla("D37", "Definicion", punto="3.7")],
        "edges": [ar3("C1", "condicion_de", "Op", no_verificada_e3=True), ar3("C2", "condicion_de", "Op", no_verificada_e3=True),
                  ar3("C1", "remite_a", "D37", props={"alcance": "interna", "destino": "cla::3.7", "evidencia": "punto 3.7"})]}
r_ej = RK.t_ej_cla_5111(ctx_sintetico(RK.Grafo(g_ej), perfil="r2"))
caso("EJ-cla-5.1.1.1 (r2a): dos condicion_de + remite_a a cla::3.7 → resuelto; (iii) informativo; no verificadas por E3 declaradas",
     r_ej["estado"] == "resuelto" and r_ej["valores"]["iii_informativo_umbral_minimo_estricto_2_veces_base_cla_3_7"]
     and "no_verificada_e3" in r_ej["detalle"])
g_ej_ref = json.loads(json.dumps(g_ej))
g_ej_ref["edges"][2] = ar3("C1", "referencia", "D37", props={"destino": "cla::3.7", "evidencia": "punto 3.7"}, rol_fuente="referencia_cruzada")
caso("EJ-cla-5.1.1.1: en un grafo r2 la referencia no alcanza para (ii) → persiste",
     RK.t_ej_cla_5111(ctx_sintetico(RK.Grafo(g_ej_ref), perfil="r2"))["estado"] == "persiste")
caso("EJ-cla-5.1.1.1: en los perfiles existentes, la forma de origen (referencia) → resuelto",
     RK.t_ej_cla_5111(ctx_sintetico(RK.Grafo(g_ej_ref)))["estado"] == "resuelto")
g_r1ej = {"nodes": [n_cla("Op", "Operacion"), n_cla("R1", "Restriccion"), n_cla("R2", "Restriccion"), n_cla("O37", "Obligacion", punto="3.7")],
          "edges": [ar3("R1", "limita", "Op"), ar3("R2", "limita", "Op"),
                    ar3("R1", "referencia", "O37", props={"destino": "cla::3.7", "evidencia": "punto 3.7"}, rol_fuente="referencia_cruzada")]}
caso("EJ-cla-5.1.1.1 (estructura de r1): dos limita + referencia → resuelto", RK.t_ej_cla_5111(ctx_sintetico(RK.Grafo(g_r1ej)))["estado"] == "resuelto")
g_dev = {"nodes": [n_cla("Op", "Operacion"), n_cla("C1", "Condicion"), n_cla("C2", "Condicion")], "edges": []}
caso("EJ-cla-5.1.1.1 (desarrollo r1): Condicion aisladas y sin remisión → persiste", RK.t_ej_cla_5111(ctx_sintetico(RK.Grafo(g_dev)))["estado"] == "persiste")
caso("EJ-cla-5.1.1.1: sin nodos del punto → no_aplicable", RK.t_ej_cla_5111(ctx_sintetico(RK.Grafo({"nodes": [], "edges": []})))["estado"] == "no_aplicable")

# LN-1 a LN-8 (enums_r2.json real; marcas de nodo inyectadas)
MARCAS = ("cola_humana", "cola_chunks", "estado_e3", "colision_cross_to")


def ctx_r2(nodes, edges=(), **kw):
    return ctx_sintetico(RK.Grafo({"nodes": list(nodes), "edges": list(edges)}), perfil="r2", marcas_nodo_r2=MARCAS, **kw)


ob = nodo_gen3("Ob", "Obligacion", "Ob", {"descripcion": "d", "tipo": "calculo", "frecuencia": "mensual"})
caso("LN-*: con --perfil existente → no_aplicable", all(f(ctx_sintetico(RK.Grafo({"nodes": [ob], "edges": []})))["estado"] == "no_aplicable"
                                                     for f in (RK.t_ln_1, RK.t_ln_2, RK.t_ln_3, RK.t_ln_4, RK.t_ln_5, RK.t_ln_6, RK.t_ln_7, RK.t_ln_8)))
caso("LN-1 pasa: valores en la lista", RK.t_ln_1(ctx_r2([ob]))["estado"] == "resuelto")
ob_mal = json.loads(json.dumps(ob)); ob_mal["properties"]["frecuencia"] = "previa"
caso("LN-1 contraejemplo: frecuencia fuera de lista sin marca → persiste", RK.t_ln_1(ctx_r2([ob_mal]))["estado"] == "persiste")
ob_mal["fuera_de_lista"] = ["frecuencia"]
caso("LN-1: fuera de lista con la marca → resuelto (contado)", RK.t_ln_1(ctx_r2([ob_mal]))["valores"]["fuera_de_lista_marcados"] == {"Obligacion.frecuencia": 1})
ob_u = json.loads(json.dumps(ob)); ob_u["properties"]["umbrales"] = [{"tramo": "x", "valor": "1", "unidad": "lustros", "comparacion": "maximo_inclusivo", "tramo_verificado": "exacta"}]
caso("LN-1 contraejemplo: unidad del elemento de umbral fuera de lista sin marca → persiste", RK.t_ln_1(ctx_r2([ob_u]))["estado"] == "persiste")
caso("LN-2 pasa: claves definidas y marcas de nodo", RK.t_ln_2(ctx_r2([dict(ob, properties=dict(ob["properties"], cola_humana="true"))]))["estado"] == "resuelto")
caso("LN-2 contraejemplo: clave fuera de la definición en properties → persiste",
     RK.t_ln_2(ctx_r2([dict(ob, properties=dict(ob["properties"], plazo_o_frecuencia="x"))]))["estado"] == "persiste")
suj = nodo_gen3("Sujeto_banco", "Sujeto", "Bancos", {"nivel": "clase"})
e_suj = ar3("Ob", "aplica_a", "Sujeto_banco", sujeto_mencion="los bancos", mencion_verificada="exacta", metodo_resolucion="R1_label_exacto")
caso("LN-3 / LN-4 pasan: mención, verificación y método", RK.t_ln_3(ctx_r2([ob, suj], [e_suj]))["estado"] == "resuelto"
     and RK.t_ln_4(ctx_r2([ob, suj], [e_suj]))["estado"] == "resuelto")
e_sin = ar3("Ob", "aplica_a", "Sujeto_banco", mencion_verificada="ausente")
caso("LN-3 / LN-4 contraejemplos: sin mención (r2a) y sin método → persiste", RK.t_ln_3(ctx_r2([ob, suj], [e_sin]))["estado"] == "persiste"
     and RK.t_ln_4(ctx_r2([ob, suj], [e_sin]))["estado"] == "persiste")
caso("LN-3: la arista de esqueleto no cuenta", RK.t_ln_3(ctx_r2([ob, suj], [dict(e_sin, rol_fuente="esqueleto")]))["estado"] == "no_aplicable")
with tempfile.TemporaryDirectory(prefix="selftest_ln_") as tmpl:
    tmpl = Path(tmpl)
    prop_n = nodo_gen3("Sujeto_propuesto_x", "Sujeto", "X", {"nivel": "propuesto", "cuarentena": "true"})
    (tmpl / RK.REGISTRO_NO_MAPEADOS).write_text(json.dumps({"id_nodo": "Sujeto_propuesto_x", "estado": "cuarentena"}) + "\n", encoding="utf-8")
    caso("LN-5 pasa: registro y grafo coinciden", RK.t_ln_5(ctx_r2([prop_n], registro_dir=tmpl))["estado"] == "resuelto")
    caso("LN-5 contraejemplo: fila en cuarentena sin nodo → persiste", RK.t_ln_5(ctx_r2([], registro_dir=tmpl))["estado"] == "persiste")
    caso("LN-5: sin registro → no_aplicable", RK.t_ln_5(ctx_r2([prop_n], registro_dir=tmpl / "no"))["estado"] == "no_aplicable")

    class E4Stub:
        def __init__(self, cambia):
            self.cambia = cambia

        def indice_desde_lista(self, filas):
            return {}

        def reresolver_registro(self, filas, idx, rol, arch, sha):
            out = [dict(f, estado="resuelto") if self.cambia else dict(f) for f in filas]
            return {"filas": out, "resueltas_ahora": len(filas) if self.cambia else 0, "catalogo_sha256": sha}
    caso("LN-6 pasa: re-resolución idempotente (stub de r1_e4)",
         RK.t_ln_6(ctx_r2([prop_n], registro_dir=tmpl, e4={"r1_e4": E4Stub(False)}))["estado"] == "resuelto")
    caso("LN-6 contraejemplo: la re-resolución cambia el registro → persiste",
         RK.t_ln_6(ctx_r2([prop_n], registro_dir=tmpl, e4={"r1_e4": E4Stub(True)}))["estado"] == "persiste")
    caso("LN-7: sin registro de omisiones (r2a) → no_aplicable", RK.t_ln_7(ctx_r2([ob], registro_dir=tmpl))["estado"] == "no_aplicable")
    (tmpl / "omisiones.jsonl").write_text(json.dumps({"categoria": "tabla", "tramo_verificado": "exacta"}) + "\n"
                                          + json.dumps({"categoria": "otra", "tramo_verificado": "exacta"}) + "\n", encoding="utf-8")
    caso("LN-7 contraejemplo: omisión con categoría fuera del enum y sin marca → persiste",
         RK.t_ln_7(ctx_r2([ob], registro_dir=tmpl))["estado"] == "persiste")
caso("LN-8: el bloque del prompt y el JSON único del repo no difieren", RK.t_ln_8(ctx_r2([ob]))["estado"] == "resuelto")
b8 = RK.lineas_bloque("Sujeto_x — Equis (alias: X1, X2) [instancia]\nSujeto_rol_y — Ye [rol del TO a.pdf]\n## Raíz")
caso("LN-8: lectura de las líneas del bloque (alias, instancia, rol)",
     b8 == {"Sujeto_x": ("Equis", "X1, X2", True, None), "Sujeto_rol_y": ("Ye", "", False, "a.pdf")})

# Censos
caso("censo igual descripción: misma descripción salvo espacios, mayúsculas y acentos",
     RK.misma_descripcion("Exportación  a consumo", "exportacion a consumo") and not RK.misma_descripcion("a", "b")
     and not RK.misma_descripcion(None, None))
g_ig = RK.Grafo({"nodes": [nodo_gen3("A", "Condicion", "A", {"descripcion": "Igual texto"}), nodo_gen3("B", "Condicion", "B", {"descripcion": "igual  texto"}),
                           nodo_gen3("C", "Operacion", "C", {"descripcion": "otro"})],
                 "edges": [ar3("A", "condicion_de", "B"), ar3("A", "condicion_de", "C")]})
ci = RK.censo_igual_descripcion(g_ig)
caso("censo igual descripción: cuenta la arista entre dos nodos de igual descripción, sin regla de retiro",
     ci["aristas"] == 1 and ci["por_firma"] == {"Condicion --condicion_de--> Condicion": 1} and ci["regla_de_retiro"].startswith("ninguna"))
ct = RK.control_igual_descripcion_lectura()
caso("censo igual descripción, control: sobre las 105 relaciones de la lectura marca C22, M50 y M56 a M59; M50 es correcta",
     ct["relaciones"] == 105 and sorted(ct["marcadas"]) == ["C22", "M50", "M56", "M57", "M58", "M59"]
     and ct["correctas_en_la_lectura_entre_las_marcadas"] == ["M50"], str(ct))
g_cr = RK.Grafo({"nodes": [n_cla("C1", "Condicion"), n_cla("D37", "Definicion", punto="3.7"),
                           nodo_gen3("O", "Obligacion", "O", punto="1.1")],
                 "edges": [ar3("C1", "remite_a", "D37", props={"alcance": "interna", "destino": "cla::3.7", "evidencia": "punto 3.7"}),
                           ar3("C1", "referencia", "O", props={"destino": "cap::1.1", "evidencia": "punto 1.1 de Capitales"},
                               rol_fuente="referencia_cruzada", provenance={"to": "cla", "archivo": CLA_PDF, "punto": "5.1.1.1"})]})
cr = RK.censo_remisiones(g_cr)
caso("censo de remisiones: las dos formas, por firma y por alcance (regla aplicada a la referencia)",
     cr["aristas"] == 2 and cr["por_forma"] == {"referencia": 1, "remite_a": 1}
     and cr["aristas_por_alcance"] == {"externa": 1, "interna": 1} and cr["citas"] == 2
     and cr["firmas_fuera_de_remite_a"] == 0)

# --------------------------------------------------------------------------- #
for x in OK:
    print("  OK   " + x)
for x in FAIL:
    print("  FAIL " + x)
print(f"\nselftest_regression_kg: {len(OK)}/{len(OK) + len(FAIL)} casos OK")
sys.exit(0 if not FAIL else 1)
