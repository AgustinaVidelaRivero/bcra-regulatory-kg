"""
tests_cerrar.py — Tests de respuesta conocida de cerrar_adjudicacion.cerrar sobre
casos SINTÉTICOS (ninguna respuesta ni veredicto real). Offline.

Uso: .venv/bin/python -B data/experiment/ev2_adjudicacion/code/tests_cerrar.py
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun_adj as ca              # noqa: E402
import cerrar_adjudicacion as cz    # noqa: E402

ADJ = ca.ADJ
FALLOS = []
N = 0


def check(nombre, cond, detalle=""):
    global N
    N += 1
    if cond:
        print(f"  ok  {nombre}")
    else:
        FALLOS.append(nombre)
        print(f"  FALLO {nombre} {detalle}")


def ficha_tabla(fid, idb, origen, grafo, final, resp, modales, fuente="base", reps=None, ids_reps=None):
    """Una fila de tabla SOLO_MESA sintética; resp = lista de (id_resp, rep, veredicto_juez)."""
    return {"n": 0, "id_ficha": fid, "id_pregunta": "Q-" + idb, "sha256_respuesta": ca.sha256_texto("R:" + fid),
            "n_criterios": len(modales), "origen": origen, "grafo": grafo, "id_opaco_base": idb,
            "final_juez_par": final, "fuente_final": fuente, "veredictos_reps": reps, "ids_reps": ids_reps,
            "respuestas": [{"id_opaco_respuesta": i, "rep": r, "origen_respuesta": "enc" if r else "base",
                            "veredicto_juez_respuesta": v, "modales_juez": modales} for i, r, v in resp]}


def ficha_ws(fid, marcas):
    return {"n": 0, "id_ficha": fid, "pregunta": "?", "respuesta": "R:" + fid,
            "criterios": [{"indice": j, "criterio": "c", "cita_textual": "q", "veredicto": m}
                          for j, m in enumerate(marcas, start=1)], "observaciones": None}


def final(idb, grafo, fin, re_corrido=False, reps=None, ids_reps=None):
    return {"id_opaco_base": idb, "id_pregunta": "Q-" + idb, "grafo": grafo, "final": fin,
            "fuente_final": "enc" if re_corrido else "base", "re_corrido": re_corrido,
            "veredictos_reps": reps, "ids_reps": ids_reps}


def escenario():
    """Población sintética:
      P1 heredado (base ADJ), 3 criterios, juez modales [cumplido, dudoso, no_cumplido]
      P2 heredado incompleto
      P3 pendiente §7 votos [correcto, incorrecto, ADJ]; una ficha F3
      P4 pendiente §7 votos [ADJ, parcial, ADJ]; r1 y r3 texto idéntico → UNA ficha F4 cubre ambas
      P5 pendiente §7 votos [ADJ, ADJ, parcial]; dos fichas F5a (r1), F5b (r2), F5b sin adjudicar
      P6 muestra correcto (juez correcto), humana no_cumplido en 1 → parcial (error dirección A)
      P7 muestra p+i (juez incorrecto), humana todo cumplido → correcto (error dirección B)
      P8 muestra p+i (juez parcial), humana incorrecto (desacuerdo de grado)
      P9 muestra p+i (juez parcial), humana parcial (acuerdo)
      P10 par decidido por el juez, sin ficha
    """
    tabla = {"fichas": [
        ficha_tabla("F1", "P1", "heredado_base", "v2", ADJ, [("B1", None, ADJ)], ["cumplido", "dudoso", "no_cumplido"]),
        ficha_tabla("F2", "P2", "heredado_base", "v3", ADJ, [("B2", None, ADJ)], ["dudoso", "cumplido"]),
        ficha_tabla("F3", "P3", "s7_pendiente", "v2", ADJ, [("E3c", 3, ADJ)], ["cumplido", "dudoso"], "enc",
                    ["correcto", "incorrecto", ADJ], ["E3a", "E3b", "E3c"]),
        ficha_tabla("F4", "P4", "s7_pendiente", "run_3", ADJ, [("E4a", 1, ADJ), ("E4c", 3, ADJ)], ["dudoso", "no_cumplido"],
                    "enc", [ADJ, "parcial", ADJ], ["E4a", "E4b", "E4c"]),
        ficha_tabla("F5a", "P5", "s7_pendiente", "v3", ADJ, [("E5a", 1, ADJ)], ["dudoso", "cumplido"], "enc",
                    [ADJ, ADJ, "parcial"], ["E5a", "E5b", "E5c"]),
        ficha_tabla("F5b", "P5", "s7_pendiente", "v3", ADJ, [("E5b", 2, ADJ)], ["cumplido", "dudoso"], "enc",
                    [ADJ, ADJ, "parcial"], ["E5a", "E5b", "E5c"]),
        ficha_tabla("F6", "P6", "muestra_correcto", "v2", "correcto", [("B6", None, "correcto")], ["cumplido", "cumplido"]),
        ficha_tabla("F7", "P7", "muestra_parcial_incorrecto", "v3", "incorrecto", [("B7", None, "incorrecto")],
                    ["no_cumplido", "no_cumplido"]),
        ficha_tabla("F8", "P8", "muestra_parcial_incorrecto", "run_3", "parcial", [("E8b", 2, "parcial")],
                    ["cumplido", "no_cumplido"], "enc", ["incorrecto", "parcial", "parcial"], ["E8a", "E8b", "E8c"]),
        ficha_tabla("F9", "P9", "muestra_parcial_incorrecto", "run_3", "parcial", [("B9", None, "parcial")],
                    ["cumplido", "no_cumplido", "no_cumplido"]),
    ]}
    finales = [
        final("P1", "v2", ADJ), final("P2", "v3", ADJ),
        final("P3", "v2", ADJ, True, ["correcto", "incorrecto", ADJ], ["E3a", "E3b", "E3c"]),
        final("P4", "run_3", ADJ, True, [ADJ, "parcial", ADJ], ["E4a", "E4b", "E4c"]),
        final("P5", "v3", ADJ, True, [ADJ, ADJ, "parcial"], ["E5a", "E5b", "E5c"]),
        final("P6", "v2", "correcto"), final("P7", "v3", "incorrecto"),
        final("P8", "run_3", "parcial", True, ["incorrecto", "parcial", "parcial"], ["E8a", "E8b", "E8c"]),
        final("P9", "run_3", "parcial"), final("P10", "v2", "parcial"),
    ]
    ws = {"fichas": [
        ficha_ws("F1", ["cumplido", "no_cumplido", "no_cumplido"]),      # → parcial
        ficha_ws("F2", ["cumplido", None]),                               # incompleta
        ficha_ws("F3", ["cumplido", "no_cumplido"]),                      # parcial → votos corr/inco/parc → parcial (mediana)
        ficha_ws("F4", ["no_cumplido", "no_cumplido"]),                   # incorrecto → inco/parc/inco → incorrecto
        ficha_ws("F5a", ["cumplido", "cumplido"]),                        # correcto → corr/ADJ/parc → depende → ADJ
        ficha_ws("F5b", [None, None]),                                    # sin adjudicar
        ficha_ws("F6", ["cumplido", "no_cumplido"]),                      # parcial ≠ juez correcto (dirección A)
        ficha_ws("F7", ["cumplido", "cumplido"]),                         # correcto ≠ juez incorrecto (dirección B)
        ficha_ws("F8", ["no_cumplido", "no_cumplido"]),                   # incorrecto ≠ juez parcial (grado)
        ficha_ws("F9", ["cumplido", "no_cumplido", "no_cumplido"]),       # parcial = juez parcial
    ]}
    return ws, tabla, finales


def main():
    print("== escenario principal")
    ws, tabla, finales = escenario()
    res = cz.cerrar(ws, tabla, finales)
    d = {x["id_opaco_base"]: x for x in res["definitivos"]}
    check("P1 heredado → parcial por mapping", d["P1"]["definitivo"] == "parcial" and d["P1"]["via"] == "adjudicacion_base")
    check("P2 heredado incompleto → ADJ", d["P2"]["definitivo"] == ADJ and not d["P2"]["completo"])
    check("P3 corr/inco/ADJ→parcial resuelto → parcial (mediana)", d["P3"]["definitivo"] == "parcial"
          and d["P3"]["votos_resueltos"] == ["correcto", "incorrecto", "parcial"])
    check("P4 una ficha cubre r1 y r3 → inco/parc/inco → incorrecto", d["P4"]["definitivo"] == "incorrecto"
          and d["P4"]["votos_resueltos"] == ["incorrecto", "parcial", "incorrecto"] and len(d["P4"]["resoluciones"]) == 2)
    check("P5 corr/ADJ/parc (F5b sin adjudicar) → sigue ADJ, incompleto", d["P5"]["definitivo"] == ADJ
          and d["P5"]["via"] == "adjudicacion_s7_incompleta" and d["P5"]["respuestas_sin_adjudicar"] == ["E5b"])
    check("P6-P9 muestra: definitivo = juez (no reemplaza)", all(d[p]["definitivo"] == d[p]["final_juez"] and
                                                              d[p]["via"].startswith("juez_") for p in ("P6", "P7", "P8", "P9")))
    check("P10 sin ficha → juez", d["P10"]["definitivo"] == "parcial" and d["P10"]["fichas"] == [])
    check("pares incompletos = P2, P5", res["pares_incompletos"] == ["P2", "P5"])
    check("fichas incompletas = F2, F5b", res["fichas_incompletas"] == ["F2", "F5b"])
    check("distribución definitiva", res["distribucion_definitivos"] ==
          {"parcial": 5, ADJ: 2, "incorrecto": 2, "correcto": 1}, res["distribucion_definitivos"])
    m = res["muestra_resumen"]
    check("muestra n=4 adjudicadas 4", m["n_muestra"] == 4 and m["n_adjudicadas"] == 4)
    check("dirección A: 1/1", m["direccion_A_sobre_acreditacion"] == {"n_juez_correcto": 1, "errores": 1, "tasa": 1.0})
    check("dirección B: 1/3", m["direccion_B_sub_acreditacion"]["errores"] == 1
          and m["direccion_B_sub_acreditacion"]["n_juez_parcial_incorrecto"] == 3
          and abs(m["direccion_B_sub_acreditacion"]["tasa"] - 1 / 3) < 1e-9)
    check("desacuerdo de grado 1", m["desacuerdo_de_grado_parcial_incorrecto"] == 1)
    check("acuerdo exacto 1/4", m["acuerdo_exacto"] == 1)
    check("matriz", m["matriz_juez_x_humano"] == {"correcto": {"parcial": 1}, "incorrecto": {"correcto": 1},
                                                  "parcial": {"incorrecto": 1, "parcial": 1}}, m["matriz_juez_x_humano"])
    # acuerdo por criterio: F6 1/2, F7 0/2, F8 1/2, F9 3/3 → 5/9
    check("acuerdo por criterio 5/9", m["acuerdo_por_criterio"] == {"n_criterios": 9, "en_acuerdo": 5, "tasa": 5 / 9},
          m["acuerdo_por_criterio"])
    # dudosos resueltos: F1 C2 dudoso→no_cumplido; F3 C2 dudoso→no_cumplido; F4 C1 dudoso→no_cumplido; F5a C1 dudoso→cumplido
    check("dudosos resueltos", res["resueltos_dudosos"] == {"no_cumplido": 3, "cumplido": 1}, res["resueltos_dudosos"])
    check("cruce por grafo v2", res["cruce_por_grafo"]["v2"] == {"correcto": 1, "parcial": 3, "incorrecto": 0, ADJ: 0},
          res["cruce_por_grafo"]["v2"])
    check("cruce por grafo v3", res["cruce_por_grafo"]["v3"] == {"correcto": 0, "parcial": 0, "incorrecto": 1, ADJ: 2})
    check("cruce por grafo run_3", res["cruce_por_grafo"]["run_3"] == {"correcto": 0, "parcial": 2, "incorrecto": 1, ADJ: 0})
    check("muestra por grafo run_3 2/1", res["cruce_muestra_por_grafo"]["run_3"] == {"n": 2, "coinciden": 1, "sin_adjudicar": 0})

    print("== variante: P5 completada → corr/parc/parc → parcial")
    ws2 = {"fichas": [f if f["id_ficha"] != "F5b" else ficha_ws("F5b", ["cumplido", "no_cumplido"]) for f in ws["fichas"]]}
    r2 = cz.cerrar(ws2, tabla, finales)
    d2 = {x["id_opaco_base"]: x for x in r2["definitivos"]}
    check("P5 → parcial completo", d2["P5"]["definitivo"] == "parcial" and d2["P5"]["via"] == "adjudicacion_s7"
          and d2["P5"]["votos_resueltos"] == ["correcto", "parcial", "parcial"])

    print("== variante: invariancia con faltante (P5: F5a=parcial, F5b sin adjudicar → parc/ADJ/parc → parcial)")
    ws3 = {"fichas": [f if f["id_ficha"] != "F5a" else ficha_ws("F5a", ["cumplido", "no_cumplido"]) for f in ws["fichas"]]}
    r3 = cz.cerrar(ws3, tabla, finales)
    d3 = {x["id_opaco_base"]: x for x in r3["definitivos"]}
    check("P5 invariante con faltante → parcial", d3["P5"]["definitivo"] == "parcial"
          and d3["P5"]["via"] == "adjudicacion_s7_invariante_con_faltante" and d3["P5"]["completo"])

    print("== errores de validación")
    def levanta(nombre, wsx):
        try:
            cz.cerrar(wsx, tabla, finales)
            check(nombre, False, "no levantó")
        except ValueError as e:
            check(nombre, True, str(e))
    levanta("marca inválida levanta", {"fichas": [f if f["id_ficha"] != "F1" else ficha_ws("F1", ["cumplido", "dudoso", "no_cumplido"])
                                                  for f in ws["fichas"]]})
    levanta("ficha desconocida levanta", {"fichas": ws["fichas"] + [ficha_ws("FX", ["cumplido"])]})
    levanta("ficha faltante levanta", {"fichas": ws["fichas"][1:]})
    levanta("respuesta alterada levanta", {"fichas": [dict(f, respuesta="otra") if f["id_ficha"] == "F1" else f
                                                      for f in ws["fichas"]]})
    levanta("n criterios distinto levanta", {"fichas": [f if f["id_ficha"] != "F1" else ficha_ws("F1", ["cumplido"])
                                                        for f in ws["fichas"]]})
    levanta("ficha repetida levanta", {"fichas": ws["fichas"] + [ws["fichas"][0]]})
    # marcas con mayúsculas / espacios se normalizan
    r4 = cz.cerrar({"fichas": [f if f["id_ficha"] != "F1" else ficha_ws("F1", [" Cumplido", "NO_CUMPLIDO ", "no_cumplido"])
                               for f in ws["fichas"]]}, tabla, finales)
    check("marcas normalizadas", {x["id_opaco_base"]: x for x in r4["definitivos"]}["P1"]["definitivo"] == "parcial")

    print(f"\n{N - len(FALLOS)}/{N} checks ok; fallos: {FALLOS}")
    sys.exit(1 if FALLOS else 0)


if __name__ == "__main__":
    main()
