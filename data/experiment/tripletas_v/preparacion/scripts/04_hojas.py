"""
04_hojas.py — U-TRIP-V, paso g: las hojas de lectura de la autora, vacías, en lectura/.

  - el gold (§3.4 y §3.5): hoja_piloto.csv y hoja_lote_01.csv … hoja_lote_09.csv, con las fichas en el orden sellado y,
    por arista, «correcta» (sí, no o no decidible), «importancia» (esencial, útil o accesoria), una nota y la columna
    opcional de observaciones de umbral, sin cifra (enmienda 1, §11, la lectura adosada). En la cabecera, el nombre de
    la hoja, el sha256 del acta y la hora de inicio y la de fin del lote, que la autora completa;
  - el pool (§4.2 y §4.3): hoja_pool.csv con las 20, componente por componente (sujeto, predicado, valores,
    calificadores y modalidad: sostenido, contradicho o no consta), si requiere adjudicación humana y los tres rasgos de
    importancia (conducta exigible, valor o plazo concreto, relación principal de la unidad), sí o no.
El sellado de cada hoja lo hace lectura/sellar_hoja.py. Este script no pisa una hoja que ya exista.
  python3 -I -B 04_hojas.py --acta <acta_sorteo_V.json> --sello <sello_sorteo_V.txt> --salida <lectura/>
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun_v as V  # noqa: E402

COLUMNAS_GOLD = ("orden", "ref", "predicado", "clave", "correcta", "importancia", "nota", "observacion_umbral")
COLUMNAS_POOL = ("orden", "ref", "predicado", "clave", "comp_sujeto", "comp_predicado", "comp_valores",
                 "comp_calificadores", "comp_modalidad", "requiere_adjudicacion", "rasgo_conducta_exigible",
                 "rasgo_valor_concreto", "rasgo_relacion_principal", "nota")


def hoja(nombre: str, s_acta: str, columnas: tuple, filas: list) -> str:
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerows([["hoja", nombre], ["acta_sorteo_V.json_sha256", s_acta], ["hora_inicio", ""], ["hora_fin", ""], [],
                 list(columnas)])
    for i, (ref, pred, k) in enumerate(filas, 1):
        w.writerow([i, ref, pred, k] + [""] * (len(columnas) - 4))
    return buf.getvalue()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--acta", type=Path, required=True)
    ap.add_argument("--sello", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    s_acta = V.sha_archivo(a.acta)
    if a.sello.read_text(encoding="utf-8").split()[0] != s_acta:
        raise SystemExit("el acta no es la de su sello")
    acta = json.loads(a.acta.read_text(encoding="utf-8"))
    pred = {f[0]: f[1] for f in acta["poblacion"]["filas"]}
    refs = {k: f"V{i + 1:03d}" for i, k in enumerate(acta["sorteo"]["orden"])}
    hojas = {f"hoja_{lote}.csv": hoja(lote, s_acta, COLUMNAS_GOLD, [(refs[k], pred[k], k) for k in ks])
             for lote, ks in acta["sorteo"]["lotes"].items()}
    hojas["hoja_pool.csv"] = hoja("pool", s_acta, COLUMNAS_POOL,
                                  [(x["ref"], x["predicado"], x["clave"]) for x in acta["sorteo"]["pool"]])
    a.salida.mkdir(parents=True, exist_ok=True)
    existentes = [n for n in hojas if (a.salida / n).exists()]
    if existentes:
        raise SystemExit(f"ya existen {existentes}: no se pisa una hoja")
    out = {}
    for n, t in hojas.items():
        (a.salida / n).write_text(t, encoding="utf-8")
        out[n] = V.sha_archivo(a.salida / n)
    print(json.dumps({"hora": V.hora(), "hojas_vacias_sha256": out,
                      "sellar_hoja.py_sha256": V.sha_archivo(a.salida / "sellar_hoja.py")}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
