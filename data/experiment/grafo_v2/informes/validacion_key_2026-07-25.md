# Informe — Validación de answer key: FRENO (archivo inexistente)

**La unidad no se ejecutó: `data/experiment/grafo_v2/piloto/answer_key.json` no existe.**

Verificaciones hechas (todas de solo lectura):

- `find` sobre `answer_key*` en todo el repo: el único match es `piloto/answer_key_TEMPLATE.json`.
- El TEMPLATE sigue **vacío**: 18 entradas, 0 con contenido (por si el key se hubiera llenado ahí en vez de en un archivo nuevo).
- Último commit: `892b3dd` (B1a) — trae solo la plantilla vacía. El swap de B1a-bis está en el working tree sin commitear (`M muestra_piloto.json`, `M answer_key_TEMPLATE.json`).
- Branch `extraccion-schema-v2` ✓. Ajenos sin tocar: `?? sessions_server/`.

**No se modificó ningún archivo.** La unidad indicaba operar sobre `answer_key.json` y reemplazar referencias `[PSPCP]`, `[PNFC]`, `[rol Exterior]`, `[rol RegInf]`, `[rol CapMin]`, `[rol Clasificación]` e instancias marcadas — no hay archivo del cual leerlas, y la regla explícita es no inventar lo que no se puede resolver.

Hipótesis para destrabar (decisión de la autora): (1) el key llenado quedó en un borrador local fuera de git (¿`docs/tesis/`?) y falta copiarlo a `piloto/answer_key.json`; (2) quedó en otra sesión/máquina; (3) todavía no se escribió.

Al existir el archivo en la ruta indicada, relanzar la unidad: se harán los reemplazos con tabla completa, la validación de todos los ids de `sujetos_esperados`/`sujetos_prohibidos` contra `esquema_v2_clases.json`, y el chequeo de los 18 `chunk_id` contra `muestra_piloto.json`.
