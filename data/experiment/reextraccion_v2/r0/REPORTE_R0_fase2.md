# REPORTE de R0, fase 2: E3-01 de la tanda 0, con API (14/10/2026; USD 0,157948 de un tope de 1,50; sin commit)

Rige el «seguí» de la autora del 13/10/2026 sobre el despacho de la fase 1, con estas decisiones:
- b1: sembrar las 20 filas de O3 en la base de E3 del pipeline;
- c1: correr en `r0/corrida/` y anexar a `salida_r2b/{ext,docvig}/`;
- quedan autorizadas las dos bases y `logs/cache_usage.jsonl`, con respaldos;
- A3r se redefine en el selftest de claves.

Las rutas son de `data/experiment/reextraccion_v2/` salvo que digan otra cosa. Los controles corrieron sobre copias del repo hechas
con el `rsync` de la cláusula de la mesa, con 0 archivos de entorno y 0 enlaces (`fase2/copias.log` del paquete). La foto del repo no
abre los `.env`: los registra por tamaño y fecha (`r0/controles/foto_repo_sin_env_R0.py`).

## 1. Antes de correr

**Paso 0** (14:11:56): todo dio lo esperado. HEAD estaba en `1d690df3`; las tres carpetas no tenían cambios, y los seis sha256 eran
los del «seguí».

**Respaldos** (14:14:06 a 14:14:07; `revision_R0_fase2/respaldos/`). En las siete copias, el sha256 coincide con el del original.

| Archivo | Tamaño | sha256 |
|---|---|---|
| `e3_verificador/cache/e3_verificacion.db` | 265.510.912 | `221d8874632a…` |
| `e3_verificacion.db-wal` | 0 | `e3b0c44298fc…` |
| `e3_verificacion.db-shm` | 32.768 | `fd4c9fda9cd3…` |
| `e3_verificador/cache/e1_reintentos.db` | 53.846.016 | `9c0f87cc53cd…` |
| `e1_reintentos.db-wal` | 0 | `e3b0c44298fc…` |
| `e1_reintentos.db-shm` | 32.768 | `fd4c9fda9cd3…` |
| `logs/cache_usage.jsonl` | 3.910.767 (16.611 líneas) | `9e6d0085ea6f…` |

Los dos `-wal` estaban vacíos. Los sha256 enteros están en el `manifest.txt` del paquete.

**Otros registros previos:**
- el sha256 de los 234 archivos de `salida_r2b/` (19 de ext y 18 de docvig) y de los 57 de la E0 de la tanda 0, a las 14:14:17;
- la foto del repo a las 14:13:42: 50.453 archivos, de los cuales 7 son de entorno y quedaron registrados sin abrir;
- los `.pyc`: 10.158, y 2.213 fuera de `.venv/`.

## 2. La corrida

Comando, desde la raíz del repo: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/reextraccion_v2/r0/correr_r0.py
--correr --tope 1.50 --reuso-o3 sembrar`. Corrió de 14:14:31 a 14:15:45, salió con 0 y sin freno.

- **Controles previos:** 20 de 20 en cada uno, y los esperados son iguales a los sellados (`81598c97…`).
- **Sembrado:** se insertaron 20 filas de O3 en `e3_verificacion.db` (7.698 → 7.718), las 20 iguales a O3 y ninguna presente antes.
- **Llamadas:** 26 pasaron por la guardia. Las 20 verificaciones salieron de la caché local (USD 0). Hubo 6 llamadas a la API: 3
  reintentos de E1 y 3 re-verificaciones de E3. Todas respondieron `claude-haiku-4-5-20251001` (E1) o `claude-sonnet-5` (E3).
- **Gasto:** USD 0,157948 en el presupuesto compartido, el log de usage y el registro de llamadas; las tres fuentes coinciden.

## 3. Los controles sobre `r0/corrida/`, antes de anexar

`r0/controles/r0_f2_controles.py` → `r0/controles/r0_f2_controles.json`. Corrió sobre una copia; el repo no cambió (fotos de las
14:17:42 y 14:17:54). Los seis controles dan OK.

1. **E1 del intento 0:** acierta la caché en 20 de 20, en la corrida y ahora.
2. **Las 20 verificaciones y el reparto:**
   - las 20 salen de las filas sembradas y su veredicto es el de O3 en 20 de 20;
   - el reparto es 16, 3 y 1, el de la enmienda 7, §1.2, unidad por unidad;
   - el estado de cada aceptada es el que da el veredicto de O3.
3. **Las re-verificaciones, contra O3 y contra la tanda 0** (se declaran: E3 no fija la temperatura):

   | Unidad | O3, intento 0 | R0, re-verificación | Estado en R0 | Tanda 0, re-verificación y estado |
   |---|---|---|---|---|
   | `ext::3.6.4.1` | 1 faltante, 1 bloqueante | `completo_ok` | `aceptado_tras_reintento` | 2 residuales (baja y media); `aceptado_tras_reintento` |
   | `ext::3.16.2.1` | 2 faltantes, 1 bloqueante | 2 residuales (media, sin cita verificada; baja) | `aceptado_tras_reintento` | 1 residual (baja); `aceptado_tras_reintento` |
   | `ext::3.18.1.1` | 2 faltantes, 2 bloqueantes | 1 faltante alto, sin cita verificada | `cola_humana` | 1 faltante alto, sin cita verificada; `cola_humana` |

   - En `ext::3.18.1.1`, la re-verificación de R0 trajo el veredicto entero como texto dentro de `faltantes`. El código lo leyó como
     JSON (`lectura_faltantes: json`, el caso j de P3b) y dio `faltantes_detectados`. En el JSON del control figura `veredicto: null`
     porque el resumen lee el campo de arriba.
   - `ext::3.6.4.1` se acepta con la marca `copia_nota_e3` en la descripción de una Excepcion (`ext/copias_nota_e3.jsonl`). Pasa de
     3 a 4 entidades y se queda en 4 relaciones.
   - `ext::3.16.2.1` pasa de 13 a 17 entidades y de 12 a 26 relaciones, sin marcas.
4. **Reintentos:** solo donde los manda el ratchet, que son las 3 unidades, cada una con un reintento de E1, y solo ellas tienen
   reintentos en `finales`.
5. **El costo real:** 6 líneas nuevas en `logs/cache_usage.jsonl`, y el log es su respaldo más esas líneas. Con la fórmula de caching:

   | Componente | Llamadas | USD |
   |---|---|---|
   | E1 | 3 | 0,087305 |
   | E3 | 3 | 0,070643 |
   | Total | 6 | 0,157948 |

   - Tokens: 20.940 de entrada, 8.889 de salida, 39.477 de escritura y 78.954 de lectura de la caché de la API.
   - Contra lo estimado: A, 0,0719 (no cuenta la escritura de los prefijos); mi estimación con reuso, 0,1555.
6. **Las bases:**
   - en `e3_verificacion.db`, 23 filas nuevas (las 20 sembradas y 3 re-verificaciones, todas `claude-sonnet-5`);
   - en `e1_reintentos.db`, 3 filas nuevas (`claude-haiku-4-5-20251001`);
   - en las dos, 0 borradas y 0 cambiadas.

## 4. Las cuentas

| | Aceptadas con el intento 0 | Aceptadas tras reintento | A la cola | Total |
|---|---|---|---|---|
| ext | 16 (11 `completo_ok_directo`, 5 `aceptado_con_residuales`) | 2 | 1 (`cola_humana`) | 19 |
| docvig | 0 | 0 | 1 (`cola_humana_veredicto_inutilizable`) | 1 |
| Total | 16 | 2 | 2 | 20 |

Reintentaron 3 (`ext::3.6.4.1`, `ext::3.16.2.1` y `ext::3.18.1.1`). La que volvió a reintentar y terminó en la cola es `ext::3.18.1.1`,
por la regla de siempre (decisión 3 al firmar la enmienda 7): ratchet de un reintento y cola.

## 5. El anexo

Corrió `correr_r0.py --anexar` de 14:18:29 a 14:18:30: 8 archivos y 49 renglones (`r0/corrida/anexo_r0.json`).

| Archivo | Renglones | sha256 antes → después |
|---|---|---|
| ext/finales | 19 | `228d3f9f…` → `922a91fa…` |
| ext/veredictos | 22 | `d76cd722…` → `d38e9d5b…` |
| ext/reintentos_e3 | 3 | `018620b5…` → `1de09948…` |
| ext/cola_humana | 1 | `5b7f5e87…` → `82aeeea1…` |
| ext/copias_nota_e3 | 1 | `c5d315a9…` → `93c4bf4f…` |
| docvig/finales | 1 | `e7883727…` → `08db166c…` |
| docvig/veredictos | 1 | `e96ab413…` → `5cc66dc1…` |
| docvig/cola_humana | 1 | `d1375405…` → `de4f1c40…` |

**El control** (`r0/controles/r0_f2_control_anexo.py` → `r0_f2_control_anexo.json`, contra el sha256 de las 14:14:17 y la versión de
HEAD) da OK:
- cambian exactamente los 8 archivos del anexo;
- cada uno es su versión de HEAD más los renglones de `r0/corrida/`, byte a byte, todos de las 20;
- los otros 226 archivos de `salida_r2b/` no cambian, y ninguno se agrega ni se borra;
- la E0 de la tanda 0 sigue igual: 57 de 57;
- en `finales.jsonl`, la última versión de las 20 es la nueva, y la de las demás unidades no cambia.

Fuera de `salida_r2b/`, el anexo solo escribió `r0/corrida/anexo_r0.json` (fotos de las 14:17:54 y las 14:19:03).

## 6. A3r

Sobre una copia hecha después del anexo (14:20:47 a 14:21:20), corrí dos versiones del selftest de claves.

**El selftest de hoy, sin cambios** (`--salida-r2b <copia>/…/salida_r2b`; 14:21:38 a 14:21:46): veredicto FRENO.
- A3r da DISCREPANCIA solo por las 20 presentes: `items_presentes` son las 20, no falta ningún no ítem y faltan 1.034.
- De eso salen el contraste con la tabla en FRENO (las filas F18a y F23b citan A3r) y el veredicto.
- Contra el JSON de HEAD, hay dos diferencias más, ajenas a la regla:
  - el contraste tiene la fila F19d, que entró a la tabla en `2374968a` (13/10/2026), después de la última regeneración del JSON
    (`604640c3`, 07/10/2026); coincide;
  - en el perfil sellado, el bloque A3 sigue OK (2.430 de 2.430) y su conteo informativo `claves_db_en_namespace` pasa de 7.698 a
    7.721: el namespace de E3 es el mismo en los dos perfiles, y esas son las 23 filas de R0.
- A1, A1r y las 69 variaciones (25 del perfil sellado y 44 del r2b) son iguales.

Ningún otro bloque da otra cosa, así que seguí.

**La redefinición**, en `mantenimiento/code/selftest_clave_cache.py`:
- `regla_a3r`, una función pura sobre los pares, las claves de la base y las 20 de R0: exige presentes los no ítems y las 20 claves de
  `verificacion` de `r0/esperados_r0.json` (las lee `claves_verificacion_r0`, controlando el sha256 `81598c97…`), y ausentes,
  exactamente, los ítems que no son de R0. Cualquier otra ausencia o presencia es DISCREPANCIA.
- Dos variaciones de control dentro del bloque A3r, que aplican la misma regla a la base alterada y tienen que dar DISCREPANCIA:
  - A3r_v1 quita una de las 20 (la primera en orden, `docvig::3.3.2`);
  - A3r_v2 agrega la clave de un ítem que no es de R0 (el primero, `cap::1.4.1`).
- No son variaciones R, porque toda variación R exige su fila en la tabla.
- Se actualizan el encabezado del módulo y el campo `regla`.

**El selftest entero, con la redefinición** (14:23:12 a 14:23:19): veredicto OK.
- A3r da OK: 1.386 no ítems y las 20 de R0 presentes; 1.034 ausentes, que son los ítems que no son de R0; A3r_v1 y A3r_v2 dan
  DISCREPANCIA.
- El contraste con la tabla da OK, y no hay variaciones con discrepancia.
- Una segunda corrida, ya con la nota en la tabla de la copia, dio el mismo JSON byte a byte (`e11175ed…`).

**En el repo**, igual byte a byte a la copia:
- `mantenimiento/code/selftest_clave_cache.py` (`43916f77…` → `9cceae48…`);
- `mantenimiento/selftest_clave_cache.json` (→ `e11175ed…`);
- la nota fechada en `mantenimiento/tabla_reprocesamiento.md` (→ `ede20745…`).

Antes de pasarlos, controlé que las versiones del repo fueran las que había copiado. Los diffs están en el paquete:
- `.py`: 67 líneas agregadas y 11 borradas (`git diff --numstat`), entre ellas el encabezado, las dos funciones y el bloque de E3
  de A3r;
- `.json`: 86 agregadas y 25 borradas, en el bloque A3r, la fila F19d del contraste y el conteo del namespace;
- tabla: 12 líneas agregadas, la nota.

## 7. Lo que manda declarar la enmienda 7, §1.5

`r0/controles/r0_f2_cifras_enmienda7.py` → `r0_f2_cifras_enmienda7.json`. Usa la última versión de cada unidad en `finales.jsonl` de
los diez TOs, en HEAD (antes del anexo) y ahora. En HEAD reproduce las anclas: 74 en la cola y la población de 2.366.

- **La cola de la tanda 0 r2b:** de 74 a 69 de 2.439. Por estado, de 43, 29 y 2 a 42, 25 y 2 (inutilizable, `cola_humana` e
  inválida).
  - Salen 5: `ext::2.6.1.1`, `ext::3.5.6.1`, `ext::3.6.1.1` y `ext::3.6.4.2`, que estaban en `cola_humana`, y `ext::3.13.1.10`, que
    estaba en inutilizable.
  - No entra ninguna.
  - Siguen en la cola `ext::3.18.1.1` y `docvig::3.3.2`.
- **La población de U-LECTURA-ACEPTADAS:** de 2.366 a 2.371. Los ítems pasan de 1.003 a 1.008, y los no ítems siguen en 1.363.
  - `ext::2.6.1.2`, de la muestra de 60, se leyó sobre el reintento; su última versión es ahora el intento 0 (`completo_ok_directo`).
  - Las cifras de L2 quedan medidas sobre el grafo sellado anterior.
- **La línea de base del pre-registro de la tanda 1:** la cola medida en r2b, 74 de 2.439 (3,0 %), y la que queda para el grafo
  re-sellado, 69 de 2.439 (2,8 %).
  - El ensamblado del re-sellado todavía no corrió: la cifra es la de `finales.jsonl` después de R0, que es lo que ese ensamblado
    toma.
- **Las notas en `docs/insumos_escritura.md` §7,** ítems 4 y 6, que pide el §1.5, no estaban entre mis escrituras: quedan PENDIENTES.

## 8. Errores propios y declaraciones

- **Error propio, con su causa.** `correr_r0.py` usa los mismos dos clientes para los dos TOs, y el runner arma clientes nuevos por TO.
  Por eso, en la carpeta de trabajo:
  - `r0/corrida/estado_corpus.json` le asigna a `docvig:e3` el gasto de ext (0,157948, cuando el de docvig fue 0);
  - `r0/corrida/docvig/resumen_e3.json` cuenta las llamadas acumuladas (23);
  - el checkpoint de cierre de docvig imprime «gasto=USD 0.32».

  El gasto real y el tope se controlaron con el presupuesto compartido, el log y el registro de llamadas, que coinciden en 0,157948.
  Nada de lo anexado sale de esos archivos. En la corrida en seco de la fase 1 ya pasaba, y no lo vi.
- **Error propio de la fase 1, con su causa.** Las fotos de la fase 1 usaron el script de S0-6a-bis, que calcula el sha256 de todos
  los archivos. Para eso leyó los 7 archivos de entorno, y sus sha256 quedaron en las fotos del paquete `revision_R0` (y en su copia
  permanente). Ninguna salida muestra su contenido. En la fase 2 la foto los registra sin abrirlos.
- **Borrados del scratchpad** (14:13:22): la copia de la fase 1, que conservaba el `.env.example` rastreado de `run_2_papers/code/`, y
  las bases de su corrida en seco.
- **Los `-wal` y los `-shm` de las dos bases desaparecieron después de la corrida** (foto final contra la de las 14:13:42). SQLite,
  en modo WAL, vuelca el `-wal` en la base y borra los dos archivos al cerrarse la última conexión. Los `-wal` estaban vacíos, los
  datos nuevos están en los `.db` (los controles leyeron ahí las 23 y las 3 filas nuevas), y las copias de los cuatro archivos
  están en los respaldos.
- **Las copias de la fase 2 no tienen el `.env.example`.** Ninguno de los controles compara la copia con el repo archivo por archivo.
- **Lo que no toqué:** no abrí `fuera_del_repo/` (solo escribí el paquete y su copia permanente). No actualicé el SDK, no escribí en la
  memoria ni en `.claude/`, y no usé esperas programadas.
