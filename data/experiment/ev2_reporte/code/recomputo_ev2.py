"""
recomputo_ev2.py — Recómputo determinístico (USD 0, sin API) de TODOS los
números que cita `reporte_ev2.md` (A0.1), desde los archivos commiteados de las
unidades de EV2. Cada bloque de la salida lleva la ruta del insumo del que
sale. Corrida repetida ⇒ salida idéntica (salvo la marca `generado`).

Salida: `salida/recomputo_ev2.json` (+ `salida/tablas_ev2.md` con las tablas
largas que el reporte no incluye, para el paquete de revisión).

Uso:  python3 -B data/experiment/ev2_reporte/code/recomputo_ev2.py
"""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from datetime import datetime

from comun_reporte import (CANONICO, ORDEN_GRAFOS, SALIDA_DIR, VEREDICTOS,
                           INSUMOS, cargar, escribir_json, rel_repo,
                           verificar_sellos)


def _c(grafo: str) -> str:
    return CANONICO[grafo]["nombre"]


def _tabla(por_grafo: dict) -> dict:
    """{grafo: Counter} -> filas ordenadas con nombre canónico."""
    return {g: {"nombre": _c(g), **{v: int(por_grafo.get(g, {}).get(v, 0)) for v in VEREDICTOS},
                "n": int(sum(por_grafo.get(g, {}).values()))}
            for g in ORDEN_GRAFOS}


# --------------------------------------------------------------------------- #
# 1. Fidelidad: base ciega, §7 y definitiva por grafo + vías                    #
# --------------------------------------------------------------------------- #
def bloque_fidelidad() -> dict:
    tabla = {f["id_opaco"]: f for f in cargar("tabla_base")["filas"]}
    agg_base = {a["id_opaco"]: a for a in cargar("agregados_base")["agregados"]}
    fin_enc = cargar("finales_enc")
    defs = cargar("veredictos_definitivos")["definitivos"]

    # 1.a base ciega × grafo (cruce de mesa sobre b624865)
    base_por_grafo = defaultdict(Counter)
    for op, a in agg_base.items():
        base_por_grafo[tabla[op]["grafo"]][a["veredicto_pregunta"]] += 1

    # 1.b final pre-adjudicación por par (regla de ev2_adjudicacion/README):
    #     par re-corrido en §7 → agregado de las re-corridas; si no → base.
    enc_por_par = {p["id_opaco_base"]: p for p in fin_enc["pares"]} if "pares" in fin_enc else None
    if enc_por_par is None:
        # el archivo trae la lista bajo otra clave: buscar la primera lista de dicts con id_opaco_base
        for k, v in fin_enc.items():
            if isinstance(v, list) and v and isinstance(v[0], dict) and "id_opaco_base" in v[0]:
                enc_por_par = {p["id_opaco_base"]: p for p in v}
                break
    pre_por_grafo = defaultdict(Counter)
    for op, a in agg_base.items():
        g = tabla[op]["grafo"]
        v = enc_por_par[op]["final"] if op in enc_por_par else a["veredicto_pregunta"]
        pre_por_grafo[g][v] += 1

    # 1.c definitiva × grafo y vías × grafo (64de678)
    def_por_grafo = defaultdict(Counter)
    vias_por_grafo = defaultdict(Counter)
    via_x_veredicto = defaultdict(Counter)
    filas = []
    for d in defs:
        f = tabla[d["id_opaco_base"]]
        def_por_grafo[f["grafo"]][d["definitivo"]] += 1
        vias_por_grafo[f["grafo"]][d["via"]] += 1
        via_x_veredicto[d["via"]][d["definitivo"]] += 1
        filas.append({"id_pregunta": f["id_pregunta"], "grafo": f["grafo"], "nombre": _c(f["grafo"]),
                      "id_opaco_base": d["id_opaco_base"], "final_juez": d["final_juez"],
                      "fuente_final_juez": d["fuente_final_juez"], "via": d["via"],
                      "definitivo": d["definitivo"]})
    filas.sort(key=lambda x: (x["id_pregunta"], ORDEN_GRAFOS.index(x["grafo"])))

    # 1.d por pregunta: perfil de los tres grafos
    por_pregunta = defaultdict(dict)
    for x in filas:
        por_pregunta[x["id_pregunta"]][x["grafo"]] = x["definitivo"]
    perfiles = Counter(tuple(por_pregunta[q].get(g) for g in ORDEN_GRAFOS) for q in por_pregunta)

    # 1.e definitivo × clasificación auxiliar del juez sobre la respuesta BASE
    #     (abstención / contenido; columna cruzada, pre-registro §1) y por TO
    gold = {p["id"]: p for p in cargar("gold_fidelidad")["preguntas"]}
    aux_x_def = defaultdict(Counter)
    aux_base = defaultdict(Counter)
    to_x_def = defaultdict(Counter)
    defs_por_op = {d["id_opaco_base"]: d for d in defs}
    for op, a in agg_base.items():
        f = tabla[op]
        aux_base[f["grafo"]][a["clasificacion_respuesta_modal"]] += 1
        aux_x_def[f["grafo"]][f"{a['clasificacion_respuesta_modal']}→{defs_por_op[op]['definitivo']}"] += 1
        to_x_def[(gold[f["id_pregunta"]]["to"], f["grafo"])][defs_por_op[op]["definitivo"]] += 1

    # cross-check contra el cruce sellado
    cruce = cargar("cruce_definitivo")["cruce_por_grafo"]
    ok = all(cruce[g][v] == def_por_grafo[g][v] for g in cruce for v in VEREDICTOS)

    return {
        "fuente": {"base": rel_repo(INSUMOS["agregados_base"]) + " × " + rel_repo(INSUMOS["tabla_base"]),
                   "s7": rel_repo(INSUMOS["finales_enc"]),
                   "definitiva": rel_repo(INSUMOS["veredictos_definitivos"]),
                   "cruce_sellado": rel_repo(INSUMOS["cruce_definitivo"])},
        "base_ciega_por_grafo": _tabla(base_por_grafo),
        "pre_adjudicacion_por_grafo": _tabla(pre_por_grafo),
        "definitiva_por_grafo": _tabla(def_por_grafo),
        "definitiva_coincide_con_cruce_sellado": ok,
        "vias_por_grafo": {g: {"nombre": _c(g), **dict(sorted(vias_por_grafo[g].items()))} for g in ORDEN_GRAFOS},
        "via_x_veredicto": {v: dict(sorted(c.items())) for v, c in sorted(via_x_veredicto.items())},
        "perfiles_por_pregunta": {"orden_grafos": ORDEN_GRAFOS,
                                  "conteo": {"/".join(k): n for k, n in perfiles.most_common()}},
        "auxiliar_base_por_grafo": {g: {"nombre": _c(g), **dict(sorted(aux_base[g].items()))} for g in ORDEN_GRAFOS},
        "auxiliar_base_x_definitivo_por_grafo": {g: {"nombre": _c(g), **dict(sorted(aux_x_def[g].items()))} for g in ORDEN_GRAFOS},
        "definitivo_por_to_y_grafo": {f"{to}/{g}": {v: to_x_def[(to, g)].get(v, 0) for v in VEREDICTOS[:3]}
                                      for to in ("ext", "cap", "cla", "ric", "pro") for g in ORDEN_GRAFOS},
        "definitiva_por_par": filas,
        "por_pregunta": {q: por_pregunta[q] for q in sorted(por_pregunta)},
    }


# --------------------------------------------------------------------------- #
# 2. Cobertura por criterios desde los veredictos definitivos                  #
# --------------------------------------------------------------------------- #
def bloque_criterios() -> dict:
    """Cobertura de criterios por grafo bajo la RESPUESTA REPRESENTATIVA de
    cada par:
      - via juez_base        → modales del juez sobre la respuesta base;
      - via adjudicacion_base→ marcas humanas de la ficha (respuesta base);
      - via juez_enc         → modales del juez sobre la re-corrida de MENOR
                                rep cuyo veredicto coincide con el final del
                                par (misma regla que la ficha del worksheet,
                                ev2_adjudicacion/checkpoint decisión 2);
      - via adjudicacion_s7  → re-corrida de menor rep cuyo veredicto RESUELTO
                                coincide con el definitivo; sus marcas son las
                                humanas si esa re-corrida fue adjudicada, o los
                                modales del juez si su voto ya era decidido.
    """
    tabla = {f["id_opaco"]: f for f in cargar("tabla_base")["filas"]}
    agg_base = {a["id_opaco"]: a for a in cargar("agregados_base")["agregados"]}
    agg_enc = {a["id_opaco"]: a for a in cargar("agregados_enc")["agregados"]}
    tabla_enc = cargar("tabla_enc")["filas"]
    enc_por_par_rep = {(f["id_opaco_base"], f["rep"]): f for f in tabla_enc}
    ws = {f["id_ficha"]: f for f in json.loads(
        (INSUMOS["veredictos_definitivos"].parent / "worksheet_adjudicacion.json").read_text(encoding="utf-8"))["fichas"]}
    tabla_fichas = {f["id_ficha"]: f for f in cargar("tabla_fichas")["fichas"]}
    fin_enc = cargar("finales_enc")
    enc_pares = None
    for k, v in fin_enc.items():
        if isinstance(v, list) and v and isinstance(v[0], dict) and "id_opaco_base" in v[0]:
            enc_pares = {p["id_opaco_base"]: p for p in v}
            break
    defs = cargar("veredictos_definitivos")["definitivos"]
    gold = {p["id"]: p for p in cargar("gold_fidelidad")["preguntas"]}

    def marcas_ficha(id_ficha: str) -> list[str]:
        return [c["veredicto"] for c in ws[id_ficha]["criterios"]]

    def ficha_de_respuesta(id_opaco_resp: str, fichas: list[str]) -> str | None:
        for fid in fichas:
            for r in tabla_fichas[fid]["respuestas"]:
                if r["id_opaco_respuesta"] == id_opaco_resp:
                    return fid
        return None

    filas = []
    for d in defs:
        op = d["id_opaco_base"]
        f = tabla[op]
        via = d["via"]
        if via == "juez_base":
            marcas = agg_base[op]["modales"]; rep = None; origen = "base/juez"
        elif via == "adjudicacion_base":
            marcas = d["marcas_humanas"]; rep = None; origen = "base/humana"
        elif via == "juez_enc":
            votos = enc_pares[op]["votos"] if "votos" in enc_pares[op] else None
            # buscar menor rep cuyo veredicto del juez == final
            rep = None
            for r in (1, 2, 3):
                fe = enc_por_par_rep[(op, r)]
                if agg_enc[fe["id_opaco"]]["veredicto_pregunta"] == d["definitivo"]:
                    rep = r; break
            assert rep is not None, (op, via)
            marcas = agg_enc[enc_por_par_rep[(op, rep)]["id_opaco"]]["modales"]; origen = f"enc_r{rep}/juez"
        elif via == "adjudicacion_s7":
            rep = None
            for r, vr in zip((1, 2, 3), d["votos_resueltos"]):
                if vr == d["definitivo"]:
                    rep = r; break
            assert rep is not None, (op, via)
            fe = enc_por_par_rep[(op, rep)]
            fid = ficha_de_respuesta(fe["id_opaco"], d["fichas"])
            if fid is not None:
                marcas = marcas_ficha(fid); origen = f"enc_r{rep}/humana"
            else:
                marcas = agg_enc[fe["id_opaco"]]["modales"]; origen = f"enc_r{rep}/juez"
        else:
            raise ValueError(via)
        assert len(marcas) == len(gold[f["id_pregunta"]]["gold"]["criterios"]), (op, len(marcas))
        assert all(m in ("cumplido", "no_cumplido") for m in marcas), (op, marcas)
        filas.append({"id_pregunta": f["id_pregunta"], "grafo": f["grafo"], "nombre": _c(f["grafo"]),
                      "id_opaco_base": op, "via": via, "definitivo": d["definitivo"],
                      "respuesta_representativa": origen, "n_criterios": len(marcas),
                      "cumplidos": sum(1 for m in marcas if m == "cumplido"),
                      "no_cumplidos": sum(1 for m in marcas if m == "no_cumplido"),
                      "marcas": marcas})
    filas.sort(key=lambda x: (x["id_pregunta"], ORDEN_GRAFOS.index(x["grafo"])))
    por_grafo = {}
    for g in ORDEN_GRAFOS:
        xs = [x for x in filas if x["grafo"] == g]
        n = sum(x["n_criterios"] for x in xs); c = sum(x["cumplidos"] for x in xs)
        por_grafo[g] = {"nombre": _c(g), "n_pares": len(xs), "n_criterios": n, "cumplidos": c,
                        "no_cumplidos": n - c, "cobertura": round(c / n, 4) if n else None,
                        "cobertura_por_via": {}}
        for via in ("juez_base", "adjudicacion_base", "juez_enc", "adjudicacion_s7"):
            ys = [x for x in xs if x["via"] == via]
            nn = sum(x["n_criterios"] for x in ys); cc = sum(x["cumplidos"] for x in ys)
            por_grafo[g]["cobertura_por_via"][via] = {"n_pares": len(ys), "n_criterios": nn, "cumplidos": cc}
    # consistencia con el mapping §2: cumplidos==n ⇔ correcto; 0 ⇔ incorrecto
    incons = [x["id_opaco_base"] for x in filas
              if (x["definitivo"] == "correcto") != (x["cumplidos"] == x["n_criterios"])
              or (x["definitivo"] == "incorrecto") != (x["cumplidos"] == 0)]
    return {"regla": bloque_criterios.__doc__.strip(),
            "fuente": [rel_repo(INSUMOS["veredictos_definitivos"]), rel_repo(INSUMOS["agregados_base"]),
                       rel_repo(INSUMOS["agregados_enc"]), rel_repo(INSUMOS["tabla_enc"]),
                       rel_repo(INSUMOS["tabla_fichas"]),
                       rel_repo(INSUMOS["veredictos_definitivos"].parent / "worksheet_adjudicacion.json"),
                       rel_repo(INSUMOS["gold_fidelidad"])],
            "n_criterios_gold": sum(len(p["gold"]["criterios"]) for p in gold.values()),
            "por_grafo": por_grafo,
            "inconsistencias_con_mapping": incons,
            "por_par": filas}


# --------------------------------------------------------------------------- #
# 3. Navegabilidad, censo y ausencias                                          #
# --------------------------------------------------------------------------- #
def bloque_navegabilidad() -> dict:
    nav = cargar("agregados_nav")
    censo = cargar("censo_resumen")
    aus = cargar("ausencias_diagnostico")
    out = {"fuente": {"navegabilidad": rel_repo(INSUMOS["agregados_nav"]),
                      "censo": rel_repo(INSUMOS["censo_resumen"]),
                      "ausencias": rel_repo(INSUMOS["ausencias_diagnostico"])},
           "definiciones": nav["definiciones"], "por_grafo": {}, "censo": {}, "ausencias": {}}
    for g in ORDEN_GRAFOS:
        pg = nav["por_grafo"][g]
        out["por_grafo"][g] = {"nombre": _c(g), "label": pg["label"], "n_casos_evaluados": pg["n_casos_evaluados"],
                               "replay_ok_todos": pg["replay_ok_todos"],
                               "replay_fuerte_ok_todos": pg["replay_fuerte_ok_todos"],
                               "por_variante": pg["por_variante"],
                               "brecha_literal_menos_antilexica": {
                                   k: round(pg["por_variante"]["literal"][k] - pg["por_variante"]["antilexica"][k], 4)
                                   for k in ("recall_vista_micro", "recall_vista_macro",
                                             "recall_consultada_micro", "recall_consultada_macro")},
                               "cohorte_nucleo_limpio_EE": pg.get("cohorte_nucleo_limpio_EE"),
                               "cohorte_dirigida_EA_ED": pg.get("cohorte_dirigida_EA_ED")}
        cg = censo["grafos"][g]
        out["censo"][g] = {"nombre": _c(g), **{k: cg[k] for k in (
            "n_presentes", "n_presentes_completos", "n_presentes_parciales", "n_ausentes",
            "ids_ausentes", "ids_presentes_parciales", "n_contenedores_excluidos", "n_provenances_sin_parsear")}}
        det = aus["grafos"][g]["detalle"]
        cnt = Counter()
        for x in det:
            crudo, desc = x["nodos_crudo_incl_contenedores"], x["nodos_con_descendientes"]
            if crudo == 0 and desc > 0:
                cnt["crudo=0,desc>0 (solo sub-puntos: granularidad de ancla)"] += 1
            elif crudo == 0 and desc == 0:
                cnt["crudo=0,desc=0 (ausencia total)"] += 1
            elif crudo >= 1 and desc > 0:
                cnt["crudo>=1,desc>0 (portador no resuelve bajo la regla)"] += 1
            else:
                cnt["crudo>=1,desc=0 (portador no resuelve bajo la regla)"] += 1
        out["ausencias"][g] = {"nombre": _c(g), "n_anclas_no_resueltas": aus["grafos"][g]["n_anclas_no_resueltas"],
                               "diagnostico": dict(cnt), "detalle": det}
    out["ausencias"]["nota_archivo"] = aus["nota"]
    return out


# --------------------------------------------------------------------------- #
# 4. Juez: calibración + validación contra adjudicación humana                 #
# --------------------------------------------------------------------------- #
def bloque_juez() -> dict:
    ac = cargar("juez_acuerdo_app")
    mu = cargar("reporte_muestra")
    cruce = cargar("cruce_definitivo")
    base = cargar("agregados_base")
    enc = cargar("agregados_enc")

    def nodet(agg: dict) -> dict:
        pares = 0; unan = 0; sin = 0; dud = 0
        for a in agg["agregados"]:
            for c in a["criterios"]:
                pares += 1
                if len(set(c["veredictos_reps"])) == 1:
                    unan += 1
                if c["modal"] == "sin_consenso":
                    sin += 1
                if c["modal"] == "dudoso":
                    dud += 1
        return {"pares": pares, "unanimes": unan, "sin_consenso": sin, "modal_dudoso": dud}

    return {
        "fuente": {"calibracion": rel_repo(INSUMOS["juez_acuerdo_app"]),
                   "registro": "data/experiment/ev2_juez/calibracion/registro_calibracion.md",
                   "muestra": rel_repo(INSUMOS["reporte_muestra"]),
                   "cruce_muestra": rel_repo(INSUMOS["cruce_definitivo"])},
        "calibracion_u6": {"n": ac["n"], "acuerdo": ac["acuerdo"], "desacuerdo": ac["desacuerdo"],
                           "requiere_adjudicacion": ac["requiere_adjudicacion"],
                           "matriz_humano_juez": ac["matriz_humano_juez"],
                           "proxy_criterio": ac["proxy_criterio"], "no_determinismo": ac["no_determinismo"],
                           "fragmentos_auditoria": ac["fragmentos_auditoria"]},
        "muestra_simetrica": {k: mu[k] for k in mu if k not in ("filas", "fichas", "detalle")},
        "muestra_por_grafo": {g: {"nombre": _c(g), **cruce["cruce_muestra_por_grafo"][g]} for g in ORDEN_GRAFOS},
        "no_determinismo_base": nodet(base),
        "no_determinismo_enc": nodet(enc),
        "resueltos_dudosos_por_adjudicacion": cargar("veredictos_definitivos")["resueltos_dudosos"],
    }


# --------------------------------------------------------------------------- #
# 5. Costos por unidad (archivo exacto citado por línea)                       #
# --------------------------------------------------------------------------- #
def bloque_costos() -> dict:
    lineas = []
    tot = 0.0
    for g in ("v2", "v3", "run3"):
        r = cargar(f"resumen_agente_{g}")
        lineas.append({"unidad": "ev2_corrida (agente, corrida base N=1)", "componente": f"label {r['label']}",
                       "usd": round(r["costo_usd"], 4), "archivo": rel_repo(INSUMOS[f"resumen_agente_{g}"]),
                       "campo": "costo_usd", "n": f"{r['n_casos_corridos']} casos"})
        tot += r["costo_usd"]
    r = cargar("resumen_fidelidad")
    lineas.append({"unidad": "ev2_fidelidad_eval (juez v1, N=3, 120 respuestas)", "componente": "juez",
                   "usd": r["gasto_real"]["usd"], "archivo": rel_repo(INSUMOS["resumen_fidelidad"]),
                   "campo": "gasto_real.usd", "n": f"{r['llamadas_hechas']} llamadas"}); tot += r["gasto_real"]["usd"]
    r = cargar("resumen_agente_enc")
    lineas.append({"unidad": "ev2_encadenamiento (agente, 198 re-corridas)", "componente": "agente",
                   "usd": r["gasto_dbs"]["total"]["usd"], "archivo": rel_repo(INSUMOS["resumen_agente_enc"]),
                   "campo": "gasto_dbs.total.usd", "n": f"{r['indice']['n_persistidas']} trazas"}); tot += r["gasto_dbs"]["total"]["usd"]
    r = cargar("resumen_juez_enc")
    lineas.append({"unidad": "ev2_encadenamiento (juez v1, N=3, 198 respuestas)", "componente": "juez",
                   "usd": r["gasto_real"]["usd"], "archivo": rel_repo(INSUMOS["resumen_juez_enc"]),
                   "campo": "gasto_real.usd", "n": f"{r['llamadas_hechas']} llamadas ({r['gasto_real']['filas']} pagadas)"}); tot += r["gasto_real"]["usd"]
    for k, desc in (("juez_resumen_b2", "calibración pasada 1 sobre trazas B2 — NO VÁLIDA (gasto real)"),
                    ("juez_resumen_app", "calibración pasada válida v1 (fuente app)"),
                    ("juez_resumen_app_v11", "calibración iteración v1.1 — DESCARTADA (gasto real)")):
        r = cargar(k)
        lineas.append({"unidad": "ev2_juez (calibración)", "componente": desc, "usd": r["gasto_real"]["usd"],
                       "archivo": rel_repo(INSUMOS[k]), "campo": "gasto_real.usd",
                       "n": f"{r['llamadas_hechas']} llamadas"}); tot += r["gasto_real"]["usd"]
    for u in ("ev2_corrida/navegabilidad (replay determinístico)", "ev2_adjudicacion (worksheet + cierre)",
              "ev2_reporte (esta unidad)"):
        lineas.append({"unidad": u, "componente": "offline", "usd": 0.0, "archivo": "—", "campo": "—", "n": "—"})
    return {"lineas": lineas, "total_usd": round(tot, 4),
            "nota": "Las pasadas inválida (B2) y descartada (v1.1) de calibración cuentan como gasto real. "
                    "Fuera del total: la construcción del set (queries sintéticas fase B, USD 2,20 según commit "
                    "5ceb816; generación ciega del eje de fidelidad, sin costo de API en el repo) y la "
                    "re-extracción del grafo (USD 32,97, commit 5273c0c), que son unidades previas al sello EV2."}


# --------------------------------------------------------------------------- #
# Tablas largas (paquete de revisión)                                          #
# --------------------------------------------------------------------------- #
def tablas_md(rec: dict) -> str:
    L = ["# Tablas largas del recómputo EV2 (paquete de revisión de U-A0)", "",
         "Generadas por `data/experiment/ev2_reporte/code/recomputo_ev2.py`; fuente por bloque en "
         "`salida/recomputo_ev2.json`.", ""]
    L += ["## T1. Veredicto definitivo por par (120), con vía", "",
          "| id_pregunta | grafo | final juez | fuente | vía | definitivo |", "|---|---|---|---|---|---|"]
    for x in rec["fidelidad"]["definitiva_por_par"]:
        L.append(f"| {x['id_pregunta']} | {x['nombre']} | {x['final_juez']} | {x['fuente_final_juez']} | {x['via']} | {x['definitivo']} |")
    L += ["", "## T2. Perfil por pregunta (KG-Base / KG-Refinado / KG-Reextraído)", "",
          "| id_pregunta | KG-Base | KG-Refinado | KG-Reextraído |", "|---|---|---|---|"]
    for q, v in rec["fidelidad"]["por_pregunta"].items():
        L.append(f"| {q} | {v['run_3']} | {v['v3']} | {v['v2']} |")
    L += ["", "## T3. Cobertura por criterios, por par (respuesta representativa)", "",
          "| id_pregunta | grafo | vía | definitivo | respuesta representativa | cumplidos/n |", "|---|---|---|---|---|---|"]
    for x in rec["criterios"]["por_par"]:
        L.append(f"| {x['id_pregunta']} | {x['nombre']} | {x['via']} | {x['definitivo']} | {x['respuesta_representativa']} | {x['cumplidos']}/{x['n_criterios']} |")
    L += ["", "## T4. Diagnóstico de ausencias por ancla (censo del eje sintético)", "",
          "| grafo | sample_id | estado del caso | ancla | crudo (incl. contenedores) | con descendientes |", "|---|---|---|---|---|---|"]
    for g in ORDEN_GRAFOS:
        for x in rec["navegabilidad"]["ausencias"][g]["detalle"]:
            L.append(f"| {_c(g)} | {x['sample_id']} | {x['estado_caso']} | {x['ancla']} | {x['nodos_crudo_incl_contenedores']} | {x['nodos_con_descendientes']} |")
    return "\n".join(L) + "\n"


def main() -> int:
    sellos = verificar_sellos()
    rec = {"generado": datetime.now().isoformat(timespec="seconds"),
           "unidad": "U-A0 / A0.1 — recómputo determinístico (USD 0)",
           "nomenclatura": {g: CANONICO[g] for g in ORDEN_GRAFOS},
           "sellos_insumos": sellos,
           "fidelidad": bloque_fidelidad(),
           "criterios": bloque_criterios(),
           "navegabilidad": bloque_navegabilidad(),
           "juez": bloque_juez(),
           "costos": bloque_costos()}
    escribir_json(SALIDA_DIR / "recomputo_ev2.json", rec)
    (SALIDA_DIR / "tablas_ev2.md").write_text(tablas_md(rec), encoding="utf-8")
    fid = rec["fidelidad"]
    print("base ciega × grafo:", {g: [fid['base_ciega_por_grafo'][g][v] for v in VEREDICTOS] for g in ORDEN_GRAFOS})
    print("pre-adjudicación × grafo:", {g: [fid['pre_adjudicacion_por_grafo'][g][v] for v in VEREDICTOS] for g in ORDEN_GRAFOS})
    print("definitiva × grafo:", {g: [fid['definitiva_por_grafo'][g][v] for v in VEREDICTOS] for g in ORDEN_GRAFOS},
          "coincide con cruce sellado:", fid["definitiva_coincide_con_cruce_sellado"])
    print("vías × grafo:", {g: fid["vias_por_grafo"][g] for g in ORDEN_GRAFOS})
    print("cobertura criterios:", {g: (rec['criterios']['por_grafo'][g]['cumplidos'], rec['criterios']['por_grafo'][g]['n_criterios'], rec['criterios']['por_grafo'][g]['cobertura']) for g in ORDEN_GRAFOS},
          "inconsistencias:", rec["criterios"]["inconsistencias_con_mapping"])
    print("ausencias diag:", {g: rec['navegabilidad']['ausencias'][g]['diagnostico'] for g in ORDEN_GRAFOS})
    print("costos total USD:", rec["costos"]["total_usd"])
    print(f"→ {SALIDA_DIR / 'recomputo_ev2.json'} ; {SALIDA_DIR / 'tablas_ev2.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
