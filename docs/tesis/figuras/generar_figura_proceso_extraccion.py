#!/usr/bin/env python3
"""Figura «del documento al grafo» para la Introducción.

Siete elementos en secuencia de izquierda a derecha, en dos filas unidas por
una flecha de continuidad: el Texto Ordenado de entrada, las cinco etapas del
proceso y el grafo de salida. Dos colores distinguen las etapas que ejecuta un
modelo de lenguaje de las determinísticas; la leyenda va al pie.

Misma técnica, tipografía y paleta por tipo de nodo que la figura «de la norma
al grafo»: el SVG se escribe a mano, sin dependencias externas ni red, y la
generación es determinística (dos corridas producen el mismo SVG byte a byte).
El PNG se exporta con rsvg-convert al ancho físico de la figura a 300 dpi, y
el script le graba la densidad en el encabezado.

Los tres nodos y las dos aristas del panel «Grafo» no se tipean: se toman del
grafo r1 (kg.json) por consulta —documento, tipo y punto de procedencia de
cada nodo; origen, relación y destino de cada arista— y el script comprueba al
generar que el archivo es el sellado, que cada búsqueda da exactamente un nodo
con esa procedencia y que cada arista existe con ese tipo. Cada nodo se rotula
con el nombre de su tipo y su punto de procedencia; la etiqueta que el nodo
tiene en el grafo se imprime al correr.

Uso:
    PYTHONDONTWRITEBYTECODE=1 python3 generar_figura_proceso_extraccion.py
    PYTHONDONTWRITEBYTECODE=1 python3 generar_figura_proceso_extraccion.py --verificar

Con --verificar, además, mide cada texto con las métricas reales de Helvetica
(requiere PIL y la fuente del sistema; si faltan, lo informa y sigue) y
comprueba que ningún texto exceda su caja, se superponga con otro, salga del
lienzo ni quede por debajo del tamaño mínimo impreso.
"""

import hashlib
import json
import os
import shutil
import struct
import subprocess
import sys
import zlib

AQUI = os.path.dirname(os.path.abspath(__file__))
SALIDA_SVG = os.path.join(AQUI, "figura_proceso_extraccion.svg")
SALIDA_PNG = os.path.join(AQUI, "figura_proceso_extraccion.png")
RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", ".."))
KG = os.path.join(RAIZ, "data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json")
# sha256 del kg.json sobre el que se verificó la figura (U-FIG-PROC-V,
# reports/verificacion_figura_proceso.md §1). Si el archivo cambia, el script
# frena: la figura afirma que estos nodos y aristas están en ese grafo.
KG_SHA256 = "0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a"

# --------------------------------------------------------------------------- #
# Tamaño impreso                                                               #
# A4 con márgenes de 3 cm: ancho de texto 21 - 6 = 15 cm. La figura entra a    #
# 0,85 de ese ancho. Todo tamaño de letra se controla contra ese ancho físico. #
# --------------------------------------------------------------------------- #
ANCHO_TEXTO_CM = 15.0
FRACCION = 0.85
ANCHO_FIGURA_CM = ANCHO_TEXTO_CM * FRACCION          # 12,75 cm
PT_POR_CM = 72.0 / 2.54
ANCHO_FIGURA_PT = ANCHO_FIGURA_CM * PT_POR_CM         # 361,4 pt
DPI = 300
ANCHO_PNG_PX = round(ANCHO_FIGURA_CM / 2.54 * DPI)    # 1506 px
PT_MINIMO = 9.0

W = 720                                               # unidades del lienzo


def puntos_impresos(px):
    """Tamaño en puntos de `px` unidades del lienzo con la figura a 12,75 cm."""
    return px * ANCHO_FIGURA_PT / W


# --------------------------------------------------------------------------- #
# Paleta y tipografía                                                          #
# COLOR_TIPO: copiada de generar_figura_norma_a_grafo.py (COLOR_TIPO).         #
# --------------------------------------------------------------------------- #
TIPOGRAFIA = "Helvetica,Arial,sans-serif"
COLOR_TIPO = {
    "Restriccion": "#b23a48",
    "Obligacion": "#2a6f97",
    "Operacion": "#52796f",
    "Sujeto": "#6d597a",
}
# Cajas de proceso: relleno claro y borde del mismo tono, texto oscuro. Los
# nodos del grafo van en color pleno con texto blanco, de modo que las dos
# codificaciones (clase de etapa, tipo de nodo) no se confunden.
MODELO = {"relleno": "#fbe3d3", "borde": "#e07b39"}           # modelo de lenguaje
DETERMINISTICA = {"relleno": "#e1e7ee", "borde": "#4a5a6a"}   # determinística
NEUTRO = {"relleno": "#fafafa", "borde": "#999999"}
TINTA = "#1f1f1f"
TINTA_SUB = "#444444"
FLECHA = "#555555"
GRIS_ARISTA = "#8a8a8a"
GRIS_ROTULO = "#555555"
# Trazo de remisión: ACENTO y ACENTO_TEXTO de generar_figura_norma_a_grafo.py
# (:92-93), con su grosor (2.6) y su punta de flecha.
ACENTO = "#e07b39"
ACENTO_TEXTO = "#8a4513"

FS_TITULO = 19        # rótulo de cada elemento, en negrita
FS_SUB = 18           # subtexto, rótulos laterales, nodos y leyenda
IL_TITULO = 23
IL_SUB = 22

# --------------------------------------------------------------------------- #
# Contenido: siete elementos con rótulos y orden fijos, los del párrafo que    #
# la figura ilustra.                                                          #
# Los cortes de línea de los rótulos se fijan a mano; los subtextos se         #
# envuelven solos.                                                             #
# --------------------------------------------------------------------------- #
ELEMENTOS = {
    "a": {"rotulo": ["Texto", "Ordenado"], "sub": None, "clase": NEUTRO},
    "b": {"rotulo": ["Segmentación", "en puntos"],
          "sub": "siguiendo la estructura del propio documento",
          "clase": DETERMINISTICA},
    "c": {"rotulo": ["Extracción de", "entidades y", "relaciones"],
          "sub": "un modelo de lenguaje, bajo un esquema fijo",
          "clase": MODELO},
    "d": {"rotulo": ["Revisión contra", "el texto", "de origen"],
          "sub": "un segundo modelo",
          "clase": MODELO},
    "e": {"rotulo": ["Ensamblado en", "un único grafo"],
          "sub": "determinístico",
          "clase": DETERMINISTICA},
    "f": {"rotulo": ["Resolución de", "remisiones"],
          "sub": "arista si el punto citado se localiza; registrada como no "
                 "resuelta si no",
          "clase": DETERMINISTICA},
    "g": {"rotulo": ["Grafo"], "sub": None, "clase": NEUTRO},
}
SALIDA_VUELVE = "vuelve a extraer"
SALIDA_MARCADO = ["marcado para", "revisión humana"]
LEYENDA = [(MODELO, "Etapa que ejecuta un modelo de lenguaje"),
           (DETERMINISTICA, "Etapa determinística")]

# Nodos del panel «Grafo»: tres nodos del subgrafo de los dividendos del Texto
# Ordenado de Exterior y Cambios (reports/verificacion_figura_proceso.md §5.c y
# §8.g), los mismos que la figura «de la norma al grafo» usa como restricción de
# origen, operación limitada y una de las obligaciones remitidas. Cada nodo se
# identifica por (documento, tipo, punto de procedencia con rol punto_propio);
# la búsqueda en kg.json debe dar exactamente un nodo, del que salen el id, la
# etiqueta y el punto que se rotula. Tres nodos y no cuatro: los nodos de tipo
# Sujeto son de catálogo y no tienen un punto propio único, así que no pueden
# llevar el rótulo de procedencia que la figura quiere mostrar.
TO_FIGURA = "ext"
NODOS_FIGURA = [
    ("R", "Restriccion", "3.17.1.4"),    # requisitos para pagar dividendos
    ("O", "Obligacion", "3.4.2"),        # declaración jurada del representante
    ("OP", "Operacion", "3.17.1.4"),     # pago de dividendos a no residentes
]

# Aristas del panel, con la relación tal como está en el grafo y su clase.
# La de clase "extraccion" es una firma (tipo de origen, relación, tipo de
# destino) admitida por la matriz de dominio y rango del esquema congelado:
# DOMAIN_RANGE_CONGELADO, data/experiment/esq/code/prompt_congelado.py:97-99,
# que hereda sin cambios la fila de data/experiment/esq/code/prompt_esq3b.py
# :172 (limita). La de clase "remision" no sale de la extracción: es la arista
# que produce la resolución de remisiones (relación `referencia` con
# rol_fuente = referencia_cruzada,
# data/experiment/reextraccion_v2/corpus_v2/r1_referencias.py:231-234), y por
# eso no se coteja contra esa matriz sino contra ese rol_fuente. Cada arista
# debe existir en kg.json con ese origen, esa relación y ese destino.
FIRMAS_ADMITIDAS = {
    ("Restriccion", "limita", "Operacion"),
}
ARISTAS_FIGURA = [("R", "limita", "OP", "extraccion"),
                  ("R", "referencia", "O", "remision")]
ROL_REMISION = "referencia_cruzada"
# Predicados en castellano legible, como en generar_figura_norma_a_grafo.py.
CASTELLANO = {"referencia": "remite a"}
LEYENDA_REMISION = "remisión resuelta entre puntos"
# Rótulo de cada nodo: el nombre de su tipo (primera línea) y «punto N»
# (segunda línea, en negrita).
NOMBRE_TIPO = {"Restriccion": "Restricción", "Obligacion": "Obligación",
               "Operacion": "Operación", "Sujeto": "Sujeto"}


def provenances(elem):
    """Provenances del elemento sin duplicados, en el orden del archivo."""
    ps = ([elem["provenance"]] if elem.get("provenance") else []) + (elem.get("provenances") or [])
    vistos, salida = set(), []
    for p in ps:
        clave = (p.get("to"), p.get("punto"), p.get("rol_documental"))
        if clave not in vistos:
            vistos.add(clave)
            salida.append(p)
    return salida


def cargar_grafo():
    """Lee kg.json, comprueba su sha y resuelve los nodos y aristas del panel.

    Devuelve (nodos, aristas): `nodos` mapea clave -> dict con id, tipo, punto,
    etiqueta original y etiqueta a dibujar; `aristas` es una lista de dicts con
    origen, destino, relación, rótulo, clase e índice de la arista en
    kg['edges'] (las aristas del grafo no tienen id propio).
    """
    with open(KG, "rb") as fh:
        crudo = fh.read()
    sha = hashlib.sha256(crudo).hexdigest()
    if sha != KG_SHA256:
        raise SystemExit(f"kg.json no es el verificado: sha {sha[:12]}… ≠ {KG_SHA256[:12]}…")
    kg = json.loads(crudo.decode("utf-8"))

    nodos = {}
    for clave, tipo, punto in NODOS_FIGURA:
        cands = [n for n in kg["nodes"] if n["type"] == tipo and any(
            p.get("to") == TO_FIGURA and p.get("punto") == punto
            and p.get("rol_documental") == "punto_propio" for p in provenances(n))]
        if len(cands) != 1:
            raise SystemExit(f"nodo {clave}: ({TO_FIGURA}, {tipo}, {punto}) da "
                             f"{len(cands)} nodos, no uno: {[n['id'] for n in cands]}")
        n = cands[0]
        nodos[clave] = {"id": n["id"], "tipo": tipo, "punto": punto,
                        "etiqueta": n.get("label", "")}

    aristas = []
    for a, rel, b, clase in ARISTAS_FIGURA:
        ida, idb = nodos[a]["id"], nodos[b]["id"]
        hits = [(i, e) for i, e in enumerate(kg["edges"])
                if e["source"] == ida and e["target"] == idb and e["relation"] == rel]
        if len(hits) != 1:
            raise SystemExit(f"arista {a} {rel} {b}: {len(hits)} coincidencias en kg.json, no una")
        i, e = hits[0]
        if clase == "remision":
            if e.get("rol_fuente") != ROL_REMISION:
                raise SystemExit(f"arista {a} {rel} {b}: rol_fuente {e.get('rol_fuente')!r} "
                                 f"≠ {ROL_REMISION!r}")
        else:
            if (nodos[a]["tipo"], rel, nodos[b]["tipo"]) not in FIRMAS_ADMITIDAS:
                raise SystemExit(f"arista fuera de la matriz del esquema: {a} {rel} {b}")
            if e.get("rol_fuente") is not None:
                raise SystemExit(f"arista {a} {rel} {b}: rol_fuente inesperado {e.get('rol_fuente')!r}")
        aristas.append({"a": a, "b": b, "relacion": rel, "rotulo": CASTELLANO.get(rel, rel),
                        "clase": clase, "indice": i})
    return nodos, aristas

# --------------------------------------------------------------------------- #
# Métricas de Helvetica (unidades/1000 em), para envolver y centrar sin        #
# librerías de tipografía. Misma tabla que la figura «de la norma al grafo».   #
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
    """Ancho estimado en unidades del lienzo. Helvetica Bold es ~4 % más ancha."""
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


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def f(v):
    """Formato fijo: el SVG no debe depender de la representación del float."""
    return f"{v:.1f}"


# --------------------------------------------------------------------------- #
# Primitivas de dibujo. Todo texto pasa por `texto()`, que lo deja registrado  #
# para la verificación de medidas.                                             #
# --------------------------------------------------------------------------- #
REGISTRO = []


def texto(partes, x, y, s, fs, negrita=False, relleno=TINTA, ancho_max=None,
          contexto=""):
    """Texto centrado en `x` con línea de base `y`."""
    peso = "bold" if negrita else "normal"
    partes.append(f'<text x="{f(x)}" y="{f(y)}" text-anchor="middle" '
                  f'font-size="{fs}" font-weight="{peso}" fill="{relleno}">'
                  f'{esc(s)}</text>')
    REGISTRO.append({"s": s, "fs": fs, "negrita": negrita, "cx": x, "y": y,
                     "ancho_max": ancho_max, "contexto": contexto})


def texto_izq(partes, x, y, s, fs, negrita=False, relleno=TINTA, contexto=""):
    """Texto alineado a la izquierda en `x` (solo la leyenda lo usa)."""
    peso = "bold" if negrita else "normal"
    partes.append(f'<text x="{f(x)}" y="{f(y)}" font-size="{fs}" '
                  f'font-weight="{peso}" fill="{relleno}">{esc(s)}</text>')
    REGISTRO.append({"s": s, "fs": fs, "negrita": negrita, "x0": x, "y": y,
                     "ancho_max": None, "contexto": contexto})


def caja(partes, x, y, w, h, clase, grosor="1.6", rx=8, guiones=False):
    dash = ' stroke-dasharray="5,4"' if guiones else ""
    partes.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" '
                  f'fill="{clase["relleno"]}" stroke="{clase["borde"]}" '
                  f'stroke-width="{grosor}" rx="{rx}"{dash}/>')


def trazo(partes, puntos, color, grosor, marcador, guiones=False, radio=9):
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
    partes.append(f'<path d="{d}" fill="none" stroke="{color}" '
                  f'stroke-width="{grosor}"{dash} marker-end="url(#{marcador})"/>')


# --------------------------------------------------------------------------- #
# Geometría                                                                    #
# --------------------------------------------------------------------------- #
MARGEN = 10
SEP = 22                       # separación entre cajas (largo de la flecha)
PAD_X, PAD_Y = 10, 12
HOLGURA = 2                    # margen de seguridad al envolver subtextos
W_DOC, W_PROC, W_F = 104, 168, 192


def lineas_de(clave, w):
    el = ELEMENTOS[clave]
    sub = envolver(el["sub"], FS_SUB, w - 2 * PAD_X - HOLGURA) if el["sub"] else []
    return el["rotulo"], sub


def alto_contenido(clave, w):
    rot, sub = lineas_de(clave, w)
    return len(rot) * IL_TITULO + (8 + len(sub) * IL_SUB if sub else 0)


def dibujar_proceso(partes, clave, x, y, w, h):
    """Caja de etapa: rótulo en negrita y subtexto, centrados en la caja."""
    el = ELEMENTOS[clave]
    caja(partes, x, y, w, h, el["clase"])
    rot, sub = lineas_de(clave, w)
    cx = x + w / 2.0
    yy = y + (h - alto_contenido(clave, w)) / 2.0
    for linea in rot:
        texto(partes, cx, yy + FS_TITULO - 2, linea, FS_TITULO, True, TINTA,
              w - 2 * PAD_X, f"({clave}) rótulo")
        yy += IL_TITULO
    yy += 8
    for linea in sub:
        texto(partes, cx, yy + FS_SUB - 3, linea, FS_SUB, False, TINTA_SUB,
              w - 2 * PAD_X, f"({clave}) subtexto")
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
                  f'L{f(x + w)},{f(y + p)}" fill="none" stroke="{clase["borde"]}" '
                  f'stroke-width="1.6"/>')
    for k, largo in enumerate([0.52, 0.76, 0.76, 0.60]):
        yy = y + 22 + k * 11
        partes.append(f'<path d="M{f(x + 12)},{f(yy)} L{f(x + 12 + (w - 24) * largo)},{f(yy)}" '
                      f'stroke="#c4c4c4" stroke-width="3" stroke-linecap="round"/>')
    cx = x + w / 2.0
    yy = y + h - 16 - IL_TITULO
    for linea in ELEMENTOS["a"]["rotulo"]:
        texto(partes, cx, yy, linea, FS_TITULO, True, TINTA, w - 8, "(a) rótulo")
        yy += IL_TITULO


# Composición original de la figura: la Restricción arriba, centrada; la
# Obligación abajo a la izquierda y la Operación abajo a la derecha; las dos
# aristas salen de la Restricción en diagonal con el rótulo al costado. El ancho
# de nodo era 116 y pasa a 132 porque «punto 3.17.1.4» en negrita mide 120
# unidades a 18 px. Sin la arista «requiere», el panel termina 10 unidades
# debajo de la fila inferior de nodos.
W_NODO, H_NODO = 132, 50
Y_NODOS, SEP_NODOS = 40, 52      # arranque de los nodos y separación entre filas
ALTO_GRAFO = Y_NODOS + 2 * H_NODO + SEP_NODOS + 10


def dibujar_grafo(partes, x, y, w, h, nodos, aristas):
    """(g) Contenedor neutro con el rótulo, los tres nodos en triángulo y las
    dos aristas con el nombre de su relación."""
    caja(partes, x, y, w, h, ELEMENTOS["g"]["clase"])
    cx = x + w / 2.0
    texto(partes, cx, y + 27, ELEMENTOS["g"]["rotulo"][0], FS_TITULO, True,
          TINTA, w - 2 * PAD_X, "(g) rótulo")
    y_sup = y + Y_NODOS
    y_inf = y_sup + H_NODO + SEP_NODOS
    pos = {
        "R": (cx - W_NODO / 2.0, y_sup),
        "O": (x + PAD_X, y_inf),
        "OP": (x + w - PAD_X - W_NODO, y_inf),
    }
    cxn = {k: px + W_NODO / 2.0 for k, (px, _) in pos.items()}
    y_rot = (y_sup + H_NODO + y_inf) / 2.0          # centro de la franja entre filas

    for ar_ in aristas:
        a, b, rel, clase = ar_["a"], ar_["b"], ar_["rotulo"], ar_["clase"]
        if a != "R":
            raise SystemExit(f"arista {a}-{b}: esta composición solo traza aristas "
                             f"que salen de la Restricción")
        remision = clase == "remision"
        color = ACENTO if remision else GRIS_ARISTA
        grosor = "2.6" if remision else "1.6"
        marcador = "arA" if remision else "arG"
        relleno = ACENTO_TEXTO if remision else GRIS_ROTULO
        # Diagonal desde el borde inferior de la Restricción; el rótulo va del
        # lado de afuera, a 8 unidades del trazo a la altura de su base.
        lado = -1 if cxn[b] < cx else +1
        p0 = (cx + lado * 24, y_sup + H_NODO)
        p1 = (cxn[b] - lado * 16, y_inf - 2)
        trazo(partes, [p0, p1], color, grosor, marcador)
        t = (y_rot + 11 - p0[1]) / (p1[1] - p0[1])
        x_trazo = p0[0] + (p1[0] - p0[0]) * t
        ar = ancho(rel, FS_SUB, remision)
        texto(partes, x_trazo + lado * (8 + ar / 2.0), y_rot + 6, rel, FS_SUB,
              remision, relleno, None, f"(g) arista {a}-{b} ({clase})")

    for clave, _, _ in NODOS_FIGURA:
        nodo = nodos[clave]
        px, py = pos[clave]
        partes.append(f'<rect x="{f(px)}" y="{f(py)}" width="{W_NODO}" height="{H_NODO}" '
                      f'fill="{COLOR_TIPO[nodo["tipo"]]}" fill-opacity="0.95" '
                      f'stroke="black" stroke-width="1.4" rx="7"/>')
        ncx = px + W_NODO / 2.0
        texto(partes, ncx, py + 21, NOMBRE_TIPO[nodo["tipo"]], FS_SUB, False, "white",
              W_NODO - 10, f"(g) nodo {clave} rótulo")
        texto(partes, ncx, py + 42, "punto " + nodo["punto"], FS_SUB, True, "white",
              W_NODO - 10, f"(g) nodo {clave} punto")


def componer(nodos, aristas):
    del REGISTRO[:]
    partes = []

    # ---- fila 1: (a) (b) (c) (d) ------------------------------------------ #
    y_lazo = MARGEN + FS_SUB + 10            # tramo horizontal de «vuelve a extraer»
    y1 = y_lazo + 30
    h1 = max(alto_contenido(k, W_PROC) for k in "bcd") + 2 * PAD_Y
    xa = MARGEN
    xb = xa + W_DOC + SEP
    xc = xb + W_PROC + SEP
    xd = xc + W_PROC + SEP
    cy1 = y1 + h1 / 2.0
    h_doc = 132
    dibujar_documento(partes, xa, cy1 - h_doc / 2.0, W_DOC, h_doc)
    for clave, x in (("b", xb), ("c", xc), ("d", xd)):
        dibujar_proceso(partes, clave, x, y1, W_PROC, h1)
    for x0, x1 in ((xa + W_DOC, xb), (xb + W_PROC, xc), (xc + W_PROC, xd)):
        trazo(partes, [(x0 + 2, cy1), (x1 - 2, cy1)], FLECHA, "1.8", "arN")

    # ---- salidas laterales de (d) ----------------------------------------- #
    cxc, cxd = xc + W_PROC / 2.0, xd + W_PROC / 2.0
    trazo(partes, [(cxd, y1), (cxd, y_lazo), (cxc, y_lazo), (cxc, y1 - 2)],
          GRIS_ARISTA, "1.6", "arG", guiones=True)
    texto(partes, (cxc + cxd) / 2.0, y_lazo - 9, SALIDA_VUELVE, FS_SUB, False,
          GRIS_ROTULO, cxd - cxc, "(d) salida lateral 1")

    w_marc = max(ancho(s, FS_SUB) for s in SALIDA_MARCADO) + 26
    h_marc = len(SALIDA_MARCADO) * IL_SUB + 14
    y_marc = y1 + h1 + 26
    trazo(partes, [(cxd, y1 + h1), (cxd, y_marc - 2)], GRIS_ARISTA, "1.6", "arG",
          guiones=True)
    caja(partes, cxd - w_marc / 2.0, y_marc, w_marc, h_marc,
         {"relleno": "white", "borde": GRIS_ARISTA}, grosor="1.3", rx=8, guiones=True)
    yy = y_marc + 7 + FS_SUB - 2
    for linea in SALIDA_MARCADO:
        texto(partes, cxd, yy, linea, FS_SUB, False, GRIS_ROTULO, w_marc - 12,
              "(d) salida lateral 2")
        yy += IL_SUB

    # ---- fila 2: (e) (f) (g) ---------------------------------------------- #
    y_cont = y_marc + h_marc + 16            # tramo horizontal de la continuidad
    y2 = y_cont + 30
    xe = MARGEN
    xf = xe + W_PROC + SEP
    xg = xf + W_F + SEP
    wg = W - MARGEN - xg
    hg = ALTO_GRAFO
    h2 = max(alto_contenido("e", W_PROC), alto_contenido("f", W_F)) + 2 * PAD_Y
    cy2 = y2 + hg / 2.0
    ye = cy2 - h2 / 2.0
    dibujar_proceso(partes, "e", xe, ye, W_PROC, h2)
    dibujar_proceso(partes, "f", xf, ye, W_F, h2)
    dibujar_grafo(partes, xg, y2, wg, hg, nodos, aristas)
    for x0, x1 in ((xe + W_PROC, xf), (xf + W_F, xg)):
        trazo(partes, [(x0 + 2, cy2), (x1 - 2, cy2)], FLECHA, "1.8", "arN")

    # ---- flecha de continuidad (d) → (e) ---------------------------------- #
    x_cont = W - MARGEN - 8
    cxe = xe + W_PROC / 2.0
    trazo(partes, [(xd + W_PROC + 2, cy1), (x_cont, cy1), (x_cont, y_cont),
                   (cxe, y_cont), (cxe, ye - 2)], FLECHA, "1.8", "arN")

    # ---- leyenda ----------------------------------------------------------- #
    y_ley = y2 + hg + 20
    h_ley = 68
    partes.append(f'<rect x="{f(MARGEN)}" y="{f(y_ley)}" width="{f(W - 2 * MARGEN)}" '
                  f'height="{h_ley}" fill="white" stroke="#e2e2e2" rx="5"/>')
    xx = MARGEN + 18
    for clase, rotulo in LEYENDA:
        partes.append(f'<rect x="{f(xx)}" y="{f(y_ley + 12)}" width="24" height="16" '
                      f'fill="{clase["relleno"]}" stroke="{clase["borde"]}" '
                      f'stroke-width="1.6" rx="3"/>')
        texto_izq(partes, xx + 33, y_ley + 26, rotulo, FS_SUB, False, TINTA, "leyenda")
        xx += 33 + ancho(rotulo, FS_SUB) + 40
    xx, y_fl = MARGEN + 18, y_ley + 48
    partes.append(f'<path d="M{f(xx)},{f(y_fl)} L{f(xx + 44)},{f(y_fl)}" fill="none" '
                  f'stroke="{ACENTO}" stroke-width="2.6" marker-end="url(#arA)"/>')
    texto_izq(partes, xx + 58, y_ley + 54, LEYENDA_REMISION, FS_SUB, True,
              ACENTO_TEXTO, "leyenda")
    alto_total = y_ley + h_ley + MARGEN

    alto_cm = ANCHO_FIGURA_CM * alto_total / W
    cabeza = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{ANCHO_FIGURA_CM:.2f}cm" '
        f'height="{alto_cm:.2f}cm" viewBox="0 0 {W} {f(alto_total)}" '
        f'font-family="{TIPOGRAFIA}">',
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
# PNG a 300 dpi                                                                #
# --------------------------------------------------------------------------- #
def grabar_densidad(ruta, dpi):
    """Inserta el bloque pHYs (píxeles por metro) después de IHDR."""
    with open(ruta, "rb") as fh:
        datos = fh.read()
    firma, resto = datos[:8], datos[8:]
    bloques, i = [], 0
    while i < len(resto):
        largo = struct.unpack(">I", resto[i:i + 4])[0]
        bloques.append((resto[i + 4:i + 8], resto[i:i + 12 + largo]))
        i += 12 + largo
    ppm = round(dpi / 0.0254)
    cuerpo = b"pHYs" + struct.pack(">IIB", ppm, ppm, 1)
    phys = struct.pack(">I", 9) + cuerpo + struct.pack(">I", zlib.crc32(cuerpo) & 0xFFFFFFFF)
    salida = firma
    for tipo, crudo in bloques:
        if tipo == b"pHYs":
            continue
        salida += crudo
        if tipo == b"IHDR":
            salida += phys
    with open(ruta, "wb") as fh:
        fh.write(salida)


def exportar_png():
    rsvg = shutil.which("rsvg-convert")
    if not rsvg:
        print("rsvg-convert no está instalado: se escribió el SVG y no el PNG.")
        return False
    subprocess.run([rsvg, "-w", str(ANCHO_PNG_PX), "-f", "png", "-o", SALIDA_PNG,
                    SALIDA_SVG], check=True)
    grabar_densidad(SALIDA_PNG, DPI)
    return True


# --------------------------------------------------------------------------- #
# Verificación de medidas                                                      #
# --------------------------------------------------------------------------- #
FUENTE_SISTEMA = "/System/Library/Fonts/Helvetica.ttc"


def medidor():
    """Devuelve una función ancho(s, fs, negrita) con métricas reales, o None."""
    try:
        from PIL import ImageFont
    except ImportError:
        return None
    if not os.path.exists(FUENTE_SISTEMA):
        return None
    cache = {}

    def medir(s, fs, negrita):
        clave = (fs, negrita)
        if clave not in cache:
            # La fuente se carga a 10x para medir con resolución de décimas.
            cache[clave] = ImageFont.truetype(FUENTE_SISTEMA, fs * 10,
                                              index=1 if negrita else 0)
        return cache[clave].getlength(s) / 10.0
    return medir


def verificar(alto_total):
    medir = medidor()
    fuente = "métricas reales de Helvetica" if medir else "tabla de métricas del script"
    if not medir:
        print("PIL o la fuente del sistema no están: se verifica con la tabla del script.")
        medir = ancho
    print(f"\nVERIFICACIÓN DE MEDIDAS ({fuente})")
    fallas, cajas = [], []
    for r in REGISTRO:
        a = medir(r["s"], r["fs"], r["negrita"])
        x0 = r["x0"] if "x0" in r else r["cx"] - a / 2.0
        bb = (x0, r["y"] - r["fs"] * 0.78, x0 + a, r["y"] + r["fs"] * 0.22)
        cajas.append((r, bb))
        pt = puntos_impresos(r["fs"])
        estado = []
        if pt < PT_MINIMO:
            estado.append(f"letra {pt:.2f} pt < {PT_MINIMO}")
        if r["ancho_max"] is not None and a > r["ancho_max"]:
            estado.append(f"ancho {a:.1f} > caja {r['ancho_max']:.1f}")
        if bb[0] < 0 or bb[2] > W or bb[1] < 0 or bb[3] > alto_total:
            estado.append("fuera del lienzo")
        tope = f"{r['ancho_max']:6.1f}" if r["ancho_max"] is not None else "     –"
        print(f"  {'MAL' if estado else 'ok '} {pt:5.2f} pt  ancho {a:6.1f} / {tope}  "
              f"{r['contexto']:26s} {r['s']!r}" + ("  <-- " + "; ".join(estado) if estado else ""))
        fallas += [(r["s"], e) for e in estado]
    for i in range(len(cajas)):
        for j in range(i + 1, len(cajas)):
            (ra, a), (rb, b) = cajas[i], cajas[j]
            if a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]:
                fallas.append((ra["s"], f"se superpone con {rb['s']!r}"))
                print(f"  MAL superposición: {ra['s']!r} / {rb['s']!r}")
    print(f"  textos medidos: {len(REGISTRO)}   fallas: {len(fallas)}")
    return not fallas


def main():
    nodos, aristas = cargar_grafo()
    print(f"GRAFO: {os.path.relpath(KG, RAIZ)}   sha256 {KG_SHA256[:12]}… (comprobado)")
    for clave, _, _ in NODOS_FIGURA:
        n = nodos[clave]
        print(f"  nodo {clave:2s} {n['tipo']:11s} punto {n['punto']:9s} {n['id']}")
        print(f"          etiqueta en el grafo: {n['etiqueta']!r}")
    for a in aristas:
        print(f"  arista kg['edges'][{a['indice']}]  {a['a']} --{a['relacion']}--> {a['b']}  "
              f"({a['clase']}; rótulo {a['rotulo']!r})")
    svg, alto_total = componer(nodos, aristas)
    with open(SALIDA_SVG, "w", encoding="utf-8") as fh:
        fh.write(svg)
    print(f"SVG: {SALIDA_SVG}   lienzo {W} x {alto_total:.0f}")
    print(f"Impresa a {ANCHO_FIGURA_CM:.2f} cm de ancho ({ANCHO_FIGURA_PT:.1f} pt), "
          f"alto {ANCHO_FIGURA_CM * alto_total / W:.2f} cm:")
    for nombre, fs in (("rótulos de elemento", FS_TITULO),
                       ("subtextos, salidas, nodos, leyenda", FS_SUB)):
        print(f"    {nombre:36s} {fs} -> {puntos_impresos(fs):5.2f} pt (mínimo {PT_MINIMO})")
    if exportar_png():
        print(f"PNG: {SALIDA_PNG}   {ANCHO_PNG_PX} px de ancho, {DPI} dpi")
    if "--verificar" in sys.argv[1:]:
        if not verificar(alto_total):
            raise SystemExit("FALLA: la verificación de medidas encontró defectos")


if __name__ == "__main__":
    main()
