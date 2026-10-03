"""Bloques intro/chapeau terminados en ':' (clase D) y unidades item de lista (clase C) de la tanda 0:
cuantos tienen al menos un nodo de contenido con esa unidad como chunk de procedencia, en un grafo.
Uso: python -B bloques_lista_en_grafo.py <salida_e0_tanda0> <kg.json> <out.json>"""
import json, sys
from pathlib import Path
from collections import Counter, defaultdict
e0 = Path(sys.argv[1]); kg = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8")); out = Path(sys.argv[3])
def fin(t):
    t = t.rstrip(); return t[-1] if t else ""
D, C = {}, {}
for a in sorted(e0.glob("chunks_*.json")):
    d = json.loads(a.read_text(encoding="utf-8")); cs = d["chunks"] if isinstance(d, dict) else d
    for c in cs:
        her = c.get("herencia") or []
        if c.get("tipo") == "mini_chunk" and c.get("rol_bloque") in ("intro", "chapeau_seccion") and fin(c["texto"]) == ":":
            D[c["id"]] = c["texto"][:120]
        if c.get("tipo") == "punto_terminal" and her and fin(her[-1]["texto"]) == ":":
            C[c["id"]] = her[-1]["texto"][:120]
por_chunk = defaultdict(int)
for n in kg["nodes"]:
    if n["type"] in ("TextoOrdenado", "Comunicacion", "Sujeto"): continue
    for p in n.get("provenances") or [n.get("provenance")]:
        if p and p.get("chunk_id"): por_chunk[p["chunk_id"]] += 1
res = {"D_total": len(D), "D_sin_nodo": sorted(k for k in D if not por_chunk.get(k)),
       "C_total": len(C), "C_sin_nodo": sorted(k for k in C if not por_chunk.get(k)),
       "C_nodos_por_unidad_media": round(sum(por_chunk.get(k, 0) for k in C) / max(1, len(C)), 3)}
res["D_sin_nodo_n"] = len(res["D_sin_nodo"]); res["C_sin_nodo_n"] = len(res["C_sin_nodo"])
res["D_sin_nodo_textos"] = {k: D[k] for k in res["D_sin_nodo"][:40]}
out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print({k: v for k, v in res.items() if k.endswith("_n") or k.endswith("total") or k.endswith("media")})
for k, v in list(res["D_sin_nodo_textos"].items())[:25]: print("  ", k, "|", v.replace("\n", " "))
