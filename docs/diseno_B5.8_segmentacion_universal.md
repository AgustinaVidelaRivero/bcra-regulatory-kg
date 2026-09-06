# Diseño B5.8 — Segmentación universal del corpus (los 84 «necesita reglas»)

**Estado: APROBADO por la autora — 06/09/2026** (con las tres resoluciones
del §7 asentadas en la firma de la adenda). Origen: laudo de la autora del
06/09 (adenda al laudo B5.5,
`docs/adenda_laudo_B5.5_segmentacion_universal.md`, FIRMADA 06/09): los 84
TOs sin segmentación reconocida deben volverse segmentables ANTES del
escalado, para que el capítulo del esquema describa la partición del
corpus como hecho y no como etapa.

## §0. Frontera conceptual, declarada primero

**Segmentable ≠ extraíble.** Esta secuencia produce unidades de E0 sobre
los 84 (o declara no-segmentable con causa). NO habilita la extracción del
bloque de régimen informativo: su familia mayor (71 % de las páginas)
requiere extender el esquema (hechos con valor) y el laudo `94bb7a7` §D10
exige que esa familia corra su propio ciclo ESQ antes de congelar esquema
para ella. La prosa del capítulo podrá afirmar: «la partición es un hecho:
N TOs con segmentación reconocida y verificada, M declarados no
segmentables con causa» — sin afirmar extracción donde no la hay.

## §1. Punto de partida medido (fuentes selladas)

- 152 TOs inventariados por sha (`escalado_prep/`, `111ed19`): 68
  reconocidos / 84 «necesita reglas», de los cuales 62 producen cero
  unidades. De los 84: 53 son del bloque RI (0/53), 31 son normativa
  general.
- Causas ya diagnosticadas (U-B5.6-0 + `fe_erratas_D10` + B5.2): (a)
  compuerta de rol de página de E0 (`e0_lib.py:206-207`: sin página de
  índice, todo queda en `portada`) — 47/53 del RI en esa condición; el
  modo de lectura sin raíz de sección desbloquea 44/53 (ESQ-RI-1, $0);
  (b) marcadores de sección con formato no contemplado (estilos medidos:
  «Sección N:» de óptico, encabezados sin guiones — B5.2 ya enganchó
  cedin, ri2_ae, ri_transpa); (c) TOs que llegan a cuerpo y producen cero
  por no tener líneas con formato de sección (1 caso conocido); (d)
  estructura tabular (parser B5.6, pdfplumber: alcanza 23/53 del RI y el
  12,4 % de las palabras del bloque; se construye igual por RX-10);
  (e) resto por censar.
- Interacción ya sellada: las unidades nuevas que excedan el umbral C8
  pasan por el sub-chunking de U-B5.3 (los 6 terminales anómalos medidos
  están todos en TOs de este grupo) — mecánico, sin decisión nueva.

## §2. La secuencia (5 sub-unidades, TODAS con USD 0 de API)

Regla transversal de la restricción 1: ni el corte ni la partición usan
modelo de lenguaje — reglas mecánicas con selftests sobre stubs.

- **B5.8.0 — Censo de familias de formato** (diagnóstico puro, 1 sesión).
  Clasificación mecánica de los 84 por causa (a)–(e), consolidando lo ya
  medido para el RI y extendiéndolo a los 31 no-RI; tabla TO×familia con
  evidencia (páginas, líneas de muestra) y plan de reglas por familia.
  FRENO con el censo: es el insumo para dimensionar B5.8.2 y para la
  decisión de corpus de la adenda.
- **B5.8.1 — Modo de lectura sin raíz de sección** (= ejecuta ESQ-RI-1,
  1–2 sesiones). Ataca la causa dominante (compuerta de rol de página),
  con guardas ancladas a casos medidos (patrón de tres capas de B5.2) y
  el caso aparte (c) tratado con remedio propio o declarado.
- **B5.8.2 — Reglas de marcador por familia** (1–2 sesiones, alcance
  dimensionado por el censo). Cada regla nueva anclada a casos medidos Y
  a contraejemplos (falsos marcadores rechazados), patrón B5.2.
- **B5.8.3 — Parser de tablas** (= ejecuta B5.6, 1–2 sesiones). Familia
  (d); unidades tabulares con provenance, sin LLM. Su producto cuenta
  como «segmentable (tabular)» con la salvedad del §0 declarada.
- **B5.8.4 — Partición final + health-check + declaración** (1 sesión).
  E0 seco 152/152 con todas las reglas; `healthcheck_e0.py` por TO para
  CADA uno que pase a reconocido (restricción 3); los que queden fuera,
  declarados con causa y evidencia (restricción 4 — no se fuerza nada);
  reporte con la partición nueva recomputada desde artefactos y con
  comandos (restricción 5), listo para reescribir las filas 10–15 del
  mapa de fuentes del capítulo.

## §3. Regresión de no-cambio (restricción 2 — criterio DURO adoptado)

Se adopta el criterio fuerte: **byte-identidad de los artefactos E0
sellados**, no solo conteos. En CADA sub-unidad que toque `e0_lib`/
`correr_e0`: (i) paridad byte a byte de los 5 TOs dev contra
`salida_enm01` (patrón B5.2: 20/20, sha verbatim); (ii) sha por TO de los
68 reconocidos contra `e0_dry` sellado; (iii) ídem los 10 de ESQ (762
unidades). Los tres conteos de control (1.763 / 6.340 / 762) se
recomputan y pegan. Además, al cierre de cada sub-unidad:
`selftest_manifiesto.py` 35/35 (P2 depende de `e0_lib`), selftests E0
57/57, B5.2 39/39 y `selftest_ub53` 40/40. **Cualquier diferencia =
FRENO** (invalidaría números sellados en laudos y en la Introducción).

## §4. Escrituras y fronteras

- Módulos tocables: `e0_lib.py`, `correr_e0.py`, `healthcheck_e0.py`,
  módulo nuevo del parser de tablas, selftests propios. Nada más.
- `escalado_prep/` es material sellado: SOLO LECTURA. Las salidas nuevas
  (E0 seco 152/152, censo, health-checks, partición) van a un directorio
  nuevo propio de la secuencia (p. ej. `data/experiment/segmentacion_84/`,
  a declarar en el primer freno).
- `docs/tesis/` PROHIBIDO (restricción 6): la prosa la ajusta la autora
  en el tuneo cuando la secuencia selle. Fronteras vigentes con U-B5.4
  (su directorio) y con el cableado v3 cuando se despache (call-site E1).

## §5. Costo y calendario

- **API: USD 0 en toda la secuencia** (si alguna sub-unidad creyera
  necesitar LLM para algo, eso es un FRENO y una consulta, no un gasto).
- Tiempo estimado: 5–8 sesiones de ejecutor + frenos de revisión
  (≈ 3–5 días de trabajo efectivo). El censo (B5.8.0) dimensiona el resto
  y puede recortar: si una familia resulta chica, su sub-unidad se funde
  con la siguiente por laudo del freno.

## §6. Ubicación en la ruta crítica (propuesta explícita)

- **En PARALELO a U-CAP-ESQ**, con esta interacción declarada: los tramos
  2–5 del capítulo no dependen de la partición; el §1 ya escrito declara
  la partición vigente (68/84/62) con sus filas de mapa — **la pasada
  final de coherencia del capítulo (tramo 5) incorpora los números nuevos
  de B5.8.4 en el tuneo de la autora**. Si B5.8 se atrasara, el capítulo
  puede cerrar con la partición vigente y una oración de estado — pero el
  laudo de la autora pide lo contrario, así que B5.8.4 pasa a ser
  PRERREQUISITO del cierre del capítulo (no de su escritura).
- **Efecto sobre la fecha de escalado**: el escalado ya está gateado a la
  validación del capítulo por lectura; B5.8 corre en paralelo a la
  escritura, así que solo mueve la fecha si termina DESPUÉS de que los
  tramos estén listos — con 5–8 sesiones, es la nueva cola larga de la
  ruta crítica junto con la lectura de mentores. La extracción de los 68
  (tandas 1–2) NO depende técnicamente de B5.8; la dependencia es la
  redaccional que fija la adenda.
- **B6.3**: sin cambio en el pool (142 elegibles); más TOs reconocidos =
  más opciones de cobertura para el eval set fresco.

## §7. Decisiones que la adenda deja explícitas a la autora

1. **Corpus de EXTRACCIÓN de las tandas 1–2**: sigue siendo los 68 (laudo
   B5.5 §2) — ¿o la tanda 2 incorpora los no-RI que B5.8 reconozca (~31
   candidatos de normativa general, cubiertos por el esquema congelado),
   con re-presupuesto? La adenda propone dejarlo como RE-LAUDO con el
   censo en la mano (B5.8.0), no decidirlo a ciegas hoy.
2. **El RI sigue fuera de extracción** hasta su ciclo propio (D10) — la
   adenda lo ratifica; B5.8 solo lo vuelve segmentable.
3. Si B5.6/ESQ-RI-1 se ejecutan DENTRO de esta secuencia (propuesta: sí,
   como B5.8.3 y B5.8.1), sus filas del plan se marcan «ejecutada por
   B5.8.x» — sin duplicar unidades.
