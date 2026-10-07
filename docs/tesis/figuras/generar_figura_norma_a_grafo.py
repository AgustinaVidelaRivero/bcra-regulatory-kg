#!/usr/bin/env python3
"""Figura «de la norma al grafo» para la Introducción (Figura 1.1), versión 2.

Panel superior, «En el texto», igual que en la versión 1: en gris la frase de
la unidad 5.1.1 que encabeza la lista de excepciones; debajo, con sangría, el
punto 5.1.1.1 con resaltada la frase que remite al punto 3.7; una línea «[…]»;
y el punto 3.7. Los textos se leen de la segmentación de la tanda 0 con el
perfil r2b (salida_tanda0_r2b, commit 9f6361e) y el script comprueba que son,
carácter por carácter, los de la versión 1.

Panel inferior, «En el grafo»: lo que el grafo de la tanda 0 con el perfil r2b
tiene de esos dos puntos: la Operacion de la inclusión en la cartera
comercial, las dos Condicion del 5.1.1.1 con su condicion_de hacia ella y la
Definicion del importe de referencia del 3.7, con las dos remite_a (desde la
Condicion del monto y desde la Operacion) como aristas resaltadas. Cada nodo
lleva su tipo, su punto y su etiqueta tal como está en el grafo; los colores
de tipo (relleno y borde) son los de la figura del esquema final. No se
dibujan, a propósito: la Excepcion del 5.1.1.1 (en el grafo su única arista es
establecida_en), las establecida_en hacia el Texto Ordenado y las otras
remite_a que llegan a la Definicion del 3.7; el script las cuenta y las
informa.

Versión 1 (28/09/2026; generador en fbe69d4): sobre KG-Reextraído-r1 (sha256
0226e947…), con dos Restriccion y su limita, la Obligacion del 3.7 con
referencia, la Operacion y un Sujeto; leía todo de ejemplo_prestamo_datos.json.

Fuentes, con candado de sha256 (el script frena si alguna no es la verificada):
- GRAFO: el grafo de desarrollo r2b, del que se dibuja;
- GRAFO_DIEZ: el grafo de diez documentos r2b, en el que se comprueba que lo
  dibujado está igual (mismos nodos, mismas propiedades, mismas aristas);
- CHUNKS_CLA: chunks_cla.json de salida_tanda0_r2b, de donde salen los textos;
- DATOS_V1: ejemplo_prestamo_datos.json, contra cuyos textos se comparan;
- EXTRACTOR_V1: extraer_datos_ejemplo_prestamo.py, del que se importan, sin
  modificarlos, texto_de_figura, la frase esperada de la unidad 5.1.1 y la
  frase resaltada;
- ESTILO: figura_esquema_final.svg, de donde salen los colores de tipo.

Controles, en cada corrida (el script frena si alguno falla):
- textos: los tres iguales a los de la versión 1 y la frase resaltada dentro
  del 5.1.1.1;
- grafo: cada nodo, con su tipo y su etiqueta, una sola vez y con su punto
  como única procedencia punto_propio; cada arista, una sola vez, y las
  remite_a con destino cla::3.7; entre los nodos dibujados el grafo no tiene
  otras aristas; los nodos de la unidad que no se dibujan son los declarados
  en NO_DIBUJADOS; todo igual en los dos grafos;
- inventario: el SVG se relee y, solo desde su geometría y sus textos, se
  rearman los nodos (tipo, punto, etiqueta) y las aristas (origen, relación,
  destino); tienen que ser exactamente los del grafo;
- geometría (controlar_geometria, que usan también las figuras 1.2 y 1.3):
  medidas con las métricas reales de Helvetica, ningún texto superpuesto con
  otro, ningún texto sobre una caja que no lo contiene, ningún trazo que
  atraviese una caja, ningún texto sobre un trazo que no es el suyo, 0 cruces
  entre trazos y todo dentro del lienzo.
Antes de componer la figura corren cuatro pruebas negativas (una arista de
más, una etiqueta cambiada, un cruce y un rótulo sobre una caja); cada una
tiene que hacer fallar su control. Con --perturbar <caso> se compone la figura
con ese defecto: los controles fallan y no se escribe nada.

Salidas, byte-reproducibles: figura_norma_a_grafo.svg, .png (300 dpi, densidad
grabada) y .pdf (fecha de creación fijada con SOURCE_DATE_EPOCH=0).

Uso (desde la raíz del repo):
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_norma_a_grafo.py
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_norma_a_grafo.py --salida DIR
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_norma_a_grafo.py \\
        --perturbar {arista_de_mas,etiqueta_distinta,cruce,rotulo_sobre_caja}
"""

import sys

sys.dont_write_bytecode = True  # importar los módulos hermanos no deja __pycache__

import argparse  # noqa: E402
import hashlib  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import shutil  # noqa: E402
import struct  # noqa: E402
import subprocess  # noqa: E402
import xml.etree.ElementTree as ET  # noqa: E402
import zlib  # noqa: E402
from collections import Counter  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", ".."))
sys.path.insert(0, AQUI)
NOMBRE = "figura_norma_a_grafo"
NS = "{http://www.w3.org/2000/svg}"


class Freno(Exception):
    pass


def freno(msj):
    raise Freno(msj)


# --------------------------------------------------------------------------- #
# Fuentes y candados                                                           #
# --------------------------------------------------------------------------- #
# KG-Tanda0-Desarrollo-r2b y KG-Tanda0-Diez-r2b: ensamblados de la re-extracción
# de la tanda 0 con el perfil r2b (U-REEXT-T0; último commit de los dos
# archivos, bbc38dc).
GRAFO = ("data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo_r2b/r2/kg.json",
         "6e7560433148cfe0c476cdd61199c32278187c4196d6f90dc0a38976a6d8e9a2")
GRAFO_DIEZ = ("data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2b/r2/kg.json",
              "a9631a64b422bdae634fb05135373c6f04c6272cdf7acd43a1be9f5b6c1f5f57")
# Segmentación E0 e0-r2 de la tanda 0 (salida_tanda0_r2b, commit 9f6361e).
CHUNKS_CLA = ("data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b/chunks_cla.json",
              "98808886a406d8321c678836a55f92eea983d594d95358dd21ceb537487ac0b1")
# Datos de la versión 1 y el script que los escribió (commit fbe69d4).
DATOS_V1 = ("docs/tesis/figuras/ejemplo_prestamo_datos.json",
            "25ab7b4c0d76fd735244fe0fecc17ceaba1b0e8bfd2312e7aa3cbd5c849672a2")
EXTRACTOR_V1 = ("docs/tesis/figuras/extraer_datos_ejemplo_prestamo.py",
                "4c3a441972d27304b6d58d0664dbc15b893bce7ad3e7d2d49afad947f51eeea7")
# Figura del esquema final, versión 3: cajas por tipo (data-caja).
ESTILO = ("docs/tesis/figuras/figura_esquema_final.svg",
          "dfdb16d471bb93c6351aa03b1e609452b75c428baa354c52354ce1dfe9797bb3")


def leer_con_candado(rel, esperado):
    ruta = rel if os.path.isabs(rel) else os.path.join(RAIZ, rel)
    with open(ruta, "rb") as fh:
        crudo = fh.read()
    sha = hashlib.sha256(crudo).hexdigest()
    if sha != esperado:
        freno(f"{rel} no es el verificado: sha256 {sha} ≠ {esperado}")
    return crudo


def sha256(ruta):
    with open(ruta, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


# --------------------------------------------------------------------------- #
# Contenido                                                                    #
# --------------------------------------------------------------------------- #
# Composición del panel superior, igual que en la versión 1: (clave del texto,
# recuadro, sangría en px); None marca la línea «[…]».
SANGRIA_PUNTO = 32
OMISION = "[…]"
COMPOSICION_TEXTO = [
    ("cla::5.1.1", False, 0),                 # frase que encabeza, en gris
    ("cla::5.1.1.1", True, SANGRIA_PUNTO),    # punto de la lista, con sangría
    (None, False, 0),                         # «[…]»
    ("cla::3.7", True, 0),                    # punto de otra sección
]
UNIDADES_TEXTO = ("cla::5.1.1", "cla::5.1.1.1", "cla::3.7")

UNIDAD = "cla::5.1.1.1"
DESTINO_REMISION = "cla::3.7"
# Nodos dibujados: (clave, tipo, chunk de su procedencia punto_propio, etiqueta
# tal como está en el grafo). El script los busca por tipo, etiqueta y
# procedencia, y frena si no hay exactamente uno.
NODOS = (
    ("condicion_monto", "Condicion", "cla::5.1.1.1", "Superar dos veces importe referencia punto 3.7"),
    ("operacion", "Operacion", "cla::5.1.1.1", "Inclusión en cartera comercial — créditos consumo/vivienda"),
    ("condicion_repago", "Condicion", "cla::5.1.1.1", "Repago vinculado a actividad productiva/comercial"),
    ("definicion_3_7", "Definicion", "cla::3.7", "Importe de referencia — nivel máximo de ventas anuales"),
)
# Aristas dibujadas: (origen, relación en el grafo, destino).
ARISTAS = (
    ("condicion_monto", "remite_a", "definicion_3_7"),
    ("condicion_monto", "condicion_de", "operacion"),
    ("condicion_repago", "condicion_de", "operacion"),
    ("operacion", "remite_a", "definicion_3_7"),
)
RELACION_RESALTADA = "remite_a"
# Nodos de la unidad 5.1.1.1 que no se dibujan, a propósito: (tipo, etiqueta).
NO_DIBUJADOS = (("Excepcion", "Excepción cartera comercial — créditos consumo/vivienda"),)

# Disposición del panel del grafo: (clave, columna, fila). Las aristas siguen
# RUTAS: «horizontal» entre nodos de la misma fila, «vertical» entre nodos de la
# misma columna y «codo» desde el costado del origen, en horizontal hasta la
# vertical del destino y de ahí a su borde inferior.
DISPOSICION = [
    ("condicion_monto", "izq", 0),
    ("definicion_3_7", "der", 0),
    ("operacion", "izq", 1),
    ("condicion_repago", "izq", 2),
]
COLUMNAS = {"izq": {"cx": 190, "w": 322}, "der": {"cx": 620, "w": 336}}
RUTAS = {
    ("condicion_monto", "remite_a", "definicion_3_7"): "horizontal",
    ("condicion_monto", "condicion_de", "operacion"): "vertical",
    ("condicion_repago", "condicion_de", "operacion"): "vertical",
    ("operacion", "remite_a", "definicion_3_7"): "codo",
}

MAX_ETIQUETA = 40   # caracteres por línea visible de una etiqueta de nodo

# --------------------------------------------------------------------------- #
# Paleta y tipografía                                                          #
# Colores de tipo: de la figura del esquema final (leer_colores_tipo). El      #
# resto, como en la versión 1.                                                 #
# --------------------------------------------------------------------------- #
TIPOGRAFIA = "Helvetica,Arial,sans-serif"
ACENTO = "#e07b39"        # resaltado: frase del texto y aristas de remisión
ACENTO_TEXTO = "#8a4513"  # el mismo tono, oscurecido para leer sobre el marcador
GRIS_ARISTA = "#8a8a8a"
GRIS_ROTULO = "#6f6f6f"
BORDE_PANEL = "#ccc"
FONDO_PANEL = "#fafafa"
TINTA = "#1f1f1f"
RX_NODO = 7

# --------------------------------------------------------------------------- #
# Geometría: paneles apilados a ancho completo, como en la versión 1. El       #
# lienzo de W unidades se imprime a ANCHO_PAGINA_CM; el SVG lo declara en cm.  #
# --------------------------------------------------------------------------- #
W = 860
MARGEN = 24
ANCHO_PANEL = W - 2 * MARGEN            # 812
PAD_PANEL = 18
ANCHO_PAGINA_CM = 15.0
PT_POR_CM = 72.0 / 2.54                 # 28,3465 pt/cm
DPI = 300
SOURCE_DATE_EPOCH = "0"

FS_TITULO_PANEL = 17
FS_TEXTO = 17
FS_NODO = 15
FS_ROTULO = 13
FS_LEYENDA = 13
INTERLINEA = 24
PT_MIN_TEXTO = 8.0                      # texto de los recuadros, como en la versión 1


def puntos_impresos(px, ancho_cm=ANCHO_PAGINA_CM, w=W):
    """Tamaño en puntos de `px` unidades con el lienzo impreso a `ancho_cm`."""
    return px * (ancho_cm * PT_POR_CM) / w


# --------------------------------------------------------------------------- #
# Métricas de Helvetica (unidades/1000 em) para componer; los controles miden  #
# con las métricas reales (medidor).                                           #
# --------------------------------------------------------------------------- #
_W = {
    " ": 278, "!": 278, '"': 355, "#": 556, "$": 556, "%": 889, "&": 667,
    "'": 191, "(": 333, ")": 333, "*": 389, "+": 584, ",": 278, "-": 333,
    ".": 278, "/": 278, ":": 278, ";": 278, "?": 556, "@": 1015,
    "[": 278, "]": 278, "_": 556, "«": 500, "»": 500, "—": 1000, "–": 556,
    "“": 333, "”": 333, "‘": 222, "’": 222, "…": 1000, "·": 278, "✗": 800,
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

# Helvetica Bold, donde difiere de la redonda.
_WB = {"!": 333, '"': 474, "&": 722, "'": 238, ":": 333, ";": 333, "?": 611, "@": 975,
       "A": 722, "B": 722, "J": 556, "K": 722, "L": 611,
       "b": 611, "c": 556, "d": 611, "f": 333, "g": 611, "h": 611, "i": 278, "j": 278,
       "k": 556, "l": 278, "m": 889, "n": 611, "o": 611, "p": 611, "q": 611, "r": 389,
       "s": 556, "t": 333, "u": 611, "v": 556, "w": 778, "x": 556, "y": 556,
       "í": 278, "ó": 611, "ú": 611, "ñ": 611, "ü": 611}


def ancho(texto, fs, negrita=False):
    """Ancho en unidades de `texto` a tamaño `fs`."""
    if negrita:
        return ancho_negrita(texto, fs)
    return sum(_W.get(c, 556) for c in texto) / 1000.0 * fs


def ancho_negrita(texto, fs):
    return sum(_WB.get(c, _W.get(c, 556)) for c in texto) / 1000.0 * fs


def envolver_estilos(texto, estilo, fs, ancho_max):
    """Envuelve por palabras midiendo en negrita los caracteres con estilo.
    Devuelve lista de (linea, indice_inicio)."""
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
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def f(v):
    """Formato fijo: el SVG no depende de la representación del float."""
    return f"{v:.1f}"


# --------------------------------------------------------------------------- #
# Carga de textos                                                              #
# --------------------------------------------------------------------------- #
def importar_extractor():
    """El extractor de la versión 1, con su candado (se importa sin correrlo)."""
    leer_con_candado(*EXTRACTOR_V1)
    import extraer_datos_ejemplo_prestamo as ext
    if os.path.abspath(ext.__file__) != os.path.join(RAIZ, EXTRACTOR_V1[0]):
        freno(f"se importó otro extractor: {ext.__file__}")
    return ext


def cargar_textos():
    """Textos de la figura desde la segmentación de la tanda 0, compuestos como
    en la versión 1 (extraer_datos_ejemplo_prestamo.extraer_textos), y su
    comparación con los de la versión 1."""
    ext = importar_extractor()
    chunks = {c["id"]: c for c in json.loads(leer_con_candado(*CHUNKS_CLA).decode("utf-8"))}
    textos = {}
    for cid in ext.PUNTOS_TEXTO:
        c = chunks[cid]
        texto, reunidas = ext.texto_de_figura(c["texto"])
        textos[cid] = {"unidad": c["unidad"], "texto": texto, "reunidas": reunidas,
                       "paginas": c["paginas"], "sha256_propio": c["sha256_propio"]}
    intro = chunks[ext.INTRO_5_1_1]
    enc = [h for h in intro["herencia"] if h["tipo"] == "encabezado" and h["unidad_origen"] == "5.1.1"]
    if len(enc) != 1:
        freno(f"{ext.INTRO_5_1_1}: se esperaba un encabezado de la unidad 5.1.1")
    frase, reunidas = ext.texto_de_figura(enc[0]["texto"] + "\n" + intro["texto"])
    if frase != ext.FRASE_5_1_1:
        freno(f"la frase de 5.1.1 no es la esperada: {frase!r}")
    piezas = [h["texto"] for h in chunks["cla::5.1.1.1"]["herencia"] if h["unidad_origen"] == "5.1.1"]
    if piezas != [enc[0]["texto"], intro["texto"]]:
        freno("la herencia de cla::5.1.1.1 no lleva la frase de la unidad 5.1.1")
    textos["cla::5.1.1"] = {"unidad": "5.1.1", "texto": frase, "reunidas": reunidas,
                            "fragmento_origen": ext.INTRO_5_1_1}
    resaltada = ext.FRASE_RESALTADA
    if resaltada not in textos["cla::5.1.1.1"]["texto"]:
        freno("la frase resaltada no está en el texto de cla::5.1.1.1")
    v1 = json.loads(leer_con_candado(*DATOS_V1).decode("utf-8"))
    for cid in UNIDADES_TEXTO:
        if (textos[cid]["unidad"], textos[cid]["texto"]) != (v1["textos"][cid]["unidad"],
                                                               v1["textos"][cid]["texto"]):
            freno(f"el texto de {cid} no es el de la versión 1")
    if resaltada != v1["textos"]["frase_resaltada"]:
        freno("la frase resaltada no es la de la versión 1")
    return {"textos": textos, "frase_resaltada": resaltada, "pregunta": v1["pregunta"], "v1": v1,
            "chunks": chunks}


# --------------------------------------------------------------------------- #
# Carga del subgrafo                                                           #
# --------------------------------------------------------------------------- #
def provenances(elem):
    ps = ([elem["provenance"]] if elem.get("provenance") else []) + (elem.get("provenances") or [])
    vistos, salida = set(), []
    for p in ps:
        clave = (p.get("chunk_id"), p.get("punto"), p.get("rol_documental"))
        if clave not in vistos:
            vistos.add(clave)
            salida.append(p)
    return salida


def chunks_de(elem):
    return [p.get("chunk_id") for p in provenances(elem)]


def cargar_subgrafo(par, nodos_decl=NODOS, aristas_decl=ARISTAS, no_dibujados=NO_DIBUJADOS,
                    unidad=UNIDAD):
    """Nodos y aristas declarados, buscados en el grafo (leído con su candado),
    y lo que el grafo tiene alrededor que no se dibuja."""
    kg = json.loads(leer_con_candado(*par).decode("utf-8"))
    por_id = {}
    for n in kg["nodes"]:
        if n["id"] in por_id:
            freno(f"{par[0]}: dos nodos {n['id']}")
        por_id[n["id"]] = n
    nodos = {}
    for clave, tipo, chunk, etiqueta in nodos_decl:
        c = [n for n in kg["nodes"] if n["type"] == tipo and n.get("label") == etiqueta
             and chunk in chunks_de(n)]
        if len(c) != 1:
            freno(f"{par[0]}: {len(c)} nodos {tipo} {etiqueta!r} de {chunk}, no uno")
        n = c[0]
        pp = [p for p in provenances(n) if p.get("rol_documental") == "punto_propio"]
        if [p.get("chunk_id") for p in pp] != [chunk]:
            freno(f"{par[0]}: el nodo {clave} no tiene a {chunk} como única procedencia punto_propio")
        nodos[clave] = {"id": n["id"], "type": tipo, "label": etiqueta, "punto": pp[0]["punto"],
                        "chunk": chunk, "properties": n.get("properties") or {}}
    ids = {v["id"]: k for k, v in nodos.items()}
    if len(ids) != len(nodos):
        freno("dos claves con el mismo nodo")
    aristas = []
    for o, rel, d in aristas_decl:
        hits = [(i, e) for i, e in enumerate(kg["edges"])
                if (e["source"], e["relation"], e["target"]) == (nodos[o]["id"], rel, nodos[d]["id"])]
        if len(hits) != 1:
            freno(f"{par[0]}: arista {o} {rel} {d}: {len(hits)} en el grafo, no una")
        i, e = hits[0]
        if rel == "remite_a" and (e.get("properties") or {}).get("destino") != DESTINO_REMISION:
            freno(f"la remite_a {o} → {d} no tiene destino {DESTINO_REMISION}")
        aristas.append({"origen": o, "relation": rel, "destino": d, "indice": i,
                        "properties": e.get("properties") or {}, "chunks": chunks_de(e)})
    entre = sorted((ids[e["source"]], e["relation"], ids[e["target"]]) for e in kg["edges"]
                   if e["source"] in ids and e["target"] in ids)
    if entre != sorted(aristas_decl):
        freno(f"{par[0]}: entre los nodos dibujados el grafo tiene {entre}, no {sorted(aristas_decl)}")
    # Lo que no se dibuja: las otras aristas de los nodos dibujados, por relación
    # y sentido, y los nodos de la unidad que no se dibujan, con sus aristas.
    afuera = Counter()
    for e in kg["edges"]:
        s, t = e["source"] in ids, e["target"] in ids
        if s != t:
            k = ids[e["source"]] if s else ids[e["target"]]
            otro = por_id[e["target"] if s else e["source"]]
            afuera[(k, "sale" if s else "entra", e["relation"], otro["type"])] += 1
    de_la_unidad = [n for n in kg["nodes"] if unidad in chunks_de(n) and n["type"] != "TextoOrdenado"]
    no_dib = sorted((n["type"], n["label"]) for n in de_la_unidad if n["id"] not in ids)
    if no_dib != sorted(no_dibujados):
        freno(f"{par[0]}: los nodos de {unidad} que no se dibujan son {no_dib}, no {sorted(no_dibujados)}")
    no_dib_aristas = {}
    for n in de_la_unidad:
        if n["id"] not in ids:
            no_dib_aristas[(n["type"], n["label"])] = sorted(
                ("sale" if e["source"] == n["id"] else "entra", e["relation"],
                 por_id[e["target"] if e["source"] == n["id"] else e["source"]]["type"])
                for e in kg["edges"] if n["id"] in (e["source"], e["target"]))
    return {"ruta": par[0], "sha256": par[1], "n_nodos": len(kg["nodes"]), "n_aristas": len(kg["edges"]),
            "nodos": nodos, "aristas": aristas, "afuera": afuera, "no_dibujados": no_dib_aristas}


def comparar_grafos(a, b):
    """Lo dibujado tiene que estar igual en los dos grafos."""
    clave_n = {k: (v["id"], v["type"], v["label"], v["punto"], json.dumps(v["properties"], sort_keys=True))
               for k, v in a["nodos"].items()}
    clave_m = {k: (v["id"], v["type"], v["label"], v["punto"], json.dumps(v["properties"], sort_keys=True))
               for k, v in b["nodos"].items()}
    if clave_n != clave_m:
        freno("los nodos dibujados no son iguales en los dos grafos")
    ea = [(e["origen"], e["relation"], e["destino"], json.dumps(e["properties"], sort_keys=True))
          for e in a["aristas"]]
    eb = [(e["origen"], e["relation"], e["destino"], json.dumps(e["properties"], sort_keys=True))
          for e in b["aristas"]]
    if ea != eb:
        freno("las aristas dibujadas no son iguales en los dos grafos")
    if a["no_dibujados"] != b["no_dibujados"]:
        freno("los nodos no dibujados de la unidad no tienen las mismas aristas en los dos grafos")


def leer_colores_tipo():
    """Relleno, borde y grosor de cada tipo en la figura del esquema final."""
    raiz = ET.fromstring(leer_con_candado(*ESTILO).decode("utf-8"))
    cajas = {}
    for el in raiz.iter(NS + "rect"):
        t = el.get("data-caja")
        if t:
            if t in cajas:
                freno(f"la figura del esquema final tiene dos cajas {t}")
            cajas[t] = {"relleno": el.get("fill"), "borde": el.get("stroke"),
                        "grosor": el.get("stroke-width")}
    return cajas


# --------------------------------------------------------------------------- #
# Nodos                                                                        #
# --------------------------------------------------------------------------- #
def encabezado_nodo(nodo):
    """Primera línea del nodo, en negrita: tipo y punto."""
    return f"{nodo['type']} · punto {nodo['punto']}"


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


def lineas_nodo(nodo, ancho_max, fs, etiqueta=None):
    """Encabezado en negrita y debajo la etiqueta del grafo completa, sin
    abreviar, envuelta al ancho de la caja."""
    etiqueta = nodo["label"] if etiqueta is None else etiqueta
    lineas = [(encabezado_nodo(nodo), True)]
    lineas += [(linea, False) for linea in envolver_etiqueta(etiqueta, fs, ancho_max)]
    for linea, negrita in lineas:
        if ancho(linea, fs, negrita) > ancho_max or (not negrita and len(linea) > MAX_ETIQUETA):
            freno(f"la línea {linea!r} no entra en la caja")
    if " ".join(s for s, negrita in lineas if not negrita) != etiqueta:
        freno(f"la etiqueta dibujada no es {etiqueta!r}")
    return lineas


def caja_nodo(partes, nodo, colores, cx, cy, w, h, lineas, fs, paso, clave):
    """Caja del nodo con los colores de su tipo, encabezado y etiqueta
    centrados."""
    c = colores[nodo["type"]]
    partes.append(f'<rect x="{f(cx - w / 2)}" y="{f(cy - h / 2)}" width="{f(w)}" height="{f(h)}" '
                  f'fill="{c["relleno"]}" stroke="{c["borde"]}" stroke-width="{c["grosor"]}" '
                  f'rx="{RX_NODO}" data-caja="{clave}"/>')
    ytxt = cy - (len(lineas) - 1) * paso / 2.0 + fs / 3.0
    for linea, negrita in lineas:
        partes.append(f'<text x="{f(cx)}" y="{f(ytxt)}" text-anchor="middle" font-size="{fs}" '
                      f'font-weight="{"bold" if negrita else "normal"}" fill="{TINTA}">{esc(linea)}</text>')
        ytxt += paso


# --------------------------------------------------------------------------- #
# Panel de texto (sin cambios respecto de la versión 1)                        #
# --------------------------------------------------------------------------- #
PAD_CAJA, GAP_CAJAS, GAP_ENCABEZA = 14, 15, 10


def numero_inicial(texto, unidad):
    """Largo del número de punto con que empieza el texto («5.1.1.1.»)."""
    if not unidad:
        return 0
    prefijo = unidad + "."
    return len(prefijo) if texto.startswith(prefijo) else 0


def bloques_texto(cont):
    t, frase = cont["textos"], cont["frase_resaltada"]
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
        freno("la frase resaltada debe estar en exactamente un punto")
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


def ancho_texto_bloque(b, ancho_panel):
    ancho_caja = ancho_panel - 2 * PAD_PANEL - b["sangria"]
    return ancho_caja - 2 * PAD_CAJA if b["caja"] else ancho_caja


def lineas_bloque(b, ancho_panel):
    return envolver_estilos(b["texto"], estilo_de(b), FS_TEXTO, ancho_texto_bloque(b, ancho_panel))


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


def segmentos_estilo(linea, desplazamiento, estilo):
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
    return segmentos


def texto_estilado(partes, estilo, lineas, x, y, fs, interlinea, tinta, tinta_resaltado):
    """Líneas con el número de punto en negrita y el tramo resaltado sobre
    fondo de acento. `y` es la primera línea base."""
    for linea, desplazamiento in lineas:
        segmentos = segmentos_estilo(linea, desplazamiento, estilo)
        xc = x
        for seg, m in segmentos:
            aseg = ancho_negrita(seg, fs) if m else ancho(seg, fs)
            if m == "R" and seg.strip():
                partes.append(f'<rect x="{f(xc - 1)}" y="{f(y - fs + 2)}" width="{f(aseg + 2)}" '
                              f'height="{f(fs + 5)}" fill="{ACENTO}" opacity="0.26" rx="2"/>')
            xc += aseg
        tspans = ""
        for seg, m in segmentos:
            if m == "R":
                tspans += f'<tspan font-weight="bold" fill="{tinta_resaltado}">{esc(seg)}</tspan>'
            elif m == "N":
                tspans += f'<tspan font-weight="bold">{esc(seg)}</tspan>'
            else:
                tspans += f'<tspan>{esc(seg)}</tspan>'
        partes.append(f'<text x="{f(x)}" y="{f(y)}" font-size="{fs}" fill="{tinta}" '
                      f'xml:space="preserve">{tspans}</text>')
        y += interlinea


def dibujar_panel_texto(bloques, x0, y0, ancho_panel, alto_panel):
    partes = [f'<text x="{f(x0)}" y="{f(y0 - 12)}" font-size="{FS_TITULO_PANEL}" '
              f'font-weight="bold">En el texto</text>',
              f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(ancho_panel)}" height="{f(alto_panel)}" '
              f'fill="{FONDO_PANEL}" stroke="{BORDE_PANEL}" rx="5"/>']
    y = y0 + PAD_PANEL
    for b in bloques:
        alto = alto_bloque(b, ancho_panel)
        xb = x0 + PAD_PANEL + b["sangria"]
        if b["caja"]:
            ancho_caja = ancho_panel - 2 * PAD_PANEL - b["sangria"]
            acento = b["resaltar"] is not None
            partes.append(f'<rect x="{f(xb)}" y="{f(y)}" width="{f(ancho_caja)}" height="{f(alto)}" '
                          f'fill="white" stroke="{ACENTO if acento else "#d8d8d8"}" '
                          f'stroke-width="{"1.8" if acento else "1.0"}" rx="4"/>')
            xl, yl, tinta = xb + PAD_CAJA, y + PAD_CAJA + FS_TEXTO, TINTA
        else:
            xl, yl, tinta = xb, y + FS_TEXTO, GRIS_ROTULO
        texto_estilado(partes, estilo_de(b), lineas_bloque(b, ancho_panel), xl, yl, FS_TEXTO,
                       INTERLINEA, tinta, ACENTO_TEXTO)
        y += alto + separacion_tras(b)
    return partes


# --------------------------------------------------------------------------- #
# Panel del grafo                                                              #
# --------------------------------------------------------------------------- #
PAD_GRAFO = 30      # del borde del panel a la primera y a la última fila
GAP_FILAS = 58      # entre filas: alcanza para la arista vertical y su rótulo
PASO_NODO = 18      # interlínea dentro de los nodos


def cajas_grafo(nodos, y0, etiquetas=None):
    """Posición y tamaño de cada nodo, y alto del panel."""
    etiquetas = etiquetas or {}
    lineas = {c: lineas_nodo(nodos[c], COLUMNAS[col]["w"] - 22, FS_NODO, etiquetas.get(c))
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
                            "lineas": lineas[c]}
        y += alto_fila[fi] + GAP_FILAS
    return cajas, y - GAP_FILAS + PAD_GRAFO - y0


def ruta_arista(ca, cb, forma):
    """Puntos del trazo y lugar del rótulo: (puntos, (x, y) del rótulo, con fondo)."""
    if forma == "horizontal":
        if ca["fila"] != cb["fila"]:
            freno("arista horizontal entre filas distintas")
        lado = 1 if cb["cx"] > ca["cx"] else -1
        p1 = (ca["cx"] + lado * ca["w"] / 2.0, ca["cy"])
        p2 = (cb["cx"] - lado * cb["w"] / 2.0, cb["cy"])
        return [p1, p2], ((p1[0] + p2[0]) / 2.0, p1[1] - 11)
    if forma == "vertical":
        if ca["col"] != cb["col"]:
            freno("arista vertical entre columnas distintas")
        lado = 1 if cb["cy"] > ca["cy"] else -1
        p1 = (ca["cx"], ca["cy"] + lado * ca["h"] / 2.0)
        p2 = (cb["cx"], cb["cy"] - lado * cb["h"] / 2.0)
        return [p1, p2], ((p1[0] + p2[0]) / 2.0, (p1[1] + p2[1]) / 2.0)
    if forma == "codo":
        if not cb["cy"] < ca["cy"] or not cb["cx"] > ca["cx"]:
            freno("el codo está previsto hacia arriba y a la derecha")
        p1 = (ca["cx"] + ca["w"] / 2.0, ca["cy"])
        p2 = (cb["cx"], ca["cy"])
        p3 = (cb["cx"], cb["cy"] + cb["h"] / 2.0)
        return [p1, p2, p3], ((p1[0] + p2[0]) / 2.0, p1[1] - 11)
    freno(f"forma de arista desconocida: {forma}")


def dibujar_arista(partes, k, pts, rotulo, relacion, resaltada, fs=FS_ROTULO):
    color = ACENTO if resaltada else GRIS_ARISTA
    grosor = "2.6" if resaltada else "1.5"
    marker = "arA" if resaltada else "arG"
    dash = "" if resaltada else ' stroke-dasharray="4,4"'
    d = "M" + " L".join(f"{f(x)},{f(y)}" for x, y in pts)
    partes.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{grosor}"{dash} '
                  f'stroke-linejoin="round" marker-end="url(#{marker})" opacity="0.95" data-arista="{k}"/>')
    mx, my = rotulo
    at = ancho(relacion, fs, resaltada)
    partes.append(f'<rect x="{f(mx - at / 2 - 4)}" y="{f(my - fs + 1)}" width="{f(at + 8)}" '
                  f'height="{f(fs + 6)}" fill="{FONDO_PANEL}" opacity="0.94" rx="2"/>')
    partes.append(f'<text x="{f(mx)}" y="{f(my + 4)}" text-anchor="middle" font-size="{fs}" '
                  f'font-weight="{"bold" if resaltada else "normal"}" '
                  f'fill="{ACENTO_TEXTO if resaltada else GRIS_ROTULO}" data-rotulo="{k}">{esc(relacion)}</text>')


def dibujar_panel_grafo(sub, colores, cajas, x0, y0, ancho_panel, alto_panel, aristas):
    partes = [f'<text x="{f(x0)}" y="{f(y0 - 12)}" font-size="{FS_TITULO_PANEL}" '
              f'font-weight="bold">En el grafo</text>',
              f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(ancho_panel)}" height="{f(alto_panel)}" '
              f'fill="{FONDO_PANEL}" stroke="{BORDE_PANEL}" rx="5"/>']
    for k, (o, rel, d, forma) in enumerate(aristas):
        pts, rot = ruta_arista(cajas[o], cajas[d], forma)
        dibujar_arista(partes, k, pts, rot, rel, rel == RELACION_RESALTADA)
    for clave, _, _ in DISPOSICION:
        c = cajas[clave]
        caja_nodo(partes, sub["nodos"][clave], colores, c["cx"], c["cy"], c["w"], c["h"], c["lineas"],
                  FS_NODO, PASO_NODO, clave)
    return partes


def dibujar_leyenda(y0, alto, x0=MARGEN, ancho_total=ANCHO_PANEL, fs=FS_LEYENDA):
    """Leyenda de las dos clases de arista (los tipos van escritos en cada
    nodo)."""
    partes = [f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(ancho_total)}" height="{f(alto)}" '
              f'fill="white" stroke="#e2e2e2" rx="5"/>']
    x_rot = x0 + 22
    y2 = y0 + alto / 2.0 + fs / 3.0
    partes.append(f'<text x="{f(x_rot)}" y="{f(y2)}" font-size="{fs}" font-weight="bold">Tipo de arista</text>')
    xa = x_rot + ancho("Tipo de arista", fs, True) + 26
    partes.append(f'<path d="M{f(xa)},{f(y2 - 4)} L{f(xa + 44)},{f(y2 - 4)}" fill="none" '
                  f'stroke="{ACENTO}" stroke-width="2.6" marker-end="url(#arA)"/>')
    partes.append(f'<text x="{f(xa + 58)}" y="{f(y2)}" font-size="{fs}" font-weight="bold" '
                  f'fill="{ACENTO_TEXTO}">remisión de un punto a otro</text>')
    x3 = xa + 58 + ancho("remisión de un punto a otro", fs, True) + 40
    partes.append(f'<path d="M{f(x3)},{f(y2 - 4)} L{f(x3 + 44)},{f(y2 - 4)}" fill="none" '
                  f'stroke="{GRIS_ARISTA}" stroke-width="1.5" stroke-dasharray="4,4" marker-end="url(#arG)"/>')
    partes.append(f'<text x="{f(x3 + 58)}" y="{f(y2)}" font-size="{fs}" fill="{GRIS_ROTULO}">'
                  f'resto de las relaciones</text>')
    return partes


def marcadores(extra=()):
    s = ""
    for mid, color in (("arG", GRIS_ARISTA), ("arA", ACENTO)) + tuple(extra):
        s += (f'<marker id="{mid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
              f'markerHeight="6" orient="auto-start-reverse"><path d="M0,0L10,5L0,10z" '
              f'fill="{color}"/></marker>')
    return f"<defs>{s}</defs>"


def cabecera_svg(w, alto_total, ancho_cm):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{ancho_cm:g}cm" '
            f'height="{ancho_cm * alto_total / w:.3f}cm" viewBox="0 0 {w} {f(alto_total)}" '
            f'font-family="{TIPOGRAFIA}">')


# --------------------------------------------------------------------------- #
# Controles de geometría (los usan también las figuras 1.2 y 1.3)              #
# --------------------------------------------------------------------------- #
FUENTE_SISTEMA = "/System/Library/Fonts/Helvetica.ttc"


def medidor():
    """Función ancho(s, fs, negrita) con las métricas reales de Helvetica."""
    try:
        from PIL import ImageFont
    except ImportError:
        freno("sin PIL no se miden los textos con las métricas reales de Helvetica")
    if not os.path.exists(FUENTE_SISTEMA):
        freno(f"falta la fuente {FUENTE_SISTEMA}")
    cache = {}

    def medir(s, fs, negrita):
        clave = (fs, negrita)
        if clave not in cache:
            cache[clave] = ImageFont.truetype(FUENTE_SISTEMA, int(round(fs * 10)), index=1 if negrita else 0)
        return cache[clave].getlength(s) / 10.0
    return medir


def puntos_de(d):
    """Polilínea de un atributo d con M, L y Q (las curvas, en diez tramos)."""
    import re
    toks = re.findall(r"[MLQ]|-?\d+(?:\.\d+)?", d)
    pts, cmd, i, actual = [], None, 0, None
    while i < len(toks):
        if toks[i] in "MLQ":
            cmd = toks[i]
            i += 1
            continue
        if cmd in ("M", "L"):
            actual = (float(toks[i]), float(toks[i + 1]))
            pts.append(actual)
            i += 2
        elif cmd == "Q":
            c = (float(toks[i]), float(toks[i + 1]))
            fin = (float(toks[i + 2]), float(toks[i + 3]))
            for k in range(1, 11):
                t = k / 10.0
                pts.append(((1 - t) ** 2 * actual[0] + 2 * (1 - t) * t * c[0] + t * t * fin[0],
                            (1 - t) ** 2 * actual[1] + 2 * (1 - t) * t * c[1] + t * t * fin[1]))
            actual = fin
            i += 4
    return pts


def textos_svg(raiz, medir):
    """Cada <text> con su cadena, tamaño, negrita, caja de tinta y marcas."""
    out = []
    for t in raiz.iter(NS + "text"):
        fs = float(t.get("font-size"))
        base_bold = t.get("font-weight") == "bold"
        piezas = []
        if t.text:
            piezas.append((t.text, base_bold))
        for ts in t.findall(NS + "tspan"):
            piezas.append((ts.text or "", ts.get("font-weight", "bold" if base_bold else "normal") == "bold"))
            if ts.tail:
                piezas.append((ts.tail, base_bold))
        s = "".join(p for p, _ in piezas)
        if not s.strip():
            continue
        a = sum(medir(p, fs, b) for p, b in piezas)
        x, y = float(t.get("x")), float(t.get("y"))
        anc = t.get("text-anchor", "start")
        x0 = {"start": x, "middle": x - a / 2.0, "end": x - a}[anc]
        out.append({"s": s, "fs": fs, "x": x, "y": y, "bb": (x0, y - fs * 0.78, x0 + a, y + fs * 0.22),
                    "rotulo": t.get("data-rotulo"), "negrita": base_bold})
    return out


def se_solapan(a, b):
    return a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]


def contiene(caja, bb):
    return caja[0] <= bb[0] and bb[2] <= caja[2] and caja[1] <= bb[1] and bb[3] <= caja[3]


def tramo_toca_rect(p, q, r, margen=0.0):
    """¿El tramo p-q toca el rectángulo r (achicado `margen` por lado)? Recorte
    de Liang-Barsky."""
    x0, y0, x1, y1 = r[0] + margen, r[1] + margen, r[2] - margen, r[3] - margen
    if x0 >= x1 or y0 >= y1:
        return False
    dx, dy = q[0] - p[0], q[1] - p[1]
    t0, t1 = 0.0, 1.0
    for pp, qq in ((-dx, p[0] - x0), (dx, x1 - p[0]), (-dy, p[1] - y0), (dy, y1 - p[1])):
        if pp == 0:
            if qq < 0:
                return False
        else:
            t = qq / pp
            if pp < 0:
                t0 = max(t0, t)
            else:
                t1 = min(t1, t)
            if t0 > t1:
                return False
    return True


def tramo_atraviesa_rect(p, q, r, margen=2.0):
    """¿El tramo entra al interior del rectángulo (más de `margen` adentro)?"""
    return tramo_toca_rect(p, q, r, margen)


def _orient(a, b, c):
    v = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    return 0 if abs(v) < 1e-9 else (1 if v > 0 else -1)


def _sobre(a, b, c):
    return (min(a[0], b[0]) - 1e-9 <= c[0] <= max(a[0], b[0]) + 1e-9 and
            min(a[1], b[1]) - 1e-9 <= c[1] <= max(a[1], b[1]) + 1e-9)


def tramos_se_tocan(p1, p2, q1, q2):
    o1, o2, o3, o4 = _orient(p1, p2, q1), _orient(p1, p2, q2), _orient(q1, q2, p1), _orient(q1, q2, p2)
    if o1 != o2 and o3 != o4:
        return True
    return ((o1 == 0 and _sobre(p1, p2, q1)) or (o2 == 0 and _sobre(p1, p2, q2)) or
            (o3 == 0 and _sobre(q1, q2, p1)) or (o4 == 0 and _sobre(q1, q2, p2)))


def controlar_geometria(svg, ancho_cm, w, pt_minimo=None, cruces_declarados=0):
    """Controles de geometría sobre el SVG. Cajas: los <rect> con data-caja;
    trazos: los <path> con marker-end (data-arista identifica su rótulo).
    Devuelve (fallas, informe)."""
    medir = medidor()
    raiz = ET.fromstring(svg)
    vb = [float(v) for v in raiz.get("viewBox").split()]
    alto = vb[3]
    ts = textos_svg(raiz, medir)
    cajas = []
    for r in raiz.iter(NS + "rect"):
        if r.get("data-caja"):
            x, y, ww, hh = (float(r.get(k)) for k in ("x", "y", "width", "height"))
            cajas.append((r.get("data-caja"), (x, y, x + ww, y + hh)))
    trazos = [(p.get("data-arista"), puntos_de(p.get("d"))) for p in raiz.iter(NS + "path")
              if p.get("marker-end")]
    fallas = []
    for a in range(len(ts)):
        for b in range(a + 1, len(ts)):
            if se_solapan(ts[a]["bb"], ts[b]["bb"]):
                fallas.append(f"textos superpuestos: {ts[a]['s']!r} / {ts[b]['s']!r}")
    for t in ts:
        bb = t["bb"]
        if bb[0] < 0 or bb[1] < 0 or bb[2] > w or bb[3] > alto:
            fallas.append(f"texto fuera del lienzo: {t['s']!r}")
        for nombre, c in cajas:
            if se_solapan(bb, c) and not contiene(c, bb):
                fallas.append(f"texto sobre la caja {nombre}: {t['s']!r}")
        for ident, pts in trazos:
            if t["rotulo"] is not None and t["rotulo"] == ident:
                continue
            if any(tramo_toca_rect(p, q, bb) for p, q in zip(pts, pts[1:])):
                fallas.append(f"texto sobre un trazo que no es el suyo ({ident}): {t['s']!r}")
    for ident, pts in trazos:
        for p, q in zip(pts, pts[1:]):
            for nombre, c in cajas:
                if tramo_atraviesa_rect(p, q, c):
                    fallas.append(f"el trazo {ident} atraviesa la caja {nombre}")
    cruces = []
    for i in range(len(trazos)):
        for j in range(i + 1, len(trazos)):
            (ia, pa), (ib, pb) = trazos[i], trazos[j]
            if any(tramos_se_tocan(p1, p2, q1, q2) for p1, p2 in zip(pa, pa[1:]) for q1, q2 in zip(pb, pb[1:])):
                cruces.append((ia, ib))
    if len(cruces) != cruces_declarados:
        fallas.append(f"{len(cruces)} cruce(s) entre trazos, declarados {cruces_declarados}: {cruces}")
    tamanos = sorted({t["fs"] for t in ts})
    pts = {fs: puntos_impresos(fs, ancho_cm, w) for fs in tamanos}
    if pt_minimo is not None:
        for fs, pt in pts.items():
            if pt < pt_minimo - 1e-9:
                fallas.append(f"letra de {fs:g} unidades: {pt:.2f} pt impresos, mínimo {pt_minimo}")
    return fallas, {"textos": len(ts), "cajas": len(cajas), "trazos": len(trazos), "cruces": cruces,
                    "tamanos": pts}


# --------------------------------------------------------------------------- #
# Inventario: nodos y aristas releídos del SVG                                  #
# --------------------------------------------------------------------------- #
def inventario_svg(svg):
    """Cajas de nodo (rect rx=7 con data-caja) con el texto que contienen
    (encabezado «Tipo · punto N» y etiqueta) y aristas (trazos con data-arista)
    con su caja de origen, su caja de destino (por el punto en su borde) y su
    rótulo."""
    raiz = ET.fromstring(svg)
    hijos = list(raiz.iter())
    cajas = {}
    for r in raiz.iter(NS + "rect"):
        if r.get("data-caja") and r.get("rx") == str(RX_NODO):
            x, y, ww, hh = (float(r.get(k)) for k in ("x", "y", "width", "height"))
            cajas[r.get("data-caja")] = (x, y, x + ww, y + hh)
    textos = [t for t in hijos if t.tag == NS + "text"]
    nodos = {}
    for k, R in cajas.items():
        dentro = sorted((t for t in textos if R[0] < float(t.get("x")) < R[2] and R[1] < float(t.get("y")) < R[3]),
                        key=lambda t: float(t.get("y")))
        if not dentro or dentro[0].get("font-weight") != "bold":
            nodos[k] = None
            continue
        cab = dentro[0].text or ""
        if " · punto " not in cab:
            nodos[k] = None
            continue
        tipo, punto = cab.split(" · punto ", 1)
        nodos[k] = (tipo, punto, " ".join(t.text or "" for t in dentro[1:]))
    rotulos = {t.get("data-rotulo"): t.text for t in textos if t.get("data-rotulo") is not None}

    def caja_de(p):
        en = [k for k, R in cajas.items()
              if (abs(p[0] - R[0]) < 1.01 or abs(p[0] - R[2]) < 1.01) and R[1] - 1 <= p[1] <= R[3] + 1
              or (abs(p[1] - R[1]) < 1.01 or abs(p[1] - R[3]) < 1.01) and R[0] - 1 <= p[0] <= R[2] + 1]
        return en[0] if len(en) == 1 else None
    aristas = []
    for p in raiz.iter(NS + "path"):
        ident = p.get("data-arista")
        if ident is None:
            continue
        pts = puntos_de(p.get("d"))
        o, d = caja_de(pts[0]), caja_de(pts[-1])
        aristas.append((nodos.get(o) if o else None, rotulos.get(ident), nodos.get(d) if d else None))
    return [v for v in nodos.values()], aristas


def controlar_inventario(svg, nodos_dib, aristas_dib):
    """Lo releído del SVG contra lo que el grafo tiene."""
    nodos, aristas = inventario_svg(svg)
    par = {k: (n["type"], n["punto"], n["label"]) for k, n in nodos_dib.items()}
    esperadas = [(par[o], rel, par[d]) for o, rel, d in aristas_dib]
    fallas = []
    for nombre, esp, dib in (("nodo", list(par.values()), nodos), ("arista", esperadas, aristas)):
        for x in sorted((Counter(esp) - Counter(dib)).elements(), key=str):
            fallas.append(f"{nombre} del grafo que no está en la figura: {x}")
        for x in sorted((Counter(dib) - Counter(esp)).elements(), key=str):
            fallas.append(f"{nombre} de la figura que no está en el grafo: {x}")
    return fallas, nodos, aristas


# --------------------------------------------------------------------------- #
# Exportación                                                                  #
# --------------------------------------------------------------------------- #
def grabar_densidad(ruta, dpi):
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


def png_dimensiones(ruta):
    with open(ruta, "rb") as fh:
        cab = fh.read(24)
    return struct.unpack(">II", cab[16:24])


def exportar(svg, salida, nombre, ancho_cm):
    """Escribe el SVG y exporta el PNG (ancho físico a DPI, densidad grabada) y
    el PDF (SOURCE_DATE_EPOCH fijo) con rsvg-convert. Devuelve las rutas."""
    rsvg = shutil.which("rsvg-convert")
    if not rsvg:
        freno("rsvg-convert no está instalado: no se escriben el PNG ni el PDF")
    os.makedirs(salida, exist_ok=True)
    rutas = {e: os.path.join(salida, f"{nombre}.{e}") for e in ("svg", "png", "pdf")}
    with open(rutas["svg"], "w", encoding="utf-8", newline="\n") as fh:
        fh.write(svg)
    ancho_px = round(ancho_cm / 2.54 * DPI)
    subprocess.run([rsvg, "-w", str(ancho_px), "-f", "png", "-o", rutas["png"], rutas["svg"]], check=True)
    grabar_densidad(rutas["png"], DPI)
    entorno = dict(os.environ, SOURCE_DATE_EPOCH=SOURCE_DATE_EPOCH)
    subprocess.run([rsvg, "-f", "pdf", "-o", rutas["pdf"], rutas["svg"]], check=True, env=entorno)
    return rutas


def version_rsvg():
    rsvg = shutil.which("rsvg-convert")
    if not rsvg:
        return "no instalado"
    return subprocess.run([rsvg, "--version"], stdout=subprocess.PIPE, check=True,
                          text=True).stdout.split("\n")[0].strip()


# --------------------------------------------------------------------------- #
# Composición                                                                  #
# --------------------------------------------------------------------------- #
# Prueba negativa -> control que tiene que fallar y texto de la falla propia.
PRUEBAS_NEGATIVAS = (("arista_de_mas", "inventario", "arista de la figura que no está en el grafo"),
                     ("etiqueta_distinta", "inventario", "nodo de la figura que no está en el grafo"),
                     ("cruce", "geometria", "cruce(s) entre trazos"),
                     ("rotulo_sobre_caja", "geometria", "texto sobre la caja"))


def componer(cont, sub, colores, perturbacion=None):
    bloques = bloques_texto(cont)
    aristas = [(o, rel, d, RUTAS[(o, rel, d)]) for o, rel, d in ARISTAS]
    etiquetas = {}
    if perturbacion == "arista_de_mas":
        aristas.append(("condicion_repago", "remite_a", "operacion", "vertical"))
    if perturbacion == "etiqueta_distinta":
        etiquetas["operacion"] = "Inclusión en cartera comercial — créditos de consumo o vivienda"
    if perturbacion == "cruce":
        aristas.append(("condicion_monto", "condicion_de", "condicion_repago", "vertical"))

    alto_texto = alto_panel_texto(bloques, ANCHO_PANEL)
    y_texto = 46
    y_grafo = y_texto + alto_texto + 42
    cajas, alto_grafo = cajas_grafo(sub["nodos"], y_grafo, etiquetas)
    y_leyenda = y_grafo + alto_grafo + 20
    alto_leyenda = 46
    alto_total = y_leyenda + alto_leyenda + MARGEN

    out = [cabecera_svg(W, alto_total, ANCHO_PAGINA_CM),
           f'<rect width="{W}" height="{f(alto_total)}" fill="white"/>', marcadores()]
    out += dibujar_panel_texto(bloques, MARGEN, y_texto, ANCHO_PANEL, alto_texto)
    nodos_dib = dict(sub["nodos"])
    if etiquetas:
        nodos_dib = {k: dict(v, label=etiquetas.get(k, v["label"])) for k, v in nodos_dib.items()}
    panel = dibujar_panel_grafo({"nodos": nodos_dib}, colores, cajas, MARGEN, y_grafo, ANCHO_PANEL,
                                alto_grafo, aristas)
    if perturbacion == "rotulo_sobre_caja":
        c = cajas["operacion"]
        panel.append(f'<text x="{f(c["cx"])}" y="{f(c["cy"] - c["h"] / 2 + 3)}" text-anchor="middle" '
                     f'font-size="{FS_ROTULO}" fill="{GRIS_ROTULO}">limita</text>')
    out += panel
    out += dibujar_leyenda(y_leyenda, alto_leyenda)
    out.append("</svg>")
    return "\n".join(out) + "\n", {"bloques": bloques, "cajas": cajas, "alto": alto_total}


def controlar(cont, sub, colores, perturbacion=None):
    svg, geo = componer(cont, sub, colores, perturbacion)
    c = {}
    c["inventario"], nodos_svg, aristas_svg = controlar_inventario(svg, sub["nodos"], ARISTAS)
    c["geometria"], info = controlar_geometria(svg, ANCHO_PAGINA_CM, W)
    if puntos_impresos(FS_TEXTO) < PT_MIN_TEXTO:
        c["geometria"].append(f"el texto de los recuadros imprime a {puntos_impresos(FS_TEXTO):.2f} pt")
    return svg, geo, c, info, nodos_svg, aristas_svg


def pruebas_negativas(cont, sub, colores):
    vivas = []
    for caso, control, patron in PRUEBAS_NEGATIVAS:
        _, _, c, _, _, _ = controlar(cont, sub, colores, caso)
        propia = [x for x in c[control] if patron in x]
        if not propia:
            freno(f"la prueba negativa {caso} no hizo fallar el control de {control} con «{patron}»")
        vivas.append((caso, control, propia[0], sorted(k for k, v in c.items() if v and k != control)))
    return vivas


def informe_subgrafo(sub, diez):
    print(f"GRAFO: {sub['ruta']}   sha256 {sub['sha256']}   ({sub['n_nodos']} nodos, {sub['n_aristas']} aristas)")
    print(f"  igual en {diez['ruta']}   sha256 {diez['sha256']}   ({diez['n_nodos']} nodos, "
          f"{diez['n_aristas']} aristas): mismos nodos, propiedades y aristas dibujadas")
    for clave, n in sub["nodos"].items():
        print(f"  nodo {clave:17s} {n['type']:10s} punto {n['punto']:8s} {n['label']!r}")
        print(f"       id {n['id']}   (en diez: {diez['nodos'][clave]['id'] == n['id']})")
    for a, b in zip(sub["aristas"], diez["aristas"]):
        print(f"  arista kg['edges'][{a['indice']}] (diez [{b['indice']}]) {a['origen']} --{a['relation']}--> "
              f"{a['destino']}   procedencia {a['chunks']}   properties {json.dumps(a['properties'], ensure_ascii=False)}")
    print("  NO DIBUJADO, aristas de los nodos dibujados hacia fuera del dibujo (nodo, sentido, relación, tipo del otro extremo):")
    for k, v in sorted(sub["afuera"].items()):
        print(f"    {k}: {v}")
    print("  NO DIBUJADO, nodos de la unidad y sus aristas:")
    for k, v in sub["no_dibujados"].items():
        print(f"    {k}: {v}")
    um = sub["nodos"]["condicion_monto"]["properties"].get("umbrales")
    print(f"  NO DIBUJADO, umbrales de condicion_monto: {json.dumps(um, ensure_ascii=False)}")


def argumentos():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--salida", default=AQUI,
                    help="directorio donde escribir el SVG, el PNG y el PDF (por omisión, el del script)")
    ap.add_argument("--perturbar", choices=[c for c, _, _ in PRUEBAS_NEGATIVAS], default=None,
                    help="compone la figura con ese defecto: los controles fallan y no se escribe nada")
    return ap.parse_args()


def main():
    args = argumentos()
    cont = cargar_textos()
    sub = cargar_subgrafo(GRAFO)
    diez = cargar_subgrafo(GRAFO_DIEZ)
    comparar_grafos(sub, diez)
    colores = leer_colores_tipo()
    for t in {n["type"] for n in sub["nodos"].values()}:
        if t not in colores:
            freno(f"la figura del esquema final no tiene caja {t}")

    print("FUENTES (sha256 comprobado):")
    for nombre, par in (("grafo", GRAFO), ("grafo diez", GRAFO_DIEZ), ("chunks_cla", CHUNKS_CLA),
                        ("datos v1", DATOS_V1), ("extractor v1", EXTRACTOR_V1), ("estilo", ESTILO)):
        print(f"  {nombre:13s} {par[0]}   {par[1]}")
    print("TEXTOS (iguales a los de la versión 1):")
    for cid in UNIDADES_TEXTO:
        t = cont["textos"][cid]
        extra = f"   palabras reunidas {t['reunidas']}" if t["reunidas"] else ""
        print(f"  {cid:13s} {t['texto']!r}{extra}")
    print(f"  frase resaltada {cont['frase_resaltada']!r}")
    informe_subgrafo(sub, diez)
    print("COLORES DE TIPO (de la figura del esquema final):")
    for t in sorted({n["type"] for n in sub["nodos"].values()}):
        print(f"  {t:10s} {colores[t]}")

    vivas = pruebas_negativas(cont, sub, colores)
    print(f"PRUEBAS NEGATIVAS: {len(vivas)} de {len(PRUEBAS_NEGATIVAS)} hacen fallar su control")
    for caso, control, falla, otros in vivas:
        print(f"  {caso} -> {control}: {falla}" + (f" (fallan también: {', '.join(otros)})" if otros else ""))

    svg, geo, c, info, nodos_svg, aristas_svg = controlar(cont, sub, colores, args.perturbar)
    if args.perturbar:
        print(f"PERTURBACIÓN: {args.perturbar}")
    print(f"INVENTARIO (releído del SVG): {len(nodos_svg)} nodos y {len(aristas_svg)} aristas; "
          f"fallas: {len(c['inventario'])}")
    for n in nodos_svg:
        print(f"  nodo   {n}")
    for a in aristas_svg:
        print(f"  arista {a[0][0] if a[0] else None} {a[0][1] if a[0] else ''} --{a[1]}--> "
              f"{a[2][0] if a[2] else None} {a[2][1] if a[2] else ''}")
    print(f"GEOMETRÍA: {info['textos']} textos, {info['cajas']} cajas, {info['trazos']} trazos con flecha; "
          f"cruces {len(info['cruces'])}; fallas: {len(c['geometria'])}")
    for k in c:
        for falla in c[k]:
            print(f"  MAL [{k}] {falla}")
    if any(c.values()):
        raise SystemExit("FALLA: la figura tiene defectos; no se escribe nada")
    alto = geo["alto"]
    print(f"TAMAÑO: lienzo {W} x {f(alto)}, impreso a {ANCHO_PAGINA_CM:.2f} x {ANCHO_PAGINA_CM * alto / W:.2f} cm")
    for fs, pt in sorted(info["tamanos"].items()):
        print(f"  letra {fs:g} unidades -> {pt:.2f} pt")
    rutas = exportar(svg, args.salida, NOMBRE, ANCHO_PAGINA_CM)
    for e in ("svg", "png", "pdf"):
        print(f"{e.upper()}: {os.path.relpath(rutas[e], RAIZ)}   sha256 {sha256(rutas[e])}")
    print(f"  PNG {png_dimensiones(rutas['png'])} px a {DPI} dpi; {version_rsvg()}")


if __name__ == "__main__":
    try:
        main()
    except Freno as e:
        raise SystemExit(f"FRENO {e}")
