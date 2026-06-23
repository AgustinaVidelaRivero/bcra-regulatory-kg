"""
ab_control.py — Control de no-determinismo para el A/B de caching.

Las 3 preguntas que divergieron en el A/B (off-vs-on) — CQ-009, CQ-023, CQ-029 —
se corren DOS VECES MÁS, ambas SIN cache (off vs off2). Criterio (definido de
antemano): si off-vs-off2 también diverge (veredicto del juez o citas), la
inestabilidad es propiedad de la PREGUNTA (no-determinismo run-to-run a temp 0),
no del cache → la equivalencia del caching queda demostrada para los fines del
experimento. Si alguna es perfectamente estable off-vs-off2 pero divergió
off-vs-on, esa puntual se investiga antes de congelar.

n=3: es un CONTROL DE CORDURA, no un test estadístico. Alcanza para la decisión de
caching porque el argumento estructural (cache_control es metadata que no puede
cambiar la salida del modelo) hace que la carga de la prueba sea baja.
"""

from __future__ import annotations

import json
import os

from dotenv import load_dotenv

from loader import load_graph, EVAL_DIR
from harness import GraphAgent, _norm_loc
import judge

RUN = "run_3"
QIDS = ["CQ-009", "CQ-023", "CQ-029"]
REPORT_PATH = EVAL_DIR / "03b_ab_control.md"
VERDICT_DIMS = ["correctitud", "completitud", "cita_documento_correcto",
                "cita_precision", "abstencion", "especulacion_en_prosa",
                "requiere_adjudicacion_humana"]

# Diffs observados en el A/B (off-vs-on), para reportar lado a lado.
OFF_VS_ON = {
    "CQ-009": {"citas_difieren": True,
               "verdict_diffs": ["correctitud", "completitud", "requiere_adjudicacion_humana"]},
    "CQ-023": {"citas_difieren": False, "verdict_diffs": ["completitud"]},
    "CQ-029": {"citas_difieren": False, "verdict_diffs": ["correctitud"]},
}


def _norm_citas(citas):
    return {(c.get("source_doc"), _norm_loc(c.get("location") or ""))
            for c in (citas or []) if isinstance(c, dict)}


def main():
    load_dotenv(EVAL_DIR / ".env")
    if not os.environ.get("ANTHROPIC_API_KEY", "").strip():
        raise SystemExit("ERROR: ANTHROPIC_API_KEY no seteada")
    import anthropic
    client = anthropic.Anthropic()
    kg = load_graph(RUN)
    pool = {q["id"]: q for q in
            json.load(open(EVAL_DIR / "queries" / "dev_pool.json", encoding="utf-8"))["preguntas"]}
    agent = GraphAgent(kg, client=client, cache_conversation=False)  # AMBAS sin cache

    rows = []
    for qid in QIDS:
        q = pool[qid]
        print(f"[{qid}] off (run A, sin cache)…", flush=True)
        a = agent.ask(qid, q["pregunta"])
        print(f"[{qid}] off2 (run B, sin cache)…", flush=True)
        b = agent.ask(qid, q["pregunta"])
        print(f"[{qid}] juez sobre ambas…", flush=True)
        va = judge.judge_trace(client, q, vars(a))["verdict"]
        vb = judge.judge_trace(client, q, vars(b))["verdict"]
        citas_dif = _norm_citas((a.final_json or {}).get("citas")) != \
            _norm_citas((b.final_json or {}).get("citas"))
        vdiffs = [d for d in VERDICT_DIMS if va.get(d) != vb.get(d)]
        inestable = citas_dif or bool(vdiffs)
        rows.append({"qid": qid, "citas_dif": citas_dif, "vdiffs": vdiffs,
                     "inestable": inestable, "a": a, "b": b, "va": va, "vb": vb})
        print(f"   off-vs-off2: citas_difieren={citas_dif} verdict_diffs={vdiffs} "
              f"=> {'INESTABLE' if inestable else 'ESTABLE'}", flush=True)

    _report(rows)


def _report(rows):
    # decisión
    all_unstable = all(r["inestable"] for r in rows)
    L = ["# Control de no-determinismo (off-vs-off2) — A/B de caching", ""]
    L.append("Las 3 preguntas que divergieron en off-vs-on, corridas dos veces más "
             "ambas SIN cache. Si off-vs-off2 también diverge, la inestabilidad es "
             "de la pregunta (no-determinismo a temp 0), no del cache.")
    L.append("")
    L.append("**n=3: control de cordura, no test estadístico.** El argumento "
             "estructural (cache_control es metadata, no cambia la salida del "
             "modelo) hace baja la carga de la prueba.")
    L.append("")
    veredicto = ("✅ Equivalencia del caching DEMOSTRADA (las 3 son inestables "
                 "también off-vs-off2 → la divergencia es no-determinismo, no cache)"
                 if all_unstable else
                 "⚠ Alguna pregunta es estable off-vs-off2 pero divergió off-vs-on "
                 "→ investigar antes de congelar")
    L.append(f"**Veredicto: {veredicto}.**")
    L.append("")
    L.append("## Comparación lado a lado")
    L.append("")
    L.append("| qid | off-vs-on (A/B) | off-vs-off2 (control) | ¿inestable sin cache? |")
    L.append("|-----|-----------------|------------------------|:---------------------:|")
    for r in rows:
        ref = OFF_VS_ON.get(r["qid"], {})
        on_txt = (("citas≠; " if ref.get("citas_difieren") else "")
                  + ("veredicto: " + ", ".join(ref.get("verdict_diffs") or []) or "—"))
        ctrl_txt = (("citas≠; " if r["citas_dif"] else "")
                    + ("veredicto: " + ", ".join(r["vdiffs"]) if r["vdiffs"] else
                       ("citas≠" if r["citas_dif"] else "idéntico")))
        L.append(f"| {r['qid']} | {on_txt} | {ctrl_txt} | "
                 f"{'✅ sí' if r['inestable'] else '❌ no (estable)'} |")
    L.append("")
    L.append("## Detalle de veredictos off-vs-off2")
    L.append("")
    for r in rows:
        L.append(f"**{r['qid']}** — inestable={r['inestable']}")
        for d in VERDICT_DIMS:
            if r["va"].get(d) != r["vb"].get(d):
                L.append(f"- {d}: A=`{r['va'].get(d)}` vs B=`{r['vb'].get(d)}`")
        if r["citas_dif"]:
            L.append(f"- citas A: {(r['a'].final_json or {}).get('citas')}")
            L.append(f"- citas B: {(r['b'].final_json or {}).get('citas')}")
        L.append("")
    REPORT_PATH.write_text("\n".join(L), encoding="utf-8")
    print(f"\nVeredicto del control: {'TODAS INESTABLES (equivalencia demostrada)' if all_unstable else 'HAY UNA ESTABLE — investigar'}")
    print(f"Reporte: {REPORT_PATH}")


if __name__ == "__main__":
    main()
