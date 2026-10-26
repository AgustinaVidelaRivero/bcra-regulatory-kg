"""sellar_planilla_adjudicacion_a2_2.py — el sello de tu planilla de adjudicación de A2.2 (mesa, §277).

Corre en esta carpeta, sin argumentos. Controla, sin cambiar la planilla, que las columnas, los renglones y su orden sean los de la
planilla que armó la mesa (`estructura_planilla.json`), y que cada criterio tenga su veredicto, cumplido o no_cumplido (mayúsculas y
tildes no importan). La observación es libre. Si todo pasa, escribe `sello_adjudicacion_a2_2.txt` con el sha256, los bytes y la hora de
la planilla y la hora del sello. No pisa un sello que ya existe. Si algo falla, lo lista y no sella. Acepta «,» o «;» y el BOM.
  python3 sellar_planilla_adjudicacion_a2_2.py
"""
import csv
import hashlib
import io
import json
import sys
import time
import unicodedata
from pathlib import Path

AQUI = Path(__file__).resolve().parent
PL = AQUI / "planilla_adjudicacion_a2_2.csv"
SELLO = AQUI / "sello_adjudicacion_a2_2.txt"


def plegar(s):
    s = unicodedata.normalize("NFD", (s or "").strip().lower())
    return " ".join("".join(c for c in s if unicodedata.category(c) != "Mn").replace("_", " ").split())


def leer(p):
    t = p.read_bytes().decode("utf-8-sig")
    pr = t.splitlines()[0] if t else ""
    d = ";" if pr.count(";") > pr.count(",") else ","
    filas = [f for f in csv.reader(io.StringIO(t), delimiter=d) if any(x.strip() for x in f)]
    return [c.strip() for c in filas[0]], [[c.strip() for c in f] for f in filas[1:]]


def main():
    if SELLO.exists():
        raise SystemExit(f"{SELLO.name} ya existe: no se pisa un sello")
    est = json.loads((AQUI / "estructura_planilla.json").read_text(encoding="utf-8"))
    cols, filas = leer(PL)
    errores = []
    if cols != est["columnas"]:
        errores.append("las columnas no son las de la planilla de la mesa")
    elif [f[:2] for f in filas] != est["renglones"]:
        errores.append("los renglones no son los de la planilla de la mesa, en su orden")
    else:
        for f in filas:
            r = dict(zip(cols, f + [""] * (len(cols) - len(f))))
            if plegar(r[cols[2]]) not in ("cumplido", "no cumplido"):
                errores.append(f"{r['ficha']}, criterio {r['criterio']}: el veredicto no es cumplido ni no_cumplido")
    if errores:
        print(f"NO SE SELLA: {len(errores)} problema(s)")
        for e in errores:
            print(" -", e)
        return 1
    hora = time.strftime("%Y-%m-%d %H:%M:%S %z")
    b = PL.read_bytes()
    SELLO.write_text("# sello de la adjudicación de A2.2 de la autora: sha256, bytes, hora de modificación y nombre\n"
                     f"# sellado: {hora}\n{hashlib.sha256(b).hexdigest()}  {len(b)}  "
                     f"{time.strftime('%Y-%m-%d %H:%M:%S %z', time.localtime(PL.stat().st_mtime))}  {PL.name}\n", encoding="utf-8")
    print(f"SELLADA la planilla -> {SELLO.name}, {hora}")
    return 0


if __name__ == "__main__":
    sys.dont_write_bytecode = True
    raise SystemExit(main())
