# U-LISTAS-NOMAP — N2: diseño del proceso para las listas cerradas y lo no mapeable

Mandato `docs/mandatos/ULISTAS_NOMAP_diseno.md` (firmado en `30f106c`), etapa N2. USD 0, sin API ni Neo4j. Este
documento no mide nada nuevo: toda cifra sale de `reports/u_listas_nomap/n1_inventario.json` (etapa N1, commiteada en
`9c5331c`), con la clave entre paréntesis, o de la línea de código o del comando citados. Las cifras derivadas
(restas, proyecciones) salen del comando de la sección «Comandos».

Rótulos:
- **PROPUESTA P-xN**: cada propuesta lleva un id. Ninguna se implementa ni se decide acá: la política por campo y los
  campos nuevos del tool schema los lauda la autora en L-ESQ-R2 (plan, B2.11, unidad 5, `docs/plan_tesis.md:393`);
  los implementan U-PYD (unidad 7, `:395`), U-CAT-UNICO (unidad 6, `:394`), U-R2-CODIGO (unidad 8, `:396`) y
  U-PROMPT-R2 (unidad 10, `:398`).
- **[código]**: se aplica sobre la salida guardada de E1, sin re-extraer, a USD 0 (principio 12, `docs/plan_tesis.md:299`).
- **[prompt]**: exige cambiar el prompt o el tool schema de E1, es decir, U-PROMPT-R2 y una re-extracción.
- **NO MEDIDO**: dato que N1 no midió; se dice qué unidad lo mide.

Grupos, como en N1: r1 (cinco TOs, perfil `produccion_dev`), desarrollo, cinco y diez (tanda 0, perfil `v3_b54`).
Capas: L0 crudo del primer intento de E1; L0r crudo de los reintentos de E3; L1 validado del primer intento; L2 entrada
efectiva de E2; L3 grafo.

## 0. Premisas verificadas

1. El validador de E1 rechaza por tipo de entidad (`validador_e1.py:187`), predicado (`:265`), `sujeto_id` fuera del
   catálogo (`:306`) y firma. En el perfil v3 normaliza `Obligacion.tipo` a «otra» (`:212-215`). Anula sin registro el
   padre sugerido fuera del catálogo (`:313`). Convierte las properties a string sin filtrar claves ni valores
   (`:202-206`): Restriccion.tipo, Comunicacion.tipo y las claves no tienen control.
2. El crudo del primer intento está guardado en `extracciones_e1_compact.jsonl` (`tool_input_crudo`). El del reintento
   de E3 no está en `finales.jsonl` (tablero, fila «Crudo del reintento de E3 sin persistir», [c16]); en la tanda 0 vive
   solo en `e1_reintentos.db`, que cubre las 255 unidades con reintento (N1, `reintentos_db.t0`).
3. Parte de lo que llega al grafo fuera de lista no está en el primer intento: viene del crudo de los reintentos y de
   la cola (N1, `resumen_por_lista`; por ejemplo, Comunicacion.tipo en diez: 5 en L0, 3 en L0r, 8 en L3).
4. `sujeto_propuesto` ya se define como el «nombre del sujeto tal como aparece en el texto» (tool schema,
   `prompt_e1.py:314`; prefijo, `prompt_e1.py:111`, heredado por el prefijo v3). Es el único antecedente medible de
   una mención textual.
5. Completar el catálogo JSON con los seis ids del bloque que le faltan no resuelve ningún propuesto más: 3/1/4 con el
   catálogo actual y 3/1/4 con el ampliado (N1, `reresolucion_contrafactica`).
6. E1 valida `sujeto_id` contra el bloque del prompt, no contra el JSON: agregar un id solo al JSON no le permite al
   modelo sugerirlo (`data/backlog/backlog.jsonl`, `BKL-0034`, campo `propuesta`).

## a. Política por campo ante un valor fuera de lista

### a.1 Las tres opciones y sus consecuencias

| opción | en el grafo | en la re-aplicación en código |
|---|---|---|
| rechazar el elemento | el elemento no entra; si es una entidad, sus relaciones quedan colgantes y también se rechazan | cambiar la política re-corre el validador sobre el crudo guardado; la pérdida es visible solo si el rechazo se registra |
| normalizar con contador | el valor se reemplaza por uno de la lista; el grafo queda dentro de la lista | reversible solo si se guarda el valor original; un residuo como «otra» puede esconder errores |
| registrar sin cambiar | el valor queda, con marca `fuera_de_lista` y contador | la política se puede endurecer después en código sin re-extraer |

**PROPUESTA P-a0 [código].** La política es una tabla de configuración versionada: campo → modo (rechazar,
normalizar o registrar), más las tablas de alias cerradas. La leen los modelos Pydantic de U-PYD (decisión 2 del
30/09). Cada corrida registra el sha256 de esa tabla, y cambiar un modo re-corre el código a USD 0.

### a.2 Por campo

| campo | evidencia de N1 (fuera de lista) | hoy | propuesta |
|---|---|---|---|
| tipo de entidad (9) | L0: diez 4 (`Restriction` 2 en desarrollo, `Recomendacion` 2 en cinco); r1 0; L3 0 | rechazo | P-a1 |
| predicado (13) | L0: diez 2 (`establec⏎ida_en`, `establec ida_en`); r1 2 (`aplicaA`, `exceptua_restriccion`); L0r r1 2 (`estableci_en`, `establecia_en`); L3 extraídos 0 | rechazo | P-a2 |
| sujeto_id (102) | 0 en L0, L0r, L1 y L2 en los cuatro grupos; relaciones con ambos campos 1 y sin ninguno 2 en desarrollo, rechazadas (`sujeto_extremo_invalido`) | rechazo | P-a3 |
| padre sugerido | validador: 0 anulados en la tanda 0 (en r1 pasa 1 fuera del bloque v3, porque el validador era v2); esqueleto: 1 anulado en desarrollo y diez (`Sujeto_propuesto_originante` → `Sujeto_entidad_originante_de_transferencia`, fuera del JSON) | anulación sin registro | P-a4 |
| Obligacion.tipo (6) | L0: cinco 3 (`evaluacion`, `obtención_de_datos`, `pago`), normalizados; r1 2 (`verificacion`, `verificacion_informativa`), pasan; «otra» es el valor más frecuente: 1.398 de 2.365 en el crudo de diez | normalización a «otra» (v3) | P-a5 |
| Restriccion.tipo (3) | L0 = L3: desarrollo 4 (`limite_temporal` 3, `obligacion_cualitativa` 1); resto 0 | sin control | P-a6 |
| Comunicacion.tipo (3) | L0/L0r/L3: r1 14/4/14; desarrollo 4/2/6; cinco 1/1/2; diez 5/3/8. Valores: vacío, `Decreto`, `LEY`, `MINISTERIAL`, `Resolución`, `referencia`, `referencia_normativa`, `interna`, `normas`, `TO`, `otro` | sin control | P-a7 |
| claves de properties | L0/L0r/L3: r1 10/9/12; desarrollo 6/5/9; cinco 4/0/4; diez 10/5/13. Claves: `Obligacion.plazo_o_frecuencia`, `plazo_frecuencia`, `umbral`, `destinatario`, `referencia_normativa`, `modalidad_deonica`, `plazo_o_condicion`; `Potestad.tipo`, `Potestad.umbral`; `Operacion.etapa`; `TextoOrdenado.descripcion`, `tipo`, `referencia` | sin control (`validador_e1.py:202-206`) | P-a8 |
| valores de properties | todo valor se convierte con `str()`, `None` pasa a vacío; vacíos fuera de lista en L3: Comunicacion.tipo r1 2, cinco 1; valores no string: NO MEDIDO | sin control | P-a9 |
| omisiones como string | solo strings vacíos o de salto de línea: r1 3, desarrollo 2, cinco 2, diez 4 (N1, `omisiones.*.crudo_omisiones_como_string`) | descarte silencioso (`validador_e1.py:154-156`) | P-a10 |
| Operacion.tipo | texto libre, fuera de alcance como lista (decisión 2 del mandato); diez: 1.381 valores distintos en 2.110 Operacion en L0; 1.370 en 2.047 nodos en L3 | — | sin propuesta |

Fuentes de la tabla: `resumen_por_lista`, `grupos.<g>.capas.<capa>.fuera`, `grafos.<g>`, `propuestos_e4` y
`grupos.<g>.efecto_validador` de N1.

- **PROPUESTA P-a1 (tipos) [código].**
  - Normalizar con contador solo por una tabla cerrada de alias de forma (`Restriction` → `Restriccion`).
  - Rechazar el resto con registro y convertir cada elemento rechazado en una omisión de categoría `fuera_de_tipos`
    (P-e3).
  - Consecuencia: recupera las 2 entidades de desarrollo (y sus relaciones, hoy colgantes; cuántas: NO MEDIDO) y deja
    visibles las 2 de cinco.
- **PROPUESTA P-a2 (predicados) [código].**
  - Normalizar por forma con contador: quitar espacios y saltos internos y pasar de camelCase a snake_case. Después se
    valida la firma, como hoy.
  - Sin coincidencia aproximada por distancia de edición: `estableci_en` y `establecia_en` no se corrigen solos.
  - Un alias semántico, como `exceptua_restriccion` → `exceptua`, solo entra por una tabla que lauda L-ESQ-R2.
  - Lo que no normaliza se rechaza con registro.
  - Tasa sobre N1: en el crudo de diez, 2 de 2 se recuperan por forma; en r1, 1 de 2 en L0 y 0 de 2 en L0r.
- **PROPUESTA P-a3 (sujeto_id) [código].**
  - Una relación con `sujeto_id` fuera del catálogo no se rechaza: queda sin resolver y va al registro de no mapeados
    (d), con el id original y motivo `id_fuera_de_catalogo`.
  - Relación con los dos campos: se conserva `sujeto_id` como sugerencia y el texto propuesto como mención.
  - Relación sin ninguno: se rechaza con registro.
  - Consecuencia hoy: 0 casos fuera de catálogo y 1 relación recuperada en desarrollo. La guarda importa cuando el
    catálogo cambia entre corridas (`BKL-0028`, `BKL-0029`, `BKL-0034`; U-CAT-UNICO).
- **PROPUESTA P-a4 (padre sugerido) [código].**
  - Normalizar con contador conservando el original (`padre_sugerido_crudo`).
  - Validador y esqueleto usan el mismo catálogo (U-CAT-UNICO). Eso elimina la anulación del esqueleto (1 caso) y la
    doble fuente de la fila «Catálogo de sujetos en dos fuentes» del tablero ([c13]).
- **PROPUESTA P-a5 (Obligacion.tipo) [código].**
  - Mantener la normalización a «otra», pero guardar el valor original en el elemento (`tipo_original`). Hoy queda
    solo en el texto de una advertencia (`validador_e1.py:214-221`).
  - Contar aparte la clave ausente, que hoy pasa sin normalizar (condición `"tipo" in props`, `:213`).
  - Consecuencia: el grafo no cambia (0 fuera de lista en L3 de la tanda 0), y el re-mapeo es posible si L-ESQ-R2
    agrega valores.
  - El residuo «otra» ya es mayoría en el crudo de diez (1.398 de 2.365): tres valores más no se distinguirían sin el
    original.
- **PROPUESTA P-a6 (Restriccion.tipo) [código].**
  - Registrar sin cambiar, con marca `fuera_de_lista` y contador.
  - No se normaliza: el enum no tiene residuo, y `Restriccion.tipo` decide entre `prohibe` y `limita` (tabla de
    predicados de `prompt_v3_b54.PREFIJO_SISTEMA_V3`).
  - Tampoco se rechaza: se perderían 4 Restricciones con sus aristas.
  - Derivación en código desde el predicado emitido: solo `prohibe` → `prohibicion` es unívoca. Cuántos de los 4 la
    admiten: NO MEDIDO.
  - Un valor residual o un valor nuevo (`limite_temporal` aparece 3 veces) es decisión de esquema de L-ESQ-R2
    (principio 11).
- **PROPUESTA P-a7 (Comunicacion.tipo) [código].**
  - (i) Derivar el tipo del `codigo` o del label cuando tienen la forma de una Comunicación («A 7825», «A-7825») y
    normalizar con contador. La tasa de derivación es NO MEDIDA; U-PYD la mide sobre el crudo guardado.
  - (ii) Si no deriva, registrar sin cambiar con marca `fuera_de_lista`. No se rechaza: el nodo es destino de
    `referencia` o `modificada_por`, y rechazarlo borra la remisión.
  - En el crudo de r1, 12 de los 14 valores nombran otra clase de norma (`Decreto`, `decreto`, `LEY`, `MINISTERIAL`,
    `Resolución`: 5) o una referencia genérica (`interna` 2, `referencia_normativa` 2, `normas`, `referencia`,
    `referencia a normas`: 7); los otros 2 están vacíos. La clasificación de los valores es mía. El esquema no tiene tipo para normas externas: se declara como límite del pipeline y va a L-ESQ-R2
    (principio 11).
- **PROPUESTA P-a8 (claves fuera de la definición) [código].**
  - Registrar sin cambiar fuera de `properties`: la clave pasa a `properties_no_definidas`, con contador. El contenido
    no se pierde y el nodo queda dentro de su definición.
  - Nunca se rechaza un elemento por una clave.
  - Los renombres solo entran por una tabla unívoca que lauda L-ESQ-R2. `plazo_o_frecuencia` y `plazo_frecuencia` no
    son unívocos (plazo o frecuencia) y no se renombran.
  - `umbral` en Obligacion y Potestad depende del modelo de umbrales de U-UMBRAL (unidad 3, `:391`); acá no se decide.
- **PROPUESTA P-a9 (valores sin control) [código].**
  - Cada clave recibe un tipo en el modelo Pydantic: string no vacío en las claves textuales y `numero` de
    Comunicacion entero.
  - Vacío equivale a ausente y cuenta como fuera de lista en los campos con lista ([c11]).
  - Un valor no string se registra sin cambiar, con contador. Cuántos hay: NO MEDIDO; U-PYD lo mide.
  - Consecuencia: los nodos no cambian y los vacíos quedan visibles.
- **PROPUESTA P-a10 (omisiones como string) [código].** Un string no vacío se normaliza a lista de un elemento, con
  contador. Hoy no cambia nada: N1 solo encontró strings vacíos.

## b. Mención textual del sujeto

- **PROPUESTA P-b1 (campo nuevo) [prompt].**
  - Campo `sujeto_mencion` (string) en los ítems de `relations`.
  - Obligatorio cuando `predicate` es `aplica_a` o `ejecuta`; prohibido en los demás predicados, como los `sujeto_*`.
  - El JSON Schema del tool no expresa obligatoriedad condicional (hoy `required` es solo `predicate` y `punto`,
    `prompt_e1.py:322`), así que el campo queda opcional en el schema y lo exige el validador. Una relación de sujeto
    sin mención se registra y cuenta (P-b4), no se rechaza.
  - Descripción propuesta para el tool schema: «tramo del texto del chunk que nombra al sujeto, copiado tal cual
    aparece (mismas palabras, artículos y orden); no la forma del catálogo».
- **PROPUESTA P-b2 (relación con `sujeto_id`).**
  - `sujeto_id` pasa a ser la sugerencia del modelo y se guarda como `sujeto_id_modelo`. La resolución en código (c)
    decide el sujeto final y registra los desacuerdos.
  - El catálogo se sigue ofreciendo en el prompt, porque el modelo resuelve el colectivo del TO: en diez hay 1.737
    pares con el sujeto por defecto del TO y en 1.470 su label no está en el texto (N1,
    `sujetos_forzados.diez.defecto_del_to`).
  - `sujeto_propuesto` deja de ser campo del modelo en el prompt nuevo: cuando no hay `sujeto_id`, el código lo toma
    de la mención [código]. Para el crudo guardado de la tanda 0 se sigue leyendo `sujeto_propuesto` como mención.
  - Variante mínima, **P-b2'**: mantener `sujeto_id` y `sujeto_propuesto` como hoy y solo agregar la mención.
- **PROPUESTA P-b3 (verificación, nivel 1) [código].** Subcadena normalizada con la regla de N1 (R-NORM: unión de
  cortes por guion, NFKD sin diacríticos, minúsculas, no alfanuméricos a espacio), entre límites de palabra, en el
  texto propio o heredado del chunk de E0.

**Dimensionamiento con la tasa de N1 c.** La única población comparable hoy es `sujeto_propuesto`
(`sujeto_propuesto_literal.por_grupo`). «Fallan también por tokens» = ausentes que no tienen todos sus tokens en el
texto; es la descripción posterior de N1, no una regla.

| capa | grupo | total | fallan la subcadena exacta | fallan también por tokens |
|---|---|---|---|---|
| crudo L0 | r1 | 55 | 10 | 3 |
| crudo L0 | desarrollo | 44 | 11 | 7 |
| crudo L0 | cinco | 19 | 7 | 3 |
| crudo L0 | diez | 63 | 18 | 10 |
| entrada E2 | r1 | 67 | 17 | 5 |
| entrada E2 | desarrollo | 42 | 10 | 7 |
| entrada E2 | cinco | 19 | 5 | 3 |
| entrada E2 | diez | 61 | 15 | 10 |

**Proyección, no medición.** La mención irá en toda relación `aplica_a` o `ejecuta`: 4.099 en el crudo de diez (N1,
`grupos.diez.capas.crudo.forma_sujeto`: 4.034 + 62 + 1 + 2). Si la fracción de los propuestos se mantuviera, fallarían
la subcadena exacta del orden de 1.171 menciones (18 de 63) y la verificación por tokens del orden de 651 (10 de 63).

La población de propuestos no es aleatoria ni representa a las menciones de sujetos del catálogo: son nombres
descriptivos largos. Que las menciones del colectivo («las entidades») y de clases del catálogo fallen menos es un
supuesto NO VERIFICADO. La tasa real la mide la prueba pareada de U-PROMPT-R2 (`:398`, tope a fijar en su mandato) o
la re-extracción de U-REEXT-T0.

- **PROPUESTA P-b4 (qué hacer con las que fallan).** Tasas sobre el crudo de diez.
  1. **Nunca rechazar la relación por la mención.** Rechazar por subcadena exacta habría quitado 18 de las 63
     relaciones de la población actual. Una mención parafraseada no hace falsa la relación.
  2. **Nivel 2, verificación por tokens. Propuesta nueva, no es la regla de N1 [código].** Cada token normalizado de la
     mención está en el texto del chunk, dentro de una ventana acotada.
     - Sin ventana, aceptaría 53 de 63: 45 exactas y 8 por tokens. El tamaño de la ventana y la tasa de falsas
       aceptaciones (tokens dispersos que coinciden por azar) son NO MEDIDOS; se miden en U-PYD.
     - Cuando verifica por tokens, el código reemplaza la mención por el tramo literal mínimo del texto que contiene
       esos tokens y guarda la del modelo como `sujeto_mencion_modelo`. El tramo guardado siempre es texto del chunk.
  3. **Lo que falla los dos niveles** (10 de 63) se acepta con `mencion_verificada: no` y se cuenta.
     - Su sujeto no se resuelve por la mención: queda la sugerencia del modelo, si la hay (R4 de c).
     - Si no la hay, va al registro de no mapeados con motivo `mencion_no_verificada`.
  4. **Marca por relación**: `mencion_verificada` ∈ {`exacta`, `tokens`, `no`, `ausente`}, con contadores por chunk y
     por corrida.
  5. **[prompt] Instrucción nueva en U-PROMPT-R2**:
     - copiar la mención tal cual aparece: con artículos y en el orden del texto, sin llevarla a la forma del catálogo;
     - en una enumeración, una mención por sujeto (extiende la regla 7 del prefijo, `prompt_e1.py:141`, que ya pide
       una relación por sujeto);
     - si el sujeto está en el contexto heredado, copiarlo de ahí.

     Cuánto de las fallas actuales se debe a la falta de esa instrucción no se separa con el material de N1.
- **Relación con los posibles forzados.**
  - Con la mención, el indicador de N1 pasa a ser un control: sugerencia del modelo contra la resolución por la
    mención (c).
  - En diez, 61 de 398 pares de clases e instancias que no son el sujeto por defecto no tienen label ni alias en el
    texto (N1, `sujetos_forzados.diez.otra_clase_o_instancia`). Son los casos que la mención vuelve verificables.
  - La lectura de la muestra sellada (`muestra_forzados_30.csv`) dirá cuántos son forzados reales. Quién lee lo decide
    la autora (checklist P15 y Q12).

## c. Resolución en código (E4 generalizado)

**Dónde.** Por relación, entre E3 y E2, sobre la entrada efectiva de E2. Hoy E4 corre sobre el grafo fusionado y por
nodo propuesto (`r1_e4.resolver_propuestos`, `r1_e4.py:121-175`). La mención es por relación, así que la resolución
también. E2 recibe el sujeto ya resuelto. El E4 posterior al merge queda como pasada residual o se retira; eso lo
decide U-R2-CODIGO. [código]

- **PROPUESTA P-c1 (orden de las reglas).** Entrada: la mención verificada (`exacta` o `tokens`), normalizada con
  R-NORM y singularizada con `r1_e4._singular`, y el sujeto por defecto del TO (`ROL_POR_TO_V3`).
  - **R1**: `label_exacto` o `alias_exacto` sobre la mención (criterios de `r1_e4.indice_catalogo` y
    `resolver_label`, `r1_e4.py:74-118`).
  - **R2**: `id_slug`, `label_singularizado`, `alias_en_parentesis`, en el orden de `r1_e4.resolver_label`
    (`:101-112`).
  - **R3, colectivo del TO**: la mención es una expresión colectiva («las entidades», «los sujetos obligados») y
    resuelve al sujeto por defecto del TO, que es lo que el prompt prescribe (`prompt_e1.py:110`).
    - La lista de expresiones colectivas se declara en L-ESQ-R2 y se mide sobre las menciones de r2b; hoy es NO
      MEDIBLE, porque el campo no existe.
    - Sin R3, los 1.470 pares por defecto de diez cuyo label no está en el texto (N1,
      `sujetos_forzados.diez.defecto_del_to`) solo se resolverían por la sugerencia del modelo (R4).
  - **R4, sugerencia del modelo**: si R1 a R3 no resuelven y hay `sujeto_id_modelo`, se acepta con método
    `sugerencia_modelo`. Evidencia: en diez, 337 de 398 pares de clases e instancias no por defecto tienen label o
    alias en el texto (398 − 61, N1).
  - **Padre sugerido**: nunca resuelve por sí solo. Solo desempata `alias_en_parentesis`, como hoy (`r1_e4.py:108-112`),
    y ubica el no resuelto en el registro y en el esqueleto (arista `padre_sugerido` en cuarentena).
  - **Ambigüedad**: si dos reglas dan ids distintos, no resuelve. Va al registro con motivo `ambiguo` y los
    candidatos, como hoy (`r1_e4.py:113-118`).
  - **Sin resolver**: va al registro de no mapeados (d) y a un nodo `Sujeto_propuesto` en cuarentena, como hoy
    (`e2_lib.py:382-407`).
- **PROPUESTA P-c2 (desacuerdos entre regla y modelo).**
  - Si R1 o R2 resuelven a un id distinto de `sujeto_id_modelo`, gana la regla: el prefijo pide «EXACTAMENTE la clase
    que el texto nombra» (`prompt_e1.py:106`), y la regla lee el texto.
  - Si el desacuerdo es con R3, gana el modelo cuando su id es miembro del rol del TO.
  - Todo desacuerdo se registra con los dos ids y es la población de lectura.
  - Variante **P-c2'**: gana siempre el modelo y la regla solo se registra; conserva el grafo actual.
  - Evidencia para elegir: NO MEDIDA (sin mención no hay desacuerdos que contar). El único proxy es el indicador de
    forzados (61 de 398 en diez).
- **PROPUESTA P-c3 (registro del método).**
  - Cada arista `aplica_a` o `ejecuta` que no es de esqueleto lleva `metodo_resolucion`: R1, R2 con su criterio, R3 o
    R4.
  - El detalle va en un archivo lateral por corrida, `resolucion_sujetos.jsonl`: mención, `mencion_verificada`,
    `sujeto_id_modelo`, id resuelto, regla, desacuerdo y sha256 del catálogo. Una fila por relación, con la clave del
    registro de d.
  - Así el `kg.json` crece en una clave por arista y no en el detalle.
- **El contrafáctico de N1 d, para c y d.**
  - Completar el JSON con los seis ids no resuelve ningún propuesto (3/1/4 contra 3/1/4): ninguno de los criterios de
    `r1_e4.resolver_label` resuelve los que están en cuarentena, ni con el catálogo ampliado. La palanca no es
    completar el JSON con ids que ya están en el bloque, sino:
    1. ids nuevos admitidos con el criterio de `docs/esquema_v2_diseño.md:348`, guiados por el ranking del registro
       (P-d4);
    2. para las menciones que califican una clase existente, una decisión de esquema en L-ESQ-R2: resolver a la clase
       y guardar el calificador, o mantenerlas en cuarentena. Ejemplo: «Entidades del Grupo A», con padre sugerido
       `Sujeto_rol_entidad_comprendida_reginf`, en `ens_desarrollo/r1/e4_propuestos.json`.
  - Cuántos de los 30 en cuarentena de diez son de cada clase es NO MEDIDO: requiere lectura. El registro lo vuelve
    medible con `categoria_no_mapeo` (P-d2).
  - La mención desacopla crecimiento del catálogo y re-extracción: con la mención guardada, un id nuevo se aplica en
    código. Pero el modelo solo lo sugiere cuando se regenera el bloque del prompt (premisa 6; U-CAT-UNICO).

## d. Registro de no mapeados

- **PROPUESTA P-d1 (archivo y punto del pipeline).**
  - `no_mapeados_sujetos.jsonl`, uno por TO en el directorio de salida de E1 a E3 y uno consolidado en cada
    ensamblado, con el id del nodo del grafo.
  - Lo escribe el paso de resolución (c), entero y en forma determinística, en cada aplicación o re-aplicación.
  - E2 crea los nodos `Sujeto_propuesto` desde este registro, no desde `sujeto_propuesto` como hoy
    (`e2_lib.py:382-407`): registro y grafo coinciden por construcción.
- **PROPUESTA P-d2 (campos), una fila por relación sin resolver.**
  - **Clave**: `to`, `chunk_id`, `e0_sha256_completo` (desambigua ante ids de chunk repetidos, `BKL-0037`),
    `indice_relacion` (en el crudo), `punto`, `predicado`.
  - **Elemento alcanzado**: `extremo_local_id`, `extremo_tipo`, `extremo_label`.
  - **Mención**: `mencion`, `sujeto_mencion_modelo`, `mencion_verificada`, `tramo` (bloque: propio o
    `herencia[i]`, con offsets sobre el texto de E0).
  - **Modelo**: `sujeto_id_modelo`, `sujeto_propuesto_modelo` (crudo), `padre_sugerido_crudo`, `padre_sugerido`.
  - **Resolución**: `motivo` (`sin_match`, `ambiguo`, `mencion_no_verificada`, `id_fuera_de_catalogo`), `candidatos`,
    `categoria_no_mapeo`. Esta última queda vacía y se llena por lectura: sujeto ausente del catálogo, calificación de
    una clase existente, enumeración sin partir o error de extracción.
  - **Versiones**: `catalogo_sha256`, `politica_sha256` (P-a0), `perfil`, `prefijo_hash`.
  - **Estado**: `cuarentena` o `resuelto`, y si se resolvió, `resuelto_a`, `metodo` y el `catalogo_sha256` con que
    resolvió.
- **PROPUESTA P-d3 (re-resolución por programa) [código].**
  - Cuando el catálogo cambia (sha256 nuevo del JSON único de U-CAT-UNICO), se re-corre la resolución sobre la salida
    validada guardada, con el índice nuevo (`r1_e4.indice_catalogo`).
  - Las filas que resuelven pasan a `resuelto` con el sha nuevo; se re-ensambla de E2 a E5, a USD 0 y sin
    re-extraer, porque la mención está guardada.
  - El bloque del prompt se regenera para las extracciones futuras, no para re-resolver.
  - Sobre la tanda 0 se puede aplicar ya [código], con `sujeto_propuesto` como mención: en diez, 63 relaciones en L0 (62 solo
    con propuesto y 1 con ambos campos) y 61 en L2; 34 propuestos, 30 en cuarentena (N1, `forma_sujeto`,
    `sujeto_propuesto_literal`, `propuestos_e4`).
- **PROPUESTA P-d4 (cómo se mide).**
  1. No mapeados por cada 1.000 relaciones con sujeto, por TO y por corrida.
  2. Distribución por motivo y por `categoria_no_mapeo`.
  3. Resueltos por versión del catálogo: la curva que muestra si crecer el catálogo resuelve. Con los seis ids, hoy
     sumaría 0 (N1 d).
  4. Frecuencia de las menciones no mapeadas agrupadas por forma normalizada: un ranking para el crecimiento del
     catálogo, con el criterio de admisión de `docs/esquema_v2_diseño.md:348`.

  La meta de resueltos es DECISIÓN ABIERTA de la autora (tablero, fila «Mención del sujeto sin guardar; sujetos no
  mapeables»).

## e. Omisiones con categoría y tramo literal en todo chunk

**Hoy.**
- `omisiones_no_prosa` es una lista de strings libres, pedida solo en chunks marcados por E0 (`prompt_e1.py:158-165`;
  tool schema, `:326-330`). La regla 9 del prefijo v3 (contenido meta-normativo) omite sin dejar registro.
- N1 (`omisiones`), capa [c15]: 81 de 1.763 unidades con omisión en r1, 78 de 1.763 en desarrollo, 7 de 671 en cinco y
  85 de 2.434 en diez.
- De esas, están en chunks sin marca de E0: 20, 21, 2 y 23.
- Chunks marcados con extracción y sin omisión: 0 en los cuatro.
- Las omisiones de la regla 9: NO MEDIBLES, porque no dejan registro.

- **PROPUESTA P-e1 (campo) [prompt].**
  - Campo `omisiones`, que reemplaza a `omisiones_no_prosa` en el prompt nuevo: lista de objetos `{categoria, tramo,
    nota}`, obligatoria en todo chunk (vacía si no se omite nada).
  - `categoria` ∈ {`meta_normativo`, `tabla`, `formula`, `fuera_de_tipos`}.
  - Instrucciones nuevas en U-PROMPT-R2:
    - la regla 9 pasa de «no se extrae» a «no se extrae y se registra con categoría `meta_normativo` y su tramo»;
    - la regla 4 («NO inventes tipos», que prefiere no extraer a forzar) registra lo no extraído como
      `fuera_de_tipos`;
    - la sección de contenido no-prosa usa `tabla` y `formula` con tramo.
  - Para leer el crudo de la tanda 0, cada string de `omisiones_no_prosa` se lee como omisión sin categoría y sin tramo
    [código].
- **PROPUESTA P-e2 (validación del tramo) [código].**
  1. Subcadena normalizada (R-NORM) del texto propio del chunk. No del heredado: la unidad extrae y el contexto ancla
     (`prompt_e1.py:122`).
  2. Si falla, nivel por tokens como en P-b4, y reemplazo por el tramo literal mínimo.
  3. Longitud mínima del tramo, para que identifique contenido: umbral NO MEDIDO, a fijar en U-PYD.
  4. Categoría fuera del enum: registrar sin cambiar (política de a).
  5. Coherencia con E0: una omisión `tabla` o `formula` en un chunk que E0 no marca no se rechaza. Se cuenta como señal
     de tabla no detectada, como el cuadro de códigos de `ric:9.2` (tablero, fila «Pérdidas de contenido por tablas»,
     [c17]).
  6. Un chunk marcado, con extracción y sin omisión, pasa de advertencia (`validador_e1.py:375-386`) a contador
     visible.

  Tramo no verificado: `tramo_verificado: no`, contado; la omisión se conserva.
- **PROPUESTA P-e3 (tipos rechazados como omisión) [código].**
  - Una entidad rechazada por `type_invalido` se registra como omisión `fuera_de_tipos`, con su label y su tipo
    propuesto como nota y sin tramo, porque el crudo no lo trae.
  - En diez son 4: las 2 `Recomendacion` de cinco quedan como omisión. Las 2 `Restriction` se recuperan si se adopta
    P-a1.
- **PROPUESTA P-e4 (reproceso dirigido que habilita).** La categoría y el tramo identifican chunk y tramo.
  1. `tabla` y `formula`: re-extracción dirigida con el tratamiento de tablas de U-R2-CODIGO (`:396`, primera
     prioridad), solo de los chunks con esa categoría.
  2. `fuera_de_tipos`: evidencia de esquema acumulada por forma (principio 11). La re-extracción dirigida de esos
     chunks solo tiene sentido después de un cambio de esquema en L-ESQ-R2 o en una ventana posterior.
  3. `meta_normativo`: lectura de control sobre una muestra, sin re-extraer, para vigilar el caso que la regla 9 excluye
     (contenido habilitante, que es Potestad). Quién lee lo decide la autora (P15, Q12).
  4. En los tres casos, el costo de un reproceso es proporcional a las unidades con la categoría, no al corpus
     (precedente: la re-extracción dirigida de tres unidades de cap, `corpus_tanda0/salida_dirigida/reextraccion_dirigida.json`).

**Cómo se mide.** Unidades con omisión por categoría y por marca de E0; tramos verificados sobre el total; chunks
marcados con extracción y sin omisión (hoy 0); `meta_normativo` por TO. La línea de base de esta última empieza en r2b,
porque hoy no hay registro.

## f. Qué se re-aplica sin re-extraer y qué exige el prompt nuevo

| propuesta | qué | sin re-extraer: código, r2a, USD 0 | exige prompt nuevo: U-PROMPT-R2, r2b | unidad |
|---|---|---|---|---|
| prerrequisito | crudo del reintento de E3 persistido | sí, para r2; en la tanda 0 se lee de `e1_reintentos.db` | no | U-R2-CODIGO |
| P-a0 | política como tabla versionada | sí | no | L-ESQ-R2, U-PYD |
| P-a1, P-a2 | normalización de forma de tipos y predicados, rechazo con registro | sí | no | U-PYD |
| P-a3 | sujeto_id fuera de catálogo al registro; ambos y ninguno | sí | no | U-PYD |
| P-a4 | padre sugerido conservado; catálogo único | sí | no | U-PYD, U-CAT-UNICO |
| P-a5 | Obligacion.tipo con original | sí | no | U-PYD |
| P-a6, P-a7 | Restriccion.tipo y Comunicacion.tipo: marca, derivación, registro | sí | un valor nuevo del enum: sí (L-ESQ-R2) | U-PYD, L-ESQ-R2 |
| P-a8, P-a9, P-a10 | claves y valores tipados; omisiones como string | sí | no | U-PYD |
| P-b1 | campo `sujeto_mencion` | no | sí | U-PROMPT-R2 |
| P-b2 | sujeto_id como sugerencia; propuesto derivado de la mención | parcial: en la tanda 0, con `sujeto_propuesto` como mención | sí, para todas las relaciones | U-PROMPT-R2, U-PYD |
| P-b3, P-b4 | verificación en dos niveles, tramo literal, marcas | sí, una vez que el campo existe; sobre la tanda 0, solo las 63 relaciones con propuesto de diez | la instrucción «copiar tal cual»: sí | U-PYD, U-PROMPT-R2 |
| P-c1, P-c2, P-c3 | resolución por relación, desacuerdos, método | parcial: R1, R2 y R4 sobre `sujeto_propuesto` y `sujeto_id`; R3 necesita la mención | sí, para R3 y los desacuerdos | U-R2-CODIGO, U-PYD |
| P-d1 a P-d4 | registro de no mapeados y re-resolución | sí: se construye ya desde `sujeto_propuesto` | la mención completa: sí | U-R2-CODIGO |
| P-e1 | campo `omisiones` con categoría y tramo; reglas 4 y 9 | no | sí | U-PROMPT-R2 |
| P-e2 | validación del tramo | sí, una vez que el campo existe | — | U-PYD |
| P-e3 | tipos rechazados como omisión `fuera_de_tipos` | sí | no | U-PYD |
| P-e4 | reproceso dirigido | la selección de chunks: sí | la re-extracción de los seleccionados: sí, con tope propio | U-R2-CODIGO, U-REEXT-T0 |

## g. Tests de la suite y shapes que harían falta (propuesta; no se escriben)

**Suite** (`scripts/regression_kg.py`). Ítems nuevos con prefijo LN, para no chocar con T1–T7, I1–I5, E4-a1…E4-c,
`BKL-*` y `RT-*`:
- **LN-1**: ningún valor fuera de lista sin tratar. Todo campo con lista está en la lista o lleva `fuera_de_lista` con
  su fila de contador. Línea de base: las cifras de [c11].
- **LN-2**: las `properties` de cada nodo están dentro de la definición del tipo; lo demás está en
  `properties_no_definidas`.
- **LN-3**: toda arista `aplica_a` o `ejecuta` que no es de esqueleto lleva mención y `mencion_verificada`. Hoy 0 de
  3.019 en desarrollo ([c12]).
- **LN-4**: toda arista de sujeto que no es de esqueleto lleva `metodo_resolucion`; los desacuerdos se cuentan.
- **LN-5**: registro y grafo coinciden. Cada nodo `Sujeto_propuesto` tiene al menos una fila en
  `no_mapeados_sujetos.jsonl`, y cada fila en cuarentena tiene su nodo.
- **LN-6**: re-resolución idempotente. Mismo catálogo, mismo registro byte a byte. Con el catálogo ampliado de R-CAT
  reproduce el contrafáctico de N1 (3/1/4).
- **LN-7**: toda omisión tiene categoría del enum y tramo verificado o marcado; 0 chunks marcados con extracción y sin
  omisión.
- **LN-8**: catálogo único; bloque del prompt y JSON sin diferencias (hoy 6 y 5, [c13]). Es el primer selftest de
  U-CAT-UNICO.

**Selftests de U-PYD.** Fixtures con los valores reales de N1: `Restriction`, `Recomendacion`, `establec⏎ida_en`,
`establec ida_en`, `aplicaA`, `exceptua_restriccion`, `estableci_en`, `limite_temporal`, `obligacion_cualitativa`,
Comunicacion.tipo `Decreto` y vacío, `Obligacion.plazo_o_frecuencia`, `Obligacion.tipo` `evaluacion`, un padre fuera
del catálogo, una relación con ambos campos y otra con ninguno, y `omisiones_no_prosa` = `"\n"`. Cada uno con el modo
esperado según la tabla P-a0.

**Shapes** (`scripts/shapes_validator.py`, solo stdlib, control independiente de Pydantic, `:395`). La numeración
sigue después de S23; S18 está reservada (`scripts/shapes_validator.py:160-164`).
- **S24**: enum de Restriccion.tipo, bloqueante salvo marca `fuera_de_lista`.
- **S25**: enum de Comunicacion.tipo, ídem.
- **S26**: claves cerradas por tipo, bloqueante.
- **S27**: arista de sujeto con mención y método; informativa en r2a, bloqueante desde r2b.
- **S28**: `Sujeto_propuesto` con fila en el registro, bloqueante.
- **S29**: destino de `padre_sugerido` en el catálogo único; informativa hasta U-CAT-UNICO (hoy 1 caso fuera del
  JSON). Complementa S22.

S19 (catálogo) y S20 (enum de Obligacion.tipo) ya existen (`scripts/shapes_validator.py:166-171`).

## Relación con el checklist

Ítems que la unidad absorbe o alimenta (`docs/checklist_pre_escalado.md:149-155`):
- **X6** (`BKL-0034`, sujeto de nivel órgano) y **X7** (`BKL-0028`, `BKL-0029`): los remedios se laudan en L-ESQ-R2
  y los aplica U-CAT-UNICO. Este diseño les aporta el registro de no mapeados y la re-resolución por programa (P-d1 a
  P-d4): un id nuevo se aplica en código sobre lo guardado, y el ranking del registro prioriza qué ids abrir.
- **X9** (asignación de sujeto, corrección sistemática vía prompt o validador): la vía propuesta es la mención
  verificada y la resolución en código con registro de desacuerdos (P-b1 a P-c3). El laudo de los 15 de B2.4 sigue
  pendiente, fuera de esta unidad.
- **X12** (validación con Pydantic de todas las listas, con política por campo): sección a.
- **X13** (lo no mapeable y las omisiones): secciones b a e.

## Decisiones abiertas para L-ESQ-R2 que salen de este diseño

1. Modo por campo (P-a1 a P-a10) y las tablas de alias.
2. Valor residual o valores nuevos para Restriccion.tipo; tipo para normas externas en Comunicacion (principio 11).
3. Nombre y obligatoriedad de `sujeto_mencion` (P-b1). `sujeto_propuesto` como campo del modelo o derivado (P-b2 o
   P-b2').
4. Verificación por tokens (P-b4, nivel 2) y su ventana.
5. Quién gana en un desacuerdo entre regla y modelo (P-c2 o P-c2'). La lista de expresiones colectivas de R3.
6. Categorías de omisión (P-e1) y longitud mínima del tramo (P-e2).
7. Meta de resueltos del registro (P-d4).

## Comandos

Todos desde la raíz del repo.

Cifras de N1 (las claves citadas en el texto):

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_listas_nomap/u_listas_n1.py --out-dir reports/u_listas_nomap
```

Cifras derivadas de este documento: fallas por subcadena y por tokens, proyección sobre las 4.099 relaciones de diez,
337 de 398, omisiones en chunks sin marca y «otra» en Obligacion.tipo:

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B -c "import json;J=json.load(open('reports/u_listas_nomap/n1_inventario.json'));G=['r1','desarrollo','cinco','diez'];L=J['sujeto_propuesto_literal']['por_grupo'];[print(c,g,L[c][g]['total'],L[c][g]['ausente'],L[c][g]['ausente']-L[c][g]['ausente_con_todos_los_tokens'],L[c][g]['presente']+L[c][g]['ausente_con_todos_los_tokens']) for c in ('crudo','entrada_e2') for g in G];f=J['grupos']['diez']['capas']['crudo']['forma_sujeto'];n=sum(f[k] for k in ('solo_sujeto_id','solo_sujeto_propuesto','ambos','ninguno'));x=L['crudo']['diez'];print(n,round(n*x['ausente']/x['total']),round(n*(x['ausente']-x['ausente_con_todos_los_tokens'])/x['total']));s=J['sujetos_forzados']['diez']['otra_clase_o_instancia'];print(s['pares']-s['posibles_forzados_amplia'],s['pares']);[print(g,J['omisiones'][g]['con_omisiones_por_marca']['finales_c15'].get('sin_marca',0)) for g in G];o=J['grupos']['diez']['capas']['crudo']['conteos']['Obligacion.tipo'];print(o['otra'],sum(o.values()))"
```
