"""
verifier_pilot.py — PILOTO (10 claims) de dos evaluadores de calidad del KG (Fase 2.3+).

NO toca nada congelado ni los runners existentes. Lee:
  - trazas post-hoc (posthoc_run/traces/) para la descomposición del juez (step2.verificaciones)
    y la respuesta final del agente.
  - crudos de los tool_results desde cache/calls.db, FILTRADOS por el think correcto
    (think=0 para off/, think=1 para on/), para recuperar los nodos que el agente vio.
  - los PDFs de data/experiment/subset/ (no raw/) para el pasaje fuente.

Dos evaluadores:
  · Verificador B (claim-level): por cada afirmación incorrecta del agente, determina si el
    defecto está en el KG o en el agente, comparando el nodo contra el PDF. Capa 1 (hechos) +
    Capa 2 (causa, con razonamiento). Mapeo claim→nodo con Haiku (sin embeddings, decisión).
    Verificación principal con Opus.
  · Evaluador A (ciego): por cada respuesta, calidad PERCIBIDA por un usuario que no puede
    verificar (claridad / se sostiene / abstención / confianza). Solo pregunta + respuesta
    (incluidas citas). Sonnet. Flag incluir_trayectoria (default False).

Las propias llamadas LLM del piloto se cachean en cache/verifier_pilot.db (separado de calls.db).

Uso:
  python verifier_pilot.py --preflight   # sin API: selección + nodos + PDF (mecánico)
  python verifier_pilot.py               # corrida completa (requiere API)
"""
from __future__ import annotations
import json, re, sys, unicodedata
from pathlib import Path

from loader import load_graph, EVAL_DIR
import llm_cache as lc

SUBSET_DIR = EVAL_DIR.parent / "subset"
EVAL_SET = EVAL_DIR / "queries" / "eval_set_v1.json"
OUT_DIR = EVAL_DIR / "posthoc_run" / "pilot_verificador"
PILOT_DB = EVAL_DIR / "cache" / "verifier_pilot.db"

MODEL_MAP = "claude-haiku-4-5-20251001"   # mapeo claim→nodo
MODEL_VERIF = "claude-opus-4-8"            # verificación principal (precisión del mapa)
MODEL_EVALA = "claude-sonnet-4-6"          # evaluador A ciego

# --------------------------------------------------------------------------- #
# Selección de los 10 claims del piloto                                       #
# --------------------------------------------------------------------------- #
# 4 dirigidos (causa que la autora ya analizó a mano) + 6 elegidos por diversidad.
PILOT = [
    # --- 4 dirigidos ---
    dict(label="off", run="run_1", qid="CQ-010", want="falso", kw="1.500",
         expected="contenido_kg",
         why="DIRIGIDO: el nodo dice 1.500 millones, el PDF dice 5.000 → defecto de contenido del KG."),
    dict(label="off", run="run_5", qid="CQ-017", want="falso", kw="autorizad",
         expected="desvio_agente",
         why="DIRIGIDO: fusión de conceptos (operador de cambio = entidad autorizada) → desvío del agente."),
    dict(label="on", run="run_3", qid="CQ-038", want="falso", kw="3.7",
         expected="falla_abstencion",
         why="DIRIGIDO: pregunta unanswerable; el agente no se abstuvo, afirmó un dato tangencial."),
    dict(label="off", run="run_3", qid="CQ-017", want="no_soportado", kw="ejecutan operaciones de cambio",
         expected="completitud_kg",
         why="DIRIGIDO: hedging por info inalcanzable; el KG no tiene la regla de autorización (Exterior 1.1)."),
    # --- 6 elegidos por diversidad ---
    dict(label="off", run="run_4", qid="CQ-033", want="falso", kw="17",
         why="run_4 / cadena / cita híbrida: el nodo dice '17% hasta 30/06/26' — testea nodo-vs-PDF en un calificador temporal."),
    dict(label="off", run="run_1", qid="CQ-019", want="falso", kw=None,
         why="run_1 / multi_norma / localización POR PÁGINA: el caso NIIF-9 que vi como agente-side; valida la página absoluta en otra pregunta."),
    dict(label="off", run="run_2", qid="CQ-018", want="falso", kw=None,
         why="run_2 (grafo aún no auditado) / multi_norma / localización por punto."),
    dict(label="off", run="run_5", qid="CQ-034", want="falso", kw="200",
         why="run_5 / cadena / límites USD: otro grafo + categoría; calificador de monto."),
    dict(label="off", run="run_3", qid="CQ-025", want="falso", kw=None,
         why="run_3 / factual / respuesta parcial: un falso SECUNDARIO (gradación parcial vs incorrecta)."),
    dict(label="off", run="run_2", qid="CQ-031", want="no_soportado", kw=None,
         why="run_2 / cadena / un NO_SOPORTADO para cubrir diversidad de verdict (no solo falsos)."),
]

# --------------------------------------------------------------------------- #
# Carga de traza + selección del claim                                        #
# --------------------------------------------------------------------------- #
def load_rep(label, run, qid):
    p = EVAL_DIR / "posthoc_run" / "traces" / label / run / f"{qid}.json"
    return json.load(open(p))[0]

def pick_claim(rep, want, kw):
    verifs = ((rep.get("judge") or {}).get("step2") or {}).get("verificaciones") or []
    cands = [v for v in verifs if v.get("verdict") == want]
    if kw:
        kwl = kw.lower()
        kwm = [v for v in cands if kwl in (v.get("enunciado") or "").lower()]
        if kwm: cands = kwm
    if not cands:  # fallback: cualquier falso, luego cualquier no_soportado
        cands = [v for v in verifs if v.get("verdict") in ("falso", "no_soportado")]
    cands.sort(key=lambda v: (0 if v.get("central") else 1))  # preferir central
    return cands[0] if cands else None

# --------------------------------------------------------------------------- #
# Recuperación de nodos vistos desde calls.db (filtrado por think)            #
# --------------------------------------------------------------------------- #
def recover_seen(run, label, pregunta):
    """Devuelve lista de candidatos {id, acceso, label, contenido, provenances} que el
    agente vio en esa pregunta. Filtra por gfp + think correcto."""
    think = 1 if label == "on" else 0
    kg = load_graph(run); gfp = lc.graph_fingerprint(kg)
    conn = lc._connect(PILOT_DB if False else (EVAL_DIR / "cache" / "calls.db"))
    rows = conn.execute("SELECT request_json FROM cache WHERE domain='agent' AND namespace LIKE ?",
                        (f"agent|gfp={gfp}|%think={think}",)).fetchall()
    cand = sorted([r["request_json"] for r in rows if pregunta[:40] in r["request_json"]],
                  key=len, reverse=True)
    conn.close()
    if not cand:
        return []
    msgs = json.loads(cand[0]).get("messages", [])
    # mapear tool_use (name+input) ←→ tool_result (content) por tool_use_id
    tool_use = {}     # id -> (name, input)
    results = {}      # id -> parsed result
    for m in msgs:
        c = m.get("content")
        if not isinstance(c, list): continue
        for b in c:
            if not isinstance(b, dict): continue
            if b.get("type") == "tool_use":
                tool_use[b.get("id")] = (b.get("name"), b.get("input"))
            elif b.get("type") == "tool_result":
                try: results[b.get("tool_use_id")] = json.loads(b.get("content") or "{}")
                except Exception: results[b.get("tool_use_id")] = {}
    items = {}  # dedupe por id; preferir ver_nodo sobre buscar_nodos
    def add(nid, acceso, label_, contenido, provs):
        if not nid: return
        prev = items.get(nid)
        rank = {"ver_nodo": 3, "edge": 2, "buscar_nodos": 1}
        if prev and rank.get(prev["acceso"], 0) >= rank.get(acceso, 0):
            return
        label_ = "" if label_ is None else str(label_)
        contenido = "" if contenido is None else (contenido if isinstance(contenido, str)
                                                  else json.dumps(contenido, ensure_ascii=False))
        items[nid] = {"id": nid, "acceso": acceso, "label": label_,
                      "contenido": contenido, "provenances": provs or []}
    for tid, (name, _inp) in tool_use.items():
        r = results.get(tid) or {}
        if name == "ver_nodo" and "properties" in r:
            props = r.get("properties") or {}
            desc = props.get("description") or props.get("descripcion") or \
                   "; ".join(f"{k}: {v}" for k, v in props.items())
            add(r.get("id"), "ver_nodo", r.get("label"), desc, r.get("provenances"))
        elif name == "buscar_nodos":
            for n in r.get("resultados") or []:
                add(n.get("id"), "buscar_nodos", n.get("label"),
                    n.get("resumen_propiedades"), None)
        elif name == "ver_vecinos":
            for d in ("salientes", "entrantes"):
                for e in r.get(d) or []:
                    eid = f"EDGE::{r.get('id')}--{e.get('relation')}-->{e.get('vecino_id')}"
                    add(eid, "edge", f"{r.get('label')} {e.get('relation')} {e.get('vecino_label')}",
                        f"{r.get('label')} —{e.get('relation')}→ {e.get('vecino_label')}",
                        e.get("provenances"))
    return list(items.values())

# --------------------------------------------------------------------------- #
# Pre-ranking léxico                                                          #
# --------------------------------------------------------------------------- #
def _norm(s):
    s = unicodedata.normalize("NFKD", (s or "").lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return set(re.findall(r"[a-z0-9]+", s))

def prerank(claim, cands, topn=8):
    q = _norm(claim)
    scored = []
    for c in cands:
        toks = _norm((c.get("label") or "") + " " + (c.get("contenido") or ""))
        scored.append((len(q & toks), c))
    scored.sort(key=lambda t: -t[0])
    return [c for _, c in scored[:topn]]

# --------------------------------------------------------------------------- #
# Localización del pasaje del PDF (por punto / por página)                    #
# Extraída a pdf_locate.py (refactor Fase 2.4). Se importa para preservar el  #
# comportamiento idéntico; verifier_pilot solo usa localize().                #
# --------------------------------------------------------------------------- #
from pdf_locate import localize  # noqa: E402  (localize + helpers viven en pdf_locate)

# --------------------------------------------------------------------------- #
# Helpers LLM                                                                 #
# --------------------------------------------------------------------------- #
def _extract_json(text):
    t = re.sub(r"^```(?:json)?\s*|\s*```$", "", (text or "").strip(), flags=re.I).strip()
    try: return json.loads(t)
    except Exception:
        m = re.search(r"\{.*\}", t, re.S)
        if m:
            try: return json.loads(m.group(0))
            except Exception: return None
        return None

def call_llm(client, model, system, user, max_tokens, temperature=None):
    kw = dict(model=model, max_tokens=max_tokens, system=system,
              messages=[{"role": "user", "content": user}])
    if temperature is not None:      # Opus 4.8 rechaza temperature → solo se pasa a Haiku/Sonnet
        kw["temperature"] = temperature
    resp = client.messages.create(**kw)
    text = "".join(b.text for b in resp.content if getattr(b, "type", "") == "text")
    return text

# --------------------------------------------------------------------------- #
# Mapeo claim → nodo (Haiku)                                                  #
# --------------------------------------------------------------------------- #
MAP_SYS = """Sos un asistente que mapea una AFIRMACIÓN del agente al/los NODO(S) del grafo de los que salió.
Te doy la afirmación y una lista de nodos que el agente efectivamente vio (con su contenido).
Devolvé SOLO un objeto JSON: {"nodo_ids": [...], "confianza": "alta|media|baja|ninguno", "razon": "<1 frase>"}.
Si la afirmación NO sale de ningún nodo de la lista (el agente la infirió o inventó), devolvé nodo_ids=[] y confianza="ninguno".
Si sintetiza varios nodos, incluí todos sus ids."""

def map_claim(client, claim, cands):
    top = prerank(claim, cands, topn=8)
    listing = "\n".join(
        f'- id="{c["id"]}" [{c["acceso"]}] label="{c.get("label")}" :: {(c.get("contenido") or "")[:240]}'
        for c in top)
    user = f'AFIRMACIÓN:\n"{claim}"\n\nNODOS QUE EL AGENTE VIO:\n{listing}'
    out = _extract_json(call_llm(client, MODEL_MAP, MAP_SYS, user, 600, temperature=0)) or {}
    ids = out.get("nodo_ids") or []
    by_id = {c["id"]: c for c in cands}
    nodos = [by_id[i] for i in ids if i in by_id]
    return nodos, out.get("confianza", "ninguno"), out.get("razon", ""), top

# --------------------------------------------------------------------------- #
# Verificación principal (Opus)                                               #
# --------------------------------------------------------------------------- #
VERIF_SYS = """Sos un VERIFICADOR DE CALIDAD DE UN KNOWLEDGE GRAPH regulatorio del BCRA. NO evaluás al agente:
el agente es el instrumento; el objeto de evaluación es el GRAFO. Por cada afirmación incorrecta del agente
determinás si el defecto está en el KG o en el agente, comparando el nodo del que salió contra el PDF fuente.

Te doy: la afirmación; su veredicto del juez (falso/no_soportado); la pregunta y su categoría; el/los nodo(s)
del grafo de los que salió (con su contenido) o "ninguno"; el pasaje del PDF en la ubicación citada; y, si existe,
la cita textual del ground truth.

Producí DOS capas. Razoná explícitamente conectando hecho→clasificación.

CAPA 1 (hechos):
- nodo_fiel_al_pdf: "si"|"no"|"parcial"|"na"  (¿el contenido del nodo representa fielmente lo que dice el PDF? "na" si no hay nodo)
- agente_fiel_al_nodo: "si"|"no"|"parcial"|"na"  (¿la afirmación dice lo que el nodo dice, sin agregar? "na" si no hay nodo)

CAPA 2 (causa) — seguí este árbol:
  ¿hay nodo fuente?
   NO  → unanswerable y el agente NO se abstuvo (afirmó algo, aunque sea tangencial) → "falla_abstencion" (lado agente)
       → el PDF SÍ tiene la info pedida pero ningún nodo la representa/alcanza → "completitud_kg" (lado kg)
       → el agente afirmó algo no respaldado por el PDF ni por un nodo → "desvio_agente" (lado agente)
   SÍ  → agente_fiel_al_nodo = no → "desvio_agente" (lado agente)
       → agente_fiel_al_nodo = si  y  nodo_fiel_al_pdf = no → "contenido_kg" (lado kg)
       → todo fiel pero el error vino de NO conectar dos nodos correctos (faltaría una arista) → "estructural_kg" (lado kg); marcá requiere_revision_humana=true, NO auto-decidas con certeza
       → todo correcto → "sin_defecto"
  Nota: en una pregunta unanswerable, afirmar un dato tangencial aunque esté en un nodo fiel sigue siendo "falla_abstencion".

Devolvé SOLO este JSON:
{"capa1":{"nodo_fiel_al_pdf":"...","agente_fiel_al_nodo":"..."},
 "capa2":{"clasificacion":"contenido_kg|completitud_kg|estructural_kg|desvio_agente|falla_abstencion|sin_defecto",
          "lado":"kg|agente|ninguno","razonamiento":"<cadena hecho→clasificación>",
          "confianza":"alta|media|baja","requiere_revision_humana":true|false}}"""

def verify(client, claim, verdict, pregunta, categoria, nodos, pdf_node, pdf_gt, guard_answerable=False):
    nodos_txt = "ninguno (el mapeo no encontró nodo fuente)" if not nodos else "\n".join(
        f'- id="{n["id"]}" [{n["acceso"]}] :: {(n.get("contenido") or "")}' for n in nodos)
    user = f"""AFIRMACIÓN DEL AGENTE: "{claim}"
VEREDICTO DEL JUEZ: {verdict}
PREGUNTA ({categoria}): {pregunta}

NODO(S) FUENTE:
{nodos_txt}

PASAJE DEL PDF en la ubicación del nodo ({pdf_node.get('ref') if pdf_node else 'n/a'}):
{(pdf_node or {}).get('pasaje') or '(no disponible)'}

CITA TEXTUAL DEL GROUND TRUTH (eval_set, si existe):
{pdf_gt or '(no hay — puede ser pregunta unanswerable)'}"""
    if guard_answerable:  # Ajuste 1: falla_abstencion SOLO aplica a preguntas unanswerable
        user += ("\n\nRESTRICCIÓN: esta pregunta NO es de categoría unanswerable, por lo que "
                 "'falla_abstencion' NO es una clasificación válida acá. Con nodo fuente presente, "
                 "clasificá por la rama normal del árbol (contenido_kg / desvio_agente / completitud_kg / "
                 "estructural_kg / sin_defecto) según los hechos, NO uses falla_abstencion.")
    return _extract_json(call_llm(client, MODEL_VERIF, VERIF_SYS, user, 1500)) or {}

# --------------------------------------------------------------------------- #
# Evaluador A (ciego)                                                         #
# --------------------------------------------------------------------------- #
EVALA_SYS = """Sos un usuario de servicios financieros que NO puede verificar la respuesta contra ninguna fuente.
Solo ves la pregunta y la respuesta final (con sus citas). Juzgás la calidad PERCIBIDA, no la corrección real.
Devolvé SOLO este JSON:
{"claridad":"alta|media|baja",
 "se_sostiene":"si|parcial|no",          // ¿es coherente internamente, sin contradicciones, con confianza calibrada al contenido?
 "abstencion_percibida":"apropiada|sobre_afirma|sub_afirma|na",  // ¿parece apropiadamente segura/cauta?
 "confianza_percibida_global":"alta|media|baja",
 "justificacion":"<2 frases>"}"""

def eval_a(client, pregunta, fj, incluir_trayectoria=False, steps=None):
    citas = "; ".join(f'{c.get("source_doc")} :: {c.get("location")}' for c in (fj.get("citas") or [])) or "(ninguna)"
    user = f"""PREGUNTA: {pregunta}

RESPUESTA DEL AGENTE:
{fj.get('respuesta')}

CITAS: {citas}
respondible declarado por el agente: {fj.get('respondible')}"""
    if incluir_trayectoria and steps:
        traj = "\n".join(f'  {s["n"]}. {s["tool"]}({json.dumps(s.get("input"),ensure_ascii=False)})' for s in steps)
        user += f"\n\nTRAYECTORIA (tool calls):\n{traj}"
    out = _extract_json(call_llm(client, MODEL_EVALA, EVALA_SYS, user, 600, temperature=0)) or {}
    out["vio_trayectoria"] = bool(incluir_trayectoria)
    return out

# --------------------------------------------------------------------------- #
# Orquestación                                                                #
# --------------------------------------------------------------------------- #
# Provenance imprecisa: ¿el pasaje en la ubicación que cita la provenance del nodo trata el
# MISMO tema que el contenido del nodo, o la provenance apunta al lugar equivocado?
# (Haiku — NO toca el prompt Opus ni la clasificación; agrega una dimensión de calidad del KG.)
PROV_SYS = """Te doy el CONTENIDO de un nodo del grafo y el PASAJE del PDF en la ubicación que cita su
provenance. Decidí si la provenance apunta al lugar correcto. Devolvé SOLO JSON:
{"mismo_tema": true|false, "provenance_imprecisa": true|false, "razon": "<1 frase>"}.
provenance_imprecisa=true SOLO si el pasaje trata un tema DISTINTO al contenido del nodo (la provenance
apunta al lugar equivocado, aunque el contenido del nodo pueda ser correcto en otra parte del documento).
Si tratan el MISMO tema, provenance_imprecisa=false aunque difieran en un valor (eso es contenido, no provenance)."""

def check_provenance(client, node_content, pdf_passage):
    user = f"CONTENIDO DEL NODO:\n{node_content}\n\nPASAJE DEL PDF EN LA UBICACIÓN QUE CITA SU PROVENANCE:\n{(pdf_passage or '')[:1200]}"
    out = _extract_json(call_llm(client, MODEL_MAP, PROV_SYS, user, 300, temperature=0)) or {}
    return bool(out.get("provenance_imprecisa")), out.get("razon", "")

_SEEN_CACHE = {}
def build_one(spec, client=None, preflight=False):
    rep = load_rep(spec["label"], spec["run"], spec["qid"])
    es = json.load(open(EVAL_SET)); es = es["preguntas"] if isinstance(es, dict) else es
    q = {x["id"]: x for x in es}[spec["qid"]]
    claim_v = spec.get("claim_override") or pick_claim(rep, spec.get("want"), spec.get("kw"))
    claim = (claim_v or {}).get("enunciado")
    ck = (spec["run"], spec["label"], spec["qid"])
    if ck not in _SEEN_CACHE:
        _SEEN_CACHE[ck] = recover_seen(spec["run"], spec["label"], q["pregunta"])
    cands = _SEEN_CACHE[ck]

    rec = {"meta": {k: spec.get(k) for k in ("label", "run", "qid", "expected", "why")},
           "categoria": rep.get("categoria"),
           "claim": {"enunciado": claim, "central": (claim_v or {}).get("central"),
                     "verdict_juez": (claim_v or {}).get("verdict")},
           "pregunta": q["pregunta"], "n_candidatos": len(cands)}

    if preflight or client is None:
        top = prerank(claim or "", cands, topn=5)
        rec["preflight_top_candidatos"] = [{"id": c["id"], "acceso": c["acceso"],
                                            "contenido": (c.get("contenido") or "")[:120]} for c in top]
        # localización tentativa del candidato top (si tiene provenance)
        prov = (top[0]["provenances"][0] if top and top[0].get("provenances") else None)
        if prov:
            loc = localize(prov.get("source_doc"), prov.get("location"))
            rec["preflight_pdf"] = {"prov": prov, "ref": loc.get("ref"),
                                    "pasaje_preview": (loc.get("pasaje") or "")[:160]}
        rec["cita_textual_gt"] = q.get("cita_textual")
        return rec

    # --- mapeo claim→nodo (Haiku) ---
    nodos, conf_map, razon_map, top = map_claim(client, claim, cands)
    # --- Arreglo 2: anclar el pasaje del PDF al primer nodo CON provenance (no al nodos[0]) ---
    anchor = next((n for n in nodos if n.get("provenances")), None)
    nodo_sin_prov = bool(nodos) and anchor is None
    pdf_node = None
    if anchor:
        prov = anchor["provenances"][0]
        pdf_node = localize(prov.get("source_doc"), prov.get("location"))
        pdf_node["prov"] = prov
        pdf_node["nodo_anclado"] = anchor["id"]
    pdf_gt = q.get("cita_textual")
    # --- verificación principal (Opus) ---
    res = verify(client, claim, rec["claim"]["verdict_juez"], q["pregunta"], rep.get("categoria"),
                 nodos, pdf_node, pdf_gt)
    c2 = res.get("capa2") or {}
    # --- Ajuste 1: guard de falla_abstencion (solo unanswerable). Re-pregunta SOLO este claim. ---
    guard_aplicado = False
    if rep.get("categoria") != "unanswerable" and c2.get("clasificacion") == "falla_abstencion":
        res = verify(client, claim, rec["claim"]["verdict_juez"], q["pregunta"], rep.get("categoria"),
                     nodos, pdf_node, pdf_gt, guard_answerable=True)
        c2 = res.get("capa2") or {}
        guard_aplicado = True

    rec["guard_falla_abstencion_aplicado"] = guard_aplicado
    # --- dimensión provenance_imprecisa (Haiku; solo donde puede haber problema de provenance) ---
    nfp = (res.get("capa1") or {}).get("nodo_fiel_al_pdf")
    prov_imprecisa, prov_razon = (None, None)
    if anchor and (pdf_node or {}).get("localizacion_pdf") == "ok" and nfp in ("no", "parcial"):
        prov_imprecisa, prov_razon = check_provenance(client, anchor.get("contenido"), (pdf_node or {}).get("pasaje"))
    rec["capa1_hechos"] = {
        "afirmacion_agente": claim,
        "nodo_fuente": [{"id": n["id"], "acceso": n["acceso"], "contenido": n.get("contenido"),
                         "provenances": n.get("provenances")} for n in nodos],
        "mapeo_confianza": conf_map, "mapeo_razon": razon_map,
        "nodo_sin_provenance": nodo_sin_prov,
        "pdf_pasaje_nodo": pdf_node, "localizacion_pdf": (pdf_node or {}).get("localizacion_pdf"),
        "cita_textual_gt": pdf_gt,
        "nodo_fiel_al_pdf": nfp,
        "agente_fiel_al_nodo": (res.get("capa1") or {}).get("agente_fiel_al_nodo"),
        "provenance_imprecisa": prov_imprecisa, "provenance_razon": prov_razon,
    }
    rec["capa2_causa"] = c2
    # --- Arreglo 3: discrepancia verificador↔juez (posible falso-positivo del juez) ---
    rec["discrepa_del_juez"] = (c2.get("clasificacion") == "sin_defecto"
                                and rec["claim"]["verdict_juez"] in ("falso", "no_soportado"))
    # cola de adjudicación: + confianza media + discrepa_del_juez
    #   + Ajuste 2: clasificó SIN poder anclar pasaje del PDF (menos confiable) → siempre a la cola.
    loc = (pdf_node or {}).get("localizacion_pdf")
    sin_anclaje_pdf = nodo_sin_prov or (pdf_node is None) or (loc in (None, "fallida"))
    rec["sin_anclaje_pdf"] = sin_anclaje_pdf
    rec["adjudicacion"] = (conf_map in ("baja", "ninguno")
                           or c2.get("clasificacion") == "estructural_kg"
                           or c2.get("confianza") in ("baja", "media")
                           or bool(c2.get("requiere_revision_humana"))
                           or rec["discrepa_del_juez"]
                           or sin_anclaje_pdf)
    return rec

# --------------------------------------------------------------------------- #
# Escalado: enumeración + agregación Nivel 2 (mapa por nodo-defecto)          #
# --------------------------------------------------------------------------- #
import glob as _glob

def scale_specs():
    """Todos los claims falso/no_soportado de las trazas post-hoc (OFF+ON, 5 grafos)."""
    specs = []
    for f in sorted(_glob.glob(str(EVAL_DIR / "posthoc_run" / "traces" / "*" / "*" / "*.json"))):
        parts = f.split("/"); label = parts[-3]; run = parts[-2]; qid = parts[-1][:-5]
        for rep in json.load(open(f)):
            for v in ((rep.get("judge") or {}).get("step2") or {}).get("verificaciones") or []:
                if v.get("verdict") in ("falso", "no_soportado"):
                    specs.append({"label": label, "run": run, "qid": qid,
                                  "claim_override": {"enunciado": v.get("enunciado"),
                                                     "central": v.get("central"),
                                                     "verdict": v.get("verdict")}})
    return specs

def _src_doc(rec):
    nf = rec["capa1_hechos"].get("nodo_fuente") or []
    for n in nf:
        for p in (n.get("provenances") or []):
            if p.get("source_doc"): return p["source_doc"]
    return None

def aggregate_map(records):
    """Nivel 2: colapsa claims por el NODO del KG que los originó. Un nodo malo en N claims
    = 1 defecto con impacto N. completitud_kg no tiene nodo → se agrega como 'gap' por (run,qid)."""
    from collections import defaultdict
    node_def = defaultdict(lambda: {"claims": set(), "grafos": set(), "tos": set()})
    gaps = defaultdict(lambda: {"claims": set(), "tos": set()})
    for r in records:
        c1 = r["capa1_hechos"]; c2 = r["capa2_causa"]; clasif = c2.get("clasificacion")
        run = r["meta"]["run"]; enun = r["claim"]["enunciado"]; src = _src_doc(r)
        nid = (c1.get("pdf_pasaje_nodo") or {}).get("nodo_anclado")
        if not nid:
            nf = c1.get("nodo_fuente") or []
            nid = nf[0]["id"] if nf else None
        dims = []
        if clasif in ("contenido_kg", "estructural_kg"):
            dims.append(clasif)
        if c1.get("provenance_imprecisa") is True:
            dims.append("provenance_imprecisa")
        for d in dims:
            if nid:
                e = node_def[(d, nid)]
                e["claims"].add(enun); e["grafos"].add(run)
                if src: e["tos"].add(src)
        if clasif == "completitud_kg":
            g = gaps[(run, r["meta"]["qid"])]
            g["claims"].add(enun)
            if src: g["tos"].add(src)
    defectos = [{"dimension": d, "node_id": nid, "impacto": len(e["claims"]),
                 "grafos": sorted(e["grafos"]), "tos": sorted(e["tos"]),
                 "ejemplos": sorted(e["claims"])[:2]}
                for (d, nid), e in node_def.items()]
    defectos.sort(key=lambda x: -x["impacto"])
    gaps_l = [{"run": run, "qid": qid, "n_claims": len(g["claims"]), "tos": sorted(g["tos"])}
              for (run, qid), g in gaps.items()]
    gaps_l.sort(key=lambda x: -x["n_claims"])
    return defectos, gaps_l

def adjudication_breakdown(records):
    from collections import Counter
    causes = Counter(); total = 0
    for r in records:
        if not r.get("adjudicacion"): continue
        total += 1
        c2 = r["capa2_causa"]
        if c2.get("confianza") == "media": causes["confianza_media"] += 1
        if c2.get("confianza") == "baja": causes["confianza_baja"] += 1
        if r["capa1_hechos"].get("mapeo_confianza") in ("baja", "ninguno"): causes["mapeo_baja_ninguno"] += 1
        if r.get("sin_anclaje_pdf"): causes["sin_anclaje_pdf"] += 1
        if r.get("discrepa_del_juez"): causes["discrepa_del_juez"] += 1
        if c2.get("clasificacion") == "estructural_kg": causes["estructural_kg"] += 1
        if c2.get("requiere_revision_humana"): causes["requiere_revision_humana"] += 1
    return total, dict(causes)

def run_scale(client):
    specs = scale_specs()
    print(f"== ESCALADO: {len(specs)} claims falso/no_soportado ==", flush=True)
    records = []
    for i, spec in enumerate(specs, 1):
        try:
            records.append(build_one(spec, client=client))
        except Exception as e:  # robustez: un claim que falle no tumba la corrida
            records.append({"meta": {k: spec.get(k) for k in ("label", "run", "qid")},
                            "claim": spec.get("claim_override"), "error": f"{type(e).__name__}: {e}"})
        if i % 25 == 0:
            print(f"  {i}/{len(specs)} …", flush=True)
    json.dump(records, open(OUT_DIR / "verificador_scale_full.json", "w"), ensure_ascii=False, indent=2)
    ok = [r for r in records if "error" not in r]
    defectos, gaps = aggregate_map(ok)
    adj_total, adj_causes = adjudication_breakdown(ok)
    from collections import Counter
    by_clasif = Counter(r["capa2_causa"].get("clasificacion") for r in ok)
    by_lado = Counter(r["capa2_causa"].get("lado") for r in ok)
    n_prov = sum(1 for r in ok if r["capa1_hechos"].get("provenance_imprecisa") is True)
    resumen = {"n_claims": len(records), "n_ok": len(ok), "n_error": len(records) - len(ok),
               "por_clasificacion": dict(by_clasif), "por_lado": dict(by_lado),
               "provenance_imprecisa_flags": n_prov,
               "defectos_por_nodo": defectos, "gaps_completitud": gaps,
               "adjudicacion_total": adj_total, "adjudicacion_por_causa": adj_causes}
    json.dump(resumen, open(OUT_DIR / "mapa_agregado.json", "w"), ensure_ascii=False, indent=2)
    print("\n=== RESUMEN ESCALADO ===")
    print("clasificación:", dict(by_clasif))
    print("lado:", dict(by_lado))
    print(f"defectos por nodo (únicos): {len(defectos)} | gaps completitud: {len(gaps)} | prov_imprecisa flags: {n_prov}")
    print(f"adjudicación: {adj_total}/{len(ok)} ({100*adj_total/max(1,len(ok)):.0f}%) | por causa: {adj_causes}")
    print(f"\nArchivos: {OUT_DIR}/verificador_scale_full.json , mapa_agregado.json")
    return 0

def main():
    if "--scale" in sys.argv:
        from dotenv import load_dotenv
        import os, anthropic
        load_dotenv(EVAL_DIR / ".env")
        if not os.environ.get("ANTHROPIC_API_KEY", "").strip():
            raise SystemExit("ANTHROPIC_API_KEY no seteada en evaluacion/.env")
        OUT_DIR.mkdir(parents=True, exist_ok=True)
        real = anthropic.Anthropic(max_retries=3)
        client = lc.CachingClient(real, domain="verifier_pilot", db_path=PILOT_DB,
                                  namespace=lc.make_namespace("verifier_pilot", code_ver="pilot-v1"),
                                  run_label="scale")
        return run_scale(client)
    preflight = "--preflight" in sys.argv
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    client = None
    if not preflight:
        from dotenv import load_dotenv
        import os, anthropic
        load_dotenv(EVAL_DIR / ".env")
        if not os.environ.get("ANTHROPIC_API_KEY", "").strip():
            raise SystemExit("ANTHROPIC_API_KEY no seteada en evaluacion/.env")
        real = anthropic.Anthropic(max_retries=3)
        client = lc.CachingClient(real, domain="verifier_pilot", db_path=PILOT_DB,
                                  namespace=lc.make_namespace("verifier_pilot", code_ver="pilot-v1"),
                                  run_label="pilot")
    verif_out, evala_out = [], []
    for i, spec in enumerate(PILOT, 1):
        print(f"[{i}/10] {spec['label']}/{spec['run']}/{spec['qid']} …", flush=True)
        rec = build_one(spec, client=client, preflight=preflight)
        verif_out.append(rec)
        if not preflight:
            rep = load_rep(spec["label"], spec["run"], spec["qid"])
            es = json.load(open(EVAL_SET)); es = es["preguntas"] if isinstance(es, dict) else es
            q = {x["id"]: x for x in es}[spec["qid"]]
            a = eval_a(client, q["pregunta"], (rep.get("trace") or {}).get("final_json") or {})
            a = {"qid": spec["qid"], "run": spec["run"], "label": spec["label"], **a}
            evala_out.append(a)

    tag = "preflight" if preflight else "full"
    json.dump(verif_out, open(OUT_DIR / f"verificador_{tag}.json", "w"), ensure_ascii=False, indent=2)
    if not preflight:
        json.dump(evala_out, open(OUT_DIR / "evaluador_a.json", "w"), ensure_ascii=False, indent=2)
    print(f"\nEscrito en {OUT_DIR}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
