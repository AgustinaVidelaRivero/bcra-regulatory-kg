BORRADOR — PENDIENTE DE FIRMA DE LA AUTORA (redactado el 03/10/2026 sobre HEAD `e1c9456`)

MANDATO — U-MED-R2A: MEDICIÓN r2a, EL GRAFO DE LOS DIEZ TOs CON TODO LO CORREGIDO EN CÓDIGO.
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar.
- Unidad en TRES ETAPAS, M1 a M3, en este orden, con FRENO obligatorio al final de cada una:
  reporte corto (no más de 40 líneas), paquete de revisión (CLAUDE.md §4 g) y espera de la
  revisión y del «seguí» escrito de la autora. Ninguna etapa arranca sin él.
- Costo de API: USD 0 en todas las etapas. Ninguna llamada a la API; Neo4j no se usa. No se
  re-extrae nada: todo sale de la salida guardada de E1 y E3 de la tanda 0.
- Toda corrida de control va sobre una copia armada copiando archivos (regla l), con el sha256
  del repo antes y después; las escrituras al repo son solo las enumeradas abajo.

CONTEXTO. Plan, fila B2.11, unidad 9 (docs/plan_tesis.md:398). Habilitada: U-R2-CODIGO cerrada
(`e1c9456`), U-PYD (`57a8dd2`) y U-CAT-UNICO (`bd2122d`) cerradas; L-ESQ-R2 FIRMADA (`4ef7650`)
con sus notas posteriores, y su enmienda 2 (`remite_a`, `5f9a731`).
- Qué mide: la columna «Después de r2: r2a (solo código)» del tablero de correcciones
  (docs/tablero_correcciones.md), fila por fila, con el mismo comando de cada fila. Separa lo que
  corrige el código (esta unidad) de lo que corrige el prompt (r2b, unidades 10 y 11).
- El grafo r2a es el re-ensamblado de los diez TOs de la tanda 0 con el perfil r2 completo:
  e0-r2 (tablas serializadas, pie, K con K-a′+K-b, regla L, escalera), lectura del crudo
  guardado con el modelo r2, fusión sin juntar puntos distintos, resolución de sujetos por
  relación con registro de no mapeados, lista de umbrales (par B) con base resuelta y
  verificación en tabla, `remite_a` por las reglas (a) a (i), `establecida_en` derivada, marcas
  de cola y de E3. Lo que exige el prompt nuevo no entra: mención del sujeto, omisiones con
  categoría, tramo de E1, «externa» en Comunicacion.tipo, tabla del 1.2 leída (L-ESQ-R2 §9,
  columna «r2b»).
- La entrada r2 de la fixture de la suite se sella con este grafo (decisión de la autora del
  02/10/2026; plan :397, cierre de la unidad 8), no con la prueba de desarrollo de U-R2-CODIGO.

Leé completos, antes de escribir una línea:
- la fila de la unidad 9 del plan (:398), con sus agregados (a), (b) y (c) y la fe de erratas
  del 02/10; la fila de la unidad 8 (:397), cerrada;
- docs/tablero_correcciones.md entero: las 26 filas de síntomas de la tanda 0 (:49 a :74), la
  sección de comandos [c1] a [c24] y la definición de las columnas r2a y r2b (:12-16);
- L-ESQ-R2 en su versión firmada (`git show 4ef7650:data/experiment/esq/enmienda_L-ESQ-R2_2026-09-30.md`):
  los apartados «r2a y r2b» (§1.4, §2.4, §3.4, §4.4, §5.4, §6.4, §7.4, §8.4) y el §9; y las
  tres notas posteriores a la firma del archivo actual (§7.3, §1.3 y §1.5, la marca de S18);
- la enmienda 2 de L-ESQ-R2 (`git show 5f9a731:data/experiment/esq/enmienda2_L-ESQ-R2_remite_a_2026-10-02.md`),
  §5 (cómo se cuenta), §7 (efectos) y §9 (criterio para escalar);
- data/experiment/r2_codigo/: r5_freno.md (§A a §H, §R5) y cierre_freno.md (los cuatro puntos y
  las dos definiciones de «cita»); r3_freno.md §3 (la pasada residual de E4, medida y no
  aplicada) y §5 (plazos a `frecuencia`); r3d_remisiones.py (claves `C_diez_cambio_de_destino`,
  `G_reglas_<ens>.h_irresolubles.inexistentes`) y r3_perdidas_remisiones.py;
- el pipeline que se corre, sin editarlo: data/experiment/reextraccion_v2/e0_chunking/correr_e0.py
  (`--version-e0 e0-r2`), data/experiment/tanda0/code/ensamblar_tanda0.py (`--perfil-r2`,
  `--e0-r2`), scripts/regression_kg.py (`--perfil r2`, `--registro-dir`), scripts/shapes_validator.py
  (`--perfil r2`, `--e0`, `--fase r2a`), scripts/remisiones.py, scripts/muestra_aristas_obs12.py;
- los manifiestos data/experiment/reextraccion_v2/manifiestos/tanda0_10tos.json,
  tanda0_ens_diez.json y tanda0_ens_desarrollo.json, y la entrada guardada
  data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/;
- el precedente de lectura asistida: docs/mandatos/ULECTURA_LIMITA_lectura_asistida.md y
  reports/u_umbral/lectura_limita/resultado_lectura_limita.md («Desvío declarado»).

DECISIONES YA TOMADAS. No se re-deciden.
1. El orden es M1 → M3. Las tres etapas cuestan USD 0 y no re-extraen.
2. El grafo r2a se produce con el código de `e1c9456` sin modificarlo. Si una fila del tablero
   no se puede medir con ese código, se declara «no medible en r2a» con la causa; no se cambia
   el pipeline en esta unidad.
3. La E0 e0-r2 de los diez TOs y el grafo r2a se versionan, para que la entrada de la fixture
   apunte a un grafo del repo (la prueba de desarrollo de U-R2-CODIGO quedó fuera del repo y por
   eso no se selló).
4. La entrada r2 de la fixture la propone esta unidad (estado ítem por ítem, con el sha del
   grafo); la sella la autora, que la mueve de `propuesta_r2_sin_sellar` a `estado_esperado`
   (decisión 9 del mandato de U-R2-CODIGO). El sha nuevo de `estado_esperado` se registra en el
   plan.
5. Las lecturas de M3 son lecturas asistidas: las hace la instancia y las revisa la autora; se
   rotulan así en todo artefacto, con el modelo y la versión declarados (precedente de
   U-LECTURA-LIMITA, decisión 1). Las reglas de lectura se fijan antes de leer y no se ajustan.
6. La pasada residual de E4 se mide y no se aplica (perfil r2, R3 de U-R2-CODIGO). Si se retira
   del perfil r2 lo decide la autora con la medición de M3; el cambio, si lo hay, es de otra
   unidad.
7. La regla que manda los plazos sin cuantía temporal a `frecuencia` no se toca antes de
   medirla en los diez TOs (tablero :74). Esta unidad la mide; la decisión es de la autora.
8. S18 del perfil r2 da NO PASA en r2a por los límites relativos sin elemento (nota del
   02/10/2026 a L-ESQ-R2 §1.5): es un resultado declarado, no un freno de esta unidad.

M1 — El grafo r2a. USD 0.
a. E0 e0-r2 de los diez TOs, versionada:
   `correr_e0.py --manifiesto manifiestos/tanda0_10tos.json --version-e0 e0-r2 --salida
   data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2/`. Doble corrida byte a byte
   idéntica. Control: igual a la salida e0-r2 de la batería de cierre de U-R2-CODIGO (47
   archivos; `cierre_freno.md`).
b. Grafo r2a de los diez TOs:
   `ensamblar_tanda0.py --manifiesto manifiestos/tanda0_ens_diez.json --entrada
   corpus_tanda0/salida_dirigida --perfil-r2 --e0-r2 <salida de a> --salida
   data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2a/` (directorio hermano del
   ensamblado sellado `ens_diez/`, que no se toca). Doble corrida: `kg.json`,
   registros (`remisiones_registro.json`, `no_mapeados_sujetos.jsonl`,
   `resolucion_sujetos.jsonl`) y reporte byte a byte idénticos, con la ruta normalizada donde el
   reporte la registra. Nombre del grafo: KG-Tanda0-Diez-r2a. Reportá su sha256, nodos y
   aristas, y los conteos del reporte (`remite_a`, umbrales, no mapeados, no verificadas por E3).
   Control: con el mismo comando y la prueba de desarrollo (`tanda0_ens_desarrollo.json`) se
   reproduce el grafo `93a7af72…` de la batería de cierre; ese grafo no se versiona.
c. Validación del grafo: 0 nodos y 0 aristas fuera del modelo r2 (`modelos_r2`, como en el
   reporte del ensamblado); shapes `--perfil r2 --fase r2a --e0 <salida de a>`, con la salida
   versionada junto al grafo; suite `--perfil r2 --generacion 3 --catalogo
   catalogo_unico/generados_r2/catalogo_suite_r2.json --politica-cuarentena flaggeada
   --esperado scripts/regression_kg_esperado.json`, salida versionada junto al grafo.
d. Control de los sellados (regla de U-R2-CODIGO): con el código de `e1c9456` y los perfiles
   existentes, E0 legada 34/34 y los tres ensamblados sellados byte a byte (los tres reportes con
   ruta, con la ruta normalizada). Selftests del pipeline en verde.
e. Entrada r2 de la fixture, propuesta: en `scripts/regression_kg_esperado.json`, la clave
   `propuesta_r2_sin_sellar` pasa a describir KG-Tanda0-Diez-r2a (ruta en el repo, sha, estados
   de los 56 ítems, evidencia = la corrida de c). `estado_esperado` no se toca: lo mueve la autora
   al sellar (decisión 4).
FRENO M1: sha del grafo y de la E0; conteos del reporte; veredicto de shapes (esperado: NO PASA
solo por S18, con la cantidad de límites relativos); resumen de la suite; la entrada propuesta;
los sellados reproducidos; sha256 de lo escrito.

M2 — La columna r2a del tablero. USD 0.
a. Para cada una de las 26 filas de síntomas (:49 a :74), la medición sobre KG-Tanda0-Diez-r2a
   con el comando de la fila ([c1] a [c24]), y la comparación con «Valor en la tanda 0». Si una
   fila se midió sobre desarrollo o cinco y la comparación lo pide, el mismo código produce el
   grafo r2a de desarrollo en el scratchpad (no se versiona) y la fila lleva los dos valores.
b. Filas que no se miden en r2a, con la causa declarada y sin inventar un valor: las que exigen
   correr al agente (patrones de navegación, tope de herramientas, clases de falla A0.2; USD > 0
   y EV2, fuera de esta unidad); la muestra de la observación (12), que pide una lectura con
   quién lee decidido (P15, Q12); las que exigen el prompt nuevo (mención del sujeto, omisiones
   con categoría), que llevan «r2b» en su celda; el crudo del reintento, que se mide sobre las
   salidas de U-REEXT-T0.
c. Filas con medición propia de esta unidad: «Relaciones de la matriz ampliada sin verificar por
   E3» (conteo por par, marcadas aparte); «Plazos sin cuantía mandados a `frecuencia`» (cuántos
   plazos van a `frecuencia` y cuántos quedan fuera de la lista, por TO); «Cuantías sin campo
   estructurado» (nodos con cuantía en la descripción y sin elemento de umbral, por tipo; los
   límites relativos de S18 aparte); «Test del ejemplo `cla::5.1.1.1`» (el ítem de la suite, con
   (i), (ii) y (iii) y la marca de no verificado por E3); «Regresiones de la suite contra r1»
   (los 56 ítems contra la entrada de r1 y contra la propuesta de M1).
d. Escritura: solo la columna «Después de r2: r2a (solo código)» de cada fila, con la cifra, su
   comando o clave del JSON y la fecha; y, si hace falta un comando nuevo, una entrada [c25] en
   adelante en la sección de comandos. Las demás columnas no se tocan. Todo conteo se recomputa
   contra su artefacto antes de escribirse (CLAUDE.md §4 i).
FRENO M2: la tabla de las 26 filas con su valor r2a o su causa de no medición; la lista de
comandos nuevos; sha256 de lo escrito.

M3 — Lecturas asistidas pendientes. USD 0. Cinco lecturas, cada una con su copia de trabajo
(CSV con las columnas de la muestra más veredicto, justificación y revision_autora vacía), su
script de conteo de solo lectura (doble corrida idéntica) y su regla fijada antes de leer.
a. Cambios de destino de las remisiones, de la paráfrasis al texto de E0 (plan :398, agregado
   a): muestra de 30 nodos de origen sorteados con semilla declarada entre los 732 de diez que
   cambian de destino (`r3d_remisiones.py`, `C_diez_cambio_de_destino`, recomputado sobre
   KG-Tanda0-Diez-r2a). Regla: para cada nodo, el destino por el texto de E0 es el que el texto
   cita («sí»), el de la paráfrasis era el correcto («no»), o el texto no alcanza («no
   decidible»). Con los 141 pares perdidos contra la paráfrasis de desarrollo
   (`r3_perdidas_remisiones.json`, `por_veredicto`), lectura de los 35 «sin lectura».
b. Remisiones a puntos inexistentes en la E0 del TO de destino (agregado c): las 30 de diez,
   completas, con su chunk de origen y su tramo (`G_reglas_diez.h_irresolubles.inexistentes`).
   Regla: inconsistencia de la propia normativa (el punto citado no existe o fue renumerado en
   el texto congelado; caso `cla::3.3.8`), error del detector (el punto existe y la cita se leyó
   mal), o no decidible.
c. Pasada residual de E4 (agregado b): sobre KG-Tanda0-Diez-r2a, cuántos propuestos y cuántas
   resoluciones habría hecho la pasada residual (medida y no aplicada), y lectura de cada
   resolución que proponga: correcta, incorrecta o duda. Insumo de la decisión 6.
d. Plazos mandados a `frecuencia` (tablero :74): todos los de los diez TOs (en cla eran 17, 16
   fuera de la lista). Regla: es una frecuencia («mensual», «cada 30 días»), es un plazo, es
   otra cosa («inmediata», «N/A», «previo a…»). Insumo de la decisión 7.
e. Relaciones de la matriz ampliada marcadas como no verificadas por E3 (L-ESQ-R2 §6.4;
   tablero :71): muestra de 20 por par (`condicion_de` → Operacion y → Potestad), sorteada con
   semilla declarada, leída con la regla de U-ESTUDIO-MATRIZ (correcta, incorrecta, duda) sobre
   el texto de E0. Es una señal temprana y se declara así: no reemplaza la lectura de
   confirmación sobre el grafo de r2b (plan :400), que E3 ya habrá verificado.
   Cada lectura reporta sus conteos con el intervalo de Wilson al 95 % donde la muestra es
   aleatoria, y la lista de los «no», «incorrecta» y «no decidible» con su justificación.
FRENO M3: los cinco conteos con sus intervalos, las listas, la sección «Desvío declarado» de
cada reporte y el sha256 de lo escrito. La revisión de la autora queda fuera de la unidad: si
cambia un veredicto, lo anota en revision_autora y la mesa registra el resultado final.

REQUISITOS TRANSVERSALES (CLAUDE.md §4 a–l), en todas las etapas.
- Escrituras, y solo estas:
  - data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2/ (M1.a, se crea);
  - data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2a/ (M1.b y M1.c, se crea);
  - scripts/regression_kg_esperado.json, solo la clave `propuesta_r2_sin_sellar` (M1.e);
  - docs/tablero_correcciones.md, solo la columna r2a de las filas :49 a :74 y las entradas
    nuevas de la sección de comandos (M2);
  - data/experiment/medicion_r2a/ (se crea): scripts de medición y de conteo, copias de trabajo
    de las lecturas, reportes de las tres etapas, y tu scratchpad.
  - No se editan: el pipeline, la suite, las shapes, los manifiestos, el plan, el checklist, los
    laudos, el backlog, `estado_esperado` de la fixture ni nada sellado (CLAUDE.md §3). No
    commitees.
- Python: PYTHONDONTWRITEBYTECODE=1 y .venv/bin/python -B en todo Python; ningún .pyc nuevo
  (línea de base al inicio, control al cierre).
- Afirmaciones y citas: toda afirmación lleva path:línea o comando; los conteos se recomputan
  antes de escribirse; los documentos firmados se leen en su commit de firma (regla k); lo que no
  esté en un artefacto es NO ENCONTRADO; la tesis no se cita por línea de main.tex; cero
  nombres propios de personas.
- Acciones de la autora (sellar la entrada, commitear, firmar) se escriben como PENDIENTES
  hasta su confirmación (regla j).

CRITERIO DE ACEPTACIÓN. KG-Tanda0-Diez-r2a versionado y reproducible (doble corrida), con 0
nodos ni aristas fuera del modelo r2 y con `remite_a` de `cla::5.1.1.1` a `cla::3.7` (criterio
para escalar, enmienda 2 §9); los sellados reproducidos; la columna r2a del tablero completa
con cada celda medida o con su causa de no medición; la entrada r2 propuesta con el sha del
grafo; las cinco lecturas con regla fijada antes, conteos recomputados e intervalo donde
corresponde. Commit de la autora al cierre de cada etapa.

DECISIONES ABIERTAS PARA LA AUTORA, A LA FIRMA.
1. Si el grafo r2a de desarrollo se versiona junto al de los diez (hoy: solo el de los diez; el
   de desarrollo se produce en el scratchpad para comparar filas).
2. Tamaños de las muestras de M3.a y M3.e (propuestos: 30 nodos de origen y 20 relaciones por
   par) y la semilla.
3. Si la medición de los límites relativos de S18 (25 en desarrollo, 26 en diez) suma una lectura
   asistida de su comparación y su base, como insumo para el tramo que E1 emitirá en r2b
   (plan, unidad 10).
