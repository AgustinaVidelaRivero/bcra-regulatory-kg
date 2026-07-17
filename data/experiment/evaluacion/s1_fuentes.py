"""s1_fuentes.py — S1: segunda pasada con fuentes forzadas (v7 = v6.1-D + S1).

Implementa el diseño pre-registrado de docs/diseno_v7_s1.md (§2). DOS componentes
estrictamente separados:

1. FETCH DETERMINÍSTICO (puro, sin API) — construir_paquete_fuentes:
   - Gatillo (diseño §2): atribuciones de reps válidas con causa final en
     {contenido_kg, aplicacion_erronea, estructural_kg, completitud_kg}; y, si el voto del
     caso (voto_capa_d) es de clave vacía CON síntoma no vacío (F/P de _sintoma_de_trace,
     el MISMO filtro que build_falla_context), las atribuciones sin_defecto del caso
     (tipo_gatillo "exoneracion_con_sintoma").
   - Por atribución gatillada: portador vía _extraer_portador (el extractor de D2, sin
     heurísticas nuevas); provenance del portador desde el kg del run — se usa la PRIMERA
     provenance parseable por pdf_locate.parse_point (orden del kg; se registran el índice
     usado y el total); pdf_locate.localize recupera (a) el pasaje del portador CON su
     encabezado y (b) los comparativos:
       * "seccion_madre": el encabezado de la sección madre = PRIMER nivel del punto del
         portador (existe si el punto tiene ≥2 niveles). CORRECCIÓN B3b (por mecanismo,
         hecho b del dry-run de B3): SIEMPRE se emite con estado "omitido" y nota fija —
         los encabezados de primer nivel son carátula sin prosa y localize los falla
         sistemáticamente (sondeo en los 4 TOs) — sin llamar a localize;
       * "punto_general_un_nivel_arriba": mismo prefijo, un nivel arriba (padre inmediato
         del punto del portador; existe como comparativo DISTINTO solo si el punto tiene
         ≥3 niveles — con 2 niveles el padre inmediato COINCIDE con la sección madre y se
         anota como nota mecánica, sin duplicar);
       * "referencia_interna" (CORRECCIÓN B3b, por mecanismo — hecho a del dry-run de B3:
         la conexión relevante vive en el TEXTO del pasaje, no en la jerarquía de
         numeración): menciones a otros puntos/secciones extraídas del texto del pasaje
         del PORTADOR con la regex cerrada RE_REFERENCIAS_INTERNAS (variantes
         "punto X.Y[.Z]", "puntos X.Y y X.Z", "Sección N."), en orden de aparición,
         deduplicadas por (punto, documento de destino), tope
         TOPE_REFERENCIAS_INTERNAS = 3; cada una con su mención de origen verbatim.
         CORRECCIÓN B3c (por mecanismo — hecho de B3b: la regex resolvía intra-documento
         menciones dirigidas a OTRO TO, inyectando texto equivocado): tras cada mención
         se inspecciona una ventana fija de VENTANA_MARCADOR_EXTERNO = 100 chars
         siguientes con la regex cerrada RE_MARCADOR_DOC_EXTERNO ("del TO/Texto Ordenado
         (de las normas) sobre <nombre>" / "de las normas sobre <nombre>"). Sin marcador
         → intra-documento (comportamiento previo). Con marcador: el <nombre> se matchea
         contra el mapa cerrado DOCS_CORPUS (los 5 TOs del experimento, por palabras
         clave normativas); si matchea, la referencia se localiza EN ESE documento
         (regla="referencia_interna_cross_doc", doc_destino anotado); si NO matchea (TO
         fuera del corpus), el comparativo se emite "omitido_fuera_de_corpus" con la
         mención y el marcador verbatim — NUNCA se resuelve intra-documento una mención
         marcada como externa.
     Cada comparativo lleva su regla aplicada (mecánica, sin juicio) y su ESTADO PROPIO
     ("localizado" / "fallido" / "omitido") — que NO fuerza triage (política de estados
     NO BLOQUEANTE, corrección B3b).
   - Estados explícitos del paquete por atribución (el triage fuente_no_verificable de S1
     queda RESERVADO a fallas del PORTADOR):
     "sin_portador_extraible" (cero o >1 ids del kg en la evidencia),
     "provenance_no_parseable" (ninguna provenance del portador parsea a punto/sección),
     "localizacion_fallida" (localize del pasaje del PORTADOR devolvió fallida),
     "completo" (el pasaje del PORTADOR localizó — comparativos fallidos u omitidos NO
     bloquean).

2. JUICIO S1 (la única parte con LLM) — aplicar_s1:
   - Por atribución gatillada con paquete "completo": UNA llamada por repetición (n) al
     modelo del verificador (MODEL_VERIF, importado del instrumento congelado) con
     S1_PROMPT, que presenta la atribución emitida, el contenido del nodo portador y los
     pasajes fuente, y EXIGE el esquema del diseño §2 en JSON estricto:
     alcance_declarado_en_fuente / alcance_en_el_nodo / coinciden ∈ {si, no,
     no_determinable} / causa_confirmada_o_corregida / justificacion_breve.
   - S1 NUNCA borra la emisión de v6.1-D: anota capa_s1 al lado (emision_v61d, salidas S1
     íntegras, corrigio: bool) — el mismo patrón de anotación que capa_d —, recomputa el
     voto como voto_s1 con la regla del protocolo (mayoría estricta ≥2) sobre las causas
     post-S1, preservando intactos voto, voto_capa_d y voto_pre_d6 (si existe).
   - Todo estado de fetch fallido y todo resultado no_determinable (o sin mayoría propia
     de S1 con n>1) → triage_s1 con motivo "fuente_no_verificable".
   - --n habilita repetición + voto propio de S1 por atribución (mayoría estricta
     ≥ n//2+1 sobre la causa de las salidas decididas); la POLÍTICA de N se decide en la
     calibración del dev (B4) — acá queda implementada, no decidida.

Módulo que NO modifica congelados (verificador.py, harness.py, capa_deterministica.py,
test_alcanzabilidad.py, taxonomia.md, las varas): solo los importa. S1 no re-investiga
trayectorias: juzga la atribución emitida contra la fuente (diseño §2, "lo que no cambia").
"""

import argparse
import copy
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from capa_deterministica import (          # reutilización pre-registrada — solo import
    _extraer_portador,
    _norm_texto,
    _recomputar_voto,
    _sintoma_de_trace,
)
from test_alcanzabilidad import _index_de  # resolución run|GraphIndex (mismo patrón D1-D6)
from pdf_locate import parse_point, localize
from verificador import MODEL_VERIF        # el modelo del verificador (import read-only)
from verifier_pilot import _extract_json   # parser JSON ya probado del pipeline

S1_VERSION = "s1-v0.1-dev"
S1_MAX_TOKENS = 2048

CAUSAS_GATILLO_S1 = frozenset(
    {"contenido_kg", "aplicacion_erronea", "estructural_kg", "completitud_kg"})

COINCIDEN_VALORES = ("si", "no", "no_determinable")
CAMPOS_S1 = ("alcance_declarado_en_fuente", "alcance_en_el_nodo", "coinciden",
             "causa_confirmada_o_corregida", "justificacion_breve")

S1_PROMPT = """Sos S1, la segunda pasada con fuentes forzadas de un instrumento de atribución de fallas \
sobre un sistema KG-RAG regulatorio (BCRA). NO re-investigás la falla: tu única tarea es juzgar UNA \
atribución ya emitida contra el texto fuente que se te entrega abajo, comparando ALCANCES.

Una atribución dice que un nodo del grafo (el "portador") tiene un defecto de cierta causa. El error \
típico que S1 existe para atajar: tratar como general un contenido que la fuente declara SCOPEADO \
(limitado a una cartera, un grupo, un régimen o un período), o al revés. Por eso el juicio es una \
comparación de alcances, y estás OBLIGADO a transcribirlos antes de decidir.

=== ATRIBUCIÓN EMITIDA (v6.1-D) ===
{atribucion}

=== NODO PORTADOR ({portador_id}) ===
{nodo}

=== PASAJES FUENTE (verbatim del PDF, recuperados por código desde la provenance del portador) ===
{pasajes}

Respondé ÚNICAMENTE un JSON estricto (sin texto antes ni después) con EXACTAMENTE estas claves:
{{
 "alcance_declarado_en_fuente": "<quote VERBATIM del encabezado/pasaje fuente que declara el alcance \
(copiado carácter a carácter, NO parafraseado)>",
 "alcance_en_el_nodo": "<quote VERBATIM del contenido del nodo que muestra con qué alcance lo trata>",
 "coinciden": "si | no | no_determinable",
 "causa_confirmada_o_corregida": "<la causa emitida si el juicio la confirma, o la causa corregida de la \
taxonomía v2.6.1 (contenido_kg, completitud_kg, estructural_kg, alcanzabilidad_kg, navegación, \
alucinacion_agente, aplicacion_erronea, sin_defecto) si no>",
 "justificacion_breve": "<1 a 3 frases: qué dice el alcance de la fuente, qué hace el nodo/la atribución \
con él, y por qué la causa queda confirmada o corregida>"
}}

Reglas duras:
- Los dos campos de alcance son OBLIGATORIOS y VERBATIM: si no podés transcribir un alcance desde el \
material entregado, no inventes — poné coinciden="no_determinable" y explicá qué falta.
- "coinciden" se refiere a si el alcance con que el nodo/la atribución tratan el contenido COINCIDE con \
el alcance declarado en la fuente.
- Juzgá SOLO con el material entregado (atribución + nodo + pasajes). Nada de conocimiento externo.
"""


# --------------------------------------------------------------------------- #
# 1. FETCH DETERMINÍSTICO (puro, sin API)                                      #
# --------------------------------------------------------------------------- #
# Regex CERRADA de referencias internas (corrección B3b — hecho a del dry-run de B3):
# variantes "punto X.Y[.Z]" (con o sin punto final), "puntos X.Y y X.Z" (enumeraciones con
# "y"/"e"/","), y "Sección N." (primer nivel con punto). Nada más.
RE_REFERENCIAS_INTERNAS = {
    "punto": re.compile(
        r"(?i)\bpuntos?\s+\d+(?:\.\d+)+\s*\.?(?:\s*(?:,|y|e)\s+\d+(?:\.\d+)+\s*\.?)*"),
    "seccion": re.compile(r"(?i)\bsecci[oó]n\s+(\d+)\."),
}
_RE_NUM_PUNTO = re.compile(r"\d+(?:\.\d+)+")   # extractor de números dentro de la mención
TOPE_REFERENCIAS_INTERNAS = 3

# Marcador de documento externo (corrección B3c): regex CERRADA buscada en una ventana
# fija de VENTANA_MARCADOR_EXTERNO chars a continuación de cada mención capturada.
# Variantes: "del TO sobre <nombre>", "del Texto Ordenado (de las normas) sobre <nombre>",
# "de las normas sobre <nombre>" (con comilla opcional antes del nombre). Nada más.
VENTANA_MARCADOR_EXTERNO = 100
RE_MARCADOR_DOC_EXTERNO = re.compile(
    r"(?i)\b(?:del\s+(?:TO|Texto\s+Ordenado)\s+(?:de\s+las\s+normas\s+)?sobre"
    r"|de\s+las\s+normas\s+sobre)\s+['\"“”]?([A-Za-zÁÉÍÓÚáéíóúñÑüÜ\s\-]+)")

# Mapa CERRADO de los 5 TOs del experimento: palabra clave normativa (normalizada:
# lowercase, sin acentos) → archivo del subset. Un marcador cuyo nombre no matchea ninguna
# clave es un TO FUERA del corpus.
DOCS_CORPUS = {
    "clasificacion de deudores": "TO_clasificacion_deudores_actual.pdf",
    "capitales minimos": "TO_capitales_minimos_actual.pdf",
    "exterior y cambios": "TO_exterior_cambios_actual.pdf",
    "proteccion de los usuarios": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
    "regimen informativo": "TO_regimen_informativo_contable_mensual_actual.pdf",
}

NOTA_MADRE_OMITIDA = ("seccion_madre omitida: encabezado de primer nivel = carátula sin "
                      "prosa — sondeo en los 4 TOs, reporte_b3_s1.md hecho b")
NOTA_FUERA_DE_CORPUS = ("mención dirigida a un TO fuera del corpus del experimento — no "
                        "se resuelve intra-documento (corrección B3c)")


def _doc_de_marcador(ventana):
    """Busca el marcador de documento externo en la ventana posterior a la mención.
    Devuelve (doc_destino, marcador_verbatim): (None, None) sin marcador;
    (<archivo del corpus>, marcador) si el nombre matchea DOCS_CORPUS;
    ("fuera_de_corpus", marcador) si no matchea (TO externo al corpus)."""
    m = RE_MARCADOR_DOC_EXTERNO.search(ventana or "")
    if not m:
        return None, None
    nombre = _norm_texto(re.sub(r"-\s+", "", m.group(1)))  # des-hifenado de corte de línea
    for clave, doc in DOCS_CORPUS.items():
        if clave in nombre:
            return doc, m.group(0).strip()
    return "fuera_de_corpus", m.group(0).strip()


def _referencias_de_pasaje(texto, tope=TOPE_REFERENCIAS_INTERNAS):
    """Menciones a otros puntos/secciones en el texto del pasaje del portador, por la
    regex cerrada RE_REFERENCIAS_INTERNAS: en orden de aparición, deduplicadas por
    (punto, doc_destino), con tope. Cada una con su mención de origen verbatim y — B3c —
    la detección del marcador de documento externo en la ventana fija posterior
    (doc_destino: None = intra; archivo del corpus = cross-doc; "fuera_de_corpus").
    Puro, determinístico."""
    texto = texto or ""
    menciones = []
    for m in RE_REFERENCIAS_INTERNAS["punto"].finditer(texto):
        for num in _RE_NUM_PUNTO.findall(m.group(0)):
            menciones.append((m.start(), num, m.group(0), m.end()))
    for m in RE_REFERENCIAS_INTERNAS["seccion"].finditer(texto):
        menciones.append((m.start(), m.group(1), m.group(0), m.end()))
    menciones.sort(key=lambda t: t[0])
    out, vistos = [], set()
    for _, punto, mencion, fin in menciones:
        doc_destino, marcador = _doc_de_marcador(
            texto[fin:fin + VENTANA_MARCADOR_EXTERNO])
        if (punto, doc_destino) in vistos:
            continue
        vistos.add((punto, doc_destino))
        out.append({"punto": punto, "mencion_verbatim": mencion.strip(),
                    "doc_destino": doc_destino, "marcador_verbatim": marcador})
        if len(out) >= tope:
            break
    return out


def _comparativo_de_referencia(ref, doc_portador):
    """Resuelve UNA referencia a comparativo (regla B3c): sin marcador → localize
    intra-documento; marcador a TO del corpus → localize en el doc de destino
    (regla="referencia_interna_cross_doc"); marcador a TO fuera del corpus → comparativo
    "omitido_fuera_de_corpus" SIN localize (nunca intra-documento)."""
    base = {"tipo": "referencia_interna", "punto": ref["punto"],
            "mencion_verbatim": ref["mencion_verbatim"]}
    if ref["doc_destino"] == "fuera_de_corpus":
        return {**base, "regla": "referencia_interna",
                "marcador_verbatim": ref["marcador_verbatim"],
                "estado": "omitido_fuera_de_corpus", "nota": NOTA_FUERA_DE_CORPUS}
    if ref["doc_destino"]:
        doc, regla = ref["doc_destino"], "referencia_interna_cross_doc"
    else:
        doc, regla = doc_portador, "referencia_interna"
    r = _pasaje_de(doc, f"Punto {ref['punto']}")
    out = {**base, "regla": regla, **r,
           "estado": "localizado" if r["localizacion_pdf"] == "ok" else "fallido"}
    if regla == "referencia_interna_cross_doc":
        out["doc_destino"] = doc
        out["marcador_verbatim"] = ref["marcador_verbatim"]
    return out


def _comparativos_de_punto(punto):
    """Regla determinística del diseño §2 (mecánica, sin juicio). Devuelve
    (lista de {tipo, punto, regla}, notas)."""
    niveles = punto.split(".")
    comps, notas = [], []
    if len(niveles) == 1:
        notas.append("sin_comparativos_por_regla: el punto del portador ya es de primer "
                     "nivel (no hay sección madre distinta ni padre un nivel arriba)")
        return comps, notas
    comps.append({"tipo": "seccion_madre", "punto": niveles[0],
                  "regla": "encabezado de la sección madre: primer nivel del punto del portador"})
    if len(niveles) >= 3:
        comps.append({"tipo": "punto_general_un_nivel_arriba",
                      "punto": ".".join(niveles[:-1]),
                      "regla": "mismo prefijo, un nivel arriba (padre inmediato del punto del portador)"})
    else:
        notas.append("padre_inmediato_coincide_con_seccion_madre: el punto tiene 2 niveles; "
                     "el comparativo 'un nivel arriba' es la propia sección madre (no se duplica)")
    return comps, notas


def _pasaje_de(source_doc, location):
    """Envuelve localize registrando la location consultada verbatim."""
    r = localize(source_doc, location)
    return {"source_doc": source_doc, "location_consultada": location,
            "metodo": r["metodo"], "ref": r["ref"], "pasaje": r["pasaje"],
            "localizacion_pdf": r["localizacion_pdf"]}


def construir_paquete_fuentes(caso_json, run, trace_path=None, *,
                              sintoma_F=None, sintoma_P=None):
    """Fetch determinístico de S1 según la semántica pre-registrada del docstring del
    módulo. Puro (sin API): kg + provenances + pdf_locate.

    El síntoma (F, P) sale de la traza post-hoc (`trace_path`, vía _sintoma_de_trace — el
    mismo filtro que build_falla_context) o se inyecta (sintoma_F/sintoma_P, tests sin
    disco). Exactamente una de las dos vías es obligatoria."""
    index = _index_de(run)
    ids_kg = list(index.by_id.keys())

    if trace_path is not None:
        sintoma_F, sintoma_P = _sintoma_de_trace(trace_path)
    elif sintoma_F is None or sintoma_P is None:
        raise ValueError("falta trace_path, o la dupla sintoma_F/sintoma_P (listas)")

    voto = caso_json.get("voto_capa_d")
    if voto is None:
        raise ValueError("construir_paquete_fuentes requiere la salida de la capa "
                         "determinística (falta voto_capa_d)")
    exoneracion_con_sintoma = (
        voto.get("pares_primarios_ganadores") == [] and bool(sintoma_F or sintoma_P))

    entradas = []
    for n_rep, rep in enumerate(caso_json.get("repeticiones") or [], 1):
        if rep.get("formato_invalido"):
            continue
        for j, atrib in enumerate(rep.get("atribuciones") or [], 1):
            causa = atrib.get("causa_capa2")
            if causa in CAUSAS_GATILLO_S1:
                tipo_gatillo = "causa_gatillada"
            elif exoneracion_con_sintoma and causa == "sin_defecto":
                tipo_gatillo = "exoneracion_con_sintoma"
            else:
                continue

            entrada = {
                "id_atribucion": f"rep{n_rep}_atrib{j}",
                "rep": n_rep, "atrib_idx": j,
                "tipo_gatillo": tipo_gatillo,
                "sintoma_capa1": atrib.get("sintoma_capa1"),
                "causa_capa2": causa,
                "jerarquia": atrib.get("jerarquia"),
            }
            portador, n_ids = _extraer_portador(atrib, ids_kg)
            if portador is None:
                entrada.update({"portador_id": None, "n_ids_detectados": n_ids,
                                "estado": "sin_portador_extraible"})
                entradas.append(entrada)
                continue
            entrada["portador_id"] = portador

            provs = index.by_id[portador].provenances or []
            prov_usada, prov_idx, punto = None, None, None
            for i, p in enumerate(provs):
                pt = parse_point(p.get("location"))
                if pt:
                    prov_usada, prov_idx, punto = p, i, pt
                    break
            entrada["provenances_total"] = len(provs)
            if prov_usada is None:
                entrada.update({"estado": "provenance_no_parseable",
                                "provenances_verbatim": provs})
                entradas.append(entrada)
                continue
            entrada.update({"provenance": {"source_doc": prov_usada["source_doc"],
                                           "location": prov_usada["location"]},
                            "provenance_usada_idx": prov_idx, "punto_parseado": punto})

            pasaje = _pasaje_de(prov_usada["source_doc"], prov_usada["location"])
            entrada["pasaje_portador"] = pasaje
            if pasaje["localizacion_pdf"] != "ok":
                entrada["estado"] = "localizacion_fallida"
                entradas.append(entrada)
                continue

            comps, notas = _comparativos_de_punto(punto)
            comparativos = []
            for c in comps:
                if c["tipo"] == "seccion_madre":
                    # corrección B3b (hecho b): omitida SIEMPRE, sin llamar a localize
                    comparativos.append({**c, "estado": "omitido",
                                         "nota": NOTA_MADRE_OMITIDA})
                    continue
                r = _pasaje_de(prov_usada["source_doc"], f"Punto {c['punto']}")
                comparativos.append({**c, **r,
                                     "estado": "localizado" if r["localizacion_pdf"] == "ok"
                                     else "fallido"})
            # corrección B3b (hecho a): referencias internas del TEXTO del pasaje;
            # corrección B3c: resolución por marcador de documento externo
            for ref in _referencias_de_pasaje(pasaje["pasaje"]):
                comparativos.append(
                    _comparativo_de_referencia(ref, prov_usada["source_doc"]))
            entrada["comparativos"] = comparativos
            entrada["notas_regla"] = notas
            # política NO BLOQUEANTE (B3b): completo = el PORTADOR localizó
            entrada["estado"] = "completo"
            entradas.append(entrada)

    return {
        "id_falla": caso_json.get("id_falla"),
        "run": caso_json.get("run"),
        "version_s1": S1_VERSION,
        "gatillo_caso": {
            "exoneracion_con_sintoma": exoneracion_con_sintoma,
            "sintoma_F_n": len(sintoma_F),
            "sintoma_P_n": len(sintoma_P),
        },
        "atribuciones": entradas,
    }


# --------------------------------------------------------------------------- #
# 2. JUICIO S1 (LLM) — implementado; su ejecución con API es decisión de B4+   #
# --------------------------------------------------------------------------- #
def _nodo_para_prompt(nodo):
    return json.dumps({"id": nodo.id, "type": nodo.type, "label": nodo.label,
                       "properties": nodo.properties}, ensure_ascii=False, indent=1)


def _pasajes_para_prompt(entrada):
    partes = [f"[PORTADOR — provenance verbatim: {entrada['provenance']['location']!r} "
              f"({entrada['provenance']['source_doc']}); {entrada['pasaje_portador']['ref']}]\n"
              f"{entrada['pasaje_portador']['pasaje']}"]
    for c in entrada.get("comparativos") or []:
        if c["estado"] == "localizado":
            origen = (f"; mención de origen: {c['mencion_verbatim']!r}"
                      if c.get("mencion_verbatim") else "")
            partes.append(f"[COMPARATIVO {c['tipo']} — regla: {c['regla']}{origen}; "
                          f"{c['ref']}]\n{c['pasaje']}")
        else:
            detalle = f": {c['nota']}" if c.get("nota") else ""
            partes.append(f"[COMPARATIVO {c['tipo']} (Punto {c['punto']}) — "
                          f"{c['estado']}{detalle}]")
    for nota in entrada.get("notas_regla") or []:
        partes.append(f"[NOTA MECÁNICA DEL FETCH: {nota}]")
    return "\n\n".join(partes)


def _prompt_s1(atrib, nodo, entrada):
    vista = {k: atrib.get(k) for k in
             ("sintoma_capa1", "causa_capa2", "lado", "jerarquia", "pata", "evidencia")}
    return S1_PROMPT.format(
        atribucion=json.dumps(vista, ensure_ascii=False, indent=1),
        portador_id=entrada["portador_id"],
        nodo=_nodo_para_prompt(nodo),
        pasajes=_pasajes_para_prompt(entrada))


def _llamada_s1(client, prompt, model):
    """UNA llamada al modelo del verificador; parsea el JSON estricto y valida el esquema
    del diseño §2. Salida inválida → {"error": ...} (cuenta como no decidida)."""
    resp = client.messages.create(model=model, max_tokens=S1_MAX_TOKENS,
                                  messages=[{"role": "user", "content": prompt}])
    texto = "".join(getattr(b, "text", "") for b in resp.content)
    out = _extract_json(texto)
    if not isinstance(out, dict):
        return {"error": "json_no_parseable", "texto_crudo": texto[:2000]}
    faltantes = [k for k in CAMPOS_S1 if k not in out]
    if faltantes:
        return {"error": f"campos_faltantes:{','.join(faltantes)}", "salida_cruda": out}
    if out.get("coinciden") not in COINCIDEN_VALORES:
        return {"error": f"coinciden_invalido:{out.get('coinciden')!r}", "salida_cruda": out}
    return out


def _voto_s1_atrib(salidas, n):
    """Voto propio de S1 por atribución: mayoría estricta ≥ n//2+1 sobre la causa de las
    salidas DECIDIDAS (coinciden ∈ {si, no}); errores y no_determinable no deciden."""
    umbral = n // 2 + 1
    decididas = [s for s in salidas
                 if "error" not in s and s.get("coinciden") in ("si", "no")]
    conteo = {}
    for s in decididas:
        conteo.setdefault(s["causa_confirmada_o_corregida"], []).append(s)
    orden = sorted(conteo.items(), key=lambda kv: (-len(kv[1]), kv[0]))
    ganadora = orden[0] if orden and len(orden[0][1]) >= umbral else None
    return {
        "n": n, "umbral": umbral,
        "decididas": len(decididas),
        "no_decididas": len(salidas) - len(decididas),
        "resultado": "mayoria" if ganadora else "no_determinable",
        "causa_ganadora": ganadora[0] if ganadora else None,
        "votos_ganadores": len(ganadora[1]) if ganadora else None,
    }


def aplicar_s1(caso_json, run, paquete, n=1, *, client=None, model=MODEL_VERIF):
    """Aplica el juicio S1 según la semántica pre-registrada del docstring del módulo.
    Juzga SOLO las atribuciones con paquete "completo"; el resto va a triage_s1 con motivo
    fuente_no_verificable. NUNCA borra la emisión de v6.1-D: anota capa_s1, recomputa
    voto_s1 y preserva voto / voto_capa_d / voto_pre_d6 intactos.

    `client` se inyecta (en producción, el cliente del verificador; en tests, un mock).
    Sin atribuciones a juzgar no se hace ninguna llamada (client puede ser None)."""
    index = _index_de(run)
    salida = copy.deepcopy(caso_json)
    reps = salida.get("repeticiones") or []

    motivos, flags = [], []
    juzgadas = corregidas = no_det = fallidas_fetch = 0

    for entrada in paquete.get("atribuciones") or []:
        atrib = reps[entrada["rep"] - 1]["atribuciones"][entrada["atrib_idx"] - 1]
        base = {"version": S1_VERSION,
                "id_atribucion": entrada["id_atribucion"],
                "tipo_gatillo": entrada["tipo_gatillo"],
                "estado_fetch": entrada["estado"],
                "emision_v61d": {"sintoma_capa1": atrib.get("sintoma_capa1"),
                                 "causa_capa2": atrib.get("causa_capa2"),
                                 "jerarquia": atrib.get("jerarquia")}}
        if entrada["estado"] != "completo":
            atrib["capa_s1"] = {**base, "accion": "fuente_no_verificable",
                                "corrigio": False, "triage": True}
            fallidas_fetch += 1
            if "fuente_no_verificable" not in motivos:
                motivos.append("fuente_no_verificable")
            flags.append(f"S1: {entrada['id_atribucion']} — fetch {entrada['estado']}")
            continue

        if client is None:
            raise ValueError("aplicar_s1 requiere client para juzgar paquetes completos")
        nodo = index.by_id[entrada["portador_id"]]
        prompt = _prompt_s1(atrib, nodo, entrada)
        salidas = [_llamada_s1(client, prompt, model) for _ in range(n)]
        voto_atrib = _voto_s1_atrib(salidas, n)
        juzgadas += 1

        if voto_atrib["resultado"] != "mayoria":
            atrib["capa_s1"] = {**base, "salidas_s1": salidas, "voto_s1_atrib": voto_atrib,
                                "accion": "no_determinable", "corrigio": False,
                                "triage": True}
            no_det += 1
            if "fuente_no_verificable" not in motivos:
                motivos.append("fuente_no_verificable")
            flags.append(f"S1: {entrada['id_atribucion']} — no_determinable "
                         f"({voto_atrib['decididas']}/{n} decididas)")
            continue

        causa_final = voto_atrib["causa_ganadora"]
        corrigio = causa_final != atrib.get("causa_capa2")
        atrib["capa_s1"] = {**base, "salidas_s1": salidas, "voto_s1_atrib": voto_atrib,
                            "corrigio": corrigio, "causa_post_s1": causa_final,
                            "triage": False}
        if corrigio:
            atrib["causa_capa2"] = causa_final
            corregidas += 1

    salida["voto_s1"] = _recomputar_voto(reps)
    salida["triage_s1"] = {"triage": bool(motivos), "motivos": motivos, "flags": flags}
    salida["resumen_s1"] = {
        "gatilladas": len(paquete.get("atribuciones") or []),
        "juzgadas_llm": juzgadas,
        "corregidas": corregidas,
        "no_determinable": no_det,
        "fetch_fallido": fallidas_fetch,
        "exoneracion_con_sintoma": paquete.get("gatillo_caso", {}).get(
            "exoneracion_con_sintoma", False),
    }
    salida["version_capa_s1"] = S1_VERSION
    return salida


# --------------------------------------------------------------------------- #
# CLI                                                                          #
# --------------------------------------------------------------------------- #
def _trace_default(caso_json):
    """Traza post-hoc canónica derivada de id_falla (run/CQ-XXX) — mismo layout que usa el
    pipeline: posthoc_run/traces/off/{run}/{qid}.json. Overrideable con --trace."""
    run, qid = caso_json["id_falla"].split("/")
    return Path(__file__).resolve().parent / "posthoc_run" / "traces" / "off" / run / f"{qid}.json"


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="S1 — segunda pasada con fuentes forzadas (v7 = v6.1-D + S1)")
    ap.add_argument("--caso", required=True, help="path al JSON _capa_d (salida de v6.1-D)")
    ap.add_argument("--run", required=True, help="clave del run (p. ej. run_3)")
    ap.add_argument("--out", required=True, help="path del JSON de salida")
    ap.add_argument("--n", type=int, default=1,
                    help="repeticiones del juicio S1 por atribución (política a decidir en B4)")
    ap.add_argument("--solo-fetch", action="store_true",
                    help="corre SOLO el fetch determinístico y emite el paquete (sin API)")
    ap.add_argument("--trace", default=None,
                    help="traza post-hoc del caso (default: derivada de id_falla)")
    args = ap.parse_args(argv)

    caso = json.load(open(args.caso))
    trace = args.trace or _trace_default(caso)
    paquete = construir_paquete_fuentes(caso, args.run, trace_path=trace)

    if args.solo_fetch:
        with open(args.out, "w") as f:
            json.dump(paquete, f, ensure_ascii=False, indent=1)
        print(json.dumps({"out": args.out, "version_s1": S1_VERSION, "solo_fetch": True,
                          "gatillo_caso": paquete["gatillo_caso"],
                          "atribuciones": [{k: e.get(k) for k in
                                            ("id_atribucion", "tipo_gatillo", "estado",
                                             "portador_id")}
                                           for e in paquete["atribuciones"]]},
                         ensure_ascii=False, indent=1))
        return

    # Modo completo (juicio con LLM). La caché / política de N se decide en B4.
    import anthropic
    client = anthropic.Anthropic(max_retries=3)
    salida = aplicar_s1(caso, args.run, paquete, n=args.n, client=client)
    with open(args.out, "w") as f:
        json.dump(salida, f, ensure_ascii=False, indent=1)
    print(json.dumps({"out": args.out, "version_capa_s1": salida["version_capa_s1"],
                      "resumen_s1": salida["resumen_s1"],
                      "triage_s1": salida["triage_s1"],
                      "voto_s1": salida["voto_s1"]}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
