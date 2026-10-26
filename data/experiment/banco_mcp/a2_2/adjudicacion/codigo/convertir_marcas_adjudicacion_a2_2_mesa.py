"""convertir_marcas_adjudicacion_a2_2_mesa.py — las marcas selladas de la adjudicación de A2.2 de la autora, en los veredictos por id
opaco que lee el análisis de A2.2 (`analizar_a2_2.py --adjudicaciones`, `{id_opaco: veredicto}`; mesa, §277). USD 0.
Controla el sello (el sha256 y los bytes de la planilla), la estructura y que cada criterio tenga cumplido o no_cumplido. El veredicto
de cada ficha sale del mapping §2 de EV2 (`ev2_juez/mapping.py`, `veredicto_pregunta`, el de HEAD) y va a cada id opaco de la ficha,
según la clave. No pisa una salida. Imprime solo cuántas fichas y cuántos ids.
  python3 -I -B convertir_marcas_adjudicacion_a2_2_mesa.py <carpeta de lectura> <clave.json> <repo> <salida.json>
"""
import csv
import hashlib
import importlib.util
import io
import json
import subprocess
import sys
import unicodedata
from pathlib import Path

L, CL, REPO, OUT = (Path(x) for x in sys.argv[1:5])
MAPPING = "data/experiment/ev2_juez/mapping.py"


def frena(m):
    raise SystemExit(f"FRENO: {m}")


def plegar(s):
    s = unicodedata.normalize("NFD", (s or "").strip().lower())
    return "_".join("".join(c for c in s if unicodedata.category(c) != "Mn").replace("_", " ").split())


if OUT.exists():
    frena(f"{OUT.name} ya existe: no se pisa")
pl, sello = L / "planilla_adjudicacion_a2_2.csv", L / "sello_adjudicacion_a2_2.txt"
if not sello.exists():
    frena("la planilla no está sellada")
lin = [x for x in sello.read_text(encoding="utf-8").splitlines() if x and not x.startswith("#")]
b = pl.read_bytes()
if len(lin) != 1 or lin[0].split()[0] != hashlib.sha256(b).hexdigest() or int(lin[0].split()[1]) != len(b):
    frena("la planilla no da el sha256 y los bytes de su sello")
t = b.decode("utf-8-sig")
d = ";" if t.splitlines()[0].count(";") > t.splitlines()[0].count(",") else ","
filas = [[c.strip() for c in f] for f in csv.reader(io.StringIO(t), delimiter=d) if any(x.strip() for x in f)]
est = json.loads((L / "estructura_planilla.json").read_text(encoding="utf-8"))
if filas[0] != est["columnas"] or [f[:2] for f in filas[1:]] != est["renglones"]:
    frena("la planilla no tiene la estructura de la mesa")
h = subprocess.run(["git", "--no-optional-locks", "-C", str(REPO), "show", f"HEAD:{MAPPING}"], capture_output=True)
if h.returncode != 0 or h.stdout != (REPO / MAPPING).read_bytes():
    frena("mapping.py no es el de HEAD")
spec = importlib.util.spec_from_file_location("mapping_ev2", REPO / MAPPING)
MP = importlib.util.module_from_spec(spec)
spec.loader.exec_module(MP)
marcas = {}
for f in filas[1:]:
    v = plegar(f[2])
    if v not in ("cumplido", "no_cumplido"):
        frena(f"{f[0]}, criterio {f[1]}: sin veredicto válido")
    marcas.setdefault(f[0], []).append(v)
clave = json.loads(CL.read_text(encoding="utf-8"))
out = {}
for f in clave["fichas"]:
    m = marcas.get(f["ficha"])
    if m is None or len(m) != f["n_criterios"]:
        frena(f"la ficha {f['ficha']} no tiene sus {f['n_criterios']} criterios")
    v = MP.veredicto_pregunta(m)
    for i in f["ids_opacos"]:
        out[i] = v
if set(marcas) != {f["ficha"] for f in clave["fichas"]}:
    frena("la planilla y la clave no traen las mismas fichas")
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({"fichas": len(clave["fichas"]), "ids_opacos": len(out), "salida": OUT.name}, ensure_ascii=False))
