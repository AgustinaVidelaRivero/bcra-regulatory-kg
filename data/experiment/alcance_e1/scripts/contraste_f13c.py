"""
contraste_f13c.py — U-ALCANCE-E1, A1 (USD 0): prueba el contraste de selftest_clave_cache con cada variante de la fila F13c
propuesta. Por variante, clona la copia con los cambios de A1 (cp -cR: clon APFS, copia y no enlace), reemplaza la fila
F13c de la tabla del clon por la propuesta, corre selftest_clave_cache --salida-r2b en el clon y guarda su contraste.
Uso: contraste_f13c.py --repo REPO --copia COPIA --trabajo DIR (DIR fuera del repo; ahí van los clones y la salida)
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--repo", type=Path, required=True)
ap.add_argument("--copia", type=Path, required=True)
ap.add_argument("--trabajo", type=Path, required=True)
a = ap.parse_args()
repo, copia, t = a.repo.resolve(), a.copia.resolve(), a.trabajo.resolve()
if repo in t.parents or t == repo:
    raise SystemExit("--trabajo no puede estar dentro del repo")
aqui = Path(__file__).resolve().parent
tabla = "data/experiment/mantenimiento/tabla_reprocesamiento.md"
t.mkdir(parents=True, exist_ok=True)
subprocess.run([sys.executable, "-I", "-B", str(aqui / "f13c_propuesta.py"), str(copia / tabla), str(t)], check=True)
vigente = (t / "f13c_vigente.md").read_text(encoding="utf-8")
res = {}
for v in ("A", "B"):
    clon = t / f"clon_f13c_{v}"
    shutil.rmtree(clon, ignore_errors=True)
    subprocess.run(["cp", "-cR", str(copia), str(clon)], check=True)
    p = clon / tabla
    s = p.read_text(encoding="utf-8")
    if s.count(vigente) != 1:
        raise SystemExit("la fila F13c vigente no está una vez en la tabla del clon")
    p.write_text(s.replace(vigente, (t / f"f13c_propuesta_{v}.md").read_text(encoding="utf-8")), encoding="utf-8")
    out = t / f"selftest_clave_cache_con_f13c_{v}.json"
    r = subprocess.run([str(repo / ".venv" / "bin" / "python"), "-B", "data/experiment/mantenimiento/code/selftest_clave_cache.py",
                        "--salida-r2b", "data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b", "--out", str(out)],
                       cwd=clon, capture_output=True, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"})
    d = json.loads(out.read_text(encoding="utf-8"))
    res[v] = {"rc": r.returncode, "veredicto": d["veredicto"], "contraste": d["contraste_tabla"]["estado"],
              "discrepancias": d["contraste_tabla"].get("discrepancias")}
    shutil.rmtree(clon)
(t / "contraste_f13c.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(res, ensure_ascii=False, indent=1))
