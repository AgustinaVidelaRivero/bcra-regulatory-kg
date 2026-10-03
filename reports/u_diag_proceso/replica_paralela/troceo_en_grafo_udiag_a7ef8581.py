"""Para cada punto NO terminal de clase A (titulo con ':' sin intro) y B (titulo cortado) de la E0
de la tanda 0, nodos del grafo anclados en ese punto (cualquier procedencia) y su rol_documental.
Uso: python -B troceo_en_grafo.py <salida_e0_tanda0> <kg.json> <out.json>"""
import json, sys
from pathlib import Path
from collections import Counter, defaultdict
e0 = Path(sys.argv[1]); kg = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8")); out = Path(sys.argv[3])
def fin(t):
    t = t.rstrip(); return t[-1] if t else ""
clases = {}
hijos = defaultdict(list)
for a in sorted(e0.glob("chunks_*.json")):
    to = a.stem[len("chunks_"):]
    d = json.loads(a.read_text(encoding="utf-8")); cs = d["chunks"] if isinstance(d, dict) else d
    ids = {c["id"] for c in cs}
    for c in cs:
        for h in c.get("herencia") or []:
            if h["tipo"] == "encabezado" and not str(h["unidad_origen"]).startswith("S"):
                u = h["unidad_origen"]
                tiene_intro = f"{to}::{u}::intro" in ids
                f_ = fin(h["texto"])
                k = ("A" if (f_ == ":" and not tiene_intro) else "B" if (f_ not in (".", ";", ":")) else None)
                if k:
                    clases[(to, u)] = {"clase": k, "titulo": h["texto"], "tiene_intro": tiene_intro}
                    if c["id"] not in hijos[(to, u)]:
                        hijos[(to, u)].append(c["id"])
anclados = defaultdict(list)
for n in kg["nodes"]:
    for p in n.get("provenances") or [n.get("provenance")]:
        if not p: continue
        key = (p.get("to"), p.get("punto"))
        if key in clases:
            anclados[key].append({"id": n["id"], "type": n["type"], "rol": p.get("rol_documental"),
                                  "chunk": p.get("chunk_id"),
                                  "desc": (n.get("properties") or {}).get("descripcion", "")[:140]})
res = {"A": [], "B_resumen": Counter()}
for key, v in sorted(clases.items()):
    nodos = [x for x in anclados.get(key, []) if x["type"] not in ("TextoOrdenado", "Comunicacion")]
    roles = Counter(x["rol"] for x in nodos)
    fila = {"unidad": f"{key[0]}::{key[1]}", "titulo": v["titulo"][:120], "tiene_intro": v["tiene_intro"],
            "n_hijos": len(hijos[key]), "nodos_de_contenido_anclados": len(nodos), "roles": dict(roles),
            "ejemplos": nodos[:4]}
    if v["clase"] == "A":
        res["A"].append(fila)
    else:
        res["B_resumen"]["total"] += 1
        con_herencia_enc = sum(1 for x in nodos if (x["rol"] or "").startswith("herencia_encabezado"))
        res["B_resumen"]["con_nodo_anclado_desde_encabezado"] += 1 if con_herencia_enc else 0
        res["B_resumen"]["con_intro"] += 1 if v["tiene_intro"] else 0
res["B_resumen"] = dict(res["B_resumen"])
res["A_resumen"] = {"total": len(res["A"]),
                    "con_algun_nodo_de_contenido_anclado": sum(1 for f in res["A"] if f["nodos_de_contenido_anclados"]),
                    "sin_nodo": [f["unidad"] for f in res["A"] if not f["nodos_de_contenido_anclados"]]}
out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps({"A_resumen": res["A_resumen"], "B_resumen": res["B_resumen"]}, ensure_ascii=False, indent=1))
for f in res["A"]:
    print(f["unidad"], "| hijos", f["n_hijos"], "| nodos", f["nodos_de_contenido_anclados"], f["roles"])
    for x in f["ejemplos"]: print("     ", x["type"], x["rol"], x["chunk"], "|", x["desc"])
