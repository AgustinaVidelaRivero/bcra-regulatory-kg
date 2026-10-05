ARCHIVADO el 05/10/2026, sin firmar y sin ejecutar: la extracción corre por la API (docs/plan_tesis.md:400)

MANDATO — U-PLATAFORMA: ADAPTADOR DE AMAZON BEDROCK PARA LA EXTRACCIÓN (E1 Y E3) DE LA RELEASE r2b.
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar, y docs/decisiones_caching_extraccion.md antes de
tocar cualquier llamada al modelo: sus cinco decisiones son vinculantes.
- Una etapa, con FRENO al final: reporte corto (no más de 40 líneas) y espera del «seguí» de la autora.
- Costo: USD 0, salvo dos llamadas mínimas por Bedrock, una a cada modelo, con tope de USD 0,10 entre las
  dos. Ninguna llamada a la API de Anthropic y ninguna extracción.
- PRECONDICIONES. Si falta alguna, frená sin escribir.
  - P5 de U-PROMPT-R2 commiteada (`53b7708`).
  - Para las dos llamadas: el acceso a los modelos de Anthropic habilitado en la cuenta de AWS (el formulario
    de primer uso es una acción de la autora, PENDIENTE al 05/10/2026) y las credenciales de AWS en el entorno
    de la corrida. Las credenciales no van al repo, a un reporte ni a un log.
- PLAZO: antes de U-REEXT-T0.

CONTEXTO, con sus anclas.
- Decisión de la autora del 05/10/2026: toda la extracción de la release r2b corre por Amazon Bedrock,
  empezando por U-REEXT-T0. La evaluación (agente y jueces) sigue en la API. No se mezclan plataformas en la
  extracción. Hoy no hay ninguna clave de r2b pagada: el cambio no obliga a reprocesar nada.
- Cómo está hoy.
  - E1 y E3 crean el cliente de la API (`e1_extractor/cliente_e1.py:207`; `e3_verificador/cliente_e3.py:134`).
  - Los ids de modelo y los precios están en el runner: `claude-haiku-4-5` y `claude-sonnet-5`, con los
    precios de la API (`corpus_v2/runner_corpus.py:89-94`). El id va en el pedido, y por eso en la clave.
  - El namespace de la caché no nombra la plataforma (`cliente_e1.py:118-139`; `cliente_e3.py:55-62`). El
    reintento por salida mal formada usa un sufijo, `-rforma1` (`cliente_e1.py:76`).
  - La capa de caché sellada (`data/experiment/evaluacion/llm_cache.py`) envuelve cualquier cliente que tenga
    `messages.create`. No se toca.
  - El tercer escalón del reintento transmite con `messages.stream` (`cliente_e1.py:94-98`).
- La app del repo ya usa Bedrock con el mismo SDK (`app/llm_backend.py`; `app/README.md:62-77`): reescribe
  el id del modelo debajo del cliente. Acá no sirve: el pedido guardado diría un modelo y la respuesta
  vendría de otro.
- El SDK instalado, anthropic 0.100.0, trae `AnthropicBedrock` (InvokeModel) y `AnthropicBedrockMantle` (la
  API de mensajes de Bedrock), los dos con transmisión. En el `.venv` del pipeline faltan `boto3` y
  `botocore`: `requirements.txt:11` fija `anthropic==0.100.0`, sin el extra.
- Documentación oficial, consultada el 05/10/2026.
  - Los dos modelos están disponibles. En la integración nueva, los ids son `anthropic.claude-haiku-4-5` y
    `anthropic.claude-sonnet-5`. En la anterior, Haiku 4.5 es `anthropic.claude-haiku-4-5-20251001-v1:0` y
    se invoca con un perfil de inferencia (`global.`, `us.` o `eu.`); Sonnet 5 no tiene id con versión
    (https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock y
    https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy).
  - Los puntos de acceso regionales cuestan un 10 % más que los globales
    (https://platform.claude.com/docs/en/about-claude/pricing).
  - La caché de prompts admite puntos de corte explícitos, con un mínimo de 4.096 tokens en Haiku 4.5 y de
    1.024 en Sonnet 5. Con inferencia entre regiones puede haber más escrituras de caché
    (https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html).
  - `tool_choice` forzado y `temperature` de 0 a 1 están admitidos en Haiku 4.5, que no acepta `temperature`
    y `top_p` juntas (página «Request and Response» de la API de mensajes de Claude en la guía de Bedrock:
    https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-anthropic-claude-messages-request-response.html).
- Lo que no pude leer, y lee esta unidad: los precios por token de los dos modelos en Bedrock, y las cuotas
  de la cuenta.

QUÉ HACE.
1. Antes de tocar código, con la documentación oficial y citada:
   - la integración: una sola para E1 y para E3, si acepta los dos modelos; si no, la que corresponda a
     cada uno, declarada;
   - los ids de los dos modelos y el tipo de punto de acceso;
   - los precios en Bedrock de la entrada, la salida, la escritura y la lectura de caché de cada modelo. Si la
     página de precios no los muestra, los declara la autora desde la consola.
2. El código.
   a. La plataforma se declara en el manifiesto de la corrida, en un campo opcional. Ausente quiere decir la
      API, y todo sale byte a byte como hoy. Con Bedrock lleva la integración, la región o el punto de
      acceso y los dos ids.
   b. El cliente de E1 y el de E3 salen de la plataforma del manifiesto. Vale también para el cliente de los
      reintentos del ratchet y para la transmisión del tercer escalón.
   c. El id del modelo de la plataforma va en el pedido. No se reescribe debajo de la caché.
   d. El namespace de E1, el de su reintento por salida mal formada y el de E3 llevan un sufijo de
      plataforma. Sin plataforma en el manifiesto, son los de hoy.
   e. Los precios salen de la plataforma, para el gasto y el tope (decisión 2 de caching). Cada respuesta
      real deja su línea de usage (decisión 3), y el registro del modelo guarda la plataforma, el id pedido y
      el id que devuelve la respuesta.
   f. No cambian el prefijo, el mensaje, el tool schema, la temperatura de E1 ni la de su reintento, el pedido
      de E3 fuera del id, ni ningún candado.
3. `requirements.txt`: el SDK con su extra de Bedrock, en la misma versión, y `boto3` y `botocore` fijados
   en la versión que quede instalada. La instalación en el `.venv` está autorizada.
4. La tabla de reprocesamiento y el selftest de claves:
   - una fila para la plataforma (el cliente, el id del modelo y el sufijo del namespace), de clase «todo»,
     con su variación: con Bedrock cambia la clave de E1 y la de E3 de todas las unidades;
   - lo que haga falta en F08, F09 y F10, que hoy nombran el modelo y el namespace;
   - el anclaje del perfil r2b tiene que poder correr con la plataforma del manifiesto;
   - `selftest_clave_cache.json`, regenerado sobre una copia, con el contraste con la tabla en OK.
5. Selftests, con clientes simulados y sin red: con Bedrock, el cliente, el id y el namespace que
   corresponden; sin plataforma, el mismo pedido y el mismo namespace de hoy.
6. Controles de que nada de lo anterior se mueve, sobre una copia:
   - el perfil sellado, byte a byte: el anclaje en 2.434 de 2.434 y 2.430 de 2.430, y la cadena r2a en
     `70d51e42…` y `fa4c1043…`;
   - el perfil r2b sin plataforma: las claves de las 27 unidades de P5 son las de
     data/experiment/prompt_r2/p5/salida/claves_despues.json;
   - con Bedrock, ninguna clave coincide con una de la API.
7. Las dos llamadas mínimas, con los puntos 5 y 6 en verde. Una a cada modelo, por el cliente nuevo, sin la
   caché local, con un mensaje de una línea y `max_tokens` chico. La de E1 lleva `temperature` 0; la de E3,
   el `thinking` deshabilitado de su pedido real. De cada una: si fue aceptada, el id de modelo que devuelve
   la respuesta, su usage y su identificador de pedido. Si una falla, se guarda el error tal cual. Se puede
   probar la otra integración dentro del tope, declarándolo.
8. Las cuotas de la cuenta para los dos modelos, en tokens y en pedidos por minuto: con la API de Service
   Quotas o la CLI de AWS, en solo lectura. Si la credencial no lo permite, las declara la autora desde la
   consola. Se comparan con lo que pide U-REEXT-T0, que corre en serie: unos 2.439 pedidos de E1 con un
   prefijo de 27.840 tokens, y otros tantos de E3.

FRENO final: la integración, los ids y los precios, con sus citas; lo que cambió, archivo por archivo; la
fila y la variación; los controles del punto 6; el resultado de las dos llamadas, con su costo, su fecha y
su hora; las cuotas; y lo que U-REEXT-T0 tiene que poner en sus manifiestos. Al día siguiente de las dos
llamadas, la autora verifica en la página de créditos de la consola que el crédito las cubrió.

ESCRITURAS: `e1_extractor/cliente_e1.py`, `e3_verificador/cliente_e3.py`, `corpus_v2/runner_corpus.py` y
`manifiesto_corpus.py`, de data/experiment/reextraccion_v2/; sus selftests (`e1_extractor/selftest_e1.py`,
`e3_verificador/selftest_e3.py`, `selftest_ub53.py` y `selftest_manifiesto.py`); `requirements.txt`;
data/experiment/mantenimiento/tabla_reprocesamiento.md, `code/selftest_clave_cache.py` y
`selftest_clave_cache.json`; una carpeta de la unidad, data/experiment/plataforma_bedrock/ (se crea), para el
freno, el script de las dos llamadas y sus salidas; y el scratchpad. Si hace falta otro archivo, frenás
antes de tocarlo.
PROHIBIDO: editar el prefijo, el mensaje, el tool schema, las constantes de temperatura o un candado; tocar
`data/experiment/evaluacion/llm_cache.py` o cualquier otra zona sellada; editar los manifiestos r2b, que
cambia U-REEXT-T0; llamar a la API de Anthropic; hacer más llamadas que las dos del punto 7; escribir una
credencial en un archivo; commitear.

CRITERIO DE ACEPTACIÓN. Sin plataforma en el manifiesto, todo sale byte a byte como hoy, en el perfil sellado
y en r2b. Con Bedrock, cambian el cliente, el id del modelo y el namespace, y nada más del pedido. La fila
de la tabla y su variación, con el contraste en OK. Las dos llamadas aceptadas, con el id de modelo devuelto
registrado. Las cuotas, reportadas.

DECISIONES DE LA AUTORA AL FIRMAR.
1. El tope de las dos llamadas (propuesta: USD 0,10 entre las dos).
2. El punto de acceso: global, sin recargo, o regional, con un 10 % más (propuesta: global; U-REEXT-T0 mide
   las escrituras de caché en sus primeras 27 unidades).
3. La región de AWS.
4. El nombre de la unidad y su carpeta (propuesta: U-PLATAFORMA y data/experiment/plataforma_bedrock/).

REQUISITOS: los de CLAUDE.md §4 (a a l), con PYTHONDONTWRITEBYTECODE=1 y .venv/bin/python -B; selftests y
controles sobre una copia sin enlaces, con el sha256 de los archivos del repo antes y después; todo conteo
recomputado contra su artefacto; cada dato de la documentación, con su dirección y su fecha de consulta, o
marcado NO VERIFICADA; cero nombres de personas; paquete de revisión con manifest.
