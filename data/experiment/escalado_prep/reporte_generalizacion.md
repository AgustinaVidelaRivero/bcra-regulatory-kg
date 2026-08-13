# Reporte de generalización del parser E0 sobre el universo de TOs del BCRA

Corrida EN SECO (código determinístico puro, cero llamadas a LLM, gasto USD 0) del
E0 calibrado sobre los 5 TOs del subset — `data/experiment/reextraccion_v2/e0_chunking/`,
invocado sin editar — aplicado a los TOs del índice oficial del BCRA que NO están en el
subset congelado.

## 1. Alcance y reproducción

- TOs del inventario: **152** (`inventario_tos.csv`).
- TOs con E0 corrido: **152**. TOs que abortaron: **0**.
- Veredicto **digerible**: 68. Veredicto **necesita reglas**: 84.

```bash
python3 code/construir_inventario.py     # inventario desde el índice oficial congelado
python3 code/descargar_pdfs.py           # PDFs a pdfs/ (idempotente)
python3 code/referencia_subset.py        # banda de referencia + paridad con salida_enm01
python3 code/correr_e0_seco.py           # E0 + censo en seco sobre pdfs/
python3 code/reporte_generalizacion.py   # este documento
```

## 2. Banda de referencia y umbrales

El driver de esta unidad reproduce **byte a byte** los chunks sellados de los 5 TOs del
subset (`referencia_subset.json`, campo `paridad_con_salida_enm01.identicos`): es el mismo
E0, no una reimplementación. Los umbrales son el **peor valor observado en esos 5 TOs**,
que son la única evidencia empírica de que un TO se digiere de punta a punta.

| criterio | umbral (peor del subset) |
|---|---|
| H1 cobertura exacta de líneas | debe ser verdadera |
| H2 estructura enganchada | ≥1 sección y ≥1 chunk terminal |
| H3 fronteras intra-palabra tras regla 2 | 0 |
| C4 rechazos de header por unidad | ≤ 0.2143 |
| C5 tasa de puntos anunciados sin cuerpo | ≤ 0.0556 (y ≤1 en absoluto) |
| C6 % de chunks con contenido tabular | ≤ 20.24 % |
| C7 avisos de parseo por unidad | ≤ 0.2500 |
| C8 chunk terminal más grande | ≤ 26182 chars |

Valores del subset, uno por uno:

| TO | unid. | cobertura | rech./u | anunc. sin cuerpo | % tabular | avisos/u | max chars |
|---|--:|:--:|--:|--:|--:|--:|--:|
| pro | 101 | OK | 0.0297 | 0/16 | 0.00 | 0.0099 | 4764 |
| cla | 143 | OK | 0.0280 | 0/35 | 0.00 | 0.0210 | 5789 |
| ric | 84 | OK | 0.2143 | 1/18 | 20.24 | 0.2500 | 6872 |
| cap | 462 | OK | 0.0931 | 0/51 | 2.81 | 0.0649 | 26182 |
| ext | 973 | OK | 0.0678 | 0/115 | 0.10 | 0.0031 | 4588 |

## 3. TOs que abortaron E0

Ninguno: E0 corrió de punta a punta sobre los 152 TOs del inventario.

## 4. Tabla por TO

`unid.` = chunks terminales + mini-chunks estructurales (unidades de extracción de E1).
`idx a/b` = puntos anunciados por el índice sin cuerpo / puntos que el índice declara.
`cuerpo s/a` = unidades del cuerpo que el índice no anuncia.
`front.` = fronteras intra-palabra antes → después de la regla 2.

| TO | título | pág | sec | term | mini | unid. | idx a/b | cuerpo s/a | rech. | front. | % tab | fórm | max chars | veredicto |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| lingeef | Lineamientos para la gestión de riesgos en las entidades fin… | 172 | 12 | 503 | 110 | 613 | 0/61 | 0 | 6 | 118→0 | 0.3 | 9 | 13393 | digerible |
| snp_cheq | Sistema Nacional de Pagos - Cheques y otros instrumentos com… | 159 | 8 | 189 | 351 | 540 | 0/29 | 0 | 285 | 64→0 | 4.1 | 4 | 13501 | **necesita reglas** |
| depaho | Depósitos de ahorro, cuenta sueldo y especiales | 107 | 5 | 386 | 51 | 437 | 1/71 | 4 | 17 | 22→0 | 0.0 | 1 | 2854 | digerible |
| ctacte | Reglamentación de la cuenta corriente bancaria | 86 | 13 | 336 | 52 | 388 | 0/64 | 3 | 6 | 29→0 | 0.0 | 1 | 2870 | digerible |
| cajasc | Cajas de Crédito Cooperativas (Ley 26.173) | 68 | 11 | 256 | 33 | 289 | 0/72 | 1 | 16 | 16→0 | 1.0 | 0 | 3703 | digerible |
| ctavis | Cuentas a la vista abiertas en las cajas de crédito cooperat… | 54 | 11 | 238 | 37 | 275 | 0/43 | 2 | 5 | 14→0 | 0.0 | 1 | 3285 | digerible |
| rdbcra | Régimen disciplinario a cargo del Banco Central de la Repúbl… | 54 | 11 | 218 | 43 | 261 | 0/0 | 0 | 40 | 14→0 | 1.9 | 2 | 1778 | digerible |
| cirmo3 | Circulación monetaria | 107 | 6 | 215 | 25 | 240 | 12/21 | 54 | 131 | 95→0 | 20.4 | 0 | 25270 | **necesita reglas** |
| depinv | Depósitos e inversiones a plazo | 53 | 4 | 186 | 16 | 202 | 1/40 | 0 | 4 | 7→0 | 0.0 | 3 | 1778 | digerible |
| ayccef | Autorización y composición del capital de entidades financie… | 47 | 7 | 169 | 27 | 196 | 0/42 | 0 | 4 | 2→0 | 1.0 | 0 | 5657 | digerible |
| expaef | Expansión de entidades financieras | 37 | 11 | 142 | 23 | 165 | 1/45 | 4 | 4 | 2→0 | 0.0 | 0 | 1489 | digerible |
| pimf | Principios para las infraestructuras del mercado financiero. | 29 | 5 | 140 | 25 | 165 | 0/28 | 0 | 0 | 13→0 | 0.0 | 0 | 1880 | digerible |
| lingob | Lineamientos para el gobierno societario en entidades financ… | 24 | 8 | 118 | 21 | 139 | 0/20 | 0 | 2 | 5→0 | 0.0 | 0 | 1544 | digerible |
| snp_tr_nc | Sistema Nacional de Pagos - Transferencias - Normas compleme… | 31 | 6 | 131 | 5 | 136 | 0/17 | 15 | 8 | 17→0 | 1.5 | 0 | 2376 | digerible |
| ratiofn | Ratio de fondeo neto estable. | 29 | 7 | 125 | 8 | 133 | 0/16 | 0 | 8 | 10→0 | 0.0 | 1 | 1498 | digerible |
| ratio | Ratio de cobertura de liquidez | 46 | 9 | 112 | 20 | 132 | 0/24 | 0 | 3 | 28→0 | 0.0 | 2 | 2964 | **necesita reglas** |
| finsec | Financiamiento al sector público no financiero | 62 | 9 | 113 | 18 | 131 | 0/16 | 13 | 7 | 18→0 | 0.8 | 2 | 5003 | digerible |
| snp_spd | Sistema Nacional de Pagos - Servicios de pago. | 32 | 9 | 104 | 25 | 129 | 0/34 | 4 | 1 | 3→0 | 0.0 | 0 | 1588 | digerible |
| efemin | Efectivo mínimo | 53 | 7 | 97 | 24 | 121 | 0/20 | 12 | 7 | 11→0 | 5.8 | 3 | 3026 | digerible |
| snp_cec | Sistema Nacional de Pagos - Cámaras electrónicas de compensa… | 34 | 9 | 107 | 14 | 121 | 0/0 | 0 | 4 | 24→0 | 0.0 | 0 | 3981 | digerible |
| gerc | Grandes exposiciones al riesgo de crédito. | 46 | 6 | 96 | 18 | 114 | 0/25 | 0 | 4 | 32→0 | 0.0 | 0 | 5384 | digerible |
| garant | Garantías | 25 | 4 | 93 | 11 | 104 | 0/8 | 1 | 3 | 7→0 | 0.0 | 0 | 1871 | **necesita reglas** |
| adfsp | Adelantos del Banco Central a las entidades financieras con … | 41 | 7 | 96 | 5 | 101 | 0/25 | 11 | 8 | 18→0 | 1.0 | 1 | 5501 | digerible |
| graloc | Gestión de riesgos asociados a la liquidación de operaciones… | 30 | 8 | 76 | 24 | 100 | 0/23 | 0 | 0 | 3→0 | 0.0 | 0 | 4434 | digerible |
| jafip | Disposiciones judiciales originadas en juicios entablados po… | 31 | 11 | 80 | 11 | 91 | 0/32 | 5 | 21 | 3→0 | 0.0 | 1 | 5383 | **necesita reglas** |
| snp_tr | Sistema Nacional de Pagos - Transferencias. | 62 | 4 | 79 | 10 | 89 | 2/12 | 2 | 119 | 31→0 | 9.0 | 0 | 7734 | **necesita reglas** |
| snp_psp | Proveedores de servicios de pago | 23 | 7 | 76 | 12 | 88 | 0/16 | 5 | 1 | 7→0 | 0.0 | 0 | 4344 | digerible |
| repefe | Representantes de entidades financieras del exterior no auto… | 25 | 9 | 77 | 10 | 87 | 0/20 | 7 | 2 | 2→0 | 0.0 | 0 | 1593 | digerible |
| opefci | Operaciones al contado a liquidar y a término, pases, caucio… | 33 | 8 | 71 | 6 | 77 | 0/33 | 0 | 0 | 9→0 | 0.0 | 0 | 3109 | digerible |
| rrci | Lineamientos para la respuesta y recuperación ante ciberinci… | 20 | 3 | 66 | 11 | 77 | 0/15 | 0 | 0 | 1→0 | 0.0 | 0 | 1759 | digerible |
| autenf | Autoridades de entidades financieras | 25 | 7 | 63 | 12 | 75 | 0/24 | 1 | 2 | 5→0 | 0.0 | 0 | 2140 | digerible |
| inspag | Características de los instrumentos de pago que emiten las e… | 60 | 3 | 64 | 11 | 75 | 18/55 | 7 | 18 | 4→0 | 4.0 | 3 | 2594 | **necesita reglas** |
| adrei | Agregación de datos sobre riesgos y elaboración de informes. | 19 | 5 | 49 | 21 | 70 | 0/15 | 0 | 0 | 1→0 | 0.0 | 0 | 1456 | digerible |
| afiltr | Asistencia financiera por iliquidez transitoria | 40 | 4 | 56 | 14 | 70 | 0/16 | 10 | 7 | 17→0 | 0.0 | 0 | 10129 | digerible |
| snp_debin | Sistema Nacional de Pagos - Débito Inmediato | 22 | 6 | 65 | 5 | 70 | 0/20 | 2 | 0 | 14→0 | 0.0 | 0 | 2332 | digerible |
| gracre | Graduación del crédito | 28 | 8 | 61 | 6 | 67 | 0/22 | 0 | 1 | 1→0 | 0.0 | 0 | 2171 | digerible |
| supcon | Supervisión consolidada | 21 | 6 | 54 | 13 | 67 | 0/21 | 2 | 3 | 0→0 | 0.0 | 0 | 1515 | digerible |
| tasint | Tasas de interés en las operaciones de crédito | 29 | 7 | 61 | 6 | 67 | 0/30 | 1 | 1 | 4→0 | 1.5 | 2 | 1932 | digerible |
| ordcom | Ordenamiento, emisión y  divulgación de Comunicaciones y Com… | 22 | 4 | 60 | 5 | 65 | 0/20 | 0 | 1 | 11→0 | 0.0 | 0 | 3111 | digerible |
| cryl | Central de registro y liquidación de instrumentos de deuda p… | 31 | 12 | 51 | 13 | 64 | 0/34 | 0 | 2 | 5→0 | 1.6 | 0 | 2441 | digerible |
| polcre | Política de crédito | 32 | 10 | 55 | 6 | 61 | 0/26 | 0 | 4 | 5→0 | 0.0 | 3 | 1714 | digerible |
| actgar | Afectación de activos en garantía | 18 | 3 | 52 | 8 | 60 | 0/17 | 0 | 4 | 0→0 | 0.0 | 0 | 1385 | digerible |
| gescre | Gestión crediticia | 35 | 6 | 57 | 2 | 59 | 0/25 | 0 | 4 | 16→0 | 0.0 | 0 | 7095 | digerible |
| opecam | Operadores de cambio. | 32 | 7 | 53 | 3 | 56 | 4/20 | 2 | 7 | 14→0 | 3.6 | 0 | 5310 | **necesita reglas** |
| snp_dd | Sistema Nacional de Pagos - Débitos Directos | 68 | 6 | 46 | 7 | 53 | 13/25 | 0 | 144 | 35→0 | 5.7 | 0 | 41031 | **necesita reglas** |
| pagjub | Pago de beneficios de la seg. soc. por cuenta de la Adm. Nac… | 16 | 3 | 43 | 9 | 52 | 0/18 | 0 | 0 | 1→0 | 0.0 | 1 | 2146 | digerible |
| pfmipyme | Plataformas para el financiamiento MiPyME | 14 | 5 | 47 | 5 | 52 | 0/13 | 2 | 1 | 2→0 | 0.0 | 0 | 634 | digerible |
| prevmi | Previsiones mínimas por riesgo de incobrabilidad | 25 | 5 | 48 | 4 | 52 | 0/13 | 1 | 7 | 3→0 | 1.9 | 0 | 2762 | digerible |
| fimipyme | Linea de financiamiento para la inversion productiva de MiPy… | 25 | 10 | 44 | 7 | 51 | 1/19 | 5 | 1 | 4→0 | 0.0 | 0 | 2639 | digerible |
| icmecma | Comunicación por medios electrónicos para el cuidado del med… | 27 | 5 | 45 | 2 | 47 | 0/18 | 0 | 8 | 13→0 | 0.0 | 0 | 2564 | digerible |
| snp_mep | Sistema Nacional de Pagos - Medio electrónico de pagos (MEP) | 50 | 8 | 36 | 10 | 46 | 8/25 | 25 | 1 | 16→0 | 4.3 | 0 | 49553 | **necesita reglas** |
| ri2_ci | Normas mínimas sobre controles internos para casas y agencia… | 26 | 5 | 36 | 9 | 45 | 1/8 | 5 | 0 | 27→0 | 0.0 | 0 | 11010 | digerible |
| fabcra | Firmas Autorizadas ante el BCRA | 19 | 3 | 35 | 7 | 42 | 0/14 | 0 | 9 | 13→0 | 7.1 | 0 | 2576 | digerible |
| garopt | Garantías por intermediación en operaciones entre terceros | 15 | 2 | 36 | 5 | 41 | 4/16 | 9 | 21 | 0→0 | 0.0 | 0 | 2578 | **necesita reglas** |
| raapal | Ratio de apalancamiento. | 20 | 3 | 35 | 5 | 40 | 0/8 | 0 | 3 | 9→0 | 0.0 | 4 | 5361 | digerible |
| retype | Pago de retiros y pensiones militares | 13 | 4 | 34 | 6 | 40 | 0/14 | 0 | 5 | 0→0 | 0.0 | 0 | 601 | digerible |
| servco | Servicios complementarios de la actividad financiera y activ… | 14 | 3 | 37 | 3 | 40 | 0/8 | 0 | 0 | 0→0 | 0.0 | 0 | 1488 | digerible |
| coltit | Colocación de títulos valores de deuda y obtención de líneas… | 13 | 2 | 37 | 2 | 39 | 0/11 | 0 | 1 | 0→0 | 0.0 | 0 | 896 | digerible |
| disres | Distribución de resultados | 22 | 7 | 31 | 7 | 38 | 0/3 | 16 | 2 | 9→0 | 5.3 | 0 | 3407 | digerible |
| relact | Relación para los activos inmovilizados y otros conceptos | 20 | 6 | 38 | 0 | 38 | 0/15 | 0 | 2 | 0→0 | 0.0 | 0 | 1348 | digerible |
| ri_cc | RI para Cajas de Crédito - contable | 118 | 6 | 30 | 3 | 33 | 16/28 | 18 | 61 | 21→0 | 18.2 | 7 | 10132 | **necesita reglas** |
| ccbcra | Cuentas corrientes y otras cuentas a la vista de las entidad… | 19 | 4 | 30 | 2 | 32 | 0/12 | 0 | 0 | 3→0 | 0.0 | 0 | 944 | digerible |
| rmgcti | Requisitos mínimos para la gestión y control de los riesgos … | 58 | 6 | 27 | 5 | 32 | 34/46 | 0 | 52 | 128→0 | 0.0 | 0 | 18491 | **necesita reglas** |
| docvig | Documentos de identificación en vigencia | 14 | 4 | 29 | 2 | 31 | 0/7 | 6 | 1 | 0→0 | 0.0 | 0 | 1146 | digerible |
| rmrtsd | Requisitos mínimos ges. y ctrol. tec. y seg. de la inf. asoc… | 20 | 5 | 25 | 6 | 31 | 0/9 | 1 | 1 | 33→0 | 0.0 | 0 | 3238 | digerible |
| lavdin | Prevención del lavado de activos, del financiamiento del ter… | 19 | 4 | 25 | 4 | 29 | 0/9 | 0 | 0 | 0→0 | 0.0 | 0 | 1204 | digerible |
| fclef | Fideicomisos financieros comprendidos en la Ley de Entidades… | 12 | 6 | 24 | 4 | 28 | 0/10 | 4 | 0 | 0→0 | 0.0 | 2 | 818 | digerible |
| traval | Transportadoras de valores | 15 | 5 | 22 | 6 | 28 | 0/5 | 5 | 0 | 2→0 | 3.6 | 0 | 1222 | digerible |
| apnf | Proveedores no financieros de crédito. | 15 | 3 | 21 | 6 | 27 | 0/9 | 0 | 2 | 8→0 | 3.7 | 0 | 2590 | digerible |
| ri_rml | RI Cont. Mensual - Efectivo mínimo y aplicación de recursos | 77 | 6 | 26 | 1 | 27 | 0/11 | 3 | 128 | 30→0 | 44.4 | 18 | 65711 | **necesita reglas** |
| incuca | Incumplimientos de capitales mínimos y relaciones técnicas. … | 12 | 3 | 23 | 0 | 23 | 0/12 | 0 | 0 | 2→0 | 0.0 | 0 | 1231 | digerible |
| pscpp | Proveedores de servicios de créditos entre particulares a tr… | 10 | 3 | 19 | 3 | 22 | 0/9 | 0 | 1 | 1→0 | 0.0 | 0 | 1671 | digerible |
| secfin | Secreto financiero | 10 | 4 | 17 | 5 | 22 | 0/0 | 0 | 0 | 1→0 | 0.0 | 0 | 845 | digerible |
| cescar | Cesión de cartera de créditos | 10 | 2 | 19 | 2 | 21 | 0/8 | 0 | 1 | 2→0 | 0.0 | 0 | 1081 | digerible |
| ctacor | Cuentas de corresponsalía | 10 | 3 | 16 | 5 | 21 | 0/8 | 0 | 2 | 0→0 | 0.0 | 0 | 1632 | digerible |
| fgarcp | Fondos de garantía de carácter público | 14 | 3 | 18 | 3 | 21 | 0/9 | 3 | 1 | 6→0 | 0.0 | 0 | 4360 | digerible |
| regpri | Régimen para facilitar la privatización de Bancos Prov. y Mu… | 10 | 2 | 17 | 2 | 19 | 0/8 | 0 | 5 | 0→0 | 0.0 | 0 | 1669 | **necesita reglas** |
| ri_pgn | RI Cont. Mensual - Posición Global Neta en Moneda Extranjera | 19 | 7 | 16 | 3 | 19 | 0/0 | 1 | 1 | 7→0 | 26.3 | 9 | 3976 | **necesita reglas** |
| evacre | Evaluaciones crediticias | 7 | 3 | 15 | 3 | 18 | 0/7 | 0 | 0 | 0→0 | 0.0 | 0 | 792 | digerible |
| pognme | Posición global neta de moneda extranjera. | 14 | 4 | 16 | 1 | 17 | 0/7 | 3 | 1 | 5→0 | 0.0 | 0 | 3264 | digerible |
| manori | Manuales de originación y administración de préstamos | 99 | 4 | 12 | 4 | 16 | 0/10 | 0 | 188 | 55→0 | 12.5 | 2 | 45275 | **necesita reglas** |
| snp_atm | Sistema Nacional de Pagos - Cajeros automáticos | 8 | 3 | 14 | 2 | 16 | 0/5 | 0 | 3 | 0→0 | 0.0 | 0 | 869 | digerible |
| venliq | Ventanilla de liquidez del BCRA. | 10 | 2 | 13 | 3 | 16 | 7/14 | 7 | 1 | 0→0 | 6.2 | 0 | 2498 | **necesita reglas** |
| ri_gerc | RI Cont. Mensual - Grandes exposiciones al riesgo de crédito… | 8 | 3 | 13 | 2 | 15 | 1/0 | 0 | 8 | 1→0 | 6.7 | 2 | 1973 | **necesita reglas** |
| convca | Conversión cambiaria | 8 | 2 | 10 | 3 | 13 | 0/5 | 0 | 1 | 0→0 | 0.0 | 0 | 918 | digerible |
| horari | Horario de las entidades financieras | 13 | 3 | 13 | 0 | 13 | 0/13 | 0 | 11 | 0→0 | 7.7 | 0 | 5921 | **necesita reglas** |
| osapsa | Otros servicios y actividades prestados por sujetos alcanzad… | 12 | 5 | 12 | 0 | 12 | 0/8 | 3 | 0 | 1→0 | 0.0 | 0 | 2313 | digerible |
| socgar | Sociedades de garantía recíproca inscriptas en el Banco Cent… | 14 | 3 | 11 | 1 | 12 | 0/7 | 2 | 0 | 0→0 | 0.0 | 0 | 1327 | digerible |
| ri_ai | RI Cont. Mensual - Relación para los activos inmovilizados y… | 9 | 5 | 11 | 0 | 11 | 1/0 | 0 | 5 | 4→0 | 0.0 | 1 | 3074 | **necesita reglas** |
| cateloc | Categorización de localidades para entidades financieras | 67 | 2 | 2 | 0 | 2 | 0/0 | 0 | 0 | 0→0 | 50.0 | 0 | 126723 | **necesita reglas** |
| asomut | Asociaciones mutuales. Reglamentación de su actividad financ… | 7 | 0 | 0 | 0 | 0 | 8/8 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| cedin | Certificados de depósitos para la inversión | 22 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ceninf | Centrales de información | 23 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| consyr | Instrumentación, conservación y reproducción de documentos | 11 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| dmrd | Disciplina de Mercado - Requisitos mínimos de divulgación. | 72 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| manual | RI - Manual de Cuentas vigente al 31/12/17. | 2037 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| micemp | Determinación de la condición de micro, pequeña o mediana em… | 8 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| nmaeef | Normas mínimas sobre auditorías externas para entidades fina… | 69 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| nmcief | Normas mínimas sobre controles internos para entidades finan… | 36 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| optico | Presentación de informaciones al BCRA | 43 | 0 | 0 | 0 | 0 | 75/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| plandecuentas | RI - Plan de cuentas. | 77 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| reqcac | Requisitos Operativos Mínimos de Tecnología y Sistemas de In… | 10 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri2_ae | Normas mínimas sobre auditorías externas para casas y agenci… | 44 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri2_cs | RI - Casas y Agencias de Cambio - Contable Anual | 31 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri2_pm | RI - Casas y Agencias de Cambio - Plan y Manual de Cuentas | 376 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_acsf | RI Cont. Mensual - Agencias complementarias de servicios fin… | 3 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_ao | RI Cont. Mensual - Anticipo de Operaciones. | 1 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_bdp | RI Cont. Mensual - Base de Datos Padrón | 3 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_ccna | RI para Cajas de Crédito - Normas de Auditoría | 60 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_ccpnp | RI para Cajas de Crédito - Plan de Negocios y Proyecciones | 11 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_chr | RI Cont. Mensual - Cheques Rechazados | 1 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_con | RI Cont. Mensual - Estado de Consolidación de Entidades Loca… | 16 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_cr | RI Cont. Mensual - Reclamos | 5 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_dcpc | RI - Disposiciones complementarias al plan de cuentas. | 44 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_dsf | RI Cont. Mensual - Deudores del Sistema Financiero y Composi… | 31 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_esd | RI Cont. Mensual - Estado de Situación de Deudores Consolida… | 3 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_fcem | RI - Facturas de Crédito Electrónicas MiPyME. | 1 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_icpipsp | RI - Informe de Contadores Públicos Independientes sobre el … | 13 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_ieccm | RI - Informe Especial respecto del cumplimiento de Capitales… | 1 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_iepsp | RI - Informe especial sobre el cumplimiento de las normas so… | 9 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_iesinap | RI - Informe especial de cumplimiento requerido por el punto… | 6 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_ii_31_12_19 | RI Cont. Mensual - Información Institucional de Entidades Fi… | 21 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_itme | RI Cont. Mensual - Información sobre tenencias en moneda ext… | 1 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_laft | RI - Prevención del Lavado de Activos, del Financiamiento de… | 45 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_mmsef | RI Cont. Mensual - Medidas mínimas de seguridad en entidades… | 9 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_msrl | RI Cont. Mensual - Medición y Seguimiento del Riesgo de Liqu… | 20 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_nge | RI Cont. Mensual - Normas generales | 3 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_niif | RI - Estados financieros para publicación trimestral/anual. | 86 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_oc | RI Cont. Mensual - Operaciones de Cambio | 28 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_ot | RI Cont. Mensual - Operaciones a Término | 6 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_pfmipyme | RI - Plataformas para el Financiamiento MiPyME. | 1 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_pnp | RI - Plan de negocios y proyecciones. | 44 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_pscpp | RI - Proveedores de servicios de créditos entre particulares… | 1 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_psp | RI - Proveedores de servicios de pago que ofrecen cuentas de… | 14 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_pspapt | RI - Proveedores de Servicios de Pago - Adquirentes de pagos… | 5 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_pspii | RI - Proveedores de Servicios de Pago - Información Contable | 1 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_psprca | RI - Proveedores de Servicios de Pago – Redes de Cajeros Aut… | 6 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_rcl | RI Cont. Mensual - Ratio de Cobertura de Liquidez | 2 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_rem | RI Cont. Mensual - Pago de Remuneraciones mediante Acreditac… | 2 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_saofe | RI Cont. Mensual - Seguimiento de anticipos y otras financia… | 3 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_secoexpo | RI Cont. Mensual - Seguimiento de las negociaciones de divis… | 21 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_sef | RI Cont. Mensual - Unidades de servicios de las entidades fi… | 10 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_spi | RI Cont. Mensual - Seguimiento de Pagos de Importaciones. | 11 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_tar | RI Cont. Mensual - Financiamiento con tarjetas de crédito | 7 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_tii | RI Cont. Mensual - Transferencias Inmediatas Intraentidades | 6 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_transpa | RI Cont. Mensual - Transparencia | 23 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_tsa | RI para supervisión | 92 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ri_tvf | RI Cont. Mensual - Títulos Valores | 5 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| ribspc | RI Cont. Mensual - Balance de Saldos. | 2 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| seggar | Aplicación del sistema de seguro de garantía de depósitos. | 26 | 0 | 0 | 0 | 0 | 7/7 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| seguef | Medidas mínimas de seguridad en entidades financieras | 25 | 0 | 0 | 0 | 0 | 0/0 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |
| verac | Veracidad de las registraciones contables | 5 | 0 | 0 | 0 | 0 | 6/6 | 0 | 0 | 0→0 | 0.0 | 0 | 0 | **necesita reglas** |

## 5. Causa raíz de los TOs sin estructura (fallo H2)

62 TOs no producen ninguna unidad. `code/causa_sin_estructura.py` separa el mecanismo, porque cada uno pide una regla distinta:

| causa | TOs | cuáles |
|---|--:|---|
| A. ninguna página alcanza rol 'cuerpo': no hay marca '-Índice-' que abra el cuerpo | 54 | cedin, ceninf, consyr, dmrd, manual, nmaeef, plandecuentas, ri2_ae, ri2_cs, ri2_pm, ri_acsf, ri_ao, ri_bdp, ri_ccpnp, ri_chr, ri_con, ri_cr, ri_dcpc, ri_dsf, ri_esd, ri_fcem, ri_icpipsp, ri_ieccm, ri_iepsp, ri_iesinap, ri_ii_31_12_19, ri_itme, ri_laft, ri_mmsef, ri_msrl, ri_nge, ri_niif, ri_oc, ri_ot, ri_pfmipyme, ri_pnp, ri_pscpp, ri_psp, ri_pspapt, ri_pspii, ri_psprca, ri_rcl, ri_rem, ri_saofe, ri_secoexpo, ri_sef, ri_spi, ri_tar, ri_tii, ri_transpa, ri_tsa, ri_tvf, ribspc, seguef |
| B. hay cuerpo pero el TO no usa el encabezado 'Sección N. …' | 4 | asomut, micemp, nmcief, verac |
| B'. hay líneas 'Sección N.' pero no en posición de encabezado de página (el parser las toma como contenido) | 3 | reqcac, ri_ccna, seggar |
| A. ninguna página alcanza rol 'cuerpo': hay marca de índice pero el resto cae en otro rol | 1 | optico |

Reparto por categoría del índice oficial: normativa_general: 14, regimen_informativo: 48.

Detalle por TO (roles de página, líneas con marca de índice, líneas `Sección N.`, primeras líneas del documento) en `causa_sin_estructura.json`.

## 6. Evidencia de los TOs con veredicto «necesita reglas»

### snp_cheq — Sistema Nacional de Pagos - Cheques y otros instrumentos compensables

`t-snp-cheq.pdf`, 159 páginas (150 de cuerpo), 540 unidades (189 terminales + 351 mini-chunks).

Criterios incumplidos:
- C4 rechazos de header 285 sobre 540 unidades = 0.528/u > 0.214/u; motivos dominantes: fuera_de_seccion_7×224, fuera_de_seccion_4×37, profundidad_1_es_seccion×21

Roles de página: {"cuerpo": 150, "historial": 4, "indice": 2, "portada": 1, "tabla_norma_origen": 2}. Rechazos de header por motivo: {"padre_3.1.4_no_abierto": 2, "padre_3.3.6_no_abierto": 1, "fuera_de_seccion_4": 37, "profundidad_1_es_seccion": 21, "fuera_de_seccion_7": 224}. Avisos por tipo: {"aceptado_con_columna_derivada": 29, "pagina_cuerpo_sin_seccion": 28}.

Detalle completo en `e0_dry/snp_cheq/` (`divergencias_snp_cheq.json`, `estructura_snp_cheq.json`, `chunks_snp_cheq.json`).

### cirmo3 — Circulación monetaria

`t-cirmo3.pdf`, 107 páginas (92 de cuerpo), 240 unidades (215 terminales + 25 mini-chunks).

Criterios incumplidos:
- C4 rechazos de header 131 sobre 240 unidades = 0.546/u > 0.214/u; motivos dominantes: fuera_de_seccion_7×84, fuera_de_seccion_1×29, resto_vacio_referencia_envuelta×9
- C5 el índice anuncia 12 de 21 puntos que no aparecen en el cuerpo = 0.571 > 0.056
- C6 49 chunks con contenido tabular = 20.42 % > 20.24 %

Señales adicionales (no deciden el veredicto):
- 54 unidades del cuerpo no anunciadas por el índice (peor del subset: 12)
- 4 saltos de numeración (peor del subset: 2)

Roles de página: {"cuerpo": 92, "historial": 9, "indice": 1, "portada": 1, "tabla_norma_origen": 4}. Rechazos de header por motivo: {"fuera_de_seccion_7": 84, "padre_1.7_no_abierto": 1, "fuera_de_seccion_1": 29, "padre_1.2.16_no_abierto": 1, "padre_1.2.18_no_abierto": 1, "resto_vacio_referencia_envuelta": 9, "raiz_mayor_a_max": 6}. Avisos por tipo: {"pagina_cuerpo_sin_seccion": 15, "seccion_reabierta": 1}.

Detalle completo en `e0_dry/cirmo3/` (`divergencias_cirmo3.json`, `estructura_cirmo3.json`, `chunks_cirmo3.json`).

### ratio — Ratio de cobertura de liquidez

`t-ratio.pdf`, 46 páginas (39 de cuerpo), 132 unidades (112 terminales + 20 mini-chunks).

Criterios incumplidos:
- C7 avisos de parseo 35 sobre 132 unidades = 0.265/u > 0.250/u; tipos: aceptado_con_columna_derivada×35

Roles de página: {"cuerpo": 39, "historial": 3, "indice": 2, "portada": 1, "tabla_norma_origen": 1}. Rechazos de header por motivo: {"resto_vacio_referencia_envuelta": 1, "fuera_de_seccion_6": 2}. Avisos por tipo: {"aceptado_con_columna_derivada": 35}.

Detalle completo en `e0_dry/ratio/` (`divergencias_ratio.json`, `estructura_ratio.json`, `chunks_ratio.json`).

### garant — Garantías

`t-garant.pdf`, 25 páginas (15 de cuerpo), 104 unidades (93 terminales + 11 mini-chunks).

Criterios incumplidos:
- C7 avisos de parseo 32 sobre 104 unidades = 0.308/u > 0.250/u; tipos: aceptado_con_columna_derivada×32

Roles de página: {"cuerpo": 15, "historial": 5, "indice": 1, "portada": 1, "tabla_norma_origen": 3}. Rechazos de header por motivo: {"fuera_de_seccion_1": 1, "fuera_de_seccion_3": 2}. Avisos por tipo: {"aceptado_con_columna_derivada": 32}.

Detalle completo en `e0_dry/garant/` (`divergencias_garant.json`, `estructura_garant.json`, `chunks_garant.json`).

### jafip — Disposiciones judiciales originadas en juicios entablados por ARCA

`t-jAFIP.pdf`, 31 páginas (24 de cuerpo), 91 unidades (80 terminales + 11 mini-chunks).

Criterios incumplidos:
- C4 rechazos de header 21 sobre 91 unidades = 0.231/u > 0.214/u; motivos dominantes: fuera_de_seccion_5×18, profundidad_1_es_seccion×2, resto_vacio_referencia_envuelta×1

Roles de página: {"cuerpo": 24, "historial": 4, "indice": 2, "portada": 1}. Rechazos de header por motivo: {"resto_vacio_referencia_envuelta": 1, "fuera_de_seccion_5": 18, "profundidad_1_es_seccion": 2}. Avisos por tipo: {"aceptado_con_columna_derivada": 15}.

Detalle completo en `e0_dry/jafip/` (`divergencias_jafip.json`, `estructura_jafip.json`, `chunks_jafip.json`).

### snp_tr — Sistema Nacional de Pagos - Transferencias.

`t-SNP-tr.pdf`, 62 páginas (53 de cuerpo), 89 unidades (79 terminales + 10 mini-chunks).

Criterios incumplidos:
- C4 rechazos de header 119 sobre 89 unidades = 1.337/u > 0.214/u; motivos dominantes: fuera_de_seccion_1×86, profundidad_1_es_seccion×11, padre_1.4_no_abierto×4
- C5 el índice anuncia 2 de 12 puntos que no aparecen en el cuerpo = 0.167 > 0.056

Roles de página: {"cuerpo": 53, "historial": 5, "indice": 1, "portada": 1, "tabla_norma_origen": 2}. Rechazos de header por motivo: {"profundidad_1_es_seccion": 11, "fuera_de_seccion_1": 86, "padre_1.3_no_abierto": 3, "padre_1.3.4_no_abierto": 2, "padre_1.3.5_no_abierto": 3, "padre_1.3.6_no_abierto": 2, "no_sucede_al_hermano_6": 3, "padre_1.4_no_abierto": 4, "padre_1.5_no_abierto": 2, "padre_1.5.2_no_abierto": 2, "raiz_mayor_a_max": 1}. Avisos por tipo: {"aceptado_con_columna_derivada": 5}.

Detalle completo en `e0_dry/snp_tr/` (`divergencias_snp_tr.json`, `estructura_snp_tr.json`, `chunks_snp_tr.json`).

### inspag — Características de los instrumentos de pago que emiten las entidades financieras

`t-inspag.pdf`, 60 páginas (51 de cuerpo), 75 unidades (64 terminales + 11 mini-chunks).

Criterios incumplidos:
- C4 rechazos de header 18 sobre 75 unidades = 0.240/u > 0.214/u; motivos dominantes: fuera_de_seccion_1×16, resto_vacio_referencia_envuelta×1, no_sucede_al_hermano_19×1
- C5 el índice anuncia 18 de 55 puntos que no aparecen en el cuerpo = 0.327 > 0.056
- C7 avisos de parseo 29 sobre 75 unidades = 0.387/u > 0.250/u; tipos: pagina_cuerpo_sin_seccion×20, aceptado_con_columna_derivada×9

Roles de página: {"cuerpo": 51, "historial": 4, "indice": 2, "portada": 1, "tabla_norma_origen": 2}. Rechazos de header por motivo: {"resto_vacio_referencia_envuelta": 1, "fuera_de_seccion_1": 16, "no_sucede_al_hermano_19": 1}. Avisos por tipo: {"pagina_cuerpo_sin_seccion": 20, "aceptado_con_columna_derivada": 9}.

Detalle completo en `e0_dry/inspag/` (`divergencias_inspag.json`, `estructura_inspag.json`, `chunks_inspag.json`).

### opecam — Operadores de cambio.

`t-opecam.pdf`, 32 páginas (23 de cuerpo), 56 unidades (53 terminales + 3 mini-chunks).

Criterios incumplidos:
- C5 el índice anuncia 4 de 20 puntos que no aparecen en el cuerpo = 0.200 > 0.056

Roles de página: {"cuerpo": 23, "historial": 5, "indice": 1, "portada": 1, "tabla_norma_origen": 2}. Rechazos de header por motivo: {"fuera_de_seccion_2": 4, "no_sucede_al_hermano_2": 1, "padre_6.1.3_no_abierto": 1, "fuera_de_seccion_8": 1}. Avisos por tipo: {"pagina_cuerpo_sin_seccion": 2}.

Detalle completo en `e0_dry/opecam/` (`divergencias_opecam.json`, `estructura_opecam.json`, `chunks_opecam.json`).

### snp_dd — Sistema Nacional de Pagos - Débitos Directos

`t-snp-dd.pdf`, 68 páginas (63 de cuerpo), 53 unidades (46 terminales + 7 mini-chunks).

Criterios incumplidos:
- C4 rechazos de header 144 sobre 53 unidades = 2.717/u > 0.214/u; motivos dominantes: fuera_de_seccion_6×97, fuera_de_seccion_4×25, profundidad_1_es_seccion×14
- C5 el índice anuncia 13 de 25 puntos que no aparecen en el cuerpo = 0.520 > 0.056
- C7 avisos de parseo 46 sobre 53 unidades = 0.868/u > 0.250/u; tipos: pagina_cuerpo_sin_seccion×42, aceptado_con_columna_derivada×4
- C8 chunk terminal más grande 41031 chars > 26182 chars (señal de tramo no segmentado)

Roles de página: {"cuerpo": 63, "historial": 2, "indice": 1, "portada": 1, "tabla_norma_origen": 1}. Rechazos de header por motivo: {"fuera_de_seccion_3": 8, "profundidad_1_es_seccion": 14, "fuera_de_seccion_4": 25, "fuera_de_seccion_6": 97}. Avisos por tipo: {"aceptado_con_columna_derivada": 4, "pagina_cuerpo_sin_seccion": 42}.

Detalle completo en `e0_dry/snp_dd/` (`divergencias_snp_dd.json`, `estructura_snp_dd.json`, `chunks_snp_dd.json`).

### snp_mep — Sistema Nacional de Pagos - Medio electrónico de pagos (MEP)

`t-snp-mep.pdf`, 50 páginas (33 de cuerpo), 46 unidades (36 terminales + 10 mini-chunks).

Criterios incumplidos:
- C5 el índice anuncia 8 de 25 puntos que no aparecen en el cuerpo = 0.320 > 0.056
- C8 chunk terminal más grande 49553 chars > 26182 chars (señal de tramo no segmentado)

Señales adicionales (no deciden el veredicto):
- 25 unidades del cuerpo no anunciadas por el índice (peor del subset: 12)

Roles de página: {"cuerpo": 33, "historial": 12, "indice": 2, "portada": 1, "tabla_norma_origen": 2}. Rechazos de header por motivo: {"fuera_de_seccion_7": 1}. Avisos por tipo: {}.

Detalle completo en `e0_dry/snp_mep/` (`divergencias_snp_mep.json`, `estructura_snp_mep.json`, `chunks_snp_mep.json`).

### garopt — Garantías por intermediación en operaciones entre terceros

`t-garopt.pdf`, 15 páginas (8 de cuerpo), 41 unidades (36 terminales + 5 mini-chunks).

Criterios incumplidos:
- C4 rechazos de header 21 sobre 41 unidades = 0.512/u > 0.214/u; motivos dominantes: fuera_de_seccion_1×19, resto_vacio_referencia_envuelta×2
- C5 el índice anuncia 4 de 16 puntos que no aparecen en el cuerpo = 0.250 > 0.056

Roles de página: {"cuerpo": 8, "historial": 3, "indice": 1, "portada": 1, "tabla_norma_origen": 2}. Rechazos de header por motivo: {"fuera_de_seccion_1": 19, "resto_vacio_referencia_envuelta": 2}. Avisos por tipo: {"aceptado_con_columna_derivada": 1, "pagina_cuerpo_sin_seccion": 2}.

Detalle completo en `e0_dry/garopt/` (`divergencias_garopt.json`, `estructura_garopt.json`, `chunks_garopt.json`).

### ri_cc — RI para Cajas de Crédito - contable

`t-ri-cc.pdf`, 118 páginas (68 de cuerpo), 33 unidades (30 terminales + 3 mini-chunks).

Criterios incumplidos:
- C4 rechazos de header 61 sobre 33 unidades = 1.848/u > 0.214/u; motivos dominantes: fuera_de_seccion_2×27, fuera_de_seccion_3×24, profundidad_1_es_seccion×4
- C5 el índice anuncia 16 de 28 puntos que no aparecen en el cuerpo = 0.571 > 0.056
- C7 avisos de parseo 54 sobre 33 unidades = 1.636/u > 0.250/u; tipos: pagina_cuerpo_sin_seccion×46, aceptado_con_columna_derivada×6, seccion_reabierta×2

Señales adicionales (no deciden el veredicto):
- 18 unidades del cuerpo no anunciadas por el índice (peor del subset: 12)

Roles de página: {"cuerpo": 68, "indice": 3, "portada": 47}. Rechazos de header por motivo: {"padre_1.8_no_abierto": 3, "fuera_de_seccion_3": 24, "profundidad_1_es_seccion": 4, "fuera_de_seccion_4": 3, "fuera_de_seccion_2": 27}. Avisos por tipo: {"aceptado_con_columna_derivada": 6, "seccion_reabierta": 2, "pagina_cuerpo_sin_seccion": 46}.

Detalle completo en `e0_dry/ri_cc/` (`divergencias_ri_cc.json`, `estructura_ri_cc.json`, `chunks_ri_cc.json`).

### rmgcti — Requisitos mínimos para la gestión y control de los riesgos de tecnología y seguridad de la información

`t-rmgcti.pdf`, 58 páginas (51 de cuerpo), 32 unidades (27 terminales + 5 mini-chunks).

Criterios incumplidos:
- C4 rechazos de header 52 sobre 32 unidades = 1.625/u > 0.214/u; motivos dominantes: fuera_de_seccion_2×38, fuera_de_seccion_7×12, resto_vacio_referencia_envuelta×1
- C5 el índice anuncia 34 de 46 puntos que no aparecen en el cuerpo = 0.739 > 0.056
- C7 avisos de parseo 31 sobre 32 unidades = 0.969/u > 0.250/u; tipos: pagina_cuerpo_sin_seccion×31

Roles de página: {"cuerpo": 51, "historial": 2, "indice": 2, "portada": 1, "tabla_norma_origen": 2}. Rechazos de header por motivo: {"fuera_de_seccion_2": 38, "resto_vacio_referencia_envuelta": 1, "fuera_de_seccion_7": 12, "fuera_de_seccion_10": 1}. Avisos por tipo: {"pagina_cuerpo_sin_seccion": 31}.

Detalle completo en `e0_dry/rmgcti/` (`divergencias_rmgcti.json`, `estructura_rmgcti.json`, `chunks_rmgcti.json`).

### ri_rml — RI Cont. Mensual - Efectivo mínimo y aplicación de recursos

`t-RI-RML.pdf`, 77 páginas (76 de cuerpo), 27 unidades (26 terminales + 1 mini-chunks).

Criterios incumplidos:
- C4 rechazos de header 128 sobre 27 unidades = 4.741/u > 0.214/u; motivos dominantes: fuera_de_seccion_4×95, resto_vacio_referencia_envuelta×14, profundidad_1_es_seccion×4
- C6 12 chunks con contenido tabular = 44.44 % > 20.24 %
- C7 avisos de parseo 10 sobre 27 unidades = 0.370/u > 0.250/u; tipos: aceptado_con_columna_derivada×7, pagina_cuerpo_sin_seccion×3
- C8 chunk terminal más grande 65711 chars > 26182 chars (señal de tramo no segmentado)

Roles de página: {"cuerpo": 76, "indice": 1}. Rechazos de header por motivo: {"padre_1.2_no_abierto": 1, "no_sucede_al_hermano_3": 1, "resto_minuscula_y_salto_de_0_a_17_sin_contexto_de_lista": 1, "raiz_mayor_a_max": 3, "fuera_de_seccion_1": 1, "resto_vacio_referencia_envuelta": 14, "padre_1.3_no_abierto": 3, "fuera_de_seccion_3": 3, "fuera_de_seccion_4": 95, "profundidad_1_es_seccion": 4, "fuera_de_seccion_6": 2}. Avisos por tipo: {"aceptado_con_columna_derivada": 7, "pagina_cuerpo_sin_seccion": 3}.

Detalle completo en `e0_dry/ri_rml/` (`divergencias_ri_rml.json`, `estructura_ri_rml.json`, `chunks_ri_rml.json`).

### regpri — Régimen para facilitar la privatización de Bancos Prov. y Municipales y las fusiones y absorciones

`t-regpri.pdf`, 10 páginas (6 de cuerpo), 19 unidades (17 terminales + 2 mini-chunks).

Criterios incumplidos:
- C4 rechazos de header 5 sobre 19 unidades = 0.263/u > 0.214/u; motivos dominantes: resto_vacio_referencia_envuelta×3, fuera_de_seccion_1×1, no_sucede_al_hermano_1×1

Roles de página: {"cuerpo": 6, "historial": 1, "indice": 1, "portada": 1, "tabla_norma_origen": 1}. Rechazos de header por motivo: {"resto_vacio_referencia_envuelta": 3, "fuera_de_seccion_1": 1, "no_sucede_al_hermano_1": 1}. Avisos por tipo: {}.

Detalle completo en `e0_dry/regpri/` (`divergencias_regpri.json`, `estructura_regpri.json`, `chunks_regpri.json`).

### ri_pgn — RI Cont. Mensual - Posición Global Neta en Moneda Extranjera

`t-RI-PGN.pdf`, 19 páginas (18 de cuerpo), 19 unidades (16 terminales + 3 mini-chunks).

Criterios incumplidos:
- C6 5 chunks con contenido tabular = 26.32 % > 20.24 %
- C7 avisos de parseo 7 sobre 19 unidades = 0.368/u > 0.250/u; tipos: aceptado_con_columna_derivada×7

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"cuerpo": 18, "indice": 1}. Rechazos de header por motivo: {"no_sucede_al_hermano_2": 1}. Avisos por tipo: {"aceptado_con_columna_derivada": 7}.

Detalle completo en `e0_dry/ri_pgn/` (`divergencias_ri_pgn.json`, `estructura_ri_pgn.json`, `chunks_ri_pgn.json`).

### manori — Manuales de originación y administración de préstamos

`t-manori.pdf`, 99 páginas (91 de cuerpo), 16 unidades (12 terminales + 4 mini-chunks).

Criterios incumplidos:
- C4 rechazos de header 188 sobre 16 unidades = 11.750/u > 0.214/u; motivos dominantes: fuera_de_seccion_1×18, padre_1.1_no_abierto×11, padre_3.1_no_abierto×11
- C8 chunk terminal más grande 45275 chars > 26182 chars (señal de tramo no segmentado)

Roles de página: {"cuerpo": 91, "historial": 3, "indice": 1, "portada": 1, "tabla_norma_origen": 3}. Rechazos de header por motivo: {"no_sucede_al_hermano_5": 10, "padre_1.1_no_abierto": 11, "padre_1.1.2_no_abierto": 4, "padre_1.1.4_no_abierto": 5, "padre_1.1.5_no_abierto": 9, "fuera_de_seccion_1": 18, "padre_1.1.6_no_abierto": 5, "padre_1.1.7_no_abierto": 4, "padre_1.1.8_no_abierto": 2, "padre_1.1.9_no_abierto": 3, "padre_1.1.10_no_abierto": 3, "padre_1.2_no_abierto": 10, "padre_1.2.2_no_abierto": 2, "padre_1.2.4_no_abierto": 2, "padre_1.2.7_no_abierto": 2, "profundidad_1_es_seccion": 3, "padre_1.2.8_no_abierto": 4, "padre_1.2.10_no_abierto": 2, "padre_1.3_no_abierto": 6, "padre_1.3.5_no_abierto": 2, "padre_1.3.6_no_abierto": 2, "padre_1.4_no_abierto": 2, "padre_1.4.1_no_abierto": 3, "padre_1.5_no_abierto": 2, "padre_3.1_no_abierto": 11, "padre_3.1.2_no_abierto": 2, "padre_3.1.4_no_abierto": 4, "padre_3.1.5_no_abierto": 9, "fuera_de_seccion_3": 3, "padre_3.1.6_no_abierto": 5, "padre_3.1.7_no_abierto": 2, "padre_3.1.8_no_abierto": 2, "padre_3.1.9_no_abierto": 3, "padre_3.1.10_no_abierto": 1, "padre_3.2_no_abierto": 9, "padre_3.2.2_no_abierto": 2, "padre_3.2.9_no_abierto": 2, "padre_3.3_no_abierto": 7, "padre_3.3.7_no_abierto": 3, "padre_3.4_no_abierto": 2, "padre_3.4.1_no_abierto": 3, "padre_3.5_no_abierto": 2}. Avisos por tipo: {}.

Detalle completo en `e0_dry/manori/` (`divergencias_manori.json`, `estructura_manori.json`, `chunks_manori.json`).

### venliq — Ventanilla de liquidez del BCRA.

`t-venliq.pdf`, 10 páginas (5 de cuerpo), 16 unidades (13 terminales + 3 mini-chunks).

Criterios incumplidos:
- C5 el índice anuncia 7 de 14 puntos que no aparecen en el cuerpo = 0.500 > 0.056

Roles de página: {"cuerpo": 5, "historial": 1, "indice": 2, "portada": 1, "tabla_norma_origen": 1}. Rechazos de header por motivo: {"padre_1.2_no_abierto": 1}. Avisos por tipo: {"aceptado_con_columna_derivada": 1, "pagina_cuerpo_sin_seccion": 1}.

Detalle completo en `e0_dry/venliq/` (`divergencias_venliq.json`, `estructura_venliq.json`, `chunks_venliq.json`).

### ri_gerc — RI Cont. Mensual - Grandes exposiciones al riesgo de crédito.

`t-RI-GERC.pdf`, 8 páginas (7 de cuerpo), 15 unidades (13 terminales + 2 mini-chunks).

Criterios incumplidos:
- C4 rechazos de header 8 sobre 15 unidades = 0.533/u > 0.214/u; motivos dominantes: fuera_de_seccion_2×6, no_sucede_al_hermano_6×1, resto_vacio_referencia_envuelta×1

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"cuerpo": 7, "indice": 1}. Rechazos de header por motivo: {"fuera_de_seccion_2": 6, "no_sucede_al_hermano_6": 1, "resto_vacio_referencia_envuelta": 1}. Avisos por tipo: {"aceptado_con_columna_derivada": 3}.

Detalle completo en `e0_dry/ri_gerc/` (`divergencias_ri_gerc.json`, `estructura_ri_gerc.json`, `chunks_ri_gerc.json`).

### horari — Horario de las entidades financieras

`t-horari.pdf`, 13 páginas (8 de cuerpo), 13 unidades (13 terminales + 0 mini-chunks).

Criterios incumplidos:
- C4 rechazos de header 11 sobre 13 unidades = 0.846/u > 0.214/u; motivos dominantes: resto_vacio_referencia_envuelta×8, raiz_mayor_a_max×2, fuera_de_seccion_1×1

Roles de página: {"cuerpo": 8, "historial": 2, "indice": 1, "portada": 1, "tabla_norma_origen": 1}. Rechazos de header por motivo: {"fuera_de_seccion_1": 1, "resto_vacio_referencia_envuelta": 8, "raiz_mayor_a_max": 2}. Avisos por tipo: {}.

Detalle completo en `e0_dry/horari/` (`divergencias_horari.json`, `estructura_horari.json`, `chunks_horari.json`).

### ri_ai — RI Cont. Mensual - Relación para los activos inmovilizados y otros conceptos

`t-RI-AI.pdf`, 9 páginas (8 de cuerpo), 11 unidades (11 terminales + 0 mini-chunks).

Criterios incumplidos:
- C4 rechazos de header 5 sobre 11 unidades = 0.455/u > 0.214/u; motivos dominantes: fuera_de_seccion_4×3, fuera_de_seccion_1×2
- C7 avisos de parseo 3 sobre 11 unidades = 0.273/u > 0.250/u; tipos: aceptado_con_columna_derivada×2, pagina_cuerpo_sin_seccion×1

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"cuerpo": 8, "indice": 1}. Rechazos de header por motivo: {"fuera_de_seccion_1": 2, "fuera_de_seccion_4": 3}. Avisos por tipo: {"pagina_cuerpo_sin_seccion": 1, "aceptado_con_columna_derivada": 2}.

Detalle completo en `e0_dry/ri_ai/` (`divergencias_ri_ai.json`, `estructura_ri_ai.json`, `chunks_ri_ai.json`).

### cateloc — Categorización de localidades para entidades financieras

`t-cateloc.pdf`, 67 páginas (63 de cuerpo), 2 unidades (2 terminales + 0 mini-chunks).

Criterios incumplidos:
- C6 1 chunks con contenido tabular = 50.00 % > 20.24 %
- C8 chunk terminal más grande 126723 chars > 26182 chars (señal de tramo no segmentado)

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"cuerpo": 63, "historial": 1, "indice": 1, "portada": 1, "tabla_norma_origen": 1}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/cateloc/` (`divergencias_cateloc.json`, `estructura_cateloc.json`, `chunks_cateloc.json`).

### asomut — Asociaciones mutuales. Reglamentación de su actividad financiera (Decreto 1367/93)

`t-asomut.pdf`, 7 páginas (3 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H1 cobertura no exacta: parseadas=0, en estructura=0, duplicadas=0, huérfanas=45
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0
- C5 el índice anuncia 8 de 8 puntos que no aparecen en el cuerpo = 1.000 > 0.056
- C7 avisos de parseo 6 sobre 1 unidades = 6.000/u > 0.250/u; tipos: pagina_cuerpo_sin_seccion×3, contenido_antes_de_seccion×3

Roles de página: {"cuerpo": 3, "historial": 1, "indice": 1, "portada": 1, "tabla_norma_origen": 1}. Rechazos de header por motivo: {}. Avisos por tipo: {"pagina_cuerpo_sin_seccion": 3, "contenido_antes_de_seccion": 3}.

Detalle completo en `e0_dry/asomut/` (`divergencias_asomut.json`, `estructura_asomut.json`, `chunks_asomut.json`).

### cedin — Certificados de depósitos para la inversión

`t-cedin.pdf`, 22 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"historial": 2, "portada": 18, "tabla_norma_origen": 2}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/cedin/` (`divergencias_cedin.json`, `estructura_cedin.json`, `chunks_cedin.json`).

### ceninf — Centrales de información

`t-ceninf.pdf`, 23 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"historial": 3, "portada": 20}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ceninf/` (`divergencias_ceninf.json`, `estructura_ceninf.json`, `chunks_ceninf.json`).

### consyr — Instrumentación, conservación y reproducción de documentos

`t-consyr.pdf`, 11 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"historial": 2, "portada": 8, "tabla_norma_origen": 1}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/consyr/` (`divergencias_consyr.json`, `estructura_consyr.json`, `chunks_consyr.json`).

### dmrd — Disciplina de Mercado - Requisitos mínimos de divulgación.

`t-dmrd.pdf`, 72 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 72}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/dmrd/` (`divergencias_dmrd.json`, `estructura_dmrd.json`, `chunks_dmrd.json`).

### manual — RI - Manual de Cuentas vigente al 31/12/17.

`manual.pdf`, 2037 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 2037}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/manual/` (`divergencias_manual.json`, `estructura_manual.json`, `chunks_manual.json`).

### micemp — Determinación de la condición de micro, pequeña o mediana empresa

`t-micemp.pdf`, 8 páginas (1 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H1 cobertura no exacta: parseadas=0, en estructura=0, duplicadas=0, huérfanas=25
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0
- C7 avisos de parseo 2 sobre 1 unidades = 2.000/u > 0.250/u; tipos: pagina_cuerpo_sin_seccion×1, contenido_antes_de_seccion×1

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"cuerpo": 1, "historial": 4, "indice": 1, "portada": 1, "tabla_norma_origen": 1}. Rechazos de header por motivo: {}. Avisos por tipo: {"pagina_cuerpo_sin_seccion": 1, "contenido_antes_de_seccion": 1}.

Detalle completo en `e0_dry/micemp/` (`divergencias_micemp.json`, `estructura_micemp.json`, `chunks_micemp.json`).

### nmaeef — Normas mínimas sobre auditorías externas para entidades financieras

`t-nmaeef.pdf`, 69 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 69}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/nmaeef/` (`divergencias_nmaeef.json`, `estructura_nmaeef.json`, `chunks_nmaeef.json`).

### nmcief — Normas mínimas sobre controles internos para entidades financieras

`t-nmcief.pdf`, 36 páginas (35 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H1 cobertura no exacta: parseadas=0, en estructura=0, duplicadas=0, huérfanas=1298
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0
- C7 avisos de parseo 70 sobre 1 unidades = 70.000/u > 0.250/u; tipos: pagina_cuerpo_sin_seccion×35, contenido_antes_de_seccion×35

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"cuerpo": 35, "indice": 1}. Rechazos de header por motivo: {}. Avisos por tipo: {"pagina_cuerpo_sin_seccion": 35, "contenido_antes_de_seccion": 35}.

Detalle completo en `e0_dry/nmcief/` (`divergencias_nmcief.json`, `estructura_nmcief.json`, `chunks_nmcief.json`).

### optico — Presentación de informaciones al BCRA

`t-optico.pdf`, 43 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"historial": 38, "indice": 4, "portada": 1}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/optico/` (`divergencias_optico.json`, `estructura_optico.json`, `chunks_optico.json`).

### plandecuentas — RI - Plan de cuentas.

`plandecuentas.pdf`, 77 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 77}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/plandecuentas/` (`divergencias_plandecuentas.json`, `estructura_plandecuentas.json`, `chunks_plandecuentas.json`).

### reqcac — Requisitos Operativos Mínimos de Tecnología y Sistemas de Información p/ Casas y Agencias de Cambio

`t-reqcac.pdf`, 10 páginas (8 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H1 cobertura no exacta: parseadas=0, en estructura=0, duplicadas=0, huérfanas=274
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0
- C7 avisos de parseo 16 sobre 1 unidades = 16.000/u > 0.250/u; tipos: pagina_cuerpo_sin_seccion×8, contenido_antes_de_seccion×8

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"cuerpo": 8, "indice": 1, "portada": 1}. Rechazos de header por motivo: {}. Avisos por tipo: {"pagina_cuerpo_sin_seccion": 8, "contenido_antes_de_seccion": 8}.

Detalle completo en `e0_dry/reqcac/` (`divergencias_reqcac.json`, `estructura_reqcac.json`, `chunks_reqcac.json`).

### ri2_ae — Normas mínimas sobre auditorías externas para casas y agencias de cambio.

`t-RI2-AE.pdf`, 44 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"historial": 1, "portada": 43}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri2_ae/` (`divergencias_ri2_ae.json`, `estructura_ri2_ae.json`, `chunks_ri2_ae.json`).

### ri2_cs — RI - Casas y Agencias de Cambio - Contable Anual

`t-RI2-CS.pdf`, 31 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 31}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri2_cs/` (`divergencias_ri2_cs.json`, `estructura_ri2_cs.json`, `chunks_ri2_cs.json`).

### ri2_pm — RI - Casas y Agencias de Cambio - Plan y Manual de Cuentas

`t-RI2-PM.pdf`, 376 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 376}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri2_pm/` (`divergencias_ri2_pm.json`, `estructura_ri2_pm.json`, `chunks_ri2_pm.json`).

### ri_acsf — RI Cont. Mensual - Agencias complementarias de servicios financieros.

`t-RI-ACSF.pdf`, 3 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 3}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_acsf/` (`divergencias_ri_acsf.json`, `estructura_ri_acsf.json`, `chunks_ri_acsf.json`).

### ri_ao — RI Cont. Mensual - Anticipo de Operaciones.

`t-RI-AO.pdf`, 1 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 1}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_ao/` (`divergencias_ri_ao.json`, `estructura_ri_ao.json`, `chunks_ri_ao.json`).

### ri_bdp — RI Cont. Mensual - Base de Datos Padrón

`t-RI-BDP.pdf`, 3 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 3}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_bdp/` (`divergencias_ri_bdp.json`, `estructura_ri_bdp.json`, `chunks_ri_bdp.json`).

### ri_ccna — RI para Cajas de Crédito - Normas de Auditoría

`t-RI-CcNA.pdf`, 60 páginas (58 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H1 cobertura no exacta: parseadas=0, en estructura=0, duplicadas=0, huérfanas=1953
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0
- C7 avisos de parseo 116 sobre 1 unidades = 116.000/u > 0.250/u; tipos: pagina_cuerpo_sin_seccion×58, contenido_antes_de_seccion×58

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"cuerpo": 58, "indice": 2}. Rechazos de header por motivo: {}. Avisos por tipo: {"pagina_cuerpo_sin_seccion": 58, "contenido_antes_de_seccion": 58}.

Detalle completo en `e0_dry/ri_ccna/` (`divergencias_ri_ccna.json`, `estructura_ri_ccna.json`, `chunks_ri_ccna.json`).

### ri_ccpnp — RI para Cajas de Crédito - Plan de Negocios y Proyecciones

`t-RI-CCPNP.pdf`, 11 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 11}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_ccpnp/` (`divergencias_ri_ccpnp.json`, `estructura_ri_ccpnp.json`, `chunks_ri_ccpnp.json`).

### ri_chr — RI Cont. Mensual - Cheques Rechazados

`t-RI-CHR.pdf`, 1 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 1}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_chr/` (`divergencias_ri_chr.json`, `estructura_ri_chr.json`, `chunks_ri_chr.json`).

### ri_con — RI Cont. Mensual - Estado de Consolidación de Entidades Locales con Filiales y Subsidiarias Significativas en el País y en el Exterior.

`t-RI-Con.pdf`, 16 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 16}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_con/` (`divergencias_ri_con.json`, `estructura_ri_con.json`, `chunks_ri_con.json`).

### ri_cr — RI Cont. Mensual - Reclamos

`t-RI-CR.pdf`, 5 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 5}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_cr/` (`divergencias_ri_cr.json`, `estructura_ri_cr.json`, `chunks_ri_cr.json`).

### ri_dcpc — RI - Disposiciones complementarias al plan de cuentas.

`RI-DCPC.pdf`, 44 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 44}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_dcpc/` (`divergencias_ri_dcpc.json`, `estructura_ri_dcpc.json`, `chunks_ri_dcpc.json`).

### ri_dsf — RI Cont. Mensual - Deudores del Sistema Financiero y Composición de los conjuntos económicos.

`t-RI-DSF.pdf`, 31 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 31}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_dsf/` (`divergencias_ri_dsf.json`, `estructura_ri_dsf.json`, `chunks_ri_dsf.json`).

### ri_esd — RI Cont. Mensual - Estado de Situación de Deudores Consolidado con Filiales y Subsidiarias Significativas en el País y en el Exterior .

`t-RI-ESD.PDF`, 3 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 3}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_esd/` (`divergencias_ri_esd.json`, `estructura_ri_esd.json`, `chunks_ri_esd.json`).

### ri_fcem — RI - Facturas de Crédito Electrónicas MiPyME.

`t-RI-FCEM.pdf`, 1 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 1}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_fcem/` (`divergencias_ri_fcem.json`, `estructura_ri_fcem.json`, `chunks_ri_fcem.json`).

### ri_icpipsp — RI - Informe de Contadores Públicos Independientes sobre el cumplimiento de las Normas del BCRA por parte de los Proveedores de Servicios de Pago.

`t-RI-ICPIPSP.pdf`, 13 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 13}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_icpipsp/` (`divergencias_ri_icpipsp.json`, `estructura_ri_icpipsp.json`, `chunks_ri_icpipsp.json`).

### ri_ieccm — RI - Informe Especial respecto del cumplimiento de Capitales Mínimos (Comunicación "A" 7584)

`t-RI-IECCM.pdf`, 1 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 1}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_ieccm/` (`divergencias_ri_ieccm.json`, `estructura_ri_ieccm.json`, `chunks_ri_ieccm.json`).

### ri_iepsp — RI - Informe especial sobre el cumplimiento de las normas sobre "Proveedores no financieros de crédito".

`t-RI-IEPSP.pdf`, 9 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 9}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_iepsp/` (`divergencias_ri_iepsp.json`, `estructura_ri_iepsp.json`, `chunks_ri_iepsp.json`).

### ri_iesinap — RI - Informe especial de cumplimiento requerido por el punto 1.5.5.10. de las normas sobre “Sistema Nacional de Pagos Transferencias Normas complementarias”

`t-RI-IESINAP.pdf`, 6 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 6}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_iesinap/` (`divergencias_ri_iesinap.json`, `estructura_ri_iesinap.json`, `chunks_ri_iesinap.json`).

### ri_ii_31_12_19 — RI Cont. Mensual - Información Institucional de Entidades Financieras y Cambiarias - Vigente a partir del 31.12.19

`t-RI-II-31-12-19.pdf`, 21 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 21}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_ii_31_12_19/` (`divergencias_ri_ii_31_12_19.json`, `estructura_ri_ii_31_12_19.json`, `chunks_ri_ii_31_12_19.json`).

### ri_itme — RI Cont. Mensual - Información sobre tenencias en moneda extranjera de casas y agencias de cambio.

`t-RI-ITME.pdf`, 1 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 1}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_itme/` (`divergencias_ri_itme.json`, `estructura_ri_itme.json`, `chunks_ri_itme.json`).

### ri_laft — RI - Prevención del Lavado de Activos, del Financiamiento del Terrorismo y Otras Actividades Ilícitas.

`t-RI-LAFT.pdf`, 45 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 45}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_laft/` (`divergencias_ri_laft.json`, `estructura_ri_laft.json`, `chunks_ri_laft.json`).

### ri_mmsef — RI Cont. Mensual - Medidas mínimas de seguridad en entidades financieras

`t-RI-MMSEF.pdf`, 9 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 9}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_mmsef/` (`divergencias_ri_mmsef.json`, `estructura_ri_mmsef.json`, `chunks_ri_mmsef.json`).

### ri_msrl — RI Cont. Mensual - Medición y Seguimiento del Riesgo de Liquidez

`t-RI-MSRL.pdf`, 20 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 20}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_msrl/` (`divergencias_ri_msrl.json`, `estructura_ri_msrl.json`, `chunks_ri_msrl.json`).

### ri_nge — RI Cont. Mensual - Normas generales

`t-RI-nge.pdf`, 3 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 3}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_nge/` (`divergencias_ri_nge.json`, `estructura_ri_nge.json`, `chunks_ri_nge.json`).

### ri_niif — RI - Estados financieros para publicación trimestral/anual.

`RI-NIIF.pdf`, 86 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 86}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_niif/` (`divergencias_ri_niif.json`, `estructura_ri_niif.json`, `chunks_ri_niif.json`).

### ri_oc — RI Cont. Mensual - Operaciones de Cambio

`t-RI-OC.pdf`, 28 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 28}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_oc/` (`divergencias_ri_oc.json`, `estructura_ri_oc.json`, `chunks_ri_oc.json`).

### ri_ot — RI Cont. Mensual - Operaciones a Término

`t-RI-OT.pdf`, 6 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 6}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_ot/` (`divergencias_ri_ot.json`, `estructura_ri_ot.json`, `chunks_ri_ot.json`).

### ri_pfmipyme — RI - Plataformas para el Financiamiento MiPyME.

`t-RI-PFMIPYME.pdf`, 1 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 1}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_pfmipyme/` (`divergencias_ri_pfmipyme.json`, `estructura_ri_pfmipyme.json`, `chunks_ri_pfmipyme.json`).

### ri_pnp — RI - Plan de negocios y proyecciones.

`t-ri-pnp.pdf`, 44 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 44}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_pnp/` (`divergencias_ri_pnp.json`, `estructura_ri_pnp.json`, `chunks_ri_pnp.json`).

### ri_pscpp — RI - Proveedores de servicios de créditos entre particulares a través de plataformas (RI-PSCPP)

`t-RI-PSCPP.pdf`, 1 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 1}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_pscpp/` (`divergencias_ri_pscpp.json`, `estructura_ri_pscpp.json`, `chunks_ri_pscpp.json`).

### ri_psp — RI - Proveedores de servicios de pago que ofrecen cuentas de pago.

`t-RI-PSP.pdf`, 14 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 14}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_psp/` (`divergencias_ri_psp.json`, `estructura_ri_psp.json`, `chunks_ri_psp.json`).

### ri_pspapt — RI - Proveedores de Servicios de Pago - Adquirentes de pagos con tarjeta

`t-RI-PSPAPT.pdf`, 5 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 5}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_pspapt/` (`divergencias_ri_pspapt.json`, `estructura_ri_pspapt.json`, `chunks_ri_pspapt.json`).

### ri_pspii — RI - Proveedores de Servicios de Pago - Información Contable

`t-RI-PSPII.pdf`, 1 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 1}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_pspii/` (`divergencias_ri_pspii.json`, `estructura_ri_pspii.json`, `chunks_ri_pspii.json`).

### ri_psprca — RI - Proveedores de Servicios de Pago – Redes de Cajeros Automáticos

`t-RI-PSPRCA.pdf`, 6 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 6}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_psprca/` (`divergencias_ri_psprca.json`, `estructura_ri_psprca.json`, `chunks_ri_psprca.json`).

### ri_rcl — RI Cont. Mensual - Ratio de Cobertura de Liquidez

`t-RI-RCL.pdf`, 2 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 2}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_rcl/` (`divergencias_ri_rcl.json`, `estructura_ri_rcl.json`, `chunks_ri_rcl.json`).

### ri_rem — RI Cont. Mensual - Pago de Remuneraciones mediante Acreditación en Cuenta Bancaria.

`t-RI-Rem.pdf`, 2 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 2}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_rem/` (`divergencias_ri_rem.json`, `estructura_ri_rem.json`, `chunks_ri_rem.json`).

### ri_saofe — RI Cont. Mensual - Seguimiento de anticipos y otras financiaciones de exportaciones.

`t-RI-SAOFE.pdf`, 3 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 3}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_saofe/` (`divergencias_ri_saofe.json`, `estructura_ri_saofe.json`, `chunks_ri_saofe.json`).

### ri_secoexpo — RI Cont. Mensual - Seguimiento de las negociaciones de divisas de exportaciones de bienes.

`t-RI-SECOEXPO.pdf`, 21 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 21}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_secoexpo/` (`divergencias_ri_secoexpo.json`, `estructura_ri_secoexpo.json`, `chunks_ri_secoexpo.json`).

### ri_sef — RI Cont. Mensual - Unidades de servicios de las entidades financieras

`t-RI-SEF.pdf`, 10 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 10}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_sef/` (`divergencias_ri_sef.json`, `estructura_ri_sef.json`, `chunks_ri_sef.json`).

### ri_spi — RI Cont. Mensual - Seguimiento de Pagos de Importaciones.

`t-RI–SPI.pdf`, 11 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 11}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_spi/` (`divergencias_ri_spi.json`, `estructura_ri_spi.json`, `chunks_ri_spi.json`).

### ri_tar — RI Cont. Mensual - Financiamiento con tarjetas de crédito

`t-RI-TAR.pdf`, 7 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 7}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_tar/` (`divergencias_ri_tar.json`, `estructura_ri_tar.json`, `chunks_ri_tar.json`).

### ri_tii — RI Cont. Mensual - Transferencias Inmediatas Intraentidades

`t-RI-TII.pdf`, 6 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 6}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_tii/` (`divergencias_ri_tii.json`, `estructura_ri_tii.json`, `chunks_ri_tii.json`).

### ri_transpa — RI Cont. Mensual - Transparencia

`t-RI-Transpa.pdf`, 23 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 23}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_transpa/` (`divergencias_ri_transpa.json`, `estructura_ri_transpa.json`, `chunks_ri_transpa.json`).

### ri_tsa — RI para supervisión

`t-RI-TSA.pdf`, 92 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 92}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_tsa/` (`divergencias_ri_tsa.json`, `estructura_ri_tsa.json`, `chunks_ri_tsa.json`).

### ri_tvf — RI Cont. Mensual - Títulos Valores

`t-RI-TVF.pdf`, 5 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 5}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ri_tvf/` (`divergencias_ri_tvf.json`, `estructura_ri_tvf.json`, `chunks_ri_tvf.json`).

### ribspc — RI Cont. Mensual - Balance de Saldos.

`t-RIbspc.pdf`, 2 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"portada": 2}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/ribspc/` (`divergencias_ribspc.json`, `estructura_ribspc.json`, `chunks_ribspc.json`).

### seggar — Aplicación del sistema de seguro de garantía de depósitos.

`t-seggar.pdf`, 26 páginas (14 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H1 cobertura no exacta: parseadas=0, en estructura=0, duplicadas=0, huérfanas=507
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0
- C5 el índice anuncia 7 de 7 puntos que no aparecen en el cuerpo = 1.000 > 0.056
- C7 avisos de parseo 28 sobre 1 unidades = 28.000/u > 0.250/u; tipos: pagina_cuerpo_sin_seccion×14, contenido_antes_de_seccion×14

Roles de página: {"cuerpo": 14, "historial": 8, "indice": 1, "portada": 1, "tabla_norma_origen": 2}. Rechazos de header por motivo: {}. Avisos por tipo: {"pagina_cuerpo_sin_seccion": 14, "contenido_antes_de_seccion": 14}.

Detalle completo en `e0_dry/seggar/` (`divergencias_seggar.json`, `estructura_seggar.json`, `chunks_seggar.json`).

### seguef — Medidas mínimas de seguridad en entidades financieras

`t-seguef.pdf`, 25 páginas (0 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0

Señales adicionales (no deciden el veredicto):
- sin índice parseable: el contraste índice↔cuerpo no puede correrse

Roles de página: {"historial": 5, "portada": 18, "tabla_norma_origen": 2}. Rechazos de header por motivo: {}. Avisos por tipo: {}.

Detalle completo en `e0_dry/seguef/` (`divergencias_seguef.json`, `estructura_seguef.json`, `chunks_seguef.json`).

### verac — Veracidad de las registraciones contables

`t-verac.pdf`, 5 páginas (1 de cuerpo), 0 unidades (0 terminales + 0 mini-chunks).

Criterios incumplidos:
- H1 cobertura no exacta: parseadas=0, en estructura=0, duplicadas=0, huérfanas=30
- H2 el parser no engancha estructura: secciones=0, chunks terminales=0
- C5 el índice anuncia 6 de 6 puntos que no aparecen en el cuerpo = 1.000 > 0.056
- C7 avisos de parseo 2 sobre 1 unidades = 2.000/u > 0.250/u; tipos: pagina_cuerpo_sin_seccion×1, contenido_antes_de_seccion×1

Roles de página: {"cuerpo": 1, "historial": 1, "indice": 1, "portada": 1, "tabla_norma_origen": 1}. Rechazos de header por motivo: {}. Avisos por tipo: {"pagina_cuerpo_sin_seccion": 1, "contenido_antes_de_seccion": 1}.

Detalle completo en `e0_dry/verac/` (`divergencias_verac.json`, `estructura_verac.json`, `chunks_verac.json`).

## 7. TOs digeribles con señales de atención

- **rdbcra** (Régimen disciplinario a cargo del Banco Central de la República Argentina (Leyes 21.526 y 25.065) y tramitación de sumarios cambiarios (Ley 19.359)): sin índice parseable: el contraste índice↔cuerpo no puede correrse; 8 saltos de numeración (peor del subset: 2)
- **pimf** (Principios para las infraestructuras del mercado financiero.): 4 saltos de numeración (peor del subset: 2)
- **snp_tr_nc** (Sistema Nacional de Pagos - Transferencias - Normas complementarias.): 15 unidades del cuerpo no anunciadas por el índice (peor del subset: 12)
- **finsec** (Financiamiento al sector público no financiero): 13 unidades del cuerpo no anunciadas por el índice (peor del subset: 12)
- **snp_cec** (Sistema Nacional de Pagos - Cámaras electrónicas de compensación): sin índice parseable: el contraste índice↔cuerpo no puede correrse
- **disres** (Distribución de resultados): 16 unidades del cuerpo no anunciadas por el índice (peor del subset: 12)
- **secfin** (Secreto financiero): sin índice parseable: el contraste índice↔cuerpo no puede correrse

