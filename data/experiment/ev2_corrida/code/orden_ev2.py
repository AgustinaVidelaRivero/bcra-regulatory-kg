"""
orden_ev2.py — Orden de ejecución resuelto (protocolo §5, semilla orden-ev2-v1).

Construye la lista completa de casos de la corrida (40 fidelidad + 128
navegabilidad = 168), la ordena por caso_id, aplica
random.Random("orden-ev2-v1").shuffle UNA vez, y persiste:

  - orden_global: la secuencia resuelta (idéntica para los tres grafos);
  - orden_por_grafo: la secuencia efectiva de cada grafo, que SALTEA los
    casos de navegabilidad ausentes según el censo (censo_navegabilidad_*.json)
    sin re-barajar — el orden relativo de los presentes se conserva.

Uso:  python3 -B orden_ev2.py   (requiere censo ya generado)
"""

from __future__ import annotations

import json
from datetime import datetime

from comun_ev2 import EV2_DIR, GRAFO_KEYS, SEMILLA_ORDEN, orden_resuelto

ORDEN_DIR = EV2_DIR / "orden"
CENSO_DIR = EV2_DIR / "censo"


def main() -> int:
    casos = orden_resuelto()
    assert len(casos) == 168, f"casos != 168: {len(casos)}"

    ausentes = {}
    for g in GRAFO_KEYS:
        with open(CENSO_DIR / f"censo_navegabilidad_{g}.json",
                  encoding="utf-8") as f:
            ausentes[g] = set(json.load(f)["ids_ausentes"])

    orden_global = [{"pos": i + 1, "caso_id": c["caso_id"], "eje": c["eje"]}
                    for i, c in enumerate(casos)]
    por_grafo = {}
    for g in GRAFO_KEYS:
        efectivo = [c["caso_id"] for c in casos
                    if not (c["eje"] == "navegabilidad"
                            and c["sample_id"] in ausentes[g])]
        por_grafo[g] = {"n_casos_efectivos": len(efectivo),
                        "n_salteados": len(casos) - len(efectivo),
                        "orden_efectivo": efectivo}

    payload = {
        "generado": datetime.now().isoformat(timespec="seconds"),
        "semilla": SEMILLA_ORDEN,
        "regla": ("sorted(casos, key=caso_id) + random.Random(semilla).shuffle; "
                  "por grafo se saltean las ausencias del censo sin re-barajar"),
        "n_casos": len(casos),
        "orden_global": orden_global,
        "orden_por_grafo": por_grafo,
    }
    ORDEN_DIR.mkdir(parents=True, exist_ok=True)
    out = ORDEN_DIR / "orden_ev2_resuelto.json"
    with out.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    print(f"orden resuelto ({len(casos)} casos) -> {out}")
    for g in GRAFO_KEYS:
        print(f"  {g}: efectivos {por_grafo[g]['n_casos_efectivos']} "
              f"(salteados {por_grafo[g]['n_salteados']})")
    print("  primeros 5:", [c["caso_id"] for c in casos[:5]])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
