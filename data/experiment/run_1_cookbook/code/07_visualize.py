"""
07_visualize.py — Etapa fuera-del-cookbook: visualización interactiva del KG.

Toma kg.json y genera kg_visual.html con pyvis (force-directed, nodos
coloreados por type, hover con metadata, edges con label de predicate).

NO usa la API. Sin costo. Local.

Output: ../kg_visual.html
"""

from __future__ import annotations

import argparse
import html
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from common import (
    ENTITY_TYPES,
    KG_JSON_PATH,
    RUN_DIR,
    read_json,
)

VISUAL_PATH = RUN_DIR / "kg_visual.html"

# 10 colores categóricos distinguibles (paleta "Tableau 10" + extra).
# Asignación estable por orden de ENTITY_TYPES.
COLOR_BY_TYPE: dict[str, str] = {
    "REGULATED_SUBJECT": "#4e79a7",   # azul
    "REGULATOR":         "#e15759",   # rojo
    "OPERATION":         "#f28e2c",   # naranja
    "REQUIREMENT":       "#76b7b2",   # turquesa
    "CONCEPT":           "#59a14f",   # verde
    "INSTRUMENT":        "#edc949",   # amarillo
    "CLASSIFICATION":    "#af7aa1",   # violeta
    "PROCESS":           "#ff9da7",   # rosa
    "SANCTION":          "#9c755f",   # marrón
    "REPORT_ITEM":       "#bab0ab",   # gris
}


def build_hover_html(node: dict) -> str:
    """HTML para el title del nodo (tooltip de pyvis acepta HTML)."""
    props = node.get("properties", {}) or {}
    prov = node.get("provenance", {}) or {}
    desc = props.get("description", "") or ""
    if len(desc) > 350:
        desc = desc[:347] + "…"
    lines = [
        f"<b>{html.escape(node['label'])}</b>",
        f"<i>type:</i> {html.escape(node['type'])}",
        f"<i>id:</i> <code>{html.escape(node['id'])}</code>",
        f"<i>version:</i> {html.escape(props.get('version', 'N/A'))}",
        f"<i>source_doc:</i> {html.escape(prov.get('source_doc', 'N/A'))}",
        f"<i>location:</i> {html.escape(prov.get('location', 'N/A'))}",
    ]
    if desc:
        lines.append(f"<i>description:</i> {html.escape(desc)}")
    if props.get("mention_count"):
        lines.append(f"<i>mentions:</i> {props['mention_count']}")
    if props.get("aliases"):
        aliases = props["aliases"]
        if len(aliases) > 1:
            ali_str = ", ".join(aliases[:5]) + ("…" if len(aliases) > 5 else "")
            lines.append(f"<i>aliases:</i> {html.escape(ali_str)}")
    return "<br/>".join(lines)


def render(kg: dict, out_path: Path) -> None:
    """Construye el HTML usando pyvis. Lazy-import pyvis para no romper si no está instalado."""
    try:
        from pyvis.network import Network
    except ImportError as e:
        raise SystemExit(
            "pyvis no está instalado. Corré: pip install -r requirements.txt"
        ) from e

    net = Network(
        height="900px",
        width="100%",
        directed=True,
        notebook=False,
        cdn_resources="in_line",
        bgcolor="#ffffff",
        font_color="#222222",
    )

    # Force-directed layout
    net.barnes_hut(
        gravity=-15000,
        central_gravity=0.3,
        spring_length=120,
        spring_strength=0.04,
        damping=0.09,
    )

    # Nodos
    for n in kg["nodes"]:
        etype = n["type"]
        color = COLOR_BY_TYPE.get(etype, "#cccccc")
        size = 10 + 2 * min(40, int(n.get("properties", {}).get("mention_count", 1)))
        net.add_node(
            n["id"],
            label=n["label"],
            title=build_hover_html(n),
            color=color,
            size=size,
            shape="dot",
        )

    # Edges
    for e in kg["edges"]:
        net.add_edge(
            e["source"],
            e["target"],
            label=e["relation"],
            title=html.escape(
                f"{e['relation']} · {e.get('provenance', {}).get('source_doc', '')} "
                f"· {e.get('provenance', {}).get('location', '')}"
            ),
            arrows="to",
        )

    # Opciones extra (UI): filtros por type via legend si el grafo es chico
    # pyvis no expone leyenda nativa; agregamos un nodo-"leyenda" decorativo
    # SOLO si el usuario lo pide con --legend, para no contaminar el grafo.
    # (default: no legend)

    # Render
    # pyvis.write_html() en versiones recientes acepta open_browser=False.
    try:
        net.write_html(str(out_path), open_browser=False, notebook=False)
    except TypeError:
        # Compatibilidad con versiones más viejas de pyvis
        net.show(str(out_path), notebook=False)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Etapa 7: visualización pyvis del KG.")
    parser.add_argument(
        "--out",
        type=str,
        default=str(VISUAL_PATH),
        help=f"Path del HTML de salida (default: {VISUAL_PATH}).",
    )
    args = parser.parse_args(argv)

    if not KG_JSON_PATH.exists():
        print(f"[07_visualize] Falta {KG_JSON_PATH}. Corré 04_assemble.py primero.")
        return 1

    kg = read_json(KG_JSON_PATH)
    out_path = Path(args.out)
    render(kg, out_path)
    print(
        f"[07_visualize] OK · nodes={len(kg['nodes'])} edges={len(kg['edges'])} "
        f"→ {out_path}"
    )
    print("[07_visualize] Leyenda de colores:")
    for t in ENTITY_TYPES:
        print(f"  {COLOR_BY_TYPE[t]:8s} {t}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
