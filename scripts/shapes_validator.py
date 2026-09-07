#!/usr/bin/env python3
"""Validador de shapes v0 (capas 1 y 2) para los kg.json del experimento.

Reglas determinísticas (sin LLM) S1-S12 y S15 sobre la estructura del grafo.
El kg.json de entrada es SOLO LECTURA: este script no lo modifica jamás.
Lo único que escribe es el reporte Markdown indicado por --out, y solo si esa
opción se pasa.

Uso:
    python3 scripts/shapes_validator.py [--kg RUTA] [--out RUTA]
                                        [--excepciones RUTA]

`--out` NO tiene default: sin esa opción el validador reporta por consola y no
escribe archivo alguno. Antes apuntaba a un reporte commiteado del repo y lo
sobrescribía en silencio (ver el comentario de DEFAULT_OUT).

S15 (U-ESQ-V3) es la guarda de la taxonomía de roles: un rol sin aristas
`miembro_de` entrantes es un nodo aislado del árbol, y las normas del TO que
lo declara dejan de ser alcanzables por navegación taxonómica — el mecanismo
que el capítulo del esquema presenta como aporte del grafo frente al
fragmento. Su tercera cláusula obliga a que la deuda quede VISIBLE Y CONTADA:
los roles sin miembro adjudicable se declaran en una lista, y el validador
compara la cuenta declarada contra la medida.

`--excepciones` apunta al artefacto que declara esa lista (el bloque
`excepciones_s15` de un esquema de clases, p. ej.
`data/experiment/esq_v3_miembros/esquema_v3_clases.json`). SIN esa opción la
lista declarada es vacía y cualquier rol huérfano es FAIL, que es el
comportamiento seguro por defecto.

S13, S14, S16 y S17 NO están implementadas y no se inventan: el orden de
reporte es la lista explícita S1..S12 + S15, sin huecos silenciosos.

Solo stdlib (sin dependencias de terceros).
"""

import argparse
import datetime
import json
import os
import re
import unicodedata
from collections import Counter, defaultdict

DEFAULT_KG = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "data", "experiment", "run_3_ppf_core", "kg.json",
)
# SIN default de salida (U-ESQ-V3). Hasta acá el default era
# reports/shapes_run_3_v0.md, un reporte COMMITEADO: correr la herramienta sin
# --out sobrescribía un artefacto del repo en silencio. El incidente está
# registrado desde el 02/08/2026 (data/backlog/retests/C3_retest_2026-08-02.md
# §Incidente: «escritura fuera del mandato, revertida con git checkout») y
# volvió a dispararse sobre el mismo archivo durante U-ESQ-V3. El checklist de
# un gate obliga a quien lo lee; el default obliga a cualquiera que corra la
# herramienta, así que el arreglo va acá.
#
# Sin --out el validador NO escribe: reporta por consola y listo. Es el mismo
# criterio que ya había adoptado la adaptación v2 de esta herramienta
# (data/experiment/grafo_v2/code/shapes_v2.py: `--out default=None`).
DEFAULT_OUT = None

RELACIONES_12 = {
    "aplica_a", "regula", "prohibe", "limita", "exceptua",
    "exceptua_obligacion", "requiere", "condiciona", "ejecuta",
    "establecida_en", "referencia", "modificada_por",
}

# S3 — matriz de firmas: relación -> (dominios permitidos, rango)
FIRMAS = {
    "establecida_en": ({"Obligacion", "Restriccion", "Operacion", "Excepcion"}, "TextoOrdenado"),
    "aplica_a": ({"Obligacion", "Restriccion"}, "EntidadFinanciera"),
    "regula": ({"Obligacion", "Restriccion"}, "Operacion"),
    "limita": ({"Restriccion"}, "Operacion"),
    "prohibe": ({"Restriccion"}, "Operacion"),
    "condiciona": ({"Obligacion"}, "Operacion"),
    "requiere": ({"Operacion"}, "Obligacion"),
    "exceptua": ({"Excepcion"}, "Restriccion"),
    "exceptua_obligacion": ({"Excepcion"}, "Obligacion"),
    "ejecuta": ({"EntidadFinanciera"}, "Operacion"),
    "referencia": ({"TextoOrdenado"}, "Comunicacion"),
    "modificada_por": ({"TextoOrdenado"}, "Comunicacion"),
}

UNIDADES_REGULATORIAS = ("Obligacion", "Restriccion", "Excepcion")

# S15 — orden de reporte. S13, S14, S16 y S17 no están implementadas: la lista
# es explícita para que su ausencia se lea, en vez de esconderse en un range().
ORDEN_SHAPES = [f"S{i}" for i in range(1, 13)] + ["S15"]
SHAPES_NO_IMPLEMENTADAS = ("S13", "S14", "S16", "S17")


def cargar_excepciones_s15(ruta):
    """Lee el bloque `excepciones_s15` del artefacto indicado.

    Devuelve (ids_declarados, total_declarado, por_causa, defecto). `defecto`
    describe un problema del propio artefacto (ilegible, sin bloque, cuenta
    interna inconsistente) y hace fallar S15: una lista de excepciones que no
    se puede leer no es una deuda declarada."""
    if not ruta:
        return set(), 0, {}, None
    try:
        with open(ruta, encoding="utf-8") as f:
            d = json.load(f)
    except Exception as e:
        return set(), 0, {}, f"no se pudo leer {ruta}: {e}"
    bloque = d.get("excepciones_s15")
    if not isinstance(bloque, dict):
        return set(), 0, {}, f"{ruta} no declara un bloque 'excepciones_s15'"
    filas = bloque.get("roles") or []
    ids = {r.get("rol_id") for r in filas if r.get("rol_id")}
    total = bloque.get("total")
    por_causa = bloque.get("por_causa") or {}
    if total != len(filas):
        return ids, total, por_causa, (
            f"el artefacto se contradice: declara total={total} y lista {len(filas)} roles")
    if por_causa and sum(por_causa.values()) != len(filas):
        return ids, total, por_causa, (
            f"el artefacto se contradice: la suma por causa ({sum(por_causa.values())}) "
            f"no reproduce el total listado ({len(filas)})")
    return ids, total, por_causa, None


def norm(s):
    """NFD + remoción de diacríticos + lowercase (normalización de los censos)."""
    if not isinstance(s, str):
        s = str(s)
    s = unicodedata.normalize("NFD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn").lower()


def check_provenance(prov):
    """Devuelve lista de defectos de un dict de provenance según S4."""
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


def main():
    ap = argparse.ArgumentParser(description="Validador de shapes v0 (capas 1 y 2)")
    ap.add_argument("--kg", default=DEFAULT_KG, help="Ruta al kg.json (solo lectura)")
    ap.add_argument("--out", default=DEFAULT_OUT,
                    help="Ruta del reporte Markdown. SIN default: si no se pasa, el "
                         "validador reporta por consola y no escribe ningún archivo.")
    ap.add_argument("--excepciones", default=None,
                    help="Artefacto con el bloque 'excepciones_s15' (S15). Sin esta opción "
                         "la lista declarada es vacía y todo rol huérfano es FAIL.")
    args = ap.parse_args()

    with open(args.kg, encoding="utf-8") as f:
        g = json.load(f)
    nodes, edges = g["nodes"], g["edges"]
    node_by_id = {n["id"]: n for n in nodes}
    out_edges = defaultdict(list)
    for e in edges:
        out_edges[e["source"]].append(e)

    resultados = {}   # regla -> dict(result, resumen, detalle_md, detalle_consola)

    def registrar(rid, enunciado, result, resumen, detalle_md, detalle_consola=None):
        resultados[rid] = {
            "enunciado": enunciado,
            "result": result,
            "resumen": resumen,
            "detalle_md": detalle_md,
            "detalle_consola": detalle_consola if detalle_consola is not None else detalle_md,
        }

    def lista_consola(items, limite=50):
        if len(items) <= limite:
            return items
        return items[:limite] + [f"... ({len(items)} en total; lista completa en el reporte)"]

    # ---------- S1 ----------
    viol = [f"idx {i}: relation='{e['relation']}'"
            for i, e in enumerate(edges) if norm(e["relation"]) not in RELACIONES_12]
    registrar(
        "S1", "Toda arista usa una de las 12 relaciones del esquema (nombre normalizado).",
        "PASS" if not viol else "FAIL",
        f"{len(edges) - len(viol)}/{len(edges)} aristas con relación válida; {len(viol)} violaciones.",
        viol,
    )

    # ---------- S2 ----------
    viol = []
    for i, e in enumerate(edges):
        faltan = [x for x in ("source", "target") if e[x] not in node_by_id]
        if faltan:
            viol.append(f"idx {i}: {e['relation']} {e['source']} -> {e['target']} (inexistente: {', '.join(faltan)})")
    registrar(
        "S2", "Integridad referencial: origen y destino de toda arista existen como nodos.",
        "PASS" if not viol else "FAIL",
        f"{len(viol)} aristas colgantes sobre {len(edges)}.",
        viol,
    )

    # ---------- S3 ----------
    viol = []
    for i, e in enumerate(edges):
        rel = norm(e["relation"])
        if rel not in FIRMAS or e["source"] not in node_by_id or e["target"] not in node_by_id:
            continue  # capturado por S1/S2
        dominios, rango = FIRMAS[rel]
        st = node_by_id[e["source"]]["type"]
        dt = node_by_id[e["target"]]["type"]
        if st not in dominios or dt != rango:
            viol.append(f"idx {i}: {rel} {st} -> {dt} ({e['source']} -> {e['target']})")
    registrar(
        "S3", "Toda arista respeta la matriz de firmas dominio -> rango declarada en FIRMAS.",
        "PASS" if not viol else "FAIL",
        f"{len(edges) - len(viol)}/{len(edges)} aristas conformes a firma; {len(viol)} violaciones.",
        viol,
    )

    # ---------- S4 ----------
    viol = []
    nodos_ok = 0
    for n in nodes:
        d = check_provenance(n.get("provenance"))
        if d:
            viol.append(f"nodo {n['id']}: {'; '.join(d)}")
        else:
            nodos_ok += 1
    aristas_ok = 0
    for i, e in enumerate(edges):
        d = check_provenance(e.get("provenance"))
        if d:
            viol.append(f"arista idx {i} ({e['relation']} {e['source']} -> {e['target']}): {'; '.join(d)}")
        else:
            aristas_ok += 1
    registrar(
        "S4", "Todo nodo y toda arista tienen provenance dict con exactamente source_doc y location, strings no vacías.",
        "PASS" if not viol else "FAIL",
        f"Nodos OK: {nodos_ok}/{len(nodes)}. Aristas OK: {aristas_ok}/{len(edges)}. Violaciones: {len(viol)}.",
        viol,
    )

    # ---------- S5 ----------
    viol = []
    n_loc_nodos = n_loc_aristas = 0
    for n in nodes:
        loc = (n.get("provenance") or {}).get("location", "")
        if "punto" in norm(loc):
            n_loc_nodos += 1
        else:
            viol.append(f"nodo {n['id']}: location='{loc[:80]}'")
    for i, e in enumerate(edges):
        loc = (e.get("provenance") or {}).get("location", "")
        if "punto" in norm(loc):
            n_loc_aristas += 1
        else:
            viol.append(f"arista idx {i} ({e['relation']}): location='{loc[:80]}'")
    registrar(
        "S5", "Todo location (de nodo y de arista) contiene 'punto' (normalizado).",
        "PASS" if not viol else "FAIL",
        f"Nodos con 'punto': {n_loc_nodos}/{len(nodes)}. Aristas: {n_loc_aristas}/{len(edges)}. Violaciones: {len(viol)}.",
        viol,
    )

    # ---------- S6 ----------
    archivos = {n["properties"].get("archivo") for n in nodes if n["type"] == "TextoOrdenado"}
    archivos.discard(None)
    viol = []
    for n in nodes:
        sd = (n.get("provenance") or {}).get("source_doc")
        if sd not in archivos:
            viol.append(f"nodo {n['id']}: source_doc='{sd}'")
    for i, e in enumerate(edges):
        sd = (e.get("provenance") or {}).get("source_doc")
        if sd not in archivos:
            viol.append(f"arista idx {i} ({e['relation']}): source_doc='{sd}'")
    registrar(
        "S6", "Todo source_doc pertenece al conjunto de valores de 'archivo' de los nodos TextoOrdenado.",
        "PASS" if not viol else "FAIL",
        f"Archivos válidos ({len(archivos)}): {sorted(archivos)}. Violaciones: {len(viol)}.",
        viol,
    )

    # ---------- S7 ----------
    grupos = defaultdict(list)
    for n in nodes:
        grupos[(n["type"], norm(n["label"]))].append(n)
    dups = {k: v for k, v in grupos.items() if len(v) > 1}
    detalle = []
    for (t, l), ns in sorted(dups.items()):
        detalle.append(f"[{t}] '{l}' ({len(ns)} nodos):")
        for n in ns:
            detalle.append(f"    - {n['id']}  (label: '{n['label']}')")
    registrar(
        "S7", "ERROR — Unicidad exacta: no puede haber dos nodos con el mismo (type, label normalizado).",
        "PASS" if not dups else "FAIL",
        f"{len(dups)} grupos violatorios ({sum(len(v) for v in dups.values())} nodos involucrados).",
        detalle,
    )

    # ---------- S8 ----------
    grupos2 = defaultdict(list)
    for n in nodes:
        grupos2[norm(n["label"])].append(n)
    cross = {l: ns for l, ns in grupos2.items()
             if len(ns) > 1 and len({n["type"] for n in ns}) > 1}
    detalle = []
    for l, ns in sorted(cross.items()):
        detalle.append(f"'{l}' ({len(ns)} nodos):")
        for n in ns:
            detalle.append(f"    - [{n['type']}] {n['id']}")
    registrar(
        "S8", "WARN — Colisión de label normalizado entre types distintos.",
        "PASS" if not cross else "WARN",
        f"{len(cross)} grupos con el mismo label normalizado en types distintos.",
        detalle,
    )

    # ---------- S9 ----------
    ambas = [n for n in nodes
             if "descripcion" in (n.get("properties") or {}) and "description" in (n.get("properties") or {})]
    tabla = []
    for t in sorted({n["type"] for n in nodes}):
        ns = [n for n in nodes if n["type"] == t]
        c_desc = sum(1 for n in ns if "descripcion" in (n.get("properties") or {}))
        c_engl = sum(1 for n in ns if "description" in (n.get("properties") or {}))
        c_ambas = sum(1 for n in ns
                      if "descripcion" in (n.get("properties") or {}) and "description" in (n.get("properties") or {}))
        c_ninguna = sum(1 for n in ns
                        if "descripcion" not in (n.get("properties") or {}) and "description" not in (n.get("properties") or {}))
        tabla.append(f"{t}: descripcion={c_desc}, description={c_engl}, ambas={c_ambas}, ninguna={c_ninguna} (total {len(ns)})")
    detalle = ["Tabla por type (usa cada key / ambas / ninguna):"] + [f"  {r}" for r in tabla] + \
              ["", f"Nodos con AMBAS keys ({len(ambas)}):"] + [f"    - [{n['type']}] {n['id']}" for n in ambas]
    registrar(
        "S9", "ERROR — Descripción canónica: ningún nodo tiene a la vez 'descripcion' y 'description'.",
        "PASS" if not ambas else "FAIL",
        f"{len(ambas)} nodos con ambas keys.",
        detalle,
    )

    # ---------- S10 ----------
    sin_est = defaultdict(list)
    for n in nodes:
        if n["type"] in UNIDADES_REGULATORIAS:
            if not any(norm(e["relation"]) == "establecida_en" for e in out_edges[n["id"]]):
                sin_est[n["type"]].append(n["id"])
    total_sin = sum(len(v) for v in sin_est.values())
    detalle = []
    for t in UNIDADES_REGULATORIAS:
        detalle.append(f"{t}: {len(sin_est[t])} sin establecida_en")
        for i in sin_est[t]:
            detalle.append(f"    - {i}")
    registrar(
        "S10", "ERROR — Toda unidad regulatoria (Obligacion/Restriccion/Excepcion) tiene >=1 arista saliente establecida_en.",
        "PASS" if total_sin == 0 else "FAIL",
        "Sin establecida_en: " + ", ".join(f"{t}={len(sin_est[t])}" for t in UNIDADES_REGULATORIAS) + f" (total {total_sin}).",
        detalle,
    )

    # ---------- S11 ----------
    sin_apl = defaultdict(list)
    for n in nodes:
        if n["type"] in ("Obligacion", "Restriccion"):
            if not any(norm(e["relation"]) == "aplica_a" for e in out_edges[n["id"]]):
                sin_apl[n["type"]].append(n["id"])
    total_sin = sum(len(v) for v in sin_apl.values())
    detalle = []
    for t in ("Obligacion", "Restriccion"):
        detalle.append(f"{t}: {len(sin_apl[t])} sin aplica_a")
        for i in sin_apl[t]:
            detalle.append(f"    - {i}")
    registrar(
        "S11", "WARN — Toda Obligacion y Restriccion tiene >=1 arista saliente aplica_a.",
        "PASS" if total_sin == 0 else "WARN",
        "Sin aplica_a: " + ", ".join(f"{t}={len(sin_apl[t])}" for t in ("Obligacion", "Restriccion")) + f" (total {total_sin}).",
        detalle,
        detalle_consola=[f"{t}: {len(sin_apl[t])} sin aplica_a" for t in ("Obligacion", "Restriccion")]
        + [f"(ids completos en el reporte; total {total_sin})"],
    )

    # ---------- S12 ----------
    sin_exc = []
    for n in nodes:
        if n["type"] == "Excepcion":
            if not any(norm(e["relation"]) in ("exceptua", "exceptua_obligacion") for e in out_edges[n["id"]]):
                sin_exc.append(n["id"])
    registrar(
        "S12", "ERROR — Toda Excepcion tiene >=1 arista saliente exceptua o exceptua_obligacion.",
        "PASS" if not sin_exc else "FAIL",
        f"{len(sin_exc)} Excepciones sin salida exceptua/exceptua_obligacion.",
        [f"    - {i}" for i in sin_exc],
    )

    # ---------- S15 (U-ESQ-V3) ----------
    # Todo rol tiene miembro_de no vacío O figura en la lista declarada de
    # roles sin miembro adjudicable; los miembros son clases del árbol; y el
    # validador REPORTA la lista con su cuenta.
    decl_ids, decl_total, decl_causa, decl_defecto = cargar_excepciones_s15(args.excepciones)

    roles = [n for n in nodes if (n.get("properties") or {}).get("nivel") == "rol"]
    miembros_de = defaultdict(list)
    for e in edges:
        if norm(e["relation"]) == "miembro_de":
            miembros_de[e["target"]].append(e["source"])

    huerfanos = sorted(r["id"] for r in roles if not miembros_de.get(r["id"]))
    no_declarados = [r for r in huerfanos if r not in decl_ids]
    declarados_con_miembro = sorted(i for i in decl_ids if miembros_de.get(i))

    # Segunda cláusula: el miembro es una clase del árbol. Sobre el grafo
    # vigente los 17 miembros son de nivel 'clase' (medido), y la adjudicación
    # de U-ESQ-V3 rechazó por laudo los candidatos de nivel instancia, así que
    # la regla describe lo que el grafo efectivamente tiene.
    miembros_no_clase = []
    for rol_id, ms in sorted(miembros_de.items()):
        for m in ms:
            n = node_by_id.get(m)
            niv = (n.get("properties") or {}).get("nivel") if n else None
            if niv != "clase":
                miembros_no_clase.append(
                    f"{m} --miembro_de--> {rol_id} (nivel del miembro: {niv or 'inexistente'})")

    cuenta_ok = (decl_total == len(huerfanos)) if args.excepciones else True

    viol_s15 = []
    if decl_defecto:
        viol_s15.append(f"lista de excepciones inválida: {decl_defecto}")
    viol_s15 += [f"rol huérfano NO declarado: {i}" for i in no_declarados]
    viol_s15 += [f"miembro que no es clase del árbol: {x}" for x in miembros_no_clase]
    if not cuenta_ok:
        viol_s15.append(
            f"la cuenta declarada ({decl_total}) no coincide con la medida "
            f"({len(huerfanos)} roles huérfanos en el grafo)")

    detalle_s15 = list(viol_s15)
    if decl_ids:
        detalle_s15.append("")
        detalle_s15.append(f"Lista declarada ({decl_total} roles"
                           + (f"; por causa: {decl_causa}" if decl_causa else "") + "):")
        detalle_s15 += [f"    - {i}" + ("  [YA TIENE MIEMBRO: declaración obsoleta]"
                                        if i in declarados_con_miembro else "")
                        for i in sorted(decl_ids)]

    registrar(
        "S15",
        "ERROR — Todo rol tiene miembro_de no vacío O figura en la lista declarada de roles sin "
        "miembro adjudicable; los miembros son clases del árbol; la cuenta declarada coincide "
        "con la medida.",
        "PASS" if not viol_s15 else "FAIL",
        f"{len(roles)} roles, {sum(len(v) for v in miembros_de.values())} aristas miembro_de; "
        f"{len(huerfanos)} huérfanos ({len(huerfanos) - len(no_declarados)} declarados, "
        f"{len(no_declarados)} sin declarar); {len(miembros_no_clase)} miembros que no son clase."
        + (f" Lista declarada: {decl_total}" + (f" ({decl_causa})" if decl_causa else "") + "."
           if args.excepciones else " Sin lista declarada (--excepciones no fue pasada)."),
        detalle_s15,
    )

    # ---------- Reporte ----------
    if args.out:
        os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
    fecha = datetime.date.today().isoformat()
    orden = list(ORDEN_SHAPES)
    lineas = [
        "# Validador de shapes v0 — capas 1 y 2",
        "",
        f"- **Grafo:** `{args.kg}`",
        f"- **Fecha:** {fecha}",
        f"- **Nodos:** {len(nodes)}",
        f"- **Aristas:** {len(edges)}",
        "",
    ]
    for rid in orden:
        r = resultados[rid]
        lineas += [f"## {rid} — {r['result']}", "", r["enunciado"], "", f"**Resultado:** {r['resumen']}", ""]
        if r["detalle_md"]:
            lineas += ["```"] + r["detalle_md"] + ["```", ""]
        else:
            lineas += ["Sin violaciones.", ""]
    lineas += ["## Tabla resumen", "", "| Regla | Resultado | Resumen |", "|---|---|---|"]
    for rid in orden:
        r = resultados[rid]
        lineas.append(f"| {rid} | {r['result']} | {r['resumen']} |")
    lineas.append("")
    lineas += [
        f"## Shapes no implementadas: {', '.join(SHAPES_NO_IMPLEMENTADAS)}",
        "",
        "Se declaran para que su ausencia se lea. No se inventan: implementarlas es otra unidad.",
        "",
    ]
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write("\n".join(lineas))

    # ---------- Consola ----------
    print(f"Grafo: {args.kg}")
    print(f"Nodos: {len(nodes)} | Aristas: {len(edges)}\n")
    for rid in orden:
        r = resultados[rid]
        print(f"[{r['result']:4s}] {rid} — {r['resumen']}")
        for linea in lista_consola(r["detalle_consola"]):
            print(f"        {linea}")
    print("\n=== TABLA RESUMEN ===")
    print(f"{'Regla':6s} {'Resultado':10s} Resumen")
    for rid in orden:
        r = resultados[rid]
        print(f"{rid:6s} {r['result']:10s} {r['resumen']}")
    if args.out:
        print(f"\nReporte escrito en: {os.path.abspath(args.out)}")
    else:
        print("\n(sin --out: no se escribió ningún archivo)")


if __name__ == "__main__":
    main()
