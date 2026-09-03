"""
fichas_esq3b_v2.py — FASE (f) de U-ESQ-3b-v2 ($0): genera las fichas PAREADAS
base-vs-nueva, una por unidad corrida.

Reglas que este generador implementa (mandato de la vuelta + pre-registro v2
§4 y §5; patrón de fichas_esq3b.py, que no se toca):
  - Ficha PAREADA y AUTO-CONTENIDA: texto de la unidad (propio + contexto
    heredado marcado como contexto + flags E0 si los hay), la extracción BASE
    y la extracción NUEVA (prefijo v2), ambas CRUDAS tal como las produjo el
    extractor. El brazo base de cada unidad es el que fija el §2 del
    pre-registro v2: extracción de la VUELTA 1 para las 15 del objetivo,
    extracción de ESQ-2 para las 12 de regresión fresca — la ficha NO dice
    cuál es cuál (cegado).
  - CEGADO (entrada 10): la ficha NO trae el brazo, NO trae el retoque ni el
    grupo del §2, NO trae predicciones ni marcas previas de ninguna lectura.
    Todo eso vive en `cobertura/orden/seleccion_brazos_esq3b_v2.json` y se
    junta con las marcas recién en el análisis, posterior a la lectura.
  - Orden ALEATORIZADO con semilla declarada.
  - NADA se adjudica acá: todas las marcas nacen null. El ejecutor no
    adjudica — tampoco el cumplimiento de P1–P14.
  - q4 (§4 del pre-registro v2): por cada emisión de `requisito_de_estructura`
    en la extracción NUEVA, una entrada de adjudicación avala/objeta con marca
    null. La pregunta es neutra (correcta/incorrecta contra el texto): no
    reproduce ninguna delimitación. Es arm-agnóstica: aparece en toda ficha
    cuya extracción nueva emite el valor, sin decir el brazo.

Salida: esq3b_v2/fichas/worksheet_pareado_esq3b_v2.json
Uso:  .venv/bin/python3 -B data/experiment/esq/code/fichas_esq3b_v2.py
"""

from __future__ import annotations

import hashlib
import json
import random
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_esq3b_v2 as cc      # noqa: E402

SEMILLA_ORDEN = "20260903:orden_pareado_esq3b_v2"
SALIDA = cc.FICHAS_DIR / "worksheet_pareado_esq3b_v2.json"

NOTA_DUDA = (" DUDA es categoría propia: no cuenta para ningún lado y se "
             "lista (pre-registro §4).")

PREGUNTAS = {
    "q1_cambio": ("¿Cambió la representación de la unidad entre la extracción "
                  "BASE y la NUEVA? (si / no / duda) — si cambió, describir "
                  "qué cambió." + NOTA_DUDA),
    "q2_fidelidad": ("La extracción NUEVA respecto de la BASE, ¿mejora, "
                     "empeora o deja igual la fidelidad al texto fuente de la "
                     "unidad? (mejora / empeora / igual / duda) — con "
                     "fundamento y cita textual del pasaje en juego."
                     + NOTA_DUDA),
    "q3_migracion": ("¿Aparece contenido re-tipado en una caja que la "
                     "extracción BASE no usaba para ese contenido (p. ej. "
                     "Potestad / Condicion / Definicion), o un nodo de la "
                     "BASE reemplazado por uno de tipo distinto? Si aparece, "
                     "¿esa migración es CORRECTA o INCORRECTA contra el "
                     "texto? (no_hay / correcta / incorrecta / duda) — con "
                     "cita." + NOTA_DUDA),
    "q4_requisito_estructura": (
        "Para CADA emisión de `requisito_de_estructura` en la extracción "
        "NUEVA: contra el texto fuente de la unidad, ¿la emisión es correcta "
        "(AVALA) o incorrecta (OBJETA)? (avala / objeta / duda) — con "
        "fundamento." + NOTA_DUDA),
}

# Claves que JAMÁS pueden aparecer en una ficha (cegado). El generador lo
# verifica sobre los nombres de campo de cada ficha, a cualquier profundidad.
CLAVES_PROHIBIDAS = (
    "brazo", "objetivo", "regresion", "regresión", "retoque", "retoques",
    "origen", "origen_muestra", "disparador", "azarosa", "dirigida",
    "prediccion", "predicción", "grupo", "grupos", "q1_esq2", "q2_esq2",
    "firma", "spotcheck", "spot_check", "fallada", "falladas", "ancla",
    "anclas",
)


def _claves(obj, acc: set[str]) -> set[str]:
    if isinstance(obj, dict):
        for k, v in obj.items():
            acc.add(str(k).lower())
            _claves(v, acc)
    elif isinstance(obj, list):
        for v in obj:
            _claves(v, acc)
    return acc


def _emisiones_re(nueva: dict) -> list[dict]:
    out = []
    for e in nueva.get("entities") or []:
        if (isinstance(e, dict) and e.get("type") == "Obligacion"
                and (e.get("properties") or {}).get("tipo")
                == "requisito_de_estructura"):
            out.append({"local_id": e.get("local_id"),
                        "label": e.get("label"),
                        "marca": None, "fundamento": None, "nota_duda": None})
    return out


def main(extracciones_jsonl: Path | None = None,
         salida: Path | None = None) -> int:
    """Los dos parámetros existen SOLO para que el selftest arme fichas desde
    una corrida stub en `selftest_out/`; la corrida real usa los defaults."""
    extracciones_jsonl = extracciones_jsonl or (
        cc.EXTRACCIONES_DIR / "pareado_esq3b_v2.jsonl")
    salida = salida or SALIDA
    seleccion = json.loads(
        (cc.ORDEN_DIR / "seleccion_brazos_esq3b_v2.json"
         ).read_text(encoding="utf-8"))
    nuevas = cc.cargar_jsonl_last_wins(extracciones_jsonl)
    base_v1 = cc.cargar_jsonl_last_wins(cc.JSONL_V1)
    base_esq2 = cc.cargar_extracciones_esq2()
    chunks = {c["id"]: c for c in cc.cargar_chunks_esq2()}

    cids_obj = [u["chunk_id"] for u in seleccion["objetivo"]["unidades"]]
    cids_reg = [u["chunk_id"]
                for u in seleccion["regresion_fresca"]["unidades"]]
    base_de = {**{cid: base_v1[cid] for cid in cids_obj},
               **{cid: base_esq2[cid] for cid in cids_reg}}
    cids = cids_obj + cids_reg
    faltan = [c for c in cids if c not in nuevas or nuevas[c].get("error")]
    if faltan:
        raise RuntimeError(
            f"{len(faltan)} unidades sin extracción nueva válida: {faltan[:10]} "
            f"— las fichas se arman recién con la corrida completa")

    orden = sorted(cids)
    random.Random(SEMILLA_ORDEN).shuffle(orden)

    fichas = []
    for n, cid in enumerate(orden, start=1):
        c = chunks[cid]
        base = (base_de[cid].get("tool_input_crudo") or {})
        nueva = (nuevas[cid].get("tool_input_crudo") or {})
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
            "extraccion_base": {
                "entities": base.get("entities"),
                "relations": base.get("relations"),
                "omisiones_no_prosa": base.get("omisiones_no_prosa"),
            },
            "extraccion_nueva": {
                "entities": nueva.get("entities"),
                "relations": nueva.get("relations"),
                "omisiones_no_prosa": nueva.get("omisiones_no_prosa"),
            },
            "preguntas": {
                "q1_cambio": {"pregunta": PREGUNTAS["q1_cambio"],
                              "marca": None, "que_cambio": None,
                              "nota_duda": None},
                "q2_fidelidad": {"pregunta": PREGUNTAS["q2_fidelidad"],
                                 "marca": None, "cita_textual": None,
                                 "fundamento": None, "nota_duda": None},
                "q3_migracion": {"pregunta": PREGUNTAS["q3_migracion"],
                                 "marca": None, "cita_textual": None,
                                 "fundamento": None, "nota_duda": None},
                "q4_requisito_estructura": {
                    "pregunta": PREGUNTAS["q4_requisito_estructura"],
                    "emisiones": _emisiones_re(nueva)},
            },
            "observaciones": None,
            "tiempos": {"inicio": None, "fin": None},
        })

    import prompt_esq3b_v2 as pr2
    doc = {
        "unidad": "U-ESQ-3b-v2",
        "prerregistro_v2": "data/experiment/esq/prerregistro_esq3b_v2.md (40493c9)",
        "prerregistro_v1": "data/experiment/esq/prerregistro_esq3b.md (01bf046 + f1fe0d8)",
        "semilla_orden_lectura": SEMILLA_ORDEN,
        "regla_orden": (f"random.Random('{SEMILLA_ORDEN}').shuffle sobre los "
                        f"{len(orden)} chunk_id ordenados"),
        "prefijo_v2_sha256": pr2.PREFIJO_SHA256_V2,
        "regla_duda": ("DUDA es respuesta válida y categoría propia en todas "
                       "las preguntas (q4 incluida): no cuenta para ningún "
                       "lado y se lista (pre-registro §4). El instrumento "
                       "admite una nota libre al marcarla."),
        "observaciones_por_unidad": ("campo libre propio de cada ficha "
                                     "(patrón ESQ-2/vuelta 1)."),
        "nota_instrumento": (
            "Fichas PAREADAS base-vs-nueva. CEGADAS (entrada 10): no traen "
            "brazo, ni retoque o grupo asociado, ni predicciones, ni marcas "
            "de ninguna lectura previa. Ninguna marca viene pre-cargada; "
            "DUDA es categoría propia en todas las preguntas. La lectura usa "
            "el instrumento v2 (leer_fichas_esq3b_v2.py): entrada de textos "
            "largos (entrada 11) + DETECCIÓN DEL RENDER PEGADO (bug de "
            "pegado de la vuelta 1, arreglo prerrequisito de esta lectura): "
            "un render de ficha pegado en un campo de respuesta se descarta "
            "entero y el campo se vuelve a pedir."),
        "fichas": fichas,
    }

    salida.parent.mkdir(parents=True, exist_ok=True)
    texto = json.dumps(doc, ensure_ascii=False, indent=1)
    salida.write_text(texto, encoding="utf-8")

    # --- guardas de la fase ---
    claves = set()
    for f in fichas:
        _claves(f, claves)
    prohibidas = sorted(claves & set(CLAVES_PROHIBIDAS))
    sin_marca = all(
        all(f["preguntas"][q]["marca"] is None
            for q in ("q1_cambio", "q2_fidelidad", "q3_migracion"))
        and all(e["marca"] is None
                for e in f["preguntas"]["q4_requisito_estructura"]["emisiones"])
        for f in fichas)
    print(f"[f] fichas pareadas generadas: {len(fichas)} en {salida}")
    print(f"[f] sha256 del worksheet: "
          f"{hashlib.sha256(texto.encode('utf-8')).hexdigest()}")
    print(f"[f] todas las marcas null (nada adjudicado): {sin_marca}")
    print(f"[f] claves prohibidas presentes: {prohibidas} (esperado [])")
    if prohibidas or not sin_marca:
        return 1
    print("[PASS] fase (f): worksheet pareado v2 generado — la lectura y toda "
          "adjudicación son de la autora (leer_fichas_esq3b_v2.py)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
