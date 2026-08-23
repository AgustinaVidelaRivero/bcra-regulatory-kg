#!/usr/bin/env python3
"""demo_clases_mcp.py — Demostración por clase del gate REPETIDA SOBRE EL TRANSPORTE
MCP (U-A2.0-banco, entregable 7 — condición de aceptación de la unidad).

Qué se repite y cómo (todo a USD 0, sin modelo):
  · las tools son las REALES del servidor MCP del KG (`mcp_kg/servidor_mcp_kg.py`,
    mismo código y mismo transporte stdio/JSON-RPC que usa Claude Code), con la
    config de demostración `config_mcp_kg_juguete.json` (backend `memoria` sobre
    `gate/grafo_juguete.json`, el mini-grafo con el que el gate definió sus casos
    y sus anclas);
  · la NAVEGACIÓN de cada caso se toma de las rebanadas selladas del gate
    (`gate/sesiones/rebanada_cruda.jsonl` = fase A escenificada;
    `gate/sesiones_faseB/rebanada_cruda.jsonl` = fase B con agente real), leída
    con `adaptador_cc.candidatos` importado: misma secuencia (tool, input) que
    entonces, pero ejecutada ahora contra el servidor MCP con el cliente falso;
  · la sesión se materializa con la FORMA de Claude Code (stream-json: init real
    capturado a USD 0, `tool_use` mcp__kg__*, `tool_result` con el texto que
    devolvió el servidor, `result`); el log R1 es el real del servidor;
  · el adaptador del banco (`adaptador_banco.py`, que importa el del gate) produce
    el payload; la atribución es el código de A0.2 IMPORTADO (`atribuir_payload`),
    con replay estándar y fuerte; todo dos veces (determinismo) y la adaptación
    dos veces (byte-idéntica salvo `meta.generado`).

Bordes: GATE-07 (fase A: sesión SIN tool calls), GATE-08 (tools que devuelven
vacío / id inexistente), GATE-09 (corte: `tool_use` sin `tool_result`), GATE-10
(resultado de 42.248 chars). GATE-11 (contrato v2) NO se corre: el banco expone
la firma v1 (laudo R2) y el servidor no tiene esa tool — se declara.

Limitación declarada: la navegación no la decide un agente en esta fase (la
decidió el agente del gate, real en fase B); lo que se mide acá es el
TRANSPORTE MCP + adaptador + atribución. La corrida con agente real sobre MCP
es la fase B de esta unidad.

Uso:
  .venv/bin/python -B demo_clases_mcp.py [--out resultados/demo_clases]
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import uuid
from datetime import datetime
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BANCO_DIR = AQUI.parent
EXPERIMENT_DIR = BANCO_DIR.parent
GATE_DIR = BANCO_DIR / "gate"
GATE_CODE = GATE_DIR / "code"
A02_CODE = EXPERIMENT_DIR / "ev2_reporte" / "code"
for _p in (str(BANCO_DIR), str(AQUI), str(GATE_CODE), str(A02_CODE)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import adaptador_cc as ACC                                      # noqa: E402  (gate, sellado: import)
import tools_juguete as TJ                                      # noqa: E402  (gate, sellado: import)
from atribucion_fallas import atribuir_payload, resolver_anclas  # noqa: E402  (A0.2, importado)
from demostracion_gate import render                            # noqa: E402  (gate: misma tabla)
from adaptador_banco import adaptar                             # noqa: E402
from cliente_falso import ClienteFalso                          # noqa: E402
from comun_banco import rel_repo, sha256_bytes, sha256_file     # noqa: E402

CONFIG_JUGUETE = BANCO_DIR / "mcp_kg" / "config_mcp_kg_juguete.json"
SERVIDOR = BANCO_DIR / "mcp_kg" / "servidor_mcp_kg.py"
INIT_REAL = BANCO_DIR / "agentes" / "resultados" / "init" / "stream_INIT-kg.jsonl"
FASES = {
    "A": {"casos": GATE_DIR / "casos_gate.json", "rebanada": GATE_DIR / "sesiones" / "rebanada_cruda.jsonl"},
    "B": {"casos": GATE_DIR / "casos_gate_faseB.json", "rebanada": GATE_DIR / "sesiones_faseB" / "rebanada_cruda.jsonl"},
}


def navegaciones(rebanada: Path) -> dict[str, list[tuple[str, dict]]]:
    lineas = ACC.leer_sesion(rebanada)
    acept, _ = ACC.candidatos(lineas)
    por: dict[str, list] = {}
    for a in sorted(acept, key=lambda x: x["linea_tool_use"]):
        por.setdefault(a["caso"], []).append((a["tool"], a["input"], a["contrato"]))
    return por


def init_real() -> dict:
    for l in INIT_REAL.read_text(encoding="utf-8").splitlines():
        d = json.loads(l)
        if d.get("subtype") == "init":
            return d
    raise SystemExit("sin init real capturado; correr agentes/lanzar_agente.py --modo init")


def materializar(caso_id: str, nav: list, out: Path, corte_en_step: int | None, init: dict) -> tuple[Path, Path]:
    """Ejecuta la navegación contra el servidor MCP real y escribe stream + log R1."""
    log = out / f"log_r1_{caso_id}.jsonl"
    if log.exists():
        log.unlink()
    sid = str(uuid.uuid4())
    lineas = [json.dumps(dict(init, session_id=sid), ensure_ascii=False)]
    with ClienteFalso([sys.executable, "-B", str(SERVIDOR), "--config", str(CONFIG_JUGUETE)],
                      env={"BANCO_LOG_R1": str(log), "BANCO_SESION_TAG": caso_id}) as cli:
        for k, (tool, inp, _) in enumerate(nav, 1):
            tuid = f"toolu_{caso_id}_{k:02d}"
            texto = cli.llamar(tool, inp)
            lineas.append(json.dumps({"type": "assistant", "uuid": str(uuid.uuid4()), "session_id": sid,
                                      "message": {"model": "claude-sonnet-5", "role": "assistant", "stop_reason": "tool_use",
                                                  "content": [{"type": "tool_use", "id": tuid, "name": f"mcp__kg__{tool}", "input": inp}]}},
                                     ensure_ascii=False))
            if corte_en_step == k:
                break      # corte: la sesión termina entre el tool_use y su resultado
            lineas.append(json.dumps({"type": "user", "uuid": str(uuid.uuid4()), "session_id": sid,
                                      "message": {"role": "user", "content": [{"type": "tool_result", "tool_use_id": tuid,
                                                                                "content": [{"type": "text", "text": texto}]}]}},
                                     ensure_ascii=False))
    if corte_en_step is None:
        fj = {"respuesta": f"[demo {caso_id}: sin modelo]", "citas": [], "respondible": True}
        lineas.append(json.dumps({"type": "result", "subtype": "success", "is_error": False, "num_turns": len(nav) + 1,
                                  "session_id": sid, "result": json.dumps(fj, ensure_ascii=False),
                                  "modelUsage": {}, "permission_denials": []}, ensure_ascii=False))
    stream = out / f"stream_{caso_id}.jsonl"
    stream.write_text("\n".join(lineas) + "\n", encoding="utf-8")
    return stream, log


def _canon_sin_generado(p: dict) -> str:
    q = json.loads(json.dumps(p))
    q["meta"].pop("generado", None)
    return json.dumps(q, ensure_ascii=False, sort_keys=True)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=AQUI / "resultados" / "demo_clases")
    a = ap.parse_args()
    out = a.out
    (out / "sesiones").mkdir(parents=True, exist_ok=True)
    (out / "trazas").mkdir(parents=True, exist_ok=True)
    init = init_real()
    index = TJ.cargar_index()
    aidx = TJ.cargar_ancla_index()
    grafo_sha = sha256_file(GATE_DIR / "grafo_juguete.json")

    filas, no_corridos = [], {}
    for fase, F in FASES.items():
        casos = json.loads(F["casos"].read_text(encoding="utf-8"))
        navs = navegaciones(F["rebanada"])
        for decl in casos["casos"]:
            cid = decl["caso_id"]
            etiqueta = f"{cid}@{fase}"
            if decl.get("contrato", "v1") == "v2":
                no_corridos[etiqueta] = "contrato v2: fuera del banco (laudo R2, opción B); el servidor MCP no expone esa firma"
                continue
            nav = navs.get(cid, [])
            corte = decl.get("corte_en_step")
            stream, log = materializar(etiqueta, nav, out / "sesiones", corte, init)
            extra = {"caso_id": cid, "fase_gate": fase, "anclas_gold": decl["anclas"],
                     "veredicto_declarado": decl["veredicto"], "clase_esperada": decl["clase_esperada"],
                     "grafo": rel_repo(GATE_DIR / "grafo_juguete.json"), "grafo_sha256": grafo_sha}
            p1 = adaptar(stream, log, extra)
            p2 = adaptar(stream, log, extra)
            det_adapt = _canon_sin_generado(p1) == _canon_sin_generado(p2)
            (out / "trazas" / f"{etiqueta}.json").write_text(json.dumps(p1, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            anclas, veredicto = decl["anclas"], decl["veredicto"]
            fila = {"caso_id": etiqueta, "contrato": "v1", "anclas": anclas,
                    "censo_nodos": {x: resolver_anclas([x], aidx)[x] for x in anclas}, "veredicto": veredicto,
                    "clase_esperada": decl["clase_esperada"], "n_steps": len(p1["trace"]["steps"]),
                    "corte_sesion": p1["gate"]["corte_sesion"], "atribuible_por_el_adaptador": p1["gate"]["atribuible"],
                    "determinismo_adaptador": det_adapt, "max_output_chars": max([s["output_chars"] or 0 for s in p1["trace"]["steps"]] or [0]),
                    "steps_con_sesion_truncada": p1["banco"]["steps_con_sesion_truncada"]}
            try:
                a1 = atribuir_payload(p1, anclas, aidx, index, veredicto)
                a2 = atribuir_payload(p1, anclas, aidx, index, veredicto)
                fila["determinismo_atribucion"] = (json.dumps(a1, sort_keys=True, ensure_ascii=False)
                                                   == json.dumps(a2, sort_keys=True, ensure_ascii=False))
                fila.update({"clase_obtenida": a1["clase"], "ancla_presente": a1["ancla_presente"],
                             "ancla_vista": a1["ancla_vista"], "ancla_consultada": a1["ancla_consultada"],
                             "replay_ok": a1["replay_ok"], "replay_fuerte_ok": a1["replay_fuerte_ok"],
                             "replay_fallas": a1["replay_fallas"], "replay_fuerte_fallas": a1["replay_fuerte_fallas"],
                             "por_ancla": a1["por_ancla"], "error_atribucion": None})
            except Exception as e:
                fila.update({"error_atribucion": f"{type(e).__name__}: {e}", "clase_obtenida": None})
            # Criterios: MAQUINARIA (replay estándar + fuerte + determinismo de atribución y de
            # adaptación) y CLASE (coincide con la esperada). Un caso no atribuible PASA si el
            # adaptador lo detectó (mismo criterio que el gate).
            if not fila["atribuible_por_el_adaptador"]:
                fila["maquinaria"] = "PASS (detectado como no atribuible)"
                fila["clase"] = "n/a"
                fila["veredicto_caso"] = "PASS (detectado como no atribuible)"
                fila["clase_si_se_atribuyera_igual"] = fila.get("clase_obtenida")
            else:
                maq = bool(fila.get("replay_ok") and fila.get("replay_fuerte_ok") and fila.get("determinismo_atribucion") and det_adapt)
                cl = fila.get("clase_obtenida") == decl["clase_esperada"]
                fila["maquinaria"] = "PASS" if maq else "FAIL"
                fila["clase"] = "coincide" if cl else "difiere"
                fila["veredicto_caso"] = "PASS" if (maq and cl) else "FAIL"
            filas.append(fila)
            print(f"{etiqueta}: steps={fila['n_steps']} clase {fila['clase_esperada']} -> {fila.get('clase_obtenida')} "
                  f"| replay={fila.get('replay_ok')} fuerte={fila.get('replay_fuerte_ok')} | {fila['veredicto_caso']}")

    res = {"generado": datetime.now().isoformat(timespec="seconds"),
           "unidad": "U-A2.0-banco — entregable 7 (demostración por clase sobre el transporte MCP)",
           "servidor": rel_repo(SERVIDOR), "config": rel_repo(CONFIG_JUGUETE), "config_sha256": sha256_file(CONFIG_JUGUETE),
           "grafo_juguete": rel_repo(GATE_DIR / "grafo_juguete.json"), "grafo_sha256": grafo_sha,
           "codigo_a02_importado": rel_repo(A02_CODE), "adaptador_gate_importado": rel_repo(GATE_CODE / "adaptador_cc.py"),
           "navegaciones": {f: rel_repo(F["rebanada"]) for f, F in FASES.items()},
           "no_corridos": no_corridos,
           "n_casos": len(filas), "n_pass": sum(1 for f in filas if f["veredicto_caso"].startswith("PASS")),
           "n_maquinaria_pass": sum(1 for f in filas if f["maquinaria"].startswith("PASS")),
           "n_clase_coincide": sum(1 for f in filas if f["clase"] == "coincide"),
           "determinismo_adaptador": {"ok": all(f["determinismo_adaptador"] for f in filas), "n_trazas": len(filas),
                                      "diferencias": [f["caso_id"] for f in filas if not f["determinismo_adaptador"]],
                                      "nota": "adaptación doble en memoria, JSON canónico salvo meta.generado"},
           "casos": filas}
    (out / "demo_clases_mcp.json").write_text(json.dumps(res, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    md = render(res).replace("U-A2.0-gate (entregable 5)", "U-A2.0-banco sobre MCP (entregable 7)")
    md += "\n## Lectura por criterio\n\n| caso | maquinaria | clase |\n|---|---|---|\n"
    md += "".join(f"| {f['caso_id']} | {f['maquinaria']} | {f['clase']} |\n" for f in filas)
    md += "\n## No corridos\n\n" + "".join(f"- {k}: {v}\n" for k, v in no_corridos.items())
    (out / "demo_clases_mcp.md").write_text(md, encoding="utf-8")
    print(md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
