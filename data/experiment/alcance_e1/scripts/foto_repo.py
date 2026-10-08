"""Foto sha256 de todos los archivos de un árbol (salvo .git): una línea «sha256  ruta» por archivo, ordenada.
Los enlaces simbólicos se registran por su destino (no se siguen). Uso: foto_repo.py RAIZ SALIDA"""
import hashlib
import os
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

raiz, salida = Path(sys.argv[1]), Path(sys.argv[2])


def sha(p: str) -> str:
    if os.path.islink(p):
        return "enlace:" + os.readlink(p)
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


rutas = []
for d, dirs, files in os.walk(raiz):
    if d == str(raiz):
        dirs[:] = [x for x in dirs if x != ".git"]
    for x in dirs:
        if os.path.islink(os.path.join(d, x)):
            rutas.append(os.path.join(d, x))
    rutas += [os.path.join(d, f) for f in files]
with ThreadPoolExecutor(8) as ex:
    shas = list(ex.map(sha, rutas))
lineas = sorted(f"{s}  {os.path.relpath(r, raiz)}" for s, r in zip(shas, rutas))
salida.write_text("\n".join(lineas) + "\n", encoding="utf-8")
print(len(lineas), "archivos")
