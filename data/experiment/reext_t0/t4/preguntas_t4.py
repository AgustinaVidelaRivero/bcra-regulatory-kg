"""U-REEXT-T0, T4, punto 2: las 15 preguntas de control sobre KG-Tanda0-Diez-r2b, pregunta por pregunta contra r2a. No
son evaluación ni se reportan como resultado. La corrida sobre r2b es la de t1_preguntas_control.py (sin cambios), con
--kg del ensamblado r2b de diez y la E0 r2b, sobre una copia; la de r2a es la de T1 (salida/preguntas_r2a.json, con la
revisión de la mesa). Este script solo las cruza. Escribe --out (JSON) y --md. USD 0, sin red.

Uso (desde la raíz de una copia):
  python -B data/experiment/reext_t0/t1_preguntas_control.py --kg data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2b/r2/kg.json \
      --e0 data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b --out DIR/preguntas_r2b.json
  python -B data/experiment/reext_t0/t4/preguntas_t4.py --r2b DIR/preguntas_r2b.json --out J --md M
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[4]
R2A = RAIZ / "data" / "experiment" / "reext_t0" / "salida" / "preguntas_r2a.json"
SHA_KG_R2B = "a9631a64b422bdae634fb05135373c6f04c6272cdf7acd43a1be9f5b6c1f5f57"
ORDEN = ("bien", "en parte", "falso", "no")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--r2b", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--md", type=Path, required=True)
    a = ap.parse_args()
    b, r = json.loads(a.r2b.read_text(encoding="utf-8")), json.loads(R2A.read_text(encoding="utf-8"))
    assert b["kg_sha256"] == SHA_KG_R2B, "la corrida r2b no es sobre el grafo sellado"
    pa = {p["n"]: p for p in r["preguntas"]}
    filas = []
    for p in b["preguntas"]:
        q = pa[p["n"]]
        filas.append({"n": p["n"], "pregunta": p["pregunta"], "r2a": q["resultado"], "r2b": p["resultado"],
                      "cambia": q["resultado"] != p["resultado"], "rango_r2a": q.get("rango_bm25_del_ancla"),
                      "rango_r2b": p.get("rango_bm25_del_ancla"), "detalle_r2a": q.get("detalle"),
                      "detalle_r2b": p.get("detalle")})
    tot = {k: dict(Counter(f[k] for f in filas)) for k in ("r2a", "r2b")}
    for k in tot:
        assert tot[k] == {x: v for x, v in (r if k == "r2a" else b)["totales"].items() if v}, k
    res = {"kg_r2b_sha256": b["kg_sha256"], "kg_r2a_sha256": r["kg_sha256"],
           "totales": {k: {x: tot[k].get(x, 0) for x in ORDEN} for k in tot},
           "cambian": [f["n"] for f in filas if f["cambia"]],
           "transiciones": dict(Counter(f"{f['r2a']} → {f['r2b']}" for f in filas if f["cambia"])),
           "nota": "no son evaluación ni se reportan como resultado (mandato de U-REEXT-T0, T4, punto 2)"}
    a.out.write_text(json.dumps({"resumen": res, "preguntas": filas}, ensure_ascii=False, indent=1) + "\n",
                     encoding="utf-8")
    md = ["# Punto 2: las 15 preguntas de control, r2b contra r2a (U-REEXT-T0, T4)", "",
          f"No son evaluación. r2b: `{b['kg_sha256'][:8]}…`; r2a: `{r['kg_sha256'][:8]}…`. Totales r2a "
          f"{res['totales']['r2a']}; r2b {res['totales']['r2b']}.", "",
          "| # | r2a | r2b | detalle r2b |", "|---|---|---|---|"]
    md += [f"| {f['n']} | {f['r2a']} | {f['r2b']}{' (cambia)' if f['cambia'] else ''} | {f['detalle_r2b']} |"
           for f in filas]
    a.md.write_text("\n".join(md) + "\n", encoding="utf-8")
    print(json.dumps(res, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
