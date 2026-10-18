"""Foto sha256 del repo entero, sin .git (U-ALCANCE-E1, A3; solo lectura). Sigue a foto_repo_a2.py de A2, con dos cambios
de A3, porque T4 y T5 de la tanda 1 corren en el repo mientras A3 trabaja sobre su copia:

  - los archivos de entorno (`.env`, `.env.*`, `*.env`) y los que empiezan con `NO_ABRIR_` NO se abren, como en A2; se
    registran con os.stat, por su tamaño y su fecha de modificación;
  - las carpetas de salidas de las etapas de la tanda 1 (T2 a T5) NO se abren ni se listan: cada una entra como un solo
    renglón, el sha256 de sus (ruta, tamaño, mtime) ordenados, tomados con os.stat. Así una escritura en ellas se ve como
    un cambio de la carpeta, sin abrir sus archivos ni contar cuántos tiene (cegamiento de U-MED-VERIF; mandato de A3, §6,
    PROHIBIDO: las salidas de T2 de la tanda 1; el despacho de A3: tampoco las de T4 ni de T5).

Los enlaces simbólicos se registran por su destino (no se siguen). Con --comparar, compara dos fotos y lista los archivos
nuevos, quitados y cambiados.
Uso: python -I -B foto_repo_a3.py <repo> <salida.json>
     python -I -B foto_repo_a3.py --comparar <antes.json> <despues.json> <salida.json>
"""
import fnmatch
import hashlib
import json
import os
import sys
import time
from pathlib import Path

PATRONES_SIN_ABRIR = (".env", ".env.*", "*.env", "NO_ABRIR_*")
CARPETAS_SIN_ABRIR = (
    "data/experiment/reextraccion_v2/corpus_tanda1",   # salidas de T2 de la tanda 1 (y lo que T3 suma ahí)
    "data/experiment/tanda1/t2",
    "data/experiment/tanda1/t3",
    "data/experiment/tanda1/t4",
    "data/experiment/tanda1/t5",
)


def sin_abrir(nombre: str) -> bool:
    return any(fnmatch.fnmatch(nombre, p) for p in PATRONES_SIN_ABRIR)


def digesto_sin_abrir(carpeta: Path) -> str:
    """sha256 de los (ruta relativa, tamaño, mtime) de todo lo que hay bajo `carpeta`, con os.lstat: no abre nada."""
    h = hashlib.sha256()
    for raiz, dirs, archivos in os.walk(carpeta):
        dirs.sort()
        for a in sorted(archivos):
            p = Path(raiz) / a
            st = os.lstat(p)
            h.update(f"{p.relative_to(carpeta).as_posix()}\t{st.st_size}\t{st.st_mtime_ns}\n".encode("utf-8"))
    return h.hexdigest()


def foto(repo: Path) -> tuple[dict, list, list]:
    out, cerrados, carpetas = {}, [], []
    for raiz, dirs, archivos in os.walk(repo):
        rel_raiz = Path(raiz).relative_to(repo).as_posix()
        quedan = []
        for d in sorted(dirs):
            rel = d if rel_raiz == "." else f"{rel_raiz}/{d}"
            if rel_raiz == "." and d == ".git":
                continue
            if rel in CARPETAS_SIN_ABRIR:
                out[rel + "/"] = "carpeta_sin_abrir:" + digesto_sin_abrir(Path(raiz) / d)
                carpetas.append(rel)
                continue
            quedan.append(d)
        dirs[:] = quedan
        for a in sorted(archivos):
            p = Path(raiz) / a
            rel = p.relative_to(repo).as_posix()
            if p.is_symlink():
                out[rel] = "enlace:" + os.readlink(p)
                continue
            if sin_abrir(a):
                st = os.stat(p)
                out[rel] = f"sin_abrir:tamaño={st.st_size};mtime={int(st.st_mtime)}"
                cerrados.append(rel)
                continue
            h = hashlib.sha256()
            try:
                with open(p, "rb") as f:
                    for b in iter(lambda: f.read(1 << 20), b""):
                        h.update(b)
                out[rel] = h.hexdigest()
            except OSError as ex:
                out[rel] = f"ilegible:{type(ex).__name__}"
    return out, cerrados, carpetas


def comparar(a: dict, b: dict) -> dict:
    fa, fb = a["archivos"], b["archivos"]
    return {"antes": a["tomada"], "despues": b["tomada"], "n_antes": len(fa), "n_despues": len(fb),
            "nuevos": sorted(set(fb) - set(fa)), "quitados": sorted(set(fa) - set(fb)),
            "cambiados": sorted(k for k in set(fa) & set(fb) if fa[k] != fb[k])}


if __name__ == "__main__":
    if sys.argv[1] == "--comparar":
        a = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
        b = json.loads(Path(sys.argv[3]).read_text(encoding="utf-8"))
        c = comparar(a, b)
        Path(sys.argv[4]).write_text(json.dumps(c, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"{c['n_antes']} -> {c['n_despues']} | nuevos {len(c['nuevos'])} | quitados {len(c['quitados'])} | "
              f"cambiados {len(c['cambiados'])}: {c['nuevos'] + c['quitados'] + c['cambiados']}")
        sys.exit(0)
    repo, sal = Path(sys.argv[1]), Path(sys.argv[2])
    t0 = time.strftime("%Y-%m-%d %H:%M:%S")
    f, cerrados, carpetas = foto(repo)
    t1 = time.strftime("%Y-%m-%d %H:%M:%S")
    sal.write_text(json.dumps({"tomada": f"{t0} a {t1}", "carpetas_sin_abrir": carpetas, "archivos": f},
                              ensure_ascii=False, indent=0) + "\n", encoding="utf-8")
    print(len(f), "renglones", t0, "a", t1, "| registrados sin abrir (entorno y NO_ABRIR_):", len(cerrados),
          "| carpetas sin abrir:", len(carpetas))
