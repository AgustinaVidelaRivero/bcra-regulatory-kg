# U-PROMPT-R2 · P1 — Diseño del prefijo r2 y del mensaje de E1 (FRENO P1)

**Estado.** Lo redacté el 03/10/2026: HEAD `b901f6d` al empezar y `f8cf89a` al cerrar, con tres commits de la
autora en el medio (`d69b11f`, `ebd7b1e` y `f8cf89a`). USD 0: ninguna llamada a la API y Neo4j no se
usa. Sin commit (el commit es de la autora). Es el avance de P1 que no depende de la unidad 9, como
precisa la nota posterior a la firma del mandato (`docs/mandatos/UPROMPT_R2_prefijo_nuevo.md`, «NOTAS
POSTERIORES A LA FIRMA», `ebd7b1e`): P1.a sin el mensaje de tablas, P1.b, y la parte de P1.c y P1.d que
sale del crudo guardado de la tanda 0. **Completado el mismo día sobre `f8dedd4`**, con la E0 e0-r2 que
versionó la M1 de U-MED-R2A: el bloque de tablas del mensaje (§4.2), la NOTA de E3 y su censo (§4.3) y
los tokens de entrada del mensaje nuevo (§7). Lo que queda pendiente está en §11. El FRENO P1 se hace
después de la revisión del FRENO M2 de U-MED-R2A. **Ajustes de la revisión del avance 2**
(03/10/2026, decisiones de la autora): aviso de tablas por tipo de riesgo y lista de tablas forzadas a
residual en código (§4.2), NOTA de E3 con la omisión `tabla` de esas tablas (§4.3), casos fijos de P4 con
los ids reales (§7, §10), hashes con script (§1) y tandas no aditivas (§7). **Decisiones de la autora de la
revisión del avance 4** (03/10/2026, HEAD `a807136`): la regla del encabezado de lista (F1-A de
U-DIAG-PROCESO) entra al borrador (§4.5, con su costo en §7 y su medición en P4), y la traducción de la forma
de salida en `validador_e1.py` queda autorizada para P2 (§10.2, punto 4). Las dos están asentadas en la nota
del 03/10/2026 al pie del mandato (`a807136`). **Pedidos de la revisión del avance 5** (03/10/2026, HEAD
`8edd732`), en el §4.5:
- la unidad del encabezado y E3 en la tanda 0, y cuántos encabezados quedarían vacíos con la regla 1;
- dos salidas para E3, especificadas: (a) una NOTA y (b) la guarda LAUDO B ampliada;
- dónde se mide `BKL-0035`.
En el §10.1, punto 18, la clasificación de los encabezados en línea de título, con su tratamiento por tipo.
**FRENO P1** (03/10/2026, HEAD `28e06fb`), con las decisiones de la revisión del avance 6:
- el tratamiento por tipo del encabezado entró a R30, R16 y R11, y la NOTA de E3 quedó alineada (§4.5);
- las salidas (a) y (b) para E3 quedaron aprobadas, con la condición de listar las exenciones (§4.5);
- `ctacte::6.4.7::intro` entró como caso de control, y P4 suma la pata de E3 (§4.5 y §7);
- el límite de la proxy de vacíos quedó declarado (§4.5);
- la instrucción de umbrales quedó ajustada con la columna r2a (§4.6);
- la frecuencia, con M2.c (§9).
Qué decide la autora en el FRENO: `data/experiment/prompt_r2/freno_p1.md`.

**Decisiones del FRENO P1** (la autora, 03/10/2026):
- aprobó el texto del prefijo y del mensaje, con dos ajustes (§2):
  - R8 suma la Condicion sin `condicion_de` cuando lo que condiciona no está en la unidad, y R30 remite a esa
    regla;
  - R14 suma que la Comunicacion sigue siendo una entidad con su `referencia` desde el TextoOrdenado. La fila
    `referencia` está en el prefijo;
- frecuencia: variante B. M3.d apunta a lo mismo, según la autora;
- topes: USD 2 para la pareada y USD 69 para U-REEXT-T0;
- puntos 1, 2, 3, 5, 8 y 10 del §10.1, confirmados como los recomendé. El elemento sin valor del límite
  relativo va en `validador_r2.py`;
- marca `guarda_ampliada`: no se agrega. El reporte de U-REEXT-T0 lista como exenciones de la ampliación los
  faltantes eximidos de tipo distinto de `enumeracion_incompleta` (§4.5);
- la enmienda a LAUDO B está firmada y commiteada en `0061244`.

Con los ajustes se re-corrieron la no-filtración y los hashes (§1 y §5). P2 congeló la variante B en
`e1_extractor/prompt_r2b.py` (`data/experiment/prompt_r2/freno_p2.md`).

**Árbol modificado en paralelo.** Mientras hacía la primera parte aparecieron en el árbol, de otra sesión,
las salidas de la M1 de U-MED-R2A, sin commit; no las leí ni las toqué hasta que la M1 quedó commiteada
en `f8dedd4`. De esa salida uso solo la E0 e0-r2 (`e0_chunking/salida_tanda0_r2/chunks_<to>.json`), como
pide el mandato; los grafos r2a no son insumo de P1.
Cito el plan contra `ebd7b1e` (`git show ebd7b1e:docs/plan_tesis.md`); las líneas citadas son las mismas
en `f8cf89a`, y la fila de esta unidad es `:399`.

## 0. Fuentes y versión leída

| Fuente | Versión | Control |
|---|---|---|
| L-ESQ-R2, versión firmada | `git show 4ef7650:data/experiment/esq/enmienda_L-ESQ-R2_2026-09-30.md` | sha256 `66c4a1b9…` (el de la firma); las tres notas posteriores, del archivo actual |
| Enmienda 2 de L-ESQ-R2 | `git show 5f9a731:data/experiment/esq/enmienda2_L-ESQ-R2_remite_a_2026-10-02.md` | sha256 `e779bd70…` |
| Protocolo entre tandas | `git show a304b89:docs/protocolo_entre_tandas.md` | sha256 `b23d37c5…`; igual al archivo actual |
| Mandato | `docs/mandatos/UPROMPT_R2_prefijo_nuevo.md` | firma `b901f6d`; notas `ebd7b1e`, `e7f7a2e` y `a807136` |
| U-DIAG-PROCESO, reporte y anexo | `git show 93ce4b7:reports/u_diag_proceso/reporte_u_diag_proceso.md` y `anexo_evidencia_u_diag_proceso.md` | sha256 `5f1ff89f…` y `9852d8fc…` |
| Enmienda de uso de la ventana | `git show 30f106c:data/experiment/esq/enmienda_uso_ventana_2026-09-30.md` | `:61-64` (desvío declarado), citada por la nota `a807136` |
| Prefijo sellado de la tanda 0 | perfil `v3_b54`: `prompt_v3_b54.PREFIJO_SISTEMA_V3` | sha256 `35e88c2d…`, hash canónico `54a111e2175f`, sobre el congelado `e69feaaa…` (`1be8304e3d77`) |
| Tool schema r2 | `data/experiment/pyd_r2/generados/tool_schema_r2.json` | sha256 `307d2b78…` |
| Catálogo r2 | `data/experiment/catalogo_unico/generados_r2/bloque_catalogo_r2.txt` | sha256 `c4005485…` (el de su manifiesto) |
| Crudo de la tanda 0 | `data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/<to>/extracciones_e1.jsonl` | 2.434 unidades, last-wins por `chunk_id` |
| E0 con la que se extrajo | `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0/chunks_<to>.json` | E0 legada |
| E0 e0-r2 de los diez TOs | `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2/chunks_<to>.json`, `f8dedd4` | 2.434 unidades, los mismos ids que la legada; manifiesto de la salida `d93bcc01…` (`data/experiment/medicion_r2a/m1_freno.md`, M1.a) |

El laudo de la release r2 (`docs/laudo_release_r2_pipeline.md`) es un borrador sin firma: lo leí en su
archivo actual (§1.5 a, §3.2).

## 1. Qué es el prefijo sellado y cómo se arma el nuevo

**El sellado.** El mandato ancla el prefijo en `prompt_e1.py` (`:156-165`, `:177`, `:193`, `:496-503`).
Ese módulo es la base de la cadena, con 6 tipos y 8 reglas. El texto con el que se extrajo la tanda 0
es el del perfil `v3_b54` (`manifiestos/tanda0_10tos.json`, `perfil_e1`; namespace
`e1_extraccion|cv=e1-extractor-v1-p54a111e2175f|think=0` en `corpus_tanda0/salida/cla/resumen_e1.json`):
el congelado de ESQ-3 (9 tipos, 13 predicados, reglas 1 a 9) con el bloque de catálogo v3. Comparo
contra ese texto. Las tres secciones que el mandato cita por línea (CONTENIDO NO-PROSA, REGLA
`regula`/`prohibe`/`limita` y FORMATO DE SALIDA) son iguales en los dos textos, como PROVENANCE y
EJEMPLOS NEGATIVOS; TIPOS, PREDICADOS, SUJETOS, REGLAS y LABELS difieren porque la cadena ya los cambió.

**El nuevo (propuesta para P2).** Un módulo propio en `e1_extractor/` que:
1. importa `prompt_v3_b54` sin editarlo y frena si su texto no da sha256 `35e88c2d…`;
2. aplica 30 reemplazos declarados (R0 a R26 y R28 a R30), cada uno con un ancla que debe aparecer
   exactamente una vez, como hacen `prompt_congelado.py` y `prompt_v3_b54.py`;
3. reemplaza el bloque de catálogo (R27) por `bloque_catalogo_r2.txt` tal cual, con el candado del sha
   de su manifiesto (LN-8: bloque y JSON sin diferencias);
4. usa el tool schema de `pyd_r2/generados/` regenerado con las decisiones 15 a 17 (§3);
5. conserva el nombre de la herramienta (`extraer_kg_e1`), `tool_choice` y el primer intento a 8.192
   tokens de salida (`prompt_e1.py:41`, que hereda toda la cadena), salvo lo que se decida en §8.3.
Un selftest demuestra que, fuera de los tramos reemplazados, el texto es byte a byte el del sellado
(precedente: `selftest_prompt_v3_b54.py`).

**Borrador medido** (`p1/salida/`):

| | Sellado `v3_b54` | Borrador A | Borrador B |
|---|---:|---:|---:|
| Caracteres del system | 33.370 | 51.720 | 51.780 (congelado en P2) |
| Caracteres del tool schema (JSON) | 9.033 | 20.655 | 20.655 |
| sha256 del texto | `35e88c2d…` | `d81fbc97…` | `cdb37450…` |
| Hash canónico (system + tools) | `54a111e2175f` | `f3d30f34cacd` | `14d6b63b508e` |

Los calcula `p1/hashes_borrador.py` (`p1/salida/hashes_borrador.json`) con el método de la cadena sellada
(`prompt_e1.py:415-419`, `prompt_v3_b54.py:516-520`); sobre el sellado reproduce `35e88c2d…` y
`54a111e2175f`, y si no, frena. Los del borrador son provisionales: cambian con cada ajuste hasta que P2
congele el texto.

**Caché (decisiones 1 a 4 de `docs/decisiones_caching_extraccion.md`; decisión 2 del mandato).**
- E1, antes: `e1_extraccion|cv=e1-extractor-v1-p54a111e2175f|think=0`. Después:
  `e1_extraccion|cv=e1-extractor-v1-p<hash nuevo>|think=0` (con el texto congelado, variante B, `p14d6b63b508e`). Es un
  namespace nuevo: U-REEXT-T0 paga E1 de las 2.434 unidades. El system sigue como bloque único con
  `cache_control` en el último bloque (decisión 1): el borrador no agrega nada variable al prefijo.
- E3, antes y después: `e3_verificacion|cv=e3-verificador-v1-p21a836c7de6d|think=0` (candado en
  `prompt_e3.py`). La clave local de E3 hashea el request entero, mensaje incluido (laudo de r2, §3.2):
  como el mensaje de E3 renderiza la salida de E1 (`comun_e3.render_extraccion`, `comun_e3.py:140`),
  y esa salida cambia en todas las unidades con el prefijo nuevo, **la clave de E3 cambia en todas las
  unidades**, no solo en las 38 que reciben una NOTA distinta (§4.3). El censo de P1.c ya cuenta E3
  completo (§7).

## 2. El prefijo, sección por sección: sellado y nuevo

Generado desde los reemplazos del borrador (`p1/lado_a_lado.py`; no transcripto a mano). Las variantes A
y B difieren solo en R6 (decisión 20, §9). R11, la sección OMISIONES de R26 y R30 son texto nuevo, sin
contraparte sellada: su «sellado» es el ancla donde se insertan. El orden es el de aplicación (R28 va
después de R0; R29 y R30, después de R15).

### R0 · Encabezado

Manda: L-ESQ-R2 §9 (esquema r2); decisión 10 (catálogo r2); decisión 5.

Sellado:

```text
Trabajás con un schema CERRADO y RÍGIDO (esquema v2, catálogo de sujetos v2.0). NO inventes tipos. NO inventes predicados. NO inventes sujetos.
```

Nuevo:

```text
Trabajás con un schema CERRADO y RÍGIDO (esquema r2, catálogo de sujetos r2). NO inventes tipos. NO inventes predicados. NO inventes sujetos. Lo que el texto expresa y el schema no puede representar NO se fuerza en una caja equivocada ni se calla: se registra en `omisiones` (ver OMISIONES).
```

### R28 · Encabezado · chunk de punto

Manda: F1-A de U-DIAG-PROCESO (decisión de la autora, 03/10/2026).

Sellado:

```text
Extraés SOLO del texto del punto; el contexto heredado orienta y ancla, pero NO se extrae de él (cada bloque heredado tiene su propia unidad de extracción responsable — ver PROVENANCE).
```

Nuevo:

```text
Extraés SOLO del texto del punto; el contexto heredado orienta y ancla, pero NO se extrae de él (cada bloque heredado tiene su propia unidad de extracción responsable — ver PROVENANCE), salvo un caso: si el punto es un ítem de una lista que abre el contexto heredado, su norma se compone con ese encabezado (ver COMPOSICIÓN CON EL ENCABEZADO DE UNA LISTA).
```

### R1 · TIPOS · 1 Comunicacion

Manda: decisiones 8 y 16 (L-ESQ-R2 §2.3 y §2.4; protocolo D7).

Sellado:

```text
1. **Comunicacion**: Una Comunicación A/B/C del BCRA citada en el texto. Ej.: "Com. A 7825", "Comunicación A 7000".
   Properties: codigo (string, ej. "A-7825"), tipo ("A"|"B"|"C"), numero (int).
```

Nuevo:

```text
1. **Comunicacion**: Una Comunicación A/B/C del BCRA citada en el texto (ej.: "Com. A 7825", "Comunicación A 7000"), o una norma externa citada: una ley, un decreto o una resolución.
   Properties: codigo (string: para una Comunicación, la forma "A-7825"; para una norma externa, su denominación tal como la cita el texto). NO emitas el tipo ni el número: el código los deriva de `codigo`.
```

### R2 · TIPOS · 2 TextoOrdenado

Manda: decisión 16 (protocolo D7; r3_freno.md §3).

Sellado:

```text
   Properties: materia, archivo, version.
```

Nuevo:

```text
   Sin properties: la materia, el archivo y la versión los completa el código desde el documento fuente; no los emitas.
```

### R3 · TIPOS · 3 Operacion

Manda: decisión 11 y X5 (BKL-0036).

Sellado:

```text
quién lo lleva a cabo, con qué medios, sobre qué soporte, con qué alcance — cuando no tienen otro campo donde alojarse).
```

Nuevo:

```text
quién lo lleva a cabo, con qué medios, sobre qué soporte, con qué alcance — cuando no tienen otro campo donde alojarse). El calificador que convierte el acto en el que la norma regula, y no en su versión general, es parte del acto: va en la descripción y en el label y nunca se recorta. Un acto acotado por sus condiciones, su contraparte o su modalidad no es el mismo acto sin ese acote.
```

### R4 · TIPOS · 4 Restriccion

Manda: decisión 3 (L-ESQ-R2 §1.3 y §1.4, par A).

Sellado:

```text
   Properties: descripcion (corta, grounded), tipo ("prohibicion"|"limite_cuantitativo"|"limite_cualitativo"), opcional umbral.
```

Nuevo:

```text
   Properties: descripcion (corta, grounded), tipo ("prohibicion"|"limite_cuantitativo"|"limite_cualitativo"). Sus cuantías van en `umbrales` (ver UMBRALES), no en properties.
```

### R5 · TIPOS · 5 Excepcion

Manda: decisión 3; X5 (BKL-0032).

Sellado:

```text
   Properties: descripcion (corta).

6. **Obligacion**
```

Nuevo:

```text
   Properties: descripcion (corta). Sus cuantías van en `umbrales`.
   POLARIDAD: la Excepcion dice qué queda FUERA de una regla, con el mismo sentido que el texto. Si el texto NIEGA un deber o una prohibición en general y la salvedad lo vuelve a exigir en un supuesto, la salvedad no libera de nada: es el supuesto en que el deber SÍ rige. Extraé entonces la Obligacion (o la Restriccion) acotada a ese supuesto, con su Condicion si corresponde, y no una Excepcion que diga que el deber no aplica en él. Antes de emitir una Excepcion, releé su `tramo` y verificá que la descripción no invierta el sentido del texto.

6. **Obligacion**
```

### R6 · TIPOS · 6 Obligacion

Manda: decisiones 3 y 20, variante A (regla actual).

Sellado:

```text
   Properties: descripcion (corta), tipo ("presentacion_informativa"|"calculo"|"asignacion"|"comunicacion_a_cliente"|"reporte_al_supervisor"|"otra"), opcional plazo o frecuencia.
```

Nuevo, variante A (regla actual):

```text
   Properties: descripcion (corta), tipo ("presentacion_informativa"|"calculo"|"asignacion"|"comunicacion_a_cliente"|"reporte_al_supervisor"|"otra"), opcional frecuencia: el tramo literal que fija cada cuánto se cumple el deber (diaria, semanal, mensual, trimestral, semestral, anual, con las palabras del texto) o, si el texto fija el momento del deber sin una cuantía temporal, ese tramo. Los plazos con cuantía temporal van en `umbrales`.
```

Nuevo, variante B (plazos sin cuantía temporal fuera de `frecuencia`):

```text
   Properties: descripcion (corta), tipo ("presentacion_informativa"|"calculo"|"asignacion"|"comunicacion_a_cliente"|"reporte_al_supervisor"|"otra"), opcional frecuencia: SOLO el tramo literal que fija cada cuánto se cumple el deber (diaria, semanal, mensual, trimestral, semestral, anual, con las palabras del texto). Los plazos con cuantía temporal van en `umbrales`. Un momento sin cuantía temporal no es una frecuencia: queda en la descripción y en el `tramo` de la Obligacion, no en `frecuencia`.
```

### R7 · TIPOS · 8 Condicion (definición)

Manda: decisión 7 (L-ESQ-R2 §6.3 y §6.4).

Sellado:

```text
8. **Condicion**: El ANTECEDENTE de otra norma: el supuesto que debe verificarse para que una excepción, una obligación o una restricción se active, se relaje o deje de aplicar. Por sí sola NO manda nada.
```

Nuevo:

```text
8. **Condicion**: El ANTECEDENTE de otra norma o de un acto: el supuesto que debe verificarse para que una excepción, una obligación o una restricción se active, se relaje o deje de aplicar, para que una operación pueda realizarse o para que una facultad se habilite. Por sí sola NO manda nada.
```

### R8 · TIPOS · 8 Condicion (destino de condicion_de)

Manda: decisión 7 (L-ESQ-R2 §6.4: la instrucción deja de mandarla solo a Excepcion, Obligacion o Restriccion); Condicion sin destino en la unidad (decisión de la autora en el FRENO P1, 03/10/2026).

Sellado:

```text
Conectala con `condicion_de` a la Excepcion, Obligacion o Restriccion del mismo chunk cuando el texto de la unidad enuncie ese vínculo.
```

Nuevo:

```text
Conectala con `condicion_de` a lo que ese supuesto condiciona en el mismo chunk, cuando el texto de la unidad enuncie ese vínculo: una Excepcion, una Obligacion o una Restriccion; una Operacion, cuando el acto solo puede realizarse si el supuesto se verifica; o una Potestad, cuando la facultad solo se habilita si el supuesto se verifica. Si lo que el supuesto condiciona no está en tu unidad (por ejemplo, la norma de un encabezado con unidad propia, cuando tu unidad es uno de sus ítems), emití la Condicion sin condicion_de: no la conectes con otro elemento del chunk.
```

### R9 · TIPOS · 8 Condicion (properties)

Manda: decisión 3.

Sellado:

```text
aunque su verbo esté en subjuntivo con forma de deber.
   Properties: descripcion (corta, grounded).
```

Nuevo:

```text
aunque su verbo esté en subjuntivo con forma de deber.
   Properties: descripcion (corta, grounded). Sus cuantías van en `umbrales`.
```

### R10 · TIPOS · 9 Definicion

Manda: decisión 16 (protocolo D7: Definicion.termino literal).

Sellado:

```text
   Properties: termino (el término definido, tal como lo nombra el texto), descripcion (el definiens: cita o paráfrasis fiel).
```

Nuevo:

```text
   Properties: termino (el término definido, copiado tal cual lo nombra el texto: mismas palabras y en el mismo orden, sin comillas), descripcion (el definiens: cita o paráfrasis fiel).
```

### R11 · Secciones nuevas COPIA LITERAL y UMBRALES (antes de PREDICADOS)

Manda: decisiones 3, 15, 16, 17 y 21; F1-A en el `tramo` de la norma compuesta; umbrales con la columna r2a de U-MED-R2A (tablero :67, c50b094) (bloque nuevo, insertado antes de PREDICADOS).

Sellado:

```text
# PREDICADOS VÁLIDOS (exactamente 13, ningún otro)
```

Nuevo:

```text
# COPIA LITERAL (`tramo`, `umbrales`, `sujeto_mencion`, `frecuencia`, `termino`, `omisiones`)

Varios campos piden un tramo del texto «copiado tal cual»: las mismas palabras, en el mismo orden, con sus números, signos y artículos como aparecen; un solo tramo continuo (salvo en la norma compuesta con el encabezado de una lista); sin resumir, completar, reordenar ni cambiar número o género. Podés unir una palabra cortada con guion al final de línea. El código busca cada tramo en el texto del chunk y marca el que no encuentra: un tramo reformulado no se corrige, queda marcado como no verificado.

- `tramo` (toda entidad salvo el TextoOrdenado): el tramo del texto que FUNDA la entidad, el más corto que la sostenga por sí solo (la cláusula, no el párrafo entero). Sale del texto de la unidad; solo cuando la entidad se ancla en un ancestro (ver PROVENANCE) o se compone desde el encabezado de una lista (ver COMPOSICIÓN CON EL ENCABEZADO DE UNA LISTA) sale del bloque heredado. En la norma compuesta son dos segmentos. Es la evidencia de la entidad: si dudaste entre dos tipos, el tramo es lo que permite revisar la elección.
- `otras_propiedades` (entidades y relaciones): lo que el texto dice de ese elemento y la definición de su tipo no prevé, como nombre → valor. No se descarta: se registra aparte. No lo uses para lo que ya tiene campo.

# UMBRALES (Restriccion, Obligacion, Condicion, Excepcion)

`umbrales` es una lista con un elemento por cuantía que acota la norma: monto, porcentaje, plazo con cuantía temporal, cantidad de «veces», UVA. Cada elemento es `{"tramo": …}`: el tramo literal con la cuantía y la palabra o frase que fija su sentido (un máximo, un mínimo, una negación del verbo que la compara, un «hasta», un «al menos», un ponderador), copiado tal cual. El valor, la unidad, la comparación y la base los calcula el código desde el tramo: no los escribas.
- Una cuantía, un elemento: si la cláusula fija dos cuantías (dos porcentajes, un monto y un plazo), son dos elementos.
- En la Condicion: si el supuesto se define por una cuantía (un plazo de cierta cantidad de días «o más», un monto «superior a»), esa cuantía es un elemento de la Condicion.
- Límite relativo: si el tope se compara con otra magnitud y no con un número (un nivel alcanzado en un período, el monto de otra operación, el saldo de una cuenta, un precio de referencia, lo que resultaría de otro cálculo), el elemento es el tramo de esa comparación, aunque no tenga cifra. También es límite relativo un múltiplo o una fracción de otra magnitud («el doble de», «la mitad de») y un límite fijado en otro punto o en otra norma que el texto nombra: el tramo es el de la referencia, y la remisión la registra el código.
- No es una cuantía de la norma un número que fija cómo se informa o se expresa un dato (la cantidad de decimales, la unidad en que se publica) ni un término de un cálculo (un factor, un divisor, los días de una base de cálculo): va en la descripción, no en `umbrales`.
- Una Restriccion de tipo `limite_cuantitativo` tiene al menos un elemento: la cuantía o el tramo de la comparación. Si no encontrás ninguno, revisá el tipo: definir qué es un exceso o fijar la consecuencia de un incumplimiento no es un límite.
- Cuantía de una tabla serializada (ver CONTENIDO NO-PROSA): el tramo es la fila del bloque, o la parte de la fila con la cuantía, tal como está en el bloque.
- No inventes cuantías: lo que no está en el texto no va. Un valor de relleno («N/A», «según corresponda») no es una cuantía. Si la cuantía está en los ítems de una lista que el texto anuncia, va en cada ítem (ver COMPOSICIÓN CON EL ENCABEZADO DE UNA LISTA), no en el encabezado.
- La Potestad no lleva `umbrales`.

# PREDICADOS VÁLIDOS (exactamente 13, ningún otro)
```

### R12 · PREDICADOS · aplica_a

Manda: decisión 4 (L-ESQ-R2 §3.3 y §3.4).

Sellado:

```text
| `aplica_a` | {Restriccion, Obligacion, Operacion, Excepcion, Potestad} → SUJETO del catálogo (source = local_id del elemento alcanzado; el sujeto va en sujeto_id o sujeto_propuesto, SIN target) |
```

Nuevo:

```text
| `aplica_a` | {Restriccion, Obligacion, Operacion, Excepcion, Potestad} → SUJETO (source = local_id del elemento alcanzado; el sujeto va en `sujeto_mencion`, con `sujeto_id` como sugerencia; SIN target) |
```

### R13 · PREDICADOS · ejecuta

Manda: decisión 4.

Sellado:

```text
| `ejecuta` | SUJETO del catálogo → Operacion (target = local_id de la operación; el sujeto va en sujeto_id o sujeto_propuesto, SIN source) |
```

Nuevo:

```text
| `ejecuta` | SUJETO → Operacion (target = local_id de la operación; el sujeto va en `sujeto_mencion`, con `sujeto_id` como sugerencia; SIN source) |
```

### R14 · PREDICADOS · condicion_de y remisiones

Manda: decisiones 7 y 12; la Comunicacion sigue con su `referencia` (decisión de la autora en el FRENO P1, 03/10/2026).

Sellado:

```text
| `condicion_de` | Condicion → {Excepcion, Obligacion, Restriccion} |
```

Nuevo:

```text
| `condicion_de` | Condicion → {Excepcion, Obligacion, Restriccion, Operacion, Potestad} |

La remisión del texto a otro punto o a otra norma la registra el código desde el texto: no es una relación que debas emitir ni una omisión. Esto no cambia la Comunicacion: una Comunicación o una norma externa citada sigue siendo una entidad Comunicacion, con su referencia desde el TextoOrdenado; lo que no emitís es la remisión desde el contenido. Si la remisión fija el contenido de una norma del chunk, ese contenido va en la descripción y en el `tramo` de la norma.
```

### R15 · SUJETOS

Manda: decisiones 4, 10 y 11; X5 (BKL-0033); X9 (BKL-0009 a BKL-0016).

Sellado:

```text
El sujeto de una relación `aplica_a` o `ejecuta` se ELIGE del catálogo de abajo — NO se crea:

- Poné en `sujeto_id` el id EXACTO de la entrada del catálogo que el texto nombra (matcheá por label o por alias).
- Si el punto nombra uno o más sujetos ESPECÍFICOS, emití UNA relación por CADA sujeto nombrado, usando la clase del catálogo que corresponde a ese nombre.
  ✓ "Las entidades financieras, los PSPCP y las empresas emisoras deberán informar..." → 3 relaciones aplica_a, con sujeto_id "Sujeto_entidad_financiera", "Sujeto_pspcp" y "Sujeto_empresa_no_financiera_emisora_de_tarjetas".
  ✗ MAL: una única relación hacia el rol del TO cuando el texto enumera sujetos con nombre propio.
- Usá EXACTAMENTE la clase que el texto nombra: NUNCA una más específica ni una más general. La jerarquía del grafo se ocupa de la herencia; tu trabajo es fidelidad al texto.
  ✓ el texto dice "las entidades financieras" → sujeto_id "Sujeto_entidad_financiera".
  ✗ MAL: el texto dice "las entidades financieras" y emitís "Sujeto_banco" o "Sujeto_banco_comercial" (descenso de jerarquía sin licencia del texto).
  ✗ MAL: el texto dice "los bancos comerciales" y emitís "Sujeto_entidad_financiera" (ascenso: más general que lo que el texto nombra).
- Si la norma se dirige al colectivo del TO ("las entidades", "los sujetos obligados"), usá el rol de alcance indicado en el mensaje del chunk.
- Si el texto nombra un sujeto que NO matchea ninguna entrada del catálogo ni sus alias, usá `sujeto_propuesto` (texto libre con el nombre del sujeto tal como aparece) y, si podés, `sujeto_propuesto_padre_sugerido` con el id del catálogo más cercano como padre. NO fuerces el id más parecido: ante la duda, proponé.
- `sujeto_id` y `sujeto_propuesto` son MUTUAMENTE EXCLUYENTES: exactamente uno de los dos.
- Los sujetos "del exterior" NO son entradas propias: usá la clase local correspondiente (la jurisdicción es un atributo, ya contemplado en los alias).
```

Nuevo:

```text
El sujeto de una relación `aplica_a` o `ejecuta` va en dos campos:

- `sujeto_mencion` (OBLIGATORIA en toda relación `aplica_a` o `ejecuta`): el tramo del texto que nombra al sujeto, copiado tal cual (ver COPIA LITERAL), con sus artículos y en el orden del texto; no la forma del catálogo. Si el texto de la unidad no lo nombra y el sujeto está en el contexto heredado, copiala de ahí.
- `sujeto_id` (sugerencia): el id EXACTO de la entrada del catálogo de abajo que la mención nombra (por label o por alias). La resolución final la hace el código desde la mención; tu sugerencia cuenta cuando la mención sola no alcanza.
- Si la mención no nombra ninguna entrada del catálogo ni sus alias, NO pongas `sujeto_id`: dejá la mención sola y, si podés, `sujeto_propuesto_padre_sugerido` con el id del catálogo más cercano como padre. NO fuerces el id más parecido: una mención sin id queda registrada para ampliar el catálogo; un id forzado es un error. Cuando una definición del catálogo dice que un sujeto «sigue en sujeto_propuesto», se lee así: mención sin `sujeto_id`.
- Si el punto nombra uno o más sujetos ESPECÍFICOS, emití UNA relación por CADA sujeto nombrado, cada una con su mención.
  ✓ "Las entidades financieras, los PSPCP y las empresas emisoras deberán informar..." → 3 relaciones aplica_a, con las menciones "Las entidades financieras", "los PSPCP" y "las empresas emisoras", y sujeto_id "Sujeto_entidad_financiera", "Sujeto_pspcp" y "Sujeto_empresa_no_financiera_emisora_de_tarjetas".
  ✗ MAL: una única relación hacia el rol del TO cuando el texto enumera sujetos con nombre propio.
- Usá EXACTAMENTE la clase que la mención nombra: NUNCA una más específica ni una más general. La jerarquía del grafo se ocupa de la herencia; tu trabajo es fidelidad al texto.
  ✓ el texto dice "las entidades financieras" → mención "las entidades financieras", sujeto_id "Sujeto_entidad_financiera".
  ✗ MAL: el texto dice "las entidades financieras" y emitís "Sujeto_banco" o "Sujeto_banco_comercial" (descenso de jerarquía sin licencia del texto).
  ✗ MAL: el texto dice "los bancos comerciales" y emitís "Sujeto_entidad_financiera" (ascenso: más general que lo que el texto nombra).
- Si la norma se dirige al colectivo del TO ("las entidades", "los sujetos obligados", sin otro calificativo), la mención es esa expresión y la sugerencia es el rol de alcance indicado en el mensaje del chunk: NUNCA una clase más estrecha, aunque el contexto hable de un tipo de entidad en particular.
- SUJETO ALCANZADO Y CALIFICADOR. La mención nombra al sujeto, no lo que acota el alcance de la norma. Si el texto agrega a un sujeto un calificativo que restringe a qué operaciones o actos de ese sujeto se aplica la norma, el sujeto es la clase nombrada (una mención por sujeto, sin el calificativo) y el calificativo es contenido de la norma: va en su descripción y en su `tramo`, y nunca se pierde. Una excepción para un sujeto en lo que respecta a una de sus actividades no exceptúa al sujeto entero.
- Una Obligacion o una Restriccion lleva `aplica_a` solo hacia el sujeto que el texto obliga o al que le prohíbe algo. Si el texto enuncia en voz pasiva un acto que realiza otro (la autoridad, un registro, un tercero), ese acto no es un deber del sujeto regulado: no se lo atribuyas con `aplica_a`; si es un efecto del deber del sujeto, va en la descripción de ese deber.
- `sujeto_id` y `sujeto_propuesto_padre_sugerido` son MUTUAMENTE EXCLUYENTES: a lo sumo uno de los dos.
- Los sujetos "del exterior" tienen entrada propia cuando el catálogo la tiene (entidades financieras, bancos y entidades cambiarias del exterior); si no, usá la clase local correspondiente.
```

### R29 · PROVENANCE · el contexto ancla, la unidad extrae

Manda: F1-A de U-DIAG-PROCESO (decisión de la autora, 03/10/2026).

Sellado:

```text
y extraerlo acá duplicaría y anclaría mal.
```

Nuevo:

```text
y extraerlo acá duplicaría y anclaría mal. La única excepción es la composición con el encabezado de una lista (ver COMPOSICIÓN CON EL ENCABEZADO DE UNA LISTA): ese encabezado puede no tener unidad propia (cuando está en la línea de título del punto que lo contiene) y, cuando la tiene, esa unidad no extrae la norma de los ítems.
```

### R30 · COMPOSICIÓN CON EL ENCABEZADO DE UNA LISTA (sección nueva, antes de REGLAS)

Manda: F1-A de U-DIAG-PROCESO y tratamiento por tipo del encabezado (decisiones de la autora, 03/10/2026; sección nueva, insertada antes de REGLAS).

Sellado:

```text
# REGLAS NO NEGOCIABLES
```

Nuevo:

```text
# COMPOSICIÓN CON EL ENCABEZADO DE UNA LISTA

Un encabezado que abre una lista termina en «:»: es la línea de título de un punto (bloque heredado `encabezado`, sin unidad propia) o un párrafo introductorio con unidad propia. Enuncia parte de una norma cuyo contenido está repartido en los ítems. Si el contexto heredado termina en un encabezado así y tu unidad es uno de sus ítems, mirá qué son los ítems:
- CONTENIDOS (lo que hay que hacer, informar, incluir o cumplir; los miembros de una clase que el encabezado nombra): la norma del ítem es la COMPUESTA. Extraela entera en el ítem, con `punto` = el ítem: el sujeto del encabezado, su modalidad (deber, prohibición o facultad), su cuantificador (si los ítems se exigen todos o si basta con cualquiera de ellos) y el contenido del ítem. La descripción dice la norma completa y conserva el cuantificador. Si el encabezado no trae el sujeto o la modalidad, tomalos del bloque heredado más cercano que los trae.
- SUPUESTOS O CONDICIONES de una norma que el encabezado enuncia: el ítem es una Condicion (ver Condicion) y la norma queda en la unidad del encabezado; como esa norma no está en tu unidad, la Condicion va sin `condicion_de` (ver Condicion). Si el encabezado es la línea de título de un punto, no tiene unidad propia; entonces:
  - si los supuestos son alternativos (basta cualquiera: «o», «alguno de», «cualquiera de»), la norma del ítem es la COMPUESTA: la del encabezado con el supuesto del ítem, y conserva el cuantificador;
  - si se exigen juntos («y», «la totalidad», «concurrentemente») o no queda claro, el ítem es solo una Condicion, y la norma del encabezado no se extrae en ningún ítem: repetirla con una sola condición la daría por suficiente.

En la norma compuesta:
- El sujeto del encabezado va también en la relación `aplica_a` o `ejecuta` del ítem, con la mención copiada del encabezado.
- Lo que el encabezado fija para cada ítem (un plazo, un ámbito, una condición que vale para todos los ítems) también se compone en el ítem: el plazo, como elemento de `umbrales` de la norma compuesta; la condición, como Condicion del ítem con `condicion_de` hacia esa norma. Su `tramo` es el segmento del encabezado, tomado del contexto heredado.
- El `tramo` de la entidad compuesta lleva dos segmentos, cada uno copiado tal cual y unidos por « […] »: primero el del encabezado, tomado del contexto heredado (puede abarcar bloques heredados seguidos, como una línea de título y el párrafo que la continúa); después el del ítem, tomado del texto de tu unidad.

En la unidad del encabezado:
- No se emite un nodo por el solo anuncio de la lista (regla 1), ni lo que se compone en los ítems: así no hay duplicados.
- Sí se extrae lo que el encabezado enuncia aparte de la lista: una norma propia, una excepción a la lista entera, y la norma principal cuando los ítems son sus supuestos o condiciones.

# REGLAS NO NEGOCIABLES
```

### R16 · REGLAS · 1

Manda: X5 (BKL-0035); F1-A y tratamiento por tipo del encabezado (decisiones de la autora, 03/10/2026).

Sellado:

```text
El número de punto va en el campo `punto`, no en una entidad.

2.
```

Nuevo:

```text
El número de punto va en el campo `punto`, no en una entidad. Tampoco es una entidad el anuncio de una lista: la unidad de un encabezado que abre una lista no emite una Obligacion, una Restriccion ni una Potestad cuyo único contenido es que siguen ítems, ni lo que se compone en cada ítem (el sujeto, la modalidad, el cuantificador y lo que el encabezado fija para cada ítem; ver COMPOSICIÓN CON EL ENCABEZADO DE UNA LISTA). Lo que el encabezado enuncia aparte de la lista (una norma propia, una excepción a la lista entera, la norma principal cuando los ítems son sus supuestos o condiciones) se extrae en su unidad como siempre.

2.
```

### R17 · REGLAS · 4

Manda: decisiones 5 y 17 (L-ESQ-R2 §5.3 y §8.3; protocolo D8).

Sellado:

```text
4. **NO inventes tipos ni predicados fuera de las listas.** Si una idea no encaja en los 9 tipos de entidad o 13 predicados, NO la incluyas. Es preferible no extraer algo a forzarlo en una caja equivocada.
```

Nuevo:

```text
4. **NO inventes tipos ni predicados fuera de las listas.** Si un contenido normativo no encaja en los 9 tipos de entidad, NO lo fuerces en el más parecido: registralo en `omisiones` con categoría `fuera_de_tipos`, su tramo y, en `nota`, el tipo que habrías usado. Si una relación que el texto expresa no encaja en los 13 predicados (por vocabulario o por dominio y rango), registrala con categoría `relacion_sin_predicado`, su tramo, `source` y `destino` (los local_id de sus extremos, si los extrajiste) y, en `nota`, el predicado que habrías usado. Es preferible registrar a forzar una caja equivocada.
```

### R18 · REGLAS · 7

Manda: decisión 4 (L-ESQ-R2 §3.4: extiende la regla 7).

Sellado:

```text
generá una relación `aplica_a` (o `ejecuta`) POR CADA sujeto, cada una con su propio sujeto_id del catálogo. NO metas la enumeración entera en un solo sujeto_propuesto.
```

Nuevo:

```text
generá una relación `aplica_a` (o `ejecuta`) POR CADA sujeto, cada una con SU mención (solo ese sujeto, con su artículo si lo tiene) y su sugerencia. NO metas la enumeración entera en una sola mención.
```

### R19 · REGLAS · 9 (título)

Manda: decisión 5 (L-ESQ-R2 §5.3: la regla 9 registra en lugar de callar).

Sellado:

```text
9. **CONTENIDO META-NORMATIVO: NO SE EXTRAE.**
```

Nuevo:

```text
9. **CONTENIDO META-NORMATIVO: NO SE EXTRAE, SE REGISTRA.**
```

### R20 · REGLAS · 9 (cierre)

Manda: decisión 5.

Sellado:

```text
No lo fuerces en Restriccion, Obligacion, Potestad ni Definicion: simplemente no lo extraigas.
```

Nuevo:

```text
No lo fuerces en Restriccion, Obligacion, Potestad ni Definicion: no lo extraigas y registralo en `omisiones` con categoría `meta_normativo` y su tramo.
```

### R21 · CONTENIDO NO-PROSA

Manda: decisión 6 (plan :399, notas del 02/10; L-ESQ-R2 §1.4 r2b y §5.4).

Sellado:

```text
# CONTENIDO NO-PROSA (chunks flaggeados por E0)

Si el mensaje del chunk trae un bloque "FLAGS E0" (contenido tabular y/o fórmulas detectados determinísticamente), ese contenido está DECLARADO NO-CONFIABLE en su forma extraída del PDF:

- NO reconstruyas tablas ni fórmulas: la estructura visual (columnas, alineación, sub/superíndices) pudo haberse destruido en la extracción del PDF, y una lectura "prolija" de texto destrozado fabrica contenido falso.
- Extraé SOLO lo que la prosa circundante sostiene por sí sola (el enunciado de que existe una exigencia, quién la cumple, a qué operación refiere).
- NO copies valores numéricos de celdas de tabla ni coeficientes de fórmulas a properties (umbral, plazo) salvo que la prosa los enuncie en una oración completa.
- Registrá en `omisiones_no_prosa` (lista de strings, uno por omisión) qué contenido quedó afuera y por qué (ej.: "tabla de ponderadores por grupo: estructura tabular no confiable, valores no extraídos").
- Si el chunk entero es tabla/fórmula y nada es extraíble con confianza, devolvé entities/relations con lo mínimo sostenible (puede ser solo el nodo TextoOrdenado) y registrá la omisión. Un chunk flaggeado SIN omisiones registradas y CON valores numéricos extraídos es una extracción sospechosa.
```

Nuevo:

```text
# CONTENIDO NO-PROSA (tablas y fórmulas marcadas por E0)

El texto del chunk puede traer tablas SERIALIZADAS por E0, entre `[TABLA <id> | …]` y `[FIN TABLA <id>]`, y el mensaje puede traer un bloque "FLAGS E0". Son dos cosas distintas:

- **Tabla serializada: CONFIABLE.** E0 la reconstruyó desde la estructura del PDF y la verificó contra sus celdas. Cada fila es `Fila k: clave = valor | clave = valor`. En modo «columnas», la clave es el encabezado de su columna (las líneas `Rótulo:` y `Columnas:` lo anuncian); en modo «posicional», E0 no reconoció un encabezado y la clave es `colN`: el nombre de cada columna está en las primeras filas del bloque. Leela como texto: extraé lo que dice y COPIÁ sus valores (en `umbrales`, en el `tramo` y en la descripción) tal como figuran en el bloque, asociando cada valor a su columna y a su fila. `⟨combinada con fila n⟩` marca un valor que el PDF escribe una sola vez, en la fila n, y que vale también en esa fila; `⟨abarca hasta c⟩` marca un valor que ocupa varias columnas, hasta la columna c. No reordenes filas ni columnas y no completes celdas que el bloque no trae. El mensaje lista cada tabla con lo que E0 no pudo resolver: una fila de subtítulo no es un dato y califica a las filas que la siguen; el valor de una celda combinada que E0 no asignó a sus filas puede valer para varias filas sin que el bloque indique cuáles, y si el texto no lo aclara no se asocia a ninguna: se registra la omisión `tabla`.
- **Contenido tabular residual y fórmulas: NO CONFIABLES.** Lo que el bloque "FLAGS E0" declara como contenido tabular residual (una tabla que E0 no pudo serializar, una tabla serializada que el mensaje declare no confiable, o texto con forma de tabla fuera de los bloques) y las fórmulas siguen DECLARADOS NO-CONFIABLES en su forma extraída del PDF:
  - NO reconstruyas tablas ni fórmulas: la estructura visual (columnas, alineación, sub/superíndices) pudo haberse destruido en la extracción del PDF, y una lectura "prolija" de texto destrozado fabrica contenido falso.
  - Extraé SOLO lo que la prosa circundante sostiene por sí sola (el enunciado de que existe una exigencia, quién la cumple, a qué operación refiere).
  - NO copies valores numéricos de ese contenido ni coeficientes de fórmulas a `umbrales` salvo que la prosa los enuncie en una oración completa.
  - Registrá en `omisiones` lo que quedó afuera, con categoría `tabla` o `formula`, su tramo y, en `nota`, por qué.
  - Si el chunk entero es contenido no confiable y nada es extraíble con confianza, devolvé lo mínimo sostenible (puede ser solo el nodo TextoOrdenado) y registrá la omisión. Un chunk con contenido no confiable SIN omisiones registradas y CON valores numéricos extraídos de ese contenido es una extracción sospechosa.
```

### R22 · EJEMPLOS NEGATIVOS · predicados

Manda: coherencia (13 predicados desde el congelado) y decisión 5.

Sellado:

```text
- ❌ Predicado "regulado_por" o "contiene" o "se_aplica_si" → no están en la lista de 12.
```

Nuevo:

```text
- ❌ Predicado "regulado_por" o "contiene" o "se_aplica_si" → no están en la lista de 13. Si la relación está en el texto y ningún predicado la representa, va a `omisiones` como `relacion_sin_predicado`.
```

### R23 · EJEMPLOS NEGATIVOS · aplica_a

Manda: decisión 4; alineación con BKL-0038 (una Restriccion no usa regula).

Sellado:

```text
- ❌ Restriccion --aplica_a--> Operacion → MAL, `aplica_a` requiere un SUJETO del catálogo como rango (sujeto_id). Usá `regula` o `prohibe`/`limita`.
```

Nuevo:

```text
- ❌ Restriccion --aplica_a--> Operacion → MAL, `aplica_a` requiere un SUJETO como rango (en `sujeto_mencion`). Usá `prohibe` o `limita`, según el tipo de la Restriccion.
```

### R24 · EJEMPLOS NEGATIVOS · sujetos y polaridad

Manda: decisión 4.

Sellado:

```text
- ❌ Entidad de tipo "EntidadFinanciera" o "Sujeto" → los sujetos NO son entidades del chunk: van en sujeto_id/sujeto_propuesto de aplica_a/ejecuta.
- ❌ sujeto_id "Sujeto_entidad_financiera" para "empresas de seguros" → si el sujeto no matchea entrada ni alias del catálogo, usá sujeto_propuesto; NO fuerces el más parecido.
```

Nuevo:

```text
- ❌ Entidad de tipo "EntidadFinanciera" o "Sujeto" → los sujetos NO son entidades del chunk: van en la mención (con su sugerencia) de aplica_a/ejecuta.
- ❌ sujeto_id "Sujeto_entidad_financiera" para "empresas de seguros" → si la mención no nombra entrada ni alias del catálogo, va sin sujeto_id; NO fuerces el más parecido.
- ❌ sujeto_mencion "Sujeto_entidad_financiera" o "Entidades financieras" cuando el texto dice otra cosa → la mención es el texto del chunk, no el catálogo.
- ❌ Excepcion que dice que un deber no aplica en el supuesto en que el texto lo exige → invierte la polaridad (ver Excepcion).
```

### R25 · REGLA regula / prohibe / limita

Manda: P1.a (alineación con BKL-0038, plan :396) y decisión 9 (L-ESQ-R2 §1.4).

Sellado:

```text
Tres predicados Restriccion→Operacion. NO son intercambiables. Elegí según `Restriccion.tipo`:

- Si `Restriccion.tipo = "prohibicion"` → usá `prohibe`. Patrón: "no podrá", "se prohíbe", "queda prohibido".
- Si `Restriccion.tipo = "limite_cuantitativo"` (hay umbral numérico: %, $, monto) → usá `limita`.
- Si `Restriccion.tipo = "limite_cualitativo"` (restricción cualitativa sin monto) → usá `limita`.
- `regula` queda RESERVADO para Obligacion→Operacion. Cuando una Obligacion regula cómo se hace una Operacion, usá `regula`.

✅ Restriccion(tipo=prohibicion) --prohibe--> Operacion
✅ Restriccion(tipo=limite_cuantitativo, umbral="10%") --limita--> Operacion
✅ Restriccion(tipo=limite_cualitativo) --limita--> Operacion
✅ Obligacion --regula--> Operacion
❌ Restriccion(tipo=limite_cuantitativo) --regula--> Operacion  ← MAL, usá `limita`
❌ Restriccion(tipo=prohibicion) --regula--> Operacion  ← MAL, usá `prohibe`
```

Nuevo:

```text
Tres predicados Restriccion→Operacion. NO son intercambiables. El predicado sale de `Restriccion.tipo`, y el código controla que coincidan:

- Si `Restriccion.tipo = "prohibicion"` → usá `prohibe`. Patrón: "no podrá", "se prohíbe", "queda prohibido", sin una cuantía que fije hasta dónde.
- Si `Restriccion.tipo = "limite_cuantitativo"` (hay una cuantía: %, $, monto, plazo, o un límite relativo) → usá `limita`.
- Si `Restriccion.tipo = "limite_cualitativo"` (restricción cualitativa sin monto) → usá `limita`.
- Una Restriccion NUNCA usa `regula`: `regula` queda RESERVADO para Obligacion→Operacion. Cuando una Obligacion regula cómo se hace una Operacion, usá `regula`.
- Si dudás entre prohibición y límite, decidí primero el tipo (¿el texto veda el acto o lo acota?) y usá el predicado de ese tipo. Una Restriccion "prohibicion" con `limita`, o una "limite_cuantitativo" o "limite_cualitativo" con `prohibe`, queda marcada como incoherente.
- **Destino de `limita`:** el destino de `limita` es el acto o la magnitud que el tope acota o, si es un ponderador, la exposición que pondera; no su base, su finalidad, su consecuencia ni el supuesto que lo habilita.

✅ Restriccion(tipo=prohibicion) --prohibe--> Operacion
✅ Restriccion(tipo=limite_cuantitativo, umbrales=[{tramo: "no podrá superar el 10 %"}]) --limita--> Operacion
✅ Restriccion(tipo=limite_cualitativo) --limita--> Operacion
✅ Obligacion --regula--> Operacion
❌ Restriccion(tipo=limite_cuantitativo) --regula--> Operacion  ← MAL, usá `limita`
❌ Restriccion(tipo=prohibicion) --regula--> Operacion  ← MAL, usá `prohibe`
❌ Restriccion(tipo=prohibicion) --limita--> Operacion  ← MAL: o el tipo es un límite, o el predicado es `prohibe`
❌ Restriccion --limita--> la base del tope, su finalidad o lo que pasa si se supera  ← MAL: el destino es lo que el tope acota
```

### R26 · OMISIONES (nueva) y FORMATO DE SALIDA

Manda: decisiones 5, 15 y 17 (L-ESQ-R2 §5.3 y §8.3; protocolo D6 y D8).

Sellado:

```text
# FORMATO DE SALIDA

Llamá la herramienta `extraer_kg_e1` con el schema dado. Si el chunk no tiene contenido normativo extraíble (preámbulo vacío, lista de abreviaturas, etc.), devolvé entities y relations vacíos (el nodo TextoOrdenado igual va). Todo elemento lleva `punto`.
```

Nuevo:

```text
# OMISIONES (campo `omisiones`, en TODO chunk)

`omisiones` es una lista, obligatoria en todo chunk (vacía si no omitiste nada), con un elemento por cada contenido del texto de la unidad que NO extrajiste:
- `categoria`: `meta_normativo` (regla 9); `tabla` o `formula` (contenido no confiable, ver CONTENIDO NO-PROSA); `fuera_de_tipos` (contenido normativo que no encaja en ningún tipo, regla 4); `relacion_sin_predicado` (relación que el texto expresa y ningún predicado representa, regla 4).
- `tramo`: el tramo del texto PROPIO de la unidad que no extrajiste, copiado tal cual (no del contexto heredado: ese tiene su propia unidad).
- `nota`: por qué quedó afuera; en `fuera_de_tipos`, el tipo que habrías usado; en `relacion_sin_predicado`, el predicado que habrías usado.
- `source` y `destino` (solo en `relacion_sin_predicado`, opcionales): los local_id de los extremos de esa relación, si los extrajiste como entidades.
No registres como omisión lo que sí extrajiste, los títulos ni las remisiones a otros puntos o normas.

# FORMATO DE SALIDA

Llamá la herramienta `extraer_kg_e1` con el schema dado. Si el chunk no tiene contenido normativo extraíble (preámbulo vacío, lista de abreviaturas, etc.), devolvé entities y relations vacíos (el nodo TextoOrdenado igual va). Todo elemento lleva `punto`; toda entidad salvo el TextoOrdenado lleva `tramo`; toda relación `aplica_a` o `ejecuta` lleva `sujeto_mencion`; `omisiones` va siempre (vacía si no omitiste nada).
```

### R27 · Bloque de catálogo (de «## Sujetos regulados» a «## Roles de alcance por TO»)

Manda: decisión 10 (L-ESQ-R2 §7.4; LN-8).

- Sellado: <bloque de catálogo v3: 13290 caracteres, sha256 6cda11be8ee8…>.
- Nuevo: <bloque_catalogo_r2.txt: 15092 caracteres, sha256 c40054853bd8…>, el archivo generado por U-CAT-UNICO desde `catalogo_sujetos_r2.json` (`data/experiment/catalogo_unico/generados_r2/bloque_catalogo_r2.txt`, el sha256 de su `manifest_generados_r2.json`), tal cual.

## 3. Tool schema

**Qué se conecta.** El generado por U-PYD desde `modelos_r2.py` (`pyd_r2/generados/tool_schema_r2.json`),
con los cambios de las decisiones 15 a 17. Los medí en una copia del modelo fuera del repo
(`p1/espejo_tool_schema.py`); P2 los escribe en `modelos_r2.py` y regenera con `generar_r2.py`.

**Control de la decisión 13.** Con el `modelos_r2.py` vigente (sha256 `71cab622…`), `generar_r2.py`
reproduce byte a byte el tool schema (`307d2b78…`) y los enums (`abd197ac…`) del repo; solo cambia el
manifiesto (`8ed3e812…` → `01ef3052…`), porque registra el sha del modelo, que cambió después de
`57a8dd2` por agregados que no alteran lo generado. Con las decisiones 15 a 17, el tool schema pasa a
`0c391f2b…` y los enums no cambian (`abd197ac…`).

| Campo | Sellado `v3_b54` | r2 de U-PYD (hoy) | r2 con 15 a 17 |
|---|---|---|---|
| `entities[]` | un ítem; `properties` libre (string → string) | `anyOf` de 9 ítems, uno por tipo, `properties` cerradas por tipo | ídem |
| `tramo` de evidencia | no | no | requerido en 8 tipos; el TextoOrdenado no lo lleva (§10, punto 1) |
| `umbrales[].tramo` | no (`umbral` y `plazo` como strings en `properties`) | Restriccion, Obligacion, Condicion, Excepcion | ídem |
| `Obligacion.properties.frecuencia` | no (`plazo o frecuencia`) | tramo literal | ídem (ver §9) |
| `Comunicacion.properties` | libre (`codigo`, `tipo`, `numero`) | `codigo`, `tipo` (enum con «externa»), `numero` | solo `codigo` (decisión 16) |
| `TextoOrdenado.properties` | libre (`materia`, `archivo`, `version`) | los tres | sale (decisión 16) |
| `Definicion.termino` | libre | sin descripción | «copiado tal cual» (decisión 16) |
| `otras_propiedades` | no | en entidades | en entidades y relaciones (decisión 17) |
| `relations[].sujeto_mencion` | no | sí | ídem |
| `relations[].sujeto_propuesto` | sí | no (P-b2) | ídem |
| `sujeto_id` y padre sugerido | enum de 102 ids | enum de 110 ids | ídem |
| `predicate` | 13 | 13, sin `remite_a` | 13, sin `remite_a` (decisión 12) |
| Omisiones | `omisiones_no_prosa`, lista de strings, opcional | `omisiones` requerida: `categoria` (5), `tramo`, `nota` | más `source` y `destino` opcionales (decisión 17) |
| `required` del input | `entities`, `relations` | más `omisiones` | ídem |

Controles sobre el borrador (`censo_p1.json`, `control_tool_schema_borrador`): 13 predicados, `remite_a`
ausente del tool schema y del texto del prefijo, `tramo` requerido en los 8 tipos que lo llevan y no en
el TextoOrdenado, Comunicacion solo con `codigo`, TextoOrdenado sin `properties`, `otras_propiedades` en
relaciones, y la omisión con `categoria`, `tramo`, `nota`, `source` y `destino`.

**Tamaño.** El tool schema r2 tiene 20.655 caracteres contra 9.033 del sellado. Pesa la estructura que
genera Pydantic: nueve ramas `anyOf` que repiten las descripciones de `local_id`, `label`, `punto`,
`otras_propiedades` y `tramo`, y los dos enums de 110 ids. Es caché de lectura: su costo está en §7.

**No verificado.** Que la API acepte `anyOf` con `const` dentro de `items` en un tool sin modo estricto:
el generador y sus selftests no llaman a la API. Lo verifica la primera llamada de P4.

## 4. Mensaje de usuario de E1 y NOTA de E3

### 4.1 Mensaje de E1, fuera de las tablas

El nuevo módulo arma su propio mensaje, porque `prompt_e1.build_user_message` es parte de la cadena
sellada. Reusa sus partes; los cambios son:

| Línea | Sellado | Nuevo | Manda |
|---|---|---|---|
| Documento, TO, tipo de unidad, puntos admitidos, contexto heredado, texto | igual | igual | — |
| Rótulo del contexto heredado de un ítem de lista (706 unidades de la tanda 0, §4.5) | «Contexto estructural heredado (SOLO contexto y anclaje: NO extraigas contenido normativo de estos bloques — cada uno tiene su propia unidad de extracción; ver PROVENANCE):» | «Contexto estructural heredado (contexto y anclaje; NO extraigas contenido normativo de estos bloques, salvo un caso: el último bloque abre la lista de la que este punto es un ítem, así que la norma del ítem se compone con ese encabezado — ver COMPOSICIÓN CON EL ENCABEZADO DE UNA LISTA):» | F1-A |
| Alcance del TO | «…usá `<rol>` como sujeto.» (en los 5 TOs de desarrollo sin la guarda de B5.4) | «…sugerí `<rol>` en `sujeto_id`, con la expresión del texto como `sujeto_mencion`. Es el sujeto de aplica_a cuando la norma se dirige al colectivo; NO es el ejecutor por defecto en ejecuta.», en todos los TOs | decisión 4 |
| FLAGS E0, fórmulas | «…registrar omisiones en `omisiones_no_prosa`» | «…registrar en `omisiones` con categoría `formula`» | decisión 5 |
| Bloque de tablas | la línea «FLAGS E0» y todas las líneas de evidencia | ver §4.2 | decisión 6 |
| Cierre | «Recordá: nodo TextoOrdenado con local_id='to', todo elemento con `punto` de la lista admitida.» | lo mismo más «; toda entidad con su `tramo`; toda relación de sujeto con su `sujeto_mencion`; `omisiones` siempre (vacía si no omitiste nada).» | decisiones 4, 5 y 15 |

La tabla de alcance por TO no cambia: `catalogo_unico/generados_r2/rol_por_to_r2.json` y `ROL_POR_TO_V3`
coinciden en los 71 TOs (0 diferencias). La guarda de `ejecuta` se extiende a los 5 TOs de desarrollo,
que hoy no la llevan solo para quedar byte a byte iguales al mensaje de producción; con un namespace
nuevo esa razón no rige. Es un cambio para aprobar.

### 4.2 Bloque de tablas del mensaje (sobre la E0 e0-r2, `f8dedd4`)

**Qué trae la E0 e0-r2** (`censo_p1.json`, `mensaje_r2`). De las 2.434 unidades, 45 tienen
`contenido_tabular`, todas en ric, cap y ext:
- 39 llevan `flags.tablas_e0`, con 54 tablas detectadas. 37 tienen al menos una tabla serializada (51
  tablas en total). En 3 de esas 39, `contenido_tabular_residual` es verdadero: `ric::S2` y `ric::3.1.4`
  (tabla detectada y no serializada) y `cap::4.2.1.2` (tres serializadas y una no).
- 6 están marcadas solo por la heurística legada y no tienen la clave residual: `cap::2.13`, `cap::3.2.4`,
  `cap::4.2.2`, `cap::4.3.3.2`, `cap::7.1.1::intro` y `ext::7.1.1.3`, los seis que anotó el plan
  (`ebd7b1e:docs/plan_tesis.md:399`, nota (i) del 02/10).
- 53 unidades tienen `formula`.
- Los metadatos de complejidad existen en las 54 entradas de `tablas_e0` (`modo`, `celdas_propagadas`,
  `celdas_con_alcance`, `combinadas_sin_propagar`, `filas_subtitulo`). Entre las 51 serializadas, 24 están en
  modo posicional, 6 tienen celdas propagadas, 19 tienen celdas con alcance de varias columnas, 6 tienen
  celdas combinadas sin propagar y 11 tienen filas de subtítulo. 12 tablas, en 8 chunks, reciben el aviso
  de riesgo.
- 24 de los 25 chunks con tabla que la E0 legada ya marcaba tienen líneas de evidencia que el bloque
  reemplazó, como dice la nota (ii) del plan.
- Con e0-r2 cambia la fuente (texto o herencia) de 41 unidades, las mismas 41 de R1.d
  (`r2_codigo/r1d_censo_requests.json`, `a01c491`).

**Reglas del bloque** (`p1/mensaje_r2_borrador.py`, `bloque_flags`):
1. **Tablas serializadas.** Si el chunk tiene alguna, el mensaje abre con «TABLAS SERIALIZADAS POR E0 en
   el texto (CONFIABLES: leelas y copiá sus valores, ver CONTENIDO NO-PROSA del sistema):» y una línea por
   tabla, graduada por sus metadatos (decisión 6):
   - modo posicional: avisa que las claves son `colN` y que el nombre de cada columna está en las primeras
     filas del bloque;
   - celdas propagadas y celdas con alcance: las cuenta y nombra su marca;
   - filas de subtítulo: «ATENCIÓN, 1 fila de subtítulo: no es un dato; califica a las filas que la
     siguen.» (en plural: «no son datos; cada una califica a las filas que la siguen»);
   - celdas combinadas sin asignar: «ATENCIÓN, 1 celda combinada que E0 no asignó a sus filas: su valor
     puede valer para varias filas y el bloque no indica cuáles. Si el texto no lo aclara, no lo asocies a
     ninguna fila: registrá la omisión `tabla` con su tramo.» (en plural: «el valor de cada una puede
     valer para varias filas»);
   - sin nada de eso: «confiable, sin celdas combinadas».
   Todas las cantidades concuerdan en número («1 fila», «3 filas»; «1 celda», «18 celdas»).
2. **Residual y fórmulas.** Si `contenido_tabular_residual` es verdadero, o falta la clave y
   `contenido_tabular` es verdadero, o hay `formula`: la línea «FLAGS E0» de hoy, con «contenido tabular
   fuera de los bloques confiables» cuando también hay bloques, y con la omisión en `omisiones` y su
   categoría. Si hay tablas detectadas sin serializar, una línea que las nombra.
3. **Evidencia.** Las líneas de `evidencia_formula` se imprimen como hoy. Las de `evidencia_tabular` se
   imprimen solo si hay contenido tabular residual, y solo las que siguen en el texto propio o heredado.
   Con residual falso no se imprime ninguna: o las reemplazó el bloque, o la heurística de E0 ya no las
   ve como tabulares fuera de los bloques. Resultado: 23 líneas impresas y 70 suprimidas (confirmado por la
   autora, 03/10/2026).
4. **Tablas forzadas a residual, en código** (decisión de la autora, 03/10/2026). Una lista explícita de
   tablas (`TABLAS_RESIDUALES_FORZADAS`, ids de `flags.tablas_e0[].tabla`; hoy vacía) pasa a residual una
   tabla serializada: sale de la lista de confiables, el chunk queda con residual verdadero y el mensaje
   la nombra: «Tablas serializadas por E0 que se tratan como contenido NO-CONFIABLE (`<id>`): no copies
   sus valores; registrá la omisión `tabla` con su tramo.». El prefijo ya contempla el caso (R21: el
   residual incluye «una tabla serializada que el mensaje declare no confiable»), así que usar la lista no
   lo cambia: cambia solo el mensaje, y la clave de caché, de las unidades que traen esa tabla, sin abrir la
   ventana. En P2 la lista vive en un archivo versionado que lee el módulo del perfil, con la tabla, el
   motivo y la fecha de cada alta. Demostración con `cap::tabla037` en `p1/salida/ejemplos_mensaje_r2.md`.

Ejemplos completos, sellado y nuevo, en `p1/salida/ejemplos_mensaje_r2.md`: `cap::1.2` (tabla simple, la
de `BKL-0006`), `ric::9.2.1` (el cuadro de códigos), `cap::6.2.2.6` (aviso de riesgo), `cap::4.2.1.2`
(serializadas y residual), `ric::S2` (tabla sin serializar), `cap::2.13` (sin la clave residual),
`ric::11.2.3` (bloque heredado) y `cla::5.1.1.1` (sin tabla), más `cap::6.2.2.6` con `cap::tabla037` en la
lista de tablas forzadas a residual.

**Un caso que muestra por qué hace falta el aviso.** En `cap::6.2.2.6` (tabla de desestimaciones
horizontales, posicional, 20 celdas combinadas sin propagar), el bloque pone porcentajes de las columnas
«entre zonas» sobre las filas de subtítulo «Años*»: la serialización conserva cada celda, pero no a qué
filas se aplica un valor que el PDF combina entre zonas. Decidido (03/10/2026): aviso, no residual. El
aviso le dice al modelo que la fila de subtítulo califica a las que siguen y que un valor combinado que el
texto no aclara no se asocia y se registra como omisión. `cap::6.2.2.6` entra como caso fijo de P4: si la
pareada muestra la asociación mal hecha en `cap::tabla037`, esa tabla pasa a la lista de tablas forzadas a
residual antes de U-REEXT-T0.

### 4.3 NOTA del mensaje de E3 (`prompt_e3.py:241`)

Fuera del prefijo de E3 (`p1/mensaje_r2_borrador.py`, `nota_e3_r2`; la NOTA de hoy, reproducida en
`nota_e3_sellada`, coincide byte a byte con la de `prompt_e3.build_user_message` en los 70 chunks marcados
de la E0 legada):
- con tabla serializada: «NOTA: esta unidad tiene tablas serializadas por E0 (bloques [TABLA …] … [FIN
  TABLA …] del texto fuente, verificados contra el documento): su contenido es texto confiable y su
  omisión se evalúa como la de cualquier otro contenido.»; si alguna tabla lleva aviso de riesgo (decisión
  de la autora, 03/10/2026): «E0 dejó sin resolver parte de la estructura de `<id>` (20 celdas combinadas
  sin asignar a sus filas y 1 fila de subtítulo): la omisión `tabla` que el extractor declare sobre esa
  tabla no es faltante.», con el detalle por tabla y la concordancia de número; si además hay residual o
  fórmulas: «Además, E0
  detectó en esta unidad … (flag determinístico): el extractor tenía instrucción de NO reconstruir ese
  contenido y declarar las omisiones; ese contenido normativo ni extraído ni declarado es faltante tipo
  contenido_tabular_no_declarado; declarado, no.»;
- sin tabla serializada confiable (incluida una tabla forzada a residual): la NOTA de hoy, sin cambios.

**Censo** (`censo_p1.json`, `nota_e3`): la NOTA cambia en **38 chunks**: los 37 con tabla serializada y
`ric::S2`, que la E0 legada no marcaba y e0-r2 sí (la NOTA es la de hoy; cambia porque aparece, y queda
así: aclaración de la autora del 03/10/2026). 8 de los 38 llevan la oración de la omisión `tabla`
(`ric::4.3.3`, `ric::10.2`, `ric::11.1.1`, `ric::11.2::intro`, `ric::11.2.3`, `cap::5.3.2.3`, `cap::6.2.2.4`
y `cap::6.2.2.6`). Agrega 5.315 caracteres en total. Si solo cambiara la NOTA, esas 38 unidades pagarían E3
de nuevo: ≈ USD 0,35 al promedio de E3 de la tanda 0 (USD 22,28 entre 2.427 unidades). Los tokens de la
NOTA cuestan USD 0,003. En U-REEXT-T0 ese costo ya está dentro de E3 completo, porque la clave de E3 cambia en todas las
unidades (§1).

### 4.4 Qué ve E3 en r2b: un hueco del mandato

E3 y el ratchet no leen la validación del perfil r2, sino la del validador de E1 legado:
`runner_corpus.py:567` y `ratchet_e3.py:279` llaman a `validador_e1.validar_salida` con el `esquema` del
perfil, y `comun_e3.render_extraccion` renderiza `properties` y `omisiones_no_prosa` (`comun_e3.py:186`).
Con la salida del prefijo nuevo eso falla de tres maneras:
1. una relación de sujeto con mención y sin `sujeto_id` se rechaza («requiere exactamente UNO de
   sujeto_id/sujeto_propuesto», `validador_e1.py:302`), así que E3 no la ve y puede reclamarla como
   faltante;
2. `umbrales`, `tramo` y `otras_propiedades` están fuera de `properties` (`validador_e1.py:202` solo lee
   `properties`), así que E3 no ve las cuantías y puede reportar calificadores despojados;
3. `omisiones` no es `omisiones_no_prosa`, así que E3 no ve las omisiones declaradas y puede reportar
   `contenido_tabular_no_declarado`.
Las firmas nuevas de `condicion_de` pasan si el `esquema` del perfil nuevo usa `modelos_r2.firma_r2`
(`perfil_e1.py`, escritura autorizada). Lo demás exige leer la forma r2 en la validación de la fase E1,
y los tres archivos que la hacen (`validador_e1.py`, `ratchet_e3.py`, `comun_e3.py`) no estaban entre las
escrituras del mandato firmado. El cambio: en `validador_e1.py`, una proyección de la forma r2 a la forma
que leen E3 y el ratchet, detrás del `esquema` del perfil, con el camino por defecto byte a byte igual
(la mención sin id como `sujeto_propuesto`, los tramos de umbral como properties legibles, las omisiones
como strings con su categoría; el tramo de evidencia no se traduce). La nota `a807136` suma
`validador_e1.py` y `selftest_e1.py` a las escrituras. Autorizada para P2 (decisión de la autora del
03/10/2026; §10.2, punto 4).

### 4.5 Composición con el encabezado de una lista (F1-A)

**Qué se adopta** (decisión de la autora del 03/10/2026; nota al pie del mandato, `a807136`). El problema F1
de U-DIAG-PROCESO es la pérdida de la norma del encabezado que completan los incisos
(`git show 93ce4b7:reports/u_diag_proceso/reporte_u_diag_proceso.md`, §1 y §5). De su opción F1-A entra la
primera mitad: cada inciso extrae la norma compuesta con su encabezado heredado (sujeto, modalidad y
cuantificador, «todos» o «cualquiera de las alternativas»), y la unidad del encabezado no emite nodo por el
solo anuncio de la lista (condición de cierre de `BKL-0035`). La segunda mitad, que hacía emitir el deber a la
unidad del encabezado, no se adopta: contradice esa condición de cierre.

**Por tipo de ítem** (punto 18 del §10, aprobado por la autora el 03/10/2026; nota al pie del mandato en el
árbol de trabajo, sin commit al 03/10/2026). R30 distingue qué son los ítems:
- **Contenidos** (lo que hay que hacer, informar, incluir o cumplir, o los miembros de una clase): el ítem
  compone la norma del encabezado. Si el último encabezado no trae la modalidad o el sujeto, se toman del
  bloque heredado más cercano que los trae.
- **Lo que el encabezado fija para cada ítem** (un plazo, un ámbito, una condición que vale para todos):
  también se compone en el ítem, haya o no unidad del encabezado. El plazo va como elemento de `umbrales` de
  la norma compuesta, y la condición como Condicion del ítem con `condicion_de` hacia ella. Su `tramo` es el
  segmento del encabezado, tomado del heredado.
- **Supuestos o condiciones de una norma del encabezado:** el ítem es una Condicion y la norma queda en la
  unidad del encabezado. Si el encabezado está en la línea de título, no tiene unidad:
  - con supuestos alternativos, la norma se compone en cada ítem con su cuantificador;
  - con condiciones conjuntas, o si no queda claro, no se compone, y la norma principal queda como límite
    declarado. Ante la duda, se tratan como conjuntas.

**Por qué hay que levantar la prohibición.** El prefijo sellado prohíbe extraer del contexto heredado
(`prompt_e1.py:52`, `:122`; mensaje, `:479-481`) porque supone que cada bloque heredado tiene su propia
unidad. Cuando el encabezado está en la línea de título del punto, esa unidad no existe: E0 no emite
mini-chunk sin segmento de prosa (ficha 11, `ayccef::4.2.7.2`; anexo de U-DIAG-PROCESO, §2). Para ese caso la
prohibición deja la norma sin unidad que la extraiga.

**Dónde vive en el borrador** (§2):
- R28 (encabezado del prefijo, chunk de punto): la regla «extraés solo del texto del punto» gana la
  excepción del ítem de lista.
- R29 (PROVENANCE): la excepción, con su motivo (el encabezado puede no tener unidad propia y, cuando la
  tiene, esa unidad no extrae la norma de los ítems).
- R30 (sección nueva COMPOSICIÓN CON EL ENCABEZADO DE UNA LISTA, antes de REGLAS): el tratamiento por tipo
  de ítem; el sujeto del encabezado en `aplica_a` o `ejecuta`, con la mención copiada del encabezado; lo que
  el encabezado fija para cada ítem; el `tramo`; y qué extrae, y qué no, la unidad del encabezado.
- R16 (regla 1): no son entidades ni el anuncio de una lista ni lo que se compone en los ítems. Lo que el
  encabezado enuncia aparte de la lista (una norma propia, una excepción a la lista entera, la norma
  principal cuando los ítems son sus supuestos o condiciones) se extrae en su unidad.
- R11 (COPIA LITERAL): el tramo es «un solo tramo continuo», salvo en la norma compuesta, y sale del
  heredado cuando se compone desde el encabezado.
- Mensaje (§4.1): en un ítem, el rótulo del contexto heredado nombra la excepción. Un ítem es un chunk de
  punto cuyo último bloque heredado termina en «:» (definición de U-DIAG-PROCESO,
  `reports/u_diag_proceso/code/censo_estructural.py`, `93ce4b7`; `p1/mensaje_r2_borrador.py`, `es_item`).
  En la tanda 0 son 706 de las 2.434 unidades (`censo_p1.json`, `agregados.items`), los mismos 706 que
  cuenta U-DIAG-PROCESO (reporte, §3).

**Tramo de la entidad compuesta.** El encabezado y el inciso no son texto contiguo, así que el `tramo` de
la entidad compuesta lleva dos segmentos copiados tal cual, unidos por « […] »: primero el del encabezado,
tomado del contexto heredado; después el del ítem, tomado del texto propio. No cambia el tool schema
(`tramo` sigue siendo un string). El separador no aparece en el texto propio ni en el heredado de ninguna
unidad, con ninguna de las dos E0 (`censo_p1.json`, `control_separador_f1a`: 0 en la legada, 0 en e0-r2, y 0
para «[...]»), así que partir el tramo por él no es ambiguo. La verificación en código (P3) está en §8.2.

**Ejemplo** (`p1/salida/ejemplos_mensaje_r2.md`, `ctacte::2.3.4.1`): un inciso que en la tanda 0 salió sin el
deber del encabezado, mientras sus hermanos sí lo componían (reporte de U-DIAG-PROCESO, §3).

**Límite declarado** (decisión de la autora, 03/10/2026). En un encabezado en línea de título sin unidad
propia que enuncia condiciones conjuntas, la norma principal no se extrae. En la tanda 0 no hay ninguno (0 de
10), y en la partición hay 1 candidato de 87 (`gracre::2.2.9`, proxy). La clasificación de los 10 está en el
§10.2, punto 18.

**Un encabezado con condición propia: `ext::4.8.6::intro`** (`p1/salida/ejemplos_mensaje_r2.md`).
- La cláusula empieza en la línea de título y sigue en el párrafo con unidad propia: «En el caso de que un
  cliente haya concretado una operación de venta con obligación de recompra utilizando los bonos BOPREAL
  adquiridos en una suscripción primaria complementariamente será aplicable lo siguiente:».
- Los tres ítems (`ext::4.8.6.1` a `.3`) son normas que valen en ese caso. La condición vale para cada uno:
  es de tipo (ii).
- Lo que extrae cada unidad con el borrador:
  - cada ítem, su norma y una Condicion con `condicion_de` hacia ella. El `tramo` de la Condicion es el
    segmento del encabezado, que abarca los dos bloques heredados seguidos (la línea de título y el párrafo);
  - la unidad del encabezado no emite nada más que el TextoOrdenado, porque todo lo que enuncia se compone en
    los ítems.
- E3 sobre la unidad del encabezado:
  - la NOTA le dice que la condición que vale para cada ítem se compone en los ítems y que su ausencia ahí
    no es faltante;
  - si igual la reclama citando la cláusula dentro del bloque (en la tanda 0 citó «de recompra utilizando
    … será aplicable lo siguiente:», dentro del bloque), la guarda la exime, porque la unidad quedó sin
    Obligacion, Restriccion ni Potestad.
- En la tanda 0 sin la regla, la primera pasada la dejó vacía y el reintento creó una Condicion en el
  encabezado.
- Con el borrador, la condición queda tres veces, una por ítem, cada una atada a su norma; en el encabezado
  no queda. No es un duplicado: cada Condicion condiciona una norma distinta.

**Ventana.** Declaración de la autora (nota `a807136`): F1 entra en el ciclo de la ventana aunque la destapó
ESQ-2 y no la tanda 0, como el desvío del §2.4 de la enmienda de uso de la ventana (`30f106c`, `:61-64`); sus
fichas son de TOs ya excluidos de B6.3 (a), así que no reduce el conjunto de evaluación.

**Medición en P4** (nota `a807136`). Fuera del sorteo, los chunks de las cinco fichas de F1 miden que la regla
corrige los casos que la motivaron; se reportan aparte de los 40 sorteados y del estrato fuera de muestra:

| Ficha (ESQ-2) | Chunk | Forma (anexo de U-DIAG-PROCESO, §2) |
|---|---|---|
| 11 | `ayccef::4.2.7.2` | (a) encabezado en la línea de título de 4.2.7, sin unidad propia |
| 13 | `expaef::6.6.2` | (b) composición parcial |
| 48 | `ayccef::3.4.1` | (b) inciso vacío; ficha contaminada (anexo, §2) |
| 52 | `expaef::1.1.2.5` | (b) sin composición, operación inventada |
| 64 | `adrei::4.3.1::intro` | (c) encabezado con unidad propia, extraído vacío |

La ficha 64 es la unidad de un encabezado: con la regla no emite nodo, y se mide por sus incisos
(`adrei::4.3.1.1`, `.2` y `.3`). Son 8 chunks; como los del estrato fuera de muestra, no tienen salida del
prefijo sellado en la caché: los dos brazos corren por la API, el sellado sobre la E0 legada y el nuevo sobre
e0-r2, las dos producidas en el scratchpad (P4.b). Qué se lee: la norma del encabezado representada en cada
inciso, con su cuantificador; el sujeto del encabezado en la relación; el tramo compuesto verificado en sus
dos segmentos; ninguna operación inventada; y ningún nodo de solo anuncio en `adrei::4.3.1::intro`. La
generalización se lee en los ítems que caigan en el sorteo de los 40, reportados aparte del resto de la
muestra. En los dos brazos se cuentan, además, las Condicion de ítems sin `condicion_de` (R8; decisión de la
autora en el FRENO P1).

#### La unidad del encabezado y E3 (`BKL-0035`)

Insumo: `p1/encabezados_lista.py` → `p1/salida/encabezados_lista.json` y `.md`, sobre la primera pasada de E1,
los veredictos de E3 y el estado final de la tanda 0 (`corpus_tanda0/salida/<to>/`, `ad6d5ad`). Un encabezado de
lista con unidad propia es un mini-chunk intro o chapeau_seccion cuyo texto termina en «:» (definición de
U-DIAG-PROCESO); la tanda 0 tiene 212, los mismos en la E0 legada y en e0-r2.

**Qué pasó en la tanda 0.**
- En la primera pasada, E1 dejó 9 de los 212 sin contenido.
- E3 bloqueó 6 de esos 9, todos con un faltante `otro` de severidad alta:
  - 5 quedaron aceptados tras el reintento, con nodos que creó el reintento. En `ctacte::8.3::intro` y
    `8.4::intro` es la Obligacion de solo anuncio de `BKL-0035`.
  - 1 fue a cola humana (`lingob::6.2.4::intro`).
- Los otros 3 se aceptaron vacíos: `ext::5.5::intro`, `ext::S15::chapeau_seccion` y `ext::S6::chapeau_seccion`.
- Dónde está la cita de los 6 bloqueos:
  - en 4, la cita es la cláusula que abre la lista, dentro del bloque;
  - en los otros 2 (`ctacte::1.5.4::intro` y `ctacte::3.2.1::intro`), la cláusula empieza en la línea de título,
    y la cita también. En los dos el encabezado tiene contenido propio: una condición («siempre que medie
    autorización expresa del cliente») y la norma principal (la falta de esas especificaciones quita al título
    el valor de cheque).
- La guarda LAUDO B (`ratchet_e3.py:102-118`) no eximió ninguno: exime solo el tipo `enumeracion_incompleta`.
- E3 también reclama la cláusula cuando la unidad tiene contenido. En la verificación, 23 faltantes
  bloqueantes de los 212 encabezados citan la cláusula dentro del bloque: 17 `otro`, 4
  `contenido_tabular_no_declarado` y 2 `excepcion_ausente` (`e3_en_minis_ordenadores`). Leí sus notas:
  - todos menos uno reclaman los ítems, que están en los puntos hijos;
  - el otro, en `ext::9.3.3::intro`, reclama una restricción propia del encabezado («sólo en la medida que se
    verifique alguna de las siguientes situaciones»).

**Cuántos quedarían vacíos con la regla 1.** Es una proxy textual sobre e0-r2, NO MEDIDA
(`proyeccion_regla1`). La cláusula se toma completa: si empieza en la línea de título de la misma unidad, se
le une esa parte. De los 212:
- 88 tienen texto además de la cláusula que abre la lista: conservan contenido;
- 30 anuncian casos, supuestos o condiciones. Por R30, los ítems son Condicion y la unidad conserva la norma
  principal;
- 30 son solo la cláusula, con una marca de plazo o de condición. Son dudosos: lo que vale para cada ítem no
  tiene dónde ir si la unidad no emite la norma (§10.1, punto 18, tipo (ii));
- 64 son solo la cláusula, sin marca: quedarían vacíos.
Estimo 64 vacíos, y hasta 94 con los dudosos. En la primera pasada de la tanda 0, 56 de esos 64 tenían
contenido: es lo que la regla 1 les quita.

**Qué haría E3 con ellos.** El prefijo de E3 y su NOTA de hoy no cambian. Si E3 trata a esos vacíos como a
los 9 de la tanda 0 (6 de 9 bloqueados), serían del orden de 40 bloqueos. Es una extrapolación desde n = 9:
da un orden de magnitud, no es una medición. Cada bloqueo lleva a un reintento, y el reintento crea nodos.
En la tanda 0, 5 de los 6 reintentos crearon nodos:
- 2 de solo anuncio, justo los que prohíbe la regla 1 (`ctacte::8.3::intro` y `8.4::intro`);
- 3 con contenido propio del encabezado: una condición o la norma principal (`ctacte::1.5.4::intro`,
  `ctacte::3.2.1::intro` y `ext::4.8.6::intro`).

**Salida (a): NOTA de E3 para los encabezados de lista.**
- **Qué escribe.**
  - En `prompt_e3.py`, dentro de `build_user_message` (`:224-263`): una NOTA más, que se suma a la de tablas
    cuando la unidad es un encabezado de lista.
  - En `validador_e1.py`, dentro de la proyección «r2» ya autorizada: la validación que devuelve lleva la
    marca `forma_salida: "r2"`. Así la NOTA aparece solo con la salida nueva.
- **Borrador** (`p1/mensaje_r2_borrador.py`, `nota_e3_encabezado_r2`), alineado con el tratamiento por tipo:
  «NOTA: esta unidad es el encabezado de una lista (su texto termina en «:»); los ítems son los puntos que siguen, cada uno con su propia unidad. En esta extracción se componen en cada ítem el sujeto, la modalidad y el cuantificador del encabezado, y también lo que el encabezado fija para cada ítem (un plazo, un ámbito, una condición que vale para todos los ítems). Esta unidad no emite un nodo por el solo anuncio de la lista ni repite lo que se compone en los ítems: que falten aquí no es faltante. Sí es faltante, si no fue extraído, lo que el encabezado enuncia aparte de la lista: una norma propia, una excepción a la lista entera, o la norma principal cuando los ítems son sus supuestos o condiciones.»
  No dice que sea faltante en el encabezado nada de lo que los ítems componen.
- **Perfiles existentes.** Su validación no lleva la marca, así que el mensaje de E3 queda byte a byte igual
  (`selftest_manifiesto.py`, P3 y P4). El prefijo de E3 y su candado no cambian.
- **Costo.** 212 unidades, 706 caracteres por NOTA: ≈ USD 0,09 de entrada de E3 en U-REEXT-T0
  (`nota_e3_encabezado`).
- **No-filtración.** 0 coincidencias en las ventanas del texto fijo del mensaje (`nofiltracion_mensaje.json`).
- **Qué no hace.** Reduce los reclamos, no los impide. Su efecto no se mide antes de U-REEXT-T0, porque P4
  corre E1 solo.
- **Escritura.** El mandato firmado autoriza `prompt_e3.py` solo para la NOTA de las tablas
  (`git show b901f6d:docs/mandatos/UPROMPT_R2_prefijo_nuevo.md`, `:40` y `:281-282`). Esta NOTA la aprobó la
  autora el 03/10/2026. La nota al pie del mandato que la suma a las escrituras está en el árbol de trabajo:
  su commit es PENDIENTE.
- **Alternativas.** Ninguna evita escribir `prompt_e3.py`. El prefijo de E3 está sellado con candado y el
  mensaje es su única parte variable. Poner el aviso en el render de la extracción
  (`comun_e3.render_extraccion`) obliga a escribir `comun_e3.py`, que también está fuera de las escrituras, y
  mezcla el aviso con lo extraído.

**Salida (b): guarda LAUDO B ampliada.**
- **Qué escribe.**
  - En `ratchet_e3.py`:
    - `_guardia_estructural` (`:102-118`) deja de exigir el tipo `enumeracion_incompleta` cuando la ampliación
      está activa. Las demás condiciones no cambian: mini ordenador, descendientes en el corpus, y cita
      verificada que termina en «:» y está dentro del bloque.
    - `evaluar_veredicto` (`:121`) recibe la validación verificada y activa la ampliación solo si esa
      validación trae la marca `forma_salida: "r2"`.
    - `ciclo_ratchet` le pasa la validación en la verificación (`:384`) y en la re-verificación (`:426`).
  - En `selftest_e3.py`: casos nuevos; los existentes no cambian.
  - En `runner_corpus.py:862` (`claves_reintentos_cache`, escritura autorizada): le pasa la misma validación,
    para que coincida la clave reconstruida del reintento.
- **Salvaguarda** (aprobada). La ampliación aplica solo si la validación verificada no tiene Obligacion,
  Restriccion ni Potestad, es decir, si la unidad quedó como la deja la regla 1.
- **Registro de cada exención** (condición de la autora: el reporte de U-REEXT-T0 lista cada unidad eximida
  para leerla). Sin marca nueva, por decisión de la autora en el FRENO P1. Las exenciones de la ampliación son
  los faltantes `estructural_no_bloqueante` de tipo distinto de `enumeracion_incompleta`:
  - en el perfil r2b, `runner_corpus.py` las lista en `resumen_e3.json` (`exenciones_ampliacion_laudo_b`, con
    la unidad, la fase, la cita y el tipo, y `unidades_eximidas_ampliacion`);
  - el reporte de U-REEXT-T0 copia esa lista;
  - en los perfiles existentes, el resumen no cambia.
- **Recuento sobre la tanda 0** (`guarda_ampliada_tanda0`; los 212 tienen descendientes):
  - En la verificación hubo 32 encabezados con algún faltante bloqueante.
  - Sin la salvaguarda, la ampliación habría desbloqueado 22 de los 32: 17 que se reintentaron y 5 que fueron
    a cola humana. En la re-verificación, 4 de 4, los cuatro de cola humana.
  - Con la salvaguarda habría desbloqueado 5: `ctacte::6.4.7::intro`, `ctacte::8.3::intro`, `ctacte::8.4::intro`,
    `ext::4.8.6::intro` y `lingob::6.2.4::intro`.
  - Sin salvaguarda se desbloquea también `ext::9.3.3::intro`, cuyo reclamo es legítimo. Con ella sigue
    bloqueando, porque su extracción tenía la Potestad.
- **Qué garantiza.** Si la unidad del encabezado sale sin norma y E3 la reclama citando la cláusula dentro del
  bloque, no hay reintento: la unidad se acepta con el faltante como residual declarado, y ningún reintento
  crea el nodo.
  - No cubre la cita que empieza en la línea de título (2 de los 6 bloqueos de la tanda 0), y no debe
    cubrirla: en esos dos el encabezado tenía contenido propio.
- **Perfiles existentes.** Sin la marca, la guarda es la de hoy. `r1_cola_flaggeada.py`,
  `recompute_politica_enm01.py` y `reextraccion_dirigida.py` la llaman sin validación, así que no cambian.
- **Costo.** USD 0 en sí misma. Ahorra el ciclo de reintento de cada bloqueo que exime: ≈ USD 0,020 a la
  tarifa r2, de E1 0,0126 más E3 0,0074 (`costo_ciclo_de_reintento_usd`). Con unos 40 bloqueos son
  ≈ USD 0,8 menos, que la estimación del §7 no descuenta.
- **Escritura.** La autora aprobó la ampliación con la salvaguarda el 03/10/2026. LAUDO B es una política
  laudada del ratchet (`ratchet_e3.py:44-53`, laudos del 11/08/2026), así que la regla la fija una enmienda.
  - La enmienda (`docs/enmienda_laudo_B_guarda_ratchet_2026-10-03.md`) está en el árbol de trabajo como
    borrador sin firma. Su firma y su commit son PENDIENTES de la autora.
  - La nota al pie del mandato que suma `ratchet_e3.py` y `selftest_e3.py` a las escrituras está en el árbol
    de trabajo. Su commit es PENDIENTE.
  - La entrada `BKL-0039` (`ctacte::6.4.7::intro`, de la misma especie que `BKL-0035`) también está en el
    árbol de `data/backlog/backlog.jsonl`, sin commit.
  - Lo especificado acá coincide con lo que fija la enmienda (§2, puntos 1 a 6).
- **Alternativas.** Ninguna da la misma garantía sin escribir `ratchet_e3.py`:
  - la NOTA sola reduce los reclamos, pero no los impide;
  - marcar o descartar en `validador_r2` (autorizado) el nodo de solo anuncio que cree el reintento haría
    cumplir al grafo por construcción. Pero la condición de cierre de `BKL-0035` se mide sobre la extracción
    final (ver abajo), así que la ocultaría en lugar de cumplirla;
  - saltear E3 en esas unidades pierde los reclamos legítimos sobre el contenido propio del encabezado.

**Las dos juntas** (aprobadas por la autora el 03/10/2026; §10.2, punto 20). La NOTA baja los reclamos, y con
ellos los faltantes residuales que quedan en el registro. La guarda asegura que un reclamo que llegue igual no
termine en el nodo.

**Pata de E3 en P4** (aprobada por la autora el 03/10/2026). Corre E3 con la NOTA y la guarda, en el ciclo
completo del ratchet, sobre cuatro encabezados de lista: `ctacte::8.3::intro`, `ctacte::8.4::intro`,
`ctacte::6.4.7::intro` y `adrei::4.3.1::intro`. Se reporta aparte de lo demás.
- **E1.** Los tres de la tanda 0 entran como casos de control de la especie de `BKL-0035` (`BKL-0039` para
  `ctacte::6.4.7::intro`). El brazo sellado sale de la caché y el nuevo corre por la API. `adrei::4.3.1::intro`
  ya está entre los casos de F1.
- **Qué se lee:**
  - si E1 deja vacía la unidad del encabezado;
  - si E3 la reclama;
  - si la guarda exime el reclamo, listando cada exención;
  - si un reintento crea el nodo.
- **Costo** (`censo_p1.json`, `estimacion_p4.total`):
  - E1 nuevo de los tres casos de control: USD 0,014;
  - pata de E3, central (solo la verificación, porque la guarda exime): 0,058;
  - pata de E3, alta (además un reintento de E1 y una re-verificación por unidad): 0,140.
  - Base: una escritura del prefijo de E3 (≈ 11.637 tokens) y, por llamada, la media de la tanda 0 más la
    NOTA.

**Límite de la proxy de vacíos.** La proxy clasifica `ext::4.8.6::intro` como «sin marca», aunque su
encabezado abre con una condición. Su lista de marcas tiene «en caso», pero no «en el caso de que» ni «en los
casos en que». Con esa marca sumada, la clase baja de 64 a 63 (`proyeccion_regla1.limite_de_la_proxy`).
Ese es el único caso en la clase. La estimación sigue siendo una proxy textual: NO MEDIDA.

**Dónde se mide `BKL-0035`.** Su condición de cierre se mide sobre la extracción final de U-REEXT-T0, después
de E3 y del reintento, no sobre la primera pasada de E1. P4 corre E1 solo (decisión 18) y no ve lo que hace el
ratchet. En la pareada, `adrei::4.3.1::intro` y los encabezados que caigan en el sorteo dicen si E1 cumple la
regla 1, no si el nodo sobrevive a E3. El plan dice lo mismo en la fila de U-REEXT-T0
(`git show 91a6dba:docs/plan_tesis.md`, `:400`), y el backlog lo registra como nota de `BKL-0035` en el mismo
commit.

### 4.6 Instrucción de umbrales con la columna r2a (M2 de U-MED-R2A)

**Fuente.** El FRENO M2 de U-MED-R2A, commiteado en `c50b094`
(`git show c50b094:data/experiment/medicion_r2a/m2_freno.md`, sha256 `b2e18874…`), fila :67 del tablero:
- 7 nodos de 689 tienen cuantía y ningún elemento de umbral (diez);
- 26 Restricciones `limite_cuantitativo` de 301 no tienen lista ni marca: son la S18 «aparte»
  (`m2/m2_medicion.json`, `f67_cuantias` y `f67_limites_relativos_s18`).
Leí los 33 nodos en el grafo r2a (`ens_diez_r2a/r2/kg.json`, sha256 `99fe2bfa…`, el mismo de M1).

**Lo que muestran.**
- **De los 7 sin elemento, 6 no son umbrales:**
  - 5 son la cantidad de decimales con que se informa o se publica una tasa (cinco Obligaciones de ctacte);
  - 1 es el término de un cálculo (los días que eligen un factor, en cap).
  - El séptimo sí es un umbral: el plazo mínimo que define el supuesto de una Condicion (ext).
- **Los 26 límites, por lectura propia:**
  - la mayoría se comparan con otra magnitud: el nivel alcanzado en un mes, el monto que corresponde según
    otra norma, un precio de referencia, la exigencia que resultaría de otro cálculo;
  - en algunos el tope es un múltiplo de otra magnitud («el doble de»);
  - en otros remiten a un límite fijado en otro punto;
  - 3 no son límites: la definición de un exceso, la consecuencia de un incumplimiento, y un encabezado de
    lista con un valor inventado entre corchetes.

**Cambios en R11 (UMBRALES).**
- La lista es de cuantías «que acotan la norma».
- La Condicion lleva como elemento la cuantía que define su supuesto.
- El límite relativo suma los múltiplos y fracciones de otra magnitud y el límite fijado en otro punto o en otra
  norma. En ese caso el tramo es el de la referencia, y la remisión la registra el código.
- No son cuantías de la norma la precisión con que se informa un dato ni un término de un cálculo.
- Una Restriccion `limite_cuantitativo` tiene al menos un elemento: si no hay ninguno, se revisa el tipo.
- La cuantía de los ítems de una lista va en cada ítem, no en el encabezado.
El texto describe los patrones sin citar los chunks (regla de no-filtración, §5). No cambia el tool schema ni
el código del par B: el tramo de un umbral ya se verifica contra el texto propio y el heredado
(`ensamblar_tanda0.py:620-626` y `:732`), y eso cubre el plazo compuesto desde un encabezado.

## 5. Dónde se implementa cada decisión

| Decisión | Prefijo (§2) | Tool schema (§3) | Mensaje (§4) | Código (P2 y P3) |
|---|---|---|---|---|
| 3 umbrales, par A | R4, R5, R6, R9, R11 (UMBRALES, ajustada con la columna r2a: §4.6) | `umbrales[].tramo` (U-PYD) | — | `llenar_umbrales_r2` ya lee `tramos_e1` (`ensamblar_tanda0.py:663`, `:699`) y verifica contra el texto propio y heredado (`:620-626`, `:732`) |
| 4 sujetos | R12, R13, R15, R18, R23, R24 | `sujeto_mencion`; sin `sujeto_propuesto` (U-PYD) | alcance | resolución R1 a R4 (U-R2-CODIGO) |
| 5 omisiones | R0, R17, R19, R20, R21, R22, R26 | `omisiones` (U-PYD) | fórmulas | registro de omisiones (P3) |
| 6 tablas | R11 (cuantía de tabla), R21 | — | bloque de tablas (§4.2) | lista de tablas forzadas a residual (§4.2, regla 4) |
| 7 matriz | R7, R8, R14 | sin cambio (la matriz no está en el tool schema) | — | `firma_r2` en el `esquema` del perfil |
| 8 «externa» | R1 (normas externas en Comunicacion) | sale `tipo` (decisión 16) | — | derivación desde `codigo` (`validador_r2.derivar_comunicacion`) |
| 9 destino de `limita` | R25 | — | — | — |
| 10 catálogo | R27; R15 (sujetos del exterior) | enum de 110 ids (U-PYD) | — | LN-8 |
| 11 calificadores | R15 («sujeto alcanzado y calificador»), R3 | — | — | RT-C6-5 en la suite |
| 12 `remite_a` fuera | R14 (las remisiones las registra el código) | 13 predicados, sin `remite_a` | — | — |
| 15 tramo de evidencia | R11 (COPIA LITERAL), R5, R26 | `tramo` en 8 tipos | cierre | verificación (§8.2) |
| 16 campos derivados | R1, R2, R10 | salen 5 campos; `termino` literal | — | derivación (P3) |
| 17 válvulas | R11 (`otras_propiedades`), R17, R26 | `otras_propiedades` en relaciones; `source` y `destino` | — | aristas con no definidas (P3) |
| 20 `frecuencia` | R6, variantes A y B | ver §9 | — | `frecuencia_desde_tramo` |
| 21 límites relativos | R11 («Límite relativo», con múltiplos y límites de otro punto; §4.6) | — | — | elemento sin valor: ver §10, punto 5 |
| BKL-0038 (P1.a) | R23, R25 | — | — | marca de coherencia (U-PYD) |
| F1-A, encabezado de lista, por tipo de ítem (§4.5) | R28, R29, R30; R16 (regla 1); R11 (tramo de dos segmentos, tramo del heredado) | sin cambio (`tramo` sigue siendo un string) | rótulo del contexto heredado del ítem | verificación del tramo compuesto y del tramo heredado (§8.2, P3) |
| E3 y la unidad del encabezado (§4.5) | — | — | NOTA de E3 de los encabezados de lista (`prompt_e3.py`) | marca `forma_salida` (`validador_e1.py`); guarda ampliada con salvaguarda y marca `guarda_ampliada` (`ratchet_e3.py`, `selftest_e3.py`); lista de exenciones (`runner_corpus.py`) |

**No-filtración** (regla de ESQ-3b, `data/experiment/esq/prerregistro_esq3b_v2.md:42-50` y `:177-184`),
contra las ventanas de 5 palabras de los 2.942 chunks de los diez TOs y de los cuatro TOs del estrato fuera
de muestra: **0 en las instrucciones nuevas y en el mensaje; 19 del bloque de catálogo, declaradas**
(contenido decidido por U-CAT-UNICO; `p1/salida/nofiltracion_A.json`, `choques_por_origen`, y
`p1/salida/nofiltracion_mensaje.json`). Bigramas y trigramas distintivos de los casos de control (los fijos de
P4, los de X5 y los ocho chunks de F1, sobre su texto propio y heredado): 0 en las instrucciones nuevas; en
el bloque de catálogo, cinco distintos («alta gerencia», «gestion de riesgos», «del banco central»,
«gobierno societario» y «miembros del directorio»), en cinco casos de control (`adrei::4.3.1.1`, `.2` y `.3`,
`expaef::1.1.2.5` y `lingob::2.3.2.2`; `bi_trigramas_de_control_por_origen`): son nombres y definiciones de
sujetos del catálogo decidido, declarados como las 19 ventanas. Por esta regla las instrucciones
no citan los casos de prueba: la decisión 11 nombra la cláusula de mutuales de `pro::1.1.2.5` y los
ejemplos de límite relativo del plan son de chunks de la tanda 0, así que el borrador describe los dos
patrones sin citarlos (precedente: en ESQ-3b la regla de no-filtración reemplazó el ejemplo dictado,
ratificado por la autora en `prerregistro_esq3b_v2.md:42-50`). Lo ratifica la autora (§10, punto 2).

## 6. P1.b: X5 y X9

### 6.1 X5, incorrectas `E1-prompt` de la observación (12)

| Entrada | Defecto (backlog) | Qué la ataca |
|---|---|---|
| `BKL-0032` (`data/backlog/backlog.jsonl:77`) | polaridad invertida en `docvig::3.3::cierre` | R5, POLARIDAD de la Excepcion; R24, ejemplo negativo; el `tramo` de evidencia deja verificable la descripción |
| `BKL-0033` (`:78`) | `aplica_a` al banco de un acto en voz pasiva de otro (`ctacte::7.3.1.5`) | R15, viñeta de la voz pasiva y los actos de terceros |
| `BKL-0035` (`:80`) | Obligacion vacía desde el anuncio de una lista (`ctacte::8.3::intro`, `8.4::intro`) | R16, regla 1, y R30: la unidad del encabezado no emite nodo por el solo anuncio; el sujeto, la modalidad y el cuantificador van compuestos en cada ítem (F1-A, §4.5). En la tanda 0 ese nodo lo creó el reintento de E3: lo cubren las salidas (a) y (b) del §4.5. La fusión de los dos puntos es de ensamblado y ya la corrige U-R2-CODIGO (T2). La condición de cierre se mide sobre la extracción final de U-REEXT-T0, después de E3, no en P4 |
| `BKL-0039` (árbol de trabajo, sin commit al 03/10/2026) | Obligacion de solo anuncio creada por el reintento de E3 (`ctacte::6.4.7::intro`) | lo mismo que `BKL-0035`; caso de control de la pata de E3 de P4 (§4.5) |
| `BKL-0036` (`:81`) | calificador amputado de la Operacion (`lingob::2.3.2.2`) | R3, Operacion; regla 8 sellada (completitud) |

Las cuatro se verifican con su condición de cierre sobre el grafo de r2b (U-REEXT-T0); la pareada de P4
las lee como casos aparte si caen en la muestra. La regla 1 se revisó con la propuesta de U-DIAG-PROCESO
(F1-A, §4.5): el anuncio no es entidad, el sujeto, la modalidad y el cuantificador del encabezado viajan a
los ítems, y lo demás que el encabezado enuncia (una condición, un plazo, una excepción) se sigue
extrayendo en su unidad.

### 6.2 X9, asignación de sujeto de B2.4

**Conteo.** El plan dice nueve (`ebd7b1e:docs/plan_tesis.md:380`; checklist X9, `ebd7b1e:docs/checklist_pre_escalado.md:167`).
En el backlog hay **ocho** entradas `triaged` de asignación de sujeto: `BKL-0009` a `BKL-0016`, las T1 a
T8 de `data/backlog/expediente_retriage_v3.md:136-143`, con 31 aristas VP. La novena es NO ENCONTRADA:
ninguna otra entrada `triaged` anterior a la observación (12) tiene especie de sujeto (las 15 de B2.4 son
`BKL-0001`, `0002`, `0008` a `0016`, `0018` y `0020` a `0022`).

| Entrada | Patrón | Qué la ataca |
|---|---|---|
| `BKL-0009`, `0010`, `0011` (T1–T3) | descenso: banco o banco comercial donde el texto dice entidad o entidad financiera | código: con la mención literal, R1 (label o alias exacto) gana sobre la sugerencia; prompt: R15 conserva las reglas de clase exacta |
| `BKL-0012` (T4) | término de otro TO (usuario de servicios financieros en Exterior) | prompt: R15, sin `sujeto_id` si la mención no nombra la entrada; el código usa la sugerencia solo sin regla (R4) |
| `BKL-0013` (T5, 18 aristas) | estrechamiento: «la(s) entidad(es)» de Exterior asignado a entidad financiera | prompt: R15, viñeta del colectivo («NUNCA una clase más estrecha»). El código no alcanza: con R3 gana la sugerencia del modelo (L-ESQ-R2 §3.3, punto 5) |
| `BKL-0014`, `0015` (T6, T7) | clase forzada (VPU → exportador; «los residentes» → persona humana) | prompt: R15, sin `sujeto_id` si la mención no nombra la entrada; la mención sin id va al registro de no mapeados |
| `BKL-0016` (T8) | «los clientes» → exportador | código: R1 resuelve a `Sujeto_cliente` desde la mención literal |

El laudo de los 15 de B2.4 sigue pendiente (checklist X9); esta tabla es el remedio que el diseño de
U-LISTAS-NOMAP asignó al prompt, no el laudo.

### 6.3 Ausencias que E1 no emitió (plan, fila 10)

Las de D2 de U-PRE-R2-DIAG (`reports/u_pre_r2/d2_ausencias.md`, §4): 4 E-tabla (`ric::7.2`) y 4 G
(`ric::9.2.1`, con E-tabla-no-marcada como secundaria). Las ataca la lectura de tablas (decisión 6) y la
omisión `tabla` con tramo (decisión 5). En la E0 e0-r2 las dos quedan serializadas: `ric::7.2` en
`ric::tabla020` (columnas) y `ric::9.2.1` en `ric::tabla022` (columnas) y `ric::tabla023` (posicional),
sin avisos de riesgo. Con el prefijo nuevo su contenido llega como texto confiable. La presencia se mide
con R-CITA y R-PRES sobre el grafo de r2b.

## 7. P1.c: costo (parte del crudo guardado)

Fórmula de caching (decisión 2): entrada sin caché × 1,00, escritura × 1,25, lectura × 0,10 y salida ×
5,00 USD/MTok para E1 (Haiku 4.5); E3, 2,00 / 2,50 / 0,20 / 10,00 (`runner_corpus.py:18-19`). Todas las
cifras son ESTIMACIONES sobre el crudo de la tanda 0, no mediciones del prefijo nuevo.

**Calibraciones** (`censo_p1.json`, `calibracion`):
- Salida de E1: tokens ≈ 76,99 + 0,42762 × caracteres del JSON del tool call (2.434 unidades; error
  relativo mediano 3,7 %, p90 9,9 %).
- Mensaje: tokens ≈ 469,03 + 0,31161 × caracteres (error mediano 1,7 %, p90 4,0 %). Los tokens del mensaje
  nuevo salen de los tokens medidos de cada unidad más 0,31161 × la diferencia de caracteres entre el
  mensaje nuevo sobre e0-r2 y el sellado sobre la E0 legada: +754.826 caracteres, ≈ +235.209 tokens
  (de 2.763.771 a ≈ 2.998.980; `censo_p1.json`, `mensaje_r2`), casi todo por la línea de alcance y el
  cierre; 81.896 de esos caracteres son el rótulo del contexto heredado de los ítems (116 caracteres más
  en cada uno de los 706, §4.1).
- Prefijo: recta sobre cuatro prefijos medidos (produccion_dev 9.983; canal abierto 10.801; esq3b_v2
  11.933; v3_b54 15.433 tokens de caché por llamada), tokens ≈ −409,8 + 0,33796 × system + 0,50131 × tool
  schema (residuos de −71 a +97). El texto congelado (variante B) da 27.444 tokens; una recta de un solo
  término da 26.046. Tomo 27.444 como central: el tool schema r2 queda fuera del rango de los puntos medidos.
- Control: el costo de E1 recomputado del crudo da USD 18,11 contra 18,07 de las fases cerradas.

**Salida que agregan o quitan los campos nuevos** (tokens en la tanda 0; `delta_tokens_por_campo_total`):

| Campo | Δ tokens | Base de la estimación |
|---|---:|---|
| Tramo de evidencia (decisión 15) | +663.704 | §8.1 (cota baja: +569.226) |
| TextoOrdenado sin `properties` (decisión 16) | −132.023 | lo que hoy emite cada unidad |
| Mención del sujeto (decisión 4) | +66.705 | 4.099 relaciones de sujeto |
| Umbrales como tramos (decisión 3) | +33.172 | 925 elementos en 795 entidades; incluye 49 Restricciones `limite_cuantitativo` sin cuantía |
| Salen `umbral` y `plazo` de v3 | −8.914 | — |
| Omisiones: clave en todo chunk | +5.775 | — |
| Omisiones de v3 con categoría y tramo | +10.183 | 162 omisiones; tramo supuesto de 100 caracteres |
| `frecuencia`, variante A / B | +4.548 / +484 | §9 |
| Comunicacion sin `tipo` ni `numero` | −380 | — |
| `otras_propiedades` | +128 | claves fuera de la definición |
| Composición con el encabezado de una lista (F1-A, §4.5) | +133.245 | 706 ítems, 937 entidades compuestas (Obligacion, Restriccion o Potestad; un ítem con contenido y sin ninguna cuenta una); cada una suma al `tramo` el segmento del encabezado (168 caracteres de media: 157.486 entre 937) y el separador, y el encabezado en la descripción en las 892 cuya descripción no trae el 60 % de sus palabras de contenido. Cota alta: no descuenta los nodos de solo anuncio que dejan de emitirse |
| Omisiones nuevas (solo escenario alto) | +37.787 | proxy: 60 chunks con forma meta-normativa, 4 tipos rechazados, 327 firmas inválidas que la matriz r2 no recupera |
| **Total, central A** | **+776.144** | +33,7 % sobre 2.301.009 |

**Costo por escenario** (`costos`, `recalculo_tandas_usd`):

| Escenario | E1 | E3 | E1 y E3 | Por unidad |
|---|---:|---:|---:|---:|
| Tanda 0 medida (fases cerradas) | 18,07 | 22,28 | 40,35 | 0,0166 |
| r2b central, variante B (congelada) | 25,20 | 23,93 | 49,13 | 0,0202 |
| r2b alto, variante B (omisiones nuevas) | 25,39 | 24,01 | 49,40 | 0,0203 |
| r2b central, variante A (referencia) | 25,22 | 23,94 | 49,16 | 0,0202 |
| r2b cota baja del tramo de evidencia (A) | 24,75 | 23,74 | 48,49 | 0,0199 |
| r2b sin tramo de evidencia (A, referencia) | 21,90 | 22,57 | 44,47 | 0,0183 |

Desglose de E1 central (B): lectura del prefijo USD 6,67 (antes 3,75), escrituras 0,17 (5 escrituras, como
en el crudo), mensaje 3,00 (antes 2,76) y salida 15,39 (antes 11,51). E3: verificador 19,95 (todas las claves
cambian, §1), más 0,88 por lo que renderice de los campos nuevos (supuesto: 70 % de los caracteres
agregados, con la proyección de §4.4, autorizada), más los reintentos de E1 del ratchet, 2,33 × 1,337. La
variante B cuesta USD 0,02 menos que la A. F1-A sola suma ≈ USD 0,67 de salida de E1 (133.245 × 5 USD/MTok),
más su parte del render de E3 y de los reintentos; U-DIAG-PROCESO la estimaba en ≈ 0,13 con tokens
supuestos (reporte, tabla del §5): la diferencia es que el `tramo` lleva el segmento del encabezado y que
la descripción se compone.

**Salidas (a) y (b) del §4.5, aprobadas.** La NOTA de los encabezados suma ≈ USD 0,09 de entrada de E3. La
guarda ampliada ahorra ≈ USD 0,020 por cada reintento que evita: del orden de USD 0,8 si los bloqueos son unos
40. La estimación central no incluye ninguna de las dos, y la cifra que sigue tampoco.

**Tope de U-REEXT-T0 (E1 a E3, 2.434 unidades).** Estimación central USD 49,13 (variante B); con el factor
1,4 del precedente (`runner_corpus.py:17`), 68,78: **USD 69**, fijado por la autora en el FRENO P1. Ya incluye el mensaje de tablas, F1-A con el
tratamiento por tipo y la instrucción de umbrales ajustada con la M2 de U-MED-R2A. Las celdas de E5, si se
re-evalúan, van aparte (`ebd7b1e:docs/plan_tesis.md:400`, USD 21,2577 de referencia).

**Tandas del protocolo, a la tarifa nueva** (central B; entre paréntesis, a USD 0,0166):

| Tanda | Unidades | USD |
|---|---:|---:|
| 1 (ejemplo del §7) | 3.292 | 66,45 (54,65) |
| 2, digeribles restantes | 5.669 | 114,43 (94,11) |
| 2, no-RI plenos | 2.008 | 40,53 (33,33) |
| 3, RI plenos | 976 | 19,70 (16,20) |
| Partición completa | 9.324 | 188,21 (154,78) |

**Las filas no se suman.** Cada una es un grupo de unidades a la tarifa nueva, no una porción del total:
- la tanda 1 del ejemplo toma TOs de los grupos de las tandas 2 y 3 (10 digeribles y 10 «necesita
  reglas», 6 de ellos RI; protocolo §7, `a304b89`), y las filas de las tandas 2 y 3 están antes de
  descontarlos: el protocolo las escribe «menos los que entren a la tanda 1» y «menos los no segmentables
  y los que entren antes» (§5);
- la fila de la partición completa es el universo de los 152 TOs, no la suma de las otras: incluye los cinco
  TOs nuevos de la tanda 0 (ctacte, lingob, polcre, pagjub, docvig); los cinco de desarrollo no están en los
  152 (protocolo §5).

Si la autora aprueba estas cifras, van al protocolo como nota fechada (PENDIENTE de su decisión).

**Pareada de P4 (decisión 18).** Brazo nuevo de E1 solo, por estrato (`estimacion_p4`; el estrato «con
tabla serializada» sale de la E0 e0-r2: 37 chunks):
- 40 sorteados: ≈ USD 0,64 a la media de cada estrato y 1,08 a su p90;
- casos fijos: 0,06 (`cap::1.2`, `ric::9.2.1`, `cla::5.1.1.1`, `pro::1.1.2.5` y `cap::6.2.2.6`, decisión de la
  autora del 03/10/2026);
- fuera de muestra: 0,08 el brazo nuevo y 0,06 el sellado;
- casos de F1 (los 8 chunks de §4.5, los dos brazos por la API, a la media por unidad): 0,08 el brazo nuevo y
  0,06 el sellado;
- casos de control de `BKL-0035` y `BKL-0039` (brazo nuevo): 0,01;
- pata de E3 (§4.5): 0,06 central y 0,14 alto;
- escrituras de caché: 0,05.
Total ≈ **USD 1,11 central, 1,63 alto**: el tope de USD 2 alcanza. Si un
chunk sorteado del estrato fuera de muestra coincide con un caso de F1, se corre una vez y la cifra es cota
alta. Referencia: la pareada de B5.4 costó USD 0,2902 (`d3f2214`).

## 8. P1.d: tramo de evidencia, término literal y riesgo de corte

### 8.1 Tramo de evidencia: largo y costo

Apliqué la regla de la mención (P-b3 y P-b4, holgura 2) a la descripción guardada de cada entidad, contra
el texto propio y heredado de su chunk: si es exacta, el tramo es la descripción; si verifica por tokens,
el tramo literal mínimo; si no verifica, el largo de la descripción como aproximación. Cota baja: la
ventana mínima del texto que contiene las palabras del label, cuando es más corta.

| Tipo | Entidades | Exacta | Por tokens | No | Tokens medios |
|---|---:|---:|---:|---:|---:|
| Obligacion | 2.365 | 1.538 | 23 | 804 | 82,6 |
| Operacion | 2.110 | 535 | 24 | 1.551 | 70,8 |
| Condicion | 1.325 | 884 | 17 | 424 | 65,4 |
| Restriccion | 818 | 343 | 9 | 466 | 73,5 |
| Definicion | 622 | 319 | 6 | 297 | 88,6 |
| Potestad | 461 | 265 | 3 | 193 | 88,3 |
| Excepcion | 364 | 161 | 4 | 199 | 84,8 |
| Comunicacion | 31 | — | — | — | 10,7 (la cita) |

Hoy la descripción ya es una cita literal en la mitad de las entidades (4.045 exactas de 8.065, sin
contar 4 de tipo inválido). Por eso el tramo duplica la descripción en esos casos: es la mayor parte del
costo (USD 3,32 de salida en la tanda 0; 2,85 con la cota baja). Cambiar la descripción a paráfrasis corta
no lo manda ninguna decisión y cambia lo que lee el agente: no lo propongo (§10, punto 7).

### 8.2 Verificación en código (para P3)

- Regla: `validador_r2.verificar_tramo(tramo, texto_completo(chunk), holgura=2)` (`validador_r2.py:181`),
  la misma de la mención: «exacta» (subcadena normalizada de R-NORM), «tokens» (ventana de a lo sumo los
  tokens distintos más 2; se guarda el tramo literal mínimo del texto y el del modelo como
  `tramo_modelo`) o «no». Sin tramo, «ausente».
- Marca en el nodo: `tramo` y `tramo_verificado` (lista `TRAMO_VERIFICADO`, `modelos_r2.py:214`). En
  `NodoR2` y `EntidadR2` son campos nuevos de la decisión 15. Un nodo fundido de varios chunks guarda un
  tramo por procedencia.
- Contador: `tramo_entidad.<nivel>` por chunk y por corrida, en el registro del validador.
- Selftest: exacta; con corte de palabra por guion; reordenada (tokens); ausente del texto (no); vacía
  (ausente); entidad anclada en un ancestro con tramo del heredado; TextoOrdenado sin tramo.
- `Definicion.termino`: la misma regla, con marca `termino_verificado`. Hoy, sin la instrucción, 473 de
  622 términos son exactos, 38 por tokens y 111 no verifican.
- **Tramo compuesto de F1-A** (§4.5). Con `texto_completo`, los dos segmentos no verificarían como un tramo:
  están separados por todo el texto propio. Si el tramo contiene « […] » una sola vez, el código lo parte:
  el primer segmento se verifica contra el texto heredado (los bloques unidos, porque un encabezado puede
  estar repartido entre la línea de título y el párrafo de la misma unidad, como en la ficha 52) y el
  segundo contra el texto propio, con la misma regla y holgura. Así el código comprueba que el encabezado
  sale del contexto heredado y el contenido del ítem. `tramo_verificado` toma el menor de los dos niveles
  («no» < «tokens» < «exacta»); el nivel de cada segmento va al registro del validador
  (`tramo_compuesto.encabezado.<nivel>` y `tramo_compuesto.item.<nivel>`), sin campos nuevos en el modelo.
  Con dos o más separadores, «no». En una unidad que no es ítem, cada segmento se verifica contra
  `texto_completo` y se cuenta aparte (`tramo_compuesto.fuera_de_item`). Selftest: los dos segmentos
  exactos; encabezado repartido entre título y párrafo; primer segmento copiado del texto propio (no);
  compuesto fuera de un ítem; dos separadores.
- **Lo que se compone desde el encabezado en un ítem** (tipo (ii) del §4.5): la Condicion y el elemento de
  umbral cuyo `tramo` es el segmento del encabezado. La Condicion se verifica con la regla general, contra
  `texto_completo`, que incluye el heredado; el umbral, en el par B, también contra el texto propio y el
  heredado (`ensamblar_tanda0.py:620-626`). En un ítem, el tramo de una Condicion que verifica solo en el
  heredado se cuenta aparte (`tramo_entidad.heredado_compuesto`). Fuera de un ítem, un tramo del heredado
  sigue admitido solo para la entidad anclada en un ancestro. Selftest: la Condicion compuesta de un ítem con
  su tramo en dos bloques heredados seguidos (la línea de título y el párrafo, como en `ext::4.8.6.1`).

### 8.3 Riesgo de corte (`BKL-0030`)

Primer intento a 8.192 tokens de salida y reintento del perfil r2 a 16.384
(`cliente_e1.MAX_TOKENS_REINTENTO_CORTE_R2`, `cliente_e1.py:68`); si el reintento también corta, R4.b
parte la unidad (`runner_corpus.py:582`). En la tanda 0 cortaron tres unidades de cap: su reintento a
32.768 lo rechazó la SDK y se recuperaron en la dirigida a 16.384 (`cap::4.2.1.2` 11.925, `cap::4.3.3.1`
9.212, `cap::3.1.14.1` 8.371 tokens).

Proyección con la salida más larga estimada (central A; `escenarios_salida`):
- 7 unidades superan 8.192 y van al reintento: `cap::4.2.1.2` (17.796), `cap::4.3.3.1` (13.808),
  `cap::3.1.14.1` (12.928), `cap::3.1.14.2` (10.131), `cap::5.3.2.3` (10.007), `cap::6.10.1.2` (8.943) y
  `ext::3.16.3.2` (8.255); 16 superan el 80 % de 8.192;
- 6 de las 7 entran en 16.384; `cap::4.3.3.1` queda al 84 % del techo;
- `cap::4.2.1.2` lo supera: R4.b la parte. Ya cortaba a 16.384 en r1 (laudo de r2, §1.1).
Propuesta: dejar el primer intento en 8.192. Los siete primeros intentos cortados cuestan ≈ USD 0,29
(7 × 8.192 × 5 USD/MTok); subir el primer intento cambiaría el request de todas las unidades sin
ahorro que lo justifique. Sin el tramo de evidencia serían las mismas tres de la tanda 0
(`A_central_sin_evidencia`, que conserva F1-A entera, incluido el segmento del encabezado en el `tramo`).

## 9. Decisión 20: las dos variantes de `frecuencia`

**M2.c** (FRENO M2 de U-MED-R2A, `c50b094`; tablero :74; `m2/m2_medicion.json`, `f74_frecuencia`). En el
grafo r2a de los diez TOs, el código manda 250 plazos de Obligacion a `frecuencia`, y 213 quedan fuera de la
lista.
- Los 37 de la lista: anual 7, diaria 3, mensual 14, semestral 4, trimestral 9.
- Por TO, mandados y fuera de lista: cap 49/37, cla 17/16, ctacte 46/41, docvig 1/1, ext 69/69, lingob 17/14,
  pagjub 11/11, polcre 3/2, pro 20/16, ric 17/6.
- En desarrollo: 172 y 144.
Mi proxy sobre el crudo daba 253 y 214: la diferencia es de criterio de conteo, y la cifra que vale es la de
M2.c. **M3.d no llegó.** En el árbol hay salidas de M3 sin commit, de otra sesión, y no las leí.


| | Variante A (regla actual) | Variante B (plazos sin cuantía fuera de `frecuencia`) |
|---|---|---|
| Texto del prefijo | R6 A: `frecuencia` recibe la periodicidad o el momento sin cuantía temporal | R6 B: `frecuencia` solo recibe la periodicidad; el momento sin cuantía queda en la descripción y el `tramo` |
| Efecto en el grafo | como r2a: 213 valores marcados fuera de lista (M2.c) | `frecuencia` solo con las frecuencias de la lista (37 en r2a); el momento sin cuantía no tiene campo estructurado |
| Tool schema | la descripción del campo (`modelos_r2.py:663`, «Tramo literal de la frecuencia») queda más estrecha que la instrucción; alinearla es un cambio del modelo fuera de las decisiones 15 a 17 | sin cambio: la descripción ya dice eso |
| Costo (tanda 0) | +4.548 tokens de salida | +484 (USD 0,02 menos en total) |
| Comparabilidad r2a–r2b | la fila del tablero sigue midiendo lo mismo | la fila baja a ~0 por construcción |

**Qué son los fuera de lista** (`p1/frecuencia_r2a.py` → `p1/salida/frecuencia_r2a.json`). En r2a hay 217
Obligaciones con `frecuencia` fuera de la lista y 153 valores distintos; son los mismos 217 y 153 de la fila :64
de M2.
- Los más frecuentes son momentos sin cuantía («previa», «en el día», «inmediato», «al momento de …») o
  continuidades («permanente», «continuo»), y valores de relleno («sin especificar», «no especificado», «N/A»).
  Los de relleno son 38 nodos con 17 valores, por una proxy sobre el texto del valor.
- Casi ninguno es una periodicidad.
- Los de relleno vienen de la propiedad `plazo` libre de v3. Con el tramo literal del borrador desaparecen en
  las dos variantes.

La elección es sobre los momentos:
- A los guarda en `frecuencia` como tramo literal fuera de la lista;
- B los deja en la descripción y en el `tramo` de la norma, que son literales y verificados, y `frecuencia`
  vuelve a ser una lista cerrada.

**Se decide en el FRENO P1, con M2.c (M3.d no llegó). Recomiendo B.**
- Un momento sin cuantía no es una periodicidad, y como valor marcado de un campo de lista nadie lo consulta
  por ese campo.
- El costo de B es el mismo que el de A.
- Con B, la fila :74 del tablero baja a ~0 por construcción: hay que leerla así, y no como una mejora del
  extractor.

## 10. Para el FRENO P1

### 10.1 Puntos que estaban abiertos: decididos en el FRENO P1

La autora decidió todos el 03/10/2026:
- 1, 2, 3, 8 y 10, confirmados como los recomendé;
- 5, el elemento sin valor del límite relativo, va en `validador_r2.py` (P3);
- 6, frecuencia: variante B.
Abajo queda el texto con el que se presentaron.

1. **Tramo del TextoOrdenado.** La decisión 15 dice «cada entidad de los nueve tipos», y la 16 deriva el
   TextoOrdenado en código. El borrador no le pide tramo al TextoOrdenado. A confirmar.
2. **No-filtración sobre las decisiones 11 y 21.** El borrador describe los patrones sin citar los casos
   de prueba (§5). A ratificar.
3. **Decisiones 8 y 16.** «externa» deja de estar en el tool schema (sale `Comunicacion.tipo`) y vive en
   la derivación del código; el prompt admite normas externas como Comunicacion (R1). A confirmar.
5. **Límites relativos (decisión 21).** `reglas_comparacion.analizar` solo devuelve cuantías numéricas
   (`reglas_comparacion.py:486-490`): con el tramo de un límite relativo, `llenar_umbrales_r2` no arma
   ningún elemento. El elemento sin valor necesita código nuevo en `reglas_comparacion.py` o en
   `ensamblar_tanda0.py` (fuera de las escrituras) o en `validador_r2.py` (autorizado). A decidir dónde.
6. **Variante de `frecuencia`** (§9). M2.c: 250 plazos a `frecuencia` y 213 fuera de la lista; M3.d no llegó.
   Recomiendo B. Decide la autora en el FRENO P1, porque P2 congela el prefijo.
8. **Catálogo r2 con «sujeto_propuesto».** La definición de `Sujeto_entidad_originante_de_transferencia`
   en `catalogo_sujetos_r2.json` dice «ese sujeto sigue en sujeto_propuesto», un campo que r2b retira. El
   borrador lo aclara en R15; la alternativa es enmendar el JSON en una unidad que lo autorice (LN-8 impide
   tocar el bloque). A elegir.
10. **Guarda de `ejecuta` en los 5 TOs de desarrollo** (§4.1): el borrador la extiende a todos. A aprobar.

### 10.2 Decididos, confirmados o registrados

4. **Validación de la fase E1 para E3 y el ratchet** (§4.4). **Autorizada para P2** (decisión de la autora
   del 03/10/2026; la nota `a807136` al pie del mandato suma `validador_e1.py` y `selftest_e1.py` a las
   escrituras): la traducción en `validador_e1.py`, con `forma_salida` en `perfil_e1.EsquemaValidacion`, solo
   con «r2», sobre una copia, sin tocar la salida cruda; con los perfiles existentes, el resultado byte a
   byte igual, cubierto por los selftests del validador y del manifiesto; el tramo de evidencia no se
   traduce. Lo que sigue es la especificación que P2 implementa.
   - **Por qué hace falta.** E3 y el ratchet no leen la validación del perfil r2: el runner
     (`runner_corpus.py:567`) y el ratchet (`ratchet_e3.py:279`) llaman a
     `validador_e1.validar_salida(tool_input, chunk, esquema=perfil.esquema)`, y el mensaje de E3 renderiza
     esa salida (`comun_e3.render_extraccion`, `comun_e3.py:140-190`: `properties`, `sujeto_id` o
     `sujeto_propuesto`, `omisiones_no_prosa`). Con la salida del prefijo nuevo y el validador como está:
     - (a) una relación `aplica_a` o `ejecuta` con mención y sin `sujeto_id` se rechaza
       (`validador_e1.py:299-303`), y con mención, sin id y con padre sugerido, también (`:308-311`,
       `padre_sugerido_sin_propuesto`): E3 no la ve y puede reclamarla como faltante (referencia: 63
       relaciones con `sujeto_propuesto` en el crudo de diez);
     - (b) `umbrales`, `tramo` y `otras_propiedades` quedan fuera, porque el validador lee solo `properties`
       (`:202-206`): E3 no ve las cuantías y puede reportar calificadores despojados;
     - (c) `omisiones` no es `omisiones_no_prosa` (`:154-156`): E3 no ve ninguna omisión declarada y, en los
       83 chunks marcados de e0-r2, puede reportar `contenido_tabular_no_declarado`; el validador además
       advierte `flag_sin_omisiones_declaradas` (`:376-385`).
     Cada faltante falso dispara un reintento del ratchet, que se paga, o manda la unidad a la cola humana.
     El grafo r2 no se pierde, porque lo arma `validador_r2` desde el crudo, pero las decisiones del ratchet
     y la cola humana salen de esa vista parcial.
   - **El cambio.** Una proyección de la forma r2 a la forma que leen E3 y el ratchet, dentro de
     `validador_e1.validar_salida` y solo si el `esquema` del perfil la pide. Con `esquema` None o de los
     perfiles existentes, el camino es byte a byte el de hoy.
     1. `perfil_e1.EsquemaValidacion` (escritura autorizada) suma un campo `forma_salida` con default `"v3"`.
        El perfil nuevo lo pone en `"r2"`, con `firma_valida = modelos_r2.firma_r2` (la matriz ampliada), el
        catálogo r2 (110 ids) y el enum de `Obligacion.tipo`.
     2. `validador_e1.validar_salida`, con `forma_salida == "r2"`, proyecta una copia del input antes de
        validar (el crudo no se muta):
        - relación de sujeto con `sujeto_mencion` y sin `sujeto_id` → `sujeto_propuesto = sujeto_mencion`;
          con `sujeto_id`, se descarta el padre sugerido (en r2 el padre va solo sin id);
        - entidad: los tramos de `umbrales` → `properties["umbrales"]`, como texto separado por « | »;
          `otras_propiedades` → `properties`, con prefijo si choca con una clave definida; `tramo` no se
          proyecta: es evidencia, no contenido, y E3 juzga si el contenido extraído cubre el texto;
        - `omisiones` → `omisiones_no_prosa`, un string por omisión, «[categoría] tramo — nota», con
          «source → destino» en `relacion_sin_predicado`;
        - `otras_propiedades` de las relaciones no se proyecta: E3 no renderiza propiedades de relaciones.
     3. Selftests: los de `validador_e1` (`selftest_e1.py`, `selftest_cablev3.py`) en verde, con los
        casos existentes sin cambios y casos nuevos de la proyección en `selftest_e1.py`; y
        `selftest_manifiesto.py` P3 y P4 con los requests de E3 byte a byte para los perfiles existentes.
     El prefijo de E3 y su candado no cambian; cambia solo el contenido de su mensaje, que ya cambia en todas
     las unidades (§1). El rótulo del render, «Omisiones no-prosa declaradas por el extractor»
     (`comun_e3.py:188`), queda también para `meta_normativo`, `fuera_de_tipos` y `relacion_sin_predicado`:
     imprecisión declarada. Tamaño estimado: unas 40 líneas en `validador_e1.py` y 2 en `perfil_e1.py`, NO
     MEDIDO hasta P2.
   - **Alternativas.** Ninguna evita escribir fuera de las escrituras del mandato:
     - proyectar en el runner (autorizado) cubre el primer intento, pero no los reintentos, que el ratchet
       re-valida directo con `validador_e1` (`ratchet_e3.py:279`): exige además escribir `ratchet_e3.py`;
     - un validador provisto por el perfil y llamado desde el runner y el ratchet: también exige
       `ratchet_e3.py`;
     - cambiar `comun_e3.render_extraccion` para leer la forma r2 no evita el rechazo de las relaciones con
       mención sin id, que ocurre antes, en el validador, y suma `comun_e3.py`;
     - proyectar en el cliente de E1 alteraría el crudo guardado, que `validador_r2` necesita íntegro
       (principio 12): descartada;
     - no tocar nada deja a E3 sobre la vista parcial descrita arriba.
     La de menor alcance es la proyección en `validador_e1.py`, detrás del `esquema` del perfil: es la
     autorizada.
7. **Descripción y tramo duplicados** en la mitad de las entidades (§8.1): se mantienen; cambiar la
   descripción no está decidido.
9. **Bloque de catálogo y no-filtración.** Las definiciones nuevas del catálogo r2 citan texto de la
   tanda 0 y de los TOs fuera de muestra (19 ventanas de 5 palabras, en `lingob`, `pro`, `cap`, `ext`,
   `ctacte`, `ayccef`, `expaef` y `adrei`). Son contenido decidido en U-CAT-UNICO: quedan declarados.
11. **X9 son ocho, no nueve** (§6.2).
12. **Casos fijos de P4** (decisión 19). `ric:9.2` era el ancla de D2, no un chunk: el cuadro de códigos
    está en `ric::9.2.1`, que en e0-r2 trae dos tablas serializadas. Decidido (03/10/2026): `ric::9.2.1`
    reemplaza a `ric::9.2`, se suma `cap::6.2.2.6` y `ric::9.2.2` no entra. La lista de control de
    `p1/nofiltracion.py` lleva los ids reales. Registrado en la nota fechada al pie del mandato (`e7f7a2e`),
    que vale para la decisión 19 y P4.a; la extensión a la prueba en seco de P2.d (`ric::9.2.1` en lugar de
    `ric::9.2`) entró en `a807136`. P2.d imprime entonces los requests de `cap::1.2`, `ric::9.2.1`, uno con
    sujeto propuesto y `cla::5.1.1.1`.
13. **Tope de P4**: USD 2 alcanza, con los casos de F1, los de `BKL-0035` y `BKL-0039` y la pata de E3: 1,11
    central y 1,63 alto (§7). **Tope de U-REEXT-T0**: propongo USD 69 para E1 a E3 (49,11 × 1,4); lo fija la
    autora en el FRENO P1.
14. **U-DIAG-PROCESO** (commiteada en `93ce4b7`). De sus dos problemas, entra al prefijo F1 (F1-A, primera
    mitad; §4.5), con R16 revisada y el censo re-corrido. El vínculo entre unidades no cambia el prefijo: la
    forma A se mide sobre el grafo de U-REEXT-T0 y la forma B va a A1.8 o queda como límite
    (`git show a807136:docs/plan_tesis.md`, `:398`, `:400` y `:327`).
15. **Tablas serializadas con celdas sin resolver** (§4.2): 12 de las 51 llevan el aviso de riesgo.
    Decidido (03/10/2026): aviso, no residual, redactado por tipo de riesgo; la designación de residual se
    puede forzar en código con una lista explícita de tablas, sin cambiar el prefijo (§4.2, regla 4).
16. **Evidencia tabular con residual falso** (§4.2, regla 3): el borrador no imprime ninguna línea, incluso
    las que siguen en el texto (en 6 chunks queda 1 línea: `ric::5.1.3.2`, `ric::5.2.4`, `ric::7.2`,
    `ric::9.2.2`, `cap::2.1` y `cap::2.12.4.1`). La decisión 6 pide suprimir las
    que reemplazó el bloque; suprimir también las otras es mi lectura de que la heurística de E0 ya no las
    ve como tabulares. Confirmado por la autora (03/10/2026).
17. **La NOTA de E3 en `ric::S2`** aparece porque e0-r2 marca el chunk, no por el texto nuevo de la NOTA.
    Queda contada entre los 38 (§4.3). Aclaración, sin cambio (autora, 03/10/2026).
18. **F1-A, tratamiento por tipo del encabezado** (§4.5). **Aprobado por la autora el 03/10/2026**, con el
    límite declarado de las condiciones conjuntas en un encabezado en línea de título sin unidad propia. Está
    en R30, R16 y R11 del borrador, y la NOTA de E3 está alineada (§4.5).
    - **La tanda 0 tiene 10** (`encabezados_lista.json`, `encabezados_titulo`, con el contexto heredado y los
      ítems de cada uno; los mismos 10 en e0-r2). Los clasifiqué por lectura propia:

    | Encabezado | Tipo | Por qué |
    |---|---|---|
    | `cap::10.2.1` «Serán ECAI elegibles las siguientes:» | (i) | los ítems son las clases elegibles; basta cualquiera |
    | `cap::6.10.1` «Un marco de valuación prudente deberá incluir, como mínimo, lo siguiente:» | (i) | contenidos de un deber, todos |
    | `cap::8.3.3` «Los instrumentos incluidos en el PNc deberán observar los siguientes requisitos:» | (i) | requisitos redactados como deber, todos |
    | `ctacte::2.3.4` «Se deberá especificar:» | (i) | contenidos de un deber |
    | `cla::2.2.1` «Los siguientes conceptos por intermediación financiera:» | (i), con la norma en un ancestro | la exclusión está en el título de 2.2 («Exclusiones.») |
    | `cla::2.2.2` «Las siguientes garantías otorgadas:» | (i), ídem | ídem |
    | `ext::4.7.4` «cuenta con una declaración jurada del cliente en la que deja constancia de que:» | (i), anidado | los ítems, unidos por «y», son el contenido de una declaración que la entidad debe verificar (intro de 4.7) |
    | `cap::6.8.3` «Para las exposiciones valuadas a modelo, si la entidad puede:» | (ii), anidado | el ámbito vale para cada ítem; la modalidad viene del intro de 6.8 («deberán, como mínimo, tomar en consideración lo siguiente:») |
    | `ctacte::6.4.6` «No corresponderá la comunicación al BCRA de los rechazos motivados por:» | (iii), alternativas | la norma principal está en el encabezado; los ítems son motivos, y cada uno basta |
    | `polcre::2.1.3` «Financiaciones a productores, procesadores o acopiadores de bienes, siempre que:» | (iii), alternativas | el primer ítem termina en «; o» |

    - **Resultado:** 7 de tipo (i), 3 de ellos con la modalidad o la norma en un ancestro; 1 de tipo (ii); 2 de
      tipo (iii), los dos con alternativas. Ninguno de los 10 es de tipo (iii) con condiciones conjuntas.
    - **Cuándo componer es verdadero:**
      - es verdadero si los ítems son contenidos de un deber: deber de A y B equivale a deber de A y deber de B;
      - es verdadero si los ítems son supuestos alternativos: «si A o B, entonces N» equivale a «si A, N» y
        «si B, N»;
      - es falso si los ítems son condiciones conjuntas: «si A y B, entonces N» no implica «si A, N»;
      - es falso si los ítems son contenidos alternativos de un deber y se pierde el cuantificador: deber de A
        o B no es deber de A. R30 ya pide conservar el cuantificador.
    - **Tratamiento por tipo (aprobado):**
      - **(i):** componer, como dice R30. Hay que agregar que, si el último encabezado no trae la modalidad o el
        sujeto, se toman del bloque heredado más cercano que los trae (4 de los 10 son listas anidadas o toman
        la norma de un título ancestro). El primer segmento del `tramo` puede abarcar bloques heredados
        consecutivos; la verificación del §8.2 lo admite, porque compara con el heredado unido. Riesgo: componer
        con el ancestro equivocado.
      - **(ii):** componer también el plazo, el ámbito o la condición que vale para cada ítem, tanto en los
        títulos como en los encabezados con unidad. La viñeta de R30 «el ítem no repite lo demás…» pasaría a
        distinguir: lo que califica a cada ítem se compone en el ítem; lo que es otra norma del encabezado (una
        excepción a toda la lista, una norma propia) queda en su unidad. Así también tienen lugar los 30
        encabezados con unidad que tienen marca de plazo o condición (§4.5), porque un plazo no tiene dónde ir
        si no se emite la norma. Riesgo bajo: un plazo que vale para cada ítem es verdadero en cada uno.
      - **(iii) con alternativas:** componer la norma principal en cada ítem, con el cuantificador («basta
        cualquiera de los supuestos»). Es verdadero. En los encabezados con unidad, R30 ya conserva la norma
        en su unidad y hace Condicion a los ítems: no cambia.
      - **(iii) con condiciones conjuntas:** no componer, porque sería falso. Los ítems son Condicion. Si el
        encabezado está en la línea de título, la norma principal queda como límite declarado, con destino a
        E0 (un mini-chunk para el título que abre una lista) en una versión posterior. Cuando el texto no deja
        claro si son conjuntas o alternativas, se tratan como conjuntas: la falla va hacia perder la norma, no
        hacia crear permisos falsos.
    - **Tamaño fuera de la tanda 0.** La partición tiene 87 encabezados de título sin unidad
      (`particion_titulo_sin_unidad`, proxy mecánica, NO MEDIDA). 4 anuncian condiciones o supuestos:
      - `gracre::2.2.9` («que reúnan las siguientes condiciones»), el único candidato a condiciones conjuntas;
      - `polcre::2.1.3`, con alternativas;
      - `retype::3.1.2` y `seguef::5.4.6`, que empiezan con «Cuando…:» y son del tipo (ii).
    - Entró al borrador en este avance, con el censo y la no-filtración re-corridos.
19. **F1-A, regla del encabezado de lista** (§4.5; decisión de la autora del 03/10/2026, nota `a807136`):
    composición en los incisos, sin nodo por el solo anuncio, tramo de dos segmentos verificado por el
    código (§8.2), costo en §7 y medición en P4 con los casos de F1 reportados aparte.
20. **Salidas (a) y (b) para E3 y la unidad del encabezado** (§4.5). **Aprobadas juntas por la autora el
    03/10/2026**: (a) la NOTA de E3 para los encabezados de lista; (b) la guarda ampliada, con la salvaguarda.
    - Condición: el reporte de U-REEXT-T0 lista cada unidad eximida (marca `guarda_ampliada`, §4.5).
    - Las escrituras nuevas (`prompt_e3.py` para esta NOTA; `ratchet_e3.py` y `selftest_e3.py`) están en la
      nota al pie del mandato, y la regla en la enmienda a LAUDO B. Las dos están en el árbol de trabajo, sin
      commit; la enmienda es un borrador sin firma. Commit y firma: PENDIENTES de la autora.
    - P4 suma la pata de E3 sobre cuatro encabezados de lista, y `ctacte::6.4.7::intro` (`BKL-0039`) como caso de
      control (§4.5 y §7).

## 11. Pendiente

Lo que dependía de la E0 e0-r2, de U-DIAG-PROCESO y de la M2 de U-MED-R2A está en el borrador, con el censo
re-corrido. Falta:
- **en el FRENO P1**, que decide la autora: el texto del prefijo y del mensaje (§2 y §4); los puntos abiertos
  del §10.1; la variante de `frecuencia` (punto 6); el tope de U-REEXT-T0; y las cifras de las tandas, que van
  como nota fechada al protocolo si las aprueba;
- **commits y firmas, PENDIENTES de la autora:** la nota al pie del mandato sobre las escrituras de E3, la
  enmienda a LAUDO B (borrador sin firma) y la entrada `BKL-0039`, las tres en el árbol de trabajo;
- **en P2:**
  - la traducción de la forma «r2» en `validador_e1.py`, con la marca `forma_salida`;
  - la NOTA de los encabezados en `prompt_e3.py`;
  - la guarda ampliada en `ratchet_e3.py` y `selftest_e3.py`, con la marca `guarda_ampliada` y su lista en
    `runner_corpus.py`;
- **en P3:** la verificación del tramo compuesto y del tramo heredado de lo compuesto (§8.2);
- **tras la pareada de P4:** si la asociación de `cap::tabla037` sale mal hecha, el alta de esa tabla en la
  lista de tablas forzadas a residual, antes de U-REEXT-T0.

## 12. Comandos y artefactos

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p1/reproducir_p1.py --espejo <dir fuera del repo>
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p1/lado_a_lado.py
```

`reproducir_p1.py` corre también el censo del mensaje sobre la E0 e0-r2, los ejemplos, el lado a lado y
las huellas de los borradores.
Doble corrida con espejos distintos: salidas byte a byte iguales. Herramientas en `data/experiment/prompt_r2/p1/`:
`borrador_prefijo_r2.py`, `mensaje_r2_borrador.py`, `espejo_tool_schema.py`, `nofiltracion.py`,
`censo_p1.py`, `ejemplos_mensaje_r2.py`, `lado_a_lado.py`, `hashes_borrador.py`, `encabezados_lista.py`,
`frecuencia_r2a.py` y `reproducir_p1.py`. El control del separador del tramo compuesto (§4.5) está en `censo_p1.json`,
`control_separador_f1a`; la unidad del encabezado, E3 y los encabezados de título, en
`encabezados_lista.json` y `encabezados_lista.md`; los valores de `frecuencia` de r2a, en
`frecuencia_r2a.json`. Artefactos en `p1/salida/`:
`prefijo_r2_borrador_{A,B}.txt`, `reemplazos_r2_borrador_{A,B}.json`, `generados_hoy/` y
`generados_d15_17/` (tool schema, enums y manifiesto), `nofiltracion_{A,B}.json`,
`literales_mensaje_r2.txt` y `nofiltracion_mensaje.json` (el texto fijo del mensaje y de la NOTA: 0
ventanas de los chunks de prueba), `censo_p1.json`, `ejemplos_mensaje_r2.md`, `lado_a_lado.md` y `hashes_borrador.json`. Sus sha256, en el manifiesto
del paquete de revisión.
