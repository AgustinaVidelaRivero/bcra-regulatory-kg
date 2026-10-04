# Índice de insumos del repo para la escritura de la tesis

Índice de los artefactos del repo que alimentan la escritura. Lo mantengo desde el
30/09/2026 (plan, fila C1.11). La escritura sigue en la mesa de escritura; este índice
le dice qué insumo usar, de dónde sale y con qué salvedades.

**Convenciones.**
- La tesis se cita por sección y frase desde la versión de Overleaf.
  `docs/tesis/main.tex` del repo está desactualizado y no se usa como fuente (plan,
  fila C1.11).
- Las secciones se nombran por su contenido, según la estructura decidida el 30/09:
  - capítulo 3: del documento a su análisis y al esquema;
  - capítulo 4: el pipeline, componente por componente, y la construcción por etapas,
    con la tanda 0 como primera etapa.
  El número de sección en Overleaf queda NO VERIFICADO.
- Toda cifra que pase a la tesis se toma del artefacto, con su comando o su clave, no
  de este índice.
- Estado de cada insumo: **disponible** (commiteado) o **pendiente** (unidad en curso).

## 1. Estadísticas descriptivas del corpus — disponible

- **Ruta y commit:**
  - `reports/u_insumos_cap/estadisticas_corpus.md` y `estadisticas_corpus.json`,
    generados por `reports/u_insumos_cap/u_insumos_i1.py`;
  - commit `ded3494` (U-INSUMOS-CAP, etapa I1);
  - comando: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_insumos_cap/u_insumos_i1.py`;
  - doble corrida byte a byte idéntica, y una re-corrida independiente de la mesa
    también idéntica.
- **Qué contiene:** para el corpus escalado (152 TOs), el conjunto de desarrollo (5) y
  los cinco TOs de la tanda 0:
  - TOs por clase y por categoría;
  - páginas por rol y por TO;
  - unidades por tipo y por profundidad;
  - estructura de la numeración: puntos terminales y contenedores;
  - tablas y fórmulas;
  - largos de unidad;
  - remisiones internas y externas;
  - marcadores deónticos;
  - tabla de origen de las disposiciones y procedencia, por TO;
  - nodos por tipo y aristas por predicado de KG-Tanda0-Desarrollo-r1 y de
    KG-Reextraído-r1.

  Las reglas R0 a R17 se declararon antes de aplicarse (§1 del `.md`). Las cuatro
  cifras publicadas de la partición (152 / 6.757 / 9.324 / 559) están reproducidas
  (§0).
- **Alimenta:**
  - capítulo 3: la descripción de los documentos del BCRA y su análisis (tamaño,
    estructura de la numeración, tablas, remisiones, lenguaje deóntico, tabla de
    origen);
  - capítulo 4: la construcción por etapas (qué se procesó en desarrollo y en la tanda
    0) y el grafo resultante (nodos y aristas por tipo).
- **Salvedades:**
  1. Las tablas lógicas son 559 parseadas (`particion_152.json`) o 563 detectadas
     (`conteos_b584.json`), según el archivo. Hay que citar cuál.
  2. Las remisiones «externas» son menciones a una norma nombrada detectadas por regex
     (regla R8). Pueden ser del mismo TO y no son remisiones entre TOs. Para las
     remisiones entre TOs se usan las aristas `referencia` entre TOs del grafo.
  3. Los cinco TOs de la tanda 0 no tienen chunks marcados como tabla.
  4. Límites que declara el propio reporte (§7):
     - los anexos son una cota inferior;
     - los TOs sin portada legible quedan sin dato de procedencia;
     - la clase de la partición no aplica al conjunto de desarrollo;
     - las tablas lógicas de cla, ext, pro y ric son NO ENCONTRADO (solo cap tiene el
       testigo del parser).
  5. Las 9.324 unidades incluyen 69 chunks con id repetido en 4 TOs. Son colisiones de
     numeración (`BKL-0037`) y no cambian las cifras publicadas.

## 2. Recorrido del ejemplo del préstamo por componente — disponible

- **Ruta y commit:**
  - `reports/u_insumos_cap/recorrido_prestamo.md`, generado por
    `reports/u_insumos_cap/u_insumos_i2.py`;
  - commit `f32f20c` (U-INSUMOS-CAP, etapa I2; mandato
    `docs/mandatos/UINSUMOS_CAP_escritura.md`, firmado en `30f106c`);
  - comando: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_insumos_cap/u_insumos_i2.py`;
  - doble corrida byte a byte idéntica, y una re-corrida independiente de la mesa
    también idéntica. El script se detiene si falla cualquier afirmación que el `.md`
    escribe como texto fijo.
- **Qué contiene:** el paso del ejemplo `cla::5.1.1.1` → `cla::3.7` por trece
  componentes: E0, E1, E3, extracción final, E2, E4, esqueleto, referencias y
  procedencia de r1, grafo final, agente, juez, atribución A0.2 e indicadores de cita.
  Para cada uno, el artefacto con ruta y línea o id, o NO ENCONTRADO, y una línea con
  lo que el ejemplo muestra. Incluye las dependencias con las cuatro figuras del
  ejemplo.
- **Alimenta:**
  - capítulo 4: el pipeline, componente por componente, y las figuras del ejemplo
    (`docs/tesis/figuras/LEEME_figura_*.md`);
  - **uso posible en el capítulo 4:** el mismo punto extraído por dos generaciones
    del pipeline, como ilustración de la construcción por etapas (ver la salvedad 2).
- **Salvedades:**
  1. Los datos son de KG-Reextraído-r1 (`0226e947…`), construido con el esquema v2.
  2. En KG-Tanda0-Desarrollo-r1 el ejemplo tiene otra estructura: 2 Condicion, 1
     Definicion y 1 Operacion, sin `limita` ni remisión al 3.7 (recomputado por la mesa
     el 30/09). En r1 son 2 Restriccion y 1 Operacion, con 2 `limita` y la remisión.
  3. La remisión de r1 al 3.7 sale de la paráfrasis del nodo (descripción y
     `umbral`), no del texto de E0.
  4. E4, juez, atribución A0.2 e indicadores de cita son NO ENCONTRADO:
     - E4 no toca el ejemplo;
     - la corrida del agente sobre el ejemplo fue sin juez;
     - A0.2 exige el veredicto de cada traza;
     - los indicadores de cita se calculan solo sobre las trazas de EV2.
  5. Los sha de los LEEME de figuras que cita el recorrido son los del árbol de
     trabajo al correr I2, y coinciden con los commiteados en `e6e6021`.
  6. Después de la re-extracción de la tanda 0 (U-REEXT-T0), estos datos siguen
     siendo de r1, salvo que se regeneren (tablero, fila del test del ejemplo).

## 3. Umbrales (U-UMBRAL) — disponible

- **Ruta y commit:**
  - `reports/u_umbral/`: `u1_mediciones.json` y `.md` (U1, commit `e81ed69`);
    `u2_muestra_trazas.json` y `.md`, `muestra_limita_30.csv` y `reporte_u_umbral.md`
    (U2, commit `e4d053b`);
  - mandato `docs/mandatos/UUMBRAL_investigacion.md`, firmado en `30f106c`;
  - comandos: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_umbral/u_umbral_u1.py`
    y `… reports/u_umbral/u_umbral_u2.py`. Dobles corridas byte a byte idénticas, y
    re-corridas independientes de la mesa también idénticas;
  - lectura de la muestra de 30 aristas `limita`: `reports/u_umbral/lectura_limita/`
    (U-LECTURA-LIMITA, commit `bf4709d`; mandato
    `docs/mandatos/ULECTURA_LIMITA_lectura_asistida.md`, firmado en `67a9e6b`). Comando:
    `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_umbral/lectura_limita/conteo_lectura.py`.
    Doble corrida byte a byte idéntica, y re-corrida de la mesa también idéntica.
- **Qué contiene:**
  - seis mediciones sobre umbrales en los tres grafos (desarrollo, r1 y diez):
    literalidad de `umbral` y `plazo`, tablas que E0 no marca, cuantías sin campo, un
    prototipo de llenado en código, aristas `limita` y trazas;
  - la evidencia ordenada en dos ejes, dónde vive el umbral y cómo se llena, con la
    propuesta como par (representación, método de llenado) y su alternativa
    (`reporte_u_umbral.md`);
  - la precisión de `limita` en KG-Tanda0-Desarrollo-r1: 21 «sí», 7 «no» y 2 «no
    decidible» de 30, con los errores de destino y sus tipos (base, finalidad,
    consecuencia, supuesto) y los ponderadores de riesgo modelados como Restriccion
    (`resultado_lectura_limita.md`);
  - la orientación de la autora para L-ESQ-R2 está registrada en el plan (fila B2.11,
    unidad 5).
- **Alimenta:**
  - capítulo 3: dónde vive el umbral, justificado por los documentos (umbrales
    frecuentes, a menudo relativos a otro valor y a veces varios en un mismo punto);
  - capítulo 4: cómo se llena (E1 copia el tramo literal; la normalización y la
    verificación contra E0 y el parser de tablas son código).
- **Salvedades:**
  1. Los denominadores de U-UMBRAL salen del [c14] del mandato (605 en desarrollo, 638
     en r1, 682 en diez). En la tesis se citan los del tablero corregido: 606, 639 y
     683. La diferencia es un nodo, «diez (10) años».
  2. EV2 se usa como diagnóstico, sobre 8 criterios con cuantía, no como resultado
     (principio 7 del plan).
  3. La muestra de 30 aristas `limita` se leyó en la unidad 4b del plan
     (U-LECTURA-LIMITA, `bf4709d`). Es una lectura asistida: leyó una instancia de modelo y
     revisó la autora, sin cambios. Es un desvío declarado respecto de la lectura humana. La
     instancia es `claude-opus-5-5` (Claude Opus 5.5), confirmado por la autora el 30/09 con el
     registro de la sesión de Claude Code `deda25f2-7092-4eb5-acd8-56ae8d1fba91.jsonl`. Es una fracción
     sobre n = 30, de un solo grafo y sin criterio fijado de antemano, así que se cita como
     dato descriptivo y como fracción cruda.
  4. El costo del llenado por un modelo es una estimación no verificada.

## 4. Listas cerradas y lo no mapeable (U-LISTAS-NOMAP) — disponible

- **Ruta y commit:**
  - `reports/u_listas_nomap/`: `n1_inventario.json` y `.md` y `muestra_forzados_30.csv`
    (N1, commit `9c5331c`, generados por `u_listas_n1.py`); `diseno_listas_nomap.md`
    (N2, commit `acc310e`);
  - mandato `docs/mandatos/ULISTAS_NOMAP_diseno.md`, firmado en `30f106c`;
  - comandos: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_listas_nomap/u_listas_n1.py --out-dir reports/u_listas_nomap`,
    y el comando de cifras derivadas al pie del diseño. Doble corrida byte a byte
    idéntica; re-corridas de la mesa también idénticas.
- **Qué contiene:**
  - el inventario de las listas cerradas en el crudo de E1 (r1 y tanda 0), con su
    paso por el validador y su llegada al grafo;
  - los sujetos: propuestos, posibles forzados, literalidad de la mención y la
    re-resolución contrafáctica;
  - las omisiones y la diferencia entre los dos catálogos;
  - el diseño: política por campo, mención del sujeto con verificación en dos niveles,
    resolución en código, registro de no mapeados y omisiones con categoría.

  La orientación de la autora para L-ESQ-R2 sobre las siete decisiones del diseño está
  registrada en el plan (fila B2.11, unidad 5).
- **Alimenta:**
  - capítulo 3: cómo trata el esquema lo que no encaja en sus listas;
  - capítulo 4: la resolución de sujetos en código, el registro de no mapeados y las
    omisiones.
- **Salvedades:**
  1. La proyección de menciones que fallarían la verificación (del orden de 1.171 sobre
     4.099 en el crudo de diez) sale de los sujetos propuestos y no es representativa
     de las menciones del catálogo. La tasa real la mide U-PROMPT-R2 o U-REEXT-T0.
  2. Es un diseño: nada está implementado.
  3. Las cifras se leen por nivel (crudo del primer intento, entrada de E2 y grafo); por
     ejemplo, «otra» en Obligacion.tipo es 1.398 de 2.365 en el crudo de diez y 1.411 de
     2.367 en el grafo.
  4. La muestra de 30 posibles forzados está sellada y sin leer; quién la lee lo decide
     la autora.

## 5. Mantenimiento: empalme de un subgrafo re-extraído (U-MANT) — disponible

- **Ruta y commit:**
  - `data/experiment/mantenimiento/`: `procedimiento_empalme.md`, `code/empalme_subgrafo.py`,
    `demo_empalme_dirigida.json` y `demo_empalme_renumeracion.json` (M2, commit `7ed5ced`);
    `tabla_reprocesamiento.md` (M1, commit `e18d616`);
  - mandato `docs/mandatos/UMANT_mantenimiento.md`, firmado en `36edf24`;
  - comando: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/mantenimiento/code/empalme_subgrafo.py dirigida --trabajo <dir fuera del repo> --out <json>`.
    Doble corrida byte a byte idéntica; la re-corrida de la mesa del 02/10/2026 también.
- **Qué contiene:**
  - el empalme dirigido reconstruye los 6 `kg.json` sellados de la tanda 0 (`kg.json` y
    `r1/kg.json` de los tres ensamblados) a partir de la salida base y de las tres unidades de
    cap re-extraídas, sin llamar a la API (`demo_empalme_dirigida.json`, clave
    `kg_iguales_al_sellado`);
  - el procedimiento: cómo se identifican las unidades cambiadas, qué se re-extrae, cómo se
    sustituyen las salidas, qué se re-ensambla y qué se controla después;
  - la tabla de qué obliga a reprocesar y qué no;
  - la corrida del control contra el sitio del 02/10/2026 (M3, commit `98400e5`;
    `control_sitio/corridas/2026-10-02/resumen_corrida.json`, `pedidos.json` y
    `clasificacion_cambios.json`): en los 25 días desde la corrida del 07/09/2026 cambiaron 19
    de los 157 TOs, y 23 difieren del corpus congelado; el sitio responde a los pedidos
    condicionales: de 157 pedidos de PDF, 138 volvieron con 304 y 19 con 200;
  - el ejemplo de la tesis no cambió en el sitio entre mayo y octubre de 2026: el TO de
    Clasificación de deudores difiere del congelado en las páginas 1, 10, 44, 50 y 57
    (`clasificacion_cambios.json`, entrada `cladeu`), y `cla::5.1.1.1` y `cla::3.7` están en
    las páginas 16 y 14, con su herencia en la 16 y la 9
    (`data/experiment/reextraccion_v2/e0_chunking/salida_tanda0/chunks_cla.json`).
- **Alimenta:** la sección de mantenimiento de la tesis.
- **Salvedades:**
  1. Es una demostración en seco sobre una re-extracción ya hecha, con los perfiles
     existentes. La actualización real de un TO que cambió en el sitio es de U-SUBGRAFO.
  2. Las unidades que solo cambian de número se re-extraen; renumerarlas en código es una
     propuesta que pide laudo (plan, B2.11, unidad 13).
  3. Las dos cifras de cambio son de ventanas distintas y no se combinan: 19 es desde el
     07/09/2026; 23 es contra el corpus congelado, descargado entre el 07 y el 10/05/2026 (los 5 de
     desarrollo) y el 13/08/2026 (los 152; `docs/fe_erratas_fecha_corpus_congelado.md`).
  4. El control compara y avisa; no actualiza el corpus. El corpus congelado se mantiene para
     la re-extracción y la evaluación (decisión de la autora del 02/10/2026; plan, B2.11,
     unidad 11).

## 6. Segmentación oficial con e0-r2 de los 152 TOs (U-SEG-OFICIAL) — pendiente

- **Ruta y commit:** NO EXISTE todavía. Mandato en borrador,
  `docs/mandatos/USEG_OFICIAL_segmentacion_e0r2.md`; plan, B2.11, unidad 15 (`docs/plan_tesis.md:404`).
  Se genera después del cierre de U-R2-CODIGO-2, que cambia e0-r2.
- **Qué va a contener:** la E0 de los 152 TOs con su manifiesto (qué TOs se segmentan por punto y
  cuáles van por la vía de páginas) y las cifras de la segmentación, cada una con su archivo, su
  clave y su comando.
- **Alimenta:** la sección 4.1 de la tesis. Hasta que exista, sus cifras no se toman de la
  segmentación legada (`data/experiment/segmentacion_84/b584_particion/`) ni de la escalera de R5 de
  U-R2-CODIGO, que corrió en el scratchpad (`data/experiment/r2_codigo/r5_freno.md`, §D).
- **Disparador de escritura (VSEG41, 03/10/2026).** Cuando la segmentación oficial quede commiteada,
  se corre una verificación de solo lectura sobre ese artefacto que recomputa las cifras de la sección
  4.1 marcadas [AL CIERRE: e0-r2] en el .tex. La verificación lista, por cada marca:
  1. la marca, con su frase;
  2. la cifra que corresponde;
  3. el campo del manifiesto o del archivo de donde sale;
  4. el comando que la reproduce.
- **Salvedades:**
  1. Las marcas están en la fuente de Overleaf. Desde el repo no se ven: `grep -rn "AL CIERRE" docs/tesis/`
     da vacío el 03/10/2026. Su cantidad y su texto quedan NO VERIFICADOS hasta esa verificación.
  2. No se registra en el tablero de correcciones (`docs/tablero_correcciones.md`), que es por síntoma
     del grafo.
