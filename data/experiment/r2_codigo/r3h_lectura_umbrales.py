"""U-R2-CODIGO, R3.h — cómo muestra el agente la lista de umbrales de un nodo
r2 (L-ESQ-R2 §1.4: NO VERIFICADO hasta esta unidad). Solo lectura, en
memoria, sin Neo4j ni API.

Tres caminos, leídos sin editarlos:
  - harness (cuarteto sellado): loader.load_graph_from_path → GraphIndex;
    `ver_nodo` devuelve `n.properties` tal cual (evaluacion/harness.py:179-190)
    y `buscar_nodos` resume las properties con `_short_props` (:116-129);
  - Neo4j: la carga guarda todas las properties en `props_json`
    (neo4j/cargar_kg.py, `_fila_nodo`) y deja como propiedad del nodo de Neo4j
    solo los valores string, número, booleano o lista de strings (:105-111);
    `Neo4jIndex.ver_nodo` devuelve `json.loads(props_json)`
    (neo4j/neo4j_index.py:206-223). Acá se reproduce en memoria la fila de
    la carga y su lectura;
  - tools_v2 (agente_v2): `ver_nodo_v2` es `Neo4jIndex.ver_nodo` sin cambio
    (agente_v2/tools_v2.py:156-157).

Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/r2_codigo/r3h_lectura_umbrales.py \\
    --kg <kg.json del perfil r2> --nodo <id> --out <json>
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
for p in (REPO / "data" / "experiment" / "evaluacion", REPO / "data" / "experiment" / "neo4j"):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))
import loader  # noqa: E402  (cuarteto sellado: solo import)
import harness  # noqa: E402  (cuarteto sellado: solo import)
import cargar_kg  # noqa: E402  (solo import; no abre conexión)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--kg", required=True)
    ap.add_argument("--nodo", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    kg = loader.load_graph_from_path(a.kg)
    idx = harness.GraphIndex(kg)
    vista_harness = idx.ver_nodo(a.nodo)
    nodo = idx.by_id[a.nodo]
    fila = cargar_kg._fila_nodo(nodo, "prueba_r2")
    vista_neo4j = {"properties": json.loads(fila["props_json"])}
    busqueda = idx.buscar_nodos(nodo.label, 5)
    resumen = next((r for r in busqueda["resultados"] if r["id"] == a.nodo), None)
    umb = (vista_harness.get("properties") or {}).get("umbrales")
    out = {
        "unidad": "U-R2-CODIGO", "etapa": "R3.h", "kg": "/".join(Path(a.kg).parts[-4:]), "nodo": a.nodo,
        "harness_ver_nodo_muestra_la_lista": isinstance(umb, list) and bool(umb),
        "harness_ver_nodo_umbrales": umb,
        "neo4j_props_json_muestra_la_lista": vista_neo4j["properties"].get("umbrales") == umb,
        "neo4j_propiedad_umbrales_en_el_nodo": "umbrales" in fila,
        "neo4j_claves_como_propiedad": sorted(k for k in fila if k not in cargar_kg.PROPS_RESERVADAS),
        "tools_v2_ver_nodo_v2": "Neo4jIndex.ver_nodo sin cambio: igual que neo4j_props_json",
        "buscar_nodos_resumen_propiedades": resumen["resumen_propiedades"] if resumen else None,
        "buscar_nodos_resumen_menciona_la_lista": bool(resumen) and "umbrales" in resumen["resumen_propiedades"],
    }
    Path(a.out).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in out.items() if k != "harness_ver_nodo_umbrales"}, ensure_ascii=False,
                     indent=1))


if __name__ == "__main__":
    main()
