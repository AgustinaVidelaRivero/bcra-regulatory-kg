#!/usr/bin/env python3
"""Figura del método de evaluación (capítulo 5, entrada), por script y nunca a mano.

Es un diagrama del método: no lee datos, registros ni resultados de la
evaluación. Qué dibuja, a 15 cm de ancho:
- a la izquierda, los datos: los documentos, el grafo evaluado y los
  fragmentos de los documentos;
- arriba, la banda de la evaluación intrínseca: la precisión (una muestra de
  tripletas del grafo y su juez) y la cobertura (una muestra de pasajes, la
  tripleta más importante de cada uno, su comprobación, su orden y el juez de
  presencia);
- abajo, la banda de la evaluación extrínseca: las preguntas, el agente con sus
  dos servidores, la respuesta, su juez, las reglas de las citas, la fidelidad,
  la atribución de las fallas y la comparación con los fragmentos.
Cada caja lleva, si la tiene, el número de la sección que la trata, en negrita
y arriba a la izquierda. Ninguna caja nombra un modelo ni lleva una cantidad.

Contenido: la tabla CAJAS (una línea por caja: clase, sección y texto) y la
tabla FLECHAS (una línea por flecha). Cambiar una etiqueta, una sección o la
clase de una caja es cambiar su línea en CAJAS; el texto se parte solo en
renglones al ancho de su caja (ANCHO_TEXTO).

Formato: el de la figura del proceso del capítulo 4
(generar_figura_proceso.py): biblioteca estándar y rsvg-convert, la paleta
por clase (naranja para lo que ejecuta un modelo de lenguaje, azul para el
código y las reglas fijas, gris para los datos y los resultados), la
tipografía, los cuerpos, las interlíneas, los márgenes internos, los grosores,
las esquinas, las puntas de flecha, la leyenda, el ancho y la resolución
(FORMATO, con la línea que declara cada valor). El texto va alineado a la
izquierda, como en la figura del extractor como función. Si
generar_figura_proceso.py está junto a este script (o se da con --formato),
cada valor se coteja con la línea que lo declara.

Controles (verificar(); si uno falla, no se escribe nada):
  1. contenido: las cajas dibujadas son las de CAJAS, cada una con su clase, y
     el texto dibujado de cada caja, unido, es el de CAJAS letra por letra;
     ningún texto nombra un modelo;
  2. trazado: las flechas son exactamente las de FLECHAS; ningún tramo es
     diagonal ni nulo ni va hacia la izquierda; cada caja de destino tiene el
     centro a la derecha del de su origen, salvo las de A_LA_IZQUIERDA; cada
     flecha sale del borde de su caja (o de un tramo de su flecha madre) y
     llega al borde de su caja de destino, lejos de las esquinas;
  3. cajas: ninguna se superpone con otra ni con la leyenda; cada caja está en
     su banda y los datos, fuera de las bandas; ningún trazo ni punta entra
     en una caja;
  4. cruces: entre flechas, solo los cruces de CRUCES (en ángulo recto); ningún
     contacto ni superposición; dos flechas no pasan a menos de DISTANCIA_MIN;
  5. textos: ninguno por debajo de 7 pt impresos, fuera de su caja, superpuesto
     a otro texto ni tocado por un trazo o una punta;
  6. margen y tamaño: nada a menos de 2 mm del borde; el alto no pasa de
     ALTO_MAX_CM;
  7. registro: el SVG se relee y cada caja, muestra y flecha tiene el color de
     su clase.

Salida: figura_evaluacion.png (1772 px de ancho, 300 dpi grabados en el PNG),
byte a byte reproducible con el mismo rsvg-convert.

Uso (desde la raíz del repositorio):
    PYTHONDONTWRITEBYTECODE=1 python3 -B docs/tesis/figuras/fig_evaluacion.py
Opciones: --salida <directorio> (por omisión, el del script), --svg <ruta>
(guarda también el SVG) y --formato <ruta de generar_figura_proceso.py>.
"""

from __future__ import annotations

import argparse
import hashlib
import math
import os
import re
import shutil
import struct
import subprocess
import sys
import xml.etree.ElementTree as ET
import zlib

sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
NOMBRE = "figura_evaluacion"

# ========================================================================== #
# Contenido: una línea por caja                                              #
# ========================================================================== #
# clave: (clase, sección, texto). Clases: «modelo» (naranja), «codigo» (azul),
# «datos» (gris) y «resultado» (gris, con el texto en negrita). La barra « / »
# separa la primera línea (negrita) de la segunda (normal, más chica).
CAJAS = {
    "documentos":          ("datos",     None,    "Los documentos"),
    "grafo":               ("datos",     None,    "El grafo evaluado"),
    "fragmentos":          ("datos",     None,    "Los fragmentos de los documentos"),
    "muestra_tripletas":   ("datos",     None,    "Muestra de tripletas del grafo"),
    "juez_tripletas":      ("modelo",    "5.2.1", "Juez de las tripletas / ¿Es correcta? ¿Cuánto importa?"),
    "res_precision":       ("resultado", "5.2.1", "Precisión e importancia"),
    "muestra_pasajes":     ("datos",     None,    "Muestra de pasajes"),
    "extrae":              ("modelo",    "5.2.2", "Extrae la tripleta más importante de cada pasaje"),
    "tramo":               ("codigo",    "5.2.2", "Comprueba que su tramo esté en el pasaje"),
    "ordena":              ("modelo",    "5.2.2", "Ordena las tripletas por importancia"),
    "juez_presencia":      ("modelo",    "5.2.2", "Juez de presencia / ¿Está la tripleta en el grafo?"),
    "res_cobertura":       ("resultado", "5.2.2", "Cobertura"),
    "redacta":             ("modelo",    "5.4",   "Redacta las preguntas"),
    "preguntas":           ("datos",     None,    "Preguntas con sus criterios"),
    "agente":              ("modelo",    "5.3",   "Agente / Consulta uno de los 2 servidores"),
    "servidor_grafo":      ("codigo",    "5.3",   "Servidor del grafo"),
    "servidor_fragmentos": ("codigo",    "5.3",   "Servidor de los fragmentos"),
    "respuesta":           ("datos",     None,    "Respuesta, citas y traza"),
    "juez_respuestas":     ("modelo",    "5.4",   "Juez de las respuestas / ¿Cumple cada criterio?"),
    "reglas_citas":        ("codigo",    "5.4",   "Reglas de las citas"),
    "res_fidelidad":       ("resultado", "5.5",   "Fidelidad"),
    "atribucion":          ("codigo",    "5.6",   "Atribución de las fallas"),
    "res_comparacion":     ("resultado", "5.7",   "Comparación con los fragmentos"),
}
# (origen, destino, punta en los dos extremos)
FLECHAS = (
    ("grafo", "muestra_tripletas", False),
    ("muestra_tripletas", "juez_tripletas", False),
    ("juez_tripletas", "res_precision", False),
    ("documentos", "muestra_pasajes", False),
    ("muestra_pasajes", "extrae", False),
    ("extrae", "tramo", False),
    ("tramo", "ordena", False),
    ("ordena", "juez_presencia", False),
    ("grafo", "juez_presencia", False),
    ("juez_presencia", "res_cobertura", False),
    ("documentos", "redacta", False),
    ("redacta", "preguntas", False),
    ("preguntas", "agente", False),
    ("grafo", "servidor_grafo", False),
    ("fragmentos", "servidor_fragmentos", False),
    ("servidor_grafo", "agente", True),
    ("servidor_fragmentos", "agente", True),
    ("agente", "respuesta", False),
    ("respuesta", "juez_respuestas", False),
    ("preguntas", "juez_respuestas", False),
    ("respuesta", "reglas_citas", False),
    ("juez_respuestas", "res_fidelidad", False),
    ("reglas_citas", "res_fidelidad", False),
    ("juez_respuestas", "atribucion", False),
    ("respuesta", "atribucion", False),
    ("juez_respuestas", "res_comparacion", False),
)
BANDAS = {
    "intrinseca": "Evaluación intrínseca, el contenido del grafo",
    "extrinseca": "Evaluación extrínseca, las respuestas del agente",
}
# Cruces entre flechas que la composición no puede evitar: los documentos y el
# grafo alimentan las dos bandas, así que la flecha del grafo a su servidor
# cruza las dos flechas que salen de los documentos.
CRUCES = {
    (("grafo", "servidor_grafo"), ("documentos", "muestra_pasajes")),
    (("grafo", "servidor_grafo"), ("documentos", "redacta")),
}
# Flechas cuya caja de destino tiene el centro a la izquierda del de su origen:
# la cadena de la cobertura no entra en una fila y sube, con una flecha
# vertical, de la fila de abajo a la de arriba.
A_LA_IZQUIERDA = {("ordena", "juez_presencia")}


class Falla(Exception):
    """Un control no se cumple: la figura no se escribe."""


def falla(control: str, motivo: str):
    raise Falla(f"[{control}] {motivo}")


# ========================================================================== #
# Formato (el de la figura del proceso)                                      #
# ========================================================================== #
# Valores de docs/tesis/figuras/generar_figura_proceso.py; al lado de cada uno,
# la línea que lo declara en ese script.
W = 760                                                  # :163
TIPOGRAFIA = "Helvetica,Arial,sans-serif"                # :164
MODELO = {"relleno": "#fbe3d3", "borde": "#e07b39"}      # :165
DETERMINISTICA = {"relleno": "#e1e7ee", "borde": "#4a5a6a"}  # :166
NEUTRO = {"relleno": "#fafafa", "borde": "#999999"}      # :167
TINTA, TINTA_SUB = "#1f1f1f", "#444444"                  # :168
FLECHA = "#555555"                                       # :169
FS_TITULO, FS_TEXTO = 14, 13                             # :171
IL = {FS_TITULO: 18, FS_TEXTO: 17}                       # :172
SEP_TITULO = 5                                           # :173
PAD_X, PAD_Y = 9, 11                                     # :174
GROSOR_CAJA = 1.6                                        # :175
GROSOR_FLUJO, GROSOR_RAMA = 1.8, 1.6                     # :176
RADIO = 9                                                # :177
RX = 8                                                   # :178
MARGEN = 12                                              # :180
LEYENDA_MARCO = 'fill="white" stroke="#e2e2e2" stroke-width="1" rx="5"'  # :181
MUESTRA_W, MUESTRA_H, FILA_LEY = 24, 16, 22              # :182
MARCADOR_A = 'viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '   # :183
MARCADOR_B = 'markerHeight="6" orient="auto"><path d="M0,0L10,5L0,10z"'  # :184
LEYENDA = (("modelo", "Pieza que ejecuta un modelo de lenguaje"),        # :278
           ("codigo", "Pieza de código"),                                # :279
           ("datos", "Datos"))                                           # :280
ANCHO_CM = 15.0                                          # :311
DPI = 300                                                # :313
PT_MINIMO = 7.0                                          # :315
MARGEN_MM = 2.0                                          # :316
DISTANCIA_MIN = 3.0                                      # :319
SEP_CAJAS = 8.0                                          # :320
HOLGURA_TEXTO = 1.5                                      # :318
HUECO_PUNTA = 2.0                                        # :324
ASC, DESC = 0.78, 0.22                                   # :350
GRUPO_LEYENDA = 10                                       # :420
RX_MUESTRA = 3                                           # :1123
LEJOS_ESQUINA = RX + 4                                   # :325
MARCADOR = MARCADOR_A + MARCADOR_B
# La punta del arranque de una flecha doble: el mismo marcador, con el
# triángulo dado vuelta y la referencia en el otro extremo.
MARCADOR_INICIO = MARCADOR_A.replace('refX="9"', 'refX="1"') + MARCADOR_B.replace(
    "M0,0L10,5L0,10z", "M10,0L0,5L10,10z")
PALETA = {"modelo": MODELO, "codigo": DETERMINISTICA, "datos": NEUTRO, "resultado": NEUTRO}
ESTILO_TRAZO = {"flujo": GROSOR_FLUJO, "rama": GROSOR_RAMA}
PT_POR_CM = 72.0 / 2.54
ANCHO_PNG_PX = round(ANCHO_CM / 2.54 * DPI)              # 1772
MARGEN_MIN = MARGEN_MM * W / (ANCHO_CM * 10)             # 10,1 unidades
ALTO_MAX_CM = 13.0

# nombre → (valor que usa la figura, línea citada, patrón de la línea en
# generar_figura_proceso.py, grupo que se compara con el valor)
FORMATO = {
    "W": (W, 163, r"^W = (\d+) ", int),
    "TIPOGRAFIA": (TIPOGRAFIA, 164, r'^TIPOGRAFIA = "([^"]+)"$', str),
    "MODELO": (MODELO, 165, r"^MODELO = (\{[^}]*\})$", "lit"),
    "DETERMINISTICA": (DETERMINISTICA, 166, r"^DETERMINISTICA = (\{[^}]*\})$", "lit"),
    "NEUTRO": (NEUTRO, 167, r"^NEUTRO = (\{[^}]*\})$", "lit"),
    "TINTA, TINTA_SUB": ((TINTA, TINTA_SUB), 168, r'^TINTA, TINTA_SUB = ("#[0-9a-f]{6}", "#[0-9a-f]{6}")$', "lit"),
    "FLECHA": (FLECHA, 169, r'^FLECHA, GRIS_ARISTA = "(#[0-9a-f]{6})", "#[0-9a-f]{6}"$', str),
    "FS_TITULO, FS_TEXTO": ((FS_TITULO, FS_TEXTO), 171, r"^FS_TITULO, FS_TEXTO = (\d+, \d+)$", "lit"),
    "IL": ((IL[FS_TITULO], IL[FS_TEXTO]), 172, r"^IL = \{FS_TITULO: (\d+), FS_TEXTO: (\d+)\}$", int),
    "SEP_TITULO": (SEP_TITULO, 173, r"^SEP_TITULO = (\d+)$", int),
    "PAD_X, PAD_Y": ((PAD_X, PAD_Y), 174, r"^PAD_X, PAD_Y = (\d+, \d+)$", "lit"),
    "GROSOR_CAJA": (GROSOR_CAJA, 175, r"^GROSOR_CAJA, GROSOR_DISCONTINUA = ([\d.]+), [\d.]+$", float),
    "GROSOR_FLUJO, GROSOR_RAMA": ((GROSOR_FLUJO, GROSOR_RAMA), 176,
                                  r"^GROSOR_FLUJO, GROSOR_RAMA = ([\d.]+, [\d.]+)$", "lit"),
    "RADIO": (RADIO, 177, r"^RADIO = (\d+) ", int),
    "RX": (RX, 178, r"^RX = (\d+) ", int),
    "MARGEN": (MARGEN, 180, r"^MARGEN = (\d+)$", int),
    "LEYENDA_MARCO": (LEYENDA_MARCO, 181, r"^LEYENDA_MARCO = '(.+)'$", str),
    "MUESTRA_W, MUESTRA_H, FILA_LEY": ((MUESTRA_W, MUESTRA_H, FILA_LEY), 182,
                                       r"^MUESTRA_W, MUESTRA_H, FILA_LEY = (\d+, \d+, \d+)$", "lit"),
    "MARCADOR_A": (MARCADOR_A, 183, r"^MARCADOR_A = '(.+)'$", str),
    "MARCADOR_B": (MARCADOR_B, 184, r"^MARCADOR_B = '(.+)'$", str),
    "LEYENDA modelo": (LEYENDA[0][1], 278, r'^LEYENDA = \(\("modelo", "([^"]+)"\),$', str),
    "LEYENDA codigo": (LEYENDA[1][1], 279, r'^\s+\("codigo", "([^"]+)"\),$', str),
    "LEYENDA datos": (LEYENDA[2][1], 280, r'^\s+\("datos", "([^"]+)"\)\)$', str),
    "ANCHO_CM": (ANCHO_CM, 311, r"^ANCHO_CM = ([\d.]+)$", float),
    "DPI": (DPI, 313, r"^DPI = (\d+)$", int),
    "PT_MINIMO": (PT_MINIMO, 315, r"^PT_MINIMO = ([\d.]+)$", float),
    "MARGEN_MM": (MARGEN_MM, 316, r"^MARGEN_MM = ([\d.]+)$", float),
    "HOLGURA_TEXTO": (HOLGURA_TEXTO, 318, r"^HOLGURA_TEXTO = ([\d.]+) ", float),
    "DISTANCIA_MIN": (DISTANCIA_MIN, 319, r"^DISTANCIA_MIN = ([\d.]+) ", float),
    "SEP_CAJAS": (SEP_CAJAS, 320, r"^SEP_CAJAS = ([\d.]+) ", float),
    "HUECO_PUNTA": (HUECO_PUNTA, 324, r"^HUECO_PUNTA = ([\d.]+) ", float),
    "LEJOS_ESQUINA": ("RX + 4", 325, r"^LEJOS_ESQUINA = (RX \+ 4) ", str),
    "ASC, DESC": ((ASC, DESC), 350, r"^ASC, DESC = ([\d.]+, [\d.]+) ", "lit"),
    "GRUPO_LEYENDA": (GRUPO_LEYENDA, 420, r"^GRUPO_LEYENDA = (\d+)$", int),
    "RX_MUESTRA": (RX_MUESTRA, 1123, r"""^\s+f'stroke-width="\{GROSOR_CAJA\}" rx="(\d+)"/>'\)$""", int),
}


def cotejar_formato(ruta: str) -> list[str]:
    """Cada valor de FORMATO contra la línea de generar_figura_proceso.py que lo
    declara. Falla si un valor no coincide; si la línea cambió de número, lo
    informa."""
    import ast
    with open(ruta, encoding="utf-8") as fh:
        lineas = fh.read().splitlines()
    out = []
    for nombre, (valor, citada, patron, conv) in FORMATO.items():
        hallados = [(i + 1, m) for i, l in enumerate(lineas) for m in [re.search(patron, l)] if m]
        if len(hallados) != 1:
            falla("formato", f"{nombre}: {len(hallados)} líneas con {patron!r} en {ruta}, se esperaba una")
        n, m = hallados[0]
        grupos = [ast.literal_eval(g) if conv == "lit" else conv(g) for g in m.groups()]
        leido = grupos[0] if len(grupos) == 1 else tuple(grupos)
        if leido != valor:
            falla("formato", f"{nombre}: la figura usa {valor!r} y {ruta}:{n} declara {leido!r}")
        nota = "" if n == citada else f" (citada :{citada})"
        out.append(f"{nombre}: {valor!r} ← :{n}{nota}")
    return out


# ========================================================================== #
# Métrica de texto: anchos AFM de Helvetica y Helvetica-Bold (/1000)         #
# ========================================================================== #
# Las tablas de generar_figura_proceso.py (:335-349), con «¿» y «?» agregados
# (Adobe Core 14: questiondown 611 y question 556 en Helvetica; 611 y 611 en
# Helvetica-Bold).
_CARS = " (),-.0123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz«»ÁÉÍÑÓÚáéíñóú"
_AFM = {
    False: dict(zip(_CARS, (
        278, 333, 333, 278, 333, 278, 556, 556, 556, 556, 556, 556, 556, 556, 556, 556, 278, 667,
        667, 722, 722, 667, 611, 778, 722, 278, 500, 667, 556, 833, 722, 778, 667, 778, 722, 667,
        611, 722, 667, 944, 667, 667, 611, 556, 556, 500, 556, 556, 278, 556, 556, 222, 222, 500,
        222, 833, 556, 556, 556, 556, 333, 500, 278, 556, 500, 722, 500, 500, 500, 556, 556, 667,
        667, 278, 722, 778, 722, 556, 556, 278, 556, 556, 556))),
    True: dict(zip(_CARS, (
        278, 333, 333, 278, 333, 278, 556, 556, 556, 556, 556, 556, 556, 556, 556, 556, 333, 722,
        722, 722, 722, 667, 611, 778, 722, 278, 556, 722, 611, 833, 722, 778, 667, 778, 722, 667,
        611, 722, 667, 944, 667, 667, 611, 556, 611, 556, 611, 556, 333, 611, 611, 278, 278, 556,
        278, 889, 611, 611, 611, 611, 389, 556, 333, 611, 556, 778, 556, 556, 500, 556, 556, 722,
        667, 278, 722, 778, 722, 556, 556, 278, 611, 611, 611))),
}
_AFM[False].update({"¿": 611, "?": 556})
_AFM[True].update({"¿": 611, "?": 611})


def ancho(s: str, fs: float, negrita: bool) -> float:
    tabla = _AFM[negrita]
    faltan = sorted({c for c in s if c not in tabla})
    if faltan:
        falla("textos", f"caracteres sin medida AFM en {s!r}: {faltan}")
    return sum(tabla[c] for c in s) * fs / 1000.0


def puntos_impresos(unidades: float) -> float:
    return unidades * ANCHO_CM * PT_POR_CM / W


def f(v: float) -> str:
    """Un decimal fijo (el de la figura del proceso, :567-570)."""
    return f"{v:.1f}"


# ========================================================================== #
# Texto de cada caja                                                          #
# ========================================================================== #
# Ancho del texto de cada caja (sin los márgenes internos). Medidas de esta
# figura: deciden en cuántos renglones se parte cada texto.
ANCHO_TEXTO = {
    "documentos": 84, "grafo": 84, "fragmentos": 84,
    "muestra_tripletas": 60, "juez_tripletas": 86, "res_precision": 97,
    "juez_presencia": 86, "res_cobertura": 101,
    "muestra_pasajes": 74, "extrae": 93, "tramo": 112, "ordena": 107,
    "redacta": 101, "preguntas": 98, "agente": 78,
    "servidor_grafo": 80, "servidor_fragmentos": 80, "respuesta": 81,
    "juez_respuestas": 120, "reglas_citas": 148, "res_fidelidad": 84,
    "atribucion": 94, "res_comparacion": 130,
}
FS_SECCION = FS_TEXTO                    # el número de sección, en negrita
SEP_SECCION = ancho(" ", FS_TITULO, True)  # del número al título


def partir(palabras: list[str], wmax: float, fs: int, negrita: bool, sangria: float = 0.0) -> list[str]:
    """Renglones de `palabras` en `wmax`; el primero empieza en `sangria`."""
    lineas, actual = [], ""
    for p in palabras:
        disponible = wmax - (sangria if not lineas else 0.0)
        cand = p if not actual else actual + " " + p
        if ancho(cand, fs, negrita) <= disponible:
            actual = cand
            continue
        if not actual or ancho(p, fs, negrita) > wmax:
            falla("textos", f"«{p}» no entra en {wmax} junto a lo que lo precede")
        lineas.append(actual)
        actual = p
    lineas.append(actual)
    return lineas


def lineas_caja(clave: str) -> list[dict]:
    """Renglones de la caja: cada uno con sus piezas (texto, cuerpo, negrita,
    color, desplazamiento, tipo) y su interlínea y separación previa."""
    _, seccion, texto = CAJAS[clave]
    titulo, _, segunda = texto.partition(" / ")
    wmax = ANCHO_TEXTO[clave]
    sangria = ancho(seccion, FS_SECCION, True) + SEP_SECCION if seccion else 0.0
    out = []
    for i, s in enumerate(partir(titulo.split(), wmax, FS_TITULO, True, sangria)):
        piezas = []
        dx = 0.0
        if i == 0 and seccion:
            piezas.append((seccion, FS_SECCION, True, TINTA, 0.0, "seccion"))
            dx = sangria
        piezas.append((s, FS_TITULO, True, TINTA, dx, "titulo"))
        out.append({"piezas": piezas, "il": IL[FS_TITULO], "sep": 0})
    if segunda:
        for i, s in enumerate(partir(segunda.split(), wmax, FS_TEXTO, False)):
            out.append({"piezas": [(s, FS_TEXTO, False, TINTA_SUB, 0.0, "texto")], "il": IL[FS_TEXTO],
                        "sep": SEP_TITULO if i == 0 else 0})
    return out


def alto_contenido(clave: str) -> float:
    return sum(l["sep"] + l["il"] for l in lineas_caja(clave))


def ancho_caja(clave: str) -> int:
    """El ancho de una caja de la figura del proceso (:383-384)."""
    return math.ceil(ANCHO_TEXTO[clave] + 2 * PAD_X + 2)


def alto_caja(clave: str) -> int:
    """El alto de una caja de la figura del proceso (:387-388)."""
    return math.ceil(alto_contenido(clave) + 2 * PAD_Y)


# ========================================================================== #
# Composición                                                                 #
# ========================================================================== #
# Medidas de esta figura (no salen de otra figura).
X_TRONCO = 128                   # vertical de la flecha del grafo a su servidor
X_BANDA = 138                    # borde izquierdo de las bandas
PAD_BANDA = 4                    # del borde de la banda a las cajas, a los costados
ALTO_ROTULO = 28                 # rótulo de la banda: 6 + interlínea 18 + 4
SEP_BANDAS = 8                   # entre las dos bandas
PIE_BANDA = 4                    # de las cajas al borde inferior de la banda
SEP_FLECHA = 20                  # entre dos cajas unidas por una flecha horizontal
SEP_DOBLE = 32                   # entre dos cajas unidas por una flecha doble
SEP_VERTICAL = 20                # entre dos cajas unidas por una flecha vertical
CARRIL = 10                      # de las cajas al carril del grafo, arriba y abajo
SEP_FILA_B = 22                  # de la respuesta a las reglas de las citas
SOBRE_LEYENDA = 10               # de la banda de abajo a la leyenda
FILA_U = ("muestra_tripletas", "juez_tripletas", "res_precision", "juez_presencia", "res_cobertura")
SEP_SIN_FLECHA = math.ceil(SEP_CAJAS + GROSOR_CAJA)  # entre dos cajas vecinas sin flecha
SEP_U = (SEP_FLECHA, SEP_FLECHA, SEP_SIN_FLECHA, SEP_FLECHA)
FILA_L = ("muestra_pasajes", "extrae", "tramo", "ordena")
BANDA_DE = {k: "intrinseca" for k in FILA_U + FILA_L}
BANDA_DE.update({k: "extrinseca" for k in (
    "redacta", "preguntas", "agente", "servidor_grafo", "servidor_fragmentos", "respuesta",
    "juez_respuestas", "reglas_citas", "res_fidelidad", "atribucion", "res_comparacion")})


def caja(clave: str, x: float, y: float) -> dict:
    return {"clave": clave, "x": float(x), "y": float(y), "w": float(ancho_caja(clave)),
            "h": float(alto_caja(clave)), "clase": CAJAS[clave][0]}


def der(c):
    return c["x"] + c["w"]


def aba(c):
    return c["y"] + c["h"]


def cx(c):
    return c["x"] + c["w"] / 2.0


def cy(c):
    return c["y"] + c["h"] / 2.0


def comun(a: dict, b: dict, eje: str) -> tuple[float, float]:
    """Tramo en común de dos cajas en x o en y, lejos de las esquinas."""
    if eje == "x":
        lo, hi = max(a["x"], b["x"]) + LEJOS_ESQUINA, min(der(a), der(b)) - LEJOS_ESQUINA
    else:
        lo, hi = max(a["y"], b["y"]) + LEJOS_ESQUINA, min(aba(a), aba(b)) - LEJOS_ESQUINA
    if lo > hi:
        falla("composicion", f"«{a['clave']}» y «{b['clave']}» no tienen tramo común en {eje}")
    return lo, hi


def armar() -> dict:
    """Ubica bandas, cajas, flechas y leyenda; nada se dibuja todavía."""
    C = {}
    x0 = X_BANDA + PAD_BANDA
    x1 = W - MARGEN - PAD_BANDA
    B = {}

    # ---- banda de arriba: dos filas ------------------------------------- #
    yb = float(MARGEN)
    tc = yb + ALTO_ROTULO
    h_u = max(alto_caja(k) for k in FILA_U)
    h_l = max(alto_caja(k) for k in FILA_L)
    cy_u = tc + h_u / 2.0
    y_carril = tc + h_u + CARRIL
    cy_l = y_carril + CARRIL + h_l / 2.0
    x = x0
    for k, sep in zip(FILA_U, SEP_U + (0,)):
        C[k] = caja(k, x, cy_u - alto_caja(k) / 2.0)
        x += ancho_caja(k) + sep
    x = x0
    for k in FILA_L:
        C[k] = caja(k, x, cy_l - alto_caja(k) / 2.0)
        x += ancho_caja(k) + SEP_FLECHA
    fin_a = tc + h_u + 2 * CARRIL + h_l + PIE_BANDA
    B["intrinseca"] = {"x": float(X_BANDA), "y": yb, "w": float(W - MARGEN - X_BANDA), "h": fin_a - yb}

    # ---- banda de abajo: tres niveles alrededor del agente -------------- #
    yb2 = fin_a + SEP_BANDAS
    tc2 = yb2 + ALTO_ROTULO
    h_j = alto_caja("juez_respuestas")
    a0 = tc2 + h_j + SEP_VERTICAL                       # borde superior del agente
    ag = C["agente"] = caja("agente", 0, a0)
    sg = caja("servidor_grafo", x0, 0)
    y_sg = a0 + LEJOS_ESQUINA + 4                       # la flecha doble del servidor del grafo
    sg["y"] = y_sg + LEJOS_ESQUINA + 4 - sg["h"]
    C["servidor_grafo"] = sg
    rd = C["redacta"] = caja("redacta", x0, sg["y"] - SEP_SIN_FLECHA - alto_caja("redacta"))
    pr = C["preguntas"] = caja("preguntas", der(rd) + SEP_FLECHA, rd["y"])
    ag["x"] = max(der(sg) + SEP_DOBLE, cx(pr) - ag["w"] / 2.0)   # el agente, debajo de las preguntas
    sf =C["servidor_fragmentos"] = caja("servidor_fragmentos", x0, aba(sg) + SEP_SIN_FLECHA)
    y_sf = sf["y"] + 2 * LEJOS_ESQUINA                  # la flecha doble del servidor de los fragmentos
    rs = C["respuesta"] = caja("respuesta", der(ag) + SEP_FLECHA, a0)
    at = C["atribucion"] = caja("atribucion", der(rs) + SEP_FLECHA, a0)
    jr = C["juez_respuestas"] = caja("juez_respuestas", der(pr) + SEP_FLECHA, tc2)
    y_jf = aba(jr) - LEJOS_ESQUINA                      # la salida del juez a la fidelidad
    co = C["res_comparacion"] = caja("res_comparacion", der(jr) + SEP_FLECHA, 0)
    co["y"] = y_jf - LEJOS_ESQUINA - co["h"]
    rg = C["reglas_citas"] = caja("reglas_citas", rs["x"], aba(rs) + SEP_FILA_B)
    fi = C["res_fidelidad"] = caja("res_fidelidad", der(rg) + SEP_FLECHA, rg["y"])
    fin_b = max(aba(c) for c in C.values() if BANDA_DE.get(c["clave"]) == "extrinseca") + PIE_BANDA
    B["extrinseca"] = {"x": float(X_BANDA), "y": yb2, "w": float(W - MARGEN - X_BANDA), "h": fin_b - yb2}

    # ---- datos, a la izquierda ------------------------------------------ #
    for k, centro in (("grafo", cy_u), ("documentos", cy_l), ("fragmentos", cy(sf))):
        c = C[k] = caja(k, MARGEN, 0)
        c["y"] = centro - c["h"] / 2.0
    gr, do, fr = C["grafo"], C["documentos"], C["fragmentos"]

    # ---- flechas -------------------------------------------------------- #
    hp = HUECO_PUNTA
    T = []

    def flecha(desde, hasta, puntos, estilo="flujo", madre=None, doble=False):
        T.append({"desde": desde, "hasta": hasta, "nombre": f"{desde} → {hasta}", "estilo": estilo,
                  "madre": madre, "doble": doble, "puntos": [(float(f(px)), float(f(py))) for px, py in puntos]})

    def horizontal(a, b, y=None, estilo="flujo"):
        A, Bx = C[a], C[b]
        lo, hi = comun(A, Bx, "y")
        y = (lo + hi) / 2.0 if y is None else y
        if not lo <= y <= hi:
            falla("composicion", f"«{a} → {b}» en y={y:.1f} fuera de su tramo común")
        flecha(a, b, [(der(A), y), (Bx["x"] - hp, y)], estilo)

    def vertical(a, b, x):
        A, Bx = C[a], C[b]
        lo, hi = comun(A, Bx, "x")
        if not lo <= x <= hi:
            falla("composicion", f"«{a} → {b}» en x={x:.1f} fuera de su tramo común")
        if Bx["y"] > A["y"]:
            flecha(a, b, [(x, aba(A)), (x, Bx["y"] - hp)])
        else:
            flecha(a, b, [(x, A["y"]), (x, aba(Bx) + hp)])

    mt, jt, rp, jp, rc = (C[k] for k in FILA_U)
    mp, ex, tr, od = (C[k] for k in FILA_L)
    # banda de arriba
    horizontal("grafo", "muestra_tripletas", cy_u, "rama")
    horizontal("muestra_tripletas", "juez_tripletas", cy_u)
    horizontal("juez_tripletas", "res_precision", cy_u)
    horizontal("documentos", "muestra_pasajes", cy_l, "rama")
    horizontal("muestra_pasajes", "extrae", cy_l)
    horizontal("extrae", "tramo", cy_l)
    horizontal("tramo", "ordena", cy_l)
    lo, hi = comun(od, jp, "x")
    x_oj = hi - 6
    vertical("ordena", "juez_presencia", x_oj)
    x_gj = jp["x"] + LEJOS_ESQUINA + 2
    y_g2 = aba(gr) - LEJOS_ESQUINA
    y_s = cy(sg)
    flecha("grafo", "servidor_grafo", [(der(gr), y_g2), (X_TRONCO, y_g2), (X_TRONCO, y_s), (sg["x"] - hp, y_s)],
           "rama")
    flecha("grafo", "juez_presencia", [(X_TRONCO, y_carril), (x_gj, y_carril), (x_gj, aba(jp) + hp)], "rama",
           madre="grafo → servidor_grafo")
    horizontal("juez_presencia", "res_cobertura", cy_u)
    # banda de abajo
    flecha("documentos", "redacta", [(cx(do), aba(do)), (cx(do), cy(rd)), (rd["x"] - hp, cy(rd))], "rama")
    horizontal("redacta", "preguntas", cy(rd))
    lo, hi = comun(pr, ag, "x")
    vertical("preguntas", "agente", (lo + hi) / 2.0)
    horizontal("fragmentos", "servidor_fragmentos", cy(sf), "rama")
    flecha("servidor_grafo", "agente", [(der(sg) + hp, y_sg), (ag["x"] - hp, y_sg)], doble=True)
    flecha("servidor_fragmentos", "agente", [(der(sf) + hp, y_sf), (ag["x"] - hp, y_sf)], doble=True)
    horizontal("agente", "respuesta", cy(rs))
    lo, hi = comun(rs, jr, "x")
    vertical("respuesta", "juez_respuestas", lo + 4)
    horizontal("preguntas", "juez_respuestas", cy(pr))
    lo, hi = comun(rs, rg, "x")
    vertical("respuesta", "reglas_citas", hi - 4)
    x_jf = der(at) + 3 * LEJOS_ESQUINA
    flecha("juez_respuestas", "res_fidelidad", [(der(jr), y_jf), (x_jf, y_jf), (x_jf, fi["y"] - hp)])
    horizontal("reglas_citas", "res_fidelidad", cy(fi))
    lo, hi = comun(jr, at, "x")
    vertical("juez_respuestas", "atribucion", (lo + hi) / 2.0)
    horizontal("respuesta", "atribucion", cy(rs))
    horizontal("juez_respuestas", "res_comparacion", cy(co))

    # ---- leyenda, abajo a la izquierda (la de la figura del proceso) ---- #
    y_ley = max(fin_b, aba(fr)) + SOBRE_LEYENDA
    w_ley = 12 + MUESTRA_W + 9 + max(ancho(s, FS_TEXTO, False) for _, s in LEYENDA) + 12
    h_ley = GRUPO_LEYENDA + len(LEYENDA) * FILA_LEY + 6
    L = {"x": float(MARGEN), "y": float(f(y_ley)), "w": float(f(w_ley)), "h": float(h_ley)}
    alto = math.ceil(L["y"] + L["h"] + MARGEN)
    return {"cajas": C, "bandas": B, "trazos": T, "leyenda": L, "alto": alto,
            "geo": {"x0": x0, "x1": x1, "a0": a0, "y_carril": y_carril}}


# ========================================================================== #
# Elementos derivados: textos, puntas, tramos                                #
# ========================================================================== #
def bb(c: dict) -> tuple:
    return (c["x"], c["y"], c["x"] + c["w"], c["y"] + c["h"])


def textos_de(M: dict) -> list[dict]:
    """Todo texto dibujado, con su caja (o su banda, o la leyenda) y su posición."""
    out = []
    for clave, c in M["cajas"].items():
        yy = c["y"] + (c["h"] - alto_contenido(clave)) / 2.0
        for i, l in enumerate(lineas_caja(clave)):
            yy += l["sep"]
            fs_l = max(p[1] for p in l["piezas"])
            base = yy + (l["il"] - fs_l) / 2.0 + ASC * fs_l
            for s, fs, negrita, color, dx, tipo in l["piezas"]:
                out.append({"s": s, "fs": fs, "negrita": negrita, "color": color,
                            "x": float(f(c["x"] + PAD_X + dx)), "y": float(f(base)),
                            "dentro": clave, "tipo": tipo, "linea": i})
            yy += l["il"]
    for k, b in M["bandas"].items():
        base = b["y"] + 6 + (IL[FS_TITULO] - FS_TITULO) / 2.0 + ASC * FS_TITULO
        out.append({"s": BANDAS[k], "fs": FS_TITULO, "negrita": True, "color": TINTA,
                    "x": float(f(M["geo"]["x0"])), "y": float(f(base)), "dentro": f"banda {k}",
                    "tipo": "rotulo", "linea": 0})
    L = M["leyenda"]
    for k, (_, s) in enumerate(LEYENDA):
        yc = L["y"] + GRUPO_LEYENDA + k * FILA_LEY + FILA_LEY / 2.0
        out.append({"s": s, "fs": FS_TEXTO, "negrita": False, "color": TINTA,
                    "x": float(f(L["x"] + 12 + MUESTRA_W + 9)), "y": float(f(yc + 0.28 * FS_TEXTO)),
                    "dentro": "leyenda", "tipo": "leyenda", "linea": k})
    return out


def muestras_leyenda(M: dict) -> list[dict]:
    L = M["leyenda"]
    out = []
    for k, (clase, _) in enumerate(LEYENDA):
        yc = L["y"] + GRUPO_LEYENDA + k * FILA_LEY + FILA_LEY / 2.0
        out.append({"clave": f"leyenda_{clase}", "clase": clase, "x": float(f(L["x"] + 12)),
                    "y": float(f(yc - MUESTRA_H / 2.0)), "w": float(MUESTRA_W), "h": float(MUESTRA_H)})
    return out


def caja_texto(t: dict) -> tuple:
    a = ancho(t["s"], t["fs"], t["negrita"])
    return (t["x"], t["y"] - ASC * t["fs"], t["x"] + a, t["y"] + DESC * t["fs"])


def tramos(t: dict) -> list[tuple]:
    return list(zip(t["puntos"], t["puntos"][1:]))


def puntas(t: dict) -> list[tuple]:
    """Triángulos de las puntas (marcador de 10 × 10 a 6 veces el grosor): la del
    final y, en una flecha doble, la del arranque."""
    g = ESTILO_TRAZO[t["estilo"]]
    lp = 6 * g
    out = []
    pares = [(t["puntos"][-2], t["puntos"][-1])]
    if t["doble"]:
        pares.append((t["puntos"][1], t["puntos"][0]))
    for (xa, ya), (xb, yb) in pares:
        largo = math.hypot(xb - xa, yb - ya)
        ux, uy = (xb - xa) / largo, (yb - ya) / largo
        tip = (xb + 0.1 * lp * ux, yb + 0.1 * lp * uy)
        bx, by = xb - 0.9 * lp * ux, yb - 0.9 * lp * uy
        out.append((tip, (bx - 0.5 * lp * uy, by + 0.5 * lp * ux), (bx + 0.5 * lp * uy, by - 0.5 * lp * ux)))
    return out


def caja_punta(p: tuple) -> tuple:
    return (min(q[0] for q in p), min(q[1] for q in p), max(q[0] for q in p), max(q[1] for q in p))


# ========================================================================== #
# Geometría de los controles (la de la figura del proceso)                   #
# ========================================================================== #
def cruza(a, b) -> bool:
    return a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]


def ampliar(b, d) -> tuple:
    return (b[0] - d, b[1] - d, b[2] + d, b[3] + d)


def contiene(c, b, holgura=0.0) -> bool:
    return (c[0] + holgura <= b[0] and b[2] <= c[2] - holgura
            and c[1] + holgura <= b[1] and b[3] <= c[3] - holgura)


def corta(p, q, r) -> bool:
    """True si el segmento pq pasa por el interior abierto del rectángulo r."""
    dx, dy = q[0] - p[0], q[1] - p[1]
    t0, t1 = 0.0, 1.0
    for pp, qq in ((-dx, p[0] - r[0]), (dx, r[2] - p[0]), (-dy, p[1] - r[1]), (dy, r[3] - p[1])):
        if pp == 0:
            if qq <= 0:
                return False
            continue
        t = qq / pp
        if pp < 0:
            t0 = max(t0, t)
        else:
            t1 = min(t1, t)
        if t0 >= t1:
            return False
    return True


def dist_punto_segmento(p, a, b) -> float:
    dx, dy = b[0] - a[0], b[1] - a[1]
    l2 = dx * dx + dy * dy
    t = 0.0 if l2 == 0 else max(0.0, min(1.0, ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / l2))
    return math.hypot(p[0] - a[0] - t * dx, p[1] - a[1] - t * dy)


def dist_punto_caja(p, r) -> float:
    return math.hypot(max(r[0] - p[0], 0.0, p[0] - r[2]), max(r[1] - p[1], 0.0, p[1] - r[3]))


def dist_segmento_caja(p, q, r) -> float:
    if corta(p, q, r) or contiene(r, (p[0], p[1], p[0], p[1])):
        return 0.0
    esquinas = ((r[0], r[1]), (r[2], r[1]), (r[0], r[3]), (r[2], r[3]))
    return min([dist_punto_caja(p, r), dist_punto_caja(q, r)] + [dist_punto_segmento(e, p, q) for e in esquinas])


def sobre(p, a, b, tol=1e-6) -> bool:
    return (min(a[0], b[0]) - tol <= p[0] <= max(a[0], b[0]) + tol
            and min(a[1], b[1]) - tol <= p[1] <= max(a[1], b[1]) + tol
            and abs((b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])) <= tol)


def contacto(a0, a1, b0, b1):
    """Contacto entre dos tramos ortogonales: («x», punto) si se cruzan,
    («toque», punto) si uno toca al otro con un extremo, («superpuestos», punto)
    si van uno sobre otro; None si no se tocan."""
    ha, hb = a0[1] == a1[1], b0[1] == b1[1]
    if ha != hb:
        (h0, h1), (v0, v1) = ((a0, a1), (b0, b1)) if ha else ((b0, b1), (a0, a1))
        p = (v0[0], h0[1])
        if not (sobre(p, h0, h1) and sobre(p, v0, v1)):
            return None
        return ("toque" if p in (h0, h1, v0, v1) else "x", p)
    eje = 1 if ha else 0
    if a0[eje] != b0[eje]:
        return None
    o = 1 - eje
    lo = max(min(a0[o], a1[o]), min(b0[o], b1[o]))
    hi = min(max(a0[o], a1[o]), max(b0[o], b1[o]))
    if lo > hi:
        return None
    return ("superpuestos", (lo, a0[1]) if ha else (a0[0], lo))


def dist_segmentos(a0, a1, b0, b1) -> float:
    if contacto(a0, a1, b0, b1) is not None:
        return 0.0
    return min(dist_punto_segmento(a0, b0, b1), dist_punto_segmento(a1, b0, b1),
               dist_punto_segmento(b0, a0, a1), dist_punto_segmento(b1, a0, a1))


def en_borde(p, c) -> str | None:
    """Lado del borde de la caja c sobre el que está p, lejos de las esquinas."""
    x0, y0, x1, y1 = bb(c)
    if abs(p[1] - y0) < 1e-6 and x0 + LEJOS_ESQUINA <= p[0] <= x1 - LEJOS_ESQUINA:
        return "arriba"
    if abs(p[1] - y1) < 1e-6 and x0 + LEJOS_ESQUINA <= p[0] <= x1 - LEJOS_ESQUINA:
        return "abajo"
    if abs(p[0] - x0) < 1e-6 and y0 + LEJOS_ESQUINA <= p[1] <= y1 - LEJOS_ESQUINA:
        return "izquierda"
    if abs(p[0] - x1) < 1e-6 and y0 + LEJOS_ESQUINA <= p[1] <= y1 - LEJOS_ESQUINA:
        return "derecha"
    return None


NORMAL = {"arriba": (0, -1), "abajo": (0, 1), "izquierda": (-1, 0), "derecha": (1, 0)}


def direccion(a, b) -> tuple:
    return ((b[0] > a[0]) - (b[0] < a[0]), (b[1] > a[1]) - (b[1] < a[1]))


def llega(t, q0, q1, caja_destino) -> bool:
    """El tramo q0 → q1 termina a HUECO_PUNTA del borde de la caja, hacia adentro."""
    dx, dy = direccion(q0, q1)
    p = (q1[0] + HUECO_PUNTA * dx, q1[1] + HUECO_PUNTA * dy)
    lado = en_borde(p, caja_destino)
    return lado is not None and (dx, dy) == tuple(-v for v in NORMAL[lado])


# ========================================================================== #
# Controles                                                                   #
# ========================================================================== #
MODELOS = re.compile(r"haiku|sonnet|opus|claude|anthropic|gpt|gemini|llama|mistral|qwen", re.I)


def controlar_contenido(M: dict) -> dict:
    if sorted(M["cajas"]) != sorted(CAJAS):
        falla("contenido", f"cajas dibujadas {sorted(M['cajas'])} ≠ las de CAJAS")
    for clave, c in M["cajas"].items():
        if c["clase"] != CAJAS[clave][0] or c["clase"] not in PALETA:
            falla("contenido", f"«{clave}» es «{c['clase']}» y en CAJAS es «{CAJAS[clave][0]}»")
    textos = textos_de(M)
    por_caja = {}
    for t in textos:
        if MODELOS.search(t["s"]):
            falla("contenido", f"«{t['s']}» nombra un modelo")
        por_caja.setdefault(t["dentro"], []).append(t)
    for clave, (_, seccion, texto) in CAJAS.items():
        ts = por_caja.pop(clave, [])
        sec = [t["s"] for t in ts if t["tipo"] == "seccion"]
        tit = " ".join(t["s"] for t in ts if t["tipo"] == "titulo")
        seg = " ".join(t["s"] for t in ts if t["tipo"] == "texto")
        dibujado = tit + (" / " + seg if seg else "")
        if sec != ([seccion] if seccion else []) or dibujado != texto:
            falla("contenido", f"«{clave}»: dibujado {sec} «{dibujado}» ≠ CAJAS {seccion} «{texto}»")
        if seccion and not any(t["tipo"] == "seccion" and t["linea"] == 0 and
                               t["x"] == float(f(M["cajas"][clave]["x"] + PAD_X)) for t in ts):
            falla("contenido", f"«{clave}»: el número de sección no está arriba a la izquierda")
    for k, s in BANDAS.items():
        if [t["s"] for t in por_caja.pop(f"banda {k}", [])] != [s]:
            falla("contenido", f"el rótulo de la banda «{k}» no es «{s}»")
    if [t["s"] for t in por_caja.pop("leyenda", [])] != [s for _, s in LEYENDA]:
        falla("contenido", "la leyenda no es la de la figura del proceso")
    if por_caja:
        falla("contenido", f"textos sin caja: {sorted(por_caja)}")
    return {"textos": len(textos), "cajas": len(M["cajas"])}


def controlar_trazado(M: dict) -> dict:
    T, C = M["trazos"], M["cajas"]
    por_nombre = {t["nombre"]: t for t in T}
    n_tramos = 0
    for t in T:
        for p, q in tramos(t):
            n_tramos += 1
            if p == q:
                falla("trazado", f"tramo nulo en «{t['nombre']}» en {p}")
            if p[0] != q[0] and p[1] != q[1]:
                falla("trazado", f"tramo diagonal en «{t['nombre']}»: {p} → {q}")
        for (a, b), (c, d) in zip(tramos(t), tramos(t)[1:]):
            if direccion(a, b) == tuple(-v for v in direccion(c, d)):
                falla("trazado", f"«{t['nombre']}» vuelve sobre sí misma en {b}")
        p0, p1 = t["puntos"][0], t["puntos"][1]
        if t["madre"]:
            m = por_nombre.get(t["madre"])
            if m is None or m["desde"] != t["desde"]:
                falla("trazado", f"«{t['nombre']}» arranca de una flecha que no sale de su caja")
            if not any(sobre(p0, a, b) and p0 not in (a, b) for a, b in tramos(m)):
                falla("trazado", f"«{t['nombre']}» no arranca sobre un tramo de «{t['madre']}»")
        elif t["doble"]:
            if not llega(t, p1, p0, C[t["desde"]]):
                falla("trazado", f"«{t['nombre']}» no arranca a {HUECO_PUNTA} del borde de «{t['desde']}»")
        else:
            lado = en_borde(p0, C[t["desde"]])
            if lado is None or direccion(p0, p1) != NORMAL[lado]:
                falla("trazado", f"«{t['nombre']}» no sale del borde de «{t['desde']}» hacia afuera ({p0})")
        if not llega(t, t["puntos"][-2], t["puntos"][-1], C[t["hasta"]]):
            falla("trazado", f"«{t['nombre']}» no llega al borde de «{t['hasta']}» ({t['puntos'][-1]})")
    izquierda = set()
    for t in T:
        if any(q[0] < p[0] for p, q in tramos(t)):
            falla("trazado", f"«{t['nombre']}» tiene un tramo hacia la izquierda")
        if cx(C[t["hasta"]]) < cx(C[t["desde"]]):
            izquierda.add((t["desde"], t["hasta"]))
    if izquierda != A_LA_IZQUIERDA:
        falla("trazado", f"destinos a la izquierda de su origen {sorted(izquierda)} ≠ {sorted(A_LA_IZQUIERDA)}")
    dibujadas = sorted((t["desde"], t["hasta"], t["doble"]) for t in T)
    if dibujadas != sorted(FLECHAS):
        sobran = [c for c in dibujadas if c not in FLECHAS]
        faltan = [c for c in FLECHAS if c not in dibujadas]
        falla("trazado", f"flechas distintas de FLECHAS: sobran {sobran}; faltan {faltan}")
    return {"flechas": len(T), "tramos": n_tramos, "dobles": sum(t["doble"] for t in T)}


def controlar_cajas(M: dict) -> dict:
    C, BD = M["cajas"], M["bandas"]
    L = M["leyenda"]
    todas = [(k, bb(c), GROSOR_CAJA) for k, c in C.items()]
    todas.append(("leyenda", (L["x"], L["y"], L["x"] + L["w"], L["y"] + L["h"]), 1.0))
    minimo = math.inf
    for i in range(len(todas)):
        for j in range(i + 1, len(todas)):
            (ka, a, ga), (kb, b, gb) = todas[i], todas[j]
            dx = max(b[0] - a[2], 0.0, a[0] - b[2])
            dy = max(b[1] - a[3], 0.0, a[1] - b[3])
            d = math.hypot(dx, dy) - (ga + gb) / 2.0
            minimo = min(minimo, d)
            if cruza(a, b) or d < SEP_CAJAS:
                falla("cajas", f"«{ka}» se superpone con «{kb}» o queda a {d:.1f} (< {SEP_CAJAS})")
    bandas = {k: (b["x"], b["y"], b["x"] + b["w"], b["y"] + b["h"]) for k, b in BD.items()}
    if cruza(*bandas.values()):
        falla("cajas", "las dos bandas se superponen")
    for k, c in C.items():
        banda = BANDA_DE.get(k)
        r = ampliar(bb(c), GROSOR_CAJA / 2.0)
        for kb, rb in bandas.items():
            if kb == banda and not contiene(rb, r, 1.0):
                falla("cajas", f"«{k}» no está dentro de su banda «{kb}»")
            if kb != banda and cruza(r, rb):
                falla("cajas", f"«{k}» entra en la banda «{kb}»")
    if any(cruza(todas[-1][1], rb) for rb in bandas.values()):
        falla("cajas", "la leyenda entra en una banda")
    for t in M["trazos"]:
        for k, r, _ in todas:
            interior = ampliar(r, -1.0)
            if any(corta(p, q, interior) for p, q in tramos(t)):
                falla("cajas", f"la flecha «{t['nombre']}» atraviesa la caja «{k}»")
            if any(cruza(caja_punta(p), ampliar(r, -0.5)) for p in puntas(t)):
                falla("cajas", f"una punta de «{t['nombre']}» entra en la caja «{k}»")
    return {"cajas": len(todas), "separacion_minima": minimo}


def controlar_cruces(M: dict) -> dict:
    T = M["trazos"]
    cruces, contactos, minimo = set(), [], (math.inf, "", "")
    for i in range(len(T)):
        for j in range(i + 1, len(T)):
            a, b = T[i], T[j]
            familia = a["madre"] == b["nombre"] or b["madre"] == a["nombre"]
            arranque = (b["puntos"][0] if b["madre"] == a["nombre"]
                        else a["puntos"][0] if a["madre"] == b["nombre"] else None)
            hay = False
            for p, q in tramos(a):
                for u, v in tramos(b):
                    c = contacto(p, q, u, v)
                    if c is None or (familia and c[1] == arranque):
                        continue
                    hay = True
                    if c[0] == "x":
                        cruces.add(tuple(sorted(((a["desde"], a["hasta"]), (b["desde"], b["hasta"])))))
                    else:
                        contactos.append((a["nombre"], b["nombre"], c))
            if not familia and not hay:
                d = min(dist_segmentos(p, q, u, v) for p, q in tramos(a) for u, v in tramos(b))
                d -= (ESTILO_TRAZO[a["estilo"]] + ESTILO_TRAZO[b["estilo"]]) / 2.0
                if d < minimo[0]:
                    minimo = (d, a["nombre"], b["nombre"])
    esperados = {tuple(sorted(c)) for c in CRUCES}
    if contactos:
        falla("cruces", f"contactos entre flechas: {contactos}")
    if cruces != esperados:
        falla("cruces", f"cruces {sorted(cruces)} ≠ los de CRUCES {sorted(esperados)}")
    if minimo[0] < DISTANCIA_MIN:
        falla("cruces", f"«{minimo[1]}» pasa a {minimo[0]:.1f} de «{minimo[2]}» (< {DISTANCIA_MIN})")
    for t in T:
        for o in T:
            if o is t or o["nombre"] == t["madre"] or t["nombre"] == o["madre"]:
                continue
            for pt in puntas(t):
                for p, q in tramos(o):
                    d = dist_segmento_caja(p, q, caja_punta(pt)) - ESTILO_TRAZO[o["estilo"]] / 2.0
                    if d < HOLGURA_TEXTO:
                        falla("cruces", f"una punta de «{t['nombre']}» toca la flecha «{o['nombre']}»")
    return {"cruces": sorted(cruces), "distancia_minima": minimo}


def controlar_textos(M: dict) -> dict:
    C = M["cajas"]
    textos = [(t, caja_texto(t)) for t in textos_de(M)]
    L = M["leyenda"]
    contenedores = {k: (bb(c), GROSOR_CAJA) for k, c in C.items()}
    contenedores["leyenda"] = ((L["x"], L["y"], L["x"] + L["w"], L["y"] + L["h"]), 1.0)
    for k, b in M["bandas"].items():
        contenedores[f"banda {k}"] = ((b["x"], b["y"], b["x"] + b["w"], b["y"] + b["h"]), 1.0)
    muestras = [(m["clave"], (m["x"], m["y"], m["x"] + m["w"], m["y"] + m["h"])) for m in muestras_leyenda(M)]
    minimos = {"texto-texto": math.inf, "texto-trazo": math.inf, "texto-borde de su caja": math.inf}
    tamanos = {}
    for t, r in textos:
        pt = puntos_impresos(t["fs"])
        tamanos[t["fs"]] = pt
        if pt < PT_MINIMO:
            falla("textos", f"«{t['s']}»: letra de {pt:.2f} pt (< {PT_MINIMO})")
        if r[0] < 0 or r[1] < 0 or r[2] > W or r[3] > M["alto"]:
            falla("textos", f"«{t['s']}» sale del lienzo")
        c, g = contenedores[t["dentro"]]
        holg = min(r[0] - c[0], c[2] - r[2], r[1] - c[1], c[3] - r[3])
        if not t["dentro"].startswith("banda"):
            minimos["texto-borde de su caja"] = min(minimos["texto-borde de su caja"], holg)
        if holg < g / 2.0 + HOLGURA_TEXTO:
            falla("textos", f"«{t['s']}» a {holg:.1f} del borde de «{t['dentro']}»")
        for k, (c2, g2) in contenedores.items():
            if k != t["dentro"] and not k.startswith("banda") and cruza(r, ampliar(c2, g2 / 2.0)):
                falla("textos", f"«{t['s']}» se superpone con la caja «{k}»")
        for k, m in muestras:
            if cruza(ampliar(r, HOLGURA_TEXTO), m):
                falla("textos", f"«{t['s']}» toca la muestra «{k}» de la leyenda")
        for tr in M["trazos"]:
            g3 = ESTILO_TRAZO[tr["estilo"]] / 2.0
            d = min(dist_segmento_caja(p, q, r) for p, q in tramos(tr)) - g3
            minimos["texto-trazo"] = min(minimos["texto-trazo"], d)
            if d < HOLGURA_TEXTO:
                falla("textos", f"«{t['s']}» toca la flecha «{tr['nombre']}»")
            if any(cruza(ampliar(r, HOLGURA_TEXTO), caja_punta(p)) for p in puntas(tr)):
                falla("textos", f"«{t['s']}» toca una punta de «{tr['nombre']}»")
    for i in range(len(textos)):
        for j in range(i + 1, len(textos)):
            (ta, a), (tb, b) = textos[i], textos[j]
            if cruza(a, b):
                falla("textos", f"«{ta['s']}» se superpone con «{tb['s']}»")
            dx = max(b[0] - a[2], 0.0, a[0] - b[2])
            dy = max(b[1] - a[3], 0.0, a[1] - b[3])
            minimos["texto-texto"] = min(minimos["texto-texto"], math.hypot(dx, dy))
    return {"textos": len(textos), "tamanos": tamanos, "minimos": minimos, "cajas_texto": textos}


def controlar_margen(M: dict, textos) -> dict:
    todas = [(f"texto «{t['s']}»", r) for t, r in textos]
    todas += [(f"caja «{k}»", ampliar(bb(c), GROSOR_CAJA / 2.0)) for k, c in M["cajas"].items()]
    for k, b in M["bandas"].items():
        todas.append((f"banda «{k}»", ampliar((b["x"], b["y"], b["x"] + b["w"], b["y"] + b["h"]), 0.5)))
    L = M["leyenda"]
    todas.append(("leyenda", ampliar((L["x"], L["y"], L["x"] + L["w"], L["y"] + L["h"]), 0.5)))
    for t in M["trazos"]:
        g = ESTILO_TRAZO[t["estilo"]] / 2.0
        xs, ys = [p[0] for p in t["puntos"]], [p[1] for p in t["puntos"]]
        todas.append((f"flecha «{t['nombre']}»", (min(xs) - g, min(ys) - g, max(xs) + g, max(ys) + g)))
        todas += [(f"punta de «{t['nombre']}»", caja_punta(p)) for p in puntas(t)]
    distancia = {"izquierdo": lambda r: r[0], "superior": lambda r: r[1],
                 "derecho": lambda r: W - r[2], "inferior": lambda r: M["alto"] - r[3]}
    minimos = {}
    for borde, d in distancia.items():
        minimos[borde] = min(d(r) for _, r in todas)
        for nombre, r in todas:
            if d(r) < MARGEN_MIN:
                falla("margen", f"{nombre} a {d(r):.1f} unidades del borde {borde} (< {MARGEN_MIN:.1f})")
    alto_cm = ANCHO_CM * M["alto"] / W
    if alto_cm > ALTO_MAX_CM:
        falla("margen", f"la figura mide {alto_cm:.2f} cm de alto (> {ALTO_MAX_CM})")
    return {"elementos": len(todas), "minimos": minimos, "alto_cm": alto_cm}


def verificar(M: dict) -> dict:
    rep = {"contenido": controlar_contenido(M), "trazado": controlar_trazado(M),
           "cajas": controlar_cajas(M), "cruces": controlar_cruces(M)}
    rep["textos"] = controlar_textos(M)
    rep["margen"] = controlar_margen(M, rep["textos"]["cajas_texto"])
    rep["svg"] = dibujar(M)
    rep["registro"] = controlar_registro(rep["svg"], M)
    return rep


# ========================================================================== #
# Emisión del SVG                                                            #
# ========================================================================== #
def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def path_redondeado(puntos) -> str:
    """Poligonal con esquinas redondeadas de radio RADIO (la de la figura del
    proceso, :1060-1073)."""
    d = f"M{f(puntos[0][0])},{f(puntos[0][1])}"
    for i in range(1, len(puntos) - 1):
        (x0, y0), (x1, y1), (x2, y2) = puntos[i - 1], puntos[i], puntos[i + 1]

        def hacia(xa, ya, xb, yb):
            largo = math.hypot(xb - xa, yb - ya)
            r = min(RADIO, largo / 2.0)
            return xa + (xb - xa) * r / largo, ya + (yb - ya) * r / largo
        ex, ey = hacia(x1, y1, x0, y0)
        sx, sy = hacia(x1, y1, x2, y2)
        d += f" L{f(ex)},{f(ey)} Q{f(x1)},{f(y1)} {f(sx)},{f(sy)}"
    return d + f" L{f(puntos[-1][0])},{f(puntos[-1][1])}"


def dibujar(M: dict) -> str:
    alto = M["alto"]
    alto_cm = ANCHO_CM * alto / W
    partes = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{ANCHO_CM:.2f}cm" height="{alto_cm:.2f}cm" '
        f'viewBox="0 0 {W} {alto}" font-family="{TIPOGRAFIA}">',
        f'<rect width="{W}" height="{alto}" fill="white"/>',
        f'<defs><marker id="arN" {MARCADOR} fill="{FLECHA}"/></marker>'
        f'<marker id="arNi" {MARCADOR_INICIO} fill="{FLECHA}"/></marker></defs>',
    ]
    for k, b in M["bandas"].items():
        partes.append(f'<rect data-banda="{k}" x="{f(b["x"])}" y="{f(b["y"])}" width="{f(b["w"])}" '
                      f'height="{f(b["h"])}" {LEYENDA_MARCO}/>')
    for clave, c in M["cajas"].items():
        pal = PALETA[c["clase"]]
        partes.append(f'<rect data-caja="{clave}" x="{f(c["x"])}" y="{f(c["y"])}" width="{f(c["w"])}" '
                      f'height="{f(c["h"])}" fill="{pal["relleno"]}" stroke="{pal["borde"]}" '
                      f'stroke-width="{GROSOR_CAJA}" rx="{RX}"/>')
    for t in M["trazos"]:
        inicio = ' marker-start="url(#arNi)"' if t["doble"] else ""
        partes.append(f'<path data-flecha="{esc(t["nombre"])}" d="{path_redondeado(t["puntos"])}" fill="none" '
                      f'stroke="{FLECHA}" stroke-width="{ESTILO_TRAZO[t["estilo"]]}"{inicio} '
                      f'marker-end="url(#arN)"/>')
    L = M["leyenda"]
    partes.append(f'<rect x="{f(L["x"])}" y="{f(L["y"])}" width="{f(L["w"])}" height="{f(L["h"])}" '
                  f'{LEYENDA_MARCO}/>')
    for m in muestras_leyenda(M):
        pal = PALETA[m["clase"]]
        partes.append(f'<rect data-caja="{m["clave"]}" x="{f(m["x"])}" y="{f(m["y"])}" width="{f(m["w"])}" '
                      f'height="{f(m["h"])}" fill="{pal["relleno"]}" stroke="{pal["borde"]}" '
                      f'stroke-width="{GROSOR_CAJA}" rx="{RX_MUESTRA}"/>')
    for t in textos_de(M):
        peso = "bold" if t["negrita"] else "normal"
        partes.append(f'<text x="{f(t["x"])}" y="{f(t["y"])}" font-size="{t["fs"]}" font-weight="{peso}" '
                      f'fill="{t["color"]}">{esc(t["s"])}</text>')
    return "\n".join(partes + ["</svg>"]) + "\n"


def controlar_registro(svg: str, M: dict) -> dict:
    """El SVG se relee: cada caja, muestra de la leyenda y flecha tiene el color
    y el trazo de su clase o su estilo."""
    raiz = ET.fromstring(svg)
    clase_de = {k: c["clase"] for k, c in M["cajas"].items()}
    clase_de.update({f"leyenda_{c}": c for c, _ in LEYENDA})
    por_nombre = {t["nombre"]: t for t in M["trazos"]}
    n = {"cajas": 0, "muestras": 0, "flechas": 0, "textos": 0}
    for el in raiz.iter():
        clave = el.get("data-caja")
        if clave is not None:
            pal = PALETA[clase_de[clave]]
            if (el.get("fill"), el.get("stroke")) != (pal["relleno"], pal["borde"]):
                falla("registro", f"«{clave}» con relleno {el.get('fill')} y borde {el.get('stroke')}")
            n["muestras" if clave.startswith("leyenda_") else "cajas"] += 1
        nombre = el.get("data-flecha")
        if nombre is not None:
            t = por_nombre[nombre]
            esperado = (FLECHA, str(ESTILO_TRAZO[t["estilo"]]), "url(#arN)",
                        "url(#arNi)" if t["doble"] else None)
            if (el.get("stroke"), el.get("stroke-width"), el.get("marker-end"), el.get("marker-start")) != esperado:
                falla("registro", f"la flecha «{nombre}» no tiene el trazo de su estilo")
            n["flechas"] += 1
        if el.tag.endswith("text"):
            n["textos"] += 1
    if n["cajas"] != len(M["cajas"]) or n["muestras"] != len(LEYENDA) or n["flechas"] != len(M["trazos"]):
        falla("registro", f"elementos sin color controlado: {n}")
    return n


# ========================================================================== #
# Exportación                                                                #
# ========================================================================== #
def con_densidad(png: bytes, dpi: int) -> bytes:
    """El PNG con el bloque pHYs (píxeles por metro) después de IHDR (el de la
    figura del proceso, :1190-1211)."""
    firma, resto = png[:8], png[8:]
    salida, i = firma, 0
    ppm = round(dpi / 0.0254)
    cuerpo = b"pHYs" + struct.pack(">IIB", ppm, ppm, 1)
    phys = struct.pack(">I", 9) + cuerpo + struct.pack(">I", zlib.crc32(cuerpo) & 0xFFFFFFFF)
    while i < len(resto):
        largo = struct.unpack(">I", resto[i:i + 4])[0]
        tipo, bloque = resto[i + 4:i + 8], resto[i:i + 12 + largo]
        i += 12 + largo
        if tipo == b"pHYs":
            continue
        salida += bloque
        if tipo == b"IHDR":
            salida += phys
    return salida


def exportar(svg: str) -> bytes:
    rsvg = shutil.which("rsvg-convert")
    if not rsvg:
        falla("exportacion", "rsvg-convert no está instalado: no se escribe el PNG")
    r = subprocess.run([rsvg, "-w", str(ANCHO_PNG_PX), "-f", "png"], input=svg.encode("utf-8"),
                       capture_output=True)
    if r.returncode != 0:
        falla("exportacion", r.stderr.decode("utf-8", "replace"))
    return con_densidad(r.stdout, DPI)


# ========================================================================== #
# Principal                                                                   #
# ========================================================================== #
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--salida", default=AQUI, help="directorio del PNG (por omisión, el del script)")
    ap.add_argument("--svg", default=None, help="si se da, guarda también el SVG en esa ruta")
    ap.add_argument("--formato", default=None,
                    help="generar_figura_proceso.py con el que se coteja el formato "
                         "(por omisión, el que está junto a este script, si está)")
    args = ap.parse_args()
    ruta_formato = args.formato or os.path.join(AQUI, "generar_figura_proceso.py")
    try:
        cotejo = cotejar_formato(ruta_formato) if os.path.exists(ruta_formato) else None
        M = armar()
        rep = verificar(M)
        png = exportar(rep["svg"])
    except Falla as e:
        print(f"ALTO {e}")
        print("No se escribe nada.")
        return 1

    if cotejo is None:
        print("FORMATO: no cotejado (no está generar_figura_proceso.py junto al script ni se dio --formato)")
    else:
        print(f"FORMATO cotejado con {ruta_formato} (nombre: valor ← línea):")
        for linea in cotejo:
            print(f"  {linea}")
    c = rep["contenido"]
    print(f"CONTENIDO: {c['cajas']} cajas, las de CAJAS, con su clase y su texto letra por letra; "
          f"{c['textos']} textos en total; ninguno nombra un modelo")
    t = rep["trazado"]
    print(f"TRAZADO: {t['flechas']} flechas ({t['dobles']} con punta en los dos extremos), {t['tramos']} tramos, "
          f"0 diagonales; extremos en el borde de su caja; flechas = las de FLECHAS")
    k = rep["cajas"]
    print(f"CAJAS: {k['cajas']} (con la leyenda), sin superposiciones; separación mínima entre bordes "
          f"{k['separacion_minima']:.1f}; cada caja en su banda; ningún trazo ni punta entra en una caja")
    x = rep["cruces"]
    d = x["distancia_minima"]
    print(f"CRUCES entre flechas: {len(x['cruces'])}, los de CRUCES; contactos: 0; distancia mínima entre "
          f"flechas que no se cruzan {d[0]:.1f} («{d[1]}» / «{d[2]}»), exigida {DISTANCIA_MIN}")
    for a, b in x["cruces"]:
        print(f"  «{a[0]} → {a[1]}» × «{b[0]} → {b[1]}»")
    tx = rep["textos"]
    print(f"TEXTOS: {tx['textos']}, sin superposiciones; distancias mínimas: "
          + "; ".join(f"{a} {b:.1f}" for a, b in tx["minimos"].items()))
    for fs in sorted(tx["tamanos"]):
        print(f"  letra {fs} unidades -> {tx['tamanos'][fs]:.2f} pt impresos a {ANCHO_CM:.0f} cm")
    mg = rep["margen"]
    mm = ANCHO_CM * 10 / W
    print(f"MARGEN ({mg['elementos']} elementos): mínimo a cada borde "
          + ", ".join(f"{b} {v:.1f} u = {v * mm:.2f} mm" for b, v in mg["minimos"].items())
          + f"; exigido {MARGEN_MM:.1f} mm")
    rg = rep["registro"]
    print(f"REGISTRO: colores controlados en {rg['cajas']} cajas, {rg['muestras']} muestras y "
          f"{rg['flechas']} flechas; {rg['textos']} textos en el SVG")

    os.makedirs(args.salida, exist_ok=True)
    ruta_png = os.path.join(args.salida, f"{NOMBRE}.png")
    with open(ruta_png, "wb") as fh:
        fh.write(png)
    if args.svg:
        with open(args.svg, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(rep["svg"])
    wpx, hpx = struct.unpack(">II", png[16:24])
    print(f"TAMAÑO: lienzo {W} × {M['alto']}; impreso {ANCHO_CM:.2f} × {mg['alto_cm']:.2f} cm; "
          f"PNG {wpx} × {hpx} px a {DPI} dpi")
    print(f"PNG: {os.path.relpath(ruta_png)}  sha256 {hashlib.sha256(png).hexdigest()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
