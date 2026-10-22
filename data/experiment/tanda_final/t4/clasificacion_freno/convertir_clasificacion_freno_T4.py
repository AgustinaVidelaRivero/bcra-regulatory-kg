"""Convierte la exportación de Numbers de la planilla de la clasificación del freno de T4 (tanda final) en la planilla marcada que se
sella (mesa, 22/10/2026, §236). Es el convertidor de la ampliación de T4 (`t4/ampliacion/lectura_autora/convertir_lectura_T4_ampliacion.py`)
con esta planilla: sus columnas y sus respuestas válidas.

Uso, desde esta carpeta: python3 -I convertir_clasificacion_freno_T4.py <exportación.csv>

Lee la planilla clasificacion_freno_T4.csv de esta carpeta (controla su sha256 contra planilla_clasificacion_freno_T4.sha256) y la
exportación (.csv de Numbers, UTF-8 con o sin BOM, separador «;», «,» o tabulador). Toma n, id, celda, tramo, muestra, ficha y
nota_de_la_lectura de la planilla, y de la exportación solo capa, falla_de_esquema, campo, se_repite y nota_clasificacion. No decide ni
cambia ninguna marca: saca espacios al principio y al final, junta en una línea los saltos y tabuladores de una celda, y escribe «sí» donde
dice «si» (lo informa). Frena sin escribir nada si algo no cierra:
  - la cabecera no es la de la planilla, o hay columnas de más con texto;
  - la cantidad de filas, o el n, el id y la celda de una fila, no son los de la planilla;
  - capa, falla_de_esquema, campo o se_repite vacíos o fuera de sus respuestas válidas (capa y campo admiten dos o más, unidas con «+»);
  - falla_de_esquema «sí» o «no_se» sin la razón en nota_clasificacion.
Si todo pasa, escribe clasificacion_freno_T4_marcada.csv (UTF-8, «;» y «\\n») y no pisa una que ya exista. El sello lo hace la autora
(LEEME_clasificacion_freno_T4.md).
"""
import csv
import hashlib
import io
import re
import sys
from collections import Counter
from pathlib import Path

D = Path(__file__).resolve().parent
PLANILLA, SALIDA = D / "clasificacion_freno_T4.csv", D / "clasificacion_freno_T4_marcada.csv"
SHA = D / "planilla_clasificacion_freno_T4.sha256"
FIJAS = ["n", "id", "celda", "tramo", "muestra", "ficha", "nota_de_la_lectura"]
LLENAS = ["capa", "falla_de_esquema", "campo", "se_repite", "nota_clasificacion"]
COLS = FIJAS + LLENAS
CAPAS = ["E0", "E1-prompt", "E1-validador", "catálogo", "E2", "E3", "ensamblado", "no_se"]
CAMPOS = ["sujeto", "relacion", "valor", "calificador", "modalidad", "tipo_de_nodo", "otro"]
ESQUEMA = ["sí", "no", "no_se"]
REPITE = ["sí", "no"]
errores, avisos, arreglos = [], [], []


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def frenar(msg: str) -> None:
    print("FRENO:", msg)
    sys.exit(1)


if len(sys.argv) != 2:
    frenar("uso: python3 -I convertir_clasificacion_freno_T4.py <exportación.csv>")
EXP = Path(sys.argv[1]).expanduser()
if not EXP.is_absolute():
    EXP = D / EXP
for p in (PLANILLA, SHA):
    if not p.exists():
        frenar(f"no encuentro {p.name} en {D}")
if SHA.read_text(encoding="utf-8").split()[:2] != [sha(PLANILLA), PLANILLA.name]:
    frenar(f"{PLANILLA.name} no da el sha256 de {SHA.name}: no la uses")
if not EXP.exists():
    frenar(f"no existe {EXP}")
if EXP.resolve() in (PLANILLA.resolve(), SALIDA.resolve()):
    frenar("la exportación no puede ser la planilla ni la marcada")
plant = list(csv.reader(io.StringIO(PLANILLA.read_text(encoding="utf-8"), newline=""), delimiter=";"))
if plant[0] != COLS or any(len(r) != len(COLS) for r in plant):
    frenar(f"la planilla no tiene la forma esperada ({len(COLS)} columnas)")
texto = EXP.read_bytes().decode("utf-8-sig")
primera = texto.splitlines()[0] if texto else ""
sep = max((";", ",", "\t"), key=primera.count)
filas = list(csv.reader(io.StringIO(texto, newline=""), delimiter=sep))
cab = [c.strip() for c in filas[0]] if filas else []
if cab[:len(COLS)] != COLS:
    frenar(f"la cabecera de la exportación no es la de la planilla: {cab}")
if any(c for c in cab[len(COLS):]):
    frenar(f"la exportación tiene columnas de más: {cab[len(COLS):]}")
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


def si(v: str, donde: str) -> str:
    if v == "si":
        arreglos.append(f"{donde}: escribí «sí» donde decía «si»")
        return "sí"
    return v


def varias(v: str, validas: list, donde: str) -> bool:
    partes = [x.strip() for x in v.split("+")]
    if not v or any(x not in validas for x in partes) or len(set(partes)) != len(partes):
        errores.append(f"{donde}: {v!r} no es una de {validas} (o varias, unidas con «+», sin repetir)")
        return False
    return True


n = len(COLS)
out = [COLS]
for i, (p, e) in enumerate(zip(plant[1:], datos), start=2):
    e = (e + [""] * n) if len(e) < n else e
    if any(c.strip() for c in e[n:]):
        errores.append(f"fila {i}: hay texto fuera de las {n} columnas")
    if [e[k].strip() for k in (0, 1, 2)] != p[:3]:
        errores.append(f"fila {i}: n/id/celda de la exportación no son los de la planilla (no se reordena ni se agrega nada)")
        continue
    for k in range(3, len(FIJAS)):
        if limpiar(e[k], f"fila {i} {COLS[k]}") != p[k]:
            avisos.append(f"fila {i}: la columna {COLS[k]} de la exportación difiere de la planilla (uso la de la planilla)")
    capa = limpiar(e[7], f"fila {i} capa")
    esq = si(limpiar(e[8], f"fila {i} falla_de_esquema"), f"fila {i} falla_de_esquema")
    campo = limpiar(e[9], f"fila {i} campo")
    rep = si(limpiar(e[10], f"fila {i} se_repite"), f"fila {i} se_repite")
    nota = limpiar(e[11], f"fila {i} nota_clasificacion")
    varias(capa, CAPAS, f"fila {i} capa")
    varias(campo, CAMPOS, f"fila {i} campo")
    if esq not in ESQUEMA:
        errores.append(f"fila {i}: falla_de_esquema {esq!r} no es una de {ESQUEMA}")
    elif esq != "no" and not nota:
        errores.append(f"fila {i}: falla_de_esquema {esq!r} sin la razón en nota_clasificacion")
    if rep not in REPITE:
        errores.append(f"fila {i}: se_repite {rep!r} no es una de {REPITE}")
    out.append(p[:len(FIJAS)] + [capa, esq, campo, rep, nota])
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
c_esq = Counter(r[8] for r in out[1:])
print(f"\nOK: {SALIDA.name}, {len(out) - 1} filas, separador de la exportación {sep!r}, sha256 {sha(SALIDA)}")
print("capa:", dict(Counter(x for r in out[1:] for x in r[7].split("+"))))
print("falla de esquema:", dict(c_esq))
print("lo que sigue:", "lo ven antes de seguir (hay «sí» o «no_se»)" if c_esq["sí"] or c_esq["no_se"] else
      "sin falla de esquema: el freno se acepta y se declara como residuo")
for t, lista in (("arreglos de forma", arreglos), ("avisos", avisos)):
    if lista:
        print(f"{t} ({len(lista)}):")
        for x in lista:
            print("  -", x)
