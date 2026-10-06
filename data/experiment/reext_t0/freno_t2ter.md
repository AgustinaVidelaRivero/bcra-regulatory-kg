# FRENO T2-ter de U-REEXT-T0 — reparación acotada, A1r y tabla de reprocesamiento (06/10/2026, USD 0,249002 de un tope de 1, sin commit)

**Precondiciones** (salidas):
- a. `git log --oneline -1 -- data/experiment/reext_t0` → `4ab7a0a U-REEXT-T0 T2-bis (…`; el `git status --short` de `reext_t0`, `reextraccion_v2` y `mantenimiento` sale vacío. b. `git diff --stat 9f6361e HEAD -- …/e0_chunking/` sale vacío. c. `pgrep -fl runner_corpus` no devuelve nada (rc 1).
- d. `cap:e1` 6.088218, `cap:e3` 4.789644; presupuesto 50.152696. La última versión de `cap::4.2.1.2::parte1` y de `cap::3.1.1.2` da `salida_mal_formada_tras_reintento`, y su crudo trae solo `['entities']`.
- **Contradicción**: el despacho dice que el defecto lo tuvieron diez unidades y que en 8 el reintento lo resolvió. Recontado desde los registros de E1 (`cifra_reparacion.py`): son 12 salidas en **8** unidades, y el reintento resolvió **6**. La nota firmada no da la cifra de unidades.

**Código**, primero sobre una copia y después en el repo (diffs en el paquete):
- `runner_corpus.py`: `reparar_relations_ausente` (`:542-559`), la reparación al cerrar el camino de forma (`:710-720`), la marca `reparacion_forma` (`:727-728`) y `reparadas_forma` en el resumen de E1 (`:816-819`). La reparación es de r2b, como `-rforma2` (lectura mía). «La acepta» la leo como sin rechazos de chunk.
- El registro guarda la salida reparada como `tool_input_crudo`, porque `entrada_r2` la vuelve a validar. La salida del modelo queda en la caché y en `reintento_forma`.
- `selftest_clave_cache.py`: en A1r, la clave del reintento por forma se arma con `kwargs_reintento_forma_r2b`, y las unidades con segundo reintento suman su clave en `-rforma2` (`:433-490`). Se agrega la variación R25b (`:1186-1202`).

**Sobre la copia**:
- La batería da igual que la final de T2-bis, salvo `selftest_clave_cache`, que pasa de FRENO a **OK**. A1r da 2.449 claves, 8 en `-rforma1` y 2 en `-rforma2`, todas en la base; A3r da 2.438 pares. El contraste, con R25b en F08c, da OK.
- Contra T2-bis, ninguna variación del selftest cambia: **0 claves se mueven**.
- Pruebas sintéticas: **8/8**. Sin `entities`, con `relations` inválida, con un corte final o con el perfil sellado, la salida sigue dando error.
- En seco (`seco_t2ter.py`): 0 pedidos de E1 al SDK, 2 de E3, «corrida completa».

**Corrida** (`lanzar_t2ter.py`, `--autorizado-tope 80.0`, vigilante a 51,152696, que no actuó; de 08:46:41 a 08:48:54, −03): «corrida completa: gasto global=USD 50.4017».
- **Gasto nuevo 0,249002** = E3 0,129267 + 1 reintento de E1 del ratchet 0,119735. `cap:e1` sigue en 6,088218, `cap:e3` queda en 5,038646 y el presupuesto en 50,401698. **4 filas nuevas = 4 líneas de usage**. E1 no pagó nada: 7 aciertos de caché.
- `cap::3.1.1.2` queda reparada en `-rforma2` y `aceptado_con_residuales`, con 2 nodos.
- `parte1` queda reparada en `-rforma2`. E3 reclamó, el ratchet hizo 1 reintento y la unidad terminó en la **cola humana**; sus 54 nodos entran al E2 r2 marcados como cola.
- **Sin validación: 0.** El E2 r2 de cap pasa de 2.190 a 2.244 nodos; las aristas no cambian (3.150), porque las reparadas traen `relations = []`. El E2 del perfil de E1 pasa de 451 a 452 aceptados y sigue declarando `cap::4.2.1.2` reemplazada.
- **Criterios** (`criterios_t2ter.py`, sobre copias): C1 a C4 OK. Las 461 unidades y partes conservan su registro y su expediente, y los nueve TOs no cambian. El selftest de claves, sobre una copia con la salida de esta corrida, da A1r OK y A3r OK (2.440 pares); solo cambian los conteos de E3.
- **Cuenta de las 2.439**: 1.337 + 812 + 216 + 73 en cola + 1 particionada (parte1 en la cola, parte2 `aceptado_con_residuales`). Las diferencias con los contadores de T2-bis están en el paquete; las normas validadas pasan de 3.603 a 3.632.

**Cifra para la tesis** (decisión 5; `cifra_reparacion.py`, el resumen de E1 y los registros dan lo mismo):
- Después de T2: 7 salidas mal formadas en 6 unidades.
- Después de T2-bis: 12 en 8.
- Después de T2-ter: **12 salidas mal formadas en 8 unidades**. Las 12 son 8 primeros intentos, 2 `-rforma1` y 2 `-rforma2`. 6 unidades se resolvieron con un reintento, **2 quedaron reparadas** y 0 agotadas.

**Tabla**: 45 menciones re-ancladas a las líneas del repo (`reanclar_tabla.py`): las 24 de la lista de T2-bis, F20 y las demás que corrió T2-ter. F08c describe `-rforma2` y la reparación, y suma R25b. Verificación sobre el código del repo: **0 desplazadas**. En dos rangos el código cambió por dentro: F08d `cliente_e1.py:265-283` y F20 `:473-586`.

**Para la autora**: 1. Propongo una fila propia, F08f: la regla de la reparación cambia el E3 de las reparadas y no su E1 (E1 «no cambia», E3 «cambia (las reparadas)»), con una variación nueva, R25c. 2. La parte 1 queda en la cola humana. 3. La contradicción de la cifra de unidades.

**Controles**: el sha256 del repo cambia solo en `runner_corpus.py`, `selftest_clave_cache.py`, la tabla, `salida_r2b/cap/` (15 archivos), los 3 checkpoints, el estado, el presupuesto, las 3 bases, `logs/cache_usage.jsonl` y `reext_t0/t2ter/` (7 scripts) más este freno. `.pyc`: 2.213. Grep de convenciones: en el paquete.

**Paquete:** `revision_UREEXT_T0_FRENO_T2ter/`, en el scratchpad. **Commit PENDIENTE de la autora. Espero el «seguí»; T3 no empezó.**
