"""Pydantic models para la salida estructurada del extractor.

Schema-based ESTRICTO: 7 entidades, 12 predicados. Cualquier cosa fuera de eso
se rechaza en validación (no llega al kg.json).

Aprendizajes Run 2: relations debe tener default_factory=list (no todos los
chunks producen relations). El extractor tolera chunks con entities sin relations.
"""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field, field_validator, model_validator


# === SCHEMA CERRADO ===

ENTITY_TYPES = (
    "Comunicacion",
    "TextoOrdenado",
    "EntidadFinanciera",
    "Operacion",
    "Restriccion",
    "Excepcion",
    "Obligacion",
)
EntityType = Literal[
    "Comunicacion",
    "TextoOrdenado",
    "EntidadFinanciera",
    "Operacion",
    "Restriccion",
    "Excepcion",
    "Obligacion",
]

PREDICATES = (
    "establecida_en",
    "referencia",
    "modificada_por",
    "aplica_a",
    "regula",
    "exceptua",
    "exceptua_obligacion",
    "prohibe",
    "limita",
    "ejecuta",
    "requiere",
    "condiciona",
)
Predicate = Literal[
    "establecida_en",
    "referencia",
    "modificada_por",
    "aplica_a",
    "regula",
    "exceptua",
    "exceptua_obligacion",
    "prohibe",
    "limita",
    "ejecuta",
    "requiere",
    "condiciona",
]


# Tabla dominio/rango canónica del schema.md. Se usa para filtrar tripletas
# inválidas en post-proceso.
DOMAIN_RANGE: dict[str, tuple[set[str], set[str]]] = {
    "establecida_en":        ({"Restriccion", "Obligacion", "Excepcion", "Operacion"}, {"TextoOrdenado"}),
    "referencia":            ({"TextoOrdenado"}, {"Comunicacion"}),
    "modificada_por":        ({"TextoOrdenado"}, {"Comunicacion"}),
    "aplica_a":              ({"Restriccion", "Obligacion"}, {"EntidadFinanciera"}),
    "regula":                ({"Restriccion", "Obligacion"}, {"Operacion"}),
    "exceptua":              ({"Excepcion"}, {"Restriccion"}),
    "exceptua_obligacion":   ({"Excepcion"}, {"Obligacion"}),
    "prohibe":               ({"Restriccion"}, {"Operacion"}),
    "limita":                ({"Restriccion"}, {"Operacion"}),
    "ejecuta":               ({"EntidadFinanciera"}, {"Operacion"}),
    "requiere":              ({"Operacion"}, {"Obligacion"}),
    "condiciona":            ({"Obligacion"}, {"Operacion"}),
}


# === MODELOS PYDANTIC ===

class EntityOut(BaseModel):
    """Entidad extraída por el LLM."""
    local_id: str = Field(description="Identificador local dentro del chunk (e.g., 'e1', 'e2'). Usado para referenciar en relations.")
    type: EntityType = Field(description="Tipo de entidad (uno de los 7).")
    label: str = Field(description="Etiqueta legible humana (ej. 'Comunicación A 7825', 'Bancos comerciales', 'Restricción de financiación al sector público').")
    properties: dict[str, str] = Field(
        default_factory=dict,
        description="Propiedades de la entidad (key=str, value=str). Ver schema.md para propiedades requeridas por tipo.",
    )

    @field_validator("label")
    @classmethod
    def label_not_empty(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("label no puede estar vacío")
        return v

    @model_validator(mode="before")
    @classmethod
    def coerce_properties_to_str(cls, data):
        """Coerce property values to strings.

        El LLM tiende a devolver enteros/floats para campos como 'numero',
        'umbral', 'plazo' aunque el schema diga string. Coerción robusta evita
        validaciones rotas por trivialidades de tipo (Run 1+2 lección).
        """
        if isinstance(data, dict) and "properties" in data and isinstance(data["properties"], dict):
            data["properties"] = {
                str(k): ("" if v is None else str(v))
                for k, v in data["properties"].items()
            }
        return data


class RelationOut(BaseModel):
    """Relación entre dos entidades del MISMO chunk."""
    source: str = Field(description="local_id de la entidad source (debe existir en entities del mismo chunk).")
    target: str = Field(description="local_id de la entidad target (debe existir en entities del mismo chunk).")
    predicate: Predicate = Field(description="Tipo de relación (uno de los 12).")


class ExtractionOut(BaseModel):
    """Salida estructurada del LLM para un chunk."""
    entities: list[EntityOut] = Field(default_factory=list)
    relations: list[RelationOut] = Field(default_factory=list)

    @model_validator(mode="before")
    @classmethod
    def coerce_lists_from_json_string(cls, data):
        """Algunas veces el LLM devuelve entities/relations como STRING JSON
        (en lugar de array). Coercer si es el caso."""
        import json as _json
        if isinstance(data, dict):
            for key in ("entities", "relations"):
                v = data.get(key)
                if isinstance(v, str):
                    try:
                        parsed = _json.loads(v)
                        if isinstance(parsed, list):
                            data[key] = parsed
                    except _json.JSONDecodeError:
                        pass  # Pydantic dará error claro abajo
        return data


# === FUNCIONES DE VALIDACIÓN POST-EXTRACCIÓN ===

def is_valid_triple(source_type: str, predicate: str, target_type: str) -> bool:
    """Valida (dominio, predicado, rango) contra DOMAIN_RANGE."""
    if predicate not in DOMAIN_RANGE:
        return False
    dom, ran = DOMAIN_RANGE[predicate]
    return source_type in dom and target_type in ran


def filter_extraction(extraction: ExtractionOut) -> tuple[ExtractionOut, dict[str, int]]:
    """Filtra entities/relations contra el schema cerrado.

    Devuelve (extracción_filtrada, métricas) donde métricas cuenta descartes por causa.
    """
    metrics = {
        "entities_in": len(extraction.entities),
        "entities_out": 0,
        "relations_in": len(extraction.relations),
        "relations_out": 0,
        "rel_dropped_unknown_predicate": 0,
        "rel_dropped_dangling_ref": 0,
        "rel_dropped_domain_range": 0,
    }

    # Entities ya están validadas a nivel Literal por Pydantic. Pasan todas.
    out_entities = list(extraction.entities)
    metrics["entities_out"] = len(out_entities)

    by_local: dict[str, EntityOut] = {e.local_id: e for e in out_entities}

    out_relations: list[RelationOut] = []
    for r in extraction.relations:
        # Pydantic ya bloquea predicados fuera de la lista. Defensivo igual.
        if r.predicate not in DOMAIN_RANGE:
            metrics["rel_dropped_unknown_predicate"] += 1
            continue
        src = by_local.get(r.source)
        tgt = by_local.get(r.target)
        if src is None or tgt is None:
            metrics["rel_dropped_dangling_ref"] += 1
            continue
        if not is_valid_triple(src.type, r.predicate, tgt.type):
            metrics["rel_dropped_domain_range"] += 1
            continue
        out_relations.append(r)

    metrics["relations_out"] = len(out_relations)
    return ExtractionOut(entities=out_entities, relations=out_relations), metrics


def empty_metrics() -> dict[str, int]:
    return {
        "entities_in": 0,
        "entities_out": 0,
        "relations_in": 0,
        "relations_out": 0,
        "rel_dropped_unknown_predicate": 0,
        "rel_dropped_dangling_ref": 0,
        "rel_dropped_domain_range": 0,
    }


def merge_metrics(a: dict[str, int], b: dict[str, int]) -> dict[str, int]:
    out = empty_metrics()
    for k in out:
        out[k] = a.get(k, 0) + b.get(k, 0)
    return out
