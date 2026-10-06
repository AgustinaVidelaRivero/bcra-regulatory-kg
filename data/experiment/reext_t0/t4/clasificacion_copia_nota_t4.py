"""U-REEXT-T0, T4, punto 3: mi lectura de los casos de copia de la nota de E3 con la regla fijada antes
(data/experiment/prompt_r2/p3b2/regla_lectura_copia_nota.md, sha256 1427b16c…, sin ajustes), sobre la lista de
lista_copia_nota_t4.py. Como en la lectura de P3b-2 (data/experiment/prompt_r2/p3b2/lectura_copia_nota.md), las
flexiones de una palabra de la unidad (género, número, forma verbal, con clítico) cuentan como presentes (regla 2); una
derivación (otro sustantivo, otro verbo, una nominalización) es otra palabra. Las clases van por orden: 1 metalenguaje,
2 coincidencia legítima, 3 copia real, 4 dudosa. La lectura es la de abajo, caso por caso, con su razón; el script solo
la cruza con la lista y cuenta. Escribe --out (JSON) y --md. USD 0.

Uso: python -B data/experiment/reext_t0/t4/clasificacion_copia_nota_t4.py --lista LISTA.json --out J --md M
"""
from __future__ import annotations

import argparse
import json
from collections import Counter, OrderedDict
from pathlib import Path

R, L, D = "copia real", "coincidencia legítima", "dudosa"
LECTURA = {
    1: (R, "ausentes «protección», «usuarios», «servicios»: son el título del TO (label del TextoOrdenado), no texto de la unidad"),
    2: (R, "ausentes «protección», «usuarios», «servicios»: la frase de la nota, que es el título del TO"),
    3: (R, "ausente «cómputo» (la unidad no tiene ninguna forma de computar)"),
    4: (R, "ausente «basta»: «no basta con alguna» es la frase de la nota"),
    5: (L, "«el manual de procedimientos de» es la frase de la norma"),
    6: (L, "«llevar un legajo de cada deudor», sin el artículo"),
    7: (R, "ausente «obligación»: nominalización que agrega la nota; «abrir» está en la unidad («abrirse»)"),
    8: (L, "«cedidos por deudores en concurso preventivo», literal"),
    9: (L, "ídem caso 8"),
    10: (R, "ausente «anterior»: «el porcentaje del párrafo anterior» es la frase de la nota"),
    11: (L, "«en los términos del punto 2.2.5.», literal"),
    12: (L, "«Grupos A, B o C», literal"),
    13: (L, "ídem caso 12"),
    14: (R, "ausentes «cómputo», «excluidas», «quedan»: la exclusión del cómputo es la lectura de la nota"),
    15: (R, "ausente «exclusivamente»: la nota glosa «sólo»"),
    16: (L, "«con fondos de líneas asignadas», literal"),
    17: (L, "«no se incluyen las operaciones de pase que no hayan podido liquidarse»: «liquidadas», flexión"),
    18: (L, "«garantía bajo el método simple», de la norma"),
    19: (R, "ausente «integra»"),
    20: (R, "ausente «régimen»"),
    21: (R, "ausente «quedan»: «quedan reemplazados» es la frase de la nota"),
    22: (L, "«requisitos de acceso del cliente», de la norma"),
    23: (R, "ausente «operación»"),
    24: (L, "«no comprendido en los puntos 13.2.1. a 13.2.5.» sin «los puntos»"),
    25: (L, "ídem caso 24"),
    26: (L, "«códigos de concepto» y los servicios de la lista, de la norma"),
    27: (D, "las palabras están («específicas» solo en «disposiciones específicas»), pero «servicios específicos» es la "
              "frase de la nota y no reformula la norma, que dice «los siguientes códigos de concepto»"),
    28: (R, "ausente «sujeto»; «alcanzado» es flexión de «alcanzadas»"),
    29: (R, "ausente «cómputo» («computados» es otra palabra, derivada)"),
    30: (L, "«podrán dar acceso al mercado de cambios», de la norma"),
    31: (L, "ídem caso 30"),
    32: (L, "ídem caso 30"),
    33: (L, "ídem caso 30"),
    34: (L, "«el requisito de conformidad previa del BCRA», de la norma (como los casos 16 y 18 de P3b-2)"),
    35: (R, "ausentes «basta» y «supuesto»"),
    36: (D, "frase sobre la estructura del texto («de las cuales la situación del punto 3.4.4.7 es una»), que está en "
              "la nota; la norma la dice con otras palabras («alguna de las siguientes situaciones»)"),
    37: (L, "«el acceso al mercado de cambios», de la norma"),
    38: (L, "«no registren vencimientos de capital»: «deben registrar», flexión"),
    39: (L, "«en los primeros 2 (dos) años por el endeudamiento», literal"),
    40: (L, "ídem caso 39"),
    41: (L, "ídem caso 39"),
    42: (L, "«con una anterioridad no mayor a 3», de la norma"),
    43: (L, "remite al 3.5.4 por su número, como su encabezado («3.5.4. En la medida que…»)"),
    44: (R, "ausente «vigencia» (la norma dice «vigente»): el mismo caso que el 19 de P3b-2"),
    45: (D, "«incluido el presente punto 3.5.6.11» es una frase de la nota sobre la estructura; «incluido» está "
              "como «incluyendo» en otra oración"),
    46: (L, "ídem caso 34"),
    47: (R, "ausente «prohibición» (la norma dice «Se prohíbe»: nominalización de la nota)"),
    48: (R, "ídem caso 47"),
    49: (R, "ausente «calificación»"),
    50: (L, "«BOPREAL por deudores de importaciones», del título 4.4 (como el caso 22 de P3b-2)"),
    51: (L, "ídem caso 50"),
    52: (L, "«el equivalente en moneda local», de la norma"),
    53: (L, "ídem caso 52"),
    54: (L, "«haber suscripto BOPREAL Serie 1», de la norma"),
    55: (L, "«venta con obligación de recompra de BOPREAL», de la norma (como el caso 23 de P3b-2)"),
    56: (L, "ídem caso 55"),
    57: (L, "«los capítulos 26 y 71», literal"),
    58: (L, "«en caso de no disponerla… la documentación que avale la capitalización»: flexiones"),
    59: (L, "«al cumplimiento de las condiciones», de la norma"),
    60: (L, "«operaciones 7.9.1.1», de la norma"),
    61: (R, "ausentes «1» y «x»: «7.9.3.1 a 7.9.3.x» es el marcador de posición de la nota (como el caso 44 de P3b-2)"),
    62: (R, "ausente «facultad»"),
    63: (R, "ausente «régimen»; «comprendidos», flexión"),
    64: (L, "«estado civil» y «titulares»: flexión"),
    65: (L, "«personas jurídicas titulares de cuentas corrientes», de la norma"),
    66: (L, "«contrato o estatuto, objeto social y», de la norma"),
    67: (L, "«carecen de valor como cheques»: flexión"),
    68: (L, "«de valor como cheque», de la norma"),
    69: (R, "ausente «carencia» (nominalización de «carecen»)"),
    70: (L, "ídem caso 67"),
    71: (R, "ídem caso 69"),
    72: (R, "ídem caso 69"),
    73: (L, "«a persona determinada sin cláusula “no a la orden”», de la norma"),
    74: (L, "«a favor de persona determinada», de la norma"),
    75: (L, "«los rechazos de los puntos 6.4.6.2. a 6.4.6.4.», de la norma"),
    76: (L, "«efectuadas con sujeción a», de la norma"),
    77: (R, "ausente «modificación» (la norma dice «modificar»)"),
    78: (R, "ausente «necesidad» (la norma dice «sea necesario»)"),
    79: (L, "«inclusión en la Central de», de la norma"),
    80: (L, "«falta de pago de la multa», de la norma"),
    81: (L, "«el Directorio se asegurará de que», de la norma"),
    82: (R, "ausente «recomendación»: «una recomendación de buena práctica» es la lectura de la nota"),
    83: (L, "«esté condicionado al resultado de», flexión"),
    84: (L, "«préstamos de organismos multilaterales de crédito», de la norma"),
    85: (L, "«para los aspectos no previstos», de la norma"),
    86: (R, "ausente «obligación»: nominalización de la nota"),
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lista", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--md", type=Path, required=True)
    a = ap.parse_args()
    lista = json.loads(a.lista.read_text(encoding="utf-8"))
    casos = lista["casos"]
    assert sorted(LECTURA) == [c["n"] for c in casos], "la lectura no cubre la lista"
    filas = []
    for c in casos:
        clase, razon = LECTURA[c["n"]]
        # control: la clase 3 exige una palabra de contenido ausente; la 2 y la 4, ninguna ausente salvo flexiones
        if clase == R:
            assert c["contenido_ausente_de_la_unidad"], c["n"]
        filas.append(OrderedDict([("n", c["n"]), ("chunk_id", c["chunk_id"]), ("local_id", c["local_id"]),
                                  ("type", c["type"]), ("campo", c["campo"]), ("clase", clase), ("razon", razon),
                                  ("clase_mecanica", c["clase_mecanica"])]))
    cnt = Counter(f["clase"] for f in filas)
    unidades = {k: sorted({f["chunk_id"] for f in filas if f["clase"] == k}) for k in (R, L, D)}
    res = OrderedDict([("regla_sha256", lista["resumen"]["regla_sha256"]), ("casos", len(filas)),
                       ("unidades", lista["resumen"]["unidades"]),
                       ("por_clase", {k: cnt.get(k, 0) for k in (R, L, D, "metalenguaje")}),
                       ("unidades_con_al_menos_una_copia_real", len(unidades[R])),
                       ("unidades_por_clase", {k: len(v) for k, v in unidades.items()}),
                       ("mecanica_3_que_la_lectura_no_confirma", [f["n"] for f in filas if f["clase_mecanica"] == 3 and f["clase"] != R]),
                       ("referencia_r2a", "11 de 45 (data/experiment/prompt_r2/p3b2/lectura_copia_nota.md)")])
    a.out.write_text(json.dumps({"resumen": res, "casos": filas}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    md = ["# Lectura de los casos de copia de la nota de E3 (U-REEXT-T0, T4, punto 3)", "",
          f"Regla `regla_lectura_copia_nota.md` (sha256 `{res['regla_sha256'][:12]}…`), sin ajustes. {res['casos']} casos en "
          f"{res['unidades']} unidades: copia real {cnt.get(R, 0)}, coincidencia legítima {cnt.get(L, 0)}, dudosa {cnt.get(D, 0)}, "
          f"metalenguaje 0. Unidades con al menos una copia real: {len(unidades[R])}. Referencia (r2a): 11 de 45.", "",
          "| # | Unidad | Entidad, campo | Clase | Razón |", "|---|---|---|---|---|"]
    md += [f"| {f['n']} | `{f['chunk_id']}` | {f['local_id']} {f['type']}, {f['campo']} | {f['clase']} | {f['razon']} |" for f in filas]
    a.md.write_text("\n".join(md) + "\n", encoding="utf-8")
    print(json.dumps(res, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
