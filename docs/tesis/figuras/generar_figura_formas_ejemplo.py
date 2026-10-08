#!/usr/bin/env python3
"""Figura «las formas del contenido en el ejemplo» para el análisis del documento (capítulo 3, sección 3.3).

Tres bloques de Clasificación de deudores, de arriba abajo, con el texto del
artefacto de unidades:
- en gris, el párrafo del 5.1.1: su título («5.1.1. Cartera comercial.») y el
  párrafo sin numerar que abre la excepción;
- en negro, el texto completo del 5.1.1.1, con sus cortes de línea originales;
- en gris, el 3.7: su título y su texto, sin marcas.
Debajo del texto del 5.1.1 y del 5.1.1.1, un subrayado por cada tramo marcado
(TRAMOS), en el color de su forma; un tramo anidado en otro va en un segundo
nivel, más abajo. Cada tramo tiene su rótulo al margen derecho, con el nombre
de la forma en minúscula y en el mismo color, unido al subrayado por una línea
guía: la figura no depende solo del color. Una flecha va de la remisión del
5.1.1.1 al bloque del 3.7, que es solo su destino. La figura no lleva nombres
de archivo, rutas, identificadores internos ni nombres de tipo del esquema.

Nada del contenido se tipea ni se supone:
- el artefacto de unidades es salida_enm01/chunks_cla.json, con candado de
  sha256 (CHUNKS_SHA256): el bloque del 5.1.1 son dos tramos de la herencia de
  la unidad del 5.1.1.1 (el encabezado y el párrafo sin numerar del 5.1.1); el
  del 5.1.1.1, el texto de esa unidad; el del 3.7, el texto de la suya;
- cada bloque se comprueba contra el PDF del corpus (candado de sha256 e
  inventario del conjunto de desarrollo), en la página que le asigna el
  artefacto (16 o 14): su texto tiene que estar tal cual en la página y cada
  línea tiene que ser una línea de la página. Si no, el script frena antes de
  dibujar y muestra la diferencia;
- cada tramo tiene que ser un fragmento literal del texto de su bloque, una
  sola vez, tomando los cortes de línea como espacios y el guion de corte
  («pro-» / «ductiva») como parte de la palabra, y tiene que estar en la
  página del PDF con la misma normalización; un tramo anidado tiene que caer
  dentro del suyo y dos tramos no pueden solaparse de otro modo; el bloque al
  que llega la flecha no lleva marcas. Si no, el script frena antes de
  dibujar;
- el texto propio de la figura son los rótulos, fijos en TRAMOS; el script
  comprueba que cada uno empiece con el nombre de su forma, que su partición
  en líneas no cambie el texto y que ninguno lleve un nombre de tipo o de
  relación del esquema;
- los subrayados se ubican midiendo cada línea con las métricas reales de
  Helvetica; sin ellas, el script no dibuja.

Controles, en cada corrida (el script frena si fallan): los de geometría y de
margen de generar_figura_formacion_to.py (ningún texto por debajo de 7 pt
impresos a 15 cm, fuera del lienzo, superpuesto a otro, fuera de la caja que
lo contiene, cortado por el borde de otra caja ni tocado por una marca; ningún
texto ni elemento dibujado a menos de 2 mm de un borde) y uno de trazos:
ningún subrayado, línea guía o tramo de la flecha a menos de DISTANCIA_MIN de
un trazo de otro tramo. Además, lo dibujado reconstruye el texto de cada
bloque y ningún texto dibujado lleva nombres de archivo, rutas o
identificadores internos.

Reutiliza por importación, como las figuras hermanas: de
generar_figura_norma_a_grafo.py, la tipografía, el naranja de la remisión, el
escape y formato del SVG, la exportación a PNG a 300 dpi con la densidad
grabada y el medidor con métricas reales de Helvetica; de
generar_figura_proceso_extraccion.py, el ancho de texto de 15 cm.

El SVG es intermedio: se pasa a rsvg-convert por la entrada estándar y no se
escribe salvo con --svg. Salidas: figura_formas_ejemplo.png y
figura_formas_ejemplo.pdf, las dos byte-reproducibles (el PDF, con la fecha de
creación fijada por SOURCE_DATE_EPOCH).

Uso (desde la raíz del repo):
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_formas_ejemplo.py
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_formas_ejemplo.py --svg <ruta>
"""

import argparse
import hashlib
import json
import math
import os
import re
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET

sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import generar_figura_norma_a_grafo as base          # noqa: E402
import generar_figura_proceso_extraccion as proc     # noqa: E402

import pdfplumber                                     # noqa: E402

RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", ".."))
SALIDA_PNG = os.path.join(AQUI, "figura_formas_ejemplo.png")
SALIDA_PDF = os.path.join(AQUI, "figura_formas_ejemplo.pdf")

# --------------------------------------------------------------------------- #
# Fuentes y candados                                                           #
# --------------------------------------------------------------------------- #
REL_PDF = "data/experiment/subset/TO_clasificacion_deudores_actual.pdf"
REL_INVENTARIO = "data/experiment/reextraccion_v2/manifiestos/desarrollo_5tos.json"
REL_CHUNKS = "data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_cla.json"
PDF_SHA256 = "6e7f528d3fea7b756f15e1278eecd828f203f0651fc6f778212033de6a0883e2"
CHUNKS_SHA256 = "98808886a406d8321c678836a55f92eea983d594d95358dd21ceb537487ac0b1"
TO = "cla"
# Versión del corpus: la portada debe decir las dos cosas.
PORTADA = ("“A” 8378", "19/12/2025")

# Los tres bloques, de arriba abajo. «partes» es "texto" (el texto propio de la
# unidad) o los tramos de su herencia, como (tipo, unidad de origen), en el
# orden del artefacto; «pagina», la del PDF donde tiene que estar (la que le
# asigna el artefacto); «sep», el aire sobre el bloque. El bloque del 5.1.1
# tiene que dar exactamente las dos líneas de LINEAS_5_1_1.
BLOQUES = (
    {"clave": "5.1.1", "id": f"{TO}::5.1.1.1", "partes": (("encabezado", "5.1.1"), ("intro", "5.1.1")),
     "pagina": 16, "gris": True, "sep": 0},
    {"clave": "5.1.1.1", "id": f"{TO}::5.1.1.1", "partes": "texto", "pagina": 16, "gris": False,
     "sep": 9},
    {"clave": "3.7", "id": f"{TO}::3.7", "partes": "texto", "pagina": 14, "gris": True, "sep": 22},
)
LINEAS_5_1_1 = ("5.1.1. Cartera comercial.",
                "Abarca todas las financiaciones comprendidas, con excepción de las siguientes:")

# Tramos marcados: su texto literal (los cortes de línea como espacios y el
# guion de corte dentro de la palabra), su bloque, su forma, el tramo que lo
# contiene si está anidado y su rótulo, partido en líneas para que entre en el
# margen derecho.
TRAMOS = (
    {"clave": "excepcion", "bloque": "5.1.1", "texto": "con excepción de las siguientes",
     "forma": "excepción", "dentro_de": None,
     "rotulo": "excepción (abierta en el 5.1.1)", "lineas_rotulo": ("excepción", "(abierta en el 5.1.1)")},
    {"clave": "condicion_importe", "bloque": "5.1.1.1",
     "texto": "que superen el equivalente a dos veces el importe de referencia establecido en el punto 3.7.",
     "forma": "condición", "dentro_de": None, "rotulo": "condición", "lineas_rotulo": ("condición",)},
    {"clave": "umbral", "bloque": "5.1.1.1", "texto": "dos veces el importe de referencia",
     "forma": "umbral", "dentro_de": "condicion_importe", "rotulo": "umbral",
     "lineas_rotulo": ("umbral",)},
    {"clave": "remision", "bloque": "5.1.1.1", "texto": "establecido en el punto 3.7.",
     "forma": "remisión", "dentro_de": "condicion_importe", "rotulo": "remisión",
     "lineas_rotulo": ("remisión",)},
    {"clave": "condicion_repago", "bloque": "5.1.1.1",
     "texto": ("cuyo repago no se encuentre vinculado a ingresos fijos o periódicos del cliente sino "
               "a la evolución de su actividad productiva o comercial"),
     "forma": "condición", "dentro_de": None, "rotulo": "condición", "lineas_rotulo": ("condición",)},
    {"clave": "acto", "bloque": "5.1.1.1", "texto": "se incluirán dentro de la cartera comercial",
     "forma": "acto regulado", "dentro_de": None, "rotulo": "acto regulado",
     "lineas_rotulo": ("acto regulado",)},
)
# La flecha sale de este tramo y llega al bloque del punto al que remite, que
# no lleva marcas: es solo el destino de la flecha.
FLECHA_DESDE = "remision"
RX_PUNTO_REMITIDO = re.compile(r"en el punto (\d+(?:\.\d+)*)\.$")

# Color de cada forma: el del subrayado y su línea guía, y el de su rótulo.
# Tonos de la paleta compartida (generar_figura_norma_a_grafo.py:81-90); la
# remisión lleva el naranja de las remisiones de las figuras del ejemplo, y su
# rótulo, el mismo tono oscurecido para leer sobre blanco (ACENTO_TEXTO).
COLOR_FORMA = {
    "excepción": ("#6d597a", "#6d597a"),
    "condición": ("#2a6f97", "#2a6f97"),
    "umbral": ("#b23a48", "#b23a48"),
    "remisión": (base.ACENTO, base.ACENTO_TEXTO),
    "acto regulado": ("#52796f", "#52796f"),
}
# Nada de esto puede aparecer en un texto dibujado (como en
# generar_figura_unidad_extraccion.py).
PROHIBIDOS = (re.compile(r"extractor", re.I), re.compile(r"::"), re.compile(r"\.(json|pdf|py|md)\b"),
              re.compile(r"/"), re.compile(r"\bcla\b"), re.compile(r"chunk", re.I))
# Nombres de tipo y de relación del esquema, que ningún rótulo puede llevar:
# los tipos de nodo de r1 (corpus_v2/salida_r1/kg.json) y los tipos y
# predicados del perfil r2 (pyd_r2/generados/enums_r2.json en eb277ce).
NOMBRES_ESQUEMA = ("Comunicacion", "TextoOrdenado", "Operacion", "Restriccion", "Excepcion",
                   "Obligacion", "Sujeto", "Potestad", "Condicion", "Definicion",
                   "establecida_en", "referencia", "modificada_por", "aplica_a", "regula", "exceptua",
                   "exceptua_obligacion", "prohibe", "limita", "ejecuta", "requiere", "condiciona",
                   "condicion_de")

# --------------------------------------------------------------------------- #
# Tamaño impreso: 15 cm de ancho                                               #
# --------------------------------------------------------------------------- #
W = proc.W                                            # 720 unidades de lienzo
ANCHO_FIGURA_CM = proc.ANCHO_TEXTO_CM                 # 15,00
ANCHO_FIGURA_PT = ANCHO_FIGURA_CM * proc.PT_POR_CM    # 425,2
DPI = base.DPI                                        # 300
ANCHO_PNG_PX = round(ANCHO_FIGURA_CM / 2.54 * DPI)    # 1772
PT_MINIMO = 7.0
# Margen a los cuatro bordes (el de generar_figura_formacion_to.py): ningún
# texto ni trazo a menos de MARGEN_MM impresos; la composición deja MARGEN.
MARGEN_MM = 2.0
MARGEN_MIN = MARGEN_MM * W / (ANCHO_FIGURA_CM * 10)   # 9,6 unidades
MARGEN = 11                                           # 2,29 mm


def puntos_impresos(unidades):
    """Tamaño en puntos de `unidades` del lienzo con la figura a 15 cm."""
    return unidades * ANCHO_FIGURA_PT / W


TIPOGRAFIA = base.TIPOGRAFIA
TRAZO = "#4a5a6a"                   # gris oscuro de la paleta compartida
BORDE = "#999999"
FONDO_BLOQUE = "#f4f6f8"
TINTA = "#1f1f1f"                   # negro: el texto del 5.1.1.1
TINTA_SUAVE = "#555555"             # gris: el párrafo del 5.1.1 y el 3.7
esc, f = base.esc, base.f

FS = 13                 # texto transcripto y rótulos (7,68 pt impresos)
IL = 27                 # interlínea del texto: deja lugar a dos niveles de subrayado y un carril
IL_ROT = 16             # interlínea de los rótulos de dos líneas
DY_CENTRO = FS * 0.28   # de la línea de base al centro de la caja del texto
# Debajo de cada línea de base: los dos niveles de subrayado y el carril por
# donde corre una guía que baja desde el final de un tramo.
DY_NIVEL = {1: 5.2, 2: 9.6}
DY_CARRIL = 13.2
GROSOR_MARCA = 1.5
GROSOR_GUIA = 0.8
GROSOR_FLECHA = 1.6
DISTANCIA_MIN = 2.5     # entre los ejes de dos trazos de tramos distintos

X_FLECHA = MARGEN + 4   # calle izquierda: el tramo vertical de la flecha
X_BLOQUE = 32
PAD_X = 7
X_TEXTO = X_BLOQUE + PAD_X
W_BLOQUE = 523          # la línea más larga (la segunda del 3.7) mide 502,9 a FS
X_BORDE_DER = X_BLOQUE + W_BLOQUE
X_CODO = X_BORDE_DER + 5            # donde una guía deja la horizontal
X_ROT = 582                         # columna de los rótulos
SEP_GUIA_ROT = 5                    # entre el final de la guía y su rótulo
SEP_ROTULOS = 3                     # entre las cajas de dos rótulos
PAD_SUP = 6                         # del borde superior del bloque a la primera línea
ABAJO = 19                          # de la última línea de base al borde inferior

RX_NUMERO = re.compile(r"^(\d+(?:\.\d+)*)\.\s")


def sha256(ruta):
    with open(ruta, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def norm(s):
    """Guiones de fin de línea fuera y blancos colapsados (regla R7 de U-INSUMOS-CAP)."""
    return re.sub(r"\s+", " ", s.replace("-\n", "")).strip()


def candado(rel, esperado):
    s = sha256(os.path.join(RAIZ, rel))
    if s != esperado:
        raise SystemExit(f"{rel} no es el verificado: sha {s[:12]}… ≠ {esperado[:12]}…")


def freno(motivo, evidencia=()):
    """Frena antes de dibujar, con la evidencia."""
    lineas = [f"FRENO antes de dibujar: {motivo}"] + [f"  {x}" for x in evidencia]
    raise SystemExit("\n".join(lineas))


# --------------------------------------------------------------------------- #
# Texto normalizado y tramos                                                   #
# --------------------------------------------------------------------------- #
def mapa(lineas):
    """Texto del bloque con los cortes de línea como espacios y el guion de
    corte dentro de la palabra (un «-» al final de una línea que no es la
    última se quita y la línea se une a la siguiente sin espacio), y, por cada
    carácter, su (línea, columna); None para el espacio de un corte de línea.
    Devuelve también los cortes con guion, como (línea, «pro-», «ductiva»)."""
    chars, pos, cortes = [], [], []
    for k, s in enumerate(lineas):
        corte = k + 1 < len(lineas) and s.endswith("-")
        if corte:
            cortes.append((k, s.rsplit(" ", 1)[-1], lineas[k + 1].split(" ", 1)[0]))
        for c, ch in enumerate(s[:-1] if corte else s):
            chars.append(ch)
            pos.append((k, c))
        if k + 1 < len(lineas) and not corte:
            chars.append(" ")
            pos.append(None)
    return "".join(chars), pos, cortes


def segmentar(lineas, pos, i, j):
    """Segmentos (línea, columna inicial, columna final) del tramo [i, j) del
    texto normalizado. El guion de corte va con la parte de la palabra que
    queda en su línea."""
    por_linea = {}
    for p in pos[i:j]:
        if p is not None:
            por_linea.setdefault(p[0], []).append(p[1])
    ks = sorted(por_linea)
    if ks != list(range(ks[0], ks[-1] + 1)):
        raise SystemExit(f"tramo en líneas no consecutivas: {ks}")
    segs = []
    for k in ks:
        c0, c1 = min(por_linea[k]), max(por_linea[k]) + 1
        if k + 1 in por_linea and lineas[k].endswith("-") and c1 == len(lineas[k]) - 1:
            c1 += 1
        segs.append((k, c0, c1))
    # Las líneas intermedias van enteras; la primera llega al final de su
    # línea y la última empieza al comienzo de la suya.
    for n, (k, c0, c1) in enumerate(segs):
        if (n > 0 and c0 != 0) or (n + 1 < len(segs) and c1 != len(lineas[k])):
            raise SystemExit(f"tramo partido en la línea {k + 1}: columnas {c0}-{c1}")
    return segs


# --------------------------------------------------------------------------- #
# Carga y comprobaciones                                                       #
# --------------------------------------------------------------------------- #
def anclas_artefacto(ids):
    """Línea del artefacto donde está cada texto de cada unidad: el `texto`
    propio (sangría de 2) y el de cada tramo de la herencia (sangría de 4), en
    orden (como en generar_figura_unidad_extraccion.py)."""
    with open(os.path.join(RAIZ, REL_CHUNKS), encoding="utf-8") as fh:
        lineas = fh.read().split("\n")
    out = {}
    for cid in ids:
        inicio = [i for i, x in enumerate(lineas) if x == f'  "id": "{cid}",']
        if len(inicio) != 1:
            raise SystemExit(f"artefacto: el id {cid} aparece {len(inicio)} veces")
        i = inicio[0] + 1
        propio, herencia = None, []
        while i < len(lineas) and not lineas[i].startswith('  "id": '):
            x = lineas[i]
            if x.startswith('  "texto": '):
                propio = (i + 1, json.loads("{" + x.strip().rstrip(",") + "}")["texto"])
            elif x.startswith('    "texto": '):
                herencia.append((i + 1, json.loads("{" + x.strip().rstrip(",") + "}")["texto"]))
            i += 1
        out[cid] = {"inicio": inicio[0] + 1, "texto": propio, "herencia": herencia}
    return out


def piezas_del_bloque(b, ch, anclas):
    """Las piezas de texto del artefacto que forman el bloque, en orden:
    (nombre, texto, línea del artefacto)."""
    a = anclas[b["id"]]
    if b["partes"] == "texto":
        if ch["paginas"] != [b["pagina"]]:
            raise SystemExit(f"{b['id']}: el artefacto no lo pone entero en la página {b['pagina']}")
        if not ch["texto"].startswith(f"{ch['unidad']}. {ch['titulo']}\n"):
            raise SystemExit(f"{b['id']}: el texto no empieza con su número y su título")
        return [("texto", ch["texto"], a["texto"])]
    if len(a["herencia"]) != len(ch["herencia"]):
        raise SystemExit(f"{b['id']}: anclas de la herencia incompletas")
    claves = [(h["tipo"], h["unidad_origen"]) for h in ch["herencia"]]
    ks = [claves.index(p) if p in claves else None for p in b["partes"]]
    if None in ks or ks != list(range(ks[0], ks[0] + len(ks))) or len(set(claves)) != len(claves):
        raise SystemExit(f"{b['id']}: la herencia no tiene {b['partes']} consecutivos: {claves}")
    out = []
    for k in ks:
        h = ch["herencia"][k]
        if h["paginas"] != [b["pagina"]]:
            raise SystemExit(f"{b['id']} herencia {k + 1}: no está en la página {b['pagina']}")
        out.append((f"herencia {k + 1}: {h['tipo']} de {h['unidad_origen']}", h["texto"], a["herencia"][k]))
    return out


def resolver():
    candado(REL_PDF, PDF_SHA256)
    candado(REL_CHUNKS, CHUNKS_SHA256)
    with open(os.path.join(RAIZ, REL_INVENTARIO), encoding="utf-8") as fh:
        inv = [t for t in json.load(fh)["tos"] if t["id"] == TO]
    if len(inv) != 1 or inv[0]["sha256_pdf"] != PDF_SHA256 or inv[0]["pdf"] != REL_PDF:
        raise SystemExit("el inventario del conjunto de desarrollo no declara este PDF para cla")
    with open(os.path.join(RAIZ, REL_CHUNKS), encoding="utf-8") as fh:
        lista = json.load(fh)
    chunks = {c["id"]: c for c in lista}
    if len(chunks) != len(lista):
        raise SystemExit("artefacto: ids repetidos")
    paginas = sorted({b["pagina"] for b in BLOQUES})
    with pdfplumber.open(os.path.join(RAIZ, REL_PDF)) as doc:
        portada = [l["text"] for l in doc.pages[0].extract_text_lines()]
        if not all(any(p in x for x in portada) for p in PORTADA):
            raise SystemExit(f"la portada no dice la versión del corpus {PORTADA}")
        pdf = {n: {"crudo": doc.pages[n - 1].extract_text(),
                   "lineas": [l["text"] for l in doc.pages[n - 1].extract_text_lines()]}
               for n in paginas}

    # Cada bloque: sus piezas del artefacto, cada una tal cual en su página.
    anclas = anclas_artefacto(sorted({b["id"] for b in BLOQUES}))
    bloques = {}
    for b in BLOQUES:
        ch = chunks[b["id"]]
        pg = pdf[b["pagina"]]
        piezas = []
        for nombre, s, (linea_art, s_art) in piezas_del_bloque(b, ch, anclas):
            if s_art != s:
                raise SystemExit(f"{b['id']} {nombre}: la línea {linea_art} del artefacto no da ese texto")
            faltan = [x for x in s.split("\n") if x not in pg["lineas"]]
            if s not in pg["crudo"] or faltan:
                freno(f"el bloque {b['clave']} ({nombre}) difiere de la página {b['pagina']} del PDF",
                      [f"artefacto: {x!r}" for x in s.split("\n")]
                      + [f"no es una línea de la página: {x!r}" for x in faltan]
                      + [f"página: {x!r}" for x in pg["lineas"]])
            piezas.append({"nombre": nombre, "texto": s, "linea_artefacto": linea_art,
                           "lineas_pdf": [pg["lineas"].index(x) + 1 for x in s.split("\n")]})
        lineas = [x for p in piezas for x in p["texto"].split("\n")]
        if b["clave"] == "5.1.1" and tuple(lineas) != LINEAS_5_1_1:
            freno("el bloque del 5.1.1 no son las dos líneas fijadas", [repr(x) for x in lineas])
        normalizado, pos, cortes = mapa(lineas)
        if normalizado != norm("\n".join(lineas)):
            raise SystemExit(f"bloque {b['clave']}: la normalización no es la de la regla R7")
        bloques[b["clave"]] = {"id": b["id"], "unidad": ch["unidad"], "piezas": piezas,
                               "lineas": lineas, "normalizado": normalizado, "pos": pos,
                               "cortes": cortes, "pagina": b["pagina"], "gris": b["gris"]}

    # Cada tramo: literal y único en el texto de su bloque, y en la página.
    tramos = {}
    for t in TRAMOS:
        blk = bloques[t["bloque"]]
        n = blk["normalizado"].count(t["texto"])
        pagina_norm = norm(pdf[blk["pagina"]]["crudo"])
        n_pdf = pagina_norm.count(t["texto"])
        if n != 1 or n_pdf < 1:
            freno(f"el tramo «{t['texto']}» no es literal y único en el bloque {t['bloque']} "
                  f"({n} apariciones) o no está en la página {blk['pagina']} ({n_pdf})",
                  [f"bloque normalizado: {blk['normalizado']!r}"])
        i = blk["normalizado"].index(t["texto"])
        j = i + len(t["texto"])
        segs = segmentar(blk["lineas"], blk["pos"], i, j)
        tramos[t["clave"]] = dict(t, i=i, j=j, segmentos=segs, n_pdf=n_pdf,
                                  dibujado=[blk["lineas"][k][c0:c1] for k, c0, c1 in segs])

    # Anidamiento: el anidado cae dentro del suyo; dos tramos del mismo bloque
    # están separados o uno contiene al otro; el nivel es la profundidad.
    def nivel(clave):
        p = tramos[clave]["dentro_de"]
        return 1 if p is None else nivel(p) + 1

    for t in tramos.values():
        p = t["dentro_de"]
        if p is not None:
            q = tramos[p]
            if q["bloque"] != t["bloque"] or not (q["i"] <= t["i"] and t["j"] <= q["j"]):
                freno(f"el tramo «{t['texto']}» no cae dentro de «{q['texto']}»")
        t["nivel"] = nivel(t["clave"])
    for a in tramos.values():
        for b in tramos.values():
            if a["clave"] < b["clave"] and a["bloque"] == b["bloque"]:
                separados = a["j"] <= b["i"] or b["j"] <= a["i"]
                anidados = a["dentro_de"] == b["clave"] or b["dentro_de"] == a["clave"]
                if not separados and not anidados:
                    freno(f"los tramos «{a['texto']}» y «{b['texto']}» se solapan sin anidarse")
                if anidados and a["nivel"] == b["nivel"]:
                    raise SystemExit("dos tramos anidados en el mismo nivel")
    if max(t["nivel"] for t in tramos.values()) > max(DY_NIVEL):
        raise SystemExit("más niveles de anidamiento que los previstos")

    # Rótulos: empiezan con el nombre de su forma, la partición no cambia el
    # texto, la forma tiene color y ningún rótulo lleva nombres del esquema.
    for t in tramos.values():
        if " ".join(t["lineas_rotulo"]) != t["rotulo"] or not t["rotulo"].startswith(t["forma"]):
            raise SystemExit(f"rótulo {t['rotulo']!r} mal formado")
        if t["forma"] not in COLOR_FORMA or t["forma"] != t["forma"].lower():
            raise SystemExit(f"forma {t['forma']!r} sin color o no en minúscula")
        palabras = re.findall(r"[^\s()]+", t["rotulo"])
        if any(p in NOMBRES_ESQUEMA for p in palabras):
            raise SystemExit(f"el rótulo {t['rotulo']!r} lleva un nombre del esquema")
    if len({c for c, _ in COLOR_FORMA.values()}) != len(COLOR_FORMA):
        raise SystemExit("dos formas con el mismo color")

    # La flecha: de la remisión del 5.1.1.1 al bloque del punto remitido.
    rem = tramos[FLECHA_DESDE]
    m = RX_PUNTO_REMITIDO.search(rem["texto"])
    destino = [c for c, blk in bloques.items() if m and blk["unidad"] == m.group(1)]
    if rem["forma"] != "remisión" or len(destino) != 1 or destino[0] == rem["bloque"]:
        raise SystemExit("la flecha no va de una remisión al bloque del punto remitido")
    marcados = [t["texto"] for t in tramos.values() if t["bloque"] == destino[0]]
    if marcados:
        freno(f"el bloque {destino[0]}, destino de la flecha, lleva marcas",
              [f"tramo: «{x}»" for x in marcados])
    return {"bloques": bloques, "tramos": tramos, "portada": portada, "destino": destino[0],
            "anclas": anclas, "n_chunks": len(chunks)}


# --------------------------------------------------------------------------- #
# Composición                                                                  #
# --------------------------------------------------------------------------- #
REGISTRO = []   # textos dibujados
CAJAS = {}      # cajas que contienen texto: clave -> (x0, y0, x1, y1)
MARCAS = []     # cajas de los trazos, que ningún texto puede tocar: (nombre, caja)
TRAZOS = []     # segmentos de los trazos: (tramo dueño, nombre, punto, punto)
MEDIR = None    # métricas reales de Helvetica (base.medidor)


def texto(partes, x, y, s, fs, negrita=False, relleno=TINTA, contexto="", dentro=None,
          fuente=None):
    peso = "bold" if negrita else "normal"
    partes.append(f'<text x="{f(x)}" y="{f(y)}" font-size="{fs}" font-weight="{peso}" '
                  f'fill="{relleno}">{esc(s)}</text>')
    REGISTRO.append({"s": s, "fs": fs, "negrita": negrita, "x": x, "y": y, "ancla": "start",
                     "relleno": relleno, "contexto": contexto, "dentro": dentro, "fuente": fuente})


def rect(partes, x0, y0, x1, y1, borde, grosor, relleno="none", rx=0):
    partes.append(f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(x1 - x0)}" height="{f(y1 - y0)}" '
                  f'rx="{rx}" fill="{relleno}" stroke="{borde}" stroke-width="{grosor}"/>')


def trazo(partes, puntos, color, grosor, dueno, nombre, flecha=False):
    """Polilínea; registra cada segmento para los controles de trazos y de
    geometría (caja con medio grosor y 0,3 de holgura)."""
    d = " ".join(("M" if i == 0 else "L") + f"{f(x)},{f(y)}" for i, (x, y) in enumerate(puntos))
    m = ' marker-end="url(#punta)"' if flecha else ""
    partes.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{grosor}"{m}/>')
    h = grosor / 2.0 + 0.3
    for n, (p, q) in enumerate(zip(puntos, puntos[1:]), start=1):
        TRAZOS.append((dueno, f"{nombre}, tramo {n}", p, q))
        MARCAS.append((f"{nombre}, tramo {n}", (min(p[0], q[0]) - h, min(p[1], q[1]) - h,
                                                max(p[0], q[0]) + h, max(p[1], q[1]) + h)))
    if flecha:
        # La punta: 6 veces el grosor de largo y de ancho, con la punta a una
        # décima de su largo más allá del final del trazo.
        (x0, y0), (x1, y1) = puntos[-2], puntos[-1]
        if y0 != y1 or x1 <= x0:
            raise SystemExit("la flecha tiene que llegar en horizontal, hacia la derecha")
        largo = 6 * grosor
        MARCAS.append((f"{nombre}, punta", (x1 - 0.9 * largo, y1 - largo / 2, x1 + 0.1 * largo,
                                            y1 + largo / 2)))


def repartir(deseadas, altos):
    """Ubica los rótulos en la columna: cada uno lo más cerca posible de la y
    de su guía, en el mismo orden, sin que dos cajas queden a menos de
    SEP_ROTULOS. `altos` da, por rótulo, cuánto ocupa arriba y abajo de su y.
    Los rótulos que chocan se agrupan y el grupo se centra en el promedio de
    sus desplazamientos."""
    n = len(deseadas)
    paso = [altos[i][1] + SEP_ROTULOS + altos[i + 1][0] for i in range(n - 1)]
    grupos = []   # [primero, último, y del primero]
    for i in range(n):
        grupos.append([i, i, deseadas[i]])
        while True:
            g = grupos[-1]
            off, acum = [], 0.0
            for k in range(g[0], g[1] + 1):
                off.append(acum)
                if k < g[1]:
                    acum += paso[k]
            g[2] = sum(deseadas[k] - o for k, o in zip(range(g[0], g[1] + 1), off)) / len(off)
            if len(grupos) > 1:
                p = grupos[-2]
                y_ult = p[2] + sum(paso[k] for k in range(p[0], p[1]))
                if g[2] < y_ult + paso[p[1]]:
                    grupos[-2:] = [[p[0], g[1], 0.0]]
                    continue
            break
    ys = []
    for a, b, y in grupos:
        for k in range(a, b + 1):
            ys.append(y)
            if k < b:
                y += paso[k]
    return ys


def componer(res):
    del REGISTRO[:]
    CAJAS.clear()
    del MARCAS[:]
    del TRAZOS[:]
    partes = []
    base_linea = {}   # (bloque, línea) -> y de la línea de base
    y = MARGEN
    for b in BLOQUES:
        blk = res["bloques"][b["clave"]]
        y += b["sep"]
        lineas = blk["lineas"]
        alto = PAD_SUP + FS * 0.78 + (len(lineas) - 1) * IL + ABAJO
        clave = f"bloque {b['clave']}"
        if b["gris"]:
            rect(partes, X_BLOQUE, y, X_BORDE_DER, y + alto, BORDE, "1", FONDO_BLOQUE, rx=2)
        else:
            rect(partes, X_BLOQUE, y, X_BORDE_DER, y + alto, TRAZO, "1.3", "white", rx=2)
        CAJAS[clave] = (X_BLOQUE, y, X_BORDE_DER, y + alto)
        yb = y + PAD_SUP + FS * 0.78
        for k, s in enumerate(lineas):
            texto(partes, X_TEXTO, yb, s, FS, relleno=TINTA_SUAVE if b["gris"] else TINTA,
                  contexto=clave, dentro=clave, fuente=(b["clave"], k))
            base_linea[(b["clave"], k)] = yb
            yb += IL
        y += alto
    y_fin_bloques = y

    def x_col(bloque, k, c):
        return X_TEXTO + MEDIR(res["bloques"][bloque]["lineas"][k][:c], FS, False)

    # Subrayados, y el comienzo de la guía de cada tramo: desde el final del
    # primer segmento que llega al final de su línea, en horizontal; si
    # ninguno llega, desde el final del tramo, bajando al carril.
    guias = []
    for t in res["tramos"].values():
        color = COLOR_FORMA[t["forma"]][0]
        lineas = res["bloques"][t["bloque"]]["lineas"]
        for k, c0, c1 in t["segmentos"]:
            yn = base_linea[(t["bloque"], k)] + DY_NIVEL[t["nivel"]]
            trazo(partes, [(x_col(t["bloque"], k, c0), yn), (x_col(t["bloque"], k, c1), yn)], color,
                  GROSOR_MARCA, t["clave"], f"subrayado {t['clave']}, línea {k + 1}")
        al_final = [(k, c1) for k, _, c1 in t["segmentos"] if c1 == len(lineas[k])]
        if al_final:
            k, c1 = al_final[0]
            yn = base_linea[(t["bloque"], k)] + DY_NIVEL[t["nivel"]]
            puntos, modo = [(x_col(t["bloque"], k, c1), yn), (X_CODO, yn)], f"al final de la línea {k + 1}"
        else:
            k, _, c1 = t["segmentos"][-1]
            yn = base_linea[(t["bloque"], k)] + DY_NIVEL[t["nivel"]]
            yc = base_linea[(t["bloque"], k)] + DY_CARRIL
            x = x_col(t["bloque"], k, c1)
            puntos, modo = [(x, yn), (x, yc), (X_CODO, yc)], f"baja al carril de la línea {k + 1}"
        guias.append({"tramo": t, "puntos": puntos, "modo": modo})

    # Rótulos: en el orden de sus guías, repartidos en la columna.
    guias.sort(key=lambda g: g["puntos"][-1][1])
    altos = [(FS * 0.78 - DY_CENTRO, FS * 0.22 + DY_CENTRO + (len(g["tramo"]["lineas_rotulo"]) - 1) * IL_ROT)
             for g in guias]
    ys = repartir([g["puntos"][-1][1] for g in guias], altos)
    y_max = y_fin_bloques
    for g, yr in zip(guias, ys):
        t = g["tramo"]
        trazo_c, texto_c = COLOR_FORMA[t["forma"]]
        g["y_rotulo"] = yr
        trazo(partes, g["puntos"] + [(X_ROT - SEP_GUIA_ROT, yr)], trazo_c, GROSOR_GUIA, t["clave"],
              f"guía {t['clave']}")
        for j, s in enumerate(t["lineas_rotulo"]):
            texto(partes, X_ROT, yr + DY_CENTRO + j * IL_ROT, s, FS, relleno=texto_c,
                  contexto=f"rótulo {t['clave']}", fuente=("rótulo", t["clave"]))
        y_max = max(y_max, yr + DY_CENTRO + (len(t["lineas_rotulo"]) - 1) * IL_ROT + FS * 0.22)

    # La flecha: baja del comienzo de la remisión al carril de su línea, corre
    # a la izquierda hasta la calle, baja y entra al bloque remitido a la
    # altura del centro de su primera línea.
    rem = res["tramos"][FLECHA_DESDE]
    k, c0, _ = rem["segmentos"][0]
    xs = x_col(rem["bloque"], k, c0)
    yn = base_linea[(rem["bloque"], k)] + DY_NIVEL[rem["nivel"]]
    yc = base_linea[(rem["bloque"], k)] + DY_CARRIL
    yd = base_linea[(res["destino"], 0)] - DY_CENTRO
    puntos_flecha = [(xs, yn), (xs, yc), (X_FLECHA, yc), (X_FLECHA, yd), (X_BLOQUE - 1, yd)]
    trazo(partes, puntos_flecha, COLOR_FORMA[rem["forma"]][0], GROSOR_FLECHA, rem["clave"],
          "flecha de la remisión", flecha=True)
    caja_destino = CAJAS[f"bloque {res['destino']}"]
    if not (caja_destino[1] < yd < caja_destino[3]):
        raise SystemExit("la flecha no llega al bloque remitido")

    alto_total = y_max + MARGEN
    alto_cm = ANCHO_FIGURA_CM * alto_total / W
    cabeza = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{ANCHO_FIGURA_CM:.2f}cm" '
        f'height="{alto_cm:.2f}cm" viewBox="0 0 {W} {f(alto_total)}" font-family="{TIPOGRAFIA}">',
        f'<rect width="{W}" height="{f(alto_total)}" fill="white"/>',
        '<defs><marker id="punta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
        f'markerHeight="6" orient="auto"><path d="M0,0L10,5L0,10z" '
        f'fill="{COLOR_FORMA[rem["forma"]][0]}"/></marker></defs>',
    ]
    return "\n".join(cabeza + partes + ["</svg>"]) + "\n", alto_total, guias, puntos_flecha


def comprobar_transcripcion(res):
    """Lo dibujado, reconstruido por bloque, es el texto del artefacto, en su
    caja y en su color; cada rótulo es el fijado, en el color de su forma; y
    ningún texto dibujado lleva nombres de archivo, rutas o identificadores
    internos."""
    for b in BLOQUES:
        blk = res["bloques"][b["clave"]]
        dibujado = [r for r in REGISTRO if r["fuente"] and r["fuente"][0] == b["clave"]]
        if "\n".join(r["s"] for r in dibujado) != "\n".join(p["texto"] for p in blk["piezas"]):
            raise SystemExit(f"bloque {b['clave']}: lo dibujado no es el texto del artefacto")
        color = TINTA_SUAVE if b["gris"] else TINTA
        if any(r["relleno"] != color or r["dentro"] != f"bloque {b['clave']}" for r in dibujado):
            raise SystemExit(f"bloque {b['clave']}: una línea fuera de su caja o de su color")
    for t in res["tramos"].values():
        dibujado = [r for r in REGISTRO if r["fuente"] == ("rótulo", t["clave"])]
        if tuple(r["s"] for r in dibujado) != t["lineas_rotulo"]:
            raise SystemExit(f"el rótulo de {t['clave']} no es el fijado")
        if any(r["relleno"] != COLOR_FORMA[t["forma"]][1] for r in dibujado):
            raise SystemExit(f"el rótulo de {t['clave']} no va en el color de su forma")
    for r in REGISTRO:
        for rx in PROHIBIDOS:
            if rx.search(r["s"]):
                raise SystemExit(f"texto prohibido en la figura ({rx.pattern}): {r['s']!r}")


# --------------------------------------------------------------------------- #
# Controles de geometría y medidas (los de generar_figura_formacion_to.py)     #
# --------------------------------------------------------------------------- #
def cruza(a, b):
    return a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]


def contiene(c, b):
    return c[0] <= b[0] and b[2] <= c[2] and c[1] <= b[1] and b[3] <= c[3]


def controlar_geometria(alto_total):
    fallas, cajas = [], []
    tamanos = {}
    for r in REGISTRO:
        a = MEDIR(r["s"], r["fs"], r["negrita"])
        x0 = {"start": r["x"], "middle": r["x"] - a / 2.0, "end": r["x"] - a}[r["ancla"]]
        bb = (x0, r["y"] - r["fs"] * 0.78, x0 + a, r["y"] + r["fs"] * 0.22)
        cajas.append((r, bb))
        pt = puntos_impresos(r["fs"])
        tamanos[r["fs"]] = pt
        if pt < PT_MINIMO:
            fallas.append(f"{r['s']!r}: letra {pt:.2f} pt < {PT_MINIMO}")
        if bb[0] < 0 or bb[2] > W or bb[1] < 0 or bb[3] > alto_total:
            fallas.append(f"{r['s']!r}: fuera del lienzo")
        if r["dentro"] and not contiene(CAJAS[r["dentro"]], bb):
            fallas.append(f"{r['s']!r}: sale de su caja {r['dentro']}")
        for clave, c in CAJAS.items():
            if cruza(bb, c) and not contiene(c, bb):
                fallas.append(f"{r['s']!r}: lo corta el borde de la caja {clave}")
        for nombre, m in MARCAS:
            if cruza(bb, m):
                fallas.append(f"{r['s']!r}: lo toca {nombre}")
    for i in range(len(cajas)):
        for j in range(i + 1, len(cajas)):
            if cruza(cajas[i][1], cajas[j][1]):
                fallas.append(f"{cajas[i][0]['s']!r} se superpone con {cajas[j][0]['s']!r}")
    cajas_texto = [(r["s"], bb) for r, bb in cajas]
    holgura = min(CAJAS[r["dentro"]][2] - bb[2] for r, bb in cajas if r["dentro"])
    return len(REGISTRO), len(MARCAS), len(CAJAS), tamanos, fallas, cajas_texto, holgura


# --------------------------------------------------------------------------- #
# Trazos: ninguno a menos de DISTANCIA_MIN de un trazo de otro tramo           #
# --------------------------------------------------------------------------- #
def distancia_segmentos(a0, a1, b0, b1):
    def orientacion(p, q, r):
        v = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
        return (v > 0) - (v < 0)

    def punto_segmento(p, q0, q1):
        dx, dy = q1[0] - q0[0], q1[1] - q0[1]
        largo2 = dx * dx + dy * dy
        t = 0.0 if largo2 == 0 else max(0.0, min(1.0, ((p[0] - q0[0]) * dx + (p[1] - q0[1]) * dy) / largo2))
        return math.hypot(p[0] - q0[0] - t * dx, p[1] - q0[1] - t * dy)

    o = (orientacion(a0, a1, b0), orientacion(a0, a1, b1), orientacion(b0, b1, a0),
         orientacion(b0, b1, a1))
    if o[0] != o[1] and o[2] != o[3] and 0 not in o:
        return 0.0
    return min(punto_segmento(a0, b0, b1), punto_segmento(a1, b0, b1), punto_segmento(b0, a0, a1),
               punto_segmento(b1, a0, a1))


def controlar_trazos():
    fallas, minimo = [], None
    for i in range(len(TRAZOS)):
        for j in range(i + 1, len(TRAZOS)):
            da, na, a0, a1 = TRAZOS[i]
            db, nb, b0, b1 = TRAZOS[j]
            if da == db:
                continue
            d = distancia_segmentos(a0, a1, b0, b1)
            if minimo is None or d < minimo[0]:
                minimo = (d, na, nb)
            if d < DISTANCIA_MIN:
                fallas.append(f"{na} a {d:.2f} de {nb}")
    return fallas, minimo, len(TRAZOS)


# --------------------------------------------------------------------------- #
# Margen a los bordes (el de generar_figura_formacion_to.py)                   #
# --------------------------------------------------------------------------- #
RX_COORD = re.compile(r"-?\d+(?:\.\d+)?")


def cajas_dibujo(svg):
    """Caja de cada elemento dibujado del SVG (rectángulos, trazos, círculos),
    con medio grosor de trazo y, en los trazos con punta de flecha, el largo de
    la punta (6 veces el grosor). No cuentan el fondo (el rectángulo sin x) ni
    las definiciones."""
    ns = "{http://www.w3.org/2000/svg}"
    out = []
    for el in ET.fromstring(svg):
        tag = el.tag.replace(ns, "")
        grosor = float(el.get("stroke-width", 0)) if el.get("stroke", "none") != "none" else 0.0
        m = grosor / 2
        if tag == "rect" and el.get("x") is not None:
            x, y = float(el.get("x")), float(el.get("y"))
            w, h = float(el.get("width")), float(el.get("height"))
            out.append((f"rectángulo en ({x:.1f}, {y:.1f})", (x - m, y - m, x + w + m, y + h + m)))
        elif tag == "circle":
            cx, cy, r = (float(el.get(k)) for k in ("cx", "cy", "r"))
            out.append((f"círculo en ({cx:.1f}, {cy:.1f})", (cx - r - m, cy - r - m, cx + r + m,
                                                             cy + r + m)))
        elif tag == "path":
            v = [float(n) for n in RX_COORD.findall(el.get("d"))]
            xs, ys = v[0::2], v[1::2]
            c = [min(xs) - m, min(ys) - m, max(xs) + m, max(ys) + m]
            if el.get("marker-end"):
                p = 6 * grosor
                c = [min(c[0], xs[-1] - p), min(c[1], ys[-1] - p), max(c[2], xs[-1] + p),
                     max(c[3], ys[-1] + p)]
            out.append((f"trazo desde ({xs[0]:.1f}, {ys[0]:.1f})", tuple(c)))
    return out


def controlar_margen(svg, cajas_texto, alto_total):
    """Distancia mínima de todo texto y todo elemento dibujado a cada borde;
    falla todo lo que quede a menos de MARGEN_MIN."""
    todas = [(f"texto {s!r}", bb) for s, bb in cajas_texto] + cajas_dibujo(svg)
    distancia = {"izquierdo": lambda bb: bb[0], "superior": lambda bb: bb[1],
                 "derecho": lambda bb: W - bb[2], "inferior": lambda bb: alto_total - bb[3]}
    minimos, fallas = {}, []
    for borde, d in distancia.items():
        minimos[borde] = min(d(bb) for _, bb in todas)
        for nombre, bb in todas:
            if d(bb) < MARGEN_MIN:
                fallas.append(f"{nombre}: a {d(bb):.1f} unidades del borde {borde}")
    return minimos, fallas, len(todas)


# --------------------------------------------------------------------------- #
# Exportación e invariantes                                                    #
# --------------------------------------------------------------------------- #
# cairo escribe /CreationDate en el /Info del PDF; con SOURCE_DATE_EPOCH fijo el
# PDF es byte-reproducible (mismo recurso que generar_figura_pagina_to.py).
SOURCE_DATE_EPOCH = "0"


def exportar(svg):
    rsvg = shutil.which("rsvg-convert")
    if not rsvg:
        raise SystemExit("rsvg-convert no está instalado: no se escriben el PNG ni el PDF")
    datos = svg.encode("utf-8")
    subprocess.run([rsvg, "-w", str(ANCHO_PNG_PX), "-f", "png", "-o", SALIDA_PNG],
                   input=datos, check=True)
    base.grabar_densidad(SALIDA_PNG, DPI)
    entorno = dict(os.environ, SOURCE_DATE_EPOCH=SOURCE_DATE_EPOCH)
    subprocess.run([rsvg, "-f", "pdf", "-o", SALIDA_PDF], input=datos, check=True, env=entorno)


def invariantes_pdf():
    from pypdf import PdfReader
    lector = PdfReader(SALIDA_PDF)
    pagina = lector.pages[0]
    fecha = (lector.metadata or {}).get("/CreationDate")
    contenido = hashlib.sha256(pagina.get_contents().get_data()).hexdigest()
    return contenido, fecha, (float(pagina.mediabox.width), float(pagina.mediabox.height))


def main():
    global MEDIR
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--svg", help="guarda además el SVG intermedio en esta ruta")
    args = ap.parse_args()

    res = resolver()
    print(f"PDF: {REL_PDF}   sha256 {PDF_SHA256[:12]}… (comprobado; igual al del inventario "
          f"{REL_INVENTARIO})")
    print(f"     portada: {res['portada'][0]!r}; {PORTADA[0]} · {PORTADA[1]} (comprobado)")
    print(f"UNIDADES: {REL_CHUNKS}   sha256 {CHUNKS_SHA256[:12]}… (comprobado), "
          f"{res['n_chunks']} unidades")
    print("BLOQUES (artefacto -> página del PDF; líneas del PDF contadas desde 1 en "
          "extract_text_lines; cada pieza está tal cual en la página):")
    for b in BLOQUES:
        blk = res["bloques"][b["clave"]]
        color = "gris" if b["gris"] else "negro"
        print(f"  {b['clave']:8s} {color:5s} de {blk['id']} (registro desde la línea "
              f"{res['anclas'][blk['id']]['inicio']} del artefacto), página {blk['pagina']}:")
        for p in blk["piezas"]:
            print(f"     {p['nombre']:30s} artefacto línea {p['linea_artefacto']}; PDF exacto, "
                  f"líneas {p['lineas_pdf']}")
        if blk["cortes"]:
            print(f"     cortes con guion: {[(k + 1, a, b_) for k, a, b_ in blk['cortes']]}")
    print("TRAMOS (literal y único en el texto normalizado de su bloque; en la página del PDF "
          "normalizada):")
    for t in res["tramos"].values():
        segs = "; ".join(f"línea {k + 1} cols {c0}-{c1}" for k, c0, c1 in t["segmentos"])
        print(f"  {t['rotulo']:32s} bloque {t['bloque']:7s} nivel {t['nivel']}; caracteres "
              f"{t['i']}-{t['j']} del bloque (1 aparición), {t['n_pdf']} en la página; {segs}")
        print(f"     subrayado: {t['dibujado']}")

    MEDIR = base.medidor()
    if MEDIR is None:
        raise SystemExit("sin las métricas reales de Helvetica no se pueden ubicar los subrayados")
    svg, alto_total, guias, puntos_flecha = componer(res)
    comprobar_transcripcion(res)
    print(f"TRANSCRIPCIÓN: lo dibujado reconstruye el texto del artefacto en los {len(BLOQUES)} "
          "bloques; gris = 5.1.1 y 3.7, negro = 5.1.1.1; rótulos fijados, en el color de su "
          "forma; sin textos prohibidos")
    print("GUÍAS Y RÓTULOS (y de la guía al llegar al codo -> y del rótulo):")
    for g in guias:
        print(f"  {g['tramo']['rotulo']:32s} {g['modo']:28s} {g['puntos'][-1][1]:6.1f} -> "
              f"{g['y_rotulo']:6.1f}")
    print("FLECHA: " + " -> ".join(f"({x:.1f}, {y:.1f})" for x, y in puntos_flecha)
          + f"; llega al bloque {res['destino']}")
    n_txt, n_marcas, n_cajas, tamanos, fallas, cajas_texto, holgura = controlar_geometria(alto_total)
    fallas_trazos, minimo, n_seg = controlar_trazos()
    minimos, fallas_margen, n_elem = controlar_margen(svg, cajas_texto, alto_total)
    print(f"GEOMETRÍA (métricas reales de Helvetica): {n_txt} textos, {n_cajas} cajas, {n_marcas} "
          f"marcas; fallas: {len(fallas)}; holgura mínima de una línea a la derecha de su bloque "
          f"{holgura:.1f} unidades")
    for x in fallas:
        print(f"  MAL {x}")
    print(f"TRAZOS ({n_seg} segmentos): distancia mínima entre trazos de tramos distintos "
          f"{minimo[0]:.2f} unidades ({minimo[1]} / {minimo[2]}); exigida {DISTANCIA_MIN}; "
          f"fallas: {len(fallas_trazos)}")
    for x in fallas_trazos:
        print(f"  MAL {x}")
    mm = ANCHO_FIGURA_CM * 10 / W
    print(f"MARGEN ({n_elem} elementos: textos, rectángulos, trazos): mínimo a cada borde "
          + ", ".join(f"{b} {v:.1f} u = {v * mm:.2f} mm" for b, v in minimos.items())
          + f"; exigido {MARGEN_MM:.1f} mm ({MARGEN_MIN:.1f} u); fallas: {len(fallas_margen)}")
    for x in fallas_margen:
        print(f"  MAL {x}")
    if fallas or fallas_trazos or fallas_margen:
        raise SystemExit("FALLA: la geometría de la figura tiene defectos")
    for fs in sorted(tamanos):
        print(f"LETRA {fs} unidades -> {tamanos[fs]:.2f} pt impresos a {ANCHO_FIGURA_CM:.0f} cm")
    print(f"ALTO: lienzo {W} x {alto_total:.1f}, impreso a {ANCHO_FIGURA_CM:.2f} x "
          f"{ANCHO_FIGURA_CM * alto_total / W:.2f} cm")
    if args.svg:
        with open(args.svg, "w", encoding="utf-8") as fh:
            fh.write(svg)
        print(f"SVG: {args.svg}")
    print(f"SVG sha256 {hashlib.sha256(svg.encode('utf-8')).hexdigest()}")
    exportar(svg)
    contenido, fecha, caja = invariantes_pdf()
    print(f"PNG: {os.path.relpath(SALIDA_PNG, RAIZ)}   sha256 {sha256(SALIDA_PNG)}")
    print(f"PDF: {os.path.relpath(SALIDA_PDF, RAIZ)}   sha256 {sha256(SALIDA_PDF)}")
    print(f"     {caja[0]:.1f} x {caja[1]:.1f} pt; /CreationDate {fecha!r} "
          f"(SOURCE_DATE_EPOCH={SOURCE_DATE_EPOCH}); stream de contenido sha256 {contenido}")


if __name__ == "__main__":
    main()
