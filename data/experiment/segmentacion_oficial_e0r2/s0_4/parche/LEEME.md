# Parche de S0-4 de U-SEG-OFICIAL (sin aplicar)

Tres diffs, sin aplicar en el repo:

- `parche_S0-4_sobre_26c6502_sin_aplicar.diff`: el código de E0 de S0-4 completo (las reglas de S0-3 sin el mecanismo
  4, más sub-documento, sdg3, 4a, 4b y apartados) en `e0_lib.py` (+607 −47), `correr_e0.py` (+58 −10) y
  `selftest_e0.py` (+444 −9), sobre el código de E0 de `26c6502` (que es el de HEAD: `git diff --stat 26c6502 HEAD --
  data/experiment/reextraccion_v2/e0_chunking` sale vacío). Es el que S0-4b aplicaría al repo.
- `parche_S0-4_sobre_S0-3_sin_aplicar.diff`: lo mismo, incremental sobre el parche de S0-3
  (`../../s0_3/parche/parche_S0-3_sobre_26c6502_sin_aplicar.diff`): `e0_lib.py` (+399 −42), `correr_e0.py` (+42 −17),
  `selftest_e0.py` (+247 −26). Quita el mecanismo 4 y agrega las reglas de S0-4; en `selftest_e0.py`, además de los
  casos q, r y s, actualiza dos casos medidos de etapas anteriores que S0-4 cambia (ri_spi 93 unidades;
  `nmcief::A2::3.2.1`).
- `parche_interruptores_prototipo_S0-4_sin_aplicar.diff`: sobre el primero, la variable de entorno con que medí cada
  regla sola y la configuración con todo apagado (`S0_4_REGLAS`: lista de reglas separadas por coma, de REGLAS_S0_3 y
  REGLAS_S0_4; sin la variable o con TODAS, todas). Solo para reproducir los censos; no va al repo.

Aplicación, sobre una copia (nunca sobre el repo), desde `data/experiment/reextraccion_v2/e0_chunking/` de la copia:

```
patch -p1 < <ruta>/parche_S0-4_sobre_26c6502_sin_aplicar.diff
```

o, sobre una copia que ya tiene el parche de S0-3:

```
patch -p1 < <ruta>/parche_S0-4_sobre_S0-3_sin_aplicar.diff
```

y, para el prototipo con interruptores, a continuación:

```
patch -p1 < <ruta>/parche_interruptores_prototipo_S0-4_sin_aplicar.diff
```

sha256 que tienen que dar (verificado aplicando los diffs sobre los archivos de `git show 26c6502:…`, por los dos
caminos):
- `e0_lib.py` `6226a8f89c0af5d0194daba9d32a62cfc645696063195749d5e9ff75be9aad60`,
  `correr_e0.py` `682d033e79ecd12ff090cd4fc402bfd127096e438a239cbaa39f800022daf6b5`,
  `selftest_e0.py` `f518f5375632238fe770877ada46d316855e2b633bfd0de7bef75daa1259763e`;
- con el de interruptores: `correr_e0.py` `6c434fee63eb2e22c6cc8b1e3bdd3bd89339e4a603a5729ef831feb170f1e400`
  (`e0_lib.py` y `selftest_e0.py`, iguales).
