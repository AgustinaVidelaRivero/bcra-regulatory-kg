"""
run_frozen.py — Pipeline de la corrida congelada (Fase 2.3).

Diseño (spec firmada):
  eval_set_v1 (23 preguntas) × 5 grafos × N repeticiones (N parametrizable, def 3).
  Caching ON. Orden fijo de grafos run_1→run_5; orden fijo de preguntas.

Agregación:
  Veredicto por celda (pregunta×grafo×dimensión) = MODAL de las N repeticiones.
  La distribución completa se persiste siempre. Estabilidad por grafo = % de celdas
  con veredicto unánime. Empate modal → celda 'sin_consenso' (a revisión humana; NO
  se inventa desempate).

Checkpoints:
  Se procesa UN grafo por invocación (--mode graph --graph run_X). Al terminar el
  grafo se frena y se escribe un checkpoint; el operador revisa y re-invoca para el
  siguiente. Los checkpoints detectan fallas técnicas; no ajustan nada.

Política de errores:
  Infra (timeout/529/rate limit) → retry hasta 3 con backoff exponencial, logueado.
  parse_error o corte por max_tokens en la respuesta final → NO se reintenta: es
  comportamiento del sistema bajo evaluación, se registra como traza fallida.

Ceguera del juez: el payload del juez se audita para que no filtre identidad del run.

Cola de adjudicación: trazas con afirmaciones CENTRALES no_soportadas → se acumulan
  en evaluacion/adjudicacion_pendiente.json con pregunta + afirmaciones + citas.

NO ejecutar sobre el eval_set hasta orden explícita. El modo `smoke` valida la
maquinaria con 2 preguntas del dev_pool × run_3 × N=2 (sin tocar el eval_set).

CHANGELOG / rulings:
  2026-06-10 — Fix de la capa de REPORTING (no del sistema bajo evaluación).
    Distinción que aplica este ruling: el SISTEMA BAJO EVALUACIÓN (harness, juez,
    eval_set — congelados por commit) NO se toca bajo ninguna circunstancia. La
    CAPA DE REPORTING (generación de checkpoints) es instrumentación de lectura:
    se puede corregir con registro, y este fix NO toca ni produce datos de
    evaluación. Bug corregido: el selector de "traza más conflictiva" en el
    checkpoint usaba el conteo de celdas `sin_consenso` (empates 1-1-1); cuando
    todos los desacuerdos son splits 2-1, ese conteo es 0 y devolvía la primera
    celda (en run_1 imprimió CQ-002 dos veces). Nuevo selector: la celda con más
    dimensiones NO unánimes (sin_consenso incluido). Rige para los 5 checkpoints;
    el de run_1 se regeneró desde `agg_run_1.json` persistido (modo `regen`), sin
    re-correr el modelo ni alterar un solo dato. La política de "re-correr desde
    cero" aplica a bugs de INFRAESTRUCTURA que afectan datos; este no lo es.
  2026-06-10 — Limitación descubierta: run_frozen DESCARTA los steps de tool calls.
    Hallazgo: el QuestionTrace del harness captura en memoria `steps` (cada tool
    call con input + output truncado) y `seen_provenances`, pero evaluate_cell
    arma el rep dict con un subconjunto que NO los incluye, y el objeto se
    descarta. Las trazas congeladas (frozen_run/traces/) solo guardan respuesta
    final + veredicto + metadata; la trayectoria por repetición no es recuperable.
    (Las trazas del loop MANUAL — trazas/manual_run_*.json — sí tienen steps, pero
    son del dev_pool, no del eval_set.)
    DECISIÓN (autora): NO se agrega persistencia de steps a runs 4-5 a mitad de
    corrida. Motivación: la corrida congelada debe producir datos UNIFORMES en los
    5 grafos; como los steps de run_1-3 son irrecuperables, la única uniformidad
    alcanzable es SIN steps. Agregarlos a 4-5 rompería la simetría forense entre
    grafos. No se toca el pipeline para esto.
    MITIGACIÓN — protocolo post-hoc: la lectura de trayectorias se hará tras el
    cierre, con una pasada DIRIGIDA de re-corridas de celdas seleccionadas con
    logging completo, sobre cualquier grafo, etiquetadas como ILUSTRATIVAS y FUERA
    del dataset congelado (no entran a los agregados ni a la comparación).

TAREAS POST-CORRIDA:
  - Agregar persistencia de steps (y seen_provenances) a run_frozen para usos
    futuros: la FASE DE ESCALADO (corpus completo / más grafos) la va a necesitar
    para forensics de trayectoria sin re-correr. Fix documentado: en evaluate_cell,
    incluir en el rep dict `"steps": tr.steps` y `"seen_provenances":
    tr.seen_provenances` (o, mejor, volcarlos a un archivo aparte por repetición
    para no inflar el agregado). NO aplicar sobre el dataset congelado actual — es
    para la próxima corrida desde cero.
  - INSTRUMENTACIÓN COMPLETA (auditoría del mentor, ver 04_auditoria_instrumentacion.md).
    El harness de RE-CORRIDAS POST-HOC e iteración (y la fase de escalado) debe
    PERSISTIR TODO POR DEFECTO — de acá en adelante. Lo que la corrida congelada
    descartó NO se recupera re-corriendo el dataset congelado (eso lo cambiaría):
    se obtiene en la capa post-hoc dirigida ya prevista. A persistir por llamada:
      · Agente: response crudo completo (content[] sin reducir), steps con outputs
        de tool SIN truncar, stop_reason, y thinking si se habilita.
      · Juez: Paso 1 completo (afirmaciones_verificables, reportes_de_alcance,
        patas_de_la_pregunta) y Paso 2 completo (verificaciones por-afirmación con
        su verdict, cobertura_patas por-pata, texto crudo de ambas llamadas), y
        thinking si se habilita.
      · Tokens: desglose por llamada (input / output / cache_read / cache_write),
        no solo el costo en USD.
    CONFIG de la fase post-hoc: se HABILITARÁ thinking en agente y juez (en la
    corrida congelada no se generó por estar deshabilitado; eso queda intacto).
    NO implementar nada de esto ahora: el camino crítico es worksheet de
    adjudicación → adjudicación humana contra PDFs → reporte etapa 2 → ganador.
"""

from __future__ import annotations

import argparse
import json
import random
import time
from collections import Counter, defaultdict
from pathlib import Path

from dotenv import load_dotenv

from loader import load_graph, EVAL_DIR
from harness import GraphAgent
import judge

GRAPH_ORDER = ["run_1", "run_2", "run_3", "run_4", "run_5"]
EVAL_SET = EVAL_DIR / "queries" / "eval_set_v1.json"
DEV_POOL = EVAL_DIR / "queries" / "dev_pool.json"
FROZEN_DIR = EVAL_DIR / "frozen_run"
SMOKE_DIR = EVAL_DIR / "frozen_smoke"
ADJ_QUEUE = EVAL_DIR / "adjudicacion_pendiente.json"

VERDICT_DIMS = ["correctitud", "completitud", "cita_documento_correcto",
                "cita_precision", "abstencion", "especulacion_en_prosa"]
# Precios (USD/MTok)
HAIKU_IN, HAIKU_OUT = 1.00, 5.00
SONNET_IN, SONNET_OUT = 3.00, 15.00
CACHE_W, CACHE_R = 1.25, 0.10


# --------------------------------------------------------------------------- #
# Cliente con retry de infraestructura (logueado)                              #
# --------------------------------------------------------------------------- #
class _RetryingMessages:
    def __init__(self, real, log, max_retries=3, base=2.0):
        self._real = real
        self._log = log
        self._max = max_retries
        self._base = base

    def create(self, **kwargs):
        import anthropic
        infra = (anthropic.RateLimitError, anthropic.APITimeoutError,
                 anthropic.APIConnectionError, anthropic.InternalServerError,
                 anthropic.APIStatusError)
        for attempt in range(self._max + 1):
            try:
                return self._real.messages.create(**kwargs)
            except infra as e:
                status = getattr(e, "status_code", None)
                # Solo reintentar infra retryable (429/5xx/timeout/conexión).
                retryable = isinstance(e, (anthropic.RateLimitError,
                                           anthropic.APITimeoutError,
                                           anthropic.APIConnectionError,
                                           anthropic.InternalServerError)) \
                    or (status is not None and status >= 500)
                if not retryable or attempt == self._max:
                    self._log({"event": "infra_fail", "attempt": attempt + 1,
                               "error": f"{type(e).__name__}: {e}", "status": status})
                    raise
                delay = round(self._base ** attempt + random.uniform(0, 0.5), 2)
                self._log({"event": "retry", "attempt": attempt + 1,
                           "error": f"{type(e).__name__}", "status": status,
                           "sleep_s": delay})
                time.sleep(delay)


class RetryingClient:
    def __init__(self, real, log):
        self._real = real
        self.messages = _RetryingMessages(real, log)


# --------------------------------------------------------------------------- #
# Ceguera del juez — auditoría del payload                                     #
# --------------------------------------------------------------------------- #
_CAPTURE = {"on": False, "payloads": []}
_JUDGE_CALL_ORIG = judge._call


def _spy_call(client, system, payload, max_tokens):
    if _CAPTURE["on"]:
        _CAPTURE["payloads"].append(payload)
    return _JUDGE_CALL_ORIG(client, system, payload, max_tokens)


judge._call = _spy_call  # intercepta SIEMPRE; solo captura cuando _CAPTURE['on']

FORBIDDEN = {
    "run_keys": ["run_1", "run_2", "run_3", "run_4", "run_5"],
    "graph_names": ["cookbook", "papers", "ppf_core", "schema_light", "hybrid"],
    "paths": ["kg.json", "source_kg", "data/experiment", "/run_", "frozen_"],
    "node_id_prefixes": ["Obligacion_", "TextoOrdenado_", "Restriccion_",
                         "Operacion_", "Comunicacion_", "Concepto_", "con_",
                         "ope_", "req_", "rsj_", "cla_", "ins_"],
}


def audit_blindness(payloads):
    """Escanea los payloads REALES enviados al juez en busca de identidad del run."""
    findings = {k: [] for k in FORBIDDEN}
    blob = json.dumps(payloads, ensure_ascii=False)
    blob_low = blob.lower()
    for cat, toks in FORBIDDEN.items():
        for t in toks:
            hay = (t.lower() in blob_low) if cat != "node_id_prefixes" else (t in blob)
            if hay:
                findings[cat].append(t)
    # claves de top-level de cada payload (para mostrar la superficie expuesta)
    keys = sorted({k for p in payloads if isinstance(p, dict) for k in p})
    return {"findings": findings, "payload_keys": keys, "n_payloads": len(payloads)}


# --------------------------------------------------------------------------- #
# Self-test sintético del RetryingClient (no usa API real)                     #
# --------------------------------------------------------------------------- #
def selftest_retry():
    """Inyecta errores de infra simulados y verifica backoff exponencial, logueo
    de cada intento, rendición al 3er fallo, y registro de traza fallida-por-infra.
    Devuelve (passed, summary_line, checks)."""
    import anthropic
    import httpx
    req = httpx.Request("POST", "https://api.anthropic.com/v1/messages")

    def mk(cls, status):
        return cls("synthetic", response=httpx.Response(status, request=req), body=None)
    mk429 = lambda: mk(anthropic.RateLimitError, 429)
    mk529 = lambda: mk(anthropic.InternalServerError, 529)
    mktimeout = lambda: anthropic.APITimeoutError(request=req)
    mk400 = lambda: mk(anthropic.BadRequestError, 400)

    class FakeMsgs:
        def __init__(self, seq):
            self.seq = list(seq)
            self.calls = 0

        def create(self, **kw):
            self.calls += 1
            if self.seq:
                exc = self.seq.pop(0)
                if exc is not None:
                    raise exc
            return {"ok": True}

    class FakeClient:
        def __init__(self, msgs):
            self.messages = msgs

    orig_sleep = time.sleep
    time.sleep = lambda s: None   # backoff sin demora real; el delay se loguea igual
    checks = []
    try:
        # A: 429 persistente -> 3 retries + rendición, raise
        log = []
        fm = FakeMsgs([mk429() for _ in range(10)])
        rc = RetryingClient(FakeClient(fm), lambda e: log.append(e))
        raised = False
        try:
            rc.messages.create(model="x", max_tokens=1, messages=[])
        except anthropic.RateLimitError:
            raised = True
        retry_logs = [e for e in log if e["event"] == "retry"]
        fail_logs = [e for e in log if e["event"] == "infra_fail"]
        checks.append(("429 persistente: 3 retries + rendición + raise",
                       raised and fm.calls == 4 and len(retry_logs) == 3 and len(fail_logs) == 1))
        # B: backoff exponencial creciente (delays logueados ~1,2,4)
        delays = [e["sleep_s"] for e in retry_logs]
        checks.append(("backoff exponencial creciente",
                       len(delays) == 3 and delays[0] < delays[1] < delays[2] and delays[1] >= 1.99))
        # C: 529 y timeout también reintentan 3x
        for name, mker in [("529", mk529), ("timeout", mktimeout)]:
            log = []
            fm = FakeMsgs([mker() for _ in range(10)])
            rc = RetryingClient(FakeClient(fm), lambda e: log.append(e))
            try:
                rc.messages.create(model="x", max_tokens=1, messages=[])
            except Exception:
                pass
            checks.append((f"{name} reintenta 3x",
                           fm.calls == 4 and sum(1 for e in log if e["event"] == "retry") == 3))
        # D: transitorio (2 fallos) -> éxito
        log = []
        fm = FakeMsgs([mk429(), mk529()])
        rc = RetryingClient(FakeClient(fm), lambda e: log.append(e))
        r = rc.messages.create(model="x", max_tokens=1, messages=[])
        checks.append(("transitorio (2 fallos) -> éxito",
                       r == {"ok": True} and fm.calls == 3
                       and sum(1 for e in log if e["event"] == "retry") == 2))
        # D2: 400 (no infra) NO se reintenta
        log = []
        fm = FakeMsgs([mk400() for _ in range(5)])
        rc = RetryingClient(FakeClient(fm), lambda e: log.append(e))
        try:
            rc.messages.create(model="x", max_tokens=1, messages=[])
        except anthropic.BadRequestError:
            pass
        checks.append(("400 NO se reintenta (1 sola llamada)",
                       fm.calls == 1 and sum(1 for e in log if e["event"] == "retry") == 0))
        # E: ask() registra la traza como fallida-por-infra
        kg = load_graph("run_3")
        fm = FakeMsgs([mk429() for _ in range(50)])
        rc = RetryingClient(FakeClient(fm), lambda e: None)
        ag = GraphAgent(kg, client=rc, cache_conversation=True)
        tr = ag.ask("SELFTEST", "¿pregunta de prueba?")
        checks.append(("ask() registra traza fallida-por-infra",
                       tr.error is not None and "RateLimitError" in (tr.error or "")
                       and not tr.parse_ok))
    finally:
        time.sleep = orig_sleep

    passed = all(ok for _, ok in checks)
    summary = (f"self-test retry: {'PASS' if passed else 'FAIL'} "
               f"({sum(1 for _, ok in checks if ok)}/{len(checks)} checks)")
    return passed, summary, checks


# --------------------------------------------------------------------------- #
# Evaluación + agregación                                                      #
# --------------------------------------------------------------------------- #
def _harness_cost(tr):
    return round((tr.tokens_in * HAIKU_IN + tr.cache_write * HAIKU_IN * CACHE_W
                  + tr.cache_read * HAIKU_IN * CACHE_R) / 1e6
                 + tr.tokens_out * HAIKU_OUT / 1e6, 6)


def _judge_cost(usage):
    return round(usage["in"] * SONNET_IN / 1e6 + usage["out"] * SONNET_OUT / 1e6, 6)


def evaluate_cell(agent, client, q, run_key, N):
    """Corre N repeticiones de (q, grafo), juzga cada una. Devuelve lista de reps."""
    reps = []
    for k in range(N):
        tr = agent.ask(q["id"], q["pregunta"])
        failed = (not tr.parse_ok) or tr.truncated_max_tokens or (tr.error is not None)
        verdict, judge_usage, judge_err = None, {"in": 0, "out": 0}, None
        if not failed:
            jr = judge.judge_trace(client, q, vars(tr))
            verdict = jr["verdict"]
            judge_usage = jr["usage"]
            judge_err = jr.get("errors") or None
        reps.append({
            "rep": k + 1,
            "qid": q["id"], "run": run_key, "categoria": q.get("categoria"),
            "respondible": (tr.final_json or {}).get("respondible"),
            "citas": (tr.final_json or {}).get("citas"),
            "respuesta": (tr.final_json or {}).get("respuesta"),
            "tool_calls_used": tr.tool_calls_used,
            "hit_tool_limit": tr.hit_tool_limit,
            "parse_ok": tr.parse_ok,
            "truncated_max_tokens": tr.truncated_max_tokens,
            "error": tr.error,
            "failed_trace": failed,
            "verdict": verdict,
            "harness_cost": _harness_cost(tr),
            "judge_cost": _judge_cost(judge_usage),
            "judge_error": judge_err,
        })
    return reps


def _mode(values):
    """(verdict_modal, unanime, distribucion). Empate modal → 'sin_consenso'."""
    c = Counter(json.dumps(v, ensure_ascii=False) for v in values)
    maxn = max(c.values())
    winners = [k for k, n in c.items() if n == maxn]
    dist = {k: n for k, n in c.items()}
    if len(winners) == 1:
        return json.loads(winners[0]), (maxn == len(values)), dist
    return "sin_consenso", False, dist


def aggregate_cell(reps):
    """Agrega por dimensión sobre las reps NO fallidas. Devuelve {dim: {...}}."""
    good = [r["verdict"] for r in reps if r["verdict"] is not None]
    out = {"n_reps": len(reps), "n_validas": len(good), "dimensiones": {}}
    if not good:
        out["sin_veredicto"] = True
        return out
    for dim in VERDICT_DIMS:
        vals = [v.get(dim) for v in good if v.get(dim) is not None]
        if not vals:
            continue  # dimensión N/A para esta pregunta (p. ej. abstencion en factual)
        verdict, unanime, dist = _mode(vals)
        out["dimensiones"][dim] = {"modal": verdict, "unanime": unanime,
                                   "distribucion": dist, "n": len(vals)}
    return out


# --------------------------------------------------------------------------- #
# Cola de adjudicación                                                         #
# --------------------------------------------------------------------------- #
def _append_adjudicacion(reps):
    pend = []
    for r in reps:
        v = r["verdict"] or {}
        if v.get("requiere_adjudicacion_humana"):
            ns = (v.get("afirmaciones_no_soportadas") or {}).get("centrales") or []
            pend.append({
                "qid": r["qid"], "run": r["run"], "rep": r["rep"],
                "pregunta": None,  # se completa en run_graph con el texto
                "afirmaciones_centrales_no_soportadas": ns,
                "citas_agente": r["citas"],
            })
    return pend


def _flush_adjudicacion(items):
    existing = []
    if ADJ_QUEUE.exists():
        existing = json.load(open(ADJ_QUEUE, encoding="utf-8"))
    existing.extend(items)
    json.dump(existing, open(ADJ_QUEUE, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)


# --------------------------------------------------------------------------- #
# Corrida de un grafo (con checkpoint)                                         #
# --------------------------------------------------------------------------- #
def run_graph(run_key, questions, N, outdir, client, selftest_line=None):
    kg = load_graph(run_key)
    agent = GraphAgent(kg, client=client, cache_conversation=True)
    (outdir / "traces" / run_key).mkdir(parents=True, exist_ok=True)

    cells, adj_items = [], []
    for q in questions:
        reps = evaluate_cell(agent, client, q, run_key, N)
        # persistir trazas crudas por repetición
        json.dump(reps, open(outdir / "traces" / run_key / f"{q['id']}.json", "w",
                             encoding="utf-8"), ensure_ascii=False, indent=2)
        agg = aggregate_cell(reps)
        cells.append({"qid": q["id"], "categoria": q.get("categoria"),
                      "agg": agg, "reps_meta": [
                          {kk: r[kk] for kk in ("rep", "respondible", "hit_tool_limit",
                                                "parse_ok", "truncated_max_tokens",
                                                "error", "failed_trace",
                                                "harness_cost", "judge_cost")}
                          for r in reps]})
        for a in _append_adjudicacion(reps):
            a["pregunta"] = q["pregunta"]
            adj_items.append(a)

    if adj_items:
        _flush_adjudicacion(adj_items)
    json.dump(cells, open(outdir / f"agg_{run_key}.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    _write_checkpoint(run_key, cells, N, outdir, len(adj_items), selftest_line)
    return cells


def _stability(cells):
    tot = uni = 0
    for c in cells:
        for dim, info in c["agg"].get("dimensiones", {}).items():
            tot += 1
            if info["unanime"]:
                uni += 1
    return uni, tot


def _write_checkpoint(run_key, cells, N, outdir, n_adj, selftest_line=None):
    reps_meta = [m for c in cells for m in c["reps_meta"]]
    n_reps = len(reps_meta)
    hit = sum(1 for m in reps_meta if m["hit_tool_limit"])
    parse_err = sum(1 for m in reps_meta if not m["parse_ok"])
    trunc = sum(1 for m in reps_meta if m["truncated_max_tokens"])
    failed = sum(1 for m in reps_meta if m["failed_trace"])
    cost = sum(m["harness_cost"] + m["judge_cost"] for m in reps_meta)
    uni, tot = _stability(cells)
    unans = [c for c in cells if c["categoria"] == "unanswerable"]

    L = [f"# Checkpoint — {run_key} (N={N})", ""]
    if selftest_line:
        L.append(f"- {selftest_line}")
    L.append(f"- Preguntas: {len(cells)} | repeticiones: {n_reps}")
    L.append(f"- Costo acumulado (este grafo): ${cost:.4f}")
    L.append(f"- hit_tool_limit: {hit}/{n_reps} ({100*hit/n_reps:.0f}%)")
    L.append(f"- parse_errors: {parse_err} | cortes max_tokens: {trunc} | "
             f"trazas fallidas: {failed}")
    L.append(f"- Estabilidad: {uni}/{tot} celdas unánimes "
             f"({100*uni/tot:.0f}%)" if tot else "- Estabilidad: s/celdas")
    L.append(f"- Cola de adjudicación (nuevas este grafo): {n_adj}")
    L.append("")
    L.append("## Comportamiento de unanswerable")
    if unans:
        unans_reps = [m for c in unans for m in c["reps_meta"]]
        n_false = sum(1 for m in unans_reps if m["respondible"] is False)
        L.append(f"- respondible=false en **{n_false}/{len(unans_reps)}** "
                 f"repeticiones de unanswerable"
                 + (" (TODAS ✅)" if n_false == len(unans_reps) else " ⚠ REVISAR"))
        for c in unans:
            dims = c["agg"].get("dimensiones", {})
            ab = dims.get("abstencion", {})
            es = dims.get("especulacion_en_prosa", {})
            rs = [m["respondible"] for m in c["reps_meta"]]
            L.append(f"- {c['qid']}: respondible={rs} | abstencion modal={ab.get('modal')} "
                     f"(unánime={ab.get('unanime')}); especulacion modal="
                     f"{es.get('modal')} (dist={es.get('distribucion')})")
    else:
        L.append("- (ninguna unanswerable en este conjunto)")
    L.append("")
    # Muestra: una factual_directa limpia (todas las dims unánimes) + la más
    # conflictiva = la celda con MÁS dimensiones no unánimes (incluye sin_consenso
    # como caso particular). Fix del reporter: el selector previo usaba el conteo de
    # sin_consenso, que es 0 cuando todos los desacuerdos son splits 2-1 → devolvía
    # la primera celda. Ver changelog (capa de reporting).
    def _n_nonunan(c):
        return sum(1 for i in c["agg"].get("dimensiones", {}).values()
                   if not i["unanime"])
    factual_clean = next((c for c in cells if c["categoria"] == "factual_directa"
                          and c["agg"].get("dimensiones")
                          and all(i["unanime"] for i in c["agg"]["dimensiones"].values())), None)
    conflictiva = max(cells, key=_n_nonunan) if cells else None
    if conflictiva and _n_nonunan(conflictiva) == 0:
        conflictiva = None  # todas las celdas unánimes
    L.append("## Trazas de muestra")
    for label, c in [("factual limpia", factual_clean), ("más conflictiva", conflictiva)]:
        if not c:
            continue
        dims = c["agg"].get("dimensiones", {})
        m0 = c["reps_meta"][0]
        L.append(f"- ({label}) {c['qid']} ({c['categoria']}): "
                 + ", ".join(f"{d}={i['modal']}{'' if i['unanime'] else '*'}"
                             for d, i in dims.items())
                 + f" | rep1 cost=${m0['harness_cost']+m0['judge_cost']:.4f}")
    L.append("(* = dimensión no unánime / sin_consenso)")
    L.append("")
    L.append("**FRENO de checkpoint.** Revisar y dar OK antes del siguiente grafo. "
             "Los checkpoints detectan fallas técnicas; no ajustan nada. Un bug de "
             "infraestructura ⇒ documentar, arreglar y RE-EJECUTAR la corrida desde cero.")
    p = outdir / f"checkpoint_{run_key}.md"
    p.write_text("\n".join(L), encoding="utf-8")
    print(f"\n=== CHECKPOINT {run_key} ===")
    print("\n".join(L[1:14]))
    print(f"Checkpoint: {p}")


# --------------------------------------------------------------------------- #
# Smoke (valida la maquinaria; NO toca el eval_set)                            #
# --------------------------------------------------------------------------- #
def run_smoke(client, log):
    pool = {q["id"]: q for q in json.load(open(DEV_POOL, encoding="utf-8"))["preguntas"]}
    qids = ["CQ-023", "dev_unans_1"]   # answerable+adjudicación  +  unanswerable
    questions = [pool[i] for i in qids]
    SMOKE_DIR.mkdir(parents=True, exist_ok=True)
    # limpiar cola de adjudicación previa del smoke (archivo separado)
    global ADJ_QUEUE
    ADJ_QUEUE = SMOKE_DIR / "adjudicacion_pendiente_SMOKE.json"
    if ADJ_QUEUE.exists():
        ADJ_QUEUE.unlink()

    _CAPTURE["on"] = True
    _CAPTURE["payloads"] = []
    cells = run_graph("run_3", questions, N=2, outdir=SMOKE_DIR, client=client)
    _CAPTURE["on"] = False
    audit = audit_blindness(_CAPTURE["payloads"])
    json.dump(audit, open(SMOKE_DIR / "blindness_audit.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    _write_smoke_report(cells, audit, log)


def _write_smoke_report(cells, audit, log):
    L = ["# Smoke del pipeline de corrida congelada", ""]
    L.append("2 preguntas del dev_pool (CQ-023 answerable+adjudicación, dev_unans_1 "
             "unanswerable) × run_3 × N=2. Valida repeticiones, agregación modal, "
             "checkpoint, política de errores, cola de adjudicación y ceguera del juez. "
             "**NO toca el eval_set.**")
    L.append("")
    L.append("## Agregación modal (N=2)")
    L.append("")
    L.append("| qid | categoria | dimensión | modal | unánime | distribución |")
    L.append("|-----|-----------|-----------|-------|:-------:|--------------|")
    for c in cells:
        for dim, info in c["agg"].get("dimensiones", {}).items():
            uni = "✅" if info["unanime"] else ("⚠ sin_consenso" if info["modal"] == "sin_consenso" else "—")
            L.append(f"| {c['qid']} | {c['categoria']} | {dim} | {info['modal']} | "
                     f"{uni} | {info['distribucion']} |")
    L.append("")
    L.append("> Con N=2, cualquier desacuerdo entre las 2 reps marca la dimensión "
             "`sin_consenso` (empate modal 1-1). Es esperado en preguntas de frontera.")
    L.append("")
    L.append("## Ceguera del juez — auditoría")
    L.append("")
    L.append(f"Payloads del juez auditados: **{audit['n_payloads']}** (2 por traza: "
             "Paso 1 + Paso 2). Claves de top-level expuestas al juez: "
             f"`{', '.join(audit['payload_keys'])}`.")
    L.append("")
    any_leak = False
    for cat, toks in audit["findings"].items():
        if toks:
            any_leak = True
            L.append(f"- ⚠ **{cat}**: aparecen {toks}")
    if not any_leak:
        L.append("- ✅ **Sin fugas de identidad de run**: no aparece ningún run_key "
                 "(run_1..5), nombre de grafo (cookbook/papers/ppf_core/schema_light/"
                 "hybrid), path (kg.json/source_kg/data\\_experiment/frozen) ni prefijo "
                 "de id de nodo (Obligacion_/ope_/con_/…) en ningún payload.")
    L.append("")
    L.append("Lo único que el juez ve y correlaciona con el grafo es **contenido "
             "legítimo bajo evaluación**: la prosa de la respuesta, y las citas "
             "(`source_doc` = nombre de PDF, COMPARTIDO por los 5 grafos; `location` "
             "con su granularidad, que el juez NECESITA para puntuar `cita_precision`). "
             "No hay etiqueta ni metadata que identifique el run.")
    L.append("")
    L.append("## Cola de adjudicación")
    L.append("")
    if ADJ_QUEUE.exists():
        adj = json.load(open(ADJ_QUEUE, encoding="utf-8"))
        L.append(f"{len(adj)} entrada(s) en `{ADJ_QUEUE.name}`. Ejemplo:")
        if adj:
            e = adj[0]
            L.append(f"- {e['qid']} rep{e['rep']}: "
                     f"{len(e['afirmaciones_centrales_no_soportadas'])} afirmación(es) "
                     f"central(es) no soportada(s); citas={e['citas_agente']}")
    else:
        L.append("(sin entradas)")
    L.append("")
    L.append("## Política de errores (verificada)")
    L.append("")
    reps_meta = [m for c in cells for m in c["reps_meta"]]
    L.append(f"- Retries de infraestructura logueados: {len(log['events'])} eventos "
             f"(ver `retries.jsonl`). 0 = no hubo errores de infra en el smoke.")
    L.append(f"- parse_errors: {sum(1 for m in reps_meta if not m['parse_ok'])} | "
             f"cortes max_tokens: {sum(1 for m in reps_meta if m['truncated_max_tokens'])} "
             f"(no se reintentan: comportamiento del sistema).")
    L.append("")
    L.append("## Costo del smoke")
    cost = sum(m["harness_cost"] + m["judge_cost"] for m in reps_meta)
    L.append(f"- Total: **${cost:.4f}** ({len(reps_meta)} repeticiones).")
    L.append("")
    p = SMOKE_DIR / "smoke_report.md"
    p.write_text("\n".join(L), encoding="utf-8")
    print(f"\nSmoke report: {p}")
    print(f"Blindness audit fugas: "
          f"{'NINGUNA' if not any(audit['findings'].values()) else audit['findings']}")
    print(f"Costo smoke: ${cost:.4f}")


# --------------------------------------------------------------------------- #
# Reporte final — DRAFT (etapa 1, con pendientes de adjudicación marcados)      #
# --------------------------------------------------------------------------- #
REPORT_DRAFT = FROZEN_DIR / "reporte_final_draft.md"
CATS_ANS = ["factual_directa", "multi_norma", "cadena_restriccion_excepcion"]


def _cell_correctitud(cell, run, qid, pendiente_set, qcat):
    """Modal de correctitud, salvo que la celda esté pendiente de adjudicación
    (REGLA: correctitud se retiene si la celda tiene afirmaciones centrales en la
    cola; las demás dimensiones SÍ se reportan)."""
    if qcat.get(qid) != "unanswerable" and (run, qid) in pendiente_set:
        return "pendiente_adjudicacion"
    dims = cell["agg"].get("dimensiones", {})
    return dims.get("correctitud", {}).get("modal")


def build_report():
    queue = json.load(open(ADJ_QUEUE, encoding="utf-8")) if ADJ_QUEUE.exists() else []
    pendiente_set = {(x["run"], x["qid"]) for x in queue}
    pool = json.load(open(EVAL_SET, encoding="utf-8"))["preguntas"]
    qcat = {q["id"]: q["categoria"] for q in pool}
    qorder = [q["id"] for q in pool]
    data = {}
    for r in GRAPH_ORDER:
        cells = json.load(open(FROZEN_DIR / f"agg_{r}.json", encoding="utf-8"))
        data[r] = {c["qid"]: c for c in cells}

    def reps_all(r):
        return [m for c in data[r].values() for m in c["reps_meta"]]

    L = ["# Reporte final (DRAFT — etapa 1) — corrida congelada Fase 2.3", ""]
    L.append("eval_set_v1 (23 preguntas) × 5 grafos × N=3. Respondedor "
             "`claude-haiku-4-5-20251001` (caching ON), juez `claude-sonnet-4-6` "
             "v2.1.1, ambos congelados. Veredicto por celda = MODAL de 3 reps.")
    L.append("")
    L.append("> ⚠️ **DRAFT de dos etapas.** REGLA: toda celda answerable con ≥1 "
             "afirmación CENTRAL no soportada (en la cola de adjudicación) tiene su "
             "**correctitud marcada `pendiente_adjudicacion`** — NO se emite veredicto "
             "final de correctitud sobre ella hasta que la autora adjudique contra "
             "los PDFs. Las demás dimensiones (completitud, citas, abstención) SÍ se "
             "reportan. La **etapa 2 (final)** se emite tras la adjudicación humana.")
    L.append("")

    # 1. Resumen por grafo
    L.append("## 1. Resumen por grafo")
    L.append("")
    L.append("| Grafo | Costo | Estabilidad (unánimes) | sin_consenso | hit_limit | Adj. (rep / preg.) | Celdas pendientes |")
    L.append("|-------|------:|-----------------------:|-------------:|----------:|-------------------:|------------------:|")
    tot_cost = 0.0
    for r in GRAPH_ORDER:
        cells = list(data[r].values())
        cost = sum(m["harness_cost"] + m["judge_cost"] for m in reps_all(r))
        tot_cost += cost
        uni = sum(1 for c in cells for i in c["agg"].get("dimensiones", {}).values() if i["unanime"])
        totd = sum(1 for c in cells for _ in c["agg"].get("dimensiones", {}))
        sc = sum(1 for c in cells for i in c["agg"].get("dimensiones", {}).values()
                 if i["modal"] == "sin_consenso")
        hit = sum(1 for m in reps_all(r) if m["hit_tool_limit"])
        adj_rep = sum(1 for x in queue if x["run"] == r)
        adj_q = len({x["qid"] for x in queue if x["run"] == r})
        pend = len({qid for qid in data[r]
                    if qcat.get(qid) != "unanswerable" and (r, qid) in pendiente_set})
        L.append(f"| {r} | ${cost:.4f} | {uni}/{totd} ({100*uni/totd:.0f}%) | {sc} "
                 f"| {hit}/69 ({100*hit/69:.0f}%) | {adj_rep} / {adj_q} | {pend} |")
    L.append(f"| **TOTAL** | **${tot_cost:.4f}** | | | | {len(queue)} / — | |")
    L.append("")

    # 2. Correctitud: grafo × categoría (pendientes retenidos)
    L.append("## 2. Correctitud — grafo × categoría (answerable)")
    L.append("")
    L.append("Conteo de celdas por veredicto modal. `pend` = correctitud retenida "
             "(pendiente de adjudicación). El veredicto de esas celdas NO es final.")
    L.append("")
    L.append("| Grafo | Categoría | correcta | parcial | incorrecta | pend |")
    L.append("|-------|-----------|---------:|--------:|-----------:|-----:|")
    for r in GRAPH_ORDER:
        for cat in CATS_ANS:
            qs = [q for q in qorder if qcat[q] == cat and q in data[r]]
            cnt = Counter(_cell_correctitud(data[r][q], r, q, pendiente_set, qcat) for q in qs)
            L.append(f"| {r} | {cat} | {cnt.get('correcta',0)} | {cnt.get('parcial',0)} "
                     f"| {cnt.get('incorrecta',0)} | {cnt.get('pendiente_adjudicacion',0)} |")
    L.append("")

    # 3. Completitud: grafo × categoría
    L.append("## 3. Completitud — grafo × categoría (answerable)")
    L.append("")
    L.append("| Grafo | Categoría | completa | parcial |")
    L.append("|-------|-----------|---------:|--------:|")
    for r in GRAPH_ORDER:
        for cat in CATS_ANS:
            qs = [q for q in qorder if qcat[q] == cat and q in data[r]]
            cnt = Counter(data[r][q]["agg"].get("dimensiones", {}).get("completitud", {}).get("modal")
                          for q in qs)
            L.append(f"| {r} | {cat} | {cnt.get('completa',0)} | {cnt.get('parcial',0)} |")
    L.append("")

    # 4. Unanswerable: abstención + especulación
    L.append("## 4. Unanswerable — abstención y especulación (4 preguntas × grafo)")
    L.append("")
    L.append("| Grafo | abst. correcta | abst. incorrecta | espec. True | espec. False |")
    L.append("|-------|---------------:|-----------------:|------------:|-------------:|")
    unans_q = [q for q in qorder if qcat[q] == "unanswerable"]
    for r in GRAPH_ORDER:
        ab = Counter(data[r][q]["agg"]["dimensiones"].get("abstencion", {}).get("modal") for q in unans_q)
        es = Counter(data[r][q]["agg"]["dimensiones"].get("especulacion_en_prosa", {}).get("modal") for q in unans_q)
        L.append(f"| {r} | {ab.get('correcta',0)} | {ab.get('incorrecta',0)} "
                 f"| {es.get(True,0)} | {es.get(False,0)} |")
    L.append("")

    # 5. Citas
    L.append("## 5. Citas — por grafo (todas las celdas)")
    L.append("")
    L.append("| Grafo | doc_correcto True | doc_correcto False | prec: punto | pagina | ausente |")
    L.append("|-------|------------------:|-------------------:|------------:|-------:|--------:|")
    for r in GRAPH_ORDER:
        dc = Counter(); pr = Counter()
        for c in data[r].values():
            d = c["agg"].get("dimensiones", {})
            if "cita_documento_correcto" in d:
                dc[d["cita_documento_correcto"]["modal"]] += 1
            if "cita_precision" in d:
                pr[d["cita_precision"]["modal"]] += 1
        L.append(f"| {r} | {dc.get(True,0)} | {dc.get(False,0)} | {pr.get('punto',0)} "
                 f"| {pr.get('pagina',0)} | {pr.get('ausente',0)} |")
    L.append("")

    # 6. Celdas pendientes de adjudicación (detalle)
    L.append("## 6. Celdas pendientes de adjudicación (correctitud retenida)")
    L.append("")
    pend_cells = sorted({(x["run"], x["qid"]) for x in queue
                         if qcat.get(x["qid"]) != "unanswerable"})
    L.append(f"**{len(pend_cells)} celdas answerable** con correctitud retenida "
             f"(de {len(queue)} entradas de cola; ver `adjudicacion_pendiente.json`):")
    by_run = defaultdict(list)
    for r, q in pend_cells:
        by_run[r].append(q)
    for r in GRAPH_ORDER:
        if by_run[r]:
            L.append(f"- {r}: {', '.join(by_run[r])}")
    unans_flagged = sorted({(x["run"], x["qid"]) for x in queue
                            if qcat.get(x["qid"]) == "unanswerable"})
    if unans_flagged:
        L.append("")
        L.append(f"Además, {len(unans_flagged)} celdas **unanswerable** tienen "
                 "afirmaciones a adjudicar (su veredicto de abstención se reporta, "
                 "pero las afirmaciones flageadas igual requieren chequeo contra PDFs): "
                 + "; ".join(f"{r}/{q}" for r, q in unans_flagged))
    L.append("")
    L.append("## 7. Notas metodológicas")
    L.append("")
    L.append("**(a) Métrica comparativa de adjudicación.** La unidad PRINCIPAL es "
             "**preguntas distintas flageadas** por grafo: run_1=10, run_2=10, "
             "run_3=9, run_4=6, run_5=7. La métrica por REPETICIÓN (25/22/18/11/14) "
             "es SECUNDARIA: el conteo por-rep mezcla *cuántas preguntas* necesitan "
             "adjudicación con la *inestabilidad rep-level* del flag, sobre-ponderando "
             "la segunda.")
    L.append("")
    L.append("**(b) `multi_norma` no-puntuable en correctitud sin adjudicación.** En "
             "los **5 grafos**, TODAS las celdas `multi_norma` quedaron "
             "`pendiente_adjudicacion` (tabla 2: correcta/parcial/incorrecta en cero, "
             "todo en `pend`). El gold resumido (respuesta_esperada + cita_textual + "
             "ground_truth_secciones) no puede soportar respuestas multi-hop "
             "granulares verdaderas: una respuesta que combina 2+ secciones produce "
             "afirmaciones más finas que el referente, que el juez marca `no_soportado` "
             "(no falso) → adjudicación humana. Es **hallazgo metodológico, no "
             "defecto**: el mecanismo de seguridad del juez (no validar contra "
             "conocimiento paramétrico) operando como se diseñó. La correctitud de "
             "`multi_norma` solo es comparable entre estrategias DESPUÉS de la etapa 2.")
    L.append("")
    L.append("---")
    L.append("**Etapa 2 (final):** tras la adjudicación humana de las afirmaciones "
             "centrales contra los PDFs, las celdas `pendiente_adjudicacion` reciben "
             "su correctitud final (correcta si las afirmaciones se verifican, "
             "incorrecta/parcial si alguna central resulta falsa) y se re-emiten las "
             "tablas 1, 2 y 6. NADA del dataset congelado se re-corre: la adjudicación "
             "solo resuelve veredictos retenidos.")
    REPORT_DRAFT.write_text("\n".join(L), encoding="utf-8")
    print(f"Draft escrito en: {REPORT_DRAFT}")
    print(f"Celdas pendientes (answerable): {len(pend_cells)} | costo total: ${tot_cost:.4f}")


# --------------------------------------------------------------------------- #
def _make_client():
    log = {"events": []}
    outdir = None

    def logger(ev):
        log["events"].append(ev)
    import anthropic
    real = anthropic.Anthropic(max_retries=0)  # el retry lo maneja RetryingClient
    return RetryingClient(real, logger), log


def main():
    load_dotenv(EVAL_DIR / ".env")
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["selftest", "smoke", "graph", "regen", "report"],
                    required=True)
    ap.add_argument("--graph", choices=GRAPH_ORDER)
    ap.add_argument("--N", type=int, default=3)
    args = ap.parse_args()
    import os

    if args.mode == "regen":
        # Regenera el checkpoint desde el agg persistido (capa de reporting; sin API).
        if not args.graph:
            raise SystemExit("--graph requerido en modo regen")
        cells = json.load(open(FROZEN_DIR / f"agg_{args.graph}.json", encoding="utf-8"))
        n_adj = 0
        if ADJ_QUEUE.exists():
            n_adj = sum(1 for x in json.load(open(ADJ_QUEUE, encoding="utf-8"))
                        if x.get("run") == args.graph)
        st = None
        stf = FROZEN_DIR / "selftest_retry.json"
        if stf.exists():
            st = json.load(open(stf, encoding="utf-8")).get("summary")
        _write_checkpoint(args.graph, cells, args.N, FROZEN_DIR, n_adj, st)
        raise SystemExit(0)

    if args.mode == "report":
        build_report()
        raise SystemExit(0)

    if args.mode == "selftest":
        passed, summary, checks = selftest_retry()
        print(summary)
        for name, ok in checks:
            print(f"  {'OK ' if ok else 'XX '}{name}")
        FROZEN_DIR.mkdir(parents=True, exist_ok=True)
        json.dump({"passed": passed, "summary": summary, "checks": checks},
                  open(FROZEN_DIR / "selftest_retry.json", "w", encoding="utf-8"),
                  ensure_ascii=False, indent=2)
        raise SystemExit(0 if passed else 1)

    if not os.environ.get("ANTHROPIC_API_KEY", "").strip():
        raise SystemExit("ERROR: ANTHROPIC_API_KEY no seteada")

    client, log = _make_client()
    if args.mode == "smoke":
        run_smoke(client, log)
        # persistir log de retries del smoke
        json.dump(log["events"], open(SMOKE_DIR / "retries.jsonl", "w",
                                      encoding="utf-8"), ensure_ascii=False, indent=2)
    elif args.mode == "graph":
        if not args.graph:
            raise SystemExit("--graph requerido en modo graph")
        passed, st_summary, _ = selftest_retry()
        if not passed:
            raise SystemExit(f"Self-test del retry FALLÓ — NO se larga la corrida. {st_summary}")
        print(st_summary, flush=True)
        FROZEN_DIR.mkdir(parents=True, exist_ok=True)
        questions = json.load(open(EVAL_SET, encoding="utf-8"))["preguntas"]
        run_graph(args.graph, questions, args.N, FROZEN_DIR, client,
                  selftest_line=st_summary)
        json.dump(log["events"], open(FROZEN_DIR / f"retries_{args.graph}.jsonl", "w",
                                      encoding="utf-8"), ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
