**[06/10/2026]** Re-redactado como U-COMP-E1, la comparación chica antes de la tanda 1 (`docs/mandatos/UCOMP_E1_comparacion_chica_modelo.md`), por decisión de la autora del 06/10/2026, con tope de USD 25; este borrador queda como base histórica.

POSTERGADO: experimento posterior al escalado (decisión de la autora del 05/10/2026). BORRADOR, sin firmar.
- No se ejecuta ahora y no decide el modelo de E1 de la release r2b, que es `claude-haiku-4-5` con
  temperatura 0 (docs/plan_tesis.md:400).
- Pasa a ser un experimento de la tesis: compara Haiku 4.5 con modelos más grandes, por la API, sobre una
  muestra, para reportar cuánto cambiaría el grafo y a qué costo (docs/plan_tesis.md:778).
- Su mandato se re-redacta en ese momento. El texto de abajo es el borrador del 05/10/2026 y queda como
  base: su plazo («antes de U-REEXT-T0»), la pausa de la plataforma y el criterio para elegir el modelo de
  la release ya no rigen.

MANDATO — U-PROMPT-R2, ETAPA P6: EXPLORACIÓN PARA ELEGIR EL MODELO DE E1.
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar, y docs/decisiones_caching_extraccion.md antes de
tocar cualquier llamada al modelo: sus cinco decisiones son vinculantes.
- Una etapa, con un control previo sin gasto (P6.0) y un FRENO al final: reporte corto (no más de 40 líneas)
  y espera del «seguí» de la autora.
- Costo: tope de USD 25 (decisión 1 al firmar), con freno duro. Todas las llamadas van a la API de
  Anthropic. Ninguna llamada a Amazon Bedrock ni a AWS.
- No elige el modelo. Mide, aplica el criterio firmado y reporta; la elección es de la autora.
- PRECONDICIONES. Si falta alguna, frená sin gastar.
  - P5 de U-PROMPT-R2 commiteada (`53b7708`), con sus salidas en data/experiment/prompt_r2/p5/salida/.
  - Este mandato firmado, con su criterio y sus decisiones.
  - La clave de la API en data/experiment/evaluacion/.env. No va al repo, a un reporte ni a un log.
- PLAZO: antes de U-REEXT-T0. La plataforma de la extracción (la API o Amazon Bedrock) y el mandato de
  U-PLATAFORMA quedan en pausa hasta el resultado de esta etapa (decisión de la autora del 05/10/2026).

CONTEXTO, con sus anclas.
- Por qué. Con el prefijo de P3c y temperatura 0, `claude-haiku-4-5` no cumple las reglas de los grupos b
  en ninguna de las dos corridas de P5: 0 de 3 en b1, 0 de 3 en b2 y 0 de 2 en los encabezados. En c
  cumple 1 de 4, y en a, 1 de 3. Sumando a, a_transicion, b1, b2, los encabezados y c: 3 de 16 en la
  corrida A y 2 de 16 en la B. El ejemplo sale completo en las dos (2 de 2). E3 da veredicto completo en 6
  de las 10 unidades que verificó (data/experiment/prompt_r2/p5/salida/marcas_p5.json y resultados_p5.jsonl).
- El pedido de E1 del perfil r2b: `temperature` 0, `tool_choice` forzado a `extraer_kg_e1`, sin `thinking`,
  `max_tokens` 8.192 en el primer intento (`e1_extractor/prompt_r2b.py:109-110`, `:440-450`; el modelo, en
  `corpus_v2/runner_corpus.py:89`; el techo, en la fila F08 de la tabla de reprocesamiento).
- Documentación oficial, consultada el 05/10/2026. Los tres modelos nuevos NO aceptan ese pedido tal cual.
  - `tool_choice` forzado: `{"type": "tool"}` y `{"type": "any"}` devuelven un error 400 en los tres. Solo
    aceptan `auto` y `none`. Para que el modelo llame a la herramienta, la documentación indica decirlo en
    el prompt; para un JSON que cumpla el schema, `strict: true` o salidas estructuradas
    (https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5,
    …/models/opus-5-5/whats-new-opus-5-5 y …/models/fable-5-1/whats-new-fable-5-1).
  - `temperature`: un valor distinto del de por defecto devuelve un error 400 en los tres (las mismas
    páginas y …/models/sonnet-5-5/overview).
  - `thinking`: en `claude-opus-5-5` y `claude-fable-5-1` el pensamiento adaptativo está siempre encendido;
    `disabled` devuelve un error 400. Su profundidad se regula con `output_config.effort` (`low`, `medium`,
    `high`, `xhigh`, `max`; por defecto, `medium` en Opus 5.5 y `high` en Fable 5.1). En
    `claude-sonnet-5-5` lo más bajo es `thinking: {"type": "between_tools"}`, que apaga el pensamiento
    previo; `disabled` devuelve un error 400. El pensamiento se cobra como salida y cuenta contra
    `max_tokens`. El `effort` regula toda la respuesta, no solo el pensamiento
    (https://platform.claude.com/docs/en/build-with-claude/effort).
  - Tokenizador: los tres usan el de los modelos desde Opus 4.7, que da cerca de un 30 % más de tokens por
    el mismo texto que `claude-haiku-4-5`. El conteo de tokens es gratis, es una estimación, cuenta con el
    tokenizador del modelo que se le pasa y valida `tool_choice` igual que el pedido
    (https://platform.claude.com/docs/en/build-with-claude/token-counting).
  - Precios por millón de tokens (entrada, salida, escritura de caché de 5 minutos, lectura de caché), de
    la página de cada modelo: Haiku 4.5, USD 1, 5, 1,25 y 0,10; Sonnet 5.5, 2, 10, 2,50 y 0,20; Opus 5.5,
    4, 20, 5 y 0,20; Fable 5.1, 10, 50, 12,50 y 0,25. El mínimo para la caché es de 512 tokens en los tres.
  - Fable 5.1 puede devolver `stop_reason: "refusal"` por sus clasificadores (…/whats-new-fable-5-1).
  - Límites: por nivel de uso de la cuenta, con un tope de gasto mensual (USD 500 en el nivel Start y
    1.000 en Build) y límites por minuto por modelo; los de la cuenta se ven en la consola y en los
    encabezados `anthropic-ratelimit-*` de cada respuesta (https://platform.claude.com/docs/en/api/rate-limits).
  - Bedrock: los cuatro modelos tienen id en la integración nueva. Haiku 4.5 y Fable 5.1 están abiertos a
    toda cuenta; Sonnet 5.5 y Opus 5.5 dependen de un criterio de acceso que se ve en la consola de AWS.
    Esa integración no admite salidas estructuradas
    (https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock).
- Consecuencia. Cada brazo nuevo corre con un pedido adaptado, y lo que se compara es un modelo con su
  pedido, no el modelo solo. Es la comparación que sirve para decidir: si se elige un modelo nuevo, su
  pedido en producción será el adaptado.
- El SDK del repo es anthropic 0.100.0 (`requirements.txt:11`). No se actualiza en esta etapa.

BRAZOS. En todos: el prefijo de P3c (`322c5a23e9b7`) con su punto de caché, el mismo mensaje por unidad, el
mismo tool schema (sin `strict`), las 27 unidades selladas de P4b (data/experiment/prompt_r2/p5/salida/
seleccion_p5.json, que lleva el sha256 de la selección de P4b) y la e0 de C2
(`e0_chunking/salida_tanda0_r2b/`). El código es el del commit vigente al despacho; el pedido lo arma el
perfil r2b y el script de la etapa cambia solo lo que dice esta tabla.

| Brazo | Modelo | Qué cambia del pedido de E1 | Corridas |
|---|---|---|---|
| H | `claude-haiku-4-5` | nada | las dos de P5, sin pagarlas de nuevo |
| S | `claude-sonnet-5-5` | sin `temperature`; `tool_choice` `auto`; `thinking` `between_tools`; `max_tokens` 16.384 | 2 |
| O | `claude-opus-5-5` | sin `temperature`; `tool_choice` `auto`; `output_config.effort` `low`; `max_tokens` 16.384 | 2 |
| F | `claude-fable-5-1` | lo mismo que O | 2 |

- «El thinking, como en el pedido real de E1» quiere decir sin pensamiento. Sonnet 5.5 lo admite con
  `between_tools`, con el `effort` por defecto. Opus 5.5 y Fable 5.1 no lo admiten: van con `effort` `low`,
  lo más cercano, que además acorta la respuesta (decisión 2 al firmar).
- `max_tokens` de 16.384 en el primer intento, porque el pensamiento cuenta contra el techo y el
  tokenizador nuevo da más tokens. Si corta, un reintento a 40.960 con transmisión. Cada corte se registra.
- Respuesta sin llamada a la herramienta, o con una entrada mal formada: un solo reintento con el mismo
  pedido, en un namespace aparte. Se registran las dos respuestas. Un `refusal` no se reintenta.
- Cada corrida, en su base propia, como en P5. Todo en serie. Las bases de P6 no se reutilizan en ninguna
  corrida del pipeline.
- Si el SDK instalado no tiene un campo (`output_config`, `between_tools`), va por `extra_body`. Si no se
  puede enviar, frenás.

QUÉ HACE.
P6.0 — Control previo, USD 0. Si algo falla, frenás y reportás sin gastar.
  a. Con el perfil r2b del commit vigente, las claves de E1 de las 27 unidades son las de
     data/experiment/prompt_r2/p5/salida/claves_despues.json: el brazo H es el mismo pedido.
  b. Los tres modelos nuevos están disponibles para la cuenta: la lista de modelos de la API y un conteo de
     tokens por modelo. El conteo lleva el pedido adaptado; si lo rechaza, se guarda el error tal cual.
  c. El conteo de tokens, por modelo: el prefijo y la entrada de cada una de las 27 unidades, contra los de
     Haiku (27.840 de prefijo; 38.421 de entrada entre las 27).
  d. Una prueba con un cliente simulado: la capa de caché guarda y devuelve una respuesta que trae bloques
     `thinking` además del `tool_use`. La capa de caché es zona sellada: si no puede, frenás.
  e. Las reglas de marcado y de medición, en un archivo (`p6/reglas_p6.md`), antes de la primera llamada
     paga: las de P4b y P5 sin cambios (`p4b/marcas_p4b.py`, `p4b/analisis_p4b.py`, `p5/marcas_p5.py`,
     `p5/analisis_p5.py`), la definición de «umbral con tramo verificado» sobre los campos del validador
     (`umbrales_tramos`), y el criterio de este mandato copiado tal cual. Su sha256 y su hora quedan en un
     archivo de sello.
  f. La proyección del gasto con los tokens de c y los precios del contexto. Si pasa el tope, frenás.
P6.1 — E1 de los brazos S, O y F: dos corridas de 27 unidades cada uno. De cada respuesta se guarda la
  entrada de la herramienta, el `stop_reason`, el `usage` completo (con el pensamiento, si lo separa), los
  segundos de la llamada y, de la primera de cada modelo, los encabezados de límites. Después de las 3
  primeras unidades de la corrida A de cada brazo, re-proyectás su gasto con lo medido; si el total de la
  etapa pasa el tope, frenás antes de seguir.
P6.2 — E3 sobre cada brazo y cada corrida: la primera verificación, sin el ciclo de reintentos, como en P5
  (`cliente_e3.verificar_chunk` y `ratchet_e3.evaluar_veredicto`), con `claude-sonnet-5` por la API y su
  pedido sin cambios. Son 216 verificaciones (4 brazos, 2 corridas, 27 unidades) menos las 10 de la corrida
  A de Haiku que P5 ya pagó (su corrida `e3a`): 206 nuevas. Una unidad sin salida de E1 no se verifica.
P6.3 — Mediciones, por brazo y por corrida, con `p6/reglas_p6.md`:
  a. Viabilidad: pedidos aceptados; unidades con llamada a la herramienta al primer intento, con el
     reintento o sin ella; cortes; `refusal`; rechazos del validador por motivo y correcciones.
  b. Los grupos a a f y el ejemplo, por la lectura cegada de P6.4.
  c. Las omisiones `meta_normativo` y el contador por clase; las menciones de sujeto que verifican; las
     normas con relación de sujeto; los umbrales con tramo verificado; `cap::tabla037`.
  d. E3: unidades con veredicto completo y aceptable, faltantes por severidad y bloqueantes.
  e. La variación entre las dos corridas de cada brazo: respuestas idénticas, y marcas que cambian.
  f. Costo y tiempo: tokens de entrada, de salida y de pensamiento por unidad; salida por carácter de texto
     propio; costo de E1 por unidad; segundos por unidad (en Haiku, P5 no los midió: se aproximan con las
     horas de sus registros, y se declara); los límites de la cuenta por modelo.
  g. Proyección, por modelo, del costo de U-REEXT-T0 y de la extracción completa (las tandas 1 a 3: 8.653
     unidades más), con el método de `p5/proyeccion_p5.py`, ponderada por estrato y sin ponderar, y E3 en
     la API.
  h. De la documentación, con su dirección y su fecha: la disponibilidad de cada modelo en Bedrock y su
     calendario de retiro. Si los créditos de AWS cubren a cada modelo queda NO VERIFICADA: se comprueba
     en la página de créditos después de una primera llamada, que esta etapa no hace.
P6.4 — Lectura cegada. Una ficha por unidad, brazo y corrida (216), con un código, sin el brazo, el modelo,
  la corrida, el `usage`, el pensamiento ni los tiempos, en el orden de una semilla declarada. La clave de
  los códigos queda en un archivo que no se abre hasta sellar las marcas con su sha256. La lectura la hace
  una instancia que recibe solo las fichas y las reglas; si no se puede, la hace la instancia de la unidad
  sin abrir la clave ni los resultados por brazo, y lo declara. Las fichas de Haiku se marcan de nuevo, a
  ciegas; se reporta cuántas de sus 54 marcas coinciden con las de P5. La lectura es asistida; la revisa la
  autora.
P6.5 — El criterio, aplicado tal cual, con su tabla.

CRITERIO DE ELECCIÓN. Lo firma la autora; no se cambia después de la primera llamada paga.
1. Viabilidad. Un brazo queda afuera si la API rechaza su pedido, si en alguna corrida más de 1 de las 27
   unidades queda sin una salida bien formada después del reintento, o si alguna respuesta es un `refusal`.
2. Tres familias, con un valor por corrida:
   - el ejemplo: completo o no (en `cla::5.1.1::intro`, la Definicion de alcance; en `cla::5.1.1.1`, la
     Excepcion, la Operacion de clasificar y una Condicion por cada condición);
   - las reglas que fallaron: unidades que cumplen sobre las que aplican, sumando los grupos a,
     a_transicion, b1, b2, los encabezados de b y c (16 unidades);
   - E3: unidades con veredicto completo en la primera verificación, sobre 27.
3. «Claramente peor». En una familia, un brazo es claramente peor que el mejor (el de mayor promedio de sus
   dos corridas) si sus dos corridas quedan por debajo de las dos del mejor y, además, la diferencia entre
   los promedios supera la mayor diferencia entre las dos corridas de un mismo brazo, tomada entre los
   cuatro. En el ejemplo: incompleto en las dos corridas, con el mejor completo en las dos.
4. Elección: entre los brazos viables que no son claramente peores que el mejor en ninguna familia, el de
   menor costo de E1 por unidad, medido.
5. Techo: si la extracción completa con el brazo elegido proyecta más que el techo de la decisión 3, el
   criterio no elige y decide la autora.
6. Las demás mediciones se reportan y no entran al criterio.
7. Límites que se declaran con el resultado:
   - con 27 unidades y dos corridas, una diferencia chica no se distingue de la variación, y en la duda el
     criterio se queda con el más barato;
   - el prefijo y las reglas de marcado se ajustaron mirando salidas de Haiku, y los calibradores de E3
     salen de extracciones de Haiku;
   - E3 es `claude-sonnet-5`, de la familia de uno de los brazos;
   - cada brazo nuevo se mide con una sola configuración de pensamiento.

FRENO final (`data/experiment/prompt_r2/freno_p6.md`): el control previo; la tabla de viabilidad; las tres
familias por brazo y corrida, y el resultado del criterio; las demás mediciones; el costo real contra el
tope; la proyección por modelo; Bedrock y retiro por modelo; los límites del punto 7; y, para cada brazo
distinto de H que el criterio deje en pie, lo que habría que cambiar y volver a validar antes de
U-REEXT-T0 (el pedido de E1 y sus techos, la temperatura, la fila del modelo en la tabla de
reprocesamiento, el censo de unidades grandes con el tokenizador nuevo, y una pasada de E3 y del ratchet).

ESCRITURAS: data/experiment/prompt_r2/p6/ (se crea: los scripts de la etapa, `reglas_p6.md` y `salida/`),
data/experiment/prompt_r2/freno_p6.md y el scratchpad. Si hace falta otro archivo, frenás antes de tocarlo.
PROHIBIDO: tocar el código del pipeline (data/experiment/reextraccion_v2/), el prefijo, el mensaje, el tool
schema, las constantes de temperatura, un candado, la tabla de reprocesamiento, los manifiestos,
`requirements.txt` o cualquier zona sellada; actualizar el SDK; llamar a Bedrock o a AWS; correr un brazo
o una corrida que no esté en la tabla; cambiar las reglas o el criterio después de la primera llamada paga;
elegir el modelo; escribir la clave en un archivo; commitear.

CRITERIO DE ACEPTACIÓN. El control previo completo y anterior a la primera llamada paga, con el sello de
las reglas. Los tres brazos nuevos con sus dos corridas, o el error de la API guardado tal cual. E3 sobre
toda unidad con salida. Las marcas selladas antes de abrir la clave. Cada cifra del freno, recomputada
contra su archivo. El gasto, bajo el tope.

DECISIONES DE LA AUTORA AL FIRMAR.
1. El tope (propuesta: USD 25; la proyección previa da 14,77 sin pensamiento y 20,15 con un pensamiento
   de la mitad de la salida; con el `effort` por defecto en Opus 5.5 y Fable 5.1, hasta 33,77).
2. El pensamiento de Opus 5.5 y Fable 5.1 (propuesta: `effort` `low`; la alternativa es el de por defecto,
   que piensa más y cuesta más).
3. El techo de costo de la extracción completa para el punto 5 del criterio (lo fija la autora).
4. El criterio de elección, como está escrito arriba.
5. Las fichas de Haiku se marcan de nuevo, a ciegas (propuesta: sí).
6. Los brazos son los cuatro de la tabla (propuesta: no agregar ninguno).

REQUISITOS: los de CLAUDE.md §4 (a a l), con PYTHONDONTWRITEBYTECODE=1 y .venv/bin/python -B; la corrida,
los selftests y los controles sobre una copia sin enlaces, con el sha256 de los archivos del repo antes y
después; decisiones de caching 1 a 5 (el gasto, por los clientes, con los precios de cada modelo; cada
respuesta real con su línea de usage); todo conteo recomputado contra su artefacto; cada dato de la
documentación, con su dirección y su fecha de consulta, o marcado NO VERIFICADA; cero nombres de personas;
paquete de revisión con manifest.
