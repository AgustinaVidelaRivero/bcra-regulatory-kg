# U-R2-CODIGO — FRENO R5 (final), con los ajustes A a H

USD 0, sin API ni Neo4j. Batería final `control_r5.sh` y su continuación `control_r5_parte2.sh` (paquete de revisión;
la primera parte se cortó por el límite de tiempo de la ejecución en segundo plano y la continuación siguió desde la
etapa de pies con las mismas copias). Regla l de CLAUDE.md §4 (`79a493c`): todo corre sobre copias armadas con
`rsync --copy-links` (0 enlaces en las cuatro copias: actual, HEAD, regla (g) anterior a R4 y ajuste propuesto de K) y
la batería toma el sha256 de todos los archivos del repo (salvo `.git`) antes y después.

Control del repo. Entre el inicio y el fin de la batería cambiaron solo cinco archivos, todos nuevos y ajenos a esta
unidad: `docs/tesis/figuras/{figura_ficha.pdf,figura_ficha.png,figura_ficha.svg,LEEME_figura_ficha.md,generar_figura_ficha.py}`,
creados entre las 18:11 y las 18:15 del 02/10/2026 por otra sesión de trabajo (`ls -la` en el paquete). La batería
escribe solo en el scratchpad. Sin `.pyc` nuevos (286 entradas antes y después).

Rutas en los reportes. Con copias reales, los reportes del ensamblado registran la ruta absoluta de la copia y de la
salida. En R4, el espejo enlazado resolvía esas rutas al repo y los reportes coincidían byte a byte. Ahora comparo los
reportes con la ruta de la copia reemplazada por la del repo (`comparar_rutas.py`): todos iguales.

## A — evidencia dentro de un solo tramo

`r1_referencias.menciones_por_tramo` lee cada tramo por separado (texto propio del chunk o un tramo heredado) y la
evidencia sale del original de ese tramo; las normas nombradas en tramos anteriores del punto siguen como antecedentes
de la anáfora. Control (`r3d_remisiones.py`, `en_el_texto`, cada tramo por separado):
- desarrollo: 12.547 aristas, 0 con evidencia fuera de un único tramo; 0 evidencias no literales;
- diez: 13.709 aristas, 0 y 0.
Sobre las pruebas r2, la shape S31 da 0 violaciones: 12.833 de 12.833 aristas `remite_a` en desarrollo, 14.000 de
14.000 en diez y 179 de 179 en cla, todas con la evidencia en un tramo del chunk de la arista.

## B — regla (g) en tres pasos

Orden: igualdad con un título; título prefijo del texto capturado (gana el más largo); texto capturado de dos o más
palabras como comienzo de un único título. Títulos: inventario más `nombres_remision` del manifiesto. La captura entre
comillas llega a la comilla de cierre y la sin comillas toma hasta 400 caracteres: un punto dentro del título ya no la
corta.

Controles (`r5_comparar_g.py`, tablas con el código de cada versión en su copia):
- `pagjub::2.2` resuelve a pagjub por igualdad en diez, con el `nombres_remision` del manifiesto. En la partición, que
  usa solo el inventario, no resuelve: el título del inventario está abreviado («seg. soc.», «Adm.»).
- «Incumplimientos de capitales mínimos…» no resuelve a cap en ningún caso: en la partición, 8 menciones van a incuca
  (6 por igualdad, 1 por prefijo, 1 por comienzo) y 2 quedan irresolubles.
- Las 41 citas de la partición que la (g) de R4 dejó irresolubles (recomputadas: 41 de resuelta a irresoluble y 43 de
  irresoluble a resuelta entre la (g) anterior y la de R4; el freno de R4 decía 45 en el segundo sentido, con otra clave
  de mención): con la (g) actual, 35 vuelven a resolver, todas al mismo TO que antes (15 por igualdad, 8 por prefijo,
  12 por comienzo), y 6 siguen irresolubles (lista en `comparacion_g_anterior_R4_actual_B_R5.json`).
- Cambios de la (g) de R4 a la actual: desarrollo, ninguno entre las menciones comunes; diez, 1 de irresoluble a
  resuelta (`pagjub::2.2`, igualdad); partición, 61 de irresoluble a resuelta (34 por igualdad, 13 por prefijo, 12 por
  comienzo y 2 sin vía de (g): dos anáforas «dicho ordenamiento» cuya norma antecedente ahora resuelve); 0 de resuelta a
  irresoluble y 0 con otro TO. Las menciones que están en una sola versión (45 y 42 en desarrollo, 52 y 47 en diez)
  cambian de clave porque A cambió su evidencia.

## C — «de estas normas» y formas afines

«De estas normas», «de estas disposiciones», «de esta norma» y «de este régimen» son el propio TO, como «de las
presentes normas» (`RE_PROPIO_TO`). `cap::8.5::cierre` → `cap::1.4` existe en desarrollo y en diez (destinos
`cap::1.4`, `cap::3.1` y `cap::S7`). «De este ordenamiento» y «de este texto ordenado» siguen la regla de anáfora (e):
si antes se nombró otra norma en el tramo, resuelven a esa norma (caso del selftest: `gescre`). En el corpus aparecen
2 veces, en la partición (`dmrd::S6::parte5`, `repefe::S9::chapeau_seccion`), sin norma antes, y quedan irresolubles;
en los 10 TOs de la tanda 0, 0 veces. Decisión de la autora: si «este» se lee como el propio TO.

## D — escalera de E0 en e0-r2 (agregado 9)

`correr_e0.escalera_e0_r2`: etapa 1 vigente, etapa 2 con marcadores y etapa 3 sin raíz, cada una con K y el pie desde
la línea «Versión». Control sobre los 152 TOs de la partición (`r5_escalera_particion.py --comparar --atribuir`,
`escalera_particion_D_R5.json`): 0 TOs en 0 chunks; modo de lectura igual al de `conteos_b584.json` en los 152; 128 TOs
con los mismos ids. Diferencias de ids por clase: 69 desambiguados (L), 7 unidades sin partir por tabla y 205 de K, en
19 TOs. Chunks con texto distinto: 145 por tablas, 72 por K, 32 por arrastre de un cambio de ids de K, 45 por pies y 5
por pies y K. La atribución vuelve a parsear con K y el pie encendidos y apagados: ninguna diferencia queda sin causa.

**Hallazgo: K pierde texto o estructura en 4 TOs de la partición.** Lo mido aquí por primera vez: el censo de R3
(`rk_fuera_de_muestra.py`) contó las líneas que K conserva, no las que el encabezado forzado quita ni el efecto de lo
conservado sobre el parseo.
- `ri_rml::1.11`: el título del punto («1.11. Metodología … abiertas en el» / «B.C.R.A.») cae en la zona de
  encabezado y la línea «B.C.R.A.» la cierra: K quita el título y el cuerpo se suma a `ri_rml::1.10.4`.
- `nmaeef::S11`: K quita dos renglones de la norma («6. Revisión de la razonable consolidación…» y el siguiente, que
  nombra al B.C.R.A. dentro de la oración).
- `snp_cheq`: K conserva «3.INSTRUCCIONES OPERATIVAS.», el título de la sección repetido en el cuerpo, y el anclaje por
  columna cierra la pila. 7 puntos (3.1.2.3 a 3.1.4.2) quedan como 97 chunks intersticiales.
- `snp_dd`: K conserva «6. TRANSACCIONES Y MENSAJES.» y parte del 6.2.6 pasa a `snp_dd::S6::cierre`.
Propuesta, sin aplicar (`parche_ajuste_K_propuesto_R5.py`, medida sobre una copia):
- K-a′: después de un renglón que empieza con numeración de punto y tiene minúsculas, una línea «B.C.R.A.» ya no cierra
  el encabezado; la de sección sí;
- K-b: una línea en mayúsculas con numeración de un nivel («3.INSTRUCCIONES…») se descarta como antes de K.
Efecto: cambian exactamente esos 4 TOs de 152, que recuperan lo perdido; la tanda 0 no cambia (e0-r2 idéntica); la
ganancia de `ri_rcl` (1.1 y 1.2 en lugar de `S21`) se conserva (una primera variante sin la excepción de la línea de
sección la perdía).

## E — T7 de `r1_tests.py`

`corpus_v2/r1_tests.py:68`, con el criterio de `en_cuarentena`. Sobre KG-Refinado, T7 marca 8 casos, todos
«subclase_de desde propuesto» (los 11 de formato desaparecen); sobre r1 pasa (`t7_r1_tests_KG_Refinado_r1_E_R5.json`).
Los tres ensamblados sellados se reproducen: `kg.json` y demás archivos byte a byte, y los tres reportes que registran
rutas, iguales con la ruta normalizada.

## F — censo R1.d con la e0-r2 final

`r1d_censo_requests.py`: de 2.434 unidades de la tanda 0, 41 cambian de pedido (41 por texto propio, 16 de ellas
también por flags y 1 también por herencia). Costo estimado USD 0,6806 (antes 39 y USD 0,6474).

## G — pies de página

`r4_pies_e0.py --simular`, líneas que la regla quita además de las que el recorte histórico quitaba:
- tanda 0: 7 líneas distintas, 11 apariciones (versión 3, fecha 2, «Comunicación C» 1, vigencia 1, por línea distinta);
- 157 PDFs: 476 distintas, 4.388 apariciones (versión 305, CONAU 102, fecha 48, «Comunicación C» 18, vigencia 1 y
  otra 2, por línea distinta).
Las 2 de forma «otra» son de `manual` y son pie: «(cid:127)» bajo la fecha (página 1169) y «COMUNICACIÓN “C“ 49366»,
con comilla de cierre invertida (página 1884). Ninguna es texto de la norma.

## H — remisiones irresolubles por causa

Pruebas r2 (`reporte_ensamblado_r2.json`, `remite_a.irresolubles_por_causa`):
- desarrollo, 425: norma fuera del inventario 155, punto sin nodos 172, anáfora sin número 49, punto inexistente en
  E0 26, autorreferencia al punto propio 22, anáfora sin antecedente 1;
- diez, 510: 189, 205, 55, 30, 30 y 1.
Las de «punto inexistente», con chunk de origen y tramo: 26 en desarrollo y 30 en diez
(`r3d_remisiones_A_C_H_R5.json`, `G_reglas_<ens>.h_irresolubles.inexistentes`).

## R5 — suite y shapes del perfil r2

Escrito:
- `scripts/remisiones.py` (nuevo, solo stdlib): `es_remision` reconoce las dos formas; firma de `remite_a`; alcance.
- `scripts/muestra_aristas_obs12.py`: el universo resta `remite_a` igual que `referencia`. Sin `remite_a` la salida
  no cambia: la muestra sobre r1 es byte a byte la de HEAD.
- `scripts/regression_kg.py`: R-T4, R-T5 (remisiones con la función), R-E4a8, BKL-0028 contra los tres ids
  esperados, BKL-0006 y BKL-0023 con la lista de umbrales, `EJ-cla-5.1.1.1`, LN-1 a LN-8, censos informativos
  (igual descripción, remisiones por firma y alcance), `--perfil r2`, `--registro-dir`, `--sin-censos`.
- `scripts/shapes_validator.py`, `--perfil r2`: S1 y S3 r2, S18 reescrita, S20 y S24 a S31, S21 con la función;
  vocabulario de `pyd_r2/generados/enums_r2.json` con candado (`abd197ac…`). El perfil congelado y v0 no cambian.
- Selftests: `selftest_regression_kg.py` 140/140, `selftest_shapes_congelado.py` 79/79,
  `selftest_muestra_aristas_obs12.py` 26/26 (con el directorio de salida limpio; d10 falla igual con el código de
  HEAD porque `reports/obs12_selftest_r1/` tiene commiteados el manifest y el log).

Prueba r2 de desarrollo (kg `93a7af72…`), suite: 56 ítems, 35 resuelto, 11 persiste, 10 no_aplicable.
- T4 resuelto (126 = 126); T5 persiste (25 de 30 por contenido, 28 sin la condición de tipo); E4-a8 no_aplicable (el
  perfil r2 no escribe `e4_propuestos.json`); BKL-0028 resuelto.
- `EJ-cla-5.1.1.1` resuelto: (i) dos `condicion_de`, marcadas no verificadas por E3; (ii) `remite_a` a `cla::3.7`;
  (iii) mínimo estricto, 2 «veces», base resuelta a `cla::3.7`. Lo mismo en diez y en cla. Sobre los sellados:
  KG-Reextraído-r1 resuelto y KG-Tanda0-Desarrollo-r1 persiste, como pide el mandato.
- LN-1, LN-2, LN-4, LN-5, LN-6 y LN-8 resuelto; LN-3 persiste (41 de 3.052 aristas de sujeto con mención); LN-7
  no_aplicable (las omisiones con categoría y tramo son de r2b).
- BKL-0006 y BKL-0023 no_aplicable, como en desarrollo r1: el direccionamiento pide «exigencia básica» y la oración de
  compañías financieras en una Restriccion, y los nodos nuevos no las dicen. La inversión del 1.2 de cap sigue en el
  grafo («2.500 M$ bancos»). Decisión de la autora: si se re-direcciona.

Shapes r2, prueba de desarrollo: NO PASA solo por S18 (25 de 273 Restricciones `limite_cuantitativo` sin lista ni
umbral guardado); el resto de las bloqueantes PASS, S27 WARN (3.011 aristas sin mención, informativa en r2a). Diez: S18
con 26 de 301. Cla: PASA. L-ESQ-R2 §1.5 pide «lista no vacía o marca» sin definir la marca: acepto como marca el
umbral guardado sin lista (`campos_heredados_v3.umbral` o `properties_no_definidas.umbral`). Decisión de la autora.

Sin regresiones sobre los sellados:
- shapes: el perfil congelado sobre r1 y los tres ensamblados da lo mismo que el validador de HEAD (con la ruta
  normalizada); v0 sobre run_3, el mismo reporte;
- suite, actual contra HEAD en 7 grafos: cambian de estado T4 y E4-a8 en los tres ensamblados de la tanda 0 (persiste
  → resuelto, R-T4 y R-E4a8, como anticipó D1) y E4-a8 en KG-Reextraído (persiste → no_aplicable: R-E4a8 lee la
  tabla del propio ensamblado y `corpus_v2/salida/` no la tiene; antes leía la de r1). Contra la fixture: 0
  regresiones en KG-Refinado, KG-Reextraído-r1 y KG-Base; 1 en KG-Reextraído, ese E4-a8. Cambia el detalle de T4, T5
  y E4-a8. Los ítems nuevos quedan «sin esperado».

Entrada r2 de la fixture: propuesta, sin sellar, en la clave `propuesta_r2_sin_sellar` de
`scripts/regression_kg_esperado.json`, fuera de `estado_esperado`: la suite no la lee. El sha canónico de
`estado_esperado` no cambia (`69b46385…`).

Remisiones `remite_a` de las pruebas r2 (`reporte_ensamblado_r2.json`):
- desarrollo: 12.833 aristas (interna 12.049, externa 775, to_entero 9; 52 firmas) y 1.382 citas resueltas (1.328,
  46 y 8);
- diez: 14.000 aristas (13.021, 949 y 30) y 1.547 citas (1.474, 52 y 21);
- cla: 179 aristas (177 y 2) y 31 citas (30 y 1).
La regla de alcance aplicada a los sellados (censo de la suite, forma `referencia`):
- KG-Reextraído-r1: 5.645 = 5.456 internas + 183 externas + 6 to_entero (el control de la enmienda 1);
- desarrollo r1: 4.242 (4.118, 120 y 4); diez r1: 4.819 (4.631, 174 y 14); cinco r1: 518 (513 internas y 5 to_entero).

Mediciones de la tanda 1 que van a necesitar la función de remisiones (enmienda 1, R5.e; no se tocan acá):
- `tanda0/code/lectura_e6_tanda0.py`: obs10 (:140-149, extracción = total − referencia − esqueleto), obs11 (:12, clave
  `referencias` del reporte) y plan (1) (:19, referencias por tipo de origen);
- `ev2_tanda0/code/atribucion_tanda0.py:188` (ancla vista por `referencia` en `ver_vecinos`);
- `ev2_r1/code/selftest_r1.py:129` y `:141` (replay de `ver_vecinos`).

## Errores propios, con su causa

1. La regla (i) de R4 (`26d274d`) armaba la procedencia del bloque heredado solo con `to`, `punto`, `rol_documental` y
   `chunk_id`, sin `archivo`, `paginas` ni `ancestros`. S4 y S6 del perfil r2 lo detectaron: 132 aristas `remite_a` de
   la prueba de desarrollo. Ahora `p_h` tiene la forma de las procedencias heredadas de E2 (`r1_referencias.py`, regla
   (i)), y S4 y S6 pasan.
2. El censo de K de R3 no midió las líneas que el encabezado forzado quita ni el efecto de lo conservado sobre el
   parseo: por eso los defectos de D aparecen recién ahora.
3. Lancé la batería en segundo plano sin pedir el tiempo máximo y se cortó a los 30 minutos. La continuación siguió con
   las mismas copias y el control de sha cubre las dos partes.

## Pendiente de la autora

El ajuste de K (D); la marca de S18; el re-direccionamiento de BKL-0006 y BKL-0023; «este ordenamiento» (C); la
entrada de E4-a8 de KG-Reextraído en la fixture; sellar la entrada r2. Fuera de la lista del mandato quedan, de
L-ESQ-R2: la shape informativa «cuantía en la descripción ⇒ elemento en la lista» (§1.5), la entrada que fija las dos
firmas nuevas y el conteo de no verificadas por E3 (§6.5) y una entrada por id nuevo leída contra su chunk (§7.5).
Commit de la autora: PENDIENTE.
