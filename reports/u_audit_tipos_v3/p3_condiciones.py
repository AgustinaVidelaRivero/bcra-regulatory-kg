"""Punto 3: por que 35 Condiciones de ens_desarrollo/r1 no tienen aristas. Solo lectura.
Traza cada nodo a la entidad del registro final (extracciones_finales_<to>.jsonl, lo que
ensambla E2) y al registro E1 (extracciones_e1.jsonl, con crudo)."""
import json, sys, collections
REPO = "/Users/agustinavidelarivero/INGENIERIA IA/TESIS/bcra-regulatory-kg"
sys.path.insert(0, REPO + "/data/experiment/reextraccion_v2/e2_reduce")
sys.path.insert(0, REPO + "/data/experiment/grafo_v2/code")
sys.path.insert(0, REPO + "/data/experiment/esq/code")
import prompt_congelado as pc  # noqa
# e2_lib importa schema (lee esquema_v2_clases.json) — solo funciones puras
from e2_lib import entity_slug_v3  # noqa
T0 = REPO + "/data/experiment/reextraccion_v2/corpus_tanda0"
kg = json.load(open(T0 + "/ens_desarrollo/r1/kg.json"))
deg = collections.Counter()
for e in kg["edges"]:
    deg[e["source"]] += 1; deg[e["target"]] += 1
aislados = [n for n in kg["nodes"] if n["type"] == "Condicion" and deg[n["id"]] == 0]
def jl(p):
    out = {}
    for ln in open(p):
        d = json.loads(ln); out[d["chunk_id"]] = d
    return out
fin, e1 = {}, {}
for to in ("pro", "cla", "ric", "cap", "ext"):
    fin.update(jl(f"{T0}/salida_dirigida/{to}/extracciones_finales_{to}.jsonl"))
    e1.update(jl(f"{T0}/salida_dirigida/{to}/extracciones_e1.jsonl"))
filas = []
for n in aislados:
    cands = [p.get("chunk_id") for p in n["provenances"]]
    cid = lid = None
    for c in cands + sorted(fin):
        rf = fin.get(c)
        if not rf or not rf.get("validacion"):
            continue
        loc = [e["local_id"] for e in rf["validacion"]["entidades"]
               if e["type"] == "Condicion" and f"Condicion_{entity_slug_v3(e)}" == n["id"]]
        if loc:
            cid, lid = c, loc[0]; break
    assert lid is not None, n["id"]
    rf = fin[cid]; val = rf["validacion"]
    rels_final = [r for r in val["relaciones"] if lid in (r.get("source"), r.get("target"))]
    rech_final = [r for r in val["rechazos"] if isinstance(r.get("elemento"), dict)
                  and lid in (r["elemento"].get("source"), r["elemento"].get("target"))]
    # relaciones crudas del registro final: si el final es el de E1, el crudo esta en E1
    r1 = e1.get(cid) or {}
    crudo = r1.get("tool_input_crudo") or {}
    final_es_e1 = rf.get("estado_e3") in ("completo_ok_directo", "aceptado_con_residuales")
    fila = {"id": n["id"], "to": n["provenance"]["to"], "chunk_id": cid, "local_id": lid,
            "estado_e3": rf.get("estado_e3"), "final_es_salida_e1": final_es_e1,
            "relaciones_validas_en_final": [(r["predicate"], r.get("source"), r.get("target")) for r in rels_final],
            "rechazos_en_final": [(x["motivo"], x["detalle"]) for x in rech_final]}
    if final_es_e1:
        cr = [r for r in (crudo.get("relations") or []) if lid in (r.get("source"), r.get("target"))]
        fila["relaciones_crudas_e1"] = [(r.get("predicate"), r.get("source"), r.get("target"), r.get("sujeto_id")) for r in cr]
        fila["establecida_en_emitida_en_crudo"] = any(r.get("predicate") == "establecida_en" and r.get("source") == lid for r in cr)
    filas.append(fila)
# clasificacion
def causa(f):
    if f["relaciones_validas_en_final"]:
        return "tiene_relaciones_validas_en_final (revisar)"
    if not f["rechazos_en_final"]:
        return "sin_relaciones_emitidas (ni validas ni rechazadas)"
    motivos = {m for m, _ in f["rechazos_en_final"]}
    return "solo_rechazadas:" + "+".join(sorted(motivos))
cl = collections.Counter(causa(f) for f in filas)
firmas = collections.Counter(d for f in filas for m, d in f["rechazos_en_final"])
est = collections.Counter(f.get("establecida_en_emitida_en_crudo") for f in filas)
res = {"n": len(filas), "causa": dict(cl), "firmas_rechazadas": {k: v for k, v in firmas.most_common()},
       "estado_e3": dict(collections.Counter(f["estado_e3"] for f in filas)),
       "establecida_en_emitida_en_crudo_e1 (solo final==E1)": {str(k): v for k, v in est.items()}}
json.dump(filas, open("/tmp/u_audit_tipos/p3_filas.json", "w"), ensure_ascii=False, indent=1)
json.dump(res, open("/tmp/u_audit_tipos/p3_resumen.json", "w"), ensure_ascii=False, indent=1)
print(json.dumps(res, ensure_ascii=False, indent=1))
