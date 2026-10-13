# FRENO de R0, fase 1 (13/10/2026; USD 0, sin API, sin commit)

## Paso 0 (16:49:51 −03)

```
$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg
6556de22 Segmentacion oficial: registro de la primera pasada de la adjudicacion, armada
cc6b0cd6c56831c486d60bf7da64712cea391a1eb2948eef822448567df9bab6  data/experiment/e3_listas/o3/lista_unidades_afectadas_tanda0.json
a287c7479939bab8667131c1c9a59cadd61f129a8bb9e0eeed8c2e1567c082a6  data/experiment/reextraccion_v2/corpus_v2/runner_corpus.py
e7b4b164f0062f2d501e854d6e7582e6d35d69ee7f87d13abe86b6b9c673ec10  data/experiment/reextraccion_v2/e3_verificador/cliente_e3.py
```

`git status` no mostró nada en las dos carpetas. Todo dio lo esperado.

## Resultado

El detalle y la evidencia están en `REPORTE_R0_fase1.md` y en `controles/`. Todo corrió sobre una copia del repo sin enlaces.

- **Reparto de las 20, por script, con el código del pipeline:** el de la enmienda 7, §1.2.
  - 16 se aceptan con el intento 0: 11 completas y 5 con residuales; de ellas, 11 habían reintentado y 5 estaban en la cola.
  - Reintentan `ext::3.6.4.1`, `ext::3.16.2.1` y `ext::3.18.1.1`.
  - `docvig::3.3.2` vuelve a la cola.
  - Por TO: ext 19 y docvig 1.
  - La evaluación de O3 se reproduce en 20 de 20, y el E1 del intento 0 está en la caché de E1 en 20 de 20, con la respuesta guardada.
- **a. La clave:** la que arma el runner es la de O3 en 20 de 20, con el namespace y el pedido canónico iguales byte a byte. Ninguna
  está en la base de E3 del pipeline.
- **b. La base:** propongo cuatro caminos, todos implementados y probados en seco. Recomiendo b1.
  - b1, sembrar las 20 filas de O3 en la base del pipeline: USD 0 por las 20, y se redefine A3r.
  - b2, sembrarlas en una base propia de R0: USD 0, y no toca las bases del pipeline.
  - b3, leerlas como respuesta desde la base de O3.
  - b4, no reusarlas: USD 0,2382 más, y el reparto puede cambiar.
- **c. Dónde escribe:** R0 corre siempre en su carpeta (`r0/corrida/`). Recomiendo c1.
  - c1: anexa sus renglones a `salida_r2b/{ext,docvig}/` (`--anexar`, enmienda 5, §1.3), y controla que cada archivo quede igual a
    su versión anterior más lo nuevo.
  - c2: la carpeta se sella como la copia y se anexa en el re-sellado.
- **Script:** `correr_r0.py`.
  - Importa el runner y corre `runner_corpus.fase_e3` sobre una carpeta con el E1 de las 20.
  - Los clientes son los reales, con el tope compartido (`--tope` obligatorio, hasta 1,50).
  - Una guardia controla, antes de cada llamada, el prefijo y el sha256 del mensaje contra los sellados en `esperados_r0.json`
    (`81598c97…`), y después de cada respuesta, el id del modelo.
  - Pide además `--reuso-o3` (la pregunta b).
- **Corrida en seco:** pasan 11 de 11 escenarios (aceptar, reintentar, cola, tope, reanudación, error de la API transitorio y
  persistente, respuesta mal formada, modelo distinto y mensaje distinto), con el anexo y su rechazo. Durante la corrida no cambiaron
  ni el repo ni las bases de la copia.
- **Costo** (USD; tarifas de la enmienda 7, §1.4, recomputadas desde sus fuentes):
  - A, 0,0719; B, 0,3102; C, 0,7179; C sin la caché de E1, 0,9196.
  - Mi estimación con reuso, contando la escritura de los dos prefijos: 0,1555; sin reuso, 0,3937.
  - Todo, debajo del tope de 1,50.

## Errores propios

- El `rsync` de la copia (con las exclusiones de S0-6b) copió 6 `.env` al scratchpad. Los borré sin abrirlos, a las 16:54:12.
- La primera cuenta de la tarifa de E1 leía resúmenes por TO que, en las fases reabiertas, cuentan solo el último proceso. La corregí
  antes de escribir cifras.

## Para la fase 2

- **El «seguí» de la autora.**
- **Sus decisiones sobre b y c.**
- **Las escrituras que dependen de b y el mandato no enumera:** la base de E3 y la de reintentos de E1, y `logs/cache_usage.jsonl`.
- **El camino de A3r:** propongo un control de R0 sin editar el selftest; si no, una autorización para editarlo.
- **La consulta de deprecaciones.**

## Foto, `.pyc`, convenciones y paquete

- **Foto sha256 del repo entero, sin `.git` y sin otra exclusión** (`segmentacion_oficial_e0r2/s0_6/bis/scripts/foto_repo_entero_S0-6a-bis.py`):
  la tomé antes, a las 16:50:13, con 50.441 archivos. Este FRENO entra en la foto, así que la de después y su comparación van en el
  mensaje del FRENO.
- **`.pyc`:** antes había 10.158, y 2.213 fuera de `.venv/`. Todo corrió con `-B` y `PYTHONDONTWRITEBYTECODE=1`.
- **Grep de convenciones:** `controles/grep_convenciones_R0_fase1.txt`.
- **Paquete:** `revision_R0/` en el scratchpad, con su `manifest.txt`, y su copia permanente en `fuera_del_repo/scratchpads/`. La ruta
  y la verificación van en el mensaje del FRENO.

Nada commiteado y ningún mensaje de commit preparado. No escribí en la memoria ni en `.claude/`, y no usé esperas programadas.
