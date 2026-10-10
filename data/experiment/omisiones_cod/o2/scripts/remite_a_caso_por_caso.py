"""U-OMISIONES-COD, O2 — toda `remite_a` que cambia en un grafo r2b, caso por caso y con su control (nota del 10/10/2026
al pie de la v7: «O2 mide su efecto sobre todas las `remite_a` y explica caso por caso toda arista que cambie fuera de las
78 del reagrupamiento»). Tres salidas `r2/` de la misma cadena: HEAD, O1 (G-r con el grupo partido por el rol) y O2
(G-r con el agrupamiento sin el rol). Solo lee.

  1. O1 → O2, el efecto del agrupamiento sin el rol solo:
     - las que salen (reagrupamiento): en O1 la cita (chunk, evidencia, destino) se atribuyó con «todos_los_nodos_del_punto»
       a un grupo que incluía el origen; en O2 la misma cita se atribuye con «contiene_la_unidad» a otros nodos del mismo
       punto y chunk, y no al origen (si el mismo texto también es heredado, su cita de «texto_heredado» tampoco va al
       origen);
     - las que siguen y pierden una procedencia (J): cada procedencia que se pierde es la de una cita que cumple lo mismo;
     - las que entran: tienen que ser 0.
  2. HEAD → O2, las que entran y salen, una por una, con su clase:
     - destino con id de G-r: el nodo destino cambió de punto; control: el nodo está anclado en la unidad citada de un
       lado y no del otro (sale: en HEAD sí, en O2 no; entra: al revés). Anclado es la regla de destinos del detector:
       alguna de sus procedencias tiene el mismo (to, punto) que la unidad citada (`r1_referencias.py`, `anclados`);
     - origen con id de G-r: el nodo origen cambió de punto; control: su punto es el de la cita de un lado y no del otro;
     - sin cambio de id en los extremos: la reatribución dentro del punto; control: en HEAD la cita fue a todo el punto
       («todos_los_nodos_del_punto») con el origen, y en O2 va con «contiene_la_unidad» a otros nodos, que son de G-r;
     - re-tecleadas (el mismo par con el id nuevo del otro lado): se cuentan aparte, porque no son cambios de la arista.
  Toda arista que no cumple el control de su clase va a «sin_explicar», y el control es que no haya ninguna.
Uso: python -B remite_a_caso_por_caso.py <r2 HEAD> <r2 O1> <r2 O2> --out <json>
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, OrderedDict
from pathlib import Path


def cargar(d: Path):
    kg = json.loads((d / "kg.json").read_text(encoding="utf-8"))
    reg = json.loads((d / "remisiones_registro.json").read_text(encoding="utf-8"))
    nodos = {n["id"]: n for n in kg["nodes"]}
    ra = {(e["source"], e["target"]): e for e in kg["edges"] if e["relation"] == "remite_a"}
    return nodos, reg, ra


def citas_por_clave(reg: list[dict]) -> dict:
    """(chunk_id, evidencia, destino) -> lista de (atribucion, origenes, nodos del destino)."""
    out: dict = {}
    for c in reg:
        for d in c["destinos"]:
            out.setdefault((c.get("chunk_id"), c["evidencia"], d["destino"]), []).append(
                (c.get("atribucion"), list(c["origenes"]), list(d.get("nodos") or []), c.get("procedencia", {})))
    return out


def anclado(nodo: dict | None, destino: str) -> bool:
    """¿El nodo está anclado en la unidad citada (`to::punto`)? Alguna procedencia con el mismo (to, punto)."""
    if nodo is None:
        return False
    to, u = destino.split("::", 1)
    return any(p.get("to") == to and p.get("punto") == u for p in nodo.get("provenances", []))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("head", type=Path)
    ap.add_argument("o1", type=Path)
    ap.add_argument("o2", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    nh, rh, eh = cargar(a.head)
    n1, r1, e1 = cargar(a.o1)
    n2, r2, e2 = cargar(a.o2)
    c1, c2, ch = citas_por_clave(r1), citas_por_clave(r2), citas_por_clave(rh)
    punto = lambda n: n["provenance"].get("punto")  # noqa: E731
    res = OrderedDict([("remite_a", {"head": len(eh), "o1": len(e1), "o2": len(e2)})])
    sin_explicar = []

    def control_reagrupamiento(s: str, k: tuple) -> tuple[bool, dict]:
        antes = [x for x in c1.get(k, []) if s in x[1]]
        despues = c2.get(k, [])
        d1 = [x for x in despues if x[0] != "texto_heredado"]
        ok = (bool(antes) and all(x[0] == "todos_los_nodos_del_punto" for x in antes) and bool(d1)
              and all(x[0] == "contiene_la_unidad" for x in d1) and all(s not in x[1] for x in despues)
              and all(n2[o]["provenance"].get("punto") == n1[s]["provenance"].get("punto") for x in d1 for o in x[1]))
        return ok, {"atribucion_o1": sorted({x[0] for x in antes}), "atribucion_o2": sorted({x[0] for x in despues}),
                    "en_o2_la_cita_va_a": sorted({o for x in despues for o in x[1]})}

    # 1. O1 -> O2
    salen, entran = sorted(set(e1) - set(e2)), sorted(set(e2) - set(e1))
    filas_s = []
    for s, t in salen:
        e = e1[(s, t)]
        k = (e["provenance"].get("chunk_id"), e["properties"]["evidencia"], e["properties"]["destino"])
        ok, det = control_reagrupamiento(s, k)
        f = {"source": s, "target": t, "destino": k[2], "chunk_id": k[0], "evidencia": k[1][:160],
             "punto_origen": punto(n1[s]), "rol_origen": n1[s]["provenance"].get("rol_documental"), **det}
        filas_s.append(f)
        if not ok:
            sin_explicar.append({"bloque": "o1_a_o2_sale", **f})
    filas_c = []
    for st in sorted(set(e1) & set(e2)):
        x, y = e1[st], e2[st]
        if x == y:
            continue
        s, t = st
        js = lambda L: [json.dumps(p, sort_keys=True, ensure_ascii=False) for p in L]  # noqa: E731
        perdidas = [json.loads(p) for p in js(x.get("provenances", [])) if p not in js(y.get("provenances", []))]
        ganadas = [p for p in js(y.get("provenances", [])) if p not in js(x.get("provenances", []))]
        resto = {f for f in set(x) | set(y) if f not in ("provenance", "provenances") and x.get(f) != y.get(f)}
        prim = y["provenance"] in y.get("provenances", [])
        controles = []
        for p in perdidas:
            ks = [kk for kk in c1 if kk[0] == p.get("chunk_id") and kk[2] == x["properties"]["destino"]
                  and any(s in z[1] and t in z[2] for z in c1[kk])]
            controles.append(bool(ks) and all(control_reagrupamiento(s, kk)[0] for kk in ks))
        ok = bool(perdidas) and not ganadas and not resto and prim and all(controles)
        f = {"source": s, "target": t, "destino": x["properties"]["destino"], "punto_origen": punto(n2[s]),
             "cambia_la_principal": x["provenance"] != y["provenance"],
             "procedencias_perdidas": [{kk: p.get(kk) for kk in ("chunk_id", "punto", "rol_documental")} for p in perdidas],
             "procedencias_o1": len(x.get("provenances", [])), "procedencias_o2": len(y.get("provenances", []))}
        filas_c.append(f)
        if not ok:
            sin_explicar.append({"bloque": "o1_a_o2_cambia", **f})
    res["o1_a_o2"] = OrderedDict([
        ("salen", len(salen)), ("entran", len(entran)), ("cambian", len(filas_c)),
        ("cambian_con_la_principal", sum(1 for f in filas_c if f["cambia_la_principal"])),
        ("cambian_solo_en_provenances", sum(1 for f in filas_c if not f["cambia_la_principal"])),
        ("entran_lista", [f"{s} -> {t}" for s, t in entran]),
        ("salen_lista", filas_s), ("cambian_lista", filas_c)])
    # 2. HEAD -> O2
    ids_h, ids_2 = set(nh), set(n2)
    viejos, nuevos = ids_h - ids_2, ids_2 - ids_h
    por = {}
    for i in viejos:
        por.setdefault((nh[i]["type"], nh[i]["label"]), []).append(i)
    ren = {por[(n2[j]["type"], n2[j]["label"])][0]: j for j in nuevos
           if len(por.get((n2[j]["type"], n2[j]["label"]), [])) == 1}
    ren_inv = {v: k for k, v in ren.items()}
    sale, entra = sorted(set(eh) - set(e2)), sorted(set(e2) - set(eh))
    filas, clases = [], Counter()
    for lado, pares in (("sale", sale), ("entra", entra)):
        for s, t in pares:
            src = eh if lado == "sale" else e2
            e = src[(s, t)]
            dest = e["properties"]["destino"]
            f = {"lado": lado, "source": s, "target": t, "destino": dest, "evidencia": e["properties"]["evidencia"][:160]}
            if lado == "sale" and (ren.get(s, s), ren.get(t, t)) in e2 or lado == "entra" and (ren_inv.get(s, s), ren_inv.get(t, t)) in eh:
                f["clase"] = "re-tecleada"
                clases[(lado, f["clase"])] += 1
                filas.append(f)
                continue
            ok = True
            if t in viejos or t in nuevos:
                vh = t if lado == "sale" else ren_inv.get(t)
                v2 = ren.get(t) if lado == "sale" else t
                ph = nh[vh]["provenance"].get("punto") if vh in nh else None
                p2 = n2[v2]["provenance"].get("punto") if v2 in n2 else None
                f.update({"clase": "destino con id de G-r", "punto_destino_head": ph, "punto_destino_o2": p2,
                          "en_la_unidad_head": anclado(nh.get(vh), dest), "en_la_unidad_o2": anclado(n2.get(v2), dest)})
                ok = (f["en_la_unidad_head"], f["en_la_unidad_o2"]) == ((True, False) if lado == "sale" else (False, True))
            elif s in viejos or s in nuevos:
                vh = s if lado == "sale" else ren_inv.get(s)
                v2 = ren.get(s) if lado == "sale" else s
                ph = nh[vh]["provenance"].get("punto") if vh in nh else None
                p2 = n2[v2]["provenance"].get("punto") if v2 in n2 else None
                pc = e["provenance"].get("punto")
                f.update({"clase": "origen con id de G-r", "punto_origen_head": ph, "punto_origen_o2": p2,
                          "punto_de_la_cita": pc})
                ok = (ph == pc and p2 != pc) if lado == "sale" else (p2 == pc and ph != pc)
            else:
                k = None
                cands = [kk for kk in ch if kk[1] == e["properties"]["evidencia"] and kk[2] == dest
                         and any(s in z[1] for z in ch[kk])] if lado == "sale" else []
                antes = [z for kk in cands for z in ch[kk] if s in z[1]]
                despues = [z for kk in cands for z in c2.get(kk, [])]
                movidos = sorted({o for z in despues for o in z[1]})
                f.update({"clase": "sin cambio de id en los extremos", "punto_origen": punto(nh[s]) if s in nh else None,
                          "atribucion_head": sorted({z[0] for z in antes}), "atribucion_o2": sorted({z[0] for z in despues}),
                          "en_o2_la_cita_va_a": movidos, "esos_nodos_son_de_G_r": all(o in nuevos for o in movidos)})
                ok = (lado == "sale" and f["atribucion_head"] == ["todos_los_nodos_del_punto"]
                      and f["atribucion_o2"] == ["contiene_la_unidad"] and bool(movidos) and s not in movidos
                      and f["esos_nodos_son_de_G_r"])
            clases[(lado, f["clase"])] += 1
            filas.append(f)
            if not ok:
                sin_explicar.append({"bloque": "head_a_o2", **f})
    res["head_a_o2"] = OrderedDict([("salen", len(sale)), ("entran", len(entra)),
                                    ("por_clase", {f"{l}|{c}": n for (l, c), n in sorted(clases.items())}),
                                    ("lista", filas)])
    res["sin_explicar"] = sin_explicar
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    vista = OrderedDict([("remite_a", res["remite_a"]),
                         ("o1_a_o2", {k: v for k, v in res["o1_a_o2"].items() if not k.endswith("_lista")}),
                         ("head_a_o2", {k: v for k, v in res["head_a_o2"].items() if k != "lista"}),
                         ("sin_explicar", len(sin_explicar))])
    print(json.dumps(vista, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
