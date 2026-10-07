# Parche de S0-3 de U-SEG-OFICIAL (prototipo sin aplicar)

Dos diffs, sin aplicar en el repo:

- `parche_S0-3_sobre_26c6502_sin_aplicar.diff`: los cinco mecanismos de S0-3 en `e0_lib.py` y `correr_e0.py`, y los
  bloques n, o y p de `selftest_e0.py` (más el caso del acompañamiento T, que pasa de ri_dcpc a snp_dd), sobre el
  código de E0 de `26c6502` (que es el de HEAD: `git diff --stat 26c6502 HEAD -- data/experiment/reextraccion_v2/e0_chunking`
  sale vacío). Las reglas son constantes de e0-r2 (`correr_e0.REGLAS_S0_3`); el mecanismo 4 no corre en los diez TOs
  de la tanda 0 (`correr_e0.TOS_TANDA0_SIN_M4`; decisión de la autora PENDIENTE).
- `parche_interruptores_prototipo_S0-3_sin_aplicar.diff`: sobre el anterior, las dos variables de entorno con que medí
  cada regla sola (`S0_3_REGLAS`, `S0_3_M4_EN_TANDA0`). Solo para reproducir el censo por regla; no va al repo.

Aplicación, sobre una copia (nunca sobre el repo), desde `data/experiment/reextraccion_v2/e0_chunking/` de la copia:

```
patch -p1 < <ruta>/parche_S0-3_sobre_26c6502_sin_aplicar.diff
```

y, para el prototipo con interruptores, a continuación:

```
patch -p1 < <ruta>/parche_interruptores_prototipo_S0-3_sin_aplicar.diff
```

sha256 que tienen que dar (verificado aplicando los dos diffs sobre los archivos de `git show 26c6502:…`):
- con el primero: `e0_lib.py` `3ce0a2d8f9abbc75a6f5da3cd63bf15232673628adad6e6c4e63fd452b91a0cc`,
  `correr_e0.py` `0002ed4e5919a738295a8d6b26789cdf3d39043f9d4564b90a79cffb06f6b6da`,
  `selftest_e0.py` `cd4b98dba40e3c1877ba80eb60dc64a7bd7102e16eafdd9862cd72a5985828e3`;
- con los dos: `correr_e0.py` `33e03aafc9ace4691c88d698323c8a141752427a717158a1030e6fa19e11f3f5` (`e0_lib.py` y
  `selftest_e0.py`, iguales).
