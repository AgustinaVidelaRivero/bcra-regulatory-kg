# Reporte de U-REEXT-T0: re-extracción de la tanda 0 con el perfil r2b (T5, 06/10/2026)

Mandato firmado en `e2027dd` (texto firmado: sha256 `17a110874bf2…`), con sus notas al pie hasta la del FRENO T4,
segundo tramo (`c9d4c40`). Etapas: T1 `23585e2`; T2 `3d793aa`, T2-bis `4ab7a0a` y T2-ter `ad99ac7`; T3 `c499eb3`;
T3-bis `bbc38dc`; sello de los grafos r2b `c9540c0`; T4 `be6b074` y `889b2f9`. Decisiones de la autora en las notas
`5527178`, `07ef3c9`, `3da9c2a`, `04cec96` y `c9d4c40`. Grafos sellados: KG-Tanda0-Diez-r2b `a9631a64…` (8.816 nodos,
27.632 aristas) y KG-Tanda0-Desarrollo-r2b `6e756043…`.

**Cómo se reproduce cada cifra.** `t5/comandos_t5.sh <repo> <copia> <salida>` corre, sobre una copia del repo sin
enlaces simbólicos, los comandos de las cifras: shapes, suite, controles de T3, medición del tablero con M10,
reparación acotada, selftest de claves y la simulación sin la cola. Al final corre `t5/cifras_t5.py`, que recomputa
cada cifra contra su archivo y escribe `t5/salida/anexo_cifras_t5.json` (y su `.md`). Lo corrí dos veces, a dos salidas
distintas, y el anexo sale igual byte a byte. Las salidas completas de los comandos están en el paquete de revisión del
FRENO T5. Abajo, «anexo, bloque N» remite a las claves del JSON.

## 1. Costos, gate, tablero y controles de T3

**Costos** (anexo, bloque 1, `costos`; fuentes: `salida/contadores_t2.json` de `3d793aa`, y `estado_corpus.json` y
`presupuesto_compartido.json` de la corrida):
- T2: USD 49,6598, de los cuales E1 cuesta 24,7195 y E3 24,9403. E3 se reparte en 21,9706 de verificación y 2,9697 de
  los reintentos de E1 del ratchet.
- T2-bis: USD 0,49291 (`4ab7a0a`). T2-ter: USD 0,249002 (`ad99ac7`). T1, T3, T3-bis, T4 y T5: USD 0, sin API.
- **Total de la unidad: USD 50,401698 de un tope de 80.** El script controla que el presupuesto compartido sea igual a
  T2 + T2-bis + T2-ter. Las fases cerradas suman E1 25,146929 + E3 25,25477 = 50,401699; la diferencia de 0,000001
  es de redondeo.
- Tarifa por unidad de T2, sobre las 2.439 unidades: E1 0,010135, E3 0,010226 (verificación 0,009008 y reintentos del
  ratchet 0,001218) y las dos etapas 0,020361.

**Gate de T3-bis**, re-corrido sobre la copia (anexo, bloque 1, `gate`):
- Shapes, con perfil r2, fase r2b y la E0 r2b: **PASA en los dos grafos**, con 18 de 18 bloqueantes en PASS. La
  consola sale idéntica a la de T3-bis.
- Suite, con la fixture sellada (`f72518b3…`): diez da 48 resueltos, 11 persisten y 9 no aplican; desarrollo da 45,
  11 y 12.
- Contra la fixture hay 68 ítems: 9 NO VERIFICADAS (sellados en null), 56 coinciden y **3 regresiones**, RT-C5-3,
  RT-C6-1 y RT-C6-2. Son las declaradas en T3-bis (decisión 3 de la autora): RT-C5-3 por paráfrasis sin cambio de
  sentido, y RT-C6-1 y RT-C6-2 por desviación de fidelidad del modelo en la descripción, con el tramo fiel.
- Las otras declaraciones de T3-bis siguen igual: BKL-0021, en cuarentena declarada, y `remite_a`, sin tocar.

**Columna «r2b» del tablero** (anexo, bloque 1, `tablero_r2b`):
- Tiene 26 filas. T3-bis escribió 22 (una de ellas es «No medible en T3 ni en T3-bis»), y las 4 «No medible en r2b»
  quedan sin tocar.
- La columna del repo es exactamente la derivación de la medición y los controles commiteados en T3-bis. Lo comprobé
  corriendo `escribir_columna_r2b_t3bis.py` sobre el tablero de `bbc38dc^` y comparando con `cmp`.
- Volví a medir sobre la copia (`t3/medicion_tablero_r2b.py`, con M10 regenerado): todas las cifras dan igual. La
  diferencia está en 36 líneas, ninguna de ellas una cifra:
  - el sha256 del reporte del ensamblador, que guarda la ruta absoluta (P20, punto 6);
  - el bloque de regresión, porque `ens_<g>_r2b/suite_perfil_r2.json` se generó antes del sello, con una fixture sin
    las entradas r2b. Con la fixture sellada, la suite da 3 y 56, como dice el tablero.

**Controles de T3 (a–r)**: `t3/controles_t3.py` sobre la copia da `controles_t3bis.json` byte a byte.

**Reparación acotada** (`t2ter/cifra_reparacion.py`; anexo, bloque 1, `reparacion`):
- Hubo 12 salidas mal formadas en 8 unidades: 8 primeros intentos, 2 en `-rforma1` y 2 en `-rforma2`.
- 6 unidades se resolvieron con un reintento, 2 quedaron reparadas (`cap::3.1.1.2` y `cap::4.2.1.2::parte1`) y ninguna
  quedó agotada.

## 2. Lo que P4b dejó sin mejorar

Para cada medida doy la cifra, lo que se puede corregir en código entre tandas sin tocar el prefijo (los insumos a–d
del segundo tramo de T4) y lo que quedaría como límite declarado. La decisión es de la autora. Fuentes:
`t4/salida/tasas_t4.json` (`889b2f9`), la adjudicación por supuesto de la nota `c9d4c40` y `salida/contadores_t2.json`.
Anexo, bloque 2.

**Listas que exceptúan** (T4, punto 6):
- b1: encabezados 1/3 e ítems 9/21. b2: encabezados 5/7 e ítems **0/32** (Wilson 0,000–0,107). `ctacte::3.2`,
  aparte: 0/1 y 0/5.
- `ext::3.13.1` y `ext::3.6.1` están selladas como b1 pero sus encabezados tienen la forma de b2. Con el criterio de b2,
  b1 encabezados daría 3/3; y si las dos listas fueran b2, b1 encabezados daría 1/1 y b2 encabezados 7/9.
- Corrección en código: ninguno de los insumos a–d corrige las listas.
- Límite declarado: los ítems de b2 no llevan en la Condicion ni el cuantificador ni la norma exceptuada (0/32), y en
  b1 9 de 21 ítems llevan la Excepcion del miembro.

**Una Condicion por supuesto** (T4, punto 7):
- Criterio sellado: 1/30 (0,006–0,167).
- Por supuesto, sobre 137 de la fase A, con la adjudicación de `ext::4.1.3.2` de la nota `c9d4c40`:

  | Clase | Supuestos | Wilson al 95 % |
  |---|---|---|
  | Condicion con su relación | 43/137 | 0,242–0,396 |
  | Dentro de una norma | 77/137 | 0,478–0,642 |
  | Fusionados | 7/137 | 0,025–0,102 |
  | Omitidos | 2/137 | 0,004–0,052 |
  | Sin relación | 8/137 | 0,030–0,111 |

  En 26 de las 30 unidades hay al menos un supuesto dentro de una norma.
- Corrección en código: el insumo (d), marcar `supuesto_en_norma`, mide y no corrige.
- Límite declarado: 77 de 137 supuestos dentro de una norma.

**Omisiones `meta_normativo` normativas** (T2 y T4, punto 8):
- T2: hay 1.137 omisiones. 404 traen marca del contador y 390 tienen el tramo solo en el texto heredado.
- T2: la primera verificación de E3 vio 1.222 y objetó 404; el reintento recuperó 59, y 18 dejaron de declararse sin
  que el contenido aparezca.
- T4, sin marca (733 omisiones):
  - 19/30 son normativas, o 14/30 sin las remisiones puras; 0/30 son habilitantes.
  - Con el tramo propio, la estimación es **390,9 [264,9; 511,4]** con remisiones y **268,8 [160,3; 399,4]** sin
    ellas. Es lo que se le escapa al contador.
  - Con el tramo heredado: 4 de 30, unas 97,7 [38,9; 217,6].
- T4, con marca (404 omisiones):
  - 27/30 son normativas y 3/30 habilitantes.
  - Con el tramo propio: 10/30, unas 134,7 [77,7; 206,9].
  - Con el tramo heredado: 18 de 30, unas 242,4 [171,0; 304,7].
- La estimación supone una muestra aleatoria simple dentro de cada grupo.
- Correcciones en código:
  - (a) Marcar en el ensamblado las omisiones con el tramo heredado y dejarlas fuera de la pérdida de la unidad.
  - (b) Marcar «revisar» las omisiones con marca del contador y las de recomendación.
  - (c) Detectar unidades enteras registradas como omisión (`ext::5.8.2.2`) e ítems cuyo texto propio es una omisión
    (`ctacte::2.1.1.4`).
- Límite declarado: las normativas sin marca con el tramo propio, de 268,8 a 390,9 de 733, que el contador no ve.

## 3. La variación del modelo

Anexo, bloque 3.

- **E1, P5** (el mismo pedido dos veces, con temperatura 0; `prompt_r2/p5/salida/analisis_p5.json`): 6 de 27
  respuestas iguales byte a byte.
- **E1, punto 5.b de T4** (una tercera respuesta al mismo pedido): 4 de 27 son idénticas a una respuesta de P5 y 23
  difieren de las dos. La marca del grupo cambia en 3 contra la corrida a y en 5 contra la b.
- **E3, P5**: en 10 unidades con la misma clave en dos corridas, el veredicto es el mismo en 10 de 10, la evaluación
  en 9 de 10, y la salida es igual byte a byte en 6 de 10.
- **E3, esta corrida** (la base `e3_verificacion.db`, desde el inicio de T2, y `veredictos.jsonl`):
  - Hubo 2.685 pedidos, todos distintos: ninguno se repitió, la caché no tuvo aciertos y ninguno lleva temperatura.
  - Por eso ninguna unidad tuvo dos veredictos para el mismo pedido, y la variación de E3 no se puede medir sobre
    `veredictos.jsonl`.
  - 245 de 2.440 unidades tienen dos veredictos, pero el segundo es sobre la salida del reintento de E1: es otro
    pedido, no una variación del modelo.

## 4. Lo que sigue a esta unidad, sin hacerlo

- **Lo que lista el mandato:**
  - La lectura de confirmación de `condicion_de` → Operacion y → Potestad.
  - La medición de la `remite_a` estructural (30 aristas, piso de Wilson 0,75) y del lado del destino, después de la
    unidad que atribuye `remite_a` por tramo.
  - La alternativa de unión de las operaciones por encabezado (30 uniones, piso 0,75).
  - La recuperación por tramo de lo que el reintento dejó.
  - R2 de U-RERESOL-CAT sobre este crudo. Incluye la lectura de la parte B de la enmienda 6 a L-ESQ-R2 (`aplica_a`
    derivada y marcada hacia el rol de alcance, solo si la lectura llega a 28 correctas de 30). Sus insumos de T3-bis:
    los propuestos descartados («se», «cada una»), con sus aristas quitadas; las menciones verbales («podrán»,
    «Deberá rechazarse»); los demostrativos; BKL-0028; y BKL-0021, en cuarentena.
- **U-SINCOLA-T0** (decisión 1 de la autora, nota `c9d4c40`, registrada en `docs/plan_tesis.md`, B2.11). Es el
  ensamblado de los diez TOs sin la cola humana, con `ensamblar_tanda0.py --sin-cola` y el criterio de toda la
  procedencia en la cola: salen 313 nodos y 1.503 aristas, y se quedan los 21 nodos compartidos. Lleva:
  - su doble corrida y sus shapes;
  - su entrada en la suite, con las expectativas de la entrada r2b sellada sin cambiar ninguna y lo que difiera,
    declarado;
  - su registro en `grafos.py` y su recarga en Neo4j.

  La simulación que corrí (sección 6) da un solo cambio en la suite, LN-5, que pasa de resuelto a persiste, como dio
  la de la revisión. Hasta ese sello, el grafo evaluado es el sellado con la exclusión declarada, y el gate del
  pipeline se midió sobre el grafo completo.
- **Mantenimiento del runner, P20** (`docs/checklist_pre_escalado.md`, fila P20; ocho puntos):
  1. Un manejador de SIGUSR1 para frenar de forma ordenada.
  2. Un tope de gasto por corrida.
  3. Los selftests que fallan desde HEAD. `selftest_clave_cache` da hoy VEREDICTO OK, con A1r y A3r verificados
     (sección 5), así que el texto de la fila quedó atrás en ese selftest. `selftest_canal_abierto_e1` no lo corrí en
     T5: según el freno de T3-bis (`bbc38dc`) da 45 de 46.
  4. La clave de la salida original en la marca `reparacion_forma`.
  5. La variación propia de F08f.
  6. Las rutas absolutas en los reportes.
  7. El tamaño de los grafos versionados: el kg de diez pesa 50,21 MB y el límite de GitHub es de 100 MB.
  8. `.DS_Store` en el `.gitignore`.
- **Experimento de comparación de modelos** (`docs/insumos_escritura.md`, §7, ítem 2). Los dos hallazgos de T4 son la
  línea de base: las omisiones normativas y la Condicion por supuesto, con las cifras firmes de la sección 2. El ítem
  tiene cifras que quedaron atrás; ver «Contradicciones».

## 5. Claves de la caché y tabla de reprocesamiento

**El selftest** (`data/experiment/mantenimiento/code/selftest_clave_cache.py --salida-r2b
data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b`, sobre la copia; anexo, bloque 5):
- Da **VEREDICTO OK**. A1r (anclaje de E1 r2b) da **OK**: 2.449 claves calculadas y presentes en la base, de ellas 8
  en `-rforma1` y 2 en `-rforma2`, sobre 2.441 registros. A3r (E3) da **OK**: 2.440 pares.
- Antes de esta corrida, la salida commiteada (`53b7708`) daba NO_VERIFICABLE en las dos.
- La E0 de la corrida es `salida_tanda0_r2b/`, así que la constante `E0_TANDA0_R2B` no cambia.
- Corrió dos veces y salió igual. La salida escrita en `data/experiment/mantenimiento/selftest_clave_cache.json` es la
  corrida con la tabla ya editada; contra la tabla vieja, solo cambia el texto de las tres clases que el selftest
  repite.

**La tabla de reprocesamiento** (`data/experiment/mantenimiento/tabla_reprocesamiento.md`). El diff toca solo las filas
F05, F10 y F14 (líneas 140, 150 y 157) y el §5.
- **Filas.** «Enmienda en curso: ver nota» pasa a citar la enmienda 3 al protocolo entre tandas, firmada el
  04/10/2026 en `0cb0c70`: F05 por el §1, punto 1; F10 por el §1, punto 2; y F14 por el §1, punto 3, con la regla de
  cruce del §3 (`bd77541`).
- **§5.** La estimación del perfil r2b (E1 0,010544 y E3 0,010333 por unidad, en `2a857db`) se reemplaza por la tarifa
  observada: E1 0,010135, E3 0,010226 y las dos etapas 0,020361.
- **Comando 1 nuevo**, sobre `salida/contadores_t2.json` (`3d793aa`), con su salida:
  `24.7195 0.010135 24.9403 0.010226 21.9706 0.009008 2.9697 0.001218 49.6598 0.020361`.
- El desglose de E1 y E3 sale de las fases cerradas y de los clientes de los resúmenes, que es lo que guardan los
  contadores. Las bases dan los tokens por fila, pero no el precio.

## 6. La cola humana

**Cifra y regla:**
- Hay 74 unidades en la cola. Con la adjudicación, **12 de 30 tienen error** (Wilson al 95 %: 0,246–0,577).
- El límite superior supera 0,25, así que la regla del §1, punto 6, de la enmienda al protocolo del 04/10/2026
  (`8d01b04`) se dispara.

**Salida elegida.** La autora decidió (nota `c9d4c40`) que las 74 salen del grafo evaluado de la tanda 0, por la forma
(a): un ensamblado nuevo en U-SINCOLA-T0. T5 la reporta y no la ejecuta.

**Qué sale** (anexo, bloque 6; criterio: toda la procedencia en la cola, sobre el kg de diez `a9631a64…`):
- **Nodos:** salen **313 de 8.816**. Se quedan 21 compartidos: 6 sujetos (entre ellos `Sujeto_banco`, `Sujeto_cliente` y
  `Sujeto_entidad_financiera`), 5 roles, 9 `TextoOrdenado` y una Restriccion.
- **Aristas:** salen **1.503 de 27.632**:
  - 411 llevan la marca de la cola: `establecida_en` 224, `condicion_de` 76, `aplica_a` 73 y 38 de otras relaciones.
  - 1.092 son derivadas, sin marca: `remite_a` 1.004, `establecida_en` 86 y `padre_sugerido` 2.
- `cap::4.2.1.2::parte1` sale entera: 53 entidades.
- **Lo que no se toca:**
  - Ninguna unidad de la cola cae bajo el ancla de alguna de las 14 preguntas que la tienen; la 14 recorre todo el
    grafo.
  - El ejemplo de la tesis (`cla::5.1.1` y `cla::3.7`) no está en la cola.
- **Simulación sobre la copia:** el grafo de diez sin lo que sale queda en 8.503 nodos y 26.129 aristas.
  - Las 15 preguntas de control dan lo mismo: 12/1/2/0, sin ningún cambio.
  - La suite cambia un solo ítem, LN-5, de resuelto a persiste, por el registro de los propuestos.
  - La simulación no es el ensamblado de U-SINCOLA-T0.

## Contradicciones y pendientes (mandan los archivos; lo reporto, no lo corrijo)

1. `docs/tablero_correcciones.md`, columna r2b, fila de las regresiones de la suite (línea 55): dice que el
   `kg_sha256` de la fixture «en el repo es null hasta que lo complete la autora». Desde `c9540c0` la fixture lo
   tiene. El tablero no está entre las escrituras de T5.
2. `tabla_reprocesamiento.md`: el §4 dice todavía «A1r y A3r: NO_VERIFICABLE», y las notas de las líneas 129, 187, 220
   y 245 dicen «la enmienda al protocolo está en curso». T5 solo autoriza el §5 y las filas F05, F10 y F14.
3. `docs/insumos_escritura.md`, §7, ítem 2:
   - Dice «en 25 de 30 unidades hay al menos un supuesto dentro de una norma». Con la adjudicación de `ext::4.1.3.2`
     (`c9d4c40`) son 26.
   - Las normativas con el tramo propio figuran «entre 377 y 526», y las del heredado en 302. Las firmes son 268,8 a
     390,9 sin marca y 134,7 con marca, y 340,1 en el heredado (97,7 más 242,4).
4. `docs/checklist_pre_escalado.md`, P20, punto 3: dice que `selftest_clave_cache` falla. Hoy da OK.

## Errores propios en T5, con su causa

- La primera corrida de las shapes fue sin `--e0`, y S31 quedó «NO COMPUTABLE». Repetí con la E0 r2b, como en T3-bis.
- Para extraer el comando 1 creé por un instante un enlace `.venv` dentro de la copia, apuntando al `.venv` del repo, y
  lo quité enseguida. No hacía falta: el comando corrió con la ruta absoluta del python del repo. Nada se escribió a
  través del enlace, y la comparación de sha256 del repo lo confirma. Va contra la regla l.
- `cifras_t5.py` leía al principio el `selftest_clave_cache.json` de la copia, que era el viejo, y el bloque 5 salía
  NO_VERIFICABLE. Lo corregí: ahora lee la salida de la corrida y controla que sea la del repo.
- El primer conteo del tablero contaba 5 «No medible», porque sumaba la celda escrita por T3-bis. Lo separé en 4 sin
  tocar y 1 escrita.
- En un borrador de este reporte los nodos compartidos decían «10 `TextoOrdenado`». El recuento contra el anexo da 9, más
  6 sujetos, 5 roles y una Restriccion.
