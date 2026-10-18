"""B6.1, tanda 1, T4, segundo tramo: pasa al repo, archivo por archivo, los bytes que este tramo produjo en el scratchpad, con el modelo de
escribir_en_el_repo_t4t1.py. Ningún generador corre sobre el repo. Sin ampliación, el tramo no cambia ningún archivo: todo es nuevo y
va bajo data/experiment/tanda1/t4/.
Uso: python3 -I -B escribir_en_el_repo_t4t2.py <staging> <repo> <salida.json> [--seco]
  - Antes, frena sin escribir nada si: una ruta ya existe en el repo; una ruta está fuera de data/experiment/tanda1/t4/; un nombre empieza
    con NO_ABRIR_ o es un .env; un archivo trae la ruta del scratchpad o de la carpeta personal.
  - Después: cada archivo del repo es, byte a byte, el del staging.
"""
import hashlib
import json
import shutil
import sys
from pathlib import Path

sys.dont_write_bytecode = True
T4 = "data/experiment/tanda1/t4/"


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def escribir(ST: Path, R: Path, SAL: Path, seco: bool) -> int:
    archivos = sorted(p.relative_to(ST).as_posix() for p in ST.rglob("*") if p.is_file())
    res = {"nuevos": len(archivos), "cambian": 0, "escritos": {}, "seco": seco}
    fallas = [f"ya existe {r}" for r in archivos if (R / r).exists()]
    fallas += [f"fuera de {T4}: {r}" for r in archivos if not r.startswith(T4)]
    fallas += [f"nombre vedado: {r}" for r in archivos if Path(r).name.startswith("NO_ABRIR_") or Path(r).name.endswith(".env")
               or Path(r).name == ".env" or Path(r).name.startswith(".env.")]
    rutas = (b"/private" + b"/tmp", b"/Us" + b"ers/")  # partidas, para que este archivo no las lleve escritas
    fallas += [f"ruta absoluta en {r}" for r in archivos if any(x in (ST / r).read_bytes() for x in rutas)]
    res["fallas_previas"] = fallas
    if fallas:
        SAL.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print("FRENA sin escribir:", fallas[:10])
        return 1
    if not seco:
        for rel in archivos:
            d = R / rel
            d.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ST / rel, d)
        for rel in archivos:
            a, b = (R / rel).read_bytes(), (ST / rel).read_bytes()
            res["escritos"][rel] = {"sha256": sha(a), "igual_al_staging": a == b}
    res["ok"] = seco or all(v["igual_al_staging"] for v in res["escritos"].values())
    SAL.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(("SECO: " if seco else "") + f"nuevos {len(archivos)}, cambian 0; controles previos OK"
          + ("" if seco else f"; escritos iguales al staging: {sum(v['igual_al_staging'] for v in res['escritos'].values())} de "
             f"{len(res['escritos'])}"))
    return 0 if res["ok"] else 1


if __name__ == "__main__":
    sys.exit(escribir(Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve(), Path(sys.argv[3]), "--seco" in sys.argv))
