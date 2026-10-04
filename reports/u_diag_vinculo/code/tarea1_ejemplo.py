"""U-DIAG-VINCULO, tarea 1: aristas entre los nodos anclados en el párrafo sin numerar de cla::5.1.1
(unidad cla::5.1.1::intro) y los anclados en cla::5.1.1.1, en cualquier dirección, y caminos entre ellos.

Solo lectura, USD 0. Corre sobre una copia del grafo (regla l), nunca sobre el repo. Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B tarea1_ejemplo.py <kg.json>

Definiciones (fijadas antes de correr):
- Un nodo está «anclado» en una unidad si alguna de sus procedencias (`provenances`, o `provenance` si no
  hay lista) tiene ese `chunk_id`.
- Nodo concentrador: TextoOrdenado o Sujeto (nodos compartidos por muchas unidades; el TextoOrdenado de
  cla tiene procedencias en 143 unidades). Se informan aparte: un camino que pasa por ellos no es un
  vínculo normativo entre las dos unidades.
- Camino: búsqueda en anchura sobre el grafo no dirigido, con y sin los concentradores.
"""
import hashlib
import json
import sys
from collections import deque

A, B = "cla::5.1.1::intro", "cla::5.1.1.1"
CONCENTRADORES = ("TextoOrdenado", "Sujeto")

ruta = sys.argv[1]
raw = open(ruta, "rb").read()
print("kg:", ruta)
print("sha256:", hashlib.sha256(raw).hexdigest())
kg = json.loads(raw)
nodos, aristas = kg["nodes"], kg["edges"]
print("nodos:", len(nodos), "aristas:", len(aristas))


def chunks(x):
    provs = x.get("provenances") or ([x["provenance"]] if x.get("provenance") else [])
    return {p.get("chunk_id") for p in provs}


tipo = {n["id"]: n["type"] for n in nodos}
en_a = {n["id"] for n in nodos if A in chunks(n)}
en_b = {n["id"] for n in nodos if B in chunks(n)}
for rot, ids in (("A " + A, en_a), ("B " + B, en_b)):
    print(f"\n== nodos anclados en {rot}: {len(ids)}")
    for n in nodos:
        if n["id"] in ids:
            print(f"  {n['type']:<13} {n['id']}  | {n['label']}  | unidades de procedencia: {len(chunks(n))}")
            if n["type"] not in CONCENTRADORES:
                print("     properties:", json.dumps(n.get("properties"), ensure_ascii=False))
print("\nnodos en las dos unidades:", sorted(en_a & en_b))

cont_a = {i for i in en_a if tipo[i] not in CONCENTRADORES}
cont_b = {i for i in en_b if tipo[i] not in CONCENTRADORES}
print("\n== aristas entre un nodo de A y un nodo de B (cualquier dirección), todos los nodos")
n_ab = 0
for e in aristas:
    s, t = e["source"], e["target"]
    if (s in en_a and t in en_b) or (s in en_b and t in en_a):
        n_ab += 1
        print(f"  {tipo[s]}:{s} -{e['relation']}-> {tipo[t]}:{t}  chunks={sorted(chunks(e))}")
print("total:", n_ab)
print("\n== aristas entre nodos de contenido de A y de B (sin concentradores)")
n_cc = sum(1 for e in aristas if (e["source"] in cont_a and e["target"] in cont_b)
           or (e["source"] in cont_b and e["target"] in cont_a))
print("total:", n_cc)

print("\n== aristas que tocan los nodos de contenido de A o de B")
for e in aristas:
    if e["source"] in cont_a | cont_b or e["target"] in cont_a | cont_b:
        extra = {k: v for k, v in e.items() if k not in ("source", "target", "relation", "provenance", "provenances")}
        print(f"  {tipo[e['source']]}:{e['source'][:70]} -{e['relation']}-> {tipo.get(e['target'])}:{e['target'][:70]}"
              f"  chunks={sorted(chunks(e))}  {json.dumps(extra, ensure_ascii=False)}")

ady = {}
for e in aristas:
    ady.setdefault(e["source"], []).append((e["target"], e["relation"], "->"))
    ady.setdefault(e["target"], []).append((e["source"], e["relation"], "<-"))


def camino(origenes, destinos, excluir):
    prev = {o: None for o in origenes}
    q = deque(origenes)
    while q:
        u = q.popleft()
        if u in destinos:
            path = []
            while prev[u] is not None:
                v, rel, d = prev[u]
                path.append((v, rel, d, u))
                u = v
            return list(reversed(path))
        for v, rel, d in ady.get(u, []):
            if v not in prev and (v in destinos or tipo.get(v) not in excluir):
                prev[v] = (u, rel, d)
                q.append(v)
    return None


print("\n== camino más corto entre contenido de A y contenido de B")
for rot, excl in (("con concentradores", ()), ("sin concentradores", CONCENTRADORES)):
    p = camino(sorted(cont_a), cont_b, excl)
    if p is None:
        print(f"  {rot}: NINGUNO")
    else:
        print(f"  {rot}: {len(p)} saltos")
        for u, rel, d, v in p:
            print(f"     {tipo[u]}:{u[:60]} {d}{rel}{d} {tipo[v]}:{v[:60]}")
