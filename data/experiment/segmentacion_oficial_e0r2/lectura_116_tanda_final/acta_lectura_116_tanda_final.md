# Lectura corta de 1.16 en la tanda final, cortes 1 a 10: acta (mesa, §145, 17/10/2026)

## Qué se leyó y con qué regla

- **1.16:** el último ítem de una lista que se lleva el cierre del padre.
- **La lectura corta escalonada,** sobre los 28 documentos con algún candidato sin leer:
  - 30 cortes, en el orden sellado el 16/10/2026 a las 08:19:19, antes de las fichas (`sello/orden_y_cortes_116_tanda_final.json`,
    `3db5328f…`, semilla `U-SEG-OFICIAL:1_16:tanda_final`);
  - se leen primero los cortes 1 a 10 (registro de decisiones, §15, `:488-500`; pre-registro de la tanda 1, `:700-704`).
- **Las reglas que la autora fijó antes de leer** (17/10/2026, 18:05; registro de decisiones, §27):
  - una dudosa de corte entre los 10 primeros hace seguir hasta el 30;
  - cualquier error de corte confirmado hace seguir;
  - la columna `limpieza` sigue la convención de S1-quater.
- **El material** (`material/`, manifiesto `da130ee1…`, armado el 16/10/2026 a las 08:21:24): las fichas de los 30 cortes, la planilla
  vacía y el LEEME.
  - Las 45 páginas, a 110 ppp, no entran al repo: quedan en el paquete de la mesa, con su sha256 en el manifiesto.
  - Los scripts del orden y de las fichas están en `scripts/`. Los insumos del orden quedan en el paquete de la mesa, con su sha256 en el
    sello.

## La lectura y sus sellos

- La leyó la autora el 17/10/2026. Le llevó unos 11 minutos, según su cuenta.
- **Vale el sello v3,** del 17/10/2026 a las 18:33:58 (`lectura/sello_planilla_116_tanda_final_v3.txt`):
  - `planilla_116_tanda_final.tsv`, `fe4a5c322eeec67a8c075f2152b823a90e0696179d10b89358a70037db462ac0`;
  - la exportación con punto y coma, `f7c3af4195f2ad106add50414c9072d9091507fa1815d43d460af8f0da20670d`.
- **Los sellos v1 (18:19:19) y v2 (18:20:56) sellaron por error la planilla vacía** (`8c0dbf40…`, igual a la plantilla de la mesa,
  controlado), porque se salteó la conversión. Lo declara la autora:
  - la primera exportación (`286e99e7…`) tenía sus marcas corridas una columna, con el id en la columna `marca`;
  - la corrigió ella en Numbers, y la exportación corregida quedó guardada encima de esa;
  - por eso la primera exportación no se conserva, y su contenido no se puede controlar.
  - Los dos sellos van en `lectura/` tal como están.

## El control de la mesa

Lo hace `../control_lecturas_1710/controlar_lecturas_1710_mesa.py`. Da 0 fallas:
- el sha256 de los dos archivos es el del sello v3;
- el `.tsv` de los sellos v1 y v2 es la plantilla vacía;
- la cabecera y las 30 filas son las de la plantilla, y las 4 columnas fijas son iguales fila por fila;
- la exportación tiene el mismo contenido que el `.tsv`;
- solo el tramo 1 tiene marcas;
- los códigos son los válidos de S1-quater.

## Lo que dio

- **10 de 10 correctas, sin errores ni dudosas de corte.** Los documentos son snp_tr_nc, fimipyme, ordcom, tasint, fabcra, inspag,
  snp_spd, adfsp, raapal y repefe.
- **Rige la rama 0:** la lectura para, y los otros 18 documentos se declaran con «0 de 10». Ningún documento sale de la tanda final por
  1.16.
