#!/usr/bin/env python3
"""inventario_caracteres_e0.py — Inventario de caracteres de los pasajes (propio + herencia) de una E0
(USD 0). Sirve para saber qué reglas del tokenizador UAX #29 aplican de verdad al corpus del BM25 de
fragmentos (FRENO A2.1-a, §4).

Uso: python3 -B inventario_caracteres_e0.py [--manifiesto <manifiestos_e0/...json>]
     (escribe controles/inventario_caracteres_<manifiesto_e0>.json)
"""
from __future__ import annotations

import argparse
import collections
import json
import sys
import unicodedata
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BANCO_DIR = AQUI.parent
for _p in (str(BANCO_DIR), str(BANCO_DIR / "mcp_vector")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import construir_indice as CI                 # noqa: E402
from comun_banco import rel_repo              # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifiesto", type=Path, default=BANCO_DIR / "mcp_vector" / "manifiestos_e0" / "e0_tanda0_r2b_desarrollo.json")
    a = ap.parse_args()
    man, man_e0 = CI.cargar_manifiesto(a.manifiesto)
    pasajes, _ = CI.construir_pasajes(man)
    cnt = collections.Counter(ch for p in pasajes for ch in p["texto"])
    cats = collections.Counter()
    for ch, n in cnt.items():
        cats[unicodedata.category(ch)] += n
    no_alfanum = sorted(([f"U+{ord(ch):04X}", unicodedata.name(ch, "?"), unicodedata.category(ch), n]
                         for ch, n in cnt.items() if not ch.isalnum() and ch not in " \n"), key=lambda x: -x[3])
    letras_no_latinas = sorted([ch, unicodedata.name(ch, "?"), n] for ch, n in cnt.items()
                               if ch.isalpha() and "LATIN" not in unicodedata.name(ch, ""))
    out = {"unidad": "A2.1, tramo 1 — inventario de caracteres de la E0 del BM25",
           "comando": f"python3 -B data/experiment/banco_mcp/a2_1/inventario_caracteres_e0.py --manifiesto {rel_repo(a.manifiesto)}",
           "manifiesto_e0": man_e0, "unicodedata": unicodedata.unidata_version, "n_pasajes": len(pasajes),
           "n_caracteres": sum(cnt.values()), "n_distintos": len(cnt),
           "fuera_del_plano_basico": sum(n for ch, n in cnt.items() if ord(ch) > 0xFFFF),
           "por_categoria": dict(sorted(cats.items())),
           "marcas_y_formato": {c: cats.get(c, 0) for c in ("Mn", "Mc", "Me", "Cf")},
           "guion_blando_U+00AD": cnt.get("­", 0), "espacio_fino_U+202F": cnt.get(" ", 0),
           "no_alfanumericos": no_alfanum, "letras_no_latinas": letras_no_latinas}
    (AQUI / "controles").mkdir(exist_ok=True)
    salida = AQUI / "controles" / f"inventario_caracteres_{man['manifiesto_e0']}.json"
    salida.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print({k: out[k] for k in ("n_pasajes", "n_caracteres", "n_distintos", "fuera_del_plano_basico", "marcas_y_formato",
                               "guion_blando_U+00AD", "espacio_fino_U+202F")}, "| letras no latinas:",
          [x[0] for x in letras_no_latinas], "->", rel_repo(salida))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
