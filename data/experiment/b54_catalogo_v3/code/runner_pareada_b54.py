"""
runner_pareada_b54.py — U-B5.4 fase 3: corrida de la verificación pareada.

34 unidades ya extraídas (6 brazos, predicciones SELLADAS por el commit
f19e978 en predicciones_pareada_selladas_b54.md) re-extraídas bajo el prefijo
v3 (sha 29af2e29880b…, namespace 4ed889c74cb8). Autorización de gasto: tope
USD 0,50 con FRENO DURO en el runner.

Cumple docs/decisiones_caching_extraccion.md (las cinco, vinculantes):
  D1 — prefijo v3 como bloque system con cache_control ephemeral y todo lo
       variable en el mensaje (build_request_kwargs_v3);
  D2 — costo SIEMPRE con la fórmula de caching (in×1 + cw×1.25 + cr×0.10 +
       out×precio_salida);
  D3 — una línea JSON de usage por response real de la API
       (logs/cache_usage_pareada_b54.jsonl, component="pareada_b54");
  D4 — corrida SECUENCIAL (prefijo idéntico entre llamadas);
  D5 — no toca el pipeline de evaluación (esto es extracción; la caché local
       es la capa llm_cache con .db PROPIA de la unidad).

Patrón llm-capture: CachingClient (write-through, crudo íntegro, errores no
se cachean) sobre anthropic.Anthropic(max_retries=3); namespace con el hash
del prefijo v3 embebido en code_ver (rotación de namespace aceptada);
never-pay-twice (los hits no suman gasto). Cruce db==jsonl al cierre.

Uso (desde cualquier cwd, venv de la raíz):
    .venv/bin/python data/experiment/b54_catalogo_v3/code/runner_pareada_b54.py
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

import llm_cache as lc  # noqa: E402 — capa sellada, SOLO se importa
import prompt_v3_b54 as v3  # noqa: E402

# ------------------------------ constantes ------------------------------- #

MODEL = "claude-haiku-4-5"  # modelo de E1 en producción (runner_faseB_e1.py)
TOPE_USD = 0.50             # freno duro (autorización de fase 3)
SHA_SELLADO = "29af2e29880b8e435cc40a93913b911ae9db9d2feab43d06c9ecfca2e3652edf"

# Precios claude-haiku-4-5 (USD/MTok) — fórmula de la decisión 2.
PRICE_IN, PRICE_OUT = 1.00, 5.00
PRICE_CW, PRICE_CR = 1.25, 0.10

CACHE_DB = _UNIT / "cache" / "pareada_b54.db"
LOG_USAGE = _UNIT / "logs" / "cache_usage_pareada_b54.jsonl"
OUT_JSONL = _UNIT / "resultados_pareada_b54.jsonl"
OUT_GASTO = _UNIT / "gasto_pareada_b54.json"

# Selección SELLADA (predicciones_pareada_selladas_b54.md, commit f19e978):
# 34 unidades en 6 brazos. dev = chunks de e0_chunking/salida_enm01;
# esq2/68 = chunks de escalado_prep/e0_dry.
SELECCION: tuple[tuple[str, str], ...] = (
    # Brazo A — estabilidad de los 5 roles dev (10)
    ("cap::1.1", "A"), ("cap::1.2", "A"), ("cla::1.1", "A"), ("cla::1.2.1", "A"),
    ("pro::1.1.1", "A"), ("pro::1.1.2.7", "A"), ("ric::1.1", "A"), ("ric::1.2", "A"),
    ("ext::1.2", "A"), ("ext::1.3", "A"),
    # Brazo B — atracción cross-TO observada (8)
    ("ayccef::2.9.2::intro", "B"), ("actgar::2.3.6.3", "B"), ("actgar::2.7.2", "B"),
    ("expaef::5.7.1.2", "B"), ("expaef::5.7.1.3", "B"), ("lavdin::1.1.1", "B"),
    ("lavdin::1.3.3", "B"), ("cryl::4.1", "B"),
    # Brazo C — propuesto → adiciones F1.4 (7)
    ("cap::6.2.1.1", "C"), ("cryl::3.1", "C"), ("traval::1.1::intro", "C"),
    ("traval::2.3", "C"), ("traval::S2::cierre", "C"), ("expaef::9.3", "C"),
    ("expaef::9.5.3", "C"),
    # Brazo D — anti-atracción de potestades (5)
    ("ayccef::2.1", "D"), ("ayccef::3.1", "D"), ("ayccef::4.1", "D"),
    ("cryl::1.3", "D"), ("cryl::3.2::intro", "D"),
    # Brazo E — controles de clase estable (3)
    ("actgar::1.2", "E"), ("actgar::2.2.2", "E"), ("actgar::2.4.1", "E"),
    # Brazo F — anti-atracción del id SNP nuevo (1)
    ("cap::3.1.14::intro", "F"),
)

TOS_DEV = ("cap", "cla", "ext", "pro", "ric")


def cargar_chunks() -> dict[str, dict]:
    """Carga los dicts de chunk de las mismas fuentes que las extracciones
    persistidas: dev = e0_chunking/salida_enm01; ESQ-2/68 = e0_dry."""
    necesarios = {cid for cid, _ in SELECCION}
    tos = sorted({cid.split("::", 1)[0] for cid in necesarios})
    chunks: dict[str, dict] = {}
    for to in tos:
        if to in TOS_DEV:
            path = _REPO / "data/experiment/reextraccion_v2/e0_chunking/salida_enm01" / f"chunks_{to}.json"
        else:
            path = _REPO / "data/experiment/escalado_prep/e0_dry" / to / f"chunks_{to}.json"
        for ch in json.loads(path.read_text()):
            if ch["id"] in necesarios:
                if ch["id"] in chunks:
                    raise RuntimeError(f"chunk duplicado en fuente: {ch['id']} — se frena")
                chunks[ch["id"]] = ch
    faltan = necesarios - set(chunks)
    if faltan:
        raise RuntimeError(f"chunks no encontrados: {sorted(faltan)} — se frena")
    return chunks


def costo_usd(u: dict) -> float:
    """Fórmula de caching (decisión 2)."""
    return (u.get("input_tokens", 0) * PRICE_IN
            + u.get("cache_creation_input_tokens", 0) * PRICE_CW
            + u.get("cache_read_input_tokens", 0) * PRICE_CR
            + u.get("output_tokens", 0) * PRICE_OUT) / 1e6


def usage_de(resp) -> dict:
    u = resp.usage
    return {
        "input_tokens": getattr(u, "input_tokens", 0) or 0,
        "cache_creation_input_tokens": getattr(u, "cache_creation_input_tokens", 0) or 0,
        "cache_read_input_tokens": getattr(u, "cache_read_input_tokens", 0) or 0,
        "output_tokens": getattr(u, "output_tokens", 0) or 0,
    }


def tool_input_de(resp) -> dict | None:
    for b in resp.content:
        if getattr(b, "type", None) == "tool_use":
            return b.input
    return None


def main() -> None:
    # Candado del prefijo sellado: si el módulo no reproduce el sha del commit
    # f19e978, NO se gasta.
    if v3.PREFIJO_SHA256_V3 != SHA_SELLADO:
        raise RuntimeError(
            f"prefijo v3 en disco ({v3.PREFIJO_SHA256_V3[:12]}…) != sellado "
            f"({SHA_SELLADO[:12]}…) — se frena SIN gastar")

    load_dotenv(_EVAL_DIR / ".env")
    import os
    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise RuntimeError("falta ANTHROPIC_API_KEY (evaluacion/.env) — se frena sin gastar")

    chunks = cargar_chunks()
    print(f"selección sellada: {len(SELECCION)} unidades | chunks cargados: {len(chunks)}")

    CACHE_DB.parent.mkdir(parents=True, exist_ok=True)
    LOG_USAGE.parent.mkdir(parents=True, exist_ok=True)

    namespace = lc.make_namespace(
        "extraccion_pareada_b54",
        code_ver=f"pareada-b54-v1+{v3.PREFIJO_HASH_V3}",
        graph_fp=None, thinking=False)
    real = anthropic.Anthropic(max_retries=3)
    client = lc.CachingClient(
        real, namespace=namespace, db_path=CACHE_DB,
        domain="extraccion_pareada_b54", thinking_enabled=False,
        run_label="pareada_b54_f3")
    print(f"namespace: {namespace}")

    gasto = 0.0
    resultados: list[dict] = []
    log_f = open(LOG_USAGE, "a")
    try:
        # SECUENCIAL (decisión 4): un solo hilo, en orden de la selección.
        for cid, brazo in SELECCION:
            if gasto >= TOPE_USD:
                raise RuntimeError(
                    f"FRENO DURO: gasto acumulado USD {gasto:.4f} >= tope {TOPE_USD} "
                    f"antes de {cid} — corrida ABORTADA")
            kwargs = v3.build_request_kwargs_v3(chunks[cid], MODEL)
            hits_antes = client.stats()["hits"]
            resp = client.messages.create(**kwargs)
            fue_hit = client.stats()["hits"] > hits_antes
            u = usage_de(resp)
            costo = 0.0 if fue_hit else costo_usd(u)  # never-pay-twice
            gasto += costo
            # Decisión 3: una línea de usage por response real (los hits se
            # loguean marcados, con costo 0).
            log_f.write(json.dumps({
                "ts": datetime.now().isoformat(), "component": "pareada_b54",
                "doc": cid, "hit": fue_hit, "model": resp.model,
                "stop_reason": resp.stop_reason, **u,
                "costo_usd": round(costo, 6),
            }, ensure_ascii=False) + "\n")
            log_f.flush()
            ti = tool_input_de(resp)
            resultados.append({
                "chunk_id": cid, "brazo": brazo, "hit": fue_hit,
                "model_resuelto": resp.model, "stop_reason": resp.stop_reason,
                "usage": u, "costo_usd": round(costo, 6),
                "tool_input_crudo": ti,
            })
            n_rel = len((ti or {}).get("relations", []) or [])
            print(f"  [{brazo}] {cid}: {'HIT' if fue_hit else 'miss'} "
                  f"stop={resp.stop_reason} rel={n_rel} costo={costo:.4f} acum={gasto:.4f}")
            if gasto >= TOPE_USD:
                raise RuntimeError(
                    f"FRENO DURO: gasto acumulado USD {gasto:.4f} >= tope {TOPE_USD} "
                    f"tras {cid} — corrida DETENIDA")
    finally:
        log_f.close()
        with open(OUT_JSONL, "w") as f:
            for r in resultados:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        stats = client.stats()
        resumen = {
            "unidades_corridas": len(resultados), "gasto_usd": round(gasto, 4),
            "tope_usd": TOPE_USD, "modelo_pedido": MODEL,
            "modelos_resueltos": sorted({r["model_resuelto"] for r in resultados}),
            "namespace": namespace, "db": str(CACHE_DB.relative_to(_REPO)),
            "stats_cache": stats,
        }
        OUT_GASTO.write_text(json.dumps(resumen, ensure_ascii=False, indent=1))
        client.close()

    # ---- cruce db == jsonl (patrón llm-capture) ---- #
    import sqlite3
    conn = sqlite3.connect(CACHE_DB)
    n_db = conn.execute(
        "SELECT COUNT(*) FROM cache WHERE namespace = ?", (namespace,)).fetchone()[0]
    n_acc = conn.execute(
        "SELECT COUNT(*) FROM access_log WHERE run_label = 'pareada_b54_f3'").fetchone()[0]
    conn.close()
    misses = sum(1 for r in resultados if not r["hit"])
    print(f"\ncruce db==jsonl: {len(resultados)} líneas jsonl | {n_db} filas cache "
          f"(misses {misses}) | {n_acc} accesos logueados")
    if n_db != misses:
        raise RuntimeError("cruce db==jsonl FALLÓ: filas de caché != misses — revisar")
    print(f"GASTO REAL: USD {gasto:.4f} (tope {TOPE_USD}) | "
          f"modelos resueltos: {resumen['modelos_resueltos']}")


if __name__ == "__main__":
    main()
