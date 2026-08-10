"""
validador.py — Puertas de calidad (§6 del diseño). Todo descarte con motivo.

Cuatro puertas sobre cada pregunta generada:

  (a) RESOLUCIÓN UNÍVOCA — qué es verificable mecánicamente y qué no:
      Mecánico:
        - el gold resuelve a >=1 nodo del grafo (censo por ancla, sin
          contenedores) — si no resuelve, DESCARTE;
        - cada ancla resuelve a UNA unidad del mapa de territorio (la ancla
          como punto normativo es unívoca por construcción del parser);
        - alcanzabilidad: todo nodo del censo entra al índice léxico de
          buscar_nodos (el harness indexa label+id y el id nunca es vacío),
          y se reporta si algún nodo gold está aislado (grado 0).
      Diagnóstico SIN descarte: tamaño del censo por ancla. Medido sobre el
      grafo vigente, la granularidad de ancla es GRUESA (mediana 29 nodos por
      ancla tras excluir contenedores; cap:3.1 -> 212): la unicidad A NIVEL
      NODO no es decidible mecánicamente con esta granularidad de location, y
      un umbral duro descartaría ~83 % de los golds por un artefacto de
      extracción. Por eso la métrica primaria agrega POR ANCLA (metrica.py) y
      acá solo se reporta `censo_grande` (> CENSO_DIAGNOSTICO nodos).
      NO mecánico (queda flaggeado `requiere_llm`):
        - que la PREGUNTA no admita otro gold igual de válido (juicio
          semántico sobre el texto de la pregunta contra el resto del grafo);
        - unicidad a nivel nodo dentro del punto normativo (ver arriba).

  (b) AUTO-CONTENCIÓN — heurísticas mecánicas:
        - deícticos y referencias colgantes ("el punto anterior", "dicho
          inciso", "este fragmento", ...);
        - fugas de la mecánica de generación ("nodo", "grafo", "subgrafo",
          "fragmento", ids técnicos con guiones bajos o sufijos hex);
        - forma de pregunta (termina en '?') y largo en [LARGO_MIN, LARGO_MAX].
      NO mecánico (flag `requiere_llm`): comprensibilidad real sin contexto.

  (c) EXCLUSIÓN DE MATERIAL QUEMADO — cruce de TODAS las anclas del sample
      contra el mapa de 5 sets (regla laudada de validar_anclas.py, incluida
      la regla de parciales: descarte si el ancla abarca un subpunto quemado).
      El sampler ya la aplicó; la puerta la re-verifica porque el validador
      debe poder correr sobre cualquier entrada, no solo la de este sampler.

  (d) ANTI-LÉXICAS — mecánico:
        - solape léxico (métrica de comun.solape_lexico) <= SOLAPE_UMBRAL;
        - mismo gold: el gold declarado del par es EL MISMO objeto del sample
          (invariante por construcción en este pipeline — la evolución no
          declara gold propio). Lo NO mecánico (flag `requiere_llm`): que la
          reformulación siga RESOLVIENDO a ese gold (que el cambio de
          vocabulario no haya corrido la pregunta a otra respuesta).

SOLAPE_UMBRAL = 0.15: a lo sumo ~1 de cada 7 tokens de contenido de la
pregunta puede pertenecer al vocabulario del gold. No es 0 porque hay términos
inevitables del dominio (p. ej. el token del TO: "cambios", "deudores") cuya
prohibición total haría las preguntas artificiales; el selftest muestra la
métrica con ejemplos por encima y por debajo del umbral.
"""

from __future__ import annotations

import re

from comun import Quemado, solape_lexico
from resolucion import AnclaIndex

CENSO_DIAGNOSTICO = 50   # censo por ancla mayor a esto se reporta (no descarta)
LARGO_MIN, LARGO_MAX = 40, 600
SOLAPE_UMBRAL = 0.15

# Deícticos / referencias colgantes (puerta b). Sobre texto en minúsculas.
_DEICTICOS = [
    r"\bel punto anterior\b", r"\bel punto mencionado\b", r"\bdicho punto\b",
    r"\bdicha norma\b", r"\bdicho inciso\b", r"\beste punto\b",
    r"\beste texto\b", r"\bel texto anterior\b", r"\blo anterior\b",
    r"\bantes mencionad", r"\barriba mencionad", r"\bya citad",
    r"\bel siguiente punto\b", r"\bcomo se indic[oó]\b",
    r"\bseg[uú]n (?:el|lo) (?:fragmento|contexto|extracto)\b",
]
# Fugas de la mecánica de generación (puerta b).
_FUGAS = [
    r"\bnodos?\b", r"\bgrafos?\b", r"\bsubgrafos?\b", r"\bfragmentos?\b",
    r"\baristas?\b", r"\bel elemento dado\b", r"\bla respuesta es\b",
    r"[a-z]+_[a-z]+_[a-z0-9_]+",      # ids técnicos con guiones bajos
    r"\b[0-9a-f]{6}\b",               # sufijos hex de ids del grafo
]


class Validador:
    def __init__(self, ancla_index: AnclaIndex, quemado: Quemado):
        self.idx = ancla_index
        self.quemado = quemado

    # ------------------ puerta (a) ------------------ #
    def puerta_a(self, sample: dict) -> dict:
        anclas = sample["gold"]["anclas"]
        censo = self.idx.censo(anclas)
        motivos, flags = [], []
        if not censo["nodos_gold"]:
            motivos.append("a_gold_no_resuelve: ninguna ancla del gold "
                           "resuelve a un nodo del grafo (sin contenedores)")
        for a in anclas:
            _, _, unidad = self.quemado.evaluar(a["to"], a["ancla"])
            if unidad is None:
                motivos.append(f"a_ancla_sin_unidad: {a['to']}:{a['ancla']} "
                               "no resuelve a una unidad del mapa")
        censo_grande = {f"{k[0]}:{k[1]}": len(ids)
                        for k, ids in censo["resueltas"].items()
                        if len(ids) > CENSO_DIAGNOSTICO}
        flags += ["a_unicidad_semantica_de_la_pregunta",
                  "a_unicidad_nodal_dentro_del_punto"]  # no mecánicos
        return {"puerta": "a", "ok": not motivos, "motivos": motivos,
                "requiere_llm": flags,
                "censo": {"nodos_gold": censo["nodos_gold"],
                          "anclas_ausentes": [list(k) for k in censo["ausentes"]],
                          "censo_grande_diagnostico": censo_grande}}

    # ------------------ puerta (b) ------------------ #
    def puerta_b(self, pregunta: str) -> dict:
        motivos = []
        p = (pregunta or "").strip()
        bajo = p.lower()
        for rx in _DEICTICOS:
            if re.search(rx, bajo):
                motivos.append(f"b_deictico: /{rx}/")
        for rx in _FUGAS:
            if re.search(rx, bajo):
                motivos.append(f"b_fuga_generacion: /{rx}/")
        if "?" not in p:
            motivos.append("b_sin_interrogacion")
        if not (LARGO_MIN <= len(p) <= LARGO_MAX):
            motivos.append(f"b_largo_fuera_de_rango: {len(p)} chars "
                           f"(rango [{LARGO_MIN}, {LARGO_MAX}])")
        return {"puerta": "b", "ok": not motivos, "motivos": motivos,
                "requiere_llm": ["b_comprensibilidad_sin_contexto"]}

    # ------------------ puerta (c) ------------------ #
    def puerta_c(self, sample: dict) -> dict:
        anclas = [{"to": a["to"], "ancla": a["ancla"]}
                  for n in sample["subgrafo"]["nodos"] for a in n["anclas"]]
        ok, detalle = self.quemado.todas_aptas(anclas)
        motivos = [] if ok else [
            "c_quemado: " + "; ".join(
                f"{d['to']}:{d['ancla']} {d['motivo']}"
                for d in detalle if d["veredicto"] == "descartado")]
        return {"puerta": "c", "ok": ok, "motivos": motivos, "requiere_llm": []}

    # ------------------ puerta (d) ------------------ #
    def puerta_d(self, antilexica: str, tokens_prohibidos: set,
                 gold_sample: dict, gold_declarado: dict | None = None) -> dict:
        motivos = []
        sol = solape_lexico(antilexica, tokens_prohibidos)
        if sol["solape"] > SOLAPE_UMBRAL:
            motivos.append(
                f"d_solape_alto: {sol['solape']:.3f} > {SOLAPE_UMBRAL} "
                f"(tokens en común: {', '.join(sol['tokens_en_comun'])})")
        # mismo gold — parte mecánica: si la evolución declara gold propio,
        # debe ser idéntico al del sample (en este pipeline no declara: hereda).
        if gold_declarado is not None and gold_declarado != gold_sample:
            motivos.append("d_gold_distinto: la evolución declara un gold "
                           "que no es el del sample")
        return {"puerta": "d", "ok": not motivos, "motivos": motivos,
                "requiere_llm": ["d_misma_resolucion_semantica"],
                "solape": sol}

    # ------------------ pipeline completo ------------------ #
    def validar(self, sample: dict, pregunta_literal: str,
                pregunta_antilexica: str | None = None,
                tokens_prohibidos: set | None = None) -> dict:
        """Valida un sample + su(s) pregunta(s). Veredicto global + detalle."""
        puertas = [self.puerta_a(sample),
                   self.puerta_b(pregunta_literal),
                   self.puerta_c(sample)]
        if pregunta_antilexica is not None:
            b_anti = self.puerta_b(pregunta_antilexica)
            b_anti["puerta"] = "b_antilexica"
            puertas.append(b_anti)
            puertas.append(self.puerta_d(pregunta_antilexica,
                                         tokens_prohibidos or set(),
                                         sample["gold"]))
        motivos = [m for p in puertas for m in p["motivos"]]
        return {
            "sample_id": sample.get("sample_id"),
            "veredicto": "apto" if not motivos else "descartado",
            "motivos": motivos,
            "requiere_llm": sorted({f for p in puertas
                                    for f in p["requiere_llm"]}),
            "detalle_puertas": puertas,
        }
