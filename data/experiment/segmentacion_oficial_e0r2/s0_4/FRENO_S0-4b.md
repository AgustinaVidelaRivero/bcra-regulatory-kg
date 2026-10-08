# U-SEG-OFICIAL — FRENO S0-4b (08/10/2026)
S0-4b del mandato FIRMADO en `e543cb2` (texto firmado `44cf30ca…`), con sus notas al pie hasta las del 08/10/2026 (tarde, `b8332ff`), y el «seguí» de S0-4b. USD 0, sin API. **Nada commiteado**: el mensaje queda PREPARADO. Detalle, salidas y comandos: `REPORTE_S0-4b.md` y `censos/` del paquete.

**Antes**: los asientos de la mesa del 08/10/2026 (noche) están en el log (`b8332ff`, HEAD al empezar); JSON de claves `923dd900…`; código de E0 del repo = `26c6502`; foto sha256 del repo y 2.213 `.pyc`.

**Aplicado una sola vez** (`patch -p1` desde `e0_chunking/`, parche `186e50f0…`, el del paquete revisado; prueba en seco limpia, rc 0): `e0_lib.py` `65a8c3b8bb09da4d…`, `correr_e0.py` `94d353495a585e0a…`, `selftest_e0.py` `ec186071368ca5c4…` (sha256 completos en el informe, §2). `git diff --stat` en `e0_chunking/`: solo esos tres, +1.373 −67.

**Registro en `segmentacion_oficial_e0r2/s0_4/`**: 122 archivos (S0-4a en `s0_4/`, S0-4a-bis en `bis/`, S0-4a-ter en `ter/`: diseño, FRENO, censos, scripts y parche), iguales por sha256 a los de los paquetes revisados, salvo los dos diseños con **nota fechada** al final:
- `DISENO_S0-4.md`: ri_tsa es `reconocido_pleno` (`s1/controles_S1.json`); ri_mmsef cambia 3 avisos y el `text_col` del nodo 2.2 (de null a 76,6).
- `bis/DISENO_S0-4a-bis.md`: los 11.427 son 4.659 del Apartado B y 6.768 del C con los criterios de validación y las aclaraciones (1.380 + 5.388).

Contradicción resuelta por lo autorizado: los FRENO de etapa van en la raíz de `segmentacion_oficial_e0r2/` (como `FRENO_S0-3.md`), pero el «seguí» solo autoriza `s0_4/`, así que los tres quedaron dentro de `s0_4/` (lo dice la nota).

**Controles sobre una copia del repo aplicado** (`censos/controles_S0-4b.txt`; lote `scripts/lote_s04b_S0-4b.sh`):
- Tanda 0 con el script secuencial: **57/57** byte a byte.
- Los 152 dos veces: **768/768, 0 distintos**, e iguales 768/768 a la final de S0-4a-ter: **9.625 unidades**. Los 25 de la tanda 0 dentro de los 152, iguales.
- `selftest_e0` **151/151**, b52 39/39, b581 34/34, b582 59/59, b583 33/33.
- Selftest de claves: **VEREDICTO OK**, contraste con la tabla OK, salida igual byte a byte a `923dd900…`.
- **Manifiesto de los 768** (insumo de S1-bis): `manifiesto_salida_e0_152_S0-4b.json`, y la salida en `e0_152_salida_S0-4b_corrida1.tar.gz` (`333e8e74…`).

**Tabla de reprocesamiento, F19b** (`tabla_reprocesamiento.md:181`): `correr_e0.py:95-100` no se mueve; `:327-339 → :360-372`, `:576-585 → :609-618`, `:1266 → :1302`; `e0_lib.py:352 → :360`, `:473 → :556`. Cada una verificada sobre el código aplicado. Ninguna fila nueva; contraste del selftest de claves OK.

**Hallazgo, sin tocar porque no está autorizado**: 12 citas de la tabla al código de E0 (F16b, F18a, F18b y su nota, F20, F21) se escribieron sobre código anterior a `26c6502` y ya no apuntaban a lo que describen antes de S0-4. Su destino en el código final está en `censos/anclas_e0_tabla_fuera_de_F19b_S0-4b.txt`; tres dan «no contiguo». Para una unidad de la tabla.

**Decisiones de la autora que el código incorpora** (informe §6):
- 07/10/2026 (noche), sobre S0-3: S0-4 antes de S1-bis, sub-documento por lista, 4a y 4b en lugar del mecanismo 4 y fuera de la tanda 0, 1b y guardas, apartados de ri_ai.
- 07/10/2026 (noche), sobre S0-4a: la tanda 0 sin 4a ni 4b; formulario, circular y sdg3.
- 08/10/2026: las 3, 4 y 5 del §8 de S0-4a; (a) a (d) de S0-4a-bis (ri_oc con sdr1, ri_ccna corregido, la tanda 0 declarada, la nota); (a) a (d) de S0-4a-ter (apl con el Apartado C y los tres límites).

**Límites declarados** (cifras sobre la corrida 1, `limites_declarados_S0-4b.json`):
- `nmaeef::2.9` (1.087 caracteres).
- La tanda 0, fuera de 4a y 4b: 123 puntos. 53 son de 4a, con la oración entera en la herencia (53 de 53, en 249 unidades: E1 la veía); 61 de 4b, cosméticos; 9 sin regla.
- `ri_cc::RIP::S0` (57.922 caracteres; tanda 3).
- Las 10 unidades de solo rótulo: `ri_ccna::D1A3L2::S0` 22, `ri_oc::A2::S0` 30, `ri_oc::SA` 34, `nmcief::A1P2::S0` 50, `nmcief::A1P4::S0` 40, `ri_ccna::D2A1P1::S0` 21, `ri_ccna::D2A1P2::S0` 27, `ri_icpipsp::A1C1::S0` 43, `A1C2::S0` 37 y `A1C3::S0` 73.
- A.1 y A.2 de ri_ccna dentro de `D1A3L1::S0` (1.220 caracteres).
- Los criterios de validación de ri_oc como cierre de C (5.313 caracteres), heredados por C.1 a C.11: 5.484 caracteres cada una, 5.277 de cierre. En total, 837 unidades con cierre heredado, en 60 TOs.
- `ri_oc::B.2::intro` (115 caracteres; cosmético).
- `nmcief::A6::S0` (23.071) y `manori::1.5.1` (15.949), a la condición 12. Hay 28 unidades de más de 13.944 caracteres.
- ri_tsa y ri2_pm, fuera por lista.

**Repo antes y después** (`censos/convivencia_S0-4b.txt`): por S0-4b cambian solo los tres archivos de E0, la tabla y los 122 de `s0_4/`. De otra mano cambiaron, durante la sesión, `CLAUDE.md` (commit `1f9b262`, que movió HEAD) y `.claude/scheduled_tasks.lock`, que se borró. `.pyc` 2.213 = 2.213. **Grep de convenciones** (script de S0-4a; control positivo 16 de 16): sobre el paquete, 0 nombres de personas, 0 rutas absolutas, 0 referencias al origen de una decisión, 1 coincidencia de texto del corpus (`grep_convenciones_paquete_S0-4b.txt`). Sobre los 122 archivos escritos en `s0_4/`: 0 nombres de personas y 0 rutas con el usuario. Hay 282 coincidencias: 256 son del script del grep y de las tres salidas de grep de las etapas (la lista de términos y sus contextos) y 26 son texto del corpus (`grep_convenciones_s0_4_repo_S0-4b.txt`).

**Mensaje de commit PREPARADO** (`mensaje_commit_S0-4b.txt`), no corrido. Comandos para la autora, desde la raíz del repo:
```
git add data/experiment/reextraccion_v2/e0_chunking/e0_lib.py data/experiment/reextraccion_v2/e0_chunking/correr_e0.py data/experiment/reextraccion_v2/e0_chunking/selftest_e0.py data/experiment/mantenimiento/tabla_reprocesamiento.md data/experiment/segmentacion_oficial_e0r2/s0_4
git commit -F <paquete>/mensaje_commit_S0-4b.txt
```

**Paquete**: `<scratchpad>/revision_USEG_OFICIAL_FRENO_S0-4b/` con `manifest.txt`, con el registro de `s0_4/` adentro (`registro_s0_4_S0-4b.tar.gz`). **Copia permanente** (CLAUDE.md §4.g): `~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/622e3b69-11da-4087-ada8-a82839c1329a/scratchpad/revision_USEG_OFICIAL_FRENO_S0-4b/`, con `ditto`; verificada en la copia contra su `manifest.txt`: 31 de 31 archivos iguales (sha256 y bytes), 0 distintos.

FRENO. Espero la revisión; después sigue S1-bis.
