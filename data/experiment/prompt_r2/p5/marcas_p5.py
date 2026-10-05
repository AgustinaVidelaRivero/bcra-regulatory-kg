"""
marcas_p5.py — U-PROMPT-R2, P5 (USD 0, sin API): la lectura asistida de las fichas de P5 (LECTURA, por unidad y
corrida, con su razón), con las reglas de marcado de P4b (`p4b/marcas_p4b.py`: lo que mide cada grupo), y la medición d:
por grupo, en cuántos casos cambia la marca de cada corrida contra la del brazo «p3c» de P4b (el mismo prefijo, sin
temperatura fijada), y de una corrida contra la otra. Como fracción.

Lo que mide cada grupo es lo de P4b (diseño de P3c-1, §8):
  - a: ninguna omisión `meta_normativo` con deber, prohibición, facultad, condición, excepción, alcance o modalidad, y
    ese contenido extraído con su tipo;
  - b1 (ítems): Excepcion por el miembro que queda afuera, con la norma exceptuada en la descripción, sin `exceptua`
    colgante;
  - b2 (ítems): Condicion del supuesto, con su cuantificador y la norma exceptuada en la descripción;
  - b, encabezados: Definicion de la clase (b1); la norma y la excepción unidas (b2);
  - c: una Condicion por supuesto, con label, descripción, tramo y umbral del mismo supuesto;
  - d: la norma del encabezado no se emite aparte en el ítem;
  - e: sin relación de sujeto cuando el texto no nombra al sujeto, y menciones que verifican;
  - el ejemplo: en `cla::5.1.1::intro`, la Definicion de alcance; en `cla::5.1.1.1`, la Excepcion, la Operacion de
    clasificar y una Condicion por cada condición;
  - f: ningún valor de `cap::tabla037` copiado y la omisión `tabla` declarada.
La lectura es mía y asistida; la revisa la autora. «cumple», «no_cumple» o «no_aplica» (la unidad no da el caso).
Donde las dos corridas son iguales byte a byte, la lectura es una sola y vale para las dos.

Escribe solo --salida. Uso (desde la raíz de una copia):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p5/marcas_p5.py --analisis A --salida DIR
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
MARCAS_P4B = AQUI.parent / "p4b" / "salida" / "marcas_p4b.json"
CORRIDAS = ("a", "b")
C, N, NA = "cumple", "no_cumple", "no_aplica"

# Lectura por unidad: {"a": (marca, razón), "b": (marca, razón)}; con las dos salidas iguales, la misma en las dos.
LECTURA: dict[str, dict[str, tuple[str, str]]] = {
    # a, régimen de transición
    "ext::13.1.4": {"a": (C, "el régimen de transición, extraído: la Condicion «hasta el 12/12/23» de la Obligacion de "
                             "verificar el encuadre en 13.4, y la Potestad de suscribir BOPREAL con su Condicion; sin "
                             "omisión meta_normativo"),
                    "b": (N, "el régimen extraído igual, pero registra como meta_normativo el cierre heredado de 13.1 "
                             "(«quedan sujetos a la conformidad previa del BCRA»), un deber")},
    # a
    "ext::6.1.1": {"a": (C, "Definicion de lo que la clase comprende; sin omisión"),
                   "b": (C, "Definicion de lo que la clase comprende; sin omisión")},
    "cap::10.3.3.1": {"a": (N, "registra «De lo contrario, será de aplicación lo siguiente» como meta_normativo, que lleva "
                               "la condición del régimen alternativo (lectura dudosa: el resto anuncia la lista); la "
                               "Condicion «De lo contrario» va aparte, sin condicion_de"),
                      "b": (N, "registra «De lo contrario, será de aplicación lo siguiente» como meta_normativo (lectura "
                               "dudosa, como en a); la condición no se extrae")},
    "cap::11.4": {"a": (N, "registra «A los efectos de la determinación de la RPC» como meta_normativo: alcance, por la "
                           "prueba del prefijo"),
                  "b": (N, "registra «A los efectos de la determinación de la RPC» como meta_normativo, como en a")},
    # b1 (lectura dudosa de la lista: ver p4b/seleccion_p4b.md)
    "ctacte::3.2.2": {"a": (N, "Restriccion, no Excepcion; `prohibe` colgante rechazado"),
                      "b": (N, "Operacion y Restriccion, no Excepcion")},
    "ctacte::3.2.5": {"a": (N, "Restriccion, no Excepcion"),
                      "b": (N, "Condicion del supuesto y Restriccion de la clase, con `prohibe` a la Operacion; no hay "
                               "Excepcion")},
    "ctacte::3.2.4": {"a": (N, "Restriccion, no Excepcion"),
                      "b": (N, "Restriccion, no Excepcion")},
    # b2
    "ext::3.5.3.4": {"a": (N, "las Condicion no nombran la norma exceptuada; van a la Excepcion compuesta del encabezado, "
                              "que la regla deja en la unidad del encabezado (una Restriccion condicion_de la Excepcion "
                              "se rechaza por la firma)"),
                     "b": (N, "las Condicion van a la Operacion y ninguna nombra la norma exceptuada; sin Excepcion")},
    "ext::3.5.3.5": {"a": (N, "la Condicion no nombra la norma exceptuada; la nombra la Excepcion compuesta"),
                     "b": (N, "una Condicion junta el supuesto con su marco (14.2.1) y no nombra la norma exceptuada; la "
                              "nombra la Excepcion")},
    "ext::3.5.3.1": {"a": (N, "una Condicion por supuesto hacia la Operacion o la Potestad; ninguna nombra la norma "
                              "exceptuada"),
                     "b": (N, "una Condicion por supuesto hacia la Operacion o la Potestad; ninguna nombra la norma "
                              "exceptuada")},
    # b, encabezados
    "ctacte::3.2::intro": {"a": (N, "Restriccion, no Definicion de la clase"),
                           "b": (N, "Restriccion, no Definicion de la clase")},
    "ext::3.5.3::intro": {"a": (N, "la norma (como Potestad del BCRA) y la Excepcion, con `exceptua` rechazado por la "
                                   "firma; sin omisión meta_normativo"),
                          "b": (N, "la norma (como Potestad del BCRA) y la Excepcion, con `exceptua` rechazado por la "
                                   "firma; sin omisión meta_normativo")},
    # c
    "cap::5.3.1.3": {"a": (N, "las ocho de a) a h), como Condicion de la Restriccion del 0 %; el supuesto «participante "
                              "esencial» va en la Operacion, y los de ii) no son Condicion (solo b) se conecta a la del "
                              "10 %); iii), con una Condicion"),
                     "b": (N, "las ocho de a) a h); «participante esencial», ii) y iii) no son Condicion")},
    "cla::6.5.4.5": {"a": (N, "dos Condicion coherentes («las otras condiciones»); el supuesto del pago del 10 % sin "
                              "atrasos va dentro de la norma de reclasificación, con umbrales, y el del crédito adicional, "
                              "dentro de la Restriccion de permanencia"),
                     "b": (N, "dos Condicion coherentes («las otras condiciones»); el supuesto del pago del 10 % sin "
                              "atrasos va dentro de la norma de reclasificación, con umbrales, y el del crédito adicional, "
                              "dentro de la Restriccion de permanencia")},
    "ext::10.4.2.5": {"a": (N, "una Condicion junta dos supuestos (no persona humana y constituida hasta 365 días) y el "
                               "monto va como umbral del deber"),
                      "b": (N, "una Condicion junta dos supuestos (no persona humana y constituida hasta 365 días) y el "
                               "monto va como umbral del deber")},
    "ext::10.3.6": {"a": (C, "una Condicion por supuesto (documentación, desde el 13/12/23, salvo 10.10.2.11, desde el "
                             "14/04/25), coherentes y hacia su norma; el plazo más 15 días, umbral de la Obligacion que "
                             "lo exige"),
                    "b": (C, "una Condicion por supuesto (documentación, desde el 13/12/23, salvo 10.10.2.11, desde el "
                             "14/04/25), coherentes y hacia su norma; el plazo más 15 días, umbral de la Obligacion que "
                             "lo exige")},
    # d
    "ext::10.4.3.6": {"a": (C, "sin entidad aparte para la facultad del encabezado; su condición, como Condicion del ítem"),
                      "b": (C, "sin entidad aparte para la facultad del encabezado, que registra como meta_normativo")},
    "ext::4.1.4.7": {"a": (N, "emite aparte la norma del encabezado (Restriccion con el tramo solo del encabezado, "
                              "heredado_compuesto 1) y registra «cuando tales pagos se originen…» como meta_normativo"),
                     "b": (C, "una Obligacion compuesta (tramo de dos segmentos) con el contenido del ítem")},
    "polcre::2.1.15": {"a": (C, "sin entidad aparte para el deber del encabezado"),
                       "b": (C, "sin entidad aparte para el deber del encabezado, que registra como meta_normativo")},
    "cap::10.2.2.4": {"a": (N, "el deber del encabezado («deberán cumplir cada uno de los siguientes seis criterios») va "
                               "aparte, como Condicion con el tramo del encabezado, condicion_de las cuatro Obligacion "
                               "(lectura dudosa: no va como norma)"),
                      "b": (N, "el deber del encabezado va aparte, como Condicion con el tramo del encabezado, como en a "
                               "(lectura dudosa)")},
    # e
    "cap::6.3.2::intro": {"a": (N, "aplica_a «las entidades», que el texto no nombra (mención no verificada)"),
                          "b": (N, "aplica_a «los restantes derivados sobre acciones…»: verifica en el texto, pero no es "
                                   "un sujeto")},
    "cap::3.2::intro": {"a": (C, "sin relación de sujeto"),
                        "b": (N, "aplica_a «Las participaciones en fondos»: verifica en el texto, pero no es un sujeto")},
    "cap::6.3.2.1": {"a": (C, "sin relación de sujeto"),
                     "b": (N, "cinco aplica_a «las entidades», que el texto no nombra")},
    "polcre::5.3": {"a": (N, "dos aplica_a «las entidades», que el texto no nombra"),
                    "b": (N, "tres aplica_a «las entidades», que el texto no nombra")},
    # el ejemplo
    "cla::5.1.1::intro": {"a": (C, "Definicion «Cartera comercial — alcance»; «con excepción de las siguientes», como "
                                   "fuera_de_tipos"),
                          "b": (C, "Definicion «Cartera comercial — alcance»; «con excepción de las siguientes», como "
                                   "fuera_de_tipos")},
    "cla::5.1.1.1": {"a": (C, "Excepcion, Operacion de inclusión en la cartera comercial y una Condicion por cada "
                              "condición (monto y repago), hacia esa Operacion; el `exceptua` de la Excepcion a la "
                              "Operacion de los créditos se rechaza por la firma"),
                     "b": (C, "Excepcion, Operacion de inclusión en la cartera comercial y una Condicion por cada "
                              "condición (monto y repago), hacia esa Operacion; el `exceptua` se rechaza por la firma, "
                              "como en a")},
    # f
    "cap::6.2.2.6": {"a": (C, "ningún porcentaje de cap::tabla037 copiado; la omisión `tabla` declarada"),
                     "b": (C, "ningún porcentaje de cap::tabla037 copiado; la omisión `tabla` declarada")},
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--analisis", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    sal = a.salida.resolve()
    if REPO in sal.parents or sal == REPO:
        raise SystemExit("--salida no puede estar dentro del repo")
    an = json.loads(a.analisis.read_text(encoding="utf-8"))
    sel = json.loads((AQUI / "salida" / "seleccion_p5.json").read_text(encoding="utf-8"))
    p4b = json.loads(MARCAS_P4B.read_text(encoding="utf-8"))["lectura"]
    faltan = sorted(set(an["filas"]) - set(LECTURA))
    if faltan:
        raise SystemExit(f"unidades sin lectura: {faltan}")
    iguales = set(an["medicion_b"]["a_contra_b"]["unidades_iguales"])
    for cid in iguales:
        if LECTURA[cid]["a"] != LECTURA[cid]["b"]:
            raise SystemExit(f"{cid}: salidas iguales con lecturas distintas")
    grupos: dict[str, list[str]] = {}
    for u in sel["unidades"]:
        grupos.setdefault(u["grupo"], []).append(u["id"])
    tabla, cambios = {}, {}
    for g, ids in grupos.items():
        fila = {}
        for f in CORRIDAS:
            m = Counter(LECTURA[c][f][0] for c in ids)
            fila[f] = {"cumple": m[C], "de": len(ids) - m[NA]}
        m = Counter(p4b[c]["p3c"]["marca"] for c in ids)
        fila["p4b_p3c"] = {"cumple": m[C], "de": len(ids) - m[NA]}
        tabla[g] = fila
        cambios[g] = {
            "a_contra_p4b": {"cambian": [c for c in ids if LECTURA[c]["a"][0] != p4b[c]["p3c"]["marca"]], "de": len(ids)},
            "b_contra_p4b": {"cambian": [c for c in ids if LECTURA[c]["b"][0] != p4b[c]["p3c"]["marca"]], "de": len(ids)},
            "a_contra_b": {"cambian": [c for c in ids if LECTURA[c]["a"][0] != LECTURA[c]["b"][0]], "de": len(ids)}}
    totales = {k: {"cambian": sum(len(cambios[g][k]["cambian"]) for g in cambios),
                   "de": sum(cambios[g][k]["de"] for g in cambios)} for k in ("a_contra_p4b", "b_contra_p4b", "a_contra_b")}
    out = {"comando": "data/experiment/prompt_r2/p5/marcas_p5.py --analisis A --salida DIR",
           "tabla": tabla, "cambios_de_marca": cambios, "totales": totales,
           "lectura": {c: {f: {"marca": LECTURA[c][f][0], "razon": LECTURA[c][f][1]} for f in CORRIDAS}
                       | {"p4b_p3c": p4b[c]["p3c"]} for c in sorted(LECTURA)}}
    sal.mkdir(parents=True, exist_ok=True)
    (sal / "marcas_p5.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"tabla": tabla, "cambios": {g: {k: f"{len(v['cambian'])} de {v['de']}" for k, v in d.items()}
                                                  for g, d in cambios.items()}, "totales": totales},
                     ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
