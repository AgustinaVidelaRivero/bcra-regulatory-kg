#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
adjudicar.py — llenado interactivo del worksheet de adjudicación EV2.

Uso (desde la raíz del repo):
  python3 adjudicar.py data/experiment/ev2_adjudicacion/adjudicacion/worksheet_adjudicacion.json

Comportamiento:
- Recorre las fichas en orden, salteando las ya completas (reanudable).
- Por criterio: muestra el criterio y su cita, y pide la marca.
    c = cumplido · n = no_cumplido · o = agregar/editar observación de la ficha
    a = volver al criterio anterior de la ficha · s = saltear ficha (queda pendiente)
    q = guardar y salir
- GUARDA tras cada marca (archivo temporal + os.replace: nunca deja el JSON roto).
- Al final imprime el resumen de completitud.

La herramienta NO opina, NO muestra veredictos de nadie y NO computa el
veredicto de pregunta (eso lo hace cerrar_adjudicacion.py con el mapping).
"""
import json
import os
import sys
import textwrap

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
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tmp, path)


def ficha_completa(ficha):
    return all(c.get("veredicto") in ("cumplido", "no_cumplido")
               for c in ficha["criterios"])


def pedir(prompt, validas):
    while True:
        try:
            v = input(prompt).strip().lower()
        except EOFError:
            return "q"
        if v in validas:
            return v
        print(f"  → opción inválida (usá: {' / '.join(sorted(validas))})")


def adjudicar_ficha(ficha, path, data):
    n_crit = len(ficha["criterios"])
    print("\n" + "=" * W)
    print(f"FICHA {ficha['n']} — {ficha['id_ficha']}   ·   TO: {ficha['to_nombre']} ({ficha['to']})   ·   ancla: {ficha['ancla']}")
    print("-" * W)
    print("PREGUNTA:")
    print(wrap(ficha["pregunta"]))
    print("-" * W)
    print("RESPUESTA DEL SISTEMA (completa):")
    print(wrap(ficha["respuesta"]))
    print("-" * W)

    i = 0
    while i < n_crit:
        c = ficha["criterios"][i]
        ya = f"   [marca actual: {c['veredicto']}]" if c.get("veredicto") else ""
        print(f"\nCRITERIO {c['indice']} de {n_crit}{ya}")
        print(wrap(c["criterio"]))
        print("  Cita textual del TO:")
        print(wrap("«" + c["cita_textual"] + "»", indent="    "))
        v = pedir("  marca [c=cumplido / n=no_cumplido / o=observación / a=anterior / s=saltear ficha / q=guardar y salir]: ",
                  {"c", "n", "o", "a", "s", "q"})
        if v == "q":
            guardar(path, data)
            print("\nGuardado. Podés retomar cuando quieras con el mismo comando.")
            sys.exit(0)
        if v == "s":
            print("  Ficha salteada (queda pendiente).")
            return
        if v == "a":
            i = max(0, i - 1)
            continue
        if v == "o":
            print("  Observación actual:", ficha.get("observaciones") or "(ninguna)")
            obs = input("  Nueva observación de la ficha (enter = dejar como está): ").strip()
            if obs:
                ficha["observaciones"] = obs
                guardar(path, data)
            continue
        c["veredicto"] = "cumplido" if v == "c" else "no_cumplido"
        guardar(path, data)
        i += 1

    obs = input("\nObservaciones de la ficha (opcional, enter para seguir): ").strip()
    if obs:
        prev = ficha.get("observaciones")
        ficha["observaciones"] = (prev + " | " + obs) if prev else obs
        guardar(path, data)
    print(f"Ficha {ficha['n']} completa.")


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
        print("No queda nada pendiente. Corré cerrar_adjudicacion.py.")
        return

    for ficha in fichas:
        if ficha_completa(ficha):
            continue
        adjudicar_ficha(ficha, path, data)

    pend = [f["n"] for f in fichas if not ficha_completa(f)]
    marcas = sum(1 for f in fichas for c in f["criterios"]
                 if c.get("veredicto") in ("cumplido", "no_cumplido"))
    print("\n" + "=" * W)
    print(f"RESUMEN: {marcas}/{sum(len(f['criterios']) for f in fichas)} criterios marcados; "
          f"fichas pendientes: {pend if pend else 'ninguna'}")
    if not pend:
        print("Listo: worksheet completo. Siguiente paso: cerrar_adjudicacion.py")


if __name__ == "__main__":
    main()
