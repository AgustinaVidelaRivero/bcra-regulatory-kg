#!/usr/bin/env python3
"""Figura «la misma pregunta con dos formas de consultar» para la Introducción.

Dos columnas bajo una pregunta común. Izquierda, «Recuperación por fragmentos»:
los cuatro puntos del ejemplo como fragmentos, cada uno con su número y la
etiqueta corta de su nodo, el recuperado enmarcado (con la frase de remisión
resaltada) y los no recuperados en gris; debajo, la respuesta que se puede
redactar solo con lo recuperado. Derecha, «Consulta del grafo»: buscar, abrir el
nodo del punto 3.17.1.4 y seguir las aristas de remisión; debajo, la respuesta
con cada condición y su punto.

Versión compacta: el alto del PNG está acotado (ALTO_MAX_PNG_PX) para que la
figura impresa a 12,75 cm ocupe menos de media página con el texto corrido a
7 pt o más; el script se detiene sin escribir si no lo cumple.

Misma técnica que generar_figura_norma_a_grafo.py, del que IMPORTA las fuentes,
la frase de remisión y los textos de los puntos (nada se retipea), la
verificación de aristas contra el grafo, las métricas de Helvetica, la paleta y
la leyenda. El SVG se escribe a mano y se exporta a PNG con rsvg-convert, sin
dejar el SVG en el repo (se pasa por stdin). Generación determinística.

Uso:
    python3 docs/tesis/figuras/generar_figura_fragmentos_vs_grafo.py
    python3 docs/tesis/figuras/generar_figura_fragmentos_vs_grafo.py --svg RUTA
    .venv/bin/python docs/tesis/figuras/generar_figura_fragmentos_vs_grafo.py --verificar-busqueda
"""

import sys

sys.dont_write_bytecode = True  # importar al generador hermano no deja __pycache__

import argparse
import hashlib
import os
import struct
import subprocess
import zlib

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import generar_figura_norma_a_grafo as base  # noqa: E402

SALIDA_PNG = os.path.join(AQUI, "figura_fragmentos_vs_grafo.png")

# --------------------------------------------------------------------------- #
# Contenido                                                                    #
# --------------------------------------------------------------------------- #
PREGUNTA = ("¿Puede una empresa pagar dividendos a accionistas del exterior? "
            "¿Qué requisitos debe cumplir?")

# Resultado de la búsqueda por texto completo que sirve la app (Neo4jIndex en
# modo 'fulltext', índice Lucene/BM25 `nodos_fulltext_kg_reextraido_r1`,
# limite=10) con PREGUNTA como consulta. Cada par es (punto, recuperado):
# el orden es el de primera aparición del punto en el ranking (mejor posición
# de un nodo de contenido con punto propio en ese punto) y «recuperado» es que
# esa posición esté entre los diez primeros. Se reproduce, con Neo4j levantado,
# con la opción --verificar-busqueda, que detiene el script si ya no coincide.
LIMITE_BUSQUEDA = 10
RESULTADO_BUSQUEDA = [
    ("3.17.1.4", True),
    ("3.4.3", False),
    ("3.4.2", False),
    ("3.4.1", False),
]
SUBTITULO_FRAGMENTOS = "Los cuatro puntos del ejemplo"
ETIQUETA_RECUPERADO = "recuperado"
ETIQUETA_NO_RECUPERADO = "fuera de lo recuperado"
OMISION = "[…] "     # la frase de remisión es un recorte del punto 3.17.1.4

# Nodo que la figura rotula con cada punto (el mismo de «de la norma al grafo»).
CLAVE_DE_PUNTO = {"3.17.1.4": "R", "3.4.1": "O1", "3.4.2": "O2", "3.4.3": "O3"}

# Los nodos de contexto (operación y sujeto) se dibujan atenuados, como en la
# figura «de la norma al grafo», para que la leyenda compartida nombre solo
# cosas que la figura muestra.
DIBUJAR_CONTEXTO = True

# --------------------------------------------------------------------------- #
# Geometría. Mismo ancho en píxeles que la figura «de la norma al grafo»; la    #
# letra es dos puntos más grande en las clases menores (rótulos, encabezados y  #
# etiquetas de nodo), porque esta figura se imprime a 12,75 cm y las de la otra #
# quedaban por debajo de 6,5 pt. El texto corrido va a FS_TEXTO.                #
# --------------------------------------------------------------------------- #
W = base.W
MARGEN = base.MARGEN
MARGEN_V = 8
ANCHO_TOTAL = base.ANCHO_PANEL
SEPARACION = 20
ANCHO_COL = (ANCHO_TOTAL - SEPARACION) / 2.0     # 396
PAD = 14
PAD_V = 12

FS_TITULO = base.FS_TITULO_PANEL     # 17
FS_TEXTO = base.FS_TEXTO             # 17
FS_ENCABEZADO = base.FS_ENCABEZADO + 2   # 17
FS_NODO = base.FS_NODO + 2           # 17
FS_ROTULO = base.FS_ROTULO + 2       # 15
FS_LEYENDA = base.FS_LEYENDA + 2     # 15
INTERLINEA = base.INTERLINEA
PASO_NODO = 19                       # interlínea dentro de los nodos
PASO_ROTULO = 17                     # interlínea de la pregunta en la búsqueda

ANCHO_IMPRESO_CM = 12.75
DPI = 300
ANCHO_PNG_PX = int(round(ANCHO_IMPRESO_CM / 2.54 * DPI))   # 1506
ALTO_MAX_PNG_PX = 1700
PT_MIN_TEXTO = 7.0

GRIS_TEXTO_APAGADO = "#9a9a9a"
GRIS_BORDE_APAGADO = "#bdbdbd"
FONDO_APAGADO = "#f1f1f1"
COLOR_FLUJO = "#555"

ancho, envolver, esc, f = base.ancho, base.envolver, base.esc, base.f


def puntos_impresos(px):
    return px * (ANCHO_IMPRESO_CM * base.PT_POR_CM) / W


# Anchos de Helvetica Bold (unidades/1000 em) donde difieren de la redonda. En
# una columna angosta el 4 % con que el generador hermano aproxima la negrita
# queda corto (la minúscula es ~10 % más ancha) y la frase resaltada desbordaba
# el recuadro: acá la negrita se mide con su propia tabla.
_WB = {"!": 333, '"': 474, "&": 722, "'": 238, ":": 333, ";": 333, "?": 611, "@": 975,
       "A": 722, "B": 722, "J": 556, "K": 722, "L": 611,
       "b": 611, "c": 556, "d": 611, "f": 333, "g": 611, "h": 611, "i": 278, "j": 278,
       "k": 556, "l": 278, "m": 889, "n": 611, "o": 611, "p": 611, "q": 611, "r": 389,
       "s": 556, "t": 333, "u": 611, "v": 556, "w": 778, "x": 556, "y": 556,
       "í": 278, "ó": 611, "ú": 611, "ñ": 611, "ü": 611}


def ancho_negrita(texto, fs):
    return sum(_WB.get(c, base._W.get(c, 556)) for c in texto) / 1000.0 * fs


def envolver_negrita(texto, fs, ancho_max):
    """Mismo envoltorio por palabras que base.envolver, medido en negrita."""
    lineas, actual, inicio, cursor = [], "", 0, 0
    for palabra in texto.split(" "):
        cand = palabra if not actual else actual + " " + palabra
        if actual and ancho_negrita(cand, fs) > ancho_max:
            lineas.append((actual, inicio))
            inicio, actual = cursor, palabra
        else:
            actual = cand
        cursor += len(palabra) + 1
    if actual:
        lineas.append((actual, inicio))
    return lineas


# --------------------------------------------------------------------------- #
# Piezas                                                                       #
# --------------------------------------------------------------------------- #
def panel(x, y, w, h):
    return (f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" '
            f'fill="{base.FONDO_PANEL}" stroke="{base.BORDE_PANEL}" rx="5"/>')


def flecha_flujo(x, y1, y2):
    return (f'<path d="M{f(x)},{f(y1)} L{f(x)},{f(y2)}" fill="none" stroke="{COLOR_FLUJO}" '
            f'stroke-width="1.5" marker-end="url(#arF)"/>')


# Fragmento compacto: encabezado con el número y el estado, debajo la etiqueta
# corta del nodo de ese punto; el recuperado agrega la frase de remisión.
LINEA_ENCABEZADO = 26      # del borde superior a la línea base del encabezado
LINEA_ETIQUETA = 50        # ídem, a la línea base de la etiqueta
ALTO_FRAGMENTO = 62
SALTO_FRASE = 28           # de la etiqueta a la primera línea de la frase
GAP_FRAGMENTOS = 12        # mínimo; crece hasta GAP_FRAGMENTOS_MAX si la columna sobra
GAP_FRAGMENTOS_MAX = 26
ALTO_SUBTITULO = 22


def frase_de(bloque):
    """Frase de remisión del fragmento recuperado, tomada del generador hermano y
    comprobada contra el texto del punto; None si el punto no remite."""
    if not bloque["resaltar"]:
        return None
    if bloque["resaltar"] not in bloque["texto"]:
        raise SystemExit(f"la frase resaltada no está en el texto del punto {bloque['punto']}")
    return OMISION + bloque["resaltar"]


def lineas_frase(bloque, w, recuperado):
    frase = frase_de(bloque) if recuperado else None
    return envolver_negrita(frase, FS_TEXTO, w - 2 * PAD) if frase else []


def alto_fragmento(bloque, w, recuperado):
    n = len(lineas_frase(bloque, w, recuperado))
    if not n:
        return ALTO_FRAGMENTO
    return LINEA_ETIQUETA + SALTO_FRASE + (n - 1) * INTERLINEA + 16


def dibujar_fragmento(bloque, etiqueta, x, y, w, recuperado):
    partes = []
    alto = alto_fragmento(bloque, w, recuperado)
    if recuperado:
        partes.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(alto)}" '
                      f'fill="white" stroke="#333" stroke-width="1.8" rx="4"/>')
    else:
        partes.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(alto)}" '
                      f'fill="{FONDO_APAGADO}" stroke="{GRIS_BORDE_APAGADO}" '
                      f'stroke-width="1.0" stroke-dasharray="5,4" rx="4"/>')
    y_enc = y + LINEA_ENCABEZADO
    partes.append(f'<text x="{f(x + PAD)}" y="{f(y_enc)}" font-size="{FS_ENCABEZADO}" '
                  f'font-weight="bold" fill="{"#333" if recuperado else GRIS_TEXTO_APAGADO}">'
                  f'Punto {esc(bloque["punto"])}</text>')
    if recuperado:
        partes.append(f'<text x="{f(x + w - PAD)}" y="{f(y_enc)}" text-anchor="end" '
                      f'font-size="{FS_ROTULO}" font-weight="bold" fill="#333">'
                      f'{esc(ETIQUETA_RECUPERADO)}</text>')
    else:
        partes.append(f'<text x="{f(x + w - PAD)}" y="{f(y_enc)}" text-anchor="end" '
                      f'font-size="{FS_ROTULO}" font-style="italic" fill="{base.GRIS_ROTULO}">'
                      f'{esc(ETIQUETA_NO_RECUPERADO)}</text>')
    if ancho(etiqueta, FS_TEXTO) > w - 2 * PAD:
        raise SystemExit(f"la etiqueta de {bloque['punto']} no entra en una línea")
    partes.append(f'<text x="{f(x + PAD)}" y="{f(y + LINEA_ETIQUETA)}" font-size="{FS_TEXTO}" '
                  f'fill="{"#1f1f1f" if recuperado else GRIS_TEXTO_APAGADO}">{esc(etiqueta)}</text>')

    # Frase de remisión: todo resaltado salvo la marca de omisión inicial.
    yl = y + LINEA_ETIQUETA + SALTO_FRASE
    for linea, desplazamiento in lineas_frase(bloque, w, recuperado):
        corte = max(0, len(OMISION) - desplazamiento)
        previo, marcado = linea[:corte], linea[corte:]
        xc = x + PAD + ancho(previo, FS_TEXTO)
        partes.append(f'<rect x="{f(xc - 1)}" y="{f(yl - FS_TEXTO + 2)}" '
                      f'width="{f(ancho_negrita(marcado, FS_TEXTO) + 2)}" height="{f(FS_TEXTO + 5)}" '
                      f'fill="{base.ACENTO}" opacity="0.26" rx="2"/>')
        tspans = (f'<tspan>{esc(previo)}</tspan>' if previo else "")
        tspans += (f'<tspan font-weight="bold" fill="{base.ACENTO_TEXTO}">{esc(marcado)}</tspan>')
        partes.append(f'<text x="{f(x + PAD)}" y="{f(yl)}" font-size="{FS_TEXTO}" '
                      f'fill="#1f1f1f" xml:space="preserve">{tspans}</text>')
        yl += INTERLINEA
    return partes, alto


def alto_columna_fragmentos(bloques, estado):
    w = ANCHO_COL - 2 * PAD
    total = PAD_V + ALTO_SUBTITULO
    total += sum(alto_fragmento(b, w, estado[b["punto"]]) for b in bloques)
    total += GAP_FRAGMENTOS * (len(bloques) - 1)
    return total + PAD_V


def dibujar_columna_fragmentos(bloques, etiquetas, estado, x0, y0, alto):
    partes = [panel(x0, y0, ANCHO_COL, alto)]
    partes.append(f'<text x="{f(x0 + PAD)}" y="{f(y0 + PAD_V + 12)}" font-size="{FS_ROTULO}" '
                  f'font-weight="bold" fill="#444">{esc(SUBTITULO_FRAGMENTOS)}</text>')
    # Si la columna de enfrente es más alta, los recuadros se separan un poco
    # más (hasta un tope) en vez de dejar todo el sobrante al pie.
    sobrante = alto - alto_columna_fragmentos(bloques, estado)
    gap = min(GAP_FRAGMENTOS_MAX, GAP_FRAGMENTOS + sobrante / (len(bloques) - 1))
    y = y0 + PAD_V + ALTO_SUBTITULO
    for b in bloques:
        piezas, h = dibujar_fragmento(b, etiquetas[b["punto"]], x0 + PAD, y,
                                      ANCHO_COL - 2 * PAD, estado[b["punto"]])
        partes += piezas
        y += h + gap
    return partes


def lineas_nodo(nodos, nid, w):
    """Líneas de texto de un nodo: el número de punto (si lo tiene) y la
    etiqueta corta envuelta al ancho de la caja."""
    corta, _ = base.etiqueta_de(nodos, nid)
    punto = base.punto_de_la_figura(nodos[nid])
    lineas = [(punto, True)] if punto else []
    lineas += [(linea, False) for linea, _ in envolver(corta, FS_NODO, w - 22)]
    return lineas


def alto_nodo(nodos, nid, w):
    return len(lineas_nodo(nodos, nid, w)) * PASO_NODO + 8


def dibujar_nodo(nodos, nid, cx, cy, w, h, focal):
    """Mismo estilo de nodo que la figura «de la norma al grafo»."""
    color = base.COLOR_TIPO[nodos[nid]["type"]]
    partes = [f'<rect x="{f(cx - w / 2)}" y="{f(cy - h / 2)}" width="{f(w)}" height="{f(h)}" '
              f'fill="{color}" fill-opacity="{"0.95" if focal else "0.45"}" '
              f'stroke="{"black" if focal else "#777"}" '
              f'stroke-width="{"1.8" if focal else "1.1"}" rx="7"/>']
    lineas = lineas_nodo(nodos, nid, w)
    ytxt = cy - (len(lineas) - 1) * PASO_NODO / 2.0 + 6
    for linea, es_punto in lineas:
        partes.append(f'<text x="{f(cx)}" y="{f(ytxt)}" text-anchor="middle" '
                      f'font-size="{FS_NODO}" font-weight="{"bold" if es_punto else "normal"}" '
                      f'fill="{"white" if focal else "#222"}">{esc(linea)}</text>')
        ytxt += PASO_NODO
    return partes


# Disposición del panel de la consulta (coordenadas relativas a su esquina).
# Las alturas salen del número de líneas de cada elemento; solo los anchos y
# las separaciones son fijos. Los nodos remitidos son anchos para que la
# mayoría de las etiquetas entren en una sola línea.
X_PILDORA, ANCHO_PILDORA = 14, 368
X_R, ANCHO_R = 14, 320
X_NODO, ANCHO_NODO = 102, 280
TRONCO_REMISION = 38     # x del tronco del que salen las tres remisiones
TRONCO_CONTEXTO = 22     # x del tronco de las aristas de contexto
X_FLECHA_BUSQUEDA = 300
SALTO_PASO = 18          # de un elemento a la línea base del rótulo del paso siguiente
BAJO_PASO = 8            # del rótulo del paso al elemento que encabeza
GAP_NODOS = 6
GAP_CONTEXTO = 10


def disposicion_grafo(nodos, ids):
    """Posiciones verticales del panel de la consulta y su alto total."""
    claves_ctx = ["OP", "SU"] if DIBUJAR_CONTEXTO else []
    d = {"pasos": {}, "cajas": {}}
    y = PAD_V + 13
    d["pasos"][1] = (PAD + 4, y)
    lineas = envolver(PREGUNTA, FS_ROTULO, ANCHO_PILDORA - 44)
    y += BAJO_PASO
    d["pildora"] = {"y": y, "h": len(lineas) * PASO_ROTULO + 12, "lineas": lineas}
    y += d["pildora"]["h"] + SALTO_PASO
    d["pasos"][2] = (PAD + 4, y)
    y += BAJO_PASO
    h = alto_nodo(nodos, ids["R"], ANCHO_R)
    d["cajas"]["R"] = {"cx": X_R + ANCHO_R / 2.0, "cy": y + h / 2.0, "w": ANCHO_R, "h": h, "focal": True}
    y += h + SALTO_PASO
    d["pasos"][3] = (X_NODO, y)
    y += BAJO_PASO
    for i, clave in enumerate(["O1", "O2", "O3"] + claves_ctx):
        if clave == "OP":
            y += GAP_CONTEXTO - GAP_NODOS
        h = alto_nodo(nodos, ids[clave], ANCHO_NODO)
        d["cajas"][clave] = {"cx": X_NODO + ANCHO_NODO / 2.0, "cy": y + h / 2.0,
                             "w": ANCHO_NODO, "h": h, "focal": clave.startswith("O")}
        y += h + GAP_NODOS
    d["alto"] = y - GAP_NODOS + PAD_V
    return d


def dibujar_columna_grafo(nodos, ids, aristas, disp, x0, y0, alto):
    partes = [panel(x0, y0, ANCHO_COL, alto)]
    cajas = disp["cajas"]

    def paso(n, texto):
        x, y = disp["pasos"][n]
        return (f'<text x="{f(x0 + x)}" y="{f(y0 + y)}" font-size="{FS_ROTULO}" '
                f'font-weight="bold" fill="#444">{esc(texto)}</text>')

    # Paso 1: buscar, con la misma pregunta.
    partes.append(paso(1, "1 · Buscar"))
    p = disp["pildora"]
    partes.append(f'<rect x="{f(x0 + X_PILDORA)}" y="{f(y0 + p["y"])}" width="{f(ANCHO_PILDORA)}" '
                  f'height="{f(p["h"])}" fill="white" stroke="#999" stroke-width="1.2" rx="20"/>')
    yl = y0 + p["y"] + p["h"] / 2.0 - (len(p["lineas"]) - 1) * PASO_ROTULO / 2.0 + 5
    for linea, _ in p["lineas"]:
        partes.append(f'<text x="{f(x0 + X_PILDORA + ANCHO_PILDORA / 2.0)}" y="{f(yl)}" '
                      f'text-anchor="middle" font-size="{FS_ROTULO}" font-style="italic" '
                      f'fill="#333">{esc(linea)}</text>')
        yl += PASO_ROTULO

    # Paso 2: abrir el nodo encontrado.
    r = cajas["R"]
    partes.append(paso(2, "2 · Abrir el nodo encontrado"))
    partes.append(flecha_flujo(x0 + X_FLECHA_BUSQUEDA, y0 + p["y"] + p["h"],
                               y0 + r["cy"] - r["h"] / 2.0 - 3))

    # Paso 3: seguir las remisiones. La existencia de cada arista ya fue
    # comprobada contra el grafo por base.cargar(); acá solo se traza.
    partes.append(paso(3, "3 · Seguir las aristas «remite a»"))
    por_id = {ids[k]: k for k in ids}
    y_salida = y0 + r["cy"] + r["h"] / 2.0
    rotulos = []
    for origen, relacion, destino in aristas:
        ka, kb = por_id[origen], por_id[destino]
        remision = (relacion == "referencia")
        if not remision and not DIBUJAR_CONTEXTO:
            continue
        if ka != "R" or kb not in cajas:
            raise SystemExit(f"arista sin trazado definido: {ka} -> {kb} ({relacion})")
        caja = cajas[kb]
        tx = x0 + (TRONCO_REMISION if remision else TRONCO_CONTEXTO)
        x_llegada = x0 + caja["cx"] - caja["w"] / 2.0 - 2
        cy = y0 + caja["cy"]
        color = base.ACENTO if remision else base.GRIS_ARISTA
        extra = "" if remision else ' stroke-dasharray="4,4"'
        partes.append(f'<path d="M{f(tx)},{f(y_salida)} L{f(tx)},{f(cy)} L{f(x_llegada)},{f(cy)}" '
                      f'fill="none" stroke="{color}" stroke-width="{"2.6" if remision else "1.5"}"'
                      f'{extra} stroke-linejoin="round" '
                      f'marker-end="url(#{"arA" if remision else "arG"})"/>')
        rotulos.append(((tx + x_llegada) / 2.0, cy - 12,
                        base.CASTELLANO.get(relacion, relacion), remision))
    for mx, my, texto, remision in rotulos:
        at = ancho_negrita(texto, FS_ROTULO) if remision else ancho(texto, FS_ROTULO)
        partes.append(f'<rect x="{f(mx - at / 2 - 1)}" y="{f(my - FS_ROTULO + 1)}" '
                      f'width="{f(at + 2)}" height="{f(FS_ROTULO + 4)}" '
                      f'fill="{base.FONDO_PANEL}" opacity="0.94" rx="2"/>')
        partes.append(f'<text x="{f(mx)}" y="{f(my + 2)}" text-anchor="middle" '
                      f'font-size="{FS_ROTULO}" font-weight="{"bold" if remision else "normal"}" '
                      f'fill="{base.ACENTO_TEXTO if remision else base.GRIS_ROTULO}">'
                      f'{esc(texto)}</text>')

    for clave, c in cajas.items():
        partes += dibujar_nodo(nodos, ids[clave], x0 + c["cx"], y0 + c["cy"],
                               c["w"], c["h"], c["focal"])
    return partes


# --------------------------------------------------------------------------- #
# Respuestas                                                                   #
# --------------------------------------------------------------------------- #
ALTO_FILA = 26
GAP_FILA = 4


def textos_respuesta(nodos, ids):
    """La respuesta de cada columna, armada con lo que esa columna obtuvo: a la
    izquierda, la frase de remisión del único fragmento recuperado; a la
    derecha, la etiqueta de cada nodo alcanzado por una arista de remisión."""
    izquierda = (f"Sí, {base.FRASE_RESALTADA.rstrip('.')} "
                 f"(punto {base.PUNTO_ORIGEN}).")
    derecha = f"Sí, si se cumplen las condiciones a las que remite el punto {base.PUNTO_ORIGEN}:"
    condiciones = []
    for punto in base.PUNTOS_DESTINO:
        corta, _ = base.etiqueta_de(nodos, ids[CLAVE_DE_PUNTO[punto]])
        condiciones.append((punto, corta))
    return izquierda, derecha, condiciones


def alto_respuesta(entradas):
    ancho_txt = ANCHO_COL - 2 * PAD
    n = max(len(envolver(t, FS_TEXTO, ancho_txt)) for t in entradas)
    alto = (PAD_V + FS_ENCABEZADO + 6 + n * INTERLINEA + 6
            + 3 * (ALTO_FILA + GAP_FILA) - GAP_FILA + PAD_V)
    return alto, n


def dibujar_respuesta(titulo, entrada, filas, completas, n_lineas, x0, y0, alto):
    partes = [panel(x0, y0, ANCHO_COL, alto)]
    partes.append(f'<text x="{f(x0 + PAD)}" y="{f(y0 + PAD_V + FS_ENCABEZADO - 2)}" '
                  f'font-size="{FS_ENCABEZADO}" font-weight="bold" fill="#333">{esc(titulo)}</text>')
    yl = y0 + PAD_V + FS_ENCABEZADO + 6 + FS_TEXTO
    for linea, _ in envolver(entrada, FS_TEXTO, ANCHO_COL - 2 * PAD):
        partes.append(f'<text x="{f(x0 + PAD)}" y="{f(yl)}" font-size="{FS_TEXTO}" '
                      f'fill="#1f1f1f">{esc(linea)}</text>')
        yl += INTERLINEA
    y = y0 + PAD_V + FS_ENCABEZADO + 6 + n_lineas * INTERLINEA + 6
    x, w = x0 + PAD, ANCHO_COL - 2 * PAD
    for punto, etiqueta in filas:
        y_txt = y + ALTO_FILA / 2.0 + 6
        if completas:
            partes.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(ALTO_FILA)}" '
                          f'fill="white" stroke="#d8d8d8" rx="4"/>')
            partes.append(f'<rect x="{f(x)}" y="{f(y)}" width="6" height="{f(ALTO_FILA)}" '
                          f'fill="{base.COLOR_TIPO["Obligacion"]}" rx="2"/>')
            x_etq = x + 14 + ancho_negrita(punto, FS_TEXTO) + 8
            if x_etq + ancho(etiqueta, FS_TEXTO) > x + w - 6:
                raise SystemExit(f"la condición de {punto} no entra en una línea")
            partes.append(f'<text x="{f(x + 14)}" y="{f(y_txt)}" font-size="{FS_TEXTO}" '
                          f'font-weight="bold" fill="#1f1f1f">{esc(punto)}</text>')
            partes.append(f'<text x="{f(x_etq)}" y="{f(y_txt)}" font-size="{FS_TEXTO}" '
                          f'fill="#1f1f1f">{esc(etiqueta)}</text>')
        else:
            cy = y + ALTO_FILA / 2.0
            partes.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(ALTO_FILA)}" '
                          f'fill="none" stroke="{GRIS_BORDE_APAGADO}" stroke-width="1.2" '
                          f'stroke-dasharray="5,4" rx="4"/>')
            for dx1, dy1, dx2, dy2 in [(-5, -5, 5, 5), (-5, 5, 5, -5)]:
                partes.append(f'<path d="M{f(x + 19 + dx1)},{f(cy + dy1)} L{f(x + 19 + dx2)},{f(cy + dy2)}" '
                              f'stroke="{base.GRIS_ROTULO}" stroke-width="2"/>')
            partes.append(f'<text x="{f(x + 34)}" y="{f(y_txt)}" font-size="{FS_TEXTO}" '
                          f'font-style="italic" fill="{base.GRIS_ROTULO}">'
                          f'condición del punto {esc(punto)}: omitida</text>')
        y += ALTO_FILA + GAP_FILA
    return partes


def dibujar_leyenda(nodos, ids, y0, alto):
    """La leyenda de la figura «de la norma al grafo» (misma función, mismo
    contenido), con la letra al tamaño de los rótulos de esta figura. El tamaño
    es una constante de módulo del generador hermano: se sustituye solo durante
    la llamada."""
    original = base.FS_LEYENDA
    base.FS_LEYENDA = FS_LEYENDA
    try:
        return base.dibujar_leyenda(nodos, ids, y0, alto)
    finally:
        base.FS_LEYENDA = original


# --------------------------------------------------------------------------- #
# PNG                                                                          #
# --------------------------------------------------------------------------- #
def con_resolucion(png, dpi):
    """Reescribe el bloque pHYs para que el PNG declare `dpi` puntos por pulgada."""
    firma, cuerpo = png[:8], png[8:]
    ppm = int(round(dpi / 0.0254))
    datos = struct.pack(">IIB", ppm, ppm, 1)
    phys = (struct.pack(">I", len(datos)) + b"pHYs" + datos
            + struct.pack(">I", zlib.crc32(b"pHYs" + datos) & 0xFFFFFFFF))
    salida, i = [firma], 0
    while i < len(cuerpo):
        largo = struct.unpack(">I", cuerpo[i:i + 4])[0]
        tipo = cuerpo[i + 4:i + 8]
        bloque = cuerpo[i:i + 12 + largo]
        if tipo != b"pHYs":
            salida.append(bloque)
        if tipo == b"IHDR":
            salida.append(phys)
        i += 12 + largo
    return b"".join(salida)


def exportar_png(svg):
    try:
        proc = subprocess.run(["rsvg-convert", "-f", "png", "-w", str(ANCHO_PNG_PX)],
                              input=svg.encode("utf-8"), stdout=subprocess.PIPE, check=True)
    except FileNotFoundError:
        raise SystemExit("falta rsvg-convert (librsvg): no se puede exportar el PNG")
    png = con_resolucion(proc.stdout, DPI)
    ancho_px, alto_px = struct.unpack(">II", png[16:24])
    if alto_px > ALTO_MAX_PNG_PX:
        raise SystemExit(f"el PNG mide {alto_px} px de alto: supera el máximo de {ALTO_MAX_PNG_PX}")
    with open(SALIDA_PNG, "wb") as fh:
        fh.write(png)
    return ancho_px, alto_px, hashlib.sha256(png).hexdigest()


# --------------------------------------------------------------------------- #
# Verificación opcional de RESULTADO_BUSQUEDA contra la búsqueda de la app      #
# --------------------------------------------------------------------------- #
def verificar_busqueda(nodos):
    """Corre la misma búsqueda que sirve la app (solo lectura; requiere Neo4j y
    el driver) y comprueba el orden y el estado declarados en RESULTADO_BUSQUEDA."""
    sys.path.insert(0, os.path.join(base.RAIZ, "data/experiment/neo4j"))
    from conexion import abrir_driver
    from neo4j_index import Neo4jIndex
    from harness import _tokens

    driver = abrir_driver()
    indice = Neo4jIndex(driver, grafo="KG_Reextraido_r1", modo="fulltext")
    top = indice.buscar_nodos(PREGUNTA, limite=LIMITE_BUSQUEDA)["resultados"]
    with driver.session() as sesion:
        ranking = [fila["id"] for fila in sesion.run(
            f"CALL db.index.fulltext.queryNodes('{indice.indice}', $q) YIELD node, score "
            "RETURN node.id AS id ORDER BY score DESC, size(node.label) ASC, node.id ASC",
            q=" ".join(_tokens(PREGUNTA)))]
    driver.close()
    if ranking[:LIMITE_BUSQUEDA] != [r["id"] for r in top]:
        raise SystemExit("el ranking completo no coincide con la llamada de la app")

    def posicion(punto):
        for i, nid in enumerate(ranking, start=1):
            nodo = nodos.get(nid)
            if (nodo and nodo["type"] in base.TIPOS_CON_PUNTO
                    and any(p.get("to") == "ext" and p.get("punto") == punto
                            and p.get("rol_documental") == "punto_propio"
                            for p in base.provenances(nodo))):
                return i
        return None

    print(f"\nBÚSQUEDA (índice {indice.indice}, {len(ranking)} resultados con coincidencia)")
    medido = []
    for punto, _ in RESULTADO_BUSQUEDA:
        pos = posicion(punto)
        medido.append((punto, pos))
        print(f"  punto {punto:9s} primera aparición: "
              f"{pos if pos is not None else 'NO APARECE'}")
    orden = sorted(medido, key=lambda t: (t[1] is None, t[1]))
    esperado = [(p, pos is not None and pos <= LIMITE_BUSQUEDA) for p, pos in orden]
    if esperado != RESULTADO_BUSQUEDA:
        raise SystemExit(f"RESULTADO_BUSQUEDA ya no coincide con la búsqueda: {esperado}")
    print("  --> RESULTADO_BUSQUEDA coincide con la búsqueda de la app.")


# --------------------------------------------------------------------------- #
# Composición                                                                  #
# --------------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--svg", metavar="RUTA", help="guarda además el SVG en RUTA")
    ap.add_argument("--verificar-busqueda", action="store_true",
                    help="comprueba RESULTADO_BUSQUEDA contra Neo4j antes de dibujar")
    args = ap.parse_args()

    if puntos_impresos(FS_TEXTO) < PT_MIN_TEXTO:
        raise SystemExit("el texto corrido imprimiría por debajo del mínimo")

    nodos, ids, chunks, aristas = base.cargar()
    if args.verificar_busqueda:
        verificar_busqueda(nodos)

    por_punto = {b["punto"]: b for b in base.bloques_texto(chunks)}
    if sorted(por_punto) != sorted(p for p, _ in RESULTADO_BUSQUEDA):
        raise SystemExit("RESULTADO_BUSQUEDA no cubre exactamente los cuatro puntos")
    bloques = [por_punto[p] for p, _ in RESULTADO_BUSQUEDA]
    estado = dict(RESULTADO_BUSQUEDA)

    # La etiqueta de cada fragmento es la del nodo que la figura rotula con ese
    # punto; se comprueba que ese nodo provenga del punto y que su texto sea el
    # de la disposición que lo origina (misma verificación del generador hermano).
    etiquetas = {}
    for punto, clave in CLAVE_DE_PUNTO.items():
        if base.punto_de_la_figura(nodos[ids[clave]]) != punto:
            raise SystemExit(f"el nodo {clave} no proviene del punto {punto}")
        etiquetas[punto], _ = base.etiqueta_de(nodos, ids[clave])
    filas = base.verificar_correspondencia(nodos, ids, list(por_punto.values()),
                                           base.nodos_por_punto(nodos))
    if not all(fila["ok"] for fila in filas):
        raise SystemExit("FALLA: algún punto no corresponde al nodo dibujado")

    resp_izq, resp_der, condiciones = textos_respuesta(nodos, ids)

    # Alturas.
    lineas_pregunta = [q if q.endswith("?") else q + "?" for q in PREGUNTA.split("? ")]
    alto_pregunta = 8 + FS_ROTULO + 3 + len(lineas_pregunta) * INTERLINEA + 4
    y_pregunta = MARGEN_V
    y_titulos = y_pregunta + alto_pregunta + 34
    y_cols = y_titulos + 9
    disp = disposicion_grafo(nodos, ids)
    alto_cols = max(alto_columna_fragmentos(bloques, estado), disp["alto"])
    y_resp = y_cols + alto_cols + 18
    alto_resp, n_lineas = alto_respuesta([resp_izq, resp_der])
    y_leyenda = y_resp + alto_resp + 8
    alto_leyenda = 70
    alto_total = y_leyenda + alto_leyenda + MARGEN_V

    x_izq = MARGEN
    x_der = MARGEN + ANCHO_COL + SEPARACION

    out = []
    out.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{f(alto_total)}" '
               f'viewBox="0 0 {W} {f(alto_total)}" font-family="{base.TIPOGRAFIA}">')
    out.append(f'<rect width="{W}" height="{f(alto_total)}" fill="white"/>')
    marcadores = ""
    for mid, color in [("arG", base.GRIS_ARISTA), ("arA", base.ACENTO), ("arF", COLOR_FLUJO)]:
        marcadores += (f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
                       f'markerHeight="6" orient="auto-start-reverse"><path d="M0,0L10,5L0,10z" '
                       f'fill="{color}"/></marker>')
    out.append(f'<defs>{marcadores}</defs>')

    # Pregunta común.
    out.append(f'<rect x="{f(MARGEN)}" y="{f(y_pregunta)}" width="{f(ANCHO_TOTAL)}" '
               f'height="{f(alto_pregunta)}" fill="white" stroke="#333" stroke-width="1.4" rx="5"/>')
    out.append(f'<text x="{f(W / 2.0)}" y="{f(y_pregunta + 8 + FS_ROTULO - 2)}" text-anchor="middle" '
               f'font-size="{FS_ROTULO}" font-weight="bold" fill="{base.GRIS_ROTULO}">'
               f'La misma pregunta</text>')
    yl = y_pregunta + 8 + FS_ROTULO + 3 + FS_TEXTO
    for linea in lineas_pregunta:
        out.append(f'<text x="{f(W / 2.0)}" y="{f(yl)}" text-anchor="middle" font-size="{FS_TEXTO}" '
                   f'font-weight="bold" fill="#1f1f1f">{esc(linea)}</text>')
        yl += INTERLINEA

    for x_col, titulo in [(x_izq, "Recuperación por fragmentos"), (x_der, "Consulta del grafo")]:
        out.append(flecha_flujo(x_col + ANCHO_COL / 2.0, y_pregunta + alto_pregunta,
                                y_titulos - FS_TITULO - 3))
        out.append(f'<text x="{f(x_col + ANCHO_COL / 2.0)}" y="{f(y_titulos)}" text-anchor="middle" '
                   f'font-size="{FS_TITULO}" font-weight="bold">{esc(titulo)}</text>')

    out += dibujar_columna_fragmentos(bloques, etiquetas, estado, x_izq, y_cols, alto_cols)
    out += dibujar_columna_grafo(nodos, ids, aristas, disp, x_der, y_cols, alto_cols)

    for x_col in (x_izq, x_der):
        out.append(flecha_flujo(x_col + ANCHO_COL / 2.0, y_cols + alto_cols, y_resp - 3))
    sin_condiciones = [(punto, None) for punto, _ in condiciones]
    out += dibujar_respuesta("Respuesta con lo recuperado", resp_izq, sin_condiciones,
                             False, n_lineas, x_izq, y_resp, alto_resp)
    out += dibujar_respuesta("Respuesta con lo consultado", resp_der, condiciones,
                             True, n_lineas, x_der, y_resp, alto_resp)

    out += dibujar_leyenda(nodos, ids, y_leyenda, alto_leyenda)
    out.append('</svg>')
    svg = "\n".join(out) + "\n"

    ancho_px, alto_px, sha = exportar_png(svg)
    if args.svg:
        with open(args.svg, "w", encoding="utf-8") as fh:
            fh.write(svg)

    # ---------------- informe a stdout (no forma parte de la figura) --------- #
    print(f"PNG: {os.path.relpath(SALIDA_PNG, base.RAIZ)}   {ancho_px} x {alto_px} px a {DPI} dpi "
          f"({ANCHO_IMPRESO_CM} cm x {alto_px / DPI * 2.54:.2f} cm; máximo {ALTO_MAX_PNG_PX} px de alto)")
    print(f"sha256 PNG: {sha}")
    print(f"sha256 SVG: {hashlib.sha256(svg.encode('utf-8')).hexdigest()}   "
          f"({W} x {f(alto_total)} px)")
    print(f"Impresa a {ANCHO_IMPRESO_CM} cm de ancho:")
    for nombre, px in [("texto corrido: pregunta, etiquetas de fragmento, frase, respuestas", FS_TEXTO),
                       ("títulos de columna", FS_TITULO),
                       ("encabezados de recuadro y etiquetas de nodo", FS_NODO),
                       ("rótulos de estado, de paso y de arista; pregunta en la búsqueda", FS_ROTULO),
                       ("leyenda", FS_LEYENDA)]:
        print(f"    {nombre:68s} {px:4.1f} px -> {puntos_impresos(px):5.2f} pt")
    print("\nFRAGMENTOS (orden de la búsqueda)")
    for b in bloques:
        print(f"  punto {b['punto']:9s} {'RECUPERADO   ' if estado[b['punto']] else 'no recuperado'} "
              f"{etiquetas[b['punto']]!r}")
    print("\nARISTAS DIBUJADAS")
    por_id = {ids[k]: k for k in ids}
    for o, r, d in aristas:
        if r != "referencia" and not DIBUJAR_CONTEXTO:
            continue
        print(f"  {por_id[o]:3s} --{base.CASTELLANO.get(r, r):12s}--> {por_id[d]:3s}")
    print("\nRESPUESTAS")
    print(f"  izquierda: {resp_izq}")
    print(f"  derecha:   {resp_der}")
    for punto, etiqueta in condiciones:
        print(f"             - {punto}  {etiqueta}")


if __name__ == "__main__":
    main()
