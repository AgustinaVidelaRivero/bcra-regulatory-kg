"""
runner_r1.py — Corrida del agente N=1 sobre KG-Reextraído-r1: las 40 preguntas
de fidelidad de EV2 (U-B1.8; pre-registro ev2_r1/preregistro_ev2_r1.md §4).

Reutiliza sin editar `runner_ev2.correr_grafo` (corrida base, bb89a8e): mismo
FullCaptureAgent (harness congelado, modelo hardcodeado en harness.MODEL),
misma persistencia por caso (traza + steps_full + raw_turns_agent + metadata).
r1 entra por el registro en memoria de comun_r1 (adaptador de provenance
idéntico al de la vista v2 de la base); el kg.json se verifica por sha256
antes de correr (4/4 grafos).

Orden: semilla `orden-ev2-r1` (comun_r1.casos_fidelidad_r1), persistido en
orden/orden_agente_r1.json. Label `ev2_r1_base`, db propia
cache/ev2_r1_base.db (gitignorada). Retomable: los casos con traza persistida
se saltean (never-pay-twice, además, por la db).

GATING DE GASTO: el modo real exige --autorizado-fase-b y --tope <USD>
(autorización explícita de la sesión). Freno por proyección de correr_grafo
(protocolo §5). El selftest offline vive en selftest_r1.py.

Uso (fase B, solo con autorización explícita):
  .venv/bin/python -B data/experiment/ev2_r1/code/runner_r1.py \
      --autorizado-fase-b --tope <USD>
  --solo-resumen: recomputa el índice de trazas sin llamar a la API.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_r1 as cr                      # noqa: E402  (registra r1 al importarse)
import runner_ev2 as rv                    # noqa: E402  (runner base, sin editar)


def indice_trazas(casos: list[dict], outdir: Path) -> dict:
    """Estado de las 40 corridas previstas (patrón runner_enc.indice_trazas)."""
    filas, faltan = [], []
    for c in casos:
        f = outdir / f"{rv._sanitizar(c['caso_id'])}.json"
        if not f.exists():
            faltan.append(c["caso_id"])
            continue
        t = json.loads(f.read_text(encoding="utf-8"))
        tr, m = t["trace"], t["meta"]
        filas.append({"caso_id": c["caso_id"], "parse_ok": bool(tr.get("parse_ok")),
                      "error": tr.get("error"),
                      "respuesta_ok": bool(tr.get("parse_ok"))
                      and isinstance((tr.get("final_json") or {}).get("respuesta"), str)
                      and bool((tr.get("final_json") or {}).get("respuesta", "").strip()),
                      "tools": tr.get("tool_calls_used"),
                      "hit_tool_limit": tr.get("hit_tool_limit"),
                      "cost_usd_harness": tr.get("cost_usd"),
                      "cache_turnos": m.get("cache_turnos"), "model": m.get("model"),
                      "kg_sha256": m.get("kg_sha256"),
                      "graph_fingerprint": m.get("graph_fingerprint")})
    incompletas = [x["caso_id"] for x in filas if not x["respuesta_ok"]]
    return {"n_previstas": len(casos), "n_persistidas": len(filas),
            "n_faltantes": len(faltan), "faltantes": faltan,
            "n_incompletas": len(incompletas), "incompletas": incompletas,
            "modelos": sorted({x["model"] for x in filas}),
            "kg_sha256": sorted({x["kg_sha256"] for x in filas}),
            "hits_turnos_trazas": sum((x["cache_turnos"] or {}).get("hits", 0) for x in filas),
            "hit_tool_limit": sum(bool(x["hit_tool_limit"]) for x in filas),
            "costo_harness_usd": round(sum(x["cost_usd_harness"] or 0 for x in filas), 4),
            "errores": dict(Counter(str(x["error"]) for x in filas if x["error"])),
            "filas": filas}


def main() -> int:
    ap = argparse.ArgumentParser(description="Agente N=1 sobre r1 (fase B, requiere autorización)")
    ap.add_argument("--autorizado-fase-b", action="store_true")
    ap.add_argument("--tope", type=float, default=None, help="tope USD de ESTA etapa")
    ap.add_argument("--solo-resumen", action="store_true")
    args = ap.parse_args()

    sellos = cr.verificar_sellos(verbose=True)
    casos = cr.casos_fidelidad_r1()
    cr.persistir_orden(casos)
    outdir = cr.TRAZAS_DIR / cr.R1["label"]

    if args.solo_resumen:
        idx = indice_trazas(casos, outdir)
        cr.UNIDAD_DIR.joinpath("reporte").mkdir(parents=True, exist_ok=True)
        (cr.UNIDAD_DIR / "reporte" / "indice_trazas_agente_r1.json").write_text(
            json.dumps(idx, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps({k: v for k, v in idx.items() if k != "filas"},
                         ensure_ascii=False, indent=2))
        return 0

    if not args.autorizado_fase_b or args.tope is None:
        print("ABORTADO: la fase B exige --autorizado-fase-b y --tope <USD>. Nada se llamó.")
        return 2

    cr.escribir_sellos("sellos_inicio_faseB_agente.txt")
    outdir.mkdir(parents=True, exist_ok=True)
    pend = [c for c in casos
            if not (outdir / f"{rv._sanitizar(c['caso_id'])}.json").exists()]
    print(f"== U-B1.8 agente r1: {len(casos)} casos, {len(casos) - len(pend)} ya "
          f"persistidos, {len(pend)} pendientes | tope USD {args.tope} ==", flush=True)
    estado = {"gastado": 0.0, "corridos": 0, "total": len(pend), "tope_usd": args.tope}
    resumen = None
    if pend:
        real = rv._real_client()
        resumen = rv.correr_grafo(cr.R1_KEY, client_real=real,
                                  db_path=cr.CACHE_DIR / f"{cr.R1['label']}.db",
                                  label=cr.R1["label"], casos=pend, outdir=outdir,
                                  estado_gasto=estado)
    idx = indice_trazas(casos, outdir)
    cr.UNIDAD_DIR.joinpath("reporte").mkdir(parents=True, exist_ok=True)
    (cr.UNIDAD_DIR / "reporte" / "indice_trazas_agente_r1.json").write_text(
        json.dumps(idx, ensure_ascii=False, indent=2), encoding="utf-8")
    (cr.UNIDAD_DIR / "reporte" / "resumen_agente_r1.json").write_text(json.dumps(
        {"ts": datetime.now().isoformat(timespec="seconds"), "tope_usd": args.tope,
         "estado_gasto": estado, "resumen_correr_grafo": resumen,
         "indice": {k: v for k, v in idx.items() if k != "filas"}},
        ensure_ascii=False, indent=2), encoding="utf-8")
    cr.escribir_sellos("sellos_fin_faseB_agente.txt")
    if cr.verificar_sellos() != sellos:
        raise RuntimeError("sellos cambiaron durante la corrida")
    frenado = estado["corridos"] < len(pend)
    print(f"persistidas {idx['n_persistidas']}/{idx['n_previstas']} | incompletas "
          f"{idx['n_incompletas']} | gasto ${estado['gastado']:.4f}"
          + (" | FRENADO POR PROYECCIÓN" if frenado else ""), flush=True)
    return 1 if frenado else 0


if __name__ == "__main__":
    raise SystemExit(main())
