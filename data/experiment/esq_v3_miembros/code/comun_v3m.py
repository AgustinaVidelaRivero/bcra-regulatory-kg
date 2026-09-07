"""
comun_v3m.py — U-ESQ-V3: utilidades compartidas de la unidad.

Resolución de rutas SIN absolutos embebidos: todo cuelga de la ubicación de
este archivo dentro del repo (patrón de prompt_v3_b54.py, corrección 1 del
laudo B5.4 fase 1). Los scripts de la unidad son cwd-independientes.

Solo lectura sobre artefactos ajenos: el catálogo v3 sellado se IMPORTA
(nunca se edita), los chunks de e0_dry se leen, el esquema v2 se lee.
"""

from __future__ import annotations

import json
import sys
import unicodedata
from pathlib import Path

CODE = Path(__file__).resolve().parent              # esq_v3_miembros/code
UNIDAD = CODE.parent                                # esq_v3_miembros
EXPERIMENT = UNIDAD.parent                          # data/experiment
REPO = EXPERIMENT.parents[1]                        # raíz del repo

B54_CODE = EXPERIMENT / "b54_catalogo_v3" / "code"
E0_DRY = EXPERIMENT / "escalado_prep" / "e0_dry"
ESQUEMA_V2 = EXPERIMENT / "grafo_v2" / "esquema_v2_clases.json"
ESQUEMA_V3 = UNIDAD / "esquema_v3_clases.json"


def cargar_v3():
    """Importa el módulo SELLADO del catálogo v3 (solo lectura)."""
    if str(B54_CODE) not in sys.path:
        sys.path.insert(0, str(B54_CODE))
    import prompt_v3_b54 as v3  # noqa: PLC0415
    return v3


def esquema_v2() -> dict:
    return json.loads(ESQUEMA_V2.read_text(encoding="utf-8"))


def norm(s: str) -> str:
    """Normalización de comparación: sin acentos, minúsculas, sin puntuación,
    espacios colapsados."""
    s = unicodedata.normalize("NFD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    s = "".join(c if c.isalnum() or c.isspace() else " " for c in s)
    return " ".join(s.split())


def singular(tok: str) -> str:
    """Singularización mínima del castellano (solo para comparar)."""
    if len(tok) > 4 and tok.endswith("es"):
        return tok[:-2]
    if len(tok) > 3 and tok.endswith("s"):
        return tok[:-1]
    return tok


def clave(s: str) -> str:
    """Clave de comparación: normalizada y singularizada token a token."""
    return " ".join(singular(t) for t in norm(s).split())


def chunk_de(cita: str) -> dict | None:
    """Devuelve el chunk de e0_dry cuyo id es `cita` (formato `<to>::<unidad>`)."""
    to = cita.split("::", 1)[0]
    p = E0_DRY / to / f"chunks_{to}.json"
    if not p.exists():
        return None
    for c in json.loads(p.read_text(encoding="utf-8")):
        if c["id"] == cita:
            return c
    return None


def catalogo_v3_index() -> dict[str, dict]:
    """id → {label, alias:[...], nivel} de las 102 entradas del bloque v3.

    Parsing del bloque sellado con el mismo criterio de perfil_e1.
    _labels_catalogo_v3 (nivel por sufijo), extendido con los alias — que
    ese consumidor descarta y el matcheo de esta unidad necesita.
    """
    v3 = cargar_v3()
    out: dict[str, dict] = {}
    for linea in v3.BLOQUE_CATALOGO_V3.split("\n"):
        if not (linea.startswith("Sujeto_") and " — " in linea):
            continue
        sid, resto = linea.split(" — ", 1)
        if "[rol del TO" in resto:
            nivel = "rol"
        elif "[instancia]" in resto:
            nivel = "instancia"
        else:
            nivel = "clase"
        alias: list[str] = []
        if " (alias: " in resto:
            cabeza, cola = resto.split(" (alias: ", 1)
            alias = [a.strip() for a in cola.rsplit(")", 1)[0].split(",")]
        else:
            cabeza = resto
        label = cabeza.replace(" [instancia]", "")
        i = label.find(" [rol del TO")
        if i != -1:
            label = label[:i]
        out[sid] = {"label": label.strip(), "alias": alias, "nivel": nivel}
    if len(out) != 102:
        raise RuntimeError(f"catálogo v3: {len(out)} entradas (esperadas 102) — se frena")
    return out
