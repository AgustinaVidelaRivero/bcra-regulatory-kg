"""Re-sellado único de la tanda 0, §2.2 del mandato: el diff de un grafo r2b re-sellado contra el mismo grafo de O2 (el
código de U-OMISIONES-COD sin las salidas de R0), declarado por campo y con su causa, en el formato de
omisiones_cod/o2/salidas/diff_declarado_*.json (objeto, clave, cambio, causa, campos, detalle), más dos claves por fila:
`unidades_r0` (las unidades de R0 que lo explican) y `via` (la regla). Solo lee.

Entre los dos grafos cambia solo la entrada de R0: el mismo código (ded41d50), y en corpus_tanda0/salida_r2b los 49
renglones que R0 anexó en 8 archivos, todos de sus 20 unidades (r0/controles/r0_f2_control_anexo.json). Las reglas de
causa, en orden; la primera que vale se declara:
  procedencia     el objeto (nodo, arista o elemento de umbral) tiene procedencia en una unidad de R0, en el grafo de
                  O2 o en el re-sellado (la unidad o una de sus partes, `<unidad>::parteN`);
  procedencia_agregada  un nodo que sigue y cuya lista de procedencias cambia solo en entradas de unidades de R0 (un
                  Sujeto o un TextoOrdenado que agrega las de las aristas que recibe);
  extremo         una arista cuyo origen o destino tiene procedencia en una unidad de R0, en cualquiera de los dos grafos;
  sin_causa       ninguna de las anteriores. El control es que no quede ninguna fila sin causa.
Uso: python -I -B diff_r0.py <dir r2 de O2> <dir r2 re-sellado> --unidades-r0 <json con la lista> --out <json>
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter, OrderedDict
from pathlib import Path


def provs(x: dict) -> list:
    return [p for p in [x.get("provenance")] + (x.get("provenances") or []) if p]


def chunks_de(x: dict | None) -> set:
    return {p.get("chunk_id") for p in provs(x or {}) if p.get("chunk_id")}


def campos(a: dict, b: dict, pre: str = "") -> list[str]:
    out = []
    for k in sorted(set(a) | set(b)):
        va, vb = a.get(k, "<ausente>"), b.get(k, "<ausente>")
        if va == vb:
            continue
        if isinstance(va, dict) and isinstance(vb, dict) and k != "properties_no_definidas":
            out += campos(va, vb, f"{pre}{k}.")
        else:
            out.append(f"{pre}{k}")
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("o2", type=Path)
    ap.add_argument("nuevo", type=Path)
    ap.add_argument("--unidades-r0", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    U = sorted(json.loads(a.unidades_r0.read_text(encoding="utf-8")))

    def de_r0(chs: set) -> list[str]:
        return sorted({u for u in U for c in chs if c == u or c.startswith(u + "::")})

    ba, bb = (a.o2 / "kg.json").read_bytes(), (a.nuevo / "kg.json").read_bytes()
    A, B = json.loads(ba), json.loads(bb)
    na, nb = {n["id"]: n for n in A["nodes"]}, {n["id"]: n for n in B["nodes"]}
    filas = []

    def fila(objeto, clave, cambio, causa, campos_=None, detalle=None, unidades=None, via=None):
        filas.append(OrderedDict([("objeto", objeto), ("clave", clave), ("cambio", cambio), ("causa", causa),
                                  ("campos", campos_), ("detalle", detalle), ("unidades_r0", unidades or []),
                                  ("via", via)]))

    def causa_nodo(i: str) -> tuple[str, list, str | None]:
        u = de_r0(chunks_de(na.get(i)) | chunks_de(nb.get(i)))
        return ("R0", u, "procedencia") if u else ("sin_causa", [], None)

    nodo_r0 = {}
    for i in sorted(set(na) - set(nb)):
        c, u, v = causa_nodo(i)
        nodo_r0[i] = u
        fila("nodo", i, "sale", c, detalle=na[i]["type"], unidades=u, via=v)
    for i in sorted(set(nb) - set(na)):
        c, u, v = causa_nodo(i)
        nodo_r0[i] = u
        fila("nodo", i, "entra", c, detalle=nb[i]["type"], unidades=u, via=v)
    for i in sorted(set(na) & set(nb)):
        x, y = na[i], nb[i]
        cs = campos(x, y)
        if not cs:
            continue
        u = de_r0(chunks_de(x) | chunks_de(y))
        nodo_r0[i] = u
        elementos = []
        if "properties.umbrales" in cs:
            ua, ub = (x["properties"].get("umbrales") or []), (y["properties"].get("umbrales") or [])
            if len(ua) == len(ub):
                cs = [c for c in cs if c != "properties.umbrales"]
                for k, (ea, eb) in enumerate(zip(ua, ub)):
                    d = campos(ea, eb)
                    if d:
                        elementos.append((k, d))
        if cs:
            if u:
                fila("nodo", i, "cambia", "R0", cs, x["type"], u, "procedencia")
            else:
                fila("nodo", i, "cambia", "sin_causa", cs, x["type"])
        for k, d in elementos:
            fila("elemento", f"{i}#{k}", "cambia", "R0" if u else "sin_causa", d, x["type"], u,
                 "procedencia" if u else None)
    # Sujeto o TextoOrdenado sin procedencia propia de R0 pero cuya lista cambia solo en entradas de R0: se revisa abajo
    for f in filas:
        if f["objeto"] == "nodo" and f["cambio"] == "cambia" and f["causa"] == "sin_causa":
            x, y = na[f["clave"]], nb[f["clave"]]
            sa = {json.dumps(p, sort_keys=True, ensure_ascii=False) for p in provs(x)}
            sb = {json.dumps(p, sort_keys=True, ensure_ascii=False) for p in provs(y)}
            dif = [json.loads(s) for s in sa ^ sb]
            u = de_r0({p.get("chunk_id") for p in dif if p.get("chunk_id")})
            solo_prov = all(c == "provenances" or c.startswith("provenance") for c in f["campos"])
            if dif and solo_prov and len(u) and all(de_r0({p.get("chunk_id")}) for p in dif):
                f["causa"], f["unidades_r0"], f["via"] = "R0", u, "procedencia_agregada"
                nodo_r0[f["clave"]] = u
    # aristas
    k = lambda e: (e["source"], e["relation"], e["target"])  # noqa: E731
    ea, eb = {k(e): e for e in A["edges"]}, {k(e): e for e in B["edges"]}

    def causa_arista(kk, ex, ey) -> tuple[str, list, str | None]:
        u = de_r0(chunks_de(ex) | chunks_de(ey))
        if u:
            return "R0", u, "procedencia"
        s, _, t = kk
        u = de_r0(chunks_de(na.get(s)) | chunks_de(nb.get(s)) | chunks_de(na.get(t)) | chunks_de(nb.get(t)))
        if u:
            return "R0", u, "extremo"
        return "sin_causa", [], None

    for kk in sorted(set(ea) - set(eb)):
        c, u, v = causa_arista(kk, ea[kk], None)
        fila("arista", "|".join(kk), "sale", c, unidades=u, via=v)
    for kk in sorted(set(eb) - set(ea)):
        c, u, v = causa_arista(kk, None, eb[kk])
        fila("arista", "|".join(kk), "entra", c, unidades=u, via=v)
    for kk in sorted(set(ea) & set(eb)):
        cs = campos(ea[kk], eb[kk])
        if not cs:
            continue
        c, u, v = causa_arista(kk, ea[kk], eb[kk])
        fila("arista", "|".join(kk), "cambia", c, cs, unidades=u, via=v)
    cont = Counter((f["objeto"], f["cambio"], f["causa"], f["via"] or "-") for f in filas)
    por_unidad = Counter(u for f in filas for u in f["unidades_r0"])
    res = OrderedDict([
        ("sha256_o2", hashlib.sha256(ba).hexdigest()), ("sha256_nuevo", hashlib.sha256(bb).hexdigest()),
        ("nodos", [len(A["nodes"]), len(B["nodes"])]), ("aristas", [len(A["edges"]), len(B["edges"])]),
        ("unidades_r0", U),
        ("por_objeto_cambio_causa_y_via", {"|".join(x): n for x, n in sorted(cont.items())}),
        ("filas_por_unidad_r0", dict(sorted(por_unidad.items()))),
        ("n_filas", len(filas)),
        ("sin_causa", [f for f in filas if f["causa"] == "sin_causa"]),
        ("lista", filas)])
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k2: (v if k2 != "sin_causa" else len(v)) for k2, v in res.items() if k2 != "lista"},
                     ensure_ascii=False, indent=1)[:4000])
    return 0


if __name__ == "__main__":
    sys.exit(main())
