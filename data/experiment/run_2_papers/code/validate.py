"""
validate.py — Validación estructural V1-V8 sobre el output crudo del LLM.

Implementa la sección §5 del schema.md. Trabaja sobre los entities/relations
LOCALES de un chunk (con local_id), antes de la resolución global.

Devuelve:
- Lista de violaciones (cada una con código, severidad y mensaje).
- Si el chunk debe ser marcado para retry (alguna V1-V5 o V7 disparó).
- El subset CLEAN de entities/relations que pasaron la validación.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Optional

from schema import (
    DEFAULT_VERSION,
    DEONTIC_MODALITIES,
    ENTITY_TYPES,
    PREDICATE_BY_NAME,
    PREDICATE_NAMES,
)


# Detector heurístico de "nodos que son jerarquía documental"
RE_LABEL_HIERARCHY = re.compile(
    r"^(punto|secci[oó]n|cap[ií]tulo|anexo|art[ií]culo|inciso|p[áa]rrafo|t[ií]tulo|libro|t[oó]mo)\s",
    re.IGNORECASE,
)
RE_PURE_NUMBERING = re.compile(r"^\s*\d+(\.\d+)+\s*$")  # "3.16.3.4"
# Mata-label si tiene jerarquía documental embebida ("sujeto del punto 3.2.1.1")
RE_HIERARCHY_EMBEDDED = re.compile(
    r"\b(punto|secci[oó]n|cap[ií]tulo|anexo|art[ií]culo|inciso)\s+\d+(\.\d+){1,5}\b",
    re.IGNORECASE,
)


RETRY_TRIGGERING_CODES = {"V1", "V2", "V3", "V4", "V5", "V7"}


@dataclass
class Violation:
    code: str          # "V1" .. "V8"
    severity: str      # "error" | "warning"
    msg: str
    where: str = ""    # local_id o descripción
    detail: dict = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "code": self.code,
            "severity": self.severity,
            "msg": self.msg,
            "where": self.where,
            "detail": self.detail,
        }


@dataclass
class ValidationOutcome:
    clean_entities: list[dict]
    clean_relations: list[dict]
    violations: list[Violation]
    triggers_retry: bool

    def to_dict(self) -> dict:
        return {
            "clean_entities": self.clean_entities,
            "clean_relations": self.clean_relations,
            "violations": [v.to_dict() for v in self.violations],
            "triggers_retry": self.triggers_retry,
        }


def _looks_like_doc_hierarchy(label: str) -> bool:
    if not label:
        return True
    s = label.strip()
    if RE_PURE_NUMBERING.match(s):
        return True
    if RE_LABEL_HIERARCHY.match(s):
        # excepción: "Sección de definiciones" o "Artículo del usuario" siguen siendo
        # de jerarquía documental.
        return True
    if RE_HIERARCHY_EMBEDDED.search(s):
        # "sujeto obligado del punto 3.2.1.1" → V7
        return True
    return False


def validate(raw_output: dict, source_doc: str, location: str) -> ValidationOutcome:
    """Aplica V1-V8 al output crudo. No modifica el input; devuelve clean copies."""
    raw_entities = raw_output.get("entities", []) or []
    raw_relations = raw_output.get("relations", []) or []

    violations: list[Violation] = []
    clean_entities: list[dict] = []
    accepted_ids: set[str] = set()

    # ---------- Validar entities ----------
    for e in raw_entities:
        if not isinstance(e, dict):
            violations.append(Violation("V1", "error", "Entity no es dict", detail={"raw": e}))
            continue
        local_id = str(e.get("local_id", "")).strip() or e.get("id", "")
        etype = (e.get("type") or "").strip()
        label = (e.get("label") or "").strip()
        properties = e.get("properties") or {}

        # V1 — tipo válido
        if etype not in ENTITY_TYPES:
            violations.append(Violation(
                "V1", "error",
                f"Tipo de entidad inválido: '{etype}'",
                where=local_id, detail={"label": label},
            ))
            continue

        # V7 — jerarquía documental
        if _looks_like_doc_hierarchy(label):
            violations.append(Violation(
                "V7", "error",
                f"Label parece jerarquía documental, no entidad regulatoria: '{label}'",
                where=local_id, detail={"type": etype},
            ))
            continue

        # V6 — modalidad deóntica (auto-corregible)
        if etype == "Obligacion":
            mod = (properties.get("modalidad") or "").strip().lower()
            if mod not in DEONTIC_MODALITIES:
                violations.append(Violation(
                    "V6", "warning",
                    f"Obligacion sin modalidad deóntica válida (era '{mod}'), se asigna 'obligacion'",
                    where=local_id,
                ))
                properties["modalidad"] = "obligacion"

        # version default
        if "version" not in properties:
            properties["version"] = DEFAULT_VERSION

        # Entity aceptada
        clean_e = {
            "local_id": local_id or f"auto_{len(clean_entities)}",
            "type": etype,
            "label": label,
            "properties": properties,
        }
        clean_entities.append(clean_e)
        accepted_ids.add(clean_e["local_id"])

    # ---------- Validar relations ----------
    clean_relations: list[dict] = []
    entity_type_by_id = {e["local_id"]: e["type"] for e in clean_entities}

    for r in raw_relations:
        if not isinstance(r, dict):
            violations.append(Violation("V2", "error", "Relation no es dict", detail={"raw": r}))
            continue
        rel = (r.get("relation") or "").strip()
        src = str(r.get("source") or "").strip()
        tgt = str(r.get("target") or "").strip()

        # V2 — predicado válido
        if rel not in PREDICATE_NAMES:
            violations.append(Violation(
                "V2", "error",
                f"Predicado inválido: '{rel}'",
                detail={"source": src, "target": tgt},
            ))
            continue
        spec = PREDICATE_BY_NAME[rel]

        # V5 — endpoints existen
        if src not in accepted_ids or tgt not in accepted_ids:
            violations.append(Violation(
                "V5", "error",
                f"Edge '{rel}' apunta a endpoints no extraídos en este chunk",
                detail={"source": src, "target": tgt,
                        "source_exists": src in accepted_ids,
                        "target_exists": tgt in accepted_ids},
            ))
            continue

        src_t = entity_type_by_id[src]
        tgt_t = entity_type_by_id[tgt]

        # V3 — dominio
        if src_t not in spec.domain:
            violations.append(Violation(
                "V3", "error",
                f"Predicado '{rel}' no admite dominio '{src_t}' (dominio válido: {sorted(spec.domain)})",
                detail={"source": src, "target": tgt, "src_type": src_t},
            ))
            continue

        # V4 — rango
        if spec.same_type:
            if src_t != tgt_t:
                violations.append(Violation(
                    "V4", "error",
                    f"Predicado '{rel}' requiere mismo tipo (es_subtipo_de): {src_t} vs {tgt_t}",
                    detail={"source": src, "target": tgt},
                ))
                continue
        else:
            if tgt_t not in spec.range:
                violations.append(Violation(
                    "V4", "error",
                    f"Predicado '{rel}' no admite rango '{tgt_t}' (rango válido: {sorted(spec.range)})",
                    detail={"source": src, "target": tgt, "tgt_type": tgt_t},
                ))
                continue

        clean_relations.append({
            "source": src,
            "target": tgt,
            "relation": rel,
        })

    triggers_retry = any(v.code in RETRY_TRIGGERING_CODES for v in violations)
    return ValidationOutcome(
        clean_entities=clean_entities,
        clean_relations=clean_relations,
        violations=violations,
        triggers_retry=triggers_retry,
    )


def violations_to_feedback(violations: list[Violation]) -> list[str]:
    """Convierte violaciones a strings pedagógicos para el prompt de retry."""
    out: list[str] = []
    for v in violations:
        if v.code == "V1":
            out.append(
                f"[{v.code}] {v.msg}. Tipos permitidos: {ENTITY_TYPES}."
            )
        elif v.code == "V2":
            out.append(
                f"[{v.code}] {v.msg}. Predicados permitidos: {PREDICATE_NAMES}."
            )
        elif v.code == "V3":
            out.append(
                f"[{v.code}] {v.msg}. Reformulá o descartá la tripleta."
            )
        elif v.code == "V4":
            out.append(
                f"[{v.code}] {v.msg}. Reformulá o descartá la tripleta."
            )
        elif v.code == "V5":
            out.append(
                f"[{v.code}] {v.msg}. Todas las entidades referenciadas en relations deben aparecer también en entities con el mismo local_id."
            )
        elif v.code == "V7":
            out.append(
                f"[{v.code}] {v.msg}. NO incluyas 'Punto N.N.N', 'Sección X', 'Capítulo Y', 'Anexo Z' como nodos. Esa información va en provenance."
            )
        else:
            out.append(f"[{v.code}] {v.msg}")
    return out
