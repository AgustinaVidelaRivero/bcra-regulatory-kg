#!/usr/bin/env python3
"""Figura «la sección 5 de Clasificación de deudores como árbol» (capítulo 3), versión 2.

La sección 5 del Texto Ordenado de Clasificación de deudores y todos sus
puntos, como árbol con sangría: cada punto con su número y su título tal como
figuran en E0 (estructura_cla.json, campos `numero` y `titulo`), el título
cortado según la regla de titulo_mostrado (abajo). Dos estilos,
con leyenda: punto contenedor (tiene subpuntos) y punto terminal (no los
tiene). Los contenedores con párrafos sin numerar llevan una marca (¶), según
la regla REGLA_MARCA, declarada abajo antes de aplicarse. Los puntos 5.1.1 y
5.1.1.1, los del ejemplo del préstamo, van resaltados con un contorno naranja.
Si la sección tuviera más de UMBRAL_COLAPSO puntos, se mostraría completo su
primer punto de primer nivel (el 5.1) y los demás de primer nivel irían
colapsados, con la cantidad de puntos que contienen; la sección 5 no llega a
ese umbral y se muestra completa.

«Punto contenedor», «punto terminal» y «párrafo sin numerar» son nombres de
este trabajo, no del BCRA (los mismos de la figura de la página del ejemplo).

Nada del contenido se tipea ni se supone:
- el árbol (números, títulos, hijos) sale de estructura_cla.json y la marca, de
  chunks_cla.json, los dos de la E0 de salida_enm01, con candado de sha256;
- el script comprueba que el título mostrado de cada punto (sin «…») sea un
  prefijo, cortado en palabra entera, de la primera línea del punto en la
  página del PDF del corpus que E0 declara (candado de sha256 del PDF), que la
  sección sea la de esa página, que los contenedores y terminales
  de la estructura coincidan con los chunks (un chunk `punto_terminal` por
  terminal, ninguno por contenedor) y que la marca de los chunks coincida con
  los segmentos `intro`/`cierre` de la estructura.

Controles de geometría, en cada corrida (el script frena si fallan), con las
métricas reales de Helvetica: ningún texto por debajo de 7 pt impresos a 15 cm,
fuera del lienzo, superpuesto a otro, fuera de la caja que lo contiene,
cortado por el borde de otra caja ni tocado por una marca (conectores del
árbol, contornos de resaltado); y ningún texto ni elemento dibujado a menos de
2 mm (MARGEN_MM, a 15 cm de ancho) de uno de los cuatro bordes.

Reutiliza por importación, como la figura de la página del ejemplo: de
generar_figura_norma_a_grafo.py, la tipografía, el naranja de resaltado, el
escape y formato del SVG y la tabla de métricas; de
generar_figura_proceso_extraccion.py, el ancho de texto de 15 cm, la
exportación a PNG a 300 dpi con la densidad grabada y el medidor con métricas
reales de Helvetica.

El SVG es intermedio: se pasa a rsvg-convert por la entrada estándar y no se
escribe salvo con --svg. Salidas: figura_arbol_seccion.png y
figura_arbol_seccion.pdf, las dos byte-reproducibles (el PDF, con la fecha de
creación fijada por SOURCE_DATE_EPOCH).

Uso (desde la raíz del repo):
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_arbol_seccion.py
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_arbol_seccion.py --svg <ruta>
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
SALIDA_PNG = os.path.join(AQUI, "figura_arbol_seccion.png")
SALIDA_PDF = os.path.join(AQUI, "figura_arbol_seccion.pdf")

# --------------------------------------------------------------------------- #
# Fuentes y candados                                                           #
# --------------------------------------------------------------------------- #
REL_PDF = "data/experiment/subset/TO_clasificacion_deudores_actual.pdf"
REL_CHUNKS = "data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_cla.json"
REL_ESTRUCTURA = "data/experiment/reextraccion_v2/e0_chunking/salida_enm01/estructura_cla.json"
PDF_SHA256 = "6e7f528d3fea7b756f15e1278eecd828f203f0651fc6f778212033de6a0883e2"
CHUNKS_SHA256 = "98808886a406d8321c678836a55f92eea983d594d95358dd21ceb537487ac0b1"
ESTRUCTURA_SHA256 = "3cd26083fee7355ef3d8027ac353a744c2f1cfa35830535fe1be2b9505eaf917"
TO = "cla"
SECCION = "5"
RESALTADOS = ("5.1.1", "5.1.1.1")
UMBRAL_COLAPSO = 25

# Regla de la marca, declarada antes de aplicarse (tiene_parrafos): un punto
# contenedor lleva la marca si E0 tiene para él al menos un bloque de párrafo
# sin numerar, es decir, un chunk de tipo `mini_chunk` cuya `unidad` es el
# número del punto, con `rol_bloque` `intro` (antes de sus subpuntos) o
# `cierre` (después).
REGLA_MARCA = ("mini_chunk", ("intro", "cierre"))
MARCA = "¶"

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
TRAZO = "#4a5a6a"                   # gris oscuro de la paleta compartida
FONDO_CONTENEDOR = "#e1e7ee"        # el mismo tono, claro (paleta de las figuras hermanas)
BORDE_TERMINAL = "#999999"
CONECTOR = "#8a8a8a"
TINTA = "#1f1f1f"
TINTA_SUAVE = "#555555"
esc, f = base.esc, base.f

FS = 14                 # números y títulos de los puntos (8,27 pt impresos)
FS_CHICO = 13           # leyenda (7,68 pt impresos)
ALTO_CAJA = 24
PASO_FILA = 32
SANGRIA = 26
X0 = MARGEN             # borde izquierdo de la raíz
PAD = 8                 # aire interior de las cajas
ANCHO_MARCA = 16        # casilla de la marca dentro del contenedor
HOLGURA = 8             # margen al cortar títulos con la tabla de métricas
ELIPSIS = "…"
AIRE_RESALTADO = 3.5    # del contorno naranja a la caja

# Texto fijo de la leyenda.
LEYENDA = (
    ("contenedor", "Punto contenedor: tiene subpuntos"),
    ("terminal", "Punto terminal: no tiene subpuntos"),
    ("marca", "Párrafos sin numerar antes o después de los subpuntos"),
    ("resaltado", "Puntos del ejemplo (5.1.1 y 5.1.1.1)"),
)


def sha256(ruta):
    with open(ruta, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def candado(rel, esperado):
    s = sha256(os.path.join(RAIZ, rel))
    if s != esperado:
        raise SystemExit(f"{rel} no es el verificado: sha {s[:12]}… ≠ {esperado[:12]}…")


# --------------------------------------------------------------------------- #
# Carga y comprobaciones                                                       #
# --------------------------------------------------------------------------- #
def cargar():
    candado(REL_PDF, PDF_SHA256)
    candado(REL_CHUNKS, CHUNKS_SHA256)
    candado(REL_ESTRUCTURA, ESTRUCTURA_SHA256)
    with open(os.path.join(RAIZ, REL_ESTRUCTURA), encoding="utf-8") as fh:
        estructura = json.load(fh)
    with open(os.path.join(RAIZ, REL_CHUNKS), encoding="utf-8") as fh:
        chunks = json.load(fh)
    secs = [s for s in estructura["secciones"] if s["numero"] == SECCION]
    if len(secs) != 1:
        raise SystemExit(f"estructura: la sección {SECCION} aparece {len(secs)} veces")
    return secs[0], chunks


def puntos_de(nodo):
    """Todos los puntos bajo `nodo`, en orden de documento."""
    out = []
    for h in nodo.get("hijos", []):
        out.append(h)
        out += puntos_de(h)
    return out


def tiene_parrafos(numero, chunks):
    tipo, roles = REGLA_MARCA
    return any(c["tipo"] == tipo and c["unidad"] == numero and c.get("rol_bloque") in roles
               for c in chunks)


def comprobar(seccion, chunks):
    """Contraste de E0 con el PDF y de la estructura con los chunks."""
    puntos = puntos_de(seccion)
    terminales_chunk = {c["unidad"] for c in chunks if c["tipo"] == "punto_terminal"}
    fallas = []
    for p in puntos:
        es_contenedor = bool(p.get("hijos"))
        if es_contenedor == (p["numero"] in terminales_chunk):
            fallas.append(f"{p['numero']}: la estructura y los chunks no coinciden en si es terminal")
        marca = tiene_parrafos(p["numero"], chunks)
        roles = {sg["rol"] for sg in p.get("segmentos", [])} & set(REGLA_MARCA[1])
        if marca != bool(roles):
            fallas.append(f"{p['numero']}: la marca de los chunks ≠ los segmentos de la estructura")
        if marca and not es_contenedor:
            fallas.append(f"{p['numero']}: un terminal con párrafo sin numerar")
    paginas = sorted({seccion["pagina"]} | {p["pagina"] for p in puntos})
    with pdfplumber.open(os.path.join(RAIZ, REL_PDF)) as doc:
        lineas = {n: [l["text"] for l in doc.pages[n - 1].extract_text_lines()] for n in paginas}
    raiz = f"Sección {seccion['numero']}. {seccion['titulo']}"
    if raiz not in lineas[seccion["pagina"]]:
        fallas.append(f"PDF: {raiz!r} no es una línea de la página {seccion['pagina']}")
    for p in puntos:
        if raiz not in lineas[p["pagina"]]:
            fallas.append(f"PDF: la página {p['pagina']} de {p['numero']} no es de la sección")
    for r in RESALTADOS:
        if r not in {p["numero"] for p in puntos}:
            fallas.append(f"el resaltado {r} no es un punto de la sección")
    if fallas:
        raise SystemExit("FALLA de fuentes:\n  " + "\n  ".join(fallas))
    return puntos, raiz, paginas, lineas


def filas(seccion, chunks, umbral=UMBRAL_COLAPSO):
    """Filas del árbol: (profundidad, nodo, clase, marca, colapsado). Con más de
    `umbral` puntos, el primer punto de primer nivel se muestra completo y los
    demás de primer nivel, colapsados con la cantidad de puntos que contienen."""
    n_puntos = len(puntos_de(seccion))
    colapsar = n_puntos > umbral
    out = []

    def agregar(nodo, prof, completo):
        clase = "contenedor" if nodo.get("hijos") else "terminal"
        marca = clase == "contenedor" and tiene_parrafos(nodo["numero"], chunks)
        if not completo and nodo.get("hijos"):
            out.append((prof, nodo, clase, marca, len(puntos_de(nodo))))
            return
        out.append((prof, nodo, clase, marca, None))
        for h in nodo.get("hijos", []):
            agregar(h, prof + 1, True)
    for i, h in enumerate(seccion.get("hijos", [])):
        agregar(h, 1, not colapsar or i == 0)
    return out, n_puntos, colapsar


def ancho_titulo_max(prof, marca, n_col, num):
    """Ancho disponible para el título en una línea: hasta el margen derecho,
    descontados el número, los aires, la casilla de la marca y la cuenta de
    los colapsados."""
    x0 = X0 + prof * SANGRIA - 12
    extra = f" · {n_col} puntos" if n_col is not None else ""
    usado = PAD + ancho(num, FS, True) + ancho(" ", FS) + ancho(extra, FS) + PAD
    if marca:
        usado += ANCHO_MARCA + 6
    return (W - MARGEN) - x0 - usado - HOLGURA


def titulo_mostrado(titulo, ancho_max):
    """Regla de corte: el título de E0 se corta en una palabra entera. Se quita
    la palabra final si termina en guion (la dividida al final de la línea del
    documento) y, si no entra en una línea, las palabras finales que sobran.
    Lleva «…» si se quitó alguna palabra o si no termina en punto, es decir, si
    la oración que abre el punto sigue en el documento. Devuelve el texto sin
    «…», si lleva «…» y la razón."""
    palabras = titulo.split(" ")
    razones = []
    if palabras[-1].endswith("-"):
        palabras = palabras[:-1]
        razones.append("palabra dividida con guion")
    quitadas = 0
    while palabras:
        t = " ".join(palabras)
        sigue = bool(razones) or quitadas > 0 or not t.endswith(".")
        if ancho(t + (ELIPSIS if sigue else ""), FS) <= ancho_max:
            break
        palabras = palabras[:-1]
        quitadas += 1
    if not palabras:
        raise SystemExit(f"el título {titulo!r} no entra en una línea")
    if quitadas:
        razones.append(f"{quitadas} palabra(s) no entran en una línea")
    t = " ".join(palabras)
    if not t.endswith(".") and not razones:
        razones.append("la oración sigue en el documento")
    return t, bool(razones), razones


def titulos(lista):
    """Título mostrado de cada fila del árbol."""
    out = {}
    for prof, nodo, clase, marca, n_col in lista:
        out[nodo["numero"]] = titulo_mostrado(
            nodo["titulo"], ancho_titulo_max(prof, marca, n_col, nodo["numero"]))
    return out


def comprobar_titulos(lista, mostrados, lineas, chunks):
    """El texto mostrado (sin «…») es un prefijo de la primera línea del punto
    en su página del PDF, cortado en palabra entera; si lleva «…» solo porque
    no termina en punto, el punto sigue en otra línea."""
    texto_chunk = {c["unidad"]: c["texto"] for c in chunks if c["tipo"] == "punto_terminal"}
    fallas = []
    for _, nodo, clase, _, _ in lista:
        num = nodo["numero"]
        t, elipsis, razones = mostrados[num]
        primeras = [x for x in lineas[nodo["pagina"]] if x.startswith(f"{num}. ")]
        if len(primeras) != 1:
            fallas.append(f"{num}: {len(primeras)} líneas del PDF abren con su número")
            continue
        resto = primeras[0][len(num) + 2:]
        if not resto.startswith(t) or (len(resto) > len(t) and resto[len(t)] != " "):
            fallas.append(f"{num}: {t!r} no es un prefijo en palabra entera de {resto!r}")
        if t.endswith("-"):
            fallas.append(f"{num}: el texto mostrado termina en guion")
        if razones == ["la oración sigue en el documento"]:
            if clase != "terminal" or len(texto_chunk.get(num, "").split("\n")) < 2:
                fallas.append(f"{num}: no se puede comprobar que la oración siga")
    if fallas:
        raise SystemExit("FALLA de títulos:\n  " + "\n  ".join(fallas))


# --------------------------------------------------------------------------- #
# Composición                                                                  #
# --------------------------------------------------------------------------- #
REGISTRO = []
CAJAS = {}
MARCAS = []


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


def linea(partes, puntos, color, grosor, nombre=None):
    d = " ".join(("M" if i == 0 else "L") + f"{f(x)},{f(y)}" for i, (x, y) in enumerate(puntos))
    partes.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{grosor}"/>')
    if nombre:
        for i, (p, q) in enumerate(zip(puntos, puntos[1:]), start=1):
            MARCAS.append((f"{nombre}, tramo {i}", (min(p[0], q[0]) - 0.6, min(p[1], q[1]) - 0.6,
                                                    max(p[0], q[0]) + 0.6, max(p[1], q[1]) + 0.6)))


def ancho(s, fs, negrita=False):
    """Ancho para componer: tabla de métricas del script (determinística)."""
    return base.ancho_negrita(s, fs) if negrita else base.ancho(s, fs)


def estilo(partes, clase, x0, y0, x1, y1):
    if clase == "contenedor":
        rect(partes, x0, y0, x1, y1, TRAZO, "1.4", FONDO_CONTENEDOR, rx=3)
    else:
        rect(partes, x0, y0, x1, y1, BORDE_TERMINAL, "1", "white", rx=3)


def casilla_marca(partes, x0, y0, clave):
    """La marca ¶: una casilla con el signo, dentro del contenedor."""
    x1, y1 = x0 + ANCHO_MARCA, y0 + ANCHO_MARCA
    rect(partes, x0, y0, x1, y1, TRAZO, "1", "white", rx=2)
    CAJAS[clave] = (x0, y0, x1, y1)
    texto(partes, (x0 + x1) / 2, y0 + ANCHO_MARCA / 2 + FS_CHICO * 0.36, MARCA, FS_CHICO, True,
          relleno=TRAZO, ancla="middle", contexto="marca", dentro=clave)


def resaltado(partes, x0, y0, x1, y1, nombre):
    a = AIRE_RESALTADO
    rect(partes, x0 - a, y0 - a, x1 + a, y1 + a, ACENTO, "2", rx=5)
    for i, caja in enumerate(((x0 - a - 1, y0 - a - 1, x1 + a + 1, y0 - a + 1),
                              (x0 - a - 1, y1 + a - 1, x1 + a + 1, y1 + a + 1),
                              (x0 - a - 1, y0 - a - 1, x0 - a + 1, y1 + a + 1),
                              (x1 + a - 1, y0 - a - 1, x1 + a + 1, y1 + a + 1)), start=1):
        MARCAS.append((f"contorno de {nombre}, lado {i}", caja))


def componer(lista, mostrados, raiz):
    del REGISTRO[:]
    CAJAS.clear()
    del MARCAS[:]
    partes = []

    # Raíz: el encabezado de la sección, sin caja.
    y = MARGEN + FS * 0.78
    texto(partes, X0, y, raiz, FS, True, contexto="sección")
    y_raiz_base = y + FS * 0.22 + 3
    y = y_raiz_base + 8

    cajas_fila = []
    for prof, nodo, clase, marca, n_col in lista:
        x0 = X0 + prof * SANGRIA - 12
        num = nodo["numero"]
        t, elipsis, _ = mostrados[num]
        tit = t + (ELIPSIS if elipsis else "")
        extra = f" · {n_col} puntos" if n_col is not None else ""
        w_num = ancho(num, FS, True)
        w = PAD + w_num + ancho(" ", FS) + ancho(tit + extra, FS) + PAD
        if marca:
            w += ANCHO_MARCA + 6
        y0, y1 = y, y + ALTO_CAJA
        estilo(partes, clase, x0, y0, x0 + w, y1)
        clave = f"punto {num}"
        CAJAS[clave] = (x0, y0, x0 + w, y1)
        yb = (y0 + y1) / 2 + FS * 0.36
        texto(partes, x0 + PAD, yb, num, FS, True, contexto="número", dentro=clave)
        texto(partes, x0 + PAD + w_num + ancho(" ", FS), yb, tit + extra, FS,
              relleno=TINTA, contexto="título", dentro=clave)
        if marca:
            casilla_marca(partes, x0 + w - PAD - ANCHO_MARCA + 2, y0 + (ALTO_CAJA - ANCHO_MARCA) / 2,
                          f"marca {num}")
        if num in RESALTADOS:
            resaltado(partes, x0, y0, x0 + w, y1, num)
        cajas_fila.append((prof, num, (x0, y0, x0 + w, y1)))
        y += PASO_FILA

    # Conectores: de cada padre (o de la raíz) a sus hijos, en ángulo recto,
    # por la izquierda de las cajas.
    padres = {}
    pila = []
    for prof, num, caja in cajas_fila:
        while pila and pila[-1][0] >= prof:
            pila.pop()
        padres.setdefault(pila[-1][1] if pila else None, []).append((num, caja))
        pila.append((prof, num, caja))
    por_num = {num: caja for _, num, caja in cajas_fila}
    for padre, hijos in padres.items():
        if padre is None:
            xv, ytop = X0 + 6, y_raiz_base
        else:
            c = por_num[padre]
            xv, ytop = c[0] + 8, c[3]
            if padre in RESALTADOS:
                ytop += AIRE_RESALTADO + 1.5
        ymid = [(c[1] + c[3]) / 2 for _, c in hijos]
        linea(partes, [(xv, ytop), (xv, ymid[-1])], CONECTOR, "1.2", nombre=f"conector de {padre}")
        for (num, c), ym in zip(hijos, ymid):
            # El conector llega al contorno naranja, no lo atraviesa.
            xh = c[0] - (AIRE_RESALTADO + 1.5 if num in RESALTADOS else 0)
            linea(partes, [(xv, ym), (xh, ym)], CONECTOR, "1.2", nombre=f"conector de {padre}")

    # Leyenda, en dos columnas, dentro del margen.
    y_ley = y + 10
    alto_ley = 2 * 30 + 10
    x_ley0, x_ley1 = MARGEN + 0.5, W - MARGEN - 0.5
    rect(partes, x_ley0, y_ley, x_ley1, y_ley + alto_ley, "#cccccc", "1", "#fafafa", rx=3)
    CAJAS["leyenda"] = (x_ley0, y_ley, x_ley1, y_ley + alto_ley)
    col = (MARGEN + 12, 420)
    for k, (clave, rotulo) in enumerate(LEYENDA):
        # Dos por fila: (contenedor, terminal) y (marca, resaltado).
        cx = col[k % 2]
        cy = y_ley + 10 + (k // 2) * 30
        xm0, ym0, xm1, ym1 = cx, cy, cx + 34, cy + 20
        if clave in ("contenedor", "terminal"):
            estilo(partes, clave, xm0, ym0, xm1, ym1)
            CAJAS[f"muestra {clave}"] = (xm0, ym0, xm1, ym1)
        elif clave == "marca":
            rect(partes, xm0, ym0, xm1, ym1, TRAZO, "1.4", FONDO_CONTENEDOR, rx=3)
            CAJAS["muestra marca"] = (xm0, ym0, xm1, ym1)
            casilla_marca(partes, xm0 + (34 - ANCHO_MARCA) / 2, ym0 + 2, "marca de la leyenda")
        else:
            rect(partes, xm0 + 4, ym0 + 4, xm1 - 4, ym1 - 4, BORDE_TERMINAL, "1", "white", rx=2)
            CAJAS["muestra resaltado"] = (xm0 + 4, ym0 + 4, xm1 - 4, ym1 - 4)
            resaltado(partes, xm0 + 4, ym0 + 4, xm1 - 4, ym1 - 4, "la muestra")
        texto(partes, xm1 + 10, (ym0 + ym1) / 2 + FS_CHICO * 0.36, rotulo, FS_CHICO,
              relleno=TINTA_SUAVE, contexto="leyenda", dentro="leyenda")
    alto_total = y_ley + alto_ley + 0.5 + MARGEN
    alto_cm = ANCHO_FIGURA_CM * alto_total / W
    cabeza = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{ANCHO_FIGURA_CM:.2f}cm" '
        f'height="{alto_cm:.2f}cm" viewBox="0 0 {W} {f(alto_total)}" font-family="{TIPOGRAFIA}">',
        f'<rect width="{W}" height="{f(alto_total)}" fill="white"/>',
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
    # Las cajas de los puntos no se tocan entre sí.
    puntos = [(k, c) for k, c in CAJAS.items() if k.startswith("punto ")]
    for i in range(len(puntos)):
        for j in range(i + 1, len(puntos)):
            if cruza(puntos[i][1], puntos[j][1]):
                fallas.append(f"las cajas {puntos[i][0]} y {puntos[j][0]} se tocan")
    cajas_texto = [(r["s"], bb) for r, bb in cajas]
    return fuente, len(REGISTRO), len(MARCAS), len(CAJAS), tamanos, fallas, cajas_texto


# --------------------------------------------------------------------------- #
# Margen a los bordes (mismo control que generar_figura_formacion_to.py)      #
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

    seccion, chunks = cargar()
    puntos, raiz, paginas, lineas = comprobar(seccion, chunks)
    lista, n_puntos, colapsar = filas(seccion, chunks)
    mostrados = titulos(lista)
    comprobar_titulos(lista, mostrados, lineas, chunks)
    svg, alto_total = componer(lista, mostrados, raiz)
    print(f"PDF: {REL_PDF}   sha256 {PDF_SHA256[:12]}… (comprobado)")
    print(f"E0:  {REL_ESTRUCTURA}   sha256 {ESTRUCTURA_SHA256[:12]}… (comprobado)")
    print(f"     {REL_CHUNKS}   sha256 {CHUNKS_SHA256[:12]}… (comprobado)")
    print(f"SECCIÓN: {raiz!r}; {n_puntos} puntos (umbral de colapso {UMBRAL_COLAPSO}): "
          + ("se colapsan los de primer nivel salvo el primero" if colapsar
             else "se muestra completa"))
    print(f"     el título mostrado de cada punto (sin «…») es un prefijo en palabra entera "
          f"de su primera línea en el PDF (página {paginas}): comprobado")
    tipo, roles = REGLA_MARCA
    print(f"REGLA DE LA MARCA: chunk `{tipo}` con `unidad` = número del punto y "
          f"`rol_bloque` en {list(roles)}")
    for prof, nodo, clase, marca, n_col in lista:
        rol = sorted({c["rol_bloque"] for c in chunks if c["tipo"] == tipo
                      and c["unidad"] == nodo["numero"] and c.get("rol_bloque") in roles})
        print(f"  {'  ' * prof}{nodo['numero']:9s} {clase:10s} "
              f"{('marca ' + ','.join(rol)) if marca else '':14s} "
              f"{'RESALTADO ' if nodo['numero'] in RESALTADOS else ''}{nodo['titulo']!r}")
    print("TÍTULOS MOSTRADOS (regla de titulo_mostrado):")
    for _, nodo, _, _, _ in lista:
        t, elipsis, razones = mostrados[nodo["numero"]]
        print(f"     {nodo['numero']:9s} {t + (ELIPSIS if elipsis else '')!r}"
              + (f"  <- «…»: {'; '.join(razones)}" if elipsis else ""))
    n_cont = sum(1 for _, _, c, _, _ in lista if c == "contenedor")
    n_marca = sum(1 for _, _, _, m, _ in lista if m)
    print(f"     {len(lista)} filas: {n_cont} contenedores ({n_marca} con marca), "
          f"{len(lista) - n_cont} terminales")
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
