# FRENO de R0, fase 2 (14/10/2026; USD 0,157948 de un tope de 1,50; sin commit)

## Paso 0 (14:11:56 −03)

```
$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg
1d690df3 Reextraccion: la primera fase de la etapa con API de la tanda 0, revisada
d317e4baf2065875f57de6fd1e1c9b28da702efe511cfdb847379f4fe045f382  data/experiment/reextraccion_v2/r0/correr_r0.py
81598c9704a1e66b53c501c7fff34ce1d9b71d20ae0b5a91548ecbf4aba8bfa6  data/experiment/reextraccion_v2/r0/esperados_r0.json
a287c7479939bab8667131c1c9a59cadd61f129a8bb9e0eeed8c2e1567c082a6  data/experiment/reextraccion_v2/corpus_v2/runner_corpus.py
e7b4b164f0062f2d501e854d6e7582e6d35d69ee7f87d13abe86b6b9c673ec10  data/experiment/reextraccion_v2/e3_verificador/cliente_e3.py
cc6b0cd6c56831c486d60bf7da64712cea391a1eb2948eef822448567df9bab6  data/experiment/e3_listas/o3/lista_unidades_afectadas_tanda0.json
43916f77c71c769c1c2f484895c017ab33606f09086fe27cf97a3944f23aa824  data/experiment/mantenimiento/code/selftest_clave_cache.py
```

`git status` no mostró nada en las tres carpetas. Todo dio lo esperado. El detalle está en `REPORTE_R0_fase2.md`.

## Respaldos (14:14:06 a 14:14:07; `revision_R0_fase2/respaldos/`)

| Archivo | sha256 (original = copia) |
|---|---|
| `e3_verificacion.db` | `221d8874632a697901d2fcccc0897812bd2950019ad20d36bc58e3875793c2c9` |
| `e3_verificacion.db-wal` (0 B) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `e3_verificacion.db-shm` | `fd4c9fda9cd3f9ae7c962b0ddf37232294d55580e1aa165aa06129b8549389eb` |
| `e1_reintentos.db` | `9c0f87cc53cdab1d362e8b8d7c475d72d856dedd7644459b6ffb30fc0f408e86` |
| `e1_reintentos.db-wal` (0 B) | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `e1_reintentos.db-shm` | `fd4c9fda9cd3f9ae7c962b0ddf37232294d55580e1aa165aa06129b8549389eb` |
| `logs/cache_usage.jsonl` (16.611 líneas) | `9e6d0085ea6fb1a7ff8c1c523e087878c07dcbe0357232e60e0457367d13847e` |

Los 7 coinciden con el original, y los dos `-wal` estaban vacíos.

## Corrida y controles

- **Corrida** (14:14:31 a 14:15:45; salida 0, sin freno):
  - sembradas 20 filas de O3, iguales a O3;
  - las 20 verificaciones salieron de la caché local;
  - 6 llamadas a la API, con los modelos `claude-haiku-4-5-20251001` y `claude-sonnet-5`.
- **Controles previos al anexo, sobre una copia** (`controles/r0_f2_controles.json`): OK.
  - El E1 del intento 0 acierta la caché en 20 de 20.
  - Las 20 verificaciones son iguales a O3, y el reparto es 16, 3 y 1, unidad por unidad.
  - Solo hubo reintentos donde los manda el ratchet.
  - El costo coincide en el log, el presupuesto y el registro de llamadas.
  - En las bases se agregaron filas (23 en E3 y 3 en E1) y no se borró ni cambió ninguna.
- **Cuentas:**
  - aceptadas con el intento 0: 16 (11 directas y 5 con residuales);
  - reintentaron 3: dos se aceptaron tras el reintento (`ext::3.6.4.1`, con la marca `copia_nota_e3`, y `ext::3.16.2.1`) y
    `ext::3.18.1.1` volvió a la cola (`cola_humana`, como en la tanda 0);
  - `docvig::3.3.2` volvió a la cola (inutilizable).
  - Por TO: ext 19 (18 aceptadas y 1 en la cola) y docvig 1 (en la cola).
- **Re-verificaciones contra O3 y contra la tanda 0** (declaradas, REPORTE §3): las tres terminan como en la tanda 0. En
  `ext::3.18.1.1`, el veredicto llegó como texto dentro de `faltantes` y el código lo leyó como JSON (el caso j de P3b).
- **Costo:** USD 0,157948, con E1 0,087305 y E3 0,070643. Lo estimado era A, 0,0719, sin la escritura de los prefijos; mi estimación
  con reuso, 0,1555.

## Anexo (14:18:29 a 14:18:30)

- `--anexar` agregó 49 renglones en 8 archivos de `salida_r2b/{ext,docvig}/`. Los sha256 de antes y después están en
  `corrida/anexo_r0.json` y en la tabla del REPORTE §5.
- **Control** (`controles/r0_f2_control_anexo.json`): OK.
  - Cada archivo es su versión de HEAD más los renglones nuevos, todos de las 20.
  - Los otros 226 archivos de `salida_r2b/` no cambiaron.
  - La E0 de la tanda 0 sigue igual: 57 de 57.

## Selftest de claves, antes y después (sobre una copia posterior al anexo)

- **Antes, sin cambios:** veredicto FRENO. A3r da DISCREPANCIA solo por las 20 presentes; de eso salen el contraste y el veredicto.
  - Además, contra el JSON de HEAD, aparece en el contraste la fila F19d: entró a la tabla en `2374968a`, después del JSON
    (`604640c3`), y coincide.
  - En el perfil sellado, A3 sigue OK; su conteo informativo del namespace de E3 pasa de 7.698 a 7.721 por las filas de R0.
  - Ningún otro bloque da otra cosa.
- **Después, con A3r redefinido** (`regla_a3r`, más A3r_v1 y A3r_v2): veredicto OK.
  - A3r da OK: ausentes exactamente los 1.034 ítems que no son de R0, y presentes los no ítems y las 20.
  - A3r_v1 y A3r_v2 dan DISCREPANCIA.
  - Dos corridas dieron el mismo JSON byte a byte.
- **En el repo**, igual byte a byte a la copia: `mantenimiento/code/selftest_clave_cache.py` (`9cceae48…`),
  `mantenimiento/selftest_clave_cache.json` (`e11175ed…`) y la nota en `mantenimiento/tabla_reprocesamiento.md`. Los diffs están en el
  paquete.

## Enmienda 7, §1.5

- **Cola de la tanda 0 r2b:** de 74 a 69 de 2.439. Por estado, de 43, 29 y 2 a 42, 25 y 2. Salen 5 y no entra ninguna.
- **Población de L2:** de 2.366 a 2.371. Ítems de 1.003 a 1.008; no ítems, 1.363.
  - `ext::2.6.1.2`, de la muestra, cambió de última versión: las cifras de L2 se declaran medidas sobre el grafo sellado anterior.
- **Línea de base del pre-registro:** 74 de 2.439 (3,0 %) en r2b, y 69 de 2.439 (2,8 %) para el grafo re-sellado, cuyo ensamblado está
  pendiente.
- **Las notas en `docs/insumos_escritura.md` §7,** ítems 4 y 6, quedan PENDIENTES: no estaban entre mis escrituras.

## Errores propios

- **Clientes compartidos entre TOs.** `correr_r0.py` usa los mismos dos clientes para los dos TOs. Por eso, `corrida/estado_corpus.json`
  y `corrida/docvig/resumen_e3.json` cargan en docvig el gasto y las llamadas de ext. El gasto real es el del presupuesto compartido,
  y nada de lo anexado sale de esos archivos.
- **La foto de la fase 1 abrió los `.env`.** Esas fotos leyeron los 7 archivos de entorno para calcular su sha256, que quedó en el
  paquete `revision_R0`; ninguna salida muestra su contenido. La foto de la fase 2 los registra sin abrirlos.

## Foto, `.pyc`, convenciones y paquete

- **Foto del repo, sin `.git` y con los `.env` registrados solo por tamaño y fecha** (`controles/foto_repo_sin_env_R0.py`): antes,
  14:13:42, 50.453 archivos. La de después y la comparación van en el mensaje del FRENO, porque este archivo entra en la foto.
- **Los `-wal` y los `-shm` de las dos bases desaparecieron** con la corrida. SQLite, en modo WAL, los vuelca y los borra al cerrarse
  la última conexión. Los datos están en los `.db`, y las copias de los cuatro archivos están en los respaldos.
- **`.pyc`:** antes había 10.158, y 2.213 fuera de `.venv/`.
- **Grep de convenciones:** `controles/grep_convenciones_R0_fase2.txt`.
- **Paquete:** `revision_R0_fase2/`, con sus respaldos y su `manifest.txt`, y una copia permanente verificada. La ruta va en el mensaje
  del FRENO.

Nada commiteado y ningún mensaje de commit preparado. No escribí en la memoria ni en `.claude/`, y no usé esperas programadas.
