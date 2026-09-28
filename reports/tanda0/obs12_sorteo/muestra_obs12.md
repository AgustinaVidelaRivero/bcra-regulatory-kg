# Muestra de la observación (12) — aristas de extracción contra el texto

- Fecha del sorteo: 2026-09-28
- Grafo: `data/experiment/reextraccion_v2/corpus_tanda0/ens_cinco/r1/kg.json`
- sha256 del grafo: `4097d4fd3f300cb1c2cf09bef59e3ccb9a30b1de18334e6230102a5a3106d00a`
- Semilla: 20260927
- n (universo de aristas de extracción, A4.1): 3345 (total 3983 − referencia 521 − esqueleto 117 + solapamiento 0)
- k: 30
- Triplas duplicadas en el universo: 0
- E0: `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0`
  - chunks_ctacte.json: `e65fd5e7defc68c0ed2f2054f36757099175a0e68305704e5bde6474fbdc1a9d`
  - chunks_docvig.json: `97b62c050d8880b3e9d5fe0df69b2b908e6faaecfac317f02ded831bdbf435dd`
  - chunks_lingob.json: `8c502976b7e34989e18ca1be2d7e1a4625fd91d3ef42bf6f9846f8d348dad0b0`
  - chunks_pagjub.json: `1bba0713dae796c4ba811bac3ed64f411d9f0372771cf36dbd9e4150be312c38`
  - chunks_polcre.json: `9f6518549f4fbade3b5791f3b25062bd65a74e684a264d6df4ac9ecfdf11815b`
- Textos del punto ancla no encontrados: 0
- Relaciones en la muestra: establecida_en 21, aplica_a 7, regula 2
- Índices: [28, 50, 289, 292, 317, 437, 493, 546, 757, 803, 978, 1040, 1198, 1273, 1282, 1438, 1480, 1656, 1907, 1992, 2027, 2066, 2205, 2519, 2569, 2608, 2721, 2791, 3107, 3221]

Regla: universo de A4.1; orden por la tripla (source, relation, target); `sorted(random.Random(semilla).sample(range(n), k))` (enmienda del 27/09/2026, §2.1 y §2.2).

---

## 1 · índice 28 · `establecida_en`

- **Origen:** `Condicion_calidad_de_principal_pagador_con_renuncia_a_beneficios_4d7e12` · tipo `Condicion` · label «Calidad de principal pagador con renuncia a beneficios»
  - propiedades: `{"descripcion": "El garante se constituye como principal pagador con renuncia a los beneficios de excusión y división"}`
- **Relación:** `establecida_en`
- **Destino:** `TextoOrdenado_polcre_pdf` · tipo `TextoOrdenado` · label «Política de Crédito»
  - propiedades: `{"materia": "Política general de crédito", "archivo": "polcre.pdf", "version": "", "materia_variantes": ["Política general de crédito", "Política crediticia", "Política de Crédito", "Política de crédito", "Aplicación de la capacidad de préstamo de depósitos en moneda extranjera", "Aplicación de capacidad de préstamo de depósitos en moneda extranjera", "Financiaciones a productores, procesadores o acopiadores", "Aplicación de capacidad de préstamo en moneda extranjera", "Políticas de crédito", "Capacidad de préstamo de depósitos en moneda extranjera", "Aplicación de capacidad de préstamo", "Recursos propios líquidos", "Financiamiento al sector público no financiero del país", "Financiamiento a residentes en el exterior", "Financiamiento", "Préstamos de Unidades de Valor Adquisitivo (UVA)", "Préstamos de Unidades de Valor Adquisitivo", "Préstamos en UVA", "Préstamos de Unidades de Vivienda (UVI)", "Préstamos de Unidades de Vivienda actualizables por ICC", "Préstamos en Unidades de Vivienda", "Financiaciones a Grandes empresas exportadoras", "Financiaciones a Grandes empresas exportadoras — Clientes comprendidos", "Financiaciones", "Política de Créditos"], "version_variantes": ["", "actual", "vigente"]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "polcre", "archivo": "polcre.pdf", "punto": "2.1.2", "rol_documental": "punto_propio", "chunk_id": "polcre::2.1.2", "paginas": [6], "ancestros": ["S2", "2.1"]}`
- **Provenances (1):**
  - `{"to": "polcre", "archivo": "polcre.pdf", "punto": "2.1.2", "rol_documental": "punto_propio", "chunk_id": "polcre::2.1.2", "paginas": [6], "ancestros": ["S2", "2.1"]}`
- **Texto del punto ancla** (`polcre::2.1.2`):

> 2.1.2. Otras financiaciones a exportadores, que cuenten con un flujo de ingresos futuros en
> moneda extranjera y se constate, en el año previo al otorgamiento de la financiación,
> una facturación en moneda extranjera por un importe que guarde razonable relación con
> esa financiación.
> También quedarán comprendidas las financiaciones otorgadas a clientes que cuenten
> con garantías en moneda extranjera otorgadas por los sujetos señalados precedente-
> mente y que se constituyan como principales pagadores con renuncia a los beneficios
> de excusión y división.

- **Herencia (13):**
  - [encabezado] S2 (páginas [6]):

    > Sección 2. Aplicación de la capacidad de préstamo de depósitos en moneda extranjera.

  - [encabezado] 2.1 (páginas [6]):

    > 2.1. Destinos.

  - [intro] 2.1 (páginas [6]):

    > La capacidad de préstamo de los depósitos en moneda extranjera deberá aplicarse, en la co-
    > rrespondiente moneda de captación, en forma indistinta, a los siguientes destinos:

  - [cierre] 2.1 (páginas [8]):

    > La aplicación de la capacidad de préstamo de depósitos en moneda extranjera a los destinos
    > vinculados a operaciones de importación (previstos en los puntos 2.1.6., 2.1.7. y la parte atri-
    > buible a éstos por aplicación de los puntos 2.1.8. y 2.1.9.), no podrá superar el valor que resulte
    > de la siguiente expresión:
    > C max (F / C ; 0,05)

  - [cierre] 2.1 (páginas [8]):

    > x

  - [cierre] 2.1 (páginas [8]):

    > t base base

  - [cierre] 2.1 (páginas [8]):

    > Siendo:
    > C: capacidad de préstamo del mes al que corresponda.

  - [cierre] 2.1 (páginas [8]):

    > t

  - [cierre] 2.1 (páginas [9]):

    > F : financiación de importaciones comprendidas, correspondientes al trimestre agos-
    > base

  - [cierre] 2.1 (páginas [9]):

    > to/octubre de 2008.

  - [cierre] 2.1 (páginas [9]):

    > C : capacidad de préstamo que corresponda al trimestre agosto/octubre de 2008.

  - [cierre] 2.1 (páginas [9]):

    > base

  - [cierre] 2.1 (páginas [9]):

    > Las financiaciones y capacidad de préstamo deberán ser computadas de acuerdo con lo esta-
    > blecido en el punto 2.5.

---

## 2 · índice 50 · `establecida_en`

- **Origen:** `Condicion_cheques_emitidos_posteriores_a_notificacion_de_cierre_62d313` · tipo `Condicion` · label «Cheques emitidos posteriores a notificación de cierre»
  - propiedades: `{"descripcion": "Se trate de cheques emitidos con posterioridad a la pertinente notificación de cierre"}`
- **Relación:** `establecida_en`
- **Destino:** `TextoOrdenado_ctacte_pdf` · tipo `TextoOrdenado` · label «Cuentas a la vista»
  - propiedades: `{"materia": "Cuentas a la vista", "archivo": "ctacte.pdf", "version": "actual", "cola_humana": "true", "cola_chunks": ["ctacte::1.3.1.1", "ctacte::1.5.1.1", "ctacte::1.5.1.10", "ctacte::1.5.1.11", "ctacte::1.5.1.4", "ctacte::1.5.1.5", "ctacte::1.5.1.6", "ctacte::1.5.1.7", "ctacte::1.5.2.11", "ctacte::10.2.3::intro", "ctacte::12.1.2.5", "ctacte::3.5.2", "ctacte::4.5.1.2", "ctacte::6.4.1::intro", "ctacte::6.4.7::cierre", "ctacte::7.2.2.2", "ctacte::7.2.2.4", "ctacte::7.3.1.5"], "estado_e3": "cola_humana; cola_humana_veredicto_inutilizable", "materia_variantes": ["Cuentas a la vista", "Cuentas de corresponsalía", "Cuentas corrientes", "Identificación de titulares de cuentas corrientes", "Identificación de titulares y autorizados — cuentas corrientes", "Funcionamiento de cuentas corrientes", "cuentas_corrientes", "Identificación de titulares y personas autorizadas en cuentas corrientes", "cuentas de corresponsalía", "cuentas corrientes", "Cuentas a la vista (corrientes)", "Cuentas a la vista / Cuentas corrientes", "Cuentas Corrientes", "Movimiento de cuentas", "Cuentas a la vista (ctacte)", "Cuentas a la vista en el BCRA", "Cuentas corrientes — Tasas de interés", "Cheques", "Cheques — Títulos sin valor", "cheques", "Cheques - Títulos sin valor", "Cheques y cuentas de corresponsalía", "Cheques y sistemas de reproducción de firmas digitalizadas", "Cheques y corresponsalía", "Cheques - Reproducción de firmas digitalizadas", "Cheques librados por medios electrónicos", "Cheques de pago diferido", "Cheques de pago diferido — Cuentas de corresponsalía", "Endosos en cheques", "Endosos, modalidades especiales de emisión y aval", "Cuentas de Corresponsalía", "Cuentas de corresponsalía — Endosos, modalidades especiales de emisión y aval", "cuentas_de_corresponsalia", "Cheques — modalidades especiales de emisión", "Cheque certificado", "Rechazo de cheques — Defectos formales", "Rechazo de cheques", "ctacte", "Rechazo de cheques — Procedimiento — Motivos", "Extravío, sustracción o adulteración de cheques", "Extravío, sustracción o adulteración de cheques y otros documentos", "Cheques y documentos", "Central de cheques rechazados", "Central de cuentacorrentistas inhabilitados", "Central de cheques denunciados como extraviados, sustraídos o adulterados", "Central de cheques rechazados, Central de cuentacorrentistas inhabilitados, Central de cheques denunciados", "Cuentas a la vista — Correspondencia", "Cierre de cuentas y suspensión del servicio de pago de cheques", "Cuentas a la vista de corresponsales", "Procedimiento de cierre de cuentas", "Avisos — Contenido mínimo — Requisitos comunes", "Avisos — requisitos especiales para avisos de retención de cheques de pago diferido", "Avisos — Contenido mínimo — Requisitos especiales para cierre o suspensión", "Disposiciones generales", "Operaciones y servicios financieros", "Cuentas corrientes especiales", "transferencias", "Cooperación tributaria internacional", "Disposiciones generales - Cajeros automáticos", "cuentas de depósito", "Apertura de cuentas en forma no presencial", "cuentas corrientes no presenciales", "Procedimientos especiales de identificación de aportes a campañas electorales", "Cuentas corrientes — procedimientos especiales de identificación de aportes electorales", "Cuentas corrientes bancarias — Agrupaciones políticas"], "version_variantes": ["actual", "", "ctacte", "vigente", "3a. Comunicación A 3244"]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "ctacte", "archivo": "ctacte.pdf", "punto": "6.3.3", "rol_documental": "punto_propio", "chunk_id": "ctacte::6.3.3", "paginas": [36], "ancestros": ["S6", "6.3"]}`
- **Provenances (1):**
  - `{"to": "ctacte", "archivo": "ctacte.pdf", "punto": "6.3.3", "rol_documental": "punto_propio", "chunk_id": "ctacte::6.3.3", "paginas": [36], "ancestros": ["S6", "6.3"]}`
- **Texto del punto ancla** (`ctacte::6.3.3`):

> 6.3.3. La cuenta corriente se encuentre cerrada o exista suspensión del servicio de pago de
> cheques en forma previa a ello -exclusivamente en las condiciones a que se refiere la
> presente reglamentación- y se trate de cheques emitidos con posterioridad a la pertinen-
> te notificación de cierre.
> Los cheques emitidos con anterioridad a la pertinente notificación de cierre serán devuel-
> tos sin registrar, pero ello no se considerará rechazo a la registración y, por lo tanto, no
> deberá informarse al Banco Central de la República Argentina por ese motivo, ni dará lu-
> gar a la aplicación de multas.
> La leyenda a colocar en estos últimos casos será "Devuelto sin registrar por cuenta ce-
> rrada. Art. 60 Ley de Cheques".

- **Herencia (3):**
  - [encabezado] S6 (páginas [34]):

    > Sección 6. Rechazo de cheques.

  - [encabezado] 6.3 (páginas [36]):

    > 6.3. Causales de no registración.

  - [intro] 6.3 (páginas [36]):

    > Deberá rechazarse la registración de los cheques de pago diferido presentados a registro
    > cuando:

---

## 3 · índice 289 · `establecida_en`

- **Origen:** `Condicion_tasa_tamar_ultimo_dia_habil_o_ultima_disponible_37a814` · tipo `Condicion` · label «Tasa TAMAR: último día hábil o última disponible»
  - propiedades: `{"descripcion": "A tal fin se tomará en cuenta la tasa que informe el BCRA correspondiente al último día hábil del período del incumplimiento o, en su ausencia, la última disponible"}`
- **Relación:** `establecida_en`
- **Destino:** `TextoOrdenado_ctacte_pdf` · tipo `TextoOrdenado` · label «Cuentas a la vista»
  - propiedades: `{"materia": "Cuentas a la vista", "archivo": "ctacte.pdf", "version": "actual", "cola_humana": "true", "cola_chunks": ["ctacte::1.3.1.1", "ctacte::1.5.1.1", "ctacte::1.5.1.10", "ctacte::1.5.1.11", "ctacte::1.5.1.4", "ctacte::1.5.1.5", "ctacte::1.5.1.6", "ctacte::1.5.1.7", "ctacte::1.5.2.11", "ctacte::10.2.3::intro", "ctacte::12.1.2.5", "ctacte::3.5.2", "ctacte::4.5.1.2", "ctacte::6.4.1::intro", "ctacte::6.4.7::cierre", "ctacte::7.2.2.2", "ctacte::7.2.2.4", "ctacte::7.3.1.5"], "estado_e3": "cola_humana; cola_humana_veredicto_inutilizable", "materia_variantes": ["Cuentas a la vista", "Cuentas de corresponsalía", "Cuentas corrientes", "Identificación de titulares de cuentas corrientes", "Identificación de titulares y autorizados — cuentas corrientes", "Funcionamiento de cuentas corrientes", "cuentas_corrientes", "Identificación de titulares y personas autorizadas en cuentas corrientes", "cuentas de corresponsalía", "cuentas corrientes", "Cuentas a la vista (corrientes)", "Cuentas a la vista / Cuentas corrientes", "Cuentas Corrientes", "Movimiento de cuentas", "Cuentas a la vista (ctacte)", "Cuentas a la vista en el BCRA", "Cuentas corrientes — Tasas de interés", "Cheques", "Cheques — Títulos sin valor", "cheques", "Cheques - Títulos sin valor", "Cheques y cuentas de corresponsalía", "Cheques y sistemas de reproducción de firmas digitalizadas", "Cheques y corresponsalía", "Cheques - Reproducción de firmas digitalizadas", "Cheques librados por medios electrónicos", "Cheques de pago diferido", "Cheques de pago diferido — Cuentas de corresponsalía", "Endosos en cheques", "Endosos, modalidades especiales de emisión y aval", "Cuentas de Corresponsalía", "Cuentas de corresponsalía — Endosos, modalidades especiales de emisión y aval", "cuentas_de_corresponsalia", "Cheques — modalidades especiales de emisión", "Cheque certificado", "Rechazo de cheques — Defectos formales", "Rechazo de cheques", "ctacte", "Rechazo de cheques — Procedimiento — Motivos", "Extravío, sustracción o adulteración de cheques", "Extravío, sustracción o adulteración de cheques y otros documentos", "Cheques y documentos", "Central de cheques rechazados", "Central de cuentacorrentistas inhabilitados", "Central de cheques denunciados como extraviados, sustraídos o adulterados", "Central de cheques rechazados, Central de cuentacorrentistas inhabilitados, Central de cheques denunciados", "Cuentas a la vista — Correspondencia", "Cierre de cuentas y suspensión del servicio de pago de cheques", "Cuentas a la vista de corresponsales", "Procedimiento de cierre de cuentas", "Avisos — Contenido mínimo — Requisitos comunes", "Avisos — requisitos especiales para avisos de retención de cheques de pago diferido", "Avisos — Contenido mínimo — Requisitos especiales para cierre o suspensión", "Disposiciones generales", "Operaciones y servicios financieros", "Cuentas corrientes especiales", "transferencias", "Cooperación tributaria internacional", "Disposiciones generales - Cajeros automáticos", "cuentas de depósito", "Apertura de cuentas en forma no presencial", "cuentas corrientes no presenciales", "Procedimientos especiales de identificación de aportes a campañas electorales", "Cuentas corrientes — procedimientos especiales de identificación de aportes electorales", "Cuentas corrientes bancarias — Agrupaciones políticas"], "version_variantes": ["actual", "", "ctacte", "vigente", "3a. Comunicación A 3244"]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "ctacte", "archivo": "ctacte.pdf", "punto": "11.3", "rol_documental": "punto_propio", "chunk_id": "ctacte::11.3", "paginas": [54], "ancestros": ["S11"]}`
- **Provenances (1):**
  - `{"to": "ctacte", "archivo": "ctacte.pdf", "punto": "11.3", "rol_documental": "punto_propio", "chunk_id": "ctacte::11.3", "paginas": [54], "ancestros": ["S11"]}`
- **Texto del punto ancla** (`ctacte::11.3`):

> 11.3. Transferencias de saldos.
> Su realización se efectuará de conformidad con las disposiciones operativas establecidas por
> el BCRA.
> Los importes no ingresados en tiempo y forma a esta Institución por las entidades financieras
> estarán sujetos a un interés equivalente a la aplicación de 1,5 veces la Tasa Mayorista de Ar-
> gentina (TAMAR) total de bancos.
> A tal fin se tomará en cuenta la tasa que informe el BCRA correspondiente al último día hábil
> del período del incumplimiento o, en su ausencia, la última disponible.

- **Herencia (1):**
  - [encabezado] S11 (páginas [54]):

    > Sección 11. Procedimiento para la recepción de depósitos por las multas legalmente exigibles.

---

## 4 · índice 292 · `establecida_en`

- **Origen:** `Condicion_timing_previo_a_apertura_de_cuenta_de_alianza_3e3548` · tipo `Condicion` · label «Timing: previo a apertura de cuenta de alianza»
  - propiedades: `{"descripcion": "Previamente a efectuar la apertura de la cuenta de la alianza electoral"}`
- **Relación:** `establecida_en`
- **Destino:** `TextoOrdenado_ctacte_pdf` · tipo `TextoOrdenado` · label «Cuentas a la vista»
  - propiedades: `{"materia": "Cuentas a la vista", "archivo": "ctacte.pdf", "version": "actual", "cola_humana": "true", "cola_chunks": ["ctacte::1.3.1.1", "ctacte::1.5.1.1", "ctacte::1.5.1.10", "ctacte::1.5.1.11", "ctacte::1.5.1.4", "ctacte::1.5.1.5", "ctacte::1.5.1.6", "ctacte::1.5.1.7", "ctacte::1.5.2.11", "ctacte::10.2.3::intro", "ctacte::12.1.2.5", "ctacte::3.5.2", "ctacte::4.5.1.2", "ctacte::6.4.1::intro", "ctacte::6.4.7::cierre", "ctacte::7.2.2.2", "ctacte::7.2.2.4", "ctacte::7.3.1.5"], "estado_e3": "cola_humana; cola_humana_veredicto_inutilizable", "materia_variantes": ["Cuentas a la vista", "Cuentas de corresponsalía", "Cuentas corrientes", "Identificación de titulares de cuentas corrientes", "Identificación de titulares y autorizados — cuentas corrientes", "Funcionamiento de cuentas corrientes", "cuentas_corrientes", "Identificación de titulares y personas autorizadas en cuentas corrientes", "cuentas de corresponsalía", "cuentas corrientes", "Cuentas a la vista (corrientes)", "Cuentas a la vista / Cuentas corrientes", "Cuentas Corrientes", "Movimiento de cuentas", "Cuentas a la vista (ctacte)", "Cuentas a la vista en el BCRA", "Cuentas corrientes — Tasas de interés", "Cheques", "Cheques — Títulos sin valor", "cheques", "Cheques - Títulos sin valor", "Cheques y cuentas de corresponsalía", "Cheques y sistemas de reproducción de firmas digitalizadas", "Cheques y corresponsalía", "Cheques - Reproducción de firmas digitalizadas", "Cheques librados por medios electrónicos", "Cheques de pago diferido", "Cheques de pago diferido — Cuentas de corresponsalía", "Endosos en cheques", "Endosos, modalidades especiales de emisión y aval", "Cuentas de Corresponsalía", "Cuentas de corresponsalía — Endosos, modalidades especiales de emisión y aval", "cuentas_de_corresponsalia", "Cheques — modalidades especiales de emisión", "Cheque certificado", "Rechazo de cheques — Defectos formales", "Rechazo de cheques", "ctacte", "Rechazo de cheques — Procedimiento — Motivos", "Extravío, sustracción o adulteración de cheques", "Extravío, sustracción o adulteración de cheques y otros documentos", "Cheques y documentos", "Central de cheques rechazados", "Central de cuentacorrentistas inhabilitados", "Central de cheques denunciados como extraviados, sustraídos o adulterados", "Central de cheques rechazados, Central de cuentacorrentistas inhabilitados, Central de cheques denunciados", "Cuentas a la vista — Correspondencia", "Cierre de cuentas y suspensión del servicio de pago de cheques", "Cuentas a la vista de corresponsales", "Procedimiento de cierre de cuentas", "Avisos — Contenido mínimo — Requisitos comunes", "Avisos — requisitos especiales para avisos de retención de cheques de pago diferido", "Avisos — Contenido mínimo — Requisitos especiales para cierre o suspensión", "Disposiciones generales", "Operaciones y servicios financieros", "Cuentas corrientes especiales", "transferencias", "Cooperación tributaria internacional", "Disposiciones generales - Cajeros automáticos", "cuentas de depósito", "Apertura de cuentas en forma no presencial", "cuentas corrientes no presenciales", "Procedimientos especiales de identificación de aportes a campañas electorales", "Cuentas corrientes — procedimientos especiales de identificación de aportes electorales", "Cuentas corrientes bancarias — Agrupaciones políticas"], "version_variantes": ["actual", "", "ctacte", "vigente", "3a. Comunicación A 3244"]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "ctacte", "archivo": "ctacte.pdf", "punto": "12.11.1.2", "rol_documental": "punto_propio", "chunk_id": "ctacte::12.11.1.2", "paginas": [62], "ancestros": ["S12", "12.11", "12.11.1"]}`
- **Provenances (1):**
  - `{"to": "ctacte", "archivo": "ctacte.pdf", "punto": "12.11.1.2", "rol_documental": "punto_propio", "chunk_id": "ctacte::12.11.1.2", "paginas": [62], "ancestros": ["S12", "12.11", "12.11.1"]}`
- **Texto del punto ancla** (`ctacte::12.11.1.2`):

> 12.11.1.2. Agrupaciones políticas que integran la alianza.
> Previamente a efectuar la apertura de la cuenta de la alianza electoral,
> las entidades deberán recabar los datos de las agrupaciones políticas
> que la integran (denominación, duración, domicilios real y legal, número
> de inscripción, y responsables económicos-financieros o tesoreros, se-
> gún los datos obrantes en la justicia electoral), incluyendo las cuentas
> bancarias únicas de las que sean titulares, a los fines de efectuar las
> eventuales transferencias de fondos remanentes al momento de cierre
> de cuenta.

- **Herencia (6):**
  - [encabezado] S12 (páginas [55]):

    > Sección 12. Disposiciones generales.

  - [encabezado] 12.11 (páginas [62]):

    > 12.11. Procedimientos especiales de identificación de aportes a campañas electorales. Ley 27.504

  - [intro] 12.11 (páginas [62]):

    > –modificatoria de la Ley 26.215–.

  - [encabezado] 12.11.1 (páginas [62]):

    > 12.11.1. Apertura de cuenta.

  - [intro] 12.11.1 (páginas [62]):

    > Las entidades financieras que abran cuentas corrientes bancarias a la orden de las
    > agrupaciones políticas o alianzas electorales, según el requerimiento que a tal efec-
    > to establezca el oficio librado por el Juzgado Federal con competencia electoral,
    > deberán registrar los siguientes datos:

  - [cierre] 12.11.1 (páginas [62]):

    > La utilización de subcuentas –según lo previsto en el artículo 23 del Decreto
    > Nº 443/11 del Poder Ejecutivo Nacional– será considerada como una modalidad es-
    > trictamente operativa.

---

## 5 · índice 317 · `establecida_en`

- **Origen:** `Definicion_cheque_especificacion_de_banco_girado_y_domicilio_6c2e91` · tipo `Definicion` · label «Cheque — especificación de banco girado y domicilio»
  - propiedades: `{"termino": "banco girado y domicilio de pago", "descripcion": "Una de las especificaciones requeridas para que un título valga como cheque, conforme a los artículos 2°, 4°, 23 y 54 de la Ley de Cheques"}`
- **Relación:** `establecida_en`
- **Destino:** `TextoOrdenado_ctacte_pdf` · tipo `TextoOrdenado` · label «Cuentas a la vista»
  - propiedades: `{"materia": "Cuentas a la vista", "archivo": "ctacte.pdf", "version": "actual", "cola_humana": "true", "cola_chunks": ["ctacte::1.3.1.1", "ctacte::1.5.1.1", "ctacte::1.5.1.10", "ctacte::1.5.1.11", "ctacte::1.5.1.4", "ctacte::1.5.1.5", "ctacte::1.5.1.6", "ctacte::1.5.1.7", "ctacte::1.5.2.11", "ctacte::10.2.3::intro", "ctacte::12.1.2.5", "ctacte::3.5.2", "ctacte::4.5.1.2", "ctacte::6.4.1::intro", "ctacte::6.4.7::cierre", "ctacte::7.2.2.2", "ctacte::7.2.2.4", "ctacte::7.3.1.5"], "estado_e3": "cola_humana; cola_humana_veredicto_inutilizable", "materia_variantes": ["Cuentas a la vista", "Cuentas de corresponsalía", "Cuentas corrientes", "Identificación de titulares de cuentas corrientes", "Identificación de titulares y autorizados — cuentas corrientes", "Funcionamiento de cuentas corrientes", "cuentas_corrientes", "Identificación de titulares y personas autorizadas en cuentas corrientes", "cuentas de corresponsalía", "cuentas corrientes", "Cuentas a la vista (corrientes)", "Cuentas a la vista / Cuentas corrientes", "Cuentas Corrientes", "Movimiento de cuentas", "Cuentas a la vista (ctacte)", "Cuentas a la vista en el BCRA", "Cuentas corrientes — Tasas de interés", "Cheques", "Cheques — Títulos sin valor", "cheques", "Cheques - Títulos sin valor", "Cheques y cuentas de corresponsalía", "Cheques y sistemas de reproducción de firmas digitalizadas", "Cheques y corresponsalía", "Cheques - Reproducción de firmas digitalizadas", "Cheques librados por medios electrónicos", "Cheques de pago diferido", "Cheques de pago diferido — Cuentas de corresponsalía", "Endosos en cheques", "Endosos, modalidades especiales de emisión y aval", "Cuentas de Corresponsalía", "Cuentas de corresponsalía — Endosos, modalidades especiales de emisión y aval", "cuentas_de_corresponsalia", "Cheques — modalidades especiales de emisión", "Cheque certificado", "Rechazo de cheques — Defectos formales", "Rechazo de cheques", "ctacte", "Rechazo de cheques — Procedimiento — Motivos", "Extravío, sustracción o adulteración de cheques", "Extravío, sustracción o adulteración de cheques y otros documentos", "Cheques y documentos", "Central de cheques rechazados", "Central de cuentacorrentistas inhabilitados", "Central de cheques denunciados como extraviados, sustraídos o adulterados", "Central de cheques rechazados, Central de cuentacorrentistas inhabilitados, Central de cheques denunciados", "Cuentas a la vista — Correspondencia", "Cierre de cuentas y suspensión del servicio de pago de cheques", "Cuentas a la vista de corresponsales", "Procedimiento de cierre de cuentas", "Avisos — Contenido mínimo — Requisitos comunes", "Avisos — requisitos especiales para avisos de retención de cheques de pago diferido", "Avisos — Contenido mínimo — Requisitos especiales para cierre o suspensión", "Disposiciones generales", "Operaciones y servicios financieros", "Cuentas corrientes especiales", "transferencias", "Cooperación tributaria internacional", "Disposiciones generales - Cajeros automáticos", "cuentas de depósito", "Apertura de cuentas en forma no presencial", "cuentas corrientes no presenciales", "Procedimientos especiales de identificación de aportes a campañas electorales", "Cuentas corrientes — procedimientos especiales de identificación de aportes electorales", "Cuentas corrientes bancarias — Agrupaciones políticas"], "version_variantes": ["actual", "", "ctacte", "vigente", "3a. Comunicación A 3244"]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "ctacte", "archivo": "ctacte.pdf", "punto": "3.2.1.5", "rol_documental": "punto_propio", "chunk_id": "ctacte::3.2.1.5", "paginas": [20], "ancestros": ["S3", "3.2", "3.2.1"]}`
- **Provenances (1):**
  - `{"to": "ctacte", "archivo": "ctacte.pdf", "punto": "3.2.1.5", "rol_documental": "punto_propio", "chunk_id": "ctacte::3.2.1.5", "paginas": [20], "ancestros": ["S3", "3.2", "3.2.1"]}`
- **Texto del punto ancla** (`ctacte::3.2.1.5`):

> 3.2.1.5. El nombre del banco girado y el domicilio de pago.

- **Herencia (6):**
  - [encabezado] S3 (páginas [20]):

    > Sección 3. Cheques.

  - [encabezado] 3.2 (páginas [20]):

    > 3.2. Títulos que carecen de valor como cheques.

  - [intro] 3.2 (páginas [20]):

    > El título respecto del que se presentare alguna de las siguientes situaciones, enumeradas
    > taxativamente a continuación, no valdrá como cheque:

  - [cierre] 3.2 (páginas [20]):

    > Los títulos devueltos por esas situaciones no podrán ser objeto de nuevas presentaciones.

  - [encabezado] 3.2.1 (páginas [20]):

    > 3.2.1. Falta de alguna de las especificaciones contenidas en los artículos 2°, incisos 1 a 6, 4°,

  - [intro] 3.2.1 (páginas [20]):

    > 23 y 54, incisos 1 a 9, de la Ley de Cheques, a saber:

---

## 6 · índice 437 · `establecida_en`

- **Origen:** `Excepcion_la_obligacion_no_aplicara_cuando_se_trate_de_modificaciones_en_el_numero_de_docu_bf163e` · tipo `Excepcion` · label «Constancias obligatorias — modificación número documento»
  - propiedades: `{"descripcion": "La obligación no aplicará cuando se trate de modificaciones en el número de documento de identidad de acuerdo con lo previsto en el punto 3.1.4"}`
- **Relación:** `establecida_en`
- **Destino:** `TextoOrdenado_docvig_pdf` · tipo `TextoOrdenado` · label «docvig»
  - propiedades: `{"materia": "documentos de identidad", "archivo": "docvig.pdf", "version": "", "cola_humana": "true", "cola_chunks": ["docvig::1.2.2", "docvig::2.2.1.1", "docvig::2.2.2.1"], "estado_e3": "cola_humana; cola_humana_veredicto_inutilizable", "materia_variantes": ["documentos de identidad", "Documentación de vigilancia", "vigilancia", "Identificación de clientes", "requisitos documentales para extranjeros", "Requisitos documentales para extranjeros", "Documentos válidos para ciudadanos de Estados Partes del Mercosur", "Documentación de identidad para extranjeros residentes", "Documentos de viaje", "requisitos documentales para extranjeros mayores de 75 años con residencia transitoria o precaria, nacidos en otros países", "docvig", "identificación de extranjeros", "Vigilancia", "Documentación de personas humanas no residentes", "Documentos de identidad y vigilancia", "Vigencia de documentos de identidad", "Rectificación de documentos de identidad", "Vigilancia de documentos de identidad", "Prevención del lavado de activos y financiamiento del terrorismo", "Verificación de identidad"], "version_variantes": ["", "actual"]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "docvig", "archivo": "docvig.pdf", "punto": "3.3", "rol_documental": "bloque_cierre", "chunk_id": "docvig::3.3::cierre", "paginas": [8], "ancestros": ["S3"]}`
- **Provenances (1):**
  - `{"to": "docvig", "archivo": "docvig.pdf", "punto": "3.3", "rol_documental": "bloque_cierre", "chunk_id": "docvig::3.3::cierre", "paginas": [8], "ancestros": ["S3"]}`
- **Texto del punto ancla** (`docvig::3.3::cierre`):

> No será obligatoria para el cliente la entrega de las constancias del CUIT/CUIL a raíz de la recti-
> ficación en el nombre y/o apellido y/o en otros datos de identificación, excepto cuando se trate
> de modificaciones en el número de documento de identidad de acuerdo con lo previsto en el
> punto 3.1.4.

- **Herencia (2):**
  - [encabezado] S3 (páginas [7]):

    > Sección 3. Rectificación de documentos de identidad.

  - [encabezado] 3.3 (páginas [7]):

    > 3.3. Acreditación de los cambios.

---

## 7 · índice 493 · `establecida_en`

- **Origen:** `Excepcion_se_exceptuan_cuando_los_cheques_se_depositen_en_la_caja_de_valores_s_a_para_ser__01f444` · tipo `Excepcion` · label «Excepción — endosos para negociación en mercados de valores»
  - propiedades: `{"descripcion": "Se exceptúan cuando los cheques se depositen en la Caja de Valores S.A. para ser negociados en las bolsas de comercio y mercados de valores autorizados por la Comisión Nacional de Valores, siendo necesario que los endosos sean extendidos con la cláusula 'para su negociación en mercados de valores'"}`
- **Relación:** `establecida_en`
- **Destino:** `TextoOrdenado_ctacte_pdf` · tipo `TextoOrdenado` · label «Cuentas a la vista»
  - propiedades: `{"materia": "Cuentas a la vista", "archivo": "ctacte.pdf", "version": "actual", "cola_humana": "true", "cola_chunks": ["ctacte::1.3.1.1", "ctacte::1.5.1.1", "ctacte::1.5.1.10", "ctacte::1.5.1.11", "ctacte::1.5.1.4", "ctacte::1.5.1.5", "ctacte::1.5.1.6", "ctacte::1.5.1.7", "ctacte::1.5.2.11", "ctacte::10.2.3::intro", "ctacte::12.1.2.5", "ctacte::3.5.2", "ctacte::4.5.1.2", "ctacte::6.4.1::intro", "ctacte::6.4.7::cierre", "ctacte::7.2.2.2", "ctacte::7.2.2.4", "ctacte::7.3.1.5"], "estado_e3": "cola_humana; cola_humana_veredicto_inutilizable", "materia_variantes": ["Cuentas a la vista", "Cuentas de corresponsalía", "Cuentas corrientes", "Identificación de titulares de cuentas corrientes", "Identificación de titulares y autorizados — cuentas corrientes", "Funcionamiento de cuentas corrientes", "cuentas_corrientes", "Identificación de titulares y personas autorizadas en cuentas corrientes", "cuentas de corresponsalía", "cuentas corrientes", "Cuentas a la vista (corrientes)", "Cuentas a la vista / Cuentas corrientes", "Cuentas Corrientes", "Movimiento de cuentas", "Cuentas a la vista (ctacte)", "Cuentas a la vista en el BCRA", "Cuentas corrientes — Tasas de interés", "Cheques", "Cheques — Títulos sin valor", "cheques", "Cheques - Títulos sin valor", "Cheques y cuentas de corresponsalía", "Cheques y sistemas de reproducción de firmas digitalizadas", "Cheques y corresponsalía", "Cheques - Reproducción de firmas digitalizadas", "Cheques librados por medios electrónicos", "Cheques de pago diferido", "Cheques de pago diferido — Cuentas de corresponsalía", "Endosos en cheques", "Endosos, modalidades especiales de emisión y aval", "Cuentas de Corresponsalía", "Cuentas de corresponsalía — Endosos, modalidades especiales de emisión y aval", "cuentas_de_corresponsalia", "Cheques — modalidades especiales de emisión", "Cheque certificado", "Rechazo de cheques — Defectos formales", "Rechazo de cheques", "ctacte", "Rechazo de cheques — Procedimiento — Motivos", "Extravío, sustracción o adulteración de cheques", "Extravío, sustracción o adulteración de cheques y otros documentos", "Cheques y documentos", "Central de cheques rechazados", "Central de cuentacorrentistas inhabilitados", "Central de cheques denunciados como extraviados, sustraídos o adulterados", "Central de cheques rechazados, Central de cuentacorrentistas inhabilitados, Central de cheques denunciados", "Cuentas a la vista — Correspondencia", "Cierre de cuentas y suspensión del servicio de pago de cheques", "Cuentas a la vista de corresponsales", "Procedimiento de cierre de cuentas", "Avisos — Contenido mínimo — Requisitos comunes", "Avisos — requisitos especiales para avisos de retención de cheques de pago diferido", "Avisos — Contenido mínimo — Requisitos especiales para cierre o suspensión", "Disposiciones generales", "Operaciones y servicios financieros", "Cuentas corrientes especiales", "transferencias", "Cooperación tributaria internacional", "Disposiciones generales - Cajeros automáticos", "cuentas de depósito", "Apertura de cuentas en forma no presencial", "cuentas corrientes no presenciales", "Procedimientos especiales de identificación de aportes a campañas electorales", "Cuentas corrientes — procedimientos especiales de identificación de aportes electorales", "Cuentas corrientes bancarias — Agrupaciones políticas"], "version_variantes": ["actual", "", "ctacte", "vigente", "3a. Comunicación A 3244"]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "ctacte", "archivo": "ctacte.pdf", "punto": "5.1.1.1", "rol_documental": "punto_propio", "chunk_id": "ctacte::5.1.1.1", "paginas": [30], "ancestros": ["S5", "5.1", "5.1.1"]}`
- **Provenances (1):**
  - `{"to": "ctacte", "archivo": "ctacte.pdf", "punto": "5.1.1.1", "rol_documental": "punto_propio", "chunk_id": "ctacte::5.1.1.1", "paginas": [30], "ancestros": ["S5", "5.1", "5.1.1"]}`
- **Texto del punto ancla** (`ctacte::5.1.1.1`):

> 5.1.1.1. Cheques comunes: hasta un endoso.

- **Herencia (5):**
  - [encabezado] S5 (páginas [30]):

    > Sección 5. Endosos, modalidades especiales de emisión y aval.

  - [encabezado] 5.1 (páginas [30]):

    > 5.1. Endoso.

  - [encabezado] 5.1.1 (páginas [30]):

    > 5.1.1. Límite.

  - [intro] 5.1.1 (páginas [30]):

    > Los cheques que se presenten al cobro o –en su caso– a la registración hasta el
    > 31.12.27 inclusive, sólo podrán contener la cantidad de endosos que seguidamente se
    > indican:

  - [cierre] 5.1.1 (páginas [30]):

    > Se exceptúan de las limitaciones establecidas en este punto a los endosos que las enti-
    > dades financieras realicen para la obtención de financiación, a favor de una entidad fi-
    > nanciera o de un fiduciario de un fideicomiso financiero, en ambos casos comprendidos
    > en la Ley de Entidades Financieras y las sucesivas transmisiones a favor de otros sujetos
    > de la misma naturaleza, así como cuando los cheques se depositen en la Caja de Valo-
    > res S.A. para ser negociados en las bolsas de comercio y mercados de valores autoriza-
    > dos por la Comisión Nacional de Valores de la República Argentina, en cuyo caso los en-
    > dosos deberán ser extendidos con la cláusula “... para su negociación en mercados de
    > valores”. También se exceptuarán de la citada limitación los endosos a favor del BCRA y
    > aquellos efectuados en los ECHEQ.

---

## 8 · índice 546 · `aplica_a`

- **Origen:** `Obligacion_acompanar_la_nomina_de_los_cheques_comunes_y_de_pago_diferido_librados_a_la_fech_bd0f7f` · tipo `Obligacion` · label «Acompañar nómina de cheques librados»
  - propiedades: `{"descripcion": "Acompañar la nómina de los cheques (comunes y de pago diferido) librados a la fecha de notificación del pertinente cierre, aún no presentados al cobro, consignando su tipo, fechas de libramiento y, en su caso, de pago, con indicación de sus correspondientes importes.", "tipo": "presentacion_informativa"}`
- **Relación:** `aplica_a`
- **Destino:** `Sujeto_propuesto_cuentacorrentista` · tipo `Sujeto` · label «cuentacorrentista»
  - propiedades: `{"nivel": "propuesto", "cuarentena": "true", "padre_sugerido": "Sujeto_cliente"}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "ctacte", "archivo": "ctacte.pdf", "punto": "9.2.1.1", "rol_documental": "punto_propio", "chunk_id": "ctacte::9.2.1.1", "paginas": [49], "ancestros": ["S9", "9.2", "9.2.1"]}`
- **Provenances (1):**
  - `{"to": "ctacte", "archivo": "ctacte.pdf", "punto": "9.2.1.1", "rol_documental": "punto_propio", "chunk_id": "ctacte::9.2.1.1", "paginas": [49], "ancestros": ["S9", "9.2", "9.2.1"]}`
- **Texto del punto ancla** (`ctacte::9.2.1.1`):

> 9.2.1.1. Acompañar la nómina de los cheques (comunes y de pago diferido) librados a la
> fecha de notificación del pertinente cierre, aún no presentados al cobro, consig-
> nando su tipo, fechas de libramiento y, en su caso, de pago, con indicación de
> sus correspondientes importes, informar los anulados y devolver los no utiliza-
> dos.

- **Herencia (4):**
  - [encabezado] S9 (páginas [49]):

    > Sección 9. Cierre de cuentas y suspensión del servicio de pago de cheques como medida previa al cierre de la cuenta.

  - [encabezado] 9.2 (páginas [49]):

    > 9.2. Procedimiento.

  - [intro] 9.2 (páginas [49]):

    > Al verificarse cualquiera de las causales previstas en el punto 9.1., se observará el siguiente
    > procedimiento.

  - [encabezado] 9.2.1 (páginas [49]):

    > 9.2.1. Por parte del cuentacorrentista.

---

## 9 · índice 757 · `regula`

- **Origen:** `Obligacion_cuando_una_entidad_financiera_se_niegue_a_pagar_un_cheque_comun_o_de_pago_diferi_977898` · tipo `Obligacion` · label «Constancia de rechazo al dorso o repositorio ECHEQ»
  - propiedades: `{"descripcion": "Cuando una entidad financiera se niegue a pagar un cheque –común o de pago diferido–, sea presentado directamente por el tenedor ante la girada o a través de sistemas de compensación, antes de devolverlo deberá hacer constar esa negativa al dorso del mismo título o en añadido relacionado o registrarlo ante el repositorio de ECHEQ", "tipo": "otra", "plazo": "antes de devolverlo", "cola_humana": "true", "cola_chunks": ["ctacte::6.4.1::intro"], "estado_e3": "cola_humana_veredicto_inutilizable"}`
- **Relación:** `regula`
- **Destino:** `Operacion_rechazo_de_cheque_comun_o_diferido_a36303` · tipo `Operacion` · label «Rechazo de cheque común o diferido»
  - propiedades: `{"tipo": "rechazo de cheque", "descripcion": "Negativa a pagar un cheque común o de pago diferido, sea presentado directamente ante la girada o a través de sistemas de compensación", "cola_humana": "true", "cola_chunks": ["ctacte::6.4.1::intro"], "estado_e3": "cola_humana_veredicto_inutilizable"}`
- **Propiedades de la arista:** `{"cola_humana": "true", "cola_chunks": ["ctacte::6.4.1::intro"], "estado_e3": "cola_humana_veredicto_inutilizable"}`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "ctacte", "archivo": "ctacte.pdf", "punto": "6.4.1", "rol_documental": "bloque_intro", "chunk_id": "ctacte::6.4.1::intro", "paginas": [37], "ancestros": ["S6", "6.4"]}`
- **Provenances (1):**
  - `{"to": "ctacte", "archivo": "ctacte.pdf", "punto": "6.4.1", "rol_documental": "bloque_intro", "chunk_id": "ctacte::6.4.1::intro", "paginas": [37], "ancestros": ["S6", "6.4"]}`
- **Texto del punto ancla** (`ctacte::6.4.1::intro`):

> diferido–, sea presentado directamente por el tenedor ante la girada o a través de siste-
> mas de compensación, antes de devolverlo deberá hacer constar esa negativa al dorso
> del mismo título o en añadido relacionado o registrarlo ante el repositorio de ECHEQ
> –produciéndose en los tres casos los efectos previstos en el artículo 38 de la Ley de
> Cheques–, con expresa mención de:

- **Herencia (3):**
  - [encabezado] S6 (páginas [34]):

    > Sección 6. Rechazo de cheques.

  - [encabezado] 6.4 (páginas [37]):

    > 6.4. Procedimiento.

  - [encabezado] 6.4.1 (páginas [37]):

    > 6.4.1. Cuando una entidad financiera se niegue a pagar un cheque –común o de pago

---

## 10 · índice 803 · `aplica_a`

- **Origen:** `Obligacion_debera_dejar_constancia_del_termino_por_el_cual_se_extiende_la_certificacion_e33731` · tipo `Obligacion` · label «Constancia de término de certificación»
  - propiedades: `{"tipo": "presentacion_informativa", "descripcion": "Deberá dejar constancia del término por el cual se extiende la certificación"}`
- **Relación:** `aplica_a`
- **Destino:** `Sujeto_banco` · tipo `Sujeto` · label «Bancos»
  - propiedades: `{"nivel": "clase", "cola_humana": "true", "cola_chunks": ["ctacte::1.5.1.1", "ctacte::1.5.1.10", "ctacte::1.5.1.11", "ctacte::1.5.1.4", "ctacte::1.5.1.5", "ctacte::1.5.1.6", "ctacte::1.5.1.7", "ctacte::1.5.2.11", "ctacte::12.1.2.5", "ctacte::3.5.2", "ctacte::4.5.1.2", "ctacte::6.4.1::intro", "ctacte::6.4.7::cierre", "ctacte::7.2.2.2", "ctacte::7.2.2.4", "ctacte::7.3.1.5"], "estado_e3": "cola_humana; cola_humana_veredicto_inutilizable", "alias": ["Bancos del exterior", "Banco del exterior"]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "ctacte", "archivo": "ctacte.pdf", "punto": "5.5.1", "rol_documental": "punto_propio", "chunk_id": "ctacte::5.5.1", "paginas": [32], "ancestros": ["S5", "5.5"]}`
- **Provenances (1):**
  - `{"to": "ctacte", "archivo": "ctacte.pdf", "punto": "5.5.1", "rol_documental": "punto_propio", "chunk_id": "ctacte::5.5.1", "paginas": [32], "ancestros": ["S5", "5.5"]}`
- **Texto del punto ancla** (`ctacte::5.5.1`):

> 5.5.1. El banco que, en uso de las facultades conferidas por los artículos 48 y 49 de la Ley de
> Cheques, certifique un cheque a requerimiento del librador o del portador, deberá dejar
> constancia del término por el cual se extiende, así como que esa certificación deberá
> ser acreditada en la forma prevista en el punto 5.5.4.

- **Herencia (2):**
  - [encabezado] S5 (páginas [30]):

    > Sección 5. Endosos, modalidades especiales de emisión y aval.

  - [encabezado] 5.5 (páginas [32]):

    > 5.5. Cheque certificado.

---

## 11 · índice 978 · `establecida_en`

- **Origen:** `Obligacion_el_directorio_a_traves_de_la_intervencion_del_comite_de_auditoria_tiene_la_respo_903913` · tipo `Obligacion` · label «Directorio — Acceso irrestricto auditorías»
  - propiedades: `{"descripcion": "El Directorio, a través de la intervención del Comité de auditoría, tiene la responsabilidad de asegurar que tanto la función de auditoría interna como la de auditoría externa tengan acceso irrestricto a todos los sectores y a toda la información de la entidad.", "tipo": "otra"}`
- **Relación:** `establecida_en`
- **Destino:** `TextoOrdenado_lingob_pdf` · tipo `TextoOrdenado` · label «Lineamientos de gobierno societario»
  - propiedades: `{"materia": "Gobierno societario", "archivo": "lingob.pdf", "version": "actual", "cola_humana": "true", "cola_chunks": ["lingob::1.2.4", "lingob::2.1::intro", "lingob::6.1", "lingob::6.2.4::intro", "lingob::7.1.1", "lingob::7.1::intro"], "estado_e3": "cola_humana; cola_humana_veredicto_inutilizable", "materia_variantes": ["Gobierno societario", "gobierno societario", "Gobierno corporativo", "Código de gobierno societario", "Gobierno de Entidades Financieras", "Gobierno corporativo de entidades financieras", "Gobierno corporativo y gestión de riesgos", "Gobierno corporativo y administración de riesgos", "Alta Gerencia", "control interno", "Gobierno corporativo y responsabilidades del Directorio", "Directorio", "Gobierno Societario — Directorio", "Gobierno societario de entidades financieras", "Gobierno corporativo y autoridades de entidades financieras", "Directorio y gobierno corporativo", "Gobierno societario y funciones del Directorio", "Gobierno corporativo y funciones del Directorio", "Gobierno societario y administración de entidades financieras", "gobierno corporativo", "Directorio de entidades financieras", "Gobierno Societario", "Directorio, independencia, gobierno corporativo", "Gobiernos corporativos", "Gobierno corporativo y estructura directiva", "Directorio — Objetivos estratégicos y valores", "Gobierno Corporativo", "línea de gobierno", "Gobierno corporativo y responsabilidades de la Alta Gerencia", "Goberanza de entidades financieras", "Gobernanza", "Lingob", "Alta Gerencia - Responsabilidades", "Autoridades de entidades financieras", "Gobernanza corporativa — Alta Gerencia", "Gobernanza — Alta Gerencia — Decisiones gerenciales", "Comités — Líneas de Gobierno", "gobiernos corporativos", "Gobernanza corporativa y comités", "Governance y Comités", "Gobierno y administración de entidades financieras", "Estructura de gobierno corporativo", "Auditoría interna", "Auditorías y controles internos", "Auditorías interna y externa. Controles internos.", "Auditoría externa", "auditoría", "auditoría externa, controles internos", "Auditorías interna y externa", "Auditorías interna y externa, controles internos", "Política de incentivos económicos al personal", "Política de incentivos económicos", "Política de incentivos al personal", "Incentivos económicos", "Incentivos económicos al personal", "incentivos económicos", "Política de transparencia — Estructura del Directorio y Alta Gerencia", "Gobierno corporativo y divulgación de información", "Gobierno societario y transparencia", "gobierno_societario", "Gobierno corporativo y transparencia", "Política de transparencia en el gobierno societario", "gobierno corporativo y transparencia", "Gobierno corporativo / Transparencia", "Gobierno corporativo y políticas organizacionales", "Política de Conocimiento de Estructura Organizacional", "Política de conozca su estructura organizacional", "Otras políticas organizacionales", "Políticas organizacionales — conocimiento de estructuras", "Política de conocimiento de la estructura organizacional", "Estructura organizacional y gestión de riesgos", "Gobierno corporativo y estructura organizacional", "Políticas organizacionales — estructuras y productos complejos", "Políticas organizacionales", "Políticas organizacionales y estructura organizacional", "Governance y políticas organizacionales", "Paridad de género en autoridades de entidades financieras"], "version_variantes": ["actual", "", "1", "TO lingob", "TO"]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "lingob", "archivo": "lingob.pdf", "punto": "5.1.4", "rol_documental": "punto_propio", "chunk_id": "lingob::5.1.4", "paginas": [12], "ancestros": ["S5", "5.1"]}`
- **Provenances (1):**
  - `{"to": "lingob", "archivo": "lingob.pdf", "punto": "5.1.4", "rol_documental": "punto_propio", "chunk_id": "lingob::5.1.4", "paginas": [12], "ancestros": ["S5", "5.1"]}`
- **Texto del punto ancla** (`lingob::5.1.4`):

> 5.1.4. Acceso a la información.
> El Directorio, a través de la intervención del Comité de auditoría, tiene la responsabilidad
> de asegurar que tanto la función de auditoría interna como la de auditoría externa tengan
> acceso irrestricto a todos los sectores y a toda la información de la entidad.
> El Comité de auditoría deberá coordinar los esfuerzos de las auditorías externa e interna,
> mantener un diálogo fluido con éstas y monitorear el cumplimiento de las tareas com-
> prometidas. En el caso de las entidades financieras públicas, además deberá mantener,
> de corresponder, un diálogo con las instituciones de auditorías estatales y otros organis-
> mos de supervisión estatal responsables.

- **Herencia (2):**
  - [encabezado] S5 (páginas [11]):

    > Sección 5. Auditorías interna y externa. Controles internos.

  - [encabezado] 5.1 (páginas [11]):

    > 5.1. Auditorías interna y externa.

---

## 12 · índice 1040 · `establecida_en`

- **Origen:** `Obligacion_el_otorgamiento_de_asistencia_financiera_a_residentes_en_el_exterior_solo_proced_85bb87` · tipo `Obligacion` · label «Asistencia financiera a residentes exterior sujeta a criterio general»
  - propiedades: `{"descripcion": "El otorgamiento de asistencia financiera a residentes en el exterior sólo procederá en tanto se ajuste al criterio general sobre política de crédito indicado en la Sección 1.", "tipo": "otra"}`
- **Relación:** `establecida_en`
- **Destino:** `TextoOrdenado_polcre_pdf` · tipo `TextoOrdenado` · label «Política de Crédito»
  - propiedades: `{"materia": "Política general de crédito", "archivo": "polcre.pdf", "version": "", "materia_variantes": ["Política general de crédito", "Política crediticia", "Política de Crédito", "Política de crédito", "Aplicación de la capacidad de préstamo de depósitos en moneda extranjera", "Aplicación de capacidad de préstamo de depósitos en moneda extranjera", "Financiaciones a productores, procesadores o acopiadores", "Aplicación de capacidad de préstamo en moneda extranjera", "Políticas de crédito", "Capacidad de préstamo de depósitos en moneda extranjera", "Aplicación de capacidad de préstamo", "Recursos propios líquidos", "Financiamiento al sector público no financiero del país", "Financiamiento a residentes en el exterior", "Financiamiento", "Préstamos de Unidades de Valor Adquisitivo (UVA)", "Préstamos de Unidades de Valor Adquisitivo", "Préstamos en UVA", "Préstamos de Unidades de Vivienda (UVI)", "Préstamos de Unidades de Vivienda actualizables por ICC", "Préstamos en Unidades de Vivienda", "Financiaciones a Grandes empresas exportadoras", "Financiaciones a Grandes empresas exportadoras — Clientes comprendidos", "Financiaciones", "Política de Créditos"], "version_variantes": ["", "actual", "vigente"]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "polcre", "archivo": "polcre.pdf", "punto": "5.1", "rol_documental": "punto_propio", "chunk_id": "polcre::5.1", "paginas": [13], "ancestros": ["S5"]}`
- **Provenances (1):**
  - `{"to": "polcre", "archivo": "polcre.pdf", "punto": "5.1", "rol_documental": "punto_propio", "chunk_id": "polcre::5.1", "paginas": [13], "ancestros": ["S5"]}`
- **Texto del punto ancla** (`polcre::5.1`):

> 5.1. Criterio general.
> El otorgamiento de asistencia financiera a residentes en el exterior sólo procederá en tanto se
> ajuste al criterio general sobre política de crédito indicado en la Sección 1.
> Conforme a ello, se podrán conceder líneas de crédito a bancos del exterior, corresponsales o
> no, y a otros residentes en el exterior destinadas a facilitar las exportaciones locales.
> También se admite la existencia de créditos a residentes en el exterior correspondientes a des-
> fases de liquidación de operaciones con títulos valores o monedas extranjeras con cotización y
> las operaciones previstas en los siguientes puntos.

- **Herencia (1):**
  - [encabezado] S5 (páginas [13]):

    > Sección 5. Financiamiento a residentes en el exterior.

---

## 13 · índice 1198 · `establecida_en`

- **Origen:** `Obligacion_establecer_procesos_adecuados_para_la_aprobacion_de_operaciones_y_nuevos_product_9a5431` · tipo `Obligacion` · label «Establecer procesos adecuados aprobación operaciones»
  - propiedades: `{"descripcion": "Establecer procesos adecuados para la aprobación de operaciones y nuevos productos, en especial en relación con dichas actividades", "tipo": "otra"}`
- **Relación:** `establecida_en`
- **Destino:** `TextoOrdenado_lingob_pdf` · tipo `TextoOrdenado` · label «Lineamientos de gobierno societario»
  - propiedades: `{"materia": "Gobierno societario", "archivo": "lingob.pdf", "version": "actual", "cola_humana": "true", "cola_chunks": ["lingob::1.2.4", "lingob::2.1::intro", "lingob::6.1", "lingob::6.2.4::intro", "lingob::7.1.1", "lingob::7.1::intro"], "estado_e3": "cola_humana; cola_humana_veredicto_inutilizable", "materia_variantes": ["Gobierno societario", "gobierno societario", "Gobierno corporativo", "Código de gobierno societario", "Gobierno de Entidades Financieras", "Gobierno corporativo de entidades financieras", "Gobierno corporativo y gestión de riesgos", "Gobierno corporativo y administración de riesgos", "Alta Gerencia", "control interno", "Gobierno corporativo y responsabilidades del Directorio", "Directorio", "Gobierno Societario — Directorio", "Gobierno societario de entidades financieras", "Gobierno corporativo y autoridades de entidades financieras", "Directorio y gobierno corporativo", "Gobierno societario y funciones del Directorio", "Gobierno corporativo y funciones del Directorio", "Gobierno societario y administración de entidades financieras", "gobierno corporativo", "Directorio de entidades financieras", "Gobierno Societario", "Directorio, independencia, gobierno corporativo", "Gobiernos corporativos", "Gobierno corporativo y estructura directiva", "Directorio — Objetivos estratégicos y valores", "Gobierno Corporativo", "línea de gobierno", "Gobierno corporativo y responsabilidades de la Alta Gerencia", "Goberanza de entidades financieras", "Gobernanza", "Lingob", "Alta Gerencia - Responsabilidades", "Autoridades de entidades financieras", "Gobernanza corporativa — Alta Gerencia", "Gobernanza — Alta Gerencia — Decisiones gerenciales", "Comités — Líneas de Gobierno", "gobiernos corporativos", "Gobernanza corporativa y comités", "Governance y Comités", "Gobierno y administración de entidades financieras", "Estructura de gobierno corporativo", "Auditoría interna", "Auditorías y controles internos", "Auditorías interna y externa. Controles internos.", "Auditoría externa", "auditoría", "auditoría externa, controles internos", "Auditorías interna y externa", "Auditorías interna y externa, controles internos", "Política de incentivos económicos al personal", "Política de incentivos económicos", "Política de incentivos al personal", "Incentivos económicos", "Incentivos económicos al personal", "incentivos económicos", "Política de transparencia — Estructura del Directorio y Alta Gerencia", "Gobierno corporativo y divulgación de información", "Gobierno societario y transparencia", "gobierno_societario", "Gobierno corporativo y transparencia", "Política de transparencia en el gobierno societario", "gobierno corporativo y transparencia", "Gobierno corporativo / Transparencia", "Gobierno corporativo y políticas organizacionales", "Política de Conocimiento de Estructura Organizacional", "Política de conozca su estructura organizacional", "Otras políticas organizacionales", "Políticas organizacionales — conocimiento de estructuras", "Política de conocimiento de la estructura organizacional", "Estructura organizacional y gestión de riesgos", "Gobierno corporativo y estructura organizacional", "Políticas organizacionales — estructuras y productos complejos", "Políticas organizacionales", "Políticas organizacionales y estructura organizacional", "Governance y políticas organizacionales", "Paridad de género en autoridades de entidades financieras"], "version_variantes": ["actual", "", "1", "TO lingob", "TO"]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "lingob", "archivo": "lingob.pdf", "punto": "7.2.3.3", "rol_documental": "punto_propio", "chunk_id": "lingob::7.2.3.3", "paginas": [19], "ancestros": ["S7", "7.2", "7.2.3"]}`
- **Provenances (1):**
  - `{"to": "lingob", "archivo": "lingob.pdf", "punto": "7.2.3.3", "rol_documental": "punto_propio", "chunk_id": "lingob::7.2.3.3", "paginas": [19], "ancestros": ["S7", "7.2", "7.2.3"]}`
- **Texto del punto ancla** (`lingob::7.2.3.3`):

> 7.2.3.3. Establecer procesos adecuados para la aprobación de operaciones y nuevos
> productos, en especial en relación con dichas actividades (por ejemplo, límites
> aplicables, medidas para mitigar el riesgo legal y de reputación, exigencias de
> información, etc.).

- **Herencia (5):**
  - [encabezado] S7 (páginas [17]):

    > Sección 7. Otras políticas organizacionales.

  - [encabezado] 7.2 (páginas [18]):

    > 7.2. Política de “conozca su estructura organizacional”.

  - [intro] 7.2 (páginas [18]):

    > En línea con las buenas prácticas, el Directorio y la Alta Gerencia deberán entender en la es-
    > tructura operativa de la entidad, incluidas las estructuras a que se refiere el punto 7.1.9. (princi-
    > pio de “conozca su estructura organizacional”).
    > El Directorio deberá establecer políticas y límites para operar con determinadas jurisdicciones
    > del exterior y para el uso de estructuras complejas o de menor transparencia, para operaciones
    > propias o por cuenta de terceros. Asimismo, deberá asegurar que la Alta Gerencia dé
    > cumplimiento a las políticas referidas a la identificación y gestión de los riesgos –incluso legal y
    > de reputación– asociados a tales operaciones, actividades o estructuras. Por su parte, la Alta
    > Gerencia bajo la supervisión del Directorio, deberá documentar este proceso de evaluación,
    > autorización y gestión del riesgo, para dotarlo de mayor transparencia para los auditores y
    > supervisores.
    > El Directorio deberá adoptar medidas y asegurar que los riesgos de estas actividades se com-
    > prendan y gestionen adecuadamente, tales como:

  - [encabezado] 7.2.3 (páginas [19]):

    > 7.2.3. Definir políticas, procedimientos y estrategias adecuados para aprobar estructuras o ins-

  - [intro] 7.2.3 (páginas [19]):

    > trumentos financieros complejos, utilizados o vendidos por la entidad financiera, y que
    > permitan la evaluación periódica de la utilización y/o venta de esas estructuras, produc-
    > tos o instrumentos, como parte del examen habitual de gestión.
    > Las entidades financieras que empleen este tipo de estructuras, productos o instrumen-
    > tos deberán evaluar y gestionar adecuadamente los riesgos derivados de su utilización y
    > comercialización, incluidos los riesgos legales y de reputación.
    > En este sentido, el Directorio y la Alta Gerencia se asegurarán de que se apliquen políti-
    > cas y procedimientos, respectivamente, para:

---

## 14 · índice 1273 · `aplica_a`

- **Origen:** `Obligacion_identificar_los_distintos_tipos_de_transaccion_mediante_un_codigo_especifico_que_d86a7a` · tipo `Obligacion` · label «Identificar tipos transacción mediante código»
  - propiedades: `{"tipo": "otra", "descripcion": "Identificar los distintos tipos de transacción mediante un código específico que cada entidad instrumente a tal efecto en el extracto"}`
- **Relación:** `aplica_a`
- **Destino:** `Sujeto_banco` · tipo `Sujeto` · label «Bancos»
  - propiedades: `{"nivel": "clase", "cola_humana": "true", "cola_chunks": ["ctacte::1.5.1.1", "ctacte::1.5.1.10", "ctacte::1.5.1.11", "ctacte::1.5.1.4", "ctacte::1.5.1.5", "ctacte::1.5.1.6", "ctacte::1.5.1.7", "ctacte::1.5.2.11", "ctacte::12.1.2.5", "ctacte::3.5.2", "ctacte::4.5.1.2", "ctacte::6.4.1::intro", "ctacte::6.4.7::cierre", "ctacte::7.2.2.2", "ctacte::7.2.2.4", "ctacte::7.3.1.5"], "estado_e3": "cola_humana; cola_humana_veredicto_inutilizable", "alias": ["Bancos del exterior", "Banco del exterior"]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "ctacte", "archivo": "ctacte.pdf", "punto": "1.5.2.3", "rol_documental": "punto_propio", "chunk_id": "ctacte::1.5.2.3", "paginas": [10, 11], "ancestros": ["S1", "1.5", "1.5.2"]}`
- **Provenances (1):**
  - `{"to": "ctacte", "archivo": "ctacte.pdf", "punto": "1.5.2.3", "rol_documental": "punto_propio", "chunk_id": "ctacte::1.5.2.3", "paginas": [10, 11], "ancestros": ["S1", "1.5", "1.5.2"]}`
- **Texto del punto ancla** (`ctacte::1.5.2.3`):

> 1.5.2.3. Enviar al cuentacorrentista, como máximo 8 días corridos después de finalizado
> cada mes y/o el período menor que se establezca y en las condiciones que se
> convenga, un extracto con el detalle de cada uno de los movimientos que se
> efectúen en la cuenta –débitos y créditos–, cualquiera sea su concepto, identifi-
> cando los distintos tipos de transacción mediante un código específico que cada
> entidad instrumente a tal efecto y los saldos registrados en el período que com-
> prende, pidiéndole su conformidad por escrito. También se deberán identificar en
> el correspondiente extracto las operaciones realizadas por cuenta propia o por
> cuenta de terceros, en la medida que se trate de depósitos de cheques por im-
> portes superiores a $ 1.000 y que así se encuentren identificados por el corres-
> pondiente endoso, mediante el procedimiento único que cada entidad opte por
> aplicar a tal fin.
> Adicionalmente, en el resumen se hará constar la clave bancaria uniforme (CBU)
> para que el cliente pueda formular su adhesión a servicios de débito automático,
> el plazo de compensación vigente para la operatoria de depósito de cheques y
> otros documentos compensables y el importe total debitado en el período en
> concepto de “Impuesto a las transacciones financieras”.
> En ese extracto o resumen de cuenta, adicionalmente las entidades informarán
> los siguientes datos mínimos:
> i) De producirse débitos correspondientes al servicio de débito automático:
> - Denominación de la empresa prestadora de servicios, organismo recauda-
> dor de impuestos, etc., al cual se destinaron los fondos debitados.
> - Identificación del cliente en la empresa o ente (apellido y nombre o código
> o cuenta, etc.).
> - Concepto de la operación causante del débito (mes, bimestre, cuota, etc.).
> - Importe debitado.
> - Fecha de débito.
> ii)De efectuarse transferencias:
> La información prevista en el punto 3.2. de las normas sobre “Sistema Nacio-
> nal de Pagos – Transferencias”, según corresponda.
> Se presumirá conformidad con el movimiento registrado en el banco si dentro de
> los 60 días corridos de vencido el respectivo período no se ha presentado en la
> entidad financiera la formulación de un reclamo.
> Cuando se reconozcan intereses sobre los saldos acreedores, se informarán las
> tasas nominal y efectiva, ambas anuales, correspondientes al período informado.
> Además, se hará constar la leyenda que corresponda incluir en materia de garan-
> tía de los depósitos, según lo previsto en el punto 6. de las normas sobre “Apli-
> cación del sistema de seguro de garantía de los depósitos” y, en el lugar que de-
> termine la entidad, número de clave de identificación tributaria (CUIT, CUIL o
> CDI) de los titulares de la cuenta, según los registros de la depositaria. Será obli-
> gación consignar los datos de hasta tres de sus titulares; cuando ellos excedan
> de dicho número, además, se indicará la cantidad total.

- **Herencia (4):**
  - [encabezado] S1 (páginas [5]):

    > Sección 1. Funcionamiento.

  - [encabezado] 1.5 (páginas [9]):

    > 1.5. Aspectos del funcionamiento a incluir en el contrato de cuenta corriente.

  - [intro] 1.5 (páginas [9]):

    > En sus cláusulas se deberá prever, como mínimo:

  - [encabezado] 1.5.2 (páginas [10]):

    > 1.5.2. Obligaciones de la entidad.

---

## 15 · índice 1282 · `aplica_a`

- **Origen:** `Obligacion_incluir_en_el_aviso_de_rechazo_al_pago_o_a_la_registracion_de_cheques_el_domicil_df2bb6` · tipo `Obligacion` · label «Inclusión domicilio cuenta — aviso de rechazo»
  - propiedades: `{"descripcion": "Incluir en el aviso de rechazo al pago o a la registración de cheques el domicilio de la cuenta registrado en la entidad girada, cuando éste no coincida con el inserto en el cuerpo del cheque", "tipo": "presentacion_informativa"}`
- **Relación:** `aplica_a`
- **Destino:** `Sujeto_banco` · tipo `Sujeto` · label «Bancos»
  - propiedades: `{"nivel": "clase", "cola_humana": "true", "cola_chunks": ["ctacte::1.5.1.1", "ctacte::1.5.1.10", "ctacte::1.5.1.11", "ctacte::1.5.1.4", "ctacte::1.5.1.5", "ctacte::1.5.1.6", "ctacte::1.5.1.7", "ctacte::1.5.2.11", "ctacte::12.1.2.5", "ctacte::3.5.2", "ctacte::4.5.1.2", "ctacte::6.4.1::intro", "ctacte::6.4.7::cierre", "ctacte::7.2.2.2", "ctacte::7.2.2.4", "ctacte::7.3.1.5"], "estado_e3": "cola_humana; cola_humana_veredicto_inutilizable", "alias": ["Bancos del exterior", "Banco del exterior"]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "ctacte", "archivo": "ctacte.pdf", "punto": "10.2.2.2", "rol_documental": "punto_propio", "chunk_id": "ctacte::10.2.2.2", "paginas": [53], "ancestros": ["S10", "10.2", "10.2.2"]}`
- **Provenances (1):**
  - `{"to": "ctacte", "archivo": "ctacte.pdf", "punto": "10.2.2.2", "rol_documental": "punto_propio", "chunk_id": "ctacte::10.2.2.2", "paginas": [53], "ancestros": ["S10", "10.2", "10.2.2"]}`
- **Texto del punto ancla** (`ctacte::10.2.2.2`):

> 10.2.2.2. Dirigidos al tenedor o presentante.
> i) Domicilio de la cuenta registrado en la entidad girada, cuando éste no
> coincida con el inserto en el cuerpo del cheque.
> ii) Nombres y apellidos del/os firmantes del/os cheque/s y su/s respectivo/s
> domicilio/s real/es.

- **Herencia (4):**
  - [encabezado] S10 (páginas [52]):

    > Sección 10. Avisos.

  - [encabezado] 10.2 (páginas [52]):

    > 10.2. Contenido mínimo.

  - [encabezado] 10.2.2 (páginas [52]):

    > 10.2.2. Requisitos adicionales en los avisos de rechazos al pago o a la registración de che-

  - [intro] 10.2.2 (páginas [52]):

    > ques.

---

## 16 · índice 1438 · `aplica_a`

- **Origen:** `Obligacion_la_informacion_referida_a_estos_documentos_sera_dada_de_baja_cuando_la_entidad_f_85d60d` · tipo `Obligacion` · label «Dar de baja información de documentos según presentación al cobro»
  - propiedades: `{"descripcion": "La información referida a estos documentos será dada de baja cuando la entidad financiera interviniente haya informado, conforme a la correspondiente guía operativa, la presentación al cobro o cuando corresponda dar de baja los cheques con motivo de la aplicación de lo previsto en el punto 7.3.3.2. iii)", "tipo": "otra", "cola_humana": "true", "cola_chunks": ["ctacte::7.3.1.5"], "estado_e3": "cola_humana"}`
- **Relación:** `aplica_a`
- **Destino:** `Sujeto_banco` · tipo `Sujeto` · label «Bancos»
  - propiedades: `{"nivel": "clase", "cola_humana": "true", "cola_chunks": ["ctacte::1.5.1.1", "ctacte::1.5.1.10", "ctacte::1.5.1.11", "ctacte::1.5.1.4", "ctacte::1.5.1.5", "ctacte::1.5.1.6", "ctacte::1.5.1.7", "ctacte::1.5.2.11", "ctacte::12.1.2.5", "ctacte::3.5.2", "ctacte::4.5.1.2", "ctacte::6.4.1::intro", "ctacte::6.4.7::cierre", "ctacte::7.2.2.2", "ctacte::7.2.2.4", "ctacte::7.3.1.5"], "estado_e3": "cola_humana; cola_humana_veredicto_inutilizable", "alias": ["Bancos del exterior", "Banco del exterior"]}`
- **Propiedades de la arista:** `{"cola_humana": "true", "cola_chunks": ["ctacte::7.3.1.5"], "estado_e3": "cola_humana"}`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "ctacte", "archivo": "ctacte.pdf", "punto": "7.3.1.5", "rol_documental": "punto_propio", "chunk_id": "ctacte::7.3.1.5", "paginas": [42], "ancestros": ["S7", "7.3", "7.3.1"]}`
- **Provenances (1):**
  - `{"to": "ctacte", "archivo": "ctacte.pdf", "punto": "7.3.1.5", "rol_documental": "punto_propio", "chunk_id": "ctacte::7.3.1.5", "paginas": [42], "ancestros": ["S7", "7.3", "7.3.1"]}`
- **Texto del punto ancla** (`ctacte::7.3.1.5`):

> 7.3.1.5. Informar, dentro de las 24 hs. hábiles siguientes a la recepción de la denuncia
> en la cual consten todos los datos identificatorios del cheque, al BCRA a los
> fines de que los documentos mencionados en el punto 7.1., excepto la fórmula
> especial para solicitar cuadernos de cheques, sean incluidos en la “Central de
> cheques denunciados como extraviados, sustraídos o adulterados”, de acuer-
> do con el procedimiento que se establezca en la correspondiente guía opera-
> tiva que difundirá esta Institución.
> La información referida a estos documentos será dada de baja cuando la enti-
> dad financiera interviniente haya informado, conforme a la correspondiente
> guía operativa, la presentación al cobro o cuando corresponda dar de baja los
> cheques con motivo de la aplicación de lo previsto en el punto 7.3.3.2. iii).

- **Herencia (3):**
  - [encabezado] S7 (páginas [41]):

    > Sección 7. Extravío, sustracción o adulteración de cheques y otros documentos.

  - [encabezado] 7.3 (páginas [41]):

    > 7.3. Obligaciones a cargo del banco.

  - [encabezado] 7.3.1 (páginas [41]):

    > 7.3.1. Cuando se haya dado cumplimiento a lo previsto en los puntos 7.2.2. y/o 7.2.3.

---

## 17 · índice 1480 · `regula`

- **Origen:** `Obligacion_las_cuentas_corrientes_deberan_contar_con_el_uso_de_cheques_ab8878` · tipo `Obligacion` · label «Uso de cheques — cuentas corrientes»
  - propiedades: `{"descripcion": "Las cuentas corrientes deberán contar con el uso de cheques", "tipo": "otra", "plazo": ""}`
- **Relación:** `regula`
- **Destino:** `Operacion_uso_de_cheques_en_cuentas_corrientes_247103` · tipo `Operacion` · label «Uso de cheques en cuentas corrientes»
  - propiedades: `{"tipo": "uso_de_cheques", "descripcion": "Utilización de cheques como instrumento en cuentas corrientes"}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "ctacte", "archivo": "ctacte.pdf", "punto": "1.2", "rol_documental": "punto_propio", "chunk_id": "ctacte::1.2", "paginas": [5], "ancestros": ["S1"]}`
- **Provenances (1):**
  - `{"to": "ctacte", "archivo": "ctacte.pdf", "punto": "1.2", "rol_documental": "punto_propio", "chunk_id": "ctacte::1.2", "paginas": [5], "ancestros": ["S1"]}`
- **Texto del punto ancla** (`ctacte::1.2`):

> 1.2. Atención de las cuentas.
> Las cuentas corrientes deberán contar con el uso de cheques, salvo que estén abiertas a nom-
> bre de personas jurídicas, en cuyo caso podrá establecerse que sea opcional la utilización de
> cheques.

- **Herencia (1):**
  - [encabezado] S1 (páginas [5]):

    > Sección 1. Funcionamiento.

---

## 18 · índice 1656 · `establecida_en`

- **Origen:** `Obligacion_las_modificaciones_en_las_condiciones_pactadas_incluyendo_el_importe_de_las_comi_fd050c` · tipo `Obligacion` · label «Modificaciones en condiciones — conforme Protección usuarios 2.3.4»
  - propiedades: `{"descripcion": "Las modificaciones en las condiciones pactadas –incluyendo el importe de las comisiones y/o cargos– deberán efectuarse de conformidad con lo dispuesto en el punto 2.3.4. de las normas sobre 'Protección de los usuarios de servicios financieros'.", "tipo": "otra"}`
- **Relación:** `establecida_en`
- **Destino:** `TextoOrdenado_ctacte_pdf` · tipo `TextoOrdenado` · label «Cuentas a la vista»
  - propiedades: `{"materia": "Cuentas a la vista", "archivo": "ctacte.pdf", "version": "actual", "cola_humana": "true", "cola_chunks": ["ctacte::1.3.1.1", "ctacte::1.5.1.1", "ctacte::1.5.1.10", "ctacte::1.5.1.11", "ctacte::1.5.1.4", "ctacte::1.5.1.5", "ctacte::1.5.1.6", "ctacte::1.5.1.7", "ctacte::1.5.2.11", "ctacte::10.2.3::intro", "ctacte::12.1.2.5", "ctacte::3.5.2", "ctacte::4.5.1.2", "ctacte::6.4.1::intro", "ctacte::6.4.7::cierre", "ctacte::7.2.2.2", "ctacte::7.2.2.4", "ctacte::7.3.1.5"], "estado_e3": "cola_humana; cola_humana_veredicto_inutilizable", "materia_variantes": ["Cuentas a la vista", "Cuentas de corresponsalía", "Cuentas corrientes", "Identificación de titulares de cuentas corrientes", "Identificación de titulares y autorizados — cuentas corrientes", "Funcionamiento de cuentas corrientes", "cuentas_corrientes", "Identificación de titulares y personas autorizadas en cuentas corrientes", "cuentas de corresponsalía", "cuentas corrientes", "Cuentas a la vista (corrientes)", "Cuentas a la vista / Cuentas corrientes", "Cuentas Corrientes", "Movimiento de cuentas", "Cuentas a la vista (ctacte)", "Cuentas a la vista en el BCRA", "Cuentas corrientes — Tasas de interés", "Cheques", "Cheques — Títulos sin valor", "cheques", "Cheques - Títulos sin valor", "Cheques y cuentas de corresponsalía", "Cheques y sistemas de reproducción de firmas digitalizadas", "Cheques y corresponsalía", "Cheques - Reproducción de firmas digitalizadas", "Cheques librados por medios electrónicos", "Cheques de pago diferido", "Cheques de pago diferido — Cuentas de corresponsalía", "Endosos en cheques", "Endosos, modalidades especiales de emisión y aval", "Cuentas de Corresponsalía", "Cuentas de corresponsalía — Endosos, modalidades especiales de emisión y aval", "cuentas_de_corresponsalia", "Cheques — modalidades especiales de emisión", "Cheque certificado", "Rechazo de cheques — Defectos formales", "Rechazo de cheques", "ctacte", "Rechazo de cheques — Procedimiento — Motivos", "Extravío, sustracción o adulteración de cheques", "Extravío, sustracción o adulteración de cheques y otros documentos", "Cheques y documentos", "Central de cheques rechazados", "Central de cuentacorrentistas inhabilitados", "Central de cheques denunciados como extraviados, sustraídos o adulterados", "Central de cheques rechazados, Central de cuentacorrentistas inhabilitados, Central de cheques denunciados", "Cuentas a la vista — Correspondencia", "Cierre de cuentas y suspensión del servicio de pago de cheques", "Cuentas a la vista de corresponsales", "Procedimiento de cierre de cuentas", "Avisos — Contenido mínimo — Requisitos comunes", "Avisos — requisitos especiales para avisos de retención de cheques de pago diferido", "Avisos — Contenido mínimo — Requisitos especiales para cierre o suspensión", "Disposiciones generales", "Operaciones y servicios financieros", "Cuentas corrientes especiales", "transferencias", "Cooperación tributaria internacional", "Disposiciones generales - Cajeros automáticos", "cuentas de depósito", "Apertura de cuentas en forma no presencial", "cuentas corrientes no presenciales", "Procedimientos especiales de identificación de aportes a campañas electorales", "Cuentas corrientes — procedimientos especiales de identificación de aportes electorales", "Cuentas corrientes bancarias — Agrupaciones políticas"], "version_variantes": ["actual", "", "ctacte", "vigente", "3a. Comunicación A 3244"]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "ctacte", "archivo": "ctacte.pdf", "punto": "1.5.2.10", "rol_documental": "punto_propio", "chunk_id": "ctacte::1.5.2.10", "paginas": [13], "ancestros": ["S1", "1.5", "1.5.2"]}`
- **Provenances (1):**
  - `{"to": "ctacte", "archivo": "ctacte.pdf", "punto": "1.5.2.10", "rol_documental": "punto_propio", "chunk_id": "ctacte::1.5.2.10", "paginas": [13], "ancestros": ["S1", "1.5", "1.5.2"]}`
- **Texto del punto ancla** (`ctacte::1.5.2.10`):

> 1.5.2.10. Las modificaciones en las condiciones pactadas –incluyendo el importe de las
> comisiones y/o cargos– deberán efectuarse de conformidad con lo dispuesto en
> el punto 2.3.4. de las normas sobre “Protección de los usuarios de servicios fi-
> nancieros”.
> Los fondos debitados indebidamente por comisiones y/o cargos deberán ser re-
> integrados a los titulares de acuerdo con lo dispuesto en el punto 2.3.5. de las
> normas sobre “Protección de los usuarios de servicios financieros”.

- **Herencia (4):**
  - [encabezado] S1 (páginas [5]):

    > Sección 1. Funcionamiento.

  - [encabezado] 1.5 (páginas [9]):

    > 1.5. Aspectos del funcionamiento a incluir en el contrato de cuenta corriente.

  - [intro] 1.5 (páginas [9]):

    > En sus cláusulas se deberá prever, como mínimo:

  - [encabezado] 1.5.2 (páginas [10]):

    > 1.5.2. Obligaciones de la entidad.

---

## 19 · índice 1907 · `establecida_en`

- **Origen:** `Obligacion_presentacion_de_tipo_y_numero_del_documento_para_establecer_su_identificacion_se_f6fcb1` · tipo `Obligacion` · label «Documentación de tipo y número de documento»
  - propiedades: `{"descripcion": "Presentación de tipo y número del documento para establecer su identificación, según lo previsto en las normas sobre 'Documentos de identificación en vigencia', debiéndose observar además lo establecido en la Sección 4. de dichas normas", "tipo": "otra", "plazo": "En cada presentación o actualización"}`
- **Relación:** `establecida_en`
- **Destino:** `TextoOrdenado_ctacte_pdf` · tipo `TextoOrdenado` · label «Cuentas a la vista»
  - propiedades: `{"materia": "Cuentas a la vista", "archivo": "ctacte.pdf", "version": "actual", "cola_humana": "true", "cola_chunks": ["ctacte::1.3.1.1", "ctacte::1.5.1.1", "ctacte::1.5.1.10", "ctacte::1.5.1.11", "ctacte::1.5.1.4", "ctacte::1.5.1.5", "ctacte::1.5.1.6", "ctacte::1.5.1.7", "ctacte::1.5.2.11", "ctacte::10.2.3::intro", "ctacte::12.1.2.5", "ctacte::3.5.2", "ctacte::4.5.1.2", "ctacte::6.4.1::intro", "ctacte::6.4.7::cierre", "ctacte::7.2.2.2", "ctacte::7.2.2.4", "ctacte::7.3.1.5"], "estado_e3": "cola_humana; cola_humana_veredicto_inutilizable", "materia_variantes": ["Cuentas a la vista", "Cuentas de corresponsalía", "Cuentas corrientes", "Identificación de titulares de cuentas corrientes", "Identificación de titulares y autorizados — cuentas corrientes", "Funcionamiento de cuentas corrientes", "cuentas_corrientes", "Identificación de titulares y personas autorizadas en cuentas corrientes", "cuentas de corresponsalía", "cuentas corrientes", "Cuentas a la vista (corrientes)", "Cuentas a la vista / Cuentas corrientes", "Cuentas Corrientes", "Movimiento de cuentas", "Cuentas a la vista (ctacte)", "Cuentas a la vista en el BCRA", "Cuentas corrientes — Tasas de interés", "Cheques", "Cheques — Títulos sin valor", "cheques", "Cheques - Títulos sin valor", "Cheques y cuentas de corresponsalía", "Cheques y sistemas de reproducción de firmas digitalizadas", "Cheques y corresponsalía", "Cheques - Reproducción de firmas digitalizadas", "Cheques librados por medios electrónicos", "Cheques de pago diferido", "Cheques de pago diferido — Cuentas de corresponsalía", "Endosos en cheques", "Endosos, modalidades especiales de emisión y aval", "Cuentas de Corresponsalía", "Cuentas de corresponsalía — Endosos, modalidades especiales de emisión y aval", "cuentas_de_corresponsalia", "Cheques — modalidades especiales de emisión", "Cheque certificado", "Rechazo de cheques — Defectos formales", "Rechazo de cheques", "ctacte", "Rechazo de cheques — Procedimiento — Motivos", "Extravío, sustracción o adulteración de cheques", "Extravío, sustracción o adulteración de cheques y otros documentos", "Cheques y documentos", "Central de cheques rechazados", "Central de cuentacorrentistas inhabilitados", "Central de cheques denunciados como extraviados, sustraídos o adulterados", "Central de cheques rechazados, Central de cuentacorrentistas inhabilitados, Central de cheques denunciados", "Cuentas a la vista — Correspondencia", "Cierre de cuentas y suspensión del servicio de pago de cheques", "Cuentas a la vista de corresponsales", "Procedimiento de cierre de cuentas", "Avisos — Contenido mínimo — Requisitos comunes", "Avisos — requisitos especiales para avisos de retención de cheques de pago diferido", "Avisos — Contenido mínimo — Requisitos especiales para cierre o suspensión", "Disposiciones generales", "Operaciones y servicios financieros", "Cuentas corrientes especiales", "transferencias", "Cooperación tributaria internacional", "Disposiciones generales - Cajeros automáticos", "cuentas de depósito", "Apertura de cuentas en forma no presencial", "cuentas corrientes no presenciales", "Procedimientos especiales de identificación de aportes a campañas electorales", "Cuentas corrientes — procedimientos especiales de identificación de aportes electorales", "Cuentas corrientes bancarias — Agrupaciones políticas"], "version_variantes": ["actual", "", "ctacte", "vigente", "3a. Comunicación A 3244"]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "ctacte", "archivo": "ctacte.pdf", "punto": "1.3.1.7", "rol_documental": "punto_propio", "chunk_id": "ctacte::1.3.1.7", "paginas": [6], "ancestros": ["S1", "1.3", "1.3.1"]}`
- **Provenances (1):**
  - `{"to": "ctacte", "archivo": "ctacte.pdf", "punto": "1.3.1.7", "rol_documental": "punto_propio", "chunk_id": "ctacte::1.3.1.7", "paginas": [6], "ancestros": ["S1", "1.3", "1.3.1"]}`
- **Texto del punto ancla** (`ctacte::1.3.1.7`):

> 1.3.1.7. Tipo y número del documento para establecer su identificación, según lo previsto
> en las normas sobre “Documentos de identificación en vigencia”, debiéndose
> observar además lo establecido en la Sección 4. de dichas normas.

- **Herencia (6):**
  - [encabezado] S1 (páginas [5]):

    > Sección 1. Funcionamiento.

  - [encabezado] 1.3 (páginas [5]):

    > 1.3. Identificación de los titulares de cuentas corrientes y de las personas autorizadas a operar en

  - [intro] 1.3 (páginas [5]):

    > ellas.

  - [encabezado] 1.3.1 (páginas [5]):

    > 1.3.1. Personas humanas (titulares, cada una de las personas a cuya orden quedará la cuenta

  - [intro] 1.3.1 (páginas [5]):

    > y representante legal, autoridades y autorizados para utilizar la cuenta en el caso de per-
    > sonas jurídicas).

  - [cierre] 1.3.1 (páginas [6]):

    > Las presentaciones o actualizaciones de los datos detallados en los puntos 1.3.1.1. a
    > 1.3.1.5. y 1.3.1.7., y de la declaración jurada prevista en el punto 1.3.1.8., podrán ser
    > realizadas presencialmente o a través de medios electrónicos de comunicación, siendo
    > de aplicación en este último caso lo previsto en el punto 12.10.

---

## 20 · índice 1992 · `aplica_a`

- **Origen:** `Obligacion_se_asegurara_de_que_la_alta_gerencia_implemente_procedimientos_para_promover_con_1b8439` · tipo `Obligacion` · label «Alta Gerencia implementar procedimientos conducta profesional»
  - propiedades: `{"descripcion": "Se asegurará de que la Alta Gerencia implemente procedimientos para promover conductas profesionales", "tipo": "otra"}`
- **Relación:** `aplica_a`
- **Destino:** `Sujeto_entidad_financiera` · tipo `Sujeto` · label «Entidades financieras»
  - propiedades: `{"nivel": "clase", "cola_humana": "true", "cola_chunks": ["lingob::2.1::intro", "lingob::6.1", "lingob::7.1.1", "lingob::7.1::intro"], "estado_e3": "cola_humana; cola_humana_veredicto_inutilizable", "alias": ["Entidades financieras del exterior", "Entidad financiera del exterior", "Entidades financieras emisoras de tarjetas de crédito y/o compra", "Entidad financiera emisora de tarjetas de crédito y/o compra"]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "lingob", "archivo": "lingob.pdf", "punto": "2.3.2", "rol_documental": "bloque_intro", "chunk_id": "lingob::2.3.2::intro", "paginas": [7], "ancestros": ["S2", "2.3"]}`
- **Provenances (1):**
  - `{"to": "lingob", "archivo": "lingob.pdf", "punto": "2.3.2", "rol_documental": "bloque_intro", "chunk_id": "lingob::2.3.2::intro", "paginas": [7], "ancestros": ["S2", "2.3"]}`
- **Texto del punto ancla** (`lingob::2.3.2::intro`):

> ductas profesionales y que prevengan y/o limiten la existencia de actividades o situacio-
> nes que puedan afectar negativamente la calidad del gobierno societario, tales como:

- **Herencia (3):**
  - [encabezado] S2 (páginas [5]):

    > Sección 2. Directorio.

  - [encabezado] 2.3 (páginas [7]):

    > 2.3. Objetivos estratégicos y valores organizacionales.

  - [encabezado] 2.3.2 (páginas [7]):

    > 2.3.2. Se asegurará de que la Alta Gerencia implemente procedimientos para promover con-

---

## 21 · índice 2027 · `establecida_en`

- **Origen:** `Obligacion_se_demostrara_con_cualquiera_de_las_siguientes_alternativas_05c68a` · tipo `Obligacion` · label «Demostración de cancelación — alternativas»
  - propiedades: `{"descripcion": "Se demostrará con cualquiera de las siguientes alternativas", "tipo": "otra"}`
- **Relación:** `establecida_en`
- **Destino:** `TextoOrdenado_ctacte_pdf` · tipo `TextoOrdenado` · label «Cuentas a la vista»
  - propiedades: `{"materia": "Cuentas a la vista", "archivo": "ctacte.pdf", "version": "actual", "cola_humana": "true", "cola_chunks": ["ctacte::1.3.1.1", "ctacte::1.5.1.1", "ctacte::1.5.1.10", "ctacte::1.5.1.11", "ctacte::1.5.1.4", "ctacte::1.5.1.5", "ctacte::1.5.1.6", "ctacte::1.5.1.7", "ctacte::1.5.2.11", "ctacte::10.2.3::intro", "ctacte::12.1.2.5", "ctacte::3.5.2", "ctacte::4.5.1.2", "ctacte::6.4.1::intro", "ctacte::6.4.7::cierre", "ctacte::7.2.2.2", "ctacte::7.2.2.4", "ctacte::7.3.1.5"], "estado_e3": "cola_humana; cola_humana_veredicto_inutilizable", "materia_variantes": ["Cuentas a la vista", "Cuentas de corresponsalía", "Cuentas corrientes", "Identificación de titulares de cuentas corrientes", "Identificación de titulares y autorizados — cuentas corrientes", "Funcionamiento de cuentas corrientes", "cuentas_corrientes", "Identificación de titulares y personas autorizadas en cuentas corrientes", "cuentas de corresponsalía", "cuentas corrientes", "Cuentas a la vista (corrientes)", "Cuentas a la vista / Cuentas corrientes", "Cuentas Corrientes", "Movimiento de cuentas", "Cuentas a la vista (ctacte)", "Cuentas a la vista en el BCRA", "Cuentas corrientes — Tasas de interés", "Cheques", "Cheques — Títulos sin valor", "cheques", "Cheques - Títulos sin valor", "Cheques y cuentas de corresponsalía", "Cheques y sistemas de reproducción de firmas digitalizadas", "Cheques y corresponsalía", "Cheques - Reproducción de firmas digitalizadas", "Cheques librados por medios electrónicos", "Cheques de pago diferido", "Cheques de pago diferido — Cuentas de corresponsalía", "Endosos en cheques", "Endosos, modalidades especiales de emisión y aval", "Cuentas de Corresponsalía", "Cuentas de corresponsalía — Endosos, modalidades especiales de emisión y aval", "cuentas_de_corresponsalia", "Cheques — modalidades especiales de emisión", "Cheque certificado", "Rechazo de cheques — Defectos formales", "Rechazo de cheques", "ctacte", "Rechazo de cheques — Procedimiento — Motivos", "Extravío, sustracción o adulteración de cheques", "Extravío, sustracción o adulteración de cheques y otros documentos", "Cheques y documentos", "Central de cheques rechazados", "Central de cuentacorrentistas inhabilitados", "Central de cheques denunciados como extraviados, sustraídos o adulterados", "Central de cheques rechazados, Central de cuentacorrentistas inhabilitados, Central de cheques denunciados", "Cuentas a la vista — Correspondencia", "Cierre de cuentas y suspensión del servicio de pago de cheques", "Cuentas a la vista de corresponsales", "Procedimiento de cierre de cuentas", "Avisos — Contenido mínimo — Requisitos comunes", "Avisos — requisitos especiales para avisos de retención de cheques de pago diferido", "Avisos — Contenido mínimo — Requisitos especiales para cierre o suspensión", "Disposiciones generales", "Operaciones y servicios financieros", "Cuentas corrientes especiales", "transferencias", "Cooperación tributaria internacional", "Disposiciones generales - Cajeros automáticos", "cuentas de depósito", "Apertura de cuentas en forma no presencial", "cuentas corrientes no presenciales", "Procedimientos especiales de identificación de aportes a campañas electorales", "Cuentas corrientes — procedimientos especiales de identificación de aportes electorales", "Cuentas corrientes bancarias — Agrupaciones políticas"], "version_variantes": ["actual", "", "ctacte", "vigente", "3a. Comunicación A 3244"]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "ctacte", "archivo": "ctacte.pdf", "punto": "8.3", "rol_documental": "bloque_intro", "chunk_id": "ctacte::8.3::intro", "paginas": [45], "ancestros": ["S8"]}`
- **Provenances (2):**
  - `{"to": "ctacte", "archivo": "ctacte.pdf", "punto": "8.3", "rol_documental": "bloque_intro", "chunk_id": "ctacte::8.3::intro", "paginas": [45], "ancestros": ["S8"]}`
  - `{"to": "ctacte", "archivo": "ctacte.pdf", "punto": "8.4", "rol_documental": "bloque_intro", "chunk_id": "ctacte::8.4::intro", "paginas": [46], "ancestros": ["S8"]}`
- **Texto del punto ancla** (`ctacte::8.3::intro`):

> Se demostrará con cualquiera de las siguientes alternativas:

- **Herencia (2):**
  - [encabezado] S8 (páginas [44]):

    > Sección 8. “Central de cheques rechazados”, “Central de cuentacorrentistas inhabili- tados” y “Central de cheques denunciados como extraviados, sustraídos o adulterados”.

  - [encabezado] 8.3 (páginas [45]):

    > 8.3. Cancelaciones de cheques rechazados.

---

## 22 · índice 2066 · `establecida_en`

- **Origen:** `Obligacion_sera_obligacion_consignar_numero_de_clave_de_identificacion_tributaria_cuit_cuil_c536ec` · tipo `Obligacion` · label «Consignar CUIT/CUIL/CDI titulares»
  - propiedades: `{"tipo": "otra", "descripcion": "Será obligación consignar número de clave de identificación tributaria (CUIT, CUIL o CDI) de los titulares de la cuenta, según los registros de la depositaria, hasta tres de sus titulares; cuando ellos excedan, además, se indicará la cantidad total"}`
- **Relación:** `establecida_en`
- **Destino:** `TextoOrdenado_ctacte_pdf` · tipo `TextoOrdenado` · label «Cuentas a la vista»
  - propiedades: `{"materia": "Cuentas a la vista", "archivo": "ctacte.pdf", "version": "actual", "cola_humana": "true", "cola_chunks": ["ctacte::1.3.1.1", "ctacte::1.5.1.1", "ctacte::1.5.1.10", "ctacte::1.5.1.11", "ctacte::1.5.1.4", "ctacte::1.5.1.5", "ctacte::1.5.1.6", "ctacte::1.5.1.7", "ctacte::1.5.2.11", "ctacte::10.2.3::intro", "ctacte::12.1.2.5", "ctacte::3.5.2", "ctacte::4.5.1.2", "ctacte::6.4.1::intro", "ctacte::6.4.7::cierre", "ctacte::7.2.2.2", "ctacte::7.2.2.4", "ctacte::7.3.1.5"], "estado_e3": "cola_humana; cola_humana_veredicto_inutilizable", "materia_variantes": ["Cuentas a la vista", "Cuentas de corresponsalía", "Cuentas corrientes", "Identificación de titulares de cuentas corrientes", "Identificación de titulares y autorizados — cuentas corrientes", "Funcionamiento de cuentas corrientes", "cuentas_corrientes", "Identificación de titulares y personas autorizadas en cuentas corrientes", "cuentas de corresponsalía", "cuentas corrientes", "Cuentas a la vista (corrientes)", "Cuentas a la vista / Cuentas corrientes", "Cuentas Corrientes", "Movimiento de cuentas", "Cuentas a la vista (ctacte)", "Cuentas a la vista en el BCRA", "Cuentas corrientes — Tasas de interés", "Cheques", "Cheques — Títulos sin valor", "cheques", "Cheques - Títulos sin valor", "Cheques y cuentas de corresponsalía", "Cheques y sistemas de reproducción de firmas digitalizadas", "Cheques y corresponsalía", "Cheques - Reproducción de firmas digitalizadas", "Cheques librados por medios electrónicos", "Cheques de pago diferido", "Cheques de pago diferido — Cuentas de corresponsalía", "Endosos en cheques", "Endosos, modalidades especiales de emisión y aval", "Cuentas de Corresponsalía", "Cuentas de corresponsalía — Endosos, modalidades especiales de emisión y aval", "cuentas_de_corresponsalia", "Cheques — modalidades especiales de emisión", "Cheque certificado", "Rechazo de cheques — Defectos formales", "Rechazo de cheques", "ctacte", "Rechazo de cheques — Procedimiento — Motivos", "Extravío, sustracción o adulteración de cheques", "Extravío, sustracción o adulteración de cheques y otros documentos", "Cheques y documentos", "Central de cheques rechazados", "Central de cuentacorrentistas inhabilitados", "Central de cheques denunciados como extraviados, sustraídos o adulterados", "Central de cheques rechazados, Central de cuentacorrentistas inhabilitados, Central de cheques denunciados", "Cuentas a la vista — Correspondencia", "Cierre de cuentas y suspensión del servicio de pago de cheques", "Cuentas a la vista de corresponsales", "Procedimiento de cierre de cuentas", "Avisos — Contenido mínimo — Requisitos comunes", "Avisos — requisitos especiales para avisos de retención de cheques de pago diferido", "Avisos — Contenido mínimo — Requisitos especiales para cierre o suspensión", "Disposiciones generales", "Operaciones y servicios financieros", "Cuentas corrientes especiales", "transferencias", "Cooperación tributaria internacional", "Disposiciones generales - Cajeros automáticos", "cuentas de depósito", "Apertura de cuentas en forma no presencial", "cuentas corrientes no presenciales", "Procedimientos especiales de identificación de aportes a campañas electorales", "Cuentas corrientes — procedimientos especiales de identificación de aportes electorales", "Cuentas corrientes bancarias — Agrupaciones políticas"], "version_variantes": ["actual", "", "ctacte", "vigente", "3a. Comunicación A 3244"]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "ctacte", "archivo": "ctacte.pdf", "punto": "1.5.2.3", "rol_documental": "punto_propio", "chunk_id": "ctacte::1.5.2.3", "paginas": [10, 11], "ancestros": ["S1", "1.5", "1.5.2"]}`
- **Provenances (1):**
  - `{"to": "ctacte", "archivo": "ctacte.pdf", "punto": "1.5.2.3", "rol_documental": "punto_propio", "chunk_id": "ctacte::1.5.2.3", "paginas": [10, 11], "ancestros": ["S1", "1.5", "1.5.2"]}`
- **Texto del punto ancla** (`ctacte::1.5.2.3`):

> 1.5.2.3. Enviar al cuentacorrentista, como máximo 8 días corridos después de finalizado
> cada mes y/o el período menor que se establezca y en las condiciones que se
> convenga, un extracto con el detalle de cada uno de los movimientos que se
> efectúen en la cuenta –débitos y créditos–, cualquiera sea su concepto, identifi-
> cando los distintos tipos de transacción mediante un código específico que cada
> entidad instrumente a tal efecto y los saldos registrados en el período que com-
> prende, pidiéndole su conformidad por escrito. También se deberán identificar en
> el correspondiente extracto las operaciones realizadas por cuenta propia o por
> cuenta de terceros, en la medida que se trate de depósitos de cheques por im-
> portes superiores a $ 1.000 y que así se encuentren identificados por el corres-
> pondiente endoso, mediante el procedimiento único que cada entidad opte por
> aplicar a tal fin.
> Adicionalmente, en el resumen se hará constar la clave bancaria uniforme (CBU)
> para que el cliente pueda formular su adhesión a servicios de débito automático,
> el plazo de compensación vigente para la operatoria de depósito de cheques y
> otros documentos compensables y el importe total debitado en el período en
> concepto de “Impuesto a las transacciones financieras”.
> En ese extracto o resumen de cuenta, adicionalmente las entidades informarán
> los siguientes datos mínimos:
> i) De producirse débitos correspondientes al servicio de débito automático:
> - Denominación de la empresa prestadora de servicios, organismo recauda-
> dor de impuestos, etc., al cual se destinaron los fondos debitados.
> - Identificación del cliente en la empresa o ente (apellido y nombre o código
> o cuenta, etc.).
> - Concepto de la operación causante del débito (mes, bimestre, cuota, etc.).
> - Importe debitado.
> - Fecha de débito.
> ii)De efectuarse transferencias:
> La información prevista en el punto 3.2. de las normas sobre “Sistema Nacio-
> nal de Pagos – Transferencias”, según corresponda.
> Se presumirá conformidad con el movimiento registrado en el banco si dentro de
> los 60 días corridos de vencido el respectivo período no se ha presentado en la
> entidad financiera la formulación de un reclamo.
> Cuando se reconozcan intereses sobre los saldos acreedores, se informarán las
> tasas nominal y efectiva, ambas anuales, correspondientes al período informado.
> Además, se hará constar la leyenda que corresponda incluir en materia de garan-
> tía de los depósitos, según lo previsto en el punto 6. de las normas sobre “Apli-
> cación del sistema de seguro de garantía de los depósitos” y, en el lugar que de-
> termine la entidad, número de clave de identificación tributaria (CUIT, CUIL o
> CDI) de los titulares de la cuenta, según los registros de la depositaria. Será obli-
> gación consignar los datos de hasta tres de sus titulares; cuando ellos excedan
> de dicho número, además, se indicará la cantidad total.

- **Herencia (4):**
  - [encabezado] S1 (páginas [5]):

    > Sección 1. Funcionamiento.

  - [encabezado] 1.5 (páginas [9]):

    > 1.5. Aspectos del funcionamiento a incluir en el contrato de cuenta corriente.

  - [intro] 1.5 (páginas [9]):

    > En sus cláusulas se deberá prever, como mínimo:

  - [encabezado] 1.5.2 (páginas [10]):

    > 1.5.2. Obligaciones de la entidad.

---

## 23 · índice 2205 · `establecida_en`

- **Origen:** `Operacion_aplicacion_de_capacidad_de_prestamo_a_titulos_de_deuda_y_certificados_de_partici_0f737a` · tipo `Operacion` · label «Aplicación de capacidad de préstamo a títulos de deuda y certificados de participación»
  - propiedades: `{"tipo": "financiación mediante títulos de deuda o certificados de participación", "descripcion": "Aplicación de la capacidad de préstamo de depósitos en moneda extranjera a títulos de deuda o certificados de participación en fideicomisos financieros cuya base son préstamos originados en los destinos previstos en los puntos 2.1.1. a 2.1.4. y el primer párrafo del punto 2.1.6., o documentos de cesión de flujo de fondos de contratos de crédito en moneda extranjera."}`
- **Relación:** `establecida_en`
- **Destino:** `TextoOrdenado_polcre_pdf` · tipo `TextoOrdenado` · label «Política de Crédito»
  - propiedades: `{"materia": "Política general de crédito", "archivo": "polcre.pdf", "version": "", "materia_variantes": ["Política general de crédito", "Política crediticia", "Política de Crédito", "Política de crédito", "Aplicación de la capacidad de préstamo de depósitos en moneda extranjera", "Aplicación de capacidad de préstamo de depósitos en moneda extranjera", "Financiaciones a productores, procesadores o acopiadores", "Aplicación de capacidad de préstamo en moneda extranjera", "Políticas de crédito", "Capacidad de préstamo de depósitos en moneda extranjera", "Aplicación de capacidad de préstamo", "Recursos propios líquidos", "Financiamiento al sector público no financiero del país", "Financiamiento a residentes en el exterior", "Financiamiento", "Préstamos de Unidades de Valor Adquisitivo (UVA)", "Préstamos de Unidades de Valor Adquisitivo", "Préstamos en UVA", "Préstamos de Unidades de Vivienda (UVI)", "Préstamos de Unidades de Vivienda actualizables por ICC", "Préstamos en Unidades de Vivienda", "Financiaciones a Grandes empresas exportadoras", "Financiaciones a Grandes empresas exportadoras — Clientes comprendidos", "Financiaciones", "Política de Créditos"], "version_variantes": ["", "actual", "vigente"]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "polcre", "archivo": "polcre.pdf", "punto": "2.1.8", "rol_documental": "punto_propio", "chunk_id": "polcre::2.1.8", "paginas": [7], "ancestros": ["S2", "2.1"]}`
- **Provenances (1):**
  - `{"to": "polcre", "archivo": "polcre.pdf", "punto": "2.1.8", "rol_documental": "punto_propio", "chunk_id": "polcre::2.1.8", "paginas": [7], "ancestros": ["S2", "2.1"]}`
- **Texto del punto ancla** (`polcre::2.1.8`):

> 2.1.8. Títulos de deuda o certificados de participación en fideicomisos financieros en moneda
> extranjera –incluidos otros derechos de cobro específicamente reconocidos en los con-
> tratos de fideicomiso constituidos o a constituirse en el marco de los préstamos que
> otorguen organismos multilaterales de crédito de los cuales la República Argentina sea
> parte–, cuyos activos fideicomitidos sean préstamos originados por las entidades finan-
> cieras en alguno de los destinos previstos en los puntos 2.1.1. a 2.1.4. y el primer párra-
> fo del punto 2.1.6. o documentos en los cuales se haya cedido al fiduciario el flujo de
> fondos en pesos o moneda extranjera, de los contratos de crédito en moneda extranjera
> en los términos y condiciones a que se refieren los citados puntos.

- **Herencia (13):**
  - [encabezado] S2 (páginas [6]):

    > Sección 2. Aplicación de la capacidad de préstamo de depósitos en moneda extranjera.

  - [encabezado] 2.1 (páginas [6]):

    > 2.1. Destinos.

  - [intro] 2.1 (páginas [6]):

    > La capacidad de préstamo de los depósitos en moneda extranjera deberá aplicarse, en la co-
    > rrespondiente moneda de captación, en forma indistinta, a los siguientes destinos:

  - [cierre] 2.1 (páginas [8]):

    > La aplicación de la capacidad de préstamo de depósitos en moneda extranjera a los destinos
    > vinculados a operaciones de importación (previstos en los puntos 2.1.6., 2.1.7. y la parte atri-
    > buible a éstos por aplicación de los puntos 2.1.8. y 2.1.9.), no podrá superar el valor que resulte
    > de la siguiente expresión:
    > C max (F / C ; 0,05)

  - [cierre] 2.1 (páginas [8]):

    > x

  - [cierre] 2.1 (páginas [8]):

    > t base base

  - [cierre] 2.1 (páginas [8]):

    > Siendo:
    > C: capacidad de préstamo del mes al que corresponda.

  - [cierre] 2.1 (páginas [8]):

    > t

  - [cierre] 2.1 (páginas [9]):

    > F : financiación de importaciones comprendidas, correspondientes al trimestre agos-
    > base

  - [cierre] 2.1 (páginas [9]):

    > to/octubre de 2008.

  - [cierre] 2.1 (páginas [9]):

    > C : capacidad de préstamo que corresponda al trimestre agosto/octubre de 2008.

  - [cierre] 2.1 (páginas [9]):

    > base

  - [cierre] 2.1 (páginas [9]):

    > Las financiaciones y capacidad de préstamo deberán ser computadas de acuerdo con lo esta-
    > blecido en el punto 2.5.

---

## 24 · índice 2519 · `establecida_en`

- **Origen:** `Operacion_operar_con_directores_administradores_y_vinculados_967f5e` · tipo `Operacion` · label «Operar con directores, administradores y vinculados»
  - propiedades: `{"tipo": "operaciones crediticias y financieras", "descripcion": "Operar con sus directores y administradores y con empresas o personas vinculadas con ellos –en los términos previstos en el punto 1.2.2. de las normas sobre \"Grandes exposiciones al riesgo de crédito\"–"}`
- **Relación:** `establecida_en`
- **Destino:** `TextoOrdenado_lingob_pdf` · tipo `TextoOrdenado` · label «Lineamientos de gobierno societario»
  - propiedades: `{"materia": "Gobierno societario", "archivo": "lingob.pdf", "version": "actual", "cola_humana": "true", "cola_chunks": ["lingob::1.2.4", "lingob::2.1::intro", "lingob::6.1", "lingob::6.2.4::intro", "lingob::7.1.1", "lingob::7.1::intro"], "estado_e3": "cola_humana; cola_humana_veredicto_inutilizable", "materia_variantes": ["Gobierno societario", "gobierno societario", "Gobierno corporativo", "Código de gobierno societario", "Gobierno de Entidades Financieras", "Gobierno corporativo de entidades financieras", "Gobierno corporativo y gestión de riesgos", "Gobierno corporativo y administración de riesgos", "Alta Gerencia", "control interno", "Gobierno corporativo y responsabilidades del Directorio", "Directorio", "Gobierno Societario — Directorio", "Gobierno societario de entidades financieras", "Gobierno corporativo y autoridades de entidades financieras", "Directorio y gobierno corporativo", "Gobierno societario y funciones del Directorio", "Gobierno corporativo y funciones del Directorio", "Gobierno societario y administración de entidades financieras", "gobierno corporativo", "Directorio de entidades financieras", "Gobierno Societario", "Directorio, independencia, gobierno corporativo", "Gobiernos corporativos", "Gobierno corporativo y estructura directiva", "Directorio — Objetivos estratégicos y valores", "Gobierno Corporativo", "línea de gobierno", "Gobierno corporativo y responsabilidades de la Alta Gerencia", "Goberanza de entidades financieras", "Gobernanza", "Lingob", "Alta Gerencia - Responsabilidades", "Autoridades de entidades financieras", "Gobernanza corporativa — Alta Gerencia", "Gobernanza — Alta Gerencia — Decisiones gerenciales", "Comités — Líneas de Gobierno", "gobiernos corporativos", "Gobernanza corporativa y comités", "Governance y Comités", "Gobierno y administración de entidades financieras", "Estructura de gobierno corporativo", "Auditoría interna", "Auditorías y controles internos", "Auditorías interna y externa. Controles internos.", "Auditoría externa", "auditoría", "auditoría externa, controles internos", "Auditorías interna y externa", "Auditorías interna y externa, controles internos", "Política de incentivos económicos al personal", "Política de incentivos económicos", "Política de incentivos al personal", "Incentivos económicos", "Incentivos económicos al personal", "incentivos económicos", "Política de transparencia — Estructura del Directorio y Alta Gerencia", "Gobierno corporativo y divulgación de información", "Gobierno societario y transparencia", "gobierno_societario", "Gobierno corporativo y transparencia", "Política de transparencia en el gobierno societario", "gobierno corporativo y transparencia", "Gobierno corporativo / Transparencia", "Gobierno corporativo y políticas organizacionales", "Política de Conocimiento de Estructura Organizacional", "Política de conozca su estructura organizacional", "Otras políticas organizacionales", "Políticas organizacionales — conocimiento de estructuras", "Política de conocimiento de la estructura organizacional", "Estructura organizacional y gestión de riesgos", "Gobierno corporativo y estructura organizacional", "Políticas organizacionales — estructuras y productos complejos", "Políticas organizacionales", "Políticas organizacionales y estructura organizacional", "Governance y políticas organizacionales", "Paridad de género en autoridades de entidades financieras"], "version_variantes": ["actual", "", "1", "TO lingob", "TO"]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "lingob", "archivo": "lingob.pdf", "punto": "2.3.2.2", "rol_documental": "punto_propio", "chunk_id": "lingob::2.3.2.2", "paginas": [8], "ancestros": ["S2", "2.3", "2.3.2"]}`
- **Provenances (1):**
  - `{"to": "lingob", "archivo": "lingob.pdf", "punto": "2.3.2.2", "rol_documental": "punto_propio", "chunk_id": "lingob::2.3.2.2", "paginas": [8], "ancestros": ["S2", "2.3", "2.3.2"]}`
- **Texto del punto ancla** (`lingob::2.3.2.2`):

> 2.3.2.2. Operar con sus directores y administradores y con empresas o personas vincu-
> ladas con ellos –en los términos previstos en el punto 1.2.2. de las normas so-
> bre “Grandes exposiciones al riesgo de crédito”–, en condiciones más favora-
> bles que las acordadas de ordinario a su clientela.

- **Herencia (6):**
  - [encabezado] S2 (páginas [5]):

    > Sección 2. Directorio.

  - [chapeau_seccion] S2 (páginas [5]):

    > Los miembros del Directorio deberán contar con los conocimientos y competencias necesarias para
    > comprender claramente sus responsabilidades y funciones dentro del gobierno societario y obrar
    > con lealtad y con la diligencia de un buen hombre de negocios en los asuntos de la entidad financie-
    > ra.
    > Se considera una buena práctica que el Directorio se conforme observando el criterio de paridad de
    > género, a efectos de potenciar la discusión y enriquecer la toma de decisiones con respecto a estra-
    > tegias, políticas y asunción de riesgos.
    > En los casos en que la presidencia del Directorio sea ejercida por un miembro que desempeña tam-
    > bién funciones ejecutivas, se adoptarán las medidas necesarias a los efectos de que las decisiones
    > se mantengan en línea con los objetivos societarios.

  - [encabezado] 2.3 (páginas [7]):

    > 2.3. Objetivos estratégicos y valores organizacionales.

  - [intro] 2.3 (páginas [7]):

    > Con ajuste al objeto social establecido por la Asamblea de accionistas, se considera como bue-
    > na práctica que el Directorio apruebe y supervise los objetivos estratégicos y los valores socie-
    > tarios, comunicándolos a toda la organización. A esos efectos, el Directorio:

  - [encabezado] 2.3.2 (páginas [7]):

    > 2.3.2. Se asegurará de que la Alta Gerencia implemente procedimientos para promover con-

  - [intro] 2.3.2 (páginas [7]):

    > ductas profesionales y que prevengan y/o limiten la existencia de actividades o situacio-
    > nes que puedan afectar negativamente la calidad del gobierno societario, tales como:

---

## 25 · índice 2569 · `establecida_en`

- **Origen:** `Operacion_presentacion_de_documento_de_viaje_mercosur_be2ab6` · tipo `Operacion` · label «Presentación de documento de viaje Mercosur»
  - propiedades: `{"tipo": "presentación de documento identificatorio", "descripcion": "Presentación de documento de viaje admitido por la Decisión Mercosur en vigencia por nacidos en Estados Partes del Mercosur o Estados Asociados"}`
- **Relación:** `establecida_en`
- **Destino:** `TextoOrdenado_docvig_pdf` · tipo `TextoOrdenado` · label «docvig»
  - propiedades: `{"materia": "documentos de identidad", "archivo": "docvig.pdf", "version": "", "cola_humana": "true", "cola_chunks": ["docvig::1.2.2", "docvig::2.2.1.1", "docvig::2.2.2.1"], "estado_e3": "cola_humana; cola_humana_veredicto_inutilizable", "materia_variantes": ["documentos de identidad", "Documentación de vigilancia", "vigilancia", "Identificación de clientes", "requisitos documentales para extranjeros", "Requisitos documentales para extranjeros", "Documentos válidos para ciudadanos de Estados Partes del Mercosur", "Documentación de identidad para extranjeros residentes", "Documentos de viaje", "requisitos documentales para extranjeros mayores de 75 años con residencia transitoria o precaria, nacidos en otros países", "docvig", "identificación de extranjeros", "Vigilancia", "Documentación de personas humanas no residentes", "Documentos de identidad y vigilancia", "Vigencia de documentos de identidad", "Rectificación de documentos de identidad", "Vigilancia de documentos de identidad", "Prevención del lavado de activos y financiamiento del terrorismo", "Verificación de identidad"], "version_variantes": ["", "actual"]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "docvig", "archivo": "docvig.pdf", "punto": "2.1.2.1", "rol_documental": "punto_propio", "chunk_id": "docvig::2.1.2.1", "paginas": [4], "ancestros": ["S2", "2.1", "2.1.2"]}`
- **Provenances (1):**
  - `{"to": "docvig", "archivo": "docvig.pdf", "punto": "2.1.2.1", "rol_documental": "punto_propio", "chunk_id": "docvig::2.1.2.1", "paginas": [4], "ancestros": ["S2", "2.1", "2.1.2"]}`
- **Texto del punto ancla** (`docvig::2.1.2.1`):

> 2.1.2.1. Nacidos en Estados Partes del Mercosur o Estados Asociados.
> - Documento Nacional de Identidad digital (DNI-d).
> - Pasaporte del país de origen.
> - Documento de viaje admitido por la Decisión Mercosur en vigencia.

- **Herencia (3):**
  - [encabezado] S2 (páginas [4]):

    > Sección 2. Para extranjeros

  - [encabezado] 2.1 (páginas [4]):

    > 2.1. De hasta 75 años al 31.12.14.

  - [encabezado] 2.1.2 (páginas [4]):

    > 2.1.2. Con menos de un año de otorgada la residencia permanente o temporaria en el país.

---

## 26 · índice 2608 · `establecida_en`

- **Origen:** `Operacion_procesamiento_de_informacion_rendicion_cuentas_544df2` · tipo `Operacion` · label «Procesamiento de información rendición cuentas»
  - propiedades: `{"tipo": "procesamiento de información", "descripcion": "El procesamiento de la información de la rendición de cuentas dará lugar a diferentes movimientos de fondos"}`
- **Relación:** `establecida_en`
- **Destino:** `TextoOrdenado_pagjub_pdf` · tipo `TextoOrdenado` · label «Pago de beneficios ANSES»
  - propiedades: `{"materia": "Pago de beneficios ANSES", "archivo": "pagjub.pdf", "version": "actual", "version_variantes": ["actual", ""], "materia_variantes": ["Pago de beneficios ANSES", "pago de beneficios ANSES"]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "pagjub", "archivo": "pagjub.pdf", "punto": "2.8", "rol_documental": "bloque_intro", "chunk_id": "pagjub::2.8::intro", "paginas": [9], "ancestros": ["S2"]}`
- **Provenances (1):**
  - `{"to": "pagjub", "archivo": "pagjub.pdf", "punto": "2.8", "rol_documental": "bloque_intro", "chunk_id": "pagjub::2.8::intro", "paginas": [9], "ancestros": ["S2"]}`
- **Texto del punto ancla** (`pagjub::2.8::intro`):

> El procesamiento de la información de la rendición de cuentas dará lugar a diferentes movi-
> mientos de fondos los que, según los casos correspondientes, se describen a continuación:

- **Herencia (2):**
  - [encabezado] S2 (páginas [5]):

    > Sección 2. Rendición de cuentas por parte de las entidades financieras.

  - [encabezado] 2.8 (páginas [9]):

    > 2.8. Liquidación de la rendición de cuentas.

---

## 27 · índice 2721 · `aplica_a`

- **Origen:** `Potestad_admitir_firmas_de_funcionarios_delegados_1e6457` · tipo `Potestad` · label «Admitir firmas de funcionarios delegados»
  - propiedades: `{"descripcion": "Alternativamente se admitirán las firmas de quienes tengan delegadas dichas funciones de acuerdo con el procedimiento previsto en el punto 1.5."}`
- **Relación:** `aplica_a`
- **Destino:** `Sujeto_rol_alcance_pagjub` · tipo `Sujeto` · label «Entidades participantes (Pago de beneficios ANSES)»
  - propiedades: `{"nivel": "rol"}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "pagjub", "archivo": "pagjub.pdf", "punto": "2.1", "rol_documental": "punto_propio", "chunk_id": "pagjub::2.1", "paginas": [5], "ancestros": ["S2"]}`
- **Provenances (1):**
  - `{"to": "pagjub", "archivo": "pagjub.pdf", "punto": "2.1", "rol_documental": "punto_propio", "chunk_id": "pagjub::2.1", "paginas": [5], "ancestros": ["S2"]}`
- **Texto del punto ancla** (`pagjub::2.1`):

> 2.1. Elementos que la conforman.
> Por cada período de pago, las entidades participantes deberán presentar una nota con un re-
> sumen de la rendición de las órdenes de pago cuyo pago le haya sido encomendado por la
> ANSES.
> Dicha nota, que deberá confeccionarse respetando el contenido y la estructura que se consigna
> en el punto 2.2., tendrá carácter de declaración jurada. Deberá presentarse en original y dupli-
> cado y estar suscripta por dos de los funcionarios responsables de la rendición de cuentas,
> conforme con el procedimiento de designación establecido en el punto 1.4. Alternativamente se
> admitirán las firmas de quienes tengan delegadas dichas funciones de acuerdo con el procedi-
> miento previsto en el punto 1.5.
> Junto con la nota deberán presentarse, por separado, dos archivos, conteniendo en un caso,
> un detalle de las órdenes de pago efectivamente abonadas y, en el otro, un detalle de las órde-
> nes de pago impagas.
> Cada uno de los citados archivos deberá ser entregado a la Gerencia de Cuentas Corrientes
> del BCRA, con las características que se especifican en el punto 2.3.

- **Herencia (1):**
  - [encabezado] S2 (páginas [5]):

    > Sección 2. Rendición de cuentas por parte de las entidades financieras.

---

## 28 · índice 2791 · `establecida_en`

- **Origen:** `Potestad_facultad_de_otorgar_nuevas_financiaciones_46ed43` · tipo `Potestad` · label «Facultad de otorgar nuevas financiaciones»
  - propiedades: `{"descripcion": "La entidad financiera podrá otorgarle nuevas financiaciones en la medida que con tales desembolsos no se supere el importe de $30.000 millones"}`
- **Relación:** `establecida_en`
- **Destino:** `TextoOrdenado_polcre_pdf` · tipo `TextoOrdenado` · label «Política de Crédito»
  - propiedades: `{"materia": "Política general de crédito", "archivo": "polcre.pdf", "version": "", "materia_variantes": ["Política general de crédito", "Política crediticia", "Política de Crédito", "Política de crédito", "Aplicación de la capacidad de préstamo de depósitos en moneda extranjera", "Aplicación de capacidad de préstamo de depósitos en moneda extranjera", "Financiaciones a productores, procesadores o acopiadores", "Aplicación de capacidad de préstamo en moneda extranjera", "Políticas de crédito", "Capacidad de préstamo de depósitos en moneda extranjera", "Aplicación de capacidad de préstamo", "Recursos propios líquidos", "Financiamiento al sector público no financiero del país", "Financiamiento a residentes en el exterior", "Financiamiento", "Préstamos de Unidades de Valor Adquisitivo (UVA)", "Préstamos de Unidades de Valor Adquisitivo", "Préstamos en UVA", "Préstamos de Unidades de Vivienda (UVI)", "Préstamos de Unidades de Vivienda actualizables por ICC", "Préstamos en Unidades de Vivienda", "Financiaciones a Grandes empresas exportadoras", "Financiaciones a Grandes empresas exportadoras — Clientes comprendidos", "Financiaciones", "Política de Créditos"], "version_variantes": ["", "actual", "vigente"]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "polcre", "archivo": "polcre.pdf", "punto": "7.1", "rol_documental": "bloque_cierre", "chunk_id": "polcre::7.1::cierre", "paginas": [19], "ancestros": ["S7"]}`
- **Provenances (1):**
  - `{"to": "polcre", "archivo": "polcre.pdf", "punto": "7.1", "rol_documental": "bloque_cierre", "chunk_id": "polcre::7.1::cierre", "paginas": [19], "ancestros": ["S7"]}`
- **Texto del punto ancla** (`polcre::7.1::cierre`):

> Cuando el cliente reúna la condición del punto 7.1.1. pero el importe total de sus financiaciones
> en pesos en el sistema financiero no supere el importe de $ 30.000 millones y no haya mante-
> nido pases y/o cauciones bursátiles tomadas –en pesos– durante los últimos 90 días corridos,
> la entidad financiera podrá otorgarle nuevas financiaciones en la medida que con tales desem-
> bolsos no se supere ese importe.
> Cuando se trate de conjuntos económicos se los considerará como un solo cliente, a cuyo
> efecto será de aplicación el punto 1.2.2. de las normas sobre “Grandes exposiciones al riesgo
> de crédito”.
> A los fines de la imputación de las financiaciones, será de aplicación lo previsto en las normas
> sobre “Grandes exposiciones al riesgo de crédito”.

- **Herencia (2):**
  - [encabezado] S7 (páginas [18]):

    > Sección 7. Financiaciones a “Grandes empresas exportadoras”.

  - [encabezado] 7.1 (páginas [18]):

    > 7.1. Clientes comprendidos.

---

## 29 · índice 3107 · `establecida_en`

- **Origen:** `Restriccion_los_certificados_de_deposito_a_plazo_fijo_solo_pueden_colocarse_en_entidades_que_191032` · tipo `Restriccion` · label «Calificación mínima AA para depósitos a plazo fijo»
  - propiedades: `{"tipo": "limite_cualitativo", "descripcion": "Los certificados de depósito a plazo fijo solo pueden colocarse en entidades que cuenten con calificación internacional no inferior a 'AA'"}`
- **Relación:** `establecida_en`
- **Destino:** `TextoOrdenado_polcre_pdf` · tipo `TextoOrdenado` · label «Política de Crédito»
  - propiedades: `{"materia": "Política general de crédito", "archivo": "polcre.pdf", "version": "", "materia_variantes": ["Política general de crédito", "Política crediticia", "Política de Crédito", "Política de crédito", "Aplicación de la capacidad de préstamo de depósitos en moneda extranjera", "Aplicación de capacidad de préstamo de depósitos en moneda extranjera", "Financiaciones a productores, procesadores o acopiadores", "Aplicación de capacidad de préstamo en moneda extranjera", "Políticas de crédito", "Capacidad de préstamo de depósitos en moneda extranjera", "Aplicación de capacidad de préstamo", "Recursos propios líquidos", "Financiamiento al sector público no financiero del país", "Financiamiento a residentes en el exterior", "Financiamiento", "Préstamos de Unidades de Valor Adquisitivo (UVA)", "Préstamos de Unidades de Valor Adquisitivo", "Préstamos en UVA", "Préstamos de Unidades de Vivienda (UVI)", "Préstamos de Unidades de Vivienda actualizables por ICC", "Préstamos en Unidades de Vivienda", "Financiaciones a Grandes empresas exportadoras", "Financiaciones a Grandes empresas exportadoras — Clientes comprendidos", "Financiaciones", "Política de Créditos"], "version_variantes": ["", "actual", "vigente"]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "polcre", "archivo": "polcre.pdf", "punto": "5.2", "rol_documental": "punto_propio", "chunk_id": "polcre::5.2", "paginas": [13], "ancestros": ["S5"]}`
- **Provenances (1):**
  - `{"to": "polcre", "archivo": "polcre.pdf", "punto": "5.2", "rol_documental": "punto_propio", "chunk_id": "polcre::5.2", "paginas": [13], "ancestros": ["S5"]}`
- **Texto del punto ancla** (`polcre::5.2`):

> 5.2. Colocaciones en bancos del exterior.
> Las entidades financieras podrán mantener en bancos del exterior cuentas de corresponsalía y
> cuentas a la vista necesarias para sus operaciones, de acuerdo con lo establecido en las nor-
> mas sobre “Cuentas de corresponsalía” y certificados de depósito a plazo fijo en entidades que
> cuenten con calificación internacional no inferior a “AA”.

- **Herencia (1):**
  - [encabezado] S5 (páginas [13]):

    > Sección 5. Financiamiento a residentes en el exterior.

---

## 30 · índice 3221 · `establecida_en`

- **Origen:** `Restriccion_no_se_admitira_que_los_cheques_lleven_mas_de_3_firmas_9e1d3b` · tipo `Restriccion` · label «Límite de firmas en cheques»
  - propiedades: `{"tipo": "limite_cuantitativo", "descripcion": "No se admitirá que los cheques lleven más de 3 firmas", "umbral": "3"}`
- **Relación:** `establecida_en`
- **Destino:** `TextoOrdenado_ctacte_pdf` · tipo `TextoOrdenado` · label «Cuentas a la vista»
  - propiedades: `{"materia": "Cuentas a la vista", "archivo": "ctacte.pdf", "version": "actual", "cola_humana": "true", "cola_chunks": ["ctacte::1.3.1.1", "ctacte::1.5.1.1", "ctacte::1.5.1.10", "ctacte::1.5.1.11", "ctacte::1.5.1.4", "ctacte::1.5.1.5", "ctacte::1.5.1.6", "ctacte::1.5.1.7", "ctacte::1.5.2.11", "ctacte::10.2.3::intro", "ctacte::12.1.2.5", "ctacte::3.5.2", "ctacte::4.5.1.2", "ctacte::6.4.1::intro", "ctacte::6.4.7::cierre", "ctacte::7.2.2.2", "ctacte::7.2.2.4", "ctacte::7.3.1.5"], "estado_e3": "cola_humana; cola_humana_veredicto_inutilizable", "materia_variantes": ["Cuentas a la vista", "Cuentas de corresponsalía", "Cuentas corrientes", "Identificación de titulares de cuentas corrientes", "Identificación de titulares y autorizados — cuentas corrientes", "Funcionamiento de cuentas corrientes", "cuentas_corrientes", "Identificación de titulares y personas autorizadas en cuentas corrientes", "cuentas de corresponsalía", "cuentas corrientes", "Cuentas a la vista (corrientes)", "Cuentas a la vista / Cuentas corrientes", "Cuentas Corrientes", "Movimiento de cuentas", "Cuentas a la vista (ctacte)", "Cuentas a la vista en el BCRA", "Cuentas corrientes — Tasas de interés", "Cheques", "Cheques — Títulos sin valor", "cheques", "Cheques - Títulos sin valor", "Cheques y cuentas de corresponsalía", "Cheques y sistemas de reproducción de firmas digitalizadas", "Cheques y corresponsalía", "Cheques - Reproducción de firmas digitalizadas", "Cheques librados por medios electrónicos", "Cheques de pago diferido", "Cheques de pago diferido — Cuentas de corresponsalía", "Endosos en cheques", "Endosos, modalidades especiales de emisión y aval", "Cuentas de Corresponsalía", "Cuentas de corresponsalía — Endosos, modalidades especiales de emisión y aval", "cuentas_de_corresponsalia", "Cheques — modalidades especiales de emisión", "Cheque certificado", "Rechazo de cheques — Defectos formales", "Rechazo de cheques", "ctacte", "Rechazo de cheques — Procedimiento — Motivos", "Extravío, sustracción o adulteración de cheques", "Extravío, sustracción o adulteración de cheques y otros documentos", "Cheques y documentos", "Central de cheques rechazados", "Central de cuentacorrentistas inhabilitados", "Central de cheques denunciados como extraviados, sustraídos o adulterados", "Central de cheques rechazados, Central de cuentacorrentistas inhabilitados, Central de cheques denunciados", "Cuentas a la vista — Correspondencia", "Cierre de cuentas y suspensión del servicio de pago de cheques", "Cuentas a la vista de corresponsales", "Procedimiento de cierre de cuentas", "Avisos — Contenido mínimo — Requisitos comunes", "Avisos — requisitos especiales para avisos de retención de cheques de pago diferido", "Avisos — Contenido mínimo — Requisitos especiales para cierre o suspensión", "Disposiciones generales", "Operaciones y servicios financieros", "Cuentas corrientes especiales", "transferencias", "Cooperación tributaria internacional", "Disposiciones generales - Cajeros automáticos", "cuentas de depósito", "Apertura de cuentas en forma no presencial", "cuentas corrientes no presenciales", "Procedimientos especiales de identificación de aportes a campañas electorales", "Cuentas corrientes — procedimientos especiales de identificación de aportes electorales", "Cuentas corrientes bancarias — Agrupaciones políticas"], "version_variantes": ["actual", "", "ctacte", "vigente", "3a. Comunicación A 3244"]}`
- **Propiedades de la arista:** `null`
- **rol_fuente:** `null`
- **Provenance:** `{"to": "ctacte", "archivo": "ctacte.pdf", "punto": "1.5.1.8", "rol_documental": "punto_propio", "chunk_id": "ctacte::1.5.1.8", "paginas": [10], "ancestros": ["S1", "1.5", "1.5.1"]}`
- **Provenances (1):**
  - `{"to": "ctacte", "archivo": "ctacte.pdf", "punto": "1.5.1.8", "rol_documental": "punto_propio", "chunk_id": "ctacte::1.5.1.8", "paginas": [10], "ancestros": ["S1", "1.5", "1.5.1"]}`
- **Texto del punto ancla** (`ctacte::1.5.1.8`):

> 1.5.1.8. Integrar los cheques en pesos o dólares estadounidenses –según corresponda–,
> redactarlos en idioma nacional y firmarlos de puño y letra o por los medios alter-
> nativos que se autoricen.
> No se admitirá que los cheques lleven más de 3 firmas.

- **Herencia (4):**
  - [encabezado] S1 (páginas [5]):

    > Sección 1. Funcionamiento.

  - [encabezado] 1.5 (páginas [9]):

    > 1.5. Aspectos del funcionamiento a incluir en el contrato de cuenta corriente.

  - [intro] 1.5 (páginas [9]):

    > En sus cláusulas se deberá prever, como mínimo:

  - [encabezado] 1.5.1 (páginas [9]):

    > 1.5.1. Obligaciones del cuentacorrentista.

