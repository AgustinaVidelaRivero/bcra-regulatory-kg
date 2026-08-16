"""
cruce_mesa.py — Herramienta de la REVISIÓN: cruza los veredictos ciegos
(out/veredictos_agregados_ciego.json) con la tabla de des-anonimización
(desanonimizacion/tabla_id_opaco.json) → veredicto × grafo, por pregunta.

Este script NO se ejecuta sobre las salidas reales dentro de la unidad de
evaluación: el mandato reserva el cruce veredicto × grafo a la mesa de revisión.
En la unidad solo se prueba sobre los datos SINTÉTICOS del selftest.

Uso (mesa):
  .venv/bin/python -B data/experiment/ev2_fidelidad_eval/code/cruce_mesa.py \
      [--agregados out/veredictos_agregados_ciego.json] \
      [--tabla desanonimizacion/tabla_id_opaco.json] [--out <ruta.json>]
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

UNIDAD_DIR = Path(__file__).resolve().parent.parent


def cruzar(agg: dict, tabla: dict) -> dict:
    fila = {f["id_opaco"]: f for f in tabla["filas"]}
    por_grafo = defaultdict(Counter)
    por_pregunta = defaultdict(dict)
    filas = []
    for a in agg["agregados"]:
        f = fila[a["id_opaco"]]
        por_grafo[f["grafo"]][a["veredicto_pregunta"]] += 1
        por_pregunta[f["id_pregunta"]][f["grafo"]] = a["veredicto_pregunta"]
        filas.append({"id_opaco": a["id_opaco"], "id_pregunta": f["id_pregunta"], "grafo": f["grafo"],
                      "veredicto": a["veredicto_pregunta"], "modales": a["modales"],
                      "clasificacion_auxiliar": a["clasificacion_respuesta_modal"],
                      "respondible_flag": f.get("respondible_flag"),
                      "auditoria_fragmentos": a["auditoria_fragmentos"]})
    inc = Counter(fila[x["id_opaco"]]["grafo"] for x in agg.get("incompletas", []))
    return {"n_filas": len(filas),
            "veredicto_por_grafo": {g: dict(c) for g, c in sorted(por_grafo.items())},
            "incompletas_por_grafo": dict(inc),
            "por_pregunta": {q: dict(sorted(v.items())) for q, v in sorted(por_pregunta.items())},
            "filas": sorted(filas, key=lambda x: (x["id_pregunta"], x["grafo"]))}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--agregados", type=Path, default=UNIDAD_DIR / "out" / "veredictos_agregados_ciego.json")
    ap.add_argument("--tabla", type=Path, default=UNIDAD_DIR / "desanonimizacion" / "tabla_id_opaco.json")
    ap.add_argument("--out", type=Path, default=None)
    args = ap.parse_args()
    agg = json.loads(args.agregados.read_text(encoding="utf-8"))
    tabla = json.loads(args.tabla.read_text(encoding="utf-8"))
    cruce = cruzar(agg, tabla)
    texto = json.dumps(cruce, ensure_ascii=False, indent=2)
    if args.out:
        args.out.write_text(texto, encoding="utf-8")
        print(f"→ {args.out}")
    print(json.dumps({"n_filas": cruce["n_filas"], "veredicto_por_grafo": cruce["veredicto_por_grafo"],
                      "incompletas_por_grafo": cruce["incompletas_por_grafo"]}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
