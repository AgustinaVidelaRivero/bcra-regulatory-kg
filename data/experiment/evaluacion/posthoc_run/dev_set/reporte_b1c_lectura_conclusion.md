# B1c — Trazado lectura→conclusión en los casos de frontera

Fecha: 2026-07-16. SOLO LECTURA; única escritura: este archivo (zona gitignored). Sin API.
Material: los JSONs congelados de piloto_v6/ y validacion_v61/. **Solo hechos — sin
propuesta de diseño.**

**Fuente:** `_meta.trayectoria_verificador` de cada rep (pasos `{n, tool, input,
output_truncado}`; el output está truncado a TRUNC=1200 en la traza — verificador.py:58 —
por eso los fragmentos pegados son los primeros ~200 chars del campo `pasaje` del output
almacenado). **Campo de justificación persistido:** `razonamiento` (str, por rep) — primeros
280 chars pegados por rep. La atribución se identifica por par + jerarquía +
`evidencia.nodo.ubicacion`.

**Selección de reps:** en cada caso, las reps cuyas primarias contienen el par indicado
(las 2 primeras en orden de rep); en (5), la rep que emitió `aplicacion_erronea` como
primaria (rep 1) y la primera de las de `navegación` (rep 2).

## Trazado completo (código: extractor sobre los JSONs congelados; output íntegro)

```

============================================================================
(1) piloto run_3/CQ-018 [mayoría contenido_kg] — rep 1 (archivo off_run_3_CQ-018.json)
============================================================================
  paso 1: leer_pasaje_pdf({"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Punto 4.1. Niveles de clasificación."})
     → 4.1. Niveles de clasificación.  4.2. Criterio básico de clasificación.  4.3. Evaluación de la capacidad de pago.  4.4. Financiaciones cubiertas con garantías preferidas “A”.  4.5. Deudores que no …
  paso 2: leer_pasaje_pdf({"source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf", "location": "Punto 3.2. Controles. (parte 1)"})
     → 3.2. Controles.  3. 2.1. De los sujetos obligados.  3. 2.1.1. Directivo Responsable de Protección de los Usuarios de Servicios Financi e- ros/Comité de Protección de los Usuarios de Servicios Fin…
  paso 3: leer_pasaje_pdf({"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Punto 4.2"})
     → 4.2. Criterio básico de clasificación.  El criterio básico a ser utilizado para efectuar tal clasificación es la capacidad de pago en el fu- turo de la deuda o de los compromisos objeto de la garant…
  paso 4: leer_pasaje_pdf({"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Punto 4.3"})
     → 4.3. Evaluación de la capacidad de pago.  4.3.1. Al evaluar la capacidad de repago, el énfasis deberá ponerse en el análisis de los flujos  de fondos realizado por la entidad.  4.3.2. En segundo lu…
  paso 5: leer_pasaje_pdf({"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Punto 10.1. Proveedores no financieros de crédito."})
     → 10.1. Proveedores no financieros de crédito. Las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveed o- res no financieros de crédito alcanzados por las normas sob…
  paso 8: leer_pasaje_pdf({"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Punto 7.1"})
     → 7.1. Criterio de clasificación. Sin perjuicio de que los análisis previos al otorgamiento de las financiaciones y refinanciaciones también deben guardar relación con la capacidad de pago de los deud…
  paso 9: leer_pasaje_pdf({"source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf", "location": "Punto 3.2.1.1"})
     → {"localizacion_pdf": "fallida", "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf", "location": "Punto 3.2.1.1", "ref": "Punto/Sección 3.2.1.1 (mejor score=n/a < 6)", "mensaje": "…
  paso 10: leer_pasaje_pdf({"source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf", "location": "Punto 3.2.1.1"})
     → {"localizacion_pdf": "fallida", "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf", "location": "Punto 3.2.1.1", "ref": "Punto/Sección 3.2.1.1 (mejor score=n/a < 6)", "mensaje": "…
  paso 12: leer_pasaje_pdf({"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Punto 6.5"})
     → 6.5. Niveles de clasificación. Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las s i- guientes cinco categorías, las que se definen teniendo en cuenta las co…

  ATRIBUCIONES EMITIDAS (par · jerarquía · portador según evidencia.nodo.ubicacion):
    1. {noise_sensitivity, contenido_kg} · primaria · portador: Obligacion_evaluar_capacidad_de_pago (abierto por el agente en paso 13)
    2. {noise_sensitivity, contenido_kg} · primaria · portador: Obligacion_analisis_de_flujos_de_fondos (prov Punto 4.3)
    3. {noise_sensitivity, provenance_imprecisa} · secundaria · portador: Obligacion_las_entidades_financieras_las_empresas_no_financieras_emisoras_de_tarjetas_de_c

  campo de justificación persistido: `razonamiento` (str, 2227 chars). Primeros 280:
    PATAS 1 y 2 (cumplir Protección al Usuario / deber de clasificar) fueron aprobadas por el juez y no se re-litigan. El foco son 4 afirmaciones marcadas no_soportado. (A) 'Directivo Responsable': el claim está SOPORTADO literalmente por el nodo consultado en el paso 4 y es fiel al…

  HECHOS: leyó 9 pasajes (8 ubicaciones únicas):
    - TO_clasificacion_deudores_actual.pdf :: Punto 10.1. Proveedores no financieros de crédito.
    - TO_clasificacion_deudores_actual.pdf :: Punto 4.1. Niveles de clasificación.
    - TO_clasificacion_deudores_actual.pdf :: Punto 4.2
    - TO_clasificacion_deudores_actual.pdf :: Punto 4.3
    - TO_clasificacion_deudores_actual.pdf :: Punto 6.5
    - TO_clasificacion_deudores_actual.pdf :: Punto 7.1
    - TO_proteccion_usuarios_servicios_financieros_actual.pdf :: Punto 3.2. Controles. (parte 1)
    - TO_proteccion_usuarios_servicios_financieros_actual.pdf :: Punto 3.2.1.1
  PUNTO COMPARATIVO CLAVE (¿leyó el 10.1 de Clasificación?): LEÍDO

============================================================================
(1) piloto run_3/CQ-018 [mayoría contenido_kg] — rep 2 (archivo off_run_3_CQ-018.json)
============================================================================
  paso 1: leer_pasaje_pdf({"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Punto 4.1. Niveles de clasificación."})
     → 4.1. Niveles de clasificación.  4.2. Criterio básico de clasificación.  4.3. Evaluación de la capacidad de pago.  4.4. Financiaciones cubiertas con garantías preferidas “A”.  4.5. Deudores que no …
  paso 2: leer_pasaje_pdf({"source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf", "location": "Punto 3.2. Controles. (parte 1)"})
     → 3.2. Controles.  3. 2.1. De los sujetos obligados.  3. 2.1.1. Directivo Responsable de Protección de los Usuarios de Servicios Financi e- ros/Comité de Protección de los Usuarios de Servicios Fin…
  paso 3: leer_pasaje_pdf({"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Punto 4.2. Criterio básico de clasificación."})
     → 4.2. Criterio básico de clasificación.  El criterio básico a ser utilizado para efectuar tal clasificación es la capacidad de pago en el fu- turo de la deuda o de los compromisos objeto de la garant…
  paso 4: leer_pasaje_pdf({"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Punto 4.3. Evaluación de la capacidad de pago."})
     → 4.3. Evaluación de la capacidad de pago.  4.3.1. Al evaluar la capacidad de repago, el énfasis deberá ponerse en el análisis de los flujos  de fondos realizado por la entidad.  4.3.2. En segundo lu…
  paso 5: leer_pasaje_pdf({"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Punto 10.1. Proveedores no financieros de crédito."})
     → 10.1. Proveedores no financieros de crédito. Las empresas no financieras emisoras de tarjetas de crédito y/o compra y los otros proveed o- res no financieros de crédito alcanzados por las normas sob…
  paso 6: leer_pasaje_pdf({"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Sección 7"})
     → {"localizacion_pdf": "fallida", "source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Sección 7", "ref": "Punto/Sección 7 (mejor score=-33 < 6)", "mensaje": "No se pudo anclar el pasaje e…
  paso 7: leer_pasaje_pdf({"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Sección 6"})
     → 6. 5.1. En situación normal.  E l análisis del flu jo de fondos del cliente demuestra que es capaz de atender adecuada- mente todos sus compromisos financieros.  E ntre los indicadores que puede…
  paso 8: leer_pasaje_pdf({"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Punto 7.2"})
     → 7.2. Niveles de clasificación.  7.2.1. Situación normal.  Comprende los clientes que atienden en forma puntual el pago de sus obligaciones o con  atrasos que no superan los 31 días.  Los adelantos…
  paso 9: leer_pasaje_pdf({"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Punto 7.1"})
     → 7.1. Criterio de clasificación. Sin perjuicio de que los análisis previos al otorgamiento de las financiaciones y refinanciaciones también deben guardar relación con la capacidad de pago de los deud…
  paso 11: leer_pasaje_pdf({"source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf", "location": "Punto 3.2.1.1"})
     → {"localizacion_pdf": "fallida", "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf", "location": "Punto 3.2.1.1", "ref": "Punto/Sección 3.2.1.1 (mejor score=n/a < 6)", "mensaje": "…
  paso 12: leer_pasaje_pdf({"source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf", "location": "Sección 3"})
     → 3. 1.4. Registro de Reintegros de Importes (RRI).  E n este registro se deberán asentar los montos reintegrados a los usuarios, identifican- do en cada caso al usuario afectado, la causal generado…

  ATRIBUCIONES EMITIDAS (par · jerarquía · portador según evidencia.nodo.ubicacion):
    1. {noise_sensitivity, contenido_kg} · primaria · portador: Obligacion_evaluar_capacidad_de_pago (abierto por el agente, paso 13); provenance Punto 4.
    2. {noise_sensitivity, contenido_kg} · secundaria · portador: Obligacion_para_clasificacion_en_situacion_normal_el_analisis_del_flujo_de_fondos_del_clie
    3. {noise_sensitivity, sin_defecto} · sin_par · portador: Obligacion_las_entidades_financieras_las_empresas_no_financieras_emisoras_de_tarjetas_de_c

  campo de justificación persistido: `razonamiento` (str, 2410 chars). Primeros 280:
    Descompuse en 3 patas. Pata 1 (Protección al Usuario) y Pata 2 (deben clasificar) fueron aprobadas por el juez en sus claims centrales; el agente las cubrió con nodos pertinentes (paso 4: Directivo Responsable con provenance a Protección 3.2; paso 15: 'Clasificar deudores por mor…

  HECHOS: leyó 11 pasajes (11 ubicaciones únicas):
    - TO_clasificacion_deudores_actual.pdf :: Punto 10.1. Proveedores no financieros de crédito.
    - TO_clasificacion_deudores_actual.pdf :: Punto 4.1. Niveles de clasificación.
    - TO_clasificacion_deudores_actual.pdf :: Punto 4.2. Criterio básico de clasificación.
    - TO_clasificacion_deudores_actual.pdf :: Punto 4.3. Evaluación de la capacidad de pago.
    - TO_clasificacion_deudores_actual.pdf :: Punto 7.1
    - TO_clasificacion_deudores_actual.pdf :: Punto 7.2
    - TO_clasificacion_deudores_actual.pdf :: Sección 6
    - TO_clasificacion_deudores_actual.pdf :: Sección 7
    - TO_proteccion_usuarios_servicios_financieros_actual.pdf :: Punto 3.2. Controles. (parte 1)
    - TO_proteccion_usuarios_servicios_financieros_actual.pdf :: Punto 3.2.1.1
    - TO_proteccion_usuarios_servicios_financieros_actual.pdf :: Sección 3
  PUNTO COMPARATIVO CLAVE (¿leyó el 10.1 de Clasificación?): LEÍDO

============================================================================
(2) piloto run_3/CQ-033 [mayoría contenido_kg-primaria] — rep 1 (archivo off_run_3_CQ-033.json)
============================================================================
  paso 1: leer_pasaje_pdf({"source_doc": "TO_capitales_minimos_actual.pdf", "location": "Punto 12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026"})
     → 12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026 c omo con- secuencia de lo establecido en el punto 4.1. del TO sobre Autoridades de Entidades Financie- ras, la …
  paso 2: leer_pasaje_pdf({"source_doc": "TO_capitales_minimos_actual.pdf", "location": "Punto 7.3. Límite para las entidades del grupo 2."})
     → 7.3. Límite para las entidades del grupo 2. La exigencia determinada a través de la aplicación de la expresión descripta en el punto 7. 2. no podrá superar: 7.3.1. El 20% en el caso de entidades de…

  ATRIBUCIONES EMITIDAS (par · jerarquía · portador según evidencia.nodo.ubicacion):
    1. {noise_sensitivity, contenido_kg} · primaria · portador: Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_b_dete

  campo de justificación persistido: `razonamiento` (str, 2261 chars). Primeros 280:
    SÍNTOMA: el juez marcó no_soportado la afirmación no-central 'Ese límite del 17% está vigente hasta el 30/06/26'. C1a (pata 'cuál es el límite'): el dato apareció en la trayectoria (paso 3 devuelve un nodo con '...hasta el 30/06/26 no podrá superar el 17%') → no es context_recall…

  HECHOS: leyó 2 pasajes (2 ubicaciones únicas):
    - TO_capitales_minimos_actual.pdf :: Punto 12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026
    - TO_capitales_minimos_actual.pdf :: Punto 7.3. Límite para las entidades del grupo 2.
  PUNTO COMPARATIVO CLAVE (¿leyó el 7.3/7.3.2 además del 12.3?): LEÍDO

============================================================================
(2) piloto run_3/CQ-033 [mayoría contenido_kg-primaria] — rep 2 (archivo off_run_3_CQ-033.json)
============================================================================
  paso 1: leer_pasaje_pdf({"source_doc": "TO_capitales_minimos_actual.pdf", "location": "Punto 12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026"})
     → 12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026 c omo con- secuencia de lo establecido en el punto 4.1. del TO sobre Autoridades de Entidades Financie- ras, la …
  paso 2: leer_pasaje_pdf({"source_doc": "TO_capitales_minimos_actual.pdf", "location": "Punto 7.3. Límite para las entidades del grupo 2."})
     → 7.3. Límite para las entidades del grupo 2. La exigencia determinada a través de la aplicación de la expresión descripta en el punto 7. 2. no podrá superar: 7.3.1. El 20% en el caso de entidades de…

  ATRIBUCIONES EMITIDAS (par · jerarquía · portador según evidencia.nodo.ubicacion):
    1. {noise_sensitivity, contenido_kg} · primaria · portador: Restriccion_la_exigencia_de_capital_por_riesgo_operacional_para_entidades_del_grupo_b_dete

  campo de justificación persistido: `razonamiento` (str, 2689 chars). Primeros 280:
    El único claim que el juez marcó incorrecto es la afirmación [no central] 'Ese límite del 17% está vigente hasta el 30/06/26'. Descomposición: la pata 1 ('cuál es el límite para Grupo 2') tuvo su dato pertinente (17%) presente en la trayectoria; el juez aprobó el '17% del promedi…

  HECHOS: leyó 2 pasajes (2 ubicaciones únicas):
    - TO_capitales_minimos_actual.pdf :: Punto 12.3. Para aquellas entidades financieras que sean reclasificadas desde el 01/01/2026
    - TO_capitales_minimos_actual.pdf :: Punto 7.3. Límite para las entidades del grupo 2.
  PUNTO COMPARATIVO CLAVE (¿leyó el 7.3/7.3.2 además del 12.3?): LEÍDO

============================================================================
(3) validación run_2/CQ-018 [contenido_kg] — rep 1 (archivo off_run_2_CQ-018.json)
============================================================================
  paso 1: leer_pasaje_pdf({"source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf", "location": "Sección 5 > Punto 1.1"})
     → 1.1. Partes. 1.1.1. Usuario de servicios financieros. A los efectos de la presente reglamentación, este concepto comprende a las personas humanas y jurídicas que en beneficio propio o de su grupo f…
  paso 2: leer_pasaje_pdf({"source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf", "location": "Sección 2 > Punto 2.4"})
     → 2.4. Disposiciones generales.  2.2. 4.1. La accesibilidad a los puntos de atención al usuario (casas operativas y cajeros  automáticos) deberá respetar características apropiadas para cada uno de e…
  paso 3: leer_pasaje_pdf({"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Sección 6 > Punto 6.4"})
     → 6.4. Reconsideración obligatoria de la clasificación.  En forma adicional a la periodicidad mínima expuesta precedentemente, se deberá analizar de- jando constancia fundamentada de la decisión adopt…
  paso 4: leer_pasaje_pdf({"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Sección 3 > Punto 3.6"})
     → 3.6. Aprobación de la clasificación. La clasificación de los deudores y el cálculo de las previsiones por riesgo de incobrabilidad, ta n- to la regulatoria como la contable por aplicación de la de l…
  paso 5: leer_pasaje_pdf({"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Sección 7 > Sección 7 — preámbulo"})
     → {"localizacion_pdf": "fallida", "source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Sección 7 > Sección 7 — preámbulo", "ref": "Punto/Sección 7 (mejor score=-33 < 6)", "mensaje": "No se…
  paso 6: leer_pasaje_pdf({"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Sección 6 > Punto 5.1"})
     → 5.1. En situación normal.  E l análisis del flu jo de fondos del cliente demuestra que es capaz de atender adecuada- mente todos sus compromisos financieros.  E ntre los indicadores que pueden re…
  paso 7: leer_pasaje_pdf({"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Punto 3.6"})
     → 3.6. Aprobación de la clasificación. La clasificación de los deudores y el cálculo de las previsiones por riesgo de incobrabilidad, ta n- to la regulatoria como la contable por aplicación de la de l…
  paso 8: leer_pasaje_pdf({"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Sección 7"})
     → {"localizacion_pdf": "fallida", "source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Sección 7", "ref": "Punto/Sección 7 (mejor score=-33 < 6)", "mensaje": "No se pudo anclar el pasaje e…
  paso 9: leer_pasaje_pdf({"source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf", "location": "Punto 1.1"})
     → 1.1. Partes. 1.1.1. Usuario de servicios financieros. A los efectos de la presente reglamentación, este concepto comprende a las personas humanas y jurídicas que en beneficio propio o de su grupo f…
  paso 13: leer_pasaje_pdf({"source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf", "location": "Sección 3"})
     → 3. 1.4. Registro de Reintegros de Importes (RRI).  E n este registro se deberán asentar los montos reintegrados a los usuarios, identifican- do en cada caso al usuario afectado, la causal generado…

  ATRIBUCIONES EMITIDAS (par · jerarquía · portador según evidencia.nodo.ubicacion):
    1. {noise_sensitivity, contenido_kg} · primaria · portador: concepto_definido:capacidad_de_pago (paso 12)
    2. {noise_sensitivity, contenido_kg} · secundaria · portador: concepto_definido:criterios_objetivos_de_clasificacion (paso 11)
    3. {noise_sensitivity, provenance_imprecisa} · primaria · portador: obligacion:considerar_y_resolver_fundadamente_reclamos_de_usuarios (provenance Sección 5 >
    4. {noise_sensitivity, provenance_imprecisa} · primaria · portador: obligacion:publicar_contratos_de_adhesion_en_sitio_de_internet_institucional (provenance S

  campo de justificación persistido: `razonamiento` (str, 2973 chars). Primeros 280:
    FASE A: el agente descompuso la pregunta correctamente y consultó los sujetos, sus vecinos (obligaciones) y los conceptos de clasificación. La respuesta enumeró obligaciones de protección y criterios de clasificación. FASE B/C: (1) Pata 'criterio de clasificación' — el juez marcó…

  HECHOS: leyó 10 pasajes (10 ubicaciones únicas):
    - TO_clasificacion_deudores_actual.pdf :: Punto 3.6
    - TO_clasificacion_deudores_actual.pdf :: Sección 3 > Punto 3.6
    - TO_clasificacion_deudores_actual.pdf :: Sección 6 > Punto 5.1
    - TO_clasificacion_deudores_actual.pdf :: Sección 6 > Punto 6.4
    - TO_clasificacion_deudores_actual.pdf :: Sección 7
    - TO_clasificacion_deudores_actual.pdf :: Sección 7 > Sección 7 — preámbulo
    - TO_proteccion_usuarios_servicios_financieros_actual.pdf :: Punto 1.1
    - TO_proteccion_usuarios_servicios_financieros_actual.pdf :: Sección 2 > Punto 2.4
    - TO_proteccion_usuarios_servicios_financieros_actual.pdf :: Sección 3
    - TO_proteccion_usuarios_servicios_financieros_actual.pdf :: Sección 5 > Punto 1.1
  PUNTO COMPARATIVO CLAVE (¿leyó el 10.1 de Clasificación?): NO LEÍDO

============================================================================
(3) validación run_2/CQ-018 [contenido_kg] — rep 2 (archivo off_run_2_CQ-018.json)
============================================================================
  paso 1: leer_pasaje_pdf({"source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf", "location": "Sección 5 > Punto 1.1"})
     → 1.1. Partes. 1.1.1. Usuario de servicios financieros. A los efectos de la presente reglamentación, este concepto comprende a las personas humanas y jurídicas que en beneficio propio o de su grupo f…
  paso 2: leer_pasaje_pdf({"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Sección 6 > Punto 6.4"})
     → 6.4. Reconsideración obligatoria de la clasificación.  En forma adicional a la periodicidad mínima expuesta precedentemente, se deberá analizar de- jando constancia fundamentada de la decisión adopt…
  paso 3: leer_pasaje_pdf({"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Sección 3 > Punto 3.6"})
     → 3.6. Aprobación de la clasificación. La clasificación de los deudores y el cálculo de las previsiones por riesgo de incobrabilidad, ta n- to la regulatoria como la contable por aplicación de la de l…
  paso 4: leer_pasaje_pdf({"source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf", "location": "Sección 2 > Punto 2.4"})
     → 2.4. Disposiciones generales.  2.2. 4.1. La accesibilidad a los puntos de atención al usuario (casas operativas y cajeros  automáticos) deberá respetar características apropiadas para cada uno de e…
  paso 5: leer_pasaje_pdf({"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Sección 6 > Punto 5.1"})
     → 5.1. En situación normal.  E l análisis del flu jo de fondos del cliente demuestra que es capaz de atender adecuada- mente todos sus compromisos financieros.  E ntre los indicadores que pueden re…
  paso 6: leer_pasaje_pdf({"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Sección 7 > Sección 7 — preámbulo"})
     → {"localizacion_pdf": "fallida", "source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Sección 7 > Sección 7 — preámbulo", "ref": "Punto/Sección 7 (mejor score=-33 < 6)", "mensaje": "No se…
  paso 7: leer_pasaje_pdf({"source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf", "location": "Sección 3 > Sección 3 — preámbulo"})
     → 3. 1.4. Registro de Reintegros de Importes (RRI).  E n este registro se deberán asentar los montos reintegrados a los usuarios, identifican- do en cada caso al usuario afectado, la causal generado…
  paso 8: leer_pasaje_pdf({"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Sección 7"})
     → {"localizacion_pdf": "fallida", "source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Sección 7", "ref": "Punto/Sección 7 (mejor score=-33 < 6)", "mensaje": "No se pudo anclar el pasaje e…

  ATRIBUCIONES EMITIDAS (par · jerarquía · portador según evidencia.nodo.ubicacion):
    1. {noise_sensitivity, contenido_kg} · primaria · portador: concepto_definido:capacidad_de_pago (label genérico, sin marca de alcance cartera comercia
    2. {noise_sensitivity, sin_defecto} · sin_par · portador: obligacion:considerar_y_resolver_fundadamente_reclamos_de_usuarios; edges obligado_a hacia
    3. {noise_sensitivity, provenance_imprecisa} · secundaria · portador: obligacion:considerar_y_resolver_fundadamente_reclamos_de_usuarios; edges hacia entregar_d

  campo de justificación persistido: `razonamiento` (str, 3133 chars). Primeros 280:
    Descompuse las patas y clasifiqué por pata (C1a) y luego por claim (C1b). PROTECCIÓN AL USUARIO (patas 1 y 3): el dato pertinente SÍ apareció — el agente vio en los pasos 7 y 8 los edges obligado_a hacia 'considerar y resolver fundadamente reclamos de usuarios', 'entregar detalle…

  HECHOS: leyó 8 pasajes (8 ubicaciones únicas):
    - TO_clasificacion_deudores_actual.pdf :: Sección 3 > Punto 3.6
    - TO_clasificacion_deudores_actual.pdf :: Sección 6 > Punto 5.1
    - TO_clasificacion_deudores_actual.pdf :: Sección 6 > Punto 6.4
    - TO_clasificacion_deudores_actual.pdf :: Sección 7
    - TO_clasificacion_deudores_actual.pdf :: Sección 7 > Sección 7 — preámbulo
    - TO_proteccion_usuarios_servicios_financieros_actual.pdf :: Sección 2 > Punto 2.4
    - TO_proteccion_usuarios_servicios_financieros_actual.pdf :: Sección 3 > Sección 3 — preámbulo
    - TO_proteccion_usuarios_servicios_financieros_actual.pdf :: Sección 5 > Punto 1.1
  PUNTO COMPARATIVO CLAVE (¿leyó el 10.1 de Clasificación?): NO LEÍDO

============================================================================
(4) validación run_4/CQ-017 [estructural_kg] — rep 2 (archivo off_run_4_CQ-017.json)
============================================================================
  paso 3: leer_pasaje_pdf({"source_doc": "TO_exterior_cambios_actual.pdf", "location": "Sección 15.1"})
     → 15.1. Artículos 1° y 2° del Decreto 260/02.  15.2. Artículos 1°, 2° y 3° del Decreto 609/19.  Tabla de correlaciones.  B.C.R.A. TEXTO ORDENADO DE LAS NORMAS SOBRE  \"EXTERIOR Y CAMBIOS\".  Versió…
  paso 4: leer_pasaje_pdf({"source_doc": "TO_exterior_cambios_actual.pdf", "location": "Punto 3.10"})
     → 3.10. Compra de moneda extranjera por parte de otros residentes –excluidas las  entidades– para la formación de activos externos y por operaciones con  derivados.  3.11. Otras compras de moneda ext…
  paso 5: leer_pasaje_pdf({"source_doc": "TO_exterior_cambios_actual.pdf", "location": "p.183-185"})
     → ii) El VPU deberá presentar la documentación que avale la capitalización definitiva del aporte. En caso de no dispone rla, deberá presentar constancia del inicio del trámite de inscripción ante el R…
  paso 6: leer_pasaje_pdf({"source_doc": "TO_exterior_cambios_actual.pdf", "location": "p.34-36"})
     → 3.10. Compra de moneda extranjera por parte de otros residentes –excluidas las entidades– para la  formación de activos externos y por operaciones con derivados.  El acceso al  mercado  de  cambios …

  ATRIBUCIONES EMITIDAS (par · jerarquía · portador según evidencia.nodo.ubicacion):
    1. {context_recall, estructural_kg} · primaria · portador: operador_de_cambio (ver_vecinos, paso 5) — sus únicas aristas son al TO de protección de u

  campo de justificación persistido: `razonamiento` (str, 2270 chars). Primeros 280:
    SÍNTOMA (C1a, por pata): la pata 1 fue aprobada por el juez; no se re-litiga. La pata 2 (¿el operador de cambio debe intervenir como entidad autorizada en el mercado de cambios?) nunca obtuvo su dato pertinente en la trayectoria: ningún nodo consultado responde si el operador de…

  HECHOS: leyó 4 pasajes (4 ubicaciones únicas):
    - TO_exterior_cambios_actual.pdf :: Punto 3.10
    - TO_exterior_cambios_actual.pdf :: Sección 15.1
    - TO_exterior_cambios_actual.pdf :: p.183-185
    - TO_exterior_cambios_actual.pdf :: p.34-36
  PUNTO COMPARATIVO CLAVE (¿leyó el 1.1 de Exterior?): NO LEÍDO

============================================================================
(4) validación run_4/CQ-017 [estructural_kg] — rep 3 (archivo off_run_4_CQ-017.json)
============================================================================
  paso 1: leer_pasaje_pdf({"source_doc": "TO_exterior_cambios_actual.pdf", "location": "Sección 15.1"})
     → 15.1. Artículos 1° y 2° del Decreto 260/02.  15.2. Artículos 1°, 2° y 3° del Decreto 609/19.  Tabla de correlaciones.  B.C.R.A. TEXTO ORDENADO DE LAS NORMAS SOBRE  \"EXTERIOR Y CAMBIOS\".  Versió…
  paso 2: leer_pasaje_pdf({"source_doc": "TO_exterior_cambios_actual.pdf", "location": "Punto 3.10"})
     → 3.10. Compra de moneda extranjera por parte de otros residentes –excluidas las  entidades– para la formación de activos externos y por operaciones con  derivados.  3.11. Otras compras de moneda ext…
  paso 3: leer_pasaje_pdf({"source_doc": "TO_exterior_cambios_actual.pdf", "location": "p.183-185"})
     → ii) El VPU deberá presentar la documentación que avale la capitalización definitiva del aporte. En caso de no dispone rla, deberá presentar constancia del inicio del trámite de inscripción ante el R…
  paso 4: leer_pasaje_pdf({"source_doc": "TO_exterior_cambios_actual.pdf", "location": "p.34-36"})
     → 3.10. Compra de moneda extranjera por parte de otros residentes –excluidas las entidades– para la  formación de activos externos y por operaciones con derivados.  El acceso al  mercado  de  cambios …
  paso 11: leer_pasaje_pdf({"source_doc": "TO_exterior_cambios_actual.pdf", "location": "p.140-142"})
     → Si la nacionalización de los bienes requiere un plazo mayor y el pago  anticipado se conc reta en su totalidad en el marco de lo previsto en los  puntos 10.10.2.3. a 10.10.2.6. o 10.10.2.14.ii), la …

  ATRIBUCIONES EMITIDAS (par · jerarquía · portador según evidencia.nodo.ubicacion):
    1. {context_recall, estructural_kg} · primaria · portador: entidad_autorizada y operador_de_cambio (ver_vecinos): no existe arista que los conecte

  campo de justificación persistido: `razonamiento` (str, 2425 chars). Primeros 280:
    SÍNTOMA: el juez marcó no_soportadas dos afirmaciones 'no central' que el agente insertó al reportar la pata 2 como no concluyente. Verifiqué su origen y verdad: ambas provienen de nodos consultados (mercado_libre_de_cambios paso 11, personas_juridicas_no_autorizadas paso 15) y l…

  HECHOS: leyó 5 pasajes (5 ubicaciones únicas):
    - TO_exterior_cambios_actual.pdf :: Punto 3.10
    - TO_exterior_cambios_actual.pdf :: Sección 15.1
    - TO_exterior_cambios_actual.pdf :: p.140-142
    - TO_exterior_cambios_actual.pdf :: p.183-185
    - TO_exterior_cambios_actual.pdf :: p.34-36
  PUNTO COMPARATIVO CLAVE (¿leyó el 1.1 de Exterior?): NO LEÍDO

============================================================================
(5a) validación run_4/CQ-019 [rep que ACERTÓ aplicacion_erronea] — rep 1 (archivo off_run_4_CQ-019.json)
============================================================================
  paso 1: leer_pasaje_pdf({"source_doc": "TO_capitales_minimos_actual.pdf", "location": "Punto 3.1.11.2"})
     → 3.1.11.2. Cálculo de las variables.     i) KSA.    Es la exigencia de capital promedio de las exposiciones subyacentes; es  decir, el ratio entre la suma de las exposiciones subyacentes ponderada…
  paso 3: leer_pasaje_pdf({"source_doc": "TO_capitales_minimos_actual.pdf", "location": "Punto 3.1.11.1"})
     → 3.1.11.1. Conceptos.    La información necesaria para calcular las siguientes variables será provista  o estimada por cada entidad:    i) KSA: exigencia de capital que hubiera correspondido a las…
  paso 4: leer_pasaje_pdf({"source_doc": "TO_capitales_minimos_actual.pdf", "location": "p.42"})
     → Las entidades deberán considerar la realidad o finalidad económica de la  transacción y aplicar estas definiciones de manera prudente en función de las  características de la estructura.     Si la…
  paso 5: leer_pasaje_pdf({"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Sección 1.1"})
     → 1.1. Criterio  general.  Los clientes de la entidad (tanto residentes en el país, de los sectores público y privado, finan- cieros y no financieros, como residentes en el exterior), por las financi…
  paso 6: leer_pasaje_pdf({"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Punto 6.5"})
     → 6.5. Niveles de clasificación. Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las s i- guientes cinco categorías, las que se definen teniendo en cuenta las co…
  paso 7: leer_pasaje_pdf({"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Punto 6.4.1"})
     → 6.4.1. Modificación de alguno de los criterios objetivos de clasificación que surjan de estas nor- mas (término de morosidad, situación jurídica del cliente o de sus deudas, cumplimiento  de refinan…

  ATRIBUCIONES EMITIDAS (par · jerarquía · portador según evidencia.nodo.ubicacion):
    1. {noise_sensitivity, aplicacion_erronea} · primaria · portador: prevision_especifica (abierto por el agente, paso 4)
    2. {context_recall, completitud_kg} · primaria · portador: categoria_de_clasificacion (paso 13) — no vincula categoría con determinación de prevision
    3. {faithfulness, alucinacion_agente} · secundaria · portador: ksa (paso 15)

  campo de justificación persistido: `razonamiento` (str, 3004 chars). Primeros 280:
    SÍNTOMA: el juez reprobó varias afirmaciones centrales. Descompuse en dos patas.

PATA 1 (qué previsión no se deduce): El agente respondió 'previsión específica' y 'monto bruto de la exposición', citando el nodo prevision_especifica (abierto en paso 4) y su edge a KSA. El conteni…

  HECHOS: leyó 6 pasajes (6 ubicaciones únicas):
    - TO_capitales_minimos_actual.pdf :: Punto 3.1.11.1
    - TO_capitales_minimos_actual.pdf :: Punto 3.1.11.2
    - TO_capitales_minimos_actual.pdf :: p.42
    - TO_clasificacion_deudores_actual.pdf :: Punto 6.4.1
    - TO_clasificacion_deudores_actual.pdf :: Punto 6.5
    - TO_clasificacion_deudores_actual.pdf :: Sección 1.1
  PUNTO COMPARATIVO CLAVE (¿leyó el 2.3.1 además del 3.1.11?): NO LEÍDO

============================================================================
(5b) validación run_4/CQ-019 [una rep de navegación] — rep 2 (archivo off_run_4_CQ-019.json)
============================================================================
  paso 1: leer_pasaje_pdf({"source_doc": "TO_capitales_minimos_actual.pdf", "location": "Punto 3.1.11.2"})
     → 3.1.11.2. Cálculo de las variables.     i) KSA.    Es la exigencia de capital promedio de las exposiciones subyacentes; es  decir, el ratio entre la suma de las exposiciones subyacentes ponderada…
  paso 2: leer_pasaje_pdf({"source_doc": "TO_capitales_minimos_actual.pdf", "location": "p.42-45"})
     → Las entidades deberán considerar la realidad o finalidad económica de la  transacción y aplicar estas definiciones de manera prudente en función de las  características de la estructura.     Si la…
  paso 8: leer_pasaje_pdf({"source_doc": "TO_capitales_minimos_actual.pdf", "location": "Punto 2.1"})
     → 2.1. Exigencia. 2.2. Exclusiones. 2.3. Cómputo de los conceptos comprendidos. 2.4. Requisitos de debida diligencia. 2.5. Criterios para la determinación de los activos ponderados por riesgo. 2.6.…
  paso 9: leer_pasaje_pdf({"source_doc": "TO_capitales_minimos_actual.pdf", "location": "p.7-10"})
     → A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras se clasificarán en: i) Grupo 1: entidades calificadas por el BCRA como de importancia sistémica …
  paso 10: leer_pasaje_pdf({"source_doc": "TO_capitales_minimos_actual.pdf", "location": "Punto 2.3"})
     → 2.3. Cómputo de los conceptos comprendidos. 2.3.1. Bases individual y consolidada mensual. Los conceptos comprendidos se computarán sobre la base de los saldos al último día de cada mes (capitales,…
  paso 11: leer_pasaje_pdf({"source_doc": "TO_capitales_minimos_actual.pdf", "location": "Punto 2.4"})
     → 2.4. Requisitos de debida diligencia. Las entidades financieras del grupo 1 deberán llevar a cabo un proceso de debida diligencia –al momento del otorgamiento del crédito y con frecuencia mínima anu…
  paso 16: leer_pasaje_pdf({"source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Punto 6.5.1"})
     → {"localizacion_pdf": "fallida", "source_doc": "TO_clasificacion_deudores_actual.pdf", "location": "Punto 6.5.1", "ref": "Punto/Sección 6.5.1 (mejor score=-76 < 6)", "mensaje": "No se pudo anclar el pa…

  ATRIBUCIONES EMITIDAS (par · jerarquía · portador según evidencia.nodo.ubicacion):
    1. {context_recall, navegación} · primaria · portador: deudores_clasificados_en_situacion_normal (nodo portador de la respuesta; NUNCA apareció e
    2. {context_recall, navegación} · primaria · portador: deudores_clasificados_en_situacion_normal (la vinculación correcta es directa: la categorí
    3. {noise_sensitivity, aplicacion_erronea} · secundaria · portador: prevision_especifica (fiel al PDF pero su alcance es el régimen de titulizaciones/KSA, dec

  campo de justificación persistido: `razonamiento` (str, 2639 chars). Primeros 280:
    SÍNTOMA: el juez marcó falsos los claims centrales sobre qué previsión no se deduce ('previsión específica' / 'monto bruto' / 'KSA'). MÉTODO por patas: (1) La pata central pregunta qué previsión NO se deduce al computar los activos (A) para la exigencia GENERAL por riesgo de créd…

  HECHOS: leyó 7 pasajes (7 ubicaciones únicas):
    - TO_capitales_minimos_actual.pdf :: Punto 2.1
    - TO_capitales_minimos_actual.pdf :: Punto 2.3
    - TO_capitales_minimos_actual.pdf :: Punto 2.4
    - TO_capitales_minimos_actual.pdf :: Punto 3.1.11.2
    - TO_capitales_minimos_actual.pdf :: p.42-45
    - TO_capitales_minimos_actual.pdf :: p.7-10
    - TO_clasificacion_deudores_actual.pdf :: Punto 6.5.1
  PUNTO COMPARATIVO CLAVE (¿leyó el 2.3.1 además del 3.1.11?): LEÍDO

============================================================================
RESUMEN
============================================================================
  (1) piloto run_3/CQ-018 [mayoría contenido_kg] rep1: 8 ubicaciones únicas · ¿leyó el 10.1 de Clasificación? → LEÍDO
  (1) piloto run_3/CQ-018 [mayoría contenido_kg] rep2: 11 ubicaciones únicas · ¿leyó el 10.1 de Clasificación? → LEÍDO
  (2) piloto run_3/CQ-033 [mayoría contenido_kg-primaria] rep1: 2 ubicaciones únicas · ¿leyó el 7.3/7.3.2 además del 12.3? → LEÍDO
  (2) piloto run_3/CQ-033 [mayoría contenido_kg-primaria] rep2: 2 ubicaciones únicas · ¿leyó el 7.3/7.3.2 además del 12.3? → LEÍDO
  (3) validación run_2/CQ-018 [contenido_kg] rep1: 10 ubicaciones únicas · ¿leyó el 10.1 de Clasificación? → NO LEÍDO
  (3) validación run_2/CQ-018 [contenido_kg] rep2: 8 ubicaciones únicas · ¿leyó el 10.1 de Clasificación? → NO LEÍDO
  (4) validación run_4/CQ-017 [estructural_kg] rep2: 4 ubicaciones únicas · ¿leyó el 1.1 de Exterior? → NO LEÍDO
  (4) validación run_4/CQ-017 [estructural_kg] rep3: 5 ubicaciones únicas · ¿leyó el 1.1 de Exterior? → NO LEÍDO
  (5a) validación run_4/CQ-019 [rep que ACERTÓ aplicacion_erronea] rep1: 6 ubicaciones únicas · ¿leyó el 2.3.1 además del 3.1.11? → NO LEÍDO
  (5b) validación run_4/CQ-019 [una rep de navegación] rep2: 7 ubicaciones únicas · ¿leyó el 2.3.1 además del 3.1.11? → LEÍDO
```

## Tabla final — caso × rep × lectura × punto comparativo clave × atribución

| Caso / rep | Pasajes leídos (ubicaciones únicas) | Punto comparativo clave | Atribución primaria emitida |
|---|---|---|---|
| (1) piloto r3/CQ-018 rep1 | 8 — 4.x y 6.x de Clasificación, 10.1 incluido | ¿10.1 de Clasificación? **LEÍDO** | {noise_sensitivity, contenido_kg} |
| (1) piloto r3/CQ-018 rep2 | 11 — ídem, 10.1 incluido | **LEÍDO** | {noise_sensitivity, contenido_kg} |
| (2) piloto r3/CQ-033 rep1 | 2 — **Punto 12.3 Y Punto 7.3** (el 7.3 con "7.3.1. El 20%..." en la ventana) | ¿7.3/7.3.2 además del 12.3? **LEÍDO** | {noise_sensitivity, contenido_kg} (primaria) |
| (2) piloto r3/CQ-033 rep2 | 2 — ídem | **LEÍDO** | {noise_sensitivity, contenido_kg} (primaria) |
| (3) valid. r2/CQ-018 rep1 | 10 — 4.x/6.x/7.x de Clasificación y Protección | ¿10.1 de Clasificación? **NO LEÍDO** | {noise_sensitivity, contenido_kg} |
| (3) valid. r2/CQ-018 rep2 | 8 — ídem | **NO LEÍDO** | {noise_sensitivity, contenido_kg} |
| (4) valid. r4/CQ-017 rep2 | 4 — Protección 1.1.x/3.x | ¿1.1 de Exterior? **NO LEÍDO** | {context_recall, estructural_kg} |
| (4) valid. r4/CQ-017 rep3 | 5 — ídem | **NO LEÍDO** | {context_recall, estructural_kg} |
| (5a) valid. r4/CQ-019 rep1 (la que acertó) | 6 — 3.1.11.1/3.1.11.2/p.42 de Capitales + 1.1/6.4.1/6.5 de Clasificación | ¿2.3.1 además del 3.1.11? **NO LEÍDO** | {noise_sensitivity, aplicacion_erronea} + {context_recall, completitud_kg} |
| (5b) valid. r4/CQ-019 rep2 (navegación) | 7 — 3.1.11.2/p.42-45 + **Punto 2.1, Punto 2.3** (la ventana muestra "2.3.1. Bases...") + 2.4 + 6.5.1 (localización fallida) | **LEÍDO** (Punto 2.3, cuya ventana incluye el encabezado 2.3.1) | {context_recall, navegación} ×2 |

**Hechos transversales del trazado (sin adjudicar):**

- En el piloto (run_3), las reps de la mayoría de CQ-018 y CQ-033 **SÍ leyeron los puntos
  comparativos clave** (10.1; 7.3) y emitieron igualmente `contenido_kg`.
- En la validación, las reps de r2/CQ-018 y r4/CQ-017 **NO leyeron** los puntos comparativos
  (10.1 de Clasificación; 1.1 de Exterior).
- En r4/CQ-019, la rep que emitió `aplicacion_erronea` (5a) **no leyó el 2.3.1** — su
  razonamiento persistido ancla en el alcance declarado del nodo (KSA) —; la rep de
  `navegación` (5b) **sí leyó el Punto 2.3** (además de intentar 6.5.1 de Clasificación, con
  `localizacion_pdf: "fallida"` — registrada verbatim).
- Una `localizacion_pdf: "fallida"` real quedó capturada en el trazado (5b, paso 16).

---

*Fin de B1c. Hechos para el diseño de v7. Frenado para revisión.*
