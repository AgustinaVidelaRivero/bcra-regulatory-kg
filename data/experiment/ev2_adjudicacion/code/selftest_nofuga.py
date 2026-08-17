"""
selftest_nofuga.py — Selftest OFFLINE del worksheet ciego de adjudicación:
(1) 0 marcadores prohibidos en worksheet_adjudicacion.{json,md} (grafo, label,
rep, veredictos/fragmentos del juez, ids EV2R-/EV2E-/EV2F- y sus sufijos hex);
(2) estructura de cada ficha (solo claves permitidas; marcas en blanco);
(3) integridad: respuesta (sha256), pregunta, TO/ancla y criterios de cada
ficha coinciden con la tabla SOLO_MESA y el gold sellado;
(4) orden y numeración reproducibles con la semilla; ids de ficha únicos;
(5) población y muestra re-derivadas desde los insumos coinciden con la tabla
SOLO_MESA y con los esperados.

Uso: .venv/bin/python -B data/experiment/ev2_adjudicacion/code/selftest_nofuga.py
Escribe selftest_out/selftest_nofuga.txt (gitignorado) además de stdout.
"""

from __future__ import annotations

import json
import random
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun_adj as ca  # noqa: E402

CLAVES_FICHA = {"n", "id_ficha", "to", "to_nombre", "ancla", "pregunta", "respuesta", "criterios", "observaciones"}
CLAVES_CRIT = {"indice", "criterio", "cita_textual", "veredicto"}
CLAVES_WS = {"worksheet", "semilla_orden", "n_fichas", "marcas_validas", "instrucciones", "fichas"}

LINEAS, FALLOS, N = [], [], 0


def check(nombre, cond, detalle=""):
    global N
    N += 1
    ln = f"  {'ok ' if cond else 'FALLO'} {nombre}" + (f" — {detalle}" if detalle and not cond else "")
    print(ln)
    LINEAS.append(ln)
    if not cond:
        FALLOS.append(nombre)


def main():
    txt_json = ca.WORKSHEET_JSON.read_text(encoding="utf-8")
    txt_md = ca.WORKSHEET_MD.read_text(encoding="utf-8")
    ws = json.loads(txt_json)
    tabla = json.loads(ca.TABLA_FICHAS.read_text(encoding="utf-8"))
    ins = ca.cargar_insumos()
    gold = ins["gold"]

    print("== (1) marcadores prohibidos")
    for nombre, txt in (("json", txt_json), ("md", txt_md)):
        m = ca.buscar_marcadores(txt)
        check(f"0 marcadores en worksheet.{nombre}", not m, str(m))
    # sufijos hex de TODOS los ids opacos de base y encadenamiento, y los ids de pregunta
    sufijos = [i.split("-", 1)[1] for i in list(ins["base_tab"]) + list(ins["enc_tab"])]
    for nombre, txt in (("json", txt_json), ("md", txt_md)):
        hits = [s for s in sufijos if s in txt]
        check(f"0 sufijos de id opaco en worksheet.{nombre} ({len(sufijos)} buscados)", not hits, str(hits[:5]))
        hits_q = [q for q in gold if q in txt]
        check(f"0 ids de pregunta en worksheet.{nombre}", not hits_q, str(hits_q[:5]))
    for pal in ("v2", "v3", "run_3", "juez", "correcto", "parcial", "incorrecto", "dudoso"):
        # palabras que podrían aparecer legítimamente en una respuesta: se listan como dato, no como fallo
        n = len(re.findall(rf"(?<![A-Za-z0-9_]){re.escape(pal)}(?![A-Za-z0-9_])", txt_json))
        LINEAS.append(f"  info: '{pal}' como palabra aparece {n} veces en el json (texto de respuestas/instrucciones)")
        print(LINEAS[-1])

    print("== (2) estructura")
    check("claves de nivel superior", set(ws) == CLAVES_WS, str(set(ws) ^ CLAVES_WS))
    check("n_fichas coincide", ws["n_fichas"] == len(ws["fichas"]) == tabla["n_fichas"])
    check("marcas válidas = cumplido/no_cumplido", ws["marcas_validas"] == ["cumplido", "no_cumplido"])
    ok_claves = all(set(f) == CLAVES_FICHA for f in ws["fichas"])
    check("cada ficha tiene exactamente las claves permitidas", ok_claves)
    ok_crit = all(set(c) == CLAVES_CRIT for f in ws["fichas"] for c in f["criterios"])
    check("cada criterio tiene exactamente las claves permitidas", ok_crit)
    check("todas las marcas en blanco (None)", all(c["veredicto"] is None for f in ws["fichas"] for c in f["criterios"]))
    check("observaciones en blanco", all(f["observaciones"] is None for f in ws["fichas"]))
    check("numeración 1..n", [f["n"] for f in ws["fichas"]] == list(range(1, len(ws["fichas"]) + 1)))
    ids = [f["id_ficha"] for f in ws["fichas"]]
    check("ids de ficha únicos y con prefijo", len(set(ids)) == len(ids) and all(i.startswith(ca.PREFIJO_FICHA) for i in ids))
    check("md contiene cada ficha una vez", all(txt_md.count(f"`{i}`") == 1 for i in ids))

    print("== (3) integridad contra tabla SOLO_MESA y gold")
    tab = {f["id_ficha"]: f for f in tabla["fichas"]}
    check("mismos ids en tabla y worksheet", set(tab) == set(ids))
    ok_sha = ok_preg = ok_crit_gold = ok_id = ok_to = True
    for f in ws["fichas"]:
        t = tab[f["id_ficha"]]
        g = gold[t["id_pregunta"]]
        ok_sha &= ca.sha256_texto(f["respuesta"]) == t["sha256_respuesta"]
        ok_preg &= f["pregunta"] == g["pregunta"]
        ok_to &= f["to"] == g["to"] and f["to_nombre"] == g["to_nombre"] and f["ancla"] == g["ancla"]
        ok_crit_gold &= [(c["indice"], c["criterio"], c["cita_textual"]) for c in f["criterios"]] == \
            [(j, c["criterio"], c["cita_textual"]) for j, c in enumerate(g["criterios"], start=1)]
        ok_id &= f["id_ficha"] == ca.id_ficha(t["id_pregunta"], t["sha256_respuesta"])
        ok_id &= t["n"] == f["n"]
    check("sha256 de cada respuesta = tabla", ok_sha)
    check("pregunta = gold", ok_preg)
    check("TO/ancla = gold", ok_to)
    check("criterios y citas = gold (orden y texto)", ok_crit_gold)
    check("id_ficha y n reproducibles", ok_id)
    # la respuesta de la ficha es la que está en la traza de origen
    ok_traza = True
    for t in tabla["fichas"]:
        for r in t["respuestas"]:
            txt = (ca.respuesta_base(ins, r["id_opaco_respuesta"]) if r["origen_respuesta"] == "base"
                   else ca.respuesta_enc(ins, r["id_opaco_respuesta"]))
            ok_traza &= ca.sha256_texto(txt) == t["sha256_respuesta"]
    check("cada respuesta cubierta se lee de su traza con el mismo sha256", ok_traza)

    print("== (4) orden reproducible")
    claves = sorted((t["id_pregunta"], t["sha256_respuesta"]) for t in tabla["fichas"])
    random.Random(ca.SEMILLA_WORKSHEET).shuffle(claves)
    esperado = [ca.id_ficha(q, s) for q, s in claves]
    check(f"orden = shuffle('{ca.SEMILLA_WORKSHEET}') sobre (id_pregunta, sha256) ordenados", esperado == ids)

    print("== (5) población y muestra re-derivadas")
    res = ca.construir_fichas(ins)
    check("re-derivación reproduce la tabla SOLO_MESA (fichas)", res["fichas_mesa"] == tabla["fichas"])
    check("re-derivación reproduce el worksheet", ca.worksheet_json(res["worksheet"]) == ws)
    check("tabla final por grafo = esperada", res["tabla_final"] == ca.ESPERADO_FINAL_POR_GRAFO, str(res["tabla_final"]))
    her, pen = res["pobA"]["heredados"], res["pobA"]["pendientes_s7"]
    check("21 heredados", len(her) == 21, str(len(her)))
    check("9 pendientes §7", len(pen) == 9, str(len(pen)))
    check("heredados por grafo 7/8/6", Counter(x["grafo"] for x in her) == Counter({"v2": 7, "v3": 8, "run_3": 6}))
    check("pendientes por grafo 3/4/2", Counter(x["grafo"] for x in pen) == Counter({"v2": 3, "v3": 4, "run_3": 2}))
    votos_adj = sum(len(x["objetivos"]) for x in pen)
    check("votos ADJ en los 9 pendientes = 17 (mandato esperaba 24: 24 = 17 + 7 en pares invariantes)", votos_adj == 17, str(votos_adj))
    total_adj = sum(1 for x in res["fin"] if x["re_corrido"] for v in x["veredictos_reps"] if v == ca.ADJ)
    check("votos ADJ en las 198 respuestas §7 = 24", total_adj == 24, str(total_adj))
    por_origen = Counter(f["origen"] for f in tabla["fichas"])
    check("fichas por origen 21/15/3/9", por_origen == Counter({"heredado_base": 21, "s7_pendiente": 15,
                                                                 "muestra_correcto": 3, "muestra_parcial_incorrecto": 9}),
          str(por_origen))
    check("48 fichas", len(ids) == 48)
    check("muestra correcto 1/1/1", {g: d["k_correcto"] for g, d in res["muestra"]["detalle_estratos"].items()} == {"v2": 1, "v3": 1, "run_3": 1})
    check("muestra parcial+incorrecto 3/3/3", {g: d["k_parcial_incorrecto"] for g, d in res["muestra"]["detalle_estratos"].items()} == {"v2": 3, "v3": 3, "run_3": 3})
    # cada ficha con más de una respuesta: mismo par, textos idénticos, todas ADJ
    multi = [t for t in tabla["fichas"] if len(t["respuestas"]) > 1]
    check("fichas con varias respuestas = 2 (textos idénticos dentro de un par, todas req.adj.)",
          len(multi) == 2 and all(t["origen"] == "s7_pendiente" and
                                  all(r["veredicto_juez_respuesta"] == ca.ADJ for r in t["respuestas"]) for t in multi))
    # cada respuesta de muestra coincide con el final del par y es la de menor rep
    ok_m = True
    for t in tabla["fichas"]:
        if not t["origen"].startswith("muestra_"):
            continue
        r = t["respuestas"][0]
        ok_m &= r["veredicto_juez_respuesta"] == t["final_juez_par"]
        if t["veredictos_reps"]:
            ok_m &= r["rep"] == 1 + t["veredictos_reps"].index(t["final_juez_par"])
        else:
            ok_m &= r["rep"] is None
    check("muestra: respuesta de la ficha = final del par (menor rep si re-corrido; base si no)", ok_m)
    # ninguna ficha de la muestra ni heredada comparte par con otra ficha
    pares_por_origen = Counter((t["id_opaco_base"], t["origen"]) for t in tabla["fichas"])
    check("heredados y muestra: una ficha por par", all(n == 1 for (p, o), n in pares_por_origen.items() if o != "s7_pendiente"))

    resumen = f"\n{N - len(FALLOS)}/{N} checks ok; fallos: {FALLOS}"
    print(resumen)
    out = ca.UNIDAD_DIR / "selftest_out"
    out.mkdir(exist_ok=True)
    (out / "selftest_nofuga.txt").write_text("\n".join(LINEAS) + resumen + "\n", encoding="utf-8")
    sys.exit(1 if FALLOS else 0)


if __name__ == "__main__":
    main()
