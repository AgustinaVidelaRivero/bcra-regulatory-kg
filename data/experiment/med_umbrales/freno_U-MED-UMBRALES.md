# FRENO — U-MED-UMBRALES (unidad de diseño, USD 0, sin API)

**Repo.** HEAD `1f9b262` al inicio y `18d9e05` al cierre. Entraron tres commits que no son de esta sesión (`293fe8d`, `33c43e9` y
`18d9e05`), y ninguno toca un archivo citado (`git diff --name-only 1f9b262 HEAD`).
- `git status --short` pasa de 14 a 10 líneas. Las cuatro que faltan (los tres archivos de `e0_chunking` y `s0_4/`) entraron en
  `18d9e05`; no hay ninguna línea mía.
- `.pyc` fuera de `.venv`: 2.213 entradas al inicio y al cierre (`diff` vacío).
- Todo el Python corrió con `PYTHONDONTWRITEBYTECODE=1 -B`, sobre copias en el scratchpad.

**Entregables.**
- `borrador_enmienda1_preregistro_tripletas_umbrales_U-MED-UMBRALES.md`: la enmienda 1 al pre-registro de tripletas, en BORRADOR y sin
  firmar.
- `propuesta_U-MED-UMBRALES.md`: las razones, las opciones con su costo y su tiempo, y las decisiones D1 a D10.

**Lo que propongo.**
1. **Vehículo:** una enmienda, con la vía de umbrales como sección propia. Es admisible porque no se sorteó nada: el sorteo de V espera
   el re-sellado (`docs/laudo_release_r2_pipeline.md:53`). Las once decisiones y los topes no cambian.
2. **Unidad y cifra:** el elemento de umbral. La cifra es el *núcleo*: pertinencia, valor, unidad, moneda, comparación y base literal.
   Al lado van el *completo* (con el tipo de días y el destino) y el *núcleo contra la definición*.
   - La referencia es la norma leída con L-ESQ-R2 §1.3 (`4ef7650`) y sus enmiendas 3 y 5, nunca el código.
   - Estricto por inclusivo cuenta como *contradicha*.
   - Lectura en dos pasos: el primero, sin los campos del grafo.
3. **Población y muestra:** los elementos del grafo evaluado sin cola, en los TOs fuera de los 15 de exclusión. La muestra:
   - 240 elementos con contenido, estratificados por autor, origen y base, con un mínimo de 25 por estrato;
   - el censo de las bases resueltas;
   - 30 vacíos.
   La mitad del ancho da 0,0498 con p = 0,85 (efecto de diseño 1,21).
4. **Quién lee:**
   - A: la autora. USD 0, entre 8 y 13 horas (NO VERIFICADO). Es la que recomiendo.
   - B: un juez por la API, calibrado en la tanda 0, con una sola recalibración. Cuesta unos USD 13,8.
   - C, dos sesiones de Claude Code: descartada por el principio 8 (`plan:272-279`).
5. **Afirmación:** «el grafo guarda correctamente hasta qué monto…» exige un límite inferior de al menos 0,90 en el núcleo y en la
   comparación. Con 240, sale con probabilidad 0,70 si la exactitud real es 0,95.
6. **Piloto:** 40 elementos del grafo sin cola de la tanda 0, en dos lotes, sin cifra para el capítulo 5. No contamina porque la tanda 0
   queda fuera de la población y porque el orden es fijo: regla → correcciones → sello → sorteo.
7. **Lo compartido con tripletas:** el armador de fichas, el sorteo, los estimadores y el acta. Se esperan entre 0,35 y 2,0 fichas
   comunes; cuando las haya, va primero la tripleta, cerrada, y el solapamiento se declara.
8. **Clases de error:** si son de implementación, se corrigen en código en el grupo 2, con un test de regresión por clase, control
   negativo y re-ensamblado a USD 0. Las de la definición, solo después de una enmienda a L-ESQ-R2. Las de E1 o E0 van al backlog.

**Hallazgo del recuento.** 305 de los 1.306 elementos del grafo sin cola de la tanda 0 están vacíos (314 de 1.373 en `a9631a64`): son
del validador, sin valor, sin base y con la comparación `no_determinada`. Quedan fuera del núcleo y se leen aparte. Las cifras de
1.373 umbrales los incluyen.

**Desvíos y contradicciones.**
- El mandato dice «no corras ninguna medición». Corrí recuentos estructurales del marco sobre copias: los tamaños de estrato, los
  vacíos y el solapamiento. No juzgan ningún campo, y las cifras del mandato se reproducen (el script de VERIF-UMBRALES da `diff` vacío).
- Agregué el estrato de vacíos a los que pide el mandato.
- El pre-registro de tripletas no tiene una cláusula de enmienda: la enmienda se apoya en el precedente de la tanda 0 y en la firma.

**PENDIENTE (acciones de la autora):** las decisiones D1 a D10, la firma, el commit de la enmienda con sus scripts, la nota al pie del
pre-registro y la nota al plan.

**Paquete y copia.** `revision_U-MED-UMBRALES/`, con `manifest.txt`. La copia permanente va a `fuera_del_repo/scratchpads/`, con la misma
ruta relativa; el resultado de su verificación está en el mensaje del FRENO.
