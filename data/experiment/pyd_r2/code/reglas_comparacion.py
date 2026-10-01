"""
reglas_comparacion.py — U-PYD: reglas en código que fijan `comparacion` de un
elemento de umbral a partir de su tramo (L-ESQ-R2, versión firmada en 4ef7650,
§1.3, punto 3), más la detección de la cuantía (valor, unidad) y de la base.

El laudo fija el SENTIDO de cada forma; este módulo es la implementación.
Precedencia (§1.3.3): coeficiente → negación → compuestas (con la adyacencia
de «mínimo»/«máximo») → simples → igual → sin marcador.

  - Coeficiente: «pondera…», «ponderador», «ponderación», «coeficiente»,
    «factor». Es el único marcador que puede venir también de la descripción
    o del título del punto; «factor», solo del tramo o del título
    (calibración P3, decisión 4).
  - Simples: mínimo estricto = las raíces «super-» y «exced-» (toda forma,
    salvo «superintend-», «supervis-», «superfic-», «superávit» y
    «excedente»; «superior(es)» cuenta con o sin «a»), «más de», «mayor(es)
    a»; máximo estricto = «inferior(es) a», «menos de», «menor(es) a».
    «Mayor», «menor» e «inferior» cuentan solo seguidos de «a» o de «al»
    (notas del 01/10 a L-ESQ-R2 §1.3; calibración P3, decisiones 1 y 3).
  - Negación general: «no» o «sin» delante de una simple, con cero a tres
    palabras en el medio, invierte el sentido (¬ mínimo estricto = máximo
    inclusivo; ¬ máximo estricto = mínimo inclusivo). DECLARADO: la misma
    inversión se aplica a los comparativos compuestos «igual o superior/
    mayor/inferior/menor» y «menor/inferior/mayor/superior o igual»
    (¬ mínimo inclusivo = máximo estricto y viceversa).
  - Compuestas: «igual o superior/mayor», «mayor/superior o igual», «al
    menos», «por lo menos», «como mínimo», «un mínimo de» → mínimo
    inclusivo; «igual o inferior/menor», «menor/inferior o igual», «como
    máximo», «hasta», «dentro de» → máximo inclusivo. «Mínimo»/«máximo» en
    cualquier género y número seguidos inmediatamente de la cuantía, con o
    sin «de» (o «del»), tienen el mismo nivel. «Como máximo», «como mínimo»,
    «al menos» y «por lo menos» valen también pospuestos a la cuantía; «o
    más» y «o menos», solo pospuestos y pegados a ella (mínimo / máximo
    inclusivo). Calibración P3, decisión 2.
  - Igual (calibración P3, decisión 5): «igual(es) a/al» o «equivalente(s)
    a/al» pegados a la cuantía, con la precedencia más baja de las formas
    con marcador (después de las simples), salvo que haya otro comparativo
    en la cláusula. DECLARADO: «comparativo» es la palabra comparativa
    (raíces «super-»/«exced-», «mayor», «menor», «superior», «inferior»,
    «más», «menos»; COMPARATIVO_EN_CLAUSULA); además, como en la propuesta
    de P2, «máximo», «mínimo», «tope» o «límite» en la ventana anterior
    excluyen (TOPE_EN_VENTANA). «Hasta» temporal o «capital mínimo» lejos de
    la cuantía no excluyen.
  - Sin marcador: plazo (unidad temporal) → máximo inclusivo con
    `comparacion_asumida`; cualquier otra cuantía → `no_determinada`.
    «Límite», «tope», «entre» y «máximo» no adyacente no son marcadores
    (calibración P3, decisión 9).

Adyacencia: los marcadores se buscan en una ventana junto a cada cuantía, no
en todo el texto: hasta VENTANA_ANTES palabras antes y VENTANA_DESPUES después,
sin cruzar un límite de cláusula («;», «:», punto final) ni otra cuantía. La
negación se busca hacia atrás desde el marcador, dentro de la cláusula.

Cuantías: adaptación de las regex D-P6 del prototipo de U-UMBRAL
(reports/u_umbral/u_umbral_u1.py:563-590), con dos cambios declarados: el
paréntesis después del número admite texto («365 (trescientos sesenta y cinco)
días») y una cuantía repetida entre paréntesis junto a otra igual («30%
(treinta por ciento)») se cuenta una vez.

Sin API, sin archivos: funciones puras.
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import asdict, dataclass, field
from decimal import Decimal, InvalidOperation
from typing import Optional

VENTANA_ANTES = 10
VENTANA_DESPUES = 3
NEGACION_MAX_MEDIO = 3
BASE_MAX_PALABRAS = 20

# ------------------------------------------------------------------------- #
# Plegado: minúsculas y sin diacríticos, con el mismo largo que el original   #
# ------------------------------------------------------------------------- #


def _plegar_char(c: str) -> str:
    d = unicodedata.normalize("NFKD", c)
    base = "".join(x for x in d if not unicodedata.combining(x))
    base = base.lower()
    return base if len(base) == 1 else c.lower()[:1] or c


def plegar(texto: str) -> str:
    """Minúsculas y sin diacríticos, carácter por carácter (los offsets del
    texto plegado son los del original)."""
    return "".join(_plegar_char(c) for c in texto)


# ------------------------------------------------------------------------- #
# Cuantías                                                                    #
# ------------------------------------------------------------------------- #
LETRAS_VALOR = {"un": 1, "una": 1, "uno": 1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
                "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11, "doce": 12,
                "trece": 13, "catorce": 14, "quince": 15, "dieciseis": 16, "diecisiete": 17,
                "dieciocho": 18, "diecinueve": 19, "veinte": 20, "veintiuno": 21, "veintiun": 21,
                "veintidos": 22, "veintitres": 23, "veinticuatro": 24, "veinticinco": 25,
                "veintiseis": 26, "veintisiete": 27, "veintiocho": 28, "veintinueve": 29,
                "treinta": 30, "cuarenta": 40, "cincuenta": 50, "sesenta": 60, "setenta": 70,
                "ochenta": 80, "noventa": 90, "cien": 100}
_ALT_LV = "|".join(sorted(LETRAS_VALOR, key=len, reverse=True))
_NUM = r"(\d+(?:[.,]\d+)?|" + _ALT_LV + r")"
_PAREN = r"(?:\s*\([^()]{1,60}\))?"
_CIFRA = r"(\d[\d.,]*\d|\d)"

# Los patrones corren sobre el texto plegado (sin tildes, minúsculas).
PATRONES = (
    ("porcentaje", re.compile(r"(?<![\d.,])(\d+(?:[.,]\d+)?)\s*%")),
    ("porcentaje", re.compile(r"(?<![\w.,])" + _NUM + _PAREN + r"\s+por\s+ciento\b")),
    ("veces", re.compile(r"(?<![\w.,])" + _NUM + _PAREN + r"\s+veces\b")),
    ("plazo", re.compile(r"(?<![\w.,])(\d+|" + _ALT_LV + r")" + _PAREN
                         + r"\s*(dias?|mes(?:es)?|anos?|horas?|semanas?)\b"
                         r"(?:\s+(habiles|corridos))?")),
    ("monto_pref", re.compile(r"(us\$|u\$s|usd|eur|€|\$)\s*" + _CIFRA
                              + r"(?:\s*(mil\s+millones|millones|mil)\b)?")),
    ("monto_suf", re.compile(r"(?<![\d.,])" + _CIFRA
                             + r"\s*(?:(mil\s+millones\s+de|millones\s+de|mil)\s+)?"
                             r"(pesos|dolares(?:\s+estadounidenses)?|usd|uva|euros)\b")),
)
_RE_COMPUESTO_ANTES = re.compile(r"(?:\b(?:" + _ALT_LV + r"|ciento|mil|cientos)\s+(?:y\s+)?)$")
MONEDA_CODIGO = {"$": "ARS", "pesos": "ARS", "us$": "USD", "u$s": "USD", "usd": "USD",
                 "dolares": "USD", "dolares estadounidenses": "USD", "eur": "EUR", "€": "EUR",
                 "euros": "EUR"}
MULT = {None: 1, "mil": 10 ** 3, "millones": 10 ** 6, "mil millones": 10 ** 9,
        "millones de": 10 ** 6, "mil millones de": 10 ** 9}
UNIDAD_TEMPORAL = (("dia", "dias"), ("mes", "meses"), ("ano", "anios"),
                   ("hora", "horas"), ("semana", "semanas"))


def parse_num(s: str) -> Optional[Decimal]:
    s = s.strip()
    if s in LETRAS_VALOR:
        return Decimal(LETRAS_VALOR[s])
    s = s.rstrip(".,")
    if "," in s:
        s2 = s.replace(".", "").replace(",", ".")
    elif re.fullmatch(r"\d{1,3}(\.\d{3})+", s):
        s2 = s.replace(".", "")
    else:
        s2 = s
    try:
        return Decimal(s2)
    except InvalidOperation:
        return None


def dec_str(d: Decimal) -> str:
    t = format(d.normalize(), "f")
    return t


@dataclass
class Cuantia:
    inicio: int
    fin: int
    texto: str
    clase: str
    valor: Optional[str] = None
    unidad: Optional[str] = None
    moneda: Optional[str] = None
    dias_tipo: Optional[str] = None
    fuera_de_lista: list = field(default_factory=list)
    comparacion: str = "no_determinada"
    regla: str = "sin_marcador"
    marcador: Optional[str] = None
    fuente_marcador: Optional[str] = None
    comparacion_asumida: bool = False
    base: Optional[str] = None
    ventana: str = ""

    def como_dict(self) -> dict:
        return asdict(self)


def _compuesto(pleg: str, inicio: int, grupo: str) -> bool:
    if grupo not in LETRAS_VALOR:
        return False
    return bool(_RE_COMPUESTO_ANTES.search(pleg[max(0, inicio - 30):inicio]))


def detectar_cuantias(texto: str) -> list[Cuantia]:
    """Cuantías del texto, en orden, sin solapamientos."""
    pleg = plegar(texto)
    crudos: list[Cuantia] = []
    for clase, pat in PATRONES:
        for m in pat.finditer(pleg):
            c = Cuantia(inicio=m.start(), fin=m.end(), texto=texto[m.start():m.end()], clase=clase)
            if clase in ("porcentaje", "veces"):
                g = m.group(1)
                if _compuesto(pleg, m.start(1), g):
                    continue
                v = parse_num(g)
                c.valor = dec_str(v) if v is not None else None
                c.unidad = "porcentaje" if clase == "porcentaje" else "veces"
            elif clase == "plazo":
                g, u, cal = m.group(1), m.group(2), m.group(3)
                if _compuesto(pleg, m.start(1), g):
                    continue
                v = parse_num(g)
                c.valor = dec_str(v) if v is not None else None
                c.unidad = next(n for pref, n in UNIDAD_TEMPORAL if u.startswith(pref))
                if c.unidad == "dias" and cal:
                    c.dias_tipo = "habiles" if cal == "habiles" else "corridos"
                if c.unidad not in ("dias", "meses", "anios"):
                    c.fuera_de_lista.append("unidad")
                c.clase = "plazo"
            elif clase == "monto_pref":
                mon = MONEDA_CODIGO[m.group(1)]
                v = parse_num(m.group(2))
                mult = MULT[re.sub(r"\s+", " ", m.group(3)) if m.group(3) else None]
                c.valor = dec_str(v * mult) if v is not None else None
                c.unidad, c.moneda, c.clase = "moneda", mon, "monto"
            else:
                v = parse_num(m.group(1))
                mult = MULT[re.sub(r"\s+", " ", m.group(2)) if m.group(2) else None]
                nombre = re.sub(r"\s+", " ", m.group(3))
                c.valor = dec_str(v * mult) if v is not None else None
                if nombre == "uva":
                    c.unidad = "uva"
                else:
                    c.unidad, c.moneda = "moneda", MONEDA_CODIGO[nombre]
                c.clase = "monto"
            crudos.append(c)
    crudos.sort(key=lambda c: (c.inicio, -(c.fin - c.inicio)))
    out: list[Cuantia] = []
    for c in crudos:
        if out and c.inicio < out[-1].fin:
            continue
        if out and _repetida_entre_parentesis(texto, out[-1], c):
            continue
        out.append(c)
    return out


def _repetida_entre_parentesis(texto: str, a: Cuantia, b: Cuantia) -> bool:
    """«30% (treinta por ciento)» o «treinta por ciento (30%)»: la segunda es
    la misma cuantía escrita de nuevo entre paréntesis."""
    if (a.valor, a.unidad) != (b.valor, b.unidad):
        return False
    return bool(re.fullmatch(r"\s*\(\s*", texto[a.fin:b.inicio])) and \
        bool(re.match(r"\s*\)", texto[b.fin:]))


# ------------------------------------------------------------------------- #
# Cláusulas y ventanas                                                        #
# ------------------------------------------------------------------------- #
_ABREV = frozenset({"com", "art", "arts", "inc", "res", "nro", "n", "pto", "ptos", "ap", "cfr",
                    "etc", "dec", "gral", "ej", "pag", "sr", "sres", "dr", "dra", "lic", "sec",
                    "num", "cap", "tit", "pt", "aprox"})
_RE_LIMITE = re.compile(r"[;:]|\.(?=\s|$)")


def limites_de_clausula(texto: str) -> list[int]:
    out = []
    for m in _RE_LIMITE.finditer(texto):
        if m.group() == ".":
            prev = re.search(r"(\w+)$", texto[:m.start()])
            if prev and plegar(prev.group(1)) in _ABREV:
                continue
        out.append(m.start())
    return out


def _palabras(s: str) -> list[re.Match]:
    return list(re.finditer(r"\S+", s))


# ------------------------------------------------------------------------- #
# Marcadores (sobre texto plegado)                                            #
# ------------------------------------------------------------------------- #
# Raíces (calibración P3, decisión 1): toda forma, con las exclusiones listadas.
_SUPER = r"super(?!intend|vis|fic|avit)\w*"
_EXCED = r"exced(?!ente)\w*"
SIMPLES = (
    ("minimo_estricto", "raiz_super", re.compile(r"\b" + _SUPER)),
    ("minimo_estricto", "raiz_exced", re.compile(r"\b" + _EXCED)),
    ("minimo_estricto", "mas_de", re.compile(r"\bmas\s+de\b")),
    ("minimo_estricto", "mayor", re.compile(r"\bmayor(?:es)?\s+al?\b")),
    ("maximo_estricto", "inferior", re.compile(r"\binferior(?:es)?\s+al?\b")),
    ("maximo_estricto", "menos_de", re.compile(r"\bmenos\s+de\b")),
    ("maximo_estricto", "menor", re.compile(r"\bmenor(?:es)?\s+al?\b")),
)
COMPUESTAS = (
    ("minimo_inclusivo", "igual_o_superior",
     re.compile(r"\biguale?s?\s+o\s+(?:superior(?:es)?|mayor(?:es)?)\b")),
    ("maximo_inclusivo", "igual_o_inferior",
     re.compile(r"\biguale?s?\s+o\s+(?:inferior(?:es)?|menor(?:es)?)\b")),
    ("maximo_inclusivo", "menor_o_igual",
     re.compile(r"\b(?:menor|inferior)(?:es)?\s+o\s+iguale?s?\b")),
    ("minimo_inclusivo", "mayor_o_igual",
     re.compile(r"\b(?:mayor|superior)(?:es)?\s+o\s+iguale?s?\b")),
    ("maximo_inclusivo", "como_maximo", re.compile(r"\bcomo\s+maximo\b")),
    ("maximo_inclusivo", "hasta", re.compile(r"\bhasta\b")),
    ("maximo_inclusivo", "dentro_de", re.compile(r"\bdentro\s+de\b")),
    ("minimo_inclusivo", "al_menos", re.compile(r"\bal\s+menos\b")),
    ("minimo_inclusivo", "como_minimo", re.compile(r"\bcomo\s+minimo\b")),
    ("minimo_inclusivo", "un_minimo_de", re.compile(r"\bun\s+minimo\s+de\b")),
    ("minimo_inclusivo", "por_lo_menos", re.compile(r"\bpor\s+lo\s+menos\b")),
)
POSPUESTAS = ("como_maximo", "como_minimo", "al_menos", "por_lo_menos")
COMPARATIVOS_COMPUESTOS = ("igual_o_superior", "igual_o_inferior", "menor_o_igual", "mayor_o_igual")
# «o más» / «o menos»: solo pospuestos y pegados a la cuantía (admite un paréntesis).
SOLO_POSPUESTAS = re.compile(r"\s*(?:\([^()]{0,60}\)\s*)?o\s+(mas|menos)\b")
ADYACENCIA = (
    ("minimo_inclusivo", "adyacencia_minimo", re.compile(r"\bminim[oa]s?\s+(?:del?\s+)?$")),
    ("maximo_inclusivo", "adyacencia_maximo", re.compile(r"\bmaxim[oa]s?\s+(?:del?\s+)?$")),
)
COEFICIENTE = re.compile(r"\bponder\w*|\bcoeficientes?\b|\bfactor(?:es)?\b")
# Desde la descripción, «factor» no cuenta (calibración P3, decisión 4).
COEFICIENTE_DESCRIPCION = re.compile(r"\bponder\w*|\bcoeficientes?\b")
# «igual» (calibración P3, decisión 5): pegado a la cuantía.
RE_IGUAL_PEGADO = re.compile(r"\b(iguale?s?|equivalentes?)\s+al?\s+$")
# Otro comparativo en la cláusula excluye «igual»: la palabra comparativa,
# con o sin «a» («superior» entra por la raíz «super-»).
COMPARATIVO_EN_CLAUSULA = re.compile(
    r"\b" + _SUPER + r"|\b" + _EXCED + r"|\b(?:mayor|menor|inferior)(?:es)?\b|\bmas\b|\bmenos\b")
# Y, como en la propuesta de P2 (A-IGUAL), estas palabras en la ventana anterior.
TOPE_EN_VENTANA = re.compile(r"\b(?:maxim[oa]s?|minim[oa]s?|topes?|limites?)\b")
NEGADORES = ("no", "sin")
INVERSION = {"minimo_estricto": "maximo_inclusivo", "maximo_estricto": "minimo_inclusivo",
             "minimo_inclusivo": "maximo_estricto", "maximo_inclusivo": "minimo_estricto"}

# Formas candidatas para «igual» que mide mediciones_p2.py entre las cuantías
# sin marcador; no se aplican (la regla es RE_IGUAL_PEGADO).
CANDIDATAS_IGUAL = (
    ("igual_a", re.compile(r"\biguale?s?\s+(?:a|al)\b")),
    ("equivalente_a", re.compile(r"\bequivalentes?\s+(?:a|al)\b")),
    ("sera_de", re.compile(r"\bser(?:a|an)\s+(?:de|del)\s*$")),
    ("fijado_en", re.compile(r"\bfijad[oa]s?\s+en\b")),
    ("de_a_secas", re.compile(r"\b(?:de|del)\s+$")),
)


def _negada(pleg: str, inicio_clausula: int, inicio_marcador: int) -> Optional[str]:
    """Negador («no»/«sin») con cero a NEGACION_MAX_MEDIO palabras entre él y
    el marcador, dentro de la cláusula. Devuelve el negador o None."""
    previo = re.findall(r"[a-z0-9ñ]+", pleg[inicio_clausula:inicio_marcador])
    for j in range(len(previo) - 1, max(-1, len(previo) - 2 - NEGACION_MAX_MEDIO), -1):
        if previo[j] in NEGADORES:
            return previo[j]
    return None


def _en(rango: tuple[int, int], m_ini: int) -> bool:
    return rango[0] <= m_ini < rango[1]


def fijar_comparacion(texto: str, c: Cuantia, inicio_clausula: int, fin_clausula: int,
                      fin_previa: int, inicio_siguiente: int,
                      descripcion: Optional[str] = None, titulo: Optional[str] = None) -> None:
    """Fija comparacion, regla, marcador y ventana de la cuantía `c`."""
    pleg = plegar(texto)
    ini_antes = max(inicio_clausula, fin_previa)
    pal = _palabras(texto[ini_antes:c.inicio])
    if len(pal) > VENTANA_ANTES:
        ini_antes = ini_antes + pal[-VENTANA_ANTES].start()
    fin_desp = min(fin_clausula, inicio_siguiente)
    pal_d = _palabras(texto[c.fin:fin_desp])
    if len(pal_d) > VENTANA_DESPUES:
        fin_desp = c.fin + pal_d[VENTANA_DESPUES - 1].end()
    antes = (ini_antes, c.inicio)
    despues = (c.fin, fin_desp)
    c.ventana = texto[ini_antes:fin_desp]

    # 1. Coeficiente: en la ventana, en la descripción o en el título.
    for fuente, s in (("tramo", pleg[antes[0]:despues[1]]), ("descripcion", plegar(descripcion or "")),
                      ("titulo", plegar(titulo or ""))):
        m = (COEFICIENTE_DESCRIPCION if fuente == "descripcion" else COEFICIENTE).search(s)
        if m:
            original = {"tramo": texto[antes[0]:despues[1]], "descripcion": descripcion or "",
                        "titulo": titulo or ""}[fuente]
            c.comparacion, c.regla, c.marcador, c.fuente_marcador = (
                "coeficiente", "coeficiente", original[m.start():m.end()], fuente)
            return

    compuestas = []
    for sentido, forma, pat in COMPUESTAS:
        for m in pat.finditer(pleg, antes[0], antes[1]):
            compuestas.append((m.start(), m.end(), sentido, forma, texto[m.start():m.end()]))
        if forma in POSPUESTAS:
            for m in pat.finditer(pleg, despues[0], despues[1]):
                compuestas.append((m.start(), m.end(), sentido, forma, texto[m.start():m.end()]))
    for sentido, forma, pat in ADYACENCIA:
        m = pat.search(pleg[antes[0]:antes[1]])
        if m:
            a0 = antes[0] + m.start()
            # Si la adyacencia cae dentro de una compuesta listada («como máximo»,
            # «un mínimo de»), cuenta la compuesta: mismo nivel, forma más específica.
            if not any(x[0] <= a0 < x[1] for x in compuestas):
                compuestas.append((a0, antes[1], sentido, forma, texto[a0:antes[1]].strip()))
    m = SOLO_POSPUESTAS.match(pleg, c.fin, min(fin_clausula, inicio_siguiente))
    if m:
        sentido, forma = (("minimo_inclusivo", "o_mas") if m.group(1) == "mas"
                          else ("maximo_inclusivo", "o_menos"))
        compuestas.append((m.start(1) - 2, m.end(), sentido, forma, texto[m.start(1) - 2:m.end()]))
    dentro_de_igual = [(a, b) for a, b, _, f, _ in compuestas if f in COMPARATIVOS_COMPUESTOS]

    simples = []
    for sentido, forma, pat in SIMPLES:
        for m in pat.finditer(pleg, antes[0], antes[1]):
            if any(a <= m.start() < b for a, b in dentro_de_igual):
                continue
            simples.append((m.start(), m.end(), sentido, forma, texto[m.start():m.end()]))

    def distancia(x):
        return c.inicio - x[1] if x[0] < c.inicio else x[0] - c.fin

    # 2. Negación de una simple o de «igual o …».
    negadas = []
    for x in simples + [y for y in compuestas if y[3] in COMPARATIVOS_COMPUESTOS]:
        neg = _negada(pleg, inicio_clausula, x[0])
        if neg:
            negadas.append((x, neg))
    if negadas:
        (x, neg) = min(negadas, key=lambda t: distancia(t[0]))
        c.comparacion = INVERSION[x[2]]
        c.regla, c.marcador, c.fuente_marcador = f"negacion:{x[3]}", f"{neg} … {x[4]}", "tramo"
        return
    # 3. Compuestas y adyacencia.
    if compuestas:
        x = min(compuestas, key=distancia)
        c.comparacion, c.regla, c.marcador, c.fuente_marcador = x[2], f"compuesta:{x[3]}", x[4], "tramo"
        return
    # 4. Simples.
    if simples:
        x = min(simples, key=distancia)
        c.comparacion, c.regla, c.marcador, c.fuente_marcador = x[2], f"simple:{x[3]}", x[4], "tramo"
        return
    # 5. Igual: pegado a la cuantía y sin otro comparativo en la cláusula.
    m = RE_IGUAL_PEGADO.search(pleg[antes[0]:antes[1]])
    if m:
        mi = antes[0] + m.start()
        clausula = (pleg[inicio_clausula:mi] + " " * (c.fin - mi) + pleg[c.fin:fin_clausula])
        if not COMPARATIVO_EN_CLAUSULA.search(clausula) and not TOPE_EN_VENTANA.search(pleg[antes[0]:mi]):
            forma = "equivalente_a" if m.group(1).startswith("equivalente") else "igual_a"
            c.comparacion, c.regla, c.marcador, c.fuente_marcador = (
                "igual", f"igual:{forma}", texto[mi:antes[1]].strip(), "tramo")
            return
    # 6. Sin marcador.
    if c.clase == "plazo":
        c.comparacion, c.regla, c.comparacion_asumida = "maximo_inclusivo", "sin_marcador_plazo", True
    else:
        c.comparacion, c.regla = "no_determinada", "sin_marcador"


# ------------------------------------------------------------------------- #
# Base (umbral relacional)                                                    #
# ------------------------------------------------------------------------- #
_RE_CONECTOR_PORC = re.compile(r"\s*(?:\([^()]{0,60}\)\s*)?(?:de|del|sobre)\s+")
_RE_CONECTOR_VECES = re.compile(r"\s*(?:\([^()]{0,60}\)\s*)?(?:(?:de|del|sobre)\s+|(?=(?:el|la|los|las|su|sus)\s))")
_RE_ARTICULO = re.compile(r"(?:el|la|los|las|lo)\s+")
_RE_COLA = re.compile(r"(?:\s+(?:y/o|y|o|e|u))+\s*$")


def fijar_base(texto: str, c: Cuantia, fin_clausula: int) -> None:
    if c.unidad not in ("porcentaje", "veces"):
        return
    pleg = plegar(texto)
    pat = _RE_CONECTOR_PORC if c.unidad == "porcentaje" else _RE_CONECTOR_VECES
    m = pat.match(pleg, c.fin, fin_clausula)
    if not m:
        return
    ini = m.end()
    a = _RE_ARTICULO.match(pleg, ini, fin_clausula)
    if a:
        ini = a.end()
    fin = fin_clausula
    coma = texto.find(",", ini, fin)
    if coma != -1:
        fin = coma
    base = texto[ini:fin]
    pal = _palabras(base)
    if len(pal) > BASE_MAX_PALABRAS:
        base = base[:pal[BASE_MAX_PALABRAS - 1].end()]
    base = _RE_COLA.sub("", " ".join(base.split())).strip()
    c.base = base or None


# ------------------------------------------------------------------------- #
# Entrada                                                                     #
# ------------------------------------------------------------------------- #
def analizar(tramo: str, descripcion: Optional[str] = None,
             titulo: Optional[str] = None) -> list[Cuantia]:
    """Cuantías del tramo, cada una con valor, unidad, base y comparación.
    `descripcion` y `titulo` solo aportan el marcador de coeficiente."""
    cs = detectar_cuantias(tramo)
    lims = limites_de_clausula(tramo)
    for i, c in enumerate(cs):
        ini_cl = max([p + 1 for p in lims if p < c.inicio], default=0)
        fin_cl = min([p for p in lims if p >= c.fin], default=len(tramo))
        fin_prev = cs[i - 1].fin if i > 0 else 0
        ini_sig = cs[i + 1].inicio if i + 1 < len(cs) else len(tramo)
        fijar_comparacion(tramo, c, ini_cl, fin_cl, fin_prev, ini_sig, descripcion, titulo)
        fijar_base(tramo, c, min(fin_cl, ini_sig))
    return cs


def elemento_umbral(c: Cuantia, tramo: str, origen: Optional[str] = None) -> dict:
    """Diccionario con la forma de modelos_r2.ElementoUmbral."""
    fuera = list(c.fuera_de_lista)
    d = {"tramo": tramo, "valor": c.valor, "unidad": c.unidad, "moneda": c.moneda,
         "dias_tipo": c.dias_tipo, "comparacion": c.comparacion, "base": c.base,
         "comparacion_asumida": c.comparacion_asumida, "regla_comparacion": c.regla,
         "origen": origen, "fuera_de_lista": fuera}
    return d
