"""
correr_calibracion.py — Lanza la pasada de calibración autorizada (25 casos ×
N=3) con FRENO POR PROYECCIÓN de tope de gasto, contabilizando desde las dbs.

Precios y tope llegan por CLI (nunca hardcodeados). Antes de cada llamada se
proyecta: gasto_real_hasta_ahora + (llamadas_restantes × costo_promedio_por_
llamada_observado); si la proyección supera el tope, se frena ANTES de llamar
y se reporta. El gasto real sale de las tablas `cache` de las dbs de las tres
repeticiones (tokens por fila × precios), no de contadores en memoria.

Uso:
  .venv/bin/python data/experiment/ev2_juez/correr_calibracion.py \
      --criterios data/experiment/exploracion/u6_fidelidad/criterios_u6.json \
      --precio-in 3.00 --precio-out 15.00 --tope 1.50
"""

from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path

from driver_calibracion import (JUEZ_DIR, RUN_LABEL_BASE, _ya_juzgados, agregar,
                                armar_casos, cargar_criterios, cargar_preguntas,
                                cargar_respuestas, cargar_respuestas_app,
                                verificar_cross_hits)
from juez import construir_cliente_real, juzgar


DB_PREFIX = "juez_calibracion"


def gasto_dbs(cache_dir: Path, reps: int, pin: float, pout: float) -> dict:
    """Gasto real desde las dbs: solo filas de la tabla cache (una por miss pagado)."""
    tin = tout = filas = 0
    por_rep = {}
    for rep in range(1, reps + 1):
        p = cache_dir / f"{DB_PREFIX}_r{rep}.db"
        if not p.exists():
            por_rep[rep] = {"filas": 0, "in": 0, "out": 0, "usd": 0.0}
            continue
        conn = sqlite3.connect(str(p))
        n, i, o = conn.execute(
            "SELECT COUNT(*), COALESCE(SUM(input_tokens),0), COALESCE(SUM(output_tokens),0) "
            "FROM cache").fetchone()
        conn.close()
        por_rep[rep] = {"filas": n, "in": i, "out": o,
                        "usd": round(i / 1e6 * pin + o / 1e6 * pout, 4)}
        filas += n; tin += i; tout += o
    return {"filas": filas, "input_tokens": tin, "output_tokens": tout,
            "usd": round(tin / 1e6 * pin + tout / 1e6 * pout, 4), "por_rep": por_rep}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--criterios", required=True, type=Path)
    ap.add_argument("--reps", type=int, default=3)
    ap.add_argument("--precio-in", type=float, required=True)
    ap.add_argument("--precio-out", type=float, required=True)
    ap.add_argument("--tope", type=float, required=True)
    ap.add_argument("--out", type=Path, default=JUEZ_DIR / "out")
    ap.add_argument("--cache-dir", type=Path, default=JUEZ_DIR / "cache")
    ap.add_argument("--fuente-respuestas", choices=("trazas", "app"), default="trazas")
    ap.add_argument("--db-prefix", default="juez_calibracion",
                    help="prefijo de las dbs por repetición (separar pasadas)")
    args = ap.parse_args()
    pin, pout = args.precio_in, args.precio_out
    global DB_PREFIX
    DB_PREFIX = args.db_prefix

    preguntas = cargar_preguntas()
    respuestas = (cargar_respuestas_app(preguntas) if args.fuente_respuestas == "app"
                  else cargar_respuestas())
    casos = armar_casos(preguntas, respuestas, cargar_criterios(args.criterios))
    total_llamadas = len(casos) * args.reps
    args.out.mkdir(parents=True, exist_ok=True)
    print(f"{len(casos)} casos × {args.reps} reps = {total_llamadas} llamadas | "
          f"precios in {pin} / out {pout} USD/MTok | tope USD {args.tope}")

    frenado = None
    hechas = 0
    for rep in range(1, args.reps + 1):
        out_path = args.out / f"veredictos_r{rep}.jsonl"
        ya = _ya_juzgados(out_path)
        client = construir_cliente_real(rep, run_label=f"{RUN_LABEL_BASE}_{args.fuente_respuestas}_r{rep}",
                                        cache_dir=args.cache_dir, db_prefix=DB_PREFIX)
        try:
            with out_path.open("a", encoding="utf-8") as fh:
                for c in casos:
                    if c["qid"] in ya:
                        hechas += 1
                        continue
                    g = gasto_dbs(args.cache_dir, args.reps, pin, pout)
                    restantes = total_llamadas - hechas
                    prom = g["usd"] / g["filas"] if g["filas"] else 0.0
                    proy = g["usd"] + restantes * prom
                    if g["filas"] >= 3 and proy > args.tope:
                        frenado = {"en": f"rep {rep} {c['qid']}", "gasto_usd": g["usd"],
                                   "proyeccion_usd": round(proy, 4), "hechas": hechas,
                                   "restantes": restantes}
                        break
                    r = juzgar(client, c["pregunta"], c["respuesta"], c["criterios"])
                    reg = {"qid": c["qid"], "rep": rep,
                           "clasificacion_respuesta": r["veredicto"]["clasificacion_respuesta"],
                           "criterios": r["veredicto"]["criterios"],
                           "respondible_flag": c["respondible_flag"],
                           "meta": r["meta"]}
                    fh.write(json.dumps(reg, ensure_ascii=False) + "\n")
                    fh.flush()
                    hechas += 1
                    print(f"  [rep {rep}] {c['qid']} in={r['meta']['input_tokens']} "
                          f"out={r['meta']['output_tokens']} stop={r['meta']['stop_reason']} "
                          f"| acumulado USD {gasto_dbs(args.cache_dir, args.reps, pin, pout)['usd']}")
        finally:
            client.close()
        if frenado:
            break

    g = gasto_dbs(args.cache_dir, args.reps, pin, pout)
    resumen = {"fuente_respuestas": args.fuente_respuestas, "db_prefix": DB_PREFIX,
               "llamadas_hechas": hechas, "llamadas_totales": total_llamadas,
               "gasto_real": g, "precios": {"in": pin, "out": pout}, "tope": args.tope,
               "frenado_por_proyeccion": frenado}
    if frenado:
        print(f"FRENO POR PROYECCIÓN: {frenado}")
    else:
        agg = agregar(args.out, args.reps, casos)
        agg["verificacion_cross_hits"] = verificar_cross_hits(
            [args.cache_dir / f"{DB_PREFIX}_r{r}.db" for r in range(1, args.reps + 1)])
        (args.out / "veredictos_agregados.json").write_text(
            json.dumps(agg, ensure_ascii=False, indent=2), encoding="utf-8")
        resumen["cross_hits"] = agg["verificacion_cross_hits"]["cross_hits"]
        dist = {}
        for a in agg["agregados"]:
            dist[a["veredicto_pregunta"]] = dist.get(a["veredicto_pregunta"], 0) + 1
        resumen["veredictos_pregunta"] = dist
    (args.out / "resumen_corrida.json").write_text(
        json.dumps(resumen, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(resumen, ensure_ascii=False, indent=2))
    return 1 if frenado else 0


if __name__ == "__main__":
    raise SystemExit(main())
