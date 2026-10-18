"""Mesa, §145 (17/10/2026): el cruce del gold de Q12, mitad de ajuste, con los veredictos del juez de EV2. USD 0, sin API.

Sigue `decisiones_128_mesa/gold/para_leer/como_se_mide_el_juez_gold_q12.md` y el asiento de la §129
(`decisiones_129_mesa/gold/asiento_medicion_gold_q12_mesa.md`), con las dos propuestas confirmadas por la autora el 16/10 a las 14:04:04 y
otra vez el 17/10 (§145):
  - un «dudoso» del juez (o un «sin_consenso») cuenta como desacuerdo, y al lado va la cifra sin esos pares; en la respuesta, su
    «requiere_adjudicacion» cuenta igual;
  - la cifra principal va sobre los 82 pares, con todas las marcas de la autora; al lado, sin los marcados «necesita experto del dominio» o
    «criterio mal planteado».
Y la cifra que pidió la autora: cuántas de las 20 llegaron a su adjudicación en EV2 (vía `adjudicacion_base` de los veredictos definitivos,
regla de `ev2_reporte/code/recomputo_ev2.py:132`, `:176`) y las cifras principales sin ellas; las de `adjudicacion_s7`, aparte.
Insumos: las planillas selladas de la autora (copias), la clave del sorteo, y del repo (un clon de git) los veredictos agregados del juez
(`data/experiment/ev2_fidelidad_eval/out/veredictos_agregados_ciego.json`) y los definitivos
(`data/experiment/ev2_adjudicacion/adjudicacion/veredictos_definitivos_ciego.json`). El criterio i de la ficha es el `indice` i del juez
(el armado de las fichas los numera en el orden del gold, `armar_fichas_gold_q12_mesa.py:113-115`).
Uso: python3 -I -B cruce_gold_q12_ajuste_mesa.py <carpeta con las planillas de la autora> <clave> <clon del repo> <salida.json>"""
import csv
import json
import math
import sys
from collections import Counter
from pathlib import Path

A, CLAVE, CL, OUT = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]), Path(sys.argv[4])
clave = json.loads(CLAVE.read_text(encoding="utf-8"))["fichas"]
agr = {x["id_opaco"]: x for x in json.loads((CL / "data/experiment/ev2_fidelidad_eval/out/veredictos_agregados_ciego.json")
                                              .read_text(encoding="utf-8"))["agregados"]}
defs = {d["id_opaco_base"]: d for d in json.loads((CL / "data/experiment/ev2_adjudicacion/adjudicacion/veredictos_definitivos_ciego.json")
                                                   .read_text(encoding="utf-8"))["definitivos"]}
crit = list(csv.DictReader(open(A / "planilla_criterios_gold_q12_ajuste.csv", encoding="utf-8")))
resp = {r["ficha"]: r for r in csv.DictReader(open(A / "planilla_respuestas_gold_q12_ajuste.csv", encoding="utf-8"))}
cab = list(crit[0].keys())
VER, DUD, EXP, MAL = cab[2], cab[4], cab[5], cab[6]
CLAS = list(next(iter(resp.values())).keys())[1]
si = lambda x: x.strip() in ("si", "sí")  # noqa: E731
ORD = {"incorrecto": 0, "parcial": 1, "correcto": 2}


def wilson(k, n, z=1.959964):
    if n == 0:
        return None
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    r = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return [round((c - r) / d, 4), round((c + r) / d, 4)]


def veredicto(marcas):
    if all(m == "cumplido" for m in marcas):
        return "correcto"
    if all(m == "no_cumplido" for m in marcas):
        return "incorrecto"
    return "parcial"


pares, respuestas = [], []
for f in clave:
    a = agr[f["id_opaco"]]
    assert a["n_criterios"] == f["n_criterios"] == len(a["modales"]), f["ficha"]
    assert [c["indice"] for c in a["criterios"]] == list(range(1, f["n_criterios"] + 1)), f["ficha"]
    mias = [c for c in crit if c["ficha"] == f["ficha"]]
    assert [int(c["criterio"]) for c in mias] == list(range(1, f["n_criterios"] + 1)), f["ficha"]
    for c, j in zip(mias, a["modales"]):
        pares.append({"par": f"{f['ficha']}-{c['criterio']}", "ficha": f["ficha"], "juez": j, "autora": c[VER],
                      "dudosa": si(c[DUD]), "experto": si(c[EXP]), "mal_planteado": si(c[MAL])})
    va = veredicto([c[VER] for c in mias])
    cl_a = resp[f["ficha"]][CLAS].replace("abstención", "abstencion")
    respuestas.append({"ficha": f["ficha"], "juez": a["veredicto_pregunta"], "autora": va, "clas_juez": a["clasificacion_respuesta_modal"],
                       "clas_autora": cl_a, "via": defs[f["id_opaco"]]["via"], "grafo": f["grafo"], "to": f["to"]})


def cifras_criterio(ps):
    n = len(ps)
    acu = [p for p in ps if p["juez"] == p["autora"]]
    dud = [p for p in ps if p["juez"] in ("dudoso", "sin_consenso")]
    A_ = [p["par"] for p in ps if p["juez"] == "cumplido" and p["autora"] == "no_cumplido"]
    B_ = [p["par"] for p in ps if p["juez"] == "no_cumplido" and p["autora"] == "cumplido"]
    sin_d = [p for p in ps if p not in dud]
    k2 = sum(p["juez"] == p["autora"] for p in sin_d)
    return {"n": n, "acuerdo": len(acu), "fraccion": round(len(acu) / n, 4) if n else None, "wilson95": wilson(len(acu), n),
            "direccion_A_juez_acredita": len(A_), "pares_A": A_, "direccion_B_juez_no_acredita": len(B_), "pares_B": B_,
            "dudoso_del_juez": len(dud), "pares_dudoso_del_juez": [p["par"] for p in dud],
            "sin_dudosos_del_juez": {"n": len(sin_d), "acuerdo": k2, "fraccion": round(k2 / len(sin_d), 4) if sin_d else None,
                                     "wilson95": wilson(k2, len(sin_d))}}


def cifras_respuesta(rs):
    n = len(rs)
    acu = sum(r["juez"] == r["autora"] for r in rs)
    adj = [r["ficha"] for r in rs if r["juez"] == "requiere_adjudicacion"]
    A_ = [r["ficha"] for r in rs if r["juez"] in ORD and ORD[r["juez"]] > ORD[r["autora"]]]
    B_ = [r["ficha"] for r in rs if r["juez"] in ORD and ORD[r["juez"]] < ORD[r["autora"]]]
    sin = [r for r in rs if r["juez"] != "requiere_adjudicacion"]
    k2 = sum(r["juez"] == r["autora"] for r in sin)
    return {"n": n, "acuerdo": acu, "fraccion": round(acu / n, 4) if n else None, "wilson95": wilson(acu, n),
            "direccion_A_juez_mas_favorable": len(A_), "fichas_A": A_, "direccion_B_juez_menos_favorable": len(B_), "fichas_B": B_,
            "requiere_adjudicacion": len(adj), "fichas_requiere_adjudicacion": adj,
            "sin_requiere_adjudicacion": {"n": len(sin), "acuerdo": k2, "fraccion": round(k2 / len(sin), 4) if sin else None}}


adj_base = {r["ficha"] for r in respuestas if r["via"] == "adjudicacion_base"}
s7 = sorted(r["ficha"] for r in respuestas if r["via"] == "adjudicacion_s7")
sin_marcas = [p for p in pares if not p["experto"] and not p["mal_planteado"]]
out = {
 "criterio": {"principal_82": cifras_criterio(pares), "sin_experto_ni_mal_planteado": cifras_criterio(sin_marcas),
              "sin_adjudicacion_base": cifras_criterio([p for p in pares if p["ficha"] not in adj_base])},
 "respuesta": {"principal_20": cifras_respuesta(respuestas),
               "sin_adjudicacion_base": cifras_respuesta([r for r in respuestas if r["ficha"] not in adj_base])},
 "clasificacion_abstencion_contenido": {"n": 20, "acuerdo": sum(r["clas_juez"] == r["clas_autora"] for r in respuestas),
                                        "desacuerdos": [r["ficha"] for r in respuestas if r["clas_juez"] != r["clas_autora"]]},
 "via_en_EV2": {"por_via": dict(Counter(r["via"] for r in respuestas)), "adjudicacion_base": sorted(adj_base), "adjudicacion_s7_aparte": s7},
 "marcas_de_la_autora": {"dudosa": [p["par"] for p in pares if p["dudosa"]], "experto": [p["par"] for p in pares if p["experto"]],
                         "mal_planteado": [p["par"] for p in pares if p["mal_planteado"]]},
 "veredictos_de_la_autora_por_respuesta": dict(Counter(r["autora"] for r in respuestas)),
 "veredictos_del_juez_por_respuesta": dict(Counter(r["juez"] for r in respuestas)),
 "modales_del_juez_por_criterio": dict(Counter(p["juez"] for p in pares)),
 "pares": pares, "respuestas": respuestas,
}
OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
c, r = out["criterio"], out["respuesta"]
print(f"por criterio (82): {c['principal_82']['acuerdo']} de {c['principal_82']['n']} ({c['principal_82']['wilson95']}); "
      f"A {c['principal_82']['direccion_A_juez_acredita']}, B {c['principal_82']['direccion_B_juez_no_acredita']}, "
      f"dudoso del juez {c['principal_82']['dudoso_del_juez']}; sin dudosos {c['principal_82']['sin_dudosos_del_juez']['acuerdo']} de "
      f"{c['principal_82']['sin_dudosos_del_juez']['n']}")
print(f"  sin experto ni mal planteado: {c['sin_experto_ni_mal_planteado']['acuerdo']} de {c['sin_experto_ni_mal_planteado']['n']}; "
      f"sin adjudicacion_base: {c['sin_adjudicacion_base']['acuerdo']} de {c['sin_adjudicacion_base']['n']}")
print(f"por respuesta (20): {r['principal_20']['acuerdo']} de 20; A {r['principal_20']['direccion_A_juez_mas_favorable']}, "
      f"B {r['principal_20']['direccion_B_juez_menos_favorable']}, requiere adjudicación {r['principal_20']['requiere_adjudicacion']}; "
      f"sin adjudicacion_base: {r['sin_adjudicacion_base']['acuerdo']} de {r['sin_adjudicacion_base']['n']}")
print(f"abstención o contenido: {out['clasificacion_abstencion_contenido']['acuerdo']} de 20; vías: {out['via_en_EV2']['por_via']}")
