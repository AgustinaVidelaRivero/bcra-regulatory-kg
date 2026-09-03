"""
chequeo_esq3b_v2.py — Chequeo de conformidad de una extracción contra el
esquema V2 de U-ESQ-3b-v2.

Patrón de `chequeo_esq3b.py` (que no se toca) con el vocabulario y la matriz
de la vuelta 2 (`prompt_esq3b_v2`): 9 tipos, 13 predicados (sin
`exceptua_operacion`). NO reemplaza ni modifica `validador_e1.py`; su único
destino es el REPORTE del ejecutor (conteos de tipos/predicados emitidos,
firmas aceptadas o rechazadas, anomalías). No se usa para armar las fichas
—las fichas muestran la extracción CRUDA— y no adjudica nada.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_esq3b_v2 as cc   # noqa: E402,F401  (sys.path de e1_extractor)
from comun_e1 import puntos_admitidos  # noqa: E402
import prompt_esq3b_v2 as pr  # noqa: E402


def _lista(valor):
    if isinstance(valor, str):
        try:
            valor = json.loads(valor)
        except json.JSONDecodeError:
            return None
    return valor if isinstance(valor, list) else None


def _txt(v):
    if isinstance(v, str):
        v = v.strip()
        return v or None
    return None


def chequear(tool_input, chunk: dict) -> dict:
    """Devuelve conteos y rechazos por elemento contra el esquema v2."""
    out = {
        "entidades_in": 0, "entidades_ok": 0,
        "relaciones_in": 0, "relaciones_ok": 0,
        "tipos_emitidos": {}, "predicados_emitidos": {},
        "obligacion_tipo_emitido": {},
        "rechazos": [],
    }
    if not isinstance(tool_input, dict):
        out["rechazos"].append({"nivel": "chunk", "motivo": "salida_no_dict"})
        return out
    admitidos = set(puntos_admitidos(chunk))
    entities = _lista(tool_input.get("entities"))
    relations = _lista(tool_input.get("relations"))
    if entities is None or relations is None:
        out["rechazos"].append({"nivel": "chunk",
                                "motivo": "entities_o_relations_invalidos"})
        return out

    out["entidades_in"] = len(entities)
    out["relaciones_in"] = len(relations)
    por_local: dict[str, dict] = {}
    for i, e in enumerate(entities):
        ref = f"entities[{i}]"
        if not isinstance(e, dict):
            out["rechazos"].append({"nivel": "entidad", "motivo": "entidad_no_dict",
                                    "detalle": ref})
            continue
        etype = e.get("type")
        local_id = _txt(e.get("local_id"))
        punto = _txt(e.get("punto"))
        out["tipos_emitidos"][str(etype)] = out["tipos_emitidos"].get(str(etype), 0) + 1
        if etype == "Obligacion":
            t = ((e.get("properties") or {}) or {}).get("tipo")
            out["obligacion_tipo_emitido"][str(t)] = \
                out["obligacion_tipo_emitido"].get(str(t), 0) + 1
        if etype not in pr.ENTITY_TYPES_V2:
            out["rechazos"].append({"nivel": "entidad", "motivo": "type_invalido",
                                    "detalle": f"{ref}: {etype!r}"})
            continue
        if local_id is None:
            out["rechazos"].append({"nivel": "entidad", "motivo": "local_id_ausente",
                                    "detalle": ref})
            continue
        if punto is None or punto not in admitidos:
            out["rechazos"].append({"nivel": "entidad",
                                    "motivo": "punto_ausente_o_fuera_de_admitidos",
                                    "detalle": f"{ref}: {punto!r}"})
            continue
        por_local[local_id] = e
        out["entidades_ok"] += 1

    for i, r in enumerate(relations):
        ref = f"relations[{i}]"
        if not isinstance(r, dict):
            out["rechazos"].append({"nivel": "relacion", "motivo": "relacion_no_dict",
                                    "detalle": ref})
            continue
        pred = r.get("predicate")
        out["predicados_emitidos"][str(pred)] = \
            out["predicados_emitidos"].get(str(pred), 0) + 1
        if pred not in pr.PREDICATES_V2:
            out["rechazos"].append({"nivel": "relacion", "motivo": "predicado_invalido",
                                    "detalle": f"{ref}: {pred!r}"})
            continue
        punto = _txt(r.get("punto"))
        if punto is None or punto not in admitidos:
            out["rechazos"].append({"nivel": "relacion",
                                    "motivo": "punto_ausente_o_fuera_de_admitidos",
                                    "detalle": f"{ref}: {punto!r}"})
            continue
        source, target = _txt(r.get("source")), _txt(r.get("target"))
        if pred in pr.SUJETO_PREDICATES:
            extremo = source if pred == "aplica_a" else target
            ent = por_local.get(extremo) if extremo else None
            if ent is None:
                out["rechazos"].append({"nivel": "relacion", "motivo": "ref_colgante",
                                        "detalle": f"{ref} ({pred}): {extremo!r}"})
                continue
            src_t, tgt_t = ((ent.get("type"), "Sujeto") if pred == "aplica_a"
                            else ("Sujeto", ent.get("type")))
        else:
            src_e, tgt_e = por_local.get(source), por_local.get(target)
            if src_e is None or tgt_e is None:
                out["rechazos"].append({"nivel": "relacion", "motivo": "ref_colgante",
                                        "detalle": f"{ref} ({pred}): "
                                                   f"{source!r}→{target!r}"})
                continue
            src_t, tgt_t = src_e.get("type"), tgt_e.get("type")
        if not pr.firma_valida(src_t, pred, tgt_t):
            out["rechazos"].append({"nivel": "relacion", "motivo": "firma_invalida",
                                    "detalle": f"{ref}: {src_t} --{pred}--> {tgt_t}"})
            continue
        out["relaciones_ok"] += 1

    return out
