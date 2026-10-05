"""
costo_p4b.py — U-PROMPT-R2, P4b (USD 0): el costo real contra el tope y la proyección, y la proyección de U-REEXT-T0
con la salida medida.

Costo real: `gasto_p4b.jsonl` de la corrida (una línea por modo; la fórmula de caching de cada cliente, decisión 2) y el
presupuesto compartido (`presupuesto_p4b.json`).
U-REEXT-T0 (2.434 unidades): la re-estimación de P4 (`p4/costo_real_p4.py`: la base sellada de P1, los deltas de
P3b-2 y los cocientes de P4 del prefijo `3817de475c93` contra el sellado), con lo que mide P4b encima:
  - el prefijo de P3c, medido (27.840 tokens, la llamada de P3c-2);
  - la entrada sin caché y la salida de E1, por los cocientes P3c/anterior de P4b (suma de `input_tokens` y de
    `output_tokens` de las unidades con salida en los dos brazos). Las unidades se eligieron por lectura, no se
    sortearon: los cocientes son una cota, no una estimación de la tanda;
  - E3 y los reintentos del ratchet escalan con la salida, como en P4;
  - el tercer escalón, con la estimación de P3c-1 (`p3c2/salida/costo_p3c2.json`).

Escribe solo en --salida (costo_p4b.json). Uso (desde la raíz de una copia):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p4b/costo_p4b.py --trabajo DIR --proyeccion P \
      --salida DIR
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

AQUI = Path(__file__).resolve().parent
PR2 = AQUI.parent
CENSO = PR2 / "p1" / "salida" / "censo_p1.json"
COSTO_P3B2 = PR2 / "p3b2" / "salida" / "costo_p3b2.json"
COSTO_P4 = PR2 / "p4" / "salida" / "costo_real_p4.json"
COSTO_P3C2 = PR2 / "p3c2" / "salida" / "costo_p3c2.json"
PREC = {"in": 1.00, "out": 5.00, "cw": 1.25, "cr": 0.10}
N = 2434
PREFIJO_P3C = 27840


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--trabajo", type=Path, required=True)
    ap.add_argument("--proyeccion", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    gastos = [json.loads(x) for x in (a.trabajo / "gasto_p4b.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
    pres = json.loads((a.trabajo / "presupuesto_p4b.json").read_text(encoding="utf-8"))
    proy = json.loads(a.proyeccion.read_text(encoding="utf-8"))
    res = {}
    for x in (a.trabajo / "resultados_p4b.jsonl").read_text(encoding="utf-8").splitlines():
        if x.strip():
            r = json.loads(x)
            res[r["chunk_id"]] = r
    real: dict = {}
    for g in gastos:
        k = g["modo"] if g["modo"] != "e1" else f"e1_{g['brazo']}"
        if g["modo"] != "e3":           # en el modo e3, el cliente de E1 del proceso no llama: E1 va por el de reintentos
            d = real.setdefault(k, {"usd": 0.0, "llamadas": 0})
            d["usd"] += g["e1"]["gasto_usd_real"]
            d["llamadas"] += g["e1"]["llamadas"]
        for sub in ("e3", "e1_reintentos"):
            if sub in g:
                s = real.setdefault(f"pata_{sub}", {"usd": 0.0, "llamadas": 0})
                s["usd"] += g[sub]["gasto_usd_real"]
                s["llamadas"] += g[sub]["llamadas"]
    real = {k: {"usd": round(v["usd"], 4), "llamadas": v["llamadas"]} for k, v in real.items()}
    ids = sorted({r["id"] for r in res.values() if r.get("brazo") == "anterior"}
                 & {r["id"] for r in res.values() if r.get("brazo") == "p3c"})
    ok = [c for c in ids if res[f"{c}|anterior"].get("usage") and res[f"{c}|p3c"].get("usage")]

    def suma(brazo, k):
        return sum(res[f"{c}|{brazo}"]["usage"][k] for c in ok)
    h_in = suma("p3c", "input_tokens") / suma("anterior", "input_tokens")
    h_out = suma("p3c", "output_tokens") / suma("anterior", "output_tokens")
    censo = json.loads(CENSO.read_text(encoding="utf-8"))
    p3b2 = json.loads(COSTO_P3B2.read_text(encoding="utf-8"))
    p4 = json.loads(COSTO_P4.read_text(encoding="utf-8"))
    c3c2 = json.loads(COSTO_P3C2.read_text(encoding="utf-8"))
    fc, u = censo["tanda0_fases_cerradas"], censo["usage_crudo_total"]
    base_in, base_out = u["input_tokens"] * PREC["in"] / 1e6, u["output_tokens"] * PREC["out"] / 1e6
    e3v, e1r = fc["e3_verificador_usd"], fc["e3_reintentos_e1_usd"]
    render_p1 = censo["costos"]["B_central"]["e3_extra_por_render_usd"]
    crec_p1 = censo["escenarios_salida"]["B_central"]["crecimiento_salida"]
    deltas = p3b2["u_reext_t0"]["componentes_usd"]
    p3b_resto = sum(v for k, v in deltas.items() if k not in ("e1_prefijo_lecturas", "e1_prefijo_escrituras"))
    # el tercer escalón con la salida del prefijo nuevo (P3c-1): de la mediana al máximo, sin y con el ratchet
    esc3 = {k: v for k, v in c3c2["u_reext_t0"]["tercer_escalon_usd"].items() if k.startswith("nuevo")}
    esc3_min = min(v["sin_ratchet"] for v in esc3.values())
    esc3_max = max(v["sin_ratchet"] for v in esc3.values())
    esc3_ratchet = max(v["con_ratchet"] for v in esc3.values())
    escenarios = {}
    for nombre, v in p4["u_reext_t0"].items():
        g_out = v["crecimiento_salida"] * h_out
        g_in = p4["medido"]["entrada_nuevo_sobre_sellado"] * h_in
        e1 = (N - 5) * PREFIJO_P3C * PREC["cr"] / 1e6 + 5 * PREFIJO_P3C * PREC["cw"] / 1e6 + base_in * g_in + base_out * g_out
        e3 = e3v + render_p1 * max(0.0, g_out - 1) / crec_p1 + e1r * g_out
        total = e1 + e3 + p3b_resto
        escenarios[f"p4_{nombre}"] = {"crecimiento_salida_sobre_sellado": round(g_out, 3), "e1_usd": round(e1, 2),
                                       "e3_usd": round(e3, 2), "deltas_p3b2_usd": round(p3b_resto, 2),
                                       "central_usd": round(total, 2),
                                       "con_tercer_escalon_usd": [round(total + esc3_min, 2), round(total + esc3_max, 2)],
                                       "con_tercer_escalon_y_ratchet_max_usd": round(total + esc3_ratchet, 2),
                                       "por_1_4_usd": round((total + esc3_max) * 1.4, 2)}
    out = {"comando": "data/experiment/prompt_r2/p4b/costo_p4b.py --trabajo DIR --proyeccion P --salida DIR",
           "costo_real": {"por_paso": real, "total_compartido_usd": pres["gasto_usd"], "tope_usd": pres["tope_usd"],
                          "proyeccion_central_usd": proy["total"]["central_usd"],
                          "proyeccion_alta_usd": proy["total"]["alto_usd"]},
           "medido": {"unidades_con_salida_en_los_dos_brazos": len(ok),
                      "entrada_p3c_sobre_anterior": round(h_in, 3), "salida_p3c_sobre_anterior": round(h_out, 3),
                      "prefijo_tokens_p3c": PREFIJO_P3C},
           "u_reext_t0": escenarios, "tercer_escalon_p3c1_usd": {"sin_ratchet": [esc3_min, esc3_max], "con_ratchet_max": esc3_ratchet}, "tope_vigente_usd": 72}
    a.salida.mkdir(parents=True, exist_ok=True)
    (a.salida / "costo_p4b.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
