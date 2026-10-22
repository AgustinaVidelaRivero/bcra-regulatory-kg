"""Mesa, §230 (22/10/2026): el control de la lectura de la autora de la ampliación de T4 (tanda final, aceptadas no ítems), contra su
sello, contra la planilla y contra el convertidor commiteados con el TF4b. Es el control del primer tramo
(`t4/control_lectura_mesa/control_lectura_T4_mesa.py`, §223) con una sola muestra. USD 0, sin API, sin escribir en el repo: la
conversión se corre de nuevo sobre una copia, en una carpeta temporal. No informa ninguna cuenta por veredicto: dice solo si hay alguna
respuesta que no decide («dudosa»).
Uso: python3 -I -B control_lectura_T4_ampliacion_mesa.py <salida.json>"""
import csv
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path

OUT = Path(sys.argv[1])
REPO = Path.home() / "INGENIERIA IA/TESIS/bcra-regulatory-kg"
AM = "data/experiment/tanda_final/t4/ampliacion"
REL = f"{AM}/lectura_autora"
L = REPO / REL
M = "aceptadas_no_items_ampliacion"
git = lambda *a: subprocess.run(["git", "--no-optional-locks", "-C", str(REPO), *a], capture_output=True, check=True).stdout  # noqa: E731
sha = lambda b: hashlib.sha256(b).hexdigest()  # noqa: E731
DE_LA_AUTORA = sorted([f"{REL}/{M}_exportada.csv", f"{REL}/{M}_marcada.csv", f"{REL}/sello_lectura_T4_ampliacion.txt"])
res, mal = {}, []


def ok(k, c, d=None):
    res[k] = {"pasa": bool(c), **({"detalle": d} if d is not None else {})}
    if not c:
        mal.append(k)


# 1. el sello
sello = (L / "sello_lectura_T4_ampliacion.txt").read_text(encoding="utf-8").splitlines()
filas_sello = [re.fullmatch(r"([0-9a-f]{64})  (\S+_marcada\.csv)  (\d{4}-\d\d-\d\d \d\d:\d\d:\d\d [+-]\d{4})", l) for l in sello]
ok("1a el sello: una línea con sha256, nombre y hora", len(sello) == 1 and all(filas_sello))
por_nombre = {f.group(2): (f.group(1), f.group(3)) for f in filas_sello if f}
ok("1b el sello nombra la marcada de la ampliación", sorted(por_nombre) == [f"{M}_marcada.csv"])
ok("1c la marcada tiene el sha256 del sello (155e23dc…)", all(sha((L / n).read_bytes()) == h and h.startswith("155e23dc") for n, (h, _) in por_nombre.items()))
ok("1d la hora del sello es la hora de modificación de la marcada (date -r)",
   all(datetime.fromtimestamp((L / n).stat().st_mtime).astimezone().strftime("%Y-%m-%d %H:%M:%S %z") == t for n, (_, t) in por_nombre.items()))
res["1e_informativo_de_solo_lectura"] = {n: not ((L / n).stat().st_mode & 0o222) for n in [f"{M}_marcada.csv", "sello_lectura_T4_ampliacion.txt"]}
# 2. lo commiteado, sin cambios, y nada más que lo de la autora
nuevos = sorted(l[3:] for l in git("status", "--porcelain=v1", "-uall", "--", "data/experiment/tanda_final/t4").decode().splitlines() if l.startswith("?? "))
ok("2a sin rastrear en t4/: los 3 de la autora (la exportación, la marcada y el sello), nada más", nuevos == DE_LA_AUTORA, nuevos)
mod = git("status", "--porcelain=v1", "--untracked-files=no", "--", "data/experiment/tanda_final").decode().strip()
ok("2b nada rastreado modificado en tanda_final/: la planilla, el convertidor y el LEEME son los del TF4b", mod == "")
ok("2c la planilla en blanco es la de la ampliación (e99eaa2c…)", sha((L / f"{M}.csv").read_bytes()).startswith("e99eaa2c")
   and sha((L / f"{M}.csv").read_bytes()) == sha(git("show", f"HEAD:{REL}/{M}.csv")))
ok("2d ningún documento de Numbers ni temporal en t4/ampliacion/", not any(p.suffix == ".numbers" or p.name.startswith(("~", ".~")) or p.suffix == ".tmp"
                                                                          for p in (REPO / AM).rglob("*")))
# 3. la marcada contra su planilla
COLS = ["id", "celda", "ficha", "propuesta", "justificacion", "veredicto_autora", "nota_autora"]
VALIDAS = ["con error", "sin error", "dudosa"]
leer = lambda p: list(csv.reader(io.StringIO(p.read_text(encoding="utf-8"), newline=""), delimiter=";"))  # noqa: E731
pl, mk = leer(L / f"{M}.csv"), leer(L / f"{M}_marcada.csv")
forma = {"filas": len(mk) - 1,
         "columnas_fijas_iguales": mk[0] == COLS and len(mk) == len(pl) and all(len(r) == 7 for r in mk) and [r[:5] for r in mk] == [r[:5] for r in pl],
         "veredictos_validos": all(r[5] in VALIDAS for r in mk[1:]),
         "razon_cuando_cambia": all(r[6] for r in mk[1:] if r[5] != r[3]),
         "fichas_existen": all((REPO / "data/experiment/tanda_final" / r[2].split("#")[0]).exists() or (REPO / r[2].split("#")[0]).exists() for r in mk[1:])}
ok("3a la marcada: la cabecera, las filas y las cinco columnas fijas de su planilla; veredictos válidos; razón donde cambia la propuesta; "
   "las fichas existen", all(v for k, v in forma.items() if k != "filas"), forma)
ok("3b 30 filas", forma["filas"] == 30)
# 4. la conversión, de nuevo, sobre una copia
with tempfile.TemporaryDirectory(prefix="conv_t4_ampl_") as t:
    T = Path(t)
    for n in ("convertir_lectura_T4_ampliacion.py", f"{M}.csv", f"{M}_exportada.csv"):
        shutil.copy2(L / n, T / n)
    p = subprocess.run([sys.executable, "-I", "-B", str(T / "convertir_lectura_T4_ampliacion.py"), M, f"{M}_exportada.csv"], capture_output=True,
                       text=True, cwd=str(T), env={"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "HOME": str(Path.home()), "LANG": "en_US.UTF-8"})
    igual = p.returncode == 0 and (T / f"{M}_marcada.csv").exists() and (T / f"{M}_marcada.csv").read_bytes() == (L / f"{M}_marcada.csv").read_bytes()
ok("4 la conversión, corrida de nuevo sobre una copia del convertidor, la planilla y la exportación, da la marcada byte a byte", igual)
res["muestra_con_alguna_dudosa"] = any(r[5] == "dudosa" for r in mk[1:])
res["mal"] = mal
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for k, v in res.items():
    if isinstance(v, dict) and "pasa" in v:
        print(("OK " if v["pasa"] else "MAL"), k, "" if v["pasa"] else v.get("detalle"))
print("1e, informativo: de solo lectura", sum(res["1e_informativo_de_solo_lectura"].values()), "de", len(res["1e_informativo_de_solo_lectura"]))
print("alguna dudosa:", "sí" if res["muestra_con_alguna_dudosa"] else "no")
print(f"controles: {sum(1 for v in res.values() if isinstance(v, dict) and 'pasa' in v)}, mal: {len(mal)} {mal}")
sys.exit(1 if mal else 0)
