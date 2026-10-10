"""U-OMISIONES-COD, O1 — grupos J, A (en el ensamblado), D (h) y K sobre las salidas `r2/` de la etapa completa,
contra la etapa sin J ni A, h y K. Solo lee.

J: por cada `remite_a`, la procedencia principal antes y después, con su causa: «tramo_del_propio_origen» (cambia el
tramo por el de la procedencia del nodo de origen con la misma clave), «marca_sin_tramo» (cita del texto heredado:
`tramo_verificado = ausente`), «otros_campos_del_origen» (misma clave y mismo tramo, otros campos), «igual». Controla
que origen, destino y evidencia no cambien y que cada procedencia nueva sea una de las del origen o lleve la marca.
Uso: python -B medir_J_A_h_K.py <dir r2 antes> <dir r2 después> --out <json>
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, OrderedDict
from pathlib import Path

CLAVE = ("to", "punto", "rol_documental", "chunk_id")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("antes", type=Path)
    ap.add_argument("despues", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    A = json.loads((a.antes / "kg.json").read_text(encoding="utf-8"))
    B = json.loads((a.despues / "kg.json").read_text(encoding="utf-8"))
    nb = {n["id"]: n for n in B["nodes"]}
    k = lambda e: (e["source"], e["relation"], e["target"])  # noqa: E731
    ea = {k(e): e for e in A["edges"] if e["relation"] == "remite_a"}
    eb = {k(e): e for e in B["edges"] if e["relation"] == "remite_a"}
    res = OrderedDict([("remite_a", [len(ea), len(eb)]), ("mismas_aristas", set(ea) == set(eb))])
    causa, control, malas = Counter(), Counter(), []
    for key in sorted(ea):
        x, y = ea[key], eb[key]
        control["misma_evidencia_y_destino"] += x.get("properties") == y.get("properties")
        pa, pb = x["provenance"], y["provenance"]
        propias = nb[key[0]].get("provenances", [])
        if pb.get("tramo_verificado") == "ausente" and pb.get("tramo") is None:
            c = "marca_sin_tramo"
        elif pa == pb:
            c = "igual"
        elif {q: pa.get(q) for q in CLAVE} == {q: pb.get(q) for q in CLAVE} and pa.get("tramo") != pb.get("tramo"):
            c = "tramo_del_propio_origen"
        elif {q: pa.get(q) for q in CLAVE} == {q: pb.get(q) for q in CLAVE}:
            c = "otros_campos_del_origen"
        else:
            c = "otra_clave"
        causa[c] += 1
        es_propia = any(all(pb.get(q) == p.get(q) for q in pb if q not in ("chunk_id",)) for p in propias) \
            or c == "marca_sin_tramo"
        control["procedencia_del_propio_origen_o_marca"] += es_propia
        if not es_propia and len(malas) < 10:
            malas.append({"arista": "|".join(key), "procedencia": pb})
        control["provenances_cambia"] += x.get("provenances") != y.get("provenances")
    res["por_causa"] = dict(causa)
    res["controles"] = dict(control)
    res["no_propias_ejemplos"] = malas
    sin_tramo = lambda E: sum(1 for e in E.values() for p in e.get("provenances", []) if p.get("tramo") is None)  # noqa: E731
    res["entradas_de_provenances_sin_tramo"] = [sin_tramo(ea), sin_tramo(eb)]
    rep = json.loads((a.despues / "reporte_ensamblado_r2.json").read_text(encoding="utf-8"))
    res["A_reporte"] = rep.get("omisiones")
    res["A_supuestos_en_norma"] = rep.get("supuestos_en_norma")
    res["h_aristas_por_origen"] = rep.get("aristas_por_origen")
    res["h_total_aristas"] = rep.get("edges_total")
    res["K_irresolubles_por_causa"] = rep["remite_a"].get("irresolubles_por_causa")
    res["K_citas_irresolubles"] = rep["remite_a"].get("citas_irresolubles")
    res["H_tipo"] = Counter(str(n["properties"].get("tipo")) for n in B["nodes"] if n["type"] == "Comunicacion")
    res["H_marca"] = sum(1 for n in B["nodes"] if n["type"] == "Comunicacion"
                         and (n.get("properties_no_definidas") or {}).get("tipo_no_derivable"))
    res["H_sin_tratar"] = sum(1 for n in B["nodes"] if n["type"] == "Comunicacion" and not n["properties"].get("tipo")
                              and not (n.get("properties_no_definidas") or {}).get("tipo_no_derivable"))
    res["validacion_modelos_r2"] = {kk: rep["validacion_modelos_r2"][kk] for kk in
                                    ("nodos_fuera_del_modelo", "aristas_fuera_del_modelo")}
    res["doble_corrida_byte_identica"] = rep.get("doble_corrida_byte_identica")
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(res, ensure_ascii=False, indent=1, default=dict) + "\n", encoding="utf-8")
    print(json.dumps(res, ensure_ascii=False, indent=1, default=dict)[:6000])
    return 0


if __name__ == "__main__":
    sys.exit(main())
