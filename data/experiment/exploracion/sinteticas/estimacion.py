"""
estimacion.py — Estimación de tokens y costo de la FASE B (T7). Código puro:
mide los prompts REALES de este pipeline sobre los samples ya muestreados; no
llama a ninguna API y NO fija precios — la fórmula queda parametrizada en
precio-por-Mtok y se resuelve en la autorización.

Supuestos explícitos (cada uno impreso en la tabla):

  S1. RATIO chars→tokens: medido con el único par (texto, tokens) conocido y
      estable del proyecto: el prefijo system+tools del harness ≈ 1.433 tokens
      (documentado en harness._apply_cache_breakpoint). ratio =
      chars(SYSTEM_PROMPT + tools JSON) / 1433. Es castellano técnico del
      mismo dominio que estos prompts.
  S2. OUTPUT de generación/evolución: una pregunta JSON de ~400 chars
      (largo típico del rango aceptado por la puerta b) => 400/ratio tokens.
  S3. OUTPUT de validación LLM: veredicto JSON corto ~200 chars.
  S4. FACTOR DE DESCARTE: precedente U6 = 39 generadas / 25 aptas = 1,56.
      Se aplica 1,6 sobre generación+evolución (los descartes también pagan
      su validación, que se estima sobre el volumen bruto).
  S5. La pregunta literal dentro del prompt de evolución se representa con un
      placeholder de 400 chars (en fase B es la salida real del paso 1).

Validaciones LLM marcadas necesarias por el validador (flags `requiere_llm`):
  V1. b_comprensibilidad_sin_contexto — por PREGUNTA (literal y anti-léxica).
  V2. a_unicidad_semantica_de_la_pregunta — por SAMPLE (sobre la literal;
      la anti-léxica hereda el gold).
  V3. d_misma_resolucion_semantica — por PAR (que la anti-léxica siga
      resolviendo al mismo gold).
  (a_unicidad_nodal_dentro_del_punto NO se paga: quedó documentada como no
   decidible a esta granularidad de ancla; no es un check por caso.)

Uso:  python3 estimacion.py   (lee out/samples.json; escribe out/estimacion.json)
"""

from __future__ import annotations

import json
from pathlib import Path

from comun import load_kg_raw
from generador import (TokensProhibidos, prompt_evolucion_antilexica,
                       prompt_generacion)
from harness import SYSTEM_PROMPT, TOOLS

AQUI = Path(__file__).resolve().parent

PLACEHOLDER_LITERAL = "x" * 400        # S5
OUT_CHARS_PREGUNTA = 400               # S2
OUT_CHARS_VEREDICTO = 200              # S3
FACTOR_DESCARTE = 1.6                  # S4
TOKENS_HARNESS_PREFIJO = 1433          # S1 (harness._apply_cache_breakpoint)


def ratio_chars_por_token() -> float:
    chars = len(SYSTEM_PROMPT) + len(json.dumps(TOOLS, ensure_ascii=False))
    return chars / TOKENS_HARNESS_PREFIJO


def _prompt_validacion_comprensibilidad(pregunta: str) -> str:
    """Check V1 de fase B — recalibrado por laudo de calibración: aclaración de
    contexto (dominio normativo fijo) + TRES ejemplos resueltos, en lugar de la
    regla declarativa (que exigía nombrar el marco normativo y descartó 10/10
    en la calibración inicial)."""
    return f"""\
Sos un revisor de preguntas de evaluación para un sistema cuyo dominio \
normativo es FIJO: el corpus regulatorio del BCRA (toda pregunta se responde \
contra esa normativa; el sistema ya lo sabe). AUTO-CONTENIDA significa: el \
caso se identifica sin ambigüedad por su propio contenido y no hay \
referencias colgantes al material con el que se generó la pregunta. NO exige \
nombrar el marco normativo, el Texto Ordenado ni la comunicación — ese \
contexto es fijo del sistema.

Ejemplos resueltos:

1. "En el marco del cálculo de exposición de contraparte mediante metodología \
de aforos, ¿qué restricción aplica respecto de los contratos que contienen \
cláusulas de abandono o ruptura (walkaway clauses) al momento de determinar \
la exigencia de capital?"
   -> {{"autocontenida": true, "motivo": "el caso queda identificado por su \
contenido técnico; no necesita citar la norma"}}

2. "En un caso de siniestro, ¿qué declaración jurada debe exigir la entidad y \
quién debe firmarla?"
   -> {{"autocontenida": true, "motivo": "pregunta corta con caso \
identificado; el dominio fijo repone el resto"}}

3. "¿Qué establece el punto anterior sobre capitales?"
   -> {{"autocontenida": false, "motivo": "referencia colgante: 'el punto \
anterior' no existe para quien lee la pregunta sola"}}

Indicá si la siguiente pregunta es auto-contenida bajo ese criterio.
Respondé SOLO JSON: {{"autocontenida": true|false, "motivo": "..."}}

PREGUNTA:
{pregunta}
"""


def _prompt_validacion_unicidad(pregunta: str, subgrafo_render: str) -> str:
    """Borrador fase B del check V2."""
    return f"""\
Sos un revisor de claves de evaluación. Te doy una pregunta y el fragmento
normativo que se declara como su respuesta (el gold). Indicá si la pregunta
admite OTRA respuesta igual de válida que no sea este fragmento (si es así,
la clave no es unívoca). Respondé SOLO JSON:
{{"gold_unico": true|false, "respuesta_alternativa": "..."}}

PREGUNTA:
{pregunta}

GOLD DECLARADO:
{subgrafo_render}
"""


def _prompt_validacion_mismo_gold(literal: str, antilexica: str) -> str:
    """Borrador fase B del check V3."""
    return f"""\
Te doy dos formulaciones de una pregunta de evaluación. Indicá si preguntan
EXACTAMENTE lo mismo (misma respuesta correcta), o si la reformulación cambió
el objeto de la pregunta. Respondé SOLO JSON:
{{"misma_pregunta": true|false, "diferencia": "..."}}

FORMULACIÓN ORIGINAL:
{literal}

REFORMULACIÓN:
{antilexica}
"""


def estimar(samples_path: Path = AQUI / "out" / "samples.json") -> dict:
    with open(samples_path, encoding="utf-8") as f:
        data = json.load(f)
    samples = data["samples"]
    n = len(samples)
    ratio = ratio_chars_por_token()
    tp = TokensProhibidos(load_kg_raw())

    def tok(chars: float) -> float:
        return chars / ratio

    # --- prompts reales, medidos sample por sample ---
    chars_gen, chars_evo, chars_v1, chars_v2 = [], [], [], []
    from generador import render_subgrafo
    for s in samples:
        prohibidos = tp.de_sample(s)
        pg = prompt_generacion(s)
        pe = prompt_evolucion_antilexica(s, PLACEHOLDER_LITERAL, prohibidos)
        chars_gen.append(len(pg))
        chars_evo.append(len(pe))
        chars_v1.append(len(_prompt_validacion_comprensibilidad(
            PLACEHOLDER_LITERAL)))
        chars_v2.append(len(_prompt_validacion_unicidad(
            PLACEHOLDER_LITERAL, render_subgrafo(s))))
    chars_v3 = len(_prompt_validacion_mismo_gold(PLACEHOLDER_LITERAL,
                                                 PLACEHOLDER_LITERAL))

    def linea(nombre, n_calls, chars_in_prom, chars_out):
        tin = tok(chars_in_prom) * n_calls
        tout = tok(chars_out) * n_calls
        return {"item": nombre, "n_llamadas": round(n_calls, 1),
                "tokens_in_por_llamada": round(tok(chars_in_prom)),
                "tokens_out_por_llamada": round(tok(chars_out)),
                "tokens_in_total": round(tin),
                "tokens_out_total": round(tout)}

    prom = lambda xs: sum(xs) / len(xs)
    bruto = n * FACTOR_DESCARTE           # volumen generado incl. descartes (S4)
    lineas = [
        linea("generacion_literal", bruto, prom(chars_gen), OUT_CHARS_PREGUNTA),
        linea("evolucion_antilexica", bruto, prom(chars_evo), OUT_CHARS_PREGUNTA),
        linea("V1_autocontencion (x2 preguntas)", 2 * bruto, prom(chars_v1),
              OUT_CHARS_VEREDICTO),
        linea("V2_unicidad_gold (x1 sample)", bruto, prom(chars_v2),
              OUT_CHARS_VEREDICTO),
        linea("V3_mismo_gold (x1 par)", bruto, chars_v3, OUT_CHARS_VEREDICTO),
    ]
    tin = sum(l["tokens_in_total"] for l in lineas)
    tout = sum(l["tokens_out_total"] for l in lineas)
    return {
        "supuestos": {
            "S1_ratio_chars_por_token": round(ratio, 3),
            "S1_base": f"{len(SYSTEM_PROMPT) + len(json.dumps(TOOLS, ensure_ascii=False))} chars "
                       f"/ {TOKENS_HARNESS_PREFIJO} tok (prefijo harness)",
            "S2_chars_out_pregunta": OUT_CHARS_PREGUNTA,
            "S3_chars_out_veredicto": OUT_CHARS_VEREDICTO,
            "S4_factor_descarte": FACTOR_DESCARTE,
            "S4_base": "precedente U6: 39 generadas / 25 aptas = 1,56",
            "S5_placeholder_literal_chars": len(PLACEHOLDER_LITERAL),
            "n_samples_base": n,
        },
        "lineas": lineas,
        "totales": {
            "tokens_in": tin,
            "tokens_out": tout,
            "formula_costo_usd":
                f"costo = {tin}/1e6 * P_in + {tout}/1e6 * P_out   "
                "(P_in, P_out = precio USD por Mtok del modelo que se laude; "
                "sin caching — los prompts no comparten prefijo largo)",
        },
    }


def main():
    res = estimar()
    out = AQUI / "out" / "estimacion.json"
    with out.open("w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1)
    print(json.dumps(res["supuestos"], ensure_ascii=False, indent=1))
    print(f"{'item':40s} {'calls':>7s} {'in/call':>8s} {'out/call':>8s} "
          f"{'in_tot':>9s} {'out_tot':>9s}")
    for l in res["lineas"]:
        print(f"{l['item']:40s} {l['n_llamadas']:>7} "
              f"{l['tokens_in_por_llamada']:>8} {l['tokens_out_por_llamada']:>8} "
              f"{l['tokens_in_total']:>9} {l['tokens_out_total']:>9}")
    print(res["totales"]["formula_costo_usd"])
    print(f"-> {out}")


if __name__ == "__main__":
    main()
