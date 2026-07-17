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

En `app/sessions/<fecha>.jsonl` (un archivo por día, ignorado por git).
El registro es append-only: una línea JSON por turno y una por feedback,
nunca se edita una línea ya escrita. Las líneas de turno guardan los
resultados completos de las tools (sin truncar), así que sirven como
traza íntegra de cada respuesta.

## Limitaciones conocidas

- Un chat a la vez: el server serializa las preguntas.
- La numeración de turnos se reinicia si se reinicia el server.
- Cada turno es independiente: el agente no ve la historia de la
  conversación, solo la pregunta actual.
- Recargar la página crea una sesión nueva.
