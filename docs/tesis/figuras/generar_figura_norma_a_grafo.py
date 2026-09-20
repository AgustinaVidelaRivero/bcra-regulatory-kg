#!/usr/bin/env python3
"""Figura «de la norma al grafo» para la Introducción.

Panel superior: texto verbatim de los puntos del Texto Ordenado.
Panel inferior: los nodos y aristas que la extracción produjo a partir de ellos,
con la remisión resaltada.

Sin dependencias externas: escribe el SVG a mano (misma técnica, tipografía y
paleta que la figura de la cláusula del 125 %). Generación determinística: dos
corridas sobre las mismas fuentes producen el mismo SVG byte a byte.

Uso:
    python3 docs/tesis/figuras/generar_figura_norma_a_grafo.py
"""

import json
import os
import unicodedata

# --------------------------------------------------------------------------- #
# Fuentes de datos                                                             #
# --------------------------------------------------------------------------- #
RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
KG = os.path.join(RAIZ, "data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json")
CHUNKS = os.path.join(RAIZ, "data/experiment/reextraccion_v2/e0_chunking/salida/chunks_ext.json")
SALIDA_SVG = os.path.join(os.path.dirname(__file__), "figura_norma_a_grafo.svg")

# Nodos de la figura, por sufijo de id. Seis nodos: la restricción del punto de
# origen, las tres obligaciones a las que remite, la operación que limita y el
# sujeto al que se aplica. El nodo del Texto Ordenado queda fuera.
SUF_RESTRICCION = "8355c7"                          # restricción anclada en 3.17.1.4
SUF_OBLIGACIONES = ["999fbd", "ed6cf9", "6514f0"]   # remitidas por arista referencia
SUF_OPERACION = "59fccf"                            # pagos de utilidades y dividendos
ID_SUJETO = "Sujeto_rol_entidad_autorizada_exterior"

PUNTO_ORIGEN = "3.17.1.4"
PUNTOS_DESTINO = ["3.4.1", "3.4.2", "3.4.3"]
FRASE_RESALTADA = ("en la medida que se verifiquen los requisitos previstos "
                   "en los puntos 3.4.1. a 3.4.3.")

# Aristas que se dibujan, además de las tres remisiones: solo estas dos del
# contexto, para que el grafo no se llene de relaciones repetidas.
ARISTAS_CONTEXTO = [("R", "limita", "OP"), ("R", "aplica_a", "SU")]

# Fragmento del punto que se muestra en cada recuadro. Debe ser la disposición
# que origina el nodo dibujado con ese número, no la primera línea del punto:
# 3.4.2 contiene dos disposiciones y el nodo de la figura viene de la segunda.
# `omite_antes` marca con […] que el punto tiene texto previo no mostrado.
# Cada fragmento se verifica carácter por carácter contra el texto de la unidad
# de extracción antes de dibujar.
FRAGMENTOS = {
    "3.17.1.4": {"desde": None, "omite_antes": False},
    "3.4.1":    {"desde": None, "omite_antes": False},
    "3.4.2":    {"desde": "La entidad deberá contar con una declaración jurada",
                 "omite_antes": True},
    "3.4.3":    {"desde": None, "omite_antes": False},
}

# Etiquetas acortadas a 40 caracteres. Clave: sufijo de id.
ETIQUETAS_CORTAS = {
    "8355c7": "Requisitos para pagar dividendos",
    "6514f0": "Verificación del Relevamiento externo",
    "59fccf": "Pago de dividendos a no residentes",
    "Sujeto_rol_entidad_autorizada_exterior": "Entidades autorizadas en cambios",
}
MAX_ETIQUETA = 40

# Predicados en castellano legible.
CASTELLANO = {
    "referencia": "remite a",
    "aplica_a": "se aplica a",
    "limita": "limita",
    "establecida_en": "establecida en",
    "regula": "regula",
    "condiciona": "condiciona",
    "prohibe": "prohíbe",
    "requiere": "requiere",
}

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


def tokens(texto):
    """Palabras normalizadas (minúsculas, sin acentos) para cotejar textos."""
    plano = unicodedata.normalize("NFKD", texto.lower())
    plano = "".join(c for c in plano if not unicodedata.combining(c))
    limpio = "".join(c if c.isalnum() else " " for c in plano)
    return [t for t in limpio.split() if t]


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


# Solo los nodos de contenido provienen de un punto del Texto Ordenado. Los de
# catálogo (Sujeto) son estructura: su procedencia enumera los cientos de puntos
# donde aparecen, y no tienen «su» punto.
TIPOS_CON_PUNTO = ("Obligacion", "Restriccion", "Excepcion", "Operacion")
PUNTOS_FIGURA = [PUNTO_ORIGEN] + PUNTOS_DESTINO


def punto_de_la_figura(elem):
    """Punto que rotula al nodo en esta figura, o None si no corresponde."""
    if elem["type"] not in TIPOS_CON_PUNTO:
        return None
    propios = puntos_propios(elem)
    for p in PUNTOS_FIGURA:
        if p in propios:
            return p
    return None


def cargar():
    with open(KG, encoding="utf-8") as fh:
        kg = json.load(fh)
    nodos = {n["id"]: n for n in kg["nodes"]}

    def por_sufijo(suf):
        cands = sorted(i for i in nodos if i.endswith(suf))
        if len(cands) != 1:
            raise SystemExit(f"sufijo {suf!r} no identifica un nodo único: {cands}")
        return cands[0]

    ids = {"R": por_sufijo(SUF_RESTRICCION), "OP": por_sufijo(SUF_OPERACION), "SU": ID_SUJETO}
    for n, suf in enumerate(SUF_OBLIGACIONES, start=1):
        ids[f"O{n}"] = por_sufijo(suf)
    for clave, nid in ids.items():
        if nid not in nodos:
            raise SystemExit(f"nodo ausente del grafo: {clave} → {nid}")

    with open(CHUNKS, encoding="utf-8") as fh:
        chunks = {c["unidad"]: c for c in json.load(fh)}

    # Aristas a dibujar: las tres remisiones de la restricción a las tres
    # obligaciones, más las dos de contexto elegidas. Cada una se comprueba
    # contra el grafo: si alguna no existiera allí, el script se detiene.
    existentes = set()
    for e in kg["edges"]:
        existentes.add((e["source"], e["relation"], e["target"]))
    aristas = []
    for clave in ["O1", "O2", "O3"]:
        aristas.append((ids["R"], "referencia", ids[clave]))
    for ka, rel, kb in ARISTAS_CONTEXTO:
        aristas.append((ids[ka], rel, ids[kb]))
    for a in aristas:
        if a not in existentes:
            raise SystemExit(f"arista inexistente en el grafo: {a}")
    return nodos, ids, chunks, aristas


def etiqueta_de(nodos, nid):
    """Etiqueta a dibujar: la del grafo, o la acortada si supera el máximo."""
    original = nodos[nid].get("label", "")
    for clave, corta in ETIQUETAS_CORTAS.items():
        if nid.endswith(clave) or nid == clave:
            return corta, original
    return original, original


# --------------------------------------------------------------------------- #
# Panel de texto                                                               #
# --------------------------------------------------------------------------- #
def normalizar(texto, unidad):
    """Quita el prefijo del número de punto y une los cortes de línea del PDF.

    No cambia ninguna palabra ni signo: solo el punto de corte de línea, que es
    un artefacto de la maquetación del PDF.
    """
    cuerpo = texto
    prefijo = unidad + "."
    if cuerpo.startswith(prefijo):
        cuerpo = cuerpo[len(prefijo):]
    return " ".join(cuerpo.split())


def bloques_texto(chunks):
    """Los cuatro recuadros del panel de texto, en orden numérico.

    De cada punto se muestra la disposición que origina el nodo dibujado con ese
    número. El fragmento se toma del texto de la unidad de extracción y se
    verifica que aparezca allí literalmente.
    """
    bloques = []
    for punto in [PUNTO_ORIGEN] + PUNTOS_DESTINO:
        completo = normalizar(chunks[punto]["texto"], punto)
        cfg = FRAGMENTOS[punto]
        if cfg["desde"] is None:
            fragmento = completo
        else:
            if cfg["desde"] not in completo:
                raise SystemExit(f"el fragmento de {punto} no está en el texto de la unidad")
            fragmento = completo[completo.index(cfg["desde"]):]
        bloques.append({
            "punto": punto,
            "texto": ("[…] " if cfg["omite_antes"] else "") + fragmento,
            "fragmento": fragmento,
            "completo": completo,
            "resaltar": FRASE_RESALTADA if punto == PUNTO_ORIGEN else None,
        })
    return bloques


def alto_panel_texto(bloques, ancho_panel):
    ancho_texto = ancho_panel - 2 * PAD_PANEL - 2 * 14
    total = 0
    for i, b in enumerate(bloques):
        lineas = envolver(b["texto"], FS_TEXTO, ancho_texto)
        total += 14 + FS_ENCABEZADO + 8 + len(lineas) * INTERLINEA + 14 - 6
        if i < len(bloques) - 1:
            total += 15
    return total + 2 * PAD_PANEL


def dibujar_panel_texto(bloques, x0, y0, ancho_panel, alto_panel):
    partes = []
    partes.append(f'<text x="{f(x0)}" y="{f(y0 - 12)}" font-size="{FS_TITULO_PANEL}" '
                  f'font-weight="bold">En el texto</text>')
    partes.append(f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(ancho_panel)}" '
                  f'height="{f(alto_panel)}" fill="{FONDO_PANEL}" stroke="{BORDE_PANEL}" rx="5"/>')

    pad_caja, gap = 14, 15
    ancho_caja = ancho_panel - 2 * PAD_PANEL
    ancho_texto = ancho_caja - 2 * pad_caja
    y = y0 + PAD_PANEL

    for b in bloques:
        lineas = envolver(b["texto"], FS_TEXTO, ancho_texto)
        alto = pad_caja + FS_ENCABEZADO + 8 + len(lineas) * INTERLINEA + pad_caja - 6
        acento = b["resaltar"] is not None
        borde = ACENTO if acento else "#d8d8d8"
        grosor = "1.8" if acento else "1.0"
        partes.append(f'<rect x="{f(x0 + PAD_PANEL)}" y="{f(y)}" width="{f(ancho_caja)}" '
                      f'height="{f(alto)}" fill="white" stroke="{borde}" '
                      f'stroke-width="{grosor}" rx="4"/>')
        partes.append(f'<text x="{f(x0 + PAD_PANEL + pad_caja)}" y="{f(y + pad_caja + FS_ENCABEZADO - 2)}" '
                      f'font-size="{FS_ENCABEZADO}" font-weight="bold" fill="#333">'
                      f'Punto {esc(b["punto"])}</text>')

        if b["resaltar"] and b["resaltar"] in b["texto"]:
            ini = b["texto"].index(b["resaltar"])
            fin = ini + len(b["resaltar"])
        else:
            ini = fin = -1

        yl = y + pad_caja + FS_ENCABEZADO + 8 + FS_TEXTO
        for linea, desplazamiento in lineas:
            xl = x0 + PAD_PANEL + pad_caja
            segmentos, actual, marca = [], "", None
            for k, ch in enumerate(linea):
                m = (ini <= desplazamiento + k < fin)
                if marca is None:
                    marca = m
                if m != marca:
                    segmentos.append((actual, marca))
                    actual, marca = "", m
                actual += ch
            if actual:
                segmentos.append((actual, bool(marca)))

            xc = xl
            for seg, m in segmentos:
                aseg = ancho(seg, FS_TEXTO, m)
                if m and seg.strip():
                    partes.append(f'<rect x="{f(xc - 1)}" y="{f(yl - FS_TEXTO + 2)}" '
                                  f'width="{f(aseg + 2)}" height="{f(FS_TEXTO + 5)}" '
                                  f'fill="{ACENTO}" opacity="0.26" rx="2"/>')
                xc += aseg
            tspans = ""
            for seg, m in segmentos:
                if m:
                    tspans += (f'<tspan font-weight="bold" fill="{ACENTO_TEXTO}">'
                               f'{esc(seg)}</tspan>')
                else:
                    tspans += f'<tspan>{esc(seg)}</tspan>'
            partes.append(f'<text x="{f(xl)}" y="{f(yl)}" font-size="{FS_TEXTO}" '
                          f'fill="#1f1f1f" xml:space="preserve">{tspans}</text>')
            yl += INTERLINEA
        y += alto + gap
    return partes


# --------------------------------------------------------------------------- #
# Panel del grafo                                                              #
# --------------------------------------------------------------------------- #
ALTO_GRAFO = 344


def dibujar_panel_grafo(nodos, ids, aristas, x0, y0, ancho_panel, alto_panel):
    partes = []
    partes.append(f'<text x="{f(x0)}" y="{f(y0 - 12)}" font-size="{FS_TITULO_PANEL}" '
                  f'font-weight="bold">En el grafo</text>')
    partes.append(f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(ancho_panel)}" '
                  f'height="{f(alto_panel)}" fill="{FONDO_PANEL}" stroke="{BORDE_PANEL}" rx="5"/>')

    # La restricción del punto de origen a la izquierda; las tres obligaciones a
    # las que remite, apiladas a la derecha; debajo, la operación que limita y el
    # sujeto al que se aplica.
    cajas = {
        "R":  {"x": x0 + 190, "y": y0 + 118, "w": 322, "h": 60, "focal": True},
        "O1": {"x": x0 + 620, "y": y0 + 56,  "w": 336, "h": 56, "focal": True},
        "O2": {"x": x0 + 620, "y": y0 + 124, "w": 336, "h": 56, "focal": True},
        "O3": {"x": x0 + 620, "y": y0 + 192, "w": 336, "h": 56, "focal": True},
        "OP": {"x": x0 + 190, "y": y0 + 288, "w": 322, "h": 54, "focal": False},
        "SU": {"x": x0 + 620, "y": y0 + 288, "w": 336, "h": 54, "focal": False},
    }
    por_id = {ids[k]: k for k in ids}

    # Trazado de cada arista: salida, llegada, punto de control de la curva
    # cuadrática (o None si es recta) y corrimiento del rótulo. La EXISTENCIA de
    # cada arista se lee del grafo; solo su recorrido es decisión de dibujo.
    RUTAS = {
        ("R", "O1"): ((351, 104), (452, 56),  None,       (0, -4)),
        ("R", "O2"): ((351, 118), (452, 124), None,       (0, -5)),
        ("R", "O3"): ((351, 132), (452, 192), None,       (0, -4)),
        ("R", "OP"): ((190, 148), (190, 261), None,       (0, 0)),
        ("R", "SU"): ((300, 148), (452, 288), (392, 250), (-6, 12)),
    }

    for origen, relacion, destino in aristas:
        ka, kb = por_id[origen], por_id[destino]
        if (ka, kb) not in RUTAS:
            raise SystemExit(f"arista sin trazado definido: {ka} -> {kb} ({relacion})")
        (ax, ay), (bx, by), ctrl, (ox, oy) = RUTAS[(ka, kb)]
        p1, p2 = (x0 + ax, y0 + ay), (x0 + bx, y0 + by)
        resaltada = (relacion == "referencia")
        color = ACENTO if resaltada else GRIS_ARISTA
        grosor = "2.6" if resaltada else "1.5"
        marker = "arA" if resaltada else "arG"
        dash = "" if resaltada else ' stroke-dasharray="4,4"'
        if ctrl is None:
            d = f"M{f(p1[0])},{f(p1[1])} L{f(p2[0])},{f(p2[1])}"
            mx, my = (p1[0] + p2[0]) / 2.0, (p1[1] + p2[1]) / 2.0
        else:
            c = (x0 + ctrl[0], y0 + ctrl[1])
            d = f"M{f(p1[0])},{f(p1[1])} Q{f(c[0])},{f(c[1])} {f(p2[0])},{f(p2[1])}"
            mx = (p1[0] + 2 * c[0] + p2[0]) / 4.0
            my = (p1[1] + 2 * c[1] + p2[1]) / 4.0
        partes.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{grosor}"'
                      f'{dash} marker-end="url(#{marker})" opacity="0.95"/>')

        texto = CASTELLANO.get(relacion, relacion)
        mx, my = mx + ox, my + oy
        at = ancho(texto, FS_ROTULO, resaltada)
        partes.append(f'<rect x="{f(mx - at / 2 - 4)}" y="{f(my - FS_ROTULO + 1)}" '
                      f'width="{f(at + 8)}" height="{f(FS_ROTULO + 6)}" '
                      f'fill="{FONDO_PANEL}" opacity="0.94" rx="2"/>')
        peso = "bold" if resaltada else "normal"
        relleno = ACENTO_TEXTO if resaltada else GRIS_ROTULO
        partes.append(f'<text x="{f(mx)}" y="{f(my + 4)}" text-anchor="middle" '
                      f'font-size="{FS_ROTULO}" font-weight="{peso}" fill="{relleno}">'
                      f'{esc(texto)}</text>')

    for clave in ["R", "O1", "O2", "O3", "OP", "SU"]:
        nid = ids[clave]
        nodo = nodos[nid]
        caja = cajas[clave]
        color = COLOR_TIPO[nodo["type"]]
        opac = "0.95" if caja["focal"] else "0.45"
        trazo = "black" if caja["focal"] else "#777"
        grosor = "1.8" if caja["focal"] else "1.1"
        relleno_txt = "white" if caja["focal"] else "#222"
        partes.append(f'<rect x="{f(caja["x"] - caja["w"] / 2)}" y="{f(caja["y"] - caja["h"] / 2)}" '
                      f'width="{f(caja["w"])}" height="{f(caja["h"])}" fill="{color}" '
                      f'fill-opacity="{opac}" stroke="{trazo}" stroke-width="{grosor}" rx="7"/>')

        # Número de punto en negrita en la primera línea (solo si el nodo
        # proviene de un punto) y debajo la etiqueta. Ninguna línea pasa de
        # MAX_ETIQUETA caracteres.
        corta, _ = etiqueta_de(nodos, nid)
        elegido = punto_de_la_figura(nodo)
        lineas = ([(elegido, True)] if elegido else [])
        for linea, _ in envolver(corta, FS_NODO, caja["w"] - 22):
            lineas.append((linea, False))
        ytxt = caja["y"] - (len(lineas) - 1) * 9 + 5
        for linea, es_punto in lineas:
            peso = "bold" if es_punto else "normal"
            partes.append(f'<text x="{f(caja["x"])}" y="{f(ytxt)}" text-anchor="middle" '
                          f'font-size="{FS_NODO}" font-weight="{peso}" '
                          f'fill="{relleno_txt}">{esc(linea)}</text>')
            ytxt += 18
    return partes


def dibujar_leyenda(nodos, ids, y0, alto):
    """Leyenda mínima: tipos de nodo presentes y las dos clases de arista."""
    partes = []
    presentes = []
    for clave in ["R", "O1", "OP", "SU"]:
        t = nodos[ids[clave]]["type"]
        if t not in presentes:
            presentes.append(t)
    NOMBRE = {"Restriccion": "Restricción", "Obligacion": "Obligación",
              "Operacion": "Operación", "Sujeto": "Sujeto"}

    partes.append(f'<rect x="{f(MARGEN)}" y="{f(y0)}" width="{f(ANCHO_PANEL)}" '
                  f'height="{f(alto)}" fill="white" stroke="#e2e2e2" rx="5"/>')

    # Fila 1: tipos de nodo presentes.
    x_rot = MARGEN + 22
    partes.append(f'<text x="{f(x_rot)}" y="{f(y0 + 27)}" font-size="{FS_LEYENDA}" '
                  f'font-weight="bold">Tipo de nodo</text>')
    xx = x_rot + ancho("Tipo de nodo", FS_LEYENDA, True) + 26
    for t in presentes:
        partes.append(f'<rect x="{f(xx)}" y="{f(y0 + 16)}" width="17" height="13" '
                      f'fill="{COLOR_TIPO[t]}" rx="2"/>')
        partes.append(f'<text x="{f(xx + 24)}" y="{f(y0 + 27)}" font-size="{FS_LEYENDA}">'
                      f'{esc(NOMBRE[t])}</text>')
        xx += 24 + ancho(NOMBRE[t], FS_LEYENDA) + 26

    # Fila 2: las dos clases de arista.
    y2 = y0 + 56
    partes.append(f'<text x="{f(x_rot)}" y="{f(y2)}" font-size="{FS_LEYENDA}" '
                  f'font-weight="bold">Tipo de arista</text>')
    xa = x_rot + ancho("Tipo de nodo", FS_LEYENDA, True) + 26
    partes.append(f'<path d="M{f(xa)},{f(y2 - 4)} L{f(xa + 44)},{f(y2 - 4)}" fill="none" '
                  f'stroke="{ACENTO}" stroke-width="2.6" marker-end="url(#arA)"/>')
    partes.append(f'<text x="{f(xa + 58)}" y="{f(y2)}" font-size="{FS_LEYENDA}" '
                  f'font-weight="bold" fill="{ACENTO_TEXTO}">remisión de un punto a otro</text>')
    x3 = xa + 58 + ancho("remisión de un punto a otro", FS_LEYENDA, True) + 40
    partes.append(f'<path d="M{f(x3)},{f(y2 - 4)} L{f(x3 + 44)},{f(y2 - 4)}" fill="none" '
                  f'stroke="{GRIS_ARISTA}" stroke-width="1.5" stroke-dasharray="4,4" '
                  f'marker-end="url(#arG)"/>')
    partes.append(f'<text x="{f(x3 + 58)}" y="{f(y2)}" font-size="{FS_LEYENDA}" '
                  f'fill="{GRIS_ROTULO}">resto de las relaciones</text>')
    return partes


# --------------------------------------------------------------------------- #
# Verificación de correspondencia texto ↔ nodo                                 #
# --------------------------------------------------------------------------- #
def raiz_del_id(nid):
    """Palabras del id que provienen del texto de la disposición extraída."""
    cuerpo = nid.split("_", 1)[1] if "_" in nid else nid
    partes = cuerpo.split("_")
    if partes and len(partes[-1]) == 6 and all(c in "0123456789abcdef" for c in partes[-1]):
        partes = partes[:-1]
    return [p for p in partes if p]


def cobertura(nid, texto):
    """Fracción de las palabras del id que aparecen en `texto`."""
    raiz = raiz_del_id(nid)
    if not raiz:
        return 0.0
    presentes = set(tokens(texto))
    return sum(1 for p in raiz if p in presentes) / len(raiz)


def verificar_correspondencia(nodos, ids, bloques, kg_nodos_por_punto):
    """Para cada recuadro: el texto mostrado debe corresponder al nodo rotulado
    con ese número, y no a otra disposición del mismo punto."""
    dibujado_en = {}
    for clave in ["R", "O1", "O2", "O3", "OP", "SU"]:
        p = punto_de_la_figura(nodos[ids[clave]])
        if p:
            dibujado_en.setdefault(p, []).append(ids[clave])

    filas = []
    for b in bloques:
        punto = b["punto"]
        propios = dibujado_en.get(punto, [])
        # El nodo de contenido que la figura rotula con este número. Para
        # 3.17.1.4 hay dos (la restricción y la operación): manda la restricción.
        elegido = None
        for nid in propios:
            if nodos[nid]["type"] in ("Restriccion", "Obligacion", "Excepcion"):
                elegido = nid
                break
        if elegido is None and propios:
            elegido = propios[0]
        propia = cobertura(elegido, b["fragmento"]) if elegido else 0.0
        # Las demás disposiciones de contenido del mismo punto, dibujadas o no.
        otras = []
        for n in kg_nodos_por_punto.get(punto, []):
            if n["id"] == elegido or n["type"] not in ("Restriccion", "Obligacion", "Excepcion"):
                continue
            otras.append((n["id"], cobertura(n["id"], b["fragmento"])))
        peor_otra = max([c for _, c in otras], default=0.0)
        filas.append({"punto": punto, "nodo": elegido, "cobertura_propia": propia,
                      "otras": otras, "mejor_otra": peor_otra,
                      "ok": propia >= 0.75 and propia > peor_otra})
    return filas


def nodos_por_punto(nodos):
    idx = {}
    for n in nodos.values():
        for p in provenances(n):
            if p.get("to") == "ext" and p.get("rol_documental") == "punto_propio" and p.get("punto"):
                idx.setdefault(p["punto"], [])
                if n["id"] not in [x["id"] for x in idx[p["punto"]]]:
                    idx[p["punto"]].append(n)
    for k in idx:
        idx[k].sort(key=lambda n: (n["type"], n["id"]))
    return idx


# --------------------------------------------------------------------------- #
# Composición                                                                  #
# --------------------------------------------------------------------------- #
def main():
    nodos, ids, chunks, aristas = cargar()
    bloques = bloques_texto(chunks)
    idx_punto = nodos_por_punto(nodos)

    alto_texto = alto_panel_texto(bloques, ANCHO_PANEL)
    y_texto = 46
    y_grafo = y_texto + alto_texto + 42
    y_leyenda = y_grafo + ALTO_GRAFO + 20
    alto_leyenda = 82
    alto_total = y_leyenda + alto_leyenda + MARGEN

    out = []
    out.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{alto_total}" '
               f'viewBox="0 0 {W} {alto_total}" font-family="{TIPOGRAFIA}">')
    out.append(f'<rect width="{W}" height="{alto_total}" fill="white"/>')
    out.append('<defs>'
               '<marker id="arG" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
               f'markerHeight="6" orient="auto-start-reverse"><path d="M0,0L10,5L0,10z" '
               f'fill="{GRIS_ARISTA}"/></marker>'
               '<marker id="arA" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
               f'markerHeight="6" orient="auto-start-reverse"><path d="M0,0L10,5L0,10z" '
               f'fill="{ACENTO}"/></marker>'
               '</defs>')
    out += dibujar_panel_texto(bloques, MARGEN, y_texto, ANCHO_PANEL, alto_texto)
    out += dibujar_panel_grafo(nodos, ids, aristas, MARGEN, y_grafo, ANCHO_PANEL, ALTO_GRAFO)
    out += dibujar_leyenda(nodos, ids, y_leyenda, alto_leyenda)
    out.append('</svg>')

    with open(SALIDA_SVG, "w", encoding="utf-8") as fh:
        fh.write("\n".join(out) + "\n")

    # ---------------- informe a stdout (no forma parte de la figura) --------- #
    print(f"SVG: {SALIDA_SVG}   {W} x {alto_total} px "
          f"(relación alto/ancho {alto_total / W:.2f})")
    print(f"Impresa a {ANCHO_PAGINA_CM:.0f} cm de ancho ({ANCHO_PAGINA_CM * PT_POR_CM:.1f} pt):")
    for nombre, px in [("texto de los recuadros", FS_TEXTO), ("encabezado de recuadro", FS_ENCABEZADO),
                       ("etiqueta de nodo", FS_NODO), ("rótulo de arista", FS_ROTULO),
                       ("leyenda", FS_LEYENDA)]:
        pt = puntos_impresos(px)
        marca = "  <-- mínimo exigido 8 pt" if nombre.startswith("texto") else ""
        print(f"    {nombre:24s} {px:4.1f} px -> {pt:5.2f} pt{marca}")

    print(f"\nnodos dibujados: {len(ids)}   aristas dibujadas: {len(aristas)}")
    print("\nNODOS")
    for clave in ["R", "O1", "O2", "O3", "OP", "SU"]:
        nid = ids[clave]
        nodo = nodos[nid]
        corta, original = etiqueta_de(nodos, nid)
        marca = "" if corta == original else f"  [acortada de {len(original)}]"
        pt = punto_de_la_figura(nodo)
        propios = puntos_propios(nodo)
        detalle = (f"punto {pt}" + (f" (+{len(propios) - 1} más)" if len(propios) > 1 else "")
                   ) if pt else f"sin punto propio único ({len(propios)} apariciones)"
        print(f"  {clave:3s} {nodo['type']:12s} {detalle:34s} etiqueta[{len(corta):2d}] "
              f"{corta!r}{marca}")
    print("\nARISTAS")
    por_id = {ids[k]: k for k in ids}
    for o, r, d in aristas:
        estado = "RESALTADA" if r == "referencia" else "gris     "
        print(f"  {estado} {por_id[o]:3s} --{CASTELLANO.get(r, r):15s}--> {por_id[d]:3s}")

    print("\nCORRESPONDENCIA texto mostrado <-> nodo rotulado con ese número")
    filas = verificar_correspondencia(nodos, ids, bloques, idx_punto)
    todo_ok = True
    for fila in filas:
        todo_ok = todo_ok and fila["ok"]
        print(f"  Punto {fila['punto']:9s} {'OK ' if fila['ok'] else 'MAL'} "
              f"cobertura del nodo dibujado {fila['cobertura_propia']:.2f} · "
              f"mejor de las otras disposiciones del punto {fila['mejor_otra']:.2f}")
        print(f"      nodo: {fila['nodo']}")
        for nid, c in fila["otras"]:
            print(f"      otra disposición del punto ({c:.2f}): {nid}")
    if not todo_ok:
        raise SystemExit("FALLA: algún recuadro no corresponde al nodo dibujado")
    print("  --> los cuatro recuadros corresponden al nodo rotulado con su número.")


if __name__ == "__main__":
    main()
