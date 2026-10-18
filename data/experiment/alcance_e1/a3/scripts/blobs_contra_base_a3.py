"""U-ALCANCE-E1, A3 (USD 0, sin API; solo lectura): controla que cada archivo rastreado de una copia del repo tenga el blob
de la base. Lee `git ls-files -s` del repo y `git ls-tree -r <base>` (con -z, sin comillas en las rutas) y calcula el
blob de cada archivo de la copia como `git hash-object` («blob <bytes>\\0<contenido>», sha1; el repo no tiene
.gitattributes, así que no hay filtros). No abre los archivos de entorno ni los `NO_ABRIR_` (no están en la copia) ni nada
bajo las carpetas de salidas de la tanda 1 (T2 a T5): esas rutas se cuentan aparte y no se listan.
Uso: python3 -I -B blobs_contra_base_a3.py <repo> <base> <copia> <salida.json>
"""
import fnmatch
import hashlib
import json
import os
import subprocess
import sys
from collections import Counter
from pathlib import Path

repo, base, copia, salida = sys.argv[1], sys.argv[2], Path(sys.argv[3]), Path(sys.argv[4])
SIN_ABRIR = ("data/experiment/reextraccion_v2/corpus_tanda1/", "data/experiment/tanda1/t2/", "data/experiment/tanda1/t3/",
             "data/experiment/tanda1/t4/", "data/experiment/tanda1/t5/")
EXCLUIDOS_DEL_RSYNC = ("data/experiment/tanda1/t4/", "data/experiment/tanda1/t5/")


def git(*a: str) -> bytes:
    return subprocess.run(["git", "--no-optional-locks", "-C", repo, *a], capture_output=True, check=True).stdout


def blob(p: Path) -> str:
    b = p.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest()


idx = {}
for reg in git("ls-files", "-s", "-z").split(b"\0"):
    if reg:
        meta, ruta = reg.decode("utf-8").split("\t", 1)
        modo, sha, _etapa = meta.split()
        idx[ruta] = (modo, sha)
arbol = {}
for reg in git("ls-tree", "-r", "-z", base).split(b"\0"):
    if reg:
        meta, ruta = reg.decode("utf-8").split("\t", 1)
        modo, _tipo, sha = meta.split()
        arbol[ruta] = (modo, sha)

faltan, distintos, iguales, cuentas = Counter(), [], {}, Counter()
for ruta, (modo, sha) in sorted(arbol.items()):
    p = copia / ruta
    nombre = ruta.rsplit("/", 1)[-1]
    if ruta.startswith(EXCLUIDOS_DEL_RSYNC):
        faltan["t4 y t5 (excluidos del rsync)"] += 1
        continue
    if modo == "120000":
        faltan["enlace simbólico (el rsync --no-links lo saltea)"] += int(not p.exists())
        cuentas["enlaces rastreados"] += 1
        continue
    if any(fnmatch.fnmatch(nombre, x) for x in (".env", ".env.*", "*.env", "NO_ABRIR_*")):
        faltan["entorno o NO_ABRIR_ (excluidos del rsync, sin abrir)"] += 1
        continue
    if "/__pycache__/" in f"/{ruta}" or nombre == ".DS_Store":
        faltan["__pycache__ o .DS_Store (excluidos del rsync)"] += 1
        continue
    if not p.is_file():
        faltan["otros (falta en la copia)"] += 1
        distintos.append([ruta, "falta en la copia"])
        continue
    if ruta.startswith(SIN_ABRIR):
        cuentas["en carpetas de salidas de la tanda 1 (no se abren)"] += 1
        continue
    b = blob(p)
    if b == sha:
        iguales[ruta] = sha
    else:
        distintos.append([ruta, f"blob {b} en la copia, {sha} en la base"])

no_rastreados = Counter()
for raiz, dirs, archivos in os.walk(copia):
    rel_raiz = Path(raiz).relative_to(copia).as_posix()
    rel_raiz = "" if rel_raiz == "." else rel_raiz + "/"
    if rel_raiz.startswith(SIN_ABRIR):
        dirs[:] = []
        continue
    for a in archivos:
        r = rel_raiz + a
        if r not in arbol:
            # data/<carpeta>/<carpeta>; lo demás, solo su carpeta de primer nivel (las de sesiones tienen nombres de
            # personas en el segundo nivel, que no van a un artefacto).
            partes = r.split("/")
            no_rastreados["/".join(partes[:3]) if partes[0] == "data" and len(partes) > 3 else partes[0]] += 1

res = {"repo_head": git("rev-parse", "HEAD").decode().strip(), "base": git("rev-parse", base).decode().strip(),
       "indice_igual_al_arbol_de_la_base": idx == arbol, "rastreados_en_la_base": len(arbol),
       "comparados_iguales": len(iguales), "distintos_o_faltantes": distintos, "sin_comparar": dict(faltan),
       "otras_cuentas": dict(cuentas), "no_rastreados_en_la_copia_por_carpeta": dict(sorted(no_rastreados.items())),
       "blobs_iguales": iguales}
salida.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in res.items() if k != "blobs_iguales"}, ensure_ascii=False, indent=1))
sys.exit(0 if not distintos and res["indice_igual_al_arbol_de_la_base"] else 1)
