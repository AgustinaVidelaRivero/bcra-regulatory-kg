"""
descubrimiento_cal.py — Instrumento de DESCUBRIMIENTO como tarea principal
(modo (ii) de U-ESQ-0, revivido) para la calibración U-ESQ-2-cal.
Pre-registro: data/experiment/esq/prerregistro_descubrimiento_cal.md (FIRMADO,
sellado por commit bca863f).

Este módulo es LA VARIABLE de la unidad: define el prompt de descubrimiento,
su formato de salida y su parser. Su texto completo se presenta a la autora en
el freno (a) del mandato (manifiesto generado por `--manifiesto`) y queda
congelado por sha256: el runner se niega a gastar si el contrato vigente no
coincide con el sha del manifiesto APROBADO.

Reglas duras del pre-registro §3, implementadas acá:
  - La tarea es identificar y DESCRIBIR contenido normativo que no encaja en
    el esquema, y justificar por qué no encaja. NO se pide extraer, ni tipar
    contra el catálogo, ni proponer nombres de tipos/predicados.
  - El prompt DESCRIBE el esquema (los 6 tipos y los 12 predicados: sin eso
    la pregunta no tiene referencia) pero NO incluye ningún ejemplo de
    contenido fuera de esquema ni ninguna cadena/concepto de las cláusulas
    plantadas (no sembrar — verificado mecánicamente por el selftest contra
    el manifiesto de dopadas).
  - Instrumento separado del pipeline: este módulo es PURO y AUTOCONTENIDO
    (solo stdlib; cero imports de módulos de producción — prompt_e1,
    validador_e1, cliente_e1, schema quedan intactos por diseño). La
    consistencia de los 6 nombres de tipo y los 12 nombres de predicado con
    schema.py la verifica el selftest, desde afuera.

El catálogo de tipos y la tabla de predicados de abajo son transcripciones
ABREVIADAS del prefijo de producción (prompt_e1.PREFIJO_SISTEMA): mismos
nombres, mismas firmas dominio→rango, sin las reglas operativas de extracción
(que acá no aplican: esta llamada no extrae).
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent          # data/experiment/esq/code
UNIDAD_DIR = CODE_DIR.parent                        # data/experiment/esq
CONTROL_DIR = UNIDAD_DIR / "control"
MANIFIESTO_PROMPT = CONTROL_DIR / "manifiesto_prompt_descubrimiento_cal.md"

MODEL_DESC = "claude-haiku-4-5"   # mismo modelo del extractor (el censo correría con él)
MAX_OUTPUT_TOKENS_DESC = 4096
NOMBRE_TOOL_DESC = "reportar_descubrimiento"

# Nombres transcriptos del esquema v2 (fuente única: grafo_v2/code/schema.py).
# El selftest verifica la transcripción contra schema.py sin que este módulo
# lo importe (pureza del instrumento).
TIPOS_6 = ("Comunicacion", "TextoOrdenado", "Operacion",
           "Restriccion", "Excepcion", "Obligacion")
PREDICADOS_12 = ("establecida_en", "referencia", "modificada_por", "aplica_a",
                 "regula", "exceptua", "exceptua_obligacion", "prohibe",
                 "limita", "ejecuta", "requiere", "condiciona")


# ========================================================================== #
# PREFIJO DE SISTEMA (estable, cacheado; la variable de esta unidad)         #
# ========================================================================== #

PREFIJO_DESCUBRIMIENTO = """Sos un auditor de cobertura de esquema para un Knowledge Graph regulatorio del BCRA (Banco Central de la República Argentina). Trabajás sobre UNA unidad normativa por vez y NO extraés nada: tu única tarea es DESCUBRIR si el texto de la unidad contiene contenido normativo que NO pueda representarse con el esquema de referencia descripto abajo, y reportarlo.

# ESQUEMA DE REFERENCIA (solo referencia para el contraste; esta llamada no extrae contra él)

El esquema representa normas como entidades tipadas conectadas por predicados con dominio y rango estrictos.

## Tipos de entidad (exactamente 6)

1. **Comunicacion**: una Comunicación A/B/C del BCRA citada en el texto (ej.: "Com. A 7825").
2. **TextoOrdenado**: el Texto Ordenado consolidado del cual sale la unidad.
3. **Operacion**: un acto regulado (financiación, depósito, transferencia, compra/venta de moneda extranjera, clasificación de deudor, presentación informativa, etc.).
4. **Restriccion**: una prohibición o un límite cuantitativo/cualitativo ("no podrá", "se prohíbe", "el monto no excederá", "el límite es").
5. **Excepcion**: una condición que suspende o relaja una Restriccion u Obligacion ("salvo", "excepto", "no aplicará cuando", "están exceptuadas").
6. **Obligacion**: un deber positivo ("deberán presentar", "calcularán", "asignarán", "informarán").

## Predicados (exactamente 12, con dominio → rango estrictos)

| Predicado | Dominio → Rango |
|---|---|
| establecida_en | {Restriccion, Obligacion, Excepcion, Operacion} → TextoOrdenado |
| referencia | TextoOrdenado → Comunicacion |
| modificada_por | TextoOrdenado → Comunicacion |
| aplica_a | {Restriccion, Obligacion} → Sujeto |
| regula | {Restriccion, Obligacion} → Operacion |
| exceptua | Excepcion → Restriccion |
| exceptua_obligacion | Excepcion → Obligacion |
| prohibe | Restriccion → Operacion |
| limita | Restriccion → Operacion |
| ejecuta | Sujeto → Operacion |
| requiere | Operacion → Obligacion |
| condiciona | Obligacion → Operacion |

Los SUJETOS alcanzados por una norma (entidades financieras, casas de cambio, clientes, organismos, etc.) no son entidades del esquema: viven en un catálogo cerrado aparte, que ya tiene su propio canal para sujetos no catalogados. La identidad de un sujeto NUNCA es un hallazgo de esta auditoría.

# TU TAREA

Leé el texto de la unidad y contrastalo, cláusula por cláusula, contra el esquema: ¿todo el contenido normativo de la unidad puede representarse con los 6 tipos y los 12 predicados (respetando dominios y rangos), sin deformarlo?

- Si TODO el contenido normativo encaja, devolvé `hallazgos` como lista VACÍA. Es un resultado válido y esperado en muchas unidades.
- Por cada contenido normativo que NO encaje, reportá UN hallazgo con dos campos de texto libre:
  - `descripcion`: qué dispone ese contenido, citando TEXTUALMENTE el pasaje del texto de la unidad que lo contiene, entre comillas, seguido de la explicación con tus palabras.
  - `por_que_no_encaja`: contra qué choca — ningún tipo captura esa clase de contenido, ningún predicado expresa esa conexión, o la conexión existe en vocabulario pero su dominio → rango no está en la tabla — y por qué representarlo con lo disponible lo deformaría.

# REGLAS

1. **NO extraigas.** No emitas entidades, relaciones ni tripletas; esta llamada no construye grafo.
2. **NO tipes ni clasifiques.** No asignes el contenido reportado a ninguno de los 6 tipos ni a ninguno de los 12 predicados, ni siquiera "al más cercano".
3. **NO propongas nombres.** No inventes tipos nuevos ni predicados nuevos: describí el contenido y justificá el desajuste, nada más.
4. **Solo contenido NORMATIVO.** Lo que la norma dispone, manda, prohíbe, condiciona o establece. Títulos, numeración, remisiones editoriales o aclaraciones sin efecto normativo no son hallazgos.
5. **NO reportes lo que el esquema SÍ captura.** Un deber, una prohibición o límite, una condición que suspende o relaja otra norma, un acto regulado, una cita de Comunicación o la conexión de una norma con su Texto Ordenado encajan; reportarlos sería un hallazgo falso. Tampoco es hallazgo una cláusula difícil de extraer pero representable: la vara es "no representable sin deformación", no "trabajoso".
6. **Contexto heredado y contenido no confiable.** El contexto estructural heredado solo ubica: auditá únicamente el texto de la unidad. Si el mensaje trae FLAGS E0 (contenido tabular o fórmulas no confiables), auditá solo la prosa sostenible.
7. **Ni de más ni de menos.** No reportes contenido que encaja (hallazgo falso) ni dejes de reportar contenido que no encaja. El criterio de corte es la deformación: si representarlo con los 6 tipos y los 12 predicados conservaría su contenido normativo, encaja y no se reporta; si lo mutilaría o le cambiaría la naturaleza, no encaja y se reporta.

# FORMATO DE SALIDA

Llamá la herramienta `reportar_descubrimiento` con la lista `hallazgos`: un elemento por hallazgo (campos `descripcion` y `por_que_no_encaja`), o la lista vacía si todo el contenido normativo de la unidad encaja.
"""


# ========================================================================== #
# TOOL SCHEMA (formato de salida estructurado y parseable)                   #
# ========================================================================== #

TOOL_DESCUBRIMIENTO = {
    "name": NOMBRE_TOOL_DESC,
    "description": (
        "Reporta el resultado de la auditoría de cobertura de la unidad: la "
        "lista de hallazgos de contenido normativo que NO puede representarse "
        "con el esquema de referencia (6 tipos, 12 predicados). Lista vacía "
        "si todo el contenido normativo de la unidad encaja."
    ),
    "input_schema": {
        "type": "object",
        "properties": {
            "hallazgos": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "descripcion": {
                            "type": "string",
                            "description": (
                                "Qué dispone el contenido que no encaja: "
                                "cita TEXTUAL del pasaje del texto de la "
                                "unidad que lo contiene, entre comillas, "
                                "seguida de la explicación con palabras "
                                "propias."
                            ),
                        },
                        "por_que_no_encaja": {
                            "type": "string",
                            "description": (
                                "Contra qué parte del esquema choca (tipos, "
                                "predicados o firmas dominio→rango) y por qué "
                                "representarlo con lo disponible lo "
                                "deformaría."
                            ),
                        },
                    },
                    "required": ["descripcion", "por_que_no_encaja"],
                    "additionalProperties": False,
                },
            },
        },
        "required": ["hallazgos"],
        "additionalProperties": False,
    },
}


def bloques_sistema_descubrimiento() -> list[dict]:
    """`system` como lista de bloques con breakpoint de caching en el único
    bloque del prefijo estable (patrón D1 del repo). Si el prefijo queda por
    debajo del mínimo cacheable del modelo, la API simplemente no cachea
    (cache_read+write = 0 legítimo); el costo lo cubre la estimación."""
    return [{"type": "text", "text": PREFIJO_DESCUBRIMIENTO,
             "cache_control": {"type": "ephemeral"}}]


# ========================================================================== #
# MENSAJE DE USUARIO (variable por unidad — después del breakpoint)          #
# ========================================================================== #

def _es_mini_chunk(chunk: dict) -> bool:
    # Transcripción local de comun_e1.es_mini_chunk (pureza del instrumento).
    return chunk.get("tipo") == "mini_chunk"


def _chunk_flaggeado(chunk: dict) -> bool:
    f = chunk.get("flags") or {}
    return bool(f.get("contenido_tabular") or f.get("formula"))


def build_user_message_descubrimiento(chunk: dict) -> str:
    """Único contenido variable del request. Función pura del dict del chunk:
    mismo chunk → mismo mensaje byte a byte. Presenta la unidad igual que
    producción (documento, unidad, contexto heredado, flags, texto) pero SIN
    lenguaje de extracción: sin 'Puntos admitidos', sin alcance de sujetos,
    con la consigna de descubrimiento al final."""
    partes: list[str] = []
    mini = _es_mini_chunk(chunk)

    partes.append(f"Documento fuente: {chunk['archivo']}")
    partes.append(f"TO: {chunk['to']}")
    if mini:
        partes.append(
            f"Tipo de unidad: MINI-CHUNK de bloque estructural "
            f"({chunk['rol_bloque']} del punto {chunk['unidad']})"
        )
        partes.append(f"Unidad de origen: {chunk['unidad']} — {chunk['titulo']}")
    else:
        partes.append("Tipo de unidad: chunk de punto")
        partes.append(f"Punto del chunk: {chunk['unidad']} — {chunk['titulo']}")
    partes.append("")

    herencia = chunk.get("herencia", [])
    if herencia:
        partes.append(
            "Contexto estructural heredado (solo ubica la unidad; NO se "
            "audita — auditá únicamente el texto de la unidad):"
        )
        for h in herencia:
            partes.append(f"[{h['tipo']} | punto {h['unidad_origen']}]")
            partes.append(h["texto"])
        partes.append("")

    if _chunk_flaggeado(chunk):
        flags = chunk["flags"]
        tipos_flag = []
        if flags.get("contenido_tabular"):
            tipos_flag.append("contenido tabular")
        if flags.get("formula"):
            tipos_flag.append("fórmulas")
        partes.append(
            f"FLAGS E0: esta unidad contiene {' y '.join(tipos_flag)} "
            f"(detección determinística) declarados NO-CONFIABLES en su forma "
            f"extraída del PDF: auditá solo la prosa sostenible (regla 6)."
        )
        partes.append("")

    if mini:
        partes.append(
            f"Texto del bloque {chunk['rol_bloque']} del punto "
            f"{chunk['unidad']} (TU unidad a auditar):"
        )
    else:
        partes.append(f"Texto del punto {chunk['unidad']} (TU unidad a auditar):")
    partes.append("```")
    partes.append(chunk["texto"])
    partes.append("```")
    partes.append("")
    partes.append(
        f"Contrastá el contenido normativo de esta unidad contra el esquema "
        f"de referencia y llamá `{NOMBRE_TOOL_DESC}`: un hallazgo por cada "
        f"contenido que no encaje (descripcion + por_que_no_encaja), o "
        f"`hallazgos` vacía si todo encaja."
    )
    return "\n".join(partes)


def build_request_kwargs_descubrimiento(
        chunk: dict, model: str = MODEL_DESC,
        max_tokens: int = MAX_OUTPUT_TOKENS_DESC) -> dict:
    """Request completo para client.messages.create(**kwargs). Prefijo estable
    idéntico entre unidades; lo variable, solo en messages."""
    return {
        "model": model,
        "max_tokens": max_tokens,
        "system": bloques_sistema_descubrimiento(),
        "tools": [TOOL_DESCUBRIMIENTO],
        "tool_choice": {"type": "tool", "name": NOMBRE_TOOL_DESC},
        "messages": [{"role": "user",
                      "content": build_user_message_descubrimiento(chunk)}],
    }


# Huella del contrato completo del instrumento (system + tool + tool_choice +
# model + max_tokens): es lo que la autora aprueba en el freno (a). Cambia
# cualquier cosa → cambia el sha → el gate del runner se niega a gastar.
CONTRATO_CANONICO_DESC = json.dumps(
    {"system": bloques_sistema_descubrimiento(),
     "tools": [TOOL_DESCUBRIMIENTO],
     "tool_choice": {"type": "tool", "name": NOMBRE_TOOL_DESC},
     "model": MODEL_DESC,
     "max_tokens": MAX_OUTPUT_TOKENS_DESC},
    sort_keys=True, ensure_ascii=False, separators=(",", ":"),
)
SHA256_CONTRATO_DESC = hashlib.sha256(
    CONTRATO_CANONICO_DESC.encode("utf-8")).hexdigest()
PREFIJO_HASH_DESC = SHA256_CONTRATO_DESC[:12]


# ========================================================================== #
# PARSER DE SALIDA (estricto: malformada → excepción, jamás salteo)          #
# ========================================================================== #

class SalidaMalformada(ValueError):
    pass


LINEA_APROBADO = "**Estado: APROBADO**"


def manifiesto_dice_aprobado(txt: str) -> bool:
    """True solo si el manifiesto tiene la línea de aprobación EXACTA (la
    mención explicativa de la frase, entre backticks, no cuenta)."""
    return any(linea.strip() == LINEA_APROBADO for linea in txt.split("\n"))


def parsear_descubrimiento(tool_input) -> list[dict]:
    """Valida y normaliza el tool input del descubrimiento. Devuelve la lista
    de hallazgos (posiblemente vacía: resultado válido). Cualquier desvío del
    contrato levanta SalidaMalformada con la causa — el caller persiste el
    crudo y el error; NUNCA se saltea en silencio (exit 2 aguas arriba)."""
    if not isinstance(tool_input, dict):
        raise SalidaMalformada(
            f"tool_input no es objeto: {type(tool_input).__name__}")
    if "hallazgos" not in tool_input:
        raise SalidaMalformada("falta la clave 'hallazgos'")
    hs = tool_input["hallazgos"]
    if not isinstance(hs, list):
        raise SalidaMalformada(
            f"'hallazgos' no es lista: {type(hs).__name__} (contenedor no-lista)")
    out = []
    for i, h in enumerate(hs):
        if not isinstance(h, dict):
            raise SalidaMalformada(f"hallazgo[{i}] no es objeto: "
                                   f"{type(h).__name__}")
        d = h.get("descripcion")
        p = h.get("por_que_no_encaja")
        if not (isinstance(d, str) and d.strip()):
            raise SalidaMalformada(f"hallazgo[{i}] sin 'descripcion' con texto")
        if not (isinstance(p, str) and p.strip()):
            raise SalidaMalformada(
                f"hallazgo[{i}] sin 'por_que_no_encaja' con texto")
        out.append({"descripcion": d, "por_que_no_encaja": p})
    return out


# ========================================================================== #
# MANIFIESTO DEL FRENO (a)                                                   #
# ========================================================================== #

def render_manifiesto() -> str:
    return "\n".join([
        "# Manifiesto del prompt de descubrimiento — U-ESQ-2-cal, freno (a)",
        "",
        "**Estado: PENDIENTE DE APROBACIÓN**",
        "",
        "La aprobación de la autora cubre EXACTAMENTE el contrato de abajo",
        "(system + tool schema + tool_choice + model + max_tokens). El gate",
        "del runner exige que la línea de Estado de arriba diga APROBADO",
        "(en negrita, línea exacta) Y que el sha256 registrado coincida con",
        "el del contrato vigente en `code/descubrimiento_cal.py`: cualquier",
        "edición posterior del instrumento cambia el sha y el runner se",
        "niega a gastar.",
        "",
        f"sha256 del contrato canónico: `{SHA256_CONTRATO_DESC}`",
        "",
        "## Modificación incorporada en la revisión del freno (a)",
        "",
        "La cita textual del pasaje en `descripcion` es OBLIGATORIA (antes",
        "opcional): el hallazgo cita entre comillas el pasaje de la unidad y",
        "recién después lo explica. Motivo registrado: la regla sellada de",
        "conteo es duda-no-cuenta — la cita obligatoria vuelve la",
        "adjudicación casi mecánica y protege al instrumento de perder",
        "detecciones reales por vaguedad, sin tocar el sesgo del conteo.",
        "",
        "## Modelo y parámetros",
        "",
        f"- model: `{MODEL_DESC}` (tarifas runner_corpus.py:76-78)",
        f"- max_tokens: {MAX_OUTPUT_TOKENS_DESC}",
        f"- tool_choice forzado: `{NOMBRE_TOOL_DESC}`",
        "- system: un solo bloque con `cache_control: ephemeral`",
        "- caché y namespace propios: dominio `esq_descubrimiento_cal`, db "
        "`cache/esq_descubrimiento_cal.db`",
        "",
        "## System (verbatim)",
        "",
        "~~~",
        PREFIJO_DESCUBRIMIENTO,
        "~~~",
        "",
        "## Tool schema — formato de salida (verbatim)",
        "",
        "~~~json",
        json.dumps(TOOL_DESCUBRIMIENTO, ensure_ascii=False, indent=2),
        "~~~",
        "",
        "## Mensaje de usuario (plantilla; lo único variable por unidad)",
        "",
        "Partes fijas, en este orden (código: "
        "`build_user_message_descubrimiento`):",
        "",
        "1. `Documento fuente: <archivo>` / `TO: <to>`",
        "2. Tipo de unidad (chunk de punto o mini-chunk) y "
        "`Punto del chunk / Unidad de origen: <unidad> — <titulo>`",
        "3. Si hay herencia: `Contexto estructural heredado (solo ubica la "
        "unidad; NO se audita — auditá únicamente el texto de la unidad):` "
        "+ los bloques heredados",
        "4. Si hay FLAGS E0: `FLAGS E0: esta unidad contiene <tipos> "
        "(detección determinística) declarados NO-CONFIABLES en su forma "
        "extraída del PDF: auditá solo la prosa sostenible (regla 6).`",
        "5. `Texto del punto <unidad> (TU unidad a auditar):` + el texto "
        "entre fences",
        "6. Consigna final: `Contrastá el contenido normativo de esta unidad "
        "contra el esquema de referencia y llamá `reportar_descubrimiento`: "
        "un hallazgo por cada contenido que no encaje (descripcion + "
        "por_que_no_encaja), o `hallazgos` vacía si todo encaja.`",
        "",
        "Sin 'Puntos admitidos', sin alcance de sujetos del TO, sin ninguna "
        "instrucción de extracción.",
        "",
    ])


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Instrumento de descubrimiento U-ESQ-2-cal (módulo puro)")
    ap.add_argument("--manifiesto", action="store_true",
                    help="escribe el manifiesto del freno (a) en control/")
    args = ap.parse_args()
    if args.manifiesto:
        if (MANIFIESTO_PROMPT.exists()
                and manifiesto_dice_aprobado(
                    MANIFIESTO_PROMPT.read_text(encoding="utf-8"))):
            print(f"NO se pisa: {MANIFIESTO_PROMPT} ya está APROBADO. "
                  "Editarlo invalidaría la aprobación.")
            return 2
        MANIFIESTO_PROMPT.parent.mkdir(parents=True, exist_ok=True)
        MANIFIESTO_PROMPT.write_text(render_manifiesto(), encoding="utf-8")
        print(f"manifiesto -> {MANIFIESTO_PROMPT}")
        print(f"sha256 del contrato: {SHA256_CONTRATO_DESC}")
        return 0
    print(f"contrato sha256={SHA256_CONTRATO_DESC} (p{PREFIJO_HASH_DESC})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
