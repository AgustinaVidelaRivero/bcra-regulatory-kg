#!/usr/bin/env python3
"""run_agente_solo.py — Wrapper de corrida agente-solo (sin juez) para sets SIN gold.

Para sets de preguntas sin respuesta esperada no hay juez posible: el síntoma
lo pone el laudo humano y el diagnóstico el verificador validado (modo
sin-gold, mismo contrato que produce `scripts/adaptador_sesiones.py`). Este
wrapper corre el pipeline de `run_posthoc` con el AGENTE INTACTO (mismo
`GraphAgent`, mismo cliente cacheado, mismo modelo, mismos parámetros) y
reemplaza EN MEMORIA el punto de invocación del juez (`run_posthoc.run_rep`,
que llama a `judge.judge_trace`) por una variante que escribe un stub de juez
explícitamente vacío. Ningún módulo congelado se edita (patrón wrapper de
`run_escalon1.py`: importar y ajustar en memoria).

Contrato del rep (verificado contra el adaptador en `--selftest`):
  · top-level `sin_gold: "laudo_humano"` — marca del modo sin-gold.
  · bloque `judge` = réplica exacta del stub del adaptador de sesiones
    (claves `stub` / `step1` con sus tres listas vacías / `step2.verificaciones`
    vacía), para que `verifier_pilot.load_rep` y el builder del verificador
    consuman estas trazas igual que las del intake de la app.
  · el resto del rep conserva el layout de `run_posthoc.run_rep` (trace
    completo, `raw_turns_agent` crudos por turno, costos), con
    `raw_turns_judge = []` y `judge_cost = 0.0`.

Escrituras (idénticas en layout a run_posthoc):
  · posthoc_run/traces/<label>/<run>/<qid>.json  — lista de reps por pregunta.
  · posthoc_run/summary_<label>_<run>.json       — summary de run_posthoc
    aumentado con `tokens_agente` (agregado de los contadores del harness:
    tokens_in / tokens_out / cache_read / cache_write por trace).

Guardas:
  · `--label` es OBLIGATORIO y se rechaza si su directorio ya existe bajo
    posthoc_run/traces/ (las corridas selladas off/on/escalon1*/gate_* no se
    pisan). La caché local hace que re-correr con un label nuevo no re-pague.
  · `--queries` es OBLIGATORIO: este runner es para sets sin gold; no hereda
    el default eval_set_v1 (que tiene gold y juez propio) de run_posthoc.
  · Sin optimizaciones de caching de Anthropic nuevas: rige la decisión 5 de
    docs/decisiones_caching_extraccion.md. Este wrapper no agrega breakpoints
    de caché; el agente corre byte-idéntico a run_posthoc.

Ubicación: los wrappers/runners de evaluación viven en evaluacion/runners/
(convención de run_posthoc.py / run_etapa2.py); no existe evaluacion/code/.

Uso, desde la raíz del repo:
    .venv/bin/python data/experiment/evaluacion/runners/run_agente_solo.py \
        --run run_3 --reps 1 --queries <ruta_set_sin_gold> --label <label>
    .venv/bin/python data/experiment/evaluacion/runners/run_agente_solo.py --selftest
"""
from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path

RUNNERS_DIR = Path(__file__).resolve().parent
EVAL_DIR = RUNNERS_DIR.parent
REPO_ROOT = EVAL_DIR.parents[2]
sys.path.insert(0, str(RUNNERS_DIR))
sys.path.insert(0, str(EVAL_DIR))

import run_posthoc  # noqa: E402

SIN_GOLD = "laudo_humano"

# Réplica EXACTA del stub de juez del adaptador de sesiones (claves y valores);
# el selftest la compara por igualdad profunda contra la salida real de
# scripts/adaptador_sesiones.construir_rep para detectar cualquier drift.
JUDGE_STUB = {
    "stub": "sin_gold: laudo_humano — sin juez; listas vacías a propósito",
    "step1": {
        "patas_de_la_pregunta": [],
        "afirmaciones_verificables": [],
        "reportes_de_alcance": [],
    },
    "step2": {"verificaciones": []},
}


# --------------------------------------------------------------------------- #
# Reemplazo del punto de invocación del juez (run_posthoc.run_rep)             #
# --------------------------------------------------------------------------- #
def run_rep_agente_solo(agent, judge_client, agent_cache, judge_cache, q,
                        run_key, rep_k, thinking, capture_raw=True) -> dict:
    """Misma firma y mismo lado-agente que run_posthoc.run_rep; el juez no se
    invoca nunca (judge_client/judge_cache quedan sin uso) y el bloque judge
    es el stub sin_gold."""
    qid = q["id"]
    a0 = run_posthoc._max_access_rowid(agent_cache)
    tr = agent.ask(qid, q.get("pregunta", ""))
    if capture_raw:
        _, _, agent_turns = run_posthoc._turns_since(agent_cache, a0, "agent")
    else:
        agent_turns = []

    failed = (not tr.parse_ok) or tr.truncated_max_tokens or (tr.error is not None)
    return {
        "rep": rep_k + 1,
        "qid": qid, "run": run_key, "categoria": q.get("categoria"),
        "thinking_enabled": thinking,
        "failed_trace": failed,
        "origen": "run_agente_solo",
        "sin_gold": SIN_GOLD,
        "trace": vars(tr),
        "raw_turns_agent": agent_turns,
        "judge": copy.deepcopy(JUDGE_STUB),
        "raw_turns_judge": [],
        "harness_cost": tr.cost_usd,
        "judge_cost": 0.0,
    }


def run_graph_agente_solo(real_client, run_key, questions, *, reps, thinking,
                          db_path, label):
    """Delegación a run_posthoc.run_graph (con run_rep ya parcheado) + summary
    aumentado con el agregado de tokens del agente que ya contabiliza el
    harness (QuestionTrace.tokens_in/out y contadores de caché)."""
    summary = run_posthoc.run_graph(real_client, run_key, questions, reps=reps,
                                    thinking=thinking, db_path=db_path, label=label)
    outdir = run_posthoc.POSTHOC_DIR / "traces" / label / run_key
    tok = {"tokens_in": 0, "tokens_out": 0, "cache_read": 0, "cache_write": 0}
    for q in questions:
        for r in json.load(open(outdir / f"{q['id']}.json", encoding="utf-8")):
            t = r.get("trace") or {}
            for k in tok:
                tok[k] += int(t.get(k, 0) or 0)
    summary["modo"] = "agente_solo"
    summary["sin_gold"] = SIN_GOLD
    summary["tokens_agente"] = tok
    spath = run_posthoc.POSTHOC_DIR / f"summary_{label}_{run_key}.json"
    json.dump(summary, open(spath, "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)
    print(f"  -> tokens agente {label}/{run_key}: {tok}", flush=True)
    return summary


# --------------------------------------------------------------------------- #
# Selftest OFFLINE (sin API): 1 pregunta sintética con cliente falso           #
# --------------------------------------------------------------------------- #
def _selftest() -> int:
    import importlib.util
    import tempfile
    from anthropic.types import Message

    _checks = []
    def check(name, cond):
        _checks.append((name, bool(cond)))

    # stub de referencia: la salida REAL del adaptador de sesiones (no una copia)
    spec = importlib.util.spec_from_file_location(
        "adaptador_sesiones", REPO_ROOT / "scripts" / "adaptador_sesiones.py")
    adaptador = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(adaptador)
    rep_adaptador = adaptador.construir_rep({"tools_llamadas": []}, {}, "selftest")

    # cliente falso: 2 turnos scripteados (tool_use + final JSON), cero API.
    TURN1 = {
        "id": "msg_t1", "type": "message", "role": "assistant",
        "model": "claude-haiku-4-5-20251001",
        "content": [
            {"type": "text", "text": "Busco en el grafo."},
            {"type": "tool_use", "id": "toolu_a", "name": "buscar_nodos",
             "input": {"consulta": "encaje", "limite": 5}},
        ],
        "stop_reason": "tool_use", "stop_sequence": None,
        "usage": {"input_tokens": 1433, "output_tokens": 40,
                  "cache_read_input_tokens": 0, "cache_creation_input_tokens": 1200},
    }
    TURN2 = {
        "id": "msg_t2", "type": "message", "role": "assistant",
        "model": "claude-haiku-4-5-20251001",
        "content": [{"type": "text",
                     "text": '{"respuesta":"prueba","citas":[],"respondible":true}'}],
        "stop_reason": "end_turn", "stop_sequence": None,
        "usage": {"input_tokens": 1600, "output_tokens": 60,
                  "cache_read_input_tokens": 1433, "cache_creation_input_tokens": 0},
    }

    class FakeMessages:
        def __init__(self):
            self.calls = 0
            self.script = [TURN1, TURN2]
        def create(self, **kwargs):
            i = self.calls
            self.calls += 1
            if i >= len(self.script):
                raise AssertionError(
                    f"llamada inesperada #{i+1} al cliente: el juez u otro "
                    "componente intentó llamar a la API")
            return Message.model_validate(self.script[i])

    class FakeClient:
        def __init__(self, m):
            self.messages = m

    q_synth = {"id": "ST-SOLO", "pregunta": "¿qué es el encaje?",
               "categoria": "selftest_sin_gold"}
    label = "selftest_agente_solo"

    posthoc_dir_orig = run_posthoc.POSTHOC_DIR
    run_rep_orig = run_posthoc.run_rep
    with tempfile.TemporaryDirectory() as tmp:
        tmpd = Path(tmp)
        fake = FakeMessages()
        try:
            # TODO lo que escribe run_graph se redirige al tempdir (el repo no
            # se toca): trazas, summary y calls.db del selftest.
            run_posthoc.POSTHOC_DIR = tmpd / "posthoc_run"
            run_posthoc.run_rep = run_rep_agente_solo
            summary = run_graph_agente_solo(
                FakeClient(fake), "run_3", [q_synth], reps=1, thinking=False,
                db_path=tmpd / "calls.db", label=label)
        finally:
            run_posthoc.POSTHOC_DIR = posthoc_dir_orig
            run_posthoc.run_rep = run_rep_orig

        # -- (ii) la traza pasa por load_rep del verificador sin error --------
        import verifier_pilot as vp
        vp_eval_orig = vp.EVAL_DIR
        rep, load_err = None, None
        try:
            vp.EVAL_DIR = tmpd
            rep = vp.load_rep(label, "run_3", "ST-SOLO")
        except Exception as e:  # noqa: BLE001 — el selftest reporta, no aborta
            load_err = repr(e)
        finally:
            vp.EVAL_DIR = vp_eval_orig
        check("(ii) verifier_pilot.load_rep carga la traza sin error "
              f"(err={load_err})", rep is not None)

        if rep is not None:
            # -- (i) stub sin_gold con las claves EXACTAS del adaptador -------
            check("(i) bloque judge == stub del adaptador (igualdad profunda, "
                  "claves y valores)", rep["judge"] == rep_adaptador["judge"])
            check("(i) marca top-level sin_gold == 'laudo_humano'",
                  rep.get("sin_gold") == rep_adaptador["sin_gold"] == SIN_GOLD)

            # -- (iii) ningún bloque de juez real -----------------------------
            j = rep["judge"]
            check("(iii) judge sin claves de juez real (verdict/usage)",
                  "verdict" not in j and "usage" not in j)
            check("(iii) step1/step2 con listas vacías",
                  j["step1"] == {"patas_de_la_pregunta": [],
                                 "afirmaciones_verificables": [],
                                 "reportes_de_alcance": []}
                  and j["step2"] == {"verificaciones": []})
            check("(iii) raw_turns_judge == [] y judge_cost == 0.0",
                  rep["raw_turns_judge"] == [] and rep["judge_cost"] == 0.0)
            check("(iii) el juez no tocó la API ni su caché: cliente falso "
                  "llamado solo por el agente (2 turnos), judge_cache 0 accesos",
                  fake.calls == 2
                  and summary["judge_cache_stats"]["accesses"] == 0)

            # -- lado agente intacto + conteo de tokens -----------------------
            check("agente: loop real completo (2 turnos, respuesta final parseada)",
                  rep["trace"]["parse_ok"] and rep["trace"]["tool_calls_used"] == 1
                  and len(rep["raw_turns_agent"]) == 2)
            check("summary: tokens_agente poblados desde los contadores del "
                  "harness (in=3033 out=100 cr=1433 cw=1200)",
                  summary["tokens_agente"] == {"tokens_in": 3033, "tokens_out": 100,
                                               "cache_read": 1433, "cache_write": 1200})

    print("\n=== run_agente_solo --selftest (OFFLINE, sin API) ===\n")
    passed = sum(ok for _, ok in _checks)
    for name, ok in _checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    print(f"\n  {passed}/{len(_checks)} checks OK")
    print("  RESULTADO:", "PASS ✅" if passed == len(_checks) else "FAIL ❌")
    return 0 if passed == len(_checks) else 1


# --------------------------------------------------------------------------- #
# CLI (compatible con run_posthoc: --run --reps --queries --label --db)        #
# --------------------------------------------------------------------------- #
def main() -> int:
    ap = argparse.ArgumentParser(
        description="Corrida agente-solo (sin juez) para sets sin gold.")
    ap.add_argument("--run", default="run_3", help="run key o 'all' (def run_3)")
    ap.add_argument("--reps", type=int, default=3, help="repeticiones por pregunta")
    ap.add_argument("--thinking", action="store_true",
                    help="prende thinking_enabled del agente (def OFF)")
    ap.add_argument("--queries", default=None,
                    help="set de preguntas SIN gold (obligatorio; sin default)")
    ap.add_argument("--label", default=None,
                    help="etiqueta de corrida (obligatoria; no puede pisar una existente)")
    ap.add_argument("--db", default=str(run_posthoc.DB_PATH))
    ap.add_argument("--selftest", action="store_true", help="prueba OFFLINE (sin API)")
    args = ap.parse_args()

    if args.selftest:
        return _selftest()

    if not args.queries:
        raise SystemExit("ERROR: --queries es obligatorio (este runner es para "
                         "sets sin gold; no hereda el eval_set con gold).")
    if not args.label:
        raise SystemExit("ERROR: --label es obligatorio.")
    existentes = run_posthoc.POSTHOC_DIR / "traces" / args.label
    if existentes.exists():
        raise SystemExit(f"ERROR: el label '{args.label}' ya existe en "
                         f"{existentes} — elegí un label nuevo (las corridas "
                         "selladas no se pisan).")

    run_posthoc.run_rep = run_rep_agente_solo  # juez fuera, EN MEMORIA
    real = run_posthoc._real_client()
    runs = run_posthoc.RUN_KEYS if args.run == "all" else [args.run]
    questions = run_posthoc._load_questions(Path(args.queries))
    for rk in runs:
        run_graph_agente_solo(real, rk, questions, reps=args.reps,
                              thinking=args.thinking, db_path=Path(args.db),
                              label=args.label)
    return 0


if __name__ == "__main__":
    sys.exit(main())
