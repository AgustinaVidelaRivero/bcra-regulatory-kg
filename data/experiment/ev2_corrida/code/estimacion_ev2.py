"""
estimacion_ev2.py — Estimación de costo PARAMETRIZADA de la fase B (mandato f).

NO contiene precios: la fórmula deja P_in, P_out, P_cache_write, P_cache_read
como VARIABLES (USD por millón de tokens) a resolver en la autorización.

Conteo de corridas: censo/censo_navegabilidad_*.json + orden resuelto
(fidelidad 40 por grafo; navegabilidad 2×presentes por grafo; N=1).

Tokens por corrida (medianas de corridas HISTÓRICAS del repo, mismo agente
Haiku 4.5 / mismas tools / thinking OFF; el selftest offline usa un cliente
falso y no aporta tokens reales — se declara):
  - v3   : posthoc_run/summary_escalon1b_r3_reensamblado_v3.json
           (36 corridas frescas, hit_rate 0.0)
  - run_3: posthoc_run/summary_off_run_3.json
           (23 corridas frescas, hit_rate 0.0)
  - v2   : SIN corrida histórica (grafo nuevo). Proxy CONSERVADOR: máximo por
           campo entre las corridas frescas citadas (incluye
           summary_u6_exploracion_reensamblado_v3.json, 25 corridas frescas).

Fórmula:
  USD_total = Σ_grafo n_grafo × (T_in·P_in + T_out·P_out
                                 + T_cw·P_cache_write + T_cr·P_cache_read) / 1e6

Uso:  python3 -B estimacion_ev2.py
"""

from __future__ import annotations

import json
from datetime import datetime

from comun_ev2 import EV2_DIR, EVAL_DIR, GRAFO_KEYS

POSTHOC = EVAL_DIR / "posthoc_run"
FUENTES = {
    "v3": "summary_escalon1b_r3_reensamblado_v3.json",
    "run_3": "summary_off_run_3.json",
    "u6_extra": "summary_u6_exploracion_reensamblado_v3.json",
}


def _por_corrida(nombre: str) -> dict:
    s = json.load(open(POSTHOC / nombre, encoding="utf-8"))
    a, n = s["agent_cache_stats"], s["n_reps_total"]
    assert a["hit_rate"] == 0.0, f"{nombre} no es corrida fresca"
    return {"fuente": f"posthoc_run/{nombre}", "n_corridas_fuente": n,
            "T_in": round(a["tokens_in"] / n), "T_out": round(a["tokens_out"] / n),
            "T_cr": round(a["cache_read"] / n), "T_cw": round(a["cache_write"] / n)}


def main() -> int:
    t_v3 = _por_corrida(FUENTES["v3"])
    t_r3 = _por_corrida(FUENTES["run_3"])
    t_u6 = _por_corrida(FUENTES["u6_extra"])
    t_v2 = {"fuente": ("proxy conservador: máximo por campo entre "
                       f"{t_v3['fuente']}, {t_r3['fuente']}, {t_u6['fuente']} "
                       "(v2 no tiene corrida histórica)"),
            "n_corridas_fuente": None}
    for k in ("T_in", "T_out", "T_cr", "T_cw"):
        t_v2[k] = max(t_v3[k], t_r3[k], t_u6[k])
    tokens = {"v2": t_v2, "v3": t_v3, "run_3": t_r3}

    conteo, filas = {}, []
    for g in GRAFO_KEYS:
        censo = json.load(open(EV2_DIR / "censo" / f"censo_navegabilidad_{g}.json",
                               encoding="utf-8"))
        n_fid, n_nav = 40, 2 * censo["n_presentes"]
        n = n_fid + n_nav
        conteo[g] = {"fidelidad": n_fid, "navegabilidad": n_nav, "total": n,
                     "nav_presentes": censo["n_presentes"],
                     "nav_ausentes": censo["n_ausentes"]}
        t = tokens[g]
        filas.append({
            "grafo": g, "n_corridas": n,
            "tokens_por_corrida": {k: t[k] for k in ("T_in", "T_out", "T_cr", "T_cw")},
            "fuente_tokens": t["fuente"],
            "tokens_totales": {k: n * t[k] for k in ("T_in", "T_out", "T_cr", "T_cw")},
        })

    total_corridas = sum(c["total"] for c in conteo.values())
    tot = {k: sum(f["tokens_totales"][k] for f in filas)
           for k in ("T_in", "T_out", "T_cr", "T_cw")}

    payload = {
        "generado": datetime.now().isoformat(timespec="seconds"),
        "alcance": ("fase B de esta unidad: corrida del agente, N=1, ambos ejes, "
                    "tres grafos. NO incluye: re-corridas N=3 sobre 'parcial', "
                    "auditoría del 10%, ni juez de fidelidad (etapas posteriores "
                    "con su propia autorización)."),
        "conteo_corridas": conteo,
        "total_corridas": total_corridas,
        "tokens_por_grafo": filas,
        "tokens_totales": tot,
        "formula": ("USD_total = sum_grafo n_grafo * (T_in*P_in + T_out*P_out "
                    "+ T_cw*P_cache_write + T_cr*P_cache_read) / 1e6  "
                    "== (Tot_in*P_in + Tot_out*P_out + Tot_cw*P_cache_write "
                    "+ Tot_cr*P_cache_read) / 1e6"),
        "variables_de_precio": ["P_in", "P_out", "P_cache_write", "P_cache_read"],
        "nota_selftest": ("el selftest offline usa cliente falso: sus tokens no "
                          "son medición; los T_* salen de las corridas históricas "
                          "citadas en fuente_tokens"),
    }
    outdir = EV2_DIR / "estimacion"
    outdir.mkdir(parents=True, exist_ok=True)
    with (outdir / "estimacion_fase_b.json").open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    md = ["# Estimación parametrizada — fase B corrida EV2 (sin precios)", "",
          f"Generado: {payload['generado']}. Alcance: {payload['alcance']}", "",
          "| grafo | fid | nav (2×presentes) | corridas | T_in | T_out | T_cw | T_cr | fuente |",
          "|---|---|---|---|---|---|---|---|---|"]
    for f_ in filas:
        g = f_["grafo"]; c = conteo[g]; t = f_["tokens_por_corrida"]
        md.append(f"| {g} | {c['fidelidad']} | {c['navegabilidad']} | {c['total']} "
                  f"| {t['T_in']} | {t['T_out']} | {t['T_cw']} | {t['T_cr']} "
                  f"| {f_['fuente_tokens']} |")
    md += ["",
           f"**Total corridas: {total_corridas}.** Tokens totales estimados: "
           f"in {tot['T_in']:,} / out {tot['T_out']:,} / cache_write {tot['T_cw']:,} "
           f"/ cache_read {tot['T_cr']:,}.", "",
           "```",
           "USD_total = ( Tot_in  × P_in",
           "            + Tot_out × P_out",
           "            + Tot_cw  × P_cache_write",
           "            + Tot_cr  × P_cache_read ) / 1e6",
           "```",
           "",
           "Precios (USD/MTok) como variables, a resolver en la autorización: "
           "P_in, P_out, P_cache_write, P_cache_read.",
           "",
           payload["nota_selftest"] + "."]
    with (outdir / "estimacion_fase_b.md").open("w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")

    print(json.dumps({"total_corridas": total_corridas,
                      "conteo": conteo, "tokens_totales": tot},
                     ensure_ascii=False, indent=2))
    print("-> estimacion/estimacion_fase_b.{json,md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
