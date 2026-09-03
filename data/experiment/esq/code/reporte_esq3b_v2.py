"""
reporte_esq3b_v2.py — FRENO FINAL de U-ESQ-3b-v2 ($0, sin API): computa el
reporte del ejecutor desde lo persistido.

Contenido (mandato de la vuelta):
  - costo real por DOS vías independientes: (a) log de usage D3 (component
    `esq3b_v2_pareado_e1` en logs/cache_usage.jsonl) y (b) filas de la db
    propia bajo el namespace de la vuelta — ambas con la fórmula D2; se
    verifica que coinciden;
  - conteos por brazo, modelo resuelto por llamada, cruce db==jsonl;
  - sellos sha256 (db, jsonl, worksheet pareado, selección);
  - anomalías declaradas (errores, cortes por max_tokens, extracciones
    vacías) — las extracciones vacías como CONTEO por brazo, sin identidad;
  - agregados DESCRIPTIVOS del vocabulario emitido SIN nombrar qué unidades
    los produjeron (lección del desvío (b) de la vuelta 1: nombrar unidades
    siembra la lectura). NADA se adjudica: los veredictos de P1–P14 son de
    la autora sobre las fichas y de la mesa por recomputo posterior.

Salida: esq3b_v2/reporte_freno_final_esq3b_v2.json
Uso:  .venv/bin/python3 -B data/experiment/esq/code/reporte_esq3b_v2.py
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_esq3b_v2 as cc      # noqa: E402
import prompt_esq3b_v2 as pr     # noqa: E402

JSONL = cc.EXTRACCIONES_DIR / "pareado_esq3b_v2.jsonl"
WORKSHEET = cc.FICHAS_DIR / "worksheet_pareado_esq3b_v2.json"
SELECCION = cc.ORDEN_DIR / "seleccion_brazos_esq3b_v2.json"
SALIDA = cc.ESQ3B_V2_DIR / "reporte_freno_final_esq3b_v2.json"


def sha256_de(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def costo_via_log() -> dict:
    """Vía (a): las líneas D3 del componente propio en logs/cache_usage.jsonl
    (una línea por response REAL de la API)."""
    if not cc.CACHE_USAGE_LOG.exists():
        return {"disponible": False}
    agg = {"n": 0, "input_tokens": 0, "output_tokens": 0,
           "cache_write_tokens": 0, "cache_read_tokens": 0}
    with cc.CACHE_USAGE_LOG.open(encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue
            r = json.loads(linea)
            if r.get("component") != "esq3b_v2_pareado_e1":
                continue
            agg["n"] += 1
            agg["input_tokens"] += r.get("input_tokens") or 0
            agg["output_tokens"] += r.get("output_tokens") or 0
            agg["cache_write_tokens"] += r.get("cache_creation_input_tokens") or 0
            agg["cache_read_tokens"] += r.get("cache_read_input_tokens") or 0
    return {"disponible": True, **agg,
            "costo_usd": round(cc.costo_usd_desde_usage(agg), 4)}


def costo_via_db() -> dict:
    """Vía (b): filas de la db propia bajo el namespace de la vuelta."""
    conn = cc.conectar_db_readonly(cc.DB_V2)
    filas = conn.execute(
        "SELECT COUNT(*), COALESCE(SUM(input_tokens),0), "
        "COALESCE(SUM(output_tokens),0), COALESCE(SUM(cache_write_tokens),0), "
        "COALESCE(SUM(cache_read_tokens),0) FROM cache WHERE namespace = ?",
        (cc.namespace_v2(),)).fetchone()
    conn.close()
    agg = {"n": filas[0], "input_tokens": filas[1], "output_tokens": filas[2],
           "cache_write_tokens": filas[3], "cache_read_tokens": filas[4]}
    return {**agg, "costo_usd": round(cc.costo_usd_desde_usage(agg), 4)}


def main() -> int:
    seleccion = json.loads(SELECCION.read_text(encoding="utf-8"))
    brazo_de = {u["chunk_id"]: "objetivo"
                for u in seleccion["objetivo"]["unidades"]}
    brazo_de.update({u["chunk_id"]: "regresion_fresca"
                     for u in seleccion["regresion_fresca"]["unidades"]})
    regs = cc.cargar_jsonl_last_wins(JSONL)
    resumen_corrida = json.loads(
        (cc.ESQ3B_V2_DIR / "resumen_esq3b_v2.json").read_text(encoding="utf-8"))

    via_a = costo_via_log()
    via_b = costo_via_db()
    coinciden = (via_a.get("disponible")
                 and all(via_a[k] == via_b[k] for k in
                         ("n", "input_tokens", "output_tokens",
                          "cache_write_tokens", "cache_read_tokens")))

    # --- anomalías (sin identidad para lo descriptivo) ---
    errores = [{"chunk_id": cid, "error": r["error"],
                "stop_reason": r.get("stop_reason")}
               for cid, r in regs.items() if r.get("error")]
    max_tokens = [cid for cid, r in regs.items()
                  if r.get("stop_reason") == "max_tokens"]
    vacias_por_brazo: dict[str, int] = {"objetivo": 0, "regresion_fresca": 0}
    for cid, r in regs.items():
        if r.get("error"):
            continue
        ents = (r.get("tool_input_crudo") or {}).get("entities") or []
        if sum(1 for e in ents if isinstance(e, dict)
               and e.get("type") != "TextoOrdenado") == 0:
            vacias_por_brazo[brazo_de[cid]] += 1

    # --- agregados descriptivos SIN identidad de unidades ---
    tipos = {"Potestad": 0, "Condicion": 0, "Definicion": 0}
    condicion_de = 0
    oblig_tipo = {"reporte_al_supervisor": 0, "requisito_de_estructura": 0}
    re_por_brazo = {"objetivo": 0, "regresion_fresca": 0}
    unidades_con_tipo_nuevo = {"objetivo": 0, "regresion_fresca": 0}
    for cid, r in regs.items():
        if r.get("error"):
            continue
        ti = r.get("tool_input_crudo") or {}
        ents = [e for e in (ti.get("entities") or []) if isinstance(e, dict)]
        rels = [x for x in (ti.get("relations") or []) if isinstance(x, dict)]
        con_nuevo = False
        for e in ents:
            if e.get("type") in tipos:
                tipos[e.get("type")] += 1
                con_nuevo = True
            if e.get("type") == "Obligacion":
                t = (e.get("properties") or {}).get("tipo")
                if t in oblig_tipo:
                    oblig_tipo[t] += 1
                    if t == "requisito_de_estructura":
                        re_por_brazo[brazo_de[cid]] += 1
        for x in rels:
            if x.get("predicate") == "condicion_de":
                condicion_de += 1
        if con_nuevo:
            unidades_con_tipo_nuevo[brazo_de[cid]] += 1

    worksheet = json.loads(WORKSHEET.read_text(encoding="utf-8"))
    n_fichas = len(worksheet["fichas"])
    marcas_null = all(
        all(f["preguntas"][q]["marca"] is None
            for q in ("q1_cambio", "q2_fidelidad", "q3_migracion"))
        and all(e["marca"] is None
                for e in f["preguntas"]["q4_requisito_estructura"]["emisiones"])
        for f in worksheet["fichas"])
    q4_entradas = sum(
        len(f["preguntas"]["q4_requisito_estructura"]["emisiones"])
        for f in worksheet["fichas"])

    reporte = {
        "unidad": "U-ESQ-3b-v2",
        "fase": "(e) corrida + (f) fichas — FRENO FINAL",
        "prefijo_v2_hash": pr.PREFIJO_HASH_V2,
        "prefijo_v2_sha256_texto": pr.PREFIJO_SHA256_V2,
        "namespace": cc.namespace_v2(),
        "costo": {
            "via_a_log_usage_d3": via_a,
            "via_b_db_namespace_propio": via_b,
            "coinciden": bool(coinciden),
            "tope_usd": cc.TOPE_USD,
            "dentro_del_tope": via_b["costo_usd"] <= cc.TOPE_USD,
            "checkpoint_0_30_del_mandato": via_b["costo_usd"] <= 0.30,
            "formula": ("D2: in×1,00 + out×5,00 + cw×1,25 + cr×0,10 "
                        "(USD/MTok), decisiones_caching_extraccion.md:32-42; "
                        "tarifas runner_corpus.py:76-78"),
        },
        "conteos_por_brazo": resumen_corrida["persistidas_sin_error_por_brazo"],
        "seleccionadas": resumen_corrida["seleccionadas"],
        "modelo_resuelto_por_llamada": resumen_corrida["modelo_resuelto_por_llamada"],
        "cruce_db_jsonl": resumen_corrida["cruce_db_jsonl"],
        "sellos_sha256": {
            "db_esq_3b_v2": sha256_de(cc.DB_V2),
            "extracciones_pareado_esq3b_v2_jsonl": sha256_de(JSONL),
            "worksheet_pareado_esq3b_v2_json": sha256_de(WORKSHEET),
            "seleccion_brazos_esq3b_v2_json": sha256_de(SELECCION),
        },
        "produccion_y_cobertura_intactas_por_sha":
            resumen_corrida["produccion_y_cobertura_intactas_por_sha"],
        "insumos_v1_intactos_por_sha":
            resumen_corrida["insumos_v1_intactos_por_sha"],
        "anomalias": {
            "unidades_con_error": errores,
            "cortes_max_tokens": max_tokens,
            "extracciones_vacias_por_brazo_sin_identidad": vacias_por_brazo,
            "sin_fila_en_db": resumen_corrida["cruce_db_jsonl"]["sin_fila_db"],
            "cruce_db_jsonl_divergente": resumen_corrida["cruce_db_jsonl"]["dif"],
        },
        "fichas": {
            "n": n_fichas,
            "todas_las_marcas_null": marcas_null,
            "entradas_q4_pre_generadas": q4_entradas,
            "worksheet": str(WORKSHEET.relative_to(cc.REPO_DIR)),
            "instrumento": "leer_fichas_esq3b_v2.py (bug de pegado arreglado)",
        },
        "vocabulario_emitido_descriptivo_sin_identidad": {
            "nota": ("conteo DESCRIPTIVO del ejecutor; SIN identidad de "
                     "unidades (regla del mandato — lección del desvío (b) "
                     "de la vuelta 1: nombrar unidades siembra la lectura). "
                     "NO adjudica ninguna predicción: los veredictos de "
                     "P1–P14 son de la autora sobre las fichas cegadas y de "
                     "la mesa por recomputo mecánico posterior."),
            "tipos": tipos,
            "predicado_condicion_de": condicion_de,
            "obligacion_tipo": oblig_tipo,
            "emisiones_requisito_de_estructura_por_brazo": re_por_brazo,
            "unidades_con_algun_tipo_nuevo_por_brazo": unidades_con_tipo_nuevo,
        },
    }
    SALIDA.write_text(json.dumps(reporte, ensure_ascii=False, indent=1),
                      encoding="utf-8")
    print(json.dumps(reporte, ensure_ascii=False, indent=1))
    print(f"\npersistido: {SALIDA.relative_to(cc.REPO_DIR)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
