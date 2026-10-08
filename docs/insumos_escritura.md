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

- **Ruta y commit:** NO EXISTE todavía. Mandato firmado por la autora el 05/10/2026,
  `docs/mandatos/USEG_OFICIAL_segmentacion_e0r2.md`; plan, B2.11, unidad 15 (`docs/plan_tesis.md:404`).
  Se genera después del cierre de U-R2-CODIGO-2 (`9f6361e`), que cambia e0-r2.
- **Qué va a contener:** la E0 de los 152 TOs con su manifiesto (qué TOs se segmentan por punto y
  cuáles van por la vía de páginas) y las cifras de la segmentación, cada una con su archivo, su
  clave y su comando.
- **Alimenta:** la sección 4.1 de la tesis y las cifras que la tesis toma de la segmentación fuera de
  esa sección (punto 4 de S2 del mandato): las unidades por conjunto, los puntos y el porcentaje de
  terminales por clase de documento, y los documentos que toman el primer nivel como sección o no son
  segmentables. Por la nota del 05/10/2026 al pie del mandato (`2bfda2a`), también: la lista de las reglas
  de segmentación vigentes en e0-r2, con los documentos que usa cada una, para rehacer la tabla de reglas
  de la tesis (4.d); y las unidades por grupo de documentos, con documentos y páginas, más lo que queda
  fuera del grafo según las enmiendas a las adendas 1 y 2 del laudo B5.5 (4.e). Por la tercera nota al
  pie del mandato, del 05/10/2026, también el resultado de la lectura de cortes contra el PDF y el del
  censo de renglones fuera de toda unidad (4.f). De la lectura, la cifra que cita la tesis es la
  estimación ponderada por modo de lectura, con su intervalo; la cota sin ponderar sobre las 90 unidades
  es la del piso, y no es la que representa al corpus. Las definiciones de ese
  punto, la de «clase de documento» incluida, se fijan contra el texto vigente del capítulo 4 antes de
  despachar S2; hoy esas cifras salen de la partición legada
  (`reports/u_insumos_cap/estadisticas_corpus.md` y `reports/u_cap3_datos/datos.md`). Hasta que el
  artefacto exista, las cifras de la sección 4.1 no se toman de la segmentación legada
  (`data/experiment/segmentacion_84/b584_particion/`) ni de la escalera de R5 de U-R2-CODIGO, que corrió
  en el scratchpad (`data/experiment/r2_codigo/r5_freno.md`, §D).
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
  3. **Un compromiso, no un hecho (05/10/2026).** El capítulo 4 afirma que los bloques de texto corrido de
     los documentos no segmentables ingresan al grafo al ensamblar el corpus escalado (el texto está en
     Overleaf y no se ve desde el repo). Hoy ningún grafo tiene esas 77 unidades de prosa, y su procedencia
     por página existe solo en `data/experiment/cobertura_bloque_a/chunks_a2.json` y
     `a2_salida/extracciones_a2.jsonl`. El documento de cifras de esa unidad lo dice
     (`data/experiment/cobertura_bloque_a/cifras_vigentes.md:12-17`): lo escribible es «medido y adjudicado,
     pendiente de ingreso». El ingreso es de U-BLOQUE-A, condición de entrada de la tanda 3
     (`docs/plan_tesis.md:772`; decisión de la autora), con mandato a redactar después de U-REEXT-T0. Hasta
     que esa unidad cierre, la frase es un compromiso: se revisa en la versión final de la tesis.
  4. **Lo que cambia en el capítulo 4 con S0 de U-SEG-OFICIAL (05/10/2026).** Son cifras del prototipo de
     S0-1 (`3920323`; `data/experiment/segmentacion_oficial_e0r2/FRENO_S0-1.md`), reproducidas por la
     revisión sobre una copia. Se confirman con la corrida oficial de S1:
     - ri_spi deja de ser no segmentable: pasa de 1 unidad a 95, por su marcador de letra y número;
     - los documentos no segmentables pasan de 12 a 11, y sus páginas, de 161 a 150 (ri_spi tiene 11);
     - el primer grupo, el de los documentos escritos en puntos, incluye dos con páginas fuera de toda
       unidad: ri_cc (pp. 2 a 47) y ri_tsa (pp. 3 a 61), 105 páginas en total. Entran por la vía de página
       con la tanda 3 (`docs/plan_tesis.md:772`).

## 7. Re-extracción de la tanda 0 con el perfil r2b (U-REEXT-T0) — pendiente

- **Ruta y commit:** en curso. Mandato firmado por la autora el 05/10/2026 (`docs/mandatos/UREEXT_T0_reextraccion_tanda0.md`,
  `e2027dd`, con sus notas al pie); extracción en `3d793aa`, `4ab7a0a` y `ad99ac7`; ensamblados r2b de T3 en `c499eb3`
  (`data/experiment/reextraccion_v2/corpus_tanda0/ens_{diez,desarrollo}_r2b/`), con el gate sin pasar y una vuelta
  T3-bis aprobada el 06/10/2026 (nota al pie del mandato). Los grafos finales se sellan después de T3-bis.
- **Qué va a contener para la tesis:** las cifras de la re-extracción (costo, estados, la reparación acotada como
  procedimiento con su cifra: 12 salidas mal formadas en 8 unidades, 6 resueltas con un reintento, 2 reparadas, 0
  agotadas; nota del 06/10/2026, `5527178`), el gate de r2b y lo que la suite y las shapes dijeron de él.
- **Insumos ya decididos** (06/10/2026):
  1. **El tramo literal frente a la descripción** (decisión de la autora sobre el FRENO T3). El ítem RT-C6-1/2 de la
     suite muestra el papel de las dos capas del nodo: la norma (`pro::1.1.2.5`) dice «excepto que se trate de
     asociaciones mutuales **o** cooperativas, por las financiaciones que otorguen»; la descripción de la Excepcion que
     extrajo E1 con el perfil r2b dice «las asociaciones mutuales **y** cooperativas, en lo que respecta a las
     financiaciones que otorguen»; su `tramo` (la cita textual que E1 guarda y E3 verifica contra el texto) conserva el
     «o». La fidelidad al texto se audita en el tramo; la descripción es la lectura del modelo, y puede cambiar un
     conector sin que el tramo lo haga. Se declara como desviación de fidelidad del modelo en la descripción, con el
     alcance igual (cada clase queda exceptuada) y el tramo fiel. Fuentes: `docs/mandatos/UREEXT_T0_reextraccion_tanda0.md`
     (nota del 06/10/2026 sobre el FRENO T3, decisión 3) y el freno de T3-bis cuando exista.
  2. **Dos hallazgos de T4, material para el experimento posterior de comparación de modelos** (06/10/2026; lecturas de la
      instancia con segunda lectura de la mesa y adjudicación de la autora, `04cec96` y `c9d4c40`;
      `data/experiment/reext_t0/freno_t4.md`, `freno_t4_tramo2.md` y `t4/salida/tasas_t4.json`). (a)
     Omisiones `meta_normativo` con contenido normativo según el §1 de la enmienda 7: en la muestra de 30 sin marca del
     contador, 19 de 30 son normativas (14 de 30 sin contar las remisiones puras) y 4 tienen el tramo en el texto
     heredado; en la de 30 con marca, 27 de 30 (adjudicación de la autora), 18 con el tramo heredado y 3 habilitantes. Proyectadas a las 1.137 omisiones `meta_normativo` del ensamblado r2b de diez (733 sin marca y 404
     con marca; `t4/salida/sorteos_t4.json`), las normativas sobre el tramo propio son 390,9 [264,9; 511,4] con las remisiones o 268,8
      [160,3; 399,4] sin ellas en las 733 sin marca, y 134,7 [77,7; 206,9] en las 404 con marca; las del tramo heredado van
      aparte: 340,1 (97,7 más 242,4). Wilson al 95 %; `t4/salida/tasas_t4.json`, punto 8. (b) Una Condicion por supuesto:
     1 de 30 unidades del grupo c cumple el criterio sellado; en 26 de 30 unidades hay al menos un supuesto dentro de
      una norma (recontado sobre los 137 supuestos con la adjudicación de `ext::4.1.3.2`), y en la mayoría de ellas otros supuestos sí quedan como Condicion con su relación. Medida por supuesto
     del segundo tramo (`t4/salida/tasas_t4.json`, 137 supuestos de la fase A, clasificación de la instancia con
     segunda lectura de la mesa y adjudicación de la autora del 06/10/2026): 43 de 137 son Condicion con su relación
     hacia la norma que condicionan (Wilson al 95 %: 0,242–0,396), 77 de 137 van dentro de una norma (0,478–0,642), 7
     fusionados, 2 omitidos y 8 sin relación; las enumeraciones de la fase A se cuentan por miembro. Los dos miden lo que el modelo de E1 hace con el prefijo congelado:
     son la línea de base de la comparación con otro modelo, y lo que se pueda corregir en código entre tandas se
     declara aparte de lo que queda como límite del modelo.
  3. **El vínculo entre unidades, forma A, como límite declarado** (decisión de la autora del 06/10/2026). En el grafo r2b de
     la tanda 0 (diez TOs, `a9631a64`), 42 de 715 Condicion de ítem conservan la norma que condicionan en el encabezado de un
     ancestro, sin arista hacia ella (0,059; Wilson al 95 % [0,044; 0,078]; control 3.e de T3 de U-REEXT-T0,
     `data/experiment/reext_t0/t3bis/salida/controles_t3bis.json`, `e_forma_A`; referencia con la matriz congelada: 36 de las
     56 sin `condicion_de`, sobre 458). El grafo no deriva esa arista: el enlazador estructural que propuso U-DIAG-PROCESO
     (VU-B) dio en r2a 13 de 23 con predicado tipado y 45 de 76 con `remite_a`, bajo el piso 0,75 (U-DIAG-VINCULO, `b0ee084`);
     la lectura la resuelve la navegación por la jerarquía de la procedencia (condición 10 del checklist). Complemento
     pendiente, sin plazo: la lectura de precisión de los 42 casos (cuántos tienen de verdad la norma en el encabezado).
  4. **El verificador de E3 y los ítems de lista: límite declarado de la tanda 0** (decisión de la autora del 06/10/2026, opción (ii)
     con (iii), tras U-DIAG-E3-LISTAS; reporte y propuesta en `reports/u_diag_e3_listas/`). En la tanda 0, 1.054 de las 2.440 unidades
     verificadas son ítems de una lista; el fuente que recibió E3 lleva solo los bloques heredados de tipo encabezado
     (`e3_verificador/comun_e3.py:123-125`), así que en 1.015 ítems el bloque que abre la lista no llegó ni al texto ni a la verificación
     de citas, y ningún ítem recibió la regla de composición (la NOTA va solo al encabezado, `prompt_e3.py:315-316`). Efecto medido:
     31 reclamos que piden en el ítem la norma del encabezado, que el prefijo de E1 manda no emitir ahí (16 bloqueantes); 5 reclamos de
     polaridad, ninguno fundado; 9 de 15 falsas alarmas de contenido agregado en una muestra con semilla (Wilson al 95 % [0,357; 0,802]);
     17 reintentos y 7 unidades de la cola humana (5 de las 29 `cola_humana`) por esos reclamos; 2 errores reales de composición que
     siguen en pie (`pro::4.2.1.4`, `lingob::7.1.7`). Los ítems son 1.054 de 2.440 unidades pero 50 de las 74 de la cola. La tanda 0 no
     se re-verifica (principio 9; la clase es «E3 de las afectadas» y se corrige entre tandas): la corrección rige desde la tanda 1
     (U-E3-LISTAS: el bloque que abre la lista en el fuente y en las citas de E3, y una NOTA del ítem), y la medición aparte (O3 de esa
     unidad: E3 corregido sobre las 20 unidades afectadas, sin re-sellar) da cuántos reclamos desaparecen y cuántas de las 17
     extracciones finales cambió un reintento infundado, comparadas con su intento 0. Cifras de O3 (07/10/2026; USD 0,238 en 20
     llamadas; `data/experiment/e3_listas/freno_o3.md`, cifras en `data/experiment/e3_listas/o3/resumen_o3.json`; las 20 son 17 con
     reintento por esos reclamos y 7 en la cola, 4 en los dos grupos, lista sellada `cc6b0cd6…`): (a) primera verificación con E3
     corregido, con la extracción que vio E3 en la tanda 0: de los 21 reclamos P, C, B y B2 del intento 0 (3 C, 16 B, 2 B2) desaparecen
     18 y persisten 3 por la regla sellada antes de contar (`o3/criterio_o3.md`), 15 y 6 por la lectura; aparecen 3 nuevos (un C, un B
     y un B2; el C, leído, es el reclamo viejo de `docvig::3.3.2`, que viene del cierre del punto y no de la lista); 11 de las 20
     unidades salen completas y 16 de las 20 se aceptarían sin reintento (14 de las 17 que reintentaron); van al reintento
     `ext::3.6.4.1` (reclamo B que, leído, es una falsa alarma contra la NOTA), `ext::3.16.2.1` (reclamo B fundado: el tramo es una
     facultad del texto propio del ítem, no la norma del encabezado; adjudicación de la autora del 07/10/2026, que corrige la lectura
     sellada de O3) y `ext::3.18.1.1` (reclamos de composición fundados), y a la cola `docvig::3.3.2`; residuo de falsas alarmas
     bloqueantes: 1 (`ext::3.6.4.1`), y `ext::3.6.4.2` conserva el mismo reclamo, medio y sin bloquear.
     (b) De las 17 extracciones finales, 13 son el reintento y las 13 cambiaron
     respecto del intento 0 (entran 58 entidades y 40 relaciones, salen 26 y 7, cambian de descripción 5); las 4 cuya final es el
     intento 0, control, sin cambios; en 11 de las 13 el E3 corregido acepta el intento 0. (c) La norma del encabezado vuelta a
     emitir en el ítem (conteo por código, D3): 1 de las 20 unidades en el intento 0 y 8 en la final; las 7 nuevas son finales del
     reintento con un reclamo B en el intento 0. D1 (el bloque en el fuente de las citas): de los 14 faltantes nuevos, 6 verifican su
     cita solo por D1 y 2 de ellos bloquean, los dos en `ext::3.18.1.1` y de composición, no la norma del encabezado: el riesgo
     declarado de D1 no aparece en las 20.
     **O5, el caso resuelto en la NOTA del ítem, se probó y no se adoptó** (decisión de la autora del 07/10/2026; USD 0,241 de un tope
     de 0,50, en las mismas 20 unidades, una corrida por unidad; `data/experiment/e3_listas/freno_o5.md`, cifras en `o5/a/cifras_o5.json`):
     - Con el criterio sellado, el residuo de O3 desaparece: ningún reclamo cita ya el bloque declarado `[meta_normativo]`, el control
       `ext::3.16.2.1` conserva su reclamo fundado y en las otras 17 no hay bloqueantes nuevos.
     - Pero la lectura muestra otro reclamo B bloqueante en `ext::3.6.4.1` (pide la excepción compuesta, contra C5b y C7 de la NOTA), y
       `ext::3.6.4.2` suma una falsa alarma de polaridad, ajena a la lista.
     - Los bloqueantes son 5, como en O3, y las falsas alarmas bloqueantes pasan de 2 a 3.
     - Con una corrida por unidad no se separa del ruido; cuesta unos USD 0,62 más por corrida del tamaño de la tanda 0; y seguir
       ajustando sería calibrar el verificador contra su propio control.
     - El mensaje de E3 queda con el candado de O4 (`079d2489…` / `66bc8656…`). El residuo de `ext::3.6.4.1` queda como límite declarado
       del verificador.
     **Límite declarado de la tanda 0 y hallazgo para la tesis (decisión de la autora del 07/10/2026):** en la tanda 0, el verificador
     reclamó en los ítems de lista normas que están en el encabezado (reclamos P, C, B y B2 que P3C-d1 y d2 no piden extraer en el ítem);
     esos reclamos falsos dispararon reintentos y 13 de las 17 extracciones finales del grupo afectado son el reintento, distinto del
     intento 0 (entran 58 entidades y 40 relaciones, salen 26 y 7): en 11 de las 13, el verificador corregido (NOTA del ítem, D1 y D2)
     habría aceptado el intento 0; y la norma del encabezado aparece repetida en el ítem en 8 de las 20 unidades de la extracción final,
     contra 1 en el intento 0. El grafo evaluado de la tanda 0 (`e22fae1a…`) conserva esas extracciones: no se re-verifica ni se re-extrae
     (principio 9, enmienda 5); el límite se declara con estas cifras, y desde la tanda 1 rige el verificador corregido (`7fe848c`). Para la
     tesis: un reclamo falso del verificador no es inocuo, cambia la extracción (reintento con feedback) y puede duplicar normas.
  5. **Tasa de error por unidad de las aceptadas de la tanda 0** (U-LECTURA-ACEPTADAS, L2 del 07/10/2026; reporte
     `data/experiment/lectura_aceptadas/reporte_l2.md`, cifras en `estimadores_l2.json`; L0 y L1 en `6e611d6`). Método: 30
     unidades por estrato (ítems de lista y no ítems), sorteadas con semilla sellada antes de leer entre las 2.366 aceptadas
     del grafo evaluado sin la cola (`e22fae1a`), leídas con el criterio de T4 por la instancia y a ciegas por la mesa (el
     mismo veredicto en las 60) y adjudicadas por la autora. Tres cifras: (i) por unidad, ítems 6 de 30 (Wilson al 95 %
     [0,095; 0,373]) y no ítems 4 de 30 ([0,053; 0,297]); ponderada con W₁ = 1.003/2.366, la tasa del grafo, 0,162 ± 0,093
     ([0,069; 0,254]; conservador por los límites de Wilson, [0,071; 0,329]), frente a 12 de 30 en la cola ([0,246; 0,577],
     `data/experiment/reext_t0/t4/salida/tasas_t4.json`); (ii) `remite_a`: 0 de 167 no sostenidas por cita y destino, en 11
     unidades; (iii) tipos documentales mal asignados, como observación y no como error: 4 nodos `Comunicacion` en 2
     unidades (dos puntos del mismo TO y dos leyes). Es la línea de base de la vigilancia por tanda del pre-registro de la
     tanda 1 (reporte, §8).
  6. **Vínculos que faltan en la tanda 0: Excepcion y Condicion sin su regla, por causa, como límite declarado** (U-DIAG-CAP3-GRAFO,
     `df59e79`; decisiones de la autora del 07/10/2026).
     - **Cuánto.** En el grafo de diez de la tanda 0 (`a9631a64`) hay 256 Excepcion sin `exceptua` ni `exceptua_obligacion` y 331
       Condicion sin `condicion_de`; en el sin cola, 252 y 322. Fuente: `reports/u_diag_cap3_grafo/REPORTE_UDIAG_CAP3_GRAFO.md`, tarea
       a.1, con lectura de 393 casos con criterio escrito antes y una relectura a ciegas que coincide en 22 de 25 en la causa.
     - **Por causa** (Excepcion + Condicion):
       - (i) la regla está en otra unidad: 77 + 89, de ellas 49 y 60 en ítems de lista;
       - (ii) la regla es una Operacion: 48 + 0 (41 relaciones rechazadas por firma antes de E3 y 7 no emitidas);
       - (iii) emitida, y caída por otro rechazo: 31 + 122;
       - (iv) nunca emitida, con la regla en la unidad: 49 + 49;
       - (v) no une a una regla (sobre todo, acotan una definición): 51 + 71.
     - **Decisiones.**
       - (i): la unión ítem–encabezado (regla E) no entra antes de la tanda 1, porque su precisión es 18 de 30 (Wilson [0,423; 0,754]),
         bajo el piso de 0,75. Queda como límite declarado. Una regla más estrecha se fija por escrito y se mide en una unidad propia,
         en paralelo con el escalado; si pasa, entra antes de sellar el grafo de la evaluación final.
       - (ii): límite declarado en la tanda 0; desde la tanda 1, según la enmienda 8 a L-ESQ-R2, condicionada a la lectura de las 41.
       - (iii), (iv) y (v): límite declarado.
     - **Forma A.** La declarada el 06/10 se sostiene: 60 de 953 Condicion de ítem en (i), del orden de 42 de 715 (con bases distintas,
       declaradas en el reporte).
     - **Lo que sí se corrige en código antes del re-sellado único:** la procedencia por tramo (G-r, en U-OMISIONES-COD). Cambia el
       punto de 22 nodos y solo el rol de 173, con 0 fusiones; 22 de 22 coherentes en la lectura.
