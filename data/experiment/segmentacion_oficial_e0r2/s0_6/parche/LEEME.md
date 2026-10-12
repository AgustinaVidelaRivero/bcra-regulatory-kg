# Parche de E0 de S0-6a (U-SEG-OFICIAL)

- `parche_e0_S0-6a.diff` (sha256 `a7b7ea50df9efb293ee754f2a9f5ba9ed79e06a62074c05a3348804d17a271ac`): las reglas
  generales A a K de S0-6a, en `data/experiment/reextraccion_v2/e0_chunking/`, sobre el código de S0-5b (el del repo).
  S0-6b lo aplica, una sola vez, desde `e0_chunking/`:

  ```
  patch -p1 --dry-run < parche_e0_S0-6a.diff
  patch -p1 < parche_e0_S0-6a.diff
  ```

  | archivo | sha256 antes (S0-5b) | sha256 después | renglones |
  |---|---|---|---|
  | `e0_lib.py` | `bd2190ad50515ee900448c25dc8e663b3b7d7c52b9e4d8e874f7442b3bec7a51` | `6dd42bf3a82dcd21ab2a417c3a7ef9ddfc60f6ef982684c04ad165476d189cf6` | +984 −38 |
  | `correr_e0.py` | `68bd74b501af7023e97ac837d40390e0732e167dba1f0a5c73f39fc859c2787d` | `cd97223aa7100984eff89081424b2f78de19f2624bef09de5495bbd1b2280fba` | +58 −8 |
  | `selftest_e0.py` | `789630b5c0995075392b6590730d5105c39765c611ad840914f606b67b9ce3c0` | `83ae5576d0f2eaf49e2be7c4fa0f7fb87c14cead35ea0f149e0625eff78433c3` | +548 −15 |

  `e0_tablas.py` no cambia (`ab300a22…`). Prueba en seco sobre una copia de los tres archivos de partida
  (`scripts/armar_parche_S0-6a.sh`): rc 0, y los tres archivos de después, iguales byte a byte a los finales.
- `interruptor_prototipo_S0-6a.diff` (sha256 `f9a8240ff76f8f415dc54a41cbab5f1080f75075dc9c64ea22ce6fa95fa71f59`): los
  dos interruptores del prototipo sobre el código final, `S0_6_REGLAS` (las reglas que corren, para el censo por regla)
  y `S0_6_TANDA0=1` (las reglas también en la tanda 0, solo para medir). **No va al repo ni al parche de S0-6b.** Lo
  regenera `scripts/armar_proto_S0-6a.py`.
