# Intake del feedback de la app — Motor 2

Flujo completo (laudo D1: el 👎 humano es el SÍNTOMA; el verificador validado
pone el DIAGNÓSTICO — acá no hay juez porque no hay respuesta esperada):

1. Un usuario de la app vota 👎 una respuesta (con comentario opcional); la
   sesión queda en `app/sessions/<usuario>/<session_id>.jsonl`.
2. `scripts/adaptador_sesiones.py` convierte cada 👎 en una traza
   load_rep-compatible en `trazas/<session>_<turno>/` (stub de juez
   explícitamente vacío, `sin_gold: laudo_humano`, síntoma en
   `sintoma_humano`) y apenda una línea a `cola_intake.jsonl`, estado
   `pendiente_de_triage`. Idempotente por clave `session+turno`.
3. **Guarda de quemado:** pregunta con match normalizado contra EV1/CQ/CQN/CQN2
   → `territorio_quemado: true` (con set e id). Se marca, no se descarta: el
   laudo de qué hacer es humano.
4. Triage humano de la cola → alta al `backlog.jsonl` (otra unidad; el
   adaptador NUNCA escribe en el backlog).
5. El verificador validado diagnostica la traza ({síntoma, causa}); etiqueta
   según el grafo de la sesión (`docs/spec_backlog_refinamiento.md` §3.b).
6. La entrada entra al circuito de refinamiento (propuesta sellada + laudo);
   el cierre de cada caso sigue el orden laudado: chunk-contra-PDF → pregunta
   con gold NO quemada → mini-key.
