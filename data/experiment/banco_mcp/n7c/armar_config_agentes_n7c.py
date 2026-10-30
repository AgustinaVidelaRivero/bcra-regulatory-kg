#!/usr/bin/env python3
"""armar_config_agentes_n7c.py — B2 de N7c: arma, por código y siempre igual, las dos configuraciones de agentes de B2,
n7c/config_agentes_n7c.json (la de B2: N7, N7c y N7c+, tres repeticiones cada una) y n7c/config_agentes_n7c_humo.json (la del
humo: la misma salvo las repeticiones, una por configuración). Con --verificar no escribe: dice si los dos archivos son, byte
a byte, los que arma.

Cada campo, con su fuente (también en el campo `fuentes_de_los_campos` del archivo):
  - `prompt`, `corte_R5`, `modelo`, `claude_code_version_sellada`, `modo_harness`, `env_por_sesion` y `base`: los de
    b63/v2/b2/config_agentes_b63.json, tal cual;
  - `R5`: config_agentes_b63.json no lo trae; sale de su `corte_R5`, con la forma que exige correr_n6.armar_entrada
    (tope_tool_calls_prompt, max_turns y max_budget_usd): 30, 32 y 1,80, el R5 de N6;
  - los brazos:
      kg_N7       el brazo `kg` de config_agentes_b63.json, campo por campo;
      kg_N7c      el mismo, con el JSON de MCP y la config del servidor de N7c (n7c/mcp_kg_n7c_evaluado.json y
                  n7c/config_mcp_kg_n7c_evaluado.json) y sus módulos en `archivos_servidor` (el servidor primero);
      kg_N7c_amp  el mismo, con los de N7c+ (n7c/mcp_kg_n7c_amp_evaluado.json y n7c/config_mcp_kg_n7c_amp_evaluado.json);
  - `configuraciones_n6`: N7, N7c y N7c+, cada una con su brazo, sus repeticiones y `carga_codificador: true` (las tres
    cargan el codificador de consultas: su config pide el denso). N7c+ va con la clave `N7c_amp`: el id de una sesión lleva
    la clave de su configuración (correr_n6.id_sesion) y `+` no es válido en un id (agentes/lanzar_lote_paralelo.py:74);
    `nombres` da su nombre, N7c+.
Uso: python3 -I -B data/experiment/banco_mcp/n7c/armar_config_agentes_n7c.py [--verificar]
"""
from __future__ import annotations

import copy
import hashlib
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BANCO_DIR = AQUI.parent
B63 = "b63/v2/b2/config_agentes_b63.json"
SALIDAS = {"b2": AQUI / "config_agentes_n7c.json", "humo": AQUI / "config_agentes_n7c_humo.json"}
REPETICIONES = {"b2": 3, "humo": 1}
DE_B63 = ("prompt", "corte_R5", "modelo", "claude_code_version_sellada", "modo_harness", "env_por_sesion", "base")
SERVIDOR_N7 = ["mcp_kg/servidor_mcp_kg_nav_cand.py", "mcp_kg/servidor_mcp_kg_nav.py", "mcp_kg/servidor_mcp_kg.py",
               "mcp_kg/familias_nav.py", "mcp_kg/familias_nav_cand.py", "mcp_kg/indice_puntos.py",
               "mcp_kg/codificador_consultas.py"]
BRAZOS = {
    "kg_N7": {},
    "kg_N7c": {"mcp_config": "n7c/mcp_kg_n7c_evaluado.json", "config_servidor": "n7c/config_mcp_kg_n7c_evaluado.json",
               "archivos_servidor": ["mcp_kg/servidor_mcp_kg_nav_rel.py"] + SERVIDOR_N7 + ["mcp_kg/familias_nav_rel.py"]},
    "kg_N7c_amp": {"mcp_config": "n7c/mcp_kg_n7c_amp_evaluado.json",
                   "config_servidor": "n7c/config_mcp_kg_n7c_amp_evaluado.json",
                   "archivos_servidor": ["mcp_kg/servidor_mcp_kg_nav_rel_amp.py", "mcp_kg/servidor_mcp_kg_nav_rel.py"]
                   + SERVIDOR_N7 + ["mcp_kg/familias_nav_rel.py", "mcp_kg/familias_nav_rel_amp.py"]},
}
CONFIGURACIONES = (("N7", "kg_N7"), ("N7c", "kg_N7c"), ("N7c_amp", "kg_N7c_amp"))


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def armar() -> dict[str, str]:
    b63 = json.loads((BANCO_DIR / B63).read_text(encoding="utf-8"))
    kg = b63["brazos"]["kg"]
    if kg["archivos_servidor"] != SERVIDOR_N7 or kg["mcp_config"] != "n7/mcp_kg_n7_evaluado.json":
        raise SystemExit("ABORTO: el brazo kg de config_agentes_b63.json no es el de N7")
    brazos = {}
    for nombre, cambios in BRAZOS.items():
        b = copy.deepcopy(kg)
        for k, v in cambios.items():
            if k not in b:
                raise SystemExit(f"ABORTO: el campo {k} no está en el brazo kg de B6.3")
            b[k] = v
        brazos[nombre] = b
    corte = b63["corte_R5"]
    archivos_brazos = sorted({r for b in brazos.values() for r in [b["mcp_config"], b["config_servidor"],
                                                                     *b["archivos_servidor"]]})
    out = {}
    for clave, ruta in SALIDAS.items():
        c = {"unidad": "N7c, B2: la configuración de agentes de N7, N7c y N7c+ (n7c/armar_config_agentes_n7c.py)",
             "por_que": ("La corrección del brazo del grafo (N7c) se compara en B2 en tres configuraciones del mismo brazo "
                         "sobre el grafo evaluado de B6.3: N7 (la elegida en N6, T-F6), N7c (ver_punto con la sección de "
                         "puntos relacionados) y N7c+ (además, la familia y la línea de la cita). Las instrucciones del "
                         "agente, el modelo, el CLI y R5 son los de B6.3; cambia solo el servidor del grafo."),
             "fuentes": {"config_agentes_b63": {"ruta": B63, "sha256": sha(BANCO_DIR / B63)}},
             "fuentes_de_los_campos": {
                 **{k: "config_agentes_b63.json, tal cual" for k in DE_B63},
                 "R5": "sale del corte_R5 de config_agentes_b63.json (30, 32 y 1,80: el R5 de N6)",
                 "brazos.kg_N7": "el brazo kg de config_agentes_b63.json, campo por campo",
                 "brazos.kg_N7c": "el brazo kg de config_agentes_b63.json con mcp_config, config_servidor y "
                                  "archivos_servidor de N7c",
                 "brazos.kg_N7c_amp": "el brazo kg de config_agentes_b63.json con mcp_config, config_servidor y "
                                      "archivos_servidor de N7c+",
                 "configuraciones_n6": "N7, N7c y N7c+ (clave N7c_amp), con carga_codificador true y sus repeticiones: 3 en "
                                       "B2 y 1 en el humo",
                 "sha256_de_cada_archivo": "los archivos que nombran los brazos, medidos al armar"},
             **{k: b63[k] for k in DE_B63},
             "R5": {"tope_tool_calls_prompt": corte["tope_tool_calls_en_prompt"], "max_turns": corte["max_turns"],
                    "max_budget_usd": corte["max_budget_usd_por_sesion"]},
             "brazos": brazos,
             "configuraciones_n6": {cid: {"brazo": b, "repeticiones": REPETICIONES[clave], "carga_codificador": True}
                                    for cid, b in CONFIGURACIONES},
             "nombres": {"N7": "N7", "N7c": "N7c", "N7c_amp": "N7c+"},
             "sha256_de_cada_archivo": {r: sha(BANCO_DIR / r) for r in archivos_brazos}}
        out[clave] = json.dumps(c, ensure_ascii=False, indent=1) + "\n"
    return out


def main(argv: list[str]) -> int:
    textos = armar()
    if "--verificar" in argv:
        iguales = {k: SALIDAS[k].is_file() and SALIDAS[k].read_text(encoding="utf-8") == t for k, t in textos.items()}
        print(json.dumps({"iguales_a_lo_que_se_arma": iguales}, ensure_ascii=False))
        return 0 if all(iguales.values()) else 1
    for k, t in textos.items():
        SALIDAS[k].write_text(t, encoding="utf-8")
        print(f"{hashlib.sha256(t.encode('utf-8')).hexdigest()}  n7c/{SALIDAS[k].name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
