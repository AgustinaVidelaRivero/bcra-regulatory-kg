"""
selftest_nofuga_tanda0.py — Selftest NO-FUGA de las planillas ciegas de
adjudicación de C2 a C5 (anexo E5.c de U-TANDA0-2A, E5.c.1 d), OBLIGATORIO
antes de entregar. USD 0, sin API, sin escrituras. Molde:
ev2_r1/code/selftest_nofuga_r1.py (774acac) y
ev2_adjudicacion/code/selftest_nofuga.py (03ebe83).

Sobre los archivos PUBLICABLES (planilla_mezclada y planilla_c5 en .json y
.md, sus CSV de marcas y censo_planillas_ciego.md), como texto plano:
  1. Marcadores inequívocos en TODO el texto, incluidos los textos que se
     muestran tal cual (pregunta, respuesta, criterio, cita): ids de pregunta
     (EV2F-, T0F-) y los propios ids, prefijos de ids opacos de las cuatro
     celdas y sus sufijos buscados SIN prefijo, sha256 de respuestas (completos
     o sus primeros 12 hex), sha de los grafos (completos o sus primeros 8 hex),
     labels de corrida, KG- y KG_.
  2. El resto de la lista del anexo (decisión 3 c) en todo lo demás: celda,
     grafo, backend, label, rep, veredictos y modales del juez, fragmentos,
     origen, población, ids opacos, sha, nombres de grafo o de backend (r1,
     desarrollo, diez, Neo4j, memoria, GraphIndex, fulltext) y rutas. Las
     apariciones de esas palabras DENTRO de los textos mostrados se cuentan y
     se reportan por planilla; no fallan.
  3. Estructura: claves ciegas exactas por ficha y por criterio, ids FT0-
     únicos, numeración 1..N, .md y .csv iguales a su render desde el .json,
     CSV con una fila por criterio y marcas vacías, censo ciego solo con
     fichas y criterios por planilla.
  4. Consistencia contra adjudicacion_SOLO_MESA/ y el gold: respuesta = sha de
     la tabla y de su traza; pregunta, TO, ancla y criterios = gold de su
     pregunta; reemplazo de cita solo en los criterios sin cita autorizados;
     id de ficha y orden reproducibles.
  5. planilla_mezclada: ningún campo permite separar sus fichas por celda
     (mismas claves, sal única por planilla, un solo sorteo de orden sobre la
     unión, campos no textuales iguales para la misma pregunta).
  6. Re-derivación: planillas_tanda0.construir() reproduce byte a byte los
     publicables y los SOLO_MESA (doble corrida), con los totales del anexo.
  7. PROVOCACIÓN: inyectar marcadores y sufijos en copias debe disparar la
     detección; una palabra común dentro de una respuesta se cuenta y no falla.

La salida no publica censos por celda ni por origen ni pertenencias.

Uso:  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/ev2_tanda0/code/selftest_nofuga_tanda0.py
"""

from __future__ import annotations

import copy
import csv
import io
import json
import random
import re
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import planillas_tanda0 as pt              # noqa: E402
ce0 = pt.ce0

_checks: list[tuple[str, bool]] = []


def check(nombre: str, cond) -> None:
    _checks.append((nombre, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {nombre}")


CLAVES_TOP = {"planilla", "n_fichas", "n_criterios", "marcas_validas", "csv_de_marcas",
              "instrucciones", "fichas"}
CLAVES_FICHA = {"n", "id_ficha", "to", "to_nombre", "ancla", "pregunta", "respuesta",
                "criterios", "observaciones"}
CLAVES_CRITERIO = {"indice", "criterio", "cita_textual"}
CAMPOS_MOSTRADOS = ("pregunta", "respuesta")
CAMPOS_MOSTRADOS_CRITERIO = ("criterio", "cita_textual")

# Regla 1: inequívocos (se buscan también dentro de los textos mostrados)
MARCADORES_INEQUIVOCOS = (
    ["EV2F-", "T0F-", "EV2R-", "EV2E-", "EV2R1-", "EV2E1-", "T0C", "KG-", "KG_",
     "ev2_r1_base", "ev2_r1_enc", "ev2_r1_eval", "ev2_base_", "ev2_enc_", "ev2_tanda0",
     "_enc_r1", "_enc_r2", "_enc_r3", "_juez_r", "_enc_juez"]
    + [ce0.CELDAS[c].label for c in pt.CELDAS_ADJ]
    + [p for c in pt.CELDAS_ADJ for p in (ce0.CELDAS[c].prefijo_base, ce0.CELDAS[c].prefijo_enc)])

# Regla 2: resto de la lista (fuera de los textos mostrados)
MARCADORES_RESTO_RE = [
    r"\bC[2-5]\b", r"\bc[2-5]\b", r"(?i)celda", r"(?i)grafo", r"(?i)backend", r"(?i)label",
    r"\brep\b", r"(?i)modal", r"(?i)fragmento", r"(?i)origen", r"(?i)heredad", r"(?i)s7_",
    r"(?i)muestra_", r"(?i)poblaci", r"(?i)requiere_adjudicacion", r"(?i)dudoso", r"(?i)sin_consenso",
    r"(?i)correcto", r"(?i)parcial", r"(?i)juez", r"(?i)id_opaco", r"(?i)sha256", r"(?i)solo_mesa",
    r"(?i)r1", r"(?i)desarrollo", r"(?i)diez", r"(?i)neo4j", r"(?i)memoria", r"(?i)graphindex",
    r"(?i)fulltext", r"(?i)auditoria", r"(?i)disparad", r"(?i)kg_path", r"(?i)fingerprint",
    r"data/", r"experiment/", r"/Users", r"\.py\b", r"\.jsonl?\b", r'"final', r'"veredicto_juez',
    r'"id_pregunta"', r"veredictos_reps", r"ids_reps"]
PALABRAS_COMUNES = ["r1", "desarrollo", "diez", "memoria", "neo4j", "fulltext", "graphindex",
                    "celda", "grafo", "juez", "correcto", "parcial", "incorrecto"]


def fugas_inequivocas(texto: str, u: dict) -> list[str]:
    out = [f"marcador:{m}" for m in MARCADORES_INEQUIVOCOS if m in texto]
    out += ["sufijo_opaco" for s in u["sufijos"] if s in texto]
    out += ["id_pregunta" for q in u["qids"] if q in texto]
    out += ["sha_respuesta" for s in u["shas_resp"] if s in texto or s[:12] in texto]
    out += ["sha_grafo" for s in u["shas_grafo"] if s in texto or s[:8] in texto]
    return out


def fugas_resto(texto: str) -> list[str]:
    return [f"resto:{rx}" for rx in MARCADORES_RESTO_RE if re.search(rx, texto)]


def blanquear(pj: dict) -> dict:
    """Copia del .json con los textos mostrados tal cual vaciados (regla 2)."""
    b = copy.deepcopy(pj)
    for f in b["fichas"]:
        for k in CAMPOS_MOSTRADOS:
            f[k] = ""
        for c in f["criterios"]:
            for k in CAMPOS_MOSTRADOS_CRITERIO:
                c[k] = ""
    return b


def textos_mostrados(pj: dict) -> str:
    return "\n".join([f[k] for f in pj["fichas"] for k in CAMPOS_MOSTRADOS]
                     + [c[k] for f in pj["fichas"] for c in f["criterios"]
                        for k in CAMPOS_MOSTRADOS_CRITERIO])


def universo() -> dict:
    sufijos, shas = [], set()
    for c in pt.CELDAS_ADJ:
        p = pt.rutas_insumos(ce0.CELDAS[c])
        for k in ("base_tab", "enc_tab"):
            for f in pt._leer_json(p[k])["filas"]:
                sufijos.append(f["id_opaco"].split("-", 1)[1])
                shas.add(f["sha256_respuesta"])
    qids = [f"EV2F-{i:03d}" for i in range(1, 41)] + [p["id"] for p in ce0.cargar_preguntas_c5()]
    shas_grafo = sorted({ce0.CELDAS[c].kg_sha256 for c in pt.CELDAS_ADJ})
    return {"sufijos": sufijos, "qids": qids, "shas_resp": sorted(shas), "shas_grafo": shas_grafo}


def main() -> int:
    print("== SELFTEST NO-FUGA de las planillas de adjudicación de C2 a C5 (E5.c.1, USD 0) ==")
    u = universo()
    check(f"universo de control: {len(u['sufijos'])} sufijos opacos únicos de las cuatro celdas, "
          f"{len(u['qids'])} ids de pregunta, {len(u['shas_resp'])} sha de respuestas, "
          f"{len(u['shas_grafo'])} sha de grafos",
          len(u["sufijos"]) == len(set(u["sufijos"])) == 359 and len(u["qids"]) == 60
          and len(u["shas_grafo"]) == 3)

    tabla = pt._leer_json(pt.TABLA_FICHAS_SM)
    pert = pt._leer_json(pt.PERTENENCIA_SM)
    mesa = {f["id_ficha"]: f for f in tabla["fichas"]}
    golds = {c: pt.cargar_gold_fichas(ce0.CELDAS[c]) for c in pt.CELDAS_ADJ}

    textos = {}
    pjs = {}
    for nom in pt.PLANILLAS:
        pjs[nom] = pt._leer_json(pt.planilla_json_path(nom))
        textos[pt.planilla_json_path(nom).name] = pt.planilla_json_path(nom).read_text(encoding="utf-8")
        textos[pt.planilla_md_path(nom).name] = pt.planilla_md_path(nom).read_text(encoding="utf-8")
        textos[pt.marcas_csv_path(nom).name] = pt.marcas_csv_path(nom).read_text(encoding="utf-8")
    textos[pt.CENSO_CIEGO.name] = pt.CENSO_CIEGO.read_text(encoding="utf-8")

    print("-- (1) marcadores inequívocos en todo el texto de cada publicable")
    for nombre, texto in textos.items():
        f = fugas_inequivocas(texto, u)
        check(f"{nombre}: 0 inequívocos (ids, sufijos, sha de respuestas y grafos, labels, KG-/KG_)", not f)
        if f:
            print(f"      -> {sorted(set(f))[:6]}")

    print("-- (2) resto de la lista fuera de los textos mostrados; palabras comunes dentro, contadas")
    for nom, pj in pjs.items():
        b = blanquear(pj)
        f = fugas_resto(json.dumps(b, ensure_ascii=False, indent=2))
        check(f"{nom}.json sin textos mostrados: 0 marcadores del resto", not f)
        if f:
            print(f"      -> {f[:6]}")
        f = fugas_resto(pt.render_md(b))
        check(f"{nom}.md sin textos mostrados: 0 marcadores del resto", not f)
        if f:
            print(f"      -> {f[:6]}")
        mostrado = textos_mostrados(pj)
        cuenta = {w: len(re.findall(re.escape(w), mostrado, re.I)) for w in PALABRAS_COMUNES}
        print(f"  info {nom}: palabras comunes dentro de los textos mostrados: "
              f"{ {k: v for k, v in cuenta.items() if v} or 'ninguna'}")
    for nom in pt.PLANILLAS:
        f = fugas_resto(textos[pt.marcas_csv_path(nom).name])
        check(f"{nom}_marcas.csv: 0 marcadores del resto", not f)
    f = fugas_resto(textos[pt.CENSO_CIEGO.name])
    check("censo_planillas_ciego.md: 0 marcadores del resto", not f)

    print("-- (3) estructura")
    ids_todos = []
    for nom, pj in pjs.items():
        fichas = pj["fichas"]
        ids = [x["id_ficha"] for x in fichas]
        ids_todos += ids
        check(f"{nom}: claves de nivel superior exactas", set(pj) == CLAVES_TOP)
        check(f"{nom}: fichas con claves ciegas exactas y observaciones en blanco",
              all(set(x) == CLAVES_FICHA and x["observaciones"] is None for x in fichas))
        check(f"{nom}: criterios con claves ciegas exactas e índices 1..K",
              all(set(c) == CLAVES_CRITERIO for x in fichas for c in x["criterios"])
              and all([c["indice"] for c in x["criterios"]] == list(range(1, len(x["criterios"]) + 1))
                      for x in fichas))
        check(f"{nom}: n_fichas y n_criterios coinciden; numeración 1..N",
              pj["n_fichas"] == len(fichas)
              and pj["n_criterios"] == sum(len(x["criterios"]) for x in fichas)
              and [x["n"] for x in fichas] == list(range(1, len(fichas) + 1)))
        check(f"{nom}: ids FT0- con 8 hex y únicos",
              all(re.fullmatch(r"FT0-[0-9a-f]{8}", i) for i in ids) and len(set(ids)) == len(ids))
        check(f"{nom}: marcas válidas y nombre del CSV",
              pj["marcas_validas"] == ["cumplido", "no_cumplido"]
              and pj["csv_de_marcas"] == f"{nom}_marcas.csv")
        check(f"{nom}.md = render desde el .json", textos[pt.planilla_md_path(nom).name] == pt.render_md(pj))
        csv_txt = textos[pt.marcas_csv_path(nom).name]
        filas = list(csv.reader(io.StringIO(csv_txt)))
        check(f"{nom}_marcas.csv = render; encabezado {pt.COLUMNAS_CSV}; una fila por criterio, "
              "veredicto y observacion vacíos",
              csv_txt == pt.render_csv(pj) and filas[0] == pt.COLUMNAS_CSV
              and filas[1:] == [[x["id_ficha"], str(c["indice"]), "", ""]
                                for x in fichas for c in x["criterios"]])
    check("ids de ficha únicos entre las dos planillas", len(set(ids_todos)) == len(ids_todos))
    censo = textos[pt.CENSO_CIEGO.name].splitlines()
    filas_censo = [ln for ln in censo if ln.startswith("| planilla_")]
    check("censo ciego: solo fichas y criterios por planilla (dos filas, tres columnas)",
          censo[0].startswith("# ") and len(filas_censo) == 2
          and all(len(ln.strip("|").split("|")) == 3 for ln in filas_censo)
          and textos[pt.CENSO_CIEGO.name] == pt.render_censo_ciego(
              {n: {"fichas": pjs[n]["fichas"]} for n in pt.PLANILLAS}))

    print("-- (4) consistencia contra la tabla SOLO_MESA, las trazas y el gold")
    check("tabla SOLO_MESA y pertenencia cubren exactamente las fichas publicadas",
          set(mesa) == set(ids_todos)
          and {(x["id_ficha"], x["celda"], x["planilla"], x["n"]) for x in pert["fichas"]}
          == {(m["id_ficha"], m["celda"], m["planilla"], m["n"]) for m in mesa.values()})
    ok_pl = ok_sha = ok_gold = ok_id = ok_cita = ok_n = True
    for nom, pj in pjs.items():
        sal = pt.PLANILLAS[nom]["sal_id_ficha"]
        celdas_ok = set(pt.PLANILLAS[nom]["celdas"])
        for x in pj["fichas"]:
            m = mesa[x["id_ficha"]]
            ok_pl &= m["planilla"] == nom and m["celda"] in celdas_ok
            ok_n &= m["n"] == x["n"] and m["n_criterios"] == len(x["criterios"])
            ok_sha &= pt.sha256_texto(x["respuesta"]) == m["sha256_respuesta"]
            g = golds[m["celda"]][m["id_pregunta"]]
            ok_gold &= (x["pregunta"] == g["pregunta"] and x["to"] == g["to"]
                        and x["to_nombre"] == g["to_nombre"] and x["ancla"] == g["ancla"]
                        and [(c["indice"], c["criterio"], c["cita_textual"]) for c in x["criterios"]]
                        == [(j, c["criterio"], c["cita_textual"]) for j, c in enumerate(g["criterios"], 1)])
            for j, c in enumerate(x["criterios"], 1):
                es_reemplazo = c["cita_textual"] == pt.TEXTO_SIN_CITA
                autorizado = m["celda"] == "C5" and (m["id_pregunta"], j) in ce0.CRITERIOS_CITA_VACIA_AUTORIZADOS
                ok_cita &= es_reemplazo == autorizado and (j in m["criterios_sin_cita"]) == autorizado
            ok_id &= x["id_ficha"] == pt.id_ficha(sal, m["celda"], m["id_pregunta"], m["sha256_respuesta"])
    check("cada ficha pertenece a una celda de su planilla (mezclada: C2-C4; c5: C5)", ok_pl)
    check("n y número de criterios iguales a la tabla SOLO_MESA", ok_n)
    check("sha256 de cada respuesta = tabla SOLO_MESA", ok_sha)
    check("pregunta, TO, nombre del TO, ancla y criterios con su cita = gold de la pregunta", ok_gold)
    check("reemplazo de cita solo en los criterios sin cita autorizados de C5", ok_cita)
    check("id de ficha reproducible con la sal de la planilla", ok_id)
    ok_traza = True
    ins_tabs = {}
    for c in pt.CELDAS_ADJ:
        p = pt.rutas_insumos(ce0.CELDAS[c])
        ins_tabs[c] = {f["id_opaco"]: f for k in ("base_tab", "enc_tab") for f in pt._leer_json(p[k])["filas"]}
    for m in mesa.values():
        for r in m["respuestas"]:
            fila = ins_tabs[m["celda"]][r["id_opaco_respuesta"]]
            ok_traza &= pt.sha256_texto(pt.leer_respuesta(ce0.CELDAS[m["celda"]], fila)) == m["sha256_respuesta"]
    check("cada respuesta cubierta se lee de su traza con el mismo sha256", ok_traza)
    ok_orden = True
    for nom, pj in pjs.items():
        orden = sorted(x["id_ficha"] for x in pj["fichas"])
        random.Random(pt.PLANILLAS[nom]["semilla_orden"]).shuffle(orden)
        ok_orden &= orden == [x["id_ficha"] for x in pj["fichas"]]
    check("orden de cada planilla = un solo sorteo con su semilla sobre los ids ordenados", ok_orden)

    print("-- (5) planilla_mezclada: ningún campo separa sus fichas por celda")
    mz = pjs["planilla_mezclada"]["fichas"]
    check("mismas claves en todas las fichas y en todos los criterios",
          len({tuple(sorted(x)) for x in mz}) == 1
          and len({tuple(sorted(c)) for x in mz for c in x["criterios"]}) == 1)
    check("una sola sal para toda la planilla (la celda entra al hash, no se lee en el id)",
          len({pt.PLANILLAS["planilla_mezclada"]["sal_id_ficha"]}) == 1 and ok_id)
    por_q: dict[str, set] = {}
    for x in mz:
        clave = json.dumps({k: x[k] for k in ("to", "to_nombre", "ancla", "pregunta", "criterios")},
                           ensure_ascii=False, sort_keys=True)
        por_q.setdefault(mesa[x["id_ficha"]]["id_pregunta"], set()).add(clave)
    check("para una misma pregunta, todos los campos salvo la respuesta son idénticos entre fichas",
          all(len(v) == 1 for v in por_q.values()))
    check("el orden sale de un solo sorteo sobre la unión (no agrupado por celda)", ok_orden)

    print("-- (6) re-derivación y doble corrida")
    r1, r2 = pt.construir(), pt.construir()
    pub1, pub2 = pt.publicables(r1), pt.publicables(r2)
    sm1, sm2 = pt.solo_mesa(r1), pt.solo_mesa(r2)
    check("doble corrida: publicables y SOLO_MESA byte-idénticos entre sí", pub1 == pub2 and sm1 == sm2)
    check("re-derivación reproduce byte a byte los publicables escritos",
          all(p.read_text(encoding="utf-8") == t for p, t in pub1.items()))
    check("re-derivación reproduce byte a byte los SOLO_MESA escritos",
          all(p.read_text(encoding="utf-8") == t for p, t in sm1.items()))
    v = r1["verificacion"]
    check("finales recomputados desde los crudos del juez con agregar_par = tabla_celdas_E5.json",
          v["finales_reproducen_tabla_E5"])
    check("totales = esperados del anexo (25 pares ADJ, 29 respuestas objetivo en A, 14 fichas en B)",
          (v["pares_adj_total"], v["objetivos_a_total"], v["fichas_b_total"]) == (25, 29, 14))
    todas = [m for p in r1["planillas"].values() for m in p["mesa"]]
    check("C5: ninguna ficha de la muestra B sobre las preguntas excluidas del marco",
          not any(m["celda"] == "C5" and m["origen"].startswith("muestra_")
                  and m["id_pregunta"] in pt.EXCLUIDAS_MUESTRA["C5"] for m in todas))
    multi = [m for m in todas if len(m["respuestas"]) > 1]
    check("fichas con varias respuestas: solo pendientes del §7, un solo par, votos ADJ del juez",
          all(m["origen"] == "s7_pendiente" and all(r["veredicto_juez_respuesta"] == pt.ADJ
                                                    for r in m["respuestas"]) for m in multi))
    cubiertas = {(m["celda"], r["id_opaco_respuesta"]) for m in todas for r in m["respuestas"]}
    ok_cov = True
    for c, pc in r1["por_celda"].items():
        for x in pc["pob_a"]["heredados"]:
            ok_cov &= (c, x["id_opaco_base"]) in cubiertas
        for x in pc["pob_a"]["pendientes_s7"]:
            for ide, vv in zip(x["ids_reps"], x["veredictos_reps"]):
                ok_cov &= ((c, ide) in cubiertas) == (vv == pt.ADJ)
    check("población A: cada heredado y cada voto ADJ de un pendiente del §7 tiene ficha; "
          "los votos no ADJ no", ok_cov)
    ok_mb = True
    for m in todas:
        if not m["origen"].startswith("muestra_"):
            continue
        r = m["respuestas"][0]
        ok_mb &= len(m["respuestas"]) == 1 and r["veredicto_juez_respuesta"] == m["final_juez_par"]
        ok_mb &= (r["rep"] == 1 + m["veredictos_reps"].index(m["final_juez_par"])) if m["veredictos_reps"] \
            else r["rep"] is None
    check("muestra B: una respuesta por ficha, la de menor rep que coincide con el final (base si "
          "no se re-corrió)", ok_mb)
    claves_celda = [(m["celda"], m["id_pregunta"], m["sha256_respuesta"]) for m in todas]
    check("una ficha por (celda, pregunta, texto): nunca se comparte entre celdas",
          len(set(claves_celda)) == len(claves_celda))

    print("-- (7) provocación")
    md = textos[pt.planilla_md_path("planilla_mezclada").name]
    check("provocación 1: id de pregunta inyectado → detectado",
          any("marcador:EV2F-" == x for x in fugas_inequivocas(md + "\nEV2F-007", u)))
    check("provocación 2: sufijo opaco solo, sin prefijo → detectado",
          "sufijo_opaco" in fugas_inequivocas(md + "\n" + u["sufijos"][0], u))
    check("provocación 3: label de corrida inyectado → detectado",
          any(x == f"marcador:{ce0.CELDAS['C3'].label}"
              for x in fugas_inequivocas(md + "\n" + ce0.CELDAS["C3"].label, u)))
    check("provocación 4: sha de grafo abreviado a 8 hex → detectado",
          "sha_grafo" in fugas_inequivocas(md + "\n" + u["shas_grafo"][0][:8], u))
    check("provocación 5: sha de respuesta abreviado a 12 hex → detectado",
          "sha_respuesta" in fugas_inequivocas(md + "\n" + u["shas_resp"][0][:12], u))
    sucia = copy.deepcopy(pjs["planilla_mezclada"])
    sucia["fichas"][0]["to_nombre"] += " C3"
    check("provocación 6: celda inyectada fuera de los textos mostrados → detectada",
          bool(fugas_resto(json.dumps(blanquear(sucia), ensure_ascii=False))))
    sucia = copy.deepcopy(pjs["planilla_mezclada"])
    sucia["fichas"][0]["respuesta"] += " Neo4j memoria desarrollo"
    check("provocación 7: palabra común dentro de una respuesta → se cuenta, no falla",
          not fugas_resto(json.dumps(blanquear(sucia), ensure_ascii=False))
          and len(re.findall("neo4j", textos_mostrados(sucia), re.I))
          == len(re.findall("neo4j", textos_mostrados(pjs["planilla_mezclada"]), re.I)) + 1)
    sucia["instrucciones"] += " Neo4j"
    check("provocación 8: la misma palabra en las instrucciones → detectada",
          bool(fugas_resto(json.dumps(blanquear(sucia), ensure_ascii=False))))
    sucia = copy.deepcopy(pjs["planilla_mezclada"])
    sucia["fichas"][0]["respuesta"] += " KG-Tanda0"
    check("provocación 9: KG- dentro de una respuesta → detectado (inequívoco)",
          any(x == "marcador:KG-" for x in fugas_inequivocas(json.dumps(sucia, ensure_ascii=False), u)))

    passed = sum(ok for _, ok in _checks)
    print(f"\n  {passed}/{len(_checks)} checks OK")
    print("  RESULTADO:", "PASS" if passed == len(_checks) else "FAIL")
    return 0 if passed == len(_checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
