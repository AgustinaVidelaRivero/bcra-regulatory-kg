"""
correr_e2.py — CLI de la corrida E2 (reduce) para un TO.

Uso:
    python3 correr_e2.py --to pro \
        --extracciones ../e1_extractor/salida/faseB_pro/extracciones.jsonl

Escribe en salida/: grafo_<to>.json, fanin_<to>.json, censo_<to>.json,
reporte_e2_<to>.json. Si la guarda de fan-in detecta ausentes, duplicados o
inesperados, ABORTA sin escribir grafo (solo persiste el reporte de fan-in),
salvo --permitir-parcial explícito — en cuyo caso el reporte queda marcado
`parcial: true`. Código puro, cero LLM.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from e2_lib import BASE, FanInError, TOS, reducir

SALIDA = BASE / "salida"


def _dump(path: Path, obj) -> None:
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--to", required=True, choices=TOS)
    ap.add_argument("--extracciones", required=True, type=Path)
    ap.add_argument("--permitir-parcial", action="store_true",
                    help="ensambla aun con fan-in no apto; el reporte queda "
                         "marcado parcial (jamás es el default)")
    args = ap.parse_args()

    SALIDA.mkdir(parents=True, exist_ok=True)
    try:
        res = reducir(args.to, args.extracciones,
                      permitir_parcial=args.permitir_parcial)
    except FanInError as e:
        _dump(SALIDA / f"fanin_{args.to}.json", e.fanin)
        print(f"ABORTADO — {e}", flush=True)
        print(f"Reporte de fan-in: {SALIDA / f'fanin_{args.to}.json'}", flush=True)
        return 2

    (SALIDA / f"grafo_{args.to}.json").write_text(res["grafo_json"] + "\n",
                                                  encoding="utf-8")
    _dump(SALIDA / f"fanin_{args.to}.json", res["fanin"])
    _dump(SALIDA / f"censo_{args.to}.json", res["censo"])
    _dump(SALIDA / f"reporte_e2_{args.to}.json", res["reporte"])

    r = res["reporte"]
    print(json.dumps({k: r[k] for k in
                      ("to", "parcial", "fanin", "nodes_total", "edges_total",
                       "nodes_by_type", "edges_by_relation", "stats",
                       "cuarentena", "sha256_grafo")},
                     ensure_ascii=False, indent=2), flush=True)
    nc, nm = r["censo"]["nivel_chunk"], r["censo"]["nivel_mapa"]
    print(f"\nCenso nivel chunk: {nc['cubiertas']}/{nc['unidades']} cubiertas, "
          f"{len(nc['ausencias'])} ausencias", flush=True)
    for a in nc["ausencias"]:
        print(f"  - {a['unidad']} ({a['chunk_id']}): {a['diagnostico']}", flush=True)
    print(f"Censo nivel mapa: {nm['cubiertas']}/{nm['unidades']} cubiertas, "
          f"{len(nm['ausencias'])} ausencias", flush=True)
    for a in nm["ausencias"]:
        print(f"  - {a['unidad']}: {a['diagnostico']}", flush=True)
    if r["rechazos_e2"]:
        print(f"\nRECHAZOS E2 (re-validación): {len(r['rechazos_e2'])}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
