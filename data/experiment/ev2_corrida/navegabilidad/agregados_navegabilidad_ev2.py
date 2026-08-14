"""agregados_navegabilidad_ev2.py — Agregados del eje de navegabilidad EV2.

Lee los resultados por caso (resultados_navegabilidad_<label>.json, producidos
por replay_navegabilidad_ev2.py) y computa los agregados del mandato, siempre
etiquetados por cohorte y SIN promediar cohortes entre sí:

  - por grafo × variante (literal vs anti-léxica);
  - por grafo × estrato (E-A..E-E) × variante;
  - cohorte núcleo limpio (E-E) y cohorte dirigida (E-A..E-D), por separado;
  - tabla de ausencias por grafo (ids del censo commiteado) + anclas ausentes
    parciales por caso.

Cada celda trae: n_casos, n_anclas (pooled), y recall micro (pooled sobre
anclas) y macro (promedio de recalls por caso) para vista y consultada, más
la brecha vista-sin-consultar. Determinístico, $0.

Salida: agregados_navegabilidad.json (dentro de navegabilidad/).
"""

import json
from pathlib import Path

NAV_DIR = Path(__file__).resolve().parent
EV2_DIR = NAV_DIR.parent
CENSO_DIR = EV2_DIR / "censo"

LABELS = {"v2": "ev2_base_v2", "v3": "ev2_base_v3", "run_3": "ev2_base_run3"}
ESTRATOS = ["E-A", "E-B", "E-C", "E-D", "E-E"]
VARIANTES = ["literal", "antilexica"]
DIRIGIDA = {"E-A", "E-B", "E-C", "E-D"}


def celda(casos: list[dict]) -> dict:
    n = len(casos)
    if n == 0:
        return {"n_casos": 0}
    na = sum(c["n_anclas"] for c in casos)
    nv = sum(c["n_vistas"] for c in casos)
    nc = sum(c["n_consultadas"] for c in casos)
    nb = sum(c["n_brecha"] for c in casos)
    return {
        "n_casos": n,
        "n_anclas": na,
        "n_vistas": nv,
        "n_consultadas": nc,
        "n_brecha_vista_sin_consultar": nb,
        "recall_vista_micro": round(nv / na, 4) if na else None,
        "recall_consultada_micro": round(nc / na, 4) if na else None,
        "recall_vista_macro": round(sum(c["recall_vista"] for c in casos) / n, 4),
        "recall_consultada_macro": round(sum(c["recall_consultada"] for c in casos) / n, 4),
    }


def main() -> int:
    agregados = {"definiciones": {
        "recall_micro": "sum(n_vistas|n_consultadas) / sum(n_anclas) sobre los casos de la celda",
        "recall_macro": "promedio simple de los recalls por caso de la celda",
        "brecha_vista_sin_consultar": "anclas vistas en un output pero jamás consultadas (ver_nodo/ver_vecinos)",
        "denominadores": "casos presentes según censo commiteado: v2 44, v3 64, run_3 60; ausencias fuera de la métrica (protocolo §2)",
    }, "por_grafo": {}}

    for grafo, label in LABELS.items():
        res = json.loads((NAV_DIR / f"resultados_navegabilidad_{label}.json")
                         .read_text(encoding="utf-8"))
        casos = res["resultados"]
        censo = json.loads((CENSO_DIR / f"censo_navegabilidad_{grafo}.json")
                           .read_text(encoding="utf-8"))
        g = {
            "label": label,
            "n_casos_evaluados": res["n_casos_evaluados"],
            "replay_ok_todos": res["replay_ok_todos"],
            "replay_fuerte_ok_todos": res["replay_fuerte_ok_todos"],
            "por_variante": {},
            "por_estrato_variante": {},
            "cohorte_nucleo_limpio_EE": {},
            "cohorte_dirigida_EA_ED": {},
            "ausencias": {
                "n_ausentes": censo["n_ausentes"],
                "ids_ausentes": censo["ids_ausentes"],
                "ids_presentes_parciales": censo.get("ids_presentes_parciales", []),
            },
            "anclas_ausentes_por_caso": sorted(
                {c["caso_id"]: c["anclas_ausentes_en_este_grafo"]
                 for c in casos if c["anclas_ausentes_en_este_grafo"]}.items()),
        }
        for v in VARIANTES:
            cv = [c for c in casos if c["variante"] == v]
            g["por_variante"][v] = celda(cv)
            g["cohorte_nucleo_limpio_EE"][v] = celda(
                [c for c in cv if c["estrato"] == "E-E"])
            g["cohorte_dirigida_EA_ED"][v] = celda(
                [c for c in cv if c["estrato"] in DIRIGIDA])
            for e in ESTRATOS:
                g["por_estrato_variante"][f"{e}::{v}"] = celda(
                    [c for c in cv if c["estrato"] == e])
        # brecha central del eje: literal - antilexica (recall consultada micro)
        lit, anti = g["por_variante"]["literal"], g["por_variante"]["antilexica"]
        g["brecha_literal_vs_antilexica"] = {
            "recall_vista_micro": round(lit["recall_vista_micro"] - anti["recall_vista_micro"], 4),
            "recall_consultada_micro": round(lit["recall_consultada_micro"] - anti["recall_consultada_micro"], 4),
            "recall_vista_macro": round(lit["recall_vista_macro"] - anti["recall_vista_macro"], 4),
            "recall_consultada_macro": round(lit["recall_consultada_macro"] - anti["recall_consultada_macro"], 4),
        }
        agregados["por_grafo"][grafo] = g

    out = NAV_DIR / "agregados_navegabilidad.json"
    out.write_text(json.dumps(agregados, ensure_ascii=False, indent=2),
                   encoding="utf-8")
    print(json.dumps(agregados, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
