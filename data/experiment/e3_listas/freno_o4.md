# FRENO O4 de U-E3-LISTAS: check K estricto (07/10/2026; USD 0, sin API; sin commit)

Mandato firmado en `d9d8888`. La decisión de la autora sobre el check K está en la nota al pie del 07/10/2026 (`604640c`). O2 está en `7fe848c` y O3 en `6dde4b9`; HEAD era `6dde4b9` al empezar (17:23:34). Todo corrió sobre copias de `6dde4b9` armadas con `git archive`, sin enlaces, con las tres bases de la caché y los diez PDF copiados. Paquete: `revision_UE3_LISTAS_FRENO_O4/`, con `manifest.txt`.

**Qué quedó en el repo (sin commit):** solo `selftest_e3.py`, en el bloque K (`git diff --numstat HEAD`: 28 líneas más y 5 menos). Su sha pasa de `59363091…` a `295c569c…`.
- El check «K: sin tablas serializadas…» compara ahora byte a byte contra un mensaje esperado armado desde `m_v3`, con la función local `k_igual`:
  - las NOTAS de siempre, más la NOTA del ítem;
  - después, el resto de `m_v3`, con el fuente entre cercas cambiado por el que lleva el bloque.
- Sin NOTA del ítem, sigue siendo `m_r2 == m_v3`. La franja del fuente, su rótulo y sus cercas vuelven a compararse enteras.
- Tres checks nuevos (`:611-617`) arman mensajes manipulados desde `m_r2`, y los tres tienen que dar False:
  - una línea extra entre la cerca de cierre y «ELEMENTOS EXTRAÍDOS»;
  - otro rótulo para la sección del fuente;
  - el fuente duplicado.
- El caso positivo es el check reescrito, con el mensaje real.

**Criterios:**
1. `selftest_e3` sobre la copia da 114/114: los 111 de HEAD más los 3 nuevos. Fuera de esos 3, la salida es igual a la de HEAD línea a línea.
2. Control de los negativos: en otra copia, con el cuerpo de `k_igual` cambiado por el predicado de O2, fallan exactamente los 3 checks nuevos (111 ok, 3 FAIL).
3. La prueba de la mesa (`verif_check_k.py`, `7f0ebf4e…`), corrida sobre la copia, da una salida igual byte a byte a la suya.
   - En una copia de esa prueba con una columna más (K_O4) el mensaje real pasa y los 7 manipulados frenan.
   - Entre esos 7 están los 3 que dejaba pasar O2. También el 7 (una línea extra solo en el mensaje sin marca), que O2 tampoco frenaba.
4. Candado:
   - `prompt_e3.py`, `comun_e3.py`, `ratchet_e3.py` y la fixture son iguales byte a byte a HEAD.
   - Recomputado sobre la copia, da la fixture `079d2489…` y el mensaje `66bc8656…`, los dos confirmados.
   - El check M del sha de los mensajes (`selftest_e3.py:734`) da verde.
5. Los vecinos dan igual que en HEAD: `selftest_r2`, `selftest_r3`, `selftest_dirigida_tanda0` y `selftest_clave_cache` (su JSON, byte a byte). Las únicas diferencias son el orden en que `selftest_r3` imprime un conjunto y la ruta temporal de `selftest_dirigida_tanda0`.

**Desvío declarado (mandan los archivos):**
- La decisión firmada dice «con el fuente duplicado» y el despacho, «el fuente duplicado dentro de las cercas».
- El caso que pide el despacho (el fuente dos veces entre las mismas cercas) ya lo frenaba O2: la contención del fuente con sus cercas deja de cumplirse.
- El caso que O2 dejaba pasar es el 3 de la mesa: el bloque entero repetido, cada copia con sus cercas.
- Por eso el check (c) cubre las dos variantes. Con el predicado de O2, (c) falla por la segunda.
- La prueba de la mesa la extendí en una copia (`verif_check_k_o4.py`, con su diff en el paquete). El original no lo toqué.

**Controles:**
- Tomé el sha256 del repo a las 17:23 y a las 17:29. De lo mío cambia solo `selftest_e3.py`; después se suma este freno.
- Hay cambios ajenos: 5 archivos de la figura de la tripleta en `docs/tesis/figuras/`, commiteados en `52335db` (17:26:59). Ese commit no toca `e3_verificador/` ni `e3_listas/`.
- Hay 2.213 `.pyc` y ningún `__pycache__` en las copias. El grep de convenciones da 0 nombres y 0 rutas.

Commit PENDIENTE de la autora: con él cierra la unidad. FRENO O4.
