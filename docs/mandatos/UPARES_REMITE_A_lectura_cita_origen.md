# U-PARES-REMITE-A — Lectura a ciegas de los pares cita–origen de G-r

**PARA FIRMAR.** Redactado por la mesa el 10/10/2026, por decisión de la autora del mismo día, después del commit de O2 de
U-OMISIONES-COD (`ded41d50`).
USD 0, sin API. No bloquea nada: ni el re-sellado único ni la tanda 1. Cuándo se despacha lo decide la autora después de S1-ter.

## 0. Qué es y por qué

G-r, de la v7 de U-OMISIONES-COD, corrige el punto y el rol de la procedencia de las entidades cuyo tramo está en una unidad hija. La
nota del 10/10/2026 al pie de la v7 le sumó que los orígenes de una cita se agrupen sin el rol. Las dos cosas cambian `remite_a`: a qué
nodo se atribuye cada cita y a qué nodos de la unidad citada va.

La revisión de O2 controló coherencia, no corrección. El control del destino usa la misma definición que el código (`anclados`,
`r1_referencias.py:1069-1083`), así que mide que el registro y el grafo digan lo mismo, no que la cita vaya al destino correcto (nota de
la mesa al pie de `data/experiment/omisiones_cod/o2/FRENO_O2.md`).

Esta lectura mide la corrección. La lee un lector a ciegas y no la mesa, porque G-r entró a la v7 y el agrupamiento sin el rol lo
recomendó la mesa (revisión de O1).

## 1. Sobre qué

- **El grafo:** r2b de los diez documentos, con el código de HEAD antes de O2 (`40c54830`) y con el de O2 (`710664e9`, `ded41d50`).
- **La población:** las 204 `remite_a` que cambian entre los dos, de
  `data/experiment/omisiones_cod/o2/salidas/remite_a_caso_por_caso_r2b_diez.json` (`head_a_o2`):
  - 137 salen y 67 entran;
  - agrupadas en **74 pares cita–origen** (la evidencia de la cita y el nodo origen): 62 con el destino de G-r, 8 con el origen de G-r y
    4 en `ctacte::1.5.3` (las 76 que salen por la regla D1).
  - Cada par tiene de 1 a 19 aristas: 57 pares con 1, 5 con 2, 1 con 3, 2 con 4, 1 con 6, 2 con 7, 1 con 11 y 5 con 19.
- **Se leen los 74.** No hay muestra.

## 2. La ficha

Una ficha por par, en un orden fijado por semilla (§6). Cada ficha trae:
- la cita, marcada dentro del texto de su unidad (propio y heredado), con la página renderizada;
- la unidad citada;
- el nodo origen: su tipo, su etiqueta y el tramo de la norma que representa;
- una fila por arista del par, en orden fijado por semilla. Cada fila trae el nodo destino: su tipo, su etiqueta y la unidad en la que está
  anclado.

La ficha **no** trae ids, la clase del par, de qué lado está cada arista (si existe con el código de O2 o con el anterior), ni ninguna
mención de G-r ni de la mesa.

## 3. Criterio, sellado antes de leer

**Por arista,** el lector marca:
- **cierta:** el texto sostiene que la regla que representa el nodo origen remite, con esta cita, a lo que representa el nodo destino. El
  destino tiene que ser algo de la unidad citada que la cita nombra;
- **no cierta:** el texto no lo sostiene;
- **no decidible:** el texto no alcanza para decidir; va con su motivo.

**Por par** (lo calcula la mesa, no el lector):
- **correcto:** cada arista que existe con el código de O2 está marcada cierta, y cada una que el código de O2 sacó está marcada no cierta;
- **incorrecto:** alguna arista no coincide;
- **no decidible:** alguna arista es no decidible y ninguna es incorrecta.

## 4. El piso (PENDIENTE de la autora al firmar)

- **Propuesta de la mesa:** límite inferior de Wilson al 95 % de correctos / (correctos + incorrectos) de 0,75 o más, con los no
  decidibles excluidos y reportados. Es el piso de la lectura de la matriz y de (e).
  - Con los 74 decididos admite hasta 11 incorrectos (63 de 74 da 0,7531; 62 de 74, 0,7376). Para otro n, se recalcula con el mismo piso.
- **Propuesta de la mesa:** con más de 15 pares no decidibles (20 %, la proporción de 6 de 30 de la matriz), no se decide con esta
  lectura.
- Se reporta además, sin decidir nada, la cifra por arista (las 204).

## 5. Quién lee, quién adjudica

- **Lee** una sesión nueva, abierta en la carpeta del lector, fuera del repo. Su despacho empieza con el paso 0: «Controlá con `pwd` que la
  carpeta actual sea <la carpeta del lector>; si no lo es, frená sin abrir nada». La plantilla es la de la mesa
  (`plantilla_despacho_lectura_ciega_mesa.md`). El lector sella su planilla (sha256 y hora) y no calcula.
- **Arma el paquete y calcula** la mesa, con scripts: las fichas desde las salidas de O2, sin leerlas para juzgar; el sello; la cifra. La
  mesa **no lee ni adjudica**.
- **Adjudica** la autora: los pares incorrectos y los no decidibles, y 5 correctos sorteados con la semilla del §6. Como en la C4 de la
  matriz, la cifra final es la de su adjudicación.

## 6. Semillas

Se derivan del sha256 del texto firmado de este mandato (los renglones antes de «## Firma»), como en la enmienda 1 y en U-CONF-MATRIZ:
el orden de las fichas, el de las aristas dentro de cada ficha y los 5 correctos para la autora. Las calcula la mesa al firmar y las
anota en la sección «Firma».

## 7. Qué pasa con G-r si no llega al piso (PENDIENTE de la autora al firmar)

- **(a) G-r se mantiene.** Su cifra se declara, los errores se clasifican, y una clase sistemática que se pueda corregir con código va al
  grupo 2, por una regla general. Es lo que rige para → Operacion en U-CONF-MATRIZ.
- **(b) Se revierte solo su efecto sobre `remite_a`:** el agrupamiento sin el rol y la atribución por el punto nuevo.
  - Si el resultado llega antes del re-sellado único, entra al re-sellado, como única excepción al alcance congelado (§29 de la hoja de
    ruta de la mesa).
  - Si llega después, va al grupo 2.
- **(c) Se revierte G-r entero** antes del re-sellado.
- **Recomendación de la mesa: (a).** La lectura no bloquea, y G-r corrige también la procedencia de nodos que no tienen que ver con
  `remite_a` (204 nodos cambian de punto o de rol en diez). Revertirlo desharía correcciones que esta lectura no mide.
- Si llega al piso: G-r y el agrupamiento quedan, y la cifra se declara.

## 8. Escrituras y prohibiciones

- **ESCRITURAS:** `data/experiment/omisiones_cod/pares_remite_a/` (se crea: el armador, las fichas sin la clave, el acta del orden, la
  planilla sellada, el cálculo y el registro); la carpeta del lector, fuera del repo; el scratchpad.
- **PROHIBIDO:** el código, los grafos y sus registros, los mandatos firmados, la API, y commitear.
- **REQUISITOS:** CLAUDE.md §4 (a a l). Mensajes de commit sin unidades, documentos ni mecanismos mientras haya una lectura a ciegas
  pendiente.

## 9. Decisiones al firmar

1. El piso y el tope de no decidibles (§4).
2. Qué pasa con G-r si no llega (§7).
3. La unidad de la cifra: el par, como decidió la autora (los 74); la cifra por arista, solo informativa.

## Firma

PENDIENTE de la autora.
