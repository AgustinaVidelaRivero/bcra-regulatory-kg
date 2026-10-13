# Parche de E0 de S0-6a-bis (U-SEG-OFICIAL)

**Este parche declara en el código la lista de R5-a por lista que queda (`LISTAS_R5A_S0_6`): resuelta sobre
`LISTAS_R5A_S0_5`, nombra las listas con error de corte. Ninguna lectura a ciegas lo abre, tampoco la de S1-quater.**

- `parche_e0_S0-6a-bis.diff` (sha256 `a0f291c487bb243ffea1d9bbc56fb26990f7c147b3ef4ef49d4b74ded55a581f`): las reglas
  generales A a M de S0-6a y S0-6a-bis, en `data/experiment/reextraccion_v2/e0_chunking/`, **completo sobre el código de
  S0-5b** (el del repo); reemplaza a `../../parche/parche_e0_S0-6a.diff`. S0-6b lo aplica, una sola vez, desde
  `e0_chunking/`:

  ```
  patch -p1 --dry-run < parche_e0_S0-6a-bis.diff
  patch -p1 < parche_e0_S0-6a-bis.diff
  ```

  | archivo | sha256 antes (S0-5b) | sha256 después | renglones |
  |---|---|---|---|
  | `e0_lib.py` | `bd2190ad50515ee900448c25dc8e663b3b7d7c52b9e4d8e874f7442b3bec7a51` | `d89aab1a578252cd6296f03e8e8859644f008740cd493ef6d82e86c5009db298` | +1132 −40 |
  | `correr_e0.py` | `68bd74b501af7023e97ac837d40390e0732e167dba1f0a5c73f39fc859c2787d` | `78c54c4cd7dc47d592a2f9dcadc1bf97535af2d6ea0f67d67c8021010650cb5e` | +90 −11 |
  | `selftest_e0.py` | `789630b5c0995075392b6590730d5105c39765c611ad840914f606b67b9ce3c0` | `eb4f11e61981476957aceadb67bfbf80934c8f903c11760b41fc2530bbe38282` | +708 −15 |

  `e0_tablas.py` no cambia (`ab300a22…`). Prueba en seco sobre una copia de los tres archivos de partida
  (`../scripts/armar_parche_S0-6a-bis.sh`): rc 0, y los tres archivos de después, iguales byte a byte a los finales
  (`../controles/prueba_parche_S0-6a-bis.txt`). Aplicado con `patch -p1` a una copia nueva del repo (sin enlaces), da
  los mismos tres archivos; sobre esa copia corrieron los controles y los selftests.
- `diff_contra_S0-6a_S0-6a-bis.diff` (sha256 `25da715d60786423a63e1eff6540aaa480cc4e09a06ba17e4171408f8269acd4`): lo
  que cambia del código del parche de S0-6a (`6dd42bf3…`, `cd97223a…`, `83ae5576…`) al de este: `e0_lib.py` +166 −20,
  `correr_e0.py` +35 −6, `selftest_e0.py` +173 −13. Es para leer el cambio; no se aplica. En seco sobre una copia de los
  archivos de S0-6a: rc 0, y los tres archivos de después, iguales byte a byte a los finales.
- `interruptor_prototipo_S0-6a-bis.diff` (sha256 `9ffaa3590ce0ab40a4614611889cd12d992f34ec4881802be25d4fa50c13e75a`):
  los dos interruptores del prototipo sobre el código final, `S0_6_REGLAS` (las reglas que corren, de `a` a `m`, para
  el censo por regla) y `S0_6_TANDA0=1` (las reglas también en la tanda 0, solo para medir). **No va al repo ni al
  parche de S0-6b.** Lo regenera `../../scripts/armar_proto_S0-6a.py`, sin cambios: las letras `l` y `m` entran por
  `REGLAS_S0_6`.
