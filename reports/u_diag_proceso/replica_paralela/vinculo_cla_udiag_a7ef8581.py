"""Caso de desarrollo del vinculo entre unidades hermanas sin cita: Excepcion ancladas bajo cla::2.2
(«Exclusiones») y nodos de contenido bajo cla::2.1 («Conceptos incluidos»); aristas entre ambos. USD 0.
Uso: python -B vinculo_cla.py <kg.json> <out.json>"""
import json, sys
from collections import Counter
kg = json.load(open(sys.argv[1], encoding="utf-8"))
pun = {}
for n in kg["nodes"]:
    ps = [p for p in (n.get("provenances") or []) if p.get("to") == "cla"]
    if ps:
        pun[n["id"]] = (n["type"], sorted({p["punto"] for p in ps}))
def bajo(pts, pref):
    return any(p == pref or p.startswith(pref + ".") for p in pts)
exc = sorted(i for i, (t, p) in pun.items() if t == "Excepcion" and bajo(p, "2.2"))
reg = sorted(i for i, (t, p) in pun.items() if t in ("Restriccion", "Obligacion", "Operacion", "Definicion", "Condicion", "Potestad") and bajo(p, "2.1"))
E = Counter()
for e in kg["edges"]:
    if e["source"] in exc:
        tgt = pun.get(e["target"])
        zona = "bajo_2.1" if tgt and tgt[0] != "TextoOrdenado" and bajo(tgt[1], "2.1") else ("TextoOrdenado" if tgt and tgt[0] == "TextoOrdenado" else ("bajo_2.2" if tgt and bajo(tgt[1], "2.2") else "otro"))
        E[f"{e['relation']}|{tgt[0] if tgt else 'sin_procedencia_cla'}|{zona}"] += 1
res = {"excepcion_bajo_2_2": len(exc), "contenido_bajo_2_1": len(reg), "aristas_desde_excepcion_2_2": dict(E),
       "aristas_hacia_contenido_2_1": sum(v for k, v in E.items() if k.endswith("bajo_2.1"))}
json.dump(res, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps(res, ensure_ascii=False))
