"""
validador_e1.py — Validación determinística de la salida del extractor E1 (T3).

Código puro, sin LLM (principio 2.b del diseño: lo determinístico va en
código). Toma el input del tool call del extractor y el chunk de E0, y valida:

  1. Estructura parseable (dict con entities/relations; coerción defensiva de
     listas serializadas como string — lección heredada del schema v2).
  2. Conformidad con el esquema v2: types contra ENTITY_TYPES, predicados y
     firmas de aristas contra la matriz DOMAIN_RANGE, sujetos contra el
     catálogo cerrado (sujeto_id ∈ catálogo; sujeto_id/sujeto_propuesto
     mutuamente excluyentes; padre sugerido fuera de catálogo se anula).
  3. Provenance presente en TODO elemento: campo `punto` obligatorio y dentro
     del conjunto admitido del chunk (punto propio + unidades de herencia).

Todo rechazo queda REGISTRADO con motivo estable (input del mini-ratchet de
E3, que en esta fase solo se registra — no hay re-extracción acá). Los
rechazos son por elemento: un elemento inválido no tumba el chunk; una
estructura no parseable sí (rechazo a nivel chunk).
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field

import comun_e1  # noqa: F401  (sys.path para schema)
from comun_e1 import chunk_flaggeado, puntos_admitidos, rol_documental_de_punto
from schema import (
    ENTITY_TYPES,
    PREDICATES,
    SUJETO_PREDICATES,
    SUJETOS_CATALOGO_SET,
    is_valid_triple,
)


@dataclass
class ResultadoValidacion:
    chunk_id: str
    entidades: list[dict] = field(default_factory=list)
    relaciones: list[dict] = field(default_factory=list)
    omisiones_no_prosa: list[str] = field(default_factory=list)
    rechazos: list[dict] = field(default_factory=list)      # motivo registrado
    advertencias: list[dict] = field(default_factory=list)  # registro, no rechazo
    metricas: dict = field(default_factory=dict)

    @property
    def chunk_rechazado(self) -> bool:
        return any(r["nivel"] == "chunk" for r in self.rechazos)

    def as_dict(self) -> dict:
        return {
            "chunk_id": self.chunk_id,
            "entidades": self.entidades,
            "relaciones": self.relaciones,
            "omisiones_no_prosa": self.omisiones_no_prosa,
            "rechazos": self.rechazos,
            "advertencias": self.advertencias,
            "metricas": self.metricas,
        }


def _rechazo(nivel: str, motivo: str, detalle: str, elemento=None) -> dict:
    r = {"nivel": nivel, "motivo": motivo, "detalle": detalle}
    if elemento is not None:
        r["elemento"] = elemento
    return r


def _coerce_lista(valor):
    """entities/relations pueden llegar como string JSON (slip conocido del
    extractor v2). Coerción defensiva; si no es lista al final, es None."""
    if isinstance(valor, str):
        try:
            valor = json.loads(valor)
        except json.JSONDecodeError:
            return None
    return valor if isinstance(valor, list) else None


def _str_o_none(v):
    if isinstance(v, str):
        v = v.strip()
        return v or None
    return None


def validar_salida(tool_input, chunk: dict, canal_abierto: bool = False) -> ResultadoValidacion:
    """Valida el input del tool call de un chunk. Devuelve elementos aceptados
    (normalizados, con provenance completa {to, archivo, punto, rol_documental})
    y rechazos con motivo registrado.

    canal_abierto (experimental, explícito, default False = comportamiento de
    producción sin cambio alguno): habilita los campos tipo_propuesto (en
    entidades, junto a type) y predicado_propuesto (en relaciones, junto a
    predicate), calcados de sujeto_propuesto. Exclusión mutua exacta con
    type/predicate; los enums no se relajan. Una propuesta transportada por un
    elemento que este validador rechaza NO se pierde para la medición: vive en
    tool_input_crudo (el validador no muta su input)."""
    res = ResultadoValidacion(chunk_id=chunk["id"])
    admitidos = set(puntos_admitidos(chunk))

    # --- Nivel chunk: estructura ---
    if isinstance(tool_input, str):
        try:
            tool_input = json.loads(tool_input)
        except json.JSONDecodeError as e:
            res.rechazos.append(_rechazo("chunk", "salida_no_parseable", f"JSON inválido: {e}"))
            res.metricas = _metricas(res, 0, 0)
            return res
    if not isinstance(tool_input, dict):
        res.rechazos.append(_rechazo("chunk", "salida_no_dict", f"tipo {type(tool_input).__name__}"))
        res.metricas = _metricas(res, 0, 0)
        return res

    entities = _coerce_lista(tool_input.get("entities"))
    relations = _coerce_lista(tool_input.get("relations"))
    if entities is None or relations is None:
        res.rechazos.append(_rechazo(
            "chunk", "entities_o_relations_invalidos",
            "entities/relations ausentes o no-lista (ni siquiera como string JSON)"))
        res.metricas = _metricas(res, 0, 0)
        return res

    omisiones = tool_input.get("omisiones_no_prosa") or []
    if isinstance(omisiones, list):
        res.omisiones_no_prosa = [o for o in omisiones if isinstance(o, str) and o.strip()]

    # --- Entidades ---
    by_local: dict[str, dict] = {}
    for i, e in enumerate(entities):
        ref = f"entities[{i}]"
        if not isinstance(e, dict):
            res.rechazos.append(_rechazo("entidad", "entidad_no_dict", ref, e))
            continue
        local_id = _str_o_none(e.get("local_id"))
        etype = e.get("type")
        label = _str_o_none(e.get("label"))
        punto = _str_o_none(e.get("punto"))

        tipo_prop = _str_o_none(e.get("tipo_propuesto")) if canal_abierto else None

        if local_id is None:
            res.rechazos.append(_rechazo("entidad", "local_id_ausente", ref, e))
            continue
        if local_id in by_local:
            res.rechazos.append(_rechazo("entidad", "local_id_duplicado", f"{ref}: '{local_id}'", e))
            continue
        if tipo_prop is not None:
            # Canal abierto: tipo propuesto fuera de esquema. Exclusión mutua
            # exacta con type (calcada de sujeto_id/sujeto_propuesto): un tipo
            # fuera de esquema jamás entra silencioso en el enum.
            if etype is not None:
                res.rechazos.append(_rechazo(
                    "entidad", "tipo_canal_invalido",
                    f"{ref} ({local_id}): requiere exactamente UNO de type/tipo_propuesto", e))
                continue
        elif etype not in ENTITY_TYPES:
            res.rechazos.append(_rechazo("entidad", "type_invalido", f"{ref}: '{etype}'", e))
            continue
        if label is None:
            res.rechazos.append(_rechazo("entidad", "label_vacio", ref, e))
            continue
        if punto is None:
            res.rechazos.append(_rechazo("entidad", "punto_ausente", f"{ref} ({local_id})", e))
            continue
        if punto not in admitidos:
            res.rechazos.append(_rechazo(
                "entidad", "punto_fuera_de_admitidos",
                f"{ref} ({local_id}): '{punto}' ∉ {sorted(admitidos)}", e))
            continue

        props_in = e.get("properties") or {}
        props = (
            {str(k): ("" if v is None else str(v)) for k, v in props_in.items()}
            if isinstance(props_in, dict) else {}
        )

        norm = {
            "local_id": local_id,
            "type": etype,
            "label": label,
            "properties": props,
            "provenance": {
                "to": chunk["to"],
                "archivo": chunk["archivo"],
                "punto": punto,
                "rol_documental": rol_documental_de_punto(chunk, punto),
            },
        }
        if canal_abierto:
            # junto a type, análogo a sujeto_propuesto en relaciones: la clave
            # existe en TODA entidad validada de una corrida con canal abierto
            # (None cuando la entidad usa el enum). Con el flag apagado la
            # clave NO existe: salida byte-idéntica a producción.
            norm["tipo_propuesto"] = tipo_prop
        by_local[local_id] = norm
        res.entidades.append(norm)

        if len(label.split()) > 12:
            res.advertencias.append({
                "tipo": "label_largo", "local_id": local_id,
                "detalle": f"{len(label.split())} palabras (regla: ≤8, tolerancia 12)"})

    # --- Relaciones ---
    for i, r in enumerate(relations):
        ref = f"relations[{i}]"
        if not isinstance(r, dict):
            res.rechazos.append(_rechazo("relacion", "relacion_no_dict", ref, r))
            continue
        pred = r.get("predicate")
        pred_prop = _str_o_none(r.get("predicado_propuesto")) if canal_abierto else None
        if pred_prop is not None:
            # Canal abierto: predicado propuesto fuera de esquema. Exclusión
            # mutua exacta con predicate (calcada de sujeto_id/sujeto_propuesto).
            if pred is not None:
                res.rechazos.append(_rechazo(
                    "relacion", "predicado_canal_invalido",
                    f"{ref}: requiere exactamente UNO de predicate/predicado_propuesto", r))
                continue
        elif pred not in PREDICATES:
            res.rechazos.append(_rechazo("relacion", "predicado_invalido", f"{ref}: '{pred}'", r))
            continue

        punto = _str_o_none(r.get("punto"))
        if punto is None:
            res.rechazos.append(_rechazo("relacion", "punto_ausente", f"{ref} ({pred})", r))
            continue
        if punto not in admitidos:
            res.rechazos.append(_rechazo(
                "relacion", "punto_fuera_de_admitidos",
                f"{ref} ({pred}): '{punto}' ∉ {sorted(admitidos)}", r))
            continue

        source = _str_o_none(r.get("source"))
        target = _str_o_none(r.get("target"))
        sujeto_id = _str_o_none(r.get("sujeto_id"))
        sujeto_prop = _str_o_none(r.get("sujeto_propuesto"))
        padre_sug = _str_o_none(r.get("sujeto_propuesto_padre_sugerido"))

        if pred_prop is not None:
            # Predicado propuesto: no existe firma en DOMAIN_RANGE contra la
            # cual validar (ni forma de saber si el extremo es un sujeto), así
            # que extremos y sujeto_* pasan normalizados tal como vienen. El
            # anclaje (`punto`) ya se validó arriba como en toda relación.
            pass
        elif pred in SUJETO_PREDICATES:
            # Slip predecible heredado del v2: extremo sujeto mandado además
            # en target (aplica_a) / source (ejecuta) → se ignora ese campo.
            if pred == "aplica_a":
                target = None
            else:
                source = None

            if (sujeto_id is None) == (sujeto_prop is None):
                res.rechazos.append(_rechazo(
                    "relacion", "sujeto_extremo_invalido",
                    f"{ref} ({pred}): requiere exactamente UNO de sujeto_id/sujeto_propuesto", r))
                continue
            if sujeto_id is not None and sujeto_id not in SUJETOS_CATALOGO_SET:
                res.rechazos.append(_rechazo(
                    "relacion", "sujeto_id_fuera_de_catalogo", f"{ref}: '{sujeto_id}'", r))
                continue
            if padre_sug is not None and sujeto_prop is None:
                res.rechazos.append(_rechazo(
                    "relacion", "padre_sugerido_sin_propuesto", ref, r))
                continue
            if padre_sug is not None and padre_sug not in SUJETOS_CATALOGO_SET:
                padre_sug = None  # pista inválida: se anula, no invalida la relación

            extremo_chunk = source if pred == "aplica_a" else target
            campo = "source" if pred == "aplica_a" else "target"
            if extremo_chunk is None:
                res.rechazos.append(_rechazo(
                    "relacion", "extremo_chunk_ausente", f"{ref} ({pred}): falta {campo}", r))
                continue
            ent = by_local.get(extremo_chunk)
            if ent is None:
                res.rechazos.append(_rechazo(
                    "relacion", "ref_colgante", f"{ref} ({pred}): {campo}='{extremo_chunk}'", r))
                continue
            src_t, tgt_t = (ent["type"], "Sujeto") if pred == "aplica_a" else ("Sujeto", ent["type"])
            if not is_valid_triple(src_t, pred, tgt_t):
                res.rechazos.append(_rechazo(
                    "relacion", "firma_invalida", f"{ref}: {src_t} --{pred}--> {tgt_t}", r))
                continue
        else:
            if sujeto_id or sujeto_prop or padre_sug:
                res.rechazos.append(_rechazo(
                    "relacion", "sujeto_en_predicado_no_sujeto",
                    f"{ref}: sujeto_* solo vale en {SUJETO_PREDICATES}, no en {pred}", r))
                continue
            if source is None or target is None:
                res.rechazos.append(_rechazo(
                    "relacion", "extremo_chunk_ausente", f"{ref} ({pred}): requiere source y target", r))
                continue
            src_e, tgt_e = by_local.get(source), by_local.get(target)
            if src_e is None or tgt_e is None:
                res.rechazos.append(_rechazo(
                    "relacion", "ref_colgante",
                    f"{ref} ({pred}): source='{source}' target='{target}'", r))
                continue
            if not is_valid_triple(src_e["type"], pred, tgt_e["type"]):
                res.rechazos.append(_rechazo(
                    "relacion", "firma_invalida",
                    f"{ref}: {src_e['type']} --{pred}--> {tgt_e['type']}", r))
                continue

        rel_out = {
            "source": source,
            "target": target,
            "predicate": pred,
            "sujeto_id": sujeto_id,
            "sujeto_propuesto": sujeto_prop,
            "sujeto_propuesto_padre_sugerido": padre_sug,
            "provenance": {
                "to": chunk["to"],
                "archivo": chunk["archivo"],
                "punto": punto,
                "rol_documental": rol_documental_de_punto(chunk, punto),
            },
        }
        if canal_abierto:
            # junto a predicate, análogo a sujeto_propuesto: la clave existe
            # en TODA relación validada de una corrida con canal abierto (None
            # cuando la relación usa el enum). Con el flag apagado la clave NO
            # existe: salida byte-idéntica a producción.
            rel_out["predicado_propuesto"] = pred_prop
        res.relaciones.append(rel_out)

    # --- Registro del tratamiento de flags (no rechaza: insumo de E3) ---
    if chunk_flaggeado(chunk):
        extrajo_algo = any(e["type"] != "TextoOrdenado" for e in res.entidades)
        if extrajo_algo and not res.omisiones_no_prosa:
            res.advertencias.append({
                "tipo": "flag_sin_omisiones_declaradas",
                "detalle": "chunk flaggeado tabular/formula con extracción y sin omisiones registradas"})
        if not extrajo_algo and not res.omisiones_no_prosa:
            res.advertencias.append({
                "tipo": "flag_vacio_sin_registro",
                "detalle": "chunk flaggeado sin extracción y sin omisiones registradas"})

    res.metricas = _metricas(res, len(entities), len(relations))
    return res


def _metricas(res: ResultadoValidacion, n_ent_in: int, n_rel_in: int) -> dict:
    por_motivo: dict[str, int] = {}
    for r in res.rechazos:
        por_motivo[r["motivo"]] = por_motivo.get(r["motivo"], 0) + 1
    return {
        "entities_in": n_ent_in,
        "entities_out": len(res.entidades),
        "relations_in": n_rel_in,
        "relations_out": len(res.relaciones),
        "rechazos": len(res.rechazos),
        "rechazos_por_motivo": por_motivo,
        "advertencias": len(res.advertencias),
    }
