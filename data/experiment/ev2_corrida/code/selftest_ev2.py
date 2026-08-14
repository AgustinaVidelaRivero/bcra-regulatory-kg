"""
selftest_ev2.py — SELFTEST OFFLINE de la corrida EV2 (fase A, $0, sin API).

Corrida en seco de punta a punta con un cliente FALSO scripteado (patrón
run_posthoc._selftest) sobre el grafo v3, ejercitando el circuito REAL:
FullCaptureAgent -> CachingClient (db propia) -> persistencia por caso.

Casos: los 2 primeros de cada eje según el orden resuelto (semilla
orden-ev2-v1) del grafo v3. Guiones:
  - navegabilidad caso 1: buscar_nodos(gold_id) + ver_nodo(gold_id) + final
      -> la métrica debe dar ancla VISTA y CONSULTADA.
  - navegabilidad caso 2: buscar_nodos(gold_id) + final (sin abrir el nodo)
      -> la métrica debe dar ancla VISTA sin consultar (BRECHA).
  - fidelidad (2 casos): buscar_nodos + final
      -> la respuesta final queda persistida SIN evaluar (ningún juez).

Verifica (con evidencia impresa):
  1. Persistencia completa por caso: metadata exigida por el mandato, traza
     del harness, steps_full sin truncar (output_chars == len(json)),
     raw_turns_agent == nº de llamadas API.
  2. Cero invocaciones de juez: la db de caché solo contiene domain='agent'.
  3. Replay de caché: re-corrida de los mismos casos con un cliente que
     EXPLOTA si lo llaman -> 100% hits (no se re-pagaría nada).
  4. Métrica determinística auto-verificada: visto/consultado/brecha sobre
     las trazas del dry run coincide con lo scripteado, con replay estándar
     y replay fuerte OK.

Todo se escribe bajo selftest_out/ (gitignorado) y cache/ (gitignorado).

Uso:  .venv/bin/python -B selftest_ev2.py
"""

from __future__ import annotations

import json
import shutil
import sqlite3
from pathlib import Path

from comun_ev2 import EV2_DIR, cargar_aptos, cargar_runtime, indice_anclas
from runner_ev2 import FullCaptureAgent, correr_grafo, _casos_efectivos, _sanitizar
from metrica_ev2 import evaluar_caso

from anthropic.types import Message  # noqa: E402
from harness import GraphIndex  # noqa: E402

SELFTEST_DIR = EV2_DIR / "selftest_out"
DB_PATH = EV2_DIR / "cache" / "ev2_selftest_v3.db"
LABEL = "ev2_selftest_v3"

_checks = []


def check(nombre, cond):
    _checks.append((nombre, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {nombre}")


# --------------------------------------------------------------------------- #
# Cliente falso scripteado                                                     #
# --------------------------------------------------------------------------- #
def _msg(content, stop_reason):
    return Message.model_validate({
        "id": "msg_selftest", "type": "message", "role": "assistant",
        "model": "claude-haiku-4-5-20251001", "content": content,
        "stop_reason": stop_reason, "stop_sequence": None,
        "usage": {"input_tokens": 1500, "output_tokens": 60,
                  "cache_read_input_tokens": 0,
                  "cache_creation_input_tokens": 1200},
    })


def turno_tool(nombre, args, uid):
    return _msg([{"type": "text", "text": "Exploro el grafo."},
                 {"type": "tool_use", "id": uid, "name": nombre,
                  "input": args}], "tool_use")


def turno_final(respuesta):
    txt = json.dumps({"respuesta": respuesta, "citas": [],
                      "respondible": True}, ensure_ascii=False)
    return _msg([{"type": "text", "text": txt}], "end_turn")


class FakeSequential:
    """Devuelve los mensajes scripteados en orden global. Explota si se le
    pide más de lo scripteado (llamada API no prevista)."""

    def __init__(self, script):
        self.script = list(script)
        self.calls = 0
        self.messages = self

    def create(self, **kwargs):
        if self.calls >= len(self.script):
            raise AssertionError("llamada API no prevista en el selftest")
        m = self.script[self.calls]
        self.calls += 1
        return m


class ExplodingClient:
    """Cliente que falla si se lo llama: prueba que el replay es 100% caché."""

    def __init__(self):
        self.messages = self

    def create(self, **kwargs):
        raise AssertionError("el replay llamó al cliente real (cache miss)")


# --------------------------------------------------------------------------- #
# Selftest                                                                     #
# --------------------------------------------------------------------------- #
def main() -> int:
    print("== SELFTEST OFFLINE EV2 (sin API, $0) ==")
    # limpieza de corridas previas del selftest (solo artefactos gitignorados)
    if SELFTEST_DIR.exists():
        shutil.rmtree(SELFTEST_DIR)
    if DB_PATH.exists():
        DB_PATH.unlink()

    efectivos = _casos_efectivos("v3")
    fid = [c for c in efectivos if c["eje"] == "fidelidad"][:2]
    nav = [c for c in efectivos if c["eje"] == "navegabilidad"][:2]
    casos = nav[:1] + fid + nav[1:]   # intercalado arbitrario, orden estable
    print("  casos del dry run:", [c["caso_id"] for c in casos])

    # gold ids del censo v3 para los 2 casos de navegabilidad
    censo = json.load(open(EV2_DIR / "censo" / "censo_navegabilidad_v3.json",
                           encoding="utf-8"))
    por_sample = {c["sample_id"]: c for c in censo["casos"]}
    gold = {}
    for c in nav:
        anc = por_sample[c["sample_id"]]["anclas"][0]
        gold[c["caso_id"]] = anc["nodos_gold"][0]

    # precondición: buscar_nodos(gold_id, 50) DEBE devolver el gold (visto)
    index = GraphIndex(cargar_runtime("v3"))
    for cid, gid in gold.items():
        res = index.buscar_nodos(gid, 50)
        ok = any(r["id"] == gid for r in res["resultados"])
        check(f"precondición: buscar_nodos devuelve el gold de {cid}", ok)

    # guion global en el orden de `casos`
    script = []
    for c in casos:
        if c["eje"] == "navegabilidad":
            gid = gold[c["caso_id"]]
            script.append(turno_tool("buscar_nodos",
                                     {"consulta": gid, "limite": 50}, "t_b"))
            if c is nav[0]:
                script.append(turno_tool("ver_nodo", {"id": gid}, "t_v"))
            script.append(turno_final(f"dry run navegabilidad {c['caso_id']}"))
        else:
            script.append(turno_tool("buscar_nodos",
                                     {"consulta": "selftest fidelidad"}, "t_b"))
            script.append(turno_final(f"dry run fidelidad {c['caso_id']}"))

    fake = FakeSequential(script)
    outdir = SELFTEST_DIR / "trazas"
    resumen = correr_grafo("v3", client_real=fake, db_path=DB_PATH,
                           label=LABEL, casos=casos, outdir=outdir)
    check("el guion se consumió completo (todas las llamadas previstas)",
          fake.calls == len(script))
    check("resumen: 4 casos corridos", resumen["n_casos_corridos"] == 4)

    # --- 1) persistencia completa por caso ---
    META_KEYS = {"unidad", "label", "grafo", "kg_path", "kg_sha256", "eje",
                 "caso_id", "pos_orden_global", "pos_orden_efectivo",
                 "semilla_orden", "n_rep", "model", "temperature",
                 "max_tool_calls", "thinking_enabled", "timestamp_inicio",
                 "timestamp_fin", "code_version", "graph_fingerprint",
                 "cache_turnos", "fidelidad_sin_evaluar"}
    persistidos = sorted(outdir.glob("*.json"))
    check("4 trazas + 1 resumen persistidos", len(persistidos) == 5)
    payloads = {}
    for c in casos:
        p = outdir / f"{_sanitizar(c['caso_id'])}.json"
        with p.open(encoding="utf-8") as f:
            payloads[c["caso_id"]] = json.load(f)
    ok_meta = all(META_KEYS <= set(pl["meta"]) for pl in payloads.values())
    check("metadata completa en los 4 casos", ok_meta)
    ok_full = all(
        sf["output_chars"] == len(json.dumps(sf["output"], ensure_ascii=False))
        for pl in payloads.values() for sf in pl["steps_full"])
    check("steps_full sin truncar (output_chars == len(json))", ok_full)
    ok_1a1 = all(len(pl["steps_full"]) == pl["trace"]["tool_calls_used"]
                 for pl in payloads.values())
    check("steps_full 1:1 con tool_calls_used", ok_1a1)
    ok_raw = all(len(pl["raw_turns_agent"]) == len(pl["trace"]["api_calls"])
                 for pl in payloads.values())
    check("raw_turns_agent == nº de llamadas API por caso", ok_raw)
    ok_fid = all(pl["trace"]["parse_ok"] and pl["trace"]["final_json"]
                 and pl["meta"]["fidelidad_sin_evaluar"]
                 for cid, pl in payloads.items() if cid.startswith("EV2F"))
    check("fidelidad: respuesta final persistida sin evaluar", ok_fid)

    # --- 2) cero juez: la db solo tiene domain='agent' ---
    conn = sqlite3.connect(DB_PATH)
    domains = [r[0] for r in conn.execute(
        "SELECT DISTINCT domain FROM cache UNION "
        "SELECT DISTINCT domain FROM access_log")]
    conn.close()
    check("db de caché sin dominio de juez (solo 'agent')",
          domains == ["agent"])

    # --- 3) replay: misma corrida, cliente que explota -> 100% hits ---
    outdir2 = SELFTEST_DIR / "trazas_replay"
    resumen2 = correr_grafo("v3", client_real=ExplodingClient(),
                            db_path=DB_PATH, label=LABEL + "_replay",
                            casos=casos, outdir=outdir2)
    ok_hits = all(True for _ in [0]) and resumen2["cache_stats"]["misses"] == 0 \
        and resumen2["cache_stats"]["hits"] == len(script)
    check("replay 100% hits (0 misses, ninguna llamada real)", ok_hits)
    pl2 = json.load(open(outdir2 / f"{_sanitizar(casos[0]['caso_id'])}.json",
                         encoding="utf-8"))
    check("replay reproduce la misma respuesta final",
          pl2["trace"]["final_json"] ==
          payloads[casos[0]["caso_id"]]["trace"]["final_json"])

    # --- 4) métrica determinística auto-verificada ---
    aptos = {r["sample_id"]: r for r in cargar_aptos()}
    ancla_index = indice_anclas("v3")
    ev1 = evaluar_caso(payloads[nav[0]["caso_id"]],
                       aptos[nav[0]["sample_id"]]["gold"]["anclas"],
                       ancla_index, index)
    ev2 = evaluar_caso(payloads[nav[1]["caso_id"]],
                       aptos[nav[1]["sample_id"]]["gold"]["anclas"],
                       ancla_index, index)
    a1, a2 = ev1["por_ancla"][0], ev2["por_ancla"][0]
    check("métrica caso 1: ancla VISTA y CONSULTADA (scripteado ver_nodo)",
          a1["vista"] and a1["consultada"] and not a1["brecha_vista_sin_consultar"])
    check("métrica caso 2: ancla VISTA sin consultar -> BRECHA",
          a2["vista"] and not a2["consultada"] and a2["brecha_vista_sin_consultar"])
    check("replay estándar OK en ambos casos",
          ev1["replay_ok"] and ev2["replay_ok"])
    check("replay FUERTE OK en ambos casos (steps_full == re-ejecución)",
          ev1["replay_fuerte_ok"] and ev2["replay_fuerte_ok"])

    # --- resultado ---
    print("\n  archivos persistidos del dry run:")
    for p in sorted(SELFTEST_DIR.rglob("*.json")):
        print(f"    {p.relative_to(EV2_DIR)}  ({p.stat().st_size} bytes)")
    print(f"    cache/{DB_PATH.name}  ({DB_PATH.stat().st_size} bytes)")

    passed = sum(ok for _, ok in _checks)
    print(f"\n  {passed}/{len(_checks)} checks OK")
    print("  RESULTADO:", "PASS" if passed == len(_checks) else "FAIL")
    return 0 if passed == len(_checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
