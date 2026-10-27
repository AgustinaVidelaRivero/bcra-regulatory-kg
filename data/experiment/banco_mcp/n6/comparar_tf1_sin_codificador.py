#!/usr/bin/env python3
"""comparar_tf1_sin_codificador.py — N6 de U-NAV-DISENO: si T−F1 puede ir sin el codificador de consultas (decisión de la autora
del 27/10/2026, punto 8: «T−F1 sin codificador, si comprobás por código que sus herramientas no lo usan y que sus salidas dan
iguales byte a byte sin él»). USD 0, sin modelo de lenguaje.

  1. Por código (ast): cada uso del denso en familias_nav.py y familias_nav_cand.py (el atributo `denso` y la clase `Denso`), con
     la función donde está; y, para cada herramienta de T−F1 de las familias, las funciones que alcanza desde su método (las
     llamadas `self.<método>` del navegador y las de las funciones del módulo), y si alguna toca el denso.
  2. Byte a byte, por stdio (banco_mcp/cliente_falso.py) sobre el Neo4j propio de N6: el servidor nuevo con la config de T−F1 con
     el denso (la de n6/config_mcp_kg_n6_T-F1.json con el bloque `denso` de config_mcp_kg_nav_acumulado.json, que lanza el
     codificador) y con la config de T−F1 sin él (n6/config_mcp_kg_n6_T-F1.json), uno después del otro (una sola carga del
     codificador a la vez), con la misma batería en sus 9 herramientas (la del selftest del servidor: las tres de hoy, las 1.757
     llamadas de ver_descendientes y las otras de la navegación). Compara cada salida y el `output_str` de cada llamada del log
     R1. La cabecera del log R1 cambia en fuente.navegacion.denso (el modelo o nada) y en lo que nombra la config: se declara y
     no cuenta como diferencia.
  3. La memoria de la máquina antes y después de cada servidor (memoria_n6.memoria_maquina).
Escribe un JSON con el resultado, sin texto de las salidas (sus sha256). Código 1 si algo difiere.
Uso: NEO4J_URI=bolt://127.0.0.1:57687 BANCO_VENV_VECTOR=<venv> python -B n6/comparar_tf1_sin_codificador.py --salida <json> --trabajo <dir>
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import os
import sys
import time
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BANCO_DIR = AQUI.parent
MCP_KG = BANCO_DIR / "mcp_kg"
for _p in (str(BANCO_DIR), str(MCP_KG), str(AQUI)):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import selftest_servidor_mcp_kg_nav_cand as ST  # noqa: E402  (la batería del selftest del servidor)
import memoria_n6 as MEM  # noqa: E402
from cliente_falso import ClienteFalso  # noqa: E402

NEO4J_URI_N6 = "bolt://127.0.0.1:57687"
CONFIG_TF1 = AQUI / "config_mcp_kg_n6_T-F1.json"
CONFIG_ACUM = MCP_KG / "config_mcp_kg_nav_acumulado.json"


def sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


# --------------------------------------------------------------------------- #
# 1. Por código                                                                #
# --------------------------------------------------------------------------- #
def usos_del_denso() -> dict:
    """Los usos del denso en las dos familias y, por herramienta de T−F1, las funciones que alcanza y si tocan el denso."""
    funcs, usos = {}, []
    for archivo in ("familias_nav.py", "familias_nav_cand.py"):
        arbol = ast.parse((MCP_KG / archivo).read_text(encoding="utf-8"))
        for nodo in arbol.body:
            dentro = [(f"{nodo.name}.{f.name}", f) for f in nodo.body if isinstance(f, ast.FunctionDef)] \
                if isinstance(nodo, ast.ClassDef) else ([(nodo.name, nodo)] if isinstance(nodo, ast.FunctionDef) else [])
            for nombre, f in dentro:
                llama, toca = set(), []
                for x in ast.walk(f):
                    if isinstance(x, ast.Attribute) and x.attr == "denso" or isinstance(x, ast.Name) and x.id == "Denso":
                        toca.append(x.lineno)
                    if isinstance(x, ast.Call):
                        fn = x.func
                        if isinstance(fn, ast.Attribute) and isinstance(fn.value, ast.Name) and fn.value.id in ("self", "FN"):
                            llama.add(fn.attr)
                        elif isinstance(fn, ast.Name):
                            llama.add(fn.id)
                funcs[f"{archivo}:{nombre}"] = {"llama": llama, "toca_denso": sorted(set(toca))}
                for ln in sorted(set(toca)):
                    usos.append({"archivo": archivo, "funcion": nombre, "renglon": ln})
    por_nombre = {}
    for k, v in funcs.items():
        por_nombre.setdefault(k.rsplit(".", 1)[-1].split(":")[-1], []).append(k)

    def alcanza(desde: list[str]) -> set[str]:
        vistos, pila = set(), list(desde)
        while pila:
            k = pila.pop()
            if k in vistos:
                continue
            vistos.add(k)
            for n in funcs[k]["llama"]:
                pila.extend(por_nombre.get(n, []))
        return vistos

    import servidor_mcp_kg_nav_cand as CAND   # noqa: PLC0415
    cfg = json.loads(CONFIG_TF1.read_text(encoding="utf-8"))
    herramientas = [t["name"] for t in CAND.tools_de(cfg["familias"]) if "familia" in t]
    por_h = {}
    for h in herramientas:
        raices = [k for k in funcs if k.endswith(f".{h}")]
        alc = alcanza(raices)
        por_h[h] = {"metodos": sorted(raices), "funciones_alcanzadas": len(alc),
                    "tocan_el_denso": sorted(k for k in alc if funcs[k]["toca_denso"])}
    return {"usos_del_denso": usos, "herramientas_de_T-F1_de_las_familias": herramientas, "por_herramienta": por_h,
            "ninguna_herramienta_de_T-F1_llega_al_denso": all(not v["tocan_el_denso"] for v in por_h.values())}


# --------------------------------------------------------------------------- #
# 2. Byte a byte                                                               #
# --------------------------------------------------------------------------- #
def correr_servidor(config: Path, llamadas: list, log: Path) -> dict:
    env = {k: v for k, v in os.environ.items() if k in ("NEO4J_URI", "BANCO_VENV_VECTOR", "PATH", "HOME", "TMPDIR")}
    env.update({"PYTHONDONTWRITEBYTECODE": "1", "BANCO_LOG_R1": str(log), "BANCO_SESION_TAG": "comparar_tf1",
                "HF_HUB_OFFLINE": "1", "TRANSFORMERS_OFFLINE": "1"})
    cmd = [sys.executable, "-B", str(MCP_KG / "servidor_mcp_kg_nav_cand.py"), "--config", str(config)]
    antes = MEM.memoria_maquina()
    t0 = time.time()
    with ClienteFalso(cmd=cmd, env=env, cwd=BANCO_DIR.parents[2]) as cli:
        tools = [t["name"] for t in cli.listar_tools()]
        salidas = [cli.llamar(n, a) for n, a in llamadas]
    despues = MEM.memoria_maquina()
    lineas = [json.loads(x) for x in log.read_text(encoding="utf-8").splitlines() if x.strip()]
    return {"tools": tools, "salidas": salidas, "duracion_s": round(time.time() - t0, 1),
            "log_inicio": next(x for x in lineas if x.get("evento") == "inicio"),
            "log_salidas": [x.get("output_str") for x in lineas if x.get("evento") == "llamada"],
            "memoria_antes": antes, "memoria_despues": despues}


def diferencias(a, b, ruta="") -> list[str]:
    if isinstance(a, dict) and isinstance(b, dict):
        out = []
        for k in sorted(set(a) | set(b)):
            out += diferencias(a.get(k), b.get(k), f"{ruta}.{k}" if ruta else k)
        return out
    return [] if a == b else [ruta]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path, required=True)
    ap.add_argument("--trabajo", type=Path, required=True, help="carpeta para la config con el denso y los logs (fuera del repo)")
    a = ap.parse_args()
    if os.environ.get("NEO4J_URI") != NEO4J_URI_N6 or not os.environ.get("BANCO_VENV_VECTOR"):
        raise SystemExit(f"FRENO: hace falta NEO4J_URI={NEO4J_URI_N6} y BANCO_VENV_VECTOR")
    codigo = usos_del_denso()
    a.trabajo.mkdir(parents=True, exist_ok=True)
    sin = json.loads(CONFIG_TF1.read_text(encoding="utf-8"))
    con = dict(sin)
    con["denso"] = json.loads(CONFIG_ACUM.read_text(encoding="utf-8"))["denso"]
    con_p = a.trabajo / "config_mcp_kg_n6_T-F1_con_el_denso.json"
    con_p.write_text(json.dumps(con, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    from conexion import abrir_driver      # noqa: PLC0415  (data/experiment/neo4j, por servidor_mcp_kg)
    from grafos import GRAFOS              # noqa: PLC0415
    import familias_nav_cand as FNC        # noqa: PLC0415
    driver = abrir_driver()
    nav = FNC.NavegadorCand(driver, GRAFOS[sin["grafo"]]["label"], (MCP_KG / sin["indice_puntos"]).resolve(),
                            sha256_manifiesto=sin["sha256_manifiesto_indice"], python_vector=None,
                            hubs_esperados=sin["hubs_esperados"])
    base, vd, otras = ST.bateria(nav)
    driver.close()
    llamadas = base + vd + otras
    r_con = correr_servidor(con_p, llamadas, a.trabajo / "log_r1_tf1_con_el_denso.jsonl")
    r_sin = correr_servidor(CONFIG_TF1, llamadas, a.trabajo / "log_r1_tf1_sin_el_denso.jsonl")
    iguales = sum(x == y for x, y in zip(r_con["salidas"], r_sin["salidas"]))
    iguales_log = sum(x == y for x, y in zip(r_con["log_salidas"], r_sin["log_salidas"]))
    por_tool = {}
    for (n, _), x, y in zip(llamadas, r_con["salidas"], r_sin["salidas"]):
        t = por_tool.setdefault(n, [0, 0])
        t[0] += 1
        t[1] += x == y
    cab = diferencias(r_con["log_inicio"], r_sin["log_inicio"])
    esperadas = {"config_sha256", "fuente.navegacion.denso", "entorno.config_path", "config.denso.nota", "config.denso.requerido",
                 "config.denso.python_env", "config.denso.modelo", "config.denso.revision", "argv", "timestamp", "pid"}
    todo_igual = (r_con["tools"] == r_sin["tools"] and iguales == len(llamadas) == len(r_con["salidas"]) == len(r_sin["salidas"])
                  and iguales_log == len(llamadas) == len(r_con["log_salidas"]) == len(r_sin["log_salidas"])
                  and r_con["salidas"] == r_con["log_salidas"] and r_sin["salidas"] == r_sin["log_salidas"])
    out = {"que": "T−F1 con y sin el codificador de consultas (decisión de la autora del 27/10/2026, punto 8)",
           "por_codigo": codigo, "llamadas": len(llamadas), "por_herramienta": {k: {"llamadas": v[0], "iguales": v[1]}
                                                                               for k, v in sorted(por_tool.items())},
           "herramientas_servidas": r_sin["tools"], "mismas_herramientas": r_con["tools"] == r_sin["tools"],
           "salidas_iguales": iguales, "log_r1_output_str_iguales": iguales_log,
           "log_r1_igual_a_la_salida": {"con": r_con["salidas"] == r_con["log_salidas"], "sin": r_sin["salidas"] == r_sin["log_salidas"]},
           "sha256_salidas": {"con": sha("\n".join(map(sha, r_con["salidas"]))), "sin": sha("\n".join(map(sha, r_sin["salidas"])))},
           "cabecera_log_r1_difiere_en": cab, "cabecera_solo_lo_declarado": set(cab) <= esperadas,
           "denso_en_la_cabecera": {"con": r_con["log_inicio"]["fuente"]["navegacion"]["denso"],
                                    "sin": r_sin["log_inicio"]["fuente"]["navegacion"]["denso"]},
           "memoria": {"con_el_denso": {"antes": r_con["memoria_antes"], "despues": r_con["memoria_despues"]},
                       "sin_el_denso": {"antes": r_sin["memoria_antes"], "despues": r_sin["memoria_despues"]}},
           "duracion_s": {"con": r_con["duracion_s"], "sin": r_sin["duracion_s"]},
           "todo_igual": todo_igual and codigo["ninguna_herramienta_de_T-F1_llega_al_denso"] and set(cab) <= esperadas}
    a.salida.parent.mkdir(parents=True, exist_ok=True)
    a.salida.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for p in (a.trabajo / "log_r1_tf1_con_el_denso.jsonl", a.trabajo / "log_r1_tf1_sin_el_denso.jsonl"):
        p.unlink()
    print(json.dumps({k: out[k] for k in ("llamadas", "salidas_iguales", "log_r1_output_str_iguales", "mismas_herramientas",
                                         "cabecera_log_r1_difiere_en", "denso_en_la_cabecera", "todo_igual")}, ensure_ascii=False))
    print("por código:", json.dumps({"usos": [f"{u['archivo']}:{u['renglon']} {u['funcion']}" for u in codigo["usos_del_denso"]],
                                     "llegan_al_denso": {h: v["tocan_el_denso"] for h, v in codigo["por_herramienta"].items()}},
                                    ensure_ascii=False))
    return 0 if out["todo_igual"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
