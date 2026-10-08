#!/usr/bin/env python3
"""Figura «las unidades del ejemplo» para el análisis del documento (capítulo 3, sección 3.2).

Dos unidades de Clasificación de deudores, una debajo de la otra, tal como las
arma el artefacto de unidades con el que se construyó el grafo r1:
- arriba, «Unidad de extracción del punto 5.1.1.1»: en gris, la herencia del
  punto terminal en tres bloques (el título de la sección; el título y el
  párrafo sin numerar del 5.1; el título y el párrafo sin numerar del 5.1.1);
  en negro, el texto completo del 5.1.1.1. Al margen, un rótulo por bloque y
  una llave que agrupa los tres bloques grises bajo «cadena estructural»;
- abajo, «Unidad de extracción del párrafo del 5.1.1»: en gris, los títulos
  de la sección 5, del 5.1 y del 5.1.1; en negro, solo el párrafo sin numerar
  del 5.1.1. Al margen, un rótulo por bloque y una llave que agrupa los tres
  bloques grises bajo «títulos que ubican el párrafo».
Debajo de cada unidad, su lugar en el documento, precedido de «Lugar:». Gris
es la herencia y negro
es el texto, tal como los recibe el modelo en cada unidad. La figura no muestra
nada de la salida de la extracción ni tipos o nombres de nodos.

Nada del contenido se tipea ni se supone:
- el artefacto de unidades es salida_enm01/chunks_cla.json, con candado de
  sha256 (CHUNKS_SHA256); el script comprueba que las unidades que la E1 de r1
  procesó para cla (extracciones_e1.jsonl de corpus_v2/salida, con su propio
  candado) son exactamente las de este artefacto;
- la composición de cada unidad (qué tramos de la herencia lleva, en qué orden
  y con qué tipo) debe ser la fijada en UNIDADES; si el artefacto arma una
  unidad de otra manera, el script frena;
- el texto de cada bloque es el del artefacto, transcripto tal cual y con sus
  saltos de línea; el script lo reconstruye desde lo dibujado y lo compara con
  el artefacto, y comprueba que cada tramo esté en la página 16 del PDF del
  corpus (candado de sha256 e inventario del conjunto de desarrollo). Si un
  tramo está en la página solo después de normalizar blancos y guiones de fin
  de línea, informa la diferencia y dibuja lo que dice el artefacto; si no
  está ni así, frena;
- el texto propio de la figura (títulos, rótulos, llaves, lugar) es fijo; el
  script deriva de cada unidad el texto esperado (números de punto, clase de
  bloque, nombre del Texto Ordenado según la portada) y frena si no coincide.

Controles, en cada corrida (el script frena si fallan), con las métricas
reales de Helvetica: ningún texto por debajo de 7 pt impresos a 15 cm, fuera
del lienzo, superpuesto a otro, fuera de la caja que lo contiene, cortado por
el borde de otra caja ni tocado por una llave; ningún texto ni elemento
dibujado a menos de 2 mm (MARGEN_MM, a 15 cm de ancho) de uno de los cuatro
bordes; ningún texto con nombres de archivo, rutas o identificadores internos.
Los controles de geometría y de margen son los de
generar_figura_formacion_to.py.

Reutiliza por importación, como las figuras de la página del ejemplo y de cómo
se forma un Texto Ordenado: de generar_figura_norma_a_grafo.py, la tipografía,
el escape y formato del SVG, la tabla de métricas, la exportación a PNG a
300 dpi con la densidad grabada y el medidor con métricas reales de
Helvetica; de generar_figura_proceso_extraccion.py, el ancho de texto de
15 cm.

El SVG es intermedio: se pasa a rsvg-convert por la entrada estándar y no se
escribe salvo con --svg. Salidas: figura_unidad_extraccion.png y
figura_unidad_extraccion.pdf, las dos byte-reproducibles (el PDF, con la fecha
de creación fijada por SOURCE_DATE_EPOCH).

Uso (desde la raíz del repo):
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_unidad_extraccion.py
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_unidad_extraccion.py --svg <ruta>
"""

import argparse
import hashlib
import json
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
SALIDA_PNG = os.path.join(AQUI, "figura_unidad_extraccion.png")
SALIDA_PDF = os.path.join(AQUI, "figura_unidad_extraccion.pdf")

# --------------------------------------------------------------------------- #
# Fuentes y candados                                                           #
# --------------------------------------------------------------------------- #
REL_PDF = "data/experiment/subset/TO_clasificacion_deudores_actual.pdf"
REL_INVENTARIO = "data/experiment/reextraccion_v2/manifiestos/desarrollo_5tos.json"
REL_CHUNKS = "data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_cla.json"
REL_E1_R1 = "data/experiment/reextraccion_v2/corpus_v2/salida/cla/extracciones_e1.jsonl"
PDF_SHA256 = "6e7f528d3fea7b756f15e1278eecd828f203f0651fc6f778212033de6a0883e2"
CHUNKS_SHA256 = "98808886a406d8321c678836a55f92eea983d594d95358dd21ceb537487ac0b1"
E1_R1_SHA256 = "3346f7fbd6fff7869fb07baafa2497af90b4047a597169337b547f6f6d825f45"
TO = "cla"
# Versión del corpus: la portada debe decir las dos cosas.
PORTADA = ("“A” 8378", "19/12/2025")
# Nombre del Texto Ordenado en los rótulos de lugar: el de la portada, en
# minúsculas salvo la inicial.
NOMBRE_TO = "Clasificación de deudores"
PAGINA = 16

# Las dos unidades. Para cada bloque gris, los tramos de la herencia que lo
# forman, como (tipo, unidad de origen), en el orden del artefacto, y su
# rótulo; luego el rótulo del texto, la llave y el lugar. Todo el texto propio
# se comprueba contra lo que se deriva de la unidad (comprobar_textos_fijos).
UNIDADES = (
    {"clave": "terminal", "id": f"{TO}::5.1.1.1", "tipo": "punto_terminal", "unidad": "5.1.1.1",
     "titulo": "Unidad de extracción del punto 5.1.1.1",
     "grises": (((("encabezado", "S5"),), "título de la sección"),
                ((("encabezado", "5.1"), ("intro", "5.1")), "texto del 5.1"),
                ((("encabezado", "5.1.1"), ("intro", "5.1.1")), "texto del 5.1.1")),
     "rotulo_texto": "texto del 5.1.1.1",
     "llave": ("cadena", "estructural"),
     "lugar": "Lugar: Clasificación de deudores, punto 5.1.1.1"},
    {"clave": "bloque", "id": f"{TO}::5.1.1::intro", "tipo": "mini_chunk", "unidad": "5.1.1",
     "titulo": "Unidad de extracción del párrafo del 5.1.1",
     "grises": (((("encabezado", "S5"),), "título de la sección"),
                ((("encabezado", "5.1"),), "título del 5.1"),
                ((("encabezado", "5.1.1"),), "título del 5.1.1")),
     "rotulo_texto": "párrafo sin numerar del 5.1.1",
     "llave": ("títulos", "que ubican", "el párrafo"),
     "lugar": "Lugar: Clasificación de deudores, punto 5.1.1"},
)
# Rótulo de la llave de cada clase de unidad (en la figura, partido en líneas
# para que entre a la derecha de la llave).
TEXTO_LLAVE = {"punto_terminal": "cadena estructural",
               "mini_chunk": "títulos que ubican el párrafo"}
# Nada de esto puede aparecer en un texto dibujado (decisión 6 del mandato).
PROHIBIDOS = (re.compile(r"extractor", re.I), re.compile(r"::"), re.compile(r"\.(json|pdf|py|md)\b"),
              re.compile(r"/"), re.compile(r"\bcla\b"), re.compile(r"chunk", re.I))

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
TINTA = "#1f1f1f"                   # negro: el texto de la unidad
TINTA_SUAVE = "#555555"             # gris: la herencia, los rótulos, las llaves y el lugar
esc, f = base.esc, base.f

FS_TITULO = 14          # título de cada unidad, en negrita (8,27 pt impresos)
FS = 13                 # texto transcripto, rótulos y lugar (7,68 pt impresos)
IL = 16                 # interlínea de FS
PAD_X = 7               # aire interior de los bloques
PAD_Y = 5
SEP_TITULO = 6          # entre el título de la unidad y su primer bloque
SEP_GRIS = 4            # entre bloques grises
SEP_TEXTO = 9           # entre la herencia y el texto
SEP_LUGAR = 6           # entre el último bloque y el lugar
SEP_UNIDAD = 24         # entre las dos unidades
X_BLOQUE = MARGEN
W_BLOQUE = 480          # la línea más larga del texto transcripto mide 462,5 a FS
CALLE = 10              # entre los bloques y los rótulos
X_ROT = X_BLOQUE + W_BLOQUE + CALLE
SEP_LLAVE = 8           # entre el rótulo más ancho de la herencia y la llave
ANCHO_LLAVE = 10
R_LLAVE = 5
SEP_ROT_LLAVE = 6       # entre la punta de la llave y su rótulo

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


# --------------------------------------------------------------------------- #
# Carga y comprobaciones                                                       #
# --------------------------------------------------------------------------- #
def anclas_artefacto(ids):
    """Línea del artefacto donde está cada texto de cada unidad: el `texto`
    propio (sangría de 2) y el de cada tramo de la herencia (sangría de 4), en
    orden. Se comprueba que la línea decodificada dé ese texto."""
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
        out[cid] = {"texto": propio, "herencia": herencia}
    return out


def comprobar_textos_fijos(u, ch, portada_nombre):
    """El texto propio de la figura se deriva de la unidad: números de punto,
    clase de cada bloque y nombre del Texto Ordenado."""
    def rotulo_esperado(tramos):
        tipos = [t for t, _ in tramos]
        origen = {o for _, o in tramos}
        if len(origen) != 1:
            raise SystemExit(f"{u['id']}: un bloque gris mezcla tramos de unidades distintas {tramos}")
        o = origen.pop()
        if o.startswith("S") and tipos == ["encabezado"]:
            return "título de la sección"
        if tipos == ["encabezado"]:
            return f"título del {o}"
        if tipos == ["encabezado", "intro"]:
            return f"texto del {o}"
        raise SystemExit(f"{u['id']}: bloque gris sin rótulo previsto {tramos}")
    for tramos, rotulo in u["grises"]:
        if rotulo != rotulo_esperado(tramos):
            raise SystemExit(f"rótulo {rotulo!r} ≠ {rotulo_esperado(tramos)!r}")
    if u["tipo"] == "punto_terminal":
        esperados = {"titulo": f"Unidad de extracción del punto {u['unidad']}",
                     "rotulo_texto": f"texto del {u['unidad']}"}
    else:
        esperados = {"titulo": f"Unidad de extracción del párrafo del {u['unidad']}",
                     "rotulo_texto": f"párrafo sin numerar del {u['unidad']}"}
    if u["llave"] is None or " ".join(u["llave"]) != TEXTO_LLAVE[u["tipo"]]:
        raise SystemExit(f"{u['id']}: la llave no es «{TEXTO_LLAVE[u['tipo']]}»")
    esperados["lugar"] = f"Lugar: {NOMBRE_TO}, punto {u['unidad']}"
    for k, v in esperados.items():
        if u[k] != v:
            raise SystemExit(f"{u['id']}: {k} {u[k]!r} ≠ {v!r}")
    if NOMBRE_TO.upper() != portada_nombre:
        raise SystemExit(f"el nombre {NOMBRE_TO!r} no es el de la portada {portada_nombre!r}")
    if ch["unidad"] != u["unidad"] or ch["tipo"] != u["tipo"]:
        raise SystemExit(f"{u['id']}: unidad o tipo ≠ artefacto ({ch['unidad']}, {ch['tipo']})")


def resolver():
    candado(REL_PDF, PDF_SHA256)
    candado(REL_CHUNKS, CHUNKS_SHA256)
    candado(REL_E1_R1, E1_R1_SHA256)
    with open(os.path.join(RAIZ, REL_INVENTARIO), encoding="utf-8") as fh:
        inv = [t for t in json.load(fh)["tos"] if t["id"] == TO]
    if len(inv) != 1 or inv[0]["sha256_pdf"] != PDF_SHA256 or inv[0]["pdf"] != REL_PDF:
        raise SystemExit("el inventario del conjunto de desarrollo no declara este PDF para cla")
    with open(os.path.join(RAIZ, REL_CHUNKS), encoding="utf-8") as fh:
        lista = json.load(fh)
    chunks = {c["id"]: c for c in lista}
    if len(chunks) != len(lista):
        raise SystemExit("artefacto: ids repetidos")

    # Las unidades que la E1 de r1 procesó para cla son las de este artefacto.
    with open(os.path.join(RAIZ, REL_E1_R1), encoding="utf-8") as fh:
        registros = [json.loads(x) for x in fh if x.strip()]
    ids_e1 = {r["chunk_id"] for r in registros}
    if ids_e1 != set(chunks):
        raise SystemExit("la E1 de r1 no procesó exactamente las unidades de este artefacto")
    tipos_e1 = {(r["chunk_id"], r["tipo_unidad"]) for r in registros}
    for u in UNIDADES:
        if (u["id"], u["tipo"]) not in tipos_e1:
            raise SystemExit(f"la E1 de r1 no procesó {u['id']} como {u['tipo']}")

    with pdfplumber.open(os.path.join(RAIZ, REL_PDF)) as doc:
        portada = [l["text"] for l in doc.pages[0].extract_text_lines()]
        if not all(any(p in x for x in portada) for p in PORTADA):
            raise SystemExit(f"la portada no dice la versión del corpus {PORTADA}")
        pg = doc.pages[PAGINA - 1]
        crudo = pg.extract_text()
        lineas_pdf = [l["text"] for l in pg.extract_text_lines()]

    # Composición de cada unidad: la herencia tiene exactamente los tramos
    # fijados, en ese orden; el texto es el propio de la unidad.
    for u in UNIDADES:
        ch = chunks[u["id"]]
        comprobar_textos_fijos(u, ch, portada[0])
        esperada = [t for tramos, _ in u["grises"] for t in tramos]
        real = [(h["tipo"], h["unidad_origen"]) for h in ch["herencia"]]
        if real != esperada:
            raise SystemExit(f"{u['id']}: el artefacto arma la herencia de otra manera: {real}")
        if ch["paginas"] != [PAGINA] or any(h["paginas"] != [PAGINA] for h in ch["herencia"]):
            raise SystemExit(f"{u['id']}: el artefacto no la pone entera en la página {PAGINA}")
    term, blq = (chunks[u["id"]] for u in UNIDADES)
    if not term["texto"].startswith(f"{term['unidad']}. {term['titulo']}\n"):
        raise SystemExit("el texto del punto terminal no empieza con su número y su título")
    if blq["rol_bloque"] != "intro" or any(RX_NUMERO.match(x) for x in blq["texto"].split("\n")):
        raise SystemExit("el texto de la unidad estructural no es solo un párrafo sin numerar")
    # Los títulos que la unidad estructural hereda son los mismos que hereda el
    # punto terminal.
    titulos_term = {h["unidad_origen"]: h["texto"] for h in term["herencia"] if h["tipo"] == "encabezado"}
    if any(titulos_term.get(h["unidad_origen"]) != h["texto"] for h in blq["herencia"]):
        raise SystemExit("los títulos heredados de las dos unidades no coinciden")

    # Cada tramo, contra la página del PDF.
    anclas = anclas_artefacto([u["id"] for u in UNIDADES])
    tramos = []
    for u in UNIDADES:
        ch = chunks[u["id"]]
        a = anclas[u["id"]]
        piezas = [(f"herencia {k + 1}: {h['tipo']} de {h['unidad_origen']}", h["texto"], a["herencia"][k])
                  for k, h in enumerate(ch["herencia"])] + [("texto", ch["texto"], a["texto"])]
        if len(a["herencia"]) != len(ch["herencia"]):
            raise SystemExit(f"{u['id']}: anclas de la herencia incompletas")
        for nombre, s, (linea_art, s_art) in piezas:
            if s_art != s:
                raise SystemExit(f"{u['id']} {nombre}: la línea {linea_art} del artefacto no da ese texto")
            exacto = s in crudo
            por_linea = [lineas_pdf.index(x) + 1 if x in lineas_pdf else None for x in s.split("\n")]
            if not exacto and norm(s) not in norm(crudo):
                raise SystemExit(f"{u['id']} {nombre}: no está en la página {PAGINA} del PDF")
            tramos.append({"unidad": u["clave"], "nombre": nombre, "texto": s,
                           "linea_artefacto": linea_art, "exacto": exacto,
                           "lineas_pdf": por_linea})
    return {"chunks": chunks, "portada": portada, "tramos": tramos, "n_e1": len(registros),
            "n_ids_e1": len(ids_e1)}


# --------------------------------------------------------------------------- #
# Composición                                                                  #
# --------------------------------------------------------------------------- #
REGISTRO = []   # textos dibujados
CAJAS = {}      # cajas que contienen texto: clave -> (x0, y0, x1, y1)
MARCAS = []     # trazos que ningún texto puede tocar: (nombre, caja)


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


def bloque(partes, clave, y, lineas, gris):
    """Un bloque: caja y sus líneas, tal como vienen. Devuelve su borde inferior."""
    alto = 2 * PAD_Y + FS + (len(lineas) - 1) * IL
    if gris:
        rect(partes, X_BLOQUE, y, X_BLOQUE + W_BLOQUE, y + alto, BORDE, "1", FONDO_BLOQUE, rx=2)
    else:
        rect(partes, X_BLOQUE, y, X_BLOQUE + W_BLOQUE, y + alto, TRAZO, "1.3", "white", rx=2)
    CAJAS[clave] = (X_BLOQUE, y, X_BLOQUE + W_BLOQUE, y + alto)
    yb = y + PAD_Y + FS * 0.78
    for s, fuente in lineas:
        texto(partes, X_BLOQUE + PAD_X, yb, s, FS, relleno=TINTA_SUAVE if gris else TINTA,
              contexto=clave, dentro=clave, fuente=fuente)
        yb += IL
    return y + alto


def rotulo(partes, y0, y1, s, contexto):
    texto(partes, X_ROT, (y0 + y1) / 2.0 + FS * 0.36, s, FS, relleno=TINTA_SUAVE,
          contexto=contexto)


def llave(partes, x0, y0, y1, nombre):
    """Llave que abre a la izquierda y apunta a la derecha, de y0 a y1."""
    x1, x2, ym, r = x0 + ANCHO_LLAVE / 2.0, x0 + ANCHO_LLAVE, (y0 + y1) / 2.0, R_LLAVE
    d = (f"M{f(x0)},{f(y0)} Q{f(x1)},{f(y0)} {f(x1)},{f(y0 + r)} L{f(x1)},{f(ym - r)} "
         f"Q{f(x1)},{f(ym)} {f(x2)},{f(ym)} Q{f(x1)},{f(ym)} {f(x1)},{f(ym + r)} "
         f"L{f(x1)},{f(y1 - r)} Q{f(x1)},{f(y1)} {f(x0)},{f(y1)}")
    partes.append(f'<path d="{d}" fill="none" stroke="{TRAZO}" stroke-width="1.2"/>')
    MARCAS.append((nombre, (x0 - 0.6, y0 - 0.6, x2 + 0.6, y1 + 0.6)))
    return x2, ym


def componer_unidad(partes, u, ch, y):
    clave = u["clave"]
    yt = y + FS_TITULO * 0.78
    texto(partes, X_BLOQUE, yt, u["titulo"], FS_TITULO, True, contexto=f"título {clave}")
    y = yt + FS_TITULO * 0.22 + SEP_TITULO
    k = 0
    y_cadena = y
    for i, (tramos, rot) in enumerate(u["grises"], start=1):
        lineas = []
        for _ in tramos:
            lineas += [(x, (clave, "herencia", k)) for x in ch["herencia"][k]["texto"].split("\n")]
            k += 1
        y_fin = bloque(partes, f"{clave} gris {i}", y, lineas, gris=True)
        rotulo(partes, y, y_fin, rot, f"rótulo {clave}")
        y = y_fin + SEP_GRIS
    y_fin_cadena = y - SEP_GRIS
    y = y_fin_cadena + SEP_TEXTO
    lineas = [(x, (clave, "texto", None)) for x in ch["texto"].split("\n")]
    y_fin = bloque(partes, f"{clave} texto", y, lineas, gris=False)
    rotulo(partes, y, y_fin, u["rotulo_texto"], f"rótulo {clave}")
    if u["llave"]:
        rotulos_cadena = [r for _, r in u["grises"]]
        x_llave = X_ROT + max(base.ancho(r, FS) for r in rotulos_cadena) + SEP_LLAVE
        x_punta, ym = llave(partes, x_llave, y_cadena, y_fin_cadena, f"llave {clave}")
        n = len(u["llave"])
        for j, s in enumerate(u["llave"]):
            yb = ym + (j - (n - 1) / 2.0) * IL + FS * 0.36
            texto(partes, x_punta + SEP_ROT_LLAVE, yb, s, FS, relleno=TINTA_SUAVE,
                  contexto=f"llave {clave}")
    yl = y_fin + SEP_LUGAR + FS * 0.78
    texto(partes, X_BLOQUE, yl, u["lugar"], FS, relleno=TINTA_SUAVE, contexto=f"lugar {clave}")
    return yl + FS * 0.22


def componer(res):
    del REGISTRO[:]
    CAJAS.clear()
    del MARCAS[:]
    partes = []
    y = MARGEN
    for i, u in enumerate(UNIDADES):
        if i:
            y += SEP_UNIDAD
        y = componer_unidad(partes, u, res["chunks"][u["id"]], y)
    alto_total = y + MARGEN
    alto_cm = ANCHO_FIGURA_CM * alto_total / W
    cabeza = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{ANCHO_FIGURA_CM:.2f}cm" '
        f'height="{alto_cm:.2f}cm" viewBox="0 0 {W} {f(alto_total)}" font-family="{TIPOGRAFIA}">',
        f'<rect width="{W}" height="{f(alto_total)}" fill="white"/>',
    ]
    return "\n".join(cabeza + partes + ["</svg>"]) + "\n", alto_total


def comprobar_transcripcion(res):
    """Lo dibujado, reconstruido por unidad y por tramo, es el texto del
    artefacto; gris es la herencia y negro el texto; ningún texto dibujado
    lleva nombres de archivo, rutas o identificadores internos."""
    for u in UNIDADES:
        ch = res["chunks"][u["id"]]
        piezas = {}
        for r in REGISTRO:
            if r["fuente"] and r["fuente"][0] == u["clave"]:
                piezas.setdefault(r["fuente"][1:], []).append(r)
        esperado = {("herencia", k): h["texto"] for k, h in enumerate(ch["herencia"])}
        esperado[("texto", None)] = ch["texto"]
        if set(piezas) != set(esperado):
            raise SystemExit(f"{u['id']}: lo dibujado no cubre exactamente la herencia y el texto")
        for clave, s in esperado.items():
            dibujado = "\n".join(r["s"] for r in piezas[clave])
            if dibujado != s:
                raise SystemExit(f"{u['id']} {clave}: lo dibujado no es el texto del artefacto")
            color = TINTA if clave[0] == "texto" else TINTA_SUAVE
            if any(r["dentro"] is None or ("gris" in r["dentro"]) != (clave[0] == "herencia")
                   for r in piezas[clave]):
                raise SystemExit(f"{u['id']} {clave}: tramo en un bloque que no le corresponde")
            if any(r["relleno"] != color for r in piezas[clave]):
                raise SystemExit(f"{u['id']} {clave}: tramo en un color que no le corresponde")
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
    medir = base.medidor()
    fuente = "métricas reales de Helvetica" if medir else "tabla de métricas del script"
    if not medir:
        medir = base.ancho
    fallas, cajas = [], []
    tamanos = {}
    for r in REGISTRO:
        a = medir(r["s"], r["fs"], r["negrita"])
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
    return fuente, len(REGISTRO), len(MARCAS), len(CAJAS), tamanos, fallas, cajas_texto, holgura


# --------------------------------------------------------------------------- #
# Margen a los bordes (el de generar_figura_formacion_to.py)                   #
# --------------------------------------------------------------------------- #
RX_COORD = re.compile(r"-?\d+(?:\.\d+)?")


def cajas_dibujo(svg):
    """Caja de cada elemento dibujado del SVG (rectángulos, trazos, círculos),
    con medio grosor de trazo y, en los trazos con punta de flecha, el largo de
    la punta (6 veces el grosor). No cuentan el fondo (el rectángulo sin x) ni
    las definiciones. En los trazos con curvas, la caja incluye los puntos de
    control (cota superior de la curva)."""
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
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--svg", help="guarda además el SVG intermedio en esta ruta")
    args = ap.parse_args()

    res = resolver()
    print(f"PDF: {REL_PDF}   sha256 {PDF_SHA256[:12]}… (comprobado; igual al del inventario "
          f"{REL_INVENTARIO})")
    print(f"     portada: {res['portada'][0]!r}; {PORTADA[0]} · {PORTADA[1]} (comprobado)")
    print(f"UNIDADES: {REL_CHUNKS}   sha256 {CHUNKS_SHA256[:12]}… (comprobado), "
          f"{len(res['chunks'])} unidades")
    print(f"E1 de r1: {REL_E1_R1}   sha256 {E1_R1_SHA256[:12]}… (comprobado): "
          f"{res['n_e1']} registros sobre {res['n_ids_e1']} unidades = las del artefacto")
    print(f"TRAMOS (artefacto -> página {PAGINA} del PDF; líneas del PDF contadas desde 1 en "
          "extract_text_lines):")
    for t in res["tramos"]:
        estado = "exacto" if t["exacto"] else "DIFERENCIA (solo normalizado)"
        print(f"  {t['unidad']:8s} {t['nombre']:30s} artefacto línea {t['linea_artefacto']}; "
              f"PDF {estado}, líneas {t['lineas_pdf']}")
    diferencias = [t for t in res["tramos"] if not t["exacto"]]
    print(f"     diferencias artefacto / PDF: {len(diferencias)} (se dibuja lo que dice el artefacto)")

    svg, alto_total = componer(res)
    comprobar_transcripcion(res)
    print(f"TRANSCRIPCIÓN: lo dibujado reconstruye el texto del artefacto en las "
          f"{len(UNIDADES)} unidades; gris = herencia, negro = texto; sin textos prohibidos")
    (fuente, n_txt, n_marcas, n_cajas, tamanos, fallas, cajas_texto,
     holgura) = controlar_geometria(alto_total)
    minimos, fallas_margen, n_elem = controlar_margen(svg, cajas_texto, alto_total)
    print(f"GEOMETRÍA ({fuente}): {n_txt} textos, {n_cajas} cajas, {n_marcas} marcas; "
          f"fallas: {len(fallas)}; holgura mínima de una línea a la derecha de su bloque "
          f"{holgura:.1f} unidades")
    for x in fallas:
        print(f"  MAL {x}")
    mm = ANCHO_FIGURA_CM * 10 / W
    print(f"MARGEN ({n_elem} elementos: textos, rectángulos, trazos, círculos): mínimo a cada "
          "borde " + ", ".join(f"{b} {v:.1f} u = {v * mm:.2f} mm" for b, v in minimos.items())
          + f"; exigido {MARGEN_MM:.1f} mm ({MARGEN_MIN:.1f} u); fallas: {len(fallas_margen)}")
    for x in fallas_margen:
        print(f"  MAL {x}")
    if fallas or fallas_margen:
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
