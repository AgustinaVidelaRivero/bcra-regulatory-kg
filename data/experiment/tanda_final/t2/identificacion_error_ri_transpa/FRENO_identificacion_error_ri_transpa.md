# FRENO corto — el error definitivo de ri_transpa (tanda final, T2, después del FRENO T2 parcial 1; 19/10/2026)

USD 0, sin API, sin relanzar. Las cifras salen de `identificar_error_ri_transpa.py` → `identificacion_error_ri_transpa.json` y de
`unidades_mismo_camino_tramo2.py` → `unidades_mismo_camino_tramo2.json`, en esta carpeta. Desde la raíz del repo:
`<repo>/.venv/bin/python -B data/experiment/tanda_final/t2/identificacion_error_ri_transpa/<script> --repo "$PWD" --out <json>`.

## Lo que leí

De la salida del runner, solo `ri_transpa/`: el script recorre `extracciones_e1.jsonl` para encontrar la unidad con error (la regla de
`resumen_t2.py`) y de ella guarda solo campos sin contenido (id, tipo, error, `stop_reason`, tokens, reintentos, partición); de
`finales.jsonl` toma solo los ids, para saber si la unidad llegó a E3; mira si está en `particiones_por_corte.json`. No guarda ni
muestra `tool_input_crudo`, `validacion`, `titulo` ni la salida de ningún intento, ni ningún estado de E3. Los caracteres salen de la
E0 de la tanda final, y la partición, del código de E0.

## La unidad

- **`ri_transpa::Sbloque1::chapeau_seccion`**, un `mini_chunk` de 21.712 caracteres propios (21.749 completos).
- **Fase: E1.** No está en `finales.jsonl`: no llegó a E3. No hay NO_ABRIR_ que dar.
- **Error:** `salida_mal_formada_tras_reintento`.
- **El último intento:** max_tokens 8.192, `stop_reason` max_tokens, 8.192 tokens de salida.
- **Intentos de E1: 3**, en un solo renglón de `extracciones_e1.jsonl`:
  1. el pedido, con max_tokens 8.192: `stop_reason` tool_use, 6.132 tokens de salida, **mal formado** (`entities_o_relations_invalidos`);
  2. el reintento por forma 1 (`-rforma1`, temperatura 1), con max_tokens 8.192: cortó (max_tokens, 8.192 tokens);
  3. el reintento por forma 2 (`-rforma2`, temperatura 1), con max_tokens 8.192: cortó igual.
- **Partición: el runner no intentó partirla.** No hay reintento por corte, ni tercer escalón, ni informe de partición en su registro,
  y no está en `particiones_por_corte.json`. Se podría partir: `particionar_por_corte` la parte en 2 (13.705 y 8.006 caracteres; 12
  bloques de tabla y 19 ítems con guion). En la corrida en seco de T1 se partió así porque el stub la hacía cortar.

## El camino

El runner escala el max_tokens (a 16.384, después partición o 40.960) solo si **el primer intento** corta
(`cliente_e1.crear_con_reintento_corte`). Acá el primer intento no cortó: salió mal formado con 6.132 tokens. Los reintentos por forma
van con el max_tokens de ese pedido, 8.192, porque el techo de corte se usa solo si hubo corte (`runner_corpus.py`, `kwargs_forma`). Si
cortan, la unidad queda con `salida_mal_formada_tras_reintento`, sin escalar ni partir. El censo de T1 (sección 6) no contemplaba este
camino: miraba solo la capacidad del reintento por corte.

## Las unidades del tramo 2 que pasan por el mismo camino

Para fallar así, una unidad tiene que poder sacar más de 8.192 tokens en un reintento por forma, y además su primer intento tiene que
salir mal formado sin cortar. Con las razones de salida del censo de T1, eso pide más de 5.443 caracteres propios con la p90 (1,5051
tokens por carácter) y más de 7.073 con la mediana (1,1582).

- **Tramo 2: 25 de 4.350 unidades sobre el umbral de la p90, y 18 sobre el de la mediana.** Por tipo: 17 `seccion_sin_puntos` y 8
  `punto_terminal`; ningún `mini_chunk`. Por TO: snp_mep 7, cateloc 6, afiltr 4, reqcac 2, y rmgcti, ri2_ci, gescre, horari, finsec y
  adfsp 1 cada uno.
- **Las 8 mayores son las del censo de T1:** `cateloc::Sbloque10` (48.321, la única que se parte), `cateloc::Sbloque9` (19.633),
  `cateloc::Sbloque7` (16.797), `cateloc::Sbloque8` (15.779), `cateloc::Sbloque6` (13.753), `rmgcti::S11` (11.244), `ri2_ci::S5`
  (11.170) y `reqcac::SB` (11.111). Las otras 17, de 10.881 a 5.484 caracteres, no estaban en el censo; ninguna se parte. La lista
  completa, con su tipo, sus bloques de tabla y si se parten, está en `unidades_mismo_camino_tramo2.json`.
- **Para comparar, el tramo 1** tenía 15 unidades sobre el umbral de la p90 (14 sobre el de la mediana), y falló una de ellas, esta. En el
  control entre tramos, 6 de sus 601 unidades tuvieron reintento por forma.
- Es una lista de exposición, no una predicción: solo falla la que, además, saca un primer intento mal formado sin cortar.

## Controles

- Nada escrito fuera de esta carpeta: `git status --porcelain --untracked-files=no` vacío, y los `.pyc` siguen en 11.236.
- No mostré contenido de ninguna extracción ni ninguna cifra por estado de E3.

FRENO. Espero la decisión de la autora.
