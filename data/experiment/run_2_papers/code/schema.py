"""
schema.py — Tipos de entidad, predicados controlados, dominio/rango.

La fuente de verdad humana es ../schema.md. Este archivo es la traducción
ejecutable: lo que el pipeline usa para validar (V1-V8) y para construir
el SYSTEM_PROMPT.

Run 2 — Papers del estado del arte.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

# ---------------------------------------------------------------------------
# Tipos de entidad (12). Ver schema.md §2.
# ---------------------------------------------------------------------------

ENTITY_TYPES: list[str] = [
    "SujetoRegulado",
    "OrganismoRegulador",
    "Obligacion",
    "Operacion",
    "ConceptoDefinido",
    "Requisito",
    "Umbral",
    "Plazo",
    "Procedimiento",
    "Sancion",
    "InstrumentoFinanciero",
    "NormaReferenciada",
]

ENTITY_TYPE_DEFINITIONS: dict[str, str] = {
    "SujetoRegulado": "Persona física/jurídica a la que la norma le impone deberes o le habilita facultades (entidades financieras, bancos, casas de cambio, usuarios financieros, fiduciarios).",
    "OrganismoRegulador": "Autoridad que emite, supervisa, recibe informes o impone sanciones (BCRA, SEFyC, UIF, AFIP, CNV).",
    "Obligacion": "Deber, prohibición o facultad que la norma establece. Modalidad deóntica en properties.modalidad ∈ {obligacion, prohibicion, facultad}.",
    "Operacion": "Acción/transacción regulada (compra de divisas, otorgamiento de préstamo, transferencia al exterior, depósito a plazo).",
    "ConceptoDefinido": "Definición técnica o legal establecida por la norma (deudor en situación 1, patrimonio neto computable, cliente financiero).",
    "Requisito": "Condición técnica/operativa que se debe cumplir (presentar DDJJ, contar con sistema informático apto).",
    "Umbral": "Valor numérico/cuantitativo que activa, limita o califica una obligación u operación (8% RPC, USD 10.000 mensuales).",
    "Plazo": "Especificación temporal (mensual, 30 días corridos, primer día hábil del mes siguiente).",
    "Procedimiento": "Secuencia operativa estructurada que debe seguirse (presentación del RICM, procedimiento de reclamo).",
    "Sancion": "Consecuencia por incumplimiento (multa, suspensión, observación, intimación).",
    "InstrumentoFinanciero": "Producto/contrato regulado (préstamo hipotecario, depósito a plazo, garantía prendaria, tarjeta de crédito).",
    "NormaReferenciada": "Otra norma citada por el TO (Ley 21.526, Decreto 540/24, Comunicación 'A' 7891, otro Texto Ordenado).",
}

DEONTIC_MODALITIES = {"obligacion", "prohibicion", "facultad"}

# ---------------------------------------------------------------------------
# Vocabulario controlado de predicados (23). Ver schema.md §3.
# Cada predicado declara dominio y rango.
# `same` significa "rango debe ser igual al tipo del sujeto".
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class PredicateSpec:
    name: str
    domain: frozenset[str]
    range: frozenset[str]
    same_type: bool = False  # si True, type(target) debe == type(source)
    definition: str = ""


def _spec(name: str, dom: list[str], rng: list[str], same_type: bool = False, defn: str = "") -> PredicateSpec:
    return PredicateSpec(
        name=name,
        domain=frozenset(dom),
        range=frozenset(rng),
        same_type=same_type,
        definition=defn,
    )


PREDICATES: list[PredicateSpec] = [
    # 3.1 Imputación
    _spec("obligado_a", ["SujetoRegulado"], ["Obligacion"],
          defn="El sujeto regulado tiene asignada esta obligación."),
    _spec("puede_realizar", ["SujetoRegulado"], ["Operacion"],
          defn="El sujeto está habilitado para realizar la operación."),
    _spec("supervisado_por", ["SujetoRegulado", "Operacion"], ["OrganismoRegulador"],
          defn="El sujeto u operación está bajo supervisión del organismo."),
    # 3.2 Aplicabilidad
    _spec("aplica_a", ["Obligacion"],
          ["SujetoRegulado", "Operacion", "InstrumentoFinanciero", "Procedimiento", "ConceptoDefinido"],
          defn="La obligación se aplica al sujeto, operación, instrumento, procedimiento o concepto definido. "
               "(Rango ampliado post-smoke: Procedimiento y ConceptoDefinido son destinos legítimos observados en el corpus.)"),
    _spec("condicion_de_aplicabilidad", ["Requisito"], ["Obligacion", "Operacion"],
          defn="La obligación/operación solo aplica si se cumple este requisito (precondición normativa)."),
    _spec("excepcion_a", ["Obligacion"], ["Obligacion"],
          defn="Esta obligación constituye una excepción a otra obligación."),
    # 3.3 Composición operativa
    _spec("requiere",
          ["Obligacion", "Operacion", "Procedimiento", "InstrumentoFinanciero", "Sancion"],
          ["Requisito"],
          defn="Para satisfacer/realizar/ejecutar/usar/imponer se necesita cumplir este requisito. "
               "(Dominio ampliado post-smoke: instrumentos y sanciones también pueden tener requisitos legítimos.)"),
    _spec("involucra_instrumento", ["Operacion", "Obligacion"], ["InstrumentoFinanciero"],
          defn="La operación u obligación opera sobre o se refiere a este instrumento. "
               "(Dominio ampliado post-smoke: obligaciones también pueden ser sobre instrumentos.)"),
    _spec("requiere_autorizacion_de", ["Operacion"], ["OrganismoRegulador"],
          defn="La operación requiere autorización previa del organismo."),
    _spec("parte_de_procedimiento", ["Operacion", "Requisito"], ["Procedimiento"],
          defn="La operación o requisito es parte de un procedimiento más amplio."),
    _spec("ejecutado_por", ["Procedimiento"], ["SujetoRegulado"],
          defn="El procedimiento debe ejecutarlo este sujeto."),
    _spec("dirigido_a", ["Procedimiento"], ["OrganismoRegulador"],
          defn="El procedimiento se presenta o se dirige a este organismo."),
    # 3.4 Cuantitativas/temporales
    _spec("tiene_plazo", ["Obligacion", "Operacion", "Procedimiento"], ["Plazo"],
          defn="Debe cumplirse en este plazo."),
    _spec("tiene_umbral", ["Obligacion", "Operacion", "InstrumentoFinanciero"], ["Umbral"],
          defn="Está sujeto a este umbral cuantitativo."),
    # 3.5 Sancionatorias
    _spec("genera_sancion", ["Obligacion"], ["Sancion"],
          defn="El incumplimiento de la obligación genera esta sanción."),
    _spec("impuesta_por", ["Sancion"], ["OrganismoRegulador"],
          defn="La sanción es impuesta por este organismo."),
    _spec("recae_sobre", ["Sancion"], ["SujetoRegulado"],
          defn="La sanción se impone a este sujeto regulado."),
    # 3.6 Conceptuales/referenciales
    _spec("definido_por", ["ConceptoDefinido"], ["NormaReferenciada"],
          defn="El concepto está definido por una norma externa citada."),
    _spec("usa_concepto",
          ["Obligacion", "Operacion", "Requisito", "Procedimiento", "ConceptoDefinido"],
          ["ConceptoDefinido"],
          defn="La entidad invoca el concepto definido. "
               "(Dominio ampliado post-smoke: un concepto definido también puede apoyarse en otro concepto definido.)"),
    _spec("clasifica_a", ["Obligacion", "Procedimiento"], ["ConceptoDefinido"],
          defn="La obligación o procedimiento produce una clasificación según el concepto."),
    _spec("referencia",
          ["Obligacion", "Operacion", "ConceptoDefinido", "Procedimiento", "Requisito"],
          ["NormaReferenciada"],
          defn="La entidad referencia o se remite a una norma externa (cross-reference)."),
    _spec("modifica", ["NormaReferenciada"], ["NormaReferenciada"],
          defn="Una norma modifica, complementa, deroga o sustituye a otra."),
    # 3.7 Taxonomía
    _spec("es_subtipo_de", ENTITY_TYPES, ENTITY_TYPES, same_type=True,
          defn="Subsunción taxonómica. Sujeto y objeto deben ser del MISMO tipo."),
]

PREDICATE_BY_NAME: dict[str, PredicateSpec] = {p.name: p for p in PREDICATES}
PREDICATE_NAMES: list[str] = [p.name for p in PREDICATES]


# ---------------------------------------------------------------------------
# Provenance schema (regla común del protocolo)
# ---------------------------------------------------------------------------


@dataclass
class Provenance:
    source_doc: str
    location: str

    def to_dict(self) -> dict:
        return {"source_doc": self.source_doc, "location": self.location}


# ---------------------------------------------------------------------------
# Versión vigente por default (regla 2 del protocolo)
# ---------------------------------------------------------------------------

DEFAULT_VERSION = "vigente_2026-05"


# ---------------------------------------------------------------------------
# Helpers para el SYSTEM_PROMPT (renderizado del vocabulario controlado)
# ---------------------------------------------------------------------------


def render_entity_types_for_prompt() -> str:
    lines = []
    for t in ENTITY_TYPES:
        lines.append(f"- `{t}`: {ENTITY_TYPE_DEFINITIONS[t]}")
    return "\n".join(lines)


def render_predicates_for_prompt() -> str:
    lines = []
    for p in PREDICATES:
        if p.same_type:
            sig = "DOMINIO=RANGO (mismo tipo en ambos extremos)"
        else:
            dom = " | ".join(sorted(p.domain))
            rng = " | ".join(sorted(p.range))
            sig = f"DOMINIO: {dom}  →  RANGO: {rng}"
        lines.append(f"- `{p.name}` ({sig}): {p.definition}")
    return "\n".join(lines)
