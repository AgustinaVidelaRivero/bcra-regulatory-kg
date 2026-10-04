# VERIF-UNION-OPERACIONES — Anexo de la tarea 3: muestra de 20 pares no unidos

Regla (sin modelos): dos Operacion del mismo TO, en nodos distintos, son candidatas si las palabras significativas que comparten son mayoría estricta de las de cada etiqueta. Palabras significativas: tokens del slug de la etiqueta (`slugify_full`, sin acentos ni mayúsculas) fuera de una lista de 35 palabras vacías, con plural plegado (`-es` tras l, n, r, d, z o j → se quita; si no, `-s` final → se quita). Implementación: `verif_union_ops.py`, funciones `palabras` y `plegar`. Lista completa de pares: `t3_pares_todos_VERIF_UNION_OPS.json`.

Muestra: `random.Random(20261004).sample(range(n_pares), 20)` sobre los pares ordenados por TO (pro, cla, ric, cap, ext) y por id.

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

Resultado: mismo acto sí 3, no 12, dudoso 5 (suma 20).

01. [par 715, ext] **Acceso al mercado de cambios — fideicomisos** (ext::3.11.3::cierre) / **Acceso al mercado de cambios para pago diferido** (ext::10.6.5) — no. acceso de fideicomisos para garantías de deuda (3.11.3) y acceso para el pago diferido de bienes donados (10.6.5).
02. [par 221, cap] **Cálculo de exigencia de capital por riesgo de tipo de cambio** (cap::6.4.1) / **Cálculo de exposición riesgo tipo de cambio/tasa** (cap::6.4.2.2) — no. A es el cálculo de la exigencia por riesgo de tipo de cambio; B mide la exposición de un contrato a término (insumo).
03. [par 1240, ext] **Acceso al mercado de cambios para pago de capital** (ext::4.8.4.1) / **Acceso al mercado de cambios por pago deuda comercial servicios** (ext::13.1.2) — no. pago de capital de deudas elegibles para BOPREAL (4.8.4) y pago de deudas comerciales por servicios (13.1.2).
04. [par 1609, ext] **Cobro de exportación de bienes con liquidación en mercado** (ext::8.5.20.3) / **Cobro de exportaciones de bienes y servicios** (ext::14.3.2) — no. cobros liquidados durante los decretos (8.5.20.3) y cobros del VPU acumulados en cuentas sin liquidar (14.3.2).
05. [par 1124, ext] **Acceso al mercado de cambios — pagos por importaciones** (ext::10.1) / **Acceso al mercado de cambios para pago** (ext::10.4.3.6) — dudoso. (i) 10.1 es el acceso general por importaciones; 10.4.3.6 es un requisito del pago contra documentos.
06. [par 2142, ext] **Liquidación de divisas por cobro de exportaciones** (ext::7.5.1) / **Liquidación divisas exportaciones** (ext::7.2.1) — sí. mismo ingreso y liquidación de cobros de exportación: 7.2.1 lo define como imputable y 7.5.1 amplía su plazo.
07. [par 781, ext] **Acceso al mercado de cambios — garantías y avales** (ext::10.1) / **Emisión certificaciones acceso mercado de cambios** (ext::11.1.1.11) — no. acceso de entidades por garantías de importaciones (10.1) y emisión de certificaciones para 7.11 (11.1.1.11).
08. [par 2750, ext] **Registro cambiario operaciones propias** (ext::5.10.3) / **Registro de operaciones propias en fecha de efecto** (ext::5.10.2) — sí. mismo registro cambiario de operaciones propias (5.10): 5.10.2 fija la fecha (efecto sobre la PGC, ext::6.7) y 5.10.3 lo excluye para créditos y depósitos.
09. [par 519, ext] **Acceso a mercado de cambios endeudamiento** (ext::3.5.6.7) / **Acceso al mercado de cambios para pago** (ext::10.4.3.6) — no. acceso para cancelar endeudamientos financieros (3.5.6.7) y para pagar deudas comerciales de importación (10.4.3.6).
10. [par 1949, ext] **Financiación comercial para importación de bienes de capital** (ext::14.2.1.8) / **Financiaciones comerciales pagos a vista importaciones bienes** (ext::7.3.10) — dudoso. (ii) financiaciones comerciales de importaciones en dos regímenes: VPU-RIGI, bienes de capital (14.2.1.8) y mecanismo de 7.11 (7.3.10).
11. [par 593, ext] **Acceso al mercado de cambios** (ext::1.2, ext::3.5.6::cierre, ext::3.16.3.4, ext::13.1::intro) / **Acceso mercado cambios egresos VPU** (ext::14.4.1) — dudoso. (i) A reúne el acceso general (1.2) con casos particulares; B es el acceso del VPU por todo concepto (14.4.1).
12. [par 1611, ext] **Cobro de exportación de bienes con liquidación en mercado** (ext::8.5.20.3) / **Cobro exportación bienes exceptuado** (ext::7.2.5) — no. cobros liquidados durante los decretos (8.5.20.3) y cobros exceptuados de liquidar (7.2.5).
13. [par 2445, ext] **Pago de capital e intereses de deudas por importación** (ext::7.10.1.1) / **Pago importación bienes capital** (ext::10.10.2.7) — no. pago de deudas de importación aplicando cobros (7.10.1.1) y pago de bienes de capital con registro pendiente (10.10.2.7).
14. [par 1472, ext] **Boleto de cambio de venta — importaciones** (ext::10.4.5) / **Boleto de compra/venta de cambio** (ext::1.4) — dudoso. (i) 1.4 es el boleto de toda operación de cambio; 10.4.5 el boleto de los pagos con registro pendiente.
15. [par 852, ext] **Acceso al mercado de cambios — otras compras de bienes** (ext::10.1) / **Acceso al mercado de cambios para pago al exterior** (ext::10.4.2::intro, ext::10.4.3.1) — no. otras compras de bienes en el exterior (10.1) y pago de importaciones con registro pendiente (10.4.2, 10.4.3).
16. [par 876, ext] **Acceso al mercado de cambios — pago anticipado de importaciones** (ext::10.4.2.4) / **Acceso al mercado de cambios — pagos de importaciones** (ext::10.4.5) — dudoso. (i) 10.4.5 rige todo pago con registro pendiente; 10.4.2.4 es un requisito del pago anticipado.
17. [par 387, cap] **Tenencia de oro amonedado o barras buena entrega** (cap::2.12.1.3) / **Tenencia de oro amonedado o en barras** (cap::5.3.1.2) — no. mismo activo, actos distintos: tenencia propia de oro ponderada (2.12.1.3) y oro admitido como garantía (5.3.1.2).
18. [par 1019, ext] **Acceso al mercado de cambios — pago servicios no residentes** (ext::13.4.4) / **Pago servicio no residente BOPREAL** (ext::13.4.6) — sí. mismo pago de servicios hasta el 12/12/23 (13.4); 13.4.4 y 13.4.6 son dos excepciones de la misma lista.
19. [par 734, ext] **Acceso al mercado de cambios — garantías financieras** (ext::3.15.2::intro) / **Acceso al mercado de cambios — liquidación de endeudamiento** (ext::10.10.2.5) — no. acceso de entidades por garantías financieras (3.15.2) y acceso del cliente con un endeudamiento para importar (10.10.2.5).
20. [par 1094, ext] **Acceso al mercado de cambios — pagos de importaciones** (ext::10.4.5) / **Emisión de certificaciones de acceso al mercado de cambios** (ext::11.1.6.2) — no. acceso por pagos de importaciones (10.4.5) y emisión de certificaciones por la entidad de seguimiento (11.1.6.2).
