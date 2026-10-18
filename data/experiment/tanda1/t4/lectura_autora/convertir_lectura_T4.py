"""Convierte la exportación de Numbers de una planilla de la lectura de T4 (tanda 1, primer tramo) en la planilla marcada que se sella.

Uso, desde esta carpeta: python3 -I convertir_lectura_T4.py <muestra> <exportación.csv>
  <muestra>: cola, aceptadas_items, aceptadas_no_items, vigilancia_2, vigilancia_7, vigilancia_1, vigilancia_3 u observacion_12.

Lee la planilla <muestra>.csv de esta carpeta (controla su sha256) y la exportación (.csv de Numbers, UTF-8 con o sin BOM, separador «;»,
«,» o tabulador). Toma id, celda, ficha, propuesta y justificacion de la planilla, y de la exportación solo veredicto_autora y nota_autora.
No decide ni cambia ninguna marca: solo saca espacios al principio y al final y junta en una línea los saltos de línea y tabuladores dentro
de una celda. Frena sin escribir nada si algo no cierra:
  - la cabecera no es la de la planilla, o hay columnas de más con texto;
  - la cantidad de filas, o el id y la celda de una fila, no son los de la planilla (no se reordena ni se agrega nada);
  - un veredicto_autora vacío o que no es una de las respuestas válidas de la muestra (se escriben tal cual las del LEEME);
  - un veredicto_autora distinto de la propuesta sin la razón en nota_autora.
Si todo pasa, escribe <muestra>_marcada.csv (UTF-8, «;» y «\\n») y no pisa una que ya exista. El sello lo hace la autora (LEEME).
"""
import csv
import hashlib
import io
import re
import sys
from collections import Counter
from pathlib import Path

D = Path(__file__).resolve().parent
SHA_PLANILLAS = {
    "cola": "5f1fefe1887fd999a989a7414790018b6dc3390f3f4c256423cb84cd358f799a",
    "aceptadas_items": "4932f4a80c8ae43d9667d280647e13bbc9f8f174f1d16da356961864d92fe439",
    "aceptadas_no_items": "cc830b718cb13ccb595f95d1b0d0cc229f79802c1600c6f2665255d6ffec1e8a",
    "vigilancia_2": "580e4b047d839b5f6a4528544645fe66b87037b5daee2505fbb2e8d311b55045",
    "vigilancia_7": "b047d9ed7992ebc315eea8e55fe16a85233e8fa38d47cda5a85419649e17d7a1",
    "vigilancia_1": "609577900a2522faf14fe0ba1fc6808ab89e58a352bb49028b2170bbcd52a52b",
    "vigilancia_3": "099ab7e227a93d5ca0075f4e9286ef82139018c9bc74f86edd6e29462e50a3ae",
    "observacion_12": "f4ba30e1831c1221d9f7b40214f01c437590182792ec85e096983853aeaf04a5"
}
CAPAS = ["E0", "E1-prompt", "E1-validador", "catálogo", "E2", "E3", "ensamblado"]
UNIDAD = ["con error", "sin error", "dudosa"]
VALIDAS = {"cola": UNIDAD, "aceptadas_items": UNIDAD, "aceptadas_no_items": UNIDAD,
           "vigilancia_2": ["vaciamiento", "no vaciamiento", "no decidible"],
           "vigilancia_7": ["con apoyo", "sin apoyo", "no decidible"],
           "vigilancia_1": ["sí", "no", "no decidible"],
           "vigilancia_3": ["duplicación", "distintos"],
           "observacion_12": ["correcta", "no decidible"] + [f"incorrecta ({c})" for c in CAPAS]}
COLS = ["id", "celda", "ficha", "propuesta", "justificacion", "veredicto_autora", "nota_autora"]
errores, avisos, arreglos = [], [], []


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def frenar(msg: str) -> None:
    print("FRENO:", msg)
    sys.exit(1)


if len(sys.argv) != 3:
    frenar("uso: python3 -I convertir_lectura_T4.py <muestra> <exportación.csv>")
m = sys.argv[1]
if m not in SHA_PLANILLAS:
    frenar(f"la muestra {m!r} no es una de {list(SHA_PLANILLAS)}")
PLANILLA, SALIDA = D / f"{m}.csv", D / f"{m}_marcada.csv"
EXP = Path(sys.argv[2]).expanduser()
if not EXP.is_absolute():
    EXP = D / EXP
if not PLANILLA.exists():
    frenar(f"no encuentro {PLANILLA.name} en {D}")
if sha(PLANILLA) != SHA_PLANILLAS[m]:
    frenar(f"{PLANILLA.name} no es la del material de T4 (sha256 distinto): no la uses")
if not EXP.exists():
    frenar(f"no existe {EXP}")
if EXP.resolve() in (PLANILLA.resolve(), SALIDA.resolve()):
    frenar("la exportación no puede ser la planilla ni la marcada")
plant = list(csv.reader(io.StringIO(PLANILLA.read_text(encoding="utf-8"), newline=""), delimiter=";"))
if plant[0] != COLS or any(len(r) != 7 for r in plant):
    frenar("la planilla no tiene la forma esperada (7 columnas)")
texto = EXP.read_bytes().decode("utf-8-sig")
primera = texto.splitlines()[0] if texto else ""
sep = max((";", ",", "\t"), key=primera.count)
filas = list(csv.reader(io.StringIO(texto, newline=""), delimiter=sep))
cab = [c.strip() for c in filas[0]] if filas else []
if cab[:7] != COLS:
    frenar(f"la cabecera de la exportación no es la de la planilla: {cab}")
if any(c for c in cab[7:]):
    frenar(f"la exportación tiene columnas de más: {cab[7:]}")
datos = filas[1:]
while datos and not any(c.strip() for c in datos[-1]):
    datos.pop()
    arreglos.append("saqué una fila vacía al final")
if len(datos) != len(plant) - 1:
    frenar(f"la exportación tiene {len(datos)} filas de datos y la planilla {len(plant) - 1}")


def limpiar(v: str, donde: str) -> str:
    w = re.sub(r"[\r\n\t]+", " ", v).strip()
    if w != v.strip():
        arreglos.append(f"{donde}: junté en una línea un salto o un tabulador")
    return w


out = [COLS]
for i, (p, e) in enumerate(zip(plant[1:], datos), start=2):
    e = (e + [""] * 7) if len(e) < 7 else e
    if any(c.strip() for c in e[7:]):
        errores.append(f"fila {i}: hay texto fuera de las 7 columnas")
    if e[0].strip() != p[0] or e[1].strip() != p[1]:
        errores.append(f"fila {i}: id/celda de la exportación ({e[0]!r}, {e[1]!r}) no son los de la planilla ({p[0]!r}, {p[1]!r})")
        continue
    for k in (2, 3, 4):
        if limpiar(e[k], f"fila {i} {COLS[k]}") != p[k]:
            avisos.append(f"fila {i}: la columna {COLS[k]} de la exportación difiere de la planilla (uso la de la planilla)")
    ver, nota = limpiar(e[5], f"fila {i} veredicto_autora"), limpiar(e[6], f"fila {i} nota_autora")
    if not ver:
        errores.append(f"fila {i} ({p[0]}): veredicto_autora vacío")
    elif ver not in VALIDAS[m]:
        errores.append(f"fila {i} ({p[0]}): veredicto_autora {ver!r} no es una de {VALIDAS[m]}")
    elif ver != p[3] and not nota:
        errores.append(f"fila {i} ({p[0]}): el veredicto cambia la propuesta ({p[3]!r} → {ver!r}) y falta la razón en nota_autora")
    out.append(p[:5] + [ver, nota])
if errores:
    print(f"\n{len(errores)} PROBLEMA(S) — no escribí nada. Corregilos en Numbers, exportá de nuevo y volvé a correr:")
    for x in errores:
        print("  -", x)
    sys.exit(1)
if SALIDA.exists():
    frenar(f"{SALIDA.name} ya existe: no la piso. Si es de una corrida vieja, renombrala")
buf = io.StringIO()
csv.writer(buf, delimiter=";", lineterminator="\n").writerows(out)
SALIDA.write_text(buf.getvalue(), encoding="utf-8")
cambian = [r[0] for r in out[1:] if r[5] != r[3]]
print(f"\nOK: {SALIDA.name}, {len(out) - 1} filas, separador de la exportación {sep!r}, sha256 {sha(SALIDA)}")
print("veredictos:", dict(Counter(r[5] for r in out[1:])))
print(f"cambian la propuesta: {len(cambian)}" + (f" ({', '.join(cambian)})" if cambian else ""))
if arreglos:
    print(f"arreglos de forma ({len(arreglos)}):")
    for x in arreglos:
        print("  -", x)
if avisos:
    print(f"avisos ({len(avisos)}):")
    for x in avisos:
        print("  -", x)
