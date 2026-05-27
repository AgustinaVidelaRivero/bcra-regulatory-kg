"""
visualize.py — Genera kg_visual.html con pyvis.

Estrategia:
- Render del grafo entero si tiene ≤ 600 nodos.
- Si es más grande, render del subgrafo de los TOP-N nodos por grado
  más sus vecinos directos (para legibilidad).
- Cada tipo de nodo tiene color propio. Tooltip con label, tipo,
  versión y provenance principal.
"""

from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

from pyvis.network import Network


COLOR_BY_TYPE = {
    "SujetoRegulado":         "#1f77b4",  # azul
    "OrganismoRegulador":     "#17becf",  # cyan
    "Obligacion":             "#d62728",  # rojo
    "Operacion":              "#ff7f0e",  # naranja
    "ConceptoDefinido":       "#9467bd",  # violeta
    "Requisito":              "#bcbd22",  # oliva
    "Umbral":                 "#e377c2",  # rosa
    "Plazo":                  "#7f7f7f",  # gris
    "Procedimiento":          "#2ca02c",  # verde
    "Sancion":                "#8c564b",  # marrón
    "InstrumentoFinanciero":  "#aec7e8",  # azul claro
    "NormaReferenciada":      "#c49c94",  # marrón claro
}


def _select_subgraph(nodes, edges, top_n: int = 250):
    """Top-N nodos por grado + vecinos directos."""
    deg = Counter()
    for e in edges:
        deg[e["source"]] += 1
        deg[e["target"]] += 1
    top_ids = set(nid for nid, _ in deg.most_common(top_n))
    # vecinos directos
    keep_ids = set(top_ids)
    for e in edges:
        if e["source"] in top_ids or e["target"] in top_ids:
            keep_ids.add(e["source"])
            keep_ids.add(e["target"])
    kept_nodes = [n for n in nodes if n["id"] in keep_ids]
    kept_edges = [e for e in edges if e["source"] in keep_ids and e["target"] in keep_ids]
    return kept_nodes, kept_edges


def render(kg: dict, out_path: Path, max_nodes_full: int = 600, top_n_subgraph: int = 250):
    nodes = kg["nodes"]
    edges = kg["edges"]
    truncated = False
    if len(nodes) > max_nodes_full:
        nodes, edges = _select_subgraph(nodes, edges, top_n=top_n_subgraph)
        truncated = True

    net = Network(
        height="900px", width="100%", bgcolor="#ffffff", font_color="#222222",
        directed=True, notebook=False, cdn_resources="remote",
    )
    net.barnes_hut(
        gravity=-12000, central_gravity=0.25,
        spring_length=140, spring_strength=0.02, damping=0.35, overlap=0.1,
    )
    net.set_options("""
    var options = {
      "interaction": {"hover": true, "tooltipDelay": 80, "navigationButtons": true},
      "edges": {"arrows": {"to": {"enabled": true, "scaleFactor": 0.6}},
                "smooth": {"type": "dynamic"}, "color": {"inherit": false, "color": "#888"}},
      "nodes": {"shape": "dot", "scaling": {"min": 6, "max": 32}}
    }
    """)

    deg = Counter()
    for e in edges:
        deg[e["source"]] += 1
        deg[e["target"]] += 1

    for n in nodes:
        color = COLOR_BY_TYPE.get(n["type"], "#cccccc")
        props = n.get("properties", {}) or {}
        prov = n.get("provenance", {}) or {}
        tt_lines = [
            f"<b>{n['label']}</b>",
            f"<i>{n['type']}</i>",
            f"version: {props.get('version','')}",
        ]
        if props.get("modalidad"):
            tt_lines.append(f"modalidad: {props['modalidad']}")
        if props.get("valor"):
            tt_lines.append(f"valor: {props['valor']} {props.get('unidad','')}")
        if props.get("duracion"):
            tt_lines.append(f"duración: {props['duracion']} {props.get('unidad','')}")
        if props.get("description"):
            desc_raw = props["description"]
            # description puede ser str o list (resultado del dedup de nodos).
            if isinstance(desc_raw, list):
                desc_str = " | ".join(str(d) for d in desc_raw if d)
            else:
                desc_str = str(desc_raw)
            desc = desc_str[:300].replace("<", "&lt;").replace(">", "&gt;")
            tt_lines.append(f"<br>{desc}")
        tt_lines.append(f"<br><small>{prov.get('source_doc','')}<br>{prov.get('location','')}</small>")
        net.add_node(
            n["id"],
            label=n["label"][:50],
            title="<br>".join(tt_lines),
            color=color,
            value=max(1, deg.get(n["id"], 1)),
            group=n["type"],
        )

    for e in edges:
        net.add_edge(e["source"], e["target"], title=e["relation"], label=e["relation"])

    out_path.parent.mkdir(parents=True, exist_ok=True)
    html = net.generate_html()

    # Inyectar leyenda y banner
    legend_items = "".join(
        f'<span style="margin-right:12px;"><span style="display:inline-block;width:10px;height:10px;background:{c};border-radius:50%;margin-right:4px;vertical-align:middle;"></span>{t}</span>'
        for t, c in COLOR_BY_TYPE.items()
    )
    banner = ""
    if truncated:
        banner = (
            '<div style="background:#fff8d7;padding:8px;border:1px solid #e8d36b;'
            'border-radius:6px;margin:8px 16px;font-family:sans-serif;font-size:13px;">'
            f'Vista reducida: top-{top_n_subgraph} nodos por grado + vecinos directos (de {len(kg["nodes"])} totales).</div>'
        )
    legend_div = (
        '<div style="padding:8px 16px;font-family:sans-serif;font-size:13px;'
        'border-bottom:1px solid #eee;background:#fafafa;">'
        f'<b>Run 2 — Papers del estado del arte</b> · '
        f'{len(kg["nodes"])} nodos / {len(kg["edges"])} edges<br>'
        f'<span style="display:inline-block;margin-top:6px;">{legend_items}</span>'
        '</div>'
    )
    html = html.replace("<body>", "<body>" + legend_div + banner)
    out_path.write_text(html)


if __name__ == "__main__":
    kg_path = Path(sys.argv[1])
    out = Path(sys.argv[2])
    kg = json.loads(kg_path.read_text())
    render(kg, out)
    print(f"wrote {out}")
