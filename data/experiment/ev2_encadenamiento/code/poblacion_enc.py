"""
poblacion_enc.py — Fase A (offline, USD 0): derivación de la población disparada
por la corrida base de fidelidad, con conteos verificados contra lo esperado.

Escribe:
  - sellos/sellos_inicio_faseA.txt      — sha256 del instrumento, cuarteto, grafos
                                          e insumos de la base;
  - poblacion/poblacion_disparada.json  — 63 pares "parcial" (v2 23 / v3 22 /
                                          run_3 18) + auditoría (1 por grafo,
                                          semilla auditoria-ev2-v1) = 66 pares;
  - orden/orden_agente_por_grafo.json   — casos por grafo en el orden del
                                          protocolo §5 (orden-ev2-v1 filtrado).
Si poblacion/ ya existe, verifica que coincida (levanta si no).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(CODE_DIR))
import comun_enc as en   # noqa: E402


def main() -> int:
    p_sellos = en.escribir_sellos("sellos_inicio_faseA.txt")
    pob = en.derivar_poblacion()
    en.POBLACION_DIR.mkdir(parents=True, exist_ok=True)
    p_pob = en.POBLACION_DIR / "poblacion_disparada.json"
    nuevo = json.dumps(pob, ensure_ascii=False, indent=2)
    if p_pob.exists() and json.loads(p_pob.read_text(encoding="utf-8"))["pares"] != pob["pares"]:
        raise RuntimeError(f"{p_pob} ya existe y difiere de lo recomputado")
    p_pob.write_text(nuevo, encoding="utf-8")

    orden = {}
    for g in en.GRAFOS:
        cs = en.casos_agente(pob, g)
        orden[g] = {"label_por_rep": {r: en.label_agente(g, r) for r in range(1, en.REPS_AGENTE + 1)},
                    "n_casos": len(cs),
                    "casos": [{"caso_id": c["caso_id"], "pos_orden_global": c["pos_orden_global"]}
                              for c in cs]}
    en.ORDEN_DIR.mkdir(parents=True, exist_ok=True)
    p_ord = en.ORDEN_DIR / "orden_agente_por_grafo.json"
    p_ord.write_text(json.dumps({"semilla": en.ce.SEMILLA_ORDEN,
                                 "regla": "orden resuelto global de la corrida base (comun_ev2.orden_resuelto) "
                                          "filtrado a los pares disparados de cada grafo; mismo orden en las 3 reps",
                                 "por_grafo": orden}, ensure_ascii=False, indent=2), encoding="utf-8")

    resumen = {k: v for k, v in pob.items() if k != "pares"}
    resumen["sellos"] = en.rel_repo(p_sellos)
    resumen["archivos"] = [en.rel_repo(p_pob), en.rel_repo(p_ord)]
    print(json.dumps(resumen, ensure_ascii=False, indent=2))
    print("pares por (grafo, tipo):")
    from collections import Counter
    for k, n in sorted(Counter((p["grafo"], p["tipo"]) for p in pob["pares"]).items()):
        print(f"  {k}: {n}")
    print("auditoría:", {g: v["ids_muestra"] for g, v in pob["auditoria_por_grafo"].items()})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
