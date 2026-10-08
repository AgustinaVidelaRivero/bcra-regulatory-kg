# Mandato U-CASI-DUPLICADOS — casi duplicados del mismo tipo: muestra adjudicada y fusión solo de forma (BKL-0031, pasos 2 y 3)

**FIRMADO por la autora el 08/10/2026** (firma por mensaje de la autora; versión para firmar en `08ccdfa`; redactado por la mesa el 08/10/2026,
por decisión de la autora del mismo día sobre el
barrido de los límites declarados, fila ENS-14, grupo 2 (paquete de la mesa
`hoja_de_ruta_tanda1_mesa/barrido_limites_declarados_0810_mesa.md`, §3, fuera del repo); asentada en el plan, fila B6.3, nota del
08/10/2026). No va antes de la tanda 1: corre en paralelo con el escalado, como corrección del ensamblado. Si la
regla pasa su umbral, se aplica a todas las tandas en el próximo armado, antes de sellar el grafo evaluado (el de B6.3,
`docs/protocolo_dos_grafos.md`, §2). USD 0, sin API.

DE DÓNDE SALE.
- **El límite.** «Duplicación de contenido entre cajas» («mismo pasaje en ≥2 nodos»): límite 6 de la Tabla 4 del laudo del esquema
  congelado (`data/experiment/esq/laudo_esquema_congelado.md:96` y `:182`, firmado en `2593d4d`; adenda de grupos,
  `adenda_laudo_esquema_congelado_grupos_2026-10-06.md:22`), con destino r2 y vigilancia en la tanda 1.
- **`BKL-0031`** (`data/backlog/backlog.jsonl:76`). El ensamblado funde solo por identidad exacta. Remedio en tres pasos: (1) un detector
  que reporta pares y no funde; (2) la adjudicación por muestra con semilla; (3) solo con esa muestra laudada, una regla de fusión para
  diferencias de forma que nunca actúa si el diff toca números, plazos, porcentajes, fechas o sujetos, con procedencias acumuladas.
  Condición de cierre del paso 3: M1 y M2 bajan, cero fusiones que toquen esos valores (selftest con pares adversariales), suite y shapes
  sin regresiones. Lo mismo en el laudo de r2 (anexo A, §1.2, `docs/laudo_release_r2_pipeline.md:178-205`, BORRADOR) y en el plan
  (`docs/plan_tesis.md:392`).
- **El paso 1 está hecho.** `data/experiment/r2_codigo/r4_detector_casi_duplicados.py` (R4.a de U-R2-CODIGO, `26d274d`): mismo tipo, mismo
  conjunto de Sujetos adyacentes, similitud M2 ≥ 75 sobre el label normalizado, mismo TO (o TOs unidos por `referencia`). Marca
  `mismo_texto_normalizado` (el label) y `diff_toca_valores` (dígitos, «%» y palabras de plazo entre las palabras que cambian en el label
  y la descripción, `:56`). Corrido sobre r2b en T3 de U-REEXT-T0
  (`data/experiment/reext_t0/t3bis/salida/r4_detector_casi_duplicados_r2b.json`, `bbc38dc`, sha256 `70bbef4c…`): en `a9631a64`, 4.109
  pares, 2.705 nodos en algún par, 347 con el mismo texto normalizado y 2.516 cuya diferencia toca valores; en desarrollo (`6e756043`),
  3.841 pares.
- **Los pasos 2 y 3 vienen a esta unidad.** Decisión de la autora del 04/10/2026: van a la revisión de fusionados posterior a U-REEXT-T0,
  con el detector sobre r2b como dato (`docs/plan_tesis.md:385`, decisión (2), y `:405`).
- **La fusión de r2 ya no junta puntos distintos.** `entity_slug_r2` (`reextraccion_v2/e2_reduce/e2_lib.py:845-860`) funde por identidad
  exacta y nunca junta nodos de puntos distintos. Así resolvió T2, la regresión real de dos Restriccion con la misma oración en
  `ext::7.5.3` y `ext::7.8.5.1` (laudo de r2, §4, `:426`; checklist R32, `docs/checklist_pre_escalado.md:148`). Una fusión de casi
  duplicados entre puntos distintos lo reabriría.
- **Recomputado por la mesa al redactar** (copia sin enlaces, detector sin cambios, USD 0; fuera del repo; NO VERIFICADO en el repo hasta
  D1):
  - en `a9631a64`, por estrato, con los valores primero: 216 con el mismo label normalizado y sin valores, 1.377 que difieren en forma y
    2.516 que tocan valores (131 de ellos con el mismo label). En el mismo punto, 1.022 pares (883 nodos): 12, 269 y 741. Entre puntos
    distintos, 3.087: 204, 1.108 y 1.775;
  - en `e22fae1a` (sin cola diez): 3.792 pares, 2.551 nodos, estratos 192, 1.245 y 2.355; en el mismo punto, 983 pares: 11, 238 y 734;
  - nodos de contenido con procedencia en más de un punto: **0** en los dos grafos (solo Sujeto 70, Comunicacion 13 y TextoOrdenado 10).
    Lo pendiente del plan sobre esos nodos (`:405`, EO18 de M3.e, medido en r2a) no tiene casos en r2b. Las operaciones de un mismo acto
    repartidas en varios puntos son otro límite (ENS-15 del barrido, grupo 3).
- **Lo que no cubre.** El detector solo empareja nodos del mismo tipo. El mismo pasaje en nodos de tipos distintos queda fuera de esta
  unidad y sigue declarado.

LA REGLA DE FUSIÓN. Se fija por escrito y se sella (sha256 y hora), con su código y su selftest, antes de sortear la muestra de D2
(decisión 1). Propuesta de la mesa, para que D1 la precise contra el código:
- **Ámbito:** pares del detector en el mismo punto, TO::punto (decisión 2).
- **Igualdad estructural**, toda obligatoria:
  - mismo tipo;
  - mismo conjunto de Sujetos adyacentes por aristas no derivadas (sin las de `esqueleto`, `derivada_de_procedencia`, U3 de
    U-UNION-ESTRECHA ni U-APLICA-ROL-ALCANCE), para que el orden con esas unidades no cambie qué pares se funden;
  - `properties` iguales salvo `descripcion`, después de normalizar (umbrales, plazo, tipo, modalidad y demás);
  - las mismas marcas de cola, cuarentena y E3;
  - ninguna arista entre los dos nodos.
- **Guardas sobre la diferencia:** las palabras que cambian en el diff de label y descripción, como en el detector. Nunca funde si una de
  esas palabras es o contiene:
  - **un número:** un dígito; un numeral en letras de la lista de [c14] (`docs/tablero_correcciones.md:169-178`: un, una, dos… cien),
    «mil», «millón», «millones», «medio», «mitad» o «doble»; «%», «por ciento» o «veces»; una unidad de monto de [c14] ($, US$, U$S, USD,
    UVA, pesos, dólares);
  - **un plazo:** día, hábil, corrido, semana, mes, año, hora, bimestre, trimestre, semestre, plazo, término, vencimiento, antelación,
    anticipación o prórroga; o una periodicidad (diario, mensual, bimestral, trimestral, semestral, anual); en singular o plural;
  - **una fecha:** un nombre de mes, «fecha», «vigencia» o «vigor» (las fechas en cifras caen en la guarda de número);
  - **un sujeto:** parte de una clave no ambigua del índice de E4 (`label_exacto`, `alias_exacto`, `label_singularizado`) o de una
    expresión colectiva de R3 (`reextraccion_v2/corpus_v2/r1_e4.py:306`), buscada con límite de palabra. Tampoco funde si los dos nodos
    difieren en la `sujeto_mencion` de sus aristas de sujeto;
  - **una negación, una modalidad o una excepción** (decisión 3): no, ni, nunca, sin, salvo, excepto, excepción, deberá(n), debe(n),
    podrá(n), puede(n), prohíbe, prohibido, obligatorio, facultativo.
  - La guarda de número cubre la marca `diff_toca_valores` del detector: la regla nunca funde un par del estrato «valores».
- **Componentes:** se funden pares. Un componente de tres nodos o más se funde solo si todos sus pares cumplen la regla; si no, ninguno.
- **La fusión:**
  - sobrevive el id menor en orden lexicográfico, con su label y su descripción;
  - las aristas del absorbido se re-apuntan, y las triplas repetidas se funden con procedencias acumuladas, como `r1_e4._reapuntar`
    (`r1_e4.py:179-180`); las procedencias del absorbido se suman a las del sobreviviente;
  - la marca va en `properties_no_definidas.fusion_de_forma` del sobreviviente (ids absorbidos y sha256 de la regla), sin tocar
    `modelos_r2.py`; todo va al registro `fusiones_de_forma.jsonl` (el par, el diff y las guardas evaluadas).
- Solo en la fase r2b, como último paso de la cadena, después de las aristas derivadas; r1 y r2a no cambian.

ETAPAS.
- **D1. El marco, el criterio y la regla, sellados antes de sortear y de leer** (sobre una copia, sin leer ningún par).
  - El detector del paso 1, sin cambios, sobre `a9631a64`, `e22fae1a` y los dos de desarrollo: las cifras de arriba, con los estratos y el
    ámbito.
  - Control: los nodos de contenido con procedencia en más de un punto, en los cuatro grafos r2b.
  - Criterio de «duplicado de forma», sellado: los dos nodos expresan el mismo contenido del texto (la misma norma, condición, definición
    u operación), con el mismo alcance (a quién y a qué se aplica) y los mismos valores (números, plazos, fechas, sujetos). La diferencia
    es solo de redacción. Las no decidibles se declaran y cuentan como no duplicado.
  - El texto de la regla con sus listas cerradas, en `data/experiment/casi_duplicados/regla_d1.md`, sellado con su código y con un
    selftest sintético: un par adversarial por guarda, uno entre puntos distintos, uno con una arista entre los dos nodos y un componente
    que no cumple todos contra todos. Control negativo: el código sin guardas funde los adversariales.
  - FRENO D1: la autora aprueba el criterio y el texto de la regla.
- **D2. La muestra adjudicada.**
  - Marco: los pares del detector en el ámbito, en `a9631a64`, en tres estratos: «mismo texto» (mismo label normalizado y diff sin
    valores), «forma» (el resto sin valores) y «valores». 30 por estrato, con una semilla nueva, distinta de toda semilla ya usada en el
    repo, fijada y sellada antes de sortear; censo si el estrato tiene menos de 30 (en el mismo punto, «mismo texto» tiene 12).
  - Precisión de la regla: los pares leídos que la regla funde y, si son menos de 30, más pares de las fusiones de la regla, con la misma
    semilla, hasta 30. El procedimiento se sella con la semilla.
  - Fichas sin veredicto, sin el estrato y en orden sorteado: los dos nodos (tipo, label, descripción, tramo, punto), el texto de la
    unidad y el heredado.
  - Lectura en tres pasos, cada una sellada antes de comparar: primera, de una sesión aparte que no diseñó la regla (FRENO D2-a, sin la
    cifra); segunda, a ciegas, de la mesa; adjudicación de la autora de las divergencias.
  - Cifras: duplicados de forma sobre leídos en cada estrato, con Wilson al 95 %; y la precisión de la regla, con Wilson.
  - FRENO D2 con las cifras.
- **D3. La regla: pre-medición y aplicación.**
  - **D3-a, pre-medición, sin leer**, en `a9631a64` y `e22fae1a`: cuántos pares fundiría, por tipo y por TO; cuántos bloquea cada guarda
    (la primera que lo bloquea y todas las que lo bloquean); cuántos componentes quedan sin fundir. Control: ninguna fusión con
    `diff_toca_valores`. Si la precisión de D2 no llega al umbral (decisión 4), no se funde: el límite 6 queda declarado con las cifras de
    D2 por estrato y la unidad cierra acá. FRENO D3-a.
  - **D3-b, si pasa: la implementación**, solo r2b (fila F15 de la tabla de reprocesamiento, solo código sobre lo guardado).
  - **El riesgo para la suite, controlado.** Sobre los grafos armados con y sin la fusión, con la misma base de código:
    - la suite del gate de la release (laudo de r2, §3, `docs/laudo_release_r2_pipeline.md:66-70`), con la fixture vigente y sin editarla:
      0 regresiones no declaradas. Siguen declaradas las tres de T3-bis (RT-C5-3, RT-C6-1, RT-C6-2);
    - la lista de los ítems de la suite cuyo estado, detalle o valores cambian, con los ids fundidos que intervienen; y los ids absorbidos
      que aparecen en la fixture o en `scripts/regression_kg.py`, por grep. Son los matchers que apuntan a nodos fundidos;
    - shapes, perfil r2 y fase r2b: bloqueantes en PASS;
    - M1 y M2, con el comando del tablero (laudo de r2, §3, punto 3, `:71`), con y sin la fusión.
  - Lista exacta de fusiones (`fusiones_de_forma.jsonl`).
  - Diff de los cuatro grafos r2b armados con el código de la base de D3 y con el código nuevo. No se compara contra los sha sellados, que
    ya no son la salida de HEAD (`reresolucion_catalogo/freno_r2_3bis.md:14-15`). Solo desaparecen los absorbidos, y solo cambian las
    aristas re-apuntadas o fundidas, y las procedencias y la marca de los sobrevivientes. r2a, `70d51e42…` y `fa4c1043…` byte a byte.
  - Selftest de claves OK, sin claves movidas.
  - Nota en F15, y las anclas de la tabla que corran, en cualquier fila, corregidas (precedente: R2-3 de U-RERESOL-CAT).
  - Entra en el próximo armado de todas las tandas, antes de sellar el grafo evaluado.

CRITERIOS DE ACEPTACIÓN. Cada uno con su comando y su salida:
- el criterio y la regla, sellados antes del sorteo (sha256 y hora, y los mtimes de las salidas, posteriores);
- la semilla, el procedimiento y la lista, sellados antes de leer;
- las tres lecturas selladas antes de comparar;
- el selftest sintético de la regla en verde, con su control negativo;
- doble corrida del detector, de la pre-medición y, en D3-b, de las cadenas, byte a byte;
- en D3-b, que `kg.json` cambie solo por las fusiones de la lista, y r2a byte a byte;
- la suite con 0 regresiones no declaradas, las shapes bloqueantes en PASS, y M1 y M2 con y sin la fusión;
- `selftest_r3` y `selftest_clave_cache --salida-r2b` en verde, sin claves movidas;
- sha256 del repo antes y después de cada corrida;
- 2.213 `.pyc`;
- grep de convenciones (nombres de personas, referencias a mensajes o correos), pegado aunque dé vacío.

ESCRITURAS:
- `data/experiment/casi_duplicados/` (se crea) y el scratchpad;
- en D3-b, además: `data/experiment/tanda0/code/fusion_forma_r2b.py` (se crea; decisión 5), la llamada en
  `data/experiment/tanda0/code/ensamblar_tanda0.py` (solo r2b), `data/experiment/r2_codigo/selftest_r3.py` (casos nuevos, entre ellos los
  adversariales), y la nota de F15 y las anclas que corran en `data/experiment/mantenimiento/tabla_reprocesamiento.md`.

PROHIBIDO: el prefijo y el mensaje de E1, E3, los validadores, `modelos_r2.py`, `e2_lib.py` (la clave de fusión exacta no cambia), el
detector del paso 1 (se copia, no se edita), la suite y su fixture (se corren, no se editan), los grafos sellados y sus registros,
`grafos.py`, la API, commitear.

REQUISITOS: CLAUDE.md §4 (a a l). Por la regla l, las corridas y los selftests van sobre una copia sin enlaces, con el sha256 del repo
antes y después.

CONVIVENCIA:
- D1, D2 y D3-a son de solo lectura sobre lo guardado: pueden correr en cualquier momento después de la firma.
- D3-b toca `ensamblar_tanda0.py`. Va después de U-OMISIONES-COD (BORRADOR v5 de la mesa, fuera del repo: G-r cambia el punto de 22 nodos,
  y el ámbito es el punto), de U3 de U-UNION-ESTRECHA y de B3 de U-APLICA-ROL-ALCANCE. La fusión va última en la cadena: re-apunta también
  sus aristas.
- Se decide junto con R32 (T2) y R13 (H2) del checklist (`:120`, `:129`, `:148`). Con el ámbito del mismo punto, T2 sigue resuelto.
- El laudo de r2 (BORRADOR v2) no dice que los pasos 2 y 3 salieron de r2. Su anexo A, §2, punto 5 (`:312-314`), los pone todavía antes de
  la corrida de r2, y la §5 de la v2 no lo reemplaza. Por la regla d de CLAUDE.md §4 mandan los archivos: la mesa propone declararlo en la
  §5 de la v2 antes de su firma.
- No entra al re-sellado único de la tanda 0 previo a la tanda 1: entra en el armado que precede al sello del grafo evaluado.

DECISIONES DE LA AUTORA AL FIRMAR, con la recomendación de la mesa:
1. **Cuándo se sella la regla.** (a) En D1, antes de leer, y su precisión se mide en D2 sobre los pares que funde; (b) en D3, después de
   D2, con una lectura de control propia de 30 fusiones, semilla nueva y piso de 28. **Recomendación: (a).** Es una sola lectura y la
   regla no se ajusta a los veredictos. Si después de D2 se quiere cambiar la regla, se sella de nuevo y se mide por (b).
2. **Ámbito.** (a) El mismo punto: 1.022 pares en `a9631a64`, 281 sin valores (12 + 269); (b) el mismo documento: 4.109 pares, 1.593 sin
   valores (216 + 1.377). **Recomendación: (a).** Es el «mismo pasaje» del límite (`laudo_esquema_congelado.md:182`), mantiene resuelto T2
   y no crea nodos con procedencia en más de un punto.
3. **La guarda de negación, modalidad y excepción**, que el texto de la decisión no nombra. **Recomendación: sí.** Pasar de «deberá» a
   «podrá», o agregar un «salvo», cambia la norma sin tocar números, plazos, fechas ni sujetos. Solo cuesta fusiones de menos.
4. **El umbral para aplicar** (laudo de r2, §5, punto 3, `:436-437`). **Recomendación:** límite inferior de Wilson al 95 % ≥ 0,75 sobre 30
   fusiones leídas: 28 de 30 (0,787; con 27, 0,744), el piso de L-ESQ-R2 §6.3. Alternativa más estricta: 30 de 30 (0,887). La de 28
   alcanza porque los grafos sellados quedan, la lista de fusiones se declara y la fusión se rehace desde lo guardado.
5. **Dónde va el código y qué fila.** **Recomendación:** un módulo nuevo (`fusion_forma_r2b.py`) con una sola llamada en la cadena, para
   que el diff de `ensamblar_tanda0.py` y las anclas que corren sean pocos; y una nota en F15, sin fila nueva. Una fila F15f pediría su
   variación en `selftest_clave_cache.py` y el contraste regenerado, como F13c en U-ALCANCE-E1.
6. **Lo pendiente de los nodos con procedencia en más de un punto** (`docs/plan_tesis.md:405`). **Recomendación:** se cierra para r2b con
   la cuenta de D1 (hoy, 0 nodos de contenido), y lo de las operaciones entre puntos sigue en ENS-15. Si D1 encuentra casos, queda
   abierto, con su lista.

**Decididas al firmar (08/10/2026):**
1. **(a)**: la regla se sella en D1, antes de leer, y su precisión se mide en D2 sobre los pares que funde.
2. **(a)**: el ámbito es el mismo punto (1.022 pares en `a9631a64`, 281 sin valores).
3. **Sí** a la guarda de negación, modalidad y excepción.
4., 5. y 6. **PENDIENTES**: no se tomaron al firmar (el umbral para aplicar, dónde va el código y la fila, y lo pendiente de los nodos
   con procedencia en más de un punto); el umbral se decide antes de D3-a.

## Firma

FIRMADO por la autora el 08/10/2026 (versión para firmar en `08ccdfa`), con las decisiones 1 a 3 y las 4 a 6 PENDIENTES. Rige desde esta
firma: D1 puede empezar.
