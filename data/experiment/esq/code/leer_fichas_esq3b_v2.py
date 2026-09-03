#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
leer_fichas_esq3b_v2.py — instrumento de lectura de las fichas PAREADAS de
U-ESQ-3b-v2. Patrón de `leer_fichas_esq3b.py` copiado dentro de la vuelta
(el instrumento v1 no se toca), con los cambios del pre-registro v2 §5:

  (BUG DE PEGADO — prerrequisito de la lectura) todo campo de prosa entra por
      `entrada_larga_v2.leer_texto_largo`, que DETECTA las firmas del render
      de ficha en el texto entrante y, si un render fue pegado en un campo de
      respuesta, DESCARTA el campo entero y lo vuelve a pedir: el campo queda
      limpio o no queda. El render del instrumento se construye en
      `render_ficha()` (una función, un string), de modo que el selftest puede
      pegar un render REAL y verificar el descarte.
  (entrada 11) se mantiene la entrada de textos largos: multilínea con
      terminador '.', ':f <ruta>', ':e', alarma ante líneas de ≥1000 bytes.
  (cegado, entrada 10) la ficha no muestra brazo, retoque, origen de muestra,
      predicción ni marca previa — el worksheet directamente no los contiene.
  (q4 — §4 del pre-registro v2) toda emisión de `requisito_de_estructura` en
      la extracción NUEVA se adjudica avala/objeta (DUDA válida), emisión por
      emisión. La pregunta es neutra (correcta/incorrecta contra el texto):
      no reproduce ninguna delimitación.

Uso (desde la raíz del repo):
  python3 data/experiment/esq/code/leer_fichas_esq3b_v2.py \
      data/experiment/esq/esq3b_v2/fichas/worksheet_pareado_esq3b_v2.json

Por ficha, tres preguntas pareadas + la adjudicación por emisión de q4:
  q1 ¿cambió?      1=sí · 2=no · d=DUDA
  q2 fidelidad     1=mejora · 2=empeora · 3=igual · d=DUDA
  q3 migración     1=no hay · 2=correcta · 3=incorrecta · d=DUDA
  q4 (por emisión) 1=avala · 2=objeta · d=DUDA
  s=saltear ficha · q=guardar y salir

DUDA es respuesta válida y categoría propia en TODAS las preguntas: no cuenta
para ningún lado, se lista, y admite una nota libre. Cada ficha cierra con un
campo de observaciones libre (patrón ESQ-2/vuelta 1).

Guarda tras cada marca (temp + os.replace) y es reanudable. La herramienta NO
opina y NO computa tablas: la adjudicación es de la autora.
"""
import json
import os
import sys
import textwrap
import time
from datetime import datetime
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from entrada_larga_v2 import (  # noqa: E402
    W_RENDER,
    leer_texto_largo,
    pedir_opcion,
)

W = W_RENDER

MARCAS = {
    "q1_cambio": {"1": "si", "2": "no", "d": "duda"},
    "q2_fidelidad": {"1": "mejora", "2": "empeora", "3": "igual", "d": "duda"},
    "q3_migracion": {"1": "no_hay", "2": "correcta", "3": "incorrecta",
                     "d": "duda"},
}
MARCAS_Q4 = {"1": "avala", "2": "objeta", "d": "duda"}


def wrap(txt, indent="  "):
    out = []
    for para in (txt or "").splitlines():
        if not para.strip():
            out.append("")
            continue
        out.append(textwrap.fill(para, width=W, initial_indent=indent,
                                 subsequent_indent=indent))
    return "\n".join(out)


def guardar(path, data):
    tmp = str(path) + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    os.replace(tmp, path)


def ficha_completa(ficha):
    p = ficha["preguntas"]
    if not all(p[k]["marca"] in set(MARCAS[k].values()) for k in MARCAS):
        return False
    q4 = p["q4_requisito_estructura"]
    return all(e["marca"] in set(MARCAS_Q4.values()) for e in q4["emisiones"])


def _render_extraccion(lineas, ext, titulo):
    ents = ext.get("entities") or []
    rels = ext.get("relations") or []
    por_id = {e.get("local_id"): e for e in ents if isinstance(e, dict)}
    lineas.append(f"  {titulo}")
    lineas.append("    ENTIDADES:")
    if not ents:
        lineas.append("      (ninguna)")
    for e in ents:
        if not isinstance(e, dict):
            lineas.append(f"      (elemento no-dict: {e!r})")
            continue
        props = e.get("properties") or {}
        lineas.append(f"      [{e.get('local_id')}] {e.get('type')} · punto "
                      f"{e.get('punto')}")
        lineas.append(wrap(f"label: {e.get('label')}", indent="          "))
        if props:
            lineas.append(wrap("props=" + json.dumps(props, ensure_ascii=False),
                               indent="          "))
    lineas.append("    RELACIONES:")
    if not rels:
        lineas.append("      (ninguna)")
    for r in rels:
        if not isinstance(r, dict):
            lineas.append(f"      (elemento no-dict: {r!r})")
            continue
        src = por_id.get(r.get("source"), {})
        tgt = por_id.get(r.get("target"), {})
        suj = ""
        if r.get("sujeto_id"):
            suj = f" · sujeto_id={r['sujeto_id']}"
        if r.get("sujeto_propuesto"):
            suj += f" · sujeto_propuesto=«{r['sujeto_propuesto']}»"
        lsrc = src.get("label") or r.get("source") or "—"
        ltgt = tgt.get("label") or r.get("target") or "—"
        lineas.append(f"      {r.get('predicate')} · punto {r.get('punto')}{suj}")
        lineas.append(wrap(f"{lsrc}  →  {ltgt}", indent="          "))
    om = ext.get("omisiones_no_prosa") or []
    if om:
        lineas.append("    OMISIONES NO-PROSA declaradas por el extractor:")
        for o in om:
            lineas.append(wrap(f"- {o}", indent="      "))


def render_ficha(ficha, total) -> str:
    """El render COMPLETO de la ficha como un string. Es la única fuente del
    texto que se imprime, y la que el selftest del bug de pegado usa para
    pegar un render real."""
    lineas: list[str] = []
    lineas.append("=" * W)
    lineas.append(f"FICHA {ficha['n']}/{total} — {ficha['chunk_id']}   ·   "
                  f"TO: {ficha['to']}   ·   unidad {ficha['unidad']} "
                  f"({ficha['tipo_unidad']}"
                  + (f", bloque {ficha['rol_bloque']}"
                     if ficha.get("rol_bloque") else "")
                  + ")")
    lineas.append(wrap(f"Título: {ficha['titulo']}"))
    lineas.append("-" * W)
    ctx = ficha["texto_fuente"].get("contexto_heredado") or []
    if ctx:
        lineas.append("CONTEXTO HEREDADO (solo contexto; la unidad de "
                      "extracción es el texto propio):")
        for h in ctx:
            lineas.append(f"  [{h['tipo']} | punto {h['unidad_origen']}]")
            lineas.append(wrap(h["texto"], indent="    "))
        lineas.append("-" * W)
    if ficha["texto_fuente"].get("flags_e0"):
        lineas.append(f"FLAGS E0 (contenido no-prosa declarado no-confiable): "
                      f"{ficha['texto_fuente']['flags_e0']}")
        lineas.append("-" * W)
    lineas.append("TEXTO FUENTE DE LA UNIDAD:")
    lineas.append(wrap(ficha["texto_fuente"]["texto_propio"]))
    lineas.append("-" * W)
    lineas.append("EXTRACCIONES PAREADAS (crudas, tal como las produjo el "
                  "extractor):")
    _render_extraccion(lineas, ficha["extraccion_base"],
                       "A) EXTRACCIÓN BASE")
    lineas.append("")
    _render_extraccion(lineas, ficha["extraccion_nueva"],
                       "B) EXTRACCIÓN NUEVA")
    lineas.append("-" * W)
    return "\n".join(lineas)


def checkpoint_ritmo(data, completas_sesion, t_por_ficha):
    if not t_por_ficha:
        return
    orden = sorted(t_por_ficha)
    mediana = orden[len(orden) // 2]
    total = len(data["fichas"])
    hechas = sum(1 for f in data["fichas"] if ficha_completa(f))
    restantes = total - hechas
    print("\n" + "·" * W)
    print(f"CHECKPOINT DE RITMO — {completas_sesion} fichas esta sesión · "
          f"mediana {mediana/60:.1f} min/ficha · restantes {restantes} ≈ "
          f"{restantes * mediana / 60:.0f} min proyectados")
    print("·" * W)


def leer_ficha(ficha, path, data, total):
    p = ficha["preguntas"]
    print("\n" + render_ficha(ficha, total))

    if ficha["tiempos"]["inicio"] is None:
        ficha["tiempos"]["inicio"] = datetime.now().isoformat(timespec="seconds")
        guardar(path, data)
    t0 = time.time()

    # --- q1 ---
    print("\nP1. " + p["q1_cambio"]["pregunta"])
    v = pedir_opcion("  marca [1=sí / 2=no / d=duda / s=saltear / q=salir]: ",
                     {"1", "2", "d", "s", "q"})
    if v == "q":
        guardar(path, data)
        print("\nGuardado. Reanudá con el mismo comando.")
        sys.exit(0)
    if v == "s":
        print("  Ficha salteada (queda pendiente).")
        return None
    p["q1_cambio"]["marca"] = MARCAS["q1_cambio"][v]
    if v == "d":
        p["q1_cambio"]["nota_duda"] = leer_texto_largo(
            "  nota de la DUDA (opcional; la duda no cuenta para ningún lado, "
            "se lista):").texto or None
    elif v != "2":
        p["q1_cambio"]["que_cambio"] = leer_texto_largo(
            "  qué cambió:").texto
    guardar(path, data)

    # --- q2 ---
    print("\nP2. " + p["q2_fidelidad"]["pregunta"])
    v = pedir_opcion("  marca [1=mejora / 2=empeora / 3=igual / d=duda / "
                     "q=salir]: ", {"1", "2", "3", "d", "q"})
    if v == "q":
        guardar(path, data)
        sys.exit(0)
    p["q2_fidelidad"]["marca"] = MARCAS["q2_fidelidad"][v]
    if v == "d":
        p["q2_fidelidad"]["nota_duda"] = leer_texto_largo(
            "  nota de la DUDA (opcional; la duda no cuenta para ningún lado, "
            "se lista):").texto or None
    else:
        if v in ("1", "2"):
            p["q2_fidelidad"]["cita_textual"] = leer_texto_largo(
                "  cita TEXTUAL del pasaje en juego (obligatoria):",
                obligatorio=True).texto
        p["q2_fidelidad"]["fundamento"] = leer_texto_largo(
            "  fundamento:").texto
    guardar(path, data)

    # --- q3 ---
    print("\nP3. " + p["q3_migracion"]["pregunta"])
    v = pedir_opcion("  marca [1=no hay / 2=correcta / 3=incorrecta / d=duda / "
                     "q=salir]: ", {"1", "2", "3", "d", "q"})
    if v == "q":
        guardar(path, data)
        sys.exit(0)
    p["q3_migracion"]["marca"] = MARCAS["q3_migracion"][v]
    if v == "d":
        p["q3_migracion"]["nota_duda"] = leer_texto_largo(
            "  nota de la DUDA (opcional; la duda no cuenta para ningún lado, "
            "se lista):").texto or None
    elif v in ("2", "3"):
        p["q3_migracion"]["cita_textual"] = leer_texto_largo(
            "  cita TEXTUAL del pasaje en juego (obligatoria):",
            obligatorio=True).texto
        p["q3_migracion"]["fundamento"] = leer_texto_largo(
            "  por qué la migración es correcta / incorrecta:").texto
    guardar(path, data)

    # --- q4: adjudicación por emisión de requisito_de_estructura ---
    q4 = p["q4_requisito_estructura"]
    if q4["emisiones"]:
        print("\nP4. " + q4["pregunta"])
        for e in q4["emisiones"]:
            if e["marca"] is not None:
                continue
            print(wrap(f"emisión [{e['local_id']}]: {e['label']}",
                       indent="  "))
            v = pedir_opcion("  marca [1=avala / 2=objeta / d=duda / "
                             "q=salir]: ", {"1", "2", "d", "q"})
            if v == "q":
                guardar(path, data)
                sys.exit(0)
            e["marca"] = MARCAS_Q4[v]
            if v == "d":
                e["nota_duda"] = leer_texto_largo(
                    "  nota de la DUDA (opcional):").texto or None
            else:
                e["fundamento"] = leer_texto_largo(
                    "  fundamento (contra el texto fuente):").texto
            guardar(path, data)

    obs = leer_texto_largo("\nObservaciones de la ficha (opcional):").texto
    if obs:
        prev = ficha.get("observaciones")
        ficha["observaciones"] = (prev + " | " + obs) if prev else obs
    ficha["tiempos"]["fin"] = datetime.now().isoformat(timespec="seconds")
    guardar(path, data)
    print(f"Ficha {ficha['n']} completa.")
    return time.time() - t0


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    path = sys.argv[1]
    data = json.load(open(path, encoding="utf-8"))
    fichas = data["fichas"]
    tot = len(fichas)

    pend = [f for f in fichas if not ficha_completa(f)]
    print(f"Worksheet pareado v2: {tot} fichas · completas {tot - len(pend)} · "
          f"pendientes {len(pend)}")
    if not pend:
        print("No queda nada pendiente. Las marcas quedan en el worksheet para "
              "la adjudicación por retoque, posterior a la lectura.")
        return

    completas_sesion = 0
    tiempos: list[float] = []
    for ficha in fichas:
        if ficha_completa(ficha):
            continue
        t = leer_ficha(ficha, path, data, tot)
        if t is not None:
            completas_sesion += 1
            tiempos.append(t)
            if completas_sesion % 10 == 0:
                checkpoint_ritmo(data, completas_sesion, tiempos)

    pend = [f["n"] for f in fichas if not ficha_completa(f)]
    print("\n" + "=" * W)
    print(f"RESUMEN: fichas pendientes: {pend if pend else 'ninguna'}")


if __name__ == "__main__":
    main()
