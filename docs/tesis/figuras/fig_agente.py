#!/usr/bin/env python3
"""Figura del agente de la evaluación y de los 2 servidores de herramientas
que puede consultar, por script y nunca a mano.

Es un diagrama del método: no lee datos, registros ni resultados, ni ningún
archivo; usa solo las constantes de este script. Qué dibuja, a 15 cm de ancho
y de izquierda a derecha:
- el pedido, que llega al agente;
- el agente, del alto de los 2 servidores;
- el servidor de los fragmentos arriba y el del grafo abajo, unidos al agente
  por flechas de doble punta (las llamadas), con su fuente de datos a la misma
  altura y, entre las 2 fuentes, la traza que guarda el servidor; debajo del
  servidor del grafo, la anotación del ejemplo del préstamo;
- arriba a la derecha, la respuesta del agente, a la que se llega por encima
  de los servidores.

Contenido: la tabla CAJAS (una línea por caja: clase, título y texto), la
tabla FLECHAS (una línea por flecha) y los 3 textos sin caja (ROTULO_LLAMADAS,
ROTULO_SERVIDORES y ANOTACION). El texto se parte solo en renglones al ancho
de su caja (ANCHO_TEXTO).

Formato: el de la figura de la comparación (fig_comparacion.py, sha256
1b75dd15c61dc769524f6c2ec508b4a0061f697d897b35a8f44f07cec9247511), copiado sin
cambios: paleta por clase, tipografía, cuerpos, interlíneas, márgenes internos,
grosores, esquinas, puntas de flecha, leyenda, ancho y resolución. Al lado de
cada valor, la línea que lo declara en ese script (C:<línea>). Agregados de
esta figura: los anchos AFM de «|» y «_», que la tabla de la comparación no
trae, y la punta del comienzo de las flechas de doble punta, espejo de la del
final. La comparación no usa letra monoespaciada: ver_remisiones va en la
normal.

Controles (verificar(); si uno falla, no se escribe nada):
  1. contenido: las cajas dibujadas son las de CAJAS, cada una con su clase, y
     su título y su texto dibujados, unidos, son los de CAJAS letra por letra;
     los textos sin caja y la leyenda, también;
  2. disposición: las columnas van de izquierda a derecha; los 2 servidores,
     uno arriba del otro; cada fuente de datos, a la altura de su servidor;
     «llamadas» sobre su flecha, «Un servidor por corrida» entre las 2 flechas
     del agente a los servidores y la anotación debajo del servidor del grafo;
  3. trazado: las flechas son exactamente las de FLECHAS, con sus puntas;
     ningún tramo es diagonal, nulo ni va hacia la izquierda; cada flecha sale
     del borde de su caja y llega al borde de la de destino, lejos de las
     esquinas;
  4. cajas: ninguna se superpone con otra ni con la leyenda; ningún trazo ni
     punta entra en una caja;
  5. cruces: ninguno entre flechas, ni contactos; dos flechas no pasan a menos
     de DISTANCIA_MIN; ninguna punta toca otra flecha;
  6. textos: ninguno con letra menor que FS_TEXTO, fuera de su caja (o, si no
     tiene caja, dentro de una), superpuesto a otro texto ni tocado por un
     trazo o una punta;
  7. margen: nada a menos de 2 mm del borde;
  8. registro: el SVG se relee y cada caja, muestra y flecha tiene el color,
     el grosor y las puntas de su clase;
  9. imagen: el PNG mide ANCHO_PNG_PX de ancho y graba DPI.

Salida: figura_agente.png, junto al script (1772 px de ancho, 300 dpi grabados
en el PNG), con rsvg-convert.

Uso: PYTHONDONTWRITEBYTECODE=1 python3 -B fig_agente.py
"""

from __future__ import annotations

import hashlib
import math
import os
import shutil
import struct
import subprocess
import sys
import xml.etree.ElementTree as ET
import zlib

sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
NOMBRE = "figura_agente"

# ========================================================================== #
# Contenido: una línea por caja y una por flecha                             #
# ========================================================================== #
# clave: (clase, título, texto). Clases: «modelo» (naranja), «codigo» (azul,
# reglas fijas) y «datos» (gris). El título va en negrita; el texto, debajo,
# en letra normal y gris.
CAJAS = {
    "pedido":     ("datos",  "El pedido", "La plantilla, igual para los 2 sistemas, con la pregunta, el tope de 30 llamadas y el bloque de las herramientas del servidor"),
    "agente":     ("modelo", "Agente", "Claude Sonnet 5 en Claude Code, con sus herramientas propias apagadas"),
    "srv_grafo":  ("codigo", "Servidor del grafo", "3 herramientas sobre los nodos y 7 de navegación por los puntos"),
    "srv_frag":   ("codigo", "Servidor de los fragmentos", "Una herramienta, que devuelve los 5 fragmentos más afines, en 2 configuraciones, la combinada y la densa"),
    "grafo":      ("datos",  "El grafo evaluado", "El sellado, en Neo4j"),
    "fragmentos": ("datos",  "Los fragmentos", "Todas las unidades de extracción, también las apartadas"),
    "respuesta":  ("datos",  "La respuesta", "El texto, las citas con su documento y su punto, y si encontró con qué responder"),
    "traza":      ("datos",  "La traza", "Cada llamada, con su entrada y su salida, que guarda el servidor"),
}
# (origen, destino, puntas): 1, solo al final; 2, en los dos extremos.
FLECHAS = (
    ("pedido", "agente", 1),
    ("agente", "srv_grafo", 2),
    ("agente", "srv_frag", 2),
    ("srv_grafo", "grafo", 2),
    ("srv_frag", "fragmentos", 2),
    ("agente", "respuesta", 1),
    ("srv_grafo", "traza", 1),
    ("srv_frag", "traza", 1),
)
# Textos sin caja, en el gris del texto de las cajas.
ROTULO_LLAMADAS = "llamadas"                    # sobre la flecha agente ↔ servidor de los fragmentos
FLECHA_LLAMADAS = ("agente", "srv_frag")
ROTULO_SERVIDORES = "Un servidor por corrida"   # entre las 2 flechas del agente a los servidores
ANOTACION = "En el ejemplo del préstamo, ver_remisiones lleva del 5.1.1.1 al 3.7"  # debajo del servidor del grafo


class Falla(Exception):
    """Un control no se cumple: la figura no se escribe."""


def falla(control: str, motivo: str):
    raise Falla(f"[{control}] {motivo}")


# ========================================================================== #
# Formato (el de la figura de la comparación, sin cambios)                   #
# ========================================================================== #
# C es fig_comparacion.py (sha256 1b75dd15…9247511); al lado de cada valor, la
# línea que lo declara en C.
W = 760                                                  # C:136
TIPOGRAFIA = "Helvetica,Arial,sans-serif"                # C:137
MODELO = {"relleno": "#fbe3d3", "borde": "#e07b39"}      # C:138
DETERMINISTICA = {"relleno": "#e1e7ee", "borde": "#4a5a6a"}  # C:139
NEUTRO = {"relleno": "#fafafa", "borde": "#999999"}      # C:140
TINTA, TINTA_SUB = "#1f1f1f", "#444444"                  # C:141
FLECHA = "#555555"                                       # C:142
FS_TITULO, FS_TEXTO = 14, 13                             # C:143
IL = {FS_TITULO: 18, FS_TEXTO: 17}                       # C:144
SEP_TITULO = 5                                           # C:145
PAD_X, PAD_Y = 9, 11                                     # C:146
GROSOR_CAJA = 1.6                                        # C:147
GROSOR_FLUJO = 1.8                                       # C:148 (GROSOR_FLUJO, GROSOR_RAMA = 1.8, 1.6)
RADIO = 9                                                # C:149
RX = 8                                                   # C:150
MARGEN = 12                                              # C:151
LEYENDA_MARCO = 'fill="white" stroke="#e2e2e2" stroke-width="1" rx="5"'  # C:152
MUESTRA_W, MUESTRA_H, FILA_LEY = 24, 16, 22              # C:153
MARCADOR_A = 'viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '   # C:154
MARCADOR_B = 'markerHeight="6" orient="auto"><path d="M0,0L10,5L0,10z"'  # C:155
LEYENDA = (("modelo", "Pieza que ejecuta un modelo de lenguaje"),        # C:156
           ("codigo", "Reglas fijas"),                                   # C:157
           ("datos", "Datos"))                                           # C:158
ANCHO_CM = 15.0                                          # C:160
DPI = 300                                                # C:161
PT_MINIMO = 7.0                                          # C:162
MARGEN_MM = 2.0                                          # C:163
DISTANCIA_MIN = 3.0                                      # C:164
SEP_CAJAS = 8.0                                          # C:165
HOLGURA_TEXTO = 1.5                                      # C:166
HUECO_PUNTA = 2.0                                        # C:167
ASC, DESC = 0.78, 0.22                                   # C:168
GRUPO_LEYENDA = 10                                       # C:169
RX_MUESTRA = 3                                           # C:170
LEJOS_ESQUINA = RX + 4                                   # C:171
MARCADOR = MARCADOR_A + MARCADOR_B                       # C:172
PALETA = {"modelo": MODELO, "codigo": DETERMINISTICA, "datos": NEUTRO}  # C:173, sin «resultado»
PT_POR_CM = 72.0 / 2.54                                  # C:175
ANCHO_PNG_PX = round(ANCHO_CM / 2.54 * DPI)              # C:176; 1772
MARGEN_MIN = MARGEN_MM * W / (ANCHO_CM * 10)             # C:177; 10,1 unidades
SEP_FLECHA = 20                                          # C:353
SOBRE_LEYENDA = 10                                       # C:355
SEP_SIN_FLECHA = math.ceil(SEP_CAJAS + GROSOR_CAJA)      # C:356
FS_MINIMO = FS_TEXTO
# Agregado: la punta del comienzo de las flechas de doble punta, espejo de
# MARCADOR (el triángulo apunta hacia atrás y su vértice queda a 1 unidad del
# comienzo, como el de MARCADOR queda a 1 unidad del final).
MARCADOR_INICIO = ('viewBox="0 0 10 10" refX="1" refY="5" markerWidth="6" '
                   'markerHeight="6" orient="auto"><path d="M10,0L0,5L10,10z"')

# ========================================================================== #
# Métrica de texto: anchos AFM de Helvetica y Helvetica-Bold (/1000)         #
# ========================================================================== #
# Las tablas de C:256-270.
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
# Agregados de esta figura: «|» (bar) y «_» (underscore), con los anchos de las
# tablas AFM de Helvetica (260 y 556) y Helvetica-Bold (280 y 556).
_AFM[False].update({"|": 260, "_": 556})
_AFM[True].update({"|": 280, "_": 556})


def ancho(s: str, fs: float, negrita: bool) -> float:
    tabla = _AFM[negrita]
    faltan = sorted({c for c in s if c not in tabla})
    if faltan:
        falla("textos", f"caracteres sin medida AFM en {s!r}: {faltan}")
    return sum(tabla[c] for c in s) * fs / 1000.0


def puntos_impresos(unidades: float) -> float:
    return unidades * ANCHO_CM * PT_POR_CM / W


def f(v: float) -> str:
    """Un decimal fijo."""
    return f"{v:.1f}"


# ========================================================================== #
# Medidas de esta figura                                                      #
# ========================================================================== #
# Ancho del texto de cada caja (sin los márgenes internos): decide en cuántos
# renglones se parte cada texto.
ANCHO_TEXTO = {
    "pedido": 84,
    "agente": 97,
    "srv_grafo": 114, "srv_frag": 114,
    "grafo": 117, "traza": 117, "fragmentos": 117,
    "respuesta": 87,
}
# Las columnas, de izquierda a derecha, y lo que va entre cada una y la
# siguiente. Entre el agente y los servidores va el hueco de los rótulos: lo
# que sobra del ancho (None). Entre cada servidor y su fuente, una flecha de
# doble punta, que necesita lugar para las 2 puntas y un tramo entre ellas.
# Entre las fuentes y la respuesta no pasa ninguna flecha.
SEP_DOBLE = 32
COLUMNAS = (("pedido",), ("agente",), ("srv_frag", "srv_grafo"),
            ("fragmentos", "traza", "grafo"), ("respuesta",))
SEPARACIONES = (SEP_FLECHA, None, SEP_DOBLE, SEP_SIN_FLECHA)
# Los servidores, de arriba abajo, cada uno con su fuente de datos. El del
# grafo va abajo para que su anotación quede debajo de él, lejos del rótulo
# «Un servidor por corrida», que va entre los 2.
ARRIBA, ABAJO = ("srv_frag", "fragmentos"), ("srv_grafo", "grafo")
PUENTE = 2           # del margen al tramo de arriba de la flecha a la respuesta
SUBIDA = 28          # de ese tramo a la fila de arriba
BAJADA = 22          # de la vuelta de cada flecha a la traza hasta su caja
LIBRE = 14           # de un tramo horizontal a la caja que pasa por encima o por debajo
SEP_ANOTACION = 8    # del servidor del grafo a su anotación
SOBRE_FLECHA = 7     # del rótulo «llamadas» a su flecha
LADO_ROTULO = 4      # margen a cada lado de los rótulos del hueco


def partir(palabras: list[str], wmax: float, fs: int, negrita: bool) -> list[str]:
    """Renglones de `palabras` en `wmax`."""
    lineas, actual = [], ""
    for p in palabras:
        cand = p if not actual else actual + " " + p
        if ancho(cand, fs, negrita) <= wmax:
            actual = cand
            continue
        if not actual or ancho(p, fs, negrita) > wmax:
            falla("textos", f"«{p}» no entra en {wmax}")
        lineas.append(actual)
        actual = p
    lineas.append(actual)
    return lineas


def lineas_caja(clave: str) -> list[dict]:
    """Renglones de la caja: el título en negrita y, debajo, el texto en gris."""
    _, titulo, texto = CAJAS[clave]
    wmax = ANCHO_TEXTO[clave]
    out = [{"s": s, "fs": FS_TITULO, "negrita": True, "color": TINTA, "tipo": "titulo",
            "il": IL[FS_TITULO], "sep": 0} for s in partir(titulo.split(), wmax, FS_TITULO, True)]
    for i, s in enumerate(partir(texto.split(), wmax, FS_TEXTO, False)):
        out.append({"s": s, "fs": FS_TEXTO, "negrita": False, "color": TINTA_SUB, "tipo": "texto",
                    "il": IL[FS_TEXTO], "sep": SEP_TITULO if i == 0 else 0})
    return out


def alto_contenido(clave: str) -> float:
    return sum(l["sep"] + l["il"] for l in lineas_caja(clave))


def ancho_caja(clave: str) -> int:
    return math.ceil(ANCHO_TEXTO[clave] + 2 * PAD_X + 2)


def alto_caja(clave: str) -> int:
    return math.ceil(alto_contenido(clave) + 2 * PAD_Y)


def base_renglon(y_arriba: float, fs: int) -> float:
    """Línea de base de un renglón que empieza en y_arriba, con su interlínea."""
    return y_arriba + (IL[fs] - fs) / 2.0 + ASC * fs


# ========================================================================== #
# Composición                                                                 #
# ========================================================================== #
def caja(clave: str, x: float, y: float, alto: float | None = None) -> dict:
    return {"clave": clave, "x": float(f(x)), "y": float(f(y)), "w": float(ancho_caja(clave)),
            "h": float(alto_caja(clave) if alto is None else alto), "clase": CAJAS[clave][0]}


def der(c):
    return c["x"] + c["w"]


def aba(c):
    return c["y"] + c["h"]


def cx(c):
    return c["x"] + c["w"] / 2.0


def cy(c):
    return c["y"] + c["h"] / 2.0


def ancho_leyenda() -> float:
    """El ancho de la leyenda de C."""
    return 12 + MUESTRA_W + 9 + max(ancho(s, FS_TEXTO, False) for _, s in LEYENDA) + 12


def armar() -> dict:
    """Ubica cajas, flechas, textos sin caja y leyenda; nada se dibuja todavía."""
    anchos = [max(ancho_caja(k) for k in col) for col in COLUMNAS]
    hueco = W - 2 * MARGEN - sum(anchos) - sum(s for s in SEPARACIONES if s is not None)
    xs, x = [], float(MARGEN)
    for a, s in zip(anchos, SEPARACIONES + (0,)):
        xs.append(x)
        x += a + (hueco if s is None else s)
    yb = float(MARGEN + PUENTE)
    y1 = yb + SUBIDA
    lineas_serv = partir(ROTULO_SERVIDORES.split(), hueco - 2 * LADO_ROTULO, FS_TEXTO, False)
    if ancho(ROTULO_LLAMADAS, FS_TEXTO, False) > hueco - 2 * LADO_ROTULO:
        falla("composicion", f"«{ROTULO_LLAMADAS}» no entra en el hueco de {hueco:.1f}")

    # ---- fila de arriba: el servidor de arriba, su fuente (alineada arriba)
    # y la respuesta ------------------------------------------------------ #
    C = {}
    s1 = C[ARRIBA[0]] = caja(ARRIBA[0], xs[2], y1)
    f1 = C[ARRIBA[1]] = caja(ARRIBA[1], xs[3], y1)
    rs = C["respuesta"] = caja("respuesta", xs[4], y1)

    # ---- la traza, debajo de esa fuente: la flecha del servidor de arriba
    # pasa por debajo de la fuente y baja a la traza ---------------------- #
    yt1 = aba(f1) + LIBRE
    if yt1 > aba(s1) - LEJOS_ESQUINA:
        falla("composicion", f"no queda tramo libre de «{ARRIBA[0]}» a la traza")
    tr = C["traza"] = caja("traza", xs[3], yt1 + BAJADA)

    # ---- el servidor de abajo y su fuente (alineada abajo): la flecha del
    # servidor pasa por encima de la fuente y sube a la traza ------------- #
    h2, hf = alto_caja(ABAJO[0]), alto_caja(ABAJO[1])
    d2 = h2 - hf - LIBRE               # de la parte de arriba del servidor a su flecha
    if d2 < LEJOS_ESQUINA:
        falla("composicion", f"no queda tramo libre de «{ABAJO[0]}» a la traza")
    yt2 = aba(tr) + BAJADA
    s2 = C[ABAJO[0]] = caja(ABAJO[0], xs[2], yt2 - d2)
    f2 = C[ABAJO[1]] = caja(ABAJO[1], xs[3], aba(s2) - hf)

    # ---- el agente, del alto de los servidores; el pedido, a su altura -- #
    ag = C["agente"] = caja("agente", xs[1], y1, alto=aba(s2) - y1)
    pe = C["pedido"] = caja("pedido", xs[0], cy(ag) - alto_caja("pedido") / 2.0)

    # ---- la anotación, debajo del servidor del grafo ------------------- #
    sg = C["srv_grafo"]
    lineas_an = partir(ANOTACION.split(), sg["w"], FS_TEXTO, False)
    y_an = aba(sg) + SEP_ANOTACION

    # ---- textos sin caja ------------------------------------------------ #
    L = []

    def libre(s, x, base, tipo, i):
        L.append({"s": s, "fs": FS_TEXTO, "negrita": False, "color": TINTA_SUB, "x": float(f(x)),
                  "y": float(f(base)), "dentro": None, "tipo": tipo, "linea": i})

    s_ll = C[FLECHA_LLAMADAS[1]]
    w_ll = ancho(ROTULO_LLAMADAS, FS_TEXTO, False)
    libre(ROTULO_LLAMADAS, der(ag) + (hueco - w_ll) / 2.0,
          cy(s_ll) - GROSOR_FLUJO / 2.0 - SOBRE_FLECHA - DESC * FS_TEXTO, "llamadas", 0)
    y_serv = (cy(s1) + cy(s2)) / 2.0 - len(lineas_serv) * IL[FS_TEXTO] / 2.0
    for i, s in enumerate(lineas_serv):
        libre(s, der(ag) + (hueco - ancho(s, FS_TEXTO, False)) / 2.0,
              base_renglon(y_serv + i * IL[FS_TEXTO], FS_TEXTO), "servidores", i)
    for i, s in enumerate(lineas_an):
        libre(s, sg["x"], base_renglon(y_an + i * IL[FS_TEXTO], FS_TEXTO), "anotacion", i)

    # ---- flechas -------------------------------------------------------- #
    hp = HUECO_PUNTA
    T = []

    def flecha(desde, hasta, puntos, n_puntas=1):
        T.append({"desde": desde, "hasta": hasta, "puntas": n_puntas, "nombre": f"{desde} → {hasta}",
                  "puntos": [(float(f(px)), float(f(py))) for px, py in puntos]})

    flecha("pedido", "agente", [(der(pe), cy(ag)), (ag["x"] - hp, cy(ag))])
    # el agente con cada servidor y cada servidor con su fuente, de ida y vuelta
    for s, fu in ((s1, f1), (s2, f2)):
        flecha("agente", s["clave"], [(der(ag) + hp, cy(s)), (s["x"] - hp, cy(s))], 2)
        flecha(s["clave"], fu["clave"], [(der(s) + hp, cy(fu)), (fu["x"] - hp, cy(fu))], 2)
    # el agente a la respuesta, por encima de los servidores y sus fuentes
    flecha("agente", "respuesta", [(cx(ag), ag["y"]), (cx(ag), yb), (cx(rs), yb), (cx(rs), rs["y"] - hp)])
    # cada servidor a la traza, que está entre las 2 fuentes
    flecha(s1["clave"], "traza", [(der(s1), yt1), (cx(tr), yt1), (cx(tr), tr["y"] - hp)])
    flecha(s2["clave"], "traza", [(der(s2), yt2), (cx(tr), yt2), (cx(tr), aba(tr) + hp)])
    orden = [(d, h) for d, h, _ in FLECHAS]
    T.sort(key=lambda t: orden.index((t["desde"], t["hasta"])) if (t["desde"], t["hasta"]) in orden else -1)

    # ---- leyenda, abajo a la izquierda, debajo de lo que tiene encima --- #
    w_ley = ancho_leyenda()
    limite = MARGEN + w_ley + SEP_CAJAS
    encima = [aba(c) for c in C.values() if c["x"] < limite]
    encima += [t["y"] + DESC * t["fs"] for t in L if t["x"] < limite]
    y_ley = max(encima) + SOBRE_LEYENDA
    h_ley = GRUPO_LEYENDA + len(LEYENDA) * FILA_LEY + 6
    Ly = {"x": float(MARGEN), "y": float(f(y_ley)), "w": float(f(w_ley)), "h": float(h_ley)}
    alto = math.ceil(max([Ly["y"] + Ly["h"]] + [aba(c) for c in C.values()]
                         + [t["y"] + DESC * t["fs"] for t in L]) + MARGEN)
    return {"cajas": C, "trazos": T, "libres": L, "leyenda": Ly, "alto": alto, "hueco": hueco,
            "xs": xs, "y_puente": yb}


# ========================================================================== #
# Elementos derivados: textos, puntas, tramos                                 #
# ========================================================================== #
def bb(c: dict) -> tuple:
    return (c["x"], c["y"], c["x"] + c["w"], c["y"] + c["h"])


def textos_de(M: dict) -> list[dict]:
    """Todo texto dibujado, con su caja (la leyenda, o ninguna) y su posición."""
    out = []
    for clave, c in M["cajas"].items():
        yy = c["y"] + (c["h"] - alto_contenido(clave)) / 2.0
        for i, l in enumerate(lineas_caja(clave)):
            yy += l["sep"]
            base = yy + (l["il"] - l["fs"]) / 2.0 + ASC * l["fs"]
            out.append({"s": l["s"], "fs": l["fs"], "negrita": l["negrita"], "color": l["color"],
                        "x": float(f(c["x"] + PAD_X)), "y": float(f(base)),
                        "dentro": clave, "tipo": l["tipo"], "linea": i})
            yy += l["il"]
    out.extend(M["libres"])
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


def _triangulo(origen, sentido, adelante, atras):
    """Triángulo de una punta: el vértice a `adelante` de `origen` en `sentido`
    y la base a `atras` en sentido contrario, de ancho 6 veces el grosor."""
    lp = 6 * GROSOR_FLUJO
    ux, uy = sentido
    tip = (origen[0] + adelante * lp * ux, origen[1] + adelante * lp * uy)
    bx, by = origen[0] - atras * lp * ux, origen[1] - atras * lp * uy
    return (tip, (bx - 0.5 * lp * uy, by + 0.5 * lp * ux), (bx + 0.5 * lp * uy, by - 0.5 * lp * ux))


def _unitario(a, b):
    largo = math.hypot(b[0] - a[0], b[1] - a[1])
    return ((b[0] - a[0]) / largo, (b[1] - a[1]) / largo)


def puntas(t: dict) -> list[tuple]:
    """La punta del final (marcador de 10 × 10 a 6 veces el grosor, vértice a 1
    unidad del final) y, si la flecha es de doble punta, la del comienzo."""
    (xa, ya), (xb, yb) = t["puntos"][-2], t["puntos"][-1]
    out = [_triangulo((xb, yb), _unitario((xa, ya), (xb, yb)), 0.1, 0.9)]
    if t["puntas"] == 2:
        p0, p1 = t["puntos"][0], t["puntos"][1]
        ux, uy = _unitario(p0, p1)
        out.append(_triangulo(p0, (-ux, -uy), 0.1, 0.9))
    return out


def caja_punta(p: tuple) -> tuple:
    return (min(q[0] for q in p), min(q[1] for q in p), max(q[0] for q in p), max(q[1] for q in p))


# ========================================================================== #
# Geometría de los controles                                                  #
# ========================================================================== #
def cruza(a, b) -> bool:
    return a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]


def ampliar(b, d) -> tuple:
    return (b[0] - d, b[1] - d, b[2] + d, b[3] + d)


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


def contiene(c, b) -> bool:
    return c[0] <= b[0] and b[2] <= c[2] and c[1] <= b[1] and b[3] <= c[3]


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


def sale(p0, p1, caja_origen, doble: bool) -> bool:
    """El tramo p0 → p1 sale del borde de la caja hacia afuera; si la flecha es
    de doble punta, empieza a HUECO_PUNTA del borde."""
    dx, dy = direccion(p0, p1)
    p = (p0[0] - HUECO_PUNTA * dx, p0[1] - HUECO_PUNTA * dy) if doble else p0
    lado = en_borde(p, caja_origen)
    return lado is not None and (dx, dy) == NORMAL[lado]


def llega(q0, q1, caja_destino) -> bool:
    """El tramo q0 → q1 termina a HUECO_PUNTA del borde de la caja, hacia adentro."""
    dx, dy = direccion(q0, q1)
    p = (q1[0] + HUECO_PUNTA * dx, q1[1] + HUECO_PUNTA * dy)
    lado = en_borde(p, caja_destino)
    return lado is not None and (dx, dy) == tuple(-v for v in NORMAL[lado])


# ========================================================================== #
# Controles                                                                   #
# ========================================================================== #
def controlar_contenido(M: dict) -> dict:
    if sorted(M["cajas"]) != sorted(CAJAS):
        falla("contenido", f"cajas dibujadas {sorted(M['cajas'])} ≠ las de CAJAS")
    for clave, c in M["cajas"].items():
        if c["clase"] != CAJAS[clave][0] or c["clase"] not in PALETA:
            falla("contenido", f"«{clave}» es «{c['clase']}» y en CAJAS es «{CAJAS[clave][0]}»")
    textos = textos_de(M)
    por_caja = {}
    for t in textos:
        por_caja.setdefault(t["dentro"] or t["tipo"], []).append(t)
    for clave, (_, titulo, texto) in CAJAS.items():
        ts = por_caja.pop(clave, [])
        tit = " ".join(t["s"] for t in ts if t["tipo"] == "titulo")
        seg = " ".join(t["s"] for t in ts if t["tipo"] == "texto")
        if (tit, seg) != (titulo, texto):
            falla("contenido", f"«{clave}»: dibujado «{tit} / {seg}» ≠ CAJAS «{titulo} / {texto}»")
        if any(t["negrita"] != (t["tipo"] == "titulo") for t in ts):
            falla("contenido", f"«{clave}»: el título no va en negrita o el texto sí")
        if any(t["color"] != (TINTA if t["tipo"] == "titulo" else TINTA_SUB) for t in ts):
            falla("contenido", f"«{clave}»: el texto no va en el gris de las cajas")
    for tipo, esperado in (("llamadas", ROTULO_LLAMADAS), ("servidores", ROTULO_SERVIDORES),
                           ("anotacion", ANOTACION)):
        ts = por_caja.pop(tipo, [])
        if " ".join(t["s"] for t in ts) != esperado:
            falla("contenido", f"el texto sin caja «{esperado}» no es el dibujado")
        if any(t["color"] != TINTA_SUB or t["negrita"] for t in ts):
            falla("contenido", f"«{esperado}» no va en el gris normal del texto de las cajas")
    if [t["s"] for t in por_caja.pop("leyenda", [])] != [s for _, s in LEYENDA]:
        falla("contenido", "la leyenda no es la de LEYENDA")
    if por_caja:
        falla("contenido", f"textos sin destino: {sorted(por_caja)}")
    return {"textos": len(textos), "cajas": len(M["cajas"])}


def controlar_disposicion(M: dict) -> dict:
    C, xs = M["cajas"], M["xs"]
    for i, col in enumerate(COLUMNAS):
        for k in col:
            if C[k]["x"] != float(f(xs[i])):
                falla("disposicion", f"«{k}» no está en su columna")
    for i in range(len(COLUMNAS) - 1):
        if max(der(C[k]) for k in COLUMNAS[i]) >= min(C[k]["x"] for k in COLUMNAS[i + 1]):
            falla("disposicion", f"la columna {i + 1} no queda a la izquierda de la {i + 2}")
    s1, s2 = C[ARRIBA[0]], C[ABAJO[0]]
    if s1["x"] != s2["x"] or aba(s1) >= s2["y"]:
        falla("disposicion", "los servidores no quedan uno arriba del otro")
    for srv, fuente in (ARRIBA, ABAJO):
        fu, sv = C[fuente], C[srv]
        if not (fu["y"] < aba(sv) and sv["y"] < aba(fu)):
            falla("disposicion", f"«{fuente}» no queda a la altura de «{srv}»")
    tr = C["traza"]
    if not (aba(C[ARRIBA[1]]) < tr["y"] and aba(tr) < C[ABAJO[1]]["y"]):
        falla("disposicion", "la traza no queda entre las 2 fuentes")
    por_tipo = {}
    for t in M["libres"]:
        por_tipo.setdefault(t["tipo"], []).append(caja_texto(t))
    # «llamadas», sobre su flecha y dentro de su largo
    fl = next(t for t in M["trazos"] if (t["desde"], t["hasta"]) == FLECHA_LLAMADAS)
    (xa, ya), (xb, _) = fl["puntos"][0], fl["puntos"][-1]
    r = por_tipo["llamadas"][0]
    if not (xa <= r[0] and r[2] <= xb and 0 < ya - r[3] <= 12):
        falla("disposicion", "«llamadas» no queda sobre su flecha")
    # «Un servidor por corrida», entre las 2 flechas del agente a los servidores
    y_fl = sorted(t["puntos"][0][1] for t in M["trazos"] if t["desde"] == "agente" and t["puntas"] == 2)
    rs = por_tipo["servidores"]
    if not all(der(C["agente"]) < r[0] and r[2] < s1["x"] and y_fl[0] < r[1] and r[3] < y_fl[1] for r in rs):
        falla("disposicion", "«Un servidor por corrida» no queda entre las 2 flechas a los servidores")
    # la anotación, debajo del servidor del grafo y dentro de su ancho
    sg, ra = C["srv_grafo"], por_tipo["anotacion"]
    if not aba(sg) < ra[0][1] <= aba(sg) + SEP_ANOTACION + IL[FS_TEXTO]:
        falla("disposicion", "la anotación no queda debajo del servidor del grafo")
    if not all(sg["x"] <= r[0] and r[2] <= der(sg) and r[1] > aba(sg) for r in ra):
        falla("disposicion", "la anotación se sale del ancho del servidor del grafo")
    return {"hueco": M["hueco"]}


def controlar_trazado(M: dict) -> dict:
    T, C = M["trazos"], M["cajas"]
    n_tramos = 0
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
        if not sale(t["puntos"][0], t["puntos"][1], C[t["desde"]], t["puntas"] == 2):
            falla("trazado", f"«{t['nombre']}» no sale del borde de «{t['desde']}» hacia afuera")
        if not llega(t["puntos"][-2], t["puntos"][-1], C[t["hasta"]]):
            falla("trazado", f"«{t['nombre']}» no llega al borde de «{t['hasta']}» ({t['puntos'][-1]})")
        if C[t["hasta"]]["x"] < C[t["desde"]]["x"]:
            falla("trazado", f"«{t['hasta']}» empieza a la izquierda de «{t['desde']}»")
    dibujadas = sorted((t["desde"], t["hasta"], t["puntas"]) for t in T)
    if dibujadas != sorted(FLECHAS):
        falla("trazado", f"flechas distintas de FLECHAS: {dibujadas}")
    return {"flechas": len(T), "tramos": n_tramos, "dobles": sum(t["puntas"] == 2 for t in T)}


def rect_leyenda(M: dict) -> tuple:
    L = M["leyenda"]
    return (L["x"], L["y"], L["x"] + L["w"], L["y"] + L["h"])


def controlar_cajas(M: dict) -> dict:
    C = M["cajas"]
    todas = [(k, bb(c), GROSOR_CAJA) for k, c in C.items()]
    todas.append(("leyenda", rect_leyenda(M), 1.0))
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
    minimo = (math.inf, "", "")
    for i in range(len(T)):
        for j in range(i + 1, len(T)):
            a, b = T[i], T[j]
            for p, q in tramos(a):
                for u, v in tramos(b):
                    c = contacto(p, q, u, v)
                    if c is not None:
                        falla("cruces", f"«{a['nombre']}» y «{b['nombre']}»: {c[0]} en {c[1]}")
            d = min(dist_segmentos(p, q, u, v) for p, q in tramos(a) for u, v in tramos(b)) - GROSOR_FLUJO
            if d < minimo[0]:
                minimo = (d, a["nombre"], b["nombre"])
    if minimo[0] < DISTANCIA_MIN:
        falla("cruces", f"«{minimo[1]}» pasa a {minimo[0]:.1f} de «{minimo[2]}» (< {DISTANCIA_MIN})")
    for t in T:
        for o in T:
            if o is t:
                continue
            for pt in puntas(t):
                for p, q in tramos(o):
                    d = dist_segmento_caja(p, q, caja_punta(pt)) - GROSOR_FLUJO / 2.0
                    if d < HOLGURA_TEXTO:
                        falla("cruces", f"una punta de «{t['nombre']}» toca la flecha «{o['nombre']}»")
    return {"distancia_minima": minimo}


def controlar_textos(M: dict) -> dict:
    C = M["cajas"]
    textos = [(t, caja_texto(t)) for t in textos_de(M)]
    contenedores = {k: (bb(c), GROSOR_CAJA) for k, c in C.items()}
    contenedores["leyenda"] = (rect_leyenda(M), 1.0)
    muestras = [(m["clave"], (m["x"], m["y"], m["x"] + m["w"], m["y"] + m["h"])) for m in muestras_leyenda(M)]
    minimos = {"texto-texto": math.inf, "texto-trazo": math.inf, "texto-borde de su caja": math.inf,
               "texto sin caja-caja": math.inf}
    tamanos = {}
    for t, r in textos:
        pt = puntos_impresos(t["fs"])
        tamanos[t["fs"]] = pt
        if t["fs"] < FS_MINIMO or pt < PT_MINIMO:
            falla("textos", f"«{t['s']}»: letra de {t['fs']} unidades, {pt:.2f} pt")
        if r[0] < 0 or r[1] < 0 or r[2] > W or r[3] > M["alto"]:
            falla("textos", f"«{t['s']}» sale del lienzo")
        if t["dentro"] is not None:
            c, g = contenedores[t["dentro"]]
            holg = min(r[0] - c[0], c[2] - r[2], r[1] - c[1], c[3] - r[3])
            minimos["texto-borde de su caja"] = min(minimos["texto-borde de su caja"], holg)
            if holg < g / 2.0 + HOLGURA_TEXTO:
                falla("textos", f"«{t['s']}» a {holg:.1f} del borde de «{t['dentro']}»")
        for k, (c2, g2) in contenedores.items():
            if k == t["dentro"]:
                continue
            if cruza(r, ampliar(c2, g2 / 2.0 + (HOLGURA_TEXTO if t["dentro"] is None else 0.0))):
                falla("textos", f"«{t['s']}» se superpone con la caja «{k}»")
            if t["dentro"] is None:
                dx = max(c2[0] - r[2], 0.0, r[0] - c2[2])
                dy = max(c2[1] - r[3], 0.0, r[1] - c2[3])
                minimos["texto sin caja-caja"] = min(minimos["texto sin caja-caja"], math.hypot(dx, dy) - g2 / 2.0)
        for k, m in muestras:
            if cruza(ampliar(r, HOLGURA_TEXTO), m):
                falla("textos", f"«{t['s']}» toca la muestra «{k}» de la leyenda")
        for tr in M["trazos"]:
            d = min(dist_segmento_caja(p, q, r) for p, q in tramos(tr)) - GROSOR_FLUJO / 2.0
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
    todas.append(("leyenda", ampliar(rect_leyenda(M), 0.5)))
    for t in M["trazos"]:
        g = GROSOR_FLUJO / 2.0
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
    return {"elementos": len(todas), "minimos": minimos, "alto_cm": ANCHO_CM * M["alto"] / W}


def verificar(M: dict) -> dict:
    rep = {"contenido": controlar_contenido(M), "disposicion": controlar_disposicion(M),
           "trazado": controlar_trazado(M), "cajas": controlar_cajas(M), "cruces": controlar_cruces(M)}
    rep["textos"] = controlar_textos(M)
    rep["margen"] = controlar_margen(M, rep["textos"]["cajas_texto"])
    rep["svg"] = dibujar(M)
    rep["registro"] = controlar_registro(rep["svg"], M)
    return rep


# ========================================================================== #
# Emisión del SVG                                                             #
# ========================================================================== #
def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def path_redondeado(puntos) -> str:
    """Poligonal con esquinas redondeadas de radio RADIO."""
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
        f'<marker id="arI" {MARCADOR_INICIO} fill="{FLECHA}"/></marker></defs>',
    ]
    for clave, c in M["cajas"].items():
        pal = PALETA[c["clase"]]
        partes.append(f'<rect data-caja="{clave}" x="{f(c["x"])}" y="{f(c["y"])}" width="{f(c["w"])}" '
                      f'height="{f(c["h"])}" fill="{pal["relleno"]}" stroke="{pal["borde"]}" '
                      f'stroke-width="{GROSOR_CAJA}" rx="{RX}"/>')
    for t in M["trazos"]:
        inicio = ' marker-start="url(#arI)"' if t["puntas"] == 2 else ""
        partes.append(f'<path data-flecha="{esc(t["nombre"])}" d="{path_redondeado(t["puntos"])}" fill="none" '
                      f'stroke="{FLECHA}" stroke-width="{GROSOR_FLUJO}"{inicio} marker-end="url(#arN)"/>')
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
    """El SVG se relee: cada caja, muestra de la leyenda y flecha tiene el color,
    el grosor y las puntas de su clase."""
    raiz = ET.fromstring(svg)
    clase_de = {k: c["clase"] for k, c in M["cajas"].items()}
    clase_de.update({f"leyenda_{c}": c for c, _ in LEYENDA})
    por_nombre = {t["nombre"]: t for t in M["trazos"]}
    n = {"cajas": 0, "muestras": 0, "flechas": 0, "textos": 0}
    for el in raiz.iter():
        clave = el.get("data-caja")
        if clave is not None:
            pal = PALETA[clase_de[clave]]
            if (el.get("fill"), el.get("stroke"), el.get("stroke-width")) != (
                    pal["relleno"], pal["borde"], str(GROSOR_CAJA)):
                falla("registro", f"«{clave}» con relleno {el.get('fill')}, borde {el.get('stroke')} "
                                  f"y grosor {el.get('stroke-width')}")
            n["muestras" if clave.startswith("leyenda_") else "cajas"] += 1
        nombre = el.get("data-flecha")
        if nombre is not None:
            t = por_nombre[nombre]
            esperado = (FLECHA, str(GROSOR_FLUJO), "url(#arN)", "url(#arI)" if t["puntas"] == 2 else None)
            if (el.get("stroke"), el.get("stroke-width"), el.get("marker-end"), el.get("marker-start")) != esperado:
                falla("registro", f"la flecha «{nombre}» no tiene el trazo o las puntas de su línea en FLECHAS")
            n["flechas"] += 1
        if el.tag.endswith("text"):
            n["textos"] += 1
    if n["cajas"] != len(M["cajas"]) or n["muestras"] != len(LEYENDA) or n["flechas"] != len(M["trazos"]):
        falla("registro", f"elementos sin color controlado: {n}")
    return n


# ========================================================================== #
# Exportación                                                                 #
# ========================================================================== #
def con_densidad(png: bytes, dpi: int) -> bytes:
    """El PNG con el bloque pHYs (píxeles por metro) después de IHDR."""
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


def leer_png(png: bytes) -> dict:
    """Ancho, alto y densidad grabada (dpi) de un PNG."""
    wpx, hpx = struct.unpack(">II", png[16:24])
    i, dpi = 8, None
    while i < len(png):
        largo = struct.unpack(">I", png[i:i + 4])[0]
        if png[i + 4:i + 8] == b"pHYs":
            ppx, ppy, unidad = struct.unpack(">IIB", png[i + 8:i + 17])
            dpi = (round(ppx * 0.0254, 2), round(ppy * 0.0254, 2)) if unidad == 1 else None
        i += 12 + largo
    return {"ancho": wpx, "alto": hpx, "dpi": dpi}


def exportar(svg: str) -> bytes:
    rsvg = shutil.which("rsvg-convert")
    if not rsvg:
        falla("exportacion", "rsvg-convert no está instalado: no se escribe el PNG")
    r = subprocess.run([rsvg, "-w", str(ANCHO_PNG_PX), "-f", "png"], input=svg.encode("utf-8"),
                       capture_output=True)
    if r.returncode != 0:
        falla("exportacion", r.stderr.decode("utf-8", "replace"))
    png = con_densidad(r.stdout, DPI)
    info = leer_png(png)
    if info["ancho"] != ANCHO_PNG_PX or info["dpi"] != (DPI, DPI):
        falla("imagen", f"el PNG mide {info['ancho']} px y graba {info['dpi']} dpi")
    return png


# ========================================================================== #
# Principal                                                                   #
# ========================================================================== #
def main() -> int:
    try:
        M = armar()
        rep = verificar(M)
        png = exportar(rep["svg"])
    except Falla as e:
        print(f"ALTO {e}")
        print("No se escribe nada.")
        return 1

    print("CAJAS (renglones dibujados):")
    for clave, c in M["cajas"].items():
        print(f"  {clave}: x={c['x']} y={c['y']} {c['w']:.0f}×{c['h']:.0f} [{c['clase']}]")
        for l in lineas_caja(clave):
            print(f"      {'N' if l['negrita'] else ' '} {l['s']}")
    print("TEXTOS SIN CAJA:")
    for t in M["libres"]:
        print(f"  [{t['tipo']}] x={t['x']} base={t['y']}  {t['s']}")
    c = rep["contenido"]
    print(f"CONTENIDO: {c['cajas']} cajas, las de CAJAS, con su clase, su título y su texto letra por letra; "
          f"{c['textos']} renglones de texto en total, con los sin caja y la leyenda")
    print(f"DISPOSICIÓN: columnas de izquierda a derecha; servidores uno arriba del otro; fuentes a la "
          f"altura de su servidor; hueco de los rótulos {rep['disposicion']['hueco']:.1f}")
    t = rep["trazado"]
    print(f"TRAZADO: {t['flechas']} flechas ({t['dobles']} de doble punta), {t['tramos']} tramos, 0 diagonales, "
          f"0 hacia la izquierda; extremos en el borde de su caja; flechas = las de FLECHAS")
    k = rep["cajas"]
    print(f"CAJAS: {k['cajas']} (con la leyenda), sin superposiciones; separación mínima entre bordes "
          f"{k['separacion_minima']:.1f}; ningún trazo ni punta entra en una caja")
    d = rep["cruces"]["distancia_minima"]
    print(f"CRUCES entre flechas: 0; contactos: 0; distancia mínima entre flechas {d[0]:.1f} "
          f"(«{d[1]}» / «{d[2]}»), exigida {DISTANCIA_MIN}")
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
    print(f"REGISTRO: color, grosor y puntas controlados en {rg['cajas']} cajas, {rg['muestras']} muestras y "
          f"{rg['flechas']} flechas; {rg['textos']} textos en el SVG")

    ruta_png = os.path.join(AQUI, f"{NOMBRE}.png")
    with open(ruta_png, "wb") as fh:
        fh.write(png)
    info = leer_png(png)
    print(f"TAMAÑO: lienzo {W} × {M['alto']}; impreso {ANCHO_CM:.2f} × {mg['alto_cm']:.2f} cm; "
          f"PNG {info['ancho']} × {info['alto']} px a {info['dpi'][0]:.0f} dpi")
    print(f"PNG: {ruta_png}  sha256 {hashlib.sha256(png).hexdigest()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
