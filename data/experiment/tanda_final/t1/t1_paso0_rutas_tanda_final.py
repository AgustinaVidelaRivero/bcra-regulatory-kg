"""Paso 0 de T1 (tanda final): las 78 rutas del código de la cadena, en HEAD y en el árbol.

Lee data/experiment/tanda_final/preregistro/codigo_de_la_cadena_c66c7ecd_mesa.json y, para
cada ruta, compara su sha256 con el de `git show HEAD:<ruta>` y con el del archivo
del árbol. Sale con 0 si las 78 dan en los dos, con 1 si no.

Uso, desde la raíz del repo: python3 t1_paso0_rutas_tanda_final.py [--repo <raíz>] [--git-repo <repo>]
--git-repo (por defecto, --repo) es de dónde salen los objetos de HEAD: en una prueba sobre una copia, que no tiene
.git, es el repo, y el árbol es el de la copia.
"""
import argparse
import sys as _s
_s.dont_write_bytecode = True
import hashlib
import json
import subprocess
import sys
from pathlib import Path

SELLO = "data/experiment/tanda_final/preregistro/codigo_de_la_cadena_c66c7ecd_mesa.json"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default=".")
    ap.add_argument("--git-repo", default=None)
    a = ap.parse_args()
    repo = Path(a.repo).resolve()
    git_repo = Path(a.git_repo).resolve() if a.git_repo else repo
    d = json.loads((repo / SELLO).read_text(encoding="utf-8"))
    rutas = d["rutas"]
    ok_head = ok_arbol = 0
    malas = []
    for r in rutas:
        ruta, esperado = r["ruta"], r["sha256"]
        blob = subprocess.run(["git", "-C", str(git_repo), "show", f"HEAD:{ruta}"],
                              capture_output=True, check=False)
        h_head = hashlib.sha256(blob.stdout).hexdigest() if blob.returncode == 0 else None
        p = repo / ruta
        h_arbol = hashlib.sha256(p.read_bytes()).hexdigest() if p.is_file() else None
        ok_head += h_head == esperado
        ok_arbol += h_arbol == esperado
        if h_head != esperado or h_arbol != esperado:
            malas.append((ruta, esperado, h_head, h_arbol))
    print(f"sello: {SELLO} (n declarado = {d['n']}, commit = {d['commit']})")
    print(f"rutas leídas: {len(rutas)}")
    print(f"HEAD:  {ok_head} de {len(rutas)}")
    print(f"árbol: {ok_arbol} de {len(rutas)}")
    for m in malas:
        print("NO DA:", *m)
    sys.exit(0 if (not malas and len(rutas) == d["n"] == 78) else 1)


if __name__ == "__main__":
    main()
