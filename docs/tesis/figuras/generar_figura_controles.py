#!/usr/bin/env python3
"""Genera la figura F3 (la escalera de controles) del capítulo del esquema,
POR SCRIPT desde los artefactos sellados de los cuatro controles — nunca
dibujada a mano, como F1, F1b y F2.

Fuentes (se LEEN, jamás se editan):
  data/experiment/esq/control/resumen_control_esq.json           — P1
  data/experiment/esq/control/resumen_control_esq_p1bis.json     — P1'
  data/experiment/esq/control/resumen_control_esq_p1ter.json     — P1''
  data/experiment/esq/control/adjudicacion_descubrimiento_cal.md — P-cal.
      El cómputo de P-cal es adjudicación fila por fila; el resumen json de
      esa corrida DECLARA que no computa P-cal, así que el veredicto se lee
      de la tabla «Cómputo contra P-cal» de ese .md y no del json.
  data/experiment/esq/control/resumen_descubrimiento_cal.json    — cruce
      mecánico de P-cal (cero-hallazgos), solo para verificar que la
      adjudicación no se contradice con el conteo automático.
  data/experiment/esq/control/diagnostico_control_esq.md         — el 19/20
      que motiva el segundo control.

NOMENCLATURA — excepción de fuentes, declarada. Los RÓTULOS DE TEXTO no salen
de `main.tex`: la versión de §3.5 que está en el repo no es la vigente (la
subsección se tunea fuera del repo y todavía no se commiteó), así que leerla
daría el vocabulario viejo. La fuente de la nomenclatura es la tabla
`tab:controles` transcrita en TABLA_CONTROLES, más abajo. Los NÚMEROS, en
cambio, siguen saliendo sin excepción de los artefactos sellados, y el script
FRENA si la tabla transcrita y los artefactos no coinciden.

Qué muestra la figura (las cinco piezas del mandato):
  1. Los cuatro controles en secuencia vertical, en el orden en que se
     corrieron.
  2. La REGLA DE ORDEN: sobre cada flecha, el motivo por el que hubo un
     control más. Los rótulos van EN la flecha —el trazo se interrumpe y el
     texto ocupa la interrupción—, no en un cuadro aparte.
  3. Junto a cada control, exigencia declarada y resultado observado por
     grupo, con marca de aprobado / no aprobado.
  4. El CAMBIO DE PAPEL del grupo de diez unidades limpias: corre como
     columna propia a la derecha, cruzando los cuatro controles, y la
     columna se parte donde el papel cambia — en los tres primeros acota
     escrituras indebidas en el canal; en el cuarto, hallazgos falsos de la
     lectura.
  5. La flecha de salida hacia la medición por lectura.

La figura NO repite la tabla del capítulo: la tabla da las celdas sueltas, la
figura da la estructura causal que las encadena.

Distinción en blanco y negro (el informe se imprime sin color): aprobado y no
aprobado se separan por DOS canales redundantes que no son el color —relleno
(disco lleno contra disco hueco) y glifo (tilde contra aspa)—, los dos
dibujados como trazos, sin depender de ninguna fuente. El color es acento
redundante. Las dos vías se separan por el trazo de su banda (continuo contra
raya-punto), tampoco por el tono.

Salida: figura_controles.svg. El PDF vectorial se exporta con rsvg-convert
(ver LEEME_figura_controles.md); el \\includegraphics va sin extensión.

Determinístico: sin fecha de generación, sin aleatoriedad, sin rutas
absolutas. Dos corridas producen bytes idénticos.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

FIG_DIR = Path(__file__).resolve().parent
REPO = FIG_DIR.parents[2]
CTRL = REPO / "data" / "experiment" / "esq" / "control"

F_P1 = CTRL / "resumen_control_esq.json"
F_P1BIS = CTRL / "resumen_control_esq_p1bis.json"
F_P1TER = CTRL / "resumen_control_esq_p1ter.json"
F_CAL_MD = CTRL / "adjudicacion_descubrimiento_cal.md"
F_CAL_JSON = CTRL / "resumen_descubrimiento_cal.json"
F_DIAG = CTRL / "diagnostico_control_esq.md"

SALIDA = FIG_DIR / "figura_controles.svg"

# ========================================================================== #
# 1. Carga de los artefactos + candados                                      #
# ========================================================================== #

P1 = json.loads(F_P1.read_text(encoding="utf-8"))["conteos_por_brazo"]
P1BIS = json.loads(F_P1BIS.read_text(encoding="utf-8"))["conteos_P1bis"]
P1TER_ALL = json.loads(F_P1TER.read_text(encoding="utf-8"))
P1TER = P1TER_ALL["conteos_P1ter"]
CAL_MEC = json.loads(F_CAL_JSON.read_text(encoding="utf-8"))["conteo_mecanico"]

_diag = F_DIAG.read_text(encoding="utf-8")
_m = re.search(r"\*\*(\d+)/(\d+) unidades re-declararon `omisiones_no_prosa`",
               _diag)
assert _m, "el diagnóstico ya no declara el cruce pareado del brazo A"
DIAG_A_RE, DIAG_A_N = int(_m.group(1)), int(_m.group(2))
assert (DIAG_A_RE, DIAG_A_N) == (19, 20), (DIAG_A_RE, DIAG_A_N)

# --- P-cal: la tabla adjudicada, fila por fila ---------------------------- #
_cal_md = F_CAL_MD.read_text(encoding="utf-8")
_bloque = _cal_md.split("## Cómputo contra P-cal", 1)
assert len(_bloque) == 2, "la adjudicación ya no trae «Cómputo contra P-cal»"
CAL: dict[str, dict] = {}
for _ln in _bloque[1].splitlines():
    _c = [x.strip() for x in _ln.strip().strip("|").split("|")]
    if len(_c) != 4 or _c[0] in ("condición", "---"):
        continue
    _obs = re.search(r"\*\*(\d+)/(\d+)\*\*|\*\*(\d+)\*\*", _c[2])
    if not _obs:
        continue
    CAL[_c[0]] = {
        "umbral": _c[1],
        "obs": ((int(_obs.group(1)), int(_obs.group(2))) if _obs.group(1)
                else (int(_obs.group(3)), None)),
        "veredicto": _c[3].replace("*", "").strip(),
    }
assert set(CAL) == {"A′ total", "A′ mitad tipo", "A′ mitad predicado",
                    "Cruces", "C (limpias con espurias)"}, sorted(CAL)
assert CAL["A′ total"]["obs"] == (9, 10)
assert CAL["A′ total"]["umbral"] == "≥7/10"
assert CAL["A′ mitad tipo"]["obs"] == (4, 5)
assert CAL["A′ mitad tipo"]["umbral"] == "≥3/5"
assert CAL["A′ mitad predicado"]["obs"] == (5, 5)
assert CAL["A′ mitad predicado"]["umbral"] == "≥3/5"
assert CAL["Cruces"]["obs"] == (0, None)
assert CAL["C (limpias con espurias)"]["obs"] == (7, 10)
assert CAL["C (limpias con espurias)"]["umbral"] == "≤1/10"
assert CAL["C (limpias con espurias)"]["veredicto"] == "NO pasa"
assert "P-cal FALSADA" in _bloque[1]

# Cruce con el conteo mecánico de la MISMA corrida. Son medidas distintas
# —la mecánica cuenta «trajo hallazgos», la adjudicada «la detección vale»—
# y acá solo se verifica que no se contradicen: la única dopada sin
# detección posible es la que devolvió cero hallazgos.
assert CAL_MEC["n_con_hallazgos"]["A'"] == 9, CAL_MEC["n_con_hallazgos"]
assert CAL_MEC["n_cero_hallazgos"]["A'"] == 1
assert CAL_MEC["cero_hallazgos"]["A'"] == ["dop::tipo::pro::1.1.1"]

# --- Candados sobre los tres primeros peldaños ---------------------------- #
assert (P1["A"]["n"], P1["A"]["emiten_algun_propuesto"]) == (20, 0)
assert P1["A"]["umbral"] == ">=10 de 20" and P1["A"]["pasa"] is False
assert (P1["B"]["n"], P1["B"]["reportan_relacion"]) == (10, 3)
assert P1["B"]["umbral"] == ">=7 de 10" and P1["B"]["pasa"] is False
assert (P1["C"]["n"], P1["C"]["emiten_tipo_propuesto"]) == (10, 0)
assert P1["C"]["pasa"] is True and P1["C"]["umbral"].startswith("<=1 de 10")

for _p, _n in ((P1BIS, "P1'"), (P1TER, "P1''")):
    _a = _p["A_prime"]
    assert (_a["n"], _a["hits_total"]) == (10, 0), _n
    assert _a["umbral_total"] == ">=7 de 10" and _a["pasa"] is False, _n
    assert (_a["mitad_tipo"]["n"], _a["mitad_tipo"]["hits"]) == (5, 0), _n
    assert _a["mitad_tipo"]["umbral"] == ">=3 de 5", _n
    assert (_a["mitad_predicado"]["n"],
            _a["mitad_predicado"]["hits"]) == (5, 0), _n
    assert _a["mitad_predicado"]["umbral"] == ">=3 de 5", _n
    _c = _p["C"]
    assert (_c["n"], _c["emiten_tipo_propuesto"]) == (10, 0), _n
    assert _c["pasa"] is True and _c["umbral"].startswith("<=1 de 10"), _n

# La comparación pareada del tercer peldaño: 20 unidades, ni un cambio.
_par = P1TER_ALL["comparacion_pareada_P1bis"]["por_unidad"]
assert len(_par) == 20, len(_par)
PAR_N = len(_par)
PAR_SIN_CAMBIO = sum(
    1 for u in _par.values()
    if u["p1bis_emite"] == u["p1ter_emite"])
assert PAR_SIN_CAMBIO == 20, PAR_SIN_CAMBIO

# ========================================================================== #
# 2. La tabla vigente (nomenclatura) y el modelo de la figura                #
# ========================================================================== #

# TABLA_CONTROLES es la transcripción de `tab:controles`, y es la ÚNICA fuente
# de los rótulos de texto. Cada `grupo` se dibuja VERBATIM, carácter por
# carácter. Los números que trae se cotejan contra los artefactos sellados en
# el bloque siguiente, y si no coinciden el script FRENA: los rótulos los manda
# la tabla, los números los mandan los artefactos.
#   (control, grupo, signo, exigido, obtenido)
TABLA_CONTROLES = [
    ("Primero", "20 unidades con omisión ya declarada", "ge", 10, 0),
    ("Primero", "10 con una relación rechazada por la matriz", "ge", 7, 3),
    ("Primero", "10 limpias", "le", 1, 0),
    ("Segundo", "10 unidades dopadas", "ge", 7, 0),
    ("Segundo", "10 limpias", "le", 1, 0),
    ("Tercero", "10 dopadas, con las dos frases de cierre neutralizadas",
     "ge", 7, 0),
    ("Tercero", "10 limpias", "le", 1, 0),
    ("Cuarto", "10 dopadas, por lectura en lugar del canal", "ge", 7, 9),
    ("Cuarto", "10 limpias", "le", 1, 7),
]

# Las mismas nueve filas, leídas de los artefactos: (umbral, obtenido, n).
_ART = [
    (P1["A"]["umbral"], P1["A"]["emiten_algun_propuesto"], P1["A"]["n"]),
    (P1["B"]["umbral"], P1["B"]["reportan_relacion"], P1["B"]["n"]),
    (P1["C"]["umbral"], P1["C"]["emiten_tipo_propuesto"], P1["C"]["n"]),
    (P1BIS["A_prime"]["umbral_total"], P1BIS["A_prime"]["hits_total"],
     P1BIS["A_prime"]["n"]),
    (P1BIS["C"]["umbral"], P1BIS["C"]["emiten_tipo_propuesto"],
     P1BIS["C"]["n"]),
    (P1TER["A_prime"]["umbral_total"], P1TER["A_prime"]["hits_total"],
     P1TER["A_prime"]["n"]),
    (P1TER["C"]["umbral"], P1TER["C"]["emiten_tipo_propuesto"],
     P1TER["C"]["n"]),
    (CAL["A′ total"]["umbral"], CAL["A′ total"]["obs"][0],
     CAL["A′ total"]["obs"][1]),
    (CAL["C (limpias con espurias)"]["umbral"],
     CAL["C (limpias con espurias)"]["obs"][0],
     CAL["C (limpias con espurias)"]["obs"][1]),
]


def _parse_umbral(u: str) -> tuple[str, int, int]:
    """«>=10 de 20» y «≥7/10» -> (signo, exigido, denominador)."""
    signo = "ge" if (">=" in u or "≥" in u) else "le"
    nums = [int(x) for x in re.findall(r"\d+", u.split("(")[0])]
    return signo, nums[0], nums[1]


# El cotejo tabla ↔ artefacto. Si alguna fila discrepa, no se dibuja ninguno
# de los dos: se frena y se lauda.
DENOM: list[int] = []
for (_c, _g, _sg, _ex, _ob), (_u, _o, _n) in zip(TABLA_CONTROLES, _ART):
    _s, _e, _d = _parse_umbral(_u)
    assert (_s, _e, _o, _d) == (_sg, _ex, _ob, _n), (
        f"la tabla vigente y el artefacto sellado discrepan en «{_g}»: "
        f"tabla {_sg}{_ex}/{_ob} · artefacto {_u} / {_o} sobre {_n}")
    DENOM.append(_n)
assert len(TABLA_CONTROLES) == 9, len(TABLA_CONTROLES)

GRUPOS_TABLA = {g for _, g, _, _, _ in TABLA_CONTROLES}


def fila(i: int) -> tuple[str, str, str, bool]:
    """Fila i de la tabla, con su rótulo VERBATIM y sus números del artefacto."""
    _c, g, sg, ex, ob = TABLA_CONTROLES[i]
    n = DENOM[i]
    umb = f"{'≥' if sg == 'ge' else '≤'} {ex} de {n}"
    pasa = (ob >= ex) if sg == "ge" else (ob <= ex)
    return g, umb, f"{ob} de {n}", pasa


def submitad(texto: str, clave: str) -> tuple[str, str, str, bool]:
    """Las dos mitades del cuarto control: no están en la tabla, y se dibujan
    como desglose de su fila, no como grupos aparte."""
    ob, n = CAL[clave]["obs"]
    _s, ex, dn = _parse_umbral(CAL[clave]["umbral"])
    return texto, f"≥ {ex} de {dn}", f"{ob} de {n}", ob >= ex


# Las mitades de los controles segundo y tercero NO se dibujan: son 0 de 5 y
# 0 de 5 en cada uno, redundantes con el 0 de 10 de su fila total. Las del
# cuarto sí, porque 4 de 5 y 5 de 5 no se deducen del 9 de 10.
assert (P1BIS["A_prime"]["mitad_tipo"]["hits"],
        P1BIS["A_prime"]["mitad_predicado"]["hits"]) == (0, 0)
assert (P1TER["A_prime"]["mitad_tipo"]["hits"],
        P1TER["A_prime"]["mitad_predicado"]["hits"]) == (0, 0)

PELDANOS = [
    {
        "n": "1",
        "titulo": "Control primero · tres grupos",
        "filas": [fila(0), fila(1)],
        "nota": None,
        "carril": fila(2),
    },
    {
        "n": "2",
        "titulo": "Control segundo",
        "filas": [fila(3)],
        "nota": "las diez plantadas entraron deformadas dentro del esquema",
        "carril": fila(4),
    },
    {
        "n": "3",
        "titulo": "Control tercero",
        "filas": [fila(5)],
        "nota": f"{PAR_SIN_CAMBIO} de {PAR_N} unidades sin un solo cambio "
                f"frente al control segundo",
        "carril": fila(6),
    },
    {
        "n": "4",
        "titulo": "Control cuarto",
        "filas": [fila(7),
                  submitad("de ellas, las 5 que piden un tipo",
                           "A′ mitad tipo"),
                  submitad("de ellas, las 5 que piden una relación",
                           "A′ mitad predicado")],
        "nota": "cita el pasaje y explica el desajuste; "
                f"{CAL['Cruces']['obs'][0]} cruces tipo/relación",
        "carril": fila(8),
    },
]

# Guarda de verbatim: todo rótulo de grupo dibujado tiene que ser, carácter
# por carácter, una celda de la columna «Grupo» de la tabla. Las dos mitades
# del cuarto control se declaran aparte porque son desglose, no grupo.
DESGLOSE = {"de ellas, las 5 que piden un tipo",
            "de ellas, las 5 que piden una relación"}
for _p in PELDANOS:
    for _d, _, _, _ in _p["filas"] + [_p["carril"]]:
        assert _d in GRUPOS_TABLA or _d in DESGLOSE, (
            f"rótulo que no es verbatim de la columna «Grupo»: {_d!r}")

# La regla de orden: por qué hubo un control más. Cada motivo sale del
# artefacto que lo funda; el LEEME cita la línea de cada uno.
MOTIVOS = [
    "Ningún grupo medía el canal: uno midió la regla de omisión "
    f"({DIAG_A_RE} de {DIAG_A_N}) y el otro se eligió por conducta previa. "
    "Falta contenido plantado.",
    "Corregida la descripción del canal, la única explicación en pie es el "
    "lenguaje de cierre del prompt. Declarado antes de correr.",
    "Los cierres neutralizados no movieron una sola unidad: el canal abierto "
    "queda cerrado sin un tercer retoque, escrito de antemano.",
]
MOTIVO_SALIDA = ("El instrumento ve lo plantado pero inunda de falsos el "
                 "texto limpio: el censo automático queda cerrado.")

VIAS = [
    (0, "el canal abierto — extraer y de paso avisar", True),
    (3, "la consulta separada — preguntar en una llamada aparte", False),
]

CARRIL_TIT = "10 limpias"          # verbatim de la columna «Grupo»
CARRIL_SUB = "el mismo grupo en los cuatro controles"
CARRIL_PAPEL_1 = "en los tres primeros acota escrituras indebidas en el canal"
CARRIL_PAPEL_2 = "en el cuarto acota hallazgos falsos de la lectura"
CARRIL_CORTE = "el papel cambia acá"

SALIDA_TIT = "MEDICIÓN DE COBERTURA POR LECTURA"
SALIDA_SUB = ("una ficha por unidad sobre los diez documentos del "
              "conjunto de prueba")

PIE = "los cuatro controles corren sobre el conjunto de desarrollo"

# ========================================================================== #
# 3. Tipografía y paleta                                                     #
# ========================================================================== #

LINEWIDTH_MM = 150.0   # a4 con márgenes laterales de 3 cm (main.tex:9)
PT_MIN = 8.0

TIPO_SANS = "Helvetica,Arial,sans-serif"

FS_TIT = 25            # título del peldaño y de la caja de salida
FS_TXT = 22            # filas de la tabla, carril, rótulos de flecha
FS_CHICO = 22          # notas, veredicto, bandas, leyenda — mismo piso

LH = 25.0              # interlínea

C_TINTA = "#16181d"
C_GRIS = "#585d66"
C_LINEA = "#9aa0a8"
C_SUAVE = "#f2f3f5"
C_OK = "#1f6f5c"       # acento redundante del aprobado
C_NO = "#8c2f39"       # acento redundante del no aprobado
BLANCO = "#ffffff"

_W = {
    " ": 278, "!": 278, '"': 355, "#": 556, "$": 556, "%": 889, "&": 667,
    "'": 191, "(": 333, ")": 333, "*": 389, "+": 584, ",": 278, "-": 333,
    ".": 278, "/": 278, ":": 278, ";": 278, "?": 556, "@": 1015, "[": 278,
    "]": 278, "_": 556, "{": 334, "|": 260, "}": 334, "·": 278, "«": 333,
    "»": 333, "—": 1000, "–": 556, "→": 1000, "≥": 549, "≤": 549,
    "′": 191, "″": 355, "¿": 556, "¡": 278,
}
for _c in "0123456789":
    _W[_c] = 556
for _c, _w in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                  (667, 667, 722, 722, 667, 611, 778, 722, 278, 500, 667, 556,
                   833, 722, 778, 667, 778, 722, 667, 611, 722, 667, 944, 667,
                   667, 611)):
    _W[_c] = _w
for _c, _w in zip("abcdefghijklmnopqrstuvwxyz",
                  (556, 556, 500, 556, 556, 278, 556, 556, 222, 222, 500, 222,
                   833, 556, 556, 556, 556, 333, 500, 278, 556, 500, 722, 500,
                   500, 500)):
    _W[_c] = _w
for _a, _b in (("á", "a"), ("é", "e"), ("ó", "o"), ("ú", "u"), ("ñ", "n"),
               ("ü", "u"), ("Á", "A"), ("É", "E"), ("Í", "I"), ("Ó", "O"),
               ("Ú", "U"), ("Ñ", "N")):
    _W[_a] = _W[_b]
_W["í"] = 278


def ancho(texto: str, fs: float, bold: bool = False) -> float:
    tot = sum(_W.get(c, 556) for c in texto)
    return tot / 1000.0 * fs * (1.09 if bold else 1.0)


def envolver(texto: str, fs: float, maxw: float,
             bold: bool = False) -> list[str]:
    """Corta en palabras. FRENA si una palabra sola no entra: nunca recorta
    ni achica en silencio — el remedio es acortar el texto o ensanchar la
    caja, y las dos son decisiones, no efectos colaterales."""
    lineas: list[str] = []
    actual = ""
    for pal in texto.split():
        assert ancho(pal, fs, bold) <= maxw + 0.5, (
            f"palabra que no entra en {maxw:.0f} px a {fs} pt: {pal!r}")
        cand = f"{actual} {pal}".strip()
        if ancho(cand, fs, bold) <= maxw:
            actual = cand
        else:
            lineas.append(actual)
            actual = pal
    if actual:
        lineas.append(actual)
    return lineas


# ========================================================================== #
# 4. Geometría                                                               #
# ========================================================================== #

MARGEN = 34.0
GUTTER = 26.0          # aire entre la columna de peldaños y el carril

W_CARRIL = 290.0
W_PELD = 760.0

X_PELD = MARGEN
X_CARRIL = X_PELD + W_PELD + GUTTER
ANCHO_SVG = X_CARRIL + W_CARRIL + MARGEN

PAD = 12.0             # relleno interno de las cajas
H_FILA = 28.0          # alto de una fila de la tabla del peldaño
H_BANDA = 32.0         # alto de la banda de vía
AIRE_FLECHA = 14.0     # tramo de flecha visible a cada lado del rótulo

# Columnas de la tabla del peldaño
COL_TXT = X_PELD + PAD                 # borde izquierdo de la descripción
COL_MARCA = X_PELD + W_PELD - PAD - 14.0   # centro del disco
COL_OBS = COL_MARCA - 28.0             # borde derecho del observado
W_OBS = 84.0                           # «0 de 20» en negrita
COL_UMB = COL_OBS - W_OBS - 12.0       # borde derecho del umbral
W_UMB = 108.0                          # «≥ 10 de 20»
W_DESC = COL_UMB - W_UMB - 14.0 - COL_TXT

# Columnas del carril
CAR_UMB = X_CARRIL + PAD
CAR_MARCA = X_CARRIL + W_CARRIL - PAD - 14.0
CAR_OBS = CAR_MARCA - 28.0
W_CAR_OBS = 84.0
W_CAR_UMB = CAR_OBS - W_CAR_OBS - 10.0 - CAR_UMB

W_ROTULO = W_PELD + 14.0               # ancho de los rótulos de flecha
assert W_ROTULO <= W_PELD + GUTTER - 10.0, "el rótulo invade el carril"
W_CAJA = W_PELD - 2 * PAD              # ancho útil dentro de un peldaño
W_CAR = W_CARRIL - 2 * PAD             # ancho útil dentro del carril

# --- Envolturas (se hacen antes de medir alturas) -------------------------- #
for _p in PELDANOS:
    _p["titulo_ls"] = envolver(_p["titulo"], FS_TIT, W_CAJA, bold=True)
    _p["nota_ls"] = (envolver(_p["nota"], FS_CHICO, W_CAJA)
                     if _p["nota"] else [])
    assert len(_p["titulo_ls"]) == 1, _p["titulo_ls"]
    assert len(_p["nota_ls"]) <= 1, _p["nota_ls"]
    # el rótulo de grupo se dibuja verbatim; si no entra en una línea,
    # envuelve y su fila crece — no se recorta ni se abrevia
    _p["filas_ls"] = [envolver(d, FS_TXT, W_DESC) for d, _, _, _ in _p["filas"]]
    for _ls in _p["filas_ls"]:
        assert len(_ls) <= 2, _ls

MOTIVOS_LS = [envolver(m, FS_TXT, W_ROTULO) for m in MOTIVOS]
SALIDA_LS = envolver(MOTIVO_SALIDA, FS_TXT, W_ROTULO)
for _ls in MOTIVOS_LS + [SALIDA_LS]:
    assert len(_ls) <= 2, (
        "un rótulo de flecha pasó de dos líneas; acortar el texto o "
        f"ensanchar la columna: {_ls}")
VIAS_LS = [(i, envolver(t, FS_CHICO, W_CAJA - 6, bold=True), c)
           for (i, t, c) in VIAS]
for _i, _ls, _c in VIAS_LS:
    assert len(_ls) == 1, _ls
CARRIL_TIT_LS = envolver(CARRIL_TIT, FS_CHICO, W_CAR, bold=True)
CARRIL_SUB_LS = envolver(CARRIL_SUB, FS_CHICO, W_CAR)
CARRIL_P1_LS = envolver(CARRIL_PAPEL_1, FS_CHICO, W_CAR)
CARRIL_P2_LS = envolver(CARRIL_PAPEL_2, FS_CHICO, W_CAR)
CORTE_LS = envolver(CARRIL_CORTE, FS_CHICO, W_CAR, bold=True)
SAL_SUB_LS = envolver(SALIDA_SUB, FS_CHICO, W_CAJA)
assert len(CORTE_LS) == 1, CORTE_LS


def alto_fila(ls: list[str]) -> float:
    return H_FILA + (len(ls) - 1) * (LH - 3.0)


def alto_peldano(p: dict) -> float:
    h = PAD + FS_TIT + 12.0 + sum(alto_fila(ls) for ls in p["filas_ls"])
    if p["nota_ls"]:
        h += 9.0 + len(p["nota_ls"]) * LH
    return h + PAD - 2.0


# El título del carril tiene que caber por encima de su primera fila. Las dos
# glosas de papel ya no van acá: viven pegadas al corte, que es donde el papel
# cambia, y así no hace falta abrir aire arriba de toda la figura.
ALTO_CAB_CARRIL = (PAD + len(CARRIL_TIT_LS) * LH
                   + len(CARRIL_SUB_LS) * LH + 4.0)
_h1 = alto_peldano(PELDANOS[0])
EXTRA_TOP = max(0.0, ALTO_CAB_CARRIL - (H_BANDA + 12.0 + _h1 / 2.0 - 20.0))

# --- Recorrido vertical: todas las y se asignan antes de dibujar ----------- #
_y = MARGEN + EXTRA_TOP
GEOM: list[dict] = []
BANDAS: list[tuple[float, float, list[str], bool]] = []
FLECHAS: list[dict] = []


def _banda_si_toca(i: int) -> None:
    global _y
    for (a, ls, cont) in VIAS_LS:
        if i == a:
            BANDAS.append((_y, H_BANDA, ls, cont))
            _y += H_BANDA + 12.0


for i, p in enumerate(PELDANOS):
    _banda_si_toca(i)
    h = alto_peldano(p)
    GEOM.append({"y": _y, "h": h, "p": p})
    _y += h
    lineas = MOTIVOS_LS[i] if i < len(PELDANOS) - 1 else SALIDA_LS
    h_gap = AIRE_FLECHA * 2 + len(lineas) * LH + 12.0
    FLECHAS.append({"y0": _y, "h": h_gap, "lineas": lineas})
    _y += h_gap

Y_SALIDA = _y
H_SALIDA = PAD + FS_TIT + 8.0 + len(SAL_SUB_LS) * LH + PAD - 6.0
_y += H_SALIDA + 22.0

Y_LEY = _y
H_LEY = FS_CHICO + 16.0
_y += H_LEY

ALTO_SVG = _y + MARGEN

# ========================================================================== #
# 5. Guardas de maquetación                                                  #
# ========================================================================== #

_desbordes: list[str] = []


def chequear(texto: str, fs: float, disponible: float, donde: str,
             bold: bool = False) -> None:
    w = ancho(texto, fs, bold)
    if w > disponible + 0.5:
        _desbordes.append(f"{donde}: {w:.1f} px > {disponible:.1f} px "
                          f"— {texto!r}")


for g in GEOM:
    p = g["p"]
    chequear(p["titulo_ls"][0], FS_TIT, W_CAJA,
             f"título del control {p['n']}", bold=True)
    for (_d, umb, obs, _ok), _ls in zip(p["filas"], p["filas_ls"]):
        for ln in _ls:
            chequear(ln, FS_TXT, W_DESC, f"rótulo de grupo, control {p['n']}")
        chequear(umb, FS_TXT, W_UMB, f"exigencia, control {p['n']}")
        chequear(obs, FS_TXT, W_OBS, f"observado, control {p['n']}", bold=True)
    for ln in p["nota_ls"]:
        chequear(ln, FS_CHICO, W_CAJA, f"nota, control {p['n']}")
    _d_c, umb_c, obs_c, _ = p["carril"]
    chequear(_d_c, FS_TXT, W_CAR - W_CAR_OBS - 40,
             f"rótulo de grupo del carril, control {p['n']}")
    chequear(umb_c, FS_TXT, W_CAR_UMB, f"exigencia del carril, control {p['n']}")
    chequear(obs_c, FS_TXT, W_CAR_OBS,
             f"observado del carril, control {p['n']}", bold=True)

for _ls in MOTIVOS_LS + [SALIDA_LS]:
    for ln in _ls:
        chequear(ln, FS_TXT, W_ROTULO, "rótulo de flecha")
for (_a, _ls, _c) in VIAS_LS:
    chequear(_ls[0], FS_CHICO, W_CAJA - 6, "banda de vía", bold=True)
for ln in (CARRIL_TIT_LS + CARRIL_SUB_LS + CARRIL_P1_LS
           + CARRIL_P2_LS + CORTE_LS):
    chequear(ln, FS_CHICO, W_CAR, "carril")
chequear(SALIDA_TIT, FS_TIT, W_CAJA, "salida", bold=True)
for ln in SAL_SUB_LS:
    chequear(ln, FS_CHICO, W_CAJA, "salida (subtítulo)")

assert not _desbordes, ("texto que no entra en su caja:\n  "
                        + "\n  ".join(_desbordes))

# --- Piso tipográfico ------------------------------------------------------ #


def pt_impreso(fs: float) -> float:
    """Cuerpo en puntos IMPRESOS al entrar a width=\\linewidth."""
    return fs / ANCHO_SVG * LINEWIDTH_MM / 25.4 * 72.0


_CUERPOS = {"título de control": FS_TIT, "fila de tabla": FS_TXT,
            "nota / banda / glosa / leyenda": FS_CHICO}
_flojos = {k: round(pt_impreso(v), 2) for k, v in _CUERPOS.items()
           if pt_impreso(v) < PT_MIN}
assert not _flojos, (
    f"tipografía por debajo de {PT_MIN} pt impresos a {LINEWIDTH_MM} mm: "
    f"{_flojos} (ancho del lienzo {ANCHO_SVG:.1f} px)")

# --- Bloques que no se pisan ----------------------------------------------- #
_ocupado: list[tuple[float, float, str]] = []
for g in GEOM:
    _ocupado.append((g["y"], g["y"] + g["h"], f"control {g['p']['n']}"))
for (y0, h, _ls, _c) in BANDAS:
    _ocupado.append((y0, y0 + h, "banda de vía"))
for fl in FLECHAS:
    _ocupado.append((fl["y0"], fl["y0"] + fl["h"], "flecha"))
_ocupado.append((Y_SALIDA, Y_SALIDA + H_SALIDA, "salida"))
_ocupado.sort()
for (a0, a1, na), (b0, b1, nb) in zip(_ocupado, _ocupado[1:]):
    assert a1 <= b0 + 0.01, f"{na} y {nb} se solapan ({a1:.1f} > {b0:.1f})"

# El corte del carril tiene que caer ENTRE el control tercero y el cuarto: si
# dejara de hacerlo, la figura estaría afirmando otro cambio de papel. Las dos
# glosas se cuelgan del corte —una arriba y otra abajo—, que es donde el
# cambio ocurre.
_Y_CAR0 = GEOM[0]["y"] - H_BANDA - 12.0 - EXTRA_TOP
_Y_CAR1 = GEOM[-1]["y"] + GEOM[-1]["h"]
# La fila del carril de un control es una caja de 40 px centrada en su medio.
_fila_carril = [g["y"] + g["h"] / 2.0 for g in GEOM]
_hueco0 = _fila_carril[2] + 20.0     # borde inferior de la tercera fila
_hueco1 = _fila_carril[3] - 20.0     # borde superior de la cuarta

_ALTO_G1 = len(CARRIL_P1_LS) * LH
_ALTO_G2 = len(CARRIL_P2_LS) * LH
AIRE_CORTE = 22.0     # aire a cada lado del rótulo del corte
_ALTO_CORTE = _ALTO_G1 + AIRE_CORTE + LH + AIRE_CORTE + _ALTO_G2
assert _ALTO_CORTE <= _hueco1 - _hueco0, (
    f"las dos glosas del papel no entran en el hueco del corte: "
    f"{_ALTO_CORTE:.0f} px sobre {_hueco1 - _hueco0:.0f} px")
# centrado en el hueco: la glosa 1, el rótulo del corte, la línea, la glosa 2
_Y_G1 = _hueco0 + (_hueco1 - _hueco0 - _ALTO_CORTE) / 2.0
Y_CORTE = _Y_G1 + _ALTO_G1 + AIRE_CORTE + LH
assert GEOM[2]["y"] + GEOM[2]["h"] < Y_CORTE < GEOM[3]["y"], (
    "el corte del carril se salió de entre el control tercero y el cuarto")
assert _Y_CAR0 + ALTO_CAB_CARRIL <= _fila_carril[0] - 20.0 + 0.5, (
    "la cabecera del carril invade su primera fila")

# ========================================================================== #
# 6. Dibujo                                                                  #
# ========================================================================== #

OUT: list[str] = []


def add(s: str) -> None:
    OUT.append(s)


def f(v: float) -> str:
    return f"{v:.2f}".rstrip("0").rstrip(".")


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def texto(x: float, y: float, s: str, fs: float, color: str = C_TINTA,
          bold: bool = False, anchor: str = "start",
          italic: bool = False) -> None:
    est = (f'font-family="{TIPO_SANS}" font-size="{f(fs)}" fill="{color}"'
           + (' font-weight="bold"' if bold else "")
           + (' font-style="italic"' if italic else "")
           + (f' text-anchor="{anchor}"' if anchor != "start" else ""))
    add(f'<text x="{f(x)}" y="{f(y)}" {est}>{esc(s)}</text>')


def caja(x: float, y: float, w: float, h: float, relleno: str = BLANCO,
         borde: str = C_TINTA, an: float = 2.0, r: float = 7.0,
         dash: str | None = None) -> None:
    d = f' stroke-dasharray="{dash}"' if dash else ""
    add(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" '
        f'rx="{f(r)}" fill="{relleno}" stroke="{borde}" '
        f'stroke-width="{f(an)}"{d}/>')


def marca(cx: float, cy: float, ok: bool) -> None:
    """Aprobado / no aprobado SIN depender del color ni de ninguna fuente.

    Dos canales redundantes: relleno (lleno contra hueco) y glifo (tilde
    contra aspa), los dos dibujados como trazos.
    """
    r = 12.5
    if ok:
        add(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="{C_OK}" '
            f'stroke="{C_TINTA}" stroke-width="1.4"/>')
        add(f'<path d="M {f(cx - 6.2)} {f(cy + 0.4)} '
            f'L {f(cx - 2.0)} {f(cy + 5.2)} L {f(cx + 6.6)} {f(cy - 5.6)}" '
            f'fill="none" stroke="{BLANCO}" stroke-width="3.2" '
            f'stroke-linecap="round" stroke-linejoin="round"/>')
    else:
        add(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(r)}" fill="{BLANCO}" '
            f'stroke="{C_NO}" stroke-width="2.8"/>')
        for (dx0, dy0, dx1, dy1) in ((-5.3, -5.3, 5.3, 5.3),
                                     (-5.3, 5.3, 5.3, -5.3)):
            add(f'<path d="M {f(cx + dx0)} {f(cy + dy0)} '
                f'L {f(cx + dx1)} {f(cy + dy1)}" stroke="{C_NO}" '
                f'stroke-width="3.0" stroke-linecap="round"/>')


add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{f(ANCHO_SVG)}" '
    f'height="{f(ALTO_SVG)}" viewBox="0 0 {f(ANCHO_SVG)} {f(ALTO_SVG)}">')
add(f'<rect width="{f(ANCHO_SVG)}" height="{f(ALTO_SVG)}" fill="{BLANCO}"/>')
add(f'<defs><marker id="pta" viewBox="0 0 10 10" refX="9" refY="5" '
    f'markerWidth="6" markerHeight="6" orient="auto-start-reverse">'
    f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{C_TINTA}"/></marker></defs>')

# --- 6.a  La columna del grupo de las diez limpias, al fondo --------------- #
caja(X_CARRIL, _Y_CAR0, W_CARRIL, _Y_CAR1 - _Y_CAR0, relleno=C_SUAVE,
     borde=C_LINEA, an=1.8, r=10.0)
_yy = _Y_CAR0 + PAD
for ln in CARRIL_TIT_LS:
    texto(X_CARRIL + PAD, _yy + FS_CHICO * 0.82, ln, FS_CHICO, C_TINTA,
          bold=True)
    _yy += LH
for ln in CARRIL_SUB_LS:
    texto(X_CARRIL + PAD, _yy + FS_CHICO * 0.82, ln, FS_CHICO, C_GRIS,
          italic=True)
    _yy += LH

# Las dos glosas del papel van colgadas del corte, arriba y abajo, porque el
# corte es donde el papel cambia.
_yy = _Y_G1
for ln in CARRIL_P1_LS:
    texto(X_CARRIL + PAD, _yy + FS_CHICO * 0.82, ln, FS_CHICO, C_GRIS)
    _yy += LH
texto(X_CARRIL + W_CARRIL / 2.0, Y_CORTE - 11.0, CORTE_LS[0], FS_CHICO,
      C_TINTA, bold=True, anchor="middle")
add(f'<path d="M {f(X_CARRIL + 8)} {f(Y_CORTE)} '
    f'L {f(X_CARRIL + W_CARRIL - 8)} {f(Y_CORTE)}" stroke="{C_TINTA}" '
    f'stroke-width="2.6" stroke-dasharray="9 5"/>')
_yy = Y_CORTE + AIRE_CORTE
for ln in CARRIL_P2_LS:
    texto(X_CARRIL + PAD, _yy + FS_CHICO * 0.82, ln, FS_CHICO, C_GRIS)
    _yy += LH

# Espina de la columna: las filas son UN mismo grupo recorriendo los cuatro
# controles, no cuatro mediciones sueltas. Se dibuja SOLO en los huecos entre
# filas consecutivas, y el hueco donde cae el corte queda vacío a propósito:
# ahí el grupo cambia de papel, y la continuidad se interrumpe con él. El
# hueco saltado es además el que aloja las dos glosas, de modo que la espina
# nunca cruza texto.
_esp_x = X_CARRIL + W_CARRIL / 2.0
_saltados = 0
for _k in range(len(GEOM) - 1):
    _a = GEOM[_k]["y"] + GEOM[_k]["h"] / 2.0 + 20.0
    _b = GEOM[_k + 1]["y"] + GEOM[_k + 1]["h"] / 2.0 - 20.0
    if _a < Y_CORTE < _b:
        _saltados += 1
        continue
    add(f'<path d="M {f(_esp_x)} {f(_a)} L {f(_esp_x)} {f(_b)}" '
        f'stroke="{C_LINEA}" stroke-width="2.2"/>')
assert _saltados == 1, (
    "el corte del carril tiene que caer en exactamente un hueco entre filas, "
    f"y cayó en {_saltados}")

# --- 6.b  Bandas de vía ---------------------------------------------------- #
for (y0, h, ls, continuo) in BANDAS:
    caja(X_PELD, y0, W_PELD, h, relleno=BLANCO, borde=C_TINTA, an=2.0, r=5.0,
         dash=None if continuo else "11 5")
    texto(X_PELD + 15, y0 + h / 2.0 + FS_CHICO * 0.34, ls[0], FS_CHICO,
          C_TINTA, bold=True)

# --- 6.c  Peldaños --------------------------------------------------------- #
for g in GEOM:
    p, y, h = g["p"], g["y"], g["h"]
    caja(X_PELD, y, W_PELD, h, relleno=BLANCO, borde=C_TINTA, an=2.6, r=9.0)

    texto(COL_TXT, y + PAD + FS_TIT * 0.82, p["titulo_ls"][0], FS_TIT,
          C_TINTA, bold=True)

    yf = y + PAD + FS_TIT + 12.0
    for (_d, umb, obs, ok), ls in zip(p["filas"], p["filas_ls"]):
        hf = alto_fila(ls)
        cy = yf + hf / 2.0
        add(f'<path d="M {f(COL_TXT)} {f(yf)} L {f(X_PELD + W_PELD - PAD)} '
            f'{f(yf)}" stroke="{C_LINEA}" stroke-width="1"/>')
        _yl = cy - (len(ls) - 1) * (LH - 3.0) / 2.0
        for ln in ls:
            texto(COL_TXT, _yl + FS_TXT * 0.34, ln, FS_TXT, C_TINTA)
            _yl += LH - 3.0
        texto(COL_UMB, cy + FS_TXT * 0.34, umb, FS_TXT, C_GRIS, anchor="end")
        texto(COL_OBS, cy + FS_TXT * 0.34, obs, FS_TXT, C_TINTA, bold=True,
              anchor="end")
        marca(COL_MARCA, cy, ok)
        yf += hf

    if p["nota_ls"]:
        yf += 9.0
        for ln in p["nota_ls"]:
            texto(COL_TXT, yf + FS_CHICO * 0.82, ln, FS_CHICO, C_GRIS,
                  italic=True)
            yf += LH

    _d_c, umb_c, obs_c, ok_c = p["carril"]
    cyc = y + h / 2.0
    add(f'<path d="M {f(X_PELD + W_PELD)} {f(cyc)} L {f(X_CARRIL)} '
        f'{f(cyc)}" stroke="{C_LINEA}" stroke-width="1.4" '
        f'stroke-dasharray="4 4"/>')
    caja(X_CARRIL + 8, cyc - 20.0, W_CARRIL - 16, 40.0, relleno=BLANCO,
         borde=C_LINEA, an=1.5, r=6.0)
    texto(CAR_UMB, cyc + FS_TXT * 0.34, umb_c, FS_TXT, C_GRIS)
    texto(CAR_OBS, cyc + FS_TXT * 0.34, obs_c, FS_TXT, C_TINTA, bold=True,
          anchor="end")
    marca(CAR_MARCA, cyc, ok_c)

# --- 6.d  Flechas con su motivo EN el trazo -------------------------------- #
_cx = X_PELD + W_PELD / 2.0
for fl in FLECHAS:
    y0, hh, ls = fl["y0"], fl["h"], fl["lineas"]
    y_rot0 = y0 + AIRE_FLECHA + 6.0
    add(f'<path d="M {f(_cx)} {f(y0)} L {f(_cx)} {f(y_rot0 - 3)}" '
        f'stroke="{C_TINTA}" stroke-width="2.6"/>')
    yy = y_rot0
    for ln in ls:
        texto(_cx, yy + FS_TXT * 0.82, ln, FS_TXT, C_TINTA, anchor="middle")
        yy += LH
    add(f'<path d="M {f(_cx)} '
        f'{f(y0 + AIRE_FLECHA + 6.0 + len(ls) * LH)} '
        f'L {f(_cx)} {f(y0 + hh)}" stroke="{C_TINTA}" stroke-width="2.6" '
        f'marker-end="url(#pta)"/>')

# --- 6.e  Caja de salida --------------------------------------------------- #
caja(X_PELD, Y_SALIDA, W_PELD, H_SALIDA, relleno=C_SUAVE, borde=C_TINTA,
     an=3.2, r=9.0)
texto(X_PELD + W_PELD / 2.0, Y_SALIDA + PAD + FS_TIT * 0.82, SALIDA_TIT,
      FS_TIT, C_TINTA, bold=True, anchor="middle")
_ys = Y_SALIDA + PAD + FS_TIT + 8.0
for ln in SAL_SUB_LS:
    texto(X_PELD + W_PELD / 2.0, _ys + FS_CHICO * 0.82, ln, FS_CHICO, C_GRIS,
          anchor="middle")
    _ys += LH

# --- 6.f  Leyenda de las dos marcas + pie ---------------------------------- #
_lx = X_PELD + 4.0
_ly = Y_LEY + H_LEY / 2.0
for ok, rot in ((True, "alcanza su umbral"), (False, "no lo alcanza")):
    marca(_lx + 13, _ly, ok)
    texto(_lx + 32, _ly + FS_CHICO * 0.34, rot, FS_CHICO, C_GRIS)
    _lx += 32 + ancho(rot, FS_CHICO) + 34
texto(ANCHO_SVG - MARGEN, _ly + FS_CHICO * 0.34, PIE, FS_CHICO, C_GRIS,
      anchor="end")
assert _lx < ANCHO_SVG - MARGEN - ancho(PIE, FS_CHICO) - 20, (
    "la leyenda pisa el pie")

add("</svg>")
SALIDA.write_text("\n".join(OUT) + "\n", encoding="utf-8")

print(f"escrito {SALIDA.relative_to(REPO)}  "
      f"{ANCHO_SVG:.1f} x {ALTO_SVG:.1f} px")
print("cuerpos impresos a width=\\linewidth "
      f"({LINEWIDTH_MM:.0f} mm): "
      + " · ".join(f"{k} {pt_impreso(v):.2f} pt"
                   for k, v in _CUERPOS.items()))
print(f"alto impreso: {ALTO_SVG / ANCHO_SVG * LINEWIDTH_MM:.1f} mm")
