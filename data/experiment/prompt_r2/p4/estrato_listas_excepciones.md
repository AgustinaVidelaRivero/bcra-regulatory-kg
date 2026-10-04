# Estrato de listas de excepciones de P4 (elegidas por lectura)

04/10/2026, antes de correr la pareada. USD 0.

**Qué mide.** Si la regla f del parche (cada ítem de una lista de excepciones es una Excepcion compuesta con la norma
del encabezado, sin `exceptua` cuando esa norma está en otra unidad) generaliza a listas que no se leyeron al escribirla
(nota de P3b al mandato, `docs/mandatos/UPROMPT_R2_prefijo_nuevo.md:517-519`).

**De dónde salen.** De los 221 párrafos contenedores de la tanda 0 que detecta el censo de U-DIAG-VINCULO
(`reports/u_diag_vinculo/salidas/censo_anuncios.json`, `contenedores_tanda0`; `b0ee084`).
- Excluí, por unidad, los contenedores leídos o citados al escribir la regla f: las muestras de U-DIAG-VINCULO
  (`muestra10`, `muestra_aT` y `muestra_aR`), los que nombran su reporte, su anexo, sus lecturas, su regla y el censo, y
  los que nombran el diseño y el freno de P3b-1. Quedan 185.
- Leí la cláusula de los 185, sin mirar el tipo léxico del censo, y tomé las que anuncian una lista de excepciones:
  cada ítem es un caso en que la norma no se aplica.

**Las cinco listas.**

| Contenedor | La cláusula (resumida) | Por qué es una lista de excepciones |
|---|---|---|
| `ext::3.5.6::intro` | se requiere la conformidad previa del BCRA cuando el acreedor es vinculado; «este requisito no resultará aplicable cuando la operación encuadre en alguna de las siguientes» | cada ítem es un supuesto alternativo en que el requisito no rige |
| `ext::13.4::intro` | se requiere la conformidad previa para pagar servicios devengados hasta el 12/12/23, «excepto cuando […] la entidad verifique que:» | los ítems son las excepciones, alternativas (terminan en «; o») |
| `ext::3.3.3::intro` | se requiere la conformidad previa por intereses con vinculadas; «este requisito no resultará aplicable cuando la operación encuadre en alguna de las siguientes situaciones:» | cada ítem es una situación que exceptúa |
| `ctacte::6.2::intro` | «Serán atendidos los cheques […] no comprendidos en las situaciones previstas en el punto 6.1., cuando:» (título: casos no susceptibles de rechazo) | cada ítem es un caso en que no rige el rechazo |
| `ctacte::5.1.2::intro` | los cheques «no a la orden» podrán transmitirse por endoso «en los casos de transferencias […] cuando se extienda:» | cada ítem es un caso en que no rige la intransmisibilidad del cheque «no a la orden» |

**Las que descarté**, aunque su cláusula habla de una excepción:
- `ext::3.5.4`, `ext::2.6.1`, `ext::7.8.4` y `ext::2.7`: los ítems son las condiciones de una sola excepción, no
  excepciones distintas;
- `ext::3.16.2`: los ítems son el contenido de una declaración jurada.

**Los ítems.**
- **Cuántos por lista:** uno por lista, y uno más en cada lista de ext, que son las más largas: 8 unidades.
- **Cómo se eligen:** por semilla, entre los ítems que no se nombran en ninguna lectura anterior (`muestra_p4.py`,
  `LISTAS` y `LEIDOS`; incluye la lectura de los 45 casos de P3b-2).
- **Lectura:** leí los 8 elegidos antes de correr. Cada uno es un caso de su excepción, así que no reemplacé ninguno.

| Ítem | Lista | Qué dice |
|---|---|---|
| `ext::3.5.6.9` | `ext::3.5.6` | el cliente cuenta con una certificación de aumento de exportaciones (2021 a 2023) por el capital que paga |
| `ext::3.5.6.1` | `ext::3.5.6` | se trata de operaciones propias de las entidades financieras locales |
| `ext::13.4.8` | `ext::13.4` | el pago lo hace, desde el 10/02/24, una persona humana o una MiPyMe que cumple condiciones (con sub-ítems) |
| `ext::13.4.4` | `ext::13.4` | el cliente cuenta con una certificación de los regímenes del Decreto 277/22 por el monto a pagar |
| `ext::3.3.3.1` | `ext::3.3.3` | se trata de operaciones propias de las entidades financieras locales |
| `ext::3.3.3.3` | `ext::3.3.3` | el cliente cuenta con una certificación de los regímenes del Decreto 277/22 por el valor que se abona |
| `ctacte::6.2.4` | `ctacte::6.2` | se observan faltas de ortografía |
| `ctacte::5.1.2.2` | `ctacte::5.1.2` | a favor de fiduciarios de fideicomisos financieros, para operaciones del fideicomiso |

En los 8 ítems, el último bloque heredado es un párrafo de cierre del punto que contiene la lista: es el caso que la
regla g del parche reconoce como ítem.
