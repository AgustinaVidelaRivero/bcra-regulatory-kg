#!/usr/bin/env python3
"""Figura del proceso de construcción del grafo (capítulo 4, introducción), POR SCRIPT y nunca a mano.

Qué dibuja, en dos filas a 15 cm de ancho:
- arriba, de izquierda a derecha: el Texto Ordenado (PDF), la Segmentación y
  las unidades de extracción, con un conector que baja al Extractor;
- abajo, de izquierda a derecha: el Extractor, el Validador, el Verificador,
  el Ensamblado y el grafo;
- entre las dos filas, como datos que entran: el esquema final, que entra al
  Extractor y al Validador, y el catálogo de sujetos, que entra al Extractor,
  al Validador y al Ensamblado;
- el ciclo del Verificador: una flecha de vuelta al Extractor, rotulada
  «re-extracción, 1 vez», y una flecha a la revisión humana, rotulada «si no
  se resuelve» (lo que pasa después con la revisión humana no se dibuja);
- como datos registrados que salen: los elementos rechazados, del Validador,
  y los sujetos sin asignar, en cuarentena, del Ensamblado.
El Validador es un solo bloque. La figura no lleva identificadores internos,
nombres de archivo, nombres de modelos ni cifras (salvo el «1» del rótulo de
la re-extracción, que se coteja con el código).

Estilo: el de la figura de la comparación de estrategias
(generar_figura_experimento_estrategias.py) y su paleta, que viene de
generar_figura_proceso_extraccion.py: naranja para las piezas que ejecuta un
modelo de lenguaje, gris azulado («azul») para las que son código, gris neutro
para los datos, y la caja blanca de borde discontinuo de la revisión contra
los Textos Ordenados para la revisión humana, con su flecha gris discontinua.
Misma tipografía, cuerpos, interlíneas, márgenes internos, grosores, esquinas,
puntas de flecha y marco de la leyenda. El generador no importa esos módulos:
los lee como texto, con candado de sha256, y coteja cada valor que usa con la
línea que lo declara (ESTILO); si una fuente cambia, frena antes de dibujar.

Fuentes (FUENTES):
  - generar_figura_proceso_extraccion.py, con candado de sha256: la paleta
    (MODELO, DETERMINISTICA, NEUTRO, TINTA, TINTA_SUB, FLECHA, GRIS_ARISTA);
  - generar_figura_norma_a_grafo.py, con candado de sha256: la tipografía;
  - generar_figura_experimento_estrategias.py, con candado de sha256: lienzo,
    cuerpos, interlíneas, márgenes, grosores, esquinas, caja discontinua,
    puntas y leyenda;
  - data/experiment/reextraccion_v2/e3_verificador/ratchet_e3.py: el tope de
    re-extracciones del verificador (TOPE_REINTENTOS), que da el «1» del
    rótulo. Es código en desarrollo: el candado no es el sha del archivo sino
    la línea del tope, que tiene que ser una sola y valer 1.
Los anchos de texto salen de las métricas AFM de Helvetica y Helvetica-Bold
(Adobe Core 14), copiadas abajo; todo con la biblioteca estándar.

Controles (verificar(); el primero que falla FRENA y no se escribe nada):
  1. contenido: los textos dibujados son exactamente los fijados (TEXTO,
     ROTULOS, LEYENDA); ninguno lleva identificadores internos, nombres de
     archivo, nombres de modelos ni cifras, salvo el «1» del rótulo, que es
     el tope del código; cada caja tiene la clase (modelo, código, datos,
     revisión humana) que le corresponde (CLASE);
  2. trazado: ningún tramo diagonal ni nulo; cada flecha sale del borde de su
     caja (o de un tramo de su flecha madre) y llega al borde de su caja de
     destino, lejos de las esquinas redondeadas; las flechas dibujadas son
     exactamente las de CONEXIONES, con su estilo y su rótulo;
  3. cajas: ninguna caja se superpone con otra; ningún trazo ni punta entra en
     una caja;
  4. cruces: entre dos flechas cualesquiera no hay ningún cruce ni contacto
     (solo el arranque de una rama sobre su flecha madre); dos flechas no
     pasan a menos de DISTANCIA_MIN; ninguna punta toca otra flecha;
  5. textos: ninguno por debajo de 7 pt impresos, fuera del lienzo o de su
     caja, superpuesto a otra caja, a otro texto o a una marca, ni tocado por
     un trazo o una punta;
  6. rótulos: cada uno junto a un tramo recto de su flecha (a JUNTO o menos),
     dentro de su largo y lejos de cualquier otra flecha;
  7. margen: nada a menos de 2 mm del borde del lienzo;
  8. registro y colores: el SVG emitido se relee; cada elemento está
     registrado, en orden, y cada caja y flecha tiene el color de su clase.
Pruebas negativas (MUTACIONES; corren en cada ejecución, antes de escribir):
un rótulo sobre una caja, un tramo diagonal y un cruce entre dos flechas;
cada una tiene que frenar en el control que le corresponde.

Salidas, byte-reproducibles: figura_proceso.svg, .png (300 dpi, densidad
grabada) y .pdf (rsvg-convert con SOURCE_DATE_EPOCH=0).

Uso (desde la raíz del repo):
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_proceso.py
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_proceso.py --salida <dir>
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_proceso.py --mutacion cruce_entre_flechas
"""

from __future__ import annotations

import argparse
import ast
import copy
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
RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", ".."))
NOMBRE = "figura_proceso"


class Freno(Exception):
    """Falla de un control: la figura no se escribe."""


def freno(control: str, motivo: str):
    raise Freno(f"[{control}] {motivo}")


# ========================================================================== #
# Fuentes y candados                                                         #
# ========================================================================== #
FIG = "docs/tesis/figuras"
# Las tres figuras hermanas llevan candado de sha256 del archivo entero. El
# código del verificador no: es código en desarrollo y la figura solo toma de
# él el tope de re-extracciones, así que el candado es la línea que lo declara
# (una sola, con el valor que dibuja el rótulo; ver controlar_contenido).
FUENTES = {
    "paleta": (f"{FIG}/generar_figura_proceso_extraccion.py",
               "6a91931abeb9927842f76fa50471497e926c69fc56617c62ef7f05ddf6c010d6"),
    "tipografia": (f"{FIG}/generar_figura_norma_a_grafo.py",
                   "9b0e45a299a0a078d250ccc999d192cbb83038bd8c00baa6bd8972d021b73f3d"),
    "hermana": (f"{FIG}/generar_figura_experimento_estrategias.py",
                "d68e1d87ba09bdb8faa7904400d042a7674cbd6ae5b8deb11dbfcf8163aa9755"),
    "verificador": ("data/experiment/reextraccion_v2/e3_verificador/ratchet_e3.py", None),
}
LEIDOS = {}      # clave -> sha256 del archivo leído


def sha256(ruta: str) -> str:
    with open(ruta, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def leer(clave: str) -> str:
    rel, esperado = FUENTES[clave]
    with open(os.path.join(RAIZ, rel), "rb") as fh:
        crudo = fh.read()
    sha = hashlib.sha256(crudo).hexdigest()
    if esperado is not None and sha != esperado:
        freno("fuentes", f"{rel} no es el verificado: sha256 {sha[:12]}… ≠ {esperado[:12]}…")
    LEIDOS[clave] = sha
    return crudo.decode("utf-8")


def lineas_con(texto: str, patron: str, clave: str, varias: bool = False) -> list[tuple[int, tuple]]:
    """(número de línea, grupos) de las líneas que cumplen `patron`: una sola,
    o con `varias`, al menos una y todas con los mismos grupos."""
    hallados = [(i + 1, m.groups()) for i, l in enumerate(texto.splitlines())
                for m in [re.search(patron, l)] if m]
    if not hallados or (not varias and len(hallados) != 1):
        freno("fuentes", f"{FUENTES[clave][0]}: {len(hallados)} líneas con {patron!r}, se esperaba una")
    if len({g for _, g in hallados}) != 1:
        freno("fuentes", f"{FUENTES[clave][0]}: las líneas con {patron!r} declaran valores distintos")
    return hallados


# ========================================================================== #
# Estilo (el de la figura de la comparación de estrategias)                  #
# ========================================================================== #
W = 760                                  # unidades de lienzo para 15 cm
TIPOGRAFIA = "Helvetica,Arial,sans-serif"
MODELO = {"relleno": "#fbe3d3", "borde": "#e07b39"}
DETERMINISTICA = {"relleno": "#e1e7ee", "borde": "#4a5a6a"}
NEUTRO = {"relleno": "#fafafa", "borde": "#999999"}
TINTA, TINTA_SUB = "#1f1f1f", "#444444"
FLECHA, GRIS_ARISTA = "#555555", "#8a8a8a"
DISCONTINUA = {"relleno": "white", "borde": GRIS_ARISTA}
FS_TITULO, FS_TEXTO = 14, 13
IL = {FS_TITULO: 18, FS_TEXTO: 17}
SEP_TITULO = 5
PAD_X, PAD_Y = 9, 11
GROSOR_CAJA, GROSOR_DISCONTINUA = 1.6, 1.3
GROSOR_FLUJO, GROSOR_RAMA = 1.8, 1.6
RADIO = 9                                # esquinas de los trazos
RX = 8                                   # esquinas de las cajas
GUIONES = "5,4"
MARGEN = 12
LEYENDA_MARCO = 'fill="white" stroke="#e2e2e2" stroke-width="1" rx="5"'
MUESTRA_W, MUESTRA_H, FILA_LEY = 24, 16, 22
MARCADOR_A = 'viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
MARCADOR_B = 'markerHeight="6" orient="auto"><path d="M0,0L10,5L0,10z"'
MARCADOR = MARCADOR_A + MARCADOR_B

# nombre → (fuente, patrón de la línea que lo declara, conversión, valor que la
# figura usa, varias). «lit» lee el grupo como literal de Python; «txt», como
# texto. Con varias=True el patrón puede estar en más de una línea, siempre con
# el mismo valor.
ESTILO = {
    "MODELO": ("paleta", r'^MODELO = (\{[^}]*\})', "lit", MODELO, False),
    "DETERMINISTICA": ("paleta", r'^DETERMINISTICA = (\{[^}]*\})', "lit", DETERMINISTICA, False),
    "NEUTRO": ("paleta", r'^NEUTRO = (\{[^}]*\})', "lit", NEUTRO, False),
    "TINTA": ("paleta", r'^TINTA = ("#[0-9a-f]{6}")$', "lit", TINTA, False),
    "TINTA_SUB": ("paleta", r'^TINTA_SUB = ("#[0-9a-f]{6}")$', "lit", TINTA_SUB, False),
    "FLECHA": ("paleta", r'^FLECHA = ("#[0-9a-f]{6}")$', "lit", FLECHA, False),
    "GRIS_ARISTA": ("paleta", r'^GRIS_ARISTA = ("#[0-9a-f]{6}")$', "lit", GRIS_ARISTA, False),
    "TIPOGRAFIA": ("tipografia", r'^TIPOGRAFIA = ("[^"]+")$', "lit", TIPOGRAFIA, False),
    "W": ("hermana", r'^W = (\d+) ', "lit", W, False),
    "DISCONTINUA": ("hermana", r'^DISCONTINUA = \{"relleno": ("\w+"), "borde": proc\.GRIS_ARISTA\}',
                    "lit", DISCONTINUA["relleno"], False),
    "FS_TITULO": ("hermana", r'^FS_TITULO = (\d+) ', "lit", FS_TITULO, False),
    "FS_TEXTO": ("hermana", r'^FS_TEXTO = (\d+) ', "lit", FS_TEXTO, False),
    "IL": ("hermana", r'^IL = \{FS_TITULO: (\d+), FS_TEXTO: (\d+)\}$', "lit",
           (IL[FS_TITULO], IL[FS_TEXTO]), False),
    "SEP_TITULO": ("hermana", r'^SEP_TITULO = (\d+) ', "lit", SEP_TITULO, False),
    "PAD": ("hermana", r'^PAD_X, PAD_Y = (\d+), (\d+)$', "lit", (PAD_X, PAD_Y), False),
    "GROSOR_CAJA": ("hermana", r'^GROSOR_CAJA = ([\d.]+)$', "lit", GROSOR_CAJA, False),
    "GROSOR_FLUJO": ("hermana", r'^GROSOR_FLUJO = ([\d.]+) ', "lit", GROSOR_FLUJO, False),
    "GROSOR_RAMA": ("hermana", r'^GROSOR_RAMA = ([\d.]+) ', "lit", GROSOR_RAMA, False),
    "RADIO": ("hermana", r'^RADIO = (\d+) ', "lit", RADIO, False),
    "RX": ("hermana", r'^def caja\(partes, clave, x, y, w, h, clase, grosor=GROSOR_CAJA, rx=(\d+), '
                      r'guiones=False\):$', "lit", RX, False),
    "GUIONES": ("hermana", r"^    dash = ' stroke-dasharray=\"(\d+,\d+)\"' if guiones else \"\"$",
                "txt", GUIONES, True),
    "GROSOR_DISCONTINUA": ("hermana", r'DISCONTINUA, grosor=([\d.]+), guiones=True\)$', "lit",
                           GROSOR_DISCONTINUA, False),
    "MARGEN": ("hermana", r'^MARGEN = (\d+) ', "lit", MARGEN, False),
    "LEYENDA_MARCO": ("hermana", r"(fill=\"white\" stroke=\"#e2e2e2\" stroke-width=\"1\" rx=\"5\")/>'\)$",
                      "txt", LEYENDA_MARCO, False),
    "LEYENDA_MUESTRA": ("hermana", r'^    muestra_w, muestra_h, fila_ley = (\d+), (\d+), (\d+)$', "lit",
                        (MUESTRA_W, MUESTRA_H, FILA_LEY), False),
    "MARCADOR_A": ("hermana", r"^        '<marker id=\"arN\" (" + re.escape(MARCADOR_A) + r")'$", "txt",
                   MARCADOR_A, False),
    "MARCADOR_B": ("hermana", r"^        f'(" + re.escape(MARCADOR_B) + r") fill=\"\{FLECHA\}\"/></marker>'$",
                   "txt", MARCADOR_B, False),
}


def leer_fuentes() -> dict:
    """Lee las fuentes con candado; coteja el estilo y devuelve el tope."""
    textos = {c: leer(c) for c in FUENTES}
    D = {"lineas": {}}
    for nombre, (clave, patron, conv, usado, varias) in ESTILO.items():
        hallados = lineas_con(textos[clave], patron, clave, varias)
        grupos = hallados[0][1]
        vals = [ast.literal_eval(g) if conv == "lit" else g for g in grupos]
        leido = vals[0] if len(vals) == 1 else tuple(vals)
        lugar = FUENTES[clave][0] + ":" + ",".join(str(n) for n, _ in hallados)
        if leido != usado:
            freno("estilo", f"{nombre}: la figura usa {usado!r} y {lugar} declara {leido!r}")
        D["lineas"][nombre] = lugar
    hallados = lineas_con(textos["verificador"], r'^TOPE_REINTENTOS = (\d+)$', "verificador")
    D["tope"] = int(hallados[0][1][0])
    D["lineas"]["TOPE_REINTENTOS"] = f"{FUENTES['verificador'][0]}:{hallados[0][0]}"
    return D


# ========================================================================== #
# Lo que la figura afirma                                                    #
# ========================================================================== #
# Contenido de cada caja: (texto, estilo); «titulo» va en negrita.
TEXTO = {
    "texto_ordenado": (("Texto Ordenado", "titulo"), ("(PDF)", "texto")),
    "segmentacion": (("Segmentación", "titulo"),),
    "unidades": (("Unidades de extracción", "titulo"),),
    "extractor": (("Extractor", "titulo"),),
    "validador": (("Validador", "titulo"),),
    "verificador": (("Verificador", "titulo"),),
    "ensamblado": (("Ensamblado", "titulo"),),
    "grafo": (("Grafo", "titulo"),),
    "esquema": (("Esquema final", "titulo"),),
    "catalogo": (("Catálogo de sujetos", "titulo"),),
    "rechazados": (("Elementos rechazados", "titulo"),),
    "cuarentena": (("Sujetos sin asignar,", "titulo"), ("en cuarentena", "titulo")),
    "revision": (("Revisión", "titulo"), ("humana", "titulo")),
}
# Qué es cada caja: pieza que ejecuta un modelo de lenguaje, pieza de código,
# datos o la revisión humana (que no es ninguna de las tres).
CLASE = {
    "texto_ordenado": "datos", "segmentacion": "codigo", "unidades": "datos",
    "extractor": "modelo", "validador": "codigo", "verificador": "modelo",
    "ensamblado": "codigo", "grafo": "datos", "esquema": "datos", "catalogo": "datos",
    "rechazados": "datos", "cuarentena": "datos", "revision": "humana",
}
PALETA = {"modelo": MODELO, "codigo": DETERMINISTICA, "datos": NEUTRO, "humana": DISCONTINUA}
LEYENDA = (("modelo", "Pieza que ejecuta un modelo de lenguaje"),
           ("codigo", "Pieza de código"),
           ("datos", "Datos"))
ROTULO_REEXTRACCION = "re-extracción, {n} vez"
ROTULO_NO_RESUELVE = "si no se resuelve"
LINEA_PRINCIPAL = ("texto_ordenado", "segmentacion", "unidades", "extractor", "validador",
                   "verificador", "ensamblado", "grafo")
# Las flechas: (desde, hasta, estilo, rótulo). «flujo» es la línea principal;
# «rama», las entradas, salidas y la vuelta al extractor; «humana», la flecha
# discontinua hacia la revisión humana.
CONEXIONES = (
    tuple((a, b, "flujo", None) for a, b in zip(LINEA_PRINCIPAL, LINEA_PRINCIPAL[1:]))
    + (("esquema", "extractor", "rama", None), ("esquema", "validador", "rama", None),
       ("catalogo", "extractor", "rama", None), ("catalogo", "validador", "rama", None),
       ("catalogo", "ensamblado", "rama", None),
       ("verificador", "extractor", "rama", "reextraccion"),
       ("verificador", "revision", "humana", "no_resuelve"),
       ("validador", "rechazados", "rama", None),
       ("ensamblado", "cuarentena", "rama", None))
)
ESTILO_TRAZO = {"flujo": (FLECHA, GROSOR_FLUJO, False, "arN"),
                "rama": (FLECHA, GROSOR_RAMA, False, "arN"),
                "humana": (GRIS_ARISTA, GROSOR_RAMA, True, "arG")}
# Nada de esto puede aparecer en un texto dibujado.
PROHIBIDOS = (re.compile(r"\bE[0-9]\b"), re.compile(r"\br[0-9]"), re.compile(r"\bv[0-9]"),
              re.compile(r"perfil", re.I), re.compile(r"_"), re.compile(r"::"), re.compile(r"[/\\]"),
              re.compile(r"\.(jsonl?|py|md|db|pdf|txt)\b", re.I),
              re.compile(r"haiku|sonnet|opus|claude|anthropic|gpt", re.I),
              re.compile(r"\b[0-9a-f]{7,40}\b"))

# ========================================================================== #
# Tamaño impreso y holguras                                                  #
# ========================================================================== #
ANCHO_CM = 15.0
PT_POR_CM = 72.0 / 2.54
DPI = 300
ANCHO_PNG_PX = round(ANCHO_CM / 2.54 * DPI)        # 1772
PT_MINIMO = 7.0
MARGEN_MM = 2.0
MARGEN_MIN = MARGEN_MM * W / (ANCHO_CM * 10)       # 10,1 unidades
HOLGURA_TEXTO = 1.5      # de un texto a un trazo, una marca o el borde de su caja
DISTANCIA_MIN = 3.0      # entre dos flechas
SEP_CAJAS = 8.0          # entre los bordes de dos cajas
JUNTO = 8.0              # de un rótulo a su tramo, como máximo
AJENA = 5.0              # un rótulo, al menos tanto más lejos de otra flecha que de la suya
ROTULO_AIRE = 4.0        # del trazo al rótulo
HUECO_PUNTA = 2.0        # del final del trazo al borde de la caja de destino
LEJOS_ESQUINA = RX + 4   # un extremo de flecha, de las esquinas redondeadas de su caja


def puntos_impresos(unidades: float) -> float:
    return unidades * ANCHO_CM * PT_POR_CM / W


# ========================================================================== #
# Métrica de texto: anchos AFM de Helvetica y Helvetica-Bold (/1000)         #
# ========================================================================== #
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
ASC, DESC = 0.78, 0.22      # alto sobre y bajo la línea de base, en em (los de la hermana)


def ancho(s: str, fs: float, negrita: bool) -> float:
    tabla = _AFM[negrita]
    falta = sorted({c for c in s if c not in tabla})
    if falta:
        freno("textos", f"caracteres sin medida AFM en {s!r}: {falta}")
    return sum(tabla[c] for c in s) * fs / 1000.0


def fs_de(estilo: str) -> int:
    return FS_TITULO if estilo == "titulo" else FS_TEXTO


def lineas_caja(clave: str) -> list[tuple]:
    """(texto, fs, negrita, color, separación previa) de cada línea de la caja."""
    out, previo = [], None
    for s, estilo in TEXTO[clave]:
        sep = SEP_TITULO if (previo == "titulo" and estilo == "texto") else 0
        out.append((s, fs_de(estilo), estilo == "titulo", TINTA if estilo == "titulo" else TINTA_SUB, sep))
        previo = estilo
    return out


def alto_contenido(clave: str) -> float:
    return sum(sep + IL[fs] for _, fs, _, _, sep in lineas_caja(clave))


def ancho_contenido(clave: str) -> float:
    return max(ancho(s, fs, b) for s, fs, b, _, _ in lineas_caja(clave))


def ancho_caja(clave: str) -> int:
    return math.ceil(ancho_contenido(clave) + 2 * PAD_X + 2)


def alto_caja(clave: str) -> int:
    return math.ceil(alto_contenido(clave) + 2 * PAD_Y)


# ========================================================================== #
# Geometría                                                                  #
# ========================================================================== #
# Hoja del Texto Ordenado: esquina plegada y dos renglones sobre el texto.
PLIEGUE = 20
RENGLONES = ((18, 0.60), (28, 0.76))       # (alto desde el borde superior, fracción del ancho útil)
Y_TEXTO_HOJA = 38
SEP_FILA1 = 40                             # entre las cajas de la fila de arriba
# Fila de abajo: carril del conector que baja de las unidades, a la izquierda.
X_CARRIL = 28
X_FILA2 = 56
W_GRAFO, H_FILA2 = 72, 52
NODOS_GLIFO = ((18, 19), (36, 9), (54, 19))
ARISTAS_GLIFO = ((0, 1), (1, 2), (0, 2))
R_NODO = 3.6
Y_TEXTO_GRAFO = 28
# Banda entre filas, de arriba abajo: el conector de las unidades, el bus del
# catálogo (con la caja del catálogo) y la caja del esquema, anidada bajo el bus.
BAJO_FILA1 = 17          # de la hoja al conector
ENTRE_BUSES = 24         # del conector al bus del catálogo
BAJO_BUS = 16            # del bus a la caja del esquema
SOBRE_FILA2 = 24         # de la caja del esquema a la fila de abajo
# Debajo de la fila de abajo.
BAJO_FILA2 = 22          # a los elementos rechazados
BAJO_RECHAZADOS = 20     # a la vuelta al extractor
BAJO_VUELTA = 24         # a la revisión humana y a la cuarentena
SALIDA_VERIFICADOR = 26  # de cada costado del verificador a sus dos salidas de abajo
DX_CUARENTENA = 30       # la salida a la cuarentena, a la derecha del centro del ensamblado
SOBRE_LEYENDA = 36       # de la vuelta al extractor a la leyenda
GRUPO_LEYENDA = 10


def caja(clave: str, x: float, y: float, w: float, h: float, forma: str = "rect") -> dict:
    return {"clave": clave, "x": float(x), "y": float(y), "w": float(w), "h": float(h),
            "clase": CLASE[clave], "forma": forma}


def armar_modelo(D: dict) -> dict:
    """Ubica cajas, flechas y rótulos. Todo se deriva de las constantes y de
    los anchos de texto; nada se dibuja todavía."""
    C = {}
    # ---- fila de arriba --------------------------------------------------- #
    w_hoja = ancho_caja("texto_ordenado")
    h_hoja = math.ceil(Y_TEXTO_HOJA + alto_contenido("texto_ordenado") + PAD_Y)
    C["texto_ordenado"] = caja("texto_ordenado", MARGEN, MARGEN, w_hoja, h_hoja, "hoja")
    cy1 = MARGEN + h_hoja / 2.0
    w_pieza = max(ancho_caja(k) for k in ("segmentacion", "extractor", "validador", "verificador",
                                           "ensamblado"))
    h_una = alto_caja("segmentacion")
    x = MARGEN + w_hoja + SEP_FILA1
    C["segmentacion"] = caja("segmentacion", x, cy1 - h_una / 2.0, w_pieza, h_una)
    x += w_pieza + SEP_FILA1
    C["unidades"] = caja("unidades", x, cy1 - h_una / 2.0, ancho_caja("unidades"), h_una)

    # ---- banda entre filas y fila de abajo ------------------------------- #
    y_u = MARGEN + h_hoja + BAJO_FILA1
    y_c = y_u + ENTRE_BUSES
    y_esq = y_c + BAJO_BUS
    h_esq = alto_caja("esquema")
    y2 = y_esq + h_esq + SOBRE_FILA2
    sep2 = (W - MARGEN - X_FILA2 - 4 * w_pieza - W_GRAFO) / 4.0
    x = X_FILA2
    for k in ("extractor", "validador", "verificador", "ensamblado"):
        C[k] = caja(k, x, y2, w_pieza, H_FILA2)
        x += w_pieza + sep2
    C["grafo"] = caja("grafo", x, y2, W_GRAFO, H_FILA2, "grafo")
    E, V, Ve, A = (C[k] for k in ("extractor", "validador", "verificador", "ensamblado"))
    cy2 = y2 + H_FILA2 / 2.0
    # Esquema, centrado entre el extractor y el validador; catálogo, sobre el ensamblado.
    w_esq = ancho_caja("esquema")
    cx_esq = (E["x"] + E["w"] + V["x"]) / 2.0
    C["esquema"] = caja("esquema", cx_esq - w_esq / 2.0, y_esq, w_esq, h_esq)
    S = C["esquema"]
    w_cat, h_cat = ancho_caja("catalogo"), alto_caja("catalogo")
    cx_a = A["x"] + A["w"] / 2.0
    C["catalogo"] = caja("catalogo", cx_a - w_cat / 2.0, y_c - h_cat / 2.0, w_cat, h_cat)
    K = C["catalogo"]
    # Bajadas: las del esquema dentro de su ancho; las del catálogo, por fuera de él.
    x_e_esq = S["x"] + LEJOS_ESQUINA + 3
    x_v_esq = S["x"] + S["w"] - LEJOS_ESQUINA - 6
    x_e_cat = E["x"] + 28
    x_v_cat = V["x"] + V["w"] - 37

    # ---- debajo de la fila de abajo -------------------------------------- #
    w_rec, h_rec = ancho_caja("rechazados"), alto_caja("rechazados")
    cx_v = V["x"] + V["w"] / 2.0
    y_rec = y2 + H_FILA2 + BAJO_FILA2
    C["rechazados"] = caja("rechazados", cx_v - w_rec / 2.0, y_rec, w_rec, h_rec)
    y_vuelta = y_rec + h_rec + BAJO_RECHAZADOS
    x_vuelta = Ve["x"] + SALIDA_VERIFICADOR
    x_humana = Ve["x"] + Ve["w"] - SALIDA_VERIFICADOR
    cx_e = E["x"] + E["w"] / 2.0
    y_bajo = y_vuelta + BAJO_VUELTA
    w_rev, h_rev = ancho_caja("revision"), alto_caja("revision")
    C["revision"] = caja("revision", x_humana - w_rev / 2.0, y_bajo, w_rev, h_rev)
    x_cuar = cx_a + DX_CUARENTENA
    w_cua, h_cua = ancho_caja("cuarentena"), alto_caja("cuarentena")
    C["cuarentena"] = caja("cuarentena", x_cuar - w_cua / 2.0, y_bajo, w_cua, h_cua)

    # ---- flechas ---------------------------------------------------------- #
    U, TO, SG = C["unidades"], C["texto_ordenado"], C["segmentacion"]
    G = C["grafo"]
    hp = HUECO_PUNTA
    T = []

    def flecha(nombre, desde, hasta, estilo, puntos, red=None, madre=None):
        T.append({"nombre": nombre, "desde": desde, "hasta": hasta, "estilo": estilo,
                  "red": red or nombre, "madre": madre,
                  "puntos": [(float(f(px)), float(f(py))) for px, py in puntos]})

    flecha("Texto Ordenado → Segmentación", "texto_ordenado", "segmentacion", "flujo",
           [(TO["x"] + TO["w"], cy1), (SG["x"] - hp, cy1)])
    flecha("Segmentación → Unidades", "segmentacion", "unidades", "flujo",
           [(SG["x"] + SG["w"], cy1), (U["x"] - hp, cy1)])
    cx_u = U["x"] + U["w"] / 2.0
    flecha("Unidades → Extractor", "unidades", "extractor", "flujo",
           [(cx_u, U["y"] + U["h"]), (cx_u, y_u), (X_CARRIL, y_u), (X_CARRIL, cy2), (E["x"] - hp, cy2)])
    for a, b in (("extractor", "validador"), ("validador", "verificador"),
                 ("verificador", "ensamblado"), ("ensamblado", "grafo")):
        ca, cb = C[a], C[b]
        flecha(f"{TEXTO[a][0][0]} → {TEXTO[b][0][0]}", a, b, "flujo",
               [(ca["x"] + ca["w"], cy2), (cb["x"] - hp, cy2)])
    flecha("Esquema final → Extractor", "esquema", "extractor", "rama",
           [(x_e_esq, S["y"] + S["h"]), (x_e_esq, y2 - hp)], red="esquema")
    flecha("Esquema final → Validador", "esquema", "validador", "rama",
           [(x_v_esq, S["y"] + S["h"]), (x_v_esq, y2 - hp)], red="esquema")
    flecha("Catálogo → Extractor", "catalogo", "extractor", "rama",
           [(K["x"], y_c), (x_e_cat, y_c), (x_e_cat, y2 - hp)], red="catalogo")
    flecha("Catálogo → Validador", "catalogo", "validador", "rama",
           [(x_v_cat, y_c), (x_v_cat, y2 - hp)], red="catalogo", madre="Catálogo → Extractor")
    flecha("Catálogo → Ensamblado", "catalogo", "ensamblado", "rama",
           [(cx_a, K["y"] + K["h"]), (cx_a, y2 - hp)], red="catalogo")
    flecha("Verificador → Extractor", "verificador", "extractor", "rama",
           [(x_vuelta, y2 + H_FILA2), (x_vuelta, y_vuelta), (cx_e, y_vuelta), (cx_e, y2 + H_FILA2 + hp)])
    flecha("Verificador → Revisión humana", "verificador", "revision", "humana",
           [(x_humana, y2 + H_FILA2), (x_humana, y_bajo - hp)])
    flecha("Validador → Elementos rechazados", "validador", "rechazados", "rama",
           [(cx_v, y2 + H_FILA2), (cx_v, y_rec - hp)])
    flecha("Ensamblado → Cuarentena", "ensamblado", "cuarentena", "rama",
           [(x_cuar, y2 + H_FILA2), (x_cuar, y_bajo - hp)])

    # ---- rótulos, cada uno junto a un tramo recto de su flecha ------------ #
    R = [
        {"clave": "reextraccion", "texto": ROTULO_REEXTRACCION.format(n=D["tope"]),
         "flecha": "Verificador → Extractor", "tramo": 1, "lado": "abajo"},
        {"clave": "no_resuelve", "texto": ROTULO_NO_RESUELVE,
         "flecha": "Verificador → Revisión humana", "tramo": 0, "lado": "derecha"},
    ]
    por_nombre = {t["nombre"]: t for t in T}
    for r in R:
        t = por_nombre[r["flecha"]]
        (ax, ay), (bx, by) = t["puntos"][r["tramo"]], t["puntos"][r["tramo"] + 1]
        g = ESTILO_TRAZO[t["estilo"]][1] / 2.0
        if r["lado"] == "abajo":
            r["x"], r["ancla"] = (ax + bx) / 2.0, "middle"
            r["y"] = ay + g + ROTULO_AIRE + ASC * FS_TEXTO
        else:
            r["x"], r["ancla"] = ax + g + ROTULO_AIRE, "start"
            r["y"] = (ay + by) / 2.0 + (ASC - DESC) / 2.0 * FS_TEXTO
        r["x"], r["y"] = float(f(r["x"])), float(f(r["y"]))

    # ---- leyenda, abajo a la izquierda ------------------------------------ #
    y_ley = y_vuelta + SOBRE_LEYENDA
    w_ley = 12 + MUESTRA_W + 9 + max(ancho(s, FS_TEXTO, False) for _, s in LEYENDA) + 12
    h_ley = GRUPO_LEYENDA + len(LEYENDA) * FILA_LEY + 6
    L = {"x": float(MARGEN), "y": float(f(y_ley)), "w": float(f(w_ley)), "h": float(h_ley)}

    alto = math.ceil(max(L["y"] + L["h"], max(c["y"] + c["h"] for c in C.values())) + MARGEN)
    return {"cajas": C, "trazos": T, "rotulos": R, "leyenda": L, "alto": alto,
            "geo": {"y_conector": y_u, "y_bus": y_c, "y_vuelta": y_vuelta, "sep_fila2": sep2,
                    "w_pieza": w_pieza}}


# ========================================================================== #
# Elementos derivados: textos, marcas, puntas                                #
# ========================================================================== #
def f(v: float) -> str:
    """Formato fijo (el de la figura hermana): el SVG no depende de la
    representación del float."""
    return f"{v:.1f}"


def bb(c: dict) -> tuple:
    return (c["x"], c["y"], c["x"] + c["w"], c["y"] + c["h"])


def grosor_caja(c: dict) -> float:
    return GROSOR_DISCONTINUA if c["clase"] == "humana" else GROSOR_CAJA


def textos_de(M: dict) -> list[dict]:
    """Todo texto dibujado, con su caja, su posición y su pieza."""
    out = []
    for clave, c in M["cajas"].items():
        top = {"hoja": Y_TEXTO_HOJA, "grafo": Y_TEXTO_GRAFO}.get(c["forma"])
        yy = c["y"] + (top if top is not None else (c["h"] - alto_contenido(clave)) / 2.0)
        for i, (s, fs, negrita, color, sep) in enumerate(lineas_caja(clave)):
            yy += sep
            base = yy + (IL[fs] - fs) / 2.0 + ASC * fs
            out.append({"s": s, "fs": fs, "negrita": negrita, "color": color, "ancla": "middle",
                        "x": float(f(c["x"] + c["w"] / 2.0)), "y": float(f(base)),
                        "dentro": clave, "pieza": (clave, i)})
            yy += IL[fs]
    for r in M["rotulos"]:
        out.append({"s": r["texto"], "fs": FS_TEXTO, "negrita": False, "color": TINTA_SUB,
                    "ancla": r["ancla"], "x": r["x"], "y": r["y"], "dentro": None,
                    "pieza": ("rotulo", r["clave"])})
    L = M["leyenda"]
    for k, (_, s) in enumerate(LEYENDA):
        yc = L["y"] + GRUPO_LEYENDA + k * FILA_LEY + FILA_LEY / 2.0
        out.append({"s": s, "fs": FS_TEXTO, "negrita": False, "color": TINTA, "ancla": "start",
                    "x": float(f(L["x"] + 12 + MUESTRA_W + 9)), "y": float(f(yc + 0.28 * FS_TEXTO)),
                    "dentro": "leyenda", "pieza": ("leyenda", k)})
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
    x0 = {"start": t["x"], "middle": t["x"] - a / 2.0, "end": t["x"] - a}[t["ancla"]]
    return (x0, t["y"] - ASC * t["fs"], x0 + a, t["y"] + DESC * t["fs"])


def marcas_de(M: dict) -> list[tuple]:
    """(nombre, caja envolvente, dibujo) de cada marca: renglones y pliegue de
    la hoja, nodos y aristas del glifo del grafo."""
    out = []
    H = M["cajas"]["texto_ordenado"]
    x, y, w = H["x"], H["y"], H["w"]
    pl = [(x + w - PLIEGUE, y), (x + w - PLIEGUE, y + PLIEGUE), (x + w, y + PLIEGUE)]
    out.append(("pliegue", (pl[0][0] - GROSOR_CAJA / 2, y - GROSOR_CAJA / 2, x + w + GROSOR_CAJA / 2,
                            y + PLIEGUE + GROSOR_CAJA / 2), ("polilinea", pl, NEUTRO["borde"], GROSOR_CAJA)))
    for k, (dy, frac) in enumerate(RENGLONES):
        x0, x1 = x + 12, x + 12 + (w - 24) * frac
        out.append((f"renglón {k + 1}", (x0 - 1.5, y + dy - 1.5, x1 + 1.5, y + dy + 1.5),
                    ("renglon", [(x0, y + dy), (x1, y + dy)], "#c4c4c4", 3)))
    G = M["cajas"]["grafo"]
    for a, b in ARISTAS_GLIFO:
        (xa, ya), (xb, yb) = NODOS_GLIFO[a], NODOS_GLIFO[b]
        p, q = (G["x"] + xa, G["y"] + ya), (G["x"] + xb, G["y"] + yb)
        out.append((f"glifo, arista {a + 1}-{b + 1}",
                    (min(p[0], q[0]) - 0.65, min(p[1], q[1]) - 0.65, max(p[0], q[0]) + 0.65,
                     max(p[1], q[1]) + 0.65), ("arista", [p, q], GRIS_ARISTA, 1.3)))
    for k, (dx, dy) in enumerate(NODOS_GLIFO):
        cx, cy = G["x"] + dx, G["y"] + dy
        out.append((f"glifo, nodo {k + 1}", (cx - R_NODO, cy - R_NODO, cx + R_NODO, cy + R_NODO),
                    ("nodo", (cx, cy), DETERMINISTICA["borde"], R_NODO)))
    return out


def punta(t: dict) -> tuple:
    """Triángulo de la punta (marcador de 10 × 10, refX 9, a 6 veces el grosor)."""
    g = ESTILO_TRAZO[t["estilo"]][1]
    (xa, ya), (xb, yb) = t["puntos"][-2], t["puntos"][-1]
    largo = math.hypot(xb - xa, yb - ya)
    ux, uy = (xb - xa) / largo, (yb - ya) / largo
    lp = 6 * g
    tip = (xb + 0.1 * lp * ux, yb + 0.1 * lp * uy)
    bx, by = xb - 0.9 * lp * ux, yb - 0.9 * lp * uy
    return (tip, (bx - 0.5 * lp * uy, by + 0.5 * lp * ux), (bx + 0.5 * lp * uy, by - 0.5 * lp * ux))


def caja_punta(t: dict) -> tuple:
    p = punta(t)
    return (min(q[0] for q in p), min(q[1] for q in p), max(q[0] for q in p), max(q[1] for q in p))


def tramos(t: dict) -> list[tuple]:
    return list(zip(t["puntos"], t["puntos"][1:]))


# ========================================================================== #
# Geometría de los controles                                                 #
# ========================================================================== #
def cruza(a, b) -> bool:
    return a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]


def ampliar(b, d) -> tuple:
    return (b[0] - d, b[1] - d, b[2] + d, b[3] + d)


def contiene(c, b, holgura=0.0) -> bool:
    return (c[0] + holgura <= b[0] and b[2] <= c[2] - holgura
            and c[1] + holgura <= b[1] and b[3] <= c[3] - holgura)


def corta(p, q, r) -> bool:
    """True si el segmento pq pasa por el interior abierto del rectángulo r
    (recorte de Liang-Barsky)."""
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
    return min([dist_punto_caja(p, r), dist_punto_caja(q, r)]
               + [dist_punto_segmento(e, p, q) for e in esquinas])


def dist_segmentos(a0, a1, b0, b1) -> float:
    if contacto(a0, a1, b0, b1) is not None:
        return 0.0
    return min(dist_punto_segmento(a0, b0, b1), dist_punto_segmento(a1, b0, b1),
               dist_punto_segmento(b0, a0, a1), dist_punto_segmento(b1, a0, a1))


def sobre(p, a, b, tol=1e-6) -> bool:
    return (min(a[0], b[0]) - tol <= p[0] <= max(a[0], b[0]) + tol
            and min(a[1], b[1]) - tol <= p[1] <= max(a[1], b[1]) + tol
            and abs((b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])) <= tol)


def contacto(a0, a1, b0, b1):
    """Punto de contacto entre dos tramos ortogonales, o None. Devuelve
    («x», punto) si se cruzan en X, («toque», punto) si uno toca al otro con
    un extremo y («superpuestos», punto) si van uno sobre otro."""
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
    p = (lo, a0[1]) if ha else (a0[0], lo)
    return ("superpuestos", p)


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


# ========================================================================== #
# Controles                                                                  #
# ========================================================================== #
def controlar_contenido(M: dict, D: dict) -> dict:
    if sorted(M["cajas"]) != sorted(TEXTO):
        freno("contenido", f"cajas dibujadas {sorted(M['cajas'])} ≠ las fijadas {sorted(TEXTO)}")
    for clave, c in M["cajas"].items():
        if c["clase"] != CLASE[clave]:
            freno("contenido", f"la caja «{clave}» es «{c['clase']}» y le corresponde «{CLASE[clave]}»")
    if D["tope"] != 1:
        freno("contenido", f"el tope de re-extracciones del código es {D['tope']}: el rótulo dice «1 vez»")
    textos = textos_de(M)
    por_pieza = {}
    for t in textos:
        por_pieza.setdefault(t["pieza"][0], []).append((t["pieza"][1], t["s"]))
        for rx in PROHIBIDOS:
            if rx.search(t["s"]):
                freno("contenido", f"«{t['s']}» lleva {rx.pattern!r}")
        digitos = re.findall(r"\d+", t["s"])
        if digitos and not (t["pieza"] == ("rotulo", "reextraccion") and digitos == [str(D["tope"])]):
            freno("contenido", f"«{t['s']}» lleva cifras")
    for clave in TEXTO:
        dibujado = [s for _, s in sorted(por_pieza.pop(clave, []))]
        if dibujado != [s for s, _ in TEXTO[clave]]:
            freno("contenido", f"«{clave}»: dibujado {dibujado} ≠ fijado {[s for s, _ in TEXTO[clave]]}")
    rot = dict(por_pieza.pop("rotulo", []))
    fijados = {"reextraccion": ROTULO_REEXTRACCION.format(n=D["tope"]), "no_resuelve": ROTULO_NO_RESUELVE}
    if rot != fijados:
        freno("contenido", f"rótulos dibujados {rot} ≠ fijados {fijados}")
    ley = [s for _, s in sorted(por_pieza.pop("leyenda", []))]
    if ley != [s for _, s in LEYENDA]:
        freno("contenido", f"leyenda dibujada {ley} ≠ fijada")
    if por_pieza:
        freno("contenido", f"textos sin pieza fijada: {sorted(por_pieza)}")
    return {"textos": len(textos)}


def controlar_trazado(M: dict) -> dict:
    T = M["trazos"]
    por_nombre = {t["nombre"]: t for t in T}
    # 1. tramos: ni diagonales ni nulos
    n_tramos = 0
    for t in T:
        for p, q in tramos(t):
            n_tramos += 1
            if p == q:
                freno("trazado", f"tramo nulo en «{t['nombre']}» en {p}")
            if p[0] != q[0] and p[1] != q[1]:
                freno("trazado", f"tramo diagonal en «{t['nombre']}»: {p} → {q}")
        for (a, b), (c, d) in zip(tramos(t), tramos(t)[1:]):
            if direccion(a, b) == tuple(-v for v in direccion(c, d)):
                freno("trazado", f"«{t['nombre']}» vuelve sobre sí misma en {b}")
    # 2. extremos: salida del borde de su caja (o de su flecha madre) y llegada al borde de la de destino
    C = M["cajas"]
    for t in T:
        p0, p1 = t["puntos"][0], t["puntos"][1]
        if t["madre"]:
            m = por_nombre.get(t["madre"])
            if m is None or m["red"] != t["red"]:
                freno("trazado", f"«{t['nombre']}» arranca de una flecha que no es de su red")
            if not any(sobre(p0, a, b) and p0 not in (a, b) for a, b in tramos(m)):
                freno("trazado", f"«{t['nombre']}» no arranca sobre un tramo de «{t['madre']}»")
        else:
            lado = en_borde(p0, C[t["desde"]])
            if lado is None or direccion(p0, p1) != NORMAL[lado]:
                freno("trazado", f"«{t['nombre']}» no sale del borde de «{t['desde']}» hacia afuera ({p0})")
        q0, q1 = t["puntos"][-2], t["puntos"][-1]
        dx, dy = direccion(q0, q1)
        llegada = (q1[0] + HUECO_PUNTA * dx, q1[1] + HUECO_PUNTA * dy)
        lado = en_borde(llegada, C[t["hasta"]])
        if lado is None or (dx, dy) != tuple(-v for v in NORMAL[lado]):
            freno("trazado", f"«{t['nombre']}» no llega al borde de «{t['hasta']}» ({q1})")
    # 3. conexiones: exactamente las fijadas, con su estilo y su rótulo
    rot = {r["flecha"]: r["clave"] for r in M["rotulos"]}
    dibujadas = sorted((t["desde"], t["hasta"], t["estilo"], rot.get(t["nombre"], "")) for t in T)
    fijadas = sorted((a, b, e, r or "") for a, b, e, r in CONEXIONES)
    if dibujadas != fijadas:
        sobran = [c for c in dibujadas if c not in fijadas]
        faltan = [c for c in fijadas if c not in dibujadas]
        freno("trazado", f"flechas distintas de las fijadas: sobran {sobran}; faltan {faltan}")
    return {"flechas": len(T), "tramos": n_tramos}


def controlar_cajas(M: dict) -> dict:
    C = M["cajas"]
    todas = [(k, bb(c), grosor_caja(c)) for k, c in C.items()]
    L = M["leyenda"]
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
                freno("cajas", f"la caja «{ka}» se superpone con «{kb}» o queda a {d:.1f} (< {SEP_CAJAS})")
    for t in M["trazos"]:
        for k, r, _ in todas:
            interior = ampliar(r, -1.0)
            if any(corta(p, q, interior) for p, q in tramos(t)):
                freno("cajas", f"la flecha «{t['nombre']}» atraviesa la caja «{k}»")
            if cruza(caja_punta(t), ampliar(r, -0.5)):
                freno("cajas", f"la punta de «{t['nombre']}» entra en la caja «{k}»")
    return {"cajas": len(todas), "separacion_minima": minimo}


def controlar_cruces(M: dict) -> dict:
    T = M["trazos"]
    cruces, contactos, minimo = [], [], (math.inf, "", "")
    for i in range(len(T)):
        for j in range(i + 1, len(T)):
            a, b = T[i], T[j]
            familia = a["madre"] == b["nombre"] or b["madre"] == a["nombre"]
            arranque = (b["puntos"][0] if b["madre"] == a["nombre"]
                        else a["puntos"][0] if a["madre"] == b["nombre"] else None)
            for p, q in tramos(a):
                for u, v in tramos(b):
                    c = contacto(p, q, u, v)
                    if c is not None and not (familia and c[1] == arranque):
                        (cruces if c[0] == "x" else contactos).append((a["nombre"], b["nombre"], c[1], c[0]))
            if not familia:
                d = min(dist_segmentos(p, q, u, v) for p, q in tramos(a) for u, v in tramos(b))
                d -= (ESTILO_TRAZO[a["estilo"]][1] + ESTILO_TRAZO[b["estilo"]][1]) / 2.0
                if d < minimo[0]:
                    minimo = (d, a["nombre"], b["nombre"])
    if cruces or contactos:
        def fmt(x):
            return "; ".join(f"«{n1}» × «{n2}» en ({p[0]:g}, {p[1]:g})" for n1, n2, p, _ in x)
        partes = []
        if cruces:
            partes.append(f"{len(cruces)} cruce(s) entre flechas: {fmt(cruces)}")
        if contactos:
            partes.append(f"{len(contactos)} contacto(s) entre flechas: {fmt(contactos)}")
        freno("cruces", " | ".join(partes))
    if minimo[0] < DISTANCIA_MIN:
        freno("cruces", f"«{minimo[1]}» pasa a {minimo[0]:.1f} de «{minimo[2]}» (< {DISTANCIA_MIN})")
    for t in T:
        for o in T:
            if o is t:
                continue
            for p, q in tramos(o):
                if dist_segmento_caja(p, q, caja_punta(t)) - ESTILO_TRAZO[o["estilo"]][1] / 2.0 < HOLGURA_TEXTO:
                    if o["nombre"] == t["madre"] or t["nombre"] == o["madre"]:
                        continue
                    freno("cruces", f"la punta de «{t['nombre']}» toca la flecha «{o['nombre']}»")
    return {"cruces": len(cruces), "distancia_minima": minimo}


def controlar_textos(M: dict) -> dict:
    C = M["cajas"]
    textos = [(t, caja_texto(t)) for t in textos_de(M)]
    marcas = marcas_de(M)
    L = M["leyenda"]
    contenedores = {k: (bb(c), grosor_caja(c)) for k, c in C.items()}
    contenedores["leyenda"] = ((L["x"], L["y"], L["x"] + L["w"], L["y"] + L["h"]), 1.0)
    muestras = [(m["clave"], (m["x"], m["y"], m["x"] + m["w"], m["y"] + m["h"])) for m in muestras_leyenda(M)]
    minimos = {"texto-texto": math.inf, "texto-trazo": math.inf, "texto-marca": math.inf,
               "texto-borde de su caja": math.inf}
    tamanos = {}
    for t, r in textos:
        pt = puntos_impresos(t["fs"])
        tamanos[t["fs"]] = pt
        if pt < PT_MINIMO:
            freno("textos", f"«{t['s']}»: letra de {pt:.2f} pt (< {PT_MINIMO})")
        if r[0] < 0 or r[1] < 0 or r[2] > W or r[3] > M["alto"]:
            freno("textos", f"«{t['s']}» sale del lienzo")
        if t["dentro"] is not None:
            c, g = contenedores[t["dentro"]]
            holg = min(r[0] - c[0], c[2] - r[2], r[1] - c[1], c[3] - r[3])
            minimos["texto-borde de su caja"] = min(minimos["texto-borde de su caja"], holg)
            if holg < g / 2.0 + HOLGURA_TEXTO:
                freno("textos", f"«{t['s']}» a {holg:.1f} del borde de su caja «{t['dentro']}»")
        for k, (c, g) in contenedores.items():
            if k != t["dentro"] and cruza(r, ampliar(c, g / 2.0)):
                freno("textos", f"«{t['s']}» se superpone con la caja «{k}»")
        for k, m in muestras:
            if cruza(ampliar(r, HOLGURA_TEXTO), m):
                freno("textos", f"«{t['s']}» toca la muestra «{k}» de la leyenda")
        for nombre, m, _ in marcas:
            dx = max(m[0] - r[2], 0.0, r[0] - m[2])
            dy = max(m[1] - r[3], 0.0, r[1] - m[3])
            minimos["texto-marca"] = min(minimos["texto-marca"], math.hypot(dx, dy))
            if cruza(ampliar(r, HOLGURA_TEXTO), m):
                freno("textos", f"«{t['s']}» toca la marca «{nombre}»")
        for tr in M["trazos"]:
            g = ESTILO_TRAZO[tr["estilo"]][1] / 2.0
            d = min(dist_segmento_caja(p, q, r) for p, q in tramos(tr)) - g
            minimos["texto-trazo"] = min(minimos["texto-trazo"], d)
            if d < HOLGURA_TEXTO:
                freno("textos", f"«{t['s']}» toca la flecha «{tr['nombre']}»")
            if cruza(ampliar(r, HOLGURA_TEXTO), caja_punta(tr)):
                freno("textos", f"«{t['s']}» toca la punta de «{tr['nombre']}»")
    for i in range(len(textos)):
        for j in range(i + 1, len(textos)):
            (ta, a), (tb, b) = textos[i], textos[j]
            if cruza(a, b):
                freno("textos", f"«{ta['s']}» se superpone con «{tb['s']}»")
            dx = max(b[0] - a[2], 0.0, a[0] - b[2])
            dy = max(b[1] - a[3], 0.0, a[1] - b[3])
            minimos["texto-texto"] = min(minimos["texto-texto"], math.hypot(dx, dy))
    return {"textos": len(textos), "tamanos": tamanos, "minimos": minimos, "cajas_texto": textos}


def controlar_rotulos(M: dict) -> dict:
    por_nombre = {t["nombre"]: t for t in M["trazos"]}
    textos = {t["pieza"][1]: (t, caja_texto(t)) for t in textos_de(M) if t["pieza"][0] == "rotulo"}
    out = {}
    for r in M["rotulos"]:
        t = por_nombre[r["flecha"]]
        _, rb = textos[r["clave"]]
        a, b = t["puntos"][r["tramo"]], t["puntos"][r["tramo"] + 1]
        g = ESTILO_TRAZO[t["estilo"]][1] / 2.0
        if a[1] == b[1]:
            lo, hi = sorted((a[0], b[0]))
            dentro = lo + RADIO <= rb[0] and rb[2] <= hi - RADIO
            gap = max(rb[1] - a[1], a[1] - rb[3]) - g
        else:
            lo, hi = sorted((a[1], b[1]))
            dentro = lo + RADIO <= rb[1] and rb[3] <= hi - RADIO
            gap = max(rb[0] - a[0], a[0] - rb[2]) - g
        if not dentro:
            freno("rotulos", f"«{r['texto']}» se sale del tramo recto de «{t['nombre']}»")
        if not (HOLGURA_TEXTO <= gap <= JUNTO):
            freno("rotulos", f"«{r['texto']}» a {gap:.1f} de su tramo (entre {HOLGURA_TEXTO} y {JUNTO})")
        ajena = min((min(dist_segmento_caja(p, q, rb) for p, q in tramos(o))
                     - ESTILO_TRAZO[o["estilo"]][1] / 2.0, o["nombre"])
                    for o in M["trazos"] if o is not t)
        if ajena[0] < gap + AJENA:
            freno("rotulos", f"«{r['texto']}» queda a {ajena[0]:.1f} de «{ajena[1]}», "
                             f"más cerca que {gap:.1f} + {AJENA}")
        out[r["texto"]] = (gap, ajena)
    return out


def controlar_margen(M: dict, textos) -> dict:
    todas = [(f"texto «{t['s']}»", r) for t, r in textos]
    todas += [(f"caja «{k}»", ampliar(bb(c), grosor_caja(c) / 2.0)) for k, c in M["cajas"].items()]
    L = M["leyenda"]
    todas.append(("leyenda", ampliar((L["x"], L["y"], L["x"] + L["w"], L["y"] + L["h"]), 0.5)))
    todas += [(f"marca «{n}»", m) for n, m, _ in marcas_de(M)]
    for t in M["trazos"]:
        g = ESTILO_TRAZO[t["estilo"]][1] / 2.0
        xs, ys = [p[0] for p in t["puntos"]], [p[1] for p in t["puntos"]]
        todas.append((f"flecha «{t['nombre']}»", (min(xs) - g, min(ys) - g, max(xs) + g, max(ys) + g)))
        todas.append((f"punta de «{t['nombre']}»", caja_punta(t)))
    distancia = {"izquierdo": lambda r: r[0], "superior": lambda r: r[1],
                 "derecho": lambda r: W - r[2], "inferior": lambda r: M["alto"] - r[3]}
    minimos = {}
    for borde, d in distancia.items():
        minimos[borde] = min(d(r) for _, r in todas)
        for nombre, r in todas:
            if d(r) < MARGEN_MIN:
                freno("margen", f"{nombre} a {d(r):.1f} unidades del borde {borde} (< {MARGEN_MIN:.1f})")
    return {"elementos": len(todas), "minimos": minimos}


def verificar(M: dict, D: dict) -> dict:
    rep = {"contenido": controlar_contenido(M, D), "trazado": controlar_trazado(M),
           "cajas": controlar_cajas(M), "cruces": controlar_cruces(M)}
    rep["textos"] = controlar_textos(M)
    rep["rotulos"] = controlar_rotulos(M)
    rep["margen"] = controlar_margen(M, rep["textos"]["cajas_texto"])
    svg, dibujados = dibujar(M)
    rep["registro"] = controlar_registro(svg, dibujados, M)
    rep["svg"] = svg
    return rep


# ========================================================================== #
# Emisión del SVG                                                            #
# ========================================================================== #
def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def path_redondeado(puntos) -> str:
    """Poligonal con esquinas redondeadas de radio RADIO (la técnica de la hermana)."""
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


def dibujar(M: dict) -> tuple[str, list]:
    partes, dib = [], []

    def add(etiqueta, s):
        partes.append(s)
        dib.append(etiqueta)

    C = M["cajas"]
    for clave, c in C.items():
        pal = PALETA[c["clase"]]
        x, y, w, h = c["x"], c["y"], c["w"], c["h"]
        if c["forma"] == "hoja":
            p = PLIEGUE
            add(("caja", clave),
                f'<path data-caja="{clave}" d="M{f(x + 4)},{f(y)} L{f(x + w - p)},{f(y)} '
                f'L{f(x + w)},{f(y + p)} L{f(x + w)},{f(y + h - 4)} '
                f'Q{f(x + w)},{f(y + h)} {f(x + w - 4)},{f(y + h)} '
                f'L{f(x + 4)},{f(y + h)} Q{f(x)},{f(y + h)} {f(x)},{f(y + h - 4)} '
                f'L{f(x)},{f(y + 4)} Q{f(x)},{f(y)} {f(x + 4)},{f(y)} Z" '
                f'fill="{pal["relleno"]}" stroke="{pal["borde"]}" stroke-width="{GROSOR_CAJA}"/>')
        else:
            guiones = f' stroke-dasharray="{GUIONES}"' if c["clase"] == "humana" else ""
            add(("caja", clave),
                f'<rect data-caja="{clave}" x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" '
                f'fill="{pal["relleno"]}" stroke="{pal["borde"]}" stroke-width="{grosor_caja(c)}" '
                f'rx="{RX}"{guiones}/>')
    for nombre, _, (tipo, geo, color, g) in marcas_de(M):
        if tipo == "nodo":
            add(("marca", nombre), f'<circle cx="{f(geo[0])}" cy="{f(geo[1])}" r="{g}" fill="{color}"/>')
        else:
            d = " ".join(("M" if i == 0 else "L") + f"{f(px)},{f(py)}" for i, (px, py) in enumerate(geo))
            cap = ' stroke-linecap="round"' if tipo == "renglon" else ""
            add(("marca", nombre), f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{g}"{cap}/>')
    for t in M["trazos"]:
        color, g, discontinua, marcador = ESTILO_TRAZO[t["estilo"]]
        dash = f' stroke-dasharray="{GUIONES}"' if discontinua else ""
        add(("flecha", t["nombre"]),
            f'<path data-flecha="{esc(t["nombre"])}" d="{path_redondeado(t["puntos"])}" fill="none" '
            f'stroke="{color}" stroke-width="{g}"{dash} marker-end="url(#{marcador})"/>')
    L = M["leyenda"]
    add(("leyenda", "marco"),
        f'<rect x="{f(L["x"])}" y="{f(L["y"])}" width="{f(L["w"])}" height="{f(L["h"])}" {LEYENDA_MARCO}/>')
    for m in muestras_leyenda(M):
        pal = PALETA[m["clase"]]
        add(("leyenda", m["clave"]),
            f'<rect data-caja="{m["clave"]}" x="{f(m["x"])}" y="{f(m["y"])}" width="{f(m["w"])}" '
            f'height="{f(m["h"])}" fill="{pal["relleno"]}" stroke="{pal["borde"]}" '
            f'stroke-width="{GROSOR_CAJA}" rx="3"/>')
    for t in textos_de(M):
        anc = "" if t["ancla"] == "start" else f' text-anchor="{t["ancla"]}"'
        peso = "bold" if t["negrita"] else "normal"
        add(("texto", t["s"]),
            f'<text x="{f(t["x"])}" y="{f(t["y"])}"{anc} font-size="{t["fs"]}" font-weight="{peso}" '
            f'fill="{t["color"]}">{esc(t["s"])}</text>')
    alto = M["alto"]
    alto_cm = ANCHO_CM * alto / W
    cabeza = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{ANCHO_CM:.2f}cm" height="{alto_cm:.2f}cm" '
        f'viewBox="0 0 {W} {alto}" font-family="{TIPOGRAFIA}">',
        f'<rect width="{W}" height="{alto}" fill="white"/>',
        f'<defs><marker id="arN" {MARCADOR} fill="{FLECHA}"/></marker>'
        f'<marker id="arG" {MARCADOR} fill="{GRIS_ARISTA}"/></marker></defs>',
    ]
    return "\n".join(cabeza + partes + ["</svg>"]) + "\n", dib


def controlar_registro(svg: str, dibujados: list, M: dict) -> dict:
    """El SVG se relee: cada elemento está registrado, en orden, y cada caja,
    muestra de la leyenda y flecha tiene el color de su clase."""
    ns = "{http://www.w3.org/2000/svg}"
    raiz = ET.fromstring(svg)
    hijos = list(raiz)
    tags = [el.tag.replace(ns, "") for el in hijos]
    esperado = {"caja": None, "marca": None, "flecha": "path", "leyenda": "rect", "texto": "text"}
    if tags[:2] != ["rect", "defs"]:
        freno("registro", f"el SVG no empieza con el fondo y las definiciones: {tags[:2]}")
    if len(tags) - 2 != len(dibujados):
        freno("registro", f"{len(tags) - 2} elementos en el SVG y {len(dibujados)} registrados")
    for el, tag, (tipo, nombre) in zip(hijos[2:], tags[2:], dibujados):
        if esperado[tipo] and tag != esperado[tipo]:
            freno("registro", f"{tipo} «{nombre}» emitido como <{tag}>")
        if tag == "text" and el.text != nombre:
            freno("registro", f"texto «{nombre}» emitido como «{el.text}»")
    colores = {"cajas": 0, "muestras": 0, "flechas": 0}
    clase_de = dict(CLASE, **{f"leyenda_{c}": c for c, _ in LEYENDA})
    for el in hijos[2:]:
        clave = el.get("data-caja")
        if clave is not None:
            pal = PALETA[clase_de[clave]]
            if (el.get("fill"), el.get("stroke")) != (pal["relleno"], pal["borde"]):
                freno("registro", f"«{clave}» con relleno {el.get('fill')} y borde {el.get('stroke')}, "
                                  f"no los de «{clase_de[clave]}»")
            colores["muestras" if clave.startswith("leyenda_") else "cajas"] += 1
        nombre = el.get("data-flecha")
        if nombre is not None:
            t = next(t for t in M["trazos"] if t["nombre"] == nombre)
            color, g, discontinua, marcador = ESTILO_TRAZO[t["estilo"]]
            if (el.get("stroke"), el.get("stroke-width"), el.get("stroke-dasharray") is not None,
                    el.get("marker-end")) != (color, str(g), discontinua, f"url(#{marcador})"):
                freno("registro", f"la flecha «{nombre}» no tiene el trazo de su estilo «{t['estilo']}»")
            colores["flechas"] += 1
    if colores["cajas"] != len(M["cajas"]) or colores["muestras"] != len(LEYENDA):
        freno("registro", f"cajas o muestras sin color controlado: {colores}")
    return {"elementos": len(dibujados), "colores": colores}


# ========================================================================== #
# Exportación                                                                #
# ========================================================================== #
# cairo escribe /CreationDate en el PDF; con SOURCE_DATE_EPOCH fijo el PDF es
# byte-reproducible (el recurso de las figuras hermanas).
SOURCE_DATE_EPOCH = "0"


def grabar_densidad(ruta: str, dpi: int) -> None:
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


def png_dimensiones(ruta: str) -> tuple[int, int]:
    with open(ruta, "rb") as fh:
        cab = fh.read(24)
    return struct.unpack(">II", cab[16:24])


def pdf_mediabox(ruta: str) -> tuple[float, float]:
    """MediaBox de la página, buscada en claro y en los flujos comprimidos."""
    with open(ruta, "rb") as fh:
        datos = fh.read()
    textos = [datos]
    for m in re.finditer(rb"stream\r?\n", datos):
        fin = datos.find(b"endstream", m.end())
        try:
            textos.append(zlib.decompress(datos[m.end():fin]))
        except zlib.error:
            pass
    for t in textos:
        m = re.search(rb"/MediaBox\s*\[\s*([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s*\]", t)
        if m:
            x0, y0, x1, y1 = (float(v) for v in m.groups())
            return (x1 - x0, y1 - y0)
    freno("exportacion", "el PDF no declara su MediaBox")


def exportar(ruta_svg: str, ruta_png: str, ruta_pdf: str) -> None:
    rsvg = shutil.which("rsvg-convert")
    if not rsvg:
        freno("exportacion", "rsvg-convert no está instalado: no se escriben el PNG ni el PDF")
    subprocess.run([rsvg, "-w", str(ANCHO_PNG_PX), "-f", "png", "-o", ruta_png, ruta_svg], check=True)
    grabar_densidad(ruta_png, DPI)
    entorno = dict(os.environ, SOURCE_DATE_EPOCH=SOURCE_DATE_EPOCH)
    subprocess.run([rsvg, "-f", "pdf", "-o", ruta_pdf, ruta_svg], check=True, env=entorno)


# ========================================================================== #
# Pruebas negativas                                                          #
# ========================================================================== #
def _mut_rotulo_sobre_caja(M):
    """El rótulo de la re-extracción, sobre la caja del validador."""
    r = next(r for r in M["rotulos"] if r["clave"] == "reextraccion")
    V = M["cajas"]["validador"]
    r["x"], r["y"] = V["x"] + V["w"] / 2.0, V["y"] + V["h"] - 6


def _mut_tramo_diagonal(M):
    """La flecha del validador al verificador llega 10 unidades más abajo."""
    t = next(t for t in M["trazos"] if t["nombre"] == "Validador → Verificador")
    t["puntos"][-1] = (t["puntos"][-1][0], t["puntos"][-1][1] + 10)


def _mut_cruce_entre_flechas(M):
    """La flecha a la revisión humana sale del verificador a la izquierda de la
    vuelta al extractor, baja por debajo de ella y dobla hacia su caja: cruza
    una sola vez el tramo horizontal de la vuelta."""
    t = next(t for t in M["trazos"] if t["nombre"] == "Verificador → Revisión humana")
    Ve, Rv = M["cajas"]["verificador"], M["cajas"]["revision"]
    x0 = Ve["x"] + LEJOS_ESQUINA
    y_giro = M["geo"]["y_vuelta"] + 12
    x1 = Rv["x"] + LEJOS_ESQUINA + 2
    t["puntos"] = [(x0, Ve["y"] + Ve["h"]), (x0, y_giro), (x1, y_giro), (x1, Rv["y"] - HUECO_PUNTA)]


# mutación → (función, control que tiene que frenar, textos que el freno tiene que nombrar)
MUTACIONES = {
    "rotulo_sobre_caja": (_mut_rotulo_sobre_caja, "textos",
                          ("«re-extracción, 1 vez» se superpone con la caja «validador»",)),
    "tramo_diagonal": (_mut_tramo_diagonal, "trazado", ("tramo diagonal en «Validador → Verificador»",)),
    "cruce_entre_flechas": (_mut_cruce_entre_flechas, "cruces",
                            ("1 cruce(s) entre flechas", "«Verificador → Extractor» × "
                                                         "«Verificador → Revisión humana»")),
}


def probar_mutacion(nombre: str, M: dict, D: dict) -> str:
    funcion, control, esperado = MUTACIONES[nombre]
    M2 = copy.deepcopy(M)
    funcion(M2)
    try:
        verificar(M2, D)
    except Freno as e:
        msg = str(e)
        if not msg.startswith(f"[{control}]") or not all(x in msg for x in esperado):
            freno("pruebas", f"la mutación {nombre} frenó en otro control o con otro motivo: {msg}")
        return msg
    freno("pruebas", f"la mutación {nombre} no frenó")


# ========================================================================== #
# Principal                                                                  #
# ========================================================================== #
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--salida", default=AQUI,
                    help="directorio del SVG, el PNG y el PDF (por omisión, el del script)")
    ap.add_argument("--mutacion", choices=sorted(MUTACIONES),
                    help="inyecta un defecto: el generador tiene que frenar sin escribir nada")
    args = ap.parse_args()
    try:
        D = leer_fuentes()
        M = armar_modelo(D)
        base = copy.deepcopy(M)
        if args.mutacion:
            MUTACIONES[args.mutacion][0](M)
            verificar(M, D)
            print(f"ERROR: la mutación {args.mutacion} no frenó")
            return 2
        rep = verificar(M, D)
        negativas = {n: probar_mutacion(n, base, D) for n in sorted(MUTACIONES)}
    except Freno as e:
        print(f"FRENO {e}")
        print("No se escribe nada.")
        return 1

    print("FUENTES (sha256 comprobado; sin candado de archivo, el sha leído):")
    for clave, (rel, sha) in FUENTES.items():
        marca = sha if sha is not None else f"{LEIDOS[clave]} (candado: la línea del tope)"
        print(f"  {clave:12s} {rel}  {marca}")
    print("ESTILO Y TOPE (cada valor que usa la figura, contra la línea que lo declara):")
    for k, v in D["lineas"].items():
        print(f"  {k:20s} {v}")
    print(f"  tope de re-extracciones del verificador: {D['tope']}")
    c = rep["contenido"]
    print(f"CONTENIDO: {c['textos']} textos, los fijados; ninguno con identificadores, archivos, modelos "
          f"ni cifras (salvo el «{D['tope']}» del rótulo, = tope del código)")
    t = rep["trazado"]
    print(f"TRAZADO: {t['flechas']} flechas, {t['tramos']} tramos, 0 diagonales; extremos en el borde de "
          f"su caja; conexiones = las fijadas")
    k = rep["cajas"]
    print(f"CAJAS: {k['cajas']} (con la leyenda), sin superposiciones; separación mínima entre bordes "
          f"{k['separacion_minima']:.1f}; ningún trazo ni punta entra en una caja")
    x = rep["cruces"]
    d = x["distancia_minima"]
    print(f"CRUCES entre flechas: {x['cruces']}; contactos: 0; distancia mínima entre flechas "
          f"{d[0]:.1f} («{d[1]}» / «{d[2]}»), exigida {DISTANCIA_MIN}")
    tx = rep["textos"]
    print(f"TEXTOS: {tx['textos']}, sin superposiciones; distancias mínimas: "
          + "; ".join(f"{a} {b:.1f}" for a, b in tx["minimos"].items()))
    for fs in sorted(tx["tamanos"]):
        print(f"  letra {fs} unidades -> {tx['tamanos'][fs]:.2f} pt impresos a {ANCHO_CM:.0f} cm")
    print("RÓTULOS: distancia a su tramo / a la flecha ajena más cercana")
    for s, (gap, (da, na)) in rep["rotulos"].items():
        print(f"  «{s}»  {gap:.1f} / {da:.1f} («{na}»)")
    mg = rep["margen"]
    mm = ANCHO_CM * 10 / W
    print(f"MARGEN ({mg['elementos']} elementos): mínimo a cada borde "
          + ", ".join(f"{b} {v:.1f} u = {v * mm:.2f} mm" for b, v in mg["minimos"].items())
          + f"; exigido {MARGEN_MM:.1f} mm")
    rg = rep["registro"]
    print(f"REGISTRO: {rg['elementos']} elementos del SVG, todos registrados; colores controlados en "
          f"{rg['colores']['cajas']} cajas, {rg['colores']['muestras']} muestras y "
          f"{rg['colores']['flechas']} flechas")
    print("PRUEBAS NEGATIVAS (cada una frena en su control):")
    for n, msg in negativas.items():
        print(f"  {n:20s} {msg}")
    g = M["geo"]
    print(f"COMPOSICIÓN: ancho de pieza {g['w_pieza']}; separación en la fila de abajo {g['sep_fila2']:.2f}; "
          f"conector y=" + f(g["y_conector"]) + "; bus del catálogo y=" + f(g["y_bus"])
          + "; vuelta al extractor y=" + f(g["y_vuelta"]))

    os.makedirs(args.salida, exist_ok=True)
    rutas = {ext: os.path.join(args.salida, f"{NOMBRE}.{ext}") for ext in ("svg", "png", "pdf")}
    with open(rutas["svg"], "w", encoding="utf-8", newline="\n") as fh:
        fh.write(rep["svg"])
    try:
        exportar(rutas["svg"], rutas["png"], rutas["pdf"])
        mb = pdf_mediabox(rutas["pdf"])
    except Freno as e:
        print(f"FRENO {e}")
        return 1
    wpx, hpx = png_dimensiones(rutas["png"])
    alto = M["alto"]
    print(f"TAMAÑO: lienzo {W} × {alto}; impreso {ANCHO_CM:.2f} × {ANCHO_CM * alto / W:.2f} cm; "
          f"PNG {wpx} × {hpx} px a {DPI} dpi; PDF {mb[0]:.2f} × {mb[1]:.2f} pt "
          f"({mb[0] / PT_POR_CM:.2f} × {mb[1] / PT_POR_CM:.2f} cm)")
    for ext in ("svg", "png", "pdf"):
        print(f"{ext.upper()}: {rutas[ext]}  sha256 {sha256(rutas[ext])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
