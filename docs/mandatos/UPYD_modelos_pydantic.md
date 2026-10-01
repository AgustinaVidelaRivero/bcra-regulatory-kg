FIRMADO por la autora — 2026-10-01

MANDATO — U-PYD: MODELOS PYDANTIC, POLÍTICA POR CAMPO Y VALIDADOR DEL PERFIL r2.
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar.
- Unidad en DOS ETAPAS, con FRENO obligatorio al final de cada una: reporte corto (no más de
  40 líneas) y espera de la revisión y del «seguí» escrito de la autora. P2 no arranca sin él.
- Costo de API: USD 0. Ninguna llamada a la API; Neo4j no se usa; sin red.

CONTEXTO. Plan, fila B2.11, unidad 7 (docs/plan_tesis.md:396), habilitada: L-ESQ-R2 firmada
(`4ef7650`) y U-CAT-UNICO cerrada (`bd2122d`). Checklist X12; alimenta W13 (corrección del
párrafo de la sección 3.4 de la tesis, que hace la mesa de escritura con lo implementado).
- Hoy el validador de E1 rechaza por tipo, predicado, `sujeto_id` y firma, pero no controla
  Restriccion.tipo, Comunicacion.tipo, las claves ni los valores de las properties, y descarta
  algunas cosas sin registro (reports/u_listas_nomap/diseno_listas_nomap.md, §0).
- L-ESQ-R2 decide el esquema de la release r2 y asigna a esta unidad (§12):
  - la política por campo (§2);
  - la verificación de la mención del sujeto (§3) y de las omisiones (§5);
  - el control de coherencia entre el tipo de la Restricción y su predicado (`BKL-0038`, §1.1);
  - la implementación de las reglas de comparación de los umbrales (§1.3, punto 3);
  - las mediciones que el laudo dejó para esta unidad.
- La unidad construye un módulo único de modelos y un validador en un perfil nuevo. Los
  perfiles y los prompts sellados no se editan. La conexión del perfil al runner, a E2 y al
  ensamblado es de U-R2-CODIGO (unidad 8); el prompt es de U-PROMPT-R2 (unidad 10).

Leé completos, antes de escribir una línea:
- data/experiment/esq/enmienda_L-ESQ-R2_2026-09-30.md (FIRMADA en `4ef7650`): §0.2, §1.3 a §1.5,
  §2, §3, §5, §6.4, §9 y §12, y las notas posteriores a la firma;
- reports/u_listas_nomap/diseno_listas_nomap.md: secciones a (P-a0 a P-a10), b (P-b1 a P-b4),
  e (P-e1 a P-e3), f y g (selftests con los valores reales de N1);
- reports/u_listas_nomap/n1_inventario.json: claves `resumen_por_lista`,
  `grupos.<g>.capas.<capa>.fuera`, `sujeto_propuesto_literal`, `omisiones` y `entradas` (las
  rutas y sha256 del crudo);
- data/experiment/reextraccion_v2/e1_extractor/validador_e1.py (`validar_salida`, :89) y
  prompt_e1.py (`TOOL_SCHEMA_E1`, :268-335);
- data/experiment/catalogo_unico/generados_r2/ (enums, labels, rol por TO, catálogo de la suite;
  `bd2122d`);
- reports/u_estudio_matriz/uestmat_reporte_U-ESTUDIO-MATRIZ.md, tabla del punto 1, filas P01 y
  P02 (relaciones nuevas en la primera pasada de E1);
- los casos de control de las reglas de comparación (L-ESQ-R2 §1.3, punto 3): el texto de E0 de
  `cla::5.1.1.1` (docs/tesis/figuras/ejemplo_prestamo_datos.json, `textos`) y las filas 9, 15 y
  21 de reports/u_umbral/lectura_limita/lectura_limita_30.csv;
- la regex de cuantía del comando [c14] de docs/tablero_correcciones.md y el prototipo de U-UMBRAL
  (reports/u_umbral/u_umbral_u1.py).

DECISIONES YA TOMADAS. No se re-deciden.
1. Un módulo único de modelos Pydantic: salida de E1 por tipo de entidad, relación, omisión y
   elemento de umbral, y nodo y arista del grafo. De los mismos modelos se generan el tool schema
   y los enums (plan, :396).
2. La política por campo es una tabla de configuración versionada (campo → modo, más las tablas
   de alias), con su sha256 registrado en cada corrida. El valor original se guarda siempre
   (L-ESQ-R2 §2.3).
3. Valores cerrados (L-ESQ-R2 §1.3, §2.3, §5.3, §6.3):
   - Obligacion.tipo con sus seis valores;
   - Restriccion.tipo sin valor nuevo;
   - Comunicacion.tipo con «A», «B», «C» y «externa»;
   - `comparacion` con siete valores: máximo inclusivo, máximo estricto, mínimo inclusivo,
     mínimo estricto, igual, coeficiente y `no_determinada`;
   - `unidad`: porcentaje, moneda con su código, días (corridos o hábiles), meses, años, «veces»
     y UVA;
   - frecuencia: diaria, semanal, mensual, trimestral, semestral y anual;
   - omisiones con cinco categorías;
   - la matriz con `condicion_de` → Operacion y → Potestad.
4. Alias aceptados: los de forma para tipos y predicados, y `exceptua_restriccion` → `exceptua`.
   No hay renombres de claves.
5. La mención del sujeto se verifica en dos niveles (subcadena normalizada y tokens dentro de una
   ventana) y nunca se rechaza la relación por la mención (L-ESQ-R2 §3).
6. Las reglas de comparación están definidas por su sentido en L-ESQ-R2 §1.3, punto 3. La
   implementación exacta y su calibración son de esta unidad, con los cuatro casos de control
   como prueba obligatoria.
7. `shapes_validator.py` sigue solo con stdlib, como control independiente. El catálogo r2 de
   U-CAT-UNICO se lee, no se edita.
8. **Confirmado por la autora en la firma (01/10):** las shapes del perfil nuevo (S3 con la matriz ampliada, S18
   reescrita, S24 a S29) las escribe U-R2-CODIGO junto con la suite, y no esta unidad, para que
   el control independiente no lo escriba la misma unidad que el validador.

P1 — Modelos, política y validador del perfil r2. USD 0.
a. Módulo de modelos: data/experiment/pyd_r2/code/modelos_r2.py. Cubre:
   - las entidades de los nueve tipos con sus properties (L-ESQ-R2 §0.2 con los cambios de §1 y
     §2): la lista de umbrales (tramo, valor, unidad, comparación y base) en Restriccion,
     Obligacion, Condicion y Excepcion, y la frecuencia en Obligacion;
   - las relaciones, con `sujeto_mencion` y `sujeto_id` como sugerencia del modelo;
   - las omisiones, con categoría, tramo y nota;
   - el nodo y la arista del grafo, con las marcas (`fuera_de_lista`, `properties_no_definidas`,
     `mencion_verificada`, `comparacion_asumida`, la marca de no verificada por E3 y la de
     coherencia tipo–predicado).
b. Política: data/experiment/pyd_r2/politica_campos_r2.json, con los modos de P-a0 a P-a10, las
   tablas de alias de la decisión 4 y su sha256.
c. Validador del perfil r2: data/experiment/pyd_r2/code/validador_r2.py. Aplica la política y
   devuelve el resultado con contadores. Incluye:
   - el control de `BKL-0038`, como marca y sin rechazar;
   - la matriz ampliada, con la marca de no verificada por E3 en las relaciones que la matriz
     congelada rechazaba (L-ESQ-R2 §6.4);
   - la verificación de la mención en dos niveles;
   - la validación del tramo de las omisiones (P-e2) y la conversión de tipos rechazados en
     omisiones `fuera_de_tipos` (P-e3).
d. Reglas de comparación: data/experiment/pyd_r2/code/reglas_comparacion.py, por el sentido de
   L-ESQ-R2 §1.3, punto 3. Las cuatro reglas de forma son coeficiente, raíces, negación general
   (con cero a tres palabras en el medio) y compuestas. Encima rigen la adyacencia (con «mínimo» o
   «máximo» seguidos de la cuantía), la precedencia y el caso sin marcador.
e. Generación: data/experiment/pyd_r2/generados/tool_schema_r2.json y los enums, desde los modelos
   y desde el catálogo r2.
f. Selftest data/experiment/pyd_r2/code/selftest_pyd_r2.py, con:
   - los valores reales de N1 de la sección g del diseño, cada uno con su modo esperado según la
     política;
   - las reglas de comparación por sentido, la precedencia, la adyacencia (con «capital mínimo»
     como negativo) y los cuatro casos de control obligatorios:
     - el préstamo → mínimo estricto, con su base;
     - la fila 9 → máximo inclusivo;
     - la fila 21 → máximo inclusivo, sin disparar coeficiente;
     - la fila 15 → mínimo inclusivo;
   - un negativo de la raíz «super-»: «Superintendencia» no es marcador;
   - el control de `BKL-0038` y la marca de no verificada por E3;
   - el tool schema generado: un elemento válido pasa y uno con un valor fuera de lista queda
     marcado, no descartado.
g. requirements.txt: se agrega `pydantic==2.13.4`, la versión ya instalada en el .venv. No se
   instala nada.
FRENO P1:
- el resultado del selftest por grupo;
- la política con su sha256;
- el tool schema generado, con su sha256;
- el sha256 de lo escrito.

P2 — Prueba sobre el crudo guardado de la tanda 0, y mediciones. USD 0.
a. Lector del crudo v3: data/experiment/pyd_r2/code/lector_crudo_v3.py. Lee el primer intento de
   E1 (`extracciones_e1_compact.jsonl`, `tool_input_crudo`) y los reintentos de E3
   (data/experiment/reextraccion_v2/e3_verificador/cache/e1_reintentos.db, solo con
   `file:…?immutable=1`), con las rutas y sha256 de `n1_inventario.json`, `entradas`.
   - `sujeto_propuesto` se lee como mención.
   - Cada cadena de `omisiones_no_prosa` se lee como omisión sin categoría ni tramo.
b. Corrida del validador r2 sobre r1 y los cuatro grupos de la tanda 0 (desarrollo, cinco, diez).
   Salida: data/experiment/pyd_r2/resultados/prueba_crudo_t0.json y .md, con:
   - los valores fuera de lista por campo y su tratamiento;
   - normalizaciones, alias aplicados y `properties_no_definidas`;
   - las marcas de `BKL-0038` y la mención verificada por nivel;
   - las omisiones `fuera_de_tipos`;
   - las relaciones recuperadas por la matriz ampliada, marcadas como no verificadas por E3.
c. Controles de reproducción. Cualquier diferencia no explicada es FRENO.
   - Los valores fuera de lista del crudo coinciden con N1 (`resumen_por_lista`). Lo que cambia
     por las listas r2 (por ejemplo, «externa» en Comunicacion.tipo) va en una tabla de
     reconciliación, valor por valor.
   - Las relaciones recuperadas coinciden con U-ESTUDIO-MATRIZ, columna de primera pasada (P01 y
     P02).
   - Ningún elemento que el validador v3 aceptaba se pierde en silencio: se acepta, se normaliza
     con contador o se marca.
d. Mediciones que el laudo dejó para esta unidad:
   - **Ventana de la verificación por tokens** (nivel 2 de la mención), sobre los 63 propuestos
     del crudo de diez (N1). Se mide la tasa de falsas aceptaciones contrastando cada mención con
     el texto de otro chunk del mismo TO, elegido con semilla fija.
   - **Reglas de comparación:** la frecuencia de cada forma y los falsos positivos de «factor».
     Se proponen el valor y la regla de «igual», que no tiene regla inicial. La población son las
     ventanas de cuantía de las descripciones guardadas, que son la población del par B (regex
     [c14]): los tramos de r2a todavía no existen, porque los produce U-R2-CODIGO después de esta
     unidad. La frecuencia sobre los tramos de r2a se re-mide en la medición r2a (unidad 9).
   - **Largo mínimo del tramo de las omisiones:** con los datos guardados solo hay cadenas
     libres, no tramos. Se propone un valor provisional con su base declarada, y la medición
     definitiva queda para r2b.
FRENO P2, final:
- las tablas de (b);
- los controles de reproducción;
- las tres mediciones con su comando;
- el sha256 de lo escrito.

Commit de la autora.

REQUISITOS TRANSVERSALES (CLAUDE.md §4 a–j), en todas las etapas.
- Escrituras: solo data/experiment/pyd_r2/ (se crea), requirements.txt (una línea) y tu
  scratchpad.
  - No se editan validador_e1.py, perfil_e1.py, prompt_e1.py, los prompts sellados, e2_lib.py,
    scripts/shapes_validator.py, scripts/regression_kg.py, data/experiment/catalogo_unico/, el
    plan, el checklist, el tablero, los laudos ni el backlog.
  - Nada sellado se toca (CLAUDE.md §3). No commitees.
- Python:
  - PYTHONDONTWRITEBYTECODE=1 y .venv/bin/python -B en todo Python.
  - Ningún __pycache__ ni .pyc nuevo: línea de base al inicio (conteo de .pyc) y control al
    cierre.
  - Las dbs de caché solo con `file:…?immutable=1`.
  - Doble corrida byte a byte idéntica de todo lo que la etapa escribe.
- Afirmaciones y citas:
  - Toda afirmación lleva path:línea o comando.
  - Los conteos se recomputan antes de escribirse (§4 i); fracción cruda sobre n chico, sin
    porcentaje.
  - Lo que no esté en un artefacto es NO ENCONTRADO.
  - La tesis no se cita por línea de docs/tesis/main.tex; la fuente es Overleaf.
  - Los mentores solo por rol; cero nombres propios.
- Si algo de este mandato contradice un archivo del repo, mandan los archivos y se reporta la
  contradicción.
- Revisión y checkpoint:
  - Paquete de revisión revision_UPYD_P<n>/ por etapa, con manifest.txt (sha256 y una línea por
    archivo) y nombres únicos.
  - Checkpoint checkpoint_UPYD.md en el scratchpad, actualizado al cierre de cada etapa y antes
    de cualquier compactación.
- Shell zsh: variables entre comillas o como arrays; ningún comentario con # dentro de los
  bloques de comandos para copiar.

CRITERIO DE ACEPTACIÓN por etapa:
- el reporte corto con las salidas pedidas;
- git status --short con solo data/experiment/pyd_r2/ como nuevo y requirements.txt modificado;
- doble corrida byte a byte idéntica de lo que la etapa escribe;
- P1: selftest en verde, con los cuatro casos de control de comparación;
- P2: los tres controles de reproducción en verde o explicados valor por valor, y ningún
  elemento perdido en silencio;
- el grep de convenciones, pegado aunque dé vacío.

FRENO al final de cada etapa.
