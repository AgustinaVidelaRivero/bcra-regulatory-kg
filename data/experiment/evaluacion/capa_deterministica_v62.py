"""capa_deterministica_v62.py — v6.2-D = v6.1-D + D7 (puntero estructural).

Implementa `docs/diseno_ciclo2.md` §2 (commit b84668e). **CAPA NUEVA AL LADO:**
capa_deterministica.py (v6.1-D, el baseline congelado) se IMPORTA sin modificarse; este
módulo solo agrega la decisión de frontera con D7 y recompone el pipeline.

SEMÁNTICA D7 (verbatim del diseño §2):
- Extracción: los ids de vecinos aparecidos en los outputs COMPLETOS RE-EJECUTADOS de
  `ver_vecinos` de la traza post-hoc (regla de la casa — nunca `output_truncado`), con
  evidencia {paso, relacion, nodo_consultado}; primera aparición (paso mínimo). Los
  listados de `buscar_nodos` NO se incluyen (canal léxico = D1).
- Tabla de verdad de la frontera navegación/alcanzabilidad (filas 0-3):
    0) portador no extraíble        → R3 como hoy; D7 NO aplica.
    1) D1 alcanzable                → navegación (como hoy).
    2) D1 NO alcanzable, puntero SÍ → navegación (D7: el grafo lo señalizó).
    3) D1 NO alcanzable, puntero NO → alcanzabilidad_kg (como hoy).
  En la fila 2 el módulo anotado es "D7" (puntero_estructural: true + evidencia); si el
  LLM había votado navegación, su voto SOBREVIVE (discrepancia=False); si había votado
  alcanzabilidad, se CORRIGE a navegación (discrepancia=True, emisión preservada).
- Bordes: ver_vecinos con error o 0 vecinos no aporta; D7 no razona sobre presupuesto;
  múltiples apariciones → se registra la primera.

Pipeline v6.2-D: D2' (esta tabla) → D3 → D5 → D6 → voto_pre_d6 → recomputo → D4 — los
módulos D3/D5/D6/D4 son los de v6.1-D importados tal cual. VERSION: "v6.2-D(2026-07)".
"""

import argparse
import copy
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from capa_deterministica import (   # v6.1-D congelada — SOLO imports
    FRONTERA_NAV, CAUSA_NAV, CAUSA_ALC,
    _en_frontera, _extraer_portador, _evidencia_d1_reducida, _recomputar_voto,
    aplicar_d3, aplicar_d4, aplicar_d5, aplicar_d6, _sintoma_de_trace,
)
from test_alcanzabilidad import (
    evaluar_alcanzabilidad, tokens_expuestos_de_trace, _index_de,
)

VERSION_CAPA_V62 = "v6.2-D(2026-07)"


# --------------------------------------------------------------------------- #
# D7 — extracción de punteros estructurales                                    #
# --------------------------------------------------------------------------- #
def extraer_punteros_estructurales(trace_path, index):
    """{vecino_id: {paso, relacion, nodo_consultado}} desde los outputs COMPLETOS
    re-ejecutados de los ver_vecinos de la traza (primera aparición, paso mínimo)."""
    elem = json.load(open(trace_path))[0]
    punteros = {}
    for s in elem["trace"]["steps"]:
        if s.get("tool") != "ver_vecinos":
            continue
        inp = s.get("input") or {}
        o = index.ver_vecinos(inp.get("id", ""), inp.get("direccion", "ambas"))
        if not isinstance(o, dict) or "error" in o:
            continue
        for lado in ("salientes", "entrantes"):
            for e in o.get(lado, []):
                vid = e.get("vecino_id")
                if vid and vid not in punteros:
                    punteros[vid] = {"paso": s["n"], "relacion": e.get("relation"),
                                     "nodo_consultado": inp.get("id")}
    return punteros


# --------------------------------------------------------------------------- #
# D2' — decisión de frontera con la tabla de verdad de 4 filas                 #
# --------------------------------------------------------------------------- #
def aplicar_d2_v62(caso_json, run, trace_path=None, *,
                   pregunta=None, consultas_agente=None, tokens_expuestos=None,
                   punteros=None):
    """Como aplicar_d2 de v6.1-D pero con D7 en la decisión (tabla del docstring).
    Los insumos de D1 salen de la traza o se inyectan (tests); `punteros` inyectable."""
    index = _index_de(run)
    ids_kg = list(index.by_id.keys())

    if trace_path is not None:
        elem = json.load(open(trace_path))[0]
        pregunta = elem["trace"]["question"]
        consultas_agente = [s["input"]["consulta"] for s in elem["trace"]["steps"]
                            if s.get("tool") == "buscar_nodos"]
        tokens_expuestos = tokens_expuestos_de_trace(trace_path, index=index)
        if punteros is None:
            punteros = extraer_punteros_estructurales(trace_path, index)
    elif pregunta is None or consultas_agente is None or tokens_expuestos is None:
        raise ValueError("falta trace_path, o la terna pregunta/consultas_agente/tokens_expuestos")
    punteros = punteros or {}

    salida = copy.deepcopy(caso_json)
    cache_d1 = {}
    reps_tocadas, corregidas, discrepancias, triage = set(), 0, 0, 0
    decisiones_con_puntero = 0

    for i, rep in enumerate(salida.get("repeticiones") or [], 1):
        if rep.get("formato_invalido"):
            continue
        for atrib in rep.get("atribuciones") or []:
            if not _en_frontera(atrib):
                continue
            reps_tocadas.add(i)
            portador, n_ids = _extraer_portador(atrib, ids_kg)
            if portador is None:
                # fila 0 — R3 como hoy; D7 NO aplica
                atrib["capa_d"] = {"modulo": "D2", "accion": "sin_portador_extraible",
                                   "triage": True}
                triage += 1
                continue
            if portador not in cache_d1:
                cache_d1[portador] = evaluar_alcanzabilidad(
                    portador, pregunta, consultas_agente, tokens_expuestos, index)
            d1 = cache_d1[portador]
            puntero = punteros.get(portador)
            emision = atrib["causa_capa2"]

            if d1["alcanzable"]:
                # fila 1 — como hoy (D2)
                decision, modulo = CAUSA_NAV, "D2"
            elif puntero is not None:
                # fila 2 — D7: el grafo lo señalizó
                decision, modulo = CAUSA_NAV, "D7"
                decisiones_con_puntero += 1
            else:
                # fila 3 — como hoy (D2)
                decision, modulo = CAUSA_ALC, "D2"

            anot = {
                "modulo": modulo,
                "portador_id": portador,
                "emision_llm": emision,
                "decision_codigo": decision,
                "discrepancia": decision != emision and not (
                    decision == CAUSA_NAV and emision in FRONTERA_NAV),
                "alcanzable": d1["alcanzable"],
                "evidencia_d1": _evidencia_d1_reducida(d1),
            }
            if modulo == "D7":
                anot["puntero_estructural"] = True
                anot["evidencia"] = dict(puntero)
            atrib["capa_d"] = anot
            atrib["causa_capa2"] = decision
            corregidas += 1
            if anot["discrepancia"]:
                discrepancias += 1

    salida["voto_capa_d"] = _recomputar_voto(salida.get("repeticiones") or [])
    salida["resumen_capa_d"] = {
        "reps_tocadas": sorted(reps_tocadas),
        "atribuciones_corregidas": corregidas,
        "discrepancias": discrepancias,
        "triage": triage,
        "punteros_estructurales_extraidos": len(punteros),
        "decisiones_con_puntero": decisiones_con_puntero,
    }
    return salida


# --------------------------------------------------------------------------- #
# Pipeline compuesto v6.2-D                                                    #
# --------------------------------------------------------------------------- #
def aplicar_capa_v62(caso_json, run, trace_path=None, *,
                     pregunta=None, consultas_agente=None, tokens_expuestos=None,
                     outputs_completos=None, sintoma_F=None, sintoma_P=None,
                     punteros=None):
    """v6.2-D: D2' (tabla con D7) → D3 → D5 → D6 → voto_pre_d6 → recomputo → D4.
    D3/D5/D6/D4 son los de v6.1-D, importados sin cambios."""
    index = _index_de(run)
    if trace_path is not None:
        sintoma_F, sintoma_P = _sintoma_de_trace(trace_path)
    elif sintoma_F is None or sintoma_P is None:
        raise ValueError("falta trace_path, o la dupla sintoma_F/sintoma_P (listas)")
    salida = aplicar_d2_v62(caso_json, index, trace_path=trace_path, pregunta=pregunta,
                            consultas_agente=consultas_agente,
                            tokens_expuestos=tokens_expuestos, punteros=punteros)
    resumen_d2 = salida["resumen_capa_d"]
    salida = aplicar_d3(salida, index)
    salida = aplicar_d5(salida, index, trace_path=trace_path, pregunta=pregunta,
                        consultas_agente=consultas_agente,
                        tokens_expuestos=tokens_expuestos,
                        outputs_completos=outputs_completos)
    salida = aplicar_d6(salida, sintoma_F, sintoma_P)
    salida["voto_pre_d6"] = salida["voto_capa_d"]
    salida["voto_capa_d"] = _recomputar_voto(salida.get("repeticiones") or [])
    salida = aplicar_d4(salida)
    salida["resumen_capa_d"] = resumen_d2   # el de D2' (con los contadores de D7)
    salida["version_capa"] = VERSION_CAPA_V62
    return salida


# --------------------------------------------------------------------------- #
# CLI (misma firma que capa_deterministica)                                    #
# --------------------------------------------------------------------------- #
def main(argv=None):
    ap = argparse.ArgumentParser(description="Capa determinística v6.2-D (= v6.1-D + D7)")
    ap.add_argument("--caso", required=True)
    ap.add_argument("--run", required=True)
    ap.add_argument("--trace", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args(argv)
    caso = json.load(open(args.caso))
    salida = aplicar_capa_v62(caso, args.run, trace_path=args.trace)
    with open(args.out, "w") as f:
        json.dump(salida, f, ensure_ascii=False, indent=1)
    print(json.dumps({"out": args.out, "version_capa": salida["version_capa"],
                      "resumen_capa_d": salida["resumen_capa_d"],
                      "triage_capa_d": salida["triage_capa_d"],
                      "voto_capa_d": salida["voto_capa_d"]}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
