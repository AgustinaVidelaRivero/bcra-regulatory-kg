"""
r1_e4.py — B1.2: E4 DETERMINÍSTICO (sin LLM) sobre el grafo ya fusionado
cross-TO (salida de r1_invariantes.merge_grafos_guardado).

(a) resolver_propuestos: Sujeto propuesto (nivel=propuesto, cuarentena) →
    id del catálogo cerrado (esquema_v2_clases.json: 65 clases/instancias +
    5 roles) SOLO por criterios de igualdad declarados, en este orden y sin
    ambigüedad (si dos criterios apuntan a ids distintos → cuarentena con
    motivo "ambiguo"):
      label_exacto          norm(label) == norm(label_catálogo)
      alias_exacto          norm(label) == norm(alias declarado)
      id_slug               slug(label) == slug del id del catálogo
      label_singularizado   norm(label sin paréntesis), singularizando cada
                            token, == ídem del label del catálogo
      alias_en_parentesis   la sigla entre paréntesis del label es alias
                            declarado Y (el padre_sugerido coincide con ese
                            id O no hay padre_sugerido)
    Lo que no resuelve queda en cuarentena tal cual (nivel=propuesto,
    cuarentena=true, padre_sugerido si lo hubo). NUNCA se crea una clase.
    Al resolver: el nodo propuesto desaparece, su provenance se acumula en
    el nodo del catálogo (se crea desde el catálogo si no existía en el
    grafo), sus aristas se re-apuntan (dedup de triplas con provenances
    acumuladas) y el nodo del catálogo recibe `alias_resueltos` (lista) para
    conservar el alias (principio 2.e: merge aditivo, reversible, registrado).

(b) canonizar_texto_ordenado: un único nodo TextoOrdenado por TO, con id y
    `archivo` derivados de la provenance (archivo del PDF según E0). Todo
    otro nodo TextoOrdenado cuyas provenances pertenecen a un TO (p. ej. el
    emitido por ric::4.1.1.4 con archivo="normas sobre Capitales mínimos…")
    se elimina y sus aristas se re-apuntan al canónico, con registro.

(c) filtrar_conflictos: de los conflictos de properties (intra-TO de E2 +
    cross-TO del merge), `materia`/`version` de TextoOrdenado salen del
    registro de conflictos y quedan como VARIANTES (insumo descriptivo);
    el resto (Operacion.tipo, *.descripcion, …) se persiste como
    conflictos REALES, sin resolver (insumo de un E4-LLM futuro).
"""

from __future__ import annotations

import re
from copy import deepcopy

import r1_comun as C
from e2_lib import slugify_full                    # noqa: E402 (se importa)

PROPS_VARIANTE_TO = ("materia", "version")


# ----------------------------------------------------------------------- #
# (a) resolución de propuestos                                            #
# ----------------------------------------------------------------------- #
def _singular(w: str) -> str:
    if len(w) > 4 and w.endswith("es") and w[-3] in "lrndzsjy":
        return w[:-2]
    if len(w) > 3 and w.endswith("s"):
        return w[:-1]
    return w


def _norm_sing(s: str) -> str:
    return " ".join(_singular(w) for w in C.norm(s).split())


def _sin_parentesis(s: str) -> str:
    return re.sub(r"\s*\([^)]*\)", "", s or "")


def _parentesis(s: str) -> str | None:
    m = re.search(r"\(([^)]+)\)", s or "")
    return m.group(1) if m else None


def indice_catalogo(catalogo: dict) -> dict[tuple[str, str], str]:
    """(criterio, clave) → id del catálogo. Construido una sola vez."""
    idx: dict[tuple[str, str], str] = {}

    def put(k: tuple[str, str], i: str) -> None:
        # Si dos entradas del catálogo colisionan en una clave, la clave se
        # marca ambigua y no resuelve (nunca se elige en silencio).
        if k in idx and idx[k] != i:
            idx[k] = "__AMBIGUO__"
        else:
            idx.setdefault(k, i)

    entradas = [(e["id"], e["label"], e.get("alias") or []) for e in catalogo["clases"]]
    entradas += [(r["id"], r["label"], []) for r in catalogo["roles"]]
    for i, label, alias in entradas:
        put(("label_exacto", C.norm(label)), i)
        put(("id_slug", i[len("Sujeto_"):]), i)
        put(("label_singularizado", _norm_sing(_sin_parentesis(label))), i)
        for a in alias:
            put(("alias_exacto", C.norm(a)), i)
    return idx


def resolver_label(label: str, padre_sugerido: str | None,
                   idx: dict[tuple[str, str], str]) -> tuple[str | None, str, list[tuple[str, str]]]:
    """→ (id_resuelto | None, motivo, candidatos). Determinístico."""
    cands: list[tuple[str, str]] = []
    for crit, clave in (("label_exacto", C.norm(label)),
                        ("alias_exacto", C.norm(label)),
                        ("id_slug", slugify_full(label)),
                        ("label_singularizado", _norm_sing(_sin_parentesis(label)))):
        hit = idx.get((crit, clave))
        if hit and hit != "__AMBIGUO__":
            cands.append((crit, hit))
    sigla = _parentesis(label)
    if sigla:
        hit = idx.get(("alias_exacto", C.norm(sigla)))
        if hit and hit != "__AMBIGUO__" and (padre_sugerido in (None, "", hit)):
            cands.append(("alias_en_parentesis", hit))
    ids = {i for _, i in cands}
    if not cands:
        return None, "sin_match_en_catalogo", cands
    if len(ids) > 1:
        return None, "ambiguo", cands
    return cands[0][1], "resuelto_por_" + "+".join(sorted({c for c, _ in cands})), cands


def resolver_propuestos(kg: dict, catalogo: dict) -> dict:
    """Muta kg (nodes/edges). Devuelve registro con tabla por propuesto."""
    idx = indice_catalogo(catalogo)
    info_cat: dict[str, dict] = {}
    for e in catalogo["clases"]:
        info_cat[e["id"]] = {"label": e["label"], "nivel": e["nivel"]}
    for r in catalogo["roles"]:
        info_cat[r["id"]] = {"label": r["label"], "nivel": "rol"}

    nodes_by_id = {n["id"]: n for n in kg["nodes"]}
    tabla: list[dict] = []
    remap: dict[str, str] = {}
    for n in list(kg["nodes"]):
        if n["type"] != "Sujeto" or n.get("properties", {}).get("nivel") != "propuesto":
            continue
        padre = n["properties"].get("padre_sugerido")
        rid, motivo, cands = resolver_label(n["label"], padre, idx)
        fila = {"id_propuesto": n["id"], "label": n["label"], "padre_sugerido": padre,
                "n_provenances": len(n.get("provenances", [])),
                "candidatos": [list(c) for c in cands]}
        if rid is None:
            fila.update({"estado": "cuarentena", "motivo": motivo,
                         "resuelto_a": None})
            tabla.append(fila)
            continue
        if rid not in info_cat:
            raise RuntimeError(f"resolución a id fuera de catálogo: {rid}")
        fila.update({"estado": "resuelto", "motivo": motivo, "resuelto_a": rid,
                     "label_catalogo": info_cat[rid]["label"]})
        tabla.append(fila)
        remap[n["id"]] = rid
        destino = nodes_by_id.get(rid)
        if destino is None:
            destino = {"id": rid, "type": "Sujeto", "label": info_cat[rid]["label"],
                       "properties": {"nivel": info_cat[rid]["nivel"]},
                       "provenance": dict(n["provenance"]), "provenances": []}
            nodes_by_id[rid] = destino
            kg["nodes"].append(destino)
            fila["nodo_catalogo_creado"] = True
        vistos = {C.prov_key(p) for p in destino.get("provenances", [])}
        for p in n.get("provenances", []):
            if C.prov_key(p) not in vistos:
                destino.setdefault("provenances", []).append(p)
                vistos.add(C.prov_key(p))
        ar = destino["properties"].setdefault("alias_resueltos", [])
        if n["label"] not in ar:
            ar.append(n["label"])
        kg["nodes"].remove(n)
        del nodes_by_id[n["id"]]

    aristas_reapuntadas = _reapuntar(kg, remap)
    return {"tabla": tabla, "remap": remap, "aristas_reapuntadas": aristas_reapuntadas,
            "n_resueltos": sum(1 for f in tabla if f["estado"] == "resuelto"),
            "n_cuarentena": sum(1 for f in tabla if f["estado"] == "cuarentena"),
            "motivos": C.conteo([{"m": f["motivo"]} for f in tabla], "m")}


def _reapuntar(kg: dict, remap: dict[str, str]) -> int:
    """Re-apunta aristas según remap, fusionando triplas duplicadas con
    provenances acumuladas (dedup exacto). Devuelve cuántas se re-apuntaron."""
    if not remap:
        return 0
    edges_by_key: dict[tuple, dict] = {}
    n_re = 0
    for e in kg["edges"]:
        s, t = e["source"], e["target"]
        ns, nt = remap.get(s, s), remap.get(t, t)
        if (ns, nt) != (s, t):
            n_re += 1
            e["source"], e["target"] = ns, nt
        k = (ns, e["relation"], nt)
        if k in edges_by_key:
            m = edges_by_key[k]
            vistos = {C.prov_key(p) for p in m.get("provenances", [])}
            for p in e.get("provenances", []):
                if C.prov_key(p) not in vistos:
                    m.setdefault("provenances", []).append(p)
                    vistos.add(C.prov_key(p))
        else:
            edges_by_key[k] = e
    kg["edges"] = list(edges_by_key.values())
    return n_re


# ----------------------------------------------------------------------- #
# (b) TextoOrdenado solo desde provenance                                 #
# ----------------------------------------------------------------------- #
def id_texto_ordenado_canonico(archivo: str) -> str:
    # Misma convención de id de E2: TextoOrdenado_<slug(archivo)>.
    return f"TextoOrdenado_{slugify_full(archivo)}"


def canonizar_texto_ordenado(kg: dict) -> dict:
    archivos = {to: C.archivo_de_to(to) for to in C.TOS_ORDEN}
    canon = {to: id_texto_ordenado_canonico(a) for to, a in archivos.items()}
    nodes_by_id = {n["id"]: n for n in kg["nodes"]}
    registro: list[dict] = []
    remap: dict[str, str] = {}
    for n in list(kg["nodes"]):
        if n["type"] != "TextoOrdenado":
            continue
        tos = sorted({p["to"] for p in n.get("provenances", [])})
        if len(tos) != 1:
            raise RuntimeError(f"TextoOrdenado con provenance de {tos}: {n['id']}")
        to = tos[0]
        cid = canon[to]
        if n["id"] == cid:
            n["properties"]["archivo"] = archivos[to]
            continue
        destino = nodes_by_id.get(cid)
        if destino is None:
            raise RuntimeError(f"falta el TextoOrdenado canónico de {to}: {cid}")
        registro.append({"id_eliminado": n["id"], "label": n["label"],
                         "properties": deepcopy(n["properties"]),
                         "provenances": deepcopy(n.get("provenances", [])),
                         "reasignado_a": cid, "to": to,
                         "motivo": "TextoOrdenado espurio: el archivo emitido por E1 no es el "
                                   "del PDF del TO (provenance.archivo); la identidad del TO "
                                   "se toma SOLO de la provenance"})
        vistos = {C.prov_key(p) for p in destino.get("provenances", [])}
        for p in n.get("provenances", []):
            if C.prov_key(p) not in vistos:
                destino["provenances"].append(p)
                vistos.add(C.prov_key(p))
        remap[n["id"]] = cid
        kg["nodes"].remove(n)
        del nodes_by_id[n["id"]]
    n_re = _reapuntar(kg, remap)
    return {"canonicos": canon, "archivos": archivos, "eliminados": registro,
            "aristas_reapuntadas": n_re}


# ----------------------------------------------------------------------- #
# (c) filtro de ruido en conflictos                                       #
# ----------------------------------------------------------------------- #
def filtrar_conflictos(conflictos_intra: list[dict], conflictos_cross: list[dict]) -> dict:
    """conflictos_intra: items de e2_lib (id, property, conservado, descartado,
    chunk_id) con campo `to` agregado; conflictos_cross: items de
    ensamblar_corpus.merge_grafos (nivel, id, property, gana, pierde, to_perdedor)."""
    reales: list[dict] = []
    variantes: dict[str, dict[str, list[str]]] = {}
    n_var = 0
    for c in conflictos_intra:
        tipo = c["id"].split("_", 1)[0]
        if tipo == "TextoOrdenado" and c["property"] in PROPS_VARIANTE_TO:
            v = variantes.setdefault(c["id"], {}).setdefault(c["property"], [])
            for val in (c["conservado"], c["descartado"]):
                if val not in v:
                    v.append(val)
            n_var += 1
        else:
            reales.append({"origen": "intra_to", "to": c.get("to"), "tipo": tipo, **c})
    for c in conflictos_cross:
        tipo = c["id"].split("_", 1)[0]
        if tipo == "TextoOrdenado" and c["property"] in PROPS_VARIANTE_TO:
            v = variantes.setdefault(c["id"], {}).setdefault(c["property"], [])
            for val in (c["gana"], c["pierde"]):
                if val not in v:
                    v.append(val)
            n_var += 1
        else:
            reales.append({"origen": "cross_to", "tipo": tipo, **c})
    return {
        "n_total": len(conflictos_intra) + len(conflictos_cross),
        "n_variantes_to": n_var,
        "n_reales": len(reales),
        "reales_por_tipo_property": C.conteo(
            [{"k": f"{r['tipo']}.{r['property']}"} for r in reales], "k"),
        "variantes_texto_ordenado": variantes,
        "conflictos_reales": reales,
    }
