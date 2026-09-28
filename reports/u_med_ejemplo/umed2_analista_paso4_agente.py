#!/usr/bin/env python3
"""U-MED-EJEMPLO-2, Paso 4 — Tres corridas del agente (GraphAgentNeo4j sobre KG_Reextraido_r1,
modo fulltext) con la pregunta del analista, sin juez.

Instanciación como el runner de la tanda 0 (data/experiment/ev2_tanda0/code/runner_ev2_neo4j.py,
leído, no importado):
  - modo 'fulltext' (línea 107), driver abrir_driver() (395), Neo4jIndex(driver, grafo, modo) (397);
  - agente con cache_conversation=True (252) y cliente CachingClient (182-191) con namespace
    agent|gfp=<sha sellado>|neo4j:<modo>:<índice> (176-179) sobre anthropic.Anthropic(max_retries=3)
    tras load_dotenv(evaluacion/.env) (réplica de runner_ev2._real_client, runner_ev2.py:234-240).
  - La captura íntegra de outputs replica FullCaptureAgentNeo4j (runner_ev2_neo4j.py:149-170) como
    subclase de GraphAgentNeo4j, sin tocar ask ni el loop del harness.
Una db de caché NUEVA por corrida en /tmp/u_med_ejemplo/ (sin hits entre corridas); jamás la
db por defecto de llm_cache (evaluacion/cache/calls.db).
Modos:  --config  (sin API: modelo, sha256 de instrucciones, tope, índice; escribe *_config.json)
        --correr  (API: hasta tres corridas; FRENO si fallan dos seguidas)
Uso: PYTHONDONTWRITEBYTECODE=1 <REPO>/.venv/bin/python umed2_analista_paso4_agente.py <REPO> --config|--correr
"""
import hashlib, json, sqlite3, sys
from datetime import datetime
from pathlib import Path

REPO = Path(sys.argv[1])
MODO = sys.argv[2]
assert MODO in ("--config", "--correr"), MODO
EXP = REPO / "data/experiment"
EVAL_DIR = EXP / "evaluacion"
sys.path.insert(0, str(EXP / "neo4j"))
from grafos import GRAFOS, verificar_sha  # noqa: E402  (agrega EVAL_DIR al path)
import harness  # noqa: E402  (solo import)
import llm_cache as lc  # noqa: E402  (solo import)
from agente_neo4j import GraphAgentNeo4j  # noqa: E402  (sin modificar)
from neo4j_index import Neo4jIndex  # noqa: E402  (sin modificar)
from conexion import abrir_driver  # noqa: E402

OUT = Path("/tmp/u_med_ejemplo")
PFX = "umed2_analista_"
GRAFO = "KG_Reextraido_r1"
MODO_INDICE = "fulltext"
N_CORRIDAS = 3
PREGUNTA = ("Para una entidad financiera, ¿qué condiciones hacen que los créditos para consumo o "
            "vivienda deban clasificarse en la cartera comercial?")
# mismos sellos que runner_ev2_neo4j.py:116-125 para los módulos que se importan acá
SELLOS = {
    EVAL_DIR / "harness.py": "fd267e833866f86850e43130e627b08d78e05523b97484696de0ab0c8c9fba9e",
    EXP / "neo4j" / "agente_neo4j.py": "403a9b4295961f461c73a35b46ccc4d973a20cefdddf2ae97b50231dd7a3576a",
    EXP / "neo4j" / "neo4j_index.py": "5f38db1b915caf8a4cd71e0f7f0d281ba5a9ca6867d327a9e0f4aac67cd2d0c1",
}


def sha(b):
    return hashlib.sha256(b).hexdigest()


class AgenteCaptura(GraphAgentNeo4j):
    """GraphAgentNeo4j con registro del output íntegro de cada tool call (réplica de
    FullCaptureAgentNeo4j, runner_ev2_neo4j.py:149-170)."""

    def __init__(self, indice, client=None, cache_conversation=True):
        super().__init__(indice, client=client, cache_conversation=cache_conversation)
        self.full_outputs = []

    def _run_tool(self, name, args):
        result = super()._run_tool(name, args)
        s = json.dumps(result, ensure_ascii=False)
        self.full_outputs.append({"n": len(self.full_outputs) + 1, "tool": name, "input": args,
                                  "output": result, "output_chars": len(s)})
        return result


def verificar_sellos():
    out = {}
    for p, esperado in SELLOS.items():
        got = sha(p.read_bytes())
        if got != esperado:
            raise SystemExit(f"SELLO ROTO: {p} {got} != {esperado}")
        out[str(p.relative_to(REPO))] = got
    return out


def config(indice):
    return {
        "modelo": harness.MODEL, "modelo_origen": "data/experiment/evaluacion/harness.py:47",
        "temperature": harness.TEMPERATURE, "temperature_origen": "harness.py:48",
        "max_tokens": harness.MAX_TOKENS, "max_tokens_origen": "harness.py:49",
        "tope_tool_calls": harness.MAX_TOOL_CALLS, "tope_origen": "harness.py:50 (forzado final en harness.py:527-536)",
        "instrucciones_sha256_utf8": sha(harness.SYSTEM_PROMPT.encode("utf-8")),
        "instrucciones_origen": "harness.SYSTEM_PROMPT, harness.py:61-92",
        "instrucciones_n_chars": len(harness.SYSTEM_PROMPT),
        "tools_sha256_json_sort_keys": sha(json.dumps(harness.TOOLS, ensure_ascii=False, sort_keys=True).encode("utf-8")),
        "tools_origen": "harness.TOOLS, harness.py:240-286",
        "indice_clase": f"{type(indice).__module__}.{type(indice).__name__}",
        "indice_grafo": indice.grafo, "indice_label": indice.label, "indice_modo": indice.modo,
        "indice_fulltext": indice.indice,
        "indice_origen": "neo4j_index.py:105-109 (indice = GRAFOS[grafo]['indice_fulltext'], grafos.py:80); "
                         "modo fulltext = runner_ev2_neo4j.py:107",
        "cache_conversation": True, "cache_conversation_origen": "runner_ev2_neo4j.py:252",
        "sellos": verificar_sellos(),
    }


def turnos_crudos(db):
    con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    filas = con.execute("SELECT c.*, a.ts AS acc_ts, a.hit AS acc_hit, a.run_label AS acc_label "
                        "FROM access_log a JOIN cache c ON c.key = a.key ORDER BY a.rowid").fetchall()
    con.close()
    return [{"access_ts": f["acc_ts"], "hit": f["acc_hit"], "run_label": f["acc_label"], "key": f["key"],
             "model": f["model"], "input_tokens": f["input_tokens"], "output_tokens": f["output_tokens"],
             "cache_read_tokens": f["cache_read_tokens"], "cache_write_tokens": f["cache_write_tokens"],
             "stop_reason": f["stop_reason"], "raw": json.loads(f["raw_json"])} for f in filas]


def main():
    kg_sha = verificar_sha(GRAFO)
    driver = abrir_driver()
    try:
        indice = Neo4jIndex(driver, grafo=GRAFO, modo=MODO_INDICE)
        cfg = config(indice)
        cfg["kg_sha256"] = kg_sha
        # instancia de verificación, sin cliente real: el agente efectivamente usa este índice
        dummy = AgenteCaptura(indice, client=object(), cache_conversation=True)
        cfg["agente_clase_base"] = "agente_neo4j.GraphAgentNeo4j (agente_neo4j.py:56-65)"
        cfg["agente_index_es_el_neo4jindex"] = dummy.index is indice
        cfg["agente_backend"] = dummy.backend
        if MODO == "--config":
            (OUT / f"{PFX}paso4_config.json").write_text(json.dumps(cfg, ensure_ascii=False, indent=1), encoding="utf-8")
            print(json.dumps(cfg, ensure_ascii=False, indent=1))
            return 0

        from dotenv import load_dotenv
        import os
        load_dotenv(EVAL_DIR / ".env")
        if not os.environ.get("ANTHROPIC_API_KEY", "").strip():
            raise SystemExit("FRENO: ANTHROPIC_API_KEY no disponible")
        import anthropic
        real = anthropic.Anthropic(max_retries=3)
        gfp = f"{GRAFOS[GRAFO]['sha256']}|neo4j:{indice.modo}:{indice.indice}"
        cv = lc.code_version()
        resumen, fallas_seguidas = [], 0
        for c in range(1, N_CORRIDAS + 1):
            db = OUT / f"{PFX}paso4_cache_c{c}.db"
            traza = OUT / f"{PFX}paso4_traza_c{c}.json"
            if db.exists() or traza.exists():
                raise SystemExit(f"FRENO: {db.name} o {traza.name} ya existe; no se sobrescribe")
            cache = lc.CachingClient(real, domain="agent", db_path=db,
                                     namespace=lc.make_namespace("agent", code_ver=cv, graph_fp=gfp, thinking=False),
                                     thinking_enabled=False, run_label=f"{PFX}c{c}")
            agente = AgenteCaptura(indice, client=cache, cache_conversation=True)
            t0 = datetime.now().isoformat(timespec="seconds")
            tr = agente.ask(f"umed2_analista_c{c}", PREGUNTA)
            t1 = datetime.now().isoformat(timespec="seconds")
            stats = cache.stats()
            cache.close()
            crudos = turnos_crudos(db)
            payload = {"meta": {"corrida": c, "grafo": GRAFO, "kg_sha256": kg_sha, "backend": agente.backend,
                                "model": harness.MODEL, "temperature": harness.TEMPERATURE,
                                "max_tool_calls": harness.MAX_TOOL_CALLS, "cache_conversation": True,
                                "code_version": cv, "graph_fingerprint": gfp, "cache_db": str(db),
                                "cache_stats": stats, "timestamp_inicio": t0, "timestamp_fin": t1,
                                "model_segun_api": sorted({t["raw"].get("model") for t in crudos} - {None})},
                       "pregunta": PREGUNTA, "trace": vars(tr), "steps_full": agente.full_outputs,
                       "raw_turns_agent": crudos}
            traza.write_text(json.dumps(payload, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
            resumen.append({"corrida": c, "tools": tr.tool_calls_used, "parse_ok": tr.parse_ok,
                            "hit_tool_limit": tr.hit_tool_limit, "error": tr.error, "costo_usd": tr.cost_usd,
                            "cache_stats": stats})
            print(f"corrida {c}: tools={tr.tool_calls_used} parse_ok={tr.parse_ok} error={tr.error} "
                  f"costo=${tr.cost_usd:.6f} hits={stats['hits']}/{stats['accesses']}", flush=True)
            fallas_seguidas = fallas_seguidas + 1 if tr.error else 0
            if fallas_seguidas >= 2:
                print("FRENO: la API falló dos veces seguidas", flush=True)
                break
        (OUT / f"{PFX}paso4_resumen.json").write_text(json.dumps(
            {"corridas": resumen, "costo_total_usd": round(sum(r["costo_usd"] for r in resumen), 6),
             "sellos_al_final": verificar_sellos()}, ensure_ascii=False, indent=1), encoding="utf-8")
    finally:
        driver.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
