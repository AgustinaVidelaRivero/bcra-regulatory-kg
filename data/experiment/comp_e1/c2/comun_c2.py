"""
comun_c2.py — U-COMP-E1, C2 (lectura cegada): bases de T4, salidas de C1, intento 0 de Haiku, texto de las unidades,
renderizado de una extracción y candidatos automáticos para la lectura. USD 0, sin API.

Bases (las mismas fichas de T4; mandato, MEDICIONES y LECTURA; reglas selladas en c0/reglas_lectura_c0.md):
  - M1: los 137 supuestos de la fase A de las 30 unidades del grupo c, con su fragmento literal, tal como los enumeró
    T4 (reext_t0/t4/salida/tasas_t4.json, punto_7.por_supuesto.supuestos; decisión 6 de la autora);
  - M2: las 60 omisiones leídas en T4 (fichas_punto8_omisiones.json) con el «normativo» adjudicado por la autora
    (adjudicacion_autora.json: con_marca 14 y 26 pasan a normativas; sin_marca 9, 13, 23, 28 y 29 son remisiones
    puras, normativas en la cifra con remisiones): 46 normativas y 14 no normativas.
Salidas que se leen: resultados_<S1|S2|O1|O2>.jsonl de C1 (tool_input_crudo y validacion_r2, con el tramo de cada
entidad y omisión verificado por código) y, para las 8 unidades con reintento, el intento 0 de Haiku
(c0/salida/intento0_haiku.jsonl), validado aquí con validador_r2.validar (forma r2) para tener los mismos niveles.
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

AQUI = Path(__file__).resolve().parent            # comp_e1/c2
COMP_E1 = AQUI.parent
REPO = AQUI.parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
for p in (REX / "e1_extractor", REPO / "data" / "experiment" / "pyd_r2" / "code", REPO / "data" / "experiment" / "evaluacion"):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))

ETIQUETAS = ("S1", "S2", "O1", "O2")
ETIQUETA_HAIKU = "H0"          # el intento 0 de Haiku, solo en las 8 unidades con reintento
C1_SALIDA = COMP_E1 / "c1" / "salida"
INTENTO0 = COMP_E1 / "c0" / "salida" / "intento0_haiku.jsonl"
UNIDADES_JSON = COMP_E1 / "unidades.json"
T4 = REPO / "data" / "experiment" / "reext_t0" / "t4"
E0 = REX / "e0_chunking" / "salida_tanda0_r2b"
SALIDA_R2B = REX / "corpus_tanda0" / "salida_r2b"
CLASES_M1 = ("condicion_con_relacion", "dentro_de_norma", "fusionado", "omitido", "sin_relacion")
SUBTIPOS_SR = ("norma_en_heredado", "norma_presente", "norma_no_emitida")
CLASES_M2 = ("extraida_tramo_verificado", "extraida_tramo_no_verificable", "omision_otra_vez", "ausente")
# Adjudicación de la autora sobre el punto 8 (adjudicacion_autora.json): las que cambian de «no normativa» a normativa.
ADJ_NORMATIVAS = {("con_marca", 14), ("con_marca", 26)}
ADJ_REMISION_PURA = {("sin_marca", 9), ("sin_marca", 13), ("sin_marca", 23), ("sin_marca", 28), ("sin_marca", 29)}


def jsonl_last_wins(p: Path, clave: str = "chunk_id") -> dict:
    out: dict = {}
    for x in Path(p).read_text(encoding="utf-8").splitlines():
        if x.strip():
            r = json.loads(x)
            out[r[clave]] = r
    return out


def unidades() -> list[dict]:
    return json.loads(UNIDADES_JSON.read_text(encoding="utf-8"))["unidades"]


def resultados_c1() -> dict[str, dict]:
    return {et: jsonl_last_wins(C1_SALIDA / f"resultados_{et}.jsonl") for et in ETIQUETAS}


def intento0_haiku() -> dict:
    return jsonl_last_wins(INTENTO0)


def supuestos_t4() -> dict[str, list[dict]]:
    """chunk_id → lista de supuestos de la fase A (fragmento literal, miembros, clase de Haiku en T4, dónde)."""
    t = json.loads((T4 / "salida" / "tasas_t4.json").read_text(encoding="utf-8"))
    out: dict[str, list[dict]] = {}
    for s in t["punto_7"]["por_supuesto"]["supuestos"]:
        out.setdefault(s["chunk_id"], []).append(s)
    assert sum(len(v) for v in out.values()) == 137 and len(out) == 30, "los 137 supuestos de las 30 unidades"
    return out


def omisiones_t4() -> list[dict]:
    """Las 60 fichas del punto 8 con el «normativo» adjudicado y la marca de remisión pura."""
    f = json.loads((T4 / "salida" / "fichas_punto8_omisiones.json").read_text(encoding="utf-8"))["fichas"]
    out = []
    for x in f:
        k = (x["grupo"], x["n"])
        y = dict(x)
        y["normativo_adjudicado"] = bool(x["normativo"]) or k in ADJ_NORMATIVAS
        y["remision_pura"] = k in ADJ_REMISION_PURA
        out.append(y)
    assert len(out) == 60 and sum(o["normativo_adjudicado"] for o in out) == 46, "60 omisiones, 46 normativas adjudicadas"
    return out


def chunks_de(to: str) -> dict:
    d = json.loads((E0 / f"chunks_{to}.json").read_text(encoding="utf-8"))
    out = {c["id"]: c for c in (d["chunks"] if isinstance(d, dict) else d)}
    p = SALIDA_R2B / to / "particiones_por_corte.json"
    if p.exists():
        for cid, v in json.loads(p.read_text(encoding="utf-8")).items():
            for parte in v["partes"]:
                base = dict(out[cid])
                base.update({k: parte[k] for k in parte if k != "id"}, id=parte["id"])
                out[parte["id"]] = base
    return out


def chunks(unids: list[dict]) -> dict:
    out: dict = {}
    for to in sorted({u["to"] for u in unids}):
        out.update(chunks_de(to))
    return out


def texto(c: dict) -> dict:
    return {"propio": c.get("texto") or "", "heredado": [h.get("texto") for h in c.get("herencia") or [] if h.get("texto")],
            "titulo": c.get("titulo")}


# ------------------------------------------------------------------------------------------------ normalización
def norm(s) -> str:
    """Espacios simples, comillas rectas y sin el corte de palabra con guion de la E0 (como fichas_t4.norm)."""
    s = re.sub(r"\s+", " ", (s or "").replace("“", '"').replace("”", '"'))
    return re.sub(r"(\w)- (\w)", r"\1\2", s).strip()


def plano(s) -> str:
    s = unicodedata.normalize("NFKD", norm(s)).lower()
    s = "".join(ch for ch in s if not unicodedata.combining(ch))
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


_STOP = set("de del la el los las y o u a en que se con por para al lo su sus un una unos unas no si es son ser como mas "
            "este esta estos estas ese esa aquel segun sobre entre hasta desde sin ante tras cuando donde cual cuales "
            "i ii iii iv v vi vii viii ix x b c d e f g h".split())


def tokens(s) -> set[str]:
    return {t for t in plano(s).split() if t not in _STOP and (len(t) >= 3 or t.isdigit())}


def solap(a: set[str], b: set[str]) -> float:
    return (len(a & b) / len(a)) if a else 0.0


# ------------------------------------------------------------------------------------------------ extracción
def validacion_r2_de(reg: dict, chunk: dict) -> dict:
    """La validación r2 del registro (C1 la trae; el intento 0 de Haiku se valida aquí con el mismo validador)."""
    if reg.get("validacion_r2"):
        return reg["validacion_r2"]
    import validador_r2 as V  # noqa: PLC0415
    return V.validar(reg["tool_input_crudo"], chunk, forma="r2")


def entidades_de(val: dict) -> list[dict]:
    out = []
    for e in val.get("entidades") or []:
        pv = e.get("provenance") or {}
        props = {k: v for k, v in (e.get("properties") or {}).items() if k != "descripcion" and v not in (None, "", [], {})}
        out.append({"local_id": e.get("local_id"), "type": e.get("type"), "label": e.get("label"),
                    "descripcion": (e.get("properties") or {}).get("descripcion"), "properties": props,
                    "umbrales": [u.get("tramo") if isinstance(u, dict) else u for u in (e.get("umbrales_tramos") or [])],
                    "tramo": pv.get("tramo"), "tramo_verificado": pv.get("tramo_verificado"),
                    "no_definidas": e.get("properties_no_definidas") or {}})
    return out


def relaciones_de(val: dict) -> list[dict]:
    tipos = {e.get("local_id"): e.get("type") for e in val.get("entidades") or []}
    out = []
    for r in val.get("relaciones") or []:
        out.append({"source": r.get("source"), "tipo_source": r.get("tipo_source") or tipos.get(r.get("source")),
                    "predicate": r.get("predicate"), "target": r.get("target"),
                    "tipo_target": r.get("tipo_target") or tipos.get(r.get("target")),
                    "sujeto_mencion": r.get("sujeto_mencion"), "sujeto_id": r.get("sujeto_id_modelo") or r.get("sujeto_id")})
    return out


def omisiones_de(val: dict) -> list[dict]:
    return [{"categoria": o.get("categoria"), "tramo": o.get("tramo"), "nota": o.get("nota"),
             "tramo_verificado": o.get("tramo_verificado")} for o in val.get("omisiones") or []]


def rechazos_de(val: dict) -> list[str]:
    return [f"{r.get('nivel')}:{r.get('motivo')}" for r in val.get("rechazos") or []]


def corto(s, n=320) -> str:
    s = norm(s)
    return s if len(s) <= n else s[:n] + "…"


def render_extraccion(val: dict) -> list[str]:
    """Líneas Markdown de una extracción (como fichas_t4.bloque_extraccion): entidades con props, umbrales, tramo y
    nivel; relaciones con tipos y mención; omisiones con categoría y nivel; rechazos."""
    out = []
    rech = rechazos_de(val)
    if rech:
        out.append(f"- Rechazos del validador r2: {', '.join(rech)}")
    for e in entidades_de(val):
        if e["type"] == "TextoOrdenado":
            continue
        props = f" · props: `{json.dumps(e['properties'], ensure_ascii=False)}`" if e["properties"] else ""
        nd = f" · no definidas: `{json.dumps(e['no_definidas'], ensure_ascii=False)[:200]}`" if e["no_definidas"] else ""
        umb = f" · umbral: {[corto(u, 80) for u in e['umbrales']]}" if e["umbrales"] else ""
        out.append(f"- **{e['local_id']} {e['type']}** «{norm(e['label'])}» — {corto(e['descripcion'] or '', 400)}{props}{nd}{umb}"
                   f" · tramo [{e['tramo_verificado']}]: «{corto(e['tramo'])}»")
    for r in relaciones_de(val):
        if r["predicate"] == "establecida_en":
            continue
        suj = f"{r['sujeto_id'] or 'Sujeto'} (mención «{norm(r['sujeto_mencion'])}»)" if (r["sujeto_mencion"] or r["sujeto_id"]) else None
        if suj and r["source"] is None:
            # relación de sujeto con el sujeto como fuente (ejecuta): Sujeto → entidad destino
            out.append(f"- R: {suj} —{r['predicate']}→ {r['target']} {r['tipo_target'] or ''}".rstrip())
        else:
            dest = suj if suj else f"{r['target']} {r['tipo_target'] or ''}".strip()
            out.append(f"- R: {r['source']} {r['tipo_source'] or ''} —{r['predicate']}→ {dest}")
    for o in omisiones_de(val):
        out.append(f"- Omisión `{o['categoria']}` [{o['tramo_verificado']}]: «{corto(o['tramo'])}» — {corto(o['nota'] or '', 200)}")
    return out


# ------------------------------------------------------------------------------------------------ candidatos
def candidatos_supuesto(frag: str, val: dict, k: int = 4) -> list[str]:
    """Entidades cuyo label, descripción, tramo o umbrales comparten más términos con el fragmento del supuesto
    (ayuda para ubicarlo; la clase la decide la lectura)."""
    ft = tokens(frag)
    filas = []
    for e in entidades_de(val):
        if e["type"] == "TextoOrdenado":
            continue
        et = tokens(" ".join([e["label"] or "", e["descripcion"] or "", e["tramo"] or ""] + [u or "" for u in e["umbrales"]]))
        s = solap(ft, et)
        if s > 0:
            filas.append((s, e["local_id"], e["type"]))
    filas.sort(key=lambda x: (-x[0], x[1]))
    return [f"{lid} {t} ({s:.2f})" for s, lid, t in filas[:k]]


def candidatos_omision(tramo_t4: str, val: dict) -> dict:
    """Entidades cuyo tramo verificado cubre el tramo de la omisión de T4 (solapamiento de términos del tramo de T4 y
    contención del texto normalizado), y omisiones de la salida que lo cubren."""
    tt = tokens(tramo_t4)
    pl = plano(tramo_t4)
    ents, oms = [], []
    for e in entidades_de(val):
        if e["type"] == "TextoOrdenado" or not e["tramo"]:
            continue
        pe = plano(e["tramo"])
        s = solap(tt, tokens(e["tramo"]))
        cont = pl in pe or (pe in pl and len(pe) > 20)
        if s >= 0.3 or cont:
            ents.append({"local_id": e["local_id"], "type": e["type"], "label": e["label"], "tramo_verificado": e["tramo_verificado"],
                         "solapamiento": round(s, 2), "contiene": pl in pe, "contenido_en": (pe in pl and len(pe) > 20)})
    for i, o in enumerate(omisiones_de(val)):
        po = plano(o["tramo"] or "")
        s = solap(tt, tokens(o["tramo"]))
        cont = (pl in po) or (po in pl and len(po) > 20)
        if s >= 0.3 or cont:
            oms.append({"indice": i, "categoria": o["categoria"], "tramo_verificado": o["tramo_verificado"], "solapamiento": round(s, 2),
                        "contiene": pl in po, "contenido_en": (po in pl and len(po) > 20), "tramo": corto(o["tramo"], 200)})
    ents.sort(key=lambda x: -x["solapamiento"]); oms.sort(key=lambda x: -x["solapamiento"])
    return {"entidades": ents, "omisiones": oms}
