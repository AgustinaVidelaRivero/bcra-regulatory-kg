# Cifras de la sección 15 del FRENO T1 (las genera cifras_reparto_t1.py)

### A. El cambio y su control

| control | resultado |
|---|---|
| sha256 de tanda_final_98tos_r2b.json | e9993b9dc87e866850a0357572f03c54a3b08dd56f5cb272e42da5d33c81dfeb |
| sha256 de lanzar_t2.py | 462dfeabc160eb0d8a15e3062a498c0f3d6d10ff2ccdccff9795f75079b05ba3 |
| sha256 de sha256_para_T2.txt | 12f7e21716108deae98fdba4408baaa7ec405632c13c33c353a35df8fd1a35e2 |
| el manifiesto es la alternativa, byte a byte | True |
| git diff --numstat (agregados, quitados, archivo) | 197 197 data/experiment/reextraccion_v2/manifiestos/tanda_final_98tos_r2b.json; 1 1 data/experiment/tanda_final/t1/sha256_para_T2.txt; 1 1 data/experiment/tanda_final/t2/lanzar_t2.py |
| sha256_para_T2.txt: renglones y OK | 499 y 499 |

### B. El control de entradas con el manifiesto nuevo

| control | resultado |
|---|---|
| a_prefijo | OK |
| b_tool_schema | OK |
| c_namespace_e1 | OK |
| d_prefijo_y_namespace_e3 | OK |
| e_salida_tanda_final_r2b | OK |
| f_candado_catalogo | OK |
| g_temperatura | OK |
| h_candados_y_selftest_claves | OK |
| i_mensajes_e1_contra_la_base_de_a3 | OK |
| j_herencia_recortada_tanda_final | OK |
| k_rol_de_alcance | OK |
| l_sellos_manifiesto_tanda_final | OK |
| m_carga_y_control_en_contra | OK |
| veredicto | OK |
| l: estimado, tope y diferencia con U × tarifa + 0,209440 | 104.749803, 151.5835, -0.000002 |
| m: carga | {'ok': True, 'orden_igual': True, 'perfil': 'r2b', 'tos': 98} |
| m: el contra frena en | ri_bdp (de los 33: True) |
| m: el contra difiere solo en rol_alcance | True |
| m: sha256 del manifiesto y del contra | e9993b9dc87e866850a0357572f03c54a3b08dd56f5cb272e42da5d33c81dfeb, 08ac4ea0169094cb921094a30edc293d758efb218ab4defcb453555e9d2a64a9 |
| el volcado de los mensajes de la copia, igual al de T1 | True |

### C. Las tres pruebas del lanzador con el manifiesto nuevo

| prueba | salida | TOs lanzados | controles previos | freno por modelo | control entre tramos | opciones | parada |
|---|---|---|---|---|---|---|---|
| lanzador_reparto_prueba_1_punta_a_punta.log | rc=0 | ri_bdp, ri_ieccm, reqcac | True (sha256 del manifiesto: True; HEAD:  78 de 78, árbol: 78 de 78) | OK, OK, OK, OK | OK | autorizado_tramo_2=False, retomar_tras_pausa=False, hora_simulada=None | — |
| lanzador_reparto_prueba_2_autorizado_tramo_2.log | rc=0 | ri_bdp, ri_ieccm, reqcac | True (sha256 del manifiesto: True; HEAD:  78 de 78, árbol: 78 de 78) | OK, OK, OK, OK | FRENO | autorizado_tramo_2=True, retomar_tras_pausa=False, hora_simulada=None | — |
| lanzador_reparto_prueba_3_retomar_tras_pausa.log | rc=0 | ri_bdp, ri_ieccm, reqcac | True (sha256 del manifiesto: True; HEAD:  78 de 78, árbol: 78 de 78) | OK, OK, OK, OK | OK | autorizado_tramo_2=False, retomar_tras_pausa=True, hora_simulada=2026-10-23T18:00:00-03:00 | — |

### D. Las bases de la caché del repo y el ancla de la hora de fin de T1

| control | resultado |
|---|---|
| shasum -a 256 -c, después de las pruebas | data/experiment/reextraccion_v2/e1_extractor/cache/e1_extraccion.db: OK; data/experiment/reextraccion_v2/e3_verificador/cache/e1_reintentos.db: OK; data/experiment/reextraccion_v2/e3_verificador/cache/e3_verificacion.db: OK |
| hoy, contra el sha256 de antes | {'e1_extraccion.db': True, 'e1_reintentos.db': True, 'e3_verificacion.db': True} |
| ancla (stat) | 2026-10-18 22:46:26 data/experiment/tanda_final/t1/FRENO_T1.md |
| ancla (stat) | 2026-10-18 23:46:08 <scratchpad>/checkpoint_tanda_final.md |
| ancla (stat) | 2026-10-18 22:47:04 <scratchpad>/revision_tanda_final_FRENO_T1/manifest.txt |
| ancla (stat) | 2026-10-18 22:47:04 <scratchpad>/verificacion_copia_paquete.txt |
| ancla (stat) | 2026-10-18 22:47:04 $HOME/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/afadde2e-6298-47fb-9777-7fcb43152d50/scratchpad/revision_tanda_final_FRENO_T1/manifest.txt |
