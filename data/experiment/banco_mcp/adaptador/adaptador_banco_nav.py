#!/usr/bin/env python3
"""adaptador_banco_nav.py — Adaptador de trazas del banco para el brazo del grafo de B6.3, con las herramientas de
navegación (ATRIB_NAV). Módulo NUEVO que IMPORTA `adaptador_banco.py` y `gate/code/adaptador_cc.py` sin editarlos.

Lo que no cambia respecto de `adaptador_banco.adaptar`: el lector de la sesión (`leer_stream`) y del log R1
(`leer_log`), el JSON final del contrato R4 (`final_json_de`), la marca de completitud R3, el truncado del harness
(`adaptador_cc._truncar`) y la forma del payload que consume la atribución. Las tres herramientas v1 van igual que hoy:
su salida, del log R1, a `steps_full` como JSON; la atribución las controla con la re-ejecución.

Lo que cambia:
  · las herramientas del servidor del grafo que se aceptan son las diez del brazo `kg` de B6.3: las `tools_esperadas`
    de `b63/v2/b2/config_agentes_b63.json` (sha256 verificado), que incluyen las tres v1 (`TOOLS_VALIDAS`);
  · un pedido a un nombre que no es una herramienta del servidor (por ejemplo `mcp__kg`, sin el sufijo de ninguna de
    las diez) no llegó al servidor: no es un step, no entra a la reconciliación R7 y se cuenta aparte, en
    `banco.pedidos_sin_herramienta`. Su tool_result tiene que ser un error del cliente; si no lo es, el payload no es
    atribuible. En `adaptador_banco.adaptar` ese pedido entra a la lista de llamadas MCP y corre en uno el orden de la
    reconciliación de todas las que le siguen;
  · R7, con el log R1 como fuente de verdad: la k-ésima llamada a una herramienta de la sesión <-> la k-ésima
    `llamada` del log, con la misma herramienta, la misma entrada, `n` del log igual a k, `output_sha256` del log igual
    al sha256 de su `output_str` y, cuando la sesión trae el texto entero del tool_result, el mismo texto que el log.
    Un texto de la sesión más corto que el del log es un truncado del transporte (como en HEAD: se registra y la salida
    sale del log); uno distinto del mismo largo o más largo rechaza el step;
  · la salida de las siete de navegación es texto, no JSON: va a `steps_full` tal cual, con `formato: "texto"`.

Uso:
  adaptador_banco_nav.py --dir <dir con stream_<id>.jsonl + log_r1_<id>.jsonl> --id <id> --out <dir>
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BANCO_DIR = AQUI.parent
GATE_CODE = BANCO_DIR / "gate" / "code"
for _p in (str(AQUI), str(BANCO_DIR), str(GATE_CODE)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import adaptador_banco as AB  # noqa: E402  (HEAD, sin editar: lectores de sesión y de log, JSON final R4)
from adaptador_cc import TOOLS_VALIDAS, _truncar  # noqa: E402  (HEAD, sin editar)
from comun_banco import rel_repo, sha256_bytes  # noqa: E402

VERSION = "1.0-nav"
SERVIDOR = "mcp_kg"
PREFIJO_KG = "mcp__kg__"
CONFIG_AGENTES_B63 = BANCO_DIR / "b63" / "v2" / "b2" / "config_agentes_b63.json"
SHA_CONFIG_AGENTES_B63 = "eaff32bbad93cb9bc1f9d66ea2c4887cba8268f71007be6bb7158cc97bf0d0c4"


def tools_del_brazo_kg(path: Path = CONFIG_AGENTES_B63, sha_esperado: str = SHA_CONFIG_AGENTES_B63) -> tuple[str, ...]:
    """Las `tools_esperadas` del brazo `kg` de la configuración sellada de B6.3, sin el prefijo del servidor."""
    crudo = path.read_bytes()
    if sha256_bytes(crudo) != sha_esperado:
        raise SystemExit(f"ABORTO: {path.name} no es el de HEAD (sha256 {sha256_bytes(crudo)})")
    esperadas = json.loads(crudo)["brazos"]["kg"]["tools_esperadas"]
    if not esperadas or not all(isinstance(t, str) and t.startswith(PREFIJO_KG) for t in esperadas):
        raise SystemExit(f"ABORTO: las tools_esperadas del brazo kg no llevan todas el prefijo {PREFIJO_KG}")
    tools = tuple(t[len(PREFIJO_KG):] for t in esperadas)
    if len(set(tools)) != len(tools) or not set(TOOLS_VALIDAS) <= set(tools):
        raise SystemExit("ABORTO: las tools_esperadas del brazo kg repiten un nombre o no incluyen las tres v1")
    return tools


TOOLS_KG_B63 = tools_del_brazo_kg()
TOOLS_NAV_B63 = tuple(t for t in TOOLS_KG_B63 if t not in TOOLS_VALIDAS)


def clasificar_nombre(nombre) -> tuple[str, str | None]:
    """("herramienta", tool) para una de las diez con el prefijo del servidor; ("sin_herramienta", None) para
    cualquier otro nombre MCP (no llega al servidor); ("ajeno", None) para un nombre que no es MCP."""
    nombre = str(nombre)
    if nombre.startswith(PREFIJO_KG) and nombre[len(PREFIJO_KG):] in TOOLS_KG_B63:
        return "herramienta", nombre[len(PREFIJO_KG):]
    if nombre.startswith("mcp__"):
        return "sin_herramienta", None
    return "ajeno", None


def _sha_texto(s: str) -> str:
    return sha256_bytes(s.encode("utf-8"))


def adaptar(stream_path: Path, log_path: Path, meta_extra: dict | None = None,
            servidor: str | None = None) -> dict:
    ses = AB.leer_stream(stream_path)
    log = AB.leer_log(log_path)
    srv = servidor or (log["inicio"] or {}).get("servidor") or SERVIDOR
    if srv != SERVIDOR:
        raise SystemExit(f"ABORTO: este adaptador es el del brazo del grafo ({SERVIDOR}); el servidor es {srv!r}")

    llamadas, pedidos, ajenos = [], [], []
    for u in ses["usos"]:
        clase, tool = clasificar_nombre(u["name"])
        if clase == "herramienta":
            llamadas.append((u, tool))
        elif clase == "sin_herramienta":
            r = ses["resultados"].get(u["tool_use_id"])
            pedidos.append({"orden_en_sesion": u["orden"], "tool_use_id": u["tool_use_id"], "nombre": u["name"],
                            "linea_tool_use": u["linea"], "tiene_tool_result": r is not None,
                            "tool_result_is_error": None if r is None else r.get("is_error"),
                            "tool_result_sha256": None if r is None or r.get("texto") is None else _sha_texto(r["texto"]),
                            "llego_al_servidor": False})
        else:
            ajenos.append(u)

    steps, full, mapa, rechazos, incidencias = [], [], [], [], []
    corte = False
    n = 0
    for k, (u, tool) in enumerate(llamadas):
        r = ses["resultados"].get(u["tool_use_id"])
        if r is None:
            corte = True
            incidencias.append({"tool_use_id": u["tool_use_id"], "tool": tool, "input": u["input"],
                                "motivo": "tool_use sin tool_result (corte de sesión)"})
            continue
        n += 1
        ll = log["llamadas"][k] if k < len(log["llamadas"]) else None
        formato = "json" if tool in TOOLS_VALIDAS else "texto"
        entrada = {"n": n, "tool_use_id": u["tool_use_id"], "linea_tool_use": u["linea"],
                   "linea_tool_result": r["linea"], "uuid_asistente": u.get("uuid"),
                   "timestamp": u.get("timestamp"), "transporte": "mcp", "formato": formato,
                   "call_id_log": ll["call_id"] if ll else None, "n_log": ll["n"] if ll else None}
        motivo, s, obj = None, None, None
        texto_ses = r["texto"]
        if ll is None:
            motivo = "sin llamada correspondiente en el log R1"
        elif ll["tool"] != tool or ll["input"] != u["input"]:
            motivo = (f"log R1 no coincide: log=({ll['tool']}, {json.dumps(ll['input'], ensure_ascii=False)}) "
                      f"sesión=({tool}, {json.dumps(u['input'], ensure_ascii=False)})")
        elif ll.get("n") != k + 1:
            motivo = f"el n del log ({ll.get('n')}) no es el orden de la llamada en la sesión ({k + 1})"
        elif ll["output_str"] is None:
            motivo = f"el servidor registró error: {ll['error']}"
        elif _sha_texto(ll["output_str"]) != ll.get("output_sha256"):
            motivo = "el output_sha256 del log no es el sha256 de su output_str"
        elif texto_ses is not None and texto_ses != ll["output_str"] and len(texto_ses) >= len(ll["output_str"]):
            motivo = "el texto del tool_result de la sesión no es el del log (no es un truncado: mismo largo o más)"
        else:
            s = ll["output_str"]                   # ÍNTEGRO, del servidor
            if formato == "json":
                try:
                    obj = json.loads(s)
                except json.JSONDecodeError as e:
                    motivo = f"la salida de una herramienta v1 no es JSON: {e}"
        if motivo:
            rechazos.append(entrada | {"motivo_rechazo": motivo})
            steps.append({"n": n, "tool": tool, "input": u["input"], "output_truncado": None, "output_chars": None})
            mapa.append(entrada | {"ok": False})
            continue
        igual = (texto_ses == s) if texto_ses is not None else None
        truncado_por_transporte = texto_ses is not None and texto_ses != s
        steps.append({"n": n, "tool": tool, "input": u["input"], "output_truncado": _truncar(s), "output_chars": len(s)})
        if formato == "json":
            full.append({"n": n, "tool": tool, "input": u["input"], "output": obj, "output_chars": len(s)})
        else:
            full.append({"n": n, "tool": tool, "input": u["input"], "output": s, "output_chars": len(s),
                         "formato": "texto"})
        mapa.append(entrada | {"ok": True, "output_sha256_log": ll["output_sha256"],
                               "sesion_igual_al_log": igual,
                               "sesion_truncada_por_transporte": truncado_por_transporte,
                               "chars_sesion": None if texto_ses is None else len(texto_ses),
                               "chars_log": len(s)})
        incidencias.append({"n": n, "fuente_output": "log_r1", "igual_a_la_sesion": igual, "chars": len(s)})

    fj = AB.final_json_de(ses["result"])
    res = ses["result"] or {}
    pedidos_sin_error = [p for p in pedidos if p["tool_result_is_error"] is not True]
    completa = bool(res.get("subtype") == "success" and not res.get("is_error") and fj is not None
                    and log["fin"] is not None and len(log["llamadas"]) == len(llamadas) and not corte
                    and not pedidos_sin_error)
    motivos = []
    if res.get("subtype") != "success" or res.get("is_error"): motivos.append(f"result.subtype={res.get('subtype')}")
    if fj is None: motivos.append("sin JSON final del contrato R4")
    if log["fin"] is None: motivos.append("log R1 sin línea fin")
    if len(log["llamadas"]) != len(llamadas):
        motivos.append(f"log {len(log['llamadas'])} llamadas vs sesión {len(llamadas)} tool_use a herramientas del servidor")
    if corte: motivos.append("corte de sesión")
    if pedidos_sin_error:
        motivos.append(f"{len(pedidos_sin_error)} pedidos a nombres que no son herramientas sin un tool_result de error")
    atribuible = completa and not rechazos
    fuente = (log["inicio"] or {}).get("fuente") or {}
    payload = {
        "meta": {
            "unidad": "ATRIB_NAV", "origen": "claude_code_session+mcp_log_r1", "transporte": "mcp",
            "adaptador": rel_repo(Path(__file__)), "adaptador_version": VERSION,
            "adaptador_banco_importado": rel_repo(Path(AB.__file__)),
            "adaptador_gate_importado": rel_repo(GATE_CODE / "adaptador_cc.py"),
            "servidor": srv, "config_sha256_servidor": (log["inicio"] or {}).get("config_sha256"),
            "grafo": fuente.get("kg_path"), "grafo_sha256": fuente.get("kg_sha256") or fuente.get("sha256_matriz"),
            "stream": rel_repo(stream_path), "log_r1": rel_repo(log_path), "log_r1_sha256": log["sha256"],
            "session_id": (ses["init"] or {}).get("session_id") or res.get("session_id"),
            "contrato_tools": "v1+navegacion_b63",
            "tools_aceptadas": list(TOOLS_KG_B63),
            "config_agentes_b63": rel_repo(CONFIG_AGENTES_B63), "config_agentes_b63_sha256": SHA_CONFIG_AGENTES_B63,
            "generado": datetime.now().isoformat(timespec="seconds"),
        } | (meta_extra or {}),
        "trace": {"question": (meta_extra or {}).get("pregunta"), "steps": steps, "final_json": fj,
                  "tool_calls_used": len(steps),
                  # R5: no existe hit_tool_limit del harness; se reporta el corte del banco aparte
                  "hit_tool_limit": False},
        "steps_full": full,
        "gate": {"corte_sesion": corte, "atribuible": atribuible, "n_steps_adaptados": len(steps),
                 "mapa_steps": mapa, "incidencias": incidencias, "rechazos": rechazos},
        "banco": {"completitud_R3": {"completa": completa, "motivos": motivos},
                  "n_tool_use_mcp": len(llamadas) + len(pedidos),
                  "n_tool_use_herramientas": len(llamadas),
                  "pedidos_sin_herramienta": {"n": len(pedidos), "detalle": pedidos},
                  "n_tool_use_ajenos": len(ajenos),
                  "ajenos": [{"name": a["name"], "tool_use_id": a["tool_use_id"]} for a in ajenos],
                  "n_llamadas_log": len(log["llamadas"]),
                  "corte_R5": {"num_turns": res.get("num_turns"), "subtype": res.get("subtype")},
                  "steps_con_sesion_truncada": sum(1 for m in mapa if m.get("sesion_truncada_por_transporte"))},
    }
    return payload


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", type=Path, required=True)
    ap.add_argument("--id", required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    p = adaptar(a.dir / f"stream_{a.id}.jsonl", a.dir / f"log_r1_{a.id}.jsonl", {"caso_id": a.id})
    a.out.mkdir(parents=True, exist_ok=True)
    (a.out / f"{a.id}.json").write_text(json.dumps(p, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{a.id}: {p['gate']['n_steps_adaptados']} steps | corte={p['gate']['corte_sesion']} | "
          f"atribuible={p['gate']['atribuible']} | rechazos={len(p['gate']['rechazos'])} | "
          f"pedidos sin herramienta={p['banco']['pedidos_sin_herramienta']['n']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
