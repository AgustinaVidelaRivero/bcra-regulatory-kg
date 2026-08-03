# Propuesta E3 — Salvedad mutuales/cooperativas del 1.1.2.5 de Protección de Usuarios

Entrada del backlog: **BKL-0003** (fuente escalon1_fallas, especie `ausencia`,
adjudicación humana; retriage v3: `vigente_sin_cambios` — "misma ausencia en v3
('mutual' 0 hits)").
Formato: `.claude/skills/kg-refinement/references/formato_propuesta.md`.
Precedente de estructura: `data/backlog/propuestas/E4_enumeracion_65.md` (C5).
Estado: PROPUESTA — la aplicación es otra unidad, post-laudo explícito.

Grafo objetivo: `data/experiment/grafo_v2/reensamblado_v3/kg.json` (vigente;
precondición verificada: 4.468 nodos / 8.071 aristas).
Fuente de verdad: `data/experiment/subset/TO_proteccion_usuarios_servicios_financieros_actual.pdf`,
Sección 1, punto 1.1.2 (verbatim completo extraído como artefacto de la unidad:
`punto_1_1_2_proteccion_verbatim_E3.txt` en el paquete de revisión;
reproducción: `pdftotext -layout data/experiment/subset/TO_proteccion_usuarios_servicios_financieros_actual.pdf - | sed -n '85,110p'`).

```yaml
id_falla: "BKL-0003 (E3 · EV1-028, adjudicada humana 3-0 incorrecta; ausencia ratificada en retriage v3: 'mutual' 0 hits en v2 y v3)"
categoria_defecto: completitud_kg   # especie del backlog: ausencia — la salvedad del 1.1.2.5 no está en ningún campo de ningún nodo del grafo vigente (sondas de esta unidad: "mutual" 0 hits sobre id+label+properties de los 4468 nodos)
palanca: grafo/esquema
cambio_exacto: >
  Crear en reensamblado_v3/kg.json UN nodo `Excepcion` con la salvedad del
  punto 1.1.2.5 y DOS aristas, usando exclusivamente firmas dominio/rango ya
  existentes en la matriz vigente. Convención de id verificada contra el
  código generador de v3 (data/experiment/grafo_v2/code/assemble_v3.py,
  entity_slug_v3): Excepcion → slug(descripcion)[:80] + sha1(slug)[:6]. El id
  fue recomputado con esa función y verificado INEXISTENTE en el grafo
  vigente (0 colisiones contra los 4468 ids).

  NODO (rol_fuente: "restauracion_manual" — trazable: no proviene del
  pipeline de extracción; provenance leída del PDF; valor ya en uso en el
  grafo vigente por el precedente C5, 10 nodos):

  N1 — salvedad del 1.1.2.5:
    id: "Excepcion_otros_proveedores_no_financieros_de_credito_alcanzados_por_las_normas_sobre_prov_5f95b9"
    type: "Excepcion"
    label: "Excepción del punto 1.1.2.5 (Protección de usuarios): la asociación
            mutual o cooperativa (asociaciones mutuales o cooperativas)
            alcanzada por las normas sobre proveedores no financieros de
            crédito queda exceptuada del carácter de sujeto obligado por las
            financiaciones que otorgue"
    # Label: variante C_mixta elegida por laudo — cubre singular y plural (la
    # variante A daba rank None en la query 'excepción asociaciones mutuales
    # cooperativas'); label interpretativo declarado en nota_fuente.
    properties:
      descripcion: "Otros proveedores no financieros de crédito alcanzados
        por las normas sobre “Proveedores no financieros de crédito”, excepto
        que se trate de asociaciones mutuales o cooperativas, por las
        financiaciones que otorguen."
      nota_fuente: "descripcion verbatim del inciso 1.1.2.5 completo; el
        label es interpretativo (recuperación léxica) y no es texto del PDF —
        la formulación normativa vinculante es la de descripcion"
      # NOTA para el laudo: la descripcion es el inciso 1.1.2.5 ÍNTEGRO
      # (regla de inclusión + salvedad), no la salvedad recortada: recortarla
      # ("excepto que se trate de…") dejaría un fragmento sin sujeto ni
      # contexto. El label parafrasea el efecto de la salvedad (la lectura
      # adjudicada en BKL-0003) y duplica singular/plural
      # ("asociación mutual o cooperativa (asociaciones mutuales o
      # cooperativas)") porque el índice del harness tokeniza label+id sin
      # stemming (harness.py, _tokens sobre label + id): sin la forma
      # singular, la query real fallada "asociación mutual" (paso 8, r1-r3)
      # no lo encuentra. Comparación de variantes de label en la tabla de
      # alcanzabilidad y en el artefacto medicion_alcanzabilidad_E3_salida.txt.
    provenance: {source_doc: "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
                 location: "Punto 1.1.2.5"}
    provenances: [ (la misma) ]
    # location "Punto 1.1.2.5" replica byte a byte la del nodo esqueleto
    # hermano Sujeto_proveedor_no_financiero_de_credito.

  ARISTAS (2; ambas con la provenance del nodo y rol_fuente
  "restauracion_manual"; endpoints existentes verificados; SOLO firmas ya
  presentes en la matriz vigente — inventario completo de firmas con
  Excepcion como source, medido en esta unidad:
    Excepcion --establecida_en--> TextoOrdenado   (235 usos)
    Excepcion --exceptua--> Restriccion           (175 usos)
    Excepcion --exceptua_obligacion--> Obligacion (74 usos)
  y CERO firmas con Excepcion como target):
    1. N1 --establecida_en--> "TextoOrdenado_to_proteccion_usuarios_servicios_financieros_actual_pdf"
       # firma Excepcion→TextoOrdenado, 235 usos
    2. N1 --exceptua_obligacion--> "Obligacion_estas_normas_son_de_aplicacion_a_todos_los_sujetos_obligados_enumerados_en_el_pu_2cf191"
       # firma Excepcion→Obligacion, 74 usos. El target es el nodo del punto
       # 1.3 ("Estas normas son de aplicación a todos los sujetos obligados
       # enumerados en el punto 1.1.2. …", rol_fuente cuerpo, ya conectado por
       # aplica_a al rol de sujetos obligados): la salvedad exceptúa a las
       # asociaciones mutuales o cooperativas de esa aplicación. Es el mismo
       # patrón de uso de exceptua_obligacion en el grafo (p. ej.
       # Excepcion_este_requerimiento_no_sera_de_aplicacion_… →
       # Obligacion_las_entidades_financieras_del_grupo_1_deberan_…).

  LÍMITE DE VOCABULARIO (flaggeado para el laudo): la conexión semánticamente
  más directa sería una arista de N1 al Sujeto exceptuado o al rol
  (Excepcion→Sujeto), pero la matriz vigente tiene CERO aristas con firma
  Excepcion→Sujeto (inventario arriba) y crearla sería una firma nueva —
  prohibido por la restricción de alcance de esta unidad (decisión 4). La
  relación con los sujetos queda portada léxicamente (label y descripcion de
  N1 nombran a las asociaciones mutuales o cooperativas y a los proveedores
  no financieros de crédito) y topológicamente a un salto: N1
  --exceptua_obligacion--> Obligacion_…_2cf191 --aplica_a-->
  Sujeto_rol_sujeto_obligado_proteccion. El modelado explícito de sujetos
  (nodo Sujeto para mutuales/cooperativas, arista de exclusión) es territorio
  del esquema v2: BKL-0020.
cita_pdf: >
  [TO_proteccion_usuarios_servicios_financieros_actual.pdf, Sección 1.
  Disposiciones generales, punto 1.1.2., pág. 1 del rótulo interno de sección
  (Versión 8a., Com. "A" 7744) — verbatim]:
  "1.1.2. Sujetos obligados.
   1.1.2.1. Entidades financieras.
   1.1.2.2. Operadores de cambio, por las operaciones comprendidas en las
            normas sobre “Exterior y cambios”.
   1.1.2.3. Fiduciarios de fideicomisos acreedores de créditos cedidos por
            entidades financieras.
   1.1.2.4. Empresas no financieras emisoras de tarjetas de crédito y/o compra.
   1.1.2.5. Otros proveedores no financieros de crédito alcanzados por las
            normas sobre “Proveedores no financieros de crédito”, excepto que
            se trate de asociaciones mutuales o cooperativas, por las
            financiaciones que otorguen.
   1.1.2.6. Proveedores de servicios de pago que ofrecen cuentas de pago
            (PSPCP).
   1.1.2.7. Proveedores de servicios de pago que cumplen la función de
            iniciación (PSI) y prestan el servicio de billetera digital.
   Cuando un tercero desarrolle tareas relativas a servicios ofrecidos por
   los sujetos obligados o en su nombre, ambos serán responsables por el
   cumplimiento de las presentes normas. Lo anterior deberá establecerse en
   los instrumentos que acuerden la realización de dichas tareas."
  (Guiones de corte de línea del layout normalizados: "finan-cieras",
  "obliga-dos". Texto completo con layout en el artefacto
  punto_1_1_2_proteccion_verbatim_E3.txt del paquete de revisión;
  reproducción: pdftotext -layout
  data/experiment/subset/TO_proteccion_usuarios_servicios_financieros_actual.pdf -
  | sed -n '85,110p')
como_se_verificaria: >
  RE-TEST pre-especificado, en tres capas:
  (1) chunk-contra-PDF (vía de cierre declarada en BKL-0003): releer el punto
  1.1.2.5 del PDF y confirmar que properties.descripcion de N1 coincide
  literalmente con el inciso completo, que el label no afirma nada que la
  salvedad no diga (la excepción alcanza SOLO a asociaciones mutuales o
  cooperativas, SOLO por las financiaciones que otorguen), y que la
  provenance dice Punto 1.1.2.5. EV1-028 está QUEMADA: no participa del
  re-test.
  (2) estructural: el id no colisiona, las 2 aristas existen, ambos endpoints
  resuelven (cero colgantes), ninguna arista introduce una firma
  dominio/rango inexistente en la matriz previa, y los 9 nodos con provenance
  en el 1.1.2 (7 previos + el rol + N1) más las 7 aristas miembro_de del rol
  permanecen byte-idénticos salvo la adición.
  (3) réplica del índice (GraphIndex real sobre v3 + N1 en memoria, ya medida
  en esta propuesta — ver tabla): las queries textuales del agente en las
  réplicas falladas de EV1-028 que nombran a la mutual o a la excepción
  devuelven N1 dentro del corte de 10.
  PREGUNTAS NUEVAS DE VERIFICACIÓN (ninguna de EV1/CQ/CQN/CQN2; gold anclado
  en el verbatim de esta propuesta):
  RT-1 "Según el punto 1.1.2.5 de las normas de protección de los usuarios de
       servicios financieros, ¿qué sujetos quedan exceptuados del carácter de
       sujeto obligado y respecto de qué operaciones?" — gold: las
       asociaciones mutuales o cooperativas (alcanzadas por las normas sobre
       "Proveedores no financieros de crédito"), por las financiaciones que
       otorguen.
  RT-2 "Una cooperativa alcanzada por las normas sobre 'Proveedores no
       financieros de crédito', ¿reviste el carácter de sujeto obligado de
       las normas de protección de los usuarios de servicios financieros por
       las financiaciones que otorgue?" — gold: no; el 1.1.2.5 incluye a los
       otros proveedores no financieros de crédito "excepto que se trate de
       asociaciones mutuales o cooperativas, por las financiaciones que
       otorguen". (Gemela de la falla sobre el otro sujeto exceptuado; NO es
       una pregunta de EV1.)
  RT-3 (no-regresión sobre el nodo de sujetos obligados existente,
       Sujeto_rol_sujeto_obligado_proteccion): "¿Qué sujetos enumera el punto
       1.1.2 como sujetos obligados de las normas de protección de los
       usuarios de servicios financieros?" — gold: los siete incisos del
       verbatim (entidades financieras; operadores de cambio; fiduciarios de
       fideicomisos acreedores de créditos cedidos por entidades financieras;
       empresas no financieras emisoras de tarjetas de crédito y/o compra;
       otros proveedores no financieros de crédito con la salvedad de
       mutuales/cooperativas; PSPCP; PSI con billetera digital). Verifica que
       el rol y sus 7 miembro_de siguen alcanzables e intactos.
  RT-4 (no-regresión de alcance de la excepción): "¿Una empresa no financiera
       emisora de tarjetas de crédito es sujeto obligado de las normas de
       protección de los usuarios de servicios financieros?" — gold: sí
       (inciso 1.1.2.4). Verifica que la excepción nueva no se sobreextiende
       a sujetos no exceptuados.
categoria_riesgo: alto
justificacion_riesgo: >
  Aplicando el criterio fijo: la propuesta CREA estructura nueva (1 nodo, 2
  aristas), el dato es una EXCEPCIÓN normativa ("datos con ambigüedad o
  excepciones" está enumerado como alto), y el label es una paráfrasis
  interpretativa elegida por medición de alcanzabilidad. La descripcion es
  transcripción literal, pero la decisión de anclaje (qué obligación
  exceptúa) es juicio de modelado → revisión humana.
```

## Expediente (P0 — qué falta, qué reveló, qué respondió el agente)

- **Qué falta:** la salvedad del 1.1.2.5. Backlog BKL-0003: especie
  `ausencia`, "salvedad mutuales/cooperativas (1.1.2.5) ausente"; deslinde
  v2 (2026-07-27): "'mutuales o cooperativas': 0 hits. Sondas de control:
  'mutual' 0 hits en todo el grafo"; retriage v3 (E3): "'mutual' da 0 hits
  en v3 y 0 en v2 (doc Protección). El 1b la mantuvo 3-0 incorrecta."
- **Qué reveló la falta:** el grafo vigente porta la regla de inclusión
  (arista Sujeto_proveedor_no_financiero_de_credito --miembro_de-->
  Sujeto_rol_sujeto_obligado_proteccion, provenance "Punto 1.1.2") pero no
  su excepción: el esqueleto nodificó al PNFC (1.1.2.5) sin la salvedad. Un
  grafo que afirma la membresía sin la excepción produce respuestas
  ancladas-pero-incorrectas — instancia directa del hallazgo rector
  grounded ≠ correct.
- **Qué respondió el agente (ficha EV1-028, 3-0 incorrecta):**
  - Réplica 1: "Sí. … los Proveedores no financieros de crédito (PNFC)
    revisten el carácter de sujetos obligados … Por lo tanto, una asociación
    mutual … reviste el carácter de sujeto obligado …" (claim central del
    juez: falso). Siguió la arista miembro_de sin excepción a la vista.
  - Réplicas 2 y 3 (idénticas): "… los Proveedores no financieros de crédito
    (PNFC) revisten el carácter de sujetos obligados … Sin embargo, el grafo
    no contiene información específica que permita determinar si una
    asociación mutual … es clasificada como PNFC …" (respondible: false;
    claim central: falso). El agente buscó la excepción y no la encontró:
    queries "asociación mutual" (paso 8, 3 réplicas) y "exclusión excluido
    no alcanzado no incluido sujeto obligado" (paso 9, r2/r3) — la segunda
    es literalmente una búsqueda de la salvedad ausente.

## Estado del grafo vigente (P2)

**(a) Nodos con provenance en el 1.1.2** (9 hits de sonda sobre
`provenances[].location` conteniendo "1.1.2" con source_doc de Protección;
comando en el paquete de revisión):

| Inciso | Nodo | Observación |
|---|---|---|
| 1.1.2 (rol) | `Sujeto_rol_sujeto_obligado_proteccion` | esqueleto, nivel rol |
| 1.1.2.1 | `Sujeto_entidad_financiera` | esqueleto |
| 1.1.2.2 | — | NO nodificado en Protección; `Sujeto_entidad_cambiaria` existe con provenance TO_exterior_cambios "Punto 5.4.2.2" y arista miembro_de al rol con provenance "Punto 1.1.2" |
| 1.1.2.3 | — | NO nodificado en Protección; `Sujeto_fiduciario_de_fideicomiso_financiero` existe con provenance TO_clasificacion "Punto 10.2" y arista miembro_de al rol |
| 1.1.2.4 | `Sujeto_empresa_no_financiera_emisora_de_tarjetas` | esqueleto |
| 1.1.2.5 | `Sujeto_proveedor_no_financiero_de_credito` | esqueleto — porta la INCLUSIÓN, no la salvedad |
| 1.1.2.6 | `Sujeto_proveedor_de_servicios_de_pago`, `Sujeto_pspcp` | esqueleto |
| 1.1.2.7 | `Sujeto_psi_billetera_digital` | esqueleto |

La salvedad del 1.1.2.5 no está nodificada en ningún inciso. (Constancia
para el laudo, sin acción en esta propuesta: los incisos 1.1.2.2 y 1.1.2.3
tampoco tienen nodo propio anclado en Protección; sus sujetos existen
anclados en otros TOs.)

**(b) Sondas** (normalización NFD sin diacríticos, minúsculas, sobre id +
label + properties string de los 4.468 nodos; salida completa en
`sondas_grafo_vigente_E3.txt` del paquete):

- "mutual": **0 hits**.
- "cooperativa": 4 hits, todos de Capitales Mínimos (cajas de crédito
  cooperativas, exigencia básica del 1.2) — ninguno de Protección:
  `Sujeto_caja_de_credito_cooperativa` (id),
  `Restriccion_restantes_entidades_salvo_cajas_de_credito_cooperativas_deberan_observar_exigenc_7b4b77` (id),
  `Excepcion_cajas_de_credito_cooperativas_estan_exceptuadas_de_la_exigencia_basica_de_restan_53466d` (id),
  `Obligacion_desde_el_01_06_24_y_hasta_el_31_12_24_correspondera_que_tales_entidades_en_funci_9f9564` (campo descripcion).
- "proveedores no financieros de credito": 5 hits —
  `Sujeto_proveedor_no_financiero_de_credito` (label),
  `Obligacion_clasificar_deudores_por_mora_923aa3` (description),
  `Restriccion_las_entidades_financieras_las_empresas_no_financieras_emisoras_de_tarjetas_de_cr_241bea` (descripcion),
  `Obligacion_las_entidades_financieras_los_pspcp_las_empresas_no_financieras_emisoras_de_tarj_132127` (descripcion),
  `Obligacion_las_entidades_financieras_las_empresas_no_financieras_emisoras_de_tarjetas_de_cr_c12642` (descripcion).
  Ninguno porta la salvedad.

**(c) Vecindario del nodo de sujetos obligados afectado**
(`Sujeto_rol_sujeto_obligado_proteccion`: JSON completo y las 168 aristas
incidentes volcados en `vecindario_rol_sujetos_obligados_E3.txt` del
paquete; también el del PNFC, 15 aristas, en
`vecindario_pnfc_E3.txt`). Resumen: el rol (esqueleto, nivel rol,
provenance "Punto 1.1.2") recibe 7 aristas miembro_de (una por sujeto,
incluida la del PNFC con provenance "Punto 1.1.2") y 161 aristas aplica_a
de reglas de cuerpo. El PNFC además es target de subclase_de desde
`Sujeto_empresa_no_financiera_emisora_de_tarjetas` y miembro_de hacia
`Sujeto_rol_obligado_a_clasificar_clasificacion` (Clasificación, Secciones
1 y 10). Ninguna arista ni nodo del vecindario expresa la salvedad.

## Verificación de alcanzabilidad léxica (medida, índice replicado)

Réplica del `GraphIndex` real (`data/experiment/evaluacion/harness.py`,
tokens sobre label+id, sin stemming) sobre el vigente cargado con
`loader.load_graph_from_path` + N1 agregado EN MEMORIA (el kg.json no se
tocó; precondición 4468/8071 asertada en el script). Script y salida
completa: `medir_alcanzabilidad_E3.py` y
`medicion_alcanzabilidad_E3_salida.txt` en el paquete. Las siete primeras
queries son las que el agente Haiku usó textualmente en las réplicas
falladas de EV1-028; las cuatro últimas, variantes plausibles. Rank dentro
del corte de 10 (— = fuera del top-10); "rol" y "pnfc" son los controles
`Sujeto_rol_sujeto_obligado_proteccion` y
`Sujeto_proveedor_no_financiero_de_credito`, con su rank baseline
(pre-cambio) → post:

| Query | N1 (rank) | rol pre→post | pnfc pre→post |
|---|---|---|---|
| "asociación mutual financiaciones proveedor no financiero crédito" (r1-r3, paso 1) | **1** | —→— | 1→2 |
| "sujeto obligado protección usuarios servicios financieros" (r1-r3, paso 2) | **1** | 4→5 | —→— |
| "proveedor no financiero crédito" (r1-r3, paso 3) | — | —→— | 1→1 |
| "asociación mutual" (r1-r3, paso 8) | **1** | —→— | —→— |
| "definición proveedor no financiero crédito PNFC" (r1, paso 9) | — | —→— | 1→1 |
| "proveedor no financiero crédito comercios empresas personas jurídicas" (r1, paso 10) | — | —→— | 1→1 |
| "exclusión excluido no alcanzado no incluido sujeto obligado" (r2/r3, paso 9) | **4** | —→— | 10→— |
| "mutuales cooperativas sujeto obligado protección usuarios" (variante) | **1** | 1→2 | —→— |
| "excepción asociaciones mutuales cooperativas" (variante) | **1** | —→— | —→— |
| "cooperativa que otorga financiaciones protección de usuarios" (variante) | **1** | 5→5 | —→— |
| "asociaciones mutuales proveedores no financieros de crédito" (variante) | **1** | —→— | 1→2 |

Lectura: N1 entra al top-10 (rank 1 en 6 de 7 casos con hit) en TODAS las
queries que nombran a la mutual/cooperativa o buscan la excepción —
incluidas las dos búsquedas fallidas clave de las réplicas (paso 8 y paso
9 r2/r3, que en baseline devolvían cero nodos relevantes). Las tres
queries puramente de PNFC (pasos 3, 9-r1, 10) no lo devuelven y conservan
al PNFC en rank 1: la excepción no canibaliza la regla. Desplazamientos de
control acotados (rol 4→5 y 1→2; pnfc 1→2 en dos queries donde N1 pasa al
1; pnfc pierde el rank 10 en la query de exclusión a manos de N1, que es
exactamente el nodo que esa búsqueda pedía). Se midieron 3 variantes de
label (A natural sin plural duplicado, B corta, C adoptada): A pierde la
variante "excepción asociaciones mutuales cooperativas" y B pierde las
cuatro queries reales de las réplicas; la C adoptada cubre 8 de 11 con las
3 restantes siendo las de PNFC puro que no deben devolverla (comparación
completa en la salida del script).

## Qué NO se toca (decisión 4 — restricción de alcance)

- **Ningún nodo Sujeto/EntidadFinanciera se modifica**: los 7 miembros del
  rol, el rol `Sujeto_rol_sujeto_obligado_proteccion` y
  `Sujeto_proveedor_no_financiero_de_credito` quedan byte-idénticos.
- **No se crean sujetos nuevos**: las asociaciones mutuales o cooperativas
  NO se nodifican como Sujeto (mi diseño natural lo pediría — nodo Sujeto +
  arista de exclusión al rol — pero eso remodela sujetos y exige la firma
  inexistente Excepcion→Sujeto o una relación de no-membresía: territorio
  del esquema v2, BKL-0020). Esta propuesta se limita a la salvedad como
  `Excepcion`, conforme al laudo. Desvío: NINGUNO — el diseño cabe completo
  en las firmas vigentes.
- **No se crean firmas nuevas**: las 2 aristas usan Excepcion→TextoOrdenado
  (establecida_en, 235 usos previos) y Excepcion→Obligacion
  (exceptua_obligacion, 74 usos previos).
- La arista `Sujeto_proveedor_no_financiero_de_credito --miembro_de-->
  Sujeto_rol_sujeto_obligado_proteccion` NO se borra ni se anota: la
  inclusión de los PNFC no-mutuales sigue vigente en la norma; la excepción
  se agrega al lado, no encima.
- Ningún nodo ni arista existente se modifica o borra; el cambio es
  aditivo: 4.468 → 4.469 nodos, 8.071 → 8.073 aristas.
