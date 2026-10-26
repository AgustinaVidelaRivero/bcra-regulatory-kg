#!/usr/bin/env python3
"""test_aislamiento_paralelo.py — El aislamiento entre sesiones y entre brazos sobre el lanzador en paralelo
(U-BANCO-PARALELO, punto 4.b; registro de decisiones, §52, §53, §85 y §88). USD 0: modo init (ninguna petición llega a
la API) más el cliente falso.

Las sesiones son las de N6 y B6.3 con la configuración de prueba de los brazos de N6 (paralelo/config_agentes_n6_prueba.json):
el grafo con el servidor de navegación (mcp_kg/mcp_kg_nav.json) y fragmentos del acumulado, BM25 e híbrida.

  1. Lo compartido de solo lectura, antes: el sha256 del kg.json del acumulado, de cada archivo de los índices que usan
     las sesiones (el índice por punto y los de fragmentos), del `pip freeze` del venv de fragmentos, y la base Neo4j
     (KG_Meta, cuentas y la huella de cargar_kg.huella_neo4j).
  2. Un lote de 9 sesiones en modo init con P = 3, por agentes/lanzar_lote_paralelo.py, en tres tandas con sesiones del
     grafo y de fragmentos a la vez. Por sesión, los cuatro controles de hoy (test_aislamiento.py): (a) el inventario de
     system/init, (b) sin tools de archivos ni código del grafo en fragmentos, (c) sin red ni driver en fragmentos, (d)
     el servidor `connected` y una llamada real por su JSON (punto 3); y los nuevos: un proceso de servidor MCP por sesión
     (pid distinto, del log R1), un log R1 con solo lo suyo y su mapa R7 contra su stream, ningún archivo de una sesión en
     otra, una carpeta de configuración por sesión, distinta y fuera del repo y de git, el cwd compartido vacío después de
     cada tanda y al final, la superposición de horas de cada tanda en el registro del lote, el entorno de cada brazo por
     nombre y NEO4J_URI en el servidor del grafo de cada sesión (su log R1: backend neo4j y el KG_Meta del acumulado).
  3. En ejecución, con las mismas tres tandas: los servidores de las sesiones de cada tanda vivos a la vez, cada uno por su
     JSON de MCP con el entorno de su sesión (N6.env_sesion) y su log R1. Mientras el servidor del grafo de la sesión de
     al lado responde una llamada real, el de fragmentos responde las suyas, y después de cada llamada `lsof` sobre el pid
     de ese servidor y sus hijos: ninguna conexión al puerto de Neo4j (el de NEO4J_URI de la sesión del grafo, y el 7687
     por defecto de conexion.py), ningún archivo abierto bajo el kg.json, data/experiment/neo4j/ ni mcp_kg/indice_puntos/,
     ningún descriptor de un codificador de consultas del grafo y ningún proceso hijo de un servidor del grafo. Cada
     sesión del grafo, con su codificador (hijo de su servidor, pid distinto), su conexión a NEO4J_URI y ningún archivo
     de mcp_vector/indice/ abierto. Después, cada log R1 con solo sus llamadas, de las tools de su brazo, contra lo que
     pidió y recibió el cliente.
  4. El control negativo, que tiene que fallar: una copia, en --tmp, de la configuración de fragmentos con el servidor del
     grafo agregado (el control 1 la marca), y un proceso de prueba propio con un socket al puerto de Neo4j y el kg.json
     abierto (el control 2 lo detecta). Si alguno no falla, el test no vale.
  5. Lo compartido, después: igual a lo de antes.

Ninguna salida de tool se imprime ni se escribe en el resultado: van por sha256 y por cuentas. La espera es la del padre
sobre sus hijos y la del cliente falso sobre sus llamadas: sin sleep.

Uso: NEO4J_URI=bolt://127.0.0.1:37687 BANCO_VENV_VECTOR=<venv> .venv/bin/python -B test_aislamiento_paralelo.py \\
       --out <dir> --sesiones <dir> --tmp <dir> --resultado <json>
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import threading
import time
from pathlib import Path
from urllib.parse import urlparse

AQUI = Path(__file__).resolve().parent
BANCO_DIR = AQUI.parent
for _p in (str(BANCO_DIR), str(AQUI), str(BANCO_DIR / "agentes"), str(BANCO_DIR / "paralelo")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import lanzar_agente as LA                              # noqa: E402
import guardas_lote as G                                # noqa: E402
import lanzar_agente_n6_prueba as N6                    # noqa: E402
import control_neo4j_propio as CN                       # noqa: E402
import test_aislamiento as BASE                         # noqa: E402  (expandir, cmd_desde_mcp_json y las listas de (a) a (c))
import testigo_aislamiento as TES                       # noqa: E402  (el testigo: agregado al punto 4.b, criterio 13)
from cliente_falso import ClienteFalso                  # noqa: E402
from comun_banco import rel_repo, sha256_file           # noqa: E402

REPO_DIR = LA.REPO_DIR
CFG = N6.cargar_cfg()
FRAG = ("fragmentos_bm25", "fragmentos_hibrida")
KG_JSON = REPO_DIR / "data/experiment/tanda1/t3/acumulado/ens_treinta_r2b_sincola/r2/kg.json"
RUTAS_GRAFO = [KG_JSON, REPO_DIR / "data/experiment/neo4j", BANCO_DIR / "mcp_kg" / "indice_puntos"]
RUTAS_INDICES_FRAG = [BANCO_DIR / "mcp_vector" / "indice"]
INDICES_USADOS = [BANCO_DIR / "mcp_kg/indice_puntos/KG_Acumulado_Tandas0y1_r2b_sincola",
                  BANCO_DIR / "mcp_vector/indice/e0_acumulado_30tos_bm25", BANCO_DIR / "mcp_vector/indice/e0_acumulado_30tos_denso"]
PUERTO_DEFECTO = 7687                                     # conexion.py: bolt://localhost:7687
CODIGO_FRAG = ["mcp_vector/servidor_mcp_vector.py", "mcp_vector/bm25_fragmentos.py"]
TANDAS = [["kg", "fragmentos_bm25", "kg"], ["fragmentos_hibrida", "kg", "fragmentos_bm25"], ["kg", "fragmentos_hibrida", "kg"]]
CONSULTAS = ["efectivo mínimo", "plazo fijo", "tasa de interés"]


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


# --------------------------------------------------------------------------------------------------------------------- #
# Lo compartido de solo lectura                                                                                         #
# --------------------------------------------------------------------------------------------------------------------- #
def compartido() -> dict:
    archivos = {rel_repo(KG_JSON): sha256_file(KG_JSON)}
    for d in INDICES_USADOS:
        for p in sorted(d.iterdir()):
            if p.is_file():
                archivos[rel_repo(p)] = sha256_file(p)
    venv = os.environ["BANCO_VENV_VECTOR"]
    freeze = subprocess.run([f"{venv}/bin/python", "-m", "pip", "freeze"], capture_output=True, text=True).stdout
    return {"archivos": archivos, "pip_freeze_venv_fragmentos_sha256": sha(freeze.encode()),
            "neo4j": CN.estado(con_huella=True)}


# --------------------------------------------------------------------------------------------------------------------- #
# lsof y la tabla de procesos (por pid; nunca el entorno)                                                              #
# --------------------------------------------------------------------------------------------------------------------- #
def lsof(pids: list[int]) -> list[dict]:
    """Los descriptores abiertos de esos pids: [{pid, comando, fd, tipo, dispositivo, nombre}], de `lsof -F`."""
    if not pids:
        return []
    out = subprocess.run(["lsof", "-nP", "-p", ",".join(map(str, pids)), "-F", "pcftdn"], capture_output=True,
                         text=True).stdout
    filas, pid, cmd, cur = [], None, None, None
    for l in out.splitlines():
        k, v = l[:1], l[1:]
        if k == "p":
            pid, cur = int(v), None
        elif k == "c":
            cmd = v
        elif k == "f":
            cur = {"pid": pid, "comando": cmd, "fd": v, "tipo": None, "dispositivo": None, "nombre": None}
            filas.append(cur)
        elif cur is not None and k == "t":
            cur["tipo"] = v
        elif cur is not None and k == "d":
            cur["dispositivo"] = v
        elif cur is not None and k == "n":
            cur["nombre"] = v
    return filas


def arbol(pid: int) -> list[int]:
    t = G.tabla_procesos()
    return [pid] + sorted(G.descendientes(pid, t))


def bajo(nombre: str | None, rutas: list[Path]) -> bool:
    if not nombre or not nombre.startswith("/"):
        return False
    try:
        p = Path(nombre).resolve()
    except OSError:
        return False
    return any(p == r.resolve() or p.is_relative_to(r.resolve()) for r in rutas)


def tubos_de(pids: list[int]) -> tuple[set, set]:
    """(direcciones propias, direcciones del otro extremo) de los pipes y sockets unix de esos pids."""
    propias, otras = set(), set()
    for f in lsof(pids):
        if f["tipo"] in ("PIPE", "unix"):
            if f["dispositivo"]:
                propias.add(f["dispositivo"])
            if f["nombre"] and f["nombre"].startswith("->"):
                otras.add(f["nombre"][2:])
    return propias, otras


def descriptores_de_codificador(fds: list[dict], codificadores: list[int]) -> list[str]:
    """Los descriptores de `fds` que son un extremo de un pipe o socket unix de un codificador (su mismo extremo o el
    otro): por la dirección propia (campo d de lsof) y la del otro extremo (campo n, «->0x…»)."""
    if not codificadores:
        return []
    propias, otras = tubos_de(codificadores)
    return [f"{f['pid']}:{f['fd']}" for f in fds if f["tipo"] in ("PIPE", "unix") and f["pid"] not in codificadores
            and (f["dispositivo"] in otras or f["dispositivo"] in propias or (f["nombre"] or "").removeprefix("->") in propias)]


def control_2(pid: int, puertos: set[int], servidores_grafo: set[int], codificadores: list[int]) -> dict:
    """El control 2 sobre un proceso de fragmentos y sus hijos: ninguna conexión a los puertos de Neo4j, ningún archivo
    bajo los del grafo, ningún descriptor de un codificador del grafo y ningún proceso hijo de un servidor del grafo."""
    pids = arbol(pid)
    fds = lsof(pids)
    tcp = [f["nombre"] for f in fds if f["tipo"] in ("IPv4", "IPv6") and f["nombre"]
           and any(re.search(rf"(->|^)[^ ]*:{p}\b", f["nombre"]) for p in puertos)]
    archivos = [f["nombre"] for f in fds if bajo(f["nombre"], RUTAS_GRAFO)]
    desc_cod = descriptores_de_codificador(fds, codificadores)
    t = G.tabla_procesos()
    hijos_de_grafo = [q for q in pids if G.ancestros(q, t) & servidores_grafo]
    return {"pids": pids, "n_descriptores": len(fds), "conexiones_a_neo4j": tcp, "archivos_del_grafo": archivos,
            "descriptores_de_un_codificador": desc_cod, "procesos_hijos_de_un_servidor_del_grafo": hijos_de_grafo,
            "PASS": not tcp and not archivos and not desc_cod and not hijos_de_grafo}


def control_grafo(pid: int, puerto: int) -> dict:
    """El lado del grafo: su conexión al Neo4j de NEO4J_URI, su codificador hijo y ningún archivo de los índices de
    fragmentos abierto (él y sus hijos)."""
    pids = arbol(pid)
    t = G.tabla_procesos()
    fds = lsof(pids)
    cod = [q for q in pids if q in t and t[q][0] == pid and "codificador_consultas.py" in t[q][1]]
    conex = [f["nombre"] for f in fds if f["pid"] == pid and f["tipo"] in ("IPv4", "IPv6")
             and re.search(rf"->[^ ]*:{puerto}\b", f["nombre"] or "")]
    a_7687 = [f["nombre"] for f in fds if f["tipo"] in ("IPv4", "IPv6") and re.search(rf"->[^ ]*:{PUERTO_DEFECTO}\b", f["nombre"] or "")]
    frag = [f["nombre"] for f in fds if bajo(f["nombre"], RUTAS_INDICES_FRAG)]
    return {"pids": pids, "codificador": cod, "conexiones_a_NEO4J_URI": len(conex), "conexiones_al_7687": a_7687,
            "archivos_de_los_indices_de_fragmentos": frag,
            "PASS": len(cod) == 1 and len(conex) >= 1 and not a_7687 and not frag}


# --------------------------------------------------------------------------------------------------------------------- #
# Fase de init: el lote por el lanzador en paralelo                                                                    #
# --------------------------------------------------------------------------------------------------------------------- #
def lote_init(out: Path, sesiones: Path) -> tuple[dict, list[dict]]:
    ses = []
    for t, brazos in enumerate(TANDAS, 1):
        for b in brazos:
            ses.append({"id": f"AISL-{len(ses) + 1:02d}-{b}", "brazo": b, "bloque": f"T{t}",
                        "pregunta": "pregunta de prueba (modo init, sin modelo)"})
    lote = out / "lote_init.json"
    lote.parent.mkdir(parents=True, exist_ok=True)
    lote.write_text(json.dumps({"sesiones": ses}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    consola = open(out / "consola_lote_init.txt", "w", encoding="utf-8")
    p = subprocess.Popen([sys.executable, "-B", str(BANCO_DIR / "agentes" / "lanzar_lote_paralelo.py"), "--lote", str(lote),
                          "--out", str(out / "init"), "--sesiones", str(sesiones), "-P", "3", "--modo", "init",
                          "--tope", "0", "--freno", "0", "--lanzador", "paralelo/lanzar_agente_n6_prueba.py"],
                         stdout=consola, stderr=subprocess.STDOUT)
    puertos = sorted({urlparse(os.environ["NEO4J_URI"]).port, PUERTO_DEFECTO})
    observadas, muestras = {}, 0
    while p.poll() is None:                       # mientras corre el lote: quién de cada sesión se conecta a Neo4j
        muestras += 1
        for pid, puerto_remoto in conexiones_neo4j(puertos):
            i, srv = sesion_de(pid, p.pid)
            if i is not None:
                o = observadas.setdefault(i, {"puertos_remotos": set(), "procesos": set()})
                o["puertos_remotos"].add(puerto_remoto)
                o["procesos"].add(srv)
    consola.close()
    reg = json.loads((out / "init" / "registro_lote.json").read_text(encoding="utf-8"))
    reg["_rc"] = p.returncode
    reg["_conexiones"] = {"muestras_de_lsof": muestras, "puertos": puertos,
                          "por_sesion": {i: {k: sorted(v) for k, v in o.items()} for i, o in observadas.items()}}
    return reg, ses


def conexiones_neo4j(puertos: list[int]) -> list[tuple[int, int]]:
    """(pid, puerto remoto) de las conexiones TCP establecidas a esos puertos (lsof -i, solo esos puertos)."""
    args = ["lsof", "-nP", "-sTCP:ESTABLISHED", "-F", "pcn"] + [f"-iTCP:{q}" for q in puertos]
    out, pid, res = subprocess.run(args, capture_output=True, text=True).stdout, None, []
    for l in out.splitlines():
        if l[:1] == "p":
            pid = int(l[1:])
        elif l[:1] == "n" and "->" in l:
            remoto = l[1:].split("->", 1)[1]
            try:
                q = int(remoto.rsplit(":", 1)[1])
            except ValueError:
                continue
            if q in puertos:
                res.append((pid, q))
    return res


_SESION_DE: dict[int, tuple] = {}


def sesion_de(pid: int, lote_pid: int) -> tuple[str | None, str | None]:
    """La sesión del lote a la que pertenece un proceso (por el `--id` del lanzador de la sesión entre sus ancestros) y
    qué es (el servidor del grafo, el de fragmentos, el codificador u otro). Lee solo `ps ... args=` (sin el entorno)."""
    if pid in _SESION_DE:
        return _SESION_DE[pid]
    t = G.tabla_procesos()
    cadena = sorted(G.ancestros(pid, t))
    if lote_pid not in cadena:
        _SESION_DE[pid] = (None, None)
        return _SESION_DE[pid]
    i = next((m.group(1) for q in cadena if "lanzar_agente_n6_prueba.py" in t[q][1]
              for m in [re.search(r"--id (\S+)", t[q][1])] if m), None)
    a = t.get(pid, (0, ""))[1]
    srv = ("servidor del grafo" if "servidor_mcp_kg_nav.py" in a else "servidor de fragmentos" if "servidor_mcp_vector.py" in a
           else "codificador" if "codificador_consultas.py" in a else "otro")
    _SESION_DE[pid] = (i, srv)
    return _SESION_DE[pid]


def leer_sesion(out: Path, i: str) -> dict:
    d = out / "init" / i
    m = json.loads((d / f"meta_{i}.json").read_text(encoding="utf-8"))
    c = json.loads((d / f"comando_{i}.json").read_text(encoding="utf-8"))
    log = [json.loads(x) for x in (d / f"log_r1_{i}.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
    stream = LA.parsear_stream((d / f"stream_{i}.jsonl").read_text(encoding="utf-8").splitlines())
    return {"meta": m, "comando": c, "log": log, "stream": stream, "dir": d}


def control_a(s: dict, brazo: str) -> dict:
    tools = set(s["meta"]["inventario_tools_R6"]["tools_en_init"] or [])
    esperadas = set(CFG["brazos"][brazo]["tools_esperadas"])
    otras = set().union(*(set(CFG["brazos"][b]["tools_esperadas"]) for b in CFG["brazos"] if b != brazo
                          and CFG["brazos"][b]["servidor"] != CFG["brazos"][brazo]["servidor"]))
    r = {"tools": sorted(tools), "coincide_con_esperadas": tools == esperadas, "tools_del_otro_brazo": sorted(tools & otras),
         "builtin": sorted(t for t in tools if t in BASE.TOOLS_ARCHIVOS_SHELL_RED or not t.startswith("mcp__")),
         "permission_mode": s["meta"]["harness_R10"]["permission_mode"],
         "servidores": s["meta"]["servidores_mcp"]["en_init"]}
    r["PASS"] = (r["coincide_con_esperadas"] and not r["tools_del_otro_brazo"] and not r["builtin"]
                 and r["permission_mode"] == "dontAsk" and bool(r["servidores"])
                 and all(x.get("status") == "connected" for x in r["servidores"]))
    return r


def controles_estaticos_fragmentos() -> dict:
    """(b) y (c) de test_aislamiento.py sobre el código de los dos servidores de fragmentos y su venv."""
    venv = os.environ["BANCO_VENV_VECTOR"]
    codigo = {r: (BANCO_DIR / r).read_text(encoding="utf-8") for r in CODIGO_FRAG}
    imports = sorted({i for t in codigo.values() for i in re.findall(r"^\s*(?:from|import)\s+([A-Za-z_][\w.]*)", t, flags=re.M)})
    modulos_grafo = {"neo4j", "neo4j_index", "grafos", "conexion", "harness", "loader", "tools_juguete", "agente_v2",
                     "tools_v2", "familias_nav", "indice_puntos", "servidor_mcp_kg", "servidor_mcp_kg_nav", "codificador_consultas"}
    r_imp = subprocess.run([f"{venv}/bin/python", "-c", "import neo4j"], capture_output=True, text=True)
    menciona = sorted({x for x in BASE.ARTEFACTOS_GRAFO + ["indice_puntos", "kg.json"] for t in codigo.values() if x in t})
    sockets = {r: bool(re.search(r"\bsocket\b|GraphDatabase|bolt://|:7687|requests\.|urllib|httpx", t)) for r, t in codigo.items()}
    return {"codigo": CODIGO_FRAG, "imports": imports,
            "importa_modulos_del_grafo": sorted({i.split(".")[0] for i in imports} & modulos_grafo),
            "menciona_artefactos_del_grafo": menciona,
            "import_neo4j_en_el_venv_de_fragmentos": {"returncode": r_imp.returncode,
                                                       "error": (r_imp.stderr.strip().splitlines() or [""])[-1][-80:]},
            "codigo_abre_sockets_o_bolt": sockets,
            "b_PASS": not ({i.split(".")[0] for i in imports} & modulos_grafo) and not menciona and r_imp.returncode != 0,
            "c_PASS": not any(sockets.values()) and r_imp.returncode != 0}


def fase_init(a, comp_antes: dict) -> dict:
    reg, ses = lote_init(a.out, a.sesiones)
    ids = [s["id"] for s in ses]
    datos = {i: leer_sesion(a.out, i) for i in ids}
    est = controles_estaticos_fragmentos()
    por_sesion, pids_srv, cfgs = {}, {}, {}
    for s in ses:
        i, b = s["id"], s["brazo"]
        d = datos[i]
        log, m, c = d["log"], d["meta"], d["comando"]
        ini = next((x for x in log if x["evento"] == "inicio"), {})
        fin = next((x for x in log if x["evento"] == "fin"), {})
        pids_srv[i] = ini.get("pid")
        cfg = c["env_declarado"]["CLAUDE_CONFIG_DIR"]
        cfgs[i] = cfg
        usos, _ = LA.tool_calls_de(d["stream"]["mensajes"])
        otros_ids = [j for j in ids if j != i]
        nombres_out = [p.name for p in d["dir"].rglob("*")]
        cfg_dir = Path.home() / cfg[2:] if cfg.startswith("~/") else REPO_DIR / cfg
        nombres_cfg = [str(p.relative_to(cfg_dir)) for p in cfg_dir.rglob("*")] if cfg_dir.exists() else []
        sids_otros = [datos[j]["comando"]["session_id"] for j in otros_ids]
        entorno = c["env_declarado"]["entorno_de_la_sesion"]
        r = {"brazo": b, "a_inventario": control_a(d, b),
             "servidor_pid": ini.get("pid"), "servidor_pid_en_fin": fin.get("pid"),
             "log_r1": {"tags": sorted({x["sesion_tag"] for x in log if "sesion_tag" in x}), "servidor": ini.get("servidor"),
                        "eventos": [x["evento"] for x in log], "n_llamadas": sum(x["evento"] == "llamada" for x in log),
                        "pids_en_sus_lineas": sorted({x["pid"] for x in log if "pid" in x}),
                        "tool_use_mcp_en_el_stream": len([u for u in usos if str(u["name"]).startswith("mcp__")]),
                        "mapa_R7": m["mapa_R7"]},
             "archivos": {"n_en_su_salida": len(nombres_out), "todos_con_su_id": all(i in n for n in nombres_out),
                          "con_el_id_de_otra": [n for n in nombres_out for j in otros_ids if j in n],
                          "n_en_su_carpeta_de_configuracion": len(nombres_cfg),
                          "con_el_session_id_de_otra": [n for n in nombres_cfg for x in sids_otros if x in n],
                          "log_r1_propio": c["env_declarado"]["BANCO_LOG_R1"].endswith(f"{i}/log_r1_{i}.jsonl")},
             "carpeta_configuracion": cfg,
             "entorno_nombres": sorted(entorno.keys()),
             "NEO4J_URI": entorno.get("NEO4J_URI")}
        esp_srv = "mcp_kg" if b == "kg" else "mcp_vector"
        r["log_r1"]["PASS"] = (r["log_r1"]["tags"] == [i] and r["log_r1"]["servidor"] == esp_srv
                               and r["log_r1"]["eventos"][0] == "inicio" and "fin" in r["log_r1"]["eventos"]
                               and r["log_r1"]["n_llamadas"] == r["log_r1"]["tool_use_mcp_en_el_stream"] == len(m["mapa_R7"]) == 0
                               and r["servidor_pid"] == r["servidor_pid_en_fin"]
                               and r["log_r1"]["pids_en_sus_lineas"] == [r["servidor_pid"]])
        r["archivos"]["PASS"] = (r["archivos"]["todos_con_su_id"] and not r["archivos"]["con_el_id_de_otra"]
                                 and not r["archivos"]["con_el_session_id_de_otra"] and r["archivos"]["log_r1_propio"])
        obs = reg["_conexiones"]["por_sesion"].get(i, {"puertos_remotos": [], "procesos": []})
        r["conexiones_a_neo4j_observadas"] = obs
        if b == "kg":
            fu = ini.get("fuente") or {}
            r["neo4j_en_el_servidor"] = {"backend": fu.get("backend"), "kg_meta_sha256": fu.get("kg_meta_sha256"),
                                         "PASS": fu.get("backend") == "neo4j"
                                         and fu.get("kg_meta_sha256") == CFG_GRAFO["kg_sha256_esperado"]
                                         and entorno.get("NEO4J_URI") == os.environ["NEO4J_URI"]
                                         and obs["puertos_remotos"] == [urlparse(os.environ["NEO4J_URI"]).port]
                                         and obs["procesos"] == ["servidor del grafo"]}
        else:
            neo_otros = sorted(k for k in entorno if k != "NEO4J_URI" and ("NEO4J" in k or "KG" in k.split("_") or "INDICE" in k))
            r["fragmentos"] = {"1_inventario_sin_grafo_ni_archivos_shell_red": r["a_inventario"]["PASS"],
                               "2_init_sin_conexiones_a_neo4j_observadas": not obs["puertos_remotos"],
                               "3_log_r1_solo_de_su_brazo": r["log_r1"]["PASS"],
                               "4_venv_sin_driver_y_codigo_sin_sockets": est["c_PASS"],
                               "5_variables_de_neo4j_o_del_grafo_ademas_de_NEO4J_URI": neo_otros}
        por_sesion[i] = r
    # entre sesiones
    pids = [p for p in pids_srv.values() if p]
    distintos_pid = len(set(pids)) == len(pids) == len(ids)
    cfg_vals = list(cfgs.values())
    cfg_abs = [(Path.home() / x[2:] if x.startswith("~/") else REPO_DIR / x).resolve() for x in cfg_vals]
    real_repo = (Path.home() / "INGENIERIA IA" / "TESIS" / "bcra-regulatory-kg").resolve()
    cfg_ok = (len(set(cfg_vals)) == len(cfg_vals)
              and all(not p.is_relative_to(REPO_DIR) and not p.is_relative_to(real_repo) and LA.dentro_de_git(p) is None
                      for p in cfg_abs))
    cwd_eventos = [e for e in reg["eventos"] if e["evento"] == "control del cwd compartido"]
    cwd_ahora = [str(p.relative_to(a.sesiones / "cwd")) for p in (a.sesiones / "cwd").rglob("*")]
    tandas = {}
    for t in range(1, len(TANDAS) + 1):
        de_t = [s["id"] for s in reg["sesiones"] if s["tanda"] == t]
        sup = [x for x in reg["superposiciones"] if x["a"] in de_t and x["b"] in de_t
               and "kg" in x["brazos"] and any(b.startswith("fragmentos") for b in x["brazos"])]
        tandas[t] = {"sesiones": de_t, "superposiciones_grafo_fragmentos": [{k: x[k] for k in ("a", "b", "segundos")} for x in sup],
                     "PASS": bool(sup)}
    entorno_por_brazo = {}
    for i, r in por_sesion.items():
        entorno_por_brazo.setdefault(r["brazo"], set()).update(r["entorno_nombres"])
    escuchan = {p: bool(subprocess.run(["lsof", "-nP", f"-iTCP:{p}", "-sTCP:LISTEN"], capture_output=True, text=True).stdout.strip())
                for p in (7474, 7687, 37474, 37687)}
    res = {"conexiones_observadas_durante_el_lote": reg["_conexiones"],
           "registro_del_lote": {"rc": reg["_rc"], "codigo": reg["codigo"], "P": reg["P"], "modo": reg["modo"],
                                 "estados": {e: sum(1 for s in reg["sesiones"] if s["estado"] == e)
                                             for e in {s["estado"] for s in reg["sesiones"]}},
                                 "workers": {s["id"]: s.get("worker") for s in reg["sesiones"]},
                                 "horas": {s["id"]: [s.get("inicio"), s.get("fin")] for s in reg["sesiones"]},
                                 "orden_de_fin": reg["orden_de_fin"]},
           "estaticos_fragmentos_b_c": est, "por_sesion": por_sesion,
           "servidor_un_proceso_por_sesion": {"pids": pids_srv, "PASS": distintos_pid},
           "carpetas_de_configuracion": {"distintas_y_fuera_del_repo_y_de_git": cfg_ok, "n": len(cfg_vals)},
           "cwd_compartido": {"controles_del_lote": [{"cuando": e["cuando"], "vacio": e["vacio"]} for e in cwd_eventos],
                              "contenido_al_final_del_test": cwd_ahora,
                              "PASS": bool(cwd_eventos) and all(e["vacio"] for e in cwd_eventos) and not cwd_ahora},
           "tandas_superposicion_grafo_fragmentos": tandas,
           "entorno_por_brazo_nombres": {b: sorted(v) for b, v in entorno_por_brazo.items()},
           "NEO4J_URI_valor": os.environ["NEO4J_URI"],
           "puertos_que_escuchan_durante_el_test": escuchan}
    res["PASS"] = (reg["_rc"] == 0 and all(r["a_inventario"]["PASS"] and r["log_r1"]["PASS"] and r["archivos"]["PASS"]
                                          for r in por_sesion.values())
                   and all(r["neo4j_en_el_servidor"]["PASS"] for r in por_sesion.values() if r["brazo"] == "kg")
                   and all(not r["fragmentos"]["5_variables_de_neo4j_o_del_grafo_ademas_de_NEO4J_URI"]
                           and r["fragmentos"]["2_init_sin_conexiones_a_neo4j_observadas"]
                           for r in por_sesion.values() if r["brazo"] != "kg")
                   and est["b_PASS"] and est["c_PASS"] and distintos_pid and cfg_ok and res["cwd_compartido"]["PASS"]
                   and all(t["PASS"] for t in tandas.values()))
    return res


# --------------------------------------------------------------------------------------------------------------------- #
# Fase en ejecución                                                                                                     #
# --------------------------------------------------------------------------------------------------------------------- #
class Servidor:
    def __init__(self, sid: str, brazo: str, out: Path):
        self.sid, self.brazo = sid, brazo
        self.log = (out / f"log_r1_{sid}.jsonl").resolve()
        env_s, _ = N6.env_sesion(CFG, brazo, "api", self.log, sid, "init", None)
        self.env_sesion = env_s
        cmd, e = BASE.cmd_desde_mcp_json(BANCO_DIR / CFG["brazos"][brazo]["mcp_config"], env_s)
        antes = G.descendientes(os.getpid(), G.tabla_procesos())
        self.cli = ClienteFalso(cmd, env=env_s | e, timeout_s=900)
        self.cli.__enter__()
        t = G.tabla_procesos()                       # una sola foto: el `ps` de la anterior ya no está
        nuevos = G.descendientes(os.getpid(), t) - antes
        self.pid = next(q for q in nuevos if t[q][0] == os.getpid() and "servidor_mcp" in t[q][1])
        self.llamadas = []

    def llamar(self, tool: str, args: dict) -> dict:
        t0 = time.time()
        texto = self.cli.llamar(tool, args)
        t1 = time.time()
        self.llamadas.append({"tool": tool, "input": args, "output_sha256": sha(texto.encode("utf-8")), "t0": t0, "t1": t1})
        return self.llamadas[-1]

    def cerrar(self):
        self.cli.__exit__(None, None, None)


def fase_ejecucion(a) -> dict:
    out = a.out / "ejecucion"
    out.mkdir(parents=True, exist_ok=True)
    puerto = urlparse(os.environ["NEO4J_URI"]).port
    puertos = {puerto, PUERTO_DEFECTO}
    res, codificadores_vistos = {"puertos_vigilados": sorted(puertos), "tandas": {}}, {}
    for t, brazos in enumerate(TANDAS, 1):
        srv = [Servidor(f"EJEC-T{t}-{k + 1}-{b}", b, out) for k, b in enumerate(brazos)]
        grafo = [s for s in srv if s.brazo == "kg"]
        frag = [s for s in srv if s.brazo != "kg"]
        pids_grafo = {s.pid for s in grafo}
        cods = {}
        for g in grafo:
            tt = G.tabla_procesos()
            cods[g.sid] = [q for q in G.descendientes(g.pid, tt) if "codificador_consultas.py" in tt[q][1]]
        todos_cods = [q for v in cods.values() for q in v]
        rondas = []
        for ronda, (tool_g, args_g) in enumerate([("buscar_puntos", {"consulta": CONSULTAS[t - 1], "limite": 3}),
                                                  ("buscar_nodos", {"consulta": CONSULTAS[t - 1], "limite": 3})], 1):
            hilos = []
            for g in grafo:
                h = threading.Thread(target=g.llamar, args=(tool_g, args_g))
                h.start()
                hilos.append(h)
            controles = []
            t_ronda = time.time()

            def de_fragmentos(f):
                # sus llamadas, cada una seguida del control 2 sobre su servidor y sus hijos
                for q in (CONSULTAS[t - 1], CONSULTAS[t - 1] + " requisitos"):
                    ll = f.llamar("buscar_pasajes", {"consulta": q, "limite": 3})
                    controles.append({"sesion": f.sid, "llamada": len(f.llamadas), "_t": (ll["t0"], ll["t1"]),
                                      "control_2": control_2(f.pid, puertos, pids_grafo, todos_cods)})
            for f in frag:
                h = threading.Thread(target=de_fragmentos, args=(f,))
                h.start()
                hilos.append(h)
            for h in hilos:
                h.join()
            # a la vez: el intervalo de la llamada de fragmentos se superpone con el de la llamada del grafo de la ronda
            del_grafo = {g.sid: g.llamadas[-1] for g in grafo}
            for c in controles:
                t0, t1 = c.pop("_t")
                c["llamada_s"] = [round(t0 - t_ronda, 3), round(t1 - t_ronda, 3)]
                c["grafo_respondiendo_a_la_vez"] = [sid for sid, g in del_grafo.items() if max(g["t0"], t0) < min(g["t1"], t1)]
            llamadas_grafo_s = {sid: [round(g["t0"] - t_ronda, 3), round(g["t1"] - t_ronda, 3)] for sid, g in del_grafo.items()}
            lado_grafo = {g.sid: control_grafo(g.pid, puerto) | {
                "control_positivo_descriptor_de_su_codificador": len(descriptores_de_codificador(lsof([g.pid]), cods[g.sid]))}
                for g in grafo}
            rondas.append({"ronda": ronda, "tool_del_grafo": tool_g, "llamadas_del_grafo_s": llamadas_grafo_s,
                           "fragmentos": controles, "grafo": lado_grafo})
        for s in srv:
            s.cerrar()
        logs = {}
        for s in srv:
            lineas = [json.loads(x) for x in s.log.read_text(encoding="utf-8").splitlines() if x.strip()]
            ll = [x for x in lineas if x["evento"] == "llamada"]
            mapa = [{"n": k + 1, "tool": c["tool"], "coincide": (k < len(ll) and ll[k]["tool"] == c["tool"]
                                                                and ll[k]["input"] == c["input"]
                                                                and ll[k]["output_sha256"] == c["output_sha256"])}
                    for k, c in enumerate(s.llamadas)]
            tools_brazo = {x.rsplit("__", 1)[-1] for x in CFG["brazos"][s.brazo]["tools_esperadas"]}
            ini = next((x for x in lineas if x["evento"] == "inicio"), {})
            logs[s.sid] = {"brazo": s.brazo, "pid": s.pid, "pid_en_el_log": ini.get("pid"),
                           "tags": sorted({x["sesion_tag"] for x in lineas if "sesion_tag" in x}), "n_llamadas": len(ll),
                           "n_pedidas": len(s.llamadas), "tools": sorted({x["tool"] for x in ll}),
                           "mapa": mapa, "con_fin": any(x["evento"] == "fin" for x in lineas),
                           "PASS": (sorted({x["sesion_tag"] for x in lineas if "sesion_tag" in x}) == [s.sid] and len(ll) == len(s.llamadas)
                                    and all(m["coincide"] for m in mapa) and {x["tool"] for x in ll} <= tools_brazo
                                    and ini.get("pid") == s.pid and any(x["evento"] == "fin" for x in lineas))}
        for k, v in cods.items():
            codificadores_vistos[k] = v
        fr_ok = all(c["control_2"]["PASS"] for r in rondas for c in r["fragmentos"])
        concurrente = all(any(c["grafo_respondiendo_a_la_vez"] for r in rondas for c in r["fragmentos"] if c["sesion"] == f.sid)
                          for f in frag)
        gr_ok = all(v["PASS"] and v["control_positivo_descriptor_de_su_codificador"] > 0
                    for r in rondas for v in r["grafo"].values())
        res["tandas"][t] = {"servidores": {s.sid: s.pid for s in srv}, "codificadores": cods, "rondas": rondas,
                            "logs_r1": logs, "fragmentos_PASS": fr_ok, "con_el_grafo_respondiendo_a_la_vez": concurrente,
                            "grafo_PASS": gr_ok, "logs_PASS": all(v["PASS"] for v in logs.values())}
    todos = [q for v in codificadores_vistos.values() for q in v]
    pids_srv = [p for t in res["tandas"].values() for p in t["servidores"].values()]
    res["codificador_uno_por_sesion_del_grafo"] = {"por_sesion": codificadores_vistos,
                                                   "PASS": all(len(v) == 1 for v in codificadores_vistos.values())
                                                   and len(set(todos)) == len(todos)}
    res["servidores_pid_distintos"] = len(set(pids_srv)) == len(pids_srv)
    res["PASS"] = (all(t["fragmentos_PASS"] and t["grafo_PASS"] and t["logs_PASS"] and t["con_el_grafo_respondiendo_a_la_vez"]
                       for t in res["tandas"].values())
                   and res["codificador_uno_por_sesion_del_grafo"]["PASS"] and res["servidores_pid_distintos"])
    return res


# --------------------------------------------------------------------------------------------------------------------- #
# Control negativo                                                                                                      #
# --------------------------------------------------------------------------------------------------------------------- #
def negativo(a) -> dict:
    tmp = a.tmp
    tmp.mkdir(parents=True, exist_ok=True)
    frag = json.loads((BANCO_DIR / CFG["brazos"]["fragmentos_bm25"]["mcp_config"]).read_text(encoding="utf-8"))
    kg = json.loads((BANCO_DIR / CFG["brazos"]["kg"]["mcp_config"]).read_text(encoding="utf-8"))
    frag["mcpServers"]["kg"] = kg["mcpServers"]["kg"]
    mcp_neg = tmp / "mcp_fragmentos_bm25_con_el_grafo_NEGATIVO.json"
    mcp_neg.write_text(json.dumps(frag, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    cfg = json.loads(N6.CONFIG_N6.read_text(encoding="utf-8"))
    cfg["brazos"]["fragmentos_bm25"]["mcp_config"] = str(mcp_neg)
    cfg_neg = tmp / "config_agentes_n6_prueba_NEGATIVO.json"
    cfg_neg.write_text(json.dumps(cfg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    out = a.out / "negativo"
    r = subprocess.run([sys.executable, "-B", str(BANCO_DIR / "paralelo" / "lanzar_agente_n6_prueba.py"), "--brazo",
                        "fragmentos_bm25", "--id", "NEG-fragmentos_bm25", "--pregunta", "pregunta de prueba (modo init)",
                        "--out", str(out), "--modo", "init", "--sesiones", str(a.sesiones.parent / (a.sesiones.name + "_negativo")),
                        "--config-agentes", str(cfg_neg)], capture_output=True, text=True)
    m = json.loads((out / "meta_NEG-fragmentos_bm25.json").read_text(encoding="utf-8"))
    c1 = control_a({"meta": m}, "fragmentos_bm25")
    # control 2: un proceso propio con un socket al puerto de Neo4j y el kg.json abierto, que solo espera su entrada
    puerto = urlparse(os.environ["NEO4J_URI"]).port
    guion = tmp / "proceso_negativo.py"
    guion.write_text("import socket, sys\ns = socket.create_connection(('127.0.0.1', int(sys.argv[1])))\n"
                     "f = open(sys.argv[2], 'rb')\nprint('listo', flush=True)\nsys.stdin.read()\n", encoding="utf-8")
    p = subprocess.Popen(["python3", str(guion), str(puerto), str(KG_JSON)], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         text=True)
    listo = p.stdout.readline().strip()                 # espera a que tenga el socket y el archivo (sin sleep)
    c2 = control_2(p.pid, {puerto, PUERTO_DEFECTO}, set(), [])
    p.stdin.close()
    rc = p.wait()
    return {"config_negativa": {"mcp_json": rel_repo(mcp_neg), "config_agentes": rel_repo(cfg_neg), "rc_lanzador": r.returncode,
                                "tools_en_init": c1["tools"], "control_1": {k: c1[k] for k in ("tools_del_otro_brazo",
                                                                                                "coincide_con_esperadas", "PASS")},
                                "FALLA_COMO_DEBE": not c1["PASS"] and bool(c1["tools_del_otro_brazo"])},
            "proceso_negativo": {"listo": listo, "control_2": {k: c2[k] for k in ("conexiones_a_neo4j", "archivos_del_grafo", "PASS")},
                                 "rc_al_cerrarle_la_entrada": rc,
                                 "FALLA_COMO_DEBE": (not c2["PASS"] and bool(c2["conexiones_a_neo4j"]) and bool(c2["archivos_del_grafo"]))}}


CFG_GRAFO = json.loads((BANCO_DIR / CFG["brazos"]["kg"]["config_servidor"]).read_text(encoding="utf-8"))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--sesiones", type=Path, required=True)
    ap.add_argument("--tmp", type=Path, required=True)
    ap.add_argument("--resultado", type=Path, required=True)
    ap.add_argument("--banco-paralelo", type=Path, required=True, help="donde va uno de los CLAUDE.md plantados del testigo")
    ap.add_argument("--privado", type=Path, required=True, help="los cuerpos capturados del testigo, fuera del paquete")
    a = ap.parse_args()
    for v in ("NEO4J_URI", "BANCO_VENV_VECTOR"):
        if not os.environ.get(v):
            raise SystemExit(f"falta {v} en el entorno")
    res = {"unidad": "U-BANCO-PARALELO — test de aislamiento sobre el lanzador en paralelo (USD 0)",
           "config_agentes": {"ruta": rel_repo(N6.CONFIG_N6), "sha256": sha256_file(N6.CONFIG_N6)}}
    antes = compartido()
    if not antes["neo4j"]["ok"]:
        raise SystemExit("ABORTO: el Neo4j de NEO4J_URI no responde o no es el acumulado")
    res["negativo"] = negativo(a)
    if not (res["negativo"]["config_negativa"]["FALLA_COMO_DEBE"] and res["negativo"]["proceso_negativo"]["FALLA_COMO_DEBE"]):
        res["PASS"] = False
        res["NO_VALE"] = "el control negativo no falló: el test no vale"
    else:
        res["init"] = fase_init(a, antes)
        res["ejecucion"] = fase_ejecucion(a)
        res["testigo"] = TES.fase_testigo(a.out / "testigo", a.sesiones.parent / (a.sesiones.name + "_testigo"), a.tmp / "testigo",
                                          a.privado, a.banco_paralelo, a.out / "init")
        despues = compartido()
        res["compartido_solo_lectura"] = {"antes": antes, "despues": despues, "PASS": antes == despues}
        res["PASS"] = (res["init"]["PASS"] and res["ejecucion"]["PASS"] and res["testigo"]["PASS"]
                       and res["compartido_solo_lectura"]["PASS"])
    a.resultado.parent.mkdir(parents=True, exist_ok=True)
    a.resultado.write_text(json.dumps(res, ensure_ascii=False, indent=1).replace(str(a.tmp.resolve()), "<tmp>")
                           .replace(str(a.tmp), "<tmp>").replace(str(Path.home()), "$HOME") + "\n",
                           encoding="utf-8")
    for k in ("negativo", "init", "ejecucion", "testigo", "compartido_solo_lectura"):
        if k in res:
            v = res[k]
            print(f"{k}: " + ("PASS" if v.get("PASS") else
                               ("FALLA COMO DEBE" if k == "negativo" and all(x["FALLA_COMO_DEBE"] for x in v.values()) else "FAIL")))
    print("TOTAL:", "PASS" if res["PASS"] else "FAIL")
    return 0 if res["PASS"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
