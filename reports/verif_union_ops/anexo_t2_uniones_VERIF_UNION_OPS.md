# VERIF-UNION-OPERACIONES — Anexo de la tarea 2: las 37 operaciones que unieron puntos distintos

Grafo: KG-Tanda0-Desarrollo-r2a (`ens_desarrollo_r2a/r2/kg.json`, sha256 `93a7af72…`, `f8dedd4`). Texto de cada unidad: E0 de `e0_chunking/salida_tanda0/chunks_<to>.json`. Etiqueta, tipo y descripción de cada instancia: crudo validado de `salida_dirigida/<to>/finales.jsonl` (cola humana: `extracciones_e1_compact.jsonl`). Insumo completo: `t2_insumo_VERIF_UNION_OPS.json`.

Criterio (el mismo en las dos tareas). Mismo acto = la misma acción sobre el mismo objeto
(lo que se paga, liquida, compra, certifica, clasifica o registra). No cambian el acto: requisitos,
plazos, sujetos, montos, los modos de cumplir un requisito, ni la remisión explícita al mismo punto
(«en el marco de 3.4», «encuadradas en 14.2.3»).
- correcta / sí: todas las unidades regulan ese mismo acto.
- incorrecta / no: al menos dos unidades regulan actos con distinta acción u objeto.
- dudosa / dudoso: (i) una unidad es la regla general y otra un caso particular de ella; (ii) el
  objeto es de la misma clase, pero el TO separa los casos por régimen, modalidad o fecha, con
  condiciones propias; (iii) la etiqueta nombra un medio común, con el mismo texto en todas las
  unidades, de actos distintos.

Resultado: correcta 18, incorrecta 8, dudosa 11 (suma 37).

01. **Acceso al mercado de cambios** — incorrecta. acceso para pagar cosas distintas: deudas financieras (3.5.6) y servicios de no residentes (13.1); 1.2 es la regla general.
    - unidades: ext::1.2 (punto_propio), ext::3.5.6::cierre (bloque_cierre), ext::3.16.3.4 (punto_propio), ext::13.1::intro (bloque_intro)
02. **Acceso al mercado de cambios — pago títulos deuda** — correcta. mismo acto de 3.5 (pago de deudas financieras): 3.5.1.12 es un modo de cumplir 3.5.1 y 3.5.3 fija el plazo.
    - unidades: ext::3.5.1.12 (herencia_encabezado), ext::3.5.3::intro (bloque_intro)
03. **Acceso al mercado de cambios para pago al exterior** — dudosa. (ii) pago de importaciones con registro pendiente en dos modalidades que el TO separa: anticipado (10.4.2) y contra documentos de embarque (10.4.3).
    - unidades: ext::10.4.2::intro (bloque_intro), ext::10.4.3.1 (herencia_encabezado)
04. **Boleto de venta de cambio — BOPREAL** — incorrecta. tres boletos por operaciones distintas: B26 importación de bienes (4.4), S33 servicios (4.5), I12/I13/P28 deudas con vinculadas (4.7).
    - unidades: ext::4.4.5 (herencia_encabezado), ext::4.5::cierre (bloque_cierre), ext::4.7::cierre (bloque_cierre)
    - etiquetas crudas: Boleto de venta de cambio - BOPREAL / Boleto de venta de cambio BOPREAL / Boleto de venta de cambio — BOPREAL
05. **Cancelación de financiaciones en moneda extranjera** — correcta. mismo acto (cancelar financiaciones en ME de entidades locales): 3.6.3 lo habilita para las pendientes al 30/08/19 y 3.16.1 lo exime del requisito de la ARCA.
    - unidades: ext::3.6.3 (punto_propio), ext::3.16.1 (punto_propio)
06. **Canje y/o arbitraje con fondos en moneda extranjera** — dudosa. (iii) mismo canje con fondos propios en ME, con el mismo texto, como medio de tres pagos distintos: importación a la vista, anticipo de bienes de capital y servicios.
    - unidades: ext::10.10.2.13 (punto_propio), ext::10.10.2.14 (punto_propio), ext::13.3.9 (punto_propio)
07. **Clasificación de deudores** — correcta. mismo acto: 3.2 fija la periodicidad de la clasificación y 4.5 excluye a los deudores con garantías preferidas A.
    - unidades: cla::3.2 (punto_propio), cla::4.5 (punto_propio)
08. **Clasificación de exposiciones a instrumentos** — correcta. mismo acto para dos grupos de entidades con categorías distintas; la descripción conservada nombra solo al grupo 1.
    - unidades: cap::2.11.1 (punto_propio), cap::2.11.2 (punto_propio)
09. **Clasificación en categoría Irrecuperable** — correcta. tres indicadores de la misma categoría Irrecuperable.
    - unidades: cla::6.5.5.3 (punto_propio), cla::6.5.5.4 (punto_propio), cla::6.5.5.5 (punto_propio)
    - etiquetas crudas: Clasificación en categoría Irrecuperable / Clasificación en categoría irrecuperable
10. **Cobros de exportaciones de bienes** — dudosa. (iii) la etiqueta es el título de la Sección 7; 7.10 y 7.11 regulan la aplicación de cobros a operaciones distintas.
    - unidades: ext::7.10::intro (bloque_intro), ext::7.11::intro (bloque_intro)
11. **Compra de instrumentos** — incorrecta. objeto y acción distintos: compra por la entidad de instrumentos del CA (8.3.2.10) y compra con su financiación de instrumentos del PNc (8.3.3.9).
    - unidades: cap::8.3.2.10 (punto_propio), cap::8.3.3.9 (punto_propio)
12. **Compra de moneda extranjera para garantías** — dudosa. (ii) misma compra de ME para garantías en dos regímenes de 3.11: endeudamientos en general (3.11.1) y los de 7.9 (3.11.3, al que remite 7.9.6).
    - unidades: ext::3.11.1.5 (herencia_encabezado), ext::3.11.3.1 (herencia_encabezado), ext::7.9.6 (punto_propio)
13. **Emisión de certificación de aplicación** — dudosa. (i) 9.5 fija el contenido de toda certificación de aplicación; 9.3.10.5 es una condición del caso de repatriaciones.
    - unidades: ext::9.3.10.5 (herencia_encabezado), ext::9.5 (punto_propio)
14. **Emisión de certificación de aumento de exportaciones** — correcta. mismo acto: 3.18.2.4 es uno de los requisitos que enumera 3.18.2.
    - unidades: ext::3.18.2::intro (bloque_intro), ext::3.18.2.4 (punto_propio)
    - etiquetas crudas: Emisión de Certificación de aumento de exportaciones / Emisión de certificación de aumento de exportaciones
15. **Emisión de certificaciones de aplicación** — incorrecta. certificaciones para cancelar financiaciones de distinta clase: de exportación (9.3.1, 9.3.4) y asociadas a importaciones (9.3.13); 9.3 es la regla general.
    - unidades: ext::9.3::intro (bloque_intro), ext::9.3.1.2 (punto_propio), ext::9.3.4 (punto_propio), ext::9.3.13 (punto_propio)
16. **Emisión de certificaciones de aplicación de divisas** — incorrecta. certificaciones para cancelar financiaciones distintas: posfinanciaciones de entidades locales (9.3.5) y préstamos financieros vigentes al 31/08/19 (9.3.7).
    - unidades: ext::9.3.5::intro (bloque_intro), ext::9.3.7 (punto_propio)
17. **Evaluación de capacidad de repago** — correcta. mismo acto: 4.4 excluye la evaluación con garantías preferidas A y 3.4.2 dispensa el legajo por esa misma causa.
    - unidades: cla::3.4.2 (punto_propio), cla::4.4 (punto_propio)
18. **Financiación especializada grandes proyectos infraestructura** — correcta. mismo objeto: 2.7.2.2 lo define y 2.12.5.3 le asigna el ponderador (130 %).
    - unidades: cap::2.7.2.2 (punto_propio), cap::2.12.5.3 (punto_propio)
19. **Financiaciones en moneda extranjera por EF locales** — dudosa. (ii) financiaciones en ME de entidades locales en el régimen general (3.6.1.1) y en el del VPU-RIGI (14.2.1.5, solo las no fondeadas con líneas del exterior).
    - unidades: ext::3.6.1.1 (punto_propio), ext::14.2.1.5 (punto_propio)
20. **Giro de divisas al exterior — utilidades y dividendos** — correcta. mismo acto de 3.4: 3.4.4.6 es una de las situaciones de 3.4.4.
    - unidades: ext::3.4::intro (bloque_intro), ext::3.4.4.6 (punto_propio)
21. **Identificación del cliente por canales electrónicos** — correcta. mismo acto: la introducción de 5.4.2 enumera los medios de identificación y 5.4.2.2 es uno de ellos.
    - unidades: ext::5.4.2::intro (bloque_intro), ext::5.4.2.2 (punto_propio)
22. **Ingreso y liquidación de divisas en mercado de cambios** — incorrecta. objetos distintos: fondos de un endeudamiento financiero (3.5.1) y cobros de exportación (7.1.1.1).
    - unidades: ext::3.5.1::intro (bloque_intro), ext::7.1.1.1 (punto_propio)
23. **Ingreso y liquidación divisas exportación** — correcta. mismo acto de 7.1.1; 7.1.1.2 y 7.1.1.4 fijan plazos por tipo de bien.
    - unidades: ext::7.1.1::intro (bloque_intro), ext::7.1.1.2 (punto_propio), ext::7.1.1.4 (punto_propio)
24. **Liquidación en mercado de cambios** — incorrecta. tres fondos distintos: sobrantes de garantías (3.11.4), cobros de activos en el exterior (3.16.2.2) y anticipos y financiaciones de exportación (7.1.3).
    - unidades: ext::3.11.4 (punto_propio), ext::3.16.2.2 (punto_propio), ext::7.1.3 (punto_propio)
25. **Liquidación simultánea de financiaciones en moneda extranjera** — dudosa. (iii) mismo medio, con el mismo texto, de dos pagos distintos: importación a la vista (10.10.2.13) y anticipo de bienes de capital (10.10.2.14).
    - unidades: ext::10.10.2.13 (punto_propio), ext::10.10.2.14 (punto_propio)
26. **Operaciones de financiación con títulos valores (pase)** — correcta. mismo tipo de operación (pase); cada punto regula un subconjunto: sin CCP con NBFI (5.2.2.6), bajo acuerdo de neteo (5.3.2.5).
    - unidades: cap::5.2.2.6 (punto_propio), cap::5.3.2.5 (punto_propio)
27. **Operaciones DvP fallidas** — correcta. mismo objeto: 2.12.13 remite a 4.1 y 4.1.1 fija la exigencia.
    - unidades: cap::2.12.13 (punto_propio), cap::4.1.1 (punto_propio)
28. **Pago de servicios de no residentes** — dudosa. (ii) pago de servicios en dos regímenes por fecha de prestación: desde el 13/12/23 con anticipación (13.3.7) y hasta el 12/12/23 (13.4.7, 13.4.8).
    - unidades: ext::13.3.7 (punto_propio), ext::13.4.7 (punto_propio), ext::13.4.8 (punto_propio)
29. **Pago de utilidades y dividendos a accionistas no residentes** — dudosa. (ii) utilidades a accionistas no residentes por dos vías: aplicación de cobros en el marco de 7.10 (9.3.12) y acceso del VPU (14.2.2).
    - unidades: ext::9.3.12::intro (bloque_intro), ext::14.2.2 (punto_propio)
30. **Pagos de utilidades y dividendos a accionistas no residentes** — correcta. mismo acto, con los requisitos de 3.4.1 a 3.4.3; 3.17 y 3.18 son dos certificaciones que habilitan el acceso por su monto.
    - unidades: ext::3.17.1.4 (punto_propio), ext::3.18.1.2 (punto_propio)
31. **Repatriación de aportes inversión directa** — correcta. mismo acto (repatriación aplicando cobros, 7.9): 3.13.2 la admite y 9.3.10.2 condiciona su certificación.
    - unidades: ext::3.13.2 (punto_propio), ext::9.3.10.2 (punto_propio)
32. **Repatriación de aportes inversión directa VPU-RIGI** — correcta. las dos unidades nombran las repatriaciones «encuadradas en el punto 14.2.3».
    - unidades: ext::3.13.1.11 (punto_propio), ext::7.9.1.7 (punto_propio)
33. **Repatriación inversión directa no residentes** — dudosa. (ii) misma repatriación en tres casos con condiciones propias: aporte desde el 02/10/20 (3.13.1.7), plan gas (3.13.1.8) y certificación del Decreto 277/22 (3.17.1.6).
    - unidades: ext::3.13.1.7 (punto_propio), ext::3.13.1.8 (punto_propio), ext::3.17.1.6 (punto_propio)
34. **Repatriación inversiones portafolio — no residentes** — correcta. mismo acto y mismo medio (canje con cobros de BOPREAL) en 3.13.1.13 y 4.8.1.4.
    - unidades: ext::3.13.1.13 (punto_propio), ext::4.8.1.4 (punto_propio)
35. **Seguimiento de permiso de embarque** — correcta. mismo acto de la Sección 8: dar por cumplido el seguimiento (8.5, 8.5.19) y reportarlo (8.4.3).
    - unidades: ext::8.4.3::cierre (bloque_cierre), ext::8.5::intro (bloque_intro), ext::8.5.19::intro (bloque_intro)
36. **Suscripción de Bonos BOPREAL** — incorrecta. suscripción por deudas de distinta clase: importaciones de bienes (4.4.2) y utilidades pendientes o cobradas (3.4, 4.6.2.3).
    - unidades: ext::3.4::cierre (bloque_cierre), ext::4.4.2 (herencia_encabezado), ext::4.6.2.3 (herencia_encabezado)
    - etiquetas crudas: Suscripción de Bonos BOPREAL / Suscripción de bonos BOPREAL
37. **Venta de divisas con débito en cuentas** — dudosa. (iii) mismo requisito, con el mismo texto, en tres pagos de importaciones: con registro en el SEPAIMPO (10.3.2), anticipado (10.4.2) y contra documentos (10.4.3).
    - unidades: ext::10.3.2.2 (punto_propio), ext::10.4.2.3 (punto_propio), ext::10.4.3.5 (punto_propio)
