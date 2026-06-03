"""
Visualización pyvis del kg.json del Run 5 — Híbrido core + emergente.

- Colores por tipo: los 4 core con paleta saturada, emergentes con paleta atenuada
  y misma familia cromática que el tipo core con el que más se relacionan
  (heurística simple — mejora visual, no afecta el grafo).
- Labels de nodo cortos (label canónico); description y categoria en tooltip.
- Edges con label del predicado, tooltip con provenance.
- Layout barnes-hut (default pyvis), tamaño nodo proporcional al log de su grado.
"""

from __future__ import annotations

import json
import math
from collections import Counter
from pathlib import Path

from pyvis.network import Network

RUN_DIR = Path(__file__).resolve().parent.parent
KG_PATH = RUN_DIR / "kg.json"
OUT_PATH = RUN_DIR / "kg_visual.html"

# Colores: los 4 core fuertes, emergentes en gris atenuado.
TYPE_COLORS = {
    "EntidadFinanciera": "#1f77b4",  # azul
    "Operacion": "#2ca02c",          # verde
    "Restriccion": "#d62728",        # rojo
    "Excepcion": "#ff7f0e",          # naranja
    # Emergentes — paleta gris / pastel.
    "Concepto": "#9467bd",           # púrpura
    "Documento": "#8c564b",          # marrón
    "Autoridad": "#e377c2",          # rosa
    "Plazo": "#7f7f7f",              # gris
    "InstrumentoFinanciero": "#bcbd22",  # oliva
    "Sancion": "#17becf",            # cian
    "RegimenInformativo": "#aec7e8",  # azul claro
    "Norma": "#ffbb78",              # naranja claro
    "Moneda": "#98df8a",             # verde claro
}
DEFAULT_COLOR = "#cccccc"


def _color_for(type_: str) -> str:
    return TYPE_COLORS.get(type_, DEFAULT_COLOR)


def _node_title(n: dict) -> str:
    """HTML para el tooltip del nodo (al hover)."""
    parts = [
        f"<b>{n['label']}</b>",
        f"<i>type:</i> {n['type']}",
    ]
    props = n.get("properties") or {}
    if props.get("categoria"):
        parts.append(f"<i>categoria:</i> {props['categoria']}")
    if props.get("description"):
        desc = props["description"]
        if len(desc) > 250:
            desc = desc[:250] + "..."
        parts.append(f"<i>desc:</i> {desc}")
    prov = n.get("provenance") or {}
    if prov.get("source_doc"):
        parts.append(f"<i>doc:</i> {prov['source_doc']}")
    if prov.get("location"):
        parts.append(f"<i>loc:</i> {prov['location']}")
    return "<br>".join(parts)


def _edge_title(e: dict) -> str:
    parts = [f"<b>{e['relation']}</b>"]
    prov = e.get("provenance") or {}
    if prov.get("source_doc"):
        parts.append(f"<i>doc:</i> {prov['source_doc']}")
    if prov.get("location"):
        parts.append(f"<i>loc:</i> {prov['location']}")
    return "<br>".join(parts)


def build(kg: dict, out_path: Path) -> None:
    nodes = kg["nodes"]
    edges = kg["edges"]

    # Grado para sizing
    degree: Counter = Counter()
    for e in edges:
        degree[e["source"]] += 1
        degree[e["target"]] += 1

    net = Network(
        height="900px",
        width="100%",
        bgcolor="#fafafa",
        font_color="#222222",
        directed=True,
        notebook=False,
        cdn_resources="remote",
    )
    # Layout: barnes-hut, parámetros un poco más relajados para grafos grandes.
    net.barnes_hut(
        gravity=-12000,
        central_gravity=0.2,
        spring_length=180,
        spring_strength=0.04,
        damping=0.4,
        overlap=0.0,
    )

    for n in nodes:
        size = 10 + 4 * math.log1p(degree.get(n["id"], 0))
        net.add_node(
            n["id"],
            label=n["label"],
            title=_node_title(n),
            color=_color_for(n["type"]),
            size=size,
            shape="dot",
        )

    for e in edges:
        net.add_edge(
            e["source"],
            e["target"],
            label=e["relation"],
            title=_edge_title(e),
            arrows="to",
            color={"color": "#888888", "opacity": 0.6},
            font={"size": 8, "color": "#444444", "align": "middle"},
            smooth={"type": "continuous"},
        )

    # Set options that pyvis exposes via set_options (físicas adicionales).
    net.set_options(
        """
        var options = {
          "physics": {
            "stabilization": {"iterations": 200, "updateInterval": 25},
            "minVelocity": 0.5
          },
          "interaction": {
            "hover": true,
            "tooltipDelay": 100,
            "navigationButtons": true,
            "keyboard": {"enabled": true}
          }
        }
        """
    )
    net.write_html(str(out_path), notebook=False, open_browser=False)


def main() -> None:
    if not KG_PATH.exists():
        raise SystemExit(f"kg.json no existe en {KG_PATH}. Corré assemble.py primero.")
    kg = json.loads(KG_PATH.read_text(encoding="utf-8"))
    print(f"[load] {len(kg['nodes'])} nodos, {len(kg['edges'])} edges")
    build(kg, OUT_PATH)
    print(f"[write] {OUT_PATH}")
    print(f"  → abrí el archivo en el navegador para ver el grafo")


if __name__ == "__main__":
    main()
