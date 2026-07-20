"""Barrido de auditoría del ground-truth de los 5 casos-control (solo lectura).

Genera una hoja de auditoría por caso en posthoc_run/auditoria_gt/, para adjudicación
humana. Este script ES la declaración de método: correrlo regenera las hojas idénticas.

MÉTODO
------
Grafo:   loader.load_graph('run_3') — el mismo adaptador congelado que usan las tools
         (kg.json de run_3_ppf_core normalizado en memoria). 4.050 nodos, 6.634 aristas.
Campos barridos por nodo: id, label, type, description y TODAS las properties,
         provenances (source_doc + location). NO solo lo que indexa buscar_nodos
         (que indexa únicamente label+id).
Matching: minúsculas + sin acentos (plegado 1:1 por carácter, preserva offsets para
         los snippets) sobre el texto original de cada campo. Los patrones son regex
         (listados en cada afirmación negativa de cada hoja).
PDF:     pypdf sobre data/experiment/subset/. Pasajes vía pdf_locate.localize cuando
         ancla; si no, ocurrencias en texto completo con whitespace colapsado y
         des-guionado ('xxx- yyy'→'xxxyyy'). OJO: pypdf inserta espacios intra-palabra
         ('quiene s'); los pasajes se muestran tal cual salen del extractor.
Criterio de reporte: TODOS los nodos que matchean algún patrón se listan con snippet,
         aunque parezcan irrelevantes — la relevancia la juzga la autora, no el script.
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

EVAL = Path(__file__).resolve().parents[2]   # data/experiment/evaluacion
sys.path.insert(0, str(EVAL))
import os
os.chdir(EVAL)

from loader import load_graph
from pdf_locate import localize, pdf_pages

OUT = EVAL / "posthoc_run" / "auditoria_gt"
CAL = EVAL / "posthoc_run" / "calibracion_verificador_v4"
COMMIT = "e35fe21"

# ----------------------------------------------------------------- helpers
def fold(s: str) -> str:
    """minúsculas + sin acentos, 1:1 por carácter (offsets preservados)."""
    out = []
    for ch in s or "":
        d = unicodedata.normalize("NFKD", ch)
        b = "".join(c for c in d if not unicodedata.combining(c))
        out.append((b[:1] or ch).lower())
    return "".join(out)

def n_ws(s): return re.sub(r"\s+", " ", (s or "")).strip()
def n_dh(s): return re.sub(r"(\w)-\s+(\w)", r"\1\2", n_ws(s))

kg = load_graph("run_3")
NODES = list(kg.nodes)
EDGES = list(kg.edges)

def fields_of(n):
    fs = [("id", n.id), ("label", n.label or ""), ("type", n.type or "")]
    for k, v in (n.properties or {}).items():
        fs.append((f"properties.{k}", v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)))
    fs.append(("provenances", json.dumps(n.provenances or [], ensure_ascii=False)))
    return fs

def sweep(patterns):
    """patterns: list[(nombre, regex_str)]. Regex se aplica sobre fold(texto original).
    Devuelve dict nombre -> lista de (node_id, field, snippet_original). Los patrones
    SIN matches quedan con lista vacía (el 0 es un resultado, no se omite)."""
    out = {}
    for name, rx in patterns:
        crx = re.compile(rx)
        rows = []
        for n in NODES:
            for field, text in fields_of(n):
                m = crx.search(fold(text))
                if m:
                    a, b = max(0, m.start() - 90), min(len(text), m.end() + 90)
                    snip = ("…" if a else "") + text[a:b] + ("…" if b < len(text) else "")
                    rows.append((n.id, field, n_ws(snip)))
                    break
        out[name] = rows
    return out

def fmt_sweep(res):
    L = []
    for name, rows in res.items():
        L.append(f"\n**Patrón `{name}`** — **{len(rows)} nodo(s)**:" +
                 ("  ⟵ **CERO matches en los 4.050 nodos**" if not rows else "") + "\n")
        for nid, field, snip in rows:
            L.append(f"- `{nid}` · campo `{field}`\n  > {snip}")
    return "\n".join(L) + "\n"

def pdf_pasaje(doc, loc, alt_anchor=None, max_len=750):
    """Pasaje vía localize; si falla o si se pide alt_anchor, ocurrencias en texto completo."""
    r = localize(doc, loc)
    if r.get("localizacion_pdf") == "ok" and not alt_anchor:
        return f"[{r.get('metodo')}: {r.get('ref')}]\n> " + n_ws(r.get("pasaje") or "")[:max_len]
    full = n_dh(" ".join(pdf_pages(doc)))
    anchor = alt_anchor or loc
    outs = []
    for m in re.finditer(re.escape(anchor), full):
        outs.append("> " + full[m.start():m.start() + max_len])
        if len(outs) >= 3:
            break
    if outs:
        return f"[texto completo, ocurrencias de «{anchor}» ({len(outs)} mostradas)]\n" + "\n\n".join(outs)
    return f"[NO LOCALIZADO: localize({doc},{loc}) falló y «{anchor}» no aparece en el texto completo]"

def nodo_verbatim(nid):
    for n in NODES:
        if n.id == nid:
            return "```json\n" + json.dumps(
                {"id": n.id, "type": n.type, "label": n.label,
                 "properties": n.properties, "provenances": n.provenances},
                ensure_ascii=False, indent=1) + "\n```"
    return f"**NO EXISTE** el nodo `{nid}` en run_3."

def v4_busquedas(qid):
    rec = json.loads((CAL / f"{qid}.json").read_text())
    L = []
    for i, a in enumerate(rec.get("atribuciones") or []):
        for b in a.get("busquedas") or []:
            L.append(f"- (atr{i} `{a.get('categoria')}`) «{b.get('consulta')}» → {b.get('resultado')}")
    for s in (rec["_meta"].get("trayectoria_verificador") or []):
        if s["tool"] == "buscar_nodos":
            labels = re.findall(r'"label": "([^"]{0,70})"', s.get("output_truncado") or "")
            L.append(f"- (trayectoria, paso {s['n']}) «{s['input'].get('consulta')}» → {labels[:4]}")
    if qid == "CQ-034":  # parse_ok=False: búsquedas desde el final_raw
        fr = rec["_meta"]["final_raw"]
        for x in re.findall(r'\{\s*"consulta"[^}]*\}', fr):
            try:
                b = json.loads(x)
                L.append(f"- (final_raw) «{b.get('consulta')}» → {b.get('resultado')}")
            except Exception:
                pass
    return "\n".join(L) or "_(sin búsquedas registradas)_"

METODO = """## Método (declarado — reproducible con `_barrido.py` de esta carpeta)

- **Grafo:** `loader.load_graph('run_3')` (mismo adaptador que usan las tools), commit `{commit}`. {nn} nodos, {ne} aristas.
- **Campos barridos por nodo:** `id`, `label`, `type`, `description` y **todas** las `properties`, `provenances` — NO solo label/id (que es lo único que indexa `buscar_nodos`).
- **Matching:** regex sobre texto plegado (minúsculas, sin acentos, offsets preservados). Los patrones exactos se listan en cada afirmación NEGATIVA.
- **PDF:** pypdf sobre `data/experiment/subset/`; pasajes vía `pdf_locate.localize` o, si no ancla, ocurrencias en texto completo (whitespace colapsado + des-guionado). pypdf puede insertar espacios intra-palabra; los pasajes se muestran tal cual.
- **Se listan TODOS los candidatos** que matchean, aunque parezcan irrelevantes: la relevancia la juzga la autora.
- **Evidencia cruzada v4:** las búsquedas documentadas del verificador v4 se anotan como insumo lado a lado, sin usarlas como veredicto.
""".format(commit=COMMIT, nn=len(NODES), ne=len(EDGES))

# =================================================================== CQ-031
def hoja_cq031():
    s = [f"# Auditoría GT — CQ-031 (`cadena_restriccion_excepcion` · TO clasificacion)\n", METODO,
         "## GT bajo auditoría\n",
         "> **completitud_kg** (nodo stub / enumeración del PDF no poblada). Secciones GT: Punto 4.5 · Punto 4.4.\n",
         "## Descomposición en afirmaciones atómicas\n",
         "| # | Tipo | Afirmación |\n|---|---|---|",
         "| P1 | POSITIVA | El PDF (Punto 4.5) enumera los deudores que no deben ser objeto de clasificación. |",
         "| P2 | POSITIVA | El PDF (Punto 4.4) establece respecto de qué financiaciones no corresponde evaluar capacidad de repago. |",
         "| P3 | POSITIVA | Existe en run_3 un nodo stub sobre 'deudores que no deben ser objeto de clasificación' sin la enumeración. |",
         "| N1 | NEGATIVA | No existe ningún nodo que contenga la enumeración del 4.5 (poblada). |",
         "| N2 | NEGATIVA | No existe ningún nodo con la regla del 4.4 (no evaluar capacidad de repago con garantías preferidas 'A'). |\n",
         "## P1 — PDF, Punto 4.5 (verbatim)\n", pdf_pasaje("TO_clasificacion_deudores_actual.pdf", "Punto 4.5"), "",
         "## P2 — PDF, Punto 4.4 (verbatim)\n", pdf_pasaje("TO_clasificacion_deudores_actual.pdf", "Punto 4.4"), "",
         "## P3 — Nodo stub (verbatim desde kg)\n", nodo_verbatim("Restriccion_deudores_que_no_deben_ser_objeto_de_clasificacion"), "",
         "## N1 + N2 — Barrido programático (4.050 nodos, todos los campos)\n",
         "Patrones (regex sobre texto plegado):\n",
         "```\nno seran objeto de clasificacion\ngarantias preferidas\ncesion sin responsabilidad\ncapacidad de (re)?pago\nobjeto de clasificacion\n```\n"]
    rows = sweep([
        ("no seran objeto de clasificacion", r"no seran objeto de clasificaci"),
        ("garantias preferidas", r"garantias preferidas"),
        ("cesion sin responsabilidad", r"cesion sin responsabilidad"),
        ("capacidad de (re)pago", r"capacidad de (re)?pago"),
        ("objeto de clasificacion", r"objeto de clasificacion"),
    ])
    s.append(fmt_sweep(rows))
    s += ["## Evidencia cruzada — búsquedas del verificador v4 (insumo, no veredicto)\n", v4_busquedas("CQ-031")]
    return "\n".join(s)

# =================================================================== CQ-034
def hoja_cq034():
    s = [f"# Auditoría GT — CQ-034 (`cadena_restriccion_excepcion` · TO exterior)\n", METODO,
         "## GT bajo auditoría\n",
         "> **completitud_kg** (límite faltante en la extracción). Límites literales en el PDF: USD 100 con efectivo (3.8) y USD 200 para otras modalidades (3.9).\n",
         "## Descomposición en afirmaciones atómicas\n",
         "| # | Tipo | Afirmación |\n|---|---|---|",
         "| P1 | POSITIVA | El PDF (Punto 3.8) contiene el límite USD 100 con efectivo. |",
         "| P2 | POSITIVA | El PDF (Punto 3.9) contiene el límite general USD 200 para otras modalidades. |",
         "| P3 | POSITIVA | Existe en run_3 un nodo de 'formación de activos externos' (stub, sin límites). |",
         "| N1 | NEGATIVA | No existe ningún nodo que contenga el límite USD 200 mensual (otras modalidades / 3.9). |",
         "| N2 | NEGATIVA | No existe ningún nodo que asocie un límite de monto al débito en cuenta. |\n",
         "## P1 — PDF, Punto 3.8 (verbatim)\n", pdf_pasaje("TO_exterior_cambios_actual.pdf", "Punto 3.8"), "",
         "## P2 — PDF, Punto 3.9 (verbatim)\n", pdf_pasaje("TO_exterior_cambios_actual.pdf", "Punto 3.9"), "",
         "## P3 — Nodo FAE (verbatim desde kg)\n", nodo_verbatim("Operacion_formacion_de_activos_externos"), "",
         "## N1 + N2 — Barrido programático\n",
         "Patrones:\n```\n\\busd 200\\b | \\b200\\b (con borde de palabra)\ndoscientos\notras modalidades\nayuda familiar\nformacion de activos externos\ndebito en cuenta\natesoramiento | atesorar\n```\n"]
    rows = sweep([
        ("USD 200 / 200", r"\busd\s*200\b|\b200\b(?!\d)"),
        ("doscientos", r"doscientos"),
        ("otras modalidades", r"otras modalidades"),
        ("ayuda familiar", r"ayuda familiar"),
        ("formacion de activos externos", r"formacion de activos externos"),
        ("debito en cuenta", r"debito en cuenta"),
        ("atesoramiento/atesorar", r"atesor"),
    ])
    s.append(fmt_sweep(rows))
    s += ["## Evidencia cruzada — búsquedas del verificador v4 (insumo, no veredicto)\n", v4_busquedas("CQ-034")]
    return "\n".join(s)

# =================================================================== CQ-017
def hoja_cq017():
    s = [f"# Auditoría GT — CQ-017 (`multi_norma` · TOs proteccion, exterior)\n", METODO,
         "## GT bajo auditoría\n",
         "> MIXTA, dos PRIMARIAS de grafo: **estructural_kg** (falta la arista cross-documento Protección 1.1.2.2 ↔ Exterior 1.1) y **provenance_imprecisa** (el nodo del operador de cambio cita 'Punto 1.1' grueso en vez de '1.1.2.2').\n",
         "## Descomposición en afirmaciones atómicas\n",
         "| # | Tipo | Afirmación |\n|---|---|---|",
         "| P1 | POSITIVA | Existe el nodo del operador de cambio con provenance a nivel grueso ('Punto 1.1'). |",
         "| P2 | POSITIVA | El PDF de Protección (1.1.2.2) nombra a los operadores de cambio como sujetos alcanzados (ubicación fina). |",
         "| P3 | POSITIVA | El PDF de Exterior y Cambios (Punto 1.1) establece la intervención de entidad autorizada en el mercado de cambios. |",
         "| N1 | NEGATIVA | No existe arista cross-documento que conecte la pata Protección (operador de cambio) con la pata Exterior (entidad autorizada / mercado de cambios). |\n",
         "## P1 — Nodo del operador de cambio (verbatim desde kg)\n", nodo_verbatim("EntidadFinanciera_operador_de_cambio"), "",
         "## P2 — PDF Protección, 1.1.2.2 (verbatim)\n",
         pdf_pasaje("TO_proteccion_usuarios_servicios_financieros_actual.pdf", "Punto 1.1.2.2", alt_anchor="1.1.2.2."), "",
         "## P3 — PDF Exterior y Cambios, Punto 1.1 (verbatim)\n", pdf_pasaje("TO_exterior_cambios_actual.pdf", "Punto 1.1"), "",
         "## N1 — Barrido de ARISTAS entre las dos patas\n",
         "Conjuntos definidos por patrón (sobre todos los campos de cada nodo):\n",
         "- **Pata Protección** (`operador(es) de cambio`): nodos cuyo texto matchea `operador(es)? de cambio`.\n",
         "- **Pata Exterior** (`entidad/persona autorizada`, `mercado (único/libre) de cambios`): matchea `(entidad|persona)s? autorizada|mercado( unico| libre)?s? de cambios`.\n",
         "Se listan TODAS las aristas incidentes a cada conjunto, marcando las que CRUZAN de un conjunto al otro.\n"]
    rx1 = re.compile(r"operador(es)? de cambio")
    rx2 = re.compile(r"(entidad|persona)e?s? autorizada|mercado( unico| libre)?s? de cambios")
    set1, set2_ext, set2_nuc = set(), set(), set()
    for n in NODES:
        blob = fold(" | ".join(t for _, t in fields_of(n)))
        if rx1.search(blob):
            set1.add(n.id)
        if rx2.search(blob):
            set2_ext.add(n.id)
        if rx2.search(fold(f"{n.id} {n.label or ''}")):   # núcleo: solo label/id
            set2_nuc.add(n.id)
    s.append(f"**Pata Protección — {len(set1)} nodo(s):** " + ", ".join(f"`{i}`" for i in sorted(set1)) + "\n")
    s.append(f"**Pata Exterior, NÚCLEO (patrón sobre label/id) — {len(set2_nuc)} nodo(s):** " +
             ", ".join(f"`{i}`" for i in sorted(set2_nuc)) + "\n")
    s.append(f"**Pata Exterior, EXTENDIDA (patrón sobre todos los campos, incl. description/provenances) — "
             f"{len(set2_ext)} nodo(s).** Lista completa de ids al final de la hoja; el chequeo de cruce "
             "de abajo se computa sobre este conjunto COMPLETO.\n")

    def rowfmt(e):
        return (f"`{e.source}` —**{e.relation}**→ `{e.target}` · "
                f"prov: {json.dumps(e.provenances or [], ensure_ascii=False)[:150]}")

    cross = [rowfmt(e) for e in EDGES
             if ((e.source in set1 and e.target in set2_ext) or
                 (e.target in set1 and e.source in set2_ext))]
    inc1 = [rowfmt(e) for e in EDGES if e.source in set1 or e.target in set1]
    inc2n = [rowfmt(e) for e in EDGES if e.source in set2_nuc or e.target in set2_nuc]
    s.append(f"### Aristas que CRUZAN pata Protección ↔ pata Exterior EXTENDIDA ({len(cross)}):\n")
    s.append("\n".join(f"- {r}" for r in cross) or "_(NINGUNA — cero aristas conectan las dos patas, "
                                                   "incluso con el conjunto Exterior extendido a 250+ nodos)_")
    s.append(f"\n### Todas las aristas incidentes a la pata Protección ({len(inc1)}):\n")
    s.append("\n".join(f"- {r}" for r in inc1) or "_(ninguna)_")
    s.append(f"\n### Todas las aristas incidentes al NÚCLEO de la pata Exterior ({len(inc2n)}):\n")
    s.append("\n".join(f"- {r}" for r in inc2n) or "_(ninguna)_")
    s += ["\n## Evidencia cruzada — búsquedas del verificador v4 (insumo, no veredicto)\n", v4_busquedas("CQ-017")]
    s.append("\n## Apéndice — Pata Exterior EXTENDIDA, lista completa de ids\n")
    s.append(", ".join(f"`{i}`" for i in sorted(set2_ext)))
    return "\n".join(s)

# =================================================================== CQ-020
def hoja_cq020():
    s = [f"# Auditoría GT — CQ-020 (`multi_norma` · TOs capitales, regimen)\n", METODO,
         "## GT bajo auditoría\n",
         "> MIXTA: primaria **completitud_kg** (falta el nodo de frecuencia de reporte para riesgo de crédito; por su ausencia el agente mis-aplica el de riesgo de mercado) + secundaria **generación-de-más** (glosas k/APRc/INC sin soporte).\n",
         "## Descomposición en afirmaciones atómicas\n",
         "| # | Tipo | Afirmación |\n|---|---|---|",
         "| P1 | POSITIVA | El PDF (Régimen, Punto 1.1) establece la frecuencia (mensual, con excepciones trimestrales). |",
         "| P2 | POSITIVA | Existe el nodo de frecuencia de riesgo de MERCADO (el que el agente mis-aplicó). |",
         "| N1 | NEGATIVA | No existe ningún nodo de frecuencia/periodicidad de reporte para riesgo de CRÉDITO. |",
         "| N2 | NEGATIVA | No existe ningún nodo que defina las variables de la fórmula CRC (0,08 como coeficiente; A/p/PFB/CCF como conceptos). |\n",
         "## P1 — PDF Régimen, Punto 1.1 (verbatim)\n", pdf_pasaje("TO_regimen_informativo_contable_mensual_actual.pdf", "Punto 1.1"), "",
         "## P2 — Nodo de frecuencia de riesgo de mercado (verbatim desde kg)\n", nodo_verbatim("Obligacion_informar_exigencia_de_capitales_por_riesgo"), "",
         "## N1 + N2 — Barrido programático\n",
         "Patrones (cruces con ventana de proximidad de 120 caracteres, en ambos órdenes):\n",
         "```\n(frecuencia|mensual|periodicidad|trimestral) ×120× (riesgo de credito|crc)\n(informar|presentar|reportar) ×80× credito\n(riesgo de credito) — todos los nodos que lo mencionan\n0[,.]08\ncoeficiente\nactivos ponderados\n\\bapr_?c?\\b\n```\n"]
    prox = r"(frecuencia|mensual|periodicidad|trimestral).{0,120}(riesgo de credito|\bcrc\b)|(riesgo de credito|\bcrc\b).{0,120}(frecuencia|mensual|periodicidad|trimestral)"
    rows = sweep([
        ("frecuencia×riesgo de credito", prox),
        ("informar/presentar×credito", r"(informar|presentar|reportar).{0,80}credito"),
        ("riesgo de credito (todos)", r"riesgo de credito"),
        ("0,08", r"0[,.]08"),
        ("coeficiente", r"coeficiente"),
        ("activos ponderados", r"activos ponderados"),
        ("APRc", r"\bapr_?c?\b"),
    ])
    s.append(fmt_sweep(rows))
    s += ["## Evidencia cruzada — búsquedas del verificador v4 (insumo, no veredicto)\n", v4_busquedas("CQ-020")]
    return "\n".join(s)

# =================================================================== CQ-025
def hoja_cq025():
    s = [f"# Auditoría GT — CQ-025 (`multi_norma` · TO regimen)\n", METODO,
         "## GT bajo auditoría\n",
         "> MIXTA: pata 1 **contenido_kg** PRIMARIA (el nodo `Operacion_calculo_de_riesgo_de_mercado` dice 'mensual'; el PDF 1.1 ubica riesgo de mercado 4.3-4.5 en las excepciones TRIMESTRALES) + pata 2 **falso positivo del juez** (apalancamiento trimestral, bien respondido y citado). Regla: detectar pata 1 como navegación NO es acierto — 'el dato correcto (trimestral) no existe en el grafo'.\n",
         "## Descomposición en afirmaciones atómicas\n",
         "| # | Tipo | Afirmación |\n|---|---|---|",
         "| P1 | POSITIVA | El nodo `Operacion_calculo_de_riesgo_de_mercado` dice 'mensual'. |",
         "| P2 | POSITIVA | El PDF (Punto 1.1) ubica los datos de riesgo de mercado (4.3-4.5) entre las excepciones trimestrales. |",
         "| P3 | POSITIVA | El PDF (10.1/10.1.1) dice que el ratio de apalancamiento se informa con frecuencia trimestral, y el agente lo respondió y citó así. |",
         "| N1 | NEGATIVA | Ningún nodo del grafo contiene el dato correcto 'trimestral' para riesgo de mercado. |\n",
         "## P1 — Nodo (verbatim desde kg)\n", nodo_verbatim("Operacion_calculo_de_riesgo_de_mercado"), "",
         "## P2 — PDF Régimen, Punto 1.1 (verbatim)\n", pdf_pasaje("TO_regimen_informativo_contable_mensual_actual.pdf", "Punto 1.1"), "",
         "## P3 — PDF Régimen, Punto 10.1 (verbatim; el cuerpo, no el índice)\n",
         pdf_pasaje("TO_regimen_informativo_contable_mensual_actual.pdf", "Punto 10.1",
                    alt_anchor="Los datos se informarán con frecuencia trimestral"), ""]
    # respuesta del agente (traza congelada)
    rep = json.loads((EVAL / "posthoc_run/traces/off/run_3/CQ-025.json").read_text())[0]
    fj = (rep.get("trace") or {}).get("final_json") or {}
    citas = "; ".join(f"{c.get('source_doc')} :: {c.get('location')}" for c in (fj.get("citas") or []))
    s += ["**Respuesta del agente (traza, verbatim):**\n", f"> {n_ws(fj.get('respuesta') or '')[:700]}\n", f"citas: {citas}\n",
          "## N1 — Barrido programático\n",
          "Patrones:\n```\ntrimestral ×120× mercado (ambos órdenes)\ntrimestral — todos los nodos\nriesgo de mercado — todos los nodos\n4\\.3|4\\.4|4\\.5 (en provenances/propiedades)\n```\n"]
    rows = sweep([
        ("trimestral×mercado", r"trimestral.{0,120}mercado|mercado.{0,120}trimestral"),
        ("trimestral (todos)", r"trimestral"),
        ("riesgo de mercado (todos)", r"riesgo de mercado"),
        ("4.3/4.4/4.5", r"\b4\.[345]\b"),
    ])
    s.append(fmt_sweep(rows))
    s += ["## Evidencia cruzada — búsquedas del verificador v4 (insumo, no veredicto)\n", v4_busquedas("CQ-025")]
    return "\n".join(s)

# ------------------------------------------------------------------ main
OUT.mkdir(parents=True, exist_ok=True)
for qid, fn in (("CQ-031", hoja_cq031), ("CQ-034", hoja_cq034), ("CQ-017", hoja_cq017),
                ("CQ-020", hoja_cq020), ("CQ-025", hoja_cq025)):
    p = OUT / f"{qid}.md"
    p.write_text(fn(), encoding="utf-8")
    print(p.name, p.stat().st_size, "bytes")
