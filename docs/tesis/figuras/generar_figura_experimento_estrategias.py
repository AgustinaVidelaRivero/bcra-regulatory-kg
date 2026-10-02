#!/usr/bin/env python3
"""Figura «el experimento de la comparación de estrategias» (capítulo 3, sección 3.7).

Diagrama de flujo de izquierda a derecha, en dos filas:
- arriba, la construcción: el conjunto de desarrollo (5 Textos Ordenados), las
  cinco estrategias de esquema, una caja por estrategia con su nombre, y los
  cinco grafos, uno por estrategia; a la derecha, las 23 preguntas con su
  reparto por tipo;
- abajo, la evaluación: el agente, al que llegan los grafos y las preguntas,
  con sus operaciones y su tope de llamadas; las 3 respuestas por pregunta y
  grafo; el juez, con sus dos pasos; y las 4 medidas. Debajo del juez, en una
  caja discontinua, las afirmaciones que la referencia no decide, revisadas
  contra los Textos Ordenados, con una flecha a la medida «correctas», la única
  que esa revisión cambia.

Misma técnica, tipografía y paleta que generar_figura_proceso_extraccion.py,
de donde se importan: cajas de etapa con el rótulo en negrita, la hoja con la
esquina plegada para el documento de entrada, naranja para las etapas que
ejecuta un modelo de lenguaje (las cinco extracciones, el agente y el juez),
gris azulado para las determinísticas (el cálculo de las medidas), cajas
neutras para lo que entra y sale, y la misma leyenda al pie. La figura no lleva
nombres de archivo, commits, ids de preguntas ni nombres de run.

Los textos son los fijados para la figura (TEXTO, ESTRATEGIAS, MEDIDAS); los
cortes de línea se fijan a mano en CORTES y el script comprueba que no cambien
el texto. Cada número del texto se coteja al generar con la fuente que lo
respalda, con candado de sha256 (FUENTES; si una fuente cambia, el script
frena antes de dibujar):
- 5 Textos Ordenados, 23 preguntas y su reparto 10/5/4/4: metadatos y
  preguntas del conjunto de evaluación de la comparación;
- 3 operaciones y tope de 15 llamadas: las herramientas y la constante del
  agente;
- 2 pasos: los dos bloques de instrucciones del juez;
- 3 respuestas por pregunta y grafo y 5 grafos: el número de repeticiones de la
  corrida y las trazas congeladas (5 grafos × 23 preguntas × 3 repeticiones);
- las afirmaciones revisadas contra los Textos Ordenados: el método declarado
  en la adjudicación firmada;
- las 4 medidas y que la revisión solo cambia «correctas»: las tablas del
  reporte final de la corrida.

Controles, en cada corrida (el script frena si fallan):
- contenido: lo dibujado reconstruye el texto fijado, cada número coincide con
  su fuente y ningún texto lleva nombres de archivo, rutas, commits, ids de
  preguntas, nombres de run ni identificadores internos;
- textos, con las métricas reales de Helvetica: ningún texto por debajo de
  7 pt impresos a 15 cm, fuera del lienzo, fuera de la caja que lo contiene,
  cortado por el borde de otra caja, superpuesto a otro texto, tocado por una
  marca (renglones, pliegue, nodos y aristas de los grafos), por un trazo o por
  una punta de flecha;
- trazos: ninguno entra en el interior de una caja y ninguno pasa a menos de
  DISTANCIA_MIN de un trazo de otro grupo;
- margen: ningún texto ni elemento dibujado a menos de 2 mm de un borde;
- registro: cada elemento del SVG está registrado en los controles anteriores
  (el SVG se relee y sus elementos se cotejan uno a uno con el registro).

Salidas, byte-reproducibles: figura_experimento_estrategias.svg, .png (300 dpi,
densidad grabada) y .pdf (fecha de creación fijada por SOURCE_DATE_EPOCH).

Uso (desde la raíz del repo):
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_experimento_estrategias.py
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_experimento_estrategias.py --salida <directorio>
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
from collections import Counter

sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import generar_figura_norma_a_grafo as base          # noqa: E402
import generar_figura_proceso_extraccion as proc     # noqa: E402

RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", ".."))
NOMBRE = "figura_experimento_estrategias"

# --------------------------------------------------------------------------- #
# Fuentes y candados                                                           #
# --------------------------------------------------------------------------- #
EV = "data/experiment/evaluacion"
FUENTES = {
    "preguntas": (f"{EV}/queries/eval_set_v1.json",
                  "aabe36d2b6b519dc82a56841fe315db9600e669115d7efa170978f96ea9c1931"),
    "agente": (f"{EV}/harness.py",
               "fd267e833866f86850e43130e627b08d78e05523b97484696de0ab0c8c9fba9e"),
    "juez": (f"{EV}/judge.py",
             "7169145aaeb3f2d90a7e3873964378aa6520c5688fed136cf5a79ea63b589eaa"),
    "corrida": (f"{EV}/run_frozen.py",
                "b460a4455bb1e9a6b512c9acd99bde6e7720229e113451b6ed59c8155fb6b067"),
    "revision": (f"{EV}/adjudicacion_FIRMADO.json",
                 "9f1bd89e1bbb1e669c50d654e75bd1df9ba17f61b1bc740a9a0c61166c25abda"),
    "reporte": (f"{EV}/frozen_run/reporte_final.md",
                "a91291f9d02c35fd5c54251bc558b4a380b1c9f19e9cc6b871c33c00c2d7f0f0"),
}
REL_TRAZAS = f"{EV}/frozen_run/traces"
# Líneas del reporte final que tienen que estar tal cual: la tabla de
# correctas, la de las otras tres medidas y el título que las declara no
# afectadas por la adjudicación.
REPORTE_CORRECTAS = "**Totales answerable por grafo (19 preguntas):**"
REPORTE_NO_AFECTADAS = "## 2. Dimensiones cerradas (congeladas — no afectadas por la adjudicación)"
REPORTE_DIMENSIONES = ("| Grafo | Estabilidad | hit_limit | abst. correcta/incorr. | cita_doc T/F "
                       "| prec punto/pag/aus | Costo |")

# --------------------------------------------------------------------------- #
# Texto fijado para la figura                                                  #
# --------------------------------------------------------------------------- #
# Las estrategias en el orden de la sección, con el directorio de su grafo
# (no se dibuja: el script comprueba que exista y que su prefijo sea el de la
# carpeta de trazas correspondiente).
ESTRATEGIAS = (("Receta genérica", "run_1_cookbook"),
               ("Vocabulario controlado", "run_2_papers"),
               ("Esquema cerrado", "run_3_ppf_core"),
               ("Emergente", "run_4_schema_light"),
               ("Híbrida", "run_5_hybrid"))
MEDIDAS = ("correctas", "estables", "citas a nivel de punto", "límite agotado")
# Tipo de pregunta (categoría en el conjunto de evaluación) y su rótulo.
CATEGORIAS = (("factual_directa", "de dato directo"),
              ("multi_norma", "de varias normas"),
              ("cadena_restriccion_excepcion", "de restricción hasta su excepción"),
              ("unanswerable", "sin respuesta"))
# Operación del agente y la herramienta que la implementa, en el orden de la
# lista de herramientas.
OPERACIONES = (("buscar", "buscar_nodos"), ("abrir", "ver_nodo"), ("listar vecinos", "ver_vecinos"))

TEXTO = {
    "conjunto_titulo": "Conjunto de desarrollo",
    "conjunto_tos": "5 Textos Ordenados",
    "estrategias_encabezado": "5 estrategias de esquema",
    "grafos_encabezado": "5 grafos",
    "preguntas_titulo": "23 preguntas",
    "preguntas_reparto": ("10 de dato directo, 5 de varias normas, "
                          "4 de restricción hasta su excepción, 4 sin respuesta"),
    "agente_titulo": "Agente",
    "agente_operaciones": "3 operaciones: buscar, abrir, listar vecinos",
    "agente_tope": "tope de 15 llamadas",
    "respuestas": "3 respuestas por pregunta y grafo",
    "juez_titulo": "Juez",
    "juez_pasos": "2 pasos: descompone en afirmaciones y las verifica contra la referencia",
    "revision_titulo": "Afirmaciones que la referencia no decide",
    "revision_texto": "revisadas contra los Textos Ordenados",
    "medidas_titulo": "4 medidas",
    "medidas_lista": ", ".join(MEDIDAS),
}
# Cortes de línea fijados a mano; las listas se cortan en sus elementos.
SEPARADOR = {"preguntas_reparto": ", ", "medidas_lista": ", "}
CORTES = {
    "conjunto_titulo": ("Conjunto de", "desarrollo"),
    "conjunto_tos": ("5 Textos", "Ordenados"),
    "preguntas_reparto": ("10 de dato directo", "5 de varias normas",
                          "4 de restricción hasta su excepción", "4 sin respuesta"),
    "agente_operaciones": ("3 operaciones: buscar,", "abrir, listar vecinos"),
    "respuestas": ("3 respuestas", "por pregunta y grafo"),
    "juez_pasos": ("2 pasos: descompone en", "afirmaciones y las verifica", "contra la referencia"),
    "medidas_lista": MEDIDAS,
}
# Contenido de cada caja: piezas de TEXTO, con el estilo de cada línea
# («titulo», en negrita; «texto», normal). En «respuestas» la primera línea es
# el rótulo y la segunda el texto.
BLOQUES = {
    "conjunto": (("conjunto_titulo", "titulo"), ("conjunto_tos", "texto")),
    "preguntas": (("preguntas_titulo", "titulo"), ("preguntas_reparto", "texto")),
    "agente": (("agente_titulo", "titulo"), ("agente_operaciones", "texto"), ("agente_tope", "texto")),
    "respuestas": (("respuestas", ("titulo", "texto")),),
    "juez": (("juez_titulo", "titulo"), ("juez_pasos", "texto")),
    "revision": (("revision_titulo", "titulo"), ("revision_texto", "texto")),
    "medidas": (("medidas_titulo", "titulo"), ("medidas_lista", "texto")),
}
LEYENDA = proc.LEYENDA      # la misma leyenda, con el mismo texto
# Nada de esto puede aparecer en un texto dibujado.
PROHIBIDOS = (re.compile(r"run", re.I), re.compile(r"\bCQ", re.I), re.compile(r"unans", re.I),
              re.compile(r"\.(json|py|pdf|md|tex)\b"), re.compile(r"[/\\]"), re.compile(r"::"),
              re.compile(r"_"), re.compile(r"\b[0-9a-f]{7,40}\b"),
              re.compile(r"cookbook|papers|ppf|schema|hybrid|frozen|harness|judge", re.I))

# --------------------------------------------------------------------------- #
# Tamaño impreso: 15 cm de ancho                                               #
# --------------------------------------------------------------------------- #
W = 760                                               # unidades de lienzo
ANCHO_FIGURA_CM = proc.ANCHO_TEXTO_CM                 # 15,00
ANCHO_FIGURA_PT = ANCHO_FIGURA_CM * proc.PT_POR_CM    # 425,2
DPI = proc.DPI                                        # 300
ANCHO_PNG_PX = round(ANCHO_FIGURA_CM / 2.54 * DPI)    # 1772
PT_MINIMO = 7.0
MARGEN_MM = 2.0
MARGEN_MIN = MARGEN_MM * W / (ANCHO_FIGURA_CM * 10)   # 10,1 unidades
MARGEN = 12                                           # 2,37 mm


def puntos_impresos(unidades):
    """Tamaño en puntos de `unidades` del lienzo con la figura a 15 cm."""
    return unidades * ANCHO_FIGURA_PT / W


# --------------------------------------------------------------------------- #
# Paleta y tipografía (las de generar_figura_proceso_extraccion.py)            #
# --------------------------------------------------------------------------- #
TIPOGRAFIA = base.TIPOGRAFIA
MODELO, DETERMINISTICA, NEUTRO = proc.MODELO, proc.DETERMINISTICA, proc.NEUTRO
DISCONTINUA = {"relleno": "white", "borde": proc.GRIS_ARISTA}   # la caja lateral
TINTA, TINTA_SUB = proc.TINTA, proc.TINTA_SUB
FLECHA, GRIS_ARISTA = proc.FLECHA, proc.GRIS_ARISTA
GRIS_RENGLON = "#c4c4c4"
COLOR_NODO = DETERMINISTICA["borde"]
esc, f = base.esc, base.f

FS_TITULO = 14          # rótulos de caja y encabezados, en negrita (7,83 pt)
FS_TEXTO = 13           # texto de caja, nombres de estrategia y leyenda (7,27 pt)
IL = {FS_TITULO: 18, FS_TEXTO: 17}
SEP_TITULO = 5          # entre el rótulo y el texto de una caja
SEP_GRUPO = 4           # entre dos piezas de texto de una caja
PAD_X, PAD_Y = 9, 11
GROSOR_CAJA = 1.6
GROSOR_FLUJO = 1.8      # flechas entre etapas
GROSOR_RAMA = 1.6       # reparto, estrategia a grafo, colector y trazos discontinuos
RADIO = 9               # esquinas de los trazos

# --------------------------------------------------------------------------- #
# Geometría                                                                    #
# --------------------------------------------------------------------------- #
# Fila de arriba.
X_DOC, W_DOC = MARGEN, 112
Y_TEXTO_DOC = 62        # del borde superior de la hoja al texto, debajo de los renglones
X_BARRA = X_DOC + W_DOC + 18
X_EST, W_EST, H_EST, SEP_EST = X_BARRA + 22, 170, 28, 8
X_GRAF, W_GRAF = X_EST + W_EST + 26, 64
X_COL = X_GRAF + W_GRAF + 16
NODOS_GLIFO = ((14, 19), (32, 9), (50, 19))
ARISTAS_GLIFO = ((0, 1), (1, 2), (0, 2))
R_NODO = 3.6
# Conectores entre filas: el de los grafos va por arriba y entra al agente más
# a la izquierda que el de las preguntas, así que no se cruzan.
BAJO_COLUMNA = 20       # de la última estrategia al conector de los grafos
ENTRE_CONECTORES = 12
SOBRE_FILA = 24         # del conector de las preguntas a la fila de abajo
DX_ENTRADA = (48, 112)  # entradas al agente, desde su borde izquierdo
# Fila de abajo.
FILA2 = (("agente", 160, MODELO), ("respuestas", 136, NEUTRO), ("juez", 172, MODELO),
         ("medidas", 154, DETERMINISTICA))
CARRIL = 24             # a la derecha de las medidas, para la flecha de la revisión
BAJO_FILA = 30          # de la fila de abajo a la revisión y a la leyenda
SEP_LEYENDA = 24        # entre la leyenda y la revisión
DISTANCIA_MIN = 3.0     # entre los ejes de dos trazos de grupos distintos
HOLGURA_TEXTO = 1.5     # de un texto a una marca, un trazo o el borde de su caja

# --------------------------------------------------------------------------- #
# Fuentes                                                                      #
# --------------------------------------------------------------------------- #
def sha256(ruta):
    with open(ruta, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def freno(motivo):
    raise SystemExit(f"FRENO: {motivo}")


def leer(clave):
    rel, esperado = FUENTES[clave]
    with open(os.path.join(RAIZ, rel), "rb") as fh:
        crudo = fh.read()
    sha = hashlib.sha256(crudo).hexdigest()
    if sha != esperado:
        freno(f"{rel} no es el verificado: sha256 {sha[:12]}… ≠ {esperado[:12]}…")
    return crudo.decode("utf-8")


def unico(patron, texto, clave):
    hallados = re.findall(patron, texto, re.M)
    if len(hallados) != 1:
        freno(f"{FUENTES[clave][0]}: {len(hallados)} coincidencias de {patron!r}, no una")
    return hallados[0]


def comprobar_fuentes():
    """Lee cada fuente con su candado y devuelve los hechos que la figura afirma."""
    h = {}
    ev = json.loads(leer("preguntas"))
    meta = ev["metadata"]
    cats = Counter(p["categoria"] for p in ev["preguntas"])
    if len(ev["preguntas"]) != meta["total"] or dict(cats) != meta["distribucion"]:
        freno("las preguntas del conjunto no coinciden con su total o su distribución declarados")
    if set(cats) != {c for c, _ in CATEGORIAS}:
        freno(f"categorías del conjunto {sorted(cats)} ≠ las de la figura")
    h["tos"] = len(meta["corpus"])
    h["preguntas"] = meta["total"]
    h["reparto"] = [(cats[c], rotulo) for c, rotulo in CATEGORIAS]
    ids = {p["id"] for p in ev["preguntas"]}

    ag = leer("agente")
    h["tope"] = int(unico(r"^MAX_TOOL_CALLS = (\d+)$", ag, "agente"))
    h["herramientas"] = re.findall(r'^        "name": "(\w+)",$', ag, re.M)
    if h["herramientas"] != [t for _, t in OPERACIONES]:
        freno(f"herramientas del agente {h['herramientas']} ≠ las de la figura")
    # El tope se controla al cerrar cada turno (por eso una repetición puede
    # pasar de 15 llamadas; el LEEME lo cuenta).
    unico(r"^ +if tr\.tool_calls_used >= MAX_TOOL_CALLS:$", ag, "agente")

    ju = leer("juez")
    h["pasos"] = re.findall(r"^# Paso (\d+) — ", ju, re.M)
    if h["pasos"] != ["1", "2"]:
        freno(f"bloques de pasos del juez {h['pasos']} ≠ ['1', '2']")
    if "requiere_adjudicacion_humana=true" not in ju:
        freno("el juez no declara la cola de adjudicación de las afirmaciones no soportadas")

    co = leer("corrida")
    h["repeticiones"] = int(unico(r'add_argument\("--N", type=int, default=(\d+)\)', co, "corrida"))
    trazas = os.path.join(RAIZ, REL_TRAZAS)
    carpetas = sorted(d for d in os.listdir(trazas) if os.path.isdir(os.path.join(trazas, d)))
    h["grafos"] = len(carpetas)
    if len(carpetas) != len(ESTRATEGIAS):
        freno(f"{len(carpetas)} carpetas de trazas para {len(ESTRATEGIAS)} estrategias")
    for (nombre, carpeta), d in zip(ESTRATEGIAS, carpetas):
        if not carpeta.startswith(d + "_"):
            freno(f"la estrategia {nombre!r} ({carpeta}) no corresponde a las trazas de {d}")
        if not os.path.isfile(os.path.join(RAIZ, "data/experiment", carpeta, "kg.json")):
            freno(f"falta el grafo de la estrategia {nombre!r}")
    h["corridas"] = 0
    for d in carpetas:
        archivos = sorted(a for a in os.listdir(os.path.join(trazas, d)) if a.endswith(".json"))
        if {a[:-5] for a in archivos} != ids:
            freno(f"las trazas de {d} no son las {len(ids)} preguntas del conjunto")
        for a in archivos:
            with open(os.path.join(trazas, d, a), encoding="utf-8") as fh:
                reps = json.load(fh)
            if sorted(r["rep"] for r in reps) != list(range(1, h["repeticiones"] + 1)):
                freno(f"{d}/{a}: repeticiones {[r['rep'] for r in reps]}")
            h["corridas"] += len(reps)

    rv = json.loads(leer("revision"))
    adj = rv["meta"]["adjudicacion"]
    if adj["estado"] != "firmado" or f"contra los {h['tos']} PDFs del subset" not in adj["metodo"]:
        freno("la adjudicación no está firmada o no declara la revisión contra los Textos Ordenados")
    h["metodo_revision"] = adj["metodo"]
    h["afirmaciones_revisadas"] = rv["meta"]["afirmaciones_unicas_tras_agrupado"]

    lineas = leer("reporte").splitlines()
    for linea in (REPORTE_CORRECTAS, REPORTE_NO_AFECTADAS, REPORTE_DIMENSIONES):
        if linea not in lineas:
            freno(f"el reporte final no tiene la línea {linea!r}")
    h["lineas_reporte"] = [lineas.index(x) + 1 for x in
                           (REPORTE_CORRECTAS, REPORTE_NO_AFECTADAS, REPORTE_DIMENSIONES)]
    return h


def numero(clave):
    return int(TEXTO[clave].split()[0])


def cotejar_texto(h):
    """Cada número del texto fijado contra su fuente; los cortes no cambian el texto."""
    fallas = []

    def igual(que, a, b):
        if a != b:
            fallas.append(f"{que}: {a!r} ≠ {b!r}")
    igual("Textos Ordenados", numero("conjunto_tos"), h["tos"])
    igual("estrategias", numero("estrategias_encabezado"), len(ESTRATEGIAS))
    igual("grafos", numero("grafos_encabezado"), h["grafos"])
    igual("preguntas", numero("preguntas_titulo"), h["preguntas"])
    igual("reparto", TEXTO["preguntas_reparto"], ", ".join(f"{n} {r}" for n, r in h["reparto"]))
    igual("operaciones", TEXTO["agente_operaciones"],
          f"{len(h['herramientas'])} operaciones: " + ", ".join(o for o, _ in OPERACIONES))
    igual("tope", TEXTO["agente_tope"], f"tope de {h['tope']} llamadas")
    igual("respuestas", TEXTO["respuestas"], f"{h['repeticiones']} respuestas por pregunta y grafo")
    igual("pasos del juez", numero("juez_pasos"), len(h["pasos"]))
    igual("medidas", numero("medidas_titulo"), len(MEDIDAS))
    igual("corridas", h["corridas"], h["grafos"] * h["preguntas"] * h["repeticiones"])
    for clave, lineas in CORTES.items():
        igual(f"cortes de {clave}", SEPARADOR.get(clave, " ").join(lineas), TEXTO[clave])
    if fallas:
        freno("el texto de la figura no coincide con sus fuentes:\n  " + "\n  ".join(fallas))


# --------------------------------------------------------------------------- #
# Primitivas de dibujo: todo lo que se dibuja queda registrado                 #
# --------------------------------------------------------------------------- #
REGISTRO = []     # textos
CAJAS = {}        # clave -> caja (x0, y0, x1, y1), con el grosor de su borde
MARCAS = []       # (nombre, caja): renglones, pliegue, nodos y aristas de los grafos
TRAZOS = []       # {grupo, nombre, puntos, grosor, punta}
DIBUJADOS = []    # etiqueta de cada elemento, en el orden del SVG
MEDIR = None      # métricas reales de Helvetica (proc.medidor)


def lineas_de(clave):
    return CORTES.get(clave, (TEXTO[clave],))


def texto(partes, x, y, s, fs, negrita, relleno, dentro, pieza, ancla="middle"):
    peso = "bold" if negrita else "normal"
    anc = "" if ancla == "start" else f' text-anchor="{ancla}"'
    partes.append(f'<text x="{f(x)}" y="{f(y)}"{anc} font-size="{fs}" font-weight="{peso}" '
                  f'fill="{relleno}">{esc(s)}</text>')
    DIBUJADOS.append("text")
    REGISTRO.append({"s": s, "fs": fs, "negrita": negrita, "x": float(f(x)), "y": float(f(y)),
                     "ancla": ancla, "dentro": dentro, "pieza": pieza})


def caja(partes, clave, x, y, w, h, clase, grosor=GROSOR_CAJA, rx=8, guiones=False):
    dash = ' stroke-dasharray="5,4"' if guiones else ""
    partes.append(f'<rect x="{f(x)}" y="{f(y)}" width="{f(w)}" height="{f(h)}" '
                  f'fill="{clase["relleno"]}" stroke="{clase["borde"]}" '
                  f'stroke-width="{grosor}" rx="{rx}"{dash}/>')
    DIBUJADOS.append("rect")
    x, y, w, h = (float(f(v)) for v in (x, y, w, h))
    CAJAS[clave] = {"bb": (x, y, x + w, y + h), "grosor": grosor}


def marca_trazo(partes, nombre, puntos, color, grosor, cap=""):
    d = " ".join(("M" if i == 0 else "L") + f"{f(x)},{f(y)}" for i, (x, y) in enumerate(puntos))
    extra = f' stroke-linecap="{cap}"' if cap else ""
    partes.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{grosor}"{extra}/>')
    DIBUJADOS.append("path")
    xs = [float(f(x)) for x, _ in puntos]
    ys = [float(f(y)) for _, y in puntos]
    m = grosor / 2.0
    MARCAS.append((nombre, (min(xs) - m, min(ys) - m, max(xs) + m, max(ys) + m)))


def trazo(partes, grupo, nombre, puntos, color, grosor, marcador=None, guiones=False):
    """Poligonal con esquinas redondeadas (las de proc.trazo) y punta de flecha
    opcional. Registra la geometría real: los tramos rectos y cada esquina
    muestreada en diez puntos de su curva."""
    puntos = [(float(f(x)), float(f(y))) for x, y in puntos]
    d = f"M{f(puntos[0][0])},{f(puntos[0][1])}"
    muestra = [puntos[0]]
    for i in range(1, len(puntos) - 1):
        (x0, y0), (x1, y1), (x2, y2) = puntos[i - 1], puntos[i], puntos[i + 1]

        def hacia(xa, ya, xb, yb):
            largo = math.hypot(xb - xa, yb - ya)
            r = min(RADIO, largo / 2.0)
            return xa + (xb - xa) * r / largo, ya + (yb - ya) * r / largo

        ex, ey = (float(f(v)) for v in hacia(x1, y1, x0, y0))
        sx, sy = (float(f(v)) for v in hacia(x1, y1, x2, y2))
        d += f" L{f(ex)},{f(ey)} Q{f(x1)},{f(y1)} {f(sx)},{f(sy)}"
        muestra.append((ex, ey))
        for k in range(1, 11):
            t = k / 10.0
            muestra.append(((1 - t) ** 2 * ex + 2 * (1 - t) * t * x1 + t * t * sx,
                            (1 - t) ** 2 * ey + 2 * (1 - t) * t * y1 + t * t * sy))
    d += f" L{f(puntos[-1][0])},{f(puntos[-1][1])}"
    muestra.append(puntos[-1])
    dash = ' stroke-dasharray="5,4"' if guiones else ""
    mk = f' marker-end="url(#{marcador})"' if marcador else ""
    partes.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{grosor}"{dash}{mk}/>')
    DIBUJADOS.append("path")
    punta = None
    if marcador:
        # Marcador de 10 × 10 con refX 9, dibujado a 6 veces el grosor: la punta
        # queda una décima de su largo más allá del final del trazo.
        (xa, ya), (xb, yb) = puntos[-2], puntos[-1]
        largo = math.hypot(xb - xa, yb - ya)
        ux, uy = (xb - xa) / largo, (yb - ya) / largo
        lp = 6 * grosor
        tip = (xb + 0.1 * lp * ux, yb + 0.1 * lp * uy)
        bx, by = xb - 0.9 * lp * ux, yb - 0.9 * lp * uy
        punta = (tip, (bx - 0.5 * lp * uy, by + 0.5 * lp * ux), (bx + 0.5 * lp * uy, by - 0.5 * lp * ux))
    TRAZOS.append({"grupo": grupo, "nombre": nombre, "puntos": muestra, "grosor": grosor,
                   "punta": punta})


def circulo(partes, nombre, cx, cy, r, relleno):
    partes.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{r}" fill="{relleno}"/>')
    DIBUJADOS.append("circle")
    cx, cy = float(f(cx)), float(f(cy))
    MARCAS.append((nombre, (cx - r, cy - r, cx + r, cy + r)))


# --------------------------------------------------------------------------- #
# Contenido de las cajas                                                       #
# --------------------------------------------------------------------------- #
def renglones(clave):
    """Líneas de la caja: (texto, fs, negrita, color, pieza, separación previa)."""
    out, previo = [], None
    for k, (pieza, estilo) in enumerate(BLOQUES[clave]):
        lineas = lineas_de(pieza)
        estilos = estilo if isinstance(estilo, tuple) else (estilo,) * len(lineas)
        for i, (s, e) in enumerate(zip(lineas, estilos)):
            if previo is None:
                sep = 0
            elif previo == "titulo" and e == "texto":
                sep = SEP_TITULO
            elif i == 0 and k > 0:
                sep = SEP_GRUPO
            else:
                sep = 0
            fs = FS_TITULO if e == "titulo" else FS_TEXTO
            out.append((s, fs, e == "titulo", TINTA if e == "titulo" else TINTA_SUB,
                        (pieza, i), sep))
            previo = e
    return out


def alto_contenido(clave):
    return sum(sep + IL[fs] for _, fs, _, _, _, sep in renglones(clave))


def ancho_contenido(clave):
    return max(MEDIR(s, fs, b) for s, fs, b, _, _, _ in renglones(clave))


def escribir(partes, clave, cx, y_arriba):
    """Escribe las líneas de la caja centradas en cx desde y_arriba; devuelve
    la línea de base de cada línea, por pieza."""
    bases, yy = {}, y_arriba
    for s, fs, negrita, color, pieza, sep in renglones(clave):
        yy += sep
        base_y = yy + (IL[fs] - fs) / 2.0 + 0.78 * fs
        texto(partes, cx, base_y, s, fs, negrita, color, clave, pieza)
        bases[pieza] = base_y
        yy += IL[fs]
    return bases


def caja_con_texto(partes, clave, x, y, w, h, clase, **kw):
    caja(partes, clave, x, y, w, h, clase, **kw)
    return escribir(partes, clave, x + w / 2.0, y + (h - alto_contenido(clave)) / 2.0)


def dibujar_documento(partes, x, y, w, h):
    """La hoja con la esquina plegada y cuatro renglones (la de proc), con el
    texto debajo de los renglones."""
    p = 20
    partes.append(f'<path d="M{f(x + 4)},{f(y)} L{f(x + w - p)},{f(y)} '
                  f'L{f(x + w)},{f(y + p)} L{f(x + w)},{f(y + h - 4)} '
                  f'Q{f(x + w)},{f(y + h)} {f(x + w - 4)},{f(y + h)} '
                  f'L{f(x + 4)},{f(y + h)} Q{f(x)},{f(y + h)} {f(x)},{f(y + h - 4)} '
                  f'L{f(x)},{f(y + 4)} Q{f(x)},{f(y)} {f(x + 4)},{f(y)} Z" '
                  f'fill="{NEUTRO["relleno"]}" stroke="{NEUTRO["borde"]}" '
                  f'stroke-width="{GROSOR_CAJA}"/>')
    DIBUJADOS.append("path")
    xf, yf, wf, hf = (float(f(v)) for v in (x, y, w, h))
    CAJAS["conjunto"] = {"bb": (xf, yf, xf + wf, yf + hf), "grosor": GROSOR_CAJA}
    marca_trazo(partes, "pliegue", [(x + w - p, y), (x + w - p, y + p), (x + w, y + p)],
                NEUTRO["borde"], GROSOR_CAJA)
    for k, largo in enumerate((0.52, 0.76, 0.76, 0.60)):
        yy = y + 20 + k * 10
        marca_trazo(partes, f"renglón {k + 1}", [(x + 12, yy), (x + 12 + (w - 24) * largo, yy)],
                    GRIS_RENGLON, 3, cap="round")
    # La punta redondeada del renglón sobresale medio grosor a cada lado.
    for k in range(4):
        nombre, (a, b, c, d) = MARCAS[-4 + k]
        MARCAS[-4 + k] = (nombre, (a - 1.5, b, c + 1.5, d))
    return escribir(partes, "conjunto", x + w / 2.0, y + Y_TEXTO_DOC)


def dibujar_grafo(partes, i, x, y):
    """Un grafo: caja neutra con tres nodos y tres aristas."""
    caja(partes, f"grafo {i + 1}", x, y, W_GRAF, H_EST, NEUTRO)
    for a, b in ARISTAS_GLIFO:
        (xa, ya), (xb, yb) = NODOS_GLIFO[a], NODOS_GLIFO[b]
        marca_trazo(partes, f"grafo {i + 1}, arista {a + 1}-{b + 1}",
                    [(x + xa, y + ya), (x + xb, y + yb)], GRIS_ARISTA, 1.3)
    for k, (dx, dy) in enumerate(NODOS_GLIFO):
        circulo(partes, f"grafo {i + 1}, nodo {k + 1}", x + dx, y + dy, R_NODO, COLOR_NODO)


# --------------------------------------------------------------------------- #
# Composición                                                                  #
# --------------------------------------------------------------------------- #
def componer():
    del REGISTRO[:]
    CAJAS.clear()
    del MARCAS[:]
    del TRAZOS[:]
    del DIBUJADOS[:]
    partes = []
    geo = {}

    # ---- fila de arriba: encabezados, conjunto, estrategias, grafos -------- #
    y_enc = MARGEN + 0.78 * FS_TITULO + 2
    texto(partes, X_EST + W_EST / 2.0, y_enc, TEXTO["estrategias_encabezado"], FS_TITULO, True,
          TINTA, None, ("estrategias_encabezado", 0))
    texto(partes, X_GRAF + W_GRAF / 2.0, y_enc, TEXTO["grafos_encabezado"], FS_TITULO, True,
          TINTA, None, ("grafos_encabezado", 0))
    y_col = y_enc + 0.22 * FS_TITULO + 10
    centros = [y_col + H_EST / 2.0 + i * (H_EST + SEP_EST) for i in range(len(ESTRATEGIAS))]
    y_bajo_col = centros[-1] + H_EST / 2.0
    cy = (centros[0] + centros[-1]) / 2.0          # centro de la columna = tercera estrategia

    alto_doc = Y_TEXTO_DOC + alto_contenido("conjunto") + PAD_Y
    dibujar_documento(partes, X_DOC, cy - alto_doc / 2.0, W_DOC, alto_doc)

    # Reparto del conjunto a las cinco estrategias: la línea del medio sigue
    # derecho a la tercera; la primera y la última doblan desde la barra.
    trazo(partes, "reparto", "del conjunto a la estrategia 3", [(X_DOC + W_DOC, cy), (X_EST - 2, cy)],
          FLECHA, GROSOR_RAMA, "arN")
    for i in (0, len(centros) - 1):
        trazo(partes, "reparto", f"a la estrategia {i + 1}",
              [(X_BARRA, cy), (X_BARRA, centros[i]), (X_EST - 2, centros[i])], FLECHA, GROSOR_RAMA, "arN")
    for i in range(1, len(centros) - 1):
        if centros[i] != cy:
            trazo(partes, "reparto", f"a la estrategia {i + 1}", [(X_BARRA, centros[i]), (X_EST - 2, centros[i])],
                  FLECHA, GROSOR_RAMA, "arN")

    y_c1 = y_bajo_col + BAJO_COLUMNA
    y_c2 = y_c1 + ENTRE_CONECTORES
    y2 = y_c2 + SOBRE_FILA
    for i, (nombre, _) in enumerate(ESTRATEGIAS):
        c = centros[i]
        caja(partes, f"estrategia {i + 1}", X_EST, c - H_EST / 2.0, W_EST, H_EST, MODELO)
        texto(partes, X_EST + W_EST / 2.0, c + 0.28 * FS_TEXTO, nombre, FS_TEXTO, True, TINTA,
              f"estrategia {i + 1}", ("estrategia", i))
        trazo(partes, f"estrategia {i + 1} a su grafo", f"de la estrategia {i + 1} a su grafo",
              [(X_EST + W_EST + 2, c), (X_GRAF - 2, c)], FLECHA, GROSOR_RAMA, "arN")
        dibujar_grafo(partes, i, X_GRAF, c - H_EST / 2.0)
    # Colector de los grafos, que baja y entra al agente por arriba.
    x_ag = MARGEN
    trazo(partes, "colector", "de los grafos al agente",
          [(X_GRAF + W_GRAF, centros[0]), (X_COL, centros[0]), (X_COL, y_c1),
           (x_ag + DX_ENTRADA[0], y_c1), (x_ag + DX_ENTRADA[0], y2 - 2)], FLECHA, GROSOR_FLUJO, "arN")
    for i in range(1, len(centros)):
        trazo(partes, "colector", f"del grafo {i + 1} al colector",
              [(X_GRAF + W_GRAF, centros[i]), (X_COL, centros[i])], FLECHA, GROSOR_RAMA)

    # ---- preguntas, a la derecha de la fila de arriba ---------------------- #
    w_pre = math.ceil(ancho_contenido("preguntas") + 2 * PAD_X + 2)
    x_pre = W - MARGEN - w_pre
    alto_pre = alto_contenido("preguntas") + 2 * PAD_Y
    y_pre = cy - alto_pre / 2.0
    caja_con_texto(partes, "preguntas", x_pre, y_pre, w_pre, alto_pre, NEUTRO)
    cx_pre = x_pre + w_pre / 2.0
    trazo(partes, "preguntas", "de las preguntas al agente",
          [(cx_pre, y_pre + alto_pre), (cx_pre, y_c2), (x_ag + DX_ENTRADA[1], y_c2),
           (x_ag + DX_ENTRADA[1], y2 - 2)], FLECHA, GROSOR_FLUJO, "arN")

    # ---- fila de abajo: agente, respuestas, juez, medidas ------------------ #
    h2 = max(alto_contenido(k) for k, _, _ in FILA2) + 2 * PAD_Y
    libre = W - 2 * MARGEN - CARRIL - sum(w for _, w, _ in FILA2)
    sep2 = libre / (len(FILA2) - 1)
    cy2 = y2 + h2 / 2.0
    x, pos, bases = x_ag, {}, {}
    for k, (clave, w, clase) in enumerate(FILA2):
        bases[clave] = caja_con_texto(partes, clave, x, y2, w, h2, clase)
        pos[clave] = (x, w)
        if k > 0:
            xa = pos[FILA2[k - 1][0]][0] + pos[FILA2[k - 1][0]][1]
            trazo(partes, f"flujo {k}", f"de {FILA2[k - 1][0]} a {clave}",
                  [(xa + 2, cy2), (x - 2, cy2)], FLECHA, GROSOR_FLUJO, "arN")
        x += w + sep2

    # ---- leyenda (abajo a la izquierda) y revisión (debajo del juez) -------- #
    y3 = y2 + h2 + BAJO_FILA
    muestra_w, muestra_h, fila_ley = 24, 16, 22
    w_ley = 12 + muestra_w + 9 + max(MEDIR(s, FS_TEXTO, False) for _, s in LEYENDA) + 12
    h_ley = 10 + len(LEYENDA) * fila_ley + 6
    partes.append(f'<rect x="{f(MARGEN)}" y="{f(y3)}" width="{f(w_ley)}" height="{f(h_ley)}" '
                  f'fill="white" stroke="#e2e2e2" stroke-width="1" rx="5"/>')
    DIBUJADOS.append("rect")
    CAJAS["leyenda"] = {"bb": (float(f(MARGEN)), float(f(y3)), float(f(MARGEN)) + float(f(w_ley)),
                               float(f(y3)) + float(f(h_ley))), "grosor": 1.0}
    for k, (clase, rotulo) in enumerate(LEYENDA):
        yc = y3 + 10 + k * fila_ley + fila_ley / 2.0
        caja(partes, f"leyenda, muestra {k + 1}", MARGEN + 12, yc - muestra_h / 2.0, muestra_w, muestra_h,
             clase, rx=3)
        texto(partes, MARGEN + 12 + muestra_w + 9, yc + 0.28 * FS_TEXTO, rotulo, FS_TEXTO, False, TINTA,
              "leyenda", ("leyenda", k), ancla="start")

    x_ju, w_ju = pos["juez"]
    cx_ju = x_ju + w_ju / 2.0
    w_rev = math.ceil(ancho_contenido("revision") + 2 * PAD_X + 2)
    x_rev = max(MARGEN + w_ley + SEP_LEYENDA, cx_ju - w_rev / 2.0)
    alto_rev = alto_contenido("revision") + 2 * PAD_Y
    if not x_rev + 20 <= cx_ju <= x_rev + w_rev - 20:
        freno("la flecha del juez no cae sobre la caja de la revisión")
    caja_con_texto(partes, "revision", x_rev, y3, w_rev, alto_rev, DISCONTINUA, grosor=1.3, guiones=True)
    trazo(partes, "juez a revisión", "del juez a la revisión", [(cx_ju, y2 + h2), (cx_ju, y3 - 2)],
          GRIS_ARISTA, GROSOR_RAMA, "arG", guiones=True)
    x_me, w_me = pos["medidas"]
    y_corr = bases["medidas"][("medidas_lista", 0)] - 0.28 * FS_TEXTO
    x_carril = x_me + w_me + CARRIL / 2.0
    cy_rev = y3 + alto_rev / 2.0
    trazo(partes, "revisión a correctas", "de la revisión a «correctas»",
          [(x_rev + w_rev, cy_rev), (x_carril, cy_rev), (x_carril, y_corr), (x_me + w_me + 2, y_corr)],
          GRIS_ARISTA, GROSOR_RAMA, "arG", guiones=True)

    alto_total = math.ceil(max(y3 + alto_rev, y3 + h_ley) + MARGEN)
    geo.update({"alto": alto_total, "fila2": pos, "sep2": sep2, "h2": h2, "w_pre": w_pre,
                "w_rev": w_rev, "x_rev": x_rev, "w_ley": w_ley})

    alto_cm = ANCHO_FIGURA_CM * alto_total / W
    cabeza = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{ANCHO_FIGURA_CM:.2f}cm" '
        f'height="{alto_cm:.2f}cm" viewBox="0 0 {W} {alto_total}" font-family="{TIPOGRAFIA}">',
        f'<rect width="{W}" height="{alto_total}" fill="white"/>',
        '<defs>'
        '<marker id="arN" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
        f'markerHeight="6" orient="auto"><path d="M0,0L10,5L0,10z" fill="{FLECHA}"/></marker>'
        '<marker id="arG" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
        f'markerHeight="6" orient="auto"><path d="M0,0L10,5L0,10z" fill="{GRIS_ARISTA}"/></marker>'
        '</defs>',
    ]
    return "\n".join(cabeza + partes + ["</svg>"]) + "\n", geo


# --------------------------------------------------------------------------- #
# Controles                                                                    #
# --------------------------------------------------------------------------- #
def cruza(a, b):
    return a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]


def contiene(c, b, holgura=0.0):
    return (c[0] + holgura <= b[0] and b[2] <= c[2] - holgura
            and c[1] + holgura <= b[1] and b[3] <= c[3] - holgura)


def ampliar(b, d):
    return (b[0] - d, b[1] - d, b[2] + d, b[3] + d)


def caja_texto(r):
    a = MEDIR(r["s"], r["fs"], r["negrita"])
    x0 = {"start": r["x"], "middle": r["x"] - a / 2.0, "end": r["x"] - a}[r["ancla"]]
    return (x0, r["y"] - r["fs"] * 0.78, x0 + a, r["y"] + r["fs"] * 0.22)


def corta(p, q, r):
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


def distancia_punto_segmento(p, q0, q1):
    dx, dy = q1[0] - q0[0], q1[1] - q0[1]
    largo2 = dx * dx + dy * dy
    t = 0.0 if largo2 == 0 else max(0.0, min(1.0, ((p[0] - q0[0]) * dx + (p[1] - q0[1]) * dy) / largo2))
    return math.hypot(p[0] - q0[0] - t * dx, p[1] - q0[1] - t * dy)


def distancia_punto_caja(p, r):
    return math.hypot(max(r[0] - p[0], 0.0, p[0] - r[2]), max(r[1] - p[1], 0.0, p[1] - r[3]))


def distancia_segmento_caja(p, q, r):
    if corta(p, q, r) or contiene(r, (p[0], p[1], p[0], p[1])):
        return 0.0
    esquinas = ((r[0], r[1]), (r[2], r[1]), (r[0], r[3]), (r[2], r[3]))
    return min([distancia_punto_caja(p, r), distancia_punto_caja(q, r)]
               + [distancia_punto_segmento(e, p, q) for e in esquinas])


def distancia_segmentos(a0, a1, b0, b1):
    def orientacion(p, q, r):
        v = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
        return (v > 0) - (v < 0)
    o = (orientacion(a0, a1, b0), orientacion(a0, a1, b1), orientacion(b0, b1, a0),
         orientacion(b0, b1, a1))
    if o[0] != o[1] and o[2] != o[3] and 0 not in o:
        return 0.0
    return min(distancia_punto_segmento(a0, b0, b1), distancia_punto_segmento(a1, b0, b1),
               distancia_punto_segmento(b0, a0, a1), distancia_punto_segmento(b1, a0, a1))


def caja_punta(t):
    xs = [p[0] for p in t["punta"]]
    ys = [p[1] for p in t["punta"]]
    return (min(xs), min(ys), max(xs), max(ys))


def segmentos(t):
    return list(zip(t["puntos"], t["puntos"][1:]))


def controlar_contenido():
    """Lo dibujado reconstruye el texto fijado y no lleva nada prohibido."""
    fallas = []
    por_pieza = {}
    for r in REGISTRO:
        por_pieza.setdefault(r["pieza"][0], []).append((r["pieza"][1], r["s"]))
        for rx in PROHIBIDOS:
            if rx.search(r["s"]):
                fallas.append(f"{r['s']!r} lleva {rx.pattern!r}")
    for clave in TEXTO:
        dibujado = SEPARADOR.get(clave, " ").join(s for _, s in sorted(por_pieza.pop(clave, [])))
        if dibujado != TEXTO[clave]:
            fallas.append(f"{clave}: dibujado {dibujado!r} ≠ fijado {TEXTO[clave]!r}")
    for clave, esperado in (("estrategia", [n for n, _ in ESTRATEGIAS]),
                            ("leyenda", [s for _, s in LEYENDA])):
        dibujado = [s for _, s in sorted(por_pieza.pop(clave, []))]
        if dibujado != esperado:
            fallas.append(f"{clave}: dibujado {dibujado!r} ≠ fijado {esperado!r}")
    for clave in por_pieza:
        fallas.append(f"texto dibujado sin pieza fijada: {clave}")
    return fallas


def controlar_textos(alto_total):
    fallas, tamanos = [], {}
    cajas_t = [(r, caja_texto(r)) for r in REGISTRO]
    minimos = {"texto-texto": math.inf, "texto-trazo": math.inf, "texto-marca": math.inf,
               "texto-borde de su caja": math.inf}
    for r, bb in cajas_t:
        pt = puntos_impresos(r["fs"])
        tamanos[r["fs"]] = pt
        if pt < PT_MINIMO:
            fallas.append(f"{r['s']!r}: letra {pt:.2f} pt < {PT_MINIMO}")
        if bb[0] < 0 or bb[2] > W or bb[1] < 0 or bb[3] > alto_total:
            fallas.append(f"{r['s']!r}: fuera del lienzo")
        if r["dentro"] is not None:
            c = CAJAS[r["dentro"]]["bb"]
            holg = min(bb[0] - c[0], c[2] - bb[2], bb[1] - c[1], c[3] - bb[3])
            minimos["texto-borde de su caja"] = min(minimos["texto-borde de su caja"], holg)
            if holg < CAJAS[r["dentro"]]["grosor"] / 2.0 + HOLGURA_TEXTO:
                fallas.append(f"{r['s']!r}: a {holg:.1f} del borde de su caja {r['dentro']}")
        for clave, c in CAJAS.items():
            if clave != r["dentro"] and cruza(bb, ampliar(c["bb"], c["grosor"] / 2.0)):
                fallas.append(f"{r['s']!r}: se superpone con la caja {clave}")
        for nombre, m in MARCAS:
            if cruza(ampliar(bb, HOLGURA_TEXTO), m):
                fallas.append(f"{r['s']!r}: lo toca la marca {nombre}")
        for t in TRAZOS:
            for p, q in segmentos(t):
                d = distancia_segmento_caja(p, q, bb) - t["grosor"] / 2.0
                minimos["texto-trazo"] = min(minimos["texto-trazo"], d)
                if d < HOLGURA_TEXTO:
                    fallas.append(f"{r['s']!r}: lo toca el trazo {t['nombre']}")
                    break
            if t["punta"] and cruza(ampliar(bb, HOLGURA_TEXTO), caja_punta(t)):
                fallas.append(f"{r['s']!r}: lo toca la punta de {t['nombre']}")
    for r, bb in cajas_t:
        for nombre, m in MARCAS:
            dx = max(m[0] - bb[2], 0.0, bb[0] - m[2])
            dy = max(m[1] - bb[3], 0.0, bb[1] - m[3])
            minimos["texto-marca"] = min(minimos["texto-marca"], math.hypot(dx, dy))
    for i in range(len(cajas_t)):
        for j in range(i + 1, len(cajas_t)):
            (ra, a), (rb, b) = cajas_t[i], cajas_t[j]
            if cruza(a, b):
                fallas.append(f"{ra['s']!r} se superpone con {rb['s']!r}")
            dx = max(b[0] - a[2], 0.0, a[0] - b[2])
            dy = max(b[1] - a[3], 0.0, a[1] - b[3])
            minimos["texto-texto"] = min(minimos["texto-texto"], math.hypot(dx, dy))
    return fallas, tamanos, minimos, cajas_t


def controlar_trazos():
    fallas = []
    minimo = (math.inf, "", "")
    for t in TRAZOS:
        for clave, c in CAJAS.items():
            interior = ampliar(c["bb"], -1.0)
            if any(corta(p, q, interior) for p, q in segmentos(t)):
                fallas.append(f"el trazo {t['nombre']} entra en la caja {clave}")
            if t["punta"] and cruza(caja_punta(t), ampliar(c["bb"], -0.5)):
                fallas.append(f"la punta de {t['nombre']} entra en la caja {clave}")
    en_cajas = len(fallas)
    for i in range(len(TRAZOS)):
        for j in range(i + 1, len(TRAZOS)):
            a, b = TRAZOS[i], TRAZOS[j]
            if a["grupo"] == b["grupo"]:
                continue
            d = min(distancia_segmentos(p, q, u, v) for p, q in segmentos(a) for u, v in segmentos(b))
            if d < minimo[0]:
                minimo = (d, a["nombre"], b["nombre"])
            if d < DISTANCIA_MIN:
                fallas.append(f"{a['nombre']} a {d:.2f} de {b['nombre']}")
    return fallas, minimo, en_cajas


def controlar_margen(cajas_t, alto_total):
    todas = [(f"texto {r['s']!r}", bb) for r, bb in cajas_t]
    todas += [(f"caja {k}", ampliar(c["bb"], c["grosor"] / 2.0)) for k, c in CAJAS.items()]
    todas += [(f"marca {n}", m) for n, m in MARCAS]
    for t in TRAZOS:
        xs = [p[0] for p in t["puntos"]]
        ys = [p[1] for p in t["puntos"]]
        g = t["grosor"] / 2.0
        todas.append((f"trazo {t['nombre']}", (min(xs) - g, min(ys) - g, max(xs) + g, max(ys) + g)))
        if t["punta"]:
            todas.append((f"punta de {t['nombre']}", caja_punta(t)))
    distancia = {"izquierdo": lambda bb: bb[0], "superior": lambda bb: bb[1],
                 "derecho": lambda bb: W - bb[2], "inferior": lambda bb: alto_total - bb[3]}
    minimos, fallas = {}, []
    for borde, d in distancia.items():
        minimos[borde] = min(d(bb) for _, bb in todas)
        for nombre, bb in todas:
            if d(bb) < MARGEN_MIN:
                fallas.append(f"{nombre}: a {d(bb):.1f} unidades del borde {borde}")
    return minimos, fallas, len(todas)


def controlar_registro(svg):
    """Cada elemento del SVG (salvo el fondo y las definiciones) está en el
    registro, en el mismo orden."""
    ns = "{http://www.w3.org/2000/svg}"
    hijos = [el.tag.replace(ns, "") for el in ET.fromstring(svg)]
    if hijos[:2] != ["rect", "defs"]:
        return [f"el SVG no empieza con el fondo y las definiciones: {hijos[:2]}"]
    if hijos[2:] != DIBUJADOS:
        return [f"elementos del SVG {Counter(hijos[2:])} ≠ registrados {Counter(DIBUJADOS)}"]
    return []


# --------------------------------------------------------------------------- #
# Exportación                                                                  #
# --------------------------------------------------------------------------- #
# cairo escribe /CreationDate en el /Info del PDF; con SOURCE_DATE_EPOCH fijo el
# PDF es byte-reproducible (el recurso de las figuras hermanas).
SOURCE_DATE_EPOCH = "0"


def exportar(ruta_svg, ruta_png, ruta_pdf):
    rsvg = shutil.which("rsvg-convert")
    if not rsvg:
        freno("rsvg-convert no está instalado: no se escriben el PNG ni el PDF")
    subprocess.run([rsvg, "-w", str(ANCHO_PNG_PX), "-f", "png", "-o", ruta_png, ruta_svg], check=True)
    proc.grabar_densidad(ruta_png, DPI)
    entorno = dict(os.environ, SOURCE_DATE_EPOCH=SOURCE_DATE_EPOCH)
    subprocess.run([rsvg, "-f", "pdf", "-o", ruta_pdf, ruta_svg], check=True, env=entorno)


def invariantes_pdf(ruta_pdf):
    from pypdf import PdfReader
    lector = PdfReader(ruta_pdf)
    pagina = lector.pages[0]
    fecha = (lector.metadata or {}).get("/CreationDate")
    contenido = hashlib.sha256(pagina.get_contents().get_data()).hexdigest()
    return contenido, fecha, (float(pagina.mediabox.width), float(pagina.mediabox.height))


def main():
    global MEDIR
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--salida", default=AQUI,
                    help="directorio donde escribir el SVG, el PNG y el PDF (por omisión, el del script)")
    args = ap.parse_args()

    h = comprobar_fuentes()
    print("FUENTES (sha256 comprobado):")
    for clave, (rel, sha) in FUENTES.items():
        print(f"  {clave:10s} {rel}   {sha[:12]}…")
    print(f"  Textos Ordenados del conjunto: {h['tos']}; preguntas: {h['preguntas']}; reparto: "
          + ", ".join(f"{n} {r}" for n, r in h["reparto"]))
    print(f"  herramientas del agente: {h['herramientas']}; tope: {h['tope']} (controlado al cerrar "
          f"cada turno)")
    print(f"  pasos del juez: {h['pasos']}; repeticiones por defecto de la corrida: {h['repeticiones']}")
    print(f"  trazas: {h['grafos']} grafos × {h['preguntas']} preguntas × {h['repeticiones']} = "
          f"{h['corridas']} corridas")
    print(f"  adjudicación firmada: {h['afirmaciones_revisadas']} afirmaciones, método "
          f"{h['metodo_revision']!r}")
    print(f"  reporte final, líneas {h['lineas_reporte']} (correctas; no afectadas por la "
          f"adjudicación; estables, límite y citas)")
    cotejar_texto(h)
    print("TEXTO: cada número coincide con su fuente; los cortes de línea no cambian el texto")

    MEDIR = proc.medidor()
    if MEDIR is None:
        freno("sin las métricas reales de Helvetica (PIL y la fuente del sistema) no se compone la figura")
    svg, geo = componer()
    alto_total = geo["alto"]
    fallas_contenido = controlar_contenido()
    fallas_textos, tamanos, minimos, cajas_t = controlar_textos(alto_total)
    fallas_trazos, minimo_trazos, en_cajas = controlar_trazos()
    minimos_margen, fallas_margen, n_elem = controlar_margen(cajas_t, alto_total)
    fallas_registro = controlar_registro(svg)

    print(f"CONTENIDO: {len(REGISTRO)} textos; fallas: {len(fallas_contenido)}")
    for x in fallas_contenido:
        print(f"  MAL {x}")
    print(f"TEXTOS (métricas reales de Helvetica) contra {len(REGISTRO)} textos, {len(CAJAS)} cajas, "
          f"{len(MARCAS)} marcas y {len(TRAZOS)} trazos ({sum(1 for t in TRAZOS if t['punta'])} con "
          f"punta); fallas: {len(fallas_textos)}")
    print("  distancias mínimas: " + "; ".join(f"{k} {v:.1f}" for k, v in minimos.items()))
    for x in fallas_textos:
        print(f"  MAL {x}")
    print(f"TRAZOS: {en_cajas} trazos o puntas en el interior de una caja; distancia mínima entre "
          f"trazos de grupos distintos {minimo_trazos[0]:.1f} ({minimo_trazos[1]} / "
          f"{minimo_trazos[2]}), exigida {DISTANCIA_MIN}; fallas: {len(fallas_trazos)}")
    for x in fallas_trazos:
        print(f"  MAL {x}")
    mm = ANCHO_FIGURA_CM * 10 / W
    print(f"MARGEN ({n_elem} elementos): mínimo a cada borde "
          + ", ".join(f"{b} {v:.1f} u = {v * mm:.2f} mm" for b, v in minimos_margen.items())
          + f"; exigido {MARGEN_MM:.1f} mm ({MARGEN_MIN:.1f} u); fallas: {len(fallas_margen)}")
    for x in fallas_margen:
        print(f"  MAL {x}")
    print(f"REGISTRO: {len(DIBUJADOS)} elementos del SVG, todos registrados; fallas: "
          f"{len(fallas_registro)}")
    for x in fallas_registro:
        print(f"  MAL {x}")
    if fallas_contenido or fallas_textos or fallas_trazos or fallas_margen or fallas_registro:
        raise SystemExit("FALLA: la figura tiene defectos; no se escribe nada")
    for fs in sorted(tamanos):
        print(f"LETRA {fs} unidades -> {tamanos[fs]:.2f} pt impresos a {ANCHO_FIGURA_CM:.0f} cm")
    print(f"ALTO: lienzo {W} x {alto_total}, impreso a {ANCHO_FIGURA_CM:.2f} x "
          f"{ANCHO_FIGURA_CM * alto_total / W:.2f} cm")
    print("COMPOSICIÓN: fila de abajo " + ", ".join(f"{k} x={x:.1f} w={w}" for k, (x, w) in geo["fila2"].items())
          + f"; separación {geo['sep2']:.1f}; alto {geo['h2']:.1f}; preguntas w={geo['w_pre']}; "
          f"revisión x={geo['x_rev']:.1f} w={geo['w_rev']}; leyenda w={geo['w_ley']:.1f}")

    os.makedirs(args.salida, exist_ok=True)
    rutas = {ext: os.path.join(args.salida, f"{NOMBRE}.{ext}") for ext in ("svg", "png", "pdf")}
    with open(rutas["svg"], "w", encoding="utf-8", newline="\n") as fh:
        fh.write(svg)
    exportar(rutas["svg"], rutas["png"], rutas["pdf"])
    contenido, fecha, caja_pdf = invariantes_pdf(rutas["pdf"])
    for ext in ("svg", "png", "pdf"):
        print(f"{ext.upper()}: {rutas[ext]}   sha256 {sha256(rutas[ext])}")
    print(f"     PDF {caja_pdf[0]:.1f} x {caja_pdf[1]:.1f} pt; /CreationDate {fecha!r} "
          f"(SOURCE_DATE_EPOCH={SOURCE_DATE_EPOCH}); stream de contenido sha256 {contenido}")


if __name__ == "__main__":
    main()
