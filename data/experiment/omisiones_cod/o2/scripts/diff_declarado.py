"""U-OMISIONES-COD, O2 — el diff de un grafo r2b con el código nuevo contra el mismo grafo con el código de HEAD,
acotado y declarado por campo: cada nodo, arista y elemento de umbral que cambia, con su causa. Solo lee.

Causas (v7 y notas del 10/10/2026 al pie):
  f    la mención de sujeto con contracciones: `mencion_verificada` (y la mención guardada, el método) de las aristas de
       sujeto, y lo que se resuelve distinto por eso (un propuesto que sale, su arista, una arista nueva);
  f′   el singular «entidad» de R3: las aristas `aplica_a` de los propuestos «la entidad» que pasan al rol, los propuestos
       que salen con su `padre_sugerido`, las fusiones con una arista que ya existía;
  C    la base de los umbrales (g, g1, g2, g3): `base`, `base_destino`, `base_via`, `base_no_resuelta` de un elemento;
  L    el tramo de E1: `tramo` y `tramo_verificado` de un elemento;
  G-r  la procedencia por tramo: los nodos que cambian de punto (id nuevo; sus aristas, re-tecleadas con el id nuevo),
       la procedencia de los nodos que cambian de rol, las `establecida_en` derivadas de esos nodos, y las `remite_a`
       que entran o salen por la regla de destinos y de origen (con el agrupamiento sin el rol);
  H    el tipo de la Comunicacion: `tipo`, `numero` y `properties_no_definidas.tipo_no_derivable`;
  J    la procedencia de `remite_a`: `provenance` y `provenances` de una `remite_a` que sigue (mismo origen y destino).
Todo cambio que no cae en una regla queda «sin_causa», y el control es que no haya ninguno.
Uso: python -B diff_declarado.py <dir r2 HEAD> <dir r2 nuevo> --out <json>
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import unicodedata
from collections import Counter, OrderedDict
from pathlib import Path

CAMPOS_C = {"base", "base_destino", "base_via", "base_no_resuelta"}
CAMPOS_L = {"tramo", "tramo_verificado"}
CAMPOS_SUJ = {"mencion_verificada", "sujeto_mencion", "sujeto_mencion_modelo", "metodo_resolucion"}


def jl(p: Path) -> list[dict]:
    return [json.loads(x) for x in Path(p).read_text(encoding="utf-8").splitlines() if x.strip()]


def norm(s) -> str:
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", " ", s)).strip()


def sin_art(s) -> str:
    w = norm(s).split()
    return " ".join(w[1:] if w and w[0] in ("el", "la", "los", "las") else w)


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
    ap.add_argument("head", type=Path)
    ap.add_argument("nuevo", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    bh, bn = (a.head / "kg.json").read_bytes(), (a.nuevo / "kg.json").read_bytes()
    A, B = json.loads(bh), json.loads(bn)
    na, nb = {n["id"]: n for n in A["nodes"]}, {n["id"]: n for n in B["nodes"]}
    gr = json.loads((a.nuevo / "procedencia_g_r.json").read_text(encoding="utf-8"))
    # G-r: ids viejos y nuevos de los nodos que cambian de punto (por tipo y etiqueta)
    salen, entran = set(na) - set(nb), set(nb) - set(na)
    por_tl = {}
    for i in salen:
        por_tl.setdefault((na[i]["type"], na[i]["label"]), []).append(i)
    ren = {}
    for j in entran:
        c = por_tl.get((nb[j]["type"], nb[j]["label"]), [])
        if len(c) == 1 and na[c[0]]["type"] != "Sujeto":
            ren[c[0]] = j
    inv = {v: k for k, v in ren.items()}
    mapa = lambda x: ren.get(x, x)  # noqa: E731
    # sujetos: los propuestos que salen (f o f′ por la mención de su registro)
    nm_h = jl(a.head / "no_mapeados_sujetos.jsonl")
    prop_men = {}
    for f in nm_h:
        if f.get("id_nodo"):
            prop_men.setdefault(f["id_nodo"], set()).add(sin_art(f.get("mencion")))
    def causa_propuesto(i):
        m = prop_men.get(i, set())
        return "f′" if m and all(x == "entidad" for x in m) else "f"
    # sujetos que reciben o dejan de recibir aristas de sujeto por f o f′ (sus procedencias cambian por eso)
    eh_ = {(e["source"], e["relation"], e["target"]): e for e in A["edges"] if e["relation"] in ("aplica_a", "ejecuta")}
    en_ = {(e["source"], e["relation"], e["target"]): e for e in B["edges"] if e["relation"] in ("aplica_a", "ejecuta")}
    destinos_sujeto = {}
    for kk in set(eh_) ^ set(en_):
        e = en_.get(kk) or eh_.get(kk)
        suj = kk[2] if kk[1] == "aplica_a" else kk[0]
        c = "f′" if sin_art(e.get("sujeto_mencion")) == "entidad" else "f"
        destinos_sujeto[suj] = c if destinos_sujeto.get(suj) in (None, c) else "f y f′"
    for kk in set(eh_) & set(en_):
        if eh_[kk].get("metodo_resolucion") != en_[kk].get("metodo_resolucion") and en_[kk].get("metodo_resolucion") == "R3":
            destinos_sujeto.setdefault(kk[2], "f′")
    filas = []

    def fila(objeto, clave, cambio, causa, campos_=None, detalle=None):
        filas.append(OrderedDict([("objeto", objeto), ("clave", clave), ("cambio", cambio), ("causa", causa),
                                  ("campos", campos_), ("detalle", detalle)]))
    # ---- nodos
    for i in sorted(salen):
        if i in ren:
            fila("nodo", i, "sale", "G-r", detalle=f"id nuevo {ren[i]}")
        elif na[i]["type"] == "Sujeto" and (na[i].get("properties") or {}).get("nivel") == "propuesto":
            fila("nodo", i, "sale", causa_propuesto(i), detalle="propuesto que deja de tener filas en cuarentena")
        else:
            fila("nodo", i, "sale", "sin_causa")
    for j in sorted(entran):
        fila("nodo", j, "entra", "G-r" if j in inv else "sin_causa", detalle=f"id viejo {inv.get(j)}")
    elementos = []
    for i in sorted(set(na) & set(nb)) + sorted(ren):
        x, y = na[i], nb[mapa(i)]
        cs = campos(x, y)
        if i in ren:
            cs = [c for c in cs if c != "id"]
        if not cs:
            continue
        resto, h = [], []
        for c in cs:
            if c == "properties.umbrales":
                ua, ub = (x["properties"].get("umbrales") or []), (y["properties"].get("umbrales") or [])
                if len(ua) != len(ub):
                    resto.append(c)
                    continue
                for k, (ea, eb) in enumerate(zip(ua, ub)):
                    d = set(campos(ea, eb))
                    if not d:
                        continue
                    if d <= CAMPOS_C:
                        caus = "C"
                    elif d <= CAMPOS_L:
                        caus = "L"
                    elif d <= CAMPOS_C | CAMPOS_L:
                        caus = "C y L"
                    else:
                        caus = "sin_causa"
                    elementos.append(OrderedDict([("nodo", mapa(i)), ("i", k), ("causa", caus), ("campos", sorted(d))]))
            elif x["type"] == "Comunicacion" and c in ("properties.tipo", "properties.numero", "properties_no_definidas"):
                h.append(c)
            elif c in ("provenance", "provenances") or c.startswith("provenance."):
                resto.append(c)
            else:
                resto.append(c)
        if h:
            fila("nodo", mapa(i), "cambia", "H", h)
        prov = [c for c in resto if c in ("provenances",) or c.startswith("provenance")]
        otros = [c for c in resto if c not in prov]
        if prov:
            roles_a = [(p.get("punto"), p.get("rol_documental")) for p in x.get("provenances", [])]
            roles_b = [(p.get("punto"), p.get("rol_documental")) for p in y.get("provenances", [])]
            if x["type"] == "Sujeto" and i in destinos_sujeto:
                fila("nodo", mapa(i), "cambia", destinos_sujeto[i], prov,
                     "procedencias del sujeto: las de las aristas de sujeto que recibe o deja de recibir")
            elif i in ren or roles_a != roles_b:
                fila("nodo", mapa(i), "cambia", "G-r", prov, "punto o rol de la procedencia")
            else:
                fila("nodo", mapa(i), "cambia", "sin_causa", prov)
        if otros:
            fila("nodo", mapa(i), "cambia", "sin_causa", otros)
    # ---- aristas
    k = lambda e: (e["source"], e["relation"], e["target"])  # noqa: E731
    ea = {k(e): e for e in A["edges"]}
    eb = {k(e): e for e in B["edges"]}
    ea_m = {(mapa(s), r, mapa(t)): e for (s, r, t), e in ea.items()}
    sale_e = sorted(set(ea_m) - set(eb))
    entra_e = sorted(set(eb) - set(ea_m))
    retecleadas = {kk for kk in ea_m if kk in eb and kk not in ea}

    def causa_sujeto(e, lado):
        s, r, t = e["source"], e["relation"], e["target"]
        if r == "padre_sugerido":
            return causa_propuesto(s) if lado == "sale" else "sin_causa"
        if r in ("aplica_a", "ejecuta"):
            suj = t if r == "aplica_a" else s
            if lado == "sale" and suj in na and suj not in nb:
                return causa_propuesto(suj)
            men = sin_art(e.get("sujeto_mencion"))
            if lado == "entra" and men == "entidad" and e.get("metodo_resolucion") == "R3":
                return "f′"
            if lado == "entra":
                return "f"
        return None
    for kk in sale_e:
        e = ea_m[kk]
        c = causa_sujeto(e, "sale")
        if c is None and e["relation"] == "remite_a":
            c = "G-r"
        if c is None and (kk[0] in inv or kk[2] in inv):
            c = "G-r"
        fila("arista", "|".join(kk), "sale", c or "sin_causa")
    for kk in entra_e:
        e = eb[kk]
        c = causa_sujeto(e, "entra")
        if c is None and e["relation"] == "remite_a":
            c = "G-r"
        if c is None and (kk[0] in inv or kk[2] in inv):
            c = "G-r"
        fila("arista", "|".join(kk), "entra", c or "sin_causa")
    for kk in sorted(set(ea_m) & set(eb)):
        x, y = dict(ea_m[kk]), eb[kk]
        x["source"], x["target"] = mapa(x["source"]), mapa(x["target"])
        cs = campos(x, y)
        if not cs and kk not in retecleadas:
            continue
        if not cs:
            fila("arista", "|".join(kk), "re-tecleada", "G-r", detalle="mismo contenido con el id nuevo de un extremo")
            continue
        sujeto = set(cs) & CAMPOS_SUJ
        prov = [c for c in cs if c == "provenances" or c.startswith("provenance")]
        otros = [c for c in cs if c not in prov and c not in CAMPOS_SUJ and c != "sujeto_id_modelo"]
        if x["relation"] == "remite_a" and not otros and not sujeto:
            caus = "J"
        elif x["relation"] == "establecida_en" and not otros and not sujeto:
            caus = "G-r"
        elif sujeto and "mencion_verificada" in sujeto and not otros:
            caus = "f"
        elif x["relation"] in ("aplica_a", "ejecuta") and y.get("metodo_resolucion") == "R3" and not otros:
            caus = "f′"
        elif (kk[0] in inv or kk[2] in inv) and not otros:
            caus = "G-r"
        else:
            caus = "sin_causa"
        fila("arista", "|".join(kk), "cambia" + (" (re-tecleada)" if kk in retecleadas else ""), caus, cs)
    for e in elementos:
        fila("elemento", f"{e['nodo']}#{e['i']}", "cambia", e["causa"], e["campos"])
    cont = Counter((f["objeto"], f["cambio"].split(" ")[0], f["causa"]) for f in filas)
    res = OrderedDict([
        ("sha256_head", hashlib.sha256(bh).hexdigest()), ("sha256_nuevo", hashlib.sha256(bn).hexdigest()),
        ("nodos", [len(A["nodes"]), len(B["nodes"])]), ("aristas", [len(A["edges"]), len(B["edges"])]),
        ("ids_de_G_r", len(ren)), ("procedencia_g_r_cambia_el_punto", sum(1 for c in gr if c["punto"] != c["punto_g_r"])),
        ("por_objeto_cambio_y_causa", {"|".join(x): n for x, n in sorted(cont.items())}),
        ("sin_causa", [f for f in filas if f["causa"] == "sin_causa"]),
        ("lista", filas)])
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k2: v for k2, v in res.items() if k2 not in ("lista",)}, ensure_ascii=False, indent=1)[:5000])
    return 0


if __name__ == "__main__":
    sys.exit(main())
