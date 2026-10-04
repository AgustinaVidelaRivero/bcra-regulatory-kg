BORRADOR — PENDIENTE DE FIRMA

MANDATO — U-NAV-DISENO: DISEÑO DE LA NAVEGACIÓN DEL AGENTE (A1.8). SE PREPARA AHORA Y SE MIDE DESPUÉS DE LA TANDA 1.
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar.
- Unidad en DOS PARTES. Parte 1, ahora, USD 0: N1 (diagnóstico), N2 (diseño de herramientas), N3 (preguntas
  de desarrollo, por una instancia aparte) y N4 (protocolo de medición). Parte 2, después de la tanda 1, con
  tope a fijar por la autora: N5 (implementación, USD 0), N6 (ablaciones) y N7 (pre-registro).
- FRENO obligatorio al final de cada etapa, con reporte corto (no más de 40 líneas) y espera del «seguí»
  escrito de la autora. La parte 2 no arranca sin un «seguí» propio, posterior al cierre de la tanda 1.
- Costo de API: USD 0 en la parte 1. Ninguna llamada a la API. Neo4j local, solo consultas de lectura.
- Durante la tanda 1 el agente queda fijo: la parte 1 no toca el agente, sus herramientas ni los índices
  (decisión de la autora del 01/10/2026, docs/plan_tesis.md:327).

CONTEXTO, con sus anclas.
- El agente: `GraphAgent` (data/experiment/evaluacion/harness.py:423, archivo sellado) y `GraphAgentNeo4j`
  (data/experiment/neo4j/agente_neo4j.py:56), con tres herramientas (`buscar_nodos`, `ver_nodo`,
  `ver_vecinos`) y `max_tool_calls` 15.
- Atribución A0.2 de los pares definitivos parciales o incorrectos (reports/tanda0/reporte_fase2a.md, §4
  punto 3; regla en data/experiment/ev2_reporte/regla_atribucion.md, `40603a9`): ausencia_kg /
  alcanzabilidad más vista_no_consultada / generacion = 8/8/18 en C1, 6/2/23 en C2, 8/7/15 en C3, 9/3/17 en
  C4 y 0/4/8 en C5.
- Necesidades ya registradas en la fila A1.8 (docs/plan_tesis.md:327):
  - vecinos salientes sobre una Operacion con restricciones entrantes, en las cuatro celdas;
  - remisiones vistas y no abiertas;
  - el campo `termino` fuera del índice (data/experiment/neo4j/indices.py:78);
  - tope de 15 llamadas alcanzado en 23 de 40 respuestas base de C2, 27 de 40 de C3, 17 de 40 de C4 y 11
    de 20 de C5;
  - 23 de las 31 ausencias de C1 a C4 son contenido presente bajo puntos descendientes del ancla
    (categoría P de D2, reports/u_pre_r2/d2_ausencias.md:46-58; checklist N9);
  - 157 nodos con la cuantía después del carácter 160 de la descripción, que el resumen de `buscar_nodos`
    no muestra (harness.py:110-124; reports/u_umbral/u1_mediciones.json);
  - la forma B del vínculo entre unidades (regla en una unidad hermana, sin cita; 1 de 38);
  - el volumen de `remite_a`: 14.000 aristas en KG-Tanda0-Diez-r2a, y `alcance` no se exporta a Neo4j
    (enmienda 2 de L-ESQ-R2, §7). Una cita da una arista por cada nodo de origen y cada nodo de contenido
    del punto citado (`corpus_v2/r1_referencias.py:1087-1089`; enmienda 2, `5f9a731:127`): en
    KG-Tanda0-Desarrollo-r2a, 1.382 citas dan 12.833 aristas, y en diez, 1.547 dan 14.000
    (`reporte_ensamblado_r2.json`, clave `remite_a`);
  - el alcance que fija la cadena de títulos cuando los títulos no terminan en «:» (hallazgo 2.7 de
    U-REVISION-LIBRE, reports/u_revision_libre/freno_a1.md, punto 3; `54f57cd`). Las unidades
    `docvig::2.1.1.1`, `2.1.2.1` y `2.2.1.1` listan «Pasaporte del país de origen» bajo el mismo título
    y solo se distinguen por los títulos de sus ancestros (la edad y el tipo de residencia). Sus nodos
    no los llevan: la procedencia trae los ids de los ancestros, no sus títulos. Puntos terminales con
    menos de 100 caracteres propios: 228 de 2.052 en la tanda 0 y 1.275 de 7.430 en la partición
    (cifras de esa unidad, NO VERIFICADAS: no las recomputé);
  - la marca de la cola humana (`cola_humana`, `cola_chunks` y `estado_e3`) y `no_verificada_e3`. Las
    unidades de la cola humana entran al grafo marcadas (decisión de la autora del 04/10/2026,
    docs/plan_tesis.md:363). En los nodos, el cargador exporta la marca y `ver_nodo` la devuelve
    (data/experiment/neo4j/cargar_kg.py:93-114; neo4j_index.py:206-223). En las aristas no llega: el
    cargador exporta solo `orden` y `provenances_json` (cargar_kg.py:153-174). En KG-Tanda0-Diez-r2a
    son 291 nodos y 466 aristas con la marca de la cola, y 697 aristas con `no_verificada_e3`. Las claves
    que quedan fuera de `properties` (`properties_no_definidas` del nodo y `no_verificada_e3` de la
    arista) no pasan de la vista que arma el grafo para el agente
    (data/experiment/tanda0/code/comun_tanda0.py:78-94);
  - la unión de las operaciones. Con la fase r2b las operaciones se unen solo dentro de su punto (decisión
    de la autora del 04/10/2026, docs/plan_tesis.md:399): un mismo acto regulado en varios puntos queda en
    varios nodos. Hasta r2a se unían por etiqueta: en KG-Tanda0-Desarrollo-r2a, 37 de 1.555 operaciones
    juntan más de un punto, y en diez, 59 de 2.047; los grafos r1 de las trazas tienen las mismas uniones.
    De las 37 de desarrollo, 18 juntan el mismo acto, 8 juntan actos distintos y 11 son dudosas
    (reports/verif_union_ops/, lectura de esa verificación).
- «Cierre léxico»: NO ENCONTRADO con ese nombre en el plan, el checklist, el tablero ni el protocolo
  (grep del 03/10/2026). N1 lo define con su evidencia o lo descarta.
- El patrón «jueces unánimes, falla del grafo; jueces dispersos, falla de navegación» no tiene ancla en el
  repo (NO VERIFICADO). N1 lo mide; no se da por cierto.

PARTE 1 — AHORA (USD 0).

N1. DIAGNÓSTICO SOBRE LAS TRAZAS QUE YA EXISTEN.
- Entrada, solo lectura: trazas de C1 (data/experiment/ev2_r1/trazas/, `774acac`) y de C2 a C5
  (data/experiment/ev2_tanda0/trazas/, `7f3b207`), con sus re-corridas; salidas del juez y veredictos
  definitivos; reports/tanda0/atribucion_tanda0.json.
- Unidad de análisis: cada criterio no cumplido de cada par definitivo parcial o incorrecto. Si la salida
  del juez no identifica el criterio, se cuenta el par y se declara.
- Cuatro clases, con regla operativa escrita ANTES de clasificar:
  1. no encontró el nodo: el nodo que porta el contenido está en el grafo y no apareció en ningún resultado;
  2. lo encontró y no siguió sus relaciones: el nodo apareció y no se abrió, o se abrió y el contenido del
     criterio estaba en un vecino no recorrido (entrantes, `remite_a`, `condicion_de`, `exceptua`,
     `exceptua_obligacion`, hijos del punto);
  3. el contenido no estaba en el grafo;
  4. llegó bien y generó mal: los nodos necesarios se abrieron y la respuesta falla.
  La regla declara cómo se corresponde con las clases de A0.2, que mira el ancla y no el criterio. Las 23
  ausencias P de D2 no van a la clase 3. Lo que la regla no decide va a lectura asistida, con «no
  decidible» como resultado válido y contado.
- Prueba del patrón de los jueces: antes de usarlo, verificar qué varía entre los tres votos de las
  re-corridas (el agente, el juez o los dos; docs/protocolo_corrida_ev2.md:104-116). Después, la tabla de
  votos (unánimes / divididos) por clase, en conteos crudos por celda. Sin porcentajes sobre n chico.
- Cota por herramienta, sin agente: para cada falla de las clases 1 y 2, qué herramienta candidata de N2
  habría puesto el nodo a la vista (consulta fuera de línea contra el grafo de la celda). Es una cota
  superior, y se declara así.
- Conteo de los patrones de la fila A1.8 por clase, y de las respuestas que llegaron al tope de llamadas.
- Efecto de la multiplicación de las aristas de remisión sobre la navegación (decisión de la autora del
  04/10/2026): cuántas llamadas a `ver_vecinos` devuelven aristas de remisión, cuántas de esas aristas van
  al mismo punto citado, y cuántas respuestas llegan por ellas al tope de vecinos (`limite` 40) o al de
  llamadas. Las trazas que existen son de grafos r1, donde la remisión es `referencia` (4.836 aristas en
  KG-Tanda0-Diez-r1): se mide sobre ellas y se declara. La medida sobre `remite_a` se repite en la parte 2.
- Efecto de la separación de las operaciones sobre la navegación (decisión de la autora del 04/10/2026):
  cuántas respuestas pasaron por una Operacion que junta más de un punto y siguieron sus aristas hacia
  nodos de otro punto. Son los caminos que la separación corta. Se cuenta por celda, con el veredicto de
  cada respuesta.
FRENO N1.

N2. DISEÑO DE LAS HERRAMIENTAS CANDIDATAS (documento; no se implementa en la parte 1).
Para cada una: firma (entradas, salida y tamaño máximo), necesidad que atiende con su conteo de N1, qué
exige del grafo o del índice, costo estimado en tokens por llamada, y si la mejora vale igual para el
sistema por fragmentos o es propia de la navegación por aristas (diferencia declarada entre brazos, A1.8).
1. Búsqueda híbrida: texto completo y semántica (modelo del bake-off, docs/decision_modelo_embeddings.md),
   sobre la descripción, `termino`, el tramo literal de cada entidad del perfil r2b y el texto de la
   unidad; búsqueda por número de punto. Mismo analizador en los dos brazos, o la diferencia declarada.
   Para una operación, la búsqueda devuelve todas las operaciones del mismo acto repartidas en varios
   puntos, con el punto de cada una (decisión de la autora del 04/10/2026). El diseño dice con qué regla
   las reúne. Caso de prueba: «Clasificación en categoría Irrecuperable», que hoy es un nodo con
   `cla::6.5.5.3`, `6.5.5.4` y `6.5.5.5` y con r2b son tres: una búsqueda encuentra las tres.
2. Recorrido por predicado: vecinos filtrados por predicado y dirección (`remite_a` con su `alcance`,
   `condicion_de`, `limita`, `exceptua` y `exceptua_obligacion`). Declarar qué exige exportar `alcance`.
   Al seguir `remite_a`, la salida agrupa los nodos por punto citado (`destino`): una entrada por cita,
   con los nodos de ese punto adentro (decisión de la autora del 04/10/2026). No cambia el grafo.
3. Jerarquía: subir al punto padre, bajar a los hijos, ver los hermanos (ausencias P; forma B).
   Caso de prueba obligatorio (decisión de la autora del 04/10/2026, tras U-DIAG-VINCULO, `b0ee084`): desde
   un contenedor que anuncia una lista, el agente llega a los nodos de sus puntos hijos. Son 637
   contenedores en la partición (reports/u_diag_vinculo/salidas/censo_anuncios.json). El caso fijo es el
   ejemplo de la tesis: de la Definicion de `cla::5.1.1::intro` a la Excepcion de `cla::5.1.1.1`. La
   relación no existe como arista: la herramienta la recorre por `punto` y `ancestros` de la procedencia.
4. Texto fuente de la unidad, con su página.
5. Vista de umbrales: las cuantías de un nodo con su tramo literal.
6. Títulos de los ancestros (hallazgo 2.7; decisión de la autora del 04/10/2026: herramienta candidata,
   medida por ablación, fuera de la configuración base). La cadena de títulos de los ancestros de cada
   nodo entra al índice de búsqueda y se muestra en el resumen de la búsqueda y en la vista del nodo. Se
   toma de la E0, por `punto` y `ancestros` de la procedencia: no cambia el grafo ni el prompt de E1.
   Caso de prueba: los nodos de `docvig::2.1.1.1`, `2.1.2.1` y `2.2.1.1` se distinguen por su cadena de
   títulos, en la búsqueda y en la vista.
Las instrucciones del agente y el tope de llamadas se tratan como parámetros de la configuración.
Tres reglas de las vistas (decisiones de la autora del 04/10/2026). No son herramientas y no cambian la
cantidad de configuraciones de N4:
- Marcas de verificación. El agente ve la marca de la cola humana en el nodo y en la arista, y
  `no_verificada_e3` en la arista. Exige exportar a Neo4j las propiedades de la arista y las claves que
  quedan fuera de `properties`, y devolverlas en `ver_vecinos`: es el mismo cambio que pide `alcance`.
  El diseño dice cómo se le muestra la marca al agente y qué le indican las instrucciones sobre el
  contenido no verificado.
- Modalidad clasificada. La vista del nodo muestra `properties_no_definidas.modalidad_clasificada`, con el
  tramo copiado (`modalidad` o `consecuencia`). Es la clasificación que hace el código desde el marcador
  que copia E1: `recomendacion`, `consecuencia_de_incumplimiento` o `no_clasificada` (diseño de P3b de
  U-PROMPT-R2, data/experiment/prompt_r2/p3b/diseno_p3b.md, §7; `023f9a0`). Es una de las claves fuera de
  `properties` que la vista hoy no lleva.
- Lo que la vista no muestra (decisión de la autora del 04/10/2026). La marca
  `properties_no_definidas.copia_nota_e3` no se le muestra al agente. Marca una posible copia de la nota del
  verificador en la descripción, y acierta en 11 de los 45 casos leídos de la tanda 0
  (data/experiment/prompt_r2/p3b2/lectura_copia_nota.md, `c8c3970`). Sirve para la evaluación y para las
  muestras de cada tanda, no para la navegación.

N3. PREGUNTAS DE DESARROLLO, POR UNA INSTANCIA APARTE.
- Conjunto separado del de EV2 y del de B6.3. Nunca se usa para evaluar ni se reporta como resultado.
- Lo genera a ciegas una instancia aparte, solo desde los PDF (precedente:
  data/experiment/exploracion/ev2_fidelidad/registro_generacion_ev2_fidelidad.md). No lee el grafo, las
  trazas, las preguntas de EV2 ni las de la tanda 0, el diseño de N2 ni material de B6.3.
- Sobre TOs presentes en el grafo de desarrollo y ya excluidos de B6.3 (a). La lista se verifica contra
  data/experiment/esq/documentos_excluidos_esq.json y docs/protocolo_entre_tandas.md §6, y se declara.
- Con gold por criterios y anclas, en el molde de EV2, y registro de generación con sha256 de los PDF.
- Tamaño propuesto: 30 preguntas, con cupos por necesidad (remisión, condición o excepción, umbral,
  jerarquía, definición). Se sella con su sha256 antes de que la instancia de esta unidad lo lea.
- La revisión cruza después sus anclas con las de EV2 y declara las coincidencias.

N4. PROTOCOLO DE MEDICIÓN (documento; corre en la parte 2).
- Grafo de desarrollo de r2b, fijo. Modelo del agente y juez, los de EV2, sin cambios.
- Configuraciones: base (las tres herramientas de hoy), todas, y todas menos una por cada herramienta.
  Con seis herramientas son 8. La base se repite 3 veces para medir la variación entre corridas.
- Medidas por configuración: fidelidad por criterio (criterios cumplidos sobre el total), precisión de
  citas (fundada, existente, al ancla), costo por pregunta, llamadas a herramientas y respuestas que llegan
  al tope, y las cuatro clases de N1 sobre las fallas.
- Lo verificado y lo no verificado se miden aparte: las mismas medidas, para las respuestas que abren o
  citan algún nodo o arista con la marca de la cola humana o con `no_verificada_e3`, y para las demás.
- Regla de decisión, escrita antes de medir: una herramienta entra si quitarla baja la fidelidad por
  criterio más que la variación entre corridas de la base; a igualdad, la configuración más barata.
- Requisito de la configuración: la que se pre-registre tiene que pasar el caso de prueba obligatorio
  de la jerarquía (N2, herramienta 3). No es un resultado de la ablación: si la regla de decisión deja
  afuera la herramienta que lo cubre, la configuración no se pre-registra así y vuelve a la autora.
- Costo estimado: (8 + 2) × 30 = 300 corridas. Referencia: las cuatro celdas de E5 costaron USD 21,2577
  por 140 respuestas base con sus re-corridas y el juez (docs/plan_tesis.md:400), unos USD 0,15 por
  respuesta: alrededor de USD 46. ESTIMACIÓN NO VERIFICADA: las herramientas nuevas cambian los tokens.
- Pre-registro: la configuración elegida (herramientas, instrucciones, tope, índices y analizador) se
  sella con su sha256 antes del pre-registro de B6.3 y se declara ahí. Lo que mejora la búsqueda se aplica
  igual al sistema por fragmentos.
FRENO N2-N4, con el diseño y el protocolo juntos.

PARTE 2 — DESPUÉS DE LA TANDA 1 (no arranca sin «seguí» y tope).
N5. Implementación de las herramientas en módulos nuevos, con selftest (USD 0). FRENO.
N6. Ablaciones según N4, con el tope que fije la autora. FRENO.
N7. Pre-registro de la configuración elegida. FRENO final.

ESCRITURAS. Parte 1: solo data/experiment/navegacion/ (se crea) y el scratchpad; la instancia de N3, solo
data/experiment/navegacion/preguntas_dev/. Parte 2: módulos nuevos bajo data/experiment/navegacion/.
PROHIBIDO: editar el cuarteto sellado de evaluación, las trazas, los eval sets y los grafos; usar EV2 o
material de B6.3 para medir en la parte 2; usar el conjunto de N3 para evaluar; commitear.

DECISIONES DE LA AUTORA AL FIRMAR.
1. Tope de N6 (estimación: USD 46, NO VERIFICADA).
2. Tamaño y TOs del conjunto de N3 (propuesta: 30).
3. Si las 40 de EV2 y las 20 de la tanda 0 siguen como material de ajuste, como dice la fila A1.8, o
   quedan solo para el diagnóstico de N1.
4. Cantidad de configuraciones y repeticiones de la base.
5. Si N5 puede empezar sobre el grafo de U-REEXT-T0 antes del cierre de la tanda 1.
6. Si `alcance` se exporta a Neo4j (hoy no: enmienda 2 de L-ESQ-R2, §7). Las marcas de verificación de
   las aristas se exportan por la decisión del 04/10/2026; queda por decidir si `alcance` va en el mismo
   cambio.
7. Si las marcas de verificación entran también a la configuración base de N4 (propuesta: no; la base
   queda como el agente de hoy, para que se compare con las trazas que ya existen). Los títulos de los
   ancestros no entran a la base: decisión de la autora del 04/10/2026 (N2, herramienta 6).

REQUISITOS: los de CLAUDE.md §4 (a a l), con PYTHONDONTWRITEBYTECODE=1 y .venv/bin/python -B; todo conteo
con el comando que lo reproduce; copias para verificar armadas copiando archivos; cero nombres de personas.
