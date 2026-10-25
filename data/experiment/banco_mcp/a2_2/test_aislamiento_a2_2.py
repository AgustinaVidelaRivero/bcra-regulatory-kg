#!/usr/bin/env python3
"""test_aislamiento_a2_2.py — Aislamiento POR CAPACIDAD de los tres brazos de A2.2 (pre-registro, §2 y §8, punto 3), a USD 0:
modo init del lanzador de A2.2 (ninguna petición llega a la API), el cliente falso del banco y una corrida auditada de cada
servidor. Los mismos criterios (a) a (d) que aislamiento/test_aislamiento.py (U-A2.0-banco) y a2_1/test_aislamiento_a2_1.py
(A2.1, tramo 1), de los que se importan o se copian las piezas, aplicados a la configuración de A2.2:

  (a) inventario: en `system/init`, cada brazo trae solo sus tools (las tres del grafo, o `mcp__fragmentos__buscar_pasajes`),
      ninguna del otro brazo y ninguna built-in; permission mode dontAsk; su servidor connected; el CLI sellado.
  (b) artefactos del otro brazo: el agente no tiene tools de archivos ni de shell; el código de cada servidor no importa módulos
      del otro brazo ni nombra sus artefactos; en los de fragmentos, `import neo4j` falla en su venv; y en la corrida auditada
      ningún servidor importa los módulos ni abre los archivos del otro brazo (el de fragmentos BM25, además, ni el modelo).
  (c) red: el agente no tiene tools de red ni de shell; en la corrida auditada, los servidores de fragmentos no abren ningún
      socket de red (solo el par AF_UNIX del loop de asyncio), y el del grafo se conecta solo a su Neo4j local (puerto 7687).
  (d) positivo por brazo, con el del brazo del grafo: el servidor connected con sus tools en init, y una llamada real por el MISMO
      JSON de MCP que devuelve datos de su fuente (el grafo de desarrollo re-sellado en Neo4j, o los pasajes de su índice).

Los streams de las sesiones init traen el cwd absoluto: quedan fuera del repo, como el de A2.1 (registro, §16, decisión 6). En
a2_2/aislamiento/ van las metas, los comandos, los prompts, los logs R1 y el resumen aislamiento_a2_2.json.

Uso: BANCO_VENV_VECTOR=<venv 3.12> .venv/bin/python -B data/experiment/banco_mcp/a2_2/test_aislamiento_a2_2.py
     [--out <dir>] [--init-dir <dir fuera del repo>]
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
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
import lanzar_agente_a2_2 as L22                                   # noqa: E402
import test_aislamiento as TA                                       # noqa: E402  (U-A2.0-banco: solo import)
from cliente_falso import ClienteFalso                              # noqa: E402
from comun_banco import rel_repo, sha256_file                       # noqa: E402

SONDA = BANCO_DIR / "a2_1" / "sonda_auditoria.py"
MODULOS_GRAFO = {"neo4j", "neo4j_index", "grafos", "conexion", "harness", "loader", "tools_juguete", "agente_v2", "tools_v2"}
MODULOS_FRAGMENTOS = {"servidor_mcp_vector", "bm25_fragmentos", "construir_indice", "sentence_transformers", "torch",
                      "transformers"}
MODULOS_MODELO = {"numpy", "torch", "transformers", "sentence_transformers", "huggingface_hub", "safetensors", "tokenizers"}
RE_SOCKETS = r"\bsocket\b|GraphDatabase|bolt://|:7687|requests\.|urllib|httpx"      # la de test_aislamiento.main (c)
ARTEFACTOS_FRAGMENTOS = ["mcp_vector/indice", "indice_bm25.json", "embeddings_docs.npy", "pasajes.json", "harrier"]
SUBPROCESOS_PLATFORM = {"uname", "file"}
LLAMADAS = {"kg": ("buscar_nodos", [{"consulta": "efectivo mínimo", "limite": 3}, {"consulta": "clasificación de deudores"}]),
            "fragmentos_bm25": ("buscar_pasajes", [{"consulta": "efectivo mínimo", "limite": 3},
                                                   {"consulta": "clasificación de deudores en situación 3"}]),
            "fragmentos_denso": ("buscar_pasajes", [{"consulta": "efectivo mínimo", "limite": 3}])}
CODIGO = {"kg": [BANCO_DIR / "mcp_kg" / "servidor_mcp_kg.py"],
          "fragmentos_bm25": [BANCO_DIR / "mcp_vector" / "servidor_mcp_vector.py", BANCO_DIR / "mcp_vector" / "bm25_fragmentos.py"],
          "fragmentos_denso": [BANCO_DIR / "mcp_vector" / "servidor_mcp_vector.py"]}
INIT_DIR_DEFAULT = L22.LA.BANCO_SESIONES / "aislamiento_a2_2"
# la carpeta personal y las carpetas temporales del sistema (la de /tmp resuelta, la de TMPDIR y la de las carpetas por usuario)
RUTAS_DE_LA_MAQUINA = (str(Path.home()), str(Path("/tmp").resolve()), tempfile.gettempdir(), str(Path("/var/folders")))


def trae_rutas_de_la_maquina(texto: str) -> bool:
    """Si un texto trae la carpeta personal o una carpeta temporal del sistema: no va al repo."""
    return any(r in texto for r in RUTAS_DE_LA_MAQUINA)


def enmascarar(p: str) -> str:
    try:
        return rel_repo(p)
    except Exception:  # noqa: BLE001
        return p


def env_brazo(env: dict, brazo: str, log_r1: Path, tag: str) -> tuple[list[str], dict]:
    cfg = L22.cargar_cfg()
    e = dict(env, BANCO_LOG_R1=str(log_r1), BANCO_SESION_TAG=tag)
    if brazo == "kg":
        e["BANCO_PYTHON_KG"] = L22.python_kg()[0]
    return TA.cmd_desde_mcp_json(BANCO_DIR / cfg["brazos"][brazo]["mcp_config"], e)


def corrida_auditada(env: dict, brazo: str, out: Path) -> dict:
    cmd, e = env_brazo(env, brazo, out / f"log_r1_auditada_{brazo}.jsonl", f"aislamiento_auditada_{brazo}")
    python, servidor, args = cmd[0], cmd[2], cmd[3:]
    tool, llamadas = LLAMADAS[brazo]
    with tempfile.TemporaryDirectory() as td:
        reg = Path(td) / "sonda.json"
        with ClienteFalso([python, "-B", str(SONDA), str(reg), servidor] + args, env=e, timeout_s=900) as cli:
            tools = [t["name"] for t in cli.listar_tools()]
            textos = [cli.llamar(tool, c) for c in llamadas]
        r = json.loads(reg.read_text(encoding="utf-8"))
    importados = set(r["imports"]) | set(r["sys_modules_al_salir"])
    raiz = {m.split(".")[0] for m in importados}
    abiertos = [enmascarar(p) for p in r["open"]]
    otro = MODULOS_FRAGMENTOS if brazo == "kg" else MODULOS_GRAFO
    prohibidos = otro | (MODULOS_MODELO if brazo == "fragmentos_bm25" else set())
    abiertos_otro = ([p for p in abiertos if any(x in p for x in ARTEFACTOS_FRAGMENTOS)] if brazo == "kg" else
                     [p for p in abiertos if any(x in p for x in TA.ARTEFACTOS_GRAFO) or p.endswith("kg.json")])
    abiertos_modelo = [p for p in abiertos if ".cache/huggingface" in p or "harrier" in p or p.endswith((".npy", ".safetensors"))]
    nuevos = [s for s in r["socket"] if s["evento"] == "socket.__new__"]
    red = [s for s in r["socket"] if s["evento"] != "socket.__new__"]
    return {"python_servidor": r["python"], "tools": tools, "n_llamadas": len(textos),
            "n_resultados": [len(json.loads(t).get("resultados", [])) for t in textos],
            "modulos_prohibidos_importados": sorted(raiz & prohibidos), "n_modulos_importados": len(importados),
            "n_archivos_abiertos": len(abiertos),
            "archivos_abiertos_del_repo": sorted({p for p in abiertos if not p.startswith(("/", "~"))}),
            "abiertos_del_otro_brazo": abiertos_otro, "abiertos_del_modelo": abiertos_modelo if brazo == "fragmentos_bm25" else
            f"{len(abiertos_modelo)} (el denso carga su modelo desde la caché local)" if brazo == "fragmentos_denso" else [],
            "sockets_creados": len(nuevos), "familias_de_socket": sorted({s["familia"] for s in nuevos}),
            "eventos_de_red": red, "subprocesos": sorted({x["ejecutable"] for x in r["subprocess"]})}


def red_admitida(brazo: str, din: dict) -> bool:
    if brazo != "kg":
        return not din["eventos_de_red"] and all(f == "AF_UNIX" for f in din["familias_de_socket"])
    # el del grafo: solo su Neo4j local (localhost, 127.0.0.1 o ::1, puerto 7687), y la resolución de localhost
    for ev in din["eventos_de_red"]:
        txt = " ".join(ev.get("args", []))
        if ev["evento"] in ("socket.connect", "socket.connect_ex"):
            if "7687" not in txt or not any(h in txt for h in ("127.0.0.1", "::1", "localhost")):
                return False
        elif ev["evento"] == "socket.getaddrinfo":
            if "localhost" not in txt and "127.0.0.1" not in txt:
                return False
        elif ev["evento"] not in ("socket.bind",):
            return False
    return True


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=AQUI / "aislamiento")
    ap.add_argument("--init-dir", type=Path, default=None, help="dónde corren las sesiones init (fuera del repo)")
    ap.add_argument("--sesiones", type=Path, default=L22.LA.BANCO_SESIONES)
    a = ap.parse_args(argv)
    out = a.out
    init_dir = a.init_dir or (INIT_DIR_DEFAULT / datetime.now().strftime("%Y%m%dT%H%M%S"))
    if init_dir.resolve().is_relative_to(REPO_DIR):
        raise SystemExit("las sesiones init corren fuera del repo")
    out.mkdir(parents=True, exist_ok=True)
    venv_vec = os.environ.get("BANCO_VENV_VECTOR")
    if not venv_vec:
        raise SystemExit("BANCO_VENV_VECTOR no definido")
    env = dict(os.environ, BANCO_REPO=str(REPO_DIR), BANCO_VENV_VECTOR=venv_vec)
    cfg = L22.cargar_cfg()
    tools_de = {b: set(cfg["brazos"][b]["tools_esperadas"]) for b in cfg["brazos"]}
    r_imp = subprocess.run([f"{venv_vec}/bin/python", "-c", "import neo4j"], capture_output=True, text=True)
    res = {"generado": datetime.now(timezone.utc).isoformat(timespec="seconds"),
           "unidad": "A2.2, tramo 1 — aislamiento por capacidad de los tres brazos (§8, punto 3)",
           "modo": "init (USD 0) + cliente falso + corrida auditada", "config_agentes_a2_2_sha256": sha256_file(L22.CONFIG_A22),
           "sesiones_init_fuera_del_repo": enmascarar(str(init_dir)), "brazos": {}}
    (out / "init").mkdir(parents=True, exist_ok=True)
    for b in sorted(cfg["brazos"]):
        pid = f"AISL-{b}"
        meta = L22.lanzar(b, pid, "pregunta de prueba (modo init, sin modelo)", init_dir, modo="init", sesiones=a.sesiones)
        for f in sorted(init_dir.glob(f"*_{pid}*")):
            if f.name.startswith("stream_") or f.name.startswith("sesion_"):
                continue
            texto = f.read_text(encoding="utf-8", errors="replace")
            if trae_rutas_de_la_maquina(texto):
                raise SystemExit(f"{f.name} trae una ruta de la máquina: no va al repo (correr con --init-dir bajo la carpeta "
                                 "personal, o con el de omisión)")
            shutil.copyfile(f, out / "init" / f.name)
        tools = set(meta["inventario_tools_R6"]["tools_en_init"] or [])
        srv = meta["servidores_mcp"]["en_init"] or []
        # el otro brazo: para el grafo, los de fragmentos; para una configuración de fragmentos, el grafo (las dos de
        # fragmentos comparten su tool por diseño: registro, §16, decisión 1)
        otros = set().union(*(tools_de[x] for x in tools_de if (x == "kg") != (b == "kg")))
        a_res = {"tools": sorted(tools), "esperadas": sorted(tools_de[b]), "coincide": tools == tools_de[b],
                 "sin_tools_de_otro_brazo": not (tools & otros),
                 "sin_builtin": not (tools & TA.TOOLS_ARCHIVOS_SHELL_RED) and all(t.startswith("mcp__") for t in tools),
                 "permission_mode": meta["harness_R10"]["permission_mode"], "servidores_en_init": srv,
                 "claude_code_version": meta["harness_R10"]["claude_code_version"],
                 "coincide_con_sellada": meta["harness_R10"]["coincide_con_sellada"]}
        a_res["PASS"] = (a_res["coincide"] and a_res["sin_tools_de_otro_brazo"] and a_res["sin_builtin"]
                         and a_res["permission_mode"] == "dontAsk" and any(s.get("status") == "connected" for s in srv)
                         and a_res["coincide_con_sellada"])
        din = corrida_auditada(env, b, out)
        fuentes = {rel_repo(p): p.read_text(encoding="utf-8") for p in CODIGO[b]}
        imports = sorted({m for t in fuentes.values() for m in re.findall(r"^\s*(?:from|import)\s+([A-Za-z_][\w.]*)", t, flags=re.M)})
        otro_mod = MODULOS_FRAGMENTOS if b == "kg" else MODULOS_GRAFO
        artef = ARTEFACTOS_FRAGMENTOS if b == "kg" else TA.ARTEFACTOS_GRAFO
        menciona = sorted({x for t in fuentes.values() for x in artef if x in t})
        b_res = {"agente_tools_de_archivo_o_shell": sorted(tools & TA.TOOLS_ARCHIVOS_SHELL_RED),
                 "codigo": {k: sha256_file(REPO_DIR / k) for k in fuentes}, "imports_del_codigo": imports,
                 "importa_modulos_del_otro_brazo": sorted({i.split(".")[0] for i in imports} & otro_mod),
                 "menciona_artefactos_del_otro_brazo": menciona,
                 "corrida_auditada": {k: din[k] for k in ("python_servidor", "tools", "n_llamadas", "n_resultados",
                                                          "modulos_prohibidos_importados", "n_modulos_importados",
                                                          "n_archivos_abiertos", "archivos_abiertos_del_repo",
                                                          "abiertos_del_otro_brazo", "abiertos_del_modelo")}}
        if b != "kg":
            b_res["import_neo4j_en_venv"] = {"returncode": r_imp.returncode, "stderr_tail": r_imp.stderr.strip()[-120:]}
        b_res["PASS"] = (not b_res["agente_tools_de_archivo_o_shell"] and not b_res["importa_modulos_del_otro_brazo"]
                         and not menciona and not din["modulos_prohibidos_importados"] and not din["abiertos_del_otro_brazo"]
                         and (b != "fragmentos_bm25" or not din["abiertos_del_modelo"])
                         and (b == "kg" or r_imp.returncode != 0) and all(n > 0 for n in din["n_resultados"]))
        abre = {k: bool(re.search(RE_SOCKETS, t)) for k, t in fuentes.items()}
        c_res = {"agente_tools_de_red_o_shell": sorted(tools & {"Bash", "WebFetch", "WebSearch"}),
                 "codigo_abre_sockets_o_bolt": abre,
                 "corrida_auditada": {k: din[k] for k in ("sockets_creados", "familias_de_socket", "eventos_de_red", "subprocesos")},
                 "subprocesos_admitidos": sorted(SUBPROCESOS_PLATFORM),
                 "regla": ("solo su Neo4j local, 127.0.0.1:7687 (docker-compose.yml del backend del grafo)" if b == "kg" else
                           "ningún socket de red: solo el par AF_UNIX del loop de asyncio")}
        c_res["PASS"] = (not c_res["agente_tools_de_red_o_shell"] and (b == "kg" or not any(abre.values()))
                         and red_admitida(b, din) and set(din["subprocesos"]) <= SUBPROCESOS_PLATFORM)
        tool, llamadas = LLAMADAS[b]
        cmd, e = env_brazo(env, b, out / f"log_r1_positivo_{b}.jsonl", f"aislamiento_positivo_{b}")
        with ClienteFalso(cmd, env=e, timeout_s=900) as cli:
            lista = [t["name"] for t in cli.listar_tools()]
            texto = cli.llamar(tool, llamadas[0])
        obj = json.loads(texto)
        n = len(obj.get("resultados", []))
        log = L22.LA.leer_log_r1(out / f"log_r1_positivo_{b}.jsonl")
        fuente = (log.get("inicio") or {}).get("fuente") or {}
        d_res = {"mcp_status_en_init": srv, "tools_servidor": lista, "llamada": {"tool": tool, "input": llamadas[0]},
                 "n_resultados": n, "chars": len(texto),
                 "primer_resultado": (obj["resultados"][0].get("id") if n else None), "fuente_segun_log": fuente}
        esperada = {"kg": ["buscar_nodos", "ver_nodo", "ver_vecinos"]}.get(b, ["buscar_pasajes"])
        d_res["PASS"] = (n > 0 and sorted(lista) == esperada and any(s.get("status") == "connected" for s in srv)
                         and (b != "kg" or fuente.get("kg_sha256") == "acb26dca0885e9ea83ab02637f15c1dac57885f0cf017c5fb16173ac7dfcac31"))
        res["brazos"][b] = {"a_inventario": a_res, "b_artefactos_del_otro_brazo": b_res, "c_red": c_res, "d_positivo": d_res,
                            "PASS": all(x["PASS"] for x in (a_res, b_res, c_res, d_res))}
        print(f"{b}: (a) {'PASS' if a_res['PASS'] else 'FAIL'} | (b) {'PASS' if b_res['PASS'] else 'FAIL'} | "
              f"(c) {'PASS' if c_res['PASS'] else 'FAIL'} | (d) {'PASS' if d_res['PASS'] else 'FAIL'}", flush=True)
    res["PASS"] = all(v["PASS"] for v in res["brazos"].values())
    for f in out.glob("log_r1_*.jsonl"):
        if trae_rutas_de_la_maquina(f.read_text(encoding="utf-8", errors="replace")):
            raise SystemExit(f"{f.name} trae una ruta de la máquina")
    texto = json.dumps(res, ensure_ascii=False, indent=2) + "\n"
    if trae_rutas_de_la_maquina(texto):
        raise SystemExit("aislamiento_a2_2.json traería una ruta de la máquina")
    (out / "aislamiento_a2_2.json").write_text(texto, encoding="utf-8")
    print("TOTAL:", "PASS" if res["PASS"] else "FAIL", "->", rel_repo(out / "aislamiento_a2_2.json"))
    return 0 if res["PASS"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
