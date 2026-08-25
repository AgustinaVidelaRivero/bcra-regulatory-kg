"""
cierre_r1.py — CIERRE de U-B1.8 tras la adjudicación de la autora (USD 0):

  1. Veredictos DEFINITIVOS por par: mapping §2 en código sobre las marcas
     humanas del worksheet (sha 91c839c5…; nada se decide a mano) — heredados
     por vía `adjudicacion_base`; pendientes del §7 resolviendo cada voto ADJ
     con la ficha que lo cubre y re-agregando con `agregar_par` (9044a04),
     vía `adjudicacion_s7`; el resto conserva su final (juez_base / juez_enc).
  2. Tasa de error del juez EN AMBAS DIRECCIONES desde la muestra simétrica
     (acuerdo exacto por ficha, acuerdo por criterio, sobre-acreditación y
     sub-acreditación) — la muestra mide error del juez, no reemplaza
     veredictos.
  3. Tabla final de r1 AL LADO de las tres selladas (citadas, no re-medidas)
     con cobertura de criterios y abstenciones.
  4. Atribución causal A0.2 (regla sellada 40603a9, funciones IMPORTADAS de
     ev2_reporte/code/atribucion_fallas.py): 40 trazas base contra su propio
     veredicto + tabla secundaria de las 72 re-corridas §7; replay estándar y
     FUERTE obligatorios; censo de anclas con diagnóstico H24 y sensibilidad
     por descendientes (informativa); pares definitivos con traza
     representativa. Doble corrida interna byte-idéntica (salvo `generado`).
  5. Lectura P1–P5 en FORMATO FIJO (pre-registro §7): una fila por
     predicción, predicho | observado | veredicto, sin narrativa.
  6. Costos desde dbs (precios verificados 2026-08-23).

Salidas: cierre/{cierre_r1.json, reporte_final_r1.md, atribucion_por_traza_r1.md}.

Uso:  .venv/bin/python -B data/experiment/ev2_r1/code/cierre_r1.py
"""

from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_r1 as cr                      # noqa: E402  (registra r1 al importarse)
import comun_ev2 as ce                     # noqa: E402
import worksheet_r1 as wr                  # noqa: E402
import agregacion_enc as ag                # noqa: E402  (regla sellada 9044a04)
from comun_r1 import cf, mapping           # noqa: E402
from gasto_dbs_r1 import gasto_db          # noqa: E402

REPORTE_CODE = cr.EXP_DIR / "ev2_reporte" / "code"
if str(REPORTE_CODE) not in sys.path:
    sys.path.insert(0, str(REPORTE_CODE))
from atribucion_fallas import (CLASES, atribuir_payload, clasificar,  # noqa: E402
                               navegacion_de_traza, parse_ancla)
from harness import GraphIndex             # noqa: E402

CIERRE_DIR = cr.UNIDAD_DIR / "cierre"
WORKSHEET_SHA_ESPERADO = "91c839c5e0b5681f0b5588ec97607eaa1c4a9d282ce114f85d00d6ecfa899eff"
ADJ = "requiere_adjudicacion"

# Tabla definitiva SELLADA de EV2 (reporte_ev2.md §2 / tablero §2.b): se CITA.
SELLADAS = {
    "KG-Base (12c226e2)": {"correcto": 3, "parcial": 20, "incorrecto": 17,
                           "cobertura": 56, "abstenciones": 9},
    "KG-Refinado (26fac8b4)": {"correcto": 5, "parcial": 26, "incorrecto": 9,
                               "cobertura": 73, "abstenciones": 4},
    "KG-Reextraído (8e2eadee)": {"correcto": 4, "parcial": 27, "incorrecto": 9,
                                 "cobertura": 70, "abstenciones": 7},
}

# Predicciones del pre-registro §5 (sellado 6c5507b) — umbrales verbatim.
PRE = {
    "P1": {"texto": "censo: presentes(r1) >= 31/40 (no-resueltas <= 9)"},
    "P2a": {"texto": "trazas base ausencia_kg < 9, con diagnóstico granularidad < 8"},
    "P2b": {"texto": "incorrectos definitivos con clase ausencia_kg < 4"},
    "P3": {"texto": "generacion en trazas base dentro de 21 ± 3 ([18, 24])"},
    "P4": {"texto": "techo de retrieval (alcanzabilidad + vista_no_consultada, "
                    "trazas base) dentro de 6 ± 3 ([3, 9]); < 3 = hallazgo contra H17"},
    "P5": {"texto": "incorrectos definitivos <= 9; dirección de correctos/parciales "
                    "reportada con tamaño (diferencias de 1–3 preguntas no son señal)"},
}


def cargar_worksheet_marcado() -> dict:
    sha = cr.sha256_path(wr.WORKSHEET_JSON)
    if sha != WORKSHEET_SHA_ESPERADO:
        raise RuntimeError(f"worksheet con sha inesperado: {sha}")
    ws = json.loads(wr.WORKSHEET_JSON.read_text(encoding="utf-8"))
    marcas = [c["veredicto"] for f in ws["fichas"] for c in f["criterios"]]
    if len(marcas) != 49 or any(m not in ("cumplido", "no_cumplido") for m in marcas):
        raise RuntimeError("marcas incompletas o fuera de dominio")
    return ws


def humanos_por_ficha(ws: dict, mesa: dict) -> dict[str, dict]:
    """{id_ficha: {marcas, veredicto_humano}} — mapping §2 en código."""
    out = {}
    for f in ws["fichas"]:
        m = mesa[f["id_ficha"]]
        if len(f["criterios"]) != m["n_criterios"]:
            raise ValueError(f"{f['id_ficha']}: n_criterios inconsistente")
        marcas = [c["veredicto"] for c in f["criterios"]]
        out[f["id_ficha"]] = {"marcas": marcas,
                              "veredicto_humano": mapping.veredicto_pregunta(marcas)}
    return out


# --------------------------------------------------------------------------- #
# Definitivos                                                                  #
# --------------------------------------------------------------------------- #
def resolver_definitivos(ins: dict, ws: dict) -> dict:
    fin = wr.finales_por_par(ins)                       # re-verifica agregar_par
    tabla = json.loads(wr.TABLA_FICHAS.read_text(encoding="utf-8"))
    mesa = {f["id_ficha"]: f for f in tabla["fichas"]}
    hum = humanos_por_ficha(ws, mesa)

    # ficha que cubre cada respuesta ADJ (id_opaco_respuesta -> id_ficha)
    ficha_de_resp = {}
    for fid, m in mesa.items():
        for r in m["respuestas"]:
            ficha_de_resp[r["id_opaco_respuesta"]] = fid

    definitivos, resoluciones_s7 = [], []
    for x in fin:
        rec = {"id_pregunta": x["id_pregunta"], "id_opaco_base": x["id_opaco_base"],
               "final_pre_adjudicacion": x["final"], "re_corrido": x["re_corrido"],
               "tipo_enc": x["tipo_enc"], "veredictos_reps": x["veredictos_reps"],
               "ids_reps": x["ids_reps"]}
        if x["final"] != ADJ:
            rec.update({"definitivo": x["final"],
                        "via": "juez_enc" if x["fuente_final"] == "s7" else "juez_base"})
        elif not x["re_corrido"]:
            fid = ficha_de_resp[x["id_opaco_base"]]
            rec.update({"definitivo": hum[fid]["veredicto_humano"],
                        "via": "adjudicacion_base", "id_ficha": fid,
                        "marcas_humanas": hum[fid]["marcas"]})
        else:
            votos, resol = [], []
            for rep, (ide, v) in enumerate(zip(x["ids_reps"], x["veredictos_reps"]),
                                           start=1):
                if v == ADJ:
                    fid = ficha_de_resp[ide]
                    v = hum[fid]["veredicto_humano"]
                    resol.append({"rep": rep, "id_opaco_respuesta": ide,
                                  "id_ficha": fid, "veredicto_humano": v,
                                  "marcas_humanas": hum[fid]["marcas"]})
                votos.append(v)
            defin = ag.agregar_par(votos)
            if defin == ADJ:
                raise RuntimeError(f"{x['id_opaco_base']}: sigue ADJ tras adjudicar")
            rec.update({"definitivo": defin, "via": "adjudicacion_s7",
                        "votos_resueltos": votos, "resoluciones": resol})
            resoluciones_s7.append(rec)
        definitivos.append(rec)
    if len(definitivos) != 40:
        raise ValueError("definitivos != 40")
    return {"fin": fin, "mesa": mesa, "hum": hum, "ficha_de_resp": ficha_de_resp,
            "definitivos": definitivos,
            "tabla_definitiva": dict(Counter(d["definitivo"] for d in definitivos)),
            "vias": dict(Counter(d["via"] for d in definitivos))}


def marcas_representativas(res: dict, ins: dict) -> list[dict]:
    """Por par definitivo: traza representativa (regla ratificada de A0.2) y
    las marcas de la fuente del veredicto (modales del juez o humanas)."""
    out = []
    for d in res["definitivos"]:
        if d["via"] in ("juez_base", "adjudicacion_base"):
            origen, id_resp, rep = "base", d["id_opaco_base"], None
            if d["via"] == "juez_base":
                marcas = ins["base_agg"][d["id_opaco_base"]]["modales"]
            else:
                marcas = d["marcas_humanas"]
        else:
            votos = d.get("votos_resueltos") or d["veredictos_reps"]
            rep = next(r for r, v in enumerate(votos, start=1)
                       if v == d["definitivo"]
                       and d["veredictos_reps"][r - 1] != "sin_veredicto")
            id_resp = d["ids_reps"][rep - 1]
            origen = "enc"
            resol = {r["rep"]: r for r in d.get("resoluciones", [])}
            marcas = (resol[rep]["marcas_humanas"] if rep in resol
                      else ins["enc_agg"][id_resp]["modales"])
        out.append({**d, "repr_origen": origen, "repr_rep": rep,
                    "repr_id_opaco": id_resp, "repr_marcas": marcas,
                    "repr_cumplidos": marcas.count("cumplido"),
                    "auxiliar": (ins["base_agg"] if origen == "base"
                                 else ins["enc_agg"])[id_resp]["clasificacion_respuesta_modal"]})
    return out


# --------------------------------------------------------------------------- #
# Muestra simétrica: error del juez en ambas direcciones                       #
# --------------------------------------------------------------------------- #
def evaluar_muestra(res: dict, ins: dict) -> dict:
    filas = []
    for fid, m in res["mesa"].items():
        if m["origen"] not in ("muestra_correcto", "muestra_parcial_incorrecto"):
            continue
        h = res["hum"][fid]
        juez_final = m["final_juez_par"]
        modales = m["respuestas"][0]["modales_juez"]
        por_crit = list(zip(h["marcas"], modales))
        filas.append({
            "id_ficha": fid, "origen": m["origen"],
            "veredicto_juez": juez_final, "veredicto_humano": h["veredicto_humano"],
            "acuerdo_exacto": juez_final == h["veredicto_humano"],
            "n_criterios": m["n_criterios"],
            "criterios_acuerdo": sum(1 for a, b in por_crit if a == b),
            "juez_sobre_acredita": sum(1 for a, b in por_crit
                                       if a == "no_cumplido" and b == "cumplido"),
            "juez_sub_acredita": sum(1 for a, b in por_crit
                                     if a == "cumplido" and b == "no_cumplido"),
        })
    corr = [f for f in filas if f["origen"] == "muestra_correcto"]
    return {"n_fichas": len(filas),
            "acuerdo_exacto": sum(f["acuerdo_exacto"] for f in filas),
            "criterios": sum(f["n_criterios"] for f in filas),
            "criterios_acuerdo": sum(f["criterios_acuerdo"] for f in filas),
            "sobre_acreditacion_criterios": sum(f["juez_sobre_acredita"] for f in filas),
            "sub_acreditacion_criterios": sum(f["juez_sub_acredita"] for f in filas),
            "flip_descendente_correctos": sum(1 for f in corr
                                              if f["veredicto_humano"] != "correcto"),
            "n_correctos_auditados": len(corr),
            "filas": filas}


# --------------------------------------------------------------------------- #
# Atribución A0.2 sobre r1                                                     #
# --------------------------------------------------------------------------- #
def veredictos_por_traza(res: dict, ins: dict) -> tuple[dict, dict, list]:
    """(base {q: {...}}, enc {(q, rep): {...}}, excluidas)."""
    base = {}
    for d in res["definitivos"]:
        q = d["id_pregunta"]
        a = ins["base_agg"][d["id_opaco_base"]]
        if d["via"] == "adjudicacion_base":
            v, marcas, fuente = d["definitivo"], d["marcas_humanas"], "adjudicacion_base"
        else:
            v, marcas, fuente = a["veredicto_pregunta"], a["modales"], "juez_base"
        base[q] = {"veredicto": v, "fuente": fuente, "marcas": marcas,
                   "auxiliar": a["clasificacion_respuesta_modal"],
                   "id_opaco": d["id_opaco_base"]}
    enc, excluidas = {}, []
    resol_por_resp = {}
    for d in res["definitivos"]:
        for r in d.get("resoluciones", []) or []:
            resol_por_resp[r["id_opaco_respuesta"]] = r
    for f in ins["enc_tab"].values():
        a = ins["enc_agg"][f["id_opaco"]]
        v, marcas, fuente = a["veredicto_pregunta"], a["modales"], "juez_enc"
        if v == ADJ:
            if f["id_opaco"] in resol_por_resp:
                r = resol_por_resp[f["id_opaco"]]
                v, marcas, fuente = r["veredicto_humano"], r["marcas_humanas"], "adjudicacion_s7"
            else:
                excluidas.append({"id_pregunta": f["id_pregunta"], "rep": f["rep"],
                                  "id_opaco": f["id_opaco"],
                                  "motivo": "sin_veredicto_propio (voto ADJ de par "
                                            "decidido por invariancia)"})
                continue
        enc[(f["id_pregunta"], f["rep"])] = {
            "veredicto": v, "fuente": fuente, "marcas": marcas,
            "auxiliar": a["clasificacion_respuesta_modal"], "id_opaco": f["id_opaco"],
            "label": f["label"], "tipo": f["tipo"]}
    return base, enc, excluidas


def atribuir_r1(res: dict, ins: dict) -> dict:
    gold = {p["id"]: p["gold"]["ancla"] for p in ce.cargar_fidelidad()}
    aidx = cr.indice_anclas_r1()
    index = GraphIndex(ce.cargar_runtime(cr.R1_KEY))
    vb, ve, excluidas = veredictos_por_traza(res, ins)

    censo = {}
    for q, anclas in gold.items():
        censo[q] = {}
        for a in anclas:
            to, punto = parse_ancla(a)
            censo[q][a] = {"n": len(aidx.resolver(to, punto)),
                           "crudo_incl_contenedores": len(aidx.resolver(
                               to, punto, incluir_contenedores=True)),
                           "con_descendientes": len(aidx.resolver(
                               to, punto, incluir_descendientes=True))}

    def atribuir_dir(label: str, q: str, v: dict, origen: str, rep=None) -> dict:
        p = cr.TRAZAS_DIR / label / f"{q}.json"
        payload = json.loads(p.read_text(encoding="utf-8"))
        at = atribuir_payload(payload, gold[q], aidx, index, v["veredicto"])
        return {"origen": origen, "id_pregunta": q, "rep": rep, "label": label,
                "fuente_veredicto": v["fuente"], "auxiliar": v["auxiliar"],
                "n_criterios": len(v["marcas"]),
                "n_no_cumplidos": sum(1 for m in v["marcas"] if m == "no_cumplido"),
                **at}

    filas_base = [atribuir_dir(cr.R1["label"], q, vb[q], "base") for q in sorted(vb)]
    filas_enc = [atribuir_dir(v["label"], q, v, "enc", rep)
                 for (q, rep), v in sorted(ve.items())]

    def tabla(filas, key_fn):
        t = defaultdict(Counter)
        for x in filas:
            t[key_fn(x)][x["clase"] or "correcto"] += 1
        return {k: dict(v) for k, v in sorted(t.items())}

    def clase_conteo(filas):
        c = Counter((x["clase"] or "correcto") for x in filas)
        return {k: c.get(k, 0) for k in CLASES + ["correcto"]}

    # diagnóstico de anclas no resueltas + sensibilidad por descendientes (H24)
    diag = []
    for q, d in censo.items():
        for a, x in d.items():
            if x["n"] == 0:
                if x["crudo_incl_contenedores"] == 0 and x["con_descendientes"] > 0:
                    k = "granularidad"
                elif x["crudo_incl_contenedores"] == 0:
                    k = "ausencia_total"
                else:
                    k = "contenedor"
                diag.append({"id_pregunta": q, "ancla": a, **x, "diagnostico": k})
    diag_por_q = {d["id_pregunta"]: d for d in diag}
    sens = []
    for x in filas_base:
        if x["clase"] != "ausencia_kg":
            continue
        q = x["id_pregunta"]
        payload = json.loads((cr.TRAZAS_DIR / cr.R1["label"] / f"{q}.json")
                             .read_text(encoding="utf-8"))
        resueltas = {a: aidx.resolver(*parse_ancla(a), incluir_descendientes=True)
                     for a in gold[q]}
        nav = navegacion_de_traza(payload["trace"], resueltas, index,
                                  verificar_replay=False)
        sens.append({"id_pregunta": q, "veredicto": x["veredicto"],
                     "diagnostico_censal": diag_por_q.get(q, {}).get("diagnostico"),
                     "n_nodos_desc": sum(len(v) for v in resueltas.values()),
                     "clase_con_descendientes": clasificar(
                         x["veredicto"], nav["presente"], nav["vista"], nav["consultada"])})

    # pares definitivos: clase de la traza representativa
    reprs = marcas_representativas(res, ins)
    por_base = {x["id_pregunta"]: x for x in filas_base}
    por_enc = {(x["id_pregunta"], x["rep"]): x for x in filas_enc}
    pares_def = []
    for d in reprs:
        if d["repr_origen"] == "base":
            at = por_base[d["id_pregunta"]]
            clase = clasificar(d["definitivo"], at["ancla_presente"],
                               at["ancla_vista"], at["ancla_consultada"])
        else:
            at = por_enc[(d["id_pregunta"], d["repr_rep"])]
            clase = clasificar(d["definitivo"], at["ancla_presente"],
                               at["ancla_vista"], at["ancla_consultada"])
        pares_def.append({"id_pregunta": d["id_pregunta"], "definitivo": d["definitivo"],
                          "via": d["via"], "repr": f"{d['repr_origen']}"
                          + (f"_r{d['repr_rep']}" if d["repr_rep"] else ""),
                          "clase": clase, "auxiliar": at["auxiliar"]})

    return {
        "censo_anclas": censo,
        "diagnostico_no_resueltas": {"n": len(diag),
                                     "conteo": dict(Counter(d["diagnostico"] for d in diag)),
                                     "detalle": diag},
        "base": {"n": len(filas_base), "clase": clase_conteo(filas_base),
                 "clase_x_veredicto": tabla(filas_base, lambda x: x["veredicto"]),
                 "clase_x_auxiliar": tabla(filas_base, lambda x: x["auxiliar"]),
                 "replay_ok": sum(x["replay_ok"] for x in filas_base),
                 "replay_fuerte_ok": sum(x["replay_fuerte_ok"] for x in filas_base),
                 "por_traza": filas_base},
        "enc": {"n": len(filas_enc), "n_excluidas": len(excluidas),
                "excluidas": excluidas, "clase": clase_conteo(filas_enc),
                "clase_x_veredicto": tabla(filas_enc, lambda x: x["veredicto"]),
                "replay_ok": sum(x["replay_ok"] for x in filas_enc),
                "replay_fuerte_ok": sum(x["replay_fuerte_ok"] for x in filas_enc),
                "por_traza": filas_enc},
        "sensibilidad_descendientes": {
            "nota": ("INFORMATIVA, fuera de la regla ratificada (H24): re-clasificación "
                     "de las trazas base ausencia_kg con incluir_descendientes=True."),
            "conteo": dict(Counter(s["clase_con_descendientes"] for s in sens)),
            "detalle": sens},
        "pares_definitivos": {
            "clase_x_definitivo": tabla(pares_def, lambda x: x["definitivo"]),
            "incorrectos_detalle": [p for p in pares_def if p["definitivo"] == "incorrecto"],
            "por_par": pares_def},
        "reprs": reprs,
    }


# --------------------------------------------------------------------------- #
# P1–P5, costos, render                                                        #
# --------------------------------------------------------------------------- #
def lectura_p1p5(at: dict, res: dict) -> list[dict]:
    censo_pres = 40 - at["diagnostico_no_resueltas"]["n"]
    base_cl = at["base"]["clase"]
    gran_base = sum(1 for x in at["base"]["por_traza"] if x["clase"] == "ausencia_kg"
                    and (at["diagnostico_no_resueltas"] and
                         next((d["diagnostico"] for d in
                               at["diagnostico_no_resueltas"]["detalle"]
                               if d["id_pregunta"] == x["id_pregunta"]), None)
                         == "granularidad"))
    inc_def = at["pares_definitivos"]["clase_x_definitivo"].get("incorrecto", {})
    inc_aus = inc_def.get("ausencia_kg", 0)
    n_inc = sum(inc_def.values())
    techo = base_cl["alcanzabilidad"] + base_cl["vista_no_consultada"]
    td = res["tabla_definitiva"]
    filas = [
        {"prediccion": "P1", "predicho": PRE["P1"]["texto"],
         "observado": f"presentes {censo_pres}/40 (no-resueltas "
                      f"{at['diagnostico_no_resueltas']['n']})",
         "veredicto": "cumplida" if censo_pres >= 31 else "no cumplida"},
        {"prediccion": "P2a", "predicho": PRE["P2a"]["texto"],
         "observado": f"ausencia_kg {base_cl['ausencia_kg']} (granularidad {gran_base})",
         "veredicto": "cumplida" if base_cl["ausencia_kg"] < 9 and gran_base < 8
         else "no cumplida"},
        {"prediccion": "P2b", "predicho": PRE["P2b"]["texto"],
         "observado": f"incorrectos definitivos ausencia_kg {inc_aus} de {n_inc}",
         "veredicto": "cumplida" if inc_aus < 4 else "no cumplida"},
        {"prediccion": "P3", "predicho": PRE["P3"]["texto"],
         "observado": f"generacion {base_cl['generacion']}",
         "veredicto": "cumplida" if 18 <= base_cl["generacion"] <= 24
         else "no cumplida"},
        {"prediccion": "P4", "predicho": PRE["P4"]["texto"],
         "observado": f"alcanzabilidad {base_cl['alcanzabilidad']} + "
                      f"vista_no_consultada {base_cl['vista_no_consultada']} = {techo}",
         "veredicto": "cumplida" if 3 <= techo <= 9 else "no cumplida"},
        {"prediccion": "P5", "predicho": PRE["P5"]["texto"],
         "observado": f"incorrectos {td.get('incorrecto', 0)}; correctos "
                      f"{td.get('correcto', 0)} (selladas 3/5/4); parciales "
                      f"{td.get('parcial', 0)} (selladas 20/26/27)",
         "veredicto": "cumplida" if td.get("incorrecto", 0) <= 9 else "no cumplida"},
    ]
    return filas


def costos_desde_dbs() -> dict:
    cache = cr.CACHE_DIR
    lineas = {
        "agente_base (ev2_r1_base.db)": gasto_db(cache / "ev2_r1_base.db", 1.0, 5.0),
        "juez_base (ev2_r1_eval_r1..3.db)": None,
        "agente_s7 (ev2_r1_enc_r1..3.db)": None,
        "juez_s7 (ev2_r1_enc_juez_r1..3.db)": None,
    }
    jb = [gasto_db(cache / f"ev2_r1_eval_r{r}.db", 3.0, 15.0) for r in (1, 2, 3)]
    asx = [gasto_db(cache / f"ev2_r1_enc_r{r}.db", 1.0, 5.0) for r in (1, 2, 3)]
    js = [gasto_db(cache / f"ev2_r1_enc_juez_r{r}.db", 3.0, 15.0) for r in (1, 2, 3)]
    res = {"agente_base": round(lineas["agente_base (ev2_r1_base.db)"]["usd"], 4),
           "juez_base": round(sum(g["usd"] for g in jb), 4),
           "agente_s7": round(sum(g["usd"] for g in asx), 4),
           "juez_s7": round(sum(g["usd"] for g in js), 4),
           "adjudicacion_y_cierre": 0.0}
    res["total_usd"] = round(sum(v for v in res.values()), 4)
    res["precios"] = ("verificados 2026-08-23 contra platform.claude.com/docs/en/"
                      "about-claude/pricing: haiku-4.5 1/5 (cache 1,25x/0,10x); "
                      "sonnet-4.6 3/15")
    return res


def computar() -> dict:
    ws = cargar_worksheet_marcado()
    ins = wr.cargar_insumos()
    res = resolver_definitivos(ins, ws)
    at = atribuir_r1(res, ins)
    muestra = evaluar_muestra(res, ins)
    reprs = at["reprs"]
    cobertura = sum(d["repr_cumplidos"] for d in reprs)
    abstenciones = sum(1 for x in at["base"]["por_traza"] if x["auxiliar"] == "abstencion")
    tabla_final = {"correcto": res["tabla_definitiva"].get("correcto", 0),
                   "parcial": res["tabla_definitiva"].get("parcial", 0),
                   "incorrecto": res["tabla_definitiva"].get("incorrecto", 0),
                   "cobertura": cobertura, "abstenciones": abstenciones}
    return {
        "unidad": "U-B1.8 cierre (USD 0, offline)",
        "worksheet_sha256": WORKSHEET_SHA_ESPERADO,
        "sellos": cr.verificar_sellos(),
        "definitivos": res["definitivos"],
        "tabla_definitiva_r1": res["tabla_definitiva"],
        "vias": res["vias"],
        "tabla_final_con_selladas": {**SELLADAS,
                                     "KG-Reextraído-r1 (0226e947)": tabla_final},
        "muestra_simetrica": muestra,
        "atribucion": at,
        "lectura_p1p5": lectura_p1p5(at, res),
        "costos_desde_dbs": costos_desde_dbs(),
    }


def render_md(r: dict) -> str:
    L = ["# Cierre de U-B1.8 — fidelidad EV2 de KG-Reextraído-r1", "",
         f"Generado {r['generado']}. Worksheet adjudicado sha `{r['worksheet_sha256'][:16]}…`; "
         "mapping §2 en código sobre las marcas humanas; regla de atribución "
         "A0.2 (`40603a9`) con funciones importadas; doble corrida byte-idéntica.",
         "", "## 1. Tabla final (r1 AL LADO de las selladas; las selladas se citan de "
         "`reporte_ev2.md` §2, no se re-miden)", "",
         "| Grafo | correcto | parcial | incorrecto | cobertura de criterios (164) | abstenciones (base) |",
         "|---|---|---|---|---|---|"]
    for g, d in r["tabla_final_con_selladas"].items():
        negrita = "**" if "r1" in g else ""
        L.append(f"| {negrita}{g}{negrita} | {d['correcto']} | {d['parcial']} | "
                 f"{d['incorrecto']} | {d['cobertura']} | {d['abstenciones']}/40 |")
    L += ["", f"- vías de los 40 definitivos: {r['vias']}",
          "", "## 2. Muestra simétrica — tasa de error del juez (no reemplaza veredictos)", ""]
    m = r["muestra_simetrica"]
    L += [f"- acuerdo exacto: {m['acuerdo_exacto']}/{m['n_fichas']}; acuerdo por criterio: "
          f"{m['criterios_acuerdo']}/{m['criterios']}",
          f"- sobre-acreditación del juez (criterio: juez cumplido / humana no): "
          f"{m['sobre_acreditacion_criterios']}; sub-acreditación (juez no / humana sí): "
          f"{m['sub_acreditacion_criterios']}",
          f"- flip descendente de correctos auditados: {m['flip_descendente_correctos']}"
          f"/{m['n_correctos_auditados']}", ""]
    for f in m["filas"]:
        L.append(f"  - {f['id_ficha']} [{f['origen']}]: juez {f['veredicto_juez']} / "
                 f"humana {f['veredicto_humano']} — criterios {f['criterios_acuerdo']}"
                 f"/{f['n_criterios']}")
    at = r["atribucion"]
    L += ["", "## 3. Atribución causal A0.2 (r1)", "",
          "### 3.a Trazas base (40, contra su propio veredicto)", "",
          "| ausencia_kg | alcanzabilidad | vista_no_consultada | generacion | correcto | replay | replay fuerte |",
          "|---|---|---|---|---|---|---|"]
    b = at["base"]
    L.append(f"| {b['clase']['ausencia_kg']} | {b['clase']['alcanzabilidad']} | "
             f"{b['clase']['vista_no_consultada']} | {b['clase']['generacion']} | "
             f"{b['clase']['correcto']} | {b['replay_ok']}/{b['n']} | "
             f"{b['replay_fuerte_ok']}/{b['n']} |")
    L += ["", f"- clase × veredicto: {b['clase_x_veredicto']}",
          f"- clase × auxiliar: {b['clase_x_auxiliar']}",
          f"- anclas no resueltas: {at['diagnostico_no_resueltas']['n']} "
          f"{at['diagnostico_no_resueltas']['conteo']}",
          f"- sensibilidad por descendientes (informativa, H24): "
          f"{at['sensibilidad_descendientes']['conteo']}",
          "", "### 3.b Re-corridas §7 (secundaria, contra su propio veredicto)", ""]
    e = at["enc"]
    L += [f"- {e['n']} trazas ({e['n_excluidas']} excluida/s sin veredicto propio); "
          f"clase: {e['clase']}; replay {e['replay_ok']}/{e['n']}, fuerte "
          f"{e['replay_fuerte_ok']}/{e['n']}",
          "", "### 3.c Pares definitivos (traza representativa)", "",
          f"- clase × definitivo: {at['pares_definitivos']['clase_x_definitivo']}",
          "- incorrectos definitivos, uno por uno:"]
    for p in at["pares_definitivos"]["incorrectos_detalle"]:
        L.append(f"  - {p['id_pregunta']} [{p['via']}, {p['repr']}]: {p['clase']} "
                 f"({p['auxiliar']})")
    L += ["", "## 4. Lectura P1–P5 (formato fijo del pre-registro §7)", "",
          "| predicción | número predicho (umbral/banda) | número observado | veredicto |",
          "|---|---|---|---|"]
    for f in r["lectura_p1p5"]:
        L.append(f"| {f['prediccion']} | {f['predicho']} | {f['observado']} | "
                 f"**{f['veredicto']}** |")
    c = r["costos_desde_dbs"]
    L += ["", "## 5. Costos de la unidad (desde dbs; comando: gasto_dbs_r1.py)", "",
          "| etapa | USD |", "|---|---|",
          f"| agente base N=1 | {c['agente_base']} |",
          f"| juez base N=3 | {c['juez_base']} |",
          f"| agente §7 N=3 | {c['agente_s7']} |",
          f"| juez §7 N=3 | {c['juez_s7']} |",
          f"| adjudicación + cierre | {c['adjudicacion_y_cierre']} |",
          f"| **TOTAL** | **{c['total_usd']}** |",
          "", f"Precios: {c['precios']}.", ""]
    return "\n".join(L)


def render_por_traza(r: dict) -> str:
    L = ["# Atribución por traza — r1 (U-B1.8)", "",
         "| origen | id_pregunta | rep | veredicto | fuente | clase | auxiliar | "
         "presente/vista/consultada | replay/fuerte |", "|---|---|---|---|---|---|---|---|---|"]
    at = r["atribucion"]
    for x in at["base"]["por_traza"] + at["enc"]["por_traza"]:
        L.append(f"| {x['origen']} | {x['id_pregunta']} | {x['rep'] or '-'} | "
                 f"{x['veredicto']} | {x['fuente_veredicto']} | {x['clase'] or 'correcto'} | "
                 f"{x['auxiliar']} | {int(x['ancla_presente'])}/{int(x['ancla_vista'])}"
                 f"/{int(x['ancla_consultada'])} | {int(x['replay_ok'])}"
                 f"/{int(x['replay_fuerte_ok'])} |")
    return "\n".join(L) + "\n"


def main() -> int:
    print("== Cierre de U-B1.8 ($0, offline) ==")
    r1 = computar()
    r2 = computar()                                   # doble corrida byte-idéntica
    if json.dumps(r1, ensure_ascii=False, sort_keys=True) != \
            json.dumps(r2, ensure_ascii=False, sort_keys=True):
        raise RuntimeError("doble corrida NO byte-idéntica")
    b, e = r1["atribucion"]["base"], r1["atribucion"]["enc"]
    if b["replay_ok"] != b["n"] or b["replay_fuerte_ok"] != b["n"] \
            or e["replay_ok"] != e["n"] or e["replay_fuerte_ok"] != e["n"]:
        raise RuntimeError("replay con divergencias: corrida inválida, FRENAR")
    r1["generado"] = datetime.now().isoformat(timespec="seconds")
    r1["doble_corrida_byte_identica"] = True
    CIERRE_DIR.mkdir(parents=True, exist_ok=True)
    (CIERRE_DIR / "cierre_r1.json").write_text(
        json.dumps(r1, ensure_ascii=False, indent=2), encoding="utf-8")
    (CIERRE_DIR / "reporte_final_r1.md").write_text(render_md(r1), encoding="utf-8")
    (CIERRE_DIR / "atribucion_por_traza_r1.md").write_text(render_por_traza(r1),
                                                           encoding="utf-8")
    print(f"  definitivos r1: {r1['tabla_definitiva_r1']} | vías {r1['vias']}")
    print(f"  atribución base: {b['clase']} | replay {b['replay_ok']}/{b['n']} "
          f"fuerte {b['replay_fuerte_ok']}/{b['n']}")
    print(f"  muestra: acuerdo {r1['muestra_simetrica']['acuerdo_exacto']}"
          f"/{r1['muestra_simetrica']['n_fichas']} exacto, "
          f"{r1['muestra_simetrica']['criterios_acuerdo']}"
          f"/{r1['muestra_simetrica']['criterios']} por criterio")
    for f in r1["lectura_p1p5"]:
        print(f"  {f['prediccion']}: {f['veredicto']} — {f['observado']}")
    print(f"  costos: {r1['costos_desde_dbs']['total_usd']} USD")
    print(f"  -> {CIERRE_DIR / 'reporte_final_r1.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
