# Parche de E0 de S0-5a (U-SEG-OFICIAL)

- `parche_e0_S0-5a.diff` (sha256 `c6558ea0e51008fb0b2f6f1cea0f58837099050f8418ad1197034150b5c28f98`): las seis reglas
  de S0-5a en `data/experiment/reextraccion_v2/e0_chunking/`, sobre el código de S0-4b (el del repo). Se aplica en
  S0-5b, una sola vez, desde `e0_chunking/`:

  ```
  patch -p1 --dry-run < parche_e0_S0-5a.diff
  patch -p1 < parche_e0_S0-5a.diff
  ```

  | archivo | sha256 antes | sha256 después | renglones |
  |---|---|---|---|
  | `e0_lib.py` | `65a8c3b8bb09da4d527fd94e31cfbc52168171bcd1603394aaa8b28c05361de6` | `4d0abc1a728a7fe9064a2f64de56ee9e8abc73b2a39a9ff90e001786ccc5ec26` | +410 −10 |
  | `correr_e0.py` | `94d353495a585e0ad4799813a22fb1f1670f33b558f67741b9fceb71d2fcc1bc` | `ed276d43a887ee89deb5347a5ee36f94cd2fe3f0910d3e016d72a5585662779f` | +30 −1 |
  | `selftest_e0.py` | `ec186071368ca5c415f926bc67960ccab0ede1e9ff35098df5887c2681b38079` | `9f2fbf2897f8dcb0b445e7ed4607deb7f2842e242be8a8c145a2009d66df7eda` | +284 −10 |

  Prueba en seco sobre una copia de los tres archivos de partida: rc 0, y los tres sha256 de después, iguales.
- `interruptor_prototipo_S0-5a.diff` (sha256 `049e597de1762b013699cdcb04e031302b87cbb30a3dcc58d2951e57c86be350`): el
  interruptor `S0_5_REGLAS` del prototipo del censo por regla, sobre el código final. **No va al repo.**
- `interruptor_tanda0_medicion_S0-5a.diff` (sha256 `7d25e7fcdc472a9f4a76a3df9a5d79f2ceda2c8dd779cb1bd9518ed62e27ec09`): el mismo interruptor más `S0_5_TANDA0=1`, que deja
  correr las reglas en la tanda 0, solo para medir lo que cambiarían ahí (`t0_sin_exclusion`). **No va al repo.**
