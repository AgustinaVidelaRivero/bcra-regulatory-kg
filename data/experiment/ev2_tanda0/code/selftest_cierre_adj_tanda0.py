"""
selftest_cierre_adj_tanda0.py — Selftest del cierre de la adjudicación de C2 a
C5 (anexo E5.c de U-TANDA0-2A, E5.c.1 d) con marcas SINTÉTICAS. USD 0, sin API,
sin escrituras: no toca las planillas reales ni sus CSV de marcas. Molde:
ev2_adjudicacion/code/tests_cerrar.py (03ebe83).

  1. Escenario sintético de cuatro celdas: heredado, pendiente del §7 con una
     ficha compartida por dos re-corridas, pendiente con mediana, finales del
     juez que no se tocan, muestra B que no reemplaza veredictos, y la misma
     pregunta en dos celdas con fichas distintas (reparto por celda).
  2. Tasa de error del juez por celda y agregada para C2 a C4, con C5 aparte.
  3. Validación de los CSV: encabezado, marca vacía, fuera de dominio,
     repetida, faltante, ajena, índice no entero, columnas de más o de menos;
     normalización de mayúsculas y espacios.
  4. Faltas que levantan: heredado o voto requiere_adjudicacion sin ficha.
  5. Wilson al 95 % contra valores publicados en E5; determinismo; verificación
     contra un commit con un lector simulado.
  7. Re-derivación previa al cierre (agregado en E5.c.3): planillas, censo y
     SOLO_MESA se comparan con su re-derivación; los CSV de marcas no, porque
     ya llevan las marcas y se verifican contra su commit.
  6. De punta a punta sobre las planillas reales, en memoria, con marcas
     sintéticas (todas cumplido, todas no_cumplido): ningún par queda en
     requiere_adjudicacion y ningún archivo se escribe. Solo se publican
     resultados PASS/FAIL, nunca conteos por celda.

Uso:  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/ev2_tanda0/code/selftest_cierre_adj_tanda0.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import cierre_adj_tanda0 as cz             # noqa: E402
pt = cz.pt
ADJ = cz.ADJ
C1 = {"correcto": 6, "parcial": 26, "incorrecto": 8}

_checks: list[tuple[str, bool]] = []


def check(nombre: str, cond) -> None:
    _checks.append((nombre, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {nombre}")


def levanta(fn, *args) -> bool:
    try:
        fn(*args)
    except (ValueError, RuntimeError, AssertionError):
        return True
    return False


# --------------------------------------------------------------------------- #
# Escenario sintético                                                          #
# --------------------------------------------------------------------------- #
def par(q, idb, final, re_corrido=False, votos=None, ids=None):
    return {"id_pregunta": q, "id_opaco_base": idb, "final": final, "re_corrido": re_corrido,
            "fuente_final": "s7" if re_corrido else "base", "tipo_enc": "parcial_disparado" if re_corrido else None,
            "veredictos_reps": votos, "ids_reps": ids}


def ficha(fid, celda, planilla, origen, final, resp, modales):
    """resp = lista de (id_opaco_respuesta, rep)."""
    return {"id_ficha": fid, "celda": celda, "planilla": planilla, "origen": origen,
            "n_criterios": len(modales), "final_juez_par": final,
            "respuestas": [{"id_opaco_respuesta": i, "rep": r, "modales_juez": modales,
                            "veredicto_juez_respuesta": final if origen.startswith("muestra_") else ADJ}
                           for i, r in resp]}


def escenario():
    M, P5 = "planilla_mezclada", "planilla_c5"
    fin = {
        "C2": [par("P1", "B-P1", ADJ),
               par("P2", "B-P2", ADJ, True, [ADJ, "parcial", ADJ], ["E2a", "E2b", "E2c"]),
               par("P3", "B-P3", "correcto"),
               par("P4", "B-P4", "correcto"),
               par("P5", "B-P5", "parcial", True, ["parcial", "parcial", "incorrecto"], ["E5a", "E5b", "E5c"]),
               par("QX", "B-QX2", ADJ)],
        "C3": [par("Q1", "B-Q1", ADJ, True, ["correcto", ADJ, "incorrecto"], ["E31a", "E31b", "E31c"]),
               par("Q2", "B-Q2", "incorrecto"),
               par("QX", "B-QX3", ADJ)],
        "C4": [par("R1", "B-R1", "parcial"), par("R2", "B-R2", "parcial")],
        "C5": [par("S1", "B-S1", ADJ), par("S2", "B-S2", "correcto")],
    }
    mesa = {
        M: [ficha("F1", "C2", M, "heredado_base", ADJ, [("B-P1", None)], ["cumplido", "dudoso", "cumplido"]),
            ficha("F2", "C2", M, "s7_pendiente", ADJ, [("E2a", 1), ("E2c", 3)], ["dudoso", "no_cumplido"]),
            ficha("F4", "C2", M, "muestra_correcto", "correcto", [("B-P4", None)], ["cumplido", "cumplido"]),
            ficha("F5", "C2", M, "heredado_base", ADJ, [("B-QX2", None)], ["dudoso", "cumplido"]),
            ficha("F31", "C3", M, "s7_pendiente", ADJ, [("E31b", 2)], ["cumplido", "dudoso"]),
            ficha("F32", "C3", M, "muestra_parcial_incorrecto", "incorrecto", [("B-Q2", None)],
                  ["no_cumplido", "no_cumplido"]),
            ficha("F33", "C3", M, "heredado_base", ADJ, [("B-QX3", None)], ["dudoso", "cumplido"]),
            ficha("F42", "C4", M, "muestra_parcial_incorrecto", "parcial", [("B-R2", None)],
                  ["cumplido", "no_cumplido"])],
        P5: [ficha("F51", "C5", P5, "heredado_base", ADJ, [("B-S1", None)], ["dudoso"]),
             ficha("F52", "C5", P5, "muestra_correcto", "correcto", [("B-S2", None)], ["cumplido", "cumplido"])],
    }
    marcas = {"F1": ["cumplido", "no_cumplido", "cumplido"], "F2": ["no_cumplido", "no_cumplido"],
              "F4": ["cumplido", "no_cumplido"], "F5": ["cumplido", "cumplido"],
              "F31": ["cumplido", "no_cumplido"], "F32": ["cumplido", "cumplido"],
              "F33": ["no_cumplido", "no_cumplido"], "F42": ["cumplido", "no_cumplido"],
              "F51": ["cumplido"], "F52": ["cumplido", "cumplido"]}
    pjs = {nom: {"fichas": [{"id_ficha": f["id_ficha"],
                             "criterios": [{"indice": j} for j in range(1, f["n_criterios"] + 1)]}
                            for f in fs]} for nom, fs in mesa.items()}
    res = {"por_celda": {c: {"fin": v} for c, v in fin.items()},
           "planillas": {nom: {"mesa": fs} for nom, fs in mesa.items()}}
    return res, pjs, marcas


def csv_de(pj: dict, marcas: dict, extra: list[str] | None = None, encabezado: str | None = None) -> str:
    L = [encabezado or ",".join(pt.COLUMNAS_CSV)]
    for f in pj["fichas"]:
        for c in f["criterios"]:
            L.append(f"{f['id_ficha']},{c['indice']},{marcas[f['id_ficha']][c['indice'] - 1]},")
    return "\n".join(L + (extra or [])) + "\n"


def csvs(pjs, marcas):
    return {nom: csv_de(pj, marcas) for nom, pj in pjs.items()}


def main() -> int:
    print("== SELFTEST del cierre de la adjudicación de C2 a C5 (marcas sintéticas, USD 0) ==")
    res, pjs, marcas = escenario()

    print("-- (1) definitivos por celda")
    r = cz.computar(csvs(pjs, marcas), pjs, res, c1=C1)
    d = {c: {x["id_opaco_base"]: x for x in r["solo_mesa"][c]["definitivos"]} for c in r["solo_mesa"]}
    check("heredado → veredicto humano por mapping (parcial), vía adjudicacion_base",
          d["C2"]["B-P1"]["definitivo"] == "parcial" and d["C2"]["B-P1"]["via"] == "adjudicacion_base")
    check("pendiente con una ficha que cubre r1 y r3 → incorrecto/parcial/incorrecto → incorrecto",
          d["C2"]["B-P2"]["definitivo"] == "incorrecto" and d["C2"]["B-P2"]["via"] == "adjudicacion_s7"
          and d["C2"]["B-P2"]["votos_resueltos"] == ["incorrecto", "parcial", "incorrecto"]
          and len(d["C2"]["B-P2"]["resoluciones"]) == 2)
    check("pendiente correcto/ADJ/incorrecto con ficha parcial → mediana parcial",
          d["C3"]["B-Q1"]["definitivo"] == "parcial"
          and d["C3"]["B-Q1"]["votos_resueltos"] == ["correcto", "parcial", "incorrecto"])
    check("finales del juez intactos: juez_base y juez_enc",
          d["C2"]["B-P3"]["via"] == "juez_base" and d["C2"]["B-P5"]["via"] == "juez_enc"
          and d["C2"]["B-P5"]["definitivo"] == "parcial")
    check("muestra B no reemplaza veredictos (definitivo = final del juez)",
          d["C2"]["B-P4"]["definitivo"] == "correcto" and d["C3"]["B-Q2"]["definitivo"] == "incorrecto"
          and d["C4"]["B-R2"]["definitivo"] == "parcial" and d["C5"]["B-S2"]["definitivo"] == "correcto")
    check("reparto por celda: la misma pregunta en dos celdas toma la marca de su propia ficha",
          d["C2"]["B-QX2"]["definitivo"] == "correcto" and d["C3"]["B-QX3"]["definitivo"] == "incorrecto")
    check("tablas definitivas por celda",
          r["celdas"]["C2"]["tabla_definitiva"] == {"correcto": 3, "parcial": 2, "incorrecto": 1}
          and r["celdas"]["C3"]["tabla_definitiva"] == {"correcto": 0, "parcial": 1, "incorrecto": 2}
          and r["celdas"]["C5"]["tabla_definitiva"] == {"correcto": 2, "parcial": 0, "incorrecto": 0})
    check("vías por celda",
          r["celdas"]["C2"]["vias"] == {"juez_base": 2, "juez_enc": 1, "adjudicacion_base": 2, "adjudicacion_s7": 1}
          and r["celdas"]["C3"]["vias"] == {"juez_base": 1, "juez_enc": 0, "adjudicacion_base": 1, "adjudicacion_s7": 1})

    print("-- (2) tasa de error del juez")
    m2, m3, m4 = (r["celdas"][c]["acuerdo_juez_instancia_adjudicadora"] for c in ("C2", "C3", "C4"))
    check("C2: juez correcto, humana parcial → sobre-acreditación 1 y caída de correctos 1/1",
          m2["acuerdo_exacto"] == 0 and m2["sobre_acreditacion_criterios"] == 1
          and m2["flip_descendente_correctos"] == 1 and m2["n_correctos_auditados"] == 1)
    check("C3: juez incorrecto, humana correcto → sub-acreditación 2",
          m3["acuerdo_exacto"] == 0 and m3["sub_acreditacion_criterios"] == 2)
    check("C4: acuerdo exacto y por criterio", m4["acuerdo_exacto"] == 1 and m4["criterios_acuerdo"] == 2)
    ag_ = r["acuerdo_juez_instancia_adjudicadora_agregado_C2_C4"]
    check("agregada C2 a C4: 3 fichas, acuerdo 1/3, criterios 3/6, sobre 1, sub 2, caída 1/1",
          (ag_["n_fichas"], ag_["acuerdo_exacto"], ag_["criterios_acuerdo"], ag_["criterios"],
           ag_["sobre_acreditacion_criterios"], ag_["sub_acreditacion_criterios"],
           ag_["flip_descendente_correctos"], ag_["n_correctos_auditados"]) == (3, 1, 3, 6, 1, 2, 1, 1))
    check("C5 aparte: fuera de la agregada, con su propia tasa",
          r["celdas"]["C5"]["acuerdo_juez_instancia_adjudicadora"]["n_fichas"] == 1
          and r["celdas"]["C5"]["acuerdo_juez_instancia_adjudicadora"]["acuerdo_exacto"] == 1)
    check("reportes sin filas por ficha fuera de solo_mesa",
          all("filas" not in r["celdas"][c]["acuerdo_juez_instancia_adjudicadora"] for c in r["celdas"]) and "filas" not in ag_)

    print("-- (3) validación de los CSV")
    base = csvs(pjs, marcas)
    M = "planilla_mezclada"
    def con(nom, texto):
        return lambda: cz.computar({**base, nom: texto}, pjs, res, C1)
    check("encabezado distinto levanta",
          levanta(con(M, csv_de(pjs[M], marcas, encabezado="id_ficha,indice,marca,observacion"))))
    blanco = dict(marcas, F1=["cumplido", "", "cumplido"])
    check("marca vacía levanta (no se completa)", levanta(con(M, csv_de(pjs[M], blanco))))
    check("marca fuera de dominio levanta",
          levanta(con(M, csv_de(pjs[M], dict(marcas, F1=["cumplido", "dudoso", "cumplido"])))))
    check("marca repetida levanta", levanta(con(M, csv_de(pjs[M], marcas, extra=["F1,1,cumplido,"]))))
    check("marca ajena a la planilla levanta", levanta(con(M, csv_de(pjs[M], marcas, extra=["FX,1,cumplido,"]))))
    check("índice fuera de rango levanta", levanta(con(M, csv_de(pjs[M], marcas, extra=["F1,4,cumplido,"]))))
    faltante = "\n".join(ln for ln in base[M].splitlines() if not ln.startswith("F2,2,")) + "\n"
    check("marca faltante levanta", levanta(con(M, faltante)))
    check("índice no entero levanta", levanta(con(M, csv_de(pjs[M], marcas, extra=["F1,uno,cumplido,"]))))
    check("fila con columnas de menos levanta", levanta(con(M, csv_de(pjs[M], marcas, extra=["F1,1,cumplido"]))))
    norm = dict(marcas, F1=[" Cumplido ", "NO_CUMPLIDO", "cumplido"])
    rn = cz.computar({**base, M: csv_de(pjs[M], norm)}, pjs, res, C1)
    check("marcas con mayúsculas y espacios se normalizan",
          {x["id_opaco_base"]: x for x in rn["solo_mesa"]["C2"]["definitivos"]}["B-P1"]["definitivo"] == "parcial")
    obs = base[M].replace("F1,1,cumplido,", "F1,1,cumplido,texto libre")
    check("observación libre aceptada y contada",
          cz.computar({**base, M: obs}, pjs, res, C1)["n_observaciones_en_marcas"] == 1)

    print("-- (4) faltas que levantan")
    res_sin = json.loads(json.dumps(res))
    res_sin["planillas"][M]["mesa"] = [f for f in res_sin["planillas"][M]["mesa"] if f["id_ficha"] != "F2"]
    pjs_sin = {**pjs, M: {"fichas": [f for f in pjs[M]["fichas"] if f["id_ficha"] != "F2"]}}
    check("voto requiere_adjudicacion sin ficha levanta",
          levanta(lambda: cz.computar(csvs(pjs_sin, marcas), pjs_sin, res_sin, C1)))
    res_sin = json.loads(json.dumps(res))
    res_sin["planillas"][M]["mesa"] = [f for f in res_sin["planillas"][M]["mesa"] if f["id_ficha"] != "F1"]
    pjs_sin = {**pjs, M: {"fichas": [f for f in pjs[M]["fichas"] if f["id_ficha"] != "F1"]}}
    check("heredado sin ficha levanta",
          levanta(lambda: cz.computar(csvs(pjs_sin, marcas), pjs_sin, res_sin, C1)))

    print("-- (5) Wilson, determinismo y verificación contra el commit")
    check("Wilson 95 %: 8/40 = [0.105, 0.3476] y 5/40 = [0.0546, 0.2611] (valores de E5)",
          cz.wilson(8, 40) == [0.105, 0.3476] and cz.wilson(5, 40) == [0.0546, 0.2611])
    check("Wilson 95 %: 0/20 arranca en 0", cz.wilson(0, 20)[0] == 0.0)
    r2 = cz.computar(csvs(pjs, marcas), pjs, res, c1=C1)
    check("doble cómputo idéntico",
          json.dumps(r, sort_keys=True, ensure_ascii=False) == json.dumps(r2, sort_keys=True, ensure_ascii=False))
    real = pt.planilla_json_path("planilla_c5")
    check("verificación contra el commit: mismo contenido pasa",
          not levanta(cz.verificar_commit, "X", [real], lambda c, rel: real.read_bytes()))
    check("verificación contra el commit: contenido distinto levanta",
          levanta(cz.verificar_commit, "X", [real], lambda c, rel: b"otro"))

    print("-- (6) de punta a punta sobre las planillas reales, en memoria, con marcas sintéticas")
    salidas = (cz.OUT_JSON, cz.OUT_MD, cz.DEFINITIVOS_SM)
    def estado(ps):
        return {p: (pt.sha256_path(p) if p.exists() else None) for p in ps}
    antes = estado(list(pt.publicables(pt.construir())) + list(salidas))
    rr = pt.construir()
    pjs_r = {n: json.loads(pt.planilla_json_path(n).read_text(encoding="utf-8")) for n in pt.PLANILLAS}
    ok = True
    for marca in ("cumplido", "no_cumplido"):
        cs = {n: pt.render_csv(pj).replace(",,\n", f",{marca},\n") for n, pj in pjs_r.items()}
        out = cz.computar(cs, pjs_r, rr, c1=C1)
        ok &= sum(x["n"] for x in out["celdas"].values()) == 140
        ok &= all(sum(x["tabla_definitiva"].values()) == x["n"] for x in out["celdas"].values())
        ok &= sum(x["vias"]["adjudicacion_base"] + x["vias"]["adjudicacion_s7"]
                  for x in out["celdas"].values()) == pt.ESPERADO_PARES_ADJ
        ok &= all(d["definitivo"] != ADJ for c in out["solo_mesa"] for d in out["solo_mesa"][c]["definitivos"])
    check("todas cumplido y todas no_cumplido: 140 pares definitivos, 25 adjudicados, ninguno en "
          "requiere_adjudicacion", ok)
    despues = estado(list(antes))
    check("ningún archivo real se tocó (planillas, CSV y salidas del cierre en el mismo estado)",
          antes == despues)

    print("-- (7) re-derivación previa al cierre (corrección de E5.c.3)")
    rr7 = pt.construir()
    csvs7 = {pt.marcas_csv_path(n) for n in pt.PLANILLAS}
    revisados = cz.verificar_rederivacion(rr7)
    check("planillas, censo ciego y SOLO_MESA reales = su re-derivación; los dos CSV de marcas fuera",
          len(revisados) == len(pt.publicables(rr7)) + len(pt.solo_mesa(rr7)) - 2
          and not any(pt.rel_repo(p) in revisados for p in csvs7))
    def lector(alterado):
        return lambda p: (p.read_text(encoding="utf-8") + " ") if p == alterado else p.read_text(encoding="utf-8")
    check("una planilla alterada levanta",
          levanta(cz.verificar_rederivacion, rr7, lector(pt.planilla_json_path("planilla_c5"))))
    check("un SOLO_MESA alterado levanta",
          levanta(cz.verificar_rederivacion, rr7, lector(pt.PERTENENCIA_SM)))
    check("un CSV de marcas distinto del render en blanco no levanta (se verifica contra el commit)",
          not levanta(cz.verificar_rederivacion, rr7, lector(pt.marcas_csv_path("planilla_mezclada"))))

    passed = sum(ok for _, ok in _checks)
    print(f"\n  {passed}/{len(_checks)} checks OK")
    print("  RESULTADO:", "PASS" if passed == len(_checks) else "FAIL")
    return 0 if passed == len(_checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
