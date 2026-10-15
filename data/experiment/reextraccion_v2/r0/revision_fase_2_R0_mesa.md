# R0, fase 2: revisión de la mesa (14/10/2026)

La ejecutora corrió la fase 2 en la sesión `29a33b36…`, con el «seguí» `d793664a…` (139 renglones), de 14:11 a 14:30 del 14/10/2026.
Gastó USD 0,157948 de un tope de 1,50 y quedó en FRENO. Esta nota revisa ese FRENO.

## El paquete

`revision_R0_fase2/`, fuera del repo, con copia permanente en `fuera_del_repo/scratchpads/29a33b36…/`:
- 67 archivos, todos con el sha256 de su `manifest.txt`;
- ninguno sin listar, y ningún listado que falte;
- ningún `.env`, buscado por nombre.

## Lo que dejó en el repo

- **`reextraccion_v2/r0/`:** 32 archivos nuevos, todos con un sha256 que está en el manifest del paquete. No hay `.pyc` ni
  `__pycache__`, y ninguno cae en `.gitignore`.
- **`salida_r2b/`:** 8 archivos cambiados, 5 de `ext/` y 3 de `docvig/`.
  - Cada uno es su versión de HEAD más los renglones nuevos, byte a byte, y los sha256 de antes y después son los de
    `r0/corrida/anexo_r0.json`.
  - Son 49 renglones, todos de las 20 unidades de `r0/esperados_r0.json`, y son los mismos de `r0/corrida/`.
  - Ningún otro archivo rastreado de `salida_r2b/` cambia.
  - Control propio de la mesa, fuera del repo: `control_anexo_mesa.py`.
- **`mantenimiento/`:**
  - el selftest de claves y su JSON, con el sha256 del paquete;
  - la nota en `tabla_reprocesamiento.md`, que solo agrega 12 renglones.
- **Fuera de git, dentro del repo:**
  - las dos bases de `e3_verificador/cache/`, abiertas por la mesa de solo lectura sobre una copia, contra los respaldos del paquete:
    - `e3_verificacion.db`: 23 filas nuevas en `cache`, todas `claude-sonnet-5`;
    - `e1_reintentos.db`: 3 filas nuevas, todas `claude-haiku-4-5-20251001`;
    - en las dos, 0 filas de antes que falten o cambien;
  - `logs/cache_usage.jsonl`: es su respaldo más 6 renglones.
- **El resto del repo:** la foto de la mesa, sin `.git` y con los `.env` registrados solo por su tamaño y su fecha, cambió solo en lo de
  arriba entre las 14:11 y las 14:36. Los `.env` no cambiaron.

## La sesión

Revisada en su registro, por script, desde el mensaje del «seguí»:
- **Herramientas:** 51 llamadas a Bash, 6 a Write y 1 a Edit. Ninguna a Read.
- **Escrituras con Write y Edit:** en `r0/`, el FRENO, el REPORTE y tres scripts de control; en su scratchpad, el script de la foto.
  Nada en la memoria ni en `.claude/`.
- **Corridas:** `correr_r0.py --correr` una sola vez (14:14:31) y `--anexar` una vez (14:18:29). Las otras menciones de `--correr`
  son texto de su checkpoint.
- **Esperas:** ningún `sleep` ni espera programada.
- **Carpetas vedadas:** ninguna mencionada.
- **Los `.env`:** aparecen solo como exclusiones de `rsync`, patrones de `find` y texto del FRENO, del REPORTE y del checkpoint.
  Ningún comando los abre.
- **Patrones de clave en el registro entero:** 0.

## El resultado, reproducido por la mesa

- **Los dos selftests de claves,** corridos por la mesa sobre una copia del repo sin `.env` ni enlaces:
  - el de HEAD, sin la redefinición, da FRENO: A3r da DISCREPANCIA solo porque están las 20 (1.034 ausentes y ningún no ítem
    ausente). Su JSON es, byte a byte, el del paquete (`selftest_clave_cache_sin_redefinir_post_anexo_R0_fase2.json`);
  - el redefinido da OK, y su JSON es, byte a byte, `mantenimiento/selftest_clave_cache.json` (`e11175ed…`).
- **La regla nueva de A3r** (`regla_a3r`) es la del «seguí»:
  - las ausentes, exactamente, los ítems que no son de R0;
  - presentes, los no ítems y las 20 de `verificacion` de `r0/esperados_r0.json`, controlado por su sha256;
  - dos variaciones de control que tienen que dar DISCREPANCIA.
- **El costo,** recalculado llamada por llamada desde `r0/corrida/registro_llamadas_r0.jsonl` con los precios de
  `corpus_v2/runner_corpus.py:92-96`:
  - USD 0,157948, en 6 llamadas a la API, todas de ext: E1 3 y 0,087305, y E3 3 y 0,070643;
  - docvig no hizo ninguna llamada;
  - coincide con `presupuesto_r0.json` y con el campo de cada renglón (diferencia máxima, 5·10⁻⁷).
- **Las cifras de la enmienda 7, §1.5,** recalculadas desde `finales.jsonl`, última versión por unidad, en HEAD y ahora:
  - **la cola:** de 74 a 69, por estado 43, 29 y 2 a 42, 25 y 2;
  - **salen:** `ext::2.6.1.1`, `ext::3.13.1.10`, `ext::3.5.6.1`, `ext::3.6.1.1` y `ext::3.6.4.2`, y no entra ninguna;
  - **las aceptadas:** de 2.366 a 2.371;
  - **el denominador:** `finales.jsonl` trae 2.440 entradas para las 2.439 unidades de la E0 de la tanda 0, porque `cap::4.2.1.2`
    va en dos partes por corte. El denominador sellado, 2.439, es el de las unidades (`reext_t0/t5/cifras_t5.py:35`).
- **La muestra de L2:** de sus 60 unidades (`lectura_aceptadas/sellos_l0.json`, `sorteo.muestra`), una sola está entre las 20 de R0,
  `ext::2.6.1.2`. Su última versión pasa de `aceptado_tras_reintento` a `completo_ok_directo`.

## Lo que pidió la autora, punto por punto

- **a. El gasto que `corrida/estado_corpus.json` y `corrida/docvig/resumen_e3.json` le cargan a docvig.** Propongo declararlo y no
  corregir esos dos archivos:
  - son salidas de la corrida, con su sha256 en el FRENO y en el paquete;
  - nada de lo anexado sale de ellos, y ningún script fuera de `r0/` los lee;
  - el reparto real es el de arriba: ext 0,157948 y docvig 0.
  - El origen está en `correr_r0.py`, que usa los mismos dos clientes para los dos TOs; el runner del corpus arma clientes nuevos por TO.
    R0 corre una sola vez, así que no hace falta cambiar el script.
- **b. `ext::3.18.1.1`.** Es lo previsto. La re-verificación de R0 trajo el veredicto entero como texto dentro de `faltantes`, y el
  código lo leyó con `leer_faltantes_texto` (`e3_verificador/ratchet_e3.py:156-176`, «P3b, j»), por `json.loads`
  (`lectura_faltantes: json`).
  - **Es un camino frecuente:** en los veredictos de HEAD de la tanda 0, 86 de 2.685 se leyeron así.
  - **El resultado no cambia:**
    - la re-verificación de R0 da 1 faltante, 0 utilizables, 1 bloqueante y no aceptable, lo mismo que la re-verificación de la
      tanda 0;
    - el estado final es `cola_humana` con 1 reintento, en la tanda 0 y en R0.
  - **El `veredicto: null` del control** sale de que el resumen lee el campo de arriba, no el de adentro del texto.
- **c. Las fotos de la fase 1.** Calcularon el sha256 de los 7 archivos de entorno del repo: los 6 `.env` y el `.env.example`.
  - Esos sha256 están en las fotos del paquete `revision_R0` y en su copia permanente.
  - Ninguna salida muestra el contenido de esos archivos.
  - La clave que tenían entonces está revocada desde el 13/10/2026.
  - La foto de la fase 2 los registra sin abrirlos. Las fotos de la mesa, hasta el cierre del §96, también les calcularon el sha256;
    está declarado en el §97 de su hoja de ruta.
- **d. `ext::2.6.1.2`.** Lo registro:
  - está en la muestra de 60 de L2 y la lectura la juzgó sobre su reintento;
  - después de R0, su última versión es el intento 0, `completo_ok_directo`;
  - por la enmienda 7, §1.5, las cifras de L2 quedan como medidas sobre el grafo sellado anterior (nota en `docs/insumos_escritura.md`
    §7, ítem 4).
- **e. Las notas de `docs/insumos_escritura.md` §7, ítems 4 y 6.** Las preparé y entran con este registro.

## Para el pre-registro de la tanda 1

La línea de base de la cola tiene dos cifras, como manda la enmienda 7, §1.5:
- 74 de 2.439 (3,0 %), medida en r2b;
- 69 de 2.439 (2,8 %), para el grafo re-sellado, cuyo ensamblado todavía no corrió.

La línea va en el borrador del pre-registro, PENDIENTE de la autora.

## Aprobación de la autora (15/10/2026)

Recibida a las 11:18:20 (hoja de ruta de la mesa, §100), tal cual: «de la revisión de R0: el punto a se declara, sin corregir los dos
archivos; los puntos b a e, como los dejaste».
- **a.** Queda declarado. `corrida/estado_corpus.json` y `corrida/docvig/resumen_e3.json` no se corrigen. El gasto real de la fase 2 es
  USD 0,157948, todo de ext.
- **b a e:** quedan como están arriba.
- **El pre-registro de la tanda 1:** la autora aprobó la v7 del borrador, con la línea de base de la cola: 74 y 69 de 2.439.
