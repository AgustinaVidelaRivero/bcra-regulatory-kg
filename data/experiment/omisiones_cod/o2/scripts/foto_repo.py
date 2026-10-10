"""Foto sha256 de todos los archivos del repo (salvo .git), ordenada por ruta.
Uso: python3 -I foto_repo.py <repo> <salida.tsv>
Los enlaces simbolicos se registran por su destino (readlink), sin seguirlos."""
import hashlib, os, sys
repo, out = sys.argv[1], sys.argv[2]
filas = []
for raiz, dirs, archivos in os.walk(repo):
    if raiz == repo and '.git' in dirs:
        dirs.remove('.git')
    dirs.sort()
    for a in sorted(archivos):
        p = os.path.join(raiz, a)
        rel = os.path.relpath(p, repo)
        if os.path.islink(p):
            filas.append((rel, 'LINK:' + os.readlink(p)))
            continue
        h = hashlib.sha256()
        with open(p, 'rb') as f:
            for b in iter(lambda: f.read(1 << 20), b''):
                h.update(b)
        filas.append((rel, h.hexdigest()))
filas.sort()
with open(out, 'w') as f:
    for r, h in filas:
        f.write(f'{h}\t{r}\n')
print(len(filas), 'archivos')
