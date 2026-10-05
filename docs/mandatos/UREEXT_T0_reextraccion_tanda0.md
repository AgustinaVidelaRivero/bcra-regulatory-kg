BORRADOR — PENDIENTE DE FIRMA

MANDATO — U-REEXT-T0: RE-EXTRACCIÓN DE LOS DIEZ TOs DE LA TANDA 0 CON EL PERFIL r2b, GATE DE r2b Y PRIMERA
LECTURA DE LA COLA HUMANA.
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar, y docs/decisiones_caching_extraccion.md antes de
tocar cualquier llamada al modelo: sus cinco decisiones son vinculantes.
- Unidad en CINCO ETAPAS, T1 a T5, con FRENO obligatorio al final de cada una: reporte corto (no más de 40
  líneas) y espera del «seguí» escrito de la autora.
- Costo de API: solo en T2, con tope de USD 72 para E1 a E3 de los diez TOs (decisión de la autora del
  04/10/2026, tras el FRENO P3b-2 de U-PROMPT-R2, y mantenido por la autora tras el FRENO P4; antes era
  USD 69; docs/plan_tesis.md:400). Fuera de T2, USD 0 y ninguna llamada a la API. Si la proyección de T2
  pasa el tope, se frena y se reporta: el tope no se sube solo.
- PRECONDICIONES, todas commiteadas por la autora: de U-PROMPT-R2, P4 (pareada), P3c (el ajuste del prefijo
  y del mensaje, con el prefijo re-congelado y los candados de F04b, F22, F22b y F23) y su prueba corta
  P4b; y el cierre de C2 de U-R2-CODIGO-2 (código y `salida_tanda0_r2b/`). Si falta alguna, frená sin
  escribir.
- Caché: la base de la prueba pareada de P4 no se reutiliza en esta unidad (decisión de la autora del
  04/10/2026).
- Corpus: el congelado. No se actualiza ningún PDF (decisión de la autora del 02/10/2026, plan `:400`).

CONTEXTO, con sus anclas.
- Qué es: E1 a E3 de los diez TOs de la tanda 0 (pro, cla, ric, cap, ext, ctacte, lingob, polcre, pagjub y
  docvig) con el prefijo nuevo, sobre la e0-r2 que deja C2, y sus ensamblados r2b. Es la release r2b: de ella
  dependen la tanda 1 (docs/checklist_pre_escalado.md:60-66) y la columna «r2b» del tablero
  (docs/tablero_correcciones.md, 26 filas).
- Manifiestos r2b: data/experiment/reextraccion_v2/manifiestos/tanda0_10tos_r2b.json,
  tanda0_ens_diez_r2b.json y tanda0_ens_desarrollo_r2b.json (`20b7f60`). Hoy apuntan a
  `e0_chunking/salida_tanda0_r2`, y el primero trae el tope anterior, de USD 69.
- Referencias de costo: E1 a E3 de los diez TOs con el prefijo sellado costó USD 40,35 (plan `:400`). Con
  el prefijo de P3b-2 (`3817de475c93`), la pareada de P4 midió el prefijo, la entrada y la salida. La
  re-estimación central queda entre USD 45,00, con la salida ponderada por estrato, y 49,41, sin ponderar;
  por el factor 1,4, entre 63,00 y 69,17 (data/experiment/prompt_r2/p4/salida/costo_real_p4.json; la de
  P3b-2 era 50,74 y 71,04). Es la estimación del prefijo de P4. El de P3c cambia el texto: la proyección de
  T1 usa la salida que mida P4b.
- Gate: docs/laudo_release_r2_pipeline.md, §3.1 (puntos 1 a 8), y docs/protocolo_entre_tandas.md, §1 y §4,
  con su enmienda 3 sobre las clases de reprocesamiento
  (docs/enmienda3_protocolo_entre_tandas_2026-10-04_clases_de_reprocesamiento.md, FIRMADA el 04/10/2026).
- Textos firmados que rigen acá: L-ESQ-R2 (`4ef7650`) con sus enmiendas 2 (`5f9a731`), 3 (`8d01b04`) y 4
  (`5c58f38`); la enmienda 5, sobre la negación y el comparador pegado a la cuantía, FIRMADA por la autora
  el 04/10/2026 (data/experiment/esq/enmienda5_L-ESQ-R2_negacion_y_comparador_pegado_2026-10-04.md; commit
  de la firma PENDIENTE); la
  enmienda al protocolo sobre la cola humana (`8d01b04`) con su nota (`0b98045`).

T1 — PREPARACIÓN EN SECO Y SUITE (USD 0).
1. Manifiestos r2b: `rutas.e0_salida` pasa a data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b/;
   los sellos, a los del prefijo re-congelado; y el tope global, a USD 72. Es el primer paso de la unidad
   (decisión de la autora del 04/10/2026).
2. Control de las entradas: el hash y el sha256 del prefijo y el del tool schema contra los candados de
   P3c de U-PROMPT-R2, la etapa que re-congela el prefijo; el sha256 de cada archivo de
   `salida_tanda0_r2b/` contra el cierre de C2; el candado del catálogo; el commit del código.
   - Candados de los insumos que no entran al hash del prefijo (decisión de la autora del 04/10/2026): la
     lista de tablas forzadas a residual (F04b), las líneas fijas del mensaje de E1 (F22 y F22b) y las
     NOTAS de E3 (F23). Los pone P3c de U-PROMPT-R2. T1 solo los verifica: que los módulos cargan con sus
     sha256 esperados y que en el selftest de claves las variaciones R29, R29b, R30 y R32 dan «frena».
   - `e1_extractor/selftest_prompt_r2b.py` lee `salida_tanda0_r2/` y exige que ninguna unidad lleve
     `herencia_recortada` (`:118` y `:148-149`). Al pasar a `salida_tanda0_r2b/`, ese caso cambia: la única
     unidad con el recorte es `ric::11.2.3`, y su mensaje lleva la línea del recorte una vez. El archivo se
     suma a las escrituras de la unidad solo para ese caso.
   - Los scripts de `data/experiment/medicion_r2a/` que importan `reglas_comparacion` o `r1_referencias`
     dan otras cifras con el código de C2. No se vuelven a correr acá: sus salidas selladas son de r2a.
   - Rol de alcance: nueve de los diez TOs lo tienen en `rol_por_to_r2.json` (seis con rol propio y tres con
     clase). Docvig no lo tiene, por el laudo de B5.4 (`docs/laudo_B5.4_fase1_catalogo.md:20-22`): se extrae
     sin línea de alcance, como en r2a, y se declara. En r2a tuvo 20 relaciones con sujeto, 17 resueltas por
     la sugerencia del modelo y 3 en cuarentena.
   - Unidades grandes de `salida_tanda0_r2b/`, para la corrida en seco: `cap::4.2.1.2` (26.726 caracteres
     propios), `ric::11.2::intro` (15.051), `cap::3.1.14.1` (12.101) y `cap::4.3.3.1` (10.981). Con el
     prefijo sellado, las tres de cap dieron 11.925, 8.371 y 9.212 tokens de salida: superan los 8.192 del
     primer intento y entran en el reintento de 16.384. Si alguna corta también en el reintento, solo
     `cap::4.2.1.2` se puede partir por ítems.
     Con la salida que midió P4 con el prefijo de P3b-2 (1,175 tokens por carácter de texto propio: mediana
     de 6 unidades de 3.109 a 9.825 caracteres, de 0,224 a 1,498), en el reintento entran unos 13.944
     caracteres, y 10.937 con el máximo. Por esa cuenta quedan fuera `ric::11.2::intro`, que no se puede
     partir, y `cap::4.2.1.2`: se parte en dos, de 15.056 y 11.669 caracteres, la parte mayor también pasa
     de 13.944 y una parte no se vuelve a partir. Las otras dos quedan en el borde. Es una cota: la razón
     baja con el tamaño (con el prefijo sellado, las tres de cap dieron 0,46, 0,69 y 0,84). Por su salida
     sellada y el crecimiento medido en P4 (×1,276 en el conjunto y hasta ×1,58 en las unidades de 3.000
     caracteres o más, sin `ric::9.2.1`), `cap::4.2.1.2` daría entre 15.200 y 18.900 tokens. La corrida en
     seco lista las cuatro, con el mecanismo que cubre a cada una.
3. Corrida en seco, sin llamar a la API: el request de cada unidad, su namespace y su clave de caché; las
   unidades por TO; la estimación por TO contra el tope; los namespaces de los reintentos.
4. Suite y shapes antes del gate:
   a. T6 y E4-b se parametrizan por los TextoOrdenado de los TOs del manifiesto del grafo bajo prueba, en
      lugar de los cinco de desarrollo fijos (scripts/regression_kg.py:1304-1313; E4-b depende de T6);
   b. la shape informativa «cuantía en la descripción ⇒ elemento en la lista» (L-ESQ-R2 §1.5);
   c. la entrada de la suite que fija las dos firmas nuevas de `condicion_de` (→ Operacion y → Potestad),
      con el conteo de relaciones no verificadas por E3, que tiene que ser 0 (L-ESQ-R2 §6.5);
   d. una entrada por cada id nuevo decidido, leída contra su chunk (L-ESQ-R2 §7.5);
   e. el control que exige cero elementos de extracción sin verificar, con la especificación del FRENO P3 de
      U-PROMPT-R2 (data/experiment/prompt_r2/freno_p3.md, A3, seis puntos; `4aa92c7`). Lee el conteo del
      reporte del ensamblado r2b (punto s de C2). La cola humana es la excepción explícita y se cuenta aparte.
   f. un test por punto para `BKL-0001` (`cap::2.8.3.3`) y para `BKL-0002` (`ext::3.5.3`), como T1 lo es de
      `BKL-0024`: el contenido que tiene que estar sale del expediente del retriage
      (data/backlog/expediente_retriage_v3.md, E1 y E2). Decisión de la autora del 04/10/2026.
   Los selftests de la suite y de las shapes corren sobre una copia. En las entradas ya selladas de la
   fixture cambian solo T6 y E4-b.
5. Entrada de la suite para los grafos r2b: el estado esperado, ítem por ítem, propuesto para que la autora
   lo selle ANTES del gate de T3 (laudo de r2, §3.1, punto 2). `BKL-0004` (la enumeración del 6.5 de
   Clasificación) persiste en r2a sin corrección dirigida: si persiste en r2b, entra al estado esperado como
   falla conocida, con su evidencia.
6. Las 15 preguntas de control: un script versionado que repite el procedimiento de la revisión independiente
   (reports/u_revision_libre/freno_a.md:70-72; `54f57cd`). Primero reproduce su resultado sobre
   KG-Tanda0-Diez-r2a: 8 bien, 2 en parte, 3 con algo falso y 2 sin respuesta. Si no lo reproduce, se declara
   la diferencia pregunta por pregunta.
FRENO T1.

T2 — EXTRACCIÓN, E1 A E3 (tope USD 72).
- Perfil r2b, los diez TOs, en el orden del manifiesto. Salida nueva en
  data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b/ (se crea).
- Con lo que traen P3b-2 y C2: el reintento por salida de E1 mal formada; los veredictos de E3 que llegan
  como texto, leídos en código; el reintento con menos elementos, marcado; la marca de la copia de la nota.
- Registro del modelo de cada llamada. Costo real contra el estimado, por etapa y por TO.
- Contadores: vocabulario retirado, que tiene que ser 0; unidades por estado final; unidades sin validación,
  listadas; unidades con cada marca de E3 (`lectura_veredicto_e3`, `reintento_con_menos_elementos` y
  `copia_nota_e3`); salidas mal formadas y sus reintentos; unidades que cortan en el primer intento, en el
  reintento y las partidas por corte, con sus tokens de salida; las unidades que usan el tercer escalón del
  reintento (P3c-2 de U-PROMPT-R2), con su marca; las omisiones `meta_normativo` cuyo tramo trae una marca
  de alguna de las siete clases de la enmienda 7 a L-ESQ-R2 (deber, prohibición, facultad, condición,
  excepción, alcance y modalidad), con las tres subclases de modalidad (contador de `validador_r2`, decisión
  de la autora del 04/10/2026); y los tokens de salida por carácter de texto
  propio de todas las unidades (decisión de la autora del 04/10/2026): la mediana, el percentil 90 y el
  máximo por tramo de tamaño del texto propio; aparte, las unidades de 3.000 caracteres o más (con el
  prefijo sellado, mediana 0,86 en 40 unidades; en P4, 1,175 en 6) y, una por una, las de 10.000 o más. Con
  esa medición se recalcula la capacidad del reintento (docs/checklist_pre_escalado.md, condición 12).
- Control de la caché de E3 (decisión de la autora del 04/10/2026). El namespace de E3 del perfil r2b es el
  de la tanda 0. Se cuentan los aciertos de caché de E3 contra entradas anteriores a la corrida
  (`created_at` anterior a su inicio). Se espera 0; si hay alguno, se lista con su unidad y su clave.
FRENO T2.

T3 — ENSAMBLADOS, REGISTRO Y GATE DE r2b (USD 0).
1. Dos ensamblados r2b, diez y desarrollo, en corpus_tanda0/ens_diez_r2b/ y ens_desarrollo_r2b/ (se crean).
   Doble corrida byte a byte idéntica, y el sha256 de cada `kg.json`.
2. Gate (laudo de r2, §3.1), con la entrada de la suite ya sellada por la autora:
   - shapes: `scripts/shapes_validator.py --perfil r2 --fase r2b --e0 <salida_tanda0_r2b>`;
   - suite: `scripts/regression_kg.py --perfil r2 --esperado scripts/regression_kg_esperado.json`; 0
     regresiones;
   - contadores de E1; intrínsecas de generación 3 e indicadores de cita, informativos;
   - reproducibilidad: los tres ensamblados r1 se reproducen byte a byte. Los dos r2a ya no dan los sha256
     sellados (`99fe2bfa…` y `93a7af72…`): con el código de C2 cambian los umbrales y las `remite_a` que su
     cierre declara, y el control es contra los sha256 que deje ese cierre (decisión de la autora del
     04/10/2026). Los sellados siguen en el repo y se reproducen con el código de `f8dedd4`, que es el
     commit con el que la tesis cita sus cifras. Los selftests siguen en verde;
   - nunca EV2;
   - la columna «r2b» del tablero de correcciones, con el comando de cada fila.
3. Controles propios de esta unidad, cada uno con su comando y su cifra:
   a. cero elementos de extracción sin verificar, con la cola humana aparte (T1, punto 4.e);
   b. el criterio de la remisión del ejemplo: al menos una arista `remite_a` desde un nodo anclado en
      `cla::5.1.1.1` hacia uno anclado en `cla::3.7` (enmienda 2 de L-ESQ-R2, §9; checklist `:64`);
   c. la condición 10 de la tanda 1: el nodo de la Excepcion de `cla::5.1.1.1` existe, y desde los nodos de
      `cla::5.1.1::intro` se llega a los de sus hijos por la jerarquía de la procedencia, sin agente
      (checklist `:81`);
   d. el cierre de `BKL-0035` y de `BKL-0039`, medido sobre la extracción final, después de E3: ningún nodo
      de `ctacte::8.3::intro`, `ctacte::8.4::intro` ni `ctacte::6.4.7::intro` es una Obligacion cuyo contenido
      sea solo el encabezado de la lista (data/backlog/backlog.jsonl, `condicion_de_cierre`);
   e. el vínculo entre unidades, forma A: cuántas Condicion de incisos quedan sin `condicion_de` con destino
      en el encabezado de un ancestro (con la matriz congelada eran 36 de las 56 sin `condicion_de`, sobre 458);
   f. ningún elemento de umbral con `comparacion_asumida`, y los plazos sin marcador contados (enmienda 3);
   g. los diez TextoOrdenado con su versión y su materia;
   h. `omisiones.jsonl` del ensamblado y LN-7;
   i. las aristas derivadas que tocan un nodo que solo viene de la cola humana, contadas aparte;
   j. ninguna Operacion junta más de un punto;
   k. las claves `modalidad`, `consecuencia`, `modalidad_clasificada` y `copia_nota_e3` de
      `properties_no_definidas`, contadas aparte de las demás;
   l. los mini-chunks que empiezan a mitad de oración con un tramo de dos segmentos, contados: la
      verificación en orden de lectura cubre solo el tramo simple (límite declarado en el FRENO P3b-2).
   Controles del backlog (decisión de la autora del 04/10/2026, tras el recuento de las 39 entradas):
   m. el cierre de `BKL-0032`, `BKL-0033` y `BKL-0036`, cada uno con su condición de cierre leída contra su
      chunk: `docvig::3.3::cierre` (polaridad de la excepción), `ctacte::7.3.1.5` (ninguna Obligacion de la
      baja en la Central con `aplica_a` hacia el banco) y `lingob::2.3.2.2` (la Operacion conserva el
      calificador «en condiciones más favorables…»);
   n. `BKL-0038`: el conteo de las aristas `limita` y `prohibe` por `coherencia_tipo_predicado` en los dos
      grafos r2b (en r2a, 4 `limita` incoherentes en cada uno), y la lectura de los 3 chunks de esas 4
      aristas, `cap::6.2.1.4`, `ext::3.5.6.6` y `cap::4.3.3.1`, que dice en cada una si está mal el tipo o el
      predicado;
   o. los ocho patrones de asignación de sujeto, `BKL-0009` a `BKL-0016`, leídos caso por caso sobre el grafo
      r2b contra sus chunks (data/backlog/expediente_retriage_v3.md, T1 a T8; el remedio de cada uno, en
      data/experiment/prompt_r2/diseno_prefijo_r2.md, §6.2). Es el insumo del laudo de B2.4;
   p. `BKL-0028`: la re-adjudicación del miembro del rol de ctacor (nota del 01/10/2026 en el backlog);
   q. `BKL-0021`: si el registro de no mapeados de r2b trae la mención de la entidad nominada por el
      importador; si no la trae, se cierra como «no reaparece» en el laudo de B2.4;
   r. `BKL-0031`: el detector de casi duplicados (data/experiment/r2_codigo/r4_detector_casi_duplicados.py)
      corrido sobre los dos grafos r2b, como dato para la revisión de fusionados posterior a esta unidad.
4. Registro de los dos grafos en data/experiment/neo4j/grafos.py y carga en Neo4j local (precedente:
   `cf6ca42`). Se controla que la marca de la cola humana de los nodos llega.
FRENO T3. La autora sella los grafos.

T4 — LECTURA DE LA COLA HUMANA Y PREGUNTAS DE CONTROL (USD 0 de API).
1. Cola humana, primera medición (enmienda al protocolo del 04/10/2026 y su nota): si la cola de los diez
   TOs tiene más de 30 unidades, se sortean 30 con la semilla declarada antes de leer; si tiene 30 o menos,
   se leen todas. Lectura asistida con revisión de la autora. Unidad con error: al menos un nodo o una
   relación que el texto de la unidad no sostiene; las omisiones se reportan aparte. Se reporta el intervalo
   de Wilson al 95 % y se aplica la regla: 25 % sobre el límite superior con muestra, o 10 % sobre la tasa
   observada con la cola entera.
2. Las 15 preguntas de control sobre KG-Tanda0-Diez-r2b, con el script de T1: el cambio, pregunta por
   pregunta. No son evaluación ni se reportan como resultado.
3. Copia de la nota de E3. `copia_nota_e3` marca una posible copia: no afirma que lo sea. Los casos
   marcados en esta corrida se leen con la regla de data/experiment/prompt_r2/p3b2/regla_lectura_copia_nota.md,
   fijada antes de leer, y se reporta cuántos son copias reales. Referencia: sobre el crudo de r2a, 11 de 45.
   Si la precisión sigue baja, la regla se ajusta en código entre tandas: no en esta unidad.
4. Unidades con la marca del tercer escalón del reintento (decisión de la autora del 04/10/2026). Se leen
   todas, no una muestra: la extracción de cada una contra el texto de su unidad, con el mismo criterio de
   error de la cola humana, y aparte lo que E3 no reclamó. Se reporta cuántas son, cuántas tienen error y
   cuántos tokens de salida usó cada una. Con ese número la autora decide si hace falta algo para el
   escalado. No entran a la muestra de la cola humana por llevar la marca.
FRENO T4.

T5 — REPORTE (USD 0).
- Costos, cifras del gate, la columna «r2b» del tablero y los controles de T3, cada cifra con su comando.
- Lo que sigue a esta unidad, sin hacerlo: la lectura de confirmación de `condicion_de` → Operacion y →
  Potestad; la medición de la `remite_a` estructural (30 aristas, piso de Wilson 0,75) y del lado del
  destino, después de la unidad que atribuye `remite_a` por tramo; la alternativa de unión de las
  operaciones por encabezado (30 uniones, piso 0,75); la recuperación por tramo de lo que el reintento dejó;
  la prueba de R2 de U-RERESOL-CAT sobre este crudo; y la mejora condicionada del sujeto por alcance
  (decisión de la autora del 04/10/2026): en un documento con alcance, una norma sin mención recibe
  `aplica_a` hacia el rol de alcance de su documento, como relación derivada y marcada como tal. Entra solo
  si supera el piso de precisión: 30 relaciones leídas, con el límite inferior de Wilson en 0,75 o más (28
  correctas de 30). Pide enmienda a L-ESQ-R2 §3.
- Claves de la caché (decisión de la autora del 04/10/2026, tras el freno de U-TABLA-REPROC):
  - se vuelve a correr data/experiment/mantenimiento/code/selftest_clave_cache.py con
    `--salida-r2b data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b`, sobre una copia: es el anclaje
    del perfil r2b (A1r y A3r), que hoy da NO_VERIFICABLE porque no hay claves de r2b en las dbs. Si la E0 de
    la corrida no es `salida_tanda0_r2b/`, cambia también la constante `E0_TANDA0_R2B` del selftest;
  - el §5 de data/experiment/mantenimiento/tabla_reprocesamiento.md reemplaza el costo de referencia
    estimado del perfil r2b (E1 USD 0,010544 y E3 USD 0,010333 por unidad) por la tarifa observada en esta
    corrida, con su comando;
  - en las filas F05, F10 y F14 de la tabla, «enmienda en curso» pasa a citar la enmienda 3 del protocolo
    entre tandas, firmada el 04/10/2026.
FRENO T5, final.

ESCRITURAS: los tres manifiestos r2b; corpus_tanda0/salida_r2b/, ens_diez_r2b/ y ens_desarrollo_r2b/;
scripts/regression_kg.py, scripts/shapes_validator.py y sus selftests, solo para el punto 4 de T1;
scripts/regression_kg_esperado.json, solo con la entrada que selle la autora; data/experiment/neo4j/grafos.py,
solo las dos entradas nuevas; docs/tablero_correcciones.md, solo la columna «r2b»; una carpeta de la unidad,
data/experiment/reext_t0/ (se crea), para frenos, scripts y reportes; data/experiment/mantenimiento/
tabla_reprocesamiento.md (solo el §5 y la cita de la enmienda en F05, F10 y F14), selftest_clave_cache.json
(la salida) y, solo si cambia la E0, la constante del selftest; y el scratchpad.
PROHIBIDO: editar el prefijo, el tool schema, la cadena de E0 a E5 o los validadores (si un control falla
por el código, se reporta y no se corrige acá); tocar las salidas y los grafos sellados de r1 y de r2a;
correr EV2 o cualquier celda con agente; usar las 15 preguntas como evaluación; actualizar el corpus;
commitear.

DECISIONES DE LA AUTORA AL FIRMAR.
1. El tope de T2: queda en USD 72 (decisión de la autora del 04/10/2026, tras el FRENO P4).
2. Si las celdas con agente de la tanda 0 se vuelven a correr sobre los grafos r2b (referencia: USD 21,2577;
   propuesta: no en esta unidad).
3. Las carpetas de salida (propuesta: `salida_r2b/`, `ens_diez_r2b/`, `ens_desarrollo_r2b/` y
   `data/experiment/reext_t0/`).
4. Si el registro y la carga en Neo4j van en esta unidad (propuesta: sí, en T3).
5. La semilla del sorteo de la cola humana.

PENDIENTE DE COMPLETAR ANTES DE LA FIRMA, con lo que cierren las unidades en curso.
- De P3c-2 de U-PROMPT-R2 (data/experiment/prompt_r2/freno_p3c2.md, corregido; commit PENDIENTE al
  04/10/2026): lo que T1 controla. Reemplaza a lo de P3b-2 (`c8c3970`: hash `3817de475c93`).
  - El prefijo: hash `322c5a23e9b7`, sha256 `ccffa4e3…`, 59.909 caracteres y 27.840 tokens medidos. El
    parche de P3c tiene sha256 `5e3761c1…` y se aplica sobre el prefijo de P3b-2 (`8d84364f…`).
  - El namespace de E1: `e1_extraccion|cv=e1-extractor-v1-p322c5a23e9b7|think=0`.
  - El tool schema no cambia (`0c391f2b…`). El prefijo de E3 y su namespace tampoco (`21a836c7de6d`).
  - Los candados de lo que no entra al hash del prefijo:
    - la lista de tablas forzadas a residual, con `cap::tabla037`: sha256 `98cc96b2…`;
    - el mensaje de E1: fixture `candado_mensaje_r2b.json`, sha256 `4d69f7f4…`, y mensaje `a9cb702c…`;
    - el mensaje de E3: fixture `candado_mensaje_e3.json`, sha256 `e8fa5dc4…`, y mensaje `da17c22e…`.
  - El tercer escalón del reintento: techo de 40.960 tokens, marca `escalon_3` en el registro de E1 y en su
    resumen, y error definitivo `max_tokens_hit_tras_escalon_3`.
  - Los contadores nuevos del validador: `omisiones.meta_normativo_con_marca`, con sus siete clases y las
    tres subclases de modalidad (opción, consejo y forma), `omisiones.tramo_solo_heredado` y
    `omisiones.tramo_orden_de_lectura`.
  - En el manifiesto, las unidades con tabla serializada confiable pasan de 37 a 36, por `cap::6.2.2.6`.
  La fase le llega a E2 por el parámetro `fase` de `ensamblar_r2`.
- De P4b de U-PROMPT-R2: la salida por carácter y el crecimiento de la salida con el prefijo de P3c, para
  la proyección de T1; y si ese prefijo emite la Excepcion de `cla::5.1.1.1` (condición 10 de la tanda 1,
  pendiente hasta P4b).
- De C2 de U-R2-CODIGO-2: el sha256 de cada archivo de `salida_tanda0_r2b/` y de los `pies_<to>.json`; los
  cambios declarados de ric; el namespace del reintento por salida mal formada; las claves del reporte del
  ensamblado para las omisiones, las aristas derivadas de la cola y el conteo de lo que pasó por E3; y las
  marcas de E3 en el reporte (punto t). Y los sha256 de los dos grafos de la cadena r2a con el código de su
  cierre, para el control de reproducibilidad de T3. En su freno corregido del 04/10/2026 son `70d51e42…`
  (diez) y `fa4c1043…` (desarrollo), verificados en su revisión; se confirman con el commit de C2.
- El commit de la firma de la enmienda 5 a L-ESQ-R2.
- De P4 de U-PROMPT-R2 (data/experiment/prompt_r2/freno_p4.md, sin commit al 04/10/2026): hecho. El prefijo
  de P3b-2 no emite la Excepcion de `cla::5.1.1.1`, y la autora decidió ajustar el prompt antes de esta
  unidad (P3c y P4b). La clasificación de la modalidad detectó 2 recomendaciones y ninguna consecuencia. El
  costo real fue USD 1,1086, de un tope de 2.
- El commit del código con el que corre la unidad.

REQUISITOS: los de CLAUDE.md §4 (a a l), con PYTHONDONTWRITEBYTECODE=1 y .venv/bin/python -B; verificaciones y
selftests sobre una copia sin enlaces, con el sha256 de los archivos del repo antes y después; fuentes
firmadas leídas en el commit de su firma; todo conteo recomputado contra su artefacto; cero nombres de
personas.
