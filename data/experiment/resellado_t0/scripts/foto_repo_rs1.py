"""Foto sha256 del repo entero, sin .git (re-sellado único de la tanda 0; solo lectura).

Igual que data/experiment/reextraccion_v2/r0/controles/foto_repo_sin_env_R0.py, más la cláusula de carpetas vedadas: los
archivos de entorno (`.env`, `.env.*`, `*.env`) y los que empiezan con `NO_ABRIR_` NO se abren; se registran con os.stat,
solo por su tamaño y su fecha de modificación. Los enlaces simbólicos se registran por su destino (no se siguen).
Con --comparar, compara dos fotos y lista los archivos nuevos, quitados y cambiados.
Uso: python -I -B foto_repo_rs1.py <repo> <salida.json>
     python -I -B foto_repo_rs1.py --comparar <antes.json> <despues.json> <salida.json>
"""
import fnmatch
import hashlib
import json
import os
import sys
import time
from pathlib import Path

PATRONES_SIN_ABRIR = (".env", ".env.*", "*.env", "NO_ABRIR_*")


def sin_abrir(nombre: str) -> bool:
    return any(fnmatch.fnmatch(nombre, p) for p in PATRONES_SIN_ABRIR)


def foto(repo: Path) -> tuple[dict, list]:
    out, cerrados = {}, []
    for raiz, dirs, archivos in os.walk(repo):
        dirs[:] = sorted(d for d in dirs if not (Path(raiz) == repo and d == ".git"))
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
    return out, cerrados


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
              f"cambiados {len(c['cambiados'])}")
        sys.exit(0)
    repo, sal = Path(sys.argv[1]), Path(sys.argv[2])
    t0 = time.strftime("%Y-%m-%d %H:%M:%S")
    f, cerrados = foto(repo)
    t1 = time.strftime("%Y-%m-%d %H:%M:%S")
    sal.write_text(json.dumps({"tomada": f"{t0} a {t1}", "archivos": f}, ensure_ascii=False, indent=0) + "\n",
                   encoding="utf-8")
    print(len(f), "archivos", t0, "a", t1, "| registrados sin abrir (entorno y NO_ABRIR_):", len(cerrados))
