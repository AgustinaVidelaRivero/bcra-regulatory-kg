"""
Modelos Pydantic del Run 5 — Híbrido core + emergente.

Dos capas de modelos:

1. *ModelOutput*: lo que devuelve Haiku en cada chunk. NO contiene `provenance` —
   el modelo no la emite (decisión 3.7 de schema.md), el pipeline la inyecta.
2. *KGNode / KGEdge*: lo que va al `kg.json` final, ya con `provenance` adosado
   desde el contexto del chunk de origen.

Tolerancia a fallos: `relations` tiene `default_factory=list` (lección Run 1, punto
4) para no romper si un chunk solo extrae entities sin relations.
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


# ---------- Lo que devuelve el modelo en cada chunk ----------


class ExtractedEntity(BaseModel):
    """Entidad tal como el LLM la emite. Sin provenance."""

    id: str
    type: str
    label: str
    properties: dict[str, Any] = Field(default_factory=dict)


class ExtractedRelation(BaseModel):
    """Relación tal como el LLM la emite. Sin provenance."""

    source: str
    target: str
    predicate: str


class ChunkExtraction(BaseModel):
    """Output crudo del LLM para un chunk: entities + relations, sin provenance."""

    entities: list[ExtractedEntity] = Field(default_factory=list)
    relations: list[ExtractedRelation] = Field(default_factory=list)


# ---------- Provenance y nodos/aristas del kg.json final ----------


class Provenance(BaseModel):
    """Provenance que el pipeline inyecta a cada nodo/edge del KG."""

    source_doc: str
    location: str


class KGNode(BaseModel):
    """Nodo final del kg.json, ya con provenance inyectada."""

    id: str
    type: str
    label: str
    properties: dict[str, Any] = Field(default_factory=dict)
    provenance: Provenance


class KGEdge(BaseModel):
    """Arista final del kg.json, ya con provenance inyectada."""

    source: str
    target: str
    relation: str
    provenance: Provenance


class KnowledgeGraph(BaseModel):
    """Grafo completo serializado al kg.json."""

    nodes: list[KGNode] = Field(default_factory=list)
    edges: list[KGEdge] = Field(default_factory=list)


# ---------- Estructura de chunk que va al pipeline ----------


class Chunk(BaseModel):
    """Un fragmento del TO listo para enviarse al extractor."""

    chunk_id: str
    source_doc: str
    location: str  # ruta jerárquica del punto/sección, p. ej. "Sección 1, punto 1.2.3"
    text: str
