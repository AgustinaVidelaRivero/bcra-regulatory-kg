#!/usr/bin/env python3
"""control_servidores_n7c.py — El control de los tres servidores de B2 de N7c, USD 0, antes del humo: corre desde el repo,
después del commit. Levanta, uno por vez, el servidor de cada configuración con su JSON de MCP (N7: n7/mcp_kg_n7_evaluado.json;
N7c: n7c/mcp_kg_n7c_evaluado.json; N7c+: n7c/mcp_kg_n7c_amp_evaluado.json), con el cliente MCP del banco (cliente_falso.py:
stdio, sin modelo), con BANCO_REPO en la raíz del repo, NEO4J_URI bolt://127.0.0.1:47687 (el Neo4j de B6.3) y BANCO_VENV_VECTOR
en el venv del codificador. Por stdio controla:
  - tools/list: las mismas diez herramientas en los tres, con las mismas descripciones y esquemas, y las de
    servidor_mcp_kg_nav_rel_amp.tools_de([1..5]);
  - ver_punto sobre la primera ancla de la pregunta del humo (leída por código, nunca impresa): la salida de N7 es un prefijo
    de la de N7c (seguida de un salto de línea), y la de N7c de la de N7c+; N7c trae la cabecera de la sección y N7 no; N7c+
    trae además la cabecera de la familia y, en su último renglón, la línea de la cita;
  - cada servidor cierra su log R1 (la línea `fin`).
Antes de levantar nada: las seis configuraciones dan su sha256 (correr_n7c.CONFIGURACIONES), el Neo4j de B6.3 da su huella
(control_neo4j_b63.estado) y ningún otro paso pago corre. La foto del repo (correr_n6.foto_repo), antes y después. Escribe en
<salida> (fuera del repo) los logs R1 y control_servidores_n7c.json; imprime solo cuentas, booleanos y sha256.
Las pruebas lo corren contra el servidor de juguete (n7c/seco/servidor_mcp_juguete_n7c.py), con --mcp-N7, --mcp-N7c y --mcp-N7c-amp.
Códigos: 0 todo da; 1 algo del control no da; 8 una precondición; 7 otro paso pago.
Uso: .venv/bin/python -B data/experiment/banco_mcp/n7c/control_servidores_n7c.py --salida <dir fuera del repo>
     [--preguntas-humo <json>] [--sha256-preguntas-humo <hex>] [--venv-vector <dir>]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BANCO_DIR = AQUI.parent
for _p in (str(AQUI), str(BANCO_DIR), str(BANCO_DIR / "paralelo" / "cli_falso"), str(BANCO_DIR / "mcp_kg")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import correr_n7c as C7                          # noqa: E402
import claude_falso as CF                        # noqa: E402  (HEAD: expandir, sin editar)
from cliente_falso import ClienteFalso           # noqa: E402  (HEAD, sin editar)

CN = C7.CN
REPO_DIR = CN.REPO_DIR
FDR = Path.home() / "INGENIERIA IA" / "TESIS" / "fuera_del_repo"
HUMO = FDR / "unav_n7c_c2bis" / "humo" / "preguntas_humo_N7c.json"
SHA_HUMO = "a5eea29c5d0318827e572c07be4af5fb8a9a2a7079b6e244fc3cee9adefdf4e2"
VENV_VECTOR = Path.home() / "INGENIERIA IA" / "TESIS" / "venvs" / "banco_vector_py312"
MCP = {"N7": BANCO_DIR / "n7/mcp_kg_n7_evaluado.json", "N7c": BANCO_DIR / "n7c/mcp_kg_n7c_evaluado.json",
       "N7c_amp": BANCO_DIR / "n7c/mcp_kg_n7c_amp_evaluado.json"}


def sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def cabeceras(salida: str) -> dict:
    lineas = salida.split("\n")
    return {"seccion": any(x.startswith("Puntos relacionados (") or x == "Puntos relacionados: ninguno" for x in lineas),
            "familia": any(x.startswith("Puntos de la misma familia (") or x == "Puntos de la misma familia: ninguno"
                           for x in lineas),
            "cita": lineas[-1].startswith("Para citar este punto: ") and " | " in lineas[-1]}


def levantar(conf: str, mcp_json: Path, salida: Path, env_base: dict, punto: str) -> dict:
    (nombre, s), = json.loads(mcp_json.read_text(encoding="utf-8"))["mcpServers"].items()
    log = salida / f"log_r1_control_{conf}.jsonl"
    env = env_base | {"BANCO_LOG_R1": str(log), "BANCO_SESION_TAG": f"control_servidores_{conf}"}
    cmd = [CF.expandir(s["command"], env)] + [CF.expandir(x, env) for x in s.get("args", [])]
    e = {k: CF.expandir(v, env) for k, v in (s.get("env") or {}).items()}
    cli = ClienteFalso(cmd, env=env | e, timeout_s=900)
    cli.__enter__()
    try:
        tools = [{"name": t["name"], "description": t["description"], "input_schema": t.get("inputSchema")
                  or t.get("input_schema")} for t in cli.listar_tools()]
        r = cli.llamar_crudo("ver_punto", {"punto": punto})
        out = "".join(getattr(c, "text", "") for c in r.content)
        error = bool(r.isError)
    finally:
        cli.__exit__(None, None, None)
    lineas = [json.loads(x) for x in log.read_text(encoding="utf-8").splitlines() if x.strip()] if log.is_file() else []
    return {"servidor": nombre, "tools": tools, "salida": out, "error": error,
            "log_cierra": bool(lineas) and lineas[0].get("evento") == "inicio" and lineas[-1].get("evento") == "fin"}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path, required=True)
    ap.add_argument("--preguntas-humo", type=Path, default=HUMO)
    ap.add_argument("--sha256-preguntas-humo", default=SHA_HUMO)
    ap.add_argument("--venv-vector", type=Path, default=VENV_VECTOR)
    ap.add_argument("--mcp-N7", type=Path, default=MCP["N7"])
    ap.add_argument("--mcp-N7c", type=Path, default=MCP["N7c"])
    ap.add_argument("--mcp-N7c-amp", type=Path, default=MCP["N7c_amp"])
    a = ap.parse_args(argv)
    salida = a.salida.resolve()
    res: dict = {"unidad": "N7c, control de los servidores de B2 (USD 0)"}
    try:
        if salida.is_relative_to(REPO_DIR):
            raise CN.Freno(CN.PRECONDICION, "la salida está dentro del repo")
        salida.mkdir(parents=True, exist_ok=True)
        foto = CN.foto_repo()
        res["foto_repo_antes"] = {"n_archivos": foto["n_archivos"], "sha256": foto["sha256"]}
        b = a.preguntas_humo.read_bytes()
        if hashlib.sha256(b).hexdigest() != a.sha256_preguntas_humo:
            raise CN.Freno(CN.PRECONDICION, "la pregunta del humo no da su sha256")
        punto = CN.ancla_to_punto(json.loads(b)["preguntas"][0]["gold"]["anclas"][0])
        cfg = json.loads(C7.CONFIG_AGENTES.read_text(encoding="utf-8"))
        res["configuraciones"] = C7.control_configuraciones(cfg)
        import control_neo4j_b63 as CNB          # noqa: PLC0415  (b63/v2/b2, sin editar; correr_n7c lo agrega al path)
        os.environ["NEO4J_URI"] = C7.URI_B63
        n = CNB.estado(C7.HUELLA_NEO4J_B63, C7.URI_B63)
        res["neo4j_antes"] = {k: n.get(k) for k in C7.CAMPOS_NEO4J}
        if not n.get("ok"):
            raise CN.Freno(CN.PRECONDICION, f"el Neo4j de B6.3: {n.get('motivo')}")
        otro = C7.G.otro_paso_pago()
        if otro:
            raise CN.Freno(CN.OTRO_PASO_PAGO, f"otro paso pago corriendo: {otro}")
        env_base = dict(os.environ) | {"BANCO_REPO": str(REPO_DIR), "NEO4J_URI": C7.URI_B63,
                                       "BANCO_VENV_VECTOR": str(a.venv_vector), "PYTHONDONTWRITEBYTECODE": "1"}
        mcp = {"N7": a.mcp_N7, "N7c": a.mcp_N7c, "N7c_amp": a.mcp_N7c_amp}
        r = {c: levantar(c, p.resolve(), salida, env_base, punto) for c, p in mcp.items()}
    except CN.Freno as f:
        print(f"FRENO (código {f.codigo}): {f.motivo}")
        return f.codigo
    import servidor_mcp_kg_nav_rel_amp as SRA    # noqa: PLC0415
    esperadas = [{"name": t["name"], "description": t["description"], "input_schema": t["input_schema"]}
                 for t in SRA.tools_de([1, 2, 3, 4, 5])]
    clave = lambda ts: json.dumps(sorted(ts, key=lambda t: t["name"]), ensure_ascii=False, sort_keys=True)  # noqa: E731
    o7, o7c, o7cp = r["N7"]["salida"], r["N7c"]["salida"], r["N7c_amp"]["salida"]
    cab = {c: cabeceras(x["salida"]) for c, x in r.items()}
    controles = {
        "diez_herramientas_en_los_tres": all(len(x["tools"]) == 10 for x in r.values()),
        "mismas_herramientas_y_descripciones_en_los_tres": clave(r["N7"]["tools"]) == clave(r["N7c"]["tools"])
        == clave(r["N7c_amp"]["tools"]),
        "las_de_servidor_mcp_kg_nav_rel_amp": clave(r["N7"]["tools"]) == clave(esperadas),
        "ver_punto_sin_error": not any(x["error"] for x in r.values()),
        "N7_prefijo_de_N7c": o7c.startswith(o7 + "\n"),
        "N7c_prefijo_de_N7c+": o7cp.startswith(o7c + "\n"),
        "N7_sin_las_tres_marcas": not any(cab["N7"].values()),
        "N7c_con_la_seccion": cab["N7c"]["seccion"] and not cab["N7c"]["familia"] and not cab["N7c"]["cita"],
        "N7c+_con_la_seccion_la_familia_y_la_cita": all(cab["N7c_amp"].values()),
        "los_tres_logs_R1_cierran": all(x["log_cierra"] for x in r.values()),
    }
    res |= {"controles": controles, "tamanos": {c: len(x["salida"]) for c, x in r.items()},
            "sha256_salidas": {c: sha(x["salida"]) for c, x in r.items()},
            "sha256_herramientas": {c: sha(clave(x["tools"])) for c, x in r.items()}}
    n = CNB.estado(C7.HUELLA_NEO4J_B63, C7.URI_B63)
    res["neo4j_despues"] = {k: n.get(k) for k in C7.CAMPOS_NEO4J}
    res["neo4j_igual"] = res["neo4j_antes"] == res["neo4j_despues"]
    f2 = CN.foto_repo()
    res["foto_repo_despues"] = {"n_archivos": f2["n_archivos"], "sha256": f2["sha256"]}
    res["repo_igual"] = f2["sha256"] == foto["sha256"]
    res["ok"] = all(controles.values()) and res["neo4j_igual"] and res["repo_igual"]
    (salida / "control_servidores_n7c.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"controles": controles, "tamanos": res["tamanos"],
                      "sha256_salidas": {c: s[:12] for c, s in res["sha256_salidas"].items()},
                      "neo4j_igual": res["neo4j_igual"], "repo_igual": res["repo_igual"], "ok": res["ok"]}, ensure_ascii=False))
    return 0 if res["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
