#!/usr/bin/env python3
"""Figura «la misma pregunta con dos formas de consultar» para la Introducción.

Dos columnas bajo una pregunta común. Izquierda, «Recuperación por fragmentos»:
los dos puntos del ejemplo del préstamo como fragmentos —5.1.1.1, recuperado,
con la frase que remite al punto 3.7 resaltada; 3.7, en gris, fuera de lo
recuperado— con su puesto en la búsqueda léxica, y una línea con los otros
cuatro fragmentos del top-5; debajo, la respuesta que se puede redactar solo con
lo recuperado. Derecha, «Consulta del grafo»: buscar, abrir el nodo de la
restricción del monto y seguir sus aristas —referencia hasta la obligación del
punto 3.7 y limita hasta la operación, que la otra restricción del punto 5.1.1.1
también limita—; debajo, la respuesta con cada condición y su punto.

El lado derecho muestra el camino que el grafo pone al alcance desde el nodo
encontrado; no es la traza de una corrida del agente.

Todos los datos del ejemplo (pregunta, textos, puestos de la búsqueda, nodos y
aristas) se leen de ejemplo_prestamo_datos.json, que escribe
extraer_datos_ejemplo_prestamo.py. Escritos a mano quedan solo los textos de
las dos respuestas (RESPUESTA_*).

Misma técnica que generar_figura_norma_a_grafo.py, del que IMPORTA la carga y
verificación de los datos contra kg.json, las métricas de Helvetica, la paleta y
la leyenda. El SVG se escribe a mano y se exporta a PNG con rsvg-convert, sin
dejar el SVG en el repo (se pasa por stdin). Generación determinística.

Uso:
    PYTHONDONTWRITEBYTECODE=1 python3 docs/tesis/figuras/generar_figura_fragmentos_vs_grafo.py
    PYTHONDONTWRITEBYTECODE=1 python3 docs/tesis/figuras/generar_figura_fragmentos_vs_grafo.py --svg RUTA
    PYTHONDONTWRITEBYTECODE=1 python3 docs/tesis/figuras/generar_figura_fragmentos_vs_grafo.py --verificar-busqueda
"""

import sys

sys.dont_write_bytecode = True  # importar al generador hermano no deja __pycache__

import argparse  # noqa: E402
import hashlib  # noqa: E402
import os  # noqa: E402
import struct  # noqa: E402
import subprocess  # noqa: E402
import zlib  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import generar_figura_norma_a_grafo as base  # noqa: E402

SALIDA_PNG = os.path.join(AQUI, "figura_fragmentos_vs_grafo.png")

# --------------------------------------------------------------------------- #
# Contenido                                                                    #
# --------------------------------------------------------------------------- #
# Recuperación por fragmentos: lo recuperado es el top-5 de la búsqueda léxica
# (busqueda_lexica_fragmentos.py, variante A); los puestos se leen del JSON.
LIMITE_RECUPERACION = 5
FRAGMENTOS = ["cla::5.1.1.1", "cla::3.7"]    # en este orden, de arriba abajo
SUBTITULO_FRAGMENTOS = "Los dos puntos del ejemplo"
ETIQUETA_RECUPERADO = "recuperado · puesto {puesto}"
ETIQUETA_NO_RECUPERADO = "fuera de lo recuperado · puesto {puesto}"
ETIQUETA_RESTO = "resto del top-5: {unidades}"

# Consulta del grafo: el nodo que se abre y las aristas que se siguen, por su
# clave en el JSON; cada arista debe estar en el JSON (y este, en kg.json).
NODO_ENCONTRADO = "restriccion_monto"
ARISTAS_CONSULTA = [
    ("restriccion_monto", "referencia", "obligacion_3_7"),
    ("restriccion_monto", "limita", "operacion"),
    ("restriccion_repago", "limita", "operacion"),
]
NODOS_ALCANZADOS = ["obligacion_3_7", "operacion", "restriccion_repago"]

# Respuestas: los únicos textos del ejemplo escritos a mano en la figura.
RESPUESTA_IZQUIERDA = ("Pasan a la cartera comercial si superan dos veces el importe de "
                       "referencia establecido en el punto 3.7 y su repago depende de la "
                       "actividad productiva o comercial del cliente (punto 5.1.1.1).")
RESPUESTA_IZQUIERDA_FALTA = "el importe de referencia (punto 3.7): no recuperado"
RESPUESTA_DERECHA = ("Pasan a la cartera comercial si se cumplen las dos condiciones "
                     "del punto 5.1.1.1:")
# (nodo del que sale la condición, texto, sangría). La fila se escribe
# «punto · texto», con el punto del nodo leído del JSON y la franja del color de
# su tipo. Las condiciones son dos; la fila del 3.7 no es una tercera sino la
# precisión de la del monto, y va con sangría debajo de ella.
SANGRIA_FILA = 24
RESPUESTA_DERECHA_FILAS = [
    ("restriccion_monto", "superan dos veces el importe de referencia", 0),
    ("obligacion_3_7", "el importe de referencia es el nivel máximo de ventas anuales "
                       "de la categoría Micro del sector Comercio (Ley 24.467)", SANGRIA_FILA),
    ("restriccion_repago", "su repago depende de la actividad productiva o comercial, "
                           "no de ingresos fijos", 0),
]

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
# Tope de alto: 1700 px en la versión anterior; el contenido de este ejemplo
# (textos completos de los dos puntos, etiquetas sin abreviar) no entra, y el
# contenido no se recorta: el tope sube a 1850 px.
ALTO_MAX_PNG_PX = 1850
PT_MIN_TEXTO = 7.0

GRIS_TEXTO_APAGADO = "#9a9a9a"
GRIS_BORDE_APAGADO = "#bdbdbd"
FONDO_APAGADO = "#f1f1f1"
COLOR_FLUJO = "#555"

ancho, envolver, esc, f = base.ancho, base.envolver, base.esc, base.f
ancho_negrita = base.ancho_negrita


def puntos_impresos(px):
    return px * (ANCHO_IMPRESO_CM * base.PT_POR_CM) / W


def miles(n):
    """Entero con punto de miles: 1523 -> «1.523»."""
    return f"{n:,}".replace(",", ".")


# --------------------------------------------------------------------------- #
# Piezas                                                                       #
# --------------------------------------------------------------------------- #
def panel(x, y, w, h):
    return (f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" '
            f'fill="{base.FONDO_PANEL}" stroke="{base.BORDE_PANEL}" rx="5"/>')


def flecha_flujo(x, y1, y2):
    return (f'<path d="M{f(x)},{f(y1)} L{f(x)},{f(y2)}" fill="none" stroke="{COLOR_FLUJO}" '
            f'stroke-width="1.5" marker-end="url(#arF)"/>')


def texto_estilado(partes, texto, estilo, lineas, x, y, tinta, tinta_resaltado):
    """Dibuja `lineas` (de base.envolver_estilos) con el número de punto en
    negrita y el tramo resaltado sobre fondo de acento. `y` es la primera línea
    base."""
    for linea, desplazamiento in lineas:
        segmentos, actual, marca = [], "", None
        for k, ch in enumerate(linea):
            m = estilo[desplazamiento + k]
            if marca is None:
                marca = m
            if m != marca:
                segmentos.append((actual, marca))
                actual, marca = "", m
            actual += ch
        if actual:
            segmentos.append((actual, marca))
        xc = x
        for seg, m in segmentos:
            aseg = ancho_negrita(seg, FS_TEXTO) if m else ancho(seg, FS_TEXTO)
            if m == "R" and seg.strip():
                partes.append(f'<rect x="{f(xc - 1)}" y="{f(y - FS_TEXTO + 2)}" '
                              f'width="{f(aseg + 2)}" height="{f(FS_TEXTO + 5)}" '
                              f'fill="{base.ACENTO}" opacity="0.26" rx="2"/>')
            xc += aseg
        tspans = ""
        for seg, m in segmentos:
            if m == "R":
                tspans += f'<tspan font-weight="bold" fill="{tinta_resaltado}">{esc(seg)}</tspan>'
            elif m == "N":
                tspans += f'<tspan font-weight="bold">{esc(seg)}</tspan>'
            else:
                tspans += f'<tspan>{esc(seg)}</tspan>'
        partes.append(f'<text x="{f(x)}" y="{f(y)}" font-size="{FS_TEXTO}" fill="{tinta}" '
                      f'xml:space="preserve">{tspans}</text>')
        y += INTERLINEA


# Fragmento: la marca de estado en la primera línea y debajo el texto del punto,
# que empieza con su número (en negrita); el recuperado lleva además la frase
# de remisión resaltada.
LINEA_MARCA = 24           # del borde superior a la línea base de la marca
SALTO_TEXTO = 28           # de la marca a la primera línea del texto
PIE_FRAGMENTO = 12         # de la última línea del texto al borde inferior
GAP_FRAGMENTOS = 12
ALTO_SUBTITULO = 22
ALTO_RESTO = 30


def bloque_fragmento(datos, cid, recuperado):
    t = datos["textos"][cid]
    b = {"texto": t["texto"], "unidad": t["unidad"],
         "resaltar": datos["textos"]["frase_resaltada"] if recuperado else None}
    if b["resaltar"] and b["resaltar"] not in b["texto"]:
        raise SystemExit(f"la frase resaltada no está en el texto de {cid}")
    return b


def lineas_fragmento(b, w):
    return base.envolver_estilos(b["texto"], base.estilo_de(b), FS_TEXTO, w - 2 * PAD)


def alto_fragmento(b, w):
    return LINEA_MARCA + SALTO_TEXTO + (len(lineas_fragmento(b, w)) - 1) * INTERLINEA + PIE_FRAGMENTO


def dibujar_fragmento(b, puesto, recuperado, x, y, w):
    partes = []
    alto = alto_fragmento(b, w)
    if recuperado:
        partes.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(alto)}" '
                      f'fill="white" stroke="#333" stroke-width="1.8" rx="4"/>')
        partes.append(f'<text x="{f(x + PAD)}" y="{f(y + LINEA_MARCA)}" '
                      f'font-size="{FS_ROTULO}" font-weight="bold" fill="#333">'
                      f'{esc(ETIQUETA_RECUPERADO.format(puesto=miles(puesto)))}</text>')
    else:
        partes.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(alto)}" '
                      f'fill="{FONDO_APAGADO}" stroke="{GRIS_BORDE_APAGADO}" '
                      f'stroke-width="1.0" stroke-dasharray="5,4" rx="4"/>')
        partes.append(f'<text x="{f(x + PAD)}" y="{f(y + LINEA_MARCA)}" '
                      f'font-size="{FS_ROTULO}" font-style="italic" fill="{base.GRIS_ROTULO}">'
                      f'{esc(ETIQUETA_NO_RECUPERADO.format(puesto=miles(puesto)))}</text>')
    texto_estilado(partes, b["texto"], base.estilo_de(b), lineas_fragmento(b, w),
                   x + PAD, y + LINEA_MARCA + SALTO_TEXTO,
                   "#1f1f1f" if recuperado else GRIS_TEXTO_APAGADO, base.ACENTO_TEXTO)
    return partes, alto


def alto_columna_fragmentos(bloques):
    w = ANCHO_COL - 2 * PAD
    total = PAD_V + ALTO_SUBTITULO
    total += sum(alto_fragmento(b, w) for b, _, _ in bloques)
    total += GAP_FRAGMENTOS * (len(bloques) - 1)
    return total + ALTO_RESTO + PAD_V


def dibujar_columna_fragmentos(bloques, resto, x0, y0, alto):
    partes = [panel(x0, y0, ANCHO_COL, alto)]
    partes.append(f'<text x="{f(x0 + PAD)}" y="{f(y0 + PAD_V + 12)}" font-size="{FS_ROTULO}" '
                  f'font-weight="bold" fill="#444">{esc(SUBTITULO_FRAGMENTOS)}</text>')
    y = y0 + PAD_V + ALTO_SUBTITULO
    for b, puesto, recuperado in bloques:
        piezas, h = dibujar_fragmento(b, puesto, recuperado, x0 + PAD, y, ANCHO_COL - 2 * PAD)
        partes += piezas
        y += h + GAP_FRAGMENTOS
    linea = ETIQUETA_RESTO.format(unidades=" · ".join(resto))
    if ancho(linea, FS_ROTULO) > ANCHO_COL - 2 * PAD:
        raise SystemExit("la línea del resto del top-5 no entra en la columna")
    partes.append(f'<text x="{f(x0 + PAD)}" y="{f(y - GAP_FRAGMENTOS + ALTO_RESTO - 6)}" '
                  f'font-size="{FS_ROTULO}" fill="#444">{esc(linea)}</text>')
    return partes


def alto_nodo(nodo, w):
    return len(base.lineas_nodo(nodo, w - 22, FS_NODO)) * PASO_NODO + 8


def dibujar_nodo(nodo, cx, cy, w, h):
    """Mismo estilo de nodo que la figura «de la norma al grafo»."""
    focal = nodo["type"] in base.TIPOS_FOCALES
    color = base.COLOR_TIPO[nodo["type"]]
    partes = [f'<rect x="{f(cx - w / 2)}" y="{f(cy - h / 2)}" width="{f(w)}" height="{f(h)}" '
              f'fill="{color}" fill-opacity="{"0.95" if focal else "0.45"}" '
              f'stroke="{"black" if focal else "#777"}" '
              f'stroke-width="{"1.8" if focal else "1.1"}" rx="7"/>']
    lineas = base.lineas_nodo(nodo, w - 22, FS_NODO)
    ytxt = cy - (len(lineas) - 1) * PASO_NODO / 2.0 + 6
    for linea, es_punto in lineas:
        partes.append(f'<text x="{f(cx)}" y="{f(ytxt)}" text-anchor="middle" '
                      f'font-size="{FS_NODO}" font-weight="{"bold" if es_punto else "normal"}" '
                      f'fill="{"white" if focal else "#222"}">{esc(linea)}</text>')
        ytxt += PASO_NODO
    return partes


# Disposición del panel de la consulta (coordenadas relativas a su esquina).
# Las alturas salen del número de líneas de cada elemento; solo los anchos y
# las separaciones son fijos.
X_PILDORA, ANCHO_PILDORA = 14, 368
X_R, ANCHO_R = 14, 320
# El tramo horizontal de la arista referencia (de TRONCO_REMISION a X_NODO)
# tiene que alojar su rótulo en negrita, más largo que el «remite a» anterior.
X_NODO, ANCHO_NODO = 118, 264
TRONCO_REMISION = 34     # x del tronco de la arista referencia
TRONCO_CONTEXTO = 20     # x del tronco de la arista limita que sale del nodo abierto
X_FLECHA_BUSQUEDA = 300
SALTO_PASO = 18          # de un elemento a la línea base del rótulo del paso siguiente
BAJO_PASO = 8            # del rótulo del paso al elemento que encabeza
GAP_NODOS = 6
GAP_VERTICAL = 40        # entre dos nodos unidos por una arista vertical


def disposicion_grafo(datos):
    """Posiciones verticales del panel de la consulta y su alto total."""
    nodos = datos["grafo"]["nodos"]
    d = {"pasos": {}, "cajas": {}}
    y = PAD_V + 13
    d["pasos"][1] = (PAD + 4, y)
    lineas = envolver(datos["pregunta"], FS_ROTULO, ANCHO_PILDORA - 44)
    y += BAJO_PASO
    d["pildora"] = {"y": y, "h": len(lineas) * PASO_ROTULO + 12, "lineas": lineas}
    y += d["pildora"]["h"] + SALTO_PASO
    d["pasos"][2] = (PAD + 4, y)
    y += BAJO_PASO
    h = alto_nodo(nodos[NODO_ENCONTRADO], ANCHO_R)
    d["cajas"][NODO_ENCONTRADO] = {"cx": X_R + ANCHO_R / 2.0, "cy": y + h / 2.0,
                                   "w": ANCHO_R, "h": h}
    y += h + SALTO_PASO
    d["pasos"][3] = (X_NODO, y)
    y += BAJO_PASO
    anterior = None
    for clave in NODOS_ALCANZADOS:
        if anterior is not None:
            vertical = any(a == clave and b == anterior for a, _, b in ARISTAS_CONSULTA)
            y += GAP_VERTICAL if vertical else GAP_NODOS
        h = alto_nodo(nodos[clave], ANCHO_NODO)
        d["cajas"][clave] = {"cx": X_NODO + ANCHO_NODO / 2.0, "cy": y + h / 2.0,
                             "w": ANCHO_NODO, "h": h}
        y += h
        anterior = clave
    d["alto"] = y + PAD_V
    return d


def dibujar_columna_grafo(datos, disp, x0, y0, alto):
    nodos = datos["grafo"]["nodos"]
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
    r = cajas[NODO_ENCONTRADO]
    partes.append(paso(2, "2 · Abrir el nodo encontrado"))
    partes.append(flecha_flujo(x0 + X_FLECHA_BUSQUEDA, y0 + p["y"] + p["h"],
                               y0 + r["cy"] - r["h"] / 2.0 - 3))

    # Paso 3: seguir las aristas. Las que salen del nodo abierto bajan por un
    # tronco a la izquierda y entran por el costado del nodo de destino; la que
    # une dos nodos alcanzados va en vertical entre ellos.
    partes.append(paso(3, "3 · Seguir las aristas"))
    y_salida = y0 + r["cy"] + r["h"] / 2.0
    rotulos = []
    for origen, relacion, destino in ARISTAS_CONSULTA:
        remision = (relacion == base.RELACION_RESALTADA)
        color = base.ACENTO if remision else base.GRIS_ARISTA
        extra = "" if remision else ' stroke-dasharray="4,4"'
        cb = cajas[destino]
        if origen == NODO_ENCONTRADO:
            tx = x0 + (TRONCO_REMISION if remision else TRONCO_CONTEXTO)
            x_llegada = x0 + cb["cx"] - cb["w"] / 2.0 - 2
            cy = y0 + cb["cy"]
            d = f"M{f(tx)},{f(y_salida)} L{f(tx)},{f(cy)} L{f(x_llegada)},{f(cy)}"
            rotulos.append(((tx + x_llegada) / 2.0, cy - 12, relacion, remision))
            at =ancho_negrita(relacion, FS_ROTULO) if remision else ancho(relacion, FS_ROTULO)
            if at + 8 > x_llegada - tx:
                raise SystemExit(f"el rótulo {relacion!r} no entra en el tramo horizontal")
        else:
            ca = cajas[origen]
            if ca["cx"] != cb["cx"]:
                raise SystemExit(f"arista sin trazado definido: {origen} -> {destino}")
            x = x0 + ca["cx"]
            y_ini = y0 + ca["cy"] - ca["h"] / 2.0
            y_fin = y0 + cb["cy"] + cb["h"] / 2.0 + 2
            d = f"M{f(x)},{f(y_ini)} L{f(x)},{f(y_fin)}"
            rotulos.append((x, (y_ini + y_fin) / 2.0 + 5, relacion, remision))
        partes.append(f'<path d="{d}" fill="none" stroke="{color}" '
                      f'stroke-width="{"2.6" if remision else "1.5"}"{extra} stroke-linejoin="round" '
                      f'marker-end="url(#{"arA" if remision else "arG"})"/>')
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
        partes += dibujar_nodo(nodos[clave], x0 + c["cx"], y0 + c["cy"], c["w"], c["h"])
    return partes


# --------------------------------------------------------------------------- #
# Respuestas                                                                   #
# --------------------------------------------------------------------------- #
ALTO_FILA = 26
GAP_FILA = 4
X_TEXTO_FILA = 14       # del borde de la fila al texto (a la derecha de la franja)
X_TEXTO_FALTA = 34      # ídem, a la derecha de la cruz


def filas_derecha(datos):
    """(texto de la fila, largo del número de punto, tipo del nodo, sangría)."""
    nodos = datos["grafo"]["nodos"]
    filas = []
    for clave, texto, sangria in RESPUESTA_DERECHA_FILAS:
        punto = nodos[clave]["punto"]
        filas.append((f"{punto} · {texto}", len(punto), nodos[clave]["type"], sangria))
    return filas


def lineas_fila(texto, n_negrita, x_texto, sangria=0):
    estilo = ["N"] * n_negrita + [""] * (len(texto) - n_negrita)
    return base.envolver_estilos(texto, estilo, FS_TEXTO,
                                 ANCHO_COL - 2 * PAD - sangria - x_texto - 6), estilo


def alto_filas(filas, x_texto):
    return sum(ALTO_FILA + (len(lineas_fila(t, n, x_texto, sg)[0]) - 1) * INTERLINEA + GAP_FILA
               for t, n, _, sg in filas) - GAP_FILA


def alto_respuesta(entrada, filas, x_texto):
    n = len(envolver(entrada, FS_TEXTO, ANCHO_COL - 2 * PAD))
    return (PAD_V + FS_ENCABEZADO + 6 + n * INTERLINEA + 6
            + alto_filas(filas, x_texto) + PAD_V)


def dibujar_respuesta(titulo, entrada, filas, completas, x0, y0, alto):
    partes = [panel(x0, y0, ANCHO_COL, alto)]
    partes.append(f'<text x="{f(x0 + PAD)}" y="{f(y0 + PAD_V + FS_ENCABEZADO - 2)}" '
                  f'font-size="{FS_ENCABEZADO}" font-weight="bold" fill="#333">{esc(titulo)}</text>')
    yl = y0 + PAD_V + FS_ENCABEZADO + 6 + FS_TEXTO
    lineas = envolver(entrada, FS_TEXTO, ANCHO_COL - 2 * PAD)
    for linea, _ in lineas:
        partes.append(f'<text x="{f(x0 + PAD)}" y="{f(yl)}" font-size="{FS_TEXTO}" '
                      f'fill="#1f1f1f">{esc(linea)}</text>')
        yl += INTERLINEA
    y = y0 + PAD_V + FS_ENCABEZADO + 6 + len(lineas) * INTERLINEA + 6
    x_texto = X_TEXTO_FILA if completas else X_TEXTO_FALTA
    for texto, n_negrita, tipo, sangria in filas:
        x, w = x0 + PAD + sangria, ANCHO_COL - 2 * PAD - sangria
        lf, estilo = lineas_fila(texto, n_negrita, x_texto, sangria)
        h = ALTO_FILA + (len(lf) - 1) * INTERLINEA
        y_txt = y + ALTO_FILA / 2.0 + 6
        if completas:
            partes.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" '
                          f'fill="white" stroke="#d8d8d8" rx="4"/>')
            partes.append(f'<rect x="{f(x)}" y="{f(y)}" width="6" height="{f(h)}" '
                          f'fill="{base.COLOR_TIPO[tipo]}" rx="2"/>')
            texto_estilado(partes, texto, estilo, lf, x + x_texto, y_txt, "#1f1f1f",
                           base.ACENTO_TEXTO)
        else:
            cy = y + ALTO_FILA / 2.0
            partes.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" '
                          f'fill="none" stroke="{GRIS_BORDE_APAGADO}" stroke-width="1.2" '
                          f'stroke-dasharray="5,4" rx="4"/>')
            for dx1, dy1, dx2, dy2 in [(-5, -5, 5, 5), (-5, 5, 5, -5)]:
                partes.append(f'<path d="M{f(x + 19 + dx1)},{f(cy + dy1)} L{f(x + 19 + dx2)},{f(cy + dy2)}" '
                              f'stroke="{base.GRIS_ROTULO}" stroke-width="2"/>')
            for linea, _ in lf:
                partes.append(f'<text x="{f(x + x_texto)}" y="{f(y_txt)}" font-size="{FS_TEXTO}" '
                              f'font-style="italic" fill="{base.GRIS_ROTULO}">{esc(linea)}</text>')
                y_txt += INTERLINEA
        y += h + GAP_FILA
    return partes


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
# Verificación opcional de los puestos contra la búsqueda léxica               #
# --------------------------------------------------------------------------- #
def verificar_busqueda(datos):
    """Vuelve a correr la búsqueda léxica sobre los fragmentos de E0 (solo
    lectura, sin Neo4j ni API) y comprueba el top-5 y los puestos del JSON."""
    import busqueda_lexica_fragmentos as bl
    ids, textos, shas = bl.cargar_fragmentos()
    orden, rango, *_ = bl.bm25(ids, textos, datos["pregunta"])
    bf = datos["busqueda_fragmentos"]
    if shas != bf["sha256_insumos"]:
        raise SystemExit("los fragmentos de E0 no son los del JSON")
    top = [ids[i] for i, _ in orden[:LIMITE_RECUPERACION]]
    if top != [t["chunk_id"] for t in bf["top5"]]:
        raise SystemExit(f"el top-5 ya no coincide con el JSON: {top}")
    for cid in FRAGMENTOS:
        if rango.get(cid) != bf["objetivos"][cid]["rango"]:
            raise SystemExit(f"el puesto de {cid} ya no coincide con el JSON: {rango.get(cid)}")
    print(f"\nBÚSQUEDA (BM25 sobre {len(ids)} fragmentos, recalculada): top-5 {top}; "
          + ", ".join(f"{cid} puesto {rango.get(cid)}" for cid in FRAGMENTOS)
          + "\n  --> coincide con ejemplo_prestamo_datos.json.")


# --------------------------------------------------------------------------- #
# Composición                                                                  #
# --------------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--svg", metavar="RUTA", help="guarda además el SVG en RUTA")
    ap.add_argument("--verificar-busqueda", action="store_true",
                    help="recalcula la búsqueda léxica y la compara con el JSON antes de dibujar")
    args = ap.parse_args()

    if puntos_impresos(FS_TEXTO) < PT_MIN_TEXTO:
        raise SystemExit("el texto corrido imprimiría por debajo del mínimo")

    datos = base.cargar_datos()
    if args.verificar_busqueda:
        verificar_busqueda(datos)
    nodos = datos["grafo"]["nodos"]
    en_json = {(a["origen"], a["relation"], a["destino"]) for a in datos["grafo"]["aristas"]}
    for arista in ARISTAS_CONSULTA:
        if arista not in en_json:
            raise SystemExit(f"arista de la consulta ausente del JSON: {arista}")

    # Fragmentos: puesto y estado de cada uno, y el resto del top-5.
    bf = datos["busqueda_fragmentos"]
    if len(bf["top5"]) != LIMITE_RECUPERACION:
        raise SystemExit("el JSON no trae el top-5 completo")
    bloques = []
    for cid in FRAGMENTOS:
        puesto = bf["objetivos"][cid]["rango"]
        recuperado = puesto is not None and puesto <= LIMITE_RECUPERACION
        bloques.append((bloque_fragmento(datos, cid, recuperado), puesto, recuperado))
    resto = [t["unidad"] for t in bf["top5"] if t["chunk_id"] not in FRAGMENTOS]
    if len(resto) != LIMITE_RECUPERACION - sum(1 for _, _, r in bloques if r):
        raise SystemExit("el resto del top-5 no suma cinco con los fragmentos recuperados")

    filas_izq = [(RESPUESTA_IZQUIERDA_FALTA, 0, None, 0)]
    filas_der = filas_derecha(datos)

    # Alturas.
    ancho_pregunta = ANCHO_TOTAL - 2 * PAD
    pregunta = datos["pregunta"]
    lineas_pregunta = base.envolver_estilos(pregunta, ["N"] * len(pregunta), FS_TEXTO,
                                            ancho_pregunta)
    alto_pregunta = 8 + FS_ROTULO + 3 + len(lineas_pregunta) * INTERLINEA + 4
    y_pregunta = MARGEN_V
    y_titulos = y_pregunta + alto_pregunta + 34
    y_cols = y_titulos + 9
    disp = disposicion_grafo(datos)
    alto_cols = max(alto_columna_fragmentos(bloques), disp["alto"])
    y_resp = y_cols + alto_cols + 18
    alto_resp = max(alto_respuesta(RESPUESTA_IZQUIERDA, filas_izq, X_TEXTO_FALTA),
                    alto_respuesta(RESPUESTA_DERECHA, filas_der, X_TEXTO_FILA))
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
    for linea, _ in lineas_pregunta:
        out.append(f'<text x="{f(W / 2.0)}" y="{f(yl)}" text-anchor="middle" font-size="{FS_TEXTO}" '
                   f'font-weight="bold" fill="#1f1f1f">{esc(linea)}</text>')
        yl += INTERLINEA

    for x_col, titulo in [(x_izq, "Recuperación por fragmentos"), (x_der, "Consulta del grafo")]:
        out.append(flecha_flujo(x_col + ANCHO_COL / 2.0, y_pregunta + alto_pregunta,
                                y_titulos - FS_TITULO - 3))
        out.append(f'<text x="{f(x_col + ANCHO_COL / 2.0)}" y="{f(y_titulos)}" text-anchor="middle" '
                   f'font-size="{FS_TITULO}" font-weight="bold">{esc(titulo)}</text>')

    out += dibujar_columna_fragmentos(bloques, resto, x_izq, y_cols, alto_cols)
    out += dibujar_columna_grafo(datos, disp, x_der, y_cols, alto_cols)

    for x_col in (x_izq, x_der):
        out.append(flecha_flujo(x_col + ANCHO_COL / 2.0, y_cols + alto_cols, y_resp - 3))
    out += dibujar_respuesta("Respuesta con lo recuperado", RESPUESTA_IZQUIERDA, filas_izq,
                             False, x_izq, y_resp, alto_resp)
    out += dibujar_respuesta("Respuesta con lo consultado", RESPUESTA_DERECHA, filas_der,
                             True, x_der, y_resp, alto_resp)

    dibujados = [NODO_ENCONTRADO] + NODOS_ALCANZADOS
    out += base.dibujar_leyenda(base.tipos_presentes(nodos, dibujados), y_leyenda,
                                alto_leyenda, FS_LEYENDA)
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
    for nombre, px in [("texto corrido: pregunta, fragmentos, respuestas", FS_TEXTO),
                       ("títulos de columna", FS_TITULO),
                       ("encabezados de respuesta y etiquetas de nodo", FS_NODO),
                       ("marcas, pasos, rótulos de arista; pregunta en la búsqueda", FS_ROTULO),
                       ("leyenda", FS_LEYENDA)]:
        print(f"    {nombre:60s} {px:4.1f} px -> {puntos_impresos(px):5.2f} pt")
    print(f"\nalto de las columnas: fragmentos {alto_columna_fragmentos(bloques):.0f}, "
          f"consulta {disp['alto']:.0f}")
    print("\nFRAGMENTOS")
    for b, puesto, recuperado in bloques:
        print(f"  {b['unidad']:9s} {'RECUPERADO   ' if recuperado else 'no recuperado'} puesto {miles(puesto)}")
    print(f"  resto del top-5: {resto}")
    print("\nARISTAS DIBUJADAS")
    for o, r, d in ARISTAS_CONSULTA:
        print(f"  {o} --{r}--> {d}")
    print("\nRESPUESTAS")
    print(f"  izquierda: {RESPUESTA_IZQUIERDA}")
    print(f"             ✗ {RESPUESTA_IZQUIERDA_FALTA}")
    print(f"  derecha:   {RESPUESTA_DERECHA}")
    for texto, _, tipo, sangria in filas_der:
        print(f"             - {'  ' if sangria else ''}{texto}   [{tipo}; sangría {sangria} px]")


if __name__ == "__main__":
    main()
