"""
fichas_esq3b.py — FASE (f) de U-ESQ-3b ($0): genera las fichas PAREADAS
viejo-vs-nuevo, una por unidad corrida.

Reglas que este generador implementa (mandato de la unidad + pre-registro §4):
  - Ficha PAREADA y AUTO-CONTENIDA: texto de la unidad (propio + contexto
    heredado marcado como contexto + flags E0 si los hay), la extracción VIEJA
    (esquema vigente, persistida por ESQ-2) y la extracción NUEVA (esquema
    retocado), ambas CRUDAS tal como las produjo el extractor.
  - CEGADO (entrada 10 de la cola): la ficha NO trae el brazo (objetivo /
    regresión), NO trae el retoque asociado, NO trae el origen de muestra de
    ESQ-2 ni las marcas de la lectura de ESQ-2 ni ninguna otra lectura ajena.
    Todo eso vive en `cobertura/orden/seleccion_brazos_esq3b.json` y se junta
    con las marcas recién en el análisis, posterior a la lectura.
  - Orden ALEATORIZADO con semilla declarada.
  - NADA se adjudica acá: todas las marcas nacen null. El ejecutor no adjudica.

Sobre las preguntas: el cuestionario quedó APROBADO por la Adenda 1 §5
(`f1fe0d8`). Son tres, ARM-AGNÓSTICAS por diseño —la misma pregunta sirve para
una unidad del objetivo y para una de regresión, que es lo que el cegado
exige—, y cubren las dos adjudicaciones selladas: las predicciones por retoque
(§2) y la métrica de migración a caja nueva (§3). Con los dos agregados que
laudó la adenda:
  - **DUDA es respuesta válida en las TRES** y es categoría propia: no cuenta
    para ningún lado y se lista (regla del §4 del pre-registro). El
    instrumento admite una nota libre al marcar DUDA.
  - **Observaciones libres por unidad** (patrón ESQ-2), campo propio de la
    ficha.

Salida: esq3b/fichas/worksheet_pareado_esq3b.json
Uso:  .venv/bin/python3 -B data/experiment/esq/code/fichas_esq3b.py
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

import comun_esq3b as cc      # noqa: E402

SEMILLA_ORDEN = "20260902:orden_pareado_esq3b"
SALIDA = cc.FICHAS_DIR / "worksheet_pareado_esq3b.json"

NOTA_DUDA = (" DUDA es categoría propia: no cuenta para ningún lado y se "
             "lista (pre-registro §4).")

PREGUNTAS = {
    "q1_cambio": ("¿Cambió la representación de la unidad entre la extracción "
                  "VIEJA y la NUEVA? (si / no / duda) — si cambió, describir "
                  "qué cambió." + NOTA_DUDA),
    "q2_fidelidad": ("La extracción NUEVA respecto de la VIEJA, ¿mejora, "
                     "empeora o deja igual la fidelidad al texto fuente de la "
                     "unidad? (mejora / empeora / igual / duda) — con "
                     "fundamento y cita textual del pasaje en juego."
                     + NOTA_DUDA),
    "q3_migracion": ("¿Aparece contenido re-tipado en una caja NUEVA "
                     "(Potestad / Condicion / Definicion), o un nodo de la "
                     "extracción vieja reemplazado por uno de tipo nuevo? Si "
                     "aparece, ¿esa migración es CORRECTA o INCORRECTA contra "
                     "el texto? (no_hay / correcta / incorrecta / duda) — con "
                     "cita." + NOTA_DUDA),
}

# Claves que JAMÁS pueden aparecer en una ficha (cegado). El generador lo
# verifica sobre los nombres de campo de cada ficha, a cualquier profundidad.
CLAVES_PROHIBIDAS = (
    "brazo", "objetivo", "regresion", "regresión", "retoque", "retoques",
    "origen", "origen_muestra", "disparador", "azarosa", "dirigida",
    "prediccion", "predicción", "q1_esq2", "q2_esq2", "firma", "spotcheck",
    "spot_check",
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


def main(extracciones_jsonl: Path | None = None,
         salida: Path | None = None) -> int:
    """Los dos parámetros existen SOLO para que el selftest arme fichas desde
    una corrida stub en `selftest_out/`; la corrida real usa los defaults."""
    extracciones_jsonl = extracciones_jsonl or (
        cc.EXTRACCIONES_DIR / "pareado_esq3b.jsonl")
    salida = salida or SALIDA
    seleccion = json.loads(
        (cc.ORDEN_DIR / "seleccion_brazos_esq3b.json").read_text(encoding="utf-8"))
    nuevas = cc.cargar_jsonl_last_wins(extracciones_jsonl)
    viejas = cc.cargar_extracciones_esq2()
    chunks = {c["id"]: c for c in cc.cargar_chunks_esq2()}

    cids = [u["chunk_id"] for u in seleccion["objetivo"]["unidades"]] + \
           [u["chunk_id"] for u in seleccion["regresion"]["unidades"]]
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
        vieja = (viejas[cid].get("tool_input_crudo") or {})
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
            "extraccion_vieja": {
                "entities": vieja.get("entities"),
                "relations": vieja.get("relations"),
                "omisiones_no_prosa": vieja.get("omisiones_no_prosa"),
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
            },
            "observaciones": None,
            "tiempos": {"inicio": None, "fin": None},
        })

    doc = {
        "unidad": "U-ESQ-3b",
        "laudo": "data/experiment/esq/laudo_ESQ-3a_retoques.md (0a76549)",
        "prerregistro": "data/experiment/esq/prerregistro_esq3b.md (01bf046)",
        "semilla_orden_lectura": SEMILLA_ORDEN,
        "regla_orden": (f"random.Random('{SEMILLA_ORDEN}').shuffle sobre los "
                        f"{len(orden)} chunk_id ordenados"),
        "prefijo_retocado_sha256": None,  # lo completa el bloque de abajo
        "regla_duda": ("DUDA es respuesta válida y categoría propia en las "
                       "tres preguntas: no cuenta para ningún lado y se lista "
                       "(pre-registro §4; Adenda 1 §5, f1fe0d8). El "
                       "instrumento admite una nota libre al marcarla."),
        "observaciones_por_unidad": ("campo libre propio de cada ficha "
                                     "(patrón ESQ-2; Adenda 1 §5)."),
        "nota_instrumento": (
            "Fichas PAREADAS viejo-vs-nuevo. CEGADAS (entrada 10 de la cola): "
            "no traen brazo (objetivo/regresión), ni retoque asociado, ni "
            "origen de muestra, ni ninguna marca de la lectura de ESQ-2 ni de "
            "ningún tercero. Ninguna marca viene pre-cargada; DUDA es "
            "categoría propia en las tres preguntas. La entrada de textos "
            "largos usa el instrumento arreglado (entrada 11): multilínea con "
            "terminador '.', ':f <ruta>' para leer un archivo y alarma por "
            "línea de ≥1000 bytes."),
        "fichas": fichas,
    }
    import prompt_esq3b as pr
    doc["prefijo_retocado_sha256"] = pr.PREFIJO_SHA256_RETOCADO

    salida.parent.mkdir(parents=True, exist_ok=True)
    texto = json.dumps(doc, ensure_ascii=False, indent=1)
    salida.write_text(texto, encoding="utf-8")

    # --- guardas de la fase ---
    claves = set()
    for f in fichas:
        _claves(f, claves)
    prohibidas = sorted(claves & set(CLAVES_PROHIBIDAS))
    sin_marca = all(
        f["preguntas"]["q1_cambio"]["marca"] is None
        and f["preguntas"]["q2_fidelidad"]["marca"] is None
        and f["preguntas"]["q3_migracion"]["marca"] is None
        for f in fichas)
    print(f"[f] fichas pareadas generadas: {len(fichas)} en {salida}")
    print(f"[f] sha256 del worksheet: "
          f"{hashlib.sha256(texto.encode('utf-8')).hexdigest()}")
    print(f"[f] todas las marcas null (nada adjudicado): {sin_marca}")
    print(f"[f] claves prohibidas presentes: {prohibidas} (esperado [])")
    if prohibidas or not sin_marca:
        return 1
    print("[PASS] fase (f): worksheet pareado generado — la lectura y la "
          "adjudicación son de la autora (leer_fichas_esq3b.py)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
