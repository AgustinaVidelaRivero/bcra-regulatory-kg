"""
generador.py — Generación de preguntas desde subgrafos muestreados (§2 y §5).

FASE A: estructura completa con el llamado LLM STUBBEADO. Ninguna función de
este módulo llama a una API. El cliente es inyectable (patrón del harness:
`GraphAgent(kg, client=...)`); producción inyectará un cliente real envuelto
en la caché del proyecto (llm_cache), el selftest inyecta `StubCliente` que
devuelve preguntas de fixture.

Por sample se generan DOS versiones (§5, diseño apareado):
  1. literal      — puede compartir vocabulario con los nodos del gold.
  2. anti-léxica  — reformulación sin los tokens del label ni los de alta
                    señal de la descripcion de los nodos respuesta.

Tokens prohibidos por sample (mecánica implementada acá, offline):
  - TODOS los tokens de contenido del label de cada nodo respuesta.
  - Tokens de "alta señal" de la descripcion: tokens de contenido cuya
    document-frequency en el grafo (sobre label+descripcion de todos los
    nodos) es <= DF_ALTA_SENAL — un token raro identifica al nodo; un token
    masivo ("entidades", "cambios") no discrimina y prohibirlo solo
    empobrecería la reformulación sin proteger nada.
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from comun import load_kg_raw, tokens_contenido

DF_ALTA_SENAL = 50   # df <= 50 sobre 4469 nodos ≈ token distintivo (~1 %)


# --------------------------------------------------------------------------- #
# Tokens prohibidos                                                            #
# --------------------------------------------------------------------------- #
class TokensProhibidos:
    """Calcula los tokens prohibidos de un sample para la evolución anti-léxica."""

    def __init__(self, kg_raw: dict | None = None):
        if kg_raw is None:
            kg_raw = load_kg_raw()
        self.df = Counter()
        for n in kg_raw["nodes"]:
            props = n.get("properties") or {}
            desc = props.get("descripcion") or props.get("description") or ""
            self.df.update(tokens_contenido(f"{n.get('label') or ''} {desc}"))

    def de_sample(self, sample: dict) -> set:
        respuesta_ids = set(sample["metadatos"]["debug_ids_respuesta"])
        prohibidos = set()
        for nodo in sample["subgrafo"]["nodos"]:
            if nodo["id"] not in respuesta_ids:
                continue
            prohibidos |= tokens_contenido(nodo.get("label") or "")
            for t in tokens_contenido(nodo.get("descripcion") or ""):
                if self.df[t] <= DF_ALTA_SENAL:
                    prohibidos.add(t)
        return prohibidos


# --------------------------------------------------------------------------- #
# Render del subgrafo para el prompt                                           #
# --------------------------------------------------------------------------- #
def _render_nodo(n: dict) -> str:
    partes = [f"- [{n['type']}] {n['label']}"]
    if n.get("descripcion"):
        partes.append(f"  descripcion: {n['descripcion']}")
    extra = n.get("properties_extra") or {}
    for k in sorted(extra):
        if k in ("tipo",):
            partes.append(f"  {k}: {extra[k]}")
    anclas = ", ".join(f"{a['to']}:{a['ancla']}" for a in n.get("anclas", []))
    if anclas:
        partes.append(f"  puntos normativos: {anclas}")
    return "\n".join(partes)


def render_subgrafo(sample: dict) -> str:
    lineas = ["NODOS:"]
    lineas += [_render_nodo(n) for n in sample["subgrafo"]["nodos"]]
    if sample["subgrafo"]["aristas"]:
        etiquetas = {n["id"]: n["label"] for n in sample["subgrafo"]["nodos"]}
        lineas.append("RELACIONES:")
        for a in sample["subgrafo"]["aristas"]:
            lineas.append(f"- ({etiquetas.get(a['source'], a['source'])}) "
                          f"--{a['relation']}--> "
                          f"({etiquetas.get(a['target'], a['target'])})")
    return "\n".join(lineas)


# --------------------------------------------------------------------------- #
# Prompts de generación por estrato                                            #
# --------------------------------------------------------------------------- #
_PREAMBULO = """\
Sos un generador de preguntas de evaluación sobre regulación del BCRA. Te doy \
un fragmento de un grafo de conocimiento regulatorio (nodos con label, \
descripción y punto normativo, y relaciones entre ellos). Tu tarea es redactar \
UNA pregunta en castellano cuya respuesta completa y correcta sea EXACTAMENTE \
la información de este fragmento — ni más, ni menos.

Reglas:
- La pregunta debe entenderse sola, sin ver el fragmento: nada de "este punto", \
"el nodo anterior", "según el fragmento".
- No menciones ids técnicos ni la palabra "grafo" o "nodo".
- No pidas información que el fragmento no contiene.
- Pregunta concreta de un usuario real (compliance, tesorería, auditoría), \
tono profesional.
- Respondé SOLO con un objeto JSON: {"pregunta": "..."}
"""

_INSTRUCCION_POR_ESTRATO = {
    "E-A": """\
El fragmento es una relación directa entre dos elementos normativos. Redactá la
pregunta de modo que, partiendo del elemento DADO, la respuesta sea el elemento
RESPUESTA y su relación con el dado (qué lo regula, limita, exceptúa, etc.).""",
    "E-B": """\
El fragmento es una cadena de elementos conectados. Redactá la pregunta de modo
que responderla exija recorrer la cadena completa desde el primer elemento
hasta el último: la respuesta correcta debe mencionar el elemento final y cómo
se llega a él desde el inicial (las estaciones intermedias son parte de la
respuesta).""",
    "E-C": """\
El fragmento es un elemento central (hub) y el conjunto de sus vecinos bajo una
misma relación. Redactá una pregunta de ENUMERACIÓN: la respuesta correcta debe
listar TODOS los miembros del conjunto, sin omitir ninguno. Incluí en la
pregunta el criterio que define al conjunto (la relación con el elemento
central), nunca la lista.""",
    "E-D": """\
El fragmento contiene dos cláusulas casi idénticas que difieren en un detalle
(un calificador, un plazo, un alcance). La pregunta debe apuntar SIN AMBIGÜEDAD
a la variante marcada como OBJETIVO: incluí en la pregunta el detalle que la
distingue de la otra, de modo que la otra variante NO sea una respuesta
correcta.""",
    "E-E": """\
El fragmento es un único elemento normativo. Redactá la pregunta cuya respuesta
sea el contenido de ese elemento (qué establece, a qué aplica, con qué alcance).""",
}


def prompt_generacion(sample: dict) -> str:
    estrato = sample["estrato"]
    partes = [_PREAMBULO, _INSTRUCCION_POR_ESTRATO[estrato], ""]
    ps = sample["metadatos"]["pregunta_sobre"]
    etiquetas = {n["id"]: n["label"] for n in sample["subgrafo"]["nodos"]}
    if estrato == "E-A":
        partes.append(f"DADO: {etiquetas.get(ps['dado'])}")
        partes.append(f"RESPUESTA: {etiquetas.get(ps['respuesta'])}")
    elif estrato == "E-B":
        partes.append(f"INICIO: {etiquetas.get(ps['dado'])}")
        partes.append(f"FINAL: {etiquetas.get(ps['respuesta'])}")
    elif estrato == "E-C":
        partes.append(f"ELEMENTO CENTRAL: {etiquetas.get(ps['hub'])}")
        partes.append(f"RELACIÓN DEL CONJUNTO: {ps['relacion']} "
                      f"({ps['n_miembros']} miembros)")
    elif estrato == "E-D":
        partes.append(f"OBJETIVO: {etiquetas.get(ps['objetivo'])}")
        partes.append(f"VARIANTE A DISTINGUIR: {etiquetas.get(ps['distractor'])}")
        partes.append(f"DETALLE QUE DIFIERE: {', '.join(ps['tokens_diferencia'])}")
    partes.append("")
    partes.append("FRAGMENTO:")
    partes.append(render_subgrafo(sample))
    return "\n".join(partes)


def prompt_evolucion_antilexica(sample: dict, pregunta_literal: str,
                                tokens_prohibidos: set) -> str:
    return f"""\
Sos un reformulador de preguntas de evaluación. Te doy una pregunta sobre
regulación del BCRA y una lista de PALABRAS PROHIBIDAS (la jerga con la que el
sistema evaluado indexó la respuesta). Reescribí la pregunta como la haría un
usuario que NO conoce esa jerga:

- MISMA pregunta de fondo: la respuesta correcta no debe cambiar.
- NO uses ninguna palabra prohibida ni sus variantes obvias (plural/singular,
  con/sin acento, misma raíz).
- Usá sinónimos, paráfrasis o descripciones funcionales.
- Mantené los datos que identifican el caso (montos, plazos, tipos de
  operación) expresados con otras palabras.
- Respondé SOLO con un objeto JSON: {{"pregunta": "..."}}

PREGUNTA ORIGINAL:
{pregunta_literal}

PALABRAS PROHIBIDAS:
{", ".join(sorted(tokens_prohibidos))}
"""


# --------------------------------------------------------------------------- #
# Cliente inyectable + stub                                                    #
# --------------------------------------------------------------------------- #
class ClienteLLM:
    """Interfaz mínima. Producción: implementación sobre la caché del proyecto
    (patrón llm_cache/CachingClient, ver skill llm-capture). Fase A: solo stub."""

    def generar(self, prompt: str) -> str:  # -> texto crudo del modelo
        raise NotImplementedError


class StubCliente(ClienteLLM):
    """Cliente offline para el selftest: respuestas de fixture.

    `fixtures` mapea una clave a la respuesta cruda; la clave se busca por
    substring en el prompt (los prompts reales incluyen el sample_id vía las
    labels; para el selftest la clave es un marcador inequívoco del fixture).
    Si ninguna clave matchea, devuelve `respuesta_defecto`.
    """

    def __init__(self, fixtures: dict[str, str] | None = None,
                 respuesta_defecto: str = '{"pregunta": "PREGUNTA-STUB"}'):
        self.fixtures = fixtures or {}
        self.respuesta_defecto = respuesta_defecto
        self.llamadas: list[str] = []   # registro para asserts del selftest

    def generar(self, prompt: str) -> str:
        self.llamadas.append(prompt)
        for clave, respuesta in self.fixtures.items():
            if clave in prompt:
                return respuesta
        return self.respuesta_defecto


def _parse_pregunta(crudo: str) -> str:
    """Extrae {"pregunta": ...} tolerando fences."""
    t = crudo.strip()
    if t.startswith("```"):
        t = t.strip("`")
        if t.lower().startswith("json"):
            t = t[4:]
    obj = json.loads(t.strip())
    p = obj.get("pregunta")
    if not isinstance(p, str) or not p.strip():
        raise ValueError(f"respuesta sin campo 'pregunta' válido: {crudo[:120]}")
    return p.strip()


class Generador:
    """Orquesta generación literal + evolución anti-léxica por sample."""

    def __init__(self, cliente: ClienteLLM, tokens: TokensProhibidos):
        self.cliente = cliente
        self.tokens = tokens

    def generar_par(self, sample: dict) -> dict:
        prohibidos = self.tokens.de_sample(sample)
        p_gen = prompt_generacion(sample)
        literal = _parse_pregunta(self.cliente.generar(p_gen))
        p_evo = prompt_evolucion_antilexica(sample, literal, prohibidos)
        antilexica = _parse_pregunta(self.cliente.generar(p_evo))
        return {
            "sample_id": sample["sample_id"],
            "literal": literal,
            "antilexica": antilexica,
            "tokens_prohibidos": sorted(prohibidos),
            "prompts": {"generacion": p_gen, "evolucion": p_evo},
        }
