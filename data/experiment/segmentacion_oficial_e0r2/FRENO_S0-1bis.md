# U-SEG-OFICIAL — FRENO S0-1 bis (05/10/2026)
A, B y C de la nota del 05/10/2026 al pie del mandato (`d59921f`), sobre el prototipo de S0-1. USD 0, sin API; nada implementado en el repo ni commiteado. Diseño: `s0_1bis/DISENO_S0-1bis.md`; censos, scripts y parche sin aplicar en `s0_1bis/`.

**Precondiciones.** `git log --oneline -1 -- docs/mandatos/USEG_OFICIAL_segmentacion_e0r2.md` → `d59921f`; el texto firmado (`git show e543cb2:…`) y las 239 primeras líneas en `d59921f` dan `44cf30ca0d82…`. HEAD `d59921f`; `e0_lib.py`, `correr_e0.py` y `e0_tablas.py` sin cambios desde `9f6361e` (`git diff --stat 9f6361e HEAD -- …` vacío).

**Condiciones** (`s0_1bis/censos/condiciones_S0-1bis.txt`):
- Tanda 0: 57 de 57 archivos iguales byte a byte a `salida_tanda0_r2b/`.
- 145 TOs que las reglas nuevas no tocan: iguales byte a byte a la corrida final de S0-1, en archivos por TO y entradas de los agregados. Cambian 7: con la regla 8, adfsp, ceninf, cirmo3, manori, nmaeef y ri_niif; con la 9, rdbcra.
- `particionar_por_corte` en las 2.439 unidades de la tanda 0: igual a `9f6361e` con 1,175 y con 1,498 (`435af2fe…`).
- Con solo las reglas de S0-1, el prototipo nuevo reproduce la corrida final de S0-1 (0 de 768 archivos distintos).

**A — regla 6 en E1.** Los renglones parten solo lo que pasa la capacidad del tercer escalón (40.960 tokens: 34.859 caracteres con 1,175 y 27.343 con 1,498): una unidad sin ítems, o el ítem que deja una parte por encima. El resto conserva la partición por ítems. Ninguna unidad queda sin salida con ninguna de las dos razones (con la partición de `9f6361e` quedan 3 y 4). Con el parámetro cambia de clase solo `ri2_cs::S3`: B con 1,175 y C con 1,498. En el borde queda `ri_cc::S3`, que cambia desde 1,502.

**B — regla 8.** Detecta 12 listas (150 rótulos) en 7 TOs y ninguna en la tanda 0. Es un veto sobre 108 renglones; los otros 42 ya se rechazaban y conservan su motivo. En 6 TOs aparecen 151 ids nuevos y desaparecen 136 (manori 132 y 54; cirmo3 pierde sus 52 `::rep2`). Los rótulos sin padre bajan de 70 a 12 (manori, de 58 a 0) y las tablas serializadas suben de 467 a 468. dmrd p. 6 ya la resuelve la regla 1. Límite: en 5 TOs la lista es una página de índice leída como cuerpo, y su texto queda en una unidad.

**C — regla 9.** El catálogo tiene 119 filas. Antes, 91 tenían unidad; las otras 28 no, porque E0 rechazaba su número. Las 97 unidades terminales 11.x eran esas 91 filas y 6 encabezados, y el control automático daba 10 filas limpias. La regla tiene dos partes:
- 9a acepta el número de la fila, que la celda prueba;
- 9b mueve a la unidad de su fila los renglones de cada banda de `find_tables()`: 223 renglones, en el orden del PDF.

Con las dos, quedan limpias 119 de 119 filas en el control automático y 10 de 10 en la lectura contra el PDF (semilla 20261005), así que no hace falta marcarlas. Con solo 9b, 91 limpias y 28 sin unidad. En rdbcra aparecen 28 ids nuevos y desaparecen 21. Otros 5 TOs tienen tablas con esa forma (191 filas): la regla no actúa en ellos y salen iguales.

**Cruces** (diseño §5, con el orden). La 2 actúa con y sin las reglas nuevas, en ri_niif y rdbcra. La 6 parte unidades de manori y nmaeef con y sin la 8. Sin la 8, la 7 y T actúan en manori; con la 8, T no actúa y la 7 solo reabre `manori::1.5.2`. En rdbcra no actúan ni la 6, ni la 7, ni T. Apagar cualquiera de las cuatro no cambia los 108 vetos ni el anclaje de la 9.

**Parche.** Probé en una copia los dos caminos: el completo sobre `9f6361e` y el incremental sobre el de S0-1. Los dos dan `e0_lib.py` `81c3409851ba82a3…` y `correr_e0.py` `f737028b1918cce0…`.

**Decisiones de la autora (PENDIENTES; diseño §7):** (1) regla 9: 9a y 9b (propuesta; cambia 49 ids) o solo 9b (28 filas sin unidad); (2) páginas de índice de la regla 8: dejar su texto en una unidad (propuesta) o darles rol de índice; (3) con T2: la razón del tercer escalón y el objetivo de las partes.

**Convivencia.** Las copias no tienen enlaces, `.db`, `corpus_tanda0/` ni `logs/`, y no abrí bases, carpetas ni logs de U-REEXT-T0. La foto sha256 del repo (`snapshot_repo.py`, con las exclusiones) cambia solo en 44 archivos nuevos: los 43 de `s0_1bis/` y este freno. Hay 2.213 `.pyc` antes y después, con la misma lista.

**Errores propios, con su causa.** Los cinco los detecté y corregí antes de este freno; ninguno llegó al repo.
1. El censo de listas esperaba 4 valores de la escalera, que devuelve 5.
2. El primer veto de la regla 8 cambiaba motivos de rechazo en ri_ccna y ri2_ae, porque salteaba la rama de raíz.
3. El veto en la raíz implícita registraba el rechazo, pero igual abría la raíz (nmaeef).
4. El aviso de la regla 9 cambiaba `estructura_ext.json` de la tanda 0, porque faltaba la guarda `MAX_RAIZ`.
5. Edité `correr_e0.py` durante una corrida de los 152; la rehíce con el código congelado y sale igual (0 archivos distintos).

**Paquete:** `<scratchpad>/revision_USEG_OFICIAL_FRENO_S0-1bis/` (`manifest.txt`). **Grep de convenciones** (patrones en un archivo del scratchpad, sobre `s0_1bis/`, este freno y el paquete): solo texto normativo del corpus (la descripción de una infracción del catálogo de rdbcra, en 4 renglones de tres censos y en sus copias del paquete); ninguna coincidencia en texto propio.

FRENO. Espero el «seguí» escrito de la autora; no empiezo S0-2.
