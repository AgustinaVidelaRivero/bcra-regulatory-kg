"""
construir_worksheet.py — Construye el worksheet CIEGO de adjudicación humana de
EV2 (adjudicacion/) y la tabla ficha → par (adjudicacion_SOLO_MESA/).
Offline, USD 0. Ver docstring de comun_adj.py.

Salidas:
  adjudicacion/worksheet_adjudicacion.json   fichas ciegas + espacio de marcas (a completar)
  adjudicacion/worksheet_adjudicacion.md     vista de lectura del mismo contenido
  adjudicacion/censo_worksheet_ciego.md      conteos sin grafo
  adjudicacion_SOLO_MESA/tabla_fichas_SOLO_MESA.json          ficha → (par, respuesta, origen, juez)
  adjudicacion_SOLO_MESA/poblacion_adjudicacion_SOLO_MESA.json  finales por par, población A, muestra B, verificación de esperados
  adjudicacion_SOLO_MESA/resumen_poblacion_SOLO_MESA.md

Si las salidas ya existen y difieren de lo recomputado, levanta (el worksheet
es único por sesión; se regenera solo borrando a mano).

Uso:
  .venv/bin/python -B data/experiment/ev2_adjudicacion/code/construir_worksheet.py [--forzar]
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import datetime
from pathlib import Path

import comun_adj as ca


def verificacion_esperados(res: dict) -> dict:
    tabla = res["tabla_final"]
    her, pen = res["pobA"]["heredados"], res["pobA"]["pendientes_s7"]
    votos_adj_pen = sum(len(x["objetivos"]) for x in pen)
    fichas_pen = sum(1 for f in res["fichas_mesa"] if f["origen"] == "s7_pendiente")
    # votos ADJ en TODAS las respuestas del §7 (incluye pares decididos por invariancia)
    votos_adj_total_s7 = sum(1 for x in res["fin"] if x["re_corrido"]
                             for v in x["veredictos_reps"] if v == ca.ADJ)
    votos_adj_invariantes = votos_adj_total_s7 - votos_adj_pen
    mc = {g: res["muestra"]["detalle_estratos"][g]["k_correcto"] for g in ca.GRAFOS}
    mpi = {g: res["muestra"]["detalle_estratos"][g]["k_parcial_incorrecto"] for g in ca.GRAFOS}
    adj_por_grafo = {g: tabla[g][ca.ADJ] for g in ca.GRAFOS}
    her_por_grafo = dict(Counter(x["grafo"] for x in her))
    pen_por_grafo = dict(Counter(x["grafo"] for x in pen))
    return {
        "tabla_final_por_grafo": tabla,
        "tabla_final_esperada": ca.ESPERADO_FINAL_POR_GRAFO,
        "tabla_final_ok": tabla == ca.ESPERADO_FINAL_POR_GRAFO,
        "pares_adj_por_grafo": adj_por_grafo,
        "pares_adj_esperado_por_grafo": {"v2": 10, "v3": 12, "run_3": 8},
        "n_heredados": len(her), "n_heredados_esperado": ca.ESPERADO_HEREDADOS,
        "heredados_por_grafo": her_por_grafo,
        "n_pendientes_s7": len(pen), "n_pendientes_s7_esperado": ca.ESPERADO_PENDIENTES_S7,
        "pendientes_s7_por_grafo": pen_por_grafo,
        "votos_adj_en_pendientes_s7": votos_adj_pen,
        "votos_adj_en_pendientes_s7_esperado_mandato": ca.ESPERADO_VOTOS_ADJ_S7,
        "votos_adj_en_pares_invariantes_s7": votos_adj_invariantes,
        "votos_adj_total_respuestas_s7": votos_adj_total_s7,
        "fichas_s7_pendiente": fichas_pen,
        "textos_identicos_colapsados_s7": votos_adj_pen - fichas_pen,
        "muestra_correcto_por_grafo": mc, "muestra_correcto_esperado": ca.ESPERADO_MUESTRA_CORRECTO,
        "muestra_parcial_incorrecto_por_grafo": mpi, "muestra_pi_esperado": ca.ESPERADO_MUESTRA_PI,
        "muestra_ok": mc == ca.ESPERADO_MUESTRA_CORRECTO and mpi == ca.ESPERADO_MUESTRA_PI,
        "n_fichas": len(res["fichas_mesa"]),
        "fichas_por_origen": dict(Counter(f["origen"] for f in res["fichas_mesa"])),
        "respuestas_cubiertas_por_origen": {o: sum(len(f["respuestas"]) for f in res["fichas_mesa"] if f["origen"] == o)
                                            for o in ca.ORIGENES},
    }


def resumen_md(ver: dict, res: dict) -> str:
    L = ["# Resumen de población — adjudicación EV2 (SOLO_MESA: contiene grafo)\n",
         f"generado: {datetime.now().isoformat(timespec='seconds')}\n",
         "## Tabla final pre-adjudicación por grafo (correcto / parcial / incorrecto / req.adj.)\n",
         "| grafo | correcto | parcial | incorrecto | req.adj. | esperado |", "|---|---|---|---|---|---|"]
    for g in ca.GRAFOS:
        t, e = ver["tabla_final_por_grafo"][g], ver["tabla_final_esperada"][g]
        L.append(f"| {g} | {t['correcto']} | {t['parcial']} | {t['incorrecto']} | {t[ca.ADJ]} | "
                 f"{e['correcto']}/{e['parcial']}/{e['incorrecto']}/{e[ca.ADJ]} |")
    L += [f"\n- tabla_final_ok: **{ver['tabla_final_ok']}**",
          f"- heredados (base, final req.adj.): {ver['n_heredados']} (esperado {ver['n_heredados_esperado']}); "
          f"por grafo {ver['heredados_por_grafo']}",
          f"- pendientes §7: {ver['n_pendientes_s7']} (esperado {ver['n_pendientes_s7_esperado']}); "
          f"por grafo {ver['pendientes_s7_por_grafo']}",
          f"- votos requiere_adjudicacion dentro de los 9 pendientes: **{ver['votos_adj_en_pendientes_s7']}** "
          f"(mandato esperaba {ver['votos_adj_en_pendientes_s7_esperado_mandato']}); "
          f"en pares decididos por invariancia: {ver['votos_adj_en_pares_invariantes_s7']}; "
          f"total de respuestas §7 con veredicto req.adj.: {ver['votos_adj_total_respuestas_s7']}",
          f"- fichas s7_pendiente: {ver['fichas_s7_pendiente']} (textos idénticos colapsados: "
          f"{ver['textos_identicos_colapsados_s7']})",
          f"- muestra correcto por grafo: {ver['muestra_correcto_por_grafo']} (esperado {ver['muestra_correcto_esperado']})",
          f"- muestra parcial+incorrecto por grafo: {ver['muestra_parcial_incorrecto_por_grafo']} "
          f"(esperado {ver['muestra_pi_esperado']}); muestra_ok: **{ver['muestra_ok']}**",
          f"- fichas: {ver['n_fichas']}; por origen {ver['fichas_por_origen']}; "
          f"respuestas cubiertas {ver['respuestas_cubiertas_por_origen']}",
          "\n## Pendientes §7 (votos r1/r2/r3 y respuestas a adjudicar)\n",
          "| id_pregunta | grafo | id_opaco_base | votos | ids ADJ | fichas |", "|---|---|---|---|---|---|"]
    for x in res["pobA"]["pendientes_s7"]:
        fichas = sorted({f["id_ficha"] for f in res["fichas_mesa"] if f["id_opaco_base"] == x["id_opaco_base"]})
        L.append(f"| {x['id_pregunta']} | {x['grafo']} | {x['id_opaco_base']} | {'/'.join(x['veredictos_reps'])} | "
                 f"{', '.join(o['id_opaco_respuesta'] + ' (r' + str(o['rep']) + ')' for o in x['objetivos'])} | "
                 f"{', '.join(fichas)} |")
    L += ["\n## Muestra simétrica §6\n", "| grafo | estrato | id_pregunta | final juez | fuente | respuesta en ficha |",
          "|---|---|---|---|---|---|"]
    for est in ("correcto", "parcial_incorrecto"):
        for x in res["muestra"][est]:
            o = x["objetivos"][0]
            L.append(f"| {x['grafo']} | {est} | {x['id_pregunta']} | {x['final']} | {x['fuente_final']} | "
                     f"{o['id_opaco_respuesta']}" + (f" (r{o['rep']})" if o["rep"] else " (base)") + " |")
    L += ["\n## Heredados (base, final req.adj.)\n", "| grafo | id_pregunta | id_opaco_base | ficha |", "|---|---|---|---|"]
    for x in res["pobA"]["heredados"]:
        f = next(f for f in res["fichas_mesa"] if f["id_opaco_base"] == x["id_opaco_base"])
        L.append(f"| {x['grafo']} | {x['id_pregunta']} | {x['id_opaco_base']} | {f['id_ficha']} |")
    return "\n".join(L) + "\n"


def escribir(p: Path, contenido: str, forzar: bool):
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.exists() and not forzar and p.read_text(encoding="utf-8") != contenido:
        raise RuntimeError(f"{p} ya existe y difiere de lo recomputado (usar --forzar para regenerar)")
    p.write_text(contenido, encoding="utf-8")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--forzar", action="store_true")
    a = ap.parse_args()

    ins = ca.cargar_insumos()
    res = ca.construir_fichas(ins)
    ver = verificacion_esperados(res)

    ws = ca.worksheet_json(res["worksheet"])
    md = ca.render_md(res["worksheet"])
    # los archivos ciegos no llevan sellos ni fechas (nada que permita cruzar)
    txt_json = json.dumps(ws, ensure_ascii=False, indent=2)
    fugas = ca.buscar_marcadores(txt_json) + ca.buscar_marcadores(md)
    if fugas:
        raise RuntimeError(f"marcadores prohibidos en el worksheet: {fugas}")

    escribir(ca.WORKSHEET_JSON, txt_json + "\n", a.forzar)
    escribir(ca.WORKSHEET_MD, md, a.forzar)
    escribir(ca.CENSO_CIEGO, ca.censo_ciego(res), a.forzar)

    tabla = {"SOLO_MESA": True, "semilla_orden": ca.SEMILLA_WORKSHEET, "semilla_muestra": ca.SEMILLA_MUESTRA,
             "sal_id_ficha": ca.SAL_ID_FICHA,
             "regla_id_ficha": "id_ficha = 'ADJ-' + sha256(sal|id_pregunta|sha256(respuesta))[:8]",
             "regla_ficha": "una ficha por (id_pregunta, sha256 respuesta) distinta; textos idénticos "
                            "de re-corridas de un mismo par comparten ficha",
             "sellos_insumos": ca.sellos_insumos(), "n_fichas": len(res["fichas_mesa"]),
             "fichas": res["fichas_mesa"]}
    pob = {"SOLO_MESA": True, "generado": datetime.now().isoformat(timespec="seconds"),
           "sellos_insumos": ca.sellos_insumos(), "verificacion_esperados": ver,
           "regla_final": "par re-corrido en §7 → agregar_par(votos re-corridas); resto → veredicto base",
           "regla_muestra": (f"por grafo y estrato, ids de pregunta ORDENADOS, "
                             f"random.Random('{ca.SEMILLA_MUESTRA}').sample(ids, ceil({ca.FRACCION_MUESTRA}·n)); "
                             "generador nuevo por (grafo, estrato)"),
           "regla_respuesta_muestra": ("par re-corrido → re-corrida de menor rep con veredicto == final; "
                                       "par no re-corrido → respuesta base"),
           "finales_por_par": res["fin"],
           "muestra_detalle_estratos": res["muestra"]["detalle_estratos"],
           "heredados": [{k: v for k, v in x.items()} for x in res["pobA"]["heredados"]],
           "pendientes_s7": res["pobA"]["pendientes_s7"],
           "muestra_correcto": res["muestra"]["correcto"],
           "muestra_parcial_incorrecto": res["muestra"]["parcial_incorrecto"]}
    escribir(ca.TABLA_FICHAS, json.dumps(tabla, ensure_ascii=False, indent=2) + "\n", True)
    escribir(ca.POBLACION_SM, json.dumps(pob, ensure_ascii=False, indent=2) + "\n", True)
    escribir(ca.RESUMEN_SM, resumen_md(ver, res), True)

    print(json.dumps({k: v for k, v in ver.items() if k not in ("tabla_final_esperada",)},
                     ensure_ascii=False, indent=1))
    print("escritos:", ca.rel_repo(ca.WORKSHEET_JSON), ca.rel_repo(ca.WORKSHEET_MD), ca.rel_repo(ca.CENSO_CIEGO),
          ca.rel_repo(ca.TABLA_FICHAS), ca.rel_repo(ca.POBLACION_SM), ca.rel_repo(ca.RESUMEN_SM))


if __name__ == "__main__":
    main()
