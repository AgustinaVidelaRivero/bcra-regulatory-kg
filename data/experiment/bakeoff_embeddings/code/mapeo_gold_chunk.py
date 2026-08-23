#!/usr/bin/env python3
"""Entregable 1 de U-A2.0b-bakeoff: mapeo gold -> chunk.
Aplica la regla declarada en regla_mapeo_declarada.md (sellada antes de correr).
Solo lectura sobre el repo; escribe unicamente en el scratchpad.
"""
import json, os, sys, hashlib, collections

REPO = "/Users/agustinavidelarivero/INGENIERIA IA/TESIS/bcra-regulatory-kg"
SP = os.path.dirname(os.path.abspath(__file__))
TOS = ["cap", "cla", "ext", "pro", "ric"]
E0 = os.path.join(REPO, "data/experiment/reextraccion_v2/e0_chunking/salida_enm01")
PARES = os.path.join(REPO, "data/experiment/ablacion_retrieval/pares/pares_v3.json")
UMBRAL_AMBIGUO = 10


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


chunks = []
por_to = collections.defaultdict(list)
for to in TOS:
    d = json.load(open(os.path.join(E0, f"chunks_{to}.json")))
    for c in d:
        assert c["to"] == to, (c["id"], to)
        chunks.append(c)
        por_to[to].append(c)
by_id = {c["id"]: c for c in chunks}
assert len(by_id) == len(chunks), "ids duplicados"

pares = json.load(open(PARES))["pares"]


def resolver(to, u):
    """Devuelve (ids, via) segun la regla declarada."""
    exact = [c["id"] for c in por_to[to] if c["unidad"] == u]
    if exact:
        return sorted(exact), "a"
    desc = [c["id"] for c in por_to[to] if c["unidad"].startswith(u + ".")]
    if desc:
        return sorted(desc), "b"
    return [], "ninguna"


detalle = []
for p in pares:
    anclas = []
    for a in p["gold"]["anclas"]:
        ids, via = resolver(a["to"], a["ancla"])
        anclas.append({"ancla": f"{a['to']}:{a['ancla']}", "via": via,
                       "n_chunks": len(ids), "chunk_ids": ids,
                       "location_ejemplo": a.get("location_ejemplo")})
    union_a = sorted({i for x in anclas if x["via"] == "a" for i in x["chunk_ids"]})
    union_ab = sorted({i for x in anclas for i in x["chunk_ids"]})
    detalle.append({
        "sample_id": p["sample_id"], "estrato": p["estrato"],
        "n_anclas": len(anclas), "anclas": anclas,
        "gold_chunks_a": union_a, "gold_chunks_ab": union_ab,
        "n_gold_a": len(union_a), "n_gold_ab": len(union_ab),
        "anclas_resueltas_ab": sum(1 for x in anclas if x["via"] != "ninguna"),
        "parcial": len(anclas) > 1 and 0 < sum(1 for x in anclas if x["via"] != "ninguna") < len(anclas),
        "ambiguo": len(union_ab) > UMBRAL_AMBIGUO,
    })

# --- conteos a nivel CASO (par x variante) ---
def conteos(campo_n):
    mapeados = [d for d in detalle if d[campo_n] > 0]
    return len(mapeados) * 2  # dos variantes por par


res = {
    "regla_sha256": sha(os.path.join(SP, "regla_mapeo_declarada.md")),
    "insumos": {
        "pares_v3.json": sha(PARES),
        **{f"chunks_{to}.json": sha(os.path.join(E0, f"chunks_{to}.json")) for to in TOS},
    },
    "universo": {"n_chunks": len(chunks), "n_pares": len(pares), "n_casos": len(pares) * 2},
    "casos": {
        "mapeados_solo_a": conteos("n_gold_a"),
        "mapeados_a_mas_b": conteos("n_gold_ab"),
        "no_mapeados_a_mas_b": (len(pares) - len([d for d in detalle if d["n_gold_ab"] > 0])) * 2,
        "ambiguos_fanout_gt10": len([d for d in detalle if d["ambiguo"]]) * 2,
        "parcialmente_resueltos": len([d for d in detalle if d["parcial"]]) * 2,
    },
    "pares": {
        "mapeados_solo_a": len([d for d in detalle if d["n_gold_a"] > 0]),
        "mapeados_a_mas_b": len([d for d in detalle if d["n_gold_ab"] > 0]),
        "no_mapeados": len([d for d in detalle if d["n_gold_ab"] == 0]),
        "ambiguos": len([d for d in detalle if d["ambiguo"]]),
    },
    "anclas": {
        "total": sum(d["n_anclas"] for d in detalle),
        "distintas": len({x["ancla"] for d in detalle for x in d["anclas"]}),
        "via_a": len({x["ancla"] for d in detalle for x in d["anclas"] if x["via"] == "a"}),
        "via_b": len({x["ancla"] for d in detalle for x in d["anclas"] if x["via"] == "b"}),
        "sin_resolver": sorted({x["ancla"] for d in detalle for x in d["anclas"] if x["via"] == "ninguna"}),
    },
    "distribucion_n_gold_ab": dict(sorted(collections.Counter(d["n_gold_ab"] for d in detalle).items())),
    "detalle_por_par": detalle,
}
json.dump(res, open(os.path.join(SP, "mapeo_gold_chunk.json"), "w"), ensure_ascii=False, indent=1)

# --- salida a consola, sin truncar ---
print("== universo ==");  print(json.dumps(res["universo"], indent=1))
print("== casos (de 100) ==");  print(json.dumps(res["casos"], indent=1))
print("== pares (de 50) ==");  print(json.dumps(res["pares"], indent=1))
print("== anclas (37 distintas) ==");  print(json.dumps(res["anclas"], ensure_ascii=False, indent=1))
print("== distribucion |gold| bajo (a)+(b), por par ==")
print(json.dumps(res["distribucion_n_gold_ab"], indent=1))
print("== anclas resueltas por via (b), con fan-out ==")
for d in detalle:
    for x in d["anclas"]:
        if x["via"] == "b":
            print(f"  {d['sample_id']:8s} {x['ancla']:10s} desc={x['n_chunks']:3d}")
print("== pares ambiguos (|gold|>10) ==")
for d in detalle:
    if d["ambiguo"]:
        print(f"  {d['sample_id']:8s} |gold|={d['n_gold_ab']:3d} anclas={[x['ancla'] for x in d['anclas']]}")
