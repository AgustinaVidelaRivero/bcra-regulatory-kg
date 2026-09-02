"""
reporte_esq3b.py — cierre del FRENO FINAL de U-ESQ-3b ($0, sin API).

Reúne, todo reproducible por este único comando:
  (i)   COSTO REAL contra el tope, calculado por DOS vías independientes que
        tienen que coincidir: (a) el log de usage D3
        (`logs/cache_usage.jsonl`, filtrado por el component propio de la
        unidad) y (b) las filas de la db propia bajo el namespace propio. Si
        divergen, el reporte lo dice: son dos registros distintos del mismo
        hecho y una discrepancia es un hallazgo, no un detalle.
  (ii)  conteos por brazo, modelo RESUELTO por llamada, cruce db==jsonl;
  (iii) sellos sha256 de la db, del jsonl de extracciones y del worksheet
        pareado;
  (iv)  ANOMALÍAS declaradas: unidades con error, cortes por `max_tokens`,
        unidades sin fila en la db, y las unidades del brazo de regresión que
        provienen de fichas contaminadas del desvío (a) de ESQ-2 — marca que
        va a la TABLA DE RESULTADOS y al reporte, NUNCA a las fichas pareadas
        ni a la selección sellada (nota de mesa del freno de la fase d).

No adjudica nada: los veredictos por retoque son de la autora.

Uso:  .venv/bin/python3 -B data/experiment/esq/code/reporte_esq3b.py
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_esq3b as cc       # noqa: E402
import prompt_esq3b as pr      # noqa: E402
import runner_esq3b as run     # noqa: E402

# Nota de mesa (freno de la fase d): unidades del brazo de REGRESIÓN que salen
# de fichas contaminadas del desvío (a) de ESQ-2 (lectura de la mesa a la vista
# al marcar). Se declaran en la tabla de resultados y en el reporte; NO se
# marcan en las fichas pareadas ni en la selección sellada, que no cambia de
# sha. La marca de la autora manda.
CONTAMINADAS_DESVIO_A = ("lavdin::1.1::intro", "ayccef::3.4.1")


def sha256_de(path: Path) -> str | None:
    if not path.exists():
        return None
    h = hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def costo_desde_log_usage() -> dict:
    """Vía (a): el log D3. Una línea JSON por response REAL de la API con el
    component propio de la unidad — el registro que la decisión 3 de
    `docs/decisiones_caching_extraccion.md` exige justamente para poder
    auditar el costo sin depender de la caché."""
    agg = {"n": 0, "input_tokens": 0, "output_tokens": 0,
           "cache_write_tokens": 0, "cache_read_tokens": 0}
    if not cc.CACHE_USAGE_LOG.exists():
        return {"disponible": False, **agg}
    with cc.CACHE_USAGE_LOG.open(encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue
            r = json.loads(linea)
            if r.get("component") != cc.ClienteEsq3b.COMPONENT:
                continue
            agg["n"] += 1
            agg["input_tokens"] += r.get("input_tokens") or 0
            agg["output_tokens"] += r.get("output_tokens") or 0
            agg["cache_write_tokens"] += r.get("cache_creation_input_tokens") or 0
            agg["cache_read_tokens"] += r.get("cache_read_input_tokens") or 0
    return {"disponible": True, **agg,
            "costo_usd": round(cc.costo_usd_desde_usage(agg), 4)}


def main() -> int:
    seleccion = json.loads(
        (cc.ORDEN_DIR / "seleccion_brazos_esq3b.json").read_text(encoding="utf-8"))
    resumen = run.cierre()          # recomputa desde lo persistido, sin API
    regs = cc.cargar_jsonl_last_wins(run.SALIDA_JSONL)
    log = costo_desde_log_usage()

    brazo_por_cid = {}
    for brazo in ("objetivo", "regresion"):
        for u in seleccion[brazo]["unidades"]:
            brazo_por_cid[u["chunk_id"]] = brazo

    anomalias = {
        "unidades_con_error": [
            {"chunk_id": cid, "brazo": brazo_por_cid.get(cid),
             "error": r.get("error"), "stop_reason": r.get("stop_reason")}
            for cid, r in sorted(regs.items()) if r.get("error")],
        "cortes_max_tokens": [
            cid for cid, r in sorted(regs.items())
            if r.get("stop_reason") == "max_tokens"],
        "sin_fila_en_db": resumen["cruce_db_jsonl"]["sin_fila_db"],
        "cruce_db_jsonl_divergente": resumen["cruce_db_jsonl"]["dif"],
        "regresion_de_fichas_contaminadas_desvio_a": [
            {"chunk_id": cid, "brazo": brazo_por_cid.get(cid),
             "nota": ("ficha contaminada del desvío (a) de ESQ-2; se declara en "
                      "la tabla de resultados y en el reporte, NO en las fichas "
                      "pareadas ni en la selección sellada")}
            for cid in CONTAMINADAS_DESVIO_A if cid in brazo_por_cid],
    }

    # tipos y predicados NUEVOS efectivamente emitidos (dato descriptivo del
    # ejecutor; NO es adjudicación de ninguna predicción)
    tipos_nuevos = {t: 0 for t in ("Potestad", "Condicion", "Definicion")}
    preds_nuevos = {p: 0 for p in ("condicion_de", "exceptua_operacion")}
    r9_nuevos = {v: 0 for v in ("reporte_al_supervisor", "requisito_de_estructura")}
    unidades_con_tipo_nuevo = {"objetivo": set(), "regresion": set()}
    for cid, r in regs.items():
        ch = r.get("chequeo_esquema_retocado") or {}
        for t in tipos_nuevos:
            n = (ch.get("tipos_emitidos") or {}).get(t, 0)
            tipos_nuevos[t] += n
            if n:
                unidades_con_tipo_nuevo[brazo_por_cid.get(cid, "?")].add(cid)
        for p in preds_nuevos:
            preds_nuevos[p] += (ch.get("predicados_emitidos") or {}).get(p, 0)
        for v in r9_nuevos:
            r9_nuevos[v] += (ch.get("obligacion_tipo_emitido") or {}).get(v, 0)

    ws_pareado = cc.FICHAS_DIR / "worksheet_pareado_esq3b.json"
    reporte = {
        "unidad": "U-ESQ-3b",
        "fase": "(d) corrida + (f) fichas — FRENO FINAL",
        "prefijo_retocado_hash": pr.PREFIJO_HASH_RETOCADO,
        "prefijo_retocado_sha256_texto": pr.PREFIJO_SHA256_RETOCADO,
        "namespace": resumen["namespace"],
        "costo": {
            "via_a_log_usage_d3": log,
            "via_b_db_namespace_propio": {
                **resumen["filas_db_namespace_propio"],
                "costo_usd": resumen["gasto_real_usd_desde_db"]},
            "coinciden": (log.get("disponible")
                          and log.get("costo_usd")
                          == resumen["gasto_real_usd_desde_db"]),
            "tope_usd": cc.TOPE_USD,
            "dentro_del_tope": (resumen["gasto_real_usd_desde_db"]
                                <= cc.TOPE_USD),
            "formula": resumen["formula_costo"],
        },
        "conteos_por_brazo": resumen["persistidas_sin_error_por_brazo"],
        "seleccionadas": resumen["seleccionadas"],
        "modelo_resuelto_por_llamada": resumen["modelo_resuelto_por_llamada"],
        "cruce_db_jsonl": resumen["cruce_db_jsonl"],
        "sellos_sha256": {
            "db_esq_3b": resumen["db_sha256"],
            "extracciones_pareado_esq3b_jsonl": sha256_de(run.SALIDA_JSONL),
            "worksheet_pareado_esq3b_json": sha256_de(ws_pareado),
            "seleccion_brazos_esq3b_json": sha256_de(
                cc.ORDEN_DIR / "seleccion_brazos_esq3b.json"),
        },
        "produccion_y_cobertura_intactas_por_sha":
            resumen["produccion_y_cobertura_intactas_por_sha"],
        "sellos_divergentes": resumen["sellos_divergentes"],
        "anomalias": anomalias,
        "vocabulario_nuevo_emitido": {
            "nota": ("conteo DESCRIPTIVO del ejecutor sobre el chequeo de "
                     "esquema retocado; NO adjudica ninguna predicción — los "
                     "veredictos por retoque son de la autora, sobre las "
                     "fichas pareadas"),
            "tipos": tipos_nuevos,
            "predicados": preds_nuevos,
            "obligacion_tipo_r9": r9_nuevos,
            "unidades_con_algun_tipo_nuevo": {
                k: len(v) for k, v in unidades_con_tipo_nuevo.items()},
        },
    }
    destino = cc.ESQ3B_DIR / "reporte_freno_final_esq3b.json"
    destino.write_text(json.dumps(reporte, ensure_ascii=False, indent=1),
                       encoding="utf-8")
    print(json.dumps(reporte, ensure_ascii=False, indent=1))
    print(f"\npersistido: {destino.relative_to(cc.REPO_DIR)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
