"""Convierte las exportaciones de Numbers de la lectura de U-MED-DESAMB (hoja_clases y censo_c1) a las marcadas que se sellan.

Las plantillas se leen del paquete de la mesa (decisiones_140_mesa/lectura/), controladas por sha256. Toma de la plantilla las columnas
fijas y de la exportación solo las de la autora (clase y nota; decision y nota). No decide ninguna marca: saca espacios, junta en una
línea los saltos de línea y escribe la forma canónica de los códigos («genérica» → generica, «no decidible» → no_decidible,
«une bien» → une_bien), y lista cada arreglo. Frena si algo no cierra y entonces no escribe nada.
Uso, desde la carpeta de la lectura: python3 -I convertir_desamb.py [hoja_exportada.csv] [censo_exportado.csv]
"""
import csv, hashlib, io, re, sys, unicodedata
from collections import Counter
from pathlib import Path

D = Path.cwd()
PKG = Path.home() / "INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/d0348a29-aaa4-4292-82f3-0c0149e3787e/scratchpad/hoja_de_ruta_tanda1_mesa/decisiones_140_mesa/lectura"
PL_HOJA, SHA_HOJA = PKG / "hoja_clases.csv", "ba317008b7a21bbe361bc33923790745145a534abb114e9b36a7f422ac16f2d7"
PL_CENSO, SHA_CENSO = PKG / "censo_c1.csv", "08eda995f0de732b8b69225ffd1ed5eb1cb51cc1b139d2560a9bec2ccc22cd44"
SALTEO = {"D001", "D002", "D004", "D017", "D023", "D026", "D030", "D031", "D046", "D047", "D056", "D064"}
CLASES = {"correcta", "generica", "incorrecta", "no_decidible"}
DECIS = {"une_bien", "une_mal"}
errores, arreglos = [], []

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def frenar(m): print("FRENO:", m); sys.exit(1)
def leer(p, delim=None):
    t = p.read_bytes().decode("utf-8-sig")
    if delim is None:
        prim = t.splitlines()[0] if t else ""
        delim = max(("\t", ";", ","), key=prim.count)
    return list(csv.reader(io.StringIO(t, newline=""), delimiter=delim)), delim
def limpiar(v, donde):
    w = re.sub(r"[\r\n\t]+", " ", v).strip()
    if w != v.strip(): arreglos.append(f"{donde}: junté en una línea un salto o tabulador")
    return w
def canon(v, validos, donde):
    if v in validos: return v
    s = unicodedata.normalize("NFKD", v).encode("ascii", "ignore").decode().lower().strip()
    s = re.sub(r"[\s\-]+", "_", s)
    if s in validos:
        arreglos.append(f"{donde}: escribí {v!r} como {s!r}"); return s
    return None

for p, h in ((PL_HOJA, SHA_HOJA), (PL_CENSO, SHA_CENSO)):
    if not p.exists(): frenar(f"no encuentro la plantilla {p}")
    if sha(p) != h: frenar(f"la plantilla {p.name} del paquete no es la sellada")

exp_h = D / (sys.argv[1] if len(sys.argv) > 1 else "hoja_clases_exportada.csv")
exp_c = D / (sys.argv[2] if len(sys.argv) > 2 else "censo_c1_exportado.csv")
if not exp_h.exists() or not exp_c.exists():
    print(f"FRENO: no encuentro {exp_h.name if not exp_h.exists() else ''} {exp_c.name if not exp_c.exists() else ''}".strip())
    print("Los .csv de esta carpeta (los iguales a una plantilla vacía están marcados):")
    for c in sorted(D.glob("*.csv")):
        s = sha(c); marca = " (= plantilla vacía)" if s in (SHA_HOJA, SHA_CENSO) else ""
        print(f"  {c.name}{marca}")
    print("Pasá los nombres: python3 -I convertir_desamb.py <hoja_exportada.csv> <censo_exportado.csv>")
    sys.exit(1)
for e in (exp_h, exp_c):
    if sha(e) in (SHA_HOJA, SHA_CENSO): frenar(f"{e.name} es igual a la plantilla vacía: exportaste antes de marcar, o elegiste el archivo equivocado")

# hoja_clases
pl, _ = leer(PL_HOJA, ",")
ex, sep_h = leer(exp_h)
CAB = ["item", "letra", "entrada_id", "etiqueta", "clase", "nota"]
if pl[0] != CAB or len(pl) != 92: frenar("la plantilla de la hoja no tiene la forma esperada")
if [c.strip() for c in ex[0][:6]] != CAB: frenar(f"la cabecera de {exp_h.name} no es la de la hoja: {ex[0]}")
datos = ex[1:]
while datos and not any(c.strip() for c in datos[-1]): datos.pop(); arreglos.append("hoja: saqué una fila vacía al final")
if len(datos) != 91: frenar(f"{exp_h.name} tiene {len(datos)} filas de datos, no 91")
out_h = [CAB]
for i, (p, e) in enumerate(zip(pl[1:], datos), start=2):
    e = (e + [""] * 6)[:max(6, len(e))]
    if any(c.strip() for c in e[6:]): errores.append(f"fila {i}: hay texto fuera de las 6 columnas")
    if [x.strip() for x in e[:3]] != p[:3]:
        errores.append(f"fila {i}: item/letra/entrada ({e[0]}, {e[1]}, {e[2]}) no son los de la plantilla ({p[0]}, {p[1]}, {p[2]})"); continue
    clase = limpiar(e[4], f"{p[0]}{p[1]} clase"); nota = limpiar(e[5], f"{p[0]}{p[1]} nota")
    if p[0] in SALTEO:
        if clase or nota: errores.append(f"{p[0]}{p[1]}: es un calibrador y tiene que quedar vacío (tiene {clase!r} / {nota!r})")
        out_h.append(p[:4] + ["", ""]); continue
    c = canon(clase, CLASES, f"{p[0]}{p[1]}") if clase else None
    if c is None: errores.append(f"{p[0]}{p[1]}: clase {clase!r} no es una de {sorted(CLASES)}"); continue
    out_h.append(p[:4] + [c, nota])

# censo_c1
plc, _ = leer(PL_CENSO, ",")
exc, sep_c = leer(exp_c)
CABC = ["colision", "codigo_normalizado", "nodos", "decision", "nota"]
if plc[0] != CABC or len(plc) != 3: frenar("la plantilla del censo no tiene la forma esperada")
if [c.strip() for c in exc[0][:5]] != CABC: frenar(f"la cabecera de {exp_c.name} no es la del censo: {exc[0]}")
datc = exc[1:]
while datc and not any(c.strip() for c in datc[-1]): datc.pop(); arreglos.append("censo: saqué una fila vacía al final")
if len(datc) != 2: frenar(f"{exp_c.name} tiene {len(datc)} filas de datos, no 2")
out_c = [CABC]
for p, e in zip(plc[1:], datc):
    e = (e + [""] * 5)[:max(5, len(e))]
    if e[0].strip() != p[0]: errores.append(f"censo: la fila {e[0]!r} no es la {p[0]!r}"); continue
    dec = limpiar(e[3], f"{p[0]} decision"); nota = limpiar(e[4], f"{p[0]} nota")
    c = canon(dec, DECIS, p[0]) if dec else None
    if c is None: errores.append(f"{p[0]}: decision {dec!r} no es una de {sorted(DECIS)}"); continue
    out_c.append(p[:3] + [c, nota])

if errores:
    print(f"{len(errores)} PROBLEMA(S) — no escribí nada. Corregilos en Numbers, exportá de nuevo y volvé a correr:")
    for x in errores: print("  -", x)
    sys.exit(1)
SH, SC = D / "hoja_clases_marcada.csv", D / "censo_c1_marcado.csv"
for s in (SH, SC):
    if s.exists(): frenar(f"{s.name} ya existe: no la piso. Si es de una corrida vieja, renombrala")
for s, rows in ((SH, out_h), (SC, out_c)):
    b = io.StringIO(); csv.writer(b, lineterminator="\n").writerows(rows); s.write_text(b.getvalue(), encoding="utf-8")
cnt = Counter(r[4] for r in out_h[1:] if r[0] not in SALTEO)
print(f"OK: {SH.name} (sha256 {sha(SH)}) y {SC.name} (sha256 {sha(SC)})")
print(f"separadores de las exportaciones: hoja {sep_h!r}, censo {sep_c!r}")
print(f"hoja: {sum(cnt.values())} entradas clasificadas de 78; 13 de calibradores vacías; con nota: {sum(1 for r in out_h[1:] if r[0] not in SALTEO and r[5])}")
print(f"censo: {sum(1 for r in out_c[1:] if r[3])} de 2 colisiones con decisión")
if arreglos:
    print(f"arreglos de forma: {len(arreglos)} (los primeros 10):")
    for x in arreglos[:10]: print("  -", x)
