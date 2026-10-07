# FRENO O3 de U-E3-LISTAS, final de la unidad (07/10/2026; USD 0,238213 de 1; sin commit)

Mandato firmado en `d9d8888`, con la enmienda 1 y la NOTA v2; O1 en `5a97e60`, O2 en `7fe848c`. El código de E3 es el de `7fe848c`: corrí todo sobre una copia armada con `git archive 7fe848c` (sin enlaces). Paquete: `revision_UE3_LISTAS_FRENO_O3/`, con `manifest.txt`.

**Precondiciones contra `7fe848c`: 28 de 28 OK** (`UE3_LISTAS_O3_precondiciones_7fe848c.txt`).
- Al empezar (08:07:19), HEAD era `7fe848c`. Los ocho archivos de O2 son iguales byte a byte en el commit, en el paquete de O2 y en la copia, y `e3_verificador/` del árbol de trabajo coincide con el commit. D3 está en el commit (`6646f7e6…`). Los dos valores del candado son los confirmados. «PROPUESTOS» no aparece en `prompt_e3.py`, así que no había nada que quitar.
- Lista sellada: `cc6b0cd6c56831c486d60bf7da64712cea391a1eb2948eef822448567df9bab6`, la verifiqué antes de la primera llamada. Los 20 mensajes son iguales a la medición de O2 (`a/control_mensajes_o2.json`).
- Hash equivocado (`6e16bb3`): hasta el freno pedido solo había leído; no hice ninguna escritura ni llamada. Nada de lo que hice dependió de ese hash, así que no hubo que rehacer nada.

**(a) Con API** (`o3/a/`; criterio sellado antes de la primera llamada, `criterio_o3.md`, `f3b036e3…`).
- 20 llamadas de E3, todas en `tool_use`. Tokens: 59.900 de entrada, 4.510 de salida, 11.637 de escritura de caché y 221.103 de lectura. Gasto: USD 0,238213, por llamada en `presupuesto.json`; lo estimado en seco eran USD 0,2155.
- Reclamos P, C, B y B2 del intento 0: 21 (3 C, 16 B y 2 B2).
  - Por la regla: desaparecen 18 y persisten 3, todos B (`ext::3.6.4.1`, `ext::3.6.4.2` y `ext::3.16.2.1`).
  - Por la lectura: desaparecen 15 y persisten 6 (`a/lectura_o3.json`, sellada antes de computar).
- Nuevos: 3. Un C bloqueante en `docvig::3.3.2`, que leído es el mismo reclamo de antes (viene del cierre del punto); un B2 y un B, no bloqueantes, en `ext::3.6.1.1` y `ext::3.6.1.2`.
- 11 de 20 unidades salen completas; quedan 14 faltantes, 5 de ellos bloqueantes. Con este veredicto se aceptan 16 de las 20, 14 de ellas entre las 17 que reintentaron.
  Siguen al reintento `ext::3.6.4.1` y `ext::3.16.2.1` (reclamos B que, leídos, son falsas alarmas contra la NOTA) y `ext::3.18.1.1` (composición fundada); va a la cola `docvig::3.3.2`.
- D1: 6 de los 14 faltantes verifican su cita solo gracias al bloque. Los 2 bloqueantes entre ellos son de composición en `ext::3.18.1.1`. El riesgo declarado de D1 no aparece.

**(b) Sin API** (`o3/b/`). De las 17, la final es el reintento en 13, y las 13 cambiaron: entran 58 entidades y 40 relaciones, salen 26 y 7, y 5 cambian de descripción. En las 4 cuya final es el intento 0 (el control) hay 0 cambios. En 11 de las 13, E3 corregido acepta el intento 0.

**(c) D3 por código** (`o3/c/`; selftest 5/5). Repiten la norma del encabezado 1 de las 20 en el intento 0 (`ext::3.6.1.1`) y 8 en la final. Las 7 nuevas son finales del reintento que tenían un reclamo B en el intento 0.

**Declaraciones:**
- Población: 20 unidades y no 24, por la enmienda 1. Corregí ese número en la misma frase del ítem 4 de `insumos_escritura.md` §7, donde reemplacé el PENDIENTE por las cifras.
- Excluí 3 reclamos de la re-verificación (2 P y 1 B, en `ext::3.5.6.1` y `ext::3.6.1.1`): O3 compara la primera verificación.
- Volví a sellar el criterio por una errata («P, C o B2/B» pasa a «P, C, B o B2»), a las 08:11:02, antes de la primera llamada (08:11:20).
- El despacho estimaba USD 0,05–0,10 contando solo los tokens agregados; el gasto real cuenta la llamada entera.
- `e3_listas/cache/` no está en `.gitignore`: la base (`ab532154…`, 20 filas, sin claves ni rutas) figura sin rastrear. Si entra al commit lo decide la autora.
- Error propio, con su causa: al leer la base con `mode=ro` en modo WAL quedaron un `-wal` vacío y un `-shm`. Los borré, y el sha de la base no cambió.
- `logs/cache_usage.jsonl`, que git ignora: tiene 20 líneas nuevas, de las 08:11:20 a las 08:12:16, por la decisión 3 de caching.

**Controles.**
- sha256 del repo a las 08:07 y a las 08:23. Cambian solo `e3_listas/` (28 archivos nuevos, más este freno), las líneas del ítem 4 y el log.
- Cambios ajenos (los hizo otra sesión o la autora, entre las 08:07 y las 08:15): `mantenimiento/` (2 archivos), 5 mandatos y `protocolo_entre_tandas.md`, ya en `604640c`; además, `comp_e1/c2/comun_c2.py`.
- Los commits `604640c` y `ee7c07c`, posteriores, no tocan nada de lo que O3 lee o escribe.
- Los 65 `kg.json` y las 171 bases `.db` fuera de `e3_listas/` están iguales. Hay 2.213 `.pyc`. Grep de convenciones: 0 nombres y 0 rutas; las 96 coincidencias del patrón de mensajes son rutas de `.venv` en los listados de sha.

Commit PENDIENTE de la autora. FRENO O3: final de la unidad. O4 (check K) queda para después, aparte.
