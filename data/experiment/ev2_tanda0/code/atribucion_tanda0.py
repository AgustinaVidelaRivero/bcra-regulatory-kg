"""
atribucion_tanda0.py — U-TANDA0-2A, etapa E6 b: atribución A0.2 de las fallas
de las celdas C2 a C5 con la regla sellada (data/experiment/ev2_reporte/
regla_atribucion.md, 40603a9; funciones IMPORTADAS de
ev2_reporte/code/atribucion_fallas.py, 85d9fdb, sin editar), y los puntos 3 a 5
de «LECTURA DE E6 — agregados» (plan, fila B6.0 fase 2a). USD 0, sin API.

El mandato pide la atribución sobre C3 y C4; el plan (punto 3) la pide para cada
respuesta parcial o incorrecta de C1 a C5. C1 se cita de 774acac
(ev2_r1/cierre/cierre_r1.json); C2 a C5 se computan acá con el mismo código.

Índice de cada celda: la regla re-ejecuta los pasos de la traza con el índice
del agente para saber qué vio y qué consultó (metrica.evaluar_traza) y hace
el replay fuerte contra steps_full (metrica_ev2.verificar_steps_full).
  - C3 y C5 (memoria): harness.GraphIndex sobre la vista runtime registrada por
    comun_tanda0 (igual que C1).
  - C2 y C4 (Neo4j fulltext): neo4j_index.Neo4jIndex en modo fulltext sobre la
    base cargada en el gate 5, solo lectura. Expone la misma interfaz que
    GraphIndex (neo4j_index.py:93-94), así que la regla corre sin cambios y el
    replay fuerte verifica que Neo4j devuelva hoy lo que la traza capturó.
Índice de anclas: resolucion.AnclaIndex (regla sellada: match exacto,
contenedores > 10 excluidos) sobre el kg.json de la celda con provenances
mapeadas como comun_r1.cargar_censo_raw_r1. Extensión declarada para C5: el
parser de anclas (sinteticas/comun.py, anclas_de_nodo) solo reconoce los cinco
PDF de desarrollo (DOC2TO, comun.py:52-56) e ignora toda provenance de otro
archivo; sin extensión, ninguna ancla de los cinco documentos nuevos resuelve y
toda falla de C5 saldría ausencia_kg por construcción. Para C5 se agrega a
DOC2TO, en memoria y solo mientras se construye el índice, el mapa archivo → TO
de los cinco nuevos tomado del manifiesto tanda0_10tos.json; C2 a C4 no cambian.

Veredicto de cada traza (patrón cierre_r1.veredictos_por_traza): base = el del
juez, salvo el heredado adjudicado, que toma el definitivo; re-corrida del §7 =
el del juez, salvo el voto requiere_adjudicacion resuelto por la instancia
adjudicadora; un voto requiere_adjudicacion de un par decidido por invariancia
queda excluido. Definitivos desde
data/experiment/ev2_tanda0/adjudicacion_SOLO_MESA/definitivos_por_par_tanda0_SOLO_MESA.json
(marcas 8e0597c, cierre ecd102c).

Puntos del plan:
  (3) por par definitivo parcial o incorrecto, la clase de su traza
      representativa: ausencia_kg = no estaba en el grafo; alcanzabilidad y
      vista_no_consultada = estaba y no se navegó hasta ella; generacion = se
      consultó y la respuesta igual falló. El cruce con los candidatos del §4
      del laudo de r2 y con la matriz pide lectura y no se hace acá.
  (4) patrones de A1.8 en todas las trazas: (a) un nodo que porta el ancla de
      la pregunta aparece como vecino por `referencia` en un ver_vecinos y
      nunca recibe ver_nodo en la traza; (b) ver_vecinos con dirección
      «salientes» sobre una Operacion que tiene aristas entrantes desde
      Restriccion en el grafo de la celda.
  (5) si alguna pregunta de EV2 o de C5 ancla en los puntos del ejemplo del
      préstamo (cla:5.1.1.1, cla:3.7).

Salidas: reports/tanda0/atribucion_tanda0.json, atribucion_tanda0.md y
atribucion_por_traza_tanda0.md (sin fechas).

Uso:  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/ev2_tanda0/code/atribucion_tanda0.py
"""

from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import planillas_tanda0 as pt              # noqa: E402  (insumos por celda con recómputo)
ce0 = pt.ce0
REPO = pt.REPO_DIR
REPORTE_CODE = pt.EXP_DIR / "ev2_reporte" / "code"
if str(REPORTE_CODE) not in sys.path:
    sys.path.insert(0, str(REPORTE_CODE))
from atribucion_fallas import (CLASES, atribuir_payload, clasificar,  # noqa: E402  (85d9fdb)
                               parse_ancla)
import comun_ev2 as ce                     # noqa: E402
from harness import GraphIndex             # noqa: E402
import resolucion                          # noqa: E402
from resolucion import AnclaIndex          # noqa: E402
from neo4j_index import Neo4jIndex         # noqa: E402
from conexion import abrir_driver          # noqa: E402

ADJ = "requiere_adjudicacion"
CELDAS = ("C2", "C3", "C4", "C5")
DEFINITIVOS = pt.SOLO_MESA_DIR / "definitivos_por_par_tanda0_SOLO_MESA.json"
C1_CIERRE = pt.EXP_DIR / "ev2_r1" / "cierre" / "cierre_r1.json"
REGLA_MD = pt.EXP_DIR / "ev2_reporte" / "regla_atribucion.md"
OUT_JSON = REPO / "reports" / "tanda0" / "atribucion_tanda0.json"
OUT_MD = REPO / "reports" / "tanda0" / "atribucion_tanda0.md"
OUT_TRAZAS = REPO / "reports" / "tanda0" / "atribucion_por_traza_tanda0.md"
PUNTOS_EJEMPLO = ("cla:5.1.1.1", "cla:3.7")
CLAVE_RUNTIME = {"C3": "tanda0_ens_desarrollo", "C5": "tanda0_ens_diez"}
MANIFIESTO_T0 = pt.EXP_DIR / "reextraccion_v2" / "manifiestos" / "tanda0_10tos.json"
COMUN_SINT = sys.modules[resolucion.anclas_de_nodo.__module__]     # sinteticas/comun.py


def docs_extra_c5() -> dict[str, str]:
    m = leer(MANIFIESTO_T0)
    return {t["archivo"]: t["id"] for t in m["tos"] if t["archivo"] not in COMUN_SINT.DOC2TO}


def indice_anclas(kg_path: Path, extra: dict | None) -> AnclaIndex:
    if not extra:
        return AnclaIndex(censo_raw(kg_path))
    original = dict(COMUN_SINT.DOC2TO)
    try:
        COMUN_SINT.DOC2TO.update(extra)
        return AnclaIndex(censo_raw(kg_path))
    finally:
        COMUN_SINT.DOC2TO.clear()
        COMUN_SINT.DOC2TO.update(original)


def sha256(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def leer(p: Path):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def censo_raw(path: Path) -> dict:
    data = leer(path)
    nodes = []
    for n in data.get("nodes", []):
        n = dict(n)
        provs = [ce._map_prov_v2(p) for p in (n.get("provenances") or
                                              ([n.get("provenance")] if n.get("provenance") else []))]
        n["provenances"] = [p for p in provs if p]
        nodes.append(n)
    return {"nodes": nodes, "edges": data.get("edges", [])}


def anclas_gold(celda) -> dict[str, list[str]]:
    if celda.conjunto == "ev2":
        return {p["id"]: list(p["gold"]["ancla"]) for p in leer(ce0.cf.GOLD_PATH)["preguntas"]}
    return {p["id"]: list(p["gold"]["ancla"]) for p in ce0.cargar_preguntas_c5()}


# --------------------------------------------------------------------------- #
# Veredictos por traza                                                         #
# --------------------------------------------------------------------------- #
def veredictos_por_traza(celda, ins: dict, defs: list[dict]) -> tuple[dict, dict, list]:
    base = {}
    for d in defs:
        fb = ins["base_tab"][d["id_opaco_base"]]
        a = ins["base_agg"][d["id_opaco_base"]]
        if d["via"] == "adjudicacion_base":
            v, marcas, fuente = d["definitivo"], d["marcas_humanas"], "adjudicacion_base"
        else:
            v, marcas, fuente = ins["rec_base"][d["id_opaco_base"]]["veredicto_pregunta"], a["modales"], "juez_base"
        base[d["id_pregunta"]] = {"veredicto": v, "fuente": fuente, "marcas": marcas,
                                  "auxiliar": a["clasificacion_respuesta_modal"], "label": fb["label"]}
    resol = {r["id_opaco_respuesta"]: r for d in defs for r in (d.get("resoluciones") or [])}
    enc, excluidas = {}, []
    for ide, f in ins["enc_tab"].items():
        a = ins["enc_agg"][ide]
        v, marcas, fuente = ins["rec_enc"][ide]["veredicto_pregunta"], a["modales"], "juez_enc"
        if v == ADJ:
            if ide in resol:
                r = resol[ide]
                v, marcas, fuente = r["veredicto_humano"], r["marcas_humanas"], "adjudicacion_s7"
            else:
                excluidas.append({"id_pregunta": f["id_pregunta"], "rep": f["rep"],
                                  "motivo": "voto requiere_adjudicacion de un par decidido por invariancia"})
                continue
        enc[(f["id_pregunta"], f["rep"])] = {"veredicto": v, "fuente": fuente, "marcas": marcas,
                                             "auxiliar": a["clasificacion_respuesta_modal"],
                                             "label": f["label"], "tipo": f["tipo"]}
    return base, enc, excluidas


# --------------------------------------------------------------------------- #
# Patrones de navegación (plan, punto 4)                                       #
# --------------------------------------------------------------------------- #
def patrones(payload: dict, nodos_ancla: set, tipo: dict, restr_entrantes: set) -> dict:
    abiertos = {s["input"].get("id") for s in payload.get("steps_full", []) if s["tool"] == "ver_nodo"}
    por_ref, salientes_op = set(), 0
    for s in payload.get("steps_full", []):
        if s["tool"] != "ver_vecinos":
            continue
        out = s.get("output") or {}
        for lista in (out.get("salientes") or []), (out.get("entrantes") or []):
            for v in lista:
                if v.get("relation") == "referencia" and v.get("vecino_id") in nodos_ancla:
                    por_ref.add(v["vecino_id"])
        nid = (s.get("input") or {}).get("id")
        if (s.get("input") or {}).get("direccion") == "salientes" and tipo.get(nid) == "Operacion" \
                and nid in restr_entrantes:
            salientes_op += 1
    return {"a_referencia_sin_abrir": len(por_ref - abiertos),
            "b_salientes_sobre_operacion_con_restriccion_entrante": salientes_op}


# --------------------------------------------------------------------------- #
# Una celda                                                                    #
# --------------------------------------------------------------------------- #
def atribuir_celda(c: str, driver) -> dict:
    celda = ce0.CELDAS[c]
    ins = pt.cargar_insumos(celda)
    defs = leer(DEFINITIVOS)["celdas"][c]["definitivos"]
    kg_path = ce0.kg_path(celda)
    if sha256(kg_path) != celda.kg_sha256:
        raise RuntimeError(f"{c}: kg.json con sha distinto del de la celda")
    extra = docs_extra_c5() if celda.conjunto == "tanda0" else None
    aidx = indice_anclas(kg_path, extra)
    if celda.backend == "memoria":
        index = GraphIndex(ce.cargar_runtime(CLAVE_RUNTIME[c]))
        indice_desc = f"GraphIndex en memoria ({CLAVE_RUNTIME[c]})"
    else:
        index = Neo4jIndex(driver, grafo=celda.grafo, modo="fulltext")
        indice_desc = f"Neo4jIndex fulltext ({celda.grafo}, índice {index.indice})"
    kg = leer(kg_path)
    tipo = {n["id"]: n["type"] for n in kg["nodes"]}
    restr_entrantes = {e["target"] for e in kg["edges"] if tipo.get(e["source"]) == "Restriccion"}
    gold = anclas_gold(celda)
    vb, ve, excluidas = veredictos_por_traza(celda, ins, defs)

    def una(label: str, q: str, v: dict, origen: str, rep=None) -> dict:
        p = ce0.RUTAS.trazas / label / f"{ce0.rv._sanitizar(q)}.json"
        payload = leer(p)
        at = atribuir_payload(payload, gold[q], aidx, index, v["veredicto"])
        nodos = {i for a in gold[q] for i in aidx.resolver(*parse_ancla(a))}
        pat = patrones(payload, nodos, tipo, restr_entrantes)
        return {"origen": origen, "id_pregunta": q, "rep": rep, "label": label,
                "veredicto": v["veredicto"], "fuente_veredicto": v["fuente"], "auxiliar": v["auxiliar"],
                "clase": at["clase"], "ancla_presente": at["ancla_presente"], "ancla_vista": at["ancla_vista"],
                "ancla_consultada": at["ancla_consultada"], "replay_ok": at["replay_ok"],
                "replay_fuerte_ok": at["replay_fuerte_ok"], "hit_tool_limit": at["hit_tool_limit"],
                "n_steps": at["n_steps"], **pat}

    filas_base = [una(v["label"], q, v, "base") for q, v in sorted(vb.items())]
    filas_enc = [una(v["label"], q, v, "enc", rep) for (q, rep), v in sorted(ve.items())]

    def clase_conteo(fs):
        k = Counter((x["clase"] or "correcto") for x in fs)
        return {n: k.get(n, 0) for n in CLASES + ["correcto"]}

    def cruce(fs):
        t = defaultdict(Counter)
        for x in fs:
            t[x["veredicto"]][x["clase"] or "correcto"] += 1
        return {k: dict(v) for k, v in sorted(t.items())}

    # pares definitivos: traza representativa (regla de cierre_r1.marcas_representativas)
    por_base = {x["id_pregunta"]: x for x in filas_base}
    por_enc = {(x["id_pregunta"], x["rep"]): x for x in filas_enc}
    pares = []
    for d in defs:
        if d["via"] in ("juez_base", "adjudicacion_base"):
            at, repr_ = por_base[d["id_pregunta"]], "base"
        else:
            votos = d.get("votos_resueltos") or d["veredictos_reps"]
            rep = next(r for r, v in enumerate(votos, start=1) if v == d["definitivo"])
            at, repr_ = por_enc[(d["id_pregunta"], rep)], f"enc_r{rep}"
        clase = clasificar(d["definitivo"], at["ancla_presente"], at["ancla_vista"], at["ancla_consultada"])
        pares.append({"id_pregunta": d["id_pregunta"], "definitivo": d["definitivo"], "via": d["via"],
                      "repr": repr_, "clase": clase, "auxiliar": at["auxiliar"]})
    lectura3 = {"no_estaba_en_el_grafo (ausencia_kg)": 0, "estaba_y_no_se_navego (alcanzabilidad + vista_no_consultada)": 0,
                "se_consulto_y_fallo (generacion)": 0}
    for p in pares:
        if p["definitivo"] in ("parcial", "incorrecto"):
            k = ("no_estaba_en_el_grafo (ausencia_kg)" if p["clase"] == "ausencia_kg" else
                 "se_consulto_y_fallo (generacion)" if p["clase"] == "generacion" else
                 "estaba_y_no_se_navego (alcanzabilidad + vista_no_consultada)")
            lectura3[k] += 1
    todas = filas_base + filas_enc
    return {"celda": c, "backend": celda.backend, "grafo": celda.grafo, "kg_sha256": celda.kg_sha256,
            "indice": indice_desc,
            "extension_doc2to": extra or None,
            "base": {"n": len(filas_base), "clase": clase_conteo(filas_base), "clase_x_veredicto": cruce(filas_base),
                     "replay_ok": sum(x["replay_ok"] for x in filas_base),
                     "replay_fuerte_ok": sum(x["replay_fuerte_ok"] for x in filas_base)},
            "enc": {"n": len(filas_enc), "n_excluidas": len(excluidas), "excluidas": excluidas,
                    "clase": clase_conteo(filas_enc), "replay_ok": sum(x["replay_ok"] for x in filas_enc),
                    "replay_fuerte_ok": sum(x["replay_fuerte_ok"] for x in filas_enc)},
            "pares_definitivos": {"clase_x_definitivo": cruce([{**p, "veredicto": p["definitivo"]} for p in pares]),
                                  "lectura_plan_punto_3": lectura3,
                                  "incorrectos": [p for p in pares if p["definitivo"] == "incorrecto"],
                                  "por_par": pares},
            "patrones_plan_punto_4": {
                "trazas": len(todas),
                "a_trazas_con_ancla_vista_por_referencia_sin_abrir": sum(1 for x in todas if x["a_referencia_sin_abrir"]),
                "a_nodos_ancla_vistos_por_referencia_sin_abrir": sum(x["a_referencia_sin_abrir"] for x in todas),
                "b_llamadas_salientes_sobre_operacion_con_restriccion_entrante":
                    sum(x["b_salientes_sobre_operacion_con_restriccion_entrante"] for x in todas),
                "b_trazas_con_esa_llamada": sum(1 for x in todas if x["b_salientes_sobre_operacion_con_restriccion_entrante"])},
            "por_traza": todas}


def c1_citada() -> dict:
    r = leer(C1_CIERRE)["atribucion"]
    pd = r["pares_definitivos"]
    lectura3 = Counter()
    for p in pd["por_par"]:
        if p["definitivo"] in ("parcial", "incorrecto"):
            lectura3[p["clase"]] += 1
    return {"fuente": "data/experiment/ev2_r1/cierre/cierre_r1.json (774acac)",
            "base_clase": r["base"]["clase"], "enc_clase": r["enc"]["clase"],
            "pares_definitivos_clase_x_definitivo": pd["clase_x_definitivo"],
            "lectura_plan_punto_3": {"no_estaba_en_el_grafo (ausencia_kg)": lectura3.get("ausencia_kg", 0),
                                     "estaba_y_no_se_navego (alcanzabilidad + vista_no_consultada)":
                                         lectura3.get("alcanzabilidad", 0) + lectura3.get("vista_no_consultada", 0),
                                     "se_consulto_y_fallo (generacion)": lectura3.get("generacion", 0)}}


def punto5() -> dict:
    hall = {}
    for c in ("C2", "C5"):
        for q, anclas in anclas_gold(ce0.CELDAS[c]).items():
            if any(a in PUNTOS_EJEMPLO or any(a.startswith(p + ".") for p in PUNTOS_EJEMPLO) for a in anclas):
                hall[q] = anclas
    return {"puntos": list(PUNTOS_EJEMPLO), "preguntas_que_anclan": hall,
            "lectura": ("no aplica a EV2 ni a C5: ninguna pregunta ancla en esos puntos" if not hall
                        else "aplica a las preguntas listadas")}


def computar(driver) -> dict:
    return {"unidad": "U-TANDA0-2A E6 b: atribución A0.2 (USD 0)",
            "regla": {"md": str(REGLA_MD.relative_to(REPO)), "sha256": sha256(REGLA_MD),
                      "codigo": "data/experiment/ev2_reporte/code/atribucion_fallas.py",
                      "codigo_sha256": sha256(REPORTE_CODE / "atribucion_fallas.py")},
            "definitivos": {"ruta": str(DEFINITIVOS.relative_to(REPO)), "sha256": sha256(DEFINITIVOS)},
            "c1": c1_citada(), "celdas": {c: atribuir_celda(c, driver) for c in CELDAS},
            "plan_punto_5": punto5()}


def render_md(r: dict) -> str:
    L = ["# Atribución A0.2 de las celdas C2 a C5 (U-TANDA0-2A E6 b)", "",
         f"Regla sellada `{r['regla']['md']}` (sha256 `{r['regla']['sha256'][:16]}…`), funciones importadas de "
         f"`{r['regla']['codigo']}`. Veredictos por traza desde `{r['definitivos']['ruta']}`. "
         "Generado por `data/experiment/ev2_tanda0/code/atribucion_tanda0.py`.", "",
         "## Trazas base, contra su propio veredicto", "",
         "| celda | índice | ausencia_kg | alcanzabilidad | vista_no_consultada | generacion | correcto | replay | replay fuerte |",
         "|---|---|---|---|---|---|---|---|---|",
         f"| C1 (774acac) | GraphIndex | {r['c1']['base_clase']['ausencia_kg']} | {r['c1']['base_clase']['alcanzabilidad']} | "
         f"{r['c1']['base_clase']['vista_no_consultada']} | {r['c1']['base_clase']['generacion']} | "
         f"{r['c1']['base_clase']['correcto']} | 40/40 | 40/40 |"]
    for c, x in r["celdas"].items():
        b = x["base"]
        L.append(f"| {c} | {x['indice']} | {b['clase']['ausencia_kg']} | {b['clase']['alcanzabilidad']} | "
                 f"{b['clase']['vista_no_consultada']} | {b['clase']['generacion']} | {b['clase']['correcto']} | "
                 f"{b['replay_ok']}/{b['n']} | {b['replay_fuerte_ok']}/{b['n']} |")
    L += ["", "## Re-corridas del §7 (secundaria)", ""]
    for c, x in r["celdas"].items():
        e = x["enc"]
        L.append(f"- {c}: {e['n']} trazas ({e['n_excluidas']} excluidas); clase {e['clase']}; replay "
                 f"{e['replay_ok']}/{e['n']}, fuerte {e['replay_fuerte_ok']}/{e['n']}")
    L += ["", "## Pares definitivos parciales o incorrectos (plan, punto 3)", "",
          "| celda | no estaba en el grafo | estaba y no se navegó | se consultó y falló |", "|---|---|---|---|"]
    for nom, l3 in [("C1 (774acac)", r["c1"]["lectura_plan_punto_3"])] + [(c, x["pares_definitivos"]["lectura_plan_punto_3"])
                                                                            for c, x in r["celdas"].items()]:
        L.append(f"| {nom} | {l3['no_estaba_en_el_grafo (ausencia_kg)']} | "
                 f"{l3['estaba_y_no_se_navego (alcanzabilidad + vista_no_consultada)']} | "
                 f"{l3['se_consulto_y_fallo (generacion)']} |")
    L += ["", "Incorrectos definitivos, uno por uno:"]
    for c, x in r["celdas"].items():
        for p in x["pares_definitivos"]["incorrectos"]:
            L.append(f"- {c} {p['id_pregunta']} [{p['via']}, {p['repr']}]: {p['clase']} ({p['auxiliar']})")
    L += ["", "## Patrones de navegación de A1.8 (plan, punto 4)", "",
          "| celda | trazas | (a) trazas con ancla vista por referencia sin abrir | (a) nodos | (b) llamadas salientes sobre Operacion con Restriccion entrante | (b) trazas |",
          "|---|---|---|---|---|---|"]
    for c, x in r["celdas"].items():
        p = x["patrones_plan_punto_4"]
        L.append(f"| {c} | {p['trazas']} | {p['a_trazas_con_ancla_vista_por_referencia_sin_abrir']} | "
                 f"{p['a_nodos_ancla_vistos_por_referencia_sin_abrir']} | "
                 f"{p['b_llamadas_salientes_sobre_operacion_con_restriccion_entrante']} | {p['b_trazas_con_esa_llamada']} |")
    L += ["", f"## Punto 5 del plan", "", f"- {r['plan_punto_5']['lectura']} ({', '.join(r['plan_punto_5']['puntos'])})", ""]
    return "\n".join(L)


def render_trazas(r: dict) -> str:
    L = ["# Atribución por traza, celdas C2 a C5 (U-TANDA0-2A E6 b)", "",
         "| celda | origen | pregunta | rep | veredicto | fuente | clase | auxiliar | presente/vista/consultada | replay/fuerte | (a) | (b) |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for c, x in r["celdas"].items():
        for t in x["por_traza"]:
            L.append(f"| {c} | {t['origen']} | {t['id_pregunta']} | {t['rep'] or '-'} | {t['veredicto']} | "
                     f"{t['fuente_veredicto']} | {t['clase'] or 'correcto'} | {t['auxiliar']} | "
                     f"{int(t['ancla_presente'])}/{int(t['ancla_vista'])}/{int(t['ancla_consultada'])} | "
                     f"{int(t['replay_ok'])}/{int(t['replay_fuerte_ok'])} | {t['a_referencia_sin_abrir']} | "
                     f"{t['b_salientes_sobre_operacion_con_restriccion_entrante']} |")
    return "\n".join(L) + "\n"


def main() -> int:
    driver = abrir_driver()
    try:
        r1 = computar(driver)
        r2 = computar(driver)
    finally:
        driver.close()
    if json.dumps(r1, sort_keys=True, ensure_ascii=False, default=str) != \
            json.dumps(r2, sort_keys=True, ensure_ascii=False, default=str):
        raise RuntimeError("doble cómputo NO idéntico")
    OUT_JSON.write_text(json.dumps(r1, ensure_ascii=False, indent=2, sort_keys=True, default=str) + "\n",
                        encoding="utf-8")
    r = leer(OUT_JSON)
    OUT_MD.write_text(render_md(r), encoding="utf-8")
    OUT_TRAZAS.write_text(render_trazas(r), encoding="utf-8")
    for c, x in r["celdas"].items():
        b, e = x["base"], x["enc"]
        print(f"  {c}: base {b['clase']} replay {b['replay_ok']}/{b['n']} fuerte {b['replay_fuerte_ok']}/{b['n']} | "
              f"enc replay {e['replay_ok']}/{e['n']} fuerte {e['replay_fuerte_ok']}/{e['n']}")
    for p in (OUT_JSON, OUT_MD, OUT_TRAZAS):
        print(f"  -> {p.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
