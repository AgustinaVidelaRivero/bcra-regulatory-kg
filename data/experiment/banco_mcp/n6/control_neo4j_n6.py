#!/usr/bin/env python3
"""control_neo4j_n6.py — N6 de U-NAV-DISENO: el Neo4j de NEO4J_URI es el propio de N6 y trae el grafo de N6 cargado por el
cargador de N5 (cargar_neo4j_tanda0.py), con la huella de estado de su carga, y el Navegador de HEAD (familias_nav.Navegador)
arranca sobre él con el índice por punto y los hubs de mcp_kg/config_mcp_kg_nav_acumulado.json (38, 216 y 223866c9…).

  · NEO4J_URI tiene que ser la del Neo4j propio de N6 (bolt://127.0.0.1:57687, neo4j/docker-compose.n6.yml): así ningún
    control ni ninguna sesión de N6 toca el contenedor del repo (7687) ni el de otro proyecto;
  · KG_Meta y la huella de estado y de contenido: paralelo/control_neo4j_propio.estado(con_huella=True), sin editarlo,
    contra las huellas de la carga del paso 0 de N6 (HUELLAS_CARGA);
  · el Navegador: el de HEAD, sin el denso (que no cambia los hubs), con la carpeta del índice, el sha256 del manifiesto y
    los hubs esperados de la config; si algo no da, el Navegador aborta.
Imprime solo la dirección, los sha256 y las cuentas (el usuario y la contraseña son los de conexion.py). Código 10 si algo no da.
Uso: NEO4J_URI=bolt://127.0.0.1:57687 python -B control_neo4j_n6.py
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BANCO_DIR = AQUI.parent
for _p in (str(BANCO_DIR), str(BANCO_DIR / "paralelo"), str(BANCO_DIR / "mcp_kg"), str(BANCO_DIR.parent / "neo4j")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import control_neo4j_propio as CNP              # noqa: E402  (HEAD: solo import)

NEO4J_URI_N6 = "bolt://127.0.0.1:57687"
CONFIG_GRAFO = BANCO_DIR / "mcp_kg" / "config_mcp_kg_nav_acumulado.json"
# Las huellas de las dos cargas del paso 0 de N6 (cargar_neo4j_tanda0.py, --grafo KG_Acumulado_Tandas0y1_r2b_sincola):
# iguales en las dos cargas, y la de contenido igual a la del cargador.
HUELLAS_CARGA = {"huella_estado": "25594502d016e1bbd817b4f36f270682597c149c22b405e0ec9de3ade28d21fa",
                 "huella_contenido": "a207d7fbbdca7de0702b484769814738dff31d7c89503440b3f3b598dd02b380",
                 "n_nodos": 20833, "n_aristas": 55358}
NO_DA = 10


def uri_de_n6() -> str:
    uri = os.environ.get("NEO4J_URI", "")
    if uri != NEO4J_URI_N6:
        raise SystemExit(f"FRENO (USD 0): NEO4J_URI es {uri!r}, no la del Neo4j propio de N6 ({NEO4J_URI_N6})")
    return uri


def estado() -> dict:
    uri_de_n6()
    e = CNP.estado(con_huella=True)
    e["huellas_de_la_carga"] = all(e.get(k) == v for k, v in HUELLAS_CARGA.items())
    if not e["ok"] or not e["huellas_de_la_carga"]:
        return e | {"ok": False, "motivo": e.get("motivo") or "las huellas no son las de la carga del paso 0 de N6"}
    import familias_nav as FN                   # noqa: PLC0415
    from conexion import abrir_driver           # noqa: PLC0415
    from grafos import GRAFOS                   # noqa: PLC0415
    cfg = json.loads(CONFIG_GRAFO.read_text(encoding="utf-8"))
    driver = abrir_driver()
    try:
        nav = FN.Navegador(driver, GRAFOS[cfg["grafo"]]["label"], (BANCO_DIR / "mcp_kg" / cfg["indice_puntos"]).resolve(),
                           sha256_manifiesto=cfg["sha256_manifiesto_indice"], python_vector=None,
                           hubs_esperados=cfg["hubs_esperados"])
        fuente = nav.descripcion_fuente()
        sha_hubs = FN.IP.sha256_bytes("\n".join(sorted(nav.hubs)).encode("utf-8"))
    finally:
        driver.close()
    return e | {"navegador": {"arranca": True, "n_puntos": fuente["n_puntos"], "sha256_manifiesto": fuente["sha256_manifiesto"],
                              "hubs": {"umbral": nav.umbral_hub, "n": len(nav.hubs), "sha256": sha_hubs},
                              "hubs_de_la_config": cfg["hubs_esperados"]}}


def main() -> int:
    try:
        e = estado()
    except SystemExit as x:
        print(str(x))
        return NO_DA
    print(json.dumps(e, ensure_ascii=False))
    if not e["ok"]:
        print(f"FRENO (USD 0): {e['motivo']}")
        return NO_DA
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
