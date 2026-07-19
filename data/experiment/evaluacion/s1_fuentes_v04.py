"""s1_fuentes_v04.py — S1 v0.4 = v0.3.1 + guarda de dominio + portador robusto.

Implementa `docs/diseno_ciclo2.md` §3-§4 (commit b84668e). **MÓDULO NUEVO AL LADO:**
s1_fuentes.py (v0.3.1, baseline congelado) se IMPORTA sin modificarse. Qué se importa y
qué se replica (declaración exigida por la unidad):

- IMPORTADO tal cual (congelado): construir_paquete_fuentes (el fetch v0.3.1 entero),
  _prompt_s1, _prompt_s1_exoneracion, _pasajes_para_prompt, _llamada_s1 (incluye las
  guardas de dominio de vocabulario de B4.5), _voto_s1_atrib, _nodo_para_prompt,
  S1_MAX_TOKENS, MODEL_VERIF; _recomputar_voto/_sintoma_de_trace/_mapear_claim de
  capa_deterministica; _index_de de test_alcanzabilidad; pdf_pages/_prose_score de
  pdf_locate.
- REPLICADO (con la declaración de por qué): el LOOP de juicio de aplicar_s1 (v0.3.1) —
  los estados nuevos (fuente_cross_doc / completo_por_contenido / contenido_no_unico) y
  las dos guardas no caben en el congelado sin editarlo; el flujo replicado conserva
  íntegras la política conservadora, la regla mecánica de jerarquía (v0.3) y la
  instrumentación de usage (B4.2).

GUARDA DE DOMINIO (§3): territorio = tos_fuente de la pregunta, leído del EVAL SET
SELLADO (default: data/experiment/evaluacion/queries/eval_set_cqn.json). Si el
source_doc del portador fetcheado ∉ tos_fuente → NI exonerar NI re-atribuir: estado
"fuente_cross_doc", triage con motivo `fuente_cross_doc` (anotación par
documento-portador/territorio) y LA LLAMADA LLM NO SE HACE (guarda a nivel fetch: cero
tokens, cero oportunidad de flip).

PORTADOR ROBUSTO (§4): fallback por CONTENIDO cuando el fetch por numeral falló
(sin_portador_extraible con candidatos citados / provenance_no_parseable /
localizacion_fallida), y pasaje EXTRA `portador_por_contenido` cuando el numeral localizó
pero el contenido localiza único y distinto. Mecanismo: los K literales más largos del
contenido del nodo (label + values de properties; normalización de la casa + des-hifenado)
por substring sobre el texto por página de los TOs DEL TERRITORIO (la guarda §3 aplica
también acá), ventana con página. TRES GUARDAS anti-falso-portador:
  (i) longitud mínima UMBRAL_CONTENIDO (chars normalizados; calibrado en dev — ver
      reporte de la unidad 2);
  (ii) unicidad: match en >1 documento del territorio o >MAX_UBICACIONES →
      "contenido_no_unico", triage;
  (iii) rótulo `portador_por_contenido` en el prompt; en la RAMA DE EXONERACIÓN un
      paquete cuyo portador es SOLO-por-contenido NUNCA confirma sin_defecto — si el
      voto da sin_defecto, va a triage `exoneracion_solo_por_contenido` (decide causa o
      deriva, no exonera).

S1_VERSION_V04 = "s1-v0.4-dev".
"""

import argparse
import copy
import json
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from s1_fuentes import (                  # v0.3.1 congelada — SOLO imports
    construir_paquete_fuentes, _prompt_s1, _prompt_s1_exoneracion,
    _pasajes_para_prompt, _llamada_s1, _voto_s1_atrib, _nodo_para_prompt,
    MODEL_VERIF,
)
from capa_deterministica import _recomputar_voto, _sintoma_de_trace, _mapear_claim
from test_alcanzabilidad import _index_de
from pdf_locate import pdf_pages, _prose_score

S1_VERSION_V04 = "s1-v0.4b-dev"   # unidad 2b: + requisito de fundamento (§4bis)
EVAL_SET_DEFAULT = (Path(__file__).resolve().parent / "queries" / "eval_set_cqn.json")

# Guardas del portador por contenido (calibradas en dev — documentadas en el reporte U2)
UMBRAL_CONTENIDO = 60      # chars normalizados mínimos del literal
MAX_UBICACIONES = 3        # >3 ocurrencias en el doc → contenido_no_unico
K_LITERALES = 3            # los K values más largos del contenido del nodo
VENTANA_CONTENIDO = 1400   # ventana raw alrededor del match (como localize)


# --------------------------------------------------------------------------- #
# Normalización con mapa de offsets (búsqueda normalizada, pasaje RAW)         #
# --------------------------------------------------------------------------- #
def _norm_con_mapa(texto):
    """(norm, mapa) — lowercase, sin acentos, espacios colapsados, des-hifenado de corte
    de línea ("-\\n"); mapa[i_norm] = i_raw del primer char de origen."""
    out, mapa = [], []
    i, n = 0, len(texto)
    en_espacio = False
    while i < n:
        ch = texto[i]
        if ch == "-" and i + 1 < n and texto[i + 1] == "\n":   # des-hifenado
            i += 2
            continue
        if ch.isspace():
            if not en_espacio and out:
                out.append(" "); mapa.append(i)
            en_espacio = True
            i += 1
            continue
        en_espacio = False
        for d in unicodedata.normalize("NFD", ch.lower()):
            if unicodedata.category(d) != "Mn":
                out.append(d); mapa.append(i)
        i += 1
    return "".join(out), mapa


def _norm_simple(s):
    n, _ = _norm_con_mapa(str(s or ""))
    return n


# --------------------------------------------------------------------------- #
# Portador por contenido                                                        #
# --------------------------------------------------------------------------- #
_DOC_CACHE = {}

def _doc_norm(doc):
    if doc not in _DOC_CACHE:
        pags = pdf_pages(doc)
        raw = "\n".join(pags)
        offsets = []
        pos = 0
        for p in pags:
            offsets.append(pos)
            pos += len(p) + 1
        norm, mapa = _norm_con_mapa(raw)
        _DOC_CACHE[doc] = (raw, norm, mapa, offsets)
    return _DOC_CACHE[doc]


def _pagina_de(offsets, raw_idx):
    pg = 1
    for i, off in enumerate(offsets, 1):
        if raw_idx >= off:
            pg = i
    return pg


def _literales_de(nodo):
    cands = [nodo.label or ""] + [str(v) for v in (nodo.properties or {}).values()
                                  if isinstance(v, (str, int, float))]
    con_norm = [(c, _norm_simple(c)) for c in cands]
    largos = [(c, nc) for c, nc in con_norm if len(nc) >= UMBRAL_CONTENIDO]
    largos.sort(key=lambda t: -len(t[1]))
    return largos[:K_LITERALES]


VENTANA_PALABRAS = 8       # iteración 1 (dev): ancla de 8 palabras + extensión
SLACK_EXTENSION = 40       # tolerancia de corrimiento entre ventanas consecutivas


def _ocurrencias_span(lit_norm, norm_doc):
    """Ocurrencias del literal en el doc normalizado, por match EXACTO o — iteración 1
    del dev (los nodos divergen del corpus en conectores) — por ANCLA de
    VENTANA_PALABRAS palabras + extensión greedy de ventanas consecutivas (slack
    SLACK_EXTENSION). Devuelve [(idx_norm, largo_span)]; la guarda de unicidad cuenta
    las ocurrencias del ANCLA y el umbral se exige sobre el SPAN."""
    out, pos = [], 0
    while True:                                   # 1) match exacto (camino original)
        j = norm_doc.find(lit_norm, pos)
        if j < 0:
            break
        out.append((j, len(lit_norm)))
        pos = j + 1
    if out:
        return out
    palabras = lit_norm.split(" ")
    if len(palabras) < VENTANA_PALABRAS:
        return []
    ventanas = [" ".join(palabras[i:i + VENTANA_PALABRAS])
                for i in range(0, len(palabras) - VENTANA_PALABRAS + 1)]
    ancla = None
    for vi, v in enumerate(ventanas):             # 2) primera ventana que matchea = ancla
        if norm_doc.find(v) >= 0:
            ancla = (vi, v)
            break
    if ancla is None:
        return []
    vi, v = ancla
    anclas, pos = [], 0
    while True:                                   # unicidad: TODAS las ocurrencias del ancla
        j = norm_doc.find(v, pos)
        if j < 0:
            break
        anclas.append(j)
        pos = j + 1
    for j in anclas:
        fin = j + len(v)
        pos_prev = j
        for k_v in range(vi + 1, len(ventanas)):  # extensión greedy hacia adelante
            w = ventanas[k_v]
            # las ventanas SOLAPAN con paso 1 palabra: la siguiente arranca cerca de
            # pos_prev + len(primera palabra) + 1, no al final del span
            esperado = pos_prev + len(palabras[k_v - 1]) + 1
            k = norm_doc.find(w, max(0, esperado - SLACK_EXTENSION),
                              esperado + SLACK_EXTENSION + len(w))
            if k < 0:
                break
            fin = max(fin, k + len(w))
            pos_prev = k
        out.append((j, fin - j))
    return out


def fetch_por_contenido(nodo, territorio):
    """Busca el CONTENIDO del nodo en los TOs del territorio. Devuelve
    {"estado": "ok"|"contenido_no_unico"|"sin_match", ...detalle}."""
    lits = _literales_de(nodo)
    if not lits:
        return {"estado": "sin_match", "motivo": f"sin literales ≥{UMBRAL_CONTENIDO} chars"}
    for lit_raw, lit_norm in lits:
        hits = []   # (doc, [raw_idx, ...])
        occ_por_doc = {}
        for doc in territorio:
            raw, norm, mapa, offsets = _doc_norm(doc)
            occ = [(mapa[j], largo) for j, largo in _ocurrencias_span(lit_norm, norm)
                   if largo >= UMBRAL_CONTENIDO]
            if occ:
                occ_por_doc[doc] = occ
                hits.append((doc, [i for i, _ in occ]))
        if not hits:
            continue
        if len(hits) > 1:
            return {"estado": "contenido_no_unico",
                    "literal": lit_raw[:120],
                    "docs_con_match": [d for d, _ in hits]}
        doc, idxs = hits[0]
        if len(idxs) > MAX_UBICACIONES:
            return {"estado": "contenido_no_unico", "literal": lit_raw[:120],
                    "docs_con_match": [doc], "ocurrencias": len(idxs)}
        raw, norm, mapa, offsets = _doc_norm(doc)
        # entre ≤MAX ocurrencias: la de mayor prose_score (mecanismo de la casa)
        mejor = max(idxs, key=lambda i: _prose_score(raw[i:i + 200]))
        span = max(l for i, l in occ_por_doc[doc] if i == mejor)
        a = max(0, mejor - VENTANA_CONTENIDO // 2)
        pasaje = raw[a:a + VENTANA_CONTENIDO].strip()
        return {"estado": "ok", "doc": doc, "pagina": _pagina_de(offsets, mejor),
                "literal": lit_raw[:160], "ocurrencias": len(idxs),
                "raw_idx": mejor, "span": span, "pasaje": pasaje}
    return {"estado": "sin_match",
            "motivo": "ningún literal del contenido localiza en el territorio"}


# --------------------------------------------------------------------------- #
# Post-procesamiento del paquete (guarda de dominio + fallback)                 #
# --------------------------------------------------------------------------- #
FALLIDOS_RESCATABLES = ("sin_portador_extraible", "provenance_no_parseable",
                        "localizacion_fallida")

import re as _re


def _pasaje_funda(nodo, entrada):
    """Requisito de fundamento (§4bis, unidad 2b): el contenido del nodo debe localizar
    DENTRO del pasaje por numeral (o de su página) con la MISMA maquinaria del portador
    por contenido (ancla + extensión, span ≥ UMBRAL_CONTENIDO). Devuelve
    (funda: bool, detalle)."""
    pas = (entrada.get("pasaje_portador") or {}).get("pasaje") or ""
    textos = [("pasaje", _norm_simple(pas))]
    ref = (entrada.get("pasaje_portador") or {}).get("ref") or ""
    doc = (entrada.get("provenance") or {}).get("source_doc")
    m = _re.search(r"p[áa]g\s+(\d+)", ref)
    if doc and m:
        try:
            pagina = pdf_pages(doc)[int(m.group(1)) - 1]
            textos.append((f"página {m.group(1)}", _norm_simple(pagina)))
        except Exception:
            pass
    mejor = 0
    for lit_raw, lit_norm in _literales_de(nodo):
        for donde, t in textos:
            occ = [largo for _, largo in _ocurrencias_span(lit_norm, t)
                   if largo >= UMBRAL_CONTENIDO]
            if occ:
                return True, {"donde": donde, "span": max(occ), "literal": lit_raw[:100]}
            mejor = max([mejor] + [largo for _, largo in _ocurrencias_span(lit_norm, t)])
    return False, {"span_maximo": mejor, "umbral": UMBRAL_CONTENIDO}


def _candidatos_de_entrada(entrada, capa_json, ids_kg):
    """Ids candidatos para el fallback: el portador si existe; si no, los ids del kg
    presentes en la ubicación citada (los mismos que el extractor vio y no pudo
    desambiguar)."""
    if entrada.get("portador_id"):
        return [entrada["portador_id"]]
    a = capa_json["repeticiones"][entrada["rep"] - 1]["atribuciones"][entrada["atrib_idx"] - 1]
    ev = (a.get("evidencia") or {}).get("nodo") or {}
    out = []
    for campo in ("ubicacion", "quote"):
        t = ev.get(campo) or ""
        m = sorted({nid for nid in ids_kg if nid in t})
        if m:
            out = m
            break
    return out


def preparar_paquete_v04(capa_json, run, trace_path, tos_fuente):
    """El fetch congelado de v0.3.1 + las dos piezas del ciclo 2, como post-proceso."""
    index = _index_de(run)
    ids_kg = list(index.by_id.keys())
    paq = construir_paquete_fuentes(capa_json, index, trace_path=trace_path)
    paq["version_s1"] = S1_VERSION_V04
    paq["territorio"] = list(tos_fuente)
    for e in paq["atribuciones"]:
        if e["estado"] == "completo":
            doc = e["provenance"]["source_doc"]
            if doc not in tos_fuente:
                # GUARDA DE DOMINIO (§3): ni exonerar ni re-atribuir; cero llamadas
                e["estado"] = "fuente_cross_doc"
                e["guarda_dominio"] = {"source_doc_portador": doc,
                                       "territorio": list(tos_fuente)}
                continue
            # enriquecimiento: pasaje extra por contenido, si localiza único y distinto
            r = fetch_por_contenido(index.by_id[e["portador_id"]], tos_fuente)
            if r["estado"] == "ok" and _norm_simple(r["pasaje"][:200]) not in \
               _norm_simple((e.get("pasaje_portador") or {}).get("pasaje") or ""):
                e["pasaje_portador_contenido"] = r
            # §4bis (unidad 2b) — requisito de fundamento: exento si hay pasaje extra
            # por contenido (funda por construcción); si no, el pasaje por numeral (o su
            # página) debe fundar el contenido del nodo → si no, fuente_no_funda (a
            # nivel fetch: sin llamada LLM)
            if not e.get("pasaje_portador_contenido"):
                funda, det = _pasaje_funda(index.by_id[e["portador_id"]], e)
                if not funda:
                    e["estado"] = "fuente_no_funda"
                    e["fundamento"] = det
                else:
                    e["fundamento"] = det
        elif e["estado"] in FALLIDOS_RESCATABLES:
            candidatos = _candidatos_de_entrada(e, capa_json, ids_kg)
            oks = []
            for nid in candidatos:
                r = fetch_por_contenido(index.by_id[nid], tos_fuente)
                if r["estado"] == "ok":
                    oks.append((nid, r))
                elif r["estado"] == "contenido_no_unico":
                    oks.append((nid, r))
            unicos = [(nid, r) for nid, r in oks if r["estado"] == "ok"]
            # iteración 2 (dev): la UNICIDAD se evalúa sobre la UBICACIÓN, no sobre el
            # número de candidatos — candidatos múltiples que localizan en el MISMO
            # pasaje (mismo doc, |Δidx| ≤ VENTANA/2) corroboran UN portador textual; se
            # elige el de span más largo (desempate: id orden alfabético).
            if len(unicos) > 1:
                docs = {r["doc"] for _, r in unicos}
                idxs = [r["raw_idx"] for _, r in unicos]
                if len(docs) == 1 and max(idxs) - min(idxs) <= VENTANA_CONTENIDO // 2:
                    unicos = [sorted(unicos, key=lambda t: (-t[1]["span"], t[0]))[0]]
            if len(unicos) == 1:
                nid, r = unicos[0]
                e["estado_numeral"] = e["estado"]
                e["estado"] = "completo_por_contenido"
                e["portador_id"] = nid
                e["provenance"] = {"source_doc": r["doc"],
                                   "location": f"portador_por_contenido (pág {r['pagina']})"}
                e["pasaje_portador"] = {"source_doc": r["doc"],
                                        "location_consultada": "(por contenido)",
                                        "metodo": "contenido",
                                        "ref": f"portador_por_contenido — {r['doc']} pág {r['pagina']} "
                                               f"({r['ocurrencias']} ocurrencia/s)",
                                        "pasaje": r["pasaje"],
                                        "localizacion_pdf": "ok"}
                e["comparativos"] = []
                e["notas_regla"] = ["portador_por_contenido: nunca habilita exoneración "
                                    "por sí solo (guarda iii, diseño §4)"]
                e["fallback_contenido"] = {"literal": r["literal"],
                                           "candidatos_probados": candidatos}
            elif len(unicos) > 1 or any(r["estado"] == "contenido_no_unico" for _, r in oks):
                e["estado_numeral"] = e["estado"]
                e["estado"] = "contenido_no_unico"
                e["fallback_contenido"] = {"candidatos_probados": candidatos,
                                           "detalle": [r for _, r in oks]}
            # sin match en ninguno → el estado original queda
    return paq


# --------------------------------------------------------------------------- #
# Juicio v0.4 (loop replicado de v0.3.1 + estados nuevos y guardas)            #
# --------------------------------------------------------------------------- #
def aplicar_s1_v04(caso_json, run, paquete, n=1, *, client=None, model=MODEL_VERIF,
                   sintoma_F=None, sintoma_P=None, respuesta_agente=None):
    index = _index_de(run)
    salida = copy.deepcopy(caso_json)
    reps = salida.get("repeticiones") or []

    motivos, flags = [], []
    juzgadas = corregidas = no_det = fallidas_fetch = cross_doc = no_funda = 0
    tokens_in_s1 = tokens_out_s1 = 0

    def _motivo(m):
        if m not in motivos:
            motivos.append(m)

    for entrada in paquete.get("atribuciones") or []:
        atrib = reps[entrada["rep"] - 1]["atribuciones"][entrada["atrib_idx"] - 1]
        base = {"version": S1_VERSION_V04,
                "id_atribucion": entrada["id_atribucion"],
                "tipo_gatillo": entrada["tipo_gatillo"],
                "estado_fetch": entrada["estado"],
                "emision_v61d": {"sintoma_capa1": atrib.get("sintoma_capa1"),
                                 "causa_capa2": atrib.get("causa_capa2"),
                                 "jerarquia": atrib.get("jerarquia")}}
        if entrada["estado"] == "fuente_cross_doc":
            atrib["capa_s1"] = {**base, "accion": "fuente_cross_doc",
                                "guarda_dominio": entrada.get("guarda_dominio"),
                                "corrigio": False, "triage": True}
            cross_doc += 1
            _motivo("fuente_cross_doc")
            flags.append(f"S1: {entrada['id_atribucion']} — fuente_cross_doc "
                         f"({entrada['guarda_dominio']['source_doc_portador']} ∉ territorio)")
            continue
        if entrada["estado"] == "fuente_no_funda":
            # §4bis (unidad 2b): el pasaje por numeral no funda el contenido del nodo →
            # triage, SIN llamada LLM (cero oportunidad de flip)
            atrib["capa_s1"] = {**base, "accion": "fuente_no_funda",
                                "fundamento": entrada.get("fundamento"),
                                "corrigio": False, "triage": True}
            no_funda += 1
            _motivo("fuente_no_funda")
            flags.append(f"S1: {entrada['id_atribucion']} — fuente_no_funda "
                         f"(span máx {entrada.get('fundamento', {}).get('span_maximo')})")
            continue
        if entrada["estado"] not in ("completo", "completo_por_contenido"):
            atrib["capa_s1"] = {**base, "accion": "fuente_no_verificable",
                                "corrigio": False, "triage": True}
            fallidas_fetch += 1
            _motivo("fuente_no_verificable")
            flags.append(f"S1: {entrada['id_atribucion']} — fetch {entrada['estado']}")
            continue

        if client is None:
            raise ValueError("aplicar_s1_v04 requiere client para juzgar")
        nodo = index.by_id[entrada["portador_id"]]
        entrada_prompt = entrada
        if entrada.get("pasaje_portador_contenido"):
            entrada_prompt = copy.deepcopy(entrada)
            r = entrada["pasaje_portador_contenido"]
            entrada_prompt.setdefault("comparativos", []).append({
                "tipo": "portador_por_contenido", "punto": None,
                "regla": "portador_por_contenido (fallback §4; pasaje que FUNDA el contenido)",
                "estado": "localizado", "mencion_verbatim": None,
                "ref": f"{r['doc']} pág {r['pagina']} (por contenido)",
                "pasaje": r["pasaje"], "localizacion_pdf": "ok"})
        if entrada["tipo_gatillo"] == "exoneracion_con_sintoma":
            esquema = "exoneracion"
            prompt = _prompt_s1_exoneracion(atrib, nodo, entrada_prompt, sintoma_P,
                                            respuesta_agente)
        else:
            esquema = "causa"
            prompt = _prompt_s1(atrib, nodo, entrada_prompt, sintoma_F, sintoma_P)
        llamadas = [_llamada_s1(client, prompt, model, esquema=esquema)
                    for _ in range(n)]
        salidas = [s for s, _ in llamadas]
        usages = [u for _, u in llamadas]
        tokens_in_s1 += sum(u.get("input_tokens") or 0 for u in usages)
        tokens_out_s1 += sum(u.get("output_tokens") or 0 for u in usages)
        voto_atrib = _voto_s1_atrib(salidas, n, esquema=esquema)
        juzgadas += 1

        if voto_atrib["resultado"] != "mayoria":
            atrib["capa_s1"] = {**base, "esquema": esquema, "salidas_s1": salidas,
                                "usage_s1": usages, "voto_s1_atrib": voto_atrib,
                                "accion": "no_determinable", "corrigio": False,
                                "triage": True}
            no_det += 1
            _motivo("fuente_no_verificable")
            flags.append(f"S1: {entrada['id_atribucion']} — no_determinable "
                         f"({voto_atrib['decididas']}/{n} decididas)")
            continue

        causa_final = voto_atrib["causa_ganadora"]
        # GUARDA (iii) §4: portador SOLO-por-contenido nunca confirma una exoneración
        if (esquema == "exoneracion" and entrada["estado"] == "completo_por_contenido"
                and causa_final == "sin_defecto"):
            atrib["capa_s1"] = {**base, "esquema": esquema, "salidas_s1": salidas,
                                "usage_s1": usages, "voto_s1_atrib": voto_atrib,
                                "accion": "exoneracion_solo_por_contenido",
                                "corrigio": False, "triage": True}
            _motivo("exoneracion_solo_por_contenido")
            flags.append(f"S1: {entrada['id_atribucion']} — exoneración con portador "
                         f"solo-por-contenido → deriva, no exonera")
            continue

        if esquema == "causa":
            sintoma_final = voto_atrib["sintoma_ganador"]
        else:
            sintoma_final = ("context_recall" if causa_final != "sin_defecto"
                            else atrib.get("sintoma_capa1"))
        corrigio = (causa_final != atrib.get("causa_capa2")
                    or sintoma_final != atrib.get("sintoma_capa1"))
        anot = {**base, "esquema": esquema, "salidas_s1": salidas, "usage_s1": usages,
                "voto_s1_atrib": voto_atrib, "corrigio": corrigio,
                "par_post_s1": [sintoma_final, causa_final],
                "causa_post_s1": causa_final, "triage": False}
        if corrigio:
            atrib["sintoma_capa1"] = sintoma_final
            atrib["causa_capa2"] = causa_final
            corregidas += 1
            # regla mecánica de jerarquía (v0.3), replicada
            if esquema == "exoneracion" and causa_final != "sin_defecto":
                anot["jerarquia_original"] = atrib.get("jerarquia")
                if sintoma_P:
                    if len(sintoma_P) == 1:
                        atrib["pata"] = sintoma_P[0]
                    else:
                        atrib["pata"] = list(sintoma_P)
                        anot["nota"] = "mecanica_sin_mapeo"
                    atrib["jerarquia"] = "primaria"
                else:
                    quote = ((atrib.get("evidencia") or {}).get("afirmacion")
                             or {}).get("quote") or ""
                    mapeados = _mapear_claim(quote, sintoma_F or [])
                    atrib["jerarquia"] = ("primaria"
                                          if any(c.get("central") for c in mapeados)
                                          else "secundaria")
                    anot["mapeo_claims"] = [c.get("enunciado") for c in mapeados]
                anot["jerarquia_post_s1"] = atrib["jerarquia"]
        atrib["capa_s1"] = anot

    salida["voto_s1"] = _recomputar_voto(reps)
    salida["triage_s1"] = {"triage": bool(motivos), "motivos": motivos, "flags": flags}
    salida["resumen_s1"] = {
        "gatilladas": len(paquete.get("atribuciones") or []),
        "juzgadas_llm": juzgadas,
        "corregidas": corregidas,
        "no_determinable": no_det,
        "fetch_fallido": fallidas_fetch,
        "cross_doc_bloqueadas": cross_doc,
        "fuente_no_funda": no_funda,
        "tokens_in_s1": tokens_in_s1,
        "tokens_out_s1": tokens_out_s1,
        "exoneracion_con_sintoma": paquete.get("gatillo_caso", {}).get(
            "exoneracion_con_sintoma", False),
    }
    salida["version_capa_s1"] = S1_VERSION_V04
    return salida


# --------------------------------------------------------------------------- #
# CLI                                                                          #
# --------------------------------------------------------------------------- #
def main(argv=None):
    ap = argparse.ArgumentParser(description="S1 v0.4 (guarda de dominio + portador robusto)")
    ap.add_argument("--caso", required=True)
    ap.add_argument("--run", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--n", type=int, default=1)
    ap.add_argument("--trace", required=True)
    ap.add_argument("--eval-set", default=str(EVAL_SET_DEFAULT))
    ap.add_argument("--solo-fetch", action="store_true")
    args = ap.parse_args(argv)

    caso = json.load(open(args.caso))
    qid = caso["id_falla"].split("/")[1]
    ev = json.load(open(args.eval_set))
    preguntas = ev["preguntas"] if isinstance(ev, dict) else ev
    tos = next(q["tos_fuente"] for q in preguntas if q["id"] == qid)

    paquete = preparar_paquete_v04(caso, args.run, args.trace, tos)
    if args.solo_fetch:
        json.dump(paquete, open(args.out, "w"), ensure_ascii=False, indent=1)
        print(json.dumps({"out": args.out, "solo_fetch": True,
                          "estados": [{e["id_atribucion"]: e["estado"]}
                                      for e in paquete["atribuciones"]]},
                         ensure_ascii=False, indent=1))
        return

    from dotenv import load_dotenv
    import os, anthropic
    load_dotenv(Path(__file__).resolve().parent / ".env")
    client = anthropic.Anthropic(max_retries=3)
    sintoma_F, sintoma_P = _sintoma_de_trace(args.trace)
    elem = json.load(open(args.trace))[0]
    respuesta_agente = json.dumps(elem["trace"].get("final_json"), ensure_ascii=False,
                                  indent=1)
    salida = aplicar_s1_v04(caso, args.run, paquete, n=args.n, client=client,
                            sintoma_F=sintoma_F, sintoma_P=sintoma_P,
                            respuesta_agente=respuesta_agente)
    json.dump(salida, open(args.out, "w"), ensure_ascii=False, indent=1)
    print(json.dumps({"out": args.out, "version_capa_s1": salida["version_capa_s1"],
                      "resumen_s1": salida["resumen_s1"],
                      "triage_s1": salida["triage_s1"],
                      "voto_s1": salida["voto_s1"]}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
