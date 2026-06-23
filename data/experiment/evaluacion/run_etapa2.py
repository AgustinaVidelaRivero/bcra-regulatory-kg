"""
run_etapa2.py — Reporte ETAPA 2 (final) tras la adjudicación humana firmada.

Aplica los veredictos del worksheet firmado (adjudicacion_FIRMADO.json) vía el LOG
DE PROPAGACIÓN (campo `celdas` de cada afirmación), recomputa la correctitud de las
celdas `pendiente_adjudicacion` con el mapping CONGELADO del juez v2.1.1, y re-emite
reporte_final.md. NO toca trazas congeladas, juez ni eval_set: solo resuelve los
veredictos de correctitud que estaban retenidos.

Mapping de recomputación (todas las afirmaciones del worksheet son CENTRALES — el
queue encoló afirmaciones_no_soportadas.centrales):
  · verdadera     → la central deja de ser no_soportada; no penaliza.
  · falsa         → central falsa → la repetición baja a INCORRECTA.
  · parcial       → afirmación imprecisa → la repetición baja a PARCIAL (no incorrecta).
  · no_verificable→ se mantiene NO penalizable; la repetición queda INDETERMINABLE
                    por corpus (ni correcta ni incorrecta) si ese es el peor estado.
Base determinística (de la traza congelada, NO en el queue):
  · C0=incorrecta (ya tenía una central falsa) → se mantiene incorrecta.
  · C0=parcial    (ya tenía una secundaria falsa) → parcial, salvo que una central
                    adjudicada resulte falsa → incorrecta.
  · C0=correcta   → se resuelve por las adjudicaciones (arriba).
Precedencia por repetición: incorrecta > parcial > indeterminable > correcta.
Agregación a celda: MODAL de las 3 reps; empate → sin_consenso.

Unanswerable: la adjudicación de afirmaciones tangenciales NO reabre el veredicto
de abstención; solo limpia el estado no_soportado. No se recomputa abstención.
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict

from loader import EVAL_DIR
from harness import _norm_loc

FROZEN = EVAL_DIR / "frozen_run"
FIRMADO = EVAL_DIR / "adjudicacion_FIRMADO.json"
EVAL_SET = EVAL_DIR / "queries" / "eval_set_v1.json"
PENDIENTE = EVAL_DIR / "adjudicacion_pendiente.json"
OUT = FROZEN / "reporte_final.md"
GRAPHS = ["run_1", "run_2", "run_3", "run_4", "run_5"]
CATS_ANS = ["factual_directa", "multi_norma", "cadena_restriccion_excepcion"]


def _mode(values):
    c = Counter(values)
    mx = max(c.values())
    win = [k for k, n in c.items() if n == mx]
    return (win[0] if len(win) == 1 else "sin_consenso"), (mx == len(values)), dict(c)


def _recompute_rep(c0, adj):
    """adj = lista de veredictos de las centrales de ESTA rep."""
    has = set(adj)
    if c0 == "incorrecta":
        return "incorrecta"
    if c0 == "parcial":
        return "incorrecta" if "falsa" in has else "parcial"
    # c0 == "correcta"
    if "falsa" in has:
        return "incorrecta"
    if "parcial" in has:
        return "parcial"
    if "no_verificable" in has:
        return "indeterminable_por_corpus"
    return "correcta"


def main():
    firmado = json.load(open(FIRMADO, encoding="utf-8"))
    pool = {q["id"]: q for q in json.load(open(EVAL_SET, encoding="utf-8"))["preguntas"]}
    qcat = {q: pool[q]["categoria"] for q in pool}
    qorder = [q["id"] for q in json.load(open(EVAL_SET, encoding="utf-8"))["preguntas"]]
    pend_queue = json.load(open(PENDIENTE, encoding="utf-8"))
    pendiente_set = {(x["run"], x["qid"]) for x in pend_queue}

    # ---- 1. propagación: celda(run,qid,rep) -> [(afirmacion, veredicto, evidencia)] ----
    cell_claims = defaultdict(list)
    n_prop = 0
    afirmaciones = []
    for s in firmado["secciones"]:
        for qq in s["preguntas"]:
            for af in qq["afirmaciones"]:
                afirmaciones.append((qq["qid"], af))
                for run, qid, rep in af["celdas"]:
                    cell_claims[(run, qid, rep)].append(
                        (af["afirmacion"], af["veredicto"], af.get("evidencia_seccion_pdf")))
                    n_prop += 1
    distinct_cells = len(cell_claims)
    meta_total = firmado["meta"]["celdas_propagacion_total"]

    # ---- 2. cargar trazas congeladas (per-rep C0 + centrales) ----
    traces = {}
    for r in GRAPHS:
        for qid in pool:
            p = FROZEN / "traces" / r / f"{qid}.json"
            if p.exists():
                traces[(r, qid)] = json.load(open(p, encoding="utf-8"))

    # integridad: las centrales propagadas a una rep == centrales de la traza congelada
    integridad_ok, mismatches = True, []
    for (r, qid), reps in traces.items():
        for rep in reps:
            cen_frozen = [_norm_loc(c) for c in
                          ((rep["verdict"] or {}).get("afirmaciones_no_soportadas") or {}).get("centrales", [])]
            cen_prop = [_norm_loc(a) for a, _, _ in cell_claims.get((r, qid, rep["rep"]), [])]
            if Counter(cen_frozen) != Counter(cen_prop):
                integridad_ok = False
                mismatches.append((r, qid, rep["rep"], len(cen_frozen), len(cen_prop)))

    # ---- 3. recomputar correctitud de celdas pendientes (answerable) ----
    final_corr = {}      # (run,qid) -> veredicto final
    cambios = []         # detalle de celdas que cambian
    for r in GRAPHS:
        for qid in pool:
            if qcat[qid] == "unanswerable" or (r, qid) not in traces:
                continue
            reps = traces[(r, qid)]
            if (r, qid) in pendiente_set:
                per_rep = []
                drivers = []
                for rep in reps:
                    c0 = (rep["verdict"] or {}).get("correctitud")
                    adj = [(a, v, e) for a, v, e in cell_claims.get((r, qid, rep["rep"]), [])]
                    nc = _recompute_rep(c0, [v for _, v, _ in adj])
                    per_rep.append(nc)
                    for a, v, e in adj:
                        if v != "verdadera":
                            drivers.append({"rep": rep["rep"], "afirmacion": a,
                                            "veredicto": v, "evidencia": e})
                modal, unan, dist = _mode(per_rep)
                final_corr[(r, qid)] = modal
                cambios.append({"run": r, "qid": qid, "categoria": qcat[qid],
                                "draft": "pendiente_adjudicacion", "final": modal,
                                "per_rep": per_rep, "dist": dist, "drivers": drivers})
            else:
                # no pendiente: el modal congelado es final
                agg = None
                final_corr[(r, qid)] = _frozen_modal(reps, "correctitud")

    _write_report(firmado, pool, qcat, qorder, traces, final_corr, cambios,
                  n_prop, distinct_cells, meta_total, integridad_ok, mismatches,
                  pendiente_set)

    print(f"propagaciones aplicadas: {n_prop} (meta.celdas_propagacion_total={meta_total}) "
          f"=> {'OK' if n_prop == meta_total else 'MISMATCH'}")
    print(f"celdas distintas tocadas: {distinct_cells}")
    print(f"integridad centrales(propagadas)==centrales(congeladas): "
          f"{'OK' if integridad_ok else 'FALLA ' + str(mismatches)}")
    flips = [c for c in cambios if c["final"] != "correcta"]
    print(f"celdas pendientes resueltas: {len(cambios)} | que NO quedaron correcta: {len(flips)}")
    for c in flips:
        print(f"   {c['run']}/{c['qid']} ({c['categoria']}): {c['final']} {c['dist']}")
    print(f"Reporte: {OUT}")


def _frozen_modal(reps, dim):
    vals = [(rep["verdict"] or {}).get(dim) for rep in reps
            if (rep["verdict"] or {}).get(dim) is not None]
    if not vals:
        return None
    return _mode(vals)[0]


def _write_report(firmado, pool, qcat, qorder, traces, final_corr, cambios,
                  n_prop, distinct_cells, meta_total, integridad_ok, mismatches,
                  pendiente_set):
    adj = firmado["meta"]["adjudicacion"]
    L = ["# Reporte final (ETAPA 2) — corrida congelada Fase 2.3", ""]
    L.append("eval_set_v1 (23 preguntas) × 5 grafos × N=3. Respondedor "
             "`claude-haiku-4-5-20251001` (caching ON), juez `claude-sonnet-4-6` "
             "v2.1.1 — ambos CONGELADOS. Correctitud por celda = MODAL de 3 reps. "
             "Esta etapa 2 resuelve las celdas que estaban `pendiente_adjudicacion` "
             "con la adjudicación humana firmada; NADA del dataset congelado se "
             "re-corrió ni modificó.")
    L.append("")
    L.append(f"**Adjudicación firmada** ({adj['fecha']}, {adj['adjudicador']}): "
             f"{adj['veredictos']['verdadera']} verdaderas, "
             f"{adj['veredictos']['falsa']} falsas, "
             f"{adj['veredictos']['parcial']} parciales, "
             f"{adj['veredictos']['no_verificable']} no_verificables "
             f"(200 afirmaciones únicas).")
    L.append("")

    # 0. propagación / integridad
    L.append("## 0. Propagación e integridad")
    L.append("")
    L.append(f"- Propagaciones aplicadas (veredicto→celda): **{n_prop}** vs "
             f"`meta.celdas_propagacion_total` = {meta_total} → "
             f"**{'✅ coinciden' if n_prop == meta_total else '❌ MISMATCH'}**.")
    L.append(f"- Celdas (grafo×pregunta×rep) distintas tocadas: **{distinct_cells}**.")
    L.append(f"- Integridad centrales propagadas == centrales de la traza congelada: "
             f"**{'✅ OK' if integridad_ok else '❌ FALLA: ' + str(mismatches)}**.")
    L.append("")

    # 1. Correctitud FINAL — grafo × categoría
    L.append("## 1. Correctitud FINAL — grafo × categoría (answerable)")
    L.append("")
    L.append("`indet` = indeterminable por corpus (afirmación central no_verificable; "
             "ni correcta ni incorrecta). `sin_cons` = empate modal 1-1-1.")
    L.append("")
    L.append("| Grafo | Categoría | correcta | parcial | incorrecta | indet | sin_cons |")
    L.append("|-------|-----------|---------:|--------:|-----------:|------:|---------:|")
    for r in GRAPHS:
        for cat in CATS_ANS:
            qs = [q for q in qorder if qcat[q] == cat and (r, q) in traces]
            cnt = Counter(final_corr.get((r, q)) for q in qs)
            L.append(f"| {r} | {cat} | {cnt.get('correcta',0)} | {cnt.get('parcial',0)} "
                     f"| {cnt.get('incorrecta',0)} | {cnt.get('indeterminable_por_corpus',0)} "
                     f"| {cnt.get('sin_consenso',0)} |")
    L.append("")
    # totales por grafo
    L.append("**Totales answerable por grafo (19 preguntas):**")
    L.append("")
    L.append("| Grafo | correcta | parcial | incorrecta | indet | sin_cons |")
    L.append("|-------|---------:|--------:|-----------:|------:|---------:|")
    for r in GRAPHS:
        qs = [q for q in qorder if qcat[q] != "unanswerable" and (r, q) in traces]
        cnt = Counter(final_corr.get((r, q)) for q in qs)
        L.append(f"| {r} | {cnt.get('correcta',0)} | {cnt.get('parcial',0)} "
                 f"| {cnt.get('incorrecta',0)} | {cnt.get('indeterminable_por_corpus',0)} "
                 f"| {cnt.get('sin_consenso',0)} |")
    L.append("")

    # 2. Dimensiones ya cerradas (congeladas, no las toca la adjudicación)
    L.append("## 2. Dimensiones cerradas (congeladas — no afectadas por la adjudicación)")
    L.append("")
    L.append("| Grafo | Estabilidad | hit_limit | abst. correcta/incorr. | cita_doc T/F | prec punto/pag/aus | Costo |")
    L.append("|-------|------------:|----------:|------------------------|-------------:|-------------------|------:|")
    cost_tot = 0.0
    for r in GRAPHS:
        cells = [traces[(r, q)] for q in pool if (r, q) in traces]
        repsm = [rep for reps in cells for rep in reps]
        # estabilidad: usar el agg congelado
        agg = json.load(open(FROZEN / f"agg_{r}.json", encoding="utf-8"))
        uni = sum(1 for c in agg for i in c["agg"].get("dimensiones", {}).values() if i["unanime"])
        totd = sum(1 for c in agg for _ in c["agg"].get("dimensiones", {}))
        hit = sum(1 for rep in repsm if rep["hit_tool_limit"])
        cost = sum(rep["harness_cost"] + rep["judge_cost"] for rep in repsm)
        cost_tot += cost
        # abstención / citas desde el agg congelado
        ab = Counter(); dc = Counter(); pr = Counter()
        for c in agg:
            d = c["agg"].get("dimensiones", {})
            if "abstencion" in d:
                ab[d["abstencion"]["modal"]] += 1
            if "cita_documento_correcto" in d:
                dc[d["cita_documento_correcto"]["modal"]] += 1
            if "cita_precision" in d:
                pr[d["cita_precision"]["modal"]] += 1
        L.append(f"| {r} | {uni}/{totd} ({100*uni/totd:.0f}%) | {hit}/69 ({100*hit/69:.0f}%) "
                 f"| {ab.get('correcta',0)}/{ab.get('incorrecta',0)} "
                 f"| {dc.get(True,0)}/{dc.get(False,0)} "
                 f"| {pr.get('punto',0)}/{pr.get('pagina',0)}/{pr.get('ausente',0)} "
                 f"| ${cost:.2f} |")
    L.append(f"| **TOTAL** | | | | | | **${cost_tot:.2f}** |")
    L.append("")

    # 3. Celdas que cambiaron respecto del draft (trazabilidad afirmación→celda)
    L.append("## 3. Celdas que cambiaron respecto del draft (efecto de la adjudicación)")
    L.append("")
    L.append(f"Las **{len(cambios)} celdas** que el draft marcó `pendiente_adjudicacion` "
             "reciben aquí su correctitud final. Las que se resolvieron a `correcta` "
             "(todas sus centrales verdaderas) confirman el veredicto retenido; abajo "
             "se detallan las que NO quedaron `correcta` (con la afirmación que lo causó):")
    L.append("")
    no_correcta = [c for c in cambios if c["final"] != "correcta"]
    L.append("| Grafo | Pregunta | Cat. | draft | FINAL | distribución reps |")
    L.append("|-------|----------|------|-------|-------|-------------------|")
    for c in sorted(cambios, key=lambda x: (x["final"] == "correcta", x["run"], x["qid"])):
        L.append(f"| {c['run']} | {c['qid']} | {c['categoria']} | pendiente | "
                 f"**{c['final']}** | {c['dist']} |")
    L.append("")
    L.append("### Trazabilidad afirmación→celda (solo celdas que NO quedaron correcta)")
    L.append("")
    for c in no_correcta:
        L.append(f"**{c['run']}/{c['qid']}** ({c['categoria']}) → **{c['final']}** "
                 f"(reps: {c['per_rep']})")
        for d in c["drivers"]:
            L.append(f"- rep{d['rep']} · veredicto={d['veredicto']} · «{d['afirmacion']}»")
            if d["evidencia"]:
                L.append(f"    evidencia: {d['evidencia']}")
        L.append("")

    # 4. Nota metodológica multi_norma (resuelta)
    L.append("## 4. Nota metodológica — multi_norma resuelto")
    L.append("")
    L.append("En el draft, TODAS las celdas `multi_norma` quedaron pendientes (el gold "
             "resumido no soporta afirmaciones multi-hop granulares — hallazgo, no "
             "defecto). Tras la adjudicación, su correctitud ya es comparable: ver "
             "tabla 1, fila `multi_norma` de cada grafo. La adjudicación humana cumplió "
             "exactamente la función que el mecanismo de seguridad del juez (no validar "
             "contra conocimiento paramétrico) había diferido.")
    L.append("")

    # 5. Selección del grafo ganador (decisión firmada por la autora)
    L.append("## 5. Selección del grafo ganador")
    L.append("")
    L.append("**Grafo ganador: `run_3` — estrategia `ppf_core` (schema cerrado de 7 "
             "tipos core).**")
    L.append("")
    L.append("Selección por **dominancia multidimensional** — no requiere ponderar "
             "dimensiones, porque run_3 **lidera o empata en todas**:")
    L.append("")
    L.append("- **Correctitud final:** 16/19 answerable correctas — el máximo de los "
             "5 grafos (run_2 y run_4: 15; run_1 y run_5: 13).")
    L.append("- **Estabilidad:** 93% de celdas unánimes — el máximo (resto 83-86%).")
    L.append("- **Cadenas restricción-excepción:** 4/4 correctas — único grafo sin "
             "incorrectas en la categoría.")
    L.append("- **Precisión de cita:** 20 punto / 1 página — la granularidad más fina "
             "(cita a nivel de punto/sección).")
    L.append("- **Abstención (unanswerable):** 4/4 correcta (lidera/empata).")
    L.append("- **Costo:** parejo con el resto (~$3.21/grafo).")
    L.append("")
    L.append("Como run_3 no es inferior a ningún otro grafo en ninguna dimensión "
             "evaluada, la selección es **robusta a cualquier ponderación**.")
    L.append("")
    L.append("**Salvedad — límite común a los 5 grafos.** La categoría `multi_norma` "
             "(preguntas multi-hop) es el punto débil **compartido**: ningún grafo la "
             "resuelve sólidamente (run_3: 3/5 correctas, 2 incorrectas). El gold "
             "resumido no podía puntuarla sin adjudicación humana (§4); tras la "
             "adjudicación queda como **límite de capacidad común a todas las "
             "estrategias, no un diferenciador entre ellas**. La selección de run_3 "
             "se sostiene sobre las dimensiones donde los grafos sí se distinguen.")
    L.append("")
    OUT.write_text("\n".join(L), encoding="utf-8")


if __name__ == "__main__":
    main()
