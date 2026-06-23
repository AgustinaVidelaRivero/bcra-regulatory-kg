"""
ab_investigate_cq029.py — Investigación puntual de CQ-029.

CQ-029 quedó ESTABLE en el control off-vs-off2 (2 corridas) pero había divergido
off-vs-on en el A/B. Por el criterio acordado, se investiga antes de congelar:
¿es un caso de frontera (correcta/parcial) que oscila run-to-run independiente del
cache, o el cache cambia algo?

Test: K corridas SIN cache + K corridas CON cache. Se juzga cada una y se reporta
la distribución de correctitud (y completitud, citas) por grupo. Si correctitud
VARÍA dentro del grupo sin cache → inestabilidad intrínseca de la pregunta (el
cache queda exonerado). Si el grupo sin cache es perfectamente estable y el grupo
con cache difiere de forma sistemática → se flaguea (aunque cache_control es
metadata y no puede, estructuralmente, cambiar la salida).
"""

from __future__ import annotations

import json
import os
from collections import Counter

from dotenv import load_dotenv

from loader import load_graph, EVAL_DIR
from harness import GraphAgent, _norm_loc
import judge

RUN = "run_3"
QID = "CQ-029"
K = 4
REPORT_PATH = EVAL_DIR / "03c_cq029_investigacion.md"


def _norm_citas(citas):
    return sorted((c.get("source_doc"), _norm_loc(c.get("location") or ""))
                  for c in (citas or []) if isinstance(c, dict))


def main():
    load_dotenv(EVAL_DIR / ".env")
    if not os.environ.get("ANTHROPIC_API_KEY", "").strip():
        raise SystemExit("ERROR: ANTHROPIC_API_KEY no seteada")
    import anthropic
    client = anthropic.Anthropic()
    kg = load_graph(RUN)
    pool = {q["id"]: q for q in
            json.load(open(EVAL_DIR / "queries" / "dev_pool.json", encoding="utf-8"))["preguntas"]}
    q = pool[QID]

    runs = []
    for cache in (False, True):
        agent = GraphAgent(kg, client=client, cache_conversation=cache)
        for i in range(K):
            tag = ("on" if cache else "off") + f"_{i+1}"
            print(f"[{QID}] {tag}…", flush=True)
            tr = agent.ask(QID, q["pregunta"])
            v = judge.judge_trace(client, q, vars(tr))["verdict"]
            runs.append({
                "tag": tag, "cache": cache,
                "correctitud": v.get("correctitud"),
                "completitud": v.get("completitud"),
                "cita_doc": v.get("cita_documento_correcto"),
                "citas": _norm_citas((tr.final_json or {}).get("citas")),
                "tools": tr.tool_calls_used,
                "respuesta": (tr.final_json or {}).get("respuesta", "")[:200],
            })
            print(f"   correctitud={runs[-1]['correctitud']} "
                  f"completitud={runs[-1]['completitud']} "
                  f"tools={runs[-1]['tools']} citas={runs[-1]['citas']}", flush=True)

    _report(runs)


def _report(runs):
    off = [r for r in runs if not r["cache"]]
    on = [r for r in runs if r["cache"]]
    corr_off = Counter(r["correctitud"] for r in off)
    corr_on = Counter(r["correctitud"] for r in on)
    off_varia = len(corr_off) > 1
    on_varia = len(corr_on) > 1
    # ¿las distribuciones se solapan? (mismo conjunto de valores observados)
    solapan = set(corr_off) & set(corr_on)

    if off_varia:
        concl = ("✅ INESTABILIDAD INTRÍNSECA: correctitud varía DENTRO del grupo "
                 "sin cache → es no-determinismo run-to-run de la pregunta, no el "
                 "cache. Equivalencia del caching sostenida para CQ-029.")
    elif solapan and not (len(corr_on) == 1 and len(corr_off) == 1 and
                          set(corr_on) != set(corr_off)):
        concl = ("✅ Distribuciones solapadas: los valores de correctitud con y sin "
                 "cache caen en el mismo conjunto → el cache no introduce un sesgo "
                 "distinto. Equivalencia sostenida.")
    else:
        concl = ("⚠ El grupo sin cache fue estable y el grupo con cache difiere de "
                 "forma sistemática. Revisar (aunque cache_control es metadata).")

    L = [f"# Investigación puntual de {QID} — A/B caching", ""]
    L.append(f"{K} corridas SIN cache + {K} CON cache, juzgadas individualmente. "
             "Objetivo: ¿la divergencia off-vs-on fue inestabilidad de frontera de "
             "la pregunta, o efecto del cache?")
    L.append("")
    L.append(f"**Conclusión: {concl}**")
    L.append("")
    L.append(f"Distribución de correctitud — SIN cache: {dict(corr_off)} | "
             f"CON cache: {dict(corr_on)}")
    L.append("")
    L.append("| run | cache | correctitud | completitud | cita_doc | tools | citas |")
    L.append("|-----|:-----:|-------------|-------------|:--------:|------:|-------|")
    for r in runs:
        L.append(f"| {r['tag']} | {'on' if r['cache'] else 'off'} | "
                 f"{r['correctitud']} | {r['completitud']} | {r['cita_doc']} | "
                 f"{r['tools']} | {r['citas']} |")
    L.append("")
    L.append("## Respuestas (primeros 200 chars) — para ver la variación de trayectoria")
    L.append("")
    for r in runs:
        L.append(f"**{r['tag']}**: {r['respuesta']}")
        L.append("")
    REPORT_PATH.write_text("\n".join(L), encoding="utf-8")
    print(f"\nSIN cache correctitud: {dict(corr_off)} | CON cache: {dict(corr_on)}")
    print(concl)
    print(f"Reporte: {REPORT_PATH}")


if __name__ == "__main__":
    main()
