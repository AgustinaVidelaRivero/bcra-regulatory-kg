#!/usr/bin/env python3
"""servidor_mcp_juguete_n7c.py — El servidor MCP (stdio) de juguete de la corrida en seco de N7c y de las pruebas de sus controles:
las diez herramientas del brazo del grafo (servidor_mcp_kg_nav_rel_amp.tools_de([1, 2, 3, 4, 5]): los mismos nombres,
descripciones, esquemas y anotación de tamaño que los servidores de N7, N7c y N7c+), sobre el índice de juguete de
mcp_kg/selftest_familias_nav_rel_amp.py y su doble del driver: sin Neo4j, sin el kg.json, sin el denso y sin modelo (USD 0).
La variante fija el navegador, como en los servidores reales: N7, NavegadorCand (servidor_mcp_kg_nav_cand.py); N7c, NavegadorRel
(servidor_mcp_kg_nav_rel.py); N7c_amp (N7c+), NavegadorRelAmp (servidor_mcp_kg_nav_rel_amp.py). Las siete de las familias van
por familias_nav_cand.despachar_cand, como en los servidores reales; las tres de la firma v1 devuelven un JSON de juguete sin
procedencias. El log R1 es el de comun_banco.LogR1 (inicio, una línea por llamada y fin), como en los servidores del banco. Su nombre lleva
«servidor_mcp», como los del banco, para que la guarda de memoria de N6 (control_memoria_n6.partes_del_arbol) cuente su huella
como la de un servidor.
Uso: <python del .venv> -B servidor_mcp_juguete_n7c.py --variante {N7|N7c|N7c_amp} --indice <carpeta del índice de juguete>
"""
from __future__ import annotations

import argparse
import asyncio
import json
import sys
import time
from pathlib import Path

AQUI = Path(__file__).resolve().parent
MCP_KG = AQUI.parents[1] / "mcp_kg"
if str(MCP_KG) not in sys.path:
    sys.path.insert(0, str(MCP_KG))
import selftest_familias_nav_rel_amp as ST    # noqa: E402  (el juguete y su doble del driver)
import servidor_mcp_kg_nav_rel_amp as SRA     # noqa: E402  (las diez herramientas)
from comun_banco import LogR1                  # noqa: E402

FNRA, FNR, FNC, IP = ST.FNRA, ST.FNR, ST.FNC, ST.IP
NAVEGADOR = {"N7": FNC.NavegadorCand, "N7c": FNR.NavegadorRel, "N7c_amp": FNRA.NavegadorRelAmp}
SALIDA_V1 = json.dumps({"resultados": [], "nota": "servidor de juguete de la corrida en seco de N7c"}, ensure_ascii=False)


def construir(variante: str, indice: Path):
    import mcp.types as types
    from mcp.server.lowlevel import Server

    nav = NAVEGADOR[variante](ST.DriverJuguete(), ST.LABEL, indice,
                              sha256_manifiesto=IP.sha256_file(indice / "manifiesto.json"))
    tools = SRA.tools_de([1, 2, 3, 4, 5])
    nombres_nav = {t["name"] for t in tools if "familia" in t}
    config = {"variante": variante, "servidor": "juguete de la corrida en seco de N7c"}
    log = LogR1(SRA.NOMBRE_SERVIDOR, f"juguete-{variante}", config,
                IP.sha256_bytes(json.dumps(config, sort_keys=True).encode("utf-8")), {"juguete": True}, {})
    server = Server(SRA.NOMBRE_SERVIDOR, version=f"juguete-{variante}")

    @server.list_tools()
    async def _list_tools() -> list[types.Tool]:
        return [types.Tool(name=t["name"], description=t["description"], inputSchema=t["input_schema"],
                           _meta={"anthropic/maxResultSizeChars": SRA.BASE.TOPE_CARACTERES_RESULTADO}) for t in tools]

    @server.call_tool(validate_input=False)
    async def _call_tool(name: str, arguments: dict):
        t0 = time.perf_counter()
        n, call_id = log.nuevo_call_id()
        try:
            rpc_id = server.request_context.request_id
        except LookupError:
            rpc_id = None
        out = FNC.despachar_cand(nav, name, arguments or {}) if name in nombres_nav else SALIDA_V1
        log.llamada(n, call_id, rpc_id, name, arguments or {}, out, t0)
        return [types.TextContent(type="text", text=out)]

    return server, log


async def servir(variante: str, indice: Path) -> None:
    from mcp.server.stdio import stdio_server
    server, log = construir(variante, indice)
    SRA.BASE._fin_ante_senal(log)
    try:
        async with stdio_server() as (r, w):
            await server.run(r, w, server.create_initialization_options())
    finally:
        if not log.cerrado:
            log.fin()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--variante", choices=sorted(NAVEGADOR), required=True)
    ap.add_argument("--indice", type=Path, required=True)
    a = ap.parse_args()
    asyncio.run(servir(a.variante, a.indice.resolve()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
