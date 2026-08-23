#!/usr/bin/env python3
"""selftest_integrador.py — Selftest integrador OFFLINE del banco (U-A2.0-banco,
entregable 8; cliente falso, USD 0). Recorre la cadena completa por brazo sobre
las fuentes REALES (KG-Refinado en Neo4j; índice vectorial harrier):

  init real (USD 0, lanzador) → sesión con la forma de Claude Code construida
  con llamadas MCP REALES por el mismo JSON de MCP del brazo → log R1 →
  adaptador del banco → payload → [brazo KG] atribución con el código de A0.2
  importado, replay estándar y fuerte contra `Neo4jIndex` en el MISMO modo que
  el servidor (fulltext) → metadata por traza.

Anclas y veredicto son PROPIOS y sintéticos (p. ej. `cap:1.3`, veredicto
`incorrecto` declarado): ejercitan la maquinaria, no evalúan nada. EV2 no se abre.

Para el brazo vectorial la atribución causal de A0.2 no aplica (sus clases se
definen sobre nodos del grafo); se verifica adaptación, completitud R3, mapa R7
y que cada pasaje cite TO + punto.

Uso:
  BANCO_VENV_VECTOR=<venv 3.12> .venv/bin/python -B selftest_integrador.py
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import uuid
from datetime import datetime
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BANCO_DIR = AQUI.parent
EXPERIMENT_DIR = BANCO_DIR.parent
REPO_DIR = EXPERIMENT_DIR.parents[1]
for _p in (str(BANCO_DIR), str(BANCO_DIR / "adaptador"), str(BANCO_DIR / "agentes"), str(BANCO_DIR / "gate" / "code"),
           str(EXPERIMENT_DIR / "ev2_reporte" / "code"), str(EXPERIMENT_DIR / "neo4j")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from cliente_falso import ClienteFalso                              # noqa: E402
from comun_banco import rel_repo, sha256_file                       # noqa: E402
from adaptador_banco import adaptar                                 # noqa: E402
import lanzar_agente as LA                                          # noqa: E402
import tools_juguete as TJ                                          # noqa: E402  (gate: cargar_ancla_index sobre cualquier kg.json)
from atribucion_fallas import atribuir_payload, resolver_anclas     # noqa: E402  (A0.2 importado)

OUT = AQUI / "resultados" / "selftest_integrador"
NAV = {
    "kg": [("buscar_nodos", {"consulta": "integración capital mínimo riesgo de mercado", "limite": 5}),
           ("ver_nodo", {"id": "Operacion_calculo_integracion_riesgo_de_mercado_f1a9d2"}),
           ("ver_vecinos", {"id": "Operacion_calculo_integracion_riesgo_de_mercado_f1a9d2", "direccion": "ambas"})],
    "vector": [("buscar_pasajes", {"consulta": "integración del capital mínimo por riesgo de mercado", "limite": 5}),
               ("buscar_pasajes", {"consulta": "responsabilidad patrimonial computable", "limite": 3})],
}
ANCLAS = ["cap:1.3"]          # propia, sintética, territorio verificado (verificar_territorio.py); resuelve a nodos reales
VEREDICTO = "incorrecto"      # insumo declarado (en el instrumento real lo pone el juez)


def expandir(s, env):
    return re.sub(r"\$\{([A-Z0-9_]+)(?::-([^}]*))?\}", lambda m: env.get(m.group(1), m.group(2) or ""), s)


def sesion_sintetica(brazo: str, cfg: dict, init: dict, out: Path) -> tuple[Path, Path]:
    env = dict(os.environ, BANCO_REPO=str(REPO_DIR))
    d = json.loads((BANCO_DIR / cfg["brazos"][brazo]["mcp_config"]).read_text())["mcpServers"][cfg["brazos"][brazo]["servidor"]]
    log = out / f"log_r1_{brazo}.jsonl"
    if log.exists():
        log.unlink()
    e = {k: expandir(v, dict(env, BANCO_LOG_R1=str(log), BANCO_SESION_TAG=f"selftest_{brazo}")) for k, v in d["env"].items()}
    cmd = [expandir(d["command"], env)] + [expandir(x, env) for x in d["args"]]
    sid = str(uuid.uuid4())
    lineas = [json.dumps(dict(init, session_id=sid), ensure_ascii=False)]
    srv = cfg["brazos"][brazo]["servidor"]
    with ClienteFalso(cmd, env=e, timeout_s=900) as cli:
        for k, (tool, inp) in enumerate(NAV[brazo], 1):
            texto = cli.llamar(tool, inp)
            tuid = f"toolu_self_{brazo}_{k:02d}"
            lineas.append(json.dumps({"type": "assistant", "uuid": str(uuid.uuid4()), "session_id": sid,
                                      "message": {"model": cfg["modelo"], "role": "assistant", "stop_reason": "tool_use",
                                                  "usage": {"input_tokens": 50, "output_tokens": 40, "cache_creation_input_tokens": 0, "cache_read_input_tokens": 0},
                                                  "content": [{"type": "tool_use", "id": tuid, "name": f"mcp__{srv}__{tool}", "input": inp}]}}, ensure_ascii=False))
            lineas.append(json.dumps({"type": "user", "uuid": str(uuid.uuid4()), "session_id": sid,
                                      "message": {"role": "user", "content": [{"type": "tool_result", "tool_use_id": tuid,
                                                                                "content": [{"type": "text", "text": texto}]}]}}, ensure_ascii=False))
    fj = {"respuesta": f"[selftest {brazo}: sin modelo]", "citas": ["TO_capitales_minimos_actual.pdf | Punto 1.3. Integración."], "respondible": True}
    lineas.append(json.dumps({"type": "assistant", "uuid": str(uuid.uuid4()), "session_id": sid,
                              "message": {"model": cfg["modelo"], "role": "assistant", "stop_reason": "end_turn",
                                          "usage": {"input_tokens": 100, "output_tokens": 80, "cache_creation_input_tokens": 0, "cache_read_input_tokens": 0},
                                          "content": [{"type": "text", "text": json.dumps(fj, ensure_ascii=False)}]}}, ensure_ascii=False))
    lineas.append(json.dumps({"type": "result", "subtype": "success", "is_error": False, "num_turns": len(NAV[brazo]) + 1,
                              "session_id": sid, "result": json.dumps(fj, ensure_ascii=False),
                              "modelUsage": {cfg["modelo"]: {"inputTokens": 250, "outputTokens": 160, "cacheCreationInputTokens": 0, "cacheReadInputTokens": 0}},
                              "permission_denials": []}, ensure_ascii=False))
    stream = out / f"stream_{brazo}.jsonl"
    stream.write_text("\n".join(lineas) + "\n", encoding="utf-8")
    return stream, log


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    cfg = LA.cargar(LA.CONFIG_AGENTES)
    precios = LA.cargar(LA.PRECIOS)
    res = {"generado": datetime.now().isoformat(timespec="seconds"),
           "unidad": "U-A2.0-banco — entregable 8 (selftest integrador offline)", "brazos": {}}
    for brazo in ("kg", "vector"):
        r = subprocess.run([sys.executable, "-B", str(LA.__file__), "--brazo", brazo, "--id", f"SELF-{brazo}",
                            "--pregunta", "¿Cómo se determina la integración del capital mínimo por riesgo de mercado?",
                            "--out", str(OUT), "--modo", "init"], capture_output=True, text=True)
        if r.returncode != 0:
            raise SystemExit(f"init {brazo}: {r.stderr[-500:]}")
        init = LA.parsear_stream((OUT / f"stream_SELF-{brazo}.jsonl").read_text().splitlines())["init"]
        stream, log = sesion_sintetica(brazo, cfg, init, OUT)
        extra = {"caso_id": f"SELF-{brazo}", "brazo": brazo, "pregunta": "¿Cómo se determina la integración del capital mínimo por riesgo de mercado?",
                 "anclas_gold": ANCLAS if brazo == "kg" else None, "veredicto_declarado": VEREDICTO if brazo == "kg" else None}
        p = adaptar(stream, log, extra)
        (OUT / f"traza_{brazo}.json").write_text(json.dumps(p, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        # metadata por traza con el constructor del lanzador
        comando = json.loads((OUT / f"comando_SELF-{brazo}.json").read_text())
        meta = LA.armar_meta(cfg, brazo, comando["archivos_identidad"], comando["sha_identidad_pipeline"], comando,
                             LA.parsear_stream(stream.read_text().splitlines()), LA.leer_log_r1(log), precios, "api",
                             "selftest", f"SELF-{brazo}", None, comando["claude_code_version"])
        meta["origen"] = "selftest_sintetico (sin modelo; llamadas MCP reales sobre la fuente real)"
        (OUT / f"meta_{brazo}.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        fila = {"tools_init": init["tools"], "n_steps": p["gate"]["n_steps_adaptados"], "atribuible": p["gate"]["atribuible"],
                "completa_R3": p["banco"]["completitud_R3"], "mapa_R7_ok": all(m["ok"] and m["sesion_igual_al_log"] for m in p["gate"]["mapa_steps"]),
                "max_output_chars": max(s["output_chars"] for s in p["trace"]["steps"]),
                "fuente": p["meta"]["grafo"], "fuente_sha256": p["meta"]["grafo_sha256"],
                "meta_completa": meta["completitud_R3"]["completa"], "costo_R9": meta["tokens_R9"]["costo_recomputado"]["total_usd"]}
        if brazo == "kg":
            from conexion import abrir_driver
            from neo4j_index import Neo4jIndex
            idx = Neo4jIndex(abrir_driver(), grafo="KG_Refinado", modo="fulltext")   # MISMO modo que el servidor
            aidx = TJ.cargar_ancla_index(EXPERIMENT_DIR / "grafo_v2" / "reensamblado_v3" / "kg.json")
            a1 = atribuir_payload(p, ANCLAS, aidx, idx, VEREDICTO)
            a2 = atribuir_payload(p, ANCLAS, aidx, idx, VEREDICTO)
            fila["atribucion"] = {"anclas": ANCLAS, "nodos_ancla": {x: resolver_anclas([x], aidx)[x] for x in ANCLAS},
                                  "veredicto": VEREDICTO, "clase": a1["clase"], "presente": a1["ancla_presente"],
                                  "vista": a1["ancla_vista"], "consultada": a1["ancla_consultada"],
                                  "replay_ok": a1["replay_ok"], "replay_fuerte_ok": a1["replay_fuerte_ok"],
                                  "replay_fallas": a1["replay_fallas"], "replay_fuerte_fallas": a1["replay_fuerte_fallas"],
                                  "determinismo": json.dumps(a1, sort_keys=True) == json.dumps(a2, sort_keys=True),
                                  "index_replay": "Neo4jIndex(KG_Refinado, modo=fulltext) — el mismo backend/modo del servidor"}
            fila["PASS"] = bool(fila["atribuible"] and fila["mapa_R7_ok"] and fila["meta_completa"] and a1["replay_ok"]
                                and a1["replay_fuerte_ok"] and fila["atribucion"]["determinismo"] and a1["clase"] == "generacion")
        else:
            citan = all(all(r.get("to") and r.get("unidad") for r in s["output"]["resultados"]) for s in p["steps_full"])
            fila["todos_citan_to_y_unidad"] = citan
            fila["atribucion"] = "no aplica (clases de A0.2 definidas sobre nodos del grafo)"
            fila["PASS"] = bool(fila["atribuible"] and fila["mapa_R7_ok"] and fila["meta_completa"] and citan)
        res["brazos"][brazo] = fila
        print(brazo, "PASS" if fila["PASS"] else "FAIL", json.dumps({k: v for k, v in fila.items() if k in ("n_steps", "atribuible", "mapa_R7_ok", "max_output_chars")}))
    res["PASS"] = all(b["PASS"] for b in res["brazos"].values())
    (OUT / "selftest_integrador.json").write_text(json.dumps(res, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("TOTAL:", "PASS" if res["PASS"] else "FAIL", "->", rel_repo(OUT / "selftest_integrador.json"))
    return 0 if res["PASS"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
