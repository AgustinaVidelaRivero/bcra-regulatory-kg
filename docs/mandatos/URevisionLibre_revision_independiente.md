FIRMADO por la autora el 03/10/2026

MANDATO — U-REVISION-LIBRE: REVISIÓN INDEPENDIENTE DEL GRAFO Y DE SU PROCESO DE CONSTRUCCIÓN ANTES DEL ESCALADO.
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar (solo sus reglas de trabajo; no sigas sus punteros al plan hasta la fase B).
- Costo de API: USD 0. Ninguna llamada a la API; Neo4j no se usa. Solo lectura.
- Escribís únicamente en reports/u_revision_libre/ (se crea) y en tu scratchpad. No editás código ni documentos, no commiteás.
- Tres frenos: FRENO A1 (temprano), FRENO A (fase A completa), FRENO B (final).
- Hay unidades en curso (U-PROMPT-R2 en data/experiment/prompt_r2/, U-R2-CODIGO-2): leé solo lo commiteado; no ejecutes nada en sus carpetas.

OBJETIVO. Encontrar problemas del grafo y de su proceso de construcción que el proyecto no haya visto, antes de escalar a los 152 TOs. Tu valor es la independencia: formate tu propia opinión antes de leer las conclusiones del proyecto.

FASE A — A CIEGAS. No leas, hasta el FRENO A: docs/plan_tesis.md, docs/tablero_correcciones.md, docs/checklist_pre_escalado.md, data/backlog/, docs/mandatos/, los laudos ni las enmiendas, ni los reportes de frenos (*_freno.md).
Leé:
- el corpus: los PDF de la tanda 0 y una muestra propia de TOs de la partición (data/experiment/segmentacion_84/b584_particion/), elegida por vos con criterio declarado;
- el pipeline: E0 (data/experiment/reextraccion_v2/e0_chunking/), E1, E3, E2, E4 y el ensamblado (data/experiment/tanda0/code/ensamblar_tanda0.py, corpus_v2/), el validador y los modelos (data/experiment/pyd_r2/);
- el prompt nuevo aprobado (data/experiment/prompt_r2/, lo commiteado) y el esquema que define modelos_r2.py;
- el grafo KG-Tanda0-Diez-r2a (data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2a/r2/kg.json) y su E0 (salida_tanda0_r2/).
Buscá, sin limitarte a esto:
1. Contenido de la norma que no llega al grafo, o llega deformado (comparando el PDF con los nodos).
2. Afirmaciones falsas en campos estructurados (tipos, relaciones, umbrales, sujetos, remisiones).
3. Supuestos del pipeline que no se cumplen en documentos que no son de la tanda 0 (formas de citar, de enumerar, tablas, anexos, notas, vigencias).
4. Riesgos de escala: costo, cortes, reintentos, caché, reproducibilidad, mantenimiento.
5. Aptitud para el uso: inventá entre 10 y 15 preguntas que un oficial de cumplimiento le haría a esta normativa, escritas solo desde los PDF, y verificá a mano si el grafo contiene lo necesario para responderlas y si un agente podría llegar. REGLA ESTRICTA: no uses, no busques ni leas las preguntas de EV2 ni las de la evaluación final (data/experiment/ev2*/, B6.3, pre-registros de evaluación); si las encontrás por accidente, frená y declaralo.
Cada hallazgo, con: evidencia (path:línea, id de nodo, página del PDF), gravedad (1: afirmación falsa en un campo estructurado; 2: contenido de la norma perdido; 3: ruido o costo), dónde se corrige (código sobre lo extraído, prompt, esquema, navegación del agente, límite a declarar) y frecuencia estimada con su base.

FRENO A1, temprano, antes de terminar la fase A: solo los hallazgos que exigirían cambiar el prompt de E1 o de E3. Es urgente porque el prompt nuevo se está congelando. Máximo 25 líneas.
FRENO A: la lista completa de la fase A, ordenada por gravedad, con las preguntas inventadas y el resultado de cada una.

FASE B — EL CRUCE. Después del «seguí» de la autora, leé el plan, el tablero, el checklist, el backlog, el protocolo entre tandas, los mandatos y los frenos. Para cada hallazgo de la fase A decí si es:
- ya resuelto (dónde y cómo);
- ya declarado como límite (dónde, con qué cifra);
- conocido y pendiente (en qué unidad);
- NUEVO.
Y para los nuevos: si entra antes de U-REEXT-T0, entre tandas por código (protocolo entre tandas) o como límite declarado. Una propuesta que cambie el esquema se reporta como tal y no se recomienda: la ventana de cambios de esquema está cerrada.

REQUISITOS: los de CLAUDE.md §4 (a a l), con PYTHONDONTWRITEBYTECODE=1 y .venv/bin/python -B; toda afirmación con evidencia o NO ENCONTRADO; copias para verificar armadas copiando archivos (regla l); cero nombres de personas en lo que escribas.

FRENO B, final: el reporte en reports/u_revision_libre/reporte.md, con un resumen de no más de 50 líneas, la tabla de hallazgos (hallazgo, gravedad, evidencia, clasificación del cruce, dónde se corrige, cuándo) y los NUEVOS primero.
