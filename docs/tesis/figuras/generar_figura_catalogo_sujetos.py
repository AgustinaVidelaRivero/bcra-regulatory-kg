#!/usr/bin/env python3
"""Genera la figura F2 (catálogo de sujetos) del capítulo del esquema, POR
SCRIPT desde los artefactos sellados — nunca dibujada a mano.

Fuentes (se LEEN, jamás se editan):
  data/experiment/grafo_v2/esquema_v2_clases.json  — catálogo v2.0: 58 clases
      + 7 instancias en `clases`, 5 roles de alcance en `roles`.
  data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json — grafo vigente:
      contra él se verifica que CADA arista dibujada existe (57 subclase_de,
      7 instancia_de, 17 miembro_de, 1 parte_de) y que el nodo de norma y el
      del rol existen con las etiquetas que se dibujan.

Qué muestra la figura (cinco piezas):
  1. La raíz `Sujetos` con sus 4 hijos directos — es un árbol único.
  2. La rama a profundidad completa que cita la prosa:
     Sujetos → Sujetos regulados → Entidades financieras → Bancos →
     Bancos comerciales (verificada contra el artefacto: la cadena real es
     exactamente esa).
  3. Ramas hermanas COLAPSADAS: cada rama no expandida es un solo nodo que
     declara cuántas clases contiene. Dibujadas + colapsadas = 58, asertado.
  4. Instancias: `Organismos públicos` con BCRA y SEFyC colgando por
     `instancia_de`, más un nodo colapsado con las 5 restantes. Forma propia
     (píldora), distinta de las clases.
  5. La indirección: el rol de alcance «Sujetos obligados (Protección de
     usuarios)» dibujado FUERA del árbol, con las aristas `miembro_de` que
     entran desde las clases que lo componen, y una norma real del TO de
     Protección apuntándolo con `aplica_a`. El camino
     norma → rol → clase → subclase se sigue con el dedo.

Poda declarada (regla del mandato: podar antes que achicar la tipografía):
  el rol tiene 7 miembros y se dibujan 5; los 2 restantes (PSPCP y PSI) caen
  dentro del nodo colapsado «+15 clases» de `Sujetos regulados`. El propio
  rol lo declara en su caja («7 miembros · 5 dibujados»). De las 7 instancias
  se dibujan 2 y se declaran 5.

Distinción en blanco y negro (el informe se imprime sin color): las tres
formas de entrada del catálogo se diferencian por FORMA y TRAZO, no por
color — clase = rectángulo de trazo continuo; clase colapsada = rectángulo
apilado de trazo discontinuo; instancia = píldora; rol = hexágono de trazo
raya-punto; norma = rectángulo con esquina plegada. Las cuatro relaciones se
diferencian por patrón de línea Y por forma de punta, y todas llevan su
nombre sobre el trazo.

Sentido de las flechas: en las cuatro relaciones el `source` es el hijo, el
miembro o la norma, y el `target` el padre o el rol; la punta señala
entonces al padre / al rol, como en la generalización UML. En el árbol
dibujado de izquierda a derecha eso hace que las puntas apunten hacia la
izquierda; es la dirección del artefacto y así se dibuja.

Salida: figura_catalogo_sujetos.svg. El PNG se exporta aparte con
rsvg-convert (ver LEEME_figura_catalogo_sujetos.md).

Determinístico: sin fechas, sin aleatoriedad, sin rutas absolutas; toda
iteración sobre conjuntos pasa por sorted() o por listas declaradas. Dos
corridas producen bytes idénticos.
"""

from __future__ import annotations

import collections
import json
from pathlib import Path

FIG_DIR = Path(__file__).resolve().parent
REPO = FIG_DIR.parents[2]

CATALOGO = REPO / "data" / "experiment" / "grafo_v2" / "esquema_v2_clases.json"
KG = (REPO / "data" / "experiment" / "reextraccion_v2" / "corpus_v2"
      / "salida_r1" / "kg.json")
SALIDA = FIG_DIR / "figura_catalogo_sujetos.svg"

# ========================================================================== #
# 1. Carga de los artefactos + candados de versión                           #
# ========================================================================== #

CAT = json.loads(CATALOGO.read_text(encoding="utf-8"))
assert CAT["version"] == "2.0", f"catálogo v2.0 esperado, hay {CAT['version']}"

ENTRADAS = {c["id"]: c for c in CAT["clases"]}
CLASES = [c["id"] for c in CAT["clases"] if c["nivel"] == "clase"]
INSTANCIAS = [c["id"] for c in CAT["clases"] if c["nivel"] == "instancia"]
ROLES = {r["id"]: r for r in CAT["roles"]}

assert len(CLASES) == 58, f"58 clases esperadas, hay {len(CLASES)}"
assert len(INSTANCIAS) == 7, f"7 instancias esperadas, hay {len(INSTANCIAS)}"
assert len(ROLES) == 5, f"5 roles esperados, hay {len(ROLES)}"

HIJOS = collections.defaultdict(list)
for _cid in CLASES:
    _p = ENTRADAS[_cid].get("padre")
    if _p is not None:
        HIJOS[_p].append(_cid)          # orden = orden del artefacto

RAICES = [c for c in CLASES if ENTRADAS[c].get("padre") is None]
assert RAICES == ["Sujeto_sujeto"], f"raíz única esperada, hay {RAICES}"
RAIZ = RAICES[0]

# ========================================================================== #
# 2. Qué se dibuja (declarado) y qué se colapsa (derivado)                    #
# ========================================================================== #

# Cadena a profundidad completa que cita la prosa, verificada contra el
# artefacto: si el catálogo cambiara, el assert frena antes de dibujar.
CADENA = ["Sujeto_sujeto", "Sujeto_sujeto_regulado", "Sujeto_entidad_financiera",
          "Sujeto_banco", "Sujeto_banco_comercial"]
for _i, _n in enumerate(CADENA):
    _esperado = CADENA[_i - 1] if _i else None
    assert ENTRADAS[_n].get("padre") == _esperado, (
        f"la cadena citada no es la del artefacto en {_n}: padre real "
        f"{ENTRADAS[_n].get('padre')!r}, esperado {_esperado!r}")

ROL = "Sujeto_rol_sujeto_obligado_proteccion"
assert len(ROLES[ROL]["miembros"]) == 7

# Norma real del TO de Protección de usuarios que apunta al rol con aplica_a.
NORMA = ("Obligacion_se_debera_dar_a_estos_usuarios_la_opcion_de_obtener_en_"
         "sistema_braille_la_docume_c53a37")

CLASES_DIBUJADAS = [
    "Sujeto_sujeto",
    "Sujeto_sujeto_regulado",
    "Sujeto_entidad_financiera",
    "Sujeto_banco",
    "Sujeto_banco_comercial",
    "Sujeto_entidad_cambiaria",
    "Sujeto_proveedor_no_financiero_de_credito",
    "Sujeto_empresa_no_financiera_emisora_de_tarjetas",
    "Sujeto_fiduciario_de_fideicomiso_financiero",
    "Sujeto_contraparte",
    "Sujeto_organismo_publico",
    "Sujeto_estructura",
]
SET_DIB = set(CLASES_DIBUJADAS)
assert len(SET_DIB) == len(CLASES_DIBUJADAS)
assert SET_DIB <= set(CLASES), "hay un id dibujado que no está en el catálogo"

INSTANCIAS_DIBUJADAS = ["Sujeto_bcra", "Sujeto_sefyc"]
MIEMBROS_DIBUJADOS = [m for m in ROLES[ROL]["miembros"] if m in SET_DIB]


def ancestro_dibujado(nodo: str) -> str:
    p = ENTRADAS[nodo].get("padre")
    while p is not None:
        if p in SET_DIB:
            return p
        p = ENTRADAS[p].get("padre")
    raise AssertionError(f"{nodo} no cuelga de ninguna clase dibujada")


GRUPOS: dict[str, list[str]] = collections.defaultdict(list)
for _cid in CLASES:
    if _cid not in SET_DIB:
        GRUPOS[ancestro_dibujado(_cid)].append(_cid)

# Conteo: dibujadas + colapsadas = 58, y los grupos son disjuntos y cubren
# exactamente el complemento de lo dibujado.
_union = [n for g in GRUPOS.values() for n in g]
assert len(_union) == len(set(_union)), "los grupos colapsados se solapan"
assert set(_union) == set(CLASES) - SET_DIB, "los grupos no cubren el resto"
N_COLAPSADAS = len(_union)
assert len(CLASES_DIBUJADAS) + N_COLAPSADAS == 58, (
    f"{len(CLASES_DIBUJADAS)} + {N_COLAPSADAS} != 58")

INSTANCIAS_COLAPSADAS = [i for i in INSTANCIAS if i not in INSTANCIAS_DIBUJADAS]
assert len(INSTANCIAS_DIBUJADAS) + len(INSTANCIAS_COLAPSADAS) == 7
MIEMBROS_NO_DIBUJADOS = [m for m in ROLES[ROL]["miembros"]
                         if m not in MIEMBROS_DIBUJADOS]
assert len(MIEMBROS_DIBUJADOS) + len(MIEMBROS_NO_DIBUJADOS) == 7
# Los miembros no dibujados tienen que estar DENTRO de algún grupo colapsado:
# la figura no pierde ninguno, los declara.
assert all(m in set(_union) for m in MIEMBROS_NO_DIBUJADOS)

# ========================================================================== #
# 3. Verificación contra el grafo vigente                                    #
# ========================================================================== #

_kg = json.loads(KG.read_text(encoding="utf-8"))
NODOS_KG = {n["id"]: n for n in _kg["nodes"]}
ARISTAS_KG = {(e["source"], e["relation"], e["target"]) for e in _kg["edges"]}
_cnt = collections.Counter(e["relation"] for e in _kg["edges"])
for _rel, _n in (("subclase_de", 57), ("instancia_de", 7),
                 ("miembro_de", 17), ("parte_de", 1)):
    assert _cnt[_rel] == _n, f"kg vigente: {_rel} = {_cnt[_rel]}, esperado {_n}"

# Aristas EXPLÍCITAS (un trazo dibujado = una arista del grafo).
ARISTAS_EXPLICITAS: list[tuple[str, str, str]] = []
for _c in CLASES_DIBUJADAS:
    _p = ENTRADAS[_c].get("padre")
    if _p is not None:
        assert _p in SET_DIB
        ARISTAS_EXPLICITAS.append((_c, "subclase_de", _p))
for _i in INSTANCIAS_DIBUJADAS:
    ARISTAS_EXPLICITAS.append((_i, "instancia_de", ENTRADAS[_i]["instancia_de"]))
for _m in MIEMBROS_DIBUJADOS:
    ARISTAS_EXPLICITAS.append((_m, "miembro_de", ROL))
ARISTAS_EXPLICITAS.append((NORMA, "aplica_a", ROL))

# Aristas AGREGADAS: el trazo que llega a un nodo colapsado representa las
# aristas subclase_de (o instancia_de) directas de ese grupo hacia el padre
# dibujado. Se verifican una por una igual que las explícitas.
ARISTAS_AGREGADAS: dict[str, list[tuple[str, str, str]]] = {}
for _p, _g in GRUPOS.items():
    ARISTAS_AGREGADAS[_p] = sorted(
        (n, "subclase_de", _p) for n in _g if ENTRADAS[n]["padre"] == _p)
ARISTAS_AGREGADAS["__instancias__"] = sorted(
    (i, "instancia_de", ENTRADAS[i]["instancia_de"])
    for i in INSTANCIAS_COLAPSADAS)

# --- El camino que la figura existe para mostrar -------------------------- #
# Cinco nodos y cuatro aristas: la norma apunta al rol, el rol recibe a
# Entidades financieras, y de ahí el árbol baja a Bancos y a Bancos
# comerciales. Se resalta como una unidad; el resto del dibujo va atenuado.
CAMINO_NODOS = ["NORMA", "ROL", "Sujeto_entidad_financiera", "Sujeto_banco",
                "Sujeto_banco_comercial"]
CAMINO_ARISTAS = [
    (NORMA, "aplica_a", ROL),
    ("Sujeto_entidad_financiera", "miembro_de", ROL),
    ("Sujeto_banco", "subclase_de", "Sujeto_entidad_financiera"),
    ("Sujeto_banco_comercial", "subclase_de", "Sujeto_banco"),
]
# El camino es una cadena: cada arista une dos nodos consecutivos de la lista
# (en un sentido o en el otro — la dirección la pone el artefacto, no la
# lectura). Si dejara de serlo, el resalte estaría mintiendo y esto frena.
_clave = {NORMA: "NORMA", ROL: "ROL"}
assert len(CAMINO_ARISTAS) == len(CAMINO_NODOS) - 1
for _i, (_s, _r, _t) in enumerate(CAMINO_ARISTAS):
    _par = {_clave.get(_s, _s), _clave.get(_t, _t)}
    assert _par == {CAMINO_NODOS[_i], CAMINO_NODOS[_i + 1]}, (
        f"el camino no es una cadena en el paso {_i}: {_par} != "
        f"{{{CAMINO_NODOS[_i]}, {CAMINO_NODOS[_i + 1]}}}")
# Las cuatro son aristas reales y ya están entre las que la figura dibuja una
# a una (no son agregados de un nodo colapsado).
assert all(a in ARISTAS_EXPLICITAS for a in CAMINO_ARISTAS)
assert all(a in ARISTAS_KG for a in CAMINO_ARISTAS)
# El camino usa las tres relaciones de la indirección más la del árbol.
assert {r for _, r, _ in CAMINO_ARISTAS} == {"aplica_a", "miembro_de",
                                             "subclase_de"}
EN_CAMINO = set(CAMINO_NODOS)

TODAS_LAS_ARISTAS = ARISTAS_EXPLICITAS + [
    a for k in sorted(ARISTAS_AGREGADAS) for a in ARISTAS_AGREGADAS[k]]
_faltan = [a for a in TODAS_LAS_ARISTAS if a not in ARISTAS_KG]
assert not _faltan, f"aristas dibujadas ausentes del kg vigente: {_faltan}"

# Los nodos que no vienen del catálogo (la norma y el rol) existen en el kg
# y se dibujan con SU etiqueta.
assert NORMA in NODOS_KG and NODOS_KG[NORMA]["type"] == "Obligacion"
assert ROL in NODOS_KG and NODOS_KG[ROL]["label"] == ROLES[ROL]["label"]

_pn = NODOS_KG[NORMA]["provenance"]
NORMA_LABEL = NODOS_KG[NORMA]["label"]
NORMA_PUNTO = _pn["punto"]
NORMA_PAGS = _pn["paginas"]
ROL_PUNTO = ROLES[ROL]["provenance"]["location"]

# ========================================================================== #
# 4. Estilo                                                                  #
# ========================================================================== #

TIPO_SANS = "Helvetica,Arial,sans-serif"
TIPO_MONO = "Menlo,Consolas,'Courier New',monospace"

C_CLASE = "#2a6f97"        # clases del árbol
C_COLAPSADA = "#6f6f6f"    # ramas no expandidas
C_INSTANCIA = "#6d597a"    # instancias
C_ROL = "#b5179e"          # rol de alcance (la indirección)
C_NORMA = "#b23a48"        # norma
C_TEXTO = "#1a1a1a"
C_NOTA = "#5c5c5c"
BLANCO = "#ffffff"

# Tipografía. El piso es duro: ningún texto por debajo de PT_MIN puntos
# impresos a width=\linewidth. El assert vive en §6, cuando se conoce el
# ancho final del lienzo.
LINEWIDTH_MM = 150.0  # a4 con márgenes laterales de 3 cm (main.tex:9)
PT_MIN = 8.0

ANCHO_MONO = 0.60    # avance por carácter de la familia monoespaciada

FS_NODO = 29
FS_SUB = 27          # subtítulo dentro de una caja (tipo, procedencia)
FS_REL = 27          # rótulo de relación
FS_LEY = 27          # leyenda

AN_BASE = 1.7
AN_ROL = 2.4
AN_APLICA = 3.0
OFF_MEM = 13          # separación vertical del diente miembro_de
INSET_ROL = 18        # sangrado de los lados oblicuos del hexágono del rol
PLIEGUE_NORMA = 16    # esquina plegada de la caja de norma

# --- Las dos intensidades ------------------------------------------------- #
# El camino resaltado se distingue por TRAZO y por SATURACIÓN DEL RELLENO,
# las dos legibles en blanco y negro; el color sigue siendo redundante.
AN_CAMINO = 4.6       # trazo de las cuatro aristas del camino
AN_ATENUADO = 1.9     # trazo del resto de las aristas
AN_NODO_CAMINO = 4.0  # borde de los cinco nodos del camino
AN_NODO_ATENUADO = 1.9
REL_CAMINO = 0.66     # relleno de los nodos del camino (más saturado)
REL_ATENUADO = 0.94   # relleno del resto (casi blanco)
TRAZO_ATENUADO = 0.42  # cuánto se aclara el color de lo que no es camino

PAD_X, PAD_Y = 13, 9
LH = 34              # interlineado del label
LH_SUB = 31


def mezcla(color: str, blanco: float) -> str:
    r, g, b = (int(color[i:i + 2], 16) for i in (1, 3, 5))
    m = [round(c + (255 - c) * blanco) for c in (r, g, b)]
    return "#{:02x}{:02x}{:02x}".format(*m)


def f(v: float) -> str:
    s = f"{v:.1f}"
    return s[:-2] if s.endswith(".0") else s


def esc(s: str) -> str:
    return (s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


# --- métrica de texto (Helvetica, anchos AFM /1000) ----------------------- #
_W = {
    " ": 278, "!": 278, '"': 355, "#": 556, "$": 556, "%": 889, "&": 667,
    "'": 191, "(": 333, ")": 333, "*": 389, "+": 584, ",": 278, "-": 333,
    ".": 278, "/": 278, ":": 278, ";": 278, "?": 556, "@": 1015, "[": 278,
    "]": 278, "_": 556, "{": 334, "|": 260, "}": 334, "·": 278, "«": 333,
    "»": 333, "—": 1000, "→": 1000,
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


def envolver(texto: str, fs: float, maxw: float, bold: bool = False) -> list[str]:
    lineas: list[str] = []
    actual = ""
    for pal in texto.split():
        cand = f"{actual} {pal}".strip()
        if actual and ancho(cand, fs, bold) > maxw:
            lineas.append(actual)
            actual = pal
        else:
            actual = cand
    if actual:
        lineas.append(actual)
    return lineas


# ========================================================================== #
# 5. Cajas: medida y contenido                                               #
# ========================================================================== #

class Caja:
    """Caja medida a partir de su texto: nada se dibuja fuera de su borde.

    El label y los subtítulos se envuelven al ancho máximo de la columna y el
    constructor ASSERTA que ninguna línea desborda el interior de la caja —
    una etiqueta cortada es un defecto que no puede llegar al informe.
    """

    def __init__(self, clave, forma, lineas, sub, color, maxw):
        self.clave = clave
        self.forma = forma            # clase | colapsada | instancia | rol | norma
        self.lineas = lineas
        self.sub = sub                # líneas de subtítulo, ya envueltas
        self.color = color
        anchos = ([ancho(l, FS_NODO, True) for l in lineas]
                  + [ancho(s, FS_SUB) for s in sub])
        self.w = min(maxw, max(anchos)) + 2 * PAD_X
        self.h = len(lineas) * LH + len(sub) * LH_SUB + 2 * PAD_Y
        if forma == "instancia":
            self.w += 14              # las píldoras necesitan aire en los topes
        if forma == "rol":
            self.w += 2 * INSET_ROL   # los lados oblicuos del hexágono comen
        if forma == "norma":
            self.w += PLIEGUE_NORMA   # la esquina plegada come el ángulo
        interior = (self.w - 2 * PAD_X
                    - (2 * INSET_ROL if forma == "rol" else 0)
                    - (PLIEGUE_NORMA if forma == "norma" else 0))
        for l, fs, bold in ([(l, FS_NODO, True) for l in lineas]
                            + [(s, FS_SUB, False) for s in sub]):
            assert ancho(l, fs, bold) <= interior + 0.5, (
                f"la línea {l!r} de {clave} desborda su caja "
                f"({f(ancho(l, fs, bold))} > {f(interior)})")
        self.x = 0.0
        self.y = 0.0                  # centro vertical


MAXW = {0: 189, 1: 245, 2: 259, 3: 303, 4: 192,
        "rol": 400, "norma": 300}

CAJAS: dict[str, Caja] = {}


def nueva(clave, forma, texto, sub, color, col):
    maxw = MAXW[col]
    c = Caja(clave, forma,
             envolver(texto, FS_NODO, maxw, True),
             [l for s in sub for l in envolver(s, FS_SUB, maxw)],
             color, maxw)
    c.col = col
    CAJAS[clave] = c
    return c


COL_DE = {
    "Sujeto_sujeto": 0,
    "Sujeto_sujeto_regulado": 1, "Sujeto_contraparte": 1,
    "Sujeto_organismo_publico": 1, "Sujeto_estructura": 1,
    "Sujeto_entidad_financiera": 2, "Sujeto_entidad_cambiaria": 2,
    "Sujeto_proveedor_no_financiero_de_credito": 2,
    "Sujeto_fiduciario_de_fideicomiso_financiero": 2,
    "Sujeto_banco": 3, "Sujeto_empresa_no_financiera_emisora_de_tarjetas": 3,
    "Sujeto_banco_comercial": 4,
}
for _c in CLASES_DIBUJADAS:
    nueva(_c, "clase", ENTRADAS[_c]["label"], [], C_CLASE, COL_DE[_c])

COL_COLAPSADA = {
    "Sujeto_sujeto_regulado": 2, "Sujeto_contraparte": 2,
    "Sujeto_organismo_publico": 2, "Sujeto_estructura": 2,
    "Sujeto_entidad_financiera": 3, "Sujeto_entidad_cambiaria": 3,
}
for _p in CLASES_DIBUJADAS:
    if _p in GRUPOS:
        n = len(GRUPOS[_p])
        # Sin subtítulo: «rama no expandida» ya lo dice la leyenda por la
        # forma, y el alto que ocupaba se gasta en tipografía.
        nueva(f"COL:{_p}", "colapsada", f"+{n} clases", [],
              C_COLAPSADA, COL_COLAPSADA[_p]).colapsa = n


def sigla(label: str) -> str:
    """La sigla con la que el catálogo abre la etiqueta de una instancia.

    Las dos instancias dibujadas traen el nombre desplegado entre paréntesis
    («BCRA (Banco Central de la República Argentina)»). En la figura entra
    solo la sigla —las instancias son el punto menos importante de la
    subsección— y el nombre completo va al epígrafe. No se inventa nada: la
    sigla es un prefijo literal del `label` del artefacto, y esto lo asserta.
    """
    s = label.split(" (")[0].strip()
    assert s and label.startswith(s) and s != label, (
        f"la etiqueta {label!r} no tiene la forma «SIGLA (nombre)»")
    return s


for _i in INSTANCIAS_DIBUJADAS:
    _caja = nueva(_i, "instancia", sigla(ENTRADAS[_i]["label"]), [],
                  C_INSTANCIA, 2)
    _caja.label_artefacto = ENTRADAS[_i]["label"]   # queda en el SVG
nueva("INSTCOL", "colapsada", f"+{len(INSTANCIAS_COLAPSADAS)} instancias",
      [], C_COLAPSADA, 2).colapsa = len(INSTANCIAS_COLAPSADAS)

# Una sola línea de subtítulo en cada caja de la banda, y estructural: la
# procedencia completa (documento, punto y páginas) va al epígrafe, que es
# donde no cuesta alto de figura.
nueva("ROL", "rol", ROLES[ROL]["label"],
      [f"{len(ROLES[ROL]['miembros'])} miembros · "
       f"{len(MIEMBROS_DIBUJADOS)} dibujados"],
      C_ROL, "rol")
nueva("NORMA", "norma", NORMA_LABEL,
      [f"Obligación · punto {NORMA_PUNTO}"], C_NORMA, "norma")

# ========================================================================== #
# 6. Geometría                                                               #
# ========================================================================== #

MARGEN = 26
GAPS = [48, 74, 82, 48]          # C0-C1, C1-C2, C2-C3, C3-C4

_anchos_col = {}
for _cl, _c in CAJAS.items():
    if _c.col in ("rol", "norma"):
        continue
    _anchos_col[_c.col] = max(_anchos_col.get(_c.col, 0), _c.w)

_x = float(MARGEN)
X_COL, W_COL = {}, {}
for _k in range(5):
    X_COL[_k] = _x
    W_COL[_k] = _anchos_col[_k]
    _x += _anchos_col[_k] + (GAPS[_k] if _k < 4 else 0)
ANCHO_SVG = _x + MARGEN

for _cl, _c in CAJAS.items():
    if _c.col not in ("rol", "norma"):
        _c.x = X_COL[_c.col]        # alineación a izquierda dentro de la columna

# Troncos verticales -------------------------------------------------------
X_SUB_01 = X_COL[0] + W_COL[0] + 24          # comb de la raíz
X_SUB_12 = X_COL[1] + W_COL[1] + 24          # combs de nivel 1 → 2
X_INS_12 = X_COL[1] + W_COL[1] + 50          # instancia_de
X_MEM_23 = X_COL[2] + W_COL[2] + 18          # miembro_de (hacia el rol)
X_SUB_23 = X_COL[2] + W_COL[2] + 42          # combs de nivel 2 → 3
X_SUB_34 = X_COL[3] + W_COL[3] + 24

# Banda superior: norma + rol ---------------------------------------------
rol, norma = CAJAS["ROL"], CAJAS["NORMA"]
# El rol cuelga del tronco de miembro_de; la norma se apoya en el margen
# izquierdo, que el árbol deja libre en esa banda.
rol.x = X_MEM_23 - rol.w / 2.0
norma.x = float(MARGEN)
_ancho_rotulo = ANCHO_MONO * FS_REL * len("aplica_a") + 20
assert rol.x - (norma.x + norma.w) >= _ancho_rotulo, (
    f"el tramo de aplica_a ({f(rol.x - norma.x - norma.w)} px) no alcanza "
    f"para su rótulo ({f(_ancho_rotulo)} px)")
Y_BANDA = MARGEN + max(rol.h, norma.h) / 2.0
rol.y = norma.y = Y_BANDA

# Filas del árbol ----------------------------------------------------------
FILAS = [
    ["Sujeto_banco_comercial", "Sujeto_banco"],
    ["COL:Sujeto_entidad_financiera"],
    ["COL:Sujeto_entidad_cambiaria", "Sujeto_entidad_cambiaria"],
    ["Sujeto_empresa_no_financiera_emisora_de_tarjetas",
     "Sujeto_proveedor_no_financiero_de_credito"],
    ["Sujeto_fiduciario_de_fideicomiso_financiero"],
    ["COL:Sujeto_sujeto_regulado"],
    ["COL:Sujeto_contraparte", "Sujeto_contraparte"],
    ["COL:Sujeto_organismo_publico"],
    ["Sujeto_bcra"],
    ["Sujeto_sefyc"],
    ["INSTCOL"],
    ["COL:Sujeto_estructura", "Sujeto_estructura"],
]
SEP_FILA = 14
Y_ARBOL = Y_BANDA + max(rol.h, norma.h) / 2.0 + 42

_y = Y_ARBOL
Y_FILA = []
for _fila in FILAS:
    _h = max(CAJAS[k].h for k in _fila)
    Y_FILA.append(_y + _h / 2.0)
    _y += _h + SEP_FILA
ALTO_ARBOL = _y - SEP_FILA

for _i, _fila in enumerate(FILAS):
    for _k in _fila:
        CAJAS[_k].y = Y_FILA[_i]

# Padres cuya y es el punto medio de sus hijos dibujados
CAJAS["Sujeto_entidad_financiera"].y = (Y_FILA[0] + Y_FILA[1]) / 2.0
CAJAS["Sujeto_organismo_publico"].y = (Y_FILA[7] + Y_FILA[10]) / 2.0
CAJAS["Sujeto_sujeto_regulado"].y = (
    CAJAS["Sujeto_entidad_financiera"].y + Y_FILA[5]) / 2.0
CAJAS["Sujeto_sujeto"].y = (
    CAJAS["Sujeto_sujeto_regulado"].y + CAJAS["Sujeto_estructura"].y) / 2.0

# ========================================================================== #
# 7. Emisión del SVG                                                         #
# ========================================================================== #

O: list[str] = []
SEGMENTOS: list = []      # (a, b, grosor, es_leyenda) de cada trazo
ROTULOS: list = []        # solicitudes de rótulo, resueltas al final


def add(s: str) -> None:
    O.append(s)


def texto(cx, y0, lineas, fs, color, bold=False, mono=False, anchor="middle",
          italic=False):
    fam = TIPO_MONO if mono else TIPO_SANS
    est = (f'font-family="{fam}" font-size="{f(fs)}" fill="{color}" '
           f'text-anchor="{anchor}"')
    if bold:
        est += ' font-weight="bold"'
    if italic:
        est += ' font-style="italic"'
    partes = [f'<text x="{f(cx)}" y="{f(y0)}" {est}>']
    for i, l in enumerate(lineas):
        dy = "0" if i == 0 else f(fs * 1.0 + (LH - fs))
        partes.append(f'<tspan x="{f(cx)}" dy="{dy}">{esc(l)}</tspan>')
    partes.append("</text>")
    add("".join(partes))


class _Pintada:
    """Vista de una caja con el color de borde ya resuelto por intensidad."""

    def __init__(self, caja, borde):
        self._c = caja
        self.color = borde

    def __getattr__(self, n):
        return getattr(self._c, n)


def dibujar_caja(c: Caja) -> None:
    en_camino = c.clave in EN_CAMINO
    dat = f' data-nodo="{esc(c.clave)}" data-forma="{c.forma}"'
    if getattr(c, "colapsa", None) is not None:
        dat += f' data-colapsa="{c.colapsa}"'
    if getattr(c, "label_artefacto", None):
        dat += f' data-label-artefacto="{esc(c.label_artefacto)}"'
    if en_camino:
        dat += ' data-camino="1"'
    add(f"<g{dat}>")
    x, y, w, h = c.x, c.y - c.h / 2.0, c.w, c.h
    relleno = mezcla(c.color, REL_CAMINO if en_camino else REL_ATENUADO)
    borde = c.color if en_camino else mezcla(c.color, TRAZO_ATENUADO)
    AN_BASE = AN_NODO_CAMINO if en_camino else AN_NODO_ATENUADO
    AN_ROL = AN_BASE
    c = _Pintada(c, borde)
    if c.forma == "clase":
        add(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" '
            f'rx="3" fill="{relleno}" stroke="{c.color}" '
            f'stroke-width="{f(AN_BASE)}"/>')
    elif c.forma == "colapsada":
        for dx in (7, 3.5):
            add(f'<rect x="{f(x + dx)}" y="{f(y - dx)}" width="{f(w)}" '
                f'height="{f(h)}" rx="3" fill="{BLANCO}" stroke="{c.color}" '
                f'stroke-width="1.1" stroke-dasharray="5 3" opacity="0.75"/>')
        add(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" '
            f'rx="3" fill="{relleno}" stroke="{c.color}" '
            f'stroke-width="{f(AN_BASE)}" stroke-dasharray="7 4"/>')
    elif c.forma == "instancia":
        add(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" '
            f'rx="{f(h / 2.0)}" ry="{f(h / 2.0)}" fill="{relleno}" '
            f'stroke="{c.color}" stroke-width="{f(AN_BASE)}"/>')
    elif c.forma == "rol":
        m = INSET_ROL
        pts = [(x + m, y), (x + w - m, y), (x + w, y + h / 2.0),
               (x + w - m, y + h), (x + m, y + h), (x, y + h / 2.0)]
        d = " ".join(f"{f(px)},{f(py)}" for px, py in pts)
        add(f'<polygon points="{d}" fill="{relleno}" stroke="{c.color}" '
            f'stroke-width="{f(AN_ROL)}" stroke-dasharray="11 4 3 4"/>')
    elif c.forma == "norma":
        p = float(PLIEGUE_NORMA)
        d = (f"M{f(x)},{f(y)} L{f(x + w - p)},{f(y)} L{f(x + w)},{f(y + p)} "
             f"L{f(x + w)},{f(y + h)} L{f(x)},{f(y + h)} Z")
        add(f'<path d="{d}" fill="{relleno}" stroke="{c.color}" '
            f'stroke-width="{f(AN_BASE)}"/>')
        add(f'<path d="M{f(x + w - p)},{f(y)} L{f(x + w - p)},{f(y + p)} '
            f'L{f(x + w)},{f(y + p)}" fill="none" stroke="{c.color}" '
            f'stroke-width="1.2"/>')
    alto_txt = len(c.lineas) * LH + len(c.sub) * LH_SUB
    y0 = c.y - alto_txt / 2.0 + FS_NODO * 0.78
    texto(x + w / 2.0, y0, c.lineas, FS_NODO, C_TEXTO, bold=True)
    if c.sub:
        ys = c.y - alto_txt / 2.0 + len(c.lineas) * LH + FS_SUB * 0.85
        texto(x + w / 2.0, ys, c.sub, FS_SUB, C_NOTA, italic=True)
    add("</g>")


def anotar(hijo_clave, rel, padre_clave):
    """data-* del diente: una arista concreta, o el agregado de un colapsado."""
    if hijo_clave == "INSTCOL":
        return {"data-rel": rel, "data-dst": ENTRADAS[INSTANCIAS_COLAPSADAS[0]]
                ["instancia_de"], "data-agrega": len(ARISTAS_AGREGADAS
                                                    ["__instancias__"])}
    if hijo_clave.startswith("COL:"):
        padre = hijo_clave[4:]
        return {"data-rel": rel, "data-dst": padre,
                "data-agrega": len(ARISTAS_AGREGADAS[padre]),
                "data-clases": len(GRUPOS[padre])}
    return {"data-rel": rel, "data-src": hijo_clave, "data-dst": padre_clave}


ESTILO_REL = {
    "subclase_de": (C_CLASE, AN_BASE, "none", "pt-sub"),
    "instancia_de": (C_INSTANCIA, AN_BASE, "6 4", "pt-ins"),
    "miembro_de": (C_ROL, AN_ROL, "12 4 3 4", "pt-mem"),
    "aplica_a": (C_NORMA, AN_APLICA, "none", "pt-apl"),
}


def polilinea(pts, rel, con_punta=True, datos=None, camino=False,
              leyenda=False):
    """Un trazo. `datos` deja en el SVG las anotaciones data-* con las que la
    figura se recuenta sin volver a correr el script (convención de F1).

    `camino=True` lo dibuja con la intensidad del camino resaltado y con la
    punta grande; sin él, el trazo va atenuado."""
    color, _, dash, mk = ESTILO_REL[rel]
    if not camino:
        color = mezcla(color, TRAZO_ATENUADO)
    an = AN_CAMINO if camino else AN_ATENUADO
    d = " ".join(("M" if i == 0 else "L") + f"{f(px)},{f(py)}"
                 for i, (px, py) in enumerate(pts))
    at = (f'fill="none" stroke="{color}" stroke-width="{f(an)}" '
          f'stroke-linejoin="round" stroke-linecap="round"')
    if dash != "none":
        at += f' stroke-dasharray="{dash}"'
    if con_punta:
        at += f' marker-end="url(#{mk}{"-cam" if camino else ""})"'
    # La muestra de la leyenda usa la misma intensidad pero NO es una
    # arista del dibujo: sin data-camino, el recuento desde el SVG da 4.
    if camino and not leyenda:
        at += ' data-camino="1"'
    if datos:
        at += "".join(f' {k}="{esc(str(v))}"' for k, v in sorted(datos.items()))
    add(f'<path d="{d}" {at}/>')
    # Registro para la guarda: todo segmento dibujado queda anotado con su
    # grosor, para medir después qué atraviesa.
    for _a, _b in zip(pts, pts[1:]):
        SEGMENTOS.append((_a, _b, an, leyenda))


SEP_ROTULO = 12.0      # separación mínima entre el rótulo y su tronco
MARGEN_ROTULO = 3.0    # aire exigido contra cajas, otros rótulos y trazos


def rect_rotulo(txt, x, y, anchor):
    """Rectángulo que ocupa un rótulo colocado en (x, y) con ese anclaje."""
    w = ANCHO_MONO * FS_REL * len(txt)
    x0 = {"middle": x - w / 2.0, "start": x, "end": x - w}[anchor]
    return (x0 - 5, y - FS_REL * 0.58, x0 + w + 5, y + FS_REL * 0.58)


def rotulo(txt, rel, candidatos):
    """SOLICITA un rótulo; no lo dibuja.

    Los rótulos se emiten todos juntos en una capa final (§ «capa de
    rótulos»), después de las aristas y de las cajas. Antes se dibujaban
    dentro de cada peine, y entonces su halo solo protegía de lo dibujado
    ANTES: una caja posterior podía pisarle un carácter —el defecto que se
    leía «subclase_ae»—. `candidatos` es la lista de posiciones probadas en
    orden de preferencia; la primera que pase la guarda se usa.
    """
    ROTULOS.append({"txt": txt, "rel": rel, "cand": list(candidatos)})


def bandas_libres(cajas, y_lo, y_hi):
    """Tramos de [y_lo, y_hi] que ninguna caja ocupa.

    Las bandas de las cajas se FUSIONAN antes de buscar huecos. Sin fusionar,
    dos bandas superpuestas producen un hueco fantasma —el defecto original:
    se eligió un hueco de 5,8 px entre el final de una banda y el comienzo de
    la siguiente, cuando una tercera banda lo cubría entero—.
    """
    aire = FS_REL * 0.62
    ocup = sorted((c.y - c.h / 2.0 - aire, c.y + c.h / 2.0 + aire)
                  for c in cajas)
    fus = []
    for a, b in ocup:
        if fus and a <= fus[-1][1]:
            fus[-1][1] = max(fus[-1][1], b)
        else:
            fus.append([a, b])
    libres, cursor = [], y_lo
    for a, b in fus:
        if a > cursor:
            libres.append((cursor, min(a, y_hi)))
        cursor = max(cursor, b)
        if cursor >= y_hi:
            break
    if cursor < y_hi:
        libres.append((cursor, y_hi))
    return [(a, b) for a, b in libres if b - a > 1]


def cand_tronco(x_t, y_lo, y_hi, cajas, lados=("izq", "der")):
    """Posiciones a un lado y otro del tronco, nunca encima.

    El orden de preferencia es: primero los centros de las bandas que ninguna
    caja ocupa (de la más ancha a la más angosta), y después un barrido fino
    de todo el tronco y de un margen por encima y por debajo.
    """
    pref = [ (a + b) / 2.0 for a, b in
             sorted(bandas_libres(cajas, y_lo, y_hi),
                    key=lambda t: (-(t[1] - t[0]), t[0])) ]
    barrido = [y_lo - 4.0 * i for i in range(1, 16)]
    barrido += [y_lo + 4.0 * i for i in range(int((y_hi - y_lo) // 4) + 1)]
    barrido += [y_hi + 4.0 * i for i in range(1, 16)]
    for y in pref + sorted(barrido):
        for lado in lados:
            if lado == "izq":
                yield (x_t - SEP_ROTULO, round(y, 2), "end")
            else:
                yield (x_t + SEP_ROTULO, round(y, 2), "start")


def cand_tramo(x_a, x_b, y):
    """Sobre un tramo horizontal: por encima, por debajo, y corriéndose."""
    cx = (x_a + x_b) / 2.0
    for d in (0.0, 14.0, -14.0, 28.0, -28.0, 42.0, -42.0):
        for signo in (-1.0, 1.0):
            yield (cx + d, y + signo * FS_REL * 0.95, "middle")


def comb(padre_clave, hijos_claves, x_tronco, rel, rotular=False, puerto=0.0,
         lados=("izq", "der")):
    """Dientes desde los hijos → tronco vertical → una punta en el padre.

    Un peine dibuja N aristas del artefacto con una sola punta, como en las
    figuras F1/F1b: el rótulo es único por peine. `puerto` desplaza el acceso
    sobre el borde del padre, para que dos peines que terminan en la misma
    caja (subclase_de e instancia_de sobre «Organismos públicos») no monten
    su punta en el mismo punto.
    """
    p = CAJAS[padre_clave]
    hs = [CAJAS[h] for h in hijos_claves]
    y_p = p.y + puerto
    ys = [h.y for h in hs]
    y_lo, y_hi = min(ys + [y_p]), max(ys + [y_p])
    for h in hs:
        polilinea([(h.x, h.y), (x_tronco, h.y)], rel, con_punta=False,
                  datos=anotar(h.clave, rel, padre_clave))
    if y_hi - y_lo > 0.5:
        polilinea([(x_tronco, y_lo), (x_tronco, y_hi)], rel, con_punta=False)
    polilinea([(x_tronco, y_p), (p.x + p.w, y_p)], rel)
    if rotular:
        if len(hs) >= 2:
            rotulo(rel, rel, cand_tronco(x_tronco, y_lo, y_hi, hs + [p], lados))
        else:
            rotulo(rel, rel, cand_tramo(hs[0].x, p.x + p.w, hs[0].y))


defs = []
for rel, (color0, _an, dash, mk) in sorted(ESTILO_REL.items()):
    for suf, color, k in (("", mezcla(color0, TRAZO_ATENUADO), 1.0),
                          ("-cam", color0, 1.45)):
        if rel == "subclase_de":   # triángulo hueco (generalización)
            cuerpo = (f'<path d="M0,0 L{f(11 * k)},{f(4.2 * k)} '
                      f'L0,{f(8.4 * k)} Z" fill="{BLANCO}" stroke="{color}" '
                      f'stroke-width="{f(1.5 * k)}"/>')
            w, h, rx, ry = 12 * k, 9 * k, 11 * k, 4.2 * k
        elif rel == "aplica_a":    # punta grande llena
            cuerpo = (f'<path d="M0,0 L{f(13 * k)},{f(5 * k)} '
                      f'L0,{f(10 * k)} Z" fill="{color}"/>')
            w, h, rx, ry = 13 * k, 10 * k, 13 * k, 5 * k
        elif rel == "miembro_de":  # punta llena con cola cóncava
            cuerpo = (f'<path d="M0,0 L{f(11 * k)},{f(4.2 * k)} '
                      f'L0,{f(8.4 * k)} L{f(3.2 * k)},{f(4.2 * k)} Z" '
                      f'fill="{color}"/>')
            w, h, rx, ry = 11 * k, 8.4 * k, 11 * k, 4.2 * k
        else:                      # instancia_de: punta llena chica
            cuerpo = (f'<path d="M0,0 L{f(9 * k)},{f(3.6 * k)} '
                      f'L0,{f(7.2 * k)} Z" fill="{color}"/>')
            w, h, rx, ry = 9 * k, 7.2 * k, 9 * k, 3.6 * k
        defs.append(f'<marker id="{mk}{suf}" markerUnits="userSpaceOnUse" '
                    f'markerWidth="{f(w)}" markerHeight="{f(h)}" '
                    f'refX="{f(rx)}" refY="{f(ry)}" orient="auto">'
                    f'{cuerpo}</marker>')

# --- leyenda: panel en el hueco libre de la derecha ----------------------- #
# El árbol deja vacío todo el cuadrante inferior derecho (las columnas 3 y 4
# sólo tienen contenido en las cuatro primeras filas). La leyenda va ahí: no
# agrega alto a la figura y queda a la vista mientras se lee el dibujo.
FORMAS_LEY = [
    ("clase", C_CLASE, "clase del catálogo"),
    ("colapsada", C_COLAPSADA, "rama no expandida"),
    ("instancia", C_INSTANCIA, "instancia"),
    ("rol", C_ROL, "rol de alcance"),
    ("norma", C_NORMA, "norma"),
]
RELS_LEY = ["subclase_de", "instancia_de", "miembro_de", "aplica_a"]
ETIQ_CAMINO = "camino resaltado"
NOTA_CAMINO = "norma → rol → clase → subclase"
NOTA_LEY = "La punta señala al padre o al rol."

X_PANEL = X_COL[3]
W_PANEL = ANCHO_SVG - MARGEN - X_PANEL
PAD_PANEL = 18
FILA_LEY = 38
_ultima_der = max(c.y + c.h / 2.0 for c in CAJAS.values()
                  if c.clave not in ("ROL", "NORMA") and c.col in (3, 4))
Y_PANEL = _ultima_der + 52
ALTO_LINEA_NOTA = FS_LEY + 4
NOTA_LINEAS = envolver(NOTA_LEY, FS_LEY, W_PANEL - 2 * PAD_PANEL)
CAMINO_LINEAS = envolver(NOTA_CAMINO, FS_LEY, W_PANEL - 2 * PAD_PANEL)
ALTO_PANEL = (PAD_PANEL + FS_LEY + 9 + len(FORMAS_LEY) * FILA_LEY + 16
              + len(RELS_LEY) * FILA_LEY + 16
              + FILA_LEY + len(CAMINO_LINEAS) * ALTO_LINEA_NOTA + 10
              + len(NOTA_LINEAS) * ALTO_LINEA_NOTA + PAD_PANEL)
# El panel se apoya en el hueco libre; si su contenido lo desborda, el
# lienzo crece lo justo (la guarda de no-solapamiento sigue vigente).
ALTO_SVG = max(ALTO_ARBOL, Y_PANEL + ALTO_PANEL) + MARGEN


def pt(fs: float) -> float:
    """Tamano impreso, en puntos, de un cuerpo de `fs` px a ancho pleno."""
    return fs / ANCHO_SVG * LINEWIDTH_MM / 25.4 * 72


# Piso tipográfico. Es la restricción dura de esta versión de la figura: si
# el dibujo crece de ancho hasta hacer que algún cuerpo caiga por debajo de
# PT_MIN, esto FRENA — la salida es podar, nunca achicar la tipografía.
_CUERPOS = {"etiqueta de nodo": FS_NODO, "subtítulo": FS_SUB,
            "rótulo de relación": FS_REL, "leyenda": FS_LEY}
_flojos = {n: round(pt(v), 2) for n, v in _CUERPOS.items() if pt(v) < PT_MIN}
assert not _flojos, (
    f"tipografía por debajo de {PT_MIN} pt impresos a {LINEWIDTH_MM} mm: "
    f"{_flojos} (ancho del lienzo {f(ANCHO_SVG)} px)")

# --- guarda geométrica: ninguna caja se solapa con otra ni con el panel --- #
# La pregunta «¿alguna etiqueta se superpone o se corta?» se responde por
# construcción y no por inspección visual: el texto no desborda su caja
# (assert del constructor de Caja) y ninguna caja pisa a otra (assert de acá).
_RECTS = [(c.clave, c.x, c.y - c.h / 2.0, c.x + c.w, c.y + c.h / 2.0)
          for c in (CAJAS[k] for k in sorted(CAJAS))]
_RECTS.append(("PANEL_LEYENDA", X_PANEL, Y_PANEL,
               X_PANEL + W_PANEL, Y_PANEL + ALTO_PANEL))
for _i in range(len(_RECTS)):
    _na, _ax0, _ay0, _ax1, _ay1 = _RECTS[_i]
    assert _ax1 <= ANCHO_SVG - MARGEN + 0.5 and _ax0 >= MARGEN - 0.5, (
        f"{_na} se sale del lienzo horizontalmente")
    assert _ay1 <= ALTO_SVG - MARGEN + 0.5 and _ay0 >= MARGEN - 0.5, (
        f"{_na} se sale del lienzo verticalmente")
    for _j in range(_i + 1, len(_RECTS)):
        _nb, _bx0, _by0, _bx1, _by1 = _RECTS[_j]
        if (_ax0 < _bx1 - 0.5 and _bx0 < _ax1 - 0.5
                and _ay0 < _by1 - 0.5 and _by0 < _ay1 - 0.5):
            raise AssertionError(f"se solapan las cajas {_na} y {_nb}")

add(f'<svg xmlns="http://www.w3.org/2000/svg" width="{f(ANCHO_SVG)}" '
    f'height="{f(ALTO_SVG)}" viewBox="0 0 {f(ANCHO_SVG)} {f(ALTO_SVG)}">')
add("<defs>" + "".join(defs) + "</defs>")
add(f'<rect width="{f(ANCHO_SVG)}" height="{f(ALTO_SVG)}" fill="{BLANCO}"/>')

# ---- aristas (debajo de las cajas) --------------------------------------- #
# subclase_de: raíz → 4 hijos
comb("Sujeto_sujeto",
     ["Sujeto_sujeto_regulado", "Sujeto_contraparte", "Sujeto_organismo_publico",
      "Sujeto_estructura"],
     X_SUB_01, "subclase_de", rotular=True)

# subclase_de: Sujetos regulados → 4 clases + rama colapsada
comb("Sujeto_sujeto_regulado",
     ["Sujeto_entidad_financiera", "Sujeto_entidad_cambiaria",
      "Sujeto_proveedor_no_financiero_de_credito",
      "Sujeto_fiduciario_de_fideicomiso_financiero", "COL:Sujeto_sujeto_regulado"],
     X_SUB_12, "subclase_de", rotular=True)

comb("Sujeto_contraparte", ["COL:Sujeto_contraparte"], X_SUB_12, "subclase_de")
comb("Sujeto_estructura", ["COL:Sujeto_estructura"], X_SUB_12, "subclase_de")
# Los dos peines que terminan en «Organismos públicos» entran por puertos
# distintos del mismo borde: subclase_de arriba, instancia_de abajo.
comb("Sujeto_organismo_publico", ["COL:Sujeto_organismo_publico"], X_SUB_12,
     "subclase_de", puerto=-FS_REL * 0.45)
comb("Sujeto_organismo_publico",
     ["Sujeto_bcra", "Sujeto_sefyc", "INSTCOL"], X_INS_12, "instancia_de",
     puerto=FS_REL * 0.45, rotular=True, lados=("izq",))

comb("Sujeto_entidad_financiera",
     ["Sujeto_banco", "COL:Sujeto_entidad_financiera"], X_SUB_23, "subclase_de")
comb("Sujeto_entidad_cambiaria", ["COL:Sujeto_entidad_cambiaria"], X_SUB_23,
     "subclase_de")
comb("Sujeto_proveedor_no_financiero_de_credito",
     ["Sujeto_empresa_no_financiera_emisora_de_tarjetas"], X_SUB_23,
     "subclase_de")
comb("Sujeto_banco", ["Sujeto_banco_comercial"], X_SUB_34, "subclase_de",
     rotular=True)

# miembro_de: los 5 miembros dibujados → tronco → rol
_c2 = [m for m in MIEMBROS_DIBUJADOS if CAJAS[m].col == 2]
_c3 = [m for m in MIEMBROS_DIBUJADOS if CAJAS[m].col == 3]
assert len(_c2) + len(_c3) == len(MIEMBROS_DIBUJADOS)
for m in _c2:
    c = CAJAS[m]
    polilinea([(c.x + c.w, c.y + OFF_MEM), (X_MEM_23, c.y + OFF_MEM)],
              "miembro_de", con_punta=False,
              datos={"data-rel": "miembro_de", "data-src": m, "data-dst": ROL})
for m in _c3:
    c = CAJAS[m]
    polilinea([(c.x, c.y + OFF_MEM), (X_MEM_23, c.y + OFF_MEM)],
              "miembro_de", con_punta=False,
              datos={"data-rel": "miembro_de", "data-src": m, "data-dst": ROL})
_y_mem = [CAJAS[m].y + OFF_MEM for m in MIEMBROS_DIBUJADOS]
polilinea([(X_MEM_23, max(_y_mem)), (X_MEM_23, rol.y + rol.h / 2.0)],
          "miembro_de")
rotulo("miembro_de", "miembro_de",
       cand_tronco(X_MEM_23, min(_y_mem), rol.y + rol.h / 2.0,
                   [CAJAS[m] for m in MIEMBROS_DIBUJADOS] + [rol]))

# aplica_a: norma → rol
polilinea([(norma.x + norma.w, rol.y), (rol.x, rol.y)], "aplica_a",
          datos={"data-rel": "aplica_a", "data-src": NORMA, "data-dst": ROL})
rotulo("aplica_a", "aplica_a",
       cand_tramo(norma.x + norma.w, rol.x, rol.y))

# ---- el camino, por encima ------------------------------------------------ #
# Mismos vértices que los trazos ya dibujados: esta capa los repite con la
# intensidad del camino y los tapa. No agrega aristas —las cuatro ya están
# contadas y verificadas— y por eso no lleva anotaciones data-rel: lleva
# data-camino, que es lo que la distingue.
_bc, _ba = CAJAS["Sujeto_banco_comercial"], CAJAS["Sujeto_banco"]
_ef, _no = CAJAS["Sujeto_entidad_financiera"], CAJAS["NORMA"]
polilinea([(_bc.x, _bc.y), (_ba.x + _ba.w, _ba.y)], "subclase_de", camino=True)
polilinea([(_ba.x, _ba.y), (X_SUB_23, _ba.y), (X_SUB_23, _ef.y),
           (_ef.x + _ef.w, _ef.y)], "subclase_de", camino=True)
polilinea([(_ef.x + _ef.w, _ef.y + OFF_MEM), (X_MEM_23, _ef.y + OFF_MEM),
           (X_MEM_23, rol.y + rol.h / 2.0)], "miembro_de", camino=True)
polilinea([(_no.x + _no.w, rol.y), (rol.x, rol.y)], "aplica_a", camino=True)

# El tramo de tronco que el camino resalta es el que va del rol hasta el
# diente de Entidades financieras, y solo ese: por debajo de ese punto el
# tronco sigue atenuado, porque el camino no baja por ahí. Que Entidades
# financieras sea el miembro más alto es lo que hace que el corte caiga
# justo en su diente; si dejara de serlo, el resalte cubriría tramo ajeno.
assert _ef.y + OFF_MEM == min(_y_mem), (
    "Entidades financieras dejó de ser el miembro más alto: el resalte del "
    "tronco de miembro_de cubriría tramo que el camino no recorre")

# ---- cajas --------------------------------------------------------------- #
for _cl in sorted(CAJAS):
    dibujar_caja(CAJAS[_cl])

# ---- leyenda ------------------------------------------------------------- #
add(f'<rect x="{f(X_PANEL)}" y="{f(Y_PANEL)}" width="{f(W_PANEL)}" '
    f'height="{f(ALTO_PANEL)}" rx="5" fill="#fbfbfa" stroke="#d8d8d8" '
    f'stroke-width="1"/>')
_yl = Y_PANEL + PAD_PANEL + FS_LEY
add(f'<text x="{f(X_PANEL + PAD_PANEL)}" y="{f(_yl)}" '
    f'font-family="{TIPO_SANS}" font-size="{f(FS_LEY + 1)}" fill="{C_TEXTO}" '
    f'font-weight="bold" text-anchor="start">Referencias</text>')
_yl += 9 + FILA_LEY / 2.0


def swatch(forma, color, gx, gy, gw, gh, camino=False):
    """Muestra de una forma. Por omisión, con la intensidad atenuada: es la
    del grueso del dibujo. `camino=True` la dibuja resaltada."""
    relleno = mezcla(color, REL_CAMINO if camino else REL_ATENUADO)
    borde = color if camino else mezcla(color, TRAZO_ATENUADO)
    an = AN_NODO_CAMINO if camino else AN_NODO_ATENUADO
    if forma == "clase":
        add(f'<rect x="{f(gx)}" y="{f(gy)}" width="{f(gw)}" height="{f(gh)}" '
            f'rx="3" fill="{relleno}" stroke="{borde}" stroke-width="{f(an)}"/>')
    elif forma == "colapsada":
        add(f'<rect x="{f(gx + 4)}" y="{f(gy - 4)}" width="{f(gw)}" '
            f'height="{f(gh)}" rx="3" fill="{BLANCO}" stroke="{borde}" '
            f'stroke-width="1.1" stroke-dasharray="5 3" opacity="0.75"/>')
        add(f'<rect x="{f(gx)}" y="{f(gy)}" width="{f(gw)}" height="{f(gh)}" '
            f'rx="3" fill="{relleno}" stroke="{borde}" stroke-width="{f(an)}" '
            f'stroke-dasharray="7 4"/>')
    elif forma == "instancia":
        add(f'<rect x="{f(gx)}" y="{f(gy)}" width="{f(gw)}" height="{f(gh)}" '
            f'rx="{f(gh / 2)}" ry="{f(gh / 2)}" fill="{relleno}" '
            f'stroke="{borde}" stroke-width="{f(an)}"/>')
    elif forma == "rol":
        m = 6.0
        pts = [(gx + m, gy), (gx + gw - m, gy), (gx + gw, gy + gh / 2),
               (gx + gw - m, gy + gh), (gx + m, gy + gh), (gx, gy + gh / 2)]
        add('<polygon points="' + " ".join(f"{f(a)},{f(b)}" for a, b in pts)
            + f'" fill="{relleno}" stroke="{borde}" stroke-width="{f(an)}" '
              f'stroke-dasharray="11 4 3 4"/>')
    else:
        q = 7.0
        add(f'<path d="M{f(gx)},{f(gy)} L{f(gx + gw - q)},{f(gy)} '
            f'L{f(gx + gw)},{f(gy + q)} L{f(gx + gw)},{f(gy + gh)} '
            f'L{f(gx)},{f(gy + gh)} Z" fill="{relleno}" stroke="{borde}" '
            f'stroke-width="{f(an)}"/>')

for forma, color, etiqueta in FORMAS_LEY:
    gx, gw, gh = X_PANEL + PAD_PANEL, 34.0, 19.0
    swatch(forma, color, gx, _yl - gh / 2.0, gw, gh)
    add(f'<text x="{f(gx + gw + 12)}" y="{f(_yl + FS_LEY * 0.36)}" '
        f'font-family="{TIPO_SANS}" font-size="{f(FS_LEY)}" fill="{C_NOTA}" '
        f'text-anchor="start">{esc(etiqueta)}</text>')
    _yl += FILA_LEY

_yl += 4
add(f'<line x1="{f(X_PANEL + PAD_PANEL)}" y1="{f(_yl)}" '
    f'x2="{f(X_PANEL + W_PANEL - PAD_PANEL)}" y2="{f(_yl)}" stroke="#e2e2e2" '
    f'stroke-width="1"/>')
_yl += 12

for rel in RELS_LEY:
    polilinea([(X_PANEL + PAD_PANEL + 40, _yl), (X_PANEL + PAD_PANEL, _yl)],
              rel, leyenda=True)
    add(f'<text x="{f(X_PANEL + PAD_PANEL + 51)}" y="{f(_yl + FS_LEY * 0.36)}" '
        f'font-family="{TIPO_MONO}" font-size="{f(FS_LEY)}" '
        f'fill="{ESTILO_REL[rel][0]}" text-anchor="start">{esc(rel)}</text>')
    _yl += FILA_LEY

_yl += 4
add(f'<line x1="{f(X_PANEL + PAD_PANEL)}" y1="{f(_yl)}" '
    f'x2="{f(X_PANEL + W_PANEL - PAD_PANEL)}" y2="{f(_yl)}" stroke="#e2e2e2" '
    f'stroke-width="1"/>')
_yl += 12

# --- la fila del camino: una caja resaltada, un trazo grueso, otra caja ---
_gx, _gw, _gh = X_PANEL + PAD_PANEL, 15.0, 19.0
swatch("clase", C_CLASE, _gx, _yl - _gh / 2.0, _gw, _gh, camino=True)
polilinea([(_gx + _gw + 24, _yl), (_gx + _gw + 4, _yl)], "subclase_de",
          camino=True, leyenda=True)
swatch("clase", C_CLASE, _gx + _gw + 28, _yl - _gh / 2.0, _gw, _gh, camino=True)
add(f'<text x="{f(_gx + 2 * _gw + 40)}" y="{f(_yl + FS_LEY * 0.36)}" '
    f'font-family="{TIPO_SANS}" font-size="{f(FS_LEY)}" fill="{C_TEXTO}" '
    f'font-weight="bold" text-anchor="start">{esc(ETIQ_CAMINO)}</text>')
_yl += FILA_LEY - 4

for linea in CAMINO_LINEAS:
    add(f'<text x="{f(X_PANEL + PAD_PANEL)}" y="{f(_yl)}" '
        f'font-family="{TIPO_SANS}" font-size="{f(FS_LEY)}" fill="{C_NOTA}" '
        f'font-style="italic" text-anchor="start">{esc(linea)}</text>')
    _yl += ALTO_LINEA_NOTA

_yl += 10
for linea in NOTA_LINEAS:
    add(f'<text x="{f(X_PANEL + PAD_PANEL)}" y="{f(_yl)}" '
        f'font-family="{TIPO_SANS}" font-size="{f(FS_LEY)}" fill="{C_NOTA}" '
        f'font-style="italic" text-anchor="start">{esc(linea)}</text>')
    _yl += ALTO_LINEA_NOTA

# ---- capa de rótulos + guarda de trazos ---------------------------------- #
# Los rótulos se emiten acá, al final: por encima de todas las aristas y de
# todas las cajas. Dentro de cada peine, su halo solo protegía de lo dibujado
# antes, y una caja posterior le comía caracteres.

RECT_CAJAS = [(c.clave, c.x, c.y - c.h / 2.0, c.x + c.w, c.y + c.h / 2.0)
              for c in (CAJAS[k] for k in sorted(CAJAS))]
RECT_PANEL = ("PANEL_LEYENDA", X_PANEL, Y_PANEL,
              X_PANEL + W_PANEL, Y_PANEL + ALTO_PANEL)


def _solapan(A, B, m=0.0):
    return (A[0] < B[2] + m and B[0] < A[2] + m
            and A[1] < B[3] + m and B[1] < A[3] + m)


def _segmento_toca(a, b, R, grosor, m):
    """¿El segmento a-b (recto, horizontal o vertical) entra en el rect R?

    R se agranda por el margen pedido más la mitad del grosor del trazo: lo
    que se mide es la tinta, no la línea ideal.
    """
    e = m + grosor / 2.0
    x0, y0, x1, y1 = R[0] - e, R[1] - e, R[2] + e, R[3] + e
    if abs(a[1] - b[1]) < 0.01:                       # horizontal
        return (y0 < a[1] < y1
                and max(x0, min(a[0], b[0])) < min(x1, max(a[0], b[0])))
    if abs(a[0] - b[0]) < 0.01:                       # vertical
        return (x0 < a[0] < x1
                and max(y0, min(a[1], b[1])) < min(y1, max(a[1], b[1])))
    raise AssertionError(f"segmento no ortogonal: {a} -> {b}")


def _penetra_caja(a, b, R, grosor):
    """Cuánto entra el segmento a-b DENTRO del rectángulo R, a lo largo.

    Mide longitud, no contacto: casi todos los trazos terminan sobre el borde
    de una caja (ahí va la punta de flecha, ahí arranca un diente), y eso es
    correcto. Lo que es defecto es atravesarla. La posición perpendicular se
    compara contra el interior encogido por medio grosor, de modo que se mide
    la tinta y no la línea ideal.
    """
    e = grosor / 2.0 + 1.0
    if abs(a[1] - b[1]) < 0.01:                       # horizontal
        if not (R[1] + e < a[1] < R[3] - e):
            return 0.0
        return max(0.0, min(R[2], max(a[0], b[0])) - max(R[0], min(a[0], b[0])))
    if abs(a[0] - b[0]) < 0.01:                       # vertical
        if not (R[0] + e < a[0] < R[2] - e):
            return 0.0
        return max(0.0, min(R[3], max(a[1], b[1])) - max(R[1], min(a[1], b[1])))
    raise AssertionError(f"segmento no ortogonal: {a} -> {b}")


def _rotulo_libre(R, puestos):
    if not (MARGEN - 2 <= R[0] and R[2] <= ANCHO_SVG - MARGEN + 2
            and MARGEN - 2 <= R[1] and R[3] <= ALTO_SVG - MARGEN + 2):
        return False
    for _n, *B in RECT_CAJAS + [RECT_PANEL]:
        if _solapan(R, B, MARGEN_ROTULO):
            return False
    for P in puestos:
        if _solapan(R, P, MARGEN_ROTULO):
            return False
    for a, b, grosor, ley in SEGMENTOS:
        if not ley and _segmento_toca(a, b, R, grosor, MARGEN_ROTULO):
            return False
    return True


_puestos = []
for _r in ROTULOS:
    for _i, (_x, _y, _anc) in enumerate(_r["cand"]):
        _R = rect_rotulo(_r["txt"], _x, _y, _anc)
        if _rotulo_libre(_R, _puestos):
            _r["pos"], _r["rect"], _r["cand_n"] = (_x, _y, _anc), _R, _i
            _puestos.append(_R)
            break
    else:
        raise AssertionError(
            f"no hay lugar libre para el rótulo «{_r['txt']}»: ninguno de sus "
            f"{len(_r['cand'])} candidatos queda fuera de cajas, de otros "
            f"rótulos y de todo trazo")

for _r in ROTULOS:
    _x, _y, _anc = _r["pos"]
    _color = ESTILO_REL[_r["rel"]][0]
    _R = _r["rect"]
    add(f'<rect x="{f(_R[0])}" y="{f(_R[1])}" width="{f(_R[2] - _R[0])}" '
        f'height="{f(_R[3] - _R[1])}" fill="{BLANCO}"/>')
    add(f'<text x="{f(_x)}" y="{f(_y + FS_REL * 0.36)}" '
        f'font-family="{TIPO_MONO}" font-size="{f(FS_REL)}" fill="{_color}" '
        f'text-anchor="{_anc}" data-rotulo="{esc(_r["rel"])}">'
        f'{esc(_r["txt"])}</text>')

# GUARDA NUEVA. La anterior solo comparaba caja contra caja; esta mide los
# trazos contra el interior de cada caja y contra el rectángulo de cada
# rótulo. Un trazo que cruza texto es un defecto de render, y acá frena.
TOL_PENETRACION = 3.0     # entrar menos que esto es tocar el borde, no cruzar
_VIOLA = []
for _n, *_B in RECT_CAJAS:
    for _a, _b, _g, _ley in SEGMENTOS:
        if _ley:
            continue
        _d = _penetra_caja(_a, _b, tuple(_B), _g)
        if _d > TOL_PENETRACION:
            _VIOLA.append(f"trazo {_a}->{_b} entra {_d:.1f} px en la caja {_n}")
for _r in ROTULOS:
    for _a, _b, _g, _ley in SEGMENTOS:
        if not _ley and _segmento_toca(_a, _b, _r["rect"], _g, 0.0):
            _VIOLA.append(f"trazo {_a}->{_b} cruza el rótulo «{_r['txt']}»")
    for _n, *_B in RECT_CAJAS + [RECT_PANEL]:
        if _solapan(_r["rect"], _B):
            _VIOLA.append(f"el rótulo «{_r['txt']}» pisa la caja {_n}")
assert not _VIOLA, "trazos o rótulos superpuestos:\n  " + "\n  ".join(_VIOLA)

add("</svg>")

SALIDA.write_text("\n".join(O) + "\n", encoding="utf-8")

# ========================================================================== #
# 8. Reporte de verificación (a stdout, para pegar)                          #
# ========================================================================== #

print(f"SVG escrito: {SALIDA.relative_to(REPO)}  "
      f"({f(ANCHO_SVG)} x {f(ALTO_SVG)})")
print()
print("BIYECCIÓN nodo dibujado ↔ entrada del artefacto")
print(f"  clases dibujadas       : {len(CLASES_DIBUJADAS):2d}")
for p in CLASES_DIBUJADAS:
    if p in GRUPOS:
        print(f"  colapsada bajo {ENTRADAS[p]['label']:24s}: "
              f"+{len(GRUPOS[p]):2d} clases "
              f"({len(ARISTAS_AGREGADAS[p])} subclase_de directas)")
print(f"  colapsadas (total)     : {N_COLAPSADAS:2d}")
print(f"  CONTEO  {len(CLASES_DIBUJADAS)} + {N_COLAPSADAS} = "
      f"{len(CLASES_DIBUJADAS) + N_COLAPSADAS}  (catálogo: {len(CLASES)})")
print(f"  instancias  {len(INSTANCIAS_DIBUJADAS)} dibujadas + "
      f"{len(INSTANCIAS_COLAPSADAS)} declaradas = "
      f"{len(INSTANCIAS_DIBUJADAS) + len(INSTANCIAS_COLAPSADAS)}  "
      f"(catálogo: {len(INSTANCIAS)})")
print(f"  roles       1 dibujado de {len(ROLES)} del catálogo; "
      f"miembros {len(MIEMBROS_DIBUJADOS)} dibujados + "
      f"{len(MIEMBROS_NO_DIBUJADOS)} declarados = "
      f"{len(ROLES[ROL]['miembros'])}")
print("  miembros NO dibujados (dentro de «+15 clases»):")
for m in MIEMBROS_NO_DIBUJADOS:
    print(f"      {ENTRADAS[m]['label']}")
print()
print("CAMINO RESALTADO (5 nodos, 4 aristas; cadena verificada)")
for _n in CAMINO_NODOS:
    _et = (NODOS_KG[NORMA]["label"] if _n == "NORMA"
           else ROLES[ROL]["label"] if _n == "ROL"
           else ENTRADAS[_n]["label"])
    print(f"      {_et}")
for _s, _r, _t in CAMINO_ARISTAS:
    print(f"      {_s[:52]:52s} --{_r}--> {_t}")
print(f"  las 4 son aristas explícitas del dibujo y están en el kg: "
      f"{all(a in ARISTAS_EXPLICITAS and a in ARISTAS_KG for a in CAMINO_ARISTAS)}")
print()
print("CAPA DE RÓTULOS (emitida al final, por encima de aristas y cajas)")
for _r in ROTULOS:
    _x, _y, _anc = _r["pos"]
    _R = _r["rect"]
    print(f"      «{_r['txt']:12s}» en x {_x:7.1f} y {_y:7.1f} ({_anc:6s}) "
          f"— rect x {_R[0]:7.1f}..{_R[2]:7.1f} y {_R[1]:6.1f}..{_R[3]:6.1f} "
          f"— candidato {_r['cand_n']} de {len(_r['cand'])}")
print(f"  guarda: 0 trazos dentro de una caja (más de {TOL_PENETRACION} px) "
      f"y 0 trazos sobre un rótulo, sobre {len(RECT_CAJAS)} cajas y "
      f"{sum(1 for _s in SEGMENTOS if not _s[3])} segmentos del dibujo")
print()
print("TIPOGRAFÍA impresa a width=\\linewidth "
      f"({LINEWIDTH_MM:.0f} mm; lienzo {f(ANCHO_SVG)} x {f(ALTO_SVG)} px)")
for _n, _v in _CUERPOS.items():
    print(f"      {_n:20s} {_v} px -> {pt(_v):.2f} pt")
print(f"  piso exigido {PT_MIN} pt: "
      f"{'CUMPLE' if min(pt(v) for v in _CUERPOS.values()) >= PT_MIN else 'NO'}")
print(f"  alto impreso: {ALTO_SVG / ANCHO_SVG * LINEWIDTH_MM:.1f} mm")
print()
print("INSTANCIAS abreviadas (sigla dibujada / etiqueta del artefacto)")
for _i in INSTANCIAS_DIBUJADAS:
    print(f"      {sigla(ENTRADAS[_i]['label']):6s} <- {ENTRADAS[_i]['label']}")
print()
print("ARISTAS contra el grafo vigente (salida_r1/kg.json)")
print(f"  conteos globales: subclase_de={_cnt['subclase_de']} "
      f"instancia_de={_cnt['instancia_de']} miembro_de={_cnt['miembro_de']} "
      f"parte_de={_cnt['parte_de']}")
print(f"  trazos explícitos (1 trazo = 1 arista): {len(ARISTAS_EXPLICITAS)}")
for s, r, t in ARISTAS_EXPLICITAS:
    print(f"      {s}  --{r}-->  {t}")
print(f"  trazos agregados (1 trazo = N aristas hacia el nodo colapsado): "
      f"{len(TODAS_LAS_ARISTAS) - len(ARISTAS_EXPLICITAS)}")
print(f"  TOTAL aristas representadas: {len(TODAS_LAS_ARISTAS)}  "
      f"— todas presentes en el kg vigente: "
      f"{all(a in ARISTAS_KG for a in TODAS_LAS_ARISTAS)}")
