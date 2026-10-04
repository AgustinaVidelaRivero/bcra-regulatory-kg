# U-PROMPT-R2 — FRENO P4, final (prueba pareada)

**La pareada compara release contra release:** el prefijo sellado `v3_b54` con la E0 legada, frente al prefijo nuevo
`3817de475c93` con la e0-r2. No compara el prefijo solo. Las diferencias no se atribuyen al prompt o a E0 por separado,
salvo donde la ficha lo permite: la tabla de `cap::1.2` solo existe serializada en la e0-r2.

04/10/2026. HEAD `9f6361e` (C2 de U-R2-CODIGO-2), con la enmienda 5 firmada en `3a4b980`. Tope USD 2 (decisión 18).
Gasto real: **USD 1,1086**. Sin commit. El detalle está en `p4/` y en el paquete de revisión.

**Fuentes.** Leí las notas al pie del mandato hasta la del «seguí» de P4, que coincide con el mensaje.
- **El «seguí»** confirma las dos cosas que la nota dejaba a la autora: el estrato de listas de 8 unidades y la
  medición e.
- **Diferencia menor:** la nota del 04/10/2026 sobre la enmienda 4 dice que el arreglo de la cadena de P3 está «PENDIENTE»
  de commit, pero está en `f3922d8`, del mismo minuto. Mandan los archivos.

## 1. Muestra y E0

- **Semilla:** `U-PROMPT-R2:P4:2026-10-04`, en `p4/muestra_p4.py`; salida en `p4/salida/muestra_p4.json`.
- **Grupos:**
  - 40 sorteados, 8 por estrato, con las definiciones del censo de P1;
  - 9 fijos: los cinco de control, `cla::5.1.1::intro` y `cap::8.5.1` a `8.5.3`;
  - 8 de F1;
  - 8 de listas de excepciones;
  - 8 fuera de muestra;
  - los 3 encabezados de ctacte de la pata de E3.
- **Listas de excepciones.** Las elegí por lectura (5 listas, 8 ítems) y quedaron escritas antes de correr, en
  `p4/estrato_listas_excepciones.md` (sha `798adbf2…`, 04/10/2026 17:11). Leí los 8 ítems y no reemplacé ninguno.
- **E0 de la tanda 0.** La de `f8dedd4` (`salida_tanda0_r2/`). De la muestra, solo `ric::4.3.3` es uno de los 6 chunks
  que cambian en la E0 de C2 (`salida_tanda0_r2b/`).
- **E0 fuera de muestra.** La produje en el scratchpad con `p4/e0_fuera_p4.py`, sin versionarla. En los cuatro TOs, la
  e0-r2 da los mismos `chunks_<to>.json` que la legada (sha256 iguales).

## 2. Costo y caché

| | USD |
|---|---:|
| Proyección antes de correr (`p4/salida/proyeccion_p4.json`) | 1,17 central / 1,58 alta |
| E1, brazo nuevo (76 llamadas) | 0,9239 |
| E1, brazo sellado por la API (16) | 0,1162 |
| Pata de E3 (5 llamadas) | 0,0616 |
| Reintento de E1 de la pata (1) | 0,0068 |
| **Total** (`p4/salida/gasto_p4.json`) | **1,1086** de tope 2 |

- **Brazo sellado de la tanda 0:** las 60 respuestas salen de la caché de la corrida (USD 0), y son iguales al crudo de
  `salida_dirigida`.
- **Sin incidencias:** ningún error, corte ni reintento por forma.
- **Namespaces:**
  - nuevo: `e1_extraccion|cv=e1-extractor-v1-p3817de475c93|think=0`;
  - sellado: `e1_extraccion|cv=e1-extractor-v1-p54a111e2175f|think=0`;
  - E3: `e3_verificacion|cv=e3-verificador-v1-p21a836c7de6d|think=0`.
- **Claves** (`claves_antes.json` y `claves_despues.json`):
  - antes: las 60 selladas de la tanda 0 estaban en su base y las 92 que se pagaron, en ninguna;
  - después: las 92 están en la base de P4.
- **Prefijo nuevo:** la primera llamada midió 26.309 tokens de escritura de caché (la recta de P1 daba 28.568). Hubo una
  escritura por corrida (decisión 4).

## 3. Tabla pareada (lectura asistida, PENDIENTE de revisión de la autora)

Marcas: `p4/marcas_p4.py`. Razones: `p4/lectura_p4.md`. Tabla: `p4/salida/tabla_pareada_p4.json`.

**Los 40 sorteados.**

| Dimensión | Fichas | Sellado cumple (Wilson 95 %) | Nuevo cumple (Wilson 95 %) | Solo nuevo / solo sellado |
|---|---:|---|---|---|
| Umbral con tramo literal verificado | 17 | 0 [0,000; 0,184] | 14 [0,590; 0,938] | 14 / 0 |
| Mención verificada | 29 | 1 [0,006; 0,172] | 22 [0,579; 0,878] | 21 / 0 |
| Omisiones con categoría y tramo | 14 | 0 [0,000; 0,215] | 9 [0,388; 0,837] | 9 / 0 |
| `condicion_de` con firma nueva | 1 | 1 | 1 | 0 / 0 |
| Destino de `limita` | 6 | 3 [0,188; 0,812] | 5 [0,436; 0,970] | 2 / 0 |

- **Las tres primeras son estructurales para el sellado:** el crudo v3 no trae tramo de umbral, ni mención de un
  sujeto del catálogo, ni categoría de omisión.
- **El nuevo no cumple umbral en 3 fichas** (`cap::4.3.3.2`, `cap::6.2.2.4` y `cap::7.1.2`).
- **Menciones:** 14 de las 15 que no verifican son «las entidades», un sujeto que el texto no nombra.

**Aparte** (la tabla los trae por grupo):
- fijos: umbral 5/5 en el nuevo; tabla de `cap::1.2`, el sellado la invierte y el nuevo copia bien;
- listas: mención 4/4 en el nuevo;
- F1: mención 5/5;
- fuera de muestra: mención 6 de 7, umbral 1/1.

## 4. Contadores del validador (`p4/salida/analisis_p4.json`, 76 fichas por brazo)

| | Sellado | Nuevo |
|---|---|---|
| Vocabulario retirado | 41 claves heredadas de v3; 21 `sujeto_propuesto` leídos como mención; 32 omisiones v3 leídas como nota | 0 |
| Fuera de lista | 1 | 3 |
| Tramo de entidad | 310 sin tramo | 302 exacta, 2 por tokens, 35 no |
| Mención | 136 ausentes, 16 exactas, 2 no | 107 exactas, 1 por tokens, 15 no |
| Omisiones | 32 sin categoría ni tramo | 72 con categoría: 48 exactas, 22 no, 2 ausentes |
| Tramo de umbral | — | 80 exacta |

**De las 22 omisiones que no verifican,** 7 son tramos del texto heredado. El validador verifica el tramo de la omisión
solo contra el texto propio (`pyd_r2/code/validador_r2.py:1316`), a diferencia del de la entidad: es un límite.

## 5. Mediciones

- **a. La modalidad.** El código clasificó 2 recomendaciones (`lingob::6.2.4.3` y `adrei::4.3.1.2`), las dos bien.
  - No clasificó ninguna consecuencia.
  - **La lectura de muestra:** leí las 11 fichas cuyo texto tiene una forma de la lista y cuyo brazo nuevo no copió
    nada.
    - Ninguna es una recomendación.
    - Una es una consecuencia dudosa: `ext::10.4.2.7`, la conformidad previa para quien tiene condenas cambiarias.
    - Las otras 10 no son consecuencias. Las formas que las marcan aparecen con otro sentido: «incumpl» en 5,
      «suspen» en 2, y «inhabilit», «sancion» y «cargo» en 1 cada una.
  - **Las formas:** no falta ninguna. Como detectores sobre el texto sobran, pero el clasificador se aplica al tramo
    copiado, no al texto.
- **b. Condicion de ítem sin `condicion_de`.** Son 6. La norma está en otra unidad en 1 (`ext::3.5.6.9`). En las 5 de
  `ext::3.16.3.6`, la norma está en la misma unidad.
- **c. Salida de a, b y h.**
  - a y b: 43 caracteres copiados en 2 entidades.
  - h: 2 mini-chunks a mitad de oración. Ninguno necesitó el orden de lectura para verificar; su salida va de 311 a
    228 tokens y de 413 a 732.
- **d. `cla::5.1.1.1`.** El prefijo nuevo **no emite la Excepcion**: declara el encabezado como `meta_normativo`.
  `cla::5.1.1::intro` tampoco emite nodo. Por el mandato, la condición 10 de la tanda 1 vuelve a la autora antes de
  U-REEXT-T0.
- **e. Tokens de salida por carácter de texto propio** (unidades de 3.000 caracteres o más).
  - En P4 hay 6. La mediana es 0,674 con el sellado y **1,175** con el nuevo; el nuevo es mayor en 5 de 6.
  - La referencia de 0,86 se reproduce: es la mediana sellada de las 40 unidades de ese tamaño de la tanda 0, con la
    E0 legada.

## 6. Pata de E3 y otros hallazgos

- **Pata de E3.** `ctacte::8.3::intro` y `8.4::intro` quedan aceptadas con residuales: E3 reclama la omisión
  `meta_normativo` por mal categorizada, como admite la NOTA, y la guarda la exime. `ctacte::6.4.7::intro` queda
  aceptada tras el reintento y `adrei::4.3.1::intro`, `completo_ok`. Ninguna quedó con la marca `copia_nota_e3`.
- **Regla f, en las listas.** El nuevo emite la Excepcion compuesta en 4 de 8; el sellado, en 2. Las 4 del nuevo emiten
  igual una `exceptua`: en tres queda colgante y en `ext::13.4.4` va a la norma del encabezado, repetida en el ítem. Los
  otros 4 quedan como Condicion u Operacion.
- **`cap::6.2.2.6`.** El nuevo ata el 100 % «entre zonas 1 y 3» a la banda 2-3: es la asociación mal hecha que prevé la
  nota del 03/10/2026, `:345-347`. Por esa nota, `cap::tabla037` va a `TABLAS_RESIDUALES_FORZADAS`, que no está en las
  escrituras de P4.
- **Lo que el nuevo corrige del sellado:**
  - la tabla invertida de `cap::1.2`;
  - las bandas corridas de `cap::2.12.2.4`;
  - en `cap::8.5`, el sellado no emitía los límites mínimos de los tres ítems.
- **Defectos del nuevo:**
  - `ext::3.3.3.1` trae una entidad sin `type`;
  - en `cla::5.1.1.1`, la etiqueta de la Condicion no coincide con su descripción;
  - en `cap::8.5.1`, expande COn1 como «capital operacional computable».

## 7. Recomendación para el tope de U-REEXT-T0 (hoy USD 72)

La re-estimación de `p4/costo_real_p4.py` cambia tres cosas respecto de P1: el prefijo medido, la entrada medida (×1,161)
y la salida medida. La salida va de dos maneras:

| Salida | Central | × 1,4 |
|---|---:|---:|
| Sin ponderar, 60 chunks (×1,276) | 49,41 | 69,17 |
| Ponderada por estrato (×1,007) | 45,00 | 63,00 |

- **La comparación:** P1 suponía ×1,3355, y la estimación central que fijó los 72 era 50,74.
- **Recomiendo mantener USD 72:** cubre las dos cotas con el factor 1,4.
- **Un riesgo distinto del costo:** con 1,175 tokens por carácter, una unidad de unos 7.000 caracteres propios pasa
  los 8.192 tokens del primer intento.

## 8. Controles

- **Doble corrida:** los 8 scripts de USD 0 corrieron dos veces sobre una copia sin enlaces (`cierre_p4.sh`, en el
  paquete). Las 10 salidas son iguales entre corridas y a `p4/salida/`.
  - La tabla se regeneró tras corregir el redondeo de Wilson (`-0.0` → `0.0`).
- **El repo:** durante el cierre cambiaron 4 documentos de otra sesión: `docs/checklist_pre_escalado.md`, el mandato
  de U-REEXT-T0, el plan y el tablero. Mis escrituras son solo `data/experiment/prompt_r2/p4/` y este freno.
- **`.pyc`:** 0 nuevos.
- **Código:** P4 no tocó código del pipeline.

## 9. Pendiente de la autora

1. Revisar la lectura asistida (`p4/lectura_p4.md`, `marcas_lectura_p4.json`).
2. La condición 10 de la tanda 1: el prefijo no emite la Excepcion de `cla::5.1.1.1`.
3. `cap::tabla037` a la lista de tablas residuales, como prevé la nota; queda fuera de las escrituras de P4.
4. Regla f: la Excepcion compuesta sale en 4 de 8, y con `exceptua` en las 4.
5. Las menciones «las entidades» que el texto no nombra (14) y la verificación del tramo de las omisiones solo contra
   el texto propio (7).
6. El tope de U-REEXT-T0: recomiendo mantener USD 72.
7. Las 92 respuestas pagadas viven en la base de P4, en el scratchpad. U-REEXT-T0 podría reusar las de los chunks cuya
   E0 no cambia. Llevarlas a la caché del repo es una escritura fuera de P4.
8. El commit de P4.
