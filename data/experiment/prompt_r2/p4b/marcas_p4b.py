"""
marcas_p4b.py — U-PROMPT-R2, P4b (USD 0, sin API): la lectura asistida de las fichas (LECTURA, por unidad y brazo,
con su razón) y la tabla por grupo y brazo (cuántos casos cumplen lo que mide el grupo, como fracción), más la lectura
de cada omisión `meta_normativo` (si es contenido normativo) para la medición d.

Lo que mide cada grupo (diseño de P3c-1, §8, y «seguí» de P4b):
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
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
BRAZOS = ("anterior", "p3c")
C, N, NA = "cumple", "no_cumple", "no_aplica"

# Lectura por unidad y brazo: (marca, razón). Lo que se lee es lo que mide el grupo de la unidad.
LECTURA: dict[str, dict[str, tuple[str, str]]] = {
    # a
    "ext::13.1.4": {"anterior": (C, "el régimen de transición, extraído: la Condicion «hasta el 12/12/23» de la "
                                    "Obligacion de verificar el encuadre en 13.4, y la Potestad de suscribir BOPREAL con "
                                    "su Condicion; sin omisión meta_normativo"),
                    "p3c": (N, "el régimen de transición está extraído igual, pero registra como meta_normativo el "
                               "encabezado heredado de 13.1, una facultad con condiciones")},
    "ext::6.1.1": {"anterior": (C, "Definicion de lo que la clase comprende; sin omisión"),
                   "p3c": (C, "Definicion de lo que la clase comprende; sin omisión")},
    "cap::10.3.3.1": {"anterior": (C, "el alcance de la calificación (a qué créditos se aplica), como Potestad con su "
                                      "Condicion; sin omisión meta_normativo"),
                      "p3c": (C, "el alcance de la calificación, como Potestad; sin omisión meta_normativo")},
    "cap::11.4": {"anterior": (C, "sin omisión; «A los efectos de la determinación de la RPC» queda en una Operacion, "
                                  "cuyo condicion_de a la Potestad se rechaza por la firma"),
                  "p3c": (N, "registra «A los efectos de la determinación de la RPC» como meta_normativo: por la "
                             "prueba del prefijo es alcance (sin la frase, la facultad valdría para más casos)")},
    # b1 (lectura dudosa de la lista: ver seleccion_p4b.md)
    "ctacte::3.2.2": {"anterior": (N, "Restriccion, no Excepcion; `prohibe` colgante rechazado; aplica_a «las "
                                      "entidades», que el texto no nombra"),
                      "p3c": (N, "Restriccion, no Excepcion")},
    "ctacte::3.2.5": {"anterior": (N, "Restriccion, no Excepcion"),
                      "p3c": (N, "Condicion del supuesto y Restriccion de la clase; no hay Excepcion")},
    "ctacte::3.2.4": {"anterior": (N, "Restriccion, no Excepcion"),
                      "p3c": (N, "Restriccion, no Excepcion; `prohibe` colgante rechazado")},
    # b2
    "ext::3.5.3.4": {"anterior": (N, "las Condicion no nombran la norma exceptuada; emite la Excepcion del encabezado "
                                     "con `exceptua` hacia una Restriccion equivocada"),
                     "p3c": (N, "de las tres condiciones, una es Condicion y no nombra la norma exceptuada; la nombra "
                                "una Excepcion compuesta, que la regla deja en la unidad del encabezado")},
    "ext::3.5.3.5": {"anterior": (N, "la Condicion no nombra la norma exceptuada ni el cuantificador; emite la "
                                     "Excepcion compuesta, que la regla deja en la unidad del encabezado"),
                     "p3c": (N, "la Condicion va a una Operacion; ninguna entidad nombra la norma exceptuada")},
    "ext::3.5.3.1": {"anterior": (N, "Condicion y Restriccion hacia la Operacion; ninguna nombra la norma exceptuada"),
                     "p3c": (N, "Condicion (dos condiciones en una) y Restriccion; ninguna nombra la norma exceptuada")},
    # b, encabezados
    "ctacte::3.2::intro": {"anterior": (N, "Restriccion, no Definicion de la clase"),
                           "p3c": (N, "Restriccion, no Definicion de la clase")},
    "ext::3.5.3::intro": {"anterior": (N, "la norma (como Potestad del BCRA) y la Excepcion, sin relación entre ellas"),
                          "p3c": (N, "la norma (como Potestad del BCRA) y la Excepcion, con `exceptua_obligacion` "
                                     "rechazado por la firma; y registra la exigencia de conformidad como meta_normativo")},
    # c
    "cap::5.3.1.3": {"anterior": (C, "una Condicion por supuesto (participante esencial, a) a h), no esencial, las "
                                     "de iii), con su umbral), cada una hacia su norma"),
                     "p3c": (N, "las ocho de a) a h), coherentes; pero el supuesto «participante esencial» y los de "
                                "ii) y iii) no son Condicion: van en Operacion y Excepcion")},
    "cla::6.5.4.5": {"anterior": (C, "una Condicion por supuesto, coherentes, hacia su Potestad o Restriccion; el "
                                     "«porcentaje acumulado» queda en una omisión meta_normativo"),
                     "p3c": (N, "dos Condicion coherentes; los dos supuestos «las otras condiciones» van en la "
                                "descripción de las Potestad, no como Condicion")},
    "ext::10.4.2.5": {"anterior": (N, "una Condicion junta dos supuestos (no persona humana y constituida hasta 365 "
                                      "días) y el monto va como umbral del deber"),
                      "p3c": (N, "una sola Condicion con los tres supuestos y la norma (la conformidad previa), sin "
                                 "condicion_de; la norma no se emite")},
    "ext::10.3.6": {"anterior": (N, "los supuestos de fecha van como umbral de dos Obligacion, no como Condicion"),
                    "p3c": (C, "una Condicion por supuesto (documentación, desde el 13/12/23, plazo más 15 días, desde "
                               "el 14/04/25), coherentes; aparte, la Excepcion hacia una Condicion se rechaza")},
    # d
    "ext::10.4.3.6": {"anterior": (C, "sin entidad aparte para la facultad del encabezado (heredado_compuesto 0)"),
                      "p3c": (C, "sin entidad aparte; la condición del encabezado, como Condicion del ítem")},
    "ext::4.1.4.7": {"anterior": (C, "una Obligacion compuesta (tramo de dos segmentos) que regula la Operacion del "
                                     "ítem; su descripción es la del encabezado"),
                     "p3c": (C, "una Obligacion compuesta con el contenido del ítem")},
    "polcre::2.1.15": {"anterior": (C, "sin entidad aparte para el deber del encabezado"),
                       "p3c": (C, "sin entidad aparte para el deber del encabezado")},
    "cap::10.2.2.4": {"anterior": (C, "sin entidad aparte para «deberán cumplir los criterios»"),
                      "p3c": (C, "sin entidad aparte para «deberán cumplir los criterios»")},
    # e
    "cap::6.3.2::intro": {"anterior": (N, "aplica_a «las entidades», que el texto no nombra (mención no verificada)"),
                          "p3c": (C, "sin relación de sujeto")},
    "cap::3.2::intro": {"anterior": (C, "sin relación de sujeto"),
                        "p3c": (N, "aplica_a «Las participaciones en fondos»: verifica en el texto, pero no es un sujeto")},
    "cap::6.3.2.1": {"anterior": (N, "cinco aplica_a «las entidades», que el texto no nombra"),
                     "p3c": (C, "sin relación de sujeto")},
    "polcre::5.3": {"anterior": (N, "dos aplica_a «las entidades», que el texto no nombra"),
                    "p3c": (C, "sin relación de sujeto")},
    # el ejemplo
    "cla::5.1.1::intro": {"anterior": (N, "Operacion y la frase entera como omisión meta_normativo; sin Definicion"),
                          "p3c": (C, "Definicion «Cartera comercial — alcance»; «con excepción de las siguientes», como "
                                     "fuera_de_tipos")},
    "cla::5.1.1.1": {"anterior": (C, "Excepcion, Operacion de clasificar en la cartera comercial y una Condicion por "
                                     "cada condición (monto y repago), hacia esa Operacion"),
                     "p3c": (N, "Excepcion y Operacion de clasificar, pero una sola Condicion (el repago): el monto va "
                                "como umbral de la Excepcion; su `exceptua` a la Operacion se rechaza por la firma")},
    # f
    "cap::6.2.2.6": {"anterior": (N, "copia 40 %, 30 % y 100 % de cap::tabla037 (su release no la forzaba a residual)"),
                     "p3c": (C, "ningún porcentaje de cap::tabla037 copiado; la omisión `tabla` declarada")},
}

# Lectura de cada omisión meta_normativo (medición d): (brazo, unidad) → (es contenido normativo, dudosa, razón).
META: dict[tuple[str, str], tuple[bool, bool, str]] = {
    ("anterior", "cla::5.1.1::intro"): (True, False, "el alcance de la clase (enmienda 7, §1.2)"),
    ("anterior", "cla::6.5.4.5"): (True, False, "parte del supuesto de la reclasificación: un monto más a pagar"),
    ("anterior", "ctacte::3.2.4"): (True, False, "una prohibición (cierre heredado de 3.2)"),
    ("anterior", "ctacte::3.2.5"): (True, False, "lo que queda afuera de la clase «cheque»"),
    ("anterior", "ctacte::3.2::intro"): (True, True, "el cuantificador de la lista: la enumeración es cerrada"),
    ("anterior", "ext::10.3.6"): (True, True, "aplicabilidad temporal por remisión: las cartas hasta el 12/12/23 "
                                              "siguen las condiciones de la Com. A 7914"),
    ("anterior", "ext::10.4.3.6"): (True, False, "la facultad del encabezado"),
    ("anterior", "ext::3.5.3.4"): (True, False, "el deber de conformidad previa y su excepción (encabezado heredado)"),
    ("anterior", "ext::3.5.3.5"): (True, False, "alcance: sin «en el marco de lo previsto en el punto 14.2.1» la "
                                                "excepción valdría para más casos"),
    ("anterior", "ext::4.1.4.7"): (True, False, "la condición que delimita los pagos alcanzados"),
    ("p3c", "cap::11.4"): (True, False, "alcance, por la prueba del prefijo"),
    ("p3c", "cap::3.2::intro"): (True, False, "el deber de tratar las participaciones por uno de los enfoques"),
    ("p3c", "cap::6.3.2::intro"): (True, False, "el alcance de la norma: lo que comprende"),
    ("p3c", "cla::5.1.1.1"): (True, False, "el alcance de la clase (encabezado heredado)"),
    ("p3c", "ctacte::3.2.2"): (True, True, "el cuantificador de la lista: la enumeración es cerrada (heredado)"),
    ("p3c", "ctacte::3.2.4"): (True, False, "lo que queda afuera de la clase «cheque» (heredado; ya está en su "
                                            "Restriccion)"),
    ("p3c", "ctacte::3.2.5"): (True, False, "una prohibición (cierre heredado de 3.2)"),
    ("p3c", "ext::10.3.6"): (True, True, "aplicabilidad temporal por remisión (como en el brazo anterior)"),
    ("p3c", "ext::10.4.2.5"): (True, False, "la facultad con su condición (encabezado heredado)"),
    ("p3c", "ext::10.4.3.6"): (True, False, "la alternativa del deber («o en su defecto…»); ya está en la Obligacion"),
    ("p3c", "ext::13.1.4"): (True, False, "la facultad con condiciones (encabezado heredado)"),
    ("p3c", "ext::3.5.3::intro"): (True, False, "el deber de conformidad previa"),
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
    sel = json.loads((AQUI / "salida" / "seleccion_p4b.json").read_text(encoding="utf-8"))
    faltan = sorted(set(an["filas"]) - set(LECTURA))
    if faltan:
        raise SystemExit(f"unidades sin lectura: {faltan}")
    tabla = {}
    for g, ids in sel["grupos"].items():
        fila = {}
        for b in BRAZOS:
            marcas = Counter(LECTURA[c][b][0] for c in ids)
            fila[b] = {"cumple": marcas[C], "de": len(ids) - marcas[NA]}
        tabla[g] = fila
    meta = {}
    for b in BRAZOS:
        oms = an["meta_normativo"][b]
        claves = [(b, m["id"]) for m in oms]
        sin = sorted({k for k in claves if k not in META})
        if sin or len(claves) != len(set(claves)):
            raise SystemExit(f"omisiones sin lectura o repetidas por unidad: {sin}")
        filas = [{"id": m["id"], "tramo": m["tramo"], "clases": m["clases"], "subclases_modalidad": m["subclases_modalidad"],
                  "solo_forma": m["solo_forma"], "normativa": META[(b, m["id"])][0], "dudosa": META[(b, m["id"])][1],
                  "razon": META[(b, m["id"])][2]} for m in oms]
        meta[b] = {"omisiones": len(filas), "normativas": sum(f["normativa"] for f in filas),
                   "normativas_dudosas": sum(f["normativa"] and f["dudosa"] for f in filas),
                   "marcadas": sum(bool(f["clases"]) for f in filas),
                   "marcadas_normativas": sum(bool(f["clases"]) and f["normativa"] for f in filas),
                   "marcadas_no_normativas": sum(bool(f["clases"]) and not f["normativa"] for f in filas),
                   "normativas_sin_marca": [f["id"] for f in filas if f["normativa"] and not f["clases"]],
                   "solo_forma": sum(f["solo_forma"] for f in filas), "filas": filas}
    out = {"comando": "data/experiment/prompt_r2/p4b/marcas_p4b.py --analisis A --salida DIR",
           "tabla": tabla, "meta_normativo": meta,
           "lectura": {c: {b: {"marca": LECTURA[c][b][0], "razon": LECTURA[c][b][1]} for b in BRAZOS} for c in sorted(LECTURA)}}
    sal.mkdir(parents=True, exist_ok=True)
    (sal / "marcas_p4b.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (sal / "tabla_p4b.json").write_text(json.dumps({"tabla": tabla, "meta_normativo": {b: {k: v for k, v in m.items()
                                                                                         if k != "filas"} for b, m in meta.items()}},
                                                   ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"tabla": tabla, "meta": {b: {k: v for k, v in m.items() if k != "filas"} for b, m in meta.items()}},
                     ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
