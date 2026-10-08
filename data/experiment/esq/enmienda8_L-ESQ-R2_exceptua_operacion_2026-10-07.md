# Enmienda 8 a L-ESQ-R2 — la firma (Excepcion, exceptua, Operacion)

**BORRADOR — PENDIENTE DE LA LECTURA DE SU CONDICIÓN Y DE LA FIRMA DE LA AUTORA** · Redactada: 07/10/2026 (mesa revisora), por el hallazgo a de
VERIF-CAP3-COHERENCIA y la decisión de la autora del 07/10/2026 de redactarla.

Enmienda con fecha a L-ESQ-R2 (`data/experiment/esq/enmienda_L-ESQ-R2_2026-09-30.md`, FIRMADA en `4ef7650`). L-ESQ-R2 no se edita: esta enmienda
vive al lado y se lee con ella y con sus enmiendas 2 a 7. No rige hasta la firma, y la firma exige antes la lectura del §2.

## 0. Qué enmienda y por qué

- **Lo que firmó L-ESQ-R2.** La matriz de firmas del perfil r2 (§6) se amplió solo con `condicion_de` → Operacion y → Potestad (§6.3, opción ii;
  `pyd_r2/code/modelos_r2.py`, `AMPLIACION_R2`). La lectura de la matriz (U-ESTUDIO-MATRIZ, `reports/u_estudio_matriz/lectura/resultado_lectura_matriz.md`,
  `c671b52`) dio 5 de 5 correctas para Excepcion `exceptua` → Operacion, pero ese par no se amplió «con esta evidencia» (`4ef7650`, §6.1): con 5
  filas, el límite inferior de Wilson es 0,5655, bajo el piso de 0,75 del protocolo de la matriz. L-ESQ-R2 lo vincula con R6a (el predicado
  `exceptua_operacion` que el laudo del esquema congelado dejó para r2, `laudo_esquema_congelado.md:83`): el par de la matriz cubre ese caso sin
  predicado nuevo.
- **Lo que mostró el grafo.** En el grafo diez r2b de la tanda 0 (`a9631a64…`), de los 238 rechazos por firma del validador r2, 41 son
  `(Excepcion, exceptua, Operacion)` (VERIF-CAP3-COHERENCIA, tarea a). El validador de E1 los rechaza antes de E3 (`reextraccion_v2/e1_extractor/validador_e1.py:506-510`,
  `firma_invalida`): E3 nunca los vio y el ensamblado r2b, que deja entrar solo lo que vio E3, no los puede recuperar por código.
- **Lo que dice el prefijo de E1** (parche de P3b, `prompt_r2b_parche_p3b.json`): «si la norma que la Excepcion exceptúa está en tu unidad,
  conectala: `exceptua` hacia la Restriccion, `exceptua_obligacion` hacia la Obligacion. Si esa norma no está en tu unidad […] emití la Excepcion
  sin esa relación […]: no la conectes con otro elemento del chunk». Las 41 relaciones hacia una Operacion **contradicen esa instrucción**. Pueden
  ser correctas (la excepción exime una operación: «excepto las operaciones de…») o pueden ser el modelo conectando la Excepcion con la Operacion
  del ítem cuando la norma exceptuada está en el encabezado. Por eso esta enmienda se condiciona a leerlas.

## 1. Lo que propone

Ampliar la matriz del perfil r2 con la firma `(Excepcion, exceptua, Operacion)`: una entrada más en `AMPLIACION_R2` (`modelos_r2.py`), sin
predicado nuevo, sin tocar el enum de predicados ni el tool schema (`pyd_r2/generados/tool_schema_r2.json` solo enumera predicados) y **sin tocar
el prefijo de E1** (F06 sería «todo»): la instrucción del parche de P3b sigue como está, y la asimetría (el validador acepta una firma que el
prefijo no pide) se declara.

## 2. Condición para firmarla: la lectura de las 41

Con el protocolo de la matriz de L-ESQ-R2 (§6.1), criterio fijado antes de abrir las fichas: se amplía el par si el límite inferior de Wilson
al 95 % de las correctas sobre las decididas es de al menos 0,75 y los no decidibles no pasan de 6. Con las 41 decididas, hacen falta 37
correctas (Wilson inferior 0,7745). «Correcta» = la Excepcion exime a esa Operacion según el texto de la unidad (la operación es lo que queda
afuera), no a otra norma de la unidad ni a la del encabezado. Fichas sin veredicto (texto propio y heredado, la Excepcion, la Operacion, la
relación rechazada y la instrucción del prefijo), primera lectura de la instancia, segunda lectura a ciegas de la mesa y adjudicación de la
autora sobre las divergencias, como en T4. **Denominador (decisión de la autora del 07/10/2026, noche): las 41 del crudo r2b.** El umbral de 37
correctas vale con las 41 decididas; con no decidibles, rige el piso de Wilson sobre las decididas, como en el protocolo de la matriz. Las
filas de U-ESTUDIO-MATRIZ que no están entre las 41 (M21, M23, M24 y M25, réplicas de KG-Tanda0-Desarrollo-r1; M22 ya está entre las 41) se
leen con las mismas fichas y se informan aparte, sin entrar a la cifra.
- **Si llega al piso:** se firma esta enmienda con la cifra.
- **Si no llega:** no se amplía; los rechazos son correctos según el prefijo y quedan declarados con su cifra (n de 41 correctas) en el
  capítulo del esquema, junto con R6a.

## 3. Qué cambia y qué se reprocesa (si se firma)

- **Código:** `modelos_r2.AMPLIACION_R2` (una tupla). Lo leen el validador de E1 (antes de E3) y el validador r2 del ensamblado: es **F14**
  (cambia la salida validada que ve E3 en las unidades con esa relación) y **F14b** a la vez (`tabla_reprocesamiento.md`).
- **Tanda 1 en adelante:** rige desde la extracción, sin reprocesar nada (la tanda 1 no está extraída).
- **Tanda 0** (decide la autora al firmar): (a) **rige desde la tanda 1** y la tanda 0 declara las relaciones rechazadas como límite, con la cifra
  de la lectura (recomendación de la mesa: E3 no las vio, recuperarlas exige re-verificar esas unidades y eso puede mover otros veredictos); o
  (b) E3 de las unidades afectadas de la tanda 0 antes del re-sellado único (regla de cruce de F14, enmienda 3 al protocolo, §3), con el costo
  declarado antes de correr (del orden de USD 0,01 por unidad a la tarifa de E3; menos de USD 0,50).
- **Shapes y suite:** la shape S3 del perfil r2 no lee `modelos_r2.py` directamente: lee las firmas de `pyd_r2/generados/enums_r2.json`, generado por U-PYD
  desde `modelos_r2.py` con candado de sha256 (`scripts/shapes_validator.py:65-67`, `:1090-1104`, campos `firmas_r2` y `ampliacion_r2`): hay que regenerar ese archivo y
  re-sellar su candado en el mismo cambio. La suite suma un caso (una Excepcion con `exceptua` hacia una Operacion, válida) y su contraparte
  (hacia otro tipo no ampliado, rechazada). Los validadores leen la matriz de `modelos_r2.firma_r2` (`perfil_e1.py:225` para E1;
  `validador_r2.py:1224`, `:1284` para el ensamblado).
- **Figuras:** la figura del esquema final del capítulo 3 suma la flecha Excepcion → Operacion con `exceptua`.
- **Lo que no cambia:** la unión de una excepción de ítem con la norma de su encabezado (otra unidad) no es esta enmienda: es el grupo E de
  U-OMISIONES-COD, en código y sobre lo guardado, si el diagnóstico U-DIAG-CAP3-GRAFO lo sostiene. Tampoco cambia R6a ni el predicado
  `exceptua_operacion`, que no se crea.

## Decisiones de la autora (07/10/2026, noche)

- **La condición del §2 sigue:** la enmienda se firma solo si la lectura de las 41 da al menos 37 correctas.
- **Tanda 0: opción (a) del §3.** La enmienda rige desde la tanda 1; la tanda 0 declara las relaciones rechazadas como límite, con la cifra
  de la lectura. No hay E3 de las unidades afectadas de la tanda 0. **[08/10/2026, la autora cambia esta decisión (barrido de límites,
  VAL-03b)]** Si la lectura llega a 37 y la enmienda se firma, las 21 unidades de la tanda 0 con las 41 relaciones rechazadas reciben E3
  dentro del re-sellado único (etapa R0, USD 0,2306 estimados), por la enmienda 7 al protocolo entre tandas (BORRADOR,
  `docs/enmienda7_protocolo_entre_tandas_2026-10-08_excepcion_tanda0_en_el_resellado.md`). Si no llega, rige lo de arriba.
- **Quién lee y cuándo.** Primera lectura: la instancia de U-DIAG-CAP3-GRAFO, con el criterio sellado antes de generar las fichas
  (`criterio_41_exceptua_operacion.md`, sha256 `92688681…`, sellado el 07/10/2026 a las 18:39:26; fichas sin veredicto generadas a las
  18:41). Segunda lectura a ciegas: la mesa, sin abrir la primera. Adjudicación de las divergencias: la autora. La cifra sale después de
  la adjudicación. Todo esto antes del despacho de U-OMISIONES-COD, que aplica la tupla solo si esta enmienda se firma, y antes de la
  extracción de la tanda 1.
- **Denominador, DECIDIDO por la autora el 07/10/2026 (noche): 41**, con las 4 de U-ESTUDIO-MATRIZ aparte (texto corregido en el §2). Lo que
  sigue es el análisis con que se decidió. Las fichas son 45: las 41 relaciones del crudo r2b y 4 filas de
  U-ESTUDIO-MATRIZ que no estaban entre ellas (M21, M23, M24 y M25, réplicas en memoria de KG-Tanda0-Desarrollo-r1, `eab2fdd0`; M22 ya está
  entre las 41). El §2 suma esas filas a la lectura, pero da el umbral solo para 41 decididas; es un error propio de la redacción. Con el
  piso de Wilson al 95 % sobre las decididas, hacen falta 37 correctas con 41 decididas, 40 con 45, 34 con 38 y 32 con 35. Recomendación
  de la mesa: computar la cifra sobre las 41 del crudo r2b, que son la población que la enmienda cambia, e informar aparte las 4 de la
  matriz, que vienen de otro grafo y ya se leyeron en U-ESTUDIO-MATRIZ. El piso se aplica sobre las decididas, como en el protocolo firmado
  de la matriz, y los no decidibles no pueden pasar de 6. Con las 41 decididas, el umbral es 37, la cifra que fijó la autora.

## Firma

BORRADOR — PENDIENTE de la lectura del §2 y de la firma de la autora.
