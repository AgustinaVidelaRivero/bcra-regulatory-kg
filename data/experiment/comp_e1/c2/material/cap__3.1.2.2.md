# `cap::3.1.2.2` — Al calcular los activos ponderados por riesgo, la entidad originante podrá excluir

Grupos: omisiones. Estado final en la tanda 0: `aceptado_con_residuales`.

## Texto

> *heredado:* Sección 3. Capital mínimo por riesgo de crédito. Titulizaciones e inversiones en fondos.
> *heredado:* 3.1. Tratamiento de las titulizaciones.
> *heredado:* Se denomina "posición de titulización" a la exposición a una titulización (o retitulización), tradicional o sintética, o a una estructura con similares características. La exposición a los riesgos de una titulización puede surgir, entre otros, de los siguientes conceptos: tenencia de títulos valores emitidos en el marco de la titulización –es decir, títulos de deuda y/o certificados de participación, tales como bonos de titulización de activos ("AssetBacked Securities", ABS) y bonos de titulización hipotecaria ("Mortgage-Backed Securities", MBS)–, mejoras crediticias, facilidades de liquidez, "swaps" de tasa de interés o de monedas y derivados de crédito. Las reservas ("reserve accounts"), tales como las cuentas de garantía en efectivo, se considerarán como un activo para la entidad financiera originante, recibiendo también el tratamiento de posiciones de titulización. Dado que las titulizaciones pueden estructurarse de diferentes formas, la exigencia de capital para una posición de titulización se determinará teniendo en cuenta su realidad o finalidad económica y no su forma jurídica. En los casos en que exista incertidumbre acerca de si una determinada operación debe considerarse como titulización, la entidad deberá aplicar el criterio que estime mejor se ajusta a la realidad económica de la operación e informar a la SEFyC los fundamentos que lo sustenten.
> *heredado:* 3.1.2. Entidad financiera originante.
> *propio:* 3.1.2.2. Al calcular los activos ponderados por riesgo, la entidad originante podrá excluir las exposiciones objeto de una titulización tradicional sólo si se satisface la totalidad de los siguientes requisitos operativos –debiendo computar exigencia de capital por las posiciones de titulización que conserve–: i) Se ha transferido a uno o más terceros el riesgo de crédito asociado a las exposiciones titulizadas. ii) La entidad cedente no mantiene un control directo ni indirecto (como ser a través de una sociedad controlada) sobre las exposiciones transferidas. Ellas han sido aisladas de la cedente a los efectos jurídicos de forma tal que están fuera de su alcance y del de sus acreedores, incluso en los casos de liquidación o quiebra. Estas condiciones deberán estar avaladas por dictamen jurídico. Se considera que la cedente mantiene el control efectivo de las exposiciones transferidas si: a) puede recomprarlas con el objeto de realizar sus beneficios, o b) está obligada a conservar su riesgo. El mantenimiento por parte de la cedente de la administración de las exposiciones subyacentes no implicará un control indirecto sobre ellas. iii) Los títulos valores emitidos no son obligaciones de la cedente. En consecuencia, los inversores que compren los títulos valores sólo deberán tener derechos frente al conjunto subyacente de exposiciones. iv)La cesión se ha efectuado a un "Ente de Propósito Especial" (SPE) y los inversores pueden gravar o enajenar sus títulos valores sin restricción. v) Las opciones de exclusión satisfacen las condiciones estipuladas en el punto 3.1.4. vi)La titulización no contiene cláusulas mediante las cuales: a) se obligue a la originante a alterar las exposiciones subyacentes con el objeto de mejorar su calidad crediticia, a menos que esto se logre mediante su venta –a precios de mercado– a terceros no vinculados a ésta; b) la entidad financiera deba incrementar su posición a primera pérdida –es decir, su exposición al tramo que absorbe las pérdidas en primer término– o aumentar las mejoras crediticias provistas, con posterioridad al inicio de la operación; o c) se aumente el rendimiento pagadero a las partes distintas de la originante, como pueden ser los inversores o terceros proveedores de mejoras crediticias, en respuesta a un deterioro de la calidad crediticia de las exposiciones subyacentes. vii) No se incluyen opciones de rescisión o eventos desencadenantes de la extinción del contrato –excepto que se trate de opciones de exclusión admitidas (punto 3.1.4.) o que la extinción se deba a cambios impositivos o regulatorios específicos–, ni se incluyen cláusulas de amortización anticipada que –de acuerdo con lo previsto en el punto 3.1.8.1.– impliquen que la titulización no cumple con los requerimientos operacionales del presente punto.

## Omisiones leídas en T4 (M2)

con_marca:15 [normativa; heredado] «En los casos en que exista incertidumbre acerca de si una determinada operación debe considerarse como titulización, la entidad deberá aplicar el criterio que estime mejor se ajusta a la realidad económica de la operación e informar a la SEFyC los fundamentos que lo sustenten»

## Código A

- Rechazos del validador r2: relacion:firma_invalida
- **op1 Operacion** «Exclusión de exposiciones titulizadas del cálculo de APR» — Exclusión, al calcular los activos ponderados por riesgo, de las exposiciones objeto de una titulización tradicional, por la entidad originante · props: `{"tipo": "otra"}` · tramo [exacta]: «podrá excluir las exposiciones objeto de una titulización tradicional»
- **pot1 Potestad** «Exclusión de exposiciones titulizadas de los APR» — La entidad originante puede excluir del cálculo de activos ponderados por riesgo las exposiciones objeto de una titulización tradicional, sólo si se satisface la totalidad de los requisitos operativos i) a vii) · tramo [exacta]: «Al calcular los activos ponderados por riesgo, la entidad originante podrá excluir las exposiciones objeto de una titulización tradicional sólo si se satisface la totalidad de los siguientes requisitos operativos»
- **ob1 Obligacion** «Computar capital por posiciones de titulización conservadas» — La entidad originante que excluye las exposiciones debe computar exigencia de capital por las posiciones de titulización que conserve · props: `{"tipo": "calculo"}` · tramo [exacta]: «debiendo computar exigencia de capital por las posiciones de titulización que conserve»
- **c1 Condicion** «Transferencia a terceros del riesgo de crédito» — Requisito i): se transfirió a uno o más terceros el riesgo de crédito asociado a las exposiciones titulizadas · tramo [exacta]: «Se ha transferido a uno o más terceros el riesgo de crédito asociado a las exposiciones titulizadas.»
- **c2 Condicion** «Cedente sin control y exposiciones aisladas» — Requisito ii): la cedente no mantiene control directo ni indirecto sobre las exposiciones transferidas, que han sido aisladas de la cedente a efectos jurídicos, fuera de su alcance y del de sus acreedores, incluso en liquidación o quiebra; estas condiciones deberán estar avaladas por dictamen jurídico. La administración de las exposiciones subyacentes por la cedente no implica control indirecto · tramo [exacta]: «La entidad cedente no mantiene un control directo ni indirecto (como ser a través de una sociedad controlada) sobre las exposiciones transferidas.»
- **c3 Condicion** «Títulos no son obligaciones de la cedente» — Requisito iii): los títulos valores emitidos no son obligaciones de la cedente; los inversores sólo deben tener derechos frente al conjunto subyacente de exposiciones · tramo [exacta]: «Los títulos valores emitidos no son obligaciones de la cedente.»
- **c4 Condicion** «Cesión a SPE y títulos libremente gravables o enajenables» — Requisito iv): la cesión se efectuó a un Ente de Propósito Especial (SPE) y los inversores pueden gravar o enajenar sus títulos valores sin restricción · tramo [no]: «La cesión se ha efectuado a un "Ente de Propósito Especial" (SPE) y los in-»
- **c5 Condicion** «Opciones de exclusión conformes al punto 3.1.4» — Requisito v): las opciones de exclusión satisfacen las condiciones estipuladas en el punto 3.1.4 · tramo [exacta]: «Las opciones de exclusión satisfacen las condiciones estipuladas en el punto»
- **c6 Condicion** «Sin cláusulas de alteración, mejora o mayor rendimiento» — Requisito vi): la titulización no contiene cláusulas que obliguen a la originante a alterar las exposiciones subyacentes para mejorar su calidad crediticia (salvo venta a precios de mercado a terceros no vinculados), que obliguen a incrementar su posición a primera pérdida o las mejoras crediticias tras el inicio de la operación, ni que aumenten el rendimiento pagadero a partes distintas de la ori… · tramo [exacta]: «La titulización no contiene cláusulas mediante las cuales:»
- **c7 Condicion** «Sin opciones de rescisión ni amortización anticipada incumplidora» — Requisito vii): no se incluyen opciones de rescisión o eventos desencadenantes de la extinción del contrato (excepto opciones de exclusión admitidas del punto 3.1.4 o extinción por cambios impositivos o regulatorios específicos), ni cláusulas de amortización anticipada que, según el punto 3.1.8.1, impliquen que la titulización no cumple los requerimientos operacionales · tramo [no]: «No se incluyen opciones de rescisión o eventos desencadenantes de la ex-»
- **d1 Definicion** «Control efectivo de la cedente sobre exposiciones transferidas» — Se considera que la cedente mantiene el control efectivo de las exposiciones transferidas si puede recomprarlas con el objeto de realizar sus beneficios, o está obligada a conservar su riesgo · props: `{"termino": "control efectivo"}` · tramo [exacta]: «Se considera que la cedente mantiene el control efectivo de las exposiciones transferidas si:»
- R: pot1 Potestad —aplica_a→ Sujeto (mención «la entidad originante»)
- R: ob1 Obligacion —aplica_a→ Sujeto (mención «la entidad originante»)
- R: Sujeto (mención «la entidad originante») —ejecuta→ op1 Operacion
- R: c1 Condicion —condicion_de→ pot1 Potestad
- R: c2 Condicion —condicion_de→ pot1 Potestad
- R: c3 Condicion —condicion_de→ pot1 Potestad
- R: c4 Condicion —condicion_de→ pot1 Potestad
- R: c5 Condicion —condicion_de→ pot1 Potestad
- R: c6 Condicion —condicion_de→ pot1 Potestad
- R: c7 Condicion —condicion_de→ pot1 Potestad

### A — omisiones de T4 a clasificar

- con_marca:15 → entidades: — | omisiones: —

## Código H

- **op1 Operacion** «Titulización tradicional — exclusión de exposiciones de APR» — Exclusión, al calcular los activos ponderados por riesgo, de las exposiciones objeto de una titulización tradicional por la entidad originante · props: `{"tipo": "otra"}` · tramo [exacta]: «excluir las exposiciones objeto de una titulización tradicional»
- **pot1 Potestad** «Excluir exposiciones titulizadas del cálculo de APR» — La entidad originante puede excluir del cálculo de activos ponderados por riesgo las exposiciones objeto de una titulización tradicional, sólo si se satisface la totalidad de los requisitos operativos i) a vii) · tramo [exacta]: «Al calcular los activos ponderados por riesgo, la entidad originante podrá excluir las exposiciones objeto de una titulización tradicional sólo si se satisface la totalidad de los siguientes requisitos operativos»
- **ob1 Obligacion** «Computar capital por posiciones de titulización conservadas» — La entidad originante debe computar exigencia de capital por las posiciones de titulización que conserve · props: `{"tipo": "calculo"}` · tramo [exacta]: «debiendo computar exigencia de capital por las posiciones de titulización que conserve»
- **ob2 Obligacion** «Dictamen jurídico de aislamiento y falta de control» — Las condiciones de ausencia de control directo o indirecto y de aislamiento jurídico de las exposiciones transferidas deben estar avaladas por dictamen jurídico · props: `{"tipo": "otra"}` · tramo [exacta]: «Estas condiciones deberán estar avaladas por dictamen jurídico.»
- **c1 Condicion** «Transferencia a terceros del riesgo de crédito» — Requisito i): se ha transferido a uno o más terceros el riesgo de crédito asociado a las exposiciones titulizadas · tramo [exacta]: «Se ha transferido a uno o más terceros el riesgo de crédito asociado a las exposiciones titulizadas.»
- **c2 Condicion** «Cedente sin control directo ni indirecto; exposiciones aisladas» — Requisito ii): la cedente no mantiene control directo ni indirecto sobre las exposiciones transferidas, que han sido aisladas de la cedente a efectos jurídicos, fuera de su alcance y del de sus acreedores, incluso en liquidación o quiebra · tramo [exacta]: «La entidad cedente no mantiene un control directo ni indirecto (como ser a través de una sociedad controlada) sobre las exposiciones transferidas.»
- **c3 Condicion** «Títulos no son obligaciones de la cedente» — Requisito iii): los títulos valores emitidos no son obligaciones de la cedente; los inversores sólo tienen derechos frente al conjunto subyacente de exposiciones · tramo [exacta]: «Los títulos valores emitidos no son obligaciones de la cedente.»
- **c4 Condicion** «Cesión a SPE y títulos libremente gravables o enajenables» — Requisito iv): la cesión se efectuó a un Ente de Propósito Especial (SPE) y los inversores pueden gravar o enajenar sus títulos valores sin restricción · tramo [exacta]: «La cesión se ha efectuado a un "Ente de Propósito Especial" (SPE) y los inversores pueden gravar o enajenar sus títulos valores sin restricción.»
- **c5 Condicion** «Opciones de exclusión conforme punto 3.1.4» — Requisito v): las opciones de exclusión satisfacen las condiciones estipuladas en el punto 3.1.4 · tramo [exacta]: «Las opciones de exclusión satisfacen las condiciones estipuladas en el punto 3.1.4.»
- **c6 Condicion** «Titulización sin cláusulas de mejora, primera pérdida o mayor rendimiento» — Requisito vi): la titulización no contiene cláusulas que (a) obliguen a la originante a alterar las exposiciones subyacentes para mejorar su calidad crediticia, salvo venta a precios de mercado a terceros no vinculados; (b) obliguen a la entidad a incrementar su posición a primera pérdida o las mejoras crediticias tras el inicio de la operación; o (c) aumenten el rendimiento pagadero a partes dist… · tramo [exacta]: «La titulización no contiene cláusulas mediante las cuales:»
- **c7 Condicion** «Sin opciones de rescisión ni amortización anticipada que incumplan» — Requisito vii): no se incluyen opciones de rescisión o eventos desencadenantes de la extinción del contrato (salvo opciones de exclusión admitidas según punto 3.1.4. o extinción por cambios impositivos o regulatorios específicos), ni cláusulas de amortización anticipada que, según el punto 3.1.8.1., impliquen que la titulización no cumple los requerimientos operacionales · tramo [exacta]: «No se incluyen opciones de rescisión o eventos desencadenantes de la extinción del contrato»
- **ex1 Excepcion** «Excepción: opciones de exclusión admitidas o cambios impositivos/regulatorios» — Queda afuera de la exigencia de que no se incluyan opciones de rescisión o eventos de extinción del contrato (requisito vii): las opciones de exclusión admitidas del punto 3.1.4. y la extinción por cambios impositivos o regulatorios específicos · tramo [exacta]: «excepto que se trate de opciones de exclusión admitidas (punto 3.1.4.) o que la extinción se deba a cambios impositivos o regulatorios específicos»
- **def1 Definicion** «Control efectivo de la cedente sobre exposiciones transferidas» — La cedente mantiene el control efectivo de las exposiciones transferidas si a) puede recomprarlas con el objeto de realizar sus beneficios, o b) está obligada a conservar su riesgo · props: `{"termino": "control efectivo"}` · tramo [exacta]: «Se considera que la cedente mantiene el control efectivo de las exposiciones transferidas si:»
- **def2 Definicion** «Administración de subyacentes no implica control indirecto» — El mantenimiento por la cedente de la administración de las exposiciones subyacentes no implica un control indirecto sobre ellas · props: `{"termino": "control indirecto"}` · tramo [exacta]: «El mantenimiento por parte de la cedente de la administración de las exposiciones subyacentes no implicará un control indirecto sobre ellas.»
- R: c1 Condicion —condicion_de→ pot1 Potestad
- R: c2 Condicion —condicion_de→ pot1 Potestad
- R: c3 Condicion —condicion_de→ pot1 Potestad
- R: c4 Condicion —condicion_de→ pot1 Potestad
- R: c5 Condicion —condicion_de→ pot1 Potestad
- R: c6 Condicion —condicion_de→ pot1 Potestad
- R: c7 Condicion —condicion_de→ pot1 Potestad
- R: pot1 Potestad —aplica_a→ Sujeto (mención «la entidad originante»)
- R: ob1 Obligacion —aplica_a→ Sujeto (mención «la entidad originante»)
- R: ob2 Obligacion —aplica_a→ Sujeto (mención «la entidad cedente»)
- R: Sujeto (mención «la entidad originante») —ejecuta→ op1 Operacion
- Omisión `fuera_de_tipos` [exacta]: «a) se obligue a la originante a alterar las exposiciones subyacentes con el objeto de mejorar su calidad crediticia, a menos que esto se logre mediante su venta –a precios de mercado– a terceros no vinculados a ésta;» — Subcláusulas a), b) y c) del requisito vi): se registran dentro de la descripción de la Condicion c6 (supuesto único: ausencia de cláusulas). La salvedad de venta a precios de mercado a terceros no vi…
- Omisión `relacion_sin_predicado` [exacta]: «Se considera que la cedente mantiene el control efectivo de las exposiciones transferidas si:» — La definición de control efectivo precisa el requisito ii); habría usado un predicado de precisión/definición entre Definicion y Condicion, que no existe.

### H — omisiones de T4 a clasificar

- con_marca:15 → entidades: — | omisiones: —

## Código K

- **op1 Operacion** «Exclusión de exposiciones titulizadas del cálculo APR» — Exclusión, por la entidad originante, de las exposiciones objeto de una titulización tradicional al calcular los activos ponderados por riesgo · props: `{"tipo": "cálculo de activos ponderados por riesgo"}` · tramo [exacta]: «Al calcular los activos ponderados por riesgo, la entidad originante podrá excluir las exposiciones objeto de una titulización tradicional»
- **p1 Potestad** «Facultad de excluir exposiciones de titulización tradicional» — La entidad originante podrá excluir del cálculo de activos ponderados por riesgo las exposiciones objeto de una titulización tradicional sólo si se satisfacen todos los requisitos operativos i) a vii). · tramo [exacta]: «la entidad originante podrá excluir las exposiciones objeto de una titulización tradicional sólo si se satisface la totalidad de los siguientes requisitos operativos»
- **o1 Obligacion** «Exigencia por posiciones de titulización conservadas» — La entidad originante que excluya las exposiciones debe computar exigencia de capital por las posiciones de titulización que conserve. · props: `{"tipo": "calculo"}` · tramo [exacta]: «debiendo computar exigencia de capital por las posiciones de titulización que conserve»
- **c1 Condicion** «Transferencia del riesgo de crédito a terceros» — Requisito i): el riesgo de crédito de las exposiciones titulizadas se transfirió a uno o más terceros. · tramo [exacta]: «Se ha transferido a uno o más terceros el riesgo de crédito asociado a las exposiciones titulizadas.»
- **c2 Condicion** «Ausencia de control directo o indirecto de la cedente» — Requisito ii): la cedente no mantiene control directo ni indirecto sobre las exposiciones transferidas. · tramo [exacta]: «La entidad cedente no mantiene un control directo ni indirecto (como ser a través de una sociedad controlada) sobre las exposiciones transferidas.»
- **c3 Condicion** «Aislamiento jurídico de las exposiciones transferidas» — Requisito ii): exposiciones aisladas jurídicamente de la cedente y de sus acreedores, incluso en liquidación o quiebra. · tramo [exacta]: «Ellas han sido aisladas de la cedente a los efectos jurídicos de forma tal que están fuera de su alcance y del de sus acreedores, incluso en los casos de liquidación o quiebra.»
- **c4 Condicion** «Dictamen jurídico que avale las condiciones» — Requisito ii): la falta de control y el aislamiento deben estar avalados por dictamen jurídico. · tramo [exacta]: «Estas condiciones deberán estar avaladas por dictamen jurídico.»
- **d1 Definicion** «Control efectivo de la cedente» — La cedente mantiene el control efectivo de las exposiciones transferidas si a) puede recomprarlas para realizar sus beneficios, o b) está obligada a conservar su riesgo. Mantener la administración de las exposiciones subyacentes no implica control indirecto. · props: `{"termino": "control efectivo"}` · tramo [exacta]: «Se considera que la cedente mantiene el control efectivo de las exposiciones transferidas si:»
- **c5 Condicion** «Títulos no son obligaciones de la cedente» — Requisito iii): los títulos emitidos no son obligaciones de la cedente; los inversores sólo tienen derechos frente al conjunto subyacente de exposiciones. · tramo [exacta]: «Los títulos valores emitidos no son obligaciones de la cedente.»
- **c6 Condicion** «Cesión a un Ente de Propósito Especial» — Requisito iv): la cesión se efectuó a un SPE. · tramo [exacta]: «La cesión se ha efectuado a un "Ente de Propósito Especial" (SPE)»
- **c7 Condicion** «Libre gravamen o enajenación de títulos por inversores» — Requisito iv): los inversores pueden gravar o enajenar sus títulos sin restricción. · tramo [no]: «los inversores pueden gravar o enajenar sus títulos valores sin restricción»
- **c8 Condicion** «Opciones de exclusión conformes al punto 3.1.4» — Requisito v): las opciones de exclusión cumplen el punto 3.1.4. · tramo [exacta]: «Las opciones de exclusión satisfacen las condiciones estipuladas en el punto 3.1.4.»
- **c9 Condicion** «Sin cláusula de alterar exposiciones para mejorar calidad» — Requisito vi.a): la titulización no contiene cláusulas que obliguen a la originante a alterar las exposiciones subyacentes para mejorar su calidad crediticia, salvo mediante venta a precios de mercado a terceros no vinculados. · tramo [no]: «se obligue a la originante a alterar las exposiciones subyacentes con el objeto de mejorar su calidad crediticia, a menos que esto se logre mediante su venta –a precios de mercado– a terceros no vinculados a ésta»
- **c10 Condicion** «Sin cláusula de incrementar primera pérdida o mejoras» — Requisito vi.b): no hay cláusulas por las que la entidad deba incrementar su posición a primera pérdida o aumentar las mejoras crediticias provistas después del inicio de la operación. · tramo [exacta]: «la entidad financiera deba incrementar su posición a primera pérdida»
- **c11 Condicion** «Sin cláusula de aumentar rendimiento ante deterioro» — Requisito vi.c): no hay cláusulas que aumenten el rendimiento pagadero a partes distintas de la originante en respuesta a un deterioro de la calidad crediticia de las exposiciones subyacentes. · tramo [exacta]: «se aumente el rendimiento pagadero a las partes distintas de la originante»
- **c12 Condicion** «Sin opciones de rescisión ni eventos de extinción» — Requisito vii): no se incluyen opciones de rescisión ni eventos de extinción del contrato, excepto opciones de exclusión admitidas (punto 3.1.4.) o extinción por cambios impositivos o regulatorios específicos. · tramo [no]: «No se incluyen opciones de rescisión o eventos desencadenantes de la extinción del contrato»
- **c13 Condicion** «Sin amortización anticipada incumplidora (punto 3.1.8.1)» — Requisito vii): no se incluyen cláusulas de amortización anticipada que, según el punto 3.1.8.1., impliquen incumplir los requerimientos operacionales. · tramo [exacta]: «ni se incluyen cláusulas de amortización anticipada que –de acuerdo con lo previsto en el punto 3.1.8.1.– impliquen que la titulización no cumple con los requerimientos operacionales del presente punto»
- R: p1 Potestad —aplica_a→ Sujeto_entidad_originante_de_transferencia (mención «la entidad originante»)
- R: o1 Obligacion —aplica_a→ Sujeto_entidad_originante_de_transferencia (mención «la entidad originante»)
- R: op1 Operacion —requiere→ o1 Obligacion
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: c2 Condicion —condicion_de→ p1 Potestad
- R: c3 Condicion —condicion_de→ p1 Potestad
- R: c4 Condicion —condicion_de→ p1 Potestad
- R: c5 Condicion —condicion_de→ p1 Potestad
- R: c6 Condicion —condicion_de→ p1 Potestad
- R: c7 Condicion —condicion_de→ p1 Potestad
- R: c8 Condicion —condicion_de→ p1 Potestad
- R: c9 Condicion —condicion_de→ p1 Potestad
- R: c10 Condicion —condicion_de→ p1 Potestad
- R: c11 Condicion —condicion_de→ p1 Potestad
- R: c12 Condicion —condicion_de→ p1 Potestad
- R: c13 Condicion —condicion_de→ p1 Potestad
- Omisión `relacion_sin_predicado` [exacta]: «podrá excluir las exposiciones objeto de una titulización tradicional» — Vínculo Potestad→Operacion (habilita); no hay predicado

### K — omisiones de T4 a clasificar

- con_marca:15 → entidades: — | omisiones: —

## Código W

- **op1 Operacion** «Exclusión de exposiciones titulizadas de APR» — Exclusión, por la entidad originante, de las exposiciones objeto de una titulización tradicional al calcular los activos ponderados por riesgo · props: `{"tipo": "calculo"}` · tramo [exacta]: «Al calcular los activos ponderados por riesgo, la entidad originante podrá excluir las exposiciones objeto de una titulización tradicional»
- **p1 Potestad** «Facultad de excluir exposiciones de titulización tradicional» — Al calcular los APR, la entidad originante puede excluir las exposiciones objeto de una titulización tradicional solo si se cumplen todos los requisitos operativos i) a vii) · tramo [exacta]: «la entidad originante podrá excluir las exposiciones objeto de una titulización tradicional sólo si se satisface la totalidad de los siguientes requisitos operativos»
- **o1 Obligacion** «Exigencia de capital por posiciones conservadas» — La entidad originante que excluya las exposiciones debe computar exigencia de capital por las posiciones de titulización que conserve · props: `{"tipo": "calculo"}` · tramo [exacta]: «debiendo computar exigencia de capital por las posiciones de titulización que conserve»
- **c1 Condicion** «Transferencia del riesgo de crédito a terceros» — Requisito i): riesgo de crédito de las exposiciones titulizadas transferido a uno o más terceros · tramo [exacta]: «Se ha transferido a uno o más terceros el riesgo de crédito asociado a las exposiciones titulizadas.»
- **c2 Condicion** «Ausencia de control directo o indirecto de cedente» — Requisito ii): la cedente no mantiene control directo ni indirecto sobre las exposiciones transferidas · tramo [exacta]: «La entidad cedente no mantiene un control directo ni indirecto (como ser a través de una sociedad controlada) sobre las exposiciones transferidas.»
- **c3 Condicion** «Aislamiento jurídico de exposiciones de la cedente» — Requisito ii): exposiciones aisladas jurídicamente de la cedente y sus acreedores, incluso en liquidación o quiebra · tramo [exacta]: «Ellas han sido aisladas de la cedente a los efectos jurídicos de forma tal que están fuera de su alcance y del de sus acreedores, incluso en los casos de liquidación o quiebra.»
- **o2 Obligacion** «Dictamen jurídico que avale control y aislamiento» — Las condiciones de ausencia de control y aislamiento jurídico deben estar avaladas por dictamen jurídico · props: `{"tipo": "otra"}` · tramo [exacta]: «Estas condiciones deberán estar avaladas por dictamen jurídico.»
- **d1 Definicion** «Control efectivo de la cedente» — La cedente mantiene control efectivo si: a) puede recomprar las exposiciones para realizar sus beneficios, o b) está obligada a conservar su riesgo. Mantener la administración de las exposiciones subyacentes no implica control indirecto · props: `{"termino": "control efectivo"}` · tramo [exacta]: «Se considera que la cedente mantiene el control efectivo de las exposiciones transferidas si:»
- **c4 Condicion** «Títulos no son obligaciones de la cedente» — Requisito iii): títulos emitidos no son obligaciones de la cedente; inversores solo con derechos frente al conjunto subyacente · tramo [exacta]: «Los títulos valores emitidos no son obligaciones de la cedente.»
- **c5 Condicion** «Cesión a Ente de Propósito Especial» — Requisito iv): cesión efectuada a un SPE · tramo [exacta]: «La cesión se ha efectuado a un "Ente de Propósito Especial" (SPE)»
- **c6 Condicion** «Libre gravamen o enajenación por inversores» — Requisito iv): inversores pueden gravar o enajenar sus títulos sin restricción · tramo [exacta]: «los inversores pueden gravar o enajenar sus títulos valores sin restricción»
- **c7 Condicion** «Opciones de exclusión según punto 3.1.4» — Requisito v): opciones de exclusión cumplen condiciones del punto 3.1.4 · tramo [exacta]: «Las opciones de exclusión satisfacen las condiciones estipuladas en el punto 3.1.4.»
- **c8 Condicion** «Sin cláusula de alterar exposiciones subyacentes» — Requisito vi.a): sin cláusulas que obliguen a la originante a alterar las exposiciones para mejorar su calidad, salvo venta a precios de mercado a terceros no vinculados · tramo [exacta]: «se obligue a la originante a alterar las exposiciones subyacentes con el objeto de mejorar su calidad crediticia, a menos que esto se logre mediante su venta –a precios de mercado– a terceros no vinculados a ésta»
- **c9 Condicion** «Sin cláusula de incrementar primera pérdida» — Requisito vi.b): sin cláusulas que obliguen a incrementar la posición a primera pérdida o las mejoras crediticias tras el inicio de la operación · tramo [exacta]: «la entidad financiera deba incrementar su posición a primera pérdida»
- **c10 Condicion** «Sin aumento de rendimiento por deterioro crediticio» — Requisito vi.c): sin cláusulas que aumenten el rendimiento a partes distintas de la originante ante deterioro de la calidad crediticia de las exposiciones · tramo [exacta]: «se aumente el rendimiento pagadero a las partes distintas de la originante»
- **c11 Condicion** «Sin opciones de rescisión ni eventos de extinción» — Requisito vii): sin opciones de rescisión ni eventos de extinción, excepto opciones de exclusión admitidas (3.1.4) o extinción por cambios impositivos o regulatorios específicos · tramo [exacta]: «No se incluyen opciones de rescisión o eventos desencadenantes de la extinción del contrato»
- **c12 Condicion** «Sin amortización anticipada incumplidora (3.1.8.1)» — Requisito vii): sin cláusulas de amortización anticipada que, según 3.1.8.1, impliquen incumplimiento de los requisitos operacionales · tramo [exacta]: «ni se incluyen cláusulas de amortización anticipada que –de acuerdo con lo previsto en el punto 3.1.8.1.– impliquen que la titulización no cumple con los requerimientos operacionales del presente punto»
- R: p1 Potestad —aplica_a→ Sujeto (mención «la entidad originante»)
- R: o1 Obligacion —aplica_a→ Sujeto (mención «la entidad originante»)
- R: Sujeto (mención «la entidad originante») —ejecuta→ op1 Operacion
- R: op1 Operacion —requiere→ o1 Obligacion
- R: c1 Condicion —condicion_de→ p1 Potestad
- R: c2 Condicion —condicion_de→ p1 Potestad
- R: c3 Condicion —condicion_de→ p1 Potestad
- R: c4 Condicion —condicion_de→ p1 Potestad
- R: c5 Condicion —condicion_de→ p1 Potestad
- R: c6 Condicion —condicion_de→ p1 Potestad
- R: c7 Condicion —condicion_de→ p1 Potestad
- R: c8 Condicion —condicion_de→ p1 Potestad
- R: c9 Condicion —condicion_de→ p1 Potestad
- R: c10 Condicion —condicion_de→ p1 Potestad
- R: c11 Condicion —condicion_de→ p1 Potestad
- R: c12 Condicion —condicion_de→ p1 Potestad

### W — omisiones de T4 a clasificar

- con_marca:15 → entidades: — | omisiones: —

