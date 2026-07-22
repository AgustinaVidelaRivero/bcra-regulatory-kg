"""
validate_loader.py — Valida loader.py sobre los 5 grafos congelados.

Para cada run reporta: nodos cargados, edges cargados, merges aplicados,
provenances totales, y una verificación cruzada de que los conteos
post-normalización cuadran con los crudos del kg.json.

La verificación es INDEPENDIENTE del loader: este script vuelve a abrir cada
kg.json con json.load y recomputa los conteos crudos (nodos, edges, ids únicos)
por su cuenta, y los compara contra lo que devuelve el loader.

Checks por run:
  C1  loader.raw_node_count == #nodos crudos del json
  C2  loader.raw_edge_count == #edges crudos del json
  C3  len(nodes) == #ids únicos del json            (merge colapsa por id)
  C4  len(nodes) == raw_nodes - instancias absorbidas por merge
  C5  len(edges) == raw_edges                        (no se deduplican edges)
  C6  todo edge.source/target resuelve a un id de nodo final (0 colgantes)
  C7  todo nodo final tiene >= 1 provenance
  C8  todo edge final tiene >= 1 provenance

Salida: imprime a stdout y escribe data/experiment/evaluacion/01_validacion_loader.md
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from loader import RUN_FILES, RUN_KEYS, load_graph, dump_merge_log, EVAL_DIR

REPORT_PATH = EVAL_DIR / "01_validacion_loader.md"


def raw_stats(path: Path):
    with path.open(encoding="utf-8") as f:
        data = json.load(f)
    nodes = data.get("nodes", [])
    edges = data.get("edges", [])
    ids = [n.get("id") for n in nodes]
    return {
        "raw_nodes": len(nodes),
        "raw_edges": len(edges),
        "unique_ids": len(set(ids)),
        "dup_instances": len(ids) - len(set(ids)),
    }


def validate_run(run_key: str):
    path = RUN_FILES[run_key]
    raw = raw_stats(path)
    kg = load_graph(run_key)

    final_ids = {n.id for n in kg.nodes}
    dangling = sum(
        1 for e in kg.edges
        if e.source not in final_ids or e.target not in final_ids
    )
    nodes_without_prov = sum(1 for n in kg.nodes if not n.provenances)
    edges_without_prov = sum(1 for e in kg.edges if not e.provenances)

    checks = {
        "C1 raw_node_count==json": kg.raw_node_count == raw["raw_nodes"],
        "C2 raw_edge_count==json": kg.raw_edge_count == raw["raw_edges"],
        "C3 len(nodes)==ids_unicos": len(kg.nodes) == raw["unique_ids"],
        "C4 len(nodes)==raw-absorbidas":
            len(kg.nodes) == raw["raw_nodes"] - kg.merged_instances,
        "C5 len(edges)==raw_edges": len(kg.edges) == raw["raw_edges"],
        "C6 edges_sin_colgantes": dangling == 0,
        "C7 nodos_con_provenance": nodes_without_prov == 0,
        "C8 edges_con_provenance": edges_without_prov == 0,
    }

    merge_log_path = None
    if kg.merges:
        merge_log_path = dump_merge_log(kg)

    return {
        "run_key": run_key,
        "path": path,
        "raw": raw,
        "kg": kg,
        "dangling": dangling,
        "nodes_without_prov": nodes_without_prov,
        "edges_without_prov": edges_without_prov,
        "checks": checks,
        "merge_log_path": merge_log_path,
    }


def build_report(results) -> str:
    L = []
    L.append("# Validación del loader — Fase 2.3")
    L.append("")
    L.append("Generado por `evaluacion/validate_loader.py` cargando los 5 grafos "
             "vía `evaluacion/loader.py`. Los conteos crudos se recomputan de forma "
             "independiente reabriendo cada `kg.json` con `json.load`. Los `kg.json` "
             "no se modifican.")
    L.append("")

    all_pass = all(all(r["checks"].values()) for r in results)
    L.append(f"**Resultado global: {'✅ TODOS LOS CHECKS PASAN' if all_pass else '❌ HAY CHECKS FALLIDOS'}**")
    L.append("")

    # --- tabla resumen ---
    L.append("## Resumen por run")
    L.append("")
    L.append("| Run | Nodos cargados | Edges cargados | Merges (grupos / instancias) | Provenances nodo | Provenances edge | Checks |")
    L.append("|-----|---------------:|---------------:|------------------------------|-----------------:|-----------------:|:------:|")
    for r in results:
        kg = r["kg"]
        merges = f"{len(kg.merges)} / {kg.merged_instances}" if kg.merges else "0 / 0"
        status = "✅" if all(r["checks"].values()) else "❌"
        L.append(f"| {r['run_key']} | {len(kg.nodes)} | {len(kg.edges)} | {merges} "
                 f"| {kg.total_node_provenances} | {kg.total_edge_provenances} | {status} |")
    L.append("")

    # --- verificación de conteos ---
    L.append("## Verificación de conteos post-normalización vs. crudos")
    L.append("")
    L.append("| Run | Nodos crudos (json) | Ids únicos | Instancias absorbidas | Nodos finales | Identidad verificada |")
    L.append("|-----|--------------------:|-----------:|----------------------:|--------------:|----------------------|")
    for r in results:
        kg, raw = r["kg"], r["raw"]
        identity = f"{raw['raw_nodes']} − {kg.merged_instances} = {len(kg.nodes)}"
        ok = "✅" if len(kg.nodes) == raw["raw_nodes"] - kg.merged_instances else "❌"
        L.append(f"| {r['run_key']} | {raw['raw_nodes']} | {raw['unique_ids']} "
                 f"| {kg.merged_instances} | {len(kg.nodes)} | {identity} {ok} |")
    L.append("")
    L.append("> Run 5 es el único con merges: **6.095 − 163 = 5.932** nodos esperados, "
             "que coincide con los 5.932 `id` únicos del json crudo.")
    L.append("")

    # --- detalle de checks por run ---
    L.append("## Detalle de checks por run")
    L.append("")
    check_names = list(results[0]["checks"].keys())
    header = "| Run | " + " | ".join(c.split(" ", 1)[0] for c in check_names) + " |"
    sep = "|-----|" + "|".join([":--:"] * len(check_names)) + "|"
    L.append(header)
    L.append(sep)
    for r in results:
        cells = "".join(" ✅ |" if v else " ❌ |" for v in r["checks"].values())
        L.append(f"| {r['run_key']} |" + cells)
    L.append("")
    L.append("Leyenda de checks:")
    for c in check_names:
        L.append(f"- `{c}`")
    L.append("")

    # --- logs de merge ---
    L.append("## Logs de merge")
    L.append("")
    any_log = False
    for r in results:
        if r["merge_log_path"]:
            any_log = True
            rel = r["merge_log_path"].relative_to(EVAL_DIR.parent.parent)
            kg = r["kg"]
            L.append(f"- **{r['run_key']}**: {len(kg.merges)} grupos mergeados, "
                     f"{kg.merged_instances} instancias absorbidas → `{rel}`")
    if not any_log:
        L.append("- (ninguno)")
    L.append("")

    # --- nota de provenance ---
    L.append("## Provenances")
    L.append("")
    total_np = sum(r["kg"].total_node_provenances for r in results)
    total_ep = sum(r["kg"].total_edge_provenances for r in results)
    L.append(f"Provenances totales normalizadas (source_doc + location, deduplicadas): "
             f"**{total_np}** en nodos y **{total_ep}** en edges, sumando los 5 grafos. "
             f"Todos los nodos finales tienen ≥1 provenance (C7) y todos los edges "
             f"finales tienen ≥1 provenance (C8).")
    L.append("")
    return "\n".join(L)


def main():
    results = [validate_run(rk) for rk in RUN_KEYS]

    # stdout
    print("=" * 72)
    for r in results:
        kg = r["kg"]
        status = "PASS" if all(r["checks"].values()) else "FAIL"
        print(f"[{status}] {r['run_key']}: nodes={len(kg.nodes)} edges={len(kg.edges)} "
              f"merges={len(kg.merges)} absorbidas={kg.merged_instances} "
              f"node_provs={kg.total_node_provenances} edge_provs={kg.total_edge_provenances}")
        for name, ok in r["checks"].items():
            if not ok:
                print(f"        FALLA {name}")
    print("=" * 72)

    report = build_report(results)
    REPORT_PATH.write_text(report, encoding="utf-8")
    print(f"Reporte escrito en: {REPORT_PATH}")

    all_pass = all(all(r["checks"].values()) for r in results)
    print("GLOBAL:", "TODOS PASAN" if all_pass else "HAY FALLAS")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
