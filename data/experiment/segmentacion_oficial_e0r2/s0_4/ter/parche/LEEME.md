# Parche final de S0-4 de U-SEG-OFICIAL, con S0-4a-bis y S0-4a-ter (sin aplicar)

Tres diffs, sin aplicar en el repo:

- `parche_S0-4a-ter_sobre_26c6502_sin_aplicar.diff`: el código de E0 de S0-4 completo (las reglas de S0-3 sin el
  mecanismo 4, más sd, sdg3, sdmax, sdr1, apl, sdl, sdlh, sdla, 4a, 4b y ap), en `e0_lib.py` (+696 −48), `correr_e0.py`
  (+79 −10) y `selftest_e0.py` (+598 −9), sobre el código de E0 de `26c6502`, que es el de HEAD
  (`git diff --stat 26c6502 HEAD -- data/experiment/reextraccion_v2/e0_chunking` sale vacío en `ae76f08`). Es el que
  aplicaría S0-4b. Reemplaza al de S0-4a-bis (`../../bis/parche/parche_S0-4a-bis_sobre_26c6502_sin_aplicar.diff`).
- `parche_S0-4a-ter_sobre_S0-4a-bis_sin_aplicar.diff`: lo mismo, incremental sobre el parche de S0-4a-bis: `e0_lib.py`
  (+85 −10), `correr_e0.py` (+24 −6) y `selftest_e0.py` (+137 −16). Agrega las cinco reglas de S0-4a-ter y sus casos de
  selftest.
- `parche_interruptores_prototipo_S0-4a-ter_sin_aplicar.diff`: sobre el primero, la variable de entorno con que medí
  cada regla prendida y apagada (`S0_4_REGLAS`, como en S0-4a; +8). Solo para reproducir; no va al repo.

Aplicación, sobre una copia (nunca sobre el repo), desde `data/experiment/reextraccion_v2/e0_chunking/` de la copia:

```
patch -p1 < <ruta>/parche_S0-4a-ter_sobre_26c6502_sin_aplicar.diff
```

o, sobre una copia que ya tiene el parche de S0-4a-bis:

```
patch -p1 < <ruta>/parche_S0-4a-ter_sobre_S0-4a-bis_sin_aplicar.diff
```

y, para el prototipo, a continuación:

```
patch -p1 < <ruta>/parche_interruptores_prototipo_S0-4a-ter_sin_aplicar.diff
```

sha256 que tienen que dar (verificado aplicando los diffs sobre los archivos de `git show 26c6502:…`, por los dos
caminos):
- `e0_lib.py` `65a8c3b8bb09da4d527fd94e31cfbc52168171bcd1603394aaa8b28c05361de6`,
  `correr_e0.py` `94d353495a585e0ad4799813a22fb1f1670f33b558f67741b9fceb71d2fcc1bc`,
  `selftest_e0.py` `ec186071368ca5c415f926bc67960ccab0ede1e9ff35098df5887c2681b38079`;
- con el de interruptores: `correr_e0.py` `0e9bfb8f976154ad6ed10cfbfad37eecc3e0b4a7b1a3f10e840c25a31f43fb43`
  (`e0_lib.py` y `selftest_e0.py`, iguales).
