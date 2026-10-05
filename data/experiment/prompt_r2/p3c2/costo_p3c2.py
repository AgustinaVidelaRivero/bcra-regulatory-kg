"""
costo_p3c2.py — U-PROMPT-R2, P3c-2 (USD 0): la proyección de costo con el prefijo final, re-congelado en P3c-2.

El prefijo se toma MEDIDO: los tokens de escritura de caché de la primera llamada real de P3c-2 (la del tercer escalón,
`llamada_escalon3_p3c2.json`), en lugar de la estimación por caracteres de P3c-1 (`p3c/proyeccion_p4b_p3c.py`). Lo
demás, como en P3c-1:
  - U-REEXT-T0 (2.434 unidades), lo que cambia con P3c sin la salida: lecturas y escrituras de caché del prefijo más
    largo y la línea de alcance nueva (calibración del mensaje de P1); más el tercer escalón, con los casos de
    `p3c/salida/escalon3_p3c.json`;
  - P4b: los dos brazos sobre las 29 unidades del diseño (p3c/diseno_p3c.md, §8), con las tarifas por llamada de P4,
    más la pata de E3 en 6 unidades. Escenario alto: salida y E3 por 1,5.
Escribe solo en --salida (costo_p3c2.json). Uso (desde la raíz de una copia):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p3c2/costo_p3c2.py --llamada L --salida DIR
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
P3C = AQUI.parent / "p3c"
sys.path.insert(0, str(P3C))
import mensaje_p3c_borrador as M  # noqa: E402  (los textos de la línea de alcance)

E1 = {"in": 1.00, "out": 5.00, "cw": 1.25, "cr": 0.10}          # claude-haiku-4-5, USD por MTok
N_T0 = 2434
GRUPOS = {"a": 4, "b1_items": 3, "b2_items": 3, "b_encabezados": 4, "c": 4, "d": 4, "e": 4, "ejemplo": 2, "f": 1}
PATA_E3 = 6
TOPE_P4B = 1.5


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--llamada", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    sal = a.salida.resolve()
    if REPO in sal.parents or sal == REPO:
        raise SystemExit("--salida no puede estar dentro del repo")
    g = json.loads((AQUI.parent / "p4" / "salida" / "gasto_p4.json").read_text(encoding="utf-8"))
    ll = json.loads(a.llamada.read_text(encoding="utf-8"))
    cal = json.loads((AQUI.parent / "p1" / "salida" / "censo_p1.json").read_text(encoding="utf-8"))["calibracion"]["mensaje"]
    msg = json.loads((P3C / "salida" / "mensaje_p3c.json").read_text(encoding="utf-8"))
    e3c = json.loads((P3C / "salida" / "escalon3_p3c.json").read_text(encoding="utf-8"))
    cs = g["e1_nuevo"]["cache_stats"]
    n4 = g["e1_nuevo"]["llamadas"]
    t_in, t_out = cs["tokens_in"] / n4, cs["tokens_out"] / n4
    pref_vig = cs["cache_write"]
    pref_p3c = ll["llamada_1_transmision"]["usage"]["cache_creation_input_tokens"]
    d_pref = pref_p3c - pref_vig
    d_car = len(M.ALCANCE_NUEVO.format(sug="")) - len(M.ALCANCE_VIEJO.format(sug=""))
    u_alc = msg["e_linea_alcance"]["cambia_mensaje_e1"]
    t0 = {"prefijo_tokens_p3b2_medido_en_p4": pref_vig, "prefijo_tokens_p3c_medido_en_p3c2": pref_p3c,
          "delta_prefijo_tokens": d_pref,
          "delta_lecturas_de_cache_usd": round((N_T0 - 5) * d_pref * E1["cr"] / 1e6, 4),
          "delta_escrituras_de_cache_usd": round(5 * d_pref * E1["cw"] / 1e6, 4),
          "delta_linea_alcance_usd": round(u_alc * d_car * cal["tokens_por_caracter"] * E1["in"] / 1e6, 4)}
    t0["delta_sin_salida_usd"] = round(t0["delta_lecturas_de_cache_usd"] + t0["delta_escrituras_de_cache_usd"]
                                       + t0["delta_linea_alcance_usd"], 4)
    t0["tercer_escalon_usd"] = {k: {"sin_ratchet": v["total_sin_ratchet_usd"], "con_ratchet": v["total_con_ratchet_usd"],
                                    "casos": v["n"]} for k, v in e3c["por_razon"].items()}
    t0["nota"] = ("el efecto sobre la salida de E1 (y con ella E3) lo mide P4b; el tercer escalón, con el prefijo "
                  "estimado en P3c-1 (la diferencia con el medido es menor que un centavo por caso)")
    n = sum(GRUPOS.values())

    def brazo(pref: int, k_out: float) -> float:
        return (pref * E1["cw"] + (n - 1) * pref * E1["cr"] + n * t_in * E1["in"] + n * t_out * k_out * E1["out"]) / 1e6

    e3_llamada = g["pata_e3"]["e3"]["gasto_usd_real"] / g["pata_e3"]["e3"]["llamadas"]
    e3_reint = g["pata_e3"]["e1_reintentos"]["gasto_usd_real"]
    esc = {}
    for nombre, k in (("central", 1.0), ("alto", 1.5)):
        bv, bp = brazo(pref_vig, k), brazo(pref_p3c, k)
        e3 = PATA_E3 * e3_llamada * k + e3_reint * k
        esc[nombre] = {"brazo_vigente_usd": round(bv, 4), "brazo_p3c_usd": round(bp, 4), "pata_e3_usd": round(e3, 4),
                       "total_usd": round(bv + bp + e3, 4)}
    out = {"comando": "data/experiment/prompt_r2/p3c2/costo_p3c2.py --llamada L --salida DIR",
           "u_reext_t0": t0,
           "p4b": {"grupos": GRUPOS, "unidades": n, "llamadas_e1": 2 * n, "pata_e3_unidades": PATA_E3,
                   "escenarios": esc, "tope_usd": TOPE_P4B}}
    sal.mkdir(parents=True, exist_ok=True)
    (sal / "costo_p3c2.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
