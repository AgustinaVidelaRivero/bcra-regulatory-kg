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

Diseño compartido (idéntico layout en ambas figuras, para compararlas):
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

ZONAS_F1 = [
    ("contenido deóntico", 76, 124, 300, 412),
    ("acto regulado", 506, 304, 724, 390),
    ("anclaje documental", 606, 34, 824, 250),
]
ZONAS_F1B = [
    ("contenido deóntico", 76, 124, 300, 612),
    ("acto regulado", 506, 304, 724, 390),
    ("anclaje documental", 606, 34, 824, 250),
    ("contenido definitorio", 606, 444, 824, 530),
]

H_F1, H_F1B = 590, 810

# Troncos izquierdos (x) y puertos sobre las cajas deónticas (offset desde el
# borde superior de cada caja).
X_COND, X_EST, X_APL = 16, 40, 64
OFF_EST, OFF_COND, OFF_APL = 10, 26, 42


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
        label=("exceptua", 242, 327, "end", 0))
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
    return r


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

    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" '
           f'height="{alto}" viewBox="0 0 {W} {alto}" '
           f'font-family="{TIPO_SANS}">',
           f'<rect x="0" y="0" width="{W}" height="{alto}" fill="white"/>']

    # Zonas (fondo)
    for nombre, x0, y0, x1, y1 in zonas:
        out.append(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" '
                   f'height="{y1 - y0}" fill="{FONDO_ZONA}" '
                   f'stroke="{BORDE_ZONA}" rx="8"/>')
        out.append(texto(nombre, x0 + 8, y0 + 18, FS_ZONA, TIPO_SANS,
                         GRIS_ROTULO, estilo="italic"))

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
            out.append(texto("catálogo cerrado (no lo emite el extractor)",
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


def main() -> None:
    for fig, nombre in (("f1", "figura_esquema_partida.svg"),
                        ("f1b", "figura_esquema_congelado.svg")):
        svg = dibujar(fig)
        (FIG_DIR / nombre).write_text(svg, encoding="utf-8")
        n_flechas = len(FLECHAS_F1 if fig == "f1" else FLECHAS_F1B)
        print(f"{nombre}: {n_flechas} flechas, OK")


if __name__ == "__main__":
    main()
