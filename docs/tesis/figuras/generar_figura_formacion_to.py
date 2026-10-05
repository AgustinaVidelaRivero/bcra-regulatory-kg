#!/usr/bin/env python3
"""Figura «cómo se forma un Texto Ordenado» para el análisis del documento (capítulo 3), versión 3.

Izquierda: una línea de tiempo con las comunicaciones «A» que dieron origen al
punto 5.1.1.1 de Clasificación de deudores y las que lo modificaron, según la
fila de ese punto en la tabla de correlaciones del PDF; aparte, debajo de una
línea de puntos y fuera del eje, la última comunicación incorporada que
declara la portada, que no está en esa fila. El eje ordena por número de
comunicación, sin escala de tiempo: una comunicación lleva fecha solo si el
PDF la da (en el historial, «dd/mm/aa: “A” nnnn»); las vigencias de los pies de
página no se usan como fecha de una comunicación, porque son la vigencia de
cada hoja (la misma comunicación aparece con vigencias distintas). La nota del
eje dice que el documento no da las fechas de las comunicaciones del punto: si
el historial diera fecha, en cualquiera de sus formas, a alguna comunicación de
la fila, el script frena (fechas_del_historial). Los rótulos
propios de la figura escriben «A» con comillas latinas; lo transcripto del PDF
(portada, fila de la tabla, línea del historial) conserva “A”.
Derecha: el Texto Ordenado como un manual, en cinco bloques rotulados con sus
páginas (portada, índice, cuerpo, tabla de correlaciones e historial); en el
cuerpo, una casilla por sección y, en la sección 5, el punto 5.1.1.1 resaltado; en la tabla de correlaciones, su
fila resaltada. Entre las dos, una flecha con el rótulo «cada comunicación
reemplaza las hojas que modifica».

Nada del contenido se tipea ni se supone:
- el PDF es el del corpus: candado de sha256 (PDF_SHA256), el mismo que declara
  el inventario del conjunto de desarrollo para cla;
- el texto de la portada, las comunicaciones de la línea de tiempo, el texto
  de la fila y la línea del historial se leen del PDF (pdfplumber); la fila se
  recorta por las columnas que marcan los bordes verticales de la tabla;
- el bloque de cada página sale de reglas declaradas (clasificar_paginas) y se
  contrasta con E0 (estructura_cla.json: páginas del cuerpo y primera página
  de cada sección) y con la estadística del corpus (páginas de la tabla de
  correlaciones de cla);
- el título del punto y el de su sección salen de estructura_cla.json, y el
  script comprueba que estén en la página del PDF que E0 declara.
El texto propio de la figura (encabezados, rótulos de bloque, notas) es fijo;
los números que contiene se comprueban contra lo leído.

Controles de geometría, en cada corrida (el script frena si fallan), con las
métricas reales de Helvetica: ningún texto por debajo de 7 pt impresos a 15 cm,
fuera del lienzo, superpuesto a otro, fuera de la caja que lo contiene,
cortado por el borde de otra caja ni tocado por una marca (ejes, flecha,
corchete, marcadores, línea de puntos); y ningún texto ni elemento dibujado a
menos de 2 mm (MARGEN_MM, a 15 cm de ancho) de uno de los cuatro bordes.

Reutiliza por importación, como la figura de la página del ejemplo: de
generar_figura_norma_a_grafo.py, la tipografía, el naranja de resaltado, el
escape y formato del SVG y la tabla de métricas; de
generar_figura_proceso_extraccion.py, el ancho de texto de 15 cm, la
exportación a PNG a 300 dpi con la densidad grabada y el medidor con métricas
reales de Helvetica.

El SVG es intermedio: se pasa a rsvg-convert por la entrada estándar y no se
escribe salvo con --svg. Salidas: figura_formacion_to.png y
figura_formacion_to.pdf, las dos byte-reproducibles (el PDF, con la fecha de
creación fijada por SOURCE_DATE_EPOCH).

Uso (desde la raíz del repo):
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_formacion_to.py
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_formacion_to.py --svg <ruta>
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
SALIDA_PNG = os.path.join(AQUI, "figura_formacion_to.png")
SALIDA_PDF = os.path.join(AQUI, "figura_formacion_to.pdf")

# --------------------------------------------------------------------------- #
# Fuentes y candados                                                           #
# --------------------------------------------------------------------------- #
REL_PDF = "data/experiment/subset/TO_clasificacion_deudores_actual.pdf"
REL_INVENTARIO = "data/experiment/reextraccion_v2/manifiestos/desarrollo_5tos.json"
REL_ESTRUCTURA = "data/experiment/reextraccion_v2/e0_chunking/salida_enm01/estructura_cla.json"
REL_ESTADISTICAS = "reports/u_insumos_cap/estadisticas_corpus.json"
PDF_SHA256 = "6e7f528d3fea7b756f15e1278eecd828f203f0651fc6f778212033de6a0883e2"
ESTRUCTURA_SHA256 = "3cd26083fee7355ef3d8027ac353a744c2f1cfa35830535fe1be2b9505eaf917"
ESTADISTICAS_SHA256 = "1630d1de9f5c065eec00a237f2ba21ff43e4ee11e9332409c56593b12ccbe6ab"
TO = "cla"
PUNTO = "5.1.1.1"
# Versión del corpus: la portada debe decir las dos cosas.
PORTADA = ("“A” 8378", "19/12/2025")

# --------------------------------------------------------------------------- #
# Tamaño impreso: 15 cm de ancho                                               #
# --------------------------------------------------------------------------- #
W = proc.W                                            # 720 unidades de lienzo
ANCHO_FIGURA_CM = proc.ANCHO_TEXTO_CM                 # 15,00
ANCHO_FIGURA_PT = ANCHO_FIGURA_CM * proc.PT_POR_CM    # 425,2
DPI = proc.DPI                                        # 300
ANCHO_PNG_PX = round(ANCHO_FIGURA_CM / 2.54 * DPI)    # 1772
PT_MINIMO = 7.0
# Margen a los cuatro bordes: ningún texto ni trazo a menos de MARGEN_MM
# impresos; la composición deja MARGEN unidades.
MARGEN_MM = 2.0
MARGEN_MIN = MARGEN_MM * W / (ANCHO_FIGURA_CM * 10)   # 9,6 unidades
MARGEN = 11                                           # 2,29 mm


def puntos_impresos(unidades):
    """Tamaño en puntos de `unidades` del lienzo con la figura a 15 cm."""
    return unidades * ANCHO_FIGURA_PT / W


TIPOGRAFIA = base.TIPOGRAFIA
ACENTO = base.ACENTO                # naranja: resaltado del ejemplo
ACENTO_FONDO = "#fbe3d3"            # el mismo tono, claro (paleta de las figuras hermanas)
TRAZO = "#4a5a6a"                   # gris oscuro de la paleta compartida
BORDE = "#999999"
FONDO_BLOQUE = "#f4f6f8"
TINTA = "#1f1f1f"
TINTA_SUAVE = "#555555"
FLECHA = proc.FLECHA
esc, f = base.esc, base.f

FS = 14                 # texto principal (8,27 pt impresos)
FS_CHICO = 13           # texto secundario (7,68 pt impresos)
IL = 17                 # interlínea de FS
IL_CHICO = 16           # interlínea de FS_CHICO

# Columnas del lienzo, dentro del margen
Y0 = MARGEN                           # borde superior del contenido
X_IZQ, W_IZQ = MARGEN, 220            # línea de tiempo
X_DER = 356                           # manual
W_DER = W - MARGEN - X_DER            # 353
PAD = 7                               # aire interior de los bloques
HOLGURA = 12                          # margen al envolver con la tabla de métricas
SEP_BLOQUE = 6                        # entre bloques del manual

# Texto fijo de la figura. Los números se comprueban contra lo leído.
TITULO_IZQ = (("Comunicaciones «A»", "del punto 5.1.1.1"),
              ("según su fila de la", "tabla de correlaciones"))
ROTULO_ORIGEN = "norma de origen"
ROTULO_MODIFICAN = "lo modificaron"
ROTULO_ULTIMA = ("última comunicación incorporada", "al Texto Ordenado (portada)")
NOTA_EJE = ("Orden por número de comunicación,", "sin escala de tiempo. El documento",
            "no da las fechas de las", "comunicaciones del punto.")
TEXTO_NOTA_EJE = ("Orden por número de comunicación, sin escala de tiempo. "
                  "El documento no da las fechas de las comunicaciones del punto.")
TITULO_DER = "El Texto Ordenado, como un manual"
ROTULO_FLECHA = ("cada comunicación", "reemplaza las hojas", "que modifica")
BLOQUES = ("portada", "indice", "secciones", "tabla", "historial")
# El bloque de las secciones se rotula «Cuerpo», el nombre que usa la tesis.
NOMBRE_BLOQUE = {"portada": "Portada", "indice": "Índice", "secciones": "Cuerpo",
                 "tabla": "Tabla de correlaciones", "historial": "Historial"}
ENCABEZADO_TABLA = ("Punto", "Norma de origen", "Observaciones")
OMISION = base.OMISION

RX_PIE = re.compile(r"Versi[oó]n:\s*\S+\s+COMUNICACI[OÓ]N")
RX_SECCION = re.compile(r"^(?:B\.C\.R\.A\.\s+)?Secci[oó]n (\d+)\.\s")
RX_ULTIMA = re.compile(r"Última comunicación incorporada:\s*“A”\s*(\d+)")
RX_FECHA_TO = re.compile(r"Texto ordenado al (\d{2}/\d{2}/\d{4})")
RX_HISTORIAL = re.compile(r"^(\d{2}/\d{2}/\d{2}):\s*“A”\s*(\d+)$")
# Para el control de la nota del eje: toda fecha del historial, en sus dos
# formas («19/12/25» en la lista de últimas modificaciones, «7.7.99» en las
# entradas, como «B.O. del 7.7.99»), y el comienzo de cada entrada.
RX_FECHA_LIBRE = re.compile(r"\b\d{1,2}[/.]\d{1,2}[/.]\d{2,4}\b")
RX_ENTRADA = re.compile(r'^(?:Comunicación\s+)?["“]([A-C])["“”]\s*(\d+)\s*:')
RX_LISTA = re.compile(r'^(\d{2}/\d{2}/\d{2}):\s*["“]([A-C])["“”]\s*(\d+)$')
TITULO_HISTORIAL = "Comunicaciones que componen el historial de la norma"
LINEA_MODIFICACIONES = "Últimas modificaciones:"


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
# Lectura del PDF                                                              #
# --------------------------------------------------------------------------- #
def clasificar_paginas(doc):
    """Bloque de cada página, por reglas declaradas y en este orden:
    portada   la página 1, si dice «Última comunicación incorporada»;
    índice    la página que dice «-Índice-»;
    sección   la que tiene pie de hoja («Versión: … COMUNICACIÓN») y una línea
              «Sección N.» entre sus cuatro primeras líneas (N es la sección);
    tabla     la que tiene los encabezados «NORMA DE ORIGEN» y «OBSERVACIONES»;
    historial la que dice «Comunicaciones que componen el historial de la
              norma» y todas las que la siguen.
    Una página que no cae en ninguna regla frena el script."""
    clases = []
    for pg in doc.pages:
        t = pg.extract_text() or ""
        primeras = t.splitlines()[:4]
        secciones = [m.group(1) for m in (RX_SECCION.match(x) for x in primeras) if m]
        if pg.page_number == 1 and "Última comunicación incorporada" in t:
            c = ("portada", None)
        elif "-Índice-" in t:
            c = ("indice", None)
        elif RX_PIE.search(t) and len(secciones) == 1:
            c = ("secciones", int(secciones[0]))
        elif "NORMA DE ORIGEN" in t and "OBSERVACIONES" in t:
            c = ("tabla", None)
        elif TITULO_HISTORIAL in t or (clases and clases[-1][0] == "historial"):
            if RX_PIE.search(t) or "NORMA DE ORIGEN" in t:
                raise SystemExit(f"PDF: la página {pg.page_number} del historial tiene pie o tabla")
            c = ("historial", None)
        else:
            raise SystemExit(f"PDF: la página {pg.page_number} no cae en ninguna regla")
        clases.append(c)
    # Los bloques son contiguos y van en el orden del manual.
    orden = [c for c, _ in clases]
    vistos = [c for i, c in enumerate(orden) if i == 0 or orden[i - 1] != c]
    if vistos != list(BLOQUES):
        raise SystemExit(f"PDF: los bloques no son contiguos o no van en orden: {vistos}")
    rangos = {}
    for i, c in enumerate(orden, start=1):
        a, _ = rangos.get(c, (i, i))
        rangos[c] = (a, i)
    secs = [n for c, n in clases if c == "secciones"]
    if [n for i, n in enumerate(secs) if i == 0 or secs[i - 1] != n] != sorted(set(secs)):
        raise SystemExit("PDF: las secciones no van en orden")
    primera, seccion_de = {}, {}
    for i, (c, n) in enumerate(clases, start=1):
        if c == "secciones":
            primera.setdefault(n, i)
            seccion_de[i] = n
    return rangos, primera, seccion_de, len(doc.pages)


def leer_portada(pg):
    lineas = [l["text"] for l in pg.extract_text_lines()]
    t = "\n".join(lineas)
    m_u, m_f = RX_ULTIMA.search(t), RX_FECHA_TO.search(t)
    if not (m_u and m_f):
        raise SystemExit("PDF: la portada no dice la última comunicación y la fecha del texto ordenado")
    if (f"“A” {m_u.group(1)}", m_f.group(1)) != PORTADA:
        raise SystemExit(f"la portada no dice la versión del corpus {PORTADA}")
    if len(lineas) != 3:
        raise SystemExit(f"PDF: la portada tiene {len(lineas)} líneas; se esperaban 3")
    # La línea de la comunicación viene entre guiones («-Última … 8378-»): se
    # dibuja sin ellos.
    return {"lineas": [lineas[0], lineas[1].strip("-"), lineas[2]],
            "ultima": int(m_u.group(1)), "fecha": m_f.group(1)}


def columnas_tabla(pg):
    """Intervalos de columna de la tabla de correlaciones, por sus bordes
    verticales, y el nombre de cada uno por la palabra de encabezado que cae
    en él."""
    palabras = pg.extract_words()
    # «Com.» también aparece en las observaciones («Según Com.»): la fila de
    # encabezados es la de «Secc.».
    fila_enc = [p for p in palabras if p["text"] == "Secc."]
    if len(fila_enc) != 1:
        raise SystemExit(f"PDF: página {pg.page_number}: fila de encabezados no reconocida")
    y_enc = fila_enc[0]["top"]
    y_medio = (fila_enc[0]["top"] + fila_enc[0]["bottom"]) / 2.0
    # Bordes verticales que atraviesan la fila de encabezados (los tramos
    # cortos de otras filas no delimitan columnas).
    xs = sorted({round(r["x0"], 1) for r in pg.rects if r["x1"] - r["x0"] < 1.5
                 and r["top"] <= y_medio <= r["bottom"]})
    enc = [p for p in palabras if abs(p["top"] - y_enc) < 1]
    obs = [p for p in palabras if p["text"] == "OBSERVACIONES"]
    intervalos = list(zip(xs, xs[1:]))
    nombres = {}
    for p in enc + obs:
        dentro = [iv for iv in intervalos if iv[0] <= p["x0"] and p["x1"] <= iv[1]]
        if len(dentro) != 1:
            raise SystemExit(f"PDF: el encabezado {p['text']!r} no cae en una sola columna")
        nombres.setdefault(p["text"], []).append(dentro[0])
    esperado = {"Secc.": 1, "Punto": 2, "Párr.": 2, "Com.": 1, "Anexo": 1, "OBSERVACIONES": 1}
    if {k: len(v) for k, v in nombres.items()} != esperado:
        raise SystemExit(f"PDF: columnas de la tabla no reconocidas: {nombres}")
    return {"punto": nombres["Punto"][0], "com": nombres["Com."][0],
            "obs": nombres["OBSERVACIONES"][0]}, palabras


def leer_fila(doc, paginas_tabla):
    """La fila del punto en la tabla de correlaciones: las palabras de las
    columnas Com. y Observaciones entre el número del punto y el número del
    punto siguiente."""
    hallada = []
    for n in paginas_tabla:
        pg = doc.pages[n - 1]
        cols, palabras = columnas_tabla(pg)
        en_punto = sorted((p for p in palabras
                           if cols["punto"][0] <= p["x0"] and p["x1"] <= cols["punto"][1]
                           and re.match(r"^\d+(\.\d+)*\.$", p["text"])), key=lambda p: p["top"])
        for i, p in enumerate(en_punto):
            if p["text"] == PUNTO + ".":
                fin = en_punto[i + 1]["top"] if i + 1 < len(en_punto) else pg.height
                hallada.append((n, cols, palabras, p["top"] - 1, fin - 1))
    if len(hallada) != 1:
        raise SystemExit(f"PDF: la fila del punto {PUNTO} aparece {len(hallada)} veces en la tabla")
    n, cols, palabras, y0, y1 = hallada[0]
    banda = [p for p in palabras if y0 <= p["top"] < y1]

    def columna(c):
        return [p for p in banda if cols[c][0] <= p["x0"] and p["x1"] <= cols[c][1]]

    def por_lineas(ps):
        filas = {}
        for p in sorted(ps, key=lambda p: (round(p["top"]), p["x0"])):
            filas.setdefault(round(p["top"]), []).append(p["text"])
        return [" ".join(v) for _, v in sorted(filas.items())]

    com = por_lineas(columna("com"))
    obs = por_lineas(columna("obs"))
    if not com or any(not re.fullmatch(r"“A” \d+", x) for x in com):
        raise SystemExit(f"PDF: la columna Com. de la fila no son comunicaciones «A»: {com}")
    origen = sorted({int(x.split()[1]) for x in com})
    texto_obs = " ".join(obs)
    m = re.fullmatch(r"Según Com\. “A” (.+)\.", texto_obs)
    if not m or "“" in m.group(1):
        raise SystemExit(f"PDF: las observaciones de la fila no son «Según Com. “A” …»: {texto_obs!r}")
    sin_parentesis = re.sub(r"\([^)]*\)", "", m.group(1))
    modifican = [int(x) for x in re.findall(r"\d+", sin_parentesis)]
    return {"pagina": n, "com": com, "obs": obs, "texto_obs": texto_obs,
            "origen": origen, "modifican": modifican}


def leer_historial(doc, paginas):
    """Fechas de comunicaciones que da el historial («dd/mm/aa: “A” nnnn») y su
    lista de últimas modificaciones."""
    fechas, lineas_mod = {}, []
    for n in paginas:
        lineas = [l["text"] for l in doc.pages[n - 1].extract_text_lines()]
        if n == paginas[0]:
            if lineas[0] != TITULO_HISTORIAL or lineas[1] != LINEA_MODIFICACIONES:
                raise SystemExit("PDF: el historial no empieza con su título y sus últimas modificaciones")
        for x in lineas:
            m = RX_HISTORIAL.match(x)
            if m:
                if int(m.group(2)) in fechas:
                    raise SystemExit(f"PDF: el historial da dos fechas para la “A” {m.group(2)}")
                fechas[int(m.group(2))] = m.group(1)
                lineas_mod.append(x)
    return fechas, lineas_mod


def fechas_del_historial(doc, paginas):
    """Fechas que el historial da a cada comunicación, en sus dos formas: la
    lista de últimas modificaciones («dd/mm/aa: “A” nnnn») y las entradas
    «“A” nnnn: título», con sus líneas de continuación (donde aparecen fechas
    como «B.O. del 7.7.99»). Además, toda línea del historial que tenga el
    número de la comunicación y una fecha. Devuelve {(letra, número): fechas}."""
    lineas = [x for n in paginas for x in (l["text"] for l in doc.pages[n - 1].extract_text_lines())]
    entradas, actual = [], None
    for x in lineas:
        m_l, m_e = RX_LISTA.match(x), RX_ENTRADA.match(x)
        if m_l:
            entradas.append([(m_l.group(2), int(m_l.group(3))), x])
            actual = None
        elif m_e:
            actual = [(m_e.group(1), int(m_e.group(2))), x]
            entradas.append(actual)
        elif actual is not None and not x.endswith(":"):
            actual[1] += " " + x
        else:
            actual = None
    out = {}
    for clave, texto_entrada in entradas:
        out.setdefault(clave, set()).update(RX_FECHA_LIBRE.findall(texto_entrada))
    for (letra, numero), fechas in out.items():
        for x in lineas:
            if re.search(rf"\b{numero}\b", x):
                fechas.update(RX_FECHA_LIBRE.findall(x))
    return {k: sorted(v) for k, v in out.items()}


def resolver():
    candado(REL_PDF, PDF_SHA256)
    candado(REL_ESTRUCTURA, ESTRUCTURA_SHA256)
    candado(REL_ESTADISTICAS, ESTADISTICAS_SHA256)
    with open(os.path.join(RAIZ, REL_INVENTARIO), encoding="utf-8") as fh:
        inv = [t for t in json.load(fh)["tos"] if t["id"] == TO]
    if len(inv) != 1 or inv[0]["sha256_pdf"] != PDF_SHA256 or inv[0]["pdf"] != REL_PDF:
        raise SystemExit("el inventario del conjunto de desarrollo no declara este PDF para cla")
    with open(os.path.join(RAIZ, REL_ESTRUCTURA), encoding="utf-8") as fh:
        estructura = json.load(fh)
    with open(os.path.join(RAIZ, REL_ESTADISTICAS), encoding="utf-8") as fh:
        est_cla = json.load(fh)["conjuntos"]["desarrollo_5"]["por_to"][TO]

    nodos = {}

    def recorrer(n, sec):
        nodos[n["numero"]] = (n, sec)
        for h in n.get("hijos", []):
            recorrer(h, sec)
    for s in estructura["secciones"]:
        recorrer(s, s)
    punto, seccion = nodos[PUNTO]
    if punto.get("hijos"):
        raise SystemExit(f"estructura: {PUNTO} tiene subpuntos")

    with pdfplumber.open(os.path.join(RAIZ, REL_PDF)) as doc:
        rangos, primera, seccion_de, n_paginas = clasificar_paginas(doc)
        portada = leer_portada(doc.pages[0])
        a, b = rangos["tabla"]
        fila = leer_fila(doc, list(range(a, b + 1)))
        a, b = rangos["historial"]
        fechas, lineas_mod = leer_historial(doc, list(range(a, b + 1)))
        fechas_hist = fechas_del_historial(doc, list(range(a, b + 1)))
        texto_pagina = norm(doc.pages[punto["pagina"] - 1].extract_text())

    # Contraste con E0 y con la estadística del corpus.
    a, b = rangos["secciones"]
    if b - a + 1 != estructura["paginas_cuerpo"]:
        raise SystemExit(f"PDF: {b - a + 1} páginas de secciones; E0 dice {estructura['paginas_cuerpo']}")
    e0_primera = {int(s["numero"]): s["pagina"] for s in estructura["secciones"]}
    if primera != e0_primera:
        raise SystemExit(f"PDF: primera página de cada sección ≠ E0: {primera} / {e0_primera}")
    a, b = rangos["tabla"]
    if b - a + 1 != est_cla["tabla_norma_origen_paginas"] or n_paginas != est_cla["paginas"]:
        raise SystemExit("PDF: páginas de la tabla o del documento ≠ estadística del corpus")
    etiqueta_punto = f"{PUNTO}. {punto['titulo']}"
    etiqueta_seccion = f"Sección {seccion['numero']}. {seccion['titulo']}"
    for e in (etiqueta_punto, etiqueta_seccion):
        if e not in texto_pagina:
            raise SystemExit(f"PDF: {e!r} no está en la página {punto['pagina']} que declara E0")
    if seccion_de.get(punto["pagina"]) != int(seccion["numero"]):
        raise SystemExit("PDF: la página del punto no es una página de su sección")

    # Línea de tiempo: origen, modificaciones y última comunicación incorporada,
    # ordenadas por número.
    if len(fila["origen"]) != 1:
        raise SystemExit(f"la fila tiene {len(fila['origen'])} normas de origen distintas")
    ultima = portada["ultima"]
    if ultima in fila["origen"] + fila["modifican"]:
        raise SystemExit("la última comunicación incorporada está en la fila del punto")
    eje = ([("origen", fila["origen"][0])] + [("modifica", c) for c in fila["modifican"]]
           + [("ultima", ultima)])
    numeros = [c for _, c in eje]
    if numeros != sorted(numeros) or len(set(numeros)) != len(numeros):
        raise SystemExit(f"las comunicaciones no van en orden creciente: {numeros}")
    con_fecha = {c: fechas[c] for c in numeros if c in fechas}
    # La nota del eje dice que el documento no da las fechas de las
    # comunicaciones del punto: ninguna de la fila puede tener fecha en el
    # historial, en ninguna de sus formas. La última incorporada sí la tiene
    # en la lista de últimas modificaciones, y se dibuja.
    fila_con_fecha = {c: fechas_hist[("A", c)] for _, c in eje[:-1] if fechas_hist.get(("A", c))}
    if fila_con_fecha:
        raise SystemExit(f"la nota del eje no vale: el historial da fecha a comunicaciones del "
                         f"punto {fila_con_fecha}")
    if list(con_fecha) != [ultima]:
        raise SystemExit(f"la última comunicación no tiene fecha en la lista del historial, o "
                         f"la tiene otra: {con_fecha}")
    if " ".join(NOTA_EJE) != TEXTO_NOTA_EJE:
        raise SystemExit("la nota del eje no es la fijada")
    if fechas[ultima] != portada["fecha"][:6] + portada["fecha"][8:]:
        raise SystemExit("la fecha del historial para la última no es la de la portada")
    linea_hist = next(x for x in lineas_mod if x.endswith(f"“A” {ultima}"))
    if lineas_mod[-1] != linea_hist:
        raise SystemExit("la última modificación del historial no es la última incorporada")
    if " ".join(TITULO_IZQ[0]) != f"Comunicaciones «A» del punto {PUNTO}":
        raise SystemExit("el título de la línea de tiempo no nombra el punto")
    if " ".join(ROTULO_ULTIMA) != "última comunicación incorporada al Texto Ordenado (portada)":
        raise SystemExit("el rótulo de la última comunicación no es el fijado")
    if " ".join(ROTULO_FLECHA) != "cada comunicación reemplaza las hojas que modifica":
        raise SystemExit("el rótulo de la flecha no es el fijado")
    return {"rangos": rangos, "primera": primera, "n_paginas": n_paginas, "portada": portada,
            "fila": fila, "fechas": fechas, "eje": eje, "con_fecha": con_fecha,
            "fechas_hist": fechas_hist,
            "linea_hist": linea_hist, "etiqueta_punto": etiqueta_punto,
            "etiqueta_seccion": etiqueta_seccion, "pagina_punto": punto["pagina"],
            "seccion": int(seccion["numero"])}


# --------------------------------------------------------------------------- #
# Composición                                                                  #
# --------------------------------------------------------------------------- #
REGISTRO = []   # textos dibujados
CAJAS = {}      # cajas que contienen texto: clave -> (x0, y0, x1, y1)
MARCAS = []     # trazos y marcas que ningún texto puede tocar: (nombre, caja)


def texto(partes, x, y, s, fs, negrita=False, relleno=TINTA, ancla="start", contexto="",
          dentro=None):
    peso = "bold" if negrita else "normal"
    a = f' text-anchor="{ancla}"' if ancla != "start" else ""
    partes.append(f'<text x="{f(x)}" y="{f(y)}" font-size="{fs}" font-weight="{peso}" '
                  f'fill="{relleno}"{a}>{esc(s)}</text>')
    REGISTRO.append({"s": s, "fs": fs, "negrita": negrita, "x": x, "y": y, "ancla": ancla,
                     "contexto": contexto, "dentro": dentro})


def rect(partes, x0, y0, x1, y1, borde, grosor, relleno="none", rx=0):
    partes.append(f'<rect x="{f(x0)}" y="{f(y0)}" width="{f(x1 - x0)}" height="{f(y1 - y0)}" '
                  f'rx="{rx}" fill="{relleno}" stroke="{borde}" stroke-width="{grosor}"/>')


def linea(partes, puntos, color, grosor, marcador=None, nombre=None):
    d = " ".join(("M" if i == 0 else "L") + f"{f(x)},{f(y)}" for i, (x, y) in enumerate(puntos))
    m = f' marker-end="url(#{marcador})"' if marcador else ""
    partes.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{grosor}"{m}/>')
    if nombre:
        for i, (p, q) in enumerate(zip(puntos, puntos[1:]), start=1):
            MARCAS.append((f"{nombre}, tramo {i}", (min(p[0], q[0]) - 0.6, min(p[1], q[1]) - 0.6,
                                                    max(p[0], q[0]) + 0.6, max(p[1], q[1]) + 0.6)))


def ancho(s, fs, negrita=False):
    """Ancho para componer: tabla de métricas del script (determinística)."""
    return base.ancho_negrita(s, fs) if negrita else base.ancho(s, fs)


def envolver(s, fs, ancho_max, negrita=False):
    return [x for x, _ in base.envolver(s, fs, ancho_max, negrita)]


def componer_izquierda(partes, res):
    """La línea de tiempo. Devuelve su alto, la y del rótulo de las
    modificaciones (de donde sale la flecha) y la x donde la flecha empieza."""
    y = Y0 + FS * 0.78 - IL
    for x in TITULO_IZQ[0]:
        y += IL
        texto(partes, X_IZQ, y, x, FS, True, contexto="título izquierda")
    for x in TITULO_IZQ[1]:
        y += IL_CHICO
        texto(partes, X_IZQ, y, x, FS_CHICO, relleno=TINTA_SUAVE, contexto="título izquierda")
    x_eje, x_txt = X_IZQ + 8, X_IZQ + 22
    paso = 27
    # Las comunicaciones de la fila del punto van en el eje; la última
    # incorporada, que no está en la fila, va aparte.
    fila = [(rol, c) for rol, c in res["eje"] if rol != "ultima"]
    ultima = [(rol, c) for rol, c in res["eje"] if rol == "ultima"]
    if len(ultima) != 1 or res["eje"][-1] != ultima[0]:
        raise SystemExit("la última comunicación incorporada no cierra el eje")
    y_items = []
    y += 30
    for _ in fila:
        y_items.append(y)
        y += paso
    y_fin = y_items[-1]
    linea(partes, [(x_eje, y_items[0]), (x_eje, y_fin)], TRAZO, "1.4", nombre="eje")
    x_corchete = x_txt + ancho("«A» 0000", FS, True) + 12
    x_rol = x_corchete + 8                # columna de los rótulos de rol
    modif = [yy for (rol, _), yy in zip(fila, y_items) if rol == "modifica"]
    for (rol, c), yy in zip(fila, y_items):
        r = 4.2
        if rol == "origen":
            partes.append(f'<circle cx="{f(x_eje)}" cy="{f(yy)}" r="{r}" fill="{TRAZO}"/>')
        else:
            partes.append(f'<circle cx="{f(x_eje)}" cy="{f(yy)}" r="{r}" fill="white" '
                          f'stroke="{TRAZO}" stroke-width="1.6"/>')
        MARCAS.append((f"marcador «A» {c}", (x_eje - 5.5, yy - 5.5, x_eje + 5.5, yy + 5.5)))
        texto(partes, x_txt, yy + FS * 0.36, f"«A» {c}", FS, True, contexto="comunicación")
        if rol == "origen":
            texto(partes, x_rol, yy + FS_CHICO * 0.36, ROTULO_ORIGEN, FS_CHICO,
                  relleno=TINTA_SUAVE, contexto="rol")
    # Corchete de las modificaciones.
    t = 5
    y0c, y1c = modif[0] - 7, modif[-1] + 7
    linea(partes, [(x_corchete - t, y0c), (x_corchete, y0c), (x_corchete, y1c),
                   (x_corchete - t, y1c)], TRAZO, "1.2", nombre="corchete")
    ym = (y0c + y1c) / 2.0
    texto(partes, x_rol, ym + FS_CHICO * 0.36, ROTULO_MODIFICAN, FS_CHICO,
          relleno=TINTA_SUAVE, contexto="rol")

    # Separación: una línea de puntos a lo ancho de la columna, como el corte
    # de la figura de la página del ejemplo.
    y_sep = y_fin + 20
    partes.append(f'<path d="M{f(X_IZQ + 1)},{f(y_sep)} L{f(X_IZQ + W_IZQ - 1)},{f(y_sep)}" '
                  f'fill="none" stroke="{TRAZO}" stroke-width="1.6" stroke-linecap="round" '
                  f'stroke-dasharray="0.1,5"/>')
    MARCAS.append(("línea de puntos", (X_IZQ, y_sep - 1, X_IZQ + W_IZQ, y_sep + 1)))

    # La última comunicación incorporada, fuera del eje: rombo, número, fecha
    # del historial y su rótulo debajo.
    _, c = ultima[0]
    yy = y_sep + 22
    partes.append(f'<path d="M{f(x_eje)},{f(yy - 5.5)} L{f(x_eje + 5.5)},{f(yy)} '
                  f'L{f(x_eje)},{f(yy + 5.5)} L{f(x_eje - 5.5)},{f(yy)} Z" fill="{TRAZO}"/>')
    MARCAS.append((f"marcador «A» {c}", (x_eje - 5.5, yy - 5.5, x_eje + 5.5, yy + 5.5)))
    texto(partes, x_txt, yy + FS * 0.36, f"«A» {c}", FS, True, contexto="comunicación")
    texto(partes, x_rol, yy + FS_CHICO * 0.36, res["con_fecha"][c], FS_CHICO, True,
          contexto="fecha del historial")
    yb = yy + FS * 0.36
    for x in ROTULO_ULTIMA:
        yb += IL_CHICO
        texto(partes, x_txt, yb, x, FS_CHICO, relleno=TINTA_SUAVE, contexto="rol")

    y = yb + 26
    for x in NOTA_EJE:
        texto(partes, X_IZQ, y, x, FS_CHICO, relleno=TINTA_SUAVE, contexto="nota del eje")
        y += IL_CHICO
    CAJAS["izquierda"] = (X_IZQ, 0, X_IZQ + W_IZQ, y)
    x_salida = x_rol + ancho(ROTULO_MODIFICAN, FS_CHICO) + 8
    return y - IL_CHICO + FS_CHICO * 0.22, ym, x_salida


def bloque(partes, clave, y, alto, res):
    """Marco de un bloque del manual con su rótulo y sus páginas."""
    x0, x1 = X_DER, X_DER + W_DER
    rect(partes, x0, y, x1, y + alto, BORDE, "1", FONDO_BLOQUE, rx=3)
    CAJAS[clave] = (x0, y, x1, y + alto)
    a, b = res["rangos"][clave]
    paginas = f"pág. {a}" if a == b else f"págs. {a}–{b}"
    yt = y + PAD + FS * 0.78
    texto(partes, x0 + PAD, yt, NOMBRE_BLOQUE[clave], FS, True, contexto=f"rótulo {clave}",
          dentro=clave)
    texto(partes, x1 - PAD, yt, paginas, FS_CHICO, relleno=TINTA_SUAVE, ancla="end",
          contexto=f"páginas {clave}", dentro=clave)
    return yt


def componer_derecha(partes, res):
    y = Y0 + FS * 0.78
    texto(partes, X_DER, y, TITULO_DER, FS, True, contexto="título derecha")
    y += 12
    x0, x1 = X_DER, X_DER + W_DER
    xi = x0 + PAD
    posiciones = {}

    # Portada: sus tres líneas, tal como están.
    lineas = res["portada"]["lineas"]
    alto = PAD + FS + 4 + len(lineas) * IL_CHICO + PAD - 2
    yt = bloque(partes, "portada", y, alto, res)
    for k, x in enumerate(lineas, start=1):
        texto(partes, xi + 8, yt + 3 + k * IL_CHICO, x, FS_CHICO, k == 1,
              contexto="portada", dentro="portada")
    posiciones["portada"] = (y, y + alto)
    y += alto + SEP_BLOQUE

    # Índice.
    alto = PAD + FS + PAD - 1
    bloque(partes, "indice", y, alto, res)
    posiciones["indice"] = (y, y + alto)
    y += alto + SEP_BLOQUE

    # Secciones: una casilla por sección; la del punto, resaltada, con el
    # punto debajo.
    secciones = sorted(res["primera"])
    alto_cas, sep_cas = 22, 4
    w_cas = (W_DER - 2 * PAD - (len(secciones) - 1) * sep_cas) / len(secciones)
    alto_rec = 2 * IL_CHICO + 12
    alto = PAD + FS + 8 + alto_cas + 10 + alto_rec + PAD
    yt = bloque(partes, "secciones", y, alto, res)
    yc = yt + 8
    x_sec = None
    for i, n in enumerate(secciones):
        xa = xi + i * (w_cas + sep_cas)
        es = n == res["seccion"]
        rect(partes, xa, yc, xa + w_cas, yc + alto_cas, ACENTO if es else BORDE,
             "1.6" if es else "1", ACENTO_FONDO if es else "white", rx=2)
        CAJAS[f"casilla {n}"] = (xa, yc, xa + w_cas, yc + alto_cas)
        texto(partes, xa + w_cas / 2, yc + alto_cas / 2 + FS_CHICO * 0.36, str(n), FS_CHICO,
              es, ancla="middle", contexto="casilla de sección", dentro=f"casilla {n}")
        if es:
            x_sec = xa + w_cas / 2
    yr = yc + alto_cas + 10
    rect(partes, xi, yr, x1 - PAD, yr + alto_rec, ACENTO, "1.6", ACENTO_FONDO, rx=2)
    CAJAS["punto"] = (xi, yr, x1 - PAD, yr + alto_rec)
    linea(partes, [(x_sec, yc + alto_cas), (x_sec, yr)], ACENTO, "1.6", nombre="unión sección-punto")
    texto(partes, xi + 6, yr + 4 + IL_CHICO - 3,
          f"{res['etiqueta_seccion']} · pág. {res['pagina_punto']}", FS_CHICO,
          relleno=TINTA_SUAVE, contexto="sección del punto", dentro="punto")
    texto(partes, xi + 6, yr + 4 + 2 * IL_CHICO - 3, res["etiqueta_punto"], FS_CHICO, True,
          contexto="punto", dentro="punto")
    posiciones["secciones"] = (y, y + alto)
    y += alto + SEP_BLOQUE

    # Tabla de correlaciones: encabezado y la fila del punto.
    fila = res["fila"]
    w_p, w_c = 56, 104
    xc = [xi, xi + w_p, xi + w_p + w_c, x1 - PAD]
    # Holgura menor que la general: el control con métricas reales frena si
    # una línea se sale de la fila.
    obs = envolver(fila["texto_obs"], FS_CHICO, xc[3] - xc[2] - 6 - HOLGURA / 2)
    n_lin = max(len(obs), len(fila["com"]))
    alto_fila = n_lin * IL_CHICO + 8
    alto = PAD + FS + 8 + IL_CHICO + 4 + alto_fila + PAD
    yt = bloque(partes, "tabla", y, alto, res)
    ye = yt + 8
    for i, e in enumerate(ENCABEZADO_TABLA):
        texto(partes, xc[i] + 6, ye + IL_CHICO - 4, e, FS_CHICO, relleno=TINTA_SUAVE,
              contexto="encabezado de la tabla", dentro="tabla")
    yf = ye + IL_CHICO + 4
    linea(partes, [(xi, yf - 2), (x1 - PAD, yf - 2)], BORDE, "0.8", nombre="regla de la tabla")
    rect(partes, xi, yf, x1 - PAD, yf + alto_fila, ACENTO, "1.6", ACENTO_FONDO, rx=2)
    CAJAS["fila"] = (xi, yf, x1 - PAD, yf + alto_fila)
    texto(partes, xc[0] + 6, yf + IL_CHICO, f"{PUNTO}.", FS_CHICO, True, contexto="fila",
          dentro="fila")
    for k, x in enumerate(fila["com"]):
        texto(partes, xc[1] + 6, yf + IL_CHICO + k * IL_CHICO, x, FS_CHICO, contexto="fila",
              dentro="fila")
    for k, x in enumerate(obs):
        texto(partes, xc[2] + 6, yf + IL_CHICO + k * IL_CHICO, x, FS_CHICO, contexto="fila",
              dentro="fila")
    posiciones["tabla"] = (y, y + alto)
    y += alto + SEP_BLOQUE

    # Historial: su título y la última de sus últimas modificaciones.
    lineas = [TITULO_HISTORIAL, f"{LINEA_MODIFICACIONES} {OMISION} {res['linea_hist']}"]
    alto = PAD + FS + 4 + len(lineas) * IL_CHICO + PAD - 2
    yt = bloque(partes, "historial", y, alto, res)
    for k, x in enumerate(lineas, start=1):
        texto(partes, xi + 8, yt + 3 + k * IL_CHICO, x, FS_CHICO, contexto="historial",
              dentro="historial")
    posiciones["historial"] = (y, y + alto)
    y += alto
    CAJAS["derecha"] = (x0, 0, x1, y)
    return y, posiciones


def componer(res):
    del REGISTRO[:]
    CAJAS.clear()
    del MARCAS[:]
    partes = []
    alto_izq, y_flecha_izq, x_salida = componer_izquierda(partes, res)
    alto_der, pos = componer_derecha(partes, res)
    # La flecha: horizontal, del rótulo de las modificaciones al bloque de las
    # secciones; tiene que llegar a ese bloque.
    y0s, y1s = pos["secciones"]
    xa, xb = x_salida, X_DER - 3
    if not (xa < xb and y0s + 10 <= y_flecha_izq <= y1s - 10):
        raise SystemExit("la flecha no llega al bloque de las secciones")
    linea(partes, [(xa, y_flecha_izq), (xb, y_flecha_izq)], FLECHA, "1.6", "punta",
          nombre="flecha")
    # El rótulo, centrado en la calle entre las dos columnas, sobre la flecha.
    xm = (X_IZQ + W_IZQ + X_DER) / 2.0
    y_base = y_flecha_izq - 7 - FS_CHICO * 0.22
    for k, x in enumerate(reversed(ROTULO_FLECHA)):
        texto(partes, xm, y_base - k * IL_CHICO, x, FS_CHICO, relleno=TINTA_SUAVE,
              ancla="middle", contexto="rótulo de la flecha")
    alto_total = max(alto_izq, alto_der) + MARGEN
    alto_cm = ANCHO_FIGURA_CM * alto_total / W
    cabeza = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{ANCHO_FIGURA_CM:.2f}cm" '
        f'height="{alto_cm:.2f}cm" viewBox="0 0 {W} {f(alto_total)}" font-family="{TIPOGRAFIA}">',
        f'<rect width="{W}" height="{f(alto_total)}" fill="white"/>',
        '<defs><marker id="punta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" '
        f'markerHeight="6" orient="auto"><path d="M0,0L10,5L0,10z" fill="{FLECHA}"/></marker></defs>',
    ]
    return "\n".join(cabeza + partes + ["</svg>"]) + "\n", alto_total


# --------------------------------------------------------------------------- #
# Controles de geometría y medidas                                             #
# --------------------------------------------------------------------------- #
def cruza(a, b):
    return a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]


def contiene(c, b):
    return c[0] <= b[0] and b[2] <= c[2] and c[1] <= b[1] and b[3] <= c[3]


def controlar_geometria(alto_total):
    medir = proc.medidor()
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
    return fuente, len(REGISTRO), len(MARCAS), len(CAJAS), tamanos, fallas, cajas_texto


# --------------------------------------------------------------------------- #
# Margen a los bordes                                                          #
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
    proc.grabar_densidad(SALIDA_PNG, DPI)
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
    print(f"E0:  {REL_ESTRUCTURA}   sha256 {ESTRUCTURA_SHA256[:12]}… (comprobado)")
    print(f"ESTADÍSTICA: {REL_ESTADISTICAS}   sha256 {ESTADISTICAS_SHA256[:12]}… (comprobado)")
    print(f"PORTADA (página 1): {res['portada']['lineas']}")
    print(f"BLOQUES ({res['n_paginas']} páginas): " + "; ".join(
        f"{NOMBRE_BLOQUE[c]} {a}–{b}" for c, (a, b) in res["rangos"].items()))
    print(f"     primera página de cada sección (= E0): {res['primera']}")
    fila = res["fila"]
    print(f"FILA del {PUNTO} (tabla de correlaciones, página {fila['pagina']}):")
    print(f"     Com.: {fila['com']}")
    print(f"     Observaciones: {fila['obs']}")
    print(f"     origen {fila['origen']}; lo modificaron {fila['modifican']}")
    print(f"HISTORIAL: fechas de comunicaciones que da el PDF: {res['fechas']}")
    print("EJE (orden por número):")
    for rol, c in res["eje"]:
        print(f"     “A” {c:5d}  {rol:9s} fecha: {res['con_fecha'].get(c, 'NO ENCONTRADA en el PDF')}")
    print("     fechas que el historial da a las comunicaciones del eje (lista y entradas, "
          "dd/mm/aa y d.m.aa): " + "; ".join(
              f"“A” {c} {res['fechas_hist'].get(('A', c)) or 'ninguna'}" for _, c in res["eje"]))
    print(f"     comunicaciones del historial con alguna fecha: "
          f"{[f'“{l}” {n}' for (l, n), v in sorted(res['fechas_hist'].items()) if v]}")
    print(f"PUNTO: {res['etiqueta_punto']!r} en la página {res['pagina_punto']} "
          f"({res['etiqueta_seccion']!r}); comprobado en el PDF")

    svg, alto_total = componer(res)
    fuente, n_txt, n_marcas, n_cajas, tamanos, fallas, cajas_texto = controlar_geometria(alto_total)
    minimos, fallas_margen, n_elem = controlar_margen(svg, cajas_texto, alto_total)
    print(f"GEOMETRÍA ({fuente}): {n_txt} textos, {n_cajas} cajas, {n_marcas} marcas; "
          f"fallas: {len(fallas)}")
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
