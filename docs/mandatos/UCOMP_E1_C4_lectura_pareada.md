# Mandato U-COMP-E1, etapa C4 — lectura pareada a ciegas de lo que produce cada modelo

**FIRMADO por la autora el 08/10/2026** (firma por mensaje de la autora; versión para firmar en `08ccdfa`, redactada por la mesa el mismo día
por decisión de la autora), con sus tres decisiones al firmar. Rige desde esta firma. Etapa nueva de
U-COMP-E1, que cerró con C3 (`323cef7`; mandato `docs/mandatos/UCOMP_E1_comparacion_chica_modelo.md`, FIRMADO en `cbcb823`). USD 0, sin
API: solo se leen salidas ya guardadas. No cambia la decisión de la tanda 1 (el modelo del extractor no cambia).

DE DÓNDE SALE.
- **Lo que U-COMP-E1 midió y lo que no.** C1 a C3 midieron si cada supuesto del grupo c quedó como Condicion unida a su norma (M1) y si
  se recuperaron las omisiones normativas (M2). No midieron si el resto de lo que produce cada modelo es correcto: Opus emite más
  relaciones (1.055 y 1.029 en sus dos corridas, contra 844 y 935 de Sonnet y 794 de Haiku en el intento 0, sobre las mismas 87 unidades;
  `data/experiment/comp_e1/c1/salida/m4_c1.json`, y para Haiku el conteo de la mesa sobre `c0/salida/intento0_haiku.jsonl`, con la misma
  base, `relations_out` de la validación), y no se sabe si
  son correctas ni si mete errores nuevos (`docs/insumos_escritura.md` §8, (e)).
- **Para qué.** La sección de la comparación de modelos del capítulo 5 (`docs/insumos_escritura.md` §8) y el punto de diagnóstico posterior
  a A2.2 (`docs/plan_tesis.md`, fila A2.2), donde el cambio de modelo es una de las palancas. Corre en paralelo con el escalado y tiene que
  estar lista antes de ese punto.

LO QUE SE LEE.
- **Las unidades:** una muestra de 30 de las 87 unidades de U-COMP-E1 (`data/experiment/comp_e1/unidades.json`), sorteada con una semilla
  nueva, sellada antes de sortear (propuesta: `U-COMP-E1:C4:2026-10-08`), con el sorteo de U-LECTURA-ACEPTADAS
  (`random.Random(semilla).sample(sorted(ids), 30)`).
- **Las extracciones de cada unidad, tres:** la de Haiku en su intento 0 (`c0/salida/intento0_haiku.jsonl`, el mismo pedido que los otros
  dos), la de Sonnet y la de Opus en la corrida que se fije al firmar (decisión 1). Las tres con el mismo formato: entidades con tipo,
  descripción y tramo, relaciones con origen, predicado, destino y evidencia, en un orden canónico (por tipo y por tramo), sin campos
  propios de un modelo (pensamiento, uso, ids de respuesta).
- **Recodificadas:** en cada unidad, las tres extracciones llevan códigos nuevos (distintos de los de C2, que ya se abrieron), asignados por
  una permutación por unidad con la semilla del sorteo. La tabla de códigos la escribe un script, que imprime solo su sha256; se sella
  cerrada y no se abre hasta después de la adjudicación. Se declara lo que la lectura puede descubrir igual: el largo (Opus emite más
  relaciones) y el estilo de las descripciones.

TAMAÑO, JUSTIFICADO.
- **30 unidades**, 90 extracciones. Es el tamaño de cada estrato de U-LECTURA-ACEPTADAS (`docs/mandatos/ULECTURA_ACEPTADAS_tasa_error_tanda0.md`,
  decisión 2), así la tasa por modelo es comparable con la del grafo de la tanda 0 (`docs/insumos_escritura.md` §7, ítem 5) y con la de la
  cola (12 de 30 en T4). Con 30, una tasa de 6 de 30 tiene un intervalo de Wilson al 95 % de [0,095; 0,373].
- **La comparación pareada** (cada modelo contra Haiku, unidad por unidad, McNemar exacto sobre los pares discordantes) solo detecta
  diferencias grandes: con 8 pares discordantes, 7 contra 1 da p = 0,070 y 8 contra 0, p = 0,008 (bilateral). Se declara como límite.
- **La precisión de las relaciones** sale de la misma lectura, sin muestra aparte: para decidir si una unidad tiene error hay que leer
  cada nodo y cada relación, y el veredicto de cada relación se registra. Con unas 9 a 12 relaciones por extracción, son del orden de 280
  a 360 relaciones por modelo. Más unidades (40) subirían la lectura a 120 extracciones; la propuesta es 30 (decisión 2).

CRITERIO, SELLADO ANTES DE LEER (sha256 y hora).
- **Unidad con error** (el criterio de U-LECTURA-ACEPTADAS, el del punto 1 de T4): una extracción tiene error si al menos un nodo o una
  relación suya no se sostiene en el texto de la unidad (propio o heredado). Las omisiones no cuentan como error y se anotan aparte.
- **Cada relación:** «se sostiene» (el texto de la unidad sostiene esa relación entre esos dos nodos, con ese predicado), «no se sostiene»
  (el texto alcanza para decidir y no la sostiene) o «no decidible». Cada «no se sostiene» lleva el tramo que lo muestra.
- **Cada nodo:** «se sostiene» o «no se sostiene», con el tramo.

ESTIMADORES, ESCRITOS ANTES DE LEER.
- Por modelo: unidades con error de 30, con Wilson al 95 % (z = 1,959964, la fórmula de T4); relaciones que se sostienen sobre las
  decididas, con Wilson y con un intervalo por remuestreo de unidades (las relaciones de una unidad no son independientes; semilla
  sellada); nodos que no se sostienen, por modelo.
- Pareada, Sonnet contra Haiku y Opus contra Haiku: los pares discordantes y McNemar exacto.
- **Errores nuevos:** en cada unidad, los elementos que no se sostienen en la extracción de Sonnet o de Opus sin un error de la misma
  clase en la de Haiku, por clase (nodo de tipo equivocado, relación con predicado equivocado, relación entre nodos que el texto no une,
  tramo que no sostiene).
- Todo descriptivo: no hay umbral ni decisión atada a la cifra.

ETAPAS.
- **C4-0. Preparación**, por una instancia nueva, sobre una copia: el sorteo, los códigos y las fichas, con el criterio y los estimadores,
  sellados antes de que nadie lea. La instancia no abre la tabla de códigos.
- **C4-1. Primera lectura**, de una sesión aparte, que no preparó las fichas ni diseñó el criterio. Sellada antes de comparar.
- **C4-2. Segunda lectura a ciegas de la mesa**, completa, sin abrir la primera. Sellada antes de comparar.
- **C4-3. Divergencias y adjudicación de la autora**, por unidad, por relación y por nodo.
- **C4-4. Cifras:** control previo (la lectura adjudicada es la primera con solo las líneas adjudicadas cambiadas), apertura de la tabla de
  códigos después del control, los estimadores tal como se sellaron, y FRENO C4 con el texto para la sección de la comparación de modelos
  del capítulo 5, que la mesa asienta en `docs/insumos_escritura.md` §8.

CRITERIOS DE ACEPTACIÓN, cada uno con su comando y su salida:
- la semilla, la muestra, la tabla de códigos (cerrada), el criterio y los estimadores, sellados antes de leer;
- las tres lecturas selladas antes de comparar;
- la tabla de códigos abierta después del control previo;
- sha256 del repo antes y después de cada etapa; 2.213 `.pyc`; grep de convenciones.

ESCRITURAS: `data/experiment/comp_e1/c4/` (se crea) y el scratchpad. La mesa asienta el texto en `docs/insumos_escritura.md` §8.
PROHIBIDO: la API; las salidas de C0 a C3 (solo se leen); los grafos sellados; commitear.
REQUISITOS: CLAUDE.md §4 (a a l).
CONVIVENCIA: en paralelo con el escalado y con cualquier unidad; no toca código del pipeline. Lista antes del punto de diagnóstico
posterior a A2.2.

DECISIONES QUE LA AUTORA TOMA AL FIRMAR:
1. **Qué corrida de Sonnet y de Opus.** Opciones: (a) la corrida 1 de cada uno; (b) una corrida sorteada por unidad. **Recomendación de la
   mesa: (a)**; M3 mostró que las dos corridas casi nunca coinciden (1 y 4 unidades de 87), y la variabilidad se declara.
2. **El tamaño.** Opciones: 30 o 40 unidades. **Recomendación de la mesa: 30**, comparable con U-LECTURA-ACEPTADAS, con el límite de la
   comparación pareada declarado.
3. **Quién prepara y quién lee.** Una instancia prepara (C4-0) y otra lee primero (C4-1), como en U2 de U-UNION-ESTRECHA. **Recomendación
   de la mesa:** sí, dos sesiones distintas, y la mesa en segunda lectura.

**Decididas al firmar (08/10/2026):** 1. **(a)**, la corrida 1 de Sonnet y de Opus; 2. **30 unidades**; 3. **sí**: una instancia prepara
(C4-0), otra sesión distinta lee primero (C4-1) y la mesa hace la segunda lectura a ciegas (C4-2).

## Firma

FIRMADO por la autora el 08/10/2026 (versión para firmar en `08ccdfa`), con sus tres decisiones. Rige desde esta firma.
