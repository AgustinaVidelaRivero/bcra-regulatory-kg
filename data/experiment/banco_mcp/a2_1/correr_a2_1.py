#!/usr/bin/env python3
"""correr_a2_1.py — Runner del tramo 2 de A2.1: el smoke de las dos configuraciones de
fragmentos y la caracterización de H-B2. NO corre sin autorización explícita: exige
`--autorizado-tope <USD>` y frena por proyección y por acumulado, con las guardas de
smoke/correr_smoke.py (R9: costo recomputado desde tokens con precios sellados; el
`total_cost_usd` del CLI se guarda solo para contraste).

El acumulado es UNO para todo el tramo 2: suma las meta_*.json de las dos carpetas de
salida (smoke y H-B2). Antes de cada sesión: si acumulado + 0,30 (el --max-budget-usd por
sesión) > freno, FRENO sin lanzar. Una sesión con meta ya escrita no se relanza
(reanudación), y una meta de otro modo (init frente a real) aborta la corrida.

  --fase smoke   0. P0: una sesión descartable por brazo con la pregunta trivial de
                    correr_smoke.py; proyección: estimación × (P0 medido / P0 de la fase B);
                    si supera --freno-proyeccion, FRENO.
                 1. las preguntas propias (smoke/preguntas_smoke.json) × los dos brazos.
                 2. aislamiento de punta a punta: una sesión por brazo con el pedido E2E del
                    brazo vectorial de correr_smoke.py (puerto 7687 o kg.json).
                 3. adaptación (adaptador_banco: mapa R7, completitud R3, truncados) y
                    contabilidad R9 contra el CLI. Sin atribución: no hay brazo del grafo.
  --fase hb2     las sesiones de a2_1/diseno_HB2.json, cada una con su --max-turns, y la
                 evaluación de las reglas de decisión del diseño (evaluar_hb2), con las
                 sesiones del smoke como controles si ya existen.

--modo init corre todo a USD 0 (modo init del lanzador: ninguna petición llega a la
API); es la corrida en seco del camino real.

Uso (tramo 2, solo con autorización; la clave la pone el envoltorio):
  BANCO_VENV_VECTOR=<venv> .venv/bin/python -B data/experiment/banco_mcp/a2_1/correr_a2_1.py \\
      --fase smoke --autorizado-tope 3 --freno 2
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BANCO_DIR = AQUI.parent
for _p in (str(AQUI), str(BANCO_DIR), str(BANCO_DIR / "adaptador"), str(BANCO_DIR / "smoke")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import lanzar_agente_a2_1 as L21                           # noqa: E402
from comun_banco import rel_repo                            # noqa: E402

PREGUNTAS = BANCO_DIR / "smoke" / "preguntas_smoke.json"
DISENO_HB2 = AQUI / "diseno_HB2.json"
ESTIMACION = AQUI / "estimacion_tramo2.json"
OUT_SMOKE = BANCO_DIR / "smoke" / "resultados" / "a2_1"
OUT_HB2 = AQUI / "hb2"
BRAZOS = ("fragmentos_bm25", "fragmentos_denso")
PRESUPUESTO_SESION = 0.30


def preguntas_sellados() -> tuple[str, str]:
    """La pregunta de P0 y el pedido E2E del brazo vectorial, tal cual están en correr_smoke.py."""
    import correr_smoke
    return correr_smoke.PREG_P0, correr_smoke.PREG_E2E["vector"]


def gastado(dirs: list[Path]) -> tuple[float, float]:
    r9, cli = 0.0, 0.0
    for d in dirs:
        for p in d.glob("meta_*.json") if d.exists() else []:
            m = json.loads(p.read_text(encoding="utf-8"))
            r9 += m["tokens_R9"]["costo_recomputado"]["total_usd"] or 0.0
            cli += m["tokens_R9"]["total_cost_usd_cli_solo_para_contraste"] or 0.0
    return r9, cli


class Freno(Exception):
    pass


class Corrida:
    def __init__(self, a, dirs: list[Path]):
        self.a, self.dirs = a, dirs
        self.registro = {"inicio": datetime.now().isoformat(timespec="seconds"), "fase": a.fase, "modo": a.modo,
                         "tope": a.autorizado_tope, "freno": a.freno, "via": a.via, "eventos": []}

    def sesion(self, brazo: str, pid: str, pregunta: str, out: Path, max_turns: int | None = None,
               timeout_s: float = 900.0) -> dict:
        p = out / f"meta_{pid}.json"
        if p.exists():
            m = json.loads(p.read_text(encoding="utf-8"))
            if m.get("modo") != self.a.modo:
                raise SystemExit(f"ABORTO: {rel_repo(p)} es de modo {m.get('modo')!r} y esta corrida es {self.a.modo!r}: "
                                 "no se mezclan sesiones de la corrida en seco con las reales")
            return m
        r9, _ = gastado(self.dirs)
        if r9 + PRESUPUESTO_SESION > self.a.freno or r9 + PRESUPUESTO_SESION > self.a.autorizado_tope:
            raise Freno(f"acumulado R9 {r9:.3f} + {PRESUPUESTO_SESION} > freno {self.a.freno} (tope {self.a.autorizado_tope}) antes de {pid}")
        m = self.lanzar(brazo, pid, pregunta, out, max_turns, timeout_s)
        self.registro["eventos"].append({"id": pid, "brazo": brazo, "completa": m["completitud_R3"]["completa"],
                                         "costo_R9": m["tokens_R9"]["costo_recomputado"]["total_usd"],
                                         "costo_cli": m["tokens_R9"]["total_cost_usd_cli_solo_para_contraste"],
                                         "denials": m["permission_denials"], "hb2": m["hb2"]})
        print(json.dumps(self.registro["eventos"][-1], ensure_ascii=False), flush=True)
        return m

    def lanzar(self, brazo, pid, pregunta, out, max_turns, timeout_s) -> dict:
        return L21.lanzar(brazo, pid, pregunta, out, self.a.modo, self.a.via, max_turns, None, timeout_s)

    def cerrar(self, out: Path, nombre: str) -> None:
        r9, cli = gastado(self.dirs)
        self.registro.update({"fin": datetime.now().isoformat(timespec="seconds"), "gasto_R9_usd_tramo2": round(r9, 4),
                              "gasto_cli_usd_tramo2": round(cli, 4),
                              "razon_cli_sobre_R9": round(cli / r9, 2) if r9 else None})
        out.mkdir(parents=True, exist_ok=True)
        (out / nombre).write_text(json.dumps(self.registro, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


# --------------------------------------------------------------------------- #
def fase_smoke(c: Corrida, out: Path) -> None:
    from adaptador_banco import adaptar
    preg_p0, preg_e2e = preguntas_sellados()
    preguntas = json.loads(PREGUNTAS.read_text(encoding="utf-8"))["preguntas"]
    est = json.loads(ESTIMACION.read_text(encoding="utf-8"))
    p0 = {}
    for b in BRAZOS:
        m = c.sesion(b, f"P0-{b}", preg_p0, out, timeout_s=300)
        primera = next((t for t in m["tokens_R9"]["por_llamada_api"] if t.get("modelo") == m["modelos_R8"]["declarado"]), None)
        p0[b] = {"input_tokens": primera and primera.get("input_tokens"),
                 "cache_creation": primera and primera.get("cache_creation_input_tokens"),
                 "cache_read": primera and primera.get("cache_read_input_tokens"),
                 "P0_estimado": (primera or {}).get("cache_creation_input_tokens") or (primera or {}).get("input_tokens"),
                 "contraste_P0_faseB": est["P0_faseB_referencia"]}
    c.registro["P0"] = p0
    p0_max = max([v["P0_estimado"] or 0 for v in p0.values()] or [0])
    proy = est["costo_estimado_usd"]["total_tramo2"] * (p0_max / est["P0_faseB_referencia"] if p0_max else 1.0)
    c.registro["proyeccion_usd"] = round(proy, 4)
    if proy > c.a.freno_proyeccion:
        raise Freno(f"proyección {proy:.3f} > {c.a.freno_proyeccion}")
    for q in preguntas:
        for b in BRAZOS:
            c.sesion(b, f"{q['id']}-{b}", q["pregunta"], out)
    for b in BRAZOS:
        c.sesion(b, f"E2E-{b}", preg_e2e, out)
    (out / "trazas").mkdir(parents=True, exist_ok=True)
    filas = []
    for q in preguntas:
        for b in BRAZOS:
            pid = f"{q['id']}-{b}"
            st, lg = out / f"stream_{pid}.jsonl", out / f"log_r1_{pid}.jsonl"
            if not st.exists() or not lg.exists():
                filas.append({"id": pid, "adaptado": False, "motivo": "sin stream o sin log R1"})
                continue
            p = adaptar(st, lg, {"caso_id": pid, "brazo": b, "pregunta": q["pregunta"], "anclas_gold": q["anclas"]},
                        servidor="mcp_vector")
            (out / "trazas" / f"{pid}.json").write_text(json.dumps(p, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            filas.append({"id": pid, "brazo": b, "adaptado": True, "n_steps": p["gate"]["n_steps_adaptados"],
                          "mapa_R7_ok": all(x.get("ok") for x in p["gate"]["mapa_steps"]),
                          "atribuible": p["gate"]["atribuible"], "completa": p["banco"]["completitud_R3"],
                          "truncados_por_transporte": p["banco"]["steps_con_sesion_truncada"],
                          "max_output_chars": max([s["output_chars"] or 0 for s in p["trace"]["steps"]] or [0])})
    c.registro["trazas"] = filas


def evaluar_hb2(metas: list[dict]) -> dict:
    """Reglas de decisión de a2_1/diseno_HB2.md (§5), sobre los conteos de meta["hb2"]."""
    filas = [{"id": m["pregunta_id"], "brazo": m["brazo"]} | m["hb2"] for m in metas if m.get("hb2")]
    validas = [f for f in filas if f["hay_result"] and f["num_turns"] is not None]
    excluidas = [f["id"] for f in filas if f not in validas]
    # R-a: qué cuenta num_turns
    candidatos_a = {
        "n_tool_result+1": lambda f: f["n_tool_result"] + 1,
        "n_mensajes_asistente": lambda f: f["n_mensajes_asistente"],
        "n_eventos_user+1": lambda f: f["n_eventos_user"] + 1,
        "n_llamadas_log_r1+1": lambda f: (f["n_llamadas_log_r1"] or 0) + 1,
    }
    ra = {k: {"coincide_en": sum(fn(f) == f["num_turns"] for f in validas), "de": len(validas),
              "difiere_en": [f["id"] for f in validas if fn(f) != f["num_turns"]]} for k, fn in candidatos_a.items()}
    verif_a = [k for k, v in ra.items() if v["de"] and v["coincide_en"] == v["de"]]
    # R-b: qué conteo acota --max-turns
    candidatos_b = {"n_mensajes_asistente": "n_mensajes_asistente", "num_turns": "num_turns",
                    "n_tool_use": "n_tool_use", "n_llamadas_log_r1": "n_llamadas_log_r1"}
    rb = {}
    for k, campo in candidatos_b.items():
        incompatibles = []
        for f in validas:
            v, lim = f[campo] or 0, f["max_turns_efectivo"]
            if f["corte_disparado"]:
                if v not in (lim, lim + 1):
                    incompatibles.append({"id": f["id"], "corte": True, campo: v, "max_turns": lim})
            elif v > lim:
                incompatibles.append({"id": f["id"], "corte": False, campo: v, "max_turns": lim})
        al_cortar = sorted({(f[campo] or 0) - f["max_turns_efectivo"] for f in validas if f["corte_disparado"]})
        rb[k] = {"compatible": not incompatibles, "incompatibles": incompatibles,
                 "valor_menos_max_turns_al_cortar": al_cortar}
    compatibles_b = [k for k, v in rb.items() if v["compatible"]]
    n_cortes = sum(f["corte_disparado"] for f in validas)
    hay_paralelas = any(f["max_tool_use_por_mensaje"] > 1 for f in validas)
    if n_cortes == 0:
        estado_b = "NO CARACTERIZADO: ninguna sesión disparó el corte"
    elif len(compatibles_b) == 1:
        estado_b = f"CARACTERIZADO: --max-turns acota {compatibles_b[0]}"
    elif not compatibles_b:
        estado_b = "NO CARACTERIZADO: ningún conteo candidato es compatible con todas las sesiones"
    else:
        estado_b = f"INDISTINGUIBLE con estas sesiones entre {compatibles_b}"
    cortes = [{"id": f["id"], "max_turns": f["max_turns_efectivo"], "subtype": f["subtype"], "is_error": f["is_error"],
               "n_mensajes_asistente": f["n_mensajes_asistente"], "n_tool_use": f["n_tool_use"],
               "n_tool_result": f["n_tool_result"], "num_turns": f["num_turns"],
               "n_llamadas_log_r1": f["n_llamadas_log_r1"], "log_r1_con_fin": f["log_r1_con_fin"]}
              for f in validas if f["corte_disparado"]]
    return {"n_sesiones": len(filas), "n_validas": len(validas), "excluidas_sin_result": excluidas,
            "n_cortes": n_cortes, "hubo_llamadas_paralelas": hay_paralelas,
            "R_a_num_turns": {"candidatos": ra, "verificados": verif_a,
                              "estado": (f"VERIFICADO: num_turns = {verif_a}" if verif_a else "NO VERIFICADO")},
            "R_b_max_turns": {"candidatos": rb, "compatibles": compatibles_b, "estado": estado_b},
            "R_c_al_cortar": cortes, "filas": filas}


def componer(diseno: dict, preguntas: dict, ids: list[str]) -> str:
    """Una pregunta propia tal cual, o varias en la plantilla compuesta del diseño (una por línea numerada)."""
    if len(ids) == 1:
        return preguntas[ids[0]]
    partes = "\n".join(f"({k}) {preguntas[i]}" for k, i in enumerate(ids, 1))
    return diseno["plantilla_compuesta"].format(n=len(ids), preguntas=partes)


def fase_hb2(c: Corrida, out: Path, out_smoke: Path) -> None:
    diseno = json.loads(DISENO_HB2.read_text(encoding="utf-8"))
    preguntas = {q["id"]: q["pregunta"] for q in json.loads(PREGUNTAS.read_text(encoding="utf-8"))["preguntas"]}
    metas = []
    for s in diseno["sesiones"]:
        texto = componer(diseno, preguntas, s["preguntas"])
        metas.append(c.sesion(s["brazo"], s["id"], texto, out, max_turns=s["max_turns"]))
    controles = [json.loads(p.read_text(encoding="utf-8")) for p in sorted(out_smoke.glob("meta_*.json"))] if out_smoke.exists() else []
    c.registro["evaluacion"] = evaluar_hb2(metas + controles)
    c.registro["evaluacion"]["controles_del_smoke"] = [m["pregunta_id"] for m in controles]
    # Segunda lectura, declarada en el diseño antes de correr: con las 12 sesiones de la corrida 2 de la
    # fase B (mismo CLI 2.1.241 y mismos flags, --max-turns 12) como antecedente.
    import antecedente_HB2_faseB as ANT
    c.registro["evaluacion_con_antecedente_faseB"] = evaluar_hb2(metas + controles + ANT.metas_faseB())


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fase", choices=["smoke", "hb2"], required=True)
    ap.add_argument("--autorizado-tope", type=float, required=True, help="tope autorizado en USD (explícito)")
    ap.add_argument("--freno", type=float, default=2.0, help="freno acumulado (R9) en USD, para todo el tramo 2")
    ap.add_argument("--freno-proyeccion", type=float, default=2.4)
    ap.add_argument("--modo", choices=["real", "init"], default="real")
    ap.add_argument("--via", choices=["api", "bedrock"], default="api")
    ap.add_argument("--out-smoke", type=Path, default=OUT_SMOKE)
    ap.add_argument("--out-hb2", type=Path, default=OUT_HB2)
    a = ap.parse_args(argv)
    if a.autorizado_tope <= 0:
        raise SystemExit("sin tope autorizado no se corre nada")
    c = Corrida(a, [a.out_smoke, a.out_hb2])
    out = a.out_smoke if a.fase == "smoke" else a.out_hb2
    out.mkdir(parents=True, exist_ok=True)
    nombre = "registro_smoke_a2_1.json" if a.fase == "smoke" else "registro_HB2.json"
    try:
        if a.fase == "smoke":
            fase_smoke(c, out)
        else:
            fase_hb2(c, out, a.out_smoke)
    except Freno as e:
        c.registro["FRENO"] = str(e)
        c.cerrar(out, nombre)
        print("FRENO:", e)
        return 2
    c.cerrar(out, nombre)
    print(json.dumps({k: c.registro.get(k) for k in ("P0", "proyeccion_usd", "gasto_R9_usd_tramo2", "gasto_cli_usd_tramo2",
                                                     "razon_cli_sobre_R9")}, ensure_ascii=False, indent=1))
    if a.fase == "hb2":
        ev = c.registro["evaluacion"]
        print("H-B2:", ev["R_a_num_turns"]["estado"], "|", ev["R_b_max_turns"]["estado"])
        ev2 = c.registro["evaluacion_con_antecedente_faseB"]
        print("H-B2 con el antecedente de la fase B:", ev2["R_a_num_turns"]["estado"], "|", ev2["R_b_max_turns"]["estado"])
    print("->", rel_repo(out / nombre))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
