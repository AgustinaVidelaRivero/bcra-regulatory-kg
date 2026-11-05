#!/usr/bin/env python3
"""Figura del recorrido de una respuesta por la evaluación (capítulo 5), por script y nunca a mano.

Es un diagrama sin datos de la evaluación: no lee datos, registros ni
resultados. Sigue una pregunta con el ejemplo construido que la tesis usa en
todos sus capítulos (cuándo los créditos para consumo o vivienda pasan a la
cartera comercial) y una respuesta parcial. Qué dibuja, a 15 cm de ancho:
- arriba, la pregunta y sus criterios;
- en el medio, el camino principal: el agente, la respuesta, el juez de las
  respuestas con su decisión sobre cada criterio, la regla del veredicto y el
  veredicto;
- abajo, las ramas: la traza del agente, los indicadores de las citas y su
  resultado, la lectura de la autora cuando un criterio queda en duda, y la
  atribución de la falla con su clase.

Contenido: la tabla CAJAS (una línea por caja: clase y texto) y la tabla
FLECHAS (una línea por flecha: origen, destino y rótulo). La respuesta, la
traza y las decisiones del juez son las del ejemplo construido; para poner las
de una corrida real se cambian sus líneas en CAJAS y se regenera. El texto de
cada caja se parte solo en renglones al ancho de su caja (ANCHO_TEXTO).

Formato: el del mapa de la evaluación (fig_evaluacion.py, «M» en los
comentarios), que lo toma de la figura del proceso del capítulo 4
(generar_figura_proceso.py, «P»): biblioteca estándar y rsvg-convert, la
paleta por clase, la tipografía, los cuerpos, las interlíneas, los márgenes
internos, los grosores, las esquinas, las puntas de flecha, la leyenda, el
ancho y la resolución (FORMATO, con la línea que declara cada valor). El texto
va alineado a la izquierda, como en el mapa. Los rótulos de las flechas son
los de P. Se suman dos clases: la lectura de la autora (fondo blanco y borde
del color del texto) y los resultados (gris); las dos llevan el borde 1,5
veces más grueso. Si generar_figura_proceso.py está junto a este script (o se da con
--formato), cada valor tomado de P se coteja con la línea que lo declara.

Controles (verificar(); si uno falla, no se escribe nada):
  1. contenido: las cajas dibujadas son las de CAJAS, cada una con su clase, y
     el texto dibujado de cada caja, unido, es el de CAJAS letra por letra; los
     rótulos son los de FLECHAS; ningún texto nombra un modelo;
  2. trazado: las flechas son exactamente las de FLECHAS; ningún tramo es
     diagonal ni nulo ni va hacia la izquierda; cada caja de destino tiene el
     centro a la derecha del de su origen o está debajo de él, unida por una
     flecha vertical; cada flecha sale del borde de su caja y llega al borde de
     su caja de destino, lejos de las esquinas;
  3. cajas: ninguna se superpone con otra ni con la leyenda; ningún trazo ni
     punta entra en una caja;
  4. cruces: ningún cruce, contacto ni superposición entre flechas; dos flechas
     no pasan a menos de DISTANCIA_MIN;
  5. textos: ninguno por debajo de 7 pt impresos, fuera de su caja, superpuesto
     a otro texto ni tocado por un trazo o una punta;
  6. rótulos: cada uno junto a un tramo recto de su flecha, más cerca de ella
     que de cualquier otra;
  7. margen y tamaño: nada a menos de 2 mm del borde; el alto no pasa de
     ALTO_MAX_CM;
  8. registro: el SVG se relee y cada caja, muestra y flecha tiene el color y
     el grosor de su clase.

Salida: figura_recorrido_respuesta.png (1772 px de ancho, 300 dpi grabados en
el PNG), byte a byte reproducible con el mismo rsvg-convert.

Uso (desde la raíz del repositorio):
    PYTHONDONTWRITEBYTECODE=1 python3 -B docs/tesis/figuras/fig_recorrido_respuesta.py
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
NOMBRE = "figura_recorrido_respuesta"

# ========================================================================== #
# Contenido: una línea por caja y una por flecha                             #
# ========================================================================== #
# clave: (clase, texto). Clases: «modelo» (naranja), «codigo» (azul), «datos»
# (gris), «lectura» (blanca, con el borde del color del texto y más grueso) y
# «resultado» (gris, con el borde más grueso). La barra « / » separa los renglones: el
# primero es el título (negrita) y los demás van en letra normal más chica.
CAJAS = {
    "pregunta":     ("datos",     "Pregunta / Para una entidad financiera, ¿qué condiciones hacen que los créditos para consumo o vivienda deban clasificarse en la cartera comercial?"),
    "criterios":    ("datos",     "Criterios / 1. Supera dos veces el importe de referencia / 2. El importe es el máximo de ventas anuales de la categoría Micro del sector Comercio / 3. El repago depende de la actividad del cliente"),
    "agente":       ("modelo",    "Agente / Consulta el grafo"),
    "respuesta":    ("datos",     "Respuesta / Esos créditos pasan a la cartera comercial cuando superan dos veces el importe de referencia y su repago depende de la actividad del cliente / Cita: Clasificación de deudores, 5.1.1.1"),
    "traza":        ("datos",     "Traza / Abrió el 5.1.1.1 y no siguió la remisión al 3.7"),
    "juez":         ("modelo",    "Juez de las respuestas / 1. Cumple / 2. No cumple / 3. Cumple"),
    "regla":        ("codigo",    "Regla del veredicto / Todos cumplidos, correcta / Ninguno, incorrecta / Los demás, parcial"),
    "duda":         ("lectura",   "Lectura de la autora / Pone el veredicto contra el texto oficial"),
    "veredicto":    ("resultado", "Parcial / Cumple 2 de 3 criterios"),
    "reglas_citas": ("codigo",    "Indicadores de las citas / Las citas existen / Las citas fueron consultadas / Una cita es el punto que responde"),
    "fundada":      ("resultado", "Fundada / Cumple los 3 indicadores"),
    "atribucion":   ("codigo",    "Atribución de la falla / Abrió uno de los puntos que responden"),
    "clase":        ("resultado", "Clase 4 / Lo consultó"),
}
# (origen, destino, rótulo o None)
FLECHAS = (
    ("pregunta", "agente", None),
    ("agente", "respuesta", None),
    ("agente", "traza", None),
    ("pregunta", "juez", None),
    ("criterios", "juez", None),
    ("respuesta", "juez", None),
    ("juez", "regla", None),
    ("regla", "veredicto", None),
    ("juez", "duda", "Si un criterio queda en duda"),
    ("duda", "veredicto", None),
    ("respuesta", "reglas_citas", None),
    ("traza", "reglas_citas", None),
    ("reglas_citas", "fundada", None),
    ("veredicto", "atribucion", "Si falla"),
    ("traza", "atribucion", None),
    ("atribucion", "clase", None),
)
# El camino principal: sus flechas llevan el grosor de la línea principal de
# P (GROSOR_FLUJO) y las demás, el de las entradas y las ramas (GROSOR_RAMA).
CAMINO = ("pregunta", "agente", "respuesta", "juez", "regla", "veredicto")


class Falla(Exception):
    """Un control no se cumple: la figura no se escribe."""


def falla(control: str, motivo: str):
    raise Falla(f"[{control}] {motivo}")


# ========================================================================== #
# Formato (el del mapa de la evaluación)                                     #
# ========================================================================== #
# Al lado de cada valor, la línea del mapa (M) que lo declara y, entre
# paréntesis, la de la figura del proceso (P) de la que el mapa lo toma.
W = 760                                                  # M:172 (P:163)
TIPOGRAFIA = "Helvetica,Arial,sans-serif"                # M:173 (P:164)
MODELO = {"relleno": "#fbe3d3", "borde": "#e07b39"}      # M:174 (P:165)
DETERMINISTICA = {"relleno": "#e1e7ee", "borde": "#4a5a6a"}  # M:175 (P:166)
NEUTRO = {"relleno": "#fafafa", "borde": "#999999"}      # M:176 (P:167)
TINTA, TINTA_SUB = "#1f1f1f", "#444444"                  # M:177 (P:168)
FLECHA = "#555555"                                       # M:178 (P:169)
FS_TITULO, FS_TEXTO = 14, 13                             # M:179 (P:171)
IL = {FS_TITULO: 18, FS_TEXTO: 17}                       # M:180 (P:172)
SEP_TITULO = 5                                           # M:181 (P:173)
PAD_X, PAD_Y = 9, 11                                     # M:182 (P:174)
GROSOR_CAJA = 1.6                                        # M:183 (P:175)
GROSOR_FLUJO, GROSOR_RAMA = 1.8, 1.6                     # M:184 (P:176)
RADIO = 9                                                # M:185 (P:177)
RX = 8                                                   # M:186 (P:178)
MARGEN = 12                                              # M:187 (P:180)
LEYENDA_MARCO = 'fill="white" stroke="#e2e2e2" stroke-width="1" rx="5"'  # M:188 (P:181)
MUESTRA_W, MUESTRA_H, FILA_LEY = 24, 16, 22              # M:189 (P:182)
MARCADOR_A = 'viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '   # M:190 (P:183)
MARCADOR_B = 'markerHeight="6" orient="auto"><path d="M0,0L10,5L0,10z"'  # M:191 (P:184)
ANCHO_CM = 15.0                                          # M:195 (P:311)
DPI = 300                                                # M:196 (P:313)
PT_MINIMO = 7.0                                          # M:197 (P:315)
MARGEN_MM = 2.0                                          # M:198 (P:316)
DISTANCIA_MIN = 3.0                                      # M:199 (P:319)
SEP_CAJAS = 8.0                                          # M:200 (P:320)
HOLGURA_TEXTO = 1.5                                      # M:201 (P:318)
HUECO_PUNTA = 2.0                                        # M:202 (P:324)
ASC, DESC = 0.78, 0.22                                   # M:203 (P:350)
GRUPO_LEYENDA = 10                                       # M:204 (P:420)
RX_MUESTRA = 3                                           # M:205 (P:1123)
LEJOS_ESQUINA = RX + 4                                   # M:206 (P:325)
ALTO_MAX_CM = 13.0                                       # M:217
# Los rótulos de las flechas (el mapa no tiene): los de P.
JUNTO = 8.0                                              # P:321, de un rótulo a su tramo, como máximo
AJENA = 5.0                                              # P:322, un rótulo, tanto más lejos de otra flecha
ROTULO_AIRE = 4.0                                        # P:323, del trazo al rótulo
# Las dos clases que se suman al mapa.
LECTURA = {"relleno": "#ffffff", "borde": TINTA}         # fondo blanco, borde del color del texto
GROSOR_RESULTADO = round(1.5 * GROSOR_CAJA, 1)           # 2,4: el borde del mapa, 1,5 veces (resultados y lectura)
LEYENDA = (("modelo", "Pieza que ejecuta un modelo de lenguaje"),        # M:192 (P:278)
           ("codigo", "Reglas fijas"),                                   # M:193 (P:279)
           ("datos", "Datos"),                                           # M:194 (P:280)
           ("lectura", "Lectura de la autora"),
           ("resultado", "Resultado"))
MARCADOR = MARCADOR_A + MARCADOR_B
PALETA = {"modelo": MODELO, "codigo": DETERMINISTICA, "datos": NEUTRO, "lectura": LECTURA,
          "resultado": NEUTRO}
GROSOR = {"modelo": GROSOR_CAJA, "codigo": GROSOR_CAJA, "datos": GROSOR_CAJA, "lectura": GROSOR_RESULTADO,
          "resultado": GROSOR_RESULTADO}
ESTILO_TRAZO = {"flujo": GROSOR_FLUJO, "rama": GROSOR_RAMA}
PT_POR_CM = 72.0 / 2.54                                  # M:214
ANCHO_PNG_PX = round(ANCHO_CM / 2.54 * DPI)              # M:215, 1772
MARGEN_MIN = MARGEN_MM * W / (ANCHO_CM * 10)             # M:216, 10,1 unidades

# nombre → (valor que usa la figura, línea citada, patrón de la línea en
# generar_figura_proceso.py, grupo que se compara con el valor); M:221-259.
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
    "JUNTO": (JUNTO, 321, r"^JUNTO = ([\d.]+) ", float),
    "AJENA": (AJENA, 322, r"^AJENA = ([\d.]+) ", float),
    "ROTULO_AIRE": (ROTULO_AIRE, 323, r"^ROTULO_AIRE = ([\d.]+) ", float),
    "HUECO_PUNTA": (HUECO_PUNTA, 324, r"^HUECO_PUNTA = ([\d.]+) ", float),
    "LEJOS_ESQUINA": ("RX + 4", 325, r"^LEJOS_ESQUINA = (RX \+ 4) ", str),
    "ASC, DESC": ((ASC, DESC), 350, r"^ASC, DESC = ([\d.]+, [\d.]+) ", "lit"),
    "GRUPO_LEYENDA": (GRUPO_LEYENDA, 420, r"^GRUPO_LEYENDA = (\d+)$", int),
    "RX_MUESTRA": (RX_MUESTRA, 1123, r"""^\s+f'stroke-width="\{GROSOR_CAJA\}" rx="(\d+)"/>'\)$""", int),
}


def cotejar_formato(ruta: str) -> list[str]:
    """Cada valor de FORMATO contra la línea de generar_figura_proceso.py que lo
    declara (M:262-281). Falla si un valor no coincide; si la línea cambió de
    número, lo informa."""
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
# Las tablas de M:290-306 (que son las de P:335-349 con «¿» y «?» agregados).
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
    """Un decimal fijo (M:321-323, P:567-570)."""
    return f"{v:.1f}"


# ========================================================================== #
# Texto de cada caja                                                          #
# ========================================================================== #
# Ancho del texto de cada caja (sin los márgenes internos). Medidas de esta
# figura: deciden en cuántos renglones se parte cada texto.
ANCHO_TEXTO = {
    "pregunta": 378, "criterios": 298,
    "agente": 66, "respuesta": 214, "juez": 78, "regla": 113, "veredicto": 85,
    "traza": 66, "reglas_citas": 175, "fundada": 76, "duda": 140,
    "atribucion": 100, "clase": 67,
}


def partir(palabras: list[str], wmax: float, fs: int, negrita: bool) -> list[str]:
    """Renglones de `palabras` en `wmax` (M:345-359)."""
    lineas, actual = [], ""
    for p in palabras:
        cand = p if not actual else actual + " " + p
        if ancho(cand, fs, negrita) <= wmax:
            actual = cand
            continue
        if not actual or ancho(p, fs, negrita) > wmax:
            falla("textos", f"«{p}» no entra en {wmax} junto a lo que lo precede")
        lineas.append(actual)
        actual = p
    lineas.append(actual)
    return lineas


def lineas_caja(clave: str) -> list[dict]:
    """Renglones dibujados de la caja (M:362-382): el título en FS_TITULO y
    negrita; cada renglón siguiente del texto, partido al ancho de la caja, en
    FS_TEXTO y normal, con SEP_TITULO antes del primero."""
    titulo, *resto = CAJAS[clave][1].split(" / ")
    wmax = ANCHO_TEXTO[clave]
    out = []
    for s in partir(titulo.split(), wmax, FS_TITULO, True):
        out.append({"s": s, "fs": FS_TITULO, "negrita": True, "color": TINTA, "renglon": 0,
                    "il": IL[FS_TITULO], "sep": 0})
    for j, r in enumerate(resto, start=1):
        for i, s in enumerate(partir(r.split(), wmax, FS_TEXTO, False)):
            out.append({"s": s, "fs": FS_TEXTO, "negrita": False, "color": TINTA_SUB, "renglon": j,
                        "il": IL[FS_TEXTO], "sep": SEP_TITULO if (j == 1 and i == 0) else 0})
    return out


def alto_contenido(clave: str) -> float:
    return sum(l["sep"] + l["il"] for l in lineas_caja(clave))


def ancho_caja(clave: str) -> int:
    """El ancho de una caja (M:389-391, P:383-384)."""
    return math.ceil(ANCHO_TEXTO[clave] + 2 * PAD_X + 2)


def alto_caja(clave: str) -> int:
    """El alto de una caja (M:394-396, P:387-388)."""
    return math.ceil(alto_contenido(clave) + 2 * PAD_Y)


# ========================================================================== #
# Composición                                                                 #
# ========================================================================== #
SEP_FLECHA = 20                  # M:409, entre dos cajas unidas por una flecha horizontal
SEP_VERTICAL = 20                # M:411, entre dos cajas unidas por una flecha vertical
CARRIL = 10                      # M:412, de una flecha que corre junto a una caja a la caja
SOBRE_LEYENDA = 10               # M:414, de lo de arriba a la leyenda
SEP_SIN_FLECHA = math.ceil(SEP_CAJAS + GROSOR_CAJA)  # M:416, entre dos cajas vecinas sin flecha
# Medidas de esta figura (no salen de otra figura).
SEP_ENTRADAS = 20                # entre la pregunta y los criterios
FILA_ENTRADAS = ("pregunta", "criterios")
FILA_CAMINO = ("agente", "respuesta", "juez", "regla", "veredicto")


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
    """Tramo en común de dos cajas en x o en y, lejos de las esquinas (M:446-454)."""
    if eje == "x":
        lo, hi = max(a["x"], b["x"]) + LEJOS_ESQUINA, min(der(a), der(b)) - LEJOS_ESQUINA
    else:
        lo, hi = max(a["y"], b["y"]) + LEJOS_ESQUINA, min(aba(a), aba(b)) - LEJOS_ESQUINA
    if lo > hi:
        falla("composicion", f"«{a['clave']}» y «{b['clave']}» no tienen tramo común en {eje}")
    return lo, hi


def armar() -> dict:
    """Ubica cajas, flechas, rótulos y leyenda; nada se dibuja todavía."""
    C = {}
    x_fin = W - MARGEN

    # ---- arriba: la pregunta y sus criterios ---------------------------- #
    pr = C["pregunta"] = caja("pregunta", MARGEN, MARGEN)
    cr = C["criterios"] = caja("criterios", 0, MARGEN)
    cr["x"] = x_fin - cr["w"]
    if cr["x"] < der(pr) + SEP_ENTRADAS:
        falla("composicion", "la pregunta y los criterios no entran en una fila")

    # ---- el camino principal, en una fila centrada ---------------------- #
    h_camino = max(alto_caja(k) for k in FILA_CAMINO)
    y_eje = max(aba(pr), aba(cr)) + SEP_VERTICAL + h_camino / 2.0
    x = float(MARGEN)
    for k in FILA_CAMINO:
        C[k] = caja(k, x, y_eje - alto_caja(k) / 2.0)
        x += ancho_caja(k) + SEP_FLECHA
    ag, rs, jz, rg, ve = (C[k] for k in FILA_CAMINO)
    if der(ve) > x_fin + 1e-6:
        falla("composicion", f"el camino principal llega a x={der(ve):.1f} (> {x_fin})")

    # ---- abajo: las ramas ----------------------------------------------- #
    tz = C["traza"] = caja("traza", ag["x"], aba(ag) + SEP_VERTICAL)
    ic = C["reglas_citas"] = caja("reglas_citas", der(tz) + SEP_FLECHA, aba(rs) + SEP_VERTICAL)
    fu = C["fundada"] = caja("fundada", der(ic) + SEP_FLECHA, 0)
    fu["y"] = cy(ic) - fu["h"] / 2.0
    # la lectura, tan abajo que el rótulo de su flecha, centrado en el tramo
    # vertical (P:548-549), quede a CARRIL de la regla y a RADIO del juez
    alto_rotulo = (ASC + DESC) * FS_TEXTO
    medio = max(aba(rg) + CARRIL, aba(jz) + RADIO) + alto_rotulo / 2.0
    # de la caja de al lado, SEP_CAJAS más la mitad de los dos bordes (los dos, de 2,4)
    sep_fu_du = math.ceil(SEP_CAJAS + (GROSOR[fu["clase"]] + GROSOR[CAJAS["duda"][0]]) / 2.0)
    du = C["duda"] = caja("duda", der(fu) + sep_fu_du, 2 * medio - aba(jz) + HUECO_PUNTA)
    y_dv = cy(du)                                       # la flecha de la lectura al veredicto
    at = C["atribucion"] = caja("atribucion", 0, y_dv + CARRIL)
    at["x"] = x_fin - at["w"]
    y_carril = max(aba(c) for c in (tz, ic, fu, du)) + CARRIL   # la flecha de la traza a la atribución
    if not at["y"] + LEJOS_ESQUINA <= y_carril <= aba(at) - LEJOS_ESQUINA:
        at["y"] = y_carril - at["h"] / 2.0
    cl = C["clase"] = caja("clase", 0, aba(at) + SEP_VERTICAL)
    cl["x"] = x_fin - cl["w"]

    # ---- flechas -------------------------------------------------------- #
    hp = HUECO_PUNTA
    T = []

    def flecha(desde, hasta, puntos):
        estilo = "flujo" if (desde, hasta) in zip(CAMINO, CAMINO[1:]) else "rama"
        T.append({"desde": desde, "hasta": hasta, "nombre": f"{desde} → {hasta}", "estilo": estilo,
                  "puntos": [(float(f(px)), float(f(py))) for px, py in puntos]})

    def horizontal(a, b, y=None):
        A, B = C[a], C[b]
        lo, hi = comun(A, B, "y")
        y = (lo + hi) / 2.0 if y is None else y
        if not lo <= y <= hi:
            falla("composicion", f"«{a} → {b}» en y={y:.1f} fuera de su tramo común")
        flecha(a, b, [(der(A), y), (B["x"] - hp, y)])

    def vertical(a, b, x=None):
        A, B = C[a], C[b]
        lo, hi = comun(A, B, "x")
        x = (lo + hi) / 2.0 if x is None else x
        if not lo <= x <= hi:
            falla("composicion", f"«{a} → {b}» en x={x:.1f} fuera de su tramo común")
        flecha(a, b, [(x, aba(A)), (x, B["y"] - hp)])

    # de arriba al camino principal
    vertical("pregunta", "agente")
    lo_p, hi_p = comun(pr, jz, "x")
    lo_c, hi_c = comun(cr, jz, "x")
    vertical("pregunta", "juez", (lo_p + hi_p) / 2.0)
    vertical("criterios", "juez", (lo_c + hi_c) / 2.0)
    # el camino principal
    horizontal("agente", "respuesta", y_eje)
    horizontal("respuesta", "juez", y_eje)
    horizontal("juez", "regla", y_eje)
    horizontal("regla", "veredicto", y_eje)
    # las ramas
    vertical("agente", "traza")
    vertical("respuesta", "reglas_citas")
    horizontal("traza", "reglas_citas")
    horizontal("reglas_citas", "fundada")
    x_jd = (max(jz["x"], du["x"]) + LEJOS_ESQUINA + min(der(jz), der(du)) - LEJOS_ESQUINA) / 2.0
    vertical("juez", "duda", x_jd)
    x_dv = ve["x"] + LEJOS_ESQUINA + 5                  # entra al veredicto por abajo, a la izquierda
    flecha("duda", "veredicto", [(der(du), y_dv), (x_dv, y_dv), (x_dv, aba(ve) + hp)])
    w_falla = ancho(dict(((a, b), r) for a, b, r in FLECHAS)[("veredicto", "atribucion")], FS_TEXTO, False)
    x_va = x_fin - w_falla - ROTULO_AIRE - GROSOR_RAMA / 2.0 - 2
    vertical("veredicto", "atribucion", x_va)
    x_ta = cx(tz)
    flecha("traza", "atribucion", [(x_ta, aba(tz)), (x_ta, y_carril), (at["x"] - hp, y_carril)])
    lo, hi = comun(at, cl, "x")
    vertical("atribucion", "clase", (lo + hi) / 2.0)

    # ---- rótulos, cada uno a la derecha de un tramo vertical (P:541-549) - #
    por_nombre = {t["nombre"]: t for t in T}
    R = []
    for a, b, texto in FLECHAS:
        if texto is None:
            continue
        t = por_nombre[f"{a} → {b}"]
        (ax, ay), (bx, by) = t["puntos"][0], t["puntos"][1]
        g = ESTILO_TRAZO[t["estilo"]] / 2.0
        R.append({"clave": f"{a} → {b}", "texto": texto, "flecha": t["nombre"], "tramo": 0,
                  "x": float(f(ax + g + ROTULO_AIRE)),
                  "y": float(f((ay + by) / 2.0 + (ASC - DESC) / 2.0 * FS_TEXTO))})

    # ---- leyenda, abajo a la izquierda (la de M:584-589) ---------------- #
    y_ley = y_carril + SOBRE_LEYENDA
    w_ley = 12 + MUESTRA_W + 9 + max(ancho(s, FS_TEXTO, False) for _, s in LEYENDA) + 12
    h_ley = GRUPO_LEYENDA + len(LEYENDA) * FILA_LEY + 6
    L = {"x": float(MARGEN), "y": float(f(y_ley)), "w": float(f(w_ley)), "h": float(h_ley)}
    alto = math.ceil(max(L["y"] + L["h"], max(aba(c) for c in C.values())) + MARGEN)
    return {"cajas": C, "trazos": T, "rotulos": R, "leyenda": L, "alto": alto}


# ========================================================================== #
# Elementos derivados: textos, puntas, tramos                                #
# ========================================================================== #
def bb(c: dict) -> tuple:
    return (c["x"], c["y"], c["x"] + c["w"], c["y"] + c["h"])


def textos_de(M: dict) -> list[dict]:
    """Todo texto dibujado, con su caja (o la leyenda, o su flecha) y su
    posición (M:601-626)."""
    out = []
    for clave, c in M["cajas"].items():
        yy = c["y"] + (c["h"] - alto_contenido(clave)) / 2.0
        for i, l in enumerate(lineas_caja(clave)):
            yy += l["sep"]
            base = yy + (l["il"] - l["fs"]) / 2.0 + ASC * l["fs"]
            out.append({"s": l["s"], "fs": l["fs"], "negrita": l["negrita"], "color": l["color"],
                        "x": float(f(c["x"] + PAD_X)), "y": float(f(base)), "dentro": clave,
                        "tipo": "caja", "renglon": l["renglon"], "linea": i})
            yy += l["il"]
    for r in M["rotulos"]:
        out.append({"s": r["texto"], "fs": FS_TEXTO, "negrita": False, "color": TINTA_SUB,
                    "x": r["x"], "y": r["y"], "dentro": None, "tipo": "rotulo", "flecha": r["flecha"],
                    "linea": 0})
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
    """Triángulo de la punta (marcador de 10 × 10 a 6 veces el grosor; M:648-663)."""
    lp = 6 * ESTILO_TRAZO[t["estilo"]]
    (xa, ya), (xb, yb) = t["puntos"][-2], t["puntos"][-1]
    largo = math.hypot(xb - xa, yb - ya)
    ux, uy = (xb - xa) / largo, (yb - ya) / largo
    tip = (xb + 0.1 * lp * ux, yb + 0.1 * lp * uy)
    bx, by = xb - 0.9 * lp * ux, yb - 0.9 * lp * uy
    return [(tip, (bx - 0.5 * lp * uy, by + 0.5 * lp * ux), (bx + 0.5 * lp * uy, by - 0.5 * lp * ux))]


def caja_punta(p: tuple) -> tuple:
    return (min(q[0] for q in p), min(q[1] for q in p), max(q[0] for q in p), max(q[1] for q in p))


# ========================================================================== #
# Geometría de los controles (M:673-784)                                      #
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


def llega(q0, q1, caja_destino) -> bool:
    """El tramo q0 → q1 termina a HUECO_PUNTA del borde de la caja, hacia adentro."""
    dx, dy = direccion(q0, q1)
    p = (q1[0] + HUECO_PUNTA * dx, q1[1] + HUECO_PUNTA * dy)
    lado = en_borde(p, caja_destino)
    return lado is not None and (dx, dy) == tuple(-v for v in NORMAL[lado])


# ========================================================================== #
# Controles (M:790-1036)                                                      #
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
    for clave, (_, texto) in CAJAS.items():
        ts = por_caja.pop(clave, [])
        renglones = {}
        for t in ts:
            renglones.setdefault(t["renglon"], []).append(t["s"])
        dibujado = " / ".join(" ".join(renglones[j]) for j in sorted(renglones))
        if dibujado != texto:
            falla("contenido", f"«{clave}»: dibujado «{dibujado}» ≠ CAJAS «{texto}»")
    rotulos = sorted((t["flecha"], t["s"]) for t in por_caja.pop(None, []))
    if rotulos != sorted((f"{a} → {b}", r) for a, b, r in FLECHAS if r is not None):
        falla("contenido", f"los rótulos {rotulos} no son los de FLECHAS")
    if [t["s"] for t in por_caja.pop("leyenda", [])] != [s for _, s in LEYENDA]:
        falla("contenido", "la leyenda no es la de LEYENDA")
    if por_caja:
        falla("contenido", f"textos sin caja: {sorted(por_caja)}")
    return {"textos": len(textos), "cajas": len(M["cajas"]), "rotulos": len(rotulos)}


def controlar_trazado(M: dict) -> dict:
    T, C = M["trazos"], M["cajas"]
    n_tramos, verticales = 0, []
    for t in T:
        for p, q in tramos(t):
            n_tramos += 1
            if p == q:
                falla("trazado", f"tramo nulo en «{t['nombre']}» en {p}")
            if p[0] != q[0] and p[1] != q[1]:
                falla("trazado", f"tramo diagonal en «{t['nombre']}»: {p} → {q}")
            if q[0] < p[0]:
                falla("trazado", f"«{t['nombre']}» tiene un tramo hacia la izquierda")
        for (a, b), (c, d) in zip(tramos(t), tramos(t)[1:]):
            if direccion(a, b) == tuple(-v for v in direccion(c, d)):
                falla("trazado", f"«{t['nombre']}» vuelve sobre sí misma en {b}")
        p0, p1 = t["puntos"][0], t["puntos"][1]
        lado = en_borde(p0, C[t["desde"]])
        if lado is None or direccion(p0, p1) != NORMAL[lado]:
            falla("trazado", f"«{t['nombre']}» no sale del borde de «{t['desde']}» hacia afuera ({p0})")
        if not llega(t["puntos"][-2], t["puntos"][-1], C[t["hasta"]]):
            falla("trazado", f"«{t['nombre']}» no llega al borde de «{t['hasta']}» ({t['puntos'][-1]})")
        # el destino, a la derecha del origen o debajo, unido por una flecha vertical
        if cx(C[t["hasta"]]) <= cx(C[t["desde"]]):
            if len(t["puntos"]) != 2 or direccion(p0, p1) != (0, 1):
                falla("trazado", f"«{t['nombre']}»: el destino no está a la derecha ni debajo de su origen")
            verticales.append(t["nombre"])
    dibujadas = sorted((t["desde"], t["hasta"]) for t in T)
    if dibujadas != sorted((a, b) for a, b, _ in FLECHAS):
        sobran = [c for c in dibujadas if c not in [(a, b) for a, b, _ in FLECHAS]]
        faltan = [(a, b) for a, b, _ in FLECHAS if (a, b) not in dibujadas]
        falla("trazado", f"flechas distintas de FLECHAS: sobran {sobran}; faltan {faltan}")
    return {"flechas": len(T), "tramos": n_tramos, "verticales": verticales}


def controlar_cajas(M: dict) -> dict:
    C, L = M["cajas"], M["leyenda"]
    todas = [(k, bb(c), GROSOR[c["clase"]]) for k, c in C.items()]
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
    contactos, minimo = [], (math.inf, "", "")
    for i in range(len(T)):
        for j in range(i + 1, len(T)):
            a, b = T[i], T[j]
            for p, q in tramos(a):
                for u, v in tramos(b):
                    c = contacto(p, q, u, v)
                    if c is not None:
                        contactos.append((a["nombre"], b["nombre"], c))
            d = min(dist_segmentos(p, q, u, v) for p, q in tramos(a) for u, v in tramos(b))
            d -= (ESTILO_TRAZO[a["estilo"]] + ESTILO_TRAZO[b["estilo"]]) / 2.0
            if d < minimo[0]:
                minimo = (d, a["nombre"], b["nombre"])
    if contactos:
        falla("cruces", f"cruces o contactos entre flechas: {contactos}")
    if minimo[0] < DISTANCIA_MIN:
        falla("cruces", f"«{minimo[1]}» pasa a {minimo[0]:.1f} de «{minimo[2]}» (< {DISTANCIA_MIN})")
    for t in T:
        for o in T:
            if o is t:
                continue
            for pt in puntas(t):
                for p, q in tramos(o):
                    d = dist_segmento_caja(p, q, caja_punta(pt)) - ESTILO_TRAZO[o["estilo"]] / 2.0
                    if d < HOLGURA_TEXTO:
                        falla("cruces", f"una punta de «{t['nombre']}» toca la flecha «{o['nombre']}»")
    return {"cruces": 0, "distancia_minima": minimo}


def controlar_textos(M: dict) -> dict:
    C, L = M["cajas"], M["leyenda"]
    textos = [(t, caja_texto(t)) for t in textos_de(M)]
    contenedores = {k: (bb(c), GROSOR[c["clase"]]) for k, c in C.items()}
    contenedores["leyenda"] = ((L["x"], L["y"], L["x"] + L["w"], L["y"] + L["h"]), 1.0)
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
        if t["dentro"] is not None:
            c, g = contenedores[t["dentro"]]
            holg = min(r[0] - c[0], c[2] - r[2], r[1] - c[1], c[3] - r[3])
            minimos["texto-borde de su caja"] = min(minimos["texto-borde de su caja"], holg)
            if holg < g / 2.0 + HOLGURA_TEXTO:
                falla("textos", f"«{t['s']}» a {holg:.1f} del borde de «{t['dentro']}»")
        for k, (c2, g2) in contenedores.items():
            if k != t["dentro"] and cruza(r, ampliar(c2, g2 / 2.0 + HOLGURA_TEXTO)):
                falla("textos", f"«{t['s']}» se superpone con la caja «{k}»")
        for k, m in muestras:
            if cruza(ampliar(r, HOLGURA_TEXTO), m):
                falla("textos", f"«{t['s']}» toca la muestra «{k}» de la leyenda")
        for tr in M["trazos"]:
            d = min(dist_segmento_caja(p, q, r) for p, q in tramos(tr)) - ESTILO_TRAZO[tr["estilo"]] / 2.0
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


def controlar_rotulos(M: dict) -> dict:
    """Cada rótulo junto a un tramo recto de su flecha, a no más de JUNTO, y
    más lejos de cualquier otra flecha (P:988-1015)."""
    por_nombre = {t["nombre"]: t for t in M["trazos"]}
    textos = {t["flecha"]: caja_texto(t) for t in textos_de(M) if t["tipo"] == "rotulo"}
    out = {}
    for r in M["rotulos"]:
        t = por_nombre[r["flecha"]]
        rb = textos[r["flecha"]]
        a, b = t["puntos"][r["tramo"]], t["puntos"][r["tramo"] + 1]
        g = ESTILO_TRAZO[t["estilo"]] / 2.0
        if a[1] == b[1]:
            lo, hi = sorted((a[0], b[0]))
            dentro = lo + RADIO <= rb[0] and rb[2] <= hi - RADIO
            gap = max(rb[1] - a[1], a[1] - rb[3]) - g
        else:
            lo, hi = sorted((a[1], b[1]))
            dentro = lo + RADIO <= rb[1] and rb[3] <= hi - RADIO
            gap = max(rb[0] - a[0], a[0] - rb[2]) - g
        if not dentro:
            falla("rotulos", f"«{r['texto']}» se sale del tramo recto de «{t['nombre']}»")
        if not (HOLGURA_TEXTO <= gap <= JUNTO):
            falla("rotulos", f"«{r['texto']}» a {gap:.1f} de su tramo (entre {HOLGURA_TEXTO} y {JUNTO})")
        ajena = min((min(dist_segmento_caja(p, q, rb) for p, q in tramos(o))
                     - ESTILO_TRAZO[o["estilo"]] / 2.0, o["nombre"])
                    for o in M["trazos"] if o is not t)
        if ajena[0] < gap + AJENA:
            falla("rotulos", f"«{r['texto']}» queda a {ajena[0]:.1f} de «{ajena[1]}», "
                             f"más cerca que {gap:.1f} + {AJENA}")
        out[r["texto"]] = (gap, ajena)
    return out


def controlar_margen(M: dict, textos) -> dict:
    todas = [(f"texto «{t['s']}»", r) for t, r in textos]
    todas += [(f"caja «{k}»", ampliar(bb(c), GROSOR[c["clase"]] / 2.0)) for k, c in M["cajas"].items()]
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
    rep["rotulos"] = controlar_rotulos(M)
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
    """Poligonal con esquinas redondeadas de radio RADIO (M:1046-1060, P:1060-1073)."""
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
    """El SVG (M:1063-1098)."""
    alto = M["alto"]
    alto_cm = ANCHO_CM * alto / W
    partes = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{ANCHO_CM:.2f}cm" height="{alto_cm:.2f}cm" '
        f'viewBox="0 0 {W} {alto}" font-family="{TIPOGRAFIA}">',
        f'<rect width="{W}" height="{alto}" fill="white"/>',
        f'<defs><marker id="arN" {MARCADOR} fill="{FLECHA}"/></marker></defs>',
    ]
    for clave, c in M["cajas"].items():
        pal = PALETA[c["clase"]]
        partes.append(f'<rect data-caja="{clave}" x="{f(c["x"])}" y="{f(c["y"])}" width="{f(c["w"])}" '
                      f'height="{f(c["h"])}" fill="{pal["relleno"]}" stroke="{pal["borde"]}" '
                      f'stroke-width="{GROSOR[c["clase"]]}" rx="{RX}"/>')
    for t in M["trazos"]:
        partes.append(f'<path data-flecha="{esc(t["nombre"])}" d="{path_redondeado(t["puntos"])}" fill="none" '
                      f'stroke="{FLECHA}" stroke-width="{ESTILO_TRAZO[t["estilo"]]}" marker-end="url(#arN)"/>')
    L = M["leyenda"]
    partes.append(f'<rect x="{f(L["x"])}" y="{f(L["y"])}" width="{f(L["w"])}" height="{f(L["h"])}" '
                  f'{LEYENDA_MARCO}/>')
    for m in muestras_leyenda(M):
        pal = PALETA[m["clase"]]
        partes.append(f'<rect data-caja="{m["clave"]}" x="{f(m["x"])}" y="{f(m["y"])}" width="{f(m["w"])}" '
                      f'height="{f(m["h"])}" fill="{pal["relleno"]}" stroke="{pal["borde"]}" '
                      f'stroke-width="{GROSOR[m["clase"]]}" rx="{RX_MUESTRA}"/>')
    for t in textos_de(M):
        peso = "bold" if t["negrita"] else "normal"
        partes.append(f'<text x="{f(t["x"])}" y="{f(t["y"])}" font-size="{t["fs"]}" font-weight="{peso}" '
                      f'fill="{t["color"]}">{esc(t["s"])}</text>')
    return "\n".join(partes + ["</svg>"]) + "\n"


def controlar_registro(svg: str, M: dict) -> dict:
    """El SVG se relee: cada caja, muestra de la leyenda y flecha tiene el color
    y el grosor de su clase o su estilo (M:1101-1128)."""
    raiz = ET.fromstring(svg)
    clase_de = {k: c["clase"] for k, c in M["cajas"].items()}
    clase_de.update({f"leyenda_{c}": c for c, _ in LEYENDA})
    por_nombre = {t["nombre"]: t for t in M["trazos"]}
    n = {"cajas": 0, "muestras": 0, "flechas": 0, "textos": 0}
    for el in raiz.iter():
        clave = el.get("data-caja")
        if clave is not None:
            clase = clase_de[clave]
            pal = PALETA[clase]
            esperado = (pal["relleno"], pal["borde"], str(GROSOR[clase]))
            if (el.get("fill"), el.get("stroke"), el.get("stroke-width")) != esperado:
                falla("registro", f"«{clave}» con relleno {el.get('fill')}, borde {el.get('stroke')} "
                                  f"y grosor {el.get('stroke-width')}")
            n["muestras" if clave.startswith("leyenda_") else "cajas"] += 1
        nombre = el.get("data-flecha")
        if nombre is not None:
            t = por_nombre[nombre]
            esperado = (FLECHA, str(ESTILO_TRAZO[t["estilo"]]), "url(#arN)")
            if (el.get("stroke"), el.get("stroke-width"), el.get("marker-end")) != esperado:
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
    """El PNG con el bloque pHYs (píxeles por metro) después de IHDR
    (M:1134-1151, P:1190-1211)."""
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
    """rsvg-convert al ancho de 15 cm a 300 dpi (M:1154-1162, P:1239-1246)."""
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
          f"{c['rotulos']} rótulos, los de FLECHAS; {c['textos']} textos en total; ninguno nombra un modelo")
    t = rep["trazado"]
    print(f"TRAZADO: {t['flechas']} flechas, {t['tramos']} tramos, 0 diagonales, 0 hacia la izquierda; "
          f"extremos en el borde de su caja; flechas = las de FLECHAS")
    print(f"  destino debajo del origen, con una flecha vertical: {', '.join(t['verticales'])}")
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
    for s, (gap, (da, na)) in rep["rotulos"].items():
        print(f"RÓTULO «{s}»: a {gap:.1f} de su flecha; la otra más cercana, «{na}», a {da:.1f}")
    mg = rep["margen"]
    mm = ANCHO_CM * 10 / W
    print(f"MARGEN ({mg['elementos']} elementos): mínimo a cada borde "
          + ", ".join(f"{b} {v:.1f} u = {v * mm:.2f} mm" for b, v in mg["minimos"].items())
          + f"; exigido {MARGEN_MM:.1f} mm")
    rg = rep["registro"]
    print(f"REGISTRO: color y grosor controlados en {rg['cajas']} cajas, {rg['muestras']} muestras y "
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
