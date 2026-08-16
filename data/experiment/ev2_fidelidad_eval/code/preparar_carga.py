"""
preparar_carga.py — Fase A.a/b (offline, USD 0): carga de las 120 respuestas de
EV2 con conteos, ids opacos, orden §3 y tabla de des-anonimización.

Escribe:
  - carga/censo_carga.json               — conteos (120; 40 por grafo; 3 por
                                           pregunta; 164 criterios) + sellos;
  - orden/orden_ev2_fidelidad_ciego.json — ids opacos en el orden
                                           random.Random("juez-ev2-v1").shuffle
                                           sobre (id_pregunta, sha256 respuesta);
  - desanonimizacion/tabla_id_opaco.json — id_opaco → (id_pregunta, grafo,
                                           label, sha256 respuesta); FUERA de
                                           out/ y de todo input del juez;
  - carga/mensajes_reales_medicion.json  — chars de los 120 mensajes reales
                                           del juez (system + usuario) por id
                                           opaco, insumo de la estimación. Sin
                                           grafo.
Si orden/ y desanonimizacion/ ya existen, verifica que coincidan (levanta si no).
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(CODE_DIR))
import comun_fidelidad as cf   # noqa: E402
from comun_fidelidad import juez  # noqa: E402


def main() -> int:
    sellos = cf.verificar_sellos()
    gold, respuestas, censo, casos = cf.cargar_todo()
    p_ord, p_tab = cf.persistir_orden_y_tabla(casos)
    ciegos = cf.vista_ciega(casos)

    # medición de los mensajes reales (chars), sin grafo
    med = []
    for c in ciegos:
        kw = juez.construir_kwargs(c["pregunta"], c["respuesta"], c["criterios"])
        med.append({"id_opaco": c["id_opaco"], "n_criterios": len(c["criterios"]),
                    "chars_system": len(kw["system"]),
                    "chars_usuario": len(kw["messages"][0]["content"]),
                    "chars_respuesta": len(c["respuesta"])})
    cf.CARGA_DIR.mkdir(parents=True, exist_ok=True)
    (cf.CARGA_DIR / "mensajes_reales_medicion.json").write_text(
        json.dumps({"n": len(med), "modelo": juez.MODELO, "max_tokens": juez.MAX_TOKENS,
                    "temperature": juez.TEMPERATURE, "prompt_sha256": juez.PROMPT_SHA256,
                    "mensajes": sorted(med, key=lambda m: m["id_opaco"])},
                   ensure_ascii=False, indent=2), encoding="utf-8")

    censo_out = {"sellos": sellos, "censo": censo,
                 "orden": {"archivo": str(p_ord.relative_to(cf.REPO_DIR)),
                           "semilla": cf.SEMILLA_ORDEN, "n": len(casos),
                           "primeros_5_ids_opacos": [c["id_opaco"] for c in casos[:5]],
                           "empates_clave_orden": casos[0]["empates_clave_orden"]},
                 "tabla_desanonimizacion": {"archivo": str(p_tab.relative_to(cf.REPO_DIR)),
                                            "n": len(casos),
                                            "ids_opacos_unicos": len({c["id_opaco"] for c in casos})},
                 "gold": {"archivo": str(cf.GOLD_PATH.relative_to(cf.REPO_DIR)),
                          "n_preguntas": len(gold),
                          "n_criterios": sum(len(g["criterios"]) for g in gold.values()),
                          "criterios_por_pregunta": dict(sorted(
                              __import__("collections").Counter(len(g["criterios"]) for g in gold.values()).items()))},
                 "marcadores_grafo_en_respuestas": sorted({m for c in ciegos
                                                          for m in cf.buscar_marcadores(c["respuesta"])})}
    (cf.CARGA_DIR / "censo_carga.json").write_text(
        json.dumps(censo_out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(censo_out, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
