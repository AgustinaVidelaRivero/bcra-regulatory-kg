"""
runner_retest_b54.py — U-B5.4 mini-ciclo del laudo de cierre: 3 retests
dirigidos (H1a/H4a/H2a) bajo el prefijo v3 RE-SELLADO (35e88c2dd0a2…,
namespace 54a111e2175f). Predicciones selladas ANTES de correr en
predicciones_retest_miniciclo_b54.md; tope = remanente USD 0,2098 con freno
duro. Misma disciplina que runner_pareada_b54 (cinco decisiones de caching,
patrón llm-capture, secuencial, log de usage por llamada, cruce db==jsonl).

Uso: .venv/bin/python data/experiment/b54_catalogo_v3/code/runner_retest_b54.py
"""

from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path

_CODE_DIR = Path(__file__).resolve().parent
_UNIT = _CODE_DIR.parent
_REPO = _CODE_DIR.parents[3]
_EVAL_DIR = _REPO / "data" / "experiment" / "evaluacion"
for _p in (str(_CODE_DIR), str(_EVAL_DIR)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import anthropic  # noqa: E402
from dotenv import load_dotenv  # noqa: E402

import llm_cache as lc  # noqa: E402
import prompt_v3_b54 as v3  # noqa: E402
from runner_pareada_b54 import (  # noqa: E402 — helpers compartidos de la unidad
    MODEL, cargar_chunks, costo_usd, usage_de, tool_input_de,
)

SHA_SELLADO_RETEST = "35e88c2dd0a2920302c29005b08ab9689405606d4bd5fcf8fb7ce807b1a3c512"
TOPE_USD = 0.2098  # remanente (laudo de cierre §2)

SELECCION_RETEST: tuple[tuple[str, str], ...] = (
    ("cap::3.1.14::intro", "R1-H1a-rename"),
    ("ayccef::2.1", "R2-H4a-def"),
    ("cryl::1.3", "R3-H2a-guarda"),
)

CACHE_DB = _UNIT / "cache" / "pareada_b54.db"
LOG_USAGE = _UNIT / "logs" / "cache_usage_pareada_b54.jsonl"
OUT_JSONL = _UNIT / "resultados_retest_miniciclo_b54.jsonl"
OUT_GASTO = _UNIT / "gasto_retest_miniciclo_b54.json"


def main() -> None:
    if v3.PREFIJO_SHA256_V3 != SHA_SELLADO_RETEST:
        raise RuntimeError(
            f"prefijo v3 en disco ({v3.PREFIJO_SHA256_V3[:12]}…) != re-sellado "
            f"({SHA_SELLADO_RETEST[:12]}…) — se frena SIN gastar")

    load_dotenv(_EVAL_DIR / ".env")
    import os
    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise RuntimeError("falta ANTHROPIC_API_KEY — se frena sin gastar")

    chunks = cargar_chunks()  # carga la selección de la pareada; incluye las 3
    for cid, _ in SELECCION_RETEST:
        if cid not in chunks:
            raise RuntimeError(f"chunk {cid} no está en la selección cargada — se frena")

    namespace = lc.make_namespace(
        "extraccion_pareada_b54",
        code_ver=f"pareada-b54-v1+{v3.PREFIJO_HASH_V3}",
        graph_fp=None, thinking=False)
    real = anthropic.Anthropic(max_retries=3)
    client = lc.CachingClient(
        real, namespace=namespace, db_path=CACHE_DB,
        domain="extraccion_pareada_b54", thinking_enabled=False,
        run_label="retest_b54_miniciclo")
    print(f"retests: {len(SELECCION_RETEST)} unidades | namespace: {namespace}")

    gasto = 0.0
    resultados: list[dict] = []
    log_f = open(LOG_USAGE, "a")
    try:
        for cid, tag in SELECCION_RETEST:  # SECUENCIAL (decisión 4)
            if gasto >= TOPE_USD:
                raise RuntimeError(f"FRENO DURO: USD {gasto:.4f} >= tope {TOPE_USD} — ABORTADO")
            kwargs = v3.build_request_kwargs_v3(chunks[cid], MODEL)
            hits_antes = client.stats()["hits"]
            resp = client.messages.create(**kwargs)
            fue_hit = client.stats()["hits"] > hits_antes
            u = usage_de(resp)
            costo = 0.0 if fue_hit else costo_usd(u)
            gasto += costo
            log_f.write(json.dumps({
                "ts": datetime.now().isoformat(), "component": "retest_b54",
                "doc": cid, "hit": fue_hit, "model": resp.model,
                "stop_reason": resp.stop_reason, **u, "costo_usd": round(costo, 6),
            }, ensure_ascii=False) + "\n")
            log_f.flush()
            resultados.append({
                "chunk_id": cid, "retest": tag, "hit": fue_hit,
                "model_resuelto": resp.model, "stop_reason": resp.stop_reason,
                "usage": u, "costo_usd": round(costo, 6),
                "tool_input_crudo": tool_input_de(resp),
            })
            print(f"  [{tag}] {cid}: {'HIT' if fue_hit else 'miss'} "
                  f"stop={resp.stop_reason} costo={costo:.4f} acum={gasto:.4f}")
            if gasto >= TOPE_USD:
                raise RuntimeError(f"FRENO DURO: USD {gasto:.4f} >= tope {TOPE_USD} — DETENIDO")
    finally:
        log_f.close()
        with open(OUT_JSONL, "w") as f:
            for r in resultados:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        OUT_GASTO.write_text(json.dumps({
            "unidades": len(resultados), "gasto_usd": round(gasto, 4),
            "tope_usd": TOPE_USD, "modelo_pedido": MODEL,
            "modelos_resueltos": sorted({r["model_resuelto"] for r in resultados}),
            "namespace": namespace, "stats_cache": client.stats(),
        }, ensure_ascii=False, indent=1))
        client.close()

    import sqlite3
    conn = sqlite3.connect(CACHE_DB)
    n_db = conn.execute("SELECT COUNT(*) FROM cache WHERE namespace = ?", (namespace,)).fetchone()[0]
    n_acc = conn.execute("SELECT COUNT(*) FROM access_log WHERE run_label = 'retest_b54_miniciclo'").fetchone()[0]
    conn.close()
    misses = sum(1 for r in resultados if not r["hit"])
    print(f"\ncruce db==jsonl: {len(resultados)} jsonl | {n_db} cache (misses {misses}) | {n_acc} accesos")
    if n_db != misses:
        raise RuntimeError("cruce db==jsonl FALLÓ")
    print(f"GASTO REAL RETESTS: USD {gasto:.4f} (tope {TOPE_USD})")


if __name__ == "__main__":
    main()
