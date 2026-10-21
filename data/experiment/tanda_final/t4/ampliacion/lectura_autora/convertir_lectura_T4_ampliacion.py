"""Convierte la exportación de Numbers de la planilla de la ampliación de T4 (tanda final, segundo tramo: las aceptadas no ítems) en la
planilla marcada que se sella. Es t4/lectura_autora/convertir_lectura_T4.py (el del primer tramo, que no cambia) con la planilla de la
ampliación: el mismo código, salvo el docstring, las planillas que conoce y sus respuestas válidas.

Uso, desde esta carpeta: python3 -I convertir_lectura_T4_ampliacion.py aceptadas_no_items_ampliacion <exportación.csv>

Lee la planilla aceptadas_no_items_ampliacion.csv de esta carpeta (controla su sha256) y la exportación (.csv de Numbers, UTF-8 con o sin
BOM, separador «;», «,» o tabulador). Toma id, celda, ficha, propuesta y justificacion de la planilla, y de la exportación solo
veredicto_autora y nota_autora. No decide ni cambia ninguna marca: solo saca espacios al principio y al final y junta en una línea los
saltos de línea y tabuladores dentro de una celda. Frena sin escribir nada si algo no cierra:
  - la cabecera no es la de la planilla, o hay columnas de más con texto;
  - la cantidad de filas, o el id y la celda de una fila, no son los de la planilla (no se reordena ni se agrega nada);
  - un veredicto_autora vacío o que no es una de las respuestas válidas (se escriben tal cual las del LEEME);
  - un veredicto_autora distinto de la propuesta sin la razón en nota_autora.
Si todo pasa, escribe aceptadas_no_items_ampliacion_marcada.csv (UTF-8, «;» y «\\n») y no pisa una que ya exista. El sello lo hace la
autora (LEEME_lectura_T4_ampliacion.md).
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
    "aceptadas_no_items_ampliacion": "e99eaa2c347fe95a345dc63b26208f8681e28c2daf894e120e947d2855ff2331"
}
CAPAS = ["E0", "E1-prompt", "E1-validador", "catálogo", "E2", "E3", "ensamblado"]
UNIDAD = ["con error", "sin error", "dudosa"]
VALIDAS = {"aceptadas_no_items_ampliacion": UNIDAD}
COLS = ["id", "celda", "ficha", "propuesta", "justificacion", "veredicto_autora", "nota_autora"]
errores, avisos, arreglos = [], [], []


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def frenar(msg: str) -> None:
    print("FRENO:", msg)
    sys.exit(1)


if len(sys.argv) != 3:
    frenar("uso: python3 -I convertir_lectura_T4_ampliacion.py aceptadas_no_items_ampliacion <exportación.csv>")
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
    frenar(f"{PLANILLA.name} no es la de la ampliación de T4 (sha256 distinto): no la uses")
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
