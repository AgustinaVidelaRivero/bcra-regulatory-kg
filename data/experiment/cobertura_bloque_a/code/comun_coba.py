"""Comunes de U-COB-A fase A.1 — diagnóstico y diseño del bloque A.

Sin API, sin escritura fuera de `data/experiment/cobertura_bloque_a/`.
Todas las rutas se resuelven desde la ubicación de este archivo, de modo que
los scripts corren desde cualquier cwd (requisito del mandato).

Este módulo SOLO LEE `e0_lib` (zona sellada): lo importa para reproducir el
camino de lectura vigente que corrió B5.8.4, y no lo modifica.
"""
from __future__ import annotations

import sys
from collections import Counter
from dataclasses import dataclass, asdict
from pathlib import Path

AQUI = Path(__file__).resolve()
UNIDAD = AQUI.parent.parent                      # data/experiment/cobertura_bloque_a
EXPERIMENT = UNIDAD.parent                       # data/experiment
REPO = EXPERIMENT.parent.parent                  # raíz del repositorio

E0_DIR = EXPERIMENT / "reextraccion_v2" / "e0_chunking"
PDFS = EXPERIMENT / "escalado_prep" / "pdfs"
PARTICION = EXPERIMENT / "segmentacion_84" / "b584_particion" / "particion_152.json"
ADJUDICACIONES = EXPERIMENT / "segmentacion_84" / "b584_particion" / "adjudicaciones_b584.json"

sys.path.insert(0, str(E0_DIR))
import e0_lib as E0  # noqa: E402  (import tras ajustar sys.path)

# --- los diez del bloque A y los dos declarados referencia (adenda 2 §2) ---
DIEZ = ("ri_con", "ri_spi", "ri_tii", "ri_rem", "ri_chr",
        "ri_fcem", "ri_itme", "ri_pfmipyme", "ri_pscpp", "ri_pspii")
REFERENCIA = ("optico", "plandecuentas")

# --- parámetros DECLARADOS del modelo de unidad laudado (decisión 1) ---
# Frontera de bloque = "línea en blanco": salto vertical entre líneas
# consecutivas mayor que FACTOR_BLANCO veces el interlineado modal del
# documento. El modal se toma por DOCUMENTO (no por página) porque hay
# páginas de 3 líneas donde una moda por página no es estimable.
FACTOR_BLANCO = 1.5
GAP_MAX_INTERLINEADO = 40.0   # gaps mayores no informan el interlineado modal
REDONDEO_GAP = 0.5            # cuantización para la moda


def interlineado_modal(paginas) -> float:
    """Moda de los saltos verticales entre líneas consecutivas de una misma
    página, cuantizados a REDONDEO_GAP y acotados a GAP_MAX_INTERLINEADO.

    Se calcula SOLO sobre líneas de CONTENIDO (encabezado y pie ya separados
    por e0_lib). Motivo medido — defecto propio corregido en esta fase: con
    las líneas de encabezado/pie incluidas, `ri_pfmipyme` (1 página, 3 líneas
    de prosa contra 6 de aparato) daba moda 6,5 pt en vez de 12,6, el umbral
    caía a 9,75 pt y el único párrafo del documento se partía en tres
    unidades. La moda debe describir el interlineado de la prosa, no el del
    aparato de página."""
    c = Counter()
    for lineas in paginas:
        for a, b in zip(lineas, lineas[1:]):
            g = b.top - a.top
            if 0 < g <= GAP_MAX_INTERLINEADO:
                c[round(g / REDONDEO_GAP) * REDONDEO_GAP] += 1
    if not c:
        return 0.0
    return max(c.items(), key=lambda kv: (kv[1], -kv[0]))[0]


@dataclass
class Bloque:
    """Unidad candidata: bloque de prosa contiguo dentro de una página."""
    pagina: int
    offset: int          # índice del bloque dentro de la página (0-based)
    n_lineas: int
    top_inicio: float
    top_fin: float
    x0_min: float
    texto: str
    n_lineas_tabulares: int   # líneas con ≥1 frontera de columna (ngaps>0)
    viñeta_inicial: bool
    solo_mayusculas: bool
    termina_en_dos_puntos: bool
    n_chars: int


VIÑETAS = ("•", "-", "–", "—", "‒", "▪", "·")


def _es_viñeta(texto: str) -> bool:
    t = texto.lstrip()
    return bool(t) and t[0] in VIÑETAS


def bloques_de_pagina(contenido, modal: float, pagina: int,
                      factor: float = FACTOR_BLANCO) -> list[Bloque]:
    """Aplica el modelo de unidad laudado sobre el CONTENIDO de una página
    (encabezado y pie ya separados por e0_lib.separar_encabezado_pie).

    Corte mecánico único: salto vertical > `factor` × modal.
    No se fabrica numeración ni se aplica ningún criterio semántico.
    """
    if not contenido:
        return []
    umbral = factor * modal if modal > 0 else float("inf")
    grupos: list[list] = [[contenido[0]]]
    for a, b in zip(contenido, contenido[1:]):
        if (b.top - a.top) > umbral:
            grupos.append([b])
        else:
            grupos[-1].append(b)

    out: list[Bloque] = []
    for i, g in enumerate(grupos):
        texto = " ".join(l.texto.strip() for l in g).strip()
        if not texto:
            continue
        letras = [c for c in texto if c.isalpha()]
        out.append(Bloque(
            pagina=pagina,
            offset=i,
            n_lineas=len(g),
            top_inicio=round(g[0].top, 1),
            top_fin=round(g[-1].top, 1),
            x0_min=round(min(l.x0 for l in g), 1),
            texto=texto,
            n_lineas_tabulares=sum(1 for l in g if l.ngaps > 0),
            viñeta_inicial=_es_viñeta(g[0].texto),
            solo_mayusculas=bool(letras) and not any(c.islower() for c in letras),
            termina_en_dos_puntos=texto.endswith(":"),
            n_chars=len(texto),
        ))
    return out


def leer_documento(to: str, factor: float = FACTOR_BLANCO):
    """Reproduce el camino de lectura VIGENTE (el que corrió B5.8.4 sobre
    estos documentos: clasificar_paginas(marcadores_b582=True) →
    roles_para_modo_sin_raiz) y aplica el modelo de unidad en seco.

    Devuelve (paginas, roles, modal, bloques_por_pagina, descartadas_por_pagina).
    """
    pdf = PDFS / f"{to}.pdf"
    paginas = E0.extraer_lineas(pdf)
    roles = E0.clasificar_paginas(paginas, marcadores_b582=True)
    roles = E0.roles_para_modo_sin_raiz(paginas, roles)

    # 1) separar aparato de página (encabezado/pie) con el instrumento vigente
    contenidos, descartadas = {}, {}
    for i, (lineas, rol) in enumerate(zip(paginas, roles), start=1):
        if rol != E0.ROL_CUERPO:
            contenidos[i], descartadas[i] = [], []
            continue
        cont, desc, _sec = E0.separar_encabezado_pie(lineas)
        contenidos[i], descartadas[i] = cont, desc

    # 2) interlineado modal SOLO sobre contenido (ver docstring de la función)
    modal = interlineado_modal([contenidos[i] for i in sorted(contenidos)])

    # 3) modelo de unidad laudado
    bloques = {i: bloques_de_pagina(contenidos[i], modal, i, factor)
               for i in sorted(contenidos)}
    return paginas, roles, modal, bloques, descartadas


def bloque_dict(b: Bloque, con_texto: bool = False) -> dict:
    d = asdict(b)
    if not con_texto:
        d.pop("texto")
    return d
