"""
perfil_e1.py — U-CABLE-V3: registro de PERFILES DE EXTRACCIÓN E1.

Un perfil empaqueta TODO lo que varía entre el prefijo de producción del
corpus de desarrollo y el prefijo v3 sellado por U-B5.4: constructor de
request, mensaje de usuario, tabla TO→rol, vocabulario de validación
(tipos / predicados / firmas / catálogo de sujetos) y labels del catálogo
para el ensamblado E2. El manifiesto de corpus declara qué perfil usa su
corrida (campo `perfil_e1`, default el de desarrollo); el runner despacha.

Perfiles:
  - "produccion_dev" (default): el pipeline vigente TAL CUAL — prompt_e1 +
    schema v2. `esquema`, `labels_catalogo` y `prefijo_hash_para_namespace`
    van en None: cada consumidor (validador_e1, e2_lib, cliente_e1) toma su
    camino default, byte-idéntico al comportamiento sellado.
  - "v3_b54": el prefijo v3 (catálogo de sujetos v3 sobre el esquema
    CONGELADO del gate ESQ-3), importado del módulo SELLADO
    data/experiment/b54_catalogo_v3/code/prompt_v3_b54.py (solo lectura).
    CANDADO (mandato U-CABLE-V3, decisión 1): la construcción del perfil
    recomputa sha256 y hash canónico del prefijo integrado y FRENA con
    RuntimeError si no reproducen exactamente el sello; corre al cargar el
    manifiesto, antes de toda llamada. El vocabulario de validación es el
    del esquema congelado COMPLETO (resolución 1 del freno 1: 9 tipos /
    13 predicados / firma_valida de prompt_congelado), no solo el catálogo.

NOTA DE INTEGRACIÓN VINCULANTE (mandato U-CABLE-V3, decisión 2): en
ROL_POR_TO_V3 los 36 mapeos a clase portan un id de CLASE en el campo
`rol_id`. Todo consumidor de este campo (mensaje, manifiesto, selftests) lo
lee como «sujeto por defecto del TO» — nunca asume que es un rol. La entrada
ri2_ci lleva `rol_id` None con `clase_ids` de dos clases; docvig y fimipyme
no tienen entrada (huecos del laudo F1.2, válvula sujeto_propuesto abierta).

Caching (docs/decisiones_caching_extraccion.md, vinculantes): el perfil no
llama a ninguna API. D1 la cumple el constructor de request de cada modo
(system como bloque único con cache_control ephemeral). Never-pay-twice
(decisión 4 del mandato): el namespace v3 se deriva del hash sellado
54a111e2175f con el MISMO patrón vigente de cliente_e1.namespace_e1; las
keys viejas de la db no se tocan (la key incluye el namespace).

Los imports pesados viven DENTRO de las factories: cargar este módulo es
barato (el loader de manifiesto lo importa solo para validar el nombre del
perfil, incluso sobre fixtures sintéticos con validar_roles=False).
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

_BASE = Path(__file__).resolve().parent                 # e1_extractor/
_REPO = _BASE.parents[3]                                # raíz del repo
_B54_CODE = _REPO / "data" / "experiment" / "b54_catalogo_v3" / "code"

PERFILES_CONOCIDOS = ("produccion_dev", "v3_b54")
PERFIL_DEFAULT = "produccion_dev"

# Candado del sello v3 (commit de cierre de U-B5.4). Literales propios de
# este módulo — independientes de los que porta el módulo sellado.
PREFIJO_SHA256_V3_ESPERADO = (
    "35e88c2dd0a2920302c29005b08ab9689405606d4bd5fcf8fb7ce807b1a3c512"
)
PREFIJO_HASH_V3_ESPERADO = "54a111e2175f"


@dataclass(frozen=True)
class EsquemaValidacion:
    """Vocabulario contra el que validan validador_e1 y e2_lib en modo v3.
    En el perfil de desarrollo NO existe (el campo `esquema` del perfil es
    None y cada consumidor usa su default sellado)."""
    entity_types: tuple
    predicates: tuple
    sujeto_predicates: tuple
    sujetos_catalogo_set: frozenset
    firma_valida: Callable[[str, str, str], bool]
    # Enum de Obligacion.properties.tipo (resolución 2 del freno 1): fuera de
    # enum se NORMALIZA a "otra" con contador visible — registro, no rechazo.
    # None = properties.tipo es texto libre (comportamiento dev).
    obligacion_tipo_enum: tuple | None = None
    # Valores retirados del vocabulario, contados APARTE al normalizarse
    # (vigilancia (5) del laudo de congelado: emisiones residuales = 0).
    obligacion_tipo_retirados: tuple = ()


@dataclass(frozen=True)
class PerfilE1:
    nombre: str
    prefijo_hash: str                       # para banner y diagnóstico
    prefijo_hash_para_namespace: str | None  # None = namespace histórico dev
    build_request_kwargs: Callable
    build_user_message: Callable
    rol_por_to: dict
    esquema: EsquemaValidacion | None       # None = defaults de validador/E2
    labels_catalogo: dict | None            # None = _labels_catalogo() de E2


_cache: dict[str, PerfilE1] = {}


def _labels_catalogo_v3(v3) -> dict[str, dict]:
    """id → {label, nivel} derivado mecánicamente de BLOQUE_CATALOGO_V3 (el
    bloque sellado): nivel por sufijo de línea ('[rol del TO' → rol,
    '[instancia]' → instancia, clase en otro caso), label sin el tramo de
    alias ni los sufijos. Mismo criterio de parsing que usa internamente el
    módulo sellado; assert de 102 entradas (regla i)."""
    out: dict[str, dict] = {}
    for linea in v3.BLOQUE_CATALOGO_V3.split("\n"):
        if not (linea.startswith("Sujeto_") and " — " in linea):
            continue
        sid, resto = linea.split(" — ", 1)
        if "[rol del TO" in resto:
            nivel = "rol"
        elif "[instancia]" in resto:
            nivel = "instancia"
        else:
            nivel = "clase"
        label = resto.split(" (alias", 1)[0]
        for sufijo in (" [instancia]",):
            label = label.replace(sufijo, "")
        i = label.find(" [rol del TO")
        if i != -1:
            label = label[:i]
        out[sid] = {"label": label.strip(), "nivel": nivel}
    if len(out) != 102:
        raise RuntimeError(
            f"labels del catálogo v3: {len(out)} entradas (esperadas 102) — se frena")
    return out


def _perfil_produccion_dev() -> PerfilE1:
    import prompt_e1  # noqa: PLC0415 — import diferido (ver docstring)

    return PerfilE1(
        nombre="produccion_dev",
        prefijo_hash=prompt_e1.PREFIJO_HASH,
        prefijo_hash_para_namespace=None,
        build_request_kwargs=prompt_e1.build_request_kwargs,
        build_user_message=prompt_e1.build_user_message,
        rol_por_to=prompt_e1.ROL_POR_TO,
        esquema=None,
        labels_catalogo=None,
    )


def _perfil_v3_b54() -> PerfilE1:
    if str(_B54_CODE) not in sys.path:
        sys.path.insert(0, str(_B54_CODE))
    import prompt_v3_b54 as v3       # noqa: PLC0415 — módulo SELLADO, solo import
    import prompt_congelado as pc    # noqa: PLC0415 — en path vía prompt_v3_b54

    # CANDADO (decisión 1): recomputo contra el sello, no confianza en el
    # módulo. Cualquier diferencia invalida la corrida que la contenga.
    if (v3.PREFIJO_SHA256_V3 != PREFIJO_SHA256_V3_ESPERADO
            or v3.PREFIJO_HASH_V3 != PREFIJO_HASH_V3_ESPERADO):
        raise RuntimeError(
            "candado v3: el prefijo integrado no reproduce el sello de U-B5.4 "
            f"(sha {v3.PREFIJO_SHA256_V3[:12]}… esperado "
            f"{PREFIJO_SHA256_V3_ESPERADO[:12]}…; hash {v3.PREFIJO_HASH_V3} "
            f"esperado {PREFIJO_HASH_V3_ESPERADO}) — se frena")

    esquema = EsquemaValidacion(
        entity_types=tuple(pc.ENTITY_TYPES_CONGELADO),
        predicates=tuple(pc.PREDICATES_CONGELADO),
        sujeto_predicates=tuple(pc.SUJETO_PREDICATES),
        sujetos_catalogo_set=frozenset(v3.SUJETOS_CATALOGO_V3),
        firma_valida=pc.firma_valida,
        obligacion_tipo_enum=tuple(pc.OBLIGACION_TIPO_CONGELADO),
        obligacion_tipo_retirados=("requisito_de_estructura",),
    )
    return PerfilE1(
        nombre="v3_b54",
        prefijo_hash=v3.PREFIJO_HASH_V3,
        prefijo_hash_para_namespace=v3.PREFIJO_HASH_V3,
        build_request_kwargs=v3.build_request_kwargs_v3,
        build_user_message=v3.build_user_message_v3,
        rol_por_to=v3.ROL_POR_TO_V3,
        esquema=esquema,
        labels_catalogo=_labels_catalogo_v3(v3),
    )


def perfil(nombre: str = PERFIL_DEFAULT) -> PerfilE1:
    """Devuelve el perfil por nombre (memoizado; construcción determinística).
    Nombre fuera del registro → ValueError (el loader de manifiesto lo
    traduce a ErrorManifiesto)."""
    if nombre not in PERFILES_CONOCIDOS:
        raise ValueError(
            f"perfil_e1 desconocido: {nombre!r} (conocidos: {PERFILES_CONOCIDOS})")
    if nombre not in _cache:
        _cache[nombre] = (_perfil_produccion_dev() if nombre == "produccion_dev"
                          else _perfil_v3_b54())
    return _cache[nombre]
