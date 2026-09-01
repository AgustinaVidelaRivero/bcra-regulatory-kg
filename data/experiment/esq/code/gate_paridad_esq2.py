"""
gate_paridad_esq2.py — FASE (a) de U-ESQ-2: gate de paridad por caché ($0),
precondición del pre-registro §2 (2240c9c).

Qué verifica: que el camino flag-off de ESTA unidad (prompt_e1.build_request_kwargs
con canal_abierto=False, el mismo call site que usará el runner de la corrida
grande) produce requests BYTE-IDÉNTICOS a los de la corrida de producción del
corpus (runner_corpus.fase_e1). Criterio sellado:

  - 10 unidades del conjunto de desarrollo (de los 5 TOs del subset), corridas
    por el camino de la unidad CONTRA EL NAMESPACE DE PRODUCCIÓN:
    10/10 cache hits locales, 0 misses, USD 0.
  - La validación recomputada por el validador vigente (validador_e1, flag
    apagado) sobre esas 10 debe coincidir con la persistida en producción.
  - Cruce adicional db==jsonl sobre las 10: el tool_input del crudo cacheado
    coincide con el tool_input_crudo persistido en el jsonl de producción.

USD 0 garantizado por construcción: este script NO construye ningún cliente
de API — computa la key de caché del request (llm_cache.compute_key sobre el
request canónico + namespace de producción) y la busca en la db de producción
abierta ESTRICTAMENTE READ-ONLY (URI mode=ro: ninguna escritura es posible,
ni siquiera access_log). Un miss NO dispara ninguna llamada: dispara FRENO.

Regla de selección de las 10 unidades (declarada; el pre-registro no fija
cuáles): 2 por TO del subset (cap, cla, ext, pro, ric — orden comun_e1.TOS),
las primeras 2 en el orden del archivo de E0 (E0_SALIDA_ENM01, el de la
corrida de producción) cuyo registro de producción existe con error=None
(una unidad con error no tiene validación persistida que comparar).

Salida: cobertura/gate_paridad_esq2.json + [PASS]/FRENO por stdout.
Exit code: 0 si 10/10; 3 si FRENO.

Uso:  .venv/bin/python3 -B data/experiment/esq/code/gate_paridad_esq2.py
"""

from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_cobertura_esq2 as cc      # noqa: E402  (agrega e1_extractor al path)
import comun_e1                        # noqa: E402
import prompt_e1                       # noqa: E402
import validador_e1                    # noqa: E402
import llm_cache as lc                 # noqa: E402

DB_PRODUCCION = cc.E1_DIR / "cache" / "e1_extraccion.db"
SALIDA_PRODUCCION = (cc.EXP_DIR / "reextraccion_v2" / "corpus_v2" / "salida")

N_POR_TO = 2
TOS_DEV = comun_e1.TOS   # ("cap", "cla", "ext", "pro", "ric")


def seleccionar_unidades_gate() -> list[dict]:
    """Las 10 unidades del gate según la regla declarada en la docstring."""
    seleccion: list[dict] = []
    for to in TOS_DEV:
        chunks = comun_e1.cargar_chunks((to,), e0_dir=comun_e1.E0_SALIDA_ENM01)
        prod = cc.cargar_jsonl_last_wins(
            SALIDA_PRODUCCION / to / "extracciones_e1.jsonl")
        elegidos = 0
        for c in chunks:
            reg = prod.get(c["id"])
            if reg is not None and reg.get("error") is None:
                seleccion.append({"to": to, "chunk": c, "registro_prod": reg})
                elegidos += 1
                if elegidos == N_POR_TO:
                    break
        if elegidos < N_POR_TO:
            raise RuntimeError(f"gate: {to} no tiene {N_POR_TO} unidades sin "
                               f"error en producción — revisar")
    return seleccion


def main() -> int:
    ns_prod = cc.namespace_produccion()
    print(f"[gate] namespace de producción: {ns_prod}")
    print(f"[gate] db de producción (READ-ONLY): {DB_PRODUCCION}")
    print(f"[gate] prefijo cerrado vigente: {prompt_e1.prefijo_hash(False)} "
          f"(candado esperado {cc.PREFIJO_HASH_CERRADO_ESPERADO})")
    if prompt_e1.prefijo_hash(False) != cc.PREFIJO_HASH_CERRADO_ESPERADO:
        print("FRENO: el hash del prefijo cerrado no coincide con el candado "
              "— prompt_e1 cambió respecto de producción; nada se corre")
        return 3

    seleccion = seleccionar_unidades_gate()
    conn = cc.conectar_db_readonly(DB_PRODUCCION)

    resultados = []
    hits = misses = val_ok = val_dif = cruce_ok = cruce_dif = 0
    for s in seleccion:
        c = s["chunk"]
        kwargs = prompt_e1.build_request_kwargs(c, model=cc.MODEL_E1)
        canonical = lc.canonical_request(kwargs)
        key = lc.compute_key(ns_prod, canonical)
        row = conn.execute("SELECT * FROM cache WHERE key = ?", (key,)).fetchone()
        r = {"to": s["to"], "chunk_id": c["id"], "key": key,
             "hit": row is not None}
        if row is None:
            misses += 1
            r["detalle"] = "MISS — el request de la unidad no está en la caché de producción"
        else:
            hits += 1
            r["model_db"] = row["model"]
            # cruce db == jsonl (tool_input)
            ti_db = cc.tool_input_de_raw(row["raw_json"])
            ti_jsonl = s["registro_prod"].get("tool_input_crudo")
            r["cruce_db_jsonl_tool_input"] = (ti_db == ti_jsonl)
            cruce_ok += r["cruce_db_jsonl_tool_input"]
            cruce_dif += not r["cruce_db_jsonl_tool_input"]
            # validación recomputada (validador vigente, flag apagado) vs persistida
            val_re = validador_e1.validar_salida(ti_jsonl, c).as_dict()
            val_prod = s["registro_prod"].get("validacion")
            r["validacion_coincide"] = (val_re == val_prod)
            val_ok += r["validacion_coincide"]
            val_dif += not r["validacion_coincide"]
        resultados.append(r)
        estado = "HIT " if r["hit"] else "MISS"
        extra = ""
        if r["hit"]:
            extra = (f" val=={'OK' if r['validacion_coincide'] else 'DIF'}"
                     f" db==jsonl {'OK' if r['cruce_db_jsonl_tool_input'] else 'DIF'}")
        print(f"  [{estado}] {c['id']:<28s}{extra}")
    conn.close()

    pasa = (hits == 10 and misses == 0 and val_ok == 10 and cruce_ok == 10)
    doc = {
        "generado": datetime.now().isoformat(timespec="seconds"),
        "namespace_produccion": ns_prod,
        "db_produccion": str(DB_PRODUCCION.relative_to(cc.REPO_DIR)),
        "modo_apertura_db": "sqlite URI mode=ro (solo lectura estricta)",
        "regla_seleccion": ("2 por TO del subset (orden comun_e1.TOS), las "
                            "primeras 2 en orden de archivo E0_SALIDA_ENM01 "
                            "con registro de producción sin error"),
        "prefijo_hash_cerrado": prompt_e1.prefijo_hash(False),
        "model_request": cc.MODEL_E1,
        "hits": hits, "misses": misses, "usd": 0.0,
        "validacion_coincide": val_ok, "validacion_difiere": val_dif,
        "cruce_db_jsonl_ok": cruce_ok, "cruce_db_jsonl_dif": cruce_dif,
        "pasa": pasa,
        "criterio": ("pre-registro §2: 10/10 hits, 0 misses, USD 0, validación "
                     "recomputada == persistida (más cruce db==jsonl declarado)"),
        "unidades": resultados,
    }
    cc.COBERTURA_DIR.mkdir(parents=True, exist_ok=True)
    out = cc.COBERTURA_DIR / "gate_paridad_esq2.json"
    out.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"\nRESULTADO gate: hits={hits}/10 misses={misses} USD 0 "
          f"| validacion=={val_ok}/10 | cruce db==jsonl {cruce_ok}/10")
    if pasa:
        print("[PASS] gate de paridad por caché: el camino flag-off de la "
              "unidad ES el de producción")
        return 0
    print("FRENO: el gate NO pasó — la corrida grande no puede arrancar "
          "(pre-registro §2); se reporta sin arreglar nada")
    return 3


if __name__ == "__main__":
    raise SystemExit(main())
