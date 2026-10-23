#!/usr/bin/env python3
"""corrida_en_seco_a2_1.py — Corrida en seco del runner del tramo 2 (USD 0, sin API), por el
mismo camino de imports y de código que la corrida real (CLAUDE.md §4.l): importa
correr_a2_1 tal como lo importa Python al correrlo, sin tocar sys.path por fuera, y llama a
sus funciones.

  1. Los dos scripts zsh del tramo 2, de punta a punta, con un archivo de clave FALSO
     (A21_ENTORNO, en un directorio temporal, borrado al terminar) y A21_MODO=init: el
     envoltorio, el runner y el lanzador corren igual que en la corrida real, y cada
     sesión se lanza en modo init (ninguna petición llega a la API). Se corre sobre una
     copia del repo (este archivo vive en la copia): las metas init quedan en la copia.
  2. La reanudación: el paso 1 corrido otra vez no lanza ninguna sesión nueva.
  3. Las ramas que la corrida real puede tomar, con sesiones sintéticas (sin claude):
     freno por acumulado, freno por proyección, tope no autorizado, meta de otro modo,
     corte por --max-turns, llamadas paralelas, salida sin `result` y línea mal formada
     en el stream, y la evaluación de H-B2 sobre esos casos.
  4. El control del disco y la lectura del valor remoto por tool (decisiones de la autora del
     23/10/2026), con sesiones de juguete: una transcripción con la referencia a disco (una
     ruta con un espacio) y otra sin ella; `tool_results_<id>/` vacía y con un archivo; el
     largo en unidades UTF-16; el código 3 de la corrida y su reanudación; y tres
     `.claude.json` de juguete (la clave vacía, con un número para una tool del banco y sin
     la clave), sin que llegue a la meta ningún otro campo.

Uso (en la copia; BANCO_VENV_VECTOR = venv 3.12 del servidor de fragmentos):
  .venv/bin/python -B data/experiment/banco_mcp/a2_1/corrida_en_seco_a2_1.py
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path

import correr_a2_1 as CR                    # el runner, por su propio camino de imports
import lanzar_agente_a2_1 as L21

AQUI = Path(__file__).resolve().parent
BANCO_DIR = AQUI.parent
REPO_DIR = BANCO_DIR.parents[2]


def meta_sintetica(pid: str, brazo: str, modo: str, costo: float, hb2: dict | None = None,
                   p0_cache: int | None = None) -> dict:
    return {"pregunta_id": pid, "brazo": brazo, "modo": modo, "origen": "sintetico_corrida_en_seco",
            "tokens_R9": {"costo_recomputado": {"total_usd": costo}, "total_cost_usd_cli_solo_para_contraste": costo,
                          "por_llamada_api": ([{"modelo": "claude-sonnet-5", "input_tokens": 1,
                                                "cache_creation_input_tokens": p0_cache, "cache_read_input_tokens": 0}]
                                              if p0_cache else [])},
            "modelos_R8": {"declarado": "claude-sonnet-5"}, "completitud_R3": {"completa": False},
            "permission_denials": [], "hb2": hb2 or {}}


class CorridaSintetica(CR.Corrida):
    """La Corrida del runner con `lanzar` reemplazado: escribe una meta sintética en vez de
    abrir claude, con el comando (su session_id) y, si el escenario de la sesión lo pide, la
    transcripción, `tool_results_<id>/`, el log R1 y el `.claude.json` de su carpeta de
    configuración, bajo una raíz de sesiones propia de la prueba. El resto (guardas,
    reanudación, control del disco, valor remoto, registro) es el código real."""

    def __init__(self, a, dirs, costo=0.05, p0_cache=None, escenarios=None):
        super().__init__(a, dirs)
        self.costo, self.p0_cache, self.lanzadas = costo, p0_cache, []
        self.escenarios = escenarios or {}
        self.sesiones = Path(dirs[0]).parent / "sesiones_sinteticas"

    def lanzar(self, brazo, pid, pregunta, out, max_turns, timeout_s):
        self.lanzadas.append(pid)
        sid = f"sintetica-{pid}"
        (out / f"comando_{pid}.json").write_text(json.dumps({"session_id": sid}), encoding="utf-8")
        e = self.escenarios.get(pid, {})
        if "transcripcion" in e:
            (out / f"sesion_{pid}.jsonl").write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in e["transcripcion"])
                                                    + "\n", encoding="utf-8")
        if "tool_results" in e:
            d = out / f"tool_results_{pid}"
            d.mkdir(parents=True, exist_ok=True)
            for nombre, texto in e["tool_results"].items():
                (d / nombre).write_text(texto, encoding="utf-8")
        if "log_r1" in e:
            (out / f"log_r1_{pid}.jsonl").write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in e["log_r1"]) + "\n",
                                                     encoding="utf-8")
        if "claude_json" in e:
            cfg = self.sesiones / "config" / sid
            cfg.mkdir(parents=True, exist_ok=True)
            (cfg / ".claude.json").write_text(json.dumps(e["claude_json"]), encoding="utf-8")
        m = meta_sintetica(pid, brazo, self.a.modo, self.costo, p0_cache=self.p0_cache if pid.startswith("P0") else None)
        (out / f"meta_{pid}.json").write_text(json.dumps(m), encoding="utf-8")
        return m


def args(fase: str, out_smoke: Path, out_hb2: Path, modo: str = "init", tope: float = 3.0, freno: float = 2.0):
    return argparse.Namespace(fase=fase, autorizado_tope=tope, freno=freno, freno_proyeccion=2.4, modo=modo, via="api",
                              out_smoke=out_smoke, out_hb2=out_hb2)


def hb2(pid: str, max_turns: int, corte: bool, asis: int, tool_use: int, num_turns, max_por_msj: int = 1,
        hay_result: bool = True) -> dict:
    return {"pregunta_id": pid, "brazo": "fragmentos_bm25",
            "hb2": {"max_turns_efectivo": max_turns, "num_turns": num_turns, "subtype": "error_max_turns" if corte else "success",
                    "is_error": corte, "stop_reason": None, "n_mensajes_asistente": asis, "n_tool_use": tool_use,
                    "n_tool_result": tool_use, "n_eventos_user": tool_use, "n_mensajes_con_tool_use": asis - (0 if corte else 1),
                    "max_tool_use_por_mensaje": max_por_msj, "n_llamadas_log_r1": tool_use, "log_r1_con_fin": True,
                    "corte_disparado": corte, "hay_result": hay_result}}


def ramas() -> list[dict]:
    out = []
    with tempfile.TemporaryDirectory() as td:
        sm, hb = Path(td) / "smoke", Path(td) / "hb2"
        sm.mkdir(); hb.mkdir()
        # freno por acumulado: 1,75 gastado -> la próxima sesión no se lanza; 1,65 -> sí (1,65 + 0,30 <= 2)
        (sm / "meta_previa.json").write_text(json.dumps(meta_sintetica("previa", "x", "real", 1.75)), encoding="utf-8")
        c = CorridaSintetica(args("smoke", sm, hb, modo="real"), [sm, hb])
        try:
            c.sesion("fragmentos_bm25", "S1", "q", sm)
            out.append({"rama": "freno por acumulado (1,75 + 0,30 > 2)", "ok": False})
        except CR.Freno as e:
            out.append({"rama": "freno por acumulado (1,75 + 0,30 > 2)", "ok": not c.lanzadas, "mensaje": str(e)})
        (sm / "meta_previa.json").write_text(json.dumps(meta_sintetica("previa", "x", "real", 1.65)), encoding="utf-8")
        c = CorridaSintetica(args("smoke", sm, hb, modo="real"), [sm, hb])
        c.sesion("fragmentos_bm25", "S2", "q", sm)
        out.append({"rama": "sin freno (1,65 + 0,30 <= 2)", "ok": c.lanzadas == ["S2"]})
        # el acumulado suma las dos carpetas
        (hb / "meta_hb.json").write_text(json.dumps(meta_sintetica("hb", "x", "real", 0.10)), encoding="utf-8")
        r9, _ = CR.gastado([sm, hb])
        out.append({"rama": "el acumulado suma smoke y H-B2", "ok": abs(r9 - (1.65 + 0.05 + 0.10)) < 1e-9, "r9": round(r9, 4)})
        # meta de otro modo
        c = CorridaSintetica(args("smoke", sm, hb, modo="init"), [sm, hb])
        try:
            c.sesion("fragmentos_bm25", "S2", "q", sm)
            out.append({"rama": "meta de otro modo en la carpeta", "ok": False})
        except SystemExit as e:
            out.append({"rama": "meta de otro modo en la carpeta", "ok": "no se mezclan" in str(e)})
    # freno por proyección: P0 diez veces el de referencia -> FRENO antes de las preguntas
    with tempfile.TemporaryDirectory() as td:
        sm, hb = Path(td) / "smoke", Path(td) / "hb2"
        sm.mkdir()
        ref = json.loads(CR.ESTIMACION.read_text(encoding="utf-8"))["P0_faseB_referencia"]
        c = CorridaSintetica(args("smoke", sm, hb, modo="real"), [sm, hb], costo=0.0, p0_cache=10 * ref)
        try:
            CR.fase_smoke(c, sm)
            out.append({"rama": "freno por proyección", "ok": False})
        except CR.Freno as e:
            out.append({"rama": "freno por proyección", "ok": c.lanzadas == ["P0-fragmentos_bm25", "P0-fragmentos_denso"],
                        "mensaje": str(e)})
    # tope no autorizado
    try:
        CR.main(["--fase", "smoke", "--autorizado-tope", "0", "--modo", "init"])
        out.append({"rama": "tope 0", "ok": False})
    except SystemExit as e:
        out.append({"rama": "tope 0", "ok": "sin tope autorizado" in str(e)})
    # conteos de H-B2 sobre un stream sintético: dos tool_use en eventos distintos del mismo mensaje,
    # una línea mal formada y un result de corte
    lineas = [json.dumps({"type": "system", "subtype": "init"}),
              json.dumps({"type": "assistant", "message": {"id": "m1", "content": [{"type": "tool_use", "id": "t1"}]}}),
              json.dumps({"type": "assistant", "message": {"id": "m1", "content": [{"type": "tool_use", "id": "t2"}]}}),
              "{esto no es json",
              json.dumps({"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": "t1"}]}}),
              json.dumps({"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": "t2"}]}}),
              json.dumps({"type": "assistant", "message": {"id": "m2", "content": [{"type": "tool_use", "id": "t3"}]}})]
    res = {"type": "result", "subtype": "error_max_turns", "is_error": True, "num_turns": 3}
    k = L21.conteos_hb2(lineas + [json.dumps(res)], res, {"n_llamadas": 3, "fin": {"evento": "fin"}})
    out.append({"rama": "conteos: paralelas, línea mal formada y corte", "conteos": k,
                "ok": (k["n_mensajes_asistente"] == 2 and k["n_tool_use"] == 3 and k["n_tool_result"] == 2
                       and k["max_tool_use_por_mensaje"] == 2 and k["corte_disparado"] and k["num_turns"] == 3)})
    k2 = L21.conteos_hb2(lineas, None, {"n_llamadas": 3, "fin": None})
    out.append({"rama": "conteos: stream sin result", "ok": not k2["hay_result"] and k2["num_turns"] is None
                and not k2["log_r1_con_fin"]})
    # evaluación de H-B2: si --max-turns acota mensajes del asistente, solo ese conteo queda compatible
    metas = [hb2("A", 12, False, 9, 13, 14, max_por_msj=3),   # el caso de SMK-04-kg de la fase B
             hb2("B", 2, True, 2, 3, 4, max_por_msj=2),
             hb2("C", 1, True, 1, 1, 2),
             hb2("D", 12, False, 3, 2, 3),
             hb2("E", 3, True, 0, 0, None, hay_result=False)]
    ev = CR.evaluar_hb2(metas)
    out.append({"rama": "evaluación de H-B2 (sintética)", "estado_a": ev["R_a_num_turns"]["estado"],
                "estado_b": ev["R_b_max_turns"]["estado"], "excluidas": ev["excluidas_sin_result"],
                "ok": (ev["R_b_max_turns"]["compatibles"] == ["n_mensajes_asistente"] and ev["excluidas_sin_result"] == ["E"]
                       and "n_tool_result+1" in ev["R_a_num_turns"]["verificados"] and ev["hubo_llamadas_paralelas"])})
    ev0 = CR.evaluar_hb2([hb2("D", 12, False, 3, 2, 3)])
    out.append({"rama": "evaluación de H-B2 sin cortes", "estado_b": ev0["R_b_max_turns"]["estado"],
                "ok": ev0["R_b_max_turns"]["estado"].startswith("NO CARACTERIZADO")})
    # la pregunta compuesta
    d = json.loads(CR.DISENO_HB2.read_text(encoding="utf-8"))
    pq = {q["id"]: q["pregunta"] for q in json.loads(CR.PREGUNTAS.read_text(encoding="utf-8"))["preguntas"]}
    t = CR.componer(d, pq, ["SMK-01", "SMK-03"])
    out.append({"rama": "pregunta compuesta", "texto": t, "ok": t.startswith("Respondé estas 2 preguntas:\n(1) ")
                and pq["SMK-03"] in t and CR.componer(d, pq, ["SMK-04"]) == pq["SMK-04"]})
    return out


# --------------------------------------------------------------------------- #
# El control del disco y el valor remoto por tool                              #
# --------------------------------------------------------------------------- #
REFERENCIA = ("<persisted-output>\nOutput too large (240.1KB). Full output saved to: "
              "/ruta de prueba/carpeta con un espacio/tool-results/toolu_juguete_1.txt\n\nPreview (first 2KB):\n"
              "{\"consulta\": \"...\"}\n</persisted-output>")


def linea_tool_result(tid: str, texto: str) -> dict:
    return {"type": "user", "message": {"role": "user", "content": [
        {"type": "tool_result", "tool_use_id": tid, "content": [{"type": "text", "text": texto}]}]}}


def llamada_log(n: int, texto: str) -> dict:
    return {"evento": "llamada", "n": n, "tool": "buscar_pasajes", "output_str": texto}


SECRETO = "VALOR-QUE-NO-DEBE-SALIR"
CLAUDE_JSON = {
    "vacia": {"userID": SECRETO, "cachedGrowthBookFeatures": {"tengu_velvet_ibis": {}, "otra_clave": SECRETO}},
    "con_numero": {"userID": SECRETO, "oauthAccount": {"emailAddress": SECRETO},
                   "cachedGrowthBookFeatures": {"tengu_velvet_ibis": {"mcp__fragmentos__buscar_pasajes": 30000,
                                                                      "Read": 100000, "una_tool": SECRETO}}},
    "sin_clave": {"userID": SECRETO, "cachedGrowthBookFeatures": {"otra_clave": {"x": 1}}},
}
CAMPOS_PERMITIDOS = {"clave", "archivo", "existe", "apariciones", "tools_del_banco_con_numero"}


def ramas_disco() -> list[dict]:
    out = []
    with tempfile.TemporaryDirectory() as td:
        d = Path(td) / "sesiones_de_juguete"
        d.mkdir()
        # transcripción con la referencia y sin ella
        texto_ok = '{"consulta": "efectivo mínimo", "resultados": []}'
        (d / "sesion_A.jsonl").write_text("\n".join(json.dumps(x) for x in [
            {"type": "system", "subtype": "init"}, linea_tool_result("toolu_1", texto_ok),
            linea_tool_result("toolu_2", REFERENCIA)]) + "\n", encoding="utf-8")
        (d / "sesion_B.jsonl").write_text("\n".join(json.dumps(x) for x in [
            {"type": "system", "subtype": "init"}, linea_tool_result("toolu_1", texto_ok)]) + "\n", encoding="utf-8")
        ka, kb = CR.control_disco(d, "A"), CR.control_disco(d, "B")
        out.append({"rama": "disco: transcripción con la referencia (ruta con un espacio)",
                    "ok": ka["FRENA"] and [x["tool_use_id"] for x in ka["tool_results_con_la_marca"]] == ["toolu_2"]})
        out.append({"rama": "disco: transcripción sin la referencia",
                    "ok": not kb["FRENA"] and kb["largo_mayor_utf16_en_la_transcripcion"] == len(texto_ok)})
        # tool_results_<id>/ vacía y con un archivo
        (d / "tool_results_C").mkdir()
        (d / "tool_results_D").mkdir()
        (d / "tool_results_D" / "toolu_9.txt").write_text("x", encoding="utf-8")
        kc, kd = CR.control_disco(d, "C"), CR.control_disco(d, "D")
        out.append({"rama": "disco: tool_results_<id>/ vacía", "ok": not kc["FRENA"] and kc["carpeta_tool_results"] == "vacía"})
        out.append({"rama": "disco: tool_results_<id>/ con un archivo",
                    "ok": kd["FRENA"] and kd["archivos_en_tool_results"] == ["toolu_9.txt"]})
        # el largo en unidades UTF-16 (un carácter fuera del plano básico cuenta 2)
        (d / "log_r1_E.jsonl").write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in [
            {"evento": "inicio"}, llamada_log(1, "abc"), llamada_log(2, "a\U0001D400b"), {"evento": "fin"}]) + "\n",
            encoding="utf-8")
        ke = CR.control_disco(d, "E")
        out.append({"rama": "disco: largo en unidades UTF-16 desde el log R1",
                    "largos": ke["largos_resultados_utf16_log_r1"],
                    "ok": [x["unidades_utf16"] for x in ke["largos_resultados_utf16_log_r1"]] == [3, 4]
                          and [x["caracteres"] for x in ke["largos_resultados_utf16_log_r1"]] == [3, 3]
                          and ke["largo_mayor_utf16"] == 4 and not ke["FRENA"]})
        # el valor remoto: la clave vacía, con un número para una tool del banco, sin la clave y sin archivo
        res = {}
        for nombre, contenido in CLAUDE_JSON.items():
            cfg = Path(td) / "config" / nombre
            cfg.mkdir(parents=True)
            (cfg / ".claude.json").write_text(json.dumps(contenido), encoding="utf-8")
            res[nombre] = CR.valor_remoto_por_tool(cfg)
        res["sin_archivo"] = CR.valor_remoto_por_tool(Path(td) / "config" / "no_existe")
        limpio = all(SECRETO not in json.dumps(v) and set(v) <= CAMPOS_PERMITIDOS for v in res.values())
        out.append({"rama": "valor remoto: la clave vacía",
                    "ok": res["vacia"]["existe"] and res["vacia"]["apariciones"] == [{"tools": {}, "tools_sin_numero": []}]
                          and res["vacia"]["tools_del_banco_con_numero"] == []})
        out.append({"rama": "valor remoto: un número para una tool del banco",
                    "ok": res["con_numero"]["apariciones"] == [{"tools": {"Read": 100000, "mcp__fragmentos__buscar_pasajes": 30000},
                                                                "tools_sin_numero": ["una_tool"]}]
                          and res["con_numero"]["tools_del_banco_con_numero"] == ["mcp__fragmentos__buscar_pasajes"]})
        out.append({"rama": "valor remoto: sin la clave y sin archivo",
                    "ok": res["sin_clave"] == {"clave": "tengu_velvet_ibis", "archivo": "existe", "existe": False}
                          and res["sin_archivo"] == {"clave": "tengu_velvet_ibis", "archivo": "no existe"}})
        out.append({"rama": "valor remoto: ningún otro campo ni valor del archivo", "ok": limpio})
    # la corrida real con sesiones sintéticas: frena con el código 3 en la sesión con la referencia, no lanza la
    # siguiente, y al reanudar vuelve a frenar sin lanzar nada; el número de una tool del banco va al registro
    with tempfile.TemporaryDirectory() as td:
        sm, hb = Path(td) / "smoke", Path(td) / "hb2"
        escenarios = {
            "HB2-01": {"transcripcion": [linea_tool_result("toolu_1", "{}")], "log_r1": [llamada_log(1, "{}")],
                       "claude_json": CLAUDE_JSON["con_numero"]},
            "HB2-02": {"transcripcion": [linea_tool_result("toolu_1", REFERENCIA)], "tool_results": {"toolu_1.txt": "x"},
                       "claude_json": CLAUDE_JSON["sin_clave"]},
        }
        lanzadas = []
        original = CR.Corrida

        def fabrica(a, dirs):
            c = CorridaSintetica(a, dirs, costo=0.0, escenarios=escenarios)
            c.lanzadas = lanzadas
            return c
        argv = ["--fase", "hb2", "--autorizado-tope", "3", "--freno", "2", "--modo", "init",
                "--out-smoke", str(sm), "--out-hb2", str(hb)]
        try:
            CR.Corrida = fabrica
            rc1 = CR.main(argv)
            primera = list(lanzadas)
            reg = json.loads((hb / "registro_HB2.json").read_text(encoding="utf-8"))
            meta1 = json.loads((hb / "meta_HB2-01.json").read_text(encoding="utf-8"))
            lanzadas.clear()
            rc2 = CR.main(argv)
            segunda = list(lanzadas)
        finally:
            CR.Corrida = original
        out.append({"rama": "corrida: el control del disco frena con el código 3 y no lanza la sesión siguiente",
                    "rc": rc1, "lanzadas": primera, "freno": reg.get("FRENO_DISCO"),
                    "ok": rc1 == 3 and primera == ["HB2-01", "HB2-02"] and "HB2-02" in (reg.get("FRENO_DISCO") or "")})
        out.append({"rama": "corrida: al reanudar, vuelve a frenar sin lanzar nada", "rc": rc2, "lanzadas": segunda,
                    "ok": rc2 == 3 and segunda == []})
        out.append({"rama": "corrida: el número de una tool del banco va a la meta y al registro, sin otros campos",
                    "valor_remoto_HB2-01": meta1["valor_remoto_por_tool"],
                    "ok": reg.get("valor_remoto_tools_del_banco_con_numero") == {"HB2-01": ["mcp__fragmentos__buscar_pasajes"]}
                          and SECRETO not in json.dumps(meta1) and set(meta1["valor_remoto_por_tool"]) <= CAMPOS_PERMITIDOS
                          and not meta1["control_disco"]["FRENA"]})
    return out


def zsh_init(script: str, entorno: Path) -> dict:
    env = dict(os.environ, A21_ENTORNO=str(entorno), A21_MODO="init", A21_PYTHON=sys.executable)
    env.pop("ANTHROPIC_API_KEY", None)
    r = subprocess.run(["zsh", str(AQUI / script)], capture_output=True, text=True, env=env, cwd=str(REPO_DIR))
    return {"script": script, "returncode": r.returncode, "stdout_tail": r.stdout[-1500:], "stderr_tail": r.stderr[-800:]}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=AQUI / "controles" / "corrida_en_seco_a2_1.json")
    ap.add_argument("--sin-zsh", action="store_true", help="solo las ramas sintéticas (no lanza claude)")
    a = ap.parse_args()
    res = {"generado": datetime.now().isoformat(timespec="seconds"), "unidad": "A2.1, tramo 1 — corrida en seco del tramo 2",
           "copia": "el repo donde corre este archivo (una copia hecha con la cláusula, nunca el repo)"}
    res["ramas"] = ramas() + ramas_disco()
    if not a.sin_zsh:
        import secrets
        with tempfile.TemporaryDirectory() as td:
            falso = Path(td) / "entorno_falso_corrida_en_seco.txt"
            falso.write_text(f"ANTHROPIC_API_KEY=sk-ant-FALSO-{secrets.token_hex(16)}\n", encoding="utf-8")
            p1 = zsh_init("tramo2_paso1_smoke.zsh", falso)
            n1 = len(list(CR.OUT_SMOKE.glob("comando_*.json")))
            p2 = zsh_init("tramo2_paso2_hb2.zsh", falso)
            n2 = len(list(CR.OUT_HB2.glob("comando_*.json")))
            p1b = zsh_init("tramo2_paso1_smoke.zsh", falso)
            n1b = len(list(CR.OUT_SMOKE.glob("comando_*.json")))
        metas = [json.loads(p.read_text(encoding="utf-8")) for p in sorted(CR.OUT_SMOKE.glob("meta_*.json")) + sorted(CR.OUT_HB2.glob("meta_*.json"))]
        res["zsh_init"] = {
            "paso1": p1, "paso2": p2, "paso1_otra_vez": p1b,
            "n_sesiones_paso1": n1, "n_sesiones_paso2": n2, "n_sesiones_paso1_tras_reanudar": n1b,
            "todas_init": all(m["modo"] == "init" for m in metas),
            "costo_R9_total": sum(m["tokens_R9"]["costo_recomputado"]["total_usd"] or 0 for m in metas),
            "tools_en_init": sorted({tuple(m["inventario_tools_R6"]["tools_en_init"] or []) for m in metas}),
            "servidores_connected": all(any(s.get("status") == "connected" for s in (m["servidores_mcp"]["en_init"] or []))
                                        for m in metas),
            "max_turns_efectivos_hb2": {m["pregunta_id"]: m["hb2"]["max_turns_efectivo"] for m in metas if m["pregunta_id"].startswith("HB2")},
            "archivo_falso_borrado": not Path(td).exists()}
        z = res["zsh_init"]
        z["PASS"] = (p1["returncode"] == 0 and p2["returncode"] == 0 and p1b["returncode"] == 0 and n1 == 12 and n2 == 8
                     and n1b == 12 and z["todas_init"] and z["costo_R9_total"] == 0 and z["servidores_connected"]
                     and z["tools_en_init"] == [("mcp__fragmentos__buscar_pasajes",)] and z["archivo_falso_borrado"])
    res["PASS"] = all(r["ok"] for r in res["ramas"]) and (a.sin_zsh or res["zsh_init"]["PASS"])
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(res, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for r in res["ramas"]:
        print(("OK    " if r["ok"] else "FALLA ") + r["rama"])
    if not a.sin_zsh:
        print("zsh init:", "PASS" if res["zsh_init"]["PASS"] else "FAIL")
    print("TOTAL:", "PASS" if res["PASS"] else "FAIL")
    return 0 if res["PASS"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
