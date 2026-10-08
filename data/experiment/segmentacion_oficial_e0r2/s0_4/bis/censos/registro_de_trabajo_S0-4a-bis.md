# Estado de S0-4a-bis (U-SEG-OFICIAL), registro de trabajo

Inicio: 2026-10-08 07:44:12. HEAD 7788e52, árbol de trabajo sin cambios rastreados
(solo sin seguimiento: s1/e0/ y reports/ de otras unidades). ps: ningún proceso de corridas vivo.
selftest_clave_cache.json del repo: 923dd900… (el vigente tras revertir O5).
Foto del repo antes: bis/fotos/foto_antes.json; .pyc fuera de .venv: bis/fotos/pyc_antes_sin_venv.txt.
07:44:45 copia puesta al día con HEAD 7788e52 (91 archivos: 82 que faltaban y 9 distintos, salvo los tres de e0_chunking, que llevan el código de S0-4a); 0 enlaces
07:51:25 código de S0-4a-bis en trabajo/s04bis (e0_lib 7e56f857…, correr_e0 2559b6c2…, selftest_e0 a776126d…), prototipo trabajo/s04bis_proto, medición de ri_oc trabajo/s04bis_oc; raíces impl4bis, proto4bis, oc4bis; código instalado en la copia. Prueba previa: sd5_bis (5 TOs) y bloques q y r del selftest 17/17. Lanzado bis/scripts/lote_bis.sh (registro bis/logs/lote_bis.log).
07:55:51 herencia de los 53 puntos 4a de la tanda 0: 53 sí, 0 no (bis/censos/herencia_4a_tanda0_S0-4a-bis.json), control negativo 52/1; anclas de F19b recalculadas (bis/scripts/anclas_f19b.py); parches en bis/parche/ verificados por los dos caminos; discrepancias ri_tsa y ri_mmsef verificadas (errores propios de S0-4a).
08:25:17 lote_bis completo (lote fin 08:24:01). Controles: tanda 0 57/57 en las 6 corridas; prendida contra S0-4a: 4 distintos (ri_ccna y 2 agregados... ver archivo); apagada = S0-4a 768/768; todo apagado = S1 768/768 (y contra el manifiesto de S1); doble 0 distintos; prototipo 320/320; tanda 0 dentro de los 152 25/25; selftests 137/137, 39/39, 34/34, 59/59, 33/33; claves VEREDICTO OK, salida = 923dd900 byte a byte. ri_oc medido (128 → 133). Error propio: la línea de s1/e0/ de controles_bis.sh comparaba contra una carpeta que la copia no tiene; corregida.
08:28:23 conciliación hecha (contra S0-4a 11 eventos sdmax, interacción 0; contra S1 1.540 = 1.530 + 10, interacción 1); filas F19b y F01; foto después (48 nuevos de otras unidades, 0 cambiados); .pyc 2.213 = 2.213. Siguen: diseño final, FRENO, paquete, grep, memoria.
08:30:23 diseño y FRENO escritos; armo el paquete revision_USEG_OFICIAL_FRENO_S0-4a-bis y corro el grep de convenciones.
08:31:12 grep: primera pasada con la ruta del scratchpad en selftests_e0_S0-4a-bis.txt (impresa por el selftest), reemplazada por <scratchpad>; segunda pasada 0 nombres, 0 rutas, 8 coincidencias del corpus. Paquete cerrado. FRENO S0-4a-bis.
