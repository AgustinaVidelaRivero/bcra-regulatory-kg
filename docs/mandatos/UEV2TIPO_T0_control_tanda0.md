FIRMADO por la autora — 2026-09-27

MANDATO — U-EV2-TIPO-T0: CONTROL DEL MODELO BAJO LA REGLA V2 SOBRE LAS 20
PREGUNTAS DE LA TANDA 0.
Sos una instancia ejecutora fresca en el repo bcra-regulatory-kg. Leé primero
CLAUDE.md; la fila U-EV2-TIPO de docs/plan_tesis.md con su CIERRE y sus
sub-ítems (regla v2 sellada, control V2b); el sub-ítem «B6.0 fase 2b» del
plan; scripts/ev2_tipo_control.py y scripts/ev2_tipo_control_v2.py
completos; y la hoja
data/experiment/ev2_tanda0/preguntas/tipo_pregunta_hoja_tanda0.csv (sha256
esperado e8a7fdfe767229045cf4d4cb81a27b85822d5ae6f5d3110c7445a72154cf56a0,
20 filas; mostrá shasum -a 256 y el conteo; si no coincide, FRENÁ).

Decisiones ya tomadas (no se re-deciden):
1. Los scripts sellados no se editan: ev2_tipo_control_v2.py tiene la hoja
   de EV2 y su sha cableados (:39-40, :69-70) y cargar_filas del v1 exige
   40 filas. Escribís scripts/ev2_tipo_control_tanda0.py, que importa del
   v1 armar_prompt, parsear, cargar_env, PRECIO_IN, PRECIO_OUT, MODELO,
   TEMPERATURE, MAX_TOKENS, y recibe por argumento --hoja, --sha-hoja,
   --regla, --sha-regla, --out-dir, --n (20) y --tope-usd. Misma lógica de
   llamada, mismo CachingClient, domain="control_tipo_tanda0",
   code_ver="control-tipo-tanda0+regla=<12 primeros del sha>",
   run_label="U-EV2-TIPO-T0", base de captura en
   <out-dir>/control_tipo_tanda0.db.
2. Regla: la v2,
   data/experiment/exploracion/ev2_fidelidad/regla_tipo_pregunta_v2.md
   (sha256 ef5c9aa692cb1e1b1de4c56c569864d16f190f52eb441fbdd94ebb7b978b5e0a,
   commit 41abf18). Modelo claude-sonnet-4-6, temperatura 0.0, sin thinking,
   max_tokens 1024, un reintento por pregunta, una sola corrida. Para las
   filas con dos anclas, el prompt lleva el texto de las dos tal como está
   en texto_ancla (la hoja ya los separa con =====); el material permitido
   de la regla es el mismo.
3. El control es CIEGO: no lee preguntas_tanda0.json (que trae
   tipo_previsto), ni validacion.json, ni el registro de generación, ni
   ninguna clasificación de la autora. Solo la hoja y la regla.
4. El JSON de salida lleva lo mismo que el de V2b (modelo_segun_api,
   temperatura, sha256_regla, sha256_hoja, reintentos, entradas con orden,
   id, tipo, nota, prompt) más tokens_entrada, tokens_salida,
   precios_usd_por_millon y costo_usd_calculado.
5. Tope de gasto: USD 1. Referencia: el control V2b costó USD 0,3981 por
   40 preguntas con la misma regla; 20 preguntas proyectan cerca de la
   mitad. Si --count proyecta más de USD 1, FRENÁ y preguntá.
6. Comparación, en un modo --comparar que corre DESPUÉS y por separado,
   cuando existan los dos insumos: (a) contra la clasificación de la
   autora, data/experiment/ev2_tanda0/preguntas/tipo_pregunta_autora_tanda0.csv
   (columnas orden,id,tipo,nota, la escribe la autora; sha que ella
   declare); (b) contra tipo_previsto de preguntas_tanda0.json (sha256
   b36e0662170004a5e1adfcf7ea26e91ba45a469dbbda058aac3a47f4c0cc3743).
   Salida <out-dir>/comparacion_tanda0.json con dos tablas pregunta por
   pregunta (modelo vs autora; modelo vs previsto) y una tercera autora vs
   previsto, acuerdo simple sobre 20 en cada una, y la lista de desacuerdos
   con id, orden, los tres tipos y la nota del modelo. No hay resultado
   esperado declarado: toda diferencia se reporta, nada se corrige, y la
   adjudicación es de la autora.

Tarea:
A. Escribí el script de la decisión 1. Corré --selfcheck (20 prompts, cada
   uno con la regla v2 completa más pregunta, anclas, criterios y texto del
   ancla; pegá el primero íntegro) y --count (salida a
   <out-dir>/count_tokens_tanda0.json; pegá total y cota). Subdirectorio:
   data/experiment/ev2_tanda0/preguntas/control_v2_tanda0_<fecha>/.
B. Si la cota no supera USD 1, corré --run --tope-usd 1. Reportá
   modelo_segun_api, temperatura, reintentos, sin_respuesta (esperado 0),
   tokens y costo_usd_calculado, y la distribución de tipos del modelo; NO
   reportes ni imprimas el tipo por pregunta hasta que la autora termine su
   clasificación (misma regla que TIPO-1b: la salida se sella y se compara
   después).
C. --comparar queda escrito y probado en seco con un CSV sintético de
   autora en tu scratchpad; se corre sobre el real solo cuando la autora lo
   indique.

Requisitos transversales: todo número contra su artefacto, con comando y
salida; lo que no encuentres, NO ENCONTRADO con el comando. Cero nombres
propios; los mentores solo por rol. Escritura autorizada: el script nuevo y
el subdirectorio de A; nada más. No modifiques la hoja, las preguntas, la
regla, los scripts sellados, docs/plan_tesis.md ni ningún archivo sellado.
No commitees. PYTHONDONTWRITEBYTECODE=1 en todo Python; corré con
.venv/bin/python. Paquete de revisión revision_UEV2TIPO_T0/ en tu
scratchpad con manifest.txt.

Criterios de aceptación, con salida en el reporte: sha de la hoja y de la
regla iguales a los esperados; sha256_hoja y sha256_regla dentro del JSON
iguales a esos; sin_respuesta = 0; costo_usd_calculado ≤ 1; distribución de
tipos del modelo sin detalle por pregunta; --comparar probado en seco; git
status --short con solo el script y el subdirectorio como nuevos, más
adjudicar.py y data/experiment/reextraccion_v2/corpus_tanda0/ (de otra
unidad en curso); grep de convenciones sobre el script y el JSON, pegado
aunque dé vacío.

Al terminar, reportá rutas, sha256 de cada archivo nuevo, id de modelo,
temperatura, costo real y la distribución, y frená.
