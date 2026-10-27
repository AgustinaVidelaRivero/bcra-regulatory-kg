#!/usr/bin/env python3
"""selftest_analizar_n6.py — El selftest del análisis de N6 (analizar_n6.py) sobre datos de juguete, a USD 0. Arma, en una
carpeta de trabajo fuera del repo, una salida de N6 con las 10 configuraciones de n6/config_agentes_n6.json y 6 preguntas
sintéticas con la forma de las de N3 (ninguna pregunta real): por sesión, su meta, su stream, su comando y su log R1, en
agente/lote_01/, y los agregados del juez; corre analizar_n6.analizar sobre ella y compara cada medida y cada paso de la regla de
decisión con los valores calculados a mano en este archivo (ESPERADO). El instrumento de citas corre de verdad, sobre la E0 del
acumulado de la copia.

El juguete (2 criterios por pregunta; todo «cumplido» salvo lo que sigue):
  · B: en la corrida 2, un criterio no cumplido en N3-C1; en la 3, los dos de N3-M01;
  · T−F1: los dos de N3-C1 no cumplidos (no es elegible: 1 > V(Q1) = 0,5);
  · T−F3: uno de N3-C2 no cumplido (elegible: 0,25 ≤ V(Q3) = 0,5);
  · T−F4: N3-C3 cortada por R5 (sin veredicto: sale de la métrica; en la sensibilidad, no cumplida);
  · T−F5: N3-M01 con la salida mal formada (sin veredicto);
  · T y T−F6: una sesión con 30 llamadas (al tope);
  · F1_bm25: en la corrida 2, uno de N3-C1 no cumplido; la híbrida, los dos de N3-M02 (no entra);
  · R9 medio: T−F3 la más barata; T−F2 vio una marca («no verificada») en N3-C1;
  · las citas: las sesiones de T−F3 citan un punto que no vieron y que no existe; las demás, el ancla que vieron;
  · la decisión 9: N3-C4 es una de las cuatro preguntas que se sacan de toda comparación entre una configuración con los ejemplos
    de la familia 6 y una sin ellos. B falla sus dos criterios en las 3 corridas, y T−F6 uno: el Δ de B y de T−F6 contra T, y la
    elección (con B y T entre las candidatas), dan distinto sobre las 5 sin N3-C4 y sobre las 6 (la sensibilidad, al lado).
Uso: .venv/bin/python -B data/experiment/banco_mcp/n6/selftest_analizar_n6.py --trabajo <carpeta nueva fuera del repo>
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import analizar_n6 as A          # desde su carpeta, como el análisis
CN = A.CN

PREGUNTAS = {
    "N3-C1": {"conjunto": "cupo", "necesidad": 1, "tipo": "dato_directo", "subtipo": None},
    "N3-C2": {"conjunto": "cupo", "necesidad": 2, "tipo": "varios_puntos", "subtipo": "remision"},
    "N3-C3": {"conjunto": "cupo", "necesidad": 3, "tipo": "dato_directo", "subtipo": None},
    "N3-C4": {"conjunto": "cupo", "necesidad": 4, "tipo": "dato_directo", "subtipo": None},
    "N3-M01": {"conjunto": "mezcla", "necesidad": None, "tipo": "varios_puntos", "subtipo": "remision"},
    "N3-M02": {"conjunto": "mezcla", "necesidad": None, "tipo": "dato_directo", "subtipo": None},
}
LISTA_F5 = ["N3-M01", "N3-C2"]          # N3-C2 es de cupo: Q5 toma solo las de la mezcla
NC, CU = "no_cumplido", "cumplido"
MODALES = {("B", 2, "N3-C1"): [CU, NC], ("B", 3, "N3-M01"): [NC, NC], ("T-F1", 1, "N3-C1"): [NC, NC],
           ("T-F3", 1, "N3-C2"): [NC, CU], ("F1_bm25", 2, "N3-C1"): [CU, NC], ("F1_hibrida", 1, "N3-M02"): [NC, NC],
           ("B", 1, "N3-C4"): [NC, NC], ("B", 2, "N3-C4"): [NC, NC], ("B", 3, "N3-C4"): [NC, NC],
           ("T-F6", 1, "N3-C4"): [CU, NC]}
CLASE = {("T-F4", 1, "N3-C3"): "corte_R5", ("T-F5", 1, "N3-M01"): "mal_formada"}
AL_TOPE = {("T", 1, "N3-M02"), ("T-F6", 1, "N3-M02")}
MARCA = {("T-F2", 1, "N3-C1")}
COSTO = {"B": 0.03, "T-F2": 0.02, "T-F3": 0.01}     # R9 por sesión; las demás, 0,02


def uso_de(costo: float) -> dict:
    """Un modelUsage de claude-sonnet-5 que da ese R9 (solo tokens de entrada, a USD 2 por millón)."""
    return {"claude-sonnet-5": {"inputTokens": round(costo / 2.0 * 1e6), "outputTokens": 0, "cacheReadInputTokens": 0,
                                "cacheCreationInputTokens": 0}}


def armar(trabajo: Path) -> tuple[dict, Path]:
    cfg = json.loads(CN.CONFIG_AGENTES.read_text(encoding="utf-8"))
    ps = {q: {"pregunta": f"pregunta sintética {q}", "to": "cla", "anclas": ["cla::5.1.1"],
              "criterios": [{"criterio": f"criterio {q}.{i}", "cita_textual": f"cita {i}"} for i in (1, 2)], **m}
          for q, m in PREGUNTAS.items()}
    e = {"_preguntas": ps, "_cfg": cfg, "orden": CN.armar_orden(list(ps), cfg), "presupuesto_por_sesion_usd": 1.8,
         "_sha": "selftest"}
    salida = trabajo / "salida"
    lote = salida / "agente" / "lote_01"
    agregados = []
    for s in e["orden"]["sesiones"]:
        k = (s["configuracion"], s["rep"], s["qid"])
        clase = CLASE.get(k, "completa")
        pid, d = s["id"], lote / s["id"]
        d.mkdir(parents=True)
        resp = f"respuesta sintética de {pid}"
        cita = "cla | 9.9.9" if s["configuracion"] == "T-F3" else "cla | 5.1.1"
        completa = clase == "completa"
        meta = {"brazo": s["brazo"], "modelos_R8": {"uso_por_modelo": uso_de(COSTO.get(s["configuracion"], 0.02))},
                "servidores_mcp": {"en_init": [{"name": "kg", "status": "connected"}]},
                "inventario_tools_R6": {"coincide": True},
                "completitud_R3": {"completa": completa, "motivos_incompleta": [] if completa else (
                    ["JSON final no parseable: sintético"] if clase == "mal_formada" else ["result.subtype=error_max_turns"])},
                "hb2": {"n_llamadas_log_r1": 30 if k in AL_TOPE else 5},
                "final_json_R4": ({"respuesta": resp, "citas": [cita], "respondible": True} if clase != "mal_formada" else None)}
        (d / f"meta_{pid}.json").write_text(json.dumps(meta, ensure_ascii=False), encoding="utf-8")
        (d / f"comando_{pid}.json").write_text("{}", encoding="utf-8")
        sub = "error_max_turns" if clase == "corte_R5" else "success"
        (d / f"stream_{pid}.jsonl").write_text(json.dumps({"type": "result", "subtype": sub, "is_error": clase == "corte_R5"})
                                               + "\n", encoding="utf-8")
        salida_tool = json.dumps({"consulta": "x", "total_pasajes": 1, "resultados": [
            {"to": "cla", "unidad": "5.1.1", "texto": "texto sintético" + (" no verificada" if k in MARCA else "")}]},
            ensure_ascii=False)
        (d / f"log_r1_{pid}.jsonl").write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in (
            {"evento": "inicio"}, {"evento": "llamada", "n": 1, "call_id": "c1", "tool": "buscar_pasajes", "input": {},
                                   "output_str": salida_tool, "output_chars": len(salida_tool), "output_sha256": "x",
                                   "error": None}, {"evento": "fin"})) + "\n", encoding="utf-8")
        if completa:
            agregados.append({"id_opaco": CN.id_opaco(s["qid"], s["configuracion"], s["rep"], CN.sha256_texto(resp)),
                              "n_criterios": 2, "modales": MODALES.get(k, [CU, CU])})
    (salida / "juez").mkdir(parents=True)
    (salida / "juez" / "agregados_n6_ciego.json").write_text(json.dumps({"agregados": agregados}), encoding="utf-8")
    return e, salida


ESPERADO = {
    "fidelidad_30": {"B": 0.75, "T": 1.0, "T-F1": 0.833333, "T-F2": 1.0, "T-F3": 0.916667, "T-F4": 1.0, "T-F5": 1.0,
                     "T-F6": 0.916667},
    "fidelidad_sin_FUERA_D9": {"B": 0.9, "T": 1.0, "T-F1": 0.8, "T-F2": 1.0, "T-F3": 0.9, "T-F4": 1.0, "T-F5": 1.0, "T-F6": 1.0},
    "V": {"30": 0.166666, "1": 0.5, "2": 0.0, "3": 0.5, "4": 0.0, "5": 1.0, "6": 1.0},
    "V_sin_FUERA_D9_30": 0.2,
    "elegibles": {"T-F1": False, "T-F2": True, "T-F3": True, "T-F4": False, "T-F5": False, "T-F6": True},
    "candidatas": ["B", "T", "T-F2", "T-F3", "T-F6"],
    "dentro_de_V_26": ["B", "T", "T-F2", "T-F3", "T-F6"],
    "orden_26": ["T-F3", "T-F2", "B", "T", "T-F6"],
    "dentro_de_V_30": ["T", "T-F2", "T-F3", "T-F6"],
    "elegida": "T-F3",
    "conjuntos": {"30": ["N3-C1", "N3-C2", "N3-C3", "N3-C4", "N3-M01", "N3-M02"], "1": ["N3-C1"], "2": ["N3-C4"],
                  "3": ["N3-C2", "N3-M01"], "4": ["N3-C3"], "5": ["N3-M01"], "6": ["N3-M01"]},
    "F1": {"fidelidad_bm25": 0.972222, "fidelidad_hibrida": 0.833333, "V": 0.083333, "entra": False},
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--trabajo", type=Path, required=True)
    a = ap.parse_args()
    t = a.trabajo.resolve()
    if t.exists() or t.is_relative_to(CN.REPO_DIR):
        raise SystemExit("FRENO: la carpeta de trabajo tiene que ser nueva y estar fuera del repo")
    e, salida = armar(t)
    caso = {"configuracion": "T", "llamadas": 2, "llega_en_2_llamadas_o_menos": True}
    r = A.analizar(e, salida, LISTA_F5, caso, t / "citas")
    res = []

    def chequeo(nombre, ok, det=""):
        res.append({"chequeo": nombre, "ok": bool(ok), "detalle": det})
        print(("OK   " if ok else "FALLA ") + nombre + (f" · {det}" if det else ""))

    rg = r["regla"]
    chequeo("las sesiones: 6 preguntas × 14 corridas, con sus clases", r["n_sesiones"] == 84
            and r["clases"] == {"completa": 82, "corte_R5": 1, "mal_formada": 1}, json.dumps(r["clases"]))
    chequeo("los conjuntos Qk de N4, §3 (Q5 solo con las de la mezcla de la lista)", r["conjuntos"] == ESPERADO["conjuntos"])
    chequeo("la fidelidad por criterio sobre las 30, por configuración (B junta sus 3 corridas)",
            rg["fidelidad_30"] == ESPERADO["fidelidad_30"], json.dumps(rg["fidelidad_30"]))
    chequeo("B por corrida: 0,833333, 0,75 y 0,666667",
            [r["medidas"]["B"]["por_corrida"][k]["fidelidad"] for k in (1, 2, 3)] == [0.833333, 0.75, 0.666667])
    chequeo("la decisión 9: la fidelidad sin las cuatro preguntas (N3-C4 en el juguete) y V sobre las mismas",
            rg["fidelidad_sin_FUERA_D9"] == ESPERADO["fidelidad_sin_FUERA_D9"]
            and rg["V_sin_FUERA_D9"]["30"]["V"] == ESPERADO["V_sin_FUERA_D9_30"]
            and rg["fuera_de_las_comparaciones_con_y_sin_ejemplos"] == ["N3-C4", "N3-M05", "N3-M18", "N3-M21"],
            json.dumps(rg["fidelidad_sin_FUERA_D9"]))
    chequeo("V(Q) de B, sobre las 30 y cada Qk", {k: v["V"] for k, v in rg["V"].items()} == ESPERADO["V"],
            json.dumps({k: v["V"] for k, v in rg["V"].items()}))
    chequeo("por familia: T−Fk elegible si fid(T, Qk) − fid(T−Fk, Qk) ≤ V(Qk)",
            {k: v["elegible"] for k, v in rg["familias"].items()} == ESPERADO["elegibles"],
            json.dumps({k: (v["T_menos_TFk"], v["V_Qk"], v["elegible"]) for k, v in rg["familias"].items()}))
    el = rg["eleccion"]
    chequeo("la decisión 9: con B y T entre las candidatas, la elección va sobre las 5 sin N3-C4, con V(26) = 0,2, y el desempate",
            el["sobre"].startswith("las 5 sin") and el["candidatas"] == ESPERADO["candidatas"] and el["V"] == 0.2
            and el["dentro_de_V"] == ESPERADO["dentro_de_V_26"] and el["orden_de_desempate"] == ESPERADO["orden_26"]
            and el["elegida"] == ESPERADO["elegida"], f"{el['orden_de_desempate']}")
    e30 = el["con_las_30"]
    chequeo("la decisión 9: la elección con las 30 va al lado (B queda fuera de V(30), y gana T−F3)",
            e30["V"] == 0.166666 and e30["dentro_de_V"] == ESPERADO["dentro_de_V_30"] and e30["elegida"] == "T-F3",
            f"{e30['dentro_de_V']}")
    chequeo("el requisito de la jerarquía: T−F3 tiene ver_punto y pasa", el["caso_de_la_jerarquia"]["pasa"] is True)
    filas = A.cargar_sesiones(e, salida)
    for f in filas:
        if f["configuracion"] == "T-F2":
            f["r9_final_usd"] = 0.001
    tvp = {b["configuracion_n6"]: "mcp__kg__ver_punto" in b["tools_esperadas"] for b in e["_cfg"]["brazos"].values()
           if b.get("servidor") == "kg"}
    rg2 = A.regla(filas, A.conjuntos(e, LISTA_F5), caso, tvp)
    chequeo("con T−F2 la más barata, gana T−F2 y, sin ver_punto, vuelve a la autora",
            rg2["eleccion"]["elegida"] == "T-F2" and rg2["eleccion"]["caso_de_la_jerarquia"]["pasa"] is False
            and rg2["eleccion"]["se_preregistra_asi"] is False)
    d = rg["contra_T"]["T-F1"]
    chequeo("Δ pareado de T−F1 contra T (los dos con los ejemplos: con las 30): −1/6, una baja y cinco iguales",
            d == {"sobre": "las 30", "delta": -0.166667, "preguntas_comunes": 6, "suben": 0, "bajan": 1, "igual": 5}, json.dumps(d))
    db, d6 = rg["contra_T"]["B"], rg["contra_T"]["T-F6"]
    chequeo("la decisión 9: Δ de B contra T sin N3-C4 (−0,1; 2 bajan, 3 iguales) y con las 30 al lado (−0,25; 3 bajan)",
            (db["delta"], db["preguntas_comunes"], db["bajan"], db["igual"]) == (-0.1, 5, 2, 3)
            and (db["con_las_30"]["delta"], db["con_las_30"]["preguntas_comunes"], db["con_las_30"]["bajan"]) == (-0.25, 6, 3),
            json.dumps({k: db[k] for k in ("delta", "bajan", "igual")}))
    chequeo("la decisión 9: Δ de T−F6 contra T sin N3-C4 (0) y con las 30 al lado (−0,083333; 1 baja)",
            (d6["delta"], d6["igual"], d6["con_las_30"]["delta"], d6["con_las_30"]["bajan"]) == (0.0, 5, -0.083333, 1))
    f6 = rg["familias"]["T-F6"]
    chequeo("la decisión 9: la elegibilidad de la familia 6 va sobre Q6 sin las cuatro, con la de Q6 al lado",
            f6["sobre"].startswith("Qk sin") and f6["Qk"] == ["N3-M01"] and f6["elegible"] is True
            and f6["con_las_30"]["elegible"] is True and rg["familias"]["T-F3"]["sobre"] == "Qk")
    f1 = rg["F1"]
    chequeo("F1: la híbrida no entra (0,833333 < 0,972222 − 0,083333)",
            (f1["fidelidad_bm25"], f1["fidelidad_hibrida"], f1["Vfrag_30"]["V"], f1["entra_la_hibrida"])
            == (ESPERADO["F1"]["fidelidad_bm25"], ESPERADO["F1"]["fidelidad_hibrida"], ESPERADO["F1"]["V"], ESPERADO["F1"]["entra"]))
    m4 = r["medidas"]["T-F4"]
    chequeo("sin veredicto: el corte por R5 sale de la métrica y en la sensibilidad cuenta como no cumplido",
            m4["30"]["sin_veredicto"] == 1 and m4["30"]["criterios"] == 10 and m4["30_sensibilidad"]["criterios"] == 12
            and m4["30_sensibilidad"]["fidelidad"] == 0.833333 and m4["Q4"]["fidelidad"] is None)
    chequeo("la regla de sensibilidad: T−F4 sigue sin ser elegible (1 > V(Q4) = 0)",
            r["regla_sensibilidad"]["familias"]["T-F4"]["elegible"] is False
            and r["regla_sensibilidad"]["familias"]["T-F4"]["T_menos_TFk"] == 1.0)
    op = r["medidas"]["T"]["operativo"]
    chequeo("lo operativo: al tope, llamadas y R9 medio por pregunta",
            op["al_tope"] == 1 and op["llamadas_max"] == 30 and op["r9_medio_por_pregunta_usd"] == 0.02
            and r["medidas"]["T-F4"]["operativo"]["al_tope"] == 1 and r["medidas"]["T-F3"]["operativo"]["r9_medio_por_pregunta_usd"] == 0.01)
    mv = r["medidas"]["T-F2"]
    chequeo("lo verificado aparte: T−F2 vio una marca en N3-C1", mv["preguntas_con_marca_vista"] == 1
            and mv["vio_una_marca"]["criterios"] == 2 and mv["no_vio_ninguna_marca"]["criterios"] == 10)
    ci = r["citas"]
    pc = ci.get("por_configuracion", {})
    chequeo("las citas, con el instrumento de la decisión 4: T−F3 cita un punto que no vio ni existe; T, el ancla que vio",
            ci["estado"] == "medida" and pc["T-F3"]["ind1_cita_fundada"].get("no") == 6
            and pc["T-F3"]["ind2_cita_existente"].get("no") == 6 and pc["T-F3"]["ind3_cita_al_ancla"].get("no") == 6
            and pc["T"]["ind1_cita_fundada"].get("si") == 6 and pc["T"]["ind3_cita_al_ancla"].get("si") == 6
            and pc["T-F5"]["N"] == 6, json.dumps({c: pc[c]["ind1_cita_fundada"] for c in ("T", "T-F3", "T-F5")}))
    nc = A.no_cumplidos(filas)
    chequeo("la entrada de N1: los criterios no cumplidos, por sesión", sum(len(x["criterios_no_cumplidos"]) for x in nc) == 16
            and r["clases_n1"]["estado"] == "PENDIENTE")
    regla_n1 = "db2cc290" + "0" * 56
    p = t / "clases_n1_juguete.json"
    p.write_text(json.dumps({"sha256_regla": regla_n1, "filas": [{"id": x["id"], "criterio": c, "clase": "1"}
                                                                 for x in nc for c in x["criterios_no_cumplidos"]]}), encoding="utf-8")
    c1 = A.clases_n1(p, regla_n1, filas)
    chequeo("las clases de N1, con una clasificación que cubre los no cumplidos y trae la regla", c1["estado"] == "contada"
            and sum(sum(v.values()) for v in c1["por_configuracion"].values()) == 16)
    try:
        A.clases_n1(p, "0" * 64, filas)
        aborta = False
    except SystemExit:
        aborta = True
    chequeo("una clasificación sin el sha256 de la regla sellada aborta", aborta)
    texto = json.dumps(r, ensure_ascii=False)
    chequeo("la salida no trae texto de preguntas, criterios ni respuestas",
            "pregunta sintética" not in texto and "criterio N3" not in texto and "respuesta sintética" not in texto)
    n_ok = sum(x["ok"] for x in res)
    (t / "selftest_analizar_n6.json").write_text(json.dumps({"chequeos": res, "ok": n_ok, "total": len(res)},
                                                            ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{n_ok} de {len(res)} chequeos OK")
    return 0 if n_ok == len(res) else 1


if __name__ == "__main__":
    raise SystemExit(main())
