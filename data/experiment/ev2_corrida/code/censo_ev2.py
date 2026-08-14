"""
censo_ev2.py — Censo previo por grafo del eje de navegabilidad (protocolo §2,
diseño de sintéticas §4) + resolución de golds por grafo.

Para cada uno de los 64 samples aptos y cada grafo (v2 / v3 / run_3):
  - resuelve cada ancla del gold con resolucion.AnclaIndex (regla sellada:
    match EXACTO de punto normalizado, contenedores >10 anclas excluidos);
  - clasifica el caso en ese grafo:
      presente          — TODAS sus anclas resuelven a >=1 nodo
      presente_parcial  — alguna ancla resuelve y alguna no (el caso CORRE en
                          navegabilidad sobre las anclas resueltas; las no
                          resueltas se reportan como ausencias, dato de
                          fidelidad — es exactamente el comportamiento de
                          metrica.evaluar_por_anclas)
      ausente           — NINGUNA ancla resuelve (el caso se excluye de la
                          navegabilidad de ese grafo; ausencia = dato de
                          fidelidad).
    "Presentes" a efectos de la corrida = presente + presente_parcial (hay
    gold medible); presentes + ausentes = 64 por grafo.

Salida: censo/censo_navegabilidad_<grafo>.json (uno por grafo, con ids y
nodos-gold resueltos) + censo/censo_resumen.json (tabla comparativa).

Uso:  python3 -B censo_ev2.py
"""

from __future__ import annotations

import json
from datetime import datetime

from comun_ev2 import (EV2_DIR, GRAFOS, GRAFO_KEYS, cargar_aptos,
                       indice_anclas, rel_repo, verificar_grafos)

CENSO_DIR = EV2_DIR / "censo"


def censar_grafo(grafo: str, aptos: list[dict]) -> dict:
    idx = indice_anclas(grafo)
    casos = []
    for r in aptos:
        anclas = r["gold"]["anclas"]
        detalle = []
        for a in anclas:
            ids = idx.resolver(a["to"], a["ancla"])
            detalle.append({"to": a["to"], "ancla": a["ancla"],
                            "n_nodos": len(ids), "nodos_gold": ids})
        n_res = sum(1 for d in detalle if d["n_nodos"] > 0)
        if n_res == len(detalle):
            estado = "presente"
        elif n_res == 0:
            estado = "ausente"
        else:
            estado = "presente_parcial"
        casos.append({
            "sample_id": r["sample_id"],
            "estrato": r["estrato"],
            "estado": estado,
            "n_anclas": len(detalle),
            "n_anclas_resueltas": n_res,
            "anclas": detalle,
        })

    presentes = [c for c in casos if c["estado"] in ("presente", "presente_parcial")]
    ausentes = [c for c in casos if c["estado"] == "ausente"]
    return {
        "grafo": grafo,
        "kg_path": rel_repo(GRAFOS[grafo]["path"]),
        "kg_sha256": GRAFOS[grafo]["sha256"],
        "generado": datetime.now().isoformat(timespec="seconds"),
        "regla": ("resolucion.AnclaIndex: match exacto de punto normalizado, "
                  "contenedores >10 anclas excluidos (CONTENEDOR_MAX_ANCLAS=10)"),
        "n_casos": len(casos),
        "n_presentes": len(presentes),
        "n_presentes_completos": sum(1 for c in casos if c["estado"] == "presente"),
        "n_presentes_parciales": sum(1 for c in casos
                                     if c["estado"] == "presente_parcial"),
        "n_ausentes": len(ausentes),
        "ids_presentes": [c["sample_id"] for c in presentes],
        "ids_presentes_parciales": [c["sample_id"] for c in casos
                                    if c["estado"] == "presente_parcial"],
        "ids_ausentes": [c["sample_id"] for c in ausentes],
        "n_contenedores_excluidos": len(idx.contenedores),
        "n_provenances_sin_parsear": len(idx.sin_parsear),
        "casos": casos,
    }


def main() -> int:
    print("== Censo previo por grafo (EV2, eje navegabilidad) ==")
    verificar_grafos()
    aptos = cargar_aptos()
    assert len(aptos) == 64, f"aptos != 64: {len(aptos)}"

    CENSO_DIR.mkdir(parents=True, exist_ok=True)
    resumen = {"generado": datetime.now().isoformat(timespec="seconds"),
               "n_casos_por_grafo": len(aptos), "grafos": {}}
    for g in GRAFO_KEYS:
        censo = censar_grafo(g, aptos)
        out = CENSO_DIR / f"censo_navegabilidad_{g}.json"
        with out.open("w", encoding="utf-8") as f:
            json.dump(censo, f, ensure_ascii=False, indent=2)
        chk = censo["n_presentes"] + censo["n_ausentes"]
        print(f"  {g}: presentes {censo['n_presentes']} "
              f"(completos {censo['n_presentes_completos']}, "
              f"parciales {censo['n_presentes_parciales']}) "
              f"+ ausentes {censo['n_ausentes']} = {chk}  -> {out.name}")
        assert chk == len(aptos), f"censo {g} no suma {len(aptos)}"
        resumen["grafos"][g] = {k: censo[k] for k in (
            "kg_sha256", "n_presentes", "n_presentes_completos",
            "n_presentes_parciales", "n_ausentes", "ids_ausentes",
            "ids_presentes_parciales", "n_contenedores_excluidos",
            "n_provenances_sin_parsear")}

    out = CENSO_DIR / "censo_resumen.json"
    with out.open("w", encoding="utf-8") as f:
        json.dump(resumen, f, ensure_ascii=False, indent=2)
    print(f"  resumen -> {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
