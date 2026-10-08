#!/usr/bin/env python3
"""Figura «una ficha de la medición de cobertura» (capítulo 3, sección 3.8), versión 2.2.

Una ficha real del instrumento con el que se midió la cobertura del esquema de
partida, con las respuestas de la lectura marcadas sobre el texto:
- a la izquierda, la unidad de extracción como en la figura de las unidades
  (sección 3.2): en gris, su cadena estructural; recuadrado en negro, el texto
  que se extrae, con sus párrafos; debajo, su lugar en el documento;
- a la derecha, la extracción cruda de la unidad, sin la salida del
  validador: cada entidad con su identificador local, su tipo y su etiqueta,
  y cada relación con su origen, su nombre y su destino, en el orden en que
  las produjo el extractor;
- en el texto, dos resaltados: en naranja, el párrafo que la lectura registró
  como deformado, con una flecha naranja hasta la entidad que lo representa
  mal; en gris azulado, el tramo que registró como omitido, sin flecha;
- en la lista de relaciones, la fila de la relación que la lectura registró
  como parte de la deformación (la que llega a la entidad deformada), en el
  naranja de la deformación (versión 2.1);
- abajo, una leyenda de dos líneas con el significado de cada color (en la
  versión 2.2, la deformación definida como contenido representado con un
  tipo o una relación que no le corresponde).

Nada del contenido se tipea ni se supone (FUENTES, con candado de sha256):
- la ficha, su texto y su extracción salen del worksheet de la lectura; el
  script comprueba que el texto y la cadena estructural son los del artefacto
  de unidades del que se armó la ficha, que la extracción es la del registro
  de la corrida para esa unidad, que la ficha es de la muestra al azar y no de
  las del sorteo paralelo (desvíos de la lectura, §1), y que ningún campo de
  las respuestas que usa la figura cae en la banda de truncamiento de la fe de
  erratas de esos desvíos (1020 a 1023 bytes);
- cada línea del texto está en las páginas del PDF del documento que declara
  el artefacto, y la división en párrafos se comprueba contra la geometría de
  esas páginas;
- los textos del documento y de la extracción se dibujan sin cambios; donde se
  recortan, el recorte se marca con «[…]» y el script comprueba que cada tramo
  conservado está en la fuente, en orden (RECORTES);
- el texto propio de la figura (títulos, subtítulos, la leyenda y el lugar) es
  fijo, y el lugar se deriva de la portada del documento y del número del
  punto;
- el párrafo resaltado en naranja es, salvo comillas y blancos, la cita
  textual registrada en la segunda pregunta; la entidad a la que apunta la
  flecha (ENTIDAD_DEFORMADA) tiene el tipo y la etiqueta que nombra esa
  respuesta;
- el tramo resaltado como omisión es, carácter por carácter, la cita textual
  registrada en la tercera pregunta, y ningún texto de la extracción lo
  contiene;
- la fila en naranja es la de la única relación que llega a la entidad
  deformada, y la respuesta registrada de la segunda pregunta la nombra
  («un <predicado> desde <origen> hacia ella»).

Controles, en cada corrida (el script frena si fallan), con las métricas
reales de Helvetica:
- contenido: lo dibujado reconstruye cada texto de su fuente, recortes
  incluidos; lo dibujado sobre cada resaltado reconstruye exactamente su
  tramo, y nada más va sobre un resaltado; los textos en naranja son
  exactamente los de la fila de la relación deformada; ningún texto lleva
  números de ficha, identificadores de unidad o del documento, nombres de
  archivo, rutas ni commits;
- textos: ninguno por debajo de 7 pt impresos a 15 cm, fuera del lienzo, fuera
  de la caja o del resaltado que lo contiene, cortado por el borde de otra
  caja o de otro resaltado, superpuesto a otro texto ni tocado por la flecha o
  por su punta;
- cajas: no se cruzan entre sí; los resaltados quedan dentro del texto que se
  extrae;
- flecha: no entra en el interior de ninguna caja;
- margen: ningún texto ni elemento dibujado a menos de 2 mm de un borde;
- registro: cada elemento del SVG está registrado en los controles anteriores
  (el SVG se relee y sus elementos se cotejan uno a uno con el registro).

Reutiliza por importación, como las figuras hermanas: de
generar_figura_norma_a_grafo.py, la tipografía, el escape y el formato del
SVG, la marca de omisión, la exportación a 300 dpi con la densidad grabada y
el medidor con métricas reales de Helvetica; de
generar_figura_proceso_extraccion.py, el ancho de 15 cm y la paleta (los
pares de colores de su leyenda).

Salidas, byte-reproducibles: figura_ficha.svg, .png (300 dpi, densidad
grabada) y .pdf (fecha de creación fijada por SOURCE_DATE_EPOCH).

Uso (desde la raíz del repo):
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_ficha.py
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_ficha.py --salida <directorio>
"""

import argparse
import hashlib
import json
import math
import os
import re
import shutil
import statistics
import subprocess
import sys
import xml.etree.ElementTree as ET
from collections import Counter

sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import generar_figura_norma_a_grafo as base          # noqa: E402
import generar_figura_proceso_extraccion as proc     # noqa: E402

import pdfplumber                                     # noqa: E402

RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", ".."))
NOMBRE = "figura_ficha"

# --------------------------------------------------------------------------- #
# Fuentes y candados                                                           #
# --------------------------------------------------------------------------- #
ESQ = "data/experiment/esq"
FUENTES = {
    "worksheet": (f"{ESQ}/cobertura/fichas/worksheet_fichas_esq2.json",
                  "de933cb0b180b50787afadaa0415b709922cc1e2013649b621066a0f056bb7b6"),
    "seleccion": (f"{ESQ}/cobertura/orden/seleccion_muestra_esq2.json",
                  "6c405e7c61e67b91857a5e2e5b30ce5a65ad13f3f1353e693b8fd7c8a0e0aec3"),
    "desvios": (f"{ESQ}/cobertura/desvios_lectura_esq2.md",
                "bb6db3e85d582466e83c1f57a237643af2f8f3c7b471133a2217024fe1815cb7"),
    "extraccion": (f"{ESQ}/cobertura/ayccef/extracciones_e1_ayccef.jsonl",
                   "4c132a052d58e460878166975e0d4a212cb26bf289c7fe57230186825a420580"),
    "unidades": ("data/experiment/escalado_prep/e0_dry/ayccef/chunks_ayccef.json",
                 "a1e9a674ff95ecba7d4ee30c09b69a931b4164f37abb6ac56265269531de6796"),
    "sellos": (f"{ESQ}/cobertura/sellos_produccion_sha256.json",
               "0e61230222958855c60572ac00e0c642ccc07000c4b38b4b0b4113dd4ef77869"),
    "excluidos": (f"{ESQ}/documentos_excluidos_esq.json",
                  "6b4404367a08eddb8a7714bb69e8ab6ea0a16210da742bb9a8d049936fd44e1b"),
    "pdf": ("data/experiment/escalado_prep/pdfs/ayccef.pdf",
            "aa5e3e43a920c904d47e81526ea4a61ea6b683418a2d4890b3254a029e6de9c5"),
}

# La ficha (número en el orden de lectura del worksheet). Regla de elección del
# mandato, en este orden: muestra al azar; fuera de las azarosas del sorteo
# paralelo; con alguna deformación; la de texto más corto.
FICHA = 53
EXCLUIDAS = (23, 39, 48, 65)
# Entidad que representa mal el tramo citado en la respuesta de la segunda
# pregunta (destino de la flecha).
ENTIDAD_DEFORMADA = "e5"
# Comienzo de cada párrafo del texto de la unidad, después de la línea del
# título; el script lo coteja con la geometría de las páginas del PDF.
INICIOS_PARRAFO = ("Las entidades financieras deberán requerir",
                   "El requerimiento informativo precedente",
                   "Se considerará que dos o más personas")
# Nombre del documento en el lugar: el de la portada, en minúsculas salvo la
# inicial.
NOMBRE_DOCUMENTO = "Autorización y composición del capital de entidades financieras"
# Banda de truncamiento de los campos de la lectura (fe de erratas de los
# desvíos, §5): un campo usado no puede medir entre estos bytes.
BANDA_TRUNCADO = (1020, 1023)
# Campos de las respuestas que usa la figura: la calificación de la unidad
# (para el epígrafe), la firma, la cita y lo que produjo la deformación (el
# párrafo resaltado y la entidad de la flecha), y la familia y la cita de la
# omisión (el tramo resaltado).
CAMPOS_USADOS = (("q1_representado", "marca"), ("q2_deformacion", "firma"),
                 ("q2_deformacion", "cita_textual"), ("q2_deformacion", "que_produjo"),
                 ("q3_omision", "familia"), ("q3_omision", "cita_textual"))

OMISION = base.OMISION      # «[…]»
# Recortes: para cada texto recortado, los tramos que se conservan (cada uno
# está en la fuente, en este orden) y si se corta el comienzo y el final. Los
# tramos se unen con « […] ».
RECORTES = {
    # La etiqueta de la entidad del Texto Ordenado termina con el
    # identificador interno del documento.
    ("entidad", "to"): (("Información especial —",), False, True),
}

# Texto propio de la figura.
TITULO_UNIDAD = "Unidad de extracción del punto {unidad}"
TITULO_EXTRACCION = "Extracción cruda"
SUB_ENTIDADES = "Entidades: identificador, tipo y etiqueta"
SUB_RELACIONES = "Relaciones: origen, nombre y destino"
PROPUESTO = "(sujeto propuesto)"
# Leyenda: (clave del resaltado, par de colores, texto).
LEYENDA = (("deformacion", proc.MODELO,
            "Deformación: contenido representado con un tipo o una relación que no le corresponde"),
           ("omision", proc.DETERMINISTICA, "Omisión: contenido que quedó sin extraer"))
# Nada de esto puede aparecer en un texto dibujado.
PROHIBIDOS = (re.compile(r"\bfichas?\b", re.I), re.compile(r"\bayccef\b", re.I), re.compile(r"::"),
              re.compile(r"\.(jsonl?|pdf|py|md|tex)\b"), re.compile(r"\bE[0-9]\b"),
              re.compile(r"pre-?registro", re.I), re.compile(r"\b[0-9a-f]{7,40}\b"),
              re.compile(r"chunk|worksheet|semilla", re.I), re.compile(r"\bS7\b"))

# --------------------------------------------------------------------------- #
# Tamaño impreso: 15 cm de ancho                                               #
# --------------------------------------------------------------------------- #
W = proc.W                                            # 720 unidades de lienzo
ANCHO_FIGURA_CM = proc.ANCHO_TEXTO_CM                 # 15,00
ANCHO_FIGURA_PT = ANCHO_FIGURA_CM * proc.PT_POR_CM    # 425,2
DPI = base.DPI                                        # 300
ANCHO_PNG_PX = round(ANCHO_FIGURA_CM / 2.54 * DPI)    # 1772
PT_MINIMO = 7.0
MARGEN_MM = 2.0
MARGEN_MIN = MARGEN_MM * W / (ANCHO_FIGURA_CM * 10)   # 9,6 unidades
MARGEN = 11                                           # 2,29 mm
ALTO_OBJETIVO_CM = 14.0                               # se informa; no se recorta para cumplirlo


def puntos_impresos(unidades):
    """Tamaño en puntos de `unidades` del lienzo con la figura a 15 cm."""
    return unidades * ANCHO_FIGURA_PT / W


# --------------------------------------------------------------------------- #
# Paleta y tipografía (las de las figuras hermanas)                            #
# --------------------------------------------------------------------------- #
TIPOGRAFIA = base.TIPOGRAFIA
TRAZO = "#4a5a6a"                   # borde del texto que se extrae
BORDE = "#999999"                   # borde de los bloques grises y de las entidades
FONDO_BLOQUE = "#f4f6f8"            # bloque gris de la cadena estructural
TINTA = proc.TINTA                  # texto de la unidad y de la extracción
TINTA_SUAVE = "#555555"             # herencia, identificadores, rótulos y lugar
ACENTO = proc.MODELO["borde"]       # naranja: la flecha, la entidad y la fila de la relación deformadas
COLOR = {clave: par for clave, par, _ in LEYENDA}
BORDE_LEYENDA = "#e2e2e2"           # recuadro de la leyenda (el de la figura de estrategias)
esc, f = base.esc, base.f

FS_TITULO = 14          # títulos de las columnas y tipo de entidad, en negrita (8,27 pt)
FS = 13                 # todo lo demás (7,68 pt)
IL = 16                 # interlínea de FS
PAD_X, PAD_Y = 7, 5     # aire interior de los bloques y de las entidades
SEP_TITULO = 6          # entre un título y lo que sigue
SEP_SUB = 4             # entre un subtítulo y lo que sigue
SEP_GRIS = 9            # entre la cadena estructural y el texto
SEP_PARRAFO = 5         # entre párrafos del texto
SEP_LUGAR = 6
SEP_ENTIDAD = 5
SEP_BLOQUE = 12         # entre las entidades y las relaciones
SEP_LEYENDA = 20        # entre la columna más larga y la leyenda
GROSOR_TEXTO = 1.3      # borde del texto que se extrae
GROSOR_ENTIDAD = 1.0
GROSOR_ACENTO = 1.6     # flecha y borde de la entidad deformada
GROSOR_MUESTRA = 1.6    # borde de las muestras de color de la leyenda
RADIO = 9               # esquinas de la flecha
HOLGURA_TEXTO = 1.5     # de un texto a la flecha o al borde de su caja
AIRE_RESALTE = 2.5      # del texto al borde superior e inferior de un resaltado
AIRE_OMISION = 1.0      # a los lados del tramo omitido (a la derecha, solo si lo sigue un blanco)
AIRE_OMISION_V = 1.0    # arriba y abajo del tramo omitido: menos que el aire entre líneas
# Leyenda: muestra de 24 x 16, filas de 22 (las de la figura de estrategias).
MUESTRA_W, MUESTRA_H, FILA_LEYENDA = 24, 16, 22

# Columnas de la fila de arriba.
X_IZQ = MARGEN
W_IZQ = 340
CALLE = 36              # entre las dos columnas: por acá pasa la flecha
X_DER = X_IZQ + W_IZQ + CALLE
W_DER = W - MARGEN - X_DER
DX_RELACION = 26        # de la columna del origen a la del nombre
DX_DESTINO = 14         # del nombre más ancho a la columna del destino


# --------------------------------------------------------------------------- #
# Fuentes                                                                      #
# --------------------------------------------------------------------------- #
def sha256(ruta):
    with open(ruta, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def freno(motivo):
    raise SystemExit(f"FRENO: {motivo}")


def leer_bytes(clave):
    rel, esperado = FUENTES[clave]
    with open(os.path.join(RAIZ, rel), "rb") as fh:
        crudo = fh.read()
    sha = hashlib.sha256(crudo).hexdigest()
    if sha != esperado:
        freno(f"{rel} no es el verificado: sha256 {sha[:12]}… ≠ {esperado[:12]}…")
    return crudo


def leer(clave):
    return leer_bytes(clave).decode("utf-8")


def normalizar(s):
    """Comillas tipográficas a rectas y blancos colapsados."""
    s = s.replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s).strip()


def cadenas(x):
    """Todas las cadenas de un JSON anidado."""
    if isinstance(x, str):
        yield x
    elif isinstance(x, dict):
        for v in x.values():
            yield from cadenas(v)
    elif isinstance(x, list):
        for v in x:
            yield from cadenas(v)


def recortar(fuente, tramos, corta_inicio, corta_final, nombre):
    """Texto con los tramos conservados unidos por « […] ». Cada tramo está en
    la fuente, en orden y sin solaparse, y entre dos tramos hay texto cortado."""
    pos, posiciones = 0, []
    for t in tramos:
        i = fuente.find(t, pos)
        if i < 0:
            freno(f"recorte de {nombre}: el tramo {t[:40]!r}… no está en la fuente, en orden")
        if posiciones and not re.search(r"\w", fuente[pos:i]):
            freno(f"recorte de {nombre}: dos tramos seguidos sin texto cortado entre ellos")
        posiciones.append((i, i + len(t)))
        pos = i + len(t)
    if (posiciones[0][0] == 0) == corta_inicio:
        freno(f"recorte de {nombre}: el comienzo no es el declarado")
    if (posiciones[-1][1] == len(fuente)) == corta_final:
        freno(f"recorte de {nombre}: el final no es el declarado")
    piezas = ([OMISION] if corta_inicio else []) + [x for t in tramos for x in (t, OMISION)][:-1]
    piezas += [OMISION] if corta_final else []
    return " ".join(piezas)


def lineas_pdf(pdf, paginas):
    """Líneas de texto de las páginas (desde 1), con su página y su geometría."""
    out = []
    for p in paginas:
        for k, l in enumerate(pdf.pages[p - 1].extract_text_lines(), start=1):
            out.append({"pagina": p, "linea": k, "texto": l["text"], "top": l["top"],
                        "x0": l["x0"], "x1": l["x1"]})
    return out


def comprobar_parrafos(lineas, en_pdf):
    """La división en párrafos sale de la geometría de las páginas: una línea
    abre párrafo si la anterior del texto es corta (termina antes del 60 % del
    ancho de las líneas de la unidad) y, en la misma página, el salto es mayor
    que 1,5 veces la interlínea. Devuelve los índices de comienzo de párrafo."""
    pos = []
    for s in lineas:
        cands = [l for l in en_pdf if l["texto"] == s]
        if len(cands) != 1:
            freno(f"la línea {s[:40]!r}… aparece {len(cands)} veces en las páginas, no una")
        pos.append(cands[0])
    x0 = min(p["x0"] for p in pos)
    ancho = max(p["x1"] for p in pos) - x0
    saltos = [b["top"] - a["top"] for a, b in zip(pos, pos[1:]) if a["pagina"] == b["pagina"]]
    interlinea = statistics.median(saltos)
    comienzos = []
    for i in range(1, len(pos)):
        corta = pos[i - 1]["x1"] - x0 < 0.6 * ancho
        misma = pos[i - 1]["pagina"] == pos[i]["pagina"]
        salto = pos[i]["top"] - pos[i - 1]["top"]
        if corta and (not misma or salto > 1.5 * interlinea):
            comienzos.append(i)
        elif misma and salto > 1.5 * interlinea:
            freno(f"línea {i}: salto de párrafo detrás de una línea larga")
    return comienzos, interlinea, pos


def resolver():
    """Lee cada fuente con su candado y devuelve lo que la figura dibuja."""
    ws = json.loads(leer("worksheet"))
    fichas = [x for x in ws["fichas"] if x["n"] == FICHA]
    if len(fichas) != 1:
        freno(f"el worksheet tiene {len(fichas)} fichas número {FICHA}")
    ficha = fichas[0]
    cid = ficha["chunk_id"]

    # Muestra y contaminación.
    sel = json.loads(leer("seleccion"))
    if cid not in sel["azarosa"] or cid in {d["chunk_id"] for d in sel["dirigida"]}:
        freno(f"la ficha {FICHA} no es de la muestra al azar")
    desvios = leer("desvios")
    sec1 = desvios.split("## 1.")[1].split("## 2.")[0]
    filas = re.findall(r"^\| (\d+) \| (\S+) \| \**(azarosa|dirigida)\** \|", sec1, re.M)
    if len(filas) != 10:
        freno(f"la tabla del sorteo paralelo tiene {len(filas)} filas, no 10")
    por_n = {int(n): (c, m) for n, c, m in filas}
    if tuple(sorted(n for n, (_, m) in por_n.items() if m == "azarosa")) != EXCLUIDAS:
        freno("las azarosas del sorteo paralelo no son las excluidas por el mandato")
    for n, (c, _) in por_n.items():
        if [x["chunk_id"] for x in ws["fichas"] if x["n"] == n] != [c]:
            freno(f"la fila {n} de los desvíos no es la ficha {n} del worksheet")
    if FICHA in por_n:
        freno(f"la ficha {FICHA} es del sorteo paralelo")

    # Respuestas que usa la figura: completas (fuera de la banda de truncamiento).
    pr = ficha["preguntas"]
    for q, campo in CAMPOS_USADOS:
        v = pr[q][campo]
        if not isinstance(v, str) or not v.strip():
            freno(f"{q}.{campo}: vacío")
        if BANDA_TRUNCADO[0] <= len(v.encode("utf-8")) <= BANDA_TRUNCADO[1]:
            freno(f"{q}.{campo}: {len(v.encode('utf-8'))} bytes, en la banda de truncamiento")
    q2, q3 = pr["q2_deformacion"], pr["q3_omision"]
    if q2["firma"] in ("ninguna", "duda") or q3["familia"] in ("ninguna", "duda"):
        freno(f"la ficha {FICHA} no registra una deformación y una omisión")

    # Unidad: la del artefacto, con su candado declarado en los sellos de la corrida.
    sellos = json.loads(leer("sellos"))["archivos"]
    if sellos.get(FUENTES["unidades"][0]) != FUENTES["unidades"][1]:
        freno("los sellos de la corrida no declaran este artefacto de unidades")
    unidades = [c for c in json.loads(leer("unidades")) if c["id"] == cid]
    if len(unidades) != 1:
        freno(f"el artefacto tiene {len(unidades)} unidades {cid}")
    ch = unidades[0]
    tf = ficha["texto_fuente"]
    if tf["texto_propio"] != ch["texto"]:
        freno("el texto de la ficha no es el del artefacto")
    herencia = [{"tipo": h["tipo"], "unidad_origen": h["unidad_origen"], "texto": h["texto"]}
                for h in ch["herencia"]]
    if tf["contexto_heredado"] != herencia or tf["flags_e0"] is not None:
        freno("la cadena estructural de la ficha no es la del artefacto")
    if (ficha["unidad"], ficha["to"], ficha["tipo_unidad"]) != (ch["unidad"], ch["to"], ch["tipo"]):
        freno("la ficha no identifica la unidad como el artefacto")

    # Extracción: la del registro de la corrida (el último registro de la unidad).
    regs = [json.loads(x) for x in leer("extraccion").splitlines() if x.strip()]
    regs = [r for r in regs if r.get("chunk_id") == cid]
    if not regs or regs[-1].get("error") is not None:
        freno(f"el registro de la corrida no tiene una extracción sin error de {cid}")
    crudo = regs[-1]["tool_input_crudo"]
    ext = ficha["extraccion"]
    for k in ("entities", "relations", "omisiones_no_prosa"):
        if ext[k] != crudo.get(k):
            freno(f"la extracción de la ficha ({k}) no es la del registro de la corrida")

    # PDF del documento: el que declaran el artefacto y la lista de excluidos.
    excl = [d for d in json.loads(leer("excluidos"))["documentos"] if d["id"] == ch["to"]]
    if (len(excl) != 1 or excl[0]["sha256"] != FUENTES["pdf"][1]
            or excl[0]["archivo"] != ch["archivo"] or os.path.basename(FUENTES["pdf"][0]) != ch["archivo"]):
        freno("la lista de documentos excluidos no declara este PDF para el documento")
    leer_bytes("pdf")
    with pdfplumber.open(os.path.join(RAIZ, FUENTES["pdf"][0])) as pdf:
        portada = [l["text"] for l in pdf.pages[0].extract_text_lines()]
        cuerpo = lineas_pdf(pdf, ch["paginas"])
        cadena = lineas_pdf(pdf, ch["herencia"][0]["paginas"])
    if NOMBRE_DOCUMENTO.upper() != " ".join(portada[:2]):
        freno(f"el nombre {NOMBRE_DOCUMENTO!r} no es el de la portada {portada[:2]!r}")
    if len(ch["herencia"]) != 1 or not any(l["texto"] == ch["herencia"][0]["texto"] for l in cadena):
        freno("la cadena estructural no está en su página del PDF")

    # Párrafos del texto.
    lineas = ch["texto"].split("\n")
    if lineas[0] != f"{ch['unidad']}. {ch['titulo']}":
        freno("el texto no empieza con el número y el título del punto")
    if any(s.endswith("-") or "  " in s or s != s.strip() for s in lineas):
        freno("una línea del texto termina en guion o tiene blancos de más: unirlas cambiaría el texto")
    comienzos, interlinea, geo_lineas = comprobar_parrafos(lineas, cuerpo)
    fijados = [i for i, x in enumerate(lineas) if x.startswith(INICIOS_PARRAFO)]
    if comienzos != fijados or len(fijados) != len(INICIOS_PARRAFO) or comienzos[0] != 1:
        freno(f"la división en párrafos del PDF ({comienzos}) no es la fijada ({fijados})")
    cortes = [0] + comienzos + [len(lineas)]
    parrafos = [" ".join(lineas[a:b]) for a, b in zip(cortes, cortes[1:])]

    # Deformación: el párrafo citado y la entidad que lo representa.
    citado = [i for i, p in enumerate(parrafos) if normalizar(p) == normalizar(q2["cita_textual"])]
    if len(citado) != 1:
        freno("la cita textual de la deformación no es un párrafo del texto")
    entidades = {e["local_id"]: e for e in ext["entities"]}
    if len(entidades) != len(ext["entities"]):
        freno("identificadores locales repetidos en la extracción")
    e_def = entidades.get(ENTIDAD_DEFORMADA)
    if (e_def is None or f"{e_def['type']} llamada \"{e_def['label']}\"" not in q2["que_produjo"]
            or not q2["que_produjo"].startswith(f"{ENTIDAD_DEFORMADA},")):
        freno("la respuesta registrada no nombra a la entidad de la flecha con su tipo y su etiqueta")

    # Omisión: la cita textual de la tercera pregunta, carácter por carácter,
    # una sola vez en un solo párrafo, entre límites de palabra, fuera del
    # párrafo deformado y en ningún texto de la extracción.
    cita = q3["cita_textual"]
    hallados = [(i, m.start()) for i, p in enumerate(parrafos)
                for m in re.finditer(re.escape(cita), p)]
    if len(hallados) != 1:
        freno(f"la cita de la omisión aparece {len(hallados)} veces en los párrafos, no una")
    i_om, a_om = hallados[0]
    b_om = a_om + len(cita)
    p_om = parrafos[i_om]
    if (a_om > 0 and p_om[a_om - 1] != " ") or (b_om < len(p_om) and p_om[b_om].isalnum()):
        freno("la cita de la omisión no empieza o no termina en un límite de palabra")
    if i_om == citado[0]:
        freno("la omisión cae en el párrafo deformado: los resaltados se pisarían")
    en_extraccion = [s for s in cadenas(ext) if normalizar(cita) in normalizar(s)
                     or "Superintendente" in s]
    if en_extraccion:
        freno(f"la extracción contiene el tramo omitido: {en_extraccion[0][:60]!r}")
    # Líneas del artefacto (las del PDF) que ocupa el tramo: la primera ventana
    # mínima de líneas seguidas que, unidas por un blanco, lo contiene.
    crudo_om = ch["texto"].split("\n")
    linea_om = min(((k, m) for k in range(len(crudo_om)) for m in range(1, 4)
                    if cita in " ".join(crudo_om[k:k + m])), key=lambda km: (km[1], km[0]))
    linea_om = list(range(linea_om[0], linea_om[0] + linea_om[1]))

    fila_deformacion = fila_relacion_deformada(ext, q2)

    return {"fila_deformacion": fila_deformacion,
            "ficha": ficha, "ch": ch, "ext": ext, "parrafos": parrafos,
            "citado": citado[0], "omision": (i_om, a_om, b_om), "cita_omision": cita,
            "lineas_omision": linea_om, "portada": portada[:2], "comienzos": comienzos,
            "interlinea": interlinea, "geo_lineas": geo_lineas, "n_regs": len(regs)}


def fila_relacion_deformada(ext, q2):
    """Índice, en la lista de relaciones de la extracción, de la única relación
    que llega a la entidad deformada; la respuesta registrada de la segunda
    pregunta tiene que nombrarla («un <predicado> desde <origen> hacia ella»)."""
    llegan = [i for i, r in enumerate(ext["relations"]) if r.get("target") == ENTIDAD_DEFORMADA]
    if len(llegan) != 1:
        freno(f"{len(llegan)} relaciones llegan a la entidad deformada, no una")
    r = ext["relations"][llegan[0]]
    if f"un {r['predicate']} desde {r['source']} hacia ella" not in q2["que_produjo"]:
        freno("la respuesta registrada no nombra la relación que llega a la entidad deformada")
    return llegan[0]


# --------------------------------------------------------------------------- #
# Texto de la figura: cada pieza con su fuente                                 #
# --------------------------------------------------------------------------- #
def textos_fijados(res):
    """Texto esperado de cada pieza dibujada, derivado de las fuentes."""
    ch, ext = res["ch"], res["ext"]
    t = {("titulo", "unidad"): TITULO_UNIDAD.format(unidad=ch["unidad"]),
         ("titulo", "extraccion"): TITULO_EXTRACCION,
         ("sub", "entidades"): SUB_ENTIDADES,
         ("sub", "relaciones"): SUB_RELACIONES,
         ("herencia", 0): ch["herencia"][0]["texto"],
         ("lugar", 0): f"Lugar: {NOMBRE_DOCUMENTO}, punto {ch['unidad']}"}
    for i, p in enumerate(res["parrafos"]):
        t[("parrafo", i)] = p
    for e in ext["entities"]:
        k = e["local_id"]
        t[("id", k)] = k
        t[("tipo", k)] = e["type"]
        t[("entidad", k)] = e["label"]
    for i, r in enumerate(ext["relations"]):
        t[("origen", i)] = r["source"]
        t[("relacion", i)] = r["predicate"]
        destino = [r[k] for k in ("target", "sujeto_id", "sujeto_propuesto") if k in r]
        if len(destino) != 1:
            freno(f"relación {i}: {len(destino)} destinos")
        t[("destino", i)] = destino[0]
        if "sujeto_propuesto" in r:
            t[("propuesto", i)] = PROPUESTO
    for clave, _, s in LEYENDA:
        t[("leyenda", clave)] = s
    for clave, (tramos, ini, fin) in RECORTES.items():
        if clave not in t:
            freno(f"recorte de una pieza que no se dibuja: {clave}")
        t[clave] = recortar(t[clave], tramos, ini, fin, clave)
    return t


# --------------------------------------------------------------------------- #
# Primitivas de dibujo: todo lo que se dibuja queda registrado                 #
# --------------------------------------------------------------------------- #
REGISTRO = []     # textos
CAJAS = {}        # clave -> {bb, grosor, fondo}
TRAZOS = []       # {nombre, puntos, grosor, punta}
DIBUJADOS = []    # etiqueta de cada elemento, en el orden del SVG
MEDIR = None      # métricas reales de Helvetica (base.medidor)


def texto(partes, x, y, s, fs, negrita, relleno, pieza, dentro=None, fondo=None, junta=" "):
    """`junta` es lo que va entre este texto y el anterior de la misma pieza al
    reconstruirla: un blanco entre líneas o palabras, nada dentro de una
    palabra partida por un resaltado."""
    peso = "bold" if negrita else "normal"
    partes.append(f'<text x="{f(x)}" y="{f(y)}" font-size="{fs}" font-weight="{peso}" '
                  f'fill="{relleno}">{esc(s)}</text>')
    DIBUJADOS.append("text")
    REGISTRO.append({"s": s, "fs": fs, "negrita": negrita, "x": float(f(x)), "y": float(f(y)),
                     "relleno": relleno, "pieza": pieza, "dentro": dentro, "fondo": fondo,
                     "junta": junta})


def caja(partes, clave, x0, y0, x1, y1, borde, grosor, relleno, rx=2, fondo=False):
    trazo_svg = f'stroke="{borde}" stroke-width="{grosor}"' if borde else 'stroke="none"'
    partes.append(f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(x1 - x0)}" height="{f(y1 - y0)}" '
                  f'rx="{rx}" fill="{relleno}" {trazo_svg}/>')
    DIBUJADOS.append("rect")
    x0, y0, x1, y1 = (float(f(v)) for v in (x0, y0, x1, y1))
    CAJAS[clave] = {"bb": (x0, y0, x1, y1), "grosor": grosor if borde else 0.0, "fondo": fondo}


def trazo(partes, nombre, puntos, color, grosor, marcador):
    """Poligonal con esquinas redondeadas y punta de flecha (la técnica de
    generar_figura_experimento_estrategias.py). Registra la geometría real: los
    tramos rectos y cada esquina muestreada en diez puntos de su curva."""
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
            u = k / 10.0
            muestra.append(((1 - u) ** 2 * ex + 2 * (1 - u) * u * x1 + u * u * sx,
                            (1 - u) ** 2 * ey + 2 * (1 - u) * u * y1 + u * u * sy))
    d += f" L{f(puntos[-1][0])},{f(puntos[-1][1])}"
    muestra.append(puntos[-1])
    partes.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{grosor}" '
                  f'marker-end="url(#{marcador})"/>')
    DIBUJADOS.append("path")
    # Marcador de 10 × 10 con refX 9, dibujado a 6 veces el grosor: la punta
    # queda una décima de su largo más allá del final del trazo.
    (xa, ya), (xb, yb) = puntos[-2], puntos[-1]
    largo = math.hypot(xb - xa, yb - ya)
    ux, uy = (xb - xa) / largo, (yb - ya) / largo
    lp = 6 * grosor
    tip = (xb + 0.1 * lp * ux, yb + 0.1 * lp * uy)
    bx, by = xb - 0.9 * lp * ux, yb - 0.9 * lp * uy
    punta = (tip, (bx - 0.5 * lp * uy, by + 0.5 * lp * ux), (bx + 0.5 * lp * uy, by - 0.5 * lp * ux))
    TRAZOS.append({"nombre": nombre, "puntos": muestra, "grosor": grosor, "punta": punta})


def envolver(s, ancho, fs=FS, negrita=False):
    """Líneas de `s` por palabras."""
    lineas, actual = [], ""
    for palabra in s.split(" "):
        cand = palabra if not actual else actual + " " + palabra
        if actual and MEDIR(cand, fs, negrita) > ancho:
            lineas.append(actual)
            actual = palabra
        else:
            actual = cand
    lineas.append(actual)
    return lineas


def base_linea(y_arriba, fs=FS):
    return y_arriba + fs * 0.78


# --------------------------------------------------------------------------- #
# Composición                                                                  #
# --------------------------------------------------------------------------- #
def linea_con_omision(partes, x, yy, s, off, a, b, pieza, n_om):
    """Una línea del párrafo con el tramo [a, b) del párrafo resaltado como
    omisión; `off` es la posición de la línea en el párrafo. Parte la línea en
    lo anterior al tramo, el tramo y lo posterior, cada uno en su texto, y pone
    el resaltado detrás del tramo. Devuelve cuántos resaltados dibujó."""
    sa, sb = max(a - off, 0), min(b - off, len(s))
    if sa >= sb:
        texto(partes, x, base_linea(yy), s, FS, False, TINTA, pieza, dentro="texto")
        return 0
    clave = f"omision {n_om + 1}"
    # Las posiciones del SVG van a una décima (base.f): el final del tramo se
    # redondea hacia arriba en esa grilla, para que lo que sigue no lo pise.
    x_seg = float(f(x + MEDIR(s[:sa], FS, False)))
    x_fin = math.ceil(max(x + MEDIR(s[:sb], FS, False), x_seg + MEDIR(s[sa:sb], FS, False)) * 10) / 10.0
    resto = s[sb:]
    blanco_detras = resto.startswith(" ")
    x0 = x_seg - AIRE_OMISION
    x1 = x_fin + (AIRE_OMISION if (blanco_detras or not resto) else 0.0)
    caja(partes, clave, x0, yy - AIRE_OMISION_V, x1, yy + FS + AIRE_OMISION_V, None, 0,
         COLOR["omision"]["relleno"], fondo=True)
    junta = " "
    if sa > 0:
        texto(partes, x, base_linea(yy), s[:sa].rstrip(" "), FS, False, TINTA, pieza, dentro="texto")
        junta = " " if s[sa - 1] == " " else ""
    texto(partes, x_seg, base_linea(yy), s[sa:sb], FS, False, TINTA, pieza, dentro="texto",
          fondo=clave, junta=junta)
    if resto:
        lead = len(resto) - len(resto.lstrip(" "))
        x_r = x1 if not lead else x + MEDIR(s[:sb + lead], FS, False)
        texto(partes, max(x_r, x1), base_linea(yy), resto.lstrip(" "), FS, False, TINTA, pieza,
              dentro="texto", junta=" " if lead else "")
    return 1


def columna_izquierda(partes, T, res, y):
    """Título, cadena estructural, texto con los dos resaltados y lugar.
    Devuelve el borde inferior y la altura media del párrafo deformado."""
    texto(partes, X_IZQ, base_linea(y, FS_TITULO), T[("titulo", "unidad")], FS_TITULO, True, TINTA,
          ("titulo", "unidad"))
    y += FS_TITULO + SEP_TITULO
    ancho = W_IZQ - 2 * PAD_X
    # Cadena estructural, en gris.
    lin = envolver(T[("herencia", 0)], ancho)
    alto = 2 * PAD_Y + FS + (len(lin) - 1) * IL
    caja(partes, "cadena", X_IZQ, y, X_IZQ + W_IZQ, y + alto, BORDE, 1.0, FONDO_BLOQUE)
    for k, s in enumerate(lin):
        texto(partes, X_IZQ + PAD_X, base_linea(y + PAD_Y) + k * IL, s, FS, False, TINTA_SUAVE,
              ("herencia", 0), dentro="cadena")
    y += alto + SEP_GRIS
    # Texto que se extrae: párrafos; el deformado sobre fondo naranja claro y
    # el tramo omitido sobre fondo gris azulado.
    bloques = [envolver(T[("parrafo", i)], ancho) for i in range(len(res["parrafos"]))]
    alto = 2 * PAD_Y + FS + (sum(len(b) for b in bloques) - 1) * IL + (len(bloques) - 1) * SEP_PARRAFO
    caja(partes, "texto", X_IZQ, y, X_IZQ + W_IZQ, y + alto, TRAZO, GROSOR_TEXTO, "white")
    i_om, a_om, b_om = res["omision"]
    yy = y + PAD_Y
    resalte, n_om = None, 0
    for i, b in enumerate(bloques):
        if i == res["citado"]:
            y0, y1 = yy - AIRE_RESALTE, yy + FS + (len(b) - 1) * IL + AIRE_RESALTE
            caja(partes, "deformacion", X_IZQ + PAD_X - 3, y0, X_IZQ + W_IZQ - PAD_X + 3, y1, None, 0,
                 COLOR["deformacion"]["relleno"], fondo=True)
            resalte = (y0 + y1) / 2.0
        off = 0
        for s in b:
            if i == i_om:
                n_om += linea_con_omision(partes, X_IZQ + PAD_X, yy, s, off, a_om, b_om,
                                          ("parrafo", i), n_om)
            else:
                texto(partes, X_IZQ + PAD_X, base_linea(yy), s, FS, False, TINTA, ("parrafo", i),
                      dentro="texto", fondo="deformacion" if i == res["citado"] else None)
            off += len(s) + 1
            yy += IL
        yy += SEP_PARRAFO
    y += alto + SEP_LUGAR
    for s in envolver(T[("lugar", 0)], W_IZQ):
        texto(partes, X_IZQ, base_linea(y), s, FS, False, TINTA_SUAVE, ("lugar", 0))
        y += IL
    return y - IL + FS, resalte


def columna_derecha(partes, T, res, y):
    """Entidades en cajas y relaciones en tres columnas. Devuelve el borde
    inferior y la caja de la entidad deformada."""
    ext = res["ext"]
    texto(partes, X_DER, base_linea(y, FS_TITULO), T[("titulo", "extraccion")], FS_TITULO, True,
          TINTA, ("titulo", "extraccion"))
    y += FS_TITULO + SEP_TITULO
    texto(partes, X_DER, base_linea(y), T[("sub", "entidades")], FS, False, TINTA_SUAVE,
          ("sub", "entidades"))
    y += FS + SEP_SUB
    ancho = W_DER - 2 * PAD_X
    x_tipo = X_DER + PAD_X + max(MEDIR(e["local_id"], FS, False) for e in ext["entities"]) + 6
    destino = None
    for e in ext["entities"]:
        k = e["local_id"]
        lin = envolver(T[("entidad", k)], ancho)
        alto = 2 * PAD_Y + FS_TITULO + len(lin) * IL
        deformada = k == ENTIDAD_DEFORMADA
        caja(partes, f"entidad {k}", X_DER, y, X_DER + W_DER, y + alto,
             ACENTO if deformada else BORDE, GROSOR_ACENTO if deformada else GROSOR_ENTIDAD, "white")
        yb = base_linea(y + PAD_Y, FS_TITULO)
        texto(partes, X_DER + PAD_X, yb, T[("id", k)], FS, False, TINTA_SUAVE, ("id", k),
              dentro=f"entidad {k}")
        texto(partes, x_tipo, yb, T[("tipo", k)], FS_TITULO, True, TINTA, ("tipo", k),
              dentro=f"entidad {k}")
        for j, s in enumerate(lin):
            texto(partes, X_DER + PAD_X, base_linea(y + PAD_Y + FS_TITULO + 3) + j * IL, s, FS,
                  False, TINTA, ("entidad", k), dentro=f"entidad {k}")
        if deformada:
            destino = (X_DER, y, X_DER + W_DER, y + alto)
        y += alto + SEP_ENTIDAD
    y += SEP_BLOQUE - SEP_ENTIDAD
    texto(partes, X_DER, base_linea(y), T[("sub", "relaciones")], FS, False, TINTA_SUAVE,
          ("sub", "relaciones"))
    y += FS + SEP_SUB + 2
    x_rel = X_DER + DX_RELACION
    x_des = x_rel + max(MEDIR(r["predicate"], FS, False) for r in ext["relations"]) + DX_DESTINO
    ancho_des = X_DER + W_DER - x_des
    for i, r in enumerate(ext["relations"]):
        yb = base_linea(y)
        tinta = ACENTO if i == res["fila_deformacion"] else TINTA
        texto(partes, X_DER, yb, T[("origen", i)], FS, False, tinta, ("origen", i))
        texto(partes, x_rel, yb, T[("relacion", i)], FS, False, tinta, ("relacion", i))
        lin = envolver(T[("destino", i)], ancho_des)
        for j, s in enumerate(lin):
            texto(partes, x_des, yb + j * IL, s, FS, False, tinta, ("destino", i))
        n = len(lin)
        if ("propuesto", i) in T:
            ultimo = MEDIR(lin[-1], FS, False)
            if ultimo + 4 + MEDIR(PROPUESTO, FS, False) <= ancho_des:
                texto(partes, x_des + ultimo + 4, yb + (n - 1) * IL, PROPUESTO, FS, False,
                      TINTA_SUAVE, ("propuesto", i))
            else:
                texto(partes, x_des, yb + n * IL, PROPUESTO, FS, False, TINTA_SUAVE, ("propuesto", i))
                n += 1
        y += n * IL
    return y - IL + FS, destino


def leyenda(partes, T, y):
    """Recuadro con una muestra de cada color y su texto (el estilo de la
    leyenda de generar_figura_experimento_estrategias.py)."""
    ancho = 12 + MUESTRA_W + 9 + max(MEDIR(T[("leyenda", k)], FS, False) for k, _, _ in LEYENDA) + 12
    alto = 10 + len(LEYENDA) * FILA_LEYENDA + 6
    caja(partes, "leyenda", MARGEN, y, MARGEN + ancho, y + alto, BORDE_LEYENDA, 1.0, "white", rx=5)
    for k, (clave, par, _) in enumerate(LEYENDA):
        yc = y + 10 + k * FILA_LEYENDA + FILA_LEYENDA / 2.0
        caja(partes, f"muestra {clave}", MARGEN + 12, yc - MUESTRA_H / 2.0, MARGEN + 12 + MUESTRA_W,
             yc + MUESTRA_H / 2.0, par["borde"], GROSOR_MUESTRA, par["relleno"], rx=3)
        texto(partes, MARGEN + 12 + MUESTRA_W + 9, yc + 0.28 * FS, T[("leyenda", clave)], FS, False,
              TINTA, ("leyenda", clave), dentro="leyenda")
    return y + alto


def componer(res):
    del REGISTRO[:]
    CAJAS.clear()
    del TRAZOS[:]
    del DIBUJADOS[:]
    T = textos_fijados(res)
    partes = []
    y_izq, y_resalte = columna_izquierda(partes, T, res, MARGEN)
    y_der, destino = columna_derecha(partes, T, res, MARGEN)
    # Flecha: del borde derecho del texto, a la altura del párrafo deformado,
    # por la calle entre columnas, hasta el borde izquierdo de la entidad
    # deformada.
    x_ini = X_IZQ + W_IZQ + GROSOR_TEXTO / 2.0
    x_fin = destino[0] - GROSOR_ACENTO / 2.0 - 1.0
    y_fin = (destino[1] + destino[3]) / 2.0
    x_calle = X_IZQ + W_IZQ + CALLE / 2.0
    if abs(y_fin - y_resalte) < 0.05:
        puntos = [(x_ini, y_resalte), (x_fin, y_fin)]
    else:
        puntos = [(x_ini, y_resalte), (x_calle, y_resalte), (x_calle, y_fin), (x_fin, y_fin)]
    trazo(partes, "deformación", puntos, ACENTO, GROSOR_ACENTO, "arA")
    y = leyenda(partes, T, max(y_izq, y_der) + SEP_LEYENDA)
    alto_total = math.ceil(y + MARGEN)
    alto_cm = ANCHO_FIGURA_CM * alto_total / W
    cabeza = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{ANCHO_FIGURA_CM:.2f}cm" '
        f'height="{alto_cm:.2f}cm" viewBox="0 0 {W} {alto_total}" font-family="{TIPOGRAFIA}">',
        f'<rect width="{W}" height="{alto_total}" fill="white"/>',
        '<defs><marker id="arA" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
        f'markerHeight="6" orient="auto"><path d="M0,0L10,5L0,10z" fill="{ACENTO}"/></marker></defs>',
    ]
    geo = {"alto": alto_total, "y_izq": y_izq, "y_der": y_der, "y_resalte": y_resalte,
           "y_destino": y_fin}
    return "\n".join(cabeza + partes + ["</svg>"]) + "\n", T, geo


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
    return (r["x"], r["y"] - r["fs"] * 0.78, r["x"] + a, r["y"] + r["fs"] * 0.22)


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


def caja_punta(t):
    xs = [p[0] for p in t["punta"]]
    ys = [p[1] for p in t["punta"]]
    return (min(xs), min(ys), max(xs), max(ys))


def segmentos(t):
    return list(zip(t["puntos"], t["puntos"][1:]))


def reconstruir(registros):
    if not registros:
        return ""
    return registros[0]["s"] + "".join(r["junta"] + r["s"] for r in registros[1:])


def controlar_contenido(T, res):
    """Lo dibujado reconstruye cada pieza y no lleva nada prohibido; sobre el
    resaltado naranja va el párrafo deformado y nada más; sobre los resaltados
    de la omisión va, carácter por carácter, la cita registrada y nada más."""
    fallas = []
    por_pieza = {}
    for r in REGISTRO:
        por_pieza.setdefault(r["pieza"], []).append(r)
        for rx in PROHIBIDOS:
            if rx.search(r["s"]):
                fallas.append(f"{r['s']!r} lleva {rx.pattern!r}")
    for clave, esperado in T.items():
        dibujado = reconstruir(por_pieza.pop(clave, []))
        if dibujado != esperado:
            fallas.append(f"{clave}: dibujado {dibujado[:60]!r}… ≠ fuente {esperado[:60]!r}…")
    for clave in por_pieza:
        fallas.append(f"texto dibujado sin pieza fijada: {clave}")
    deformado = [r for r in REGISTRO if r["fondo"] == "deformacion"]
    if reconstruir(deformado) != T[("parrafo", res["citado"])] or any(
            r["pieza"] != ("parrafo", res["citado"]) for r in deformado):
        fallas.append("lo dibujado sobre el resaltado naranja no es exactamente el párrafo deformado")
    omitido = [r for r in REGISTRO if (r["fondo"] or "").startswith("omision")]
    if reconstruir(omitido) != res["cita_omision"]:
        fallas.append(f"lo dibujado sobre el resaltado de la omisión ({reconstruir(omitido)!r}) no es "
                      f"la cita registrada ({res['cita_omision']!r})")
    # Texto en naranja: exactamente la fila de la relación deformada, que se
    # recalcula desde la extracción y la respuesta registrada (no desde lo
    # que usó el dibujo).
    q2 = res["ficha"]["preguntas"]["q2_deformacion"]
    fila = fila_relacion_deformada(res["ext"], q2)
    naranja = {r["pieza"] for r in REGISTRO if r["relleno"] == ACENTO}
    esperado = {(c, fila) for c in ("origen", "relacion", "destino")}
    if naranja != esperado:
        fallas.append(f"textos en naranja {sorted(naranja)} ≠ la fila de la relación deformada "
                      f"{sorted(esperado)}")
    if any(r["relleno"] != ACENTO for r in REGISTRO if r["pieza"] in esperado):
        fallas.append("una parte de la fila de la relación deformada no está en naranja")
    claves_om = sorted(k for k in CAJAS if k.startswith("omision"))
    if sorted({r["fondo"] for r in omitido}) != claves_om:
        fallas.append("un resaltado de la omisión no tiene texto encima, o un texto no tiene su resaltado")
    return fallas


def controlar_textos(alto_total):
    fallas, tamanos = [], {}
    cajas_t = [(r, caja_texto(r)) for r in REGISTRO]
    minimos = {"texto-texto": math.inf, "texto-flecha": math.inf, "texto-borde de su caja": math.inf}
    for r, bb in cajas_t:
        pt = puntos_impresos(r["fs"])
        tamanos[r["fs"]] = pt
        if pt < PT_MINIMO:
            fallas.append(f"{r['s']!r}: letra {pt:.2f} pt < {PT_MINIMO}")
        if bb[0] < 0 or bb[2] > W or bb[1] < 0 or bb[3] > alto_total:
            fallas.append(f"{r['s']!r}: fuera del lienzo")
        for k in (r["dentro"], r["fondo"]):
            if k is None:
                continue
            c = CAJAS[k]["bb"]
            holg = min(bb[0] - c[0], c[2] - bb[2], bb[1] - c[1], c[3] - bb[3])
            if not CAJAS[k]["fondo"]:
                minimos["texto-borde de su caja"] = min(minimos["texto-borde de su caja"], holg)
            # Un resaltado (sin borde) puede ceñir el texto; una caja con borde
            # deja HOLGURA_TEXTO más medio grosor.
            exigida = 0.0 if CAJAS[k]["fondo"] else CAJAS[k]["grosor"] / 2.0 + HOLGURA_TEXTO
            if holg < exigida - 1e-6:
                fallas.append(f"{r['s']!r}: a {holg:.1f} del borde de su caja {k}")
        for clave, c in CAJAS.items():
            if clave not in (r["dentro"], r["fondo"]) and cruza(bb, ampliar(c["bb"], c["grosor"] / 2.0)):
                fallas.append(f"{r['s']!r}: se superpone con la caja {clave}")
        for t in TRAZOS:
            for p, q in segmentos(t):
                d = distancia_segmento_caja(p, q, bb) - t["grosor"] / 2.0
                minimos["texto-flecha"] = min(minimos["texto-flecha"], d)
                if d < HOLGURA_TEXTO:
                    fallas.append(f"{r['s']!r}: lo toca el trazo {t['nombre']}")
                    break
            if cruza(ampliar(bb, HOLGURA_TEXTO), caja_punta(t)):
                fallas.append(f"{r['s']!r}: lo toca la punta de {t['nombre']}")
    for i in range(len(cajas_t)):
        for j in range(i + 1, len(cajas_t)):
            (ra, a), (rb, b) = cajas_t[i], cajas_t[j]
            if cruza(a, b):
                fallas.append(f"{ra['s']!r} se superpone con {rb['s']!r}")
            dx = max(b[0] - a[2], 0.0, a[0] - b[2])
            dy = max(b[1] - a[3], 0.0, a[1] - b[3])
            minimos["texto-texto"] = min(minimos["texto-texto"], math.hypot(dx, dy))
    return fallas, tamanos, minimos, cajas_t


def controlar_cajas():
    """Las cajas no se cruzan entre sí, salvo los resaltados, que van dentro
    del texto que se extrae, y las muestras de color, dentro de la leyenda."""
    fallas = []
    dentro_de = {k: "texto" for k, c in CAJAS.items() if c["fondo"]}
    dentro_de.update({k: "leyenda" for k in CAJAS if k.startswith("muestra")})
    for k, padre in dentro_de.items():
        if not contiene(CAJAS[padre]["bb"], ampliar(CAJAS[k]["bb"], CAJAS[k]["grosor"] / 2.0),
                        CAJAS[padre]["grosor"]):
            fallas.append(f"la caja {k} sale de {padre}")
    claves = list(CAJAS)
    for i in range(len(claves)):
        for j in range(i + 1, len(claves)):
            ka, kb = claves[i], claves[j]
            if dentro_de.get(ka) == kb or dentro_de.get(kb) == ka:
                continue
            a, b = CAJAS[ka], CAJAS[kb]
            if cruza(ampliar(a["bb"], a["grosor"] / 2.0), ampliar(b["bb"], b["grosor"] / 2.0)):
                fallas.append(f"la caja {ka} se cruza con la caja {kb}")
    return fallas


def controlar_trazos():
    fallas = []
    for t in TRAZOS:
        for clave, c in CAJAS.items():
            interior = ampliar(c["bb"], -1.0)
            if any(corta(p, q, interior) for p, q in segmentos(t)):
                fallas.append(f"el trazo {t['nombre']} entra en la caja {clave}")
            if cruza(caja_punta(t), ampliar(c["bb"], -0.5)):
                fallas.append(f"la punta de {t['nombre']} entra en la caja {clave}")
    return fallas


def controlar_margen(cajas_t, alto_total):
    todas = [(f"texto {r['s']!r}", bb) for r, bb in cajas_t]
    todas += [(f"caja {k}", ampliar(c["bb"], c["grosor"] / 2.0)) for k, c in CAJAS.items()]
    for t in TRAZOS:
        xs = [p[0] for p in t["puntos"]]
        ys = [p[1] for p in t["puntos"]]
        g = t["grosor"] / 2.0
        todas.append((f"trazo {t['nombre']}", (min(xs) - g, min(ys) - g, max(xs) + g, max(ys) + g)))
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
    base.grabar_densidad(ruta_png, DPI)
    entorno = dict(os.environ, SOURCE_DATE_EPOCH=SOURCE_DATE_EPOCH)
    subprocess.run([rsvg, "-f", "pdf", "-o", ruta_pdf, ruta_svg], check=True, env=entorno)


def invariantes_pdf(ruta_pdf):
    from pypdf import PdfReader
    lector = PdfReader(ruta_pdf)
    pagina = lector.pages[0]
    fecha = (lector.metadata or {}).get("/CreationDate")
    contenido = hashlib.sha256(pagina.get_contents().get_data()).hexdigest()
    return contenido, fecha, (float(pagina.mediabox.width), float(pagina.mediabox.height))


RES = {}


def main():
    global MEDIR
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--salida", default=AQUI,
                    help="directorio donde escribir el SVG, el PNG y el PDF (por omisión, el del script)")
    args = ap.parse_args()

    RES.update(resolver())
    ficha, ch = RES["ficha"], RES["ch"]
    pr = ficha["preguntas"]
    print("FUENTES (sha256 comprobado):")
    for clave, (rel, sha) in FUENTES.items():
        print(f"  {clave:10s} {rel}   {sha[:12]}…")
    print(f"FICHA {FICHA}: unidad {ficha['chunk_id']} ({ch['tipo']}), muestra al azar, fuera del "
          f"sorteo paralelo (excluidas {', '.join(map(str, EXCLUIDAS))}); "
          f"q1 {pr['q1_representado']['marca']!r}, firma {pr['q2_deformacion']['firma']!r}, "
          f"familia {pr['q3_omision']['familia']!r}")
    print(f"  texto y cadena = artefacto de unidades; extracción = último de {RES['n_regs']} "
          f"registro(s) de la corrida para la unidad; ningún campo usado en la banda de "
          f"truncamiento {BANDA_TRUNCADO[0]}-{BANDA_TRUNCADO[1]} bytes")
    print(f"  portada: {' '.join(RES['portada'])!r}")
    print(f"  líneas del texto en el PDF (página:línea, contadas desde 1 en extract_text_lines): "
          + ", ".join(f"{g['pagina']}:{g['linea']}" for g in RES["geo_lineas"]))
    print(f"  párrafos según la geometría del PDF: comienzan en las líneas {RES['comienzos']} "
          f"(interlínea {RES['interlinea']:.1f} pt); el deformado es el {RES['citado'] + 1} de "
          f"{len(RES['parrafos'])}")
    i_om, a_om, b_om = RES["omision"]
    lo = RES["lineas_omision"]
    print(f"  omisión: la cita registrada {RES['cita_omision']!r} está una sola vez, en el párrafo "
          f"{i_om + 1}, caracteres {a_om}-{b_om}; en el artefacto ocupa las líneas "
          f"{', '.join(str(k + 1) for k in lo)} del texto (PDF "
          f"{', '.join(str(RES['geo_lineas'][k]['pagina']) + ':' + str(RES['geo_lineas'][k]['linea']) for k in lo)}); "
          f"ningún texto de la extracción la contiene")

    MEDIR = base.medidor()
    if MEDIR is None:
        freno("sin las métricas reales de Helvetica (PIL y la fuente del sistema) no se compone la figura")
    svg, T, geo = componer(RES)
    alto_total = geo["alto"]
    for clave, (tramos, ini, fin) in RECORTES.items():
        print(f"RECORTE {clave}: {len(tramos)} tramo(s) conservado(s); corte al inicio {ini}, "
              f"al final {fin}")
    fallas_contenido = controlar_contenido(T, RES)
    fallas_textos, tamanos, minimos, cajas_t = controlar_textos(alto_total)
    fallas_cajas = controlar_cajas()
    fallas_trazos = controlar_trazos()
    minimos_margen, fallas_margen, n_elem = controlar_margen(cajas_t, alto_total)
    fallas_registro = controlar_registro(svg)

    omitido = [r for r in REGISTRO if (r["fondo"] or "").startswith("omision")]
    fd = RES["ext"]["relations"][RES["fila_deformacion"]]
    print(f"FILA EN NARANJA: relación {RES['fila_deformacion'] + 1} de {len(RES['ext']['relations'])}, "
          f"{fd['source']} {fd['predicate']} {fd.get('target')} (la que llega a la entidad deformada y "
          f"nombra la respuesta registrada: «un {fd['predicate']} desde {fd['source']} hacia ella»); "
          f"{sum(1 for r in REGISTRO if r['relleno'] == ACENTO)} textos en {ACENTO}")
    print(f"CONTENIDO: {len(REGISTRO)} textos, {len(T)} piezas; sobre el resaltado de la omisión, "
          f"{len(omitido)} textos en {len({r['fondo'] for r in omitido})} resaltado(s) que "
          f"reconstruyen {reconstruir(omitido)!r}; fallas: {len(fallas_contenido)}")
    for x in fallas_contenido:
        print(f"  MAL {x}")
    print(f"TEXTOS (métricas reales de Helvetica) contra {len(REGISTRO)} textos, {len(CAJAS)} cajas y "
          f"{len(TRAZOS)} flecha(s); fallas: {len(fallas_textos)}")
    print("  distancias mínimas: " + "; ".join(f"{k} {v:.1f}" for k, v in minimos.items()))
    for x in fallas_textos:
        print(f"  MAL {x}")
    print(f"CAJAS: {len(CAJAS)}; fallas: {len(fallas_cajas)}")
    for x in fallas_cajas:
        print(f"  MAL {x}")
    print(f"FLECHA: del párrafo deformado (y = {geo['y_resalte']:.1f}) a la entidad "
          f"{ENTIDAD_DEFORMADA} (y = {geo['y_destino']:.1f}); fallas: {len(fallas_trazos)}")
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
    if fallas_contenido or fallas_textos or fallas_cajas or fallas_trazos or fallas_margen or fallas_registro:
        raise SystemExit("FALLA: la figura tiene defectos; no se escribe nada")
    for fs in sorted(tamanos):
        print(f"LETRA {fs} unidades -> {tamanos[fs]:.2f} pt impresos a {ANCHO_FIGURA_CM:.0f} cm")
    alto_cm = ANCHO_FIGURA_CM * alto_total / W
    print(f"ALTO: lienzo {W} x {alto_total}, impreso a {ANCHO_FIGURA_CM:.2f} x {alto_cm:.2f} cm "
          f"(objetivo {ALTO_OBJETIVO_CM:.0f} cm: {'cumple' if alto_cm <= ALTO_OBJETIVO_CM else 'NO cumple'}; "
          f"columna izquierda hasta {geo['y_izq']:.1f}, derecha hasta {geo['y_der']:.1f})")

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
