"""Mesa, §223 (21/10/2026): el control de la lectura de la autora del primer tramo de T4 de la tanda final, contra su sello, contra el
material y contra el paquete del FRENO del primer tramo. Es el de la tanda 1 (`data/experiment/tanda1/t4/control_lectura_mesa/`, §162)
con las rutas de la tanda final, con dos cambios: el material del primer tramo no está rastreado (entra con el TF4a), así que se controla
contra el paquete de ese FRENO (`revision_tanda_final_FRENO_T4_tramo1/`, manifiesto `0f2d428e…`, en la copia permanente); y el sello no
vino pegado en el mensaje, así que se controla contra las marcadas y sus horas. USD 0, sin API, sin escribir en el repo: la conversión se
corre de nuevo sobre una copia, en una carpeta temporal. No informa ninguna cuenta por veredicto: de cada muestra dice solo si hay alguna
respuesta que no decide (dudosa o no decidible).
Uso: python3 -I -B control_lectura_T4_mesa.py <salida.json>"""
import csv
import hashlib
import io
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
T4 = "data/experiment/tanda_final/t4"
REL = f"{T4}/lectura_autora"
L = REPO / REL
PQ_T1 = Path.home() / ("INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/afadde2e-6298-47fb-9777-7fcb43152d50/scratchpad/"
                       "revision_tanda_final_FRENO_T4_tramo1")
git = lambda *a: subprocess.run(["git", "--no-optional-locks", "-C", str(REPO), *a], capture_output=True, check=True).stdout  # noqa: E731
sha = lambda b: hashlib.sha256(b).hexdigest()  # noqa: E731
MUESTRAS = ["cola", "aceptadas_items", "aceptadas_no_items", "vigilancia_2", "vigilancia_7", "vigilancia_1", "vigilancia_3", "observacion_12"]
EXPORT = {m: f"{m}_exportada.csv" for m in MUESTRAS}
FILAS = {m: (6 if m == "vigilancia_7" else 30) for m in MUESTRAS}       # revisión del primer tramo, §207: 216 filas
DE_LA_AUTORA = sorted([f"{REL}/{m}_marcada.csv" for m in MUESTRAS] + [f"{REL}/{EXPORT[m]}" for m in MUESTRAS] + [f"{REL}/sello_lectura_T4.txt"])
res, mal = {}, []


def ok(k, c, d=None):
    res[k] = {"pasa": bool(c), **({"detalle": d} if d is not None else {})}
    if not c:
        mal.append(k)


# 1. el sello
sello = (L / "sello_lectura_T4.txt").read_text(encoding="utf-8").splitlines()
filas_sello = [re.fullmatch(r"([0-9a-f]{64})  (\S+_marcada\.csv)  (\d{4}-\d\d-\d\d \d\d:\d\d:\d\d [+-]\d{4})", l) for l in sello]
ok("1a el sello: 8 líneas con sha256, nombre y hora", len(sello) == 8 and all(filas_sello))
por_nombre = {f.group(2): (f.group(1), f.group(3)) for f in filas_sello if f}
ok("1b el sello nombra las ocho marcadas, una vez cada una", sorted(por_nombre) == sorted(f"{m}_marcada.csv" for m in MUESTRAS))
ok("1c cada marcada tiene el sha256 de su línea del sello", all(sha((L / n).read_bytes()) == h for n, (h, _) in por_nombre.items()))
ok("1d la hora del sello de cada marcada es su hora de modificación (date -r)",
   all(datetime.fromtimestamp((L / n).stat().st_mtime).astimezone().strftime("%Y-%m-%d %H:%M:%S %z") == t for n, (_, t) in por_nombre.items()))
# 1e, informativo: el LEEME de la tanda final (`9e224f09…`, «El sello») no pide dejarlas de solo lectura, como sí se hizo en la tanda 1
res["1e_informativo_de_solo_lectura"] = {n: not ((L / n).stat().st_mode & 0o222) for n in list(por_nombre) + ["sello_lectura_T4.txt"]}
# 2. el material del primer tramo, sin cambios, y nada más que lo de la autora
nuevos = sorted(l[3:] for l in git("status", "--porcelain=v1", "-uall", "--", T4).decode().splitlines() if l.startswith("?? "))
del_tramo1 = [r for r in nuevos if r not in DE_LA_AUTORA]
ok("2a sin rastrear en t4/: los 17 de la autora y 40 del primer tramo, nada más", sorted(set(DE_LA_AUTORA) - set(nuevos)) == [] and
   len(del_tramo1) == 40, {"faltan_de_la_autora": sorted(set(DE_LA_AUTORA) - set(nuevos)), "del_primer_tramo": len(del_tramo1)})
pq = {sha(p.read_bytes()) for p in PQ_T1.rglob("*") if p.is_file() and p.name not in ("manifest.txt", ".DS_Store")}
ok("2b los 40 del primer tramo dan un sha256 del paquete de su FRENO (0f2d428e…)",
   sha((PQ_T1 / "manifest.txt").read_bytes()).startswith("0f2d428e") and all(sha((REPO / r).read_bytes()) in pq for r in del_tramo1))
conv = (L / "convertir_lectura_T4.py").read_text(encoding="utf-8")
SHA_PL = dict(re.findall(r'"(\w+)": "([0-9a-f]{64})"', conv.split("SHA_PLANILLAS = {", 1)[1].split("}", 1)[0]))
ok("2c las 8 planillas en blanco tienen el sha256 que controla la conversión", set(SHA_PL) == set(MUESTRAS)
   and all(sha((L / f"{m}.csv").read_bytes()) == SHA_PL[m] for m in MUESTRAS))
ok("2d ningún documento de Numbers ni temporal en t4/", not any(p.suffix == ".numbers" or p.name.startswith(("~", ".~")) or p.suffix == ".tmp"
                                                               for p in (REPO / T4).rglob("*")))
# 3. cada marcada contra su planilla
COLS = ["id", "celda", "ficha", "propuesta", "justificacion", "veredicto_autora", "nota_autora"]
CAPAS = ["E0", "E1-prompt", "E1-validador", "catálogo", "E2", "E3", "ensamblado"]
UNIDAD = ["con error", "sin error", "dudosa"]
VALIDAS = {"cola": UNIDAD, "aceptadas_items": UNIDAD, "aceptadas_no_items": UNIDAD,
           "vigilancia_2": ["vaciamiento", "no vaciamiento", "no decidible"], "vigilancia_7": ["con apoyo", "sin apoyo", "no decidible"],
           "vigilancia_1": ["sí", "no", "no decidible"], "vigilancia_3": ["duplicación", "distintos"],
           "observacion_12": ["correcta", "no decidible"] + [f"incorrecta ({c})" for c in CAPAS]}
assert all(f'"{v}"' in conv or v.startswith("incorrecta (") for vs in VALIDAS.values() for v in vs), "las respuestas no son las de la conversión"
leer = lambda p: list(csv.reader(io.StringIO(p.read_text(encoding="utf-8"), newline=""), delimiter=";"))  # noqa: E731
forma, indecisas = {}, {}
for m in MUESTRAS:
    pl, mk = leer(L / f"{m}.csv"), leer(L / f"{m}_marcada.csv")
    filas_ok = mk[0] == COLS and len(mk) == len(pl) and all(len(r) == 7 for r in mk) and [r[:5] for r in mk] == [r[:5] for r in pl]
    validas = all(r[5] in VALIDAS[m] for r in mk[1:])
    razon = all(r[6] for r in mk[1:] if r[5] != r[3])
    fichas = all(any((b / r[2].split("#")[0]).exists() for b in (REPO / T4, REPO / "data/experiment/tanda_final", REPO)) for r in mk[1:])
    forma[m] = {"filas": len(mk) - 1, "columnas_fijas_iguales": filas_ok, "veredictos_validos": validas, "razon_cuando_cambia": razon,
                "fichas_existen": fichas}
    indecisas[m] = any(r[5] in ("dudosa", "no decidible") for r in mk[1:])
ok("3a cada marcada: la cabecera, las filas y las cinco columnas fijas de su planilla; veredictos válidos; razón donde cambia la "
   "propuesta; las fichas existen", all(all(v for k, v in f.items() if k != "filas") for f in forma.values()), forma)
ok("3b las filas por muestra son las del primer tramo (30, y 6 en la vigilancia (7)): 216 en total",
   all(f["filas"] == FILAS[m] for m, f in forma.items()) and sum(f["filas"] for f in forma.values()) == 216)
# 4. la conversión, de nuevo, sobre una copia
iguales, salidas = {}, {}
for m in MUESTRAS:
    with tempfile.TemporaryDirectory(prefix="conv_t4tf_") as t:
        T = Path(t)
        for n in ("convertir_lectura_T4.py", f"{m}.csv", EXPORT[m]):
            shutil.copy2(L / n, T / n)
        p = subprocess.run([sys.executable, "-I", "-B", str(T / "convertir_lectura_T4.py"), m, EXPORT[m]], capture_output=True, text=True,
                           cwd=str(T), env={"PATH": os.environ.get("PATH", "/usr/bin:/bin"), "HOME": str(Path.home()), "LANG": "en_US.UTF-8"})
        iguales[m] = p.returncode == 0 and (T / f"{m}_marcada.csv").exists() and \
            (T / f"{m}_marcada.csv").read_bytes() == (L / f"{m}_marcada.csv").read_bytes()
        salidas[m] = [l for l in p.stdout.splitlines() if l.startswith(("OK:", "arreglos", "avisos"))] or [p.stderr.strip()[-200:]]
ok("4 la conversión, corrida de nuevo sobre una copia de la conversión, la planilla y la exportación, da cada marcada byte a byte",
   all(iguales.values()), iguales)
res["consola_de_la_conversion_sin_cuentas_por_veredicto"] = salidas
res["muestras_con_alguna_respuesta_que_no_decide"] = indecisas
res["mal"] = mal
OUT.write_text(__import__("json").dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for k, v in res.items():
    if isinstance(v, dict) and "pasa" in v:
        print(("OK " if v["pasa"] else "MAL"), k, "" if v["pasa"] else v.get("detalle"))
print("1e, informativo (el LEEME de la tanda final no lo pide): de solo lectura",
      sum(res["1e_informativo_de_solo_lectura"].values()), "de", len(res["1e_informativo_de_solo_lectura"]))
print("muestras con alguna dudosa o no decidible:", {m: ("sí" if v else "no") for m, v in indecisas.items()})
print(f"controles: {sum(1 for v in res.values() if isinstance(v, dict) and 'pasa' in v)}, mal: {len(mal)} {mal}")
sys.exit(1 if mal else 0)
