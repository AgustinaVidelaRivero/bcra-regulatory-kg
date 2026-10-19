# Cifras del FRENO T1 de la tanda final (las genera freno_t1_cifras.py)

### 1. Las cifras con las que corre la tanda (versión derivada de T1, sección final)

| cifra | valor |
|---|---|
| documentos fuera | ninguno |
| U | 4951 |
| tarifa | 0.021115 |
| estimado (U × tarifa) | 104.5404 |
| tope (derivada, 2 decimales) | 151.58 |
| tramo 1: estimado | 12.6901 |
| tramo 2: estimado | 91.8502 |
| tramo_1: TOs y unidades | 30 y 601 |
| tramo_2: TOs y unidades | 68 y 4350 |
| base del control: costo_por_unidad_RI | 0.025952 |
| base del control: costo_por_unidad_NG_sin_raiz | 0.027403 |
| base del control: base_costo_por_unidad | 0.026331 |
| base del control: umbral_costo_por_unidad_1_3 | 0.03423 |
| base del control: costo_por_unidad_estimado | 0.021115 |
| base del control: base_proporcion_cola | 0.020073 |
| base del control: umbral_proporcion_cola_1_5 | 0.030109 |
| base del control: umbral_salidas_invalidas | 0.01 |
| base del control: umbral_errores | 0 |

### 2. La E0 de los 98 con el código del gate

| control | resultado |
|---|---|
| código de la raíz contra S0-6b | 3 de 3 (OK) |
| los 152 contra el manifiesto de S0-6b | 768 de 768, 152 TOs, 10478 unidades (OK) |
| las dos corridas de los 98 | 1512 y 1512 archivos, iguales: True |
| archivos por TO contra S0-6b | 490 de 490 |
| agregados contra los 152 restringidos | 7 de 7 iguales |
| version_e0.json | True |
| primer nivel | 498 archivos, faltan 0, sobran 0 |
| unidades | 4951 (cada TO con su unidades_por_to: True) |
| PDF contra S1-ter (dos carpetas) | 196 de 196 |
| control de salud | verde: True; diferencias con S2c: 0; veredictos {'cid': 15, 'cid+paginas_sin_seccion': 1, 'paginas_sin_seccion': 7, 'paginas_sin_seccion+unidades_anomalas_por_tamano': 1, 'sano': 71, 'unidades_anomalas_por_tamano': 3} |

### 3. El manifiesto (plano, en el repo) y la alternativa con el reparto

| cifra | plano (repo) | reparto (alternativa) |
|---|---|---|
| sha256 | 23654ef8a43900b2… | e9993b9dc87e8668… |
| TOs y unidades | 98 y 4951 | 98 y 4951 |
| estimado total | 104.749803 | 104.749803 |
| tramo 1 | 12.778594 | 19.310012 |
| tramo 2 | 91.971209 | 85.439791 |
| U × tarifa + 0,209440 (A3) | 104.749805 | 104.749805 |
| diferencia | -0.000002 | -0.000002 |
| líneas de A3 por documento, sumadas | 0.209438 | 0.209438 |
| resto del reparto | 0 | -0.000002 (al e3 de ratio) |
| tope | 151.5835 (exacto 151.58352925) | 151.5835 |
| con alcance / sin alcance | 85 / 13 | 85 / 13 |
| chars_completo de la E0 | 4770887 | 4770887 |
| tramo 1: proporción de las unidades y de los caracteres | 12.1 % y 18.4 % | igual |
| checkpoint_cada | {'ctavis': 150, 'depinv': 150, 'pimf': 150} | {'ctavis': 150, 'depinv': 150, 'pimf': 150} |
| archivos de la E0 en los sellos | 498 | 498 |

`orden_corrida`, tramo 1: ri_bdp, ri_ieccm, ri_rcl, ri_esd, verac, ri_acsf, ri_cr, ri_tvf, ribspc, asomut, micemp, ri_psp, ri_transpa, ri_iesinap, ri_msrl, ri_iepsp, ri_ai, ri_pspapt, ri_tsa, ri_tar, ri_laft, ri_dsf, ri_nge, ri_ot, consyr, ri_secoexpo, seggar, ri_sef, cedin, ri_ii_31_12_19.

`orden_corrida`, tramo 2: reqcac, cateloc, convca, socgar, horari, osapsa, snp_atm, pognme, evacre, regpri, cescar, ctacor, fgarcp, pscpp, secfin, incuca, venliq, fclef, lavdin, rmrtsd, ccbcra, apnf, traval, disres, relact, coltit, raapal, servco, retype, fabcra, ri2_ci, icmecma, pfmipyme, prevmi, fimipyme, garopt, actgar, gescre, snp_mep, opecam, ordcom, gracre, supcon, cryl, tasint, snp_debin, afiltr, autenf, rrci, rmgcti, repefe, snp_psp, jafip, inspag, graloc, adfsp, seguef, garant, snp_cec, snp_spd, snp_dd, ratio, ratiofn, finsec, snp_tr_nc, pimf, depinv, ctavis.

Sin alcance declarado (rol_alcance null): asomut, fimipyme, micemp, ratio, regpri, ri_cr, ri_dsf, ri_iesinap, ri_laft, ri_pspapt, ri_transpa, rmgcti, snp_mep.

### 4. El control de entradas

| control | OK |
|---|---|
| a_prefijo | True |
| b_tool_schema | True |
| c_namespace_e1 | True |
| d_prefijo_y_namespace_e3 | True |
| e_salida_tanda_final_r2b | True |
| f_candado_catalogo | True |
| g_temperatura | True |
| h_candados_y_selftest_claves | True |
| i_mensajes_e1_contra_la_base_de_a3 | True |
| j_herencia_recortada_tanda_final | True |
| k_rol_de_alcance | True |
| l_sellos_manifiesto_tanda_final | True |
| m_carga_y_control_en_contra | True |
| veredicto | OK |
| mensajes, tanda 0 | 2439 de 2439 iguales a la base de A3 |
| mensajes, tanda 1 | 3290 de 3290 iguales a la base de A3 |
| mensajes, tanda final | 1178 unidades de 33 documentos cambian, todas solo en la línea de alcance (1178); los otros, iguales: True |
| selftest_clave_cache sin cuentas = A3 sin cuentas (JSON, consola) | True, True; veredicto OK |
| control en contra | ri_bdp |
| recorte de herencia (tanda final) | {'ri_dsf': 2, 'ri_transpa': 8, 'snp_dd': 11} |

### 5. La corrida en seco: pedidos por etapa

| etapa | pedidos | claves distintas | modelos | max_tokens | temperaturas | namespaces |
|---|---|---|---|---|---|---|
| e1 | 5022 | 5015 | {'claude-haiku-4-5': 5022} | {'8192': 4958, '16384': 47, '40960': 17} | {'0': 5022} | {'e1_extraccion|cv=e1-extractor-v1-p322c5a23e9b7|think=0': 5022} |
| e1_reintento_forma | 5 | 5 | {'claude-haiku-4-5': 5} | {'8192': 5} | {'1': 5} | {'e1_extraccion|cv=e1-extractor-v1-p322c5a23e9b7-rforma1|think=0': 3, 'e1_extraccion|cv=e1-extractor-v1-p322c5a23e9b7-rforma2|think=0': 2} |
| e1_ratchet | 1 | 1 | {'claude-haiku-4-5': 1} | {'16384': 1} | {'0': 1} | {'e1_extraccion|cv=e1-extractor-v1-p322c5a23e9b7|think=0': 1} |
| e3 | 4956 | 4948 | {'claude-sonnet-5': 4956} | {'4096': 4956} | {'sin fijar': 4956} | {'e3_verificacion|cv=e3-verificador-v1-p21a836c7de6d|think=0': 4956} |

### 6. Las cinco ramas

| rama | unidades |
|---|---|
| corte y reintento por corte | 28 |
| partición por corte | {'cateloc::Sbloque10': 5, 'ri_transpa::Sbloque1::chapeau_seccion': 2} |
| tercer escalón | 17; cortan también: 0 |
| salida mal formada (rforma1 bien, reparada, error) | ['ri_bdp::S1'], ['ri_rcl::1.2'], ['ri_esd::S1'] |
| ratchet de E3 | {'unidad': 'ri_bdp::S2', 'verificaciones_e3': 2, 'reextracciones_e1': 1} |
| llamadas a la API | 0 |
| rc del runner | 0 |
| claves ya en las bases de la copia | {'e1_extraccion_db': 0, 'e1_reintentos_db': 0, 'e3_verificacion_db': 0} |
| primer intento de E1: pedidos y claves distintas | 4958 y 4951 (6 claves con más de un pedido) |

### 7. Las unidades que no entran en una llamada (capacidad del reintento con la p90: 10885.7 caracteres; del tercer escalón: 27214.1)

| unidad | caracteres | se parte | partes (caracteres) | mecanismo | en la corrida en seco |
|---|---|---|---|---|---|
| ri_psp::SIII::chapeau_seccion | 12911 | no (sin_items_detectables) | — | 8.192 → 16.384 → tercer escalón 40.960 (no se parte: sin_items_detectables) | tercer escalón |
| ri_transpa::Sbloque1::chapeau_seccion | 21712 | sí | [13705, 8006] | 8.192 → 16.384 → partición por corte; cada parte 8.192 → 16.384 → tercer escalón 40.960 (una parte no se vuelve a partir) | partes 2; con tercer escalón ['ri_transpa::Sbloque1::chapeau_seccion::parte1'] |
| ri_iepsp::A::S4 | 17386 | no (sin_items_detectables) | — | 8.192 → 16.384 → tercer escalón 40.960 (no se parte: sin_items_detectables) | tercer escalón |
| ri_tsa::S3 | 11830 | no (sin_items_detectables) | — | 8.192 → 16.384 → tercer escalón 40.960 (no se parte: sin_items_detectables) | tercer escalón |
| ri_tsa::3.2 | 14749 | no (sin_items_detectables) | — | 8.192 → 16.384 → tercer escalón 40.960 (no se parte: sin_items_detectables) | tercer escalón |
| ri_tsa::3.3.1 | 11663 | no (sin_items_detectables) | — | 8.192 → 16.384 → tercer escalón 40.960 (no se parte: sin_items_detectables) | tercer escalón |
| ri_laft::Sbloque3 | 18650 | no (sin_items_detectables) | — | 8.192 → 16.384 → tercer escalón 40.960 (no se parte: sin_items_detectables) | tercer escalón |
| ri_dsf::S8::chapeau_seccion | 13939 | no (sin_items_detectables) | — | 8.192 → 16.384 → tercer escalón 40.960 (no se parte: sin_items_detectables) | tercer escalón |
| ri_dsf::S10::parte2 | 12991 | no (sin_items_detectables) | — | 8.192 → 16.384 → tercer escalón 40.960 (no se parte: sin_items_detectables) | tercer escalón |
| seggar::8.2 | 19998 | no (sin_items_detectables) | — | 8.192 → 16.384 → tercer escalón 40.960 (no se parte: sin_items_detectables) | tercer escalón |
| reqcac::SB | 11111 | no (sin_items_detectables) | — | 8.192 → 16.384 → tercer escalón 40.960 (no se parte: sin_items_detectables) | tercer escalón |
| cateloc::Sbloque6 | 13753 | no (sin_items_detectables) | — | 8.192 → 16.384 → tercer escalón 40.960 (no se parte: sin_items_detectables) | tercer escalón |
| cateloc::Sbloque7 | 16797 | no (sin_items_detectables) | — | 8.192 → 16.384 → tercer escalón 40.960 (no se parte: sin_items_detectables) | tercer escalón |
| cateloc::Sbloque8 | 15779 | no (sin_items_detectables) | — | 8.192 → 16.384 → tercer escalón 40.960 (no se parte: sin_items_detectables) | tercer escalón |
| cateloc::Sbloque9 | 19633 | no (sin_items_detectables) | — | 8.192 → 16.384 → tercer escalón 40.960 (no se parte: sin_items_detectables) | tercer escalón |
| cateloc::Sbloque10 | 48321 | sí | [10758, 10257, 10863, 10091, 6348] | 8.192 → 16.384 → partición por corte; cada parte 8.192 → 16.384 → tercer escalón 40.960 (una parte no se vuelve a partir) | partes 5; con tercer escalón [] |
| ri2_ci::S5 | 11170 | no (sin_items_detectables) | — | 8.192 → 16.384 → tercer escalón 40.960 (no se parte: sin_items_detectables) | tercer escalón |
| rmgcti::S11 | 11244 | no (sin_items_detectables) | — | 8.192 → 16.384 → tercer escalón 40.960 (no se parte: sin_items_detectables) | tercer escalón |

Clase A (sin partición posible, sobre la capacidad del reintento): 16; sobre la capacidad con la mediana: 7; sobre el tercer escalón: 0; sin declarar: 0; entre 8.192 y 16.384 con la p90: 22.

### 8. El estimado por TO (tarifa del §3 y líneas de A3; el del manifiesto, plano; y el de la alternativa con el reparto)

| # | TO | tramo | unid. | chars_completo | e1 | e3 | total | = manifiesto | reparto (alternativa) | cortes p90 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | ri_bdp | 1 | 3 | 2902 | 0.030953 | 0.032940 | 0.063893 | True | 0.063716 | 0 |
| 2 | ri_ieccm | 1 | 4 | 895 | 0.041235 | 0.043920 | 0.085155 | True | 0.019651 | 0 |
| 3 | ri_rcl | 1 | 4 | 3253 | 0.041271 | 0.043920 | 0.085191 | True | 0.071423 | 0 |
| 4 | ri_esd | 1 | 5 | 8093 | 0.051588 | 0.054900 | 0.106488 | True | 0.177690 | 0 |
| 5 | verac | 1 | 5 | 2180 | 0.051549 | 0.054900 | 0.106449 | True | 0.047864 | 0 |
| 6 | ri_acsf | 1 | 6 | 3870 | 0.061906 | 0.065880 | 0.127786 | True | 0.084970 | 0 |
| 7 | ri_cr | 1 | 6 | 6552 | 0.060810 | 0.065880 | 0.126690 | True | 0.143856 | 0 |
| 8 | ri_tvf | 1 | 6 | 9154 | 0.061906 | 0.065880 | 0.127786 | True | 0.200986 | 0 |
| 9 | ribspc | 1 | 7 | 1223 | 0.072224 | 0.076860 | 0.149084 | True | 0.026852 | 0 |
| 10 | asomut | 1 | 8 | 3967 | 0.081080 | 0.087840 | 0.168920 | True | 0.087100 | 0 |
| 11 | micemp | 1 | 8 | 4215 | 0.081080 | 0.087840 | 0.168920 | True | 0.092545 | 0 |
| 12 | ri_psp | 1 | 9 | 75724 | 0.092850 | 0.098820 | 0.191670 | True | 1.662599 | 2 |
| 13 | ri_transpa | 1 | 11 | 72974 | 0.111485 | 0.120780 | 0.232265 | True | 1.602220 | 5 |
| 14 | ri_iesinap | 1 | 12 | 14185 | 0.121620 | 0.131760 | 0.253380 | True | 0.311446 | 1 |
| 15 | ri_msrl | 1 | 12 | 29163 | 0.123812 | 0.131760 | 0.255572 | True | 0.640304 | 2 |
| 16 | ri_iepsp | 1 | 13 | 24664 | 0.134631 | 0.142740 | 0.277371 | True | 0.541524 | 2 |
| 17 | ri_ai | 1 | 15 | 12882 | 0.154765 | 0.164700 | 0.319465 | True | 0.282838 | 0 |
| 18 | ri_pspapt | 1 | 16 | 10527 | 0.162160 | 0.175680 | 0.337840 | True | 0.231131 | 0 |
| 19 | ri_tsa | 1 | 17 | 53964 | 0.175267 | 0.186660 | 0.361927 | True | 1.184836 | 6 |
| 20 | ri_tar | 1 | 18 | 9894 | 0.185718 | 0.197640 | 0.383358 | True | 0.217233 | 0 |
| 21 | ri_laft | 1 | 26 | 62389 | 0.263510 | 0.285480 | 0.548990 | True | 1.369816 | 2 |
| 22 | ri_dsf | 1 | 28 | 58862 | 0.283780 | 0.307440 | 0.591220 | True | 1.292377 | 5 |
| 23 | ri_nge | 1 | 30 | 3183 | 0.309531 | 0.329400 | 0.638931 | True | 0.069886 | 0 |
| 24 | ri_ot | 1 | 32 | 44425 | 0.330166 | 0.351360 | 0.681526 | True | 0.975397 | 0 |
| 25 | consyr | 1 | 34 | 18930 | 0.350535 | 0.373320 | 0.723855 | True | 0.415628 | 0 |
| 26 | ri_secoexpo | 1 | 35 | 84076 | 0.361119 | 0.384300 | 0.745419 | True | 1.845976 | 1 |
| 27 | seggar | 1 | 36 | 39047 | 0.371155 | 0.395280 | 0.766435 | True | 0.857318 | 2 |
| 28 | ri_sef | 1 | 38 | 54929 | 0.392072 | 0.417240 | 0.809312 | True | 1.206024 | 0 |
| 29 | cedin | 1 | 66 | 50650 | 0.680450 | 0.724680 | 1.405130 | True | 1.112074 | 0 |
| 30 | ri_ii_31_12_19 | 1 | 91 | 112713 | 0.939386 | 0.999180 | 1.938566 | True | 2.474732 | 0 |
| 31 | reqcac | 2 | 3 | 19848 | 0.030957 | 0.032940 | 0.063897 | True | 0.435784 | 3 |
| 32 | cateloc | 2 | 11 | 178192 | 0.113408 | 0.120780 | 0.234188 | True | 3.912391 | 16 |
| 33 | convca | 2 | 12 | 7859 | 0.121620 | 0.131760 | 0.253380 | True | 0.172553 | 0 |
| 34 | socgar | 2 | 12 | 7616 | 0.121620 | 0.131760 | 0.253380 | True | 0.167217 | 0 |
| 35 | horari | 2 | 13 | 16326 | 0.134028 | 0.142740 | 0.276768 | True | 0.358454 | 1 |
| 36 | osapsa | 2 | 13 | 9388 | 0.131755 | 0.142740 | 0.274495 | True | 0.206123 | 0 |
| 37 | snp_atm | 2 | 16 | 7824 | 0.162160 | 0.175680 | 0.337840 | True | 0.171784 | 0 |
| 38 | pognme | 2 | 17 | 10578 | 0.172295 | 0.186660 | 0.358955 | True | 0.232251 | 0 |
| 39 | evacre | 2 | 19 | 10322 | 0.192565 | 0.208620 | 0.401185 | True | 0.22663 | 0 |
| 40 | regpri | 2 | 20 | 12798 | 0.202700 | 0.219600 | 0.422300 | True | 0.280993 | 0 |
| 41 | cescar | 2 | 21 | 12515 | 0.212835 | 0.230580 | 0.443415 | True | 0.274780 | 0 |
| 42 | ctacor | 2 | 21 | 27858 | 0.212835 | 0.230580 | 0.443415 | True | 0.611651 | 0 |
| 43 | fgarcp | 2 | 22 | 20348 | 0.222970 | 0.241560 | 0.464530 | True | 0.446762 | 0 |
| 44 | pscpp | 2 | 22 | 15442 | 0.222970 | 0.241560 | 0.464530 | True | 0.339045 | 0 |
| 45 | secfin | 2 | 22 | 13671 | 0.222970 | 0.241560 | 0.464530 | True | 0.300161 | 0 |
| 46 | incuca | 2 | 23 | 12779 | 0.233105 | 0.252540 | 0.485645 | True | 0.280576 | 0 |
| 47 | venliq | 2 | 23 | 15512 | 0.237127 | 0.252540 | 0.489667 | True | 0.340582 | 0 |
| 48 | fclef | 2 | 28 | 13092 | 0.283780 | 0.307440 | 0.591220 | True | 0.287449 | 0 |
| 49 | lavdin | 2 | 29 | 16091 | 0.293915 | 0.318420 | 0.612335 | True | 0.353295 | 0 |
| 50 | rmrtsd | 2 | 31 | 55324 | 0.314185 | 0.340380 | 0.654565 | True | 1.214696 | 0 |
| 51 | ccbcra | 2 | 32 | 14458 | 0.324320 | 0.351360 | 0.675680 | True | 0.317440 | 0 |
| 52 | apnf | 2 | 34 | 34404 | 0.344590 | 0.373320 | 0.717910 | True | 0.755376 | 0 |
| 53 | traval | 2 | 35 | 34951 | 0.354725 | 0.384300 | 0.739025 | True | 0.767386 | 0 |
| 54 | disres | 2 | 38 | 49553 | 0.385130 | 0.417240 | 0.802370 | True | 1.087988 | 0 |
| 55 | relact | 2 | 38 | 16138 | 0.385130 | 0.417240 | 0.802370 | True | 0.354327 | 0 |
| 56 | coltit | 2 | 39 | 12554 | 0.395265 | 0.428220 | 0.823485 | True | 0.275636 | 0 |
| 57 | raapal | 2 | 40 | 75398 | 0.405400 | 0.439200 | 0.844600 | True | 1.655442 | 0 |
| 58 | servco | 2 | 40 | 23301 | 0.405400 | 0.439200 | 0.844600 | True | 0.511598 | 0 |
| 59 | retype | 2 | 41 | 14689 | 0.415535 | 0.450180 | 0.865715 | True | 0.322512 | 0 |
| 60 | fabcra | 2 | 42 | 50398 | 0.425670 | 0.461160 | 0.886830 | True | 1.106541 | 0 |
| 61 | ri2_ci | 2 | 45 | 87646 | 0.456075 | 0.494100 | 0.950175 | True | 1.924359 | 2 |
| 62 | icmecma | 2 | 48 | 35317 | 0.486480 | 0.527040 | 1.013520 | True | 0.775422 | 0 |
| 63 | pfmipyme | 2 | 52 | 24484 | 0.527020 | 0.570960 | 1.097980 | True | 0.537572 | 0 |
| 64 | prevmi | 2 | 52 | 43978 | 0.527020 | 0.570960 | 1.097980 | True | 0.965583 | 0 |
| 65 | fimipyme | 2 | 55 | 33971 | 0.557425 | 0.603900 | 1.161325 | True | 0.745869 | 0 |
| 66 | garopt | 2 | 55 | 17566 | 0.567042 | 0.603900 | 1.170942 | True | 0.38568 | 0 |
| 67 | actgar | 2 | 60 | 25111 | 0.608100 | 0.658800 | 1.266900 | True | 0.551338 | 0 |
| 68 | gescre | 2 | 61 | 55584 | 0.618235 | 0.669780 | 1.288015 | True | 1.220405 | 1 |
| 69 | snp_mep | 2 | 62 | 100927 | 0.628370 | 0.680760 | 1.309130 | True | 2.215958 | 7 |
| 70 | opecam | 2 | 65 | 52645 | 0.670076 | 0.713700 | 1.383776 | True | 1.155876 | 0 |
| 71 | ordcom | 2 | 65 | 30269 | 0.658775 | 0.713700 | 1.372475 | True | 0.664587 | 0 |
| 72 | gracre | 2 | 67 | 32246 | 0.679045 | 0.735660 | 1.414705 | True | 0.707995 | 0 |
| 73 | supcon | 2 | 67 | 43638 | 0.679045 | 0.735660 | 1.414705 | True | 0.958118 | 0 |
| 74 | cryl | 2 | 68 | 51420 | 0.689180 | 0.746640 | 1.435820 | True | 1.12898 | 0 |
| 75 | tasint | 2 | 69 | 42906 | 0.699315 | 0.757620 | 1.456935 | True | 0.942046 | 0 |
| 76 | snp_debin | 2 | 71 | 39534 | 0.719585 | 0.779580 | 1.499165 | True | 0.868010 | 0 |
| 77 | afiltr | 2 | 72 | 135611 | 0.729720 | 0.790560 | 1.520280 | True | 2.977481 | 4 |
| 78 | autenf | 2 | 75 | 64379 | 0.760125 | 0.823500 | 1.583625 | True | 1.413508 | 0 |
| 79 | rrci | 2 | 77 | 80477 | 0.780395 | 0.845460 | 1.625855 | True | 1.766957 | 0 |
| 80 | rmgcti | 2 | 81 | 177552 | 0.820935 | 0.889380 | 1.710315 | True | 3.898339 | 2 |
| 81 | repefe | 2 | 87 | 59581 | 0.881745 | 0.955260 | 1.837005 | True | 1.308163 | 0 |
| 82 | snp_psp | 2 | 89 | 65823 | 0.902015 | 0.977220 | 1.879235 | True | 1.445213 | 0 |
| 83 | jafip | 2 | 91 | 59109 | 0.938196 | 0.999180 | 1.937376 | True | 1.297800 | 0 |
| 84 | inspag | 2 | 93 | 93049 | 0.958816 | 1.021140 | 1.979956 | True | 2.042988 | 0 |
| 85 | graloc | 2 | 100 | 89887 | 1.013500 | 1.098000 | 2.111500 | True | 1.973563 | 0 |
| 86 | adfsp | 2 | 101 | 101617 | 1.023635 | 1.108980 | 2.132615 | True | 2.231107 | 1 |
| 87 | seguef | 2 | 101 | 78432 | 1.041295 | 1.108980 | 2.150275 | True | 1.722056 | 0 |
| 88 | garant | 2 | 106 | 103227 | 1.092844 | 1.163880 | 2.256724 | True | 2.266457 | 0 |
| 89 | snp_cec | 2 | 122 | 111586 | 1.236470 | 1.339560 | 2.576030 | True | 2.449987 | 0 |
| 90 | snp_spd | 2 | 130 | 77944 | 1.317550 | 1.427400 | 2.744950 | True | 1.711342 | 0 |
| 91 | snp_dd | 2 | 131 | 175528 | 1.350590 | 1.438380 | 2.788970 | True | 3.853900 | 0 |
| 92 | ratio | 2 | 133 | 193950 | 1.347955 | 1.460340 | 2.808295 | True | 4.258373 | 0 |
| 93 | ratiofn | 2 | 133 | 70453 | 1.347955 | 1.460340 | 2.808295 | True | 1.546869 | 0 |
| 94 | finsec | 2 | 134 | 175268 | 1.358090 | 1.471320 | 2.829410 | True | 3.848192 | 1 |
| 95 | snp_tr_nc | 2 | 136 | 73218 | 1.378360 | 1.493280 | 2.871640 | True | 1.607578 | 0 |
| 96 | pimf | 2 | 165 | 110235 | 1.672275 | 1.811700 | 3.483975 | True | 2.420324 | 0 |
| 97 | depinv | 2 | 203 | 100305 | 2.057405 | 2.228940 | 4.286345 | True | 2.202301 | 0 |
| 98 | ctavis | 2 | 271 | 167702 | 2.746585 | 2.975580 | 5.722165 | True | 3.682072 | 0 |

Total: 4951 unidades, USD 104.749803 (104.7498 a 4 decimales); iguales al manifiesto: 98 de 98; tope 151.5835, margen 46.833697, tope sobre estimado 1.4471; el runner lo lee como 104.75; cota de la salida de los cortes con la p90: 3.4818.

### 9. El ensamblado del tramo 1 (salida stub con el TextoOrdenado)

| grafo | rc | nodos | aristas | kg sha256 | doble corrida interna | TOs | con nombres_remision |
|---|---|---|---|---|---|---|---|
| tanda_final_ens_tramo1_r2b | 0 | 716 | 855 | ac284ffdecfb0915… | True | 30 | 25 |
| tanda_final_ens_tramo1_r2b_sincola | 0 | 716 | 855 | ac284ffdecfb0915… | True | 30 | 25 |

### 10. Las pruebas del lanzador sobre la copia

| prueba | salida | TOs lanzados | freno por modelo (antes y después de cada TO) | control entre tramos | parada |
|---|---|---|---|---|---|
| lanzador_prueba_1.log | rc=0 | 3 | OK, OK, OK, OK | OK | — |
| lanzador_prueba_2_control_freno.log | rc=11 | 2 | OK, OK, OK | FRENO | FRENO del control entre tramos: decide la autora |
| lanzador_prueba_3_pausa.log | rc=20 | 0 | OK | — | pausa entre documentos (viernes 23/10/2026, 18:00): no se lanza el TO siguiente |
| lanzador_prueba_3b_antes_de_la_pausa.log | rc=0 | 3 | OK, OK, OK, OK | OK | — |
| lanzador_prueba_4_caso_en_contra_modelo.log | rc=10 | 0 | FRENO | — | freno por id de modelo antes del primer TO |

### 11. La duración y el costo estimados de T2

| cifra | valor |
|---|---|
| tanda 1: lanzamientos (min) | [13.5, 42.78, 756.97] |
| tanda 1: total (min) | 813.25 |
| segundos por unidad | 14.83 |
| tanda final por unidades (min, h) | 1223.8, 20.4 |
| tramo 1 y tramo 2 por unidades (min) | 148.6 y 1075.3 |
| tanda final por caracteres (min, h; información) | 995.5, 16.59 |
| tramo 1 y tramo 2 por caracteres (min) | 183.5 y 812.0 |
| freno por modelo (corridas, s, min) | 99, 1.62, 2.7 |
| estimado (USD) | 104.7498 |
| con la razón de la tanda 1 | 106.7505 (1.0191) |
| tope, margen, tope sobre estimado | 151.5835, 46.8337, 1.4471 |

### 12. Las comprobaciones de reproducción (comprobaciones_t1.py)

| comprobación | resultado |
|---|---|
| la E0 del repo contra la corrida 1 | 498 archivos, iguales: True |
| el manifiesto del repo contra el primer armado | True |
| la derivada regenerada (md, huecos) | True, True |
| corrida en seco: mis salidas 1 = 2, y 3 igual salvo la clave nueva | True, True (['stub_con_texto_ordenado']) |
| corrida en seco: consola y resumen iguales en las tres | True |
| corrida en seco: archivos del runner, los que difieren y por qué | 1775; 301: {'checkpoint_o_ultimo_checkpoint': 203, 'reporte_e2_igual_con_la_ruta_normalizada': 98} |
| ensamblado del tramo 1 en dos procesos | {'ens_tramo1_r2b': True, 'ens_tramo1_r2b_sincola': True} |
| bases de la caché del repo antes y después de las pruebas del freno | {'e1_extraccion.db': True, 'e1_reintentos.db': True, 'e3_verificacion.db': True} |
| todo igual | True |

### 13. sha256_para_T2.txt

499 renglones, sha256 `1cd0dd382b5fbd26d3e16237940a2406428a067bf914ab4cde048fca0da16b8c`.
