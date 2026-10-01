"""
mediciones_p2.py — U-PYD, etapa P2 (d): las tres mediciones que L-ESQ-R2 dejó
para esta unidad. USD 0, solo lectura de datos guardados.

DECLARACIONES (fijadas antes de correr la medición):

D-VENT · Ventana de la verificación por tokens (nivel 2 de la mención).
  Población: las relaciones aplica_a o ejecuta del crudo L0 de diez con
  `sujeto_propuesto` no vacío (N1 cuenta 63, sujeto_propuesto_literal). Texto
  propio: texto propio más heredado del chunk (como R-LIT de N1). Por mención:
  nivel exacto y holgura mínima = (largo de la ventana mínima que contiene
  todos sus tokens distintos) − (tokens distintos). Texto ajeno: otro chunk del
  mismo TO, uno por mención, `random.Random(20261001).choice` sobre los ids del
  TO ordenados, sin el propio, en el orden de la población. Falsa aceptación =
  la mención verifica (exacta, o por tokens con holgura ≤ h) contra el texto
  ajeno. Se tabula h ∈ {0, 1, 2, 3, 4, 5, 6, 8, 10, 15, 20, sin tope}.
  Complemento declarado, fuera de lo que fija el mandato: la misma tasa contra TODOS
  los otros chunks del TO, sin sorteo.

D-COMP · Reglas de comparación. Población del par B: nodos Restriccion,
  Condicion, Obligacion y Excepcion de los grafos r1, desarrollo, cinco y diez
  cuya `properties.descripcion` (NFC, sin distinguir mayúsculas) tiene cuantía
  según el comando [c14] de docs/tablero_correcciones.md (versión vigente en
  3ffb99d, con números en letras y cifra entre paréntesis opcional). Control:
  con cuantía 639 / 606 / 77 / 683 y sin campo 218 / 287 / 36 / 323 (tablero
  de correcciones, fila «Cuantías sin campo estructurado»). Sobre cada
  descripción, `reglas_comparacion.analizar(descripcion, descripcion, título del
  punto)`, con el título del primer chunk de la procedencia del nodo. Se cuenta
  la regla de cada cuantía; `comparacion_asumida` y `no_determinada` aparte;
  las apariciones de «factor» como marcador de coeficiente, con su contexto; y,
  entre las cuantías sin marcador, las formas candidatas para «igual»
  (reglas_comparacion.CANDIDATAS_IGUAL) y otras formas no cubiertas
  (FORMAS_NO_CUBIERTAS de este script), en la ventana anterior a la cuantía.

D-LARGO · Largo mínimo del tramo de las omisiones. Con los datos guardados no
  hay tramos, solo cadenas libres: el valor es provisional. Base: el tramo
  tiene que identificar su lugar en el texto propio. Sobre los chunks con
  omisión no vacía en el crudo L0 de diez, se tokeniza el texto propio con
  R-NORM y, para n = 1 a 10, se cuenta la fracción de posiciones cuyo n-grama
  aparece una sola vez en su chunk. Valor provisional propuesto: el menor n con
  fracción ≥ 0,95 en el agregado de las posiciones.

AGREGADOS TRAS LA PRIMERA CORRIDA (01/10/2026; rotulados como posteriores, no
reemplazan ninguna declaración previa y se reportan aparte):

A-LARGO · D-LARGO no da valor: ningún n de 1 a 10 llega a 0,95 (a 10 tokens,
  0,9454). Se extiende el mismo cálculo hasta n = 40 y se informa el menor n que
  llega a 0,95 con ese rango, como dato posterior.

A-IGUAL · Propuesta de regla para «igual», medida sobre la misma población:
  «igual a/al» o «equivalente(s) a/al» seguidos inmediatamente de la cuantía
  (adyacencia), en una cuantía hoy sin marcador. Se excluye, con su motivo, la
  que tiene en la ventana anterior una compuesta en orden inverso («menor o
  igual»…), una forma de «super-»/«exced-», o «máximo», «mínimo», «tope» o
  «límite», o «o más»/«o menos» pospuesto. Se cuentan también las compuestas
  en orden inverso («menor o igual», «inferior o igual», «mayor o igual»,
  «superior o igual»), que la lista del laudo no tiene.

A-RAIZ · Formas de las raíces «super-» y «exced-» presentes en la ventana
  anterior de una cuantía sin marcador y que la implementación de P1 no
  reconoce (enumera terminaciones; por ejemplo, falta el imperfecto «superaba»).
  Se excluyen «superintend-», «supervis-», «superfic-», «superávit» y
  «excedente».

A-COEF · Fuente del marcador de coeficiente (tramo, descripción o título), por
  palabra, para dimensionar los casos de «factor».

Escribe resultados/mediciones_p2.json y .md (o en --salida), sin fechas ni
rutas absolutas.

Uso (desde la raíz del repo):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/pyd_r2/code/mediciones_p2.py
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
import sys
import unicodedata
from collections import Counter, OrderedDict
from pathlib import Path

AQUI = Path(__file__).resolve().parent
if str(AQUI) not in sys.path:
    sys.path.insert(0, str(AQUI))
import modelos_r2 as M  # noqa: E402
import reglas_comparacion as RC  # noqa: E402
import validador_r2 as V  # noqa: E402
import lector_crudo_v3 as L  # noqa: E402

REPO = M.REPO
SALIDA = M.PYD_R2 / "resultados"
COMANDO = "PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/pyd_r2/code/mediciones_p2.py"
SEMILLA_VENTANA = 20261001
HOLGURAS = (0, 1, 2, 3, 4, 5, 6, 8, 10, 15, 20, None)
TABLERO_C = "docs/tablero_correcciones.md"
TABLERO_C_SHA = "11ad670d5d534ae064eda296e8f0e3f483e1ae0660bb45e18396ee98b2b63be4"
TIPOS_CUANTIA = ("Restriccion", "Condicion", "Obligacion", "Excepcion")
ESPERADO_C14 = {"r1": (639, 218), "desarrollo": (606, 287), "cinco": (77, 36), "diez": (683, 323)}
UMBRAL_UNICIDAD = 0.95
N_MAX_DECLARADO = 10
N_MAX_POSTERIOR = 40
RE_IGUAL_ADYACENTE = re.compile(r"\b(?:iguale?s?|equivalentes?)\s+(?:a|al)\s+$")
RE_COMPARATIVO_DELANTE = re.compile(r"\b(?:menor|mayor|inferior|superior)(?:es)?\s+o\s+(?:iguale?s?|equivalentes?)\s+(?:a|al)\s+$")
RE_COMPUESTA_INVERSA = re.compile(r"\b(?:menor|inferior|mayor|superior)(?:es)?\s+o\s+iguale?s?\b")
RE_RAIZ = re.compile(r"\b(?:super|exced)\w*")
RAIZ_NO_MARCADOR = ("superintend", "supervis", "superfic", "superavit", "excedente")
RE_TOPE = re.compile(r"\b(?:maxim[oa]s?|minim[oa]s?|topes?|limites?)\b")
RE_O_MAS_MENOS = re.compile(r"^\s*(?:\([^()]{0,60}\)\s*)?o\s+(?:mas|menos)\b")


def raiz_no_reconocida(texto_plegado: str) -> list[str]:
    out = []
    for m in RE_RAIZ.finditer(texto_plegado):
        w = m.group()
        if w.startswith(RAIZ_NO_MARCADOR):
            continue
        if any(pat.fullmatch(w) for _, f, pat in RC.SIMPLES if f in ("raiz_super", "raiz_exced")):
            continue
        out.append(w)
    return out

# ------------------------------------------------------------------------- #
# [c14] (docs/tablero_correcciones.md, en 3ffb99d)                            #
# ------------------------------------------------------------------------- #
_C14_LETRAS = ("un", "una", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez",
               "once", "doce", "quince", "veinte", "treinta", "cuarenta", "sesenta", "noventa", "ciento",
               "cien")
_C14_NUM = r"(?:\d+|" + "|".join(sorted(_C14_LETRAS, key=len, reverse=True)) + r")"
_C14_UNID = r"(?:d[ií]as?|mes(?:es)?|a[ñn]os?|horas?|semanas?)"
C14 = (
    re.compile(r"\d+([.,]\d+)?\s*%|por\s+ciento", re.I),
    re.compile(r"\bveces\b", re.I),
    re.compile(r"\b" + _C14_NUM + r"\s+(?:\(\s*\d+\s*\)\s*)?" + _C14_UNID + r"\b|d[ií]as\s+(?:h[aá]biles|corridos)",
               re.I),
    re.compile(r"(?:US\$|U\$S|USD|\$)\s*\d|\d[\d.,]*\s*(?:millones\s+de\s+|mil\s+)?(?:pesos|d[oó]lares|USD|UVA)\b",
               re.I),
)
# Frases del comando [c14] que el candado exige en el texto firmado.
C14_ANCLAS = ("opcionalmente seguido de una cifra entre", "«€» y «EUR» no", "`\\bveces\\b`")


def tiene_c14(desc: str) -> bool:
    d = unicodedata.normalize("NFC", desc or "")
    return any(p.search(d) for p in C14)


FORMAS_NO_CUBIERTAS = (
    ("por_lo_menos", re.compile(r"\bpor\s+lo\s+menos\b")),
    ("o_mas_pospuesto", re.compile(r"^\s*o\s+mas\b")),
    ("o_menos_pospuesto", re.compile(r"^\s*o\s+menos\b")),
    ("tope", re.compile(r"\btopes?\b")),
    ("limite", re.compile(r"\blimites?\b")),
    ("maximo_no_adyacente", re.compile(r"\bmaxim[oa]s?\b")),
    ("minimo_no_adyacente", re.compile(r"\bminim[oa]s?\b")),
    ("superior_sin_a", re.compile(r"\bsuperior(?:es)?\b(?!\s+al?\b)")),
    ("mayor_menor_inferior_sin_a", re.compile(r"\b(?:mayor|menor|inferior)(?:es)?\b(?!\s+al?\b)")),
    ("entre", re.compile(r"\bentre\b")),
)


# ------------------------------------------------------------------------- #
# D-VENT                                                                      #
# ------------------------------------------------------------------------- #
def holgura_minima(aguja: str, texto: str) -> tuple[bool, int | None]:
    """(exacta, holgura mínima por tokens o None si falta algún token)."""
    nivel, _ = V.verificar_tramo(aguja, texto, 0)
    if nivel == "exacta":
        return True, 0
    at = V.norm_tokens(aguja)
    tt = [t for t, _, _ in V.tokens_con_spans(texto)]
    v = V._ventana_minima(tt, set(at))
    if v is None:
        return False, None
    return False, (v[1] - v[0]) - len(set(at))


def acepta(exacta: bool, hol: int | None, h: int | None) -> bool:
    if exacta:
        return True
    if hol is None:
        return False
    return h is None or hol <= h


def medir_ventana(crudo) -> dict:
    pob = []
    for reg in crudo.registros("diez", "L0"):
        ti = reg["tool_input"]
        if not isinstance(ti, dict) or not isinstance(ti.get("relations"), list):
            continue
        for i, r in enumerate(ti["relations"]):
            if not isinstance(r, dict) or r.get("predicate") not in M.PREDICADOS_SUJETO:
                continue
            sp = V._str_o_none(r.get("sujeto_propuesto"))
            if sp is not None:
                pob.append({"to": reg["to"], "chunk_id": reg["chunk_id"], "indice": i, "mencion": sp})
    por_to = {}
    for cid in sorted(crudo.chunks):
        por_to.setdefault(cid.split("::")[0], []).append(cid)
    rng = random.Random(SEMILLA_VENTANA)
    filas = []
    for p in pob:
        propio = V.texto_completo(crudo.chunks[p["chunk_id"]])
        ex, hol = holgura_minima(p["mencion"], propio)
        otros = [c for c in por_to[p["to"]] if c != p["chunk_id"]]
        ajeno = rng.choice(otros)
        exa, hola = holgura_minima(p["mencion"], V.texto_completo(crudo.chunks[ajeno]))
        todos = [holgura_minima(p["mencion"], V.texto_completo(crudo.chunks[c])) for c in otros]
        filas.append({**p, "exacta": ex, "holgura": hol, "chunk_ajeno": ajeno, "ajeno_exacta": exa,
                      "ajeno_holgura": hola, "n_otros": len(otros),
                      "todos": Counter("e" if e else ("n" if h is None else h) for e, h in todos)})
    tabla = []
    for h in HOLGURAS:
        prop = sum(acepta(f["exacta"], f["holgura"], h) for f in filas)
        prop_tok = sum((not f["exacta"]) and acepta(False, f["holgura"], h) for f in filas)
        fa = sum(acepta(f["ajeno_exacta"], f["ajeno_holgura"], h) for f in filas)
        fa_tok = sum((not f["ajeno_exacta"]) and acepta(False, f["ajeno_holgura"], h) for f in filas)
        pares = sum(f["n_otros"] for f in filas)
        fa_todos = sum(sum(n for k, n in f["todos"].items()
                           if k == "e" or (k != "n" and (h is None or k <= h))) for f in filas)
        fa_todos_tok = sum(sum(n for k, n in f["todos"].items() if k not in ("e", "n") and (h is None or k <= h))
                           for f in filas)
        tabla.append({"holgura": "sin tope" if h is None else h, "propias_aceptadas": prop,
                      "propias_por_tokens": prop_tok, "ajenas_aceptadas": fa, "ajenas_por_tokens": fa_tok,
                      "ajenas_exactas": sum(f["ajeno_exacta"] for f in filas),
                      "todos_los_otros_pares": pares, "todos_los_otros_aceptados": fa_todos,
                      "todos_los_otros_por_tokens": fa_todos_tok})
    for f in filas:
        f["todos"] = {str(k): v for k, v in sorted(f["todos"].items(), key=lambda kv: str(kv[0]))}
    n1 = crudo.n1["sujeto_propuesto_literal"]["por_grupo"]["crudo"]["diez"]
    control = {"poblacion": len(filas), "n1_total": n1["total"],
               "exactas": sum(f["exacta"] for f in filas), "n1_presente": n1["presente"],
               "tokens_sin_tope_no_exactas": sum((not f["exacta"]) and f["holgura"] is not None for f in filas),
               "n1_ausente_con_todos_los_tokens": n1["ausente_con_todos_los_tokens"]}
    control["coincide"] = (control["poblacion"] == control["n1_total"]
                           and control["exactas"] == control["n1_presente"]
                           and control["tokens_sin_tope_no_exactas"] == control["n1_ausente_con_todos_los_tokens"])
    return {"semilla": SEMILLA_VENTANA, "control_n1": control, "tabla": tabla, "menciones": filas}


# ------------------------------------------------------------------------- #
# D-COMP                                                                      #
# ------------------------------------------------------------------------- #
def _con_campo(n: dict) -> bool:
    p = n.get("properties") or {}
    return any(isinstance(p.get(k), str) and p.get(k).strip() for k in ("umbral", "plazo"))


def _titulo(n: dict, chunks: dict) -> str | None:
    for pv in n.get("provenances") or [n.get("provenance") or {}]:
        cid = pv.get("chunk_id")
        if cid and cid in chunks:
            return chunks[cid].get("titulo")
    return None


def medir_comparacion(crudo) -> dict:
    texto_c = L.leer_firmado(L.COMMIT_MANDATO, TABLERO_C, TABLERO_C_SHA).decode("utf-8")
    anclas_ok = all(a in texto_c for a in C14_ANCLAS)
    out = OrderedDict()
    out["c14_anclas_en_el_texto_firmado"] = anclas_ok
    for g in ("r1", "desarrollo", "cinco", "diez"):
        kg = json.loads(crudo._verificado(f"{g}_kg.json").decode("utf-8"))
        nodos = [n for n in kg["nodes"] if n["type"] in TIPOS_CUANTIA
                 and tiene_c14((n.get("properties") or {}).get("descripcion"))]
        sin_campo = sum(1 for n in nodos if not _con_campo(n))
        reglas, comps, por_tipo = Counter(), Counter(), Counter()
        asumida, sin_cuantia = 0, []
        factor, igual, no_cub = [], Counter(), Counter()
        coef_fuente = Counter()
        prop_igual, inversas = [], []
        raiz_nr = Counter()
        n_cuantias = 0
        for n in sorted(nodos, key=lambda x: x["id"]):
            d = n["properties"]["descripcion"]
            cs = RC.analizar(d, d, _titulo(n, crudo.chunks))
            if not cs:
                sin_cuantia.append({"id": n["id"], "descripcion": d[:200]})
            for c in cs:
                n_cuantias += 1
                reglas[c.regla] += 1
                comps[c.comparacion] += 1
                por_tipo[(n["type"], c.comparacion)] += 1
                asumida += c.comparacion_asumida
                if c.regla == "coeficiente":
                    coef_fuente[f"{c.fuente_marcador}:{RC.plegar(c.marcador or '')[:7]}"] += 1
                if c.regla in ("sin_marcador", "sin_marcador_plazo"):
                    antes_txt = RC.plegar(d[max(0, c.inicio - 200):c.inicio])
                    antes_vent = " ".join(antes_txt.split()[-RC.VENTANA_ANTES:])
                    despues_txt = RC.plegar(d[c.fin:c.fin + 80])
                    raices = raiz_no_reconocida(antes_vent)
                    for w in raices:
                        raiz_nr[f"{c.regla}:{w}"] += 1
                    if RE_IGUAL_ADYACENTE.search(antes_txt):
                        motivos = []
                        if RE_COMPUESTA_INVERSA.search(antes_vent):
                            motivos.append("compuesta_inversa")
                        if any(not w.startswith(RAIZ_NO_MARCADOR) for w in RE_RAIZ.findall(antes_vent)):
                            motivos.append("raiz_super_exced")
                        if RE_TOPE.search(antes_vent):
                            motivos.append("maximo_minimo_tope_limite")
                        if RE_O_MAS_MENOS.search(despues_txt):
                            motivos.append("o_mas_o_menos_pospuesto")
                        prop_igual.append({"id": n["id"], "regla_actual": c.regla, "cuantia": c.texto,
                                           "ventana": c.ventana, "excluida_por": motivos})
                    if RE_COMPUESTA_INVERSA.search(antes_vent):
                        inversas.append({"id": n["id"], "regla_actual": c.regla, "cuantia": c.texto,
                                         "ventana": c.ventana})
                if c.regla == "coeficiente" and RC.plegar(c.marcador or "").startswith("factor"):
                    factor.append({"id": n["id"], "tipo": n["type"], "fuente": c.fuente_marcador,
                                   "cuantia": c.texto, "ventana": c.ventana, "descripcion": d})
                if c.regla in ("sin_marcador", "sin_marcador_plazo"):
                    antes = RC.plegar(d[:c.inicio])
                    antes_v = " ".join(antes.split()[-RC.VENTANA_ANTES:])
                    despues = RC.plegar(d[c.fin:])
                    for nombre, pat in RC.CANDIDATAS_IGUAL:
                        if pat.search(antes_v + " "):
                            igual[f"{c.regla}:{nombre}"] += 1
                    for nombre, pat in FORMAS_NO_CUBIERTAS:
                        if nombre.endswith("pospuesto"):
                            if pat.search(despues):
                                no_cub[f"{c.regla}:{nombre}"] += 1
                        elif pat.search(antes_v):
                            no_cub[f"{c.regla}:{nombre}"] += 1
        esp = ESPERADO_C14[g]
        out[g] = {"nodos_con_cuantia_c14": len(nodos), "sin_campo": sin_campo,
                  "control_tablero": {"esperado": list(esp), "coincide": (len(nodos), sin_campo) == esp},
                  "cuantias_detectadas": n_cuantias, "nodos_sin_cuantia_detectada": len(sin_cuantia),
                  "regla": dict(sorted(reglas.items(), key=lambda kv: (-kv[1], kv[0]))),
                  "comparacion": dict(sorted(comps.items(), key=lambda kv: (-kv[1], kv[0]))),
                  "comparacion_asumida": asumida,
                  "no_determinada": comps.get("no_determinada", 0),
                  "comparacion_por_tipo": {f"{t}|{c}": v for (t, c), v in sorted(por_tipo.items())},
                  "factor": factor,
                  "coeficiente_por_fuente": dict(sorted(coef_fuente.items())),
                  "propuesta_igual_adyacente": prop_igual,
                  "propuesta_igual_queda": sum(1 for x in prop_igual if not x["excluida_por"]),
                  "raiz_no_reconocida_sin_marcador": dict(sorted(raiz_nr.items())),
                  "compuestas_inversas_sin_marcador": inversas,
                  "candidatas_igual_sin_marcador": dict(sorted(igual.items())),
                  "formas_no_cubiertas_sin_marcador": dict(sorted(no_cub.items())),
                  "ejemplos_sin_cuantia_detectada": sin_cuantia}
    return out


# ------------------------------------------------------------------------- #
# D-LARGO                                                                     #
# ------------------------------------------------------------------------- #
def medir_largo(crudo) -> dict:
    chunks_om = []
    for reg in crudo.registros("diez", "L0"):
        ti = reg["tool_input"]
        om = ti.get("omisiones_no_prosa") if isinstance(ti, dict) else None
        if isinstance(om, list) and any(isinstance(o, str) and o.strip() for o in om):
            chunks_om.append(reg["chunk_id"])
    filas = []
    for n in range(1, N_MAX_POSTERIOR + 1):
        tot = uni = 0
        for cid in chunks_om:
            toks = V.norm_tokens(crudo.chunks[cid].get("texto") or "")
            grams = [tuple(toks[i:i + n]) for i in range(len(toks) - n + 1)]
            c = Counter(grams)
            tot += len(grams)
            uni += sum(1 for x in grams if c[x] == 1)
        filas.append({"n": n, "posiciones": tot, "unicas": uni, "fraccion": round(uni / tot, 4) if tot else None})
    def primero(nmax):
        return next((f["n"] for f in filas if f["n"] <= nmax and f["fraccion"] is not None
                     and f["fraccion"] >= UMBRAL_UNICIDAD), None)
    n1 = crudo.n1["omisiones"]["diez"]["con_omisiones_total"]["crudo"]
    largos = sorted(len(V.norm_tokens(crudo.chunks[c].get("texto") or "")) for c in chunks_om)
    return {"chunks_con_omision": len(chunks_om), "n1_con_omisiones_crudo": n1,
            "control_coincide": len(chunks_om) == n1, "umbral_unicidad": UMBRAL_UNICIDAD,
            "tabla": filas, "valor_declarado_n_hasta_10": primero(N_MAX_DECLARADO),
            "valor_posterior_n_hasta_40": primero(N_MAX_POSTERIOR),
            "tokens_del_texto_propio": {"minimo": largos[0], "mediana": largos[len(largos) // 2],
                                        "maximo": largos[-1]}}


# ------------------------------------------------------------------------- #
def _t(filas, cab):
    out = ["| " + " | ".join(cab) + " |", "|" + "---|" * len(cab)]
    for f in filas:
        out.append("| " + " | ".join(str(x) for x in f) + " |")
    return out


def escribir_md(J: dict) -> str:
    L_ = ["# U-PYD P2 — mediciones (ventana de la mención, reglas de comparación, largo del tramo)", "",
          f"Comando: `{J['comando']}`. Declaraciones D-VENT, D-COMP y D-LARGO en el docstring del script, "
          "fijadas antes de correr.", ""]
    W = J["ventana"]
    c = W["control_n1"]
    L_ += ["## 1. Ventana de la verificación por tokens", "",
           f"Población: {c['poblacion']} menciones (`sujeto_propuesto`, crudo L0 de diez; N1 {c['n1_total']}). "
           f"Exactas {c['exactas']} (N1 {c['n1_presente']}); por tokens sin tope y no exactas "
           f"{c['tokens_sin_tope_no_exactas']} (N1 {c['n1_ausente_con_todos_los_tokens']}). "
           f"Coincide con N1: {c['coincide']}. Semilla del chunk ajeno: {W['semilla']}.", ""]
    L_ += _t([[f["holgura"], f["propias_aceptadas"], f["propias_por_tokens"], f["ajenas_aceptadas"],
               f["ajenas_exactas"], f["ajenas_por_tokens"], f["todos_los_otros_aceptados"],
               f["todos_los_otros_por_tokens"], f["todos_los_otros_pares"]] for f in W["tabla"]],
             ["holgura h", "propias aceptadas (de 63)", "propias por tokens", "ajenas aceptadas (de 63)",
              "ajenas exactas", "ajenas por tokens", "todos los otros: aceptados", "todos los otros: por tokens",
              "pares (mención, otro chunk)"]) + [""]
    L_ += ["Menciones que verifican solo por tokens contra su propio chunk:", ""]
    L_ += _t([[f["chunk_id"], f["indice"], f["mencion"], f["holgura"], f["chunk_ajeno"],
               "exacta" if f["ajeno_exacta"] else f["ajeno_holgura"]]
              for f in W["menciones"] if not f["exacta"] and f["holgura"] is not None],
             ["chunk", "relación", "mención", "holgura mínima", "chunk ajeno", "en el ajeno"]) + [""]
    C = J["comparacion"]
    L_ += ["## 2. Reglas de comparación sobre las ventanas de cuantía", "",
           f"Anclas del comando [c14] en el texto firmado: {C['c14_anclas_en_el_texto_firmado']}.", ""]
    L_ += _t([[g, d["nodos_con_cuantia_c14"], d["sin_campo"], d["control_tablero"]["esperado"],
               d["control_tablero"]["coincide"], d["cuantias_detectadas"], d["nodos_sin_cuantia_detectada"],
               d["comparacion_asumida"], d["no_determinada"]]
              for g, d in C.items() if isinstance(d, dict)],
             ["grafo", "nodos con cuantía [c14]", "sin campo", "tablero (con, sin)", "coincide",
              "cuantías detectadas", "nodos sin cuantía detectada", "comparacion_asumida", "no_determinada"]) + [""]
    for g in ("desarrollo", "diez", "r1"):
        d = C[g]
        L_ += [f"### Frecuencia de cada forma — {g}", ""]
        L_ += _t([[k, v] for k, v in d["regla"].items()], ["regla", "cuantías"]) + [""]
        L_ += _t([[k, v] for k, v in d["comparacion"].items()], ["comparación", "cuantías"]) + [""]
        L_ += [f"Candidatas para «igual» entre las cuantías sin marcador: "
               f"{', '.join(f'{k} {v}' for k, v in d['candidatas_igual_sin_marcador'].items()) or '—'}.", "",
               f"Formas no cubiertas entre las cuantías sin marcador: "
               f"{', '.join(f'{k} {v}' for k, v in d['formas_no_cubiertas_sin_marcador'].items()) or '—'}.", ""]
    L_ += ["### Fuente del marcador de coeficiente (A-COEF)", ""]
    L_ += _t([[g, ", ".join(f"{k} {v}" for k, v in C[g]["coeficiente_por_fuente"].items())]
              for g in ("r1", "desarrollo", "cinco", "diez")], ["grafo", "fuente:palabra"]) + [""]
    for g in ("diez", "r1"):
        L_ += [f"### Propuesta para «igual» (A-IGUAL) — {g}: {len(C[g]['propuesta_igual_adyacente'])} cuantías "
               f"sin marcador con «igual/equivalente a» adyacente, {C[g]['propuesta_igual_queda']} sin motivo de "
               f"exclusión; {len(C[g]['compuestas_inversas_sin_marcador'])} con compuesta inversa", ""]
        L_ += _t([["igual", x["id"][:60], x["regla_actual"], x["cuantia"], ", ".join(x["excluida_por"]) or "—",
                   x["ventana"].replace("|", "/")[:150]] for x in C[g]["propuesta_igual_adyacente"]]
                 + [["inversa", x["id"][:60], x["regla_actual"], x["cuantia"], "—",
                     x["ventana"].replace("|", "/")[:150]] for x in C[g]["compuestas_inversas_sin_marcador"]],
                 ["forma", "nodo", "regla actual", "cuantía", "excluida por", "ventana"]) + [""]
        L_ += [f"Raíces «super-»/«exced-» no reconocidas en cuantías sin marcador (A-RAIZ): "
               f"{', '.join(f'{k} {v}' for k, v in C[g]['raiz_no_reconocida_sin_marcador'].items()) or '—'}.", ""]
    for g in ("diez", "r1"):
        L_ += [f"### «factor» como marcador de coeficiente — {g} ({len(C[g]['factor'])} cuantías)", ""]
        L_ += _t([[x["id"][:60], x["tipo"], x["fuente"], x["cuantia"], x["ventana"].replace("|", "/")[:160]]
                  for x in C[g]["factor"]], ["nodo", "tipo", "fuente del marcador", "cuantía", "ventana"]) + [""]
    Lg = J["largo_tramo"]
    L_ += ["## 3. Largo mínimo del tramo de las omisiones (provisional)", "",
           f"Chunks con omisión en el crudo L0 de diez: {Lg['chunks_con_omision']} (N1 {Lg['n1_con_omisiones_crudo']}; "
           f"coincide {Lg['control_coincide']}). Criterio declarado: menor n con fracción de n-gramas únicos en su "
           f"chunk ≥ {Lg['umbral_unicidad']}, n de 1 a 10: {Lg['valor_declarado_n_hasta_10']}. Extensión posterior "
           f"(A-LARGO), n hasta 40: {Lg['valor_posterior_n_hasta_40']}. Tokens del texto propio: "
           f"{Lg['tokens_del_texto_propio']}.", ""]
    L_ += _t([[f["n"], f["posiciones"], f["unicas"], f["fraccion"]] for f in Lg["tabla"]],
             ["n", "posiciones", "únicas en su chunk", "fracción"]) + [""]
    return "\n".join(L_) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", default=str(SALIDA))
    args = ap.parse_args()
    out = Path(args.salida)
    out.mkdir(parents=True, exist_ok=True)
    crudo = L.Crudo()
    J = {"unidad": "U-PYD", "etapa": "P2", "comando": COMANDO,
         "politica": {"ruta": str(V.POLITICA.relative_to(REPO)), "sha256": V.politica_default().sha256},
         "ventana": medir_ventana(crudo), "comparacion": medir_comparacion(crudo), "largo_tramo": medir_largo(crudo)}
    b_json = (json.dumps(J, ensure_ascii=False, indent=1) + "\n").encode("utf-8")
    b_md = escribir_md(J).encode("utf-8")
    for nombre, b in (("mediciones_p2.json", b_json), ("mediciones_p2.md", b_md)):
        (out / nombre).write_bytes(b)
        print(f"{hashlib.sha256(b).hexdigest()}  {nombre}")


if __name__ == "__main__":
    main()
