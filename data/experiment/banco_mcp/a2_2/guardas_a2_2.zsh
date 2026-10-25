# guardas_a2_2.zsh — Las guardas comunes de los cinco pasos pagos de A2.2, que cada paso carga con `source` desde la raíz del repo
# (pre-registro FIRMADO, a78ead7b; despacho del tramo 1 de A2.2, punto 2.k):
#   1. el sha256 de cada archivo del tramo 1 de A2.2 (a2_2/sha256_tramo1_a2_2.txt): si uno cambió, FRENO (código 6);
#   2. ningún otro paso pago corriendo, con pgrep, como los comandos de la mesa: el juez v2 (correr_juez_v2.py), la evaluación
#      (run_posthoc.py), una extracción (runner_corpus.py, lanzar_t*, correr_tanda*, ensamblar_tanda0.py) u otro paso del banco
#      (correr_a2_1.py, correr_smoke.py, correr_a2_2.py, juez_a2_2.py): FRENO (código 7);
#   3. la lista cerrada de variables con que corre cada paso, desde un entorno vacío (`env -i`): PATH, HOME, el venv del servidor
#      de fragmentos y el modo sin red del modelo; NEO4J_URI solo si la Terminal la trae. Ni MAX_MCP_OUTPUT_TOKENS (A-D6) ni
#      JUEZ_PROMPT_VERSION pasan. La clave del agente la pone el envoltorio de A2.1 y la del juez la toma el juez de EV2.
# A22_PYTHON, A22_BANCO_PYTHON_KG y A22_PATRON_PGREP existen solo para la corrida en seco (una copia, que no lleva .venv).
A=data/experiment/banco_mcp/a2_2
PY="${A22_PYTHON:-$R/.venv/bin/python}"
if ! shasum -a 256 -c --quiet "$A/sha256_tramo1_a2_2.txt"; then
  print -r -- "FRENO: un archivo del tramo 1 de A2.2 no da su sha256"; exit 6
fi
PATRON='correr_juez_v2\.py|run_posthoc\.py|runner_corpus\.py|lanzar_t|correr_tanda|ensamblar_tanda0\.py|correr_a2_1\.py|correr_smoke\.py|correr_a2_2\.py|juez_a2_2\.py'
# Solo en la corrida en seco (A22_MODO=init), A22_PATRON_PGREP cambia el patrón: así la prueba de esta guarda no depende de otros
# pasos pagos reales que estén corriendo en la máquina. En la corrida real rige siempre el patrón completo de arriba.
if [[ "${A22_MODO:-real}" == "init" && -n "${A22_PATRON_PGREP:-}" ]]; then PATRON="$A22_PATRON_PGREP"; fi
if pgrep -f "$PATRON" >/dev/null 2>&1; then
  print -r -- "FRENO: hay otro paso pago corriendo ($(pgrep -f "$PATRON" | wc -l | tr -d ' ') procesos)"; exit 7
fi
VENV_VECTOR="${BANCO_VENV_VECTOR:-$HOME/INGENIERIA IA/TESIS/venvs/banco_vector_py312}"
ENTORNO=(PATH="$PATH" HOME="$HOME" BANCO_VENV_VECTOR="$VENV_VECTOR" HF_HUB_OFFLINE=1 TRANSFORMERS_OFFLINE=1)
if [[ -n "${NEO4J_URI:-}" ]]; then ENTORNO+=(NEO4J_URI="$NEO4J_URI"); fi
if [[ -n "${A22_BANCO_PYTHON_KG:-}" ]]; then ENTORNO+=(BANCO_PYTHON_KG="$A22_BANCO_PYTHON_KG"); fi
# Las rutas que cambia la corrida en seco (las preguntas sintéticas y su orden); vacías en la real.
EXTRA=()
if [[ -n "${A22_PREGUNTAS:-}" ]]; then EXTRA+=(--preguntas "$A22_PREGUNTAS" --sha-preguntas "$A22_SHA_PREGUNTAS" --orden "$A22_ORDEN"); fi
EXTRA_POB=()
if [[ -n "${A22_PREGUNTAS:-}" ]]; then EXTRA_POB+=(--preguntas "$A22_PREGUNTAS" --sha-preguntas "$A22_SHA_PREGUNTAS" --no-real); fi
# El control del SDK y de la versión de la API (registro, §93), primero en los pasos del juez: frena con el código 8.
control_sdk() {
  local salida
  if ! salida="$(env -i "${ENTORNO[@]}" "$PY" -I -B scripts/control_sdk_anthropic_juez_y_banco.py)"; then
    print -r -- "FRENO: el control del SDK y de la versión de la API frenó"; print -r -- "$salida" | grep '^FRENO' || true; exit 8
  fi
  print -r -- "control del SDK: $(print -r -- "$salida" | grep -c '^OK ') de 5 en OK"
}
