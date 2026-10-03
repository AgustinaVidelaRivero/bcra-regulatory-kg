"""U-MED-R2A, M3 — conteo de las lecturas asistidas (reglas: data/experiment/medicion_r2a/m3/m3_reglas_lectura.md).

Solo lectura. Para cada lectura comprueba que la copia de trabajo (m3/lecturas/) tenga las mismas filas, en el mismo
orden y con las mismas celdas que su planilla (m3/planillas/), más las columnas de lectura; que todo veredicto esté en
la lista de la regla, que toda fila tenga justificación y que `revision_autora` esté vacía. Cuenta los veredictos y
calcula el intervalo de Wilson al 95 % donde la muestra es aleatoria (M3.a y M3.e). Una copia que todavía no existe se
informa como pendiente. Escribe solo --out.

Uso, desde la raíz del repo:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/medicion_r2a/m3_conteo.py \
      --out data/experiment/medicion_r2a/m3/m3_conteo.json
"""
from __future__ import annotations

import argparse
import csv
import json
import math
from collections import Counter, OrderedDict
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
M3 = "data/experiment/medicion_r2a/m3"
LECTURAS = OrderedDict([
    ("m3d", {"planilla": "m3d_plazos_frecuencia", "copia": "m3d_lectura_plazos_frecuencia",
             "veredictos": ("frecuencia", "plazo", "otra"), "extra": ("mixto",), "grupo": "grupo", "wilson": None}),
    ("m3a", {"planilla": "m3a_cambios_destino", "copia": "m3a_lectura_cambios_destino",
             "veredictos": ("sí", "no", "no decidible"), "extra": ("destino_correcto",), "grupo": None, "wilson": "sí"}),
    ("m3a2", {"planilla": "m3a2_perdidas_sin_lectura", "copia": "m3a2_lectura_perdidas_sin_lectura",
              "veredictos": ("pérdida real", "no es pérdida", "no decidible"), "extra": (), "grupo": None, "wilson": None}),
    ("m3b", {"planilla": "m3b_puntos_inexistentes", "copia": "m3b_lectura_puntos_inexistentes",
             "veredictos": ("normativa", "detector", "E0", "no decidible"), "extra": (), "grupo": None, "wilson": None}),
    ("m3c", {"planilla": "m3c_pasada_residual_e4", "copia": "m3c_lectura_pasada_residual_e4",
             "veredictos": ("correcta", "incorrecta", "duda", "sin resolución propuesta"), "extra": (), "grupo": None,
             "wilson": None}),
    ("m3e", {"planilla": "m3e_matriz_no_verificadas", "copia": "m3e_lectura_matriz_no_verificadas",
             "veredictos": ("correcta", "incorrecta", "duda"), "extra": ("mal_tipado",), "grupo": "par",
             "wilson": "correcta"}),
])


def wilson(k: int, n: int, z: float = 1.959963984540054) -> list | None:
    if n == 0:
        return None
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    m = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return [round(c - m, 3), round(c + m, 3)]


def leer_csv(p: Path) -> tuple[list, list]:
    with p.open(encoding="utf-8", newline="") as f:
        r = csv.DictReader(f)
        return list(r.fieldnames), list(r)


def contar(nombre: str, cfg: dict) -> dict:
    pl, cp = RAIZ / M3 / "planillas" / f"{cfg['planilla']}.csv", RAIZ / M3 / "lecturas" / f"{cfg['copia']}.csv"
    if not cp.exists():
        return {"estado": "pendiente", "copia": str(cp.relative_to(RAIZ))}
    cols_p, filas_p = leer_csv(pl)
    cols_c, filas_c = leer_csv(cp)
    esperadas = cols_p + ["veredicto", *cfg["extra"], "justificacion", "revision_autora"]
    assert cols_c == esperadas, (nombre, cols_c, esperadas)
    assert len(filas_p) == len(filas_c), (nombre, len(filas_p), len(filas_c))
    for a, b in zip(filas_p, filas_c):
        assert all(a[k] == b[k] for k in cols_p), (nombre, a.get("id_lectura"))
        assert b["veredicto"] in cfg["veredictos"], (nombre, b.get("id_lectura"), b["veredicto"])
        assert b["justificacion"].strip(), (nombre, b.get("id_lectura"))
        assert b["revision_autora"] == "", (nombre, b.get("id_lectura"))
    out = OrderedDict([("estado", "leida"), ("planilla", str(pl.relative_to(RAIZ))), ("copia", str(cp.relative_to(RAIZ))),
                       ("filas", len(filas_c)),
                       ("veredictos", {v: sum(1 for f in filas_c if f["veredicto"] == v) for v in cfg["veredictos"]})])
    for e in cfg["extra"]:
        out[f"{e}_conteo"] = dict(sorted(Counter(f[e] for f in filas_c if f[e]).items()))
    grupos = [cfg["grupo"]] if cfg["grupo"] else [None]
    if cfg["grupo"]:
        out["por_grupo"] = OrderedDict()
        for g in sorted({f[cfg["grupo"]] for f in filas_c}):
            fs = [f for f in filas_c if f[cfg["grupo"]] == g]
            d = OrderedDict([("filas", len(fs)), ("veredictos", {v: sum(1 for f in fs if f["veredicto"] == v)
                                                                for v in cfg["veredictos"]})])
            if cfg["wilson"]:
                k = d["veredictos"][cfg["wilson"]]
                n_dec = sum(d["veredictos"][v] for v in cfg["veredictos"] if v not in ("duda", "no decidible"))
                d["wilson_95_sobre_decididos"] = {"k": k, "n": n_dec, "intervalo": wilson(k, n_dec)}
                d["wilson_95_sobre_todas"] = {"k": k, "n": len(fs), "intervalo": wilson(k, len(fs))}
            out["por_grupo"][g] = d
    elif cfg["wilson"]:
        k = out["veredictos"][cfg["wilson"]]
        n_dec = sum(out["veredictos"][v] for v in cfg["veredictos"] if v not in ("duda", "no decidible"))
        out["wilson_95_sobre_todas"] = {"k": k, "n": len(filas_c), "intervalo": wilson(k, len(filas_c))}
        out["wilson_95_sobre_decididos"] = {"k": k, "n": n_dec, "intervalo": wilson(k, n_dec)}
    if nombre == "m3d":
        ph = [f for f in filas_c if f["grupo"] == "plazo_heredado"]
        out["plazo_heredado_por_to"] = OrderedDict(
            (to, {v: sum(1 for f in ph if f["to"] == to and f["veredicto"] == v) for v in cfg["veredictos"]})
            for to in sorted({f["to"] for f in ph}))
        out["plazo_heredado_por_lista"] = OrderedDict(
            (l, {v: sum(1 for f in ph if f["en_lista"] == l and f["veredicto"] == v) for v in cfg["veredictos"]})
            for l in ("sí", "no"))
        out["plazo_heredado_valores_distintos_por_veredicto"] = {
            v: len({f["valor_leido"] for f in ph if f["veredicto"] == v}) for v in cfg["veredictos"]}
    out["no_y_dudosas"] = [{k: f.get(k) for k in ("id_lectura", "veredicto", *cfg["extra"], "justificacion")}
                           for f in filas_c if f["veredicto"] in ("no", "incorrecta", "no decidible", "duda",
                                                                   "pérdida real", "detector", "E0")]
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    res = OrderedDict((n, contar(n, c)) for n, c in LECTURAS.items())
    (RAIZ / a.out).write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for n, r in res.items():
        print(n, r["estado"], r.get("filas"), r.get("veredictos"))


if __name__ == "__main__":
    main()
