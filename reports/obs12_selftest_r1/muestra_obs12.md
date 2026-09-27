# Muestra de la observación (12) — aristas de extracción contra el texto

- Fecha del sorteo: 2026-09-27
- Grafo: `data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json`
- sha256 del grafo: `0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a`
- Semilla: 20260927
- n (universo de aristas de extracción, A4.1): 12010 (total 17772 − referencia 5680 − esqueleto 82 + solapamiento 0)
- k: 30
- Triplas duplicadas en el universo: 0
- E0: `data/experiment/reextraccion_v2/e0_chunking/salida_enm01`
  - chunks_cap.json: `1931138dac0a107a69a7ff6312400f00465b991d52135457735beeb3e442c825`
  - chunks_cla.json: `98808886a406d8321c678836a55f92eea983d594d95358dd21ceb537487ac0b1`
  - chunks_ext.json: `cbcd1a86f55ea49110610587873881c68c13a9d7975d3fd5e465f26302be2d12`
  - chunks_pro.json: `d8717d1c7423bb5f4d80cc830ff97635ce4d9839f8490b73860ea272568620e2`
  - chunks_ric.json: `fafebb82e07b34191b60022c1c179ea7d2213fd1f5d5f3a408b518c836c94c0d`
- Textos del punto ancla no encontrados: 0
- Relaciones en la muestra: establecida_en 11, aplica_a 8, regula 6, limita 3, condiciona 1, exceptua 1
- Índices: [115, 200, 1159, 1168, 1270, 1750, 1973, 2184, 2334, 3031, 3215, 3913, 4162, 4792, 5095, 5131, 5754, 5920, 6626, 7628, 7971, 8111, 8265, 8531, 8821, 10078, 10277, 10433, 10884, 11167]

Regla: universo de A4.1; orden por la tripla (source, relation, target); `sorted(random.Random(semilla).sample(range(n), k))` (enmienda del 27/09/2026, §2.1 y §2.2).

---

## 1 · índice 115 · `establecida_en`

- **Origen:** `Excepcion_destinaciones_suspensivas_de_exportaciones_temporarias_articulos_349_a_373_del_c_3d312b` · tipo `Excepcion` · label «Excepción seguimiento — destinaciones suspensivas»
  - propiedades: `{"descripcion": "Destinaciones suspensivas de exportaciones temporarias (artículos 349 a 373 del Código Aduanero) están exceptuadas del seguimiento"}`
- **Relación:** `establecida_en`
- **Destino:** `TextoOrdenado_to_exterior_cambios_actual_pdf` · tipo `TextoOrdenado` · label «Texto Ordenado de Exterior y Cambios»
  - propiedades: `{"materia": "exterior", "archivo": "TO_exterior_cambios_actual.pdf", "version": "actual", "descripcion": "Comprende a la administración central de provincias, de la Ciudad Autónoma de Buenos Aires, y de las municipalidades del país.", "cola_humana": "true", "cola_chunks": ["ext::10.10.2.3", "ext::10.10.2.5", "ext::10.2.4.9", "ext::10.3.2.5", "ext::10.3.3", "ext::10.3.5::intro", "ext::10.4.3::intro", "ext::10.5.5.2", "ext::10.9.4", "ext::13.2.7::intro", "ext::13.3.3", "ext::13.3.9", "ext::13.4.8", "ext::14.2.1.10", "ext::14.2.1.6", "ext::14.2.1.7", "ext::14.2.1::intro", "ext::14.5.3", "ext::3.11.2.1", "ext::3.11.3::cierre", "ext::3.14.2", "ext::3.14.5.5", "ext::3.16.2.1", "ext::3.17.3::intro", "ext::3.17.5", "ext::3.18.1::cierre", "ext::3.3.3.4", "ext::3.4.4::intro", "ext::3.5.1.12", "ext::3.5.1.9", "ext::3.5.3.5", "ext::3.5.6.10", "ext::3.5::intro", "ext::3.9::intro", "ext::4.2.8", "ext::4.4.2", "ext::4.7.2", "ext::4.8.1.1", "ext::4.8.1.2", "ext::4.8.1.3", "ext::4.8.1.5", "ext::4.8.2", "ext::7.10.6", "ext::7.11.2::cierre", "ext::7.11.3::intro", "ext::7.11.5", "ext::7.3.6", "ext::7.3::intro", "ext::7.5.7.1", "ext::7.6.1.1", "ext::7.8.5::intro", "ext::7.9.1.4", "ext::7.9.1.6", "ext::7.9.3::intersticial", "ext::8.2::intro", "ext::9.3.2", "ext::9.3.3.1", "ext::9.3.7"], "estado_e3": "cola_humana; cola_humana_veredicto_inutilizable", "materia_variantes": ["exterior", "operaciones en el mercado de cambios", "Operaciones de cambio", "exterior_cambios", "Régimen de operaciones en el exterior y operaciones de cambio", "Exterior y cambios", "Operaciones de cambio en el exterior", "Operaciones en mercado de cambios", "Operaciones cambiarias en el exterior", "Operatoria de cambios e ingresos por mercado de cambios", "Operaciones de cambios y exterior", "Disposiciones específicas para los ingresos por el mercado de cambios", "Disposiciones específicas para operaciones en el mercado de cambios — cobros de exportaciones de servicios", "Disposiciones para ingresos por mercado de cambios - Cobros de exportaciones de servicios", "Operaciones en el mercado de cambios - Exterior", "Exterior y Cambios", "Operaciones en el mercado de cambios — títulos de deuda y endeudamientos", "Operaciones en el mercado de cambios", "Disposiciones específicas para ingresos por mercado de cambios", "Operaciones de cambios — Exterior", "Exterior Cambios", "Operaciones en cambios - Ingresos por mercado de cambios", "Exterior", "Operaciones de cambios en el exterior", "Operaciones en cambios para residentes en el exterior", "Operaciones en mercado de cambios — Exterior", "Operaciones en el mercado de cambios — obligaciones de liquidación", "Operaciones de cambio - ingresos por mercado de cambios", "Operaciones de cambios en el mercado de cambios", "Operaciones de cambios", "Disposiciones para egresos por mercado de cambios", "Operaciones en el mercado de cambios - Egresos", "Disposiciones específicas para egresos por mercado de cambios", "Operaciones del mercado de cambios", "Operaciones en el mercado de cambios — Pagos de intereses de deudas por importaciones", "Disposiciones para operaciones de cambio - egresos", "Operaciones en cambios — Egresos", "Operaciones del mercado de cambios — Egresos", "Operaciones en cambios", "Operaciones de cambios — egresos", "Operaciones de cambios — Egresos", "Operaciones en el mercado de cambios — egresos", "Operaciones de cambios – disposiciones específicas para egresos", "Operaciones de cambio — egresos", "Operaciones de cambio — pagos títulos de deuda y endeudamientos", "Operaciones en el mercado de cambios — Pagos de títulos de deuda", "Operaciones en mercado de cambios — pagos de títulos y endeudamientos", "Operaciones por el mercado de cambios — pagos de títulos de deuda", "Pagos de títulos de deuda y endeudamientos con el exterior", "Operaciones de cambios - Egresos", "Operaciones en el mercado de cambios — pagos de títulos de deuda y endeudamientos", "Operaciones de cambio - Exterior", "Operaciones en el mercado de cambios — pagos de deuda y endeudamientos con el exterior", "Operaciones de cambio — Pagos de títulos de deuda y endeudamientos con el exterior", "Operaciones en el mercado de cambios — pagos de deuda externa", "Operaciones de cambios - Exterior", "Egresos por el mercado de cambios", "Egresos por mercado de cambios", "Operaciones de cambio en el mercado exterior", "Disposiciones específicas para operaciones de cambios", "Operaciones de cambio - Pagos de títulos de deuda en moneda extranjera", "Disposiciones para operaciones en el mercado de cambios", "Operaciones en el mercado de cambios — títulos de deuda", "Disposiciones para operaciones en mercado de cambios", "Operaciones en el mercado de cambios — Egresos", "Disposiciones para operaciones de cambio — exterior", "Operaciones de cambios - Egresos por el mercado de cambios", "Exterior y operaciones de cambio", "Disposiciones para operaciones de cambios en el exterior", "Disposiciones para operaciones de cambios y egreso de divisas", "Operaciones cambiarias", "Exterior - Cambios", "Disposiciones para operaciones de cambios - residentes con endeudamientos o fideicomisos", "operaciones de cambios — egresos", "Operaciones en el mercado de cambios para residentes", "Operaciones en mercado de cambios — egresos", "Operaciones en el mercado de cambios - egresos por residentes", "Disposiciones para operaciones de cambios — egresos", "Operaciones de cambio en el mercado de divisas", "Disposiciones para egresos por el mercado de cambios", "Operaciones de cambios y derivados", "Operaciones en cambios - Exterior", "Operaciones de cambio al exterior", "Operaciones de cambios - Repatriaciones y compras de moneda extranjera", "Disposiciones específicas para los egresos por el mercado de cambios", "Operaciones en cambios — Repatriaciones de inversiones directas", "Operaciones cambiarias y repatriaciones de no residentes", "Operaciones de cambios — Repatriaciones", "Operaciones del mercado de cambios - exterior", "Operaciones de cambio y transferencias de divisas", "Operaciones de cambios — Egresos por el mercado de cambios", "operaciones de cambios y egresos por el mercado de cambios", "Operaciones en el mercado de cambios — Exterior", "Operaciones en el mercado de cambios — exterior", "Operaciones de cambio - Cancelación de garantías financieras", "Operaciones de cambio — Exterior", "Operaciones en el mercado de cambios — requisitos complementarios", "Definiciones", "Operaciones de egresos por mercado de cambios", "Disposiciones para operaciones de cambios", "Operaciones de cambio - Egresos", "Mercado de cambios", "Operaciones de cambios — exterior", "Acceso al mercado de cambios", "Operaciones de cambios del mercado exterior", "Operaciones de cambio - repatriaciones de inversiones directas", "Disposiciones específicas para egresos por el mercado de cambios", "Operaciones de cambios y acceso a divisas", "Acceso a divisas para producción incremental", "Operaciones en el mercado de cambios — acceso a divisas", "Operaciones en el mercado de cambios — régimen de acceso a divisas para producción incremental de petróleo y/o gas", "Operaciones de cambios en el mercado exterior", "Operaciones de cambios — egreso de moneda extranjera", "Operaciones en el mercado de cambios - Acceso con Certificación de aumento de exportaciones", "Operaciones cambiaras, exportaciones", "Operaciones en el exterior y cambios", "Operaciones con moneda extranjera — retiros de efectivo desde el exterior", "Operaciones cambiarias y de exterior", "Operaciones con débito en cuenta local y tarjetas — Pagos al exterior", "Operaciones en el exterior y acceso al mercado de cambios", "Operaciones con cambios", "Operaciones con cambios — exterior", "Operaciones cambiarias y comerciales", "Operaciones en cambios — exterior", "Operaciones de comercio exterior y cambios", "Operaciones de cambio y comercio exterior", "Operaciones en cambios - exterior", "Operaciones con títulos valores", "Operaciones cambios exterior", "Operaciones con títulos valores — Exterior", "Operaciones en cambios - Entidades autorizadas", "Operaciones en cambios — Exterior", "Operaciones de cambio y exterior", "Operaciones de cambio de no residentes", "Operaciones cambiarias con no residentes", "Operaciones en cambios, suscripción de BOPREAL", "Operaciones de cambios — entidades autorizadas", "Operaciones en cambios y exterior", "Régimen de Operaciones de Cambios del Exterior", "exterior y cambios", "Operaciones en cambios en el exterior", "Operaciones de cambio, suscripción de bonos BOPREAL", "operaciones de cambio y exterior", "Operaciones en cambios, exterior", "Operaciones de cambio en exterior", "Operatoria de cambios en el exterior", "Operaciones de cambio — pautas operativas", "Operaciones de cambios — entidades financieras y cambiarias", "Operaciones de cambio y transferencias de fondos con el exterior", "Operaciones de cambio y transferencias de fondos desde y hacia el exterior", "Operaciones con cambios en el exterior", "Operaciones cambiarias — Exterior", "Operaciones de cambios y transferencias de divisas", "Operaciones de cambio y posiciones en moneda extranjera", "Pautas operativas para entidades autorizadas a operar en cambios", "Operaciones de cambios y tenencias en moneda extranjera", "Operaciones cambiarias propias", "Operaciones de cambio exterior", "Operaciones de cambio y remesas al exterior", "Operaciones en el exterior", "Operaciones de cambios y arbitrajes en el exterior", "Operaciones en cambios de entidades autorizadas", "Operaciones de cambio — importación y exportación de moneda nacional", "operaciones cambiarias", "Operaciones de cambio — exterior", "Exterior — Cambios", "Definiciones — Servicios", "Definición de Gobiernos locales", "Cobros de exportaciones de bienes", "Cobros de exportaciones", "Cobros de exportaciones de bienes — Exterior", "Cambios — Operaciones de comercio exterior", "Operaciones cambiarias en cuenta corriente de exportadores", "Operaciones de cambios - Cobros de exportaciones de bienes", "Operaciones con el Exterior - Cambios", "Operaciones financieras enunciadas", "Operaciones cambiarias del exterior", "Cambios - Exterior", "Operaciones de cambios, exterior", "Operaciones de cambios, cobros y pagos en el exterior", "Cobros de exportaciones — Ampliaciones de plazo", "Cobros de exportaciones de bienes — ampliaciones de plazo para liquidación de divisas", "Operaciones de cambio, comercio exterior", "Operaciones en cambios del exterior", "Cobros de exportaciones de bienes — Deudor moroso", "Cobros de exportaciones y exterior", "Operaciones de comercio exterior", "Operaciones cambiarias al exterior", "Operaciones de cambios y comercio exterior", "Operaciones en cambios y comercio exterior", "Cambios - Operaciones en el exterior", "Cobros de exportaciones de bienes - Régimen de fomento para las exportaciones de la economía del conocimiento", "Operaciones financieras habilitadas para aplicar cobros de exportaciones", "Operaciones cambiarias — exterior", "Operaciones cambistas de entidades autorizadas a operar en el exterior", "Operaciones del exterior", "Operaciones de cambios - Cobros de exportaciones", "Operaciones de cambio — Cobros de exportaciones", "Operaciones financieras habilitadas para cobros de exportaciones de bienes", "Cobros de exportaciones de bienes — operaciones financieras habilitadas", "Cobros de exportaciones de bienes y operaciones financieras habilitadas", "Operaciones cambarias y de comercio exterior", "Operaciones de exterior y cambios", "Operaciones en moneda extranjera y cambios", "Cobros de exportaciones de bienes en divisas", "Operaciones en cambios - Cobros de exportaciones", "Operaciones en cambios — Cobros de exportaciones de bienes", "Operaciones cambiarias, cobros de exportaciones", "Operaciones cambiarias en exterior", "Cobros de exportaciones de bienes — Decreto 234/21", "Operaciones de cambio, importaciones y exportaciones", "Cobros de exportaciones de bienes y financiaciones asociadas a importaciones", "Operaciones cambias en el exterior", "Operaciones de cambios, importación, exportación", "Operaciones cambiarias - Exterior", "Operaciones en cambios, financiaciones de exportación/importación", "Operaciones de cambios — Cobros de exportaciones de bienes", "Operaciones de cambios, cobros de exportaciones", "Cobros de exportaciones de bienes — Financiaciones asociadas a importaciones", "Seguimiento de negociaciones de divisas por exportaciones de bienes", "Seguimiento de negociaciones de divisas por exportaciones", "Negociación de divisas por exportaciones", "Operaciones de cambio y seguimiento de exportaciones de divisas", "Seguimiento de negociaciones de divisas por exportaciones de bienes — Exterior", "Operaciones de cambio — Seguimiento de divisas por exportaciones", "Operaciones de cambio y seguimiento de divisas por exportaciones", "Seguimiento de negociaciones de divisas", "Operaciones cambistas - seguimiento de divisas por exportaciones", "Seguimiento de negociaciones de divisas por exportaciones de bienes — Operaciones aduaneras exceptuadas", "Seguimiento de anticipos y financiaciones de exportación", "Seguimiento de anticipos y otras financiaciones de exportación", "Operaciones de cambio y seguimiento de financiaciones de exportación", "Seguimiento de anticipos y otras financiaciones de exportación de bienes", "Operaciones de cambios - Seguimiento de financiaciones de exportación", "Operaciones de cambio y financiaciones de exportación", "Seguimiento de anticipos y financiaciones de exportación de bienes", "Operaciones de cambio y financiación de exportaciones", "Seguimiento de anticipos y otras financiaciones de exportación de bienes; Certificaciones de aplicación de cobros de exportaciones", "Exterior y operaciones de cambios", "Exterior, Cambios, Operaciones de exportación", "Seguimiento de anticipos y financiaciones de exportación; certificaciones de aplicación", "Seguimiento de anticipos y financiaciones de exportación; certificaciones de aplicación de cobros", "Seguimiento de anticipos y otras financiaciones de exportación de bienes. Certificaciones de aplicación de cobros de exportaciones.", "Pagos de importaciones y operaciones de cambios en el exterior", "Pagos de importaciones y operaciones de cambio en el exterior", "Pagos de importaciones", "Pagos de importaciones y compras en el exterior", "Pagos de importaciones y compras en exterior", "Pagos de importaciones y otras compras de bienes en el exterior", "Pagos de importaciones y compras de bienes en exterior", "Pagos de importaciones y compras de bienes en el exterior", "Pagos de importaciones y operaciones de cambios", "Operaciones de cambio - Pagos de importaciones", "Operaciones en cambios, pagos de importaciones", "Exterior y Operaciones de Cambio", "Operaciones de cambio y pagos internacionales", "Pagos de importaciones y operaciones de cambio", "Operaciones en cambios - Pagos de importaciones", "Pagos de importaciones y operaciones cambiarias", "Operaciones de cambio — Pagos de importaciones", "Operaciones de cambios y pagos de importaciones", "Pagos de importaciones y operaciones en el exterior", "Pagos de importaciones y operaciones en cambios", "Pagos de importaciones en el exterior", "Pagos de importaciones y operaciones en cambios — exterior", "Operaciones en cambios y pagos de importaciones", "Operaciones en cambios con el exterior", "Pagos al exterior y operaciones de cambio", "Cambios, Pagos de importaciones", "Operaciones de cambio — Pagos de importaciones y compras de bienes en el exterior", "Pagos de importaciones y cambios", "Operaciones de cambio; pagos de importaciones", "Pagos de importaciones y operaciones cambiarias en el exterior", "Operaciones de cambios. Pagos de importaciones.", "Pagos de importaciones — Operaciones de cambio", "Operaciones en cambios — pagos de importaciones", "Operaciones de cambios y pagos al exterior", "Operaciones en cambios — Compras de bienes en exterior", "Operaciones de cambio, pagos de importaciones", "Exterior y operaciones cambiarias", "Operaciones con el exterior", "Operaciones de cambios — Pagos de importaciones", "Sistema de seguimiento de pagos de importaciones", "Sistema de seguimiento de pagos de importaciones (SEPAIMPO)", "Seguimiento de pagos de importaciones", "Régimen de operaciones en cambios", "Sistema de seguimiento de pagos de importaciones y certificación para acceso al mercado de cambios", "Sistema de seguimiento de pagos de importaciones y operaciones en comercio exterior", "Operaciones de cambios en comercio exterior", "Sistema de seguimiento de pagos de importaciones (SEPAIMPO) — Exterior y Cambios", "Sistema de seguimiento de pagos de importaciones - Certificación para afectación de despacho", "Sistema de seguimiento de pagos de importaciones (SEPAIMPO) — Certificación para afectación del despacho", "Sistema de seguimiento de pagos de importaciones (SEPAIMPO) - Certificación para afectación del despacho a pagos con registro de ingreso aduanero pendiente", "Sistema de seguimiento de pagos de importaciones (SEPAIMPO). Reporte de circunstancias que modifiquen obligaciones con el exterior.", "Sistema de seguimiento de pagos de importaciones y operaciones en mercado de cambios", "Sistema de seguimiento de pagos de importaciones (SEPAIMPO) — Reporte de cambio de entidad a cargo del seguimiento", "Operaciones de cambios. SEPAIMPO", "Pagos de servicios prestados por no residentes", "Operaciones de cambio con el exterior", "Pagos de servicios de no residentes", "Operaciones en cambios — Servicios prestados por no residentes", "Operaciones de cambios, sector exterior", "Pagos de servicios prestados por no residentes y acceso a divisas", "Operaciones de cambios — no residentes", "Operaciones de cambios - exterior", "Régimen de operaciones de cambios", "cambios", "Régimen de Incentivo para Grandes Inversiones - Acceso al mercado de cambios", "Régimen de operaciones de egreso en el mercado de cambios para VPU RIGI", "Régimen de Incentivo para Grandes Inversiones — acceso al mercado de cambios", "Operaciones de cambio - Régimen RIGI", "Cambios — operaciones de egreso para VPU adheridos al RIGI", "Régimen de operaciones de cambios para VPU adheridos al RIGI", "Régimen cambiario", "Régimen de operaciones de egreso en el mercado de cambios — RIGI", "Operaciones de cambios y egresos — RIGI", "Régimen de operaciones en cambios y exterior", "Régimen de Incentivo para Grandes Inversiones (RIGI) - Cambios", "Operaciones de cambio — RIGI", "Régimen de Incentivo para Grandes Inversiones (RIGI) — Disposiciones cambiarias", "Régimen de operaciones de cambio", "Mercado de cambios y operaciones en el exterior", "Disposiciones legales sobre estructura del mercado de cambios"], "version_variantes": ["actual", "", "ext", "vigente"]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "ext", "archivo": "TO_exterior_cambios_actual.pdf", "punto": "8.5.17.21", "rol_documental": "punto_propio", "chunk_id": "ext::8.5.17.21", "paginas": [119], "ancestros": ["S8", "8.5", "8.5.17"]}`
- **Provenances (1):**
  - `{"to": "ext", "archivo": "TO_exterior_cambios_actual.pdf", "punto": "8.5.17.21", "rol_documental": "punto_propio", "chunk_id": "ext::8.5.17.21", "paginas": [119], "ancestros": ["S8", "8.5", "8.5.17"]}`
- **Texto del punto ancla** (`ext::8.5.17.21`):

> 8.5.17.21. Destinaciones suspensivas de exportaciones temporarias (artículos 349 a
> 373 del Código Aduanero).

- **Herencia (5):**
  - [encabezado] S8 (páginas [108]):

    > Sección 8. Seguimiento de las negociaciones de divisas por exportaciones de bienes

  - [encabezado] 8.5 (páginas [112]):

    > 8.5. Otras imputaciones admitidas en el cumplimiento del seguimiento.

  - [intro] 8.5 (páginas [112]):

    > La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso
    > de embarque cuando cuente con los elementos que le permitan considerar que la operación
    > se encuentra en alguna de las situaciones detalladas a continuación y se verifiquen las
    > condiciones previstas en cada caso.
    > La documentación utilizada para certificar el concepto y monto de las divisas imputado en
    > cada caso deberá quedar archivada en la entidad a disposición del BCRA.

  - [encabezado] 8.5.17 (páginas [117]):

    > 8.5.17. Operaciones aduaneras exceptuadas del seguimiento.

  - [intro] 8.5.17 (páginas [117]):

    > Por el valor que corresponda a ventajas aduaneras u otras situaciones previstas en el
    > siguiente listado de operaciones:

---

## 2 · índice 200 · `exceptua`

- **Origen:** `Excepcion_en_caso_de_impago_o_insolvencia_del_miembro_compensador_no_habra_impedimentos_le_1da0f4` · tipo `Excepcion` · label «Salvedad orden judicial — transferencia garantía cliente en insolvencia miembro compensador»
  - propiedades: `{"descripcion": "En caso de impago o insolvencia del miembro compensador, no habrá impedimentos legales –salvo la necesidad de obtener una orden judicial, a la cual el cliente tiene derecho– para transferir la garantía que pertenece a los clientes de ese miembro compensador a la CCP, a otro u otros miembros compensadores, al cliente o a quien éste designe."}`
- **Relación:** `exceptua`
- **Destino:** `Restriccion_las_leyes_regulaciones_y_acuerdos_contractuales_o_administrativos_aplicables_hac_8d8910` · tipo `Restriccion` · label «Portabilidad transacciones — operaciones cerradas indirectamente vía CCP u otra»
  - propiedades: `{"descripcion": "Las leyes, regulaciones y acuerdos contractuales o administrativos aplicables hacen que sea altamente probable la portabilidad de las transacciones. Esto es que las transacciones compensadoras realizadas a través del miembro compensador en situación de impago o insolvencia serán concluidas indirectamente a través de la CCP o por la CCP.", "tipo": "limite_cualitativo"}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "cap", "archivo": "TO_capitales_minimos_actual.pdf", "punto": "4.3.3.1", "rol_documental": "punto_propio", "chunk_id": "cap::4.3.3.1", "paginas": [88, 89, 90, 91, 92], "ancestros": ["S4", "4.3", "4.3.3"]}`
- **Provenances (1):**
  - `{"to": "cap", "archivo": "TO_capitales_minimos_actual.pdf", "punto": "4.3.3.1", "rol_documental": "punto_propio", "chunk_id": "cap::4.3.3.1", "paginas": [88, 89, 90, 91, 92], "ancestros": ["S4", "4.3", "4.3.3"]}`
- **Texto del punto ancla** (`cap::4.3.3.1`):

> 4.3.3.1. Exposiciones por operaciones de negociación.
> i) Exposiciones de los miembros compensadores con las CCP.
> a) La entidad financiera que actúe en carácter de miembro compensa-
> dor de una CCP por operaciones propias deberá aplicar un pondera-
> dor de riesgo del 2 % a sus exposiciones con la CCP originadas en
> operaciones de derivados –OTC o negociados en mercados de valo-
> res–, de financiación con títulos valores (SFT) y de liquidación diferi-
> da. Cuando la entidad financiera preste servicios de compensación a
> clientes, aplicará el ponderador de riesgo del 2 % a la exposición con
> la CCP que se origina si, en caso de incumplimiento de la CCP, la
> entidad financiera se viera obligada –como miembro compensador a
> reembolsar al cliente toda pérdida debido al cambio de valor de sus
> transacciones. El ponderador de riesgo aplicado a los activos en ga-
> rantía aportados por la entidad financiera a una CCP deberá determi-
> narse de acuerdo con lo establecido en los párrafos primero a tercero
> del acápite iv) del presente punto.
> b) La exposición debida a dichas operaciones se calculará conforme al
> enfoque estandarizado para el riesgo de crédito de contraparte (SA-
> CCR) establecido en el punto 4.2. para los derivados OTC o negó
> ciados en mercados de valores y operaciones de liquidación diferida,
> y a lo previsto en la Sección 5. para las SFT.
> No se aplicará el plazo mínimo de veinte días hábiles para el cálculo
> del período de riesgo de margen (MPOR) de los conjuntos de neteo
> en los que se verifiquen más de 5.000 operaciones en la medida en
> que no existan disputas pendientes y que dicho conjunto no contenga
> garantías ilíquidas u operaciones exóticas. Idéntico criterio se aplica-
> rá para la determinación del período de mantenimiento mínimo (T )
> M
> utilizado en el cálculo de los aforos de las SFT previsto en el punto
> 5.3.2.3.
> En todos los casos, se utilizará un MPOR mínimo de 10 días para el
> cálculo de las exposiciones a una CCP por operaciones de derivados
> OTC.
> Cuando la CCP reciba el margen de variación de una operación y el
> activo propiedad del miembro compensador no esté protegido contra
> la insolvencia de la CCP, el horizonte temporal de riesgo mínimo a
> aplicar a dichas exposiciones será el menor entre 1 año y el plazo re-
> sidual de la operación, con un plazo mínimo de 10 días hábiles.
> c) En las operaciones con CCP radicadas en jurisdicciones en las cua-
> les la liquidación por saldos netos en caso de incumplimiento tenga
> validez legal y con independencia de si la contraparte es insolvente o
> se ha declarado en quiebra, el costo de reposición total de todos los
> contratos relevantes para determinar la exposición por operaciones
> podrá calcularse como un costo de reposición neto, siempre que el
> conjunto de operaciones compensables aplicable a dicha liquidación
> cumpla con los requisitos que en materia de validez legal se estable-
> cen en: i. el punto 5.3.2.5. para las SFT y ii. el acápite ii) del punto
> 4.2.1.1. en el caso de las operaciones con derivados.
> En la medida en que las disposiciones antes referidas contengan la
> expresión “acuerdo marco de neteo” o la frase “un contrato de neteo
> con una contraparte u otro acuerdo”, deberá interpretarse que incluye
> a todo acuerdo de neteo con validez legal que reconozca derechos
> de compensación legalmente exigibles. Si la entidad financiera no
> pudiese demostrar que los acuerdos de neteo cumplen estos reque-
> rimientos, cada transacción individual se considerará como un con-
> junto de neteo en sí misma a los efectos de calcular la exposición por
> operaciones.
> ii) Exposiciones de los miembros compensadores con sus clientes.
> El miembro compensador considerará su exposición con un cliente
> –incluyendo la potencial exposición al riesgo CVA– como una operación
> bilateral, independientemente de que el miembro compensador garantice
> la operación o actúe como un intermediario entre el cliente y la CCP. Sin
> embargo, como el período de liquidación (close-out) para las operaciones
> compensadas de los clientes es más corto, los miembros compensado-
> res podrán calcular la exigencia por la exposición a sus
> clientes aplicando un período de riesgo de margen que sea, como mí-
> nimo, de 5 días. La EAD reducida se utilizará también para el cálculo
> del ajuste de valuación de crédito –CVA– establecido en el punto 4.2.3.
> Si un miembro compensador recibe activos en garantía por las opera-
> ciones a compensar del cliente y las transfiere a la CCP, el miembro
> compensador podrá reconocer esta garantía tanto para el tramo CCP-
> miembro compensador como para el tramo miembro compensador-
> cliente de la operación. El margen inicial aportado por los clientes al
> miembro compensador mitigará su exposición respecto de sus clientes.
> Similar tratamiento se aplicará a las estructuras multinivel de clientes
> –entre clientes de nivel superior e inferior–.
> iii) Exposiciones de los clientes.
> Si la entidad financiera es cliente de un miembro compensador y realiza
> una transacción en la que el miembro compensador actúa como inter-
> mediario financiero –es decir, el miembro compensador realiza una
> transacción con la CCP por indicación del cliente–, la exposición de la
> entidad financiera hacia el miembro compensador podrá recibir el trata-
> miento del acápite i) precedente, siempre que se cumplan las siguientes
> condiciones:
> a) La CCP identifica a las transacciones a compensar como transac-
> ciones de clientes y las garantías que las amparan son mantenidas
> por la CCP y/o el miembro compensador, según sea el caso, bajo
> acuerdos que impiden que el cliente sufra pérdidas debido a: i. la
> falta de pago o la insolvencia del miembro compensador; ii. la falta
> de pago o la insolvencia de los demás clientes del miembro com-
> pensador; y iii. la falta de pago o la insolvencia conjuntas del miem-
> bro compensador y cualquiera de sus otros clientes. Esto implica
> que, en caso de impago o insolvencia del miembro compensador,
> no habrá impedimentos legales –salvo la necesidad de obtener una
> orden judicial, a la cual el cliente tiene derecho– para transferir la
> garantía que pertenece a los clientes de ese miembro compensador
> a la CCP, a otro u otros miembros compensadores, al cliente o a
> quien éste designe.
> El cliente deberá haber realizado una revisión legal adecuada –y
> llevar a cabo esas revisiones cuando sea necesario a fin de asegu-
> rar una continua aplicabilidad– y contar con fundamentos que per-
> mitan concluir que esos acuerdos serán legales, válidos, vinculan-
> tes y exigibles bajo las leyes aplicables en la/s jurisdicción/es rele-
> vante/s.
> b) Las leyes, regulaciones y acuerdos contractuales o administrativos
> aplicables hacen que sea altamente probable la portabilidad de las
> transacciones. Esto es que las transacciones compensadoras reali-
> zadas a través del miembro compensador en situación de impago o
> insolvencia serán concluidas indirectamente a través de la CCP o por
> la CCP. En tal caso, las posiciones y garantías del cliente con la CCP
> serán transferidas a valor de mercado, a menos que el cliente peti-
> cione cerrar las posiciones a valor de mercado.
> Idénticas condiciones se deberán cumplir para que la entidad financiera
> dé ese tratamiento a su exposición con una CCP por transacciones reali-
> zadas en calidad de cliente en las que su cumplimiento es garantizado
> por un miembro compensador y para las exposiciones de los clientes de
> nivel inferior con los clientes de nivel superior en las estructuras multini-
> veles, siempre que en todos los niveles de los clientes involucrados se
> cumplan las dos condiciones de este acápite.
> Cuando el cliente no esté protegido de sufrir pérdidas en caso de falta de
> pago o insolvencia conjunta del miembro compensador y alguno de sus
> clientes, pero se cumplan todas las restantes condiciones anteriormente
> expuestas, la exposición del cliente con el miembro compensador o fren-
> te al cliente de mayor nivel, respectivamente, recibirá un ponderador de
> riesgo del 4%.
> Cuando la entidad financiera sea cliente del miembro compensador y no
> se cumplan estos requisitos, la exposición con el miembro compensador,
> incluida –de corresponder– la exposición potencial por riesgo CVA, se
> deberá tratar como una operación bilateral.
> iv) Tratamiento de las garantías.
> Todo activo que la entidad financiera constituya en garantía de estas
> operaciones recibirá el ponderador que le corresponda de acuerdo con lo
> previsto en estas normas, considerando a ese efecto qué tratamiento
> –cartera de negociación o de inversión– hubiera recibido en caso de no
> haber sido depositado en la CCP. Cuando los activos de un miembro
> compensador o cliente se coloquen en garantía a favor de una CCP o
> miembro compensador, pero de modo que no queden protegidos de su
> quiebra, la entidad financiera que constituye la garantía deberá reconocer
> además el riesgo de crédito que se deriva de la posibilidad de sufrir pér-
> didas por la calidad crediticia de la entidad que recibe los activos en ga-
> rantía. Es decir que, independientemente de la cartera a la que estén
> asignados, los activos constituidos en garantía estarán sujetos también al
> requisito de riesgo de crédito de contraparte (SA-CCR) establecido en el
> punto 4.2., incluido el incremento por los aforos descriptos en el punto
> 5.3.2.3., computados de acuerdo con lo previsto en el acápite v) del pun-
> to 4.2.1.1.
> Cuando la entidad que reciba los activos en garantía sea la CCP, se
> aplicará un ponderador del 2 % a las garantías incluidas en la definición
> de exposición por operaciones. El ponderador de riesgo correspondien-
> te a la CCP se aplicará a los activos o las garantías aportados para
> otros fines. La garantía depositada que no esté resguardada en caso de
> quiebra deberá ser considerada para el Monto Neto de Garantía Inde-
> pendiente (NICA) previsto en el acápite v) del punto 4.2.1.1.
> La garantía constituida por el miembro compensador –incluyendo efec-
> tivo, títulos valores y otros activos constituidos como garantías, así co-
> mo los excesos a los márgenes inicial o de variación– mantenida por un
> custodio y protegida de la quiebra de la CCP, no está sujeta a la exi-
> gencia de capital por la exposición al riesgo de crédito de contraparte
> –esto es, el ponderador de riesgo o la EAD es igual a cero–. A ese efec-
> to, se entiende por custodio a un fiduciario o agente que mantenga los
> activos bajo un título que no le acuerde ni al custodio ni a sus acreedo-
> res un derecho o participación sobre ellos y que garantice que no se
> podrá obstaculizar judicialmente la devolución de los activos en caso de
> quiebra o insolvencia del custodio.
> La garantía constituida por un cliente, mantenida por un custodio y pro-
> tegida de la quiebra de la CCP y del miembro compensador y sus otros
> clientes no está sujeta a exigencia de capital por riesgo de crédito de
> contraparte. Si la garantía es mantenida por la CCP y no está protegida
> de su quiebra se le deberá aplicar el ponderador de riesgo del 2 % en
> caso de que se cumplan las condiciones a) y b) del acápite iii), o del 4
> % si se da el caso del anteúltimo párrafo del acápite iii).

- **Herencia (4):**
  - [encabezado] S4 (páginas [63]):

    > Sección 4. Capital mínimo por riesgo de crédito de contraparte.

  - [encabezado] 4.3 (páginas [85]):

    > 4.3. Exigencia de capital por riesgo de crédito de contraparte en operaciones con entidades de

  - [intro] 4.3 (páginas [85, 86]):

    > contraparte central.
    > Comprende a aquellas exposiciones de las entidades financieras con entidades de contrapar-
    > te central (CCP) que se originen en derivados OTC o negociados en mercados de valores y
    > en operaciones de financiación con títulos valores (“Securities Financing Transactions”, SFT)
    > y operaciones de liquidación diferida –definidas en el punto 4.2.–.
    > No están comprendidas las exposiciones originadas en operaciones al contado y que involu-
    > cren títulos valores, oro o moneda extranjera, cuya exigencia de capital se calculará conforme
    > a lo previsto en el punto 4.1.

  - [encabezado] 4.3.3 (páginas [88]):

    > 4.3.3. Exposiciones a entidades de contraparte central calificadas.

---

## 3 · índice 1159 · `regula`

- **Origen:** `Obligacion_aplicar_ponderador_de_riesgo_del_30_para_exposiciones_a_bancos_multilaterales_de_cf9e00` · tipo `Obligacion` · label «Aplicar ponderador 30% — BMD calificación A+-A-»
  - propiedades: `{"descripcion": "Aplicar ponderador de riesgo del 30% para exposiciones a bancos multilaterales de desarrollo con calificación desde A+ hasta A-", "tipo": "asignacion"}`
- **Relación:** `regula`
- **Destino:** `Operacion_asignacion_ponderador_riesgo_bmd_a_a_01368a` · tipo `Operacion` · label «Asignación ponderador riesgo BMD (A+-A-)»
  - propiedades: `{"tipo": "asignacion_ponderador_riesgo"}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "cap", "archivo": "TO_capitales_minimos_actual.pdf", "punto": "2.12.3.2", "rol_documental": "punto_propio", "chunk_id": "cap::2.12.3.2", "paginas": [24], "ancestros": ["S2", "2.12", "2.12.3"]}`
- **Provenances (1):**
  - `{"to": "cap", "archivo": "TO_capitales_minimos_actual.pdf", "punto": "2.12.3.2", "rol_documental": "punto_propio", "chunk_id": "cap::2.12.3.2", "paginas": [24], "ancestros": ["S2", "2.12", "2.12.3"]}`
- **Texto del punto ancla** (`cap::2.12.3.2`):

> 2.12.3.2. Demás.
> AAA A+ BBB+ BB+
> Inferior a No
> Calificación hasta hasta hasta hasta
> B- calificado
> AA- A- BBB- B-
> Ponderador
> 20% 30% 50% 100% 150% 50%
> de riesgo

- **Herencia (8):**
  - [encabezado] S2 (páginas [7]):

    > Sección 2. Capital mínimo por riesgo de crédito.

  - [chapeau_seccion] S2 (páginas [7]):

    > A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras
    > se clasificarán en:
    > i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local

  - [chapeau_seccion] S2 (páginas [7]):

    > (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor-
    > tancia sistémica global (G-SIB).

  - [chapeau_seccion] S2 (páginas [7]):

    > ii) Grupo 2: entidades financieras no comprendidas en el acápite i).
    > En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados
    > grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos.
    > Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los
    > acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas
    > correspondientes al nuevo grupo al que pertenezcan.

  - [encabezado] 2.12 (páginas [22]):

    > 2.12. Tabla de ponderadores de riesgo.

  - [intro] 2.12 (páginas [22]):

    > Concepto Ponderador

  - [intro] 2.12 (páginas [22]):

    > –en %–

  - [encabezado] 2.12.3 (páginas [24]):

    > 2.12.3. Exposiciones a bancos multilaterales de desarrollo (BMD).

---

## 4 · índice 1168 · `aplica_a`

- **Origen:** `Obligacion_apr_c_activos_ponderados_por_riesgo_de_credito_determinados_mediante_la_suma_de__abf714` · tipo `Obligacion` · label «Cálculo APR_C activos ponderados por riesgo»
  - propiedades: `{"descripcion": "APR_C: activos ponderados por riesgo de crédito, determinados mediante la suma de los valores obtenidos luego de aplicar la siguiente expresión: A x p + PFB x CCF x p + no DvP + (DVP + RCD + INC(inversiones significativas en empresas)) x 12,5, donde A es activos computables/exposiciones, PFB es partidas fuera de balance, CCF es factor de conversión crediticia, p es ponderador de riesgo.", "tipo": "calculo"}`
- **Relación:** `aplica_a`
- **Destino:** `Sujeto_rol_alcance_capmin` · tipo `Sujeto` · label «Entidades alcanzadas (Capitales Mínimos)»
  - propiedades: `{"nivel": "rol", "cola_humana": "true", "cola_chunks": ["cap::11.3", "cap::2.6.2::cierre", "cap::2.8.2", "cap::3.1.11.1", "cap::4.2.1.1", "cap::5.3.2.3", "cap::6.1.2.1", "cap::6.2.2.6", "cap::6.3.2.2", "cap::6.8.3.2", "cap::7.1.1.1"], "estado_e3": "cola_humana; cola_humana_reextraccion_invalida; cola_humana_veredicto_inutilizable"}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "cap", "archivo": "TO_capitales_minimos_actual.pdf", "punto": "2.1", "rol_documental": "punto_propio", "chunk_id": "cap::2.1", "paginas": [7, 8, 9], "ancestros": ["S2"]}`
- **Provenances (1):**
  - `{"to": "cap", "archivo": "TO_capitales_minimos_actual.pdf", "punto": "2.1", "rol_documental": "punto_propio", "chunk_id": "cap::2.1", "paginas": [7, 8, 9], "ancestros": ["S2"]}`
- **Texto del punto ancla** (`cap::2.1`):

> 2.1. Exigencia.
> Se determinará aplicando la siguiente expresión:
> C = (k x 0,08 x APR ) + INC
> RC C
> donde:
> C : exigencia de capital por riesgo de crédito.
> RC
> k: factor vinculado a la calificación asignada a la entidad según la evaluación efectuada por
> la SEFYC, teniendo en cuenta la siguiente escala:
> Calificación asignada Valor de “k”
> 1 1
> 2 1,03
> 3 1,08
> 4 1,13
> 5 1,19
> A este efecto, se considerará la última calificación informada para el cálculo de la
> exigencia que corresponda integrar al tercer mes siguiente a aquel en que tenga lugar la
> notificación. En tanto no se comunique, el valor de “k” será igual a 1,03.
> APR : activos ponderados por riesgo de crédito, determinados mediante la suma de los valores
> C
> obtenidos luego de aplicar la siguiente expresión:
> A x p + PFB x CCF x p + no DvP + (DVP + RCD + INC(inversiones empresas)) x 12,5
> significativas en
> donde:
> A: activos computables/exposiciones.
> PFB: partidas fuera de balance (conceptos computables no registrados en el balance
> de saldos).
> CCF: factor de conversión crediticia.
> p: ponderador de riesgo, en tanto por uno.
> no DvP: operaciones sin entrega contra pago. Importe determinado mediante la suma
> de los valores obtenidos luego de aplicar a las operaciones comprendidas el
> correspondiente ponderador de riesgo (p) conforme a lo dispuesto en el punto
> 4.1.
> DvP: operaciones de entrega contra pago fallidas (a los efectos de estas normas,
> incluyen las operaciones de pago contra pago –PvP– fallidas). Importe
> determinado mediante la suma de los valores obtenidos luego de multiplicar la
> exposición actual positiva por la exigencia de capital aplicable establecida en el
> punto 4.1.
> RCD: exigencia por riesgo de crédito de contraparte en operaciones con derivados
> extrabursátiles (over-the-counter, OTC), determinada conforme a lo establecido
> en el punto 4.2.
> INC(inversiones empresas): incremento por los excesos a los siguientes límites:
> significativas en
> – participación en el capital de cada empresa: 15%;
> – total de participaciones en el capital de empresas: 60%.
> Los límites máximos establecidos se aplicarán sobre la responsabilidad
> patrimonial computable (RPC) de la entidad financiera del último día anterior al
> que corresponda.
> INC: incremento por los siguientes excesos:
> – en la relación de activos inmovilizados y otros conceptos (Sección 4. del respectivo
> TO), excluidos los computados para la determinación del INC(inversiones
> significativas en
> empresas);
> – a los límites establecidos en el TO sobre Financiamiento al Sector Público no
> Financiero, excluidos los computados para la determinación del INC(inversiones
> significativas en empresas);
> – a los límites establecidos en el TO sobre Grandes Exposiciones al Riesgo de Crédito
> –según lo previsto en el acápite ii), punto 2.1. del TO sobre Incumplimientos de
> Capitales Mínimos y Relaciones Técnicas. Criterios Aplicables–, excluidos los
> computados para la determinación del INC(inversiones empresas);
> significativas en
> – a los límites de graduación del crédito (Sección 3. del respectivo TO); y
> – al límite de derivados sobre materias primas o productos básicos –commodities–
> previsto en el punto 1.2. del TO sobre Operaciones al Contado a Liquidar y a
> Término, Pases, Cauciones, Otros Derivados y con Fondos Comunes de Inversión.
> En la materia, serán de aplicación las disposiciones contenidas en la Sección 2. del TO
> sobre Incumplimientos de Capitales Mínimos y Relaciones Técnicas. Criterios
> Aplicables, salvo que resulte aplicable lo previsto en la Sección 3. de esas normas.
> También se computará en esta expresión la exposición crediticia resultante de la
> utilización de los cupos crediticios ampliados a que se refieren los puntos 6.1.1.2. y
> 6.1.2.1. –acápite d)– del TO sobre Financiamiento al Sector Público no Financiero
> (considerando, en su caso, lo establecido en la Sección 9. de las citadas normas)
> respecto de la asistencia financiera otorgada y/o las tenencias de instrumentos de deuda
> de fideicomisos financieros o fondos fiduciarios a que se refiere el punto 5.1. del TO
> sobre Financiamiento al Sector Público no Financiero y el punto 3.2.4. del citado
> ordenamiento computadas conforme al siguiente cronograma, el cual operará a partir de
> que se hayan comenzado a utilizar económicamente las obras o el equipamiento genere
> ingresos al fideicomiso o fondo fiduciario a través de tarifas, tasas, aranceles u otros
> conceptos similares.
> Cómputo como INC del uso del cupo
> A partir del
> ampliado –en % de dicha utilización–
> 25 Primer mes
> 50 Séptimo mes
> 100 Décimo tercer mes
> El sector público no financiero citado en estas normas es aquel definido en la Sección 1. del TO
> sobre Financiamiento al Sector Público no Financiero.

- **Herencia (4):**
  - [encabezado] S2 (páginas [7]):

    > Sección 2. Capital mínimo por riesgo de crédito.

  - [chapeau_seccion] S2 (páginas [7]):

    > A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras
    > se clasificarán en:
    > i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local

  - [chapeau_seccion] S2 (páginas [7]):

    > (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor-
    > tancia sistémica global (G-SIB).

  - [chapeau_seccion] S2 (páginas [7]):

    > ii) Grupo 2: entidades financieras no comprendidas en el acápite i).
    > En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados
    > grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos.
    > Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los
    > acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas
    > correspondientes al nuevo grupo al que pertenezcan.

---

## 5 · índice 1270 · `regula`

- **Origen:** `Obligacion_comprendera_la_totalidad_de_los_activos_externos_liquidos_de_la_entidad_netos_de_b241c1` · tipo `Obligacion` · label «Incluir activos externos líquidos netos en PGC»
  - propiedades: `{"descripcion": "Comprenderá la totalidad de los activos externos líquidos de la entidad, netos de los saldos deudores de corresponsalía originados en la operatoria del mercado de cambios.", "tipo": "otra"}`
- **Relación:** `regula`
- **Destino:** `Operacion_posicion_general_de_cambios_pgc_4fc69a` · tipo `Operacion` · label «Posición General de Cambios (PGC)»
  - propiedades: `{"tipo": "medición de posición cambiaria"}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "ext", "archivo": "TO_exterior_cambios_actual.pdf", "punto": "6.7", "rol_documental": "punto_propio", "chunk_id": "ext::6.7", "paginas": [77], "ancestros": ["S6"]}`
- **Provenances (1):**
  - `{"to": "ext", "archivo": "TO_exterior_cambios_actual.pdf", "punto": "6.7", "rol_documental": "punto_propio", "chunk_id": "ext::6.7", "paginas": [77], "ancestros": ["S6"]}`
- **Texto del punto ancla** (`ext::6.7`):

> 6.7. Posición general de cambios (PGC).
> Comprenderá la totalidad de los activos externos líquidos de la entidad, netos de los saldos
> deudores de corresponsalía originados en la operatoria del mercado de cambios. También
> quedarán comprendidas las compras y ventas concertadas en el mercado de cambios y que
> se encuentran pendientes de liquidación.
> Serán considerados activos externos líquidos de la entidad, entre otros: monedas y billetes en
> moneda extranjera, disponibilidades en oro amonedado o en barras de buena entrega, saldos
> acreedores de corresponsalía (incluyendo las transferencias a favor de terceros sin liquidación
> concertada), otros depósitos a la vista en entidades financieras del exterior, inversiones en
> títulos públicos externos y certificados de depósito a plazo.
> No formarán parte de la PGC: inversiones directas en el exterior, activos externos de terceros
> en custodia, ventas y compras a término de divisas o valores externos, depósitos en el BCRA
> en moneda extranjera en cuentas a nombre de la entidad y demás activos locales en moneda
> extranjera.

- **Herencia (2):**
  - [encabezado] S6 (páginas [75]):

    > Sección 6. Definiciones.

  - [chapeau_seccion] S6 (páginas [75]):

    > En el marco de estas disposiciones se definen los siguientes conceptos:

---

## 6 · índice 1750 · `regula`

- **Origen:** `Obligacion_debera_tenerse_en_cuenta_lo_dispuesto_en_el_punto_4_2_2994d2` · tipo `Obligacion` · label «Tener en cuenta disposición punto 4.2»
  - propiedades: `{"descripcion": "Deberá tenerse en cuenta lo dispuesto en el punto 4.2", "tipo": "otra"}`
- **Relación:** `regula`
- **Destino:** `Operacion_operaciones_con_derivados_no_comprendidas_en_2_12_14_9ae0b3` · tipo `Operacion` · label «Operaciones con derivados no comprendidas en 2.12.14»
  - propiedades: `{"tipo": "operaciones con derivados"}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "cap", "archivo": "TO_capitales_minimos_actual.pdf", "punto": "2.12.15", "rol_documental": "punto_propio", "chunk_id": "cap::2.12.15", "paginas": [27], "ancestros": ["S2", "2.12"]}`
- **Provenances (1):**
  - `{"to": "cap", "archivo": "TO_capitales_minimos_actual.pdf", "punto": "2.12.15", "rol_documental": "punto_propio", "chunk_id": "cap::2.12.15", "paginas": [27], "ancestros": ["S2", "2.12"]}`
- **Texto del punto ancla** (`cap::2.12.15`):

> 2.12.15. Operaciones con derivados no comprendidas en el punto 2.12.14. Deberá
> tenerse en cuenta lo dispuesto en el punto 4.2.

- **Herencia (7):**
  - [encabezado] S2 (páginas [7]):

    > Sección 2. Capital mínimo por riesgo de crédito.

  - [chapeau_seccion] S2 (páginas [7]):

    > A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras
    > se clasificarán en:
    > i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local

  - [chapeau_seccion] S2 (páginas [7]):

    > (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor-
    > tancia sistémica global (G-SIB).

  - [chapeau_seccion] S2 (páginas [7]):

    > ii) Grupo 2: entidades financieras no comprendidas en el acápite i).
    > En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados
    > grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos.
    > Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los
    > acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas
    > correspondientes al nuevo grupo al que pertenezcan.

  - [encabezado] 2.12 (páginas [22]):

    > 2.12. Tabla de ponderadores de riesgo.

  - [intro] 2.12 (páginas [22]):

    > Concepto Ponderador

  - [intro] 2.12 (páginas [22]):

    > –en %–

---

## 7 · índice 1973 · `regula`

- **Origen:** `Obligacion_el_activo_ponderado_por_riesgo_se_calculara_como_la_diferencia_entre_el_importe__0e4aa0` · tipo `Obligacion` · label «Calcular activo ponderado por riesgo»
  - propiedades: `{"descripcion": "El activo ponderado por riesgo se calculará como la diferencia entre el importe de la exposición –ajustado por volatilidad– y el valor del activo recibido en garantía –luego de aplicar los aforos que corresponda según la tabla de aforos regulatorios– multiplicada por el ponderador de riesgo de la contraparte conforme a la tabla de ponderadores de riesgo de la Sección 2.", "tipo": "calculo"}`
- **Relación:** `regula`
- **Destino:** `Operacion_ajuste_de_exposicion_y_garantia_por_volatilidad_da4e64` · tipo `Operacion` · label «Ajuste de exposición y garantía por volatilidad»
  - propiedades: `{"tipo": "Ajuste de exposición y activo recibido en garantía por volatilidad de mercado"}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "cap", "archivo": "TO_capitales_minimos_actual.pdf", "punto": "5.3.2", "rol_documental": "bloque_intro", "chunk_id": "cap::5.3.2::intro", "paginas": [106], "ancestros": ["S5", "5.3"]}`
- **Provenances (1):**
  - `{"to": "cap", "archivo": "TO_capitales_minimos_actual.pdf", "punto": "5.3.2", "rol_documental": "bloque_intro", "chunk_id": "cap::5.3.2::intro", "paginas": [106], "ancestros": ["S5", "5.3"]}`
- **Texto del punto ancla** (`cap::5.3.2::intro`):

> Con este método, las entidades financieras deberán ajustar los valores de la exposición
> y del activo recibido en garantía, a fin de tener en cuenta posibles futuras variaciones de
> su valor de mercado. El importe resultante luego de realizar este ajuste por volatilidad
> será superior en el caso de la exposición –con la excepción de los préstamos otorgados
> en efectivo– e inferior en el caso de la garantía –excepto cuando esté constituida por un
> depósito en la misma moneda que la exposición–.
> El activo ponderado por riesgo se calculará como la diferencia entre el importe de la ex-
> posición –ajustado por volatilidad– y el valor del activo recibido en garantía –luego de
> aplicar los aforos que corresponda (H , H y H ) según la tabla de aforos regulatorios
> e c fx
> prevista en el punto 5.3.2.3.– multiplicada por el ponderador de riesgo de la contraparte
> –conforme a la tabla de ponderadores de riesgo de la Sección 2.–.

- **Herencia (3):**
  - [encabezado] S5 (páginas [98]):

    > Sección 5. Cobertura del riesgo de crédito.

  - [encabezado] 5.3 (páginas [103]):

    > 5.3. Operaciones cubiertas con activos admitidos como garantía.

  - [encabezado] 5.3.2 (páginas [106]):

    > 5.3.2. Método integral o de reducción de la exposición.

---

## 8 · índice 2184 · `aplica_a`

- **Origen:** `Obligacion_el_deudor_debe_demostrar_el_ingreso_y_liquidacion_de_divisas_en_el_mercado_de_ca_c4595f` · tipo `Obligacion` · label «Demostración ingreso liquidación divisas por diferencia»
  - propiedades: `{"descripcion": "El deudor debe demostrar el ingreso y liquidación de divisas en el mercado de cambios por la diferencia entre el valor efectivo y el valor nominal en emisiones de títulos de deuda con registro público colocados bajo la par", "tipo": "otra"}`
- **Relación:** `aplica_a`
- **Destino:** `Sujeto_rol_entidad_autorizada_exterior` · tipo `Sujeto` · label «Entidades autorizadas a operar en cambios (Exterior)»
  - propiedades: `{"nivel": "rol", "cola_humana": "true", "cola_chunks": ["ext::10.10.2.3", "ext::10.3.2.5", "ext::10.3.3", "ext::10.3.5::intro", "ext::10.4.3::intro", "ext::10.5.5.2", "ext::10.9.4", "ext::13.2.7::intro", "ext::13.3.3", "ext::13.3.9", "ext::13.4.8", "ext::14.2.1.10", "ext::14.2.1::intro", "ext::14.5.3", "ext::3.11.2.1", "ext::3.11.3::cierre", "ext::3.14.5.5", "ext::3.16.2.1", "ext::3.17.5", "ext::3.18.1::cierre", "ext::3.3.3.4", "ext::3.5.1.12", "ext::3.5.1.9", "ext::3.5.6.10", "ext::3.5::intro", "ext::3.9::intro", "ext::4.4.2", "ext::4.8.1.1", "ext::4.8.1.2", "ext::4.8.1.3", "ext::4.8.1.5", "ext::7.10.6", "ext::7.11.2::cierre", "ext::7.11.3::intro", "ext::7.3::intro", "ext::7.5.7.1", "ext::7.6.1.1", "ext::7.9.1.4", "ext::7.9.3::intersticial", "ext::9.3.2", "ext::9.3.3.1", "ext::9.3.7"], "estado_e3": "cola_humana; cola_humana_veredicto_inutilizable"}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "ext", "archivo": "TO_exterior_cambios_actual.pdf", "punto": "3.5.1.4", "rol_documental": "punto_propio", "chunk_id": "ext::3.5.1.4", "paginas": [20], "ancestros": ["S3", "3.5", "3.5.1"]}`
- **Provenances (1):**
  - `{"to": "ext", "archivo": "TO_exterior_cambios_actual.pdf", "punto": "3.5.1.4", "rol_documental": "punto_propio", "chunk_id": "ext::3.5.1.4", "paginas": [20], "ancestros": ["S3", "3.5", "3.5.1"]}`
- **Texto del punto ancla** (`ext::3.5.1.4`):

> 3.5.1.4. por la diferencia entre el valor efectivo y el valor nominal en emisiones de
> títulos de deuda con registro público colocados bajo la par.

- **Herencia (6):**
  - [encabezado] S3 (páginas [16]):

    > Sección 3. Disposiciones específicas para los egresos por el mercado de cambios

  - [chapeau_seccion] S3 (páginas [16]):

    > Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas
    > en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–,
    > adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán
    > cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.

  - [encabezado] 3.5 (páginas [20]):

    > 3.5. Pagos de títulos de deuda suscriptos en el exterior y endeudamientos financieros con el

  - [intro] 3.5 (páginas [20]):

    > exterior.
    > Las entidades podrán dar acceso al mercado de cambios para realizar pagos de capital o
    > intereses de títulos de deuda con registro público en el exterior, otros endeudamientos
    > financieros con el exterior y títulos de deuda con registro público en el país denominados en
    > moneda extranjera íntegramente suscriptos en el exterior, en la medida que se verifiquen las
    > siguientes condiciones:

  - [encabezado] 3.5.1 (páginas [20]):

    > 3.5.1. El deudor demuestre el ingreso y liquidación de divisas en el mercado de cambios por

  - [intro] 3.5.1 (páginas [20]):

    > un monto equivalente al valor nominal del endeudamiento financiero.
    > Este requisito se considerará cumplimentado en los siguientes casos:

---

## 9 · índice 2334 · `establecida_en`

- **Origen:** `Obligacion_el_legajo_y_los_anexos_podran_llevarse_en_medios_magneticos_electronicos_u_otra__aa8a6a` · tipo `Obligacion` · label «Conservación legajo — medios magnéticos electrónicos»
  - propiedades: `{"descripcion": "El legajo y los anexos podrán llevarse en medios magnéticos, electrónicos u otra tecnología similar. En estos dos últimos casos deberán observarse los requisitos incluidos en el punto 1. de las normas sobre \"Instrumentación, conservación y reproducción de documentos\".", "tipo": "otra"}`
- **Relación:** `establecida_en`
- **Destino:** `TextoOrdenado_to_clasificacion_deudores_actual_pdf` · tipo `TextoOrdenado` · label «Clasificación de Deudores»
  - propiedades: `{"materia": "clasificación de deudores", "archivo": "TO_clasificacion_deudores_actual.pdf", "version": "actual", "cola_humana": "true", "cola_chunks": ["cla::3.5.1", "cla::3.5::intro", "cla::6.5.3.5"], "estado_e3": "cola_humana", "materia_variantes": ["clasificación de deudores", "Clasificación de deudores", "clasificacion", "clasificacion_deudores", "clasificación", "Clasificación de Deudores", "Clasificación de deudores y previsión", "Clasificación", "Clasificación de deudores y previsiones por riesgo", "Criterios de clasificación de deudores", "Clasificación de deudores de cartera comercial", "Clasificación de deudores de la cartera comercial", "clasificacion_de_deudores", "clasificación de deudores cartera consumo vivienda"], "version_variantes": ["actual", "", "cla", "vigente"]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "cla", "archivo": "TO_clasificacion_deudores_actual.pdf", "punto": "3.4.5", "rol_documental": "punto_propio", "chunk_id": "cla::3.4.5", "paginas": [13], "ancestros": ["S3", "3.4"]}`
- **Provenances (1):**
  - `{"to": "cla", "archivo": "TO_clasificacion_deudores_actual.pdf", "punto": "3.4.5", "rol_documental": "punto_propio", "chunk_id": "cla::3.4.5", "paginas": [13], "ancestros": ["S3", "3.4"]}`
- **Texto del punto ancla** (`cla::3.4.5`):

> 3.4.5. Aspectos formales.
> El legajo y los anexos podrán llevarse en medios magnéticos, electrónicos u otra tecno-
> logía similar. En estos dos últimos casos deberán observarse los requisitos incluidos en
> el punto 1. de las normas sobre “Instrumentación, conservación y reproducción de docu-
> mentos”.
> La información que surja del “Legajo Único Financiero y Económico” –establecido por la
> Resolución N° 92/21 del Ministerio de Desarrollo Productivo– será considerada para el
> cumplimiento de requerimientos contenidos en estas normas.

- **Herencia (2):**
  - [encabezado] S3 (páginas [9]):

    > Sección 3. Tarea de clasificación.

  - [encabezado] 3.4 (páginas [10]):

    > 3.4. Legajo del cliente.

---

## 10 · índice 3031 · `regula`

- **Origen:** `Obligacion_en_las_operaciones_de_credito_los_sujetos_obligados_podran_aplicar_comisiones_so_0ace27` · tipo `Obligacion` · label «Comisiones fondos no utilizados: servicios crédito»
  - propiedades: `{"descripcion": "En las operaciones de crédito, los sujetos obligados podrán aplicar comisiones sobre los importes no utilizados de los acuerdos de asignación de fondos, dado que su puesta a disposición a los usuarios configura la prestación del servicio.", "tipo": "otra"}`
- **Relación:** `regula`
- **Destino:** `Operacion_comisiones_y_cargos_21710b` · tipo `Operacion` · label «Comisiones y cargos»
  - propiedades: `{"tipo": "cobro de comisiones y cargos"}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "pro", "archivo": "TO_proteccion_usuarios_servicios_financieros_actual.pdf", "punto": "2.3.2.1", "rol_documental": "punto_propio", "chunk_id": "pro::2.3.2.1", "paginas": [11, 12], "ancestros": ["S2", "2.3", "2.3.2"]}`
- **Provenances (1):**
  - `{"to": "pro", "archivo": "TO_proteccion_usuarios_servicios_financieros_actual.pdf", "punto": "2.3.2.1", "rol_documental": "punto_propio", "chunk_id": "pro::2.3.2.1", "paginas": [11, 12], "ancestros": ["S2", "2.3", "2.3.2"]}`
- **Texto del punto ancla** (`pro::2.3.2.1`):

> 2.3.2.1. Admitidos.
> Todas las comisiones, cargos, costos, gastos, seguros y/o cualquier otro con-
> cepto –excluyendo la tasa de interés– que los sujetos obligados perciban o pre-
> tendan percibir de los usuarios de servicios financieros (comisiones y cargos),
> deben tener origen en un costo real, directo y demostrable y estar debidamente
> justificados desde el punto de vista técnico y económico.
> La aplicación de comisiones y/o cargos debe quedar circunscripta a la efectiva
> prestación de un servicio que haya sido previamente solicitado, pactado y/o au-
> torizado por el usuario.
> Las comisiones obedecen a servicios que prestan los sujetos obligados y, en
> tal sentido, pueden incluir retribuciones a su favor que excedan el costo de la
> prestación.
> Los cargos obedecen a servicios que prestan terceros, por lo que solamente
> pueden ser transferidos al costo a los usuarios.
> Asimismo, el importe de los cargos que el sujeto obligado transfiera a los usua-
> rios no podrá ser superior al que el tercero prestador perciba de particulares,
> sin intermediarios y en similares condiciones (servicios postales, compañía de
> seguros, escribanía y registros de propiedad, u otros de índole similar).
> En las operaciones de crédito, los sujetos obligados podrán aplicar comisiones
> sobre los importes no utilizados de los acuerdos de asignación de fondos, dado
> que su puesta a disposición a los usuarios configura la prestación del servicio.
> La precancelación total o parcial de financiaciones podrá dar lugar a la aplica-
> ción de comisiones. En el caso de precancelación total, no se admitirá la apli-
> cación de comisiones cuando al momento de efectuarla haya transcurrido al
> menos la cuarta parte del plazo original de la financiación o 180 días corridos
> desde su otorgamiento, de ambos el mayor.
> Además, será de aplicación lo previsto en el punto 1.7. del TO sobre Tasas de
> Interés en las Operaciones de Crédito.

- **Herencia (3):**
  - [encabezado] S2 (páginas [5]):

    > Sección 2. Derechos básicos de los usuarios de servicios financieros.

  - [encabezado] 2.3 (páginas [7]):

    > 2.3. Recaudos mínimos de la relación de consumo.

  - [encabezado] 2.3.2 (páginas [11]):

    > 2.3.2. Comisiones y cargos.

---

## 11 · índice 3215 · `establecida_en`

- **Origen:** `Obligacion_especificar_el_valor_nocional_incluyendo_la_moneda_o_unidad_de_medida_por_ejempl_fa68cb` · tipo `Obligacion` · label «Especificación del valor nocional»
  - propiedades: `{"tipo": "presentacion_informativa", "descripcion": "Especificar el valor nocional incluyendo la moneda o unidad de medida. Por ejemplo, USD 25.000.000, $ 100.000, etc."}`
- **Relación:** `establecida_en`
- **Destino:** `TextoOrdenado_to_regimen_informativo_contable_mensual_actual_pdf` · tipo `TextoOrdenado` · label «Texto Ordenado Régimen Informativo Contable»
  - propiedades: `{"materia": "régimen informativo contable mensual", "archivo": "TO_regimen_informativo_contable_mensual_actual.pdf", "version": "actual", "cola_humana": "true", "cola_chunks": ["ric::9.1.3"], "estado_e3": "cola_humana", "materia_variantes": ["régimen informativo contable mensual", "Régimen informativo contable mensual", "regimen_informativo", "Régimen Informativo Contable Mensual", "Régimen informativo", "información contable y régimen informativo", "Régimen Informativo", "Régimen informativo contable", "régimen informativo contable", "Régimen Informativo Contable", "Exigencia por riesgo operacional", "régimen informativo", "Responsabilidad Patrimonial Computable", "Régimen informativo y contable", "Ratio de apalancamiento", "información complementaria - riesgo de tasa de interés", "riesgo de tasa de interés en cartera de inversión", "Información complementaria vinculada al cálculo del riesgo de tasa de interés en cartera de inversión", "Información complementaria vinculada al cálculo del riesgo de tasa de interés", "información complementaria vinculada al cálculo del riesgo de tasa de interés", "Información complementaria vinculada al riesgo de tasa de interés en cartera de inversión"], "version_variantes": ["actual", "", "1a"]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "ric", "archivo": "TO_regimen_informativo_contable_mensual_actual.pdf", "punto": "4.5.2", "rol_documental": "punto_propio", "chunk_id": "ric::4.5.2", "paginas": [19], "ancestros": ["S4", "4.5"]}`
- **Provenances (1):**
  - `{"to": "ric", "archivo": "TO_regimen_informativo_contable_mensual_actual.pdf", "punto": "4.5.2", "rol_documental": "punto_propio", "chunk_id": "ric::4.5.2", "paginas": [19], "ancestros": ["S4", "4.5"]}`
- **Texto del punto ancla** (`ric::4.5.2`):

> 4.5.2. Futuros y Contratos a Término, incluidos los FRA
> Fecha
> Tasa de cupón
> correspondiente al Precio de
> Descripción del Contraparte/Ámb del activo Precio pactado
> plazo residual del Vencimiento del mercado del Compra / venta a
> activo ito de Valor nocional(3) subyacente del subyacente
> subyacente derivado activo término (6)
> subyacente(1) negociación (cuando (5)
> (cuando subyacente
> corresponda)(4)
> corresponda)(2)
> (1) Describir el activo comprado o vendido a futuro. Por ejemplo: Tasa de interés Badlar Privada para
> depósitos de más de 1 millón de pesos por un plazo de 30 a 35 días, dólar estadounidense, Bono
> de la Nación Arg. en dólar link con vencimiento al 2017 - AJ17D, etc.
> (2) Por ejemplo, en un futuro sobre un título público es el plazo residual del título público subyacente.
> (3) Especificar el valor nocional incluyendo la moneda o unidad de medida. Por ejemplo, USD
> 25.000.000, $ 100.000, etc.
> (4) Por ejemplo, en un futuro sobre un título público, es la tasa del cupón corriente de dicho título
> (5) Valor del subyacente pactado. Por ejemplo, valor de la tasa fija pactada, valor pactado del dólar,
> valor pactado del bono, etc.
> (6) Consignar "C" si el contrato en cuestión es una compra a término, o "V" si es una venta a término.

- **Herencia (2):**
  - [encabezado] S4 (páginas [11]):

    > Sección 4. Exigencia e integración por riesgo de mercado

  - [encabezado] 4.5 (páginas [19]):

    > 4.5. Información sobre instrumentos derivados

---

## 12 · índice 3913 · `establecida_en`

- **Origen:** `Obligacion_la_entidad_debera_verificar_previamente_a_emitir_cada_certificacion_el_cumplimie_77ebf1` · tipo `Obligacion` · label «Verificar requisitos previo a emisión de certificación»
  - propiedades: `{"descripcion": "La entidad deberá verificar, previamente a emitir cada certificación, el cumplimiento de los requisitos establecidos a la fecha de emisión de la certificación.", "tipo": "otra"}`
- **Relación:** `establecida_en`
- **Destino:** `TextoOrdenado_to_exterior_cambios_actual_pdf` · tipo `TextoOrdenado` · label «Texto Ordenado de Exterior y Cambios»
  - propiedades: `{"materia": "exterior", "archivo": "TO_exterior_cambios_actual.pdf", "version": "actual", "descripcion": "Comprende a la administración central de provincias, de la Ciudad Autónoma de Buenos Aires, y de las municipalidades del país.", "cola_humana": "true", "cola_chunks": ["ext::10.10.2.3", "ext::10.10.2.5", "ext::10.2.4.9", "ext::10.3.2.5", "ext::10.3.3", "ext::10.3.5::intro", "ext::10.4.3::intro", "ext::10.5.5.2", "ext::10.9.4", "ext::13.2.7::intro", "ext::13.3.3", "ext::13.3.9", "ext::13.4.8", "ext::14.2.1.10", "ext::14.2.1.6", "ext::14.2.1.7", "ext::14.2.1::intro", "ext::14.5.3", "ext::3.11.2.1", "ext::3.11.3::cierre", "ext::3.14.2", "ext::3.14.5.5", "ext::3.16.2.1", "ext::3.17.3::intro", "ext::3.17.5", "ext::3.18.1::cierre", "ext::3.3.3.4", "ext::3.4.4::intro", "ext::3.5.1.12", "ext::3.5.1.9", "ext::3.5.3.5", "ext::3.5.6.10", "ext::3.5::intro", "ext::3.9::intro", "ext::4.2.8", "ext::4.4.2", "ext::4.7.2", "ext::4.8.1.1", "ext::4.8.1.2", "ext::4.8.1.3", "ext::4.8.1.5", "ext::4.8.2", "ext::7.10.6", "ext::7.11.2::cierre", "ext::7.11.3::intro", "ext::7.11.5", "ext::7.3.6", "ext::7.3::intro", "ext::7.5.7.1", "ext::7.6.1.1", "ext::7.8.5::intro", "ext::7.9.1.4", "ext::7.9.1.6", "ext::7.9.3::intersticial", "ext::8.2::intro", "ext::9.3.2", "ext::9.3.3.1", "ext::9.3.7"], "estado_e3": "cola_humana; cola_humana_veredicto_inutilizable", "materia_variantes": ["exterior", "operaciones en el mercado de cambios", "Operaciones de cambio", "exterior_cambios", "Régimen de operaciones en el exterior y operaciones de cambio", "Exterior y cambios", "Operaciones de cambio en el exterior", "Operaciones en mercado de cambios", "Operaciones cambiarias en el exterior", "Operatoria de cambios e ingresos por mercado de cambios", "Operaciones de cambios y exterior", "Disposiciones específicas para los ingresos por el mercado de cambios", "Disposiciones específicas para operaciones en el mercado de cambios — cobros de exportaciones de servicios", "Disposiciones para ingresos por mercado de cambios - Cobros de exportaciones de servicios", "Operaciones en el mercado de cambios - Exterior", "Exterior y Cambios", "Operaciones en el mercado de cambios — títulos de deuda y endeudamientos", "Operaciones en el mercado de cambios", "Disposiciones específicas para ingresos por mercado de cambios", "Operaciones de cambios — Exterior", "Exterior Cambios", "Operaciones en cambios - Ingresos por mercado de cambios", "Exterior", "Operaciones de cambios en el exterior", "Operaciones en cambios para residentes en el exterior", "Operaciones en mercado de cambios — Exterior", "Operaciones en el mercado de cambios — obligaciones de liquidación", "Operaciones de cambio - ingresos por mercado de cambios", "Operaciones de cambios en el mercado de cambios", "Operaciones de cambios", "Disposiciones para egresos por mercado de cambios", "Operaciones en el mercado de cambios - Egresos", "Disposiciones específicas para egresos por mercado de cambios", "Operaciones del mercado de cambios", "Operaciones en el mercado de cambios — Pagos de intereses de deudas por importaciones", "Disposiciones para operaciones de cambio - egresos", "Operaciones en cambios — Egresos", "Operaciones del mercado de cambios — Egresos", "Operaciones en cambios", "Operaciones de cambios — egresos", "Operaciones de cambios — Egresos", "Operaciones en el mercado de cambios — egresos", "Operaciones de cambios – disposiciones específicas para egresos", "Operaciones de cambio — egresos", "Operaciones de cambio — pagos títulos de deuda y endeudamientos", "Operaciones en el mercado de cambios — Pagos de títulos de deuda", "Operaciones en mercado de cambios — pagos de títulos y endeudamientos", "Operaciones por el mercado de cambios — pagos de títulos de deuda", "Pagos de títulos de deuda y endeudamientos con el exterior", "Operaciones de cambios - Egresos", "Operaciones en el mercado de cambios — pagos de títulos de deuda y endeudamientos", "Operaciones de cambio - Exterior", "Operaciones en el mercado de cambios — pagos de deuda y endeudamientos con el exterior", "Operaciones de cambio — Pagos de títulos de deuda y endeudamientos con el exterior", "Operaciones en el mercado de cambios — pagos de deuda externa", "Operaciones de cambios - Exterior", "Egresos por el mercado de cambios", "Egresos por mercado de cambios", "Operaciones de cambio en el mercado exterior", "Disposiciones específicas para operaciones de cambios", "Operaciones de cambio - Pagos de títulos de deuda en moneda extranjera", "Disposiciones para operaciones en el mercado de cambios", "Operaciones en el mercado de cambios — títulos de deuda", "Disposiciones para operaciones en mercado de cambios", "Operaciones en el mercado de cambios — Egresos", "Disposiciones para operaciones de cambio — exterior", "Operaciones de cambios - Egresos por el mercado de cambios", "Exterior y operaciones de cambio", "Disposiciones para operaciones de cambios en el exterior", "Disposiciones para operaciones de cambios y egreso de divisas", "Operaciones cambiarias", "Exterior - Cambios", "Disposiciones para operaciones de cambios - residentes con endeudamientos o fideicomisos", "operaciones de cambios — egresos", "Operaciones en el mercado de cambios para residentes", "Operaciones en mercado de cambios — egresos", "Operaciones en el mercado de cambios - egresos por residentes", "Disposiciones para operaciones de cambios — egresos", "Operaciones de cambio en el mercado de divisas", "Disposiciones para egresos por el mercado de cambios", "Operaciones de cambios y derivados", "Operaciones en cambios - Exterior", "Operaciones de cambio al exterior", "Operaciones de cambios - Repatriaciones y compras de moneda extranjera", "Disposiciones específicas para los egresos por el mercado de cambios", "Operaciones en cambios — Repatriaciones de inversiones directas", "Operaciones cambiarias y repatriaciones de no residentes", "Operaciones de cambios — Repatriaciones", "Operaciones del mercado de cambios - exterior", "Operaciones de cambio y transferencias de divisas", "Operaciones de cambios — Egresos por el mercado de cambios", "operaciones de cambios y egresos por el mercado de cambios", "Operaciones en el mercado de cambios — Exterior", "Operaciones en el mercado de cambios — exterior", "Operaciones de cambio - Cancelación de garantías financieras", "Operaciones de cambio — Exterior", "Operaciones en el mercado de cambios — requisitos complementarios", "Definiciones", "Operaciones de egresos por mercado de cambios", "Disposiciones para operaciones de cambios", "Operaciones de cambio - Egresos", "Mercado de cambios", "Operaciones de cambios — exterior", "Acceso al mercado de cambios", "Operaciones de cambios del mercado exterior", "Operaciones de cambio - repatriaciones de inversiones directas", "Disposiciones específicas para egresos por el mercado de cambios", "Operaciones de cambios y acceso a divisas", "Acceso a divisas para producción incremental", "Operaciones en el mercado de cambios — acceso a divisas", "Operaciones en el mercado de cambios — régimen de acceso a divisas para producción incremental de petróleo y/o gas", "Operaciones de cambios en el mercado exterior", "Operaciones de cambios — egreso de moneda extranjera", "Operaciones en el mercado de cambios - Acceso con Certificación de aumento de exportaciones", "Operaciones cambiaras, exportaciones", "Operaciones en el exterior y cambios", "Operaciones con moneda extranjera — retiros de efectivo desde el exterior", "Operaciones cambiarias y de exterior", "Operaciones con débito en cuenta local y tarjetas — Pagos al exterior", "Operaciones en el exterior y acceso al mercado de cambios", "Operaciones con cambios", "Operaciones con cambios — exterior", "Operaciones cambiarias y comerciales", "Operaciones en cambios — exterior", "Operaciones de comercio exterior y cambios", "Operaciones de cambio y comercio exterior", "Operaciones en cambios - exterior", "Operaciones con títulos valores", "Operaciones cambios exterior", "Operaciones con títulos valores — Exterior", "Operaciones en cambios - Entidades autorizadas", "Operaciones en cambios — Exterior", "Operaciones de cambio y exterior", "Operaciones de cambio de no residentes", "Operaciones cambiarias con no residentes", "Operaciones en cambios, suscripción de BOPREAL", "Operaciones de cambios — entidades autorizadas", "Operaciones en cambios y exterior", "Régimen de Operaciones de Cambios del Exterior", "exterior y cambios", "Operaciones en cambios en el exterior", "Operaciones de cambio, suscripción de bonos BOPREAL", "operaciones de cambio y exterior", "Operaciones en cambios, exterior", "Operaciones de cambio en exterior", "Operatoria de cambios en el exterior", "Operaciones de cambio — pautas operativas", "Operaciones de cambios — entidades financieras y cambiarias", "Operaciones de cambio y transferencias de fondos con el exterior", "Operaciones de cambio y transferencias de fondos desde y hacia el exterior", "Operaciones con cambios en el exterior", "Operaciones cambiarias — Exterior", "Operaciones de cambios y transferencias de divisas", "Operaciones de cambio y posiciones en moneda extranjera", "Pautas operativas para entidades autorizadas a operar en cambios", "Operaciones de cambios y tenencias en moneda extranjera", "Operaciones cambiarias propias", "Operaciones de cambio exterior", "Operaciones de cambio y remesas al exterior", "Operaciones en el exterior", "Operaciones de cambios y arbitrajes en el exterior", "Operaciones en cambios de entidades autorizadas", "Operaciones de cambio — importación y exportación de moneda nacional", "operaciones cambiarias", "Operaciones de cambio — exterior", "Exterior — Cambios", "Definiciones — Servicios", "Definición de Gobiernos locales", "Cobros de exportaciones de bienes", "Cobros de exportaciones", "Cobros de exportaciones de bienes — Exterior", "Cambios — Operaciones de comercio exterior", "Operaciones cambiarias en cuenta corriente de exportadores", "Operaciones de cambios - Cobros de exportaciones de bienes", "Operaciones con el Exterior - Cambios", "Operaciones financieras enunciadas", "Operaciones cambiarias del exterior", "Cambios - Exterior", "Operaciones de cambios, exterior", "Operaciones de cambios, cobros y pagos en el exterior", "Cobros de exportaciones — Ampliaciones de plazo", "Cobros de exportaciones de bienes — ampliaciones de plazo para liquidación de divisas", "Operaciones de cambio, comercio exterior", "Operaciones en cambios del exterior", "Cobros de exportaciones de bienes — Deudor moroso", "Cobros de exportaciones y exterior", "Operaciones de comercio exterior", "Operaciones cambiarias al exterior", "Operaciones de cambios y comercio exterior", "Operaciones en cambios y comercio exterior", "Cambios - Operaciones en el exterior", "Cobros de exportaciones de bienes - Régimen de fomento para las exportaciones de la economía del conocimiento", "Operaciones financieras habilitadas para aplicar cobros de exportaciones", "Operaciones cambiarias — exterior", "Operaciones cambistas de entidades autorizadas a operar en el exterior", "Operaciones del exterior", "Operaciones de cambios - Cobros de exportaciones", "Operaciones de cambio — Cobros de exportaciones", "Operaciones financieras habilitadas para cobros de exportaciones de bienes", "Cobros de exportaciones de bienes — operaciones financieras habilitadas", "Cobros de exportaciones de bienes y operaciones financieras habilitadas", "Operaciones cambarias y de comercio exterior", "Operaciones de exterior y cambios", "Operaciones en moneda extranjera y cambios", "Cobros de exportaciones de bienes en divisas", "Operaciones en cambios - Cobros de exportaciones", "Operaciones en cambios — Cobros de exportaciones de bienes", "Operaciones cambiarias, cobros de exportaciones", "Operaciones cambiarias en exterior", "Cobros de exportaciones de bienes — Decreto 234/21", "Operaciones de cambio, importaciones y exportaciones", "Cobros de exportaciones de bienes y financiaciones asociadas a importaciones", "Operaciones cambias en el exterior", "Operaciones de cambios, importación, exportación", "Operaciones cambiarias - Exterior", "Operaciones en cambios, financiaciones de exportación/importación", "Operaciones de cambios — Cobros de exportaciones de bienes", "Operaciones de cambios, cobros de exportaciones", "Cobros de exportaciones de bienes — Financiaciones asociadas a importaciones", "Seguimiento de negociaciones de divisas por exportaciones de bienes", "Seguimiento de negociaciones de divisas por exportaciones", "Negociación de divisas por exportaciones", "Operaciones de cambio y seguimiento de exportaciones de divisas", "Seguimiento de negociaciones de divisas por exportaciones de bienes — Exterior", "Operaciones de cambio — Seguimiento de divisas por exportaciones", "Operaciones de cambio y seguimiento de divisas por exportaciones", "Seguimiento de negociaciones de divisas", "Operaciones cambistas - seguimiento de divisas por exportaciones", "Seguimiento de negociaciones de divisas por exportaciones de bienes — Operaciones aduaneras exceptuadas", "Seguimiento de anticipos y financiaciones de exportación", "Seguimiento de anticipos y otras financiaciones de exportación", "Operaciones de cambio y seguimiento de financiaciones de exportación", "Seguimiento de anticipos y otras financiaciones de exportación de bienes", "Operaciones de cambios - Seguimiento de financiaciones de exportación", "Operaciones de cambio y financiaciones de exportación", "Seguimiento de anticipos y financiaciones de exportación de bienes", "Operaciones de cambio y financiación de exportaciones", "Seguimiento de anticipos y otras financiaciones de exportación de bienes; Certificaciones de aplicación de cobros de exportaciones", "Exterior y operaciones de cambios", "Exterior, Cambios, Operaciones de exportación", "Seguimiento de anticipos y financiaciones de exportación; certificaciones de aplicación", "Seguimiento de anticipos y financiaciones de exportación; certificaciones de aplicación de cobros", "Seguimiento de anticipos y otras financiaciones de exportación de bienes. Certificaciones de aplicación de cobros de exportaciones.", "Pagos de importaciones y operaciones de cambios en el exterior", "Pagos de importaciones y operaciones de cambio en el exterior", "Pagos de importaciones", "Pagos de importaciones y compras en el exterior", "Pagos de importaciones y compras en exterior", "Pagos de importaciones y otras compras de bienes en el exterior", "Pagos de importaciones y compras de bienes en exterior", "Pagos de importaciones y compras de bienes en el exterior", "Pagos de importaciones y operaciones de cambios", "Operaciones de cambio - Pagos de importaciones", "Operaciones en cambios, pagos de importaciones", "Exterior y Operaciones de Cambio", "Operaciones de cambio y pagos internacionales", "Pagos de importaciones y operaciones de cambio", "Operaciones en cambios - Pagos de importaciones", "Pagos de importaciones y operaciones cambiarias", "Operaciones de cambio — Pagos de importaciones", "Operaciones de cambios y pagos de importaciones", "Pagos de importaciones y operaciones en el exterior", "Pagos de importaciones y operaciones en cambios", "Pagos de importaciones en el exterior", "Pagos de importaciones y operaciones en cambios — exterior", "Operaciones en cambios y pagos de importaciones", "Operaciones en cambios con el exterior", "Pagos al exterior y operaciones de cambio", "Cambios, Pagos de importaciones", "Operaciones de cambio — Pagos de importaciones y compras de bienes en el exterior", "Pagos de importaciones y cambios", "Operaciones de cambio; pagos de importaciones", "Pagos de importaciones y operaciones cambiarias en el exterior", "Operaciones de cambios. Pagos de importaciones.", "Pagos de importaciones — Operaciones de cambio", "Operaciones en cambios — pagos de importaciones", "Operaciones de cambios y pagos al exterior", "Operaciones en cambios — Compras de bienes en exterior", "Operaciones de cambio, pagos de importaciones", "Exterior y operaciones cambiarias", "Operaciones con el exterior", "Operaciones de cambios — Pagos de importaciones", "Sistema de seguimiento de pagos de importaciones", "Sistema de seguimiento de pagos de importaciones (SEPAIMPO)", "Seguimiento de pagos de importaciones", "Régimen de operaciones en cambios", "Sistema de seguimiento de pagos de importaciones y certificación para acceso al mercado de cambios", "Sistema de seguimiento de pagos de importaciones y operaciones en comercio exterior", "Operaciones de cambios en comercio exterior", "Sistema de seguimiento de pagos de importaciones (SEPAIMPO) — Exterior y Cambios", "Sistema de seguimiento de pagos de importaciones - Certificación para afectación de despacho", "Sistema de seguimiento de pagos de importaciones (SEPAIMPO) — Certificación para afectación del despacho", "Sistema de seguimiento de pagos de importaciones (SEPAIMPO) - Certificación para afectación del despacho a pagos con registro de ingreso aduanero pendiente", "Sistema de seguimiento de pagos de importaciones (SEPAIMPO). Reporte de circunstancias que modifiquen obligaciones con el exterior.", "Sistema de seguimiento de pagos de importaciones y operaciones en mercado de cambios", "Sistema de seguimiento de pagos de importaciones (SEPAIMPO) — Reporte de cambio de entidad a cargo del seguimiento", "Operaciones de cambios. SEPAIMPO", "Pagos de servicios prestados por no residentes", "Operaciones de cambio con el exterior", "Pagos de servicios de no residentes", "Operaciones en cambios — Servicios prestados por no residentes", "Operaciones de cambios, sector exterior", "Pagos de servicios prestados por no residentes y acceso a divisas", "Operaciones de cambios — no residentes", "Operaciones de cambios - exterior", "Régimen de operaciones de cambios", "cambios", "Régimen de Incentivo para Grandes Inversiones - Acceso al mercado de cambios", "Régimen de operaciones de egreso en el mercado de cambios para VPU RIGI", "Régimen de Incentivo para Grandes Inversiones — acceso al mercado de cambios", "Operaciones de cambio - Régimen RIGI", "Cambios — operaciones de egreso para VPU adheridos al RIGI", "Régimen de operaciones de cambios para VPU adheridos al RIGI", "Régimen cambiario", "Régimen de operaciones de egreso en el mercado de cambios — RIGI", "Operaciones de cambios y egresos — RIGI", "Régimen de operaciones en cambios y exterior", "Régimen de Incentivo para Grandes Inversiones (RIGI) - Cambios", "Operaciones de cambio — RIGI", "Régimen de Incentivo para Grandes Inversiones (RIGI) — Disposiciones cambiarias", "Régimen de operaciones de cambio", "Mercado de cambios y operaciones en el exterior", "Disposiciones legales sobre estructura del mercado de cambios"], "version_variantes": ["actual", "", "ext", "vigente"]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "ext", "archivo": "TO_exterior_cambios_actual.pdf", "punto": "11.1.1.4", "rol_documental": "punto_propio", "chunk_id": "ext::11.1.1.4", "paginas": [160, 161], "ancestros": ["S11", "11.1", "11.1.1"]}`
- **Provenances (2):**
  - `{"to": "ext", "archivo": "TO_exterior_cambios_actual.pdf", "punto": "11.1.1.4", "rol_documental": "punto_propio", "chunk_id": "ext::11.1.1.4", "paginas": [160, 161], "ancestros": ["S11", "11.1", "11.1.1"]}`
  - `{"to": "ext", "archivo": "TO_exterior_cambios_actual.pdf", "punto": "11.1.1.7", "rol_documental": "punto_propio", "chunk_id": "ext::11.1.1.7", "paginas": [161], "ancestros": ["S11", "11.1", "11.1.1"]}`
- **Texto del punto ancla** (`ext::11.1.1.4`):

> 11.1.1.4. Emitir a pedido del importador las certificaciones que habilitarán el acceso
> al mercado de cambios para el pago de deudas comerciales de
> importaciones con imputación a oficializaciones de importación bajo su
> seguimiento.
> La entidad deberá verificar, previamente a emitir cada certificación, el
> cumplimiento de los requisitos establecidos a la fecha de emisión de la
> certificación.

- **Herencia (5):**
  - [encabezado] S11 (páginas [160]):

    > Sección 11. Sistema de seguimiento de pagos de importaciones (SEPAIMPO).

  - [encabezado] 11.1 (páginas [160]):

    > 11.1. Seguimiento de oficializaciones de importación.

  - [intro] 11.1 (páginas [160]):

    > Quedarán comprendidas todas las oficializaciones de importación ocurridas a partir del
    > 01/11/19 y aquellas que sean anteriores por las cuales se solicite realizar pagos a través del
    > mercado de cambios a partir de la mencionada fecha.
    > Por cada oficialización del despacho de importación, el importador deberá nominar una
    > entidad para que se haga responsable del seguimiento de la oficialización. Esta entidad será
    > la responsable de verificar el cumplimiento de las condiciones estipuladas en la presente
    > normativa que habilitarán el acceso al mercado de cambios y/o la afectación de una
    > oficialización a la regularización de un pago con registro aduanero pendiente.
    > La entidad será originalmente nominada por el importador ante la ARCA, pudiendo el
    > importador posteriormente modificarla en la medida que, a la fecha de la solicitud de cambio
    > de entidad, no existan certificaciones emitidas de acceso al mercado de cambios que estén
    > pendientes de uso.
    > En caso de que el importador no haya nominado a una entidad al momento de la oficialización
    > podrá posteriormente seleccionar una entidad que se haga cargo del seguimiento.
    > Serán elegibles para el importador, quedando obligadas a llevar a cabo las responsabilidades
    > asociadas al presente seguimiento, todas las entidades financieras y casas de cambio salvo
    > aquellas que hayan notificado al BCRA que han optado por no operar en comercio exterior.

  - [encabezado] 11.1.1 (páginas [160]):

    > 11.1.1. Responsabilidades de la entidad nominada.

  - [intro] 11.1.1 (páginas [160]):

    > La entidad nominada por el importador para el seguimiento de la oficialización del
    > despacho de importación será la responsable de:

---

## 13 · índice 4162 · `aplica_a`

- **Origen:** `Obligacion_la_entidad_podra_considerar_rectificada_la_informacion_cuando_ella_se_refleje_en_980b6c` · tipo `Obligacion` · label «Consideración de rectificación de información»
  - propiedades: `{"descripcion": "La entidad podrá considerar rectificada la información cuando ella se refleje en el SECOEXPO o cuando la entidad disponga de documentación emitida por la ARCA en la cual se indique expresamente que dicho organismo considera válidos los datos indicados por el exportador en su pedido de rectificación.", "tipo": "otra"}`
- **Relación:** `aplica_a`
- **Destino:** `Sujeto_rol_entidad_autorizada_exterior` · tipo `Sujeto` · label «Entidades autorizadas a operar en cambios (Exterior)»
  - propiedades: `{"nivel": "rol", "cola_humana": "true", "cola_chunks": ["ext::10.10.2.3", "ext::10.3.2.5", "ext::10.3.3", "ext::10.3.5::intro", "ext::10.4.3::intro", "ext::10.5.5.2", "ext::10.9.4", "ext::13.2.7::intro", "ext::13.3.3", "ext::13.3.9", "ext::13.4.8", "ext::14.2.1.10", "ext::14.2.1::intro", "ext::14.5.3", "ext::3.11.2.1", "ext::3.11.3::cierre", "ext::3.14.5.5", "ext::3.16.2.1", "ext::3.17.5", "ext::3.18.1::cierre", "ext::3.3.3.4", "ext::3.5.1.12", "ext::3.5.1.9", "ext::3.5.6.10", "ext::3.5::intro", "ext::3.9::intro", "ext::4.4.2", "ext::4.8.1.1", "ext::4.8.1.2", "ext::4.8.1.3", "ext::4.8.1.5", "ext::7.10.6", "ext::7.11.2::cierre", "ext::7.11.3::intro", "ext::7.3::intro", "ext::7.5.7.1", "ext::7.6.1.1", "ext::7.9.1.4", "ext::7.9.3::intersticial", "ext::9.3.2", "ext::9.3.3.1", "ext::9.3.7"], "estado_e3": "cola_humana; cola_humana_veredicto_inutilizable"}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "ext", "archivo": "TO_exterior_cambios_actual.pdf", "punto": "8.3", "rol_documental": "punto_propio", "chunk_id": "ext::8.3", "paginas": [108, 109], "ancestros": ["S8"]}`
- **Provenances (1):**
  - `{"to": "ext", "archivo": "TO_exterior_cambios_actual.pdf", "punto": "8.3", "rol_documental": "punto_propio", "chunk_id": "ext::8.3", "paginas": [108, 109], "ancestros": ["S8"]}`
- **Texto del punto ancla** (`ext::8.3`):

> 8.3. Información de las destinaciones de exportación a disposición de las entidades.
> El sistema SECOEXPO dispuesto por el BCRA permitirá que la entidad tome conocimiento de
> los permisos de embarque para los cuales ha sido designada por un exportador.
> A través de dicho sistema, las entidades tendrán acceso a la información disponible en ARCA
> que resulte pertinente a los efectos de cumplimentar sus responsabilidades como entidad
> nominada para el seguimiento de un permiso de embarque.
> Si el exportador considera que existen errores en la forma en que un permiso de embarque ha
> sido reportado en el sistema SECOEXPO, deberá tramitar la correspondiente rectificación
> directamente ante la ARCA.
> La entidad podrá considerar rectificada la información cuando ella se refleje en el SECOEXPO
> o cuando la entidad disponga de documentación emitida por la ARCA en la cual se indique
> expresamente que dicho organismo considera válidos los datos indicados por el exportador en
> su pedido de rectificación.

- **Herencia (1):**
  - [encabezado] S8 (páginas [108]):

    > Sección 8. Seguimiento de las negociaciones de divisas por exportaciones de bienes

---

## 14 · índice 4792 · `condiciona`

- **Origen:** `Obligacion_las_entidades_deberan_realizar_el_correspondiente_boleto_de_venta_dejando_consta_a0e1fe` · tipo `Obligacion` · label «Realizar boleto de venta — pago fletes importación»
  - propiedades: `{"descripcion": "Las entidades deberán realizar el correspondiente boleto de venta dejando constancia del pago de tales fletes cuando existan fondos de operaciones contempladas en los puntos 7.11.1.2. a 7.11.1.6. destinados al pago directo al proveedor de servicios de fletes de importaciones de bienes no incluidos en condición de compra pactada", "tipo": "otra"}`
- **Relación:** `condiciona`
- **Destino:** `Operacion_pago_directo_fletes_importacion_boleto_de_venta_45d018` · tipo `Operacion` · label «Pago directo fletes importación — boleto de venta»
  - propiedades: `{"tipo": "emisión de boleto de venta para pago de fletes de importación"}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "ext", "archivo": "TO_exterior_cambios_actual.pdf", "punto": "7.11.3", "rol_documental": "bloque_cierre", "chunk_id": "ext::7.11.3::cierre", "paginas": [107], "ancestros": ["S7", "7.11"]}`
- **Provenances (1):**
  - `{"to": "ext", "archivo": "TO_exterior_cambios_actual.pdf", "punto": "7.11.3", "rol_documental": "bloque_cierre", "chunk_id": "ext::7.11.3::cierre", "paginas": [107], "ancestros": ["S7", "7.11"]}`
- **Texto del punto ancla** (`ext::7.11.3::cierre`):

> Si existiesen fondos de las operaciones contempladas en los puntos 7.11.1.2. a
> 7.11.1.6. destinados al pago en forma directa al proveedor de servicios de fletes de
> importaciones de bienes no incluidos en su condición de compra pactada, a los
> efectos del registro de la operación ante el BCRA en los términos previstos en el
> presente punto, las entidades deberán realizar el correspondiente boleto de venta
> dejando constancia del pago de tales fletes.

- **Herencia (3):**
  - [encabezado] S7 (páginas [80]):

    > Sección 7. Cobros de exportaciones de bienes.

  - [encabezado] 7.11 (páginas [103]):

    > 7.11. Financiaciones asociadas a importaciones de bienes habilitadas para la aplicación de cobros

  - [encabezado] 7.11.3 (páginas [106]):

    > 7.11.3. La entidad financiera encargada del “Seguimiento de anticipos y otras financiaciones

---

## 15 · índice 5095 · `regula`

- **Origen:** `Obligacion_las_entidades_podran_darle_acceso_al_cliente_para_pagar_el_capital_pendiente_inc_17ee37` · tipo `Obligacion` · label «Acceso al mercado de cambios — pago de capital pendiente»
  - propiedades: `{"descripcion": "Las entidades podrán darle acceso al cliente para pagar el capital pendiente, incluso antes de la fecha de vencimiento", "tipo": "otra"}`
- **Relación:** `regula`
- **Destino:** `Operacion_emision_de_titulos_de_deuda_con_registro_exterior_e4f3e2` · tipo `Operacion` · label «Emisión de títulos de deuda con registro exterior»
  - propiedades: `{"tipo": "emisión de títulos de deuda con registro en el exterior"}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "ext", "archivo": "TO_exterior_cambios_actual.pdf", "punto": "14.2.1", "rol_documental": "herencia_encabezado", "chunks_emisores": ["ext::14.2.1.1", "ext::14.2.1.3", "ext::14.2.1.4", "ext::14.2.1.5"], "chunk_id": "ext::14.2.1.1", "paginas": [176, 177], "ancestros": ["S14", "14.2"]}`
- **Provenances (1):**
  - `{"to": "ext", "archivo": "TO_exterior_cambios_actual.pdf", "punto": "14.2.1", "rol_documental": "herencia_encabezado", "chunks_emisores": ["ext::14.2.1.1", "ext::14.2.1.3", "ext::14.2.1.4", "ext::14.2.1.5"], "chunk_id": "ext::14.2.1.1", "paginas": [176, 177], "ancestros": ["S14", "14.2"]}`
- **Texto del punto ancla** (`ext::14.2.1.1`):

> 14.2.1.1. emisiones de títulos de deuda con registro en el exterior y otros
> endeudamientos financieros con el exterior ingresados y liquidados en el
> mercado de cambios.

- **Herencia (11):**
  - [encabezado] S14 (páginas [175]):

    > Sección 14. Disposiciones complementarias asociadas al Régimen de Incentivo para Grandes Inversiones (RIGI).

  - [chapeau_seccion] S14 (páginas [175]):

    > En esta sección se detallan las disposiciones complementarias en materia cambiaria que, en la
    > medida que las disposiciones generales no resulten más favorables, resultan aplicables a un
    > Vehículo de Proyecto Único (VPU) adherido al Régimen de Incentivo los referidas al “Régimen de
    > Incentivo para Grandes Inversiones” (RIGI) establecido en el Título VII de la Ley 27.742 y
    > reglamentado por el Decreto 749/24 y concordantes.

  - [encabezado] 14.2 (páginas [176]):

    > 14.2. Beneficios relacionados con el acceso al mercado de cambios para operaciones de egreso.

  - [intro] 14.2 (páginas [176]):

    > Adicionalmente lo previsto en la normativa general en materia de egresos por el mercado de
    > cambios, en la medida que se cumplan los restantes requisitos aplicables a cada operación,
    > por aquellas financiaciones o aportes de inversión directa recibidos por el VPU adherido a
    > partir de la vigencia de la Ley 27.742, las entidades podrán también dar acceso en las
    > siguientes situaciones:

  - [encabezado] 14.2.1 (páginas [176]):

    > 14.2.1. En el marco de lo dispuesto en los puntos 3.3., 3.5., 3.6. y 10.3.2., según

  - [intro] 14.2.1 (páginas [176]):

    > corresponda, sin necesidad de contar con la conformidad previa del BCRA si tal
    > requisito estuviese vigente, las entidades podrán darle acceso al cliente para pagar,
    > incluso antes de la fecha de vencimiento, los intereses devengados hasta la fecha
    > de acceso que se encuentren impagos y/o el capital pendiente de:

  - [cierre] 14.2.1 (páginas [177]):

    > En el caso de que la totalidad de los fondos obtenidos por la financiación no pudiese
    > ser computada como ingresada y liquidada en el mercado de cambios, las
    > entidades también podrán dar acceso al VPU adherido, sin necesidad de contar con
    > la conformidad previa del BCRA si tal requisito estuviese vigente, para realizar:

  - [cierre] 14.2.1 (páginas [177]):

    > i) pagos de intereses devengados hasta la fecha de acceso que se encuentren

  - [cierre] 14.2.1 (páginas [177]):

    > impagos y que correspondan a la porción del capital equivalente a la proporción
    > de los fondos recibidos por el VPU por la financiación que puede computarse
    > como ingresada y liquidada por el mercado de cambios.

  - [cierre] 14.2.1 (páginas [177]):

    > ii) pagos por capital adeudado que corresponda a la porción del capital

  - [cierre] 14.2.1 (páginas [177]):

    > equivalente a la proporción de los fondos recibidos por el VPU por la
    > financiación que puede computarse como ingresada y liquidada por el mercado
    > de cambios.

---

## 16 · índice 5131 · `aplica_a`

- **Origen:** `Obligacion_las_entidades_reconoceran_las_diferencias_por_insuficiencia_en_el_calculo_de_las_b4ede5` · tipo `Obligacion` · label «Reconocimiento diferencias insuficiencia con efecto temporal»
  - propiedades: `{"descripcion": "Las entidades reconocerán las diferencias por insuficiencia en el cálculo de las previsiones regulatorias con efecto al cierre del mes siguiente a aquel en que la entidad reciba la notificación a que se refiere el primer párrafo del punto 2.6 de las normas sobre previsiones mínimas", "tipo": "otra", "plazo": "al cierre del mes siguiente a la notificación"}`
- **Relación:** `aplica_a`
- **Destino:** `Sujeto_rol_alcance_capmin` · tipo `Sujeto` · label «Entidades alcanzadas (Capitales Mínimos)»
  - propiedades: `{"nivel": "rol", "cola_humana": "true", "cola_chunks": ["cap::11.3", "cap::2.6.2::cierre", "cap::2.8.2", "cap::3.1.11.1", "cap::4.2.1.1", "cap::5.3.2.3", "cap::6.1.2.1", "cap::6.2.2.6", "cap::6.3.2.2", "cap::6.8.3.2", "cap::7.1.1.1"], "estado_e3": "cola_humana; cola_humana_reextraccion_invalida; cola_humana_veredicto_inutilizable"}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "cap", "archivo": "TO_capitales_minimos_actual.pdf", "punto": "8.4.1.13", "rol_documental": "punto_propio", "chunk_id": "cap::8.4.1.13", "paginas": [165], "ancestros": ["S8", "8.4", "8.4.1"]}`
- **Provenances (1):**
  - `{"to": "cap", "archivo": "TO_capitales_minimos_actual.pdf", "punto": "8.4.1.13", "rol_documental": "punto_propio", "chunk_id": "cap::8.4.1.13", "paginas": [165], "ancestros": ["S8", "8.4", "8.4.1"]}`
- **Texto del punto ancla** (`cap::8.4.1.13`):

> 8.4.1.13. Diferencias por insuficiencia en el cálculo de las previsiones regulatorias
> conforme las normas sobre “Previsiones mínimas por riesgo de incobrabilidad”
> determinadas por la SEFyC, con efecto al cierre del mes siguiente a aquel en
> que la entidad reciba la notificación a que se refiere el primer párrafo del punto
> 2.6. de las citadas normas.

- **Herencia (4):**
  - [encabezado] S8 (páginas [154]):

    > Sección 8. Responsabilidad patrimonial computable.

  - [encabezado] 8.4 (páginas [162]):

    > 8.4. Conceptos deducibles.

  - [encabezado] 8.4.1 (páginas [162]):

    > 8.4.1. Conceptos deducibles del capital ordinario de nivel uno (CD ).

  - [intro] 8.4.1 (páginas [162]):

    > COn1

---

## 17 · índice 5754 · `aplica_a`

- **Origen:** `Obligacion_los_sujetos_obligados_deberan_adoptar_las_acciones_necesarias_para_garantizar_es_03c5c2` · tipo `Obligacion` · label «Adoptar acciones para garantizar derechos básicos»
  - propiedades: `{"descripcion": "Los sujetos obligados deberán adoptar las acciones necesarias para garantizar estos derechos a todos los actuales y potenciales usuarios de los servicios que ofrecen y prestan, de manera de asegurarles condiciones igualitarias de acceso a tales servicios.", "tipo": "otra"}`
- **Relación:** `aplica_a`
- **Destino:** `Sujeto_rol_sujeto_obligado_proteccion` · tipo `Sujeto` · label «Sujetos obligados (Protección de usuarios)»
  - propiedades: `{"nivel": "rol", "cola_humana": "true", "cola_chunks": ["pro::4.2.1.6"], "estado_e3": "cola_humana"}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "pro", "archivo": "TO_proteccion_usuarios_servicios_financieros_actual.pdf", "punto": "2.1", "rol_documental": "punto_propio", "chunk_id": "pro::2.1", "paginas": [5], "ancestros": ["S2"]}`
- **Provenances (1):**
  - `{"to": "pro", "archivo": "TO_proteccion_usuarios_servicios_financieros_actual.pdf", "punto": "2.1", "rol_documental": "punto_propio", "chunk_id": "pro::2.1", "paginas": [5], "ancestros": ["S2"]}`
- **Texto del punto ancla** (`pro::2.1`):

> 2.1. Concepto.
> Los usuarios de servicios financieros tienen derecho, en toda relación de consumo, a:
> − la protección de su seguridad e intereses económicos;
> − recibir información clara, suficiente, veraz y de fácil acceso y visibilidad acerca de los pro-
> ductos y/o servicios que contraten –incluyendo sus términos y condiciones–, así como co-
> pia de los instrumentos que suscriban;
> − la libertad de elección; y
> − condiciones de trato equitativo y digno.
> Los sujetos obligados deberán adoptar las acciones necesarias para garantizar estos dere-
> chos a todos los actuales y potenciales usuarios de los servicios que ofrecen y prestan, de
> manera de asegurarles condiciones igualitarias de acceso a tales servicios.

- **Herencia (1):**
  - [encabezado] S2 (páginas [5]):

    > Sección 2. Derechos básicos de los usuarios de servicios financieros.

---

## 18 · índice 5920 · `aplica_a`

- **Origen:** `Obligacion_para_determinar_el_importe_de_la_posicion_abierta_neta_en_cada_moneda_extranjera_61ffc1` · tipo `Obligacion` · label «Exclusión de posiciones deducibles — cálculo neto»
  - propiedades: `{"descripcion": "Para determinar el importe de la posición abierta neta en cada moneda extranjera las entidades podrán excluir las posiciones comprendidas en las partidas deducibles para determinar la responsabilidad patrimonial computable", "tipo": "calculo"}`
- **Relación:** `aplica_a`
- **Destino:** `Sujeto_rol_alcance_capmin` · tipo `Sujeto` · label «Entidades alcanzadas (Capitales Mínimos)»
  - propiedades: `{"nivel": "rol", "cola_humana": "true", "cola_chunks": ["cap::11.3", "cap::2.6.2::cierre", "cap::2.8.2", "cap::3.1.11.1", "cap::4.2.1.1", "cap::5.3.2.3", "cap::6.1.2.1", "cap::6.2.2.6", "cap::6.3.2.2", "cap::6.8.3.2", "cap::7.1.1.1"], "estado_e3": "cola_humana; cola_humana_reextraccion_invalida; cola_humana_veredicto_inutilizable"}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "cap", "archivo": "TO_capitales_minimos_actual.pdf", "punto": "6.4.2.4", "rol_documental": "punto_propio", "chunk_id": "cap::6.4.2.4", "paginas": [132], "ancestros": ["S6", "6.4", "6.4.2"]}`
- **Provenances (1):**
  - `{"to": "cap", "archivo": "TO_capitales_minimos_actual.pdf", "punto": "6.4.2.4", "rol_documental": "punto_propio", "chunk_id": "cap::6.4.2.4", "paginas": [132], "ancestros": ["S6", "6.4", "6.4.2"]}`
- **Texto del punto ancla** (`cap::6.4.2.4`):

> 6.4.2.4. Las posiciones a término en moneda extranjera y en oro se valuarán a los tipos
> de cambio de contado corrientes en el mercado, salvo que la entidad emplee
> para la gestión de dichas posiciones el valor actual neto, en cuyo caso se utili-
> zarán las tasas de interés y los tipos de cambio de contado corrientes.
> Para determinar el importe de la posición abierta neta en cada moneda extran-
> jera las entidades podrán excluir las posiciones comprendidas en las partidas
> deducibles para determinar la responsabilidad patrimonial computable.

- **Herencia (4):**
  - [encabezado] S6 (páginas [116]):

    > Sección 6. Capital mínimo por riesgo de mercado.

  - [encabezado] 6.4 (páginas [131]):

    > 6.4. Exigencia de capital por riesgo de tipo de cambio.

  - [intro] 6.4 (páginas [131]):

    > El presente punto establece el capital mínimo necesario para cubrir el riesgo de mantener po-
    > siciones en moneda extranjera, incluido el oro.

  - [encabezado] 6.4.2 (páginas [131]):

    > 6.4.2. Medición de la exposición en cada moneda.

---

## 19 · índice 6626 · `establecida_en`

- **Origen:** `Obligacion_se_podra_contar_con_la_refinanciacion_o_venta_de_los_subyacentes_siempre_que_las_ffb75a` · tipo `Obligacion` · label «Refinanciación — subyacentes distribuidos»
  - propiedades: `{"descripcion": "Se podrá contar con la refinanciación o venta de los subyacentes siempre que las operaciones a refinanciar estén suficientemente distribuidas en el conjunto de los activos titulizados y que sus valores residuales no sean significativos.", "tipo": "otra"}`
- **Relación:** `establecida_en`
- **Destino:** `TextoOrdenado_to_capitales_minimos_actual_pdf` · tipo `TextoOrdenado` · label «Texto Ordenado Capitales Mínimos»
  - propiedades: `{"materia": "Capitales Mínimos", "archivo": "TO_capitales_minimos_actual.pdf", "version": "", "descripcion": "Cámara de compensación que interviene entre las partes de un contrato financiero negociado en uno o más mercados, actuando como comprador para todo vendedor y como vendedor para todo comprador, garantizando la ejecución futura de los contratos. La CCP se convierte en contraparte mediante novación, sistema de ofertas abiertas u otro esquema con fuerza legal.", "tipo": "definicion", "cola_humana": "true", "cola_chunks": ["cap::11.3", "cap::2.6.2::cierre", "cap::2.8.2", "cap::3.1.1.4", "cap::3.1.1.7", "cap::3.1.11.1", "cap::4.2.1.1", "cap::4.3.1.3", "cap::5.3.2.3", "cap::6.1.2.1", "cap::6.1.2.2", "cap::6.2.2.6", "cap::6.3.2.2", "cap::6.8.3.2", "cap::7.1.1.1"], "estado_e3": "cola_humana; cola_humana_reextraccion_invalida; cola_humana_veredicto_inutilizable", "materia_variantes": ["Capitales Mínimos", "Capitales mínimos", "capitales_minimos", "Capitales mínimos por riesgo de crédito", "Sector público no financiero", "Capital mínimo por riesgo de crédito", "Evaluaciones crediticias", "Capital mínimo", "Determinación de activos ponderados por riesgo de crédito", "capitales mínimos", "capital minimo", "capital_minimo_riesgo_credito", "exposiciones_minoristas", "capital mínimo por riesgo de crédito", "capitales minimos", "Capital mínimo por riesgo de crédito — Tabla de ponderadores de riesgo", "Capital mínimo por riesgo de crédito. Titulizaciones e inversiones en fondos", "Capital mínimo por riesgo de crédito. Titulizaciones", "Tratamiento de titulizaciones e inversiones en fondos", "Capital mínimo por riesgo de crédito de contraparte", "Definición de fondos de garantía (default funds) constituidos para absorción mutualizada de pérdidas", "Definición de estructura multinivel de clientes", "Requisitos de capital", "Aforos regulatorios — Cobertura del riesgo de crédito", "Cobertura del riesgo de crédito — Operaciones de financiación con títulos valores", "Método de Medición Estándar", "Capital mínimo por riesgo de mercado", "Capital mínimo por riesgo de mercado / riesgo específico", "Exigencia de capital por riesgo de mercado", "capital_minimo", "capital mínimo por riesgo de mercado", "capital mínimo", "Capital mínimo, riesgo de mercado, políticas y procedimientos", "capital", "Capital mínimo regulatorio", "Capital mínimo por riesgo operacional", "Responsabilidad patrimonial computable"], "version_variantes": ["", "actual", "vigente"]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "cap", "archivo": "TO_capitales_minimos_actual.pdf", "punto": "3.1.14.1", "rol_documental": "punto_propio", "chunk_id": "cap::3.1.14.1", "paginas": [48, 49, 50, 51, 52, 53], "ancestros": ["S3", "3.1", "3.1.14"]}`
- **Provenances (1):**
  - `{"to": "cap", "archivo": "TO_capitales_minimos_actual.pdf", "punto": "3.1.14.1", "rol_documental": "punto_propio", "chunk_id": "cap::3.1.14.1", "paginas": [48, 49, 50, 51, 52, 53], "ancestros": ["S3", "3.1", "3.1.14"]}`
- **Texto del punto ancla** (`cap::3.1.14.1`):

> 3.1.14.1. Riesgo de los activos subyacentes.
> i) Naturaleza de los activos.
> Los activos subyacentes deberán estar constituidos por documentos a
> cobrar o derechos de crédito de carácter homogéneo en cuanto a su tipo,
> jurisdicción, legislación aplicable y moneda y sus flujos de fondos deberán
> estar contractualmente identificados, ser periódicos y consistir exclusiva-
> mente en pagos del principal e intereses o de arrendamientos financieros.
> La homogeneidad de los activos subyacentes deberá evaluarse teniendo
> en consideración los siguientes principios:
> a) La naturaleza de los activos deberá ser tal que los inversores, al reali-
> zar el proceso de debida diligencia, no necesiten analizar ni evaluar
> perfiles o factores de riesgo, crediticios o legales, sustancialmente dife-
> rentes entre sí.
> b) La homogeneidad se deberá evaluar en función de factores y perfiles
> de riesgo comunes al conjunto de los activos.
> c) Los documentos y créditos incluidos en la titulización deberán constituir
> obligaciones estándares, en términos de derechos de cobro y/o rentas
> de los activos y generar un flujo de pago a los inversores periódico y
> claramente definido –tal como el flujo que generan las facilidades que
> proveen las tarjetas de crédito–.
> d) El reembolso a los inversores en la titulización deberá provenir princi-
> palmente del producido de los activos subyacentes y no deberá de-
> pender de modo sustancial de la refinanciación de los créditos. Se po-
> drá contar con la refinanciación o venta de los subyacentes siempre
> que las operaciones a refinanciar estén suficientemente distribuidas en
> el conjunto de los activos titulizados y que sus valores residuales no
> sean significativos.
> Las tasas de interés o de descuento de referencia deberán ser tasas de
> interés de mercado y de fácil consulta –tales como tasas interbancarias o
> tasas establecidas por el BCRA y tasas sectoriales que reflejen el costo
> del fondeo de las entidades financieras–, evitándose referencias a fórmu-
> las complejas o derivados exóticos. Los límites máximos y mínimos esta-
> blecidos sobre las tasas de interés no serán considerados necesariamen-
> te como derivados exóticos.
> ii) Historia de desempeño de los activos.
> Se deberá contar con información verificable sobre pérdidas e incumpli-
> mientos respecto de activos con características de riesgo sustancialmente
> similares a los que integran la titulización y por un período de tiempo lo
> suficientemente prolongado. Ello a los efectos de proveer al inversor de
> información respecto de las distintas categorías de activos, así como de
> datos que le permitan realizar un cálculo preciso de las pérdidas espera-
> das bajo distintos escenarios de estrés, para que pueda llevar a cabo un
> adecuado proceso de debida diligencia.
> Las fuentes de información y el acceso a los datos, así como los funda-
> mentos que permitan aducir la similitud con los activos titulizados, debe-
> rán estar disponibles para todos los participantes del mercado.
> El inversor, además, deberán poder evaluar –durante su proceso de debi-
> da diligencia– si el originante, fiduciario, administrador, agente de cobro u
> otros sujetos con responsabilidad fiduciaria en la titulización cuentan con
> probados antecedentes, reunidos a lo largo de un período suficientemente
> largo, respecto de activos sustancialmente similares a aquellos que son
> objeto de titulización. Esta consideración no será condición para dar cum-
> plimiento con el presente criterio.
> El originante de la titulización, así como el acreedor inicial de los créditos
> titulizados, deberán contar con experiencia suficiente en el otorgamiento
> de financiaciones similares a las titulizadas.
> El inversor deberá determinar la experiencia y el historial de desempeño
> del originante y del acreedor inicial respecto de activos sustancialmente
> similares a los titulizados a través de un período convenientemente
> prolongado. El desempeño se deberá verificar durante un período mínimo
> de 5 años en el caso de las exposiciones minoristas que se ajusten a la
> definición prevista en el punto 2.8.1. –sin considerar las exclusiones allí
> previstas– y que cumplan con el criterio previsto en el punto 2.8.3.1. Para
> el resto de las exposiciones, el desempeño deberá verificarse durante 7
> años. Ello para evitar, por ejemplo, que se originen carteras con el solo fin
> de transferirlas.
> iii) Estado de cumplimiento de los activos.
> A fin de asegurar que sólo se asignen a una titulización documentos a co-
> brar o derechos de crédito que no estén en mora, no se podrán transferir
> activos en situación de incumplimiento o mora u obligaciones respecto de
> las cuales el originante o el fiduciario o los demás participantes de la tituli-
> zación con responsabilidad fiduciaria cuenten con evidencia de un incre-
> mento sustancial en las pérdidas esperadas o que se encuentran en ges-
> tión de cobranza.
> El originante o fiduciario deberá verificar que los activos cumplan con las
> siguientes condiciones:
> a) El obligado al pago no ha sido sometido a un proceso de quiebra o de
> reestructuración de deuda debido a dificultades financieras en los 3
> años previos a la fecha de originación, salvo que resulte de aplicación
> el período de 2 años previsto en el art. 26, inciso 4, de la Ley 25.326.
> b) El obligado al pago no cuenta con un historial de crédito desfavorable
> en algún registro público de crédito.
> c) El obligado al pago no cuenta con una evaluación de una agencia de
> calificación de créditos o un credit scoring que anticipen un riesgo de
> incumplimiento significativo.
> d) El documento a cobrar o derecho de crédito transferido no es objeto de
> litigios entre el obligado y el acreedor original.
> El análisis de estas condiciones deberá ser llevado a cabo por el originan-
> te o fiduciario dentro de los 45 días previos a la fecha de la transferencia
> de los activos. Al momento de la evaluación, no deberá existir evidencia
> que indique la posibilidad de deterioro en el estado de cumplimiento de
> los activos.
> Adicionalmente, al momento de la inclusión del activo en la cartera de
> subyacentes, deberá haberse registrado al menos un pago, excepto en el
> caso de las estructuras sobre activos de tipo rotativos (como tarjetas de
> crédito, facturas y otras exposiciones cancelables en un solo pago).
> iv)Consistencia en la originación de los activos.
> El originante deberá demostrar al inversor que los activos transferidos han
> sido generados en el curso normal de su negocio bajo estándares de ori-
> ginación uniformes y consistentes.
> Cuando esos estándares se vean afectados por cambios, el originante
> deberá comunicar el momento y el propósito de las modificaciones. Los
> estándares no deberán ser menos rigurosos que aquellos aplicados a los
> activos retenidos por el originante.
> Los documentos a cobrar o derechos de crédito titulizados –incluso cuan-
> do formen parte de carteras atomizadas– deberán satisfacer criterios de
> originación sólidos y prudentes que incluyan una evaluación de la capaci-
> dad e intención de los obligados de cumplir puntualmente con sus obliga-
> ciones. Además, en el caso de carteras atomizadas, tales documentos o
> derechos deberán ser originados en el curso normal del negocio del origi-
> nante y sus flujos de fondos esperados deberán permitir atender las obli-
> gaciones establecidas en la titulización aun en escenarios de estrés sufi-
> cientemente conservadores respecto de las pérdidas crediticias.
> Cuando los activos hayan sido adquiridos a terceros, el originan-
> te/fiduciario de la titulización deberá revisar los estándares de originación
> de esos terceros –verificando su existencia y calidad– y constatar que el
> acreedor original ha examinado y evaluado la habilidad y voluntad de los
> obligados de hacer los respectivos pagos de manera puntual.
> v) Selección y transferencia de los activos.
> El desempeño de la titulización no deberá depender de una selección de
> los subyacentes a través de la gestión activa y discrecional de la cartera.
> Por el contrario, la selección de los activos deberá estar sujeta a criterios
> de elegibilidad claramente definidos, tales como el tamaño de la obliga-
> ción, la edad del sujeto de crédito y los ratios “loan-to-value” (LTV), “debt-
> to-income” (DTI) y/o “debt service coverage” (DSC).
> En la medida en que la selección no sea discrecional, la incorporación de
> créditos en los períodos de rotación o su sustitución o recompra debido al
> incumplimiento de cláusulas contractuales no se considerará una gestión
> activa de la cartera.
> Los documentos a cobrar y créditos transferidos luego de la fecha en que
> se concreta la titulización tampoco deberán ser seleccionados de manera
> discrecional ni gestionados de forma activa. Los inversores deberían po-
> der evaluar el riesgo crediticio de la cartera de activos en forma previa a
> sus decisiones de inversión.
> A efectos de cumplir con el principio de transferencia real, deberá reali-
> zarse una cesión efectiva de derechos de forma tal que los documentos a
> cobrar y derechos de crédito:
> a) constituyan una deuda de los respectivos obligados y ello conste en las
> cláusulas de la titulización;
> b) estén fuera del alcance del cedente, sus acreedores o liquidadores y
> no estén sujetos a riesgos de modificación sustancial de los contratos
> o restitución de los activos;
> c) hayan sido objeto de una cesión de créditos; es decir, que la transfe-
> rencia del riesgo de crédito no se haya efectuado mediante un CDS,
> derivado o garantía (titulización sintética); y
> d) proporcionen un efectivo derecho contra el último obligado y no consti-
> tuyan una titulización de otras titulizaciones; es decir, que no se trate
> de retitulizaciones.
> El contrato de cesión de los créditos deberá contener cláusulas por las
> cuales el originante garantice que los documentos a cobrar o los créditos
> que están siendo transferidos para su titulización no están afectados en
> garantía ni sujetos a ninguna otra condición o gravamen que, hasta donde
> se pueda prever, afecten el cobro de las sumas pendientes.
> La documentación que instrumente la titulización deberá incluir una opi-
> nión legal independiente que respalde que la transferencia real y la cesión
> de derechos bajo la legislación aplicable se ajustan a lo indicado en los
> apartados a) a d) anteriores.
> En el caso de que la legislación aplicable a la titulización no se ajuste a lo
> previsto en los apartados a) a d) precedentes, se deberá demostrar la
> existencia de los obstáculos que así lo impiden y especificar el método del
> que disponen los inversores para ejercer sus derechos contra los obliga-
> dos al pago. Además, de corresponder, deberá informarse toda condición
> o evento que pueda retrasar o impedir la transferencia de los activos sub-
> yacentes a la titulización así como cualquier factor que pueda afectar el
> perfeccionamiento oportuno de los reclamos.
> vi) Información inicial y periódica.
> A fin de asistir a los inversores en la realización de un apropiado proceso
> de debida diligencia en forma previa a la inversión en un nuevo
> instrumento, se deberá contar con suficiente información a nivel de cada
> préstamo o, en el caso de carteras atomizadas, con datos sobre las
> características de riesgo relevantes resumidas a nivel de cada tramo de
> activos subyacentes.
> Para asistir a los inversores en el seguimiento permanente del desempe-
> ño de sus inversiones y para que aquellos inversores que deseen adquirir
> una titulización en el mercado secundario tengan información suficiente
> para realizar una correcta evaluación de la inversión, se deberá suminis-
> trar al menos trimestralmente durante la vida de la titulización datos a ni-
> vel de préstamos en función de las regulaciones aplicables o, en el caso
> de las carteras atomizadas, datos resumidos a nivel de cada tramo de ac-
> tivos subyacentes, así como también informes estandarizados dirigidos al
> inversor. Las fechas de corte de los datos deberán estar en línea con las
> utilizadas para la emisión de los informes.
> A efectos de generar confianza respecto tanto de la exactitud de lo infor-
> mado sobre los activos subyacentes como de que estos activos cumplen
> con los requisitos de elegibilidad –acápite v) precedente–, la cartera inicial
> deberá ser revisada por un contador público independiente.

- **Herencia (9):**
  - [encabezado] S3 (páginas [29]):

    > Sección 3. Capital mínimo por riesgo de crédito. Titulizaciones e inversiones en fon- dos.

  - [encabezado] 3.1 (páginas [29]):

    > 3.1. Tratamiento de las titulizaciones.

  - [intro] 3.1 (páginas [29]):

    > Se denomina “posición de titulización” a la exposición a una titulización (o retitulización), tradi-
    > cional o sintética, o a una estructura con similares características.
    > La exposición a los riesgos de una titulización puede surgir, entre otros, de los siguientes con-
    > ceptos: tenencia de títulos valores emitidos en el marco de la titulización –es decir, títulos de
    > deuda y/o certificados de participación, tales como bonos de titulización de activos (“Asset-
    > Backed Securities”, ABS) y bonos de titulización hipotecaria (“Mortgage-Backed Securities”,
    > MBS)–, mejoras crediticias, facilidades de liquidez, “swaps” de tasa de interés o de monedas y
    > derivados de crédito. Las reservas (“reserve accounts”), tales como las cuentas de garantía en
    > efectivo, se considerarán como un activo para la entidad financiera originante, recibiendo tam-
    > bién el tratamiento de posiciones de titulización.
    > Dado que las titulizaciones pueden estructurarse de diferentes formas, la exigencia de capital
    > para una posición de titulización se determinará teniendo en cuenta su realidad o finalidad eco-
    > nómica y no su forma jurídica. En los casos en que exista incertidumbre acerca de si una de-
    > terminada operación debe considerarse como titulización, la entidad deberá aplicar el criterio
    > que estime mejor se ajusta a la realidad económica de la operación e informar a la SEFyC los
    > fundamentos que lo sustenten.

  - [encabezado] 3.1.14 (páginas [47]):

    > 3.1.14. Criterios para la determinación de titulizaciones simples, transparentes y comparables.

  - [intro] 3.1.14 (páginas [47]):

    > A los fines de establecer el ponderador de riesgo a aplicar de acuerdo con el enfoque
    > estandarizado –punto 3.1.11.–, una titulización se considerará simple, transparente y
    > comparable (STC) si:
    > -se trata de una titulización tradicional que no constituye un programa ABCP;
    > - involucra una transferencia real de activos –en los términos del acápite v) del punto

  - [intro] 3.1.14 (páginas [47]):

    > 3.1.14.1.–; y

  - [intro] 3.1.14 (páginas [48]):

    > - cumple con la totalidad de los criterios previstos en el presente punto (en adelante,

  - [intro] 3.1.14 (páginas [48]):

    > “criterios STC”).

  - [intro] 3.1.14 (páginas [48]):

    > El originante/fiduciario deberá divulgar toda la información necesaria respecto de la
    > transacción que permita a los inversores determinar si la titulización cumple con los cri-
    > terios STC. En base a la información provista, el inversor deberá realizar sus propias
    > evaluaciones respecto del cumplimiento de estos criterios previo a la aplicación del en-
    > foque estandarizado.
    > Para las posiciones retenidas en las que el originante haya transferido el riesgo de
    > acuerdo con lo establecido en los puntos 3.1.2.2. y 3.1.8.2. la determinación respecto
    > del cumplimiento de los criterios será efectuada únicamente por la entidad originante.
    > Los criterios STC deberán cumplirse en todo momento. Algunos de los criterios se de-
    > berán verificar sólo al momento de la originación o cuando se genere la posición –si és-
    > ta es posterior–, tal como en el caso de las garantías y las facilidades de liquidez. No
    > obstante, los inversores y tenedores de las posiciones de titulización deberán tener en
    > cuenta las modificaciones que puedan invalidar las evaluaciones de cumplimiento pre-
    > vias, tales como las deficiencias en la frecuencia y en el contenido de los informes a los
    > inversores o los cambios en la documentación contrarios a los criterios STC.
    > En los casos en que los criterios hagan referencia a activos subyacentes –incluidos los
    > criterios previstos en el punto 3.1.14.4.– y el conjunto de subyacentes admita la incorpo-
    > ración de nuevos activos, el cumplimiento estará sujeto a que se realicen verificaciones
    > cada vez que se incorporen esos nuevos activos.
    > Cuando la SEFyC detecte que una titulización no cumple con alguno de los criterios,
    > podrá exigir la implementación de acciones correctivas y/o determinar que se suspenda
    > el tratamiento STC para una o más posiciones de titulización.

---

## 20 · índice 7628 · `establecida_en`

- **Origen:** `Operacion_generacion_impropia_de_cargos_e_intereses_compensatorios_c8910b` · tipo `Operacion` · label «Generación impropia de cargos e intereses compensatorios»
  - propiedades: `{"tipo": "cobro de intereses compensatorios por saldos deudores en cuentas de depósito distintas de cuenta corriente bancaria y otros cargos generados en forma impropia"}`
- **Relación:** `establecida_en`
- **Destino:** `TextoOrdenado_to_proteccion_usuarios_servicios_financieros_actual_pdf` · tipo `TextoOrdenado` · label «Protección de usuarios servicios financieros»
  - propiedades: `{"materia": "protección de usuarios de servicios financieros", "archivo": "TO_proteccion_usuarios_servicios_financieros_actual.pdf", "version": "actual", "descripcion": "Son aquellas personas que se desplazan con dificultad –requieran o no de ayuda técnica para ambular– o que por cualquier otra limitación física revelen impedimentos para permanecer de pie y/o acceder de la manera usual a las casas operativas. Se consideran comprendidas en este segmento a las mujeres embarazadas o personas que cargan en brazos niños de hasta dos años", "cola_humana": "true", "cola_chunks": ["pro::1.1.2.3", "pro::4.2.1.6"], "estado_e3": "cola_humana", "materia_variantes": ["protección de usuarios de servicios financieros", "Protección de Usuarios de Servicios Financieros", "Protección de usuarios", "Protección de usuarios de servicios financieros", "protección de usuarios", "Derechos básicos de usuarios — Casos especiales — Personas con dificultades visuales", "Derechos básicos de usuarios de servicios financieros", "Derechos básicos de los usuarios de servicios financieros", "proteccion de usuarios de servicios financieros"], "version_variantes": ["actual", ""]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "pro", "archivo": "TO_proteccion_usuarios_servicios_financieros_actual.pdf", "punto": "2.3.5.1", "rol_documental": "punto_propio", "chunk_id": "pro::2.3.5.1", "paginas": [15, 16], "ancestros": ["S2", "2.3", "2.3.5"]}`
- **Provenances (1):**
  - `{"to": "pro", "archivo": "TO_proteccion_usuarios_servicios_financieros_actual.pdf", "punto": "2.3.5.1", "rol_documental": "punto_propio", "chunk_id": "pro::2.3.5.1", "paginas": [15, 16], "ancestros": ["S2", "2.3", "2.3.5"]}`
- **Texto del punto ancla** (`pro::2.3.5.1`):

> 2.3.5.1. Todo importe cobrado o adeudado de cualquier forma al usuario de servicios fi-
> nancieros por los siguientes conceptos:
> i) tasas de interés, comisiones y/o cargos sin el cumplimiento de lo previsto
> en los puntos 2.3.2. a 2.3.4.;
> ii) cargos en exceso de los costos de los servicios que terceros les cobraron a
> los sujetos obligados en relación con servicios prestados a los usuarios y/o
> de los precios que el tercero prestador perciba de particulares en general;
> iii) comisiones en exceso de las máximas fijadas por el BCRA que sean de
> aplicación;
> iv) en incumplimiento al nivel de la tasa de interés máxima aplicable a finan-
> ciaciones vinculadas a tarjetas de crédito previstas en el texto ordenado
> sobre Tasas de Interés en las Operaciones de Crédito;
> v) en exceso de lo oportunamente pactado entre el usuario y el sujeto obliga-
> do;
> vi) otros generados en forma impropia por su naturaleza, tales como intereses
> compensatorios por saldos deudores generados en cuentas de depósito
> distintas de la cuenta corriente bancaria;
> vii) así como los importes adeudados al usuario por haber liquidado en forma
> incorrecta promociones, descuentos u otro tipo de beneficios –es decir, que
> no se ajustan a los términos, condiciones y/o modalidades que hubieran
> sido ofrecidos, publicitados o convenidos–;
> deberá serle reintegrado dentro de:
> - los diez (10) días hábiles siguientes al momento de la presentación del re-
> clamo ante el sujeto obligado, de conformidad con las previsiones del punto
> 3.1.6.; o
> - los cinco (5) días hábiles siguientes al momento de constatarse tal circuns-
> tancia por el sujeto obligado o por la fiscalización que realice la SEFYC.
> Ello, sin perjuicio de las sanciones que pudieran corresponder.
> En tales situaciones, corresponderá reconocer el importe de los gastos que re-
> sulten razonables realizados para la obtención del reintegro y, en todos los ca-
> sos, los intereses compensatorios pertinentes, computados desde la fecha del
> cobro indebido hasta la de su efectiva devolución. A ese efecto, el sujeto obli-
> gado deberá aplicar 1,5 veces la tasa promedio correspondiente al período
> comprendido entre el momento en que la citada diferencia hubiera sido exigible
> –fecha en la que se cobraron los importes objeto del reclamo– y el de su efecti-
> va cancelación, computado a partir de la encuesta diaria de tasas de interés de
> depósitos a plazo fijo de 30 a 59 días –de pesos o dólares estadounidenses,
> según la moneda de la operación– informada por el BCRA sobre la base de la
> información provista por la totalidad de bancos públicos y privados. Cuando la
> tasa correspondiente a tal encuesta no estuviera disponible, se deberá tomar la
> última informada.
> Cuando el usuario posea en la entidad financiera obligada una cuenta a la vista
> que se halle abierta a su nombre, ésta deberá acreditar ese importe en dicha
> cuenta en forma automática sin necesidad de requerimiento expreso. Si ello no
> fuera posible o no se tratare de una entidad financiera, el importe del reintegro
> deberá ser acreditado en una tarjeta de crédito de su titularidad o detraído del
> saldo vigente de la financiación que lo generó.
> Deberá notificarse la acreditación del reintegro o, en su caso, su puesta a dis-
> posición mediante aviso efectuado a través de medios electrónicos
> –cajeros automáticos, banca por Internet (home banking), etc.– y/o servicios te-
> lefónicos –tales como mensajes de texto y/o voz– y:
> a) documento escrito dirigido a su domicilio –en forma separada de cualquier
> otra información que se le remita (resúmenes de cuenta, boletines informa-
> tivos, etc.), aun cuando forme parte de la misma remesa–; o
> b) a su correo electrónico –en aquellos casos en que hubiere expresamente
> aceptado esa forma de notificación–.
> Estas disposiciones serán de aplicación a los efectos de dar cumplimiento a
> acuerdos extrajudiciales homologados, acuerdos homologados por acciones
> colectivas (artículo 54 de la Ley 24.240) o sentencias judiciales, en la medida
> en que no se opongan a lo previsto en esos acuerdos o a lo dispuesto por los
> poderes públicos de las distintas jurisdicciones.
> Adicionalmente, el sujeto obligado deberá verificar si este tipo de situaciones
> que generan la obligación de reintegros ha ocurrido respecto de los usuarios
> que se encuentren en la misma situación y, de corresponder, proceder a su re-
> integro según el procedimiento previsto en este punto, notificando de tal cir-
> cunstancia y resultados a su Responsable de Atención al Usuario de Servicios
> Financieros.

- **Herencia (3):**
  - [encabezado] S2 (páginas [5]):

    > Sección 2. Derechos básicos de los usuarios de servicios financieros.

  - [encabezado] 2.3 (páginas [7]):

    > 2.3. Recaudos mínimos de la relación de consumo.

  - [encabezado] 2.3.5 (páginas [15]):

    > 2.3.5. Reintegro de importes.

---

## 21 · índice 7971 · `establecida_en`

- **Origen:** `Operacion_reclasificacion_de_cliente_tratamiento_especial_24991e` · tipo `Operacion` · label «Reclasificación de cliente — tratamiento especial»
  - propiedades: `{"tipo": "reclasificacion_de_deudor"}`
- **Relación:** `establecida_en`
- **Destino:** `TextoOrdenado_to_clasificacion_deudores_actual_pdf` · tipo `TextoOrdenado` · label «Clasificación de Deudores»
  - propiedades: `{"materia": "clasificación de deudores", "archivo": "TO_clasificacion_deudores_actual.pdf", "version": "actual", "cola_humana": "true", "cola_chunks": ["cla::3.5.1", "cla::3.5::intro", "cla::6.5.3.5"], "estado_e3": "cola_humana", "materia_variantes": ["clasificación de deudores", "Clasificación de deudores", "clasificacion", "clasificacion_deudores", "clasificación", "Clasificación de Deudores", "Clasificación de deudores y previsión", "Clasificación", "Clasificación de deudores y previsiones por riesgo", "Criterios de clasificación de deudores", "Clasificación de deudores de cartera comercial", "Clasificación de deudores de la cartera comercial", "clasificacion_de_deudores", "clasificación de deudores cartera consumo vivienda"], "version_variantes": ["actual", "", "cla", "vigente"]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "cla", "archivo": "TO_clasificacion_deudores_actual.pdf", "punto": "7.2.2.2", "rol_documental": "punto_propio", "chunk_id": "cla::7.2.2.2", "paginas": [36], "ancestros": ["S7", "7.2", "7.2.2"]}`
- **Provenances (1):**
  - `{"to": "cla", "archivo": "TO_clasificacion_deudores_actual.pdf", "punto": "7.2.2.2", "rol_documental": "punto_propio", "chunk_id": "cla::7.2.2.2", "paginas": [36], "ancestros": ["S7", "7.2", "7.2.2"]}`
- **Texto del punto ancla** (`cla::7.2.2.2`):

> 7.2.2.2. En tratamiento especial.
> Para las refinanciaciones otorgadas por primera vez dentro del año calendario y
> una vez que se haya cancelado la primera cuota de dicha refinanciación, el clien-
> te podrá ser reclasificado por única vez en esta situación. Luego de la citada refi-
> nanciación y a los fines de la clasificación, deberá tenerse en cuenta únicamente
> la mora en el atraso de sus obligaciones.
> Para las posteriores refinanciaciones, recibirán el tratamiento general previsto en
> estas disposiciones.

- **Herencia (3):**
  - [encabezado] S7 (páginas [33]):

    > Sección 7. Clasificación de los deudores de la cartera para consumo o vivienda.

  - [encabezado] 7.2 (páginas [35]):

    > 7.2. Niveles de clasificación.

  - [encabezado] 7.2.2 (páginas [35]):

    > 7.2.2. Riesgo bajo.

---

## 22 · índice 8111 · `establecida_en`

- **Origen:** `Operacion_solicitud_de_ampliacion_de_plazo_de_liquidacion_ba5826` · tipo `Operacion` · label «Solicitud de ampliación de plazo de liquidación»
  - propiedades: `{"tipo": "solicitud de ampliación de plazo"}`
- **Relación:** `establecida_en`
- **Destino:** `TextoOrdenado_to_exterior_cambios_actual_pdf` · tipo `TextoOrdenado` · label «Texto Ordenado de Exterior y Cambios»
  - propiedades: `{"materia": "exterior", "archivo": "TO_exterior_cambios_actual.pdf", "version": "actual", "descripcion": "Comprende a la administración central de provincias, de la Ciudad Autónoma de Buenos Aires, y de las municipalidades del país.", "cola_humana": "true", "cola_chunks": ["ext::10.10.2.3", "ext::10.10.2.5", "ext::10.2.4.9", "ext::10.3.2.5", "ext::10.3.3", "ext::10.3.5::intro", "ext::10.4.3::intro", "ext::10.5.5.2", "ext::10.9.4", "ext::13.2.7::intro", "ext::13.3.3", "ext::13.3.9", "ext::13.4.8", "ext::14.2.1.10", "ext::14.2.1.6", "ext::14.2.1.7", "ext::14.2.1::intro", "ext::14.5.3", "ext::3.11.2.1", "ext::3.11.3::cierre", "ext::3.14.2", "ext::3.14.5.5", "ext::3.16.2.1", "ext::3.17.3::intro", "ext::3.17.5", "ext::3.18.1::cierre", "ext::3.3.3.4", "ext::3.4.4::intro", "ext::3.5.1.12", "ext::3.5.1.9", "ext::3.5.3.5", "ext::3.5.6.10", "ext::3.5::intro", "ext::3.9::intro", "ext::4.2.8", "ext::4.4.2", "ext::4.7.2", "ext::4.8.1.1", "ext::4.8.1.2", "ext::4.8.1.3", "ext::4.8.1.5", "ext::4.8.2", "ext::7.10.6", "ext::7.11.2::cierre", "ext::7.11.3::intro", "ext::7.11.5", "ext::7.3.6", "ext::7.3::intro", "ext::7.5.7.1", "ext::7.6.1.1", "ext::7.8.5::intro", "ext::7.9.1.4", "ext::7.9.1.6", "ext::7.9.3::intersticial", "ext::8.2::intro", "ext::9.3.2", "ext::9.3.3.1", "ext::9.3.7"], "estado_e3": "cola_humana; cola_humana_veredicto_inutilizable", "materia_variantes": ["exterior", "operaciones en el mercado de cambios", "Operaciones de cambio", "exterior_cambios", "Régimen de operaciones en el exterior y operaciones de cambio", "Exterior y cambios", "Operaciones de cambio en el exterior", "Operaciones en mercado de cambios", "Operaciones cambiarias en el exterior", "Operatoria de cambios e ingresos por mercado de cambios", "Operaciones de cambios y exterior", "Disposiciones específicas para los ingresos por el mercado de cambios", "Disposiciones específicas para operaciones en el mercado de cambios — cobros de exportaciones de servicios", "Disposiciones para ingresos por mercado de cambios - Cobros de exportaciones de servicios", "Operaciones en el mercado de cambios - Exterior", "Exterior y Cambios", "Operaciones en el mercado de cambios — títulos de deuda y endeudamientos", "Operaciones en el mercado de cambios", "Disposiciones específicas para ingresos por mercado de cambios", "Operaciones de cambios — Exterior", "Exterior Cambios", "Operaciones en cambios - Ingresos por mercado de cambios", "Exterior", "Operaciones de cambios en el exterior", "Operaciones en cambios para residentes en el exterior", "Operaciones en mercado de cambios — Exterior", "Operaciones en el mercado de cambios — obligaciones de liquidación", "Operaciones de cambio - ingresos por mercado de cambios", "Operaciones de cambios en el mercado de cambios", "Operaciones de cambios", "Disposiciones para egresos por mercado de cambios", "Operaciones en el mercado de cambios - Egresos", "Disposiciones específicas para egresos por mercado de cambios", "Operaciones del mercado de cambios", "Operaciones en el mercado de cambios — Pagos de intereses de deudas por importaciones", "Disposiciones para operaciones de cambio - egresos", "Operaciones en cambios — Egresos", "Operaciones del mercado de cambios — Egresos", "Operaciones en cambios", "Operaciones de cambios — egresos", "Operaciones de cambios — Egresos", "Operaciones en el mercado de cambios — egresos", "Operaciones de cambios – disposiciones específicas para egresos", "Operaciones de cambio — egresos", "Operaciones de cambio — pagos títulos de deuda y endeudamientos", "Operaciones en el mercado de cambios — Pagos de títulos de deuda", "Operaciones en mercado de cambios — pagos de títulos y endeudamientos", "Operaciones por el mercado de cambios — pagos de títulos de deuda", "Pagos de títulos de deuda y endeudamientos con el exterior", "Operaciones de cambios - Egresos", "Operaciones en el mercado de cambios — pagos de títulos de deuda y endeudamientos", "Operaciones de cambio - Exterior", "Operaciones en el mercado de cambios — pagos de deuda y endeudamientos con el exterior", "Operaciones de cambio — Pagos de títulos de deuda y endeudamientos con el exterior", "Operaciones en el mercado de cambios — pagos de deuda externa", "Operaciones de cambios - Exterior", "Egresos por el mercado de cambios", "Egresos por mercado de cambios", "Operaciones de cambio en el mercado exterior", "Disposiciones específicas para operaciones de cambios", "Operaciones de cambio - Pagos de títulos de deuda en moneda extranjera", "Disposiciones para operaciones en el mercado de cambios", "Operaciones en el mercado de cambios — títulos de deuda", "Disposiciones para operaciones en mercado de cambios", "Operaciones en el mercado de cambios — Egresos", "Disposiciones para operaciones de cambio — exterior", "Operaciones de cambios - Egresos por el mercado de cambios", "Exterior y operaciones de cambio", "Disposiciones para operaciones de cambios en el exterior", "Disposiciones para operaciones de cambios y egreso de divisas", "Operaciones cambiarias", "Exterior - Cambios", "Disposiciones para operaciones de cambios - residentes con endeudamientos o fideicomisos", "operaciones de cambios — egresos", "Operaciones en el mercado de cambios para residentes", "Operaciones en mercado de cambios — egresos", "Operaciones en el mercado de cambios - egresos por residentes", "Disposiciones para operaciones de cambios — egresos", "Operaciones de cambio en el mercado de divisas", "Disposiciones para egresos por el mercado de cambios", "Operaciones de cambios y derivados", "Operaciones en cambios - Exterior", "Operaciones de cambio al exterior", "Operaciones de cambios - Repatriaciones y compras de moneda extranjera", "Disposiciones específicas para los egresos por el mercado de cambios", "Operaciones en cambios — Repatriaciones de inversiones directas", "Operaciones cambiarias y repatriaciones de no residentes", "Operaciones de cambios — Repatriaciones", "Operaciones del mercado de cambios - exterior", "Operaciones de cambio y transferencias de divisas", "Operaciones de cambios — Egresos por el mercado de cambios", "operaciones de cambios y egresos por el mercado de cambios", "Operaciones en el mercado de cambios — Exterior", "Operaciones en el mercado de cambios — exterior", "Operaciones de cambio - Cancelación de garantías financieras", "Operaciones de cambio — Exterior", "Operaciones en el mercado de cambios — requisitos complementarios", "Definiciones", "Operaciones de egresos por mercado de cambios", "Disposiciones para operaciones de cambios", "Operaciones de cambio - Egresos", "Mercado de cambios", "Operaciones de cambios — exterior", "Acceso al mercado de cambios", "Operaciones de cambios del mercado exterior", "Operaciones de cambio - repatriaciones de inversiones directas", "Disposiciones específicas para egresos por el mercado de cambios", "Operaciones de cambios y acceso a divisas", "Acceso a divisas para producción incremental", "Operaciones en el mercado de cambios — acceso a divisas", "Operaciones en el mercado de cambios — régimen de acceso a divisas para producción incremental de petróleo y/o gas", "Operaciones de cambios en el mercado exterior", "Operaciones de cambios — egreso de moneda extranjera", "Operaciones en el mercado de cambios - Acceso con Certificación de aumento de exportaciones", "Operaciones cambiaras, exportaciones", "Operaciones en el exterior y cambios", "Operaciones con moneda extranjera — retiros de efectivo desde el exterior", "Operaciones cambiarias y de exterior", "Operaciones con débito en cuenta local y tarjetas — Pagos al exterior", "Operaciones en el exterior y acceso al mercado de cambios", "Operaciones con cambios", "Operaciones con cambios — exterior", "Operaciones cambiarias y comerciales", "Operaciones en cambios — exterior", "Operaciones de comercio exterior y cambios", "Operaciones de cambio y comercio exterior", "Operaciones en cambios - exterior", "Operaciones con títulos valores", "Operaciones cambios exterior", "Operaciones con títulos valores — Exterior", "Operaciones en cambios - Entidades autorizadas", "Operaciones en cambios — Exterior", "Operaciones de cambio y exterior", "Operaciones de cambio de no residentes", "Operaciones cambiarias con no residentes", "Operaciones en cambios, suscripción de BOPREAL", "Operaciones de cambios — entidades autorizadas", "Operaciones en cambios y exterior", "Régimen de Operaciones de Cambios del Exterior", "exterior y cambios", "Operaciones en cambios en el exterior", "Operaciones de cambio, suscripción de bonos BOPREAL", "operaciones de cambio y exterior", "Operaciones en cambios, exterior", "Operaciones de cambio en exterior", "Operatoria de cambios en el exterior", "Operaciones de cambio — pautas operativas", "Operaciones de cambios — entidades financieras y cambiarias", "Operaciones de cambio y transferencias de fondos con el exterior", "Operaciones de cambio y transferencias de fondos desde y hacia el exterior", "Operaciones con cambios en el exterior", "Operaciones cambiarias — Exterior", "Operaciones de cambios y transferencias de divisas", "Operaciones de cambio y posiciones en moneda extranjera", "Pautas operativas para entidades autorizadas a operar en cambios", "Operaciones de cambios y tenencias en moneda extranjera", "Operaciones cambiarias propias", "Operaciones de cambio exterior", "Operaciones de cambio y remesas al exterior", "Operaciones en el exterior", "Operaciones de cambios y arbitrajes en el exterior", "Operaciones en cambios de entidades autorizadas", "Operaciones de cambio — importación y exportación de moneda nacional", "operaciones cambiarias", "Operaciones de cambio — exterior", "Exterior — Cambios", "Definiciones — Servicios", "Definición de Gobiernos locales", "Cobros de exportaciones de bienes", "Cobros de exportaciones", "Cobros de exportaciones de bienes — Exterior", "Cambios — Operaciones de comercio exterior", "Operaciones cambiarias en cuenta corriente de exportadores", "Operaciones de cambios - Cobros de exportaciones de bienes", "Operaciones con el Exterior - Cambios", "Operaciones financieras enunciadas", "Operaciones cambiarias del exterior", "Cambios - Exterior", "Operaciones de cambios, exterior", "Operaciones de cambios, cobros y pagos en el exterior", "Cobros de exportaciones — Ampliaciones de plazo", "Cobros de exportaciones de bienes — ampliaciones de plazo para liquidación de divisas", "Operaciones de cambio, comercio exterior", "Operaciones en cambios del exterior", "Cobros de exportaciones de bienes — Deudor moroso", "Cobros de exportaciones y exterior", "Operaciones de comercio exterior", "Operaciones cambiarias al exterior", "Operaciones de cambios y comercio exterior", "Operaciones en cambios y comercio exterior", "Cambios - Operaciones en el exterior", "Cobros de exportaciones de bienes - Régimen de fomento para las exportaciones de la economía del conocimiento", "Operaciones financieras habilitadas para aplicar cobros de exportaciones", "Operaciones cambiarias — exterior", "Operaciones cambistas de entidades autorizadas a operar en el exterior", "Operaciones del exterior", "Operaciones de cambios - Cobros de exportaciones", "Operaciones de cambio — Cobros de exportaciones", "Operaciones financieras habilitadas para cobros de exportaciones de bienes", "Cobros de exportaciones de bienes — operaciones financieras habilitadas", "Cobros de exportaciones de bienes y operaciones financieras habilitadas", "Operaciones cambarias y de comercio exterior", "Operaciones de exterior y cambios", "Operaciones en moneda extranjera y cambios", "Cobros de exportaciones de bienes en divisas", "Operaciones en cambios - Cobros de exportaciones", "Operaciones en cambios — Cobros de exportaciones de bienes", "Operaciones cambiarias, cobros de exportaciones", "Operaciones cambiarias en exterior", "Cobros de exportaciones de bienes — Decreto 234/21", "Operaciones de cambio, importaciones y exportaciones", "Cobros de exportaciones de bienes y financiaciones asociadas a importaciones", "Operaciones cambias en el exterior", "Operaciones de cambios, importación, exportación", "Operaciones cambiarias - Exterior", "Operaciones en cambios, financiaciones de exportación/importación", "Operaciones de cambios — Cobros de exportaciones de bienes", "Operaciones de cambios, cobros de exportaciones", "Cobros de exportaciones de bienes — Financiaciones asociadas a importaciones", "Seguimiento de negociaciones de divisas por exportaciones de bienes", "Seguimiento de negociaciones de divisas por exportaciones", "Negociación de divisas por exportaciones", "Operaciones de cambio y seguimiento de exportaciones de divisas", "Seguimiento de negociaciones de divisas por exportaciones de bienes — Exterior", "Operaciones de cambio — Seguimiento de divisas por exportaciones", "Operaciones de cambio y seguimiento de divisas por exportaciones", "Seguimiento de negociaciones de divisas", "Operaciones cambistas - seguimiento de divisas por exportaciones", "Seguimiento de negociaciones de divisas por exportaciones de bienes — Operaciones aduaneras exceptuadas", "Seguimiento de anticipos y financiaciones de exportación", "Seguimiento de anticipos y otras financiaciones de exportación", "Operaciones de cambio y seguimiento de financiaciones de exportación", "Seguimiento de anticipos y otras financiaciones de exportación de bienes", "Operaciones de cambios - Seguimiento de financiaciones de exportación", "Operaciones de cambio y financiaciones de exportación", "Seguimiento de anticipos y financiaciones de exportación de bienes", "Operaciones de cambio y financiación de exportaciones", "Seguimiento de anticipos y otras financiaciones de exportación de bienes; Certificaciones de aplicación de cobros de exportaciones", "Exterior y operaciones de cambios", "Exterior, Cambios, Operaciones de exportación", "Seguimiento de anticipos y financiaciones de exportación; certificaciones de aplicación", "Seguimiento de anticipos y financiaciones de exportación; certificaciones de aplicación de cobros", "Seguimiento de anticipos y otras financiaciones de exportación de bienes. Certificaciones de aplicación de cobros de exportaciones.", "Pagos de importaciones y operaciones de cambios en el exterior", "Pagos de importaciones y operaciones de cambio en el exterior", "Pagos de importaciones", "Pagos de importaciones y compras en el exterior", "Pagos de importaciones y compras en exterior", "Pagos de importaciones y otras compras de bienes en el exterior", "Pagos de importaciones y compras de bienes en exterior", "Pagos de importaciones y compras de bienes en el exterior", "Pagos de importaciones y operaciones de cambios", "Operaciones de cambio - Pagos de importaciones", "Operaciones en cambios, pagos de importaciones", "Exterior y Operaciones de Cambio", "Operaciones de cambio y pagos internacionales", "Pagos de importaciones y operaciones de cambio", "Operaciones en cambios - Pagos de importaciones", "Pagos de importaciones y operaciones cambiarias", "Operaciones de cambio — Pagos de importaciones", "Operaciones de cambios y pagos de importaciones", "Pagos de importaciones y operaciones en el exterior", "Pagos de importaciones y operaciones en cambios", "Pagos de importaciones en el exterior", "Pagos de importaciones y operaciones en cambios — exterior", "Operaciones en cambios y pagos de importaciones", "Operaciones en cambios con el exterior", "Pagos al exterior y operaciones de cambio", "Cambios, Pagos de importaciones", "Operaciones de cambio — Pagos de importaciones y compras de bienes en el exterior", "Pagos de importaciones y cambios", "Operaciones de cambio; pagos de importaciones", "Pagos de importaciones y operaciones cambiarias en el exterior", "Operaciones de cambios. Pagos de importaciones.", "Pagos de importaciones — Operaciones de cambio", "Operaciones en cambios — pagos de importaciones", "Operaciones de cambios y pagos al exterior", "Operaciones en cambios — Compras de bienes en exterior", "Operaciones de cambio, pagos de importaciones", "Exterior y operaciones cambiarias", "Operaciones con el exterior", "Operaciones de cambios — Pagos de importaciones", "Sistema de seguimiento de pagos de importaciones", "Sistema de seguimiento de pagos de importaciones (SEPAIMPO)", "Seguimiento de pagos de importaciones", "Régimen de operaciones en cambios", "Sistema de seguimiento de pagos de importaciones y certificación para acceso al mercado de cambios", "Sistema de seguimiento de pagos de importaciones y operaciones en comercio exterior", "Operaciones de cambios en comercio exterior", "Sistema de seguimiento de pagos de importaciones (SEPAIMPO) — Exterior y Cambios", "Sistema de seguimiento de pagos de importaciones - Certificación para afectación de despacho", "Sistema de seguimiento de pagos de importaciones (SEPAIMPO) — Certificación para afectación del despacho", "Sistema de seguimiento de pagos de importaciones (SEPAIMPO) - Certificación para afectación del despacho a pagos con registro de ingreso aduanero pendiente", "Sistema de seguimiento de pagos de importaciones (SEPAIMPO). Reporte de circunstancias que modifiquen obligaciones con el exterior.", "Sistema de seguimiento de pagos de importaciones y operaciones en mercado de cambios", "Sistema de seguimiento de pagos de importaciones (SEPAIMPO) — Reporte de cambio de entidad a cargo del seguimiento", "Operaciones de cambios. SEPAIMPO", "Pagos de servicios prestados por no residentes", "Operaciones de cambio con el exterior", "Pagos de servicios de no residentes", "Operaciones en cambios — Servicios prestados por no residentes", "Operaciones de cambios, sector exterior", "Pagos de servicios prestados por no residentes y acceso a divisas", "Operaciones de cambios — no residentes", "Operaciones de cambios - exterior", "Régimen de operaciones de cambios", "cambios", "Régimen de Incentivo para Grandes Inversiones - Acceso al mercado de cambios", "Régimen de operaciones de egreso en el mercado de cambios para VPU RIGI", "Régimen de Incentivo para Grandes Inversiones — acceso al mercado de cambios", "Operaciones de cambio - Régimen RIGI", "Cambios — operaciones de egreso para VPU adheridos al RIGI", "Régimen de operaciones de cambios para VPU adheridos al RIGI", "Régimen cambiario", "Régimen de operaciones de egreso en el mercado de cambios — RIGI", "Operaciones de cambios y egresos — RIGI", "Régimen de operaciones en cambios y exterior", "Régimen de Incentivo para Grandes Inversiones (RIGI) - Cambios", "Operaciones de cambio — RIGI", "Régimen de Incentivo para Grandes Inversiones (RIGI) — Disposiciones cambiarias", "Régimen de operaciones de cambio", "Mercado de cambios y operaciones en el exterior", "Disposiciones legales sobre estructura del mercado de cambios"], "version_variantes": ["actual", "", "ext", "vigente"]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "ext", "archivo": "TO_exterior_cambios_actual.pdf", "punto": "7.5.3", "rol_documental": "punto_propio", "chunk_id": "ext::7.5.3", "paginas": [87], "ancestros": ["S7", "7.5"]}`
- **Provenances (1):**
  - `{"to": "ext", "archivo": "TO_exterior_cambios_actual.pdf", "punto": "7.5.3", "rol_documental": "punto_propio", "chunk_id": "ext::7.5.3", "paginas": [87], "ancestros": ["S7", "7.5"]}`
- **Texto del punto ancla** (`ext::7.5.3`):

> 7.5.3. Permisos cuyos fondos se encuentran retenidos en las cuentas asociadas a los
> endeudamientos financieros referidas en los puntos 7.3.5., 7.9. y 7.11. y las
> prefinanciaciones de exportaciones comprendidas en el punto 7.8.5.
> En caso de que la fecha hasta la cual los cobros de un permiso deben permanecer
> depositados en virtud de lo exigido en el contrato del financiamiento fuese posterior al
> vencimiento del plazo para la liquidación de divisas del permiso, el exportador podrá
> solicitar que este plazo sea ampliado hasta el quinto día hábil posterior a dicha fecha.
> Esta opción estará disponible hasta alcanzar el 125% (ciento veinticinco por ciento) de
> los servicios por capital e intereses a abonar en el mes corriente y los siguientes 6
> (seis) meses calendario.

- **Herencia (3):**
  - [encabezado] S7 (páginas [80]):

    > Sección 7. Cobros de exportaciones de bienes.

  - [encabezado] 7.5 (páginas [86]):

    > 7.5. Ampliaciones del plazo para el ingreso y liquidación de divisas.

  - [intro] 7.5 (páginas [86]):

    > La entidad encargada del seguimiento del permiso podrá conceder extensiones en el plazo de
    > ingreso y liquidación en las siguientes circunstancias:

---

## 23 · índice 8265 · `limita`

- **Origen:** `Restriccion_anticipos_y_prefinanciaciones_de_exportaciones_del_exterior_pendientes_al_31_08__0c7085` · tipo `Restriccion` · label «Pendientes al 31/08/19 sin liquidación en mercado»
  - propiedades: `{"descripcion": "Anticipos y prefinanciaciones de exportaciones del exterior pendientes al 31/08/19 que no fueron liquidados en el mercado de cambios", "tipo": "limite_cualitativo"}`
- **Relación:** `limita`
- **Destino:** `Operacion_anticipos_y_prefinanciaciones_de_exportaciones_7ba4e5` · tipo `Operacion` · label «Anticipos y prefinanciaciones de exportaciones»
  - propiedades: `{"tipo": "anticipos_y_prefinanciaciones_de_exportaciones"}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "ext", "archivo": "TO_exterior_cambios_actual.pdf", "punto": "7.3.7", "rol_documental": "punto_propio", "chunk_id": "ext::7.3.7", "paginas": [84], "ancestros": ["S7", "7.3"]}`
- **Provenances (1):**
  - `{"to": "ext", "archivo": "TO_exterior_cambios_actual.pdf", "punto": "7.3.7", "rol_documental": "punto_propio", "chunk_id": "ext::7.3.7", "paginas": [84], "ancestros": ["S7", "7.3"]}`
- **Texto del punto ancla** (`ext::7.3.7`):

> 7.3.7. Anticipos y prefinanciaciones de exportaciones del exterior pendientes al 31/08/19 que
> no fueron liquidados en el mercado de cambios, en la medida que se cuente con la
> conformidad previa o se aplique el mecanismo descripto en el punto 9.3.3.2.
> Los exportadores que pretendan aplicar estas operaciones a embarques oficializados a
> partir del 02/09/19 deberán nominar una única entidad para que realice el seguimiento
> del conjunto de sus operaciones.
> Los pedidos de conformidad deberán ser presentados ante el BCRA exclusivamente
> por la entidad nominada por el exportador.

- **Herencia (3):**
  - [encabezado] S7 (páginas [80]):

    > Sección 7. Cobros de exportaciones de bienes.

  - [encabezado] 7.3 (páginas [83]):

    > 7.3. Aplicación de divisas de cobros de exportaciones.

  - [intro] 7.3 (páginas [83]):

    > Existe una aplicación de divisas de cobros de exportaciones de bienes cuando se ha
    > certificado que los propios bienes exportados o las divisas cobradas por ellos fueron utilizados
    > para cancelar el capital, intereses y/o gastos de otorgamiento de operaciones de
    > financiamiento, pagar utilidades y dividendos y/o concretar la repatriación de una inversión
    > directa de un accionista no residente en los casos admitidos en los puntos 7.3.1. a 7.3.11.
    > A los efectos que los cobros de exportaciones aplicados puedan ser imputados al
    > cumplimiento de los permisos de embarque oficializados a partir del 02/09/19, será necesario
    > contar en todos los casos con una certificación de aplicación emitida por la entidad encargada
    > del “Seguimiento de anticipos y otras financiaciones de exportación de bienes”.
    > Los exportadores que efectúen liquidaciones de moneda extranjera asociadas a las
    > operaciones comprendidas en los puntos 7.3.1. al 7.3.10. deberán solicitar a la entidad
    > interviniente que le asigne un número de identificación (número APX) y la incorpore al
    > mencionado seguimiento.
    > En el caso de operaciones comprendidas en el punto 7.3.8. que no registren liquidaciones en
    > el mercado de cambios por ser refinanciaciones de deudas preexistentes, la entidad nominada
    > por el exportador atento a lo establecido en el punto 7.9.3. deberá incorporarla al mencionado
    > seguimiento, usando para su identificación el número correlativo que se le asignó a la
    > operación del cliente (número ECO: Entidad-CUIT-N° Operación).

---

## 24 · índice 8531 · `establecida_en`

- **Origen:** `Restriccion_cuente_con_una_direccion_de_poca_capacidad_y_o_experiencia_y_o_de_honestidad_poc_e62027` · tipo `Restriccion` · label «Dirección de poca capacidad, experiencia u honestidad»
  - propiedades: `{"descripcion": "Cuente con una dirección de poca capacidad y/o experiencia y/o de honestidad poco clara y/o débil y/o con sistemas de control interno objetables.", "tipo": "limite_cualitativo"}`
- **Relación:** `establecida_en`
- **Destino:** `TextoOrdenado_to_clasificacion_deudores_actual_pdf` · tipo `TextoOrdenado` · label «Clasificación de Deudores»
  - propiedades: `{"materia": "clasificación de deudores", "archivo": "TO_clasificacion_deudores_actual.pdf", "version": "actual", "cola_humana": "true", "cola_chunks": ["cla::3.5.1", "cla::3.5::intro", "cla::6.5.3.5"], "estado_e3": "cola_humana", "materia_variantes": ["clasificación de deudores", "Clasificación de deudores", "clasificacion", "clasificacion_deudores", "clasificación", "Clasificación de Deudores", "Clasificación de deudores y previsión", "Clasificación", "Clasificación de deudores y previsiones por riesgo", "Criterios de clasificación de deudores", "Clasificación de deudores de cartera comercial", "Clasificación de deudores de la cartera comercial", "clasificacion_de_deudores", "clasificación de deudores cartera consumo vivienda"], "version_variantes": ["actual", "", "cla", "vigente"]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "cla", "archivo": "TO_clasificacion_deudores_actual.pdf", "punto": "6.5.3.3", "rol_documental": "punto_propio", "chunk_id": "cla::6.5.3.3", "paginas": [24], "ancestros": ["S6", "6.5", "6.5.3"]}`
- **Provenances (1):**
  - `{"to": "cla", "archivo": "TO_clasificacion_deudores_actual.pdf", "punto": "6.5.3.3", "rol_documental": "punto_propio", "chunk_id": "cla::6.5.3.3", "paginas": [24], "ancestros": ["S6", "6.5", "6.5.3"]}`
- **Texto del punto ancla** (`cla::6.5.3.3`):

> 6.5.3.3. Cuente con una dirección de poca capacidad y/o experiencia y/o de honestidad
> poco clara y/o débil y/o con sistemas de control interno objetables.

- **Herencia (5):**
  - [encabezado] S6 (páginas [17]):

    > Sección 6. Clasificación de los deudores de la cartera comercial.

  - [encabezado] 6.5 (páginas [19]):

    > 6.5. Niveles de clasificación.

  - [intro] 6.5 (páginas [19]):

    > Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si-
    > guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta-
    > llan en cada caso.
    > Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi-
    > nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda
    > registrado en el sistema financiero, según la última información disponible en la “Central de
    > deudores” a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las
    > normas sobre “Previsiones mínimas por riesgo de incobrabilidad” correspondiente a la peor cla-
    > sificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el
    > análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a
    > los fines a que se refiere el punto 6.6.
    > A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o
    > indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales
    > que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo
    > crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en
    > oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean con-
    > sistentes con el curso normal de los negocios y exista capacidad para atender el resto de las
    > obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una
    > mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse
    > que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones.
    > Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los produc-
    > tores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de
    > Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse
    > en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la
    > emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejora-
    > miento de la clasificación asignada al cliente en función de su situación individual, preexistente
    > a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.

  - [encabezado] 6.5.3 (páginas [23]):

    > 6.5.3. Con problemas.

  - [intro] 6.5.3 (páginas [23]):

    > El análisis del flujo de fondos del cliente demuestra que tiene problemas para atender
    > normalmente la totalidad de sus compromisos financieros y que, de no ser corregidos,
    > esos problemas pueden resultar en una pérdida para la entidad financiera.
    > Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:

---

## 25 · índice 8821 · `establecida_en`

- **Origen:** `Restriccion_el_flujo_de_fondos_es_manifiestamente_insuficiente_no_alcanzando_a_cubrir_el_pag_334bc2` · tipo `Restriccion` · label «Flujo de fondos insuficiente para cubrir intereses»
  - propiedades: `{"tipo": "limite_cualitativo", "descripcion": "El flujo de fondos es manifiestamente insuficiente, no alcanzando a cubrir el pago de intereses, y es factible presumir que también tendrá dificultades para cumplir eventuales acuerdos de refinanciación."}`
- **Relación:** `establecida_en`
- **Destino:** `TextoOrdenado_to_clasificacion_deudores_actual_pdf` · tipo `TextoOrdenado` · label «Clasificación de Deudores»
  - propiedades: `{"materia": "clasificación de deudores", "archivo": "TO_clasificacion_deudores_actual.pdf", "version": "actual", "cola_humana": "true", "cola_chunks": ["cla::3.5.1", "cla::3.5::intro", "cla::6.5.3.5"], "estado_e3": "cola_humana", "materia_variantes": ["clasificación de deudores", "Clasificación de deudores", "clasificacion", "clasificacion_deudores", "clasificación", "Clasificación de Deudores", "Clasificación de deudores y previsión", "Clasificación", "Clasificación de deudores y previsiones por riesgo", "Criterios de clasificación de deudores", "Clasificación de deudores de cartera comercial", "Clasificación de deudores de la cartera comercial", "clasificacion_de_deudores", "clasificación de deudores cartera consumo vivienda"], "version_variantes": ["actual", "", "cla", "vigente"]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "cla", "archivo": "TO_clasificacion_deudores_actual.pdf", "punto": "6.5.4.1", "rol_documental": "punto_propio", "chunk_id": "cla::6.5.4.1", "paginas": [26], "ancestros": ["S6", "6.5", "6.5.4"]}`
- **Provenances (1):**
  - `{"to": "cla", "archivo": "TO_clasificacion_deudores_actual.pdf", "punto": "6.5.4.1", "rol_documental": "punto_propio", "chunk_id": "cla::6.5.4.1", "paginas": [26], "ancestros": ["S6", "6.5", "6.5.4"]}`
- **Texto del punto ancla** (`cla::6.5.4.1`):

> 6.5.4.1. Presente una situación financiera ilíquida y muy alto nivel de endeudamiento, con
> resultados negativos en la explotación y obligación de vender activos de impor-
> tancia para la actividad desarrollada y que materialmente sean de magnitud sig-
> nificativa. El flujo de fondos es manifiestamente insuficiente, no alcanzando a cu-
> brir el pago de intereses, y es factible presumir que también tendrá dificultades
> para cumplir eventuales acuerdos de refinanciación.
> En el análisis que se lleve a cabo deberá tenerse en cuenta, de corresponder, la
> eventual incidencia que en su capacidad de pago pueda tener la situación en la
> que se encuentran los demás integrantes del grupo de contrapartes conectadas
> al cual pertenece.

- **Herencia (5):**
  - [encabezado] S6 (páginas [17]):

    > Sección 6. Clasificación de los deudores de la cartera comercial.

  - [encabezado] 6.5 (páginas [19]):

    > 6.5. Niveles de clasificación.

  - [intro] 6.5 (páginas [19]):

    > Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las si-
    > guientes cinco categorías, las que se definen teniendo en cuenta las condiciones que se deta-
    > llan en cada caso.
    > Los clientes que no registren asistencia crediticia de la entidad y que posteriormente reciban fi-
    > nanciaciones de ésta que no superen el importe resultante de aplicar sobre el saldo de deuda
    > registrado en el sistema financiero, según la última información disponible en la “Central de
    > deudores” a la fecha de su otorgamiento, el porcentaje establecido en el punto 2.2.5. de las
    > normas sobre “Previsiones mínimas por riesgo de incobrabilidad” correspondiente a la peor cla-
    > sificación asignada, podrán ser clasificados por la entidad teniendo en cuenta únicamente el
    > análisis del flujo de fondos proyectado. Las asistencias así otorgadas no serán consideradas a
    > los fines a que se refiere el punto 6.6.
    > A fin de verificar el cumplimiento de las obligaciones sin recurrir a nueva financiación directa o
    > indirecta o a refinanciaciones, no se considerarán refinanciaciones las facilidades adicionales
    > que se otorguen respecto de los márgenes vigentes acordados, siempre que el nuevo apoyo
    > crediticio implique nuevos desembolsos de fondos y no supere el 10 % del cupo asignado en
    > oportunidad de la última evaluación crediticia del cliente, en la medida en que éstas sean con-
    > sistentes con el curso normal de los negocios y exista capacidad para atender el resto de las
    > obligaciones financieras, ni las nuevas financiaciones y las refinanciaciones asociadas a una
    > mayor inversión derivada de la expansión de las actividades, y siempre que pueda demostrarse
    > que el flujo de fondos proyectado permitirá afrontar la totalidad de sus obligaciones.
    > Tampoco se considerarán dentro de ese concepto las refinanciaciones otorgadas a los produc-
    > tores agropecuarios cuando ello resulte de la aplicación de disposiciones vinculadas a la Ley de
    > Emergencia Agropecuaria, sin perjuicio de lo cual, a los fines de la clasificación, deberá tenerse
    > en cuenta el flujo de fondos proyectado para el momento en que concluya la vigencia de la
    > emergencia declarada. El tratamiento que se dispense en ese marco no podrá implicar mejora-
    > miento de la clasificación asignada al cliente en función de su situación individual, preexistente
    > a la emergencia, ni su aplicación extenderse más allá de la vigencia fijada para ella.

  - [encabezado] 6.5.4 (páginas [26]):

    > 6.5.4. Con alto riesgo de insolvencia.

  - [intro] 6.5.4 (páginas [26]):

    > El análisis del flujo de fondos del cliente demuestra que es altamente improbable que
    > pueda atender la totalidad de sus compromisos financieros.
    > Entre los indicadores que pueden reflejar esta situación se destacan que el cliente:

---

## 26 · índice 10078 · `aplica_a`

- **Origen:** `Restriccion_la_repatriacion_tenga_lugar_como_minimo_180_ciento_ochenta_dias_corridos_despues_5fc0b2` · tipo `Restriccion` · label «Plazo mínimo 180 días — repatriación post-21/04/25»
  - propiedades: `{"descripcion": "la repatriación tenga lugar como mínimo 180 (ciento ochenta) días corridos después de la liquidación de los fondos del aporte si el aporte fue ingresado y liquidado a partir del 21/04/25", "tipo": "limite_cuantitativo", "umbral": "180 días corridos"}`
- **Relación:** `aplica_a`
- **Destino:** `Sujeto_rol_entidad_autorizada_exterior` · tipo `Sujeto` · label «Entidades autorizadas a operar en cambios (Exterior)»
  - propiedades: `{"nivel": "rol", "cola_humana": "true", "cola_chunks": ["ext::10.10.2.3", "ext::10.3.2.5", "ext::10.3.3", "ext::10.3.5::intro", "ext::10.4.3::intro", "ext::10.5.5.2", "ext::10.9.4", "ext::13.2.7::intro", "ext::13.3.3", "ext::13.3.9", "ext::13.4.8", "ext::14.2.1.10", "ext::14.2.1::intro", "ext::14.5.3", "ext::3.11.2.1", "ext::3.11.3::cierre", "ext::3.14.5.5", "ext::3.16.2.1", "ext::3.17.5", "ext::3.18.1::cierre", "ext::3.3.3.4", "ext::3.5.1.12", "ext::3.5.1.9", "ext::3.5.6.10", "ext::3.5::intro", "ext::3.9::intro", "ext::4.4.2", "ext::4.8.1.1", "ext::4.8.1.2", "ext::4.8.1.3", "ext::4.8.1.5", "ext::7.10.6", "ext::7.11.2::cierre", "ext::7.11.3::intro", "ext::7.3::intro", "ext::7.5.7.1", "ext::7.6.1.1", "ext::7.9.1.4", "ext::7.9.3::intersticial", "ext::9.3.2", "ext::9.3.3.1", "ext::9.3.7"], "estado_e3": "cola_humana; cola_humana_veredicto_inutilizable"}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "ext", "archivo": "TO_exterior_cambios_actual.pdf", "punto": "3.13.1.7", "rol_documental": "punto_propio", "chunk_id": "ext::3.13.1.7", "paginas": [37], "ancestros": ["S3", "3.13", "3.13.1"]}`
- **Provenances (1):**
  - `{"to": "ext", "archivo": "TO_exterior_cambios_actual.pdf", "punto": "3.13.1.7", "rol_documental": "punto_propio", "chunk_id": "ext::3.13.1.7", "paginas": [37], "ancestros": ["S3", "3.13", "3.13.1"]}`
- **Texto del punto ancla** (`ext::3.13.1.7`):

> 3.13.1.7. Repatriaciones de inversiones directas de no residentes en empresas que
> no sean controlantes de entidades financieras locales de un aporte de
> capital que haya sido ingresado y liquidado por el mercado de cambios a
> partir del 02/10/20 en la medida que:
> i) la repatriación tenga lugar como mínimo 180 (ciento ochenta) días
> corridos después de la liquidación de los fondos del aporte si el
> aporte fue ingresado y liquidado a partir del 21/04/25; o
> ii) la repatriación tenga lugar como mínimo 2 (dos) años después de su
> liquidación si el aporte fue ingresado y liquidado entre el 02/10/20 y el
> 20/04/25.

- **Herencia (7):**
  - [encabezado] S3 (páginas [16]):

    > Sección 3. Disposiciones específicas para los egresos por el mercado de cambios

  - [chapeau_seccion] S3 (páginas [16]):

    > Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas
    > en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–,
    > adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán
    > cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables.

  - [encabezado] 3.13 (páginas [36]):

    > 3.13. Repatriaciones de inversiones directas y otras compras de moneda extranjera por parte de no

  - [intro] 3.13 (páginas [36]):

    > residentes

  - [encabezado] 3.13.1 (páginas [36]):

    > 3.13.1. El acceso al mercado de cambios para la repatriación de inversiones de no

  - [intro] 3.13.1 (páginas [36]):

    > residentes y otras compras de moneda extranjera por parte de clientes no residentes
    > requerirá la conformidad previa del BCRA, excepto para las operaciones de:

  - [cierre] 3.13.1 (páginas [39]):

    > Si una repatriación de una inversión directa de no residentes consiste en una
    > reducción de capital y/o devolución de aportes irrevocables realizadas por la empresa
    > local, adicionalmente a los requisitos previstos en cada caso, la entidad deberá contar
    > con la documentación que demuestre que se han cumplimentado los mecanismos
    > legales previstos y haber verificado que se encuentra declarada, en caso de
    > corresponder, en la última presentación vencida del “Relevamiento de activos y
    > pasivos externos” el pasivo en pesos con el exterior generado a partir de la fecha de
    > la no aceptación del aporte irrevocable o de la reducción de capital según
    > corresponda.

---

## 27 · índice 10277 · `establecida_en`

- **Origen:** `Restriccion_las_exposiciones_con_garantia_hipotecaria_normativas_deberan_cumplir_con_los_req_5cf1d3` · tipo `Restriccion` · label «Exposiciones normativas requieren cumplimiento requisitos 2.9.2»
  - propiedades: `{"descripcion": "Las exposiciones con garantía hipotecaria normativas deberán cumplir con los requisitos previstos en el punto 2.9.2.", "tipo": "limite_cualitativo"}`
- **Relación:** `establecida_en`
- **Destino:** `TextoOrdenado_to_capitales_minimos_actual_pdf` · tipo `TextoOrdenado` · label «Texto Ordenado Capitales Mínimos»
  - propiedades: `{"materia": "Capitales Mínimos", "archivo": "TO_capitales_minimos_actual.pdf", "version": "", "descripcion": "Cámara de compensación que interviene entre las partes de un contrato financiero negociado en uno o más mercados, actuando como comprador para todo vendedor y como vendedor para todo comprador, garantizando la ejecución futura de los contratos. La CCP se convierte en contraparte mediante novación, sistema de ofertas abiertas u otro esquema con fuerza legal.", "tipo": "definicion", "cola_humana": "true", "cola_chunks": ["cap::11.3", "cap::2.6.2::cierre", "cap::2.8.2", "cap::3.1.1.4", "cap::3.1.1.7", "cap::3.1.11.1", "cap::4.2.1.1", "cap::4.3.1.3", "cap::5.3.2.3", "cap::6.1.2.1", "cap::6.1.2.2", "cap::6.2.2.6", "cap::6.3.2.2", "cap::6.8.3.2", "cap::7.1.1.1"], "estado_e3": "cola_humana; cola_humana_reextraccion_invalida; cola_humana_veredicto_inutilizable", "materia_variantes": ["Capitales Mínimos", "Capitales mínimos", "capitales_minimos", "Capitales mínimos por riesgo de crédito", "Sector público no financiero", "Capital mínimo por riesgo de crédito", "Evaluaciones crediticias", "Capital mínimo", "Determinación de activos ponderados por riesgo de crédito", "capitales mínimos", "capital minimo", "capital_minimo_riesgo_credito", "exposiciones_minoristas", "capital mínimo por riesgo de crédito", "capitales minimos", "Capital mínimo por riesgo de crédito — Tabla de ponderadores de riesgo", "Capital mínimo por riesgo de crédito. Titulizaciones e inversiones en fondos", "Capital mínimo por riesgo de crédito. Titulizaciones", "Tratamiento de titulizaciones e inversiones en fondos", "Capital mínimo por riesgo de crédito de contraparte", "Definición de fondos de garantía (default funds) constituidos para absorción mutualizada de pérdidas", "Definición de estructura multinivel de clientes", "Requisitos de capital", "Aforos regulatorios — Cobertura del riesgo de crédito", "Cobertura del riesgo de crédito — Operaciones de financiación con títulos valores", "Método de Medición Estándar", "Capital mínimo por riesgo de mercado", "Capital mínimo por riesgo de mercado / riesgo específico", "Exigencia de capital por riesgo de mercado", "capital_minimo", "capital mínimo por riesgo de mercado", "capital mínimo", "Capital mínimo, riesgo de mercado, políticas y procedimientos", "capital", "Capital mínimo regulatorio", "Capital mínimo por riesgo operacional", "Responsabilidad patrimonial computable"], "version_variantes": ["", "actual", "vigente"]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "cap", "archivo": "TO_capitales_minimos_actual.pdf", "punto": "2.9.1", "rol_documental": "punto_propio", "chunk_id": "cap::2.9.1", "paginas": [18], "ancestros": ["S2", "2.9"]}`
- **Provenances (1):**
  - `{"to": "cap", "archivo": "TO_capitales_minimos_actual.pdf", "punto": "2.9.1", "rol_documental": "punto_propio", "chunk_id": "cap::2.9.1", "paginas": [18], "ancestros": ["S2", "2.9"]}`
- **Texto del punto ancla** (`cap::2.9.1`):

> 2.9.1. Tratamiento.
> Las entidades financieras del grupo 1 clasificarán a las exposiciones con garantía hipo-
> tecaria en normativas –las que deberán cumplir con los requisitos previstos en el punto
> 2.9.2.– y no normativas.
> Las exposiciones con garantía hipotecaria de las entidades financieras del grupo 2 re-
> cibirán el tratamiento previsto para las exposiciones con garantía hipotecaria normati-
> vas. A tal efecto, serán de aplicación los ponderadores de riesgo previstos en los pun-
> tos 2.12.8.1. y 2.12.8.2., siempre que se observe el requisito del punto 2.9.2.1.

- **Herencia (5):**
  - [encabezado] S2 (páginas [7]):

    > Sección 2. Capital mínimo por riesgo de crédito.

  - [chapeau_seccion] S2 (páginas [7]):

    > A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras
    > se clasificarán en:
    > i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local

  - [chapeau_seccion] S2 (páginas [7]):

    > (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor-
    > tancia sistémica global (G-SIB).

  - [chapeau_seccion] S2 (páginas [7]):

    > ii) Grupo 2: entidades financieras no comprendidas en el acápite i).
    > En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados
    > grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos.
    > Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los
    > acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas
    > correspondientes al nuevo grupo al que pertenezcan.

  - [encabezado] 2.9 (páginas [18]):

    > 2.9. Exposiciones con garantía hipotecaria.

---

## 28 · índice 10433 · `limita`

- **Origen:** `Restriccion_las_operaciones_en_las_que_la_exposicion_y_el_activo_recibido_en_garantia_esten__ce97e3` · tipo `Restriccion` · label «Operaciones misma moneda efectivo títulos aforo 20%»
  - propiedades: `{"descripcion": "Las operaciones en las que la exposición y el activo recibido en garantía estén denominados en la misma moneda y el mencionado activo recibido sea efectivo depositado en la entidad financiera, o títulos valores emitidos por el sector público no financiero o instrumentos de regulación monetaria emitidos por el BCRA a los que les corresponda un ponderador de riesgo del 0% y a cuyo valor de mercado se le haya aplicado un aforo de al menos el 20%, estarán sujetas a un ponderador de riesgo del 0%", "tipo": "limite_cuantitativo", "umbral": "0%"}`
- **Relación:** `limita`
- **Destino:** `Operacion_operacion_cobertura_activos_garantia_6fe96e` · tipo `Operacion` · label «Operación cobertura activos garantía»
  - propiedades: `{"tipo": "cobertura_con_activos_garantia"}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "cap", "archivo": "TO_capitales_minimos_actual.pdf", "punto": "5.3.1.3", "rol_documental": "punto_propio", "chunk_id": "cap::5.3.1.3", "paginas": [104, 105], "ancestros": ["S5", "5.3", "5.3.1"]}`
- **Provenances (1):**
  - `{"to": "cap", "archivo": "TO_capitales_minimos_actual.pdf", "punto": "5.3.1.3", "rol_documental": "punto_propio", "chunk_id": "cap::5.3.1.3", "paginas": [104, 105], "ancestros": ["S5", "5.3", "5.3.1"]}`
- **Texto del punto ancla** (`cap::5.3.1.3`):

> 5.3.1.3. Excepciones a la aplicación del ponderador de riesgo mínimo.
> El ponderador de riesgo de la parte de la exposición cubierta podrá ser inferior
> al 20% en los siguientes casos:
> i) Las operaciones de pase estarán sujetas a un ponderador de riesgo del 0%
> cuando la contraparte sea un “participante esencial del mercado” (punto
> 5.3.1.4.) y, además, se satisfaga la totalidad de las siguientes condiciones:
> a) La exposición y el activo recibido en garantía consisten en efectivo o en
> títulos valores emitidos por el sector público no financiero sujetos a un
> ponderador de riesgo del 0%.
> b) La exposición y el activo recibido en garantía estén denominados en la
> misma moneda.
> c) El plazo de vencimiento de la operación sea de un día hábil o bien la ex-
> posición y el activo recibido en garantía se valúen diariamente a precios
> de mercado y estén sujetos a liquidación/reposición diaria de márgenes.
> d) Cuando una de las partes incumpla la liquidación/reposición de márge-
> nes, el tiempo exigido entre la última valuación a precio de mercado pre-
> via al incumplimiento y la liquidación del activo no supere los cuatro días
> hábiles.
> e) La operación se liquide a través de un sistema previamente comprobado
> para este tipo de operaciones.
> f) La documentación de la operación sea la documentación estándar para
> las operaciones de pase con los títulos valores en cuestión.
> g) La documentación de la operación contemple que, en el caso de que
> una de las partes incumpla la obligación de entregar efectivo o títulos va-
> lores o de reponer el margen o cualquier otra obligación, la operación se-
> rá inmediatamente cancelable.
> h) Ante cualquier evento de incumplimiento, la entidad financiera conserve
> el derecho irrestricto y legalmente exigible de tomar inmediatamente po-
> sesión del activo y liquidarlo para cobrar sus acreencias.
> ii) Las operaciones de pase en las cuales la contraparte no sea un “participan-
> te esencial del mercado” (punto 5.3.1.4.), pero que satisfagan las restantes
> condiciones establecidas en el acápite i), estarán sujetas a un ponderador
> de riesgo del 10%.
> iii) Las operaciones en las que la exposición y el activo recibido en garantía es-
> tén denominados en la misma moneda y el mencionado activo recibido sea
> efectivo depositado en la entidad financiera, o títulos valores emitidos por el
> sector público no financiero o instrumentos de regulación monetaria emitidos
> por el BCRA a los que les corresponda un ponderador de riesgo del 0% y a
> cuyo valor de mercado se le haya aplicado un aforo de al menos el 20%, es-
> tarán sujetas a un ponderador de riesgo del 0%.

- **Herencia (6):**
  - [encabezado] S5 (páginas [98]):

    > Sección 5. Cobertura del riesgo de crédito.

  - [chapeau_seccion] S5 (páginas [98]):

    > A los efectos del cómputo de la exigencia de capital por riesgo de crédito, se reconocerá –total o
    > parcialmente– la cobertura del riesgo de crédito (CRC) de las operaciones registradas en la cartera
    > de inversión –tales como préstamos y responsabilidades eventuales– mediante la utilización de las
    > técnicas previstas en el punto 5.1.
    > La presente sección contempla, además, el cálculo de la exposición a las operaciones de financia-
    > ción con títulos valores (securities financing transactions, SFT) –conforme a lo previsto en la Sec-
    > ción 4.–, registradas tanto en la cartera de inversión como en la cartera de negociación.

  - [encabezado] 5.3 (páginas [103]):

    > 5.3. Operaciones cubiertas con activos admitidos como garantía.

  - [intro] 5.3 (páginas [103]):

    > La aplicación de la técnica de cobertura mediante activos admitidos como garantía dependerá
    > del método elegido.

  - [encabezado] 5.3.1 (páginas [103]):

    > 5.3.1. Método simple.

  - [intro] 5.3.1 (páginas [103]):

    > Con este método, el ponderador de riesgo de la contraparte se sustituye por el pondera-
    > dor de riesgo del activo mediante el cual se cubre –parcial o totalmente– la exposición
    > –conforme a la tabla de ponderadores prevista en la Sección 2.–.

---

## 29 · índice 10884 · `limita`

- **Origen:** `Restriccion_los_pagos_de_jubilaciones_y_otros_beneficios_previsionales_a_cargo_de_las_instit_11efad` · tipo `Restriccion` · label «Acuerdo bilateral requerido — pagos previsionales»
  - propiedades: `{"descripcion": "Los pagos de jubilaciones y otros beneficios previsionales a cargo de las instituciones previsionales solo podrán cursarse cuando exista un acuerdo bilateral suscripto entre las instituciones", "tipo": "limite_cualitativo"}`
- **Relación:** `limita`
- **Destino:** `Operacion_pagos_de_jubilaciones_y_beneficios_previsionales_6f4b62` · tipo `Operacion` · label «Pagos de jubilaciones y beneficios previsionales»
  - propiedades: `{"tipo": "pago de beneficio previsional"}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "ext", "archivo": "TO_exterior_cambios_actual.pdf", "punto": "4.2.3", "rol_documental": "punto_propio", "chunk_id": "ext::4.2.3", "paginas": [58], "ancestros": ["S4", "4.2"]}`
- **Provenances (1):**
  - `{"to": "ext", "archivo": "TO_exterior_cambios_actual.pdf", "punto": "4.2.3", "rol_documental": "punto_propio", "chunk_id": "ext::4.2.3", "paginas": [58], "ancestros": ["S4", "4.2"]}`
- **Texto del punto ancla** (`ext::4.2.3`):

> 4.2.3. Pagos de jubilaciones y otros beneficios previsionales a cargo de las instituciones
> previsionales de los países cuando exista un acuerdo bilateral suscripto entre las
> instituciones.

- **Herencia (5):**
  - [encabezado] S4 (páginas [56]):

    > Sección 4. Otras disposiciones específicas.

  - [encabezado] 4.2 (páginas [58]):

    > 4.2. Operaciones cursadas a través del Sistema de Monedas Locales (SML).

  - [intro] 4.2 (páginas [58]):

    > Los clientes residentes podrán canalizar a través del SML implementado por el BCRA con los
    > bancos centrales de la República Federativa del Brasil, la República Oriental del Uruguay y la
    > República del Paraguay, las siguientes operaciones:

  - [intersticial] 4.2 (páginas [58]):

    > En el caso de la República del Paraguay y de la República Oriental del Uruguay,
    > adicionalmente podrán ser cursadas las siguientes operaciones y sus devoluciones:

  - [cierre] 4.2 (páginas [58]):

    > En el caso de la República Federativa del Brasil, las operaciones comerciales no podrán tener
    > un plazo de pago que exceda a los 360 (trescientos sesenta) días corridos.
    > En todos los casos, la entidad deberá requerir una declaración jurada del cliente respecto a
    > que la operación corresponde a aquellas comprendidas en este sistema y que se cumplen las
    > disposiciones específicas y generales que le resulten normativamente aplicables.
    > La entidad deberá realizar un boleto de compra y/o venta de cambio, según corresponda,
    > conforme a lo estipulado en el punto 5.3.

---

## 30 · índice 11167 · `aplica_a`

- **Origen:** `Restriccion_no_tendra_acceso_al_mercado_de_cambios_para_pagar_el_equivalente_de_la_deuda_por_afd711` · tipo `Restriccion` · label «Restricción acceso mercado de cambios para pago de deuda»
  - propiedades: `{"descripcion": "No tendrá acceso al mercado de cambios para pagar el equivalente de la deuda por la cual se suscribió.", "tipo": "prohibicion"}`
- **Relación:** `aplica_a`
- **Destino:** `Sujeto_rol_entidad_autorizada_exterior` · tipo `Sujeto` · label «Entidades autorizadas a operar en cambios (Exterior)»
  - propiedades: `{"nivel": "rol", "cola_humana": "true", "cola_chunks": ["ext::10.10.2.3", "ext::10.3.2.5", "ext::10.3.3", "ext::10.3.5::intro", "ext::10.4.3::intro", "ext::10.5.5.2", "ext::10.9.4", "ext::13.2.7::intro", "ext::13.3.3", "ext::13.3.9", "ext::13.4.8", "ext::14.2.1.10", "ext::14.2.1::intro", "ext::14.5.3", "ext::3.11.2.1", "ext::3.11.3::cierre", "ext::3.14.5.5", "ext::3.16.2.1", "ext::3.17.5", "ext::3.18.1::cierre", "ext::3.3.3.4", "ext::3.5.1.12", "ext::3.5.1.9", "ext::3.5.6.10", "ext::3.5::intro", "ext::3.9::intro", "ext::4.4.2", "ext::4.8.1.1", "ext::4.8.1.2", "ext::4.8.1.3", "ext::4.8.1.5", "ext::7.10.6", "ext::7.11.2::cierre", "ext::7.11.3::intro", "ext::7.3::intro", "ext::7.5.7.1", "ext::7.6.1.1", "ext::7.9.1.4", "ext::7.9.3::intersticial", "ext::9.3.2", "ext::9.3.3.1", "ext::9.3.7"], "estado_e3": "cola_humana; cola_humana_veredicto_inutilizable"}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "ext", "archivo": "TO_exterior_cambios_actual.pdf", "punto": "4.6.1.4", "rol_documental": "punto_propio", "chunk_id": "ext::4.6.1.4", "paginas": [62], "ancestros": ["S4", "4.6", "4.6.1"]}`
- **Provenances (1):**
  - `{"to": "ext", "archivo": "TO_exterior_cambios_actual.pdf", "punto": "4.6.1.4", "rol_documental": "punto_propio", "chunk_id": "ext::4.6.1.4", "paginas": [62], "ancestros": ["S4", "4.6", "4.6.1"]}`
- **Texto del punto ancla** (`ext::4.6.1.4`):

> 4.6.1.4. Cuenta con una declaración jurada del cliente en la que deja constancia de
> que:
> i) las utilidades y dividendos por las cuales solicita la suscripción se
> encuentran pendientes de pago;
> ii) no ha utilizado ya este mecanismo por esta deuda; y
> iii) toma conocimiento de que no tendrá acceso al mercado de cambios
> para pagar el equivalente de la deuda por la cual se suscribió excepto
> que el pago se concrete a partir de un canje y arbitraje con los fondos
> depositados en una cuenta local y originados en cobros de capital e
> intereses en moneda extranjera de los bonos BOPREAL.
> La declaración jurada deberá estar firmada por el representante legal de la
> empresa residente o un apoderado con facultades suficientes para asumir
> este compromiso en nombre de la empresa.

- **Herencia (6):**
  - [encabezado] S4 (páginas [56]):

    > Sección 4. Otras disposiciones específicas.

  - [encabezado] 4.6 (páginas [61]):

    > 4.6. Suscripción de bonos BOPREAL por utilidades y dividendos de accionistas no residentes

  - [intro] 4.6 (páginas [61]):

    > pendientes de pago o ya percibidas en el país.

  - [encabezado] 4.6.1 (páginas [61]):

    > 4.6.1. Suscripción de bonos BOPREAL por utilidades y dividendos pendientes de pago a no

  - [intro] 4.6.1 (páginas [61]):

    > residentes a partir de la distribución determinada por la asamblea de accionistas.
    > Los clientes podrán suscribir Bonos para la Reconstrucción de una Argentina Libre
    > (BOPREAL) por hasta el equivalente al monto en moneda local de las utilidades y
    > dividendos pendientes de pago a accionistas no residentes a partir de la distribución
    > determinada por la asamblea de accionistas.
    > La entidad que concrete la oferta de suscripción en nombre del cliente deberá verificar
    > el cumplimiento de los siguientes requisitos:

  - [cierre] 4.6.1 (páginas [62]):

    > Adicionalmente, la mencionada entidad deberá realizar un boleto de venta de cambio a
    > nombre del cliente por el código de concepto "I09. Registro de utilidades y dividendos
    > por adjudicación de bonos BOPREAL"; consignando el valor nominal en moneda
    > extranjera de los bonos BOPREAL adjudicado al cliente.

