"""Re-sellado único de la tanda 0, §2.3 del mandato: el diff de un grafo re-sellado contra su sellado, declarado por campo
y por causa, en el formato de omisiones_cod/o2/salidas/diff_declarado_*.json, más `causas_por_campo`. Solo lee.

La cadena del sellado al re-sellado, con los cuatro grafos reproducidos byte a byte sobre copias:
  S  el sellado (a9631a64 / e22fae1a / 6e756043 / 2922b72d);
  P  el código de antes de O2 (ded41d50^) sobre la entrada de antes de R0 (1d690df3): 40c54830 / 8d747e57 en diez, y en
     desarrollo el mismo sellado; entre S y P, en diez, está R2-3 (803623a), que el sellado no tiene;
  O  el código de O2 (ded41d50) sobre la misma entrada: 710664e9 / a50210b4 / 18a2747d / 9f49d62d;
  N  el re-sellado: el código de O2 sobre la entrada de R0 (2d0f5277).
Cada fila de S→N recibe, por campo (o por presencia, si el objeto sale o entra), el paso que lo cambió:
  «R2-3» si cambia de S a P; «O2:<grupo>» si cambia de P a O, con el grupo de la fila de
  omisiones_cod/o2/salidas/diff_declarado_<grafo>.json (f, f′, C, L, G-r, H, J); «R0» si cambia de O a N, con las
  unidades de la fila de diff_declarado_contra_O2_<grafo>.json. Los nodos que G-r cambia de id se siguen con el mapa
  de ids de las filas de O2 («id nuevo» / «id viejo»). Una fila sin causa queda «sin_causa»; el control es que no haya.
Uso: python -I -B diff_contra_sellado.py --s <dir r2> --p <dir r2> --o <dir r2> --n <dir r2> --diff-o2 <json>
     --diff-r0 <json> --out <json>
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter, OrderedDict, defaultdict
from pathlib import Path

AUS = "<ausente>"


def campos(a: dict, b: dict, pre: str = "") -> list[str]:
    out = []
    for k in sorted(set(a) | set(b)):
        va, vb = a.get(k, AUS), b.get(k, AUS)
        if va == vb:
            continue
        if isinstance(va, dict) and isinstance(vb, dict) and k != "properties_no_definidas":
            out += campos(va, vb, f"{pre}{k}.")
        else:
            out.append(f"{pre}{k}")
    return out


def valor(obj: dict | None, campo: str):
    if obj is None:
        return AUS
    v = obj
    for parte in campo.split("."):
        if not isinstance(v, dict) or parte not in v:
            return AUS
        v = v[parte]
    return v


def cargar(d: Path) -> tuple[dict, dict, str]:
    b = (d / "kg.json").read_bytes()
    kg = json.loads(b)
    return ({n["id"]: n for n in kg["nodes"]}, {(e["source"], e["relation"], e["target"]): e for e in kg["edges"]},
            hashlib.sha256(b).hexdigest())


def main() -> int:
    ap = argparse.ArgumentParser()
    for x in ("s", "p", "o", "n"):
        ap.add_argument(f"--{x}", type=Path, required=True)
    ap.add_argument("--diff-o2", type=Path, required=True)
    ap.add_argument("--diff-r0", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    (Sn, Se, s_sha), (Pn, Pe, p_sha), (On, Oe, o_sha), (Nn, Ne, n_sha) = (cargar(a.s), cargar(a.p), cargar(a.o),
                                                                          cargar(a.n))
    d2 = json.loads(a.diff_o2.read_text(encoding="utf-8"))
    d0 = json.loads(a.diff_r0.read_text(encoding="utf-8"))
    assert d2["sha256_head"] == p_sha and d2["sha256_nuevo"] == o_sha, "el diff de O2 no es el de estos grafos"
    assert d0["sha256_o2"] == o_sha and d0["sha256_nuevo"] == n_sha, "el diff de R0 no es el de estos grafos"
    # mapa de ids de G-r (P → O), de las filas de O2
    ren = {}
    for f in d2["lista"]:
        if f["objeto"] == "nodo" and f["cambio"] == "sale" and (f["detalle"] or "").startswith("id nuevo "):
            ren[f["clave"]] = f["detalle"][len("id nuevo "):]
    inv = {v: k for k, v in ren.items()}
    a_o = lambda i: ren.get(i, i)  # noqa: E731
    a_p = lambda i: inv.get(i, i)  # noqa: E731
    # índice de causas de O2 y de R0 por objeto (en el espacio de O, que es el de N)
    o2_idx, r0_idx, r0_u = defaultdict(set), defaultdict(set), defaultdict(set)
    for f in d2["lista"]:
        if f["objeto"] == "nodo":
            o2_idx[("nodo", a_o(f["clave"]))].add(f["causa"])
        elif f["objeto"] == "elemento":
            nid, i = f["clave"].rsplit("#", 1)
            o2_idx[("elemento", f"{a_o(nid)}#{i}")].add(f["causa"])
            o2_idx[("nodo", a_o(nid))].add(f["causa"])
        else:
            s, r, t = f["clave"].split("|")
            o2_idx[("arista", (a_o(s), r, a_o(t)))].add(f["causa"])
    for f in d0["lista"]:
        if f["objeto"] == "arista":
            s, r, t = f["clave"].split("|")
            k = ("arista", (s, r, t))
        elif f["objeto"] == "elemento":
            k = ("elemento", f["clave"])
            r0_idx[("nodo", f["clave"].rsplit("#", 1)[0])].add("R0")
            r0_u[("nodo", f["clave"].rsplit("#", 1)[0])].update(f["unidades_r0"])
        else:
            k = ("nodo", f["clave"])
        r0_idx[k].add("R0")
        r0_u[k].update(f["unidades_r0"])

    def estados_nodo(i_sn: str) -> tuple:
        """(S, P, O, N) del nodo; i_sn es un id del espacio de S (sale) o de N (entra / cambia)."""
        i_p = a_p(i_sn) if i_sn in On or i_sn in Nn else i_sn
        i_o = a_o(i_p)
        return Sn.get(i_p), Pn.get(i_p), On.get(i_o), Nn.get(i_o), i_o

    def estados_arista(k: tuple) -> tuple:
        s, r, t = k
        kp = (a_p(s), r, a_p(t))
        ko = (a_o(kp[0]), r, a_o(kp[2]))
        return Se.get(kp), Pe.get(kp), Oe.get(ko), Ne.get(ko), ko

    def pasos(es: tuple, campo: str | None, clave_o: tuple) -> list[str]:
        """Para la presencia (campo None), `es` trae la presencia de la clave LITERAL en S, P, O y N (un nodo al que G-r
        le cambia el id sale con su id viejo y entra con el nuevo en el paso de O2); para un campo, los objetos seguidos
        con el mapa de ids. El grupo de O2 y la causa de R0 se buscan con la clave en el espacio de O."""
        s, p, o, n = es
        out = []
        dif = (lambda x, y: (x is None) != (y is None)) if campo is None else (
            lambda x, y: valor(x, campo) != valor(y, campo))
        if dif(s, p):
            out.append("R2-3")
        if dif(p, o):
            g = sorted(o2_idx.get(clave_o, set()))
            out.append("O2:" + ("+".join(g) if g else "?"))
        if dif(o, n):
            out.append("R0" if clave_o in r0_idx else "R0:?")
        return out

    filas = []

    def fila(objeto, clave, cambio, cpc: dict, campos_=None, detalle=None, unidades=None):
        todas = sorted({c for v in cpc.values() for c in v})
        sin = (not todas) or any(not v for v in cpc.values()) or any(c.endswith("?") for c in todas)
        filas.append(OrderedDict([("objeto", objeto), ("clave", clave), ("cambio", cambio),
                                  ("causa", "sin_causa" if sin else " + ".join(todas)), ("campos", campos_),
                                  ("detalle", detalle), ("causas_por_campo", cpc), ("unidades_r0", sorted(unidades or []))]))
    # nodos
    lit_n = lambda i: (Sn.get(i), Pn.get(i), On.get(i), Nn.get(i))  # noqa: E731
    for i in sorted(set(Sn) - set(Nn)):
        io = a_o(i)
        fila("nodo", i, "sale", {"presencia": pasos(lit_n(i), None, ("nodo", io))}, detalle=Sn[i]["type"]
             + (f"; G-r le da el id {io}" if io != i else ""), unidades=r0_u.get(("nodo", io)))
    for j in sorted(set(Nn) - set(Sn)):
        io = j
        fila("nodo", j, "entra", {"presencia": pasos(lit_n(j), None, ("nodo", io))}, detalle=Nn[j]["type"]
             + (f"; id viejo {a_p(j)} (G-r)" if a_p(j) != j else ""), unidades=r0_u.get(("nodo", io)))
    for i in sorted(set(Sn) & set(Nn)):
        cs = campos(Sn[i], Nn[i])
        if not cs:
            continue
        s, p, o, n, io = estados_nodo(i)
        cpc = OrderedDict()
        elementos = []
        if "properties.umbrales" in cs:
            ua, ub = (Sn[i]["properties"].get("umbrales") or []), (Nn[i]["properties"].get("umbrales") or [])
            if len(ua) == len(ub):
                cs = [c for c in cs if c != "properties.umbrales"]
                for k, (x, y) in enumerate(zip(ua, ub)):
                    d = campos(x, y)
                    if d:
                        elementos.append((k, d))
        for c in cs:
            cpc[c] = pasos((s, p, o, n), c, ("nodo", io))
        if cs:
            fila("nodo", i, "cambia", cpc, cs, Sn[i]["type"], r0_u.get(("nodo", io)))
        for k, d in elementos:
            ek = ("elemento", f"{io}#{k}")
            el = lambda x: (x or {}).get("properties", {}).get("umbrales", [None] * (k + 1))[k] if x else None  # noqa: E731
            cpc_e = OrderedDict((c, pasos((el(s), el(p), el(o), el(n)), c, ek if ek in o2_idx or ek in r0_idx
                                          else ("nodo", io))) for c in d)
            fila("elemento", f"{i}#{k}", "cambia", cpc_e, d, Sn[i]["type"], r0_u.get(("nodo", io)))
    # aristas
    lit_e = lambda k: (Se.get(k), Pe.get(k), Oe.get(k), Ne.get(k))  # noqa: E731
    for k in sorted(set(Se) - set(Ne)):
        ko = estados_arista(k)[4]
        fila("arista", "|".join(k), "sale", {"presencia": pasos(lit_e(k), None, ("arista", ko))},
             detalle=("re-tecleada por G-r: " + "|".join(ko)) if ko != k else None, unidades=r0_u.get(("arista", ko)))
    for k in sorted(set(Ne) - set(Se)):
        fila("arista", "|".join(k), "entra", {"presencia": pasos(lit_e(k), None, ("arista", k))},
             unidades=r0_u.get(("arista", k)))
    for k in sorted(set(Se) & set(Ne)):
        cs = campos(Se[k], Ne[k])
        if not cs:
            continue
        s, p, o, n, ko = estados_arista(k)
        cpc = OrderedDict((c, pasos((s, p, o, n), c, ("arista", ko))) for c in cs)
        fila("arista", "|".join(k), "cambia", cpc, cs, unidades=r0_u.get(("arista", ko)))
    cont = Counter((f["objeto"], f["cambio"], f["causa"]) for f in filas)
    por_paso = Counter(c.split(":")[0] for f in filas for c in {x for v in f["causas_por_campo"].values() for x in v})
    por_grupo_o2 = Counter(c for f in filas for c in {x for v in f["causas_por_campo"].values() for x in v}
                           if c.startswith("O2:"))
    res = OrderedDict([
        ("sha256", OrderedDict([("sellado", s_sha), ("antes_de_O2", p_sha), ("O2", o_sha), ("re_sellado", n_sha)])),
        ("nodos", [len(Sn), len(Nn)]), ("aristas", [len(Se), len(Ne)]),
        ("ids_de_G_r_en_O2", len(ren)),
        ("por_objeto_cambio_y_causa", {"|".join(x): v for x, v in sorted(cont.items())}),
        ("filas_por_paso", dict(sorted(por_paso.items()))), ("filas_por_grupo_de_O2", dict(sorted(por_grupo_o2.items()))),
        ("n_filas", len(filas)), ("sin_causa", [f for f in filas if f["causa"] == "sin_causa"]), ("lista", filas)])
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: (v if k != "sin_causa" else len(v)) for k, v in res.items() if k != "lista"},
                     ensure_ascii=False, indent=1)[:5000])
    return 0


if __name__ == "__main__":
    sys.exit(main())
