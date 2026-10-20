# Material de T4 — cola (30 fichas; B6.1, tanda final, T3, punto 7.5)

Sorteo: `cola.json` (4d447ca8…, 2026-10-20T14:08:58-03:00); material armado a las 2026-10-20T14:09:10-03:00. Sin el estado de E3 ni las marcas de E3.

## 1. `ri_dsf::S1` — RI:sin_raiz · cola

Texto que vio E3 (e0, bloque de lista True; págs. 1):

```
[texto propio | punto S1]
1.Instrucciones generales.
Los importes se expresarán en miles de pesos sin decimales. A los fines del redondeo de las
magnitudes se incrementarán los valores en una unidad cuando el primer dígito de las fracciones
sea igual o mayor que 5, desechando las que resulten inferiores.
Las entidades deberán remitir mensualmente los datos solicitados en los siguientes apartados:
-A “Datos Identificatorios del Deudor”,
-B “Datos sobre la Asistencia al Deudor”,
-D “Datos Agregados de la Entidad” y
Además, y con el nivel de requerimiento que a cada uno le corresponda, deberán presentar esta
información los proveedores no financieros de crédito, los administradores de carteras crediticias
de ex-entidades financieras, los fiduciarios de fideicomisos financieros comprendidos en la Ley
de Entidades Financieras, las sociedades de garantía recíproca, los fondos de garantía de carác-
ter público y los proveedores de servicios de créditos entre particulares a través de plataformas.
```

Versión: primer intento (cola). Entidades 12, relaciones 20.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Régimen Informativo Digital de Servicios Financieros", "properties": {}, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Obligacion", "label": "Expresión de importes en miles de pesos", "properties": {"tipo": "otra", "descripcion": "Los importes se expresarán en miles de pesos sin decimales."}, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- {"local_id": "e2", "type": "Obligacion", "label": "Redondeo de magnitudes con criterio de 5", "properties": {"tipo": "otra", "descripcion": "A los fines del redondeo de las magnitudes se incrementarán los valores en una unidad cuando el primer dígito de las fracciones sea igual o mayor que 5, desechando las que resulten inferiores.", "umbrales": "igual o mayor que 5"}, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- {"local_id": "e3", "type": "Obligacion", "label": "Remisión mensual de datos identificatorios del deudor", "properties": {"tipo": "presentacion_informativa", "frecuencia": "mensualmente", "descripcion": "Las entidades deberán remitir mensualmente los datos identificatorios del deudor según el apartado A."}, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- {"local_id": "e4", "type": "Obligacion", "label": "Remisión mensual de datos sobre asistencia al deudor", "properties": {"tipo": "presentacion_informativa", "frecuencia": "mensualmente", "descripcion": "Las entidades deberán remitir mensualmente los datos sobre la asistencia al deudor según el apartado B."}, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- {"local_id": "e5", "type": "Obligacion", "label": "Remisión mensual de datos agregados de la entidad", "properties": {"tipo": "presentacion_informativa", "frecuencia": "mensualmente", "descripcion": "Las entidades deberán remitir mensualmente los datos agregados de la entidad según el apartado D."}, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- {"local_id": "e6", "type": "Obligacion", "label": "Presentación de información por PNFC", "properties": {"tipo": "presentacion_informativa", "descripcion": "Los proveedores no financieros de crédito deberán presentar la información de los apartados A, B y D con el nivel de requerimiento que les corresponda."}, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- {"local_id": "e7", "type": "Obligacion", "label": "Presentación de información por administradores de carteras", "properties": {"tipo": "presentacion_informativa", "descripcion": "Los administradores de carteras crediticias de ex-entidades financieras deberán presentar la información de los apartados A, B y D con el nivel de requerimiento que les corresponda."}, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 7}
- {"local_id": "e8", "type": "Obligacion", "label": "Presentación de información por fiduciarios de fideicomisos", "properties": {"tipo": "presentacion_informativa", "descripcion": "Los fiduciarios de fideicomisos financieros comprendidos en la Ley de Entidades Financieras deberán presentar la información de los apartados A, B y D con el nivel de requerimiento que les corresponda."}, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_c
- {"local_id": "e9", "type": "Obligacion", "label": "Presentación de información por SGR", "properties": {"tipo": "presentacion_informativa", "descripcion": "Las sociedades de garantía recíproca deberán presentar la información de los apartados A, B y D con el nivel de requerimiento que les corresponda."}, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 9}
- {"local_id": "e10", "type": "Obligacion", "label": "Presentación de información por fondos de garantía públicos", "properties": {"tipo": "presentacion_informativa", "descripcion": "Los fondos de garantía de carácter público deberán presentar la información de los apartados A, B y D con el nivel de requerimiento que les corresponda."}, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 10}
- {"local_id": "e11", "type": "Obligacion", "label": "Presentación de información por PSCPP", "properties": {"tipo": "presentacion_informativa", "descripcion": "Los proveedores de servicios de créditos entre particulares a través de plataformas deberán presentar la información de los apartados A, B y D con el nivel de requerimiento que les corresponda."}, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 11}
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e3", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e4", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- relación: {"source": "e5", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- relación: {"source": "e6", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- relación: {"source": "e7", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- relación: {"source": "e8", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 7}
- relación: {"source": "e9", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 8}
- relación: {"source": "e10", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 9}
- relación: {"source": "e11", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 10}
- relación: {"source": "e3", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_sujeto_regulado", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 11}
- relación: {"source": "e4", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_sujeto_regulado", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 12}
- relación: {"source": "e5", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_sujeto_regulado", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 13}
- relación: {"source": "e6", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 14}
- relación: {"source": "e7", "target": null, "predicate": "aplica_a", "sujeto_id": null, "sujeto_propuesto": "los administradores de carteras crediticias de ex-entidades financieras", "sujeto_propuesto_padre_sugerido": "Sujeto_sujeto_regulado", "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 15}
- relación: {"source": "e8", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_fiduciario_de_fideicomiso_financiero", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 16}
- relación: {"source": "e9", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_sociedad_de_garantia_reciproca", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 17}
- relación: {"source": "e10", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_fondo_de_garantia_publico", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 18}
- relación: {"source": "e11", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_pscpp", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 19}

## 2. `ri_dsf::S8::chapeau_seccion` — RI:sin_raiz · cola

Texto que vio E3 (e0, bloque de lista True; págs. 5, 6, 7, 8, 9, 10, 11, 12, 13, 14):

```
[encabezado | punto S8]
8. Micro, pequeña y mediana empresa.
[bloque chapeau_seccion | punto S8]
Se deberá informar, en caso de corresponder, si el deudor cumple con los atributos esta-
blecidos en el Texto ordenado “Determinación de la condición de micro, pequeña o media-
na empresa”, definidos para micro, pequeña empresa y mediana empresa de acuerdo con
la siguiente codificación:
[TABLA ri_dsf::tabla000 | página 5 | e0_tablas | posicional]
Fila 1: col1 = Tamaño/Sector ⟨abarca hasta col3⟩ | col4 = Agropecuario ⟨abarca hasta col5⟩ | col7 = Industria y | col9 = Comercio | col10 = Servicios | col11 = Construcción ⟨abarca hasta col12⟩
Fila 2: col7 = Minería
Fila 3: col5 = - código a utilizar- ⟨abarca hasta col11⟩
Fila 4: col1 = Microempresa ⟨abarca hasta col3⟩ | col4 = 41 ⟨abarca hasta col5⟩ | col6 = 42 ⟨abarca hasta col8⟩ | col9 = 43 | col10 = 44 | col11 = 45 ⟨abarca hasta col12⟩
Fila 5: col2 = Pequeña | col4 = 51 ⟨abarca hasta col5⟩ | col6 = 52 ⟨abarca hasta col8⟩ | col9 = 53 | col10 = 54 | col11 = 55 ⟨abarca hasta col12⟩
Fila 6: col2 = Empresa
Fila 7: col2 = Mediana | col4 = 61 ⟨abarca hasta col5⟩ | col6 = 62 ⟨abarca hasta col8⟩ | col9 = 63 | col10 = 64 | col11 = 65 ⟨abarca hasta col12⟩
Fila 8: col2 = Empresa tramo 1
Fila 9: col2 = Mediana | col4 = 71 ⟨abarca hasta col5⟩ | col6 = 72 ⟨abarca hasta col8⟩ | col9 = 73 | col10 = 74 | col11 = 75 ⟨abarca hasta col12⟩
Fila 10: col2 = Empresa tramo 2
[FIN TABLA ri_dsf::tabla000]
3.Deudores del Sistema Financiero.
B. DATOS SOBRE LA ASISTENCIA AL DEUDOR
1. Situación.
Categoría de clasificación que corresponda al cliente según las normas sobre “Clasifica-
ción de deudores”.
Los deudores “no clasificados” por estar las asistencias cubiertas en su totalidad con ga-
rantías preferidas “A” se deberán informar cómo situación “normal”.
2. Financiaciones
Las financiaciones serán las comprendidas en las normas sobre “Clasificación de deudo-
res”, de acuerdo con los siguientes códigos de cuentas del Balance de Saldos al último día
de cada mes.
2.1. Asistencia crediticia y Títulos privados
2.1.1. Apertura por línea del rubro “Préstamos”
(códigos 131100, 131200, 131400, 131500, 131700, 131800, 132100, 132200,
135100, 135200, 135400, 135500, 135700, 135800, 136100 y 136200).
2.1.1.1. Adelantos
2.1.1.1.1. Con garantías preferidas “A”
2.1.1.1.2. Con garantías preferidas “B”
2.1.1.1.3. Sin garantías preferidas
2.1.1.2. Descuento de títulos de crédito
2.1.1.2.1. De acuerdo con el punto 1.1.11. de las normas sobre “Garan-
tías”.
3.Deudores del Sistema Financiero.
2.1.1.3. Documentos a Sola Firma, Descontados y Comprados
2.1.1.3.1. Con garantías preferidas “A”
2.1.1.3.2. Con garantías preferidas “B”
2.1.1.3.3. Sin garantías preferidas
2.1.1.4. Hipotecarios sobre la vivienda
2.1.1.4.1. Con garantías preferidas “A”
2.1.1.4.2. Con garantías preferidas “B”
2.1.1.4.3. Sin garantías preferidas
2.1.1.5. Con otras garantías hipotecarias
2.1.1.5.1. Con garantías preferidas “A”
2.1.1.5.2. Con garantías preferidas “B”
2.1.1.5.3. Sin garantías preferidas
2.1.1.6. Prendarios sobre automotores
2.1.1.6.1. Con garantías preferidas “A”
2.1.1.6.2. Con garantías preferidas “B”
2.1.1.6.3. Sin garantías preferidas
2.1.1.7. Con otras garantías prendarias
2.1.1.7.1. Con garantías preferidas “A”
2.1.1.7.2. Con garantías preferidas “B”
2.1.1.7.3. Sin garantías preferidas
2.1.1.8. Personales
2.1.1.8.1. Con garantías preferidas “A”
2.1.1.8.2. Con garantías preferidas “B”
2.1.1.8.3. Sin garantías preferidas
2.1.1.9. Personales de monto reducido
2.1.1.9.1. Con garantías preferidas “A”
2.1.1.9.2. Con garantías preferidas “B”
2.1.1.9.3. Sin garantías preferidas
3.Deudores del Sistema Financiero.
2.1.1.10. Tarjetas de Crédito
2.1.1.10.1. Con garantías preferidas “A”
2.1.1.10.2. Con garantías preferidas “B”
2.1.1.10.3. Sin garantías preferidas
2.1.1.11. Préstamos interfinancieros no previsionables
2.1.1.12. Préstamos a entidades financieras con participación estatal mayorita-
ria cubierta con garantía del gobierno de la respectiva jurisdicción.
2.1.1.13. Otros
2.1.1.13.1. Con garantías preferidas “A”
2.1.1.13.2. Con garantías preferidas “B”
2.1.1.13.3. Sin garantías preferidas
2.1.1.14. Créditos Adicionales
2.1.1.14.1. Con garantías preferidas “A”
2.1.1.14.2. Con garantías preferidas “B”
2.1.1.14.3. Sin garantías preferidas
2.1.1.14.4. Previsiones de los Créditos Adicionales
2.1.1.15. Préstamos a Instituciones de Microcrédito
2.1.1.15.1. Con garantías preferidas “A”
2.1.1.15.2. Con garantías preferidas “B”
2.1.1.15.3. Sin garantías preferidas
2.1.1.16. Préstamos a Microemprendedores
2.1.1.16.1. Con garantías preferidas “A”
2.1.1.16.2. Con garantías preferidas “B”
2.1.1.16.3. Sin garantías preferidas
2.1.1.17. Préstamos para prefinanciación y financiación de exportaciones
2.1.1.17.1. Con garantías preferidas “A”
2.1.1.17.2. Con garantías preferidas “B”
2.1.1.17.3. Sin garantías preferidas
2.1.1.18. Hipotecarios sobre la vivienda de Unidades de Valor Adquisitivo
2.1.1.18.1. Con garantías preferidas “A”
2.1.1.18.2. Con garantías preferidas “B”
2.1.1.18.3. Sin garantías preferidas
3.Deudores del Sistema Financiero.
2.1.1.19. Con otras garantías hipotecarias de Unidades de Valor Adquisitivo
2.1.1.19.1. Con garantías preferidas “A”
2.1.1.19.2. Con garantías preferidas “B”
2.1.1.19.3. Sin garantías preferidas
2.1.1.20. Prendarios sobre automotores de Unidades de Valor Adquisitivo
2.1.1.20.1. Con garantías preferidas “A”
2.1.1.20.2. Con garantías preferidas “B”
2.1.1.20.3. Sin garantías preferidas
2.1.1.21. Con otras garantías prendarias de Unidades de Valor Adquisitivo
2.1.1.21.1. Con garantías preferidas “A”
2.1.1.21.2. Con garantías preferidas “B”
2.1.1.21.3. Sin garantías preferidas
2.1.1.22. Otros préstamos de Unidades de Valor Adquisitivo
2.1.1.22.1. Con garantías preferidas “A”
2.1.1.22.2. Con garantías preferidas “B”
2.1.1.22.3. Sin garantías preferidas
2.1.1.23. Documentos a sola firma de Unidades de Valor Adquisitivo
2.1.1.23.1. Con garantías preferidas “A”
2.1.1.23.2. Con garantías preferidas “B”
2.1.1.23.3. Sin garantías preferidas
2.1.1.24. Hipotecarios sobre vivienda de Unidades de Vivienda
2.1.1.24.1. Con garantías preferidas “A”
2.1.1.24.2. Con garantías preferidas “B”
2.1.1.24.3. Sin garantías preferidas
2.1.1.25. Personales de Unidades de Valor Adquisitivo
2.1.1.25.1. Con garantías preferidas “A”
2.1.1.25.2. Con garantías preferidas “B”
2.1.1.25.3. Sin garantías preferidas
3.Deudores del Sistema Financiero.
2.1.1.26. Con otras garantías hipotecarios de Unidades de Vivienda
2.1.1.26.1. Con garantías preferidas “A”
2.1.1.26.2. Con garantías preferidas “B”
2.1.1.26.3. Sin garantías preferidas
2.1.1.27. Financiaciones a MiPyMEs que se destinen al pago de sueldos
(Com. “A” 6946)
2.1.1.27.1. Con garantías preferidas “A”
2.1.1.27.2. Con garantías preferidas “B”
2.1.1.27.3. Sin garantías preferidas
2.1.2. Otros créditos por intermediación financiera
(códigos 141131, 141136, 141139, 141141, 141154, 141192, 141201, 141250,
142154, 142192, 142201, 145131, 145136, 145139, 145141, 145154, 145192,
145201, 146136, 146139, 146141, 146154, 146192 y 146201).
2.1.2.1. Con garantías preferidas “A”
2.1.2.2. Con garantías preferidas “B”
2.1.2.3. Sin garantías preferidas
2.1.3. Créditos por arrendamientos financieros
2.1.3.1. Cuentas por cobrar por arrendamientos financieros
(códigos 151003, 151004, 151007, 151213, 151210, 155003, 155004, 155007
y 155210)
2.1.3.1.1. Con garantías preferidas “A”
2.1.3.1.2. Con garantías preferidas “B”
2.1.3.1.3. Sin garantías preferidas
2.1.3.2. Cuentas por cobrar por arrendamientos financieros de Unidades de Va-
lor Adquisitivo – Ley 25.827
(códigos 151005, 151211 y 151214)
2.1.1.27.1. Con garantías preferidas “A”
2.1.1.27.2. Con garantías preferidas “B”
2.1.1.27.3. Sin garantías preferidas
2.1.4. Créditos diversos
(códigos 171121, 171123, 171202, 171250, 175121, 175123 175202, 176121,
176123, 176202).
3.Deudores del Sistema Financiero.
2.1.4.1. Con garantías preferidas “A”
2.1.4.2. Con garantías preferidas “B”
2.1.4.3. Sin garantías preferidas
2.1.5. Obligaciones negociables – incluye las subordinadas – y títulos de deuda de fi-
deicomisos financieros, valuados a costo amortizado y/o a valor razonable con
cambios en otros resultados integrales.
(códigos 121045, 121046, 121047, 121048, 121049, 121050, 125047, 125048,
125049, 125050, 125051, 125052, 126013, 126014).
2.1.6. Respecto de los montos consignados en los apartados 2.1.1. al 2.1.4. (excepto
lo informado en el punto 2.1.1.11. y 2.1.1.12.) deberán informarse los saldos co-
rrespondientes a:
2.1.6.1. Con garantías preferidas “A”
2.1.6.1.1. Capital e Intereses devengados
2.1.6.2. Con garantías preferidas “B”
2.1.6.2.1. Capital e Intereses devengados no previsionables al 100%
2.1.6.2.2. Intereses devengados previsionables al 100%
2.1.6.3. Sin garantías preferidas
2.1.6.3.1. Capital e Intereses devengados no previsionables al 100%
2.1.6.3.2. Intereses devengados previsionables al 100%
2.1.7. De aquellos deudores cuya situación sea 3 o 4 (de acuerdo con las normas de
Clasificación de deudores y previsiones mínimas por riesgo de incobrabilidad),
deberá informarse el monto de la deuda vencida correspondiente a los importes
consignados en los apartados 2.1.1. a 2.1.4.
Se computarán los saldos incorporados por transferencia de cartera de otras entida-
des financieras de acuerdo con lo previsto en las normas sobre “Cesión de cartera de
créditos.”.
Las garantías a computar no deberán superar los importes de las correspondientes fa-
cilidades otorgadas, individualmente consideradas.
2.2. Garantías otorgadas
A los fines de la determinación de los montos a informar deberán tenerse en cuenta
los siguientes códigos 721033 y 725033
3.Deudores del Sistema Financiero.
2.2.1. Con contragarantías preferidas “A”
2.2.2. Con contragarantías preferidas “B”
2.2.3. Sin contragarantías preferidas
Las contragarantías a computar no deberán superar los importes de las correspon-
dientes facilidades otorgadas, individualmente consideradas.
2.3. Responsabilidades eventuales:
2.3.1. Se informarán los saldos no utilizados de adelantos en cuenta corriente acorda-
dos (721003, 721006 y 725006) según la siguiente apertura:
2.3.1.1. Con contragarantías preferidas “A”
2.3.1.2. Con contragarantías preferidas “B”
2.3.1.3. Sin contragarantías preferidas
2.3.2. A los fines de la determinación de los montos a informar a través de este punto
deberán tenerse en cuenta los siguientes códigos 721005, 721008, 721038,
725003, 725004, 725005 y 725008, incluyendo, además, el saldo al último día del
mes bajo informe correspondiente al total de los documentos redescontados en
entidades financieras -en pesos y moneda extranjera 711045 y 715045- por la di-
ferencia entre el valor nominal y los intereses documentados no devengados.
2.3.2.1. Con contragarantías preferidas “A”
2.3.2.2. Con contragarantías preferidas “B”
2.3.2.3. Sin contragarantías preferidas
3. Otros conceptos
3.1. Monto por Irrecuperables en Partidas fuera de Balance
Deberán tenerse en cuenta los códigos 711046 y 715046. En el caso de corresponder
se deberán deducir los pagos a cuenta registrados en “Cobros no aplicados – Deudo-
res registrados en Partidas fuera de balance” –321158 y 325158-
3.2. Financiaciones y fianzas, avales y otras responsabilidades otorgadas desde el exterior
Deberán tenerse en cuenta los códigos 721081, 721082, 725081 y 725082.
3.3. Diferencia por adquisición de cartera
Deberán tenerse en cuenta los códigos 131906, 132306, 135906 y 136306, correspon-
dientes a los saldos provenientes de la adquisición de pasivos de clientes del Sector Pri-
vado no Financiero
3. Deudores del Sistema Financiero.
4. Además, se deberá informar:
Categoría de clasificación que corresponda al cliente según las normas sobre “Clasificación
de deudores”, sin tener en cuenta la reclasificación obligatoria.
Los plazos de suspensión de la Recategorización obligatoria prevista en los puntos 6.6. y
7.3. de las normas sobre “Clasificación de deudores”, se encuentran detallados en las res-
pectivas Normas de presentación.
5. Refinanciaciones
Se deberá informar, en caso de corresponder, la fecha de la última refinanciación concertada
por tipo de asistencia.
En el caso de deudores calificados como “en negociación o con acuerdos de refinanciación”,
la fecha que se deberá informar será la correspondiente a la manifestación fehaciente de la
intención de refinanciar.
Esta fecha se deberá informar hasta el momento en que al deudor se lo reclasifique en si-
tuación normal.
6. Previsiones valuadas según NIIF. Previsiones por riesgo de incobrabilidad y provisiones
constituidas individualmente respecto de la deuda de cada cliente.
6.1. Por la asistencia crediticia registrada en Préstamos, Otros créditos por intermediación
financiera, Créditos por arrendamientos financieros, Créditos diversos y por los con-
ceptos incluidos de Títulos privados (códigos 121135, 125135, 126135, 131601,
131901, 132301, 135601, 135901, 136301, 141301, 142301, 145301, 146301, 151312,
155312, 171302, 175302, 176302).
6.2. Por Responsabilidades eventuales y Garantías otorgadas. (código 340018).
6.3. En caso de que la entidad haya optado de acuerdo con lo dispuesto en el punto 2.2.3.
de las normas sobre “Previsiones mínimas por riesgo de incobrabilidad, se informará el
incremento de previsión correspondiente.
3. Deudores del Sistema Financiero.
7. Máxima asistencia.
En los casos de clientes vinculados o de aquellos cuyo saldo de deuda en algún momento
del mes supere el 0,5% de la Responsabilidad Patrimonial Computable de la entidad co-
rrespondiente al mes anterior o el equivalente al 40% de dos veces el importe de referencia
establecido en el punto 3.7 de las normas sobre “Clasificación de deudores”, de ambos el
mayor, no obstante informar su saldo a fin de mes, se suministrará el importe correspon-
diente a la máxima asistencia del período.
Dicha máxima asistencia deberá informarse aún en aquellos casos en que el saldo de deu-
da a fin de mes sea cero.
8. Deudores de la cartera para consumo o vivienda en situación distinta a la normal:
```

Versión: primer intento (cola). Entidades 21, relaciones 21.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Régimen Informativo Deudores", "properties": {}, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapeau_seccion"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Obligacion", "label": "Informar condición MiPyME según codificación", "properties": {"tipo": "presentacion_informativa", "descripcion": "Obligación de informar si el deudor cumple con los atributos de micro, pequeña o mediana empresa según la codificación establecida en el Texto Ordenado de Determinación de la condición de MiPyME, con códigos específicos por tamaño y sector (Agropecuario, Industria y Minería, Comercio, Servicios, Construcción): Microempresa (códigos 4
- {"local_id": "e2", "type": "Definicion", "label": "Codificación de MiPyME por tamaño y sector", "properties": {"termino": "Codificación de micro, pequeña y mediana empresa", "descripcion": "Tabla de códigos que clasifica a las MiPyME por tamaño (Microempresa, Pequeña Empresa, Mediana Empresa tramo 1, Mediana Empresa tramo 2) y por sector económico (Agropecuario, Industria y Minería, Comercio, Servicios, Construcción), con códigos numéricos específicos para cada combinación de tamaño y sector."},
- {"local_id": "e3", "type": "Obligacion", "label": "Informar categoría de clasificación del cliente", "properties": {"tipo": "presentacion_informativa", "descripcion": "Obligación de informar la categoría de clasificación que corresponda al cliente de acuerdo con las normas sobre Clasificación de deudores."}, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapeau_seccion"}, "indice_crudo": 3}
- {"local_id": "e4", "type": "Obligacion", "label": "Informar deudores no clasificados como situación normal", "properties": {"tipo": "presentacion_informativa", "descripcion": "Obligación de informar como situación \"normal\" a los deudores no clasificados cuyas asistencias estén cubiertas en su totalidad con garantías preferidas \"A\"."}, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapeau_seccion"}, "indice_crudo": 4}
- {"local_id": "e5", "type": "Obligacion", "label": "Informar financiaciones según normas de Clasificación", "properties": {"tipo": "presentacion_informativa", "descripcion": "Obligación de informar las financiaciones comprendidas en las normas sobre Clasificación de deudores, utilizando los códigos de cuentas del Balance de Saldos al último día de cada mes."}, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapeau_seccion"}, "indice_crudo": 5}
- {"local_id": "e6", "type": "Restriccion", "label": "Límite de garantías a computar", "properties": {"tipo": "limite_cuantitativo", "descripcion": "Las garantías a computar no pueden superar los importes de las facilidades otorgadas, consideradas individualmente.", "umbrales": "no deberán superar los importes de las correspondientes facilidades otorgadas, individualmente consideradas"}, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapeau_seccio
- {"local_id": "e7", "type": "Obligacion", "label": "Informar garantías otorgadas según códigos específicos", "properties": {"tipo": "presentacion_informativa", "descripcion": "Obligación de informar garantías otorgadas considerando los códigos 721033 y 725033 para la determinación de los montos."}, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapeau_seccion"}, "indice_crudo": 7}
- {"local_id": "e8", "type": "Restriccion", "label": "Límite de contragarantías a computar", "properties": {"tipo": "limite_cuantitativo", "descripcion": "Las contragarantías a computar no pueden superar los importes de las facilidades otorgadas, consideradas individualmente.", "umbrales": "no deberán superar los importes de las correspondientes facilidades otorgadas, individualmente consideradas"}, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_ch
- {"local_id": "e9", "type": "Obligacion", "label": "Informar saldos no utilizados de adelantos en cuenta corriente", "properties": {"tipo": "presentacion_informativa", "descripcion": "Obligación de informar los saldos no utilizados de adelantos en cuenta corriente acordados, utilizando los códigos 721003, 721006 y 725006, con apertura según garantías preferidas."}, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapeau_seccion"}, "indice_crudo": 9
- {"local_id": "e10", "type": "Obligacion", "label": "Informar responsabilidades eventuales según códigos", "properties": {"tipo": "presentacion_informativa", "descripcion": "Obligación de informar responsabilidades eventuales considerando códigos 721005, 721008, 721038, 725003, 725004, 725005 y 725008, incluyendo el saldo al último día del mes de documentos redescontados en entidades financieras (códigos 711045 y 715045) por la diferencia entre valor nominal e intereses documentados no devengados
- {"local_id": "e11", "type": "Obligacion", "label": "Informar monto por irrecuperables en partidas fuera de balance", "properties": {"tipo": "presentacion_informativa", "descripcion": "Obligación de informar el monto por irrecuperables en partidas fuera de balance considerando códigos 711046 y 715046, deduciendo los pagos a cuenta registrados en Cobros no aplicados (códigos 321158 y 325158)."}, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapea
- {"local_id": "e12", "type": "Obligacion", "label": "Informar financiaciones y fianzas desde el exterior", "properties": {"tipo": "presentacion_informativa", "descripcion": "Obligación de informar financiaciones y fianzas, avales y otras responsabilidades otorgadas desde el exterior, considerando códigos 721081, 721082, 725081 y 725082."}, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapeau_seccion"}, "indice_crudo": 12}
- {"local_id": "e13", "type": "Obligacion", "label": "Informar diferencia por adquisición de cartera", "properties": {"tipo": "presentacion_informativa", "descripcion": "Obligación de informar la diferencia por adquisición de cartera considerando códigos 131906, 132306, 135906 y 136306, correspondientes a saldos provenientes de adquisición de pasivos de clientes del Sector Privado no Financiero."}, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_cha
- {"local_id": "e14", "type": "Obligacion", "label": "Informar categoría de clasificación sin reclasificación obligatoria", "properties": {"tipo": "presentacion_informativa", "descripcion": "Obligación de informar la categoría de clasificación que corresponda al cliente según normas sobre Clasificación de deudores, sin considerar la reclasificación obligatoria."}, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapeau_seccion"}, "indice_crudo": 14}
- {"local_id": "e15", "type": "Obligacion", "label": "Informar fecha de última refinanciación", "properties": {"tipo": "presentacion_informativa", "descripcion": "Obligación de informar, cuando corresponda, la fecha de la última refinanciación concertada por tipo de asistencia."}, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapeau_seccion"}, "indice_crudo": 15}
- {"local_id": "e16", "type": "Obligacion", "label": "Informar fecha de manifestación de intención de refinanciar", "properties": {"tipo": "presentacion_informativa", "descripcion": "Obligación de informar, para deudores calificados como \"en negociación o con acuerdos de refinanciación\", la fecha de la manifestación fehaciente de la intención de refinanciar."}, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapeau_seccion"}, "indice_crudo": 16}
- {"local_id": "e17", "type": "Condicion", "label": "Hasta reclasificación en situación normal", "properties": {"descripcion": "La fecha de refinanciación se informa hasta el momento en que el deudor sea reclasificado en situación normal."}, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapeau_seccion"}, "indice_crudo": 17}
- {"local_id": "e18", "type": "Obligacion", "label": "Informar previsiones por riesgo de incobrabilidad", "properties": {"tipo": "presentacion_informativa", "descripcion": "Obligación de informar previsiones valuadas según NIIF y provisiones por riesgo de incobrabilidad constituidas individualmente respecto de la deuda de cada cliente."}, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapeau_seccion"}, "indice_crudo": 18}
- {"local_id": "e19", "type": "Obligacion", "label": "Informar máxima asistencia del período", "properties": {"tipo": "presentacion_informativa", "descripcion": "Obligación de informar la máxima asistencia del período para clientes vinculados o cuyo saldo de deuda supere el 0,5% de la Responsabilidad Patrimonial Computable del mes anterior o el equivalente al 40% de dos veces el importe de referencia del punto 3.7 de normas sobre Clasificación de deudores, considerando el mayor de ambos.", "umbral
- {"local_id": "e20", "type": "Obligacion", "label": "Informar máxima asistencia aun con saldo cero", "properties": {"tipo": "presentacion_informativa", "descripcion": "Obligación de informar la máxima asistencia incluso en casos en que el saldo de deuda a fin de mes sea cero."}, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapeau_seccion"}, "indice_crudo": 20}
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapeau_seccion"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapeau_seccion"}, "indice_crudo": 1}
- relación: {"source": "e3", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapeau_seccion"}, "indice_crudo": 2}
- relación: {"source": "e4", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapeau_seccion"}, "indice_crudo": 3}
- relación: {"source": "e5", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapeau_seccion"}, "indice_crudo": 4}
- relación: {"source": "e6", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapeau_seccion"}, "indice_crudo": 5}
- relación: {"source": "e7", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapeau_seccion"}, "indice_crudo": 6}
- relación: {"source": "e8", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapeau_seccion"}, "indice_crudo": 7}
- relación: {"source": "e9", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapeau_seccion"}, "indice_crudo": 8}
- relación: {"source": "e10", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapeau_seccion"}, "indice_crudo": 9}
- relación: {"source": "e11", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapeau_seccion"}, "indice_crudo": 10}
- relación: {"source": "e12", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapeau_seccion"}, "indice_crudo": 11}
- relación: {"source": "e13", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapeau_seccion"}, "indice_crudo": 12}
- relación: {"source": "e14", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapeau_seccion"}, "indice_crudo": 13}
- relación: {"source": "e15", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapeau_seccion"}, "indice_crudo": 14}
- relación: {"source": "e16", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapeau_seccion"}, "indice_crudo": 15}
- relación: {"source": "e17", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapeau_seccion"}, "indice_crudo": 16}
- relación: {"source": "e18", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapeau_seccion"}, "indice_crudo": 17}
- relación: {"source": "e19", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapeau_seccion"}, "indice_crudo": 18}
- relación: {"source": "e20", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapeau_seccion"}, "indice_crudo": 19}
- relación: {"source": "e17", "target": "e15", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dsf", "archivo": "ri_dsf.pdf", "punto": "S8", "rol_documental": "bloque_chapeau_seccion"}, "indice_crudo": 20}

## 3. `ri_iepsp::A::S4` — RI:sin_raiz · cola

Texto que vio E3 (e0, bloque de lista True; págs. 2, 3, 4, 5, 6, 7):

```
[encabezado | punto A]
-ANEXO-
[encabezado | punto A::Sbloque1]
CUIT N° [completar]
[texto propio | punto A::S4]
4. Tarea profesional
Nuestra tarea profesional fue desarrollada de conformidad con las normas sobre informes especia-
les establecidas por la Resolución Técnica N° 37 de la Federación Argentina de Consejos Profesio-
nales de Ciencias Económicas (en adelante “RT 37”) y consistió en la aplicación de ciertos procedi-
mientos necesarios para verificar el cumplimiento por parte de la Sociedad de los requerimientos del
BCRA en relación con las normas sobre “Proveedores no financieros de crédito”. La RT 37 exige
que cumplamos los requerimientos de ética, así como que planifiquemos y ejecutemos nuestra ta-
rea de tal forma que nos permita emitir el presente informe especial.
En un encargo para emitir un informe especial, el contador aplica una serie de procedimientos para
verificar el cumplimiento por parte de la Sociedad de determinados requerimientos del organismo de
control, y se limita a dar una manifestación de hallazgos sobre la base de los resultados obtenidos
de esos procedimientos. Este servicio mejora la confiabilidad de la información objeto del trabajo, al
estar acompañada por una manifestación profesional independiente. En consecuencia, nuestro tra
-2-
bajo no constituye una auditoría, una revisión de estados contables ni otro encargo de aseguramien-
to.
[En caso de que este informe lo emita el auditor, se puede agregar el párrafo siguiente:
En nuestro carácter de auditores externos de la Sociedad, hemos auditado los estados financieros
de la misma al __ de _____ de 20__, preparados de acuerdo con el [indicar el marco de información
contable], respecto de los cuales hemos emitido con fecha __ de ______ de 20__ nuestro informe
del auditor independiente sin salvedades [o con salvedades, adaptar según sea el caso], al cual nos
remitimos. No hemos efectuado ninguna auditoría sobre ningún estado financiero de la Sociedad, a
ninguna fecha y por ningún período posterior al __ de ______ de 20__.]
Los procedimientos detallados a continuación, en lo que es materia de nuestra competencia y en
ciertos casos efectuados sobre bases selectivas, han sido aplicados sobre los registros y documen-
tación que nos fueron suministrados por la Sociedad. Adicionalmente, para la ejecución de dichos
procedimientos hemos tenido en cuenta nuestro entendimiento del entorno de control interno de la
Sociedad en lo vinculado con los aspectos revisados y otros aspectos.
[adaptar y/o eliminar los procedimientos enumerados a continuación según sea aplicable a la opera-
toria de cada proveedor no financiero de crédito]
A. Tasas de interés en operaciones de crédito
i. Verificar para las financiaciones alcanzadas lo establecido en los puntos 1.3. “Bases de
liquidación”, 1.4. “Modalidades de aplicación”,1.5. “Divisor fijo” y 1.6. “Intereses punito-
rios” de las normas sobre “Tasas de interés en las operaciones de crédito”, por medio de
la revisión de la fórmula utilizada para el cálculo de los intereses y/o del reproceso del in-
terés de una muestra representativa de casos determinada a partir del universo de ope-
raciones vigentes durante el período comprendido entre __ y __ [debe abarcar el año
cubierto por la revisión].
ii. Respecto a las financiaciones vinculadas a tarjetas de crédito, por medio de la revisión
de una muestra representativa de casos determinada a partir del universo de operacio-
nes vigentes durante el período comprendido entre __ y __ [debe abarcar el año cubierto
por la revisión] verificar respecto al Interés Compensatorio lo establecido en los puntos
2.1.2. “Otras empresas emisoras” y 2.1.3. “Forma de cómputo” y respecto al Interés Pu-
nitorio lo establecido en el punto 2.2. de las normas sobre “Tasas de interés en las ope-
raciones de crédito”. Verificar además el cumplimiento de los puntos normativos citados
también en caso de refinanciaciones de saldos, de acuerdo con lo dispuesto en el punto
2.3. “Financiaciones otorgadas para refinanciar saldos adeudados de tarjetas de crédito”
de la referida normativa.
iii. Verificar por medio de la revisión de una muestra representativa de contratos, resúme-
nes de tarjeta de crédito y/o casos determinada a partir del universo de operaciones vi-
gentes durante el período comprendido entre __ y __ [debe abarcar el año cubierto por la
revisión], que las comisiones y cargos cobrados a usuarios se ajusten con lo establecido
en los puntos 1.7. “Comisiones y cargos adicionales a los intereses” de las normas sobre
“Tasas de interés en las operaciones de crédito” y 2.3.2. “Comisiones y cargos” de las
normas sobre de “Protección de los usuarios de servicios financieros”.
iv. Respecto al ofrecimiento publicitario, a través de cualquier medio masivo o individual, de
créditos específicos, evaluar la existencia de políticas y procedimientos establecidos por
la Sociedad a efectos de garantizar el cumplimiento de lo establecido en la Sección 4.
“Publicidad” de las normas sobre “Tasas de interés en las operaciones de crédito”. [En
caso de inexistencia de políticas y procedimientos, verificar mediante la obtención de una
-3-
muestra representativa de publicidades en medios gráficos, radiales, televisivos, telefóni-
cos y otros medios, durante el período comprendido entre __ y __ [debe abarcar el año
cubierto por la revisión], el cumplimiento de lo dispuesto en la Sección 4. “Publicidad” de
las normas sobre “Tasas de interés en las operaciones de crédito”.]
B. Protección de usuarios de servicios financieros
i. Respecto de los modelos de contratos y otros instrumentos utilizados por la Sociedad
durante el período comprendido entre __ y __ [debe abarcar el año cubierto por la revi-
sión] en relación con las operaciones de crédito concertadas con sus clientes:
a. Verificar el cumplimiento de lo dispuesto en el punto 2.3.1. “Recaudos mínimos de la
relación de consumo - Al momento de la contratación del producto o servicio”, de las
normas sobre de “Protección de los usuarios de servicios financieros”, constatando
además la entrega al usuario de copias de los instrumentos suscriptos de acuerdo
con lo establecido en el punto 2.4. “Publicidad de la información” de la referida nor-
mativa, mediante la obtención de una muestra representativa de casos determinada a
partir del universo de operaciones vigentes durante el período comprendido entre __
y __ [debe abarcar el año cubierto por la revisión].
b. Constatar que el modelo de contrato no prevea la modificación de la tasa de interés
en determinadas circunstancias para el caso de contratos a tasa fija y determine los
parámetros a emplear en la determinación de la tasa de interés para los instrumentos
concertados a tasa variable de acuerdo con lo indicado en el punto 1.2. de la Sección
1. “Aspectos generales” de las normas sobre “Tasa de interés en operaciones de cré-
dito”.
c. Verificar la inexistencia de cláusulas que restrinjan los derechos de los usuarios o
desnaturalicen las obligaciones de los sujetos obligados, señaladas en el punto 2.3.9.
“Cláusulas abusivas” de las normas sobre “Protección de los usuarios de servicios fi-
nancieros”.
ii. En relación con la exposición de la tasa de interés y del Costo Financiero Total (CFT) ve-
rificar sobre la base de una muestra representativa de contratos y/o casos determinada a
partir del universo de operaciones vigentes durante el período comprendido entre __ y __
[debe abarcar el año cubierto por la revisión], los siguientes aspectos:
a. Que en cumplimiento de lo indicado en la Sección 3. “Expresión de Tasas” en su pun-
to 3.2. “Exposición en los documentos” de las normas sobre de “Tasa de interés en
operaciones de crédito” se deje constancia de (i) tasa de interés o de descuento
anual contractualmente pactada en tanto por ciento con al menos un decimal, (ii) tasa
de interés efectiva anual equivalente al cálculo de los intereses en forma vencida en
tanto por ciento con al menos un decimal, (iii) carácter fijo o variable de la tasa de in-
terés, con indicación en este último caso de los parámetros que se emplearán para
su determinación y periodicidad del cambio, y (iv) CFT.
b. Que a efectos de la exposición de la tasa de interés efectiva anual se utilicen las fór-
mulas previstas en el punto 3.3. “Cálculo de la tasa de interés efectiva anual” de las
normas sobre “Tasa de interés en operaciones de crédito”.
c. Que a efectos de la exposición del CFT se utilicen las fórmulas previstas en el punto
3.4. “Costo financiero total” de las normas sobre “Tasa de interés en operaciones de
crédito”.
-4-
d. Que los resúmenes de cuenta incluyan las leyendas dispuestas en el punto 2.3.14.
“Información al usuario” de las normas sobre “Protección de los usuarios de servicios
financieros”
iii. Respecto del cambio en las condiciones pactadas, constatar:
a. Que en los contratos las condiciones que puedan ser modificadas estén taxativamen-
te especificadas.
b. En caso de existir modificaciones en las condiciones pactadas, verificar para una
muestra de casos el cumplimiento de lo dispuesto en el punto 2.3.4. “Cambios de
condiciones pactadas” de las normas sobre “Protección de los usuarios de servicios
financieros” en cuanto a la notificación al usuario.
c. Verificar la información al BCRA de las comisiones y cargos percibidos, y de las altas
y los aumentos en las comisiones que deseen implementar a través del régimen in-
formativo previsto a ese efecto, así como su notificación a los usuarios de acuerdo
con lo indicado en el punto 2.5. “Información al Banco Central de la República Argen-
tina” de las normas sobre “Protección de los usuarios de servicios financieros”.
iv. Verificar lo establecido en el punto 2.3.12. “Seguros como contratación accesoria a un
servicio financiero” de las normas sobre “Protección de los usuarios de servicios financie-
ros” en cuanto a que no se cobre a los usuarios seguro de vida sobre saldo deudor y, pa-
ra el caso de otros seguros accesorios, se ofrezcan al menos tres compañías asegurado-
ras, y lo establecido en el punto 2.3.13. “Seguros como contratación no accesoria al ser-
vicio financiero” de las normas sobre “Protección de los usuarios de servicios financieros”
en lo que respecta a que, si se ofrece seguros de este tipo, el proveedor no tenga ningún
tipo de retribución del usuario, por medio de la revisión de una muestra de contratos y/o
casos determinada a partir del universo de operaciones vigentes durante el período
comprendido entre __ y __ [debe abarcar el año cubierto por la revisión].
v. En caso de detectarse intereses, comisiones y/o cargos cobrados en exceso, verificar
que se haya cumplido con lo dispuesto en el punto 2.3.5. “Reintegro de importes” de las
normas sobre “Protección de los usuarios de servicios financieros”.
vi. Con relación al servicio de atención al usuario, verificar lo siguiente:
a. Que el Directorio de la Sociedad haya designado a un funcionario como responsable
de atención al usuario de servicios financieros en carácter de titular y por lo menos
otro como suplente según lo prescripto en el punto 3.1.1. “Responsable de atención
al usuario de servicios financieros (titular o suplente a cargo)” de las normas sobre de
“Protección de usuarios de servicios financieros”.
b. Que se hayan habilitado y se mantengan actualizados (i) el Registro Centralizado de
Consultas y Reclamos (RCCR) a que se refiere el punto 3.1.3. “Registro Centralizado
de Consultas y Reclamos (RCCR)”; (ii) el Registro de Reintegros de Importes (RRI)
previsto en el punto 3.1.4. “Registro de Reintegros de Importes (RRI)”; y (iii) el Regis-
tro de Denuncias ante Instancias Judiciales y/o Administrativas de Defensa del Con-
sumidor (RDJA) establecido en el punto 3.1.5. “Registro de Denuncias ante las Ins-
tancias Judiciales y/o Administrativas de Defensa del Consumidor (RDJA)” de las
normas sobre “Protección de usuarios de servicios financieros”.
c. Que se elabore y eleve al Directorio o al Directivo Responsable de Protección de los
Usuarios de Servicios Financieros o al Comité de Protección de los Usuarios de Ser
-5-
vicios Financieros –según corresponda–, con periodicidad como mínimo trimestral, un
reporte acerca de: (i) las consultas y reclamos recibidos; (ii) las intervenciones reque-
ridas por denuncias tramitadas ante las instancias judiciales y/o administrativas de
defensa del consumidor que resulten competentes y (iii) los reintegros de importes
realizados, en cumplimiento de lo establecido en el punto 3.1.1.8. de las normas so-
bre “Protección de usuarios de servicios financieros”.
d. Que el Directorio haya aprobado, previa toma de conocimiento del Comité de Audito-
ría [para el caso en que la Sociedad cuente con un Comité de Auditoría], los pasos y
recaudos a observar para la atención de consultas y reclamos de usuarios según lo
establecido en el punto 3.1.2 “Manual de Procedimiento” de las normas sobre “Pro-
tección de usuarios de servicios financieros”.
e. Que las normas y procedimientos establecidos por la Sociedad prevean las distintas
alternativas de presentaciones de consultas y reclamos de los usuarios de servicios
financieros tal lo previsto en el punto 3.1.6. “Recepción de las presentaciones y tiem-
po de respuestas” de las normas sobre “Protección de usuarios de servicios financie-
ros”, y
f. Que la Auditoría Interna de la Sociedad complete al menos anualmente una evalua-
ción integral de los procesos implementados a efectos de dar cumplimiento a las
normas sobre “Protección de usuarios de servicios financieros”. [sólo aplicable en ca-
so que la Sociedad cuente con un área de Auditoría Interna]
vii. Con relación a la comunicación por medios electrónicos para el cuidado del medio am-
biente, verificar lo siguiente:
a. Verificar que la entidad publique en su sitio web institucional la información prevista
en los puntos 5.2. “Modelos y ubicación de la información” y 5.3. “Información de difu-
sión obligatoria” de las normas sobre “Comunicación por medios electrónicos para el
cuidado del medio ambiente”.
b. Verificar que se cumpla con la difusión en los recintos de atención al público de la in-
formación detallada en los puntos 4.4.1.2., 4.4.1.7 y 4.5.1. de las normas sobre “Co-
municación por medios electrónicos para el cuidado del medio ambiente”, en las mo-
dalidades allí previstas.
C. Régimen informativo
i. Respecto de los regímenes informativos de Financiamiento con tarjetas de crédito, Deu-
dores del sistema financiero, Transparencia y Reclamos correspondientes al período
comprendido entre el .. de ….. de ….. y el .. de ….. de …..[debe abarcar el año cubierto
por la revisión]:
a. Constatar que la Sociedad haya presentado dichos regímenes informativos en cum-
plimiento de los plazos y diseños de presentación dispuestos por el BCRA.
b. Verificar para una muestra de casos que la información incorporada en dichos regí-
menes surja de los soportes o inventarios analíticos suministrados por la Sociedad o
con la respectiva documentación de respaldo.
c. Verificar la integridad de los regímenes informativos de Deudores del sistema finan-
ciero y Financiamiento con tarjeta de crédito para el período mensual correspondiente
-6-
al último mes del período de revisión mediante el cotejo de los totales de los mismos
con los registros contables correspondientes.
d. En cuanto al régimen informativo de Reclamos constatar que la Sociedad (a) haya di-
señado procedimientos y controles para asegurar que la información incorporada al
régimen surge del Registro centralizado de consultas y reclamos; y (b) haya incorpo-
rado la dirección URL correspondiente a la sección “Información al usuario financie-
ro”, punto 5.2. de las normas sobre “Comunicación por medios electrónicos para el
cuidado del medio ambiente”.
D. Proveedores no financieros de crédito
Verificar que se haya cumplido con la actualización de la información del registro requerida en
el punto 1.3.3. de las normas sobre “Proveedores no financieros de crédito”.
E. Requisitos mínimos para la gestión de los riesgos de tecnología y seguridad de la infor-
mación asociados a los servicios financieros digitales
Verificar que la Sociedad cumple con el punto 3.3 “Identificación digital de clientes” del
texto ordenado de “Requisitos mínimos para la gestión de los riesgos de tecnología y
seguridad de la información asociados a los servicios financieros digitales”, respecto
de los procesos y controles aplicables a la identificación/alta de clientes en el marco de
la operatoria de Cobro con Transferencia.
A tal efecto, se realizaron los siguientes procedimientos:
a) Corroborar que la Sociedad aplica mecanismos de validación de la presencia real
del cliente mediante pruebas de vida.
b) Verificar que la Sociedad implementa controles para validar los puntos de contacto
declarados por el cliente, así como el dispositivo móvil asociado.
c) Verificar que la Sociedad implementa mecanismos de validación biométrica y de ve-
rificación de la documentación contra fuentes externas u organismos públicos.
d) Evaluar la existencia y aplicación de técnicas complementarias de verificación de
identidad, en función de los análisis de riesgo efectuados por la Sociedad.
e) En relación con procesos de alta no concretados:
I. verificar que no se comunican al cliente los motivos específicos de fallas en el
proceso de identificación;
II. verificar la existencia de procesos de eliminación de datos mediante borrado
seguro;
III. verificar que los datos eventualmente conservados con fines estadísticos sean
anonimizados o desasociados.
```

Versión: primer intento (cola). Entidades 39, relaciones 74.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Régimen Informativo PNFC", "properties": {}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Operacion", "label": "Verificación de cumplimiento de normas BCRA", "properties": {"tipo": "verificación de cumplimiento normativo", "descripcion": "Aplicación de procedimientos para verificar el cumplimiento por parte de la Sociedad de los requerimientos del BCRA en relación con las normas sobre Proveedores no financieros de crédito, conforme a la Resolución Técnica N° 37"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental
- {"local_id": "e2", "type": "Obligacion", "label": "Cumplimiento de requerimientos de ética", "properties": {"tipo": "otra", "descripcion": "Cumplimiento de los requerimientos de ética conforme a la RT 37"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- {"local_id": "e3", "type": "Obligacion", "label": "Planificación y ejecución de tarea profesional", "properties": {"tipo": "otra", "descripcion": "Planificación y ejecución de la tarea de forma tal que permita emitir el informe especial"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- {"local_id": "e4", "type": "Operacion", "label": "Verificación de tasas de interés en financiaciones", "properties": {"tipo": "verificación de tasas de interés", "descripcion": "Verificación de las bases de liquidación, modalidades de aplicación, divisor fijo e intereses punitorio en financiaciones, mediante revisión de fórmulas de cálculo de intereses en muestra representativa"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "in
- {"local_id": "e5", "type": "Operacion", "label": "Verificación de interés compensatorio y punitorio en tarjetas de crédito", "properties": {"tipo": "verificación de tasas de interés", "descripcion": "Verificación del Interés Compensatorio y Punitorio en financiaciones vinculadas a tarjetas de crédito, conforme a normas de Tasas de interés en operaciones de crédito"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 5
- {"local_id": "e6", "type": "Operacion", "label": "Verificación de refinanciaciones de saldos de tarjetas de crédito", "properties": {"tipo": "verificación de refinanciaciones", "descripcion": "Verificación del cumplimiento de normas de tasas de interés en refinanciaciones de saldos adeudados de tarjetas de crédito"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- {"local_id": "e7", "type": "Operacion", "label": "Verificación de comisiones y cargos cobrados a usuarios", "properties": {"tipo": "verificación de comisiones y cargos", "descripcion": "Verificación de que las comisiones y cargos cobrados a usuarios se ajusten a lo establecido en normas de Tasas de interés y Protección de usuarios"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 7}
- {"local_id": "e8", "type": "Operacion", "label": "Evaluación de políticas de publicidad de créditos", "properties": {"tipo": "evaluación de políticas", "descripcion": "Evaluación de la existencia de políticas y procedimientos para garantizar cumplimiento de normas de publicidad de créditos"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 8}
- {"local_id": "e9", "type": "Operacion", "label": "Verificación de cumplimiento de recaudos mínimos en contratos", "properties": {"tipo": "verificación de contratos", "descripcion": "Verificación del cumplimiento de recaudos mínimos en contratos y constatación de entrega de copias a usuarios conforme a normas de Protección de usuarios"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 9}
- {"local_id": "e10", "type": "Operacion", "label": "Verificación de cláusulas sobre modificación de tasa de interés", "properties": {"tipo": "verificación de contratos", "descripcion": "Constatación de que contratos a tasa fija no prevean modificación de tasa y que contratos a tasa variable determinen parámetros conforme a normas"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 10}
- {"local_id": "e11", "type": "Operacion", "label": "Verificación de ausencia de cláusulas abusivas", "properties": {"tipo": "verificación de contratos", "descripcion": "Verificación de la inexistencia de cláusulas abusivas que restrinjan derechos de usuarios o desnaturalicen obligaciones de sujetos obligados"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 11}
- {"local_id": "e12", "type": "Operacion", "label": "Verificación de exposición de tasa de interés y CFT", "properties": {"tipo": "verificación de información", "descripcion": "Verificación de la exposición correcta de tasa de interés y Costo Financiero Total en contratos y documentos"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 12}
- {"local_id": "e13", "type": "Operacion", "label": "Verificación de cambios en condiciones pactadas", "properties": {"tipo": "verificación de contratos", "descripcion": "Constatación de que en contratos las condiciones modificables estén taxativamente especificadas"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 13}
- {"local_id": "e14", "type": "Operacion", "label": "Verificación de notificación de cambios de condiciones", "properties": {"tipo": "verificación de comunicación", "descripcion": "Verificación del cumplimiento de normas de notificación al usuario en caso de cambios en condiciones pactadas"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 14}
- {"local_id": "e15", "type": "Operacion", "label": "Verificación de información de comisiones y cargos al BCRA", "properties": {"tipo": "verificación de reporte", "descripcion": "Verificación de la información al BCRA de comisiones y cargos percibidos y de altas y aumentos, así como notificación a usuarios"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 15}
- {"local_id": "e16", "type": "Operacion", "label": "Verificación de seguros accesorios", "properties": {"tipo": "verificación de seguros", "descripcion": "Verificación de que no se cobre seguro de vida sobre saldo deudor, que se ofrezcan al menos tres aseguradoras para otros seguros accesorios, y que no haya retribución en seguros no accesorios"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 16}
- {"local_id": "e17", "type": "Operacion", "label": "Verificación de reintegro de importes en exceso", "properties": {"tipo": "verificación de reintegros", "descripcion": "Verificación de cumplimiento de normas de reintegro de importes en caso de intereses, comisiones o cargos cobrados en exceso"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 17}
- {"local_id": "e18", "type": "Operacion", "label": "Verificación de designación de responsable de atención al usuario", "properties": {"tipo": "verificación de designación", "descripcion": "Verificación de que el Directorio haya designado responsable de atención al usuario en carácter de titular y suplente"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 18}
- {"local_id": "e19", "type": "Operacion", "label": "Verificación de registros de consultas, reclamos y reintegros", "properties": {"tipo": "verificación de registros", "descripcion": "Verificación de habilitación y actualización de RCCR, RRI y RDJA conforme a normas de Protección de usuarios"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 19}
- {"local_id": "e20", "type": "Operacion", "label": "Verificación de reporte trimestral de consultas y reclamos", "properties": {"tipo": "reporte_al_supervisor", "descripcion": "Elaboración y elevación de reporte trimestral al Directorio o responsable de protección de usuarios sobre consultas, reclamos, intervenciones judiciales y reintegros", "frecuencia": "como mínimo trimestral"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "i
- {"local_id": "e21", "type": "Operacion", "label": "Verificación de aprobación de manual de procedimiento", "properties": {"tipo": "verificación de aprobación", "descripcion": "Verificación de que el Directorio haya aprobado manual de procedimiento para atención de consultas y reclamos de usuarios"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 21}
- {"local_id": "e22", "type": "Operacion", "label": "Verificación de alternativas de presentación de consultas y reclamos", "properties": {"tipo": "verificación de procedimientos", "descripcion": "Verificación de que normas y procedimientos prevean distintas alternativas de presentación de consultas y reclamos"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 22}
- {"local_id": "e23", "type": "Operacion", "label": "Verificación de evaluación integral de auditoría interna", "properties": {"tipo": "verificación de auditoría", "descripcion": "Verificación de que Auditoría Interna complete evaluación integral anual de procesos de cumplimiento de normas de Protección de usuarios", "frecuencia": "al menos anualmente"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 23}
- {"local_id": "e24", "type": "Operacion", "label": "Verificación de publicación de información en sitio web", "properties": {"tipo": "verificación de información", "descripcion": "Verificación de publicación en sitio web institucional de información conforme a normas de Comunicación por medios electrónicos"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 24}
- {"local_id": "e25", "type": "Operacion", "label": "Verificación de difusión en recintos de atención al público", "properties": {"tipo": "verificación de información", "descripcion": "Verificación de difusión en recintos de atención al público de información conforme a normas de Comunicación por medios electrónicos"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 25}
- {"local_id": "e26", "type": "Operacion", "label": "Verificación de presentación de regímenes informativos", "properties": {"tipo": "verificación de reporte", "descripcion": "Constatación de presentación de regímenes informativos de Financiamiento con tarjetas de crédito, Deudores del sistema financiero, Transparencia y Reclamos conforme a plazos y diseños del BCRA"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 2
- {"local_id": "e27", "type": "Operacion", "label": "Verificación de integridad de información en regímenes informativos", "properties": {"tipo": "verificación de información", "descripcion": "Verificación de que información en regímenes informativos surja de soportes, inventarios analíticos o documentación de respaldo"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 27}
- {"local_id": "e28", "type": "Operacion", "label": "Verificación de integridad de regímenes informativos mensuales", "properties": {"tipo": "verificación de información", "descripcion": "Verificación de integridad de regímenes informativos mensuales mediante cotejo de totales con registros contables"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 28}
- {"local_id": "e29", "type": "Operacion", "label": "Verificación de procedimientos de control en régimen de reclamos", "properties": {"tipo": "verificación de procedimientos", "descripcion": "Constatación de procedimientos y controles para asegurar que información en régimen de reclamos surja del RCCR e incorporación de URL de información al usuario"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 29}
- {"local_id": "e30", "type": "Operacion", "label": "Verificación de actualización de registro de PNFC", "properties": {"tipo": "verificación de registro", "descripcion": "Verificación de cumplimiento de actualización de información del registro de Proveedores no financieros de crédito"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 30}
- {"local_id": "e31", "type": "Operacion", "label": "Verificación de identificación digital de clientes", "properties": {"tipo": "verificación de procesos", "descripcion": "Verificación de cumplimiento de requisitos de identificación digital de clientes en operatoria de Cobro con Transferencia"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 31}
- {"local_id": "e32", "type": "Operacion", "label": "Corroboración de mecanismos de validación de presencia real", "properties": {"tipo": "verificación de procesos", "descripcion": "Corroboración de aplicación de mecanismos de validación de presencia real del cliente mediante pruebas de vida"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 32}
- {"local_id": "e33", "type": "Operacion", "label": "Verificación de controles de validación de puntos de contacto", "properties": {"tipo": "verificación de controles", "descripcion": "Verificación de implementación de controles para validar puntos de contacto declarados y dispositivo móvil asociado"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 33}
- {"local_id": "e34", "type": "Operacion", "label": "Verificación de mecanismos de validación biométrica", "properties": {"tipo": "verificación de procesos", "descripcion": "Verificación de implementación de mecanismos de validación biométrica y verificación de documentación contra fuentes externas"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 34}
- {"local_id": "e35", "type": "Operacion", "label": "Evaluación de técnicas complementarias de verificación de identidad", "properties": {"tipo": "evaluación de procesos", "descripcion": "Evaluación de existencia y aplicación de técnicas complementarias de verificación de identidad según análisis de riesgo"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 35}
- {"local_id": "e36", "type": "Operacion", "label": "Verificación de no comunicación de motivos de fallas en identificación", "properties": {"tipo": "verificación de procedimientos", "descripcion": "Verificación de que no se comuniquen al cliente motivos específicos de fallas en proceso de identificación"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 36}
- {"local_id": "e37", "type": "Operacion", "label": "Verificación de procesos de eliminación de datos", "properties": {"tipo": "verificación de procesos", "descripcion": "Verificación de existencia de procesos de eliminación de datos mediante borrado seguro"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 37}
- {"local_id": "e38", "type": "Operacion", "label": "Verificación de anonimización de datos estadísticos", "properties": {"tipo": "verificación de procesos", "descripcion": "Verificación de que datos conservados con fines estadísticos sean anonimizados o desasociados"}, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 38}
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e3", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e4", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- relación: {"source": "e5", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- relación: {"source": "e6", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- relación: {"source": "e7", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- relación: {"source": "e8", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 7}
- relación: {"source": "e9", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 8}
- relación: {"source": "e10", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 9}
- relación: {"source": "e11", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 10}
- relación: {"source": "e12", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 11}
- relación: {"source": "e13", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 12}
- relación: {"source": "e14", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 13}
- relación: {"source": "e15", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 14}
- relación: {"source": "e16", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 15}
- relación: {"source": "e17", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 16}
- relación: {"source": "e18", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 17}
- relación: {"source": "e19", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 18}
- relación: {"source": "e20", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 19}
- relación: {"source": "e21", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 20}
- relación: {"source": "e22", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 21}
- relación: {"source": "e23", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 22}
- relación: {"source": "e24", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 23}
- relación: {"source": "e25", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 24}
- relación: {"source": "e26", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 25}
- relación: {"source": "e27", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 26}
- relación: {"source": "e28", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 27}
- relación: {"source": "e29", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 28}
- relación: {"source": "e30", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 29}
- relación: {"source": "e31", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 30}
- relación: {"source": "e32", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 31}
- relación: {"source": "e33", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 32}
- relación: {"source": "e34", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 33}
- relación: {"source": "e35", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 34}
- relación: {"source": "e36", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 35}
- relación: {"source": "e37", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 36}
- relación: {"source": "e38", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 37}
- relación: {"source": "e1", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 38}
- relación: {"source": "e4", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 39}
- relación: {"source": "e5", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 40}
- relación: {"source": "e6", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 41}
- relación: {"source": "e7", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 42}
- relación: {"source": "e8", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 43}
- relación: {"source": "e9", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 44}
- relación: {"source": "e10", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 45}
- relación: {"source": "e11", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 46}
- relación: {"source": "e12", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 47}
- relación: {"source": "e13", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 48}
- relación: {"source": "e14", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 49}
- relación: {"source": "e15", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 50}
- relación: {"source": "e16", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 51}
- relación: {"source": "e17", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 52}
- relación: {"source": "e18", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 53}
- relación: {"source": "e19", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 54}
- relación: {"source": "e20", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 55}
- relación: {"source": "e21", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 56}
- relación: {"source": "e22", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 57}
- relación: {"source": "e23", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 58}
- relación: {"source": "e24", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 59}
- relación: {"source": "e25", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 60}
- relación: {"source": "e26", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 61}
- relación: {"source": "e27", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 62}
- relación: {"source": "e28", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 63}
- relación: {"source": "e29", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 64}
- relación: {"source": "e30", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 65}
- relación: {"source": "e31", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 66}
- relación: {"source": "e32", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 67}
- relación: {"source": "e33", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 68}
- relación: {"source": "e34", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 69}
- relación: {"source": "e35", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 70}
- relación: {"source": "e36", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 71}
- relación: {"source": "e37", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 72}
- relación: {"source": "e38", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_proveedor_no_financiero_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_iepsp", "archivo": "ri_iepsp.pdf", "punto": "A::S4", "rol_documental": "punto_propio"}, "indice_crudo": 73}

## 4. `ri_ii_31_12_19::2.20` — RI:sin_raiz · cola

Texto que vio E3 (e0, bloque de lista True; págs. 6):

```
[encabezado | punto S2]
2. DIRECTIVOS
[texto propio | punto 2.20]
2.20. Domicilio especial (dirección, código postal, localidad, provincia, país)
```

Versión: primer intento (cola). Entidades 1, relaciones 0.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Régimen Informativo II", "properties": {}, "provenance": {"to": "ri_ii_31_12_19", "archivo": "ri_ii_31_12_19.pdf", "punto": "2.20", "rol_documental": "punto_propio"}, "indice_crudo": 0}

## 5. `ri_secoexpo::SC::rep2` — RI:sin_raiz · cola

Texto que vio E3 (e0, bloque de lista True; págs. 1):

```
[texto propio | punto SC]
APARTADO C: Baja de reportes de las entidades en el seguimiento.
Las entidades deberán presentar la información correspondiente a los requerimientos de los
Apartados B y C con una periodicidad diaria, incluyendo sólo los datos relacionados con las
novedades producidas.
```

Versión: primer intento (cola). Entidades 2, relaciones 2.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Régimen Informativo Contable", "properties": {}, "provenance": {"to": "ri_secoexpo", "archivo": "ri_secoexpo.pdf", "punto": "SC", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Obligacion", "label": "Presentación diaria de información de novedades", "properties": {"tipo": "presentacion_informativa", "frecuencia": "diaria"}, "provenance": {"to": "ri_secoexpo", "archivo": "ri_secoexpo.pdf", "punto": "SC", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_secoexpo", "archivo": "ri_secoexpo.pdf", "punto": "SC", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e1", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_rol_entidad_comprendida_reginf", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_secoexpo", "archivo": "ri_secoexpo.pdf", "punto": "SC", "rol_documental": "punto_propio"}, "indice_crudo": 1}

## 6. `ri_tar::4.1.2` — RI:sin_raiz · cola

Texto que vio E3 (e0, bloque de lista True; págs. 6):

```
[encabezado | punto S4]
4. CUADRO 3 TASAS – GENERAL–
[encabezado | punto 4.1]
4.1. Instrucciones Particulares
[texto propio | punto 4.1.2]
4.1.2. Tasa máxima de interés compensatorio por financiación de saldos de tarjetas de crédito
Se consignará la tasa nominal anual máxima de interés compensatorio aplicada a las finan-
ciaciones originadas a partir de los vencimientos de los resúmenes de cuenta que opera-
ron en el mes bajo informe.
```

Versión: primer intento (cola). Entidades 3, relaciones 3.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Régimen Informativo Tarjetas", "properties": {}, "provenance": {"to": "ri_tar", "archivo": "ri_tar.pdf", "punto": "4.1.2", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Operacion", "label": "Financiación de saldos de tarjetas de crédito", "properties": {"tipo": "Financiación", "descripcion": "Financiaciones de saldos de tarjetas de crédito originadas a partir de los vencimientos de los resúmenes de cuenta que operaron en el mes bajo informe"}, "provenance": {"to": "ri_tar", "archivo": "ri_tar.pdf", "punto": "4.1.2", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- {"local_id": "e2", "type": "Obligacion", "label": "Consignación tasa máxima interés compensatorio", "properties": {"tipo": "presentacion_informativa", "descripcion": "Consignar la tasa nominal anual máxima de interés compensatorio aplicada a las financiaciones de saldos de tarjetas de crédito originadas a partir de los vencimientos de los resúmenes de cuenta que operaron en el mes bajo informe"}, "provenance": {"to": "ri_tar", "archivo": "ri_tar.pdf", "punto": "4.1.2", "rol_documental": "punto_p
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_tar", "archivo": "ri_tar.pdf", "punto": "4.1.2", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_rol_entidad_comprendida_reginf", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_tar", "archivo": "ri_tar.pdf", "punto": "4.1.2", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e2", "target": "e1", "predicate": "regula", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_tar", "archivo": "ri_tar.pdf", "punto": "4.1.2", "rol_documental": "punto_propio"}, "indice_crudo": 2}

## 7. `ri_msrl::6.2` — RI:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 13, 14, 15, 16):

```
[encabezado | punto S6]
Sección 6. Modelos de Información
[texto propio | punto 6.2]
6.2. Salidas
[TABLA ri_msrl::tabla001 | página 13, 14, 15 | e0_tablas | posicional]
Fila 1: col1 = SALIDAS ⟨abarca hasta col3⟩
Fila 2: col1 = CÓDIGO | col2 = CONCEPTOS | col3 = Último día del mes
Fila 3: col1 = 200000/M | col2 = Salidas de efectivo
Fila 4: col1 = 210000/M | col2 = Retiros de depósitos minoristas
Fila 5: col1 = 211000/M | col2 = Depósitos minoristas estables
Fila 6: col1 = 212000/M | col2 = Otros depósitos minoristas
Fila 7: col1 = 212100/M | col2 = Depósitos a la vista en pesos
Fila 8: col1 = 212200/M | col2 = Depósitos a plazo en pesos
Fila 9: col1 = 212300/M | col2 = Depósitos a la vista y a plazo en moneda extranjera
Fila 10: col1 = 220000/M | col2 = Pérdida de fondeo mayorista no garantizado
Fila 11: col1 = 221000/M | col2 = Fondeo provisto por MiPyMEs
Fila 12: col1 = 221100/M | col2 = Fondeo estable.
Fila 13: col1 = 221200/M | col2 = Otros fondeos
Fila 14: col1 = 221210/M | col2 = Depósitos a la vista en pesos
Fila 15: col1 = 221220/M | col2 = Depósitos a plazo en pesos
Fila 16: col1 = 221230/M | col2 = Depósitos a la vista y a plazo en moneda extranjera.
Fila 17: col1 = 222000/M | col2 = Depósitos operativos generados por actividades de compensación, custodia y tesorería
Fila 18: col1 = 223000/M | col2 = Otros fondeos mayoristas no garantizados
Fila 19: col1 = 223100/M | col2 = Fondeo mayorista no garantizado provisto por empresas del sector privado no financiero
Fila 20: col1 = 223200/M | col2 = Fondeo mayorista no garantizado proveniente de Gobiernos, bancos centrales y bancos multilaterales de desarrollo
Fila 21: col1 = 223300/M | col2 = Fondeo mayorista no garantizado provisto por otras personas jurídicas, sector público no financiero y SPEs
Fila 22: col1 = CÓDIGO | col2 = CONCEPTOS | col3 = Último día del mes
Fila 23: col1 = 230000/M | col2 = Salida de fondeo garantizado
Fila 24: col1 = 231000/M | col2 = Operaciones con el BCRA o con otras contrapartes
Fila 25: col1 = 231100/M | col2 = Con el BCRA
Fila 26: col1 = 231200/M | col2 = Con otros bancos centrales
Fila 27: col1 = 231300/M | col2 = Con otras contrapartes
Fila 28: col1 = 232000/M | col2 = Operaciones con el Gobierno Nacional o con bancos multilaterales de desarrollo
Fila 29: col1 = 233000/M | col2 = Restantes operaciones
Fila 30: col1 = 250000/M | col2 = Requerimientos adicionales
Fila 31: col1 = 250100/M | col2 = Salidas de efectivo procedentes de operaciones con derivados
Fila 32: col1 = 250200/M | col2 = Cláusulas activadas por deterioro en la calidad crediticia de la entidad
Fila 33: col1 = 250300/M | col2 = Cambios en valor de mercado de activos en garantía
Fila 34: col1 = 250400/M | col2 = Garantías no segregadas mantenidas en exceso por la entidad financiera
Fila 35: col1 = 250500/M | col2 = Garantías vinculadas con operaciones cuya integración podría -de acuerdo con lo previsto en el contrato- ser exigida en cualquier momento por la contraparte
Fila 36: col1 = 250600/M | col2 = Contratos que permiten la sustitución de garantías
Fila 37: col1 = 250700/M | col2 = Cambios en el valor de mercado de operaciones que requieren integración de garantía
Fila 38: col1 = 250800/M | col2 = Pérdida de fondeo en títulos valores y otras facilidades de financiación
Fila 39: col1 = 250900/M | col2 = Porción no utilizada de las facilidades de crédito y de liquidez comprometidas con:
Fila 40: col1 = 250910/M | col2 = Clientes minoristas y MiPyMEs.
Fila 41: col1 = 250920/M | col2 = Empresas del sector privado no financiero
Fila 42: col1 = 250921/M | col2 = Facilidades de liquidez.
Fila 43: col1 = 250922/M | col2 = Facilidades de crédito.
Fila 44: col1 = CÓDIGO | col2 = CONCEPTOS | col3 = Último día del mes
Fila 45: col1 = 250930/M | col2 = Gobierno nacional, otros estados soberanos y sus bancos centrales y bancos multilaterales de desarrollo
Fila 46: col1 = 250931/M | col2 = Facilidades de liquidez
Fila 47: col1 = 250932/M | col2 = Facilidades de crédito
Fila 48: col1 = 250940/M | col2 = Entidades financieras del país.
Fila 49: col1 = 250950/M | col2 = Entidades cambiarias, aseguradoras, agentes regulados por la CNV y fiduciarios de fideicomisos no financieros
Fila 50: col1 = 250951/M | col2 = Facilidades de liquidez
Fila 51: col1 = 250952/M | col2 = Facilidades de crédito
Fila 52: col1 = 250960/M | col2 = Otras personas jurídicas, sector público no financiero -excepto el Gobierno Nacional-, y entes no incluidos en los códigos anteriores
Fila 53: col1 = 251000/M | col2 = Obligaciones contractuales de concesión de fondos dentro del período de 30 días
Fila 54: col1 = 251100/M | col2 = A entidades financieras, entidades cambiarias, aseguradoras, agentes regulados por la CNV y fiduciarios de fideicomisos no financieros
Fila 55: col1 = 251200/M | col2 = A clientes minoristas, MIPyMES y a empresas del sector privado no financiero. Excedente sobre el 50 % de entradas
Fila 56: col1 = 252000/M | col2 = Otras obligaciones contingentes de financiación
Fila 57: col1 = 252100/M | col2 = Procedentes de instrumentos de financiación de operaciones de comercio exterior
Fila 58: col1 = 252200/M | col2 = Otras obligaciones contingentes de provisión de fondos
Fila 59: col1 = 252210/M | col2 = Facilidades de crédito y liquidez “no comprometidas”
Fila 60: col1 = 252220/M | col2 = Garantías y cartas de crédito no relacionadas con operaciones de financiación al comercio exterior
[FIN TABLA ri_msrl::tabla001]
[TABLA ri_msrl::tabla002 | página 16 | e0_tablas | posicional]
Fila 1: col1 = SALIDAS ⟨abarca hasta col3⟩
Fila 2: col1 = CÓDIGO | col2 = CONCEPTOS | col3 = Ultimo día del mes
Fila 3: col1 = 252230/M | col2 = Otras obligaciones no contractuales
Fila 4: col1 = 252231/M | col2 = Por solicitudes de recompra de deuda de la misma entidad o por vehículos de inversión vinculados u otra facilidad financiera de ese tipo
Fila 5: col1 = 252232/M | col2 = Por productos estructurados para mantener su negociabilidad
Fila 6: col1 = 252233/M | col2 = Fondos administrados que se comercializan con el objeto de mantener estable su valor
Fila 7: col1 = 252240/M | col2 = Depósitos judiciales
Fila 8: col1 = 252300/M | col2 = Obligaciones no contractuales en las que las posiciones vendidas de clientes se cubren con activos de garantía de otros
Fila 9: col1 = 252400/M | col2 = clientes Obligaciones no contractuales relacionadas con UTEs o inversiones minoritarias que no se consolidan
Fila 10: col1 = 253000/M | col2 = Otras salidas de efectivo contractuales
Fila 11: col1 = 253100/M | col2 = Títulos de deuda en circulación
Fila 12: col1 = 253200/M | col2 = Por posiciones vendidas descubiertas
Fila 13: col1 = 253300/M | col2 = Otras salidas contractuales de efectivo no contempladas en los subcódigos previos
[FIN TABLA ri_msrl::tabla002]
```

Versión: primer intento (cola). Entidades 22, relaciones 21.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Régimen Informativo Mensual", "properties": {}, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Definicion", "label": "Salidas de efectivo", "properties": {"termino": "Salidas de efectivo", "descripcion": "Concepto de salida de efectivo identificado con código 200000/M, que comprende retiros de depósitos minoristas, pérdida de fondeo mayorista no garantizado, depósitos operativos generados por actividades de compensación, custodia y tesorería, y otros fondeos mayoristas no garantizados."}, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2",
- {"local_id": "e2", "type": "Definicion", "label": "Retiros de depósitos minoristas", "properties": {"termino": "Retiros de depósitos minoristas", "descripcion": "Concepto de salida identificado con código 210000/M, que comprende depósitos minoristas estables y otros depósitos minoristas (a la vista en pesos, a plazo en pesos, y a la vista y a plazo en moneda extranjera)."}, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo"
- {"local_id": "e3", "type": "Definicion", "label": "Pérdida de fondeo mayorista no garantizado", "properties": {"termino": "Pérdida de fondeo mayorista no garantizado", "descripcion": "Concepto de salida identificado con código 220000/M, que comprende fondeo provisto por MiPyMEs (estable y otros), depósitos operativos generados por actividades de compensación, custodia y tesorería, y otros fondeos mayoristas no garantizados."}, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6
- {"local_id": "e4", "type": "Definicion", "label": "Salida de fondeo garantizado", "properties": {"termino": "Salida de fondeo garantizado", "descripcion": "Concepto de salida identificado con código 230000/M, que comprende operaciones con el BCRA o con otras contrapartes, operaciones con el Gobierno Nacional o con bancos multilaterales de desarrollo, y restantes operaciones."}, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_cr
- {"local_id": "e5", "type": "Definicion", "label": "Requerimientos adicionales", "properties": {"termino": "Requerimientos adicionales", "descripcion": "Concepto de salida identificado con código 250000/M, que comprende salidas de efectivo procedentes de operaciones con derivados, cláusulas activadas por deterioro en la calidad crediticia, cambios en valor de mercado de activos en garantía, garantías no segregadas, garantías vinculadas con operaciones, contratos que permiten sustitución de garant
- {"local_id": "e6", "type": "Definicion", "label": "Salidas de efectivo procedentes de operaciones con derivados", "properties": {"termino": "Salidas de efectivo procedentes de operaciones con derivados", "descripcion": "Concepto de requerimiento adicional identificado con código 250100/M."}, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- {"local_id": "e7", "type": "Definicion", "label": "Cláusulas activadas por deterioro en la calidad crediticia", "properties": {"termino": "Cláusulas activadas por deterioro en la calidad crediticia de la entidad", "descripcion": "Concepto de requerimiento adicional identificado con código 250200/M."}, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 7}
- {"local_id": "e8", "type": "Definicion", "label": "Cambios en valor de mercado de activos en garantía", "properties": {"termino": "Cambios en valor de mercado de activos en garantía", "descripcion": "Concepto de requerimiento adicional identificado con código 250300/M."}, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 8}
- {"local_id": "e9", "type": "Definicion", "label": "Garantías no segregadas mantenidas en exceso", "properties": {"termino": "Garantías no segregadas mantenidas en exceso por la entidad financiera", "descripcion": "Concepto de requerimiento adicional identificado con código 250400/M."}, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 9}
- {"local_id": "e10", "type": "Definicion", "label": "Garantías vinculadas con operaciones exigibles en cualquier momento", "properties": {"termino": "Garantías vinculadas con operaciones cuya integración podría ser exigida en cualquier momento por la contraparte", "descripcion": "Concepto de requerimiento adicional identificado con código 250500/M."}, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 10}
- {"local_id": "e11", "type": "Definicion", "label": "Contratos que permiten la sustitución de garantías", "properties": {"termino": "Contratos que permiten la sustitución de garantías", "descripcion": "Concepto de requerimiento adicional identificado con código 250600/M."}, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 11}
- {"local_id": "e12", "type": "Definicion", "label": "Cambios en valor de mercado de operaciones con integración de garantía", "properties": {"termino": "Cambios en el valor de mercado de operaciones que requieren integración de garantía", "descripcion": "Concepto de requerimiento adicional identificado con código 250700/M."}, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 12}
- {"local_id": "e13", "type": "Definicion", "label": "Pérdida de fondeo en títulos valores y facilidades de financiación", "properties": {"termino": "Pérdida de fondeo en títulos valores y otras facilidades de financiación", "descripcion": "Concepto de requerimiento adicional identificado con código 250800/M."}, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 13}
- {"local_id": "e14", "type": "Definicion", "label": "Porción no utilizada de facilidades de crédito y liquidez comprometidas", "properties": {"termino": "Porción no utilizada de las facilidades de crédito y de liquidez comprometidas", "descripcion": "Concepto de requerimiento adicional identificado con código 250900/M, que comprende facilidades comprometidas con clientes minoristas y MiPyMEs, empresas del sector privado no financiero, Gobierno nacional y otros estados soberanos, entidades financi
- {"local_id": "e15", "type": "Definicion", "label": "Obligaciones contractuales de concesión de fondos dentro de 30 días", "properties": {"termino": "Obligaciones contractuales de concesión de fondos dentro del período de 30 días", "descripcion": "Concepto de requerimiento adicional identificado con código 251000/M."}, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 15}
- {"local_id": "e16", "type": "Definicion", "label": "Otras obligaciones contingentes de financiación", "properties": {"termino": "Otras obligaciones contingentes de financiación", "descripcion": "Concepto de requerimiento adicional identificado con código 252000/M, que comprende instrumentos de financiación de operaciones de comercio exterior y otras obligaciones contingentes de provisión de fondos."}, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "pu
- {"local_id": "e17", "type": "Definicion", "label": "Otras obligaciones no contractuales", "properties": {"termino": "Otras obligaciones no contractuales", "descripcion": "Concepto de requerimiento adicional identificado con código 252230/M, que comprende solicitudes de recompra de deuda, productos estructurados para mantener negociabilidad, y fondos administrados para mantener estable su valor."}, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_
- {"local_id": "e18", "type": "Definicion", "label": "Depósitos judiciales", "properties": {"termino": "Depósitos judiciales", "descripcion": "Concepto de requerimiento adicional identificado con código 252240/M."}, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 18}
- {"local_id": "e19", "type": "Definicion", "label": "Obligaciones no contractuales con posiciones vendidas cubiertas", "properties": {"termino": "Obligaciones no contractuales en las que las posiciones vendidas de clientes se cubren con activos de garantía de otros", "descripcion": "Concepto de requerimiento adicional identificado con código 252300/M."}, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 19}
- {"local_id": "e20", "type": "Definicion", "label": "Obligaciones no contractuales relacionadas con UTEs o inversiones minoritarias", "properties": {"termino": "Obligaciones no contractuales relacionadas con UTEs o inversiones minoritarias que no se consolidan", "descripcion": "Concepto de requerimiento adicional identificado con código 252400/M."}, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 20}
- {"local_id": "e21", "type": "Definicion", "label": "Otras salidas de efectivo contractuales", "properties": {"termino": "Otras salidas de efectivo contractuales", "descripcion": "Concepto de requerimiento adicional identificado con código 253000/M, que comprende títulos de deuda en circulación, posiciones vendidas descubiertas, y otras salidas contractuales de efectivo no contempladas en subcódigos previos."}, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documen
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e3", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e4", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- relación: {"source": "e5", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- relación: {"source": "e6", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- relación: {"source": "e7", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- relación: {"source": "e8", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 7}
- relación: {"source": "e9", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 8}
- relación: {"source": "e10", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 9}
- relación: {"source": "e11", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 10}
- relación: {"source": "e12", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 11}
- relación: {"source": "e13", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 12}
- relación: {"source": "e14", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 13}
- relación: {"source": "e15", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 14}
- relación: {"source": "e16", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 15}
- relación: {"source": "e17", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 16}
- relación: {"source": "e18", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 17}
- relación: {"source": "e19", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 18}
- relación: {"source": "e20", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 19}
- relación: {"source": "e21", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 20}

## 8. `ri_msrl::S1` — RI:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 2):

```
[texto propio | punto S1]
Sección 1. Instrucciones Generales
Se informarán los componentes del Ratio de cobertura de Liquidez - LCR - de acuerdo con los
códigos del modelo de información (Sección 5) según las instrucciones respectivas,
correspondientes al último día del mes.
El presente requerimiento deberá ser cumplido por las entidades financieras consideradas
“internacionalmente activas” a los fines del cumplimiento del Ratio de Cobertura de Liquidez.
La información tendrá frecuencia mensual y los importes se registrarán en miles de pesos, sin
decimales. Los datos se informarán convertidos a pesos, pero identificando la moneda de origen.
A los fines del redondeo de las magnitudes se incrementarán los valores en una unidad cuando el
primer dígito de las fracciones sea igual o mayor que 5, desechando estas últimas si resultan
inferiores.
Los importes en moneda extranjera se convertirán a pesos utilizando el tipo de cambio de
referencia publicado por el B.C.R.A. para el dólar estadounidense, previa aplicación del tipo de
pase correspondiente para las otras monedas comunicado por la Mesa de Operaciones.
No obstante ello, los conceptos en moneda extranjera se identificarán según su moneda de origen,
de acuerdo con la codificación prevista en el Sistema Centralizado de requerimientos informativos
(SISCEN), tabla T0003, de la que se excluirán aquellas que no estén referenciadas con el código
SWIFT.
Los datos solicitados se informarán sobre base individual y consolidada conforme las
disposiciones de la Sección 8. de las normas sobre “Ratio de cobertura de liquidez”. A esos
efectos, se definen los siguientes niveles de consolidación:
1: Casa central y sucursales en el país;
2: Casa central, sucursales y subsidiarias significativas en el país y en el exterior.
En relación con el concepto de “subsidiaria significativa” deberán tenerse en cuenta las
disposiciones del segundo párrafo del punto 8.2. de las normas sobre “Ratio de cobertura de
liquidez”.
```

Versión: primer intento (cola). Entidades 11, relaciones 11.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Ratio de Cobertura de Liquidez - LCR", "properties": {}, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Obligacion", "label": "Informar componentes LCR mensualmente", "properties": {"tipo": "presentacion_informativa", "frecuencia": "mensual"}, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- {"local_id": "e2", "type": "Obligacion", "label": "Cumplimiento LCR por entidades internacionalmente activas", "properties": {"tipo": "otra", "descripcion": "Cumplimiento del requerimiento de LCR por entidades financieras consideradas internacionalmente activas"}, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- {"local_id": "e3", "type": "Obligacion", "label": "Registrar importes en miles de pesos sin decimales", "properties": {"tipo": "presentacion_informativa", "frecuencia": "mensual"}, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- {"local_id": "e4", "type": "Obligacion", "label": "Informar datos convertidos a pesos identificando moneda origen", "properties": {"tipo": "presentacion_informativa"}, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- {"local_id": "e5", "type": "Obligacion", "label": "Redondeo de magnitudes según regla de dígito", "properties": {"tipo": "calculo"}, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- {"local_id": "e6", "type": "Obligacion", "label": "Conversión a pesos con tipo de cambio BCRA", "properties": {"tipo": "calculo"}, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- {"local_id": "e7", "type": "Obligacion", "label": "Identificar conceptos en moneda extranjera según SISCEN", "properties": {"tipo": "presentacion_informativa"}, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 7}
- {"local_id": "e8", "type": "Obligacion", "label": "Informar datos sobre base individual y consolidada", "properties": {"tipo": "presentacion_informativa"}, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 8}
- {"local_id": "e9", "type": "Definicion", "label": "Niveles de consolidación", "properties": {"termino": "niveles de consolidación", "descripcion": "Nivel 1: Casa central y sucursales en el país; Nivel 2: Casa central, sucursales y subsidiarias significativas en el país y en el exterior"}, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 9}
- {"local_id": "e10", "type": "Condicion", "label": "Concepto de subsidiaria significativa según normas LCR", "properties": {"descripcion": "Para la aplicación del concepto de subsidiaria significativa, deben tenerse en cuenta las disposiciones del segundo párrafo del punto 8.2 de las normas sobre Ratio de cobertura de liquidez"}, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 10}
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e3", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e4", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- relación: {"source": "e5", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- relación: {"source": "e6", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- relación: {"source": "e7", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- relación: {"source": "e8", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 7}
- relación: {"source": "e9", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 8}
- relación: {"source": "e10", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 9}
- relación: {"source": "e2", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_msrl", "archivo": "ri_msrl.pdf", "punto": "S1", "rol_documental": "punto_propio"}, "indice_crudo": 10}

## 9. `cedin::12.1` — NG:sin_raiz · cola

Texto que vio E3 (e0, bloque de lista True; págs. 14, 15):

```
[encabezado | punto S12]
12. Extravío, sustracción o destrucción del CEDIN.
[texto propio | punto 12.1]
12.1. Obligaciones a cargo del tenedor desposeído.
Comunicará de inmediato en cualquier casa de una entidad financiera, mediante nota
recibida formalmente, lo sucedido. La notificación deberá incluir los siguientes datos:
- Motivo de la denuncia: extravío, sustracción o destrucción -total o parcial-.
- Serie, número e importe del CEDIN.
- Nombres y apellidos completos de los denunciantes, tipo y número de los documen-
tos que presentan para establecer su identificación conforme a lo previsto en las
normas sobre “Documentos de identificación en vigencia”.
- Copia certificada por la entidad del documento de identificación y, en su caso, de
los instrumentos que acrediten su personería.
- Domicilio especial constituido, en el cual se reputarán como válidas todas las co-
municaciones cursadas con relación a ese pedido.
- Descripción de las circunstancias de adquisición del CEDIN, incluyendo identifica-
ción, en su caso, de los tenedores anteriores que sean de su conocimiento.
- Descripción de las circunstancias del extravío, sustracción o destrucción, adjuntan-
do en caso de destrucción parcial la parte no destruida.
Deberá presentar ante la entidad financiera, a más tardar el día hábil siguiente, acredi-
tación fehaciente de la denuncia efectuada ante la autoridad policial, judicial u otra que
resulte competente en la jurisdicción de que se trate.
En caso de extravío, sustracción o destrucción de un certificado o fórmula sin emitir, en
poder de una entidad financiera, ésta deberá efectuar la notificación y denuncia perti-
nentes precedentemente indicadas.
```

Versión: primer intento (cola). Entidades 6, relaciones 10.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Texto Ordenado CEDIN", "properties": {}, "provenance": {"to": "cedin", "archivo": "cedin.pdf", "punto": "12.1", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Obligacion", "label": "Comunicación inmediata de extravío, sustracción o destrucción", "properties": {"descripcion": "El tenedor desposeído deberá comunicar de inmediato en cualquier casa de una entidad financiera, mediante nota recibida formalmente, el extravío, sustracción o destrucción del CEDIN.", "tipo": "comunicacion_a_cliente"}, "provenance": {"to": "cedin", "archivo": "cedin.pdf", "punto": "12.1", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- {"local_id": "e2", "type": "Obligacion", "label": "Inclusión de datos en la notificación", "properties": {"descripcion": "La notificación debe incluir: motivo de la denuncia (extravío, sustracción o destrucción total o parcial), serie, número e importe del CEDIN, nombres y apellidos completos de los denunciantes con tipo y número de documentos de identificación, copia certificada del documento de identificación y acreditación de personería, domicilio especial constituido para comunicaciones, des
- {"local_id": "e3", "type": "Obligacion", "label": "Presentación de acreditación de denuncia ante autoridad", "properties": {"descripcion": "El tenedor desposeído debe presentar ante la entidad financiera, a más tardar el día hábil siguiente, acreditación fehaciente de la denuncia efectuada ante la autoridad policial, judicial u otra competente en la jurisdicción correspondiente.", "tipo": "presentacion_informativa", "umbrales": "a más tardar el día hábil siguiente"}, "provenance": {"to": "cedin"
- {"local_id": "e4", "type": "Obligacion", "label": "Notificación y denuncia por entidad financiera de certificado o fórmula sin emitir", "properties": {"descripcion": "Cuando un certificado o fórmula sin emitir en poder de una entidad financiera sea objeto de extravío, sustracción o destrucción, la entidad financiera debe efectuar la notificación y denuncia conforme a lo indicado en las obligaciones anteriores.", "tipo": "comunicacion_a_cliente"}, "provenance": {"to": "cedin", "archivo": "cedin.p
- {"local_id": "e5", "type": "Condicion", "label": "Supuesto de certificado o fórmula sin emitir en poder de entidad", "properties": {"descripcion": "Cuando el certificado o fórmula sin emitir se encuentra en poder de una entidad financiera y es objeto de extravío, sustracción o destrucción."}, "provenance": {"to": "cedin", "archivo": "cedin.pdf", "punto": "12.1", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "cedin", "archivo": "cedin.pdf", "punto": "12.1", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "cedin", "archivo": "cedin.pdf", "punto": "12.1", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e3", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "cedin", "archivo": "cedin.pdf", "punto": "12.1", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e4", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "cedin", "archivo": "cedin.pdf", "punto": "12.1", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- relación: {"source": "e5", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "cedin", "archivo": "cedin.pdf", "punto": "12.1", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- relación: {"source": "e5", "target": "e4", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "cedin", "archivo": "cedin.pdf", "punto": "12.1", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- relación: {"source": "e1", "target": null, "predicate": "aplica_a", "sujeto_id": null, "sujeto_propuesto": "el tenedor desposeído", "sujeto_propuesto_padre_sugerido": "Sujeto_cliente", "provenance": {"to": "cedin", "archivo": "cedin.pdf", "punto": "12.1", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- relación: {"source": "e2", "target": null, "predicate": "aplica_a", "sujeto_id": null, "sujeto_propuesto": "el tenedor desposeído", "sujeto_propuesto_padre_sugerido": "Sujeto_cliente", "provenance": {"to": "cedin", "archivo": "cedin.pdf", "punto": "12.1", "rol_documental": "punto_propio"}, "indice_crudo": 7}
- relación: {"source": "e3", "target": null, "predicate": "aplica_a", "sujeto_id": null, "sujeto_propuesto": "el tenedor desposeído", "sujeto_propuesto_padre_sugerido": "Sujeto_cliente", "provenance": {"to": "cedin", "archivo": "cedin.pdf", "punto": "12.1", "rol_documental": "punto_propio"}, "indice_crudo": 8}
- relación: {"source": "e4", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "cedin", "archivo": "cedin.pdf", "punto": "12.1", "rol_documental": "punto_propio"}, "indice_crudo": 9}

## 10. `consyr::3.4.1` — NG:sin_raiz · cola

Texto que vio E3 (e0, bloque de lista True; págs. 8):

```
[encabezado | punto S3]
3. Régimen de reproducción.
[encabezado | punto 3.4]
3.4. Certificación de las reproducciones.
[texto propio | punto 3.4.1]
3.4.1. Designación de funcionarios certificantes.
Las reproducciones deberán ser autenticadas por 2 funcionarios designados por el di-
rectorio o autoridad equivalente de la entidad financiera.
```

Versión: primer intento (cola). Entidades 3, relaciones 3.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Texto Ordenado de Comunicaciones", "properties": {}, "provenance": {"to": "consyr", "archivo": "consyr.pdf", "punto": "3.4.1", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Operacion", "label": "Autenticación de reproducciones", "properties": {"tipo": "autenticación de reproducciones", "descripcion": "Autenticación de reproducciones por funcionarios designados por el directorio o autoridad equivalente de la entidad financiera"}, "provenance": {"to": "consyr", "archivo": "consyr.pdf", "punto": "3.4.1", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- {"local_id": "e2", "type": "Obligacion", "label": "Autenticación por 2 funcionarios certificantes", "properties": {"tipo": "otra", "descripcion": "Las reproducciones deberán ser autenticadas por 2 funcionarios designados por el directorio o autoridad equivalente de la entidad financiera"}, "provenance": {"to": "consyr", "archivo": "consyr.pdf", "punto": "3.4.1", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "consyr", "archivo": "consyr.pdf", "punto": "3.4.1", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "consyr", "archivo": "consyr.pdf", "punto": "3.4.1", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e2", "target": "e1", "predicate": "regula", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "consyr", "archivo": "consyr.pdf", "punto": "3.4.1", "rol_documental": "punto_propio"}, "indice_crudo": 2}

## 11. `consyr::3.4.4` — NG:sin_raiz · cola

Texto que vio E3 (e0, bloque de lista True; págs. 8):

```
[encabezado | punto S3]
3. Régimen de reproducción.
[encabezado | punto 3.4]
3.4. Certificación de las reproducciones.
[texto propio | punto 3.4.4]
3.4.4. Certificación de copias.
Las copias en papel efectuadas a partir de los soportes de información, deberán certi-
ficarse por los funcionarios designados según lo previsto en el punto 3.4.1. dejándose
constancia del elemento en el cual se origina, a tenor de lo dispuesto en el punto
3.4.2.
```

Versión: primer intento (cola). Entidades 4, relaciones 5.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Texto Ordenado de Comunicaciones", "properties": {}, "provenance": {"to": "consyr", "archivo": "consyr.pdf", "punto": "3.4.4", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Operacion", "label": "Certificación de copias en papel", "properties": {"tipo": "Certificación de reproducciones", "descripcion": "Certificación de copias en papel efectuadas a partir de soportes de información, realizada por funcionarios designados según lo previsto en el punto 3.4.1, dejándose constancia del elemento en el cual se origina, a tenor de lo dispuesto en el punto 3.4.2."}, "provenance": {"to": "consyr", "archivo": "consyr.pdf", "punto": "3.4.4", "rol_doc
- {"local_id": "e2", "type": "Obligacion", "label": "Certificar copias en papel por funcionarios designados", "properties": {"tipo": "otra", "descripcion": "Los funcionarios designados según lo previsto en el punto 3.4.1 deberán certificar las copias en papel efectuadas a partir de los soportes de información, dejándose constancia del elemento en el cual se origina, a tenor de lo dispuesto en el punto 3.4.2."}, "provenance": {"to": "consyr", "archivo": "consyr.pdf", "punto": "3.4.4", "rol_document
- {"local_id": "e3", "type": "Condicion", "label": "Constancia del elemento de origen", "properties": {"descripcion": "La certificación debe dejar constancia del elemento en el cual se origina la copia, conforme a lo dispuesto en el punto 3.4.2."}, "provenance": {"to": "consyr", "archivo": "consyr.pdf", "punto": "3.4.4", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "consyr", "archivo": "consyr.pdf", "punto": "3.4.4", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "consyr", "archivo": "consyr.pdf", "punto": "3.4.4", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e3", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "consyr", "archivo": "consyr.pdf", "punto": "3.4.4", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e2", "target": "e1", "predicate": "regula", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "consyr", "archivo": "consyr.pdf", "punto": "3.4.4", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- relación: {"source": "e3", "target": "e2", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "consyr", "archivo": "consyr.pdf", "punto": "3.4.4", "rol_documental": "punto_propio"}, "indice_crudo": 4}

## 12. `seggar::3.3.2` — NG:sin_raiz · cola

Texto que vio E3 (e0, bloque de lista True; págs. 4):

```
[encabezado | punto S3]
3. Aporte adicional.
[encabezado | punto 3.3]
3.3. La calidad de la cartera activa medida por:
[texto propio | punto 3.3.2]
3.3.2. Activos computables para determinar el capital mínimo exigido, ponderados según lo
establecido en las normas sobre “Capitales mínimos de las entidades financieras”,
respecto de los activos totales.
```

Versión: primer intento (cola). Entidades 4, relaciones 4.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Capitales Mínimos", "properties": {}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "3.3.2", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Operacion", "label": "Ponderación de activos computables", "properties": {"tipo": "Cálculo de capital mínimo", "descripcion": "Determinación del capital mínimo exigido mediante la ponderación de activos computables conforme a las normas sobre Capitales mínimos de las entidades financieras, medida como proporción respecto de los activos totales."}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "3.3.2", "rol_documental": "punto_propio"}, "indice_crudo
- {"local_id": "e2", "type": "Obligacion", "label": "Aporte adicional diferenciado — calidad de cartera", "properties": {"tipo": "asignacion", "descripcion": "Las entidades deberán efectuar un aporte adicional diferenciado según el resultado de la ponderación de la calidad de la cartera activa medida por los activos computables para determinar el capital mínimo exigido, ponderados conforme a las normas sobre Capitales mínimos, respecto de los activos totales."}, "provenance": {"to": "seggar", "arc
- {"local_id": "e3", "type": "Restriccion", "label": "Tope aporte adicional — una vez aporte normal", "properties": {"tipo": "limite_cuantitativo", "descripcion": "El aporte adicional resultante de la ponderación de factores no podrá superar una vez el aporte normal.", "umbrales": "no podrá superar una vez el aporte normal"}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "3.3.2", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "3.3.2", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "3.3.2", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e3", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "3.3.2", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e2", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "3.3.2", "rol_documental": "punto_propio"}, "indice_crudo": 3}

## 13. `seggar::8.2` — NG:sin_raiz · cola

Texto que vio E3 (e0, bloque de lista True; págs. 9, 10, 11, 12, 13, 14, 15, 16):

```
[encabezado | punto S8]
8. Legislación aplicable.
[texto propio | punto 8.2]
8.2. Decreto 540/95 (**).
Artículo 1°: Créase el "FONDO DE GARANTIA DE LOS DEPOSITOS" (FGD) con la finali-
dad de cubrir los depósitos bancarios con el alcance previsto en el presente De-
creto.
(***) Dispónese la constitución de la sociedad "SEGURO DE DEPOSITOS SOCIEDAD
ANONIMA" (SEDESA) con el objeto exclusivo de ejercer las funciones de fiducia-
rio que oportunamente le encomiende el ESTADO NACIONAL o el BANCO CEN-
TRAL DE LA REPUBLICA ARGENTINA.
(*) Publicada en el Boletín Oficial del 18.4.95. Con la modificación de la Ley 25.089 (B.O. 14.05.99).
(**) Con las modificaciones de los Decretos 1292/96, 1127/98, 1292/99, 32/01 y 214/02.
(***) Decreto 32/01. Vigencia: 26/12/01.
Artículo 2°: Delégase en el MINISTERIO DE ECONOMIA Y OBRAS Y SERVICIOS PUBLI-
COS la aprobación del Acta Constitutiva y los Estatutos Sociales de "SEGURO DE
DEPOSITOS SOCIEDAD ANONIMA" (SEDESA), que tendrá como socios al
BANCO CENTRAL DE LA REPUBLICA ARGENTINA, con una acción como míni-
mo, y a quien resulte fiduciario del contrato de fideicomiso a constituirse por las
entidades financieras autorizadas para operar en la REPUBLICA ARGENTINA
que expresen su voluntad de participar, en la proporción que para cada una de-
termine el BANCO CENTRAL DE LA REPUBLICA ARGENTINA en función de sus
aportes al FGD. Hasta la constitución de SEDESA, los aportes al FGD ingresarán
a la cuenta y entidad que determine el BANCO CENTRAL DE LA REPUBLICA
ARGENTINA.
Artículo 3°: SEDESA no recibirá compensación alguna por su actuación como fiduciario del
FGD. Los gastos de funcionamiento de la sociedad serán los estrictamente nece-
sarios para operar y deberán ser sufragados con los ingresos del FGD. La modifi-
cación de sus estatutos o de su capital requerirá al menos del voto favorable de
las acciones propiedad del BANCO CENTRAL DE LA REPUBLICA ARGENTINA.
Artículo 4°: Ordénase la protocolización del acta constitutiva y los estatutos sociales de
SEDESA, así como de toda actuación que fuere menester elevar a escritura públi-
ca, a través de la ESCRIBANIA GENERAL DE LA NACION, sin que ello implique
erogación alguna.
Artículo 5°: Instrúyese a la INSPECCION GENERAL DE JUSTICIA a otorgar las conformida-
des o autorizaciones respectivas y a tomar razón de la inscripción de SEDESA en
el registro a su cargo.
Artículo 6°: Las entidades financieras autorizadas para operar en la REPUBLICA ARGENTINA
deberán integrar el FGD con un aporte normal mensual que determinará el BAN-
CO CENTRAL DE LA REPUBLICA ARGENTINA entre un mínimo de CERO CO-
MA CERO QUINCE POR CIENTO (0,015%) y un máximo de CERO COMA CERO
SEIS POR CIENTO (0,06%) del promedio de los saldos diarios de los depósitos en
pesos y en moneda extranjera constituidos en las entidades financieras, y con los
aportes adicionales que el BANCO CENTRAL DE LA REPUBLICA ARGENTINA
establezca para cada entidad en función de los indicadores de riesgo que estime
apropiados. En ningún caso el aporte adicional podrá superar el equivalente a un
aporte normal.
A los fines del cálculo del promedio de saldos diarios de los depósitos en pesos y
en moneda extranjera, quedan excluidos los depósitos correspondientes a las
cuentas oficiales nacionales abiertas en el BANCO DE LA NACION ARGENTINA.
EL BANCO CENTRAL DE LA REPUBLICA ARGENTINA podrá disponer que la in-
tegración del aporte, sea en efectivo o mediante la asunción del compromiso de
efectuar el mismo, instrumentado en las condiciones y formalidades que determine
el BANCO CENTRAL DE LA REPUBLICA ARGENTINA, debiendo las entidades
financieras aportantes, en este último caso, cumplimentar las normas vigentes
sobre capitales mínimos. Dichos compromisos no podrán superar el CINCUEN-
TA POR CIENTO (50%) del aporte que corresponda efectuar.
Artículo 7°: EL BANCO CENTRAL DE LA REPUBLICA ARGENTINA determinará la fecha
de vencimiento de la obligación de depositar los aportes. Las entidades financieras
deberán depositar puntualmente sus aportes como condición para operar regular-
mente. Las entidades financieras que inicien sus operaciones en la REPU-
BLICA ARGENTINA podrán ingresar al fideicomiso referido en el Artículo 2º del
presente Decreto y las que dejen de operar perderán la condición para integrarlo,
cediendo sus derechos al valor nominal de las acciones de SEDESA. La Autoridad
de Aplicación establecerá anualmente la proporción de participación en el fideico-
miso por cada entidad financiera, debiendo realizarse inmediatamente las transfe-
rencias correspondientes al valor nominal de las acciones.
Artículo 8°: Cuando el FGD alcance la suma de DOS MIL MILLONES DE PESOS ($
2.000.000.000) o el CINCO POR CIENTO (5 %) del total de los depósitos del sis-
tema financiero, si dicha proporción fuere mayor, el BANCO CENTRAL DE LA
REPUBLICA ARGENTINA podrá suspender o reducir la obligación de efectuar los
aportes al FGD, restableciendo total o parcialmente dicha obligación cuando el
FGD disminuya de esa cantidad o de dicha proporción. A los fines de este Artículo,
se computarán solamente los aportes en efectivo realizados por las entidades fi-
nancieras. EL BANCO CENTRAL DE LA REPUBLICA ARGENTINA podrá adecuar
el monto total que debe alcanzar el FGD, cuando considere que el monto acumu-
lado fuera prudente en relación con la situación del mercado financiero y a las fun-
ciones del FGD.
Artículo 9°: En cualquier momento el BANCO CENTRAL DE LA REPUBLICA ARGENTINA
(*) podrá exigir a las entidades financieras el adelanto en la integración de hasta dos
años del mínimo previsto para los aportes normales, ya sea totalmente en efectivo
o incluyendo los compromisos de aporte hasta el máximo autorizado en el Artículo
6º del presente Decreto. También podrá exigir a cualquiera de las entidades finan-
cieras aportantes la constitución de garantías por las operaciones referidas en el
inciso e) del artículo 10 bis del presente decreto. El BANCO CENTRAL DE LA
REPUBLICA ARGENTINA podrá, a requerimiento de SEDESA, debitar directa-
mente los aportes normales o adicionales adeudados por las entidades financieras
de los fondos que éstas tengan depositados en dicha Institución. Del mismo modo
podrá proceder en caso de no otorgarse los compromisos de aportes previstos en
el Artículo 6º del presente decreto.
Las garantías a otorgar por las entidades financieras conforme a lo dispuesto en el
párrafo precedente se determinarán por los importes que individualmente les co-
rrespondan y serán a primer requerimiento y en las condiciones y formalidades
(*) Decreto 1292/99
que al respecto establezca el BANCO CENTRAL DE LA REPUBLICA ARGENTI-
NA.
Artículo 10: Los recursos del FONDO DE GARANTÍA DE LOS DEPÓSITOS (FGD) serán in-
(*) vertidos en: títulos públicos nacionales, sean en moneda nacional o extranjera, en
un porcentaje de su cartera no superior a la proporción de los depósitos en mone-
da local en el total de depósitos a la vista y a plazo del sistema financiero; y en ac-
tivos externos elegibles para las inversiones de las reservas internacionales del
país.
La administración de las inversiones del FONDO DE GARANTÍA DE LOS DEPÓ-
SITOS (FGD) tendrá como objetivo la preservación del capital en inversiones de
alta liquidez, con los máximos rendimientos posibles condicionados a la preserva-
ción del capital, la transparencia y el control en su administración.
Los rendimientos del FONDO DE GARANTÍA DE LOS DEPÓSITOS (FGD) forma-
rán parte del mismo y serán reinvertidos en las mismas condiciones. Mensualmen-
te SEGURO DE DEPÓSITOS SOCIEDAD ANÓNIMA (SEDESA) informará al pú-
blico el saldo del FONDO DE GARANTÍA DE LOS DEPÓSITOS (FGD) y a la SU-
PERINTENDENCIA DE ENTIDADES FINANCIERAS Y CAMBIARIAS dependiente
del BANCO CENTRAL DE LA REPÚBLICA ARGENTINA, la composición de las
inversiones y el saldo del citado Fondo.
Artículo 10: SEDESA podrá realizar con los recursos del FGD las siguientes operaciones:
(bis) (**)
a) Efectivizar la cobertura de la garantía a los depositantes, con los límites y con-
diciones que se establecen en el presente y en sus normas reglamentarias,
complementarias y aclaratorias.
b) Efectuar aportes de capital, aportes no reembolsables o préstamos a:
(I) Las entidades financieras que estén sujetas a un plan de regularización y
saneamiento y a los efectos de apoyar el cumplimiento del mismo;
(II) Las entidades financieras que adquieran activos y asuman a su cargo el
pago de los depósitos de otra entidad sometida al régimen del Artículo 35
bis y concordantes de la Ley de Entidades Financieras, cuando ello fuere
conveniente para compensar la insuficiencia de dichos activos respecto a la
totalidad de los depósitos transferidos; o
(III) Las entidades financieras absorbentes o adquirentes de entidades finan-
cieras en el marco de un plan de regularización y saneamiento.
(*) Decreto N° 1653/15.
(**) Decreto N° 1292/99.
c) Celebrar con entidades financieras que adquieran activos y asuman a su cargo
el pago de los depósitos de otra entidad sometida al régimen del Artículo 35 bis
y concordantes de la Ley de Entidades Financieras, un contrato de opción de
venta a favor de la entidad adquirente sobre todos o parte de los activos trans-
feridos.
La operación prevista en este inciso podrá concretarse mediante la constitución
de un fideicomiso al que ingresen los activos de una entidad sometida al régi-
men del artículo 35 bis de la ley citada y en el cual SEDESA, en su carácter de
administrador del FGD, adquiera derecho de beneficiario sobre el producido de
la venta o liquidación de los activos fideicomitidos.
d) Adquirir depósitos de bancos suspendidos bajo el Artículo 49 de la Carta Orgá-
nica del BANCO CENTRAL DE LA REPUBLICA ARGENTINA (Ley 24.144)
hasta los montos de la garantía previstos en el Artículo 13 del presente Decre-
to, subrogándose en los derechos de los depositantes.
e) Tomar o recibir préstamos o celebrar cualesquiera otras operaciones de crédito
con cargo al FGD, en su carácter de administrador del mismo, por hasta un
monto no superior al total de los aportes normales mensuales y adicionales de
las entidades financieras referidos en el artículo 6°, tanto en efectivo como me-
diante la asunción del compromiso de aportar con arreglo a lo previsto en el ar-
tículo 6°, durante el período de DOS (2) años contados desde el momento en
que el préstamo o la operación de crédito se celebre. A los efectos de deter-
minar el total de aportes durante el plazo de DOS (2) años antes referido, se
computará el monto de los aportes mensuales de cada entidad al tiempo de
contraerse el préstamo o celebrarse la operación de crédito.
f) Realizar, mantener o financiar programas de pase con bancos del exterior que
tengan por finalidad contribuir a la estabilidad del Sistema Financiero, con la
previa conformidad del BANCO CENTRAL DE LA REPUBLICA ARGENTINA y
con cargo al FGD.
La aplicación de las alternativas previstas en los incisos b), c) y d) precedentes así
como las operaciones a las que hace referencia el inciso e) precedente serán de-
cididas exclusivamente por un Comité Directivo, cuyas decisiones serán vinculan-
tes para SEDESA. Tal Comité estará integrado por un representante del BANCO
CENTRAL DE LA REPUBLICA ARGENTINA y un número de vocales a determi-
narse en el Contrato de Fideicomiso entre un mínimo de CUATRO (4) y un máxi-
mo de SIETE (7) representantes de las entidades financieras aportantes al FGD.
El representante del BANCO CENTRAL DE LA REPUBLICA ARGENTINA se des-
empeñará como Presidente, y tendrá derecho de veto pero no de voto.
Los vocales tendrán derecho de voto en proporción a los aportes que realicen al
FGD las entidades que representen y de acuerdo a lo dispuesto en el Contrato de
Fideicomiso.
El Comité Directivo deberá decidir la aplicación de alguna de las alternativas pre-
vistas en los incisos b), c) y d) precedentes cuando, de acuerdo con las estimacio-
nes que puedan realizarse al momento en que deba tomarse la decisión, su adop-
ción implique un costo directo al FGD menor que aquel que resultaría a cargo del
FGD en el caso de serle revocada la autorización para funcionar a la entidad afec-
tada y deba cumplirse con el pago a los depositantes previsto en el inciso a) pre-
cedente, para lo cual deberá tenerse en cuenta la situación patrimonial de la enti-
dad afectada y el recupero probable de los desembolsos de SEDESA por subro-
gación.
Excepcionalmente y en caso de estimarse que la revocación de la autorización pa-
ra funcionar de la entidad afectada pudiera poner en peligro la estabilidad de otras
entidades financieras o del sistema financiero en su conjunto, se podrá admitir la
aplicación de alguna de las alternativas previstas en los incisos b), c) y d) prece-
dentes aunque ello implicara para el FGD un costo directo mayor que el resultante
de la alternativa prevista en el inciso a), sin que en ningún caso el mismo pueda
superar el importe total de los depósitos garantizados impuestos en la entidad fi-
nanciera afectada.
Todo lo referente al Comité Directivo será previsto en el contrato de fideicomiso
que celebren el BANCO CENTRAL DE LA REPUBLICA ARGENTINA Y SEGURO
DE DEPOSITOS SOCIEDAD ANONIMA.
Artículo 11: Estarán alcanzados con la cobertura que ofrece el sistema, los depósitos en PE-
SOS y en moneda extranjera constituidos en las entidades participantes bajo la
forma de cuenta corriente, caja de ahorros, plazo fijo u otras modalidades que de-
termine el BANCO CENTRAL DE LA REPUBLICA ARGENTINA, que reúnan los
requisitos establecidos en el presente decreto y los demás que disponga la Auto-
ridad de Aplicación.
Artículo 12: No están alcanzados por la cobertura del sistema de garantía:
a) los depósitos de entidades financieras en otros intermediarios, incluidos los cer-
tificados de plazo fijo adquiridos por negociación secundaria.
b) los depósitos efectuados por personas vinculadas, directa o indirectamente, a la
entidad según las pautas establecidas o que establezca en el futuro el BANCO
CENTRAL DE LA REPUBLICA ARGENTINA.
c) los depósitos a plazo fijo de títulos valores, aceptaciones o garantías.
d) (*)
e) los demás depósitos que para el futuro excluya la Autoridad de Aplicación.
(*) Derogado por Decreto Nº 30/18.
Artículo 13: La garantía cubrirá la devolución de los depósitos a la vista o a plazo fijo hasta la
(*) suma de pesos TREINTA MIL ($ 30.000).
EL BANCO CENTRAL DE LA REPUBLICA ARGENTINA podrá disponer, en cual-
quier momento y con carácter general, la modificación de ese importe de cobertura
del sistema de garantía, en función de la evolución que experimente el proceso de
consolidación del sistema financiero y los demás indicadores que estime apropia-
dos.
Los depósitos por importes superiores al del monto de la cobertura también que-
dan comprendidos en el régimen de garantía hasta ese límite máximo.
Artículo 13 (bis): SEDESA podrá emitir títulos valores nominativos no endosables a los fines de
(**) ofrecerlos a los depositantes en pago de la garantía de los depósitos, si no contare
con fondos suficientes a esos efectos. Dichos títulos, cuyas condiciones serán es-
tablecidas con carácter general por el Banco Central de la República Argentina,
deberán ser aceptados por las entidades financieras a fin de constituir depósitos
en las condiciones que estipule dicha reglamentación.
Artículo 14: La recepción por los depositantes de las sumas desembolsadas por SEDESA con
las disponibilidades del FGD, importa la subrogación legal a favor de SEDESA en
los derechos de cobro en la liquidación o quiebra de la entidad, con los privilegios
correspondientes a los depositantes y con prioridad de cobro sobre ellos hasta la
concurrencia de las sumas abonadas por SEDESA de acuerdo a lo previsto en el
Artículo 13 del presente Decreto.
Artículo 15: La garantía rige en igualdad de condiciones para personas físicas y jurídicas. Para
determinar el importe alcanzado por la cobertura y su devolución al depositante, se
computará la totalidad de los depósitos que registre cada persona en la entidad a
la fecha de la revocación de su autorización para funcionar. En las cuentas e im-
posiciones a nombre de DOS (2) o más personas, se entenderá que una sola de
ellas goza de la garantía, prorrateándose la misma entre los participantes.
Artículo 16: (**)
Artículo 17: La garantía se hará efectiva en forma subsidiaria y complementaria al reintegro de
los depósitos por aplicación de los privilegios establecidos por la Ley de Entidades
Financieras, dentro de los TREINTA (30) días hábiles contados desde el día si-
guiente al de la revocación de la autorización para funcionar de la entidad, en la
medida en que los depositantes cumplan los requisitos establecidos y el FGD ten-
ga disponibilidades. A solicitud de SEDESA, el BANCO CENTRAL DE LA
REPUBLICA ARGENTINA podrá autorizar la extensión de dicho plazo cuando la
cantidad de beneficiarios en trámite de liquidación lo justifique.
Cuando los recursos del FGD fueren insuficientes para atender el pago de las
sumas garantizadas, el reintegro se efectuará a prorrata de los fondos disponi-
bles. El saldo se liquidará dentro de los TREINTA (30) días contados desde la fe-
cha en que el FGD informe la existencia de disponibilidades financieras. En estas
situaciones y cuando haya más de una entidad cuya autorización hubiere sido re-
vocada, la prelación para el reintegro se regirá por el orden cronológico resultante
(*) Decreto 1127/98. Vigencia: 28.9.98
(**) Decreto 214/02. Vigencia: 03.02.02
(***) Derogado por Decreto 1127/98.
del comienzo del cómputo del plazo de pago de la garantía. En ningún caso el
FGD cubrirá o reconocerá intereses por el período comprendido entre el venci-
miento original del depósito y la fecha de pago de la garantía.
Artículo 18: El pago de las sumas garantizadas se realizará en pesos o en moneda extranjera,
según la proporción de cada especie que resulte del total del capital depositado. A
ese último fin y para homogeneizar los saldos del total depositado, cuando se tra-
te de depósitos en moneda extranjera, se tomará su equivalente en pesos según
la cotización del tipo de cambio vendedor para billetes del BANCO DE LA NA-
CION ARGENTINA, correspondiente al día anterior a la revocación de la autoriza-
ción para funcionar de la entidad comprendida.
Artículo 19: SEDESA podrá rechazar o posponer hasta su reconocimiento judicial el pedido de
cobertura de la garantía cuando los depósitos respectivos no reunieren los requi-
sitos formales o sustanciales establecidos en la presente reglamentación u otras
disposiciones que dicte el BANCO CENTRAL DE LA REPUBLICA ARGENTINA.
Artículo 20: SEDESA podrá ejercer las acciones judiciales correspondientes cuando a su juicio
existan posibilidades reales de recuperar los importes desembolsados.
Artículo 21: El régimen establecido en el presente Decreto regirá respecto de los depósitos a
plazo fijo que se constituyan o renueven a partir del día 18 de abril de 1995, y res-
pecto de los depósitos a la vista que se registren en los saldos correspondientes
al cierre de ese día, constituidos en entidades financieras que no estuvieren sus-
pendidas por el BANCO CENTRAL DE LA REPUBLICA ARGENTINA ni se les
hubiese revocado su autorización para funcionar.
Artículo 22: El BANCO CENTRAL DE LA REPUBLICA ARGENTINA será la Autoridad de Apli-
cación del sistema creado por la ley 24.485 y reglamentado por el presente De-
creto, quedando facultado para dictar las normas interpretativas y de aplicación
que resulten necesarias.
Artículo 23: El Directorio de SEDESA deberá comunicar a la SUPERINTENDENCIA DE ENTI-
DADES FINANCIERAS Y CAMBIARIAS dependiente del BANCO CENTRAL DE
LA REPUBLICA ARGENTINA, su opinión respecto de las entidades financieras
que, a su juicio, tuvieren políticas crediticias o comerciales que se estimen de
riesgo superior al normal. Asimismo podrá requerírsele opinión respecto de las so-
licitudes de autorización para funcionar o de transformación que se encuentren a
consideración del BANCO CENTRAL DE LA REPUBLICA ARGENTINA.
Artículo 24: El presente Decreto entrará en vigencia partir del mismo día de su publicación en
(*) el Boletín Oficial.
```

Versión: primer intento (cola). Entidades 49, relaciones 54.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Texto Ordenado Seguro de Depósitos", "properties": {}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Comunicacion", "label": "Decreto 540/95", "properties": {"codigo": "Decreto 540/95"}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- {"local_id": "e2", "type": "Operacion", "label": "Creación del Fondo de Garantía de Depósitos", "properties": {"tipo": "Constitución de fondo", "descripcion": "Creación del Fondo de Garantía de Depósitos (FGD) con la finalidad de cubrir los depósitos bancarios con el alcance previsto en el Decreto."}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- {"local_id": "e3", "type": "Operacion", "label": "Constitución de SEDESA como fiduciario", "properties": {"tipo": "Constitución de sociedad", "descripcion": "Constitución de la sociedad SEGURO DE DEPOSITOS SOCIEDAD ANONIMA (SEDESA) con el objeto exclusivo de ejercer las funciones de fiduciario que le encomiende el ESTADO NACIONAL o el BANCO CENTRAL DE LA REPUBLICA ARGENTINA."}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crud
- {"local_id": "e4", "type": "Obligacion", "label": "Integración del FGD con aporte normal mensual", "properties": {"tipo": "asignacion", "descripcion": "Las entidades financieras autorizadas para operar en la República Argentina deberán integrar el FGD con un aporte normal mensual determinado por el BANCO CENTRAL entre un mínimo de 0,015% y un máximo de 0,06% del promedio de los saldos diarios de los depósitos en pesos y en moneda extranjera, más aportes adicionales según indicadores de riesgo.",
- {"local_id": "e5", "type": "Restriccion", "label": "Límite aporte adicional al 100% del aporte normal", "properties": {"tipo": "limite_cuantitativo", "descripcion": "El aporte adicional no podrá superar el equivalente a un aporte normal.", "umbrales": "no podrá superar el equivalente a un aporte normal"}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- {"local_id": "e6", "type": "Excepcion", "label": "Exclusión de depósitos de cuentas oficiales nacionales", "properties": {"descripcion": "Quedan excluidos del cálculo del promedio de saldos diarios los depósitos correspondientes a las cuentas oficiales nacionales abiertas en el Banco de la Nación Argentina."}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- {"local_id": "e7", "type": "Potestad", "label": "Facultad de determinar forma de integración del aporte", "properties": {"descripcion": "El BANCO CENTRAL DE LA REPUBLICA ARGENTINA podrá disponer que la integración del aporte sea en efectivo o mediante la asunción del compromiso de efectuar el mismo, en las condiciones y formalidades que determine."}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 7}
- {"local_id": "e8", "type": "Restriccion", "label": "Límite compromisos de aporte al 50%", "properties": {"tipo": "limite_cuantitativo", "descripcion": "Los compromisos de aporte no podrán superar el 50% del aporte que corresponda efectuar.", "umbrales": "no podrán superar el CINCUENTA POR CIENTO (50%)"}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 8}
- {"local_id": "e9", "type": "Obligacion", "label": "Depósito puntual de aportes como condición para operar", "properties": {"tipo": "asignacion", "descripcion": "Las entidades financieras deberán depositar puntualmente sus aportes como condición para operar regularmente."}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 9}
- {"local_id": "e10", "type": "Potestad", "label": "Facultad de suspender o reducir obligación de aportes", "properties": {"descripcion": "El BANCO CENTRAL DE LA REPUBLICA ARGENTINA podrá suspender o reducir la obligación de efectuar los aportes al FGD cuando alcance la suma de $2.000.000.000 o el 5% del total de los depósitos del sistema financiero, si dicha proporción fuere mayor."}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indic
- {"local_id": "e11", "type": "Condicion", "label": "Condición: FGD alcanza $2.000.000.000 o 5% de depósitos", "properties": {"descripcion": "El FGD alcanza la suma de $2.000.000.000 o el 5% del total de los depósitos del sistema financiero, si dicha proporción fuere mayor.", "umbrales": "DOS MIL MILLONES DE PESOS ($ 2.000.000.000) | CINCO POR CIENTO (5 %)"}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 11}
- {"local_id": "e12", "type": "Potestad", "label": "Facultad de exigir adelanto de aportes hasta dos años", "properties": {"descripcion": "El BANCO CENTRAL DE LA REPUBLICA ARGENTINA podrá exigir a las entidades financieras el adelanto en la integración de hasta dos años del mínimo previsto para los aportes normales, ya sea totalmente en efectivo o incluyendo los compromisos de aporte hasta el máximo autorizado."}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documen
- {"local_id": "e13", "type": "Potestad", "label": "Facultad de exigir garantías por operaciones de crédito", "properties": {"descripcion": "El BANCO CENTRAL DE LA REPUBLICA ARGENTINA podrá exigir a cualquiera de las entidades financieras aportantes la constitución de garantías por las operaciones de crédito referidas en el inciso e) del artículo 10 bis."}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 13}
- {"local_id": "e14", "type": "Potestad", "label": "Facultad de debitar directamente aportes adeudados", "properties": {"descripcion": "El BANCO CENTRAL DE LA REPUBLICA ARGENTINA podrá, a requerimiento de SEDESA, debitar directamente los aportes normales o adicionales adeudados por las entidades financieras de los fondos que éstas tengan depositados en dicha Institución."}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 14
- {"local_id": "e15", "type": "Operacion", "label": "Inversión de recursos del FGD en títulos públicos y activos externos", "properties": {"tipo": "Inversión de fondos", "descripcion": "Los recursos del FGD serán invertidos en títulos públicos nacionales (en moneda nacional o extranjera) en un porcentaje no superior a la proporción de los depósitos en moneda local en el total de depósitos a la vista y a plazo del sistema financiero, y en activos externos elegibles para las inversiones de las reser
- {"local_id": "e16", "type": "Obligacion", "label": "Informe mensual de saldo del FGD al público", "properties": {"tipo": "comunicacion_a_cliente", "descripcion": "SEDESA informará mensualmente al público el saldo del FGD.", "frecuencia": "Mensualmente"}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 16}
- {"local_id": "e17", "type": "Obligacion", "label": "Reporte a Superintendencia de composición de inversiones", "properties": {"tipo": "reporte_al_supervisor", "descripcion": "SEDESA informará a la SUPERINTENDENCIA DE ENTIDADES FINANCIERAS Y CAMBIARIAS la composición de las inversiones y el saldo del FGD.", "frecuencia": "Mensualmente"}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 17}
- {"local_id": "e18", "type": "Operacion", "label": "Efectivización de cobertura de garantía a depositantes", "properties": {"tipo": "Pago de garantía", "descripcion": "SEDESA podrá efectivizar la cobertura de la garantía a los depositantes, con los límites y condiciones establecidos en el presente decreto y sus normas reglamentarias, complementarias y aclaratorias."}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 18}
- {"local_id": "e19", "type": "Operacion", "label": "Aportes de capital o préstamos a entidades en regularización", "properties": {"tipo": "Aporte de capital o préstamo", "descripcion": "SEDESA podrá efectuar aportes de capital, aportes no reembolsables o préstamos a las entidades financieras que estén sujetas a un plan de regularización y saneamiento a los efectos de apoyar el cumplimiento del mismo."}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "pun
- {"local_id": "e20", "type": "Operacion", "label": "Aportes a entidades adquirentes de activos de entidad en régimen 35 bis", "properties": {"tipo": "Aporte de capital o préstamo", "descripcion": "SEDESA podrá efectuar aportes de capital, aportes no reembolsables o préstamos a las entidades financieras que adquieran activos y asuman a su cargo el pago de los depósitos de otra entidad sometida al régimen del Artículo 35 bis, cuando ello fuere conveniente para compensar la insuficiencia de dichos a
- {"local_id": "e21", "type": "Operacion", "label": "Aportes a entidades absorbentes en plan de regularización", "properties": {"tipo": "Aporte de capital o préstamo", "descripcion": "SEDESA podrá efectuar aportes de capital, aportes no reembolsables o préstamos a las entidades financieras absorbentes o adquirentes de entidades financieras en el marco de un plan de regularización y saneamiento."}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_prop
- {"local_id": "e22", "type": "Operacion", "label": "Contrato de opción de venta sobre activos transferidos", "properties": {"tipo": "Contrato de opción", "descripcion": "SEDESA podrá celebrar con entidades financieras que adquieran activos y asuman a su cargo el pago de los depósitos de otra entidad sometida al régimen del Artículo 35 bis, un contrato de opción de venta a favor de la entidad adquirente sobre todos o parte de los activos transferidos."}, "provenance": {"to": "seggar", "archivo": "
- {"local_id": "e23", "type": "Operacion", "label": "Fideicomiso de activos con derecho de beneficiario para SEDESA", "properties": {"tipo": "Constitución de fideicomiso", "descripcion": "La operación de contrato de opción podrá concretarse mediante la constitución de un fideicomiso al que ingresen los activos de una entidad sometida al régimen del artículo 35 bis, en el cual SEDESA adquiera derecho de beneficiario sobre el producido de la venta o liquidación de los activos fideicomitidos."}, "pro
- {"local_id": "e24", "type": "Operacion", "label": "Adquisición de depósitos de bancos suspendidos", "properties": {"tipo": "Adquisición de depósitos", "descripcion": "SEDESA podrá adquirir depósitos de bancos suspendidos bajo el Artículo 49 de la Carta Orgánica del BANCO CENTRAL hasta los montos de la garantía previstos en el Artículo 13, subrogándose en los derechos de los depositantes."}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"},
- {"local_id": "e25", "type": "Operacion", "label": "Toma de préstamos o créditos con cargo al FGD", "properties": {"tipo": "Toma de crédito", "descripcion": "SEDESA podrá tomar o recibir préstamos o celebrar operaciones de crédito con cargo al FGD, por hasta un monto no superior al total de los aportes normales mensuales y adicionales de las entidades financieras, tanto en efectivo como mediante la asunción del compromiso de aportar, durante el período de dos años contados desde el momento en que
- {"local_id": "e26", "type": "Operacion", "label": "Programas de pase con bancos del exterior", "properties": {"tipo": "Operación de pase", "descripcion": "SEDESA podrá realizar, mantener o financiar programas de pase con bancos del exterior que tengan por finalidad contribuir a la estabilidad del Sistema Financiero, con la previa conformidad del BANCO CENTRAL DE LA REPUBLICA ARGENTINA y con cargo al FGD."}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental":
- {"local_id": "e27", "type": "Definicion", "label": "Depósitos alcanzados por la cobertura", "properties": {"termino": "depósitos alcanzados por la cobertura", "descripcion": "Los depósitos en pesos y en moneda extranjera constituidos en las entidades participantes bajo la forma de cuenta corriente, caja de ahorros, plazo fijo u otras modalidades que determine el BANCO CENTRAL, que reúnan los requisitos establecidos en el presente decreto."}, "provenance": {"to": "seggar", "archivo": "seggar.pdf"
- {"local_id": "e28", "type": "Restriccion", "label": "Exclusión depósitos de entidades financieras en otros intermediarios", "properties": {"tipo": "prohibicion", "descripcion": "No están alcanzados por la cobertura del sistema de garantía los depósitos de entidades financieras en otros intermediarios, incluidos los certificados de plazo fijo adquiridos por negociación secundaria."}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice
- {"local_id": "e29", "type": "Restriccion", "label": "Exclusión depósitos de personas vinculadas", "properties": {"tipo": "prohibicion", "descripcion": "No están alcanzados por la cobertura del sistema de garantía los depósitos efectuados por personas vinculadas, directa o indirectamente, a la entidad según las pautas establecidas o que establezca en el futuro el BANCO CENTRAL."}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_cr
- {"local_id": "e30", "type": "Restriccion", "label": "Exclusión depósitos a plazo fijo de títulos valores", "properties": {"tipo": "prohibicion", "descripcion": "No están alcanzados por la cobertura del sistema de garantía los depósitos a plazo fijo de títulos valores, aceptaciones o garantías."}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 30}
- {"local_id": "e31", "type": "Restriccion", "label": "Límite de cobertura $30.000", "properties": {"tipo": "limite_cuantitativo", "descripcion": "La garantía cubrirá la devolución de los depósitos a la vista o a plazo fijo hasta la suma de $30.000.", "umbrales": "hasta la suma de pesos TREINTA MIL ($ 30.000)"}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 31}
- {"local_id": "e32", "type": "Potestad", "label": "Facultad de modificar importe de cobertura", "properties": {"descripcion": "El BANCO CENTRAL DE LA REPUBLICA ARGENTINA podrá disponer, en cualquier momento y con carácter general, la modificación del importe de cobertura del sistema de garantía, en función de la evolución que experimente el proceso de consolidación del sistema financiero y los demás indicadores que estime apropiados."}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "pun
- {"local_id": "e33", "type": "Operacion", "label": "Emisión de títulos valores para pago de garantía", "properties": {"tipo": "Emisión de títulos", "descripcion": "SEDESA podrá emitir títulos valores nominativos no endosables a los fines de ofrecerlos a los depositantes en pago de la garantía de los depósitos, si no contare con fondos suficientes a esos efectos."}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 33}
- {"local_id": "e34", "type": "Obligacion", "label": "Aceptación de títulos por entidades financieras", "properties": {"tipo": "otra", "descripcion": "Las entidades financieras deberán aceptar los títulos valores emitidos por SEDESA a fin de constituir depósitos en las condiciones que estipule la reglamentación del BANCO CENTRAL."}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 34}
- {"local_id": "e35", "type": "Operacion", "label": "Subrogación de SEDESA en derechos de depositantes", "properties": {"tipo": "Subrogación", "descripcion": "La recepción por los depositantes de las sumas desembolsadas por SEDESA importa la subrogación legal a favor de SEDESA en los derechos de cobro en la liquidación o quiebra de la entidad, con los privilegios correspondientes a los depositantes y con prioridad de cobro hasta la concurrencia de las sumas abonadas."}, "provenance": {"to": "segga
- {"local_id": "e36", "type": "Definicion", "label": "Cálculo de importe alcanzado por cobertura", "properties": {"termino": "importe alcanzado por la cobertura", "descripcion": "Se computará la totalidad de los depósitos que registre cada persona en la entidad a la fecha de la revocación de su autorización para funcionar."}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 36}
- {"local_id": "e37", "type": "Definicion", "label": "Cuentas a nombre de dos o más personas", "properties": {"termino": "cuentas a nombre de dos o más personas", "descripcion": "Se entenderá que una sola de ellas goza de la garantía, prorrateándose la misma entre los participantes."}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 37}
- {"local_id": "e38", "type": "Obligacion", "label": "Efectivización de garantía dentro de 30 días hábiles", "properties": {"tipo": "otra", "descripcion": "La garantía se hará efectiva en forma subsidiaria y complementaria al reintegro de los depósitos por aplicación de los privilegios establecidos por la Ley de Entidades Financieras, dentro de los 30 días hábiles contados desde el día siguiente al de la revocación de la autorización para funcionar de la entidad.", "umbrales": "dentro de los TREIN
- {"local_id": "e39", "type": "Potestad", "label": "Facultad de extender plazo de pago de garantía", "properties": {"descripcion": "El BANCO CENTRAL DE LA REPUBLICA ARGENTINA podrá autorizar la extensión del plazo de pago de la garantía a solicitud de SEDESA cuando la cantidad de beneficiarios en trámite de liquidación lo justifique."}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 39}
- {"local_id": "e40", "type": "Obligacion", "label": "Reintegro a prorrata cuando FGD insuficiente", "properties": {"tipo": "otra", "descripcion": "Cuando los recursos del FGD fueren insuficientes para atender el pago de las sumas garantizadas, el reintegro se efectuará a prorrata de los fondos disponibles."}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 40}
- {"local_id": "e41", "type": "Obligacion", "label": "Liquidación de saldo dentro de 30 días", "properties": {"tipo": "otra", "descripcion": "El saldo se liquidará dentro de los 30 días contados desde la fecha en que el FGD informe la existencia de disponibilidades financieras.", "umbrales": "dentro de los TREINTA (30) días"}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 41}
- {"local_id": "e42", "type": "Restriccion", "label": "Exclusión de intereses en pago de garantía", "properties": {"tipo": "prohibicion", "descripcion": "El FGD no cubrirá ni reconocerá intereses por el período comprendido entre el vencimiento original del depósito y la fecha de pago de la garantía."}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 42}
- {"local_id": "e43", "type": "Operacion", "label": "Pago de garantía en pesos o moneda extranjera", "properties": {"tipo": "Pago de garantía", "descripcion": "El pago de las sumas garantizadas se realizará en pesos o en moneda extranjera, según la proporción de cada especie que resulte del total del capital depositado."}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 43}
- {"local_id": "e44", "type": "Potestad", "label": "Facultad de rechazar o posponer pedido de cobertura", "properties": {"descripcion": "SEDESA podrá rechazar o posponer hasta su reconocimiento judicial el pedido de cobertura de la garantía cuando los depósitos respectivos no reunieren los requisitos formales o sustanciales establecidos en la presente reglamentación u otras disposiciones que dicte el BANCO CENTRAL."}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_doc
- {"local_id": "e45", "type": "Potestad", "label": "Facultad de ejercer acciones judiciales", "properties": {"descripcion": "SEDESA podrá ejercer las acciones judicales correspondientes cuando a su juicio existan posibilidades reales de recuperar los importes desembolsados."}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 45}
- {"local_id": "e46", "type": "Condicion", "label": "Condición: depósitos constituidos o renovados desde 18.4.95", "properties": {"descripcion": "El régimen rige respecto de los depósitos a plazo fijo que se constituyan o renueven a partir del 18 de abril de 1995, y respecto de los depósitos a la vista que se registren en los saldos correspondientes al cierre de ese día, constituidos en entidades financieras que no estuvieren suspendidas ni se les hubiese revocado su autorización para funcionar."}
- {"local_id": "e47", "type": "Obligacion", "label": "Comunicación de opinión sobre políticas crediticias", "properties": {"tipo": "reporte_al_supervisor", "descripcion": "El Directorio de SEDESA deberá comunicar a la SUPERINTENDENCIA DE ENTIDADES FINANCIERAS Y CAMBIARIAS su opinión respecto de las entidades financieras que, a su juicio, tuvieren políticas crediticias o comerciales que se estimen de riesgo superior al normal."}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2
- {"local_id": "e48", "type": "Potestad", "label": "Facultad de requerir opinión sobre solicitudes de autorización", "properties": {"descripcion": "Podrá requerírsele opinión al Directorio de SEDESA respecto de las solicitudes de autorización para funcionar o de transformación que se encuentren a consideración del BANCO CENTRAL."}, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 48}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e3", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e4", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e5", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- relación: {"source": "e6", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- relación: {"source": "e7", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- relación: {"source": "e8", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- relación: {"source": "e9", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 7}
- relación: {"source": "e10", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 8}
- relación: {"source": "e11", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 9}
- relación: {"source": "e12", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 10}
- relación: {"source": "e13", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 11}
- relación: {"source": "e14", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 12}
- relación: {"source": "e15", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 13}
- relación: {"source": "e16", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 14}
- relación: {"source": "e17", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 15}
- relación: {"source": "e18", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 16}
- relación: {"source": "e19", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 17}
- relación: {"source": "e20", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 18}
- relación: {"source": "e21", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 19}
- relación: {"source": "e22", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 20}
- relación: {"source": "e23", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 21}
- relación: {"source": "e24", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 22}
- relación: {"source": "e25", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 23}
- relación: {"source": "e26", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 24}
- relación: {"source": "e27", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 25}
- relación: {"source": "e28", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 26}
- relación: {"source": "e29", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 27}
- relación: {"source": "e30", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 28}
- relación: {"source": "e31", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 29}
- relación: {"source": "e32", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 30}
- relación: {"source": "e33", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 31}
- relación: {"source": "e34", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 32}
- relación: {"source": "e35", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 33}
- relación: {"source": "e36", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 34}
- relación: {"source": "e37", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 35}
- relación: {"source": "e38", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 36}
- relación: {"source": "e39", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 37}
- relación: {"source": "e40", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 38}
- relación: {"source": "e41", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 39}
- relación: {"source": "e42", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 40}
- relación: {"source": "e43", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 41}
- relación: {"source": "e44", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 42}
- relación: {"source": "e45", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 43}
- relación: {"source": "e46", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 44}
- relación: {"source": "e47", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 45}
- relación: {"source": "e48", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 46}
- relación: {"source": "to", "target": "e1", "predicate": "referencia", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 47}
- relación: {"source": "e4", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 48}
- relación: {"source": "e9", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 49}
- relación: {"source": "e34", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 50}
- relación: {"source": "e11", "target": "e10", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 51}
- relación: {"source": "e31", "target": "e18", "predicate": "limita", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 54}
- relación: {"source": "e42", "target": "e43", "predicate": "prohibe", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "seggar", "archivo": "seggar.pdf", "punto": "8.2", "rol_documental": "punto_propio"}, "indice_crudo": 58}

## 14. `autenf::3.1.2.3` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 7):

```
[encabezado | punto S3]
Sección 3. Antecedentes.
[encabezado | punto 3.1]
3.1. Autoridades sujetas a la previa evaluación de sus antecedentes.
[encabezado | punto 3.1.2]
3.1.2. Autoridades alcanzadas.
[intro | punto 3.1.2]
Están sujetas a la previa evaluación de sus antecedentes las nuevas autoridades que
se indican a continuación:
[texto propio | punto 3.1.2.3]
3.1.2.3. Síndicos e integrantes del Consejo de Vigilancia (o equivalente).
```

Versión: primer intento (cola). Entidades 8, relaciones 14.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Autoridades de entidades financieras", "properties": {}, "provenance": {"to": "autenf", "archivo": "autenf.pdf", "punto": "3.1.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Operacion", "label": "Designación de síndicos e integrantes del Consejo de Vigilancia", "properties": {"tipo": "Designación de autoridad", "descripcion": "Designación o propuesta de síndicos e integrantes del Consejo de Vigilancia o equivalente en entidades financieras"}, "provenance": {"to": "autenf", "archivo": "autenf.pdf", "punto": "3.1.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- {"local_id": "e2", "type": "Obligacion", "label": "Evaluación previa de antecedentes — síndicos y consejeros de vigilancia", "properties": {"tipo": "presentacion_informativa", "descripcion": "Las nuevas autoridades que se desempeñen como síndicos e integrantes del Consejo de Vigilancia o equivalente están sujetas a la previa evaluación de sus antecedentes por el BCRA"}, "provenance": {"to": "autenf", "archivo": "autenf.pdf", "punto": "3.1.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 
- {"local_id": "e3", "type": "Excepcion", "label": "Excepción evaluación previa — síndicos con antecedentes en EF", "properties": {"descripcion": "Síndicos e integrantes del Consejo de Vigilancia quedan exceptuados de la previa evaluación de antecedentes cuando cumplen con las condiciones de antecedentes en EF, plazo máximo de 3 años desde cese anterior, y cargo de igual o menor clase", "umbrales": "El período entre el cese en ese cargo y la nueva propuesta o designación, por parte del órgano de g
- {"local_id": "e4", "type": "Condicion", "label": "Antecedentes previos en entidad financiera — síndicos", "properties": {"descripcion": "Haber ejercido anteriormente un cargo de autoridad sujeta a evaluación previa en una entidad financiera"}, "provenance": {"to": "autenf", "archivo": "autenf.pdf", "punto": "3.1.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- {"local_id": "e5", "type": "Condicion", "label": "Plazo máximo entre cese y nueva designación — síndicos", "properties": {"descripcion": "El tiempo transcurrido entre el cese en el cargo anterior y la nueva propuesta o designación no debe exceder 3 años", "umbrales": "no sea mayor a 3 años"}, "provenance": {"to": "autenf", "archivo": "autenf.pdf", "punto": "3.1.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- {"local_id": "e6", "type": "Condicion", "label": "Cargo de igual o menor clase — síndicos", "properties": {"descripcion": "El nuevo cargo debe ser en una entidad financiera de igual o menor clase y de igual o inferior Grupo según la Ley de Entidades Financieras"}, "provenance": {"to": "autenf", "archivo": "autenf.pdf", "punto": "3.1.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- {"local_id": "e7", "type": "Obligacion", "label": "Certificación anual de condiciones de habilidad — síndicos", "properties": {"tipo": "presentacion_informativa", "frecuencia": "anualmente", "descripcion": "Las entidades financieras deben certificar anualmente que la persona que se desempeña como síndico o integrante del Consejo de Vigilancia mantiene las condiciones de habilidad legal, idoneidad, competencia, experiencia en la actividad financiera y posibilidad de dedicación funcional"}, "prove
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "autenf", "archivo": "autenf.pdf", "punto": "3.1.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "autenf", "archivo": "autenf.pdf", "punto": "3.1.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e3", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "autenf", "archivo": "autenf.pdf", "punto": "3.1.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e4", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "autenf", "archivo": "autenf.pdf", "punto": "3.1.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- relación: {"source": "e5", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "autenf", "archivo": "autenf.pdf", "punto": "3.1.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- relación: {"source": "e6", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "autenf", "archivo": "autenf.pdf", "punto": "3.1.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- relación: {"source": "e7", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "autenf", "archivo": "autenf.pdf", "punto": "3.1.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- relación: {"source": "e3", "target": "e2", "predicate": "exceptua_obligacion", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "autenf", "archivo": "autenf.pdf", "punto": "3.1.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 7}
- relación: {"source": "e4", "target": "e3", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "autenf", "archivo": "autenf.pdf", "punto": "3.1.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 8}
- relación: {"source": "e5", "target": "e3", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "autenf", "archivo": "autenf.pdf", "punto": "3.1.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 9}
- relación: {"source": "e6", "target": "e3", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "autenf", "archivo": "autenf.pdf", "punto": "3.1.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 10}
- relación: {"source": "e2", "target": null, "predicate": "aplica_a", "sujeto_id": null, "sujeto_propuesto": "Síndicos e integrantes del Consejo de Vigilancia (o equivalente)", "sujeto_propuesto_padre_sugerido": "Sujeto_rol_alcance_autenf", "provenance": {"to": "autenf", "archivo": "autenf.pdf", "punto": "3.1.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 11}
- relación: {"source": "e3", "target": null, "predicate": "aplica_a", "sujeto_id": null, "sujeto_propuesto": "Síndicos e integrantes del consejo de vigilancia o equivalentes", "sujeto_propuesto_padre_sugerido": "Sujeto_rol_alcance_autenf", "provenance": {"to": "autenf", "archivo": "autenf.pdf", "punto": "3.1.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 12}
- relación: {"source": "e7", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "autenf", "archivo": "autenf.pdf", "punto": "3.1.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 13}

## 15. `rmgcti::10.1` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 44, 45):

```
[encabezado | punto S10]
Sección 10. Gestión de la relación con terceras partes.
[texto propio | punto 10.1]
10.1. Exigencia de notificación previa.
Las entidades deberán informar a la Gerencia de Auditoría Externa de Sistemas de la Super-
intendencia de Entidades Financieras y Cambiarias (SEFYC) las características de los servi-
cios críticos a tercerizar, con una antelación no inferior a 60 días corridos del inicio de la terce-
rización.
La notificación previa de los servicios críticos a tercerizar deberá contener:
- La naturaleza de los servicios, conforme a la siguiente taxonomía:
• Procesamiento de datos en infraestructuras tradicionales.
• Infraestructura y procesamiento en modalidad Infrastructure as a Service (IaaS).
• Soluciones en modalidad Platform as a Service (PaaS).
• Soluciones en modalidad Software as a Service (SaaS).
• Administración y gestión de datos.
• Control de acceso a la infraestructura, a los sistemas y a los datos.
• Operaciones de seguridad (incluye SOC).
• Gestión de ciberincidentes (en cualquiera de sus etapas).
• Actividades de back-office con soporte tecnológico.
• Administración de pagos.
• Gestión de las comunicaciones y redes.
• Desarrollo, soporte y mantenimiento.
• Gestión de copias de respaldo.
• Otros servicios considerados críticos.
- Una descripción de los servicios y actividades alcanzados.
- Las ubicaciones geográficas (país, región, ciudad) donde se desarrollarán cada una de las
actividades.
- Las ubicaciones geográficas (país, región, ciudad) donde se realizarán las tareas de control
sobre las actividades.
- La fecha de puesta en funcionamiento de las actividades.
- Los datos del responsable de contacto directo en el tercero prestador de servicios (nombre,
función, teléfono y correo electrónico).
- Cuando la actividad contemple subcontrataciones (“n-ésimas partes”), deberá identificarse
cada uno de los prestadores, la actividad que realizará y las ubicaciones geográficas.
- Los instrumentos que formalicen la tercerización.
- Un plan de continuidad operativa que cumpla con los requisitos normativos vigentes.
- Contar con soluciones de continuidad alternativas conforme a lo previsto en las Secciones
3. y 6.
- En el caso de tercerización de servicios intra-grupo en el exterior, se deberá contar con una
certificación escrita del ente supervisor del país de origen que indique que:
• Se encuentra en conocimiento y no objeta la tercerización.
• Los servicios tercerizados formarán parte de su programa normal de supervisión.
• Se encuentra sujeta a principios, estándares o normas prevención del Lavado de Acti-
vos, la Financiación del Terrorismo y la Financiación de la Proliferación de Armas de
Destrucción Masiva (LA/FT/FPADM) internacionalmente aceptados, entre otros los di-
fundidos por el Grupo de Acción Financiera Internacional (FATF-GAFI) y el Comité de
Supervisión Bancaria de Basilea.
• Además, respecto de la forma de supervisión, que adhiere a los “Principios básicos para
una supervisión bancaria eficaz”, divulgados por el Comité de Supervisión Bancaria de
Basilea. Y también aplica supervisión consolidada asumiendo la vigilancia de la liquidez
y solvencia, así como la evaluación y el control de los riesgos y situaciones patrimonia-
les considerados en forma consolidada.
```

Versión: primer intento (cola). Entidades 17, relaciones 35.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Gestión de la relación con terceras partes", "properties": {}, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Obligacion", "label": "Notificación previa de servicios críticos a tercerizar", "properties": {"descripcion": "Las entidades deben informar a la SEFYC las características de los servicios críticos a tercerizar con una antelación no inferior a 60 días corridos del inicio de la tercerización.", "tipo": "reporte_al_supervisor", "frecuencia": "previa al inicio de la tercerización", "umbrales": "no inferior a 60 días corridos"}, "provenance": {"to": "rmgcti", "archivo": "r
- {"local_id": "e2", "type": "Obligacion", "label": "Contenido de notificación: naturaleza de servicios", "properties": {"descripcion": "La notificación debe incluir la naturaleza de los servicios conforme a la taxonomía especificada: procesamiento de datos en infraestructuras tradicionales, IaaS, PaaS, SaaS, administración y gestión de datos, control de acceso, operaciones de seguridad, gestión de ciberincidentes, actividades de back-office, administración de pagos, gestión de comunicaciones y re
- {"local_id": "e3", "type": "Obligacion", "label": "Contenido de notificación: descripción de servicios y actividades", "properties": {"descripcion": "La notificación debe incluir una descripción de los servicios y actividades alcanzados.", "tipo": "presentacion_informativa"}, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- {"local_id": "e4", "type": "Obligacion", "label": "Contenido de notificación: ubicaciones geográficas de desarrollo", "properties": {"descripcion": "La notificación debe incluir las ubicaciones geográficas (país, región, ciudad) donde se desarrollarán cada una de las actividades.", "tipo": "presentacion_informativa"}, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- {"local_id": "e5", "type": "Obligacion", "label": "Contenido de notificación: ubicaciones geográficas de control", "properties": {"descripcion": "La notificación debe incluir las ubicaciones geográficas (país, región, ciudad) donde se realizarán las tareas de control sobre las actividades.", "tipo": "presentacion_informativa"}, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- {"local_id": "e6", "type": "Obligacion", "label": "Contenido de notificación: fecha de puesta en funcionamiento", "properties": {"descripcion": "La notificación debe incluir la fecha de puesta en funcionamiento de las actividades.", "tipo": "presentacion_informativa"}, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- {"local_id": "e7", "type": "Obligacion", "label": "Contenido de notificación: datos del responsable de contacto", "properties": {"descripcion": "La notificación debe incluir los datos del responsable de contacto directo en el tercero prestador de servicios: nombre, función, teléfono y correo electrónico.", "tipo": "presentacion_informativa"}, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 7}
- {"local_id": "e8", "type": "Obligacion", "label": "Contenido de notificación: identificación de subcontrataciones", "properties": {"descripcion": "Cuando la actividad contemple subcontrataciones (n-ésimas partes), la notificación debe identificar cada uno de los prestadores, la actividad que realizará y las ubicaciones geográficas.", "tipo": "presentacion_informativa"}, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 8}
- {"local_id": "e9", "type": "Obligacion", "label": "Contenido de notificación: instrumentos de formalización", "properties": {"descripcion": "La notificación debe incluir los instrumentos que formalicen la tercerización.", "tipo": "presentacion_informativa"}, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 9}
- {"local_id": "e10", "type": "Obligacion", "label": "Contenido de notificación: plan de continuidad operativa", "properties": {"descripcion": "La notificación debe incluir un plan de continuidad operativa que cumpla con los requisitos normativos vigentes.", "tipo": "presentacion_informativa"}, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 10}
- {"local_id": "e11", "type": "Obligacion", "label": "Contenido de notificación: soluciones de continuidad alternativas", "properties": {"descripcion": "La notificación debe incluir soluciones de continuidad alternativas conforme a lo previsto en las Secciones 3 y 6.", "tipo": "presentacion_informativa"}, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 11}
- {"local_id": "e12", "type": "Condicion", "label": "Tercerización de servicios intra-grupo en el exterior", "properties": {"descripcion": "Cuando la tercerización de servicios se realiza intra-grupo en el exterior."}, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 12}
- {"local_id": "e13", "type": "Obligacion", "label": "Certificación del ente supervisor: conocimiento y no objeción", "properties": {"descripcion": "Se debe contar con una certificación escrita del ente supervisor del país de origen que indique que se encuentra en conocimiento y no objeta la tercerización.", "tipo": "presentacion_informativa"}, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 13}
- {"local_id": "e14", "type": "Obligacion", "label": "Certificación del ente supervisor: inclusión en programa de supervisión", "properties": {"descripcion": "La certificación debe indicar que los servicios tercerizados formarán parte del programa normal de supervisión del ente supervisor.", "tipo": "presentacion_informativa"}, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 14}
- {"local_id": "e15", "type": "Obligacion", "label": "Certificación del ente supervisor: cumplimiento LA/FT/FPADM", "properties": {"descripcion": "La certificación debe indicar que el ente supervisor se encuentra sujeto a principios, estándares o normas de prevención del Lavado de Activos, la Financiación del Terrorismo y la Financiación de la Proliferación de Armas de Destrucción Masiva (LA/FT/FPADM) internacionalmente aceptados, entre otros los difundidos por el FATF-GAFI y el Comité de Supervis
- {"local_id": "e16", "type": "Obligacion", "label": "Certificación del ente supervisor: adhesión a principios de supervisión", "properties": {"descripcion": "La certificación debe indicar que el ente supervisor adhiere a los Principios básicos para una supervisión bancaria eficaz divulgados por el Comité de Supervisión Bancaria de Basilea, y aplica supervisión consolidada asumiendo la vigilancia de la liquidez y solvencia, así como la evaluación y el control de los riesgos y situaciones patrimoni
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e3", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e4", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- relación: {"source": "e5", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- relación: {"source": "e6", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- relación: {"source": "e7", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- relación: {"source": "e8", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 7}
- relación: {"source": "e9", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 8}
- relación: {"source": "e10", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 9}
- relación: {"source": "e11", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 10}
- relación: {"source": "e12", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 11}
- relación: {"source": "e13", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 12}
- relación: {"source": "e14", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 13}
- relación: {"source": "e15", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 14}
- relación: {"source": "e16", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 15}
- relación: {"source": "e1", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_sujeto_regulado", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 16}
- relación: {"source": "e2", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_sujeto_regulado", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 17}
- relación: {"source": "e3", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_sujeto_regulado", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 18}
- relación: {"source": "e4", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_sujeto_regulado", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 19}
- relación: {"source": "e5", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_sujeto_regulado", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 20}
- relación: {"source": "e6", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_sujeto_regulado", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 21}
- relación: {"source": "e7", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_sujeto_regulado", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 22}
- relación: {"source": "e8", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_sujeto_regulado", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 23}
- relación: {"source": "e9", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_sujeto_regulado", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 24}
- relación: {"source": "e10", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_sujeto_regulado", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 25}
- relación: {"source": "e11", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_sujeto_regulado", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 26}
- relación: {"source": "e13", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_sujeto_regulado", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 27}
- relación: {"source": "e14", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_sujeto_regulado", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 28}
- relación: {"source": "e15", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_sujeto_regulado", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 29}
- relación: {"source": "e16", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_sujeto_regulado", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 30}
- relación: {"source": "e12", "target": "e13", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 31}
- relación: {"source": "e12", "target": "e14", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 32}
- relación: {"source": "e12", "target": "e15", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 33}
- relación: {"source": "e12", "target": "e16", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "rmgcti", "archivo": "rmgcti.pdf", "punto": "10.1", "rol_documental": "punto_propio"}, "indice_crudo": 34}

## 16. `ratio::2.2.6` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 11):

```
[encabezado | punto S2]
Sección 2. Fondo de activos líquidos de alta calidad.
[encabezado | punto 2.2]
2.2. Activos comprendidos.
[texto propio | punto 2.2.6]
2.2.6. Títulos de deuda emitidos por otros soberanos (o sus bancos centrales) en sus respecti-
vas monedas cuando la entidad a través de sus subsidiarias o sucursales asuma riesgo
de liquidez en esas jurisdicciones y en esas monedas y los títulos cumplan con las con-
diciones previstas en los acápites ii) a iv) del punto 2.2.5. Se computarán hasta el impor-
te de las salidas de efectivo netas en esas monedas y jurisdicciones.
```

Versión: primer intento (cola). Entidades 5, relaciones 7.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Ratio de Fondeo Neto Estable", "properties": {}, "provenance": {"to": "ratio", "archivo": "ratio.pdf", "punto": "2.2.6", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Operacion", "label": "Emisión de títulos de deuda por soberanos", "properties": {"tipo": "Emisión de títulos de deuda", "descripcion": "Títulos de deuda emitidos por otros soberanos o sus bancos centrales en sus respectivas monedas, cuando la entidad a través de sus subsidiarias o sucursales asuma riesgo de liquidez en esas jurisdicciones y en esas monedas."}, "provenance": {"to": "ratio", "archivo": "ratio.pdf", "punto": "2.2.6", "rol_documental": "punto_propio"}, "i
- {"local_id": "e2", "type": "Condicion", "label": "Riesgo de liquidez en jurisdicciones y monedas específicas", "properties": {"descripcion": "La entidad debe asumir riesgo de liquidez en las jurisdicciones y monedas de los títulos a través de sus subsidiarias o sucursales."}, "provenance": {"to": "ratio", "archivo": "ratio.pdf", "punto": "2.2.6", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- {"local_id": "e3", "type": "Condicion", "label": "Cumplimiento de condiciones del punto 2.2.5", "properties": {"descripcion": "Los títulos deben cumplir con las condiciones previstas en los acápites ii) a iv) del punto 2.2.5."}, "provenance": {"to": "ratio", "archivo": "ratio.pdf", "punto": "2.2.6", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- {"local_id": "e4", "type": "Restriccion", "label": "Límite de cómputo — salidas de efectivo netas", "properties": {"tipo": "limite_cuantitativo", "descripcion": "Los títulos se computarán hasta el importe de las salidas de efectivo netas en esas monedas y jurisdicciones.", "umbrales": "hasta el importe de las salidas de efectivo netas en esas monedas y jurisdicciones"}, "provenance": {"to": "ratio", "archivo": "ratio.pdf", "punto": "2.2.6", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ratio", "archivo": "ratio.pdf", "punto": "2.2.6", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ratio", "archivo": "ratio.pdf", "punto": "2.2.6", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e3", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ratio", "archivo": "ratio.pdf", "punto": "2.2.6", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e4", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ratio", "archivo": "ratio.pdf", "punto": "2.2.6", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- relación: {"source": "e2", "target": "e1", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ratio", "archivo": "ratio.pdf", "punto": "2.2.6", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- relación: {"source": "e3", "target": "e1", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ratio", "archivo": "ratio.pdf", "punto": "2.2.6", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- relación: {"source": "e4", "target": "e1", "predicate": "limita", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ratio", "archivo": "ratio.pdf", "punto": "2.2.6", "rol_documental": "punto_propio"}, "indice_crudo": 6}

## 17. `ratiofn::5.1.6` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 19):

```
[encabezado | punto S5]
Sección 5. Factores.
[encabezado | punto 5.1]
5.1. Factores de Fondeo Estable Disponible (FED). Factor
[texto propio | punto 5.1.6]
5.1.6. Depósitos a la vista y depósitos a plazo no comprendidos en el punto 90 %
2.3.2. con vencimiento residual inferior a un año, realizados por clientes
minoristas y MiPyMEs (punto 2.3.3.1.).
```

Versión: primer intento (cola). Entidades 2, relaciones 1.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Ratio de Fondeo Neto Estable", "properties": {}, "provenance": {"to": "ratiofn", "archivo": "ratiofn.pdf", "punto": "5.1.6", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Definicion", "label": "FED — Depósitos a la vista y plazo minoristas/MiPyMEs", "properties": {"termino": "Depósitos a la vista y depósitos a plazo no comprendidos en el punto 90 %", "descripcion": "Depósitos a la vista y depósitos a plazo con vencimiento residual inferior a un año, realizados por clientes minoristas y MiPyMEs, no comprendidos en el punto 2.3.2."}, "provenance": {"to": "ratiofn", "archivo": "ratiofn.pdf", "punto": "5.1.6", "rol_documental": "punto_prop
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ratiofn", "archivo": "ratiofn.pdf", "punto": "5.1.6", "rol_documental": "punto_propio"}, "indice_crudo": 0}

## 18. `snp_cec::4.4.1` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 7):

```
[encabezado | punto S4]
Sección 4. Requisitos para su autorización
[intro | punto 4.4]
4.4. Las autorizaciones que se otorguen para el funcionamiento de las cámaras quedarán sujetas
a la homologación técnica que deberá expedir el BCRA y, además, condicionadas al cumpli-
miento, dentro del plazo que se fije para el inicio de sus actividades, de las siguientes exigen-
cias:
[texto propio | punto 4.4.1]
4.4.1. Remisión a la SEFyC de la nómina de las autoridades designadas por la asamblea
constitutiva y de los gerentes, acompañada de los datos a que se refieren los puntos
4.1.6. y 4.1.7., salvo que ellos ya se encontraren en su poder, y nombre del auditor ex-
terno designado.
```

Versión: primer intento (cola). Entidades 6, relaciones 8.
- {"local_id": "to", "type": "TextoOrdenado", "label": "SNP - Cámaras electrónicas de compensación", "properties": {}, "provenance": {"to": "snp_cec", "archivo": "snp_cec.pdf", "punto": "4.4.1", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Operacion", "label": "Remisión de nómina de autoridades a la SEFyC", "properties": {"tipo": "presentación informativa", "descripcion": "Remisión a la SEFyC de la nómina de las autoridades designadas por la asamblea constitutiva y de los gerentes, con los datos de los puntos 4.1.6 y 4.1.7 (salvo si ya están en poder de la SEFyC), e inclusión del nombre del auditor externo designado"}, "provenance": {"to": "snp_cec", "archivo": "snp_cec.pdf", "punto": "4.4.1", "rol_docu
- {"local_id": "e2", "type": "Obligacion", "label": "Presentar nómina de autoridades y auditor a la SEFyC", "properties": {"tipo": "presentacion_informativa", "descripcion": "Deber de remitir a la SEFyC la nómina de las autoridades designadas por la asamblea constitutiva y de los gerentes, acompañada de los datos referidos en los puntos 4.1.6 y 4.1.7 (salvo que ya se encuentren en poder de la SEFyC), y el nombre del auditor externo designado"}, "provenance": {"to": "snp_cec", "archivo": "snp_cec.p
- {"local_id": "e3", "type": "Excepcion", "label": "Excepción — datos ya en poder de la SEFyC", "properties": {"descripcion": "No es necesario acompañar los datos de los puntos 4.1.6 y 4.1.7 si ya se encuentran en poder de la SEFyC"}, "provenance": {"to": "snp_cec", "archivo": "snp_cec.pdf", "punto": "4.4.1", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- {"local_id": "e4", "type": "Condicion", "label": "Cumplimiento dentro de plazo previo a inicio de actividades", "properties": {"descripcion": "El requisito debe cumplirse dentro del plazo que se fije para el inicio de las actividades de la cámara", "umbrales": "dentro del plazo que se fije para el inicio de sus actividades"}, "provenance": {"to": "snp_cec", "archivo": "snp_cec.pdf", "punto": "4.4.1", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- {"local_id": "e5", "type": "Condicion", "label": "Notificación a la SEFyC con antelación mínima", "properties": {"descripcion": "Todos los requisitos deben quedar cumplimentados con una antelación no menor de 30 días a la fecha prevista para el inicio de actividades, notificando de ello a la SEFyC", "umbrales": "no menor de 30 días"}, "provenance": {"to": "snp_cec", "archivo": "snp_cec.pdf", "punto": "4.4.1", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cec", "archivo": "snp_cec.pdf", "punto": "4.4.1", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e3", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cec", "archivo": "snp_cec.pdf", "punto": "4.4.1", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e4", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cec", "archivo": "snp_cec.pdf", "punto": "4.4.1", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e5", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cec", "archivo": "snp_cec.pdf", "punto": "4.4.1", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- relación: {"source": "e3", "target": "e2", "predicate": "exceptua_obligacion", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cec", "archivo": "snp_cec.pdf", "punto": "4.4.1", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- relación: {"source": "e4", "target": "e2", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cec", "archivo": "snp_cec.pdf", "punto": "4.4.1", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- relación: {"source": "e5", "target": "e2", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cec", "archivo": "snp_cec.pdf", "punto": "4.4.1", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- relación: {"source": "e2", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_camara_electronica_de_compensacion", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cec", "archivo": "snp_cec.pdf", "punto": "4.4.1", "rol_documental": "punto_propio"}, "indice_crudo": 7}

## 19. `ratio::2.2.3` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 10):

```
[encabezado | punto S2]
Sección 2. Fondo de activos líquidos de alta calidad.
[encabezado | punto 2.2]
2.2. Activos comprendidos.
[texto propio | punto 2.2.3]
2.2.3. Títulos públicos nacionales en pesos cuya negociación esté autorizada en el mercado se-
cundario de pases del Mercado Abierto Electrónico (MAE) –tal como en la Rueda REPO–
o en otros mercados secundarios de pases que sean amplios, profundos, activos y poco
concentrados, e instrumentos de regulación monetaria del Banco Central de la República
Argentina en pesos.
```

Versión: primer intento (cola). Entidades 4, relaciones 3.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Ratio de fondeo neto estable", "properties": {}, "provenance": {"to": "ratio", "archivo": "ratio.pdf", "punto": "2.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Definicion", "label": "Títulos públicos nacionales en pesos — FALAC", "properties": {"termino": "Títulos públicos nacionales en pesos", "descripcion": "Títulos públicos nacionales en pesos cuya negociación esté autorizada en el mercado secundario de pases del Mercado Abierto Electrónico (MAE) –tal como en la Rueda REPO– o en otros mercados secundarios de pases que sean amplios, profundos, activos y poco concentrados"}, "provenance": {"to": "ratio", "archivo": "ratio.p
- {"local_id": "e2", "type": "Definicion", "label": "Instrumentos de regulación monetaria del BCRA en pesos — FALAC", "properties": {"termino": "instrumentos de regulación monetaria del Banco Central de la República Argentina en pesos", "descripcion": "Instrumentos de regulación monetaria del Banco Central de la República Argentina en pesos, comprendidos en el fondo de activos líquidos de alta calidad"}, "provenance": {"to": "ratio", "archivo": "ratio.pdf", "punto": "2.2.3", "rol_documental": "pun
- {"local_id": "e3", "type": "Operacion", "label": "Negociación de títulos públicos en MAE o mercados secundarios de pases", "properties": {"tipo": "negociación de títulos", "descripcion": "Negociación de títulos públicos nacionales en pesos autorizada en el mercado secundario de pases del Mercado Abierto Electrónico (MAE), en la Rueda REPO, o en otros mercados secundarios de pases que sean amplios, profundos, activos y poco concentrados"}, "provenance": {"to": "ratio", "archivo": "ratio.pdf", "pu
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ratio", "archivo": "ratio.pdf", "punto": "2.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ratio", "archivo": "ratio.pdf", "punto": "2.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e3", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ratio", "archivo": "ratio.pdf", "punto": "2.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 2}

## 20. `cateloc::Sbloque6` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 10, 11, 12, 13, 14, 15, 16):

```
[encabezado | punto S2]
Sección 2. Cuadro de categorización de localidades.
[encabezado | punto Sbloque2]
CELAS FRENTISTAS DE LA VEREDA
[texto propio | punto Sbloque6]
PRESIDENTE ROQUE SAENZ
III CORDOBA MELO
PEÑA
PRESIDENTE ROQUE SAENZ
III CORDOBA SERRANO
PEÑA
III CORDOBA PUNILLA BARRIO SANTA ISABEL
III CORDOBA PUNILLA COSQUIN
III CORDOBA PUNILLA LA CUMBRE
III CORDOBA RIO CUARTO ALCIRA (EST. GIGENA)
III CORDOBA RIO CUARTO BERROTARAN
III CORDOBA RIO CUARTO CORONEL MOLDES
III CORDOBA RIO CUARTO LAS VERTIENTES
III CORDOBA RIO CUARTO MONTE DE LOS GAUCHOS
III CORDOBA RIO CUARTO SAMPACHO
III CORDOBA RIO CUARTO SAN BASILIO
III CORDOBA RIO CUARTO VICUÑA MACKENNA
III CORDOBA RIO PRIMERO SANTA ROSA DE RIO PRIMERO
III CORDOBA RIO SEGUNDO CALCHIN
III CORDOBA RIO SEGUNDO CARRILOBO
III CORDOBA RIO SEGUNDO COLAZO
III CORDOBA RIO SEGUNDO LAGUNA LARGA
III CORDOBA RIO SEGUNDO LAS JUNTURAS
III CORDOBA RIO SEGUNDO LUQUE
III CORDOBA RIO SEGUNDO MATORRALES
III CORDOBA RIO SEGUNDO PILAR
III CORDOBA RIO SEGUNDO POZO DEL MOLLE
III CORDOBA RIO SEGUNDO VILLA DEL ROSARIO
III CORDOBA SAN ALBERTO MINA CLAVERO
III CORDOBA SAN JUSTO ALTOS DE CHIPION
III CORDOBA SAN JUSTO BALNEARIA
III CORDOBA SAN JUSTO COLONIA MARINA
III CORDOBA SAN JUSTO COLONIA SAN BARTOLOME
III CORDOBA SAN JUSTO DEVOTO
III CORDOBA SAN JUSTO EL ARAÑADO
III CORDOBA SAN JUSTO LA TORDILLA
III CORDOBA SAN JUSTO LAS VARAS
III CORDOBA SAN JUSTO MARULL
III CORDOBA SAN JUSTO SACANTA
III CORDOBA SAN JUSTO SATURNINO MARIA LASPIUR
III CORDOBA SANTA MARIA DESPEÑADEROS
III CORDOBA TERCERO ARRIBA ALMAFUERTE
III CORDOBA TERCERO ARRIBA LAS PERDICES
III CORDOBA TERCERO ARRIBA VILLA ASCASUBI
III CORDOBA UNION CANALS
III CORDOBA UNION CINTRA
III CORDOBA UNION JUSTINIANO POSSE
III CORDOBA UNION PASCANAS
III CORDOBA UNION SAN ANTONIO DE LITIN
III CORDOBA UNION SAN MARCOS
III CORDOBA UNION VIAMONTE
III CORRIENTES BELLA VISTA BELLA VISTA
III CORRIENTES CURUZU CUATIA CURUZU CUATIA
III CORRIENTES ESQUINA ESQUINA
III CORRIENTES ITUZAINGO ITUZAINGO
III CORRIENTES MONTE CASEROS MONTE CASEROS
III CORRIENTES SALADAS SALADAS
III CORRIENTES SANTO TOME GOBERNADOR IGR. VALENTIN VIRASORO
III CORRIENTES SANTO TOME SANTO TOME
III CORRIENTES SAUCE SAUCE
III ENTRE RIOS COLON COLON
III ENTRE RIOS DIAMANTE DIAMANTE
III ENTRE RIOS DIAMANTE GENERAL RAMIREZ
III ENTRE RIOS FEDERACION FEDERACION
III ENTRE RIOS FEDERAL FEDERAL
III ENTRE RIOS FELICIANO SAN JOSE DE FELICIANO
III ENTRE RIOS GUALEGUAYCHU ALDEA SAN ANTONIO
III ENTRE RIOS GUALEGUAYCHU URDINARRAIN
III ENTRE RIOS LA PAZ BOVRIL
III ENTRE RIOS LA PAZ LA PAZ
III ENTRE RIOS NOGOYA LUCAS GONZALEZ
III ENTRE RIOS NOGOYA NOGOYA
III ENTRE RIOS PARANA HERNANDARIAS
III ENTRE RIOS PARANA MARIA GRANDE
III ENTRE RIOS SAN SALVADOR SAN SALVADOR
III ENTRE RIOS TALA ROSARIO DEL TALA
III ENTRE RIOS URUGUAY BASAVILBASO
III ENTRE RIOS VICTORIA VICTORIA
III ENTRE RIOS VILLAGUAY VILLAGUAY
III FORMOSA PILCOMAYO CLORINDA
III FORMOSA PIRANE EL COLORADO
III FORMOSA PIRANE PIRANE
III JUJUY EL CARMEN PERICO
LIBERTADOR GENERAL SAN MARTIN
III JUJUY LEDESMA
(EST. LEDESMA)
III JUJUY SAN PEDRO SAN PEDRO (EST. SAN PEDRO DE JUJUY)
III JUJUY YAVI LA QUIACA
III LA PAMPA ATREUCO DOBLAS
III LA PAMPA ATREUCO MACACHIN
III LA PAMPA ATREUCO MIGUEL RIGLOS
III LA PAMPA CATRILO CATRILO
III LA PAMPA CATRILO LONQUIMAY
III LA PAMPA CHAPALEUFU CEBALLOS
CORONEL HILARIO LAGOS (EST. AGUAS
III LA PAMPA CHAPALEUFU
BUENAS)
III LA PAMPA CHICAL CO ALGARROBO DEL AGUILA
III LA PAMPA CONHELO EDUARDO CASTEX
III LA PAMPA CONHELO MAURICIO MAYER
III LA PAMPA CONHELO MONTE NIEVAS
III LA PAMPA CONHELO WINIFREDA
III LA PAMPA GUATRACHE ALPACHIRI
III LA PAMPA GUATRACHE GENERAL MANUEL J. CAMPOS
III LA PAMPA GUATRACHE GUATRACHE
III LA PAMPA HUCAL JACINTO ARAUZ
III LA PAMPA LIHUEL CALEL CUCHILLO CO
III LA PAMPA LIMAY MAHUIDA LA REFORMA
III LA PAMPA LOVENTUE VICTORICA
III LA PAMPA MARACO AGUSTONI
III LA PAMPA QUEMU QUEMU COLONIA BARON
III LA PAMPA QUEMU QUEMU MIGUEL CANE
III LA PAMPA QUEMU QUEMU VILLA MIRASOL
III LA PAMPA RANCUL CALEUFU
III LA PAMPA RANCUL LA MARUJA
III LA PAMPA RANCUL PARERA
III LA PAMPA REALICO ADOLFO VAN PRAET
III LA PAMPA REALICO ALTA ITALIA
III LA PAMPA REALICO EMBAJADOR MARTINI
III LA PAMPA TRENEL ARATA
III LA PAMPA TRENEL METILEO
III LA PAMPA TRENEL TRENEL
III LA PAMPA UTRACAN ATALIVA ROCA
III LA PAMPA UTRACAN CHACHARRAMENDI
III LA PAMPA UTRACAN COLONIA SANTA MARIA
III LA PAMPA UTRACAN GENERAL ACHA
III LA PAMPA UTRACAN QUEHUE
III LA PAMPA UTRACAN UNANUE
III LA RIOJA ARAUCO AIMOGASTA
III LA RIOJA CHAMICAL CHAMICAL
III LA RIOJA CORONEL FELIPE VARELA VILLA UNION
III LA RIOJA ROSARIO VERA PEÑALOZA CHEPES
III MENDOZA GENERAL ALVEAR GENERAL ALVEAR
III MENDOZA JUNIN JUNIN
III MENDOZA LAS HERAS LAS HERAS
III MENDOZA MALARGÜE MALARGÜE
III MENDOZA RIVADAVIA MEDRANO()
III MENDOZA SAN CARLOS EUGENIO BUSTOS
III MENDOZA SAN CARLOS SAN CARLOS
III MENDOZA TUNUYAN VISTA FLORES
III MISIONES APOSTOLES APOSTOLES
III MISIONES GUARANI SAN VICENTE
III MISIONES IGUAZU PUERTO IGUAZU
III MISIONES LEANDRO N. ALEM LEANDRO N. ALEM
LIBERTADOR GRL. SAN MAR-
III MISIONES PUERTO RICO
TIN
LIBERTADOR GRL. SAN MAR-
III MISIONES RUIZ DE MONTOYA
TIN
III MISIONES MONTECARLO MONTECARLO
III MISIONES OBERA OBERA
III MISIONES SAN IGNACIO JARDIN AMERICA
III MISIONES SAN JAVIER SAN JAVIER
III NEUQUEN CHOS MALAL CHOS MALAL
III NEUQUEN CONFLUENCIA CENTENARIO
III NEUQUEN CONFLUENCIA PLAZA HUINCUL
III NEUQUEN CONFLUENCIA VILLA EL CHOCON
III NEUQUEN PEHUENCHES BUTA RANQUIL
III NEUQUEN PEHUENCHES RINCON DE LOS SAUCES
III RIO NEGRO 25 DE MAYO INGENIERO JACOBACCI
III RIO NEGRO BARILOCHE EL BOLSON
III RIO NEGRO CONESA GENERAL CONESA
III RIO NEGRO GENERAL ROCA CINCO SALTOS
III RIO NEGRO SAN ANTONIO SIERRA GRANDE
III SALTA ANTA JOAQUIN V. GONZALEZ
III SALTA CAFAYATE CAFAYATE
III SALTA GENERAL GÜEMES GENERAL GÜEMES
III SALTA GRL. JOSE DE SAN MARTIN TARTAGAL
III SALTA METAN SAN JOSE DE METAN
III SALTA ORAN SAN RAMON DE LA NUEVA ORAN
III SALTA ROSARIO DE LA FRONTERA ROSARIO DE LA FRONTERA
III SALTA ROSARIO DE LERMA ROSARIO DE LERMA
III SAN JUAN CAUCETE CAUCETE
III SAN JUAN JACHAL SAN JOSE DE JACHAL
III SAN JUAN RAWSON RAWSON
III SAN JUAN SAN MARTIN VILLA SAN MARTIN
III SAN JUAN SARMIENTO COLONIA FISCAL
III SAN JUAN SARMIENTO VILLA MEDIA AGUA
III SAN LUIS CHACABUCO TILISARAO
III SAN LUIS GENERAL PEDERNERA JUSTO DARACT
III SAN LUIS JUNIN MERLO
III SANTA CRUZ CORPEN AIKE PUERTO SANTA CRUZ
III SANTA CRUZ DESEADO CAÑADON SECO
III SANTA CRUZ DESEADO PICO TRUNCADO
III SANTA CRUZ LAGO BUENOS AIRES PERITO MORENO
III SANTA CRUZ MAGALLANES PUERTO SAN JULIAN
III SANTA CRUZ RIO CHICO GOBERNADOR GREGORES
III SANTA FE 9 DE JULIO TOSTADO
III SANTA FE CASEROS BIGAND
III SANTA FE CASEROS CHABAS
III SANTA FE CASTELLANOS BELLA ITALIA
III SANTA FE CASTELLANOS ESTACION CLUCELLAS
III SANTA FE CASTELLANOS HUMBERTO PRIMO
III SANTA FE CASTELLANOS MARIA JUANA
III SANTA FE CASTELLANOS RAMONA
III SANTA FE CASTELLANOS SANTA CLARA DE SAGUIER
III SANTA FE CASTELLANOS VILA
III SANTA FE CONSTITUCION BOMBAL
III SANTA FE CONSTITUCION JUNCAL
III SANTA FE CONSTITUCION MAXIMO PAZ (EST. PAZ)
III SANTA FE CONSTITUCION PAVON ARRIBA
III SANTA FE CONSTITUCION SANTA TERESA
III SANTA FE CONSTITUCION THEOBALD
[TABLA cateloc::tabla002 | página 14 | e0_tablas | posicional]
Fila 1: col1 = CATEGORIA | col2 = PROVINCIA | col3 = DEPARTAMENTO / PARTIDO | col4 = LOCALIDAD
Fila 2: col1 = III III III III III III III III III III III III III III III III III III III III III III III III III III III III III III III III III III III III III III III III III III III III III III III III III III III III III | col2 = SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTIAGO DEL ES- TERO SANTIAGO DEL ES- TERO SANTIAGO DEL ES- TERO TIERRA DEL FUEGO TUCUMAN TUCUMAN TUCUMAN TUCUMAN TUCUMAN TUCUMAN TUCUMAN TUCUMAN | col3 = GENERAL LOPEZ GENERAL LOPEZ GENERAL LOPEZ GENERAL LOPEZ GENERAL LOPEZ GENERAL LOPEZ GENERAL LOPEZ GENERAL LOPEZ GENERAL OBLIGADO IRIONDO IRIONDO IRIONDO LA CAPITAL LAS COLONIAS LAS COLONIAS LAS COLONIAS LAS COLONIAS LAS COLONIAS ROSARIO ROSARIO ROSARIO ROSARIO ROSARIO ROSARIO ROSARIO SAN CRISTOBAL SAN CRISTOBAL SAN CRISTOBAL SAN CRISTOBAL SAN CRISTOBAL SAN JAVIER SAN JERONIMO SAN JERONIMO SAN LORENZO SAN LORENZO SAN LORENZO SAN MARTIN SAN MARTIN SAN MARTIN SAN MARTIN VERA BANDA CHOYA RIVADAVIA RIO GRANDE FAMAILLA JUAN BAUTISTA ALBERDI LEALES LULES MONTEROS RIO CHICO TAFI VIEJO YERBA BUENA | col4 = CARMEN ELORTONDO HUGHES MARIA TERESA SANCTI SPIRITU TEODELINA VILLA CAÑAS WHEELWRIGHT VILLA OCAMPO BUSTINZA CORREA VILLA ELOISA LAGUNA PAIVA FRANCK HUMBOLDT PROGRESO SAN JERONIMO NORTE SARMIENTO ACEBAL ALVAREZ FUNES GRANADERO BAIGORRIA PEREZ PUEBLO URANGA SOLDINI CERES MOISES VILLE SAN CRISTOBAL SAN GUILLERMO VILLA TRINIDAD SAN JAVIER CORONDA MACIEL CAPITAN BERMUDEZ CORONEL ARNOLD PUERTO GENERAL SAN MARTIN CARLOS PELLEGRINI MARIA SUSANA PIAMONTE SAN MARTIN DE LAS ESCOBAS VERA (EST. GOBERNADOR VERA) LA BANDA FRIAS SELVA TOLHUIN FAMAILLA JUAN BAUTISTA ALBERDI SANTA ROSA DE LEALES LULES MONTEROS AGUILARES TAFI VIEJO YERBA BUENA - MARCOS PAZ
Fila 3: col1 = IV IV IV IV | col2 = BUENOS AIRES BUENOS AIRES BUENOS AIRES BUENOS AIRES | col3 = 9 DE JULIO ADOLFO GONZALES CHAVES AZUL AZUL | col4 = VILLA GENERAL FOURNIER (EST. 9 DE JULIO SUD) DE LA GARMA CACHARI CHILLAR
[FIN TABLA cateloc::tabla002]
GENERAL DANIEL CERRI (EST. GENERAL
IV BUENOS AIRES BAHIA BLANCA
CERRI)
IV BUENOS AIRES BENITO JUAREZ BARKER
IV BUENOS AIRES BOLIVAR PIROVANO
IV BUENOS AIRES BRAGADO GENERAL O'BRIEN
IV BUENOS AIRES BRANDSEN JEPPENER
IV BUENOS AIRES CARLOS TEJEDOR TRES ALGARROBOS (EST. CUENCA)
IV BUENOS AIRES CARMEN DE ARECO TRES SARGENTOS
IV BUENOS AIRES CORONEL DORREGO ORIENTE
IV BUENOS AIRES CORONEL PRINGLES INDIO RICO
IV BUENOS AIRES EXALTACION DE LA CRUZ LOS CARDALES
IV BUENOS AIRES FLORENTINO AMEGHINO BLAQUIER
IV BUENOS AIRES GENERAL ALVEAR GENERAL ALVEAR
IV BUENOS AIRES GENERAL GUIDO GENERAL GUIDO
IV BUENOS AIRES GENERAL LAS HERAS GENERAL HORNOS
IV BUENOS AIRES GENERAL LAS HERAS GENERAL LAS HERAS (EST. LAS HERAS)
IV BUENOS AIRES GENERAL PAZ RANCHOS
IV BUENOS AIRES GENERAL PINTO GENERAL PINTO
GERMANIA (EST. MAYOR JOSE ORE-
IV BUENOS AIRES GENERAL PINTO
LLANO)
VILLA FRANCIA (EST. CORONEL GRANA-
IV BUENOS AIRES GENERAL PINTO
DA)
IV BUENOS AIRES GENERAL PUEYRREDON CHAPADMALAL
IV BUENOS AIRES GENERAL VIAMONTE BAIGORRITA
IV BUENOS AIRES GENERAL VILLEGAS BANDERALO
IV BUENOS AIRES GENERAL VILLEGAS CORONEL CHARLONE
IV BUENOS AIRES GUAMINI GUAMINI
IV BUENOS AIRES JUNIN LAPLACETTE
IV BUENOS AIRES LA COSTA LAS TONINAS
IV BUENOS AIRES LA COSTA SAN CLEMENTE DEL TUYU
IV BUENOS AIRES LEANDRO N. ALEM JUAN BAUTISTA ALBERDI (EST. ALBERDI)
IV BUENOS AIRES LEZAMA LEZAMA
IV BUENOS AIRES LINCOLN ARENAZA
IV BUENOS AIRES LINCOLN ROBERTS
IV BUENOS AIRES LUJAN JOSE MARIA JAUREGUI (EST. JAUREGUI)
IV BUENOS AIRES MAR CHIQUITA CORONEL VIDAL
IV BUENOS AIRES MAR CHIQUITA GENERAL PIRAN
IV BUENOS AIRES MAR CHIQUITA SANTA CLARA DEL MAR
IV BUENOS AIRES MONTE HERMOSO MONTE HERMOSO
IV BUENOS AIRES NECOCHEA JUAN N. FERNANDEZ
IV BUENOS AIRES OLAVARRIA HINOJO
IV BUENOS AIRES OLAVARRIA SIERRA CHICA
IV BUENOS AIRES OLAVARRIA SIERRAS BAYAS
IV BUENOS AIRES OLAVARRIA VILLA ALFREDO FORTABAT
IV BUENOS AIRES PATAGONES STROEDER
IV BUENOS AIRES PEHUAJO FRANCISCO MADERO
IV BUENOS AIRES PEHUAJO JUAN JOSE PASO
IV BUENOS AIRES PILA PILA
IV BUENOS AIRES PRESIDENTE PERON PRESIDENTE PERON
IV BUENOS AIRES PUAN VILLA IRIS
IV BUENOS AIRES RAMALLO PEREZ MILLAN
IV BUENOS AIRES RAMALLO RAMALLO
IV BUENOS AIRES RIVADAVIA FORTIN OLAVARRIA
IV BUENOS AIRES RIVADAVIA GONZALEZ MORENO
IV BUENOS AIRES ROJAS LAS CARABELAS
IV BUENOS AIRES ROJAS RAFAEL OBLIGADO
IV BUENOS AIRES SAAVEDRA COLONIA SAN MARTIN
IV BUENOS AIRES SAAVEDRA SAAVEDRA
IV BUENOS AIRES SAN NICOLAS CONESA
IV BUENOS AIRES SAN NICOLAS LA EMILIA
IV BUENOS AIRES SAN VICENTE SAN VICENTE
IV BUENOS AIRES SUIPACHA SUIPACHA
IV BUENOS AIRES TANDIL GARDEY
IV BUENOS AIRES TANDIL MARIA IGNACIA (EST. VELA)
IV BUENOS AIRES TORDILLO GENERAL CONESA
IV BUENOS AIRES TRES ARROYOS CLAROMECO
IV BUENOS AIRES TRES ARROYOS COPETONAS
IV BUENOS AIRES TRES ARROYOS SAN FRANCISCO DE BELLOCQ
IV BUENOS AIRES VILLARINO JUAN COUSTE (EST. ALGARROBO)
IV BUENOS AIRES VILLARINO MEDANOS
IV BUENOS AIRES ZARATE LIMA
IV CATAMARCA ANDALGALA ANDALGALA
IV CATAMARCA BELEN BELEN
IV CATAMARCA BELEN LONDRES
IV CATAMARCA CAPAYAN CHUMBICHA
IV CATAMARCA EL ALTO EL ALTO
IV CATAMARCA LA PAZ ICAÑO
IV CATAMARCA LA PAZ RECREO
IV CATAMARCA POMAN POMAN
IV CATAMARCA POMAN SAUJIL
IV CATAMARCA SANTA MARIA SANTA MARIA
IV CATAMARCA SANTA ROSA LOS ALTOS
IV CATAMARCA TINOGASTA FIAMBALA
IV CATAMARCA TINOGASTA TINOGASTA
IV CATAMARCA VALLE VIEJO LAS TEJAS
IV CATAMARCA VALLE VIEJO SAN ISIDRO
IV CHACO 12 DE OCTUBRE GANCEDO
IV CHACO 12 DE OCTUBRE GENERAL PINEDO
IV CHACO 1º DE MAYO COLONIA BENITEZ
IV CHACO 1º DE MAYO MARGARITA BELEN
IV CHACO 2 DE ABRIL HERMOSO CAMPO
IV CHACO ALMIRANTE BROWN CONCEPCION DEL BERMEJO
IV CHACO ALMIRANTE BROWN LOS FRENTONES
IV CHACO ALMIRANTE BROWN PAMPA DEL INFIERNO
IV CHACO ALMIRANTE BROWN TACO POZO
IV CHACO BERMEJO GENERAL VEDIA
IV CHACO BERMEJO ISLA DEL CERRITO
IV CHACO BERMEJO LAS PALMAS
IV CHACO BERMEJO PUERTO EVA PERON
IV CHACO GENERAL BELGRANO CORZUELA
IV CHACO GENERAL DONOVAN LA ESCONDIDA
IV CHACO GENERAL DONOVAN LA VERDE
IV CHACO GENERAL DONOVAN LAPACHITO
IV CHACO GENERAL DONOVAN MAKALLE
IV CHACO GENERAL GÜEMES EL ESPINILLO
IV CHACO GENERAL GÜEMES EL SAUZALITO
IV CHACO GENERAL GÜEMES FUERTE ESPERANZA
IV CHACO GENERAL GÜEMES MIRAFLORES
IV CHACO GENERAL GÜEMES NUEVA POMPEYA
IV CHACO GENERAL GÜEMES VILLA RIO BERMEJITO
IV CHACO INDEPENDENCIA AVIA TERAI
IV CHACO LIBERTAD PUERTO TIROL
LIBERTADOR GENERAL SAN
IV CHACO CIERVO PETISO
MARTIN
```

Versión: primer intento (cola). Entidades 1, relaciones 0.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Cuadro de categorización de localidades", "properties": {}, "provenance": {"to": "cateloc", "archivo": "cateloc.pdf", "punto": "Sbloque6", "rol_documental": "punto_propio"}, "indice_crudo": 0}

## 21. `tasint::6.2` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 18):

```
[encabezado | punto S6]
Sección 6. Financiaciones otorgadas por “Otros proveedores no financieros de crédito”.
[chapeau_seccion | punto S6]
Las financiaciones otorgadas por otros proveedores no financieros de crédito alcanzados por las
normas sobre “Proveedores no financieros de crédito” –incluyendo las empresas no financieras
emisoras de tarjetas de crédito y/o compra por las financiaciones no incluidas en la Ley de Tarjetas
de Crédito–, excepto que se trate de asociaciones mutuales o cooperativas, serán objeto del si-
guiente tratamiento:
[texto propio | punto 6.2]
6.2. Expresión de las tasas y publicidad.
Serán de aplicación las disposiciones previstas en las Secciones 3. y 4.
```

Versión: primer intento (cola). Entidades 2, relaciones 3.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Tasas de interés", "properties": {}, "provenance": {"to": "tasint", "archivo": "tasint.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Obligacion", "label": "Aplicación disposiciones Secciones 3 y 4", "properties": {"descripcion": "Las disposiciones previstas en las Secciones 3 y 4 serán de aplicación a las financiaciones otorgadas por otros proveedores no financieros de crédito, incluyendo empresas no financieras emisoras de tarjetas de crédito y/o compra por las financiaciones no incluidas en la Ley de Tarjetas de Crédito.", "tipo": "otra"}, "provenance": {"to": "tasint", "archivo": "tasint.pdf", "
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "tasint", "archivo": "tasint.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e1", "target": null, "predicate": "aplica_a", "sujeto_id": null, "sujeto_propuesto": "otros proveedores no financieros de crédito", "sujeto_propuesto_padre_sugerido": "Sujeto_proveedor_no_financiero_de_credito", "provenance": {"to": "tasint", "archivo": "tasint.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e1", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_empresa_no_financiera_emisora_de_tarjetas", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "tasint", "archivo": "tasint.pdf", "punto": "6.2", "rol_documental": "punto_propio"}, "indice_crudo": 2}

## 22. `lavdin::3.2.3` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 6):

```
[encabezado | punto S3]
Sección 3. Efectivización de créditos en cuentas de depósitos.
[encabezado | punto 3.2]
3.2. Tratamiento específico.
[texto propio | punto 3.2.3]
3.2.3. En las cesiones de derechos o de títulos de crédito a favor de las entidades financieras,
sin responsabilidad para el cedente, la acreditación se practicará en una cuenta abierta
a nombre de este último.
```

Versión: primer intento (cola). Entidades 3, relaciones 3.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Texto Ordenado Prevención del Lavado de Activos", "properties": {}, "provenance": {"to": "lavdin", "archivo": "lavdin.pdf", "punto": "3.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Operacion", "label": "Cesión de derechos o títulos de crédito a favor de entidades financieras", "properties": {"tipo": "cesión de derechos o títulos de crédito", "descripcion": "Cesión de derechos o de títulos de crédito a favor de las entidades financieras, sin responsabilidad para el cedente"}, "provenance": {"to": "lavdin", "archivo": "lavdin.pdf", "punto": "3.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- {"local_id": "e2", "type": "Obligacion", "label": "Acreditación en cuenta a nombre del cedente", "properties": {"tipo": "asignacion", "descripcion": "La acreditación de la cesión se practicará en una cuenta abierta a nombre del cedente"}, "provenance": {"to": "lavdin", "archivo": "lavdin.pdf", "punto": "3.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lavdin", "archivo": "lavdin.pdf", "punto": "3.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lavdin", "archivo": "lavdin.pdf", "punto": "3.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e1", "target": "e2", "predicate": "requiere", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lavdin", "archivo": "lavdin.pdf", "punto": "3.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 2}

## 23. `raapal::2.2.3.1` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 12, 13, 14):

```
[encabezado | punto S2]
Sección 2. Medida de la exposición.
[encabezado | punto 2.2]
2.2. Criterios particulares.
[encabezado | punto 2.2.3]
2.2.3. Exposiciones por operaciones de financiación con valores (SFT).
[texto propio | punto 2.2.3.1]
2.2.3.1. Tratamiento general.
Será aplicable en los casos en que la entidad sea parte de la operación.
La medida de la exposición será la suma de los conceptos contemplados en los
acápites i) y ii).
i) Activos SFT brutos reconocidos a efectos contables –esto es sin reconoci-
miento de una compensación contable–, con los ajustes siguientes:
a) se excluirá de la medida de la exposición el valor de los títulos recibidos
en operaciones de SFT, si la entidad los hubiera reconocido en su acti-
vo; y
b) se podrán computar por el neto los saldos en efectivo a cobrar o pagar a
una misma contraparte por las operaciones SFT, si se cumplen las si-
guientes condiciones:
- Las operaciones tienen la misma fecha de liquidación final establecida
de modo explícito. Este tratamiento no será aplicable a las operacio-
nes que no tengan una fecha de finalización explícita aunque cual-
quiera de las partes les pueda poner fin en cualquier momento.
- El derecho a netear el monto debido a la contraparte con el monto a
cobrar sea exigible legalmente en el curso normal de los negocios y
también en caso de impago, insolvencia o quiebra de la contraparte.
- Las partes tengan la voluntad de liquidar las operaciones por su valor
neto o en forma simultánea o las operaciones estén sujetas a un me-
canismo de liquidación que es funcionalmente equivalente a la liquida-
ción neta –esto es, los flujos de efectivo de las operaciones equivalen,
en la práctica, a un único monto neto el día de la liquidación–. Para al-
canzar tal equivalencia, ambas operaciones se deberán liquidar a tra-
vés del mismo sistema y los acuerdos de liquidación deberán prever el
uso de facilidades de liquidez o crédito intradiario que aseguren que la
liquidación de ambas transacciones se habrá efectivizado al final del
día hábil. Además, las cuestiones que puedan surgir con los títulos va-
lores de la SFT no podrán impedir la liquidación de los débitos y crédi-
tos en efectivo. Esta última condición implica que si la liquidación de
los títulos de una operación resultara fallida sólo se podrá demorar la
liquidación del efectivo correspondiente a esa única operación o se
generará una obligación para el mecanismo de liquidación respaldada
por la facilidad de crédito asociada.
Si la falla en la liquidación de los títulos subsistiera al final del plazo
para la liquidación previsto en dicho mecanismo, la operación y su co-
rrespondiente parte en efectivo se deberán segregar del conjunto de
neteo y liquidarse en forma bruta.
Se entenderá que un mecanismo de liquidación cumple con los requi-
sitos si una operación fallida –tanto en lo que respecta a los títulos
como a los débitos o créditos en efectivo– se podrá volver a cursar
hasta tanto se logre concluir la liquidación.
En el caso de los activos SFT compensados mediante una QCCP, los acti-
vos SFT brutos reconocidos a efectos contables se reemplazarán por la ex-
posición contractual final –esto es, la exposición a la QCCP luego de efec-
tuado el proceso de novación–. Sin embargo, sólo se podrá netear el efecti-
vo a cobrar y a pagar a la QCCP si se cumple con lo previsto en este acápi-
te; todo otro neteo permitido por la QCCP no será admisible a los efectos del
ratio de apalancamiento.
ii) Riesgo de crédito de contraparte (CCR).
Será la exposición corriente, a la que no se adicionará la EPF y se compu-
tará conforme a lo siguiente:
a) Bajo un acuerdo marco de neteo (MNA) que califique en los términos del
punto 5.3.2.5. del TO sobre Capitales Mínimos de las Entidades Finan-
cieras.
La exposición corriente (E*) será el mayor entre cero y el valor razonable
de los títulos y el efectivo prestados a la contraparte en todas las opera-
ciones incluidas en el MNA (ΣE) menos el valor razonable del efectivo y
i
los títulos recibidos de la contraparte (ΣC), conforme a la siguiente ex-
i
presión:
E* = máx. {0; [ΣE – ΣC]}
i i
b) Sin MNA que califique. La exposición corriente con cada contraparte se
calculará para cada operación i en forma individual, como si fuera un
conjunto de neteo en sí misma, conforme a la siguiente expresión:
E* = máx. {0; [E – C]}
i i i
E* será igual a 0 si:
i
- E es efectivo prestado a la contraparte.
i
- La operación se trata como si constituyera un conjunto de neteo.
- El efectivo a recibir no es elegible para el tratamiento en términos netos
previsto en el acápite i) de este punto.
A los efectos del presente acápite ii), el término “contraparte” incluye no sólo
a la contraparte en una operación bilateral sino también al agente encargado
de recibir el colateral en depósito en una operación de pase tripartita y de
administrarlo. Los títulos depositados con estos agentes serán parte de E
(valor total de los títulos y el efectivo prestados a la contraparte) por hasta el
importe efectivamente prestado a la contraparte en la operación de pase. El
colateral excedente depositado con el agente tripartito y que no fuera pres-
tado podrá ser excluido.
Cuando desde un punto de vista contable correspondiera no registrar un títu-
lo valor dado en préstamo mediante una SFT, la SFT igualmente se tratará
como una operación de financiación a los efectos de calcular la medida de la
exposición; esto es, se deberán incluir los correspondientes montos compu-
tados conforme a los acápites i) y ii).
```

Versión: primer intento (cola). Entidades 21, relaciones 32.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Texto Ordenado de Apalancamiento", "properties": {}, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "c1", "type": "Condicion", "label": "Entidad sea parte de la operación SFT", "properties": {"descripcion": "La medida de la exposición es aplicable cuando la entidad es parte de la operación de financiación con valores."}, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- {"local_id": "op1", "type": "Operacion", "label": "Medida de exposición SFT — suma de activos brutos y CCR", "properties": {"tipo": "Cálculo de exposición en operaciones de financiación con valores", "descripcion": "La medida de la exposición en operaciones SFT se calcula como la suma de: i) activos SFT brutos reconocidos contablemente con ajustes especificados, y ii) riesgo de crédito de contraparte (CCR)."}, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_docum
- {"local_id": "op2", "type": "Operacion", "label": "Activos SFT brutos reconocidos contablemente", "properties": {"tipo": "Reconocimiento contable de activos SFT", "descripcion": "Activos de financiación con valores reconocidos a efectos contables sin reconocimiento de compensación contable, sujetos a los ajustes especificados en los acápites a) y b)."}, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- {"local_id": "r1", "type": "Restriccion", "label": "Exclusión títulos recibidos en SFT del activo", "properties": {"tipo": "limite_cualitativo", "descripcion": "Se excluye de la medida de exposición el valor de títulos recibidos en operaciones SFT cuando la entidad los ha reconocido en su activo."}, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- {"local_id": "p1", "type": "Potestad", "label": "Computar por neto saldos en efectivo SFT", "properties": {"descripcion": "Las entidades pueden computar por el neto los saldos en efectivo a cobrar o pagar a una misma contraparte en operaciones SFT, sujeto al cumplimiento de condiciones específicas sobre fecha de liquidación, exigibilidad legal del neteo, y mecanismo de liquidación equivalente a liquidación neta."}, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_
- {"local_id": "c2", "type": "Condicion", "label": "Misma fecha de liquidación final explícita", "properties": {"descripcion": "Las operaciones SFT deben tener la misma fecha de liquidación final establecida explícitamente. No aplica a operaciones sin fecha de finalización explícita, aunque cualquiera de las partes pueda ponerles fin en cualquier momento."}, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- {"local_id": "c3", "type": "Condicion", "label": "Derecho a netear exigible legalmente", "properties": {"descripcion": "El derecho a netear montos debe ser exigible legalmente tanto en el curso normal de los negocios como en caso de impago, insolvencia o quiebra de la contraparte."}, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 7}
- {"local_id": "c4", "type": "Condicion", "label": "Voluntad de liquidar por valor neto o mecanismo equivalente", "properties": {"descripcion": "Las partes deben tener voluntad de liquidar por valor neto, en forma simultánea, o las operaciones deben estar sujetas a un mecanismo de liquidación funcionalmente equivalente a liquidación neta, con requisitos específicos de sistema de liquidación, facilidades de liquidez intradiaria, y segregación en caso de falla de títulos."}, "provenance": {"to": "ra
- {"local_id": "op3", "type": "Operacion", "label": "Riesgo de crédito de contraparte (CCR) en SFT", "properties": {"tipo": "Cálculo de riesgo de crédito de contraparte", "descripcion": "El riesgo de crédito de contraparte (CCR) se calcula como la exposición corriente sin adición de EPF, conforme a dos métodos: bajo acuerdo marco de neteo (MNA) calificado o sin MNA calificado, con fórmulas específicas para cada caso."}, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "r
- {"local_id": "r2", "type": "Restriccion", "label": "No adición de EPF a exposición corriente CCR", "properties": {"tipo": "limite_cualitativo", "descripcion": "La exposición corriente para el cálculo de CCR no incluye la adición de EPF (Exposición Potencial Futura)."}, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 10}
- {"local_id": "c5", "type": "Condicion", "label": "MNA que califique según Capitales Mínimos", "properties": {"descripcion": "El cálculo de exposición corriente bajo MNA requiere que el acuerdo califique conforme a lo establecido en el punto 5.3.2.5 del Texto Ordenado sobre Capitales Mínimos de las Entidades Financieras."}, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 11}
- {"local_id": "op4", "type": "Operacion", "label": "Cálculo exposición corriente bajo MNA calificado", "properties": {"tipo": "Cálculo de exposición corriente", "descripcion": "Bajo MNA calificado, la exposición corriente (E*) es el máximo entre cero y la diferencia entre el valor razonable de títulos y efectivo prestados (ΣE) menos el valor razonable de títulos y efectivo recibidos (ΣC)."}, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propi
- {"local_id": "op5", "type": "Operacion", "label": "Cálculo exposición corriente sin MNA calificado", "properties": {"tipo": "Cálculo de exposición corriente", "descripcion": "Sin MNA calificado, la exposición corriente se calcula para cada operación de forma individual como si fuera un conjunto de neteo en sí misma, conforme a la fórmula E* = máx. {0; [E – C]}."}, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 13}
- {"local_id": "c6", "type": "Condicion", "label": "E* igual a cero — efectivo prestado", "properties": {"descripcion": "La exposición corriente (E*) es igual a cero cuando E representa efectivo prestado a la contraparte."}, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 14}
- {"local_id": "c7", "type": "Condicion", "label": "E* igual a cero — operación como conjunto de neteo", "properties": {"descripcion": "La exposición corriente (E*) es igual a cero cuando la operación se trata como si constituyera un conjunto de neteo en sí misma."}, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 15}
- {"local_id": "c8", "type": "Condicion", "label": "E* igual a cero — efectivo a recibir no elegible", "properties": {"descripcion": "La exposición corriente (E*) es igual a cero cuando el efectivo a recibir no es elegible para el tratamiento en términos netos del acápite i)."}, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 16}
- {"local_id": "d1", "type": "Definicion", "label": "Contraparte en operaciones SFT", "properties": {"termino": "contraparte", "descripcion": "En operaciones SFT, contraparte incluye tanto la contraparte en operación bilateral como el agente encargado de recibir y administrar colateral en depósito en operación de pase tripartita."}, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 17}
- {"local_id": "op6", "type": "Operacion", "label": "Inclusión títulos depositados con agente tripartito en E", "properties": {"tipo": "Cálculo de exposición", "descripcion": "Los títulos depositados con agentes tripartitos se incluyen en E (valor total de títulos y efectivo prestados) hasta el importe efectivamente prestado a la contraparte en la operación de pase."}, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 18}
- {"local_id": "p2", "type": "Potestad", "label": "Exclusión colateral excedente depositado con agente tripartito", "properties": {"descripcion": "El colateral excedente depositado con agente tripartito que no fue prestado puede ser excluido de la medida de exposición."}, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 19}
- {"local_id": "ob1", "type": "Obligacion", "label": "Tratamiento SFT como operación de financiación", "properties": {"tipo": "otra", "descripcion": "Cuando contablemente no se registre un título valor en préstamo mediante SFT, la operación debe tratarse como operación de financiación a efectos de cálculo de exposición, incluyendo montos conforme a acápites i) y ii)."}, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 20
- relación: {"source": "c1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "op1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "op2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "r1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- relación: {"source": "p1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- relación: {"source": "c2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- relación: {"source": "c3", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- relación: {"source": "c4", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 7}
- relación: {"source": "op3", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 8}
- relación: {"source": "r2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 9}
- relación: {"source": "c5", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 10}
- relación: {"source": "op4", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 11}
- relación: {"source": "op5", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 12}
- relación: {"source": "c6", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 13}
- relación: {"source": "c7", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 14}
- relación: {"source": "c8", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 15}
- relación: {"source": "d1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 16}
- relación: {"source": "op6", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 17}
- relación: {"source": "p2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 18}
- relación: {"source": "ob1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 19}
- relación: {"source": "c1", "target": "op1", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 20}
- relación: {"source": "c2", "target": "p1", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 21}
- relación: {"source": "c3", "target": "p1", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 22}
- relación: {"source": "c4", "target": "p1", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 23}
- relación: {"source": "c5", "target": "op4", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 24}
- relación: {"source": "c6", "target": "op5", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 25}
- relación: {"source": "c7", "target": "op5", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 26}
- relación: {"source": "c8", "target": "op5", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 27}
- relación: {"source": "op1", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 28}
- relación: {"source": "r1", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 29}
- relación: {"source": "p1", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 30}
- relación: {"source": "ob1", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 31}

## 24. `adfsp::1.2.2.1` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 5):

```
[encabezado | punto S1]
Sección 1. Aspectos generales.
[encabezado | punto 1.2]
1.2. Proyectos a financiar.
[encabezado | punto 1.2.2]
1.2.2. Destinos de los fondos.
[texto propio | punto 1.2.2.1]
1.2.2.1. Proyectos de inversión.
Las entidades podrán aplicar hasta el 30% del importe total a financiar de cada
proyecto, a anticipos de inversiones realizados por el cliente -por cuenta y riesgo
de éste-, en el plazo que media entre la fecha de aprobación del proyecto por
parte de la Unidad y la fecha del primer desembolso de fondos por parte de la
entidad financiera.
Los fondos no podrán destinarse a la adquisición de una empresa en marcha o
de tierras, o a la financiación de capital de trabajo, excepto en este último caso
por lo previsto en el punto 1.2.2.2.
```

Versión: primer intento (cola). Entidades 7, relaciones 14.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Adelantos a Entidades Financieras", "properties": {}, "provenance": {"to": "adfsp", "archivo": "adfsp.pdf", "punto": "1.2.2.1", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Operacion", "label": "Anticipos de inversiones — hasta 30%", "properties": {"tipo": "Anticipo de inversión", "descripcion": "Aplicación de hasta el 30% del importe total a financiar de cada proyecto a anticipos de inversiones realizados por el cliente, por cuenta y riesgo del cliente, en el plazo entre la aprobación del proyecto por la Unidad y el primer desembolso de fondos por la entidad financiera."}, "provenance": {"to": "adfsp", "archivo": "adfsp.pdf", "punto": "
- {"local_id": "e2", "type": "Restriccion", "label": "Prohibición — adquisición de empresa o tierras", "properties": {"tipo": "prohibicion", "descripcion": "Los fondos no podrán destinarse a la adquisición de una empresa en marcha o de tierras."}, "provenance": {"to": "adfsp", "archivo": "adfsp.pdf", "punto": "1.2.2.1", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- {"local_id": "e3", "type": "Restriccion", "label": "Prohibición — financiación de capital de trabajo", "properties": {"tipo": "prohibicion", "descripcion": "Los fondos no podrán destinarse a la financiación de capital de trabajo, excepto por lo previsto en el punto 1.2.2.2."}, "provenance": {"to": "adfsp", "archivo": "adfsp.pdf", "punto": "1.2.2.1", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- {"local_id": "e4", "type": "Restriccion", "label": "Prohibición — refinanciación de asistencias previas", "properties": {"tipo": "prohibicion", "descripcion": "Las financiaciones no podrán aplicarse a la refinanciación de asistencias previamente otorgadas por la entidad."}, "provenance": {"to": "adfsp", "archivo": "adfsp.pdf", "punto": "1.2.2.1", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- {"local_id": "e5", "type": "Condicion", "label": "Plazo — entre aprobación y primer desembolso", "properties": {"descripcion": "Los anticipos de inversión deben realizarse en el plazo que media entre la aprobación del proyecto por la Unidad y el primer desembolso de fondos por la entidad financiera.", "umbrales": "en el plazo que media entre la fecha de aprobación del proyecto por parte de la Unidad y la fecha del primer desembolso de fondos por parte de la entidad financiera"}, "provenance": {"
- {"local_id": "e6", "type": "Excepcion", "label": "Excepción — capital de trabajo en punto 1.2.2.2", "properties": {"descripcion": "La prohibición de financiar capital de trabajo no aplica cuando se cumpla lo previsto en el punto 1.2.2.2."}, "provenance": {"to": "adfsp", "archivo": "adfsp.pdf", "punto": "1.2.2.1", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "adfsp", "archivo": "adfsp.pdf", "punto": "1.2.2.1", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "adfsp", "archivo": "adfsp.pdf", "punto": "1.2.2.1", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e3", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "adfsp", "archivo": "adfsp.pdf", "punto": "1.2.2.1", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e4", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "adfsp", "archivo": "adfsp.pdf", "punto": "1.2.2.1", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- relación: {"source": "e5", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "adfsp", "archivo": "adfsp.pdf", "punto": "1.2.2.1", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- relación: {"source": "e6", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "adfsp", "archivo": "adfsp.pdf", "punto": "1.2.2.1", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- relación: {"source": "e1", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "adfsp", "archivo": "adfsp.pdf", "punto": "1.2.2.1", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- relación: {"source": "e2", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "adfsp", "archivo": "adfsp.pdf", "punto": "1.2.2.1", "rol_documental": "punto_propio"}, "indice_crudo": 7}
- relación: {"source": "e3", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "adfsp", "archivo": "adfsp.pdf", "punto": "1.2.2.1", "rol_documental": "punto_propio"}, "indice_crudo": 8}
- relación: {"source": "e4", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "adfsp", "archivo": "adfsp.pdf", "punto": "1.2.2.1", "rol_documental": "punto_propio"}, "indice_crudo": 9}
- relación: {"source": "e5", "target": "e1", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "adfsp", "archivo": "adfsp.pdf", "punto": "1.2.2.1", "rol_documental": "punto_propio"}, "indice_crudo": 10}
- relación: {"source": "e6", "target": "e3", "predicate": "exceptua", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "adfsp", "archivo": "adfsp.pdf", "punto": "1.2.2.1", "rol_documental": "punto_propio"}, "indice_crudo": 11}
- relación: {"source": "e2", "target": "e1", "predicate": "prohibe", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "adfsp", "archivo": "adfsp.pdf", "punto": "1.2.2.1", "rol_documental": "punto_propio"}, "indice_crudo": 12}
- relación: {"source": "e4", "target": "e1", "predicate": "prohibe", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "adfsp", "archivo": "adfsp.pdf", "punto": "1.2.2.1", "rol_documental": "punto_propio"}, "indice_crudo": 13}

## 25. `gescre::1.6.2` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 19):

```
[encabezado | punto S1]
Sección 1. Requisitos para el otorgamiento de financiaciones.
[encabezado | punto 1.6]
1.6. Operaciones por cuenta y orden de la casa matriz.
[intro | punto 1.6]
Se encuentran excluidas de los alcances de las disposiciones de esta sección, los clientes que
sólo reciban financiaciones y avales, fianzas y otras responsabilidades otorgados por sucursa-
les y subsidiarias locales de entidades financieras del exterior, por cuenta y orden de su casa
matriz o sus sucursales en otros países o de la entidad controlante, siempre que se observen
los siguientes requisitos:
[texto propio | punto 1.6.2]
1.6.2. La entidad deberá cumplir con lo previsto en el punto 3.1. de las normas sobre “Evalua-
ciones crediticias”, requiriendo a ese efecto calificación internacional de riesgo compren-
dida en la categoría “investment grade”.
```

Versión: primer intento (cola). Entidades 4, relaciones 4.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Gestión de crédito", "properties": {}, "provenance": {"to": "gescre", "archivo": "gescre.pdf", "punto": "1.6.2", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Operacion", "label": "Evaluación crediticia — calificación internacional", "properties": {"tipo": "Evaluación crediticia", "descripcion": "Obtención de calificación internacional de riesgo comprendida en la categoría investment grade, conforme a lo previsto en el punto 3.1. de las normas sobre Evaluaciones crediticias."}, "provenance": {"to": "gescre", "archivo": "gescre.pdf", "punto": "1.6.2", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- {"local_id": "e2", "type": "Obligacion", "label": "Cumplimiento normas evaluaciones crediticias", "properties": {"tipo": "otra", "descripcion": "La entidad deberá cumplir con lo previsto en el punto 3.1. de las normas sobre Evaluaciones crediticias, requiriendo calificación internacional de riesgo comprendida en la categoría investment grade."}, "provenance": {"to": "gescre", "archivo": "gescre.pdf", "punto": "1.6.2", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- {"local_id": "e3", "type": "Condicion", "label": "Operaciones por cuenta y orden de casa matriz", "properties": {"descripcion": "Las operaciones de financiaciones y avales, fianzas y otras responsabilidades otorgados por sucursales y subsidiarias locales de entidades financieras del exterior, por cuenta y orden de su casa matriz o sus sucursales en otros países o de la entidad controlante, están sujetas al cumplimiento de requisitos específicos, entre los cuales se encuentra el de cumplir con lo
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "gescre", "archivo": "gescre.pdf", "punto": "1.6.2", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e3", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "gescre", "archivo": "gescre.pdf", "punto": "1.6.2", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e2", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "gescre", "archivo": "gescre.pdf", "punto": "1.6.2", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e1", "target": "e2", "predicate": "requiere", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "gescre", "archivo": "gescre.pdf", "punto": "1.6.2", "rol_documental": "punto_propio"}, "indice_crudo": 4}

## 26. `raapal::2.2.4.10` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 16, 17):

```
[encabezado | punto S2]
Sección 2. Medida de la exposición.
[encabezado | punto 2.2]
2.2. Criterios particulares.
[encabezado | punto 2.2.4]
2.2.4. Exposiciones fuera de balance.
[intro | punto 2.2.4]
Las exposiciones fuera de balance a computar son tanto aquellas consideradas para el
cálculo de la exigencia de capital por riesgo de crédito –incluso las originadas en las titu-
lizaciones– como las que se definen especialmente para la determinación del ratio de
apalancamiento.
Las exposiciones por derivados reciben el tratamiento detallado en el punto 2.2.2., por lo
tanto no se computarán como exposición fuera de balance.
Para determinar la exposición, las partidas fuera de balance se convertirán en exposicio-
nes crediticias multiplicando los montos comprometidos y no utilizados por el correspon-
diente factor de conversión crediticia (CCF), conforme a lo previsto en este punto. A este
efecto, se entiende por compromiso al acuerdo contractual aceptado por el cliente que
obliga a la entidad financiera a otorgar créditos, comprar activos o emitir algún otro tipo
de sustituto crediticio.
Podrá deducirse de la exposición crediticia equivalente –esto es, de la exposición luego
de aplicar el CCF– las previsiones generales y específicas que se deducen del capital de
nivel uno, no pudiendo el monto resultante para esas exposiciones ser menor que cero.
Los factores CCF –expresados en %– serán los siguientes:
[texto propio | punto 2.2.4.10]
2.2.4.10. Exposiciones fuera de balance vinculadas con titulizaciones.
i) Facilidades que no son coberturas de riesgo de crédito.
100
ii) Si fuese establecido de forma contractual que la entidad financiera
que actúa como agente de pago y adelanta fondos para asegurar un
flujo continuo de pagos hacia los inversores –en la medida que pueda
cancelar discrecional y unilateralmente esta facilidad– tiene derecho
al reembolso completo del adelanto otorgado y ese derecho tiene pre-
lación frente a cualquier otro derecho sobre los flujos generados por
las exposiciones subyacentes, podrá aplicar a la parte de los antici-
pos de efectivo o facilidades de liquidez que se estima no será utili-
zada el CCF previsto para los compromisos cancelables incondicio-
nalmente.
A ese efecto, las entidades financieras podrán computar como parte
no utilizada de cada contrato a la menor proporción no utilizada que
resulte del historial de utilización de posiciones de titulización simila-
res durante los últimos 7 años. La entidad financiera deberá demos-
trar que realiza un seguimiento activo de la situación financiera de la
titulización y que sus sistemas de control interno permiten cancelar la
línea ante cualquier muestra de deterioro de la solvencia del progra-
ma. Además, deberá fundamentar los criterios que sustentan su ex-
pectativa de que la parte utilizada de cada una de las facilidades no
excederá de la máxima proporción que resulta de sus registros, con-
siderando para ello todos los factores determinantes y toda la infor-
mación pertinente. La estimación de la máxima proporción utilizada
se deberá revisar con periodicidad anual o con mayor frecuencia,
cuando disponga de nueva información relevante. Todo lo que exce-
da de la proporción que se estima no será utilizada recibirá un CCF
del 100 %.
```

Versión: primer intento (cola). Entidades 10, relaciones 16.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Texto Ordenado Raapal", "properties": {}, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.4.10", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Operacion", "label": "Facilidades que no son coberturas de riesgo de crédito", "properties": {"tipo": "facilidad de liquidez", "descripcion": "Facilidades vinculadas con titulizaciones que no constituyen coberturas de riesgo de crédito, sujetas a un factor de conversión crediticia del 100%."}, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.4.10", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- {"local_id": "e2", "type": "Operacion", "label": "Adelanto de fondos por agente de pago en titulizaciones", "properties": {"tipo": "adelanto de fondos", "descripcion": "Adelanto de fondos por parte de la entidad financiera que actúa como agente de pago para asegurar un flujo continuo de pagos hacia los inversores en operaciones de titulización."}, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.4.10", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- {"local_id": "e3", "type": "Condicion", "label": "Derecho de reembolso completo y prelación contractual", "properties": {"descripcion": "Condición para aplicar el CCF de compromisos cancelables incondicionalmente: que conste contractualmente que la entidad tiene derecho al reembolso completo del adelanto y que ese derecho tiene prelación sobre otros derechos sobre los flujos subyacentes."}, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.4.10", "rol_documental": "punto_prop
- {"local_id": "e4", "type": "Potestad", "label": "Aplicar CCF reducido a parte no utilizada de anticipos", "properties": {"descripcion": "Facultad de la entidad financiera de aplicar el factor de conversión crediticia para compromisos cancelables incondicionalmente a la parte de los anticipos de efectivo o facilidades de liquidez que se estima no será utilizada, cuando se cumplen las condiciones contractuales de derecho de reembolso y prelación."}, "provenance": {"to": "raapal", "archivo": "raapa
- {"local_id": "e5", "type": "Obligacion", "label": "Computar proporción no utilizada según historial de 7 años", "properties": {"tipo": "calculo", "descripcion": "Las entidades financieras pueden computar como parte no utilizada de cada contrato la menor proporción no utilizada que resulte del historial de utilización de posiciones de titulización similares durante los últimos 7 años.", "umbrales": "durante los últimos 7 años"}, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.
- {"local_id": "e6", "type": "Obligacion", "label": "Demostrar seguimiento activo de la situación financiera", "properties": {"tipo": "otra", "descripcion": "La entidad financiera debe demostrar que realiza un seguimiento activo de la situación financiera de la titulización y que sus sistemas de control interno permiten cancelar la línea ante cualquier muestra de deterioro de la solvencia del programa."}, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.4.10", "rol_documental"
- {"local_id": "e7", "type": "Obligacion", "label": "Fundamentar criterios de expectativa de utilización", "properties": {"tipo": "otra", "descripcion": "La entidad financiera debe fundamentar los criterios que sustentan su expectativa de que la parte utilizada de cada una de las facilidades no excederá de la máxima proporción que resulta de sus registros, considerando todos los factores determinantes y toda la información pertinente."}, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "pun
- {"local_id": "e8", "type": "Obligacion", "label": "Revisar estimación de proporción utilizada anualmente", "properties": {"tipo": "otra", "frecuencia": "con periodicidad anual o con mayor frecuencia"}, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.4.10", "rol_documental": "punto_propio"}, "indice_crudo": 8}
- {"local_id": "e9", "type": "Restriccion", "label": "CCF 100% para exceso de proporción estimada no utilizada", "properties": {"tipo": "limite_cuantitativo", "descripcion": "El factor de conversión crediticia aplicable a la parte de los anticipos o facilidades que exceda de la proporción estimada como no utilizada será del 100%.", "umbrales": "un CCF del 100 %"}, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.4.10", "rol_documental": "punto_propio"}, "indice_crudo": 9}
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.4.10", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.4.10", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e3", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.4.10", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e4", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.4.10", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- relación: {"source": "e5", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.4.10", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- relación: {"source": "e6", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.4.10", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- relación: {"source": "e7", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.4.10", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- relación: {"source": "e8", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.4.10", "rol_documental": "punto_propio"}, "indice_crudo": 7}
- relación: {"source": "e9", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.4.10", "rol_documental": "punto_propio"}, "indice_crudo": 8}
- relación: {"source": "e4", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.4.10", "rol_documental": "punto_propio"}, "indice_crudo": 9}
- relación: {"source": "e5", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.4.10", "rol_documental": "punto_propio"}, "indice_crudo": 10}
- relación: {"source": "e6", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.4.10", "rol_documental": "punto_propio"}, "indice_crudo": 11}
- relación: {"source": "e7", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.4.10", "rol_documental": "punto_propio"}, "indice_crudo": 12}
- relación: {"source": "e8", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.4.10", "rol_documental": "punto_propio"}, "indice_crudo": 13}
- relación: {"source": "e3", "target": "e4", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.4.10", "rol_documental": "punto_propio"}, "indice_crudo": 14}
- relación: {"source": "e9", "target": "e2", "predicate": "limita", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "raapal", "archivo": "raapal.pdf", "punto": "2.2.4.10", "rol_documental": "punto_propio"}, "indice_crudo": 15}

## 27. `apnf::1.3.1.1` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 3):

```
[encabezado | punto S1]
Sección 1. Condiciones generales.
[encabezado | punto 1.3]
1.3. Inscripción en el Banco Central de la República Argentina (BCRA).
[encabezado | punto 1.3.1]
1.3.1. Alcance.
[texto propio | punto 1.3.1.1]
1.3.1.1. Empresas no financieras emisoras de tarjetas de crédito y/o compra.
Deben inscribirse en el “Registro de empresas no financieras emisoras de tarje-
tas de crédito y/o compra”, sean o no sujeto de crédito por parte de entidades
financieras.
Para ser sujetos de crédito por parte de las entidades financieras deberán,
además, no tener restringido el acceso al financiamiento por aplicación del pun-
to 3.1.
```

Versión: primer intento (cola). Entidades 4, relaciones 6.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Texto Ordenado APNF", "properties": {}, "provenance": {"to": "apnf", "archivo": "apnf.pdf", "punto": "1.3.1.1", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Obligacion", "label": "Inscripción en registro de empresas emisoras", "properties": {"tipo": "otra", "descripcion": "Las empresas no financieras emisoras de tarjetas de crédito y/o compra deben inscribirse en el Registro de empresas no financieras emisoras de tarjetas de crédito y/o compra, sean o no sujeto de crédito por parte de entidades financieras."}, "provenance": {"to": "apnf", "archivo": "apnf.pdf", "punto": "1.3.1.1", "rol_documental": "punto_propio"}, "indic
- {"local_id": "e2", "type": "Condicion", "label": "Ser sujeto de crédito de entidades financieras", "properties": {"descripcion": "Condición para acceder al tratamiento de sujeto de crédito por parte de las entidades financieras."}, "provenance": {"to": "apnf", "archivo": "apnf.pdf", "punto": "1.3.1.1", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- {"local_id": "e3", "type": "Restriccion", "label": "Prohibición de restricción de acceso al financiamiento", "properties": {"tipo": "prohibicion", "descripcion": "Para ser sujetos de crédito por parte de las entidades financieras, las empresas no financieras emisoras de tarjetas no deben tener restringido el acceso al financiamiento por aplicación del punto 3.1."}, "provenance": {"to": "apnf", "archivo": "apnf.pdf", "punto": "1.3.1.1", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "apnf", "archivo": "apnf.pdf", "punto": "1.3.1.1", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "apnf", "archivo": "apnf.pdf", "punto": "1.3.1.1", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e3", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "apnf", "archivo": "apnf.pdf", "punto": "1.3.1.1", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e1", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_empresa_no_financiera_emisora_de_tarjetas", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "apnf", "archivo": "apnf.pdf", "punto": "1.3.1.1", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- relación: {"source": "e3", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_empresa_no_financiera_emisora_de_tarjetas", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "apnf", "archivo": "apnf.pdf", "punto": "1.3.1.1", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- relación: {"source": "e2", "target": "e3", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "apnf", "archivo": "apnf.pdf", "punto": "1.3.1.1", "rol_documental": "punto_propio"}, "indice_crudo": 5}

## 28. `ctavis::2.1.1.1` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 15):

```
[encabezado | punto S2]
Sección 2. Movimiento de las cuentas.
[encabezado | punto 2.1]
2.1. Créditos.
[encabezado | punto 2.1.1]
2.1.1. Mediante depósitos por ventanilla o cajeros automáticos.
[intro | punto 2.1.1]
Cuando se empleen boletas, éstas deberán contener, como mínimo, los siguientes datos:
[texto propio | punto 2.1.1.1]
2.1.1.1. Denominación de la caja de crédito cooperativa.
```

Versión: primer intento (cola). Entidades 1, relaciones 0.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Cuentas a la vista en el BCRA", "properties": {}, "provenance": {"to": "ctavis", "archivo": "ctavis.pdf", "punto": "2.1.1.1", "rol_documental": "punto_propio"}, "indice_crudo": 0}

## 29. `cateloc::Sbloque5` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 6, 7, 8, 9, 10):

```
[encabezado | punto S2]
Sección 2. Cuadro de categorización de localidades.
[encabezado | punto Sbloque2]
CELAS FRENTISTAS DE LA VEREDA
[texto propio | punto Sbloque5]
RAL PAZ
SAN FERNANDO DEL VALLE DE CATA-
II CATAMARCA CAPITAL
MARCA
II CHACO COMANDANTE FERNANDEZ PRESIDENCIA ROQUE SAENZ PEÑA
II CHACO SAN FERNANDO RESISTENCIA
II CHUBUT FUTALEUFU ESQUEL
II CHUBUT SARMIENTO SARMIENTO
II CORDOBA CALAMUCHITA VILLA GENERAL BELGRANO
II CORDOBA COLON JESUS MARIA
II CORDOBA COLON VILLA ALLENDE
II CORDOBA GENERAL SAN MARTIN TICINO
II CORDOBA JUAREZ CELMAN GENERAL CABRERA
II CORDOBA MARCOS JUAREZ CORRAL DE BUSTOS
II CORDOBA MARCOS JUAREZ CRUZ ALTA
II CORDOBA MARCOS JUAREZ LOS SURGENTES
II CORDOBA MARCOS JUAREZ MARCOS JUAREZ
II CORDOBA MARCOS JUAREZ MONTE BUEY
PRESIDENTE ROQUE SAENZ
II CORDOBA LABOULAYE
PEÑA
II CORDOBA PUNILLA LA FALDA
II CORDOBA PUNILLA VILLA CARLOS PAZ
II CORDOBA RIO CUARTO ADELIA MARIA
II CORDOBA RIO SEGUNDO ONCATIVO
II CORDOBA RIO SEGUNDO RIO SEGUNDO
II CORDOBA SAN JAVIER VILLA DOLORES
II CORDOBA SAN JUSTO ALICIA
II CORDOBA SAN JUSTO BRINKMANN
II CORDOBA SAN JUSTO FREYRE
II CORDOBA SAN JUSTO LAS VARILLAS
II CORDOBA SAN JUSTO MORTEROS
II CORDOBA SAN JUSTO PORTEÑA
II CORDOBA SAN JUSTO SAN FRANCISCO
II CORDOBA SANTA MARIA ALTA GRACIA
II CORDOBA TERCERO ARRIBA HERNANDO
II CORDOBA TERCERO ARRIBA OLIVA
II CORDOBA TERCERO ARRIBA RIO TERCERO
II CORDOBA UNION BELL VILLE
II CORDOBA UNION MONTE MAIZ
II CORDOBA UNION NOETINGERP
II CORRIENTES CAPITAL CORRIENTES
II CORRIENTES GOYA GOYA
II CORRIENTES PASO DE LOS LIBRES PASO DE LOS LIBRES
II ENTRE RIOS CONCORDIA CONCORDIA
II ENTRE RIOS FEDERACION CHAJARI
II ENTRE RIOS GUALEGUAY GUALEGUAY
II ENTRE RIOS GUALEGUAYCHU GUALEGUAYCHU
II ENTRE RIOS PARANA CRESPO
II ENTRE RIOS PARANA PARANA
II ENTRE RIOS URUGUAY CONCEPCION DEL URUGUAY
II FORMOSA FORMOSA FORMOSA
II JUJUY DR. MANUEL BELGRANO SAN SALVADOR DE JUJUY
II LA PAMPA CAPITAL SANTA ROSA
II LA PAMPA CHAPALEUFU INTENDENTE ALVEAR
II LA PAMPA MARACO GENERAL PICO
II LA PAMPA QUEMU QUEMU QUEMU QUEMU
II LA PAMPA REALICO INGENIERO LUIGGI
II LA PAMPA REALICO REALICO
II LA RIOJA CAPITAL LA RIOJA
II LA RIOJA CHILECITO CHILECITO
II MENDOZA GUAYMALLEN GUAYMALLEN
II MENDOZA LUJAN DE CUYO LUJAN DE CUYO
II MENDOZA MAIPU MAIPU
II MENDOZA RIVADAVIA RIVADAVIA
II MENDOZA SAN MARTIN SAN MARTIN
II MENDOZA TUNUYAN TUNUYAN
II MENDOZA TUPUNGATO TUPUNGATO
II MISIONES CAPITAL POSADAS
II MISIONES ELDORADO ELDORADO
II NEUQUEN CONFLUENCIA CUTRAL CO
II NEUQUEN LACAR SAN MARTIN DE LOS ANDES
II NEUQUEN LOS LAGOS VILLA LA ANGOSTURA
II NEUQUEN ZAPALA ZAPALA
II RIO NEGRO ADOLFO ALSINA VIEDMA
II RIO NEGRO AVELLANEDA CHOELE CHOEL
II RIO NEGRO GENERAL ROCA ALLEN
II RIO NEGRO GENERAL ROCA CATRIEL
II RIO NEGRO GENERAL ROCA CIPOLLETTI
II RIO NEGRO GENERAL ROCA GENERAL ROCA
II RIO NEGRO GENERAL ROCA VILLA REGINA
II RIO NEGRO PICHI MAHUIDA RIO COLORADO
II RIO NEGRO SAN ANTONIO SAN ANTONIO OESTE
II SALTA CAPITAL SALTA
II SAN LUIS GENERAL PEDERNERA VILLA MERCEDES
II SAN LUIS LA CAPITAL SAN LUIS
II SANTA CRUZ DESEADO CALETA OLIVIA
II SANTA CRUZ DESEADO LAS HERAS
II SANTA CRUZ DESEADO PUERTO DESEADO
II SANTA CRUZ GÜER AIKE RIO GALLEGOS
II SANTA CRUZ GÜER AIKE YACIMIENTOS RIO TURBIO
II SANTA CRUZ LAGO ARGENTINO EL CALAFATE
II SANTA FE BELGRANO ARMSTRONG
II SANTA FE BELGRANO LAS PAREJAS
II SANTA FE BELGRANO LAS ROSAS
II SANTA FE CASEROS AREQUITO
II SANTA FE CASEROS ARTEAGA
II SANTA FE CASEROS CASILDA
II SANTA FE CASEROS CHAÑAR LADEADO
II SANTA FE CASEROS SAN JOSE DE LA ESQUINA
[TABLA cateloc::tabla001 | página 8 | e0_tablas | posicional]
Fila 1: col1 = CATEGORIA | col2 = PROVINCIA | col3 = DEPARTAMENTO / PARTIDO | col4 = LOCALIDAD
Fila 2: col1 = II II II II II II II II II II II II II II II II II II II II II II II II II II II II II II II II II II II II II | col2 = SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTA FE SANTIAGO DEL ES- TERO TUCUMAN TUCUMAN | col3 = CASTELLANOS CASTELLANOS CONSTITUCION CONSTITUCION GENERAL LOPEZ GENERAL LOPEZ GENERAL LOPEZ GENERAL LOPEZ GENERAL LOPEZ GENERAL OBLIGADO GENERAL OBLIGADO IRIONDO IRIONDO IRIONDO LA CAPITAL LAS COLONIAS LAS COLONIAS LAS COLONIAS ROSARIO ROSARIO ROSARIO SAN CRISTOBAL SAN JERONIMO SAN JERONIMO SAN JUSTO SAN JUSTO SAN LORENZO SAN LORENZO SAN LORENZO SAN MARTIN SAN MARTIN SAN MARTIN SAN MARTIN VERA CAPITAL CAPITAL CHICLIGASTA | col4 = SAN VICENTE SUNCHALES ALCORTA VILLA CONSTITUCION FIRMAT() MURPHY RUFINO SANTA ISABEL VENADO TUERTO AVELLANEDA (EST. EWALD) RECONQUISTA CAÑADA DE GOMEZ SALTO GRANDE TOTORAS SANTO TOME ESPERANZA PILAR SAN CARLOS CENTRO ALVEAR ARROYO SECO VILLA GOBERNADOR GALVEZ SUARDI GALVEZ SAN GENARO GOBERNADOR CRESPO SAN JUSTO CARCARAÑA ROLDAN SAN LORENZO CAÑADA ROSQUIN EL TREBOL SAN JORGE SASTRE CALCHAQUI SANTIAGO DEL ESTERO SAN MIGUEL DE TUCUMAN (EST. TUCU- MAN) CONCEPCION
Fila 3: col1 = III III III III III III III III III III III III III III III III III III III | col2 = BUENOS AIRES BUENOS AIRES BUENOS AIRES BUENOS AIRES BUENOS AIRES BUENOS AIRES BUENOS AIRES BUENOS AIRES BUENOS AIRES BUENOS AIRES BUENOS AIRES BUENOS AIRES BUENOS AIRES BUENOS AIRES BUENOS AIRES BUENOS AIRES BUENOS AIRES BUENOS AIRES BUENOS AIRES | col3 = 25 DE MAYO 9 DE JULIO 9 DE JULIO 9 DE JULIO ADOLFO ALSINA ADOLFO ALSINA ADOLFO GONZALES CHAVES AYACUCHO BAHIA BLANCA BENITO JUAREZ BOLIVAR BRANDSEN CARLOS TEJEDOR CASTELLI CHACABUCO CHACABUCO CHACABUCO CHASCOMUS CHIVILCOY | col4 = NORBERTO DE LA RIESTRA ALFREDO DEMARCHI (EST. FACUNDO QUIROGA) DUDIGNAC MOREA MAZA RIVERA ADOLFO GONZALES CHAVES (EST. CHA- VES) AYACUCHO CABILDO BENITO JUAREZ (EST. JUAREZ) URDAMPILLETA CORONEL BRANDSEN CARLOS TEJEDOR CASTELLI CASTILLA O'HIGGINS RAWSON CHASCOMUS MOQUEHUA
[FIN TABLA cateloc::tabla001]
III BUENOS AIRES CORONEL SUAREZ HUANGUELEN
III BUENOS AIRES DAIREAUX SALAZAR
III BUENOS AIRES DOLORES DOLORES
III BUENOS AIRES EXALTACION DE LA CRUZ CAPILLA DEL SEÑOR (EST. CAPILLA)
III BUENOS AIRES GENERAL ALVARADO COMANDANTE NICANOR OTAMENDI
III BUENOS AIRES GENERAL ALVARADO MECHONGUE
III BUENOS AIRES GENERAL ARENALES ARRIBEÑOS
III BUENOS AIRES GENERAL ARENALES ASCENSION
III BUENOS AIRES GENERAL ARENALES FERRE
III BUENOS AIRES GENERAL JUAN MADARIAGA GENERAL JUAN MADARIAGA
III BUENOS AIRES GENERAL LAVALLE GENERAL LAVALLE
III BUENOS AIRES GENERAL PUEYRREDON BATAN
III BUENOS AIRES GENERAL PUEYRREDON SIERRA DE LOS PADRES
III BUENOS AIRES GENERAL VIAMONTE LOS TOLDOS
III BUENOS AIRES GENERAL VILLEGAS CAÑADA SECA
III BUENOS AIRES GENERAL VILLEGAS EMILIO V. BUNGE
III BUENOS AIRES GENERAL VILLEGAS PIEDRITAS
III BUENOS AIRES GUAMINI GARRE
III BUENOS AIRES GUAMINI LAGUNA ALSINA (EST. BONIFACIO)
III BUENOS AIRES HIPOLITO YRIGOYEN HENDERSON
III BUENOS AIRES JOSE C. PAZ JOSE C. PAZ
III BUENOS AIRES LA COSTA MAR DE AJO - SAN BERNARDO
III BUENOS AIRES LA COSTA SANTA TERESITA - MAR DEL TUYU
III BUENOS AIRES LAPRIDA LAPRIDA
CORONEL MARTINEZ DE HOZ (AP. KILO-
III BUENOS AIRES LINCOLN
METRO 322)
III BUENOS AIRES LINCOLN PASTEUR
III BUENOS AIRES LOBERIA LOBERIA
III BUENOS AIRES LOBERIA SAN MANUEL
III BUENOS AIRES LOBOS LOBOS
III BUENOS AIRES MAGDALENA MAGDALENA
III BUENOS AIRES MAIPU MAIPU
III BUENOS AIRES MAR CHIQUITA VIVORATA
III BUENOS AIRES MARCOS PAZ MARCOS PAZ
III BUENOS AIRES MONTE SAN MIGUEL DEL MONTE (EST. MONTE)
III BUENOS AIRES NAVARRO NAVARRO
III BUENOS AIRES NECOCHEA NICANOR OLIVERA (EST. LA DULCE)
III BUENOS AIRES PATAGONES CARMEN DE PATAGONES
III BUENOS AIRES PATAGONES VILLALONGA
III BUENOS AIRES PEHUAJO MONES CAZON
III BUENOS AIRES PELLEGRINI PELLEGRINI
III BUENOS AIRES PERGAMINO VILLA ANGELICA (EST. EL SOCORRO)
III BUENOS AIRES PUNTA INDIO VERONICA
III BUENOS AIRES RAUCH RAUCH
III BUENOS AIRES ROQUE PEREZ ROQUE PEREZ
III BUENOS AIRES SALTO ARROYO DULCE
III BUENOS AIRES SAN CAYETANO SAN CAYETANO
III BUENOS AIRES SAN PEDRO SANTA LUCIA
III BUENOS AIRES TAPALQUE TAPALQUE
III BUENOS AIRES TORNQUIST SIERRA DE LA VENTANA
III BUENOS AIRES TORNQUIST TORNQUIST
III BUENOS AIRES TRENQUE LAUQUEN 30 DE AGOSTO
III BUENOS AIRES TRES ARROYOS ORENSE
III BUENOS AIRES VILLARINO HILARIO ASCASUBI
III BUENOS AIRES VILLARINO MAYOR BURATOVICH
III BUENOS AIRES VILLARINO PEDRO LURO
III CHACO 25 DE MAYO MACHAGAI
III CHACO 9 DE JULIO LAS BREÑAS
III CHACO BERMEJO LA LEONESA
III CHACO CHACABUCO CHARATA
FRAY JUSTO SANTA MARIA DE
III CHACO SANTA SYLVINA
ORO
III CHACO GENERAL GÜEMES JUAN JOSE CASTELLI
III CHACO INDEPENDENCIA CAMPO LARGO
LIBERTADOR GENERAL SAN
III CHACO GENERAL JOSE DE SAN MARTIN
MARTIN
III CHACO MAIPU TRES ISLETAS
III CHACO MAYOR LUIS J. FONTANA VILLA ANGELA
III CHACO QUITILIPI QUITILIPI
III CHACO SAN FERNANDO BARRANQUERAS
III CHACO SAN LORENZO VILLA BERTHET
III CHUBUT BIEDMA PUERTO PIRAMIDE
III CHUBUT CUSHAMEN EL HOYO
III CHUBUT CUSHAMEN LAGO PUELO
III CHUBUT ESCALANTE RADA TILLY
III CHUBUT GAIMAN GAIMAN
III CHUBUT RAWSON RAWSON
III CHUBUT RIO SENGUER ALDEA BELEIRO
III CHUBUT RIO SENGUER DOCTOR RICARDO ROJAS
III CHUBUT RIO SENGUER FACUNDO
III CORDOBA COLON COLONIA TIROLESA
III CORDOBA CRUZ DEL EJE CRUZ DEL EJE
III CORDOBA GENERAL ROCA HUINCA RENANCO
III CORDOBA GENERAL ROCA VILLA HUIDOBRO
III CORDOBA GENERAL ROCA VILLA VALERIA
III CORDOBA GENERAL SAN MARTIN ARROYO CABRAL
III CORDOBA GENERAL SAN MARTIN CHAZON
III CORDOBA GENERAL SAN MARTIN ETRURIA
III CORDOBA GENERAL SAN MARTIN LA LAGUNA
III CORDOBA GENERAL SAN MARTIN LA PLAYOSA
III CORDOBA GENERAL SAN MARTIN PASCO
III CORDOBA GENERAL SAN MARTIN SILVIO PELLICO
III CORDOBA ISCHILIN DEAN FUNES
III CORDOBA JUAREZ CELMAN ALEJANDRO ROCA (EST. ALEJANDRO)
III CORDOBA JUAREZ CELMAN CARNERILLO
III CORDOBA JUAREZ CELMAN HUANCHILLAS
III CORDOBA JUAREZ CELMAN LA CARLOTA
III CORDOBA JUAREZ CELMAN UCACHA
III CORDOBA MARCOS JUAREZ ALEJO LEDESMA
III CORDOBA MARCOS JUAREZ ARIAS
III CORDOBA MARCOS JUAREZ CAMILO ALDAO
III CORDOBA MARCOS JUAREZ GENERAL BALDISSERA
III CORDOBA MARCOS JUAREZ ISLA VERDE
III CORDOBA MARCOS JUAREZ LEONES
PRESIDENTE ROQUE SAENZ
III CORDOBA GENERAL LEVALLE
PEÑA
```

Versión: primer intento (cola). Entidades 1, relaciones 0.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Cuadro de categorización de localidades", "properties": {}, "provenance": {"to": "cateloc", "archivo": "cateloc.pdf", "punto": "Sbloque5", "rol_documental": "punto_propio"}, "indice_crudo": 0}

## 30. `finsec::6.3.3.2` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 27, 28, 29):

```
[encabezado | punto S6]
Sección 6. Límites crediticios.
[encabezado | punto 6.3]
6.3. Cómputo de las financiaciones e imputación.
[encabezado | punto 6.3.3]
6.3.3. Operaciones a término, permutas, opciones y otros derivados.
[texto propio | punto 6.3.3.2]
6.3.3.2. Valor en riesgo.
i) De operaciones a término (“forwards”) y futuros, y opciones de compra o
venta, de los siguientes activos:
a) Acciones que cuenten con cotización normal y habitual por importes
significativos en mercados del país e índices sobre estas acciones.
b) Instrumentos de regulación monetaria del BCRA y títulos públicos, que
cuenten con cotización normal y habitual por importes significativos en
mercados del país.
c) Dólares estadounidenses, euros, libras esterlinas, yenes y reales.
d) Productos básicos (“commodities”) con cotización habitual en los merca-
dos, que surja diariamente de transacciones relevantes en cuyo monto la
eventual liquidación de los activos de que se trate no pueda distorsionar
significativamente su valor de mercado.
El requisito de contar con cotización normal y habitual por importes significa-
tivos en mercados del país deberá cumplirse al concertarse la operación.
VaR de operaciones a término (“forwards”) y futuros:
t
VaR = máx (5 %; 2,32 x  x )
VaR de opciones de compra o venta:
t t
VaR = máx [5 %; 2,32 x  x x |delta| + gamma x (2,32 x  x )2 x
VN / 2]
Donde
: volatilidad diaria, que equivaldrá al desvío estándar del rendi-
miento de las últimas 504 cotizaciones diarias o, en su ausencia,
de las cotizaciones existentes. Los valores considerados deberán
actualizarse al inicio de cada mes calendario.
t: cantidad de días hábiles entre la fecha de cómputo y la de valua-
ción basada en los precios de mercado del contrato derivado y li-
quidación de las diferencias a favor de una u otra contraparte, de
manera de restituir el valor del contrato a cero. Si no se prevé es-
te mecanismo, coincide con el plazo hasta el vencimiento del
contrato.
delta: coeficiente que expresa el cambio del precio de la opción ante un
cambio de un peso en el precio del activo subyacente.
gamma: coeficiente que expresa el cambio del coeficiente delta de la op-
ción ante un cambio de un peso en el precio del activo subyacen-
te.
ii) De operaciones a término (forwards) y futuros de BADLAR/TAMAR (bancos
privados), otras tasas publicadas por el BCRA, Secured Overnight Financing
Rate (SOFR), Sterling Overnight Index Average (SONIA), Tokyo Overnight
Average Rate (TONAR), Swiss Average Rate Overnight (SARON), Euro
Short-Term Rate (ESTER) y CER:
t
VaR = máx [3%; A x (T2 - T1) x ]
Donde
A: ponderador que depende de la volatilidad diaria del indicador de refe-
rencia, según la siguiente tabla
[TABLA finsec::tabla002 | página 28 | e0_tablas | columnas]
Columnas: Tasas o índice | A (en %)
Fila 1: Tasas o índice = BADLAR/TAMAR (bancos privados) | A (en %) = 0,0035
Fila 2: Tasas o índice = Otras tasas publicadas por el BCRA | A (en %) = 0,0060
Fila 3: Tasas o índice = SOFR, SONIA, TONAR, SARON o ESTER | A (en %) = 0,0010
Fila 4: Tasas o índice = CER | A (en %) = 0,0005
[FIN TABLA finsec::tabla002]
Deberán corresponder a un período de 30 días, como mínimo.
T1: período de espera, en días hábiles.
T2: período hasta el vencimiento del contrato, en días hábiles.
t: cantidad de días hábiles entre la fecha de cómputo y la de valuación ba-
sada en los precios de mercado del contrato derivado y liquidación de
las diferencias a favor de una u otra contraparte, de manera de restituir
el valor del contrato a cero. Si no se prevé este mecanismo, coincide
con T1.
iii) De operaciones de permutas (swaps) de tasas de interés, monedas y CER:
t
VaR = máx [5%; B x ]
donde
B: ponderador que depende de la volatilidad diaria del activo subyacente,
según la siguiente tabla:
[TABLA finsec::tabla003 | página 29 | e0_tablas | columnas]
Columnas: Monedas, tasas e índice | B (en %)
Fila 1: Monedas, tasas e índice = Dólar estadounidense - peso, con intercambio del principal | B (en %) = 0,60
Fila 2: Monedas, tasas e índice = Dólar estadounidense - peso, sin intercambio del principal | B (en %) = 0,20
Fila 3: Monedas, tasas e índice = Tasa fija - BADLAR/TAMAR (bancos privados) | B (en %) = 0,40
Fila 4: Monedas, tasas e índice = Tasa fija - SOFR, SONIA, TONAR, SARON o ESTER | B (en %) = 0,07
Fila 5: Monedas, tasas e índice = Tasa fija - CER | B (en %) = 0,01
Fila 6: Monedas, tasas e índice = Otros | B (en %) = 0,80
[FIN TABLA finsec::tabla003]
“Otros” incluye únicamente la combinación de tasas publicadas por el
BCRA (por depósitos a plazo fijo, BADLAR, TAMAR y BAIBAR) o la
combinación de alguna de ellas con una de las incluidas en la tabla pre-
cedente, y dólares estadounidenses, euros, libras esterlinas, yenes y
reales.
Las tasas deberán corresponder a un período de 30 días, como mínimo.
t: cantidad de días hábiles entre la fecha de cómputo y la de valuación
basada en los precios de mercado del contrato derivado y liquidación de
las diferencias a favor de una u otra contraparte, de manera de restituir
el valor del contrato a cero. Si no se prevé este mecanismo, coincide
con el plazo hasta el vencimiento del contrato.
iv) De otros derivados sobre activos que cuenten con cotización normal y habi-
tual por importes significativos en mercados del país, tasas publicadas por
dicha Institución (por depósitos a plazo fijo, BADLAR, TAMAR y BAIBAR) y
dólares estadounidenses, euros, libras esterlinas, yenes y reales:
t
VaR = 7% + C x
donde
C: 3%
t: cantidad de días hábiles entre la fecha de cómputo y la de valuación
basada en los precios de mercado del contrato derivado y liquidación de
las diferencias a favor de una u otra contraparte, de manera de restituir
el valor del contrato a cero. Si no se prevé este mecanismo, coincide
con el plazo hasta el vencimiento del contrato.
v) De otros derivados (incluidos los derivados de crédito y las opciones sobre
swaps):
VaR = 100 %
```

Versión: primer intento (cola). Entidades 11, relaciones 14.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Límites crediticios", "properties": {}, "provenance": {"to": "finsec", "archivo": "finsec.pdf", "punto": "6.3.3.2", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Operacion", "label": "Operaciones a término forwards y futuros", "properties": {"tipo": "Derivados financieros", "descripcion": "Operaciones a término (forwards) y futuros sobre acciones con cotización normal y habitual por importes significativos en mercados del país e índices sobre estas acciones; instrumentos de regulación monetaria del BCRA y títulos públicos con cotización normal y habitual por importes significativos en mercados del país; dólares estadounidenses
- {"local_id": "e2", "type": "Operacion", "label": "Opciones de compra o venta", "properties": {"tipo": "Derivados financieros", "descripcion": "Opciones de compra o venta sobre acciones con cotización normal y habitual por importes significativos en mercados del país e índices sobre estas acciones; instrumentos de regulación monetaria del BCRA y títulos públicos con cotización normal y habitual por importes significativos en mercados del país; dólares estadounidenses, euros, libras esterlinas, ye
- {"local_id": "e3", "type": "Condicion", "label": "Cotización normal y habitual al concertarse", "properties": {"descripcion": "La operación debe concertarse cuando el activo cuente con cotización normal y habitual por importes significativos en mercados del país."}, "provenance": {"to": "finsec", "archivo": "finsec.pdf", "punto": "6.3.3.2", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- {"local_id": "e4", "type": "Operacion", "label": "Operaciones a término forwards y futuros de tasas", "properties": {"tipo": "Derivados financieros sobre tasas", "descripcion": "Operaciones a término (forwards) y futuros sobre BADLAR/TAMAR (bancos privados), otras tasas publicadas por el BCRA, SOFR, SONIA, TONAR, SARON, ESTER y CER."}, "provenance": {"to": "finsec", "archivo": "finsec.pdf", "punto": "6.3.3.2", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- {"local_id": "e5", "type": "Condicion", "label": "Período mínimo de 30 días para tasas", "properties": {"descripcion": "Las tasas deben corresponder a un período de 30 días como mínimo.", "umbrales": "período de 30 días, como mínimo"}, "provenance": {"to": "finsec", "archivo": "finsec.pdf", "punto": "6.3.3.2", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- {"local_id": "e6", "type": "Operacion", "label": "Operaciones de permutas swaps de tasas", "properties": {"tipo": "Derivados financieros", "descripcion": "Operaciones de permutas (swaps) de tasas de interés, monedas y CER."}, "provenance": {"to": "finsec", "archivo": "finsec.pdf", "punto": "6.3.3.2", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- {"local_id": "e7", "type": "Condicion", "label": "Período mínimo de 30 días para swaps", "properties": {"descripcion": "Las tasas en operaciones de swaps deben corresponder a un período de 30 días como mínimo.", "umbrales": "período de 30 días, como mínimo"}, "provenance": {"to": "finsec", "archivo": "finsec.pdf", "punto": "6.3.3.2", "rol_documental": "punto_propio"}, "indice_crudo": 7}
- {"local_id": "e8", "type": "Definicion", "label": "Otros en swaps", "properties": {"termino": "Otros", "descripcion": "Incluye únicamente la combinación de tasas publicadas por el BCRA (por depósitos a plazo fijo, BADLAR, TAMAR y BAIBAR) o la combinación de alguna de ellas con una de las incluidas en la tabla de ponderadores de swaps, y dólares estadounidenses, euros, libras esterlinas, yenes y reales."}, "provenance": {"to": "finsec", "archivo": "finsec.pdf", "punto": "6.3.3.2", "rol_documental
- {"local_id": "e9", "type": "Operacion", "label": "Otros derivados sobre activos con cotización", "properties": {"tipo": "Derivados financieros", "descripcion": "Otros derivados sobre activos que cuenten con cotización normal y habitual por importes significativos en mercados del país, tasas publicadas por el BCRA (por depósitos a plazo fijo, BADLAR, TAMAR y BAIBAR) y dólares estadounidenses, euros, libras esterlinas, yenes y reales."}, "provenance": {"to": "finsec", "archivo": "finsec.pdf", "pun
- {"local_id": "e10", "type": "Operacion", "label": "Otros derivados incluidos derivados de crédito", "properties": {"tipo": "Derivados financieros", "descripcion": "Otros derivados incluidos los derivados de crédito y las opciones sobre swaps."}, "provenance": {"to": "finsec", "archivo": "finsec.pdf", "punto": "6.3.3.2", "rol_documental": "punto_propio"}, "indice_crudo": 10}
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "finsec", "archivo": "finsec.pdf", "punto": "6.3.3.2", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "finsec", "archivo": "finsec.pdf", "punto": "6.3.3.2", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e3", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "finsec", "archivo": "finsec.pdf", "punto": "6.3.3.2", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e3", "target": "e1", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "finsec", "archivo": "finsec.pdf", "punto": "6.3.3.2", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- relación: {"source": "e3", "target": "e2", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "finsec", "archivo": "finsec.pdf", "punto": "6.3.3.2", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- relación: {"source": "e4", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "finsec", "archivo": "finsec.pdf", "punto": "6.3.3.2", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- relación: {"source": "e5", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "finsec", "archivo": "finsec.pdf", "punto": "6.3.3.2", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- relación: {"source": "e5", "target": "e4", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "finsec", "archivo": "finsec.pdf", "punto": "6.3.3.2", "rol_documental": "punto_propio"}, "indice_crudo": 7}
- relación: {"source": "e6", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "finsec", "archivo": "finsec.pdf", "punto": "6.3.3.2", "rol_documental": "punto_propio"}, "indice_crudo": 8}
- relación: {"source": "e7", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "finsec", "archivo": "finsec.pdf", "punto": "6.3.3.2", "rol_documental": "punto_propio"}, "indice_crudo": 9}
- relación: {"source": "e7", "target": "e6", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "finsec", "archivo": "finsec.pdf", "punto": "6.3.3.2", "rol_documental": "punto_propio"}, "indice_crudo": 10}
- relación: {"source": "e8", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "finsec", "archivo": "finsec.pdf", "punto": "6.3.3.2", "rol_documental": "punto_propio"}, "indice_crudo": 11}
- relación: {"source": "e9", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "finsec", "archivo": "finsec.pdf", "punto": "6.3.3.2", "rol_documental": "punto_propio"}, "indice_crudo": 12}
- relación: {"source": "e10", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "finsec", "archivo": "finsec.pdf", "punto": "6.3.3.2", "rol_documental": "punto_propio"}, "indice_crudo": 13}

