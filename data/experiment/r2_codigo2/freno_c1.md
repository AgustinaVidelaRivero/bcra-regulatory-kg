# U-R2-CODIGO-2 — FRENO C1: diagnóstico, censos y diseño

Mandato FIRMADO: `docs/mandatos/UR2CODIGO2_correcciones_previas_a_reext.md` (commit de la firma `95dfd98`, sha256
`fda61dca…`, igual al archivo actual). Etapa C1, 03/10/2026.

- **Precondición de C1.** M3 de U-MED-R2A está commiteada en `4244028` (`git log`).
- **Costo.** USD 0: ningún script llama a la API; Neo4j no se usa.
- **Código de la cadena.** No edité nada. Las correcciones candidatas viven en los scripts de esta carpeta y se
  aplican en memoria durante la corrida: reemplazo de funciones de módulos importados, o texto del módulo con
  reemplazos exactos en `c1f_ric44.py`.
- **Dónde corrí.** Todo corrió sobre una copia del repo armada copiando (`rsync -a --copy-links`, 0 enlaces), con la
  versión de HEAD (`95dfd98`) en los 30 archivos que otra sesión tiene modificados sin commit (U-PROMPT-R2). Los
  grafos r2a salieron de HEAD, y ese árbol es el que los reproduce.
- **Qué está en el repo.** Los scripts y sus salidas se copiaron a `data/experiment/r2_codigo2/`. Ninguno corrió
  dentro del repo.

**Controles comunes.** Cada corrida sin cambios reproduce el grafo versionado: KG-Tanda0-Diez-r2a `99fe2bfa…` y
KG-Tanda0-Desarrollo-r2a `93a7af72…` (clave `control_sha` de cada salida). La E0 e0-r2 de la copia reproduce los 47
archivos de `salida_tanda0_r2/` byte a byte.

## Tabla de las seis correcciones y la verificación

| | Archivo que cambiaría en C2 | Qué cambia en los grafos r2a (contrafáctico) | Qué decide la autora |
|---|---|---|---|
| a | `corpus_v2/r1_referencias.py` (rama interna del detector r2) y, si se acepta, `r2_codigo/selftest_r3.py:374` | diez: −11 `remite_a` falsas (patrón 2) y +10 externas a ctacte (patrón 1); 14.000 → 13.999. Desarrollo: −11; 12.833 → 12.822. Nodos y demás aristas, iguales | la regla; si las citas del patrón (2) quedan además en el registro de remisiones; editar el selftest de R3 |
| b | `corpus_v2/runner_corpus.py` (fase E1, solo perfil r2) y `e1_extractor/cliente_e1.py` (namespace y `component`) | ninguno (r2a no se re-extrae); en U-REEXT-T0 un reintento por unidad mal formada | reintento con el mismo request y namespace propio, o con bloque de aviso; tope; reparación determinística sí o no |
| c | `pyd_r2/code/reglas_comparacion.py` | diez: 24 nodos, +23 elementos, 5 modificados, 4 plazos dejan `frecuencia`. Desarrollo: 19, +18, 5, 2 | alcance de los ordinales (todos o solo con marcador); «o más» entre paréntesis y unidad |
| d | `corpus_v2/r1_referencias.py:1198` | ninguna arista. Contador 3.801 → 1.261 (diez) y 2.993 → 1.134 (desarrollo) | si las 7 autorreferencias siguen en el registro; la fe de erratas |
| e | `tanda0/code/ensamblar_tanda0.py:864`, `:868-870` y `:873` | ninguno (sha igual sin la pasada) | si la clave del reporte desaparece o queda marcada como retirada |
| f | `e0_chunking/e0_lib.py` (`parsear_cuerpo`) y `correr_e0.py` (`escalera_e0_r2`), solo e0-r2 | E0 de ric: +`ric::4.4.3` y +`ric::4.4.4` (AL); además 4.4, 4.4.1 y 4.4.2 con la renumeración (ABL). Los 152: sin cambios. Grafos r2a: no cambian (leen la E0 guardada) | AL o ABL; salida nueva de e0-r2 para U-REEXT-T0 y la pareada |
| g | — | — | nada: los veredictos de B02 y B20 se sostienen |

## a. Detector de citas externas, por patrón (`c1a_detector.py` → `salidas/c1a_detector.json`)

**Por qué cada fila es interna.** Las 18 filas «detector» pasan por la rama interna por puntos de
`detectar_menciones_r2` (`r1_referencias.py:735-744`; en el detector de la cadena r1, `:179-187`, el `:185` del
mandato). Ninguna pasa por la rama de sección (`:745-757`; r1 `:188-196`). La causa es `norma_despues` (`:727-733`): en los
90 caracteres que siguen (`VENTANA_DESPUES`, `:50`) no hay `RE_NORMA` (`:63-65`, solo «normas sobre», «T.O. sobre/de»
y «texto ordenado sobre/de») ni anáfora (`RE_ANAFORA_NORMA`, `:482-489`). Lo que sigue en cada fila está en la clave
`filas_m3b_detector`:
- patrón (1), 9 filas: «de la NIIF 9» (B01); «“Deterioro de Valor” de la Norma Internacional de Información
  Financiera (NIIF) 9» (B03); «“Deterioro de Valor” de la NIIF 9» (B04); «de la “Reglamentación de la cuenta
  corriente bancaria”» (B07, B08); «de las normas de “Grandes exposiciones al riesgo de crédito”» (B10, B11, B12);
  «de las normas “Grandes exposiciones…”» (B16);
- patrón (2), 4 filas: «del Anexo de la Comunicación A 7914» (B13, B14, B15, B17);
- patrón (3), 5 filas: no sigue ninguna norma (B19, B21, B22, B29, B30).

**Regla propuesta.** Se aplica en la rama interna por puntos, a una mención sin marca de propio TO, sobre el texto
que sigue (expresiones en `c1a_detector.py`, `RE_PATRON_1` y `RE_PATRON_2`):
- (1) título intermedio opcional entre comillas; luego «de/del» + artículo opcional, y uno de estos:
  - «normas/disposiciones/reglamentación/texto ordenado/T.O.» + «de/sobre» opcional + nombre entre comillas;
  - un nombre entre comillas directamente;
  - «NIIF N», «NIC N» o «Norma Internacional de Información Financiera (NIIF) N».

  La mención pasa a externa a la norma nombrada. El nombre entre comillas se resuelve con la regla (g); NIIF y NIC
  quedan «norma fuera del inventario». Un nombre que empieza como división del documento («Sección…», «Anexo…»,
  «Capítulo…») no es otra norma: la mención sigue interna. Es el caso `ri_dcpc::7.2` de la partición.
- (2) «del/de la Anexo [romano] de la Comunicación [“]A[”] NNNN»: la mención deja de ser interna. Queda irresoluble,
  con causa «punto del Anexo de una Comunicación», sin arista, y la cita (Comunicación y punto) entra al registro de
  Comunicaciones.
- (3) sin cambio (decisión 7).

**Las 18 filas con la regla.**
- Patrón (1):
  - las 9 dejan de ser internas;
  - el caso NIIF 9 (B01, B03, B04) no resuelve a `cap::5.5`: queda «norma fuera del inventario»;
  - B07 y B08 nombran un TO del corpus y se resuelven como externas a `ctacte::9.2.1.1` y `ctacte::9.2.2.1`
    (+10 aristas en diez);
  - B10, B11, B12 y B16 quedan «norma fuera del inventario».
- Patrón (2): las 4 pasan a la causa nueva.
- Patrón (3): las 5 siguen «punto inexistente en E0».

**Censo pedido: `remite_a` internas falsas del patrón (1) cuando el número existe en el TO de origen: 0 en los dos
grafos.** El patrón (1) tiene 7 entradas en el registro de remisiones de diez (las 9 filas de M3.b, contadas por
unidad citada) y 6 en el de desarrollo. Todas son irresolubles: el número no existe en el TO de origen.

**Contradicción con el mandato, reportada:** el mandato da por hecho que el patrón (1) crea relaciones falsas cuando
el número existe. En los grafos r2a no pasa; donde pasa es en el patrón (2):
- la cita de `ext::10.4.4` «receptadas en el punto 10.3.6. del Anexo de la Comunicación A 7914» resuelve a
  `ext::10.3.6`, que existe en ext, y crea **11 `remite_a` falsas** en cada grafo (lista completa en
  `detalle.aristas_quitadas`);
- otras 4 citas del mismo patrón resuelven a puntos de ext que existen pero no tienen nodos (`punto_sin_nodos`: 3.17,
  tres veces, y 10.7), y 1 es autorreferencia (`ext::10.3.6`).

En total, el patrón (2) tiene 10 entradas en el registro, todas de ext; 4 de ellas son las de M3.b.

**Efecto de la regla en los registros.** Citas resueltas: diez 1.547 → 1.548, desarrollo 1.382 → 1.381.
Irresolubles: diez 510 → 508, desarrollo 425 → 425. Por causa (diez): «punto inexistente en E0» 30 → 17 (las 13 de
los patrones 1 y 2), «norma fuera del inventario» 189 → 195, «punto_sin_nodos» 205 → 201, autorreferencia 30 → 29, y
la causa nueva, 10.

**Partición, informativo** (152 TOs, texto propio de la E0 legada de la partición, `b584_particion`): 19 menciones
del patrón (1) y 1 del (2), en 17 chunks.
- NIIF 9 aparece 11 veces.
- Resuelven a un TO: dos «Protección de los usuarios…» (pro), «Lineamientos para el gobierno societario…» (lingob) y
  la «Reglamentación…» de docvig (ctacte).
- «Protección de usuarios…», sin «los», y «Sistema Nacional de Pagos – Servicios de pago» quedan sin TO.
- El falso positivo «de la “Sección 3 – Criterio generales”» (`ri_dcpc::7.2`) quedó excluido por la guarda.

## b. Reintento ante una salida de E1 mal formada (`c1b_reintento.py` → `salidas/c1b_reintento.json`)

**Las unidades.** En los diez TOs, 4 de 2.434 unidades de E1 se rechazan a nivel de chunk, todas con
`entities_o_relations_invalidos`. Son las 4 del mandato. Las 3 de desarrollo son las mismas `cap::5.3.2.3`,
`ext::6.5.3` y `ric::6.3`: los dos grafos leen el mismo crudo (`corpus_tanda0/salida_dirigida`). En las cuatro,
`stop_reason` es `tool_use`, sin error de llamada, y la salida está por debajo del techo de 8.192.

| Unidad | Qué trae el crudo | Tokens de salida |
|---|---|--:|
| `cap::5.3.2.3` | `entities` es una lista de 35 entidades válidas; falta `relations` | 5.398 |
| `ext::6.5.3` | `entities` es texto con el resto del objeto serializado («[…],\n"relations": […],\n"omisiones_no_prosa": []\n}»); `json.loads` falla con «Extra data» en 927 | 404 |
| `ric::6.3` | igual que la anterior, «Extra data» en 1.349 | 1.119 |
| `ctacte::5.6.1` | `entities` es texto con comillas sin escapar dentro de un `label` («Expresión "por aval" en…»): «Expecting ',' delimiter» en 318; `relations` es una lista | 1.856 |

**Dónde los rechaza la cadena.**
- `validador_e1.validar_salida`: en HEAD, `validador_e1.py:146-152`. El `:232` del mandato es la línea en la versión
  sin commit de U-PROMPT-R2 (`:228-234`); reporto la diferencia.
- `validador_r2.validar`: `validador_r2.py:484-489`, con el mismo motivo.

**Por qué hoy no se reintenta.** `fase_e1` marca error solo ante una falla de la API, un corte que persiste tras el
reintento o la falta de `tool_use` (`runner_corpus.py:540-569`). Una salida con `tool_use` mal formada queda con
`error = None`, por lo que:
- cuenta como hecha y no se re-llama al reanudar (`:520`);
- no llega a E3 (`comun_e3.chunk_aceptado`, `comun_e3.py:75-80`);
- queda como «rechazado_en_e1» en la entrada r2 (`runner_corpus.py:940-942`).

**Diseño propuesto, solo con el perfil r2** (`PERFIL_R2`: `--perfil-r2` o un perfil de forma «r2», como el r2b de
U-PROMPT-R2).
- **Cuándo dispara.** Después del reintento por corte, si la respuesta efectiva tiene `tool_use`, su `stop_reason` no
  es `max_tokens` y la validación de E1 rechaza el chunk con un motivo de forma: `salida_no_parseable`,
  `salida_no_dict` o `entities_o_relations_invalidos`.
- **Tope.** Un reintento por unidad, sin tercera llamada, como el reintento por corte (`cliente_e1.py:289-313`).
- **Request.** El mismo, byte a byte: el que produjo la salida mal formada, con el techo de corte si lo hubo.
- **Namespace y clave.**
  - El namespace es propio: `e1_extraccion|cv=e1-extractor-v1-p<hash del prefijo del perfil>-rforma1|think=0`.
    Va en la misma db, `e1_extractor/cache/e1_extraccion.db`.
  - La clave es sha256(namespace + «\n» + request canónico), `llm_cache.py:120-126`. Con el mismo namespace la
    caché devolvería la misma salida mal formada.
  - En las 4 unidades, verificado con la db abierta en modo inmutable: la clave de la primera pasada está en la db
    con el mismo crudo; la del reintento es otra y no está.
- **Decisiones de caching.**
  - D1: el prefijo y su breakpoint no cambian.
  - D2: el costo sale de la fórmula de `ClienteE1Real`.
  - D3: un `component` propio en el log, `reextraccion_v2_e1_reintento_forma`; hoy está fijo en
    `cliente_e1.py:189`.
  - D4: el reintento corre en el mismo bucle secuencial.
  - D5 no aplica.
- **Persistencia.** En `extracciones_e1.jsonl`:
  - `tool_input_crudo` es el del reintento, y es lo que leen E3 y la entrada r2;
  - el registro suma `reintento_forma` = {namespace, motivo, `intento_1` con `resumen_intento` de la respuesta mal
    formada}, como `reintento_corte` (`runner_corpus.py:574-580`);
  - el crudo completo de los dos intentos queda en la db.
- **Tope agotado.** `error = "salida_mal_formada_tras_reintento"`. La unidad entra en `errores_definitivos` de
  `resumen_e1.json` (`:628-654`, la lista declarada) y en `reintentos_forma`; no llega a E3.
- **Perfiles existentes.** Sin reintento, y requests byte a byte iguales: la rama está detrás de `PERFIL_R2`.
- **Costo estimado.** Una llamada de E1 por unidad mal formada. En la tanda 0 fueron 4 de 2.434.

**Alternativa para la autora.** Un bloque de aviso agregado al mensaje del reintento, como el feedback del ratchet
(`ratchet_e3.py:251`). Cambia el request por sí mismo y no necesita namespace propio, pero agrega texto de prompt
(decisión 2 del mandato: eso es de U-PROMPT-R2). Recomiendo la primera opción.

**Reparación determinística.** Es una opción, no adoptada. Se valida con los dos validadores (clave
`validacion_con_la_reparacion`):
- `ext::6.5.3` y `ric::6.3`: `{"entities": ` + el texto reconstruye el objeto sin agregar contenido. Pasan con 2
  entidades y 1 relación, y con 4 entidades y 6 relaciones, sin rechazos.
- `cap::5.3.2.3`: relaciones vacías. Pasa con 35 entidades y 0 relaciones: pierde las relaciones, que el modelo no
  emitió.
- `ctacte::5.6.1`: no admite reparación sin adivinar qué comillas son contenido.

## c. Cuantías (`c1c_cuantias.py` → `salidas/c1c_cuantias.json`)

**Qué no reconoce `detectar_cuantias`.** El patrón de plazo (`reglas_comparacion.py:115-117`) exige una cifra o un
cardinal en letras seguido de día/mes/año/hora/semana. Por eso no reconoce:
- «hs.»;
- el ordinal («quinto día hábil»);
- «hábil» o «corrido» en singular, después de una cuantía («un día hábil»: la cuantía se detecta sin `dias_tipo`);
- «180 (ciento ochenta) o más días corridos», con «o más» entre el paréntesis y la unidad.

**Búsqueda en el texto propio de e0-r2 de los diez TOs** (2.434 chunks, 996 cuantías detectadas hoy). Lo que sigue
sin cuantía son sobre todo posiciones sin número («último día del mes», 38 en tres formas) y celdas de tabla.
Formas a corregir:

| Extensión | Qué detecta | Cuantías nuevas en el texto |
|---|---|--:|
| h | «hs.», «hrs.»: horas (fuera de lista, como «horas») | 1 (`ctacte::7.3.1.5`) |
| o | ordinal + día/mes/año/semana, con «hábil/corrido» en singular o plural | 26 |
| s | «hábil/corrido» en singular tras una cuantía de días | 2 con `dias_tipo` fijado |
| m | «N (letras) o más/menos <unidad>» | 1 (`ext::3.18.3.3`) |

**Los dos casos del mandato.** «24 hs. hábiles» → 24 horas; «hasta el quinto día hábil…» → 5 días hábiles,
`maximo_inclusivo` por «hasta». Hoy no detecta ninguno de los dos.

**Contrafáctico con h, o y s sobre los grafos r2a.**

| | Nodos que cambian | Elementos nuevos (h / o) | … sin marcador (comparación asumida) | Modificados (s / arrastre de o) | Dejan `frecuencia` |
|---|--:|--:|--:|--:|--:|
| diez | 24 | 23 (1 / 22) | 19 | 5 (3 / 2) | 4 |
| desarrollo | 19 | 18 (0 / 18) | 16 | 5 (3 / 2) | 2 |

- **Plazos que dejan de ir a `frecuencia`.** En diez: `cap::7.3.2` y `cap::2.1` («tercer mes siguiente…»),
  `ctacte::7.3.1.5` («24 hs. hábiles») y `pagjub::2.5.2` («hasta el quinto día hábil… de cada período de pago»). El
  contador pasa de 250 a 246 y el de fuera de lista, de 213 a 209.
- **El caso de `pagjub::2.5.2`.** M3.d lo leyó como frecuencia mixta: al pasar a umbral pierde la periodicidad, porque
  el código manda el plazo heredado a un lado o al otro (`ensamblar_tanda0.py:707-718`).
- **Efectos a decidir.**
  - 19 de los 22 ordinales nuevos de diez no tienen marcador y reciben `maximo_inclusivo` asumido por la regla del
    plazo. Varios marcan un comienzo («a partir del octavo mes», «desde el trigésimo séptimo mes»).
  - En `cap::6.11` el ordinal «segundo mes» corta la base de un «25 %» («RPC registrada al último día del segundo mes
    anterior» → «RPC registrada al último día del»).
- **Opciones para la autora.** «o» amplio (lo medido) u «o» solo con un marcador compuesto antes («hasta el…»,
  «dentro del…»).
  - De los 22 ordinales de diez, 2 tienen «hasta» antes: `cap::7.4`, «hasta el trigésimo sexto mes», y
    `pagjub::2.5.2`. Un tercero, `cap::4.1.2`, recibe «coeficiente» por un ponderador cercano.
  - Con el restringido entrarían esos 2, y los dos «tercer mes» seguirían en `frecuencia`.
- **Selftest.** `selftest_pyd_r2.py` llama a `RC.analizar` sobre datos reales (`:516-542`, `:722`). C2 lo corre con
  los casos nuevos; el archivo tiene cambios sin commit de U-PROMPT-R2.

## d. Contador de menciones en texto heredado (`c1d_menciones.py` → `salidas/c1d_menciones.json` y `salidas/c1d_menciones_26d274d.json`)

**Definición del contador nuevo.**
- Autocita de encabezado: la mención de la regla (i) sin puntos, con secciones = [N], unidad heredada S<N> y
  evidencia que empieza con «Sección N». Es la definición de M3.
- `texto_heredado.menciones` pasa a contar las menciones sin esas autocitas, y una clave nueva,
  `texto_heredado.autocitas_de_encabezado`, cuenta las otras.
- Ninguna arista cambia: las autocitas no crean `remite_a`. Las 7 que llegan al registro son irresolubles por
  «autorreferencia al punto propio».

| Medición | Menciones hoy | Autocitas | Contador nuevo |
|---|--:|--:|--:|
| KG-Tanda0-Diez-r2a (reporte del ensamblado) | 3.801 | 2.540 | 1.261 |
| KG-Tanda0-Desarrollo-r2a | 2.993 | 1.859 | 1.134 |
| r3d, desarrollo (HEAD, `r3d_remisiones.json`) | 2.858 | 1.791 | 1.067 |
| r3d, diez (HEAD) | 3.655 | 2.461 | 1.194 |
| r3d, KG-Reextraído-r1 (HEAD) | 2.838 | 1.777 | 1.061 |
| **r3d, desarrollo, con `r1_referencias.py` de `26d274d` (la cifra 2.870)** | **2.870** | **1.791** | **1.079** |

**La cifra de 2.870 está inflada: VERIFICADO.** Reproduje el total exacto con el módulo de `26d274d` (`git show
26d274d:…/r1_referencias.py`, sha256 `886f4382…`): 1.791 de las 2.870 son autocitas de encabezado.

**Documentos y artefactos que citan las cifras viejas.**
- **Prosa:**
  - `data/experiment/r2_codigo/reglas_remisiones_postR3.md:102` («De 2.870 menciones en texto heredado…»);
  - `reports/u_diag_proceso/anexo_evidencia_u_diag_proceso.md:113` (2.870, «NO VERIFICADO, no lo medí»);
  - `data/experiment/medicion_r2a/m3_freno.md:238`, `:244-:248` (3.801, 2.993 y 2.870 «probablemente… NO
    VERIFICADO»);
  - `docs/plan_tesis.md:400` y `docs/mandatos/UR2CODIGO2_correcciones_previas_a_reext.md:19` y `:128` (dicen bien
    que 2.540 de 3.801 son autocitas; mandato firmado, no se edita).
- **Artefactos:**
  - `corpus_tanda0/ens_diez_r2a/r2/reporte_ensamblado_r2.json:935` (3.801);
  - `corpus_tanda0/ens_desarrollo_r2a/r2/reporte_ensamblado_r2.json:647` (2.993);
  - `data/experiment/r2_codigo/r3d_remisiones.json:217`, `:1661`, `:4422`, `:6243` y `:6630` (2.858, 3.655 y
    2.838);
  - `data/experiment/medicion_r2a/m3/m3_cadena_instrumentada.json:7-8` y `:184-185`, donde la cifra es la medida
    correcta del contador.

La unidad no edita ninguno.

**Texto propuesto para la fe de erratas** (nota fechada al pie de `reglas_remisiones_postR3.md`; la misma
corrección vale para el anexo de U-DIAG-PROCESO, §5):
> «Fe de erratas (fecha). Las 2.870 menciones en texto heredado de la regla (i) (`:102`, medición de `r3d_remisiones.py`
> en `26d274d`, KG-Tanda0-Desarrollo-r1 con el texto de e0-r2) incluyen 1.791 que son la línea «Sección N.» del
> encabezado heredado, leída como cita de su propia sección; ninguna crea arista. Sin ellas son 1.079. Reproducción:
> `data/experiment/r2_codigo2/c1d_menciones.py --r1-referencias` con el módulo de `26d274d` (U-R2-CODIGO-2, C1.d).
> Con el código vigente, la misma medición da 2.858, de las cuales 1.791 son autocitas (`r3d_remisiones.json`).»

## e. Pasada residual de E4 (`c1e_pasada_residual.py` → `salidas/c1e_pasada_residual.json`)

**Qué la compone en el perfil r2** (`ensamblar_tanda0.py`):
- `:864`: `E4.resolver_propuestos(deepcopy(kg), catalogo)`, sobre una copia del grafo;
- `:868-870`: la clave `e4.pasada_residual_de_propuestos_medida_no_aplicada` del reporte;
- `:873`: el archivo `e4_pasada_residual_medida.json`;
- el docstring de la cadena (`:571`).

El catálogo de `:863` lo usa el esqueleto (`:875`) y queda.

**Lo que mide hoy.** Diez: 24 propuestos y 0 resoluciones. Desarrollo: 15 propuestos y 0 resoluciones. Motivo
único: «sin match en catálogo».

**Contrafáctico.** Con la pasada reemplazada por una vacía, el grafo es el versionado byte a byte en los dos casos.

**Lectores.**
- `medicion_r2a/m3_planillas.py:193` lee el archivo de `ens_diez_r2a`, que queda versionado.
- `medicion_r2a/m2_medicion.py:294` lee la clave del reporte: fallaría sobre un reporte nuevo si U-REEXT-T0 lo
  reutiliza para la columna r2b del tablero.
- La suite y las shapes no la leen (búsqueda en `scripts/` y `data/experiment/`).

## f. El bloque 4.4 de ric en E0 (`c1f_ric44.py` → `salidas/c1f_*.json`)

**Diagnóstico** (`e0_lib.extraer_lineas`, solo lectura; imagen de la p. 16 revisada).
- **Primera causa, encabezados de la p. 16.** El PDF de ric imprime «4.3. Información complementaria vinculada al
  cálculo de la exigencia por riesgo de / mercado - Modelos de información», «4.3.1. Riesgo específico de tasa» y
  «4.3.2. Riesgo general de tasa» en la p. 16 (versión 3a, Com. «A» 6333). E0 rechaza los tres como duplicados
  (`no_sucede_al_hermano_3`, `e0_lib.py:933-934`; `estructura_ric.json`, `rechazos_header`).
- **Segunda causa, encabezados de la p. 18.** En la p. 18 (versión 2a, Com. «A» 6070), «4.4.3. Riesgo de cambio» y
  «4.4.4. Riesgo de posiciones en opciones» quedan rechazados por `padre_4.4_no_abierto` (`:922-923`).
- **Resultado.** Las páginas 16 a 18 caen en `ric::4.3.3`, en la E0 legada y en e0-r2.
- **Corrección al mandato.** El mandato dice que 4.4, 4.4.1 y 4.4.2 «ni siquiera aparecen en el texto extraído». Su
  texto sí está extraído, con los números que imprime el PDF:
  - los códigos 551100 a 551700 del «modelo inserto en el punto 4.4.1» están bajo «4.3.1»;
  - los «códigos previstos en el punto 4.4.2. a)» y el «Cuadro inserto en el punto 4.4.2. b)» están bajo «4.3.2»
    (p. 16 y 17).
- **Lo que esto aporta a M3.b.** Las 5 filas «no decidible» (B18, B23, B24, B25 y B28) se pueden decidir: la causa es
  la numeración duplicada del PDF, que imprime el bloque 4.4 como 4.3. Cambiar el veredicto es decisión de la autora.

**Corrección propuesta, dentro de e0-r2.** Un parámetro nuevo de `parsear_cuerpo`, que solo pasa `escalera_e0_r2`
(`correr_e0.py:973-976`). La E0 legada no cambia. Medí cuatro variantes, armadas en memoria con reemplazos exactos del
texto de los dos módulos (`c1f_ric44.py`):
- **A, padre sintético general.** Un encabezado de profundidad ≥ 3 con forma de título, cuyo padre no está abierto,
  abre el padre como nodo sintético (sin línea de rótulo y con título vacío), con el aviso `padre_sintetico`.
  Condiciones: el abuelo está abierto y el número del padre sucede al último hijo del abuelo.
- **AL, recomendada.** A acotada por una lista en código de (TO, padre): solo («ric», «4.4»). Es el mismo recurso que
  la lista de tablas de `cap::6.2.2.6` en U-PROMPT-R2.
- **AB y ABL.** A o AL, más una lista en código con las tres renumeraciones de la p. 16 (4.3 → 4.4, 4.3.1 → 4.4.1,
  4.3.2 → 4.4.2), con el aviso `renumerado_por_lista`. Corrigen la numeración de la norma por inferencia, a partir de
  las 5 citas y de los encabezados 4.4.3 y 4.4.4.

| E0 de la tanda 0 (diez TOs) | ids nuevos | cambia el texto | otros TOs |
|---|---|---|---|
| A y AL | `ric::4.4.3` (p. 18, 1.295 caracteres, tabla009) y `ric::4.4.4` (p. 18, 399, tabla010) | `ric::4.3.3`: de p. 15–18 y 7.651 caracteres a p. 15–17 y 5.955 | sin cambios (9 de 9) |
| AB y ABL | además `ric::4.4::intro`, `ric::4.4.1` (p. 16) y `ric::4.4.2` (p. 16–17) | `ric::4.3.3`: p. 15, 806 caracteres | sin cambios |

**Censo en los 152 TOs de la partición** (árbol de E0 de la escalera de e0-r2; `c1f_parsear_152_*.json`):
- **Variante A.** Cambia la estructura de 4 TOs: cirmo3, ri_cc, snp_cheq y venliq. Con e0-r2 completa sobre esos
  cuatro (`c1f_comparar_4tos_A.json`):
  - **cirmo3, regresión grave.** «1.7.13 Violeta» (p. 9) es una línea dentro del 1.2.11.1 («… color predominante»,
    x0 205,2), no un encabezado de punto. Con A abre un 1.7 sintético, cierra el 1.2 y hace desaparecer 49 ids (de
    `cirmo3::1.2.11.2` a `cirmo3::1.3.1`).
  - **ri_cc.** Recupera `ri_cc::1.8.1`: el PDF trae «1.8. MODELO DE INFORMACIÓN» (p. 53) y E0 lo pierde.
  - **snp_cheq.** Suma `snp_cheq::3.3.6.2`: ninguna línea extraída de las p. 37 y 38 empieza con «3.3.6.».
  - **venliq.** Suma `venliq::1.2.2` y cambia el bloque de la Sección 1 y la herencia de 11 chunks.
  - Los rechazos `padre_…_no_abierto` pasan de 307 a 352.
- **AL y ABL.** No cambian ningún id de los 152: actúan solo sobre ric, que no está en la partición (por la lista, y
  verificado en el árbol de los 152 con AL).

Recomiendo AL. A queda descartada por cirmo3; lo de ri_cc, snp_cheq y venliq es hallazgo informativo de la partición.

Esto importa para U-SEG-OFICIAL, cuyo borrador (sin firma, `docs/mandatos/USEG_OFICIAL_segmentacion_e0r2.md`)
espera el cierre de esta unidad para correr e0-r2 sobre los 152. Con AL, los 152 quedan como con el código de hoy.

Límites que se declaran:
- **En AL:** la herencia de 4.4.3 y 4.4.4 lleva el encabezado «4.4.», sin título, porque el PDF no lo trae; y el
  contenido de 4.4, 4.4.1 y 4.4.2 queda en `ric::4.3.3`, con su causa (la numeración duplicada del PDF).
- **En ABL:**
  - `ric::4.4::intro` es solo la cola del título («mercado - Modelos de información»);
  - el texto de 4.4.1 y 4.4.2 conserva los números impresos (4.3.1 y 4.3.2);
  - la herencia lleva «4.4. Información complementaria…», un número que el PDF no imprime.

**Versión de E0 y clave de caché.**
- **Va dentro de e0-r2.** El mandato la ubica ahí, y la E0 legada no cambia. Lo que se pierde: el código de e0-r2
  deja de reproducir `salida_tanda0_r2/` (`f8dedd4`) en ric. Los grafos r2a siguen reproducibles, porque el ensamblado
  lee la E0 guardada.
- **Salida nueva para U-REEXT-T0.** Hace falta una salida nueva de e0-r2: un directorio nuevo o el re-sello de la
  autora. El manifiesto r2b de U-PROMPT-R2, sin commit, apunta hoy a `salida_tanda0_r2`. La pareada de U-PROMPT-R2 y
  U-REEXT-T0 tienen que usar la misma.
- **Clave de caché.** La versión de E0 no entra al request de E1 ni al de E3. Cambian solo las claves de:
  - `ric::4.3.3`, porque cambia su texto propio (fila F01 de `mantenimiento/tabla_reprocesamiento.md`);
  - las unidades nuevas: 2 en AL y 5 en ABL (como F17/F19, sin clave previa).

  Con el prefijo r2b, U-REEXT-T0 paga igual todas las unidades. El costo extra son 2 (o 5) unidades de E1 y E3.

## g. Dos lecturas de M3.b (`c1g_lecturas.py` → `salidas/c1g_lecturas.json`)

- **B02, cap 3.6: no existe en el PDF.**
  - El índice (p. 2) lista en la Sección 3 solo «3.1. Tratamiento de las titulizaciones.» y «3.2. Tratamiento de las
    posiciones en fondos.», y el cuerpo los trae en las p. 29 y 58.
  - La única línea del PDF que nombra «3.6» es la cita misma, en la p. 104 (cuerpo, versión 13a, Com. «A» 8109):
    «…así como las retitulizaciones, las / que recibirán el tratamiento del punto 3.6.».
  - El veredicto «normativa» se sostiene.
- **B20, ric 12.1.2: el párrafo no nombra otra norma antes de la cita.**
  - Texto, en la p. 57 (versión 14a, Com. «A» 6561): «12.1.2. La partida 39000000 -a enviarse por única vez junto con
    las informaciones del período julio 2015- deberá informarse por todas las entidades que cumplan los requisitos
    previstos en el punto 5.1.2.1., independientemente de su calificación.»
  - Lo único nombrado cerca es la Comunicación «A» 5831, en el 12.1.1.
  - En todo el PDF, «5.1.2» aparece solo como encabezado sin subpuntos («5.1.2. Exigencia por riesgo operacional para
    entidades del Grupo 2», p. 22) y en esa cita.
  - El veredicto «normativa» se sostiene.

## Contradicciones con el mandato y hallazgos fuera de lo pedido

- **Censo de (a).** El mandato espera `remite_a` internas falsas del patrón (1): en r2a son 0. Las que existen son
  11, del patrón (2), en cada grafo.
- **Líneas citadas.**
  - `r1_referencias.py:185` y `:194` son del detector de la cadena r1; el del perfil r2 tiene la misma rama en
    `:735-757`.
  - `validador_e1.py:232` es la línea de la versión sin commit de U-PROMPT-R2; en HEAD, `:146-152`.
- **Las 3 unidades de desarrollo.** Son las mismas respuestas de E1 que 3 de las 4 de diez: los dos grafos leen el
  mismo crudo.
- **El bloque 4.4.** «4.4, 4.4.1 y 4.4.2 ni siquiera aparecen en el texto extraído»: aparecen, con la numeración
  que imprime el PDF (4.3, 4.3.1 y 4.3.2, p. 16).
- **Hallazgo de la partición.** E0 pierde «1.8. MODELO DE INFORMACIÓN» de ri_cc (p. 53). En snp_cheq (p. 38) y venliq
  (p. 4) hay encabezados sin padre. Es informativo para U-SEG-OFICIAL.

## Comandos

Desde la raíz de una copia del repo (regla l), con `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B`:

```
data/experiment/r2_codigo2/c1a_detector.py --out data/experiment/r2_codigo2/salidas/c1a_detector.json
data/experiment/r2_codigo2/c1b_reintento.py --out data/experiment/r2_codigo2/salidas/c1b_reintento.json
data/experiment/r2_codigo2/c1c_cuantias.py --out data/experiment/r2_codigo2/salidas/c1c_cuantias.json
data/experiment/r2_codigo2/c1d_menciones.py --out data/experiment/r2_codigo2/salidas/c1d_menciones.json
data/experiment/r2_codigo2/c1d_menciones.py --r1-referencias <archivo de git show 26d274d:data/experiment/reextraccion_v2/corpus_v2/r1_referencias.py> --out data/experiment/r2_codigo2/salidas/c1d_menciones_26d274d.json
data/experiment/r2_codigo2/c1e_pasada_residual.py --out data/experiment/r2_codigo2/salidas/c1e_pasada_residual.json
data/experiment/r2_codigo2/c1g_lecturas.py --out data/experiment/r2_codigo2/salidas/c1g_lecturas.json
data/experiment/r2_codigo2/c1f_ric44.py --correr-manifiesto data/experiment/reextraccion_v2/manifiestos/tanda0_10tos.json --variante <base|A|AB|AL|ABL> --salida <dir fuera del repo>
data/experiment/r2_codigo2/c1f_ric44.py --comparar --base <dir base> --variante-dir <dir variante> --out data/experiment/r2_codigo2/salidas/c1f_comparar_diez_<variante>.json
data/experiment/r2_codigo2/c1f_ric44.py --correr-tos cirmo3,ri_cc,snp_cheq,venliq --variante <base|A> --salida <dir fuera del repo>
data/experiment/r2_codigo2/c1f_ric44.py --parsear-152 --variante <base|A|AL> --out data/experiment/r2_codigo2/salidas/c1f_parsear_152_<variante>.json
```

## Lo que decide la autora para C2

1. (a): la regla de los patrones (1) y (2); si las citas del patrón (2) quedan también como irresolubles en el
   registro de remisiones; y si C2 puede editar `r2_codigo/selftest_r3.py`, que fija las reglas del detector en
   `:374`.
2. (b): reintento con request idéntico y namespace propio (recomendado) o con bloque de aviso; tope 1; reparación
   determinística sí o no.
3. (c): extensiones h y s; «o» amplio o restringido a marcador; «m» sí o no.
4. (d): si las 7 autorreferencias de encabezado siguen en el registro de remisiones; la fe de erratas, que es de la
   autora.
5. (e): si la clave del reporte se borra o queda marcada como retirada (lector: `m2_medicion.py:294`).
6. (f): variante AL o ABL (la A general queda descartada por cirmo3); dónde queda la salida de e0-r2 que
   usarán la pareada y U-REEXT-T0.
7. Revisar los veredictos de B18, B23, B24, B25 y B28 de M3.b con el hallazgo de (f).

## Control del repo y escrito

- **Escrito en el repo.** Solo `data/experiment/r2_codigo2/`: 24 archivos nuevos (8 scripts, este documento y 15
  salidas), 0 enlaces y ninguno ignorado por `.gitignore` (`git check-ignore`). El sha256 de cada uno está en el
  paquete de revisión.
- **Regla l.** Tomé el sha256 de todos los archivos del repo, salvo `.git` y `.venv` (21.442 al inicio), al empezar,
  antes de copiar y después de copiar. Lo único mío son los 24 archivos de `r2_codigo2/`. Durante la etapa, otras
  sesiones cambiaron 14 rutas que no toqué:
  - `docs/plan_tesis.md`, `docs/checklist_pre_escalado.md` y `docs/insumos_escritura.md`;
  - cuatro mandatos nuevos en `docs/mandatos/`;
  - la figura del extractor en `docs/tesis/figuras/` (5 archivos);
  - `reports/u_revision_libre/` (2).
- **`.pyc`.** La línea de base del inicio (11.236 entradas) es igual a la del cierre.
- **Doble corrida, byte a byte igual.**
  - Las salidas de c1a, c1b, c1c, c1d (las dos), c1e y c1g, y las cinco comparaciones de c1f.
  - La E0 de las variantes AL y ABL (47 de 47 archivos, en dos directorios) y la de A, AB y los cuatro TOs de la
    partición, repetidas con la versión final del script (47, 47 y 24 de 24).
  - Los árboles de los 152, base y A, repetidos con la versión final del script; el de AL es idéntico al de base.
- **Error propio, con su causa.** La primera doble corrida de c1a dio distinto: había corrido la salida antes de
  agregar la guarda «Sección…» y los 157 títulos de la partición. La rehíce con el código final y da igual.
- **Grep de convenciones** sobre `data/experiment/r2_codigo2/`, corrido antes de escribir esta sección (después,
  las únicas coincidencias de los dos primeros son sus propias líneas de descripción, abajo):
  - nombres propios conocidos del proyecto, «mentor», «tutor», «profesor», «reunión», «slack», «mail», «correo» y
    «whatsapp» (los nombres no se transcriben): vacío (exit 1);
  - primera persona del plural («nosotros», «hicimos», «tenemos», «nuestro/a», «decidimos», «corrimos», «vamos a»,
    «encontramos», «medimos», «proponemos»): vacío (exit 1);
  - origen conversacional («como dijo», «según dijo/pidió», «pedido por», «me/nos pidió»): vacío (exit 1).
- **Commit.** PENDIENTE de la autora.
