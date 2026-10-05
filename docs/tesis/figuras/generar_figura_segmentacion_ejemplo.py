#!/usr/bin/env python3
"""Figura del ejemplo de la segmentación (capítulo 4, sección 4.1), POR SCRIPT y nunca a mano.

Qué dibuja, a 15 cm de ancho, en dos partes:
- a la izquierda, el fragmento del punto 5.1.1 de Clasificación de deudores
  como aparece en el documento, bajo el nombre del documento y el número de su
  página: el título del punto, su párrafo propio y sus subpuntos, cada
  subpunto con su número y su primera línea, cortada con «…» si no entra;
- a la derecha, las unidades de extracción que la segmentación saca de ese
  fragmento: una tarjeta por unidad, unida por una flecha a la parte del
  fragmento de la que sale, que una llave marca. La tarjeta del 5.1.1.1 va
  abierta y muestra, con rótulos en castellano, su cadena estructural como tres
  bloques en gris, cada uno con su título (la sección 5, el 5.1 y el 5.1.1),
  su texto propio (las primeras líneas), sus páginas y sus marcas. Las otras
  dos van cerradas, solo con su nombre: «5.1.1, párrafo» y «5.1.1.2».
Los bloques de la cadena llevan solo su título: la figura de la unidad del
capítulo 3 (generar_figura_unidad_extraccion.py) ya muestra la cadena con su
texto completo, y esta no la repite. El gris de la cadena es el único color
nuevo frente a la figura del proceso: separa el contexto heredado del texto
propio. La figura no lleva identificadores internos, nombres de archivo ni
nombres de campos del código: las unidades se nombran por su punto.

Estilo: el de la figura del proceso (generar_figura_proceso.py), con su
paleta, su tipografía, sus cuerpos, interlíneas, márgenes, grosores, esquinas,
puntas de flecha, la hoja con la esquina plegada y su tabla de métricas AFM.
El generador no importa ese módulo: lo lee como texto, con candado de sha256,
y coteja cada valor que usa con la línea que lo declara (ESTILO); si cambia,
frena antes de dibujar.

Fuentes (FUENTES), todas con candado de sha256:
  - generar_figura_proceso.py: el estilo y la tabla AFM de Helvetica y
    Helvetica-Bold, a la que se suma «…» (1000 en las dos, de los mismos
    archivos AFM de Adobe que cita el registro de esa figura);
  - la segmentación de Clasificación de deudores de la tanda 0 con e0-r2,
    e0_chunking/salida_tanda0_r2b/ (commit 9f6361e): chunks_cla.json (las
    unidades, su texto, su cadena, sus páginas y sus marcas) y
    estructura_cla.json (el árbol del 5.1.1: su título, su párrafo propio y
    sus subpuntos);
  - el PDF de Clasificación de deudores del corpus: cada texto del fragmento,
    cada título de la cadena y la primera línea del texto propio son líneas
    de la página que declara la segmentación, en el orden del documento, y el
    nombre del documento, en mayúsculas, es el encabezado de esa página.

Controles (verificar(); el primero que falla FRENA y no se escribe nada):
  1. contenido: inventario contra la fuente. Cada texto dibujado es de una
     entrada del inventario, y cada entrada se dibuja: literal (igual a su
     fuente), cortada (un prefijo de su fuente que termina en una palabra
     entera, seguido de «…»), partida (sus renglones, unidos por un blanco,
     dan la fuente) o propia (un rótulo de la figura, derivado de la fuente
     cuando nombra una unidad, una página o una marca). Ningún texto lleva
     identificadores internos, nombres de archivo ni nombres de campos del
     código. Cada caja tiene su clase;
  2. trazado: ningún tramo diagonal, nulo ni de vuelta; cada flecha sale del
     lomo de la llave de su parte, hacia afuera, y llega al borde izquierdo de
     la tarjeta de su unidad, lejos de las esquinas; las flechas son
     exactamente una por unidad, de su parte a su tarjeta;
  3. cajas: dos cajas que no se contienen no se superponen y quedan a la
     separación mínima; un bloque queda dentro de su tarjeta con aire; ningún
     trazo, punta ni llave entra en una caja;
  4. cruces: entre dos flechas, ningún cruce ni contacto, y la distancia
     mínima; ninguna punta toca otra flecha; ninguna flecha toca una llave
     ajena;
  5. textos: ninguno por debajo de 7 pt impresos, fuera del lienzo o de su
     caja, superpuesto a otra caja, a otro texto o a una marca, ni tocado por
     un trazo o una punta;
  6. margen: nada a menos de 2 mm del borde del lienzo;
  7. registro y colores: el SVG emitido se relee; cada elemento está
     registrado, en orden; cada caja, llave, flecha y texto tiene el color de
     su clase, y el gris de la cadena solo está en los bloques de la cadena.
Pruebas negativas (corren en cada ejecución, antes de escribir): una por
control como mínimo (MUTACIONES y PRUEBAS_FUENTE); cada una tiene que frenar
en el control que le corresponde, con su motivo.

Salidas, byte-reproducibles: figura_segmentacion_ejemplo.svg, .png (300 dpi,
densidad grabada) y .pdf (rsvg-convert con SOURCE_DATE_EPOCH=0).

Uso (desde la raíz del repo):
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_segmentacion_ejemplo.py
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_segmentacion_ejemplo.py --salida <dir>
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_segmentacion_ejemplo.py --mutacion cruce_entre_flechas
"""

from __future__ import annotations

import argparse
import ast
import copy
import hashlib
import io
import json
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
import pdfplumber                                     # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", ".."))
NOMBRE = "figura_segmentacion_ejemplo"


class Freno(Exception):
    """Falla de un control: la figura no se escribe."""


def freno(control: str, motivo: str):
    raise Freno(f"[{control}] {motivo}")


# ========================================================================== #
# Fuentes y candados                                                         #
# ========================================================================== #
FIG = "docs/tesis/figuras"
E0 = "data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b"
FUENTES = {
    "estilo": (f"{FIG}/generar_figura_proceso.py",
               "8667c219fe5586466e3cad04bc81843a8b39025d59b443edbacf79740349cbbf"),
    "unidades": (f"{E0}/chunks_cla.json",
                 "98808886a406d8321c678836a55f92eea983d594d95358dd21ceb537487ac0b1"),
    "estructura": (f"{E0}/estructura_cla.json",
                   "3cd26083fee7355ef3d8027ac353a744c2f1cfa35830535fe1be2b9505eaf917"),
    "pdf": ("data/experiment/subset/TO_clasificacion_deudores_actual.pdf",
            "6e7f528d3fea7b756f15e1278eecd828f203f0651fc6f778212033de6a0883e2"),
}


def sha256(ruta: str) -> str:
    with open(ruta, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def candado(clave: str, crudo: bytes) -> None:
    rel, esperado = FUENTES[clave]
    sha = hashlib.sha256(crudo).hexdigest()
    if sha != esperado:
        freno("fuentes", f"{rel} no es el verificado: sha256 {sha[:12]}… ≠ {esperado[:12]}…")


def leer_crudo(clave: str) -> bytes:
    with open(os.path.join(RAIZ, FUENTES[clave][0]), "rb") as fh:
        crudo = fh.read()
    candado(clave, crudo)
    return crudo


# ========================================================================== #
# Estilo (el de la figura del proceso)                                       #
# ========================================================================== #
W = 760                                  # unidades de lienzo para 15 cm
TIPOGRAFIA = "Helvetica,Arial,sans-serif"
NEUTRO = {"relleno": "#fafafa", "borde": "#999999"}
TINTA, TINTA_SUB = "#1f1f1f", "#444444"
FLECHA = "#555555"
BLANCO = "white"                         # el relleno de la caja discontinua del proceso
FS_TITULO, FS_TEXTO = 14, 13
IL = {FS_TITULO: 18, FS_TEXTO: 17}
PAD_X, PAD_Y = 9, 11
GROSOR_CAJA, GROSOR_LLAVE = 1.6, 1.3     # el de las cajas y el de la caja discontinua
GROSOR_FLUJO = 1.8
RADIO = 9                                # esquinas de los trazos
RX = 8                                   # esquinas de las cajas
MARGEN = 12
GROSOR_BLOQUE = 1                        # el del marco de la leyenda del proceso
RX_BLOQUE = 3                            # el de las muestras de la leyenda del proceso
MARCADOR_A = 'viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
MARCADOR_B = 'markerHeight="6" orient="auto"><path d="M0,0L10,5L0,10z"'
MARCADOR = MARCADOR_A + MARCADOR_B
PLIEGUE = 20
ANCHO_CM = 15.0
DPI = 300
PT_MINIMO = 7.0
MARGEN_MM = 2.0
HOLGURA_TEXTO = 1.5      # de un texto a un trazo, una marca o el borde de su caja
DISTANCIA_MIN = 3.0      # entre dos flechas, y de una flecha a una llave ajena
SEP_CAJAS = 8.0          # entre los bordes de dos cajas que no se contienen
HUECO_PUNTA = 2.0        # del final del trazo al borde de la caja de destino
LEJOS_ESQUINA = RX + 4   # un extremo de flecha, de las esquinas redondeadas de su caja
ASC, DESC = 0.78, 0.22   # alto sobre y bajo la línea de base, en em
SOURCE_DATE_EPOCH = "0"
# El único color nuevo: el gris de los bloques de la cadena estructural.
GRIS_CADENA = "#e6e6e6"

# nombre → (patrón de la línea de generar_figura_proceso.py que lo declara,
# conversión, valor que la figura usa). «lit» lee los grupos como literales de
# Python; «txt», como texto. Cada patrón tiene que estar en una sola línea.
ESTILO = {
    "W": (r'^W = (\d+) ', "lit", W),
    "TIPOGRAFIA": (r'^TIPOGRAFIA = ("[^"]+")$', "lit", TIPOGRAFIA),
    "NEUTRO": (r'^NEUTRO = (\{[^}]*\})$', "lit", NEUTRO),
    "TINTA, TINTA_SUB": (r'^TINTA, TINTA_SUB = ("#[0-9a-f]{6}"), ("#[0-9a-f]{6}")$', "lit", (TINTA, TINTA_SUB)),
    "FLECHA": (r'^FLECHA, GRIS_ARISTA = ("#[0-9a-f]{6}"), "#[0-9a-f]{6}"$', "lit", FLECHA),
    "DISCONTINUA (relleno)": (r'^DISCONTINUA = \{"relleno": ("\w+"), "borde": GRIS_ARISTA\}$', "lit", BLANCO),
    "FS_TITULO, FS_TEXTO": (r'^FS_TITULO, FS_TEXTO = (\d+), (\d+)$', "lit", (FS_TITULO, FS_TEXTO)),
    "IL": (r'^IL = \{FS_TITULO: (\d+), FS_TEXTO: (\d+)\}$', "lit", (IL[FS_TITULO], IL[FS_TEXTO])),
    "PAD_X, PAD_Y": (r'^PAD_X, PAD_Y = (\d+), (\d+)$', "lit", (PAD_X, PAD_Y)),
    "GROSOR_CAJA, GROSOR_DISCONTINUA": (r'^GROSOR_CAJA, GROSOR_DISCONTINUA = ([\d.]+), ([\d.]+)$', "lit",
                                        (GROSOR_CAJA, GROSOR_LLAVE)),
    "GROSOR_FLUJO": (r'^GROSOR_FLUJO, GROSOR_RAMA = ([\d.]+), [\d.]+$', "lit", GROSOR_FLUJO),
    "RADIO": (r'^RADIO = (\d+) ', "lit", RADIO),
    "RX": (r'^RX = (\d+) ', "lit", RX),
    "MARGEN": (r'^MARGEN = (\d+)$', "lit", MARGEN),
    "LEYENDA_MARCO (grosor)": (r'^LEYENDA_MARCO = \'fill="white" stroke="#e2e2e2" stroke-width="(\d+)" rx="5"\'$',
                               "lit", GROSOR_BLOQUE),
    "muestra de la leyenda (esquina)": (r"^            f'stroke-width=\"\{GROSOR_CAJA\}\" rx=\"(\d+)\"/>'\)$",
                                        "lit", RX_BLOQUE),
    "MARCADOR_A": (r"^MARCADOR_A = '(" + re.escape(MARCADOR_A) + r")'$", "txt", MARCADOR_A),
    "MARCADOR_B": (r"^MARCADOR_B = '(" + re.escape(MARCADOR_B) + r")'$", "txt", MARCADOR_B),
    "PLIEGUE": (r'^PLIEGUE = (\d+)$', "lit", PLIEGUE),
    "ANCHO_CM": (r'^ANCHO_CM = ([\d.]+)$', "lit", ANCHO_CM),
    "DPI": (r'^DPI = (\d+)$', "lit", DPI),
    "PT_MINIMO": (r'^PT_MINIMO = ([\d.]+)$', "lit", PT_MINIMO),
    "MARGEN_MM": (r'^MARGEN_MM = ([\d.]+)$', "lit", MARGEN_MM),
    "HOLGURA_TEXTO": (r'^HOLGURA_TEXTO = ([\d.]+) ', "lit", HOLGURA_TEXTO),
    "DISTANCIA_MIN": (r'^DISTANCIA_MIN = ([\d.]+) ', "lit", DISTANCIA_MIN),
    "SEP_CAJAS": (r'^SEP_CAJAS = ([\d.]+) ', "lit", SEP_CAJAS),
    "HUECO_PUNTA": (r'^HUECO_PUNTA = ([\d.]+) ', "lit", HUECO_PUNTA),
    "LEJOS_ESQUINA": (r'^LEJOS_ESQUINA = RX \+ (\d+) ', "lit", LEJOS_ESQUINA - RX),
    "ASC, DESC": (r'^ASC, DESC = ([\d.]+), ([\d.]+) ', "lit", (ASC, DESC)),
    "SOURCE_DATE_EPOCH": (r'^SOURCE_DATE_EPOCH = ("\d+")$', "lit", SOURCE_DATE_EPOCH),
}
# «…» no está en la tabla AFM de la figura del proceso. Su ancho es 1000 en
# Helvetica y en Helvetica-Bold («C 188 ; WX 1000 ; N ellipsis» en los dos
# archivos AFM de Adobe que cita el registro de esa figura).
AGREGADOS_AFM = {"…": (1000, 1000)}


def cotejar_estilo(texto: str, estilo: dict) -> dict:
    """Coteja cada valor de estilo con la línea que lo declara; devuelve los lugares."""
    lugares = {}
    lineas = texto.splitlines()
    for nombre, (patron, conv, usado) in estilo.items():
        hallados = [(i + 1, m.groups()) for i, l in enumerate(lineas) for m in [re.search(patron, l)] if m]
        if len(hallados) != 1:
            freno("estilo", f"{nombre}: {len(hallados)} líneas con {patron!r} en {FUENTES['estilo'][0]}, "
                            f"se esperaba una")
        n, grupos = hallados[0]
        vals = [ast.literal_eval(g) if conv == "lit" else g for g in grupos]
        leido = vals[0] if len(vals) == 1 else tuple(vals)
        if leido != usado:
            freno("estilo", f"{nombre}: la figura usa {usado!r} y {FUENTES['estilo'][0]}:{n} declara {leido!r}")
        lugares[nombre] = f"{FUENTES['estilo'][0]}:{n}"
    return lugares


def leer_afm(texto: str) -> tuple[dict, str]:
    """La tabla AFM de la figura del proceso: `_CARS` y los anchos de `_AFM`,
    leídos del árbol sintáctico sin ejecutar el módulo."""
    cars, tablas, lugar = None, {}, []
    for nodo in ast.parse(texto).body:
        if not (isinstance(nodo, ast.Assign) and len(nodo.targets) == 1 and isinstance(nodo.targets[0], ast.Name)):
            continue
        nombre = nodo.targets[0].id
        if nombre == "_CARS":
            cars = ast.literal_eval(nodo.value)
            lugar.append(f"_CARS :{nodo.lineno}")
        elif nombre == "_AFM":
            lugar.append(f"_AFM :{nodo.lineno}-{nodo.end_lineno}")
            for k, v in zip(nodo.value.keys, nodo.value.values):
                ok = (isinstance(v, ast.Call) and getattr(v.func, "id", "") == "dict" and len(v.args) == 1
                      and isinstance(v.args[0], ast.Call) and getattr(v.args[0].func, "id", "") == "zip"
                      and getattr(v.args[0].args[0], "id", "") == "_CARS")
                if not ok:
                    freno("estilo", "la tabla _AFM de la figura del proceso no tiene la forma dict(zip(_CARS, …))")
                tablas[ast.literal_eval(k)] = ast.literal_eval(v.args[0].args[1])
    if cars is None or sorted(tablas, key=str) != [False, True] or any(len(t) != len(cars) for t in tablas.values()):
        freno("estilo", "la tabla AFM de la figura del proceso no se pudo leer entera")
    afm = {neg: dict(zip(cars, anchos)) for neg, anchos in tablas.items()}
    for c, (normal, negrita) in AGREGADOS_AFM.items():
        if c in cars:
            freno("estilo", f"«{c}» ya está en la tabla AFM de la figura del proceso")
        afm[False][c], afm[True][c] = normal, negrita
    return afm, ", ".join(lugar)


# ========================================================================== #
# Lo que la figura afirma (lo fijo; el resto se deriva de las fuentes)       #
# ========================================================================== #
TO_NOMBRE = "Clasificación de deudores"     # en mayúsculas, el encabezado de la página
PUNTO = "5.1.1"                             # el punto del ejemplo
ABIERTA = "5.1.1.1"                         # la unidad que va abierta
MAX_SUBPUNTOS = 5                           # con más, la figura tendría que resumirlos
PRIMERAS_LINEAS = 2                         # del texto propio de la unidad abierta
ENCABEZADO_UNIDADES = "Unidades de extracción"
ROTULO_CADENA = "Cadena estructural"
ROTULO_PROPIO = "Texto propio"
ROTULO_PAGINAS = "Páginas: {}"
ROTULO_MARCAS = "Marcas: {}"
SIN_MARCAS = "ninguna"
NOMBRE_PARRAFO = "{}, párrafo"
# Las marcas que la segmentación pone a una unidad, con su nombre en la figura.
MARCAS = (("contenido_tabular", "contenido tabular"), ("formula", "fórmula"))
# Nada de esto puede aparecer en un texto dibujado: identificadores internos,
# nombres de archivo y nombres de campos del código.
PROHIBIDOS = (re.compile(r"::"), re.compile(r"_"), re.compile(r"[/\\]"),
              re.compile(r"\.(jsonl?|py|md|db|pdf|txt|svg|png)\b", re.I),
              re.compile(r"\bcla\b", re.I), re.compile(r"chunk", re.I), re.compile(r"\bmini\b", re.I),
              re.compile(r"\b(intro|cierre|encabezado|herencia|flags?|paginas|tipo|unidad_origen)\b"),
              re.compile(r"\b(e0|E0|r2b?|sha)\b"), re.compile(r"\b[0-9a-f]{7,64}\b"))


# ========================================================================== #
# Tamaño impreso y composición                                               #
# ========================================================================== #
PT_POR_CM = 72.0 / 2.54
ANCHO_PNG_PX = round(ANCHO_CM / 2.54 * DPI)        # 1772
MARGEN_MIN = MARGEN_MM * W / (ANCHO_CM * 10)       # 10,1 unidades
ANCHO_HOJA = 320
ANCHO_TARJETA = 320
SANGRIA = 14             # párrafo y subpuntos, a la derecha del título del punto, como en el documento
SEP_PARTES = 8           # aire entre las partes del fragmento: el documento separa sus párrafos
SOBRE_CONTENIDO = 8      # de los encabezados a la hoja y a la primera tarjeta
SEP_TARJETAS = 12        # mínimo entre dos tarjetas
LLAVE_DX = 10            # del borde de la hoja al lomo de las llaves
LLAVE_PATA = 5           # largo de las patas de una llave
GIRO_ARRIBA, GIRO_ABAJO = 0.35, 0.65   # dónde doblan las flechas, en fracción del pasillo
PAD_BX, PAD_BY = 6, 3    # aire interno de los bloques de la tarjeta abierta
SEP_BLOQUES = 4          # entre dos bloques de la cadena
SEP_GRUPO = 6            # entre los grupos de la tarjeta abierta
BAJO_ROTULO = 3          # de un rótulo a sus bloques
SEP_BLOQUES_MIN = 2.0    # control: entre dos bloques hermanos
AIRE_CONTENIDO = 3.0     # control: de un bloque al borde de su tarjeta


def puntos_impresos(unidades: float) -> float:
    return unidades * ANCHO_CM * PT_POR_CM / W


def f(v: float) -> str:
    """Formato fijo: el SVG no depende de la representación del float."""
    return f"{v:.1f}"


# ========================================================================== #
# Lectura y derivación del contenido                                         #
# ========================================================================== #
def lineas_pdf(crudo: bytes, paginas: tuple) -> dict:
    """Líneas de texto (extract_text_lines) de las páginas pedidas, desde 1."""
    out = {}
    with pdfplumber.open(io.BytesIO(crudo)) as pdf:
        for p in paginas:
            out[p] = [l["text"] for l in pdf.pages[p - 1].extract_text_lines()]
    return out


def leer_fuentes() -> dict:
    crudos = {c: leer_crudo(c) for c in FUENTES}
    texto_estilo = crudos["estilo"].decode("utf-8")
    D = {"lugares": cotejar_estilo(texto_estilo, ESTILO)}
    D["afm"], D["lugar_afm"] = leer_afm(texto_estilo)
    D["texto_unidades"] = crudos["unidades"].decode("utf-8")
    D["texto_estructura"] = crudos["estructura"].decode("utf-8")
    D["unidades"] = json.loads(D["texto_unidades"])
    D["estructura"] = json.loads(D["texto_estructura"])
    D["pdf_crudo"] = crudos["pdf"]
    return D


def buscar_camino(estructura: dict, numero: str) -> list[dict]:
    """El camino del árbol hasta el punto `numero`: [sección, …, punto]."""
    hallados = []

    def bajar(nodo, camino):
        camino = camino + [nodo]
        if nodo.get("tipo") == "punto" and nodo.get("numero") == numero:
            hallados.append(camino)
        for h in nodo.get("hijos", []):
            bajar(h, camino)

    for s in estructura["secciones"]:
        bajar(s, [])
    if len(hallados) != 1:
        freno("contenido", f"el punto {numero} está {len(hallados)} veces en la estructura, no una")
    return hallados[0]


def titulo_linea(nodo: dict) -> str:
    """El título de un nodo como lo escribe el documento (y la cadena)."""
    if nodo["tipo"] == "seccion":
        return f"Sección {nodo['numero']}. {nodo['titulo']}"
    return f"{nodo['numero']}. {nodo['titulo']}"


def ubicar(lineas: list[str], texto: str, que: str) -> int:
    """Índice (desde 1) de la primera de las líneas consecutivas de la página
    que dan `texto` con sus saltos de línea; tiene que haber una sola."""
    partes = texto.split("\n")
    hallados = [i for i in range(len(lineas) - len(partes) + 1) if lineas[i:i + len(partes)] == partes]
    if len(hallados) != 1:
        freno("contenido", f"{que}: {len(hallados)} apariciones en la página, se esperaba una: {texto[:60]!r}")
    return hallados[0] + 1


def linea_json(texto: str, patron: str, desde: int = 1) -> int:
    """Número de la primera línea, desde la línea `desde`, que contiene `patron`."""
    for i, l in enumerate(texto.splitlines()[desde - 1:], start=desde):
        if patron in l:
            return i
    freno("contenido", f"no se encontró {patron!r} en el archivo")


def derivar(D: dict) -> dict:
    """Lo que la figura dibuja, derivado de las fuentes y contrastado entre ellas."""
    camino = buscar_camino(D["estructura"], PUNTO)
    nodo = camino[-1]
    pagina = nodo["pagina"]
    hijos = nodo["hijos"]
    if len(hijos) > MAX_SUBPUNTOS:
        freno("contenido", f"el {PUNTO} tiene {len(hijos)} subpuntos (más de {MAX_SUBPUNTOS}): "
                           f"la figura no prevé resumirlos")
    if any(h["hijos"] for h in hijos):
        freno("contenido", f"un subpunto del {PUNTO} tiene subpuntos: la figura no lo prevé")
    if [s["rol"] for s in nodo["segmentos"]] != ["intro"]:
        freno("contenido", f"el {PUNTO} no tiene un único párrafo propio antes de sus subpuntos: "
                           f"{[s['rol'] for s in nodo['segmentos']]}")
    parrafo = nodo["segmentos"][0]["texto"]

    # Las unidades que salen del punto: su párrafo propio y una por subpunto,
    # en el orden del archivo, que tiene que ser el del documento.
    del_punto = [u for u in D["unidades"] if u["unidad"] == PUNTO or u["unidad"].startswith(PUNTO + ".")]
    esperado = [(PUNTO, "mini_chunk", "intro")] + [(h["numero"], "punto_terminal", None) for h in hijos]
    obtenido = [(u["unidad"], u["tipo"], u.get("rol_bloque")) for u in del_punto]
    if obtenido != esperado:
        freno("contenido", f"las unidades del {PUNTO} son {obtenido}; la estructura pide {esperado}")
    if [u["unidad"] for u in del_punto].count(ABIERTA) != 1:
        freno("contenido", f"la unidad {ABIERTA} no sale del {PUNTO}")
    for u in del_punto:
        if u["paginas"] != [pagina]:
            freno("contenido", f"la unidad {u['unidad']} está en las páginas {u['paginas']}; "
                               f"el {PUNTO} está en la {pagina}")

    # El PDF: el nombre del documento y las líneas de la página.
    lineas = lineas_pdf(D["pdf_crudo"], (pagina,))[pagina]
    if lineas[0] != TO_NOMBRE.upper():
        freno("contenido", f"el encabezado de la página {pagina} es {lineas[0]!r}, no {TO_NOMBRE.upper()!r}")
    tu, te = D["texto_unidades"], D["texto_estructura"]
    ruta_est = FUENTES["estructura"][0]
    a_est = linea_json(te, f'"numero": "{PUNTO}"')
    a_seg = linea_json(te, '"texto": ', a_est)
    anclas = [("estructura: el punto", f"{ruta_est}:{a_est}"),
              ("estructura: su párrafo propio", f"{ruta_est}:{a_seg}")]
    for h in hijos:
        a_h = linea_json(te, f'"numero": "{h["numero"]}"', a_est)
        anclas.append((f"estructura: el subpunto {h['numero']}", f"{ruta_est}:{a_h}"))
    pdf_lineas = {}

    def en_pdf(clave, texto, que):
        pdf_lineas[clave] = ubicar(lineas, texto, que)
        return pdf_lineas[clave]

    # Fragmento: el título del punto, su párrafo y la primera línea de cada subpunto.
    titulo = titulo_linea(nodo)
    fragmento = [{"clave": "titulo", "origen": titulo, "modo": "literal", "unidad": None,
                  "pdf": en_pdf("titulo", titulo, f"el título del {PUNTO}")}]
    unidades = []
    for k, u in enumerate(del_punto):
        a_id = linea_json(tu, f'"id": "{u["id"]}"')
        a_texto = linea_json(tu, '"texto": ', a_id)
        a_pags = linea_json(tu, '"paginas": ', a_id)
        a_flags = linea_json(tu, '"flags": ', a_id)
        marcas = [nombre for campo, nombre in MARCAS if u["flags"][campo]]
        if sorted(k2 for k2 in u["flags"] if not k2.startswith("evidencia_")) != sorted(c for c, _ in MARCAS):
            freno("contenido", f"la unidad {u['unidad']} tiene marcas que la figura no conoce: {sorted(u['flags'])}")
        if u["tipo"] == "mini_chunk":
            if u["texto"] != parrafo:
                freno("contenido", f"el texto de la unidad del párrafo no es el párrafo del {PUNTO} en la estructura")
            nombre = NOMBRE_PARRAFO.format(u["unidad"])
            parte = {"clave": f"parte_{k}", "origen": parrafo, "modo": "partido", "unidad": k,
                     "pdf": en_pdf(f"parte_{k}", parrafo, f"el párrafo del {PUNTO}")}
        else:
            nombre = u["unidad"]
            primera = u["texto"].split("\n")[0]
            if not primera.startswith(u["unidad"] + ". "):
                freno("contenido", f"el texto de la unidad {u['unidad']} no empieza con su número")
            parte = {"clave": f"parte_{k}", "origen": primera, "modo": "primera", "unidad": k,
                     "pdf": en_pdf(f"parte_{k}", u["texto"], f"el texto de la unidad {u['unidad']}")}
        fragmento.append(parte)
        un = {"indice": k, "nombre": nombre, "abierta": u["unidad"] == ABIERTA, "paginas": u["paginas"],
              "marcas": marcas, "anclas": {"id": a_id, "texto": a_texto, "paginas": a_pags, "flags": a_flags}}
        anclas.append((f"unidad «{nombre}»: registro, texto, páginas, marcas",
                       f"{FUENTES['unidades'][0]}:{a_id}, :{a_texto}, :{a_pags}, :{a_flags}"))
        if un["abierta"]:
            # La cadena: un bloque por ancestro, en orden, que empieza con su título.
            bloques = []
            desde = linea_json(tu, '"herencia": ', a_id)
            for t in u["herencia"]:
                a_t = linea_json(tu, '"texto": ' + json.dumps(t["texto"], ensure_ascii=False), desde)
                desde = a_t + 1
                if t["tipo"] == "encabezado":
                    bloques.append({"origen": t["unidad_origen"], "titulo": t["texto"], "tramos": [t["tipo"]],
                                    "ancla": a_t})
                elif bloques and bloques[-1]["origen"] == t["unidad_origen"]:
                    bloques[-1]["tramos"].append(t["tipo"])
                else:
                    freno("contenido", f"la cadena de {ABIERTA} tiene un tramo sin el título de su bloque")
            ancestros = [("S" + a["numero"] if a["tipo"] == "seccion" else a["numero"], titulo_linea(a))
                         for a in camino]
            if [(b["origen"], b["titulo"]) for b in bloques] != ancestros:
                freno("contenido", f"la cadena de {ABIERTA} no es la de sus ancestros en la estructura: "
                                   f"{[(b['origen'], b['titulo']) for b in bloques]} ≠ {ancestros}")
            for i, b in enumerate(bloques):
                b["pdf"] = en_pdf(f"cadena_{i}", b["titulo"], f"el título del bloque {b['origen']}")
                anclas.append((f"cadena de «{nombre}», bloque {i + 1} ({'+'.join(b['tramos'])})",
                               f"{FUENTES['unidades'][0]}:{b['ancla']}"))
            un["cadena"] = bloques
            un["texto"] = u["texto"].split("\n")
        unidades.append(un)
    orden = [p["pdf"] for p in fragmento]
    if orden != sorted(orden) or len(set(orden)) != len(orden):
        freno("contenido", f"las partes del fragmento no están en el orden del documento: líneas {orden}")
    paginas = sorted({p for u in unidades for p in u["paginas"]})
    return {"pagina": pagina, "paginas": paginas, "fragmento": fragmento, "unidades": unidades,
            "anclas": anclas, "pdf_lineas": pdf_lineas, "lineas_pagina": lineas, "parrafo": parrafo,
            "encabezado_documento": f"{TO_NOMBRE}, página {pagina}"}


# ========================================================================== #
# Métrica de texto                                                           #
# ========================================================================== #
AFM = {}                 # se llena con la tabla de la figura del proceso


def ancho(s: str, fs: float, negrita: bool) -> float:
    tabla = AFM[negrita]
    falta = sorted({c for c in s if c not in tabla})
    if falta:
        freno("textos", f"caracteres sin medida AFM en {s!r}: {falta}")
    return sum(tabla[c] for c in s) * fs / 1000.0


def partir(s: str, disponible: float, fs: int, negrita: bool) -> list[str]:
    """Renglones de `s`, partidos en blancos, que entran en `disponible`."""
    out, actual = [], ""
    for palabra in s.split(" "):
        prueba = palabra if not actual else actual + " " + palabra
        if actual and ancho(prueba, fs, negrita) > disponible:
            out.append(actual)
            actual = palabra
        else:
            actual = prueba
    out.append(actual)
    if any(ancho(r, fs, negrita) > disponible for r in out):
        freno("textos", f"una palabra de {s[:40]!r}… no entra en {disponible:.1f}")
    return out


def cortar(s: str, disponible: float, fs: int, negrita: bool) -> str:
    """`s` si entra; si no, el prefijo más largo que termina en una palabra
    entera y que, con «…», entra."""
    if ancho(s, fs, negrita) <= disponible:
        return s
    palabras = s.split(" ")
    for n in range(len(palabras) - 1, 0, -1):
        prueba = " ".join(palabras[:n]) + "…"
        if ancho(prueba, fs, negrita) <= disponible:
            return prueba
    freno("textos", f"{s[:40]!r}… no entra ni con una palabra")


# ========================================================================== #
# Composición                                                                #
# ========================================================================== #
def armar_modelo(C: dict) -> dict:
    """Ubica cajas, textos, llaves y flechas, y arma el inventario. Todo se
    deriva de las constantes, de los anchos de texto y del contenido; nada se
    dibuja todavía."""
    M = {"cajas": {}, "textos": [], "llaves": [], "trazos": [], "inventario": []}
    cajas, textos = M["cajas"], M["textos"]

    def caja(clave, x, y, w, h, clase, forma="rect", padre=None):
        cajas[clave] = {"clave": clave, "x": float(f(x)), "y": float(f(y)), "w": float(f(w)), "h": float(f(h)),
                        "clase": clase, "forma": forma, "padre": padre}
        return cajas[clave]

    def texto(s, fs, negrita, x, y_linea, dentro, inv, color=None):
        base = y_linea + (IL[fs] - fs) / 2.0 + ASC * fs
        textos.append({"s": s, "fs": fs, "negrita": negrita, "color": color or (TINTA if negrita else TINTA_SUB),
                       "ancla": "start", "x": float(f(x)), "y": float(f(base)), "dentro": dentro, "inv": inv})

    def inventario(clave, modo, origen, lineas, fuente):
        M["inventario"].append({"clave": clave, "modo": modo, "origen": origen, "lineas": list(lineas),
                                "fuente": fuente})

    x_hoja = float(MARGEN)
    x_tarj = float(W - MARGEN - ANCHO_TARJETA)
    # ---- encabezados de las dos partes ---------------------------------- #
    texto(C["encabezado_documento"], FS_TITULO, True, x_hoja, MARGEN, None, "encabezado_documento")
    inventario("encabezado_documento", "propio", C["encabezado_documento"], [C["encabezado_documento"]],
               "nombre del documento (encabezado de la página) y página del punto")
    texto(ENCABEZADO_UNIDADES, FS_TITULO, True, x_tarj, MARGEN, None, "encabezado_unidades")
    inventario("encabezado_unidades", "propio", ENCABEZADO_UNIDADES, [ENCABEZADO_UNIDADES], "rótulo de la figura")
    y_top = MARGEN + IL[FS_TITULO] + SOBRE_CONTENIDO

    # ---- la hoja con el fragmento --------------------------------------- #
    util = ANCHO_HOJA - 2 * PAD_X - 2
    yy = y_top + PAD_Y
    partes = {}
    for i, p in enumerate(C["fragmento"]):
        if i:
            yy += SEP_PARTES
        sangria = 0 if p["clave"] == "titulo" else SANGRIA
        disponible = util - sangria
        if p["modo"] == "partido":
            lineas, modo = partir(p["origen"], disponible, FS_TEXTO, False), "partido"
        elif p["modo"] == "primera":
            lineas = [cortar(p["origen"], disponible, FS_TEXTO, False)]
            modo = "literal" if lineas[0] == p["origen"] else "cortado"
        else:
            lineas, modo = [p["origen"]], "literal"
        y0 = yy
        for s in lineas:
            texto(s, FS_TEXTO, False, x_hoja + PAD_X + 1 + sangria, yy, "hoja", p["clave"])
            yy += IL[FS_TEXTO]
        inventario(p["clave"], modo, p["origen"], lineas, f"PDF, página {C['pagina']}, línea {p['pdf']}")
        partes[p["clave"]] = {"y0": y0, "y1": yy, "unidad": p["unidad"]}
    caja("hoja", x_hoja, y_top, ANCHO_HOJA, yy + PAD_Y - y_top, "datos", "hoja")
    H = cajas["hoja"]

    # ---- llaves: una por parte que da una unidad ------------------------- #
    x_lomo = H["x"] + H["w"] + LLAVE_DX
    ini_llave = {}
    for clave, pt in partes.items():
        if pt["unidad"] is None:
            continue
        borde = (IL[FS_TEXTO] - FS_TEXTO) / 2.0
        y0, y1 = pt["y0"] + borde, pt["y1"] - borde
        nombre = C["unidades"][pt["unidad"]]["nombre"]
        M["llaves"].append({"nombre": f"llave de «{nombre}»", "unidad": pt["unidad"], "x": float(f(x_lomo)),
                            "y0": float(f(y0)), "y1": float(f(y1))})
        ini_llave[pt["unidad"]] = (float(f(x_lomo)), float(f((y0 + y1) / 2.0)))

    # ---- tarjetas -------------------------------------------------------- #
    w_bloque = ANCHO_TARJETA - 2 * PAD_X
    util_bloque = w_bloque - 2 * PAD_BX - 2
    llegada = {}
    y_prev, gap_abierta = None, None
    for u in C["unidades"]:
        k = u["indice"]
        clave = f"tarjeta_{k}"
        y_ini = ini_llave[k][1]
        if y_prev is None:
            top = y_top
        elif u["abierta"]:
            # La flecha llega a la altura del nombre de la tarjeta abierta.
            top = max(y_prev + SEP_TARJETAS, y_ini - PAD_Y - IL[FS_TITULO] / 2.0)
            gap_abierta = top - y_prev
        else:
            # Debajo de la abierta, el mismo aire que encima, para enmarcarla.
            top = y_prev + (gap_abierta if gap_abierta is not None and C["unidades"][k - 1]["abierta"]
                            else SEP_TARJETAS)
        # La tarjeta se registra antes que sus bloques, para dibujarse debajo
        # de ellos; su alto se fija al final.
        caja(clave, x_tarj, top, ANCHO_TARJETA, 0, "datos")
        yy = top + PAD_Y
        texto(u["nombre"], FS_TITULO, True, x_tarj + PAD_X + 1, yy, clave, f"nombre_{k}")
        inventario(f"nombre_{k}", "propio", u["nombre"], [u["nombre"]], "número del punto de la unidad")
        llegada[k] = yy + IL[FS_TITULO] / 2.0
        yy += IL[FS_TITULO]
        if u["abierta"]:
            yy += SEP_GRUPO
            texto(ROTULO_CADENA, FS_TEXTO, False, x_tarj + PAD_X + 1, yy, clave, "rotulo_cadena")
            inventario("rotulo_cadena", "propio", ROTULO_CADENA, [ROTULO_CADENA], "rótulo de la figura")
            yy += IL[FS_TEXTO] + BAJO_ROTULO
            for i, b in enumerate(u["cadena"]):
                if i:
                    yy += SEP_BLOQUES
                cb = f"cadena_{i}"
                h = IL[FS_TEXTO] + 2 * PAD_BY
                caja(cb, x_tarj + PAD_X, yy, w_bloque, h, "cadena", padre=clave)
                s = cortar(b["titulo"], util_bloque, FS_TEXTO, False)
                texto(s, FS_TEXTO, False, x_tarj + PAD_X + PAD_BX + 1, yy + PAD_BY, cb, cb)
                inventario(cb, "literal" if s == b["titulo"] else "cortado", b["titulo"], [s],
                           f"cadena, título del bloque {i + 1} (PDF, página {C['pagina']}, línea {b['pdf']})")
                yy += h
            yy += SEP_GRUPO
            texto(ROTULO_PROPIO, FS_TEXTO, False, x_tarj + PAD_X + 1, yy, clave, "rotulo_propio")
            inventario("rotulo_propio", "propio", ROTULO_PROPIO, [ROTULO_PROPIO], "rótulo de la figura")
            yy += IL[FS_TEXTO] + BAJO_ROTULO
            mostradas = [cortar(s, util_bloque, FS_TEXTO, False) for s in u["texto"][:PRIMERAS_LINEAS]]
            h = len(mostradas) * IL[FS_TEXTO] + 2 * PAD_BY
            caja("propio", x_tarj + PAD_X, yy, w_bloque, h, "propio", padre=clave)
            for j, s in enumerate(mostradas):
                texto(s, FS_TEXTO, False, x_tarj + PAD_X + PAD_BX + 1, yy + PAD_BY + j * IL[FS_TEXTO], "propio",
                      "texto_propio")
            inventario("texto_propio", "primeras", "\n".join(u["texto"]), mostradas,
                       "texto de la unidad, sus primeras líneas")
            yy += h + SEP_GRUPO
            pags = ROTULO_PAGINAS.format(", ".join(str(p) for p in u["paginas"]))
            texto(pags, FS_TEXTO, False, x_tarj + PAD_X + 1, yy, clave, "paginas")
            inventario("paginas", "propio", pags, [pags], "páginas de la unidad")
            yy += IL[FS_TEXTO]
            marcas = ROTULO_MARCAS.format(", ".join(u["marcas"]) if u["marcas"] else SIN_MARCAS)
            texto(marcas, FS_TEXTO, False, x_tarj + PAD_X + 1, yy, clave, "marcas")
            inventario("marcas", "propio", marcas, [marcas], "marcas de la unidad")
            yy += IL[FS_TEXTO]
        cajas[clave]["h"] = float(f(yy + PAD_Y - top))
        y_prev = top + cajas[clave]["h"]

    # ---- flechas: de la llave de cada parte a la tarjeta de su unidad ---- #
    pasillo = x_tarj - x_lomo
    giro = {"arriba": x_lomo + round(pasillo * GIRO_ARRIBA), "abajo": x_lomo + round(pasillo * GIRO_ABAJO)}
    for u in C["unidades"]:
        k = u["indice"]
        (x0, y0), y1 = ini_llave[k], float(f(llegada[k]))
        fin = x_tarj - HUECO_PUNTA
        if y0 == y1:
            puntos = [(x0, y0), (fin, y1)]
        else:
            xg = giro["arriba"] if y1 < y0 else giro["abajo"]
            puntos = [(x0, y0), (xg, y0), (xg, y1), (fin, y1)]
        M["trazos"].append({"nombre": u["nombre"], "unidad": k, "hasta": f"tarjeta_{k}",
                            "puntos": [(float(f(px)), float(f(py))) for px, py in puntos]})

    M["alto"] = math.ceil(max(c["y"] + c["h"] for c in cajas.values()) + MARGEN)
    M["geo"] = {"y_top": y_top, "x_lomo": x_lomo, "giro": giro, "pasillo": pasillo,
                "gap_abierta": gap_abierta}
    return M


# ========================================================================== #
# Elementos derivados y geometría                                            #
# ========================================================================== #
CLASE_ESPERADA = (("hoja", "datos"), ("tarjeta_", "datos"), ("cadena_", "cadena"), ("propio", "propio"))
PALETA = {"datos": {"relleno": NEUTRO["relleno"], "borde": NEUTRO["borde"], "grosor": GROSOR_CAJA, "rx": RX},
          "cadena": {"relleno": GRIS_CADENA, "borde": NEUTRO["borde"], "grosor": GROSOR_BLOQUE, "rx": RX_BLOQUE},
          "propio": {"relleno": BLANCO, "borde": NEUTRO["borde"], "grosor": GROSOR_BLOQUE, "rx": RX_BLOQUE}}


def bb(c: dict) -> tuple:
    return (c["x"], c["y"], c["x"] + c["w"], c["y"] + c["h"])


def grosor_caja(c: dict) -> float:
    return PALETA[c["clase"]]["grosor"]


def ancestros(M: dict, clave: str) -> list[str]:
    out, p = [], M["cajas"][clave]["padre"]
    while p is not None:
        out.append(p)
        p = M["cajas"][p]["padre"]
    return out


def caja_texto(t: dict) -> tuple:
    a = ancho(t["s"], t["fs"], t["negrita"])
    x0 = {"start": t["x"], "middle": t["x"] - a / 2.0, "end": t["x"] - a}[t["ancla"]]
    return (x0, t["y"] - ASC * t["fs"], x0 + a, t["y"] + DESC * t["fs"])


def marcas_de(M: dict) -> list[tuple]:
    """(nombre, caja envolvente, dibujo) de cada marca: el pliegue de la hoja y las llaves."""
    out = []
    H = M["cajas"]["hoja"]
    x, y, w = H["x"], H["y"], H["w"]
    pl = [(x + w - PLIEGUE, y), (x + w - PLIEGUE, y + PLIEGUE), (x + w, y + PLIEGUE)]
    g = GROSOR_CAJA / 2.0
    out.append(("pliegue", (pl[0][0] - g, y - g, x + w + g, y + PLIEGUE + g),
                ("polilinea", pl, NEUTRO["borde"], GROSOR_CAJA)))
    for ll in M["llaves"]:
        xl, y0, y1 = ll["x"], ll["y0"], ll["y1"]
        pts = [(xl - LLAVE_PATA, y0), (xl, y0), (xl, y1), (xl - LLAVE_PATA, y1)]
        g = GROSOR_LLAVE / 2.0
        out.append((ll["nombre"], (xl - LLAVE_PATA - g, y0 - g, xl + g, y1 + g),
                    ("llave", pts, FLECHA, GROSOR_LLAVE)))
    return out


def punta(t: dict) -> tuple:
    """Triángulo de la punta (marcador de 10 × 10, refX 9, a 6 veces el grosor)."""
    (xa, ya), (xb, yb) = t["puntos"][-2], t["puntos"][-1]
    largo = math.hypot(xb - xa, yb - ya)
    ux, uy = (xb - xa) / largo, (yb - ya) / largo
    lp = 6 * GROSOR_FLUJO
    tip = (xb + 0.1 * lp * ux, yb + 0.1 * lp * uy)
    bx, by = xb - 0.9 * lp * ux, yb - 0.9 * lp * uy
    return (tip, (bx - 0.5 * lp * uy, by + 0.5 * lp * ux), (bx + 0.5 * lp * uy, by - 0.5 * lp * ux))


def caja_punta(t: dict) -> tuple:
    p = punta(t)
    return (min(q[0] for q in p), min(q[1] for q in p), max(q[0] for q in p), max(q[1] for q in p))


def tramos(puntos) -> list[tuple]:
    return list(zip(puntos, puntos[1:]))


def tramos_llave(ll: dict) -> list[tuple]:
    xl, y0, y1 = ll["x"], ll["y0"], ll["y1"]
    return tramos([(xl - LLAVE_PATA, y0), (xl, y0), (xl, y1), (xl - LLAVE_PATA, y1)])


def cruza(a, b) -> bool:
    return a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]


def ampliar(b, d) -> tuple:
    return (b[0] - d, b[1] - d, b[2] + d, b[3] + d)


def contiene(c, b, holgura=0.0) -> bool:
    return (c[0] + holgura <= b[0] and b[2] <= c[2] - holgura
            and c[1] + holgura <= b[1] and b[3] <= c[3] - holgura)


def corta(p, q, r) -> bool:
    """True si el segmento pq pasa por el interior abierto del rectángulo r
    (recorte de Liang-Barsky)."""
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
    return min([dist_punto_caja(p, r), dist_punto_caja(q, r)]
               + [dist_punto_segmento(e, p, q) for e in esquinas])


def sobre(p, a, b, tol=1e-6) -> bool:
    return (min(a[0], b[0]) - tol <= p[0] <= max(a[0], b[0]) + tol
            and min(a[1], b[1]) - tol <= p[1] <= max(a[1], b[1]) + tol
            and abs((b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])) <= tol)


def contacto(a0, a1, b0, b1):
    """Punto de contacto entre dos tramos ortogonales, o None: («x», punto)
    si se cruzan en X, («toque», punto) si uno toca al otro con un extremo y
    («superpuestos», punto) si van uno sobre otro."""
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


def direccion(a, b) -> tuple:
    return ((b[0] > a[0]) - (b[0] < a[0]), (b[1] > a[1]) - (b[1] < a[1]))


# ========================================================================== #
# Controles                                                                  #
# ========================================================================== #
def es_corte(dibujado: str, origen: str) -> bool:
    """Un prefijo de `origen` que termina en una palabra entera, seguido de «…»."""
    if not dibujado.endswith("…"):
        return False
    pref = dibujado[:-1]
    return (bool(pref) and pref != origen and origen.startswith(pref) and not pref.endswith(" ")
            and origen[len(pref)] == " ")


def controlar_contenido(M: dict, C: dict) -> dict:
    # clases de las cajas
    for clave, c in M["cajas"].items():
        esperada = next((cl for pref, cl in CLASE_ESPERADA if clave == pref or
                         (pref.endswith("_") and clave.startswith(pref))), None)
        if c["clase"] != esperada:
            freno("contenido", f"la caja «{clave}» es «{c['clase']}» y le corresponde «{esperada}»")
    abiertas = [u for u in C["unidades"] if u["abierta"]]
    cadena = sorted(k for k in M["cajas"] if k.startswith("cadena_"))
    if len(abiertas) != 1 or len(cadena) != len(abiertas[0]["cadena"]):
        freno("contenido", f"{len(cadena)} bloques de cadena dibujados; la unidad abierta tiene "
                           f"{len(abiertas[0]['cadena']) if abiertas else 0}")
    # inventario: cada texto dibujado es de una entrada, y cada entrada se dibuja
    por_inv = {}
    for t in M["textos"]:
        for rx in PROHIBIDOS:
            if rx.search(t["s"]):
                freno("contenido", f"«{t['s']}» lleva {rx.pattern!r}")
        por_inv.setdefault(t["inv"], []).append(t["s"])
    inv = {e["clave"]: e for e in M["inventario"]}
    if sorted(por_inv) != sorted(inv):
        freno("contenido", f"textos sin entrada en el inventario o entradas sin dibujar: "
                           f"{sorted(set(por_inv) ^ set(inv))}")
    modos = {}
    for clave, e in inv.items():
        dib, origen = por_inv[clave], e["origen"]
        if dib != e["lineas"]:
            freno("contenido", f"«{clave}»: dibujado {dib} ≠ inventario {e['lineas']}")
        if e["modo"] in ("literal", "propio"):
            ok = dib == [origen]
        elif e["modo"] == "cortado":
            ok = len(dib) == 1 and es_corte(dib[0], origen)
        elif e["modo"] == "partido":
            ok = len(dib) > 1 and " ".join(dib) == origen and all(d and d == d.strip() for d in dib)
        elif e["modo"] == "primeras":
            fuente = origen.split("\n")
            ok = (len(dib) <= len(fuente)
                  and all(d == s or es_corte(d, s) for d, s in zip(dib, fuente))
                  and all(d == s for d, s in zip(dib[:-1], fuente))
                  and (len(dib) == len(fuente) or dib[-1].endswith("…")))
        else:
            ok = False
        if not ok:
            freno("contenido", f"«{clave}»: {dib} no es {e['modo']} de su fuente {origen[:70]!r}")
        modos[e["modo"]] = modos.get(e["modo"], 0) + 1
    # lo que el inventario dice de cada fuente, contra la fuente
    fuentes = {p["clave"]: p["origen"] for p in C["fragmento"]}
    abierta = abiertas[0]
    fuentes.update({f"cadena_{i}": b["titulo"] for i, b in enumerate(abierta["cadena"])})
    fuentes["texto_propio"] = "\n".join(abierta["texto"])
    fuentes.update({f"nombre_{u['indice']}": u["nombre"] for u in C["unidades"]})
    fuentes["encabezado_documento"] = C["encabezado_documento"]
    fuentes["paginas"] = ROTULO_PAGINAS.format(", ".join(str(p) for p in abierta["paginas"]))
    fuentes["marcas"] = ROTULO_MARCAS.format(", ".join(abierta["marcas"]) if abierta["marcas"] else SIN_MARCAS)
    fuentes.update({"encabezado_unidades": ENCABEZADO_UNIDADES, "rotulo_cadena": ROTULO_CADENA,
                    "rotulo_propio": ROTULO_PROPIO})
    for clave, e in inv.items():
        if fuentes.get(clave) != e["origen"]:
            freno("contenido", f"«{clave}»: el inventario cita {e['origen'][:60]!r}, la fuente dice "
                               f"{str(fuentes.get(clave))[:60]!r}")
    return {"textos": len(M["textos"]), "entradas": len(inv), "modos": modos}


def controlar_trazado(M: dict) -> dict:
    C = M["cajas"]
    llaves = {ll["unidad"]: ll for ll in M["llaves"]}
    n_tramos = 0
    for t in M["trazos"]:
        for p, q in tramos(t["puntos"]):
            n_tramos += 1
            if p == q:
                freno("trazado", f"tramo nulo en «{t['nombre']}» en {p}")
            if p[0] != q[0] and p[1] != q[1]:
                freno("trazado", f"tramo diagonal en «{t['nombre']}»: {p} → {q}")
        for (a, b), (c, d) in zip(tramos(t["puntos"]), tramos(t["puntos"])[1:]):
            if direccion(a, b) == tuple(-v for v in direccion(c, d)):
                freno("trazado", f"«{t['nombre']}» vuelve sobre sí misma en {b}")
        # salida: del lomo de la llave de su parte, a la mitad, hacia afuera
        ll = llaves.get(t["unidad"])
        p0, p1 = t["puntos"][0], t["puntos"][1]
        if ll is None or p0 != (ll["x"], float(f((ll["y0"] + ll["y1"]) / 2.0))) or direccion(p0, p1) != (1, 0):
            freno("trazado", f"«{t['nombre']}» no sale del lomo de la llave de su parte hacia afuera ({p0})")
        # llegada: al borde izquierdo de su tarjeta, lejos de las esquinas
        q0, q1 = t["puntos"][-2], t["puntos"][-1]
        x0, y0, x1, y1 = bb(C[t["hasta"]])
        if not (direccion(q0, q1) == (1, 0) and abs(q1[0] + HUECO_PUNTA - x0) < 1e-6
                and y0 + LEJOS_ESQUINA <= q1[1] <= y1 - LEJOS_ESQUINA):
            freno("trazado", f"«{t['nombre']}» no llega al borde izquierdo de «{t['hasta']}» ({q1})")
    # conexiones: una flecha por unidad, de su parte a su tarjeta
    dibujadas = sorted((t["unidad"], t["hasta"]) for t in M["trazos"])
    fijadas = sorted((k, f"tarjeta_{k}") for k in llaves)
    if dibujadas != fijadas or len(llaves) != len([k for k in C if k.startswith("tarjeta_")]):
        freno("trazado", f"flechas {dibujadas} ≠ una por unidad {fijadas}")
    return {"flechas": len(M["trazos"]), "tramos": n_tramos}


def controlar_cajas(M: dict) -> dict:
    C = M["cajas"]
    claves = list(C)
    minimos = {"separación entre cajas": math.inf, "separación entre bloques": math.inf,
               "aire de un bloque en su tarjeta": math.inf}
    for i in range(len(claves)):
        for j in range(i + 1, len(claves)):
            ka, kb = claves[i], claves[j]
            a, b = bb(C[ka]), bb(C[kb])
            ga, gb = grosor_caja(C[ka]), grosor_caja(C[kb])
            if ka in ancestros(M, kb) or kb in ancestros(M, ka):
                (kp, p, gp), (kh, h, gh) = ((ka, a, ga), (kb, b, gb)) if ka in ancestros(M, kb) else \
                    ((kb, b, gb), (ka, a, ga))
                aire = min(h[0] - p[0], p[2] - h[2], h[1] - p[1], p[3] - h[3]) - (gp + gh) / 2.0
                minimos["aire de un bloque en su tarjeta"] = min(minimos["aire de un bloque en su tarjeta"], aire)
                if aire < AIRE_CONTENIDO:
                    freno("cajas", f"el bloque «{kh}» queda a {aire:.1f} del borde de «{kp}» (< {AIRE_CONTENIDO})")
                continue
            dx = max(b[0] - a[2], 0.0, a[0] - b[2])
            dy = max(b[1] - a[3], 0.0, a[1] - b[3])
            d = math.hypot(dx, dy) - (ga + gb) / 2.0
            hermanos = C[ka]["padre"] is not None and C[ka]["padre"] == C[kb]["padre"]
            exigida = SEP_BLOQUES_MIN if hermanos else SEP_CAJAS
            nombre = "separación entre bloques" if hermanos else "separación entre cajas"
            minimos[nombre] = min(minimos[nombre], d)
            if cruza(a, b) or d < exigida:
                freno("cajas", f"la caja «{ka}» se superpone con «{kb}» o queda a {d:.1f} (< {exigida})")
    for t in M["trazos"]:
        for k, c in C.items():
            interior = ampliar(bb(c), -1.0)
            if any(corta(p, q, interior) for p, q in tramos(t["puntos"])):
                freno("cajas", f"la flecha «{t['nombre']}» atraviesa la caja «{k}»")
            if cruza(caja_punta(t), ampliar(bb(c), -0.5)):
                freno("cajas", f"la punta de «{t['nombre']}» entra en la caja «{k}»")
    for nombre, m, _ in marcas_de(M):
        if nombre == "pliegue":
            continue
        for k, c in C.items():
            if cruza(m, ampliar(bb(c), grosor_caja(c) / 2.0)):
                freno("cajas", f"la {nombre} entra en la caja «{k}»")
    return {"cajas": len(C), "minimos": minimos}


def controlar_cruces(M: dict) -> dict:
    T = M["trazos"]
    cruces, contactos, minimo = [], [], (math.inf, "", "")
    for i in range(len(T)):
        for j in range(i + 1, len(T)):
            a, b = T[i], T[j]
            for p, q in tramos(a["puntos"]):
                for u, v in tramos(b["puntos"]):
                    c = contacto(p, q, u, v)
                    if c is not None:
                        (cruces if c[0] == "x" else contactos).append((a["nombre"], b["nombre"], c[1]))
            d = min(dist_segmentos(p, q, u, v) for p, q in tramos(a["puntos"]) for u, v in tramos(b["puntos"]))
            d -= GROSOR_FLUJO
            if d < minimo[0]:
                minimo = (d, a["nombre"], b["nombre"])
    if cruces or contactos:
        def fmt(x):
            return "; ".join(f"«{n1}» × «{n2}» en ({p[0]:g}, {p[1]:g})" for n1, n2, p in x)
        partes = []
        if cruces:
            partes.append(f"{len(cruces)} cruce(s) entre flechas: {fmt(cruces)}")
        if contactos:
            partes.append(f"{len(contactos)} contacto(s) entre flechas: {fmt(contactos)}")
        freno("cruces", " | ".join(partes))
    if minimo[0] < DISTANCIA_MIN:
        freno("cruces", f"«{minimo[1]}» pasa a {minimo[0]:.1f} de «{minimo[2]}» (< {DISTANCIA_MIN})")
    for t in T:
        for o in T:
            if o is t:
                continue
            for p, q in tramos(o["puntos"]):
                if dist_segmento_caja(p, q, caja_punta(t)) - GROSOR_FLUJO / 2.0 < HOLGURA_TEXTO:
                    freno("cruces", f"la punta de «{t['nombre']}» toca la flecha «{o['nombre']}»")
    minimo_llave = (math.inf, "", "")
    for t in T:
        for ll in M["llaves"]:
            if ll["unidad"] == t["unidad"]:
                continue
            d = min(dist_segmentos(p, q, u, v) for p, q in tramos(t["puntos"]) for u, v in tramos_llave(ll))
            d -= (GROSOR_FLUJO + GROSOR_LLAVE) / 2.0
            if d < minimo_llave[0]:
                minimo_llave = (d, t["nombre"], ll["nombre"])
            if d < DISTANCIA_MIN:
                freno("cruces", f"la flecha «{t['nombre']}» pasa a {d:.1f} de la {ll['nombre']} (< {DISTANCIA_MIN})")
    return {"cruces": len(cruces), "contactos": len(contactos), "distancia_minima": minimo,
            "distancia_llave": minimo_llave}


def controlar_textos(M: dict) -> dict:
    C = M["cajas"]
    textos = [(t, caja_texto(t)) for t in M["textos"]]
    marcas = marcas_de(M)
    minimos = {"texto-texto": math.inf, "texto-trazo": math.inf, "texto-marca": math.inf,
               "texto-borde de su caja": math.inf}
    tamanos = {}
    for t, r in textos:
        pt = puntos_impresos(t["fs"])
        tamanos[t["fs"]] = pt
        if pt < PT_MINIMO:
            freno("textos", f"«{t['s']}»: letra de {pt:.2f} pt (< {PT_MINIMO})")
        if r[0] < 0 or r[1] < 0 or r[2] > W or r[3] > M["alto"]:
            freno("textos", f"«{t['s']}» sale del lienzo")
        propias = set()
        if t["dentro"] is not None:
            c = C[t["dentro"]]
            g = grosor_caja(c)
            cb = bb(c)
            holg = min(r[0] - cb[0], cb[2] - r[2], r[1] - cb[1], cb[3] - r[3])
            minimos["texto-borde de su caja"] = min(minimos["texto-borde de su caja"], holg)
            if holg < g / 2.0 + HOLGURA_TEXTO:
                freno("textos", f"«{t['s']}» a {holg:.1f} del borde de su caja «{t['dentro']}»")
            propias = {t["dentro"], *ancestros(M, t["dentro"])}
        for k, c in C.items():
            if k not in propias and cruza(r, ampliar(bb(c), grosor_caja(c) / 2.0 + HOLGURA_TEXTO)):
                freno("textos", f"«{t['s']}» se superpone con la caja «{k}»")
        for nombre, m, _ in marcas:
            dx = max(m[0] - r[2], 0.0, r[0] - m[2])
            dy = max(m[1] - r[3], 0.0, r[1] - m[3])
            minimos["texto-marca"] = min(minimos["texto-marca"], math.hypot(dx, dy))
            if cruza(ampliar(r, HOLGURA_TEXTO), m):
                freno("textos", f"«{t['s']}» toca la marca «{nombre}»")
        for tr in M["trazos"]:
            d = min(dist_segmento_caja(p, q, r) for p, q in tramos(tr["puntos"])) - GROSOR_FLUJO / 2.0
            minimos["texto-trazo"] = min(minimos["texto-trazo"], d)
            if d < HOLGURA_TEXTO:
                freno("textos", f"«{t['s']}» toca la flecha «{tr['nombre']}»")
            if cruza(ampliar(r, HOLGURA_TEXTO), caja_punta(tr)):
                freno("textos", f"«{t['s']}» toca la punta de «{tr['nombre']}»")
    for i in range(len(textos)):
        for j in range(i + 1, len(textos)):
            (ta, a), (tb, b) = textos[i], textos[j]
            if cruza(a, b):
                freno("textos", f"«{ta['s']}» se superpone con «{tb['s']}»")
            dx = max(b[0] - a[2], 0.0, a[0] - b[2])
            dy = max(b[1] - a[3], 0.0, a[1] - b[3])
            minimos["texto-texto"] = min(minimos["texto-texto"], math.hypot(dx, dy))
    return {"textos": len(textos), "tamanos": tamanos, "minimos": minimos, "cajas_texto": textos}


def controlar_margen(M: dict, textos) -> dict:
    todas = [(f"texto «{t['s']}»", r) for t, r in textos]
    todas += [(f"caja «{k}»", ampliar(bb(c), grosor_caja(c) / 2.0)) for k, c in M["cajas"].items()]
    todas += [(f"marca «{n}»", m) for n, m, _ in marcas_de(M)]
    g = GROSOR_FLUJO / 2.0
    for t in M["trazos"]:
        xs, ys = [p[0] for p in t["puntos"]], [p[1] for p in t["puntos"]]
        todas.append((f"flecha «{t['nombre']}»", (min(xs) - g, min(ys) - g, max(xs) + g, max(ys) + g)))
        todas.append((f"punta de «{t['nombre']}»", caja_punta(t)))
    distancia = {"izquierdo": lambda r: r[0], "superior": lambda r: r[1],
                 "derecho": lambda r: W - r[2], "inferior": lambda r: M["alto"] - r[3]}
    minimos = {}
    for borde, d in distancia.items():
        minimos[borde] = min(d(r) for _, r in todas)
        for nombre, r in todas:
            if d(r) < MARGEN_MIN:
                freno("margen", f"{nombre} a {d(r):.1f} unidades del borde {borde} (< {MARGEN_MIN:.1f})")
    return {"elementos": len(todas), "minimos": minimos}


def verificar(M: dict, C: dict) -> dict:
    rep = {"contenido": controlar_contenido(M, C), "trazado": controlar_trazado(M),
           "cajas": controlar_cajas(M), "cruces": controlar_cruces(M)}
    rep["textos"] = controlar_textos(M)
    rep["margen"] = controlar_margen(M, rep["textos"]["cajas_texto"])
    svg, dibujados = dibujar(M)
    rep["registro"] = controlar_registro(svg, dibujados, M)
    rep["svg"] = svg
    return rep


# ========================================================================== #
# Emisión del SVG                                                            #
# ========================================================================== #
def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def path_redondeado(puntos) -> str:
    """Poligonal con esquinas redondeadas de radio RADIO (la técnica del proceso)."""
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


def dibujar(M: dict) -> tuple[str, list]:
    partes, dib = [], []

    def add(etiqueta, s):
        partes.append(s)
        dib.append(etiqueta)

    for clave, c in M["cajas"].items():
        pal = PALETA[c["clase"]]
        relleno = c.get("relleno_forzado", pal["relleno"])
        x, y, w, h = c["x"], c["y"], c["w"], c["h"]
        if c["forma"] == "hoja":
            p = PLIEGUE
            add(("caja", clave),
                f'<path data-caja="{clave}" d="M{f(x + 4)},{f(y)} L{f(x + w - p)},{f(y)} '
                f'L{f(x + w)},{f(y + p)} L{f(x + w)},{f(y + h - 4)} '
                f'Q{f(x + w)},{f(y + h)} {f(x + w - 4)},{f(y + h)} '
                f'L{f(x + 4)},{f(y + h)} Q{f(x)},{f(y + h)} {f(x)},{f(y + h - 4)} '
                f'L{f(x)},{f(y + 4)} Q{f(x)},{f(y)} {f(x + 4)},{f(y)} Z" '
                f'fill="{relleno}" stroke="{pal["borde"]}" stroke-width="{pal["grosor"]}"/>')
        else:
            add(("caja", clave),
                f'<rect data-caja="{clave}" x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" '
                f'fill="{relleno}" stroke="{pal["borde"]}" stroke-width="{pal["grosor"]}" rx="{pal["rx"]}"/>')
    for nombre, _, (tipo, geo, color, g) in marcas_de(M):
        d = " ".join(("M" if i == 0 else "L") + f"{f(px)},{f(py)}" for i, (px, py) in enumerate(geo))
        add(("marca", nombre), f'<path data-marca="{esc(nombre)}" d="{d}" fill="none" stroke="{color}" '
                               f'stroke-width="{g}"/>')
    for t in M["trazos"]:
        add(("flecha", t["nombre"]),
            f'<path data-flecha="{esc(t["nombre"])}" d="{path_redondeado(t["puntos"])}" fill="none" '
            f'stroke="{FLECHA}" stroke-width="{GROSOR_FLUJO}" marker-end="url(#arN)"/>')
    for t in M["textos"]:
        anc = "" if t["ancla"] == "start" else f' text-anchor="{t["ancla"]}"'
        peso = "bold" if t["negrita"] else "normal"
        add(("texto", t["s"]),
            f'<text x="{f(t["x"])}" y="{f(t["y"])}"{anc} font-size="{t["fs"]}" font-weight="{peso}" '
            f'fill="{t["color"]}">{esc(t["s"])}</text>')
    alto = M["alto"]
    alto_cm = ANCHO_CM * alto / W
    cabeza = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{ANCHO_CM:.2f}cm" height="{alto_cm:.2f}cm" '
        f'viewBox="0 0 {W} {alto}" font-family="{TIPOGRAFIA}">',
        f'<rect width="{W}" height="{alto}" fill="{BLANCO}"/>',
        f'<defs><marker id="arN" {MARCADOR} fill="{FLECHA}"/></marker></defs>',
    ]
    return "\n".join(cabeza + partes + ["</svg>"]) + "\n", dib


def controlar_registro(svg: str, dibujados: list, M: dict) -> dict:
    """El SVG se relee: cada elemento está registrado, en orden, y cada caja,
    marca, flecha y texto tiene el color de su clase; el gris de la cadena
    solo está en los bloques de la cadena."""
    ns = "{http://www.w3.org/2000/svg}"
    raiz = ET.fromstring(svg)
    hijos = list(raiz)
    tags = [el.tag.replace(ns, "") for el in hijos]
    esperado = {"caja": None, "marca": "path", "flecha": "path", "texto": "text"}
    if tags[:2] != ["rect", "defs"]:
        freno("registro", f"el SVG no empieza con el fondo y las definiciones: {tags[:2]}")
    if len(tags) - 2 != len(dibujados):
        freno("registro", f"{len(tags) - 2} elementos en el SVG y {len(dibujados)} registrados")
    for el, tag, (tipo, nombre) in zip(hijos[2:], tags[2:], dibujados):
        if esperado[tipo] and tag != esperado[tipo]:
            freno("registro", f"{tipo} «{nombre}» emitido como <{tag}>")
        if tag == "text" and el.text != nombre:
            freno("registro", f"texto «{nombre}» emitido como «{el.text}»")
    # Orden de pintado: una caja se emite después de la caja que la contiene;
    # si no, la de afuera la tapa.
    orden = [el.get("data-caja") for el in hijos[2:] if el.get("data-caja") is not None]
    for clave in orden:
        for p in ancestros(M, clave):
            if orden.index(p) > orden.index(clave):
                freno("registro", f"el bloque «{clave}» se emite antes que «{p}», que lo contiene y lo tapa")
    colores = {"cajas": 0, "marcas": 0, "flechas": 0, "textos": 0}
    textos = iter(M["textos"])
    for el in hijos[2:]:
        clave = el.get("data-caja")
        if clave is not None:
            c = M["cajas"][clave]
            pal = PALETA[c["clase"]]
            if (el.get("fill"), el.get("stroke"), el.get("stroke-width")) != \
                    (pal["relleno"], pal["borde"], str(pal["grosor"])):
                freno("registro", f"«{clave}» con relleno {el.get('fill')}, borde {el.get('stroke')} y grosor "
                                  f"{el.get('stroke-width')}, no los de «{c['clase']}»")
            colores["cajas"] += 1
        if el.get("data-marca") is not None:
            nombre = el.get("data-marca")
            color, g = (NEUTRO["borde"], GROSOR_CAJA) if nombre == "pliegue" else (FLECHA, GROSOR_LLAVE)
            if (el.get("stroke"), el.get("stroke-width"), el.get("fill")) != (color, str(g), "none"):
                freno("registro", f"la marca «{nombre}» no tiene el trazo de su clase")
            colores["marcas"] += 1
        if el.get("data-flecha") is not None:
            if (el.get("stroke"), el.get("stroke-width"), el.get("marker-end")) != \
                    (FLECHA, str(GROSOR_FLUJO), "url(#arN)"):
                freno("registro", f"la flecha «{el.get('data-flecha')}» no tiene el trazo de la línea principal")
            colores["flechas"] += 1
        if el.tag.replace(ns, "") == "text":
            t = next(textos)
            color = TINTA if t["negrita"] else TINTA_SUB
            if (el.get("fill"), el.get("font-weight")) != (color, "bold" if t["negrita"] else "normal"):
                freno("registro", f"«{t['s']}» con color {el.get('fill')}, no {color}")
            colores["textos"] += 1
    usados = {v for el in raiz.iter() for a in ("fill", "stroke") for v in [el.get(a)] if v and v != "none"}
    permitidos = {NEUTRO["relleno"], NEUTRO["borde"], TINTA, TINTA_SUB, FLECHA, BLANCO, GRIS_CADENA}
    if usados - permitidos:
        freno("registro", f"colores fuera de la paleta: {sorted(usados - permitidos)}")
    con_gris = sorted(el.get("data-caja") or el.tag for el in raiz.iter() if GRIS_CADENA in (el.get("fill"),
                                                                                             el.get("stroke")))
    if con_gris != sorted(k for k, c in M["cajas"].items() if c["clase"] == "cadena"):
        freno("registro", f"el gris de la cadena está en {con_gris}")
    if colores["cajas"] != len(M["cajas"]) or colores["flechas"] != len(M["trazos"]):
        freno("registro", f"cajas o flechas sin color controlado: {colores}")
    return {"elementos": len(dibujados), "colores": colores, "paleta": sorted(usados)}


# ========================================================================== #
# Exportación                                                                #
# ========================================================================== #
def grabar_densidad(ruta: str, dpi: int) -> None:
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


def png_dimensiones(ruta: str) -> tuple[int, int]:
    with open(ruta, "rb") as fh:
        cab = fh.read(24)
    return struct.unpack(">II", cab[16:24])


def pdf_mediabox(ruta: str) -> tuple[float, float]:
    """MediaBox de la página, buscada en claro y en los flujos comprimidos."""
    with open(ruta, "rb") as fh:
        datos = fh.read()
    textos = [datos]
    for m in re.finditer(rb"stream\r?\n", datos):
        fin = datos.find(b"endstream", m.end())
        try:
            textos.append(zlib.decompress(datos[m.end():fin]))
        except zlib.error:
            pass
    for t in textos:
        m = re.search(rb"/MediaBox\s*\[\s*([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s*\]", t)
        if m:
            x0, y0, x1, y1 = (float(v) for v in m.groups())
            return (x1 - x0, y1 - y0)
    freno("exportacion", "el PDF no declara su MediaBox")


def exportar(ruta_svg: str, ruta_png: str, ruta_pdf: str) -> None:
    rsvg = shutil.which("rsvg-convert")
    if not rsvg:
        freno("exportacion", "rsvg-convert no está instalado: no se escriben el PNG ni el PDF")
    subprocess.run([rsvg, "-w", str(ANCHO_PNG_PX), "-f", "png", "-o", ruta_png, ruta_svg], check=True)
    grabar_densidad(ruta_png, DPI)
    entorno = dict(os.environ, SOURCE_DATE_EPOCH=SOURCE_DATE_EPOCH)
    subprocess.run([rsvg, "-f", "pdf", "-o", ruta_pdf, ruta_svg], check=True, env=entorno)


# ========================================================================== #
# Pruebas negativas                                                          #
# ========================================================================== #
def _texto(M, inv, j=0):
    return [t for t in M["textos"] if t["inv"] == inv][j]


def _mut_texto_alterado(M):
    """El título del bloque del 5.1 dibujado con el principio de su párrafo."""
    t = _texto(M, "cadena_1")
    t["s"] = t["s"] + " La cartera"


def _mut_corte_en_media_palabra(M):
    """La primera línea del 5.1.1.2 cortada en la mitad de una palabra (texto e inventario)."""
    e = next(e for e in M["inventario"] if e["clave"] == "parte_2")
    s = e["origen"][:e["origen"].index(" entidad") + 5] + "…"
    e["lineas"], e["modo"] = [s], "cortado"
    _texto(M, "parte_2")["s"] = s


def _mut_identificador(M):
    """La tarjeta del 5.1.1.2 nombrada con el identificador interno de la unidad."""
    t = _texto(M, "nombre_2")
    t["s"] = "cla::" + t["s"]


def _mut_tramo_diagonal(M):
    """La flecha del 5.1.1.1 llega 10 unidades más abajo de donde sale."""
    t = next(t for t in M["trazos"] if t["unidad"] == 1)
    t["puntos"][-1] = (t["puntos"][-1][0], t["puntos"][-1][1] + 10)


def _mut_tarjetas_superpuestas(M):
    """La tarjeta abierta, 30 unidades más alta: tapa la del 5.1.1.2."""
    M["cajas"]["tarjeta_1"]["h"] += 30


def _mut_cruce_entre_flechas(M):
    """La flecha del 5.1.1.2 sube por encima de la del 5.1.1.1 y vuelve a bajar: la cruza dos veces."""
    t = next(t for t in M["trazos"] if t["unidad"] == 2)
    b = next(t for t in M["trazos"] if t["unidad"] == 1)
    (x0, y0), (x3, y3) = t["puntos"][0], t["puntos"][-1]
    g = M["geo"]
    y_arriba = b["puntos"][0][1] - 12
    t["puntos"] = [(x0, y0), (g["giro"]["arriba"], y0), (g["giro"]["arriba"], y_arriba),
                   (g["giro"]["abajo"], y_arriba), (g["giro"]["abajo"], y3), (x3, y3)]


def _mut_letra_chica(M):
    """El rótulo de las marcas a 11 unidades: 6,15 pt impresos."""
    _texto(M, "marcas")["fs"] = 11


def _mut_texto_fuera_de_su_caja(M):
    """El rótulo de las marcas, 12 unidades más abajo: sale de su tarjeta."""
    _texto(M, "marcas")["y"] += 12


def _mut_margen(M):
    """El encabezado de las unidades, 5 unidades más arriba: queda a menos de 2 mm del borde."""
    _texto(M, "encabezado_unidades")["y"] -= 5


def _mut_color(M):
    """El primer bloque de la cadena, con el relleno de las tarjetas en lugar del gris."""
    M["cajas"]["cadena_0"]["relleno_forzado"] = NEUTRO["relleno"]


def _mut_bloque_tapado(M):
    """La tarjeta abierta se emite después de sus bloques: los tapa."""
    M["cajas"]["tarjeta_1"] = M["cajas"].pop("tarjeta_1")


# mutación → (función, control que tiene que frenar, textos que el freno tiene que nombrar)
MUTACIONES = {
    "texto_alterado": (_mut_texto_alterado, "contenido", ("«cadena_1»", "dibujado")),
    "corte_en_media_palabra": (_mut_corte_en_media_palabra, "contenido", ("«parte_2»", "no es cortado")),
    "identificador": (_mut_identificador, "contenido", ("«cla::5.1.1.2» lleva",)),
    "tramo_diagonal": (_mut_tramo_diagonal, "trazado", ("tramo diagonal en «5.1.1.1»",)),
    "tarjetas_superpuestas": (_mut_tarjetas_superpuestas, "cajas",
                              ("la caja «tarjeta_1» se superpone con «tarjeta_2»",)),
    "cruce_entre_flechas": (_mut_cruce_entre_flechas, "cruces",
                            ("2 cruce(s) entre flechas", "«5.1.1.1» × «5.1.1.2»")),
    "letra_chica": (_mut_letra_chica, "textos", ("«Marcas: ninguna»: letra de 6.15 pt",)),
    "texto_fuera_de_su_caja": (_mut_texto_fuera_de_su_caja, "textos",
                               ("«Marcas: ninguna» a", "del borde de su caja «tarjeta_1»")),
    "margen": (_mut_margen, "margen", ("texto «Unidades de extracción»", "del borde superior")),
    "color": (_mut_color, "registro", ("«cadena_0» con relleno #fafafa",)),
    "bloque_tapado": (_mut_bloque_tapado, "registro",
                      ("el bloque «cadena_0» se emite antes que «tarjeta_1», que lo contiene y lo tapa",)),
}


def _fuente_candado(D):
    """Un byte más en el PDF: el candado tiene que frenar."""
    candado("pdf", D["pdf_crudo"] + b"\n")


def _fuente_estilo(D):
    """La figura usa letra de 12 para el texto: no es la del proceso."""
    texto = leer_crudo("estilo").decode("utf-8")
    estilo = dict(ESTILO)
    patron, conv, _ = estilo["FS_TITULO, FS_TEXTO"]
    estilo["FS_TITULO, FS_TEXTO"] = (patron, conv, (FS_TITULO, 12))
    cotejar_estilo(texto, estilo)


def _fuente_texto_unidad(D):
    """La primera línea del 5.1.1.1 en la segmentación, con una palabra cambiada: ya no es una línea del PDF."""
    D2 = copy.deepcopy(D)
    u = next(u for u in D2["unidades"] if u["unidad"] == ABIERTA)
    u["texto"] = u["texto"].replace("consumo o vivienda", "consumo y vivienda", 1)
    derivar(D2)


def _fuente_seis_subpuntos(D):
    """El 5.1.1 con seis subpuntos: la figura tendría que resumirlos y frena."""
    D2 = copy.deepcopy(D)
    nodo = buscar_camino(D2["estructura"], PUNTO)[-1]
    nodo["hijos"] = nodo["hijos"] + [dict(nodo["hijos"][-1], numero=f"{PUNTO}.{k}") for k in range(3, 7)]
    derivar(D2)


PRUEBAS_FUENTE = {
    "candado_del_pdf": (_fuente_candado, "fuentes", ("TO_clasificacion_deudores_actual.pdf no es el verificado",)),
    "estilo_distinto": (_fuente_estilo, "estilo", ("FS_TITULO, FS_TEXTO: la figura usa (14, 12)",)),
    "texto_de_la_unidad": (_fuente_texto_unidad, "contenido",
                           ("el texto de la unidad 5.1.1.1: 0 apariciones en la página",)),
    "seis_subpuntos": (_fuente_seis_subpuntos, "contenido", ("tiene 6 subpuntos (más de 5)",)),
}


def probar(nombre: str, accion, control: str, esperado: tuple) -> str:
    try:
        accion()
    except Freno as e:
        msg = str(e)
        if not msg.startswith(f"[{control}]") or not all(x in msg for x in esperado):
            freno("pruebas", f"la prueba {nombre} frenó en otro control o con otro motivo: {msg}")
        return msg
    freno("pruebas", f"la prueba {nombre} no frenó")


def pruebas_negativas(M: dict, C: dict, D: dict) -> dict:
    out = {}
    for nombre, (fn, control, esperado) in PRUEBAS_FUENTE.items():
        out[nombre] = probar(nombre, lambda fn=fn: fn(D), control, esperado)
    for nombre, (fn, control, esperado) in MUTACIONES.items():
        def accion(fn=fn):
            M2 = copy.deepcopy(M)
            fn(M2)
            verificar(M2, C)
        out[nombre] = probar(nombre, accion, control, esperado)
    return out


# ========================================================================== #
# Principal                                                                  #
# ========================================================================== #
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--salida", default=AQUI,
                    help="directorio del SVG, el PNG y el PDF (por omisión, el del script)")
    ap.add_argument("--mutacion", choices=sorted(MUTACIONES),
                    help="inyecta un defecto: el generador tiene que frenar sin escribir nada")
    args = ap.parse_args()
    try:
        D = leer_fuentes()
        AFM.update(D["afm"])
        C = derivar(D)
        M = armar_modelo(C)
        base = copy.deepcopy(M)
        if args.mutacion:
            MUTACIONES[args.mutacion][0](M)
            verificar(M, C)
            print(f"ERROR: la mutación {args.mutacion} no frenó")
            return 2
        rep = verificar(M, C)
        negativas = pruebas_negativas(base, C, D)
    except Freno as e:
        print(f"FRENO {e}")
        print("No se escribe nada.")
        return 1

    print("FUENTES (sha256 comprobado):")
    for clave, (rel, sha) in FUENTES.items():
        print(f"  {clave:10s} {rel}  {sha}")
    print("ESTILO (cada valor que usa la figura, contra la línea que lo declara):")
    for k, v in D["lugares"].items():
        print(f"  {k:34s} {v}")
    print(f"  tabla AFM                          {FUENTES['estilo'][0]} ({D['lugar_afm']}), "
          f"más «…» = 1000")
    print(f"CONTENIDO DERIVADO (página {C['pagina']} del PDF; líneas de extract_text_lines, desde 1):")
    lin = C["lineas_pagina"]
    for p in C["fragmento"]:
        print(f"  fragmento, {p['clave']:8s} línea {p['pdf']:2d}: {lin[p['pdf'] - 1]!r}")
    for u in C["unidades"]:
        cad = ""
        if u["abierta"]:
            cad = "; cadena: " + " | ".join(f"{b['titulo']} ({'+'.join(b['tramos'])}, línea {b['pdf']})"
                                            for b in u["cadena"])
        print(f"  unidad «{u['nombre']}»: páginas {u['paginas']}; marcas {u['marcas'] or SIN_MARCAS}{cad}")
    print("ANCLAS:")
    for que, donde in C["anclas"]:
        print(f"  {que}: {donde}")
    c = rep["contenido"]
    print(f"CONTENIDO: {c['textos']} textos en {c['entradas']} entradas del inventario, por modo "
          + ", ".join(f"{k} {v}" for k, v in sorted(c["modos"].items()))
          + "; ninguno con identificadores, archivos ni campos del código")
    print("INVENTARIO (entrada, modo, lo dibujado, la fuente):")
    for e in M["inventario"]:
        print(f"  {e['clave']:22s} {e['modo']:8s} {' / '.join(e['lineas'])}  [{e['fuente']}]")
    t = rep["trazado"]
    print(f"TRAZADO: {t['flechas']} flechas, {t['tramos']} tramos, 0 diagonales; cada una sale del lomo de la "
          f"llave de su parte y llega al borde de la tarjeta de su unidad")
    k = rep["cajas"]
    print(f"CAJAS: {k['cajas']}, sin superposiciones; mínimos: "
          + "; ".join(f"{a} {b:.1f}" for a, b in k["minimos"].items())
          + "; ningún trazo, punta ni llave entra en una caja")
    x = rep["cruces"]
    d, dl = x["distancia_minima"], x["distancia_llave"]
    print(f"CRUCES entre flechas: {x['cruces']}; contactos: {x['contactos']}; distancia mínima entre flechas "
          f"{d[0]:.1f} («{d[1]}» / «{d[2]}»), de una flecha a una llave ajena {dl[0]:.1f} "
          f"(«{dl[1]}» / {dl[2]}), exigida {DISTANCIA_MIN}")
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
    print(f"REGISTRO: {rg['elementos']} elementos del SVG, todos registrados; colores controlados en "
          f"{rg['colores']['cajas']} cajas, {rg['colores']['marcas']} marcas, {rg['colores']['flechas']} flechas "
          f"y {rg['colores']['textos']} textos; colores del SVG: {', '.join(rg['paleta'])}")
    print(f"PRUEBAS NEGATIVAS ({len(negativas)}; cada una frena en su control):")
    for n, msg in negativas.items():
        print(f"  {n:24s} {msg}")
    g = M["geo"]
    print(f"COMPOSICIÓN: lomo de las llaves x={f(g['x_lomo'])}; pasillo {f(g['pasillo'])}; giros x="
          f"{g['giro']['arriba']} (hacia arriba) y x={g['giro']['abajo']} (hacia abajo); aire encima y debajo de "
          f"la tarjeta abierta {f(g['gap_abierta'])}")

    os.makedirs(args.salida, exist_ok=True)
    rutas = {ext: os.path.join(args.salida, f"{NOMBRE}.{ext}") for ext in ("svg", "png", "pdf")}
    with open(rutas["svg"], "w", encoding="utf-8", newline="\n") as fh:
        fh.write(rep["svg"])
    try:
        exportar(rutas["svg"], rutas["png"], rutas["pdf"])
        mb = pdf_mediabox(rutas["pdf"])
    except Freno as e:
        print(f"FRENO {e}")
        return 1
    wpx, hpx = png_dimensiones(rutas["png"])
    alto = M["alto"]
    print(f"TAMAÑO: lienzo {W} × {alto}; impreso {ANCHO_CM:.2f} × {ANCHO_CM * alto / W:.2f} cm; "
          f"PNG {wpx} × {hpx} px a {DPI} dpi; PDF {mb[0]:.2f} × {mb[1]:.2f} pt "
          f"({mb[0] / PT_POR_CM:.2f} × {mb[1] / PT_POR_CM:.2f} cm)")
    for ext in ("svg", "png", "pdf"):
        print(f"{ext.upper()}: {os.path.basename(rutas[ext])}  sha256 {sha256(rutas[ext])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
