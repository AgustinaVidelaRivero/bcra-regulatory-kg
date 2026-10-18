# Material de T4 — cola (30 fichas; B6.1, tanda 1, T3, punto 7.5)

Sorteo: `cola.json` (89305f3f…, 2026-10-18T10:09:26-03:00); material armado a las 2026-10-18T10:12:10-03:00. Sin el estado de E3 ni las marcas de E3.

## 1. `ri_ccna::D1F2::3.2` — RI:sin_raiz · cola

Texto que vio E3 (e0, bloque de lista True; págs. 32):

```
[encabezado | punto D1F2]
DECLARACIÓN JURADA DE AUDITORES EXTERNOS
[encabezado | punto D1F2::S3]
3. No me alcanza ninguna de las siguientes inhabilidades previstas por el artículo 10 de la Ley Nº 21.526, según se detalla a conti-
nuación:
[texto propio | punto D1F2::3.2]
3.2 Los inhabilitados para ejercer cargos públicos
```

Versión: primer intento (cola). Entidades 1, relaciones 0.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Declaración Jurada de Auditores Externos", "properties": {}, "provenance": {"to": "ri_ccna", "archivo": "ri_ccna.pdf", "punto": "D1F2::3.2", "rol_documental": "punto_propio"}, "indice_crudo": 0}

## 2. `ri_ccna::D1F2::3.7` — RI:sin_raiz · cola

Texto que vio E3 (e0, bloque de lista True; págs. 32):

```
[encabezado | punto D1F2]
DECLARACIÓN JURADA DE AUDITORES EXTERNOS
[encabezado | punto D1F2::S3]
3. No me alcanza ninguna de las siguientes inhabilidades previstas por el artículo 10 de la Ley Nº 21.526, según se detalla a conti-
nuación:
[texto propio | punto D1F2::3.7]
3.7 Quienes se encuentren alcanzados por las incompatibilidades que para el desempeño como síndico, determina el artículo
286, incisos 2) y 3) de la Ley Nº 19.550, que se refiere respectivamente a :
- Los directores, gerentes y empleados de la misma sociedad o de otra controlada o controlante, y
- Los cónyuges, los parientes por consanguinidad en línea recta, los colaterales hasta el cuarto grado inclusive y los
afines dentro del segundo, de los directores y gerentes generales.
```

Versión: primer intento (cola). Entidades 4, relaciones 3.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Declaración Jurada de Auditores Externos", "properties": {}, "provenance": {"to": "ri_ccna", "archivo": "ri_ccna.pdf", "punto": "D1F2::3.7", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Restriccion", "label": "Incompatibilidad síndico — directores, gerentes, empleados", "properties": {"tipo": "prohibicion", "descripcion": "No pueden desempeñarse como síndicos los directores, gerentes y empleados de la misma sociedad o de otra controlada o controlante, conforme al artículo 286, incisos 2) y 3) de la Ley Nº 19.550."}, "provenance": {"to": "ri_ccna", "archivo": "ri_ccna.pdf", "punto": "D1F2::3.7", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- {"local_id": "e2", "type": "Restriccion", "label": "Incompatibilidad síndico — parientes de directores y gerentes", "properties": {"tipo": "prohibicion", "descripcion": "No pueden desempeñarse como síndicos los cónyuges, los parientes por consanguinidad en línea recta, los colaterales hasta el cuarto grado inclusive y los afines dentro del segundo grado de los directores y gerentes generales, conforme al artículo 286, incisos 2) y 3) de la Ley Nº 19.550."}, "provenance": {"to": "ri_ccna", "archi
- {"local_id": "e3", "type": "Comunicacion", "label": "Ley Nº 19.550", "properties": {"codigo": "Ley Nº 19.550"}, "provenance": {"to": "ri_ccna", "archivo": "ri_ccna.pdf", "punto": "D1F2::3.7", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_ccna", "archivo": "ri_ccna.pdf", "punto": "D1F2::3.7", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_ccna", "archivo": "ri_ccna.pdf", "punto": "D1F2::3.7", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "to", "target": "e3", "predicate": "referencia", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_ccna", "archivo": "ri_ccna.pdf", "punto": "D1F2::3.7", "rol_documental": "punto_propio"}, "indice_crudo": 2}

## 3. `ri_ccna::D1F2::S1` — RI:sin_raiz · cola

Texto que vio E3 (e0, bloque de lista True; págs. 32):

```
[encabezado | punto D1F2]
DECLARACIÓN JURADA DE AUDITORES EXTERNOS
[chapeau_seccion | punto D1F2::S0]
Declaro bajo juramento como Auditor Externo de la Caja de Crédito que:
[texto propio | punto D1F2::S1]
1. No soy socio o accionista, director o administrador de la entidad, ni de personas o empresas económicamente vinculadas a ella.
```

Versión: primer intento (cola). Entidades 2, relaciones 2.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Declaración Jurada de Auditores Externos", "properties": {}, "provenance": {"to": "ri_ccna", "archivo": "ri_ccna.pdf", "punto": "D1F2::S1", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Restriccion", "label": "Prohibición de vínculos patrimoniales — auditor externo", "properties": {"tipo": "prohibicion", "descripcion": "El auditor externo no puede ser socio, accionista, director o administrador de la caja de crédito ni de personas o empresas económicamente vinculadas a ella"}, "provenance": {"to": "ri_ccna", "archivo": "ri_ccna.pdf", "punto": "D1F2::S1", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_ccna", "archivo": "ri_ccna.pdf", "punto": "D1F2::S1", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e1", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_rol_alcance_autenf", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_ccna", "archivo": "ri_ccna.pdf", "punto": "D1F2::S1", "rol_documental": "punto_propio"}, "indice_crudo": 1}

## 4. `ri_ccna::D1F2::S5` — RI:sin_raiz · cola

Texto que vio E3 (e0, bloque de lista True; págs. 32):

```
[encabezado | punto D1F2]
DECLARACIÓN JURADA DE AUDITORES EXTERNOS
[chapeau_seccion | punto D1F2::S0]
Declaro bajo juramento como Auditor Externo de la Caja de Crédito que:
[texto propio | punto D1F2::S5]
5. No he sido expresamente inhabilitado para ejercer la profesión por ninguno de los Consejos Profesionales de Ciencias Económi-
cas del país.
```

Versión: primer intento (cola). Entidades 2, relaciones 1.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Declaración Jurada de Auditores Externos", "properties": {}, "provenance": {"to": "ri_ccna", "archivo": "ri_ccna.pdf", "punto": "D1F2::S5", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Restriccion", "label": "No inhabilitación por Consejos Profesionales", "properties": {"tipo": "prohibicion", "descripcion": "El auditor externo declara que no ha sido expresamente inhabilitado para ejercer la profesión por ninguno de los Consejos Profesionales de Ciencias Económicas del país"}, "provenance": {"to": "ri_ccna", "archivo": "ri_ccna.pdf", "punto": "D1F2::S5", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_ccna", "archivo": "ri_ccna.pdf", "punto": "D1F2::S5", "rol_documental": "punto_propio"}, "indice_crudo": 0}

## 5. `ri_ccna::D1F6::S1` — RI:sin_raiz · cola

Texto que vio E3 (e0, bloque de lista True; págs. 41):

```
[encabezado | punto D1F6]
DECLARACIÓN JURADA DEL SOCIO RESPONSABLE
[chapeau_seccion | punto D1F6::S0]
Declaro bajo juramento, como Socio Responsable por la labor del auditor externo de la Entidad que:
[texto propio | punto D1F6::S1]
1. No soy socio o accionista, director o administrador de la entidad, ni de personas o empresas económicamente vinculadas a ella.
```

Versión: primer intento (cola). Entidades 2, relaciones 2.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Régimen de Cuentas Corrientes", "properties": {}, "provenance": {"to": "ri_ccna", "archivo": "ri_ccna.pdf", "punto": "D1F6::S1", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Restriccion", "label": "Prohibición de vínculos patrimoniales — Socio Responsable", "properties": {"tipo": "prohibicion", "descripcion": "El Socio Responsable no puede ser socio, accionista, director o administrador de la entidad ni de personas o empresas económicamente vinculadas a ella."}, "provenance": {"to": "ri_ccna", "archivo": "ri_ccna.pdf", "punto": "D1F6::S1", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_ccna", "archivo": "ri_ccna.pdf", "punto": "D1F6::S1", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e1", "target": null, "predicate": "aplica_a", "sujeto_id": null, "sujeto_propuesto": "Socio Responsable", "sujeto_propuesto_padre_sugerido": "Sujeto_sujeto_regulado", "provenance": {"to": "ri_ccna", "archivo": "ri_ccna.pdf", "punto": "D1F6::S1", "rol_documental": "punto_propio"}, "indice_crudo": 1}

## 6. `ri_ccna::D2A2::S1` — RI:sin_raiz · cola

Texto que vio E3 (e0, bloque de lista True; págs. 49):

```
[encabezado | punto D2A2]
ANEXO II
[texto propio | punto D2A2::S1]
1. Ciclos.
Los ciclos más relevantes en las Cajas de crédito y que requieren de un adecuado
funcionamiento de los controles internos, sin que constituya una enunciación taxativa, son los
siguientes:
- Tesorería (función financiera);
- Presentación de información contable y financiera;
- Préstamos;
- Depósitos;
- Inversiones;
- Bienes de uso diversos e intangibles
- Costos de personal;
- Tecnología informática;
- Compras;
- Contabilidad General (incluyendo las partidas pendientes de imputación)
```

Versión: primer intento (cola). Entidades 3, relaciones 3.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Régimen Informativo Cajas de Crédito", "properties": {}, "provenance": {"to": "ri_ccna", "archivo": "ri_ccna.pdf", "punto": "D2A2::S1", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Definicion", "label": "Ciclos relevantes en Cajas de crédito", "properties": {"termino": "Ciclos", "descripcion": "Los ciclos más relevantes en las Cajas de crédito que requieren de un adecuado funcionamiento de los controles internos son: Tesorería (función financiera), Presentación de información contable y financiera, Préstamos, Depósitos, Inversiones, Bienes de uso diversos e intangibles, Costos de personal, Tecnología informática, Compras, y Contabilidad General 
- {"local_id": "e2", "type": "Obligacion", "label": "Documentar e informar sobre evaluación de controles", "properties": {"tipo": "otra", "descripcion": "Las Cajas de crédito deberán documentar e informar sobre las tareas de relevamiento y evaluación de los controles de cada uno de los ciclos relevantes para asegurar el adecuado funcionamiento de la estructura de control interno."}, "provenance": {"to": "ri_ccna", "archivo": "ri_ccna.pdf", "punto": "D2A2::S1", "rol_documental": "punto_propio"}, "i
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_ccna", "archivo": "ri_ccna.pdf", "punto": "D2A2::S1", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_ccna", "archivo": "ri_ccna.pdf", "punto": "D2A2::S1", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e2", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_caja_de_credito", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_ccna", "archivo": "ri_ccna.pdf", "punto": "D2A2::S1", "rol_documental": "punto_propio"}, "indice_crudo": 2}

## 7. `ri_dcpc::3.1.1` — RI:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 9):

```
[encabezado | punto S3]
Sección 3. CRITERIOS GENERALES
[encabezado | punto 3.1]
3.1. Criterios generales de imputación para activos financieros
[texto propio | punto 3.1.1]
3.1.1. Baja en cuentas de activos financieros.
A los fines de aplicar las disposiciones de baja en cuentas de la NIIF 9, la evaluación deberá
realizarse tanto a nivel consolidado, como está previsto en el punto 3.2.1, como a nivel individual.
Aquellos activos financieros que no cumplen con las condiciones para ser dados de baja
contablemente, de acuerdo con el punto 3.2. de la NIIF 9, continuarán registrándose en las cuentas
de activos financieros que correspondan. Las entidades deberán mantener los registros detallados
que resulten necesarios para poder incluir en información complementaria a los Estados Financieros
toda la información requerida por las NIIF, así como para cumplimentar los datos que se soliciten en
el régimen informativo respecto de estos activos y, de corresponder, los pasivos asociados.
```

Versión: primer intento (cola). Entidades 5, relaciones 7.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Texto Ordenado Información Contable", "properties": {}, "provenance": {"to": "ri_dcpc", "archivo": "ri_dcpc.pdf", "punto": "3.1.1", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Operacion", "label": "Baja en cuentas de activos financieros", "properties": {"tipo": "Baja contable", "descripcion": "Evaluación de baja en cuentas de activos financieros conforme a NIIF 9, realizada tanto a nivel consolidado como a nivel individual"}, "provenance": {"to": "ri_dcpc", "archivo": "ri_dcpc.pdf", "punto": "3.1.1", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- {"local_id": "e2", "type": "Condicion", "label": "Cumplimiento condiciones baja contable NIIF 9", "properties": {"descripcion": "El activo financiero cumple con las condiciones para baja contable según punto 3.2 de NIIF 9"}, "provenance": {"to": "ri_dcpc", "archivo": "ri_dcpc.pdf", "punto": "3.1.1", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- {"local_id": "e3", "type": "Obligacion", "label": "Mantener registros detallados de activos financieros", "properties": {"tipo": "presentacion_informativa", "descripcion": "Mantener registros detallados necesarios para incluir en información complementaria a los Estados Financieros la información requerida por NIIF y cumplimentar datos del régimen informativo respecto de activos financieros y pasivos asociados"}, "provenance": {"to": "ri_dcpc", "archivo": "ri_dcpc.pdf", "punto": "3.1.1", "rol_do
- {"local_id": "e4", "type": "Obligacion", "label": "Continuar registro en cuentas de activos financieros", "properties": {"tipo": "otra", "descripcion": "Los activos financieros que no cumplen condiciones de baja contable conforme NIIF 9 punto 3.2 continuarán registrándose en las cuentas de activos financieros correspondientes"}, "provenance": {"to": "ri_dcpc", "archivo": "ri_dcpc.pdf", "punto": "3.1.1", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dcpc", "archivo": "ri_dcpc.pdf", "punto": "3.1.1", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dcpc", "archivo": "ri_dcpc.pdf", "punto": "3.1.1", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e3", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dcpc", "archivo": "ri_dcpc.pdf", "punto": "3.1.1", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e4", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dcpc", "archivo": "ri_dcpc.pdf", "punto": "3.1.1", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- relación: {"source": "e3", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dcpc", "archivo": "ri_dcpc.pdf", "punto": "3.1.1", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- relación: {"source": "e4", "target": null, "predicate": "aplica_a", "sujeto_id": null, "sujeto_propuesto": "Aquellos activos financieros", "sujeto_propuesto_padre_sugerido": "Sujeto_estructura", "provenance": {"to": "ri_dcpc", "archivo": "ri_dcpc.pdf", "punto": "3.1.1", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- relación: {"source": "e2", "target": "e4", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_dcpc", "archivo": "ri_dcpc.pdf", "punto": "3.1.1", "rol_documental": "punto_propio"}, "indice_crudo": 6}

## 8. `ri_pgn::2.2.2` — RI:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 4):

```
[encabezado | punto S2]
Sección 2. Instrucciones particulares
[encabezado | punto 2.2]
2.2. Posiciones diarias
[texto propio | punto 2.2.2]
2.2.2. Posición de contado –Código de partida 410dd-
Se informará esta posición teniendo en cuenta lo establecido en el punto 2.2.2 de las
normas sobre “Posición Global Neta de Moneda Extranjera”.
```

Versión: primer intento (cola). Entidades 3, relaciones 3.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Régimen Informativo Contable", "properties": {}, "provenance": {"to": "ri_pgn", "archivo": "ri_pgn.pdf", "punto": "2.2.2", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Operacion", "label": "Posición de contado — Código 410dd", "properties": {"tipo": "Posición de contado", "descripcion": "Posición de contado identificada con código de partida 410dd, determinada según lo establecido en el punto 2.2.2 de las normas sobre Posición Global Neta de Moneda Extranjera"}, "provenance": {"to": "ri_pgn", "archivo": "ri_pgn.pdf", "punto": "2.2.2", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- {"local_id": "e2", "type": "Obligacion", "label": "Informar posición de contado", "properties": {"tipo": "presentacion_informativa", "descripcion": "Deber de informar la posición de contado conforme a lo establecido en el punto 2.2.2 de las normas sobre Posición Global Neta de Moneda Extranjera"}, "provenance": {"to": "ri_pgn", "archivo": "ri_pgn.pdf", "punto": "2.2.2", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_pgn", "archivo": "ri_pgn.pdf", "punto": "2.2.2", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": "e1", "predicate": "regula", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_pgn", "archivo": "ri_pgn.pdf", "punto": "2.2.2", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e2", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_rol_entidad_comprendida_reginf", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_pgn", "archivo": "ri_pgn.pdf", "punto": "2.2.2", "rol_documental": "punto_propio"}, "indice_crudo": 2}

## 9. `ri_rml::Sbloque10` — RI:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 40, 41):

```
[encabezado | punto S4]
Sección 4. Disposiciones transitorias
[texto propio | punto Sbloque10]
BCRA / 5. EFECTIVO MINIMO Y APLICACIÓN DE RECURSOS (R.I. – E.M.-A.R.)
4. Disposiciones transitorias
6.3. Estructura de plazos residuales aplicable a los depósitos a plazo.
Se aplicará la de noviembre/16, sin computar los depósitos a plazo de FCI de ese perío-
do.
7. Cómputo de las colocaciones de títulos valores de deuda denominados en “UVA” y “UVI” (Co-
municación “A” 6204) durante el período marzo/17.
De existir colocaciones por este concepto, se informarán conforme se indica seguidamente:
Cómputo de los depósitos promedios
Sub-período
de las colocaciones de títulos en Se informan en el código de partida...
Marzo 2017
“UVA” y “UVI”
01/03/17 – ∑ (Saldo diario de depósitos días 1
10180X/001
20/03/17 al 20) / 31
21/013/17 – ∑ (Saldo diario de depósitos días 21
10166X/001
31/03/17 al 31) / 31
8. Posición trimestral mayo/julio de 2018.
8.1. Cómputo
La determinación de la posición trimestral de Efectivo mínimo será efectuada por
esta Institución sobre la base de los datos informados para cada uno de los meses y
los totales de control que serán incluidos conjuntamente con los datos de julio. Para
su cálculo se considerará el promedio que surja de dividir la suma de los nume-
rales de las posiciones mensuales por la cantidad de días del trimestre.
8.2. Instrucciones comunes para las informaciones correspondientes a mayo, junio y julio
de 2018.
8.2.1. Exigencia e Integración (promedio)
Se informarán por separado las partidas sujetas a exigencia correspondien-
tes a cada uno de los meses, dividiendo los saldos diarios por la cantidad de
días comprendidos en cada uno de ellos.
El mismo criterio se aplicará a los datos del Código 801000/001-Depósitos
de entidades financieras locales.
8.2.2. Disminución de Exigencia
Se informarán las partidas 70X000/001 y su correspondiente totalizadora
700000/001, en mayo, junio y julio de acuerdo con la metodología esta-
blecida en el punto 1.2.4., considerando en su cálculo los saldos co-
rrespondientes a abril/2018.
Conforme a lo dispuesto en la Comunicación “A” 6531, las partidas
702000/001 a 706000/001 sólo podrán informarse en mayo y junio.
8.2.3. Exigencia mínima diaria
Para su determinación se tendrán en cuenta las exigencias de abril, recalcu-
ladas en función de los conceptos y tasas vigentes en el trimestre.
Las partidas de exigencia mínima diaria (451000 y 451200) y de integración
diaria (4520xx) correspondientes a mayo no serán informadas.
8.2.4. Totales de Control
[TABLA ri_rml::tabla018 | página 41 | e0_tablas | columnas]
Columnas: Código | Concepto | Cómputo
Fila 1: Código = 907100/001 | Concepto = Exigencia sobre obligaciones com- prendidas | Cómputo = Trimestral
Fila 2: Código = 903100/001 | Concepto = Total de exigencia de efectivo mí- nimo (Código 907100/001 + exigen- cias adicionales) | Cómputo = Trimestral
Fila 3: Código = 904100/001 | Concepto = Integración de efectivo mínimo | Cómputo = Trimestral
Fila 4: Código = 700100/001 | Concepto = Disminución de exigencia | Cómputo = Trimestral
[FIN TABLA ri_rml::tabla018]
8.2.5. Traslado de exigencia
No corresponderá informar la partida 750000/00001 en mayo y junio.
Para el cálculo del traslado al trimestre mayo-julio se computarán los nu-
merales de abril divididos por la cantidad de días del trimestre.
Para el cálculo del traslado a agosto se computarán los numerales de la
posición mayo-julio divididos por la cantidad de días del período agosto
(31 días).
8.2.6. Cargos
De registrar defectos de integración en promedio o diaria en el trimestre,
para la liquidación del cargo se utilizará la tasa del último día hábiles de
julio.
De existir franquicias por disminución de cargos (códigos 681000/001 y
682000/001) se informarán únicamente con los datos de julio.
8.2.7. Estructura de plazos residuales
Para determinar la exigencia, en la posición trimestral se considerará la es-
tructura de plazos residuales de abril, y en agosto, la correspondiente a julio.
```

Versión: primer intento (cola). Entidades 23, relaciones 27.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Régimen Informativo - Efectivo Mínimo", "properties": {}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Operacion", "label": "Cómputo estructura plazos residuales depósitos", "properties": {"tipo": "cálculo de estructura de plazos", "descripcion": "Cálculo de la estructura de plazos residuales aplicable a los depósitos a plazo, utilizando la estructura de noviembre/16 sin computar los depósitos a plazo de FCI de ese período."}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- {"local_id": "e2", "type": "Operacion", "label": "Cómputo colocaciones títulos valores UVA/UVI", "properties": {"tipo": "cálculo de depósitos promedios", "descripcion": "Cómputo de los depósitos promedios de las colocaciones de títulos valores de deuda denominados en UVA y UVI durante marzo/17, conforme a la metodología indicada.", "referencia_normativa": "Comunicación A 6204"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indi
- {"local_id": "e3", "type": "Obligacion", "label": "Informar colocaciones UVA/UVI período 01/03-20/03", "properties": {"tipo": "presentacion_informativa", "descripcion": "Informar en el código de partida 10180X/001 el cómputo de depósitos promedios de colocaciones en UVA/UVI para el sub-período 01/03/17 a 20/03/17, calculado como suma de saldos diarios dividida por 31.", "umbrales": "días 1 al 20"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "p
- {"local_id": "e4", "type": "Obligacion", "label": "Informar colocaciones UVA/UVI período 21/03-31/03", "properties": {"tipo": "presentacion_informativa", "descripcion": "Informar en el código de partida 10166X/001 el cómputo de depósitos promedios de colocaciones en UVA/UVI para el sub-período 21/03/17 a 31/03/17, calculado como suma de saldos diarios dividida por 31.", "umbrales": "días 21 al 31"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "
- {"local_id": "e5", "type": "Operacion", "label": "Determinación posición trimestral efectivo mínimo", "properties": {"tipo": "cálculo de posición trimestral", "descripcion": "Determinación de la posición trimestral de Efectivo mínimo por el BCRA sobre la base de datos informados mensualmente y totales de control incluidos con datos de julio, calculada como promedio de posiciones mensuales dividido por cantidad de días del trimestre."}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "pun
- {"local_id": "e6", "type": "Obligacion", "label": "Informar partidas exigencia integración promedio", "properties": {"tipo": "presentacion_informativa", "descripcion": "Informar por separado las partidas sujetas a exigencia para cada mes de mayo, junio y julio de 2018, dividiendo los saldos diarios por la cantidad de días comprendidos en cada mes."}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- {"local_id": "e7", "type": "Obligacion", "label": "Aplicar mismo criterio Código 801000/001", "properties": {"tipo": "presentacion_informativa", "descripcion": "Aplicar el mismo criterio de división de saldos diarios por cantidad de días a los datos del Código 801000/001 (Depósitos de entidades financieras locales)."}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 7}
- {"local_id": "e8", "type": "Obligacion", "label": "Informar partidas disminución exigencia 70X000/001", "properties": {"tipo": "presentacion_informativa", "descripcion": "Informar las partidas 70X000/001 y su totalizadora 700000/001 en mayo, junio y julio de 2018 conforme a metodología del punto 1.2.4, considerando saldos de abril/2018.", "umbrales": "mayo, junio y julio"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_cr
- {"local_id": "e9", "type": "Restriccion", "label": "Prohibición informar partidas 702000/001-706000/001 julio", "properties": {"tipo": "prohibicion", "descripcion": "Las partidas 702000/001 a 706000/001 no podrán informarse en julio, conforme a Comunicación A 6531.", "umbrales": "sólo en mayo y junio", "referencia_normativa": "Comunicación A 6531"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 9}
- {"local_id": "e10", "type": "Obligacion", "label": "Determinar exigencia mínima diaria recalculada", "properties": {"tipo": "calculo", "descripcion": "Determinar la exigencia mínima diaria considerando las exigencias de abril recalculadas en función de conceptos y tasas vigentes en el trimestre mayo-julio."}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 10}
- {"local_id": "e11", "type": "Restriccion", "label": "Prohibición informar partidas exigencia mínima diaria mayo", "properties": {"tipo": "prohibicion", "descripcion": "Las partidas de exigencia mínima diaria (451000 y 451200) y de integración diaria (4520xx) correspondientes a mayo no podrán ser informadas.", "umbrales": "correspondientes a mayo"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 11}
- {"local_id": "e12", "type": "Obligacion", "label": "Informar totales control exigencia obligaciones", "properties": {"tipo": "presentacion_informativa", "descripcion": "Informar el total de control Código 907100/001 (Exigencia sobre obligaciones comprendidas) con cómputo trimestral.", "umbrales": "Trimestral"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 12}
- {"local_id": "e13", "type": "Obligacion", "label": "Informar total exigencia efectivo mínimo", "properties": {"tipo": "presentacion_informativa", "descripcion": "Informar el total de control Código 903100/001 (Total de exigencia de efectivo mínimo, suma de Código 907100/001 más exigencias adicionales) con cómputo trimestral.", "umbrales": "Trimestral"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 13}
- {"local_id": "e14", "type": "Obligacion", "label": "Informar integración efectivo mínimo", "properties": {"tipo": "presentacion_informativa", "descripcion": "Informar el total de control Código 904100/001 (Integración de efectivo mínimo) con cómputo trimestral.", "umbrales": "Trimestral"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 14}
- {"local_id": "e15", "type": "Obligacion", "label": "Informar disminución exigencia", "properties": {"tipo": "presentacion_informativa", "descripcion": "Informar el total de control Código 700100/001 (Disminución de exigencia) con cómputo trimestral.", "umbrales": "Trimestral"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 15}
- {"local_id": "e16", "type": "Restriccion", "label": "Prohibición informar partida traslado exigencia mayo-junio", "properties": {"tipo": "prohibicion", "descripcion": "No corresponde informar la partida 750000/00001 en mayo y junio de 2018.", "umbrales": "en mayo y junio"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 16}
- {"local_id": "e17", "type": "Operacion", "label": "Cálculo traslado exigencia trimestre mayo-julio", "properties": {"tipo": "cálculo de traslado", "descripcion": "Cálculo del traslado de exigencia al trimestre mayo-julio computando los numerales de abril divididos por la cantidad de días del trimestre."}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 17}
- {"local_id": "e18", "type": "Operacion", "label": "Cálculo traslado exigencia agosto", "properties": {"tipo": "cálculo de traslado", "descripcion": "Cálculo del traslado de exigencia a agosto computando los numerales de la posición mayo-julio divididos por 31 días.", "umbrales": "31 días"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 18}
- {"local_id": "e19", "type": "Obligacion", "label": "Utilizar tasa último día hábil julio para liquidación cargo", "properties": {"tipo": "calculo", "descripcion": "Para la liquidación de cargo por defectos de integración en promedio o diaria en el trimestre mayo-julio, utilizar la tasa del último día hábil de julio."}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 19}
- {"local_id": "e20", "type": "Obligacion", "label": "Informar franquicias disminución cargos julio", "properties": {"tipo": "presentacion_informativa", "descripcion": "Informar las franquicias por disminución de cargos (códigos 681000/001 y 682000/001) únicamente con los datos de julio.", "umbrales": "únicamente con los datos de julio"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 20}
- {"local_id": "e21", "type": "Condicion", "label": "Estructura plazos residuales abril para posición trimestral", "properties": {"descripcion": "Para determinar la exigencia en la posición trimestral, se considera la estructura de plazos residuales de abril.", "umbrales": "de abril"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 21}
- {"local_id": "e22", "type": "Condicion", "label": "Estructura plazos residuales julio para agosto", "properties": {"descripcion": "Para determinar la exigencia en agosto, se considera la estructura de plazos residuales de julio.", "umbrales": "de julio"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 22}
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e3", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e4", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- relación: {"source": "e5", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- relación: {"source": "e6", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- relación: {"source": "e7", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- relación: {"source": "e8", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 7}
- relación: {"source": "e9", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 8}
- relación: {"source": "e10", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 9}
- relación: {"source": "e11", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 10}
- relación: {"source": "e12", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 11}
- relación: {"source": "e13", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 12}
- relación: {"source": "e14", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 13}
- relación: {"source": "e15", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 14}
- relación: {"source": "e16", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 15}
- relación: {"source": "e17", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 16}
- relación: {"source": "e18", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 17}
- relación: {"source": "e19", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 18}
- relación: {"source": "e20", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 19}
- relación: {"source": "e21", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 20}
- relación: {"source": "e22", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 21}
- relación: {"source": "e6", "target": "e5", "predicate": "regula", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 22}
- relación: {"source": "e8", "target": "e5", "predicate": "regula", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 23}
- relación: {"source": "e10", "target": "e5", "predicate": "regula", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 24}
- relación: {"source": "e21", "target": "e5", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 25}
- relación: {"source": "e22", "target": "e5", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque10", "rol_documental": "punto_propio"}, "indice_crudo": 26}

## 10. `ri_rml::Sbloque14::parte1` — RI:resto · cola

Texto que vio E3 (e0_con_las_partes, bloque de lista True; págs. 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68):

```
[encabezado | punto S4]
Sección 4. Disposiciones transitorias
[texto propio | punto Sbloque14]
5. EFECTIVO MINIMO Y APLICACIÓN DE RECURSOS (R.I. – E.M.-A.R.)
11. Consideraciones particulares para la presentación de Agosto/18.
A efectos de determinar la estructura de plazos residuales (punto 1.2.3.) aplicable a los de-
pósitos a plazo fijo correspondientes a agosto/18, se considerarán los conceptos informa-
dos en julio/18 en los siguientes códigos de partida: 10140X/001, 10160X/001,
10163X/001, 10175X/001, 10171X/001, 11140X/001, 11175X/001, 11171X/001,
12140X/001, 12175X/001 y 12171X/001.
Las partidas 824000/001 y 210105/TP, continúan vigentes para el mes de agosto y
meses subsiguientes, considerado para su determinación los siguientes cálculos:
Código 824000/TP = • Código 907000/001
(Agosto/18 con tasas s/ puntos 1. Com. “A” 6526 y 2. Com.
= ∑ (Saldos promedio * em ) +
“A” 6532) (01/08 al 31/08) (21/06)
[907000/001 ∑ (Saldos promedio * Diferencia % [em
(Agosto/18 (1/08 al 31/08) (18/07) –
em ]
con tasas s/ puntos 1. Com. “A” (17/7)
Agosto/18 6526 y 2. Com. “A” 6532)
• Código 907000/001 = ∑ (Saldos prome-
(Agosto/18 c/tasas 20/06)
menos dio * em )
(01/08 al 31/08) (20/06)
907000/001
• Saldos promedio: calculados conforme a lo especificado
(Agosto/18 con
]
en el punto 10.1.
tasas al 20/06/18
11.1. Instrucciones particulares para las Entidades Grupo “A”.
11.1.1 Exigencia promedio
a) Para el subperíodo comprendido entre el 01/08 y 15/08 el modelo de informa-
ción a utilizar será el siguiente:
[TABLA ri_rml::tabla025 | página 48, 49 | e0_tablas | posicional]
Fila 1: col1 = 01/08 – 15/08 | col2 = CONCEPTO
Fila 2: col1 = CÓDIGO | col2 = PARTIDAS COMPRENDIDAS EN PESOS
Fila 3: col1 = 111078/001 | col2 = Saldos inmovilizados de depósitos judiciales a la vista y a plazo
Fila 4: col1 = 111081/001 | col2 = Saldos inmovilizados de depósitos sujetos al Aporte al Fondo de Garantía de los depósitos y computables para Aplicación de recursos
Fila 5: col1 = 111082/001 | col2 = Saldos inmovilizados de depósitos sujetos al Aporte al Fondo de Garantía de los depósitos y no computables para Aplicación de recursos
Fila 6: col1 = 111083/001 | col2 = Saldos inmovilizados de depósitos no sujetos al Aporte al Fondo de Garantía de los depósitos y computables para Aplicación de recursos
Fila 7: col1 = 111084/001 | col2 = Saldos inmovilizados de depósitos no sujetos al Aporte al Fondo de Garantía de los depósitos y no computables para Aplicación de recursos
Fila 8: col1 = 120500/001 | col2 = Saldos inmovilizados de depósitos de títulos privados y públicos (excepto nacionales)
Fila 9: col1 = 11120X/001 | col2 = Depósitos a plazo fijo de títulos valores privados
Fila 10: col1 = 11121X/001 | col2 = Obligaciones por “aceptaciones”
Fila 11: col1 = 11122X/001 | col2 = Pases pasivos de títulos valores
Fila 12: col1 = 11124X/001 | col2 = Cauciones y pases bursátiles de títulos valores
Fila 13: col1 = 11127X/001 | col2 = Otros depósitos a plazo
Fila 14: col1 = 11128X/001 | col2 = Otras obligaciones a plazo
Fila 15: col1 = 12010X/001 | col2 = Depósitos a plazo de títulos valores públicos (excepto nacionales)
Fila 16: col1 = 11140X/001 | col2 = Depósitos a plazo fijo
Fila 17: col1 = 11141X/001 | col2 = Inversiones a plazo constante
Fila 18: col1 = 11142X/001 | col2 = Inversiones con opción de cancelación anticipada
Fila 19: col1 = 11143X/001 | col2 = Inversiones con opción de renovación por plazo determinado
Fila 20: col1 = 11144X/001 | col2 = Inversiones a plazo con retribución variable
Fila 21: col1 = 111490/001 | col2 = Inversiones -correspondientes a titulares del sector público- con opción de cancelación anticipada para el inversor
Fila 22: col1 = 111460/001 | col2 = Depósitos judiciales a plazo fijo
Fila 23: col1 = 11171X/001 | col2 = Depósitos reprogramados “CEDROS”
Fila 24: col1 = 11175X/001 | col2 = Depósitos a plazo fijo con cláusula CER
Fila 25: col1 = 11180X/001 | col2 = Títulos Valores de Deuda
Fila 26: col1 = 112010/001 | col2 = Depósitos en cuenta corriente
Fila 27: col1 = 112020/001 | col2 = Depósitos en cuentas corrientes especiales para personas jurídicas
Fila 28: col1 = 112030/001 | col2 = Depósitos en cajas de ahorro y usuras pupilares
Fila 29: col1 = 112035/001 | col2 = Depósitos judiciales en cuentas a la vista
Fila 30: col1 = 112040/001 | col2 = Cuentas especiales para círculos cerrados
Fila 31: col1 = 112045/001 | col2 = Depósitos en Cuentas Sueldo y Previsionales
Fila 32: col1 = 112070/001 | col2 = Otros depósitos a la vista
Fila 33: col1 = 112080/001 | col2 = Otras obligaciones a la vista
Fila 34: col1 = 112100/001 | col2 = Saldos sin utilizar de adelantos en cuenta corriente formalizados
Fila 35: col2 = PARTIDAS COMPRENDIDAS DE DEPÓSITOS A PLAZO FIJO POR ESPECIE DE TÍTULOS VALORES PÚ- BLICOS NACIONALES E INSTRUMENTOS DE REGULACIÓN MONETARIA DEL BCRA
Fila 36: col1 = 310050/TP | col2 = Saldos Inmovilizados por depósitos de títulos valores públicos nacionales e instrumentos de regulación monetaria del BCRA constituidos hasta el 30.09.07
Fila 37: col1 = 310055/TP | col2 = Saldos Inmovilizados por depósitos de títulos valores públicos nacionales e instrumentos de regulación monetaria del BCRA constituidos a partir del 1.10.07
Fila 38: col1 = 31010X/TP | col2 = Depósitos de títulos valores públicos nacionales e instrumentos de regulación monetaria del BCRA constituidos hasta el 30.09.07
Fila 39: col1 = 31020X/TP | col2 = Depósitos de títulos valores públicos nacionales e instrumentos de regulación monetaria del BCRA constituidos a partir del 1.10.07.
Fila 40: col1 = 310300/TP | col2 = Depósitos judiciales de títulos valores públicos nacionales e instrumentos de regulación monetaria del BCRA cons- tituidos hasta el 30.09.07
Fila 41: col1 = 310400/TP | col2 = Depósitos judiciales de títulos valores públicos nacionales e instrumentos de regulación monetaria del BCRA cons- tituidos a partir del 1.10.07
[FIN TABLA ri_rml::tabla025]
Al respecto, se aclara que deberán considerar los numerales de ese período divi-
dido por 31:
∑ Saldos diarios de los días 1 al 15
_________________________________________________
31
Estas partidas, mantendrán las correlaciones con cuentas de balance definidas pa-
ra los códigos de similar concepto previstos en el modelo de información del pun-
to 1.10.1. del presente régimen.
b) Para el subperíodo comprendido entre el 16/08 y 31/08 el modelo de informa-
ción a utilizar será el del punto 1.10.1. del presente régimen, considerando los
numerales de ese período dividido por 31.
∑ Saldos diarios de los días 16 al 31
_________________________________________________
31
11.1.2 Exigencia mínima diaria.
[TABLA ri_rml::tabla026 | página 50 | e0_tablas | columnas]
Columnas: Período | Tramo de tasa | Exigencias mínimas diarias | Partidas | Base de cómputo
Fila 1: Período = Agosto/18 | Tramo de tasa = 01/08/18 a 15/08/18 | Exigencias mínimas diarias = Exigencia mínima diaria | Partidas = 451000 | Base de cómputo = julio 2018
Fila 2: Período = Agosto/18 ⟨combinada con fila 1⟩ | Tramo de tasa = 01/08/18 a 15/08/18 ⟨combinada con fila 1⟩ | Exigencias mínimas diarias = Exigencia mínima diaria so- bre depósitos y obligaciones a plazo | Partidas = 451200 | Base de cómputo = julio 2018 ⟨combinada con fila 1⟩
Fila 3: Período = Agosto/18 ⟨combinada con fila 1⟩ | Tramo de tasa = 16/08/18 a 31/08/18 | Exigencias mínimas diarias = Exigencia mínima diaria | Partidas = 451099 | Base de cómputo = julio 2018 recalculada en función de las ta- sas previstas en el punto 1. de la Comu- nicación “A” 6550
Fila 4: Período = Agosto/18 ⟨combinada con fila 1⟩ | Tramo de tasa = 16/08/18 a 31/08/18 ⟨combinada con fila 3⟩ | Exigencias mínimas diarias = Exigencia mínima diaria so- bre depósitos y obligaciones a plazo | Partidas = 451299 | Base de cómputo = julio 2018 recalculada en función de las ta- sas previstas en el punto 1. de la Comu- nicación “A” 6550 ⟨combinada con fila 3⟩
[FIN TABLA ri_rml::tabla026]
11.1.3 Cómputo del incremento de exigencia derivado del aumento de tasas.
No se admitirá integrar con bonos los incrementos de exigencia que surjan de
aplicar el efectivo mínimo vigente al 16/08 respecto del vigente al 15/08, debien-
do ser cubiertos con los conceptos de integración previstos con carácter gene-
ral.
11.1.4 Código 903200/001 - Exigencia del mes sobre los depósitos y obligaciones a
plazo en pesos.
Además de las partidas indicadas en el punto 1.9.1. Totales de control, corres-
ponderá considerar los códigos de los conceptos equivalentes a plazo defini-
dos en la tabla del apartado a).
11.1.5 Cálculo del aporte al Fondo de Garantía de los Depósitos.
Además de las partidas indicadas en la Sección 2. Base de cálculo, correspon-
derá considerar los códigos de los conceptos equivalentes definidos en la tabla
del apartado a).
Las entidades B y C reportarán el modelo de información del punto 1.10.1. para todo el
mes bajo informe
12. Instrucciones particulares para las entidades definidas en las Comunicaciones “A” 6556 y
6569. Integración de los incrementos de tasa del efectivo mínimo en pesos con “Letras
de liquidez bancaria (LELIQ) y/o Notas del BCRA (NOBAC)”.
12.1. Posición en promedio
12.1.1. Código 210106/TP
Las entidades comprendidas informarán la porción de los saldos promedio
de las “Letras de liquidez bancaria (LELIQ) y/o Notas del BCRA (NOBAC)”
depositados en la “Subcuenta 60 efectivo mínimo”, habilitada en la “Central
de Registro y Liquidación de Pasivos Públicos y Fideicomisos Financieros -
CRYL”, que se aplique a integrar el incremento de exigencia resultante de
computar en cada posición el incremento de tasas de efectivo mínimo en pe-
sos, admitidos en las normas sobre “Efectivo mínimo”.
Esta partida se identificará con el código TP correspondiente a los títulos ci-
tados. Para el caso de las LELIQ se integrará con el código 13000.
Los saldos consignados en el código 210106 son una aplicación específica
del total de las tenencias informadas en la partida 210100 para dicho TP, y
por tanto, sus saldos se encuentran incluidos en esta última partida, así co-
mo también en el correspondiente código 500000.
12.1.2. Código 825000/001
Se consignará el incremento en la exigencia proveniente del aumento en las
tasas de efectivo, integrable con Leliq y/o Nobac, según lo especificado en
las normas sobre “Efectivo mínimo”.
12.1.3. Modelo de información.
[TABLA ri_rml::tabla027 | página 51 | e0_tablas | columnas]
Columnas: Partida | Concepto | Criterio de cómputo
Fila 1: Partida = 825000/001 | Concepto = Incremento en la exigencia integrable con bonos | Criterio de cómputo = Se informarán los incrementos provenientes del au- mento en las tasas específicamente admitidos por las normas sobre “Efectivo mínimo”.
Fila 2: Partida = 210106/TP | Concepto = Aplicación de Leliq y/o Nobac deposita- dos en la CRyL | Criterio de cómputo = Porción pertinente del importe informado en partidas 210100/TP y 500000/TP Código 210106/TP ≤ Código 825000/001
[FIN TABLA ri_rml::tabla027]
12.1.4. Control del código 210100/TP a partir de septiembre/18.
Para efectuar el control previsto en los puntos 1.3. y 1.9.2. sobre la partida
210100, se detraerán de esta última los saldos del código 210105 y 210106,
quedando redefinido de la forma siguiente:
∑Código 210100/TP - Código 210105/TP - Código 210106/TP ≤ (∑ Código
11010X/001 * em(n) + ∑Código 10120X/001 * em(n) + Código 110500/001 *
em(n))
12.2. Posición diaria
Las partidas 4520XX incluirán, a partir del 01/09/18, de corresponder, la apli-
cación de la integración en letras de liquidez bancaria (Leliq) y/o notas del
BCRA (Nobac), hasta el límite del aumento de exigencia por el incremento de
las tasas referido.
Instrucciones particulares para las Entidades Grupo “A” y entidades con de-
pósitos del SPNF al cierre del mes de julio de 2018 ≥ 1% del total de los mis-
mos en el sistema financiero durante julio/18.
```

Versión: primer intento (cola). Entidades 23, relaciones 25.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Régimen Informativo - Efectivo Mínimo", "properties": {}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Operacion", "label": "Determinación estructura plazos residuales depósitos plazo fijo", "properties": {"tipo": "Cálculo de estructura de plazos", "descripcion": "Determinación de la estructura de plazos residuales para depósitos a plazo fijo de agosto/18 considerando conceptos informados en julio/18 en códigos específicos de partida"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- {"local_id": "e2", "type": "Operacion", "label": "Cálculo Código 824000/TP - Efectivo mínimo", "properties": {"tipo": "Cálculo de partida contable", "descripcion": "Cálculo del Código 824000/TP para agosto/18 aplicando tasas de Comunicaciones A 6526 y A 6532, basado en saldos promedio y diferencias porcentuales de efectivo mínimo"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- {"local_id": "e3", "type": "Operacion", "label": "Cálculo Código 210105/TP - Vigencia continuada", "properties": {"tipo": "Vigencia de partidas", "descripcion": "Las partidas 824000/001 y 210105/TP mantienen vigencia para agosto/18 y meses subsiguientes"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- {"local_id": "e4", "type": "Obligacion", "label": "Cálculo numerales período dividido por 31 (01/08-15/08)", "properties": {"tipo": "calculo", "descripcion": "Las entidades deberán considerar los numerales del período 01/08 a 15/08 dividido por 31, calculando la suma de saldos diarios de los días 1 al 15 dividida por 31", "umbrales": "dividido por 31"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- {"local_id": "e5", "type": "Obligacion", "label": "Cálculo numerales período dividido por 31 (16/08-31/08)", "properties": {"tipo": "calculo", "descripcion": "Las entidades deberán utilizar el modelo de información del punto 1.10.1 para el período 16/08 a 31/08, considerando los numerales dividido por 31, calculando la suma de saldos diarios de los días 16 al 31 dividida por 31", "umbrales": "dividido por 31"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_do
- {"local_id": "e6", "type": "Restriccion", "label": "Prohibición integración bonos incrementos exigencia tasa", "properties": {"tipo": "prohibicion", "descripcion": "No se admitirá integrar con bonos los incrementos de exigencia derivados del aumento de tasas de efectivo mínimo entre el 15/08 y el 16/08; deben cubrirse con conceptos de integración de carácter general"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo":
- {"local_id": "e7", "type": "Obligacion", "label": "Consideración códigos equivalentes plazo Código 903200/001", "properties": {"tipo": "calculo", "descripcion": "Para el Código 903200/001 (Exigencia del mes sobre depósitos y obligaciones a plazo en pesos), las entidades deberán considerar además de las partidas del punto 1.9.1 los códigos de conceptos equivalentes a plazo definidos en la tabla del apartado a)"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_d
- {"local_id": "e8", "type": "Obligacion", "label": "Consideración códigos equivalentes Fondo Garantía Depósitos", "properties": {"tipo": "calculo", "descripcion": "Para el cálculo del aporte al Fondo de Garantía de los Depósitos, las entidades deberán considerar además de las partidas de la Sección 2 los códigos de conceptos equivalentes definidos en la tabla del apartado a)"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice
- {"local_id": "e9", "type": "Obligacion", "label": "Reporte modelo información punto 1.10.1 entidades B y C", "properties": {"tipo": "presentacion_informativa", "descripcion": "Las entidades B y C deberán reportar el modelo de información del punto 1.10.1 para todo el mes bajo informe"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 9}
- {"local_id": "e10", "type": "Obligacion", "label": "Información porción saldos promedio LELIQ/NOBAC Código 210106/TP", "properties": {"tipo": "presentacion_informativa", "descripcion": "Las entidades comprendidas deberán informar la porción de saldos promedio de LELIQ y/o NOBAC depositados en la Subcuenta 60 efectivo mínimo de la CRYL que se aplique a integrar el incremento de exigencia por aumento de tasas de efectivo mínimo en pesos"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "p
- {"local_id": "e11", "type": "Obligacion", "label": "Identificación partida 210106 con código TP títulos", "properties": {"tipo": "asignacion", "descripcion": "La partida 210106 se identificará con el código TP correspondiente a los títulos (LELIQ o NOBAC); para LELIQ se utilizará el código 13000"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 11}
- {"local_id": "e12", "type": "Definicion", "label": "Relación partida 210106 con 210100 y 500000", "properties": {"termino": "Código 210106", "descripcion": "Los saldos del código 210106 constituyen una aplicación específica del total de tenencias de la partida 210100 para el TP correspondiente, estando incluidos en 210100 y en el código 500000"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 12}
- {"local_id": "e13", "type": "Obligacion", "label": "Consignación incremento exigencia Código 825000/001", "properties": {"tipo": "asignacion", "descripcion": "Se deberá consignar el incremento en la exigencia proveniente del aumento en las tasas de efectivo, integrable con Leliq y/o Nobac, conforme a las normas sobre Efectivo mínimo"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 13}
- {"local_id": "e14", "type": "Obligacion", "label": "Información incrementos exigencia Código 825000/001", "properties": {"tipo": "presentacion_informativa", "descripcion": "Se deberá informar los incrementos en la exigencia provenientes del aumento en las tasas de efectivo específicamente admitidos por las normas sobre Efectivo mínimo"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 14}
- {"local_id": "e15", "type": "Restriccion", "label": "Límite aplicación Leliq/Nobac Código 210106/TP", "properties": {"tipo": "limite_cuantitativo", "descripcion": "La aplicación de Leliq y/o Nobac en el código 210106/TP no puede exceder el incremento de exigencia del código 825000/001", "umbrales": "Código 210106/TP ≤ Código 825000/001"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 15}
- {"local_id": "e16", "type": "Obligacion", "label": "Control partida 210100/TP deducción 210105 y 210106", "properties": {"tipo": "calculo", "descripcion": "Para el control de la partida 210100/TP a partir de septiembre/18, se detraerán los saldos de los códigos 210105 y 210106, quedando redefinida la partida como: suma de 210100/TP menos 210105/TP menos 210106/TP, que debe ser menor o igual a la suma de códigos 11010X/001, 10120X/001 y 110500/001 multiplicados por el efectivo mínimo", "umbrales"
- {"local_id": "e17", "type": "Obligacion", "label": "Inclusión aplicación Leliq/Nobac partidas 4520XX", "properties": {"tipo": "asignacion", "descripcion": "A partir del 01/09/18, las partidas 4520XX deberán incluir la aplicación de integración en Leliq y/o Nobac, hasta el límite del aumento de exigencia por incremento de tasas", "umbrales": "a partir del 01/09/18 | hasta el límite del aumento de exigencia por el incremento de las tasas referido"}, "provenance": {"to": "ri_rml", "archivo": "ri_rm
- {"local_id": "c1", "type": "Comunicacion", "label": "Com. A 6526", "properties": {"codigo": "A-6526"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 18}
- {"local_id": "c2", "type": "Comunicacion", "label": "Com. A 6532", "properties": {"codigo": "A-6532"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 19}
- {"local_id": "c3", "type": "Comunicacion", "label": "Com. A 6550", "properties": {"codigo": "A-6550"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 20}
- {"local_id": "c4", "type": "Comunicacion", "label": "Com. A 6556", "properties": {"codigo": "A-6556"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 21}
- {"local_id": "c5", "type": "Comunicacion", "label": "Com. A 6569", "properties": {"codigo": "A-6569"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 22}
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e3", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e4", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- relación: {"source": "e5", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- relación: {"source": "e6", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- relación: {"source": "e7", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- relación: {"source": "e8", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 7}
- relación: {"source": "e9", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 8}
- relación: {"source": "e10", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 9}
- relación: {"source": "e11", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 10}
- relación: {"source": "e12", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 11}
- relación: {"source": "e13", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 12}
- relación: {"source": "e14", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 13}
- relación: {"source": "e15", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 14}
- relación: {"source": "e16", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 15}
- relación: {"source": "e17", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 16}
- relación: {"source": "to", "target": "c1", "predicate": "referencia", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 17}
- relación: {"source": "to", "target": "c2", "predicate": "referencia", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 18}
- relación: {"source": "to", "target": "c3", "predicate": "referencia", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 19}
- relación: {"source": "to", "target": "c4", "predicate": "referencia", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 20}
- relación: {"source": "to", "target": "c5", "predicate": "referencia", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 21}
- relación: {"source": "e4", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_rol_entidad_comprendida_reginf", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 22}
- relación: {"source": "e9", "target": null, "predicate": "aplica_a", "sujeto_id": null, "sujeto_propuesto": "Las entidades B y C", "sujeto_propuesto_padre_sugerido": "Sujeto_rol_entidad_comprendida_reginf", "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 23}
- relación: {"source": "e10", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_rol_entidad_comprendida_reginf", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 24}

## 11. `ri_rml::Sbloque14::parte4` — RI:resto · cola

Texto que vio E3 (e0_con_las_partes, bloque de lista True; págs. 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68):

```
[encabezado | punto S4]
Sección 4. Disposiciones transitorias
[encabezado | punto Sbloque14]
5. EFECTIVO MINIMO Y APLICACIÓN DE RECURSOS (R.I. – E.M.-A.R.)
[texto propio | punto Sbloque14]
21. Disminuciones de exigencia de EM en pesos (punto 7.2. de las Normas sobre “Efectivo míni-
mo”).
Código 708000/001
Se consignará el importe correspondiente a la deducción especial de la exigencia total, para enti-
dades “A” y sucursales o subsidiarias de G-SIB, de acuerdo con lo establecido en el punto 7.2.1.
de las normas sobre “Efectivo Mínimo”. Para ello se utilizará la siguiente metodología:
(812000/001 + 813000/001 ) * Coef.
(n) (n)
Donde: Coef. = % establecido normativamente para el cómputo de la disminución de exigencia por este concepto
Dicho importe de disminución no podrá superar el 2 % de los conceptos en pesos sujetos a exi-
gencia durante el período (n-1), de tal forma que:
Partida 708000/001 (n) = Menor [(812000/001(n) + 813000/001(n)) * Coef.; Partida 100000/001 (n-1) * 2 %]
Código 710000/001
Se informará el importe, correspondiente a la disminución de exigencia especial en el marco de
la emergencia sanitaria dispuesta por el Decreto N° 260/2020 y modificatorias, de acuerdo con lo
establecido en el punto 7.2.2. de las normas sobre “Efectivo mínimo”, que surja de los siguientes
cálculos:
DISM = (814000/001(n) + 828000/001(n) + 829000/001(n) * Coef.
Donde Coef. = % establecido normativamente para el cómputo de la disminución de exigencia por este concepto.
El importe a computar en la partida 710000/001 no podrá superar el 4 % de los conceptos en pe-
sos sujetos a exigencia durante el período (n-1), de manera que:
Partida 710000/001: Menor [ (814000/001(n) + 828000/001(n) + 829000/001(n)) * Coef; Partida
100000/001(n-1) * 4 %]
Si la disminución (DISM) supera el límite del 4%, el importe a computar en la partida 710000/001
podrá incrementarse considerando las siguientes expresiones:
A = [ (814000/001(n) + 828000/001(n) + 829000/001(n)) * Coef.] menos (Partida 100000/001(n-1) * 4
%).
B = (828000/001(n) + 829000/001(n)) * Coef.
C = Partida 100000/001(n-1) * 2 %
Si A > 0, entonces:
Partida 710000/001 = Menor [ (814000/001(n) + 828000/001(n) + 829000/001(n)) * Coef ; Partida
100000/001 (n-1) * 4 % ] + Menor (A;B;C)
Código 711000/001
Se informará el importe correspondiente a la disminución de exigencia especial por financiacio-
nes acordadas en el marco del Decreto N° 332/2020 (y modificatorios), de acuerdo con lo esta-
blecido en el punto 7.2.3. de las normas sobre “Efectivo mínimo”, calculado en función de la si-
guiente expresión:
Partida 711000/001(n) = [(816000/001(n) + 834000/001(n) + 835000/001(n)) * 60%] + (838000/001(n) * 24%)
Código 712000/001 (vigente hasta el 05/06/25)
Se informará el importe correspondiente a la disminución de exigencia por financiaciones otorga-
das a MiPyMES no informadas en la “Central de deudores del Sistema Financiero”, a una TNA
máxima del 24%, de acuerdo con lo establecido en el punto 7.2.4. de las normas sobre “Efectivo
mínimo”. Para ello se utilizará la siguiente expresión:
Partida 712000/001(n) = 823000/001(n) * 40 %
Código 715000/001
Se consignará el importe a deducir de la exigencia en promedio determinada para cada período,
en función de las financiaciones en pesos “Crédito a Tasa Cero 2021” otorgadas en el marco del
Decreto N° 512/21, de acuerdo con lo establecido en el punto 7.2.4. de las normas sobre “Efecti-
vo mínimo”, calculado en función de la siguiente expresión:
Partida 715000/001(n) = 853000/001(n) * 60 %
Código 812000/001
Se informará -hasta su cancelación- el saldo promedio mensual del mes anterior al bajo informe
de las financiaciones en pesos (Préstamos y Créditos por Arrendamientos Financieros) otorga-
das a MiPyMES hasta el 16/02/2020, a una TNA fija máxima del 40 %, teniendo en cuenta la de-
finición contenida en las normas sobre “Determinación de la condición de Micro, Pequeña y Me-
diana Empresa”.
Código 813000/001
Se informará el saldo promedio mensual del mes anterior al bajo informe de las financiaciones en
pesos (Préstamos y Créditos por Arrendamientos Financieros) otorgadas a MiPyMES a partir del
17/02/2020, a una TNA fija máxima del 35%, teniendo en cuenta la definición contenida en las
normas sobre “Determinación de la condición de Micro, Pequeña y Mediana Empresa”.
Código 814000/001
Se informará el saldo promedio mensual del mes anterior al bajo informe de las financiaciones en
pesos (Préstamos y Créditos por Arrendamientos Financieros) otorgadas a MiPyMES a partir del
20/03/2020, a una TNA fija máxima del 24%, teniendo en cuenta la definición contenida en las
normas sobre “Determinación de la condición de Micro, Pequeña y Mediana Empresa” y con des-
tino a líneas de capital de trabajo.
Código 815000/001 (vigente hasta el 05/06/25)
Se informará el saldo promedio mensual del mes anterior al bajo informe de las financiaciones en
pesos otorgadas a prestadores de servicios de salud humana, habilitados por el organismo com-
petente de la correspondiente jurisdicción a partir del 20/03/2020, a una TNA fija máxima del
24%, teniendo en cuenta la definición contenida el Decreto N° 260/2020 y sea destinado a la
compra de insumos y equipamiento médico.
Código 816000/001
Se informará el saldo promedio mensual del mes anterior al bajo informe de las financiaciones en
pesos otorgadas hasta el 05/11/2020 a tasa cero (0 %) acordadas en el marco del artículo 9° del
Decreto N° 332/2020 (y modificatorias).
Código 823000/001 (vigente hasta el 05/06/25)
Se informará el saldo promedio mensual del mes anterior al bajo informe de las financiaciones en
pesos (Préstamos y Créditos por Arrendamientos Financieros) otorgadas a MiPyMES no infor-
madas en la “Central de deudores del Sistema Financiero”, a partir del 11/5/2020, a una TNA fija
máxima del 24%, teniendo en cuenta la definición contenida en las normas sobre “Determinación
de la condición de Micro, Pequeña y Mediana Empresa”.
Código 827000/001 (vigente hasta el 05/06/25)
Se informará el saldo promedio mensual del mes anterior al bajo informe, de las financiaciones
en pesos otorgadas a clientes no MiPyMES, a partir del 01/07/2020, a una TNA fija máxima del
24%, en la medida que los fondos se destinen a la adquisición de maquinarias y equipos produ-
cidos por MiPyMEs locales.
Código 828000/001
Se informará el saldo promedio mensual del mes anterior al bajo informe, de las financiaciones
en pesos (Préstamos y Créditos por Arrendamientos Financieros) otorgadas a partir del
01/07/2020, a MiPyMES que recibieron los préstamos a que hace referencia el punto 7.2.2. de
las normas sobre “Efectivo mínimo”, por hasta el importe total equivalente a la masa salarial
mensual (sin aguinaldo) a pagar por el solicitante del préstamo.
Código 829000/001
Se informará el saldo promedio mensual del mes anterior al bajo informe de las financiaciones en
pesos (Préstamos y Créditos por Arrendamientos Financieros) otorgadas a MiPyMES a partir del
01/07/2020, a una TNA fija máxima del 24 %, teniendo en cuenta la definición contenida en las
normas sobre “Determinación de la condición de Micro, Pequeña y Mediana Empresa” y con des-
tino a líneas de capital de trabajo, en tanto se trate de clientes que no hayan recibido este tipo de
asistencia con anterioridad.
Código 830000/001 (vigente hasta el 05/06/25)
Se informará el saldo promedio mensual del mes anterior al bajo informe, de las financiaciones
en pesos otorgadas a prestadores de servicios de salud humana, habilitados por el organismo
competente de la correspondiente jurisdicción a partir del 01/07/2020, a una TNA fija máxima del
24 %, teniendo en cuenta la definición contenida el Decreto N° 260/2020 y sea destinado a la
compra de insumos y equipamiento médico, en tanto se trate de clientes que no hayan recibido
este tipo de asistencia con anterioridad.
Código 83100X/001 (vigente hasta el 31/12/22)
Se consignará el promedio mensual del total de retiros diarios de efectivo, correspondientes al
mes anterior al bajo informe, de cajeros automáticos ubicados en jurisdicciones que pertenezcan
a la categoría I, establecida en la Sección 2. de las normas sobre “Categorización de localidades
para entidades financieras”. Se utilizará X=1 para indicar que se trata de cajeros ubicados en las
casas operativas de la entidad, y X=2 para los que se encuentran fuera de ellas.
Código 83200X/001 (vigente hasta el 30/06/23)
Se consignará el promedio mensual del total de retiros diarios de efectivo, correspondientes al
mes anterior al bajo informe, de cajeros automáticos ubicados en jurisdicciones que pertenezcan
a la categoría II, establecida en la Sección 2. de las normas sobre “Categorización de localidades
para entidades financieras”.
Se utilizará X=1 para indicar que se trata de cajeros ubicados en las casas operativas de la entidad,
y X=2 para los que se encuentran fuera de ellas.
Código 834000/001
Se informará el saldo promedio mensual del mes anterior al bajo informe de las financiaciones en
pesos, otorgadas hasta el 05.11.2020 a “tasa subsidiada a empresas”, acordadas en el marco del
Decreto Nº 332/2020 (y modificatorios), siempre que estén comprendidas en el listado de beneficia-
rios que dé a conocer la ARCA.
Código 835000/001
Se informará el saldo promedio mensual del mes anterior al bajo informe de las financiaciones en
pesos otorgadas hasta el 05.11.2020 a “tasa cero (0 %) para cultura” acordadas en el marco del
Decreto Nº 332/2020 (y modificatorios), siempre que no hayan accedido a los “Créditos a Tasa Ce-
ro” y estén comprendidos en el listado de beneficiarios que dé a conocer la ARCA.
Código 838000/001
Se informará el saldo promedio mensual del mes anterior al bajo informe de las financiaciones en
pesos otorgadas a partir del 06.11.2020 a “tasa subsidiada para empresas”, acordadas en el marco
del Decreto Nº 332/2020 (y modificatorios) a una tasa nominal anual del 27 %.
Código 839000/001 (vigente hasta el 05/06/25)
Se informará el saldo promedio mensual del mes anterior al bajo informe de las financiaciones en
pesos otorgadas a partir del 06.11.2020 a “tasa subsidiada para empresas” acordadas en el marco
del Decreto Nº 332/2020 (y modificatorios) a una tasa nominal anual del 33 %.
Código 853000/001
Se informará el saldo promedio mensual del mes anterior al bajo informe de las financiaciones en
pesos “Crédito a Tasa Cero 2021” otorgadas en el marco del Decreto Nº 512/21.
Las financiaciones a ser informadas en los códigos 812000/001, 813000/001, 814000/001,
816000/001, 828000/001, 829000/001, 834000/001, 835000/001, 838000/001, 853000/001 podrán
ser computadas sólo en una de dichas partidas, y consecuentemente, en las de las disminuciones
de exigencia informadas en las partidas 708000/001, 710000/001, 711000/001 y 715000/001.
Las financiaciones desembolsadas a partir del 09.10.2020 y hasta 15.10.2020, en ambos casos
inclusive, no podrán ser computadas en las partidas 708000/001 y 710000/001, cuando las mismas
se otorguen a personas humanas o jurídicas, que pertenezcan a sectores que no hayan sido consi-
derados elegibles para alguno de los beneficios del Programa ATP y/o con posterioridad al
19.03.20, hayan importado bienes de consumo finales, excepto productos y/o insumos médicos. Las
financiaciones que se otorguen a partir del 06.11.2020 inclusive, serán voluntarias y no podrán
computarse en las partidas 708000/001, 710000/001.
22. Exigencia mínima diaria. (Abril 2024)
Se utilizarán los siguientes códigos de partidas según el tramo de tasas considerado, de
acuerdo con lo establecido en la Comunicación “A” 7988.
[TABLA ri_rml::tabla034 | página 66 | e0_tablas | columnas]
Columnas: Período | Tramo de tasa | Exigencias mínimas diarias | Partidas | Base de cómputo
Fila 1: Período = Abril 2024 | Tramo de tasa = 1.4.24 a 14.4.24 | Exigencias mínimas diarias = Exigencia mínima diaria | Partidas = 451099 | Base de cómputo = Marzo 2024
Fila 2: Período = Abril 2024 ⟨combinada con fila 1⟩ | Tramo de tasa = 15.4.24 a 30.4.24 | Exigencias mínimas diarias = Exigencia mínima diaria | Partidas = 451000 | Base de cómputo = Marzo 2024 recal- culada en función de las tasas previs- tas en la Comunica- ción “A” 7988.
[FIN TABLA ri_rml::tabla034]
```

Versión: primer intento (cola). Entidades 33, relaciones 36.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Régimen Informativo - Efectivo Mínimo", "properties": {}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Operacion", "label": "Cálculo disminución exigencia EM pesos (708000/001)", "properties": {"tipo": "Cálculo de disminución de exigencia", "descripcion": "Deducción especial de la exigencia total de efectivo mínimo en pesos para entidades \"A\" y sucursales o subsidiarias de G-SIB, calculada mediante la fórmula (812000/001 + 813000/001) * Coef., donde Coef. es el porcentaje establecido normativamente. El importe no podrá superar el 2% de los conceptos en pesos sujetos 
- {"local_id": "e2", "type": "Restriccion", "label": "Tope 2% — disminución exigencia 708000/001", "properties": {"tipo": "limite_cuantitativo", "descripcion": "El importe de disminución de exigencia en la partida 708000/001 no podrá superar el 2% de los conceptos en pesos sujetos a exigencia durante el período anterior.", "umbrales": "no podrá superar el 2 %"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- {"local_id": "e3", "type": "Operacion", "label": "Cálculo disminución exigencia EM emergencia sanitaria (710000/001)", "properties": {"tipo": "Cálculo de disminución de exigencia", "descripcion": "Disminución de exigencia especial en el marco de la emergencia sanitaria (Decreto N° 260/2020 y modificatorias), calculada mediante la fórmula DISM = (814000/001(n) + 828000/001(n) + 829000/001(n)) * Coef., donde Coef. es el porcentaje establecido normativamente."}, "provenance": {"to": "ri_rml", "arch
- {"local_id": "e4", "type": "Restriccion", "label": "Tope 4% — disminución exigencia 710000/001", "properties": {"tipo": "limite_cuantitativo", "descripcion": "El importe a computar en la partida 710000/001 no podrá superar el 4% de los conceptos en pesos sujetos a exigencia durante el período anterior.", "umbrales": "no podrá superar el 4 %"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- {"local_id": "e5", "type": "Condicion", "label": "Condición: DISM supera límite 4%", "properties": {"descripcion": "Cuando la disminución calculada (DISM) supera el límite del 4% de los conceptos en pesos sujetos a exigencia.", "umbrales": "supera el límite del 4%"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- {"local_id": "e6", "type": "Operacion", "label": "Cálculo incremento partida 710000/001 (condicionado)", "properties": {"tipo": "Cálculo de incremento condicional", "descripcion": "Cuando DISM supera el 4%, el importe a computar en la partida 710000/001 podrá incrementarse mediante el cálculo del menor entre A, B y C, donde A es el exceso sobre el límite del 4%, B es el componente de financiaciones de emergencia sanitaria, y C es el 2% de la base."}, "provenance": {"to": "ri_rml", "archivo": "ri
- {"local_id": "e7", "type": "Operacion", "label": "Cálculo disminución exigencia Decreto 332/2020 (711000/001)", "properties": {"tipo": "Cálculo de disminución de exigencia", "descripcion": "Disminución de exigencia especial por financiaciones acordadas en el marco del Decreto N° 332/2020 y modificatorios, calculada como la suma de: 60% de las financiaciones a tasa cero y tasa subsidiada para empresas y cultura, más 24% de las financiaciones a tasa subsidiada para empresas a partir del 06.11.2020
- {"local_id": "e8", "type": "Operacion", "label": "Cálculo disminución exigencia MiPyMES no informadas (712000/001)", "properties": {"tipo": "Cálculo de disminución de exigencia", "descripcion": "Disminución de exigencia por financiaciones otorgadas a MiPyMES no informadas en la Central de deudores del Sistema Financiero, a una TNA máxima del 24%, calculada como el 40% del saldo promedio mensual de tales financiaciones. Vigente hasta el 05/06/25."}, "provenance": {"to": "ri_rml", "archivo": "ri_r
- {"local_id": "e9", "type": "Restriccion", "label": "Límite TNA 24% — financiaciones MiPyMES 712000/001", "properties": {"tipo": "limite_cuantitativo", "descripcion": "Las financiaciones otorgadas a MiPyMES no informadas en la Central de deudores están limitadas a una Tasa Nominal Anual máxima del 24%.", "umbrales": "TNA máxima del 24%"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 9}
- {"local_id": "e10", "type": "Operacion", "label": "Cálculo deducción exigencia Crédito Tasa Cero 2021 (715000/001)", "properties": {"tipo": "Cálculo de deducción de exigencia", "descripcion": "Deducción de la exigencia en promedio por financiaciones en pesos \"Crédito a Tasa Cero 2021\" otorgadas en el marco del Decreto N° 512/21, calculada como el 60% del saldo promedio mensual de tales financiaciones."}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documen
- {"local_id": "e11", "type": "Definicion", "label": "Código 812000/001 — financiaciones MiPyMES hasta 16/02/2020", "properties": {"termino": "Código 812000/001", "descripcion": "Saldo promedio mensual del mes anterior al bajo informe de las financiaciones en pesos (Préstamos y Créditos por Arrendamientos Financieros) otorgadas a MiPyMES hasta el 16/02/2020, a una TNA fija máxima del 40%, conforme a la definición de MiPyME contenida en las normas sobre \"Determinación de la condición de Micro, Peq
- {"local_id": "e12", "type": "Definicion", "label": "Código 813000/001 — financiaciones MiPyMES desde 17/02/2020", "properties": {"termino": "Código 813000/001", "descripcion": "Saldo promedio mensual del mes anterior al bajo informe de las financiaciones en pesos (Préstamos y Créditos por Arrendamientos Financieros) otorgadas a MiPyMES a partir del 17/02/2020, a una TNA fija máxima del 35%, conforme a la definición de MiPyME contenida en las normas sobre \"Determinación de la condición de Micro,
- {"local_id": "e13", "type": "Definicion", "label": "Código 814000/001 — financiaciones MiPyMES desde 20/03/2020 capital trabajo", "properties": {"termino": "Código 814000/001", "descripcion": "Saldo promedio mensual del mes anterior al bajo informe de las financiaciones en pesos (Préstamos y Créditos por Arrendamientos Financieros) otorgadas a MiPyMES a partir del 20/03/2020, a una TNA fija máxima del 24%, con destino a líneas de capital de trabajo, conforme a la definición de MiPyME contenida e
- {"local_id": "e14", "type": "Definicion", "label": "Código 815000/001 — financiaciones prestadores salud (vigente hasta 05/06/25)", "properties": {"termino": "Código 815000/001", "descripcion": "Saldo promedio mensual del mes anterior al bajo informe de las financiaciones en pesos otorgadas a prestadores de servicios de salud humana, habilitados por el organismo competente de la correspondiente jurisdicción a partir del 20/03/2020, a una TNA fija máxima del 24%, con destino a la compra de insumo
- {"local_id": "e15", "type": "Definicion", "label": "Código 816000/001 — financiaciones tasa cero Decreto 332/2020", "properties": {"termino": "Código 816000/001", "descripcion": "Saldo promedio mensual del mes anterior al bajo informe de las financiaciones en pesos otorgadas hasta el 05/11/2020 a tasa cero (0%) acordadas en el marco del artículo 9° del Decreto N° 332/2020 y modificatorias."}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_p
- {"local_id": "e16", "type": "Definicion", "label": "Código 823000/001 — financiaciones MiPyMES no informadas (vigente hasta 05/06/25)", "properties": {"termino": "Código 823000/001", "descripcion": "Saldo promedio mensual del mes anterior al bajo informe de las financiaciones en pesos (Préstamos y Créditos por Arrendamientos Financieros) otorgadas a MiPyMES no informadas en la Central de deudores del Sistema Financiero, a partir del 11/5/2020, a una TNA fija máxima del 24%, conforme a la definic
- {"local_id": "e17", "type": "Definicion", "label": "Código 827000/001 — financiaciones maquinarias MiPyMEs (vigente hasta 05/06/25)", "properties": {"termino": "Código 827000/001", "descripcion": "Saldo promedio mensual del mes anterior al bajo informe de las financiaciones en pesos otorgadas a clientes no MiPyMES, a partir del 01/07/2020, a una TNA fija máxima del 24%, con destino a la adquisición de maquinarias y equipos producidos por MiPyMEs locales. Vigente hasta el 05/06/25."}, "provenance
- {"local_id": "e18", "type": "Definicion", "label": "Código 828000/001 — financiaciones MiPyMES emergencia sanitaria", "properties": {"termino": "Código 828000/001", "descripcion": "Saldo promedio mensual del mes anterior al bajo informe de las financiaciones en pesos (Préstamos y Créditos por Arrendamientos Financieros) otorgadas a partir del 01/07/2020 a MiPyMES que recibieron préstamos en el marco de la emergencia sanitaria, por hasta el importe total equivalente a la masa salarial mensual (si
- {"local_id": "e19", "type": "Definicion", "label": "Código 829000/001 — financiaciones MiPyMES capital trabajo desde 01/07/2020", "properties": {"termino": "Código 829000/001", "descripcion": "Saldo promedio mensual del mes anterior al bajo informe de las financiaciones en pesos (Préstamos y Créditos por Arrendamientos Financieros) otorgadas a MiPyMES a partir del 01/07/2020, a una TNA fija máxima del 24%, con destino a líneas de capital de trabajo, para clientes que no hayan recibido este tipo 
- {"local_id": "e20", "type": "Definicion", "label": "Código 830000/001 — financiaciones prestadores salud desde 01/07/2020 (vigente hasta 05/06/25)", "properties": {"termino": "Código 830000/001", "descripcion": "Saldo promedio mensual del mes anterior al bajo informe de las financiaciones en pesos otorgadas a prestadores de servicios de salud humana, habilitados por el organismo competente de la correspondiente jurisdicción a partir del 01/07/2020, a una TNA fija máxima del 24%, con destino a la
- {"local_id": "e21", "type": "Definicion", "label": "Código 83100X/001 — retiros cajeros automáticos categoría I (vigente hasta 31/12/22)", "properties": {"termino": "Código 83100X/001", "descripcion": "Promedio mensual del total de retiros diarios de efectivo del mes anterior al bajo informe de cajeros automáticos ubicados en jurisdicciones de categoría I. X=1 para cajeros en casas operativas de la entidad; X=2 para cajeros fuera de ellas. Vigente hasta el 31/12/22."}, "provenance": {"to": "ri_r
- {"local_id": "e22", "type": "Definicion", "label": "Código 83200X/001 — retiros cajeros automáticos categoría II (vigente hasta 30/06/23)", "properties": {"termino": "Código 83200X/001", "descripcion": "Promedio mensual del total de retiros diarios de efectivo del mes anterior al bajo informe de cajeros automáticos ubicados en jurisdicciones de categoría II. X=1 para cajeros en casas operativas de la entidad; X=2 para cajeros fuera de ellas. Vigente hasta el 30/06/23."}, "provenance": {"to": "ri
- {"local_id": "e23", "type": "Definicion", "label": "Código 834000/001 — financiaciones tasa subsidiada empresas Decreto 332/2020", "properties": {"termino": "Código 834000/001", "descripcion": "Saldo promedio mensual del mes anterior al bajo informe de las financiaciones en pesos otorgadas hasta el 05.11.2020 a \"tasa subsidiada a empresas\" acordadas en el marco del Decreto N° 332/2020 y modificatorios, siempre que estén comprendidas en el listado de beneficiarios que dé a conocer la ARCA."}, "
- {"local_id": "e24", "type": "Definicion", "label": "Código 835000/001 — financiaciones tasa cero cultura Decreto 332/2020", "properties": {"termino": "Código 835000/001", "descripcion": "Saldo promedio mensual del mes anterior al bajo informe de las financiaciones en pesos otorgadas hasta el 05.11.2020 a \"tasa cero (0%) para cultura\" acordadas en el marco del Decreto N° 332/2020 y modificatorios, siempre que no hayan accedido a los \"Créditos a Tasa Cero\" y estén comprendidas en el listado de
- {"local_id": "e25", "type": "Definicion", "label": "Código 838000/001 — financiaciones tasa subsidiada empresas desde 06.11.2020", "properties": {"termino": "Código 838000/001", "descripcion": "Saldo promedio mensual del mes anterior al bajo informe de las financiaciones en pesos otorgadas a partir del 06.11.2020 a \"tasa subsidiada para empresas\" acordadas en el marco del Decreto N° 332/2020 y modificatorios, a una tasa nominal anual del 27%."}, "provenance": {"to": "ri_rml", "archivo": "ri_rm
- {"local_id": "e26", "type": "Definicion", "label": "Código 839000/001 — financiaciones tasa subsidiada empresas 33% (vigente hasta 05/06/25)", "properties": {"termino": "Código 839000/001", "descripcion": "Saldo promedio mensual del mes anterior al bajo informe de las financiaciones en pesos otorgadas a partir del 06.11.2020 a \"tasa subsidiada para empresas\" acordadas en el marco del Decreto N° 332/2020 y modificatorios, a una tasa nominal anual del 33%. Vigente hasta el 05/06/25."}, "provenan
- {"local_id": "e27", "type": "Definicion", "label": "Código 853000/001 — Crédito Tasa Cero 2021", "properties": {"termino": "Código 853000/001", "descripcion": "Saldo promedio mensual del mes anterior al bajo informe de las financiaciones en pesos \"Crédito a Tasa Cero 2021\" otorgadas en el marco del Decreto N° 512/21."}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 27}
- {"local_id": "e28", "type": "Restriccion", "label": "Prohibición — computación múltiple códigos financiaciones", "properties": {"tipo": "prohibicion", "descripcion": "Las financiaciones informadas en los códigos 812000/001, 813000/001, 814000/001, 816000/001, 828000/001, 829000/001, 834000/001, 835000/001, 838000/001 y 853000/001 no pueden ser computadas en más de una partida; cada financiación se computa en una sola de ellas."}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "
- {"local_id": "e29", "type": "Restriccion", "label": "Prohibición — financiaciones 09.10.2020-15.10.2020 en 708000/001 y 710000/001", "properties": {"tipo": "prohibicion", "descripcion": "Las financiaciones desembolsadas entre el 09.10.2020 y el 15.10.2020 (ambos inclusive) no pueden ser computadas en las partidas 708000/001 y 710000/001 cuando se otorguen a personas humanas o jurídicas que pertenezcan a sectores no elegibles para beneficios del Programa ATP y/o que hayan importado bienes de cons
- {"local_id": "e30", "type": "Restriccion", "label": "Prohibición — financiaciones desde 06.11.2020 en 708000/001 y 710000/001", "properties": {"tipo": "prohibicion", "descripcion": "Las financiaciones otorgadas a partir del 06.11.2020 (inclusive) son voluntarias y no pueden ser computadas en las partidas 708000/001 y 710000/001.", "umbrales": "a partir del 06.11.2020 inclusive"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "ind
- {"local_id": "e31", "type": "Operacion", "label": "Cálculo exigencia mínima diaria abril 2024", "properties": {"tipo": "Cálculo de exigencia mínima diaria", "descripcion": "Cálculo de la exigencia mínima diaria para abril 2024 según el tramo de tasas, utilizando los códigos de partidas 451099 (para el período 1.4.24 a 14.4.24) y 451000 (para el período 15.4.24 a 30.4.24), con base de cómputo en marzo 2024, conforme a la Comunicación A 7988."}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pd
- {"local_id": "e32", "type": "Comunicacion", "label": "Com. A 7988", "properties": {"codigo": "A-7988"}, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 32}
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e2", "target": "e1", "predicate": "limita", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e3", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- relación: {"source": "e4", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- relación: {"source": "e4", "target": "e3", "predicate": "limita", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- relación: {"source": "e5", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- relación: {"source": "e6", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 7}
- relación: {"source": "e5", "target": "e6", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 8}
- relación: {"source": "e7", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 9}
- relación: {"source": "e8", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 10}
- relación: {"source": "e9", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 11}
- relación: {"source": "e9", "target": "e8", "predicate": "limita", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 12}
- relación: {"source": "e10", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 13}
- relación: {"source": "e11", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 14}
- relación: {"source": "e12", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 15}
- relación: {"source": "e13", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 16}
- relación: {"source": "e14", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 17}
- relación: {"source": "e15", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 18}
- relación: {"source": "e16", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 19}
- relación: {"source": "e17", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 20}
- relación: {"source": "e18", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 21}
- relación: {"source": "e19", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 22}
- relación: {"source": "e20", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 23}
- relación: {"source": "e21", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 24}
- relación: {"source": "e22", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 25}
- relación: {"source": "e23", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 26}
- relación: {"source": "e24", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 27}
- relación: {"source": "e25", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 28}
- relación: {"source": "e26", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 29}
- relación: {"source": "e27", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 30}
- relación: {"source": "e28", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 31}
- relación: {"source": "e29", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 32}
- relación: {"source": "e30", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 33}
- relación: {"source": "e31", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 34}
- relación: {"source": "to", "target": "e32", "predicate": "referencia", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "ri_rml", "archivo": "ri_rml.pdf", "punto": "Sbloque14", "rol_documental": "punto_propio"}, "indice_crudo": 35}

## 12. `depaho::1.3.5` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 5):

```
[encabezado | punto S1]
Sección 1. Caja de ahorros.
[encabezado | punto 1.3]
1.3. Identificación y situación fiscal del titular.
[intro | punto 1.3]
Se verificará a base de los documentos que deberán exhibir los titulares o –de corresponder–
sus apoderados o representantes legales (tutores, curadores, etc.), con ajuste a lo previsto en
los puntos 4.1. y 4.2.
Además, como mínimo, se exigirán los siguientes datos:
[texto propio | punto 1.3.5]
1.3.5. Estado civil.
```

Versión: primer intento (cola). Entidades 2, relaciones 1.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Depósitos de ahorro", "properties": {}, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "1.3.5", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Definicion", "label": "Estado civil — dato requerido", "properties": {"termino": "Estado civil", "descripcion": "Dato de identificación y situación fiscal del titular de la caja de ahorros que deberá ser acreditado conforme a lo previsto en el punto 1.3.5"}, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "1.3.5", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "1.3.5", "rol_documental": "punto_propio"}, "indice_crudo": 0}

## 13. `manori::1.2.10.2` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 24):

```
[encabezado | punto S1]
Sección 1. Manual de Originación y Administración de Préstamos Hipotecarios.
[encabezado | punto 1.2]
1.2. Originación de los préstamos hipotecarios.
[encabezado | punto 1.2.10]
1.2.10. Auditorías y control de calidad.
[texto propio | punto 1.2.10.2]
1.2.10.2. Requisitos.
El control de calidad debe incluir la revisión de una muestra estadísticamente
confiable de préstamos, cuya dimensión debe ser función del volumen total de
préstamos hipotecarios y de los niveles de riesgo. Dentro de la muestra, debe-
rá efectuarse:
i) La revisión de carpetas crediticias y legales, verificación de la existencia y
exactitud de la documentación referida a la propiedad y a aspectos crediti-
cios y legales.
ii) La evaluación de la calidad de la valuación de las propiedades.
iii) La evaluación de las decisiones crediticias.
iv) Inspecciones a propiedades a fin de comprobar el cumplimiento del destino
de los préstamos.
v) Solicitud de certificados de dominio a fin de comprobar el registro correcto
de las garantías hipotecarias.
El control de calidad debe ser constante y permanente, con un nivel de revisión
que asegure una confiabilidad estadística a la muestra que se realice.
```

Versión: primer intento (cola). Entidades 9, relaciones 16.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Manual de Originación y Administración de Préstamos Hipotecarios", "properties": {}, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.2.10.2", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Operacion", "label": "Control de calidad de préstamos hipotecarios", "properties": {"tipo": "revisión de muestra de préstamos", "descripcion": "Revisión de una muestra estadísticamente confiable de préstamos hipotecarios, cuya dimensión se determina en función del volumen total de préstamos y de los niveles de riesgo."}, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.2.10.2", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- {"local_id": "e2", "type": "Obligacion", "label": "Revisión de carpetas crediticias y legales", "properties": {"tipo": "presentacion_informativa", "descripcion": "Dentro de la muestra de control de calidad, deberá efectuarse la revisión de carpetas crediticias y legales, con verificación de la existencia y exactitud de la documentación referida a la propiedad y a aspectos crediticios y legales."}, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.2.10.2", "rol_documental": "pun
- {"local_id": "e3", "type": "Obligacion", "label": "Evaluación de calidad de valuación de propiedades", "properties": {"tipo": "calculo", "descripcion": "Dentro de la muestra de control de calidad, deberá efectuarse la evaluación de la calidad de la valuación de las propiedades."}, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.2.10.2", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- {"local_id": "e4", "type": "Obligacion", "label": "Evaluación de decisiones crediticias", "properties": {"tipo": "otra", "descripcion": "Dentro de la muestra de control de calidad, deberá efectuarse la evaluación de las decisiones crediticias."}, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.2.10.2", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- {"local_id": "e5", "type": "Obligacion", "label": "Inspecciones a propiedades para verificar destino de préstamos", "properties": {"tipo": "otra", "descripcion": "Dentro de la muestra de control de calidad, deberá efectuarse inspecciones a propiedades a fin de comprobar el cumplimiento del destino de los préstamos."}, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.2.10.2", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- {"local_id": "e6", "type": "Obligacion", "label": "Solicitud de certificados de dominio para garantías hipotecarias", "properties": {"tipo": "otra", "descripcion": "Dentro de la muestra de control de calidad, deberá efectuarse solicitud de certificados de dominio a fin de comprobar el registro correcto de las garantías hipotecarias."}, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.2.10.2", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- {"local_id": "e7", "type": "Obligacion", "label": "Control de calidad constante y permanente", "properties": {"tipo": "otra", "descripcion": "El control de calidad debe ser constante y permanente, con un nivel de revisión que asegure una confiabilidad estadística a la muestra que se realice.", "frecuencia": "constante y permanente"}, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.2.10.2", "rol_documental": "punto_propio"}, "indice_crudo": 7}
- {"local_id": "e8", "type": "Condicion", "label": "Dimensión de muestra función del volumen y riesgo", "properties": {"descripcion": "La dimensión de la muestra debe determinarse en función del volumen total de préstamos hipotecarios y de los niveles de riesgo."}, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.2.10.2", "rol_documental": "punto_propio"}, "indice_crudo": 8}
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.2.10.2", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.2.10.2", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e3", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.2.10.2", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e4", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.2.10.2", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- relación: {"source": "e5", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.2.10.2", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- relación: {"source": "e6", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.2.10.2", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- relación: {"source": "e7", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.2.10.2", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- relación: {"source": "e8", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.2.10.2", "rol_documental": "punto_propio"}, "indice_crudo": 7}
- relación: {"source": "e1", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.2.10.2", "rol_documental": "punto_propio"}, "indice_crudo": 8}
- relación: {"source": "e2", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.2.10.2", "rol_documental": "punto_propio"}, "indice_crudo": 9}
- relación: {"source": "e3", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.2.10.2", "rol_documental": "punto_propio"}, "indice_crudo": 10}
- relación: {"source": "e4", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.2.10.2", "rol_documental": "punto_propio"}, "indice_crudo": 11}
- relación: {"source": "e5", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.2.10.2", "rol_documental": "punto_propio"}, "indice_crudo": 12}
- relación: {"source": "e6", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.2.10.2", "rol_documental": "punto_propio"}, "indice_crudo": 13}
- relación: {"source": "e7", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.2.10.2", "rol_documental": "punto_propio"}, "indice_crudo": 14}
- relación: {"source": "e8", "target": "e1", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.2.10.2", "rol_documental": "punto_propio"}, "indice_crudo": 15}

## 14. `snp_tr::1.3.1.2` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 9):

```
[encabezado | punto S1]
Sección 1. Transferencias en lote.
[encabezado | punto 1.3]
1.3. Instrucciones operativas.
[encabezado | punto 1.3.1]
1.3.1. Solicitud de transferencia y compensación en la CEC.
[texto propio | punto 1.3.1.2]
1.3.1.2. Transferencias minoristas: Pago a proveedores y entre clientes o clientes y terce-
ros.
i) En pesos.
Diariamente operará una única sesión, de presentados.
Las transacciones a presentar electrónicamente a la CEC son las siguientes:
 Órdenes de transferencia.
 Devoluciones de transferencias.
ii) En moneda extranjera.
Diariamente, operarán dos sesiones en las cuales la CEC recibirá los archivos
de las entidades:
 La sesión de presentados.
 La sesión de rechazados.
```

Versión: primer intento (cola). Entidades 7, relaciones 6.
- {"local_id": "to", "type": "TextoOrdenado", "label": "SNP Transferencias Normas Complementarias", "properties": {}, "provenance": {"to": "snp_tr", "archivo": "snp_tr.pdf", "punto": "1.3.1.2", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Operacion", "label": "Órdenes de transferencia en pesos", "properties": {"tipo": "Orden de transferencia", "descripcion": "Órdenes de transferencia minoristas en pesos a presentar electrónicamente a la CEC, operadas en una única sesión diaria de presentados."}, "provenance": {"to": "snp_tr", "archivo": "snp_tr.pdf", "punto": "1.3.1.2", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- {"local_id": "e2", "type": "Operacion", "label": "Devoluciones de transferencias en pesos", "properties": {"tipo": "Devolución de transferencia", "descripcion": "Devoluciones de transferencias minoristas en pesos a presentar electrónicamente a la CEC, operadas en una única sesión diaria de presentados."}, "provenance": {"to": "snp_tr", "archivo": "snp_tr.pdf", "punto": "1.3.1.2", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- {"local_id": "e3", "type": "Operacion", "label": "Sesión de presentados en moneda extranjera", "properties": {"tipo": "Sesión de compensación", "descripcion": "Sesión de presentados en moneda extranjera, operada diariamente por la CEC para recibir archivos de las entidades."}, "provenance": {"to": "snp_tr", "archivo": "snp_tr.pdf", "punto": "1.3.1.2", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- {"local_id": "e4", "type": "Operacion", "label": "Sesión de rechazados en moneda extranjera", "properties": {"tipo": "Sesión de compensación", "descripcion": "Sesión de rechazados en moneda extranjera, operada diariamente por la CEC para recibir archivos de las entidades."}, "provenance": {"to": "snp_tr", "archivo": "snp_tr.pdf", "punto": "1.3.1.2", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- {"local_id": "e5", "type": "Obligacion", "label": "Presentación diaria única sesión pesos", "properties": {"tipo": "presentacion_informativa", "descripcion": "Diariamente operará una única sesión de presentados para transferencias minoristas en pesos.", "frecuencia": "Diariamente"}, "provenance": {"to": "snp_tr", "archivo": "snp_tr.pdf", "punto": "1.3.1.2", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- {"local_id": "e6", "type": "Obligacion", "label": "Presentación diaria dos sesiones moneda extranjera", "properties": {"tipo": "presentacion_informativa", "descripcion": "Diariamente operarán dos sesiones (presentados y rechazados) en las cuales la CEC recibirá los archivos de las entidades en moneda extranjera.", "frecuencia": "Diariamente"}, "provenance": {"to": "snp_tr", "archivo": "snp_tr.pdf", "punto": "1.3.1.2", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_tr", "archivo": "snp_tr.pdf", "punto": "1.3.1.2", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_tr", "archivo": "snp_tr.pdf", "punto": "1.3.1.2", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e3", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_tr", "archivo": "snp_tr.pdf", "punto": "1.3.1.2", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e4", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_tr", "archivo": "snp_tr.pdf", "punto": "1.3.1.2", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- relación: {"source": "e5", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_tr", "archivo": "snp_tr.pdf", "punto": "1.3.1.2", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- relación: {"source": "e6", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_tr", "archivo": "snp_tr.pdf", "punto": "1.3.1.2", "rol_documental": "punto_propio"}, "indice_crudo": 5}

## 15. `cirmo3::5.5.3.2` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 42):

```
[encabezado | punto S5]
Sección 5. Gestión sobre el numerario.
[encabezado | punto 5.5]
5.5. Compensación Interbancaria de Billetes - CIB.
[encabezado | punto 5.5.3]
5.5.3. Límites – Ampliación estacional.
[intro | punto 5.5.3]
El límite determinado en el punto 5.5.2. podrá ser ampliado por el BCRA en forma transi-
toria, entre el 1° de febrero y el 31 de mayo y entre el 1° de agosto y el 30 de noviembre,
por hasta el menor de los siguientes montos:
[texto propio | punto 5.5.3.2]
5.5.3.2. $3.000 millones.
```

Versión: primer intento (cola). Entidades 2, relaciones 1.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Gestión sobre el numerario", "properties": {}, "provenance": {"to": "cirmo3", "archivo": "cirmo3.pdf", "punto": "5.5.3.2", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Restriccion", "label": "Tope ampliación estacional CIB", "properties": {"tipo": "limite_cuantitativo", "descripcion": "El límite de ampliación estacional del sistema de Compensación Interbancaria de Billetes no podrá superar $3.000 millones, en forma transitoria entre el 1° de febrero y el 31 de mayo y entre el 1° de agosto y el 30 de noviembre.", "umbrales": "$3.000 millones"}, "provenance": {"to": "cirmo3", "archivo": "cirmo3.pdf", "punto": "5.5.3.2", "rol_documenta
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "cirmo3", "archivo": "cirmo3.pdf", "punto": "5.5.3.2", "rol_documental": "punto_propio"}, "indice_crudo": 0}

## 16. `lingeef::3.5.4.3` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 68):

```
[encabezado | punto S3]
Sección 3. Gestión del riesgo de liquidez.
[encabezado | punto 3.5]
3.5. Aplicación de herramientas de seguimiento de liquidez intradiaria. Escenarios de estrés.
[encabezado | punto 3.5.4]
3.5.4. Escenarios de estrés.
[intro | punto 3.5.4]
Las entidades financieras alcanzadas deberán evaluar qué escenarios de estrés son
relevantes en función de sus condiciones particulares y modelo de negocio y las medi-
das que deberán adoptar frente a cualquier impacto adverso, ya sea a través de un
plan de contingencia y/o en su marco de gestión del riesgo de liquidez intradiaria. Los
escenarios de estrés que deberán considerar podrán ser los siguientes u otros que en
ese ámbito se determinen:
[texto propio | punto 3.5.4.3]
3.5.4.3. Estrés de una entidad en su carácter de cliente de una entidad financiera co-
rresponsal.
Puede ocasionar que otras entidades financieras difieran sus pagos a la enti-
dad cliente, creando una pérdida de liquidez intradiaria aún mayor a la entidad
financiera que actúa como su corresponsal.
```

Versión: primer intento (cola). Entidades 5, relaciones 8.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Gestión del riesgo de liquidez", "properties": {}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "3.5.4.3", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Operacion", "label": "Estrés de entidad cliente de corresponsal", "properties": {"tipo": "escenario de estrés", "descripcion": "Escenario en el que una entidad financiera, en su carácter de cliente de una entidad corresponsal, experimenta estrés que puede ocasionar que otras entidades financieras difieran sus pagos, creando una pérdida de liquidez intradiaria mayor a la entidad que actúa como corresponsal."}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "
- {"local_id": "e2", "type": "Obligacion", "label": "Evaluar escenarios de estrés relevantes", "properties": {"tipo": "calculo", "descripcion": "Las entidades financieras alcanzadas deberán evaluar qué escenarios de estrés son relevantes en función de sus condiciones particulares y modelo de negocio, y las medidas que deberán adoptar frente a cualquier impacto adverso, ya sea a través de un plan de contingencia y/o en su marco de gestión del riesgo de liquidez intradiaria."}, "provenance": {"to": 
- {"local_id": "e3", "type": "Obligacion", "label": "Considerar efecto probable del estrés de cliente corresponsal", "properties": {"tipo": "calculo", "descripcion": "Las entidades financieras que proveen servicios de corresponsalía deberán considerar el efecto probable que el escenario de estrés de la entidad cliente tendría sobre el monto de los pagos realizados por cuenta de sus clientes y sobre las líneas de crédito extendidas a sus clientes."}, "provenance": {"to": "lingeef", "archivo": "ling
- {"local_id": "e4", "type": "Condicion", "label": "Cuando se trate del escenario de estrés de cliente corresponsal", "properties": {"descripcion": "El supuesto en que la entidad financiera actúa como cliente de una entidad corresponsal y experimenta estrés."}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "3.5.4.3", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "3.5.4.3", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "3.5.4.3", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e3", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "3.5.4.3", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e4", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "3.5.4.3", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- relación: {"source": "e2", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "3.5.4.3", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- relación: {"source": "e3", "target": null, "predicate": "aplica_a", "sujeto_id": null, "sujeto_propuesto": "las entidades financieras que proveen servicios de corresponsalía", "sujeto_propuesto_padre_sugerido": "Sujeto_entidad_financiera", "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "3.5.4.3", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- relación: {"source": "e4", "target": "e3", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "3.5.4.3", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- relación: {"source": "e3", "target": "e1", "predicate": "regula", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "3.5.4.3", "rol_documental": "punto_propio"}, "indice_crudo": 7}

## 17. `lingeef::5.4.5.1` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 116):

```
[encabezado | punto S5]
Sección 5. Gestión del riesgo de tasa de interés en la cartera de inversión.
[encabezado | punto 5.4]
5.4. Marco Estandarizado.
[encabezado | punto 5.4.5]
5.4.5. Escenarios estándar de perturbaciones de tasas de interés.
[intro | punto 5.4.5]
Las entidades financieras deben emplear los siguientes seis escenarios de perturba-
ción de las tasas de interés para capturar en el EVE los riesgos de brecha, paralelos y
no paralelos:
i) desplazamiento paralelo hacia arriba;
ii) desplazamiento paralelo hacia abajo;
iii) empinamiento de la pendiente –disminución de tasas a corto plazo y aumento de
[intro | punto 5.4.5]
tasas a largo plazo–;
[intro | punto 5.4.5]
iv) aplanamiento de la pendiente –aumento de tasas a corto plazo y disminución de
[intro | punto 5.4.5]
tasas a largo plazo–;
[intro | punto 5.4.5]
v) aumento de las tasas de corto plazo; y
vi) disminución de las tasas de corto plazo.
Los escenarios se aplican a las exposiciones al RTICI en cada moneda en la que la en-
tidad financiera mantenga exposiciones relevantes, conforme a lo definido en el punto
5.4.4.
En la siguiente tabla se listan las perturbaciones instantáneas y absolutas –en puntos
básicos– de las tasas libres de riesgo que se deberán emplear. La tasa de interés re-
sultante luego de aplicar la perturbación que corresponda estará sujeta a un mínimo de
cero.
[intro | punto 5.4.5]
((cid:1)
[intro | punto 5.4.5]
Perturbaciones instantáneas y absolutas )
[intro | punto 5.4.5]
c
[intro | punto 5.4.5]
Se aplicarán las siguientes parametrizaciones para construir los seis escenarios de
perturbación de las tasas de interés:
[texto propio | punto 5.4.5.1]
5.4.5.1. Perturbación en paralelo para la moneda c: perturbación constante paralela, al
alza o a la baja, en todas las bandas temporales:
```

Versión: primer intento (cola). Entidades 3, relaciones 4.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Gestión del riesgo de tasa de interés", "properties": {}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.5.1", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Operacion", "label": "Perturbación paralela constante en tasas", "properties": {"tipo": "Perturbación de tasas de interés", "descripcion": "Perturbación constante paralela de las tasas de interés, al alza o a la baja, aplicada uniformemente en todas las bandas temporales para la moneda c"}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.5.1", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- {"local_id": "e2", "type": "Obligacion", "label": "Emplear escenarios de perturbación de tasas", "properties": {"tipo": "calculo", "descripcion": "Las entidades financieras deben emplear los seis escenarios de perturbación de tasas de interés (incluyendo perturbación en paralelo para la moneda c: perturbación constante paralela, al alza o a la baja, en todas las bandas temporales) para capturar en el EVE los riesgos de brecha, paralelos y no paralelos"}, "provenance": {"to": "lingeef", "archivo"
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.5.1", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.5.1", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e2", "target": "e1", "predicate": "regula", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.5.1", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e2", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.5.1", "rol_documental": "punto_propio"}, "indice_crudo": 3}

## 18. `lingeef::5.4.2.3` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 105, 106, 107, 108, 109, 110, 111):

```
[encabezado | punto S5]
Sección 5. Gestión del riesgo de tasa de interés en la cartera de inversión.
[encabezado | punto 5.4]
5.4. Marco Estandarizado.
[encabezado | punto 5.4.2]
5.4.2. Tratamiento de las posiciones según la posibilidad de estandarización.
[texto propio | punto 5.4.2.3]
5.4.2.3. Posiciones no susceptibles de estandarización.
Las posiciones no susceptibles de estandarización incluyen a los depósitos sin
vencimiento (NMD), los préstamos a tasa de interés fija sujetos a riesgo de
cancelación anticipada y los depósitos a plazo sujetos a riesgo de retiro antici-
pado.
i) Tratamiento de los NMD para las entidades financieras del Grupo “A”.
Los NMD se deben separar considerando la naturaleza del depósito y del
depositante e identificar, para cada categoría –minorista transaccional,
minorista no transaccional y mayorista–, los depósitos básicos (“core”) y no
básicos (“non-core”), teniendo presente los límites especificados en la tabla
del apartado c) de este acápite. Luego, se deben asignar adecuadamente
los flujos de fondos de cada categoría, considerando los límites a los ven-
cimientos promedio establecidos en la citada tabla.
a) NMD minoristas y mayoristas.
Los NMD deben dividirse en las categorías minorista y mayorista.
Los depósitos minoristas se definen como los realizados por una persona
humana. Se considera que los depósitos realizados por una Mipyme
–conforme a la definición prevista en el TO sobre Determinación de la
Condición de Micro, Pequeña y Mediana Empresa– y gestionados como
exposiciones minoristas presentan características de riesgo de tasa de in-
terés similares a las de las cuentas minoristas y, por lo tanto, pueden tra-
tarse como depósitos minoristas, siempre que el total de los pasivos cap-
tados de la Mipyme sea inferior al importe establecido en el acápite ii) del
punto 2.8.3.3. del TO sobre Capitales Mínimos de las Entidades Financie-
ras.
Los depósitos minoristas se consideran cuentas transaccionales cuando
en dichas cuentas se realicen operaciones de manera regular (por ejem-
plo, cuando se acrediten salarios regularmente) o cuando el depósito no
devengue intereses. Los restantes depósitos minoristas se deben consi-
derar cuentas no transaccionales.
Los depósitos realizados por personas jurídicas –excluyendo aquellos que
puedan ser tratados como depósitos minoristas– se agrupan en la catego-
ría de depósitos mayoristas.
b) NMD estables y no estables, básicos y no básicos.
Para cada categoría de NMD –minorista y mayorista– se debe distinguir
entre la parte estable y no estable, considerando las variaciones de los
montos observadas en los 10 últimos años.
El segmento estable de los NMD es aquel que no se retira con un alto
grado de probabilidad. Los depósitos básicos son la parte de los NMD es-
tables que es improbable que se reaprecien, aun en presencia de cam-
bios significativos en las tasas de interés. Los restantes depósitos –es de-
cir, los no estables y los estables que no resulten básicos– constituyen los
NMD no básicos.
El volumen de los depósitos básicos se debe estimar para los depósitos
minoristas y mayoristas por separado y, posteriormente, se deben sumar
los resultados para determinar el volumen total de depósitos básicos, su-
jeto a los límites máximos establecidos en la tabla del apartado c) del pre-
sente acápite.
c) Asignación de los flujos de fondos.
Los NMD deben asignarse finalmente a la banda temporal o punto medio
de banda temporal apropiado. Los depósitos no básicos deben conside-
rarse depósitos a un día y, en consecuencia, asignarse a la banda tempo-
ral a un día o su punto medio.
Las entidades financieras deben determinar un procedimiento adecuado
para la asignación de los flujos de fondos de depósitos básicos –de
depósitos minoristas y mayoristas por separado–, sin superar el plazo
promedio máximo ponderado por monto para cada categoría que se es-
pecifica en la siguiente tabla.
Límite máximo a la proporción Límite máximo al vencimiento promedio ponderado
de depósitos básicos (%) por monto de depósitos básicos (años)
Minorista/transaccional 90 5
Minorista/no transaccional 70 4,5
Mayorista 50 4
ii) Tratamiento de los NMD para las entidades financieras del grupo B.
Las restantes entidades financieras deben considerar como depósitos bási-
cos el 50% de sus NMD totales.
Los flujos de fondos de los depósitos básicos deben asignarse a las bandas
temporales o puntos medios correspondientes sin superar el plazo promedio
máximo ponderado por monto de 4 años.
Los depósitos no básicos –es decir, el 50% restante de sus NMD totales–,
deben considerarse depósitos a un día y, en consecuencia, asignarse a la
banda temporal a un día o su punto medio.
iii) Tratamiento de las posiciones con opciones de comportamiento distintas de
los NMD.
El tratamiento descripto en este acápite se aplica únicamente a las opciones
de comportamiento relacionadas con los clientes minoristas.
Cuando un cliente mayorista cuente con una opción que pueda modificar el
patrón de los flujos de fondos nocionales sujetos a reapreciación, dicha op-
ción debe ser incluida dentro de la categoría de opciones automáticas implí-
citas sobre tasas de interés y tratarse según lo previsto en punto 5.4.3.
En los préstamos a tasa de interés fija sujetos a riesgo de cancelación anti-
cipada y en los depósitos a plazo sujetos a riesgo de retiro anticipado el
cliente dispone de una opción que, si la ejerce, alterará el perfil temporal de
los flujos de fondos de la entidad financiera. El ejercicio de la opción por
parte del cliente está influenciado, entre otros factores, por las variaciones
de las tasas de interés.
En el caso de un préstamo a tasa fija, el cliente puede disponer de una op-
ción para pagar anticipadamente el préstamo, mientras que en un depósito
a plazo fijo el cliente puede tener la opción de retirar su depósito antes de la
fecha programada.
La opcionalidad en tales productos se estima utilizando una metodología de
dos etapas: en primer lugar, se estiman tasas de referencia de pagos antici-
pados para los préstamos y de retiros anticipados para los depósitos a pla-
zo fijo considerando un escenario base, es decir con la estructura temporal
de tasas de interés vigente.
En la segunda etapa, las tasas de referencia se multiplican por escalares
dependientes de los escenarios de perturbación de tasas de interés, que re-
flejan los probables cambios de conducta en el ejercicio de las opciones.
a) Préstamos a tasa fija sujetos al riesgo de cancelación anticipada.
Los pagos anticipados –totales o parciales– cuyo costo económico no se
traslada al prestatario se denominan cancelaciones anticipadas no com-
pensadas.
En el caso de préstamos en los que el costo económico de los pagos an-
ticipados nunca se traslada al cliente, o sólo se traslada para las cance-
laciones que excedan cierto umbral, los flujos de fondos nocionales suje-
tos a reapreciación se deben asignar a su correspondiente banda tempo-
ral o punto medio utilizando la metodología descripta a continuación.
Las entidades financieras deben determinar la tasa de cancelación anti-
cipada condicional de referencia –sujeto a revisión por la SEFyC– para
cada cartera p de préstamos homogéneos susceptibles de cancelación
anticipada denominados en cada moneda c (CPRp ) para el escenario
0,c
base.
Alternativamente, la CPR de referencia también puede variar durante la
vida de cada préstamo. En ese caso, se denota CPR(k)p para cada
0,c
banda temporal k o punto medio de la banda temporal t .
k
La tasa de cancelación anticipada condicional (CPR) para cada cartera p
de préstamos homogéneos susceptibles de cancelación anticipada de-
nominados en la moneda c, en el escenario de tasas de interés i, resulta
de la siguiente expresión:
donde:
CPRp : tasa de cancelación anticipada condicional de referencia para
i,c
cada cartera homogénea de préstamos p denominados en la
moneda c para el escenario i.
(cid:2): multiplicador correspondiente al escenario i –conforme a lo
i
previsto en la tabla de este apartado– que refleja la expectativa
de que los pagos anticipados sean mayores durante los perío-
dos de descenso de las tasas de interés y menores durante pe-
ríodos de aumento.
CPRp : tasa de cancelación anticipada condicional de referencia (cons-
0,c
tante) para cada cartera homogénea de préstamos p denomina-
dos en la moneda c para el escenario base.
Multiplicador (cid:2) para cada escenario
i
de perturbación de la tasa de interés
(cid:2)
Escenario i
Escenarios de perturbación de tasas de interés (multiplicador del
número (i)
escenario)
1 Desplazamiento paralelo hacia arriba 0,8
2 Desplazamiento paralelo hacia abajo 1,2
3 Empinamiento de la pendiente 0,8
4 Aplanamiento de la pendiente 1,2
5 Aumento de las tasas de corto plazo 0,8
6 Disminución de las tasas de corto plazo 1,2
Finalmente, el flujo de fondos de cada banda temporal surgirá de la su-
ma de los pagos programados –tanto por intereses como por capital– y
los pagos no programados, estos últimos estimados a partir de multiplicar
la CPR de una cartera p de préstamos homogéneos denominados en la
moneda c en el escenario de tasas de interés i por el saldo nocional
pendiente de la banda temporal anterior:
donde:
CFp (k): flujo de fondos sujetos a reapreciación de la banda temporal
i,c
k de la cartera homogénea de préstamos p denominados en
la moneda c corregido por cancelaciones anticipadas esti-
madas para el escenario i.
CFS (k): flujo de fondos sujetos a reapreciación de la banda temporal
i,c
k correspondiente a los pagos pautados de interés y de ca-
pital denominados en la moneda c, para el escenario i.
Np (k – 1): saldo nocional de la cartera homogénea de préstamos p
i,c
denominados en la moneda c que se registra en la banda
temporal anterior.
Los flujos de fondos de referencia –es decir, dada la curva de tasas de
interés vigente y la CPRp – corresponden a i = 0, mientras que los flu-
0,c
jos correspondientes a los escenarios de perturbación de tasas de inte-
rés corresponden a i = 1 a 6.
b) Depósitos a plazo sujetos a riesgo de retiro anticipado.
Los depósitos a plazo pueden tratarse como pasivos a tasa fija y sus flu-
jos de fondos nocionales sujetos a reapreciación asignarse a las corres-
pondientes bandas temporales o puntos medios de bandas temporales
según sus fechas de vencimiento contractuales siempre que pueda de-
mostrarse, a satisfacción de la SEFyC, que:
- el depositante carece del derecho legal de retirar anticipadamente el
depósito; o
- el retiro anticipado conlleva una penalidad significativa para el cliente
que –como mínimo–compensa a la entidad por el costo de rescisión
del contrato.
De no cumplirse las citadas condiciones, se considera que el depositan-
te tiene una opción de retiro de fondos y que los depósitos a plazo están
sujetos a riesgo de retiro anticipado.
Cuando se trate de depósitos a plazo de clientes mayoristas en los que
no se cumplan tales condiciones, debe considerarse que poseen una
opción automática implícita sobre tasa de interés –es decir, que se asu-
me que el cliente siempre ejercerá su derecho de retiro de depósitos de
la forma más desventajosa para la entidad financiera– y tratarse de con-
formidad con lo previsto en el punto 5.4.3.
Las entidades financieras deben determinar la tasa de retiro anticipado
de referencia para depósitos a plazo TDRRp –sujeto a revisión de la
0,c
SEFyC– aplicable a cada cartera homogénea p de depósitos a plazo en
la moneda c y utilizarla para asignar los flujos de fondos nocionales suje-
tos a reapreciación. Los depósitos a plazo para los que se prevé su reti-
ro anticipado se asignan a la banda temporal a un día (k = 1) o a su pun-
to medio (t ).
1
La tasa de retiro anticipado de depósitos a plazo para la banda temporal
k o el punto medio de la banda temporal t aplicable a cada cartera
k
homogénea p de depósitos a plazo en la moneda c para el escenario i
se obtiene multiplicando TDRRp por un escalar u que depende del es-
0,c i
cenario i, de acuerdo con la siguiente expresión:
donde:
TDRRp : tasa de retiro anticipado de depósitos a plazo de referencia de
i,c
la cartera homogénea de depósitos p denominados en la mo-
neda c para el escenario i.
u: multiplicador correspondiente al escenario i –conforme a lo
i
previsto en la tabla de este apartado– que refleja la expectativa
de que los retiros anticipados de depósitos a plazo sean mayo-
res durante los períodos de aumento de las tasas de interés y
menores durante períodos de descenso.
TDRRp :tasa de retiro anticipado de depósitos a plazo de referencia de
0,c
la cartera homogénea de depósitos p denominados en la mo-
neda c para el escenario base.
Multiplicador u para cada escenario
i
de perturbación de la tasa de interés
Escenario Multiplicadores
Escenarios de perturbación de tasas de interés
número (i) escalares u
i
1 Desplazamiento paralelo hacia arriba 1,2
2 Desplazamiento paralelo hacia abajo 0,8
3 Empinamiento de la pendiente 0,8
4 Aplanamiento de la pendiente 1,2
5 Aumento de las tasas de corto plazo 1,2
6 Disminución de las tasas de corto plazo 0,8
Los flujos de fondos nocionales sujetos a reapreciación a asignar a la
banda temporal correspondiente a k = 1 –es decir, aquellos para los que
se prevé un retiro anticipado– en el escenario de perturbación de tasas
de interés i surgen de la siguiente expresión:
donde:
CFp (1): flujo de fondos nocionales sujetos a reapreciación de la cartera
i,c
homogénea de depósitos a plazo p denominados en la mone-
da c que se estima que se retirarán anticipadamente y por lo
tanto se asigna a la banda temporal a 1 día, para el escenario
i.
TDp : saldo de depósitos de la cartera homogénea de depósitos a
0,c
plazo p denominados en la moneda c para el escenario base.
```

Versión: primer intento (cola). Entidades 36, relaciones 51.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Gestión del riesgo de tasa de interés", "properties": {}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Definicion", "label": "Posiciones no susceptibles de estandarización", "properties": {"termino": "Posiciones no susceptibles de estandarización", "descripcion": "Incluyen a los depósitos sin vencimiento (NMD), los préstamos a tasa de interés fija sujetos a riesgo de cancelación anticipada y los depósitos a plazo sujetos a riesgo de retiro anticipado."}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "in
- {"local_id": "e2", "type": "Obligacion", "label": "Separar NMD considerando naturaleza — Grupo A", "properties": {"tipo": "calculo", "descripcion": "Para entidades del Grupo A, los NMD deben separarse considerando la naturaleza del depósito y del depositante, identificar las categorías (minorista transaccional, minorista no transaccional y mayorista), y clasificar los depósitos básicos (core) y no básicos (non-core) conforme a los límites de la tabla del apartado c)."}, "provenance": {"to": "lin
- {"local_id": "e3", "type": "Obligacion", "label": "Asignar flujos de fondos de cada categoría — Grupo A", "properties": {"tipo": "asignacion", "descripcion": "Asignar adecuadamente los flujos de fondos de cada categoría de NMD, considerando los límites a los vencimientos promedio establecidos en la tabla del apartado c)."}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- {"local_id": "e4", "type": "Definicion", "label": "Depósitos minoristas", "properties": {"termino": "Depósitos minoristas", "descripcion": "Depósitos realizados por una persona humana."}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- {"local_id": "e5", "type": "Condicion", "label": "Depósitos de MiPyME tratables como minoristas", "properties": {"descripcion": "Los depósitos de MiPyME gestionados como exposiciones minoristas pueden tratarse como depósitos minoristas si el total de pasivos captados es inferior al importe del punto 2.8.3.3 del TO sobre Capitales Mínimos.", "umbrales": "sea inferior al importe establecido en el acápite ii) del punto 2.8.3.3. del TO sobre Capitales Mínimos de las Entidades Financieras"}, "provena
- {"local_id": "e6", "type": "Definicion", "label": "Depósitos minoristas transaccionales", "properties": {"termino": "cuentas transaccionales", "descripcion": "Depósitos minoristas en los que se realicen operaciones de manera regular (p.ej. acreditación regular de salarios) o que no devenguen intereses."}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- {"local_id": "e7", "type": "Definicion", "label": "Depósitos minoristas no transaccionales", "properties": {"termino": "cuentas no transaccionales", "descripcion": "Los restantes depósitos minoristas (aquellos que no son transaccionales)."}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 7}
- {"local_id": "e8", "type": "Definicion", "label": "Depósitos mayoristas", "properties": {"termino": "Depósitos mayoristas", "descripcion": "Depósitos realizados por personas jurídicas, excluyendo aquellos tratables como depósitos minoristas."}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 8}
- {"local_id": "e9", "type": "Obligacion", "label": "Distinguir NMD entre estable y no estable — Grupo A", "properties": {"tipo": "calculo", "descripcion": "Para cada categoría de NMD (minorista y mayorista), distinguir entre la parte estable y no estable, considerando variaciones de montos en los últimos 10 años.", "umbrales": "en los 10 últimos años"}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 9}
- {"local_id": "e10", "type": "Definicion", "label": "Segmento estable de NMD", "properties": {"termino": "segmento estable de los NMD", "descripcion": "Aquel que no se retira con un alto grado de probabilidad."}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 10}
- {"local_id": "e11", "type": "Definicion", "label": "Depósitos básicos (core)", "properties": {"termino": "Depósitos básicos", "descripcion": "Parte de los NMD estables que es improbable que se reaprecien, aun ante cambios significativos en tasas de interés."}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 11}
- {"local_id": "e12", "type": "Definicion", "label": "NMD no básicos", "properties": {"termino": "NMD no básicos", "descripcion": "Los depósitos no estables y los estables que no resulten básicos."}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 12}
- {"local_id": "e13", "type": "Obligacion", "label": "Estimar volumen depósitos básicos — Grupo A", "properties": {"tipo": "calculo", "descripcion": "Estimar el volumen de depósitos básicos para minoristas y mayoristas por separado, sumar los resultados para el total, sujeto a los límites máximos de la tabla del apartado c)."}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 13}
- {"local_id": "e14", "type": "Obligacion", "label": "Asignar NMD a banda temporal — Grupo A", "properties": {"tipo": "asignacion", "descripcion": "Asignar finalmente los NMD a la banda temporal o punto medio de banda temporal apropiado."}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 14}
- {"local_id": "e15", "type": "Restriccion", "label": "Depósitos no básicos a un día", "properties": {"tipo": "limite_cualitativo", "descripcion": "Los depósitos no básicos deben considerarse depósitos a un día y asignarse a la banda temporal a un día o su punto medio."}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 15}
- {"local_id": "e16", "type": "Obligacion", "label": "Determinar procedimiento asignación depósitos básicos — Grupo A", "properties": {"tipo": "otra", "descripcion": "Determinar procedimiento adecuado para asignación de flujos de fondos de depósitos básicos (minoristas y mayoristas por separado), sin superar plazo promedio máximo ponderado por monto para cada categoría conforme a tabla."}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio
- {"local_id": "e17", "type": "Restriccion", "label": "Límite máximo depósitos básicos minorista transaccional", "properties": {"tipo": "limite_cuantitativo", "descripcion": "Límite máximo a la proporción de depósitos básicos para minorista/transaccional.", "umbrales": "90"}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 17}
- {"local_id": "e18", "type": "Restriccion", "label": "Límite máximo vencimiento minorista transaccional", "properties": {"tipo": "limite_cuantitativo", "descripcion": "Límite máximo al vencimiento promedio ponderado por monto de depósitos básicos para minorista/transaccional.", "umbrales": "5"}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 18}
- {"local_id": "e19", "type": "Restriccion", "label": "Límite máximo depósitos básicos minorista no transaccional", "properties": {"tipo": "limite_cuantitativo", "descripcion": "Límite máximo a la proporción de depósitos básicos para minorista/no transaccional.", "umbrales": "70"}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 19}
- {"local_id": "e20", "type": "Restriccion", "label": "Límite máximo vencimiento minorista no transaccional", "properties": {"tipo": "limite_cuantitativo", "descripcion": "Límite máximo al vencimiento promedio ponderado por monto de depósitos básicos para minorista/no transaccional.", "umbrales": "4,5"}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 20}
- {"local_id": "e21", "type": "Restriccion", "label": "Límite máximo depósitos básicos mayorista", "properties": {"tipo": "limite_cuantitativo", "descripcion": "Límite máximo a la proporción de depósitos básicos para mayorista.", "umbrales": "50"}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 21}
- {"local_id": "e22", "type": "Restriccion", "label": "Límite máximo vencimiento mayorista", "properties": {"tipo": "limite_cuantitativo", "descripcion": "Límite máximo al vencimiento promedio ponderado por monto de depósitos básicos para mayorista.", "umbrales": "4"}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 22}
- {"local_id": "e23", "type": "Obligacion", "label": "Considerar depósitos básicos 50% — Grupo B", "properties": {"tipo": "calculo", "descripcion": "Para entidades del Grupo B, considerar como depósitos básicos el 50% de sus NMD totales.", "umbrales": "el 50%"}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 23}
- {"local_id": "e24", "type": "Obligacion", "label": "Asignar flujos depósitos básicos — Grupo B", "properties": {"tipo": "asignacion", "descripcion": "Para entidades del Grupo B, asignar flujos de fondos de depósitos básicos a bandas temporales o puntos medios, sin superar plazo promedio máximo ponderado de 4 años.", "umbrales": "sin superar el plazo promedio máximo ponderado por monto de 4 años"}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "pu
- {"local_id": "e25", "type": "Restriccion", "label": "Depósitos no básicos a un día — Grupo B", "properties": {"tipo": "limite_cualitativo", "descripcion": "Para entidades del Grupo B, los depósitos no básicos (50% restante de NMD totales) deben considerarse depósitos a un día y asignarse a banda temporal a un día o su punto medio."}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 25}
- {"local_id": "e26", "type": "Restriccion", "label": "Tratamiento opciones comportamiento solo minoristas", "properties": {"tipo": "limite_cualitativo", "descripcion": "El tratamiento de opciones de comportamiento se aplica únicamente a opciones relacionadas con clientes minoristas."}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 26}
- {"local_id": "e27", "type": "Obligacion", "label": "Incluir opción cliente mayorista en categoría automática", "properties": {"tipo": "otra", "descripcion": "Cuando un cliente mayorista tenga una opción que modifique el patrón de flujos de fondos nocionales, incluirla en la categoría de opciones automáticas implícitas sobre tasas de interés y tratarla según punto 5.4.3."}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_cru
- {"local_id": "e28", "type": "Operacion", "label": "Cancelación anticipada de préstamo a tasa fija", "properties": {"tipo": "cancelación anticipada de préstamo a tasa fija", "descripcion": "Opción del cliente de cancelar anticipadamente un préstamo a tasa fija que altera el perfil temporal de flujos de fondos, influenciada por variaciones en tasas de interés."}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 28}
- {"local_id": "e29", "type": "Operacion", "label": "Retiro anticipado de depósito a plazo", "properties": {"tipo": "retiro anticipado de depósito a plazo", "descripcion": "Opción del cliente de retirar anticipadamente un depósito a plazo que altera el perfil temporal de flujos de fondos, influenciada por variaciones en tasas de interés."}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 29}
- {"local_id": "e30", "type": "Definicion", "label": "Cancelaciones anticipadas no compensadas", "properties": {"termino": "cancelaciones anticipadas no compensadas", "descripcion": "Pagos anticipados (totales o parciales) cuyo costo económico no se traslada al prestatario."}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 30}
- {"local_id": "e31", "type": "Obligacion", "label": "Determinar CPR de referencia base", "properties": {"tipo": "calculo", "descripcion": "Determinar la tasa de cancelación anticipada condicional de referencia (CPR) para cada cartera homogénea de préstamos susceptibles de cancelación anticipada en cada moneda, para el escenario base, sujeto a revisión de SEFyC."}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 31}
- {"local_id": "e32", "type": "Obligacion", "label": "Determinar procedimiento asignación flujos de fondos depósitos a plazo", "properties": {"tipo": "calculo", "descripcion": "Determinar la tasa de retiro anticipado de referencia (TDRR) para depósitos a plazo aplicable a cada cartera homogénea en cada moneda y utilizarla para asignar flujos de fondos nocionales, sujeto a revisión de SEFyC."}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_pr
- {"local_id": "e33", "type": "Restriccion", "label": "Asignar depósitos a plazo con retiro anticipado a un día", "properties": {"tipo": "limite_cualitativo", "descripcion": "Los depósitos a plazo para los que se prevé retiro anticipado deben asignarse a la banda temporal a un día o su punto medio."}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 33}
- {"local_id": "e34", "type": "Condicion", "label": "Depósitos a plazo sin opción de retiro anticipado", "properties": {"descripcion": "Depósitos a plazo pueden asignarse conforme vencimiento contractual si se demuestra que el depositante carece de derecho legal de retiro anticipado o que este conlleva penalidad significativa que compensa costo de rescisión."}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 34}
- {"local_id": "e35", "type": "Potestad", "label": "Variación de CPR durante vida del préstamo", "properties": {"descripcion": "La CPR de referencia puede variar durante la vida de cada préstamo, alternativa a la CPR constante por banda temporal."}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 35}
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e2", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- relación: {"source": "e3", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- relación: {"source": "e3", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- relación: {"source": "e4", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- relación: {"source": "e5", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 7}
- relación: {"source": "e6", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 8}
- relación: {"source": "e7", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 9}
- relación: {"source": "e8", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 10}
- relación: {"source": "e9", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 11}
- relación: {"source": "e9", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 12}
- relación: {"source": "e10", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 13}
- relación: {"source": "e11", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 14}
- relación: {"source": "e12", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 15}
- relación: {"source": "e13", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 16}
- relación: {"source": "e13", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 17}
- relación: {"source": "e14", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 18}
- relación: {"source": "e14", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 19}
- relación: {"source": "e15", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 20}
- relación: {"source": "e15", "target": "e29", "predicate": "limita", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 21}
- relación: {"source": "e16", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 22}
- relación: {"source": "e16", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 23}
- relación: {"source": "e17", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 24}
- relación: {"source": "e18", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 25}
- relación: {"source": "e19", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 26}
- relación: {"source": "e20", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 27}
- relación: {"source": "e21", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 28}
- relación: {"source": "e22", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 29}
- relación: {"source": "e23", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 30}
- relación: {"source": "e23", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 31}
- relación: {"source": "e24", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 32}
- relación: {"source": "e24", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 33}
- relación: {"source": "e25", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 34}
- relación: {"source": "e26", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 35}
- relación: {"source": "e27", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 36}
- relación: {"source": "e27", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 37}
- relación: {"source": "e28", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 38}
- relación: {"source": "e29", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 39}
- relación: {"source": "e30", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 40}
- relación: {"source": "e31", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 41}
- relación: {"source": "e31", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 42}
- relación: {"source": "e32", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 43}
- relación: {"source": "e32", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 44}
- relación: {"source": "e33", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 45}
- relación: {"source": "e34", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 46}
- relación: {"source": "e34", "target": "e28", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 47}
- relación: {"source": "e34", "target": "e29", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 48}
- relación: {"source": "e35", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 49}
- relación: {"source": "e35", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.4.2.3", "rol_documental": "punto_propio"}, "indice_crudo": 50}

## 19. `depaho::3.8.3.4` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 44):

```
[encabezado | punto S3]
Sección 3. Especiales.
[encabezado | punto 3.8]
3.8. Especial de inversión (Resolución 4/17 de la Unidad de Información Financiera).
[encabezado | punto 3.8.3]
3.8.3. Identificación del titular.
[intro | punto 3.8.3]
Como mínimo se exigirán los siguientes datos:
[texto propio | punto 3.8.3.4]
3.8.3.4. Copia autenticada del contrato o estatuto social –siendo de aplicación lo previsto
en el punto 4.1.2.–.
```

Versión: primer intento (cola). Entidades 3, relaciones 4.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Depósitos de ahorro", "properties": {}, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "3.8.3.4", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Obligacion", "label": "Presentar copia autenticada de contrato o estatuto social", "properties": {"descripcion": "El solicitante deberá presentar copia autenticada del contrato o estatuto social, siendo de aplicación lo previsto en el punto 4.1.2., en forma personal o por correo postal o internacional, dentro de los 60 días corridos siguientes a la fecha de la apertura de la cuenta.", "tipo": "presentacion_informativa", "frecuencia": "Dentro de los 60 días corridos si
- {"local_id": "e2", "type": "Condicion", "label": "Documentación remitida por medios electrónicos", "properties": {"descripcion": "La obligación de presentar copia autenticada se aplica cuando la documentación ha sido remitida previamente a través de medios electrónicos.", "umbrales": "Dentro de los 60 días corridos siguientes a la fecha de la apertura de la cuenta"}, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "3.8.3.4", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "3.8.3.4", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "3.8.3.4", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e2", "target": "e1", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "3.8.3.4", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e1", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_cliente", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "3.8.3.4", "rol_documental": "punto_propio"}, "indice_crudo": 3}

## 20. `efemin::6.4.3.1` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 27):

```
[encabezado | punto S6]
Sección 6. Cupo Mipyme Mínimo.
[encabezado | punto 6.4]
6.4. Financiaciones elegibles.
[encabezado | punto 6.4.3]
6.4.3. Especiales.
[texto propio | punto 6.4.3.1]
6.4.3.1. Clientes no MiPyME, en la medida en que los fondos se destinen a la adqui-
sición de maquinarias y equipos producidas por MiPyME locales.
```

Versión: primer intento (cola). Entidades 3, relaciones 4.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Texto Ordenado Efectivo Mínimo", "properties": {}, "provenance": {"to": "efemin", "archivo": "efemin.pdf", "punto": "6.4.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Operacion", "label": "Adquisición de maquinarias y equipos de MiPyME locales", "properties": {"tipo": "Financiación", "descripcion": "Adquisición de maquinarias y equipos producidas por MiPyME locales, como destino elegible de fondos para clientes no MiPyME"}, "provenance": {"to": "efemin", "archivo": "efemin.pdf", "punto": "6.4.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- {"local_id": "e2", "type": "Condicion", "label": "Fondos destinados a adquisición de maquinarias de MiPyME", "properties": {"descripcion": "Condición que habilita el financiamiento a clientes no MiPyME: que los fondos se destinen específicamente a la adquisición de maquinarias y equipos producidas por MiPyME locales"}, "provenance": {"to": "efemin", "archivo": "efemin.pdf", "punto": "6.4.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "efemin", "archivo": "efemin.pdf", "punto": "6.4.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "efemin", "archivo": "efemin.pdf", "punto": "6.4.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e2", "target": "e1", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "efemin", "archivo": "efemin.pdf", "punto": "6.4.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e1", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_mipyme", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "efemin", "archivo": "efemin.pdf", "punto": "6.4.3.1", "rol_documental": "punto_propio"}, "indice_crudo": 3}

## 21. `lingeef::4.1.2.1` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 71):

```
[encabezado | punto S4]
Sección 4. Gestión del riesgo de mercado.
[encabezado | punto 4.1]
4.1. Conceptos.
[encabezado | punto 4.1.2]
4.1.2. Gestión del riesgo de mercado.
[intro | punto 4.1.2]
Se entiende por gestión del riesgo de mercado al proceso de identificación, evaluación,
seguimiento, control y mitigación de este riesgo, el cual involucra una serie de procesos,
entre ellos:
[texto propio | punto 4.1.2.1]
4.1.2.1. Desarrollo de modelos para la estimación del riesgo;
```

Versión: primer intento (cola). Entidades 1, relaciones 0.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Gestión del riesgo de mercado", "properties": {}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "4.1.2.1", "rol_documental": "punto_propio"}, "indice_crudo": 0}

## 22. `snp_cheq::3.1.4.2` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 24, 25, 26):

```
[encabezado | punto S3]
Sección 3. Instrucciones operativas.
[encabezado | punto 3.1]
3.1. Compensación electrónica de cheques.
[encabezado | punto 3.1.4]
3.1.4. Otros aspectos operativos.
[texto propio | punto 3.1.4.2]
3.1.4.2. Feriados locales.
i) Definición.
Se considera feriado local previsto todo aquel declarado por autoridad compe-
tente (nacional, provincial, municipal o Ciudad Autónoma de Buenos Aires),
que permita ser incluido con antelación en un calendario de feriados locales.
Dicho calendario será administrado por las CEC, e incluirá las fechas de los
feriados previstos para los diferentes puntos de intercambio. Esta administra-
ción se realizará a través de un sitio web desarrollado al efecto, el cual será
actualizado con la información que deberán proveer las propias entidades fi-
nancieras.
Se considerará feriado local imprevisto todo aquel declarado por autoridad
competente (nacional, provincial, municipal o Ciudad Autónoma de Buenos Ai-
res), que no pueda ser incluido con anterioridad en el calendario administrado
por las CEC, pero que sea conocido por éstas a través de la información brin-
dada formalmente por el/los banco/s presente/s en la plaza, como máximo
hasta las 17 horas del día hábil anterior a la fecha en que se produce el feria-
do.
ii) Instrucciones operativas.
a) Feriados locales previstos:
La CEC identificará los movimientos con el/los código/s postal/es banca-
rio/s con fecha de compensación del día feriado y los retendrá sin distri-
buirlos a las entidades giradas. Por otra parte, los rechazará en la sesión
de rechazados del día del feriado local para lo cual utilizará el código R09
“feriado local”. Asimismo, en la sesión de presentados inmediata siguien-
te los presentará con fecha de compensación del día hábil siguiente, dis-
tribuyendo a las entidades giradas la información de las transacciones co-
rrespondientes al punto de intercambio que tuvo feriado local. Las tareas
que deberán realizar los distintos actores intervinientes serán:
Día D-1
En la sesión de presentados del día anterior al feriado local, la CEC identificará las transacciones
con feriado local presentadas por las entidades depositarias y las retendrá junto con las imágenes
de los cheques que superen el monto establecido como límite de truncamiento, sin distribuirlas a
las entidades giradas.
Las entidades depositarias deberán considerar que parte de las transacciones presentadas no
aplicarán en la posición de inicio de ese ciclo, ya que serán retenidas por la Cámara. No obstan-
te, para permitir un control adecuado de la “Cámara Enviada” dichas transacciones se mostrarán
por separado en los listados de posición de inicio de ciclo y en el listado bilateral, aunque sin ser
contabilizadas en esa posición, ya que serán retenidas por la CEC y no se distribuirán a las enti-
dades giradas hasta el momento de la presentación efectiva.
Día D (feriado local)
Antes de las 12.00.
Entidades y Cámaras Electrónicas:
 Distribuirán a las entidades depositarias de la plaza con feriado local los rechazos gene-
rados con su respectivo total.
Sesión de rechazados
Entidad depositaria:
 No podrá presentar rechazos de entidad depositaria para los cheques diferidos por fe-
riado local.
Cámaras electrónicas:
 Devolverán los posibles rechazos, tanto de entidad depositaria como de entidad girada
para aquellos cheques que fueron diferidos por feriado local.
Entidad girada:
 No deberá presentar rechazos de entidad girada para los cheques diferidos por feriado
local.
Para lograr la conciliación de la posición final de débitos y créditos las entidades deberán conside-
rar la siguiente información:
Entidad depositaria: conciliación de posición final: Débitos
 Rechazos de entidad depositaria.
 Rechazos recibidos de entidad girada, no rechazados por ella misma.
 Rechazos por feriado local.
Cámaras electrónicas:
 Incluirán en las posiciones consolidadas los movimientos rechazados por feriado local.
Entidad girada: conciliación de la posición final: Créditos
 Rechazados de entidad girada.
 Rechazados recibidos de entidad depositaria, no rechazados por ella misma.
 Rechazos por feriado local.
Sesión de presentados.
Cámaras electrónicas:
 Presentarán las transacciones y las imágenes de los cheques que superen el monto es-
tablecido como límite de truncamiento que fueron diferidas por feriado local.
Para lograr la conciliación de la posición final de débitos y créditos, las entidades deberán conside-
rar la siguiente información:
Entidad depositaria: conciliación de posición de presentados: Créditos
 Movimientos enviados.
 Movimientos diferidos por feriado local presentados por las cámaras.
Cámaras electrónicas:
 Distribuirán a las entidades las transacciones alcanzadas por el feriado local.
 Distribuirán las posiciones incluyendo las transacciones diferidas por feriado local.
Entidad girada: conciliación de la posición de presentados: Débitos
 Movimientos compensados recibidos.
 Movimientos diferidos por feriado local recibidos por las cámaras.
Día D + 1
Las entidades podrán presentar los rechazos como entidades depositarias y entidades giradas
que no debieron presentar el día anterior, correspondiente a los movimientos diferidos por feriado
local.
```

Versión: primer intento (cola). Entidades 19, relaciones 34.
- {"local_id": "to", "type": "TextoOrdenado", "label": "SNP Cheques", "properties": {}, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Definicion", "label": "Feriado local previsto", "properties": {"termino": "feriado local previsto", "descripcion": "Aquel declarado por autoridad competente (nacional, provincial, municipal o Ciudad Autónoma de Buenos Aires), que permita ser incluido con antelación en un calendario de feriados locales."}, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- {"local_id": "e2", "type": "Definicion", "label": "Feriado local imprevisto", "properties": {"termino": "feriado local imprevisto", "descripcion": "Aquel declarado por autoridad competente (nacional, provincial, municipal o Ciudad Autónoma de Buenos Aires), que no pueda ser incluido con anterioridad en el calendario administrado por las CEC, pero que sea conocido por éstas a través de la información brindada formalmente por el/los banco/s presente/s en la plaza, como máximo hasta las 17 horas de
- {"local_id": "e3", "type": "Obligacion", "label": "Administración de calendario de feriados locales", "properties": {"tipo": "otra", "descripcion": "Las CEC administrarán un calendario de feriados locales a través de un sitio web, que incluirá las fechas de los feriados previstos para los diferentes puntos de intercambio y será actualizado con la información que deberán proveer las entidades financieras."}, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_docu
- {"local_id": "e4", "type": "Obligacion", "label": "Provisión de información de feriados locales", "properties": {"tipo": "otra", "descripcion": "Las entidades financieras deberán proveer la información de feriados locales para la actualización del sitio web administrado por las CEC."}, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- {"local_id": "e5", "type": "Obligacion", "label": "Identificación de movimientos con feriado local", "properties": {"tipo": "otra", "descripcion": "La CEC identificará los movimientos con código postal bancario con fecha de compensación del día feriado y los retendrá sin distribuirlos a las entidades giradas."}, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- {"local_id": "e6", "type": "Obligacion", "label": "Rechazo de movimientos con código R09", "properties": {"tipo": "otra", "descripcion": "La CEC rechazará los movimientos en la sesión de rechazados del día del feriado local utilizando el código R09 'feriado local'."}, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- {"local_id": "e7", "type": "Obligacion", "label": "Presentación de movimientos en día hábil siguiente", "properties": {"tipo": "otra", "descripcion": "La CEC presentará los movimientos en la sesión de presentados inmediata siguiente con fecha de compensación del día hábil siguiente, distribuyendo a las entidades giradas la información de las transacciones correspondientes al punto de intercambio que tuvo feriado local."}, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.
- {"local_id": "e8", "type": "Obligacion", "label": "Retención de transacciones en sesión de presentados (Día D-1)", "properties": {"tipo": "otra", "descripcion": "La CEC identificará las transacciones con feriado local presentadas por las entidades depositarias en la sesión de presentados del día anterior al feriado local y las retendrá junto con las imágenes de los cheques que superen el monto establecido como límite de truncamiento, sin distribuirlas a las entidades giradas."}, "provenance": {"
- {"local_id": "e9", "type": "Obligacion", "label": "Consideración de transacciones retenidas en posición de inicio", "properties": {"tipo": "otra", "descripcion": "Las entidades depositarias deberán considerar que parte de las transacciones presentadas no aplicarán en la posición de inicio de ese ciclo, ya que serán retenidas por la Cámara. Dichas transacciones se mostrarán por separado en los listados de posición de inicio de ciclo y en el listado bilateral, aunque sin ser contabilizadas en esa 
- {"local_id": "e10", "type": "Obligacion", "label": "Distribución de rechazos antes de las 12:00 (Día D)", "properties": {"tipo": "otra", "descripcion": "Las entidades y cámaras electrónicas distribuirán a las entidades depositarias de la plaza con feriado local los rechazos generados con su respectivo total antes de las 12:00.", "umbrales": "Antes de las 12.00"}, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 10}
- {"local_id": "e11", "type": "Restriccion", "label": "Prohibición de presentación de rechazos de entidad depositaria", "properties": {"tipo": "prohibicion", "descripcion": "La entidad depositaria no podrá presentar rechazos de entidad depositaria para los cheques diferidos por feriado local."}, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 11}
- {"local_id": "e12", "type": "Obligacion", "label": "Devolución de rechazos por feriado local", "properties": {"tipo": "otra", "descripcion": "Las cámaras electrónicas devolverán los posibles rechazos, tanto de entidad depositaria como de entidad girada, para aquellos cheques que fueron diferidos por feriado local."}, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 12}
- {"local_id": "e13", "type": "Restriccion", "label": "Prohibición de presentación de rechazos de entidad girada", "properties": {"tipo": "prohibicion", "descripcion": "La entidad girada no deberá presentar rechazos de entidad girada para los cheques diferidos por feriado local."}, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 13}
- {"local_id": "e14", "type": "Obligacion", "label": "Inclusión de movimientos rechazados en posiciones consolidadas", "properties": {"tipo": "otra", "descripcion": "Las cámaras electrónicas incluirán en las posiciones consolidadas los movimientos rechazados por feriado local."}, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 14}
- {"local_id": "e15", "type": "Obligacion", "label": "Presentación de transacciones diferidas por feriado local", "properties": {"tipo": "otra", "descripcion": "Las cámaras electrónicas presentarán las transacciones y las imágenes de los cheques que superen el monto establecido como límite de truncamiento que fueron diferidas por feriado local."}, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 15}
- {"local_id": "e16", "type": "Obligacion", "label": "Distribución de transacciones alcanzadas por feriado local", "properties": {"tipo": "otra", "descripcion": "Las cámaras electrónicas distribuirán a las entidades las transacciones alcanzadas por el feriado local."}, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 16}
- {"local_id": "e17", "type": "Obligacion", "label": "Distribución de posiciones incluyendo transacciones diferidas", "properties": {"tipo": "otra", "descripcion": "Las cámaras electrónicas distribuirán las posiciones incluyendo las transacciones diferidas por feriado local."}, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 17}
- {"local_id": "e18", "type": "Potestad", "label": "Presentación de rechazos diferidos (Día D+1)", "properties": {"descripcion": "Las entidades podrán presentar los rechazos como entidades depositarias y entidades giradas que no debieron presentar el día anterior, correspondiente a los movimientos diferidos por feriado local."}, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 18}
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e3", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e4", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- relación: {"source": "e5", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- relación: {"source": "e6", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- relación: {"source": "e7", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- relación: {"source": "e8", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 7}
- relación: {"source": "e9", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 8}
- relación: {"source": "e10", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 9}
- relación: {"source": "e11", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 10}
- relación: {"source": "e12", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 11}
- relación: {"source": "e13", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 12}
- relación: {"source": "e14", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 13}
- relación: {"source": "e15", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 14}
- relación: {"source": "e16", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 15}
- relación: {"source": "e17", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 16}
- relación: {"source": "e18", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 17}
- relación: {"source": "e3", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_camara_electronica_de_compensacion", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 18}
- relación: {"source": "e4", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 19}
- relación: {"source": "e5", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_camara_electronica_de_compensacion", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 20}
- relación: {"source": "e6", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_camara_electronica_de_compensacion", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 21}
- relación: {"source": "e7", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_camara_electronica_de_compensacion", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 22}
- relación: {"source": "e8", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_camara_electronica_de_compensacion", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 23}
- relación: {"source": "e9", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_depositaria", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 24}
- relación: {"source": "e10", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_camara_electronica_de_compensacion", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 25}
- relación: {"source": "e11", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_depositaria", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 26}
- relación: {"source": "e12", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_camara_electronica_de_compensacion", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 27}
- relación: {"source": "e13", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_girada", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 28}
- relación: {"source": "e14", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_camara_electronica_de_compensacion", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 29}
- relación: {"source": "e15", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_camara_electronica_de_compensacion", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 30}
- relación: {"source": "e16", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_camara_electronica_de_compensacion", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 31}
- relación: {"source": "e17", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_camara_electronica_de_compensacion", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 32}
- relación: {"source": "e18", "target": null, "predicate": "aplica_a", "sujeto_id": null, "sujeto_propuesto": "Las entidades", "sujeto_propuesto_padre_sugerido": "Sujeto_entidad_financiera", "provenance": {"to": "snp_cheq", "archivo": "snp_cheq.pdf", "punto": "3.1.4.2", "rol_documental": "punto_propio"}, "indice_crudo": 33}

## 23. `manori::1.1.6.4` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 11):

```
[encabezado | punto S1]
Sección 1. Manual de Originación y Administración de Préstamos Hipotecarios.
[encabezado | punto 1.1]
1.1. Características y lineamientos para el otorgamiento de préstamos hipotecarios.
[encabezado | punto 1.1.6]
1.1.6. Relación Cuota / Ingreso.
[texto propio | punto 1.1.6.4]
1.1.6.4. Pautas específicas.
a) Sistema francés.
− A tasa fija, la cuota se calculará utilizando dicha tasa.
− A tasa variable, la cuota se calculará con la tasa inicial incrementada en
un 25 % (por ejemplo, si la tasa inicial es 10 % se utilizará 12,50 %). Si
existiese una tasa máxima establecida, se utilizará dicha tasa máxima.
b) Sistema alemán.
− A tasa fija, se utilizará el promedio de las cuotas correspondientes al pri-
mer 25 % del plazo del préstamo.
− A tasa variable, se utilizará el promedio de las cuotas correspondientes al
primer 25 % del plazo del préstamo que se calculará con la tasa inicial in-
crementada en un 25 % (por ejemplo, si la tasa inicial es 10 % se utilizará
12,50 %). Si existiese una tasa máxima establecida, se utilizará dicha ta-
sa máxima.
c) Otros sistemas.
Se utilizará la metodología que la entidad financiera considere conveniente
al efecto de una evaluación conservadora de la relación cuota / ingreso, to-
mando como referencia los criterios establecidos en los apartados a) y b)
precedentes.
```

Versión: primer intento (cola). Entidades 7, relaciones 13.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Manual de Originación y Administración de Préstamos Hipotecarios", "properties": {}, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.1.6.4", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Operacion", "label": "Cálculo de cuota — Sistema francés a tasa fija", "properties": {"tipo": "Cálculo de cuota", "descripcion": "En sistema francés a tasa fija, la cuota se calculará utilizando dicha tasa."}, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.1.6.4", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- {"local_id": "e2", "type": "Operacion", "label": "Cálculo de cuota — Sistema francés a tasa variable", "properties": {"tipo": "Cálculo de cuota", "descripcion": "En sistema francés a tasa variable, la cuota se calculará con la tasa inicial incrementada en un 25 %. Si existe tasa máxima establecida, se utilizará dicha tasa máxima.", "incremento_tasa": "25 %", "ejemplo": "si la tasa inicial es 10 % se utilizará 12,50 %"}, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.1.6.4", 
- {"local_id": "e3", "type": "Operacion", "label": "Cálculo de cuota — Sistema alemán a tasa fija", "properties": {"tipo": "Cálculo de cuota", "descripcion": "En sistema alemán a tasa fija, se utilizará el promedio de las cuotas correspondientes al primer 25 % del plazo del préstamo.", "base_calculo": "promedio de cuotas del primer 25 % del plazo"}, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.1.6.4", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- {"local_id": "e4", "type": "Operacion", "label": "Cálculo de cuota — Sistema alemán a tasa variable", "properties": {"tipo": "Cálculo de cuota", "descripcion": "En sistema alemán a tasa variable, se utilizará el promedio de las cuotas correspondientes al primer 25 % del plazo del préstamo, calculado con la tasa inicial incrementada en un 25 %. Si existe tasa máxima establecida, se utilizará dicha tasa máxima.", "incremento_tasa": "25 %", "base_calculo": "promedio de cuotas del primer 25 % del pl
- {"local_id": "e5", "type": "Potestad", "label": "Metodología discrecional — Otros sistemas de amortización", "properties": {"descripcion": "Para otros sistemas de amortización, la entidad financiera puede utilizar la metodología que considere conveniente para una evaluación conservadora de la relación cuota/ingreso, tomando como referencia los criterios de los sistemas francés y alemán."}, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.1.6.4", "rol_documental": "punto_propio
- {"local_id": "e6", "type": "Condicion", "label": "Existencia de tasa máxima establecida", "properties": {"descripcion": "Cuando existe una tasa máxima establecida en el préstamo."}, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.1.6.4", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.1.6.4", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.1.6.4", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e3", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.1.6.4", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e4", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.1.6.4", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- relación: {"source": "e5", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.1.6.4", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- relación: {"source": "e6", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.1.6.4", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- relación: {"source": "e1", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.1.6.4", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- relación: {"source": "e2", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.1.6.4", "rol_documental": "punto_propio"}, "indice_crudo": 7}
- relación: {"source": "e3", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.1.6.4", "rol_documental": "punto_propio"}, "indice_crudo": 8}
- relación: {"source": "e4", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.1.6.4", "rol_documental": "punto_propio"}, "indice_crudo": 9}
- relación: {"source": "e5", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.1.6.4", "rol_documental": "punto_propio"}, "indice_crudo": 10}
- relación: {"source": "e6", "target": "e2", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.1.6.4", "rol_documental": "punto_propio"}, "indice_crudo": 11}
- relación: {"source": "e6", "target": "e4", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "manori", "archivo": "manori.pdf", "punto": "1.1.6.4", "rol_documental": "punto_propio"}, "indice_crudo": 12}

## 24. `lingeef::11.1.2` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 151):

```
[encabezado | punto S11]
Sección 11. Realización de pruebas de estrés.
[encabezado | punto 11.1]
11.1. Conceptos.
[intro | punto 11.1]
Una prueba de estrés se define generalmente como la evaluación de la posición financiera de
una entidad en un escenario severamente adverso pero posible. A los fines de estos linea-
mientos, este término se utilizará para referirse no sólo a los mecanismos por los cuales se
aplican las pruebas individuales sino también al entorno en el cual esas pruebas se desarro-
llan, evalúan y utilizan en el proceso de toma de decisiones de las entidades.
Las pruebas de estrés complementan a otras herramientas de gestión y tienen un rol particu-
larmente importante a fin de:
[texto propio | punto 11.1.2]
11.1.2. Superar las limitaciones de los modelos y datos históricos;
```

Versión: primer intento (cola). Entidades 2, relaciones 1.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Lineamientos Entidades Financieras", "properties": {}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "11.1.2", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Obligacion", "label": "Superar limitaciones modelos datos históricos", "properties": {"descripcion": "Las entidades deben superar las limitaciones de los modelos y datos históricos en la realización de pruebas de estrés.", "tipo": "otra"}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "11.1.2", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "11.1.2", "rol_documental": "punto_propio"}, "indice_crudo": 0}

## 25. `lingeef::5.3.4.4` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 101):

```
[encabezado | punto S5]
Sección 5. Gestión del riesgo de tasa de interés en la cartera de inversión.
[encabezado | punto 5.3]
5.3. Proceso de gestión del riesgo de tasa de interés en la cartera de inversión.
[encabezado | punto 5.3.4]
5.3.4. Reporte de los resultados de la medición al Directorio o a sus delegados.
[intro | punto 5.3.4]
Los resultados de la medición del RTICI y las estrategias de cobertura deben ser repor-
tados al Directorio o a sus delegados periódicamente, con un adecuado nivel de agre-
gación –por nivel de consolidación y moneda– y una comparación de la exposición vi-
gente con los límites establecidos.
Aunque los tipos de informes elaborados para el Directorio o sus delegados variarán
en función de la composición de la cartera de cada entidad, deben incluir como mínimo
lo siguiente:
[texto propio | punto 5.3.4.4]
5.3.4.4. Resultados de las pruebas de estrés, incluyendo una evaluación de la sensibi-
lidad a los supuestos y parámetros clave.
```

Versión: primer intento (cola). Entidades 2, relaciones 2.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Gestión del riesgo de tasa de interés", "properties": {}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.3.4.4", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Obligacion", "label": "Incluir resultados de pruebas de estrés en reportes", "properties": {"descripcion": "Los informes al Directorio o sus delegados deben incluir como mínimo los resultados de las pruebas de estrés, incluyendo una evaluación de la sensibilidad a los supuestos y parámetros clave", "tipo": "presentacion_informativa", "frecuencia": "periódicamente"}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.3.4.4", "rol_documental": "punto_
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.3.4.4", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e1", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_financiera", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "5.3.4.4", "rol_documental": "punto_propio"}, "indice_crudo": 1}

## 26. `cajasc::3.7.3` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 20):

```
[encabezado | punto S3]
Sección 3. Operaciones pasivas.
[encabezado | punto 3.7]
3.7. Concentración de depósitos del sector privado no financiero.
[intro | punto 3.7]
El importe total consolidado que registre cada titular, no podrá exceder a partir del segundo
mes posterior al inicio de actividades, los siguientes límites:
[texto propio | punto 3.7.3]
3.7.3. A partir del tercer año de funcionamiento de la caja de crédito cooperativa:
5 % del total de depósitos (capitales) en la entidad o 30 % de la RPC, de ambos el ma-
yor.
```

Versión: primer intento (cola). Entidades 3, relaciones 4.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Cajas de crédito cooperativas", "properties": {}, "provenance": {"to": "cajasc", "archivo": "cajasc.pdf", "punto": "3.7.3", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Restriccion", "label": "Límite concentración depósitos — tercer año", "properties": {"tipo": "limite_cuantitativo", "descripcion": "A partir del tercer año de funcionamiento, el importe total consolidado por titular no podrá exceder el 5 % del total de depósitos en la entidad o el 30 % de la RPC, de ambos el mayor.", "umbrales": "5 % del total de depósitos (capitales) en la entidad | 30 % de la RPC"}, "provenance": {"to": "cajasc", "archivo": "cajasc.pdf", "punto": "3
- {"local_id": "e2", "type": "Condicion", "label": "Condición temporal — tercer año funcionamiento", "properties": {"descripcion": "La restricción se aplica a partir del tercer año de funcionamiento de la caja de crédito cooperativa.", "umbrales": "tercer año"}, "provenance": {"to": "cajasc", "archivo": "cajasc.pdf", "punto": "3.7.3", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "cajasc", "archivo": "cajasc.pdf", "punto": "3.7.3", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "cajasc", "archivo": "cajasc.pdf", "punto": "3.7.3", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e2", "target": "e1", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "cajasc", "archivo": "cajasc.pdf", "punto": "3.7.3", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e1", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_cliente", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "cajasc", "archivo": "cajasc.pdf", "punto": "3.7.3", "rol_documental": "punto_propio"}, "indice_crudo": 3}

## 27. `lingeef::6.1.3.7` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 120):

```
[encabezado | punto S6]
Sección 6. Gestión del riesgo operacional.
[encabezado | punto 6.1]
6.1. Conceptos.
[encabezado | punto 6.1.3]
6.1.3. Eventos de pérdida.
[intro | punto 6.1.3]
Se indica a continuación la lista taxativa de las categorías –a los fines de las presentes
disposiciones– para la clasificación de los eventos de pérdida derivados del riesgo
operacional, incluyendo algunos ejemplos de los conceptos que integrarían cada una de
ellas:
[texto propio | punto 6.1.3.7]
6.1.3.7. Ejecución, gestión y cumplimiento del plazo de los procesos: errores en la intro-
ducción de datos, fallas en la administración de garantías, documentación jurídi-
ca incompleta, concesión de acceso no autorizado a las cuentas de los clientes,
litigios con proveedores, etc.
```

Versión: primer intento (cola). Entidades 2, relaciones 1.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Gestión del riesgo operacional", "properties": {}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "6.1.3.7", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Definicion", "label": "Eventos de pérdida — Ejecución y gestión de procesos", "properties": {"termino": "Eventos de pérdida — Ejecución, gestión y cumplimiento del plazo de los procesos", "descripcion": "Categoría de eventos de pérdida derivados del riesgo operacional que incluye: errores en la introducción de datos, fallas en la administración de garantías, documentación jurídica incompleta, concesión de acceso no autorizado a las cuentas de los clientes, litigios co
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "6.1.3.7", "rol_documental": "punto_propio"}, "indice_crudo": 0}

## 28. `lingeef::6.1.3.3` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 120):

```
[encabezado | punto S6]
Sección 6. Gestión del riesgo operacional.
[encabezado | punto 6.1]
6.1. Conceptos.
[encabezado | punto 6.1.3]
6.1.3. Eventos de pérdida.
[intro | punto 6.1.3]
Se indica a continuación la lista taxativa de las categorías –a los fines de las presentes
disposiciones– para la clasificación de los eventos de pérdida derivados del riesgo
operacional, incluyendo algunos ejemplos de los conceptos que integrarían cada una de
ellas:
[texto propio | punto 6.1.3.3]
6.1.3.3. Relaciones laborales y seguridad en el puesto de trabajo: reclamos de indemni-
zaciones por parte de los empleados, infracciones a las normas laborales de se-
guridad e higiene, de discriminación, responsabilidades generales, etc.
```

Versión: primer intento (cola). Entidades 2, relaciones 1.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Gestión del riesgo operacional", "properties": {}, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "6.1.3.3", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Definicion", "label": "Categoría eventos pérdida: relaciones laborales", "properties": {"termino": "Relaciones laborales y seguridad en el puesto de trabajo", "descripcion": "Categoría de eventos de pérdida derivados del riesgo operacional que incluye reclamos de indemnizaciones por parte de los empleados, infracciones a las normas laborales de seguridad e higiene, de discriminación, responsabilidades generales, etc."}, "provenance": {"to": "lingeef", "archivo": "ling
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "lingeef", "archivo": "lingeef.pdf", "punto": "6.1.3.3", "rol_documental": "punto_propio"}, "indice_crudo": 0}

## 29. `depaho::4.19.4` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 78, 79):

```
[encabezado | punto S4]
Sección 4. Disposiciones generales.
[encabezado | punto 4.19]
4.19. Caja de ahorros repatriación de fondos - Bienes Personales Ley 27.541.
[texto propio | punto 4.19.4]
4.19.4. Otras disposiciones.
Los fondos repatriados del exterior en el marco de la Ley 27.541 –y sus decretos re-
glamentarios– con anterioridad al 08/02/2020 que hayan sido depositados en cajas de
ahorros en moneda extranjera –y eventualmente aplicados a la constitución o renova-
ción de plazos fijos–, serán considerados encuadrados a solicitud del declarante en el
marco de estas disposiciones.
En estos casos, las entidades financieras deberán proceder a la apertura de una “Caja
de ahorros repatriación de fondos - Bienes Personales Ley 27.541” y transferir allí los
fondos pertinentes.
```

Versión: primer intento (cola). Entidades 6, relaciones 11.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Depósitos de ahorro", "properties": {}, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "4.19.4", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Operacion", "label": "Depósito de fondos repatriados en caja de ahorros", "properties": {"tipo": "depósito en caja de ahorros", "descripcion": "Depósito de fondos repatriados del exterior conforme a la Ley 27.541 y sus decretos reglamentarios, realizados antes del 08/02/2020, en cajas de ahorros en moneda extranjera, eventualmente aplicados a la constitución o renovación de plazos fijos."}, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "4.19.4", "ro
- {"local_id": "e2", "type": "Condicion", "label": "Fondos repatriados antes de 08/02/2020", "properties": {"descripcion": "Los fondos deben haber sido repatriados antes del 08/02/2020.", "umbrales": "con anterioridad al 08/02/2020"}, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "4.19.4", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- {"local_id": "e3", "type": "Condicion", "label": "Fondos depositados en cajas de ahorros en moneda extranjera", "properties": {"descripcion": "Los fondos deben haber sido depositados en cajas de ahorros en moneda extranjera."}, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "4.19.4", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- {"local_id": "e4", "type": "Obligacion", "label": "Apertura de caja de ahorros repatriación de fondos", "properties": {"tipo": "asignacion", "descripcion": "Las entidades financieras deberán proceder a la apertura de una cuenta denominada 'Caja de ahorros repatriación de fondos - Bienes Personales Ley 27.541'."}, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "4.19.4", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- {"local_id": "e5", "type": "Obligacion", "label": "Transferencia de fondos a caja de ahorros repatriación", "properties": {"tipo": "otra", "descripcion": "Las entidades financieras deberán transferir los fondos pertinentes a la caja de ahorros repatriación de fondos abierta."}, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "4.19.4", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- relación: {"source": "e1", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "4.19.4", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e2", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "4.19.4", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e3", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "4.19.4", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e4", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "4.19.4", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- relación: {"source": "e5", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "4.19.4", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- relación: {"source": "e2", "target": "e1", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "4.19.4", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- relación: {"source": "e3", "target": "e1", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "4.19.4", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- relación: {"source": "e4", "target": "e1", "predicate": "condiciona", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "4.19.4", "rol_documental": "punto_propio"}, "indice_crudo": 7}
- relación: {"source": "e5", "target": "e1", "predicate": "condiciona", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "4.19.4", "rol_documental": "punto_propio"}, "indice_crudo": 8}
- relación: {"source": "e4", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_rol_alcance_depaho", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "4.19.4", "rol_documental": "punto_propio"}, "indice_crudo": 9}
- relación: {"source": "e5", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_rol_alcance_depaho", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "4.19.4", "rol_documental": "punto_propio"}, "indice_crudo": 10}

## 30. `depaho::2.8.1` — NG:resto · cola

Texto que vio E3 (e0, bloque de lista True; págs. 18):

```
[encabezado | punto S2]
Sección 2. Cuenta sueldo/de la seguridad social.
[encabezado | punto 2.8]
2.8. Cierre de cuentas.
[texto propio | punto 2.8.1]
2.8.1. Cuenta sueldo.
El cierre de las cuentas deberá ser comunicado por el empleador o por el trabajador
cuando la apertura haya sido tramitada por el empleador. En el caso de que dicha
apertura haya sido solicitada por el trabajador, el cierre deberá ser comunicado exclu-
sivamente por este último. En ambos casos el trabajador podrá utilizar mecanismos
electrónicos de comunicación, conforme a lo previsto en el punto 4.17.
Se hará efectivo luego de transcurridos 180 días corridos, contados desde la fecha de
la última acreditación de fondos o de la comunicación –la que sea posterior–, siendo
aplicable en ese lapso lo establecido en el punto 2.6. En el caso de existir servicios
adicionales contratados en el marco del punto 2.12., cuando la desvinculación laboral
genere la pérdida de beneficios y/o el cobro de comisiones asociados a esos servicios,
dicha circunstancia deberá ser informada al titular previamente al devengamiento de
tales conceptos –de conformidad con lo previsto en el punto 1.10.4.–.
Sin perjuicio de ello, cuando la entidad financiera depositaria reciba del correspondien-
te ente administrador de pago de las prestaciones de la seguridad social acreditacio-
nes por este último concepto con destino a estas cuentas, su cierre operará de acuer-
do con el procedimiento que establezca el mencionado ente o, en su defecto, cuando
no se hayan registrado esas acreditaciones durante el plazo de 730 días corridos.
```

Versión: primer intento (cola). Entidades 11, relaciones 13.
- {"local_id": "to", "type": "TextoOrdenado", "label": "Depósitos de ahorro", "properties": {}, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "2.8.1", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- {"local_id": "e1", "type": "Operacion", "label": "Cierre de cuenta sueldo", "properties": {"tipo": "Cierre de cuenta", "descripcion": "Cierre de cuenta sueldo comunicado por el empleador o por el trabajador según quién haya tramitado la apertura"}, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "2.8.1", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- {"local_id": "e2", "type": "Operacion", "label": "Cierre de cuenta sueldo por trabajador", "properties": {"tipo": "Cierre de cuenta", "descripcion": "Cierre de cuenta sueldo comunicado exclusivamente por el trabajador cuando la apertura fue solicitada por él"}, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "2.8.1", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- {"local_id": "e3", "type": "Obligacion", "label": "Comunicación de cierre — empleador o trabajador", "properties": {"tipo": "comunicacion_a_cliente", "descripcion": "El empleador o el trabajador debe comunicar el cierre de la cuenta sueldo cuando la apertura haya sido tramitada por el empleador"}, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "2.8.1", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- {"local_id": "e4", "type": "Obligacion", "label": "Comunicación de cierre — trabajador exclusivamente", "properties": {"tipo": "comunicacion_a_cliente", "descripcion": "El trabajador debe comunicar exclusivamente el cierre de la cuenta sueldo cuando la apertura fue solicitada por él"}, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "2.8.1", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- {"local_id": "e5", "type": "Potestad", "label": "Uso de mecanismos electrónicos para comunicación de cierre", "properties": {"descripcion": "El trabajador puede utilizar mecanismos electrónicos de comunicación para comunicar el cierre de la cuenta sueldo"}, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "2.8.1", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- {"local_id": "e6", "type": "Condicion", "label": "Transcurso de 180 días corridos desde última acreditación", "properties": {"descripcion": "El cierre se hace efectivo después de que transcurran 180 días corridos desde la última acreditación de fondos o desde la comunicación, la que sea posterior", "umbrales": "180 días corridos"}, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "2.8.1", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- {"local_id": "e7", "type": "Obligacion", "label": "Información previa sobre pérdida de beneficios y comisiones", "properties": {"tipo": "comunicacion_a_cliente", "descripcion": "La entidad financiera debe informar al titular previamente al devengamiento de comisiones cuando la desvinculación laboral genere pérdida de beneficios y/o cobro de comisiones asociados a servicios adicionales"}, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "2.8.1", "rol_documental": "punto_propio"}, 
- {"local_id": "e8", "type": "Condicion", "label": "Existencia de servicios adicionales contratados", "properties": {"descripcion": "Cuando existen servicios adicionales contratados en el marco del punto 2.12 y la desvinculación laboral genera pérdida de beneficios y/o cobro de comisiones"}, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "2.8.1", "rol_documental": "punto_propio"}, "indice_crudo": 8}
- {"local_id": "e9", "type": "Operacion", "label": "Cierre de cuenta sueldo por acreditaciones de seguridad social", "properties": {"tipo": "Cierre de cuenta", "descripcion": "Cierre de cuenta sueldo de seguridad social según el procedimiento establecido por el ente administrador de pago de prestaciones"}, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "2.8.1", "rol_documental": "punto_propio"}, "indice_crudo": 9}
- {"local_id": "e10", "type": "Condicion", "label": "Transcurso de 730 días sin acreditaciones de seguridad social", "properties": {"descripcion": "El cierre opera cuando no se han registrado acreditaciones de seguridad social durante 730 días corridos", "umbrales": "730 días corridos"}, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "2.8.1", "rol_documental": "punto_propio"}, "indice_crudo": 10}
- relación: {"source": "e3", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "2.8.1", "rol_documental": "punto_propio"}, "indice_crudo": 0}
- relación: {"source": "e4", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "2.8.1", "rol_documental": "punto_propio"}, "indice_crudo": 1}
- relación: {"source": "e5", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "2.8.1", "rol_documental": "punto_propio"}, "indice_crudo": 2}
- relación: {"source": "e6", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "2.8.1", "rol_documental": "punto_propio"}, "indice_crudo": 3}
- relación: {"source": "e7", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "2.8.1", "rol_documental": "punto_propio"}, "indice_crudo": 4}
- relación: {"source": "e8", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "2.8.1", "rol_documental": "punto_propio"}, "indice_crudo": 5}
- relación: {"source": "e10", "target": "to", "predicate": "establecida_en", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "2.8.1", "rol_documental": "punto_propio"}, "indice_crudo": 6}
- relación: {"source": "e6", "target": "e1", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "2.8.1", "rol_documental": "punto_propio"}, "indice_crudo": 7}
- relación: {"source": "e8", "target": "e7", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "2.8.1", "rol_documental": "punto_propio"}, "indice_crudo": 8}
- relación: {"source": "e10", "target": "e9", "predicate": "condicion_de", "sujeto_id": null, "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "2.8.1", "rol_documental": "punto_propio"}, "indice_crudo": 9}
- relación: {"source": "e3", "target": null, "predicate": "aplica_a", "sujeto_id": null, "sujeto_propuesto": "el empleador o por el trabajador", "sujeto_propuesto_padre_sugerido": "Sujeto_sujeto", "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "2.8.1", "rol_documental": "punto_propio"}, "indice_crudo": 10}
- relación: {"source": "e4", "target": null, "predicate": "aplica_a", "sujeto_id": null, "sujeto_propuesto": "el trabajador", "sujeto_propuesto_padre_sugerido": "Sujeto_sujeto", "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "2.8.1", "rol_documental": "punto_propio"}, "indice_crudo": 11}
- relación: {"source": "e7", "target": null, "predicate": "aplica_a", "sujeto_id": "Sujeto_entidad_depositaria", "sujeto_propuesto": null, "sujeto_propuesto_padre_sugerido": null, "provenance": {"to": "depaho", "archivo": "depaho.pdf", "punto": "2.8.1", "rol_documental": "punto_propio"}, "indice_crudo": 12}

