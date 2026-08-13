# Inventario de unidades, proyección de costo y catálogo de sujetos

Fase A del escalado. Gasto de esta unidad: **USD 0** (cero llamadas a LLM).

## 1. Tarifas reales del corpus v2

Fuente del gasto: `data/experiment/reextraccion_v2/corpus_v2/salida/estado_corpus.json`, clave `fases_cerradas`.
Fuente de los caracteres: `data/experiment/reextraccion_v2/e0_chunking/salida_enm01` (chunks sellados de E0).

```bash
python3 -c "import json; d=json.load(open('data/experiment/reextraccion_v2/corpus_v2/salida/estado_corpus.json'))['fases_cerradas']; print({k: (v['gasto_usd'], v['resumen']['n']) for k,v in d.items() if ':' in k})"
```

| fase | gasto USD | unidades | USD/unidad | chars propios | USD/char |
|---|--:|--:|--:|--:|--:|
| cap:e1 | 3.817296 | 462 | 0.008263 | 384104 | 9.938e-06 |
| cap:e3 | 5.622374 | 459 | 0.012249 | 384104 | 1.464e-05 |
| cla:e1 | 1.076603 | 143 | 0.007529 | 91657 | 1.175e-05 |
| cla:e3 | 1.416004 | 142 | 0.009972 | 91657 | 1.545e-05 |
| ext:e1 | 6.104854 | 973 | 0.006274 | 428690 | 1.424e-05 |
| ext:e3 | 12.321805 | 971 | 0.012690 | 428690 | 2.874e-05 |
| pro:e1  ← TO de calibración, excluido | 0.000000 | 101 | 0.000000 | 71879 | 0.000e+00 |
| pro:e3  ← TO de calibración, excluido | 0.206640 | 101 | 0.002046 | 71879 | 2.875e-06 |
| ric:e1 | 0.739057 | 84 | 0.008798 | 94665 | 7.807e-06 |
| ric:e3 | 1.133598 | 84 | 0.013495 | 94665 | 1.197e-05 |

Suma de las diez fases: USD 32.438231. Con la re-extracción dirigida (USD 0,527699, misma fuente) da el total de la corrida del corpus registrado en el commit del grafo v2 final.

`pro` queda fuera del cálculo de tarifas en ambas fases: fue el TO de calibración de
E0-E3 y entró a la corrida del corpus con la caché ya poblada — `pro:e1` costó USD 0,0
sobre 101 unidades y `pro:e3` USD 0,00205 por unidad, seis veces por debajo del
siguiente TO más barato. Los TOs nuevos no tienen caché previa.

Tarifas usadas para proyectar:

| fase | USD/unidad (agregado) | mín. por TO | máx. por TO | USD/char |
|---|--:|--:|--:|--:|
| E1 | 0.007062 | 0.006274 | 0.008798 | 1.175e-05 |
| E3 | 0.012375 | 0.009972 | 0.013495 | 2.051e-05 |

## 2. Inventario de unidades del universo nuevo

- TOs: **152** | páginas: **6757**
- Chunks terminales: **6670**
- Mini-chunks estructurales: **1340**
- **Unidades de extracción: 8010** (4464471 caracteres propios)

Referencia: el corpus de 5 TOs tiene 1.763 unidades. Detalle por TO en
`inventario_unidades.csv` (152 filas, ordenado por unidades).

## 3. Proyección de costo

| concepto | USD |
|---|--:|
| E1 sobre 8010 unidades | 56.57 |
| E3 sobre 8010 unidades | 99.13 |
| **Total (tarifa agregada)** | **155.70** |
| Banda baja (tarifa del TO más barato en cada fase) | 130.13 |
| Banda alta (tarifa del TO más caro en cada fase) | 178.57 |
| Contraste por caracteres, no por unidades | 144.02 |

Las dos vías de proyección — por unidad y por carácter — caen a 8 % una de otra, así que la tarifa por unidad no está arrastrada por una diferencia de
tamaño de unidad entre el corpus v2 y el universo nuevo.

### 3.1 Lo que esta cifra NO incluye

62 de los 152 TOs producen **cero** unidades: E0 no engancha su estructura (ver `reporte_generalizacion.md` §5). Entran a la suma con
costo 0, que es correcto para «lo que el pipeline puede extraer hoy» y falso para «lo que
cuesta el universo completo».

| corte | TOs | páginas | unidades | USD |
|---|--:|--:|--:|--:|
| digeribles | 68 | 2009 | 6340 | 123.24 |
| necesitan reglas (lo que se ve hoy) | 84 | 4748 | 1670 | 32.46 |

Extrapolación del volumen invisible: los 62 TOs sin estructura suman 3605 páginas. Aplicando la densidad de unidades por página
medida por categoría —
  - normativa_general: 3.1558 unidades/página (68 TOs digeribles de esta corrida)
  - regimen_informativo: 1.4237 unidades/página (ric del subset congelado (único TO de RI digerido))
— darían del orden de **5827 unidades** adicionales, **USD 113.27**. Es extrapolación, no medición: el volumen
real solo se conoce después de escribir las reglas de parseo.

Techo del escalado completo, sumando ambas partes: del orden de **USD 269** en E1+E3, sobre ~13837 unidades. No incluye E2 (determinístico, USD 0), re-extracción dirigida, ni reintentos por cola.

### 3.2 Los 25 TOs más caros

| TO | título | unidades | USD E1 | USD E3 | USD total | veredicto |
|---|---|--:|--:|--:|--:|---|
| lingeef | Lineamientos para la gestión de riesgos en las entid… | 613 | 4.33 | 7.59 | 11.92 | digerible |
| snp_cheq | Sistema Nacional de Pagos - Cheques y otros instrume… | 540 | 3.81 | 6.68 | 10.50 | necesita reglas |
| depaho | Depósitos de ahorro, cuenta sueldo y especiales | 437 | 3.09 | 5.41 | 8.49 | digerible |
| ctacte | Reglamentación de la cuenta corriente bancaria | 388 | 2.74 | 4.80 | 7.54 | digerible |
| cajasc | Cajas de Crédito Cooperativas (Ley 26.173) | 289 | 2.04 | 3.58 | 5.62 | digerible |
| ctavis | Cuentas a la vista abiertas en las cajas de crédito … | 275 | 1.94 | 3.40 | 5.35 | digerible |
| rdbcra | Régimen disciplinario a cargo del Banco Central de l… | 261 | 1.84 | 3.23 | 5.07 | digerible |
| cirmo3 | Circulación monetaria | 240 | 1.70 | 2.97 | 4.67 | necesita reglas |
| depinv | Depósitos e inversiones a plazo | 202 | 1.43 | 2.50 | 3.93 | digerible |
| ayccef | Autorización y composición del capital de entidades … | 196 | 1.38 | 2.43 | 3.81 | digerible |
| expaef | Expansión de entidades financieras | 165 | 1.17 | 2.04 | 3.21 | digerible |
| pimf | Principios para las infraestructuras del mercado fin… | 165 | 1.17 | 2.04 | 3.21 | digerible |
| lingob | Lineamientos para el gobierno societario en entidade… | 139 | 0.98 | 1.72 | 2.70 | digerible |
| snp_tr_nc | Sistema Nacional de Pagos - Transferencias - Normas … | 136 | 0.96 | 1.68 | 2.64 | digerible |
| ratiofn | Ratio de fondeo neto estable. | 133 | 0.94 | 1.65 | 2.59 | digerible |
| ratio | Ratio de cobertura de liquidez | 132 | 0.93 | 1.63 | 2.57 | necesita reglas |
| finsec | Financiamiento al sector público no financiero | 131 | 0.93 | 1.62 | 2.55 | digerible |
| snp_spd | Sistema Nacional de Pagos - Servicios de pago. | 129 | 0.91 | 1.60 | 2.51 | digerible |
| efemin | Efectivo mínimo | 121 | 0.85 | 1.50 | 2.35 | digerible |
| snp_cec | Sistema Nacional de Pagos - Cámaras electrónicas de … | 121 | 0.85 | 1.50 | 2.35 | digerible |
| gerc | Grandes exposiciones al riesgo de crédito. | 114 | 0.81 | 1.41 | 2.22 | digerible |
| garant | Garantías | 104 | 0.73 | 1.29 | 2.02 | necesita reglas |
| adfsp | Adelantos del Banco Central a las entidades financie… | 101 | 0.71 | 1.25 | 1.96 | digerible |
| graloc | Gestión de riesgos asociados a la liquidación de ope… | 100 | 0.71 | 1.24 | 1.94 | digerible |
| jafip | Disposiciones judiciales originadas en juicios entab… | 91 | 0.64 | 1.13 | 1.77 | necesita reglas |

## 4. Catálogo de sujetos: presión de fusión cross-TO

Proxy léxico determinístico sobre el texto que E0 extrajo, contra el catálogo cerrado de
`data/experiment/grafo_v2/esquema_v2_clases.json` (65 entradas). **No es adjudicación**: quién es sujeto de una norma lo decide E1, que no se corre en esta unidad.

Cobertura del análisis: 90 de 152 TOs producen texto; los otros no aportan evidencia léxica porque E0 no los engancha.

### 4.1 Entradas del catálogo que reaparecen en el universo nuevo

50 de las 65 entradas del catálogo aparecen en al menos un TO nuevo. Cada una de
ellas es un punto de fusión cross-TO: el ensamblado une nodos por id canónico, mecanismo
ya medido en el corpus de 5 TOs (`reporte_ensamblado.json` → `merges_cross_to`, 27 merges,
21 de tipo `Sujeto`).

| entrada del catálogo | TOs que la mencionan |
|---|--:|
| `Sujeto_entidad_financiera` | 88 |
| `Sujeto_banco` | 85 |
| `Sujeto_bcra` | 83 |
| `Sujeto_cliente` | 68 |
| `Sujeto_sefyc` | 59 |
| `Sujeto_sujeto` | 57 |
| `Sujeto_deudor` | 50 |
| `Sujeto_persona_humana` | 38 |
| `Sujeto_fideicomiso` | 32 |
| `Sujeto_persona_juridica` | 32 |
| `Sujeto_sector_publico_no_financiero` | 25 |
| `Sujeto_fideicomiso_financiero` | 21 |
| `Sujeto_arca` | 21 |
| `Sujeto_fondo_comun_de_inversion` | 20 |
| `Sujeto_contraparte` | 17 |
| `Sujeto_banco_comercial` | 15 |
| `Sujeto_sector_privado_no_financiero` | 15 |
| `Sujeto_usuario_de_servicios_financieros` | 14 |
| `Sujeto_caja_de_credito` | 13 |
| `Sujeto_proveedor_de_servicios_de_pago` | 13 |
| `Sujeto_entidad_cambiaria` | 10 |
| `Sujeto_pspcp` | 10 |
| `Sujeto_proveedor_no_financiero_de_credito` | 9 |
| `Sujeto_sociedad_de_garantia_reciproca` | 9 |
| `Sujeto_entidad_de_contraparte_central` | 8 |

### 4.2 TOs con más presión de fusión

| TO | título | unidades | entradas de catálogo distintas |
|---|---|--:|--:|
| efemin | Efectivo mínimo | 121 | 23 |
| ordcom | Ordenamiento, emisión y  divulgación de Comunicaci… | 65 | 22 |
| depaho | Depósitos de ahorro, cuenta sueldo y especiales | 437 | 21 |
| ri_rml | RI Cont. Mensual - Efectivo mínimo y aplicación de… | 27 | 21 |
| gerc | Grandes exposiciones al riesgo de crédito. | 114 | 20 |
| ratio | Ratio de cobertura de liquidez | 132 | 18 |
| servco | Servicios complementarios de la actividad financie… | 40 | 18 |
| cajasc | Cajas de Crédito Cooperativas (Ley 26.173) | 289 | 17 |
| icmecma | Comunicación por medios electrónicos para el cuida… | 47 | 17 |
| depinv | Depósitos e inversiones a plazo | 202 | 16 |
| ctavis | Cuentas a la vista abiertas en las cajas de crédit… | 275 | 15 |
| fgarcp | Fondos de garantía de carácter público | 21 | 15 |
| gescre | Gestión crediticia | 59 | 15 |
| lingeef | Lineamientos para la gestión de riesgos en las ent… | 613 | 15 |
| polcre | Política de crédito | 61 | 15 |
| ayccef | Autorización y composición del capital de entidade… | 196 | 14 |
| ctacte | Reglamentación de la cuenta corriente bancaria | 388 | 14 |
| garant | Garantías | 104 | 14 |
| gracre | Graduación del crédito | 67 | 14 |
| opecam | Operadores de cambio. | 56 | 14 |
| opefci | Operaciones al contado a liquidar y a término, pas… | 77 | 14 |
| ratiofn | Ratio de fondeo neto estable. | 133 | 14 |
| snp_mep | Sistema Nacional de Pagos - Medio electrónico de p… | 46 | 14 |
| afiltr | Asistencia financiera por iliquidez transitoria | 70 | 13 |
| fimipyme | Linea de financiamiento para la inversion producti… | 51 | 13 |

## 5. Catálogo de sujetos: candidatos a clase nueva

### 5.1 TOs cuyo título nombra un sujeto ausente del catálogo (3)

- **osapsa** (Otros servicios y actividades prestados por sujetos alcanzados) — núcleo detectado: «sujetos alcanzados»; unidades hoy: 12.
- **ri_acsf** (RI Cont. Mensual - Agencias complementarias de servicios financieros.) — núcleo detectado: «agencias complementarias de servicios»; unidades hoy: 0.
- **ri_con** (RI Cont. Mensual - Estado de Consolidación de Entidades Locales con Filiales y Subsidiarias Significativas en el País y en el Exterior.) — núcleo detectado: «entidades locales con filiales»; unidades hoy: 0.

### 5.2 Sintagmas frecuentes fuera del catálogo (40 TOs con al menos uno)

Screening: sintagma encabezado por un núcleo nominal del propio catálogo, podado de
artículos, preposiciones y verbos, con al menos 5 apariciones en el TO. Cada uno es un
candidato a adjudicar, no un sujeto confirmado.

**depaho** — Depósitos de ahorro, cuenta sueldo y especiales

- «caja de ahorros» ×12 — *La apertura de una caja de ahorros no podrá estar condicionada a la adquisición de ningún otro*
- «clientes a operar con cajeros» ×10 — *Los bancos comerciales de primer grado que habilitan a sus clientes a operar con cajeros au-*
- «fondos depositados» ×8 — *realicen con los fondos depositados en esta cuenta, según los destinos de inversión*
- «fondo de cese laboral» ×7 — *especiales de depósitos denominadas “Fondo de Cese Laboral para los Trabajadores*
- «empresa prestadora de servicios» ×6 — *vés de la empresa prestadora de servicios, organismo recaudador de impuestos, etc.,*

**snp_cheq** — Sistema Nacional de Pagos - Cheques y otros instrumentos compensables

- «entidad girada» ×49 — *los cheques y otros documentos compensables de la entidad depositaria a la entidad girada,*
- «entidad depositaria» ×34 — *los cheques y otros documentos compensables de la entidad depositaria a la entidad girada,*
- «entidad destino» ×18 — *do llegar el detalle de las transacciones a cada entidad destino.*
- «entidades giradas» ×15 — * Las entidades giradas puedan aplicar las transacciones recibidas en las cuentas de*
- «entidad originante» ×12 — * La entidad originante/depositaria.*

**manori** — Manuales de originación y administración de préstamos

- «companias aseguradoras del exterior» ×8 — *b) Sucursales locales de compañías aseguradoras del exterior respecto*
- «acreedor sus agentes» ×7 — *REALIZADOS EN CUALQUIER MOMENTO POR EL ACREEDOR, SUS AGENTES, SUCESORES Y CESIONARIOS, EN FORMA DIRECTA O A TRAVÉS DE*
- «deudor se obliga» ×7 — *II.1. Mientras subsista la Obligación Hipotecaria EL DEUDOR se obliga a:*
- «deudor bajo» ×7 — *criterio del ACREEDOR, no cubra satisfactoriamente las obligaciones del DEUDOR bajo LA*
- «deudor codeudor» ×6 — *Se denominan “Solicitantes” al conjunto de deudor, codeudor(es) y garante(s) de un*

**lingeef** — Lineamientos para la gestión de riesgos en las entidades financieras

- «fondos nocionales sujetos» ×13 — *puede alternarse entre estas dos opciones para flujos de fondos nocionales sujetos a*
- «estructura organizacional» ×8 — *procedimientos y estructura organizacional con las que deben contar las entidades finan-*
- «entidades financie ras» ×6
- «entidades tambien» ×6 — *Las entidades también deben contar con prácticas adecuadas para valuar sus activos,*
- «entidades deben desarrollar» ×5 — *rizado descripto en el punto 5.4., sino que las entidades deben desarrollar sus*

**snp_tr** — Sistema Nacional de Pagos - Transferencias.

- «entidad receptora» ×19 — *sificación de la información por entidad receptora, generando y enviando archi-*
- «proveedores y entre clientes» ×13 — *judicial. y Transferencias minoristas (Pago a proveedores y entre clientes o clientes y ter-*
- «entidad originante» ×10 — *de la información por entidad originante, generando y enviando archivos de sali-*
- «clientes y terceros nominadas» ×7 — *entre clientes o clientes y terceros, nominadas en moneda extranjera, en un plazo de 48*
- «entidad destino» ×7 — *transacciones a cada entidad destino.*

**ri_rml** — RI Cont. Mensual - Efectivo mínimo y aplicación de recursos

- «sujetos al aporte al fondo» ×20 — *Saldos inmovilizados de depósitos sujetos al Aporte al Fondo de Garantía de los de-*
- «estructura de plazos residuales» ×9 — *La determinación de la estructura de plazos residuales del mes anterior para los plazos fijos en*
- «deudores del sistema financiero» ×8 — *de deudores del sistema financiero” del BCRA. transitorias*
- «cajas de ahorro y usuras» ×6 — *102030/M Depósitos en cajas de ahorro y usuras pupilares*
- «casas operativas» ×5 — *Donde: Ps: Ponderador aplicable al promedio mensual total de los retiros de cajeros en las casas operativas, según*

**cajasc** — Cajas de Crédito Cooperativas (Ley 26.173)

- «deudores del sistema financiero» ×12 — *ción disponible en la "Central de deudores del sistema financiero".*
- «entidad del mes anterior» ×6 — *trimonial computable de la entidad del mes anterior al que corresponda. Dicho*
- «empresas proveedoras de servicios» ×5 — *emitidas por empresas proveedoras de servicios al público,*
- «clientes cuyas deudas» ×5 — *A partir de la incorporación en esta categoría de los clientes cuyas deudas hayan*

**cirmo3** — Circulación monetaria

- «fondos de seguridad con efecto» ×14 — *-Fondos de seguridad con efecto iris y fluorescentes a la luz ultravioleta.*
- «sociedad del estado casa» ×7 — *Acuñador: Sociedad del Estado Casa de Moneda – Argentina.*
- «personas con capacidades visuales» ×5 — *- Identificación para personas con capacidades visuales reducidas: en el an-*
- «personas con ceguera codigo» ×5 — *- Identificación para personas con ceguera: código con relieve perceptible al*

**ratio** — Ratio de cobertura de liquidez

- «fiduciarios de fideicomisos no financieros» ×9 — *doras y agentes regulados por la CNV, fiduciarios de fideicomisos no financieros y*
- «agentes regulados» ×7 — *aseguradoras, agentes regulados por la Comisión Nacional de Valores (C.N.V.) y fidu-*
- «empresas del sector privado» ×5 — *4.2.3. Fondeo mayorista no garantizado provisto por empresas del sector privado no financiero,*
- «aseguradoras y agentes regulados» ×5 — *rias, aseguradoras y agentes regulados por la CNV, así como a fiduciarios de fideicomi-*

**snp_dd** — Sistema Nacional de Pagos - Débitos Directos

- «entidad receptora» ×35 — *• La entidad receptora.*
- «entidad originante» ×24 — *• La entidad originante.*
- «entidades receptoras» ×7 — *• Las entidades receptoras puedan impactar las cuentas de sus clientes en base a las tran-*
- «entidad destino» ×6 — *tras que la "entidad destino" es aquella que recibe información de la misma.*

**finsec** — Financiamiento al sector público no financiero

- «fideicomisos o fondos fiduciarios» ×16 — *tor público no financiero, incluyendo los restantes fideicomisos o fondos fiduciarios en los que*
- «fideicomiso o fondo fiduciario» ×13 — *mentos de deuda emitidos por el fideicomiso o fondo fiduciario para el fi-*
- «fondos provenientes» ×5 — *rio con fondos provenientes del producido de la colocación de los instru-*

**gerc** — Grandes exposiciones al riesgo de crédito.

- «entidad prestamista» ×20 — *dos a la entidad prestamista o si su relación con ella implica la existencia de in-*
- «empresa del pais sujeta» ×6 — *i) A cada empresa del país sujeta a consolidación con la entidad*
- «contrapartes conectadas» ×5 — *to inesperado de una contraparte o un grupo de contrapartes conectadas (punto 1.2.1.) no per-*

**inspag** — Características de los instrumentos de pago que emiten las entidades financieras

- «entidad girada» ×6 — *- Primer renglón: el código de la entidad girada, el tipo de casa y el código postal del do-*
- «entidad girada codigo» ×6 — *Código entidad girada – Código Tipo de casa – Código Postal DV*
- «casa codigo postal» ×6 — *Código entidad girada – Código Tipo de casa – Código Postal DV*

**jafip** — Disposiciones judiciales originadas en juicios entablados por ARCA

- «fondos embargados» ×8 — *lores u otras medidas cautelares, o la transferencia de fondos embargados, dicho orga-*
- «cajas de seguridad» ×5 — *de inversión, cajas de seguridad y/o cualquier otro valor del que resulte titular.*
- «fondos y valores existentes» ×5 — *rá a los fondos y valores existentes a la fecha de su comunicación a las entidades y*

**ri2_ci** — Normas mínimas sobre controles internos para casas y agencias de cambio

- «autoridad equivalente» ×10 — *terno. El Directorio o autoridad equivalente es un factor crítico del ambien-*
- «estructura de control interno» ×8 — *La evaluación de la estructura de control interno de las casas y agencias de cambio*
- «autoridad de la entidad» ×5 — *máxima autoridad de la entidad, y dicho informe debe ser enviado a la UIF en*

**rmgcti** — Requisitos mínimos para la gestión y control de los riesgos de tecnología y seguridad de la información

- «entidades deberan definir» ×16 — *Las entidades deberán definir al menos un comité de gobierno de tecnología y seguridad*
- «entidades deberan implementar» ×9 — *sos, estructuras y activos de información, que las entidades deberán implementar con el propó-*
- «estructura las entidades» ×7 — *De acuerdo con sus operaciones, procesos y estructura, las entidades deberán establecer un*

**adfsp** — Adelantos del Banco Central a las entidades financieras con destino a financiaciones al sector productivo

- «fondos adjudicados» ×9 — *6.4. Solicitud de acreditación de fondos adjudicados.*
- «sector productivo» ×7 — *Banco……………….., en relación a los adelantos con destino a financiaciones al sector productivo,*

**autenf** — Autoridades de entidades financieras

- «miembros de los organos» ×5 — *1.1.1. Miembros de los órganos de administración (directores, consejeros o autoridades equi-*
- «autoridad de sucursales de entidades» ×5 — *1.1.4. Máxima autoridad de sucursales de entidades financieras del exterior.*

**cryl** — Central de registro y liquidación de instrumentos de deuda pública, regulación monetaria y fideicomisos financieros (CRyL).

- «caja de valores s» ×7 — *La instrucción a ser enviada de forma electrónica a la Caja de Valores S.A. será la misma que presentó el*
- «entidad autorregulada que resulte» ×5 — *Valores (CNV) y a la entidad autorregulada que resulte interesada, procediéndose al cobro de los arance-*

**ctacte** — Reglamentación de la cuenta corriente bancaria

- «entidad girada» ×12 — *La entidad girada procederá al rechazo por defecto formal de cada uno de los cheques*
- «banco girado» ×7 — *3.2.1.5. El nombre del banco girado y el domicilio de pago.*

**expaef** — Expansión de entidades financieras

- «agencia complementaria de servicios» ×10 — *En toda operación que se concierte, la agencia complementaria de servicios financieros deberá*
- «agencias complementarias de servicios» ×5 — *Las entidades financieras podrán delegar en agencias complementarias de servicios financie-*

**pagjub** — Pago de beneficios de la seg. soc. por cuenta de la Adm. Nacional de la Seguridad Social (ANSES)

- «entidad participante» ×15 — *BCRA, el que pondrá a disposición de la entidad participante los resultados obtenidos a través*
- «entidades participantes» ×5 — *1.1. Entidades participantes.*

**ratiofn** — Ratio de fondeo neto estable.

- «bancos centrales de otros» ×8 — *y bancos centrales de otros estados soberanos, así como aquel proveniente de*
- «sector financiero» ×6 — *A los efectos de estas normas, el término “sector financiero” comprende a las entidades finan-*

**repefe** — Representantes de entidades financieras del exterior no autorizadas para operar  en el país

- «entidad representada» ×7 — *completos del representante titular y antepuesto al de la entidad representada y su*
- «organismo de control societario» ×6 — *de sus inscripciones como tales ante el organismo de control societario local competen-*

**snp_cec** — Sistema Nacional de Pagos - Cámaras electrónicas de compensación

- «fondo de garantia mutualizada» ×5 — *Existirá un fondo de garantía mutualizada que operará en forma independiente*
- «entidad adherida» ×5 — *con cargo a una entidad adherida a otra cámara, procedimiento que deberá ser aplicado en*

Listado completo por TO en `catalogo_sujetos.json` y `catalogo_sujetos_resumen.csv`.

## 6. Qué queda abierto

- **D5 — definición del corpus.** Los 152 TOs son el universo publicado, no el corpus
  elegido. La selección es decisión pendiente con los mentores.
- El catálogo cerrado de sujetos fue construido sobre 5 TOs. Escalar sin ampliarlo
  empujaría a E1 a `sujeto_propuesto` masivo, que es exactamente lo que alimenta la
  cuarentena.
- Los TOs con veredicto «necesita reglas» no tienen todavía decisión: excluirlos,
  escribir reglas de parseo, o dejarlos para una segunda vuelta.

