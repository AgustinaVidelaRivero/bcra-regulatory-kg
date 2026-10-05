# Enmienda 6 a L-ESQ-R2 — el sujeto que el texto no identifica: sin alcance, cuarentena; con alcance, el rol del documento

**BORRADOR — PENDIENTE DE FIRMA** · Redactada: 2026-10-04.

Enmienda con fecha a L-ESQ-R2 (`data/experiment/esq/enmienda_L-ESQ-R2_2026-09-30.md`, FIRMADA en `4ef7650`;
sha256 del texto firmado `66c4a1b9…`). L-ESQ-R2 no se edita: esta enmienda vive al lado y se lee junto con
ella, con sus notas posteriores a la firma y con las enmiendas 2 (`5f9a731`), 3 (`8d01b04`), 4 (`5c58f38`) y
5 (`3a4b980`). La enmienda 7 está en BORRADOR. Por la regla k de CLAUDE.md §4, toda cita de L-ESQ-R2 es del
texto firmado (`git show 4ef7650:data/experiment/esq/enmienda_L-ESQ-R2_2026-09-30.md`), con su línea.

No rige hasta la firma. La autora la firma con dos mediciones a la vista, las dos sobre el crudo de
U-REEXT-T0: la de R2 de U-RERESOL-CAT (§A.2) y la lectura de la parte B (§B.2).

Tiene dos partes. La parte A, para los documentos sin alcance, rige desde la firma. La parte B, para los
documentos con alcance, es condicionada: rige solo si su lectura llega al piso.

Versiones del borrador: la primera, con la regla del colectivo, quedó en `28ec100`; la segunda, con la
relación sin mención, en `1f8d624`; la tercera, con la parte B, en `97c21e4`. Esta dice quién hace la lectura
de la parte B y qué pasa si su población tiene menos de 30 relaciones (decisiones de la autora del
04/10/2026).

---

## 0. Qué enmienda y por qué

**Lo que dice L-ESQ-R2.**

- §3.2, resolución por relación (`:565-570`): R1, label o alias exacto; R2, slug, singular y alias entre
  paréntesis; «R3: expresión colectiva → sujeto por defecto del TO»; «R4: sugerencia del modelo»; y lo
  ambiguo o sin resolver, al registro.
- §3.3, punto 5 (`:580-582`): «la regla textual gana solo con coincidencia exacta de label o alias (R1). Con
  las reglas aproximadas (R2 y R3) gana la sugerencia del modelo».
- Decisión del 30/09 (`:593-594`): la lista de expresiones colectivas de R3 es «una lista inicial cerrada,
  tomada de la redacción del propio prompt», «que se amplía en código con las menciones de r2b».

**Lo que hace el código** (`data/experiment/reextraccion_v2/corpus_v2/r1_e4.py`, en `9f6361e`).

- La lista es `("entidades", "sujetos obligados")`, comparada sin el artículo inicial (`:306`).
- Si la mención verificada es una expresión de la lista y el documento tiene alcance, R3 devuelve su rol. Si
  no lo tiene, devuelve el motivo `colectivo_sin_sujeto_por_defecto` (`:377`).
- Si la relación no trae mención, no se aplica ninguna regla textual y el motivo es `sin_mencion`.
- En la decisión, después de R1 gana la sugerencia del modelo si la hay (`:418`).
- Toda relación de sujeto del grafo sale de una relación que emitió el modelo. Una norma para la que el
  modelo no emitió ninguna queda sin `aplica_a`.

**Lo que se encontró.**

- De los 157 documentos, 86 no tienen alcance (`docs/plan_tesis.md:404`). En la tanda 0 es uno solo, docvig.
- En KG-Tanda0-Diez-r2a, docvig tiene 20 relaciones con sujeto: 17 resueltas por la sugerencia del modelo y 3
  en cuarentena. Las 17 no traen mención. Sus sugerencias van a seis ids distintos:
  `Sujeto_entidad_financiera` (7), `Sujeto_cliente` (3), `Sujeto_rol_alcance_lavdin` (3), que es el rol de
  alcance de otro documento, `Sujeto_sujeto_regulado` (2), `Sujeto_empresa_no_financiera_emisora_de_tarjetas`
  (1) y `Sujeto_entidad_cambiaria` (1) (`data/experiment/reresolucion_catalogo/salidas/r1_medicion.json`,
  clave `docvig`, `c98093a`).
- docvig no declara su alcance en ningún pasaje. Su índice tiene cuatro secciones y ninguna es de alcance.
  Nombra tres clases en lugares distintos: «las casas operativas de las entidades financieras» (puntos 1.2.3,
  2.1.3 y 2.2.3), «Recaudos especiales de las entidades financieras y cambiarias» (título del punto 3.6) y
  «las empresas no financieras emisoras de tarjetas de crédito y/o compra» (sección 4). En los puntos 3.4 y
  3.5 dice «las entidades», cuatro veces, sin decir cuáles. Queda sin alcance en U-REEXT-T0 (decisión de la
  autora del 04/10/2026).
- Con la mención obligatoria, menos normas llevan sujeto. En el crudo de la pareada de P4 de U-PROMPT-R2,
  las normas (Obligacion, Restriccion y Potestad) con `aplica_a` son 129 de 143 con el prefijo sellado y 111
  de 157 con el de P3b-2. Con el punto e de P3c, que pide no emitir la relación cuando el texto no nombra al
  sujeto, quedarían 96 de 157 (`data/experiment/prompt_r2/p4/salida/resultados_p4.jsonl`, `2ed47a0`; conteo
  de la revisión del FRENO P3c-1, `docs/plan_tesis.md:400`). En KG-Tanda0-Diez-r2a son 3.158 de 3.694
  (`data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2a/r2/kg.json`).
- El alcance del TO no está en ningún nodo del grafo: el TextoOrdenado no lo lleva como propiedad ni como
  arista.

**Por qué una enmienda.** Cambia una regla de un texto firmado, el orden del §3.2 y el punto 5 del §3.3, y
agrega una relación derivada con un umbral de entrada.

---

# Parte A — documentos sin alcance

## A.1 Qué decide

El principio: en un documento sin alcance, la sugerencia del modelo no reemplaza a un sujeto que el texto no
identifica.

1. **Expresión colectiva.** Cuando el documento no tiene alcance y la mención verificada de la relación es
   una expresión colectiva de la lista de R3, la sugerencia del modelo no se aplica. La relación va a
   cuarentena, con el motivo `colectivo_sin_sujeto_por_defecto`.
2. **Relación sin mención.** Cuando el documento no tiene alcance y la relación no trae mención, la
   sugerencia del modelo tampoco se aplica. La relación va a cuarentena, con el motivo `sin_mencion`.
3. **El registro.** En los dos casos, la fila guarda la sugerencia (`sujeto_id_modelo`).
4. **El orden.** R1 sigue primero: un label o un alias exacto gana también en un documento sin alcance. Las
   dos reglas van después de R1 y antes de R4.
5. **Cuando el documento recibe alcance,** en el catálogo de resolución o en una release:
   - las filas de la regla 1 se resuelven por R3 con `reresolver_registro`, sin volver a extraer;
   - las normas de las filas de la regla 2 pasan a la parte B, si rige.
6. **Restricción para el crecimiento del catálogo.** Ningún label ni alias puede ser igual a una expresión
   colectiva de la lista, porque R1 se evalúa antes y le ganaría a la regla. Hoy no hay ninguno.

## A.2 La medición de R2 (PENDIENTE)

**La lista de expresiones colectivas** de la regla 1 deja afuera el singular.

- **Por texto** (aproximación sobre el texto propio de la E0 de los diez TOs; no son menciones de E1): la
  lista cubre 231 de 1.088 apariciones de una forma colectiva. Fuera quedan «la entidad» (806), «el sujeto
  obligado» (33), «cada entidad» (10) y otras cinco formas (8). No cuenta las formas seguidas de
  «financiera(s)» o «cambiaria(s)», que nombran una clase (`r1_medicion.json`, clave `colectivos`).
- **Una primera mirada con menciones reales** (brazo nuevo de la pareada de P4, 76 fichas, con el prefijo de
  P3b-2; no es la medición): de 123 menciones de sujeto, 45 son «las entidades», 31 de ellas verificadas, y
  14 son «la entidad», las 14 verificadas (`data/experiment/prompt_r2/p4/salida/analisis_p4.json`, `2ed47a0`).

**Las relaciones sin mención** dependen del prefijo. Con el de P3c, la regla 2 actúa solo sobre las
relaciones sin mención que el modelo emita igual.

**Medición que falta, sobre el crudo de U-REEXT-T0** (la hace R2 de U-RERESOL-CAT), en los documentos sin
alcance:

| Qué se mide | Relaciones que pasan de la sugerencia del modelo a cuarentena | Ids que sugería el modelo |
|---|---|---|
| Regla 1, con la lista de hoy | PENDIENTE | PENDIENTE |
| Regla 1, con el singular y con «cada», «esta(s)», «dicha(s)» y «tal(es)» | PENDIENTE | PENDIENTE |
| Regla 2, relaciones sin mención | PENDIENTE | PENDIENTE |
| Aparte: relaciones con una mención que no verifica | PENDIENTE | PENDIENTE |

Y, en los documentos con alcance: en cuántas relaciones cambia el resultado de R3 o la marca de desacuerdo si
la lista se amplía. Ampliar la lista de R3 cambia R3 también ahí.

Con esas cifras la autora decide, al firmar, si la lista de la regla 1 incluye el singular y si es la misma
que la de R3.

## A.3 Efectos declarados

- **En la tanda 0,** las dos reglas actúan solo sobre docvig.
  - Sobre el crudo de r2a, la regla 1 cambiaría 0 relaciones y la regla 2, las 17 que resolvió el modelo:
    ninguna trae mención (`r1_medicion.json`, clave `docvig`).
  - La cifra real sale del crudo de U-REEXT-T0, que trae la mención y corre con el prefijo de P3c.
- **En el escalado,** actúan sobre los documentos sin alcance: sus menciones colectivas van a cuarentena, con
  un nodo por documento, porque el merge entre TOs renombra los propuestos repetidos
  (`corpus_v2/r1_invariantes.py:124`).
- **Reprocesamiento.** Es un cambio de las reglas de sujetos por relación: fila F15d de la tabla, «solo código
  sobre lo guardado» (`data/experiment/mantenimiento/tabla_reprocesamiento.md:157`). No cambia ningún request.

## A.4 Límites declarados y lo que queda abierto

- **Menciones que no verifican.** Las reglas no las alcanzan: sin verificación no hay regla textual, y gana el
  modelo. R2 las cuenta aparte, en la tabla de A.2.
- **Una relación sin mención en cuarentena no tiene con qué nombrar su nodo.** R2 dice, antes de la firma, cómo
  queda: una fila en el registro sin nodo, o un nodo por documento.
- **Si la parte B no rige,** las filas de la regla 2 de un documento que recibe alcance no tienen mención que
  re-resolver. Queda a decisión de la autora: se aplica la sugerencia guardada, se re-extrae el documento o
  siguen en cuarentena.
- **El alcance de docvig** solo de resolución, inferido del título de su punto 3.6, no se decide acá: se
  decide con la medición de R2.

## A.5 Implementación, después de la firma

- `corpus_v2/r1_e4.py`, `resolver_relaciones_r2` (`:383`): una rama nueva antes de `elif modelo:` (`:418`).
  Si el documento no tiene alcance y el motivo es `colectivo_sin_sujeto_por_defecto` o `sin_mencion`, la
  sugerencia no se aplica. El registro ya guarda `sujeto_id_modelo` (`:451`).
- **Sin alcance** quiere decir sin entrada en `rol_por_to`. `ri2_ci.pdf` tiene entrada, con dos clases y sin
  rol: tiene alcance, y las reglas no lo tocan.
- Casos nuevos en el selftest de la resolución, con un documento sin alcance.
- Control: en los documentos con alcance, `resolucion_sujetos.jsonl` sale byte a byte igual.
- La implementa R2 de U-RERESOL-CAT, con esta enmienda firmada.

---

# Parte B — documentos con alcance (condicionada)

## B.1 Qué decide

1. **La relación derivada.** En un documento con alcance, una norma (Obligacion, Restriccion o Potestad) sin
   relación de sujeto con mención recibe `aplica_a` hacia el rol de alcance de su documento.
2. **Marcada como derivada.** La crea el código en el ensamblado; no la emite E1. Lleva una marca propia que
   dice que viene del alcance del documento y no del texto de la norma, y no lleva mención. La marca tiene
   que llegar al agente (borrador de `docs/mandatos/UNAV_DISENO_navegacion_agente.md`).
3. **Precedencia.** Si el modelo emite igual una relación sin mención, con su sugerencia, en un documento con
   alcance gana la derivada. La sugerencia no se aplica y queda guardada en `resolucion_sujetos.jsonl`.
4. **Lo que no toca.**
   - Las relaciones con mención verificada: R1, R2 y R3 siguen como hoy.
   - Las relaciones con una mención que no verifica: sigue R4. Se cuentan aparte.
   - `ejecuta`: el alcance no es el ejecutor por defecto.
5. **Si esta parte no rige,** en los documentos con alcance queda la regla de hoy: R4.

## B.2 La condición: una lectura posterior a U-REEXT-T0 (PENDIENTE)

- **Población.** Las relaciones que esta parte crearía sobre KG-Tanda0-Diez-r2b. La arma R2-1 de U-RERESOL-CAT
  por simulación, sin implementar la parte B.
- **Muestra.** 30, que R2-1 sortea con una semilla declarada antes de leer. Si la población tiene menos de 30
  relaciones, se leen todas.
- **Qué se lee.** Cada una contra el texto de su unidad y su texto heredado. Es correcta si el rol de alcance
  del documento es a quien se aplica esa norma.
- **Piso.** El límite inferior del intervalo de Wilson al 95 %, en 0,75 o más.
  - Con 30 leídas son 28 correctas (0,787); con 27 no llega (0,744).
  - Con menos de 30, la misma regla sobre las leídas: de 25 a 29 admite dos incorrectas; de 19 a 24, una; de
    12 a 18, ninguna.
  - Con menos de 12 no puede llegar ni con todas correctas (con 11 da 0,741): la parte B no rige.
- **Quién.** La lectura la hace R2-1, asistida y declarada, con revisión de la autora.

| Qué se mide | Valor |
|---|---|
| Normas sin relación de sujeto con mención, en documentos con alcance | PENDIENTE |
| De esas, con una relación sin mención que el modelo emitió igual | PENDIENTE |
| De esas, con una sugerencia distinta del rol de alcance | PENDIENTE |
| Correctas en la muestra de 30 | PENDIENTE |

Si no llega al piso, la parte B no rige y la parte A no cambia.

## B.3 Efectos declarados

- **Las normas con sujeto** vuelven a subir. Las cifras de referencia están en el §0; la real sale de la
  primera fila de la tabla de B.2.
- **El sujeto derivado es el del documento, no el de la norma.** Una norma dirigida a un tercero que el texto
  no nombra recibiría el rol equivocado: eso es lo que mide la lectura.
- **Reprocesamiento.** Solo código sobre lo guardado. No cambia ningún request.
- **Las shapes y la suite.** La shape que cuenta las normas sin `aplica_a` da otro número. No se editan acá:
  el estado esperado lo sella la autora.

## B.4 Límites declarados

- **`ri2_ci.pdf`** tiene alcance con dos clases y sin rol: la derivada no tiene un destino único. No está en la
  tanda 0. Queda fuera de esta parte hasta que se decida.
- **Excepcion y Operacion** también admiten `aplica_a`, y esta parte no las cubre.

## B.5 Implementación, solo si rige

- En el ensamblado, después de la resolución por relación. La arista lleva su marca en `rol_fuente`, como la
  `establecida_en` derivada (`data/experiment/pyd_r2/code/modelos_r2.py:190` y `:632`), y su método en
  `metodo_resolucion`.
- La vista del agente y la exportación a Neo4j: U-NAV-DISENO.
- La implementa R2-2 de U-RERESOL-CAT, con esta enmienda firmada y solo si la lectura llegó al piso. Dónde va
  y qué archivos toca lo propone R2-1, y la autora lo aprueba en su «seguí».

---

## Qué no cambia

- El texto de L-ESQ-R2, sus notas y sus enmiendas 2 a 5.
- R1, R2 y el calificador, en todos los documentos. R3, en los documentos con alcance.
- El prefijo de E1, su tool schema, el catálogo de sujetos y sus candados.
- El paso de lectura del alcance entre tandas, que asigna solo clases que ya existen
  (`docs/enmienda4_protocolo_entre_tandas_2026-10-04_crecimiento_del_catalogo_y_alcance.md`, BORRADOR).

## Firma

BORRADOR — PENDIENTE DE FIRMA de la autora. Se firma con las dos mediciones: la de R2 de U-RERESOL-CAT (A.2)
y la lectura de la parte B (B.2).
