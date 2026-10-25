#!/usr/bin/env python3
"""selftest_a2_2.py — El selftest de las funciones de A2.2 que no lanzan sesiones (USD 0, sin API y sin leer EV2): el orden y las
semillas, la población de N = 3 y la agregación de sus re-corridas, la prueba exacta con Holm, Wilson, la cola (A-D11), la
ceguera y la agregación del juez, el enmascarado sobre copias sintéticas y el control de EV2 sobre un archivo sintético con su
esquema. La muestra de la auditoría se compara con la de EV2: la función `muestra_auditoria` de
`ev2_encadenamiento/code/comun_enc.py` se extrae de su árbol de sintaxis y se ejecuta con la semilla de A2.2, sin importar el
módulo (que carga la corrida base de EV2).

Corre sobre una copia (CLAUDE.md, §4.l): todo lo que escribe va a carpetas temporales. Imprime un renglón por prueba.
Uso: .venv/bin/python -B data/experiment/banco_mcp/a2_2/selftest_a2_2.py
"""
from __future__ import annotations

import ast
import json
import math
import random
import subprocess
import sys
import tempfile
from pathlib import Path

AQUI = Path(__file__).resolve().parent
if str(AQUI) not in sys.path:
    sys.path.insert(0, str(AQUI))
import comun_a2_2 as K                  # noqa: E402
import poblacion_a2_2 as PB             # noqa: E402
import analizar_a2_2 as AN              # noqa: E402
import juez_a2_2 as JA                  # noqa: E402
import control_ev2_a2_2 as CE           # noqa: E402

RES = []


def prueba(nombre: str, ok: bool, det: str = "") -> None:
    RES.append(bool(ok))
    print(("PASS " if ok else "FAIL ") + nombre + (f" — {det}" if det else ""), flush=True)


def muestra_de_ev2(semilla: str):
    """La función de EV2, tal cual en su código, con la semilla de A2.2 en el lugar de la suya."""
    src = (K.EXP_DIR / "ev2_encadenamiento" / "code" / "comun_enc.py").read_text(encoding="utf-8")
    f = next(n for n in ast.parse(src).body if isinstance(n, ast.FunctionDef) and n.name == "muestra_auditoria")
    ns = {"math": math, "random": random, "FRACCION_AUDITORIA": 0.10, "MINIMO_AUDITORIA_POR_GRAFO": 1,
          "SEMILLA_AUDITORIA": semilla}
    exec(compile(ast.Module(body=[f], type_ignores=[]), "comun_enc.muestra_auditoria", "exec"), ns)  # noqa: S102
    return ns["muestra_auditoria"]


def a(qid, b, rep, v, idop=None, modales=None, clas="contenido"):
    return {"id_opaco": idop or f"A22J-{qid}-{b}-{rep}", "veredicto_pregunta": v, "n_criterios": len(modales or ["cumplido"]),
            "modales": modales or ["cumplido"], "clasificacion_respuesta_modal": clas}


def main() -> int:
    # 1. el orden
    ids = [f"Q{i:02d}" for i in range(1, 11)]
    o1, o2 = K.armar_orden(ids), K.armar_orden(list(reversed(ids)))
    prueba("orden: determinista e independiente del orden de entrada", o1 == o2 and sorted(o1["preguntas_en_orden"]) == ids)
    prueba("orden: cada repetición de cada pregunta es una permutación de los tres brazos",
           all(sorted(o1["brazos_por_pregunta"][q][f"r{r}"]) == sorted(K.BRAZOS) for q in ids for r in K.REPETICIONES))
    xs = sorted(ids); random.Random("A22:orden_corridas:v1").shuffle(xs)
    prueba("orden: las preguntas con random.Random('A22:orden_corridas:v1').shuffle sobre los ids ordenados",
           xs == o1["preguntas_en_orden"])
    bb = sorted(K.BRAZOS); random.Random("A22:orden_corridas:v1:Q03:r2").shuffle(bb)
    prueba("orden: los brazos con random.Random(f'A22:orden_corridas:v1:{id}:r{r}')", bb == o1["brazos_por_pregunta"]["Q03"]["r2"])
    sp, sn = K.secuencia(o1, "pruebas"), K.secuencia(o1, "n1")
    prueba("secuencia: 3 pruebas (una por brazo, ordenadas) y 30 de N = 1", [s["brazo"] for s in sp] == sorted(K.BRAZOS)
           and len(sn) == 30 and [s["qid"] for s in sn[:3]] == [o1["preguntas_en_orden"][0]] * 3)
    pob = {"pares": [{"qid": "Q01", "brazo": "kg"}, {"qid": "Q05", "brazo": "fragmentos_bm25"}]}
    sr = K.secuencia(o1, "recorridas", pob)
    prueba("secuencia de re-corridas: por repetición (r2, r3, r4), 2 pares × 3 = 6, ids RC1..RC3",
           len(sr) == 6 and [s["rep"] for s in sr] == [2, 2, 3, 3, 4, 4] and sr[0]["id"].startswith("RC1-"))

    # 2. la población
    ev2 = muestra_de_ev2(K.SEMILLA_AUDITORIA)
    casos = [{"fragmentos_bm25": [f"Q{i:02d}" for i in range(n)], "kg": [f"Q{i:02d}" for i in range(m)], "fragmentos_denso": []}
             for n, m in ((1, 3), (9, 10), (11, 21), (40, 7))]
    prueba("auditoría: la misma muestra que la función de EV2 con la semilla de A2.2 (4 casos)",
           all(PB.muestra_auditoria(c) == ev2(c) for c in casos))
    prueba("auditoría: max(ceil(10 % · n), 1) y 0 sin correctos",
           [len(PB.muestra_auditoria({"kg": list(range(n))})["kg"]) for n in (0, 1, 9, 10, 11, 40)] == [0, 1, 1, 1, 2, 4])
    v1 = {}
    plan = {"kg": ["parcial", "correcto", "correcto", "requiere_adjudicacion", "incorrecto"],
            "fragmentos_bm25": ["correcto"] * 5, "fragmentos_denso": ["parcial", "parcial", "incorrecto", "incorrecto", "correcto"]}
    for b, vs in plan.items():
        for i, v in enumerate(vs):
            v1[(f"Q{i:02d}", b, 1)] = a(f"Q{i:02d}", b, 1, v)
    d = PB.derivar(v1, [f"Q{i:02d}" for i in range(5)])
    prueba("población: dispara solo «parcial» del código (requiere_adjudicacion no)",
           d["n_parciales_por_brazo"] == {"fragmentos_bm25": 0, "fragmentos_denso": 2, "kg": 1})
    prueba("población: la auditoría por brazo y P = parciales + auditadas",
           d["n_auditoria_por_brazo"] == {"fragmentos_bm25": 1, "fragmentos_denso": 1, "kg": 1}
           and d["P_por_brazo"] == {"fragmentos_bm25": 1, "fragmentos_denso": 3, "kg": 2} and d["n_sesiones_recorridas"] == 18)
    vrc = {}
    votos = {("Q00", "kg"): ["correcto", "correcto", "parcial"], ("Q00", "fragmentos_denso"): ["correcto", "parcial", "incorrecto"],
             ("Q01", "fragmentos_denso"): ["correcto", "correcto", "requiere_adjudicacion"],
             ("Q04", "fragmentos_denso"): ["correcto", "parcial", "requiere_adjudicacion"]}
    for (q, b), vs in votos.items():
        for r, v in zip(K.REPS_RECORRIDA, vs):
            vrc[(q, b, r)] = a(q, b, r, v)
    pob5 = {"pares": [{"qid": q, "brazo": b, "tipo": "parcial_disparado"} for (q, b) in votos] +
            [{"qid": "Q03", "brazo": "fragmentos_bm25", "tipo": "auditoria_correcto"}]}
    ag = PB.agregar_recorridas(pob5, vrc)
    fin = {(p["qid"], p["brazo"]): p["final"] for p in ag["pares"]}
    prueba("agregación (agregacion_enc): mayoría, empate triple a parcial, pendiente invariante y dependiente, incompleto",
           fin == {("Q00", "kg"): "correcto", ("Q00", "fragmentos_denso"): "parcial", ("Q01", "fragmentos_denso"): "correcto",
                   ("Q04", "fragmentos_denso"): "requiere_adjudicacion"} and ag["n_incompletos"] == 1)

    # 3. la estadística
    prueba("prueba exacta: 10 discordantes a favor → p = 2/1024", abs(AN.p_signos_exacta([1] * 10) - 2 / 1024) < 1e-15)
    prueba("prueba exacta: 5 a favor y 0 en contra con ceros → p = 2/32",
           abs(AN.p_signos_exacta([1] * 5 + [0] * 7) - 0.0625) < 1e-15)
    prueba("prueba exacta: sin discordantes → 1; 1 y 1 → 1; 8 contra 2 → 0,109375",
           AN.p_signos_exacta([0, 0]) == 1.0 and AN.p_signos_exacta([1, -1]) == 1.0
           and abs(AN.p_signos_exacta([1] * 8 + [-1] * 2) - 0.109375) < 1e-15)
    h1, h2, h3 = AN.holm({"x": 0.01, "y": 0.04}), AN.holm({"x": 0.06, "y": 0.01}), AN.holm({"x": 0.03, "y": 0.04})
    prueba("Holm: la primera a 0,025, la segunda a 0,05; se detiene en la primera que no rechaza",
           h1["x"]["rechaza"] and h1["y"]["rechaza"] and h1["x"]["umbral_holm"] == 0.025 and h1["y"]["umbral_holm"] == 0.05
           and h2["y"]["rechaza"] and not h2["x"]["rechaza"] and not h3["x"]["rechaza"] and not h3["y"]["rechaza"])
    w = AN.wilson(0, 10)
    prueba("Wilson: 0 de 10 → [0; 0,2775] y 5 de 10 → [0,2366; 0,7634]",
           w == [0.0, 0.277533] and AN.wilson(5, 10) == [0.236593, 0.763407], f"{w} {AN.wilson(5, 10)}")

    # 4. la cola (A-D11)
    e0 = {"cap": [{"id": "cap::1.1", "unidad": "1.1"}, {"id": "cap::2.1", "unidad": "2.1"}, {"id": "cap::2.2", "unidad": "2.2"},
                  {"id": "cap::4.2.1.2", "unidad": "4.2.1.2"}], "cla": [], "ext": [], "pro": [], "ric": []}
    prueba("resolución de anclas: exacta, por descendientes y ninguna",
           AN.resolver("cap:1.1", e0) == (["cap::1.1"], "a") and AN.resolver("cap:2", e0) == (["cap::2.1", "cap::2.2"], "b")
           and AN.resolver("cap:9", e0) == ([], "ninguna") and AN.resolver("xyz:1", e0) == ([], "ninguna"))
    pq = {"P1": {"anclas": ["cap:1.1"]}, "P2": {"anclas": ["cap:2"]}, "P3": {"anclas": ["cap:4.2.1.2"]}, "P4": {"anclas": ["cap:9", "cap:1.1"]}}
    pc = AN.preguntas_con_cola(pq, {"cap::2.2", "cap::4.2.1.2::parte1"}, e0)["por_pregunta"]
    prueba("cola: sale una pregunta si alguna de sus anclas cae en la cola; una parte cuenta como su unidad",
           pc == {"P1": False, "P2": True, "P3": True, "P4": False})

    # 5. el análisis sobre veredictos sintéticos con resultado conocido
    qs = [f"Q{i:02d}" for i in range(12)]
    vn1 = {}
    for i, q in enumerate(qs):
        vn1[(q, "kg", 1)] = a(q, "kg", 1, "correcto")
        vn1[(q, "fragmentos_bm25", 1)] = a(q, "fragmentos_bm25", 1, "incorrecto" if i < 10 else "correcto")
        vn1[(q, "fragmentos_denso", 1)] = a(q, "fragmentos_denso", 1, "incorrecto" if i < 2 else "correcto")
    f = AN.finales(qs, vn1, {"pares": []}, {})
    c = AN.comparar(f, qs)
    prueba("análisis: el grafo supera a BM25 (10 a 0, p = 0,00195) y no al denso (2 a 0): sin afirmación general",
           c["comparaciones"]["fragmentos_bm25"]["grafo_supera"] and not c["comparaciones"]["fragmentos_denso"]["grafo_supera"]
           and not c["afirmacion_general_el_grafo_supera_a_los_fragmentos"]
           and c["comparaciones"]["fragmentos_bm25"]["tasa_discordantes"] == round(10 / 12, 6))
    vn1b = {k: dict(v, veredicto_pregunta="incorrecto") if k[1] != "kg" and int(k[0][1:]) < 10 else v for k, v in vn1.items()}
    c2 = AN.comparar(AN.finales(qs, vn1b, {"pares": []}, {}), qs)
    prueba("análisis: con los dos en 10 a 0, el grafo supera a las dos y vale la afirmación general",
           c2["afirmacion_general_el_grafo_supera_a_los_fragmentos"])
    vn1c = dict(vn1)
    vn1c[("Q00", "kg", 1)] = a("Q00", "kg", 1, "requiere_adjudicacion", idop="ID-ADJ")
    del vn1c[("Q01", "kg", 1)]
    fc = AN.finales(qs, vn1c, {"pares": []}, {})
    cc, cs = AN.comparar(fc, qs), AN.comparar(fc, qs, sensibilidad=True)
    prueba("análisis: lo sin veredicto final sale (n = 10) y la sensibilidad lo cuenta como 0 (n = 12)",
           cc["comparaciones"]["fragmentos_bm25"]["n_preguntas"] == 10 and cs["comparaciones"]["fragmentos_bm25"]["n_preguntas"] == 12
           and cs["comparaciones"]["fragmentos_bm25"]["n10_grafo_si_fragmentos_no"] == 8)
    fa = AN.finales(qs, AN.aplicar_adjudicaciones(vn1c, {"ID-ADJ": "correcto"}), {"pares": []}, {})
    prueba("análisis: una adjudicación de la autora reemplaza a la requiere_adjudicacion", fa[("Q00", "kg")]["final"] == "correcto")
    pob1 = {"pares": [{"qid": "Q11", "brazo": "fragmentos_bm25", "tipo": "auditoria_correcto"}]}
    vrc1 = {("Q11", "fragmentos_bm25", r): a("Q11", "fragmentos_bm25", r, v) for r, v in zip(K.REPS_RECORRIDA, ["incorrecto", "incorrecto", "correcto"])}
    fr = AN.finales(qs, vn1, pob1, vrc1)
    prueba("análisis: un par de la población toma el agregado de sus re-corridas, no el de N = 1",
           fr[("Q11", "fragmentos_bm25")] == {"final": "incorrecto", "origen": "re-corridas"})
    pr = AN.predicciones(vn1, f, {b: {"latencia_media_s_n1": {"kg": 30.0}.get(b, 10.0), "c_agente_media_n1": {"kg": 0.1}.get(b, 0.03)}
                                  for b in K.BRAZOS})
    prueba("predicciones: el sentido observado de incorrectos, latencia y costo",
           pr["predicciones"]["2_incorrectos"]["coincide"] is False and pr["predicciones"]["4_latencia"]["coincide"] is True
           and pr["predicciones"]["5_costo_c_agente"]["coincide"] is True and pr["predicciones"]["6_asimetria"]["coincide"] is None)
    ms = [{"brazo": "kg", "hb2": {"n_llamadas_log_r1": n, "subtype": s}} for n, s in ((5, "success"), (30, "success"),
                                                                                       (31, "success"), (12, "error_max_turns"))]
    r5 = AN.r5_por_brazo(ms)["kg"]
    prueba("R5 operativo: al tope (≥ 30) 2, pasan de 30 1, cortadas 1, de 4", (r5["al_tope_30_o_mas"], r5["pasan_de_30"],
                                                                              r5["cortadas"], r5["n_sesiones"]) == (2, 1, 1, 4))

    # 6. el juez: casos, ceguera, agregación, costo inicial
    preg = {"Q01": {"pregunta": "¿pregunta sintética uno?", "criterios": [{"criterio": "c1", "cita_textual": "t1"},
                                                                          {"criterio": "c2", "cita_textual": "t2"}]},
            "Q02": {"pregunta": "¿pregunta sintética dos?", "criterios": [{"criterio": "c1", "cita_textual": "t1"}]}}
    rs = [{"qid": q, "brazo": b, "rep": 1, "id_sesion": f"N1-{q}-{b}", "respuesta": f"respuesta {q} {b} según los fragmentos",
           "respondible_flag": True} for q in preg for b in K.BRAZOS]
    c1, c2_ = JA.armar_casos(rs, preg), JA.armar_casos(list(reversed(rs)), preg)
    prueba("juez: el orden ciego es determinista, con ids opacos únicos", [x["id_opaco"] for x in c1] == [x["id_opaco"] for x in c2_]
           and len({x["id_opaco"] for x in c1}) == 6)
    ciegos = JA.vista_ciega(c1)
    prueba("juez: la ceguera da 0 fugas en la vista ciega y frena con un campo de más",
           JA.verificar_ceguera(ciegos) == [] and JA.verificar_ceguera([dict(ciegos[0], brazo="kg")]) != [])
    prueba("juez: las marcas de brazo en las respuestas se cuentan, sin editarlas",
           JA.marcas_por_brazo(c1)["kg"]["por_marca"]["fragmento"] == 2)
    with tempfile.TemporaryDirectory() as td:
        od = Path(td) / "n1"
        od.mkdir()
        meta = {"input_tokens": 1000, "output_tokens": 200, "modelo": "claude-sonnet-4-6", "stop_reason": "end_turn",
                "prompt_sha256": JA.PROMPT_SHA256, "code_ver": "x"}
        x0, x1 = ciegos[0], ciegos[1]
        for rep, vs in zip(K.REPS_JUEZ, (["cumplido", "dudoso"], ["cumplido", "no_cumplido"], ["cumplido", "no_cumplido"])):
            vv = vs[:len(x0["criterios"])]
            with (od / f"veredictos_r{rep}.jsonl").open("a", encoding="utf-8") as fh:
                fh.write(json.dumps({"id_opaco": x0["id_opaco"], "rep": rep, "clasificacion_respuesta": "contenido",
                                     "criterios": [{"indice": i + 1, "veredicto": v, "fragmento": None, "justificacion": ""}
                                                   for i, v in enumerate(vv)], "meta": meta}) + "\n")
        g = JA.agregar(od, [x0, x1])
        esperado = "parcial" if len(x0["criterios"]) == 2 else "correcto"
        prueba("juez: modal por criterio y mapping de EV2; una respuesta sin sus tres repeticiones queda incompleta",
               g["n_agregados"] == 1 and g["agregados"][0]["veredicto_pregunta"] == esperado and len(g["incompletas"]) == 1)
        prueba("juez: el costo de la primera respuesta, 0,0378; después, el mayor de las juzgadas",
               JA.costo_mayor_juzgada(Path(td) / "otro") == 0.0378 and abs(JA.costo_mayor_juzgada(Path(td)) - 3 * 0.006) < 1e-12)

    # 7. el enmascarado, sobre una copia sintética (una carpeta personal de prueba)
    casa = "/home/usuario_de_prueba"
    with tempfile.TemporaryDirectory() as td:
        raiz = Path(td) / "raiz"
        n1 = raiz / "data/experiment/banco_mcp/a2_2/resultados/n1"
        n1.mkdir(parents=True)
        cwd = casa + "/INGENIERIA IA/TESIS/fuera_del_repo/banco_sesiones/cwd"
        (n1 / "stream_N1-Q01-kg.jsonl").write_text(json.dumps({"type": "system", "subtype": "init", "cwd": cwd}) + "\n"
                                                    + json.dumps({"type": "result", "x": casa + "/otra"}) + "\n", encoding="utf-8")
        (n1 / "sesion_N1-Q01-kg.jsonl").write_text(json.dumps({"cwd": cwd}) + "\n", encoding="utf-8")
        js, orig = Path(td) / "enm.json", Path(td) / "originales"
        sc = AQUI / "enmascarar_cwd_a2_2.py"
        r1 = subprocess.run([sys.executable, "-B", str(sc), "--calcular", str(raiz), str(js)], capture_output=True, text=True)
        r2 = subprocess.run([sys.executable, "-B", str(sc), "--probar", str(raiz), str(js)], capture_output=True, text=True)
        r3 = subprocess.run([sys.executable, "-B", str(sc), "--aplicar", str(raiz), str(js), "--originales", str(orig)],
                            capture_output=True, text=True)
        texto = (n1 / "stream_N1-Q01-kg.jsonl").read_text(encoding="utf-8")
        oc = orig / "data/experiment/banco_mcp/a2_2/resultados/n1/stream_N1-Q01-kg.jsonl"
        prueba("enmascarado: calcular, probar y aplicar; la carpeta personal pasa a $HOME y el original queda afuera",
               r1.returncode == 0 and r2.returncode == 0 and r3.returncode == 0 and "usuario_de_prueba" not in texto
               and "$HOME/INGENIERIA IA" in texto and oc.exists() and "usuario_de_prueba" in oc.read_text(encoding="utf-8"),
               r1.stdout.strip() + " | " + r3.stdout.strip())
        r4 = subprocess.run([sys.executable, "-B", str(sc), "--probar", str(raiz), str(js)], capture_output=True, text=True)
        prueba("enmascarado: después de aplicar, probar frena (los archivos ya no son los originales)", r4.returncode != 0)

    # 8. el control de EV2 sobre un archivo sintético con el esquema
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "preguntas.json"
        p.write_text(json.dumps({"preguntas": [
            {"id": "S1", "pregunta": "¿s1?", "to": "cap", "gold": {"criterios": [{"criterio": "c", "cita_textual": "t"}], "ancla": ["cap:1.1"]}},
            {"id": "S2", "pregunta": "¿s2?", "to": "cap", "gold": {"criterios": [{"criterio": "c", "cita_textual": "t"}], "ancla": ["cap:4.2.1.2"]}},
            {"id": "S3", "pregunta": "¿s3?", "to": "cap", "gold": {"criterios": [{"criterio": "c", "cita_textual": "t"}], "ancla": ["cap:99.9"]}}]}),
            encoding="utf-8")
        r = CE.controlar(p, K.sha256_file(p), real=False)
        prueba("control de EV2: cuenta preguntas, criterios, anclas fuera de la E0 y preguntas en la cola",
               (r["n_preguntas"], r["n_criterios"], r["anclas"]["no_estan_en_la_E0_instancias"], r["preguntas_con_alguna_ancla_en_la_cola"])
               == (3, 3, 1, 1), json.dumps(r["anclas"]["por_via_instancias"]))
        try:
            K.cargar_preguntas(p, K.sha256_file(p), real=True)
            prueba("EV2: la corrida real no acepta otro archivo", False)
        except K.FrenoA22:
            prueba("EV2: la corrida real no acepta otro archivo", True)

    print(f"selftest A2.2: {sum(RES)} de {len(RES)} en PASS")
    return 0 if all(RES) else 1


if __name__ == "__main__":
    raise SystemExit(main())
