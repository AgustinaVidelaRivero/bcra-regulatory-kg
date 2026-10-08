# Estado de S0-4a al retomar tras el corte (07/10/2026, 20:38)

Verificado por la salida (ps, git, logs y archivos de cada corrida), no de memoria.

## Procesos
- `ps`: ningún proceso de corridas, lotes ni selftests de esta sesión vivo (solo el proceso de la propia sesión coincide
  con el patrón del scratchpad). Nada corre dos veces al relanzar.

## Repo
- HEAD `1190a8a` (al empezar, `f96ab49`). Entre los dos, 4 commits de otras unidades (dac7d57, df59e79, 4f738ed,
  1190a8a); `git diff --stat f96ab49 HEAD` de e0_chunking/, segmentacion_oficial_e0r2/, el mandato de U-SEG-OFICIAL, la
  tabla de reprocesamiento, escalado_prep/ y segmentacion_84/: vacío.
- Código de E0 del repo: `26c6502` sin cambios (c5e7106a…, 4570a0c8…, af114a4d…). Nada mío en el repo.
- Árbol de trabajo con modificaciones sin commit de otras unidades (11 archivos, entre ellos
  `data/experiment/mantenimiento/tabla_reprocesamiento.md`, +4 −4) y archivos nuevos de otras unidades. No son míos.
- `data/experiment/mantenimiento/selftest_clave_cache.json` del repo sigue en `923dd900…`.

## Scratchpad: hecho y completo
- Copia del repo (`copia/`, HEAD f96ab49, 0 enlaces) con el código de S0-4 instalado en e0_chunking/ (6226a8f8…,
  682d033e…, 215844127…). Raíces mínimas `raices/{base26,s03,s03sinm4,impl4,proto4}`.
- Código de S0-4 en `trabajo/s04/` (y `trabajo/s04_proto/`), parches en `s0_4/parche/` (verificados por los dos caminos)
  con LEEME.
- Corridas completas (log «listo N TOs, 0 con error» y archivos completos): base, s03_sin_m4, t0_base, t0p_base,
  t0_s03_sin_m4, **final** (152, 768 archivos), final_proto_x (63 TOs), r_sd, sin_sdg3, s03_sd, r_ap, s03_ap,
  r_4a_s, r_4b_s, s03_4a_s, s03_4b_s (52 TOs), r_m1a, r_m1b, r_m2a_x, r_m2b, r_m2c_x, r_m3, r_m5a, r_m5b, r_m5c,
  y la tanda 0: t0_final, t0_off, t0_sd, t0_sdg3, t0_4a, t0_4b, t0_ap, t0_m1a, t0_m1b, t0_m2a, t0_m2b, t0_m2c, t0_m3,
  t0_m5a, t0_m5b, t0_m5c.
- Selftest de claves sobre la copia con el código de S0-4: completo (rc=0, VEREDICTO OK, salida igual a 923dd900…).
- Censos en `s0_4/censos/` (sub-documento en los 152, por regla, 4a/4b validado, final contra S1 y S0-3, atribución
  contra S0-3, errores de S1, renombres, filas por regla, precondiciones, unidades de los TOs de sub-documento).
- Borradores: `s0_4/DISENO_S0-4.md` (§0-§1), `s0_4/borrador_secciones.md` (§2-§11 con huecos ‹›), `FRENO_S0-4a.md`
  (con huecos ‹›).

## Quedó a medias: se rehace entera
- `off` (flujo A, 7 TOs, detenida a propósito), `r_m2a` (flujo C, detenida a propósito por memoria): se descartan; las
  reemplazan off (=off_x + off_m) y r_m2a (=r_m2a_x + r_m2a_m).
- `off_x` (106 TOs), `s03cfg_x` (106), `final2_x` (110): cortadas → se rehacen enteras.
- `t0_final2` (3 TOs): cortada → se rehace entera.
- Selftests de E0 (`selftest_e0` quedó en el bloque k; b52, b581, b582 y b583 no corrieron): se rehacen enteros.
- Pendientes que no empezaron: las corridas de manual (final2_m, off_m, s03cfg_m, r_m2a_m, r_m2c_m, final_proto_m) y las
  uniones (off, s03cfg, final2, r_m2a, r_m2c, final_proto).

## Plan al retomar
1. Borrar las corridas a medias (off, r_m2a, off_x, s03cfg_x, final2_x, t0_final2).
2. Relanzar: off_x, s03cfg_x, final2_x sin manual en paralelo; después manual de a una (final2_m, off_m, s03cfg_m,
   r_m2a_m, r_m2c_m, final_proto_m); uniones; t0_final2. Después, los selftests de E0 enteros.
3. Comparaciones (todo apagado = S1; solo S0-3 = S0-3 sin m4; doble corrida; prototipo = código), atribución contra S1,
   tanda 0 por regla, cerrar diseño y freno, foto del repo, .pyc, paquete y grep.
20:38:47 corridas a medias movidas a corridas/descartadas_corte/ (off, r_m2a, off_x, s03cfg_x, final2_x, t0_final2); se rehacen enteras
20:39:13 lanzado herr/lote_s04f.sh (registro en trabajo/logs/lote_s04f.log)
20:54:23 selftest_e0 primera corrida 132/134: fallan dos casos medidos de etapas anteriores por efecto de S0-4 (ri_spi 95 → 93 por 4b; nmcief::3.2.1 → nmcief::A2::3.2.1 por sd); casos corregidos en trabajo/s04/selftest_e0.py (f518f537…), copiado a copia/raices/s04_proto; segunda corrida de selftest_e0 lanzada (trabajo/logs/selftest_e0_S0-4_segunda.txt)
21:05:31 lote_s04f completo: off, s03cfg, final2 (unidas, 768) y los controles pasan; r_m2a y r_m2c unidas iguales a S0-3; atribución contra S1 hecha (1 interacción leída: nmcief::A4::S1). Siguen: cerrar diseño y freno, fotos, .pyc, paquete, grep.
21:17:27 cierre: diseño y FRENO completos; foto después (21:09, 0ea2d74) con las 126 diferencias atribuidas a otras unidades; .pyc fuera de .venv 2.213 = 2.213; grep de convenciones (0 nombres, 0 rutas); paquete revision_USEG_OFICIAL_FRENO_S0-4a armado con manifest. FRENO S0-4a.
