"""
ab_caching.py — A/B de prompt caching multi-turn en el harness (Fase 2.3).

Corre las 6 preguntas del loop manual (dev_pool) sobre Run 3, dos veces:
versión SIN cache y versión CON cache (cache_control móvil en el último bloque de
usuario; ámbito INTRA-pregunta — ver harness._apply_cache_breakpoint).

Equivalencia (definida de antemano; NO se exigen trazas byte-idénticas porque
temp 0 admite no-determinismo menor de la API):
  (a) los 6 JSON finales parsean en ambas versiones,
  (b) respondible idéntico por pregunta,
  (c) mismas citas post-normalización (o diferencias solo de orden),
  (d) test operacional fuerte: el juez CONGELADO v2.1.1 da veredictos idénticos
      en todas las dimensiones sobre ambas versiones de cada traza.

Métricas: cache_creation_input_tokens y cache_read_input_tokens por pregunta,
costo total con/sin cache, y el factor de ahorro NETO real (la escritura de cache
cuesta 1,25× y la lectura 0,1×; preguntas cortas pueden no ahorrar).
"""

from __future__ import annotations

import json
import os

from dotenv import load_dotenv

from loader import load_graph, EVAL_DIR
from harness import GraphAgent, _norm_loc
import judge

RUN = "run_3"
QIDS = ["CQ-001", "CQ-009", "CQ-023", "CQ-029", "CQ-032", "dev_unans_1"]
REPORT_PATH = EVAL_DIR / "03_ab_caching.md"
VERDICT_DIMS = ["correctitud", "completitud", "cita_documento_correcto",
                "cita_precision", "abstencion", "especulacion_en_prosa",
                "requiere_adjudicacion_humana"]


def _norm_citas(citas):
    out = set()
    for c in citas or []:
        if isinstance(c, dict):
            out.add((c.get("source_doc"), _norm_loc(c.get("location") or "")))
    return out


def main():
    load_dotenv(EVAL_DIR / ".env")
    if not os.environ.get("ANTHROPIC_API_KEY", "").strip():
        raise SystemExit("ERROR: ANTHROPIC_API_KEY no seteada")
    import anthropic
    client = anthropic.Anthropic()

    kg = load_graph(RUN)
    pool = {q["id"]: q for q in
            json.load(open(EVAL_DIR / "queries" / "dev_pool.json", encoding="utf-8"))["preguntas"]}
    agent_off = GraphAgent(kg, client=client, cache_conversation=False)
    agent_on = GraphAgent(kg, client=client, cache_conversation=True)

    rows = []
    for qid in QIDS:
        q = pool[qid]
        print(f"[{qid}] sin cache…", flush=True)
        off = agent_off.ask(qid, q["pregunta"])
        print(f"[{qid}] con cache…", flush=True)
        on = agent_on.ask(qid, q["pregunta"])
        print(f"[{qid}] juez sobre ambas…", flush=True)
        v_off = judge.judge_trace(client, q, vars(off))["verdict"]
        v_on = judge.judge_trace(client, q, vars(on))["verdict"]

        eq_resp = (off.final_json or {}).get("respondible") == (on.final_json or {}).get("respondible")
        eq_parse = off.parse_ok and on.parse_ok
        eq_citas = _norm_citas((off.final_json or {}).get("citas")) == \
            _norm_citas((on.final_json or {}).get("citas"))
        verdict_diffs = [d for d in VERDICT_DIMS if v_off.get(d) != v_on.get(d)]
        eq_judge = not verdict_diffs

        rows.append({
            "qid": qid,
            "off": off, "on": on,
            "eq_parse": eq_parse, "eq_resp": eq_resp, "eq_citas": eq_citas,
            "eq_judge": eq_judge, "verdict_diffs": verdict_diffs,
            "v_off": v_off, "v_on": v_on,
        })
        print(f"   parse={eq_parse} respondible={eq_resp} citas={eq_citas} "
              f"juez={eq_judge}{'  DIFFS:'+str(verdict_diffs) if verdict_diffs else ''} "
              f"| cache_w={on.cache_write} cache_r={on.cache_read} "
              f"| costo off=${off.cost_usd:.5f} on=${on.cost_usd:.5f}", flush=True)

    _report(rows)


def _report(rows):
    all_eq = all(r["eq_parse"] and r["eq_resp"] and r["eq_citas"] and r["eq_judge"]
                 for r in rows)
    cost_off = sum(r["off"].cost_usd for r in rows)
    cost_on = sum(r["on"].cost_usd for r in rows)
    tin_off = sum(r["off"].tokens_in for r in rows)
    tin_on = sum(r["on"].tokens_in for r in rows)
    cw = sum(r["on"].cache_write for r in rows)
    cr = sum(r["on"].cache_read for r in rows)

    L = ["# A/B de prompt caching (multi-turn) — harness KG-RAG", ""]
    L.append("6 preguntas del dev_pool sobre Run 3, SIN cache vs CON cache "
             "(cache_control móvil en el último bloque de usuario; ámbito "
             "INTRA-pregunta). Respondedor `claude-haiku-4-5-20251001`, temp 0. "
             "Juez de equivalencia: v2.1.1 CONGELADO.")
    L.append("")
    L.append(f"**Equivalencia: {'✅ PASA' if all_eq else '❌ NO pasa'}** "
             "(parse + respondible + citas post-norm + veredictos del juez idénticos).")
    L.append("")
    L.append("## Equivalencia por pregunta")
    L.append("")
    L.append("| qid | parse | respondible | citas (post-norm) | juez idéntico | diffs |")
    L.append("|-----|:-----:|:-----------:|:-----------------:|:-------------:|-------|")
    for r in rows:
        d = ", ".join(r["verdict_diffs"]) if r["verdict_diffs"] else "—"
        L.append(f"| {r['qid']} | {'✅' if r['eq_parse'] else '❌'} | "
                 f"{'✅' if r['eq_resp'] else '❌'} | {'✅' if r['eq_citas'] else '❌'} | "
                 f"{'✅' if r['eq_judge'] else '❌'} | {d} |")
    L.append("")
    L.append("## Economía del cache (medida, no asumida)")
    L.append("")
    L.append("La escritura de cache cuesta 1,25× y la lectura 0,1×. El costo `on` "
             "ya incluye el premium de escritura. Las preguntas cortas (pocas "
             "tools) pueden no ahorrar; la ganancia está en las largas.")
    L.append("")
    L.append("| qid | tools | tok_in off | tok_in on | cache_creation | cache_read | costo off | costo on | Δ% |")
    L.append("|-----|------:|-----------:|----------:|---------------:|-----------:|----------:|---------:|----:|")
    for r in rows:
        off, on = r["off"], r["on"]
        dpct = (1 - on.cost_usd / off.cost_usd) * 100 if off.cost_usd else 0.0
        L.append(f"| {r['qid']} | {on.tool_calls_used} | {off.tokens_in} | {on.tokens_in} "
                 f"| {on.cache_write} | {on.cache_read} | ${off.cost_usd:.5f} "
                 f"| ${on.cost_usd:.5f} | {dpct:+.1f}% |")
    L.append(f"| **TOTAL** | | {tin_off} | {tin_on} | {cw} | {cr} | "
             f"**${cost_off:.5f}** | **${cost_on:.5f}** | "
             f"**{(1-cost_on/cost_off)*100:+.1f}%** |")
    L.append("")
    factor = cost_off / cost_on if cost_on else float("inf")
    L.append(f"**Factor de ahorro neto: {factor:.2f}×** "
             f"(costo sin cache / costo con cache, sobre las 6 preguntas).")
    L.append("")
    L.append("**Ámbito declarado:** el ahorro es INTRA-pregunta. El prefijo "
             "compartido entre preguntas distintas (system+tools, ~1.433 tok) está "
             "por debajo del mínimo cacheable de Haiku 4.5 (4.096 tok), por lo que "
             "el cache NO se comparte entre preguntas: cada pregunta arranca "
             "conversación nueva y solo reutiliza el cache dentro de su propio loop "
             "de tools.")
    L.append("")
    REPORT_PATH.write_text("\n".join(L), encoding="utf-8")
    print(f"\nEquivalencia global: {'PASA' if all_eq else 'NO PASA'}")
    print(f"Costo off=${cost_off:.5f}  on=${cost_on:.5f}  factor={factor:.2f}x")
    print(f"Reporte: {REPORT_PATH}")


if __name__ == "__main__":
    main()
