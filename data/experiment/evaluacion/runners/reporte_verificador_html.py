#!/usr/bin/env python3
"""reporte_verificador_html.py — Reporte HTML por corrida del verificador (Fase 2.4+).

Genera UN HTML autocontenido (CSS inline, sin JS, sin CDN — abre offline) por corrida:
    posthoc_run/reportes_html/<timestamp>_<run>_<label>/reporte.html
y regenera el index.html acumulado en posthoc_run/reportes_html/.

Uso:
    python reporte_verificador_html.py --input posthoc_run/calibracion_verificador_v4 \
        --run run_3 --label off [--ground-truth ../../.claude/.../casos_control.md]

- --ground-truth es OPCIONAL: si se pasa, cada falla muestra su GT junto a la atribución
  (modo calibración); si no, la columna no existe (modo pipeline real).
- Los casos con parse_ok=False NO se omiten: banner de advertencia + final_raw colapsable.
- Colapsado con <details>/<summary> nativo; colapsado por default salvo el encabezado.
"""
from __future__ import annotations

import argparse
import html
import json
import re
import subprocess
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]      # evaluacion/
sys.path.insert(0, str(BASE))

LADOS = ("grafo", "agente", "ninguno", "indeterminado")
LADO_COLOR = {"grafo": "#b45309", "agente": "#1d4ed8", "ninguno": "#6b7280",
              "indeterminado": "#7c3aed", "?": "#111827"}


def esc(x) -> str:
    return html.escape(str(x)) if x is not None else ""


CSS = """
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
     max-width:1100px;margin:2rem auto;padding:0 1rem;color:#1f2937;line-height:1.45;font-size:15px}
h1{font-size:1.3rem;margin-bottom:.2rem} h2{font-size:1.05rem}
.meta{color:#4b5563;font-size:.85rem;border:1px solid #e5e7eb;border-radius:6px;
      padding:.6rem .9rem;background:#f9fafb;margin-bottom:1.2rem}
.meta code{background:#eef2f7;padding:0 .25em;border-radius:3px}
details.falla{border:1px solid #d1d5db;border-radius:8px;margin:.8rem 0;background:#fff}
details.falla>summary{cursor:pointer;padding:.6rem .9rem;font-weight:600;list-style-position:inside}
details.falla[open]>summary{border-bottom:1px solid #e5e7eb}
details.falla>div{padding:.4rem 1rem 1rem}
details.sec{border:1px solid #e5e7eb;border-radius:6px;margin:.5rem 0}
details.sec>summary{cursor:pointer;padding:.35rem .7rem;font-weight:600;font-size:.9rem;background:#f9fafb}
details.sec>div{padding:.5rem .9rem}
.badge{display:inline-block;color:#fff;border-radius:4px;padding:.05rem .45rem;
       font-size:.75rem;font-weight:600;margin-left:.3rem;vertical-align:middle}
.chip{display:inline-block;background:#eef2f7;color:#374151;border-radius:4px;
      padding:.05rem .45rem;font-size:.75rem;margin-left:.3rem;vertical-align:middle}
.warn{background:#fee2e2;border:1px solid #ef4444;border-radius:6px;padding:.5rem .8rem;
      margin:.5rem 0;font-weight:600;color:#7f1d1d}
.gt{background:#ecfdf5;border:1px solid #10b981;border-radius:6px;padding:.5rem .8rem;
    margin:.5rem 0;font-size:.85rem;white-space:pre-wrap}
.gt b{color:#065f46}
blockquote.q{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.83rem;
             background:#f8fafc;border-left:3px solid #94a3b8;margin:.4rem 0;
             padding:.45rem .7rem;white-space:pre-wrap}
.ubic{color:#6b7280;font-size:.75rem;font-family:ui-monospace,SFMono-Regular,Menlo,monospace;margin-top:.25rem}
.pde{background:#fef3c7;border:1px solid #f59e0b;border-radius:6px;padding:.5rem .8rem;margin:.5rem 0}
.okconst{background:#ecfdf5;border:1px solid #10b981;border-radius:6px;padding:.5rem .8rem;margin:.5rem 0}
table{border-collapse:collapse;width:100%;font-size:.83rem;margin:.4rem 0}
th,td{border:1px solid #e5e7eb;padding:.3rem .5rem;text-align:left;vertical-align:top}
th{background:#f3f4f6}
td.mono, .mono{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.78rem}
pre.raw{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.75rem;
        white-space:pre-wrap;background:#f8fafc;border:1px solid #e5e7eb;padding:.6rem;border-radius:6px}
.stats{color:#4b5563;font-size:.83rem}
a{color:#1d4ed8}
"""


# --------------------------------------------------------------------------- #
# Insumos                                                                      #
# --------------------------------------------------------------------------- #
def git_commit() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=BASE,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception as e:
        return f"(no disponible: {type(e).__name__})"


def compute_namespace(run: str) -> str:
    """Namespace de caché reconstruido con el código ACTUAL (mismo cálculo que
    build_verificador_client). Si el código cambió desde la corrida, difiere — por eso
    el encabezado lo declara como 'calculado con el código actual'."""
    try:
        from loader import load_graph
        import llm_cache as lc
        import verificador
        kg = load_graph(run)
        return lc.make_namespace("verificador", code_ver=verificador.CODE_VER,
                                 graph_fp=lc.graph_fingerprint(kg), thinking=False)
    except Exception as e:
        return f"(no calculable: {type(e).__name__}: {e})"


def load_trace(run: str, label: str, qid: str) -> dict | None:
    p = BASE / "posthoc_run" / "traces" / label / run / f"{qid}.json"
    if p.exists():
        return json.load(open(p))[0]
    return None


def parse_ground_truth(path: Path) -> dict:
    """Extrae de casos_control.md (o similar) el bloque '**Atribución humana...**' por CQ."""
    txt = path.read_text(encoding="utf-8")
    out = {}
    for m in re.finditer(r"^###\s+(CQ-\d+)[^\n]*\n(.*?)(?=^###\s+CQ-|\Z)", txt, re.M | re.S):
        qid, body = m.group(1), m.group(2)
        g = re.search(r"^-\s+\*\*Atribuci[oó]n humana.*?(?=^-\s+\*\*Palanca|\Z)", body, re.M | re.S)
        out[qid] = g.group(0).strip() if g else None
    return out


# --------------------------------------------------------------------------- #
# Render                                                                       #
# --------------------------------------------------------------------------- #
def badge(atr: dict) -> str:
    lado = atr.get("lado") if atr.get("lado") in LADOS else "?"
    txt = f'{atr.get("categoria")} · {atr.get("jerarquia")}'
    return f'<span class="badge" style="background:{LADO_COLOR[lado]}">{esc(txt)}</span>'


def sec(titulo: str, inner: str, open_: bool = False) -> str:
    return (f'<details class="sec"{" open" if open_ else ""}><summary>{esc(titulo)}</summary>'
            f'<div>{inner}</div></details>')


def render_evidencia(ev: dict) -> str:
    L = []
    for pieza in ("afirmacion", "nodo", "fuente"):
        it = ev.get(pieza)
        if isinstance(it, dict):
            L.append(f"<div><b>{esc(pieza)}</b>"
                     f'<blockquote class="q">{esc(it.get("quote"))}'
                     f'<div class="ubic">↳ {esc(it.get("ubicacion"))}</div></blockquote></div>')
        elif it is not None:  # contrato viejo (string) — se muestra igual, marcado
            L.append(f"<div><b>{esc(pieza)}</b> <span class='chip'>formato string (contrato v3)</span>"
                     f'<blockquote class="q">{esc(it)}</blockquote></div>')
    return "".join(L)


def render_busquedas(bs: list) -> str:
    if not bs:
        return '<p class="stats">(sin búsquedas declaradas)</p>'
    rows = "".join(f'<tr><td class="mono">{esc(b.get("consulta"))}</td>'
                   f"<td>{esc(b.get('resultado'))}</td></tr>" for b in bs if isinstance(b, dict))
    return f"<table><tr><th>consulta</th><th>resultado</th></tr>{rows}</table>"


def render_atribucion(i: int, a: dict) -> str:
    L = [f"<h3 style='font-size:.95rem'>Atribución {i} {badge(a)}</h3>"]
    if a.get("pata"):
        L.append(f'<p class="stats">pata: {esc(a["pata"])}</p>')
    if a.get("categoria") == "frontera_no_determinada":
        L.append(f'<p><b>entre:</b> {esc(", ".join(a.get("entre") or []) or "(no declarado)")}<br>'
                 f'<b>evidencia faltante que decidiría el caso:</b> {esc(a.get("evidencia_faltante") or "(no declarada)")}</p>')
    L.append(render_evidencia(a.get("evidencia") or {}))
    L.append("<b>búsquedas</b>" + render_busquedas(a.get("busquedas") or []))
    return "".join(L)


def render_extraccion(et: dict) -> str:
    L = []
    tcs = et.get("tool_calls") or []
    if tcs:
        rows = "".join(
            f"<tr><td>{esc(t.get('paso'))}</td><td class='mono'>{esc(t.get('tool'))}</td>"
            f"<td class='mono'>{esc(t.get('args'))}</td><td>{esc(t.get('devolvio'))}</td>"
            f"<td>{'sí' if t.get('pertinente') else 'no'}</td></tr>"
            for t in tcs if isinstance(t, dict))
        L.append(f"<table><tr><th>paso</th><th>tool</th><th>args</th><th>devolvió</th>"
                 f"<th>pertinente</th></tr>{rows}</table>")
    pde = et.get("paso_decision_error")
    if isinstance(pde, dict) and (pde.get("quote") or pde.get("paso") is not None):
        L.append(f'<div class="pde"><b>Paso de la decisión que llevó al error — paso '
                 f'{esc(pde.get("paso"))}:</b><blockquote class="q">{esc(pde.get("quote"))}</blockquote></div>')
    else:
        dac = et.get("decision_agente_correcta")
        L.append('<div class="okconst"><b>Constatación: no hay paso de decisión erróneo del agente '
                 "(el agente actuó bien sobre lo que tenía)</b>"
                 + (f"<br>{esc(dac)}" if dac else "") + "</div>")
    td = et.get("thinking_decision")
    if td:
        L.append(f"<p><b>thinking en la decisión:</b></p><blockquote class='q'>{esc(td)}</blockquote>")
    patas = et.get("patas") or []
    if patas:
        L.append("<p><b>patas (según step1 del juez):</b></p><ul>"
                 + "".join(f"<li>{esc(p)}</li>" for p in patas) + "</ul>")
    return "".join(L)


def render_falla(qid: str, rec: dict, trace: dict | None, gt_text: str | None) -> tuple[str, Counter]:
    m = rec.get("_meta") or {}
    cs = m.get("contexto_stats") or {}
    ats = rec.get("atribuciones") or []
    lados = Counter((a.get("lado") if a.get("lado") in LADOS else "?") for a in ats)
    parse_ok = bool(m.get("parse_ok"))
    if not parse_ok:
        lados["rotos"] += 1

    badges = "".join(badge(a) for a in ats) or (
        '<span class="badge" style="background:#ef4444">⚠ sin JSON parseable</span>')
    conf = f'<span class="chip">confianza: {esc(rec.get("confianza") or "—")}</span>'
    cat = f'<span class="chip">{esc(cs.get("categoria") or (trace or {}).get("categoria") or "?")}</span>'
    head = f"<b>{esc(qid)}</b> {cat} {badges} {conf}"

    body = []
    if gt_text:
        body.append(f'<div class="gt"><b>Ground-truth (calibración) — verbatim de la fuente de GT:</b>\n'
                    f"{esc(gt_text)}</div>")
    if not parse_ok:
        body.append('<div class="warn">⚠ parse_ok=False — el JSON final del verificador es inválido. '
                    "El caso NO se omite: abajo está el final_raw íntegro.</div>")

    # b. pregunta + síntoma
    if trace:
        tr = trace.get("trace") or {}
        pregunta = tr.get("question") or "(sin pregunta en la traza)"
        verifs = ((trace.get("judge") or {}).get("step2") or {}).get("verificaciones") or []
        fallidos = [v for v in verifs if v.get("verdict") in ("falso", "no_soportado")]
        sint = "".join(f'<li>[{esc(v.get("verdict"))}{"/central" if v.get("central") else ""}] '
                       f"“{esc(v.get('enunciado'))}”</li>" for v in fallidos) or \
               "<li>(el juez no expuso afirmaciones desagregadas)</li>"
        body.append(sec("Pregunta y síntoma",
                        f"<p><b>{esc(pregunta)}</b></p><ul>{sint}</ul>"))
    else:
        body.append(sec("Pregunta y síntoma", "<p>(traza no encontrada en posthoc_run/traces/)</p>"))

    # c. extracción de traza
    et = rec.get("extraccion_traza")
    if isinstance(et, dict):
        body.append(sec("Extracción de traza (FASE A del verificador)", render_extraccion(et)))
    elif parse_ok:
        body.append(sec("Extracción de traza", "<p>(el output no trae extraccion_traza)</p>"))

    # d. atribuciones
    if ats:
        body.append(sec(f"Atribuciones ({len(ats)})",
                        "<hr style='border:none;border-top:1px solid #e5e7eb'>".join(
                            render_atribucion(i, a) for i, a in enumerate(ats))))

    # e. razonamiento
    if rec.get("razonamiento"):
        body.append(sec("Razonamiento del verificador",
                        f'<blockquote class="q">{esc(rec["razonamiento"])}</blockquote>'))

    # roto: final_raw íntegro
    if not parse_ok and m.get("final_raw"):
        body.append(sec("final_raw íntegro (caso roto)", f'<pre class="raw">{esc(m["final_raw"])}</pre>'))

    # f. stats
    stats = (f"tool calls del verificador: {m.get('tool_calls_used')} · tokens {m.get('tokens_in')} in / "
             f"{m.get('tokens_out')} out · latencia {m.get('latency_s')} s · "
             f"nodos vistos recuperados: {cs.get('n_seen')} · claims fallidos: {cs.get('n_claims_fallidos')}"
             + (f" · error: {esc(m.get('error'))}" if m.get("error") else ""))
    body.append(sec("Stats (_meta)", f'<p class="stats">{stats}</p>'))

    return (f'<details class="falla"><summary>{head}</summary><div>{"".join(body)}</div></details>',
            lados)


# --------------------------------------------------------------------------- #
# Index acumulado                                                              #
# --------------------------------------------------------------------------- #
def regenerate_index(root: Path) -> Path:
    metas = []
    for mj in sorted(root.glob("*/meta.json")):
        try:
            metas.append(json.loads(mj.read_text()))
        except Exception:
            continue
    metas.sort(key=lambda x: x.get("timestamp", ""), reverse=True)
    rows = []
    for x in metas:
        resumen = " · ".join(f"{k}: {v}" for k, v in (x.get("resumen_lados") or {}).items()) or "—"
        rows.append(f"<tr><td class='mono'>{esc(x.get('timestamp'))}</td><td>{esc(x.get('run'))}</td>"
                    f"<td>{esc(x.get('label'))}</td><td class='mono'>{esc(x.get('commit'))}</td>"
                    f"<td>{esc(x.get('n_fallas'))}</td><td>{esc(resumen)}</td>"
                    f"<td><a href='{esc(x.get('dir'))}/reporte.html'>reporte</a></td></tr>")
    doc = (f"<!DOCTYPE html><html lang='es'><head><meta charset='utf-8'>"
           f"<title>Reportes del verificador</title><style>{CSS}</style></head><body>"
           f"<h1>Reportes del verificador — índice acumulado</h1>"
           f"<p class='stats'>Regenerado: {datetime.now().isoformat(timespec='seconds')}. "
           f"Una fila por corrida; más reciente arriba.</p>"
           f"<table><tr><th>timestamp</th><th>run</th><th>label</th><th>commit</th>"
           f"<th>fallas</th><th>atribuciones por lado</th><th></th></tr>{''.join(rows)}</table>"
           f"</body></html>")
    p = root / "index.html"
    p.write_text(doc, encoding="utf-8")
    return p


# --------------------------------------------------------------------------- #
# Main                                                                         #
# --------------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser(description="Reporte HTML por corrida del verificador.")
    ap.add_argument("--input", required=True, help="directorio con los CQ-*.json del verificador")
    ap.add_argument("--run", required=True, help="run del grafo (p. ej. run_3)")
    ap.add_argument("--label", required=True, help="off|on (subcarpeta de posthoc_run/traces)")
    ap.add_argument("--ground-truth", default=None,
                    help="OPCIONAL: ruta a casos_control.md (o similar); agrega el GT por falla")
    args = ap.parse_args()

    indir = (BASE / args.input) if not Path(args.input).is_absolute() else Path(args.input)
    files = sorted(indir.glob("CQ-*.json"))
    if not files:
        raise SystemExit(f"Sin CQ-*.json en {indir}")

    gt = parse_ground_truth(Path(args.ground_truth)) if args.ground_truth else {}
    commit = git_commit()
    ns = compute_namespace(args.run)
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")

    root = BASE / "posthoc_run" / "reportes_html"
    outdir = root / f"{ts}_{args.run}_{args.label}"
    outdir.mkdir(parents=True, exist_ok=True)

    fallas_html, total_lados = [], Counter()
    for f in files:
        qid = f.stem
        rec = json.loads(f.read_text())
        trace = load_trace(args.run, args.label, qid)
        h, lados = render_falla(qid, rec, trace, gt.get(qid))
        fallas_html.append(h)
        total_lados.update(lados)

    gen_ts = datetime.now().isoformat(timespec="seconds")
    header = (f"<div class='meta'><b>Corrida del verificador</b><br>"
              f"generado: <code>{esc(gen_ts)}</code> · run: <code>{esc(args.run)}</code> · "
              f"label: <code>{esc(args.label)}</code> · commit: <code>{esc(commit)}</code><br>"
              f"namespace de caché (calculado con el código actual): <code>{esc(ns)}</code><br>"
              f"inputs: <code>{esc(str(indir))}</code> · {len(files)} fallas · "
              f"ground-truth: <code>{esc(args.ground_truth or '(sin GT — modo pipeline)')}</code></div>")

    doc = (f"<!DOCTYPE html><html lang='es'><head><meta charset='utf-8'>"
           f"<title>Verificador — {esc(args.run)}/{esc(args.label)} — {esc(ts)}</title>"
           f"<style>{CSS}</style></head><body>"
           f"<h1>Reporte del verificador — {esc(args.run)} / {esc(args.label)}</h1>"
           f"{header}{''.join(fallas_html)}"
           f"<p class='stats'>Fin del reporte. <a href='../index.html'>← índice de corridas</a></p>"
           f"</body></html>")
    out = outdir / "reporte.html"
    out.write_text(doc, encoding="utf-8")

    (outdir / "meta.json").write_text(json.dumps({
        "timestamp": ts, "run": args.run, "label": args.label, "commit": commit,
        "n_fallas": len(files), "resumen_lados": dict(total_lados),
        "dir": outdir.name, "inputs": str(indir), "namespace": ns,
        "ground_truth": args.ground_truth,
    }, ensure_ascii=False, indent=1), encoding="utf-8")

    idx = regenerate_index(root)
    print(f"reporte: {out}")
    print(f"index  : {idx}")


if __name__ == "__main__":
    sys.exit(main())
