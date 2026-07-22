#!/usr/bin/env python3
"""Genera un HTML de demo (trazas + outputs del juez) para mostrar en reunión.
Lee datos reales de frozen_run/ y trazas/ — sin transcripción manual."""
import json, html, glob, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def esc(x):
    return html.escape(str(x)) if x is not None else ""

# ---------- cargar preguntas (eval_set + dev) ----------
def load_questions():
    byid = {}
    for fn in ["queries/eval_set_v1.json", "queries/dev.json"]:
        try:
            d = json.load(open(os.path.join(BASE, fn)))
        except Exception:
            continue
        its = d if isinstance(d, list) else (d.get("queries") or d.get("preguntas") or list(d.values())[0])
        if isinstance(its, dict):
            its = list(its.values())
        for it in its:
            if isinstance(it, dict) and (it.get("qid") or it.get("id")):
                byid[it.get("qid") or it.get("id")] = it
    return byid

Q = load_questions()

def verdict_for(run, qid, rep):
    f = os.path.join(BASE, f"frozen_run/traces/{run}/{qid}.json")
    for r in json.load(open(f)):
        if r["rep"] == rep:
            return r
    return None

# ---------- traza manual (paso a paso) ----------
manual = json.load(open(os.path.join(BASE, "trazas/manual_run_1.json")))
trace = manual["trazas"][0]  # CQ-001

# ---------- selección de outputs del juez ----------
CASOS = [
    ("run_1", "CQ-002", 1, "Caso ✅ — respuesta correcta y completa"),
    ("run_1", "CQ-031", 1, "Caso ❌ — afirmación central falsa detectada"),
    ("run_1", "CQ-018", 1, "Caso ⚖️ — requiere adjudicación humana"),
    ("run_1", "CQ-038", 3, "Caso 🚫 — pregunta no respondible (abstención)"),
]

# =================== HTML ===================
parts = []
parts.append("""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Evaluación KG-RAG · Trazas y juez</title>
<style>
:root{
  --bg:#0f1117; --card:#1a1d27; --card2:#232735; --ink:#e6e8ee; --mut:#8b90a0;
  --acc:#6ea8fe; --green:#3fb950; --red:#f85149; --amber:#d29922; --line:#2b3040;
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);
  font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
.wrap{max-width:1040px;margin:0 auto;padding:32px 22px 80px}
h1{font-size:26px;margin:0 0 4px}
h2{font-size:20px;margin:48px 0 6px;padding-top:14px;border-top:1px solid var(--line)}
.sub{color:var(--mut);margin:0 0 8px}
.lead{color:var(--mut);max-width:760px}
code,.mono{font-family:"SF Mono",SFMono-Regular,Menlo,Consolas,monospace}
.card{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:20px 22px;margin:18px 0}
.q{font-size:17px;font-weight:600;margin:0 0 6px}
.pill{display:inline-block;font-size:11px;font-weight:600;letter-spacing:.3px;text-transform:uppercase;
  padding:3px 9px;border-radius:999px;margin:0 6px 6px 0;background:var(--card2);color:var(--mut)}
.pill.cat{background:#1f2a44;color:#9cc2ff}
.label{font-size:11px;text-transform:uppercase;letter-spacing:.5px;color:var(--mut);margin:14px 0 4px}
.ans{background:var(--card2);border-radius:8px;padding:12px 14px;border-left:3px solid var(--acc)}
.exp{background:#14241a;border-left:3px solid var(--green);border-radius:8px;padding:12px 14px}
.cite{font-size:13px;color:var(--mut)}
.cite b{color:var(--ink)}
/* steps */
.steps{margin:10px 0 0;padding:0;list-style:none;counter-reset:s}
.step{display:flex;gap:12px;padding:9px 0;border-bottom:1px dashed var(--line)}
.step:last-child{border-bottom:0}
.snum{flex:0 0 30px;height:30px;border-radius:8px;background:var(--card2);display:flex;align-items:center;
  justify-content:center;font-weight:700;color:var(--acc);font-size:13px}
.stool{font-family:"SF Mono",monospace;font-weight:600;color:#9cc2ff}
.sinput{color:var(--mut);font-family:"SF Mono",monospace;font-size:12.5px}
.sout{color:#7d8290;font-size:12px;margin-top:4px;font-family:"SF Mono",monospace;
  background:#0c0e14;border-radius:6px;padding:7px 9px;white-space:pre-wrap;word-break:break-word}
/* verdict grid */
.vgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px;margin:12px 0}
.vbox{background:var(--card2);border-radius:8px;padding:10px 12px}
.vbox .k{font-size:11px;text-transform:uppercase;letter-spacing:.4px;color:var(--mut)}
.vbox .v{font-size:16px;font-weight:700;margin-top:2px}
.v.ok{color:var(--green)} .v.bad{color:var(--red)} .v.warn{color:var(--amber)} .v.neu{color:var(--ink)}
.just{margin:10px 0 0}
.just .j{padding:8px 0;border-bottom:1px dashed var(--line)}
.just .j:last-child{border-bottom:0}
.just .jk{font-weight:600;color:#9cc2ff;font-size:13px}
.claims{margin:8px 0 0;padding:10px 12px;background:#241a1a;border-radius:8px;border-left:3px solid var(--amber)}
.claims ul{margin:6px 0 0;padding-left:18px}
.claims li{font-size:13px;color:#d8c9a0;margin:2px 0}
.meta{font-size:12px;color:var(--mut);margin-top:10px}
.adj-yes{color:var(--amber);font-weight:700}
.adj-no{color:var(--green);font-weight:600}
.note{font-size:13px;color:var(--mut);background:var(--card2);border-radius:8px;padding:10px 14px;margin:8px 0}
</style>
</head>
<body><div class="wrap">
""")

parts.append(f"""
<h1>Evaluación downstream KG-RAG — ejemplos</h1>
<p class="sub mono">FASE 2.3 · agente respondedor: claude-haiku-4-5 · juez: arquitectura de 2 pasos calibrada 12/12 vs. humano</p>
<p class="lead">El agente responde <i>competency questions</i> regulatorias usando el Knowledge Graph como herramienta
(tools <code>buscar_nodos</code>, <code>ver_nodo</code>, <code>ver_vecinos</code>). Un LLM-juez evalúa cada
respuesta contra ground truth verificado contra los PDFs del BCRA. Abajo: <b>una traza completa</b> del agente
navegando el grafo, y <b>cuatro veredictos del juez</b> que muestran el rango de casos.</p>
""")

# ---------------- TRAZA ----------------
parts.append('<h2>1 · Traza del agente — cómo razona sobre el grafo</h2>')
parts.append(f'<p class="lead">Pregunta <code>{esc(trace["qid"])}</code> sobre Run&nbsp;1. El agente encadena '
             f'{trace["tool_calls_used"]} llamadas a tools (búsqueda → inspección de nodos → vecinos) antes de responder.</p>')
parts.append('<div class="card">')
parts.append(f'<p class="q">{esc(trace["question"])}</p>')
parts.append('<div class="label">Cadena de razonamiento (tool calls)</div>')
parts.append('<ul class="steps">')
# mostrar pasos; incluir snippet de output solo en algunos para no saturar
show_out = {1, 3}
for s in trace["steps"]:
    inp = json.dumps(s["input"], ensure_ascii=False)
    out = ""
    if s["n"] in show_out:
        snip = s.get("output_truncado", "")[:420]
        out = f'<div class="sout">{esc(snip)}…</div>'
    parts.append(
        f'<li class="step"><div class="snum">{s["n"]}</div><div style="flex:1">'
        f'<span class="stool">{esc(s["tool"])}</span> '
        f'<span class="sinput">{esc(inp)}</span>{out}</div></li>'
    )
parts.append('</ul>')
fj = trace["final_json"]
parts.append('<div class="label">Respuesta final del agente</div>')
parts.append(f'<div class="ans">{esc(fj["respuesta"])}</div>')
cites = " · ".join(f'<b>{esc(c["source_doc"])}</b> {esc(c["location"])}' for c in fj.get("citas", []))
parts.append(f'<div class="cite" style="margin-top:8px">📄 {cites}</div>')
parts.append(f'<div class="meta">{trace["tool_calls_used"]} tool calls · '
             f'${trace["cost_usd"]:.4f} · {trace["latency_s"]:.1f}s</div>')
parts.append('</div>')

# ---------------- JUEZ ----------------
parts.append('<h2>2 · Outputs del juez — cuatro casos</h2>')
parts.append('<p class="lead">El juez emite veredicto estructurado por dimensiones (correctitud, completitud, '
             'precisión de cita), lista afirmaciones no soportadas separando <b>centrales</b> (núcleo de la respuesta) '
             'de <b>secundarias</b> (color), y marca cuándo escalar a <b>adjudicación humana</b>.</p>')

def vclass(dim, val):
    if val in ("correcta", "completa"): return "ok"
    if val in ("incorrecta",): return "bad"
    if val in ("parcial",): return "warn"
    return "neu"

for run, qid, rep, titulo in CASOS:
    r = verdict_for(run, qid, rep)
    q = Q.get(qid, {})
    v = r["verdict"] or {}
    parts.append('<div class="card">')
    parts.append(f'<div style="font-weight:700;font-size:13px;color:var(--mut);margin-bottom:8px">{esc(titulo)} · <span class="mono">{esc(qid)} / {esc(run)}</span></div>')
    parts.append(f'<p class="q">{esc(q.get("pregunta",""))}</p>')
    cat = q.get("categoria"); dif = q.get("dificultad")
    if cat: parts.append(f'<span class="pill cat">{esc(cat)}</span>')
    if dif: parts.append(f'<span class="pill">dificultad {esc(dif)}</span>')

    if q.get("respuesta_esperada"):
        parts.append('<div class="label">Respuesta esperada (ground truth)</div>')
        parts.append(f'<div class="exp">{esc(q["respuesta_esperada"])}</div>')

    parts.append('<div class="label">Respuesta del agente</div>')
    parts.append(f'<div class="ans">{esc(r["respuesta"])}</div>')
    cites = " · ".join(f'<b>{esc(c["source_doc"])}</b> {esc(c["location"])}' for c in r.get("citas", []))
    parts.append(f'<div class="cite" style="margin-top:8px">📄 {cites}</div>')

    # veredicto
    parts.append('<div class="label">Veredicto del juez</div>')
    parts.append('<div class="vgrid">')
    dims = [
        ("Correctitud", v.get("correctitud")),
        ("Completitud", v.get("completitud")),
        ("Abstención", v.get("abstencion")),
        ("Precisión cita", v.get("cita_precision")),
    ]
    for k, val in dims:
        if val is None:
            cls = "neu"; disp = "—"
        else:
            cls = vclass(k, val); disp = esc(val)
        parts.append(f'<div class="vbox"><div class="k">{k}</div><div class="v {cls}">{disp}</div></div>')
    parts.append('</div>')

    # afirmaciones no soportadas
    anc = v.get("afirmaciones_no_soportadas", {}) or {}
    cen = anc.get("centrales", []) or []
    sec = anc.get("secundarias", []) or []
    if cen or sec:
        parts.append('<div class="claims">')
        if cen:
            parts.append(f'<div style="color:var(--red);font-weight:600;font-size:13px">⚠ {len(cen)} afirmación(es) CENTRAL(es) no soportada(s):</div><ul>')
            for c in cen: parts.append(f'<li>{esc(c)}</li>')
            parts.append('</ul>')
        if sec:
            parts.append(f'<div style="color:var(--amber);font-weight:600;font-size:13px;margin-top:6px">{len(sec)} secundaria(s) no soportada(s):</div><ul>')
            for c in sec: parts.append(f'<li>{esc(c)}</li>')
            parts.append('</ul>')
        parts.append('</div>')

    # justificación
    just = v.get("justificacion", {}) or {}
    if just:
        parts.append('<div class="just">')
        for k in ["correctitud", "completitud", "citas", "abstencion"]:
            if just.get(k):
                parts.append(f'<div class="j"><span class="jk">{k}:</span> {esc(just[k])}</div>')
        parts.append('</div>')

    adj = v.get("requiere_adjudicacion_humana")
    badge = '<span class="adj-yes">⚖️ requiere adjudicación humana</span>' if adj else '<span class="adj-no">✓ veredicto automático</span>'
    parts.append(f'<div class="meta">{badge} · harness ${r.get("harness_cost",0):.4f} · juez ${r.get("judge_cost",0):.4f}</div>')
    parts.append('</div>')

parts.append('</div></body></html>')

out = os.path.join(BASE, "demo_evaluacion.html")
open(out, "w").write("\n".join(parts))
print("OK ->", out)
