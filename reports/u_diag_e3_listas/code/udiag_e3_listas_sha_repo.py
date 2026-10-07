"""sha256 de todos los archivos del repo salvo .git; los enlaces simbólicos se registran como «LINK:destino».

Uso: python sha_repo.py <repo> <salida.tsv>
"""
import hashlib
import os
import sys

repo, out = sys.argv[1], sys.argv[2]
filas = []
for raiz, dirs, archivos in os.walk(repo, followlinks=False):
    rel_raiz = os.path.relpath(raiz, repo)
    if rel_raiz == ".git" or rel_raiz.startswith(".git" + os.sep):
        dirs[:] = []
        continue
    if rel_raiz == ".":
        dirs[:] = [d for d in dirs if d != ".git"]
    # los directorios enlazados se registran como enlace y no se recorren
    for d in list(dirs):
        p = os.path.join(raiz, d)
        if os.path.islink(p):
            filas.append((os.path.relpath(p, repo), "LINK:" + os.readlink(p)))
            dirs.remove(d)
    for a in archivos:
        p = os.path.join(raiz, a)
        rel = os.path.relpath(p, repo)
        if os.path.islink(p):
            filas.append((rel, "LINK:" + os.readlink(p)))
            continue
        h = hashlib.sha256()
        with open(p, "rb") as f:
            for bloque in iter(lambda: f.read(1 << 20), b""):
                h.update(bloque)
        filas.append((rel, h.hexdigest()))
filas.sort()
with open(out, "w", encoding="utf-8") as f:
    for rel, h in filas:
        f.write(f"{h}\t{rel}\n")
print(len(filas), "entradas")
