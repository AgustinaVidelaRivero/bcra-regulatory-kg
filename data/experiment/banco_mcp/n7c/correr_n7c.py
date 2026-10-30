#!/usr/bin/env python3
"""correr_n7c.py — El corredor de B2 de N7c: el de N6 (n6/correr_n6.py, importado sin editarlo) para las tres configuraciones
del brazo del grafo sobre el grafo evaluado de B6.3, N7, N7c y N7c+ (n7c/config_agentes_n7c.json; N7c+ con la clave `N7c_amp`,
porque `+` no es válido en un id de sesión: agentes/lanzar_lote_paralelo.py:74). Corre todo lo de N6 con siete reasignaciones,
cada una de un nombre que correr_n6 o su módulo leen al llamar (las líneas son las de correr_n6.py y sus módulos en HEAD):
  1. las configuraciones: CONFIG_AGENTES (el valor por defecto de --config-agentes, que main lee al llamarse, :1007); la
     entrada guarda la ruta de la suya y la relee (:269, :303, :317);
  2. el Neo4j de B6.3: `precondiciones` (main la llama por su nombre, :1059) controla el Neo4j de B6.3 con
     b63/v2/b2/control_neo4j_b63.py (sin editarlo): NEO4J_URI bolt://127.0.0.1:47687 y la huella de contenido de B6.3, en lugar
     del Neo4j propio de N6;
  3. el control de las configuraciones por sha256: la misma `precondiciones`, en lugar de armar_configuraciones_n6 --verificar,
     controla los JSON de MCP y las configs de los servidores de N7, N7c y N7c+ contra sus sha256, que la configuración de
     agentes de la entrada los nombre en su brazo y que sus brazos sean los de la configuración de B2, la que usa el lanzador
     (n7c/lanzar_agente_n7c.py); en los dos modos de entrada;
  4. el tope y el freno: TOPE y FRENO, USD 45 y 38 (D-B2-8), que cargar_entrada exige a una entrada real (:310) y que main toma
     como valor por defecto al llamarse (:1009-1010);
  5. la semilla del orden: SEMILLA_ORDEN y `armar_orden` (armar_entrada y cargar_entrada la llaman por su nombre, :259, :319),
     con N7C:orden:v1 como valor por defecto (el de correr_n6 queda fijado en su firma, :203);
  6. el contenedor de la guarda de memoria: control_memoria_n6.CONTENEDOR, neo4j-bcra-kg-indices-eval (docker() lo lee al
     llamarse, n6/control_memoria_n6.py:133-134 y :147; armar_entrada lo guarda en la entrada, :285);
  7. la guarda de otro paso pago: guardas_lote_n6.PATRON_PAGO y PATRON_PAGO_REAL, con
     `|correr_n7c\\.py|correr_juez_v3\\.py|corrida_cortada_v3\\.py` (paralelo/guardas_lote_n6.py:48, :53; la entrada guarda el
     real y cargar_entrada lo compara, :271, :305).
El octavo cambio (D-B2-6) no es una reasignación: es el lanzador de una sesión, n7c/lanzar_agente_n7c.py, que las dos entradas
nombran como su lanzador.
Lo que queda como en N6, tal cual: las clases de las sesiones, el reintento, el orden de los lotes (primero el sin codificador,
que en B2 queda vacío porque las tres configuraciones cargan el codificador), R5, la memoria y sus umbrales, Docker, el juez de
EV2 con su semilla, su sal y su prefijo de ids opacos, el prefijo «N6-» de los ids de sesión, el registro (registro_n6.json),
la foto del repo, los códigos de salida, el mensaje del freno de cargar_entrada (que sigue diciendo 130 y 100, aunque compara
con 45 y 38) y los valores por defecto de --entrada, --salida y --lanzador (los comandos los pasan siempre).
Uso: .venv/bin/python -B data/experiment/banco_mcp/n7c/correr_n7c.py {entrada|controles|agente|juez|todo|estado} ...
     (los argumentos de correr_n6.main)
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BANCO_DIR = AQUI.parent
for _p in (str(BANCO_DIR / "n6"), str(BANCO_DIR / "b63" / "v2" / "b2")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import correr_n6 as CN                          # noqa: E402  (HEAD, sin editar)
from comun_banco import sha256_file             # noqa: E402

G, CM = CN.G, CN.CM

# 1. Las configuraciones.
CONFIG_AGENTES = AQUI / "config_agentes_n7c.json"
CN.CONFIG_AGENTES = CONFIG_AGENTES

# 2 y 3. El Neo4j de B6.3 y el control de las configuraciones por sha256.
URI_B63 = "bolt://127.0.0.1:47687"
HUELLA_NEO4J_B63 = "2645da6d01795d520f3c4ab5e237050c530238061f849cd7d1e0170be9223463"
CONFIG_LANZADOR = AQUI / "config_agentes_n7c.json"      # la que fija n7c/lanzar_agente_n7c.py
CONFIGURACIONES = {
    "N7": {"brazo": "kg_N7", "archivos": {
        "n7/mcp_kg_n7_evaluado.json": "4e3b9ccb062d8eea26049bb8814d62a5807cd683211539394bedb87632c43777",
        "n7/config_mcp_kg_n7_evaluado.json": "9e9f0ee5b9be4ff41bb2c8cc0c3528892d346197097c6de8b9c5007cb308d8c5"}},
    "N7c": {"brazo": "kg_N7c", "archivos": {
        "n7c/mcp_kg_n7c_evaluado.json": "13a3ae62a542478f2c4bb9261a979de5801ce90fc8fc441b0a695ddd35bb729c",
        "n7c/config_mcp_kg_n7c_evaluado.json": "41b0a6db1950877a23743d100f0ebc3e41e05430c472ad4484f09752e1220d81"}},
    "N7c_amp": {"brazo": "kg_N7c_amp", "archivos": {
        "n7c/mcp_kg_n7c_amp_evaluado.json": "ef76623881b82478950319e07d4a790879b89390ce3fb99bc59b6a221d91a109",
        "n7c/config_mcp_kg_n7c_amp_evaluado.json": "31b39342c736720e5b002423b66453ff219b40daec8e9b73a461e8f8648ad666"}},
}
CAMPOS_NEO4J = ("NEO4J_URI", "kg_meta_sha256", "n_nodos", "n_aristas", "huella_estado", "huella_contenido", "ok")


def _canonico(x) -> str:
    return json.dumps(x, ensure_ascii=False, sort_keys=True)


def control_configuraciones(cfg: dict) -> dict:
    """Por configuración: sus dos archivos dan su sha256 y la configuración de agentes los nombra en su brazo. Y los brazos de
    la configuración de agentes son los de la que usa el lanzador. Frena (8) si algo no da."""
    out, mal = {}, []
    if set(cfg["configuraciones_n6"]) != set(CONFIGURACIONES):
        raise CN.Freno(CN.PRECONDICION, "la configuración de agentes no trae las tres configuraciones de B2")
    for cid, c in CONFIGURACIONES.items():
        b = cfg["brazos"].get(c["brazo"]) or {}
        distintos = [r for r, s in c["archivos"].items() if not (BANCO_DIR / r).is_file() or sha256_file(BANCO_DIR / r) != s]
        nombra = (cfg["configuraciones_n6"][cid].get("brazo") == c["brazo"]
                  and {b.get("mcp_config"), b.get("config_servidor")} == set(c["archivos"]))
        out[cid] = {"sha256_iguales": not distintos, "distintos": distintos, "la_config_de_agentes_los_nombra": nombra}
        if distintos or not nombra:
            mal.append(cid)
    lanzador = json.loads(CONFIG_LANZADOR.read_text(encoding="utf-8"))
    out["brazos_iguales_a_los_del_lanzador"] = _canonico(cfg["brazos"]) == _canonico(lanzador["brazos"])
    if mal or not out["brazos_iguales_a_los_del_lanzador"]:
        raise CN.Freno(CN.PRECONDICION, f"configuraciones de B2 que no dan: {mal}; brazos iguales a los del lanzador: "
                                        f"{out['brazos_iguales_a_los_del_lanzador']}")
    return out


def precondiciones(e: dict, con_neo4j: bool = True) -> dict:
    """Las de correr_n6.precondiciones con el control de las configuraciones de B2 y el Neo4j de B6.3: antes de lanzar nada."""
    out = {"configuraciones": control_configuraciones(e["_cfg"])}
    if con_neo4j:
        import control_neo4j_b63 as CNB                 # noqa: PLC0415  (b63/v2/b2, sin editar)
        n = CNB.estado(HUELLA_NEO4J_B63, URI_B63)
        out["neo4j"] = {k: n.get(k) for k in CAMPOS_NEO4J}
        if not n.get("ok"):
            raise CN.Freno(CN.PRECONDICION, f"el Neo4j de B6.3: {n.get('motivo')}")
    ext = G.extraccion_corriendo()
    out["extraccion"] = ext
    if ext:
        raise CN.Freno(CN.EXTRACCION, f"una extracción corriendo: {ext}")
    otro = G.otro_paso_pago()
    out["otro_paso_pago"] = otro
    if otro:
        raise CN.Freno(CN.OTRO_PASO_PAGO, f"otro paso pago corriendo: {otro}")
    return out


CN.precondiciones = precondiciones

# 4. El tope y el freno (D-B2-8).
CN.TOPE, CN.FRENO = 45.0, 38.0

# 5. La semilla del orden.
SEMILLA_ORDEN = "N7C:orden:v1"
_armar_orden_n6 = CN.armar_orden


def armar_orden(ids: list[str], cfg_agentes: dict, semilla: str = SEMILLA_ORDEN) -> dict:
    """correr_n6.armar_orden con la semilla de B2 por defecto."""
    return _armar_orden_n6(ids, cfg_agentes, semilla)


CN.SEMILLA_ORDEN, CN.armar_orden = SEMILLA_ORDEN, armar_orden

# 6. El contenedor de la guarda de memoria: el del Neo4j de B6.3.
CM.CONTENEDOR = "neo4j-bcra-kg-indices-eval"

# 7. La guarda de otro paso pago.
SUFIJO_N7C = r"|correr_n7c\.py|correr_juez_v3\.py|corrida_cortada_v3\.py"
PATRON_N6 = G.R5.PATRON_PAGO_REAL + G.SUFIJO_N6
G.PATRON_PAGO = G.PATRON_PAGO_REAL = PATRON_N6 + SUFIJO_N7C

main = CN.main

if __name__ == "__main__":
    raise SystemExit(main())
