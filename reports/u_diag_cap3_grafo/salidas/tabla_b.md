# Tarea b: nodos de contenido con el punto en un ancestro de su unidad

Fuente: `procedencia_b.json` (`udiag_b_procedencia.py`). Clase de VERIF: la regla de VERIF-CAP3-COHERENCIA, tarea d. Diagnóstico: `verificar_tramo` del validador r2, holgura 2.

## diez: 222 nodos; clase de VERIF parrafo_del_ancestro 109; cruza_titulo_y_parrafo_del_ancestro 61; titulo_del_ancestro 23; no_ubicado 22; texto_propio_de_la_unidad 7

Los 113 cuyo tramo no está en el párrafo del ancestro, por diagnóstico y por clase de VERIF:

| diagnóstico | cruza_titulo_y_parrafo_del_ancestro | no_ubicado | texto_propio_de_la_unidad | titulo_del_ancestro | total |
|---|---:|---:|---:|---:|---:|
| rol_mal:deberia_ser_el_parrafo_heredado | 61 | 0 | 0 | 3 | 64 |
| punto_y_rol_coherentes:tramo_en_el_titulo_del_ancestro | 0 | 0 | 0 | 20 | 20 |
| punto_mal_atribuido:a_la_unidad | 0 | 11 | 7 | 0 | 18 |
| no_ubicado | 0 | 7 | 0 | 0 | 7 |
| punto_mal_atribuido:a_otro_ancestro | 0 | 4 | 0 | 0 | 4 |

G restringida (G-r) en los 222: cambia el punto 22 ({'Operacion': 9, 'Obligacion': 8, 'Potestad': 4, 'Restriccion': 1}); solo el rol 173; sin cambio 27.

- g_restringida_en_todos_los_nodos_de_contenido: cambian el punto 22 ({'ancestro->unidad': 18, 'ancestro->ancestro': 4}; por tipo {'Operacion': 9, 'Obligacion': 8, 'Potestad': 4, 'Restriccion': 1}); solo el rol 173; ids que se fusionarían 0; pertenencias a subgrafos de hermanas que se pierden (§5.6) 145.
- g_literal_en_todos_los_nodos_de_contenido: cambian el punto 149 ({'unidad->ancestro': 127, 'ancestro->unidad': 18, 'ancestro->ancestro': 4}; por tipo {'Operacion': 43, 'Condicion': 36, 'Obligacion': 26, 'Potestad': 22, 'Excepcion': 15, 'Restriccion': 6, 'Definicion': 1}); solo el rol 173; ids que se fusionarían 7; pertenencias a subgrafos de hermanas que se pierden (§5.6) 145.

## sincola: 208 nodos; clase de VERIF parrafo_del_ancestro 101; cruza_titulo_y_parrafo_del_ancestro 58; titulo_del_ancestro 23; no_ubicado 20; texto_propio_de_la_unidad 6

Los 107 cuyo tramo no está en el párrafo del ancestro, por diagnóstico y por clase de VERIF:

| diagnóstico | cruza_titulo_y_parrafo_del_ancestro | no_ubicado | texto_propio_de_la_unidad | titulo_del_ancestro | total |
|---|---:|---:|---:|---:|---:|
| rol_mal:deberia_ser_el_parrafo_heredado | 58 | 0 | 0 | 3 | 61 |
| punto_y_rol_coherentes:tramo_en_el_titulo_del_ancestro | 0 | 0 | 0 | 20 | 20 |
| punto_mal_atribuido:a_la_unidad | 0 | 11 | 6 | 0 | 17 |
| no_ubicado | 0 | 7 | 0 | 0 | 7 |
| punto_mal_atribuido:a_otro_ancestro | 0 | 2 | 0 | 0 | 2 |

G restringida (G-r) en los 208: cambia el punto 19 ({'Obligacion': 8, 'Operacion': 8, 'Potestad': 3}); solo el rol 162; sin cambio 27.

- g_restringida_en_todos_los_nodos_de_contenido: cambian el punto 19 ({'ancestro->unidad': 17, 'ancestro->ancestro': 2}; por tipo {'Obligacion': 8, 'Operacion': 8, 'Potestad': 3}); solo el rol 162; ids que se fusionarían 0; pertenencias a subgrafos de hermanas que se pierden (§5.6) 140.
- g_literal_en_todos_los_nodos_de_contenido: cambian el punto 134 ({'unidad->ancestro': 115, 'ancestro->unidad': 17, 'ancestro->ancestro': 2}; por tipo {'Operacion': 38, 'Condicion': 35, 'Obligacion': 25, 'Potestad': 20, 'Excepcion': 10, 'Restriccion': 5, 'Definicion': 1}); solo el rol 162; ids que se fusionarían 6; pertenencias a subgrafos de hermanas que se pierden (§5.6) 140.
