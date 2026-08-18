"""
tests_replay_v2.py — Tests del ADAPTADOR de replay v2-aware (U-A1.4): el
re-ejecutor `agente_celda.reejecutar_step_celda` + `BackendCelda`, inyectado
por atributo de módulo en `metrica` / `metrica_ev2` (que no se editan).
Necesita el contenedor Neo4j con KG-Refinado (tools reales, $0, sin API).

Qué verifica:
  T1  despacho v2 de `ver_vecinos` == `ToolsV2.ver_vecinos_v2` directo (mismos
      argumentos: relacion / pagina / por_pagina) y == `ToolsV2.despachar`
      (mismos defaults cuando faltan argumentos);
  T2  despacho v1 de `ver_vecinos` == `Neo4jIndex.ver_vecinos(id, direccion)`
      == harness `GraphIndex.ver_vecinos` in-memory (paridad);
  T3  `buscar_nodos`: celda bm25 == Neo4jIndex fulltext; celda booleano ==
      Neo4jIndex paridad == GraphIndex in-memory (byte a byte);
  T4  la inyección reemplaza `metrica._reejecutar_step` y `metrica_ev2._reejecutar_step`
      solo dentro del contexto y los restaura al salir;
  T5  sobre una traza v2 sintética (steps ejecutados con el mismo backend),
      `evaluar_payload` da replay estándar y fuerte OK, y con el re-ejecutor
      ORIGINAL (v1) el replay fuerte de un step con `pagina`/`relacion` FALLA
      (demuestra que el adaptador es necesario y que el replay fuerte detecta
      el backend equivocado);
  T6  celdas v1: `evaluar_payload` usa el `_reejecutar_step` original (no inyecta).

Uso: .venv/bin/python -B tests_replay_v2.py   (exit 0 si todo PASS)
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

CORRIDA_DIR = Path(__file__).resolve().parent
if str(CORRIDA_DIR) not in sys.path:
    sys.path.insert(0, str(CORRIDA_DIR))

from comun_corrida import GRAFO, cargar_celdas, indice_anclas_refinado, verificar_kg_meta  # noqa: E402
from agente_celda import BackendCelda, reejecutar_step_celda  # noqa: E402
import replay_ablacion as ra  # noqa: E402
import metrica  # noqa: E402
import metrica_ev2  # noqa: E402
from harness import GraphIndex, TRUNC_TOOL_OUTPUT, _truncate  # noqa: E402
from comun_ev2 import cargar_runtime  # noqa: E402
from tools_v2 import ToolsV2  # noqa: E402
from neo4j_index import Neo4jIndex  # noqa: E402

HUB = "Sujeto_rol_sujeto_obligado_proteccion"     # nodo con 7 entrantes miembro_de (BKL-0027)


def _traza_desde_steps(backend: BackendCelda, steps: list[tuple[str, dict]]) -> dict:
    """Payload mínimo con formato de la corrida a partir de (tool, args)."""
    trace_steps, steps_full = [], []
    for i, (tool, args) in enumerate(steps, 1):
        out = backend.despachar(tool, args)
        s = json.dumps(out, ensure_ascii=False)
        trace_steps.append({"n": i, "tool": tool, "input": args, "output_truncado": _truncate(s),
                            "output_chars": len(s)})
        steps_full.append({"n": i, "tool": tool, "input": args, "output": out, "output_chars": len(s)})
    return {"meta": {}, "trace": {"steps": trace_steps}, "steps_full": steps_full}


def correr_tests(driver=None, verbose: bool = True) -> list[tuple[str, bool]]:
    if driver is None:
        from conexion import abrir_driver
        driver = abrir_driver()
    verificar_kg_meta(driver, GRAFO)
    celdas = cargar_celdas()
    B = {cid: BackendCelda(driver, c, grafo=GRAFO) for cid, c in celdas.items()}
    tv2 = ToolsV2(driver, grafo=GRAFO)
    idx_par = Neo4jIndex(driver, grafo=GRAFO, modo="paridad")
    idx_ft = Neo4jIndex(driver, grafo=GRAFO, modo="fulltext")
    gi = GraphIndex(cargar_runtime("v3"))
    checks = []

    def ck(nombre, cond):
        checks.append((nombre, bool(cond)))
        if verbose:
            print(f"  [{'PASS' if cond else 'FAIL'}] {nombre}")

    # hub con > 40 vecinos en alguna dirección para ejercitar página 2
    hub_grande = None
    with driver.session() as s:
        rec = s.run(f"MATCH (n:`{GRAFO}`)<-[r]-(:`{GRAFO}`) WITH n, count(r) AS c WHERE c > 40 "
                    "RETURN n.id AS id ORDER BY c DESC, n.id LIMIT 1").single()
        hub_grande = rec["id"] if rec else HUB

    # T1 — v2
    for cid in ("C01_booleano_v2", "C11_bm25_v2"):
        b = B[cid]
        casos = [{"id": HUB, "relacion": "miembro_de", "pagina": 1, "por_pagina": 5},
                 {"id": hub_grande, "pagina": 2},
                 {"id": hub_grande, "pagina": 2, "por_pagina": 10, "relacion": None},
                 {"id": HUB}, {"id": "no_existe_xyz"}]
        ok = True
        for args in casos:
            a = reejecutar_step_celda(b, {"tool": "ver_vecinos", "input": args})
            d = tv2.ver_vecinos_v2(args["id"], relacion=args.get("relacion"), pagina=args.get("pagina", 1),
                                   por_pagina=args.get("por_pagina", 40))
            e = tv2.despachar("ver_vecinos", args)
            ok = ok and (a == d == e)
        ck(f"T1 {cid}: reejecutar ver_vecinos == ToolsV2.ver_vecinos_v2 == ToolsV2.despachar ({len(casos)} args)", ok)
        r2 = reejecutar_step_celda(b, {"tool": "ver_vecinos", "input": {"id": hub_grande, "pagina": 2}})
        ck(f"T1 {cid}: página 2 de un hub grande no vacía y rotulada pagina=2",
           r2.get("pagina") == 2 and (r2.get("entrantes") or r2.get("salientes")))

    # T2 — v1
    for cid in ("C00_booleano_v1", "C10_bm25_v1"):
        b = B[cid]
        ok = True
        for args in ({"id": HUB, "direccion": "entrantes"}, {"id": HUB}, {"id": hub_grande, "direccion": "ambas"},
                     {"id": "no_existe_xyz"}):
            a = metrica._reejecutar_step(b.index_busqueda, {"tool": "ver_vecinos", "input": args})
            d = idx_par.ver_vecinos(args["id"], args.get("direccion", "ambas"))
            g = gi.ver_vecinos(args["id"], args.get("direccion", "ambas"))
            ok = ok and (a == d == g)
        ck(f"T2 {cid}: metrica._reejecutar_step(Neo4jIndex) ver_vecinos == Neo4jIndex == GraphIndex in-memory", ok)

    # T3 — buscar_nodos por retriever
    consultas = ["asociaciones mutuales", "financiación exportaciones", "Sujeto_rol_sujeto_obligado_proteccion", "de la"]
    ok_bm = all(B["C10_bm25_v1"].buscar_nodos(q, 10) == idx_ft.buscar_nodos(q, 10) == B["C11_bm25_v2"].buscar_nodos(q, 10)
                for q in consultas)
    ok_bo = all(B["C00_booleano_v1"].buscar_nodos(q, 10) == idx_par.buscar_nodos(q, 10) == gi.buscar_nodos(q, 10)
                == B["C01_booleano_v2"].buscar_nodos(q, 10) for q in consultas)
    ck("T3 bm25: BackendCelda(C10/C11).buscar_nodos == Neo4jIndex fulltext", ok_bm)
    ck("T3 booleano: BackendCelda(C00/C01).buscar_nodos == Neo4jIndex paridad == GraphIndex in-memory", ok_bo)
    ck("T3 los dos retrievers difieren en al menos una consulta (el factor R es real)",
       any(idx_ft.buscar_nodos(q, 10) != idx_par.buscar_nodos(q, 10) for q in consultas))

    # T4 — inyección y restauración
    o1, o2 = metrica._reejecutar_step, metrica_ev2._reejecutar_step
    with ra._Inyeccion(reejecutar_step_celda):
        dentro = (metrica._reejecutar_step is reejecutar_step_celda and metrica_ev2._reejecutar_step is reejecutar_step_celda)
    ck("T4 inyección activa dentro del contexto", dentro)
    ck("T4 restauración al salir", metrica._reejecutar_step is o1 and metrica_ev2._reejecutar_step is o2)

    # T5 — traza v2 sintética
    ancla_index = indice_anclas_refinado()
    b = B["C11_bm25_v2"]
    steps = [("buscar_nodos", {"consulta": "sujeto obligado", "limite": 5}),
             ("ver_vecinos", {"id": HUB, "relacion": "miembro_de", "pagina": 1}),
             ("ver_vecinos", {"id": hub_grande, "pagina": 2, "por_pagina": 40}),
             ("ver_nodo", {"id": HUB})]
    payload = _traza_desde_steps(b, steps)
    ev = ra.evaluar_payload(payload, [], ancla_index, b)
    ck("T5 replay estándar + fuerte OK con el adaptador v2-aware", ev["replay_ok"] and ev["replay_fuerte_ok"])
    ev_mal = metrica_ev2.evaluar_caso(payload, [], ancla_index, b.index_busqueda)   # re-ejecutor ORIGINAL (v1)
    ck("T5 con el re-ejecutor v1 original el replay FUERTE de la traza v2 falla (adaptador necesario)",
       not ev_mal["replay_fuerte_ok"] and any(f["tool"] == "ver_vecinos" for f in ev_mal["replay_fuerte_fallas"]))
    ck("T5 tras evaluar, metrica._reejecutar_step sigue siendo el original",
       metrica._reejecutar_step is o1 and metrica_ev2._reejecutar_step is o2)

    # T6 — v1 usa el original
    b1 = B["C10_bm25_v1"]
    payload1 = _traza_desde_steps(b1, [("buscar_nodos", {"consulta": "sujeto obligado", "limite": 5}),
                                       ("ver_vecinos", {"id": HUB, "direccion": "entrantes"})])
    ev1 = ra.evaluar_payload(payload1, [], ancla_index, b1)
    ck("T6 celda v1: replay estándar + fuerte OK con el re-ejecutor original y Neo4jIndex(fulltext)",
       ev1["replay_ok"] and ev1["replay_fuerte_ok"])
    return checks


def main() -> int:
    print("== tests del adaptador de replay v2-aware ==")
    checks = correr_tests()
    fails = [n for n, ok in checks if not ok]
    print(f"{len(checks) - len(fails)}/{len(checks)} PASS")
    return 0 if not fails else 1


if __name__ == "__main__":
    raise SystemExit(main())
