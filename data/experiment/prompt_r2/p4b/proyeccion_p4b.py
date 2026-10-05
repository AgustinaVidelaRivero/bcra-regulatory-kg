"""
proyeccion_p4b.py — U-PROMPT-R2, P4b (USD 0, sin API): la proyección de costo antes de correr, con la fórmula de
caching (decisión 2) y las tarifas de claude-haiku-4-5 y claude-sonnet-5.

  - E1, por brazo y unidad: la entrada sin caché, con la calibración del mensaje de P1 (`p1/salida/censo_p1.json`,
    `calibracion.mensaje`: a + tokens por carácter) sobre los caracteres del mensaje de usuario que arma el perfil de
    cada release (`claves_antes_<brazo>.json`); la salida, con la recta de P4 (brazo nuevo, 76 unidades:
    `p4/salida/analisis_p4.json`) sobre los caracteres del texto propio; el prefijo, medido: 26.309 tokens el de
    `3817de475c93` (escritura de caché de P4, `p4/salida/gasto_p4.json`) y 27.840 el de `322c5a23e9b7` (llamada real de
    P3c-2, `p3c2/salida/llamada_escalon3_p3c2.json`), una escritura por brazo y lecturas en el resto;
  - la llamada del tercer escalón: central, la salida de su unidad por la recta; peor caso, los 40.960 tokens;
  - la pata de E3: por llamada, las tarifas de la pata de P4; central, una verificación por unidad y un reintento de
    E1 en total, como en P4; alto, dos verificaciones y un reintento de E1 por unidad.
Escenario alto: salida de E1 y E3 por 1,5, y el tercer escalón en su peor caso.

Escribe solo en --salida (proyeccion_p4b.json). Uso (desde la raíz de una copia):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p4b/proyeccion_p4b.py --trabajo DIR --salida DIR
"""
from __future__ import annotations

import argparse
import json
import statistics as st
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
PR2 = AQUI.parent
E1 = {"in": 1.00, "out": 5.00, "cw": 1.25, "cr": 0.10}          # claude-haiku-4-5, USD por MTok
PREFIJO = {"anterior": 26309, "p3c": 27840}
TECHO_ESCALON_3 = 40960
TOPE = 1.5


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--trabajo", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    sal = a.salida.resolve()
    if REPO in sal.parents or sal == REPO:
        raise SystemExit("--salida no puede estar dentro del repo")
    sel = json.loads((AQUI / "salida" / "seleccion_p4b.json").read_text(encoding="utf-8"))
    cal = json.loads((PR2 / "p1" / "salida" / "censo_p1.json").read_text(encoding="utf-8"))["calibracion"]["mensaje"]
    an = json.loads((PR2 / "p4" / "salida" / "analisis_p4.json").read_text(encoding="utf-8"))
    g4 = json.loads((PR2 / "p4" / "salida" / "gasto_p4.json").read_text(encoding="utf-8"))
    ll = json.loads((PR2 / "p3c2" / "salida" / "llamada_escalon3_p3c2.json").read_text(encoding="utf-8"))
    assert g4["e1_nuevo"]["cache_stats"]["cache_write"] == PREFIJO["anterior"]
    assert ll["llamada_1_transmision"]["usage"]["cache_creation_input_tokens"] == PREFIJO["p3c"]
    xs, ys = [], []
    for f in an["filas"].values():
        u = (f.get("usage") or {}).get("nuevo")
        if u:
            xs.append(f["chars_propio"])
            ys.append(u["output_tokens"])
    mx, my = st.mean(xs), st.mean(ys)
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    recta = {"a": my - b * mx, "b": b, "n": len(xs)}

    def salida_e1(chars: int) -> float:
        return recta["a"] + recta["b"] * chars

    chars = sel["chars_propio"]
    brazos, e1_total = {}, {"central": 0.0, "alto": 0.0}
    for brazo in ("anterior", "p3c"):
        cl = json.loads((a.trabajo / f"claves_antes_{brazo}.json").read_text(encoding="utf-8"))
        n = len(cl)
        t_in = sum(cal["a"] + cal["tokens_por_caracter"] * f["chars_mensaje"] for f in cl)
        t_out = sum(salida_e1(chars[f["chunk_id"]]) for f in cl)
        pref = PREFIJO[brazo]
        fijo = (pref * E1["cw"] + (n - 1) * pref * E1["cr"] + t_in * E1["in"]) / 1e6
        brazos[brazo] = {"unidades": n, "tokens_entrada_sin_cache": round(t_in), "tokens_salida": round(t_out),
                         "central_usd": round(fijo + t_out * E1["out"] / 1e6, 4),
                         "alto_usd": round(fijo + 1.5 * t_out * E1["out"] / 1e6, 4)}
        for k in e1_total:
            e1_total[k] += brazos[brazo][f"{k}_usd"]
    corta = min((chars[c], c) for c in chars)[1]
    cl3 = {f["chunk_id"]: f for f in json.loads((a.trabajo / "claves_antes_p3c.json").read_text(encoding="utf-8"))}
    in3 = cal["a"] + cal["tokens_por_caracter"] * cl3[corta]["chars_mensaje"]
    base3 = (PREFIJO["p3c"] * E1["cr"] + in3 * E1["in"]) / 1e6
    escalon3 = {"unidad": corta, "central_usd": round(base3 + salida_e1(chars[corta]) * E1["out"] / 1e6, 4),
                "peor_caso_usd": round(base3 + TECHO_ESCALON_3 * E1["out"] / 1e6, 4)}
    pe = g4["pata_e3"]
    e3_llamada = pe["e3"]["gasto_usd_real"] / pe["e3"]["llamadas"]
    e1_reint = pe["e1_reintentos"]["gasto_usd_real"] / pe["e1_reintentos"]["llamadas"]
    n3 = len(sel["pata_e3"])
    pata = {"unidades": n3, "e3_usd_por_llamada_p4": round(e3_llamada, 5), "reintento_e1_usd_p4": e1_reint,
            "central_usd": round(n3 * e3_llamada + e1_reint, 4),
            "alto_usd": round(1.5 * n3 * (2 * e3_llamada + e1_reint), 4)}
    total = {"central_usd": round(e1_total["central"] + escalon3["central_usd"] + pata["central_usd"], 4),
             "alto_usd": round(e1_total["alto"] + escalon3["peor_caso_usd"] + pata["alto_usd"], 4)}
    out = {"comando": "data/experiment/prompt_r2/p4b/proyeccion_p4b.py --trabajo DIR --salida DIR",
           "recta_salida_p4": {k: round(v, 4) if isinstance(v, float) else v for k, v in recta.items()},
           "calibracion_mensaje_p1": {"a": cal["a"], "tokens_por_caracter": cal["tokens_por_caracter"]},
           "prefijo_tokens": PREFIJO, "e1_por_brazo": brazos, "escalon3": escalon3, "pata_e3": pata,
           "total": total, "tope_usd": TOPE, "dentro_del_tope": {k: v <= TOPE for k, v in total.items()}}
    sal.mkdir(parents=True, exist_ok=True)
    (sal / "proyeccion_p4b.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
