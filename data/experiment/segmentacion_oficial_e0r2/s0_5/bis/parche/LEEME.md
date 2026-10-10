# Parche de E0 de S0-5a-bis (U-SEG-OFICIAL)

- `parche_e0_S0-5a-bis.diff` (sha256 `421ee9132035a0d481c4c15b92997fcaa1dc0074b58537db8944cb88878ffbf4`): las reglas de
  S0-5a con las correcciones de S0-5a-bis (R5-a por lista y sin tablas, R5-f y R5-g), en
  `data/experiment/reextraccion_v2/e0_chunking/`, sobre el código de S0-4b (el del repo). **Reemplaza al parche de
  S0-5a** (`s0_5/parche/parche_e0_S0-5a.diff`, `c6558ea0…`): S0-5b aplica este, una sola vez, desde `e0_chunking/`:

  ```
  patch -p1 --dry-run < parche_e0_S0-5a-bis.diff
  patch -p1 < parche_e0_S0-5a-bis.diff
  ```

  | archivo | sha256 antes (S0-4b) | sha256 después | renglones |
  |---|---|---|---|
  | `e0_lib.py` | `65a8c3b8bb09da4d527fd94e31cfbc52168171bcd1603394aaa8b28c05361de6` | `bd2190ad50515ee900448c25dc8e663b3b7d7c52b9e4d8e874f7442b3bec7a51` | +536 −12 |
  | `correr_e0.py` | `94d353495a585e0ad4799813a22fb1f1670f33b558f67741b9fceb71d2fcc1bc` | `68bd74b501af7023e97ac837d40390e0732e167dba1f0a5c73f39fc859c2787d` | +107 −1 |
  | `selftest_e0.py` | `ec186071368ca5c415f926bc67960ccab0ede1e9ff35098df5887c2681b38079` | `789630b5c0995075392b6590730d5105c39765c611ad840914f606b67b9ce3c0` | +524 −10 |

  Prueba en seco sobre una copia de los tres archivos de partida: rc 0, y los tres archivos de después, iguales byte a
  byte a los finales.
- `interruptor_prototipo_S0-5a-bis.diff` (sha256 `5d048e6be8652255fef6d29120224c4a183f1a25a8935420e29b18ecb6667e4f`):
  los dos interruptores del prototipo sobre el código final, `S0_5_REGLAS` (las reglas que corren, para el censo por
  regla) y `S0_5_TANDA0=1` (las reglas también en la tanda 0, solo para medir). **No va al repo.** Lo regenera
  `scripts/armar_proto_S0-5a-bis.py`.
