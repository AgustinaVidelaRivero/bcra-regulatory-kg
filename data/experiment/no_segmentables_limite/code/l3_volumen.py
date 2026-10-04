"""U-NOSEG-LIMITE, L3 — volumen del texto por página que quedaría al alcance del agente (diseño; este
script solo mide). USD 0, solo lectura del repo.

Mide, con los caracteres por página extraídos por `e0_lib.extraer_lineas` en el espejo del scratchpad
(entrada --roles, registrada con su sha256): páginas, caracteres, caracteres por página (mediana y
máximo) y una ESTIMACIÓN NO VERIFICADA de tokens y de costo de entrada por página leída, para cuatro
conjuntos: los 12 no segmentables, los 9 del bloque A, las fichas de los 2 parciales y las páginas de
cuerpo entre fichas (población del estrato 3 de L4). Escribe `l3_volumen.json`.

Anclas de la estimación:
  - caracteres por token de entrada: mediana 3,2267 [3,0287; 3,3696], 360 llamadas
    (data/experiment/ev2_encadenamiento/estimacion/estimacion_fase_b.md:20); es otra mezcla de texto,
    así que la cifra es orientativa;
  - tarifa de entrada de Haiku 4.5: USD 1,00 por millón de tokens
    (data/experiment/cobertura_bloque_a/code/correr_a2.py:43).

Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/no_segmentables_limite/code/l3_volumen.py \
      --roles <roles_por_pagina_todos.json del scratchpad>
"""

from __future__ import annotations

import argparse
import hashlib
import json
import statistics
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
OUT = REPO / "data" / "experiment" / "no_segmentables_limite"
CPT = (3.0287, 3.2267, 3.3696)
USD_MTOK_IN = 1.00
DOCE = ("optico", "plandecuentas", "ri_chr", "ri_con", "ri_fcem", "ri_itme", "ri_pfmipyme", "ri_pscpp",
        "ri_pspii", "ri_rem", "ri_spi", "ri_tii")
NUEVE = ("ri_chr", "ri_con", "ri_fcem", "ri_itme", "ri_pfmipyme", "ri_pscpp", "ri_pspii", "ri_rem", "ri_tii")


def stats(chars: list[int]) -> dict:
    tot = sum(chars)
    med = statistics.median(chars) if chars else 0
    return {"paginas": len(chars), "caracteres": tot, "mediana_por_pagina": med,
            "maximo_por_pagina": max(chars) if chars else 0,
            "tokens_por_pagina_mediana_estimacion": [round(med / c) for c in reversed(CPT)],
            "usd_entrada_por_pagina_mediana_estimacion": [round(med / c / 1e6 * USD_MTOK_IN, 5) for c in reversed(CPT)],
            "tokens_total_estimacion": [round(tot / c) for c in reversed(CPT)]}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--roles", required=True)
    a = ap.parse_args()
    roles = json.loads(Path(a.roles).read_text(encoding="utf-8"))
    muestra = json.loads((OUT / "l4_muestra.json").read_text(encoding="utf-8"))
    pob3 = {(t, p) for t, p in muestra["poblacion_estrato_3"]}

    def chars(tos, rol=None, extra=None):
        out = []
        for t in tos:
            r, c = roles[t]["roles"], roles[t]["chars_por_pagina"]
            for i in range(len(r)):
                if (rol is None or r[i] == rol) and (extra is None or (t, i + 1) in extra):
                    out.append(c[i])
        return out

    res = {"_meta": {"unidad": "U-NOSEG-LIMITE, L3", "sha256_roles": hashlib.sha256(Path(a.roles).read_bytes()).hexdigest(),
                     "chars_por_token": CPT, "usd_por_mtok_entrada": USD_MTOK_IN,
                     "nota": "ESTIMACIÓN NO VERIFICADA: tokens y USD derivados de caracteres con la razón citada"},
           "doce_no_segmentables": stats(chars(DOCE)),
           "nueve_bloque_a": stats(chars(NUEVE)),
           "ri_spi": stats(chars(("ri_spi",))),
           "optico_y_plandecuentas": stats(chars(("optico", "plandecuentas"))),
           "fichas_de_los_parciales": stats(chars(("manual", "ri2_pm"), rol="ficha_registro")),
           "cuerpo_entre_fichas": stats(chars(("manual", "ri2_pm"), rol="cuerpo", extra=pob3)),
           "por_to": {t: stats(chars((t,))) for t in DOCE + ("manual", "ri2_pm")}}
    (OUT / "l3_volumen.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for k in ("doce_no_segmentables", "nueve_bloque_a", "ri_spi", "optico_y_plandecuentas",
              "fichas_de_los_parciales", "cuerpo_entre_fichas"):
        print(k, {x: res[k][x] for x in ("paginas", "caracteres", "mediana_por_pagina", "maximo_por_pagina",
                                         "tokens_por_pagina_mediana_estimacion", "tokens_total_estimacion")})


if __name__ == "__main__":
    main()
