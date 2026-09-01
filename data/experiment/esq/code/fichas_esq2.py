"""
fichas_esq2.py — FASE (f) de U-ESQ-2 ($0): genera las 75 fichas pareadas
texto-fuente vs extracción (pre-registro §5, 2240c9c).

Reglas selladas que este generador implementa:
  - Ficha PAREADA y AUTO-CONTENIDA: texto de la unidad (propio + contexto
    heredado marcado como contexto + flags E0 si los hay) y la extracción
    CRUDA de la unidad (entities/relations/omisiones tal como las produjo el
    extractor). La salida del validador NO se incluye: sus rechazos por
    sujetos harían visible la cuarentena D5, que no se ficha ni dispara.
  - Tres preguntas (§5) con espacio de marcas, DUDA como categoría propia en
    las tres. La cita textual del pasaje es obligatoria cuando se marca una
    firma (la exige el instrumento de lectura, leer_fichas_esq2.py).
  - Orden de lectura ALEATORIZADO con semilla declarada:
    random.Random("20260901:orden_lectura").shuffle sobre los 75 chunk_id
    ordenados (patrón worksheet EV2).
  - La ficha identifica la unidad (chunk_id) pero NO su origen de muestra
    (azarosa/dirigida) ni los disparadores: el origen vive SOLO en
    orden/seleccion_muestra_esq2.json y se junta con las marcas recién en el
    análisis (post-lectura, fuera de esta unidad).
  - NADA se adjudica acá: todas las marcas nacen null.

Salida: cobertura/fichas/worksheet_fichas_esq2.json
Uso:  .venv/bin/python3 -B data/experiment/esq/code/fichas_esq2.py
"""

from __future__ import annotations

import json
import random
import sys
from datetime import datetime
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_cobertura_esq2 as cc      # noqa: E402

SEMILLA_ORDEN = "20260901:orden_lectura"

PREGUNTAS = {
    "q1_representado": ("¿El contenido normativo de la unidad está "
                        "representado en la extracción? "
                        "(si_completo / parcial / no / duda)"),
    "q2_deformacion": ("Si hay deformación: ¿qué firma (a-g)? — con cita "
                       "textual del pasaje + qué produjo la extracción + por "
                       "qué no se representa sin deformar. "
                       "(a|b|c|d|e|f|g / ninguna / duda)"),
    "q3_omision": ("Si hay omisión de contenido normativo: ¿qué familia? "
                   "(texto libre / ninguna / duda). Se lee como COTA "
                   "SUPERIOR: extracción sin E3 (pre-registro §1)."),
}

# Lista cerrada de firmas (pre-registro §4, verbatim resumido) — es el espacio
# de respuesta del instrumento, no una sugerencia por ficha.
FIRMAS = {
    "a": "re-tipado semántico (contenido en caja errónea)",
    "b": "nominalización de relaciones (relación sin firma posible convertida en entidad)",
    "c": "inconsistencia entre unidades del mismo contenido repetido (hallazgo de lectura)",
    "d": "potestades/facultades",
    "e": "hechos con valor aplastados o perdidos",
    "f": "omisiones de contenido normativo (cota superior, sin E3)",
    "g": "OTRO (descripción libre)",
}


def main() -> int:
    sel = json.loads((cc.ORDEN_DIR / "seleccion_muestra_esq2.json"
                      ).read_text(encoding="utf-8"))
    unidades = sorted(set(sel["azarosa"])
                      | {d["chunk_id"] for d in sel["dirigida"]})
    if len(unidades) != 75:
        raise RuntimeError(f"selección con {len(unidades)} unidades != 75")

    chunks = {c["id"]: c for c in cc.cargar_chunks_esq2()}
    regs: dict[str, dict] = {}
    for to in cc.TOS_ESQ2:
        regs.update(cc.cargar_jsonl_last_wins(
            cc.COBERTURA_DIR / to / f"extracciones_e1_{to}.jsonl"))

    orden = list(unidades)
    random.Random(SEMILLA_ORDEN).shuffle(orden)

    fichas = []
    for n, cid in enumerate(orden, start=1):
        c = chunks[cid]
        reg = regs[cid]
        if reg.get("error") is not None:
            raise RuntimeError(f"{cid}: unidad con error en la selección")
        ti = reg.get("tool_input_crudo") or {}
        flags = c.get("flags") or {}
        flags_e0 = None
        if flags.get("contenido_tabular") or flags.get("formula"):
            flags_e0 = {
                "contenido_tabular": bool(flags.get("contenido_tabular")),
                "formula": bool(flags.get("formula")),
                "evidencia": (flags.get("evidencia_tabular") or [])
                             + (flags.get("evidencia_formula") or []),
            }
        fichas.append({
            "n": n,
            "chunk_id": cid,
            "to": c["to"],
            "unidad": c["unidad"],
            "titulo": c["titulo"],
            "tipo_unidad": c.get("tipo"),
            "rol_bloque": c.get("rol_bloque"),
            "texto_fuente": {
                "texto_propio": c["texto"],
                "contexto_heredado": [
                    {"tipo": h["tipo"], "unidad_origen": h["unidad_origen"],
                     "texto": h["texto"]}
                    for h in (c.get("herencia") or [])
                ],
                "flags_e0": flags_e0,
            },
            "extraccion": {
                "entities": ti.get("entities"),
                "relations": ti.get("relations"),
                "omisiones_no_prosa": ti.get("omisiones_no_prosa"),
            },
            "preguntas": {
                "q1_representado": {"pregunta": PREGUNTAS["q1_representado"],
                                    "marca": None},
                "q2_deformacion": {"pregunta": PREGUNTAS["q2_deformacion"],
                                   "firma": None, "cita_textual": None,
                                   "que_produjo": None,
                                   "por_que_no_representa": None},
                "q3_omision": {"pregunta": PREGUNTAS["q3_omision"],
                               "familia": None, "cita_textual": None},
            },
            "observaciones": None,
            "tiempos": {"inicio": None, "fin": None},
        })

    doc = {
        "generado": datetime.now().isoformat(timespec="seconds"),
        "unidad": "U-ESQ-2",
        "prerregistro": "data/experiment/esq/prerregistro_esq2.md (2240c9c)",
        "semilla_orden_lectura": SEMILLA_ORDEN,
        "regla_orden": ("random.Random('20260901:orden_lectura').shuffle "
                        "sobre los 75 chunk_id ordenados"),
        "firmas_catalogo": FIRMAS,
        "nota_instrumento": ("Las fichas NO traen origen de muestra ni "
                             "disparadores (viven en orden/"
                             "seleccion_muestra_esq2.json); ninguna marca "
                             "viene pre-cargada; DUDA es categoría propia en "
                             "las tres preguntas; la cita textual es "
                             "obligatoria al marcar firma."),
        "fichas": fichas,
    }
    destino = cc.COBERTURA_DIR / "fichas"
    destino.mkdir(parents=True, exist_ok=True)
    out = destino / "worksheet_fichas_esq2.json"
    out.write_text(json.dumps(doc, ensure_ascii=False, indent=1),
                   encoding="utf-8")

    sin_marca = all(
        f["preguntas"]["q1_representado"]["marca"] is None
        and f["preguntas"]["q2_deformacion"]["firma"] is None
        and f["preguntas"]["q3_omision"]["familia"] is None
        for f in fichas)
    campos_prohibidos = any(
        "origen" in f or "disparador" in json.dumps(f, ensure_ascii=False).lower()
        for f in fichas)
    print(f"[f] fichas generadas: {len(fichas)} en {out}")
    print(f"[f] todas las marcas null (nada adjudicado): {sin_marca}")
    print(f"[f] campos de origen/disparador en fichas: {campos_prohibidos} "
          f"(esperado False)")
    print("[PASS] fase (f): worksheet generado — la lectura es de la autora "
          "(leer_fichas_esq2.py, tandas de 10-15 con checkpoint de ritmo)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
