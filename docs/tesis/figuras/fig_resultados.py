#!/usr/bin/env python3
"""Figura de los resultados de fidelidad (capítulo 5), por script y nunca a mano.

Dos paneles de barras de fidelidad, uno al lado del otro, a 15 cm de ancho. Cada
barra lleva su intervalo al 95 % por remuestreo de las preguntas, como barra de
error. La imagen no lleva título.
- Panel izquierdo, la medición final: «Dato directo» y «Varios puntos», con
  «Grafo», «Fragmentos, combinada» y «Fragmentos, densa».
- Panel derecho, la segunda comparación: «Agregación», «Remisión» y «Condición o
  excepción», con «Grafo con el cambio», «Grafo sin el cambio», «Fragmentos,
  combinada» y «Fragmentos, densa».

Datos: los valores se leen de los archivos de análisis con
`git --no-optional-locks show <commit>:<ruta>`, por la ruta de campos
confirmatorio.principal.por_tipo.<tipo>.por_brazo.<brazo>, y de cada brazo solo
se usan media e intervalo_95. La única tabla de cifras del script es ESPERADOS,
la del control.

Control de los valores: cada media y cada extremo del intervalo se comparan con
ESPERADOS y aprueban si difieren en TOLERANCIA o menos. El resultado va a
control_valores.md; si una barra no aprueba, el script termina con error y no
genera la figura. Los renglones de RENGLONES solo se informan: si uno no
coincide en el commit, la ruta de campos manda y el script lo dice.

Control de la composición: ninguna letra por debajo de PT_MINIMO impresos a
15 cm, ningún texto superpuesto a otro ni tocado por una barra, una barra de
error o una línea, y nada a menos de MARGEN_MM del borde. Si falla, no escribe
la figura.

Salidas: figura_resultados.svg, figura_resultados.png (1772 px de ancho, 300 dpi
grabados en el PNG) y control_valores.md, byte a byte reproducibles con el mismo
rsvg-convert. Herramientas: biblioteca estándar y rsvg-convert.

Uso (desde la raíz del repositorio):
    PYTHONDONTWRITEBYTECODE=1 python3 -B <directorio>/fig_resultados.py <commit>
Opción: --salida <directorio> (por omisión, el del script).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import shutil
import struct
import subprocess
import sys
import xml.etree.ElementTree as ET
import zlib
from decimal import Decimal

sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
NOMBRE = "figura_resultados"


class Falla(Exception):
    """Un control no se cumple: la figura no se escribe."""


def falla(control: str, motivo: str):
    raise Falla(f"[{control}] {motivo}")


# ========================================================================== #
# Formato                                                                    #
# ========================================================================== #
# E es docs/tesis/figuras/fig_evaluacion.py y T es
# docs/tesis/figuras/generar_figura_tamano_tos.py; al lado de cada valor, la
# línea que lo declara. Lo que no lleva línea es medida propia de esta figura.
W = 760                                     # E:172
TIPOGRAFIA = "Helvetica,Arial,sans-serif"   # E:173
MARGEN = 12                                 # E:187
MUESTRA_W, MUESTRA_H, FILA_LEY = 24, 16, 22  # E:189
SEP_MUESTRA = 9                             # E:586 (de la muestra a su texto)
ANCHO_CM = 15.0                             # E:195
DPI = 300                                   # E:196
MARGEN_MM = 2.0                             # E:198
ASC, DESC = 0.78, 0.22                      # E:203
PT_POR_CM = 72.0 / 2.54                     # E:214
ANCHO_PNG_PX = round(ANCHO_CM / 2.54 * DPI)  # E:215 (1772)
BASE_LEYENDA = 0.28                         # E:624 (línea de base de la leyenda)
MARGEN_MIN = MARGEN_MM * W / (ANCHO_CM * 10)  # E:216 (10,1 unidades)
AZUL, AGUAMARINA = "#2a78d6", "#1baf7a"     # T:128
PIZARRA = "#4a5a6a"                         # E:175
GRILLA = "#e1e0d9"                          # T:129
EJE = "#c3c2b7"                             # T:130
TINTA = "#1f1f1f"                           # T:132
TINTA_SUAVE = "#555555"                     # T:133
GROSOR_GRILLA, GROSOR_EJE = 0.8, 1          # T:298, T:301
BASE_MARCA = 0.36                           # T:299 (línea de base de las marcas)
SOBRE_EJE = 14                              # T:302 (título del eje sobre el tope)
SEP_MARCA = 6                               # T:299 (de la marca al eje)

# Medidas propias.
PT_MINIMO = 8.0
FS = 15                                     # todos los textos (8,39 pt impresos)
IL = 18                                     # interlínea de los rótulos de grupo
ALTO_GRAFICO = 250                          # de 0 a 1 en el eje vertical
BARRA, SEP_BARRA = 28, 2                    # ancho de barra y aire entre barras
SEP_GRUPO = 25                              # aire entre grupos
GROSOR_BARRA = 1.0                          # borde de la barra, de su color
RAYA, PASO_RAYA = 2.4, 5                    # relleno rayado, a 45 grados
GROSOR_ERROR, GROSOR_HALO = 1.4, 3.4        # barra de error y su halo blanco
TOPE_ERROR = 5                              # medio ancho del tope de la barra de error
BAJO_EJE = 20                               # del eje a la línea de base del rótulo de grupo
SOBRE_LEYENDA = 10                          # de los rótulos de grupo a la leyenda
SEP_COLUMNA = 20                            # entre columnas de la leyenda

# ========================================================================== #
# Contenido                                                                  #
# ========================================================================== #
# El mismo sistema lleva el mismo estilo en los 2 paneles. El «Grafo» del panel
# izquierdo es el mismo sistema que «Grafo sin el cambio»: comparten estilo.
ESTILOS = {
    "grafo_sin_cambio": {"color": AZUL, "relleno": "liso"},
    "grafo_con_cambio": {"color": AZUL, "relleno": "rayado"},
    "combinada": {"color": AGUAMARINA, "relleno": "liso"},
    "densa": {"color": PIZARRA, "relleno": "liso"},
}
PANELES = (
    {"clave": "final",
     "fuente": "data/experiment/banco_mcp/b63/analisis/c/analisis_B63.json",
     "grupos": (("dato_directo", ("Dato directo",)),
                ("varios_puntos", ("Varios puntos",))),
     "barras": (("kg", "Grafo", "grafo_sin_cambio"),
                ("fragmentos_hibrida", "Fragmentos, combinada", "combinada"),
                ("fragmentos_denso", "Fragmentos, densa", "densa")),
     "columnas_leyenda": 1},
    {"clave": "segunda",
     "fuente": "data/experiment/banco_mcp/b64/analisis/salidas/a/analisis/analisis_B64.json",
     "grupos": (("agregacion", ("Agregación",)),
                ("remision", ("Remisión",)),
                ("condicion_excepcion", ("Condición o", "excepción"))),
     "barras": (("kg", "Grafo con el cambio", "grafo_con_cambio"),
                ("kg_n7", "Grafo sin el cambio", "grafo_sin_cambio"),
                ("fragmentos_hibrida", "Fragmentos, combinada", "combinada"),
                ("fragmentos_denso", "Fragmentos, densa", "densa")),
     "columnas_leyenda": 2},
)
RUTA_DE_CAMPOS = ("confirmatorio", "principal", "por_tipo", "{tipo}", "por_brazo", "{brazo}")
# Renglón en el que abre cada brazo, en el commit con el que se hizo la figura.
RENGLONES = {
    ("final", "dato_directo", "kg"): 1179,
    ("final", "dato_directo", "fragmentos_hibrida"): 1172,
    ("final", "dato_directo", "fragmentos_denso"): 1165,
    ("final", "varios_puntos", "kg"): 1221,
    ("final", "varios_puntos", "fragmentos_hibrida"): 1214,
    ("final", "varios_puntos", "fragmentos_denso"): 1207,
    ("segunda", "agregacion", "kg"): 261,
    ("segunda", "agregacion", "kg_n7"): 268,
    ("segunda", "agregacion", "fragmentos_hibrida"): 254,
    ("segunda", "agregacion", "fragmentos_denso"): 247,
    ("segunda", "remision", "kg"): 359,
    ("segunda", "remision", "kg_n7"): 366,
    ("segunda", "remision", "fragmentos_hibrida"): 352,
    ("segunda", "remision", "fragmentos_denso"): 345,
    ("segunda", "condicion_excepcion", "kg"): 310,
    ("segunda", "condicion_excepcion", "kg_n7"): 317,
    ("segunda", "condicion_excepcion", "fragmentos_hibrida"): 303,
    ("segunda", "condicion_excepcion", "fragmentos_denso"): 296,
}
TOLERANCIA = Decimal("0.0005")
# Valores esperados del control, a 3 decimales: panel, brazo, tipo, media,
# extremo inferior y extremo superior del intervalo.
ESPERADOS = (
    ("final", "kg", "dato_directo", "0.949", "0.900", "0.990"),
    ("final", "kg", "varios_puntos", "0.836", "0.762", "0.902"),
    ("final", "fragmentos_hibrida", "dato_directo", "1.000", "1.000", "1.000"),
    ("final", "fragmentos_hibrida", "varios_puntos", "0.865", "0.784", "0.938"),
    ("final", "fragmentos_denso", "dato_directo", "0.957", "0.903", "1.000"),
    ("final", "fragmentos_denso", "varios_puntos", "0.848", "0.764", "0.925"),
    ("segunda", "kg", "agregacion", "0.844", "0.731", "0.941"),
    ("segunda", "kg", "remision", "0.865", "0.753", "0.956"),
    ("segunda", "kg", "condicion_excepcion", "0.729", "0.588", "0.862"),
    ("segunda", "kg_n7", "agregacion", "0.854", "0.738", "0.954"),
    ("segunda", "kg_n7", "remision", "0.792", "0.677", "0.892"),
    ("segunda", "kg_n7", "condicion_excepcion", "0.708", "0.571", "0.833"),
    ("segunda", "fragmentos_hibrida", "agregacion", "0.771", "0.642", "0.885"),
    ("segunda", "fragmentos_hibrida", "remision", "0.813", "0.696", "0.919"),
    ("segunda", "fragmentos_hibrida", "condicion_excepcion", "0.740", "0.618", "0.854"),
    ("segunda", "fragmentos_denso", "agregacion", "0.542", "0.396", "0.688"),
    ("segunda", "fragmentos_denso", "remision", "0.781", "0.653", "0.896"),
    ("segunda", "fragmentos_denso", "condicion_excepcion", "0.719", "0.581", "0.848"),
)


# ========================================================================== #
# Lectura                                                                    #
# ========================================================================== #
def texto_en_commit(commit: str, ruta: str) -> str:
    r = subprocess.run(["git", "--no-optional-locks", "show", f"{commit}:{ruta}"], capture_output=True)
    if r.returncode != 0:
        falla("lectura", f"no se pudo leer {ruta} en {commit}")
    return r.stdout.decode("utf-8")


def renglon_de(lineas: list[str], ruta: tuple) -> int | None:
    """Renglón (desde 1) en el que abre la última clave de `ruta`, en un JSON con
    una clave por renglón; None si no se encuentra. Solo se informa."""
    desde, sangria_madre = 1, 0
    for clave in ruta:
        buscado = f'"{clave}":'
        sangria_hija = None
        for i in range(desde, len(lineas)):
            linea = lineas[i]
            sangria = len(linea) - len(linea.lstrip())
            if sangria <= sangria_madre:
                return None
            if sangria_hija is None:
                sangria_hija = sangria
            if sangria == sangria_hija and linea.lstrip().startswith(buscado):
                desde, sangria_madre = i + 1, sangria
                break
        else:
            return None
    return desde


def decimal_de(v, donde: str) -> Decimal:
    if isinstance(v, bool) or not isinstance(v, (int, Decimal)):
        falla("lectura", f"{donde}: no es un número")
    return Decimal(str(v))


def leer_valores(commit: str) -> dict:
    """{(panel, tipo, brazo): {media, inf, sup, renglon}}, solo con los campos media
    e intervalo_95 de cada brazo. Los números conservan su escritura del archivo."""
    valores = {}
    for panel in PANELES:
        texto = texto_en_commit(commit, panel["fuente"])
        datos = json.loads(texto, parse_float=Decimal)
        lineas = texto.split("\n")
        for tipo, _ in panel["grupos"]:
            for brazo, _, _ in panel["barras"]:
                ruta = tuple(c.format(tipo=tipo, brazo=brazo) for c in RUTA_DE_CAMPOS)
                donde = f"{panel['clave']}, {tipo}, {brazo}"
                nodo = datos
                for clave in ruta:
                    if not isinstance(nodo, dict) or clave not in nodo:
                        falla("lectura", f"{donde}: falta el campo «{clave}»")
                    nodo = nodo[clave]
                if not isinstance(nodo, dict) or "media" not in nodo or "intervalo_95" not in nodo:
                    falla("lectura", f"{donde}: faltan media o intervalo_95")
                intervalo = nodo["intervalo_95"]
                if not isinstance(intervalo, list) or len(intervalo) != 2:
                    falla("lectura", f"{donde}: intervalo_95 no es un par")
                media = decimal_de(nodo["media"], donde)
                inf, sup = decimal_de(intervalo[0], donde), decimal_de(intervalo[1], donde)
                if not (Decimal(0) <= inf <= media <= sup <= Decimal(1)):
                    falla("lectura", f"{donde}: la media y el intervalo no están ordenados entre 0 y 1")
                valores[(panel["clave"], tipo, brazo)] = {
                    "media": media, "inf": inf, "sup": sup, "renglon": renglon_de(lineas, ruta)}
    return valores


# ========================================================================== #
# Control de los valores                                                     #
# ========================================================================== #
def con_coma(v) -> str:
    return str(v).replace(".", ",")


def controlar_valores(valores: dict, commit: str) -> tuple[str, list[str], list[str]]:
    """Texto de control_valores.md, barras que no aprueban y renglones distintos."""
    esperados = {(p, t, b): (m, i, s) for p, b, t, m, i, s in ESPERADOS}
    if set(esperados) != set(valores) or len(esperados) != len(ESPERADOS):
        falla("valores", "las barras leídas no son las de ESPERADOS")
    filas, malas, distintos = [], [], []
    for panel in PANELES:
        for brazo, sistema, _ in panel["barras"]:
            for tipo, rotulo in panel["grupos"]:
                clave = (panel["clave"], tipo, brazo)
                v = valores[clave]
                leidos = (v["media"], v["inf"], v["sup"])
                esp = tuple(Decimal(x) for x in esperados[clave])
                aprueba = all(abs(a - b) <= TOLERANCIA for a, b in zip(leidos, esp))
                nombre_tipo = " ".join(rotulo)
                if not aprueba:
                    malas.append(f"{sistema}, {nombre_tipo}")
                filas.append(
                    f"| {sistema} | {nombre_tipo} "
                    f"| {con_coma(v['media'])} [{con_coma(v['inf'])}; {con_coma(v['sup'])}] "
                    f"| {con_coma(esp[0])} [{con_coma(esp[1])}; {con_coma(esp[2])}] "
                    f"| {'aprueba' if aprueba else 'NO APRUEBA'} |")
                if v["renglon"] != RENGLONES[clave]:
                    distintos.append(f"{panel['fuente']}: {tipo}.{brazo} en el renglón {v['renglon']}, "
                                     f"no en el {RENGLONES[clave]}")
    n = len(filas)
    texto = [
        "# Control de los valores de figura_resultados", "",
        f"Commit leído: `{commit}`. Una barra aprueba si su media y los 2 extremos de su "
        f"intervalo difieren en {con_coma(TOLERANCIA)} o menos de los valores esperados.", "",
        "| Sistema | Tipo | Leído, sin redondear: media [inferior; superior] | Esperado | Resultado |",
        "|---|---|---|---|---|",
        *filas, "",
        f"Aprueban {n - len(malas)} de {n} barras.", "",
        f"Renglones: {n - len(distintos)} de {n} brazos abren en el renglón de la tabla RENGLONES; "
        "la ruta de campos es la que manda.",
    ]
    texto += [f"- Renglón distinto: {d}" for d in distintos]
    return "\n".join(texto) + "\n", malas, distintos


# ========================================================================== #
# Composición                                                                #
# ========================================================================== #
# Anchos AFM de Helvetica (/1000): la tabla de E:290-297.
_CARS = " (),-.0123456789:ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz«»ÁÉÍÑÓÚáéíñóú"
_AFM = dict(zip(_CARS, (
    278, 333, 333, 278, 333, 278, 556, 556, 556, 556, 556, 556, 556, 556, 556, 556, 278, 667,
    667, 722, 722, 667, 611, 778, 722, 278, 500, 667, 556, 833, 722, 778, 667, 778, 722, 667,
    611, 722, 667, 944, 667, 667, 611, 556, 556, 500, 556, 556, 278, 556, 556, 222, 222, 500,
    222, 833, 556, 556, 556, 556, 333, 500, 278, 556, 500, 722, 500, 500, 500, 556, 556, 667,
    667, 278, 722, 778, 722, 556, 556, 278, 556, 556, 556)))


def ancho(s: str, fs: float) -> float:
    faltan = sorted({c for c in s if c not in _AFM})
    if faltan:
        falla("textos", f"caracteres sin medida en {s!r}: {faltan}")
    return sum(_AFM[c] for c in s) * fs / 1000.0


def puntos_impresos(unidades: float) -> float:
    return unidades * ANCHO_CM * PT_POR_CM / W


def f(v: float) -> str:
    """Un decimal fijo (E:321-323)."""
    return f"{v:.1f}"


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


MARCAS_EJE = (0, 2, 4, 6, 8, 10)            # en décimas
ANCHO_MARCAS = math.ceil(ancho("0,0", FS)) + SEP_MARCA
YT = MARGEN + round(ASC * FS) + SOBRE_EJE   # el 1 del eje
YB = YT + ALTO_GRAFICO                      # el 0 del eje


def y_de(v) -> float:
    return YB - float(v) * ALTO_GRAFICO


def ancho_grupo(panel: dict) -> int:
    n = len(panel["barras"])
    return n * BARRA + (n - 1) * SEP_BARRA


def ancho_panel(panel: dict) -> int:
    return len(panel["grupos"]) * (ancho_grupo(panel) + SEP_GRUPO)


def relleno_de(estilo: dict) -> str:
    return "url(#rayado)" if estilo["relleno"] == "rayado" else estilo["color"]


def componer(valores: dict) -> tuple[str, list[dict], list[tuple], int]:
    """SVG, textos con su caja, marcas con su caja, alto del lienzo."""
    fondo, barras, errores, ejes, muestras, textos, marcas = [], [], [], [], [], [], []

    def texto(x, y, s, relleno, ancla="start", contexto=""):
        a = ancho(s, FS)
        x0 = {"start": x, "middle": x - a / 2.0, "end": x - a}[ancla]
        textos.append({"s": s, "x": x, "y": y, "relleno": relleno, "ancla": ancla, "contexto": contexto,
                       "caja": (x0, y - ASC * FS, x0 + a, y + DESC * FS)})

    x_finales = {}
    x_finales["final"] = float(MARGEN + ANCHO_MARCAS)
    x_finales["segunda"] = float(W - MARGEN - ancho_panel(PANELES[1]))
    if x_finales["final"] + ancho_panel(PANELES[0]) + ANCHO_MARCAS >= x_finales["segunda"]:
        falla("composicion", "los 2 paneles no entran en el ancho")
    y_ley = YB + BAJO_EJE + IL + DESC * FS + SOBRE_LEYENDA
    filas_max = 0

    for panel in PANELES:
        xl = x_finales[panel["clave"]]
        xr = xl + ancho_panel(panel)
        # Eje vertical: su nombre y sus marcas, con coma decimal, y la grilla.
        texto(xl - ANCHO_MARCAS, YT - SOBRE_EJE, "Fidelidad", TINTA_SUAVE, contexto="eje")
        for d in MARCAS_EJE:
            y = y_de(d / 10)
            texto(xl - SEP_MARCA, y + BASE_MARCA * FS, f"{d / 10:.1f}".replace(".", ","), TINTA_SUAVE, "end",
                  contexto="marca")
            if d:
                fondo.append(f'<path data-grilla="{d}" d="M{f(xl)},{f(y)}L{f(xr)},{f(y)}" fill="none" '
                             f'stroke="{GRILLA}" stroke-width="{GROSOR_GRILLA}"/>')
                marcas.append((f"grilla {d}", (xl, y - 0.5, xr, y + 0.5)))
        ejes.append(f'<path data-grilla="0" d="M{f(xl)},{f(YB)}L{f(xr)},{f(YB)}" fill="none" '
                    f'stroke="{EJE}" stroke-width="{GROSOR_EJE}"/>')
        marcas.append(("eje", (xl, YB - 0.5, xr, YB + 0.5)))
        # Grupos de barras y sus rótulos.
        paso = ancho_grupo(panel) + SEP_GRUPO
        for k, (tipo, rotulo) in enumerate(panel["grupos"]):
            x0 = xl + SEP_GRUPO / 2.0 + k * paso
            for j, (brazo, sistema, clave_estilo) in enumerate(panel["barras"]):
                estilo = ESTILOS[clave_estilo]
                v = valores[(panel["clave"], tipo, brazo)]
                xb = x0 + j * (BARRA + SEP_BARRA)
                ym = y_de(v["media"])
                m = GROSOR_BARRA / 2.0
                barras.append(
                    f'<rect data-panel="{panel["clave"]}" data-tipo="{tipo}" data-sistema="{esc(sistema)}" '
                    f'x="{f(xb + m)}" y="{f(ym + m)}" width="{f(BARRA - GROSOR_BARRA)}" '
                    f'height="{f(YB - ym - m)}" fill="{relleno_de(estilo)}" stroke="{estilo["color"]}" '
                    f'stroke-width="{GROSOR_BARRA}"/>')
                marcas.append((f"barra {sistema}, {tipo}", (xb, ym, xb + BARRA, YB)))
                xc = xb + BARRA / 2.0
                yi, ys = y_de(v["inf"]), y_de(v["sup"])
                d = (f"M{f(xc)},{f(yi)}L{f(xc)},{f(ys)}M{f(xc - TOPE_ERROR)},{f(ys)}L{f(xc + TOPE_ERROR)},{f(ys)}"
                     f"M{f(xc - TOPE_ERROR)},{f(yi)}L{f(xc + TOPE_ERROR)},{f(yi)}")
                errores.append(f'<path d="{d}" fill="none" stroke="white" stroke-width="{GROSOR_HALO}"/>')
                errores.append(f'<path data-panel="{panel["clave"]}" data-tipo="{tipo}" '
                               f'data-sistema="{esc(sistema)}" data-error="1" d="{d}" fill="none" '
                               f'stroke="{TINTA}" stroke-width="{GROSOR_ERROR}"/>')
                marcas.append((f"error {sistema}, {tipo}",
                               (xc - TOPE_ERROR, ys - GROSOR_HALO / 2.0, xc + TOPE_ERROR, yi + GROSOR_HALO / 2.0)))
            xg = x0 + ancho_grupo(panel) / 2.0
            for n, parte in enumerate(rotulo):
                texto(xg, YB + BAJO_EJE + n * IL, parte, TINTA, "middle", contexto="grupo")
        # Leyenda del panel, debajo del panel, en el orden de las barras.
        columnas = panel["columnas_leyenda"]
        nombres = [s for _, s, _ in panel["barras"]]
        ancho_col = [max(MUESTRA_W + SEP_MUESTRA + ancho(s, FS) for s in nombres[c::columnas])
                     for c in range(columnas)]
        for i, (_, sistema, clave_estilo) in enumerate(panel["barras"]):
            estilo = ESTILOS[clave_estilo]
            fila, col = i // columnas, i % columnas
            xm = xl + sum(ancho_col[:col]) + col * SEP_COLUMNA
            yc = y_ley + fila * FILA_LEY + FILA_LEY / 2.0
            m = GROSOR_BARRA / 2.0
            muestras.append(
                f'<rect data-muestra="{esc(sistema)}" x="{f(xm + m)}" y="{f(yc - MUESTRA_H / 2.0 + m)}" '
                f'width="{MUESTRA_W - GROSOR_BARRA:g}" height="{MUESTRA_H - GROSOR_BARRA:g}" '
                f'fill="{relleno_de(estilo)}" stroke="{estilo["color"]}" stroke-width="{GROSOR_BARRA}"/>')
            marcas.append((f"muestra {sistema}", (xm, yc - MUESTRA_H / 2.0, xm + MUESTRA_W, yc + MUESTRA_H / 2.0)))
            texto(xm + MUESTRA_W + SEP_MUESTRA, yc + BASE_LEYENDA * FS, sistema, TINTA, contexto="leyenda")
        filas_max = max(filas_max, math.ceil(len(nombres) / columnas))

    alto = math.ceil(y_ley + filas_max * FILA_LEY + MARGEN)
    alto_cm = ANCHO_CM * alto / W
    cabeza = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{ANCHO_CM:.2f}cm" height="{alto_cm:.2f}cm" '
        f'viewBox="0 0 {W} {alto}" font-family="{TIPOGRAFIA}">',
        f'<rect width="{W}" height="{alto}" fill="white"/>',
        f'<defs><pattern id="rayado" patternUnits="userSpaceOnUse" width="{PASO_RAYA}" height="{PASO_RAYA}" '
        f'patternTransform="rotate(45)"><rect width="{PASO_RAYA}" height="{PASO_RAYA}" fill="white"/>'
        f'<rect width="{RAYA}" height="{PASO_RAYA}" fill="{AZUL}"/></pattern></defs>',
    ]
    letras = []
    for t in textos:
        a = f' text-anchor="{t["ancla"]}"' if t["ancla"] != "start" else ""
        letras.append(f'<text x="{f(t["x"])}" y="{f(t["y"])}" font-size="{FS}" font-weight="normal" '
                      f'fill="{t["relleno"]}"{a}>{esc(t["s"])}</text>')
    svg = "\n".join(cabeza + fondo + barras + ejes + errores + muestras + letras + ["</svg>"]) + "\n"
    return svg, textos, marcas, alto


# ========================================================================== #
# Control de la composición                                                  #
# ========================================================================== #
def cruza(a, b) -> bool:
    return a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]


def controlar_composicion(svg: str, textos: list[dict], marcas: list[tuple], alto: int) -> dict:
    ET.fromstring(svg)
    pt = puntos_impresos(FS)
    if pt < PT_MINIMO:
        falla("letra", f"{FS} unidades son {pt:.2f} pt, menos que {PT_MINIMO}")
    for i, a in enumerate(textos):
        for b in textos[i + 1:]:
            if cruza(a["caja"], b["caja"]):
                falla("textos", f"«{a['s']}» se superpone con «{b['s']}»")
        for nombre, m in marcas:
            if cruza(a["caja"], m):
                falla("textos", f"«{a['s']}» lo toca {nombre}")
    cajas = [t["caja"] for t in textos] + [m for _, m in marcas]
    minimos = {"izquierdo": min(c[0] for c in cajas), "superior": min(c[1] for c in cajas),
               "derecho": W - max(c[2] for c in cajas), "inferior": alto - max(c[3] for c in cajas)}
    for borde, d in minimos.items():
        if d < MARGEN_MIN:
            falla("margen", f"algo queda a {d:.1f} unidades del borde {borde} (mínimo {MARGEN_MIN:.1f})")
    return {"pt": pt, "textos": len(textos), "marcas": len(marcas), "minimos": minimos}


# ========================================================================== #
# Exportación                                                                #
# ========================================================================== #
def con_densidad(png: bytes, dpi: int) -> bytes:
    """El PNG con el bloque pHYs (píxeles por metro) después de IHDR (E:1134-1151)."""
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
        falla("exportacion", "rsvg-convert no está instalado: no se escribe la figura")
    r = subprocess.run([rsvg, "-w", str(ANCHO_PNG_PX), "-f", "png"], input=svg.encode("utf-8"),
                       capture_output=True)
    if r.returncode != 0:
        falla("exportacion", r.stderr.decode("utf-8", "replace"))
    return con_densidad(r.stdout, DPI)


# ========================================================================== #
# Principal                                                                  #
# ========================================================================== #
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("commit", help="commit del que se leen los archivos de análisis")
    ap.add_argument("--salida", default=AQUI, help="directorio de las salidas (por omisión, el del script)")
    args = ap.parse_args()
    try:
        valores = leer_valores(args.commit)
        control, malas, distintos = controlar_valores(valores, args.commit)
        os.makedirs(args.salida, exist_ok=True)
        with open(os.path.join(args.salida, "control_valores.md"), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(control)
        print(f"VALORES: aprueban {len(valores) - len(malas)} de {len(valores)} barras (control_valores.md)")
        print(f"RENGLONES: {len(valores) - len(distintos)} de {len(valores)} en el renglón de RENGLONES; "
              "la ruta de campos manda")
        for d in distintos:
            print(f"  renglón distinto: {d}")
        if malas:
            for m in malas:
                print(f"  no aprueba: {m}")
            falla("valores", f"{len(malas)} barras no aprueban: no se genera la figura")
        svg, textos, marcas, alto = componer(valores)
        rep = controlar_composicion(svg, textos, marcas, alto)
        png = exportar(svg)
    except Falla as e:
        print(f"ALTO {e}")
        return 1

    mm = ANCHO_CM * 10 / W
    print(f"COMPOSICIÓN: {rep['textos']} textos y {rep['marcas']} marcas, sin superposiciones; letra {FS} unidades = "
          f"{rep['pt']:.2f} pt impresos a {ANCHO_CM:.0f} cm (mínimo {PT_MINIMO:.0f})")
    print("MARGEN: " + ", ".join(f"{b} {v:.1f} u = {v * mm:.2f} mm" for b, v in rep["minimos"].items())
          + f"; exigido {MARGEN_MM:.1f} mm")
    ruta_svg = os.path.join(args.salida, f"{NOMBRE}.svg")
    ruta_png = os.path.join(args.salida, f"{NOMBRE}.png")
    with open(ruta_svg, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(svg)
    with open(ruta_png, "wb") as fh:
        fh.write(png)
    wpx, hpx = struct.unpack(">II", png[16:24])
    print(f"TAMAÑO: lienzo {W} × {alto}; impreso {ANCHO_CM:.2f} × {ANCHO_CM * alto / W:.2f} cm; "
          f"PNG {wpx} × {hpx} px a {DPI} dpi")
    print(f"SVG: sha256 {hashlib.sha256(svg.encode('utf-8')).hexdigest()}")
    print(f"PNG: sha256 {hashlib.sha256(png).hexdigest()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
