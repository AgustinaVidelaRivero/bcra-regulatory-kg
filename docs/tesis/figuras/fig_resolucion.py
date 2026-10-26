#!/usr/bin/env python3
"""Figura de la resolución de entidades y sujetos en el ensamblado, POR SCRIPT
y nunca a mano.

Qué dibuja, a 15 cm de ancho, en dos carriles que se juntan:
- a la izquierda, el carril de la entidad: la entidad que devolvió el
  extractor; el control del tipo; el identificador; la unión por
  identificador; la unión entre documentos;
- a la derecha, el carril del sujeto: la mención y la entrada sugerida; el
  orden en que el ensamblado asigna una entrada; una flecha baja de ahí a la
  caja de la unión por identificador;
- en cada caja, la línea general arriba (texto fijo, TEXTO_GENERAL) y, debajo,
  en cursiva y sobre un recuadro blanco, el ejemplo: la condición del monto
  del punto 5.1.1.1 de Clasificación de deudores en el carril de la entidad y
  las relaciones de sujeto del punto 5.1.1.2 en el del sujeto. Los tipos van
  en una pastilla con el color de su tipo en las figuras del ejemplo.

Fuentes, todas leídas del commit que se pasa con --commit
(`git show <commit>:<ruta>`), nunca del árbol de trabajo:
- el grafo (--grafo, un kg.json o un kg.json.gz; con --sha256-grafo, candado
  sobre el kg.json) y la extracción validada (--extraccion): de ahí salen
  todos los valores del ejemplo; del grafo, también la mención, la entrada
  sugerida y su etiqueta;
- los nueve tipos (TIPOS_ENTIDAD de MODELOS, leído con ast, sin importarlo);
- el estilo: cada valor sale de la línea que lo declara en el generador de
  otra figura (ESTILO) o de figura_esquema_final.svg (colores de los tipos);
  el script comprueba que esa línea esté, una sola vez, y escribe su número.
Nada del ejemplo está escrito a mano: solo las líneas generales y las
palabras que unen los valores (FRASES).

Controles (el primero que falla detiene el script y no se escribe nada):
contenido (las líneas generales son las fijadas; ningún texto con
identificadores, nombres de archivo ni comillas angulares simples); textos
(ninguno por debajo de 7,5 pt a 15 cm, fuera de su caja o superpuesto a otro);
cajas (sin superposición, separadas); flechas (tramos ortogonales, de borde a
borde, sin atravesar cajas ni cruzarse, sin tocar textos); margen (2 mm);
alto (media página A4 al ancho del texto); registro (el SVG se relee).

Salidas, byte-reproducibles: figura_resolucion.svg, .png (300 dpi, densidad
grabada) y .pdf (rsvg-convert con SOURCE_DATE_EPOCH=0).

Uso (desde la raíz del repo):
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B <ruta del script> \\
        --commit <commit> --grafo <ruta del kg.json o kg.json.gz en el commit> [--sha256-grafo <sha256>] \\
        [--extraccion <jsonl>] [--salida <dir>]
"""

from __future__ import annotations

import argparse
import ast
import gzip
import hashlib
import json
import math
import os
import re
import shutil
import struct
import subprocess
import sys
import unicodedata
import xml.etree.ElementTree as ET
import zlib

sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
NOMBRE = "figura_resolucion"


class Falla(Exception):
    """Falla de un control: la figura no se escribe."""


def fallar(control: str, motivo: str):
    raise Falla(f"[{control}] {motivo}")


# ========================================================================== #
# Fuentes                                                                    #
# ========================================================================== #
# El grafo evaluado y el sha256 de su kg.json (el del sello del grafo evaluado).
GRAFO_POR_OMISION = ("data/experiment/reaplicacion_unica/acumulado/ens_128_r2b_sincola/r2/kg.json.gz",
                     "576c97256185a0d5741cb2c35a2a85e91412f3e1119ad7a85d960b7d60c35ad3")
EXTRACCION_POR_OMISION = "data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b/cla/extracciones_finales_r2_cla.jsonl"
MODELOS = "data/experiment/pyd_r2/code/modelos_r2.py"
UNIDAD_ENTIDAD = "cla::5.1.1.1"
UNIDAD_SUJETO = "cla::5.1.1.2"
PREDICADOS_SUJETO = ("aplica_a", "ejecuta")

FIG = "docs/tesis/figuras"
PROC = f"{FIG}/generar_figura_proceso.py"
EXT = f"{FIG}/generar_figura_extractor_ejemplo.py"
ESQ = f"{FIG}/generar_figura_esquema_final.py"
NAG = f"{FIG}/generar_figura_norma_a_grafo.py"
SVG_ESQ = f"{FIG}/figura_esquema_final.svg"


def git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(["git", "--no-optional-locks", *args], capture_output=True)


def git_show(commit: str, ruta: str) -> bytes:
    r = git("show", f"{commit}:{ruta}")
    if r.returncode != 0:
        fallar("fuentes", f"git show {commit[:12]}:{ruta}: {r.stderr.decode('utf-8').strip()}")
    return r.stdout


def sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def resolver_commit(commit: str) -> str:
    raiz = git("rev-parse", "--show-toplevel")
    if raiz.returncode != 0 or os.path.realpath(raiz.stdout.decode().strip()) != os.path.realpath(os.getcwd()):
        fallar("fuentes", "el script corre desde la raíz del repositorio")
    r = git("rev-parse", "--verify", f"{commit}^{{commit}}")
    if r.returncode != 0:
        fallar("fuentes", f"no es un commit: {commit}")
    return r.stdout.decode().strip()


# ========================================================================== #
# Estilo: cada valor con la línea que lo declara en otra figura              #
# ========================================================================== #
TIPOGRAFIA = "Helvetica,Arial,sans-serif"
DETERMINISTICA = {"relleno": "#e1e7ee", "borde": "#4a5a6a"}      # «azul»: pieza de código
NEUTRO = {"relleno": "#fafafa", "borde": "#999999"}              # gris: datos
TINTA, TINTA_SUB = "#1f1f1f", "#444444"
FLECHA = "#555555"
GROSOR_CAJA = 1.6
GROSOR_FLUJO = 1.8
RADIO = 9
RX = 8
MARCO = {"relleno": "white", "borde": "#e2e2e2", "grosor": 1, "rx": 5}   # marco de la leyenda
MUESTRA_W, MUESTRA_H, FILA_LEY = 24, 16, 22
MARCADOR_A = 'viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
MARCADOR_B = 'markerHeight="6" orient="auto"><path d="M0,0L10,5L0,10z"'
MARCADOR = MARCADOR_A + MARCADOR_B
LEYENDA_CODIGO, LEYENDA_DATOS = "Pieza de código", "Datos"
GRUPO_LEYENDA = 10
HUECO_PUNTA = 2.0
LEJOS_ESQUINA = RX + 4
ANCHO_CM = 15.0
DPI = 300
SOURCE_DATE_EPOCH = "0"
W = 850
PT_MINIMO = 7.0
ANCHO_MONO = 0.602
ASC_MONO, DESC_MONO = 0.76, 0.24
MARGEN = 14
FS = 15
IL = 18
ASC, DESC = 0.78, 0.22
PAD_X, PAD_Y = 12, 9
FUENTE_SISTEMA = "/System/Library/Fonts/Helvetica.ttc"
MONO = "Menlo,Consolas,'Courier New',monospace"

# nombre -> (fuente, declaración tal cual, valores que la figura usa y que la
# declaración tiene que contener). Una línea coincide si, sin los espacios de
# los extremos, es la declaración o la declaración seguida de un comentario.
ESTILO = {
    "TIPOGRAFIA": (PROC, 'TIPOGRAFIA = "Helvetica,Arial,sans-serif"', (TIPOGRAFIA,)),
    "DETERMINISTICA": (PROC, 'DETERMINISTICA = {"relleno": "#e1e7ee", "borde": "#4a5a6a"}',
                       tuple(DETERMINISTICA.values())),
    "NEUTRO": (PROC, 'NEUTRO = {"relleno": "#fafafa", "borde": "#999999"}', tuple(NEUTRO.values())),
    "TINTA, TINTA_SUB": (PROC, 'TINTA, TINTA_SUB = "#1f1f1f", "#444444"', (TINTA, TINTA_SUB)),
    "FLECHA": (PROC, 'FLECHA, GRIS_ARISTA = "#555555", "#8a8a8a"', (FLECHA,)),
    "GROSOR_CAJA": (PROC, "GROSOR_CAJA, GROSOR_DISCONTINUA = 1.6, 1.3", (GROSOR_CAJA,)),
    "GROSOR_FLUJO": (PROC, "GROSOR_FLUJO, GROSOR_RAMA = 1.8, 1.6", (GROSOR_FLUJO,)),
    "RADIO": (PROC, "RADIO = 9", (RADIO,)),
    "RX": (PROC, "RX = 8", (RX,)),
    "MARCO": (PROC, """LEYENDA_MARCO = 'fill="white" stroke="#e2e2e2" stroke-width="1" rx="5"'""",
              tuple(MARCO.values())),
    "MUESTRAS": (PROC, "MUESTRA_W, MUESTRA_H, FILA_LEY = 24, 16, 22", (MUESTRA_W, MUESTRA_H, FILA_LEY)),
    "MARCADOR_A": (PROC, """MARCADOR_A = 'viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '""",
                   (MARCADOR_A,)),
    "MARCADOR_B": (PROC, """MARCADOR_B = 'markerHeight="6" orient="auto"><path d="M0,0L10,5L0,10z"'""",
                   (MARCADOR_B,)),
    "LEYENDA_CODIGO": (PROC, '("codigo", "Pieza de código"),', (LEYENDA_CODIGO,)),
    "LEYENDA_DATOS": (PROC, '("datos", "Datos"))', (LEYENDA_DATOS,)),
    "GRUPO_LEYENDA": (PROC, "GRUPO_LEYENDA = 10", (GRUPO_LEYENDA,)),
    "HUECO_PUNTA": (PROC, "HUECO_PUNTA = 2.0", (HUECO_PUNTA,)),
    "LEJOS_ESQUINA": (PROC, "LEJOS_ESQUINA = RX + 4", ("RX + 4",)),
    "ANCHO_CM": (PROC, "ANCHO_CM = 15.0", (ANCHO_CM,)),
    "DPI": (PROC, "DPI = 300", (DPI,)),
    "SOURCE_DATE_EPOCH": (PROC, 'SOURCE_DATE_EPOCH = "0"', (SOURCE_DATE_EPOCH,)),
    "W": (ESQ, "W, H = 850, 852", (W,)),
    "PT_MINIMO": (ESQ, "PT_MINIMO = 7.0", (PT_MINIMO,)),
    "ANCHO_MONO": (ESQ, "ANCHO_MONO = 0.602", (ANCHO_MONO,)),
    "ASC_MONO, DESC_MONO": (ESQ, "ASC_MONO, DESC_MONO = 0.76, 0.24", (ASC_MONO, DESC_MONO)),
    "MARGEN": (EXT, "MARGEN = 14", (MARGEN,)),
    "FS": (EXT, "FS_ETIQUETA = 15", (FS,)),
    "IL": (EXT, "IL_ETIQUETA = 18", (IL,)),
    "ASC, DESC": (EXT, "ASC_SANS, DESC_SANS = 0.78, 0.22", (ASC, DESC)),
    "PAD_X, PAD_Y": (EXT, "PAD_X, PAD_Y = 12, 9", (PAD_X, PAD_Y)),
    "FUENTE_SISTEMA": (NAG, 'FUENTE_SISTEMA = "/System/Library/Fonts/Helvetica.ttc"', (FUENTE_SISTEMA,)),
}
# Tipos que la figura dibuja en pastilla, con el estilo de su caja en la figura
# del esquema final (relleno y borde; el discontinuo del Sujeto).
TIPOS_PASTILLA = ("Condicion", "TextoOrdenado", "Sujeto")


def coincide(linea: str, decl: str) -> bool:
    s, d = linea.strip(), decl.strip()
    return s == d or (s.startswith(d + " ") and s[len(d):].strip().startswith("#"))


def leer_estilo(commit: str) -> dict:
    """Comprueba cada valor de ESTILO contra su línea y lee de
    figura_esquema_final.svg el estilo de las pastillas y la tipografía de los
    tipos. Devuelve el número de línea de cada valor y el estilo leído."""
    textos, lugares = {}, {}
    for nombre, (ruta, decl, usados) in ESTILO.items():
        if ruta not in textos:
            textos[ruta] = git_show(commit, ruta).decode("utf-8").splitlines()
        hallados = [i + 1 for i, l in enumerate(textos[ruta]) if coincide(l, decl)]
        if len(hallados) != 1:
            fallar("estilo", f"{nombre}: {len(hallados)} líneas «{decl}» en {ruta}, se esperaba una")
        for v in usados:
            if str(v) not in decl:
                fallar("estilo", f"{nombre}: la figura usa {v!r} y {ruta}:{hallados[0]} declara «{decl}»")
        lugares[nombre] = f"{ruta}:{hallados[0]}"
    crudo = git_show(commit, SVG_ESQ).decode("utf-8")
    lineas = crudo.splitlines()
    raiz = ET.fromstring(crudo)
    ns = "{http://www.w3.org/2000/svg}"
    pastillas = {}
    for t in TIPOS_PASTILLA:
        rs = [el for el in raiz.iter(ns + "rect") if el.get("data-caja") == t]
        if len(rs) != 1:
            fallar("estilo", f"{SVG_ESQ}: {len(rs)} cajas «{t}»")
        el = rs[0]
        n = [i + 1 for i, l in enumerate(lineas) if f'data-caja="{t}"' in l]
        pastillas[t] = {"relleno": el.get("fill"), "borde": el.get("stroke"),
                        "guiones": el.get("stroke-dasharray")}
        lugares[f"pastilla {t}"] = f"{SVG_ESQ}:{n[0]}"
    nombres = [el for el in raiz.iter(ns + "text") if el.get("font-weight") == "bold" and el.text == "Condicion"]
    if len(nombres) != 1 or nombres[0].get("font-family") != MONO:
        fallar("estilo", f"{SVG_ESQ}: el tipo «Condicion» no está en {MONO} negrita")
    lugares["tipografía de los tipos"] = f"{SVG_ESQ}:" + str(
        next(i + 1 for i, l in enumerate(lineas) if 'font-weight="bold">Condicion<' in l))
    cursivas = [i + 1 for i, l in enumerate(lineas) if 'font-style="italic"' in l]
    if not cursivas:
        fallar("estilo", f"{SVG_ESQ}: ninguna nota en cursiva")
    lugares["cursiva de las notas"] = f"{SVG_ESQ}:{cursivas[0]}"
    return {"lugares": lugares, "pastillas": pastillas}


# ========================================================================== #
# Lo que la figura afirma                                                    #
# ========================================================================== #
# Líneas generales: el texto fijado, tal cual. PARRAFOS es el mismo texto con
# sus cortes de renglón (el control comprueba que unidos den TEXTO_GENERAL).
TEXTO_GENERAL = {
    "E1": "Entidad que devolvió el extractor: tipo, etiqueta, descripción y punto",
    "E2": "Validador y ensamblado: el tipo tiene que estar entre los 9 del esquema; si no, la entidad queda fuera",
    "E3": ("Ensamblado: un identificador con el tipo y lo que identifica a la entidad; en una de contenido, "
           "también el documento y el punto"),
    "E4": ("¿Ya hay un nodo con ese identificador? Sí: se une a él y suma su procedencia. "
           "No: es un nodo nuevo"),
    "E5": "Al juntar los documentos, se unen los sujetos del catálogo y las comunicaciones con el mismo código",
    "S1": "Sujeto de una relación: la mención y la entrada del catálogo que sugiere el extractor",
    "S2": ("Ensamblado: 1. la entrada cuyo nombre o alias es la mención; 2. si no hay, la que sugirió el "
           "extractor; 3. si no sugirió ninguna, la de una regla sobre la mención; 4. si nada corresponde, "
           "un sujeto propuesto, en cuarentena"),
}
PARRAFOS = {
    "E1": (TEXTO_GENERAL["E1"],),
    "E2": (TEXTO_GENERAL["E2"],),
    "E3": (TEXTO_GENERAL["E3"],),
    "E4": ("¿Ya hay un nodo con ese identificador?", "Sí: se une a él y suma su procedencia.",
           "No: es un nodo nuevo"),
    "E5": (TEXTO_GENERAL["E5"],),
    "S1": (TEXTO_GENERAL["S1"],),
    "S2": ("Ensamblado:", "1. la entrada cuyo nombre o alias es la mención;",
           "2. si no hay, la que sugirió el extractor;", "3. si no sugirió ninguna, la de una regla sobre la mención;",
           "4. si nada corresponde, un sujeto propuesto, en cuarentena"),
}
CLASE = {"E1": "datos", "E2": "codigo", "E3": "codigo", "E4": "codigo", "E5": "codigo",
         "S1": "datos", "S2": "codigo"}
PALETA = {"codigo": DETERMINISTICA, "datos": NEUTRO}
CARRIL_ENTIDAD = ("E1", "E2", "E3", "E4", "E5")
CARRIL_SUJETO = ("S1", "S2")
CONEXIONES = (("E1", "E2"), ("E2", "E3"), ("E3", "E4"), ("E4", "E5"), ("S1", "S2"), ("S2", "E4"))
LEYENDA = (("codigo", LEYENDA_CODIGO), ("datos", LEYENDA_DATOS),
           ("ejemplo", "Ejemplo, en cursiva y sobre blanco, leído del grafo y de la extracción"))

# Palabras que unen los valores en la línea del ejemplo; los valores van entre
# llaves y salen de leer_ejemplo.
FRASES = {
    "E1": "«{etiqueta}», punto {punto}",
    "E2": "está en la lista",
    "E3": "se arma con {campos}",
    "E4_nuevo": "es un nodo nuevo",
    "E4_unido": "se une al nodo de {n} unidades",
    "E4_to": "del {punto}: se une al nodo de {n} unidades de {materia}",
    "S1": "Del {punto}: mención «{mencion}»; entrada sugerida:",
    "S2": "Las relaciones del {punto}, por el {numero}:",
}
# Campos de la clave del identificador por tipo de contenido, en la fase r2b
# (e2_lib.entity_slug_r2), con su nombre en castellano.
CAMPOS_CLAVE = {
    "Restriccion": ("descripción",), "Obligacion": ("descripción",), "Excepcion": ("descripción",),
    "Condicion": ("etiqueta", "descripción"), "Definicion": ("etiqueta", "descripción"),
    "Potestad": ("etiqueta", "descripción"), "Operacion": ("etiqueta",),
}
# Método de resolución de la arista -> número del orden de la caja del sujeto
# (r1_e4.resolver_relaciones_r2: R1; la sugerencia del modelo; R2, el
# calificador o R3; sin ninguna, la cuarentena).
def numero_de_metodo(m: str) -> int:
    if m.startswith("R1_"):
        return 1
    if m == "R4_sugerencia_modelo":
        return 2
    if m.startswith("R2_") or m in ("R2_calificador", "R3"):
        return 3
    if m == "cuarentena":
        return 4
    fallar("ejemplo", f"método de resolución sin número en el orden: {m!r}")


# Nada de esto puede aparecer en un texto dibujado.
PROHIBIDOS = (re.compile(r"::"), re.compile(r"_"), re.compile("[\u2039\u203a]"), re.compile(r"\b[0-9a-f]{7,64}\b"),
              re.compile(r"\.(jsonl?|py|md|pdf|txt|db)\b", re.I), re.compile(r"\w/\w+\.\w+|\\"))


# ========================================================================== #
# Valores del ejemplo                                                        #
# ========================================================================== #
def jsonl(b: bytes) -> list[dict]:
    return [json.loads(s) for s in b.decode("utf-8").split("\n") if s.strip()]


def procedencias(o: dict) -> list[dict]:
    return o.get("provenances") or ([o["provenance"]] if o.get("provenance") else [])


def chunks(o: dict) -> list[str]:
    return [p.get("chunk_id") for p in procedencias(o)]


def slugify_full(s: str) -> str:
    """Copia de e2_lib.slugify_full (data/experiment/reextraccion_v2/e2_reduce/e2_lib.py:90-97)."""
    if not s:
        return "empty"
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")
    return s or "empty"


def id_estable(full: str, max_len: int = 80) -> str:
    """Copia de e2_lib._id_estable (e2_lib.py:100-107)."""
    return f"{full[:max_len]}_{hashlib.sha1(full.encode('utf-8')).hexdigest()[:6]}"


def id_de_contenido(e: dict) -> str:
    """Identificador de una entidad de contenido en la fase r2b, como
    e2_lib.entity_slug_r2 (e2_lib.py:845-870) y el prefijo del tipo (:1011)."""
    t, props, pv = e["type"], e.get("properties") or {}, e.get("provenance") or {}
    ancla = slugify_full(f"{pv.get('to') or pv.get('archivo') or ''}::{pv.get('punto') or ''}")
    label = e.get("label") or ""
    if t in ("Restriccion", "Obligacion", "Excepcion"):
        clave = slugify_full(str(props.get("descripcion") or label)) + "__" + ancla
    elif t in ("Condicion", "Definicion", "Potestad"):
        clave = slugify_full(label) + "__" + slugify_full(str(props.get("descripcion") or "")) + "__" + ancla
    elif t == "Operacion":
        clave = slugify_full(label or str(props.get("tipo") or "")) + "__" + ancla
    else:
        fallar("ejemplo", f"{t} no es un tipo de contenido")
    return f"{t}_{id_estable(clave)}"


def lista_castellano(xs) -> str:
    xs = list(xs)
    return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " y " + xs[-1]


def leer_tipos(commit: str) -> tuple:
    arbol = ast.parse(git_show(commit, MODELOS).decode("utf-8"))
    for nodo in arbol.body:
        if isinstance(nodo, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "TIPOS_ENTIDAD"
                                                for t in nodo.targets):
            return tuple(ast.literal_eval(nodo.value)), nodo.lineno
    fallar("fuentes", f"{MODELOS} no declara TIPOS_ENTIDAD")


def unico_registro(filas: list[dict], unidad: str, ruta: str) -> dict:
    de = [f for f in filas if f.get("chunk_id") == unidad]
    if len(de) != 1:
        fallar("ejemplo", f"{ruta}: {len(de)} registros de {unidad}, no uno")
    if not isinstance(de[0].get("validacion"), dict):
        fallar("ejemplo", f"{ruta}: el registro de {unidad} no tiene validación")
    return de[0]["validacion"]


def leer_ejemplo(commit: str, args) -> dict:
    """Los valores del ejemplo. Del punto de la entidad se leen solo
    entidades; del punto del sujeto, solo sus relaciones de sujeto; del nodo
    de un sujeto, solo su etiqueta (no su procedencia)."""
    crudo_kg = git_show(commit, args.grafo)
    if args.grafo.endswith(".gz"):
        crudo_kg = gzip.decompress(crudo_kg)
    sha_kg = sha256(crudo_kg)
    if args.sha256_grafo and sha_kg != args.sha256_grafo:
        fallar("fuentes", f"{args.grafo}: sha256 del kg.json {sha_kg} ≠ {args.sha256_grafo}")
    kg = json.loads(crudo_kg.decode("utf-8"))
    nodos = {n["id"]: n for n in kg["nodes"]}
    if len(nodos) != len(kg["nodes"]):
        fallar("ejemplo", "el grafo tiene ids de nodo repetidos")
    tipos, linea_tipos = leer_tipos(commit)
    crudo_ext = git_show(commit, args.extraccion)
    filas = jsonl(crudo_ext)
    E = {"fuentes": {"grafo": (args.grafo, sha_kg), "extraccion": (args.extraccion, sha256(crudo_ext)),
                     "tipos": (f"{MODELOS}:{linea_tipos}", sha256(git_show(commit, MODELOS)))},
         "tipos": tipos, "avisos": []}
    if len(tipos) != 9:
        E["avisos"].append(f"{MODELOS} declara {len(tipos)} tipos; la línea general dice 9")

    # ---- carril de la entidad: entidades de la unidad --------------------- #
    v1 = unico_registro(filas, args.unidad_entidad, args.extraccion)
    ents = [e for e in v1.get("entidades", []) if e.get("type") != "Sujeto"]
    condiciones = []
    for e in ents:
        if e.get("type") != "Condicion":
            continue
        gid = id_de_contenido(e)
        if gid not in nodos:
            fallar("ejemplo", f"el identificador recalculado de la condición {e.get('local_id')} no es un nodo")
        if (nodos[gid].get("properties") or {}).get("umbrales"):
            condiciones.append((e, gid))
    if len(condiciones) != 1:
        fallar("ejemplo", f"{len(condiciones)} condiciones de {args.unidad_entidad} con umbral; se espera una")
    cond, gid = condiciones[0]
    nodo = nodos[gid]
    if nodo["label"] != cond["label"] or nodo["type"] != cond["type"]:
        fallar("ejemplo", "la etiqueta o el tipo de la condición difieren entre la extracción y el grafo")
    unidades_cond = sorted(set(chunks(nodo)))
    if args.unidad_entidad not in unidades_cond:
        fallar("ejemplo", "el nodo de la condición no tiene la procedencia de la unidad")
    tos = [e for e in ents if e.get("type") == "TextoOrdenado"]
    if len(tos) != 1:
        fallar("ejemplo", f"{len(tos)} Textos Ordenados en la extracción de {args.unidad_entidad}")
    nodos_to = [n for n in kg["nodes"] if n["type"] == "TextoOrdenado" and args.unidad_entidad in chunks(n)]
    if len(nodos_to) != 1:
        fallar("ejemplo", f"{len(nodos_to)} nodos de Texto Ordenado con la procedencia de {args.unidad_entidad}")
    nto = nodos_to[0]
    docs_to = sorted({p.get("to") for p in procedencias(nto)})
    if docs_to != [(cond.get("provenance") or {}).get("to")]:
        fallar("ejemplo", f"el nodo del Texto Ordenado reúne procedencias de {docs_to}")
    materia = (nto.get("properties") or {}).get("materia")
    if not materia:
        fallar("ejemplo", "el nodo del Texto Ordenado no tiene materia")
    E["entidad"] = {
        "tipo": cond["type"], "etiqueta": cond["label"], "punto": cond.get("punto"),
        "descripcion": (cond.get("properties") or {}).get("descripcion"),
        "documento": (cond.get("provenance") or {}).get("to"), "local_id": cond.get("local_id"),
        "tipo_en_lista": cond["type"] in tipos,
        "campos_clave": ("tipo",) + CAMPOS_CLAVE[cond["type"]] + ("documento", "punto"),
        "id_recalculado_en_el_grafo": True,
        "unidades_del_nodo": len(unidades_cond), "procedencias_del_nodo": len(chunks(nodo)),
        "to_punto": tos[0].get("punto"), "to_unidades": len(set(chunks(nto))),
        "to_procedencias": len(chunks(nto)), "to_materia": materia, "to_documento": docs_to[0]}
    if not E["entidad"]["tipo_en_lista"]:
        E["avisos"].append(f"el tipo {cond['type']!r} no está en TIPOS_ENTIDAD")

    # ---- carril del sujeto: aristas de sujeto de la unidad, en el grafo ---- #
    aristas = [e for e in kg["edges"] if e["relation"] in PREDICADOS_SUJETO and args.unidad_sujeto in chunks(e)]
    if not aristas:
        fallar("ejemplo", f"{args.unidad_sujeto} no tiene aristas de sujeto en el grafo")
    sug = {(tuple(sorted({p.get("punto") for p in procedencias(e) if p.get("chunk_id") == args.unidad_sujeto})),
            e.get("sujeto_mencion"), e.get("sujeto_id_modelo")) for e in aristas}
    if len(sug) != 1:
        fallar("ejemplo", f"las aristas de sujeto de {args.unidad_sujeto} no traen el mismo punto, la misma mención "
                          f"y la misma sugerencia: {len(sug)} combinaciones")
    puntos2, mencion, sid_sug = sug.pop()
    if len(puntos2) != 1:
        fallar("ejemplo", f"las aristas de sujeto de {args.unidad_sujeto} traen {len(puntos2)} puntos")
    punto2 = puntos2[0]
    if not (mencion and sid_sug):
        fallar("ejemplo", "sin mención o sin entrada sugerida")
    if (nodos.get(sid_sug) or {}).get("type") != "Sujeto" or not nodos[sid_sug].get("label"):
        fallar("ejemplo", "la entrada sugerida no es un nodo Sujeto con etiqueta en el grafo")
    res = {(e.get("metodo_resolucion"), e["target"] if e["relation"] == "aplica_a" else e["source"])
           for e in aristas}
    if len(res) != 1:
        fallar("ejemplo", f"las relaciones de sujeto de {args.unidad_sujeto} no se resolvieron todas igual: "
                          f"{len(res)} combinaciones de método y entrada")
    metodo, sid = res.pop()
    E["sujeto"] = {"punto": punto2, "mencion": mencion, "sugerida": nodos[sid_sug]["label"],
                   "sugerida_id_es_la_asignada": sid_sug == sid, "metodo": metodo,
                   "numero": numero_de_metodo(metodo), "asignada": nodos[sid]["label"],
                   "aristas_grafo": len(aristas)}
    return E


# ========================================================================== #
# Medida del texto                                                           #
# ========================================================================== #
_CACHE = {}


def ancho(s: str, estilo: str) -> float:
    """Ancho en unidades de lienzo a FS: Helvetica real (PIL, como el medidor
    de generar_figura_norma_a_grafo.py) o Menlo por avance fijo."""
    if estilo == "mono":
        return ANCHO_MONO * FS * len(s)
    from PIL import ImageFont  # noqa: PLC0415
    idx = {"normal": 0, "negrita": 1, "cursiva": 2}[estilo]
    if idx not in _CACHE:
        if not os.path.exists(FUENTE_SISTEMA):
            fallar("textos", f"falta la fuente {FUENTE_SISTEMA}")
        _CACHE[idx] = ImageFont.truetype(FUENTE_SISTEMA, int(round(FS * 10)), index=idx)
    return _CACHE[idx].getlength(s) / 10.0


def envolver(texto: str, primera: float, resto: float, estilo: str) -> list[str]:
    """Corte por palabras: la primera línea en `primera`, las demás en `resto`."""
    lineas, actual = [], ""
    for palabra in texto.split(" "):
        cand = palabra if not actual else actual + " " + palabra
        limite = primera if not lineas else resto
        if actual and ancho(cand, estilo) > limite:
            lineas.append(actual)
            actual = palabra
        else:
            actual = cand
    lineas.append(actual)
    return lineas


# ========================================================================== #
# Geometría                                                                  #
# ========================================================================== #
ANCHO_IZQ = 474                 # carril de la entidad
SEP_CARRILES = 34
ANCHO_DER = W - 2 * MARGEN - ANCHO_IZQ - SEP_CARRILES     # carril del sujeto
SEP_V = 28                      # entre cajas de un carril: la flecha
SEP_RECUADRO = 7                # de la línea general al recuadro del ejemplo
RECUADRO_DX = 7                 # del borde de la caja al recuadro
RECUADRO_PAD_X, RECUADRO_PAD_Y = 8, 4
IL_EJ = 21                      # interlínea del ejemplo (la pastilla mide 19)
PASTILLA_PAD_X, PASTILLA_PAD_Y = 4, 2
PASTILLA_SEP = 6
PASTILLA_RX = 3
HOLGURA_TEXTO = 1.5
SEP_CAJAS = 8.0
MARGEN_MM = 2.0
MARGEN_MIN = MARGEN_MM * W / (ANCHO_CM * 10)
ALTO_MAX_CM = 12.85             # media caja de texto de A4 (29,7 − 2 − 2 cm, entre 2)
PT_POR_CM = 72.0 / 2.54
ANCHO_PNG_PX = round(ANCHO_CM / 2.54 * DPI)


def pt(u: float) -> float:
    return u * ANCHO_CM * PT_POR_CM / W


def f(v: float) -> str:
    return f"{v:.1f}"


def filas_ejemplo(E: dict) -> dict:
    """(tipo en pastilla o None, texto) de cada renglón del ejemplo, por caja."""
    en, su = E["entidad"], E["sujeto"]
    t = en["tipo"]
    e4 = (FRASES["E4_nuevo"] if en["unidades_del_nodo"] == 1
          else FRASES["E4_unido"].format(n=en["unidades_del_nodo"]))
    return {
        "E1": ((t, FRASES["E1"].format(etiqueta=en["etiqueta"], punto=en["punto"])),),
        "E2": ((t, FRASES["E2"]),),
        "E3": ((t, FRASES["E3"].format(campos=lista_castellano(en["campos_clave"]))),),
        "E4": ((t, e4), ("TextoOrdenado", FRASES["E4_to"].format(punto=en["to_punto"], n=en["to_unidades"],
                                                                 materia=en["to_materia"]))),
        "E5": (),
        "S1": ((None, FRASES["S1"].format(punto=su["punto"], mencion=su["mencion"])), ("Sujeto", su["sugerida"])),
        "S2": ((None, FRASES["S2"].format(punto=su["punto"], numero=su["numero"])), ("Sujeto", su["asignada"])),
    }


def armar_caja(clave: str, x: float, y: float, w: float, filas: tuple) -> dict:
    util = w - 2 * PAD_X
    gen = []                                    # (texto, dx)
    for par in PARRAFOS[clave]:
        m = re.match(r"^\d\. ", par)
        sangria = ancho(m.group(0), "normal") if m else 0.0
        for j, s in enumerate(envolver(par, util, util - sangria, "normal")):
            gen.append((s, 0.0 if j == 0 else sangria))
    caja = {"clave": clave, "x": float(x), "y": float(y), "w": float(w), "clase": CLASE[clave],
            "general": gen, "ejemplo": []}
    alto = PAD_Y + len(gen) * IL
    if filas:
        interior = w - 2 * RECUADRO_DX - 2 * RECUADRO_PAD_X
        n = 0
        for tipo, texto in filas:
            ap = (ANCHO_MONO * FS * len(tipo) + 2 * PASTILLA_PAD_X + PASTILLA_SEP) if tipo else 0.0
            lineas = envolver(texto, interior - ap, interior, "cursiva")
            caja["ejemplo"].append({"tipo": tipo, "lineas": lineas, "desde": n, "dx_pastilla": ap})
            n += len(lineas)
        ry = y + alto + SEP_RECUADRO
        caja["recuadro"] = {"x": x + RECUADRO_DX, "y": ry, "w": w - 2 * RECUADRO_DX,
                            "h": 2 * RECUADRO_PAD_Y + n * IL_EJ}
        alto = ry + caja["recuadro"]["h"] - y
    caja["h"] = float(math.ceil(alto + PAD_Y))
    return caja


def textos_de_caja(c: dict, pastillas: dict) -> tuple[list, list]:
    """Textos (con su contenedor) y pastillas de una caja."""
    T, P = [], []
    for i, (s, dx) in enumerate(c["general"]):
        base = c["y"] + PAD_Y + i * IL + (IL - FS) / 2.0 + ASC * FS
        T.append({"s": s, "x": c["x"] + PAD_X + dx, "y": base, "estilo": "normal", "color": TINTA,
                  "dentro": c["clave"], "pieza": ("general", c["clave"], i)})
    if c["ejemplo"]:
        R = c["recuadro"]
        for fila in c["ejemplo"]:
            for j, s in enumerate(fila["lineas"]):
                k = fila["desde"] + j
                base = R["y"] + RECUADRO_PAD_Y + k * IL_EJ + (IL_EJ - FS) / 2.0 + ASC * FS
                x0 = R["x"] + RECUADRO_PAD_X
                if j == 0 and fila["tipo"]:
                    t = fila["tipo"]
                    pw = ANCHO_MONO * FS * len(t) + 2 * PASTILLA_PAD_X
                    ph = (ASC_MONO + DESC_MONO) * FS + 2 * PASTILLA_PAD_Y
                    p = {"tipo": t, "x": x0, "y": base - ASC_MONO * FS - PASTILLA_PAD_Y, "w": pw, "h": ph,
                         "dentro": f"recuadro {c['clave']}", "clave": f"pastilla {c['clave']} {k}",
                         **pastillas[t]}
                    P.append(p)
                    T.append({"s": t, "x": x0 + PASTILLA_PAD_X, "y": base, "estilo": "mono", "color": TINTA,
                              "dentro": p["clave"], "pieza": ("pastilla", c["clave"], k)})
                    x0 += fila["dx_pastilla"]
                T.append({"s": s, "x": x0, "y": base, "estilo": "cursiva", "color": TINTA_SUB,
                          "dentro": f"recuadro {c['clave']}", "pieza": ("ejemplo", c["clave"], k)})
    return T, P


def armar_modelo(E: dict, estilo: dict) -> dict:
    filas = filas_ejemplo(E)
    C = {}
    x_izq, x_der = float(MARGEN), float(MARGEN + ANCHO_IZQ + SEP_CARRILES)
    y = float(MARGEN)
    for k in CARRIL_ENTIDAD:
        C[k] = armar_caja(k, x_izq, y, ANCHO_IZQ, filas[k])
        y = C[k]["y"] + C[k]["h"] + SEP_V
    y = float(MARGEN)
    for k in CARRIL_SUJETO:
        C[k] = armar_caja(k, x_der, y, ANCHO_DER, filas[k])
        y = C[k]["y"] + C[k]["h"] + SEP_V
    # La flecha del sujeto entra por el costado derecho de E4, por debajo de S2:
    # si no hay lugar, el carril de la entidad baja desde E4.
    S2, E4 = C["S2"], C["E4"]
    y_in = max(S2["y"] + S2["h"] + 2 * RADIO + 4, E4["y"] + LEJOS_ESQUINA)
    falta = y_in - (E4["y"] + E4["h"] - LEJOS_ESQUINA)
    if falta > 0:
        for k in ("E4", "E5"):
            C[k] = armar_caja(k, x_izq, C[k]["y"] + math.ceil(falta), ANCHO_IZQ, filas[k])
        E4 = C["E4"]
    # Flechas.
    T = []
    for a, b in CONEXIONES:
        A, B = C[a], C[b]
        if (a, b) == ("S2", "E4"):
            xs = A["x"] + A["w"] / 2.0
            pts = [(xs, A["y"] + A["h"]), (xs, y_in), (B["x"] + B["w"] + HUECO_PUNTA, y_in)]
        else:
            cx = A["x"] + A["w"] / 2.0
            pts = [(cx, A["y"] + A["h"]), (cx, B["y"] - HUECO_PUNTA)]
        T.append({"desde": a, "hasta": b, "puntos": [(float(px), float(py)) for px, py in pts]})
    # Textos y pastillas.
    textos, pastillas = [], []
    for k in CARRIL_ENTIDAD + CARRIL_SUJETO:
        t, p = textos_de_caja(C[k], estilo["pastillas"])
        textos += t
        pastillas += p
    # Leyenda, en el carril del sujeto, debajo de la flecha que va a E4 y con su
    # borde de abajo en el de E5; una entrada por fila, el texto envuelto al
    # ancho del carril. Si no entra ahí, baja.
    x_ley = x_der
    util = ANCHO_DER - 12 - MUESTRA_W - 9 - 12
    filas_ley = [(clase, envolver(s, util, util, "normal")) for clase, s in LEYENDA]
    h_ley = GRUPO_LEYENDA + sum(FILA_LEY + (len(ls) - 1) * IL for _, ls in filas_ley) + 6
    E5 = C["E5"]
    y_ley = max(E5["y"] + E5["h"] - h_ley, y_in + GROSOR_FLUJO / 2.0 + SEP_CAJAS + 4)
    w_ley = 12 + MUESTRA_W + 9 + max(ancho(s, "normal") for _, ls in filas_ley for s in ls) + 12
    L = {"x": float(x_ley), "y": float(math.ceil(y_ley)), "w": float(math.ceil(w_ley)), "h": float(h_ley),
         "muestras": []}
    yy = L["y"] + GRUPO_LEYENDA
    for clase, ls in filas_ley:
        yc = yy + FILA_LEY / 2.0
        L["muestras"].append({"clase": clase, "x": L["x"] + 12, "y": yc - MUESTRA_H / 2.0, "w": float(MUESTRA_W),
                              "h": float(MUESTRA_H)})
        for j, s in enumerate(ls):
            textos.append({"s": s, "x": L["x"] + 12 + MUESTRA_W + 9, "y": yc + 0.28 * FS + j * IL,
                           "estilo": "normal", "color": TINTA, "dentro": "leyenda", "pieza": ("leyenda", clase, j)})
        yy += FILA_LEY + (len(ls) - 1) * IL
    alto = math.ceil(max(L["y"] + L["h"], max(c["y"] + c["h"] for c in C.values())) + MARGEN)
    return {"cajas": C, "flechas": T, "textos": textos, "pastillas": pastillas, "leyenda": L, "alto": alto,
            "y_in": y_in}


# ========================================================================== #
# Controles                                                                  #
# ========================================================================== #
def rect(c: dict) -> tuple:
    return (c["x"], c["y"], c["x"] + c["w"], c["y"] + c["h"])


def rect_texto(t: dict) -> tuple:
    a = ancho(t["s"], t["estilo"])
    asc, desc = (ASC_MONO, DESC_MONO) if t["estilo"] == "mono" else (ASC, DESC)
    return (t["x"], t["y"] - asc * FS, t["x"] + a, t["y"] + desc * FS)


def cruza(a, b) -> bool:
    return a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]


def ampliar(r, d) -> tuple:
    return (r[0] - d, r[1] - d, r[2] + d, r[3] + d)


def dist_rects(a, b) -> float:
    return math.hypot(max(b[0] - a[2], 0.0, a[0] - b[2]), max(b[1] - a[3], 0.0, a[1] - b[3]))


def rect_tramo(p, q, g) -> tuple:
    return (min(p[0], q[0]) - g, min(p[1], q[1]) - g, max(p[0], q[0]) + g, max(p[1], q[1]) + g)


def contenedores(M: dict) -> dict:
    out = {k: rect(c) for k, c in M["cajas"].items()}
    for c in M["cajas"].values():
        if c.get("recuadro"):
            out[f"recuadro {c['clave']}"] = rect(c["recuadro"])
    for p in M["pastillas"]:
        out[p["clave"]] = rect(p)
    out["leyenda"] = rect(M["leyenda"])
    return out


def controlar(M: dict, E: dict) -> dict:
    rep = {}
    # contenido
    for k, pars in PARRAFOS.items():
        if " ".join(pars) != TEXTO_GENERAL[k]:
            fallar("contenido", f"los renglones de {k} no reconstruyen su línea general")
        dib = " ".join(t["s"] for t in M["textos"] if t["pieza"][:2] == ("general", k))
        if dib != TEXTO_GENERAL[k]:
            fallar("contenido", f"la línea general de {k} dibujada no es la fijada: {dib!r}")
    for t in M["textos"]:
        for rx in PROHIBIDOS:
            if rx.search(t["s"]):
                fallar("contenido", f"«{t['s']}» lleva {rx.pattern!r}")
    # textos: letra, dentro de su contenedor, sin superposición
    if pt(FS) < 7.5 or pt(FS) < PT_MINIMO:
        fallar("textos", f"letra de {pt(FS):.2f} pt")
    cont = contenedores(M)
    R = [(t, rect_texto(t)) for t in M["textos"]]
    holg_min = math.inf
    for t, r in R:
        c = cont[t["dentro"]]
        h = min(r[0] - c[0], c[2] - r[2], r[1] - c[1], c[3] - r[3])
        holg_min = min(holg_min, h)
        if h < HOLGURA_TEXTO:
            fallar("textos", f"«{t['s']}» a {h:.1f} del borde de «{t['dentro']}»")
    for i in range(len(R)):
        for j in range(i + 1, len(R)):
            if cruza(R[i][1], R[j][1]):
                fallar("textos", f"«{R[i][0]['s']}» se superpone con «{R[j][0]['s']}»")
    for p in M["pastillas"]:
        for t, r in R:
            if t["dentro"] != p["clave"] and cruza(r, rect(p)):
                fallar("textos", f"«{t['s']}» se superpone con la pastilla «{p['tipo']}»")
        if not (cont[p["dentro"]][0] <= p["x"] and p["x"] + p["w"] <= cont[p["dentro"]][2]):
            fallar("textos", f"la pastilla «{p['tipo']}» sale de su recuadro")
    rep["textos"] = {"n": len(R), "holgura_minima": holg_min, "pt": pt(FS)}
    # cajas
    cajas = [(k, rect(c), GROSOR_CAJA) for k, c in M["cajas"].items()] + [("leyenda", rect(M["leyenda"]), 1.0)]
    sep_min = math.inf
    for i in range(len(cajas)):
        for j in range(i + 1, len(cajas)):
            d = dist_rects(cajas[i][1], cajas[j][1]) - (cajas[i][2] + cajas[j][2]) / 2.0
            sep_min = min(sep_min, d)
            if cruza(cajas[i][1], cajas[j][1]) or d < SEP_CAJAS:
                fallar("cajas", f"«{cajas[i][0]}» y «{cajas[j][0]}» a {d:.1f} (< {SEP_CAJAS})")
    rep["cajas"] = {"n": len(cajas), "separacion_minima": sep_min}
    # flechas
    g = GROSOR_FLUJO / 2.0
    tramos = []
    for t in M["flechas"]:
        pts = t["puntos"]
        for p, q in zip(pts, pts[1:]):
            if p == q or (p[0] != q[0] and p[1] != q[1]):
                fallar("flechas", f"tramo nulo o diagonal en {t['desde']} → {t['hasta']}")
            tramos.append((t, p, q))
        A, B = rect(M["cajas"][t["desde"]]), rect(M["cajas"][t["hasta"]])
        p0, p1 = pts[0], pts[1]
        if not (p0[1] == A[3] and A[0] + LEJOS_ESQUINA <= p0[0] <= A[2] - LEJOS_ESQUINA and p1[1] > p0[1]):
            fallar("flechas", f"{t['desde']} → {t['hasta']} no sale del borde de abajo de {t['desde']}")
        q0, q1 = pts[-2], pts[-1]
        dx, dy = (q1[0] > q0[0]) - (q1[0] < q0[0]), (q1[1] > q0[1]) - (q1[1] < q0[1])
        ll = (q1[0] + HUECO_PUNTA * dx, q1[1] + HUECO_PUNTA * dy)
        en_arriba = dy == 1 and ll[1] == B[1] and B[0] + LEJOS_ESQUINA <= ll[0] <= B[2] - LEJOS_ESQUINA
        en_derecha = dx == -1 and ll[0] == B[2] and B[1] + LEJOS_ESQUINA <= ll[1] <= B[3] - LEJOS_ESQUINA
        if not (en_arriba or en_derecha):
            fallar("flechas", f"{t['desde']} → {t['hasta']} no llega al borde de {t['hasta']}")
    for t, p, q in tramos:
        for k, r, _ in cajas:
            if cruza(rect_tramo(p, q, 0.0), ampliar(r, -1.0)):
                fallar("flechas", f"{t['desde']} → {t['hasta']} atraviesa «{k}»")
    for i in range(len(tramos)):
        for j in range(i + 1, len(tramos)):
            (a, p, q), (b, u, v) = tramos[i], tramos[j]
            if a is b:
                continue
            comun = {a["desde"], a["hasta"]} & {b["desde"], b["hasta"]}
            if cruza(rect_tramo(p, q, g), rect_tramo(u, v, g)) and not comun:
                fallar("flechas", f"{a['desde']} → {a['hasta']} toca {b['desde']} → {b['hasta']}")
    for t, r in R:
        for fl, p, q in tramos:
            if dist_rects(r, rect_tramo(p, q, g)) < HOLGURA_TEXTO:
                fallar("flechas", f"«{t['s']}» toca la flecha {fl['desde']} → {fl['hasta']}")
    rep["flechas"] = {"n": len(M["flechas"]), "tramos": len(tramos)}
    # margen y alto
    todo = [r for _, r, _ in cajas] + [r for _, r in R] + [rect_tramo(p, q, g) for _, p, q in tramos]
    mins = {"izquierdo": min(r[0] for r in todo), "superior": min(r[1] for r in todo),
            "derecho": min(W - r[2] for r in todo), "inferior": min(M["alto"] - r[3] for r in todo)}
    for b, d in mins.items():
        if d < MARGEN_MIN:
            fallar("margen", f"algo a {d:.1f} unidades del borde {b} (< {MARGEN_MIN:.1f})")
    rep["margen"] = mins
    alto_cm = ANCHO_CM * M["alto"] / W
    if alto_cm > ALTO_MAX_CM:
        fallar("alto", f"{alto_cm:.2f} cm de alto (> {ALTO_MAX_CM})")
    rep["alto_cm"] = alto_cm
    return rep


# ========================================================================== #
# SVG                                                                        #
# ========================================================================== #
def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def path_redondeado(puntos) -> str:
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


def caja_svg(r: dict, relleno: str, borde: str, grosor, rx, guiones=None, dato="") -> str:
    dash = f' stroke-dasharray="{guiones}"' if guiones else ""
    return (f'<rect{dato} x="{f(r["x"])}" y="{f(r["y"])}" width="{f(r["w"])}" height="{f(r["h"])}" '
            f'fill="{relleno}" stroke="{borde}" stroke-width="{grosor}" rx="{rx}"{dash}/>')


def texto_svg(t: dict) -> str:
    extra = {"normal": "", "negrita": ' font-weight="bold"', "cursiva": ' font-style="italic"',
             "mono": f' font-family="{MONO}" font-weight="bold"'}[t["estilo"]]
    return (f'<text x="{f(t["x"])}" y="{f(t["y"])}" font-size="{FS}"{extra} fill="{t["color"]}">'
            f'{esc(t["s"])}</text>')


def dibujar(M: dict) -> str:
    alto = M["alto"]
    partes = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{ANCHO_CM:.2f}cm" '
              f'height="{ANCHO_CM * alto / W:.2f}cm" viewBox="0 0 {W} {alto}" font-family="{TIPOGRAFIA}">',
              f'<rect width="{W}" height="{alto}" fill="white"/>',
              f'<defs><marker id="arN" {MARCADOR} fill="{FLECHA}"/></marker></defs>']
    for k in CARRIL_ENTIDAD + CARRIL_SUJETO:
        c = M["cajas"][k]
        pal = PALETA[c["clase"]]
        partes.append(caja_svg(c, pal["relleno"], pal["borde"], GROSOR_CAJA, RX, dato=f' data-caja="{k}"'))
        if c.get("recuadro"):
            partes.append(caja_svg(c["recuadro"], MARCO["relleno"], MARCO["borde"], MARCO["grosor"], MARCO["rx"],
                                   dato=f' data-recuadro="{k}"'))
    for p in M["pastillas"]:
        partes.append(caja_svg(p, p["relleno"], p["borde"], GROSOR_CAJA, PASTILLA_RX, guiones=p["guiones"],
                               dato=f' data-pastilla="{p["tipo"]}"'))
    for t in M["flechas"]:
        partes.append(f'<path data-flecha="{t["desde"]}-{t["hasta"]}" d="{path_redondeado(t["puntos"])}" '
                      f'fill="none" stroke="{FLECHA}" stroke-width="{GROSOR_FLUJO}" marker-end="url(#arN)"/>')
    L = M["leyenda"]
    partes.append(caja_svg(L, MARCO["relleno"], MARCO["borde"], MARCO["grosor"], MARCO["rx"]))
    for m in L["muestras"]:
        if m["clase"] == "ejemplo":
            # Una caja azul con su recuadro blanco: así se ve el ejemplo en la figura.
            partes.append(caja_svg(m, DETERMINISTICA["relleno"], DETERMINISTICA["borde"], GROSOR_CAJA, 3,
                                   dato=' data-muestra="ejemplo"'))
            dentro = {"x": m["x"] + 4, "y": m["y"] + 4, "w": m["w"] - 8, "h": m["h"] - 8}
            partes.append(caja_svg(dentro, MARCO["relleno"], MARCO["borde"], MARCO["grosor"], 2))
        else:
            pal = PALETA[m["clase"]]
            partes.append(caja_svg(m, pal["relleno"], pal["borde"], GROSOR_CAJA, 3,
                                   dato=f' data-muestra="{m["clase"]}"'))
    for t in M["textos"]:
        partes.append(texto_svg(t))
    return "\n".join(partes + ["</svg>"]) + "\n"


def controlar_registro(svg: str, M: dict) -> dict:
    """El SVG se relee: los textos son exactamente los del modelo, en orden, y
    cada caja tiene el color de su clase."""
    ns = "{http://www.w3.org/2000/svg}"
    raiz = ET.fromstring(svg)
    textos = [el.text for el in raiz.iter(ns + "text")]
    if textos != [t["s"] for t in M["textos"]]:
        fallar("registro", "los textos del SVG no son los del modelo")
    for el in raiz.iter(ns + "rect"):
        k = el.get("data-caja")
        if k and (el.get("fill"), el.get("stroke")) != tuple(PALETA[CLASE[k]].values()):
            fallar("registro", f"la caja {k} no tiene el color de su clase")
    for el in raiz.iter(ns + "rect"):
        t = el.get("data-pastilla")
        if t and el.get("stroke") != M["pastillas"][[p["tipo"] for p in M["pastillas"]].index(t)]["borde"]:
            fallar("registro", f"la pastilla {t} no tiene el borde de su tipo")
    return {"textos": len(textos), "flechas": len(list(raiz.iter(ns + "path"))) - 1}


# ========================================================================== #
# Exportación                                                                #
# ========================================================================== #
def grabar_densidad(ruta: str, dpi: int) -> None:
    """Inserta el bloque pHYs (píxeles por metro) después de IHDR, como
    generar_figura_proceso.py:1190-1211."""
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


def exportar(ruta_svg: str, ruta_png: str, ruta_pdf: str) -> None:
    rsvg = shutil.which("rsvg-convert")
    if not rsvg:
        fallar("exportacion", "rsvg-convert no está instalado")
    subprocess.run([rsvg, "-w", str(ANCHO_PNG_PX), "-f", "png", "-o", ruta_png, ruta_svg], check=True)
    grabar_densidad(ruta_png, DPI)
    subprocess.run([rsvg, "-f", "pdf", "-o", ruta_pdf, ruta_svg], check=True,
                   env=dict(os.environ, SOURCE_DATE_EPOCH=SOURCE_DATE_EPOCH))


def png_dimensiones(ruta: str) -> tuple[int, int]:
    with open(ruta, "rb") as fh:
        return struct.unpack(">II", fh.read(24)[16:24])


# ========================================================================== #
# Principal                                                                  #
# ========================================================================== #
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--commit", required=True, help="commit del que se leen todas las fuentes")
    ap.add_argument("--grafo", required=True, help="ruta del kg.json o kg.json.gz en el commit")
    ap.add_argument("--sha256-grafo", default=None, help="candado del grafo: sha256 del kg.json")
    ap.add_argument("--extraccion", default=EXTRACCION_POR_OMISION, help="extracción validada (jsonl) en el commit")
    ap.add_argument("--unidad-entidad", default=UNIDAD_ENTIDAD)
    ap.add_argument("--unidad-sujeto", default=UNIDAD_SUJETO)
    ap.add_argument("--salida", default=AQUI, help="directorio del SVG, el PNG y el PDF (por omisión, el del script)")
    args = ap.parse_args()
    if args.sha256_grafo is None and args.grafo == GRAFO_POR_OMISION[0]:
        args.sha256_grafo = GRAFO_POR_OMISION[1]
    try:
        commit = resolver_commit(args.commit)
        estilo = leer_estilo(commit)
        E = leer_ejemplo(commit, args)
        M = armar_modelo(E, estilo)
        rep = controlar(M, E)
        svg = dibujar(M)
        rep["registro"] = controlar_registro(svg, M)
    except Falla as e:
        print(f"ALTO {e}")
        print("No se escribe nada.")
        return 1

    print(f"COMMIT: {commit}")
    print("FUENTES (ruta en el commit, sha256):")
    for k, (ruta, sha) in E["fuentes"].items():
        print(f"  {k:11s} {ruta}  {sha}")
    print("ESTILO (cada valor, con la línea que lo declara en el commit):")
    for k, v in estilo["lugares"].items():
        print(f"  {k:24s} {v}")
    for t, p in estilo["pastillas"].items():
        print(f"  pastilla {t:15s} relleno {p['relleno']}, borde {p['borde']}"
              + (f", discontinuo {p['guiones']}" if p["guiones"] else ""))
    print("EJEMPLO:")
    for k, v in E["entidad"].items():
        print(f"  entidad.{k} = {v!r}")
    for k, v in E["sujeto"].items():
        print(f"  sujeto.{k} = {v!r}")
    for a in E["avisos"]:
        print(f"  AVISO {a}")
    print("TEXTOS DIBUJADOS:")
    for t in M["textos"]:
        print(f"  [{t['pieza'][0]} {t['pieza'][1]}] {t['s']}")
    print(f"CONTROLES: textos {rep['textos']['n']} a {rep['textos']['pt']:.2f} pt, holgura mínima "
          f"{rep['textos']['holgura_minima']:.1f}; cajas {rep['cajas']['n']}, separación mínima "
          f"{rep['cajas']['separacion_minima']:.1f}; flechas {rep['flechas']['n']} ({rep['flechas']['tramos']} "
          f"tramos); margen mínimo " + ", ".join(f"{b} {d:.1f}" for b, d in rep["margen"].items())
          + f"; registro {rep['registro']}")
    os.makedirs(args.salida, exist_ok=True)
    rutas = {ext: os.path.join(args.salida, f"{NOMBRE}.{ext}") for ext in ("svg", "png", "pdf")}
    with open(rutas["svg"], "w", encoding="utf-8", newline="\n") as fh:
        fh.write(svg)
    try:
        exportar(rutas["svg"], rutas["png"], rutas["pdf"])
    except Falla as e:
        print(f"ALTO {e}")
        return 1
    wpx, hpx = png_dimensiones(rutas["png"])
    print(f"TAMAÑO: lienzo {W} × {M['alto']}; impreso {ANCHO_CM:.2f} × {rep['alto_cm']:.2f} cm "
          f"(tope {ALTO_MAX_CM} cm); PNG {wpx} × {hpx} px a {DPI} dpi")
    for ext in ("svg", "png", "pdf"):
        with open(rutas[ext], "rb") as fh:
            print(f"{ext.upper()}: {rutas[ext]}  sha256 {sha256(fh.read())}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
