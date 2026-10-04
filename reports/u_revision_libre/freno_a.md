# U-REVISION-LIBRE — FRENO A: lista completa de la fase A (a ciegas)

**Base.** HEAD `95dfd98`, leído desde una copia de lo commiteado (`git archive`) en el scratchpad. Grafo: `data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2a/r2/kg.json` (8.358 nodos, 29.499 aristas), que sale de la extracción con el prompt sellado y del ensamblado r2. USD 0, sin API ni Neo4j. Escribí solo en `reports/u_revision_libre/` y en el scratchpad.

**Método.** Leí yo: el prompt nuevo (borrador B) y el de E3, 27 de 40 unidades sorteadas (semilla 20261003) contra sus nodos, 45 faltantes bloqueantes de E3, y 15 preguntas escritas desde los PDF. Delegué tres lecturas de código y datos (E0 corrida sobre los 152 TOs de la partición en una copia, ensamblado, escala) y recomputé sus cifras principales. Marco **[V]** lo que verifiqué yo y **[A]** lo que sale de una lectura delegada sin recómputo mío. Las gravedades son las del mandato: 1 = afirmación falsa en un campo estructurado; 2 = contenido de la norma perdido o deformado; 3 = ruido o costo.

**Declaraciones.** El índice de memoria del proyecto y los mensajes de los últimos commits entraron a mi contexto al abrir la sesión. Leí `prompt_r2/diseno_prefijo_r2.md` §4.3–4.5 y §10 y `p1/salida/lado_a_lado.md` (lo commiteado de `prompt_r2/`). No leí plan, tablero, checklist, backlog, mandatos, laudos, enmiendas, frenos ni nada de `ev2*`. El árbol de trabajo cambió durante la sesión por otras unidades (86 entradas en `git status` al empezar, 98 al cerrar); HEAD no cambió.

## Gravedad 1 — afirmación falsa en un campo estructurado

| # | Hallazgo | Evidencia | Frecuencia y base | Dónde se corrige |
|---|---|---|---|---|
| 1.1 | Valores de una tabla cruzados entre columnas | `cap::1.2`: el grafo dice bancos 2.500 millones y restantes 5.000; el PDF (p. 4), lo contrario. Los dos umbrales llevan `tramo_verificado: no` y se escriben igual | [V] 17 de 842 umbrales con `tramo_verificado = no` y 31 con `verificado_en_tabla = false` | Re-extracción con la tabla serializada; código: un umbral no verificado no debería quedar como valor |
| 1.2 | Límites mínimos de capital leídos como cálculo o definición | `cap::8.5.1` a `8.5.3` (PDF p. 168, «deberán observarse los siguientes límites mínimos:»): Obligacion `calculo` «el PNb deberá calcularse como… 6 %», comparación `coeficiente`; Definicion «CO: … 4,5 %» | [V] 3 de 3 ítems de esa lista | Prompt (el sentido está en el encabezado y la cifra en el ítem) y regla de `coeficiente` |
| 1.3 | Recomendación tipada como deber | `lingob::2.1.2` → Obligacion «Monitoree el perfil de riesgo»; PDF p. 5: «se considera como buena práctica» | [V] 141 Obligacion en 102 de 139 unidades de `lingob`; 8 conservan la marca. Partición: 181 de 9.324 unidades, 27 TOs | Prompt de E1 |
| 1.4 | Consecuencia de un incumplimiento forzada en Restriccion | `pagjub::2.9.2` (prohibicion «serán pasibles…», prohibicion «El BCRA debitará…»); `ctacte::6.5.1` (multa 4 % que `limita` la operación de rechazo y `aplica_a` el banco) | [V] 4 de 6 Restriccion con multa o sanción son falsas; marca de sanción en 38 de 2.434 unidades y en 216 de 9.324 de la partición | Prompt de E1 |
| 1.5 | Norma atribuida al sujeto por defecto del TO | «El BCRA procederá a acreditar…» → `aplica_a` rol de `pagjub` (`pagjub::2.8.1.2`); `ctacte::8.8.1.1`, cese de la inhabilitación → Sujeto_banco | [V] 4.026 de 4.086 aristas de sujeto sin mención (`R4_sugerencia_modelo`). [A] 30 leídas: 5 en cabeza de quien no corresponde, 9 por defecto | Prompt nuevo (mención) y código (marca «por defecto») |
| 1.6 | `remite_a` reparte una cita de punto a punto entre todos los nodos | `r1_referencias.py:1154-1172`; `cap::4.2.1.1` → `cap::4.2.1.2`: 1.080 aristas | [V] 14.000 aristas desde 1.316 pares (unidad, punto citado), mediana 6; en 6.291 el nodo de origen no nombra el punto. [A] 20 leídas: 6 con los dos extremos bien | Código |
| 1.7 | Cita a otra norma resuelta como interna | `ext::10.4.4`, «punto 10.3.6. del Anexo de la Comunicación A 7914» → 11 aristas a `ext::10.3.6` | [V] ese caso. [A] 3 menciones y 13 aristas en la tanda 0; fuera de ella, «Código Civil… Sección 7ª» y «Circular RUNOR» | Código |
| 1.8 | Plazo sin marcador asumido como máximo | `reglas_comparacion.py:443-445`; «luego del plazo de 2 (dos) años» → `maximo_inclusivo` | [V] 176 de 842 umbrales, todos con `comparacion_asumida`; 2 de 12 leídos son un máximo (semilla 99). [A] 38 de 176 | Código (no asumir) |
| 1.9 | Comparación invertida o con el borde equivocado | «no podrán tener un plazo de pago que exceda a los 360 días» → `minimo_estricto` (`ext::4.2::cierre`); «equivalente o superior al 1 %» → `minimo_estricto` (`cla::3.4.4`) | [V] esos dos. [A] 12 de 79 umbrales de reglas simples | Código |
| 1.10 | «Ponderador» pisa al comparador | «no superarán el 1,25 % de los activos ponderados» → `coeficiente` | [V] ese caso. [A] 26 de 140 `coeficiente` | Código |
| 1.11 | Operacion fundida por etiqueta entre puntos | `Operacion_emision_de_cheque_c50f16`: cuatro unidades, descripción «Cheque que carece de valor…» | [V] 64 Operacion con más de una procedencia. [A] 5 de 8 leídas describen solo el primer punto | Código (E2) |
| 1.12 | Nodos Comunicacion que no son Comunicaciones | «art. 39 inc. d) de la Ley 21.526» → `codigo: A-39` (`ctacte::12.10.2`) | [V] 11 de 22 | Código; el prompt nuevo deriva tipo y número |
| 1.13 | Datos del TextoOrdenado tomados del primer chunk | `ctacte`: materia «Cuentas a la vista»; `version` = «actual» en los 10 | [V] 10 de 10 en `version` | Código (el prompt nuevo ya lo pasa a código) |
| 1.14 | E0 no abre una sección escrita de otra forma | `opecam`, PDF «Seccón 3.»: no hay unidad S3 y su título está dentro de `opecam::2.6` | [V] `opecam`. [A] 5 TOs («Sección 2 Operaciones», «Sección 7 – …»); 0 de 10 en la tanda 0 | Código de E0 |
| 1.15 | E0 toma por rótulo de punto lo que no lo es | Remisión envuelta («y 1.7. “Diseño de registros”.»), número de ley (`ri_niif::21.526`), filas de tabla (`rdbcra::11.1.2` junta su multa con la descripción de otra fila) | [A] 10 TOs; [V] solo `rdbcra` | Código de E0 |
| 1.16 | Cierre de una lista dentro del último ítem | `pro::1.1.2.7` (PDF p. 3): el párrafo «Cuando un tercero desarrolle tareas…» vale para todo 1.1.2 | [V] 1 caso | Código de E0 |
| 1.17 | Indicador de una categoría tipado como deber | `cla::6.5.3.10`: Restriccion «Los arreglos privados deben contar con la opinión del auditor externo…» | [V] 1 de 27 unidades leídas | Prompt nuevo (ítems como Condicion); el vínculo con la categoría queda fuera (2.8) |
| 1.18 | Lista dentro de una unidad | `pro::3.2.1.3`: guiones de lo que verifica la auditoría, como deberes autónomos | [V] 1 de 27 | Prompt de E1 |

## Gravedad 2 — contenido de la norma perdido o deformado

| # | Hallazgo | Evidencia | Frecuencia y base | Dónde se corrige |
|---|---|---|---|---|
| 2.1 | Unidades mudas | `ric::6.3`, `cap::5.3.2.3`, `ext::6.5.3`, `ctacte::5.6.1`: `entities` llega como string con el JSON entero; sin E3, sin reintento, sin cola. El contenido está íntegro en el crudo | [V] 4 de 2.434 | Código |
| 2.2 | Veredicto de E3 mal formado manda la unidad a la cola | `faltantes` como string | [V] 25 veredictos; 24 se leen con `json.loads` | Código |
| 2.3 | E0 borra renglones al tope de página | `ric` p. 15: «De corresponder, la exigencia por monedas residuales se calculará conforme a los puntos 6.2.2.2. y 6.2.2.7.…» no está en ninguna unidad (`e0_lib.py:644-654`) | [V] ese caso. [A] 20 páginas, 29 renglones, 10 TOs; 4 páginas en `ric` | Código de E0 |
| 2.4 | Páginas de norma tomadas como portada o como índice | `ri_cc`: la primera unidad empieza en la p. 49; la p. 1 tiene norma («tiene carácter de declaración jurada…») | [V] `ri_cc`. [A] `ri_tsa`, `snp_mep`, `venliq`, `fimipyme`: 5 de 147; 0 de 10 | Código de E0 |
| 2.5 | Páginas de fichas fuera de toda unidad | `manual` (1.830 páginas), `ri2_pm`, `plandecuentas`, `ri_laft`, `ri_transpa` | [A] 2.281 páginas, 19,0 % del texto de los 147 | Límite a declarar |
| 2.6 | El linaje no llega al grafo | 0 aristas `modificada_por`, 17 `referencia`; el pie de cada página (versión, Comunicación, vigencia) y la tabla «Origen de las disposiciones» no pasan de E0 | [V] 10 de 10 TOs | Código (procedencia) |
| 2.7 | Alcance que vive en la cadena de títulos | `docvig::2.1.1.1`: «Pasaporte del país de origen», igual en 2.1.2.1 y 2.2.1.1; `provenance.ancestros` trae ids | [V] 228 de 2.052 puntos terminales con menos de 100 caracteres (336 nodos); partición 1.275 de 7.430 | Código (títulos en la procedencia y en la búsqueda) o prompt |
| 2.8 | Excepcion y Condicion sin la norma que tocan | `ext::2.2.1`, `pro::3.1.6`, `cla::3.4.4` | [V] Excepcion 221 de 411 (130 con la norma en la misma unidad); Condicion 232 de 1.409 (122) | Prompt (misma unidad); límite (otra unidad) |
| 2.9 | Relaciones que el modelo emite y el esquema no admite | Condicion `aplica_a` 48; Excepcion → Operacion 39; Definicion `aplica_a` 23; Potestad ↔ Operacion | [V] 1.039 rechazos por firma; 679 los admite r2 | Esquema: lo reporto, no lo recomiendo |
| 2.10 | Tipos sin relaciones ni umbrales | Definicion: 631 de 631 solo con `establecida_en`. Cuantía en la descripción y sin `umbrales`: Potestad 24, Definicion 67, Operacion 97 | [V] | Esquema: límite a declarar |
| 2.11 | Fórmulas y subíndices | `ric::6.3`; «COn1» queda «CO» + «n1»; «APRc» queda «APR» + «c» (`cap::8.5`) | [V] esos casos. [A] «(cid:N)» 432 veces en 9 TOs del resto | Límite; E0 |
| 2.12 | Tablas sin serializar fuera de la tanda 0 | — | [A] 22,4 % del texto del resto contra 4,0 % | E0 o límite |
| 2.13 | Remisiones que no llegan | Citas a un contenedor sin nodos; formas no reconocidas («el punto 4. de las presentes instrucciones», «normas de X» sin «sobre», régimen informativo nombrado) | [A] 191 pares sin arista en la tanda 0; 185, 67 y 124 apariciones en el resto | Código |
| 2.14 | El reintento reemplaza la extracción sin comparar | `cap::12.3`: de 12 a 8 entidades | [V] de 220 aceptadas tras reintento: 18 con menos entidades, 27 con menos relaciones, 12 con menos de ambas | Código |
| 2.15 | Cortes de salida | `cap::3.1.14.1`, `4.2.1.2`, `4.3.3.1` en la tanda 0 | [V] 77 unidades de 10.981 caracteres o más en 37 TOs de la partición; 53 no son puntos terminales; la mayor, 266.075 | Código y E0 |
| 2.16 | Mini-chunks que empiezan a mitad de oración | `pro::4.2.1::intro`, `cap::2.7.2::intro` | [V] 125 de 376 | E0 o mensaje de E1 |
| 2.17 | TOs sin estructura numerada | — | [A] 10 TOs en una sola unidad; `plandecuentas` vacío; 61 de 147 por caminos que la tanda 0 no ejercitó | E0; límite |
| 2.18 | Vigencias y fechas sin campo | — | [V] 355 nodos con fecha solo en la descripción; la regla 9 manda no extraer las reglas de vigencia | Límite a declarar |

## Gravedad 3 — ruido o costo

| # | Hallazgo | Frecuencia y base | Dónde se corrige |
|---|---|---|---|
| 3.1 | Operacion fragmentada; `tipo` libre | [V] 1.301 valores en 2.047 nodos; 50 nombran «acceso al mercado de cambios» | Navegación |
| 3.2 | Tres predicados Obligacion–Operacion sin definición | [V] `regula` 521, `requiere` 450, `condiciona` 89; 7 `regula` desde Restriccion | Prompt |
| 3.3 | La cola humana entra al grafo marcada y nadie la procesa | [V] 71 unidades, 291 nodos. [A] ~253 unidades a escala | Procedimiento |
| 3.4 | Contratos de E1 y E3 que no encajan | [V] `lingob::6.1`; E3 no mira lo que sobra (`prompt_e3.py:83`) | NOTA de E3 |
| 3.5 | Costo y tiempo | [A] USD 40,35 la tanda 0; USD 143 a 192 y 28 h secuenciales para los 147 TOs | — |
| 3.6 | Reproducibilidad | [A] modelo por alias, sin `temperature`; el id de nodo es un hash del texto del modelo, así que re-extraer cambia los ids | Límite; código |
| 3.7 | Mantenimiento | [A] un punto insertado en `pro` invalida 42 de 101 unidades; [V] 969 `remite_a` cruzan de TO y nada avisa si el TO citado cambió | Procedimiento |
| 3.8 | Fallos que frenan la corrida | [V] ids repetidos en `adfsp`, `ceninf`, `cirmo3`, `ri_niif`. [A] un error de E1 cierra la fase | Código |
| 3.9 | Unidades basura y herencia inflada | [V] mini-chunks «n1». [A] `manual::2.1`: 645 caracteres propios, 255.911 con herencia | E0 |
| 3.10 | Roles de TOs ajenos en el grafo | [V] 29 de 35 roles | Código |

## Preguntas de cumplimiento (15)

Las escribí desde los PDF. La búsqueda es una emulación propia de BM25 sobre label, descripción e id; no es el Lucene del agente.

| # | Pregunta | Respuesta del PDF | Resultado |
|---|---|---|---|
| 1 | ¿Cuál es la exigencia básica de capital de un banco? | 5.000 millones (`cap` 1.2) | **Falso**: el grafo dice 2.500 |
| 2 | ¿Cada cuánto se revisa un cliente comercial con 5 % o más de la RPC? | Trimestral (`cla` 6.3.1) | Bien |
| 3 | ¿Qué atraso define «riesgo medio» en consumo? | Más de 90 y hasta 180 días (`cla` 7.2.3) | Bien |
| 4 | ¿En qué plazo se resuelve un reclamo? | 10 días hábiles, con tres salvedades (`pro` 3.1.6) | Bien; la Excepcion no está conectada |
| 5 | ¿Cuál es la multa por un cheque rechazado sin fondos? | 4 %, de $100 a $50.000; 2 % si se cancela en 30 días (`ctacte` 6.5.1) | En parte: cuantías bien; sujeto y relación falsos |
| 6 | ¿Cuándo cesa la inhabilitación por multas impagas? | A los 30 días de cancelar; si no, a los 24 meses (`ctacte` 8.8.1.1) | Bien; sujeto falso |
| 7 | ¿Qué pasa si se falsea la rendición de cuentas? | Art. 41 de la LEF, débito y multa (`pagjub` 2.9.2) | En parte: está, con una prohibición que el texto no dice |
| 8 | ¿Qué documento presenta un extranjero con residencia transitoria nacido en el Mercosur? | Pasaporte o documento de viaje (`docvig` 2.1.1.1) | **No**: el nodo no dice a quién se aplica |
| 9 | ¿Es obligatorio que el Directorio evalúe cada año el código de gobierno societario? | No: es una buena práctica (`lingob` 2.1.1) | **Falso**: Obligacion |
| 10 | ¿En qué moneda se computan los depósitos de la cuenta de regularización que no son en dólares? | En esa moneda (`polcre`, sección 10) | Bien |
| 11 | ¿Qué plazo hay para liquidar divisas de EXPORTA SIMPLE? | 365 días corridos (`ext` 7.1.1.5) | Bien |
| 12 | ¿Cuáles son los límites mínimos de COn1, PNb y RPC? | 4,5 %, 6 % y 8 % de los APR (`cap` 8.5; `ric` 6.3) | **Falso**: cálculo y definición; `ric::6.3` no tiene nodos |
| 13 | ¿Hasta qué monto se agrupan créditos comerciales con los de consumo? | Dos veces el importe de referencia del punto 3.7 (`cla` 3.3.3) | Bien |
| 14 | ¿Qué Comunicación fijó la versión vigente de un punto y desde cuándo rige? | El pie de cada página lo dice | **No**: no está en el grafo |
| 15 | ¿Quiénes son sujetos obligados en protección de usuarios? | Siete clases (`pro` 1.1.2) | Bien |

Bien 8, en parte 2, falso 3, no 2.

## Lo que ordenaría primero

- Del lado del código, antes de re-extraer: 2.1, 2.2, 1.8, 1.9 y 1.10 son reglas chicas con efecto en todo el grafo, y 2.3 pierde texto dentro de la propia tanda 0.
- Del lado del prompt: 1.2, 1.3 y 1.4, que son los que hoy dan respuestas falsas a preguntas centrales.
- Antes de escalar: 1.14, 1.15, 2.4, 2.15 y 2.17 no se ven en la tanda 0, porque 61 de los 147 TOs restantes van por caminos de E0 que la tanda 0 no ejercitó.
- 2.6 y 2.7 se resuelven con datos que E0 ya tiene y no tocan ni el prompt ni el esquema.

Espero el «seguí» para la fase B.
