# Lectura de los 14 límites de sub-documento de la tanda 1: acta (mesa, §145, 17/10/2026)

## Qué se leyó y con qué regla

- **Los 14 límites de la tanda 1 que la regla de sub-documento no aplica:** manori 8, ri_rml 3, ri_gerc 1, ri_pgn 1 y snp_tr 1. Caen en 8
  unidades de la E0 corregida (`80adbd58…`).
- **La regla:** la de lectura de S1-bis. Cuenta solo el error de corte (registro de decisiones, §14, `:470-476`; pre-registro de la tanda
  1, firmado en `95b18217`, `:705-713`).
- **El material** (`material/`, manifiesto `f362fad4…`, armado el 16/10/2026 a las 01:01:51):
  - las fichas;
  - la planilla vacía;
  - el LEEME.
  - Las 17 páginas, a 110 ppp, no entran al repo: quedan en el paquete de la mesa
    (`decisiones_118_mesa/lectura_subdocumento_tanda1/material/paginas/`), con su sha256 en el manifiesto.
  - El script de las fichas está en `scripts/`.

## La lectura

- La leyó la autora el 17/10/2026. Le llevó unos 30 minutos, según su cuenta.
- **Su planilla está en `lectura/`,** sellada el 17/10/2026 a las 18:02:05 (`sello_planilla_subdocumento_tanda1.txt`):
  - `planilla_subdocumento_tanda1.tsv`, `399f2fbd4dbf1e06f9a6e1c2e5c2c290904ea04f3a7346a0d41e233179e33412`;
  - la exportación de Numbers, con punto y coma, `6bcdb2f2f8728df4b30e067ccfc9844f7719600d3ae2430bfcf30c4ea89461b4`.
- El `.tsv` sale de la exportación con un script de conversión de la autora. Toma las columnas fijas de la plantilla y las de marca de la
  exportación, y controla los códigos.

## El control de la mesa

Lo hace `../control_lecturas_1710/controlar_lecturas_1710_mesa.py`, sobre copias. Sus salidas están en la misma carpeta. Da 0 fallas:
- el sha256 de los dos archivos es el del sello;
- la cabecera es la de la plantilla, con 14 filas, y las 7 columnas fijas son iguales fila por fila;
- la exportación tiene el mismo contenido que el `.tsv`, celda por celda;
- cada `unidad_leida` está entre las unidades de la página del límite;
- los códigos de marca son los válidos de S1-quater.

## Lo que dio

- **14 de 14 correctas, sin errores ni dudosas.** Las unidades leídas son manori::1.5.1, ri_gerc::2.3, ri_pgn::S1, ri_rml::3.1,
  ri_rml::S6 y snp_tr::1.7.3.
- **El rasgo no se confirma.** Los 33 límites de sub-documento de la tanda final (18 documentos) no se leen, y quedan como los segmenta la
  E0. El texto fija solo la rama con un error de corte confirmado (pre-registro, `:705-713`). La rama sin error la leo así: es lectura de
  la mesa, declarada.
- **El orden sellado de esos 33** queda sin usar, en `orden_tanda_final/`:
  - `orden_subdocumento_tanda_final.json`, `a5aa3008…`, sellado el 16/10/2026 a las 08:20:10, con su script y su sello;
  - los insumos del orden quedan en el paquete de la mesa (`decisiones_119_mesa/insumos/`).
- **Ningún documento de la tanda 1 sale del grafo evaluado** por esta lectura (pre-registro, `:709-713`).
