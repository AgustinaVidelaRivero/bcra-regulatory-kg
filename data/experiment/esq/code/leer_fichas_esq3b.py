#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
leer_fichas_esq3b.py — instrumento de lectura de las fichas PAREADAS de
U-ESQ-3b. Patrón de `leer_fichas_esq2.py` copiado dentro de la unidad, con dos
cambios obligatorios:

  (e) ENTRADA DE TEXTOS LARGOS ARREGLADA (entrada 11 de la cola): todo campo de
      prosa entra por `entrada_larga.leer_texto_largo` — multilínea con
      terminador '.', ':f <ruta>' para leer un archivo, ':e' para $EDITOR, y
      ALARMA en el acto ante cualquier línea de ≥1000 bytes. En ESQ-2 se
      perdieron 35 colas de campo por el límite canónico de la terminal, en
      silencio; acá el campo deja de depender de una sola línea.
  (10) CEGADO: la ficha no muestra brazo, retoque, origen de muestra ni marca
      de ninguna lectura ajena — el worksheet directamente no los contiene.

Uso (desde la raíz del repo):
  python3 data/experiment/esq/code/leer_fichas_esq3b.py \
      data/experiment/esq/esq3b/fichas/worksheet_pareado_esq3b.json

Por ficha, tres preguntas (marcas de una tecla) y sus fundamentos en prosa:
  q1 ¿cambió?      1=sí · 2=no · d=DUDA
  q2 fidelidad     1=mejora · 2=empeora · 3=igual · d=DUDA
  q3 migración     1=no hay · 2=correcta · 3=incorrecta · d=DUDA
  s=saltear ficha · q=guardar y salir

DUDA es respuesta válida y categoría propia en las TRES preguntas (Adenda 1 §5,
`f1fe0d8`): no cuenta para ningún lado, se lista, y admite una nota libre.
Cada ficha cierra además con un campo de observaciones libre (patrón ESQ-2).

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

from entrada_larga import leer_texto_largo, pedir_opcion  # noqa: E402

W = 100

MARCAS = {
    "q1_cambio": {"1": "si", "2": "no", "d": "duda"},
    "q2_fidelidad": {"1": "mejora", "2": "empeora", "3": "igual", "d": "duda"},
    "q3_migracion": {"1": "no_hay", "2": "correcta", "3": "incorrecta",
                     "d": "duda"},
}


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
    return all(p[k]["marca"] in set(MARCAS[k].values()) for k in MARCAS)


def mostrar_extraccion(ext, titulo):
    ents = ext.get("entities") or []
    rels = ext.get("relations") or []
    por_id = {e.get("local_id"): e for e in ents if isinstance(e, dict)}
    print(f"  {titulo}")
    print("    ENTIDADES:")
    if not ents:
        print("      (ninguna)")
    for e in ents:
        if not isinstance(e, dict):
            print(f"      (elemento no-dict: {e!r})")
            continue
        props = e.get("properties") or {}
        print(f"      [{e.get('local_id')}] {e.get('type')} · punto "
              f"{e.get('punto')}")
        print(wrap(f"label: {e.get('label')}", indent="          "))
        if props:
            print(wrap("props=" + json.dumps(props, ensure_ascii=False),
                       indent="          "))
    print("    RELACIONES:")
    if not rels:
        print("      (ninguna)")
    for r in rels:
        if not isinstance(r, dict):
            print(f"      (elemento no-dict: {r!r})")
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
        print(f"      {r.get('predicate')} · punto {r.get('punto')}{suj}")
        print(wrap(f"{lsrc}  →  {ltgt}", indent="          "))
    om = ext.get("omisiones_no_prosa") or []
    if om:
        print("    OMISIONES NO-PROSA declaradas por el extractor:")
        for o in om:
            print(wrap(f"- {o}", indent="      "))


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
    print("\n" + "=" * W)
    print(f"FICHA {ficha['n']}/{total} — {ficha['chunk_id']}   ·   TO: "
          f"{ficha['to']}   ·   unidad {ficha['unidad']} "
          f"({ficha['tipo_unidad']}"
          + (f", bloque {ficha['rol_bloque']}" if ficha.get("rol_bloque") else "")
          + ")")
    print(wrap(f"Título: {ficha['titulo']}"))
    print("-" * W)
    ctx = ficha["texto_fuente"].get("contexto_heredado") or []
    if ctx:
        print("CONTEXTO HEREDADO (solo contexto; la unidad de extracción es el "
              "texto propio):")
        for h in ctx:
            print(f"  [{h['tipo']} | punto {h['unidad_origen']}]")
            print(wrap(h["texto"], indent="    "))
        print("-" * W)
    if ficha["texto_fuente"].get("flags_e0"):
        print(f"FLAGS E0 (contenido no-prosa declarado no-confiable): "
              f"{ficha['texto_fuente']['flags_e0']}")
        print("-" * W)
    print("TEXTO FUENTE DE LA UNIDAD:")
    print(wrap(ficha["texto_fuente"]["texto_propio"]))
    print("-" * W)
    print("EXTRACCIONES PAREADAS (crudas, tal como las produjo el extractor):")
    mostrar_extraccion(ficha["extraccion_vieja"], "A) EXTRACCIÓN VIEJA — esquema vigente")
    print()
    mostrar_extraccion(ficha["extraccion_nueva"], "B) EXTRACCIÓN NUEVA — esquema retocado")
    print("-" * W)

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
    print(f"Worksheet pareado: {tot} fichas · completas {tot - len(pend)} · "
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
