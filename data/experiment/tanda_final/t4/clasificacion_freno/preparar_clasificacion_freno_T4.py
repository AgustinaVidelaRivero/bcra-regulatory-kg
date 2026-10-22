"""Prepara la clasificación por tipo de las 16 unidades con error de las aceptadas no ítems de T4 (tanda final), para la autora (mesa,
22/10/2026, §236). USD 0. Lo corre la autora, una vez, desde cualquier carpeta:

    python3 -I -B preparar_clasificacion_freno_T4.py "<repo>"

Lee del repo, en HEAD, las dos marcadas de las aceptadas no ítems (`t4/lectura_autora/aceptadas_no_items_marcada.csv` y
`t4/ampliacion/lectura_autora/aceptadas_no_items_ampliacion_marcada.csv`), controla cada una contra el sha256 de su sello, toma las filas
con `veredicto_autora` «con error» o «dudosa» y escribe la planilla en `data/experiment/tanda_final/t4/clasificacion_freno/`, con el
tramo de cada unidad (`tanda_final/preregistro/tramos_tanda_final.json`). Copia a la misma carpeta este script, el convertidor y el LEEME,
que tienen que dar su sha256. Frena sin escribir nada si algo no cierra, y no pisa nada: la carpeta no tiene que existir. No imprime
ningún id ni ningún texto de una unidad: solo cuántas filas y el sha256 de la planilla."""
import csv
import hashlib
import io
import json
import shutil
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
SHA_PROPIOS = {"convertir_clasificacion_freno_T4.py": "6b3113ca9c4e422667e06467ebfa0a7b5fe652fef523856a6b18f2afc620108c", "LEEME_clasificacion_freno_T4.md": "dc12df0b5eccf2a321279a8b8d165c5d6385a6843c35a86cdc4e404d3a84f013"}
TF = "data/experiment/tanda_final"
MARCADAS = {"primer_tramo": (f"{TF}/t4/lectura_autora/aceptadas_no_items_marcada.csv", f"{TF}/t4/lectura_autora/sello_lectura_T4.txt"),
            "ampliacion": (f"{TF}/t4/ampliacion/lectura_autora/aceptadas_no_items_ampliacion_marcada.csv",
                           f"{TF}/t4/ampliacion/lectura_autora/sello_lectura_T4_ampliacion.txt")}
COLS = ["n", "id", "celda", "tramo", "muestra", "ficha", "nota_de_la_lectura", "capa", "falla_de_esquema", "campo", "se_repite",
        "nota_clasificacion"]
CON_ERROR = ("con error", "dudosa")


def frenar(m):
    print("FRENO:", m)
    sys.exit(1)


if len(sys.argv) != 2:
    frenar('uso: python3 -I -B preparar_clasificacion_freno_T4.py "<repo>"')
REPO = Path(sys.argv[1]).expanduser().resolve()
SAL = REPO / TF / "t4/clasificacion_freno"
if not (REPO / ".git").exists():
    frenar(f"{REPO} no es la raíz del repo")
if SAL.exists():
    frenar(f"{SAL.relative_to(REPO)} ya existe: no piso nada")
for n, h in SHA_PROPIOS.items():
    if hashlib.sha256((AQUI / n).read_bytes()).hexdigest() != h:
        frenar(f"{n} no da su sha256: usá el material del paquete de la mesa tal cual")


def show(ruta):
    return subprocess.run(["git", "--no-optional-locks", "-C", str(REPO), "show", f"HEAD:{ruta}"], capture_output=True, check=True).stdout


tramos = json.loads(show(f"{TF}/preregistro/tramos_tanda_final.json"))
tos = {t: "tramo_1" for t in tramos["tramo_1_tos"]} | {t: "tramo_2" for t in tramos["tramo_2_tos"]}
filas = []
for muestra, (rm, rs) in MARCADAS.items():
    datos, sello = show(rm), show(rs).decode("utf-8")
    nombre = rm.rsplit("/", 1)[1]
    linea = [l for l in sello.splitlines() if l.split()[1:2] == [nombre]]
    if len(linea) != 1 or linea[0].split()[0] != hashlib.sha256(datos).hexdigest():
        frenar(f"{nombre} no da el sha256 de su sello")
    for r in csv.DictReader(io.StringIO(datos.decode("utf-8")), delimiter=";"):
        if r["veredicto_autora"].strip() in CON_ERROR:
            to = r["id"].split("::")[0]
            if to not in tos:
                frenar("una unidad sin tramo")
            filas.append([r["id"], r["celda"], tos[to], muestra, r["ficha"], r["nota_autora"]])
if len(filas) != 16:
    frenar(f"las unidades con error son {len(filas)}, no 16")
SAL.mkdir(parents=True)
buf = io.StringIO()
w = csv.writer(buf, delimiter=";", lineterminator="\n")
w.writerow(COLS)
for i, f in enumerate(filas, start=1):
    w.writerow([i] + f + ["", "", "", "", ""])
(SAL / "clasificacion_freno_T4.csv").write_text(buf.getvalue(), encoding="utf-8")
for n in list(SHA_PROPIOS) + [Path(__file__).name]:
    shutil.copy2(AQUI / n, SAL / n)
sha = hashlib.sha256((SAL / "clasificacion_freno_T4.csv").read_bytes()).hexdigest()
(SAL / "planilla_clasificacion_freno_T4.sha256").write_text(f"{sha}  clasificacion_freno_T4.csv\n", encoding="utf-8")
print(f"OK: {SAL.relative_to(REPO)}/clasificacion_freno_T4.csv, {len(filas)} filas, sha256 {sha}")
