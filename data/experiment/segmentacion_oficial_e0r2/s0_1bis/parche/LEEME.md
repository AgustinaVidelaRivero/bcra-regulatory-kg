# Prototipo de S0-1 bis (U-SEG-OFICIAL), sin aplicar

- Base: `data/experiment/reextraccion_v2/e0_chunking/e0_lib.py` y `correr_e0.py` de `9f6361e` (sha256
  `9e049e5888c2352a…` y `095720c21c1d763b…`). Diseño en `../DISENO_S0-1bis.md`.
- `parche_completo_USEG_S0-1bis_prototipo_sin_aplicar.diff` lleva las siete reglas de S0-1, el acompañamiento T y lo
  de S0-1 bis (regla 6 en E1 con el tercer escalón, reglas 8 y 9). `parche_incremental_USEG_S0-1bis_sobre_S0-1_sin_aplicar.diff`
  lleva solo lo de S0-1 bis, sobre el prototipo de S0-1 (`../../s0_1/parche/`).
- Se aplica sobre una copia, nunca sobre el repo. Desde un directorio vacío fuera del repo:

```
git -C "<repo>" show 9f6361e:data/experiment/reextraccion_v2/e0_chunking/e0_lib.py > e0_lib.py
git -C "<repo>" show 9f6361e:data/experiment/reextraccion_v2/e0_chunking/correr_e0.py > correr_e0.py
patch -p1 < "<repo>/data/experiment/segmentacion_oficial_e0r2/s0_1bis/parche/parche_completo_USEG_S0-1bis_prototipo_sin_aplicar.diff"
shasum -a 256 e0_lib.py correr_e0.py
```

- Tienen que salir: `e0_lib.py` `81c3409851ba82a3eada400048ed4fe7198cc3004dd6de6233eeaa147210dcd6` y
  `correr_e0.py` `f737028b1918cce099698272821a8f5db43a8a29792e572451ba95032c0b19ab`.
- Por el otro camino (el parche completo de S0-1 y, después, el incremental) salen los mismos sha256.
- `S0_REGLAS`, `S0_PARTIR_TABLAS` y `S0_RAZON_E1` son interruptores de medición del prototipo; en S0-2 las reglas
  quedan como constantes de e0-r2 y la razón del tercer escalón sale de T2 (`../DISENO_S0-1bis.md`, §6).
