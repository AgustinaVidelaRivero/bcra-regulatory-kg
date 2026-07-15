"""capa_deterministica.py — módulo D2: decisor determinístico de la frontera
navegación / alcanzabilidad_kg.

Módulo NUEVO; no modifica congelados (verificador.py, harness.py, taxonomia.md,
casos_control.md, test_alcanzabilidad.py). Consume la salida del verificador (JSON de caso
con repeticiones) y el módulo D1 (test_alcanzabilidad).

SEMÁNTICA PRE-REGISTRADA (verbatim del pedido de implementación)
----------------------------------------------------------------
- Recorre las repeticiones válidas (formato_invalido=false). Para cada atribución cuyo par
  (sintoma_capa1, causa_capa2) sea exactamente (context_recall, navegación) o
  (context_recall, alcanzabilidad_kg):
  a. Extrae el portador_id: busca en evidencia.nodo.ubicacion (y como fallback en
     evidencia.nodo.quote) un id de nodo EXISTENTE en el grafo del run, por match exacto de
     substring contra la lista de ids del kg. Si encuentra cero o más de uno distintos → NO
     corrige: anota capa_d = {modulo: "D2", accion: "sin_portador_extraible", triage: true}
     y sigue.
  b. Con portador_id único: corre test_alcanzabilidad.evaluar_alcanzabilidad con la pregunta
     y las consultas buscar_nodos de la traza post-hoc del caso, y los tokens expuestos vía
     tokens_expuestos_de_trace. alcanzable=False → causa_capa2 := alcanzabilidad_kg;
     alcanzable=True → causa_capa2 := navegación.
  c. Anota SIEMPRE capa_d en la atribución: {modulo: "D2", emision_llm: <causa original>,
     decision_codigo: <causa final>, discrepancia: <bool>, alcanzable: <bool>,
     evidencia_d1: <dict de D1 SIN la lista completa de consultas; conservá
     n_consultas_simuladas, la lista de consultas con en_top10=true, y el mejor rank>}.
- Atribuciones con otros pares: intactas, sin capa_d.
- Recomputa el voto con la regla del protocolo (mayoría estricta ≥2 sobre reps válidas,
  sobre el multiconjunto de pares primarios YA corregidos; sin mayoría → triage) y lo emite
  como voto_capa_d, preservando el voto original intacto en el JSON de salida.
- El dict de salida es el caso_json completo + las anotaciones + un bloque resumen_capa_d:
  {reps_tocadas, atribuciones_corregidas, discrepancias, triage}.

Notas de implementación (no alteran la semántica de arriba):
- La causa "navegación" se reconoce en sus dos grafías (con y sin acento) por robustez de
  fuente; la decisión de código se emite SIEMPRE con la grafía de la taxonomía
  ("navegación" / "alcanzabilidad_kg").
- `run` acepta la clave del run (str) o un harness.GraphIndex ya construido (tests con grafo
  sintético, sin disco), igual que en D1.
- Los insumos de D1 (pregunta, consultas del agente, tokens expuestos) salen de la traza
  post-hoc (`trace_path`); para tests sin disco pueden inyectarse por parámetro
  (pregunta/consultas_agente/tokens_expuestos). Exactamente una de las dos vías es
  obligatoria.
- El match de substring del extractor exige ids completos como los escribe el verificador
  (la evidencia del contrato usa el id verbatim en `ubicacion`); si más de un id distinto
  del kg matchea (p. ej. un id contenido en otro), se cae a `sin_portador_extraible` por la
  regla pre-registrada — sin heurísticas de desempate.
- El recomputo del voto usa como clave de cada rep válida el MULTICONJUNTO ordenado de sus
  pares primarios corregidos (misma noción de clave que el voto programático del
  verificador); las reps inválidas no votan.
"""

import argparse
import copy
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from harness import GraphIndex                      # congelado — solo import
from test_alcanzabilidad import (                   # D1 — solo import
    evaluar_alcanzabilidad,
    tokens_expuestos_de_trace,
    _index_de,
)

FRONTERA_NAV = {"navegación", "navegacion"}
CAUSA_NAV = "navegación"
CAUSA_ALC = "alcanzabilidad_kg"


def _en_frontera(atrib):
    return (
        atrib.get("sintoma_capa1") == "context_recall"
        and atrib.get("causa_capa2") in (FRONTERA_NAV | {CAUSA_ALC})
    )


def _extraer_portador(atrib, ids_kg):
    """Ids del kg presentes por substring exacto en evidencia.nodo.ubicacion
    (fallback: evidencia.nodo.quote). Devuelve (portador_id | None, n_distintos)."""
    ev = (atrib.get("evidencia") or {}).get("nodo") or {}
    for campo in ("ubicacion", "quote"):
        texto = ev.get(campo) or ""
        matches = sorted({nid for nid in ids_kg if nid in texto})
        if matches:
            return (matches[0], 1) if len(matches) == 1 else (None, len(matches))
    return (None, 0)


def _evidencia_d1_reducida(d1):
    """Dict de D1 sin la lista completa de consultas: n_consultas_simuladas, las consultas
    con en_top10=true, y el mejor rank."""
    ranks = [c["rank"] for c in d1["consultas"] if c["rank"] is not None]
    return {
        "alcanzable": d1["alcanzable"],
        "n_consultas_simuladas": d1["n_consultas_simuladas"],
        "consultas_en_top10": [c for c in d1["consultas"] if c["en_top10"]],
        "mejor_rank": min(ranks) if ranks else None,
    }


def _clave_primarias(rep):
    """Multiconjunto ordenado de pares primarios de la rep (sobre causas ya corregidas)."""
    pares = sorted(
        (a.get("sintoma_capa1"), a.get("causa_capa2"))
        for a in rep.get("atribuciones") or []
        if a.get("jerarquia") == "primaria"
    )
    return tuple(pares)


def _recomputar_voto(reps):
    """Regla del protocolo: mayoría estricta ≥2 sobre reps válidas; sin mayoría → triage."""
    validas = [(i + 1, r) for i, r in enumerate(reps) if not r.get("formato_invalido")]
    conteo = {}
    for n, r in validas:
        conteo.setdefault(_clave_primarias(r), []).append(n)
    orden = sorted(conteo.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    ganadora = orden[0] if orden else None
    hay_mayoria = ganadora is not None and len(ganadora[1]) >= 2
    return {
        "resultado": "mayoria" if hay_mayoria else "frontera_no_determinada",
        "flag_voto_dividido": not hay_mayoria,
        "pares_primarios_ganadores": [list(p) for p in ganadora[0]] if hay_mayoria else None,
        "votos_ganadores": len(ganadora[1]) if hay_mayoria else None,
        "reps_validas": [n for n, _ in validas],
        "conteo": [
            {"pares_primarios": [list(p) for p in clave], "votos": len(ns), "reps": ns}
            for clave, ns in orden
        ],
    }


def aplicar_d2(caso_json, run, trace_path=None, *,
               pregunta=None, consultas_agente=None, tokens_expuestos=None):
    """Aplica el decisor D2 según la semántica pre-registrada del docstring del módulo.

    Insumos de D1: o bien `trace_path` (traza post-hoc del caso: de ahí salen la pregunta,
    las consultas buscar_nodos y los tokens expuestos), o bien los tres inyectados
    (pregunta, consultas_agente, tokens_expuestos) para tests sin disco."""
    index = _index_de(run)
    ids_kg = list(index.by_id.keys())

    if trace_path is not None:
        elem = json.load(open(trace_path))[0]
        pregunta = elem["trace"]["question"]
        consultas_agente = [s["input"]["consulta"] for s in elem["trace"]["steps"]
                            if s.get("tool") == "buscar_nodos"]
        tokens_expuestos = tokens_expuestos_de_trace(trace_path, index=index)
    elif pregunta is None or consultas_agente is None or tokens_expuestos is None:
        raise ValueError("falta trace_path, o la terna pregunta/consultas_agente/tokens_expuestos")

    salida = copy.deepcopy(caso_json)
    cache_d1 = {}
    reps_tocadas, corregidas, discrepancias, triage = set(), 0, 0, 0

    for i, rep in enumerate(salida.get("repeticiones") or [], 1):
        if rep.get("formato_invalido"):
            continue
        for atrib in rep.get("atribuciones") or []:
            if not _en_frontera(atrib):
                continue
            reps_tocadas.add(i)
            portador, n_ids = _extraer_portador(atrib, ids_kg)
            if portador is None:
                atrib["capa_d"] = {"modulo": "D2", "accion": "sin_portador_extraible",
                                   "triage": True}
                triage += 1
                continue
            if portador not in cache_d1:
                cache_d1[portador] = evaluar_alcanzabilidad(
                    portador, pregunta, consultas_agente, tokens_expuestos, index)
            d1 = cache_d1[portador]
            emision = atrib["causa_capa2"]
            decision = CAUSA_NAV if d1["alcanzable"] else CAUSA_ALC
            atrib["capa_d"] = {
                "modulo": "D2",
                "portador_id": portador,
                "emision_llm": emision,
                "decision_codigo": decision,
                "discrepancia": decision != emision and not (
                    decision == CAUSA_NAV and emision in FRONTERA_NAV),
                "alcanzable": d1["alcanzable"],
                "evidencia_d1": _evidencia_d1_reducida(d1),
            }
            atrib["causa_capa2"] = decision
            corregidas += 1
            if atrib["capa_d"]["discrepancia"]:
                discrepancias += 1

    salida["voto_capa_d"] = _recomputar_voto(salida.get("repeticiones") or [])
    salida["resumen_capa_d"] = {
        "reps_tocadas": sorted(reps_tocadas),
        "atribuciones_corregidas": corregidas,
        "discrepancias": discrepancias,
        "triage": triage,
    }
    return salida


# --------------------------------------------------------------------------- #
# CLI                                                                          #
# --------------------------------------------------------------------------- #
def main(argv=None):
    ap = argparse.ArgumentParser(description="D2 — decisor de frontera navegación/alcanzabilidad")
    ap.add_argument("--caso", required=True, help="path al JSON del caso del gate")
    ap.add_argument("--run", required=True, help="clave del run (p. ej. run_3)")
    ap.add_argument("--trace", required=True, help="path a la traza post-hoc del caso")
    ap.add_argument("--out", required=True, help="path del JSON de salida")
    args = ap.parse_args(argv)

    caso = json.load(open(args.caso))
    salida = aplicar_d2(caso, args.run, trace_path=args.trace)
    with open(args.out, "w") as f:
        json.dump(salida, f, ensure_ascii=False, indent=1)
    print(json.dumps({"out": args.out,
                      "resumen_capa_d": salida["resumen_capa_d"],
                      "voto_capa_d": salida["voto_capa_d"]},
                     ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
