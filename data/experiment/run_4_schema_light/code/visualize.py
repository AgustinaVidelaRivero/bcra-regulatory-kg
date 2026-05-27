"""
Visualización del KG con pyvis.

Decisión (acordada con la autora): top 400 nodos por grado total (in+out).
Los edges entre esos 400 se preservan; los edges hacia/desde nodos fuera del top
se descartan en la viz (no se modifica kg.json).

Colores por tipo canónico (top N tipos visibles).
"""

import json
import random
from collections import Counter
from pathlib import Path

import networkx as nx
from pyvis.network import Network

KG_PATH = Path(__file__).resolve().parents[1] / "kg.json"
HTML_PATH = Path(__file__).resolve().parents[1] / "kg_visual.html"

TOP_N = 400
COLOR_PALETTE = [
    "#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
    "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf",
    "#3366cc", "#dc3912", "#ff9900", "#109618", "#990099",
    "#0099c6", "#dd4477", "#66aa00", "#b82e2e", "#316395",
]
NEUTRAL_COLOR = "#cccccc"


def main():
    kg = json.loads(KG_PATH.read_text())
    print(f"[viz] kg loaded: {len(kg['nodes'])} nodes, {len(kg['edges'])} edges")

    # Build networkx graph to compute degrees
    G = nx.DiGraph()
    for n in kg["nodes"]:
        G.add_node(n["id"], **n)
    for e in kg["edges"]:
        G.add_edge(e["source"], e["target"], relation=e["relation"])

    # Top 400 by total degree (in + out)
    degrees = dict(G.degree())  # for DiGraph this is in+out
    top_ids = [nid for nid, _ in sorted(degrees.items(), key=lambda kv: -kv[1])[:TOP_N]]
    top_set = set(top_ids)
    print(f"[viz] top {TOP_N} nodes by total degree, deg range [{degrees[top_ids[-1]]}..{degrees[top_ids[0]]}]")

    # Sub-graph induced by top 400
    sub_nodes = [n for n in kg["nodes"] if n["id"] in top_set]
    sub_edges = [e for e in kg["edges"] if e["source"] in top_set and e["target"] in top_set]
    print(f"[viz] subgraph: {len(sub_nodes)} nodes, {len(sub_edges)} edges")

    # Colors: top 19 types get unique color, rest neutral
    type_counts = Counter(n["type"] for n in sub_nodes)
    top_types = [t for t, _ in type_counts.most_common(len(COLOR_PALETTE))]
    type_to_color = {t: COLOR_PALETTE[i] for i, t in enumerate(top_types)}

    # Build pyvis network
    net = Network(
        height="900px", width="100%",
        bgcolor="#0f1117", font_color="#e6e6e6",
        directed=True, notebook=False,
        cdn_resources="in_line",
    )
    net.barnes_hut(gravity=-3500, spring_length=120, spring_strength=0.02)

    for n in sub_nodes:
        deg = degrees[n["id"]]
        type_canon = n["type"]
        color = type_to_color.get(type_canon, NEUTRAL_COLOR)
        # type_raw como lista (si hay más de 1, mostrar todos para hacer visible la inconsistencia léxica)
        type_raw_list = n["properties"].get("type_raw", [])
        type_raw_str = " | ".join(type_raw_list)
        descr = n["properties"].get("description", "")
        if len(descr) > 200:
            descr = descr[:200] + "..."
        prov = n.get("provenance", {})
        title = (
            f"<b>{n['label']}</b><br>"
            f"<i>type canon:</i> {type_canon}<br>"
            f"<i>type_raw observados:</i> {type_raw_str}<br>"
            f"<i>degree:</i> {deg}<br>"
            f"<i>provenance:</i> {prov.get('source_doc','')} {prov.get('location','')}<br>"
            f"<i>description:</i> {descr}"
        )
        net.add_node(
            n["id"],
            label=n["label"][:40] + ("…" if len(n["label"]) > 40 else ""),
            title=title,
            color=color,
            size=10 + min(40, deg),
        )

    for e in sub_edges:
        net.add_edge(
            e["source"], e["target"],
            title=e["relation"],
            label=e["relation"][:25] + ("…" if len(e["relation"]) > 25 else ""),
            arrows="to",
            color={"color": "#666666", "opacity": 0.4},
            font={"size": 8, "color": "#aaaaaa"},
        )

    net.set_options("""
    {
        "physics": {
            "enabled": true,
            "barnesHut": {
                "gravitationalConstant": -3500,
                "centralGravity": 0.3,
                "springLength": 120,
                "springConstant": 0.02,
                "damping": 0.4
            },
            "stabilization": {"iterations": 200}
        },
        "interaction": {"hover": true, "tooltipDelay": 200}
    }
    """)

    # Write directly (without browser preview)
    html = net.generate_html()
    # Inject a small legend
    legend_lines = ["<div style='position:fixed;top:10px;left:10px;background:#1a1d24;padding:10px;border:1px solid #444;color:#eee;font:12px sans-serif;max-height:80vh;overflow-y:auto;'>"]
    legend_lines.append(f"<b>Run 4 — Schema-light puro</b><br>Top {TOP_N} nodos por grado<br>{len(sub_nodes)} nodos · {len(sub_edges)} edges<hr>")
    legend_lines.append("<b>Tipo canónico (top 20):</b><br>")
    for t in top_types:
        col = type_to_color[t]
        n_t = type_counts[t]
        legend_lines.append(f"<span style='display:inline-block;width:10px;height:10px;background:{col};margin-right:5px;border-radius:50%;'></span>{t} ({n_t})<br>")
    legend_lines.append(f"<span style='display:inline-block;width:10px;height:10px;background:{NEUTRAL_COLOR};margin-right:5px;border-radius:50%;'></span>otros tipos<br>")
    legend_lines.append("</div>")
    legend = "\n".join(legend_lines)
    html = html.replace("<body>", "<body>\n" + legend, 1)

    HTML_PATH.write_text(html, encoding="utf-8")
    print(f"[viz] → {HTML_PATH}  ({HTML_PATH.stat().st_size/1024/1024:.2f} MB)")


if __name__ == "__main__":
    main()
