# U-SEG-OFICIAL — FRENO S0-4a-ter (08/10/2026)
S0-4a-ter del mandato FIRMADO en `e543cb2` (texto firmado `44cf30ca…`), con la nota al pie del 08/10/2026 (`ae76f08`, líneas 620-655) y el despacho de S0-4a-ter con el agregado de la autora (Apartado B). USD 0, sin API. **No toqué el repo**: el código es un parche sobre `26c6502` y el registro está en el scratchpad con la estructura de `s0_4/ter/` (se copia en S0-4b). Nada commiteado. Detalle y anclas: `ter/DISENO_S0-4a-ter.md`; salidas en `ter/censos/`.

**Base**: HEAD `ae76f08`; JSON de claves `923dd900…`; copia de S0-4a-bis puesta al día con HEAD (51 archivos, 0 enlaces); punto de partida, el código de S0-4a-bis.

**Cinco reglas nuevas, cada una con su interruptor en `REGLAS_S0_4` y por lista** (efecto de cada una sola, encima de S0-4a-bis; los otros cuatro TOs de la lista no cambian con ninguna):
- **sdr1** (ri_oc; decisión a): el régimen de la página 1 es el del TO y no prefija. ri_oc 128 → 133, 12 eventos: **igual byte a byte a la medición de S0-4a-bis** (5 unidades nuevas, 3 renombres `S4`-`S6` → `A2::S4`-`S6`, `3.51` sin los anexos).
- **apl** (ri_oc; agregado de la autora): la forma de la regla 4 («APARTADO X:» y «X.n.»), que ya leía ri_spi, en la lectura sin raíz de ri_oc. **El Apartado B se separa**: 37 unidades (B.1.1 a B.3.4), y por la misma forma el C: 13 unidades. `3.51` queda con su texto, 778 caracteres. Acotada por lista, con su caso sintético y medido, sin mover otros TOs: entra.
- **sdl** (ri_ccna; decisión b): sub-documento de letra («A. GENERAL», «B. PRUEBAS SUSTANTIVAS»; serie desde la A, título en mayúsculas). B.1 y B.2 pasan a ser `D1A3L2::S1` y `S2`. Sola: 159 → 163, 103 eventos, lo del prototipo de la mesa.
- **sdlh** (ri_ccna; decisión b): **las 47 de B.3 a B.40 heredan «B. PRUEBAS SUSTANTIVAS»**. Sin sdl, además, los 2 ítems de A.2 heredan «A. GENERAL»: 49 cambios, solo herencia.
- **sdla** (ri_ccna; la pieza que pedía A.3): «A.3.», con la letra vigente y más afuera que la raíz abierta, abre su raíz. **A.3 se separa**: `D1A3L1::SA.3`, 211 caracteres. La forma «A.3.» de la regla 4 no servía, porque necesita un «APARTADO A:».
- **Juntas**: ri_oc 128 → 184; ri_ccna 159 → 164, con `D1A3::S2` (1.450) partido en A.2.2 (667), A.3 (211), el rótulo de B (22), B.1 (304) y B.2 (242). Son las posiciones de la mesa. **De la decisión (b) no queda nada sin corregir.**

**Controles duros** (`censos/controles_S0-4a-ter.txt`, `tanda0_S0-4a-ter.txt`):
- Tanda 0: **57/57** en diez corridas (final dos veces, todo apagado, S0-4a-bis, cada regla nueva sola, las cinco solas); los 25 de la tanda 0 dentro de los 152, iguales.
- Nuevas apagadas = S0-4a-bis, **768/768**; todo apagado = S1, **768/768** (también contra `s1/manifest_salida.json`).
- Prendidas: contra S0-4a-bis cambian 8 de 768 archivos, todos de ri_oc y ri_ccna. Doble corrida, 0 distintos; prototipo = código (64 TOs, 320/320).
- **Selftest de claves**: VEREDICTO OK, salida igual byte a byte a `923dd900…`.
- Selftests sobre la copia: selftest_e0 **151/151** (14 casos nuevos: sintético y medido para cada regla), b52 39/39, b581 34/34, b582 59/59, b583 33/33.
- Unidades de más de 13.944: **28** (S1 34, S0-4a 29, S0-4a-bis 29; sale `ri_oc::3.51`).

**Conciliación**:
- Cada regla sola contra S0-4a-bis: 168 eventos en 2 TOs. Una interacción: `D1A3L1::SA.3`, que solo existe con sdl y sdla juntas. sdlh y sdla llegan como contenido de los ids de sdl.
- Dentro de la final, cada regla tiene sus efectos propios: la final contra la final sin esa regla.
- Contra S1: 1.540 + 64 (ri_oc) + 5 (ri_ccna) = **1.609**. La única interacción real sigue siendo `nmcief::A4::S1`. El método marca también `ri_oc::3.51`, que no es interacción: sdr1 y apl la cambian cada una sola.
- Unidades: 9.564 → **9.625** (+113 −52; 51 de los 52 son renombres con el mismo texto). Tabla: F19b, F01, F02 y F05; ninguna fila nueva.

**Parche final** (verificado por los dos caminos): `e0_lib.py` `65a8c3b8…`, `correr_e0.py` `94d35349…`, `selftest_e0.py` `ec186071…`; reemplaza al de S0-4a-bis. **Anclas de F19b**: `correr_e0.py:95-100` no se mueve, `:327-339 → :360-372`, `:576-585 → :609-618`, `:1266 → :1302`; `e0_lib.py:352 → :360`, `:473 → :556`.

**Límites declarados que quedan**:
- ri_oc: los «Criterios de validación» y las «Aclaraciones» (pp. 19-21) no tienen forma propia. Quedan en el Apartado C: el título al final de `C.11` y el texto como `SC::cierre` (5.313). C.1 a C.11 lo heredan, con 5.484 caracteres cada uno; E0 ya hace eso en 826 unidades, con un máximo de 6.588.
- Unidades de solo rótulo nuevas: `D1A3L2::S0` (22), `ri_oc::A2::S0` (30) y `ri_oc::SA` (34). Se declaran como las 7 que ya produce sd.
- ri_ccna: A.1 y A.2 quedan en `D1A3L1::S0` (1.220), y los ítems de A.2 no heredan «A.2. ANALISIS DE VARIACIONES».
- Las guardas hacen falta. Sin lista, la forma de letra abriría en manori y ri_dsf; sin la guarda de mayúsculas, en 14 TOs más.

**Correcciones**: **los 11.427 de S0-4a-bis no eran el Apartado B**. Son 4.659 del B más 6.768 del C, de los criterios y de las aclaraciones. Es un error propio: medí hasta el final de la unidad sin leer lo que seguía, y la cifra llegó a la nota al pie y a la decisión (a). Con apl deja de ser límite. Además, ri_mmsef `text_col` del nodo 2.2 (de null a 76,6), para la nota fechada de S0-4b.

**Errores propios** (diseño §13, con su causa):
- La cifra de 11.427.
- Anclas escritas de memoria en un borrador, otra vez; corregidas contra el código antes de entregar.
- Dos afirmaciones de un borrador corregidas.
- Un script de edición con error de sintaxis, que no llegó a tocar el archivo.

**Decisiones de la autora (PENDIENTES)** (diseño §11): que apl separe también el Apartado C, con los criterios dentro como límite; las unidades de solo rótulo; el límite de A.1 y A.2.

**Convivencia** (`censos/convivencia_S0-4a-ter.txt`): foto del repo antes (10:51) y después (11:58), HEAD `ae76f08` en las dos. Hay 28 diferencias, todas de otras unidades en el árbol de trabajo, entre ellas una nota al pie del mandato sin commit de las 11:15, que leí y no contradice esta etapa. Ninguna está en E0 ni en `segmentacion_oficial_e0r2/`; `.pyc` 2.213 = 2.213. **Paquete**: `<scratchpad>/revision_USEG_OFICIAL_FRENO_S0-4a-ter/` con `manifest.txt`. **Grep de convenciones** (el script de S0-4a, sobre el paquete entero; control positivo 16 de 16; `censos/grep_convenciones_S0-4a-ter.txt`): 0 nombres de personas, 0 rutas absolutas, 0 referencias al origen de una decisión; 5 coincidencias, todas texto del corpus.

FRENO. Espero la revisión y el «seguí» de S0-4b; no aplico el código al repo.
