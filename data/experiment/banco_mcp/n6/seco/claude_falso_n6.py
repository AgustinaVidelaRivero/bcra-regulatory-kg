#!/usr/bin/env python3
"""claude_falso_n6.py — El CLI falso de la corrida en seco de N6 (U-NAV-DISENO). Ningún modelo y ninguna petición a la API:
costo USD 0. Es el de paralelo/cli_falso/claude_falso.py (importado sin editarlo: sus lectores de argumentos, la expansión de
variables, la versión sellada y los precios), con lo que piden las ramas del corredor de N6:

  · `--version`: la versión sellada seguida de la marca de falso, así pasa la guarda de la versión del lote;
  · lanza el servidor MCP de la sesión desde su JSON (--mcp-config) por el cliente falso del banco, con su entorno, y emite el
    stream como `claude -p --output-format stream-json --verbose`: system/init con las herramientas y el servidor connected, un
    tool_use y su tool_result por llamada real al servidor (de las del plan, las que el servidor sirve), el mensaje final y el
    `result` con un modelUsage sintético; sin --no-session-persistence escribe la transcripción donde la copia el lanzador;
  · el plan sale de la marca [[seco:<plan>]] de la pregunta, en el archivo de planes que nombra --estado. Un plan puede:
      falla             matar su servidor y salir con 1, sin `result` (una falla de infraestructura);
      solo_intento_1    lo de arriba y el `result` con error, solo en el intento 1 (el BANCO_SESION_TAG sin «-i2»): el
                        reintento sale bien;
      subtype/is_error  el `result` con ese subtype e is_error (el corte por R5, un error de la API, una forma desconocida);
      final             el texto final tal cual (una salida que no es el JSON del contrato);
      marca_respuesta   la marca del juez falso en la respuesta ([CORRECTA], [INCORRECTA], [MALFORMADA]…);
      otro_paso_pago    lanzar, en su propia sesión de proceso y una sola vez por carpeta de trabajo, el proceso de juguete
                        que nombra el estado (un script con un token propio en su nombre) y escribir su pid, para la rama
                        de otro paso pago;
      sistema           cambiar, una sola vez por carpeta de trabajo y por plan, el estado del `vm_stat`, el `footprint` y
                        el `docker` falsos (seco/sistema_falso_n6.py, el archivo que nombra el estado en `estado_sistema`):
                        la memoria en uso que sube a mitad de un lote, el contenedor que deja de estar sano;
      uso               el uso de tokens del `result` (el R9 de la sesión).
Lo invoca el envoltorio que arma la corrida en seco en su carpeta de trabajo (fuera del repo): `claude` en el PATH, que pasa
`--estado <json>` antes de los argumentos del lanzador. El entorno de la sesión es la lista cerrada del lanzador: el estado
viaja por el envoltorio, no por el entorno.
"""
from __future__ import annotations

import json
import os
import signal
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BANCO_DIR = AQUI.parents[1]
for _p in (str(BANCO_DIR), str(BANCO_DIR / "paralelo"), str(BANCO_DIR / "paralelo" / "cli_falso")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import claude_falso as CF                # noqa: E402  (HEAD: solo import)
from cliente_falso import ClienteFalso   # noqa: E402
import guardas_lote as GL                # noqa: E402  (solo la tabla de procesos)

VERSION = f"{CF.VERSION_SELLADA} (CLI falso de la corrida en seco de N6: ninguna petición sale)"


def _primera_vez(marca: Path) -> bool:
    """True solo para la primera sesión que lo pide en la carpeta de trabajo (la marca se crea con O_EXCL y no se borra)."""
    try:
        os.close(os.open(marca, os.O_CREAT | os.O_EXCL | os.O_WRONLY))
        return True
    except FileExistsError:
        return False


def main(argv: list[str]) -> int:
    if argv[:1] != ["--estado"]:
        sys.stderr.write("CLI falso de N6: falta --estado\n")
        return 2
    estado = json.loads(Path(argv[1]).read_text(encoding="utf-8"))
    a = CF.leer_args(argv[2:])
    if "--version" in a["flags"]:
        print(VERSION)
        return 0
    prompt, sid, model = a["-p"], a["--session-id"], a["--model"]
    m = CF.MARCA.search(prompt)
    planes = json.loads(Path(estado["planes"]).read_text(encoding="utf-8"))["planes"]
    plan = planes[m.group(1)] if m else {"llamadas": []}
    tag = os.environ.get("BANCO_SESION_TAG", "")
    if plan.get("solo_intento_1") and tag.endswith("-i2"):
        plan = {k: v for k, v in plan.items() if k in ("llamadas", "marca_respuesta", "uso", "citas")}
    (srv, s), = json.loads(Path(a["--mcp-config"]).read_text(encoding="utf-8"))["mcpServers"].items()
    env = dict(os.environ)
    cmd = [CF.expandir(s["command"], env)] + [CF.expandir(x, env) for x in s.get("args", [])]
    e = {k: CF.expandir(v, env) for k, v in (s.get("env") or {}).items()}
    transcripcion, cwd = [], Path.cwd()

    def emitir(ev: dict, a_la_transcripcion: bool = True) -> None:
        print(json.dumps(ev, ensure_ascii=False), flush=True)
        if a_la_transcripcion:
            transcripcion.append(ev | {"sessionId": sid, "timestamp": CF.ahora()})

    def guardar_transcripcion() -> None:
        if "--no-session-persistence" in a["flags"]:
            return
        slug = str(cwd).replace("/", "-").replace(" ", "-").replace("_", "-")
        d = Path(os.environ["CLAUDE_CONFIG_DIR"]) / "projects" / slug
        d.mkdir(parents=True, exist_ok=True)
        with open(d / f"{sid}.jsonl", "w", encoding="utf-8") as f:
            for ev in transcripcion:
                f.write(json.dumps(ev, ensure_ascii=False) + "\n")

    transcripcion.append({"type": "user", "sessionId": sid, "timestamp": CF.ahora(), "version": VERSION,
                          "message": {"role": "user", "content": [{"type": "text", "text": prompt}]}})
    if plan.get("sistema") and _primera_vez(Path(estado["estado_sistema"]).with_name(f"marca_sistema_{m.group(1)}")):
        ps = Path(estado["estado_sistema"])
        tmp = ps.with_name(ps.name + f".{os.getpid()}.tmp")
        tmp.write_text(json.dumps(json.loads(ps.read_text(encoding="utf-8")) | plan["sistema"]), encoding="utf-8")
        tmp.replace(ps)
    if plan.get("otro_paso_pago") and _primera_vez(Path(estado["pid_otro_paso_pago"]).with_suffix(".marca")):
        p = subprocess.Popen([sys.executable, "-B", estado["otro_paso_pago"], estado["candado_otro_paso_pago"]], stdin=subprocess.DEVNULL,
                             stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, start_new_session=True, text=True)
        p.stdout.readline()                         # su aviso de que ya corre su script
        Path(estado["pid_otro_paso_pago"]).write_text(str(p.pid), encoding="utf-8")
    cli = ClienteFalso(cmd, env=e, timeout_s=600)
    cli.__enter__()
    tools = {t["name"] for t in cli.listar_tools()}
    nombres = sorted(f"mcp__{srv}__{t}" for t in tools)
    emitir({"type": "system", "subtype": "init", "cwd": str(cwd), "session_id": sid, "tools": nombres,
            "mcp_servers": [{"name": srv, "status": "connected"}], "model": model,
            "permissionMode": a.get("--permission-mode"), "apiKeySource": "ANTHROPIC_API_KEY",
            "claude_code_version": CF.VERSION_SELLADA}, a_la_transcripcion=False)
    falla = bool(plan.get("falla"))
    llamadas = [ll for ll in plan.get("llamadas", []) if ll["tool"] in tools]
    for k, ll in enumerate(llamadas, 1):
        if falla and k > plan.get("falla_tras", 0):
            break
        tid = f"toolu_falso_{sid[:8]}_{k}"
        emitir({"type": "assistant", "uuid": f"{sid[:8]}-a{k}",
                "message": {"id": f"msg_falso_{sid[:8]}_{k}", "model": model, "role": "assistant", "stop_reason": "tool_use",
                            "content": [{"type": "tool_use", "id": tid, "name": f"mcp__{srv}__{ll['tool']}", "input": ll["input"]}],
                            "usage": {"input_tokens": 10, "output_tokens": 50}}})
        r = cli.llamar_crudo(ll["tool"], ll["input"])
        texto = "".join(getattr(c, "text", "") for c in r.content)
        emitir({"type": "user", "uuid": f"{sid[:8]}-u{k}",
                "message": {"role": "user", "content": [{"type": "tool_result", "tool_use_id": tid, "is_error": bool(r.isError),
                                                         "content": [{"type": "text", "text": texto}]}]}})
    if falla:
        tabla = GL.tabla_procesos()
        for q in GL.descendientes(os.getpid(), tabla):
            if q in tabla and tabla[q][0] == os.getpid() and "servidor_mcp" in tabla[q][1]:
                os.kill(q, signal.SIGKILL)          # el servidor muere sin escribir su línea `fin`
        guardar_transcripcion()
        sys.stderr.write("CLI falso de N6: la sesión falla, por su plan\n")
        os._exit(1)
    cli.__exit__(None, None, None)                  # el servidor escribe su línea `fin`
    n = len(llamadas)
    final = plan.get("final")
    if final is None:
        final = json.dumps({"respuesta": "respuesta de la corrida en seco " + plan.get("marca_respuesta", "[CORRECTA]"),
                            "citas": plan.get("citas", []), "respondible": True}, ensure_ascii=False)
    subtype, is_error = plan.get("subtype", "success"), bool(plan.get("is_error", False))
    if subtype == "success" and not is_error:
        emitir({"type": "assistant", "uuid": f"{sid[:8]}-a{n + 1}",
                "message": {"id": f"msg_falso_{sid[:8]}_{n + 1}", "model": model, "role": "assistant", "stop_reason": "end_turn",
                            "content": [{"type": "text", "text": final}], "usage": {"input_tokens": 10, "output_tokens": 50}}})
    u = plan.get("uso") or {"inputTokens": 1000, "outputTokens": 100, "cacheReadInputTokens": 0, "cacheCreationInputTokens": 0}
    P = CF.PRECIO
    costo = (u["inputTokens"] * P["input"] + u["cacheCreationInputTokens"] * P["cache_write_5m"]
             + u["cacheReadInputTokens"] * P["cache_read"] + u["outputTokens"] * P["output"]) / 1e6
    emitir({"type": "result", "subtype": subtype, "is_error": is_error, "num_turns": n + 1,
            "result": final if subtype == "success" else plan.get("texto_error", ""),
            "session_id": sid, "total_cost_usd": round(costo, 6), "permission_denials": [],
            "modelUsage": {model: u | {"costUSD": round(costo, 6)}}}, a_la_transcripcion=False)
    guardar_transcripcion()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
