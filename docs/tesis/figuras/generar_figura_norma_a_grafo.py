#!/usr/bin/env python3
"""Figura «de la norma al grafo» para la Introducción.

Panel superior: texto de los puntos del ejemplo del préstamo —en gris la frase
de la unidad 5.1.1 que los encabeza; debajo el punto 5.1.1.1, con resaltada la
frase que remite al punto 3.7, y el punto 3.7—.
Panel inferior: los cinco nodos y las cuatro aristas que la extracción produjo a
partir de ellos, con la remisión resaltada.

Todos los datos del ejemplo (textos, nodos, aristas) se leen de
ejemplo_prestamo_datos.json, que escribe extraer_datos_ejemplo_prestamo.py; el
script comprueba además contra kg.json (sha256 declarado en el JSON) que cada
nodo y cada arista estén en el grafo antes de dibujar.

Sin dependencias externas: escribe el SVG a mano (misma técnica, tipografía y
paleta que la figura de la cláusula del 125 %). Generación determinística: dos
corridas sobre las mismas fuentes producen el mismo SVG byte a byte.

Uso:
    PYTHONDONTWRITEBYTECODE=1 python3 docs/tesis/figuras/generar_figura_norma_a_grafo.py
"""

import hashlib
import json
import os

# --------------------------------------------------------------------------- #
# Fuentes de datos                                                             #
# --------------------------------------------------------------------------- #
AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", ".."))
DATOS = os.path.join(AQUI, "ejemplo_prestamo_datos.json")
SALIDA_SVG = os.path.join(AQUI, "figura_norma_a_grafo.svg")

# Composición del panel superior: (clave del texto en el JSON, recuadro,
# sangría en px). La frase de la unidad 5.1.1 termina en «con excepción de las
# siguientes:», así que el punto 3.7 no puede quedar debajo de ella como si
# fuera otra excepción de la lista: el recuadro de 5.1.1.1 va con sangría bajo la
# frase, y el de 3.7 vuelve al nivel de la frase, separado por una línea «[…]»
# (texto del documento que no se muestra). None marca esa línea.
SANGRIA_PUNTO = 32
OMISION = "[…]"
COMPOSICION_TEXTO = [
    ("cla::5.1.1", False, 0),                 # frase que encabeza, en gris
    ("cla::5.1.1.1", True, SANGRIA_PUNTO),    # punto de la lista, con sangría
    (None, False, 0),                         # «[…]»
    ("cla::3.7", True, 0),                    # punto de otra sección
]

# Composición del panel del grafo: (clave del nodo en el JSON, columna, fila).
# Qué nodos y aristas hay se lee del JSON y se comprueba en kg.json; esta tabla
# solo decide dónde se dibuja cada nodo. Las aristas se trazan rectas: en
# horizontal entre nodos de la misma fila y en vertical entre nodos de la misma
# columna.
DISPOSICION = [
    ("restriccion_monto", "izq", 0),
    ("obligacion_3_7", "der", 0),
    ("operacion", "izq", 1),
    ("sujeto", "der", 1),
    ("restriccion_repago", "izq", 2),
]
COLUMNAS = {"izq": {"cx": 190, "w": 322}, "der": {"cx": 620, "w": 336}}

# Convención de foco de la versión anterior: los nodos de contenido con las
# condiciones del caso, opacos con texto blanco; la operación y el sujeto, como
# contexto, translúcidos con texto oscuro.
TIPOS_FOCALES = ("Restriccion", "Obligacion", "Excepcion")
# Solo los nodos de contenido provienen de un punto del Texto Ordenado. Los de
# catálogo (Sujeto) son estructura: su procedencia enumera decenas de puntos y
# no tienen «su» punto, así que se dibujan sin número.
TIPOS_CON_PUNTO = ("Obligacion", "Restriccion", "Excepcion", "Operacion")
ORDEN_TIPOS = ["Restriccion", "Obligacion", "Operacion", "Sujeto"]
RELACION_RESALTADA = "referencia"

MAX_ETIQUETA = 40   # caracteres por línea visible de una etiqueta de nodo

# --------------------------------------------------------------------------- #
# Paleta y tipografía (idénticas a la figura de la cláusula del 125 %)         #
# --------------------------------------------------------------------------- #
TIPOGRAFIA = "Helvetica,Arial,sans-serif"
COLOR_TIPO = {
    "Excepcion": "#e07b39",
    "Restriccion": "#b23a48",
    "Obligacion": "#2a6f97",
    "Operacion": "#52796f",
    "Sujeto": "#6d597a",
    "TextoOrdenado": "#3d3d3d",
}
ACENTO = "#e07b39"        # resaltado: frase del texto y aristas de remisión
ACENTO_TEXTO = "#8a4513"  # el mismo tono, oscurecido para leer sobre el marcador
GRIS_ARISTA = "#8a8a8a"
GRIS_ROTULO = "#6f6f6f"
BORDE_PANEL = "#ccc"
FONDO_PANEL = "#fafafa"

# --------------------------------------------------------------------------- #
# Geometría: paneles apilados a ancho completo.                                #
# El ancho total está acotado por el tamaño mínimo de letra impresa: a 15 cm de #
# ancho de página, FS_TEXTO píxeles miden FS_TEXTO * 425.2 / W puntos, y ese    #
# número no puede bajar de 8.                                                   #
# --------------------------------------------------------------------------- #
W = 860
MARGEN = 24
ANCHO_PANEL = W - 2 * MARGEN            # 812
PAD_PANEL = 18
ANCHO_PAGINA_CM = 15.0
PT_POR_CM = 72.0 / 2.54                 # 28,3465 pt/cm

FS_TITULO_PANEL = 17
FS_TEXTO = 17
FS_ENCABEZADO = 15
FS_NODO = 15
FS_ROTULO = 13
FS_LEYENDA = 13
INTERLINEA = 24


def puntos_impresos(px):
    """Tamaño en puntos que tendrá `px` píxeles al imprimir la figura a 15 cm."""
    return px * (ANCHO_PAGINA_CM * PT_POR_CM) / W


# --------------------------------------------------------------------------- #
# Métricas de Helvetica (unidades/1000 em), para envolver texto y ubicar los    #
# rectángulos de resaltado sin depender de librerías de tipografía.            #
# --------------------------------------------------------------------------- #
_W = {
    " ": 278, "!": 278, '"': 355, "#": 556, "$": 556, "%": 889, "&": 667,
    "'": 191, "(": 333, ")": 333, "*": 389, "+": 584, ",": 278, "-": 333,
    ".": 278, "/": 278, ":": 278, ";": 278, "?": 556, "@": 1015,
    "[": 278, "]": 278, "_": 556, "«": 500, "»": 500, "—": 1000, "–": 556,
    "“": 333, "”": 333, "‘": 222, "’": 222, "…": 1000,
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
    """Ancho en px de `texto` a tamaño `fs`. Helvetica Bold es ~4 % más ancha."""
    total = sum(_W.get(c, 556) for c in texto)
    return total / 1000.0 * fs * (1.04 if negrita else 1.0)


# Anchos de Helvetica Bold (unidades/1000 em) donde difieren de la redonda. El
# 4 % de `ancho` queda corto para la minúscula (~10 % más ancha en negrita): el
# texto con tramos en negrita se mide con esta tabla para envolverlo y para
# ubicar el rectángulo del resaltado.
_WB = {"!": 333, '"': 474, "&": 722, "'": 238, ":": 333, ";": 333, "?": 611, "@": 975,
       "A": 722, "B": 722, "J": 556, "K": 722, "L": 611,
       "b": 611, "c": 556, "d": 611, "f": 333, "g": 611, "h": 611, "i": 278, "j": 278,
       "k": 556, "l": 278, "m": 889, "n": 611, "o": 611, "p": 611, "q": 611, "r": 389,
       "s": 556, "t": 333, "u": 611, "v": 556, "w": 778, "x": 556, "y": 556,
       "í": 278, "ó": 611, "ú": 611, "ñ": 611, "ü": 611}


def ancho_negrita(texto, fs):
    return sum(_WB.get(c, _W.get(c, 556)) for c in texto) / 1000.0 * fs


def envolver_estilos(texto, estilo, fs, ancho_max):
    """Envuelve por palabras midiendo en negrita los caracteres con estilo.
    Devuelve lista de (linea, indice_inicio), como `envolver`."""
    def medida(ini, fin):
        return sum(_WB.get(c, _W.get(c, 556)) if estilo[k] else _W.get(c, 556)
                   for k, c in zip(range(ini, fin), texto[ini:fin])) / 1000.0 * fs
    lineas, ini, fin, cursor = [], 0, None, 0
    for palabra in texto.split(" "):
        inicio_palabra, fin_palabra = cursor, cursor + len(palabra)
        if fin is not None and medida(ini, fin_palabra) > ancho_max:
            lineas.append((texto[ini:fin], ini))
            ini = inicio_palabra
        fin = fin_palabra
        cursor = fin_palabra + 1
    if fin is not None:
        lineas.append((texto[ini:fin], ini))
    return lineas


def envolver(texto, fs, ancho_max, negrita=False):
    """Envuelve por palabras. Devuelve lista de (linea, indice_inicio)."""
    lineas, actual, inicio, cursor = [], "", 0, 0
    for palabra in texto.split(" "):
        cand = palabra if not actual else actual + " " + palabra
        if actual and ancho(cand, fs, negrita) > ancho_max:
            lineas.append((actual, inicio))
            inicio = cursor
            actual = palabra
        else:
            actual = cand
        cursor += len(palabra) + 1
    if actual:
        lineas.append((actual, inicio))
    return lineas


def esc(t):
    return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def f(v):
    """Formato fijo: el SVG no debe depender de la representación del float."""
    return f"{v:.1f}"


# --------------------------------------------------------------------------- #
# Carga y verificación                                                         #
# --------------------------------------------------------------------------- #
def provenances(elem):
    ps = ([elem["provenance"]] if elem.get("provenance") else []) + (elem.get("provenances") or [])
    vistos, salida = set(), []
    for p in ps:
        clave = (p.get("to"), p.get("punto"), p.get("rol_documental"))
        if clave not in vistos:
            vistos.add(clave)
            salida.append(p)
    return salida


def puntos_propios(elem):
    return [p["punto"] for p in provenances(elem)
            if p.get("rol_documental") == "punto_propio" and p.get("punto")]


def cargar_datos():
    """Lee ejemplo_prestamo_datos.json y comprueba contra kg.json, cuyo sha256
    debe ser el declarado en el JSON, que cada nodo (id, tipo, etiqueta) y cada
    arista (índice, origen, relación, destino) estén en el grafo. Si algo no
    está, el script se detiene sin dibujar."""
    with open(DATOS, encoding="utf-8") as fh:
        datos = json.load(fh)
    fuente = datos["fuentes"]["kg"]
    with open(os.path.join(RAIZ, fuente["ruta"]), "rb") as fh:
        crudo = fh.read()
    sha = hashlib.sha256(crudo).hexdigest()
    if sha != fuente["sha256"]:
        raise SystemExit(f"kg.json no es el del JSON: sha {sha[:12]}… ≠ {fuente['sha256'][:12]}…")
    kg = json.loads(crudo.decode("utf-8"))
    por_id = {n["id"]: n for n in kg["nodes"]}
    nodos = datos["grafo"]["nodos"]
    for clave, n in nodos.items():
        g = por_id.get(n["id"])
        if g is None or g["type"] != n["type"] or g.get("label") != n["label"]:
            raise SystemExit(f"nodo ausente o distinto en kg.json: {clave} → {n['id']}")
        if n["punto"] is not None and n["punto"] not in puntos_propios(g):
            raise SystemExit(f"nodo {clave}: {n['punto']} no es punto propio en kg.json")
    for a in datos["grafo"]["aristas"]:
        e = kg["edges"][a["indice"]]
        if (e["source"], e["relation"], e["target"]) != (
                nodos[a["origen"]]["id"], a["relation"], nodos[a["destino"]]["id"]):
            raise SystemExit(f"arista inexistente en el grafo: {a}")
    return datos


def punto_del_nodo(nodo):
    """Número que rotula al nodo, o None si es de catálogo."""
    return nodo["punto"] if nodo["type"] in TIPOS_CON_PUNTO else None


def envolver_etiqueta(texto, fs, ancho_max):
    """Envuelve por palabras al ancho de la caja y a MAX_ETIQUETA caracteres
    por línea, lo que se cumpla primero."""
    lineas, actual = [], ""
    for palabra in texto.split(" "):
        cand = palabra if not actual else actual + " " + palabra
        if actual and (ancho(cand, fs) > ancho_max or len(cand) > MAX_ETIQUETA):
            lineas.append(actual)
            actual = palabra
        else:
            actual = cand
    if actual:
        lineas.append(actual)
    return lineas


def lineas_nodo(nodo, ancho_max, fs):
    """Número de punto en negrita (si el nodo proviene de un punto) y debajo la
    etiqueta del grafo completa, sin abreviar, envuelta al ancho de la caja."""
    punto = punto_del_nodo(nodo)
    lineas = [(punto, True)] if punto else []
    lineas += [(linea, False) for linea in envolver_etiqueta(nodo["label"], fs, ancho_max)]
    for linea, _ in lineas:
        if len(linea) > MAX_ETIQUETA or ancho(linea, fs) > ancho_max:
            raise SystemExit(f"la línea de etiqueta {linea!r} no entra en la caja")
    if " ".join(l for l, es_punto in lineas if not es_punto) != nodo["label"]:
        raise SystemExit(f"la etiqueta dibujada no es la del grafo: {nodo['label']!r}")
    return lineas


def numero_inicial(texto, unidad):
    """Largo del número de punto con que empieza el texto («5.1.1.1.»), que se
    dibuja en negrita; 0 si el texto no empieza con él."""
    if not unidad:
        return 0
    prefijo = unidad + "."
    return len(prefijo) if texto.startswith(prefijo) else 0


# --------------------------------------------------------------------------- #
# Panel de texto                                                               #
# --------------------------------------------------------------------------- #
PAD_CAJA, GAP_CAJAS, GAP_ENCABEZA = 14, 15, 10


def bloques_texto(datos):
    """La frase que encabeza, los dos puntos y la línea de omisión, en el orden
    de COMPOSICION_TEXTO, con el texto tal como está en el JSON y el tramo a
    resaltar (solo en el punto que remite)."""
    t = datos["textos"]
    frase = t["frase_resaltada"]
    bloques = []
    for cid, caja, sangria in COMPOSICION_TEXTO:
        if cid is None:
            bloques.append({"clave": None, "texto": OMISION, "unidad": None, "caja": False,
                            "resaltar": None, "sangria": sangria})
            continue
        texto = t[cid]["texto"]
        resaltar = frase if caja and frase in texto else None
        bloques.append({"clave": cid, "texto": texto, "unidad": t[cid]["unidad"],
                        "caja": caja, "resaltar": resaltar, "sangria": sangria})
    if sum(1 for b in bloques if b["resaltar"]) != 1:
        raise SystemExit("la frase resaltada debe estar en exactamente un punto")
    return bloques


def estilo_de(b):
    """Estilo por carácter: "R" resaltado, "N" número de punto, "" normal."""
    texto = b["texto"]
    estilo = [""] * len(texto)
    for k in range(numero_inicial(texto, b["unidad"])):
        estilo[k] = "N"
    if b["resaltar"]:
        ini = texto.index(b["resaltar"])
        for k in range(ini, ini + len(b["resaltar"])):
            estilo[k] = "R"
    return estilo


def lineas_bloque(b, ancho_panel):
    return envolver_estilos(b["texto"], estilo_de(b), FS_TEXTO, ancho_texto_bloque(b, ancho_panel))


def ancho_texto_bloque(b, ancho_panel):
    ancho_caja = ancho_panel - 2 * PAD_PANEL - b["sangria"]
    return ancho_caja - 2 * PAD_CAJA if b["caja"] else ancho_caja


def separacion_tras(b):
    return GAP_CAJAS if b["caja"] else GAP_ENCABEZA


def alto_bloque(b, ancho_panel):
    n = len(lineas_bloque(b, ancho_panel))
    alto = FS_TEXTO + (n - 1) * INTERLINEA + 4
    return alto + 2 * PAD_CAJA if b["caja"] else alto


def alto_panel_texto(bloques, ancho_panel):
    total = sum(alto_bloque(b, ancho_panel) for b in bloques)
    total += sum(separacion_tras(b) for b in bloques[:-1])
    return total + 2 * PAD_PANEL


def dibujar_panel_texto(bloques, x0, y0, ancho_panel, alto_panel):
    partes = []
    partes.append(f'<text x="{f(x0)}" y="{f(y0 - 12)}" font-size="{FS_TITULO_PANEL}" '
                  f'font-weight="bold">En el texto</text>')
    partes.append(f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(ancho_panel)}" '
                  f'height="{f(alto_panel)}" fill="{FONDO_PANEL}" stroke="{BORDE_PANEL}" rx="5"/>')

    y = y0 + PAD_PANEL
    for b in bloques:
        alto = alto_bloque(b, ancho_panel)
        lineas = lineas_bloque(b, ancho_panel)
        xb = x0 + PAD_PANEL + b["sangria"]
        if b["caja"]:
            ancho_caja = ancho_panel - 2 * PAD_PANEL - b["sangria"]
            acento = b["resaltar"] is not None
            borde = ACENTO if acento else "#d8d8d8"
            grosor = "1.8" if acento else "1.0"
            partes.append(f'<rect x="{f(xb)}" y="{f(y)}" width="{f(ancho_caja)}" '
                          f'height="{f(alto)}" fill="white" stroke="{borde}" '
                          f'stroke-width="{grosor}" rx="4"/>')
            xl, yl = xb + PAD_CAJA, y + PAD_CAJA + FS_TEXTO
            tinta = "#1f1f1f"
        else:
            xl, yl = xb, y + FS_TEXTO
            tinta = GRIS_ROTULO

        estilo = estilo_de(b)

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

            xc = xl
            for seg, m in segmentos:
                aseg = ancho_negrita(seg, FS_TEXTO) if m else ancho(seg, FS_TEXTO)
                if m == "R" and seg.strip():
                    partes.append(f'<rect x="{f(xc - 1)}" y="{f(yl - FS_TEXTO + 2)}" '
                                  f'width="{f(aseg + 2)}" height="{f(FS_TEXTO + 5)}" '
                                  f'fill="{ACENTO}" opacity="0.26" rx="2"/>')
                xc += aseg
            tspans = ""
            for seg, m in segmentos:
                if m == "R":
                    tspans += (f'<tspan font-weight="bold" fill="{ACENTO_TEXTO}">'
                               f'{esc(seg)}</tspan>')
                elif m == "N":
                    tspans += f'<tspan font-weight="bold">{esc(seg)}</tspan>'
                else:
                    tspans += f'<tspan>{esc(seg)}</tspan>'
            partes.append(f'<text x="{f(xl)}" y="{f(yl)}" font-size="{FS_TEXTO}" '
                          f'fill="{tinta}" xml:space="preserve">{tspans}</text>')
            yl += INTERLINEA
        y += alto + separacion_tras(b)
    return partes


# --------------------------------------------------------------------------- #
# Panel del grafo                                                              #
# --------------------------------------------------------------------------- #
PAD_GRAFO = 30      # del borde del panel a la primera y a la última fila
GAP_FILAS = 58      # entre filas: alcanza para la arista vertical y su rótulo
PASO_NODO = 18      # interlínea dentro de los nodos


def cajas_grafo(nodos, y0):
    """Posición y tamaño de cada nodo, y alto del panel."""
    lineas = {c: lineas_nodo(nodos[c], COLUMNAS[col]["w"] - 22, FS_NODO)
              for c, col, _ in DISPOSICION}
    filas = sorted({fila for _, _, fila in DISPOSICION})
    alto_fila = {fi: max(len(lineas[c]) * PASO_NODO + 22
                         for c, _, fila in DISPOSICION if fila == fi) for fi in filas}
    cajas, y = {}, y0 + PAD_GRAFO
    for fi in filas:
        for c, col, fila in DISPOSICION:
            if fila == fi:
                cajas[c] = {"cx": MARGEN + COLUMNAS[col]["cx"], "cy": y + alto_fila[fi] / 2.0,
                            "w": COLUMNAS[col]["w"], "h": alto_fila[fi], "col": col, "fila": fi,
                            "lineas": lineas[c],
                            "focal": nodos[c]["type"] in TIPOS_FOCALES}
        y += alto_fila[fi] + GAP_FILAS
    return cajas, y - GAP_FILAS + PAD_GRAFO - y0


def dibujar_panel_grafo(nodos, aristas, cajas, x0, y0, ancho_panel, alto_panel):
    partes = []
    partes.append(f'<text x="{f(x0)}" y="{f(y0 - 12)}" font-size="{FS_TITULO_PANEL}" '
                  f'font-weight="bold">En el grafo</text>')
    partes.append(f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(ancho_panel)}" '
                  f'height="{f(alto_panel)}" fill="{FONDO_PANEL}" stroke="{BORDE_PANEL}" rx="5"/>')

    for a in aristas:
        ca, cb = cajas[a["origen"]], cajas[a["destino"]]
        if ca["fila"] == cb["fila"]:
            lado = 1 if cb["cx"] > ca["cx"] else -1
            p1 = (ca["cx"] + lado * ca["w"] / 2.0, ca["cy"])
            p2 = (cb["cx"] - lado * cb["w"] / 2.0, cb["cy"])
            desplazamiento = -11          # rótulo encima del trazo
        elif ca["col"] == cb["col"]:
            lado = 1 if cb["cy"] > ca["cy"] else -1
            p1 = (ca["cx"], ca["cy"] + lado * ca["h"] / 2.0)
            p2 = (cb["cx"], cb["cy"] - lado * cb["h"] / 2.0)
            desplazamiento = 0            # rótulo sobre el trazo, con fondo
        else:
            raise SystemExit(f"arista sin trazado definido: {a['origen']} -> {a['destino']}")
        resaltada = (a["relation"] == RELACION_RESALTADA)
        color = ACENTO if resaltada else GRIS_ARISTA
        grosor = "2.6" if resaltada else "1.5"
        marker = "arA" if resaltada else "arG"
        dash = "" if resaltada else ' stroke-dasharray="4,4"'
        partes.append(f'<path d="M{f(p1[0])},{f(p1[1])} L{f(p2[0])},{f(p2[1])}" fill="none" '
                      f'stroke="{color}" stroke-width="{grosor}"{dash} '
                      f'marker-end="url(#{marker})" opacity="0.95"/>')

        texto = a["relation"]
        mx, my = (p1[0] + p2[0]) / 2.0, (p1[1] + p2[1]) / 2.0 + desplazamiento
        at = ancho(texto, FS_ROTULO, resaltada)
        partes.append(f'<rect x="{f(mx - at / 2 - 4)}" y="{f(my - FS_ROTULO + 1)}" '
                      f'width="{f(at + 8)}" height="{f(FS_ROTULO + 6)}" '
                      f'fill="{FONDO_PANEL}" opacity="0.94" rx="2"/>')
        peso = "bold" if resaltada else "normal"
        relleno = ACENTO_TEXTO if resaltada else GRIS_ROTULO
        partes.append(f'<text x="{f(mx)}" y="{f(my + 4)}" text-anchor="middle" '
                      f'font-size="{FS_ROTULO}" font-weight="{peso}" fill="{relleno}">'
                      f'{esc(texto)}</text>')

    for clave, _, _ in DISPOSICION:
        nodo, caja = nodos[clave], cajas[clave]
        color = COLOR_TIPO[nodo["type"]]
        opac = "0.95" if caja["focal"] else "0.45"
        trazo = "black" if caja["focal"] else "#777"
        grosor = "1.8" if caja["focal"] else "1.1"
        relleno_txt = "white" if caja["focal"] else "#222"
        partes.append(f'<rect x="{f(caja["cx"] - caja["w"] / 2)}" y="{f(caja["cy"] - caja["h"] / 2)}" '
                      f'width="{f(caja["w"])}" height="{f(caja["h"])}" fill="{color}" '
                      f'fill-opacity="{opac}" stroke="{trazo}" stroke-width="{grosor}" rx="7"/>')
        lineas = caja["lineas"]
        ytxt = caja["cy"] - (len(lineas) - 1) * PASO_NODO / 2.0 + 5
        for linea, es_punto in lineas:
            peso = "bold" if es_punto else "normal"
            partes.append(f'<text x="{f(caja["cx"])}" y="{f(ytxt)}" text-anchor="middle" '
                          f'font-size="{FS_NODO}" font-weight="{peso}" '
                          f'fill="{relleno_txt}">{esc(linea)}</text>')
            ytxt += PASO_NODO
    return partes


def dibujar_leyenda(tipos, y0, alto, fs=FS_LEYENDA):
    """Leyenda mínima: los tipos de nodo que la figura muestra, escritos como en
    el código, y las dos clases de arista."""
    partes = []
    partes.append(f'<rect x="{f(MARGEN)}" y="{f(y0)}" width="{f(ANCHO_PANEL)}" '
                  f'height="{f(alto)}" fill="white" stroke="#e2e2e2" rx="5"/>')

    # Fila 1: tipos de nodo presentes.
    x_rot = MARGEN + 22
    partes.append(f'<text x="{f(x_rot)}" y="{f(y0 + 27)}" font-size="{fs}" '
                  f'font-weight="bold">Tipo de nodo</text>')
    xx = x_rot + ancho("Tipo de nodo", fs, True) + 26
    for t in tipos:
        partes.append(f'<rect x="{f(xx)}" y="{f(y0 + 16)}" width="17" height="13" '
                      f'fill="{COLOR_TIPO[t]}" rx="2"/>')
        partes.append(f'<text x="{f(xx + 24)}" y="{f(y0 + 27)}" font-size="{fs}">'
                      f'{esc(t)}</text>')
        xx += 24 + ancho(t, fs) + 26

    # Fila 2: las dos clases de arista.
    y2 = y0 + 56
    partes.append(f'<text x="{f(x_rot)}" y="{f(y2)}" font-size="{fs}" '
                  f'font-weight="bold">Tipo de arista</text>')
    xa = x_rot + ancho("Tipo de nodo", fs, True) + 26
    partes.append(f'<path d="M{f(xa)},{f(y2 - 4)} L{f(xa + 44)},{f(y2 - 4)}" fill="none" '
                  f'stroke="{ACENTO}" stroke-width="2.6" marker-end="url(#arA)"/>')
    partes.append(f'<text x="{f(xa + 58)}" y="{f(y2)}" font-size="{fs}" '
                  f'font-weight="bold" fill="{ACENTO_TEXTO}">remisión de un punto a otro</text>')
    x3 = xa + 58 + ancho("remisión de un punto a otro", fs, True) + 40
    partes.append(f'<path d="M{f(x3)},{f(y2 - 4)} L{f(x3 + 44)},{f(y2 - 4)}" fill="none" '
                  f'stroke="{GRIS_ARISTA}" stroke-width="1.5" stroke-dasharray="4,4" '
                  f'marker-end="url(#arG)"/>')
    partes.append(f'<text x="{f(x3 + 58)}" y="{f(y2)}" font-size="{fs}" '
                  f'fill="{GRIS_ROTULO}">resto de las relaciones</text>')
    return partes


def tipos_presentes(nodos, claves):
    presentes = {nodos[c]["type"] for c in claves}
    return [t for t in ORDEN_TIPOS if t in presentes]


# --------------------------------------------------------------------------- #
# Composición                                                                  #
# --------------------------------------------------------------------------- #
def main():
    datos = cargar_datos()
    nodos, aristas = datos["grafo"]["nodos"], datos["grafo"]["aristas"]
    if sorted(c for c, _, _ in DISPOSICION) != sorted(nodos):
        raise SystemExit("DISPOSICION no cubre exactamente los nodos del JSON")
    bloques = bloques_texto(datos)

    alto_texto = alto_panel_texto(bloques, ANCHO_PANEL)
    y_texto = 46
    y_grafo = y_texto + alto_texto + 42
    cajas, alto_grafo = cajas_grafo(nodos, y_grafo)
    y_leyenda = y_grafo + alto_grafo + 20
    alto_leyenda = 82
    alto_total = y_leyenda + alto_leyenda + MARGEN

    out = []
    out.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{f(alto_total)}" '
               f'viewBox="0 0 {W} {f(alto_total)}" font-family="{TIPOGRAFIA}">')
    out.append(f'<rect width="{W}" height="{f(alto_total)}" fill="white"/>')
    out.append('<defs>'
               '<marker id="arG" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
               f'markerHeight="6" orient="auto-start-reverse"><path d="M0,0L10,5L0,10z" '
               f'fill="{GRIS_ARISTA}"/></marker>'
               '<marker id="arA" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
               f'markerHeight="6" orient="auto-start-reverse"><path d="M0,0L10,5L0,10z" '
               f'fill="{ACENTO}"/></marker>'
               '</defs>')
    out += dibujar_panel_texto(bloques, MARGEN, y_texto, ANCHO_PANEL, alto_texto)
    out += dibujar_panel_grafo(nodos, aristas, cajas, MARGEN, y_grafo, ANCHO_PANEL, alto_grafo)
    out += dibujar_leyenda(tipos_presentes(nodos, list(nodos)), y_leyenda, alto_leyenda)
    out.append('</svg>')
    svg = "\n".join(out) + "\n"

    with open(SALIDA_SVG, "w", encoding="utf-8") as fh:
        fh.write(svg)

    # ---------------- informe a stdout (no forma parte de la figura) --------- #
    print(f"SVG: {os.path.relpath(SALIDA_SVG, RAIZ)}   {W} x {f(alto_total)} px "
          f"(relación alto/ancho {alto_total / W:.2f})   "
          f"sha256 {hashlib.sha256(svg.encode('utf-8')).hexdigest()}")
    print(f"datos: {os.path.relpath(DATOS, RAIZ)}   sha256 "
          f"{hashlib.sha256(open(DATOS, 'rb').read()).hexdigest()}")
    print(f"kg.json sha256 {datos['fuentes']['kg']['sha256']} (comprobado; nodos y aristas presentes)")
    print(f"Impresa a {ANCHO_PAGINA_CM:.0f} cm de ancho ({ANCHO_PAGINA_CM * PT_POR_CM:.1f} pt):")
    for nombre, px in [("texto de los recuadros", FS_TEXTO), ("etiqueta de nodo", FS_NODO),
                       ("rótulo de arista", FS_ROTULO), ("leyenda", FS_LEYENDA)]:
        pt = puntos_impresos(px)
        marca = "  <-- mínimo exigido 8 pt" if nombre.startswith("texto") else ""
        print(f"    {nombre:24s} {px:4.1f} px -> {pt:5.2f} pt{marca}")

    print("\nTEXTOS")
    for b in bloques:
        print(f"  {str(b['clave'] or OMISION):13s} {'recuadro' if b['caja'] else 'gris    '} "
              f"sangría {b['sangria']:2d} px  "
              f"{len(lineas_bloque(b, ANCHO_PANEL))} líneas"
              f"{'  resalta ' + repr(b['resaltar']) if b['resaltar'] else ''}")
    print(f"\nnodos dibujados: {len(cajas)}   aristas dibujadas: {len(aristas)}")
    print("NODOS")
    mas_larga = max(len(linea) for c in cajas.values() for linea, _ in c["lineas"])
    for clave, _, _ in DISPOSICION:
        n, c = nodos[clave], cajas[clave]
        print(f"  {clave:19s} {n['type']:11s} punto {str(punto_del_nodo(n)):8s} "
              f"{'focal   ' if c['focal'] else 'contexto'} líneas {[l for l, _ in c['lineas']]}")
    print(f"  línea de etiqueta más larga: {mas_larga} caracteres (máximo {MAX_ETIQUETA})")
    print("ARISTAS")
    for a in aristas:
        estado = "RESALTADA" if a["relation"] == RELACION_RESALTADA else "gris     "
        print(f"  {estado} kg['edges'][{a['indice']}] {a['origen']} --{a['relation']}--> {a['destino']}")


if __name__ == "__main__":
    main()
