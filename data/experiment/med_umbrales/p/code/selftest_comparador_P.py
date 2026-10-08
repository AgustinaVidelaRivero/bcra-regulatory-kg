"""
selftest_comparador_P.py — U-MED-UMBRALES, etapa P, tramo P-a, puntos 7 y 8: casos sintéticos del formulario y del
comparador del paso 2, y una ficha inventada (no del marco) para probar el formato. No lee el grafo ni ningún insumo.

  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B selftest_comparador_P.py [--ejemplo SALIDA.md]
Corre sobre una copia (CLAUDE.md §4.l). Sale con 1 si algún caso falla.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comparador_paso2_P as K  # noqa: E402
import formulario_P as F  # noqa: E402

ID_INVENTADO = "Condicion_ficha_inventada_para_probar_el_formato_000000#u0"
NODOS = {"Definicion_importe_de_referencia_abc123": {"type": "Definicion",
                                                    "properties": {"termino": "Importe de referencia"}}}


def llenar(bloque: str, valores: dict) -> str:
    lin = []
    for x in bloque.splitlines():
        for c, v in valores.items():
            if x.startswith(f"- {c} ["):
                x = x.replace(F.VACIO, v)
        lin.append(x)
    return "\n".join(lin) + "\n"


def caso(nombre, el, valores, esperado_campos, marcas=None, sin_llenar=None):
    b = llenar(F.bloque("L9-01", ID_INVENTADO, False), valores)
    leido = F.leer(b)[ID_INVENTADO]["campos"]
    r = K.comparar(el, leido, NODOS)
    obtenido = sorted(d["campo"] for d in r["diferencias"])
    ok = obtenido == sorted(esperado_campos)
    if marcas is not None:
        ok = ok and set(r["marcas"]) == set(marcas)
    if sin_llenar is not None:
        ok = ok and r["sin_llenar"] == sin_llenar
    return nombre, ok, obtenido, r


TODO = {"pertinencia": "pertinente", "valor": "2", "unidad": "veces", "moneda": "no aplica", "tipo_de_dias": "no aplica",
        "comparacion": "minimo_estricto", "palabras_de_la_comparacion": "superen",
        "base": "importe de referencia establecido en el punto 3.7", "destino_de_la_base": "cla::3.7",
        "no_decidible": "no", "nota": "-", "hora_inicio": "10:00", "hora_fin": "10:02"}
EL = {"valor": "2", "unidad": "veces", "comparacion": "minimo_estricto",
      "base": "importe de referencia establecido en el punto 3.7", "base_destino": "cla::3.7", "base_via": "remision"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ejemplo", type=Path)
    a = ap.parse_args()
    C = []
    C.append(caso("igual en todo (el caso de control de L-ESQ-R2)", EL, TODO, [], marcas=[], sin_llenar=[]))
    C.append(caso("valor 2 contra 2.0 (Decimal)", EL, {**TODO, "valor": "2.0"}, []))
    C.append(caso("valor distinto", EL, {**TODO, "valor": "3"}, ["valor"]))
    C.append(caso("valor no numérico", EL, {**TODO, "valor": "dos"}, ["valor"]))
    C.append(caso("estricto contra inclusivo", EL, {**TODO, "comparacion": "minimo_inclusivo"}, ["comparacion"]))
    n, ok, ob, r = caso("grafo no_determinada, lectura con sentido: candidata a omitida",
                        {**EL, "comparacion": "no_determinada"}, TODO, ["comparacion"])
    C.append((n, ok and r["diferencias"][0].get("candidata", "").startswith("omitida"), ob, r))
    C.append(caso("comparación escrita con espacio y tilde", EL, {**TODO, "comparacion": "mínimo estricto"}, []))
    C.append(caso("base con artículo inicial y conjunción final", EL,
                  {**TODO, "base": "el importe de referencia establecido en el punto 3.7 y"}, []))
    C.append(caso("base con mayúsculas y tildes", EL, {**TODO, "base": "Importe de Referencia establecido en el punto 3.7"}, []))
    C.append(caso("base distinta (parcial)", EL, {**TODO, "base": "importe de referencia"}, ["base"]))
    C.append(caso("sin base contra base", EL, {**TODO, "base": "sin base"}, ["base"]))
    C.append(caso("sin base contra sin base", {k: v for k, v in EL.items() if k not in ("base", "base_destino", "base_via")},
                  {**TODO, "base": "sin base", "destino_de_la_base": "no aplica"}, []))
    C.append(caso("destino distinto", EL, {**TODO, "destino_de_la_base": "cla::3.6"}, ["destino_de_la_base"]))
    C.append(caso("destino por definición", {**EL, "base_destino": "Definicion_importe_de_referencia_abc123",
                                             "base_via": "definicion"},
                  {**TODO, "destino_de_la_base": "definicion: importe de referencia"}, []))
    C.append(caso("unidad años contra anios", {**EL, "unidad": "anios", "base": None, "base_destino": None},
                  {**TODO, "unidad": "años", "base": "sin base", "destino_de_la_base": "no aplica"}, []))
    C.append(caso("horas sin la marca fuera_de_lista", {**EL, "unidad": "horas", "base": None, "base_destino": None},
                  {**TODO, "unidad": "horas", "base": "sin base", "destino_de_la_base": "no aplica"},
                  ["unidad (marca fuera_de_lista)"]))
    C.append(caso("horas con la marca", {**EL, "unidad": "horas", "fuera_de_lista": ["unidad"], "base": None,
                                         "base_destino": None},
                  {**TODO, "unidad": "horas", "base": "sin base", "destino_de_la_base": "no aplica"}, []))
    C.append(caso("moneda USD contra ARS", {**EL, "unidad": "moneda", "moneda": "ARS"},
                  {**TODO, "unidad": "moneda", "moneda": "USD"}, ["moneda"]))
    C.append(caso("días hábiles contra corridos", {**EL, "unidad": "dias", "dias_tipo": "corridos"},
                  {**TODO, "unidad": "días", "tipo_de_dias": "hábiles"}, ["tipo_de_dias"]))
    C.append(caso("sin tipo contra vacío", {**EL, "unidad": "dias"}, {**TODO, "unidad": "dias", "tipo_de_dias": "sin tipo"}, []))
    C.append(caso("pertinencia y no decidible se marcan", EL, {**TODO, "pertinencia": "no pertinente",
                                                               "no_decidible": "sí: tabla ilegible"}, [],
                  marcas=["pertinencia", "no_decidible"]))
    sin = dict(TODO)
    sin.pop("base")
    C.append(caso("campo sin llenar: se lista y no se compara", EL, sin, [], sin_llenar=["base"]))
    # formulario: un bloque de vacío y la lectura de dos bloques
    texto = F.formulario("prueba", [("L9-01", ID_INVENTADO, False), ("L9-02", ID_INVENTADO.replace("u0", "u1"), True)])
    leido = F.leer(texto)
    C.append(("el formulario se lee: dos bloques, todos los campos sin llenar",
              len(leido) == 2 and all(v is None for b in leido.values() for v in b["campos"].values())
              and set(leido[ID_INVENTADO]["campos"]) == {c for c, _ in F.CAMPOS}
              and set(leido[ID_INVENTADO.replace("u0", "u1")]["campos"]) == {c for c, _ in F.CAMPOS_VACIO}, None, None))
    malos = 0
    for nombre, ok, ob, _ in C:
        print(("PASS" if ok else "FAIL"), "|", nombre, "|", ob if ob is not None else "")
        malos += not ok
    print(f"{len(C) - malos}/{len(C)}")
    if a.ejemplo:
        lleno = llenar(F.bloque("L9-01", ID_INVENTADO, False), TODO)
        a.ejemplo.write_text(
            "# Ficha inventada para probar el formato (no es del marco)\n\nBloque llenado como lo llenaría la autora; "
            "el selftest lo lee y lo compara con un elemento sintético igual al caso de control de L-ESQ-R2.\n\n"
            + lleno, encoding="utf-8")
    return 1 if malos else 0


if __name__ == "__main__":
    raise SystemExit(main())
