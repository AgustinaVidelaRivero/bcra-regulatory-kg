# App de chat sobre los knowledge graphs

## Qué es

Una app web para chatear con un agente RAG que responde preguntas sobre
regulación del BCRA usando exclusivamente uno de los knowledge graphs del
repo, con citas a la norma y un visor de las tools que ejecutó para
responder. Cada turno y cada feedback quedan registrados para evaluación
humana posterior. Hay una instancia hosteada y también puede correrse
localmente.

## Usar la app (instancia hosteada)

Entrá a <https://graph-tag-eval.finreggraph.com.ar/>.

Elegí tu nombre de usuario y una contraseña; la primera vez te va a pedir
además el código de invitación (provisto por la autora). Desde cualquier
otro dispositivo volvés a entrar con nombre + contraseña — nunca ves ni
administrás tokens.

Elegí el grafo (recomendado: `run_3_ppf_core`, el grafo del experimento)
y preguntá. Qué vas a ver: cada respuesta trae el texto del agente, sus
citas (documento y ubicación en la norma) en una lista plegable, y un
visor plegable con las tools ejecutadas (nombre, argumentos y un resumen
del resultado). Debajo de cada respuesta hay botones 👍/👎 con comentario
opcional para dejar feedback. El identificador de la sesión aparece en
chico bajo el encabezado; "Nueva sesión" empieza un hilo nuevo, igual que
cambiar de grafo.

**Nota de transparencia:** las sesiones quedan registradas en el servidor
(pregunta, respuesta, tools, feedback, usuario y horario) para el
análisis de la investigación.

## Correr la app localmente

### Requisitos

- Python 3.10 o superior.
- Una API key de Anthropic — SOLO si usás el backend `anthropic`; el
  modo Bedrock no la usa.

### Instalación

Desde la raíz del repo:

```bash
python3 -m venv .venv-app
source .venv-app/bin/activate
pip install -r app/requirements.txt
```

### Modo anthropic (default)

```bash
export ANTHROPIC_API_KEY=sk-ant-...
uvicorn app.main:app --port 8000
```

y abrir <http://localhost:8000/>. La app solo lee la variable de entorno;
no usa ningún archivo `.env`.

### Modo Bedrock

Para servir la inferencia vía Amazon Bedrock, sin ninguna API key de
Anthropic en el entorno:

```bash
export APP_LLM_BACKEND=bedrock
export AWS_REGION=us-east-1
export APP_BEDROCK_MODEL_ID=us.anthropic.claude-haiku-4-5-20251001-v1:0
uvicorn app.main:app --port 8000
```

Las credenciales AWS se resuelven por la cadena estándar de AWS (variables
de entorno, perfil de `~/.aws`, o el rol IAM de la instancia — lo
recomendado en EC2): la app no guarda ni maneja secretos de AWS ni de
Anthropic. `APP_BEDROCK_MODEL_ID` es el model ID que Bedrock espere (por
ejemplo un perfil de inferencia de Claude Haiku, el modelo por defecto del
proyecto). Si falta alguna de las dos variables, la app falla al arranque
con un mensaje claro. Con `APP_LLM_BACKEND` sin setear (o `anthropic`), la
app funciona contra la API de Anthropic.

### Autenticación: registro con contraseña + código de invitación

Con la autenticación activa, cada persona se registra sola desde la
página: elige nombre de usuario y contraseña, e ingresa el código de
invitación solo la primera vez (`POST /register`). Para volver a entrar
— desde el mismo dispositivo u otro — alcanza con nombre + contraseña
(`POST /login`), que devuelve el mismo token de siempre. Los tokens
Bearer siguen existiendo por debajo (`/chat` y `/feedback` exigen
`Authorization: Bearer <token>`) pero el usuario nunca los ve: el
navegador guarda el suyo (localStorage) y "salir" lo borra. La página y
`GET /runs` son públicos.

Config del server:

```bash
# Archivo de tokens (fuera de git, 600): una línea token:usuario.
# Crece solo (append) con cada registro; puede arrancar vacío.
export APP_TOKENS_FILE=/ruta/a/tokens.txt
# Obligatorio si hay APP_TOKENS_FILE: habilita el registro.
export APP_INVITE_CODE=<código>
```

Las contraseñas nunca se almacenan en claro: van a un archivo hermano
`<APP_TOKENS_FILE>.claves` (creado por la app, 600) como
`usuario:salt:hash`, con pbkdf2-HMAC-SHA256 de 200.000 iteraciones.
`APP_TOKENS` (inline, separado por comas) existe solo para pruebas y no
habilita registro ni login (503).

Códigos de error: registro — código incorrecto 403, nombre en uso 409,
usuario o contraseña inválidos 422 (usuario: letras, dígitos, `.`, `_`,
`-`, máx. 32; contraseña: mín. 8); login — usuario no registrado 404,
contraseña incorrecta 401. Anti-abuso: registros exitosos y fallos de
login comparten un cupo de 10 eventos por hora en total → 429.

### Cómo agregar un grafo

Dejá un `kg.json` en `data/experiment/<nombre>/` y reiniciá la app: el
descubrimiento de grafos ocurre al arranque. Si el grafo nuevo trae
provenance múltiple (varias ubicaciones por nodo o arista), registrá su
`adapter_key` en el dict `ADAPTER_KEYS` de `app/main.py`; si no, se carga
con el adaptador nulo.

### Dónde quedan las sesiones

En `app/sessions/<usuario>/<session_id>.jsonl` (un archivo por sesión,
agrupado por usuario, ignorado por git). Con autenticación activa, el
usuario es el que corresponde al token; sin autenticación, es `local`.
El registro es append-only: una línea JSON por turno y una por feedback,
nunca se edita una línea ya escrita. Las líneas de turno guardan los
resultados completos de las tools (sin truncar) más el backend e ID de
modelo usados, así que sirven como traza íntegra de cada respuesta. Si el
server se reinicia, la numeración de turnos de una sesión continúa desde
el archivo existente. En el deploy hosteado, las sesiones se bajan a la
máquina local por rsync (comando exacto en el runbook de
`app/deploy/reporte_frente_hosting.md`).

## Operación del deploy

El deploy hosteado se opera desde `app/deploy/`: `sync.sh <IP>` sube al
server exactamente lo que la app necesita (código + grafos, preservando
rutas relativas), y `reporte_frente_hosting.md` contiene el inventario de
infraestructura y el runbook completo (deploy, logs, rotación del código,
revocación de usuarios, descarga de sesiones, teardown).

## Limitaciones conocidas

- Recargar la página conserva tu identidad pero inicia un hilo de chat
  nuevo.
- Un chat a la vez: el server serializa las preguntas.
- Cada turno es independiente: el agente no ve la historia de la
  conversación, solo la pregunta actual.
- Transporte: la instancia hosteada va por HTTPS (proxy delante); el
  server de origen habla HTTP — para despliegues propios, poner TLS
  adelante.
- El costo por turno registrado en las trazas usa precios de la API de
  Anthropic; bajo Bedrock es solo nominal.
