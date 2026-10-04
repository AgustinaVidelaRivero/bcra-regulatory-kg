FIRMADO por la autora el 04/10/2026

MANDATO — U-DIAG-VINCULO: COMPLEMENTO AL DIAGNÓSTICO DEL VÍNCULO ENTRE UNIDADES (tesis, capítulo 4).
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar.
- Dos frenos: FRENO V1 (temprano, no más de 15 líneas) y FRENO V2 (final, no más de 40 líneas).
- Costo de API: USD 0. Ninguna llamada a la API; Neo4j no se usa.
- Solo lectura y propuesta: no implementes, no edites código, no commitees. Escribís únicamente en reports/u_diag_vinculo/ (se crea) y en tu scratchpad.
- No uses docs/tesis/*.tex como fuente.
- URGENCIA: U-PROMPT-R2 está congelando el prefijo nuevo, y su prueba pareada (P4) espera este diagnóstico. Toda corrección que pase por el extractor tiene que saberse antes de P4.

CONTEXTO. Al escribir la sección del extractor (4.2) quedó explícita la causa del problema del vínculo entre unidades: el extractor lee una sola unidad por vez (VERIF-EXTRACTOR-42, 04/10/2026), así que cualquier relación entre contenidos de unidades distintas solo puede crearla el ensamblado, y hoy el ensamblado une unidades solo por una cita explícita (remite_a, enmienda 2 de L-ESQ-R2@5f9a731:54-55). El ejemplo que recorre toda la tesis es un caso de este problema: el párrafo sin numerar del punto 5.1.1 de Clasificación de deudores abre una excepción («Abarca todas las financiaciones comprendidas, con excepción de las siguientes») y el 5.1.1.1 la completa, en una unidad distinta. La tesis usa ese ejemplo para justificar el grafo, porque una regla leída sin su excepción da la respuesta contraria. Antecedente: U-DIAG-PROCESO (reports/u_diag_proceso/, 93ce4b7) clasificó este problema como «forma A» (el destino es el encabezado de un ancestro) y la autora lo había mandado a medir después de U-REEXT-T0; este hallazgo sube su prioridad.

DECISIONES YA TOMADAS. No se re-deciden.
1. La corrección no puede cambiar el esquema final (tipos, predicados y matriz: congelado más L-ESQ-R2 y su enmienda 2). Si una opción lo necesita, se reporta como tal y no se recomienda.
2. Esta unidad diagnostica y propone. La implementación, si se aprueba, es otra unidad con su propio mandato.

TAREA
1. En KG-Tanda0-Desarrollo-r2a (data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo_r2a/r2/kg.json; verificá que su sha256 empiece con 93a7af72), listá todas las aristas que unen un nodo con procedencia en la unidad del párrafo sin numerar de cla::5.1.1 con un nodo con procedencia en cla::5.1.1.1, en cualquier dirección. Si no hay ninguna, decilo, y decí qué camino existe hoy entre esos nodos, si existe alguno. Respuesta explícita sobre el ejemplo, aunque sea «ninguna arista».
2. Qué cubre ya el prefijo nuevo aprobado: leé la regla de composición con el encabezado de una lista (R30), la regla 1 (R16) y el ajuste de R8 (la Condicion de un ítem cuya norma está en otra unidad va sin condicion_de), en data/experiment/prompt_r2/ (lo commiteado) y en las notas fechadas al pie de docs/mandatos/UPROMPT_R2_prefijo_nuevo.md. Decí qué parte del ejemplo resuelve esa regla (por ejemplo, que la excepción del 5.1.1.1 lleve el contenido del encabezado) y qué sigue faltando (la relación entre la excepción y la regla del contenedor).
3. Medí cuántos casos de la misma forma hay en el universo, sin llamar a ningún modelo: párrafos sin numerar de un punto contenedor que anuncian contenido de sus subpuntos (por ejemplo, con «las siguientes», «con excepción de», «salvo», «en los siguientes casos»), con la regla de detección declarada antes de contar, por tipo de anuncio (excepción, condición, alcance, enumeración), en la tanda 0 y en la partición, con una muestra de 10 casos citados.
4. Evaluá estas 3 direcciones, sin implementarlas, y cualquier otra que encuentres: (a) que el ensamblado derive la relación desde la jerarquía de los puntos, sin modelo, cuando el párrafo del contenedor anuncia el contenido de sus subpuntos, con el predicado que corresponda en la matriz vigente; (b) que el extractor pueda referirse a una entidad de una unidad que está en su cadena estructural, por su punto y su tipo, y que el ensamblado lo resuelva como resuelve las remisiones; (c) una pasada aparte de un modelo sobre pares de unidad contenedora y subpunto. Para cada una, decí qué pieza cambia, si cambia el esquema, si cambia el prompt o el tool schema, si exige re-extraer, el costo estimado con su base, cómo se mediría que funciona (incluida la precisión: una arista derivada mal puesta es una afirmación falsa en un campo estructurado) y si puede entrar antes del escalado. Para (a), decí además cómo se declaran las aristas derivadas (procedencia, sin verificación de E3), como se hizo con remite_a, y si eso pide una nota o una enmienda a L-ESQ-R2.
5. Recomendá una dirección, o ninguna si ninguna es viable antes del escalado, en no más de 3 líneas.

FRENO V1, temprano: antes de terminar, respondé solo esto: ¿alguna dirección viable exige cambiar el prompt o el tool schema de E1? Si sí, cuál y por qué; si no, decilo. Con la respuesta a la tarea 1.
FRENO V2, final: las cinco tareas, con el reporte en reports/u_diag_vinculo/reporte.md.

REQUISITOS TRANSVERSALES (CLAUDE.md §4 a–l)
- PYTHONDONTWRITEBYTECODE=1 y .venv/bin/python -B en todo Python; línea de base de .pyc al inicio y control al cierre.
- Toda afirmación lleva path:línea, commit o comando. Lo que no esté en una fuente es NO ENCONTRADO. Las estimaciones de costo llevan su base de cálculo.
- Citas de documentos firmados, en su commit de firma (regla k).
- Hay unidades en curso: U-PROMPT-R2 (data/experiment/prompt_r2/), U-R2-CODIGO-2 y U-REVISION-LIBRE (reports/u_revision_libre/). Leé solo lo commiteado de sus carpetas; no ejecutes nada ahí.
- Toda corrida de control va sobre una copia armada copiando archivos (regla l).
- Shell zsh: variables entre comillas o como arrays; ningún comentario con # dentro de los bloques de comandos.
- Si algo de este mandato contradice un archivo del repo, mandan los archivos y se reporta la contradicción.

CRITERIO DE ACEPTACIÓN
- las 5 tareas respondidas con path:línea, commit o la salida del comando, o NO ENCONTRADO;
- la tarea 1 con la respuesta explícita sobre el ejemplo;
- git status --short sin cambios propios fuera de reports/u_diag_vinculo/, y .pyc con las mismas entradas al inicio y al cierre.
