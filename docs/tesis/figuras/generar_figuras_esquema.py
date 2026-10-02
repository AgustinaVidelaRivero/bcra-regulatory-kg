#!/usr/bin/env python3
"""Genera las figuras F1 (esquema de partida) y F1b (esquema congelado) del
capítulo del esquema, POR SCRIPT desde los artefactos sellados — nunca a mano.

Fuentes (se IMPORTAN, jamás se editan):
  F1  — data/experiment/grafo_v2/code/schema.py
        (ENTITY_TYPES: 6 tipos visibles + pseudo-tipo Sujeto; DOMAIN_RANGE: 12
        relaciones).
  F1b — data/experiment/esq/code/prompt_congelado.py
        (ENTITY_TYPES_CONGELADO: 9 tipos + Sujeto; DOMAIN_RANGE_CONGELADO: 13
        relaciones). Esa matriz es, por construcción de la cadena sellada, la
        retocada de prompt_esq3b.py (DOMAIN_RANGE_RETOCADO) sin la fila
        exceptua_operacion; este script lo ASSERTA explícitamente.

La importación de prompt_congelado ejecuta sus candados (hash del prefijo v2
sellado, anclas únicas, remoción completa de requisito_de_estructura): si la
cadena no es la sellada, este script FRENA antes de dibujar.

Diseño compartido (mismas cajas en las mismas posiciones en ambas figuras,
para compararlas):
  - Cajas por tipo de entidad agrupadas en zonas rotuladas: «contenido
    deóntico» (Obligacion, Restriccion, Excepcion; en F1b también Potestad y
    Condicion), «acto regulado» (Operacion, al centro), «anclaje documental»
    (TextoOrdenado, Comunicacion). En F1b, Definicion va en zona propia
    («contenido definitorio»): su delimitación sellada la excluye de los actos
    regulados (ver LEEME).
  - Sujeto: caja de borde discontinuo con la nota «catálogo cerrado (no lo
    emite el extractor)».
  - UNA flecha por cada par (tipo del dominio → tipo del rango) de cada
    relación; las flechas de una misma relación confluyen en un tronco con una
    única punta y un único rótulo. En F1b, lo agregado en la validación (tipos
    nuevos, condicion_de, ampliaciones de dominio) va resaltado: en las
    relaciones preexistentes el TRAMO DE ORIGEN nuevo porta el resalte y el
    tronco compartido conserva el color base.

Versión 2 de F1 (solo F1; F1b se emite byte-idéntica a su versión anterior):
  - La zona deóntica se rotula «lo que la norma manda, prohíbe o exime», en
    dos líneas, y la nota de Sujeto dice «se elige de un catálogo».
  - Las seis flechas entre Obligacion, Restriccion y Operacion (regula ×2,
    condiciona, prohibe, limita, requiere) dejan de ser diagonales que
    convergen en el borde izquierdo de Operacion: van ortogonales y
    separadas. Las de Obligacion bajan al borde SUPERIOR de Operacion en
    escuadras anidadas; requiere sale de ese mismo borde y entra a Obligacion
    por arriba; las tres de Restriccion llegan al borde IZQUIERDO en
    escalera. Cada rótulo queda del lado libre de su propia flecha.
  - exceptua_obligacion pasa por la izquierda de Restriccion: por la derecha
    cruzaría, por topología, las tres flechas que salen de Restriccion hacia
    Operacion.
  - El rótulo de «acto regulado» pasa a la derecha del borde superior de su
    zona: a la izquierda lo atravesarían las tres flechas que bajan.
  - verificar_geometria_f1() FRENA si alguna de esas seis flechas cruza otra
    flecha, si algún rótulo toca un trazo ajeno, una caja u otro rótulo, o si
    el trazo más cercano a un rótulo no es el de su propia flecha.

Versión 3 de F1 (solo F1; F1b sigue byte-idéntica):
  - Se corrigen los tres textos que tocaban un trazo o una caja fuera del
    corredor (rotulos_f1): referencia/modificada_por, establecida_en desde
    Operacion y el rótulo rotado de aplica_a.
  - La guarda pasa a TODA la figura: todo texto (rótulos de relación, de zona
    y la nota de Sujeto) contra todo trazo, caja y texto; todo rótulo de
    relación a no más de 6 px de su flecha y al menos 5 px más cerca de ella
    que de cualquier otra; y los cruces entre flechas tienen que ser
    exactamente los de CRUCES_DECLARADOS (4, inevitables con estas cajas).

Salidas (docs/tesis/figuras/): figura_esquema_partida.svg y
figura_esquema_congelado.svg. El PNG se exporta aparte con rsvg-convert (ver
LEEME de cada figura).

Determinístico: sin fechas, sin aleatoriedad; toda iteración sobre conjuntos
pasa por sorted(). Dos corridas producen bytes idénticos.
"""

from __future__ import annotations

import sys
from pathlib import Path

FIG_DIR = Path(__file__).resolve().parent
REPO = FIG_DIR.parents[2]

sys.path.insert(0, str(REPO / "data" / "experiment" / "esq" / "code"))

import prompt_congelado  # noqa: E402  — su import corre los candados sellados
import prompt_esq3b      # noqa: E402  — matriz retocada (fuente de la derivación)
import schema            # noqa: E402  — esquema de partida (grafo_v2/code, vía cadena)

# ========================================================================== #
# Matrices fuente + ASSERTS contra los conteos sellados                      #
# ========================================================================== #

DR_F1 = schema.DOMAIN_RANGE
DR_F1B = prompt_congelado.DOMAIN_RANGE_CONGELADO

TIPOS_F1 = tuple(schema.ENTITY_TYPES)
TIPOS_F1B = tuple(prompt_congelado.ENTITY_TYPES_CONGELADO)

assert len(DR_F1) == 12, f"F1: se esperaban 12 firmas, hay {len(DR_F1)}"
assert len(DR_F1B) == 13, f"F1b: se esperaban 13 firmas, hay {len(DR_F1B)}"
assert len(TIPOS_F1) == 6, f"F1: se esperaban 6 tipos, hay {len(TIPOS_F1)}"
assert len(TIPOS_F1B) == 9, f"F1b: se esperaban 9 tipos, hay {len(TIPOS_F1B)}"
assert set(TIPOS_F1B) == set(TIPOS_F1) | {"Potestad", "Condicion", "Definicion"}

# La matriz congelada ES la retocada sin exceptua_operacion (vínculo con
# prompt_esq3b.py, la fuente donde la matriz retocada vive como literal).
_derivada = {p: (set(d), set(r))
             for p, (d, r) in prompt_esq3b.DOMAIN_RANGE_RETOCADO.items()
             if p != "exceptua_operacion"}
assert DR_F1B == _derivada, (
    "DOMAIN_RANGE_CONGELADO no coincide con DOMAIN_RANGE_RETOCADO menos "
    "exceptua_operacion — la cadena sellada cambió, se frena")


def expandir(dr: dict) -> list[tuple[str, str, str]]:
    """Pares (predicado, tipo del dominio, tipo del rango), ordenados."""
    return sorted((p, d, r)
                  for p, (dom, ran) in dr.items()
                  for d in sorted(dom) for r in sorted(ran))


FLECHAS_F1 = expandir(DR_F1)
FLECHAS_F1B = expandir(DR_F1B)
assert len(FLECHAS_F1) == 17, f"F1: 17 flechas esperadas, hay {len(FLECHAS_F1)}"
assert len(FLECHAS_F1B) == 26, f"F1b: 26 flechas esperadas, hay {len(FLECHAS_F1B)}"

NUEVAS_F1B = sorted(set(FLECHAS_F1B) - set(FLECHAS_F1))
assert len(NUEVAS_F1B) == 9, f"F1b: 9 flechas nuevas esperadas, hay {len(NUEVAS_F1B)}"
assert set(FLECHAS_F1) <= set(FLECHAS_F1B), "F1b debe contener todas las flechas de F1"

TIPOS_NUEVOS = ("Potestad", "Condicion", "Definicion")

# ========================================================================== #
# Estilo (paleta por tipo heredada de generar_figura_norma_a_grafo.py)       #
# ========================================================================== #

TIPO_SANS = "Helvetica,Arial,sans-serif"
TIPO_MONO = "Menlo,Consolas,'Courier New',monospace"

COLOR_TIPO = {
    "Excepcion": "#e07b39",
    "Restriccion": "#b23a48",
    "Obligacion": "#2a6f97",
    "Operacion": "#52796f",
    "Sujeto": "#6d597a",
    "TextoOrdenado": "#3d3d3d",
    "Comunicacion": "#6c584c",   # tipo ausente de la paleta heredada
}
RESALTE = "#b5179e"              # «agregado en la validación» (no colisiona
                                 # con ningún color de tipo de la paleta)
GRIS_ARISTA = "#8a8a8a"
GRIS_ROTULO = "#6f6f6f"
FONDO_ZONA = "#f5f5f3"
BORDE_ZONA = "#d8d8d8"

FS_NODO = 19       # nombre de tipo (mono, bold)
FS_ROTULO = 15     # rótulo de relación (mono)
FS_ZONA = 15       # rótulo de zona (sans, italic)
FS_NOTA = 15       # nota bajo Sujeto (sans, italic)
FS_LEYENDA = 15    # leyenda F1b (sans)

ANCHO_ARISTA = 1.6
ANCHO_RESALTE = 2.6

W = 850            # ancho de ambos SVG
CAJA_W, CAJA_H = 190, 46


def hex_mix(color: str, blanco: float) -> str:
    """Mezcla `color` con blanco (0..1) para el relleno claro de las cajas."""
    r, g, b = (int(color[i:i + 2], 16) for i in (1, 3, 5))
    m = [round(c + (255 - c) * blanco) for c in (r, g, b)]
    return "#{:02x}{:02x}{:02x}".format(*m)


def f(v: float) -> str:
    s = f"{v:.1f}"
    return s[:-2] if s.endswith(".0") else s


# ========================================================================== #
# Layout compartido                                                          #
# ========================================================================== #
# Columna deóntica x=90..280 (filas y=150/250/350; F1b agrega 450/550).
# Operacion x=520..710, y=330. Documental x=620..810 (TO y=60, Com y=190).
# F1b: Definicion x=620..810 y=470; Sujeto bajo la columna deóntica.

CAJAS_F1 = {
    "Obligacion": (90, 150), "Restriccion": (90, 250), "Excepcion": (90, 350),
    "Operacion": (520, 330),
    "TextoOrdenado": (620, 60), "Comunicacion": (620, 190),
    "Sujeto": (95, 470),
}
CAJAS_F1B = dict(CAJAS_F1)
CAJAS_F1B.update({
    "Potestad": (90, 450), "Condicion": (90, 550),
    "Definicion": (620, 470),
    "Sujeto": (95, 650),
})

# En F1 el rótulo de una zona puede ir en varias líneas (tupla) y llevar su
# propia x de anclaje (ROTULO_X_F1); sin entrada, va arriba a la izquierda.
ZONAS_F1 = [
    (("lo que la norma manda,", "prohíbe o exime"), 76, 106, 300, 412),
    ("acto regulado", 506, 286, 724, 390),
    ("anclaje documental", 606, 34, 824, 250),
]
ROTULO_X_F1 = {"acto regulado": 604}
ZONAS_F1B = [
    ("contenido deóntico", 76, 124, 300, 612),
    ("acto regulado", 506, 304, 724, 390),
    ("anclaje documental", 606, 34, 824, 250),
    ("contenido definitorio", 606, 444, 824, 530),
]

H_F1, H_F1B = 590, 810

INTERLINEA_ZONA = 18   # rótulos de zona en más de una línea (solo F1)
NOTA_SUJETO = {"f1": "se elige de un catálogo",
               "f1b": "catálogo cerrado (no lo emite el extractor)"}

# Troncos izquierdos (x) y puertos sobre las cajas deónticas (offset desde el
# borde superior de cada caja).
X_COND, X_EST, X_APL = 16, 40, 64
OFF_EST, OFF_COND, OFF_APL = 10, 26, 42


def corredor_f1(r: dict) -> None:
    """Las seis flechas entre Obligacion, Restriccion y Operacion en F1.

    Obligacion → Operacion: escuadras anidadas que bajan al borde SUPERIOR de
    Operacion (la que sale más arriba baja más a la derecha, y así no se
    cruzan). requiere sale de ese mismo borde, más a la derecha, y entra a
    Obligacion por arriba: dentro del borde derecho de Obligacion no queda
    lugar para un tercer rótulo. Restriccion → Operacion: escalera al borde
    IZQUIERDO (la que sale más arriba llega más arriba y gira más a la
    derecha). Las bajadas quedan a la izquierda de x = 606, donde empieza la
    zona documental.

    Rótulo (texto, x, y de base, anclaje, rotación): cada uno del lado libre
    de su flecha — arriba de la más alta, abajo de la más baja, y en la
    escalera el del medio en el hueco entre las bajadas de sus vecinas.
    """
    op = "Operacion"
    r[("requiere", op, "Obligacion")] = dict(
        pts=[(580, 330), (580, 128), (262, 128), (262, 150)], head="down",
        label=("requiere", 421, 120, "middle", 0))
    r[("regula", "Obligacion", op)] = dict(
        pts=[(280, 162), (555, 162), (555, 330)], head="down",
        label=("regula", 418, 154, "middle", 0))
    r[("condiciona", "Obligacion", op)] = dict(
        pts=[(280, 186), (530, 186), (530, 330)], head="down",
        label=("condiciona", 405, 202, "middle", 0))
    r[("regula", "Restriccion", op)] = dict(
        pts=[(280, 256), (490, 256), (490, 338), (520, 338)], head="right",
        label=("regula", 385, 248, "middle", 0))
    r[("prohibe", "Restriccion", op)] = dict(
        pts=[(280, 273), (420, 273), (420, 353), (520, 353)], head="right",
        label=("prohibe", 375, 289, "middle", 0))
    r[("limita", "Restriccion", op)] = dict(
        pts=[(280, 290), (330, 290), (330, 368), (520, 368)], head="right",
        label=("limita", 425, 384, "middle", 0))


def rotulos_f1(r: dict) -> None:
    """Versión 3 de F1: los tres textos que tocaban un trazo o una caja.

    - referencia / modificada_por: las dos bajadas se separan (x = 636 y
      x = 790) y cada rótulo va del lado de adentro de su propia bajada, uno
      arriba del otro; antes el rótulo de modificada_por, a la izquierda de su
      línea, quedaba atravesado por la de referencia.
    - establecida_en desde Operacion: el tramo horizontal (122 px) es más
      corto que el rótulo (126 px), que se montaba sobre la caja y sobre su
      propio tramo vertical; pasa a la izquierda del tramo vertical, en la
      franja libre entre la zona documental y la de acto regulado.
    - aplica_a (rotado): la línea de base se corre 4 px a la izquierda para
      que el halo no pise su tronco.
    """
    r[("referencia", "TextoOrdenado", "Comunicacion")] = dict(
        pts=[(636, 106), (636, 190)], head="down",
        label=("referencia", 642, 136, "start", 0))
    r[("modificada_por", "TextoOrdenado", "Comunicacion")] = dict(
        pts=[(790, 106), (790, 190)], head="down",
        label=("modificada_por", 784, 170, "end", 0))
    r[("establecida_en", "Operacion", "TextoOrdenado")]["label"] = (
        "establecida_en", 826, 273, "end", 0)
    k_apl = next(k for k, s in r.items() if k[0] == "aplica_a" and s["label"])
    s, _x, y_l, anchor, rot = r[k_apl]["label"]
    r[k_apl]["label"] = (s, 56, y_l, anchor, rot)


def rutas_figura(fig: str) -> dict[tuple[str, str, str], dict]:
    """Geometría de cada flecha (predicado, dominio, rango) → spec de dibujo.

    spec: pts (polilínea), head ('up'/'down'/'left'/'right' o None si la punta
    la porta otro tramo del mismo tronco), label opcional
    (texto, x, y, anchor, rot) — el rótulo es único por tronco/acceso.
    """
    cajas = CAJAS_F1 if fig == "f1" else CAJAS_F1B
    y = {n: xy[1] for n, xy in cajas.items()}
    r: dict[tuple[str, str, str], dict] = {}

    # --- establecida_en: comb izquierdo (deónticos) + acceso derecho -------
    doms_izq = [d for d in ("Obligacion", "Restriccion", "Excepcion",
                            "Potestad", "Condicion") if d in cajas]
    y_teeth = [y[d] + OFF_EST for d in doms_izq]
    y_max = max(y_teeth)
    for i, d in enumerate(doms_izq):
        yt = y[d] + OFF_EST
        pts = [(90, yt), (X_EST, yt)]
        if i == 0:  # el primer diente porta tronco + horizontal + cabeza
            pts += [(X_EST, 83), (620, 83)]
            head, label = "right", ("establecida_en", 330, 76, "middle", 0)
        else:
            head, label = None, None
        r[("establecida_en", d, "TextoOrdenado")] = dict(
            pts=pts, head=head, label=label, tronco=[(X_EST, 83), (X_EST, y_max)])
    # acceso derecho: Operacion (+ Definicion en F1b, diente resaltado)
    y_der = 483 if fig == "f1b" else 340
    r[("establecida_en", "Operacion", "TextoOrdenado")] = dict(
        pts=[(710, 340), (832, 340), (832, 83), (810, 83)], head="left",
        label=("establecida_en", 771, 332, "middle", 0))
    if fig == "f1b":
        r[("establecida_en", "Definicion", "TextoOrdenado")] = dict(
            pts=[(810, 483), (832, 483)], head=None, label=None,
            tronco=[(832, 340), (832, y_der)])

    # --- referencia / modificada_por (documental, verticales) --------------
    r[("referencia", "TextoOrdenado", "Comunicacion")] = dict(
        pts=[(700, 106), (700, 190)], head="down",
        label=("referencia", 692, 145, "end", 0))
    r[("modificada_por", "TextoOrdenado", "Comunicacion")] = dict(
        pts=[(785, 106), (785, 190)], head="down",
        label=("modificada_por", 777, 175, "end", 0))

    # --- aplica_a: comb izquierdo → Sujeto (+ acceso desde Operacion) ------
    y_suj = y["Sujeto"]
    dr = DR_F1 if fig == "f1" else DR_F1B
    doms_apl = [d for d in ("Obligacion", "Restriccion", "Excepcion", "Potestad")
                if d in dr["aplica_a"][0]]
    y_lbl = 430 if fig == "f1" else 642
    for i, d in enumerate(doms_apl):
        yt = y[d] + OFF_APL
        # dientes desde el borde IZQUIERDO (x=90) hacia el tronco x=64
        pts = [(90, yt), (X_APL, yt)]
        if i == 0:
            pts += [(X_APL, y_suj + 22), (95, y_suj + 22)]
            head = "right"
            label = ("aplica_a", 60, y_lbl, "middle", -90)
        else:
            head, label = None, None
        r[("aplica_a", d, "Sujeto")] = dict(
            pts=pts, head=head, label=label,
            tronco=[(X_APL, min(y[dd] + OFF_APL for dd in doms_apl)),
                    (X_APL, y_suj + 22)])
    if fig == "f1b":
        r[("aplica_a", "Operacion", "Sujeto")] = dict(
            pts=[(545, 376), (545, y_suj + 14), (285, y_suj + 14)], head="left",
            label=("aplica_a", 538, 630, "end", 0))

    # --- ejecuta: Sujeto → Operacion ---------------------------------------
    y_ej = y_suj + 34
    r[("ejecuta", "Sujeto", "Operacion")] = dict(
        pts=[(285, y_ej), (615, y_ej), (615, 376)], head="up",
        label=("ejecuta", 330, y_ej + 16, "start", 0))

    # --- corredor deóntico → Operacion (diagonales) ------------------------
    def diag(pred, d, p0, p1, t, dy=-7):
        lx = p0[0] + (p1[0] - p0[0]) * t
        ly = p0[1] + (p1[1] - p0[1]) * t + dy
        r[(pred, d, r_ran)] = dict(pts=[p0, p1], head="right",
                                   label=(pred, lx, ly, "middle", 0))

    r_ran = "Operacion"
    if fig == "f1":
        corredor_f1(r)
    else:
        diag("regula", "Obligacion", (280, 166), (520, 337), 0.32)
        diag("condiciona", "Obligacion", (280, 178), (520, 346), 0.62)
        diag("regula", "Restriccion", (280, 258), (520, 355), 0.28)
        diag("prohibe", "Restriccion", (280, 270), (520, 364), 0.55)
        diag("limita", "Restriccion", (280, 282), (520, 373), 0.78)
        # requiere: Operacion → Obligacion (sentido inverso, línea superior)
        r[("requiere", "Operacion", "Obligacion")] = dict(
            pts=[(590, 330), (280, 156)], head="left",
            label=("requiere", 544, 297, "middle", 0))

    # --- exceptua / exceptua_obligacion ------------------------------------
    r[("exceptua", "Excepcion", "Restriccion")] = dict(
        pts=[(250, 350), (250, 296)], head="up",
        label=("exceptua", 244 if fig == "f1" else 242, 327, "end", 0))
    if fig == "f1":
        # Por la izquierda de Restriccion: sale del borde superior de
        # Excepcion, rodea a Restriccion y entra a Obligacion por abajo. Cruza
        # los dos dientes izquierdos de Restriccion (establecida_en y
        # aplica_a), que no forman parte del corredor hacia Operacion.
        r[("exceptua_obligacion", "Excepcion", "Obligacion")] = dict(
            pts=[(104, 350), (104, 323), (78, 323), (78, 223), (104, 223),
                 (104, 196)],
            head="up", label=("exceptua_obligacion", 110, 214, "start", 0))
    else:
        r[("exceptua_obligacion", "Excepcion", "Obligacion")] = dict(
            pts=[(280, 386), (316, 386), (316, 222), (270, 222), (270, 196)],
            head="up", label=("exceptua_obligacion", 90, 216, "start", 0))

    # --- condicion_de (solo F1b): fan-out desde Condicion ------------------
    if fig == "f1b":
        y_out = y["Condicion"] + 35
        targets = ["Excepcion", "Obligacion", "Restriccion"]
        y_min = min(y[t] + OFF_COND for t in targets)
        for i, t in enumerate(sorted(targets)):
            yt = y[t] + OFF_COND
            pts = ([(90, y_out), (X_COND, y_out), (X_COND, yt), (90, yt)]
                   if i == 0 else [(X_COND, yt), (90, yt)])
            r[("condicion_de", "Condicion", t)] = dict(
                pts=pts, head="right",
                label=(("condicion_de", 13, 480, "middle", -90) if i == 0 else None),
                tronco=[(X_COND, y_min), (X_COND, y_out)])
    if fig == "f1":
        rotulos_f1(r)
    return r


# ========================================================================== #
# Guarda geométrica de F1                                                    #
# ========================================================================== #
# Controles sobre TODA la figura (versión 3 de F1): ningún texto toca un
# trazo, una caja ni otro texto; todo rótulo de relación queda junto a su
# flecha; y los cruces entre flechas son EXACTAMENTE los declarados abajo.
# Las seis flechas del corredor Obligacion/Restriccion/Operacion no cruzan
# nada.
CORREDOR = tuple(sorted(k for k in FLECHAS_F1 if k[0] in
                        ("regula", "condiciona", "prohibe", "limita",
                         "requiere")))
assert len(CORREDOR) == 6, f"F1: 6 flechas en el corredor, hay {len(CORREDOR)}"

# Cruces declarados. Con las cajas en estas posiciones son inevitables:
# - los peines de establecida_en (sube a TextoOrdenado) y de aplica_a (baja a
#   Sujeto) salen ambos por la izquierda de la columna, y Restriccion y
#   Excepcion tienen su diente de establecida_en por debajo del primer diente
#   de aplica_a: el tronco de uno corta dientes del otro;
# - exceptua_obligacion une Excepcion (abajo) con Obligacion (arriba): por la
#   derecha cortaría las tres flechas de Restriccion a Operacion, por la
#   izquierda corta los dos dientes izquierdos de Restriccion.
CRUCES_DECLARADOS = {
    (64.0, 260.0): "tronco de aplica_a × diente establecida_en de Restriccion",
    (64.0, 360.0): "tronco de aplica_a × diente establecida_en de Excepcion",
    (78.0, 260.0): "exceptua_obligacion × diente establecida_en de Restriccion",
    (78.0, 292.0): "exceptua_obligacion × diente aplica_a de Restriccion",
}

ANCHO_MONO = 0.602     # avance de Menlo por carácter, en em
ASC, DESC = 0.76, 0.24  # alto sobre y bajo la línea de base, en em
HALO = 1.75            # mitad del stroke-width del halo de los rótulos
AIRE = 1.0             # luz mínima exigida además del halo

# Anchos AFM de Helvetica (/1000) para medir los rótulos de zona y la nota.
_AFM = dict(zip("abcdefghijklmnopqrstuvwxyz",
                (556, 556, 500, 556, 556, 278, 556, 556, 222, 222, 500, 222,
                 833, 556, 556, 556, 556, 333, 500, 278, 556, 500, 722, 500,
                 500, 500)))
_AFM.update({" ": 278, ",": 278, "(": 333, ")": 333, "á": 556, "é": 556,
             "í": 278, "ó": 556, "ú": 556})


def _ancho_sans(s: str, fs: float) -> float:
    return sum(_AFM[c] for c in s) / 1000.0 * fs


def _rect_rotulo(label) -> tuple[float, float, float, float]:
    """Caja del texto de un rótulo de relación (mono), con su rotación."""
    s, x, y, anchor, rot = label
    w = ANCHO_MONO * FS_ROTULO * len(s)
    dx0 = {"start": 0.0, "middle": -w / 2.0, "end": -w}[anchor]
    dy0, dy1 = -ASC * FS_ROTULO, DESC * FS_ROTULO
    if rot == 0:
        return (x + dx0, y + dy0, x + dx0 + w, y + dy1)
    if rot == -90:   # rotate(-90): (dx, dy) local → (x + dy, y − dx)
        return (x + dy0, y - dx0 - w, x + dy1, y - dx0)
    raise AssertionError(f"rotación no prevista: {rot}")


def _crecer(R, m):
    return (R[0] - m, R[1] - m, R[2] + m, R[3] + m)


def _largo_dentro(a, b, R) -> float:
    """Largo del segmento a-b dentro del rectángulo R (Liang-Barsky)."""
    (x0, y0), (x1, y1) = a, b
    dx, dy = x1 - x0, y1 - y0
    t0, t1 = 0.0, 1.0
    for p, q in ((-dx, x0 - R[0]), (dx, R[2] - x0),
                 (-dy, y0 - R[1]), (dy, R[3] - y0)):
        if abs(p) < 1e-12:
            if q < 0:
                return 0.0
            continue
        t = q / p
        if p < 0:
            t0 = max(t0, t)
        else:
            t1 = min(t1, t)
        if t0 > t1:
            return 0.0
    return (t1 - t0) * (dx * dx + dy * dy) ** 0.5


def _dist_punto_seg(p, a, b) -> float:
    (px, py), (ax, ay), (bx, by) = p, a, b
    vx, vy = bx - ax, by - ay
    L2 = vx * vx + vy * vy
    t = 0.0 if L2 == 0 else max(0.0, min(1.0, ((px - ax) * vx + (py - ay) * vy) / L2))
    cx, cy = ax + t * vx, ay + t * vy
    return ((px - cx) ** 2 + (py - cy) ** 2) ** 0.5


def _dist_rect_seg(R, a, b) -> float:
    if _largo_dentro(a, b, R) > 0:
        return 0.0
    def d_pr(p):
        ddx = max(R[0] - p[0], 0.0, p[0] - R[2])
        ddy = max(R[1] - p[1], 0.0, p[1] - R[3])
        return (ddx * ddx + ddy * ddy) ** 0.5
    esquinas = [(R[0], R[1]), (R[2], R[1]), (R[0], R[3]), (R[2], R[3])]
    return min([d_pr(a), d_pr(b)] + [_dist_punto_seg(c, a, b) for c in esquinas])


def _punto_cruce(a, b, c, d) -> tuple[float, float]:
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = a, b, c, d
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    assert abs(den) > 1e-12, f"trazos colineales superpuestos: {a}-{b} / {c}-{d}"
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
    return (round(x1 + t * (x2 - x1), 1), round(y1 + t * (y2 - y1), 1))


def _se_tocan(a, b, c, d) -> bool:
    """¿Los segmentos a-b y c-d se tocan o se cruzan (incluye colineales)?"""
    def o(p, q, r):
        v = (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])
        return 0 if abs(v) < 1e-9 else (1 if v > 0 else -1)

    def sobre(p, q, r):
        return (min(p[0], q[0]) - 1e-9 <= r[0] <= max(p[0], q[0]) + 1e-9 and
                min(p[1], q[1]) - 1e-9 <= r[1] <= max(p[1], q[1]) + 1e-9)
    o1, o2, o3, o4 = o(a, b, c), o(a, b, d), o(c, d, a), o(c, d, b)
    if o1 != o2 and o3 != o4:
        return True
    return ((o1 == 0 and sobre(a, b, c)) or (o2 == 0 and sobre(a, b, d)) or
            (o3 == 0 and sobre(c, d, a)) or (o4 == 0 and sobre(c, d, b)))


def verificar_geometria_f1(rutas: dict) -> dict:
    """Mide el dibujo de F1 sobre sus coordenadas y FRENA ante un defecto."""
    # Trazos: los de cada flecha y los troncos de sus peines.
    segs = []
    peine = set()
    for key in sorted(rutas):
        spec = rutas[key]
        for a, b in zip(spec["pts"], spec["pts"][1:]):
            segs.append((key, tuple(a), tuple(b)))
        if spec.get("tronco"):
            peine.add(key)
            tid = (key[0], "tronco", key[2])
            peine.add(tid)
            t = (tid, tuple(spec["tronco"][0]), tuple(spec["tronco"][1]))
            if t not in segs:
                segs.append(t)

    # 1. Cruces entre flechas distintas. Los dientes de un peine tocan su
    #    propio tronco por diseño y no cuentan.
    cruces = []
    for i in range(len(segs)):
        for j in range(i + 1, len(segs)):
            ka, a, b = segs[i]
            kb, c, d = segs[j]
            if ka == kb:
                continue
            if (ka in peine and kb in peine
                    and (ka[0], ka[2]) == (kb[0], kb[2])):
                continue
            if _se_tocan(a, b, c, d):
                cruces.append((ka, kb, _punto_cruce(a, b, c, d)))
    malos = [c for c in cruces if c[0] in CORREDOR or c[1] in CORREDOR]
    assert not malos, "F1: flechas del corredor que cruzan otra flecha:\n  " + \
        "\n  ".join(f"{m[0]} × {m[1]}" for m in malos)
    # El primer diente de cada peine repite el tronco en su polilínea: el
    # mismo cruce aparece dos veces. Se cuentan PUNTOS distintos.
    puntos: dict = {}
    for ka, kb, p in cruces:
        par = tuple(sorted((f"{ka[0]} {ka[1]}→{ka[2]}",
                            f"{kb[0]} {kb[1]}→{kb[2]}")))
        puntos.setdefault(p, set()).add(par)
    assert set(puntos) == set(CRUCES_DECLARADOS), (
        "F1: los cruces no son los declarados: sobran "
        f"{sorted(set(puntos) - set(CRUCES_DECLARADOS))}, faltan "
        f"{sorted(set(CRUCES_DECLARADOS) - set(puntos))}")

    # 2. Ningún trazo atraviesa una caja (tocar el borde es llegar o salir).
    cajas = {n: (x, y, x + CAJA_W, y + CAJA_H) for n, (x, y) in CAJAS_F1.items()}
    for key, a, b in segs:
        for n, R in cajas.items():
            dentro = _largo_dentro(a, b, _crecer(R, -1.5))
            assert dentro <= 0.5, f"F1: {key} atraviesa la caja {n} ({dentro:.1f} px)"

    # 3. Rótulos: de relación, de zona y la nota de Sujeto.
    rot = {k: _rect_rotulo(s["label"]) for k, s in rutas.items() if s["label"]}
    otros_textos = {}
    for nombre, x0, y0, x1, y1 in ZONAS_F1:
        lineas = nombre if isinstance(nombre, tuple) else (nombre,)
        xr = ROTULO_X_F1.get(lineas[0], x0 + 8)
        for i, l in enumerate(lineas):
            yb = y0 + 18 + i * INTERLINEA_ZONA
            R = (xr, yb - 0.72 * FS_ZONA, xr + _ancho_sans(l, FS_ZONA),
                 yb + 0.22 * FS_ZONA)
            assert x0 < R[0] and R[2] < x1 and y0 < R[1] and R[3] < y1, (
                f"F1: el rótulo de zona «{l}» se sale de su zona")
            otros_textos[f"zona: {l}"] = R
    sx, sy = CAJAS_F1["Sujeto"]
    wn = _ancho_sans(NOTA_SUJETO["f1"], FS_NOTA)
    yb = sy + CAJA_H + 20
    otros_textos["nota de Sujeto"] = (sx + CAJA_W / 2 - wn / 2, yb - 0.72 * FS_NOTA,
                                      sx + CAJA_W / 2 + wn / 2, yb + 0.22 * FS_NOTA)

    # Todo texto contra todo trazo, toda caja y todo otro texto.
    textos = {("rótulo",) + k: R for k, R in rot.items()}
    textos.update({("texto", n): R for n, R in otros_textos.items()})
    defectos = {}
    for t, R in sorted(textos.items()):
        Rh = _crecer(R, HALO + AIRE)
        d = []
        d += [f"trazo de {k[0]} {k[1]}→{k[2]}" for k, a, b in segs
              if _largo_dentro(a, b, Rh) > 0]
        d += [f"caja {n}" for n, C in sorted(cajas.items())
              if Rh[0] < C[2] and C[0] < Rh[2] and Rh[1] < C[3] and C[1] < Rh[3]]
        d += [f"texto {u}" for u, S in sorted(textos.items()) if u != t and
              Rh[0] < S[2] and S[0] < Rh[2] and Rh[1] < S[3] and S[1] < Rh[3]]
        if d:
            defectos[t] = sorted(set(d))
    assert not defectos, "F1: textos que tocan trazos, cajas u otros textos:\n  " + \
        "\n  ".join(f"{t}: {d}" for t, d in defectos.items())

    # 4. «Junto a su flecha»: cada rótulo de relación está a no más de
    #    JUNTO px de su propia flecha, y la flecha ajena más cercana queda al
    #    menos MARGEN_AJENA px más lejos. Un rótulo equidistante entre dos
    #    flechas no pasa. En un peine, la «flecha» del rótulo es el peine
    #    entero (dientes y tronco), porque el rótulo es uno solo.
    JUNTO, MARGEN_AJENA = 6.0, 5.0

    def grupo(k):
        return (k[0], "peine", k[2]) if k in peine else k
    cercania = {}
    for k in sorted(rot):
        R = rot[k]
        dist = {}
        for kk, a, b in segs:
            g = grupo(kk)
            dist[g] = min(dist.get(g, 1e9), _dist_rect_seg(R, a, b))
        propio = dist.pop(grupo(k))
        ajeno_k = min(dist, key=dist.get)
        assert propio <= JUNTO and dist[ajeno_k] - propio >= MARGEN_AJENA, (
            f"F1: el rótulo de {k} no queda junto a su flecha: a "
            f"{propio:.1f} px de ella y a {dist[ajeno_k]:.1f} px de {ajeno_k}")
        cercania[k] = (propio, ajeno_k, dist[ajeno_k])
    return {"cruces": puntos, "cercania": cercania,
            "n_segmentos": len(segs), "n_textos": len(textos)}


# ========================================================================== #
# Emisión SVG                                                                #
# ========================================================================== #

def cabeza(x: float, y: float, direc: str, color: str) -> str:
    d = {"right": [(x, y), (x - 9, y - 5), (x - 9, y + 5)],
         "left": [(x, y), (x + 9, y - 5), (x + 9, y + 5)],
         "up": [(x, y), (x - 5, y + 9), (x + 5, y + 9)],
         "down": [(x, y), (x - 5, y - 9), (x + 5, y - 9)]}[direc]
    pts = " ".join(f"{f(a)},{f(b)}" for a, b in d)
    return f'<polygon points="{pts}" fill="{color}"/>'


def texto(s: str, x: float, y: float, fs: int, familia: str, color: str,
          anchor: str = "start", peso: str = "normal", rot: int = 0,
          estilo: str = "", halo: bool = False) -> str:
    tr = f' transform="rotate({rot} {f(x)} {f(y)})"' if rot else ""
    extra = f' font-style="{estilo}"' if estilo else ""
    h = (' stroke="#ffffff" stroke-width="3.5" paint-order="stroke" '
         'stroke-linejoin="round"') if halo else ""
    return (f'<text x="{f(x)}" y="{f(y)}" font-size="{fs}" '
            f'font-family="{familia}" fill="{color}" text-anchor="{anchor}" '
            f'font-weight="{peso}"{extra}{h}{tr}>{s}</text>')


def dibujar(fig: str) -> str:
    cajas = CAJAS_F1 if fig == "f1" else CAJAS_F1B
    zonas = ZONAS_F1 if fig == "f1" else ZONAS_F1B
    flechas = FLECHAS_F1 if fig == "f1" else FLECHAS_F1B
    alto = H_F1 if fig == "f1" else H_F1B
    rutas = rutas_figura(fig)

    assert set(rutas.keys()) == set(flechas), (
        f"{fig}: las rutas no biyectan con la matriz — "
        f"faltan {sorted(set(flechas) - set(rutas))}, "
        f"sobran {sorted(set(rutas) - set(flechas))}")
    if fig == "f1":
        GEOMETRIA_F1.update(verificar_geometria_f1(rutas))

    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" '
           f'height="{alto}" viewBox="0 0 {W} {alto}" '
           f'font-family="{TIPO_SANS}">',
           f'<rect x="0" y="0" width="{W}" height="{alto}" fill="white"/>']

    # Zonas (fondo)
    for nombre, x0, y0, x1, y1 in zonas:
        out.append(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" '
                   f'height="{y1 - y0}" fill="{FONDO_ZONA}" '
                   f'stroke="{BORDE_ZONA}" rx="8"/>')
        lineas = nombre if isinstance(nombre, tuple) else (nombre,)
        x_rot = ROTULO_X_F1.get(lineas[0], x0 + 8) if fig == "f1" else x0 + 8
        for i, linea in enumerate(lineas):
            out.append(texto(linea, x_rot, y0 + 18 + i * INTERLINEA_ZONA,
                             FS_ZONA, TIPO_SANS, GRIS_ROTULO,
                             estilo="italic"))

    # Troncos compartidos (una vez cada uno, color base, debajo de los dientes)
    troncos: set[tuple] = set()
    for key in sorted(rutas):
        spec = rutas[key]
        t = spec.get("tronco")
        if t:
            troncos.add((tuple(t[0]), tuple(t[1]),
                         RESALTE if key[0] == "condicion_de" else GRIS_ARISTA))
    for (x0t, y0t), (x1t, y1t), col in sorted(troncos):
        wd = ANCHO_RESALTE if col == RESALTE else ANCHO_ARISTA
        out.append(f'<line x1="{f(x0t)}" y1="{f(y0t)}" x2="{f(x1t)}" '
                   f'y2="{f(y1t)}" stroke="{col}" stroke-width="{wd}"/>')

    # Flechas (cada par dominio→rango es un path con data-attrs contables)
    nuevas = set(NUEVAS_F1B) if fig == "f1b" else set()
    rotulos = []
    for key in sorted(rutas):
        pred, dom, ran = key
        spec = rutas[key]
        es_nueva = key in nuevas
        col = RESALTE if es_nueva else GRIS_ARISTA
        wd = ANCHO_RESALTE if es_nueva else ANCHO_ARISTA
        pts = spec["pts"]
        d_attr = "M " + " L ".join(f"{f(x)} {f(y)}" for x, y in pts)
        out.append(f'<path d="{d_attr}" fill="none" stroke="{col}" '
                   f'stroke-width="{wd}" data-pred="{pred}" '
                   f'data-dom="{dom}" data-ran="{ran}"/>')
        if spec["head"]:
            hx, hy = pts[-1]
            out.append(cabeza(hx, hy, spec["head"], col))
        if spec["label"]:
            s, lx, ly, anchor, rot = spec["label"]
            lcol = RESALTE if (es_nueva or (fig == "f1b" and pred == "condicion_de")) \
                else GRIS_ROTULO
            rotulos.append(texto(s, lx, ly, FS_ROTULO, TIPO_MONO, lcol,
                                 anchor=anchor, rot=rot, halo=True))

    # Cajas de tipos (encima de las flechas)
    for nombre in sorted(cajas):
        x0, y0 = cajas[nombre]
        if nombre == "Sujeto":
            out.append(f'<rect x="{x0}" y="{y0}" width="{CAJA_W}" '
                       f'height="{CAJA_H}" fill="white" '
                       f'stroke="{COLOR_TIPO["Sujeto"]}" stroke-width="2" '
                       f'stroke-dasharray="7 5" rx="6"/>')
            out.append(texto("Sujeto", x0 + CAJA_W / 2, y0 + 29, FS_NODO,
                             TIPO_MONO, "#1f1f1f", anchor="middle", peso="bold"))
            out.append(texto(NOTA_SUJETO[fig],
                             x0 + CAJA_W / 2, y0 + CAJA_H + 20, FS_NOTA,
                             TIPO_SANS, GRIS_ROTULO, anchor="middle",
                             estilo="italic"))
            continue
        es_nuevo = nombre in TIPOS_NUEVOS
        borde = RESALTE if es_nuevo else COLOR_TIPO[nombre]
        fill = hex_mix(RESALTE, 0.90) if es_nuevo else hex_mix(COLOR_TIPO[nombre], 0.88)
        wd = 2.6 if es_nuevo else 2
        out.append(f'<rect x="{x0}" y="{y0}" width="{CAJA_W}" '
                   f'height="{CAJA_H}" fill="{fill}" stroke="{borde}" '
                   f'stroke-width="{wd}" rx="6"/>')
        out.append(texto(nombre, x0 + CAJA_W / 2, y0 + 29, FS_NODO, TIPO_MONO,
                         "#1f1f1f", anchor="middle", peso="bold"))

    # Rótulos de relación al final (encima de todo, con halo blanco)
    out.extend(rotulos)

    # Leyenda (solo F1b)
    if fig == "f1b":
        ly = alto - 42
        out.append(f'<rect x="76" y="{ly}" width="26" height="18" '
                   f'fill="{hex_mix(RESALTE, 0.90)}" stroke="{RESALTE}" '
                   f'stroke-width="2.6" rx="4"/>')
        out.append(f'<line x1="112" y1="{ly + 9}" x2="152" y2="{ly + 9}" '
                   f'stroke="{RESALTE}" stroke-width="{ANCHO_RESALTE}"/>')
        out.append(cabeza(152, ly + 9, "right", RESALTE))
        out.append(texto("agregado en la validación", 164, ly + 14,
                         FS_LEYENDA, TIPO_SANS, "#1f1f1f"))
    out.append("</svg>")
    svg = "\n".join(out) + "\n"

    # --- Verificaciones sobre el marcado emitido ---------------------------
    import re
    pares = re.findall(r'data-pred="([^"]+)" data-dom="([^"]+)" '
                       r'data-ran="([^"]+)"', svg)
    assert sorted(pares) == list(flechas), (
        f"{fig}: los paths emitidos no coinciden con la matriz")
    visibles = " ".join(re.findall(r">([^<>]+)</text>", svg)).lower()
    for prohibido in (r"\bsha\b", r"\btest\b", r"\.py\b", r"\.json\b",
                      r"\bcongelado\b", r"\bretocado\b"):
        assert not re.search(prohibido, visibles), (
            f"{fig}: nombre interno «{prohibido}» en texto visible")
    return svg


GEOMETRIA_F1: dict = {}


def main() -> None:
    for fig, nombre in (("f1", "figura_esquema_partida.svg"),
                        ("f1b", "figura_esquema_congelado.svg")):
        svg = dibujar(fig)
        (FIG_DIR / nombre).write_text(svg, encoding="utf-8")
        n_flechas = len(FLECHAS_F1 if fig == "f1" else FLECHAS_F1B)
        print(f"{nombre}: {n_flechas} flechas, OK")

    g = GEOMETRIA_F1
    print()
    print(f"F1 — guarda geométrica sobre {g['n_segmentos']} trazos y "
          f"{g['n_textos']} textos: 0 textos que tocan trazo, caja u otro texto")
    print(f"  cruces entre flechas distintas: {len(g['cruces'])} puntos, "
          f"exactamente los declarados (ninguno con las 6 del corredor)")
    for p, pares in sorted(g["cruces"].items()):
        print(f"      ({p[0]:g}, {p[1]:g})  {CRUCES_DECLARADOS[p]}")
    print("  rótulos de relación: distancia a su flecha / a la flecha ajena "
          "más cercana")
    for k, (p, kk, dk) in sorted(g["cercania"].items()):
        print(f"      {k[0]:19s} {k[1]:11s}→{k[2]:13s} {p:5.1f} px  /  "
              f"{dk:5.1f} px ({kk[0]} {kk[1]}→{kk[2]})")

if __name__ == "__main__":
    main()
