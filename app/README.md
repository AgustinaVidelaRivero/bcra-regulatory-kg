# App local de chat sobre los knowledge graphs

## Qué es

Una aplicación web local para chatear con un agente RAG que responde
preguntas sobre regulación del BCRA usando exclusivamente un knowledge
graph (elegís cuál de los grafos del repo usar en cada conversación).
Cada turno y cada feedback quedan registrados en disco, para evaluación
humana posterior de las respuestas.

## Requisitos

- Python 3.10 o superior.
- Una API key de Anthropic.

## Instalación

Desde la raíz del repo:

```bash
python3 -m venv .venv-app
source .venv-app/bin/activate
pip install -r app/requirements.txt
```

## Configuración

```bash
export ANTHROPIC_API_KEY=sk-ant-...
```

La app solo lee esa variable de entorno; no usa ningún archivo `.env`.

## Modo Bedrock

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
app funciona como siempre contra la API de Anthropic.

## Autenticación: registro por código de invitación

Con la autenticación activa, cada persona se registra sola desde la
página: entra, elige un nombre e ingresa el código de invitación
(provisto por la autora). Queda identificada y puede chatear — nunca ve
ni administra tokens: el navegador guarda el suyo (localStorage) y el
link "salir" lo borra. Por debajo, `/chat` y `/feedback` siguen exigiendo
`Authorization: Bearer <token>`, así que un cliente por curl puede usar
un token del archivo directamente. La página y `GET /runs` son públicos.

Config del server:

```bash
# Archivo de tokens (fuera de git, permisos 600): una línea token:usuario.
# Crece solo (append) con cada registro.
export APP_TOKENS_FILE=/ruta/a/tokens.txt
# Obligatorio si hay APP_TOKENS_FILE: el código que habilita registrarse.
export APP_INVITE_CODE=<código>
```

`APP_TOKENS` (inline, separado por comas) sigue existiendo para pruebas,
pero sin archivo el registro autoservicio queda deshabilitado (503).
`POST /register` responde: código incorrecto → 403; nombre en uso → 409;
más de 10 registros en una hora (total, anti-abuso) → 429. El usuario
admite letras, dígitos, `.`, `_` y `-` (máx. 32). Formato inválido en el
archivo o token duplicado impiden el arranque con mensaje claro. Los
tokens y el código viajan en claro mientras el server hable HTTP plano
(limitación ya documentada): usar detrás de TLS o en red confiable.

## Arranque

Desde la raíz del repo, con el venv activado:

```bash
uvicorn app.main:app --port 8000
```

y abrir <http://localhost:8000/> en el navegador.

## Qué vas a ver

Arriba, un selector de grafo poblado con los grafos descubiertos en el
repo, cada uno con su cantidad de nodos y aristas. En el centro, el chat:
escribís una pregunta, el agente explora el grafo y responde. Cada
respuesta trae sus citas (documento y ubicación en la norma) y un visor
plegable con las tools que el agente ejecutó (nombre, argumentos y un
resumen del resultado). Debajo de cada respuesta hay botones 👍/👎 con
comentario opcional para dejar feedback. El identificador de la sesión
está visible en chico bajo el encabezado; el botón "Nueva sesión" empieza
una sesión nueva, igual que cambiar de grafo o recargar la página.

## Cómo agregar un grafo

Dejá un `kg.json` en `data/experiment/<nombre>/` y reiniciá la app: el
descubrimiento de grafos ocurre al arranque. Si el grafo nuevo trae
provenance múltiple (varias ubicaciones por nodo o arista), registrá su
`adapter_key` en el dict `ADAPTER_KEYS` de `app/main.py`; si no, se carga
con el adaptador nulo.

## Dónde quedan las sesiones

En `app/sessions/<usuario>/<session_id>.jsonl` (un archivo por sesión,
agrupado por usuario, ignorado por git). Con autenticación activa, el
usuario es el que corresponde al token; sin autenticación, es `local`. El registro es append-only: una
línea JSON por turno y una por feedback, nunca se edita una línea ya
escrita. Las líneas de turno guardan los resultados completos de las tools
(sin truncar) más el backend e ID de modelo usados, así que sirven como
traza íntegra de cada respuesta. Si el server se reinicia, la numeración
de turnos de una sesión continúa desde el archivo existente.

## Limitaciones conocidas

- Un chat a la vez: el server serializa las preguntas.
- Cada turno es independiente: el agente no ve la historia de la
  conversación, solo la pregunta actual.
- Recargar la página crea una sesión nueva.
- El server habla HTTP plano (sin TLS); al hostearlo, el TLS se agrega
  por delante (p. ej. Cloudflare).
- El costo por turno registrado en las trazas usa precios de la API de
  Anthropic; bajo Bedrock es solo nominal.
