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
    salida distinto de 0 (computar_regresion + main end-to-end con --solo).

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
ctx4 = ctx_sintetico(g_r1, esqueleto_ref=ref, relaciones_esqueleto=REL)
caso("T4 vía Contexto: resuelto", RK.t_t4(ctx4)["estado"] == "resuelto")
caso("T4: grafo sin ninguna arista de esqueleto → no_aplicable", RK.t_t4(ctx_sintetico(RK.Grafo({"nodes": esq_nodos, "edges": []}, "g", "g" * 64), esqueleto_ref=ref, relaciones_esqueleto=REL))["estado"] == "no_aplicable")

# --------------------------------------------------------------------------- #
# 5. T5 por (ancla origen, ancla destino, evidencia) e I3–I5                   #
# --------------------------------------------------------------------------- #
muestra = [{"n": 1, "source_ancla": "cap::1.2", "target_ancla": "cla::6.5.2", "evidencia_verbatim": "ver punto 6.5.2"}]
src = nodo_gen3("Ex", "Excepcion", "Origen", punto="1.2")
tgt = nodo_gen3("Ob", "Obligacion", "Destino", punto="6.5.2", archivo=CLA_PDF, to="cla")
g5 = RK.Grafo({"nodes": [src, tgt], "edges": [arista("Ex", "referencia", "Ob", rol_fuente="referencia_cruzada", props={"evidencia": "ver punto 6.5.2"}, gen=3)]})
caso("T5 pasa: arista referencia localizada por anclas + evidencia", RK.t_t5(ctx_sintetico(g5, muestra30=muestra))["estado"] == "resuelto")
g5b = RK.Grafo({"nodes": [src, tgt], "edges": [arista("Ex", "referencia", "Ob", rol_fuente="referencia_cruzada", props={"evidencia": "otra"}, gen=3)]})
r5 = RK.t_t5(ctx_sintetico(g5b, muestra30=muestra))
caso("T5 contraejemplo: misma tripla con otra evidencia → persiste", r5["estado"] == "persiste" and r5["valores"]["fallas"][0]["presente"])
caso("T5: sin aristas referencia con evidencia → no_aplicable", RK.t_t5(ctx_sintetico(G, muestra30=muestra))["estado"] == "no_aplicable")
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
caso("partición declarada 46 = 19 / 23 / 4, 15 retriever, grupos 12/12/12/10", RK.verificar_particion() == {"items": 46, "convertibles": 19, "con_condicion": 23, "no_convertibles": 4, "retriever": 15, "por_grupo": {"i-BKL": 12, "i-RT": 12, "ii": 12, "iii": 10}})
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
for x in OK:
    print("  OK   " + x)
for x in FAIL:
    print("  FAIL " + x)
print(f"\nselftest_regression_kg: {len(OK)}/{len(OK) + len(FAIL)} casos OK")
sys.exit(0 if not FAIL else 1)
