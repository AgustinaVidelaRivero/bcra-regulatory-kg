#!/usr/bin/env python3
"""control_neo4j_propio.py — El Neo4j de NEO4J_URI responde y su KG_Meta da el sha256 del grafo de N6 (el acumulado de las
tandas 0 y 1 sin cola, el `kg_sha256_esperado` de mcp_kg/config_mcp_kg_nav_acumulado.json). Lo corren el humo pago, antes
de leer la clave o lanzar nada, y el test de aislamiento, antes y después (con --huella, la huella de estado y de contenido
de cargar_kg.huella_neo4j, para declarar la base compartida de solo lectura).

Imprime la dirección (NEO4J_URI, que no es una credencial: registro de decisiones, §88), el sha256 de KG_Meta y las
cuentas; el usuario y la contraseña son los de conexion.py y no se imprimen. Código 10 si no responde o no da el sha256.
Uso: NEO4J_URI=bolt://127.0.0.1:37687 control_neo4j_propio.py [--huella]
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BANCO_DIR = AQUI.parent
NEO4J_DIR = BANCO_DIR.parent / "neo4j"
if str(NEO4J_DIR) not in sys.path:
    sys.path.insert(0, str(NEO4J_DIR))
CONFIG_GRAFO = BANCO_DIR / "mcp_kg" / "config_mcp_kg_nav_acumulado.json"
NO_RESPONDE = 10


def estado(con_huella: bool = False) -> dict:
    cfg = json.loads(CONFIG_GRAFO.read_text(encoding="utf-8"))
    uri = os.environ.get("NEO4J_URI")
    out = {"NEO4J_URI": uri, "grafo": cfg["grafo"], "kg_sha256_esperado": cfg["kg_sha256_esperado"]}
    if not uri:
        return out | {"ok": False, "motivo": "NEO4J_URI no está en el entorno"}
    import cargar_kg as CK                      # noqa: PLC0415  (data/experiment/neo4j)
    from conexion import abrir_driver           # noqa: PLC0415
    try:
        driver = abrir_driver()
        driver.verify_connectivity()
    except Exception as e:                       # solo el tipo: el mensaje no se imprime
        return out | {"ok": False, "motivo": f"no responde ({type(e).__name__})"}
    try:
        meta = CK.leer_meta(driver, cfg["grafo"]) or {}
        out["kg_meta_sha256"] = meta.get("kg_sha256")
        if con_huella:
            h = CK.huella_neo4j(driver, cfg["grafo"])
            out |= {"n_nodos": h["n_nodos"], "n_aristas": h["n_aristas"], "huella_estado": h["estado"],
                    "huella_contenido": h["contenido"]}
        else:
            from grafos import GRAFOS                # noqa: PLC0415
            label = GRAFOS[cfg["grafo"]]["label"]
            with driver.session() as s:
                out["n_nodos"] = s.run(f"MATCH (n:`{label}`) RETURN count(n) AS c").single()["c"]
    finally:
        driver.close()
    out["ok"] = out.get("kg_meta_sha256") == cfg["kg_sha256_esperado"]
    if not out["ok"]:
        out["motivo"] = "KG_Meta no da el sha256 del acumulado"
    return out


def main(argv: list[str]) -> int:
    e = estado("--huella" in argv)
    print(json.dumps(e, ensure_ascii=False))
    if not e["ok"]:
        print(f"FRENO (USD 0): {e['motivo']}")
        return NO_RESPONDE
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
