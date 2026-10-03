"""
frecuencia_r2a.py — U-PROMPT-R2, P1 (USD 0): qué son los valores de `Obligacion.frecuencia` fuera de la lista en
el grafo r2a de los diez TOs (insumo de la decisión 20, junto con M2.c de U-MED-R2A, c50b094).

Solo lectura. Uso (desde la raíz del repo):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p1/frecuencia_r2a.py
Escribe data/experiment/prompt_r2/p1/salida/frecuencia_r2a.json.
"""
from __future__ import annotations

import hashlib
import json
import re
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
KG = REPO / "data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2a/r2/kg.json"
ENUMS = REPO / "data/experiment/pyd_r2/generados/enums_r2.json"
SAL = Path(__file__).resolve().parent / "salida" / "frecuencia_r2a.json"
# Valores de relleno: no copian texto, declaran que no hay plazo (proxy declarada, no lectura).
RE_RELLENO = re.compile(r"^(n/?a|sin (plazo )?especific|no especificad|sin plazo|pendiente|de corresponder|"
                        r"conforme a|seg[uú]n lo)", re.I)


def main() -> None:
    raw = KG.read_bytes()
    assert hashlib.sha256(raw).hexdigest().startswith("99fe2bfa"), "el grafo r2a no es el de M1 (99fe2bfa…)"
    kg = json.loads(raw)
    lista = set(json.loads(ENUMS.read_text(encoding="utf-8"))["Obligacion.frecuencia"])
    fuera = Counter()
    for n in kg["nodes"]:
        f = (n.get("properties") or {}).get("frecuencia") if n["type"] == "Obligacion" else None
        if isinstance(f, str) and f.strip() and f.strip().lower() not in lista:
            fuera[f.strip()] += 1
    relleno = {v: c for v, c in fuera.items() if RE_RELLENO.search(v)}
    out = {"grafo": str(KG.relative_to(REPO)), "lista": sorted(lista),
           "nodos_fuera_de_lista": sum(fuera.values()), "valores_distintos": len(fuera),
           "relleno": {"nodos": sum(relleno.values()), "valores": len(relleno)},
           "mas_frecuentes": fuera.most_common(40)}
    SAL.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(out["nodos_fuera_de_lista"], out["valores_distintos"], out["relleno"])


if __name__ == "__main__":
    main()
