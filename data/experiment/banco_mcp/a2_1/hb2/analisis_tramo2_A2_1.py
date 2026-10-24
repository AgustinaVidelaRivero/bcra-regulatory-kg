#!/usr/bin/env python3
"""analisis_tramo2_A2_1.py — Las tablas del FRENO A2.1-b, leídas de las salidas del tramo 2 (USD 0; solo lee).

Lee smoke/resultados/a2_1/ y a2_1/hb2/ (metas y registros) y, para el antecedente, las 12 sesiones de la corrida 2 de la fase
B con a2_1/antecedente_HB2_faseB.metas_faseB. Escribe un JSON con:
  - el smoke por sesión: R3, mapa R7, log R1 con `fin`, llamadas, máximo de tool_use por mensaje, largo mayor en unidades
    UTF-16, control del disco, valor remoto, costo R9 y del CLI, denegaciones y el JSON final (respondible, citas);
  - H-B2 por sesión, con los mismos campos y los conteos de H-B2;
  - el gasto por paso y en total;
  - la fórmula de num_turns observada después de correr (no es una de las candidatas pre-declaradas de R-a):
    num_turns = tool_use + mensajes del asistente sin tool_use, verificada sesión por sesión en A2.1 y en el antecedente;
  - las llamadas en paralelo de cada sesión (la nota de la mesa).

Uso: python3 -B analisis_tramo2_A2_1.py <repo> <salida.json>
"""
import json
import sys
from pathlib import Path

repo, salida = Path(sys.argv[1]), Path(sys.argv[2])
B = repo / "data" / "experiment" / "banco_mcp"
sys.path.insert(0, str(B / "a2_1"))
import antecedente_HB2_faseB as ANT  # noqa: E402  (solo lee la fase B)


def fila(m: dict) -> dict:
    h, f, cd = m["hb2"], m["final_json_R4"], m["control_disco"]
    sin_tu = h["n_mensajes_asistente"] - h["n_mensajes_con_tool_use"]
    return {"id": m["pregunta_id"], "brazo": m["brazo"], "max_turns": h["max_turns_efectivo"],
            "completa_R3": m["completitud_R3"]["completa"], "motivos_R3": m["completitud_R3"]["motivos_incompleta"],
            "mapa_R7_coincide": all(x["coincide_tool_input"] for x in m["mapa_R7"]), "n_mapa_R7": len(m["mapa_R7"]),
            "log_r1_con_fin": h["log_r1_con_fin"], "n_llamadas_log_r1": h["n_llamadas_log_r1"],
            "num_turns": h["num_turns"], "subtype": h["subtype"], "stop_reason": h["stop_reason"],
            "n_mensajes_asistente": h["n_mensajes_asistente"], "n_mensajes_con_tool_use": h["n_mensajes_con_tool_use"],
            "n_tool_use": h["n_tool_use"], "n_tool_result": h["n_tool_result"],
            "max_tool_use_por_mensaje": h["max_tool_use_por_mensaje"], "corte_disparado": h["corte_disparado"],
            "formula_observada": h["num_turns"] == h["n_tool_use"] + sin_tu,
            "largo_mayor_utf16": cd["largo_mayor_utf16"], "disco_frena": cd["FRENA"],
            "carpeta_tool_results": cd["carpeta_tool_results"], "marcas_en_transcripcion": len(cd["tool_results_con_la_marca"]),
            "valor_remoto": {k: m["valor_remoto_por_tool"].get(k) for k in ("archivo", "existe", "apariciones",
                                                                              "tools_del_banco_con_numero")},
            "costo_R9": m["tokens_R9"]["costo_recomputado"]["total_usd"],
            "costo_cli": m["tokens_R9"]["total_cost_usd_cli_solo_para_contraste"],
            "denials": m["permission_denials"], "modelos": m["modelos_R8"]["inventario_observado"],
            "json_final": None if f is None else {"respondible": f.get("respondible"), "n_citas": len(f.get("citas") or [])},
            "claude_code_version": m["harness_R10"]["claude_code_version"], "duracion_s": m["duracion_s"]}


def tabla(d: Path) -> list:
    return [fila(json.loads(p.read_text(encoding="utf-8"))) for p in sorted(d.glob("meta_*.json"))]


smoke, hb2 = tabla(B / "smoke" / "resultados" / "a2_1"), tabla(B / "a2_1" / "hb2")
ant = []
for m in ANT.metas_faseB():
    h = m["hb2"]
    ant.append({"id": m["pregunta_id"], "num_turns": h["num_turns"], "n_tool_use": h["n_tool_use"],
                "n_mensajes_asistente": h["n_mensajes_asistente"], "n_mensajes_con_tool_use": h["n_mensajes_con_tool_use"],
                "max_tool_use_por_mensaje": h["max_tool_use_por_mensaje"],
                "formula_observada": h["num_turns"] == h["n_tool_use"] + h["n_mensajes_asistente"] - h["n_mensajes_con_tool_use"]})
reg_s = json.loads((B / "smoke" / "resultados" / "a2_1" / "registro_smoke_a2_1.json").read_text(encoding="utf-8"))
reg_h = json.loads((B / "a2_1" / "hb2" / "registro_HB2.json").read_text(encoding="utf-8"))
gasto = {p: {"n_sesiones": len(t), "R9_usd": round(sum(x["costo_R9"] for x in t), 6),
             "CLI_usd": round(sum(x["costo_cli"] for x in t), 6)} for p, t in (("paso1_smoke", smoke), ("paso2_hb2", hb2))}
gasto["total_tramo2"] = {k: round(gasto["paso1_smoke"][k] + gasto["paso2_hb2"][k], 6) for k in ("n_sesiones", "R9_usd", "CLI_usd")}
out = {"unidad": "A2.1, tramo 2 — análisis de las salidas del smoke y de H-B2",
       "comando": "python3 -B analisis_tramo2_A2_1.py <repo> <salida.json>",
       "smoke": smoke, "hb2": hb2, "antecedente_faseB": ant, "gasto": gasto,
       "registros": {"smoke": {k: reg_s.get(k) for k in ("inicio", "fin", "FRENO", "FRENO_DISCO", "P0", "proyeccion_usd",
                                                           "gasto_R9_usd_tramo2", "gasto_cli_usd_tramo2", "trazas")},
                     "hb2": {k: reg_h.get(k) for k in ("inicio", "fin", "FRENO", "FRENO_DISCO", "gasto_R9_usd_tramo2",
                                                         "gasto_cli_usd_tramo2")}},
       "formula_observada": {"enunciado": "num_turns = tool_use + mensajes del asistente sin tool_use",
                             "A2_1": f"{sum(x['formula_observada'] for x in smoke + hb2)} de {len(smoke + hb2)}",
                             "antecedente_faseB": f"{sum(x['formula_observada'] for x in ant)} de {len(ant)}"},
       "paralelas": {x["id"]: x["max_tool_use_por_mensaje"] for x in smoke + hb2}}
salida.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps({k: out[k] for k in ("gasto", "formula_observada")}, ensure_ascii=False))
print("paralelas:", out["paralelas"])
print("antecedente:", [(x["id"], x["num_turns"], x["n_tool_use"], x["n_mensajes_asistente"], x["n_mensajes_con_tool_use"], x["formula_observada"]) for x in ant])
