"""
sellar_hoja.py — U-TRIP-V: el sello de una hoja de lectura de la autora (el gold de un lote o el pool), al terminarla.

Controla, sin cambiar la hoja:
  - la cabecera: el nombre de la hoja es el del archivo, el sha256 del acta es el del sello del sorteo, y la hora de
    inicio y la de fin están puestas (AAAA-MM-DD HH:MM, con o sin segundos) y la de fin no es anterior a la de inicio;
  - las filas: son las del lote sellado en el acta, en su orden (orden, ref, predicado y clave);
  - cada fila tiene un valor permitido en cada columna obligatoria (mayúsculas y tildes no importan; «no_decidible» vale
    por «no decidible»). La nota y la observación de umbral son libres y opcionales.
Si todo pasa, escribe al lado de la hoja `sello_<hoja>.txt` con el sha256 de la hoja, su nombre y la hora (el formato del
sello de los calibradores de U-MED-DESAMB). No pisa un sello existente. Si algo falla, lo lista y no sella.

Uso (desde cualquier carpeta):
  python3 sellar_hoja.py hoja_piloto.csv
  python3 sellar_hoja.py hoja_pool.csv [--acta ../salidas/acta_sorteo_V.json --sello-acta ../salidas/sello_sorteo_V.txt]
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import sys
import time
import unicodedata
from datetime import datetime
from pathlib import Path

AQUI = Path(__file__).resolve().parent
COLUMNAS_GOLD = ("orden", "ref", "predicado", "clave", "correcta", "importancia", "nota", "observacion_umbral")
COLUMNAS_POOL = ("orden", "ref", "predicado", "clave", "comp_sujeto", "comp_predicado", "comp_valores",
                 "comp_calificadores", "comp_modalidad", "requiere_adjudicacion", "rasgo_conducta_exigible",
                 "rasgo_valor_concreto", "rasgo_relacion_principal", "nota")
COMPONENTE = {"sostenido", "contradicho", "no consta"}
SI_NO = {"si", "no"}
PERMITIDOS_GOLD = {"correcta": {"si", "no", "no decidible"}, "importancia": {"esencial", "util", "accesoria"}}
PERMITIDOS_POOL = {"comp_sujeto": COMPONENTE, "comp_predicado": COMPONENTE, "comp_valores": COMPONENTE,
                   "comp_calificadores": COMPONENTE, "comp_modalidad": COMPONENTE, "requiere_adjudicacion": SI_NO,
                   "rasgo_conducta_exigible": SI_NO, "rasgo_valor_concreto": SI_NO, "rasgo_relacion_principal": SI_NO}
CABECERA = ("hoja", "acta_sorteo_V.json_sha256", "hora_inicio", "hora_fin")


def plegar(s: str) -> str:
    s = unicodedata.normalize("NFD", (s or "").strip().lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return " ".join(s.replace("_", " ").split())


def leer_hora(s: str):
    for fmt in ("%Y-%m-%d %H:%M", "%Y-%m-%d %H:%M:%S"):
        try:
            return datetime.strptime(s.strip(), fmt)
        except ValueError:
            pass
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("hoja", type=Path)
    ap.add_argument("--acta", type=Path, default=AQUI.parent / "salidas" / "acta_sorteo_V.json")
    ap.add_argument("--sello-acta", type=Path, default=AQUI.parent / "salidas" / "sello_sorteo_V.txt")
    a = ap.parse_args()

    errores = []
    datos = a.hoja.read_bytes()
    texto = datos.decode("utf-8-sig")
    primera = texto.splitlines()[0] if texto else ""
    delim = ";" if primera.count(";") > primera.count(",") else ","
    filas = [[c.strip() for c in f] for f in csv.reader(io.StringIO(texto), delimiter=delim)]
    filas = [f for f in filas if any(f)]

    acta_bytes = a.acta.read_bytes()
    s_acta = hashlib.sha256(acta_bytes).hexdigest()
    if a.sello_acta.read_text(encoding="utf-8").split()[0] != s_acta:
        raise SystemExit(f"el acta da {s_acta} y no es la de su sello: no se sella nada")
    acta = json.loads(acta_bytes.decode("utf-8"))

    cab = {f[0]: (f[1] if len(f) > 1 else "") for f in filas[:4]}
    if tuple(cab) != CABECERA:
        errores.append(f"cabecera: se esperaban las filas {CABECERA}, hay {tuple(cab)}")
    nombre = a.hoja.stem.removeprefix("hoja_")
    if cab.get("hoja") != nombre:
        errores.append(f"cabecera: la hoja dice «{cab.get('hoja')}» y el archivo es de «{nombre}»")
    if cab.get("acta_sorteo_V.json_sha256") != s_acta:
        errores.append("cabecera: el sha256 del acta no es el del sello del sorteo")
    hi, hf = leer_hora(cab.get("hora_inicio", "")), leer_hora(cab.get("hora_fin", ""))
    if hi is None:
        errores.append("cabecera: falta la hora de inicio, o no es AAAA-MM-DD HH:MM")
    if hf is None:
        errores.append("cabecera: falta la hora de fin, o no es AAAA-MM-DD HH:MM")
    if hi and hf and hf < hi:
        errores.append("cabecera: la hora de fin es anterior a la de inicio")

    es_pool = nombre == "pool"
    columnas, permitidos = (COLUMNAS_POOL, PERMITIDOS_POOL) if es_pool else (COLUMNAS_GOLD, PERMITIDOS_GOLD)
    tabla = filas[4:]
    if not tabla or tuple(tabla[0][:len(columnas)]) != columnas:
        errores.append(f"tabla: el encabezado no es {columnas}")
        tabla = [columnas]
    if es_pool:
        esperado = [(x["ref"], x["predicado"], x["clave"]) for x in acta["sorteo"]["pool"]]
    elif nombre in acta["sorteo"]["lotes"]:
        refs = {k: f"V{i + 1:03d}" for i, k in enumerate(acta["sorteo"]["orden"])}
        pred = {f[0]: f[1] for f in acta["poblacion"]["filas"]}
        esperado = [(refs[k], pred[k], k) for k in acta["sorteo"]["lotes"][nombre]]
    else:
        raise SystemExit(f"«{nombre}» no es un lote del acta ni el pool")
    cuerpo = [dict(zip(columnas, f + [""] * (len(columnas) - len(f)))) for f in tabla[1:]]
    if len(cuerpo) != len(esperado):
        errores.append(f"tabla: {len(cuerpo)} filas y el lote sellado tiene {len(esperado)}")
    for i, (r, e) in enumerate(zip(cuerpo, esperado), 1):
        if (r["orden"], r["ref"], r["predicado"], r["clave"]) != (str(i), *e):
            errores.append(f"fila {i}: orden, ref, predicado o clave no son los del lote sellado ({e[0]})")
        for col, ok in permitidos.items():
            if plegar(r[col]) not in ok:
                errores.append(f"fila {i} ({r['ref']}): «{col}» = «{r[col]}» no es uno de {sorted(ok)}")

    if errores:
        print(f"NO SE SELLA {a.hoja.name}: {len(errores)} problema(s)")
        for e in errores:
            print(" -", e)
        return 1
    sello = a.hoja.parent / f"sello_{a.hoja.stem}.txt"
    if sello.exists():
        raise SystemExit(f"{sello.name} ya existe: no se pisa un sello")
    s_hoja = hashlib.sha256(datos).hexdigest()
    hora = time.strftime("%Y-%m-%d %H:%M:%S %z")
    sello.write_text(f"{s_hoja}  {a.hoja.name}\n{hora}\n", encoding="utf-8")
    print(f"SELLADA {a.hoja.name}: {len(cuerpo)} filas, sha256 {s_hoja}, {hora} -> {sello.name}")
    return 0


if __name__ == "__main__":
    sys.dont_write_bytecode = True
    raise SystemExit(main())
