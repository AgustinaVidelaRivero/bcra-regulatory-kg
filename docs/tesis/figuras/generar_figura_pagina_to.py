#!/usr/bin/env python3
"""Figura «la página del ejemplo» para el análisis del documento (capítulo 3), versión 3.

La página del Texto Ordenado de Clasificación de deudores que contiene los
puntos 5.1.1 y 5.1.1.1 (el ejemplo del préstamo), rasterizada desde el PDF del
corpus a 10 cm de ancho dentro de una figura de 15 cm, con una columna de seis
etiquetas a la derecha unidas a cada parte por líneas guía; debajo, un recorte
del punto 3.7, que está en otra página del mismo documento, a la misma escala.
El tramo de la página entre el encabezado de 5.1.2 y el pie se omite; el corte
se marca con una línea de puntos. El logo, el encabezado y el pie quedan.

Las seis etiquetas (título en negrita y una línea debajo), en orden: la
sección; el punto 5.1.1 como punto contenedor, con un corchete que abarca su
extensión; su párrafo sin numerar, que abre la excepción; el punto 5.1.1.1 como
punto terminal; la remisión al punto 3.7, con un recuadro naranja sobre
«punto 3.7.» y una flecha naranja hasta el recorte; y el pie de página, con su
versión, su comunicación y su vigencia. «Punto contenedor» (un punto con al
menos un subpunto), «punto terminal» (uno sin subpuntos) y «párrafo sin
numerar» (el que un contenedor tiene antes o después de sus subpuntos) son
nombres de este trabajo, no del BCRA. La imagen no lleva nombres de archivo ni
rutas.

Nada del contenido se tipea ni se supone:
- el PDF es el del corpus: candado de sha256 (PDF_SHA256), que además debe ser
  el del inventario del conjunto de desarrollo (desarrollo_5tos.json →
  tos[cla].sha256_pdf), y su portada debe decir la versión del corpus
  («“A” 8378», «19/12/2025»);
- las páginas salen de E0 (chunks_cla.json de salida_enm01, campo `paginas` de
  cla::5.1.1.1 y de cla::3.7), con candado de sha256 sobre chunks_cla.json y
  estructura_cla.json; el texto de cada chunk debe estar en la página que
  declara;
- contenedor, subpuntos y terminal salen de estructura_cla.json (`hijos`);
- toda posición (recuadros, corchete, líneas guía, flecha, cortes y recortes)
  sale de la capa de texto del PDF (pdfplumber). El texto de las etiquetas es
  fijo (ETIQUETAS); el script comprueba que sus números
  (sección 5, puntos 5.1.1, 5.1.1.1 y 3.7, sección 3) sean los leídos del PDF
  y de E0.

Controles de geometría, en cada corrida (el script frena si fallan): los
tramos de las líneas guía sobre la página, sus puntos de origen, el corchete y
la flecha no tocan ningún carácter con tinta de la página; el corchete, la
flecha y los puntos de origen tampoco tocan un borde de tabla (las líneas guía
pueden cruzar el borde de la tabla del encabezado al salir de su fila); las
líneas guía no se cruzan entre sí ni con la flecha.

Reutiliza por importación, como la figura de la tripleta: de
generar_figura_norma_a_grafo.py, la tipografía, el naranja de las remisiones,
el borde de panel, el escape y formato del SVG y la tabla de métricas; de
generar_figura_proceso_extraccion.py, el ancho de texto de 15 cm, la
exportación a PNG a 300 dpi con la densidad grabada y el medidor con métricas
reales de Helvetica.

El SVG es intermedio: se pasa a rsvg-convert por la entrada estándar y no se
escribe salvo con --svg. Salidas: figura_pagina_to.png y figura_pagina_to.pdf,
las dos byte-reproducibles (el PDF, con la fecha de creación fijada por
SOURCE_DATE_EPOCH).

Uso (desde la raíz del repo):
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_pagina_to.py
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_pagina_to.py --verificar
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_pagina_to.py --svg <ruta>

Con --verificar, además, mide cada texto de las etiquetas con las métricas
reales de Helvetica y comprueba que ninguno quede por debajo de 7 pt impresos,
salga de su columna, se superponga con otro o pise la página o el recorte.
"""

import argparse
import base64
import hashlib
import io
import json
import os
import re
import shutil
import statistics
import subprocess
import sys

sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import generar_figura_norma_a_grafo as base          # noqa: E402
import generar_figura_proceso_extraccion as proc     # noqa: E402

import pdfplumber                                     # noqa: E402
import pypdfium2 as pdfium                            # noqa: E402

RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", ".."))
SALIDA_PNG = os.path.join(AQUI, "figura_pagina_to.png")
SALIDA_PDF = os.path.join(AQUI, "figura_pagina_to.pdf")

# --------------------------------------------------------------------------- #
# Fuentes y candados                                                           #
# --------------------------------------------------------------------------- #
REL_PDF = "data/experiment/subset/TO_clasificacion_deudores_actual.pdf"
REL_INVENTARIO = "data/experiment/reextraccion_v2/manifiestos/desarrollo_5tos.json"
REL_CHUNKS = "data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_cla.json"
REL_ESTRUCTURA = "data/experiment/reextraccion_v2/e0_chunking/salida_enm01/estructura_cla.json"
# sha256 del PDF del corpus (el del inventario del conjunto de desarrollo) y de
# la E0 que da las páginas. Si alguno cambia, el script frena: la figura afirma
# que estas páginas son las de esta versión.
PDF_SHA256 = "6e7f528d3fea7b756f15e1278eecd828f203f0651fc6f778212033de6a0883e2"
CHUNKS_SHA256 = "98808886a406d8321c678836a55f92eea983d594d95358dd21ceb537487ac0b1"
ESTRUCTURA_SHA256 = "3cd26083fee7355ef3d8027ac353a744c2f1cfa35830535fe1be2b9505eaf917"
TO = "cla"
# Versión del corpus (decisión 3 del mandato de U-CAP3-DOC): la portada del PDF
# debe decir las dos cosas.
PORTADA = ("“A” 8378", "19/12/2025")
PUNTO_CONTENEDOR = "5.1.1"
PUNTO_TERMINAL = "5.1.1.1"
PUNTO_REMITIDO = "3.7"
# El corte: se conserva el encabezado de este punto y se omite lo que sigue
# hasta el pie.
PUNTO_CORTE = "5.1.2"

# --------------------------------------------------------------------------- #
# Tamaño impreso: 15 cm de ancho; la página ocupa 10 cm                        #
# --------------------------------------------------------------------------- #
W = proc.W                                            # 720 unidades de lienzo
ANCHO_FIGURA_CM = proc.ANCHO_TEXTO_CM                 # 15,00
ANCHO_FIGURA_PT = ANCHO_FIGURA_CM * proc.PT_POR_CM    # 425,2
DPI = proc.DPI                                        # 300
ANCHO_PNG_PX = round(ANCHO_FIGURA_CM / 2.54 * DPI)    # 1772
PT_MINIMO = 7.0
ANCHO_PAGINA_CM = 10.0
W_PAGINA = round(W * ANCHO_PAGINA_CM / ANCHO_FIGURA_CM)   # 480 unidades


def puntos_impresos(unidades):
    """Tamaño en puntos de `unidades` del lienzo con la figura a 15 cm."""
    return unidades * ANCHO_FIGURA_PT / W


TIPOGRAFIA = base.TIPOGRAFIA
ACENTO = base.ACENTO                # naranja: reservado a las remisiones
GRIS_BORDE = base.BORDE_PANEL       # borde de la página
TRAZO = "#4a5a6a"                   # gris oscuro de la paleta compartida
TINTA = "#1f1f1f"
TINTA_SUAVE = "#555555"
esc, f = base.esc, base.f

FS = 14                 # etiquetas: título en negrita y línea debajo (8,27 pt impresos)
IL = 18                 # interlínea de las etiquetas
CALLE = 20              # entre la página y la columna de etiquetas
MARGEN_DER = 4
X_COL = W_PAGINA + CALLE
W_COL = W - MARGEN_DER - X_COL
X_BORDE = W_PAGINA + 3  # las líneas guía salen de la página por acá
SEP_ETIQUETA = 8        # aire vertical mínimo entre etiquetas
R_ORIGEN = 2            # punto de origen de las líneas guía
BANDA_CORTE = 16        # alto de la banda del corte, en unidades
SEP_RECORTE = 14        # entre la página y el recorte del punto remitido
AIRE_ARRIBA_PT = 4      # sobre el logo
AIRE_CORTE_PT = 5       # bajo el encabezado de 5.1.2 y bajo el pie
AIRE_PIE_PT = 8         # sobre el pie
AIRE_RECORTE_PT = 6     # sobre y bajo el punto remitido
DX_FLECHA_PT = 6        # la flecha baja por el margen izquierdo, a esta distancia del contenido
AIRE_IZQ_PT = 7         # a la izquierda de la flecha
AIRE_DER_PT = 5         # a la derecha del contenido
DX_CORCHETE_PT = 7      # el corchete, a la izquierda del número del contenedor
TIC_CORCHETE_PT = 3.5   # largo de los extremos del corchete
PAD_RECUADRO_PT = 2.5   # aire de los recuadros sobre el texto
ESCALA_RASTER = 4       # píxeles por punto PDF de las imágenes embebidas

# Etiquetas: texto fijo (título, línea debajo). Los
# números se comprueban contra lo leído del PDF y de E0.
ETIQUETAS = (
    ("seccion", "Sección 5", "en el encabezado de la página"),
    ("contenedor", "Punto contenedor 5.1.1", "tiene subpuntos"),
    ("parrafo", "Párrafo sin numerar", "abre la excepción"),
    ("terminal", "Punto terminal 5.1.1.1", "no tiene subpuntos"),
    ("remision", "Remisión al punto 3.7", "el punto está en la sección 3"),
    ("pie", "Pie de página", "versión, comunicación y vigencia"),
)

RX_NUMERO = re.compile(r"^(\d+(?:\.\d+)*)\.\s")
RX_SECCION = re.compile(r"^Secci[oó]n (\d+)\.\s+(.+)$")
RX_EXCEPCION = re.compile(r"con\s+excepci[óo]n\s+de[^:.;]*")
RX_REMISION = r"(?:establecido|previsto|dispuesto)\s+en\s+el\s+punto\s+{}\.?"


def sha256(ruta):
    with open(ruta, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def norm(s):
    """Guiones de fin de línea fuera y blancos colapsados (regla R7 de U-INSUMOS-CAP)."""
    return re.sub(r"\s+", " ", s.replace("-\n", "")).strip()


def unica(paginas, que):
    if len(paginas) != 1:
        raise SystemExit(f"{que}: se esperaba una sola página en E0 y hay {paginas}")
    return paginas[0]


def caja_union(objs, pad=0.0):
    return (min(o["x0"] for o in objs) - pad, min(o["top"] for o in objs) - pad,
            max(o["x1"] for o in objs) + pad, max(o["bottom"] for o in objs) + pad)


def medio(obj):
    return (obj["top"] + obj["bottom"]) / 2.0


# --------------------------------------------------------------------------- #
# Carga y resolución                                                           #
# --------------------------------------------------------------------------- #
def cargar_e0():
    """Páginas y estructura desde E0, con sus candados."""
    rutas = {"chunks": os.path.join(RAIZ, REL_CHUNKS),
             "estructura": os.path.join(RAIZ, REL_ESTRUCTURA)}
    for clave, esperado in (("chunks", CHUNKS_SHA256), ("estructura", ESTRUCTURA_SHA256)):
        s = sha256(rutas[clave])
        if s != esperado:
            raise SystemExit(f"{clave}_{TO}.json no es el verificado: sha {s[:12]}… ≠ {esperado[:12]}…")
    with open(rutas["chunks"], encoding="utf-8") as fh:
        chunks = {c["id"]: c for c in json.load(fh)}
    with open(rutas["estructura"], encoding="utf-8") as fh:
        estructura = json.load(fh)

    term = chunks[f"{TO}::{PUNTO_TERMINAL}"]
    intro = chunks[f"{TO}::{PUNTO_CONTENEDOR}::intro"]
    remitido = chunks[f"{TO}::{PUNTO_REMITIDO}"]
    pagina = unica(term["paginas"], f"{TO}::{PUNTO_TERMINAL}")
    pagina_remitido = unica(remitido["paginas"], f"{TO}::{PUNTO_REMITIDO}")
    seccion = PUNTO_TERMINAL.split(".")[0]
    # Encabezado de la sección, encabezado del contenedor y su párrafo sin
    # numerar: en la misma página que el terminal, según E0.
    heredadas = {(h["unidad_origen"], h["tipo"]): h["paginas"] for h in term["herencia"]}
    for clave in ((f"S{seccion}", "encabezado"), (PUNTO_CONTENEDOR, "encabezado"),
                  (PUNTO_CONTENEDOR, "intro")):
        if heredadas.get(clave) != [pagina]:
            raise SystemExit(f"E0: {clave} no está en la página {pagina} ({heredadas.get(clave)})")
    if intro["paginas"] != [pagina]:
        raise SystemExit(f"E0: el párrafo sin numerar de {PUNTO_CONTENEDOR} no está en la página {pagina}")

    nodos = {}

    def recorrer(n):
        nodos[n.get("numero")] = n
        for h in n.get("hijos", []):
            recorrer(h)
    for s in estructura["secciones"]:
        recorrer(s)
    hijos = [h["numero"] for h in nodos[PUNTO_CONTENEDOR].get("hijos", [])]
    if PUNTO_TERMINAL not in hijos:
        raise SystemExit(f"estructura: {PUNTO_TERMINAL} no es hijo de {PUNTO_CONTENEDOR}")
    if nodos[PUNTO_TERMINAL].get("hijos"):
        raise SystemExit(f"estructura: {PUNTO_TERMINAL} tiene subpuntos; no es terminal")
    if not any(sg["rol"] == "intro" for sg in nodos[PUNTO_CONTENEDOR]["segmentos"]):
        raise SystemExit(f"estructura: {PUNTO_CONTENEDOR} no tiene párrafo sin numerar previo")
    return {"pagina": pagina, "pagina_remitido": pagina_remitido, "seccion": seccion,
            "hijos": hijos, "texto_terminal": term["texto"], "texto_intro": intro["texto"],
            "texto_remitido": remitido["texto"]}


def encabezado(linea):
    m = RX_NUMERO.match(linea["text"])
    return m.group(1) if m else None


def indice_de(lineas, numero):
    idx = [i for i, l in enumerate(lineas) if encabezado(l) == numero]
    if len(idx) != 1:
        raise SystemExit(f"PDF: el encabezado del punto {numero} aparece {len(idx)} veces")
    return idx[0]


def extension(lineas, i, fin_cuerpo):
    """Líneas del punto que empieza en la línea i: hasta el próximo encabezado de
    igual o menor profundidad, o hasta el pie."""
    prof = len(encabezado(lineas[i]).split("."))
    j = i + 1
    while j < fin_cuerpo:
        n = encabezado(lineas[j])
        if n is not None and len(n.split(".")) <= prof:
            break
        j += 1
    return lineas[i:j]


def leer_pagina(pag):
    lineas = pag.extract_text_lines()
    palabras = pag.extract_words()
    pie = [l for l in lineas if l["text"].startswith(("Vigencia:", "Versión:"))]
    if not pie:
        raise SystemExit(f"PDF: la página {pag.page_number} no tiene pie reconocible")
    tope_pie = min(l["top"] for l in pie)
    fin_cuerpo = next(i for i, l in enumerate(lineas) if l["top"] >= tope_pie - 1)
    pie_lineas = lineas[fin_cuerpo:]
    rects_pie = [r for r in pag.rects if r["top"] >= tope_pie - 15]
    cabecera = [l for l in lineas[:fin_cuerpo] if RX_SECCION.match(l["text"])]
    if len(cabecera) != 1:
        raise SystemExit(f"PDF: la página {pag.page_number} tiene {len(cabecera)} líneas de sección")
    return {"lineas": lineas, "palabras": palabras, "fin_cuerpo": fin_cuerpo,
            "pie_lineas": pie_lineas, "caja_pie": caja_union(pie_lineas + rects_pie),
            "tabla_pie": caja_union(rects_pie),
            "cabecera": cabecera[0], "texto": pag.extract_text(),
            # Los espacios que el PDF trae como caracteres no tienen tinta: no
            # cuentan como texto que una línea guía pueda cruzar.
            "chars": [dict(x0=c["x0"], top=c["top"], x1=c["x1"], bottom=c["bottom"],
                           size=c["size"]) for c in pag.chars if c["text"].strip()],
            "bordes": [dict(x0=r["x0"], top=r["top"], x1=r["x1"], bottom=r["bottom"])
                       for r in pag.rects],
            "imagenes": [dict(x0=i["x0"], top=i["top"], x1=i["x1"], bottom=i["bottom"])
                         for i in pag.images],
            "ancho": float(pag.width), "alto": float(pag.height)}


def fila_de(linea, bordes):
    """Borde de tabla inmediatamente arriba y abajo de una línea de texto."""
    horizontales = [b for b in bordes if b["bottom"] - b["top"] < 1
                    and b["x0"] <= linea["x0"] and b["x1"] >= linea["x0"]]
    arriba = max(b["bottom"] for b in horizontales if b["bottom"] <= medio(linea))
    abajo = min(b["top"] for b in horizontales if b["top"] >= medio(linea))
    return arriba, abajo


def resolver():
    ruta_pdf = os.path.join(RAIZ, REL_PDF)
    s = sha256(ruta_pdf)
    if s != PDF_SHA256:
        raise SystemExit(f"el PDF no es el verificado: sha {s[:12]}… ≠ {PDF_SHA256[:12]}…")
    with open(os.path.join(RAIZ, REL_INVENTARIO), encoding="utf-8") as fh:
        inv = [t for t in json.load(fh)["tos"] if t["id"] == TO]
    if len(inv) != 1 or inv[0]["sha256_pdf"] != PDF_SHA256 or inv[0]["pdf"] != REL_PDF:
        raise SystemExit("el inventario del conjunto de desarrollo no declara este PDF para cla")
    e0 = cargar_e0()

    with pdfplumber.open(ruta_pdf) as doc:
        portada = doc.pages[0].extract_text()
        if not all(p in portada for p in PORTADA):
            raise SystemExit(f"la portada no dice la versión del corpus {PORTADA}")
        pg = leer_pagina(doc.pages[e0["pagina"] - 1])
        pr = leer_pagina(doc.pages[e0["pagina_remitido"] - 1])

    # El texto de cada chunk de E0 está en la página que E0 declara.
    for clave, pagina in (("texto_terminal", pg), ("texto_intro", pg), ("texto_remitido", pr)):
        if norm(e0[clave]) not in norm(pagina["texto"]):
            raise SystemExit(f"PDF: el {clave} de E0 no está en la página declarada")

    lin = pg["lineas"]
    i_cont = indice_de(lin, PUNTO_CONTENEDOR)
    i_term = indice_de(lin, PUNTO_TERMINAL)
    i_corte = indice_de(lin, PUNTO_CORTE)
    cont = extension(lin, i_cont, pg["fin_cuerpo"])
    term = extension(lin, i_term, pg["fin_cuerpo"])
    parrafo = lin[i_cont + 1:i_term]
    if not parrafo or norm("\n".join(l["text"] for l in parrafo)) != norm(e0["texto_intro"]):
        raise SystemExit("PDF: el párrafo sin numerar no coincide con el de E0")
    if lin[i_cont + len(cont)] is not lin[i_corte]:
        raise SystemExit(f"PDF: después de {PUNTO_CONTENEDOR} no sigue {PUNTO_CORTE}")
    m_sec = RX_SECCION.match(pg["cabecera"]["text"])
    if m_sec.group(1) != e0["seccion"]:
        raise SystemExit(f"PDF: la página es de la Sección {m_sec.group(1)}, no de la {e0['seccion']}")
    if not RX_EXCEPCION.search(norm(e0["texto_intro"])):
        raise SystemExit("el párrafo sin numerar no abre una excepción («con excepción de»)")
    if not re.search(RX_REMISION.format(re.escape(PUNTO_REMITIDO)), norm(e0["texto_terminal"])):
        raise SystemExit(f"el punto terminal no remite al punto {PUNTO_REMITIDO}")

    # La remisión: las palabras «punto» y «3.7.» dentro de las líneas del terminal.
    top0, bot0 = term[0]["top"] - 1, term[-1]["bottom"] + 1
    pal = [p for p in pg["palabras"] if top0 <= p["top"] and p["bottom"] <= bot0]
    pares = [(a, b) for a, b in zip(pal, pal[1:])
             if a["text"] == "punto" and b["text"].rstrip(".") == PUNTO_REMITIDO]
    if len(pares) != 1:
        raise SystemExit(f"PDF: la remisión al punto {PUNTO_REMITIDO} aparece {len(pares)} veces en el terminal")
    linea_rem = next(l for l in term if l["top"] - 0.5 <= pares[0][0]["top"] <= l["bottom"])

    pie_txt = " ".join(l["text"] for l in pg["pie_lineas"])
    m_ver = re.search(r"Versi[oó]n:\s*(\S+)", pie_txt)
    m_com = re.search(r"COMUNICACI[OÓ]N\s*[“\"]([A-Z])[”\"]\s*(\d+)", pie_txt)
    m_vig = re.search(r"(\d{2}/\d{2}/\d{4})", pie_txt)
    if not (m_ver and m_com and m_vig):
        raise SystemExit(f"PDF: el pie no tiene versión, comunicación y vigencia: {pie_txt!r}")

    lr = pr["lineas"]
    remitido = extension(lr, indice_de(lr, PUNTO_REMITIDO), pr["fin_cuerpo"])
    if norm("\n".join(l["text"] for l in remitido)) != norm(e0["texto_remitido"]):
        raise SystemExit("PDF: el recorte del punto remitido no coincide con el texto de E0")
    m_sec_r = RX_SECCION.match(pr["cabecera"]["text"])
    if m_sec_r.group(1) != PUNTO_REMITIDO.split(".")[0]:
        raise SystemExit("PDF: el punto remitido no está en la sección que indica su número")

    # Los números de las etiquetas son los leídos.
    esperados = {"seccion": f"Sección {m_sec.group(1)}",
                 "contenedor": f"Punto contenedor {PUNTO_CONTENEDOR}",
                 "terminal": f"Punto terminal {PUNTO_TERMINAL}",
                 "remision": f"Remisión al punto {PUNTO_REMITIDO}"}
    for clave, titulo, linea in ETIQUETAS:
        if clave in esperados and titulo != esperados[clave]:
            raise SystemExit(f"etiqueta {clave}: {titulo!r} ≠ {esperados[clave]!r}")
    if not dict((c, l) for c, _, l in ETIQUETAS)["remision"].endswith(f"sección {m_sec_r.group(1)}"):
        raise SystemExit("etiqueta de la remisión: la sección no es la del punto remitido")

    # Tramos horizontales: la flecha baja por el margen izquierdo; el corchete
    # va a la izquierda del número del contenedor.
    contenido = pg["chars"] + pg["bordes"] + pg["imagenes"]
    x_min = min(o["x0"] for o in contenido)
    x_flecha = x_min - DX_FLECHA_PT
    x_corchete = cont[0]["x0"] - DX_CORCHETE_PT
    cajas = {
        "contenedor": caja_union([cont[0]], PAD_RECUADRO_PT),
        "parrafo": caja_union(parrafo, PAD_RECUADRO_PT),
        "terminal": caja_union(term, PAD_RECUADRO_PT),
        "remision": caja_union(list(pares[0]), 1.5),
    }
    x0 = x_flecha - AIRE_IZQ_PT
    x1 = max(max(o["x1"] for o in contenido), cajas["terminal"][2]) + AIRE_DER_PT
    s = W_PAGINA / (x1 - x0)                 # unidades de lienzo por punto PDF

    # Tramos verticales: del logo al encabezado de 5.1.2; el pie; el punto remitido.
    tramo_sup = (min(o["top"] for o in contenido) - AIRE_ARRIBA_PT,
                 lin[i_corte]["bottom"] + AIRE_CORTE_PT)
    if tramo_sup[1] >= lin[i_corte + 1]["top"]:
        raise SystemExit("el corte superior tocaría la línea que sigue a 5.1.2")
    caja_pie = pg["caja_pie"]
    tramo_pie = (caja_pie[1] - AIRE_PIE_PT, caja_pie[3] + AIRE_CORTE_PT)
    ultima_omitida = max(l["bottom"] for l in lin[i_corte + 1:pg["fin_cuerpo"]])
    if tramo_pie[0] <= ultima_omitida:
        raise SystemExit("el tramo del pie empezaría sobre texto omitido")
    caja_rem = caja_union(remitido)
    tramo_rem = (caja_rem[1] - AIRE_RECORTE_PT, caja_rem[3] + AIRE_RECORTE_PT)

    # Origen de cada línea guía, en puntos PDF de la página: el borde derecho
    # de la parte, a la altura de su primera línea. La sección y el pie no
    # llevan recuadro: ya tienen los bordes de su tabla.
    arriba, abajo = fila_de(pg["cabecera"], pg["bordes"])
    tabla_pie = pg["tabla_pie"]
    origenes = {
        "seccion": (pg["cabecera"]["x1"] + 2 * R_ORIGEN / s, (arriba + abajo) / 2.0),
        "contenedor": (cajas["contenedor"][2], medio(cont[0])),
        "parrafo": (cajas["parrafo"][2], medio(parrafo[0])),
        "terminal": (cajas["terminal"][2], medio(term[0])),
        "remision": (cajas["terminal"][2], medio(linea_rem)),
        # Fuera del borde derecho de la tabla del pie, a un radio de distancia.
        "pie": (tabla_pie[2] + 2 * R_ORIGEN / s, (tabla_pie[1] + tabla_pie[3]) / 2.0),
    }
    corchete = (x_corchete, cont[0]["top"], cont[-1]["bottom"])
    # La flecha: sale del borde izquierdo del recuadro del terminal, a la
    # altura de la línea de «punto 3.7.»; baja por la sangría entre el corchete
    # y el bloque; pasa bajo el contenedor por el blanco que lo separa de 5.1.2;
    # y baja por el margen izquierdo hasta el recorte.
    x_sangria = (x_corchete + cajas["terminal"][0]) / 2.0
    y_paso = (cont[-1]["bottom"] + lin[i_corte]["top"]) / 2.0
    y_rem = medio(linea_rem)
    flecha = [(cajas["terminal"][0], y_rem), (x_sangria, y_rem), (x_sangria, y_paso),
              (x_flecha, y_paso)]

    visibles = [c for c in pg["chars"]
                if tramo_sup[0] <= c["top"] and c["bottom"] <= tramo_sup[1]
                or tramo_pie[0] <= c["top"] and c["bottom"] <= tramo_pie[1]]
    tamanos = [round(c["size"], 2) for c in visibles]
    tamanos_rem = [round(c["size"], 2) for c in pr["chars"]
                   if tramo_rem[0] <= c["top"] and c["bottom"] <= tramo_rem[1]]
    return {
        "e0": e0, "pg": pg, "pr": pr, "cajas": cajas, "origenes": origenes,
        "corchete": corchete, "flecha": flecha,
        "x0": x0, "x1": x1, "x_flecha": x_flecha, "escala": s,
        "tramo_sup": tramo_sup, "tramo_pie": tramo_pie, "tramo_rem": tramo_rem,
        "tamanos": (min(tamanos), statistics.median(tamanos), max(tamanos)),
        "tamanos_rem": (min(tamanos_rem), statistics.median(tamanos_rem), max(tamanos_rem)),
        "lineas": {"contenedor": len(cont), "parrafo": len(parrafo), "terminal": len(term),
                   "remitido": len(remitido),
                   "omitidas": pg["fin_cuerpo"] - (i_corte + 1)},
        "pie_texto": pie_txt,
    }


# --------------------------------------------------------------------------- #
# Controles de geometría (en puntos PDF de la página)                          #
# --------------------------------------------------------------------------- #
def cruza(a, b):
    return a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]


def segmento(p, q, ancho=0.5):
    """Caja de un segmento horizontal o vertical."""
    return (min(p[0], q[0]) - ancho, min(p[1], q[1]) - ancho,
            max(p[0], q[0]) + ancho, max(p[1], q[1]) + ancho)


def controlar_geometria(res):
    pg, s = res["pg"], res["escala"]
    chars = [("carácter", (c["x0"], c["top"], c["x1"], c["bottom"])) for c in pg["chars"]]
    bordes = [("borde de tabla", (b["x0"], b["top"], b["x1"], b["bottom"])) for b in pg["bordes"]]
    r = R_ORIGEN / s
    piezas = []          # (nombre, caja, obstáculos)
    for clave, (x, y) in res["origenes"].items():
        piezas.append((f"línea guía {clave}, tramo sobre la página",
                       segmento((x, y), (res["x1"], y)), chars))
        piezas.append((f"punto de origen {clave}", (x - r, y - r, x + r, y + r), chars + bordes))
    xc, yc0, yc1 = res["corchete"]
    t = TIC_CORCHETE_PT
    for i, (p, q) in enumerate((((xc, yc0), (xc, yc1)), ((xc, yc0), (xc + t, yc0)),
                                ((xc, yc1), (xc + t, yc1))), start=1):
        piezas.append((f"corchete, trazo {i}", segmento(p, q), chars + bordes))
    fl = res["flecha"]
    for i, (p, q) in enumerate(zip(fl, fl[1:]), start=1):
        piezas.append((f"flecha, tramo {i}", segmento(p, q), chars + bordes))
    xf = res["x_flecha"]
    piezas.append(("flecha, tramo vertical hasta el corte",
                   segmento((xf, fl[-1][1]), (xf, res["tramo_sup"][1])), chars + bordes))
    piezas.append(("flecha, tramo vertical junto al pie",
                   segmento((xf, res["tramo_pie"][0]), (xf, res["tramo_pie"][1])), chars + bordes))
    fallas = []
    for nombre, caja, obstaculos in piezas:
        for tipo, o in obstaculos:
            if cruza(caja, o):
                fallas.append(f"{nombre} toca un {tipo} en {tuple(round(v, 1) for v in o)}")
                break
    # Las líneas guía no se cruzan: sus orígenes y sus etiquetas siguen el
    # mismo orden vertical (se controla al componer).
    return len(piezas), fallas


# --------------------------------------------------------------------------- #
# Imágenes                                                                     #
# --------------------------------------------------------------------------- #
def recortar(pdf, pagina, caja, dim):
    """PNG del recorte `caja` (puntos PDF, origen arriba a la izquierda) y la
    caja efectiva, ajustada a píxeles enteros."""
    pag = pdf[pagina - 1]
    ancho, alto = pag.get_size()
    if (round(ancho, 2), round(alto, 2)) != (round(dim[0], 2), round(dim[1], 2)):
        raise SystemExit(f"página {pagina}: pdfium y pdfplumber no dan el mismo tamaño")
    img = pag.render(scale=ESCALA_RASTER).to_pil().convert("RGB")
    px = [max(0, round(caja[0] * ESCALA_RASTER)), max(0, round(caja[1] * ESCALA_RASTER)),
          min(img.width, round(caja[2] * ESCALA_RASTER)),
          min(img.height, round(caja[3] * ESCALA_RASTER))]
    rec = img.crop(tuple(px))
    buf = io.BytesIO()
    rec.save(buf, format="PNG")
    return buf.getvalue(), tuple(v / ESCALA_RASTER for v in px), rec.size


# --------------------------------------------------------------------------- #
# Composición                                                                  #
# --------------------------------------------------------------------------- #
REGISTRO = []
PANELES = []


def texto(partes, x, y, s, negrita, relleno, contexto):
    peso = "bold" if negrita else "normal"
    partes.append(f'<text x="{f(x)}" y="{f(y)}" font-size="{FS}" font-weight="{peso}" '
                  f'fill="{relleno}">{esc(s)}</text>')
    REGISTRO.append({"s": s, "fs": FS, "negrita": negrita, "x": x, "y": y, "contexto": contexto})


def rect(partes, x0, y0, x1, y1, color, grosor, relleno="none"):
    partes.append(f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(x1 - x0)}" height="{f(y1 - y0)}" '
                  f'fill="{relleno}" stroke="{color}" stroke-width="{grosor}"/>')


def trazo(partes, puntos, color, grosor, marcador=None):
    d = " ".join(("M" if i == 0 else "L") + f"{f(x)},{f(y)}" for i, (x, y) in enumerate(puntos))
    m = f' marker-end="url(#{marcador})"' if marcador else ""
    partes.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{grosor}"{m}/>')


def imagen(partes, x, y, w, h, png):
    datos = base64.b64encode(png).decode("ascii")
    partes.append(f'<image x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" '
                  f'preserveAspectRatio="none" xlink:href="data:image/png;base64,{datos}"/>')


def componer(res, recortes):
    del REGISTRO[:]
    del PANELES[:]
    partes = []
    s, x0 = res["escala"], res["x0"]
    (png_sup, caja_sup), (png_pie, caja_pie), (png_rem, caja_rem) = recortes

    def X(x):
        return (x - x0) * s

    h_sup = (caja_sup[3] - caja_sup[1]) * s
    y_pie = h_sup + BANDA_CORTE
    h_pie = (caja_pie[3] - caja_pie[1]) * s
    alto_pagina = y_pie + h_pie
    y_rem = alto_pagina + SEP_RECORTE
    h_rem = (caja_rem[3] - caja_rem[1]) * s

    def Ys(y):
        return (y - caja_sup[1]) * s

    def Yp(y):
        return y_pie + (y - caja_pie[1]) * s

    # La página: tramo superior, banda del corte con la línea de puntos, pie.
    imagen(partes, 0, 0, W_PAGINA, h_sup, png_sup)
    imagen(partes, 0, y_pie, W_PAGINA, h_pie, png_pie)
    y_corte = h_sup + BANDA_CORTE / 2.0
    partes.append(f'<path d="M{f(0)},{f(y_corte)} L{f(W_PAGINA)},{f(y_corte)}" fill="none" '
                  f'stroke="{TRAZO}" stroke-width="1.6" stroke-linecap="round" '
                  f'stroke-dasharray="0.1,5"/>')
    rect(partes, 0.5, 0.5, W_PAGINA - 0.5, alto_pagina - 0.5, GRIS_BORDE, "1")
    PANELES.append(("página", (0, 0, W_PAGINA, alto_pagina)))

    # Recuadros y corchete.
    for clave, caja in res["cajas"].items():
        color = ACENTO if clave == "remision" else TRAZO
        rect(partes, X(caja[0]), Ys(caja[1]), X(caja[2]), Ys(caja[3]), color, "1.3")
    xc, yc0, yc1 = res["corchete"]
    tic = TIC_CORCHETE_PT
    trazo(partes, [(X(xc + tic), Ys(yc0)), (X(xc), Ys(yc0)), (X(xc), Ys(yc1)),
                   (X(xc + tic), Ys(yc1))], TRAZO, "1.3")

    # El punto remitido, debajo de la página, a la misma escala.
    imagen(partes, 0, y_rem, W_PAGINA, h_rem, png_rem)
    rect(partes, 0.65, y_rem + 0.65, W_PAGINA - 0.65, y_rem + h_rem - 0.65, ACENTO, "1.3")
    PANELES.append(("recorte", (0, y_rem, W_PAGINA, y_rem + h_rem)))
    fl = [(X(x), Ys(y)) for x, y in res["flecha"]] + [(X(res["x_flecha"]), y_rem - 1)]
    trazo(partes, fl, ACENTO, "1.6", "flecha")

    # Columna de etiquetas, en el orden de sus partes; cada una a la altura de
    # su origen o, si no entra, debajo de la anterior.
    y_libre = 0.0
    anclas = {}
    for clave, titulo, linea in ETIQUETAS:
        ox, oy = res["origenes"][clave]
        ty = Yp(oy) if clave == "pie" else Ys(oy)
        tope = max(ty - FS * 0.5, y_libre)
        texto(partes, X_COL, tope + FS * 0.78, titulo, True, TINTA, f"etiqueta {clave}")
        texto(partes, X_COL, tope + FS * 0.78 + IL, linea, False, TINTA_SUAVE, f"etiqueta {clave}")
        anclas[clave] = (X(ox), ty, tope + FS * 0.5)
        y_libre = tope + 2 * IL + SEP_ETIQUETA
    orden_origen = [anclas[c][1] for c, _, _ in ETIQUETAS]
    orden_etiqueta = [anclas[c][2] for c, _, _ in ETIQUETAS]
    if orden_origen != sorted(orden_origen) or orden_etiqueta != sorted(orden_etiqueta):
        raise SystemExit("las líneas guía se cruzarían: orígenes y etiquetas no siguen el mismo orden")

    # Líneas guía: del origen, horizontal hasta salir de la página y en diagonal
    # hasta la etiqueta. La de la remisión, en el naranja de las remisiones.
    for clave, _, _ in ETIQUETAS:
        sx, ty, ay = anclas[clave]
        color = ACENTO if clave == "remision" else TRAZO
        trazo(partes, [(sx, ty), (X_BORDE, ty), (X_COL - 5, ay)], color, "1.0")
        partes.append(f'<circle cx="{f(sx)}" cy="{f(ty)}" r="{R_ORIGEN}" fill="{color}"/>')

    alto_total = max(y_rem + h_rem, y_libre - SEP_ETIQUETA)
    alto_cm = ANCHO_FIGURA_CM * alto_total / W
    cabeza = [
        f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
        f'width="{ANCHO_FIGURA_CM:.2f}cm" height="{alto_cm:.2f}cm" '
        f'viewBox="0 0 {W} {f(alto_total)}" font-family="{TIPOGRAFIA}">',
        f'<rect width="{W}" height="{f(alto_total)}" fill="white"/>',
        '<defs><marker id="flecha" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
        f'markerHeight="6" orient="auto"><path d="M0,0L10,5L0,10z" fill="{ACENTO}"/></marker></defs>',
    ]
    geometria = {"alto_total": alto_total, "alto_pagina": alto_pagina, "h_sup": h_sup,
                 "h_pie": h_pie, "h_rem": h_rem, "anclas": anclas}
    return "\n".join(cabeza + partes + ["</svg>"]) + "\n", geometria


# --------------------------------------------------------------------------- #
# Exportación e invariantes                                                    #
# --------------------------------------------------------------------------- #
# cairo escribe /CreationDate (con segundos) en el diccionario /Info, que queda
# dentro de un /ObjStm comprimido: un grep sobre los bytes no la ve, pero el PDF
# cambia en cada corrida. Con SOURCE_DATE_EPOCH fijo, cairo escribe esa fecha y
# el PDF es byte-reproducible (probado con rsvg-convert 2.62.3 / cairo 1.18.4).
SOURCE_DATE_EPOCH = "0"


def exportar(svg):
    rsvg = shutil.which("rsvg-convert")
    if not rsvg:
        raise SystemExit("rsvg-convert no está instalado: no se escriben el PNG ni el PDF")
    datos = svg.encode("utf-8")
    subprocess.run([rsvg, "-w", str(ANCHO_PNG_PX), "-f", "png", "-o", SALIDA_PNG],
                   input=datos, check=True)
    proc.grabar_densidad(SALIDA_PNG, DPI)
    entorno = dict(os.environ, SOURCE_DATE_EPOCH=SOURCE_DATE_EPOCH)
    subprocess.run([rsvg, "-f", "pdf", "-o", SALIDA_PDF], input=datos, check=True, env=entorno)


def invariantes_pdf():
    """sha256 del stream de contenido de la página y de cada XObject del PDF, y
    la fecha de creación que declara: control adicional al sha del archivo."""
    from pypdf import PdfReader
    lector = PdfReader(SALIDA_PDF)
    pagina = lector.pages[0]
    fecha = (lector.metadata or {}).get("/CreationDate")
    contenido = hashlib.sha256(pagina.get_contents().get_data()).hexdigest()
    xobjetos = []

    def recorrer(recursos):
        xo = recursos.get("/XObject") if recursos else None
        if not xo:
            return
        for nombre in sorted(xo.keys()):
            obj = xo[nombre].get_object()
            xobjetos.append(hashlib.sha256(obj.get_data()).hexdigest())
            recorrer(obj.get("/Resources"))
    recorrer(pagina.get("/Resources"))
    return contenido, sorted(xobjetos), fecha


# --------------------------------------------------------------------------- #
# Verificación de medidas                                                      #
# --------------------------------------------------------------------------- #
def verificar(alto_total):
    medir = proc.medidor()
    fuente = "métricas reales de Helvetica" if medir else "tabla de métricas del script"
    if not medir:
        print("PIL o la fuente del sistema no están: se verifica con la tabla del script.")
        medir = base.ancho
    print(f"\nVERIFICACIÓN DE MEDIDAS ({fuente})")
    fallas, cajas = [], []
    for r in REGISTRO:
        a = medir(r["s"], r["fs"], r["negrita"])
        bb = (r["x"], r["y"] - r["fs"] * 0.78, r["x"] + a, r["y"] + r["fs"] * 0.22)
        cajas.append((r, bb))
        pt = puntos_impresos(r["fs"])
        estado = []
        if pt < PT_MINIMO:
            estado.append(f"letra {pt:.2f} pt < {PT_MINIMO}")
        if bb[2] > W - MARGEN_DER:
            estado.append(f"sale de la columna ({bb[2]:.1f} > {W - MARGEN_DER})")
        if bb[1] < 0 or bb[3] > alto_total:
            estado.append("fuera del lienzo")
        for nombre, pb in PANELES:
            if cruza(bb, pb):
                estado.append(f"pisa {nombre}")
        print(f"  {'MAL' if estado else 'ok '} {pt:5.2f} pt  ancho {a:6.1f} / {W_COL}  "
              f"{r['contexto']:20s} {r['s']!r}" + ("  <-- " + "; ".join(estado) if estado else ""))
        fallas += [(r["s"], e) for e in estado]
    for i in range(len(cajas)):
        for j in range(i + 1, len(cajas)):
            (ra, a), (rb, b) = cajas[i], cajas[j]
            if cruza(a, b):
                fallas.append((ra["s"], f"se superpone con {rb['s']!r}"))
                print(f"  MAL superposición: {ra['s']!r} / {rb['s']!r}")
    print(f"  textos medidos: {len(REGISTRO)}   fallas: {len(fallas)}")
    return not fallas


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--verificar", action="store_true")
    ap.add_argument("--svg", help="guarda además el SVG intermedio en esta ruta")
    args = ap.parse_args()

    # Cada etiqueta es un título y una sola línea: si no entra en la columna, frena.
    for _, titulo, linea in ETIQUETAS:
        for t, negrita in ((titulo, True), (linea, False)):
            if len(base.envolver(t, FS, W_COL, negrita)) != 1:
                raise SystemExit(f"la etiqueta {t!r} no entra en una línea de {W_COL} unidades")

    res = resolver()
    e0 = res["e0"]
    n_piezas, fallas = controlar_geometria(res)
    print(f"PDF: {REL_PDF}   sha256 {PDF_SHA256[:12]}… (comprobado; igual al del inventario "
          f"{REL_INVENTARIO})")
    print(f"     portada: {PORTADA[0]} · {PORTADA[1]} (comprobado)")
    print(f"E0:  {REL_CHUNKS}   sha256 {CHUNKS_SHA256[:12]}… (comprobado)")
    print(f"     {REL_ESTRUCTURA}   sha256 {ESTRUCTURA_SHA256[:12]}… (comprobado)")
    print(f"     página de {TO}::{PUNTO_TERMINAL}: {e0['pagina']}; página de "
          f"{TO}::{PUNTO_REMITIDO}: {e0['pagina_remitido']} (campo `paginas`)")
    print(f"     hijos de {PUNTO_CONTENEDOR}: {e0['hijos']}; {PUNTO_TERMINAL} sin hijos")
    print(f"PIE: {res['pie_texto']!r}")
    print(f"LÍNEAS en el PDF: {json.dumps(res['lineas'], ensure_ascii=False)}")
    print("ETIQUETAS (texto fijado; números comprobados) y ORIGEN de su línea guía (puntos PDF):")
    for clave, titulo, linea in ETIQUETAS:
        ox, oy = res["origenes"][clave]
        print(f"  {titulo} / {linea}   origen ({ox:.1f}, {oy:.1f})")
    print(f"FLECHA (puntos PDF): {[(round(x, 1), round(y, 1)) for x, y in res['flecha']]} y "
          f"baja en x = {res['x_flecha']:.1f} hasta el recorte")
    print(f"CORCHETE (puntos PDF): x = {res['corchete'][0]:.1f}, de {res['corchete'][1]:.1f} a "
          f"{res['corchete'][2]:.1f}")
    print("CONTROLES DE GEOMETRÍA: " + ("ok" if not fallas else "FALLA"))
    print(f"  piezas controladas: {n_piezas} contra {len(res['pg']['chars'])} caracteres con tinta "
          f"y {len(res['pg']['bordes'])} bordes de tabla; fallas: {len(fallas)}")
    for x in fallas:
        print(f"  MAL {x}")
    if fallas:
        raise SystemExit("FALLA: la geometría de líneas guía, flecha o corchete toca la página")

    pdf = pdfium.PdfDocument(os.path.join(RAIZ, REL_PDF))
    dims = {e0["pagina"]: (res["pg"]["ancho"], res["pg"]["alto"]),
            e0["pagina_remitido"]: (res["pr"]["ancho"], res["pr"]["alto"])}
    x0, x1 = res["x0"], res["x1"]
    pedidos = ((e0["pagina"], (x0, res["tramo_sup"][0], x1, res["tramo_sup"][1])),
               (e0["pagina"], (x0, res["tramo_pie"][0], x1, res["tramo_pie"][1])),
               (e0["pagina_remitido"], (x0, res["tramo_rem"][0], x1, res["tramo_rem"][1])))
    recortes, informe = [], []
    for pagina, caja in pedidos:
        png, efectiva, px = recortar(pdf, pagina, caja, dims[pagina])
        recortes.append((png, efectiva))
        informe.append(f"página {pagina} {tuple(round(v, 1) for v in efectiva)} pt -> {px} px")
    pdf.close()
    svg, geo = componer(res, recortes)
    print("RECORTES: " + "; ".join(informe))
    print(f"ESCALA: {res['escala']:.4f} unidades por punto PDF; ancho de página mostrado "
          f"{x1 - x0:.1f} pt en {W_PAGINA} de {W} unidades = {ANCHO_FIGURA_CM * W_PAGINA / W:.2f} cm; "
          f"columna de etiquetas {W_COL} unidades = {ANCHO_FIGURA_CM * W_COL / W:.2f} cm")
    print(f"ALTO: lienzo {W} x {geo['alto_total']:.1f}, impreso a {ANCHO_FIGURA_CM:.2f} x "
          f"{ANCHO_FIGURA_CM * geo['alto_total'] / W:.2f} cm")
    factor = ANCHO_FIGURA_PT * W_PAGINA / W / (x1 - x0)
    tmin, tmed, tmax = res["tamanos"]
    rmin, rmed, rmax = res["tamanos_rem"]
    print(f"LETRA a {ANCHO_FIGURA_CM:.0f} cm (factor de la página {factor:.4f}):")
    print(f"  página: {tmin}–{tmax} pt en el PDF (mediana {tmed}) -> "
          f"{tmin * factor:.2f}–{tmax * factor:.2f} pt impresos")
    print(f"  recorte del punto {PUNTO_REMITIDO}: {rmin}–{rmax} pt en el PDF -> "
          f"{rmin * factor:.2f}–{rmax * factor:.2f} pt impresos")
    print(f"  etiquetas: {FS} unidades -> {puntos_impresos(FS):.2f} pt impresos")
    if args.svg:
        with open(args.svg, "w", encoding="utf-8") as fh:
            fh.write(svg)
        print(f"SVG: {args.svg}")
    print(f"SVG sha256 {hashlib.sha256(svg.encode('utf-8')).hexdigest()}")
    exportar(svg)
    contenido, xobjetos, fecha = invariantes_pdf()
    print(f"PNG: {os.path.relpath(SALIDA_PNG, RAIZ)}   sha256 {sha256(SALIDA_PNG)}")
    print(f"PDF: {os.path.relpath(SALIDA_PDF, RAIZ)}   sha256 {sha256(SALIDA_PDF)}")
    print(f"     /CreationDate {fecha!r} (SOURCE_DATE_EPOCH={SOURCE_DATE_EPOCH})")
    print(f"     stream de contenido sha256 {contenido}")
    for x in xobjetos:
        print(f"     XObject sha256 {x}")
    if args.verificar and not verificar(geo["alto_total"]):
        raise SystemExit("FALLA: la verificación de medidas encontró defectos")


if __name__ == "__main__":
    main()
