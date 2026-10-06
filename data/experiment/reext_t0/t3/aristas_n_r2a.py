"""U-REEXT-T0, T3, control n (BKL-0038): las aristas `limita` desde una Restriccion «prohibicion» y `prohibe` desde una
Restriccion «limite_*» de los dos grafos r2a, con el texto de E0 r2 de sus chunks, para leer en cada una si está mal el
tipo o el predicado. Solo lee; escribe el JSON de --out. Determinístico, USD 0.

Uso (desde la raíz del repo): python -B data/experiment/reext_t0/t3/aristas_n_r2a.py --out ARCHIVO.json
"""
import argparse
import hashlib
import json
from collections import OrderedDict
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[4]
ENS = RAIZ / "data" / "experiment" / "reextraccion_v2" / "corpus_tanda0"
E0_R2 = RAIZ / "data" / "experiment" / "reextraccion_v2" / "e0_chunking" / "salida_tanda0_r2"

ap = argparse.ArgumentParser()
ap.add_argument("--out", type=Path, required=True)
a = ap.parse_args()


def incoherente(rel: str, tipo) -> bool:
    return (rel == "limita" and tipo == "prohibicion") or (rel == "prohibe" and str(tipo).startswith("limite"))


textos = {}
salida = OrderedDict([("control", "n (BKL-0038), aristas de r2a"), ("grafos", OrderedDict()), ("chunks", OrderedDict())])
for k in ("diez", "desarrollo"):
    p = ENS / f"ens_{k}_r2a" / "r2" / "kg.json"
    kg = json.loads(p.read_text(encoding="utf-8"))
    by = {n["id"]: n for n in kg["nodes"]}
    filas = []
    for e in kg["edges"]:
        if e["relation"] not in ("limita", "prohibe"):
            continue
        s, t = by[e["source"]], by[e["target"]]
        tipo = (s.get("properties") or {}).get("tipo")
        if not incoherente(e["relation"], tipo):
            continue
        chunks = sorted({x.get("chunk_id") for x in (e.get("provenances") or []) if x and x.get("chunk_id")})
        filas.append(OrderedDict([("source", s["id"]), ("label_source", s["label"]), ("tipo", tipo),
                                  ("descripcion", (s.get("properties") or {}).get("descripcion")),
                                  ("relation", e["relation"]), ("target", t["id"]), ("tipo_target", t["type"]),
                                  ("label_target", t["label"]), ("chunks", chunks)]))
        for c in chunks:
            textos.setdefault(c, None)
    salida["grafos"][k] = OrderedDict([("kg", str(p.relative_to(RAIZ))),
                                       ("sha256", hashlib.sha256(p.read_bytes()).hexdigest()),
                                       ("n", len(filas)), ("aristas", filas)])
for to in sorted({c.split("::")[0] for c in textos}):
    d = json.loads((E0_R2 / f"chunks_{to}.json").read_text(encoding="utf-8"))
    for ch in (d["chunks"] if isinstance(d, dict) else d):
        cid = ch.get("chunk_id") or ch.get("id")
        if cid in textos:
            salida["chunks"][cid] = ch.get("texto") or ch.get("text")
a.out.write_text(json.dumps(salida, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print({k: v["n"] for k, v in salida["grafos"].items()}, sorted(salida["chunks"]))
