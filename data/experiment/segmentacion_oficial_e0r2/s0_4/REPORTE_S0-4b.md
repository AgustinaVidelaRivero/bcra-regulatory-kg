# U-SEG-OFICIAL — S0-4b: el código de E0 de S0-4 aplicado al repo (informe detallado)

Etapa S0-4b del mandato FIRMADO en `e543cb2` (las 239 líneas firmadas dan `44cf30ca0d82…`), con sus notas al pie hasta
las del 08/10/2026 (tarde; en `b8332ff`), y el «seguí» de S0-4b. USD 0, sin API. Ningún commit: el mensaje queda
PREPARADO (§9). Las salidas citadas están en `censos/` de este paquete.

## 1. Antes

- `git log`: el commit de los asientos de la mesa del 08/10/2026 (noche) es `b8332ff`, HEAD al empezar.
- `data/experiment/mantenimiento/selftest_clave_cache.json` del repo: `923dd900…`.
- Código de E0 del repo: el de `26c6502` (`git diff --stat 26c6502 HEAD -- data/experiment/reextraccion_v2/e0_chunking`,
  vacío; `e0_lib.py` `c5e7106a…`, `correr_e0.py` `4570a0c8…`, `selftest_e0.py` `af114a4d…`).
- Sin cambios rastreados en el árbol de trabajo; ningún proceso mío vivo.
- Foto sha256 del repo (`fotos/` en el scratchpad; 47.214 archivos) y lista de `.pyc` (2.213).

## 2. El parche, aplicado una sola vez

- Parche: `ter/parche/parche_S0-4a-ter_sobre_26c6502_sin_aplicar.diff`, sha256 `186e50f0…`, el mismo del manifiesto
  del paquete revisado de S0-4a-ter. Prueba en seco (`patch -p1 --dry-run`) limpia; aplicado con `patch -p1` desde
  `data/experiment/reextraccion_v2/e0_chunking/` del repo, rc 0, sin `.orig` ni `.rej`
  (`censos/registro_lote_S0-4b.txt`, al final).
- sha256 en el repo, los del parche final:
  - `e0_lib.py` `65a8c3b8bb09da4d527fd94e31cfbc52168171bcd1603394aaa8b28c05361de6`;
  - `correr_e0.py` `94d353495a585e0ad4799813a22fb1f1670f33b558f67741b9fceb71d2fcc1bc`;
  - `selftest_e0.py` `ec186071368ca5c415f926bc67960ccab0ede1e9ff35098df5887c2681b38079`.
- `git diff --stat` en `e0_chunking/`: solo esos tres archivos, +1.373 −67 (`e0_lib.py` 744, `correr_e0.py` 89,
  `selftest_e0.py` 607 renglones cambiados).

## 3. El registro, en `data/experiment/segmentacion_oficial_e0r2/s0_4/`

122 archivos (`censos/registro_s0_4_sha256_S0-4b.txt`, con el sha256 de cada uno; copia verificada byte a byte):
- `s0_4/`: el registro de S0-4a: `DISENO_S0-4.md`, `FRENO_S0-4a.md`, `censos/` (32), `scripts/` (19) y `parche/` (3
  diffs y su LEEME);
- `s0_4/bis/`: el de S0-4a-bis: `DISENO_S0-4a-bis.md`, `FRENO_S0-4a-bis.md`, `censos/` (20, con el registro de trabajo
  de la etapa), `scripts/` (10) y `parche/` (4 y su LEEME);
- `s0_4/ter/`: el de S0-4a-ter: `DISENO_S0-4a-ter.md`, `FRENO_S0-4a-ter.md`, `censos/` (17, con el registro de trabajo
  de la etapa), `scripts/` (5, con el que agregó los casos de selftest) y `parche/` (3 y su LEEME).

Cada archivo es idéntico, por sha256, a uno del paquete revisado de su etapa, salvo los dos diseños con nota. **Notas
fechadas** (al final, sin editar el texto; el sha256 del texto revisado está en la nota y en
`censos/sha_textos_revisados_S0-4b.txt`):
- `DISENO_S0-4.md` (texto revisado `579f926d…`; el de `bis/DISENO_S0-4a-bis.md`, `644be886…`): ri_tsa es
  `reconocido_pleno` en `s1/controles_S1.json`, no `parcial_declarado`; ri_mmsef cambia 3 avisos y el `text_col` del
  nodo 2.2 (de null a 76,6), no «un aviso»; y dos indicaciones de lectura (el FRENO está en `s0_4/FRENO_S0-4a.md`; el
  código aplicado es el de `ter/parche/`).
- `bis/DISENO_S0-4a-bis.md`: los 11.427 caracteres de `ri_oc::3.51` que no eran del punto son 4.659 del Apartado B
  (pp. 16-17) y 6.768 del Apartado C con los criterios de validación y las aclaraciones (1.380 y 5.388; pp. 18 y
  19-21); con apl, `3.51` queda en 778.

**Una contradicción, que resolví por lo autorizado**: en el repo, los FRENO de cada etapa están en la raíz de
`segmentacion_oficial_e0r2/` (`FRENO_S0-3.md`) y el diseño de S0-4a cita el suyo como `../FRENO_S0-4a.md`; el «seguí»
autoriza cambios solo en los tres archivos de E0, la tabla y `s0_4/`. Los tres FRENO quedaron dentro de `s0_4/`, y la
nota del diseño de S0-4a lo dice. Si se los quiere en la raíz, es un movimiento de la autora o de la mesa.

## 4. Controles, sobre una copia del repo ya aplicado

La copia del scratchpad, puesta al día con `b8332ff` (10 archivos desde `git cat-file`) y con los cuatro archivos del
árbol de trabajo (los tres de E0 y la tabla), 0 enlaces; los archivos que usan los controles, iguales a los del repo
(`cmp`). Raíz `raices/impl4b`, armada desde la copia. Lote `scripts/lote_s04b.sh`; salidas en
`censos/controles_S0-4b.txt`.
- **Tanda 0, script secuencial** (`herr/correr_tanda0.py`, igual a `s0_1/scripts/correr_tanda0.py`): **57 de 57**
  archivos iguales byte a byte a `salida_tanda0_r2b/`.
- **Los 152 dos veces** (`herr/correr_152.py`, el de S0-1; `manual` aparte y juntado por TO): **768 y 768, 0
  distintos**; la corrida 1 es igual, 768 de 768, a la corrida final de S0-4a-ter (`ter_final`): **9.625 unidades**
  (`censos/manifiesto_salida_e0_152_S0-4b.json`). Los 25 archivos de la tanda 0 dentro de los 152, iguales en las dos
  corridas (agregados: 20 iguales, 15 ausentes en los dos).
- **Selftests** sobre la copia: `selftest_e0` **151/151**, b52 39/39, b581 34/34, b582 59/59, b583 33/33
  (`censos/selftests_e0_S0-4b.txt`).
- **Selftest de claves** sobre la copia, con la tabla ya corregida: **VEREDICTO OK**, anclaje r2b de E1 y E3 OK,
  **contraste con la tabla OK**, salida igual byte a byte al JSON del repo, `923dd900…`
  (`censos/selftest_claves_S0-4b.txt`).
- **Manifiesto de los 768** (insumo de S1-bis): `censos/manifiesto_salida_e0_152_S0-4b.json` (sha256 y bytes de cada
  archivo, y las unidades por TO), y la salida misma, `e0_152_salida_S0-4b_corrida1.tar.gz` (sha256 `333e8e74…`, 768
  archivos; extraída y comparada, 768 de 768 iguales).

## 5. Tabla de reprocesamiento

Fila F19b (`tabla_reprocesamiento.md:181`), solo sus anclas al código de E0: `correr_e0.py:95-100` no se mueve;
`:327-339 → :360-372` (regla 6), `:576-585 → :609-618` (regla 9), `:1266 → :1302` (T); `e0_lib.py:352 → :360` (regla 8),
`:473 → :556` (regla 3, ampliación). Comprobé en el código aplicado que cada una apunta a lo que la fila describe.
Ninguna fila nueva; el contraste del selftest de claves da OK.

**Hallazgo, sin tocar (no autorizado):** las otras anclas de la tabla al código de E0
(`censos/anclas_e0_tabla_S0-4b.txt` y `censos/anclas_e0_tabla_fuera_de_F19b_S0-4b.txt`). Dos valen y no se mueven: F01
(`correr_e0.py:86-94`) y F21 (`correr_e0.py:77-80`). Las otras 12 citas se escribieron sobre código anterior a `26c6502`
(`2a857db`, `ad99ac7`, `53b7708`) y ya no apuntaban a lo que describen antes de S0-4: F16b (`correr_e0.py:1188-1189`,
`e0_lib.py:786-816`), F18a (`e0_lib.py:394-439`, `:914-915`), F18b y la nota de F18a (`e0_lib.py:914-915`), F20
(`correr_e0.py:169-229`, `:232-254`, `:473-586`, `:741-750`) y F21 (`e0_lib.py:1808-1883`, `:421-422`). En el código
final, el código que citaban está, por ejemplo, en `e0_lib.py:1590-1591` (el bucle de páginas de cuerpo de F18a y F18b),
`:1305-1335` (`pies_de_paginas`, F16b) y `:2718-2793` (`recortar_herencia`, F21); tres dan «no contiguo» (el código
cambió por dentro). Para una unidad de la tabla.

## 6. Decisiones de la autora que el código incorpora

- **07/10/2026 (noche), sobre S0-3** (mandato, nota al pie): S0-4 antes de S1-bis, con la regla de sub-documento por
  lista (ri_sef, nmcief, ri_ccna, ri_icpipsp, ri_cc; ri_tsa y ri2_pm fuera); el mecanismo 4 fuera de la tanda 0 y
  reemplazado por 4a y 4b, también fuera de la tanda 0 por lista; la regla 1b y las guardas, sí; los apartados de ri_ai
  S4, a S0-4; `nmaeef::2.9`, límite declarado; el código de E0 cambiado una sola vez.
- **07/10/2026 (noche), sobre S0-4a**: la tanda 0 sigue excluida de 4a y 4b; formulario, circular y sdg3, aceptados.
- **08/10/2026 (tarde), las decisiones 3, 4 y 5 del §8 del diseño de S0-4a**: el rótulo sin numeración que reinicia abre
  su sub-documento; la lista de verbos de 4a y 4b como está (la del despacho más debe(n), puede(n), será(n), tendrá(n));
  los casos del §7 dentro de los sub-documentos como límite declarado, salvo ri_ccna (S0-4a-bis y S0-4a-ter).
- **08/10/2026, sobre S0-4a-bis**: (a) ri_oc, se aplica la variante (sdr1, con ri_oc en su lista); (b) ri_ccna, se
  corrige (sdl, sdlh, sdla); (c) la tanda 0, excluida de 4a y 4b con la cifra medida; (d) la nota fechada a S0-4a.
- **08/10/2026 (tarde), sobre S0-4a-ter**: (a) apl separa también el Apartado C; (b) las 10 unidades de solo rótulo,
  (c) los títulos A.1 y A.2 de ri_ccna dentro de `D1A3L1::S0` y (d) los criterios de validación de ri_oc como cierre
  heredado por C.1 a C.11, como límites declarados.

## 7. Límites declarados, con sus cifras (sobre la corrida 1 de los controles, `censos/limites_declarados_S0-4b.json`)

- `nmaeef::2.9` (1.087 caracteres): el inverso del mecanismo 1 (S0-3); grupo 2, por lista, en la release de E0 antes de
  la tanda 2 (nota del 08/10/2026, tarde, punto 5).
- **La tanda 0, excluida de 4a y 4b**: 123 puntos de la familia del mecanismo 4; 53 de la clase 4a, con la oración
  entera en la herencia de sus unidades hijas (53 de 53, en 249 unidades: E1 la veía); 61 de la 4b (22 retirando la
  intro), cosméticos; 9 sin regla (`s0_4/censos/censo_4ab_sobre_S0-3.json`,
  `bis/censos/herencia_4a_tanda0_S0-4a-bis.json`).
- `ri_cc::RIP::S0` (57.922 caracteres, tabla serializada; ri_cc está en la tanda 3).
- **Las 10 unidades de solo rótulo**: `ri_ccna::D1A3L2::S0` (22), `ri_oc::A2::S0` (30), `ri_oc::SA` (34),
  `nmcief::A1P2::S0` (50), `nmcief::A1P4::S0` (40), `ri_ccna::D2A1P1::S0` (21), `ri_ccna::D2A1P2::S0` (27),
  `ri_icpipsp::A1C1::S0` (43), `ri_icpipsp::A1C2::S0` (37) y `ri_icpipsp::A1C3::S0` (73).
- Los títulos A.1 y A.2 de ri_ccna dentro de `ri_ccna::D1A3L1::S0` (1.220 caracteres).
- Los criterios de validación de ri_oc como cierre del Apartado C (`ri_oc::SC::cierre`, 5.313 caracteres, pp. 19-21),
  heredados por C.1 a C.11: 39 tramos y 5.484 caracteres de herencia cada una, 5.277 de cierre; con las demás unidades
  con cierre heredado: 837 en 60 TOs (máximo 6.588 de cierre, `ri_ii_31_12_19::6.5`).
- `ri_oc::B.2::intro` (115 caracteres): el resto del título de B.2, partido en dos; cosmético.
- `nmcief::A6::S0` (23.071) y `manori::1.5.1` (15.949), a la lista de la condición 12 de la tanda 1; las unidades de más
  de 13.944 caracteres de los 152 son 28.
- ri_tsa y ri2_pm, fuera de la regla de sub-documento por lista.

## 8. Convivencia, `.pyc` y grep

- Foto sha256 del repo antes (13:52:00, HEAD `b8332ff`) y después (14:14:38, HEAD `1f9b262`;
  `censos/convivencia_S0-4b.txt`): cambian solo los tres archivos de E0, la tabla y los 122 de `s0_4/`; además, de otra
  mano, `CLAUDE.md` (commit `1f9b262`, durante la sesión) y `.claude/scheduled_tasks.lock` (borrado). `.pyc`: 2.213 =
  2.213.
- Grep de convenciones: en el FRENO.

## 9. Mensaje de commit, PREPARADO (no corrido)

`mensaje_commit_S0-4b.txt` de este paquete, con los comandos para la autora.
