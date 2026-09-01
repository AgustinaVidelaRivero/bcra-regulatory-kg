#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
leer_fichas_esq2.py — instrumento de lectura de las 75 fichas de U-ESQ-2.
Patrón de adjudicar.py (worksheet EV2) COPIADO dentro de la unidad: el
instrumento es auto-contenido, recorre fichas en el orden aleatorizado del
worksheet, GUARDA tras cada marca (temp + os.replace) y es reanudable.

Uso (desde la raíz del repo):
  python3 data/experiment/esq/code/leer_fichas_esq2.py \
      data/experiment/esq/cobertura/fichas/worksheet_fichas_esq2.json

Por ficha, las tres preguntas del pre-registro §5:
  q1 ¿representado?      1=sí completo · 2=parcial · 3=no · d=DUDA
  q2 ¿deformación?       a..g=firma (exige cita textual + qué produjo + por
                         qué no se representa sin deformar) · n=ninguna · d=DUDA
  q3 ¿omisión?           texto libre de familia · n=ninguna · d=DUDA
  o=observación · s=saltear ficha · q=guardar y salir

Checkpoint de ritmo (pre-registro §3): al completar cada tanda de 10 fichas
imprime tiempo mediano por ficha y proyección del total restante. El ajuste
de N, si hiciera falta, es POR LAUDO — esta herramienta solo mide.

La herramienta NO opina, NO muestra el origen de muestra ni disparadores
(no existen en el worksheet) y NO computa firmas ni tablas (eso es posterior
a la lectura, fuera de esta unidad).
"""
import json
import os
import sys
import textwrap
import time
from datetime import datetime

W = 100


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
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)
    os.replace(tmp, path)


def ficha_completa(ficha):
    p = ficha["preguntas"]
    q1 = p["q1_representado"]["marca"] in ("si_completo", "parcial", "no", "duda")
    f2 = p["q2_deformacion"]["firma"]
    q2 = (f2 in ("ninguna", "duda")
          or (f2 in tuple("abcdefg")
              and bool((p["q2_deformacion"]["cita_textual"] or "").strip())))
    q3 = (p["q3_omision"]["familia"] is not None
          and str(p["q3_omision"]["familia"]).strip() != "")
    return q1 and q2 and q3


def pedir(prompt, validas):
    while True:
        try:
            v = input(prompt).strip().lower()
        except EOFError:
            return "q"
        if v in validas:
            return v
        print(f"  → opción inválida (usá: {' / '.join(sorted(validas))})")


def pedir_texto(prompt, obligatorio=False):
    while True:
        try:
            v = input(prompt).strip()
        except EOFError:
            v = ""
        if v or not obligatorio:
            return v
        print("  → este campo es OBLIGATORIO (cita textual del pasaje)")


def mostrar_extraccion(ext):
    ents = ext.get("entities") or []
    rels = ext.get("relations") or []
    por_id = {e.get("local_id"): e for e in ents if isinstance(e, dict)}
    print("  ENTIDADES:")
    if not ents:
        print("    (ninguna)")
    for e in ents:
        if not isinstance(e, dict):
            print(f"    (elemento no-dict: {e!r})")
            continue
        props = e.get("properties") or {}
        ptxt = ("  props=" + json.dumps(props, ensure_ascii=False)) if props else ""
        print(f"    [{e.get('local_id')}] {e.get('type')} · punto {e.get('punto')}")
        print(wrap(f"label: {e.get('label')}", indent="        "))
        if ptxt:
            print(wrap(ptxt.strip(), indent="        "))
    print("  RELACIONES:")
    if not rels:
        print("    (ninguna)")
    for r in rels:
        if not isinstance(r, dict):
            print(f"    (elemento no-dict: {r!r})")
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
        print(f"    {r.get('predicate')} · punto {r.get('punto')}{suj}")
        print(wrap(f"{lsrc}  →  {ltgt}", indent="        "))
    om = ext.get("omisiones_no_prosa") or []
    if om:
        print("  OMISIONES NO-PROSA declaradas por el extractor:")
        for o in om:
            print(wrap(f"- {o}", indent="    "))


def checkpoint_ritmo(data, completas_sesion, t_por_ficha):
    if not t_por_ficha:
        return
    orden = sorted(t_por_ficha)
    mediana = orden[len(orden) // 2]
    total = len(data["fichas"])
    hechas = sum(1 for f in data["fichas"] if ficha_completa(f))
    restantes = total - hechas
    print("\n" + "·" * W)
    print(f"CHECKPOINT DE RITMO — tanda completada: {completas_sesion} fichas "
          f"esta sesión · mediana {mediana/60:.1f} min/ficha · restantes "
          f"{restantes} ≈ {restantes * mediana / 60:.0f} min proyectados")
    print("(si la proyección excede lo tolerable, el ajuste de N es POR LAUDO "
          "declarado — pre-registro §3)")
    print("·" * W)


def leer_ficha(ficha, path, data):
    p = ficha["preguntas"]
    print("\n" + "=" * W)
    print(f"FICHA {ficha['n']}/75 — {ficha['chunk_id']}   ·   TO: {ficha['to']}"
          f"   ·   unidad {ficha['unidad']} ({ficha['tipo_unidad']}"
          + (f", bloque {ficha['rol_bloque']}" if ficha.get("rol_bloque") else "")
          + ")")
    print(wrap(f"Título: {ficha['titulo']}"))
    print("-" * W)
    ctx = ficha["texto_fuente"].get("contexto_heredado") or []
    if ctx:
        print("CONTEXTO HEREDADO (solo contexto; la unidad de extracción es el texto propio):")
        for h in ctx:
            print(f"  [{h['tipo']} | punto {h['unidad_origen']}]")
            print(wrap(h["texto"], indent="    "))
        print("-" * W)
    if ficha["texto_fuente"].get("flags_e0"):
        fl = ficha["texto_fuente"]["flags_e0"]
        print(f"FLAGS E0 (contenido no-prosa declarado no-confiable): {fl}")
        print("-" * W)
    print("TEXTO FUENTE DE LA UNIDAD:")
    print(wrap(ficha["texto_fuente"]["texto_propio"]))
    print("-" * W)
    print("EXTRACCIÓN DE LA UNIDAD (cruda, tal como la produjo el extractor):")
    mostrar_extraccion(ficha["extraccion"])
    print("-" * W)

    if ficha["tiempos"]["inicio"] is None:
        ficha["tiempos"]["inicio"] = datetime.now().isoformat(timespec="seconds")
        guardar(path, data)
    t0 = time.time()

    # --- q1 ---
    print("\nP1. " + p["q1_representado"]["pregunta"])
    v = pedir("  marca [1=sí completo / 2=parcial / 3=no / d=duda / s=saltear / q=salir]: ",
              {"1", "2", "3", "d", "s", "q"})
    if v == "q":
        guardar(path, data)
        print("\nGuardado. Reanudá con el mismo comando.")
        sys.exit(0)
    if v == "s":
        print("  Ficha salteada (queda pendiente).")
        return None
    p["q1_representado"]["marca"] = {"1": "si_completo", "2": "parcial",
                                     "3": "no", "d": "duda"}[v]
    guardar(path, data)

    # --- q2 ---
    print("\nP2. " + p["q2_deformacion"]["pregunta"])
    print("  Firmas (lista cerrada del pre-registro §4):")
    for k, txt in data["firmas_catalogo"].items():
        print(wrap(f"{k}) {txt}", indent="    "))
    v = pedir("  marca [a-g=firma / n=ninguna / d=duda / q=salir]: ",
              set("abcdefg") | {"n", "d", "q"})
    if v == "q":
        guardar(path, data)
        sys.exit(0)
    if v == "n":
        p["q2_deformacion"]["firma"] = "ninguna"
    elif v == "d":
        p["q2_deformacion"]["firma"] = "duda"
        obs = pedir_texto("  nota de la duda (opcional): ")
        if obs:
            p["q2_deformacion"]["que_produjo"] = obs
    else:
        p["q2_deformacion"]["firma"] = v
        p["q2_deformacion"]["cita_textual"] = pedir_texto(
            "  cita TEXTUAL del pasaje (obligatoria): ", obligatorio=True)
        p["q2_deformacion"]["que_produjo"] = pedir_texto(
            "  qué produjo la extracción: ")
        p["q2_deformacion"]["por_que_no_representa"] = pedir_texto(
            "  por qué no se representa sin deformar: ")
    guardar(path, data)

    # --- q3 ---
    print("\nP3. " + p["q3_omision"]["pregunta"])
    v = pedir_texto("  familia omitida [texto libre / n=ninguna / d=duda]: ",
                    obligatorio=True)
    if v.lower() == "n":
        p["q3_omision"]["familia"] = "ninguna"
    elif v.lower() == "d":
        p["q3_omision"]["familia"] = "duda"
    else:
        p["q3_omision"]["familia"] = v
        cita = pedir_texto("  cita textual del contenido omitido (opcional): ")
        if cita:
            p["q3_omision"]["cita_textual"] = cita
    guardar(path, data)

    obs = pedir_texto("\nObservaciones de la ficha (opcional, enter para seguir): ")
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
    print(f"Worksheet: {tot} fichas · completas {tot - len(pend)} · pendientes {len(pend)}")
    if not pend:
        print("No queda nada pendiente. La lectura terminó; las marcas quedan "
              "en el worksheet para el análisis posterior (fuera de U-ESQ-2).")
        return

    completas_sesion = 0
    tiempos: list[float] = []
    for ficha in fichas:
        if ficha_completa(ficha):
            continue
        t = leer_ficha(ficha, path, data)
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
