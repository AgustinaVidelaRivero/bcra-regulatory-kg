"""
proyectar_c1.py — U-COMP-E1, C1: re-proyección del gasto total con los tokens reales después de la primera corrida de
cada brazo (decisión 4 del «seguí»). Lee resumen_<etiqueta>.json y presupuesto.json de --salida; escribe
proyeccion_tras_<etiqueta>.json; sale con 3 si la proyección supera el tope (parada ordenada).

Cómo proyecta, con los tokens reales (usage: entrada, cache_read, cache_write, salida) de las corridas hechas:
  - una corrida pendiente del MISMO brazo cuesta lo que costó la hecha (mismos pedidos; la caché de prompts se escribe
    una vez y se lee 86 veces, como en la corrida hecha);
  - tras S1, las dos corridas de O (sin tokens propios todavía) se proyectan con los tokens de S1 a los precios de O:
    la entrada (variable, lectura y escritura de caché) es la misma salvo el tokenizador (C0 midió 1,2695 y 1,2696:
    igual), y la salida de S1 × (1 + 0,5) por el pensamiento con effort low (el supuesto del escenario B de C0, que O1
    después mide);
  - tras O1, O2 = O1.
  PYTHONDONTWRITEBYTECODE=1 <venv>/bin/python -B data/experiment/comp_e1/c1/proyectar_c1.py --salida DIR --tras S1
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun_c1 as C  # noqa: E402

PENSAMIENTO_O = 0.5
ORDEN = ("S1", "S2", "O1", "O2")


def costo(usage: dict, p: dict) -> float:
    return (usage["input_tokens"] * p["in"] + usage["output_tokens"] * p["out"] + usage["cache_write_tokens"] * p["cw"]
            + usage["cache_read_tokens"] * p["cr"]) / 1e6


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path, required=True)
    ap.add_argument("--tras", choices=("S1", "O1"), required=True)
    a = ap.parse_args()
    hechas = {}
    for et in ORDEN:
        p = a.salida / f"resumen_{et}.json"
        if p.exists():
            hechas[et] = json.loads(p.read_text(encoding="utf-8"))
    if a.tras not in hechas:
        raise SystemExit(f"falta resumen_{a.tras}.json")
    pres = json.loads((a.salida / "presupuesto.json").read_text(encoding="utf-8"))
    est_c0 = json.loads(C.ESTIMACION_C0.read_text(encoding="utf-8"))
    # El gasto real de una corrida es el del presupuesto (por corrida): en una reanudación, una unidad vuelta a correr
    # sale de la caché local y su registro vale 0, pero lo pagado ya está en presupuesto.json.
    real = {et: hechas[et]["gasto_usd_presupuesto_corrida"] for et in hechas}
    usage = {et: hechas[et]["usage_total"] for et in hechas}
    proy = {}
    for et in ORDEN:
        b = et[0]
        if et in real:
            proy[et] = {"usd": round(real[et], 4), "fuente": "real"}
        elif f"{b}1" in usage:
            proy[et] = {"usd": round(costo(usage[f"{b}1"], C.PRECIOS[b]), 4), "fuente": f"tokens reales de {b}1 a precios de {b}"}
        elif b == "O" and "S1" in usage:
            u = dict(usage["S1"]); u["output_tokens"] = round(u["output_tokens"] * (1 + PENSAMIENTO_O))
            proy[et] = {"usd": round(costo(u, C.PRECIOS["O"]), 4),
                        "fuente": f"tokens reales de S1 a precios de O, salida × {1 + PENSAMIENTO_O} (pensamiento, supuesto del escenario B de C0)"}
        else:
            proy[et] = {"usd": None, "fuente": "sin base"}
    total = sum(x["usd"] for x in proy.values() if x["usd"] is not None)
    out = {"unidad": "U-COMP-E1, C1", "tras": a.tras, "cuando_utc": C.ahora(), "tope_usd": C.TOPE_USD,
           "gasto_real_presupuesto": pres["gasto_usd"], "por_corrida": proy, "proyeccion_total": round(total, 4),
           "pasa_tope": total > C.TOPE_USD, "estimacion_c0_cuatro_corridas": est_c0["cuatro_corridas"],
           "comparacion_corrida_hecha_vs_c0": {et: {"real": round(real[et], 4),
                                                   "c0_escenario_A": est_c0["por_brazo"][et[0]]["corrida_escenario_A"],
                                                   "c0_escenario_B": est_c0["por_brazo"][et[0]]["corrida_escenario_B"],
                                                   "usage": usage[et]} for et in real}}
    (a.salida / f"proyeccion_tras_{a.tras}.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=1))
    if out["pasa_tope"]:
        print(f"PARADA ORDENADA: la proyección {total:.2f} supera el tope {C.TOPE_USD}", flush=True)
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
