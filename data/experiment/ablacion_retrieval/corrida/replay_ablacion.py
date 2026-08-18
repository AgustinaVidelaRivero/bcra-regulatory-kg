"""
replay_ablacion.py — Replay determinístico (estándar + FUERTE) de TODAS las
trazas de la ablación, por celda, y métrica de navegabilidad por ancla
(pre-registro §4). $0, sin API.

Métrica y replay IMPORTADOS sin editar:
  - `metrica.evaluar_por_anclas` (pipeline de sintéticas): visto / consultado /
    brecha por ancla, replay estándar contra `output_truncado`+`output_chars`;
  - `metrica_ev2.evaluar_caso` (5b02d22): lo anterior + replay FUERTE contra
    `steps_full` (igualdad exacta del output íntegro persistido).

Cómo se re-ejecuta cada step, según la celda (§4):
  - celdas v1 (C00, C10): `metrica_ev2.evaluar_caso(..., index=Neo4jIndex(modo))`
    tal cual — `Neo4jIndex` tiene la interfaz de `GraphIndex` (buscar_nodos /
    ver_nodo / ver_vecinos(id, direccion)); el modo (paridad|fulltext) es el
    del retriever de la celda; ver_nodo/ver_vecinos son idénticos en ambos.
    Para el CONTROL (C00) además se cruza con `GraphIndex` in-memory sobre
    KG-Refinado (paridad sobre trazas reales): mismo replay, mismos conteos.
  - celdas v2 (C01, C11): re-ejecutor v2-aware `agente_celda.reejecutar_step_celda`
    INYECTADO por atributo de módulo (`metrica._reejecutar_step` y el nombre
    importado en `metrica_ev2`) durante la evaluación, con `index=BackendCelda`
    (mismo despacho que usó el agente: `ver_vecinos(id, relacion, pagina,
    por_pagina)` → `ToolsV2.ver_vecinos_v2`); se restaura al terminar. Ningún
    archivo de metrica/ ni agente_v2/ se edita. Tests del adaptador:
    `tests_replay_v2.py`.

Cualquier divergencia de replay (estándar o fuerte) invalida la celda y se
reporta con detalle. Salidas (sin timestamps → byte-idénticas entre corridas):
  resultados/replay_<celda>.json    detalle por traza (métrica + clases + latencias)
  resultados/replay_verificacion.json   sha256 de cada archivo en la doble corrida
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

CORRIDA_DIR = Path(__file__).resolve().parent
if str(CORRIDA_DIR) not in sys.path:
    sys.path.insert(0, str(CORRIDA_DIR))

from comun_corrida import (GRAFO, ORDEN_CELDAS, RESULTADOS_DIR, TRAZAS_DIR,  # noqa: E402
                           cargar_celda, cargar_manifest_celdas, cargar_pares,
                           huerfanos_p6, indice_anclas_refinado, orden_resuelto,
                           rel_repo, sanitizar, sha_texto, verificar_kg_meta)
from agente_celda import BackendCelda, reejecutar_step_celda  # noqa: E402

import metrica  # noqa: E402  (sintéticas; sin editar)
import metrica_ev2  # noqa: E402  (ev2_corrida/code; sin editar)
from harness import GraphIndex  # noqa: E402
from comun_ev2 import cargar_runtime  # noqa: E402  (vista runtime v3 = KG-Refinado)


class _Inyeccion:
    """Context manager: inyecta el re-ejecutor v2-aware en metrica y metrica_ev2
    por atributo de módulo y lo restaura al salir (sin editar archivos)."""

    def __init__(self, fn):
        self.fn = fn

    def __enter__(self):
        self._orig = (metrica._reejecutar_step, metrica_ev2._reejecutar_step)
        metrica._reejecutar_step = self.fn
        metrica_ev2._reejecutar_step = self.fn
        return self

    def __exit__(self, *exc):
        metrica._reejecutar_step, metrica_ev2._reejecutar_step = self._orig
        return False


def evaluar_payload(payload: dict, anclas_gold: list[dict], ancla_index, backend: BackendCelda) -> dict:
    """Métrica + replay estándar + replay fuerte de UNA traza según su celda."""
    if backend.tools_version == "v1":
        return metrica_ev2.evaluar_caso(payload, anclas_gold, ancla_index, backend.index_busqueda)
    with _Inyeccion(reejecutar_step_celda):
        return metrica_ev2.evaluar_caso(payload, anclas_gold, ancla_index, backend)


def _resumen_ev(ev: dict) -> dict:
    return {"n_anclas": ev["n_anclas"], "n_vistas": ev["n_vistas"], "n_consultadas": ev["n_consultadas"],
            "n_brecha": ev["n_brecha"], "recall_vista": ev["recall_vista"],
            "recall_consultada": ev["recall_consultada"], "por_ancla": ev["por_ancla"]}


def _clases_traza(payload: dict) -> dict:
    tr, steps_full = payload["trace"], payload.get("steps_full", [])
    fj = tr.get("final_json") if isinstance(tr.get("final_json"), dict) else None
    abst = bool(tr.get("parse_ok")) and fj is not None and fj.get("respondible") is False
    por_tool = {}
    lat_tool = {}
    n_pag_gt1 = n_vv_relacion = 0
    for s in steps_full:
        por_tool[s["tool"]] = por_tool.get(s["tool"], 0) + 1
        if "latency_tool_s" in s:
            lat_tool.setdefault(s["tool"], []).append(s["latency_tool_s"])
        if s["tool"] == "ver_vecinos":
            args = s.get("input") or {}
            try:
                if int(args.get("pagina", 1)) > 1:
                    n_pag_gt1 += 1
            except (TypeError, ValueError):
                pass
            if args.get("relacion"):
                n_vv_relacion += 1
    return {
        "tool_calls_used": tr.get("tool_calls_used"), "hit_tool_limit": bool(tr.get("hit_tool_limit")),
        "parse_ok": bool(tr.get("parse_ok")), "error": tr.get("error"),
        "abstencion": abst, "final_stop_reason": tr.get("final_stop_reason"),
        "truncated_max_tokens": bool(tr.get("truncated_max_tokens")),
        "latency_s": tr.get("latency_s"), "tokens_in": tr.get("tokens_in"),
        "tokens_out": tr.get("tokens_out"), "cache_read": tr.get("cache_read"),
        "cache_write": tr.get("cache_write"), "cost_usd_harness": tr.get("cost_usd"),
        "costo_usd_cli": payload["meta"].get("costo_usd_cli"),
        "api_calls": len(tr.get("api_calls") or []),
        "llamadas_por_tool": por_tool, "latencias_por_tool_s": lat_tool,
        "n_ver_vecinos_pagina_gt1": n_pag_gt1, "n_ver_vecinos_con_relacion": n_vv_relacion,
    }


def _huerfanos_en_traza(ev: dict, nodos_huerfanos: list[str]) -> list[dict]:
    """visto/consultado de cada nodo gold huérfano de label (P6) en esta traza,
    leído del detalle por nodo de la métrica (dedup por nodo)."""
    estado = {}
    for _ancla, lista in ev.get("detalle_nodos", {}).items():
        for pn in lista:
            if pn["nodo"] in nodos_huerfanos and pn["nodo"] not in estado:
                estado[pn["nodo"]] = {"nodo": pn["nodo"], "visto": pn["visto"],
                                      "consultado": pn["consultado"],
                                      "consultado_via": pn.get("consultado_via")}
    return [estado[n] for n in nodos_huerfanos if n in estado]


def replay_celda(celda_id: str, *, driver, ancla_index, pares_por_id: dict, huerfanos: dict,
                 trazas_dir: Path | None = None, index_inmemory: GraphIndex | None = None,
                 casos_esperados: list[dict] | None = None) -> dict:
    manifest = cargar_manifest_celdas()
    celda = cargar_celda(celda_id, manifest)
    backend = BackendCelda(driver, celda, grafo=GRAFO)
    trazas_dir = trazas_dir or (TRAZAS_DIR / celda_id)
    esperados = [c["caso_id"] for c in (casos_esperados or [])]
    resultados, faltantes, apartadas = [], [], []
    archivos = sorted(p for p in trazas_dir.glob("*.json") if not p.name.startswith("resumen_"))
    for p in archivos:
        if ".freno_contenedor" in p.name:
            apartadas.append(p.name)
            continue
        with p.open(encoding="utf-8") as f:
            payload = json.load(f)
        m = payload["meta"]
        if m["celda_id"] != celda_id or m["celda_archivo_sha256"] != celda["archivo_sha256"]:
            raise RuntimeError(f"{p.name}: traza de otra celda o de otra versión de la celda")
        par = pares_por_id[m["sample_id"]]
        anclas = par["gold"]["anclas"]
        ev = evaluar_payload(payload, anclas, ancla_index, backend)
        r = {"caso_id": m["caso_id"], "sample_id": m["sample_id"], "variante": m["variante"],
             "estrato": m["estrato"], "sub_estrato": m.get("sub_estrato"), "pos_orden": m.get("pos_orden"),
             **_resumen_ev(ev),
             "anclas_ausentes_en_este_grafo": ev["anclas_ausentes_en_este_grafo"],
             "replay_ok": ev["replay_ok"], "replay_fuerte_ok": ev["replay_fuerte_ok"],
             "replay_fallas": ev["replay_fallas"], "replay_fuerte_fallas": ev["replay_fuerte_fallas"],
             "clases": _clases_traza(payload),
             "huerfanos_p6": _huerfanos_en_traza(ev, huerfanos.get(m["sample_id"], [])),
             "detalle_nodos": ev["detalle_nodos"]}
        if celda["es_control"] and index_inmemory is not None:
            ev_mem = metrica_ev2.evaluar_caso(payload, anclas, ancla_index, index_inmemory)
            r["cruce_inmemory"] = {
                "replay_ok": ev_mem["replay_ok"], "replay_fuerte_ok": ev_mem["replay_fuerte_ok"],
                "mismos_conteos": (ev_mem["n_vistas"], ev_mem["n_consultadas"], ev_mem["n_brecha"])
                                  == (ev["n_vistas"], ev["n_consultadas"], ev["n_brecha"]),
                "mismo_por_ancla": ev_mem["por_ancla"] == ev["por_ancla"],
            }
        resultados.append(r)
    presentes = {r["caso_id"] for r in resultados}
    faltantes = [c for c in esperados if c not in presentes]
    n = len(resultados)
    out = {
        "unidad": "U-A1.4", "celda_id": celda_id, "retriever": celda["retriever"], "tools": celda["tools"],
        "celda_archivo_sha256": celda["archivo_sha256"], "trazas_dir": rel_repo(trazas_dir),
        "reejecutor": ("metrica._reejecutar_step original con Neo4jIndex(modo=%s)" % backend.index_busqueda.modo
                       if celda["tools"] == "v1" else
                       "agente_celda.reejecutar_step_celda inyectado en metrica/metrica_ev2 (BackendCelda)"),
        "n_trazas": n, "n_esperadas": len(esperados) or None, "faltantes": faltantes,
        "apartadas_freno_contenedor": apartadas,
        "replay_ok_todos": all(r["replay_ok"] for r in resultados),
        "replay_fuerte_ok_todos": all(r["replay_fuerte_ok"] for r in resultados),
        "n_divergencias": sum(1 for r in resultados if not (r["replay_ok"] and r["replay_fuerte_ok"])),
        "cruce_inmemory_ok_todos": (all(r["cruce_inmemory"]["replay_ok"] and r["cruce_inmemory"]["replay_fuerte_ok"]
                                        and r["cruce_inmemory"]["mismos_conteos"] and r["cruce_inmemory"]["mismo_por_ancla"]
                                        for r in resultados) if (celda["es_control"] and index_inmemory is not None) else None),
        "resultados": resultados,
    }
    return out


def _canon(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=False)


def replay_todo(celdas: list[str] | None = None, *, driver=None, trazas_base: Path | None = None,
                out_dir: Path | None = None, doble: bool = True, verbose: bool = True) -> dict:
    """Replay de todas las celdas, DOBLE corrida byte-idéntica (in-process) y
    escritura de resultados/replay_<celda>.json + replay_verificacion.json."""
    if driver is None:
        from conexion import abrir_driver
        driver = abrir_driver()
    verificar_kg_meta(driver, GRAFO)
    celdas = celdas or ORDEN_CELDAS
    out_dir = out_dir or RESULTADOS_DIR
    out_dir.mkdir(parents=True, exist_ok=True)
    ancla_index = indice_anclas_refinado()
    pares = cargar_pares()
    pares_por_id = {p["sample_id"]: p for p in pares}
    huer = huerfanos_p6()
    esperados = orden_resuelto(pares)
    index_mem = GraphIndex(cargar_runtime("v3"))    # KG-Refinado in-memory (cruce del control)
    verificacion = {"generado": datetime.now().isoformat(timespec="seconds"), "celdas": {}}
    salidas = {}
    for cid in celdas:
        tdir = (trazas_base / cid) if trazas_base else (TRAZAS_DIR / cid)
        kw = dict(driver=driver, ancla_index=ancla_index, pares_por_id=pares_por_id, huerfanos=huer,
                  trazas_dir=tdir, index_inmemory=index_mem, casos_esperados=esperados)
        r1 = replay_celda(cid, **kw)
        s1 = _canon(r1)
        info = {"n_trazas": r1["n_trazas"], "replay_ok_todos": r1["replay_ok_todos"],
                "replay_fuerte_ok_todos": r1["replay_fuerte_ok_todos"],
                "cruce_inmemory_ok_todos": r1["cruce_inmemory_ok_todos"],
                "sha256_corrida_1": sha_texto(s1)}
        if doble:
            r2 = replay_celda(cid, **kw)
            s2 = _canon(r2)
            info["sha256_corrida_2"] = sha_texto(s2)
            info["doble_corrida_byte_identica"] = (s1 == s2)
        p = out_dir / f"replay_{cid}.json"
        p.write_text(s1, encoding="utf-8")
        info["archivo"] = rel_repo(p)
        info["sha256_archivo"] = sha_texto(p.read_text(encoding="utf-8"))
        verificacion["celdas"][cid] = info
        salidas[cid] = r1
        if verbose:
            print(f"  {cid}: {r1['n_trazas']} trazas | replay_ok={r1['replay_ok_todos']} "
                  f"fuerte_ok={r1['replay_fuerte_ok_todos']} cruce_inmemory={r1['cruce_inmemory_ok_todos']} "
                  f"| doble={info.get('doble_corrida_byte_identica')} | faltantes={len(r1['faltantes'])}",
                  flush=True)
            for r in r1["resultados"]:
                if not (r["replay_ok"] and r["replay_fuerte_ok"]):
                    print(f"    DIVERGENCIA {r['caso_id']}: {r['replay_fallas']} {r['replay_fuerte_fallas']}")
    (out_dir / "replay_verificacion.json").write_text(_canon(verificacion), encoding="utf-8")
    return {"verificacion": verificacion, "salidas": salidas}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--celda", default="all")
    ap.add_argument("--sin-doble", action="store_true", help="una sola corrida (depuración)")
    args = ap.parse_args()
    celdas = ORDEN_CELDAS if args.celda == "all" else [args.celda]
    from comun_ablacion import verificar_piezas
    print("piezas selladas:")
    verificar_piezas()
    replay_todo(celdas, doble=not args.sin_doble)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
