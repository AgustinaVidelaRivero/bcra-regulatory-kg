#!/usr/bin/env python3
"""test_aislamiento_a2_1.py — Aislamiento POR CAPACIDAD de la configuración BM25 del
servidor de fragmentos (A2.1, tramo 1, §3, punto 4). Costo USD 0: modo init del lanzador
(ninguna petición llega a la API) y cliente falso.

Mismos criterios (a) a (d) que aislamiento/test_aislamiento.py (U-A2.0-banco), del que se
importan las piezas (lectura del JSON de MCP, conjuntos de tools y artefactos del grafo),
aplicados al brazo `fragmentos_bm25` de a2_1/config_agentes_a2_1.json, más una parte
dinámica en (b) y (c): el servidor en modo BM25 corre bajo un audit hook
(a2_1/sonda_auditoria.py) mientras recibe llamadas reales, y se registra qué importa,
qué abre y qué sockets crea.

  (a) inventario: tools del brazo en `system/init` = mcp__fragmentos__buscar_pasajes;
      ninguna del grafo, ninguna built-in, permission mode dontAsk, servidor connected.
  (b) artefactos del grafo: el agente no tiene tools de archivos ni de shell; el código del
      servidor (servidor_mcp_vector.py, bm25_fragmentos.py, construir_indice.py) no importa
      módulos del grafo ni menciona sus rutas; `import neo4j` falla en su venv; y en la
      corrida auditada el proceso no importa neo4j, numpy, torch, transformers ni
      sentence_transformers, y no abre ningún archivo del modelo (caché de Hugging Face, pesos,
      matriz densa) ni del grafo. Los metadatos `*.dist-info/` que lee (por los entry points de
      los paquetes del venv) se listan aparte.
  (c) puerto de Neo4j: sin tools de red; el código no tiene sockets ni bolt; en la corrida
      auditada no hay connect, bind, resolución de nombres ni envíos, y ningún socket de
      red (AF_INET/AF_INET6). Los únicos sockets que se admiten son AF_UNIX: el par que
      crea el loop de asyncio para despertarse (socket.socketpair), que no sale del proceso;
      y los únicos subprocesos, `uname` y `file`, que lanza platform.platform() al registrar
      el entorno en el log R1.
  (d) positivo: servidor connected con su tool en init + llamada real por el MISMO JSON de
      MCP (expansión de variables idéntica) que devuelve pasajes de su índice.

Uso:
  BANCO_VENV_VECTOR=<venv 3.12> .venv/bin/python -B data/experiment/banco_mcp/a2_1/test_aislamiento_a2_1.py
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BANCO_DIR = AQUI.parent
REPO_DIR = BANCO_DIR.parents[2]
for _p in (str(AQUI), str(BANCO_DIR), str(BANCO_DIR / "aislamiento")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import lanzar_agente_a2_1 as L21                                   # noqa: E402
import test_aislamiento as TA                                       # noqa: E402  (U-A2.0-banco: solo import)
from cliente_falso import ClienteFalso                              # noqa: E402
from comun_banco import rel_repo, sha256_file                       # noqa: E402

BRAZO = "fragmentos_bm25"
OUT = BANCO_DIR / "aislamiento" / "resultados" / "a2_1"
CODIGO = [BANCO_DIR / "mcp_vector" / "servidor_mcp_vector.py", BANCO_DIR / "mcp_vector" / "bm25_fragmentos.py",
          BANCO_DIR / "mcp_vector" / "construir_indice.py"]
# El mismo conjunto que test_aislamiento.main (b), y la misma expresión de (c).
MODULOS_GRAFO = {"neo4j", "neo4j_index", "grafos", "conexion", "harness", "loader", "tools_juguete", "agente_v2", "tools_v2"}
RE_SOCKETS = r"\bsocket\b|GraphDatabase|bolt://|:7687|requests\.|urllib|httpx"
MODULOS_PROHIBIDOS_BM25 = {"neo4j", "numpy", "torch", "transformers", "sentence_transformers", "huggingface_hub",
                           "safetensors", "tokenizers"} | MODULOS_GRAFO
SUBPROCESOS_PLATFORM = {"uname", "file"}
LLAMADAS = [{"consulta": "efectivo mínimo", "limite": 3}, {"consulta": "garantías preferidas A y B", "limite": 50},
            {"consulta": "clasificación de deudores en situación 3"}]


def enmascarar(p: str) -> str:
    try:
        return rel_repo(p)
    except Exception:
        return p


def corrida_auditada(env: dict) -> dict:
    cmd, e = TA.cmd_desde_mcp_json(BANCO_DIR / L21.cargar_cfg()["brazos"][BRAZO]["mcp_config"],
                                   dict(env, BANCO_LOG_R1=str(OUT / "log_r1_auditada_fragmentos_bm25.jsonl"),
                                        BANCO_SESION_TAG="aislamiento_auditada_fragmentos_bm25"))
    python, servidor, args = cmd[0], cmd[2], cmd[3:]
    with tempfile.TemporaryDirectory() as td:
        reg = Path(td) / "sonda.json"
        with ClienteFalso([python, "-B", str(AQUI / "sonda_auditoria.py"), str(reg), servidor] + args, env=e,
                          timeout_s=600) as cli:
            tools = [t["name"] for t in cli.listar_tools()]
            textos = [cli.llamar("buscar_pasajes", c) for c in LLAMADAS]
        r = json.loads(reg.read_text(encoding="utf-8"))
    importados = set(r["imports"]) | set(r["sys_modules_al_salir"])
    raiz = {m.split(".")[0] for m in importados}
    abiertos = [enmascarar(p) for p in r["open"]]
    # Archivos del modelo: la caché de Hugging Face, el repo del modelo, la matriz densa y los pesos. Los metadatos
    # (`*.dist-info/`) de un paquete instalado pero no importado no cuentan: se leen cuando una librería recorre los
    # entry points de todos los paquetes del venv; se listan aparte.
    abiertos_modelo = [p for p in abiertos if ".cache/huggingface" in p or "harrier" in p or p.endswith((".npy", ".safetensors"))]
    metadatos = sorted({p.split("site-packages/", 1)[1].split("/", 1)[0] for p in abiertos
                        if "site-packages/" in p and ".dist-info/" in p})
    abiertos_grafo = [p for p in abiertos if any(x in p for x in TA.ARTEFACTOS_GRAFO) or p.endswith("kg.json")]
    nuevos = [s for s in r["socket"] if s["evento"] == "socket.__new__"]
    familias = sorted({s["familia"] for s in nuevos})
    red = [s for s in r["socket"] if s["evento"] != "socket.__new__"]
    return {"python_servidor": r["python"], "tools": tools, "n_llamadas": len(textos),
            "n_resultados": [len(json.loads(t)["resultados"]) for t in textos],
            "modulos_prohibidos_importados": sorted(raiz & MODULOS_PROHIBIDOS_BM25),
            "n_modulos_importados": len(importados),
            "n_archivos_abiertos": len(abiertos),
            "archivos_abiertos_del_repo": sorted({p for p in abiertos if not p.startswith(("/", "~"))}),
            "n_abiertos_fuera_del_repo": sum(1 for p in abiertos if p.startswith(("/", "~"))),
            "abiertos_del_modelo": abiertos_modelo, "abiertos_del_grafo": abiertos_grafo,
            "metadatos_dist_info_leidos": metadatos,
            "sockets_creados": len(nuevos), "familias_de_socket": familias,
            "eventos_de_red": red, "subprocesos": sorted({x["ejecutable"] for x in r["subprocess"]}),
            "n_subprocesos": len(r["subprocess"])}


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    venv_vec = os.environ.get("BANCO_VENV_VECTOR")
    if not venv_vec:
        raise SystemExit("BANCO_VENV_VECTOR no definido")
    env = dict(os.environ, BANCO_REPO=str(REPO_DIR), BANCO_VENV_VECTOR=venv_vec)
    cfg = L21.cargar_cfg()

    # (a) inventario
    meta = L21.lanzar(BRAZO, f"AISL-{BRAZO}", "pregunta de prueba (modo init, sin modelo)", OUT / "init", modo="init")
    tools = set(meta["inventario_tools_R6"]["tools_en_init"] or [])
    esperadas = set(cfg["brazos"][BRAZO]["tools_esperadas"])
    tools_kg = set(TA.CFG["brazos"]["kg"]["tools_esperadas"])
    srv = meta["servidores_mcp"]["en_init"] or []
    a_res = {"tools": sorted(tools), "esperadas": sorted(esperadas), "coincide": tools == esperadas,
             "sin_tools_del_grafo": not (tools & tools_kg),
             "sin_builtin": not (tools & TA.TOOLS_ARCHIVOS_SHELL_RED) and all(t.startswith("mcp__") for t in tools),
             "permission_mode": meta["harness_R10"]["permission_mode"], "servidores_en_init": srv,
             "claude_code_version": meta["harness_R10"]["claude_code_version"],
             "coincide_con_sellada": meta["harness_R10"]["coincide_con_sellada"]}
    a_res["PASS"] = (a_res["coincide"] and a_res["sin_tools_del_grafo"] and a_res["sin_builtin"]
                     and a_res["permission_mode"] == "dontAsk" and any(s.get("status") == "connected" for s in srv))

    # parte dinámica de (b) y (c)
    din = corrida_auditada(env)

    # (b) artefactos del grafo
    fuentes = {rel_repo(p): p.read_text(encoding="utf-8") for p in CODIGO}
    imports = sorted({m for t in fuentes.values()
                      for m in re.findall(r"^\s*(?:from|import)\s+([A-Za-z_][\w.]*)", t, flags=re.M)})
    menciona = sorted({x for t in fuentes.values() for x in TA.ARTEFACTOS_GRAFO if x in t})
    r_imp = subprocess.run([f"{venv_vec}/bin/python", "-c", "import neo4j"], capture_output=True, text=True)
    b_res = {"agente_tools_de_archivo_o_shell": sorted(tools & TA.TOOLS_ARCHIVOS_SHELL_RED),
             "codigo": {k: sha256_file(REPO_DIR / k) for k in fuentes},
             "imports_del_codigo": imports,
             "importa_modulos_del_grafo": sorted({i.split(".")[0] for i in imports} & MODULOS_GRAFO),
             "menciona_artefactos_del_grafo": menciona,
             "import_neo4j_en_venv": {"returncode": r_imp.returncode, "stderr_tail": r_imp.stderr.strip()[-120:]},
             "corrida_auditada": {k: din[k] for k in ("python_servidor", "tools", "n_llamadas", "n_resultados",
                                                      "modulos_prohibidos_importados", "n_modulos_importados",
                                                      "n_archivos_abiertos", "archivos_abiertos_del_repo",
                                                      "n_abiertos_fuera_del_repo",
                                                      "abiertos_del_modelo", "abiertos_del_grafo",
                                                      "metadatos_dist_info_leidos")}}
    b_res["PASS"] = (not b_res["agente_tools_de_archivo_o_shell"] and not b_res["importa_modulos_del_grafo"]
                     and not menciona and r_imp.returncode != 0 and not din["modulos_prohibidos_importados"]
                     and not din["abiertos_del_modelo"] and not din["abiertos_del_grafo"]
                     and all(n > 0 for n in din["n_resultados"]))

    # (c) puerto de Neo4j
    abre = {k: bool(re.search(RE_SOCKETS, t)) for k, t in fuentes.items()}
    c_res = {"agente_tools_de_red_o_shell": sorted(tools & {"Bash", "WebFetch", "WebSearch"}),
             "codigo_abre_sockets_o_bolt": abre, "venv_tiene_driver_neo4j": r_imp.returncode == 0,
             "corrida_auditada": {k: din[k] for k in ("sockets_creados", "familias_de_socket", "eventos_de_red",
                                                      "subprocesos", "n_subprocesos")},
             "subprocesos_admitidos": sorted(SUBPROCESOS_PLATFORM),
             "puerto": "127.0.0.1:7687 (docker-compose.yml del backend del grafo)",
             "nota": ("socket.__new__ con AF_UNIX es el par del loop de asyncio (socket.socketpair): no tiene dirección "
                      "de red. Los subprocesos admitidos (uname, file) son los que lanza platform.platform() de la "
                      "biblioteca estándar al registrar el entorno en el log R1 (comun_banco.versiones_entorno, "
                      "compartido con los otros servidores): no tocan la red ni el grafo.")}
    c_res["PASS"] = (not c_res["agente_tools_de_red_o_shell"] and not any(abre.values())
                     and not c_res["venv_tiene_driver_neo4j"] and not din["eventos_de_red"]
                     and all(f == "AF_UNIX" for f in din["familias_de_socket"])
                     and set(din["subprocesos"]) <= SUBPROCESOS_PLATFORM)

    # (d) positivo por el mismo JSON de MCP
    cmd, e = TA.cmd_desde_mcp_json(BANCO_DIR / cfg["brazos"][BRAZO]["mcp_config"],
                                   dict(env, BANCO_LOG_R1=str(OUT / f"log_r1_positivo_{BRAZO}.jsonl"),
                                        BANCO_SESION_TAG=f"aislamiento_positivo_{BRAZO}"))
    with ClienteFalso(cmd, env=e, timeout_s=600) as cli:
        lista = [t["name"] for t in cli.listar_tools()]
        texto = cli.llamar("buscar_pasajes", {"consulta": "efectivo mínimo", "limite": 3})
    obj = json.loads(texto)
    n = len(obj.get("resultados", []))
    d_res = {"mcp_status_en_init": srv, "tools_servidor": lista,
             "llamada": {"tool": "buscar_pasajes", "input": {"consulta": "efectivo mínimo", "limite": 3}},
             "n_resultados": n, "chars": len(texto), "primer_resultado": obj["resultados"][0]["id"] if n else None,
             "fuente_segun_log": meta["servidores_mcp"]["fuente"]}
    d_res["PASS"] = n > 0 and lista == ["buscar_pasajes"] and any(s.get("status") == "connected" for s in srv)

    res = {"generado": datetime.now(timezone.utc).isoformat(timespec="seconds"),
           "unidad": "A2.1, tramo 1 — aislamiento por capacidad de la configuración BM25",
           "modo": "init (USD 0) + cliente falso + corrida auditada", "brazo": BRAZO,
           "config_agentes_a2_1_sha256": sha256_file(L21.CONFIG_A21),
           "a_inventario": a_res, "b_artefactos_grafo": b_res, "c_puerto_neo4j": c_res, "d_positivo": d_res,
           "inventario_persistido": rel_repo(OUT / "init" / f"meta_AISL-{BRAZO}.json"),
           "nota_brazo_del_grafo": "el positivo del brazo del grafo queda para A2.2 (mandato A2.1, §3, punto 4)",
           "PASS": a_res["PASS"] and b_res["PASS"] and c_res["PASS"] and d_res["PASS"]}
    (OUT / "aislamiento_a2_1.json").write_text(json.dumps(res, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for k in ("a_inventario", "b_artefactos_grafo", "c_puerto_neo4j", "d_positivo"):
        print(f"{k}: {'PASS' if res[k]['PASS'] else 'FAIL'}")
    print("TOTAL:", "PASS" if res["PASS"] else "FAIL", "->", rel_repo(OUT / "aislamiento_a2_1.json"))
    return 0 if res["PASS"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
