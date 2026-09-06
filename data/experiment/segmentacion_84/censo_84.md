# Censo B5.8.0 — familias de formato de los 84 TOs «necesita reglas»

Unidad **B5.8.0** (secuencia B5.8, `docs/diseno_B5.8_segmentacion_universal.md`;
adenda `docs/adenda_laudo_B5.5_segmentacion_universal.md`). Diagnóstico puro,
USD 0 de API: clasificación mecánica con reglas visibles en
`code/medir_84.py` (mediciones, E0 vigente importado en solo lectura) y
`code/clasificar_84.py` (árbol de decisión). Este documento se regenera con:

```bash
python3 data/experiment/segmentacion_84/code/medir_84.py
python3 data/experiment/segmentacion_84/code/clasificar_84.py
python3 data/experiment/segmentacion_84/code/generar_reporte_84.py
```

Universo: los 84 TOs con veredicto «necesita reglas» en
`escalado_prep/veredictos_generalizacion.json` (recomputado: 84 = 53 RI + 31 normativa general). La medición «vigente» usa
el `e0_lib.py` actual (post-B5.2); los conteos «sellado» citan el E0 en
seco de `escalado_prep/e0_dry/` (pre-B5.2). Evidencia por TO íntegra en
`censo_84.json` (páginas, líneas de muestra verbatim, conteos).

## 1. Tally por familia primaria

| familia primaria | total | RI | no-RI |
|---|--:|--:|--:|
| a — compuerta de rol de página (sin índice) | 44 | 42 | 2 |
| b_idx — marcador de índice (variante / B5.2) | 7 | 4 | 3 |
| b_sec — marcador de sección variante | 1 | 0 | 1 |
| b_pts — estructura enganchada, fallas C4/C5/C7/C8 | 22 | 5 | 17 |
| c — cuerpo sin marcador de sección | 9 | 2 | 7 |
| e — otra / no segmentable candidato | 1 | 0 | 1 |
| **suma** | **84** | **53** | **31** |

Veredicto preliminar: **70 segmentables con regla de familia** / **2 parcialmente segmentables (preámbulo sí, cuerpo ficha/lista a declarar)** / **12 candidatos a NO segmentable** (detalle §4). Suma 84.

## 2. Tabla TO × familia (84 filas)

`unid.` = unidades de extracción del E0 en seco sellado; familias y
evidencia = medición vigente. Muestras verbatim completas en `censo_84.json`.

| TO | cat | pág | unid. | primaria | secundarias | evidencia | veredicto preliminar |
|---|---|--:|--:|---|---|---|---|
| ceninf | NG | 23 | 0 | a | d | 23 páginas, roles vigentes {'portada': 20, 'historial': 3} — sin página de índice · espina p.2: «1.1. Base de datos.» | segmentable con regla de familia a (modo sin raíz de sección, B5.8.1) |
| dmrd | NG | 72 | 0 | a | d_dominante | 72 páginas, roles vigentes {'portada': 72} — sin página de índice · espina p.6: «1. Denominación o razón social de la entidad » | segmentable — B5.8.1 (espina de puntos) + B5.8.3 (tabular dominante) |
| manual | RI | 2037 | 0 | a | ficha, jerarquia_alternativa | 2037 páginas, roles vigentes {'portada': 2037} — sin página de índice · espina p.2: «1.1. Las entidades deberán adaptar su contabi» | parcialmente segmentable — preámbulo con espina (B5.8.1); el cuerpo dominante es ficha/lis |
| plandecuentas | RI | 77 | 0 | a | lista_codigos, sin_espina | 77 páginas, roles vigentes {'portada': 77} — sin página de índice | candidato a NO segmentable en esta secuencia — familia ficha/lista: exige parser de regist |
| ri2_cs | RI | 31 | 0 | a | d | 31 páginas, roles vigentes {'portada': 31} — sin página de índice · espina p.1: «1. Información para el Banco Central» | segmentable con regla de familia a (modo sin raíz de sección, B5.8.1) |
| ri2_pm | RI | 376 | 0 | a | ficha, b_sec | 376 páginas, roles vigentes {'portada': 376} — sin página de índice · espina p.1: «1.1. Las casas y agencias de cambio deberán a» | parcialmente segmentable — preámbulo con espina (B5.8.1); el cuerpo dominante es ficha/lis |
| ri_acsf | RI | 3 | 0 | a | d_dominante, sin_espina | 3 páginas, roles vigentes {'portada': 3} — sin página de índice | segmentable (tabular) — parser B5.8.3; sin espina de puntos utilizable |
| ri_ao | RI | 1 | 0 | a | — | 1 páginas, roles vigentes {'portada': 1} — sin página de índice · espina p.1: «1. Clave Única de Identificación Tributaria (» | segmentable con regla de familia a (modo sin raíz de sección, B5.8.1) |
| ri_bdp | RI | 3 | 0 | a | — | 3 páginas, roles vigentes {'portada': 3} — sin página de índice · espina p.1: «17. BASE DE DATOS PADRÓN (R.I. – B.P.)» | segmentable con regla de familia a (modo sin raíz de sección, B5.8.1) |
| ri_ccpnp | RI | 11 | 0 | a | d_dominante | 11 páginas, roles vigentes {'portada': 11} — sin página de índice · espina p.1: «1. Las disposiciones enunciadas en el present» | segmentable — B5.8.1 (espina de puntos) + B5.8.3 (tabular dominante) |
| ri_chr | RI | 1 | 0 | a | — | 1 páginas, roles vigentes {'portada': 1} — sin página de índice · espina p.1: «11. CHEQUES RECHAZADOS Y DENUNCIADOS.» | candidato a NO segmentable — espina insuficiente (1 labels en 1 pág), 0.0 % en tabla, sin  |
| ri_con | RI | 16 | 0 | a | sin_espina | 16 páginas, roles vigentes {'portada': 16} — sin página de índice | candidato a NO segmentable — espina insuficiente (0 labels en 16 pág), 0.0 % en tabla, sin |
| ri_cr | RI | 5 | 0 | a | d_dominante | 5 páginas, roles vigentes {'portada': 5} — sin página de índice · espina p.1: «22. REGIMEN INFORMATIVO SOBRE RECLAMOS» | segmentable — B5.8.1 (espina de puntos) + B5.8.3 (tabular dominante) |
| ri_dsf | RI | 31 | 0 | a | d | 31 páginas, roles vigentes {'portada': 31} — sin página de índice · espina p.1: «2.1.4. de las normas sobre “Cesión de cartera» | segmentable con regla de familia a (modo sin raíz de sección, B5.8.1) |
| ri_esd | RI | 3 | 0 | a | d | 3 páginas, roles vigentes {'portada': 3} — sin página de índice · espina p.2: «1. Asistencia crediticia» | segmentable con regla de familia a (modo sin raíz de sección, B5.8.1) |
| ri_fcem | RI | 1 | 0 | a | sin_espina | 1 páginas, roles vigentes {'portada': 1} — sin página de índice | candidato a NO segmentable — espina insuficiente (0 labels en 1 pág), 0.0 % en tabla, sin  |
| ri_icpipsp | RI | 13 | 0 | a | jerarquia_alternativa | 13 páginas, roles vigentes {'portada': 13} — sin página de índice · espina p.1: «1. Sujetos alcanzados.» | segmentable con regla de familia a (modo sin raíz de sección, B5.8.1) |
| ri_ieccm | RI | 1 | 0 | a | — | 1 páginas, roles vigentes {'portada': 1} — sin página de índice · espina p.1: «1. Sujetos alcanzados» | segmentable con regla de familia a (modo sin raíz de sección, B5.8.1) |
| ri_iepsp | RI | 9 | 0 | a | jerarquia_alternativa | 9 páginas, roles vigentes {'portada': 9} — sin página de índice · espina p.1: «1. Sujetos alcanzados.» | segmentable con regla de familia a (modo sin raíz de sección, B5.8.1) |
| ri_iesinap | RI | 6 | 0 | a | jerarquia_alternativa | 6 páginas, roles vigentes {'portada': 6} — sin página de índice · espina p.1: «1. Sujetos alcanzados» | segmentable con regla de familia a (modo sin raíz de sección, B5.8.1) |
| ri_ii_31_12_19 | RI | 21 | 0 | a | — | 21 páginas, roles vigentes {'portada': 21} — sin página de índice · espina p.1: «20. INFORMACION INSTITUCIONAL DE ENTIDADES» | segmentable con regla de familia a (modo sin raíz de sección, B5.8.1) |
| ri_itme | RI | 1 | 0 | a | sin_espina | 1 páginas, roles vigentes {'portada': 1} — sin página de índice | candidato a NO segmentable — espina insuficiente (0 labels en 1 pág), 0.0 % en tabla, sin  |
| ri_laft | RI | 45 | 0 | a | d_dominante, lista_codigos, jerarquia_alternativa | 45 páginas, roles vigentes {'portada': 45} — sin página de índice · espina p.1: «1. Instrucciones generales» | segmentable — B5.8.1 (espina de puntos) + B5.8.3 (tabular dominante) |
| ri_mmsef | RI | 9 | 0 | a | — | 9 páginas, roles vigentes {'portada': 9} — sin página de índice · espina p.1: «19. MEDIDAS MÍNIMAS DE SEGURIDAD EN ENTIDADES» | segmentable con regla de familia a (modo sin raíz de sección, B5.8.1) |
| ri_nge | RI | 3 | 0 | a | — | 3 páginas, roles vigentes {'portada': 3} — sin página de índice · espina p.1: «1. Normas Generales» | segmentable con regla de familia a (modo sin raíz de sección, B5.8.1) |
| ri_niif | RI | 86 | 0 | a | d_dominante | 86 páginas, roles vigentes {'portada': 86} — sin página de índice · espina p.1: «2.1. Disposiciones generales respecto de los » | segmentable — B5.8.1 (espina de puntos) + B5.8.3 (tabular dominante) |
| ri_oc | RI | 28 | 0 | a | d | 28 páginas, roles vigentes {'portada': 28} — sin página de índice · espina p.3: «1.1. Por las ventas de billetes y divisas en » | segmentable con regla de familia a (modo sin raíz de sección, B5.8.1) |
| ri_ot | RI | 6 | 0 | a | — | 6 páginas, roles vigentes {'portada': 6} — sin página de índice · espina p.3: «1. Fecha de concertación de la operación» | segmentable con regla de familia a (modo sin raíz de sección, B5.8.1) |
| ri_pfmipyme | RI | 1 | 0 | a | sin_espina | 1 páginas, roles vigentes {'portada': 1} — sin página de índice | candidato a NO segmentable — espina insuficiente (0 labels en 1 pág), 0.0 % en tabla, sin  |
| ri_pnp | RI | 44 | 0 | a | d | 44 páginas, roles vigentes {'portada': 44} — sin página de índice · espina p.1: «1. Apartado I – Plan de Negocios» | segmentable con regla de familia a (modo sin raíz de sección, B5.8.1) |
| ri_pscpp | RI | 1 | 0 | a | sin_espina | 1 páginas, roles vigentes {'portada': 1} — sin página de índice | candidato a NO segmentable — espina insuficiente (0 labels en 1 pág), 0.0 % en tabla, sin  |
| ri_pspapt | RI | 5 | 0 | a | d, b_sec | 5 páginas, roles vigentes {'portada': 5} — sin página de índice · espina p.2: «1. Clave Única de Identificación Tributaria (» | segmentable con regla de familia a (modo sin raíz de sección, B5.8.1) |
| ri_pspii | RI | 1 | 0 | a | — | 1 páginas, roles vigentes {'portada': 1} — sin página de índice · espina p.1: «1. Estados Contables» | candidato a NO segmentable — espina insuficiente (2 labels en 1 pág), 7.2 % en tabla, sin  |
| ri_psprca | RI | 6 | 0 | a | d, b_sec | 6 páginas, roles vigentes {'portada': 6} — sin página de índice · espina p.2: «1. C.U.I.T. del propietario del ATM de la ope» | segmentable con regla de familia a (modo sin raíz de sección, B5.8.1) |
| ri_rcl | RI | 2 | 0 | a | — | 2 páginas, roles vigentes {'portada': 2} — sin página de índice · espina p.1: «21. Ratio de Cobertura de Liquidez» | segmentable con regla de familia a (modo sin raíz de sección, B5.8.1) |
| ri_rem | RI | 2 | 0 | a | — | 2 páginas, roles vigentes {'portada': 2} — sin página de índice · espina p.1: «9. PAGO DE REMUNERACIONES MEDIANTE ACREDITACI» | candidato a NO segmentable — espina insuficiente (2 labels en 2 pág), 0.0 % en tabla, sin  |
| ri_saofe | RI | 3 | 0 | a | — | 3 páginas, roles vigentes {'portada': 3} — sin página de índice · espina p.2: «1. Operaciones bajo seguimiento de la entidad» | segmentable con regla de familia a (modo sin raíz de sección, B5.8.1) |
| ri_secoexpo | RI | 21 | 0 | a | d | 21 páginas, roles vigentes {'portada': 21} — sin página de índice · espina p.1: «25. SEGUIMIENTO DE LAS NEGOCIACIONES DE DIVIS» | segmentable con regla de familia a (modo sin raíz de sección, B5.8.1) |
| ri_sef | RI | 10 | 0 | a | d | 10 páginas, roles vigentes {'portada': 10} — sin página de índice · espina p.1: «18. UNIDADES DE SERVICIOS DE LAS ENTIDADES FI» | segmentable con regla de familia a (modo sin raíz de sección, B5.8.1) |
| ri_spi | RI | 11 | 0 | a | sin_espina, jerarquia_alternativa | 11 páginas, roles vigentes {'portada': 11} — sin página de índice | candidato a NO segmentable — espina insuficiente (0 labels en 11 pág), 7.1 % en tabla, sin |
| ri_tar | RI | 7 | 0 | a | — | 7 páginas, roles vigentes {'portada': 7} — sin página de índice · espina p.1: «1. Instrucciones Generales.» | segmentable con regla de familia a (modo sin raíz de sección, B5.8.1) |
| ri_tii | RI | 6 | 0 | a | sin_espina | 6 páginas, roles vigentes {'portada': 6} — sin página de índice | candidato a NO segmentable — espina insuficiente (0 labels en 6 pág), 13.1 % en tabla, sin |
| ri_tvf | RI | 5 | 0 | a | — | 5 páginas, roles vigentes {'portada': 5} — sin página de índice · espina p.1: «13. Títulos Valores» | segmentable con regla de familia a (modo sin raíz de sección, B5.8.1) |
| ribspc | RI | 2 | 0 | a | — | 2 páginas, roles vigentes {'portada': 2} — sin página de índice · espina p.1: «1. El “Balance de saldos” se preparará con lo» | segmentable con regla de familia a (modo sin raíz de sección, B5.8.1) |
| consyr | NG | 11 | 0 | b_idx | — | candidato de índice no contemplado p.2: «Índice -» · espina p.2: «1. Instrumentación de documentos» | segmentable con regla de familia b (marcador, B5.8.2) |
| nmaeef | NG | 69 | 0 | b_idx | jerarquia_alternativa | candidato de índice no contemplado p.1: «INDICE» · espina p.2: «1. Designación de auditores externos.» | segmentable con regla de familia b (marcador, B5.8.2) |
| ri_dcpc | RI | 44 | 0 | b_idx | b_sec | candidato de índice no contemplado p.1: «INDICE» · espina p.1: «2.1. Orden de los rubros» | segmentable con regla de familia b (marcador, B5.8.2) |
| ri_msrl | RI | 20 | 0 | b_idx | d | candidato de índice no contemplado p.1: «ÍNDICE» · espina p.4: «3.1. Detalle de conceptos» | segmentable con regla de familia b (marcador, B5.8.2) |
| ri_psp | RI | 14 | 0 | b_idx | d, b_sec | candidato de índice no contemplado p.1: «INDICE» · espina p.5: «1. Cantidad de operaciones» | segmentable con regla de familia b (marcador, B5.8.2) |
| ri_tsa | RI | 92 | 0 | b_idx | d | regla B5.2 vigente ya lo engancha (cuerpo 0→30, secciones en cuerpo 31); re-corrida pendiente (B5.8.4) · espina p.1: «1. Normas generales.» | segmentable — regla vigente (B5.2); verificar re-corrida en B5.8.4 |
| seguef | NG | 25 | 0 | b_idx | — | candidato de índice no contemplado p.2: «– Índice –» · espina p.2: «2.1. Sistema de monitoreo remoto a distancia.» | segmentable con regla de familia b (marcador, B5.8.2) |
| reqcac | NG | 10 | 0 | b_sec | sin_espina | marcador variante (seccion_romana) p.2: «Sección C. Controles a los Sistemas de Información» | segmentable con regla de familia b (marcador, B5.8.2) |
| cateloc | NG | 67 | 2 | b_pts | c8_tramo_gigante | estructura enganchada (2 unidades), falla dominante: C8 chunk terminal más grande 126723 chars > 26182 chars (señal de tramo no segmentado) · espina p.66: «1. “A” 5355 4. | segmentable con regla de familia b (afinado de numeración/marcadores, B5.8.2) |
| cirmo3 | NG | 107 | 240 | b_pts | — | estructura enganchada (240 unidades), falla dominante: C5 el índice anuncia 12 de 21 puntos que no aparecen en el cuerpo = 0.571 > 0.056 · espina p.2: «1.1. Línea monetar | segmentable con regla de familia b (afinado de numeración/marcadores, B5.8.2) |
| garant | NG | 25 | 104 | b_pts | umbral_marginal | estructura enganchada (104 unidades), falla dominante: C7 avisos de parseo 32 sobre 104 unidades = 0.308/u > 0.250/u; tipos: aceptado_con_columna_derivada×32 · espina p.2 | segmentable hoy (umbral marginal) — adjudicar en B5.8.4; afinado opcional B5.8.2 |
| garopt | NG | 15 | 41 | b_pts | — | estructura enganchada (41 unidades), falla dominante: C5 el índice anuncia 4 de 16 puntos que no aparecen en el cuerpo = 0.250 > 0.056 · espina p.2: «1. 1. Alcance.» | segmentable con regla de familia b (afinado de numeración/marcadores, B5.8.2) |
| horari | NG | 13 | 13 | b_pts | — | estructura enganchada (13 unidades), falla dominante: C4 rechazos de header 11 sobre 13 unidades = 0.846/u > 0.214/u; motivos dominantes: resto_vacio_referencia_env · esp | segmentable con regla de familia b (afinado de numeración/marcadores, B5.8.2) |
| inspag | NG | 60 | 75 | b_pts | — | estructura enganchada (75 unidades), falla dominante: C5 el índice anuncia 18 de 55 puntos que no aparecen en el cuerpo = 0.327 > 0.056 · espina p.2: «1.1. Dimensiones de | segmentable con regla de familia b (afinado de numeración/marcadores, B5.8.2) |
| jafip | NG | 31 | 91 | b_pts | umbral_marginal | estructura enganchada (91 unidades), falla dominante: C4 rechazos de header 21 sobre 91 unidades = 0.231/u > 0.214/u; motivos dominantes: fuera_de_seccion_5×18, pro · esp | segmentable hoy (umbral marginal) — adjudicar en B5.8.4; afinado opcional B5.8.2 |
| manori | NG | 99 | 16 | b_pts | jerarquia_alternativa, c8_tramo_gigante | estructura enganchada (16 unidades), falla dominante: C4 rechazos de header 188 sobre 16 unidades = 11.750/u > 0.214/u; motivos dominantes: fuera_de_seccion_1×18, p · esp | segmentable con regla de familia b (afinado de numeración/marcadores, B5.8.2) |
| opecam | NG | 32 | 56 | b_pts | — | estructura enganchada (56 unidades), falla dominante: C5 el índice anuncia 4 de 20 puntos que no aparecen en el cuerpo = 0.200 > 0.056 · espina p.2: «1.1. Autorización.» | segmentable con regla de familia b (afinado de numeración/marcadores, B5.8.2) |
| ratio | NG | 46 | 132 | b_pts | jerarquia_alternativa, umbral_marginal | estructura enganchada (132 unidades), falla dominante: C7 avisos de parseo 35 sobre 132 unidades = 0.265/u > 0.250/u; tipos: aceptado_con_columna_derivada×35 · espina p.2 | segmentable hoy (umbral marginal) — adjudicar en B5.8.4; afinado opcional B5.8.2 |
| regpri | NG | 10 | 19 | b_pts | umbral_marginal | estructura enganchada (19 unidades), falla dominante: C4 rechazos de header 5 sobre 19 unidades = 0.263/u > 0.214/u; motivos dominantes: resto_vacio_referencia_envu · esp | segmentable hoy (umbral marginal) — adjudicar en B5.8.4; afinado opcional B5.8.2 |
| ri_ai | RI | 9 | 11 | b_pts | d | estructura enganchada (11 unidades), falla dominante: C4 rechazos de header 5 sobre 11 unidades = 0.455/u > 0.214/u; motivos dominantes: fuera_de_seccion_4×3, fuera · esp | segmentable con regla de familia b (afinado de numeración/marcadores, B5.8.2) |
| ri_cc | RI | 118 | 33 | b_pts | d, jerarquia_alternativa | estructura enganchada (33 unidades), falla dominante: C5 el índice anuncia 16 de 28 puntos que no aparecen en el cuerpo = 0.571 > 0.056 · espina p.1: «1. Normas Generales | segmentable con regla de familia b (afinado de numeración/marcadores, B5.8.2) |
| ri_gerc | RI | 8 | 15 | b_pts | d | estructura enganchada (15 unidades), falla dominante: C4 rechazos de header 8 sobre 15 unidades = 0.533/u > 0.214/u; motivos dominantes: fuera_de_seccion_2×6, no_su · esp | segmentable con regla de familia b (afinado de numeración/marcadores, B5.8.2) |
| ri_pgn | RI | 19 | 19 | b_pts | d, umbral_marginal | estructura enganchada (19 unidades), falla dominante: C7 avisos de parseo 7 sobre 19 unidades = 0.368/u > 0.250/u; tipos: aceptado_con_columna_derivada×7 · espina p.1: «1 | segmentable hoy (umbral marginal) — adjudicar en B5.8.4; afinado opcional B5.8.2 |
| ri_rml | RI | 77 | 27 | b_pts | d, c8_tramo_gigante | estructura enganchada (27 unidades), falla dominante: C4 rechazos de header 128 sobre 27 unidades = 4.741/u > 0.214/u; motivos dominantes: fuera_de_seccion_4×95, re · esp | segmentable con regla de familia b (afinado de numeración/marcadores, B5.8.2) |
| rmgcti | NG | 58 | 32 | b_pts | — | estructura enganchada (32 unidades), falla dominante: C5 el índice anuncia 34 de 46 puntos que no aparecen en el cuerpo = 0.739 > 0.056 · espina p.2: «1.1. Sujetos obliga | segmentable con regla de familia b (afinado de numeración/marcadores, B5.8.2) |
| snp_cheq | NG | 159 | 540 | b_pts | — | estructura enganchada (540 unidades), falla dominante: C4 rechazos de header 285 sobre 540 unidades = 0.528/u > 0.214/u; motivos dominantes: fuera_de_seccion_7×224,  · es | segmentable con regla de familia b (afinado de numeración/marcadores, B5.8.2) |
| snp_dd | NG | 68 | 53 | b_pts | d, c8_tramo_gigante | estructura enganchada (53 unidades), falla dominante: C4 rechazos de header 144 sobre 53 unidades = 2.717/u > 0.214/u; motivos dominantes: fuera_de_seccion_6×97, fu · esp | segmentable con regla de familia b (afinado de numeración/marcadores, B5.8.2) |
| snp_mep | NG | 50 | 46 | b_pts | ficha, c8_tramo_gigante | estructura enganchada (46 unidades), falla dominante: C5 el índice anuncia 8 de 25 puntos que no aparecen en el cuerpo = 0.320 > 0.056 · espina p.2: «1.1. Definición» | segmentable con regla de familia b (afinado de numeración/marcadores, B5.8.2) |
| snp_tr | NG | 62 | 89 | b_pts | d | estructura enganchada (89 unidades), falla dominante: C4 rechazos de header 119 sobre 89 unidades = 1.337/u > 0.214/u; motivos dominantes: fuera_de_seccion_1×86, pr · esp | segmentable con regla de familia b (afinado de numeración/marcadores, B5.8.2) |
| venliq | NG | 10 | 16 | b_pts | — | estructura enganchada (16 unidades), falla dominante: C5 el índice anuncia 7 de 14 puntos que no aparecen en el cuerpo = 0.500 > 0.056 · espina p.2: «1.1. Condiciones gen | segmentable con regla de familia b (afinado de numeración/marcadores, B5.8.2) |
| asomut | NG | 7 | 0 | c | — | 3 páginas de cuerpo vigentes, 0 líneas con formato de marcador de sección (ni variante) · espina p.2: «1. Actividad financiera.» | segmentable con regla de familia a/c (raíz sintética de B5.8.1) |
| cedin | NG | 22 | 0 | c | — | 16 páginas de cuerpo vigentes, 0 líneas con formato de marcador de sección (ni variante) · espina p.2: «1. Alta del CEDIN.» | segmentable con regla de familia a/c (raíz sintética de B5.8.1) |
| micemp | NG | 8 | 0 | c | — | 1 páginas de cuerpo vigentes, 0 líneas con formato de marcador de sección (ni variante) · espina p.3: «1. Determinación.» | segmentable con regla de familia a/c (raíz sintética de B5.8.1) |
| nmcief | NG | 36 | 0 | c | jerarquia_alternativa | 35 páginas de cuerpo vigentes, 0 líneas con formato de marcador de sección (ni variante) · espina p.2: «1. Control Interno:» | segmentable con regla de familia a/c (raíz sintética de B5.8.1) |
| ri2_ae | NG | 44 | 0 | c | jerarquia_alternativa | 41 páginas de cuerpo vigentes, 0 líneas con formato de marcador de sección (ni variante) · espina p.3: «1. Designación» | segmentable con regla de familia a/c (raíz sintética de B5.8.1) |
| ri_ccna | RI | 60 | 0 | c | d, jerarquia_alternativa | 58 páginas de cuerpo vigentes, 0 líneas con formato de marcador de sección (ni variante) · espina p.2: «1. Designación.» | segmentable con regla de familia a/c (raíz sintética de B5.8.1) |
| ri_transpa | RI | 23 | 0 | c | ficha, jerarquia_alternativa | 22 páginas de cuerpo vigentes, 0 líneas con formato de marcador de sección (ni variante) · espina p.2: «14. REGIMEN INFORMATIVO DE TRANSPARENCIA» | segmentable con regla de familia a/c (raíz sintética de B5.8.1) |
| seggar | NG | 26 | 0 | c | — | 14 páginas de cuerpo vigentes, 0 líneas con formato de marcador de sección (ni variante) · espina p.2: «5.1. Depósitos comprendidos.» | segmentable con regla de familia a/c (raíz sintética de B5.8.1) |
| verac | NG | 5 | 0 | c | — | 1 páginas de cuerpo vigentes, 0 líneas con formato de marcador de sección (ni variante) · espina p.2: «1. Alcances.» | segmentable con regla de familia a/c (raíz sintética de B5.8.1) |
| optico | NG | 43 | 0 | e | sin_espina | índice reconocido (4 pág) pero 0 páginas de cuerpo — roles vigentes: {'portada': 1, 'indice': 4, 'historial': 38} | candidato a NO segmentable — índice reconocido (4 pág) pero 0 páginas de cuerpo — roles vi |

## 3. Cruce con los números sellados

- **47/53 del RI en (a)** (scoping U-B5.6-0 §1.3, fe_erratas_D10 — medido PRE-B5.2 como «100 % portada»): la medición vigente los concilia exacto como **42 en (a)** + **4 en (b_idx)** (ri_dcpc, ri_msrl, ri_psp, ri_tsa) + **1 en (c)** (ri_transpa: compuerta abierta por B5.2, sigue sin sección) = 47.
- **desbloqueo esperado 44/53 por el modo sin raíz** (diseño B5.8 §1, sobre las familias PROSA+MIXTO del scoping): el censo por TO lo refina a **31 plenos vía B5.8.1** + 2 parciales (solo preámbulo) + 4 vía reglas de índice (B5.8.2/B5.2) + 5 ya enganchados con afinado — y **11 candidatos a NO segmentable** que las familias PROSA/MIXTO del scoping no distinguían (sin espina utilizable). Diferencia REPORTADA como hallazgo, no ajustada.
- **23/53 del RI alcanzados por tablas** (scoping §1.4): re-medición con la regla re-declarada da **23/53** con ≥15 % de palabras en tabla.
- **12,4 % de palabras del RI en tabla** (scoping §1.4: 69.543/562.622): re-medición da **69543/562622 = 12.4 %** (comando en §6).
- **62 TOs con cero unidades** (adenda §1): recomputado 62.
- **caso único (c) del RI** (`ri_ccna`, fe_erratas_D10): su clasificación vigente sigue siendo «c» — COINCIDE. El segundo RI en (c) es post-B5.2 (compuerta abierta), no un desacuerdo con lo sellado.

## 4. Candidatos a NO segmentable y parciales, con causa

| TO | cat | pág | estado | causa |
|---|---|--:|---|---|
| optico | NG | 43 | candidato NO | candidato a NO segmentable — índice reconocido (4 pág) pero 0 páginas de cuerpo — roles vigentes: {'portada': 1, 'indice': 4, 'historial': 3 |
| plandecuentas | RI | 77 | candidato NO | candidato a NO segmentable en esta secuencia — familia ficha/lista: exige parser de registro (fuera de B5.8.1-3); declarar en B5.8.4 |
| ri_chr | RI | 1 | candidato NO | candidato a NO segmentable — espina insuficiente (1 labels en 1 pág), 0.0 % en tabla, sin marcadores |
| ri_con | RI | 16 | candidato NO | candidato a NO segmentable — espina insuficiente (0 labels en 16 pág), 0.0 % en tabla, sin marcadores |
| ri_fcem | RI | 1 | candidato NO | candidato a NO segmentable — espina insuficiente (0 labels en 1 pág), 0.0 % en tabla, sin marcadores |
| ri_itme | RI | 1 | candidato NO | candidato a NO segmentable — espina insuficiente (0 labels en 1 pág), 0.0 % en tabla, sin marcadores |
| ri_pfmipyme | RI | 1 | candidato NO | candidato a NO segmentable — espina insuficiente (0 labels en 1 pág), 0.0 % en tabla, sin marcadores |
| ri_pscpp | RI | 1 | candidato NO | candidato a NO segmentable — espina insuficiente (0 labels en 1 pág), 0.0 % en tabla, sin marcadores |
| ri_pspii | RI | 1 | candidato NO | candidato a NO segmentable — espina insuficiente (2 labels en 1 pág), 7.2 % en tabla, sin marcadores |
| ri_rem | RI | 2 | candidato NO | candidato a NO segmentable — espina insuficiente (2 labels en 2 pág), 0.0 % en tabla, sin marcadores |
| ri_spi | RI | 11 | candidato NO | candidato a NO segmentable — espina insuficiente (0 labels en 11 pág), 7.1 % en tabla, sin marcadores |
| ri_tii | RI | 6 | candidato NO | candidato a NO segmentable — espina insuficiente (0 labels en 6 pág), 13.1 % en tabla, sin marcadores |
| manual | RI | 2037 | parcial | parcialmente segmentable — preámbulo con espina (B5.8.1); el cuerpo dominante es ficha/lista y exige parser de registro (fuera de B5.8.1-3): |
| ri2_pm | RI | 376 | parcial | parcialmente segmentable — preámbulo con espina (B5.8.1); el cuerpo dominante es ficha/lista y exige parser de registro (fuera de B5.8.1-3): |

## 5. Plan de reglas por familia (dimensiona B5.8.1–B5.8.4)

| regla | familia(s) | TOs que alcanza | sub-unidad |
|---|---|--:|---|
| modo de lectura sin raíz de sección (compuerta + raíz sintética) | a, c | 42 (incluye 2 parciales solo por su preámbulo) | **B5.8.1** |
| reglas de marcador por variante medida (índice/sección) | b_idx, b_sec | 7 | **B5.8.2** |
| afinado de numeración/rechazos + adjudicación de umbral | b_pts | 22 (de ellos 5 marginales) | **B5.8.2 / B5.8.4** |
| parser de tablas | d | 0 primarias + 6 con tabular dominante (≥40 %) + 21 con tabular presente (15–40 %) como secundaria | **B5.8.3** |
| re-corrida y verificación (reglas B5.2 ya vigentes) | b_idx/b_sec | 1 | **B5.8.4** |
| declaración de no segmentables (y cuerpos ficha/lista parciales) con causa | e y candidatos | 12 + 2 parciales | **B5.8.4** |

## 6. Hallazgos (discrepancias y novedades REPORTADAS, no ajustadas)

1. **Candidatos de marcador de índice en formato no contemplado** en 6 TOs (consyr, nmaeef, ri_dcpc, ri_msrl, ri_psp, seguef); estilos verbatim: «INDICE»; «ÍNDICE»; «Índice -»; «– Índice –». En particular `ri_dcpc` tiene «INDICE» en p.1: la sonda del scoping (regex `[íÍiI]ndice`, scoping:199) no matchea mayúsculas sostenidas, por lo que su conclusión «la palabra no está» (fe_erratas_D10 §b) queda matizada para estos TOs. La guarda B5.2 NO se invalida: la mención en prosa de `ri_dcpc` p.10 sigue siendo contraejemplo válido para un regex laxo sin requisito de mayúscula.
2. **`ri_tsa` está enganchado COMPLETO por las reglas B5.2 vigentes** («Índice» sin guiones en p.62 + secciones): cuerpo 0→30 y 31 headers. B5.2 midió y nombró a cedin, ri2_ae y ri_transpa; ri_tsa es un cuarto beneficiario no nombrado. Ojo: con el índice en p.62, las 61 páginas previas quedan `portada` — la re-corrida de B5.8.4 debe verificar qué contenido queda fuera.
3. **B5.2 abre compuertas pero no desbloquea**: cedin, ri2_ae y ri_transpa pasan a tener cuerpo (16, 41 y 22 páginas) y siguen en 0 secciones → 0 unidades. Consistente con el alcance declarado de B5.2; su vía es B5.8.1 (familia c).
4. **`optico` no contiene articulado**: índice reconocido (4 pág, 83 entradas «Sección N.») + 38 páginas de historial genuino de Comunicaciones + 0 páginas de cuerpo. Candidato a declarar en B5.8.4.
5. **El «desbloqueo esperado 44/53» se refina hacia abajo**: 31 RI plenos vía B5.8.1; 11 TOs del RI que las familias PROSA/MIXTO del scoping contaban como desbloqueables no tienen espina utilizable (≤2 labels) y pasan a candidatos a NO segmentable, con su causa por TO en §4.
6. **Ningún TO con unidades tiene a la tabularidad como falla dominante** (familia d primaria = 0): medida por exceso relativo sobre umbral, C6 nunca domina. La tabularidad dominante (≥40 %) aparece en 6 TOs, todos bloqueados antes por la compuerta — B5.8.3 los alcanza recién detrás de B5.8.1.
7. **`reqcac` usa secciones con LETRA** («Sección C. Controles…», detectada porque C es también numeral romano): la regla b_sec de B5.8.2 debe contemplar «Sección <letra>.», no solo romanos.

## 7. Comandos de recómputo

```bash
# universo y partición 53/31
python3 -c "import json,csv; v=json.load(open('data/experiment/escalado_prep/veredictos_generalizacion.json'))['por_to']; cat={r['id']:r['categoria'] for r in csv.DictReader(open('data/experiment/escalado_prep/inventario_unidades.csv'))}; nr=[k for k,d in v.items() if d['veredicto']=='necesita reglas']; print(len(nr), sum(1 for k in nr if cat[k]=='regimen_informativo'), sum(1 for k in nr if cat[k]=='normativa_general'))"
# tally por familia primaria (suma 84)
python3 -c "import json,collections; c=json.load(open('data/experiment/segmentacion_84/censo_84.json')); t=collections.Counter(x['familia_primaria'] for x in c.values()); print(dict(t), sum(t.values()))"
# agregado de palabras en tabla del RI (cruce con 12,4 % sellado)
python3 -c "import json; c=json.load(open('data/experiment/segmentacion_84/mediciones_84.json')); import csv; cat={r['id']:r['categoria'] for r in csv.DictReader(open('data/experiment/escalado_prep/inventario_unidades.csv'))}; ri=[d for k,d in c.items() if cat[k]=='regimen_informativo']; wi=sum(d['tablas']['palabras_en_tabla'] for d in ri); wt=sum(d['tablas']['palabras_total'] for d in ri); print(wi, wt, round(100*wi/wt,1))"
```
