#!/usr/bin/env python3
"""Figura «el tamaño de los Textos Ordenados» (capítulo 3), versión 2.

Las páginas de cada uno de los 157 Textos Ordenados del corpus (los 152 del
corpus más los 5 del conjunto de desarrollo), ordenados de mayor a menor, en
escala logarítmica, una barra por documento con un color por clase (normativa
general, régimen informativo) y leyenda. Van rotulados el más grande, con el
rótulo fijo ROTULO_MAYOR («Manual de cuentas (régimen informativo)»; el script
comprueba que su título en el inventario diga «Manual de Cuentas» y que su
clase sea régimen informativo, y lo imprime completo), y Clasificación de
deudores, por su título tal como figura en el inventario del corpus.

Nada del contenido se tipea ni se supone:
- las páginas y la clase de cada documento salen de estadisticas_corpus.json
  (claves `por_to` de `corpus_152` y de `desarrollo_5`; la clase es el campo
  `categoria`), con candado de sha256; el script comprueba que las páginas de
  cada documento sean las de la sonda (`sonda_paginas`) y que la suma por
  conjunto sea la que declara el mismo archivo (`R2_paginas_total`);
- los títulos salen del inventario del corpus: inventario_tos.csv para los 152
  (campo `titulo_oficial`) e inventario_resumen.json para los 5 del conjunto de
  desarrollo (`subset_excluido`, que no están en el CSV), los dos con candado de
  sha256 igual al que declara estadisticas_corpus.json en `fuentes_principales`;
  la clase de cada uno de los 152 se contrasta con la del CSV;
- los totales por clase (documentos, páginas, mínimo, mediana y máximo) se
  recomputan; si no dan 103 y 54 documentos y 7.321 páginas en total, el
  script frena.
Las barras parten de 0,5 páginas, debajo del 1 del eje, para que los
documentos de una página se vean.

Controles de geometría, en cada corrida (el script frena si fallan), con las
métricas reales de Helvetica: ningún texto por debajo de 7 pt impresos a 15 cm,
fuera del lienzo, superpuesto a otro, fuera de la caja que lo contiene,
cortado por el borde de otra caja ni tocado por una marca (barras, líneas de
la grilla, ejes, líneas guía de los rótulos); y ningún texto ni elemento
dibujado a menos de 2 mm (MARGEN_MM, a 15 cm de ancho) de uno de los cuatro
bordes.

Colores de las clases: los lugares 1 (azul) y 3 (aguamarina) de la paleta
categórica validada de la guía de gráficos; el lugar 2, naranja, queda fuera
porque las figuras de la tesis reservan el naranja a las remisiones y al
resaltado del ejemplo. El par pasa el validador de paleta en modo claro
(separación para daltonismo ΔE 23,1; visión normal 24,0); el aguamarina tiene
un contraste de 2,74:1 con el fondo, por eso la leyenda y los rótulos van en
tinta y los totales por clase están en el LEEME.

Reutiliza por importación, como la figura de la página del ejemplo: de
generar_figura_norma_a_grafo.py, la tipografía, el escape y formato del SVG y
la tabla de métricas; de generar_figura_proceso_extraccion.py, el ancho de
texto de 15 cm, la exportación a PNG a 300 dpi con la densidad grabada y el
medidor con métricas reales de Helvetica.

El SVG es intermedio: se pasa a rsvg-convert por la entrada estándar y no se
escribe salvo con --svg. Salidas: figura_tamano_tos.png y figura_tamano_tos.pdf,
las dos byte-reproducibles (el PDF, con la fecha de creación fijada por
SOURCE_DATE_EPOCH).

Uso (desde la raíz del repo):
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_tamano_tos.py
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_tamano_tos.py --svg <ruta>
"""

import argparse
import csv
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

sys.dont_write_bytecode = True
AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import generar_figura_norma_a_grafo as base          # noqa: E402
import generar_figura_proceso_extraccion as proc     # noqa: E402

RAIZ = os.path.abspath(os.path.join(AQUI, "..", "..", ".."))
SALIDA_PNG = os.path.join(AQUI, "figura_tamano_tos.png")
SALIDA_PDF = os.path.join(AQUI, "figura_tamano_tos.pdf")

# --------------------------------------------------------------------------- #
# Fuentes y candados                                                           #
# --------------------------------------------------------------------------- #
REL_ESTADISTICAS = "reports/u_insumos_cap/estadisticas_corpus.json"
REL_INVENTARIO = "data/experiment/escalado_prep/inventario_tos.csv"
REL_RESUMEN = "data/experiment/escalado_prep/inventario_resumen.json"
ESTADISTICAS_SHA256 = "1630d1de9f5c065eec00a237f2ba21ff43e4ee11e9332409c56593b12ccbe6ab"
INVENTARIO_SHA256 = "a1db24fd2beaed2110349f295e7928bc0cd9d18333cce527773233a156a37e1f"
RESUMEN_SHA256 = "d60e65abda005433ac5d13c367b55fd40efa3124b1c698e1633f6fc1bd306f82"
CONJUNTOS = ("corpus_152", "desarrollo_5")
EJEMPLO = "cla"
# Totales que la figura tiene que reproducir (mandato de la unidad).
ESPERADO = {"normativa_general": 103, "regimen_informativo": 54, "paginas": 7321}
CLASES = ("normativa_general", "regimen_informativo")
NOMBRE_CLASE = {"normativa_general": "Normativa general",
                "regimen_informativo": "Régimen informativo"}
# Rótulo del documento más grande (su título completo del inventario va en el
# LEEME y en la consola). Vale solo si el título del inventario dice «Manual de
# Cuentas» y la clase es régimen informativo (se comprueba en main()).
ROTULO_MAYOR = "Manual de cuentas (régimen informativo)"

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
COLOR_CLASE = {"normativa_general": "#2a78d6", "regimen_informativo": "#1baf7a"}
GRILLA = "#e1e0d9"
EJE = "#c3c2b7"
GUIA = "#898781"
TINTA = "#1f1f1f"
TINTA_SUAVE = "#555555"
esc, f = base.esc, base.f

FS = 14                 # rótulos de los documentos y leyenda (8,27 pt impresos)
FS_CHICO = 13           # ejes (7,68 pt impresos)
IL = 16

# Área del gráfico (unidades de lienzo) y escala logarítmica.
XL, XR = 50, W - MARGEN
YT, YB = 42, 318
V_BASE, V_TOPE = 0.5, 3000.0          # las barras parten de 0,5 páginas
MARCAS_EJE = (1, 10, 100, 1000)
TITULO_EJE_Y = "Páginas (escala logarítmica)"


def y_de(v):
    a, b = math.log10(V_BASE), math.log10(V_TOPE)
    return YB - (math.log10(v) - a) / (b - a) * (YB - YT)


def ancho(s, fs, negrita=False):
    """Ancho para componer: tabla de métricas del script (determinística)."""
    return base.ancho_negrita(s, fs) if negrita else base.ancho(s, fs)


def numero(v):
    """Mediana en castellano: entera sin decimales; si no, con coma."""
    return str(int(v)) if float(v).is_integer() else f"{v:.1f}".replace(".", ",")


def miles(n):
    return f"{n:,}".replace(",", ".")


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
    candado(REL_ESTADISTICAS, ESTADISTICAS_SHA256)
    candado(REL_INVENTARIO, INVENTARIO_SHA256)
    candado(REL_RESUMEN, RESUMEN_SHA256)
    with open(os.path.join(RAIZ, REL_ESTADISTICAS), encoding="utf-8") as fh:
        est = json.load(fh)
    declaradas = est["fuentes_principales"]
    for rel, s in ((REL_INVENTARIO, INVENTARIO_SHA256), (REL_RESUMEN, RESUMEN_SHA256)):
        if declaradas.get(rel) != s:
            raise SystemExit(f"estadisticas_corpus.json no declara {rel} con este sha256")
    with open(os.path.join(RAIZ, REL_INVENTARIO), encoding="utf-8", newline="") as fh:
        inventario = {r["id"]: r for r in csv.DictReader(fh)}
    with open(os.path.join(RAIZ, REL_RESUMEN), encoding="utf-8") as fh:
        resumen = {x["id_interno"]: x["titulo"] for x in json.load(fh)["subset_excluido"]}

    docs, fallas = [], []
    for conj in CONJUNTOS:
        c = est["conjuntos"][conj]
        por_to = c["por_to"]
        if sorted(por_to) != sorted(c["ids"]) or len(por_to) != c["tos"]:
            fallas.append(f"{conj}: `por_to`, `ids` y `tos` no coinciden")
        for i, d in sorted(por_to.items()):
            if d["paginas"] != d["sonda_paginas"]:
                fallas.append(f"{conj}/{i}: páginas {d['paginas']} ≠ sonda {d['sonda_paginas']}")
            if d["categoria"] not in CLASES:
                fallas.append(f"{conj}/{i}: clase desconocida {d['categoria']!r}")
            if conj == "corpus_152":
                fila = inventario.get(i)
                if not fila:
                    fallas.append(f"{i}: no está en el inventario")
                    continue
                if fila["categoria"] != d["categoria"]:
                    fallas.append(f"{i}: la clase del inventario ≠ la de la estadística")
                titulo = fila["titulo_oficial"]
            else:
                if i not in resumen:
                    fallas.append(f"{i}: no está en el resumen del inventario")
                    continue
                titulo = resumen[i]
            docs.append({"id": i, "conjunto": conj, "clase": d["categoria"],
                         "paginas": d["paginas"], "titulo": titulo})
        suma = sum(d["paginas"] for d in por_to.values())
        if suma != c["R2_paginas_total"]:
            fallas.append(f"{conj}: suma de páginas {suma} ≠ R2_paginas_total {c['R2_paginas_total']}")
    if sorted(inventario) != sorted(est["conjuntos"]["corpus_152"]["por_to"]):
        fallas.append("el inventario y el corpus de 152 no tienen los mismos documentos")
    if sorted(resumen) != sorted(est["conjuntos"]["desarrollo_5"]["por_to"]):
        fallas.append("el resumen del inventario y el conjunto de desarrollo no coinciden")
    if len({d["id"] for d in docs}) != len(docs):
        fallas.append("hay documentos repetidos entre los dos conjuntos")
    if fallas:
        raise SystemExit("FALLA de fuentes:\n  " + "\n  ".join(fallas))
    # De mayor a menor; a igual cantidad de páginas, por identificador, para
    # que el orden no dependa de la lectura.
    docs.sort(key=lambda d: (-d["paginas"], d["id"]))
    return docs


def totales(docs):
    out = {}
    for c in CLASES:
        p = [d["paginas"] for d in docs if d["clase"] == c]
        out[c] = {"documentos": len(p), "paginas": sum(p), "minimo": min(p),
                  "mediana": statistics.median(p), "maximo": max(p)}
    p = [d["paginas"] for d in docs]
    out["total"] = {"documentos": len(p), "paginas": sum(p), "minimo": min(p),
                    "mediana": statistics.median(p), "maximo": max(p)}
    return out


def verificar_totales(tot):
    obtenido = {"normativa_general": tot["normativa_general"]["documentos"],
                "regimen_informativo": tot["regimen_informativo"]["documentos"],
                "paginas": tot["total"]["paginas"]}
    if obtenido != ESPERADO:
        raise SystemExit(f"FRENO: los totales no dan lo esperado: {obtenido} ≠ {ESPERADO}")


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


def linea(partes, puntos, color, grosor, nombre=None):
    d = " ".join(("M" if i == 0 else "L") + f"{f(x)},{f(y)}" for i, (x, y) in enumerate(puntos))
    partes.append(f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{grosor}"/>')
    if nombre:
        for i, (p, q) in enumerate(zip(puntos, puntos[1:]), start=1):
            MARCAS.append((f"{nombre}, tramo {i}", (min(p[0], q[0]) - 0.5, min(p[1], q[1]) - 0.5,
                                                    max(p[0], q[0]) + 0.5, max(p[1], q[1]) + 0.5)))


def componer(docs, tot):
    del REGISTRO[:]
    CAJAS.clear()
    del MARCAS[:]
    partes = []
    n = len(docs)
    paso = (XR - XL) / n
    ancho_barra = paso - 0.8

    # Grilla y eje: líneas finas, detrás de las barras.
    for v in MARCAS_EJE:
        y = y_de(v)
        linea(partes, [(XL, y), (XR, y)], GRILLA, "0.8", nombre=f"grilla {v}")
        texto(partes, XL - 6, y + FS_CHICO * 0.36, miles(v), FS_CHICO, relleno=TINTA_SUAVE,
              ancla="end", contexto="marca del eje")
    linea(partes, [(XL, YB), (XR, YB)], EJE, "1", nombre="eje x")
    texto(partes, MARGEN, YT - 14, TITULO_EJE_Y, FS_CHICO, relleno=TINTA_SUAVE,
          contexto="título del eje y")

    # Barras.
    x_de = {}
    for i, d in enumerate(docs):
        x0 = XL + i * paso + 0.4
        y0 = y_de(d["paginas"])
        partes.append(f'<rect x="{f(x0)}" y="{f(y0)}" width="{ancho_barra:.2f}" '
                      f'height="{f(YB - y0)}" fill="{COLOR_CLASE[d["clase"]]}"/>')
        MARCAS.append((f"barra {i + 1}", (x0, y0, x0 + ancho_barra, YB)))
        x_de[d["id"]] = (x0, x0 + ancho_barra, y0)

    # Rótulos: el más grande, a la derecha de su barra; Clasificación de
    # deudores, sobre las barras, con una línea guía hasta la suya.
    mayor = docs[0]
    xa, xb, ya = x_de[mayor["id"]]
    xt = xb + 8
    yt = ya + FS * 0.36                   # a la altura del tope de su barra
    texto(partes, xt, yt, ROTULO_MAYOR, FS, True, contexto="rótulo del mayor")
    texto(partes, xt + ancho(ROTULO_MAYOR, FS, True) + 10, yt,
          f"{miles(mayor['paginas'])} páginas", FS, relleno=TINTA_SUAVE, contexto="rótulo del mayor")
    ej = next(d for d in docs if d["id"] == EJEMPLO)
    xa, xb, ya = x_de[EJEMPLO]
    xm = (xa + xb) / 2
    yl = y_de(1000) + 30                  # entre las líneas de 1.000 y 100
    # La línea guía baja por el centro de su barra; el texto, a su derecha.
    texto(partes, xm + 5, yl, ej["titulo"], FS, True, contexto="rótulo del ejemplo")
    texto(partes, xm + 5, yl + IL, f"{miles(ej['paginas'])} páginas", FS, relleno=TINTA_SUAVE,
          contexto="rótulo del ejemplo")
    linea(partes, [(xm, yl - FS * 0.3), (xm, ya - 1.5)], GUIA, "1", nombre="guía del ejemplo")
    if not (xa < xm < xb):
        raise SystemExit("la línea guía no llega a la barra del ejemplo")

    # Leyenda, a la derecha, entre las líneas de 1.000 y 100 (las barras de
    # ese lado no llegan a 100): una muestra por clase y su cantidad.
    y = y_de(1000) + 30
    x_ley = 470
    for c in CLASES:
        partes.append(f'<rect x="{f(x_ley)}" y="{f(y - 10)}" width="14" height="12" '
                      f'fill="{COLOR_CLASE[c]}"/>')
        MARCAS.append((f"muestra {c}", (x_ley, y - 10, x_ley + 14, y + 2)))
        texto(partes, x_ley + 22, y, f"{NOMBRE_CLASE[c]} ({tot[c]['documentos']})", FS,
              contexto="leyenda")
        y += IL + 2

    # Título del eje x.
    y_titulo_x = YB + 22
    texto(partes, XL, y_titulo_x, f"{tot['total']['documentos']} Textos Ordenados, de mayor a "
          f"menor; {miles(tot['total']['paginas'])} páginas en total", FS_CHICO,
          relleno=TINTA_SUAVE, contexto="título del eje x")
    alto_total = y_titulo_x + FS_CHICO * 0.22 + MARGEN
    alto_cm = ANCHO_FIGURA_CM * alto_total / W
    cabeza = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{ANCHO_FIGURA_CM:.2f}cm" '
        f'height="{alto_cm:.2f}cm" viewBox="0 0 {W} {f(alto_total)}" font-family="{TIPOGRAFIA}">',
        f'<rect width="{W}" height="{f(alto_total)}" fill="white"/>',
    ]
    return "\n".join(cabeza + partes + ["</svg>"]) + "\n", alto_total, paso


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

    docs = cargar()
    tot = totales(docs)
    print(f"ESTADÍSTICA: {REL_ESTADISTICAS}   sha256 {ESTADISTICAS_SHA256[:12]}… (comprobado)")
    print(f"INVENTARIO:  {REL_INVENTARIO}   sha256 {INVENTARIO_SHA256[:12]}… (comprobado, "
          "= fuentes_principales)")
    print(f"             {REL_RESUMEN}   sha256 {RESUMEN_SHA256[:12]}… (comprobado, "
          "= fuentes_principales)")
    print("TOTALES (clase = campo `categoria`):")
    print(f"  {'clase':22s} {'docs':>5s} {'páginas':>8s} {'mín':>5s} {'mediana':>8s} {'máx':>6s}")
    for c in CLASES + ("total",):
        t = tot[c]
        print(f"  {NOMBRE_CLASE.get(c, 'Total'):22s} {t['documentos']:5d} {t['paginas']:8d} "
              f"{t['minimo']:5d} {numero(t['mediana']):>8s} {t['maximo']:6d}")
    verificar_totales(tot)
    print(f"  = {ESPERADO} (comprobado)")
    rango = {d["id"]: i + 1 for i, d in enumerate(docs)}
    mayor = docs[0]
    if mayor["paginas"] == docs[1]["paginas"]:
        raise SystemExit("el más grande no es único")
    if ("manual de cuentas" not in mayor["titulo"].lower()
            or f"({NOMBRE_CLASE[mayor['clase']].lower()})" not in ROTULO_MAYOR):
        raise SystemExit(f"el rótulo {ROTULO_MAYOR!r} no corresponde al más grande: "
                         f"{mayor['titulo']!r}, {NOMBRE_CLASE[mayor['clase']]}")
    print(f"RÓTULO: {ROTULO_MAYOR!r} (título del inventario: {mayor['titulo']!r}; "
          f"{mayor['conjunto']}, {NOMBRE_CLASE[mayor['clase']]}): {mayor['paginas']} páginas, "
          f"puesto 1 de {len(docs)}")
    d = next(x for x in docs if x["id"] == EJEMPLO)
    print(f"RÓTULO: {d['titulo']!r} (título del inventario; {d['conjunto']}, "
          f"{NOMBRE_CLASE[d['clase']]}): {d['paginas']} páginas, puesto {rango[d['id']]} "
          f"de {len(docs)}")
    svg, alto_total, paso = componer(docs, tot)
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
    print(f"BARRAS: {len(docs)}, paso {paso:.2f} unidades ({ANCHO_FIGURA_CM * paso / W * 10:.2f} mm)")
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
