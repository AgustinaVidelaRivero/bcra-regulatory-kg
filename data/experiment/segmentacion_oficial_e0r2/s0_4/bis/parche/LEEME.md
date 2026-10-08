# Parche final de S0-4 de U-SEG-OFICIAL, con S0-4a-bis (sin aplicar)

Cuatro diffs, sin aplicar en el repo:

- `parche_S0-4a-bis_sobre_26c6502_sin_aplicar.diff`: el código de E0 de S0-4 completo, con la regla sdmax de S0-4a-bis
  (las reglas de S0-3 sin el mecanismo 4, más sd, sdg3, sdmax, 4a, 4b y ap), en `e0_lib.py` (+621 −48),
  `correr_e0.py` (+61 −10) y `selftest_e0.py` (+477 −9), sobre el código de E0 de `26c6502`, que es el de HEAD
  (`git diff --stat 26c6502 HEAD -- data/experiment/reextraccion_v2/e0_chunking` sale vacío en `7788e52`). Es el que
  aplicaría S0-4b. Reemplaza al parche de S0-4a (`../../parche/parche_S0-4_sobre_26c6502_sin_aplicar.diff`).
- `parche_S0-4a-bis_sobre_S0-4a_sin_aplicar.diff`: lo mismo, incremental sobre el parche de S0-4a: `e0_lib.py` (+19 −6),
  `correr_e0.py` (+12 −9) y `selftest_e0.py` (+39 −6). Agrega la regla sdmax y sus casos q, r y s del selftest.
- `parche_interruptores_prototipo_S0-4a-bis_sin_aplicar.diff`: sobre el primero, la variable de entorno con que medí
  la regla prendida y apagada (`S0_4_REGLAS`, como en S0-4a; +8). Solo para reproducir; no va al repo.
- `parche_medicion_ri_oc_S0-4a-bis_sin_aplicar.diff`: sobre el de interruptores, la variante de medición de ri_oc
  (`S0_4_SD_MEDICION`: TOs que se suman a la lista de sub-documento, con la guarda del régimen de la página 1; +25).
  Solo para reproducir la medición del diseño, §4; no va al repo ni al parche final.

Aplicación, sobre una copia (nunca sobre el repo), desde `data/experiment/reextraccion_v2/e0_chunking/` de la copia:

```
patch -p1 < <ruta>/parche_S0-4a-bis_sobre_26c6502_sin_aplicar.diff
```

o, sobre una copia que ya tiene el parche de S0-4a:

```
patch -p1 < <ruta>/parche_S0-4a-bis_sobre_S0-4a_sin_aplicar.diff
```

y, para el prototipo y la medición, a continuación y en este orden:

```
patch -p1 < <ruta>/parche_interruptores_prototipo_S0-4a-bis_sin_aplicar.diff
patch -p1 < <ruta>/parche_medicion_ri_oc_S0-4a-bis_sin_aplicar.diff
```

sha256 que tienen que dar (verificado aplicando los diffs sobre los archivos de `git show 26c6502:…`, por los dos
caminos):
- `e0_lib.py` `7e56f857b962ce0fdc76ddc9450e212d7af1e955c00067ecebb47e828bdd4131`,
  `correr_e0.py` `2559b6c2d299b8f45ebd1a0d99c3227a97bde2597ed437eee761cd624910279b`,
  `selftest_e0.py` `a776126d29c86d9ad8f750de465abfbb84fa7c1ea460f6287458f46200e1585e`;
- con el de interruptores: `correr_e0.py` `c06625a9083d83f03628515aa65db1d1102494554dce870d7a2069ab163d0163`;
- con el de medición: `correr_e0.py` `08febab5cdef3e4aaba68acd5d3dbe75deff8c0495ec023d8ac6134bbd9ade60`
  (`e0_lib.py` y `selftest_e0.py`, iguales en los tres).
