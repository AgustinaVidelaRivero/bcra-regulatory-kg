# Prototipo de S0-1 (U-SEG-OFICIAL), sin aplicar

- Base: `data/experiment/reextraccion_v2/e0_chunking/e0_lib.py` y `correr_e0.py` de `9f6361e` (sha256
  `9e049e5888c2352a…` y `095720c21c1d763b…`; iguales en HEAD al 05/10/2026). Copia byte a byte del paquete de
  revisión del FRENO S0-1; diseño en `../DISENO_S0-1.md`.
- Se aplica sobre una copia, nunca sobre el repo. Desde un directorio vacío fuera del repo:

```
git -C "<repo>" show 9f6361e:data/experiment/reextraccion_v2/e0_chunking/e0_lib.py > e0_lib.py
git -C "<repo>" show 9f6361e:data/experiment/reextraccion_v2/e0_chunking/correr_e0.py > correr_e0.py
patch -p1 < "<repo>/data/experiment/segmentacion_oficial_e0r2/s0_1/parche/parche_completo_USEG_S0-1_prototipo_sin_aplicar.diff"
shasum -a 256 e0_lib.py correr_e0.py
```

- Tienen que salir: `e0_lib.py` `2405862332cfed732948914cc988fb65468ac07ae91ba71cf99663a54c84f0bb` y
  `correr_e0.py` `d0b4bcd453e89b3050f08f61de4f25b04092d2600d86c85a433f9e8b46f2cd96`.
- Los parches por regla, aplicados en orden (`00_comun` primero, después de `01` a `08`), dan los mismos sha256.
  Sus trozos numeran líneas desde el propio trozo: `patch` los ubica por contexto y deja archivos `.orig`. El
  índice de trozos dice qué reglas lleva cada trozo; la regla 4 está en el parche común.
- `S0_REGLAS` y `S0_PARTIR_TABLAS` son interruptores de medición del prototipo; en S0-2 las reglas quedan como
  constantes de e0-r2 (`../DISENO_S0-1.md`, §5).
