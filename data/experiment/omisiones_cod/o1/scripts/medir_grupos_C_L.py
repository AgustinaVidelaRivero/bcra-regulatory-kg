"""U-OMISIONES-COD, O1 — grupos C (g, g1, g2, g3) y L, elemento por elemento, entre dos salidas `r2/` del ensamblado
que solo difieren en esos dos grupos (antes: código sin C ni L; después: con los dos). Solo lee.

Para cada elemento de umbral (nodo, posición en la lista), los campos que cambian. C: `base`, `base_destino`,
`base_via`, `base_no_resuelta`; L: `tramo`, `tramo_verificado`. Cualquier otro campo que cambie es un defecto.
Con --premedicion-L, cruza el tramo nuevo con la pre-medición de la mesa (premedicion_tramo_e1_mesa.json).
Uso: python -B medir_grupos_C_L.py <dir r2 antes> <dir r2 después> --out <json> [--premedicion-L <json>]
     [--detector <ruta a pyd_r2/code de la copia>]
"""
from __future__ import annotations

import argparse
import json
import statistics
import sys
from collections import Counter, OrderedDict
from pathlib import Path

CAMPOS_C = ("base", "base_destino", "base_via", "base_no_resuelta")
CAMPOS_L = ("tramo", "tramo_verificado")
CORRECTAS_HOY = (("cla::3.7", 4), ("cap::3.2.1.1", 1), ("polcre::2.1.9", 1), ("cap::4.2.1.2", 1))


def elementos(kg: dict) -> dict:
    out = {}
    for n in kg["nodes"]:
        for i, el in enumerate((n.get("properties") or {}).get("umbrales") or []):
            out[(n["id"], i)] = (n, el)
    return out


def es_validador(el: dict) -> bool:
    return str(el.get("regla_comparacion") or "").startswith("limite_relativo:")


def estado_base(el: dict) -> str:
    if not el.get("base"):
        return "sin_base"
    return "resuelta" if el.get("base_destino") else ("marcada" if el.get("base_no_resuelta") else "sin_destino_ni_marca")


def chunk_de(n: dict) -> str:
    return (n.get("provenance") or {}).get("chunk_id") or ""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("antes", type=Path)
    ap.add_argument("despues", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--premedicion-L", dest="pre_l", type=Path, default=None)
    ap.add_argument("--detector", type=Path, default=None)
    a = ap.parse_args()
    A = json.loads((a.antes / "kg.json").read_text(encoding="utf-8"))
    B = json.loads((a.despues / "kg.json").read_text(encoding="utf-8"))
    ea, eb = elementos(A), elementos(B)
    assert set(ea) == set(eb), "las listas de umbrales no tienen los mismos elementos"
    res = OrderedDict()
    filas_c, filas_l, otros = [], [], []
    for k in sorted(ea):
        (na, xa), (nb, xb) = ea[k], eb[k]
        dif = sorted(c for c in set(xa) | set(xb) if xa.get(c) != xb.get(c))
        if not dif:
            continue
        ajenos = [c for c in dif if c not in CAMPOS_C + CAMPOS_L]
        if ajenos:
            otros.append({"nodo": k[0], "i": k[1], "campos": ajenos})
        if set(dif) & set(CAMPOS_C):
            ant, nue = estado_base(xa), estado_base(xb)
            if nue == "sin_base":
                motivo = "g1"
            elif ant == "resuelta" and nue == "marcada":
                motivo = "g2" if (xa.get("base_via") == "remision") else "g3"
            elif es_validador(xa):
                motivo = "g"
            else:
                motivo = "otro"
            filas_c.append({"nodo": k[0], "i": k[1], "chunk_id": chunk_de(na), "origen": "validador" if es_validador(xa)
                            else xa.get("origen"), "motivo": motivo, "estado_antes": ant, "estado_despues": nue,
                            "base": xa.get("base"), "destino_antes": xa.get("base_destino"),
                            "destino_despues": xb.get("base_destino"), "via_despues": xb.get("base_via")})
        if set(dif) & set(CAMPOS_L):
            filas_l.append({"nodo": k[0], "i": k[1], "chunk_id": chunk_de(na), "origen": xa.get("origen"),
                            "cuantia": xa.get("tramo"), "tramo_e1": xb.get("tramo"),
                            "verificado_antes": xa.get("tramo_verificado"), "verificado_despues": xb.get("tramo_verificado"),
                            "valor": xb.get("valor"), "unidad": xb.get("unidad")})
    res["campos_ajenos_que_cambian"] = otros
    # --- C
    con_base_antes = Counter(estado_base(x) for _, x in ea.values() if x.get("base"))
    todos_antes = Counter(estado_base(x) for k, (_, x) in ea.items() if x.get("base") or estado_base(eb[k][1]) != "sin_base")
    despues = Counter(estado_base(eb[k][1]) for k, (_, x) in ea.items() if x.get("base"))
    res["C"] = OrderedDict([
        ("elementos_con_base_antes", sum(con_base_antes.values())), ("antes", dict(con_base_antes)),
        ("despues_de_esos_elementos", dict(despues)),
        ("cambian", len(filas_c)), ("por_motivo", dict(Counter(f["motivo"] for f in filas_c))),
        ("g_por_resultado", dict(Counter(f["estado_despues"] for f in filas_c if f["motivo"] == "g"))),
        ("resueltas_nuevas", sorted(f"{f['chunk_id']} -> {f['destino_despues']}" for f in filas_c
                                    if f["estado_despues"] == "resuelta")),
        ("g2_y_g3", [f for f in filas_c if f["motivo"] in ("g2", "g3")]),
        ("resueltas_despues", sorted(f"{chunk_de(eb[k][0])} -> {eb[k][1].get('base_destino')}"
                                     for k in eb if estado_base(eb[k][1]) == "resuelta")),
        ("control_cap_2_3_1", [estado_base(eb[k][1]) for k in eb if chunk_de(eb[k][0]) == "cap::2.3.1"
                               and eb[k][1].get("base")]),
        ("control_correctas_de_hoy", {c: [estado_base(eb[k][1]) + ":" + str(eb[k][1].get("base_destino"))
                                          for k in eb if chunk_de(eb[k][0]) == c and ea[k][1].get("base_destino")]
                                      for c, _ in CORRECTAS_HOY}),
        ("lista", filas_c)])
    # --- L
    if a.detector is not None:
        sys.path.insert(0, str(a.detector))
        import reglas_comparacion as RCMP  # noqa: PLC0415
        assert Path(RCMP.__file__).resolve().is_relative_to(a.detector.resolve().parents[3])
        mal = []
        for f in filas_l:
            cs = RCMP.detectar_cuantias(f["tramo_e1"])
            if not any(c.texto == f["cuantia"] for c in cs):
                mal.append({k2: f[k2] for k2 in ("nodo", "i", "cuantia", "tramo_e1")})
        res["L_control_contiene_la_cuantia"] = {"sin_la_cuantia_detectada": len(mal), "lista": mal[:20]}
    crec = [len(f["tramo_e1"]) - len(f["cuantia"] or "") for f in filas_l]
    largo = [len(f["tramo_e1"]) for f in filas_l]
    por_nodo = Counter()
    for f in filas_l:
        por_nodo[f["nodo"]] += len(f["tramo_e1"]) - len(f["cuantia"] or "")
    compartidos = Counter((f["nodo"], f["tramo_e1"]) for f in filas_l)
    res["L"] = OrderedDict([
        ("elementos_que_cambian", len(filas_l)), ("por_origen", dict(Counter(f["origen"] for f in filas_l))),
        ("no_cambian_por_origen", dict(Counter("validador" if es_validador(x) else str(x.get("origen"))
                                               for k, (_, x) in ea.items()
                                               if not any(f["nodo"] == k[0] and f["i"] == k[1] for f in filas_l)))),
        ("tramo_verificado_antes", dict(Counter(f["verificado_antes"] for f in filas_l))),
        ("tramo_verificado_despues", dict(Counter(f["verificado_despues"] for f in filas_l))),
        ("elementos_en_tramos_compartidos", sum(n for n in compartidos.values() if n > 1)),
        ("tramos_compartidos", sum(1 for n in compartidos.values() if n > 1)),
        ("crecimiento_por_elemento", {"mediana": statistics.median(crec), "max": max(crec), "suma": sum(crec)} if crec else None),
        ("largo_del_tramo_nuevo", {"mediana": statistics.median(largo), "max": max(largo)} if largo else None),
        ("crecimiento_por_nodo", {"nodos": len(por_nodo), "mediana": statistics.median(por_nodo.values()),
                                  "max": max(por_nodo.values()), "suma": sum(por_nodo.values())} if por_nodo else None)])
    if a.pre_l is not None:
        pre = json.loads(a.pre_l.read_text(encoding="utf-8"))
        mesa = {(f["nodo"], f["i"]): f for f in pre["filas"]}
        mio = {(f["nodo"], f["i"]): f for f in filas_l}
        cru = Counter()
        difs = []
        for k in sorted(set(mesa) | set(mio)):
            m, y = mesa.get(k), mio.get(k)
            if m is None or y is None:
                cru["solo_en_" + ("mesa" if y is None else "o1")] += 1
                difs.append({"nodo": k[0], "i": k[1], "mesa": m, "o1": y and {kk: y[kk] for kk in ("cuantia", "tramo_e1")}})
                continue
            if m.get("estado") != "ok":
                cru["mesa_sin_tramo"] += 1
                difs.append({"nodo": k[0], "i": k[1], "mesa": m, "o1": {kk: y[kk] for kk in ("cuantia", "tramo_e1")}})
            elif m["tramo_e1"] == y["tramo_e1"]:
                cru["mismo_tramo"] += 1
            else:
                cru["otro_tramo"] += 1
                difs.append({"nodo": k[0], "i": k[1], "mesa": m["tramo_e1"], "o1": y["tramo_e1"], "cuantia": y["cuantia"]})
        res["L_cruce_con_la_premedicion_de_la_mesa"] = {"conteos_mesa": pre["conteos"], "cruce": dict(cru),
                                                        "diferencias": difs}
    res["L_lista"] = filas_l
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    vista = {k: v for k, v in res.items() if k not in ("L_lista",)}
    vista["C"] = {k: v for k, v in res["C"].items() if k not in ("lista", "resueltas_despues")}
    print(json.dumps(vista, ensure_ascii=False, indent=1)[:9000])
    return 0


if __name__ == "__main__":
    sys.exit(main())
