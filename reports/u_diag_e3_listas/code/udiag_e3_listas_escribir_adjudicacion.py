"""U-DIAG-E3-LISTAS: vuelca mi adjudicación de los 96 candidatos y de la muestra de 15 ANTES de computar.

Categorías de los candidatos (reclamos de E3 en ítems de lista que nombran una excepción o una Excepcion):
  P  polaridad o sentido de una Excepcion: el reclamo dice que la Excepcion (o el modelado del ítem como
     excepción) invierte o contradice lo que dice el texto.
  C  contenido de lo extraído (la Excepcion o la norma que exceptúa) que E3 no encuentra en su fuente.
  B  norma del encabezado de la lista que la Excepcion o la Condicion del ítem supone, reclamada como entidad del
     ítem (P3C-d1 y P3C-d2 mandan no emitirla en el ítem).
  B2 sujeto o condición del encabezado que el ítem no compone (R30 manda componerlos).
  M  modalidad de una Excepcion (facultad o regla).
  E  salvedad o excepción del texto que no quedó representada (o quedó declarada como omisión).
  O  otro: la excepción aparece de paso (calificadores, enumeraciones, reclamos retirados por la propia nota).
Juicio de los P y los C (censo): falsa_alarma_lista (el reclamo cae si E3 lee el bloque que abre la lista),
falsa_alarma_otra (cae por otra razón), mixta, fundada.
"""
import json
import sys
from pathlib import Path

SAL = Path(sys.argv[1])
c = json.loads((SAL / "fase1_candidatos.json").read_text(encoding="utf-8")) + \
    json.loads((SAL / "fase2_candidatos_extra.json").read_text(encoding="utf-8"))
cats = {
    "P": [0, 30, 39, 60, 61],
    "C": [32, 37, 74, 75, 76, 87, 90],
    "B": [10, 11, 12, 13, 14, 18, 20, 22, 24, 25, 26, 29, 31, 34, 35, 36, 38, 40, 42, 43, 44, 46, 49, 50, 51, 52,
          53, 63, 68, 69, 70],
    "B2": [28, 57, 58],
    "M": [4, 73, 79],
    "E": [1, 2, 5, 8, 45, 59, 62, 64, 67, 71, 81, 82, 83, 84],
    "O": [3, 6, 7, 9, 15, 16, 17, 19, 21, 23, 27, 33, 41, 47, 48, 54, 55, 56, 65, 66, 72, 77, 78, 80, 85, 86, 88, 89,
          91, 92, 93, 94, 95],
}
juicios = {
    0: ("falsa_alarma_lista", "el bloque intro del 5.1.1 («Abarca todas las financiaciones comprendidas, con excepción "
        "de las siguientes:») hace del ítem una exclusión con contra-excepción (P3C-b1); E3 no lo recibe"),
    30: ("falsa_alarma_lista", "el intro del 3.5.6 dice «Este requisito no resultará aplicable cuando la operación "
         "encuadre en alguna de las siguientes situaciones:»; E3 solo ve la línea de título truncada del 3.5.6"),
    39: ("falsa_alarma_lista", "el intro del 3.6.1 («excepto para la cancelación en el país ... de:») hace del ítem "
         "una excepción a la prohibición; E3 lee el ítem como una deuda prohibida"),
    60: ("falsa_alarma_otra", "«sólo será aplicable para clientes que no sean personas humanas residentes» equivale a "
         "«no es aplicable para personas humanas residentes»; el texto está entero en el ítem"),
    61: ("falsa_alarma_otra", "la misma equivalencia que ext::4.4.4 en la polaridad; la otra objeción de la nota (c1 "
         "condicion_de e1) señala un error real de modelado, que no es de polaridad"),
    32: ("falsa_alarma_lista", "«cuando el acreedor sea una contraparte vinculada al deudor» está en el intro del 3.5.6"),
    37: ("falsa_alarma_lista", "«entre residentes concertadas a partir del 01/09/19» está en el intro del 3.6.1; la "
         "nota además da a la Excepcion e2 por correcta"),
    74: ("falsa_alarma_lista", "«por el valor que corresponda a ventajas aduaneras u otras situaciones previstas» es "
         "el intro del 8.5.17"),
    75: ("falsa_alarma_lista", "el mismo intro del 8.5.17"),
    76: ("falsa_alarma_lista", "el mismo intro del 8.5.17"),
    87: ("mixta", "el plazo 31.12.27 viene del intro del 5.1.1 (composición); las cuatro excepciones vienen del "
         "cierre del 5.1.1, que el ítem no debe extraer (CIERRES y R28)"),
    90: ("fundada", "la Excepcion e5 copia el cierre del 3.3 y la Condicion e6 describe supuestos de otros puntos: "
         "ninguna de las dos sale del bloque que abre la lista"),
}
adj = {}
for cat, idx in cats.items():
    for i in idx:
        x = c[i]
        e = {"categoria": cat, "chunk_id": x["chunk_id"]}
        if i in juicios:
            e["juicio"], e["razon"] = juicios[i]
        adj[x["id"]] = e
assert len(adj) == len(c) == 96, (len(adj), len(c))
(SAL / "adjudicacion_candidatos.json").write_text(json.dumps(adj, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

muestra = {
    "cap::2.11.3.1|verificacion|0|1": ("falsa_alarma_lista", "la Condicion e4 (realidad económica, grupo 1) sale del intro del 2.11.3"),
    "cap::6.7.1.1|verificacion|0|0": ("no_relacionada", "reclama el «y» del propio ítem (cuantificador), no el bloque"),
    "cap::8.6.2|verificacion|0|0": ("mixta", "la autorización de la SEFyC viene del intro del 8.6; el valor de mercado, del cierre"),
    "ctacte::12.1.2.11|verificacion|0|1": ("no_relacionada", "el sujeto de aplica_a está mal también con el bloque: reclamo fundado"),
    "ctacte::2.1.1.4|verificacion|0|0": ("falsa_alarma_lista", "«Cuando se empleen boletas, éstas deberán contener...» es el intro del 2.1.1"),
    "ctacte::6.1.2.3|verificacion|0|0": ("no_relacionada", "el intro del 6.1.2 define causales; no prohíbe: el reclamo se sostiene con el bloque"),
    "ext::3.11.1.1|re_verificacion|1|1": ("falsa_alarma_lista", "«o los fideicomisos constituidos en el país...» está en el intro del 3.11.1"),
    "ext::3.17.4.3|verificacion|0|1": ("falsa_alarma_otro_bloque", "título del 3.17 truncado; su continuación es el intro del 3.17, que no es el que abre la lista"),
    "ext::3.18.2.3|verificacion|0|0": ("falsa_alarma_lista", "requisitos que se exigen juntos: la norma queda en la unidad del encabezado (R30)"),
    "ext::3.6.1.1|verificacion|0|0": ("falsa_alarma_lista", "«entre residentes concertadas a partir del 01/09/19» está en el intro del 3.6.1"),
    "ext::7.9.1.7|verificacion|0|0": ("falsa_alarma_lista", "«que se cumplan las condiciones consignadas en cada caso» está en el intro del 7.9.1"),
    "lingob::7.2.3.8|verificacion|0|0": ("dudosa", "la propia nota duda que la cláusula truncada agregue contenido"),
    "pagjub::2.8.3.1|verificacion|0|0": ("falsa_alarma_lista", "«en el mismo día de la aceptación» está en el intro del 2.8.3"),
    "pagjub::2.8.4.1|verificacion|0|0": ("falsa_alarma_lista", "«en el mismo día de la aceptación» está en el intro del 2.8.4"),
    "pro::3.2.3.7|verificacion|0|0": ("falsa_alarma_lista", "la disponibilidad en la sede ante el BCRA está en el intro del 3.2.3"),
}
sorteo = json.loads((SAL / "fase2_resumen.json").read_text(encoding="utf-8"))["sorteo"]["ids"]
assert sorted(muestra) == sorted(sorteo)
(SAL / "adjudicacion_muestra.json").write_text(json.dumps({k: {"juicio": a, "razon": b} for k, a in [(k, v[0]) for k, v in muestra.items()] for b in [muestra[k][1]]},
                                                          ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("ok", len(adj), len(muestra))
