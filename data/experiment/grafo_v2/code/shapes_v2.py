#!/usr/bin/env python3
"""Validador de shapes v2 para los kg.json del esquema v2 (B1b, zona libre).

Adaptación de scripts/shapes_validator.py (v0, que NO se toca) con:
- Matriz de firmas v2: aplica_a → Sujeto; ejecuta desde Sujeto; y las 4
  relaciones de esqueleto (subclase_de/miembro_de/instancia_de/parte_de)
  válidas SOLO entre nodos Sujeto. 16 relaciones en total.
- S5 adaptada: los locations del esqueleto son legítimos ("Sección N",
  "Secciones ...", "diseño v2.0"), además de "Punto ...".
- S6 ampliada: source_doc ∈ los 5 TOs del subset ∪ "esquema_v2_clases.json".
- S13 nueva: todo nodo Sujeto tiene nivel ∈ {clase, instancia, rol, propuesto}.

El kg.json de entrada es SOLO LECTURA. Solo stdlib.

Uso:
    python3 shapes_v2.py --kg RUTA [--out RUTA.md]
"""

import argparse
import datetime
import json
import os
import unicodedata
from collections import defaultdict

PDFS_SUBSET = {
    "TO_capitales_minimos_actual.pdf",
    "TO_clasificacion_deudores_actual.pdf",
    "TO_exterior_cambios_actual.pdf",
    "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
    "TO_regimen_informativo_contable_mensual_actual.pdf",
}
SOURCE_DOCS_V2 = PDFS_SUBSET | {"esquema_v2_clases.json"}

RELACIONES_ESQUELETO = {"subclase_de", "miembro_de", "instancia_de", "parte_de"}
RELACIONES_16 = {
    "aplica_a", "regula", "prohibe", "limita", "exceptua",
    "exceptua_obligacion", "requiere", "condiciona", "ejecuta",
    "establecida_en", "referencia", "modificada_por",
} | RELACIONES_ESQUELETO

# S3 — matriz de firmas v2: relación -> (dominios permitidos, rango)
FIRMAS_V2 = {
    "establecida_en": ({"Obligacion", "Restriccion", "Operacion", "Excepcion"}, "TextoOrdenado"),
    "aplica_a": ({"Obligacion", "Restriccion"}, "Sujeto"),
    "regula": ({"Obligacion", "Restriccion"}, "Operacion"),
    "limita": ({"Restriccion"}, "Operacion"),
    "prohibe": ({"Restriccion"}, "Operacion"),
    "condiciona": ({"Obligacion"}, "Operacion"),
    "requiere": ({"Operacion"}, "Obligacion"),
    "exceptua": ({"Excepcion"}, "Restriccion"),
    "exceptua_obligacion": ({"Excepcion"}, "Obligacion"),
    "ejecuta": ({"Sujeto"}, "Operacion"),
    "referencia": ({"TextoOrdenado"}, "Comunicacion"),
    "modificada_por": ({"TextoOrdenado"}, "Comunicacion"),
    # Esqueleto: solo entre nodos Sujeto.
    "subclase_de": ({"Sujeto"}, "Sujeto"),
    "miembro_de": ({"Sujeto"}, "Sujeto"),
    "instancia_de": ({"Sujeto"}, "Sujeto"),
    "parte_de": ({"Sujeto"}, "Sujeto"),
}

UNIDADES_REGULATORIAS = ("Obligacion", "Restriccion", "Excepcion")
NIVELES_VALIDOS = {"clase", "instancia", "rol", "propuesto"}


def norm(s):
    if not isinstance(s, str):
        s = str(s)
    s = unicodedata.normalize("NFD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn").lower()


def check_provenance(prov):
    defectos = []
    if not isinstance(prov, dict):
        return [f"provenance no es dict (es {type(prov).__name__})"]
    keys = set(prov.keys())
    if keys != {"source_doc", "location"}:
        defectos.append(f"keys {sorted(keys)} != ['location', 'source_doc']")
    for k in ("source_doc", "location"):
        v = prov.get(k)
        if not isinstance(v, str) or not v.strip():
            defectos.append(f"{k} vacío o no-string")
    return defectos


def validar(kg_path):
    """Corre S1-S13 sobre el kg. Devuelve (resultados, n_nodos, n_aristas)."""
    with open(kg_path, encoding="utf-8") as f:
        g = json.load(f)
    nodes, edges = g["nodes"], g["edges"]
    node_by_id = {n["id"]: n for n in nodes}
    out_edges = defaultdict(list)
    for e in edges:
        out_edges[e["source"]].append(e)

    resultados = {}

    def registrar(rid, enunciado, result, resumen, detalle):
        resultados[rid] = {"enunciado": enunciado, "result": result,
                           "resumen": resumen, "detalle": detalle}

    # ---------- S1: 16 relaciones ----------
    viol = [f"idx {i}: relation='{e['relation']}'"
            for i, e in enumerate(edges) if norm(e["relation"]) not in RELACIONES_16]
    registrar("S1", "Toda arista usa una de las 16 relaciones v2 (12 + 4 de esqueleto).",
              "PASS" if not viol else "FAIL",
              f"{len(edges) - len(viol)}/{len(edges)} válidas; {len(viol)} violaciones.", viol)

    # ---------- S2 ----------
    viol = []
    for i, e in enumerate(edges):
        faltan = [x for x in ("source", "target") if e[x] not in node_by_id]
        if faltan:
            viol.append(f"idx {i}: {e['relation']} {e['source']} -> {e['target']} (inexistente: {', '.join(faltan)})")
    registrar("S2", "Integridad referencial: origen y destino de toda arista existen como nodos.",
              "PASS" if not viol else "FAIL", f"{len(viol)} aristas colgantes sobre {len(edges)}.", viol)

    # ---------- S3: matriz v2 ----------
    viol = []
    for i, e in enumerate(edges):
        rel = norm(e["relation"])
        if rel not in FIRMAS_V2 or e["source"] not in node_by_id or e["target"] not in node_by_id:
            continue
        dominios, rango = FIRMAS_V2[rel]
        st = node_by_id[e["source"]]["type"]
        dt = node_by_id[e["target"]]["type"]
        if st not in dominios or dt != rango:
            viol.append(f"idx {i}: {rel} {st} -> {dt} ({e['source']} -> {e['target']})")
    registrar("S3", "Toda arista respeta la matriz de firmas v2 (aplica_a→Sujeto; ejecuta desde Sujeto; esqueleto Sujeto→Sujeto).",
              "PASS" if not viol else "FAIL",
              f"{len(edges) - len(viol)}/{len(edges)} conformes; {len(viol)} violaciones.", viol)

    # ---------- S4 ----------
    viol = []
    nodos_ok = aristas_ok = 0
    for n in nodes:
        d = check_provenance(n.get("provenance"))
        if d:
            viol.append(f"nodo {n['id']}: {'; '.join(d)}")
        else:
            nodos_ok += 1
    for i, e in enumerate(edges):
        d = check_provenance(e.get("provenance"))
        if d:
            viol.append(f"arista idx {i} ({e['relation']}): {'; '.join(d)}")
        else:
            aristas_ok += 1
    registrar("S4", "Todo nodo y toda arista tienen provenance {source_doc, location} completa.",
              "PASS" if not viol else "FAIL",
              f"Nodos OK: {nodos_ok}/{len(nodes)}. Aristas OK: {aristas_ok}/{len(edges)}. Violaciones: {len(viol)}.", viol)

    # ---------- S5 (adaptada v2) ----------
    def loc_valida(loc):
        nl = norm(loc)
        return ("punto" in nl) or ("seccion" in nl) or (nl.strip() == "diseño v2.0") or (nl.strip() == "diseno v2.0")

    viol = []
    n_ok_n = n_ok_a = 0
    for n in nodes:
        loc = (n.get("provenance") or {}).get("location", "")
        if loc_valida(loc):
            n_ok_n += 1
        else:
            viol.append(f"nodo {n['id']}: location='{str(loc)[:80]}'")
    for i, e in enumerate(edges):
        loc = (e.get("provenance") or {}).get("location", "")
        if loc_valida(loc):
            n_ok_a += 1
        else:
            viol.append(f"arista idx {i} ({e['relation']}): location='{str(loc)[:80]}'")
    registrar("S5", "Todo location contiene 'punto' o 'sección', o es 'diseño v2.0' (esqueleto).",
              "PASS" if not viol else "FAIL",
              f"Nodos OK: {n_ok_n}/{len(nodes)}. Aristas OK: {n_ok_a}/{len(edges)}. Violaciones: {len(viol)}.", viol)

    # ---------- S6 (ampliada v2) ----------
    viol = []
    for n in nodes:
        sd = (n.get("provenance") or {}).get("source_doc")
        if sd not in SOURCE_DOCS_V2:
            viol.append(f"nodo {n['id']}: source_doc='{sd}'")
    for i, e in enumerate(edges):
        sd = (e.get("provenance") or {}).get("source_doc")
        if sd not in SOURCE_DOCS_V2:
            viol.append(f"arista idx {i} ({e['relation']}): source_doc='{sd}'")
    registrar("S6", "Todo source_doc pertenece a los 5 TOs del subset ∪ 'esquema_v2_clases.json'.",
              "PASS" if not viol else "FAIL",
              f"Conjunto válido: 5 TOs + esquema. Violaciones: {len(viol)}.", viol)

    # ---------- S7 ----------
    grupos = defaultdict(list)
    for n in nodes:
        grupos[(n["type"], norm(n["label"]))].append(n)
    dups = {k: v for k, v in grupos.items() if len(v) > 1}
    detalle = []
    for (t, l), ns in sorted(dups.items()):
        detalle.append(f"[{t}] '{l}' ({len(ns)} nodos): " + ", ".join(n["id"] for n in ns))
    registrar("S7", "ERROR — Unicidad exacta (type, label normalizado).",
              "PASS" if not dups else "FAIL",
              f"{len(dups)} grupos violatorios ({sum(len(v) for v in dups.values())} nodos).", detalle)

    # ---------- S8 ----------
    grupos2 = defaultdict(list)
    for n in nodes:
        grupos2[norm(n["label"])].append(n)
    cross = {l: ns for l, ns in grupos2.items() if len(ns) > 1 and len({n["type"] for n in ns}) > 1}
    detalle = [f"'{l}': " + ", ".join(f"[{n['type']}] {n['id']}" for n in ns) for l, ns in sorted(cross.items())]
    registrar("S8", "WARN — Colisión de label normalizado entre types distintos.",
              "PASS" if not cross else "WARN", f"{len(cross)} grupos cross-type.", detalle)

    # ---------- S9 ----------
    ambas = [n for n in nodes
             if "descripcion" in (n.get("properties") or {}) and "description" in (n.get("properties") or {})]
    registrar("S9", "ERROR — Ningún nodo tiene a la vez 'descripcion' y 'description'.",
              "PASS" if not ambas else "FAIL", f"{len(ambas)} nodos con ambas keys.",
              [f"[{n['type']}] {n['id']}" for n in ambas])

    # ---------- S10 ----------
    sin_est = defaultdict(list)
    for n in nodes:
        if n["type"] in UNIDADES_REGULATORIAS:
            if not any(norm(e["relation"]) == "establecida_en" for e in out_edges[n["id"]]):
                sin_est[n["type"]].append(n["id"])
    total_sin = sum(len(v) for v in sin_est.values())
    registrar("S10", "ERROR — Toda unidad regulatoria tiene >=1 establecida_en saliente.",
              "PASS" if total_sin == 0 else "FAIL",
              "Sin establecida_en: " + ", ".join(f"{t}={len(sin_est[t])}" for t in UNIDADES_REGULATORIAS) + f" (total {total_sin}).",
              [f"{t}: {i}" for t in UNIDADES_REGULATORIAS for i in sin_est[t]])

    # ---------- S11 ----------
    sin_apl = defaultdict(list)
    for n in nodes:
        if n["type"] in ("Obligacion", "Restriccion"):
            if not any(norm(e["relation"]) == "aplica_a" for e in out_edges[n["id"]]):
                sin_apl[n["type"]].append(n["id"])
    total_sin = sum(len(v) for v in sin_apl.values())
    registrar("S11", "WARN — Toda Obligacion/Restriccion tiene >=1 aplica_a saliente.",
              "PASS" if total_sin == 0 else "WARN",
              "Sin aplica_a: " + ", ".join(f"{t}={len(sin_apl[t])}" for t in ("Obligacion", "Restriccion")) + f" (total {total_sin}).",
              [f"{t}: {i}" for t in ("Obligacion", "Restriccion") for i in sin_apl[t]])

    # ---------- S12 ----------
    sin_exc = []
    for n in nodes:
        if n["type"] == "Excepcion":
            if not any(norm(e["relation"]) in ("exceptua", "exceptua_obligacion") for e in out_edges[n["id"]]):
                sin_exc.append(n["id"])
    registrar("S12", "ERROR — Toda Excepcion tiene >=1 salida exceptua/exceptua_obligacion.",
              "PASS" if not sin_exc else "FAIL", f"{len(sin_exc)} Excepciones huérfanas.", sin_exc)

    # ---------- S13 (nueva v2) ----------
    viol = []
    n_suj = 0
    for n in nodes:
        if n["type"] == "Sujeto":
            n_suj += 1
            nivel = (n.get("properties") or {}).get("nivel")
            if nivel not in NIVELES_VALIDOS:
                viol.append(f"nodo {n['id']}: nivel={nivel!r}")
    registrar("S13", "Todo nodo Sujeto tiene properties.nivel ∈ {clase, instancia, rol, propuesto}.",
              "PASS" if not viol else "FAIL",
              f"{n_suj - len(viol)}/{n_suj} Sujetos con nivel válido; {len(viol)} violaciones.", viol)

    return resultados, len(nodes), len(edges)


ORDEN = [f"S{i}" for i in range(1, 14)]


def main():
    ap = argparse.ArgumentParser(description="Validador de shapes v2 (matriz v2 + esqueleto)")
    ap.add_argument("--kg", required=True, help="Ruta al kg.json (solo lectura)")
    ap.add_argument("--out", default=None, help="Ruta del reporte Markdown (opcional)")
    args = ap.parse_args()

    resultados, n_nodes, n_edges = validar(args.kg)

    print(f"Grafo: {args.kg}")
    print(f"Nodos: {n_nodes} | Aristas: {n_edges}\n")
    for rid in ORDEN:
        r = resultados[rid]
        print(f"[{r['result']:4s}] {rid} — {r['resumen']}")
        for linea in r["detalle"][:50]:
            print(f"        {linea}")
        if len(r["detalle"]) > 50:
            print(f"        ... ({len(r['detalle'])} en total)")

    if args.out:
        fecha = datetime.date.today().isoformat()
        lineas = [f"# Shapes v2 — {os.path.basename(args.kg)}", "",
                  f"- Grafo: `{args.kg}`", f"- Fecha: {fecha}",
                  f"- Nodos: {n_nodes} | Aristas: {n_edges}", "",
                  "| Regla | Resultado | Resumen |", "|---|---|---|"]
        for rid in ORDEN:
            r = resultados[rid]
            lineas.append(f"| {rid} | {r['result']} | {r['resumen']} |")
        lineas.append("")
        for rid in ORDEN:
            r = resultados[rid]
            if r["detalle"]:
                lineas += [f"## {rid} — detalle", "", "```"] + r["detalle"] + ["```", ""]
        os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as f:
            f.write("\n".join(lineas))
        print(f"\nReporte escrito en: {os.path.abspath(args.out)}")


if __name__ == "__main__":
    main()
