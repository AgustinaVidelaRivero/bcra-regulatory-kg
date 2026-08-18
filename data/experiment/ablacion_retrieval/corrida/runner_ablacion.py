"""
runner_ablacion.py — Runner POR CELDA de la corrida factorial de la ablación
de retrieval (U-A1.4; pre-registro sellado `../preregistro_ablacion.md` §4 y §6).

Por celda: pares aptos × 2 variantes (los casos y su orden se DERIVAN de
`pares/pares_v3.json` con la semilla `orden-ablacion-v1`, mismo orden en las 4
celdas), agente `AgenteCelda` ensamblado desde la celda sellada (sha
verificado), caché `llm_cache.CachingClient` con UNA db fresca por celda
(`cache/ablacion_<celda>.db`, label `ablacion_<celda>`) y namespace
`agent|gfp=<sha KG-Refinado>|cv=<sha harness>+<sha celda>|think=0`.

Por caso persiste (formato de `ev2_corrida/code/runner_ev2.py`): meta, la
traza del harness (`vars(QuestionTrace)`), `steps_full` (outputs de tool
íntegros + latencia por tool), `raw_turns_agent` (crudos de la API vía
access_log). WRITE-THROUGH: cada caso se escribe apenas termina; la caché
persiste cada llamada antes de devolverla.

RETOMA (idempotente): un caso cuya traza ya existe en `trazas/<celda>/` se
SALTEA sin tocar la API ni la caché (0 accesos ⇒ 0 hits). Si una corrida se
interrumpió a mitad de un caso, al retomarlo las llamadas ya pagadas vuelven
como hits de la MISMA db (legítimos, intra-db): el resumen los declara
(`cache_stats.hits`, `casos_con_hits`); el pre-registro exige `hits == 0` al
cierre de una celda corrida de una vez, y toda reanudación se declara.

GATING: modo real solo con `--autorizado` + `ABLACION_A14_TOPE_USD` + precios
por CLI (`--precio-in`, `--precio-out`, USD por MTok del modelo del agente,
verificados en la autorización). Cuota por celda = tope / 4 (§6). FRENO por
proyección: con ≥ 3 casos hechos, si gasto_celda / hechos × previstos > cuota,
la celda se detiene y reporta. FRENO duro por falla del contenedor Neo4j
(conectividad verificada antes de cada caso y tras cada traza con error).
Un error permanente del harness/API en un caso NO frena: la traza se persiste
con `trace.error`, se declara y la métrica se computa sobre lo que hay
(precedente EA-013).

Costo: se persiste `trace.cost_usd` (fórmula y precios del harness, sin
tocar) Y `costo_usd_cli` (misma fórmula `harness.py:576-579`, precios de la
CLI). El freno y el reporte de gasto usan los precios de la CLI.

Uso (desde la raíz del repo):
  .venv/bin/python -B data/experiment/ablacion_retrieval/corrida/runner_ablacion.py \
      --celda all --autorizado --precio-in 1.00 --precio-out 5.00
  (ABLACION_A14_TOPE_USD=20 en el entorno; `--celda C00_booleano_v1` para una)
"""

from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys
from datetime import datetime
from pathlib import Path

CORRIDA_DIR = Path(__file__).resolve().parent
if str(CORRIDA_DIR) not in sys.path:
    sys.path.insert(0, str(CORRIDA_DIR))

from comun_corrida import (CACHE_DIR, EVAL_DIR, GRAFO, KG_REFINADO_PATH,  # noqa: E402
                           KG_REFINADO_SHA256, ORDEN_CELDAS, SEMILLA_ORDEN,
                           TRAZAS_DIR, UNIDAD, cargar_celda, cargar_manifest_celdas,
                           cargar_pares, kg_vacio_refinado, namespace_celda,
                           orden_resuelto, rel_repo, sanitizar, verificar_kg_meta)
from agente_celda import AgenteCelda  # noqa: E402

RUNNERS_DIR = EVAL_DIR / "runners"
if str(RUNNERS_DIR) not in sys.path:
    sys.path.insert(0, str(RUNNERS_DIR))

import harness  # noqa: E402  (congelado; solo se importa)
import llm_cache as lc  # noqa: E402
from run_posthoc import _max_access_rowid, _turns_since  # noqa: E402

TOPE_ENV = "ABLACION_A14_TOPE_USD"
N_CELDAS = 4
MIN_HECHOS_PROYECCION = 3


# --------------------------------------------------------------------------- #
# Costo con precios de la CLI (fórmula del harness, harness.py:576-579)        #
# --------------------------------------------------------------------------- #
def costo_cli(tokens_in: int, tokens_out: int, cache_read: int, cache_write: int,
              precio_in: float, precio_out: float) -> float:
    return round((tokens_in * precio_in
                  + cache_write * precio_in * harness.CACHE_WRITE_MULT
                  + cache_read * precio_in * harness.CACHE_READ_MULT) / 1e6
                 + (tokens_out * precio_out) / 1e6, 6)


def label_celda(celda_id: str) -> str:
    return f"ablacion_{celda_id}"


def db_celda(celda_id: str) -> Path:
    return CACHE_DIR / f"{label_celda(celda_id)}.db"


def outdir_celda(celda_id: str) -> Path:
    return TRAZAS_DIR / celda_id


def path_traza(outdir: Path, caso_id: str) -> Path:
    return outdir / f"{sanitizar(caso_id)}.json"


def _cargar_traza(p: Path) -> dict | None:
    try:
        with p.open(encoding="utf-8") as f:
            d = json.load(f)
        return d if "trace" in d and "meta" in d else None
    except (OSError, ValueError):
        return None


def build_cache_client(real_client, celda: dict, *, db_path: Path, label: str):
    kg = kg_vacio_refinado()
    gfp = lc.graph_fingerprint(kg)          # sha(LOADER_VERSION + kg.json) — cruzable con EV2
    cv = lc.code_version()                  # hash de harness/judge/loader (cuarteto)
    ns = namespace_celda(celda)
    cache = lc.CachingClient(real_client, domain="agent", db_path=db_path, namespace=ns,
                             thinking_enabled=False, run_label=label)
    return cache, cv, gfp, ns


def _conectividad_ok(driver) -> bool:
    try:
        driver.verify_connectivity()
        return True
    except Exception:  # noqa: BLE001 — cualquier falla del contenedor frena
        return False


# --------------------------------------------------------------------------- #
# Corrida de UNA celda                                                         #
# --------------------------------------------------------------------------- #
def correr_celda(celda_id: str, *, client_real, precio_in: float, precio_out: float,
                 cuota_usd: float, driver=None, casos: list[dict] | None = None,
                 outdir: Path | None = None, db_path: Path | None = None,
                 label: str | None = None, verificar_meta: bool = True,
                 freno_por_proyeccion: bool = True) -> dict:
    """Corre (o retoma) los casos de la celda con N=1. Devuelve el resumen (que
    también se escribe en `<outdir>/resumen_<label>.json`)."""
    if driver is None:
        from conexion import abrir_driver
        driver = abrir_driver()
    if verificar_meta:
        verificar_kg_meta(driver, GRAFO)
    manifest = cargar_manifest_celdas()
    celda = cargar_celda(celda_id, manifest)
    label = label or label_celda(celda_id)
    db_path = db_path or db_celda(celda_id)
    outdir = outdir or outdir_celda(celda_id)
    outdir.mkdir(parents=True, exist_ok=True)

    cache, cv, gfp, ns = build_cache_client(client_real, celda, db_path=db_path, label=label)
    agent = AgenteCelda(driver, celda, client=cache, cache_conversation=True,
                        manifest_celda=manifest["celdas"][celda_id])
    if casos is None:
        casos = orden_resuelto(cargar_pares())
    n_prev = len(casos)

    # Retoma: casos ya persistidos (válidos) se saltean; su gasto cuenta para la cuota.
    ya, gasto_previo = [], 0.0
    for c in casos:
        d = _cargar_traza(path_traza(outdir, c["caso_id"]))
        if d is not None:
            ya.append(c["caso_id"])
            gasto_previo += float(d["meta"].get("costo_usd_cli") or 0.0)
    print(f"== {UNIDAD} {celda_id} ({label}) — {n_prev} casos, {len(ya)} ya persistidos, "
          f"cuota ${cuota_usd:.4f}, precios in/out {precio_in}/{precio_out} USD/MTok ==", flush=True)

    resumenes, gasto_sesion, gasto_harness = [], 0.0, 0.0
    freno = None
    casos_con_hits = []
    t_celda_ini = datetime.now().isoformat(timespec="seconds")
    for c in casos:
        p_out = path_traza(outdir, c["caso_id"])
        if c["caso_id"] in ya:
            continue
        if not _conectividad_ok(driver):
            freno = {"tipo": "contenedor", "detalle": "Neo4j sin conectividad antes del caso",
                     "caso_id": c["caso_id"]}
            print(f"  FRENO DURO: {freno}", flush=True)
            break
        a0 = _max_access_rowid(cache)
        t_ini = datetime.now().isoformat(timespec="seconds")
        tr, steps_full = agent.ask_capturando(c["caso_id"], c["pregunta"])
        t_fin = datetime.now().isoformat(timespec="seconds")
        hits, n_turnos, raw_turns = _turns_since(cache, a0, "agent")
        c_cli = costo_cli(tr.tokens_in, tr.tokens_out, tr.cache_read, tr.cache_write,
                          precio_in, precio_out)
        payload = {
            "meta": {
                "unidad": UNIDAD, "label": label, "celda_id": celda_id,
                "retriever": celda["retriever"], "tools": celda["tools"],
                "es_control": celda["es_control"],
                "system_prompt_sha256": celda["system_prompt_sha256"],
                "tools_specs_sha256": celda["tools_specs_sha256"],
                "celda_archivo_sha256": celda["archivo_sha256"],
                "backend": agent.backend,
                "grafo": GRAFO, "kg_path": rel_repo(KG_REFINADO_PATH),
                "kg_sha256": KG_REFINADO_SHA256,
                "caso_id": c["caso_id"], "sample_id": c["sample_id"],
                "variante": c["variante"], "estrato": c["estrato"],
                "sub_estrato": c.get("sub_estrato"),
                "pos_orden": c.get("pos_orden"), "semilla_orden": SEMILLA_ORDEN,
                "n_rep": 1, "model": harness.MODEL, "temperature": harness.TEMPERATURE,
                "max_tokens": harness.MAX_TOKENS, "max_tool_calls": harness.MAX_TOOL_CALLS,
                "thinking_enabled": False, "cache_conversation": True,
                "timestamp_inicio": t_ini, "timestamp_fin": t_fin,
                "code_version": cv, "graph_fingerprint": gfp, "namespace": ns,
                "cache_turnos": {"hits": hits, "total": n_turnos},
                "precios_cli_usd_por_mtok": {"in": precio_in, "out": precio_out},
                "costo_usd_cli": c_cli,
                "precios_harness_usd_por_mtok": {"in": harness.PRICE_IN_PER_M,
                                                 "out": harness.PRICE_OUT_PER_M},
            },
            "pregunta": c["pregunta"],
            "trace": vars(tr),
            "steps_full": steps_full,
            "raw_turns_agent": raw_turns,
        }
        with p_out.open("w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False, indent=2)

        if hits:
            casos_con_hits.append({"caso_id": c["caso_id"], "hits": hits, "total": n_turnos})
        gasto_sesion += c_cli
        gasto_harness += tr.cost_usd
        resumenes.append({"caso_id": c["caso_id"], "variante": c["variante"],
                          "estrato": c["estrato"], "tools": tr.tool_calls_used,
                          "hit_tool_limit": tr.hit_tool_limit, "parse_ok": tr.parse_ok,
                          "error": tr.error, "latency_s": tr.latency_s,
                          "tokens_in": tr.tokens_in, "tokens_out": tr.tokens_out,
                          "cache_read": tr.cache_read, "cache_write": tr.cache_write,
                          "costo_usd_harness": tr.cost_usd, "costo_usd_cli": c_cli,
                          "cache_hits": hits, "api_calls": n_turnos})
        print(f"  [{c.get('pos_orden')}/{n_prev}] {c['caso_id']} tools={tr.tool_calls_used} "
              f"parse_ok={tr.parse_ok} hits={hits}/{n_turnos} costo=${c_cli:.5f}"
              + (f" ERROR={tr.error}" if tr.error else ""), flush=True)

        # Error en la traza: ¿fue el contenedor? (freno duro) o error API/harness (se declara).
        if tr.error and not _conectividad_ok(driver):
            p_mal = outdir / f"{sanitizar(c['caso_id'])}.freno_contenedor.json"
            p_out.replace(p_mal)
            freno = {"tipo": "contenedor", "detalle": f"Neo4j sin conectividad tras error: {tr.error}",
                     "caso_id": c["caso_id"], "traza_apartada": rel_repo(p_mal)}
            print(f"  FRENO DURO: {freno}", flush=True)
            resumenes[-1]["apartada_por_contenedor"] = True
            break

        # Freno por proyección (§6): cuota por celda = tope / 4.
        hechos = len(ya) + len(resumenes)
        gasto_total = gasto_previo + gasto_sesion
        if freno_por_proyeccion and hechos >= MIN_HECHOS_PROYECCION:
            proy = gasto_total / hechos * n_prev
            if proy > cuota_usd:
                freno = {"tipo": "proyeccion", "gasto_celda_usd": round(gasto_total, 4),
                         "hechos": hechos, "previstos": n_prev,
                         "proyeccion_usd": round(proy, 4), "cuota_usd": cuota_usd}
                print(f"  FRENO POR PROYECCIÓN: ${gasto_total:.4f} en {hechos} casos proyecta "
                      f"${proy:.4f} > cuota ${cuota_usd:.4f}. Celda detenida.", flush=True)
                break

    stats = cache.stats()
    cache.close()
    resumen = {
        "unidad": UNIDAD, "celda_id": celda_id, "label": label, "db": rel_repo(db_path),
        "trazas_dir": rel_repo(outdir), "namespace": ns,
        "timestamp_inicio": t_celda_ini,
        "timestamp_fin": datetime.now().isoformat(timespec="seconds"),
        "n_casos_previstos": n_prev,
        "n_ya_persistidos_al_iniciar": len(ya),
        "n_corridos_esta_sesion": len(resumenes),
        "n_persistidos_total": len(ya) + len([r for r in resumenes
                                              if not r.get("apartada_por_contenedor")]),
        "precios_cli_usd_por_mtok": {"in": precio_in, "out": precio_out},
        "cuota_celda_usd": cuota_usd,
        "gasto_previo_usd_cli": round(gasto_previo, 6),
        "gasto_sesion_usd_cli": round(gasto_sesion, 6),
        "gasto_sesion_usd_harness": round(gasto_harness, 6),
        "gasto_celda_total_usd_cli": round(gasto_previo + gasto_sesion, 6),
        "cache_stats": stats,
        "casos_con_hits_esta_sesion": casos_con_hits,
        "freno": freno,
        "code_version": cv, "graph_fingerprint": gfp,
        "casos": resumenes,
    }
    with (outdir / f"resumen_{label}.json").open("w", encoding="utf-8") as f:
        json.dump(resumen, f, ensure_ascii=False, indent=2)
    print(f"  -> {len(resumenes)} trazas nuevas en {rel_repo(outdir)} | gasto sesión "
          f"${gasto_sesion:.4f} (celda ${gasto_previo + gasto_sesion:.4f}) | hits={stats['hits']} "
          f"misses={stats['misses']}" + (f" | FRENO {freno['tipo']}" if freno else ""), flush=True)
    return resumen


# --------------------------------------------------------------------------- #
# Gasto real desde la db de una celda (una fila por llamada pagada)            #
# --------------------------------------------------------------------------- #
def gasto_desde_db(db_path: Path, precio_in: float, precio_out: float) -> dict | None:
    if not db_path.exists():
        return None
    con = sqlite3.connect(str(db_path))
    filas = con.execute("SELECT model, namespace, COUNT(*), SUM(input_tokens), SUM(output_tokens), "
                        "SUM(cache_read_tokens), SUM(cache_write_tokens) FROM cache "
                        "GROUP BY model, namespace").fetchall()
    acc = con.execute("SELECT run_label, hit, COUNT(*) FROM access_log "
                      "GROUP BY run_label, hit").fetchall()
    stops = con.execute("SELECT stop_reason, COUNT(*) FROM cache GROUP BY stop_reason").fetchall()
    con.close()
    por_modelo, total = [], 0.0
    for model, ns, n, tin, tout, cr, cw in filas:
        usd = costo_cli(tin or 0, tout or 0, cr or 0, cw or 0, precio_in, precio_out)
        total += usd
        por_modelo.append({"model": model, "namespace": ns, "llamadas_pagadas": n,
                           "input_tokens": tin, "output_tokens": tout, "cache_read_tokens": cr,
                           "cache_write_tokens": cw, "usd": round(usd, 4)})
    return {"db": rel_repo(db_path), "precios_usd_por_mtok": {"in": precio_in, "out": precio_out},
            "por_modelo": por_modelo, "usd_total": round(total, 4),
            "access_log": [{"run_label": r, "hit": bool(h), "n": n} for r, h, n in acc],
            "hits_total": sum(n for _, h, n in acc if h),
            "stop_reasons": {str(s): n for s, n in stops}}


# --------------------------------------------------------------------------- #
# CLI (modo real, gateado)                                                     #
# --------------------------------------------------------------------------- #
def _real_client(max_retries=3):
    from dotenv import load_dotenv
    load_dotenv(EVAL_DIR / ".env")
    if not os.environ.get("ANTHROPIC_API_KEY", "").strip():
        raise SystemExit(f"ERROR: ANTHROPIC_API_KEY no seteada ({EVAL_DIR / '.env'})")
    import anthropic
    return anthropic.Anthropic(max_retries=max_retries)


def main() -> int:
    ap = argparse.ArgumentParser(description="Corrida factorial de la ablación (fase B, gateada).")
    ap.add_argument("--celda", required=True, help=f"{ORDEN_CELDAS} o 'all' (orden pre-registrado)")
    ap.add_argument("--autorizado", action="store_true",
                    help="declara que la fase B fue autorizada con precios verificados y tope")
    ap.add_argument("--precio-in", type=float, default=None, help="USD por MTok de entrada (Haiku)")
    ap.add_argument("--precio-out", type=float, default=None, help="USD por MTok de salida (Haiku)")
    args = ap.parse_args()

    if not args.autorizado:
        raise SystemExit("ABORTADO: falta --autorizado. Ninguna llamada a API sin autorización.")
    tope = os.environ.get(TOPE_ENV, "").strip()
    if not tope:
        raise SystemExit(f"ABORTADO: falta {TOPE_ENV} (tope declarado en la autorización).")
    if args.precio_in is None or args.precio_out is None:
        raise SystemExit("ABORTADO: faltan --precio-in / --precio-out (verificados en la autorización).")
    tope_usd = float(tope)
    cuota = tope_usd / N_CELDAS

    from comun_ablacion import verificar_piezas
    print("piezas selladas:")
    verificar_piezas()
    from conexion import abrir_driver
    driver = abrir_driver()
    meta = verificar_kg_meta(driver, GRAFO)
    print(f"KG_Meta OK: {meta['kg_sha256']}")
    real = _real_client()
    celdas = ORDEN_CELDAS if args.celda == "all" else [args.celda]
    for cid in celdas:
        if cid not in ORDEN_CELDAS:
            raise SystemExit(f"celda desconocida: {cid}")
    total = 0.0
    for cid in celdas:
        r = correr_celda(cid, client_real=real, precio_in=args.precio_in, precio_out=args.precio_out,
                         cuota_usd=cuota, driver=driver)
        total += r["gasto_sesion_usd_cli"]
        if r["freno"] and r["freno"]["tipo"] == "contenedor":
            print("Corrida detenida por falla del contenedor.", flush=True)
            break
    print(f"Gasto de esta sesión: ${total:.4f} (tope {tope_usd}, cuota/celda {cuota}).", flush=True)
    driver.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
