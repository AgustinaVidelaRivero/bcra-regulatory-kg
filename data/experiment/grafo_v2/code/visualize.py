"""Visualización pyvis del kg.json — un color por tipo de entidad.

Uso:
    python visualize.py            # lee kg.json del run, escribe kg_visual.html
    python visualize.py smoke      # versión smoke (kg_smoke.json → kg_visual_smoke.html)
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from pyvis.network import Network


RUN_DIR = Path(__file__).resolve().parents[1]


TYPE_COLOR = {
    "Comunicacion":       "#9b59b6",  # púrpura
    "TextoOrdenado":      "#34495e",  # azul oscuro
    "EntidadFinanciera":  "#3498db",  # azul claro
    "Operacion":          "#1abc9c",  # turquesa
    "Restriccion":        "#e74c3c",  # rojo
    "Excepcion":          "#f39c12",  # naranja
    "Obligacion":         "#27ae60",  # verde
}


def build_network(kg: dict, title: str) -> Network:
    # No pasamos `heading` — pyvis 0.3.2 lo duplica en el HTML generado.
    # El título lo inyectamos manualmente en `write_with_title` abajo.
    net = Network(
        height="850px",
        width="100%",
        bgcolor="#fafafa",
        font_color="#222",
        directed=True,
        notebook=False,
    )
    net.barnes_hut(
        gravity=-3500,
        central_gravity=0.15,
        spring_length=120,
        spring_strength=0.02,
        damping=0.4,
    )

    for n in kg["nodes"]:
        color = TYPE_COLOR.get(n["type"], "#7f8c8d")
        props_lines = [f"{k}: {v}" for k, v in n.get("properties", {}).items()]
        prov = n.get("provenance", {})
        prov_lines = [f"source_doc: {prov.get('source_doc','')}", f"location: {prov.get('location','')}"]
        title_html = (
            f"<b>{n['label']}</b><br/>"
            f"<i>{n['type']}</i><br/>"
            + "<br/>".join(props_lines)
            + "<br/>—<br/>"
            + "<br/>".join(prov_lines)
        )
        net.add_node(
            n["id"],
            label=n["label"][:60],
            title=title_html,
            color=color,
            shape="dot",
            size=18 if n["type"] in ("TextoOrdenado", "EntidadFinanciera") else 12,
        )

    for ed in kg["edges"]:
        prov = ed.get("provenance", {})
        title_html = (
            f"<b>{ed['relation']}</b><br/>"
            f"source_doc: {prov.get('source_doc','')}<br/>"
            f"location: {prov.get('location','')}"
        )
        net.add_edge(
            ed["source"],
            ed["target"],
            title=title_html,
            label=ed["relation"],
            arrows="to",
        )

    net.set_options("""
    var options = {
      "edges": {
        "smooth": {"type": "continuous"},
        "font": {"size": 9, "align": "middle"},
        "color": {"color": "#999"},
        "width": 1
      },
      "nodes": {
        "font": {"size": 11}
      },
      "physics": {
        "stabilization": {"iterations": 300}
      }
    }
    """)
    return net


def main() -> int:
    if len(sys.argv) > 1 and sys.argv[1] == "smoke":
        kg_path = RUN_DIR / "code" / "cache" / "kg_smoke.json"
        out = RUN_DIR / "code" / "cache" / "kg_visual_smoke.html"
        title = "Run 3 — 7 entidades core PPF (smoke)"
    else:
        kg_path = RUN_DIR / "kg.json"
        out = RUN_DIR / "kg_visual.html"
        title = "Run 3 — 7 entidades core PPF"

    if not kg_path.exists():
        print(f"No existe {kg_path}", file=sys.stderr)
        return 1

    kg = json.loads(kg_path.read_text(encoding="utf-8"))
    print(f"Cargando {kg_path}: {len(kg['nodes'])} nodos, {len(kg['edges'])} edges", flush=True)
    net = build_network(kg, title)
    out.parent.mkdir(parents=True, exist_ok=True)
    net.write_html(str(out), notebook=False, open_browser=False)

    # Limpiar los <h1></h1> vacíos que pyvis 0.3.2 inserta siempre en su template,
    # luego inyectar UN solo título.
    import re as _re
    html = out.read_text(encoding="utf-8")
    # Quitar bloques <center>\n<h1></h1>\n</center> y similares
    html = _re.sub(r"<center>\s*<h1>\s*</h1>\s*</center>", "", html)
    html = _re.sub(r"<h1>\s*</h1>", "", html)
    heading_block = f"<center><h1>{title}</h1></center>\n"
    if "<body>" in html:
        html = html.replace("<body>", "<body>\n" + heading_block, 1)
    out.write_text(html, encoding="utf-8")

    print(f"Escrito {out}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
