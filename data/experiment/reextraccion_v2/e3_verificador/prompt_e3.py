"""
prompt_e3.py — Prompt del verificador de completitud intra-unidad E3 (T1).

Diseño vinculante (docs/diseno_reextraccion_v2.md §3-E3):
  - CONTEXTO FRESCO: el verificador recibe SOLO datos — el texto fuente
    íntegro de la unidad (punto propio + herencia, de E0) y lo extraído de
    ella (de E1, post-validación, en formato legible). Jamás el contexto del
    extractor (principio 2.c). El selftest verifica que ninguna instrucción
    del prompt de E1 aparezca en el request de E3.
  - Blanco: AMPUTACIONES — el punto está presente pero despojado de
    calificadores, excepciones, ítems de enumeración o modalidad.
  - Feedback ESTRUCTURADO por faltante: tipo, cita textual del fuente no
    representada, ubicación, severidad.
  - Calibración con EJEMPLOS RESUELTOS del backlog (hallazgo H12: los jueces
    honran ejemplos y circunvalan reglas), construidos en calibradores_e3.py.
  - El verificador JAMÁS corrige: detecta y documenta. Corregir es del
    extractor (mini-ratchet, ratchet_e3.py) o del humano.

Estructura de caching (mismas 5 decisiones de docs/decisiones_caching_extraccion.md
que gobiernan E1): PREFIJO ESTABLE (instrucciones + contrato + calibradores)
como `system` en lista de bloques con cache_control ephemeral en el último
bloque; los tools (contrato estructurado) son estables y forman parte del
prefijo cacheado. TODO lo variable por unidad (fuente + extracción) va en el
mensaje de usuario, después del breakpoint. El prompt es función PURA de
(chunk, validación): mismos datos → mismo request byte a byte.
"""

from __future__ import annotations

import hashlib
import json

import comun_e3
from comun_e3 import fuente_integro, render_extraccion
import calibradores_e3

MAX_OUTPUT_TOKENS = 4096  # el veredicto es corto; techo holgado para faltantes múltiples

NOMBRE_TOOL = "verificar_completitud_e3"

TIPOS_FALTANTE = (
    "enumeracion_incompleta",
    "calificador_despojado",
    "excepcion_ausente",
    "modalidad_perdida",
    "contenido_tabular_no_declarado",
    "otro",
)

SEVERIDADES = ("alta", "media", "baja")


# ========================================================================== #
# PREFIJO DE SISTEMA (estable, cacheado) — parte 1: instrucciones            #
# ========================================================================== #

INSTRUCCIONES = """Sos un verificador de completitud para la construcción de un Knowledge Graph regulatorio del BCRA (Banco Central de la República Argentina). Trabajás con CONTEXTO FRESCO: no viste la conversación del extractor ni el resto del corpus. Recibís exactamente dos cosas, como datos: (1) el texto fuente ÍNTEGRO de una unidad estructural (el punto numerado de un Texto Ordenado más su contexto estructural heredado — encabezados, párrafos introductorios, intersticiales y de cierre de la jerarquía que lo contiene, cada bloque con su unidad de origen), y (2) los elementos que un extractor independiente extrajo de esa unidad (entidades con propiedades y relaciones, ya validados estructuralmente).

# TU TAREA

Identificar contenido NORMATIVO del texto fuente que NO está representado en lo extraído. Tu blanco son las AMPUTACIONES: el punto está presente pero llegó despojado de calificadores, excepciones, ítems de enumeración o modalidad. La evidencia del proyecto muestra que estas amputaciones sobreviven a extractores que tienen el texto completo a la vista: por eso existís vos, en contexto separado.

VOS JAMÁS CORREGÍS. No propongas la extracción arreglada, no redactes entidades, no completes descripciones. Detectás y documentás; corregir es trabajo del extractor (que recibirá tu feedback) o de revisión humana.

# QUÉ CUENTA COMO "REPRESENTADO"

Un contenido del fuente está representado si su sustancia normativa aparece en lo extraído: en la descripcion u otra property de alguna entidad, en el label, o expresado estructuralmente por una relación (p. ej. una salvedad capturada como nodo Excepcion conectado a su norma). NO se exige copia verbatim: una paráfrasis que conserva quién / qué / cuánto / cuándo / salvo qué / con qué modalidad es representación válida. La representación puede estar anclada al punto propio o a la unidad de origen del bloque heredado.

# TIPOS DE FALTANTE (exactamente estos 6)

1. `enumeracion_incompleta` — el fuente enumera ítems, categorías, incisos o renglones y lo extraído omite alguno, o omite la cláusula que ordena la enumeración.
2. `calificador_despojado` — una norma está extraída pero perdió un calificador que restringe o precisa su alcance: temporal ("informada en el mes n"), cuantitativo ("hasta el 10 %"), condicional ("siempre que...", "en la medida en que..."), o de sujeto ("cuando el sujeto obligado así lo disponga").
3. `excepcion_ausente` — una salvedad del fuente ("salvo", "excepto", "no aplicará cuando", "quedan excluidas") no aparece ni en descripciones ni como nodo Excepcion.
4. `modalidad_perdida` — la modalidad deóntica del fuente (deber / prohibición / facultad "podrá") quedó invertida o borrada en lo extraído.
5. `contenido_tabular_no_declarado` — la unidad contiene contenido tabular o fórmulas con sustancia normativa que NO fue extraído NI declarado por el extractor en sus omisiones no-prosa. Si el extractor declaró la omisión, NO es faltante: es el tratamiento correcto del contenido no-confiable.
6. `otro` — contenido normativo no representado que no encaja en 1-5 (p. ej. una norma entera de un párrafo heredado sin ningún elemento que la porte).

# QUÉ NO ES FALTANTE (no lo marques)

- Paráfrasis, reordenamientos o recortes de redacción que conservan la sustancia normativa.
- Labels cortos: el label es un nombre canónico de pocas palabras; el contenido vive en descripcion.
- Encabezados puros, títulos, numeración, referencias de índice: jerarquía documental, no contenido normativo.
- La elección de granularidad de sujetos, tipos de entidad o predicados: eso lo controla otra capa (validación de esquema). Vos verificás CONTENIDO, no modelado.
- Contenido tabular o fórmulas cuya omisión el extractor DECLARÓ en sus omisiones no-prosa.
- Contenido de otras unidades del documento que no está en el fuente que recibiste.
- Prosa no normativa: aclaraciones históricas, notas editoriales, remisiones puras ("ver punto 2.4.") sin mandato propio.

# SEVERIDAD

- `alta`: el faltante cambia una respuesta regulatoria — quién está alcanzado, qué está permitido/prohibido, un umbral, un plazo, una excepción, un ítem de enumeración normativa.
- `media`: precisión secundaria cuya ausencia degrada la respuesta sin invertirla (un calificador redundante con otro ya representado, un detalle de procedimiento).
- `baja`: matiz menor, redacción, contenido de dudosa sustancia normativa. Ante la duda entre marcar con severidad baja y no marcar, marcá con severidad baja: la decisión de re-extraer usa la lista completa.

# CONTRATO DE SALIDA

Llamá SIEMPRE a la herramienta `verificar_completitud_e3`:

- Si todo el contenido normativo del fuente está representado: `veredicto = "completo_ok"` y `faltantes = []`.
- Si no: `veredicto = "faltantes_detectados"` y un elemento en `faltantes` por cada omisión, con:
  - `tipo`: uno de los 6 tipos.
  - `cita_textual_del_fuente`: la cita VERBATIM del fuente no representada (copiala del texto fuente, guiones de corte de línea incluidos si los tiene; NUNCA la parafrasees — se verifica automáticamente contra el fuente y una cita que no aparece invalida el faltante). Citá la cláusula mínima autocontenida: el renglón, la salvedad o el ítem completo.
  - `ubicacion`: la unidad estructural donde vive la cita (el punto propio, o la unidad de origen del bloque heredado tal como figura en el fuente).
  - `severidad`: alta | media | baja.
  - `nota` (opcional): una línea sobre qué se perdió respecto de lo extraído.

Un faltante por omisión: si un mismo renglón perdió dos calificadores distintos, son dos faltantes con dos citas. No agrupes.
"""


# ========================================================================== #
# PREFIJO — parte 2: calibradores (ejemplos resueltos)                       #
# ========================================================================== #

def _render_calibrador(cal: dict) -> str:
    veredicto_json = json.dumps(cal["veredicto"], ensure_ascii=False, indent=1)
    return "\n".join([
        f"## {cal['id']} — {cal['titulo']}",
        "",
        "TEXTO FUENTE ÍNTEGRO DE LA UNIDAD:",
        "```",
        cal["fuente"],
        "```",
        "",
        "ELEMENTOS EXTRAÍDOS DE ESTA UNIDAD:",
        "```",
        render_extraccion(cal["extraccion"]),
        "```",
        "",
        f"VEREDICTO CORRECTO (input de `{NOMBRE_TOOL}`):",
        "```json",
        veredicto_json,
        "```",
        "",
        f"PORQUÉ: {cal['porque']}",
    ])


CALIBRADORES = calibradores_e3.construir_calibradores()

BLOQUE_CALIBRADORES = "\n".join(
    ["# EJEMPLOS RESUELTOS (calibran tu criterio; casos reales del proyecto)", ""]
    + [_render_calibrador(c) + "\n" for c in CALIBRADORES]
)

PREFIJO_SISTEMA = INSTRUCCIONES + "\n" + BLOQUE_CALIBRADORES


# ========================================================================== #
# TOOL SCHEMA (contrato estructurado — estable, parte del prefijo cacheado)  #
# ========================================================================== #

TOOL_SCHEMA_E3 = {
    "name": NOMBRE_TOOL,
    "description": (
        "Reporta el veredicto de completitud de la unidad: completo_ok, o la "
        "lista de faltantes (contenido normativo del fuente no representado en "
        "lo extraído), cada uno con tipo, cita textual verbatim del fuente, "
        "ubicación y severidad."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "veredicto": {
                "type": "string",
                "enum": ["completo_ok", "faltantes_detectados"],
                "description": "completo_ok exige faltantes = []; faltantes_detectados exige al menos un faltante.",
            },
            "faltantes": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "tipo": {"type": "string", "enum": list(TIPOS_FALTANTE)},
                        "cita_textual_del_fuente": {
                            "type": "string",
                            "description": "Cita VERBATIM del texto fuente no representada. Se verifica automáticamente contra el fuente: no parafrasear.",
                        },
                        "ubicacion": {
                            "type": "string",
                            "description": "Unidad estructural donde vive la cita (punto propio o unidad de origen del bloque heredado).",
                        },
                        "severidad": {"type": "string", "enum": list(SEVERIDADES)},
                        "nota": {
                            "type": "string",
                            "description": "Opcional: una línea sobre qué se perdió respecto de lo extraído.",
                        },
                    },
                    "required": ["tipo", "cita_textual_del_fuente", "ubicacion", "severidad"],
                    "additionalProperties": False,
                },
            },
        },
        "required": ["veredicto", "faltantes"],
        "additionalProperties": False,
    },
}


def bloques_sistema() -> list[dict]:
    """`system` como lista de bloques con el breakpoint de caching declarado
    en el ÚLTIMO bloque del prefijo estable (Decisión 1). Nada variable por
    unidad entra acá."""
    return [
        {
            "type": "text",
            "text": PREFIJO_SISTEMA,
            "cache_control": {"type": "ephemeral"},
        }
    ]


# Huella del prefijo completo (system + tools): identifica el contrato estable.
PREFIJO_CANONICO = json.dumps(
    {"system": bloques_sistema(), "tools": [TOOL_SCHEMA_E3]},
    sort_keys=True, ensure_ascii=False, separators=(",", ":"),
)
PREFIJO_HASH = hashlib.sha256(PREFIJO_CANONICO.encode("utf-8")).hexdigest()[:12]


# ========================================================================== #
# MENSAJE DE USUARIO (variable por unidad — después del breakpoint)          #
# ========================================================================== #

def build_user_message(chunk: dict, validacion: dict) -> str:
    """Único contenido variable del request: la unidad como DATOS. Función
    pura de (chunk, validación): mismos datos → mismo mensaje byte a byte."""
    partes: list[str] = []
    partes.append(f"Documento fuente: {chunk['archivo']}")
    partes.append(f"TO: {chunk['to']}")
    partes.append(f"Unidad bajo verificación: {chunk['unidad']} — {chunk['titulo']}")
    partes.append("")

    flags = chunk.get("flags") or {}
    if flags.get("contenido_tabular") or flags.get("formula"):
        tipos_flag = []
        if flags.get("contenido_tabular"):
            tipos_flag.append("contenido tabular")
        if flags.get("formula"):
            tipos_flag.append("fórmulas")
        partes.append(
            f"NOTA: esta unidad tiene {' y '.join(tipos_flag)} detectados "
            f"determinísticamente (flag de E0). El extractor tenía instrucción de "
            f"NO reconstruir ese contenido y declarar las omisiones. Evaluá el "
            f"tratamiento: contenido tabular/fórmula normativo ni extraído ni "
            f"declarado es faltante tipo contenido_tabular_no_declarado; declarado, no."
        )
        partes.append("")

    partes.append("TEXTO FUENTE ÍNTEGRO DE LA UNIDAD (contexto heredado + punto propio):")
    partes.append("```")
    partes.append(fuente_integro(chunk))
    partes.append("```")
    partes.append("")
    partes.append("ELEMENTOS EXTRAÍDOS DE ESTA UNIDAD (post-validación estructural):")
    partes.append("```")
    partes.append(render_extraccion(validacion))
    partes.append("```")
    partes.append("")
    partes.append(
        f"Verificá la completitud y reportá el veredicto con `{NOMBRE_TOOL}`. "
        "Recordá: citas VERBATIM del fuente, un faltante por omisión, jamás corregir."
    )
    return "\n".join(partes)


def build_request_kwargs(chunk: dict, validacion: dict, model: str,
                         max_tokens: int = MAX_OUTPUT_TOKENS) -> dict:
    """Request completo para client.messages.create(**kwargs). Prefijo estable
    idéntico entre unidades; lo variable, solo en messages. Base de la key de
    la caché local (llm_cache.canonical_request)."""
    return {
        "model": model,
        "max_tokens": max_tokens,
        # thinking NO autorizado (namespace think=0). En los modelos actuales
        # de la familia Sonnet el thinking adaptativo viene activado por
        # defecto al omitir el parámetro: se deshabilita EXPLÍCITAMENTE (los
        # tokens de thinking facturarían como output fuera de la estimación).
        "thinking": {"type": "disabled"},
        "system": bloques_sistema(),
        "tools": [TOOL_SCHEMA_E3],
        "tool_choice": {"type": "tool", "name": NOMBRE_TOOL},
        "messages": [{"role": "user", "content": build_user_message(chunk, validacion)}],
    }
