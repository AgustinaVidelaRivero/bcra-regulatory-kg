"""U-REEXT-T0, T3, punto 1 (decisión 3 de la autora): la declaración de las unidades partidas por corte y de las
reparadas, junto al reporte del ensamblado r2b. reporte_ensamblado_r2.json (tanda0/code/ensamblar_tanda0.py, código del
pipeline que T3 no toca) no las declara; este archivo las cuenta aparte, con la marca de su registro de E1.

Lee la salida de la corrida (particiones_por_corte.json, extracciones_e1.jsonl last-wins y finales.jsonl de cada TO) y
el kg.json del ensamblado; escribe <ens>/r2/declaracion_partes_y_reparadas.json. Determinístico, USD 0, sin red.

Uso (desde la raíz del repo o de una copia): python -B declaracion_partes_reparadas.py --salida-r2b DIR --ens DIR
"""
import argparse
import hashlib
import json
from collections import Counter, OrderedDict
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--salida-r2b", type=Path, required=True)
ap.add_argument("--ens", type=Path, required=True)
a = ap.parse_args()
man = json.loads((a.ens / "r2" / "reporte_ensamblado_r2.json").read_text(encoding="utf-8"))["manifiesto"]
tos = man["orden_corrida"]
kg_path = a.ens / "r2" / "kg.json"
kg = json.loads(kg_path.read_text(encoding="utf-8"))


def last_wins(p: Path) -> dict:
    out = {}
    if p.exists():
        for x in p.read_text(encoding="utf-8").splitlines():
            if x.strip():
                r = json.loads(x)
                out[r["chunk_id"]] = r
    return out


def nodos_y_aristas(chunk_ids: set) -> dict:
    """Nodos y aristas con alguna procedencia en esos chunks; cuántos llevan la marca de la cola humana."""
    def toca(x):
        return any((p or {}).get("chunk_id") in chunk_ids for p in [x.get("provenance")] + (x.get("provenances") or []))
    ns = [n for n in kg["nodes"] if toca(n)]
    es = [e for e in kg["edges"] if toca(e)]
    cola = lambda x: (x.get("properties") or {}).get("cola_humana") == "true"
    return OrderedDict([("nodos", len(ns)), ("nodos_con_marca_de_cola", sum(map(cola, ns))),
                        ("nodos_por_tipo", dict(sorted(Counter(n["type"] for n in ns).items()))),
                        ("aristas", len(es)), ("aristas_con_marca_de_cola", sum(map(cola, es)))])


partidas, reparadas = OrderedDict(), OrderedDict()
for to in tos:
    d = a.salida_r2b / to
    p = d / "particiones_por_corte.json"
    e1, fin = last_wins(d / "extracciones_e1.jsonl"), last_wins(d / "finales.jsonl")
    if p.exists():
        for cid, v in json.loads(p.read_text(encoding="utf-8")).items():
            partes = [x["id"] for x in v["partes"]]
            partidas[cid] = OrderedDict([
                ("to", to), ("registro_e1_de_la_unidad", (e1.get(cid) or {}).get("error")),
                ("informe", v["informe"]),
                ("partes", OrderedDict((x, OrderedDict([("chars_propio", next(y["chars_propio"] for y in v["partes"]
                                                                              if y["id"] == x)),
                                                        ("error_e1", (e1.get(x) or {}).get("error")),
                                                        ("reparacion_forma", (e1.get(x) or {}).get("reparacion_forma")),
                                                        ("estado_e3", (fin.get(x) or {}).get("estado")),
                                                        ("en_el_grafo", nodos_y_aristas({x}))])) for x in partes)),
                ("en_el_grafo_por_la_unidad_entera", nodos_y_aristas({cid}))])
    for cid, r in e1.items():
        if "reparacion_forma" in r:
            reparadas[cid] = OrderedDict([("to", to), ("reparacion_forma", r["reparacion_forma"]),
                                          ("error_e1", r.get("error")), ("estado_e3", (fin.get(cid) or {}).get("estado")),
                                          ("en_el_grafo", nodos_y_aristas({cid}))])
out = OrderedDict([
    ("grafo", man["nombre"]), ("kg_sha256", hashlib.sha256(kg_path.read_bytes()).hexdigest()),
    ("nota", "reporte_ensamblado_r2.json no declara las unidades partidas por corte ni las reparadas; se declaran acá "
             "(decisión 3 de la autora sobre T3). La unidad partida entra al E2 r2 por sus partes; la cola humana no "
             "ingresa al grafo como aceptada: sus nodos van marcados (properties.cola_humana)."),
    ("particionadas_por_corte", partidas), ("n_particionadas", len(partidas)),
    ("reparadas_forma", reparadas), ("n_reparadas", len(reparadas))])
dest = a.ens / "r2" / "declaracion_partes_y_reparadas.json"
dest.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps({"escrito": str(dest), "particionadas": list(partidas), "reparadas": list(reparadas)}, ensure_ascii=False))
