"""U-REEXT-T0, T4, punto 4: las unidades con la marca del tercer escalón del reintento por corte en la corrida r2b de
los diez TOs. El runner (corpus_v2/runner_corpus.py) pone la marca `escalon_3` en el registro de E1 de la unidad y la
lista en resumen_e1.json; aquí se cuentan las dos fuentes, y aparte los registros con reintento por corte (que pasaron
con el segundo escalón). Escribe --out. USD 0, sin red.

Uso (desde la raíz de una copia): python -B data/experiment/reext_t0/t4/escalon3_t4.py --out J
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[4]
SALIDA = RAIZ / "data" / "experiment" / "reextraccion_v2" / "corpus_tanda0" / "salida_r2b"
TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    registros, con_marca, en_resumen, corte, errores = 0, [], {}, [], Counter()
    for to in TOS:
        for x in (SALIDA / to / "extracciones_e1.jsonl").read_text(encoding="utf-8").splitlines():
            if x.strip():
                r = json.loads(x)
                registros += 1
                if "escalon_3" in r:
                    con_marca.append(r["chunk_id"])
                if r.get("reintento_corte"):
                    corte.append(r["chunk_id"])
                if r.get("error"):
                    errores[r["error"]] += 1
        res = json.loads((SALIDA / to / "resumen_e1.json").read_text(encoding="utf-8"))
        if "escalon_3" in res:
            en_resumen[to] = res["escalon_3"]
    out = {"registros_e1": registros, "registros_con_escalon_3": len(con_marca), "unidades_con_escalon_3": sorted(set(con_marca)),
           "resumen_e1_con_escalon_3": en_resumen,
           "registros_con_reintento_corte": len(corte), "unidades_con_reintento_corte": sorted(set(corte)),
           "errores_e1": dict(errores)}
    a.out.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
