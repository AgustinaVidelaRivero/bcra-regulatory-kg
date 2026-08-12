"""
ensamblar_corpus.py — Ensamblado FINAL del GRAFO v2 COMPLETO: merge
determinístico de los 5 grafos por TO producidos por la corrida de corpus
(runner_corpus.py → salida/<to>/grafo_<to>.json) en UN solo kg.json, más los
tests de respuesta conocida verificables sin gold externo.

Código puro, cero LLM. Reglas de merge (mismas que E2, extendidas cross-TO):
  - Nodos con el mismo id (= mismo type + slug de contenido, convención v3)
    se fusionan: provenances acumuladas con dedup exacto; properties
    first-write-wins EN ORDEN DE CORRIDA (pro → cla → ric → cap → ext, el
    mismo orden documental de la corrida) con todo conflicto REGISTRADO.
    Cross-TO solo colisionan nodos de contenido idéntico tras normalizar
    (en la práctica: Sujetos del catálogo compartido).
  - Aristas con la misma (source, relation, target) se fusionan igual.

Uso:  .venv/bin/python3 ensamblar_corpus.py [--salida DIR]
Escribe: salida/kg.json, salida/reporte_ensamblado.json,
         salida/tests_respuesta_conocida.json
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
import unicodedata
from collections import Counter
from copy import deepcopy
from pathlib import Path

AQUI = Path(__file__).resolve().parent

TOS_ORDEN = ("pro", "cla", "ric", "cap", "ext")


def _norm(s: str) -> str:
    s = unicodedata.normalize("NFD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return s.lower()


def merge_grafos(grafos: dict[str, dict]) -> dict:
    nodes: dict[str, dict] = {}
    edges: dict[tuple, dict] = {}
    conflictos: list[dict] = []
    merges_nodo_cross_to: list[dict] = []

    for to in TOS_ORDEN:
        for n in grafos[to]["nodes"]:
            nid = n["id"]
            if nid not in nodes:
                nodes[nid] = deepcopy(n)
                nodes[nid]["_tos"] = [to]
            else:
                m = nodes[nid]
                if to not in m["_tos"]:
                    merges_nodo_cross_to.append(
                        {"id": nid, "type": m.get("type"),
                         "label": m.get("label"), "tos": m["_tos"] + [to]})
                    m["_tos"].append(to)
                vistos = {json.dumps(p, ensure_ascii=False, sort_keys=True)
                          for p in m.get("provenances", [])}
                for p in n.get("provenances", []):
                    k = json.dumps(p, ensure_ascii=False, sort_keys=True)
                    if k not in vistos:
                        m.setdefault("provenances", []).append(p)
                        vistos.add(k)
                for k, v in (n.get("properties") or {}).items():
                    props = m.setdefault("properties", {})
                    if k not in props:
                        props[k] = v
                    elif props[k] != v:
                        conflictos.append({"nivel": "nodo", "id": nid,
                                           "property": k, "gana": props[k],
                                           "pierde": v, "to_perdedor": to})
                if n.get("label") != m.get("label"):
                    conflictos.append({"nivel": "nodo", "id": nid,
                                       "property": "label", "gana": m.get("label"),
                                       "pierde": n.get("label"), "to_perdedor": to})
        for e in grafos[to]["edges"]:
            k = (e["source"], e["relation"], e["target"])
            if k not in edges:
                edges[k] = deepcopy(e)
            else:
                m = edges[k]
                vistos = {json.dumps(p, ensure_ascii=False, sort_keys=True)
                          for p in m.get("provenances", [])}
                for p in e.get("provenances", []):
                    pk = json.dumps(p, ensure_ascii=False, sort_keys=True)
                    if pk not in vistos:
                        m.setdefault("provenances", []).append(p)
                        vistos.add(pk)

    for n in nodes.values():
        n.pop("_tos", None)
    return {"nodes": list(nodes.values()), "edges": list(edges.values()),
            "conflictos": conflictos, "merges_cross_to": merges_nodo_cross_to}


# --------------------- tests de respuesta conocida ----------------------- #
def _nodos_con(nodes: list[dict], pred) -> list[dict]:
    return [n for n in nodes if pred(n)]


def _texto_nodo(n: dict) -> str:
    partes = [n.get("label", "")]
    for v in (n.get("properties") or {}).values():
        partes.append(str(v))
    return _norm(" ".join(partes))


def _puntos(n: dict) -> set[str]:
    return {p.get("punto", "") for p in n.get("provenances", [])}


def _archivos(n: dict) -> set[str]:
    return {p.get("archivo", "") for p in n.get("provenances", [])}


def tests_respuesta_conocida(kg: dict) -> dict:
    nodes = kg["nodes"]
    res = {}

    # T1 — BKL-0024: ext 3.9 tiene nodos de contenido, con el tope USD 200.
    ext39 = _nodos_con(nodes, lambda n: any(
        a.startswith("TO_exterior") for a in _archivos(n)) and any(
        p == "3.9" or p.startswith("3.9.") for p in _puntos(n)))
    con_200 = [n for n in ext39 if "200" in _texto_nodo(n)]
    res["T1_bkl0024_ext_3_9"] = {
        "pass": bool(ext39) and bool(con_200),
        "nodos_anclados_3_9": len(ext39),
        "puntos": sorted({p for n in ext39 for p in _puntos(n)
                          if p == "3.9" or p.startswith("3.9.")}),
        "nodos_con_usd_200": [{"id": n["id"], "label": n["label"]}
                              for n in con_200][:8],
    }

    # T2 — cláusula del 125 % (caso rector anti-fusión U6-008): las variantes
    # casi idénticas del tope "125 %" de ext deben ser nodos SEPARADOS con
    # provenance separada (puntos distintos), no una fusión.
    n125 = _nodos_con(nodes, lambda n: ("125 %" in _texto_nodo(n)
                                        or "125%" in _texto_nodo(n))
                      and any(p.get("to") == "ext"
                              for p in n.get("provenances", [])))
    puntos_125 = sorted({p for n in n125 for p in _puntos(n)})
    res["T2_clausula_125"] = {
        "pass": len(n125) >= 5 and len(puntos_125) >= 4,
        "n_nodos_separados_ext": len(n125),
        "puntos_distintos": puntos_125,
        "nodos": [{"id": n["id"], "label": n["label"],
                   "puntos": sorted(_puntos(n))} for n in n125][:12],
    }

    # T3 — pro 1.1.2.5: la salvedad de mutuales/cooperativas está.
    pro1125 = _nodos_con(nodes, lambda n: any(
        a.startswith("TO_proteccion") for a in _archivos(n)) and
        "1.1.2.5" in _puntos(n))
    con_salvedad = [n for n in pro1125 if "mutual" in _texto_nodo(n)
                    or "cooperativ" in _texto_nodo(n)]
    excepciones = [n for n in con_salvedad if n.get("type") == "Excepcion"]
    res["T3_pro_1_1_2_5_salvedad"] = {
        "pass": bool(con_salvedad),
        "nodos_anclados": len(pro1125),
        "nodos_con_salvedad": [{"id": n["id"], "type": n["type"],
                                "label": n["label"]} for n in con_salvedad][:6],
        "de_los_cuales_excepcion": len(excepciones),
    }
    return res


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path, default=AQUI / "salida")
    args = ap.parse_args()

    grafos = {}
    for to in TOS_ORDEN:
        p = args.salida / to / f"grafo_{to}.json"
        if not p.exists():
            print(f"falta {p} — la corrida de {to} no cerró su E2")
            return 1
        grafos[to] = json.loads(p.read_text(encoding="utf-8"))

    m = merge_grafos(grafos)
    kg = {"nodes": m["nodes"], "edges": m["edges"]}
    kg_json = json.dumps(kg, ensure_ascii=False, indent=2)
    (args.salida / "kg.json").write_text(kg_json, encoding="utf-8")
    sha = hashlib.sha256(kg_json.encode("utf-8")).hexdigest()

    tests = tests_respuesta_conocida(kg)
    (args.salida / "tests_respuesta_conocida.json").write_text(
        json.dumps(tests, ensure_ascii=False, indent=1), encoding="utf-8")

    reporte = {
        "orden_merge": list(TOS_ORDEN),
        "nodes_total": len(kg["nodes"]),
        "edges_total": len(kg["edges"]),
        "nodes_by_type": dict(Counter(n["type"] for n in kg["nodes"]).most_common()),
        "por_to_pre_merge": {to: {"nodes": len(g["nodes"]),
                                  "edges": len(g["edges"])}
                             for to, g in grafos.items()},
        "merges_cross_to": m["merges_cross_to"],
        "conflictos_properties_cross_to": m["conflictos"],
        "sha256_kg": sha,
        "tests_respuesta_conocida": {k: v["pass"] for k, v in tests.items()},
    }
    (args.salida / "reporte_ensamblado.json").write_text(
        json.dumps(reporte, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({k: reporte[k] for k in
                      ("nodes_total", "edges_total", "sha256_kg",
                       "tests_respuesta_conocida")},
                     ensure_ascii=False, indent=1))
    print(f"-> {args.salida / 'kg.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
