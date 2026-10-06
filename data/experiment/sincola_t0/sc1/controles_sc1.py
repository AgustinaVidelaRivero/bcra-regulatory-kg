"""U-SINCOLA-T0, SC1 (mandato 723680e, enmienda 1 en 1f7c159), puntos 6, 7 y 8: qué salió, la condición 10 del
checklist (`:81`) con X17, y los dos conteos declarados como límite, sobre el grafo nuevo (sin la cola) de un grafo de la
tanda 0 comparado con su r2b sellado. USD 0, solo lectura; escribe solo --out. Corre desde la raíz de una COPIA del repo
(o del repo, para leer) con rutas relativas.

  6. nodos y aristas que salen (ids del sellado que no están en el nuevo), por tipo y por relación, separadas las que
     llevaban la marca de la cola de las derivadas sin marca (por rol_fuente); nodos y aristas nuevos si los hay; los
     compartidos (nodos del sellado con procedencia dentro y fuera de la cola): presentes en el nuevo, con sus
     procedencias antes y después; 0 nodos con procedencia en la cola; 0 colgantes; 0 marcas (`cola_humana`,
     `cola_chunks`, `estado_e3`); `aristas_derivadas_cola_humana.json` y el reporte en 0; las unidades descartadas del
     reporte contra la lista de `finales.jsonl`; el ejemplo de la tesis y las anclas de las 15 preguntas sin unidad en
     la cola; las 15 preguntas (resultado de `t1_preguntas_control.py` sobre el nuevo) contra las de r2b.
  7. condición 10, con el código de los controles b y c de `reext_t0/t3/controles_t3.py` sobre el kg nuevo: (i) la
     Excepcion de `cla::5.1.1.1` presente y fuera de la cola; (ii) desde cada nodo con procedencia en `cla::5.1.1::intro`,
     por la jerarquía de la procedencia, los nodos de cada chunk hijo de `cla::5.1.1`, listados; (iii) el intro conserva
     la Definicion de alcance y los tipos de `cla::5.1.1.1`; (iv) X17: `remite_a` desde `cla::5.1.1.1` hacia `cla::3.7`.
  8. forma A (control 3.e de T3, mismo código) sobre los TOs del grafo, con todas las unidades y sin las de la cola; y
     el hallazgo 2.13: `remite_a.irresolubles_por_causa` del reporte nuevo al lado del sellado.

Uso: python -B controles_sc1.py --grafo diez --kg-nuevo <ens_<g>_r2b_sincola/r2/kg.json> --kg-sellado <ens_<g>_r2b/r2/kg.json>
         [--preguntas-nuevo <json de t1_preguntas_control sobre el nuevo>] --out <json>
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from collections import Counter, OrderedDict, defaultdict
from pathlib import Path

RAIZ = Path.cwd().resolve()
REX = RAIZ / "data/experiment/reextraccion_v2"
T0 = REX / "corpus_tanda0"
SAL = T0 / "salida_r2b"
E0 = REX / "e0_chunking" / "salida_tanda0_r2b"
PREG_R2B = RAIZ / "data/experiment/reext_t0/t4/salida/preguntas_r2b.json"
SORTEOS = RAIZ / "data/experiment/reext_t0/t4/salida/sorteos_t4.json"
CONTROLES_T3BIS = RAIZ / "data/experiment/reext_t0/t3bis/salida/controles_t3bis.json"

ap = argparse.ArgumentParser()
ap.add_argument("--grafo", choices=("diez", "desarrollo"), required=True)
ap.add_argument("--kg-nuevo", required=True)
ap.add_argument("--kg-sellado", required=True)
ap.add_argument("--preguntas-nuevo", default=None)
ap.add_argument("--preguntas-sellado", default=None, help="t1_preguntas_control sobre el r2b sellado del mismo grafo (default: t4/salida/preguntas_r2b.json, que es de diez)")
ap.add_argument("--out", required=True)
a = ap.parse_args()


def leer(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def jsonl(p) -> list:
    p = Path(p)
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()] if p.exists() else []


def last_wins(p) -> dict:
    return {r["chunk_id"]: r for r in jsonl(p)}


def chunks_e0(p) -> list:
    d = leer(p)
    return d["chunks"] if isinstance(d, dict) else d


def provs(x: dict) -> list:
    return [p for p in [x.get("provenance")] + (x.get("provenances") or []) if p]


def chunks_de(x: dict) -> set:
    return {p.get("chunk_id") for p in provs(x) if p.get("chunk_id")}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    return " ".join(re.sub(r"[^a-z0-9]+", " ", s).split())


def marca(x: dict) -> bool:
    return (x.get("properties") or {}).get("cola_humana") == "true"


def sha(p) -> str:
    import hashlib
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


S = leer(a.kg_sellado)
N = leer(a.kg_nuevo)
dir_nuevo = Path(a.kg_nuevo).parent
rep_n = leer(dir_nuevo / "reporte_ensamblado_r2.json")
rep_s = leer(Path(a.kg_sellado).parent / "reporte_ensamblado_r2.json")
tos = list(rep_n["manifiesto"]["orden_corrida"])
idx_s = {n["id"]: n for n in S["nodes"]}
idx_n = {n["id"]: n for n in N["nodes"]}

# la cola: las unidades cola_humana* como última versión en finales.jsonl, de los TOs del grafo
FIN = {to: last_wins(SAL / to / "finales.jsonl") for to in tos}
cola = sorted(cid for to in tos for cid, r in FIN[to].items() if str(r.get("estado")).startswith("cola_humana"))
cola_set = set(cola)
sorteo = leer(SORTEOS)["punto_1_cola_humana"]
cola_sorteo = {m["chunk_id"] for m in sorteo["muestra_en_orden_del_sorteo"]} | set(sorteo["fuera_de_la_muestra"])

res = OrderedDict()
res["unidad"] = "U-SINCOLA-T0, SC1, puntos 6-8 (controles_sc1.py)"
res["grafo"] = a.grafo
res["kg_nuevo"] = {"ruta": a.kg_nuevo, "sha256": sha(a.kg_nuevo), "nodos": len(N["nodes"]), "aristas": len(N["edges"])}
res["kg_sellado"] = {"ruta": a.kg_sellado, "sha256": sha(a.kg_sellado), "nodos": len(S["nodes"]), "aristas": len(S["edges"])}
res["tos"] = tos

# ------------------------------------------------------------------------------------------------ 6. qué salió
g6 = OrderedDict()
g6["cola_de_finales_jsonl"] = {"n": len(cola), "por_to": dict(sorted(Counter(c.split("::")[0] for c in cola).items())),
                               "igual_al_sorteo_de_t4_en_estos_tos": set(cola) == {c for c in cola_sorteo if c.split("::")[0] in tos}}
desc = rep_n.get("cola_descartada_por_to") or {}
desc_lista = sorted(c for v in desc.values() for c in v.get("chunks", []))
g6["reporte_nuevo"] = {"con_cola": rep_n.get("con_cola"),
                       "descartadas_por_to": {to: v.get("n") for to, v in desc.items()},
                       "descartadas_total": len(desc_lista),
                       "descartadas_igual_a_la_cola_de_finales": desc_lista == cola,
                       "aristas_derivadas_que_tocan_un_nodo_solo_de_la_cola": rep_n.get("aristas_derivadas_que_tocan_un_nodo_solo_de_la_cola"),
                       "unidades_de_cola_del_grafo_por_to": {to: len((v.get("cola_flaggeada") or {}).get("chunks_de_cola") or [])
                                                             for to, v in rep_n["e2_por_to"].items()},
                       "doble_corrida_byte_identica": rep_n.get("doble_corrida_byte_identica")}
g6["aristas_derivadas_cola_humana_json"] = len(leer(dir_nuevo / "aristas_derivadas_cola_humana.json"))
# nodos
salen = [n for n in S["nodes"] if n["id"] not in idx_n]
nuevos = [n for n in N["nodes"] if n["id"] not in idx_s]
g6["nodos_que_salen"] = {"n": len(salen), "por_tipo": dict(sorted(Counter(n["type"] for n in salen).items())),
                         "con_toda_la_procedencia_en_la_cola": sum(1 for n in salen if chunks_de(n) and chunks_de(n) <= cola_set),
                         "con_marca_de_cola": sum(1 for n in salen if marca(n)),
                         "sin_procedencia_en_la_cola (no debería haber)": [n["id"] for n in salen if not (chunks_de(n) & cola_set)]}
g6["nodos_nuevos"] = {"n": len(nuevos), "por_tipo": dict(sorted(Counter(n["type"] for n in nuevos).items())),
                      "ids": [n["id"] for n in nuevos][:50]}
# aristas
key = lambda e: (e["source"], e["relation"], e["target"])  # noqa: E731
ks_n = {key(e) for e in N["edges"]}
ks_s = {key(e) for e in S["edges"]}
a_salen = [e for e in S["edges"] if key(e) not in ks_n]
a_nuevas = [e for e in N["edges"] if key(e) not in ks_s]
con_marca = [e for e in a_salen if marca(e)]
sin_marca = [e for e in a_salen if not marca(e)]
g6["aristas_que_salen"] = {"n": len(a_salen), "por_relacion": dict(Counter(e["relation"] for e in a_salen).most_common()),
                           "con_marca_de_cola": {"n": len(con_marca), "por_relacion": dict(Counter(e["relation"] for e in con_marca).most_common())},
                           "sin_marca (derivadas)": {"n": len(sin_marca), "por_relacion": dict(Counter(e["relation"] for e in sin_marca).most_common()),
                                                     "por_rol_fuente": dict(Counter(str(e.get("rol_fuente")) for e in sin_marca).most_common())},
                           "que_tocan_un_nodo_que_sale": sum(1 for e in a_salen if e["source"] not in idx_n or e["target"] not in idx_n),
                           "entre_nodos_que_quedan": [key(e) for e in a_salen if e["source"] in idx_n and e["target"] in idx_n][:50]}
g6["aristas_nuevas"] = {"n": len(a_nuevas), "por_relacion": dict(Counter(e["relation"] for e in a_nuevas).most_common()),
                        "por_rol_fuente": dict(Counter(str(e.get("rol_fuente")) for e in a_nuevas).most_common()),
                        "primeras": [key(e) for e in a_nuevas][:50]}
# compartidos
comp = [n for n in S["nodes"] if (chunks_de(n) & cola_set) and not (chunks_de(n) <= cola_set)]
filas = []
for n in comp:
    m = idx_n.get(n["id"])
    filas.append(OrderedDict([("id", n["id"]), ("type", n["type"]), ("presente_en_el_nuevo", m is not None),
                              ("procedencias_antes", len(provs(n))), ("de_la_cola_antes", len([p for p in provs(n) if p.get("chunk_id") in cola_set])),
                              ("procedencias_despues", len(provs(m)) if m else None),
                              ("de_la_cola_despues", len([p for p in provs(m) if p.get("chunk_id") in cola_set]) if m else None),
                              ("marca_antes", marca(n)), ("marca_despues", marca(m) if m else None)]))
g6["compartidos"] = {"n": len(comp), "por_tipo": dict(sorted(Counter(n["type"] for n in comp).items())),
                     "presentes_en_el_nuevo": sum(1 for f in filas if f["presente_en_el_nuevo"]),
                     "con_procedencia_de_la_cola_despues": sum(1 for f in filas if f["de_la_cola_despues"]),
                     "con_marca_despues": sum(1 for f in filas if f["marca_despues"]), "filas": filas}
# el nuevo: procedencia en la cola, colgantes, marcas
g6["nuevo_nodos_con_procedencia_en_la_cola"] = sum(1 for n in N["nodes"] if chunks_de(n) & cola_set)
g6["nuevo_aristas_con_procedencia_en_la_cola"] = sum(1 for e in N["edges"] if chunks_de(e) & cola_set)
g6["nuevo_colgantes"] = sum(1 for e in N["edges"] if e["source"] not in idx_n or e["target"] not in idx_n)
claves_marca = ("cola_humana", "cola_chunks", "estado_e3")
g6["nuevo_marcas"] = {"nodos_con_cola_humana_true": sum(1 for n in N["nodes"] if marca(n)),
                      "aristas_con_cola_humana_true": sum(1 for e in N["edges"] if marca(e)),
                      "objetos_con_alguna_clave_de_marca": sum(1 for o in N["nodes"] + N["edges"] if any(k in (o.get("properties") or {}) for k in claves_marca))}
g6["sellado_marcas"] = {"nodos": sum(1 for n in S["nodes"] if marca(n)), "aristas": sum(1 for e in S["edges"] if marca(e))}
g6["conteo_cruzado"] = {"nodos_sellado - salen + nuevos == nodos_nuevo": len(S["nodes"]) - len(salen) + len(nuevos) == len(N["nodes"]),
                        "aristas_sellado - salen + nuevas == aristas_nuevo": len(S["edges"]) - len(a_salen) + len(a_nuevas) == len(N["edges"])}
# ejemplo de la tesis y anclas de las 15 preguntas
ejemplo = sorted(c["id"] for c in chunks_e0(E0 / "chunks_cla.json") if c["id"].startswith("cla::5.1.1") or c["id"].startswith("cla::3.7"))
chunks_cla = [c["id"] for c in chunks_e0(E0 / "chunks_cla.json")]
datos_ej = RAIZ / "docs/tesis/figuras/ejemplo_prestamo_datos.json"
ids_ej = sorted(set(re.findall(r"cla::[0-9][0-9.]*(?:::[a-z0-9]+)?", datos_ej.read_text(encoding="utf-8")))) if datos_ej.exists() else []
ej_b = sorted({c for c in chunks_cla for x in ids_ej if c == x or c.startswith(x + ".") or c.startswith(x + "::")})
g6["ejemplo_de_la_tesis"] = {
    "nota": "el «18 unidades» del mandato no tiene definición en ningún archivo del repo: NO VERIFICADA; se dan dos definiciones",
    "a_criterio_t5": {"definicion": "chunks de la E0 r2b de cla bajo cla::5.1.1 y cla::3.7 (t5/cifras_t5.py)", "chunks": ejemplo, "n": len(ejemplo),
                      "en_la_cola": sorted(set(ejemplo) & cola_set)},
    "b_datos_del_ejemplo_del_prestamo": {"definicion": "los ids cla:: de docs/tesis/figuras/ejemplo_prestamo_datos.json (puntos y chunks), expandidos a los chunks de la E0 r2b de cla",
                                         "ids_en_el_archivo": ids_ej, "chunks": ej_b, "n": len(ej_b), "en_la_cola": sorted(set(ej_b) & cola_set)}}
q = leer(PREG_R2B)["preguntas"]


def ancla(x):
    return None if not x else re.sub(r" y sub-puntos$", "", x).replace("::S", "::")


def bajo(c, an):
    to, p = an.split("::")
    cto, cp = c.split("::", 1)
    return cto == to and (cp == p or cp.startswith(p + ".") or cp.startswith(p + "::"))


bajo_ancla = {p["n"]: sorted(c for c in cola if ancla(p["ancla"]) and bajo(c, ancla(p["ancla"]))) for p in q}
g6["preguntas_anclas"] = {"anclas": {p["n"]: p["ancla"] for p in q}, "unidades_de_la_cola_bajo_un_ancla": {k: v for k, v in bajo_ancla.items() if v},
                          "total_bajo_ancla": sum(len(v) for v in bajo_ancla.values())}
if a.preguntas_nuevo:
    pn = leer(a.preguntas_nuevo)
    base = leer(a.preguntas_sellado) if a.preguntas_sellado else leer(PREG_R2B)
    qb = base["preguntas"]
    antes = {p["n"]: p["resultado"] for p in qb}
    g6["preguntas_sobre_el_nuevo"] = {"kg_sha256": pn.get("kg_sha256"), "linea_de_base": a.preguntas_sellado or str(PREG_R2B), "kg_sha256_base": base.get("kg_sha256"),
                                      "totales_r2b": base["totales"], "totales_nuevo": pn["totales"],
                                      "que_cambian": {p["n"]: [antes[p["n"]], p["resultado"]] for p in pn["preguntas"] if p["resultado"] != antes[p["n"]]},
                                      "rango_bm25_que_cambia": {p["n"]: [next(x["rango_bm25_del_ancla"] for x in qb if x["n"] == p["n"]), p["rango_bm25_del_ancla"]]
                                                                for p in pn["preguntas"] if p["rango_bm25_del_ancla"] != next(x["rango_bm25_del_ancla"] for x in qb if x["n"] == p["n"])}}
res["6_que_salio"] = g6

# ------------------------------------------------------------------------------------------------ 7. condición 10
CHUNKS = {}
for f in sorted(E0.glob("chunks_*.json")):
    for c in chunks_e0(f):
        CHUNKS[c["id"]] = c
for p in sorted(SAL.glob("*/particiones_por_corte.json")):
    for v in leer(p).values():
        for c in v["partes"]:
            CHUNKS[c["id"]] = c
FR2 = {to: last_wins(SAL / to / f"extracciones_finales_r2_{to}.jsonl") for to in tos}
fin_val = {cid: r["validacion"] for to in tos for cid, r in FR2[to].items() if r.get("validacion")}


def c10(kg: dict, idx: dict) -> OrderedDict:
    def anclado(n, to, punto, exacto=True):
        return any(p.get("to") == to and (str(p.get("punto")) == punto if exacto else
                                          (str(p.get("punto")) == punto or str(p.get("punto")).startswith(punto + ".")))
                   for p in provs(n))
    n5111 = [n for n in kg["nodes"] if "cla::5.1.1.1" in chunks_de(n)]
    intro = [n for n in kg["nodes"] if "cla::5.1.1::intro" in chunks_de(n)]
    hijos_chunks = sorted(cid for cid in CHUNKS if cid.startswith("cla::5.1.1.") )
    hijos = defaultdict(list)
    for n in kg["nodes"]:
        for p in provs(n):
            cid = p.get("chunk_id") or ""
            if cid.startswith("cla::5.1.1.") and n["type"] not in ("TextoOrdenado", "Sujeto"):
                hijos[cid].append((n["id"], "5.1.1" in (p.get("ancestros") or []), marca(n)))
    exc = [n for n in n5111 if n["type"] == "Excepcion"]
    rb = [e for e in kg["edges"] if e["relation"] == "remite_a" and anclado(idx[e["source"]], "cla", "5.1.1.1")
          and anclado(idx[e["target"]], "cla", "3.7")]
    rb_sub = [e for e in kg["edges"] if e["relation"] == "remite_a" and anclado(idx[e["source"]], "cla", "5.1.1.1")
              and anclado(idx[e["target"]], "cla", "3.7", exacto=False)]
    return OrderedDict([
        ("i_excepcion_de_5_1_1_1", [{"id": n["id"], "label": n.get("label"), "cola": marca(n), "chunks": sorted(chunks_de(n)),
                                     "en_la_cola": bool(chunks_de(n) & cola_set)} for n in exc]),
        ("i_ok", len(exc) >= 1 and not any(marca(n) or (chunks_de(n) & cola_set) for n in exc)),
        ("ii_nodos_del_intro", [{"id": n["id"], "type": n["type"], "cola": marca(n)} for n in intro if n["type"] not in ("TextoOrdenado", "Sujeto")]),
        ("ii_chunks_hijos_de_5_1_1_en_e0", hijos_chunks),
        ("ii_alcanzados_por_hijo", OrderedDict((cid, {"nodos": len(v), "todos_con_ancestro_5_1_1": all(x[1] for x in v),
                                                      "con_marca": sum(1 for x in v if x[2]), "ids": sorted({x[0] for x in v})})
                                               for cid, v in sorted(hijos.items()))),
        ("ii_ok", all(cid in hijos and hijos[cid] for cid in ("cla::5.1.1.1", "cla::5.1.1.2"))
                  and all(all(x[1] for x in v) for v in hijos.values())),
        ("iii_intro_conserva_definicion_de_alcance", any(n["type"] == "Definicion" and "alcance" in norm(n.get("label")) for n in intro)),
        ("iii_tipos_en_5_1_1_1", dict(sorted(Counter(n["type"] for n in n5111).items()))),
        ("iv_x17_remite_a_5_1_1_1_a_3_7", len(rb)), ("iv_a_3_7_o_debajo", len(rb_sub)),
        ("iv_aristas", [{"source": e["source"], "target": e["target"], "chunks": sorted(chunks_de(e))} for e in rb_sub]),
        ("iv_ok", len(rb) >= 1),
        ("relaciones_rechazadas_en_5_1_1_1", [r for r in (fin_val.get("cla::5.1.1.1") or {}).get("rechazos", []) if r.get("nivel") == "relacion"])])


c10n = c10(N, idx_n)
c10s = c10(S, idx_s)
t3bis = leer(CONTROLES_T3BIS)["por_grafo"][a.grafo]
res["7_condicion_10"] = OrderedDict([
    ("nuevo", c10n),
    ("sellado_r2b_mismo_codigo", {k: c10s[k] for k in ("i_ok", "iii_tipos_en_5_1_1_1", "iii_intro_conserva_definicion_de_alcance", "iv_x17_remite_a_5_1_1_1_a_3_7", "iv_a_3_7_o_debajo")}),
    ("referencia_t3bis", {"excepcion_ids": [x["id"] for x in t3bis["c_condicion_10"]["excepcion_de_5_1_1_1"]],
                          "tipos_en_5_1_1_1": t3bis["c_condicion_10"]["tipos_en_5_1_1_1"],
                          "hijos": t3bis["c_condicion_10"]["hijos"],
                          "intro_conserva_definicion_de_alcance": t3bis["c_condicion_10"]["intro_conserva_definicion_de_alcance"],
                          "remite_a_5_1_1_1_a_3_7": t3bis["b_remision_del_ejemplo"]["remite_a_5_1_1_1_a_3_7"]}),
    ("cumple", {"i": c10n["i_ok"], "ii": c10n["ii_ok"], "iii": c10n["iii_intro_conserva_definicion_de_alcance"], "iv": c10n["iv_ok"]})])

# ------------------------------------------------------------------------------------------------ 8. límites
nrm = lambda s: " ".join((s or "").split())  # noqa: E731
dp = lambda s: nrm(s).endswith((":", "："))  # noqa: E731
DEST = {"Excepcion", "Obligacion", "Restriccion", "Operacion", "Potestad"}


def forma_a(excluir: set) -> dict:
    cnt = Counter()
    casos = []
    for cid, v in fin_val.items():
        if cid in excluir:
            continue
        c = CHUNKS.get(cid)
        if not c or c["tipo"] != "punto_terminal" or not c.get("herencia"):
            continue
        rels = v.get("relaciones", [])
        rech = [x.get("elemento") or {} for x in v.get("rechazos", []) if x.get("nivel") == "relacion"]
        ult = c["herencia"][-1]
        if not dp(ult["texto"]):
            continue
        for e in v.get("entidades", []):
            if e["type"] != "Condicion":
                continue
            cnt["condicion_de_item"] += 1
            if any(x["source"] == e["local_id"] and x["predicate"] == "condicion_de" for x in rels):
                continue
            cnt["sin_condicion_de"] += 1
            if any(x.get("source") == e["local_id"] and x.get("predicate") == "condicion_de" for x in rech):
                cnt["sin_condicion_de_pero_rechazada"] += 1
                continue
            cnt["sin_condicion_de_ni_rechazada"] += 1
            mini = f"{c['to']}::{ult.get('unidad_origen')}::intro"
            vm = fin_val.get(mini)
            dest = [x["type"] for x in (vm or {}).get("entidades", []) if x["type"] in DEST]
            if ult.get("tipo") == "intro" and dest:
                cnt["forma_A_encabezado_con_nodos_destino"] += 1
                casos.append({"chunk": cid, "mini": mini, "destinos": dest})
            elif ult.get("tipo") == "encabezado":
                cnt["encabezado_es_titulo"] += 1
            else:
                cnt["otro"] += 1
    return {"conteos": dict(cnt), "forma_A": cnt["forma_A_encabezado_con_nodos_destino"],
            "condicion_de_item_total": cnt["condicion_de_item"],
            "casos_forma_A_en_la_cola": sorted(x["chunk"] for x in casos if x["chunk"] in cola_set or x["mini"] in cola_set),
            "casos": casos}


fa_todas = forma_a(set())
fa_sin_cola = forma_a(cola_set)
res["8_limites"] = OrderedDict([
    ("forma_A", OrderedDict([
        ("nota", "control 3.e de T3 (e_forma_A de controles_t3.py, mismo código) sobre los TOs de este grafo; lee la validación final r2 de la "
                 "salida (extracciones_finales_r2_<to>.jsonl), no el kg; «sobre el grafo nuevo» = sin las unidades de la cola"),
        ("tos", tos),
        ("con_todas_las_unidades", {k: v for k, v in fa_todas.items() if k != "casos"}),
        ("sin_las_unidades_de_la_cola", {k: v for k, v in fa_sin_cola.items() if k != "casos"}),
        ("referencia_t3bis_diez_todas", t3bis.get("e_forma_A", leer(CONTROLES_T3BIS).get("e_forma_A", {})).get("conteos") if a.grafo == "diez" else leer(CONTROLES_T3BIS)["e_forma_A"]["conteos"]),
        ("casos_sin_cola", fa_sin_cola["casos"])])),
    ("hallazgo_2_13_remisiones_irresolubles", OrderedDict([
        ("clave", "reporte_ensamblado_r2.json: remite_a.citas_irresolubles e irresolubles_por_causa (la clave que medicion_r2a/m1_freno.md:86 desglosa)"),
        ("nuevo", {"menciones_detectadas": rep_n["remite_a"]["menciones_detectadas"], "citas_resueltas": rep_n["remite_a"]["citas_resueltas"],
                   "citas_irresolubles": rep_n["remite_a"]["citas_irresolubles"], "por_causa": rep_n["remite_a"]["irresolubles_por_causa"],
                   "punto_sin_nodos": rep_n["remite_a"]["irresolubles_por_causa"].get("punto_sin_nodos")}),
        ("r2b_sellado", {"menciones_detectadas": rep_s["remite_a"]["menciones_detectadas"], "citas_resueltas": rep_s["remite_a"]["citas_resueltas"],
                         "citas_irresolubles": rep_s["remite_a"]["citas_irresolubles"], "por_causa": rep_s["remite_a"]["irresolubles_por_causa"],
                         "punto_sin_nodos": rep_s["remite_a"]["irresolubles_por_causa"].get("punto_sin_nodos")}),
        ("r2a_diez_referencia", "205 de 510 irresolubles por punto sin nodos (data/experiment/medicion_r2a/m1_freno.md:86)")]))])

Path(a.out).parent.mkdir(parents=True, exist_ok=True)
Path(a.out).write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
r6 = res["6_que_salio"]
print(json.dumps({"grafo": a.grafo, "nodos": [res["kg_sellado"]["nodos"], res["kg_nuevo"]["nodos"]], "aristas": [res["kg_sellado"]["aristas"], res["kg_nuevo"]["aristas"]],
                  "salen": [r6["nodos_que_salen"]["n"], r6["aristas_que_salen"]["n"]], "nuevos": [r6["nodos_nuevos"]["n"], r6["aristas_nuevas"]["n"]],
                  "compartidos": [r6["compartidos"]["n"], r6["compartidos"]["presentes_en_el_nuevo"], r6["compartidos"]["con_procedencia_de_la_cola_despues"]],
                  "colgantes": r6["nuevo_colgantes"], "marcas": r6["nuevo_marcas"], "cond10": res["7_condicion_10"]["cumple"],
                  "forma_A": [fa_todas["forma_A"], fa_todas["condicion_de_item_total"], fa_sin_cola["forma_A"], fa_sin_cola["condicion_de_item_total"]],
                  "punto_sin_nodos": [rep_s["remite_a"]["irresolubles_por_causa"].get("punto_sin_nodos"), rep_n["remite_a"]["irresolubles_por_causa"].get("punto_sin_nodos")]},
                 ensure_ascii=False))
print("escrito:", a.out)
