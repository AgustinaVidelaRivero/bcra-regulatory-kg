# U-R2-CODIGO — FRENO R4 (con los agregados 7, 8 y 9)

USD 0, sin API ni Neo4j. Batería `control_r4.sh` (paquete de revisión): espejo en el scratchpad, dobles corridas y
selftests. Las reglas de las remisiones decididas tras el freno posterior a R3 están en
`reglas_remisiones_postR3.md`.

Salidas en esta carpeta, copias de la batería con doble corrida idéntica: `r3d_remisiones.json`,
`r3_perdidas_remisiones.json`, `r3h_lectura_umbrales.json`, `reglas_remisiones_censos.json`, `r4_pies_e0.json`,
`r4_diag_escalera_e0.json`, `r4_claves_cache.json` y `r4_detector_casi_duplicados.json`.

## Agregado 8 — pies de página dentro del texto de E0

Diagnóstico por caso (`r4_pies_e0.py`, criterio [c22]). Son 206 líneas de pie: 3 en 3 chunks de la tanda 0 y 203 en
60 chunks de 27 TOs de la partición. El recorte de E0 (`e0_lib.separar_encabezado_pie`) quita líneas desde el final de
la página mientras cumplan `RE_PIE`. Causas:
- 82 líneas: el pie cumple `RE_PIE`, pero lo sigue en la página una línea que `RE_PIE` no toma, y el recorte se
  detiene antes. Las tres de la tanda 0 son de este grupo:
  - `ric::11.1.1` y `ric::11.1.4`: después de «01/07/2018» viene «Comunicación “C” 81129»;
  - `ctacte::6.1.2.3`: «04.04.01», fecha con puntos.
  En la partición, además: año de cinco dígitos («28/03/20206», fabcra), «Circular CONAU …» y «… 1 de 3».
- 124 líneas: el pie tiene una forma que `RE_PIE` no reconoce, sobre todo «Versión : …» con espacio antes de los dos
  puntos y sin «Página N» al final (manual, 132 líneas en total), «Página99» o el pie sin «Página».
- Debajo de la línea «Versión…Comunicación» nunca hay más de 2 líneas, y todas tienen forma de pie.

Corrección, solo en e0-r2 (`pie_desde_version`, `e0_lib.py`; `correr_e0.py` la pasa con `--version-e0 e0-r2`). Si una
de las 3 últimas líneas de la página cumple `^Versi[oó]n\s*:.*Comunicaci[oó]n`, esa línea y las que la siguen son pie.
Después sigue el recorte histórico.
- E0 legada 34/34 byte a byte.
- e0-r2 de la tanda 0: 0 chunks con pie (antes 3). Cambian solo `ctacte::6.1.2.3`, `ric::11.1.1` y `ric::11.1.4`, que
  pierden «Vigencia:», la línea de versión y las que la seguían; los ids no cambian. También cambian `conteos`,
  `cobertura` y `estructura` de ctacte y ric, y el flag `evidencia_tabular` de `ric::11.1.1`, cuya primera línea de
  muestra era el pie.
- Simulación página por página sobre los 157 PDF (tanda 0 y partición), todas las páginas: las líneas [c22] que
  quedan como contenido pasan de 1.981 a 2. Las 2 son de `manual` (páginas 255 y 933), con la línea de versión fuera
  de las 3 últimas: quedan declaradas.
- La regla quita 4.388 líneas que el recorte histórico dejaba. Todas tienen forma de pie (versión, fecha, «Vigencia:»,
  «Circular CONAU …», «Comunicación “C” …»), salvo una línea de glifo «(cid:N)».

## Agregado 9 — por qué `correr_e0` con e0-r2 da 0 chunks: diagnóstico y propuesta (sin implementar)

No son solo ceninf y ri_niif. `correr_e0.correr` hace, por TO, solo la etapa 1 de la escalera de E0 (camino vigente,
`correr_e0.py`, rama `if r2:` de `correr`). La partición se generó con `correr_b584.py`, que agrega la etapa 2
(marcadores B5.8.2) y la etapa 3 (modo sin raíz B5.8.1) cuando la etapa 1 no da chunks (`correr_b584.py`, `correr_to`).
Según `conteos_b584.json`, 61 de los 152 TOs se activaron por cero unidades: 56 en modo sin raíz y 5 con marcadores.
`r4_diag_escalera_e0.py` corre la etapa 1 de `correr_e0`, legada y e0-r2, sobre esos 61 PDF: los 61 dan 0 chunks en
las dos versiones.

Propuesta, para aprobar antes de implementarla. En `correr_e0` con `--version-e0 e0-r2`, cuando la etapa 1 da 0
chunks, correr las etapas 2 y 3 como `correr_b584.correr_to`:
- etapa 2: `clasificar_paginas(…, marcadores_b582=True)` y `parsear_cuerpo(…, marcadores_b582=True)`;
- etapa 3: `roles_para_modo_sin_raiz` y `parsear_cuerpo(…, modo_sin_raiz=True)`;
- en cada etapa, K (`mayusculas_repetidas` con los roles de esa etapa) y el pie desde la línea «Versión»;
- `parsear_indice(…, marcadores_b582=…)`, las tablas de e0-r2 sobre el resultado y el modo de lectura de cada TO
  en `conteos.json`.
La versión legada no cambia: E0 legada 34/34. Control: un manifiesto de la partición en el scratchpad. Los ids de
chunk de e0-r2 de los 61 TOs tienen que ser los de `b584_particion`, salvo las diferencias declaradas de e0-r2
(tablas, K, pies e ids desambiguados por L).

## R4.a — fusión: T2 con H2, y `BKL-0031` paso 1

`e2_lib.entity_slug_r2`, usada solo por `ensamblar_r2`. `entity_slug_v3` no cambia: su selftest exige la copia textual
de `assemble_v3`. La clave tiene dos casos:
- Restriccion, Obligacion y Excepcion: descripción más el punto de la procedencia (TO::punto);
- Condicion, Definicion y Potestad: label, descripción y punto.
La fusión sigue siendo exacta, pero nunca junta nodos de puntos distintos. Operacion, Sujeto, TextoOrdenado y
Comunicacion siguen con la clave de v3. La H2 era decisión abierta del laudo; la clave elegida es mía y queda para tu
revisión.
- T2, sobre la prueba de r2 de desarrollo (`ensamblar_tanda0.py --perfil-r2 --e0-r2`; 6.470 nodos, 24.762 aristas, 0
  fuera del modelo, doble corrida idéntica): «resuelto», con 5 nodos de ext con «125 %» en 5 puntos. Sobre
  KG-Tanda0-Desarrollo-r1 da «persiste», con 4 nodos.
- H2: los conflictos de properties de los tres tipos en E4 bajan de 51 (sellado de desarrollo r1: Condicion 27,
  Definicion 13 + 8 de `termino`, Potestad 3) a 1 en r2. Ese uno es de forma: la misma descripción con y sin mayúscula
  inicial, que el slug normaliza.
- El ensamblado viejo se reproduce: `r1/kg.json` eab2fdd0, dd42d6d9 y 4097d4fd; los 3 archivos que difieren solo
  cambian la raíz de rutas.
- `BKL-0031`, paso 1 (`r4_detector_casi_duplicados.py`, solo lectura, no funde). Candidato: mismo tipo, mismo
  conjunto de Sujetos adyacentes, similitud M2 (`fuzz.ratio` sobre la superficie normalizada del label) ≥ 75, y el
  mismo TO o TOs unidos por una arista `referencia`. Pares (nodos en algún par):
  - KG-Reextraído-r1: 2.861 (1.953);
  - KG-Tanda0-Desarrollo-r1: 2.096 (1.742);
  - Diez: 2.429 (2.067);
  - Cinco: 311 (301).
  Cada par lleva el diff por palabras y la marca `diff_toca_valores`; el desglose por tipo está en el reporte. En la
  muestra que leí, casi todos son contenidos distintos con label parecido («Límite 0 %» y «Límite 20 %»; «A: punto de
  unión» y «D: punto de separación»). La adjudicación es tu paso 2.

## R4.b — `BKL-0030` y agregado 7

- (a) `cliente_e1.MAX_TOKENS_REINTENTO_CORTE_R2 = 16384`, usada solo por el runner con `--perfil-r2`. La constante de
  los perfiles existentes queda en 32.768.
- (b) Si la unidad corta también en el reintento, el runner r2 la parte con `correr_e0.particionar_por_corte`: la
  mecánica de sub-chunking de E0, disparada por el corte. Con `respetar_tablas`, una línea dentro de [TABLA … FIN
  TABLA] nunca es marcador de ítem, así que ningún límite cae dentro de un bloque (agregado 7).
- Las partes se extraen en el mismo pase y quedan en `particiones_por_corte.json`. En la compactación, E3, la entrada
  de E2 y el ensamblado (`chunks_con_partes`) reemplazan a la unidad, con la procedencia en la unidad documental.
- Pruebas sin API (`selftest_r4.py`, 26/26):
  - con los tres casos del laudo, el reintento a 16.384 pasa la guarda del SDK contra un transporte local y el de
    32.768 lo rechaza;
  - las tres claves del reintento a 16.384 están en la caché de E1, con `run_label` `tanda0_dirigida_e1`: costo 0;
  - `cap::4.2.1.2` de e0-r2 (26.726 caracteres, 3 tablas) se parte en 2 sin abrir ni cerrar una tabla a medias;
  - sin el perfil r2, el mismo corte es error definitivo con reintento a 32.768.
- Control nuevo (`r4_claves_cache.py`, semilla 20261002): con `produccion_dev` y `v3_b54` hay 106 claves en la
  muestra (E1 primer intento 20+20, E3 verificación 20+20, reintento por corte de los tres casos 3+3, reintento del
  ratchet 10+10). Son idénticas con el código de HEAD y con el de hoy. Están todas en las dbs, salvo los reintentos
  por corte, que nunca se enviaron.
- Camino sin corte: `selftest_manifiesto` y `selftest_ub53` dan logs byte a byte idénticos a los de antes de R4.

## R4.c — `cuarentena`: CONTRADICCIÓN, no ejecutada

El T7 que marca los 11 casos de formato es el de la cadena r1, `corpus_v2/r1_tests.py:68` (`!= "true"`). El laudo lo
lista como módulo (§1.4), pero el mandato no lo incluye en las escrituras («el pipeline que se toca»), así que no lo
edito. Medido sin editar: sobre KG-Refinado marca 11 «sin cuarentena=true» y 8 `subclase_de` desde propuestos (C4,
real); sobre r1 pasa. El T7 de la suite (`scripts/regression_kg.py`, `cuarentena_bool`) ya da «resuelto» sobre
KG-Refinado desde B2.1 fase 2. Decidís vos: autorizar `r1_tests.py` (leer la cuarentena con el criterio de
`en_cuarentena`) o dar el ítem por cubierto con la suite.

## R4.d — mutuales: RT-C6-5

`t_rt_c6_5` en `scripts/regression_kg.py`: la cláusula «por las financiaciones que otorguen» en N1 de C6 pasa de
informativa a test. Es un ítem del perfil r2 (`ITEMS_R2`), fuera de la partición 46 = 19/23/4 del inventario, que no
cambia.
- Da «persiste» en KG-Reextraído-r1, en KG-Tanda0-Desarrollo-r1 y en la prueba de r2, y «resuelto» en KG-Refinado,
  donde la cláusula se agregó a mano. Figura en el reporte de la suite.
- Sin entrada en la fixture: la suite lo informa como «sin esperado». La entrada de r2 la propone R5 y la sellás vos.
- `selftest_regression_kg` 89/89 (85 + 4).

## Controles de la batería

- E0 legada 34/34. e0-r2 en doble corrida idéntica. Los tres ensamblados sellados se reproducen.
- Pruebas del perfil r2 de cla y de desarrollo en doble corrida idéntica, con 0 nodos y 0 aristas fuera del modelo.
- Doble corrida idéntica de las remisiones, el desglose de pérdidas, los censos, el detector de `BKL-0031`, las claves
  de caché, los umbrales, los pies y la escalera.
- Suite sobre r1 y KG-Refinado contra la fixture: 0 regresiones; RT-C6-5 queda «sin esperado».
- Selftests:
  - e0 57/57, b52 39/39, b581 34/34, b582 59/59, b583 33/33, ub53 40/40, cable v3 45/45;
  - corpus 21/21, E2 35/35, dirigida 28/28, pyd_r2 296/296;
  - r3 83/83, r2 18/18, e0-r2 31/31, clave de caché OK, regression_kg 89/89, r4 26/26;
  - manifiesto 32/37: P5, ambiental y conocido, con log byte a byte igual al de antes de R4.
- `.pyc` y `__pycache__` sin cambios. El repo no cambió durante la batería (sha de los 109 archivos modificados o
  nuevos, antes y después).

## Error propio, con su causa

Para el control de claves de caché armé un espejo con el código de HEAD: `hacer_espejo.sh` y, para cada `.py`
modificado, `git show HEAD:<ruta> > espejo_head/<ruta>`. En ese espejo, `data/experiment/r2_codigo` es un enlace
simbólico al directorio del repo. Tres escrituras fueron al repo y pisaron con su versión de HEAD `r3d_remisiones.py`,
`selftest_r3.py` y `rk_fuera_de_muestra.py`. La primera batería de R4 ya estaba corriendo con esos archivos: la detuve
al verlo en `git status` y la descarté.
- Restauración:
  - `rk_fuera_de_muestra.py`, desde la copia del paquete posterior a R3 (sha `452a2c26…`, el de su manifiesto);
  - `r3d_remisiones.py` y `selftest_r3.py`, reaplicando en orden, sobre HEAD y sobre esa copia, los diez segmentos
    de reemplazo exacto de esta etapa, tomados del registro de la sesión (`reconstruir_restauracion_R4.py` en el
    paquete).
- Verificación: `r3d_remisiones.py` restaurado reproduce byte a byte la salida previa al incidente, y `selftest_r3` da
  83/83. Los otros diez archivos de la lista estaban en directorios copiados del espejo y no se tocaron.
- La batería nueva controla que el repo no cambie.

## Límites declarados

- Agregado 8: 2 líneas de pie en `manual` con la versión fuera de las 3 últimas líneas de la página.
- H2: 1 conflicto de forma en ext.
- R4.b: una unidad sin ítems detectables no se puede partir. `cap::3.1.14.1` y `cap::4.3.3.1` están en ese caso; con
  16.384 entraron en la re-extracción dirigida, y si volvieran a cortar quedarían como error definitivo declarado.
- `BKL-0031`: el detector reporta y no funde; la tasa de candidatos verdaderos no está medida.
