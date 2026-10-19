"""
06_paquete.py — U-TRIP-V: el paquete revision_U-TRIP-V/ para la mesa, su manifest.txt y su copia con ditto.

  - revision_U-TRIP-V/: el FRENO, los scripts, las salidas (con el log del rsync), las fichas y lectura/sellar_hoja.py. Las
    hojas de la autora, vacías todavía, NO van: van por su sha256 en el manifest (líneas de comentario, rutas relativas a
    tripletas_v/).
  - manifest.txt: una línea por archivo, `<sha256>  <ruta>` (verificable con `shasum -a 256 -c manifest.txt`).
  - la copia con `ditto` a --destino, verificada con `shasum -a 256 -c` en el destino y comparada archivo por archivo.
No pisa un paquete ni un destino que ya existan.
  python3 -I -B 06_paquete.py --raiz <tripletas_v> --rsync-log <copia.rsync.log> --destino <.../revision_U-TRIP-V>
"""
from __future__ import annotations

import argparse
import filecmp
import shutil
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun_v as V  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--raiz", type=Path, required=True)
    ap.add_argument("--rsync-log", type=Path, required=True)
    ap.add_argument("--destino", type=Path, required=True)
    a = ap.parse_args()
    R = a.raiz.resolve()
    P = R / "revision_U-TRIP-V"
    if P.exists() or a.destino.exists():
        raise SystemExit("el paquete o el destino ya existen: no se pisan")
    P.mkdir()
    shutil.copy2(R / "FRENO_U-TRIP-V.md", P / "FRENO_U-TRIP-V.md")
    for sub, patron in (("scripts", "*.py"), ("salidas", "*"), ("fichas", "*")):
        (P / sub).mkdir()
        for f in sorted((R / sub).glob(patron)):
            if f.is_file():
                shutil.copy2(f, P / sub / f.name)
    shutil.copy2(a.rsync_log, P / "salidas" / "copia.rsync.log")
    (P / "lectura").mkdir()
    shutil.copy2(R / "lectura" / "sellar_hoja.py", P / "lectura" / "sellar_hoja.py")

    archivos = sorted(p for p in P.rglob("*") if p.is_file())
    hojas = sorted((R / "lectura").glob("hoja_*.csv"))
    lineas = ["# U-TRIP-V: paquete para la revisión de la mesa (sha256 de cada archivo; verificar con",
              "# `shasum -a 256 -c manifest.txt` desde esta carpeta).",
              f"# {len(archivos)} archivos. Generado {V.hora()}."]
    lineas += [f"{V.sha_archivo(p)}  {p.relative_to(P).as_posix()}" for p in archivos]
    lineas += ["#", f"# Las hojas de la autora, vacías todavía, no van en el paquete: van por su sha256 ({len(hojas)}; rutas",
               "# relativas a tripletas_v/):"]
    lineas += [f"# {V.sha_archivo(h)}  lectura/{h.name}" for h in hojas]
    (P / "manifest.txt").write_text("\n".join(lineas) + "\n", encoding="utf-8")
    s_man = V.sha_archivo(P / "manifest.txt")

    a.destino.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(["ditto", str(P), str(a.destino)], check=True)
    chk = subprocess.run(["shasum", "-a", "256", "-c", "manifest.txt"], cwd=a.destino, capture_output=True, text=True)
    ok_lineas = [l for l in chk.stdout.splitlines() if l.endswith(": OK")]
    cmp = filecmp.dircmp(P, a.destino)
    distintos = []
    def recorrer(d):
        distintos.extend(d.left_only + d.right_only + d.diff_files + d.funny_files)
        for s in d.subdirs.values():
            recorrer(s)
    recorrer(cmp)
    iguales = all(filecmp.cmp(p, a.destino / p.relative_to(P), shallow=False) for p in archivos + [P / "manifest.txt"])
    ok = chk.returncode == 0 and len(ok_lineas) == len(archivos) and not distintos and iguales
    print({"archivos": len(archivos), "hojas_por_sha256": len(hojas), "manifest_sha256": s_man,
           "shasum_c_en_el_destino": f"{len(ok_lineas)} OK de {len(archivos)}, rc {chk.returncode}",
           "dircmp_distintos": distintos, "byte_a_byte": iguales, "ok": ok})
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
