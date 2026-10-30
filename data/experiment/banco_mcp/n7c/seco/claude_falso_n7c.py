#!/usr/bin/env python3
"""claude_falso_n7c.py — El CLI falso de la corrida en seco de N7c: el de N6 (n6/seco/claude_falso_n6.py, importado sin
editarlo: el stream, los planes, la falla, el otro paso pago, el sistema falso y la transcripción) con el servidor de juguete
(n7c/seco/servidor_mcp_juguete_n7c.py) en lugar del servidor real de la sesión. Ningún modelo y ninguna petición a la API.

Lee el JSON de MCP que le pasa el lanzador (--mcp-config: el del brazo de la sesión, en la configuración de B2 que fija
n7c/lanzar_agente_n7c.py), anota en el registro que nombra el estado (`registro_mcp`, un renglón JSON por sesión) qué JSON
recibió la sesión (por su BANCO_SESION_TAG) y qué variante le corresponde, y llama al CLI falso de N6 con el JSON de MCP de
juguete de esa variante (`mcp_juguete` del estado: el servidor de juguete con el mismo nombre, `kg`, y el mismo bloque `env`
del JSON real). Desde la copia de trabajo el servidor real no arranca (el .venv del JSON de MCP, el kg.json y la matriz densa no
están: diagnóstico de la C1); el servidor real lo prueban n7c/control_servidores_n7c.py, desde el repo, y el humo.
Un JSON de MCP que no es el de ninguna de las tres configuraciones sale con 2, sin lanzar nada.
Lo invoca el envoltorio que arma la corrida en seco en su carpeta de trabajo: `claude` en el PATH, con `--estado <json>`.
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BANCO_DIR = AQUI.parents[1]
if str(BANCO_DIR / "n6" / "seco") not in sys.path:
    sys.path.insert(0, str(BANCO_DIR / "n6" / "seco"))
import claude_falso_n6 as CF6          # noqa: E402  (HEAD, sin editar)

VARIANTE_DE = {"n7/mcp_kg_n7_evaluado.json": "N7", "n7c/mcp_kg_n7c_evaluado.json": "N7c",
               "n7c/mcp_kg_n7c_amp_evaluado.json": "N7c_amp"}


def main(argv: list[str]) -> int:
    if argv[:1] != ["--estado"]:
        sys.stderr.write("CLI falso de N7c: falta --estado\n")
        return 2
    estado = json.loads(Path(argv[1]).read_text(encoding="utf-8"))
    args = list(argv[2:])
    if "--mcp-config" in args:
        i = args.index("--mcp-config")
        real = Path(args[i + 1]).resolve()
        rel = str(real.relative_to(BANCO_DIR)) if real.is_relative_to(BANCO_DIR) else str(real)
        variante = VARIANTE_DE.get(rel)
        with open(estado["registro_mcp"], "a", encoding="utf-8") as f:
            f.write(json.dumps({"tag": os.environ.get("BANCO_SESION_TAG"), "mcp_config": rel, "variante": variante},
                               ensure_ascii=False) + "\n")
        if variante is None:
            sys.stderr.write("CLI falso de N7c: un JSON de MCP que no es el de ninguna configuración de B2\n")
            return 2
        args[i + 1] = estado["mcp_juguete"][variante]
    return CF6.main(["--estado", argv[1]] + args)


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
