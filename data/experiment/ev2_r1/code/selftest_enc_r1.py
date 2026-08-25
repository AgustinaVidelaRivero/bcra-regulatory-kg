"""
selftest_enc_r1.py — SELFTEST OFFLINE del encadenamiento §7 de U-B1.8 ($0,
sin API), previo a todo gasto de la etapa (condición de la autorización).

Cubre lo propio de enc_r1.py (agente/juez base ya cubiertos por selftest_r1 y
selftest_juez_r1):
  1. POBLACIÓN (sobre los datos REALES de la base de r1, determinístico):
     23 parciales + 5 correctos + auditoría 1 (semilla auditoria-ev2-r1,
     reproducible) = 24 pares; guarda de esperados detecta manipulación.
  2. casos_agente: 24 casos, subsecuencia del orden orden-ev2-r1.
  3. Ids opacos EV2E1- con REP en la clave: textos idénticos entre reps no
     colisionan; orden ciego juez-ev2-r1-enc determinístico; vínculo por par
     correcto.
  4. Ceguera §7: requests limpios con respuestas sintéticas; fuga PROVOCADA
     (marcador de tipo de disparo en la respuesta) detectada.
  5. agregar_pares: mayoría / ADJ invariante / incompleto, y flip de la
     auditoría (con agregar_par/flip_descendente IMPORTADOS de 9044a04).
  6. anotar_trazas_enc: agrega meta.u_b18_enc sin alterar claves (sobre una
     traza sintética bajo selftest_out/, con TRAZAS_DIR redirigido).

Uso:  .venv/bin/python -B data/experiment/ev2_r1/code/selftest_enc_r1.py
"""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_r1 as cr                      # noqa: E402
import enc_r1 as er                        # noqa: E402
import agregacion_enc as ag                # noqa: E402
from comun_r1 import cf                    # noqa: E402

OUT = cr.SELFTEST_DIR / "enc"

_checks = []


def check(nombre, cond):
    _checks.append((nombre, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {nombre}")


def main() -> int:
    print("== SELFTEST OFFLINE del §7 de U-B1.8 (sin API, $0) ==")
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    # --- 1) población (datos reales de la base de r1; sin persistir) ---
    p1, p2 = er.derivar_poblacion(), er.derivar_poblacion()
    check("población determinística (dos derivaciones idénticas)", p1 == p2)
    check("población: 23 parciales + 1 auditoría = 24 pares; 5 correctos",
          p1["n_pares"] == 24 and len(p1["ids_auditoria"]) == 1
          and len(p1["ids_correctos_ordenados"]) == 5
          and sum(1 for p in p1["pares"] if p["tipo"] == "parcial_disparado") == 23)
    check("auditoría: muestreada de los correctos con semilla auditoria-ev2-r1",
          set(p1["ids_auditoria"]) <= set(p1["ids_correctos_ordenados"]))
    orig = er.ESPERADO["pares"]
    er.ESPERADO["pares"] = 99
    try:
        er.derivar_poblacion()
        guardas = False
    except ValueError:
        guardas = True
    finally:
        er.ESPERADO["pares"] = orig
    check("guarda de esperados detecta población fuera de lo autorizado", guardas)

    # --- 2) casos_agente ---
    casos = er.casos_agente(p1)
    orden_global = [c["caso_id"] for c in cr.casos_fidelidad_r1()]
    sub = [c["caso_id"] for c in casos]
    check("casos_agente: 24 casos, subsecuencia del orden orden-ev2-r1",
          len(sub) == 24
          and [q for q in orden_global if q in set(sub)] == sub)

    # --- 3) ids opacos con rep en la clave + orden + vínculo ---
    gold = cf.cargar_gold()
    qA, qB = p1["pares"][0]["id_pregunta"], p1["pares"][1]["id_pregunta"]
    par_por_q = {p["id_pregunta"]: p for p in p1["pares"]}
    respuestas = []
    for q in (qA, qB):
        p = par_por_q[q]
        for rep in (1, 2, 3):
            # reps 1 y 2 de qA con TEXTO IDÉNTICO (caso real: re-muestreos iguales)
            texto = "texto idéntico" if (q == qA and rep in (1, 2)) \
                else f"texto sintético rep {rep}"
            respuestas.append({"id_pregunta": q, "rep": rep,
                               "label": cr.label_enc(rep), "tipo": p["tipo"],
                               "id_opaco_base": p["id_opaco_base"],
                               "veredicto_base": p["veredicto"],
                               "respuesta": texto, "respondible_flag": True,
                               "pregunta_traza": gold[q]["pregunta"]})
    c1 = er.armar_casos_enc(respuestas, gold)
    c2 = er.armar_casos_enc(respuestas, gold)
    check("orden ciego §7 determinístico", [c["id_opaco"] for c in c1]
          == [c["id_opaco"] for c in c2])
    check("ids EV2E1- únicos pese a textos idénticos entre reps (rep en la clave)",
          all(c["id_opaco"].startswith("EV2E1-") for c in c1)
          and len({c["id_opaco"] for c in c1}) == 6
          and len(c1[0]["duplicados_texto"]) == 1)
    por_par = {}
    for c in c1:
        por_par.setdefault(c["id_opaco_base"], {})[c["rep"]] = c["id_opaco"]
    check("vínculo por par: 2 pares × 3 reps",
          len(por_par) == 2 and all(set(v) == {1, 2, 3} for v in por_par.values()))

    # --- 4) ceguera ---
    ciegos = cf.vista_ciega(c1)
    check("ceguera §7 limpia: 0 fugas", er.verificar_ceguera_enc(ciegos) == [])
    sucio = [dict(ciegos[0])]
    sucio[0]["respuesta"] += " parcial_disparado"
    check("fuga PROVOCADA (tipo de disparo en la respuesta) detectada",
          er.verificar_ceguera_enc(sucio) != [])

    # --- 5) agregar_pares (sintético; regla importada de 9044a04) ---
    ids = {b: {str(r): f"EV2E1-fake{b}{r}" for r in (1, 2, 3)} for b in ("A", "B", "C")}
    vinculo = {"n_pares": 3, "pares": [
        {"id_opaco_base": "A", "tipo": "parcial_disparado", "reps": ids["A"]},
        {"id_opaco_base": "B", "tipo": "auditoria_correcto", "reps": ids["B"]},
        {"id_opaco_base": "C", "tipo": "parcial_disparado", "reps": ids["C"]},
    ]}
    def agdum(i, v):
        return {"id_opaco": i, "veredicto_pregunta": v,
                "clasificacion_respuesta_modal": "contenido"}
    agg = {"agregados": [
        agdum(ids["A"]["1"], "correcto"), agdum(ids["A"]["2"], "correcto"),
        agdum(ids["A"]["3"], "requiere_adjudicacion"),            # invariante → correcto
        agdum(ids["B"]["1"], "parcial"), agdum(ids["B"]["2"], "correcto"),
        agdum(ids["B"]["3"], "parcial"),                          # auditoría → flip
        agdum(ids["C"]["1"], "correcto"), agdum(ids["C"]["2"], "parcial"),
    ], "incompletas": [{"id_opaco": ids["C"]["3"]}]}              # C incompleto
    res = er.agregar_pares(agg, vinculo)
    porb = {p["id_opaco_base"]: p for p in res["pares"]}
    check("agregar_pares: ADJ invariante → correcto (vía de 9044a04)",
          porb["A"]["final"] == "correcto" and porb["A"]["via"] == "invariante_con_pendiente")
    check("agregar_pares: auditoría con mayoría parcial → flip descendente",
          porb["B"]["final"] == "parcial" and porb["B"]["flip_descendente"] == "flip"
          and res["auditoria"]["flips"] == 1)
    check("agregar_pares: par con rep incompleta queda fuera y contado",
          res["n_pares_agregados"] == 2 and res["n_pares_incompletos"] == 1)
    check("coherencia con agregar_par importado",
          ag.agregar_par(["correcto", "correcto", "requiere_adjudicacion"]) == "correcto")

    # --- 6) anotar_trazas_enc sobre traza sintética (TRAZAS_DIR redirigido) ---
    fake_dir = OUT / "trazas" / cr.label_enc(1)
    fake_dir.mkdir(parents=True)
    qX = p1["pares"][0]["id_pregunta"]
    (fake_dir / f"{qX}.json").write_text(json.dumps(
        {"meta": {"caso_id": qX, "label": cr.label_enc(1), "grafo": "r1"},
         "trace": {}, "pregunta": "x"}, ensure_ascii=False), encoding="utf-8")
    orig_dir = cr.TRAZAS_DIR
    try:
        cr.TRAZAS_DIR = OUT / "trazas"
        n = er.anotar_trazas_enc(p1, 1)
    finally:
        cr.TRAZAS_DIR = orig_dir
    t = json.loads((fake_dir / f"{qX}.json").read_text(encoding="utf-8"))
    check("anotar_trazas_enc: meta.u_b18_enc agregado sin alterar claves base",
          n == 1 and t["meta"]["u_b18_enc"]["tipo"] == p1["pares"][0]["tipo"]
          and t["meta"]["caso_id"] == qX
          and t["meta"]["u_b18_enc"]["semilla_orden_real"] == cr.SEMILLA_ORDEN_R1)

    passed = sum(ok for _, ok in _checks)
    print(f"\n  {passed}/{len(_checks)} checks OK")
    print("  RESULTADO:", "PASS" if passed == len(_checks) else "FAIL")
    return 0 if passed == len(_checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
