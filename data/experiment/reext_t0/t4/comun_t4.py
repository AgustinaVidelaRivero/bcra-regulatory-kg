"""U-REEXT-T0, T4: lectura común de las fichas (solo lee; USD 0). Para una unidad de la corrida r2b de los diez TOs:
el texto de E0 r2b (propio y heredado; las partes de una unidad partida por corte, de particiones_por_corte.json), la
extracción validada que entra al grafo (extracciones_finales_r2_<to>.jsonl, última versión por unidad: entidades con
su tramo, relaciones con sus extremos y menciones, omisiones y rechazos), el estado final (finales.jsonl) y, si la
unidad está en la cola humana, los faltantes que E3 dejó pendientes (cola_humana.jsonl)."""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[4]
REX = RAIZ / "data" / "experiment" / "reextraccion_v2"
SALIDA = REX / "corpus_tanda0" / "salida_r2b"
E0 = REX / "e0_chunking" / "salida_tanda0_r2b"
TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")


def _ultima(path: Path) -> dict:
    out = {}
    if path.exists():
        for x in path.read_text(encoding="utf-8").splitlines():
            if x.strip():
                r = json.loads(x)
                out[r["chunk_id"]] = r
    return out


@lru_cache(maxsize=None)
def chunks(to: str) -> dict:
    d = json.loads((E0 / f"chunks_{to}.json").read_text(encoding="utf-8"))
    out = {c["id"]: c for c in (d["chunks"] if isinstance(d, dict) else d)}
    p = SALIDA / to / "particiones_por_corte.json"
    if p.exists():
        for cid, v in json.loads(p.read_text(encoding="utf-8")).items():
            for parte in v["partes"]:
                base = dict(out[cid])
                base.update({k: parte[k] for k in parte if k != "id"}, id=parte["id"])
                out[parte["id"]] = base
    return out


@lru_cache(maxsize=None)
def extracciones(to: str) -> dict:
    return _ultima(SALIDA / to / f"extracciones_finales_r2_{to}.jsonl")


@lru_cache(maxsize=None)
def extracciones_e1(to: str) -> dict:
    """La respuesta de E1 de la corrida, validada (extracciones_e1.jsonl, última versión por unidad)."""
    return _ultima(SALIDA / to / "extracciones_e1.jsonl")


@lru_cache(maxsize=None)
def finales(to: str) -> dict:
    return _ultima(SALIDA / to / "finales.jsonl")


@lru_cache(maxsize=None)
def cola(to: str) -> dict:
    return _ultima(SALIDA / to / "cola_humana.jsonl")


@lru_cache(maxsize=None)
def resolucion() -> dict:
    """(chunk_id, índice de la relación) → id resuelto en el ensamblado sellado de diez (resolucion_sujetos.jsonl; si la
    mención quedó en cuarentena, el id del propuesto de no_mapeados_sujetos.jsonl)."""
    d = REX / "corpus_tanda0" / "ens_diez_r2b" / "r2"
    out = {}
    for nombre, campo in (("no_mapeados_sujetos.jsonl", "id_nodo"), ("resolucion_sujetos.jsonl", "resuelto_a")):
        for x in (d / nombre).read_text(encoding="utf-8").splitlines():
            if x.strip():
                f = json.loads(x)
                if f.get(campo):
                    out.setdefault((f["chunk_id"], f.get("indice_relacion")), f[campo])
    return out


def texto(cid: str) -> dict:
    to = cid.split("::")[0]
    c = chunks(to)[cid]
    her = [h.get("texto") for h in c.get("herencia") or [] if h.get("texto")]
    return {"propio": c.get("texto") or "", "heredado": her, "titulo": c.get("titulo")}


def respuesta_e1(cid: str) -> dict:
    """La respuesta cruda de E1 de la corrida (tool_input_crudo), en la forma de lectura de `extraccion`: lo que P5
    comparó (p5/analisis_p5.py, comparar). Las omisiones meta_normativo llevan las clases del contador del validador
    (validador_r2.marcas_meta_normativo), como ayuda."""
    import sys  # noqa: PLC0415
    sys.path.insert(0, str(RAIZ / "data" / "experiment" / "pyd_r2" / "code"))
    import validador_r2 as V  # noqa: PLC0415
    to = cid.split("::")[0]
    r = extracciones_e1(to).get(cid) or {}
    ti = r.get("tool_input_crudo") or {}
    ents = [e for e in ti.get("entities") or [] if isinstance(e, dict)]
    por_id = {e.get("local_id"): e for e in ents}

    def nombre(x):
        e = por_id.get(x)
        return f"{x} {e.get('type')} «{e.get('label')}»" if e else str(x)
    rels = []
    for rel in ti.get("relations") or []:
        if not isinstance(rel, dict):
            continue
        if rel.get("sujeto_mencion") is not None or rel.get("sujeto_id") is not None:
            destino = f"{rel.get('sujeto_id') or rel.get('target')} (mención «{rel.get('sujeto_mencion')}»)"
        else:
            destino = nombre(rel.get("target"))
        rels.append({"source": nombre(rel.get("source")), "predicate": rel.get("predicate"), "target": destino,
                     "coherencia": None})
    oms = []
    for o in ti.get("omisiones") or []:
        if isinstance(o, dict):
            m = V.marcas_meta_normativo(o["tramo"]) if o.get("categoria") == "meta_normativo" and isinstance(o.get("tramo"), str) else []
            oms.append({"categoria": o.get("categoria"), "tramo": o.get("tramo"), "nota": o.get("nota"), "marcas": m})
    return {"estado_final": (finales(to).get(cid) or {}).get("estado"), "error": r.get("error"),
            "entidades": [{"local_id": e.get("local_id"), "type": e.get("type"), "label": e.get("label"),
                           "descripcion": (e.get("properties") or {}).get("descripcion"),
                           "properties": {k: x for k, x in (e.get("properties") or {}).items() if k != "descripcion"}
                           | ({"umbrales": e["umbrales"]} if e.get("umbrales") else {}),
                           "tramo": e.get("tramo"), "tramo_verificado": None} for e in ents],
            "relaciones": rels, "omisiones": oms, "rechazos": len((r.get("validacion") or {}).get("rechazos") or []),
            "faltantes_e3": None}


def extraccion(cid: str, fuente: str = "final") -> dict:
    if fuente == "e1":
        return respuesta_e1(cid)
    """fuente «final»: la extracción que entra al grafo (después de E3); «e1»: la respuesta de E1 validada."""
    to = cid.split("::")[0]
    r = (extracciones_e1(to) if fuente == "e1" else extracciones(to)).get(cid) or {}
    v = r.get("validacion") or {}
    ents = v.get("entidades") or []
    por_id = {e.get("local_id"): e for e in ents}

    def nombre(x):
        e = por_id.get(x)
        return f"{x} {e['type']} «{e['label']}»" if e else str(x)
    rels = []
    for rel in v.get("relaciones") or []:
        destino = rel.get("target")
        if rel.get("sujeto_id_modelo") is not None or rel.get("sujeto_mencion") is not None:
            destino = (f"{resolucion().get((cid, rel.get('indice_crudo')))} (mención «{rel.get('sujeto_mencion')}», "
                       f"{rel.get('mencion_verificada')})")
        else:
            destino = nombre(destino)
        rels.append({"source": nombre(rel.get("source")), "predicate": rel.get("predicate"), "target": destino,
                     "coherencia": rel.get("coherencia_tipo_predicado")})
    return {"estado_final": (finales(to).get(cid) or {}).get("estado"), "error": r.get("error"),
            "entidades": [{"local_id": e.get("local_id"), "type": e["type"], "label": e["label"],
                           "descripcion": (e.get("properties") or {}).get("descripcion"),
                           "properties": {k: x for k, x in (e.get("properties") or {}).items() if k != "descripcion"},
                           # los tramos de umbral que dio el modelo (el ensamblado los completa con valor y unidad)
                           "umbrales_tramos": e.get("umbrales_tramos") or [],
                           "tramo": (e.get("provenance") or {}).get("tramo"),
                           "tramo_verificado": (e.get("provenance") or {}).get("tramo_verificado")} for e in ents],
            "relaciones": rels,
            "omisiones": [{"categoria": o.get("categoria"), "tramo": o.get("tramo"), "nota": o.get("nota")}
                          for o in v.get("omisiones") or []],
            "rechazos": len(v.get("rechazos") or []),
            "faltantes_e3": (cola(to).get(cid) or {}).get("faltantes_pendientes")}
