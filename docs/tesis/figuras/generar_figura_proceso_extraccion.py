#!/usr/bin/env python3
"""Figura «del documento al grafo» para la Introducción (Figura 1.3), versión 2.

Siete elementos en secuencia de izquierda a derecha, en dos filas unidas por
una flecha de continuidad: el Texto Ordenado de entrada, las cinco etapas del
proceso (segmentación, extracción, validación, revisión y ensamblado) y el
grafo de salida. Dos colores distinguen las etapas que ejecuta un modelo de
lenguaje de las determinísticas; la leyenda va al pie.

Versión 1 (28/09/2026; generador en fbe69d4): las cinco etapas eran
segmentación, extracción, revisión, ensamblado y resolución de remisiones, y el
recuadro «Grafo» dibujaba, del grafo r1, una Restriccion del 5.1.1.1 con
limita hacia la Operacion y referencia hacia la Obligacion del 3.7.
Versión 2:
- la caja del validador, en código, entre el extractor y el revisor;
- la resolución de las remisiones deja de ser una caja propia: pasa al
  ensamblado («une las partes y deriva las remisiones»);
- con una caja más en la primera fila, el revisor pasa a la segunda: sus dos
  salidas laterales («vuelve a extraer», hacia el extractor, y «marcado para
  revisión humana») se dibujan desde allí;
- el recuadro «Grafo» dibuja tres nodos de la figura 1.1 versión 2: la
  Condicion del monto y la Operacion del 5.1.1.1, unidas por condicion_de, y
  la Definicion del 3.7, con la remite_a resaltada; los colores de tipo son
  los de la figura del esquema final (los de la figura 1.1);
- los controles de medidas corren siempre (en la versión 1, con --verificar)
  y se suman los de geometría y de inventario de la figura 1.1.

Los tres nodos y las dos aristas del recuadro «Grafo» no se tipean: se toman
del subgrafo de la figura 1.1 (generar_figura_norma_a_grafo.cargar_subgrafo,
que lee el grafo de desarrollo r2b y el de diez documentos con su candado y
comprueba que lo dibujado está igual en los dos). La firma de condicion_de
(Condicion → Operacion) se comprueba en la matriz del esquema r2 y remite_a en
la lista de predicados derivados por código del ensamblado, los dos en
modelos_r2.py (leído con su candado). Cada nodo se rotula con su tipo, escrito
como en el código, y su punto de procedencia; cada arista, con el nombre de la
relación tal como está en el grafo.

Misma técnica, tipografía y tamaños que la versión 1: el SVG se escribe a
mano, sin red, y la generación es determinística.

Controles, en cada corrida (el script frena si fallan): cada texto medido con
las métricas reales de Helvetica entra en su caja, no se superpone con otro,
no sale del lienzo y no queda por debajo de 9 pt impresos; inventario del
recuadro «Grafo» releído del SVG contra el grafo; geometría de la figura 1.1
(ningún trazo atraviesa una caja, ningún texto sobre un trazo que no es el
suyo, 0 cruces). Antes de componer corren dos pruebas negativas (una arista de
más en el recuadro y la salida lateral cruzando la flecha de continuidad).

Salidas, byte-reproducibles: figura_proceso_extraccion.svg, .png (300 dpi,
densidad grabada) y .pdf (SOURCE_DATE_EPOCH=0).

Uso (desde la raíz del repo):
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_proceso_extraccion.py
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_proceso_extraccion.py --salida DIR
"""

import sys

sys.dont_write_bytecode = True  # importar los módulos hermanos no deja __pycache__

import argparse  # noqa: E402
import os  # noqa: E402
import xml.etree.ElementTree as ET  # noqa: E402
from collections import Counter  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import generar_figura_norma_a_grafo as base  # noqa: E402

NOMBRE = "figura_proceso_extraccion"
freno = base.freno
NS = base.NS

# Esquema r2: matriz de firmas y predicados derivados por código (U-R2-CODIGO;
# igual en bbc38dc, el commit de los dos grafos).
MODELOS_R2 = ("data/experiment/pyd_r2/code/modelos_r2.py",
              "e67f15ae13dd5419ea0ce1a08dbef63c86cbdf9c269772a0b02a4e27b4c3a2ca")
# Líneas de modelos_r2.py que el script exige, literales: la ampliación de
# condicion_de a Operacion (AMPLIACION_R2) y remite_a como predicado derivado,
# con su firma y sus propiedades.
LITERALES_R2 = {
    "extraccion": '    ("condicion_de", "Condicion", "Operacion"),',
    "derivado": 'PREDICADOS_DERIVADOS = ("remite_a",)',
    "tipos_contenido": 'TIPOS_CONTENIDO = ("Operacion", "Restriccion", "Excepcion", "Obligacion", "Potestad", "Condicion",',
    "firma_derivada": '    "remite_a": (TIPOS_CONTENIDO, TIPOS_CONTENIDO + ("TextoOrdenado",)),',
    "propiedades": 'PROPIEDADES_REMISION = ("alcance", "destino", "evidencia")',
}

# --------------------------------------------------------------------------- #
# Tamaño impreso (como en la versión 1)                                        #
# A4 con márgenes de 3 cm: ancho de texto 15 cm; la figura entra a 0,85.       #
# --------------------------------------------------------------------------- #
ANCHO_TEXTO_CM = 15.0
FRACCION = 0.85
ANCHO_FIGURA_CM = ANCHO_TEXTO_CM * FRACCION          # 12,75 cm
PT_POR_CM = 72.0 / 2.54
ANCHO_FIGURA_PT = ANCHO_FIGURA_CM * PT_POR_CM         # 361,4 pt
PT_MINIMO = 9.0
W = 720                                               # unidades del lienzo


def puntos_impresos(px):
    return px * ANCHO_FIGURA_PT / W


# --------------------------------------------------------------------------- #
# Paleta y tipografía (como en la versión 1, salvo los colores de tipo, que    #
# son los de la figura del esquema final)                                      #
# --------------------------------------------------------------------------- #
TIPOGRAFIA = "Helvetica,Arial,sans-serif"
MODELO = {"relleno": "#fbe3d3", "borde": "#e07b39"}           # modelo de lenguaje
DETERMINISTICA = {"relleno": "#e1e7ee", "borde": "#4a5a6a"}   # determinística
NEUTRO = {"relleno": "#fafafa", "borde": "#999999"}
TINTA = "#1f1f1f"
TINTA_SUB = "#444444"
FLECHA = "#555555"
GRIS_ARISTA = "#8a8a8a"
GRIS_ROTULO = "#555555"
ACENTO = base.ACENTO
ACENTO_TEXTO = base.ACENTO_TEXTO

FS_TITULO = 19
FS_SUB = 18
IL_TITULO = 23
IL_SUB = 22

# --------------------------------------------------------------------------- #
# Contenido                                                                    #
# --------------------------------------------------------------------------- #
ELEMENTOS = {
    "a": {"rotulo": ["Texto", "Ordenado"], "sub": None, "clase": NEUTRO},
    "b": {"rotulo": ["Segmentación", "en puntos"],
          "sub": "siguiendo la estructura del propio documento",
          "clase": DETERMINISTICA},
    "c": {"rotulo": ["Extracción de", "entidades y", "relaciones"],
          "sub": "un modelo de lenguaje, bajo un esquema fijo",
          "clase": MODELO},
    "v": {"rotulo": ["Validación", "contra el", "esquema"],
          "sub": "en código",
          "clase": DETERMINISTICA},
    "d": {"rotulo": ["Revisión contra", "el texto", "de origen"],
          "sub": "un segundo modelo",
          "clase": MODELO},
    "e": {"rotulo": ["Ensamblado en", "un único grafo"],
          "sub": "une las partes y deriva las remisiones",
          "clase": DETERMINISTICA},
    "g": {"rotulo": ["Grafo"], "sub": None, "clase": NEUTRO},
}
SALIDA_VUELVE = "vuelve a extraer"
SALIDA_MARCADO = ["marcado para", "revisión humana"]
LEYENDA = [(MODELO, "Etapa que ejecuta un modelo de lenguaje"),
           (DETERMINISTICA, "Etapa determinística")]
LEYENDA_REMISION = "remisión de un punto a otro"

# Nodos del recuadro «Grafo»: (posición, clave en el subgrafo de la figura 1.1).
# Arriba al centro, la Condicion del monto; abajo a la izquierda, la Definicion
# del 3.7; abajo a la derecha, la Operacion (la composición de la versión 1).
NODOS_FIGURA = [
    ("C", "condicion_monto"),
    ("D", "definicion_3_7"),
    ("OP", "operacion"),
]
# Aristas: (origen, relación, destino, clase). «extraccion»: una relación que
# devuelve el extractor, con firma en la matriz del esquema r2; «remision»: un
# predicado derivado por código en el ensamblado.
ARISTAS_FIGURA = [("C", "condicion_de", "OP", "extraccion"),
                  ("C", "remite_a", "D", "remision")]


def leer_esquema_r2():
    texto = base.leer_con_candado(*MODELOS_R2).decode("utf-8")
    lineas = texto.split("\n")
    donde = {}
    for k, lit in LITERALES_R2.items():
        n = [i for i, l in enumerate(lineas, 1) if l == lit]
        if len(n) != 1:
            freno(f"{MODELOS_R2[0]}: la línea {lit!r} aparece {len(n)} veces")
        donde[k] = n[0]
    tipos = LITERALES_R2["tipos_contenido"] + lineas[donde["tipos_contenido"]]
    return donde, tipos


def cargar_grafo():
    """Nodos y aristas del recuadro, del subgrafo de la figura 1.1."""
    sub = base.cargar_subgrafo(base.GRAFO)
    diez = base.cargar_subgrafo(base.GRAFO_DIEZ)
    base.comparar_grafos(sub, diez)
    donde, tipos_contenido = leer_esquema_r2()
    nodos = {}
    for clave, k in NODOS_FIGURA:
        n = sub["nodos"][k]
        nodos[clave] = {"clave": k, "id": n["id"], "tipo": n["type"], "punto": n["punto"], "etiqueta": n["label"]}
    por_clave = {(a["origen"], a["relation"], a["destino"]): a for a in sub["aristas"]}
    aristas = []
    for a, rel, b, clase in ARISTAS_FIGURA:
        e = por_clave.get((nodos[a]["clave"], rel, nodos[b]["clave"]))
        if e is None:
            freno(f"arista {a} {rel} {b} ausente del subgrafo de la figura 1.1")
        if clase == "extraccion":
            if (nodos[a]["tipo"], rel, nodos[b]["tipo"]) != ("Condicion", "condicion_de", "Operacion"):
                freno(f"arista de extracción sin su línea en {MODELOS_R2[0]}: {a} {rel} {b}")
            if e["properties"]:
                freno(f"arista {a} {rel} {b}: propiedades inesperadas {e['properties']}")
        else:
            if rel != "remite_a" or not all(f'"{nodos[x]["tipo"]}"' in tipos_contenido for x in (a, b)):
                freno(f"arista de remisión fuera de la firma derivada: {a} {rel} {b}")
            if sorted(e["properties"]) != ["alcance", "destino", "evidencia"]:
                freno(f"arista {a} {rel} {b}: propiedades {sorted(e['properties'])}")
        aristas.append({"a": a, "b": b, "relacion": rel, "clase": clase, "indice": e["indice"],
                        "properties": e["properties"]})
    return nodos, aristas, sub, diez, donde


# --------------------------------------------------------------------------- #
# Métricas de Helvetica para componer (la tabla de la versión 1)               #
# --------------------------------------------------------------------------- #
_W = {
    " ": 278, "!": 278, '"': 355, "#": 556, "$": 556, "%": 889, "&": 667,
    "'": 191, "(": 333, ")": 333, "*": 389, "+": 584, ",": 278, "-": 333,
    ".": 278, "/": 278, ":": 278, ";": 278, "?": 556, "@": 1015,
    "[": 278, "]": 278, "_": 556, "«": 500, "»": 500, "—": 1000, "–": 556,
}
for _c in "0123456789":
    _W[_c] = 556
for _c, _v in zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",
                  [667, 667, 722, 722, 667, 611, 778, 722, 278, 500, 667, 556,
                   833, 722, 778, 667, 778, 722, 667, 611, 722, 667, 944, 667,
                   667, 611]):
    _W[_c] = _v
for _c, _v in zip("abcdefghijklmnopqrstuvwxyz",
                  [556, 556, 500, 556, 556, 278, 556, 556, 222, 222, 500, 222,
                   833, 556, 556, 556, 556, 333, 500, 278, 556, 500, 722, 500,
                   500, 500]):
    _W[_c] = _v
for _acc, _base in [("á", "a"), ("é", "e"), ("ó", "o"), ("ú", "u"),
                    ("ñ", "n"), ("ü", "u"), ("Á", "A"), ("É", "E"), ("Í", "I"),
                    ("Ó", "O"), ("Ú", "U"), ("Ñ", "N")]:
    _W[_acc] = _W[_base]
_W["í"] = 278


def ancho(texto, fs, negrita=False):
    total = sum(_W.get(c, 556) for c in texto)
    return total / 1000.0 * fs * (1.04 if negrita else 1.0)


def envolver(texto, fs, ancho_max, negrita=False):
    lineas, actual = [], ""
    for palabra in texto.split(" "):
        cand = palabra if not actual else actual + " " + palabra
        if actual and ancho(cand, fs, negrita) > ancho_max:
            lineas.append(actual)
            actual = palabra
        else:
            actual = cand
    if actual:
        lineas.append(actual)
    return lineas


esc, f = base.esc, base.f

# --------------------------------------------------------------------------- #
# Primitivas de dibujo. Todo texto pasa por `texto()`, que lo deja registrado  #
# para la verificación de medidas.                                             #
# --------------------------------------------------------------------------- #
REGISTRO = []


def texto(partes, x, y, s, fs, negrita=False, relleno=TINTA, ancho_max=None, contexto="", rotulo=None):
    """Texto centrado en `x` con línea de base `y`."""
    peso = "bold" if negrita else "normal"
    marca = f' data-rotulo="{rotulo}"' if rotulo is not None else ""
    partes.append(f'<text x="{f(x)}" y="{f(y)}" text-anchor="middle" font-size="{fs}" '
                  f'font-weight="{peso}" fill="{relleno}"{marca}>{esc(s)}</text>')
    REGISTRO.append({"s": s, "fs": fs, "negrita": negrita, "cx": x, "y": y,
                     "ancho_max": ancho_max, "contexto": contexto})


def texto_izq(partes, x, y, s, fs, negrita=False, relleno=TINTA, contexto=""):
    peso = "bold" if negrita else "normal"
    partes.append(f'<text x="{f(x)}" y="{f(y)}" font-size="{fs}" font-weight="{peso}" '
                  f'fill="{relleno}">{esc(s)}</text>')
    REGISTRO.append({"s": s, "fs": fs, "negrita": negrita, "x0": x, "y": y,
                     "ancho_max": None, "contexto": contexto})


def caja(partes, x, y, w, h, clase, grosor="1.6", rx=8, guiones=False, nombre=None):
    dash = ' stroke-dasharray="5,4"' if guiones else ""
    marca = f' data-caja="{nombre}"' if nombre else ""
    partes.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" '
                  f'fill="{clase["relleno"]}" stroke="{clase["borde"]}" '
                  f'stroke-width="{grosor}" rx="{rx}"{dash}{marca}/>')


def trazo(partes, puntos, color, grosor, marcador, guiones=False, radio=9, arista=None):
    """Poligonal con esquinas redondeadas y punta de flecha al final."""
    d = f"M{f(puntos[0][0])},{f(puntos[0][1])}"
    for i in range(1, len(puntos) - 1):
        (x0, y0), (x1, y1), (x2, y2) = puntos[i - 1], puntos[i], puntos[i + 1]

        def hacia(xa, ya, xb, yb):
            largo = ((xb - xa) ** 2 + (yb - ya) ** 2) ** 0.5
            r = min(radio, largo / 2.0)
            return xa + (xb - xa) * r / largo, ya + (yb - ya) * r / largo

        ex, ey = hacia(x1, y1, x0, y0)
        sx, sy = hacia(x1, y1, x2, y2)
        d += f" L{f(ex)},{f(ey)} Q{f(x1)},{f(y1)} {f(sx)},{f(sy)}"
    d += f" L{f(puntos[-1][0])},{f(puntos[-1][1])}"
    dash = ' stroke-dasharray="5,4"' if guiones else ""
    marca = f' data-arista="{arista}"' if arista is not None else ""
    partes.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{grosor}"{dash} '
                  f'marker-end="url(#{marcador})"{marca}/>')


# --------------------------------------------------------------------------- #
# Geometría                                                                    #
# --------------------------------------------------------------------------- #
MARGEN = 10
SEP = 22                       # separación entre cajas (largo de la flecha)
PAD_X, PAD_Y = 10, 12
HOLGURA = 2
W_DOC, W_PROC = 104, 168


def lineas_de(clave, w):
    el = ELEMENTOS[clave]
    sub = envolver(el["sub"], FS_SUB, w - 2 * PAD_X - HOLGURA) if el["sub"] else []
    return el["rotulo"], sub


def alto_contenido(clave, w):
    rot, sub = lineas_de(clave, w)
    return len(rot) * IL_TITULO + (8 + len(sub) * IL_SUB if sub else 0)


def dibujar_proceso(partes, clave, x, y, w, h):
    el = ELEMENTOS[clave]
    caja(partes, x, y, w, h, el["clase"], nombre=f"etapa_{clave}")
    rot, sub = lineas_de(clave, w)
    cx = x + w / 2.0
    yy = y + (h - alto_contenido(clave, w)) / 2.0
    for linea in rot:
        texto(partes, cx, yy + FS_TITULO - 2, linea, FS_TITULO, True, TINTA, w - 2 * PAD_X, f"({clave}) rótulo")
        yy += IL_TITULO
    yy += 8
    for linea in sub:
        texto(partes, cx, yy + FS_SUB - 3, linea, FS_SUB, False, TINTA_SUB, w - 2 * PAD_X, f"({clave}) subtexto")
        yy += IL_SUB


def dibujar_documento(partes, x, y, w, h):
    """(a) Hoja con la esquina plegada y renglones; el rótulo va adentro."""
    p = 20
    clase = ELEMENTOS["a"]["clase"]
    partes.append(f'<path d="M{f(x + 4)},{f(y)} L{f(x + w - p)},{f(y)} '
                  f'L{f(x + w)},{f(y + p)} L{f(x + w)},{f(y + h - 4)} '
                  f'Q{f(x + w)},{f(y + h)} {f(x + w - 4)},{f(y + h)} '
                  f'L{f(x + 4)},{f(y + h)} Q{f(x)},{f(y + h)} {f(x)},{f(y + h - 4)} '
                  f'L{f(x)},{f(y + 4)} Q{f(x)},{f(y)} {f(x + 4)},{f(y)} Z" '
                  f'fill="{clase["relleno"]}" stroke="{clase["borde"]}" stroke-width="1.6"/>')
    partes.append(f'<path d="M{f(x + w - p)},{f(y)} L{f(x + w - p)},{f(y + p)} '
                  f'L{f(x + w)},{f(y + p)}" fill="none" stroke="{clase["borde"]}" stroke-width="1.6"/>')
    for k, largo in enumerate([0.52, 0.76, 0.76, 0.60]):
        yy = y + 22 + k * 11
        partes.append(f'<path d="M{f(x + 12)},{f(yy)} L{f(x + 12 + (w - 24) * largo)},{f(yy)}" '
                      f'stroke="#c4c4c4" stroke-width="3" stroke-linecap="round"/>')
    cx = x + w / 2.0
    yy = y + h - 16 - IL_TITULO
    for linea in ELEMENTOS["a"]["rotulo"]:
        texto(partes, cx, yy, linea, FS_TITULO, True, TINTA, w - 8, "(a) rótulo")
        yy += IL_TITULO


# Recuadro «Grafo», como en la versión 1: el nodo de arriba centrado, los otros
# dos abajo a izquierda y derecha, separados GAP_NODOS; las dos aristas salen
# del de arriba en diagonal con el rótulo al costado. Con el recuadro más ancho
# que en la versión 1 (la fila 2 tiene una caja de 168 en lugar de una de 192),
# los nodos de abajo se centran con la separación de la versión 1 (12) en lugar
# de pegarse a los bordes, y la diagonal llega a ENTRADA del centro del nodo de
# destino (16 en la versión 1), para que «condicion_de», más largo que «limita»,
# entre a la derecha de su trazo dentro del recuadro.
W_NODO, H_NODO = 132, 50
Y_NODOS, SEP_NODOS = 40, 52
GAP_NODOS = 12
ENTRADA = 30
ALTO_GRAFO = Y_NODOS + 2 * H_NODO + SEP_NODOS + 10


def dibujar_grafo(partes, x, y, w, h, nodos, aristas, colores):
    caja(partes, x, y, w, h, ELEMENTOS["g"]["clase"])
    cx = x + w / 2.0
    texto(partes, cx, y + 27, ELEMENTOS["g"]["rotulo"][0], FS_TITULO, True, TINTA, w - 2 * PAD_X, "(g) rótulo")
    y_sup = y + Y_NODOS
    y_inf = y_sup + H_NODO + SEP_NODOS
    pos = {"C": (cx - W_NODO / 2.0, y_sup), "D": (cx - GAP_NODOS / 2.0 - W_NODO, y_inf),
           "OP": (cx + GAP_NODOS / 2.0, y_inf)}
    cxn = {k: px + W_NODO / 2.0 for k, (px, _) in pos.items()}
    y_rot = (y_sup + H_NODO + y_inf) / 2.0
    for k, ar_ in enumerate(aristas):
        a, b, rel, clase = ar_["a"], ar_["b"], ar_["relacion"], ar_["clase"]
        if a != "C":
            freno(f"arista {a}-{b}: esta composición solo traza aristas que salen del nodo de arriba")
        remision = clase == "remision"
        color = ACENTO if remision else GRIS_ARISTA
        grosor = "2.6" if remision else "1.6"
        marcador = "arA" if remision else "arG"
        relleno = ACENTO_TEXTO if remision else GRIS_ROTULO
        lado = -1 if cxn[b] < cx else +1
        p0 = (cx + lado * 24, y_sup + H_NODO)
        p1 = (cxn[b] - lado * ENTRADA, y_inf - 2)
        trazo(partes, [p0, p1], color, grosor, marcador, arista=k)
        t = (y_rot + 11 - p0[1]) / (p1[1] - p0[1])
        x_trazo = p0[0] + (p1[0] - p0[0]) * t
        ar = ancho(rel, FS_SUB, remision)
        texto(partes, x_trazo + lado * (8 + ar / 2.0), y_rot + 6, rel, FS_SUB, remision, relleno, None,
              f"(g) arista {a}-{b} ({clase})", rotulo=k)
    for clave, _ in NODOS_FIGURA:
        nodo = nodos[clave]
        px, py = pos[clave]
        c = colores[nodo["tipo"]]
        partes.append(f'<rect x="{f(px)}" y="{f(py)}" width="{W_NODO}" height="{H_NODO}" '
                      f'fill="{c["relleno"]}" stroke="{c["borde"]}" stroke-width="{c["grosor"]}" '
                      f'rx="{base.RX_NODO}" data-caja="{clave}"/>')
        ncx = px + W_NODO / 2.0
        texto(partes, ncx, py + 21, nodo["tipo"], FS_SUB, False, TINTA, W_NODO - 10, f"(g) nodo {clave} tipo")
        texto(partes, ncx, py + 42, "punto " + nodo["punto"], FS_SUB, True, TINTA, W_NODO - 10,
              f"(g) nodo {clave} punto")


def componer(nodos, aristas, colores, perturbacion=None):
    del REGISTRO[:]
    partes = []

    # ---- fila 1: (a) (b) (c) (v) ------------------------------------------ #
    y1 = MARGEN + 6
    h1 = max(alto_contenido(k, W_PROC) for k in "bcv") + 2 * PAD_Y
    xa = MARGEN
    xb = xa + W_DOC + SEP
    xc = xb + W_PROC + SEP
    xv = xc + W_PROC + SEP
    cy1 = y1 + h1 / 2.0
    h_doc = 132
    dibujar_documento(partes, xa, cy1 - h_doc / 2.0, W_DOC, h_doc)
    for clave, x in (("b", xb), ("c", xc), ("v", xv)):
        dibujar_proceso(partes, clave, x, y1, W_PROC, h1)
    for x0, x1 in ((xa + W_DOC, xb), (xb + W_PROC, xc), (xc + W_PROC, xv)):
        trazo(partes, [(x0 + 2, cy1), (x1 - 2, cy1)], FLECHA, "1.8", "arN")

    # ---- entre filas: la vuelta al extractor y la continuidad ------------- #
    y_lazo = y1 + h1 + 33               # tramo horizontal de «vuelve a extraer»
    y_cont = y_lazo + 16                # tramo horizontal de la continuidad
    y2 = y_cont + 30
    xd = MARGEN
    xe = xd + W_PROC + SEP
    xg = xe + W_PROC + SEP
    wg = W - MARGEN - xg
    hg = ALTO_GRAFO
    h2 = max(alto_contenido("d", W_PROC), alto_contenido("e", W_PROC)) + 2 * PAD_Y
    cy2 = y2 + hg / 2.0
    yd = cy2 - h2 / 2.0
    cxc, cxd = xc + W_PROC / 2.0, xd + W_PROC / 2.0
    x_vuelta = xd + 30                  # sale de (d) a la izquierda de la continuidad
    x_cont = W - MARGEN - 8

    # ---- fila 2: (d) (e) (g) ---------------------------------------------- #
    dibujar_proceso(partes, "d", xd, yd, W_PROC, h2)
    dibujar_proceso(partes, "e", xe, yd, W_PROC, h2)
    dibujar_grafo(partes, xg, y2, wg, hg, nodos, aristas, colores)
    for x0, x1 in ((xd + W_PROC, xe), (xe + W_PROC, xg)):
        trazo(partes, [(x0 + 2, cy2), (x1 - 2, cy2)], FLECHA, "1.8", "arN")

    # ---- flecha de continuidad (v) → (d) ---------------------------------- #
    trazo(partes, [(xv + W_PROC + 2, cy1), (x_cont, cy1), (x_cont, y_cont), (cxd, y_cont), (cxd, yd - 2)],
          FLECHA, "1.8", "arN")

    # ---- salidas laterales de (d) ----------------------------------------- #
    x_sale = x_vuelta if perturbacion != "salida_cruza" else cxd + 40
    trazo(partes, [(x_sale, yd), (x_sale, y_lazo), (cxc, y_lazo), (cxc, y1 + h1 + 2)],
          GRIS_ARISTA, "1.6", "arG", guiones=True, arista="vuelta")
    texto(partes, (x_vuelta + cxc) / 2.0, y_lazo - 9, SALIDA_VUELVE, FS_SUB, False, GRIS_ROTULO,
          cxc - x_vuelta, "(d) salida lateral 1", rotulo="vuelta")
    w_marc = max(ancho(s, FS_SUB) for s in SALIDA_MARCADO) + 26
    h_marc = len(SALIDA_MARCADO) * IL_SUB + 14
    y_marc = yd + h2 + 26
    trazo(partes, [(cxd, yd + h2), (cxd, y_marc - 2)], GRIS_ARISTA, "1.6", "arG", guiones=True)
    caja(partes, cxd - w_marc / 2.0, y_marc, w_marc, h_marc, {"relleno": "white", "borde": GRIS_ARISTA},
         grosor="1.3", rx=8, guiones=True, nombre="marcado")
    yy = y_marc + 7 + FS_SUB - 2
    for linea in SALIDA_MARCADO:
        texto(partes, cxd, yy, linea, FS_SUB, False, GRIS_ROTULO, w_marc - 12, "(d) salida lateral 2")
        yy += IL_SUB

    # ---- leyenda ----------------------------------------------------------- #
    y_ley = max(y2 + hg, y_marc + h_marc) + 20
    h_ley = 68
    partes.append(f'<rect x="{f(MARGEN)}" y="{f(y_ley)}" width="{f(W - 2 * MARGEN)}" '
                  f'height="{h_ley}" fill="white" stroke="#e2e2e2" rx="5"/>')
    xx = MARGEN + 18
    for clase, rotulo in LEYENDA:
        partes.append(f'<rect x="{f(xx)}" y="{f(y_ley + 12)}" width="24" height="16" '
                      f'fill="{clase["relleno"]}" stroke="{clase["borde"]}" stroke-width="1.6" rx="3"/>')
        texto_izq(partes, xx + 33, y_ley + 26, rotulo, FS_SUB, False, TINTA, "leyenda")
        xx += 33 + ancho(rotulo, FS_SUB) + 40
    xx, y_fl = MARGEN + 18, y_ley + 48
    partes.append(f'<path d="M{f(xx)},{f(y_fl)} L{f(xx + 44)},{f(y_fl)}" fill="none" '
                  f'stroke="{ACENTO}" stroke-width="2.6" marker-end="url(#arA)"/>')
    texto_izq(partes, xx + 58, y_ley + 54, LEYENDA_REMISION, FS_SUB, True, ACENTO_TEXTO, "leyenda")
    alto_total = y_ley + h_ley + MARGEN

    alto_cm = ANCHO_FIGURA_CM * alto_total / W
    cabeza = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{ANCHO_FIGURA_CM:.2f}cm" '
        f'height="{alto_cm:.2f}cm" viewBox="0 0 {W} {f(alto_total)}" font-family="{TIPOGRAFIA}">',
        f'<rect width="{W}" height="{f(alto_total)}" fill="white"/>',
        '<defs>'
        '<marker id="arN" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
        f'markerHeight="6" orient="auto"><path d="M0,0L10,5L0,10z" fill="{FLECHA}"/></marker>'
        '<marker id="arG" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
        f'markerHeight="6" orient="auto"><path d="M0,0L10,5L0,10z" fill="{GRIS_ARISTA}"/></marker>'
        '<marker id="arA" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
        f'markerHeight="6" orient="auto"><path d="M0,0L10,5L0,10z" fill="{ACENTO}"/></marker>'
        '</defs>',
    ]
    return "\n".join(cabeza + partes + ["</svg>"]) + "\n", alto_total


# --------------------------------------------------------------------------- #
# Controles                                                                    #
# --------------------------------------------------------------------------- #
def verificar_medidas(alto_total):
    """Cada texto, medido con las métricas reales de Helvetica: entra en su
    caja, no sale del lienzo, no queda por debajo de PT_MINIMO y no se
    superpone con otro."""
    medir = base.medidor()
    fallas, cajas = [], []
    for r in REGISTRO:
        a = medir(r["s"], r["fs"], r["negrita"])
        x0 = r["x0"] if "x0" in r else r["cx"] - a / 2.0
        bb = (x0, r["y"] - r["fs"] * 0.78, x0 + a, r["y"] + r["fs"] * 0.22)
        cajas.append((r, bb))
        if puntos_impresos(r["fs"]) < PT_MINIMO:
            fallas.append(f"{r['s']!r}: letra {puntos_impresos(r['fs']):.2f} pt < {PT_MINIMO}")
        if r["ancho_max"] is not None and a > r["ancho_max"]:
            fallas.append(f"{r['s']!r}: ancho {a:.1f} > caja {r['ancho_max']:.1f}")
        if bb[0] < 0 or bb[2] > W or bb[1] < 0 or bb[3] > alto_total:
            fallas.append(f"{r['s']!r}: fuera del lienzo")
    for i in range(len(cajas)):
        for j in range(i + 1, len(cajas)):
            (ra, a), (rb, b) = cajas[i], cajas[j]
            if base.se_solapan(a, b):
                fallas.append(f"{ra['s']!r} se superpone con {rb['s']!r}")
    return fallas


def inventario(svg):
    """Nodos (tipo, punto) y aristas (origen, relación, destino) del recuadro
    «Grafo», releídos del SVG: cajas rx=7, sus dos textos, y los trazos con
    data-arista con sus extremos a 3 unidades o menos del borde de una caja."""
    raiz = ET.fromstring(svg)
    cajas = {}
    for r in raiz.iter(NS + "rect"):
        if r.get("data-caja") and r.get("rx") == str(base.RX_NODO):
            x, y, ww, hh = (float(r.get(k)) for k in ("x", "y", "width", "height"))
            cajas[r.get("data-caja")] = (x, y, x + ww, y + hh)
    textos = list(raiz.iter(NS + "text"))
    nodos = {}
    for k, R in cajas.items():
        dentro = sorted((t for t in textos if R[0] < float(t.get("x")) < R[2] and R[1] < float(t.get("y")) < R[3]),
                        key=lambda t: float(t.get("y")))
        s = [t.text for t in dentro]
        nodos[k] = (s[0], s[1][len("punto "):]) if len(s) == 2 and s[1].startswith("punto ") else None
    rotulos = {t.get("data-rotulo"): t.text for t in textos if t.get("data-rotulo") is not None}

    def caja_de(p):
        en = [k for k, R in cajas.items() if R[0] - 3 <= p[0] <= R[2] + 3 and R[1] - 3 <= p[1] <= R[3] + 3
              and not (R[0] + 3 < p[0] < R[2] - 3 and R[1] + 3 < p[1] < R[3] - 3)]
        return en[0] if len(en) == 1 else None
    aristas = []
    for p in raiz.iter(NS + "path"):
        ident = p.get("data-arista")
        if ident is None or ident == "vuelta":
            continue
        pts = base.puntos_de(p.get("d"))
        o, d = caja_de(pts[0]), caja_de(pts[-1])
        aristas.append((nodos.get(o), rotulos.get(ident), nodos.get(d)))
    return list(nodos.values()), aristas


def controlar_inventario(svg, nodos, aristas):
    dib_n, dib_a = inventario(svg)
    esp_n = [(n["tipo"], n["punto"]) for n in nodos.values()]
    esp_a = [((nodos[a["a"]]["tipo"], nodos[a["a"]]["punto"]), a["relacion"],
              (nodos[a["b"]]["tipo"], nodos[a["b"]]["punto"])) for a in aristas]
    fallas = []
    for nombre, esp, dib in (("nodo", esp_n, dib_n), ("arista", esp_a, dib_a)):
        for x in sorted((Counter(esp) - Counter(dib)).elements(), key=str):
            fallas.append(f"{nombre} del grafo que no está en la figura: {x}")
        for x in sorted((Counter(dib) - Counter(esp)).elements(), key=str):
            fallas.append(f"{nombre} de la figura que no está en el grafo: {x}")
    return fallas, dib_n, dib_a


PRUEBAS_NEGATIVAS = (("arista_de_mas", "inventario", "arista de la figura que no está en el grafo"),
                     ("salida_cruza", "geometria", "cruce(s) entre trazos"))


def controlar(nodos, aristas, colores, perturbacion=None):
    dib = list(aristas)
    if perturbacion == "arista_de_mas":
        dib.append({"a": "C", "b": "OP", "relacion": "remite_a", "clase": "remision"})
    svg, alto = componer(nodos, dib, colores, perturbacion)
    c = {"medidas": verificar_medidas(alto)}
    c["inventario"], dib_n, dib_a = controlar_inventario(svg, nodos, aristas)
    c["geometria"], info = base.controlar_geometria(svg, ANCHO_FIGURA_CM, W)
    return svg, alto, c, info, dib_n, dib_a


def pruebas_negativas(nodos, aristas, colores):
    vivas = []
    for caso, control, patron in PRUEBAS_NEGATIVAS:
        _, _, c, _, _, _ = controlar(nodos, aristas, colores, caso)
        propia = [x for x in c[control] if patron in x]
        if not propia:
            freno(f"la prueba negativa {caso} no hizo fallar el control de {control} con «{patron}»")
        vivas.append((caso, control, propia[0], sorted(k for k, v in c.items() if v and k != control)))
    return vivas


def argumentos():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--salida", default=AQUI,
                    help="directorio donde escribir el SVG, el PNG y el PDF (por omisión, el del script)")
    ap.add_argument("--perturbar", choices=[c for c, _, _ in PRUEBAS_NEGATIVAS], default=None,
                    help="compone la figura con ese defecto: los controles fallan y no se escribe nada")
    return ap.parse_args()


def main():
    args = argumentos()
    nodos, aristas, sub, diez, donde = cargar_grafo()
    colores = base.leer_colores_tipo()
    print("FUENTES (sha256 comprobado):")
    for nombre, par in (("grafo", base.GRAFO), ("grafo diez", base.GRAFO_DIEZ), ("estilo", base.ESTILO),
                        ("esquema r2", MODELOS_R2)):
        print(f"  {nombre:11s} {par[0]}   {par[1]}")
    print(f"  {MODELOS_R2[0]}: " + ", ".join(f"{k} :{v}" for k, v in donde.items()))
    for clave, _ in NODOS_FIGURA:
        n = nodos[clave]
        print(f"  nodo {clave:2s} {n['tipo']:10s} punto {n['punto']:8s} {n['id']}")
        print(f"          etiqueta en el grafo: {n['etiqueta']!r}")
    for a in aristas:
        print(f"  arista kg['edges'][{a['indice']}]  {a['a']} --{a['relacion']}--> {a['b']}  ({a['clase']}; "
              f"properties {a['properties']})")
    vivas = pruebas_negativas(nodos, aristas, colores)
    print(f"PRUEBAS NEGATIVAS: {len(vivas)} de {len(PRUEBAS_NEGATIVAS)} hacen fallar su control")
    for caso, control, falla, otros in vivas:
        print(f"  {caso} -> {control}: {falla}" + (f" (fallan también: {', '.join(otros)})" if otros else ""))
    svg, alto, c, info, dib_n, dib_a = controlar(nodos, aristas, colores, args.perturbar)
    if args.perturbar:
        print(f"PERTURBACIÓN: {args.perturbar}")
    print(f"MEDIDAS: {len(REGISTRO)} textos medidos con las métricas reales de Helvetica; fallas: {len(c['medidas'])}")
    print(f"INVENTARIO (releído del SVG): nodos {dib_n}; aristas {dib_a}; fallas: {len(c['inventario'])}")
    print(f"GEOMETRÍA: {info['textos']} textos, {info['cajas']} cajas, {info['trazos']} trazos con flecha; "
          f"cruces {len(info['cruces'])}; fallas: {len(c['geometria'])}")
    for k in c:
        for falla in c[k]:
            print(f"  MAL [{k}] {falla}")
    if any(c.values()):
        raise SystemExit("FALLA: la figura tiene defectos; no se escribe nada")
    print(f"TAMAÑO: lienzo {W} x {alto:.0f}, impreso a {ANCHO_FIGURA_CM:.2f} x {ANCHO_FIGURA_CM * alto / W:.2f} cm")
    for nombre, fs in (("rótulos de elemento", FS_TITULO), ("subtextos, salidas, nodos, leyenda", FS_SUB)):
        print(f"  {nombre:36s} {fs} -> {puntos_impresos(fs):5.2f} pt (mínimo {PT_MINIMO})")
    rutas = base.exportar(svg, args.salida, NOMBRE, ANCHO_FIGURA_CM)
    for e in ("svg", "png", "pdf"):
        print(f"{e.upper()}: {os.path.relpath(rutas[e], base.RAIZ)}   sha256 {base.sha256(rutas[e])}")
    print(f"  PNG {base.png_dimensiones(rutas['png'])} px a {base.DPI} dpi; {base.version_rsvg()}")


if __name__ == "__main__":
    try:
        main()
    except base.Freno as e:
        raise SystemExit(f"FRENO {e}")
