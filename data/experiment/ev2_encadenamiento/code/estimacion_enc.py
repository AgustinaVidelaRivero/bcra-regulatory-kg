"""
estimacion_enc.py — Estimación PARAMETRIZADA (sin precios) de la fase B del
encadenamiento, con tokens MEDIDOS:

  AGENTE (198 corridas = 66 pares × 3): tokens de la corrida BASE de cada uno de
  los 66 pares (trazas EV2F-* de data/experiment/ev2_corrida/trazas/ev2_base_*:
  trace.tokens_in / tokens_out / cache_read / cache_write, mismo agente, mismo
  grafo, misma pregunta) × 3 re-corridas. Banda: por grafo, mediana y máximo
  por corrida de las 40 trazas de fidelidad de ese grafo × corridas previstas.
  Los tokens de una re-corrida no tienen por qué coincidir con los de la base
  (no-determinismo del agente): la base es el mejor proxy disponible por par.

  JUEZ (594 llamadas = 198 respuestas × 3): entrada = chars reales del request
  (system + usuario con pregunta, respuesta, criterios) / chars-por-token
  MEDIDO en las 360 llamadas reales de la corrida base del juez
  (data/experiment/ev2_fidelidad_eval/cache/ev2_eval_r{1,2,3}.db: chars de
  request_json vs input_tokens facturados; mismo prompt v1, modelo y formato).
  Como las respuestas nuevas no existen aún, el request se construye con la
  respuesta BASE del mismo par como stand-in (mismo agente/grafo/pregunta);
  banda superior: respuesta más larga observada en la base para ese grafo.
  Salida = ajuste lineal out ≈ a + b·K medido en las mismas 360 llamadas (y
  máximo observado por K como cota).

Fórmulas (precios como variables, USD/MTok):
  USD_agente = (in·P_in + out·P_out + cw·P_cache_write + cr·P_cache_read) / 1e6
  USD_juez   = (in·P_in_juez + out·P_out_juez) / 1e6
Uso:  .venv/bin/python -B data/experiment/ev2_encadenamiento/code/estimacion_enc.py
      [--precio-in-agente --precio-out-agente --precio-cw-agente --precio-cr-agente
       --precio-in-juez --precio-out-juez]   (opcionales; sin ellos, solo tokens)
"""

from __future__ import annotations

import argparse
import json
import sqlite3
import statistics as st
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(CODE_DIR))
import comun_enc as en                # noqa: E402
from comun_enc import cf, juez        # noqa: E402

BASE_JUEZ_DBS = [cf.CACHE_DIR / f"{cf.DB_PREFIX}_r{r}.db" for r in (1, 2, 3)]
CAMPOS_AG = ("tokens_in", "tokens_out", "cache_read", "cache_write")


def trazas_base_fidelidad() -> dict[tuple[str, str], dict]:
    """(id_pregunta, grafo) → tokens + chars de respuesta de la traza base."""
    out = {}
    for lab in cf.LABELS:
        for f in sorted((en.BASE_TRAZAS_DIR / lab).glob("EV2F-*.json")):
            t = json.loads(f.read_text(encoding="utf-8"))
            tr, m = t["trace"], t["meta"]
            out[(m["caso_id"], m["grafo"])] = {**{k: tr[k] for k in CAMPOS_AG},
                                              "cost_usd_harness": tr["cost_usd"],
                                              "tools": tr["tool_calls_used"],
                                              "chars_respuesta": len((tr.get("final_json") or {}).get("respuesta") or ""),
                                              "respuesta": (tr.get("final_json") or {}).get("respuesta") or ""}
    if len(out) != 120:
        raise RuntimeError(f"esperaba 120 trazas base de fidelidad, hay {len(out)}")
    return out


def medir_juez_base() -> dict:
    ratios, out_por_k, filas, prompt_ok = [], defaultdict(list), 0, True
    for p in BASE_JUEZ_DBS:
        conn = sqlite3.connect(str(p))
        for i, o, rj in conn.execute("SELECT input_tokens, output_tokens, request_json FROM cache"):
            r = json.loads(rj)
            u = r["messages"][0]["content"]
            k = int(u.split("CRITERIOS (", 1)[1].split(")", 1)[0])
            ratios.append((len(r["system"]) + len(u)) / i)
            out_por_k[k].append(o)
            filas += 1
            prompt_ok &= (r["system"] == juez.PROMPT_JUEZ and r["model"] == juez.MODELO)
        conn.close()
    xs = [k for k, v in out_por_k.items() for _ in v]
    ys = [o for v in out_por_k.values() for o in v]
    mx, my = st.mean(xs), st.mean(ys)
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    a = my - b * mx
    return {"fuente": [en.rel_repo(p) for p in BASE_JUEZ_DBS], "n_llamadas": filas, "mismo_prompt_y_modelo": prompt_ok,
            "chars_por_token_in": {"mediana": round(st.median(ratios), 4), "min": round(min(ratios), 4),
                                   "max": round(max(ratios), 4)},
            "out_tokens_por_k": {k: {"n": len(v), "media": round(st.mean(v), 1), "max": max(v)}
                                 for k, v in sorted(out_por_k.items())},
            "ajuste_out": {"a": round(a, 2), "b": round(b, 2), "formula": "out ≈ a + b·K"}}


def main() -> int:
    ap = argparse.ArgumentParser()
    for n in ("in-agente", "out-agente", "cw-agente", "cr-agente", "in-juez", "out-juez"):
        ap.add_argument(f"--precio-{n}", type=float, default=None)
    args = ap.parse_args()

    pob = en.cargar_poblacion()
    base = trazas_base_fidelidad()
    gold = cf.cargar_gold()

    # ---------------- agente ----------------
    por_grafo = {g: [v for (q, gg), v in base.items() if gg == g] for g in en.GRAFOS}
    filas_ag, tot_central = [], Counter()
    for p in pob["pares"]:
        b = base[(p["id_pregunta"], p["grafo"])]
        filas_ag.append({"id_pregunta": p["id_pregunta"], "grafo": p["grafo"], "tipo": p["tipo"],
                         "tokens_base": {k: b[k] for k in CAMPOS_AG}, "tools_base": b["tools"],
                         "cost_usd_harness_base": b["cost_usd_harness"]})
        for k in CAMPOS_AG:
            tot_central[k] += b[k] * en.REPS_AGENTE
    n_por_grafo = Counter(p["grafo"] for p in pob["pares"])
    banda = {}
    for g in en.GRAFOS:
        n = n_por_grafo[g] * en.REPS_AGENTE
        banda[g] = {"corridas": n,
                    "mediana_por_corrida": {k: st.median(v[k] for v in por_grafo[g]) for k in CAMPOS_AG},
                    "max_por_corrida": {k: max(v[k] for v in por_grafo[g]) for k in CAMPOS_AG},
                    "media_por_corrida": {k: round(st.mean(v[k] for v in por_grafo[g])) for k in CAMPOS_AG},
                    "cost_usd_harness_medio_base": round(st.mean(v["cost_usd_harness"] for v in por_grafo[g]), 5)}
    tot_mediana = {k: sum(banda[g]["mediana_por_corrida"][k] * banda[g]["corridas"] for g in en.GRAFOS) for k in CAMPOS_AG}
    tot_max = {k: sum(banda[g]["max_por_corrida"][k] * banda[g]["corridas"] for g in en.GRAFOS) for k in CAMPOS_AG}
    costo_harness_central = round(sum(f["cost_usd_harness_base"] for f in filas_ag) * en.REPS_AGENTE, 4)
    agente = {"n_corridas": len(filas_ag) * en.REPS_AGENTE, "reps": en.REPS_AGENTE,
              "modelo": __import__("harness").MODEL,      # harness congelado (ya en sys.path vía comun_ev2)
              "fuente_tokens": "trazas base EV2F-* de los mismos 66 pares (data/experiment/ev2_corrida/trazas/ev2_base_*)",
              "tokens_central_pares_base_x3": dict(tot_central),
              "tokens_banda_mediana_grafo": tot_mediana, "tokens_banda_max_grafo": tot_max,
              "por_grafo": banda,
              "referencia_harness_cost_usd": {"nota": "harness.cost_usd de las trazas base × 3 (precios hardcodeados del "
                                                      "harness congelado; solo referencia, no es la fórmula parametrizada)",
                                              "central": costo_harness_central},
              "formula": "USD_agente = (in·P_in + out·P_out + cw·P_cache_write + cr·P_cache_read) / 1e6",
              "por_par": filas_ag}
    if None not in (args.precio_in_agente, args.precio_out_agente, args.precio_cw_agente, args.precio_cr_agente):
        pr = {"in": args.precio_in_agente, "out": args.precio_out_agente, "cw": args.precio_cw_agente, "cr": args.precio_cr_agente}
        f = lambda t: round((t["tokens_in"] * pr["in"] + t["tokens_out"] * pr["out"] + t["cache_write"] * pr["cw"]
                             + t["cache_read"] * pr["cr"]) / 1e6, 4)
        agente["precios_usd_mtok"] = pr
        agente["costo_estimado_usd"] = {"central": f(tot_central), "banda_mediana": f(tot_mediana), "banda_max": f(tot_max)}

    # ---------------- juez ----------------
    cal = medir_juez_base()
    cpt, a, b = cal["chars_por_token_in"], cal["ajuste_out"]["a"], cal["ajuste_out"]["b"]
    max_por_k = {int(k): v["max"] for k, v in cal["out_tokens_por_k"].items()}
    chars_sys = len(juez.PROMPT_JUEZ)
    chars_central, chars_max, ks = 0, 0, []
    max_resp_grafo = {g: max(v["chars_respuesta"] for v in por_grafo[g]) for g in en.GRAFOS}
    for p in pob["pares"]:
        gq = gold[p["id_pregunta"]]
        resp_base = base[(p["id_pregunta"], p["grafo"])]["respuesta"]
        kw = juez.construir_kwargs(gq["pregunta"], resp_base, gq["criterios"])
        chars_u = len(kw["messages"][0]["content"])
        chars_central += (chars_sys + chars_u) * en.REPS_AGENTE * en.REPS_JUEZ
        chars_max += (chars_sys + chars_u - len(resp_base) + max_resp_grafo[p["grafo"]]) * en.REPS_AGENTE * en.REPS_JUEZ
        ks += [len(gq["criterios"])] * en.REPS_AGENTE * en.REPS_JUEZ
    n_llam = len(ks)
    juez_est = {"n_llamadas": n_llam, "reps_juez": en.REPS_JUEZ, "modelo": juez.MODELO, "max_tokens": juez.MAX_TOKENS,
                "prompt_sha256": juez.PROMPT_SHA256, "medido_base": cal,
                "chars_stand_in": {"system": chars_sys, "total_central": chars_central, "total_banda_max": chars_max,
                                   "nota": "usuario construido con la respuesta BASE del mismo par como stand-in; "
                                           "banda máx: respuesta más larga de la base en ese grafo"},
                "criterios_por_llamada": dict(sorted(Counter(ks).items())),
                "estimacion_tokens": {
                    "input_total": {"central": round(chars_central / cpt["mediana"]),
                                    "banda_min": round(chars_central / cpt["max"]),
                                    "banda_max": round(chars_max / cpt["min"])},
                    "output_total": {"central": round(sum(a + b * k for k in ks)),
                                     "cota_max_observada": round(sum(max_por_k.get(k, a + b * k) for k in ks))}},
                "formula": "USD_juez = (input_total·P_in_juez + output_total·P_out_juez) / 1e6"}
    if None not in (args.precio_in_juez, args.precio_out_juez):
        et = juez_est["estimacion_tokens"]
        c = lambda ti, to: round(ti / 1e6 * args.precio_in_juez + to / 1e6 * args.precio_out_juez, 4)
        juez_est["precios_usd_mtok"] = {"in": args.precio_in_juez, "out": args.precio_out_juez}
        juez_est["costo_estimado_usd"] = {"central": c(et["input_total"]["central"], et["output_total"]["central"]),
                                          "banda_max": c(et["input_total"]["banda_max"], et["output_total"]["cota_max_observada"]),
                                          "banda_min": c(et["input_total"]["banda_min"], et["output_total"]["central"])}

    res = {"generado": datetime.now().isoformat(timespec="seconds"),
           "poblacion": {"n_pares": pob["n_pares"], "por_grafo": dict(n_por_grafo),
                         "n_corridas_agente": pob["n_corridas_agente"], "n_llamadas_juez": pob["n_llamadas_juez"]},
           "agente": agente, "juez": juez_est,
           "nota": "sin precios en este archivo salvo que se pasen por CLI; freno por proyección independiente por etapa"}
    en.ESTIMACION_DIR.mkdir(parents=True, exist_ok=True)
    (en.ESTIMACION_DIR / "estimacion_fase_b.json").write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
    ag_t, ju_t = agente["tokens_central_pares_base_x3"], juez_est["estimacion_tokens"]
    md = ["# Estimación parametrizada — fase B encadenamiento EV2 (sin precios)", "",
          f"Generado: {res['generado']}. Población: {pob['n_pares']} pares {dict(n_por_grafo)} × 3 = "
          f"{pob['n_corridas_agente']} corridas de agente; × 3 reps del juez = {pob['n_llamadas_juez']} llamadas al juez.", "",
          "## Agente (tokens medidos en las trazas base de los mismos 66 pares, × 3)", "",
          "| grafo | corridas | mediana in/out/cw/cr por corrida (base) | máx in/out/cw/cr | harness cost medio base (USD) |",
          "|---|---|---|---|---|"]
    for g in en.GRAFOS:
        bg = banda[g]; m, x = bg["mediana_por_corrida"], bg["max_por_corrida"]
        md.append(f"| {g} | {bg['corridas']} | {m['tokens_in']}/{m['tokens_out']}/{m['cache_write']}/{m['cache_read']} "
                  f"| {x['tokens_in']}/{x['tokens_out']}/{x['cache_write']}/{x['cache_read']} | {bg['cost_usd_harness_medio_base']} |")
    md += ["", f"- Central (tokens de la base de cada par × 3): in {ag_t['tokens_in']:,} / out {ag_t['tokens_out']:,} / "
           f"cache_write {ag_t['cache_write']:,} / cache_read {ag_t['cache_read']:,}.",
           f"- Banda mediana-grafo: {tot_mediana}; banda máx-grafo: {tot_max}.",
           f"- Referencia harness.cost_usd (precios hardcodeados del harness congelado) de las trazas base × 3: USD {costo_harness_central}.",
           f"- Fórmula: `{agente['formula']}`.", "",
           "## Juez (594 llamadas; chars→tokens y salida por K medidos en las 360 llamadas reales de la base)", "",
           f"- Medición base: {cal['n_llamadas']} llamadas, mismo prompt/modelo {cal['mismo_prompt_y_modelo']}; chars/token in mediana "
           f"{cpt['mediana']} [{cpt['min']}, {cpt['max']}]; salida ≈ {a} + {b}·K; máx por K { {k: v['max'] for k, v in cal['out_tokens_por_k'].items()} }.",
           f"- Entrada estimada: central {ju_t['input_total']['central']:,} [{ju_t['input_total']['banda_min']:,}, {ju_t['input_total']['banda_max']:,}] "
           f"(stand-in: respuesta base del mismo par; banda máx con la respuesta más larga del grafo).",
           f"- Salida estimada: central {ju_t['output_total']['central']:,} (cota máx observada {ju_t['output_total']['cota_max_observada']:,}).",
           f"- Fórmula: `{juez_est['formula']}`.", ""]
    if "costo_estimado_usd" in agente:
        md.append(f"- Agente con precios {agente['precios_usd_mtok']}: {agente['costo_estimado_usd']}")
    if "costo_estimado_usd" in juez_est:
        md.append(f"- Juez con precios {juez_est['precios_usd_mtok']}: {juez_est['costo_estimado_usd']}")
    (en.ESTIMACION_DIR / "estimacion_fase_b.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("\n".join(md))
    print(f"→ {en.ESTIMACION_DIR / 'estimacion_fase_b.json'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
