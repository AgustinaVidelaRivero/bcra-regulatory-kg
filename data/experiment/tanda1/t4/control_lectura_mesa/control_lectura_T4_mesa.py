"""Mesa, §162 (18/10/2026): el control de la lectura de la autora del primer tramo de T4 de la tanda 1, contra su sello y contra el
material. Pedido de la autora del 18/10/2026, recibido a las 16:27:04 (y sus horas, a las 16:27:43). USD 0, sin API, sin escribir en el repo:
la conversión se corre de nuevo sobre una copia en una carpeta temporal. No informa ninguna cuenta por veredicto: de cada muestra dice
solo si hay alguna respuesta que no decide (dudosa o no decidible), que hace falta para la regla del segundo tramo.
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
REL = "data/experiment/tanda1/t4/lectura_autora"
L = REPO / REL
git = lambda *a: subprocess.run(["git", "--no-optional-locks", "-C", str(REPO), *a], capture_output=True, check=True).stdout  # noqa: E731
sha = lambda b: hashlib.sha256(b).hexdigest()  # noqa: E731
MUESTRAS = ["cola", "aceptadas_items", "aceptadas_no_items", "vigilancia_2", "vigilancia_7", "vigilancia_1", "vigilancia_3", "observacion_12"]
EXPORT = {m: f"{m}_exportada.csv" for m in MUESTRAS} | {"aceptadas_no_items": "aceptadas_no_items_exportadas.csv"}   # dato de la autora
SELLO_MSJ = {"aceptadas_items": ("88526906a7443187192dc2cc50eacc82635ccf2b744cc075ffe3d6fa0851a723", "2026-10-18 15:06:08 -0300"),
             "aceptadas_no_items": ("dda313dc6add4592c66a6ea64ca4807403ef7f144658677850d46548cc275eb5", "2026-10-18 15:22:32 -0300"),
             "cola": ("818850df2cb0a68018fcc23dbf886f1d8695e4b91e063668f156b949f5baafdb", "2026-10-18 14:52:59 -0300"),
             "observacion_12": ("b1ffe65c7390c763b9f05890a198d58aa3346638f47964551cd03333187caa94", "2026-10-18 16:23:35 -0300"),
             "vigilancia_1": ("06521c23c60d02df673c79946d3af544fe35dedd6965cc0426df74cf6dcb788a", "2026-10-18 15:51:00 -0300"),
             "vigilancia_2": ("0317bac0a05c1960eb9db6332042c6d0a94e97bcf5668038f7ca91cfffef1d48", "2026-10-18 15:35:49 -0300"),
             "vigilancia_3": ("c3a268ea4d4daca0bda9ee46a5406c00739bd908ff45b900f24512a85f44ee31", "2026-10-18 16:03:25 -0300"),
             "vigilancia_7": ("a32e94f2fe099ba01e90a2b1f7817930e508287bcb27ca6c10f507ffe9dfb777", "2026-10-18 15:39:21 -0300")}
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
ok("1b el sello es el del mensaje de la autora, línea por línea",
   all(por_nombre.get(f"{m}_marcada.csv") == SELLO_MSJ[m] for m in MUESTRAS))
ok("1c cada marcada tiene el sha256 del sello",
   all(sha((L / n).read_bytes()) == h for n, (h, _) in por_nombre.items()))
ok("1d la hora del sello de cada marcada es su hora de modificación (date -r)",
   all(datetime.fromtimestamp((L / n).stat().st_mtime).astimezone().strftime("%Y-%m-%d %H:%M:%S %z") == t for n, (_, t) in por_nombre.items()))
ok("1e las ocho marcadas y el sello, de solo lectura",
   all(not ((L / n).stat().st_mode & 0o222) for n in list(por_nombre) + ["sello_lectura_T4.txt"]))
# 2. el material rastreado, sin cambios
rastreados = git("ls-files", REL).decode().split()
ok("2a los 10 archivos rastreados de la carpeta (8 planillas, el LEEME y la conversión), iguales a HEAD",
   len(rastreados) == 10 and all(sha(git("show", f"HEAD:{r}")) == sha((REPO / r).read_bytes()) for r in rastreados))
conv = (L / "convertir_lectura_T4.py").read_text(encoding="utf-8")
SHA_PL = dict(re.findall(r'"(\w+)": "([0-9a-f]{64})"', conv.split("SHA_PLANILLAS = {", 1)[1].split("}", 1)[0]))
ok("2b las 8 planillas en blanco tienen el sha256 que controla la conversión", set(SHA_PL) == set(MUESTRAS)
   and all(sha((L / f"{m}.csv").read_bytes()) == SHA_PL[m] for m in MUESTRAS))
nuevos = sorted(l[3:] for l in git("status", "--porcelain=v1", "-uall", "--", REL).decode().splitlines() if l.startswith("?? "))
esperados = sorted([f"{REL}/{m}_marcada.csv" for m in MUESTRAS] + [f"{REL}/{EXPORT[m]}" for m in MUESTRAS] + [f"{REL}/sello_lectura_T4.txt"])
ok("2c sin rastrear, solo las 8 exportaciones, las 8 marcadas y el sello (sin .numbers ni temporales)", nuevos == esperados,
   sorted(set(nuevos) ^ set(esperados)))
ok("2d el .DS_Store, ignorado por git", subprocess.run(["git", "--no-optional-locks", "-C", str(REPO), "check-ignore", "-q",
                                                       f"{REL}/.DS_Store"]).returncode == 0)
# 3. cada marcada contra su planilla
COLS = ["id", "celda", "ficha", "propuesta", "justificacion", "veredicto_autora", "nota_autora"]
# las respuestas válidas, las de la conversión (se controla abajo que estén en su texto; la conversión no se importa)
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
    fichas = all((REPO / "data/experiment/tanda1" / r[2].split("#")[0]).exists() or (REPO / r[2].split("#")[0]).exists() for r in mk[1:])
    forma[m] = {"filas": len(mk) - 1, "columnas_fijas_iguales": filas_ok, "veredictos_validos": validas, "razon_cuando_cambia": razon,
                "fichas_existen": fichas}
    indecisas[m] = any(r[5] in ("dudosa", "no decidible") for r in mk[1:])
ok("3 cada marcada: la cabecera, las filas y las cinco columnas fijas de su planilla; veredictos válidos; razón donde cambia la "
   "propuesta; las fichas existen", all(all(v for k, v in f.items() if k != "filas") for f in forma.values()), forma)
ok("3b las filas por muestra son las del LEEME (30, y 4 en la vigilancia (7))",
   all(f["filas"] == (4 if m == "vigilancia_7" else 30) for m, f in forma.items()))
# 4. la conversión, de nuevo, sobre una copia
iguales, salidas = {}, {}
for m in MUESTRAS:
    with tempfile.TemporaryDirectory(prefix="conv_t4_") as t:
        T = Path(t)
        for n in ("convertir_lectura_T4.py", f"{m}.csv", EXPORT[m]):
            shutil.copy2(L / n, T / n)
        p = subprocess.run([sys.executable, "-I", "-B", str(T / "convertir_lectura_T4.py"), m, EXPORT[m]], capture_output=True, text=True,
                           cwd=str(T))
        iguales[m] = p.returncode == 0 and (T / f"{m}_marcada.csv").read_bytes() == (L / f"{m}_marcada.csv").read_bytes()
        salidas[m] = [l for l in p.stdout.splitlines() if l.startswith(("OK:", "arreglos", "avisos"))]
        assert sha((L / EXPORT[m]).read_bytes()) != SHA_PL[m]
ok("4 la conversión, corrida de nuevo sobre una copia de la conversión, la planilla y la exportación, da cada marcada byte a byte",
   all(iguales.values()), iguales)
res["consola_de_la_conversion_sin_cuentas_por_veredicto"] = salidas
res["muestras_con_alguna_respuesta_que_no_decide"] = indecisas
res["mal"] = mal
OUT.write_text(__import__("json").dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for k, v in res.items():
    if isinstance(v, dict) and "pasa" in v:
        print(("OK " if v["pasa"] else "MAL"), k, "" if v["pasa"] else v.get("detalle"))
print("muestras con alguna dudosa o no decidible:", {m: ("sí" if v else "no") for m, v in indecisas.items()})
print(f"controles: {sum(1 for v in res.values() if isinstance(v, dict) and 'pasa' in v)}, mal: {len(mal)} {mal}")
sys.exit(1 if mal else 0)
