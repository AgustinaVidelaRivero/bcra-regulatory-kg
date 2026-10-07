#!/usr/bin/env python3
"""Figura «anatomía de una tripleta» para el capítulo 2 (Figura 2.1), versión 2.

Una sola tripleta real del grafo de la tanda 0 con el perfil r2b, del ejemplo
del préstamo: la Condicion del monto del punto 5.1.1.1 del Texto Ordenado de
Clasificación de deudores —condicion_de→ la Operacion de la inclusión en la
cartera comercial, del mismo punto. Cada nodo con el formato de la figura 1.1
versión 2: primera línea en negrita con el tipo, escrito como en el código, y
el punto («Condicion · punto 5.1.1.1»), y debajo la etiqueta del grafo,
completa; la arista con el nombre de la relación tal como está en el grafo;
tres llamadas en gris que nombran las partes de la tripleta: «nodo de origen»
y «nodo de destino», centradas sobre su caja, y «relación · nombre y
dirección», debajo de la arista. Sin leyenda.

Versión 1 (28/09/2026; generador en fbe69d4): sobre KG-Reextraído-r1 (sha256
0226e947…), la Restriccion del monto —limita→ la Operacion; nodos con la
etiqueta y debajo «punto N», relleno del color de su tipo y texto blanco; el
tipo y el punto, en las llamadas de los nodos.
Versión 2: la tripleta y el grafo de arriba; el formato de los nodos, los
colores de tipo (relleno, borde y grosor) y el texto oscuro, los de la figura
1.1 versión 2; las llamadas de los nodos, sin el tipo ni el punto, que pasan a
la caja. El resto del trazado de la versión 1 no cambia: lienzo de 720
unidades impreso a 12,75 cm, dos nodos de 260 unidades en una fila, las
llamadas de los nodos arriba y la de la relación abajo, la arista en trazo
continuo gris oscuro con su rótulo en negrita encima, y los mismos tamaños de
letra.

Fuentes, con candado de sha256 (el script frena si alguna no es la verificada):
- GRAFO: el grafo de desarrollo r2b, del que se dibuja;
- GRAFO_DIEZ: el grafo de diez documentos r2b, en el que se comprueba que lo
  dibujado está igual;
- ESTILO: figura_esquema_final.svg, de donde salen los colores de tipo (los
  mismos que lee la figura 1.1);
- MODELOS_R2: modelos_r2.py, donde se comprueba la firma de la arista en la
  matriz del esquema r2 y que la relación no es un predicado derivado;
- FIGURA_1_1: figura_norma_a_grafo.svg versión 2, contra cuyos nodos se
  comparan el tipo, el punto, la etiqueta y los colores de los dos nodos.
Los tres primeros candados son los de generar_figura_norma_a_grafo.py, del que
se importan la carga del subgrafo (cargar_subgrafo, comparar_grafos), los
colores de tipo (leer_colores_tipo), los controles de geometría y la
exportación.

Controles, en cada corrida (el script frena si alguno falla):
- grafo: cada nodo, con su tipo y su etiqueta, una sola vez y con su punto
  como única procedencia punto_propio; la arista, una sola vez; entre los dos
  nodos el grafo no tiene otras aristas; los nodos de la unidad que no se
  dibujan son los declarados en NO_DIBUJADOS; todo igual en los dos grafos; la
  arista sin rol_fuente ni propiedades, con su firma en la matriz del esquema
  r2 y su relación fuera de los predicados derivados;
- figura 1.1: los dos nodos están en figura_norma_a_grafo.svg con el mismo
  tipo, punto, etiqueta, relleno, borde y grosor;
- inventario: el SVG se relee y, solo desde su geometría y sus textos, se
  rearma la tripleta (tipo, punto y etiqueta de cada caja, la caja a la que
  apunta cada llamada, rótulo de la arista, caja donde empieza y caja donde
  termina con la flecha) y los colores de cada caja; tienen que ser los del
  grafo y los del tipo;
- geometría (controlar_geometria de la figura 1.1, más las líneas de llamada):
  medidas con las métricas reales de Helvetica, ningún texto superpuesto con
  otro, sobre una caja que no lo contiene, sobre un trazo que no es el suyo ni
  fuera del lienzo; ningún trazo que toque una caja; 0 cruces entre trazos;
  letra impresa de 7 pt o más.
Antes de componer la figura corren seis pruebas negativas (dirección
invertida, llamadas de los nodos intercambiadas, etiqueta cambiada, tipo
cambiado, rótulo sobre una caja y una línea de llamada que cruza la arista);
cada una tiene que hacer fallar su control.
Con --perturbar <caso> se compone la figura con ese defecto: los controles
fallan y no se escribe nada.

Salidas, byte-reproducibles: figura_tripleta.svg, .png (300 dpi, densidad
grabada) y .pdf (fecha de creación fijada con SOURCE_DATE_EPOCH=0).

Uso (desde la raíz del repo):
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_tripleta.py
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_tripleta.py --salida DIR
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_tripleta.py \\
        --perturbar {direccion_invertida,llamadas_intercambiadas,etiqueta_distinta,tipo_cambiado,
                     rotulo_sobre_caja,cruce}
"""

import sys

sys.dont_write_bytecode = True  # importar los módulos hermanos no deja __pycache__

import argparse  # noqa: E402
import ast  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import xml.etree.ElementTree as ET  # noqa: E402
from collections import Counter  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import generar_figura_norma_a_grafo as base  # noqa: E402

NOMBRE = "figura_tripleta"
NS = base.NS
freno = base.freno
f, esc = base.f, base.esc

# --------------------------------------------------------------------------- #
# Fuentes y candados                                                           #
# --------------------------------------------------------------------------- #
# Los dos grafos r2b y la figura del esquema final: los candados de la figura
# 1.1 (generar_figura_norma_a_grafo.py, GRAFO, GRAFO_DIEZ y ESTILO).
GRAFO = base.GRAFO
GRAFO_DIEZ = base.GRAFO_DIEZ
ESTILO = base.ESTILO
# Esquema r2: matriz de firmas y predicados derivados por código (igual en
# bbc38dc, el commit de los dos grafos).
MODELOS_R2 = ("data/experiment/pyd_r2/code/modelos_r2.py",
              "e67f15ae13dd5419ea0ce1a08dbef63c86cbdf9c269772a0b02a4e27b4c3a2ca")
# Figura 1.1 versión 2 (FIG-INTRO-R2B, 88bfe89): sus nodos fijan el tipo, el
# punto, la etiqueta y los colores con que se dibujan los dos de esta figura.
FIGURA_1_1 = ("docs/tesis/figuras/figura_norma_a_grafo.svg",
              "874292f54e3c5d70b036b070b6beb7e8ce4c568a2aa6862fde23d865588f3e9b")

# --------------------------------------------------------------------------- #
# Contenido                                                                    #
# --------------------------------------------------------------------------- #
UNIDAD = "cla::5.1.1.1"
# Nodos dibujados: (clave, tipo, chunk de su procedencia punto_propio, etiqueta
# tal como está en el grafo). Las claves son las de la figura 1.1 (data-caja
# de figura_norma_a_grafo.svg). El primero es el nodo de origen.
NODOS = (
    ("condicion_monto", "Condicion", "cla::5.1.1.1", "Superar dos veces importe referencia punto 3.7"),
    ("operacion", "Operacion", "cla::5.1.1.1", "Inclusión en cartera comercial — créditos consumo/vivienda"),
)
ORIGEN, DESTINO = NODOS[0][0], NODOS[1][0]
# La arista: (origen, relación en el grafo, destino). Debe existir exactamente
# una vez en cada grafo.
ARISTA = (ORIGEN, "condicion_de", DESTINO)
# Nodos de la unidad 5.1.1.1 que no se dibujan, a propósito: (tipo, etiqueta).
NO_DIBUJADOS = (("Condicion", "Repago vinculado a actividad productiva/comercial"),
                ("Excepcion", "Excepción cartera comercial — créditos consumo/vivienda"))
# Rótulo de la arista: el nombre de la relación tal como está en el grafo (la
# figura muestra la anatomía de la tripleta, no su lectura en castellano).
ROTULO_ARISTA = ARISTA[1]
# Las tres llamadas, en gris. El tipo y el punto de cada nodo van en su caja.
LLAMADA = {"origen": "nodo de origen",
           "relacion": "relación · nombre y dirección",
           "destino": "nodo de destino"}
LINEAS_ETIQUETA = 3   # la etiqueta del grafo, sin abreviar, entra en tres líneas

# --------------------------------------------------------------------------- #
# Tamaño impreso, paleta y tipografía                                          #
# --------------------------------------------------------------------------- #
# Como en la versión 1 (el de la figura del proceso): 0,85 del ancho de texto
# de 15 cm; lienzo de 720 unidades.
ANCHO_FIGURA_CM = 15.0 * 0.85                         # 12,75 cm
W = 720
PT_MINIMO = 7.0                                       # letra mínima impresa
TINTA = "#1f1f1f"                                     # texto de los nodos (figura 1.1)
GRIS_ARISTA = base.GRIS_ARISTA                        # líneas de llamada
GRIS_ROTULO = base.GRIS_ROTULO                        # texto de las llamadas
# Trazo y rótulo de la arista, como en la versión 1: el gris oscuro de la
# paleta compartida (borde de las etapas determinísticas de la figura del
# proceso). No es el naranja ACENTO de la figura 1.1, que las figuras de la
# Introducción reservan a las remisiones.
TRAZO_ARISTA = "#4a5a6a"

FS_NODO = 17          # encabezado «Tipo · punto N» y etiqueta de los nodos
FS_ARISTA = 17        # rótulo de la arista, en negrita
FS_LLAMADA = 15       # las tres llamadas en gris
IL_NODO = 21          # interlínea dentro del nodo

MARGEN = 24
W_NODO = 260
PAD_NODO = 12
LARGO_LLAMADA = 18      # línea de llamada entre el texto y el elemento
HOLGURA_LLAMADA = 5     # aire entre la línea de llamada y el texto o el nodo
BORDE = 3.0             # distancia máxima de un extremo de la arista al borde de su caja (inventario)
CERCA = 9.0             # distancia máxima de un extremo de llamada a lo que nombra (inventario)


# --------------------------------------------------------------------------- #
# Carga                                                                        #
# --------------------------------------------------------------------------- #
def leer_esquema_r2():
    """Las asignaciones de modelos_r2.py que el script necesita, leídas con
    ast (sin importar ni ejecutar el módulo): {nombre: (valor, línea)}."""
    arbol = ast.parse(base.leer_con_candado(*MODELOS_R2).decode("utf-8"))
    buscadas = ("PREDICADOS", "AMPLIACION_R2", "PREDICADOS_DERIVADOS")
    salida = {}
    for nodo in arbol.body:
        if isinstance(nodo, ast.Assign) and len(nodo.targets) == 1 and isinstance(nodo.targets[0], ast.Name):
            nombre = nodo.targets[0].id
        elif isinstance(nodo, ast.AnnAssign) and isinstance(nodo.target, ast.Name):
            nombre = nodo.target.id
        else:
            continue
        if nombre in buscadas:
            if nombre in salida:
                freno(f"{MODELOS_R2[0]}: {nombre} asignado dos veces")
            salida[nombre] = (ast.literal_eval(nodo.value), nodo.lineno)
    if sorted(salida) != sorted(buscadas):
        freno(f"{MODELOS_R2[0]}: faltan {sorted(set(buscadas) - set(salida))}")
    return salida


def controlar_firma(sub, diez, esquema):
    """La arista es de extracción: su relación es un predicado del esquema, no
    un predicado derivado; su firma está en la matriz r2; sin rol_fuente ni
    propiedades en ninguno de los dos grafos."""
    o, rel, d = ARISTA
    firma = (rel, sub["nodos"][o]["type"], sub["nodos"][d]["type"])
    if rel not in esquema["PREDICADOS"][0]:
        freno(f"{rel} no está en PREDICADOS de {MODELOS_R2[0]}")
    if rel in esquema["PREDICADOS_DERIVADOS"][0]:
        freno(f"{rel} es un predicado derivado: la arista no es de extracción")
    if firma not in esquema["AMPLIACION_R2"][0]:
        freno(f"la firma {firma} no está en AMPLIACION_R2 de {MODELOS_R2[0]}")
    for g in (sub, diez):
        kg = json.loads(base.leer_con_candado(g["ruta"], g["sha256"]).decode("utf-8"))
        e = kg["edges"][g["aristas"][0]["indice"]]
        if "rol_fuente" in e or e.get("properties"):
            freno(f"{g['ruta']}: la arista lleva rol_fuente o propiedades")
        inversas = [i for i, x in enumerate(kg["edges"])
                    if x["source"] == g["nodos"][d]["id"] and x["target"] == g["nodos"][o]["id"]]
        if inversas:
            freno(f"{g['ruta']}: aristas en sentido inverso {inversas}")
    return firma


def leer_figura_1_1():
    """Cajas de la figura 1.1 versión 2: {data-caja: {tipo, punto, etiqueta,
    relleno, borde, grosor}}, desde el encabezado en negrita «Tipo · punto N»
    y las líneas de la etiqueta que la caja contiene."""
    raiz = ET.fromstring(base.leer_con_candado(*FIGURA_1_1).decode("utf-8"))
    textos = list(raiz.iter(NS + "text"))
    cajas = {}
    for r in raiz.iter(NS + "rect"):
        clave = r.get("data-caja")
        if not clave:
            continue
        x, y, w, h = (float(r.get(k)) for k in ("x", "y", "width", "height"))
        dentro = sorted((t for t in textos if x < float(t.get("x")) < x + w and y < float(t.get("y")) < y + h),
                        key=lambda t: float(t.get("y")))
        if not dentro or dentro[0].get("font-weight") != "bold" or " · punto " not in (dentro[0].text or ""):
            freno(f"{FIGURA_1_1[0]}: la caja {clave} no tiene el encabezado «Tipo · punto N»")
        tipo, punto = dentro[0].text.split(" · punto ", 1)
        cajas[clave] = {"tipo": tipo, "punto": punto, "etiqueta": " ".join(t.text for t in dentro[1:]),
                        "relleno": r.get("fill"), "borde": r.get("stroke"), "grosor": r.get("stroke-width")}
    return cajas


def controlar_figura_1_1(sub, colores):
    """Los dos nodos, iguales a los de la figura 1.1: tipo, punto, etiqueta y
    colores."""
    cajas = leer_figura_1_1()
    for clave, _, _, _ in NODOS:
        n, c = sub["nodos"][clave], cajas.get(clave)
        if c is None:
            freno(f"{FIGURA_1_1[0]}: no tiene la caja {clave}")
        if (c["tipo"], c["punto"], c["etiqueta"]) != (n["type"], n["punto"], n["label"]):
            freno(f"{FIGURA_1_1[0]}: la caja {clave} es {c['tipo']} {c['punto']} {c['etiqueta']!r}, "
                  f"no {n['type']} {n['punto']} {n['label']!r}")
        if {k: c[k] for k in ("relleno", "borde", "grosor")} != colores[n["type"]]:
            freno(f"{FIGURA_1_1[0]}: la caja {clave} no tiene los colores de {n['type']} en {ESTILO[0]}")
    return cajas


def cargar():
    sub = base.cargar_subgrafo(GRAFO, NODOS, (ARISTA,), NO_DIBUJADOS, UNIDAD)
    diez = base.cargar_subgrafo(GRAFO_DIEZ, NODOS, (ARISTA,), NO_DIBUJADOS, UNIDAD)
    base.comparar_grafos(sub, diez)
    esquema = leer_esquema_r2()
    firma = controlar_firma(sub, diez, esquema)
    colores = base.leer_colores_tipo()
    for _, tipo, _, _ in NODOS:
        if tipo not in colores:
            freno(f"{ESTILO[0]} no tiene caja {tipo}")
    cajas_1_1 = controlar_figura_1_1(sub, colores)
    return sub, diez, esquema, firma, colores, cajas_1_1


# --------------------------------------------------------------------------- #
# Composición: una fila de dos nodos unidos por la arista; las llamadas de los  #
# nodos arriba, la de la relación abajo, cada una con su línea de llamada.     #
# --------------------------------------------------------------------------- #
def lineas_nodo(nodo):
    """Líneas del nodo con el formato de la figura 1.1 (lineas_nodo del
    generador base): «Tipo · punto N» en negrita y debajo la etiqueta del
    grafo, completa, sin abreviar, envuelta al ancho de la caja; el generador
    base frena si una línea no entra o si lo dibujado no es la etiqueta."""
    lineas = base.lineas_nodo(nodo, W_NODO - 2 * PAD_NODO, FS_NODO)
    if len(lineas) - 1 > LINEAS_ETIQUETA:
        freno(f"la etiqueta {nodo['label']!r} ocupa {len(lineas) - 1} líneas, máximo {LINEAS_ETIQUETA}")
    return lineas


def texto(partes, x, y, s, fs, negrita, relleno, anclaje, extra=""):
    partes.append(f'<text x="{f(x)}" y="{f(y)}" text-anchor="{anclaje}" font-size="{fs}" '
                  f'font-weight="{"bold" if negrita else "normal"}" fill="{relleno}"{extra}>{esc(s)}</text>')


def linea_llamada(partes, x0, y0, x1, y1, cual):
    partes.append(f'<path d="M{f(x0)},{f(y0)} L{f(x1)},{f(y1)}" fill="none" stroke="{GRIS_ARISTA}" '
                  f'stroke-width="1.0" opacity="1" data-llamada="{cual}"/>')


def componer(sub, colores, perturbacion=None):
    nodos = {k: dict(v) for k, v in sub["nodos"].items()}
    tipo_colores = {k: v["type"] for k, v in nodos.items()}   # los colores salen del tipo del grafo
    if perturbacion == "etiqueta_distinta":
        nodos[DESTINO]["label"] = "Inclusión en cartera comercial — créditos de consumo o vivienda"
    if perturbacion == "tipo_cambiado":
        nodos[ORIGEN]["type"] = "Restriccion"                 # solo el encabezado de la caja
    llamada_sobre = {"origen": ORIGEN, "destino": DESTINO}
    if perturbacion == "llamadas_intercambiadas":
        llamada_sobre = {"origen": DESTINO, "destino": ORIGEN}
    lineas = {k: lineas_nodo(nodos[k]) for k in (ORIGEN, DESTINO)}
    h_nodo = 2 * PAD_NODO + max(len(v) for v in lineas.values()) * IL_NODO

    y_llam = MARGEN + FS_LLAMADA
    y_nodo = y_llam + HOLGURA_LLAMADA + LARGO_LLAMADA + HOLGURA_LLAMADA
    pos = {ORIGEN: MARGEN, DESTINO: W - MARGEN - W_NODO}
    centro = {k: x + W_NODO / 2.0 for k, x in pos.items()}
    cy = y_nodo + h_nodo / 2.0
    partes = []

    # Fila superior: las llamadas de los dos nodos, centradas sobre su caja, y
    # sus líneas hasta el borde superior de la caja.
    for cual in ("origen", "destino"):
        clave = llamada_sobre[cual]
        texto(partes, centro[clave], y_llam, LLAMADA[cual], FS_LLAMADA, False, GRIS_ROTULO, "middle")
        linea_llamada(partes, centro[clave], y_llam + HOLGURA_LLAMADA, centro[clave], y_nodo - HOLGURA_LLAMADA, cual)

    # La arista: del borde derecho del origen al borde izquierdo del destino,
    # a 2 unidades de cada uno, trazo continuo en el gris oscuro, con su rótulo
    # encima.
    x0, x1 = pos[ORIGEN] + W_NODO + 2, pos[DESTINO] - 2
    if perturbacion == "direccion_invertida":
        x0, x1 = x1, x0
    partes.append(f'<path d="M{f(x0)},{f(cy)} L{f(x1)},{f(cy)}" fill="none" stroke="{TRAZO_ARISTA}" '
                  f'stroke-width="2.6" opacity="0.95" marker-end="url(#arL)" data-arista="0"/>')
    x_medio = (x0 + x1) / 2.0
    y_rotulo = cy - 9
    if perturbacion == "rotulo_sobre_caja":
        x_medio = pos[DESTINO] + 12
    texto(partes, x_medio, y_rotulo, ROTULO_ARISTA, FS_ARISTA, True, TRAZO_ARISTA, "middle", ' data-rotulo="0"')

    # Los dos nodos: caja con los colores de su tipo, encabezado y etiqueta.
    for clave in (ORIGEN, DESTINO):
        c = colores[tipo_colores[clave]]
        partes.append(f'<rect x="{f(pos[clave])}" y="{f(y_nodo)}" width="{f(W_NODO)}" height="{f(h_nodo)}" '
                      f'fill="{c["relleno"]}" stroke="{c["borde"]}" stroke-width="{c["grosor"]}" '
                      f'rx="{base.RX_NODO}" data-caja="{clave}"/>')
        yy = y_nodo + (h_nodo - len(lineas[clave]) * IL_NODO) / 2.0 + FS_NODO - 2
        for s, negrita in lineas[clave]:
            texto(partes, centro[clave], yy, s, FS_NODO, negrita, TINTA, "middle")
            yy += IL_NODO

    # Fila inferior: la llamada de la relación, con su línea desde la arista.
    x_rel = (pos[ORIGEN] + W_NODO + pos[DESTINO]) / 2.0
    y_llam_rel = y_nodo + h_nodo + HOLGURA_LLAMADA + FS_LLAMADA
    y_ini_rel = cy + HOLGURA_LLAMADA
    if perturbacion == "cruce":
        y_ini_rel = cy - 2 * HOLGURA_LLAMADA
    linea_llamada(partes, x_rel, y_ini_rel, x_rel, y_llam_rel - FS_LLAMADA - HOLGURA_LLAMADA, "relacion")
    texto(partes, x_rel, y_llam_rel, LLAMADA["relacion"], FS_LLAMADA, False, GRIS_ROTULO, "middle")
    alto_total = y_llam_rel + HOLGURA_LLAMADA + MARGEN

    defs = ('<defs><marker id="arL" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" '
            f'orient="auto"><path d="M0,0L10,5L0,10z" fill="{TRAZO_ARISTA}"/></marker></defs>')
    out = [base.cabecera_svg(W, alto_total, ANCHO_FIGURA_CM),
           f'<rect width="{W}" height="{f(alto_total)}" fill="white"/>', defs] + partes + ["</svg>"]
    return "\n".join(out) + "\n", alto_total


# --------------------------------------------------------------------------- #
# Inventario: la tripleta releída del SVG                                       #
# --------------------------------------------------------------------------- #
def distancia_a_tramo(p, a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]
    t = 0.0 if dx == dy == 0 else max(0.0, min(1.0, ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / (dx * dx + dy * dy)))
    return ((p[0] - a[0] - t * dx) ** 2 + (p[1] - a[1] - t * dy) ** 2) ** 0.5


def inventario_svg(svg):
    """Solo desde el SVG: cada caja de nodo (rect rx=7 con data-caja) con sus
    colores, su encabezado «Tipo · punto N» y su etiqueta; la arista (trazo
    con data-arista) con la caja en cuyo borde empieza, la caja en cuyo borde
    termina (la de la flecha) y su rótulo; y cada línea de llamada
    (data-llamada) con el texto junto a uno de sus extremos y la caja o la
    arista junto al otro."""
    medir = base.medidor()
    raiz = ET.fromstring(svg)
    cajas = {}
    for r in raiz.iter(NS + "rect"):
        if r.get("data-caja") and r.get("rx") == str(base.RX_NODO):
            x, y, w, h = (float(r.get(k)) for k in ("x", "y", "width", "height"))
            cajas[r.get("data-caja")] = {"R": (x, y, x + w, y + h), "relleno": r.get("fill"),
                                         "borde": r.get("stroke"), "grosor": r.get("stroke-width")}
    textos = base.textos_svg(raiz, medir)
    fallas = []
    for k, c in cajas.items():
        R = c["R"]
        dentro = sorted((t for t in textos if base.contiene(R, t["bb"])), key=lambda t: t["y"])
        if (not dentro or not dentro[0]["negrita"] or " · punto " not in dentro[0]["s"]
                or any(t["negrita"] for t in dentro[1:])):
            fallas.append(f"la caja {k} no empieza con «Tipo · punto N» en negrita seguido de la etiqueta")
            c["tipo"] = c["punto"] = c["etiqueta"] = None
            continue
        c["tipo"], c["punto"] = dentro[0]["s"].split(" · punto ", 1)
        c["etiqueta"] = " ".join(t["s"] for t in dentro[1:])

    def caja_en_borde(p):
        en = [k for k, c in cajas.items()
              if (abs(p[0] - c["R"][0]) <= BORDE or abs(p[0] - c["R"][2]) <= BORDE) and c["R"][1] <= p[1] <= c["R"][3]
              or (abs(p[1] - c["R"][1]) <= BORDE or abs(p[1] - c["R"][3]) <= BORDE) and c["R"][0] <= p[0] <= c["R"][2]]
        return en[0] if len(en) == 1 else None
    aristas = []
    rotulos = {t["rotulo"]: t["s"] for t in textos if t["rotulo"] is not None}
    for p in raiz.iter(NS + "path"):
        if p.get("data-arista") is None:
            continue
        pts = base.puntos_de(p.get("d"))
        aristas.append({"pts": pts, "origen": caja_en_borde(pts[0]), "destino": caja_en_borde(pts[-1]),
                        "rotulo": rotulos.get(p.get("data-arista")), "flecha": bool(p.get("marker-end"))})

    def texto_junto(p):
        cerca = [t for t in textos if t["bb"][0] - 1 <= p[0] <= t["bb"][2] + 1
                 and min(abs(p[1] - t["bb"][1]), abs(p[1] - t["bb"][3])) <= CERCA]
        return cerca[0] if len(cerca) == 1 else None

    def caja_junto(p):
        cerca = [k for k, c in cajas.items() if c["R"][0] <= p[0] <= c["R"][2]
                 and min(abs(p[1] - c["R"][1]), abs(p[1] - c["R"][3])) <= CERCA]
        return cerca[0] if len(cerca) == 1 else None

    def arista_junto(p):
        cerca = [i for i, a in enumerate(aristas)
                 if any(distancia_a_tramo(p, u, v) <= CERCA for u, v in zip(a["pts"], a["pts"][1:]))]
        return cerca[0] if len(cerca) == 1 else None
    llamadas = []
    for p in raiz.iter(NS + "path"):
        if p.get("data-llamada") is None:
            continue
        pts = base.puntos_de(p.get("d"))
        hallado = None
        for a, b in ((pts[0], pts[-1]), (pts[-1], pts[0])):
            t = texto_junto(a)
            if t is None:
                continue
            k, i = caja_junto(b), arista_junto(b)
            if (k is None) == (i is None):
                continue
            hallado = {"texto": t["s"], "caja": k, "arista": i, "pts": pts}
        if hallado is None:
            fallas.append(f"línea de llamada sin texto en un extremo y una caja o la arista en el otro: {pts}")
        else:
            llamadas.append(hallado)
    return cajas, aristas, llamadas, fallas


def controlar_inventario(svg, sub, colores):
    """La tripleta rearmada desde el SVG contra la del grafo."""
    cajas, aristas, llamadas, fallas = inventario_svg(svg)
    o, rel, d = ARISTA
    par = {k: (n["type"], n["punto"], n["label"]) for k, n in sub["nodos"].items()}
    esperada = [(par[o], rel, par[d])]
    # Cada caja tiene los colores del tipo que escribe su encabezado.
    for k, c in cajas.items():
        if c["tipo"] is None:
            continue
        if c["tipo"] not in colores:
            fallas.append(f"la caja {k} dice {c['tipo']}, que no tiene colores en {ESTILO[0]}")
        elif {x: c[x] for x in ("relleno", "borde", "grosor")} != colores[c["tipo"]]:
            fallas.append(f"la caja {k} dice {c['tipo']} y no tiene los colores de {c['tipo']}")
    # Cada llamada de nodo nombra su papel; tipo, punto y etiqueta son los de la
    # caja a la que apunta.
    papel = {LLAMADA["origen"]: "origen", LLAMADA["destino"]: "destino"}
    nodo_de = {}
    for ll in llamadas:
        if ll["texto"] in papel:
            cual = papel[ll["texto"]]
            if ll["caja"] is None:
                fallas.append(f"la llamada {ll['texto']!r} no apunta a una caja")
                continue
            c = cajas[ll["caja"]]
            if cual in nodo_de:
                fallas.append(f"dos llamadas de nodo de {cual}")
            nodo_de[cual] = (ll["caja"], (c["tipo"], c["punto"], c["etiqueta"]))
        elif ll["texto"] == LLAMADA["relacion"]:
            if ll["arista"] is None:
                fallas.append("la llamada de la relación no apunta a la arista")
        else:
            fallas.append(f"llamada desconocida: {ll['texto']!r}")
    if sorted(nodo_de) != ["destino", "origen"]:
        fallas.append(f"llamadas de nodo: {sorted(nodo_de)}, no origen y destino")
    if [ll["texto"] for ll in llamadas].count(LLAMADA["relacion"]) != 1:
        fallas.append("no hay exactamente una llamada de la relación")
    dibujadas = []
    for a in aristas:
        if not a["flecha"]:
            fallas.append("la arista no tiene flecha")
        extremos = {}
        for cual, caja in (("origen", a["origen"]), ("destino", a["destino"])):
            if caja is None or cual not in nodo_de:
                extremos[cual] = None
            elif nodo_de[cual][0] != caja:
                fallas.append(f"la arista {cual} en la caja {caja}; la llamada de {cual}, en {nodo_de[cual][0]}")
                extremos[cual] = None
            else:
                extremos[cual] = nodo_de[cual][1]
        dibujadas.append((extremos["origen"], a["rotulo"], extremos["destino"]))
    for nombre, esp, dib in (("nodo", list(par.values()), [v[1] for v in nodo_de.values()]),
                             ("arista", esperada, dibujadas)):
        for x in sorted((Counter(esp) - Counter(dib)).elements(), key=str):
            fallas.append(f"{nombre} del grafo que no está en la figura: {x}")
        for x in sorted((Counter(dib) - Counter(esp)).elements(), key=str):
            fallas.append(f"{nombre} de la figura que no está en el grafo: {x}")
    return fallas, nodo_de, dibujadas, llamadas


# --------------------------------------------------------------------------- #
# Geometría                                                                    #
# --------------------------------------------------------------------------- #
def controlar_llamadas(svg):
    """Las líneas de llamada, que controlar_geometria no mira (no llevan
    flecha): ninguna toca una caja ni un texto, y entre todos los trazos
    (arista y llamadas) no hay cruces."""
    raiz = ET.fromstring(svg)
    medir = base.medidor()
    textos = base.textos_svg(raiz, medir)
    cajas = []
    for r in raiz.iter(NS + "rect"):
        if r.get("data-caja"):
            x, y, w, h = (float(r.get(k)) for k in ("x", "y", "width", "height"))
            cajas.append((r.get("data-caja"), (x, y, x + w, y + h)))
    trazos = [(p.get("data-llamada") or f"arista {p.get('data-arista')}", base.puntos_de(p.get("d")))
              for p in raiz.iter(NS + "path") if p.get("data-llamada") or p.get("data-arista")]
    fallas = []
    for ident, pts in trazos:
        if ident.startswith("arista"):
            continue
        for p, q in zip(pts, pts[1:]):
            for nombre, c in cajas:
                if base.tramo_toca_rect(p, q, c):
                    fallas.append(f"la llamada {ident} toca la caja {nombre}")
            for t in textos:
                if base.tramo_toca_rect(p, q, t["bb"]):
                    fallas.append(f"la llamada {ident} toca el texto {t['s']!r}")
    cruces = []
    for i in range(len(trazos)):
        for j in range(i + 1, len(trazos)):
            (ia, pa), (ib, pb) = trazos[i], trazos[j]
            if any(base.tramos_se_tocan(p1, p2, q1, q2) for p1, p2 in zip(pa, pa[1:]) for q1, q2 in zip(pb, pb[1:])):
                cruces.append((ia, ib))
    if cruces:
        fallas.append(f"{len(cruces)} cruce(s) entre trazos, declarados 0: {cruces}")
    return fallas, {"trazos": len(trazos), "cruces": cruces}


# --------------------------------------------------------------------------- #
# Controles y pruebas negativas                                                #
# --------------------------------------------------------------------------- #
# Prueba negativa -> control que tiene que fallar y texto de la falla propia.
PRUEBAS_NEGATIVAS = (("direccion_invertida", "inventario", "arista de la figura que no está en el grafo"),
                     ("llamadas_intercambiadas", "inventario", "la llamada de origen, en"),
                     ("etiqueta_distinta", "inventario", "nodo de la figura que no está en el grafo"),
                     ("tipo_cambiado", "inventario", "no tiene los colores de Restriccion"),
                     ("rotulo_sobre_caja", "geometria", "texto sobre la caja"),
                     ("cruce", "llamadas", "cruce(s) entre trazos"))


def controlar(sub, colores, perturbacion=None):
    svg, alto = componer(sub, colores, perturbacion)
    c = {}
    c["inventario"], nodo_de, dibujadas, llamadas = controlar_inventario(svg, sub, colores)
    c["geometria"], info = base.controlar_geometria(svg, ANCHO_FIGURA_CM, W, pt_minimo=PT_MINIMO)
    c["llamadas"], info_ll = controlar_llamadas(svg)
    return svg, alto, c, info, info_ll, nodo_de, dibujadas, llamadas


def pruebas_negativas(sub, colores):
    vivas = []
    for caso, control, patron in PRUEBAS_NEGATIVAS:
        c = controlar(sub, colores, caso)[2]
        propia = [x for x in c[control] if patron in x]
        if not propia:
            freno(f"la prueba negativa {caso} no hizo fallar el control de {control} con «{patron}»")
        vivas.append((caso, control, propia[0], sorted(k for k, v in c.items() if v and k != control)))
    return vivas


def argumentos():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--salida", default=AQUI,
                    help="directorio donde escribir el SVG, el PNG y el PDF (por omisión, el del script)")
    ap.add_argument("--perturbar", choices=[c for c, _, _ in PRUEBAS_NEGATIVAS], default=None,
                    help="compone la figura con ese defecto: los controles fallan y no se escribe nada")
    return ap.parse_args()


def informe(sub, diez, esquema, firma, colores, cajas_1_1):
    print("FUENTES (sha256 comprobado):")
    for nombre, par in (("grafo", GRAFO), ("grafo diez", GRAFO_DIEZ), ("estilo", ESTILO),
                        ("esquema r2", MODELOS_R2), ("figura 1.1", FIGURA_1_1)):
        print(f"  {nombre:11s} {par[0]}   {par[1]}")
    print(f"GRAFO: {sub['ruta']}   ({sub['n_nodos']} nodos, {sub['n_aristas']} aristas)")
    print(f"  igual en {diez['ruta']}   ({diez['n_nodos']} nodos, {diez['n_aristas']} aristas)")
    for clave, n in sub["nodos"].items():
        print(f"  nodo {clave:15s} {n['type']:9s} punto {n['punto']:8s} {n['label']!r}")
        print(f"       id {n['id']}   (en diez: {diez['nodos'][clave]['id'] == n['id']})")
    a, b = sub["aristas"][0], diez["aristas"][0]
    print(f"  arista kg['edges'][{a['indice']}] (diez [{b['indice']}]) {a['origen']} --{a['relation']}--> "
          f"{a['destino']}   procedencia {a['chunks']}   properties {json.dumps(a['properties'])}")
    print(f"  firma {firma}: AMPLIACION_R2 ({MODELOS_R2[0]}:{esquema['AMPLIACION_R2'][1]}); "
          f"{firma[0]} en PREDICADOS (:{esquema['PREDICADOS'][1]}) y fuera de PREDICADOS_DERIVADOS "
          f"(:{esquema['PREDICADOS_DERIVADOS'][1]}) = {list(esquema['PREDICADOS_DERIVADOS'][0])}; "
          f"sin rol_fuente ni propiedades; sin aristas en sentido inverso")
    print("  NO DIBUJADO, aristas de los nodos dibujados hacia fuera del dibujo (nodo, sentido, relación, tipo del otro extremo):")
    for k, v in sorted(sub["afuera"].items()):
        print(f"    {k}: {v}")
    print("  NO DIBUJADO, nodos de la unidad y sus aristas:")
    for k, v in sub["no_dibujados"].items():
        print(f"    {k}: {v}")
    print("COLORES DE TIPO (de la figura del esquema final; iguales en la figura 1.1):")
    for clave, tipo, _, _ in NODOS:
        print(f"  {tipo:9s} {colores[tipo]}   figura 1.1, caja {clave}: {cajas_1_1[clave]}")


def main():
    args = argumentos()
    sub, diez, esquema, firma, colores, cajas_1_1 = cargar()
    informe(sub, diez, esquema, firma, colores, cajas_1_1)

    vivas = pruebas_negativas(sub, colores)
    print(f"PRUEBAS NEGATIVAS: {len(vivas)} de {len(PRUEBAS_NEGATIVAS)} hacen fallar su control")
    for caso, control, falla, otros in vivas:
        print(f"  {caso} -> {control}: {falla}" + (f" (fallan también: {', '.join(otros)})" if otros else ""))

    svg, alto, c, info, info_ll, nodo_de, dibujadas, llamadas = controlar(sub, colores, args.perturbar)
    if args.perturbar:
        print(f"PERTURBACIÓN: {args.perturbar}")
    print(f"INVENTARIO (releído del SVG): {len(nodo_de)} nodos, {len(dibujadas)} arista, "
          f"{len(llamadas)} llamadas; fallas: {len(c['inventario'])}")
    for cual in ("origen", "destino"):
        if cual in nodo_de:
            print(f"  nodo de {cual:7s} caja {nodo_de[cual][0]}: {nodo_de[cual][1]}")
    for t in dibujadas:
        print(f"  arista {t[0]} --{t[1]}--> {t[2]}")
    for ll in llamadas:
        print(f"  llamada {ll['texto']!r} -> " + (f"caja {ll['caja']}" if ll["caja"] else f"arista {ll['arista']}"))
    print(f"GEOMETRÍA: {info['textos']} textos, {info['cajas']} cajas, {info['trazos']} trazo con flecha; "
          f"{info_ll['trazos']} trazos con las llamadas; cruces {len(info_ll['cruces'])}; "
          f"fallas: {len(c['geometria']) + len(c['llamadas'])}")
    for k in c:
        for falla in c[k]:
            print(f"  MAL [{k}] {falla}")
    if any(c.values()):
        raise SystemExit("FALLA: la figura tiene defectos; no se escribe nada")
    print(f"TAMAÑO: lienzo {W} x {f(alto)}, impreso a {ANCHO_FIGURA_CM:.2f} x {ANCHO_FIGURA_CM * alto / W:.2f} cm")
    for fs, pt in sorted(info["tamanos"].items()):
        print(f"  letra {fs:g} unidades -> {pt:.2f} pt (mínimo {PT_MINIMO})")
    rutas = base.exportar(svg, args.salida, NOMBRE, ANCHO_FIGURA_CM)
    for e in ("svg", "png", "pdf"):
        print(f"{e.upper()}: {os.path.relpath(rutas[e], base.RAIZ)}   sha256 {base.sha256(rutas[e])}")
    print(f"  PNG {base.png_dimensiones(rutas['png'])} px a {base.DPI} dpi; {base.version_rsvg()}")


if __name__ == "__main__":
    try:
        main()
    except base.Freno as e:
        raise SystemExit(f"FRENO {e}")
