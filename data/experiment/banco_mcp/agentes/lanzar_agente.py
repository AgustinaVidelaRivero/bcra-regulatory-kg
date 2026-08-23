#!/usr/bin/env python3
"""lanzar_agente.py — Lanza UNA sesión `claude -p` por brazo y persiste todo lo que
el adaptador y la contabilidad necesitan (U-A2.0-banco, entregables 3, 5 y 6).

Por sesión produce, en --out:
  prompt_<id>.txt        el prompt literal pasado a `claude -p` (R4/R10)
  comando_<id>.json      argv completo + env relevante (sin credenciales) + sha de identidad
  stream_<id>.jsonl      salida --output-format stream-json íntegra (init, mensajes, result)
  stderr_<id>.txt        stderr del CLI
  sesion_<id>.jsonl      copia del jsonl de sesión de Claude Code (índice, no fuente de verdad)
  tool_results_<id>/     derrames a disco de resultados grandes (si los hubo)
  log_r1_<id>.jsonl      log R1 del servidor MCP de ESA sesión (fuente de verdad)
  meta_<id>.json         metadata por traza según agentes/contrato_metadata.md

Modos:
  --modo real   corrida real (cuesta; solo con autorización y tope: fase B)
  --modo init   costo USD 0: ANTHROPIC_BASE_URL apunta a un puerto cerrado, así que
                ninguna petición llega a la API; se captura el evento system/init
                (inventario de tools y servidores MCP por brazo, R6) y se mata el
                proceso. Usa --no-session-persistence.

Vía de credenciales (--via, entregable 6): `api` (ANTHROPIC_API_KEY del entorno),
`bedrock` (CLAUDE_CODE_USE_BEDROCK=1 y credenciales AWS del entorno). Nada más
cambia entre vías: el sha de identidad del pipeline (`sha_identidad`) se
computa sobre prompt, plantilla, bloques, configs de agentes/MCP/servidores,
modelo y flags — y excluye el entorno de credenciales.

Uso:
  lanzar_agente.py --brazo kg --id Q01 --pregunta "..." --out <dir> --modo init
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BANCO_DIR = AQUI.parent
REPO_DIR = BANCO_DIR.parents[2]
if str(BANCO_DIR) not in sys.path:
    sys.path.insert(0, str(BANCO_DIR))
from comun_banco import rel_repo, sha256_bytes, sha256_file  # noqa: E402

CONFIG_AGENTES = AQUI / "config_agentes.json"
PRECIOS = AQUI / "precios_sellados.json"
CREDENCIALES = AQUI / "config_credenciales.json"
VENV_VECTOR_DEFAULT = os.environ.get("BANCO_VENV_VECTOR", "")
DISALLOWED = "Bash,Read,Edit,Write,Glob,Grep,WebFetch,WebSearch,Agent,NotebookEdit"


def cargar(p: Path) -> dict:
    return json.loads(p.read_text(encoding="utf-8"))


def construir_prompt(cfg: dict, brazo: str, pregunta: str) -> str:
    plantilla = (BANCO_DIR / cfg["prompt"]["plantilla"]).read_text(encoding="utf-8")
    bloque = (BANCO_DIR / cfg["brazos"][brazo]["bloque_tools"]).read_text(encoding="utf-8").rstrip("\n")
    return (plantilla.replace("{{BLOQUE_TOOLS}}", bloque)
                     .replace("{{TOPE_TOOL_CALLS}}", str(cfg["corte_R5"]["tope_tool_calls_en_prompt"]))
                     .replace("{{PREGUNTA}}", pregunta))


def archivos_identidad(cfg: dict, brazo: str) -> dict:
    """Archivos cuyo sha define la identidad estructural del pipeline (entregable 6)."""
    b = cfg["brazos"][brazo]
    rutas = {
        "config_agentes": CONFIG_AGENTES,
        "plantilla_prompt": BANCO_DIR / cfg["prompt"]["plantilla"],
        "bloque_tools": BANCO_DIR / b["bloque_tools"],
        "mcp_config": BANCO_DIR / b["mcp_config"],
        "precios_sellados": PRECIOS,
    }
    if brazo == "kg":
        rutas["config_servidor"] = BANCO_DIR / "mcp_kg" / "config_mcp_kg.json"
        rutas["servidor"] = BANCO_DIR / "mcp_kg" / "servidor_mcp_kg.py"
    else:
        rutas["config_servidor"] = BANCO_DIR / "mcp_vector" / "config_mcp_vector.json"
        rutas["servidor"] = BANCO_DIR / "mcp_vector" / "servidor_mcp_vector.py"
    rutas["comun_banco"] = BANCO_DIR / "comun_banco.py"
    return {k: {"ruta": rel_repo(v), "sha256": sha256_file(v)} for k, v in rutas.items()}


def sha_identidad(ident: dict, modelo: str, flags: list[str], prompt: str) -> str:
    """sha256 canónico de {shas de archivos, modelo, flags sin valores de sesión, prompt}."""
    canon = {"archivos": {k: v["sha256"] for k, v in ident.items()}, "modelo": modelo,
             "flags": flags, "prompt_sha256": sha256_bytes(prompt.encode("utf-8"))}
    return sha256_bytes(json.dumps(canon, sort_keys=True, ensure_ascii=False).encode("utf-8"))


def flags_estructurales(cfg: dict, brazo: str) -> list[str]:
    b = cfg["brazos"][brazo]
    c = cfg["corte_R5"]
    return [cfg["modo_harness"], "-p", "--model", cfg["modelo"], "--output-format", "stream-json", "--verbose",
            "--tools", "", "--strict-mcp-config", "--mcp-config", b["mcp_config"],
            "--permission-mode", "dontAsk", "--allowedTools", b["allowed_tools"],
            "--disallowedTools", DISALLOWED, "--max-turns", str(c["max_turns"]),
            "--max-budget-usd", str(c["max_budget_usd_por_sesion"])]


def slug_proyecto(cwd: Path) -> str:
    # Regla medida en el gate (hallazgo B5): `pwd | tr '/ _' '---'`
    return str(cwd).replace("/", "-").replace(" ", "-").replace("_", "-")


def env_sesion(cfg: dict, brazo: str, via: str, log_r1: Path, tag: str, modo: str) -> tuple[dict, dict]:
    """(env completo para el subproceso, env declarado —sin secretos— para persistir)."""
    env = dict(os.environ)
    # limpiar vías para que solo quede la elegida
    for k in ("CLAUDE_CODE_USE_BEDROCK", "CLAUDE_CODE_USE_VERTEX", "CLAUDE_CODE_USE_FOUNDRY"):
        env.pop(k, None)
    declarado = {"BANCO_REPO": str(REPO_DIR), "BANCO_LOG_R1": str(log_r1), "BANCO_SESION_TAG": tag,
                 "MCP_TIMEOUT": cfg["env_por_sesion"]["MCP_TIMEOUT"].split()[0]}
    if brazo == "vector":
        declarado["BANCO_VENV_VECTOR"] = env.get("BANCO_VENV_VECTOR", VENV_VECTOR_DEFAULT)
        if not declarado["BANCO_VENV_VECTOR"]:
            raise SystemExit("BANCO_VENV_VECTOR no definido (venv 3.12 del servidor vectorial)")
    if via == "api":
        if modo == "real" and not env.get("ANTHROPIC_API_KEY"):
            raise SystemExit("vía api: ANTHROPIC_API_KEY no está en el entorno")
        declarado["via"] = "api (ANTHROPIC_API_KEY presente: %s)" % bool(env.get("ANTHROPIC_API_KEY"))
    elif via == "bedrock":
        env["CLAUDE_CODE_USE_BEDROCK"] = "1"
        declarado["CLAUDE_CODE_USE_BEDROCK"] = "1"
        declarado["via"] = "bedrock (credenciales AWS del entorno; AWS_REGION=%s)" % env.get("AWS_REGION")
    else:
        raise SystemExit(f"vía desconocida: {via}")
    if modo == "init":
        env["ANTHROPIC_BASE_URL"] = "http://127.0.0.1:9"   # puerto cerrado: ninguna petición sale
        env.setdefault("ANTHROPIC_API_KEY", "sk-ant-invalido-modo-init")
        declarado["ANTHROPIC_BASE_URL"] = env["ANTHROPIC_BASE_URL"]
    env.update({k: v for k, v in declarado.items() if k.isupper()})
    mascara = {"BANCO_REPO": ".", "BANCO_VENV_VECTOR": "<venv_vector fuera del repo>"}
    return env, {k: (mascara[k] if k in mascara else (rel_repo(v) if k == "BANCO_LOG_R1" else v))
                 for k, v in declarado.items()}


# --------------------------------------------------------------------------- #
# Parseo de la salida y metadata (entregable 5)                                #
# --------------------------------------------------------------------------- #
def parsear_stream(lineas: list[str]) -> dict:
    init, result, mensajes = None, None, []
    for l in lineas:
        try:
            d = json.loads(l)
        except json.JSONDecodeError:
            continue
        if d.get("type") == "system" and d.get("subtype") == "init":
            init = d
        elif d.get("type") == "result":
            result = d
        elif d.get("type") in ("assistant", "user"):
            mensajes.append(d)
    return {"init": init, "result": result, "mensajes": mensajes}


def tool_calls_de(mensajes: list[dict]) -> tuple[list[dict], dict]:
    """tool_use MCP en orden de aparición + índice tool_use_id -> tool_result."""
    usos, resultados = [], {}
    for m in mensajes:
        for c in (m.get("message") or {}).get("content", []) or []:
            if not isinstance(c, dict):
                continue
            if c.get("type") == "tool_use":
                usos.append({"tool_use_id": c.get("id"), "name": c.get("name"), "input": c.get("input"),
                             "uuid_mensaje": m.get("uuid"), "modelo": (m.get("message") or {}).get("model")})
            elif c.get("type") == "tool_result":
                resultados[c.get("tool_use_id")] = {"content": c.get("content"), "is_error": c.get("is_error")}
    return usos, resultados


def tokens_por_llamada(mensajes: list[dict]) -> list[dict]:
    """Uso por mensaje del asistente. C4: stream-json emite un evento `assistant`
    por bloque (thinking, text, tool_use) con el MISMO message.id y el mismo
    `usage`; se deduplica por message.id. El `usage` de stream es PARCIAL
    (contadores del momento del evento): sirve de inventario por llamada, no de
    contabilidad — el costo R9 sale de `modelUsage` del `result`."""
    out, vistos = [], set()
    for m in mensajes:
        if m.get("type") != "assistant":
            continue
        msg = m.get("message") or {}
        mid = msg.get("id") or m.get("uuid")
        if mid in vistos:
            continue
        vistos.add(mid)
        u = msg.get("usage") or {}
        out.append({"message_id": mid, "usage_parcial_de_stream": True,
                    "uuid": m.get("uuid"), "modelo": msg.get("model"), "stop_reason": msg.get("stop_reason"),
                    "input_tokens": u.get("input_tokens"), "output_tokens": u.get("output_tokens"),
                    "cache_creation_input_tokens": u.get("cache_creation_input_tokens"),
                    "cache_read_input_tokens": u.get("cache_read_input_tokens")})
    return out


def costo_desde_tokens(model_usage: dict, precios: dict) -> dict:
    """R9: costo desde conteos de tokens × precios sellados; nunca total_cost_usd."""
    det, total, sin_precio = {}, 0.0, []
    for modelo, u in (model_usage or {}).items():
        p = precios["modelos"].get(modelo)
        if p is None:
            sin_precio.append(modelo); continue
        c = (u.get("inputTokens", 0) * p["input"] + u.get("cacheCreationInputTokens", 0) * p["cache_write_5m"]
             + u.get("cacheReadInputTokens", 0) * p["cache_read"] + u.get("outputTokens", 0) * p["output"]) / 1e6
        det[modelo] = round(c, 6); total += c
    return {"total_usd": round(total, 6), "por_modelo": det, "modelos_sin_precio_sellado": sin_precio}


def final_json_de(result: dict | None) -> tuple[dict | None, str | None]:
    if not result:
        return None, "sin evento result"
    texto = result.get("result") or ""
    i, j = texto.find("{"), texto.rfind("}")
    if i < 0 or j < 0:
        return None, "el resultado no contiene un bloque JSON"
    try:
        d = json.loads(texto[i:j + 1])
    except json.JSONDecodeError as e:
        return None, f"JSON final no parseable: {e}"
    if not all(k in d for k in ("respuesta", "citas", "respondible")):
        return d, "JSON final sin las tres claves del contrato"
    return d, None


def leer_log_r1(p: Path) -> dict:
    if not p.exists():
        return {"existe": False}
    lineas = [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
    ini = next((l for l in lineas if l["evento"] == "inicio"), None)
    fin = next((l for l in lineas if l["evento"] == "fin"), None)
    llamadas = [l for l in lineas if l["evento"] == "llamada"]
    return {"existe": True, "ruta": rel_repo(p), "sha256": sha256_file(p), "inicio": ini, "fin": fin,
            "n_llamadas": len(llamadas),
            "llamadas": [{"n": l["n"], "call_id": l["call_id"], "tool": l["tool"], "input": l["input"],
                          "output_chars": l["output_chars"], "output_sha256": l["output_sha256"],
                          "error": l["error"]} for l in llamadas]}


def armar_meta(cfg: dict, brazo: str, ident: dict, sha_id: str, comando: dict, stream: dict,
               log: dict, precios: dict, via: str, modo: str, pregunta_id: str,
               sesion_copia: Path | None, claude_version: str) -> dict:
    init, result, mensajes = stream["init"], stream["result"], stream["mensajes"]
    usos, resultados = tool_calls_de(mensajes)
    usos_mcp = [u for u in usos if str(u["name"]).startswith("mcp__")]
    sin_result = [u["tool_use_id"] for u in usos_mcp if u["tool_use_id"] not in resultados]
    fj, motivo_fj = final_json_de(result)
    modelos = sorted({m for m in [(init or {}).get("model")] if m}
                     | set((result or {}).get("modelUsage", {}).keys())
                     | {u["modelo"] for u in usos if u.get("modelo")})
    tools_ok = (init or {}).get("tools") == cfg["brazos"][brazo]["tools_esperadas"]
    srv_ok = bool((init or {}).get("mcp_servers")) and all(s.get("status") == "connected"
                                                           for s in (init or {}).get("mcp_servers") or [])
    completa = bool(result and result.get("subtype") == "success" and not result.get("is_error")
                    and fj is not None and motivo_fj is None and log.get("fin") is not None
                    and log.get("n_llamadas") == len(usos_mcp) and not sin_result
                    and tools_ok and srv_ok)            # C3: R6 coincide y servidores connected
    motivos = []
    if not result:
        motivos.append("sin evento result")
    else:
        if result.get("subtype") != "success" or result.get("is_error"):
            motivos.append(f"result.subtype={result.get('subtype')}")
        if motivo_fj:
            motivos.append(motivo_fj)
    if log.get("fin") is None: motivos.append("log R1 sin línea fin")
    if log.get("n_llamadas") != len(usos_mcp): motivos.append(f"log R1 {log.get('n_llamadas')} llamadas vs sesión {len(usos_mcp)} tool_use MCP")
    if sin_result: motivos.append(f"tool_use sin tool_result: {sin_result}")
    if not tools_ok: motivos.append(f"inventario R6 no coincide: init={(init or {}).get('tools')}")
    if not srv_ok: motivos.append(f"servidores MCP no connected en init: {(init or {}).get('mcp_servers')}")
    corte = cfg["corte_R5"]
    return {
        "contrato": "agentes/contrato_metadata.md v1",
        "unidad": "U-A2.0-banco", "generado": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "pregunta_id": pregunta_id, "brazo": brazo, "modo": modo,
        "sesion": {"session_id": (init or {}).get("session_id") or (result or {}).get("session_id"),
                   "copia_jsonl": rel_repo(sesion_copia) if sesion_copia else None,
                   "cwd": comando["cwd"], "claude_code_version": claude_version,
                   "claude_code_version_en_init": (init or {}).get("claude_code_version")},
        "modelos_R8": {"declarado": cfg["modelo"], "inventario_observado": modelos,
                       "uso_por_modelo": (result or {}).get("modelUsage"),
                       "nota": "una sesión usa más de un modelo (b08095a, B1): el inventario es la verdad, el declarado es la intención"},
        "credenciales": {"via_declarada": via, "apiKeySource_en_init": (init or {}).get("apiKeySource")},
        "servidores_mcp": {"en_init": (init or {}).get("mcp_servers"),
                           "servidor_log_r1": (log.get("inicio") or {}).get("servidor"),
                           "version_servidor": (log.get("inicio") or {}).get("version_servidor"),
                           "config": (log.get("inicio") or {}).get("config"),
                           "config_sha256": (log.get("inicio") or {}).get("config_sha256"),
                           "fuente": (log.get("inicio") or {}).get("fuente"),
                           "entorno_servidor": (log.get("inicio") or {}).get("entorno")},
        "sha_fuentes": {"kg_sha256": ((log.get("inicio") or {}).get("fuente") or {}).get("kg_sha256"),
                        "sha256_matriz_vectorial": ((log.get("inicio") or {}).get("fuente") or {}).get("sha256_matriz")},
        "harness_R10": {"modo": cfg["modo_harness"], "permission_mode": (init or {}).get("permissionMode"),
                        "claude_code_version": claude_version,
                        "claude_code_version_sellada": cfg["claude_code_version_sellada"],
                        "coincide_con_sellada": claude_version.split()[0] == cfg["claude_code_version_sellada"],
                        "flags_estructurales": comando["flags_estructurales"],
                        "tools_denegadas": DISALLOWED, "tools_builtin": "\"\" (ninguna)",
                        "config_agentes_sha256": ident["config_agentes"]["sha256"],
                        "sha_identidad_pipeline": sha_id},
        "inventario_tools_R6": {"tools_en_init": (init or {}).get("tools"),
                                "esperadas": cfg["brazos"][brazo]["tools_esperadas"],
                                "coincide": (init or {}).get("tools") == cfg["brazos"][brazo]["tools_esperadas"]},
        "corte_R5": {"max_turns": corte["max_turns"], "tope_tool_calls_prompt": corte["tope_tool_calls_en_prompt"],
                     "max_budget_usd": corte["max_budget_usd_por_sesion"],
                     "num_turns_observado": (result or {}).get("num_turns"),
                     "n_tool_calls_observado": len(usos_mcp),
                     "corte_disparado": (result or {}).get("subtype") if result and result.get("subtype") != "success" else None},
        "completitud_R3": {"completa": completa, "motivos_incompleta": motivos,
                           "regla": "sin marca de completitud la traza se excluye de la métrica y se declara; nunca se atribuye"},
        "mapa_R7": [{"n": i + 1, "tool_use_id": u["tool_use_id"], "tool": u["name"], "input": u["input"],
                     "call_id_log": (log["llamadas"][i]["call_id"] if i < len(log.get("llamadas", [])) else None),
                     "coincide_tool_input": (i < len(log.get("llamadas", []))
                                             and log["llamadas"][i]["tool"] == str(u["name"]).rsplit("__", 1)[-1]
                                             and log["llamadas"][i]["input"] == (u["input"] or {}))}
                    for i, u in enumerate(usos_mcp)],
        "tokens_R9": {"por_llamada_api": tokens_por_llamada(mensajes),
                      "costo_recomputado": costo_desde_tokens((result or {}).get("modelUsage"), precios),
                      "total_cost_usd_cli_solo_para_contraste": (result or {}).get("total_cost_usd"),
                      "precios_sellados_sha256": ident["precios_sellados"]["sha256"]},
        "final_json_R4": fj, "permission_denials": (result or {}).get("permission_denials"),
        "log_r1": {k: v for k, v in log.items() if k in ("existe", "ruta", "sha256", "n_llamadas")},
    }


# --------------------------------------------------------------------------- #
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--brazo", choices=["kg", "vector"], required=True)
    ap.add_argument("--id", required=True, help="id de la pregunta/corrida (sesion_tag)")
    ap.add_argument("--pregunta", required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--modo", choices=["real", "init"], default="init")
    ap.add_argument("--via", choices=["api", "bedrock"], default="api")
    ap.add_argument("--cwd", type=Path, default=None, help="cwd aislado (default: smoke/cwd_<brazo>)")
    ap.add_argument("--timeout-s", type=float, default=900.0)
    a = ap.parse_args()

    cfg = cargar(CONFIG_AGENTES)
    precios = cargar(PRECIOS)
    a.out.mkdir(parents=True, exist_ok=True)
    cwd = (a.cwd or (BANCO_DIR / "smoke" / f"cwd_{a.brazo}")).resolve()
    cwd.mkdir(parents=True, exist_ok=True)
    prompt = construir_prompt(cfg, a.brazo, a.pregunta)
    (a.out / f"prompt_{a.id}.txt").write_text(prompt, encoding="utf-8")
    ident = archivos_identidad(cfg, a.brazo)
    flags = flags_estructurales(cfg, a.brazo)
    sha_id = sha_identidad(ident, cfg["modelo"], flags, prompt)
    log_r1 = (a.out / f"log_r1_{a.id}.jsonl").resolve()
    env, env_decl = env_sesion(cfg, a.brazo, a.via, log_r1, a.id, a.modo)
    session_id = str(uuid.uuid4())
    mcp_json = str(BANCO_DIR / cfg["brazos"][a.brazo]["mcp_config"])
    cmd = ["claude", cfg["modo_harness"], "-p", prompt, "--model", cfg["modelo"],
           "--output-format", "stream-json", "--verbose", "--tools", "",
           "--strict-mcp-config", "--mcp-config", mcp_json,
           "--permission-mode", "dontAsk", "--allowedTools", cfg["brazos"][a.brazo]["allowed_tools"],
           "--disallowedTools", DISALLOWED,
           "--max-turns", str(cfg["corte_R5"]["max_turns"]),
           "--max-budget-usd", str(cfg["corte_R5"]["max_budget_usd_por_sesion"]),
           "--session-id", session_id]
    if a.modo == "init":
        cmd.append("--no-session-persistence")
    claude_version = subprocess.run(["claude", "--version"], capture_output=True, text=True).stdout.strip()
    comando = {"argv": [("<prompt>" if x == prompt else (rel_repo(x) if x == mcp_json else x)) for x in cmd],
               "flags_estructurales": flags, "cwd": rel_repo(cwd), "env_declarado": env_decl,
               "session_id": session_id, "claude_code_version": claude_version,
               "archivos_identidad": ident, "sha_identidad_pipeline": sha_id,
               "lanzado": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    (a.out / f"comando_{a.id}.json").write_text(json.dumps(comando, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    t0 = time.time()
    stream_path = a.out / f"stream_{a.id}.jsonl"
    with open(stream_path, "w", encoding="utf-8") as fout, open(a.out / f"stderr_{a.id}.txt", "w", encoding="utf-8") as ferr:
        proc = subprocess.Popen(cmd, cwd=str(cwd), env=env, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE,
                                stderr=ferr, text=True)
        init_visto = False
        try:
            for linea in proc.stdout:
                fout.write(linea); fout.flush()
                if a.modo == "init" and '"subtype":"init"' in linea.replace(" ", ""):
                    init_visto = True
                if a.modo == "init" and init_visto and '"api_retry"' in linea:
                    proc.kill(); break       # modo init: ya tenemos el inventario; nada salió a la API
                if time.time() - t0 > a.timeout_s:
                    proc.kill(); break
        finally:
            try:
                proc.wait(timeout=30)
            except subprocess.TimeoutExpired:
                proc.kill()
    duracion = time.time() - t0

    # copia de la sesión (índice) y de los derrames
    sesion_copia = None
    if a.modo == "real":
        src = Path.home() / ".claude" / "projects" / slug_proyecto(cwd) / f"{session_id}.jsonl"
        if src.exists():
            sesion_copia = a.out / f"sesion_{a.id}.jsonl"
            shutil.copyfile(src, sesion_copia)
            derr = src.parent / session_id / "tool-results"
            if derr.exists():
                shutil.copytree(derr, a.out / f"tool_results_{a.id}", dirs_exist_ok=True)
    stream = parsear_stream(stream_path.read_text(encoding="utf-8").splitlines())
    log = leer_log_r1(log_r1)
    meta = armar_meta(cfg, a.brazo, ident, sha_id, comando, stream, log, precios, a.via, a.modo, a.id,
                      sesion_copia, claude_version)
    meta["duracion_s"] = round(duracion, 1)
    (a.out / f"meta_{a.id}.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"id": a.id, "brazo": a.brazo, "modo": a.modo, "tools": meta["inventario_tools_R6"],
                      "mcp": meta["servidores_mcp"]["en_init"], "completa": meta["completitud_R3"],
                      "costo": meta["tokens_R9"]["costo_recomputado"], "duracion_s": meta["duracion_s"]},
                     ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
