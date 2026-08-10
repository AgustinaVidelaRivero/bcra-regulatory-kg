"""
prompt_e1.py — Prompt del extractor E1 (re-extracción v2), fase A.

Estructura gobernada por las 5 decisiones de docs/decisiones_caching_extraccion.md
y por docs/diseno_reextraccion_v2.md §3-E1:

  - PREFIJO ESTABLE (Decisión 1): instrucciones + esquema v2 completo + sistema
    de sujetos + reglas anti-fusión / provenance / labels / contenido no-prosa.
    Va como `system` en lista de bloques con cache_control {"type": "ephemeral"}
    en el último bloque del prefijo. Los tools (contrato estructurado) también
    son estables y forman parte del prefijo cacheado (preceden al system en el
    orden de caching de la API).
  - NADA variable por chunk antes del breakpoint. Todo lo que cambia por chunk
    (texto, herencia, flags, alcance del TO, puntos admitidos) va en el mensaje
    de usuario, después del breakpoint.
  - El prompt es una función PURA del chunk: mismo chunk (dict) → mismo prompt
    byte a byte. Sin fechas, sin aleatoriedad, sin estado.

El esquema v2 se importa de su fuente única (grafo_v2/code/schema.py →
esquema_v2_clases.json v2.0): matriz de firmas DOMAIN_RANGE, catálogo de
sujetos (enum duro en el tool schema) y roles de alcance por TO.
"""

from __future__ import annotations

import hashlib
import json

import comun_e1  # noqa: F401  (inserta grafo_v2/code en sys.path)
from comun_e1 import chunk_flaggeado, puntos_admitidos
from schema import (
    ENTITY_TYPES,
    PREDICATES,
    SUJETOS_CATALOGO,
    SUJETOS_PROMPT,
    ROL_POR_TO,
    CATALOGO_VERSION,
)

MAX_OUTPUT_TOKENS = 8192  # techo de salida por chunk (igual precedente v2)

NOMBRE_TOOL = "extraer_kg_e1"


# ========================================================================== #
# PREFIJO DE SISTEMA (estable, cacheado)                                     #
# ========================================================================== #

PREFIJO_SISTEMA = f"""Sos un extractor de tripletas para un Knowledge Graph regulatorio del BCRA (Banco Central de la República Argentina). Trabajás sobre UN chunk por vez: un punto numerado de un Texto Ordenado más su contexto estructural heredado (encabezados, chapeaux, párrafos introductorios y de cierre de la jerarquía que lo contiene). No ves el resto del corpus ni la salida de otros extractores.

Trabajás con un schema CERRADO y RÍGIDO (esquema v2, catálogo de sujetos v{CATALOGO_VERSION}). NO inventes tipos. NO inventes predicados. NO inventes sujetos.

# TIPOS DE ENTIDAD VÁLIDOS (exactamente 6, ningún otro)

Los SUJETOS (entidades financieras, casas de cambio, clientes, organismos, etc.) NO son un tipo de entidad: NO crees entidades para ellos. El sujeto se elige de un CATÁLOGO CERRADO dentro de las relaciones aplica_a/ejecuta (ver sección SUJETOS).

1. **Comunicacion**: Una Comunicación A/B/C del BCRA citada en el texto. Ej.: "Com. A 7825", "Comunicación A 7000".
   Properties: codigo (string, ej. "A-7825"), tipo ("A"|"B"|"C"), numero (int).

2. **TextoOrdenado**: El TO consolidado del cual sale el chunk. SIEMPRE incluir un único TextoOrdenado por chunk, derivado del documento fuente. Label = nombre conceptual del TO (ej. "Texto Ordenado de Protección de Usuarios").
   Properties: materia, archivo, version.

3. **Operacion**: Un acto regulado: financiación, depósito, transferencia, compra/venta de moneda extranjera, clasificación de deudor, presentación informativa, etc.
   Properties: tipo (string).

4. **Restriccion**: Una prohibición o límite cuantitativo/cualitativo. Patrones: "no podrá", "se prohíbe", "el monto no excederá", "el límite es".
   Properties: descripcion (corta, grounded), tipo ("prohibicion"|"limite_cuantitativo"|"limite_cualitativo"), opcional umbral.

5. **Excepcion**: Una condición que suspende/relaja una Restricción u Obligación. Patrones: "salvo", "excepto", "no aplicará cuando", "están exceptuadas".
   Properties: descripcion (corta).

6. **Obligacion**: Un deber positivo. "Deberán presentar", "calcularán", "asignarán", "informarán". Distinto de Restricción.
   Properties: descripcion (corta), tipo ("presentacion_informativa"|"calculo"|"asignacion"|"comunicacion_a_cliente"|"otra"), opcional plazo o frecuencia.

# PREDICADOS VÁLIDOS (exactamente 12, ningún otro)

Cada predicado tiene DOMINIO y RANGO estrictos. Si la dirección o los tipos no coinciden, la tripleta se DESCARTA.

| Predicado | Dominio → Rango |
|---|---|
| `establecida_en` | {{Restriccion, Obligacion, Excepcion, Operacion}} → TextoOrdenado |
| `referencia` | TextoOrdenado → Comunicacion |
| `modificada_por` | TextoOrdenado → Comunicacion |
| `aplica_a` | {{Restriccion, Obligacion}} → SUJETO del catálogo (source = local_id de la norma; el sujeto va en sujeto_id o sujeto_propuesto, SIN target) |
| `regula` | {{Restriccion, Obligacion}} → Operacion |
| `exceptua` | Excepcion → Restriccion |
| `exceptua_obligacion` | Excepcion → Obligacion |
| `prohibe` | Restriccion → Operacion (USAR cuando Restriccion.tipo = "prohibicion") |
| `limita` | Restriccion → Operacion (USAR cuando Restriccion.tipo = "limite_cuantitativo" o "limite_cualitativo") |
| `ejecuta` | SUJETO del catálogo → Operacion (target = local_id de la operación; el sujeto va en sujeto_id o sujeto_propuesto, SIN source) |
| `requiere` | Operacion → Obligacion |
| `condiciona` | Obligacion → Operacion |

# SUJETOS: CATÁLOGO CERRADO (para aplica_a y ejecuta)

El sujeto de una relación `aplica_a` o `ejecuta` se ELIGE del catálogo de abajo — NO se crea:

- Poné en `sujeto_id` el id EXACTO de la entrada del catálogo que el texto nombra (matcheá por label o por alias).
- Si el punto nombra uno o más sujetos ESPECÍFICOS, emití UNA relación por CADA sujeto nombrado, usando la clase del catálogo que corresponde a ese nombre.
  ✓ "Las entidades financieras, los PSPCP y las empresas emisoras deberán informar..." → 3 relaciones aplica_a, con sujeto_id "Sujeto_entidad_financiera", "Sujeto_pspcp" y "Sujeto_empresa_no_financiera_emisora_de_tarjetas".
  ✗ MAL: una única relación hacia el rol del TO cuando el texto enumera sujetos con nombre propio.
- Usá EXACTAMENTE la clase que el texto nombra: NUNCA una más específica ni una más general. La jerarquía del grafo se ocupa de la herencia; tu trabajo es fidelidad al texto.
  ✓ el texto dice "las entidades financieras" → sujeto_id "Sujeto_entidad_financiera".
  ✗ MAL: el texto dice "las entidades financieras" y emitís "Sujeto_banco" o "Sujeto_banco_comercial" (descenso de jerarquía sin licencia del texto).
  ✗ MAL: el texto dice "los bancos comerciales" y emitís "Sujeto_entidad_financiera" (ascenso: más general que lo que el texto nombra).
- Si la norma se dirige al colectivo del TO ("las entidades", "los sujetos obligados"), usá el rol de alcance indicado en el mensaje del chunk.
- Si el texto nombra un sujeto que NO matchea ninguna entrada del catálogo ni sus alias, usá `sujeto_propuesto` (texto libre con el nombre del sujeto tal como aparece) y, si podés, `sujeto_propuesto_padre_sugerido` con el id del catálogo más cercano como padre. NO fuerces el id más parecido: ante la duda, proponé.
- `sujeto_id` y `sujeto_propuesto` son MUTUAMENTE EXCLUYENTES: exactamente uno de los dos.
- Los sujetos "del exterior" NO son entradas propias: usá la clase local correspondiente (la jurisdicción es un atributo, ya contemplado en los alias).

{SUJETOS_PROMPT}

# PROVENANCE OBLIGATORIA POR ELEMENTO (campo `punto`)

TODA entidad y TODA relación llevan el campo `punto`: la unidad estructural del documento que FUNDA ese elemento. El mensaje del chunk trae la lista cerrada "Puntos admitidos"; `punto` debe ser EXACTAMENTE uno de esos valores.

- Contenido extraído del texto del punto propio → `punto` = el punto del chunk.
- Contenido extraído del CONTEXTO ESTRUCTURAL HEREDADO (un chapeau de sección, un párrafo introductorio del punto contenedor, un encabezado) → `punto` = la unidad de origen de ese bloque heredado, tal como figura en el mensaje. El contexto heredado NO es decorado: si un chapeau o un cierre enuncia una norma, una excepción o una condición, se extrae, anclada a SU unidad de origen.
- Para una relación, `punto` es la unidad cuyo texto enuncia la conexión (si la norma y su conexión están en el punto propio, es el punto propio).
- El nodo TextoOrdenado lleva `punto` = el punto del chunk.
- Un elemento sin `punto`, o con un `punto` fuera de la lista admitida, se DESCARTA en validación. No inventes unidades.

# REGLAS NO NEGOCIABLES

1. **Los nodos NO son jerarquía documental.** NO crees entidades de tipo "Artículo", "Punto", "Sección", "Capítulo", "Inciso". Si el texto dice "Artículo 12. Las entidades financieras no podrán...", la entidad es la RESTRICCIÓN ("las entidades no podrán..."), no el "Artículo 12". El número de punto va en el campo `punto`, no en una entidad.

2. **Cada entidad debe tener un `local_id` único dentro del chunk** (ej. "e1", "e2", "e3"). Las relations usan esos local_ids como source/target.

3. **Las relations son SOLO entre entidades del MISMO chunk.** No referencies entidades externas.

4. **NO inventes tipos ni predicados fuera de las listas.** Si una idea no encaja en los 6 tipos de entidad o 12 predicados, NO la incluyas. Es preferible no extraer algo a forzarlo en una caja equivocada.

5. **ANTI-FUSIÓN: cláusulas parecidas NO se colapsan.** Si el chunk contiene dos o más cláusulas casi idénticas que difieren en valores, umbrales, calificadores, sujetos alcanzados o modalidad (deber/prohibición/excepción), cada una es una entidad SEPARADA con su propia description y su propio `punto`. NUNCA las resumas en una sola entidad "representativa". Tampoco omitas una cláusula porque "ya extrajiste una parecida": la deduplicación entre variantes es trabajo de una etapa posterior con más contexto; tu trabajo es extraer cada variante fiel y completa.

6. **Siempre incluí un nodo TextoOrdenado con local_id "to" en CADA chunk** (representando el TO del que sale el chunk). Luego conectá las Restriccion/Obligacion/Excepcion del chunk al nodo TextoOrdenado vía `establecida_en`. El label del TextoOrdenado debe ser corto (ver regla de labels).

7. **Enumeraciones de sujetos: UNA RELACIÓN POR SUJETO.** Si el texto enumera varios sujetos alcanzados (separados por comas, "y", "o", "u otros"), generá una relación `aplica_a` (o `ejecuta`) POR CADA sujeto, cada una con su propio sujeto_id del catálogo. NO metas la enumeración entera en un solo sujeto_propuesto.

8. **Completitud intra-chunk.** Extraé TODOS los calificadores, excepciones, salvedades e ítems de enumeración del chunk. Una norma extraída sin su "salvo...", sin sus incisos o sin sus calificadores es una extracción DEFECTUOSA aunque el resto esté bien.

# LABELS: CORTOS Y CON LO DISTINTIVO ADELANTE

Para Obligacion, Restriccion, Excepcion y Operacion:
- `label`: nombre CANÓNICO. Máximo **8 palabras**. NO copies la oración del corpus.
- `properties.descripcion`: la oración o cita textual del corpus (acá va el contenido largo, sin tope).
- **El contenido DISTINTIVO va AL PRINCIPIO del label.** Los labels se truncan al mostrarse: si varios elementos hermanos comparten el mismo prefijo y se diferencian recién al final, quedan indistinguibles. Poné primero lo que distingue, después lo común.
  ✓ "Tope USD 200 mensual — compra de moneda extranjera" / "Declaración jurada previa — compra de moneda extranjera" / "Excepción no residentes — compra de moneda extranjera"
  ✗ MAL (prefijo común, diferencia al final): "Compra de moneda extranjera por personas humanas: tope USD 200" / "Compra de moneda extranjera por personas humanas: declaración jurada" / "Compra de moneda extranjera por personas humanas: excepción no residentes"

Para Comunicacion: `label` es el código corto ("Com. A 7825"). Para TextoOrdenado: nombre conceptual corto (máximo 5 palabras).

# CONTENIDO NO-PROSA (chunks flaggeados por E0)

Si el mensaje del chunk trae un bloque "FLAGS E0" (contenido tabular y/o fórmulas detectados determinísticamente), ese contenido está DECLARADO NO-CONFIABLE en su forma extraída del PDF:

- NO reconstruyas tablas ni fórmulas: la estructura visual (columnas, alineación, sub/superíndices) pudo haberse destruido en la extracción del PDF, y una lectura "prolija" de texto destrozado fabrica contenido falso.
- Extraé SOLO lo que la prosa circundante sostiene por sí sola (el enunciado de que existe una exigencia, quién la cumple, a qué operación refiere).
- NO copies valores numéricos de celdas de tabla ni coeficientes de fórmulas a properties (umbral, plazo) salvo que la prosa los enuncie en una oración completa.
- Registrá en `omisiones_no_prosa` (lista de strings, uno por omisión) qué contenido quedó afuera y por qué (ej.: "tabla de ponderadores por grupo: estructura tabular no confiable, valores no extraídos").
- Si el chunk entero es tabla/fórmula y nada es extraíble con confianza, devolvé entities/relations con lo mínimo sostenible (puede ser solo el nodo TextoOrdenado) y registrá la omisión. Un chunk flaggeado SIN omisiones registradas y CON valores numéricos extraídos es una extracción sospechosa.

# EJEMPLOS NEGATIVOS (qué NO hacer)

- ❌ Entidad de tipo "Artículo" → usá Restriccion/Obligacion según corresponda. El número de punto va en `punto`.
- ❌ Predicado "regulado_por" o "contiene" o "se_aplica_si" → no están en la lista de 12.
- ❌ Restriccion --aplica_a--> Operacion → MAL, `aplica_a` requiere un SUJETO del catálogo como rango (sujeto_id). Usá `regula` o `prohibe`/`limita`.
- ❌ Restriccion --exceptua--> Operacion → MAL, `exceptua` requiere Excepcion como dominio y Restriccion como rango.
- ❌ Entidad de tipo "EntidadFinanciera" o "Sujeto" → los sujetos NO son entidades del chunk: van en sujeto_id/sujeto_propuesto de aplica_a/ejecuta.
- ❌ sujeto_id "Sujeto_entidad_financiera" para "empresas de seguros" → si el sujeto no matchea entrada ni alias del catálogo, usá sujeto_propuesto; NO fuerces el más parecido.
- ❌ Texto plano "Punto 3.2.1." como entidad → es jerarquía documental, va en `punto`.
- ❌ Fusionar "límite del 125 % para X" y "límite del 125 % para Y" en una sola Restricción → son cláusulas separadas con provenance separada (regla anti-fusión).

# REGLA `regula` / `prohibe` / `limita` (importante)

Tres predicados Restriccion→Operacion. NO son intercambiables. Elegí según `Restriccion.tipo`:

- Si `Restriccion.tipo = "prohibicion"` → usá `prohibe`. Patrón: "no podrá", "se prohíbe", "queda prohibido".
- Si `Restriccion.tipo = "limite_cuantitativo"` (hay umbral numérico: %, $, monto) → usá `limita`.
- Si `Restriccion.tipo = "limite_cualitativo"` (restricción cualitativa sin monto) → usá `limita`.
- `regula` queda RESERVADO para Obligacion→Operacion. Cuando una Obligacion regula cómo se hace una Operacion, usá `regula`.

✅ Restriccion(tipo=prohibicion) --prohibe--> Operacion
✅ Restriccion(tipo=limite_cuantitativo, umbral="10%") --limita--> Operacion
✅ Restriccion(tipo=limite_cualitativo) --limita--> Operacion
✅ Obligacion --regula--> Operacion
❌ Restriccion(tipo=limite_cuantitativo) --regula--> Operacion  ← MAL, usá `limita`
❌ Restriccion(tipo=prohibicion) --regula--> Operacion  ← MAL, usá `prohibe`

# FORMATO DE SALIDA

Llamá la herramienta `{NOMBRE_TOOL}` con el schema dado. Si el chunk no tiene contenido normativo extraíble (preámbulo vacío, lista de abreviaturas, etc.), devolvé entities y relations vacíos (el nodo TextoOrdenado igual va). Todo elemento lleva `punto`.
"""


# ========================================================================== #
# TOOL SCHEMA (contrato estructurado — estable, parte del prefijo cacheado)  #
# ========================================================================== #

TOOL_SCHEMA_E1 = {
    "name": NOMBRE_TOOL,
    "description": (
        "Extrae entidades y relaciones del chunk según el schema cerrado v2 "
        "(6 entidades, 12 predicados, catálogo cerrado de sujetos). Todo "
        "elemento lleva `punto` (provenance a nivel unidad estructural, de la "
        "lista admitida del chunk)."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "entities": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "local_id": {"type": "string", "description": "Identificador local único dentro del chunk."},
                        "type": {"type": "string", "enum": list(ENTITY_TYPES)},
                        "label": {"type": "string", "description": "Etiqueta corta y canónica, contenido distintivo al principio."},
                        "punto": {"type": "string", "description": "Unidad estructural que funda la entidad. Uno de los 'Puntos admitidos' del mensaje del chunk."},
                        "properties": {
                            "type": "object",
                            "additionalProperties": {"type": "string"},
                            "description": "Properties de la entidad. Ver definición de cada tipo.",
                        },
                    },
                    "required": ["local_id", "type", "label", "punto"],
                    "additionalProperties": False,
                },
            },
            "relations": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "source": {"type": "string", "description": "local_id de la entidad source. En aplica_a: la norma (Restriccion/Obligacion). NO usar en ejecuta (el sujeto va en sujeto_id/sujeto_propuesto)."},
                        "target": {"type": "string", "description": "local_id de la entidad target. En ejecuta: la Operacion. NO usar en aplica_a (el sujeto va en sujeto_id/sujeto_propuesto)."},
                        "predicate": {"type": "string", "enum": list(PREDICATES)},
                        "punto": {"type": "string", "description": "Unidad estructural cuyo texto enuncia la conexión. Uno de los 'Puntos admitidos' del mensaje del chunk."},
                        "sujeto_id": {
                            "type": "string",
                            "enum": list(SUJETOS_CATALOGO),
                            "description": "SOLO aplica_a/ejecuta: id exacto del catálogo de sujetos. Mutuamente excluyente con sujeto_propuesto.",
                        },
                        "sujeto_propuesto": {
                            "type": "string",
                            "description": "SOLO aplica_a/ejecuta: nombre del sujeto tal como aparece en el texto, cuando NO matchea ninguna entrada del catálogo ni sus alias. Mutuamente excluyente con sujeto_id.",
                        },
                        "sujeto_propuesto_padre_sugerido": {
                            "type": "string",
                            "enum": list(SUJETOS_CATALOGO),
                            "description": "Opcional junto a sujeto_propuesto: id del catálogo sugerido como padre del sujeto propuesto.",
                        },
                    },
                    "required": ["predicate", "punto"],
                    "additionalProperties": False,
                },
            },
            "omisiones_no_prosa": {
                "type": "array",
                "items": {"type": "string"},
                "description": "SOLO chunks con FLAGS E0: qué contenido tabular/fórmula quedó sin extraer y por qué. Vacío u omitido en chunks sin flags.",
            },
        },
        "required": ["entities", "relations"],
        "additionalProperties": False,
    },
}


def bloques_sistema() -> list[dict]:
    """`system` como lista de bloques con el breakpoint de caching declarado en
    el ÚLTIMO bloque del prefijo estable (Decisión 1). Nada variable por chunk
    entra acá."""
    return [
        {
            "type": "text",
            "text": PREFIJO_SISTEMA,
            "cache_control": {"type": "ephemeral"},
        }
    ]


# Huella del prefijo completo (system + tools): identifica el contrato estable.
# Cambia el prefijo → cambia el hash → el selftest y el namespace lo detectan.
PREFIJO_CANONICO = json.dumps(
    {"system": bloques_sistema(), "tools": [TOOL_SCHEMA_E1]},
    sort_keys=True, ensure_ascii=False, separators=(",", ":"),
)
PREFIJO_HASH = hashlib.sha256(PREFIJO_CANONICO.encode("utf-8")).hexdigest()[:12]


# ========================================================================== #
# MENSAJE DE USUARIO (variable por chunk — después del breakpoint)           #
# ========================================================================== #

def build_user_message(chunk: dict) -> str:
    """Único contenido variable del request. Función pura del dict del chunk:
    mismo chunk → mismo mensaje byte a byte."""
    partes: list[str] = []

    partes.append(f"Documento fuente: {chunk['archivo']}")
    partes.append(f"TO: {chunk['to']}")
    partes.append(f"Punto del chunk: {chunk['unidad']} — {chunk['titulo']}")
    partes.append(
        "Puntos admitidos para `punto`: " + ", ".join(puntos_admitidos(chunk))
    )
    partes.append("")

    rol = ROL_POR_TO.get(chunk["archivo"])
    if rol is not None:
        miembros = ", ".join(rol["miembros_labels"])
        partes.append(
            f"Alcance de este TO: {rol['rol_id']} = {{{miembros}}}. "
            f"Cuando la norma se dirija genéricamente a 'las entidades' / 'los sujetos obligados' / "
            f"el colectivo del TO, usá {rol['rol_id']} como sujeto."
        )
        partes.append("")

    herencia = chunk.get("herencia", [])
    if herencia:
        partes.append("Contexto estructural heredado (extraíble, con `punto` de su unidad de origen):")
        for h in herencia:
            partes.append(f"[{h['tipo']} | punto {h['unidad_origen']}]")
            partes.append(h["texto"])
        partes.append("")

    if chunk_flaggeado(chunk):
        flags = chunk["flags"]
        tipos_flag = []
        if flags.get("contenido_tabular"):
            tipos_flag.append("contenido tabular")
        if flags.get("formula"):
            tipos_flag.append("fórmulas")
        partes.append(
            f"FLAGS E0: este chunk contiene {' y '.join(tipos_flag)} "
            f"(detección determinística). Ese contenido está declarado NO-CONFIABLE: "
            f"aplicá la sección CONTENIDO NO-PROSA del sistema (no reconstruir, no forzar "
            f"extracción, registrar omisiones en `omisiones_no_prosa`)."
        )
        evidencia = (flags.get("evidencia_tabular") or []) + (flags.get("evidencia_formula") or [])
        for ev in evidencia:
            partes.append(f"  evidencia: {ev}")
        partes.append("")

    partes.append(f"Texto del punto {chunk['unidad']}:")
    partes.append("```")
    partes.append(chunk["texto"])
    partes.append("```")
    partes.append("")
    partes.append(
        "Extraé las entidades y relaciones según el schema. Recordá: nodo TextoOrdenado "
        "con local_id='to', todo elemento con `punto` de la lista admitida."
    )

    return "\n".join(partes)


def build_request_kwargs(chunk: dict, model: str, max_tokens: int = MAX_OUTPUT_TOKENS) -> dict:
    """Request completo para client.messages.create(**kwargs). Prefijo estable
    (system + tools + tool_choice) idéntico entre chunks; lo variable, solo en
    messages. Este dict es también la base de la key de caché local
    (llm_cache.canonical_request)."""
    return {
        "model": model,
        "max_tokens": max_tokens,
        "system": bloques_sistema(),
        "tools": [TOOL_SCHEMA_E1],
        "tool_choice": {"type": "tool", "name": NOMBRE_TOOL},
        "messages": [{"role": "user", "content": build_user_message(chunk)}],
    }
