FIRMADO por la autora el 03/10/2026

MANDATO — U-DIAG-PROCESO: DIAGNÓSTICO Y PROPUESTA DE 2 PROBLEMAS DEL PROCESO QUE LA MEDICIÓN DE COBERTURA DEJÓ SIN RESOLVER.
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar.
- Unidad en UNA ETAPA, con FRENO al final: reporte de no más de 50 líneas, más una tabla.
- Costo de API: USD 0. Ninguna llamada a la API; Neo4j no se usa.
- Solo lectura y propuesta: no implementes, no edites código, no commitees. Escribís únicamente en reports/u_diag_proceso/ (se crea) y en tu scratchpad.
- No uses docs/tesis/*.tex como fuente.
- URGENCIA: esta unidad entrega antes del FRENO P1 de U-PROMPT-R2, que está en curso. Toda corrección que pase por las instrucciones del extractor tiene que entrar en U-PROMPT-R2 antes de que su P2 congele el prefijo.

CONTEXTO. La medición de cobertura del esquema de partida (ESQ-2) dejó 2 familias de omisión que no son del esquema sino del proceso, y que hoy no resuelve nada (VERIF-ESQ-FINAL, 03/10/2026):
- Pérdida del contenido del encabezado (familia F1, «pérdida de contenido del chapeau»): el texto que encabeza una lista, y que sus incisos heredan, queda sin extraer. Fichas 11, 13, 48, 52 y 64; 5 de 38 fichas al azar, en 3 documentos (data/experiment/esq/cobertura/tabla_resultados_esq2.md@bbac990:57-61, :85). Se midió con la herencia y los mini-chunks de E0 ya puestos. El laudo ESQ-3a la mandó a «B5 con entrada trazable» (laudo_ESQ-3a_retoques.md@0a76549:231-233), y esa entrada no existe (docs/plan_tesis.md@d69b11f:717-732).
- Vínculo normativo entre unidades: una norma depende de otra escrita en otra unidad, sin una cita explícita entre las 2, y el grafo no las une. Fichas 18, 39, 61 y 72; 1 de 38 al azar más 3 dirigidas, en 4 documentos (tabla_resultados_esq2.md@bbac990:92; la cita «la resuelve E3» está en la ficha 44, worksheet_fichas_esq2.json:5412). Ni remite_a, que nace solo de una cita explícita (enmienda 2 de L-ESQ-R2@5f9a731:54-55), ni condicion_de, que sigue dentro de la unidad, la cubren.

DECISIONES YA TOMADAS. No se re-deciden.
1. La autora quiere corregir los 2 problemas antes del escalado, para que la tesis no tenga que declararlos como límites.
2. La corrección no puede cambiar el esquema: tipos, predicados y matriz quedan como en el esquema final (congelado más L-ESQ-R2 y su enmienda 2). Si una opción necesitara tocar el esquema, se reporta como tal y no se propone como recomendada.
3. Esta unidad diagnostica y propone. La implementación, si se aprueba, entra en una unidad ya planificada (U-PROMPT-R2 o U-REEXT-T0) o en otra con su propio mandato.

TAREA
1. Para cada problema, caracterizalo sobre las fichas citadas: qué se pierde, con un ejemplo textual de una ficha (path:línea), y por qué el proceso actual no lo cubre (qué pieza debería y por qué no lo hace hoy, con path:línea del código o del documento).
2. Estado actual. Para cada ficha de los 2 problemas, decí si el problema persiste con el pipeline actual: la E0 e0-r2, la herencia vigente y las remisiones de U-R2-CODIGO (incluida la regla (i), citas del texto heredado). Usá el grafo r2a de U-MED-R2A si ya está commiteado; si no, el más reciente commiteado, y declaralo. Cruzá F1 con las 23 ausencias de categoría P de la tanda 0 (reports/u_pre_r2/d2_ausencias.md: contenido presente bajo sub-puntos, enviado a A1.8) y decí si son el mismo fenómeno.
3. Prevalencia. Para cada problema, la fracción en la muestra al azar con su intervalo de Wilson al 95 %, y lo que eso implica, como orden de magnitud, sobre las unidades de la partición.
4. Para cada problema, proponé entre 1 y 3 opciones de corrección. Para cada opción, decí:
   - qué pieza cambia (E0, el extractor y sus instrucciones, el verificador E3, el ensamblado, la navegación del agente u otra);
   - si cambia el esquema;
   - si exige re-extraer y cuánto;
   - el costo estimado en USD, con la base de la estimación;
   - si consume la ventana de corrección según la enmienda de uso de la ventana (enmienda_uso_ventana_2026-09-30.md@30f106c:72-76);
   - si puede entrar en una unidad ya planificada (U-PROMPT-R2, U-REEXT-T0 o A1.8) en lugar de una unidad nueva, y si llega a tiempo para U-PROMPT-R2.
   Para el vínculo entre unidades, decí además si es un problema del grafo o de la navegación del agente (subir al encabezado, recorrer hermanos), y en el segundo caso, si cae en A1.8.
5. Para cada opción, decí cómo se mediría que funcionó: qué unidades se vuelven a leer o qué caso de control entra en la suite, y qué resultado cuenta como corregido.
6. Recomendá una opción por problema, o ninguna si ninguna es viable antes del escalado, y explicá por qué en no más de 3 líneas. Si es ninguna, proponé cómo declararlo como límite y qué cifra lo respalda.
7. Una tabla final: problema, opción, pieza, cambia el esquema (sí o no), re-extracción, costo, ventana, unidad donde entra, llega a U-PROMPT-R2 (sí o no), medición y recomendación.

REQUISITOS TRANSVERSALES (CLAUDE.md §4 a–l)
- PYTHONDONTWRITEBYTECODE=1 y .venv/bin/python -B en todo Python; línea de base de .pyc al inicio y control al cierre.
- Toda afirmación lleva path:línea, commit o comando. Lo que no esté en una fuente es NO ENCONTRADO. Las estimaciones de costo llevan su base de cálculo.
- Citas de documentos firmados, en su commit de firma (regla k).
- Hay dos unidades en curso: U-MED-R2A (escribe en data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2/, corpus_tanda0/ens_*_r2a/ y data/experiment/medicion_r2a/) y U-PROMPT-R2 (escribe en data/experiment/prompt_r2/). Podés leer lo que esté commiteado de esas carpetas, pero no ejecutes nada ahí ni leas lo que no esté commiteado.
- Toda corrida de control va sobre una copia armada copiando archivos (regla l).
- Shell zsh: variables entre comillas o como arrays; ningún comentario con # dentro de los bloques de comandos.
- Si algo de este mandato contradice un archivo del repo, mandan los archivos y se reporta la contradicción.

CRITERIO DE ACEPTACIÓN
- las 7 tareas respondidas con path:línea, commit o la salida del comando, o NO ENCONTRADO;
- al menos una opción por problema con su costo, su medición y su efecto sobre el esquema;
- git status --short sin cambios propios fuera de reports/u_diag_proceso/, y .pyc con las mismas entradas al inicio y al cierre.

FRENO al terminar.
