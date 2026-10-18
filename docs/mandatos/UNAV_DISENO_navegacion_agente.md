# Mandato U-NAV-DISENO, v6 — la navegación del agente en el banco (A1.8), antes de N7

**FIRMADO por la autora el 18/10/2026** (firma por mensaje de la autora, recibida a las 18:18:43; hoja de ruta de la mesa, §168), sobre
la v6 para firmar (sha256 `998ba8fc27e3ffa0f0ced023be117980e236d092c5fffc58d5e6d36b53d2ee41`, en el paquete de la mesa, `decisiones_166_mesa/unav/`). La autora
aceptó el mínimo de 3 por subtipo de varios puntos que agregó la mesa (§4, N3), y tomó las decisiones 9 y 10 al firmar (§8). La 9 no es
ninguna de las tres opciones de la v6: la parte de la estrategia que vale para los dos brazos va a la plantilla común desde N6, sin
medirla aparte. El texto firmado aplica las dos en el §2, el §3, el §4, el §5, el §6, el §6 bis, el §7, el §8 y el §9. Rige desde esta
firma.

La v6 la redactó la mesa el 18/10/2026 (hoja de ruta de la mesa, §166), para firmar esa noche, así la parte 1 arrancaba ese día.
Reemplaza a la v5 (§165) con lo que la autora pidió el 18/10/2026, recibido a las 17:34:23: la decisión 8 en la
(a), y cuatro cambios. N2 pasa a seis familias, cada una con su necesidad medida en N1 y su marca, y N6 vuelve a 8 configuraciones con el
mismo tope (§3, §6 y decisión 3). La regla de N4 se aplica por familia (§6). N1 mide los hubs (§4). N3 fija la mezcla de tipos desde la
norma (§4). Trae dos decisiones nuevas, la 9 y la 10, que esos cambios abren (§8). La v5 reemplazó a la v4 (§154) con los cinco cambios
que la autora pidió antes de firmar: el cegamiento por U-MED-VERIF
(§7, regla 5), tres mediciones más en N1 (§4), N2 abierto a candidatas nuevas, con la vista compuesta del punto (§3), la regla de N4 (§6)
y el generador de N3 (§4). La v4 reemplazó a la v3 (§153), con las dos decisiones de la autora del 18/10/2026 recibidas a las 10:45:54: la 7, opción (a), y la
medición F1 sobre BM25 (§6 bis). La v3 traía los tres agregados de la autora del mismo día (recibidos a las 10:31:44) y las seis
decisiones que eligió en ese mensaje (§8). Reemplaza al BORRADOR del 04/10/2026 (`docs/mandatos/UNAV_DISENO_navegacion_agente.md`, último cambio en `97c21e4d`), que no se firmó.
Firmada, va al repo en esa misma ruta, con un commit que prepara la mesa. Lo que el borrador decía y esta versión no cambia sigue con sus
anclas, en especial el CONTEXTO (las necesidades de la fila A1.8) y la regla de las cuatro clases de N1.

**De dónde sale:**
- la fila A1.8 del plan (`docs/plan_tesis.md:331`), con el registro del 07/10/2026 (D2 y D7): la parte 2 corre en el banco Claude Code +
  MCP, B1.10 entra como herramienta candidata, A2.2 corre antes de las ablaciones y A1.8 ajusta con su conjunto propio, nunca con EV2
  (F-2);
- las decisiones de la autora del 17 y el 18/10/2026: A2.2, su diagnóstico y N6 antes de N7, con lo pago en secuencia; N6 y el
  diagnóstico no se recortan; las reglas del punto 7 (hoja de la mesa, §150 y §152);
- las del 18/10/2026, recibidas a las 10:31:44 (hoja de la mesa, §153):
  - el texto del prompt, antes de A2.2 (§5);
  - las seis decisiones del §8;
  - los agregados: la híbrida medida en el brazo de fragmentos (§6 bis), el cargador sin el filtro «KG_Tanda0_» (N5) y la lista de los
    14 TOs de N3;
- las del 18/10/2026, recibidas a las 10:45:54 (hoja de la mesa, §154): la decisión 7, opción (a), y la medición F1 sobre BM25, con el
  tope de N6 entero en USD 85 y freno en 64, y GraphRAG adentro;
- el banco: `data/experiment/banco_mcp/agentes/config_agentes.json` y `data/experiment/banco_mcp/mcp_kg/servidor_mcp_kg.py`;
- el mandato de A2.1 (`docs/mandatos/A2_1_sistema_por_fragmentos_preregistro_A2_2.md`, §5, `:128-160`), que fija qué lleva el
  pre-registro de A2.2;
- los cinco cambios de la autora del 18/10/2026, pedidos antes de firmar (hoja de la mesa, §165), y el §7 bis del mandato firmado de
  U-PROC-HERENCIA (`docs/mandatos/UPROC_HERENCIA_procedencia_de_tramos_heredados.md`; registro, §34 y §35), que da la regla del
  cegamiento;
- los cambios de la v6, del 18/10/2026, recibidos a las 17:34:23 (hoja de la mesa, §166), y el relevamiento del estado del arte que trae
  la autora (`decisiones_166_mesa/unav/relevamiento_estado_del_arte_18102026.md`, en el paquete de la mesa; sus cifras quedan NO
  VERIFICADAS).

## 1. Qué cambia respecto del borrador del 04/10

1. **El instrumento:** el banco, no `GraphAgentNeo4j`.
   - Las herramientas nuevas son herramientas MCP.
   - El modelo es el del banco (`claude-sonnet-5`, CLI 2.1.241, `--bare`).
   - El juez es el de A2.2 (el de EV2, `data/experiment/ev2_juez/juez.py`, con su modelo y su prompt por sha; mandato de A2.1, `:141`).
2. **B1.10 adentro:** la búsqueda híbrida es la familia 1, la entrada (§3).
3. **Cada familia marcada** como «vale para fragmentos» o «propia del grafo». Lo que vale para fragmentos se mide en ese brazo en
   N6 y se aplica en B6.3 solo si pasa su regla (§6 bis).
4. **El orden:**
   - N1 a N5, en paralelo con la tanda final;
   - el diagnóstico de A2.2 (N5b), sobre sus trazas;
   - N4 sellado después del diagnóstico;
   - N6 después;
   - N7, antes del corte del sábado 24/10 a las 12:00.
5. **N3:** 30 preguntas sobre TOs que no entran en las preguntas de B6.3, selladas antes de usarse.
6. **El ajuste se hace solo con N3.** EV2 y las 20 de la tanda 0 quedan solo para el diagnóstico de N1 (F-2; decisión 3 del borrador,
   resuelta).
7. **El texto del prompt** (§5).
8. **El costo de N6,** recalculado con lo medido en el banco (§6).

## 2. El agente de hoy, que es la configuración base

Detalle y fuentes en el paquete de la mesa, `decisiones_150_mesa/agente/configuracion_del_agente_y_A1_8_mesa.md`.
- **Las herramientas:** `buscar_nodos`, `ver_nodo` y `ver_vecinos`, con la firma v1 del harness congelado (`servidor_mcp_kg.py:4-12`).
- **La búsqueda:** texto completo con el analizador `spanish` sobre `label`, `descripcion`, `description` e `id_texto`
  (`data/experiment/neo4j/indices.py`). El resumen corta en 160 caracteres (`data/experiment/evaluacion/harness.py:110-124`).
- **Los vecinos:** en las dos direcciones por defecto, hasta 40 por dirección (`data/experiment/neo4j/neo4j_index.py:226-272`).
- **El tope:** `--max-turns` 12, 10 llamadas en el prompt y USD 0,30 por sesión. El criterio de corte de A2.2 lo fija la autora al firmar
  su pre-registro, con la señal de H-B2 (mandato de A2.1, `:137`). La base de N6 usa ese mismo corte.
- **La base no lleva las marcas de verificación:** queda como el agente de hoy, para compararse con las trazas que ya existen (propuesta
  del borrador, decisión 7). Las marcas entran con las aristas que muestran las familias 2, 3 y 5, si entran.
- **Desde N6, la base lleva la parte común de la plantilla** (decisión 9): descomponer la pregunta y revisar las condiciones y las
  excepciones antes de responder. Con el texto del prompt del §5, es lo que la separa del agente de las trazas que ya existen, y se
  declara al compararla con ellas.

## 3. Las familias de herramientas (N2)

Seis familias (cambio de la autora del 18/10/2026, recibido a las 17:34:23). Cada una lleva su necesidad, medida en N1, y su marca. La
columna del relevamiento cita sus antecedentes, NO VERIFICADOS (`relevamiento_estado_del_arte_18102026.md`).

| # | Familia | Lo que da | Necesidad, medida en N1 | Preguntas de su necesidad en N3 | Vale para | En el relevamiento |
|---|---|---|---|---|---|---|
| 1 | **Entrada** | la búsqueda híbrida (B1.10): BM25 más el modelo denso del bake-off (`harrier-oss-v1-0.6b`), sobre la descripción, `termino`, el tramo literal de cada entidad y el texto de la unidad. Devuelve puntos, cada uno con su título, el fragmento que coincide y sus nodos. Filtra por TO, por punto y por `termino` | la mezcla, H3 (el `termino`), las 7 anclas nunca vistas; la medición 1 de N1 (la posición del ancla) | la de cupo 1 | **fragmentos, medido** (§6 bis): la híbrida y los filtros por TO y por punto. Son **propios del grafo** los nodos de la salida y el filtro por `termino`. Mismo analizador | RAGSearch, GraphRAG-Bench, HippoRAG2, RAGulating Compliance |
| 2 | **Vista de punto** | en una sola llamada: el texto de la unidad, sus nodos con su tipo, los umbrales enteros con su tramo literal, los hijos y los títulos de los ancestros | lo que el nodo no lleva; los 157 nodos con la cuantía después del carácter 160; el hallazgo 2.7 (`docvig::2.1.1.1`); las varias llamadas por punto; la medición 2 de N1 (el techo) | las de cupo 4, 5, 6 y 7 | **propia del grafo:** el brazo de fragmentos ya lee el texto; los nodos, los umbrales por nodo, los hijos y los títulos son del grafo | HippoRAG2, RAGulating Compliance |
| 3 | **Cierre de remisiones** | los puntos citados y los que citan al punto, resueltos, cada uno con su título y el comienzo de su texto, a 1 o 2 saltos | las remisiones vistas y no abiertas; el abanico de `remite_a`; la medición 3 de N1 (las `remite_a` que llegan a un punto con nodos) | la de cupo 2, y las de la mezcla del subtipo «remisión» | **propia del grafo** | RefWalk |
| 4 | **Índice del TO** | el árbol de los puntos del TO, por nivel | las 23 ausencias P de D2; el caso obligatorio de `cla::5.1.1::intro`; la forma B; la medición 3 de N1 (los contenedores con hijos alcanzables y los pasos hasta el gold) | la de cupo 3, y las de la mezcla del subtipo «excepción en un hijo» | **propia del grafo, declarada:** el árbol también sale de la E0, que los dos brazos comparten; la diferencia entre los brazos se declara en N7 (regla 3 del §7) | SearchFireSafety, PageIndex |
| 5 | **Vecinos selectivos** | primero, los tipos de relación del nodo con su cuenta; después, los vecinos de un predicado. Los hubs van resumidos: sus tipos y cuentas, sin la lista | los vecinos salientes; los hubs, con la medición 4 de N1 (qué nodos son hubs y cuánto ocupan en las respuestas) | las de la mezcla cuyo gold pasa por un hub, con la regla de la medición 4, fijadas en N4 antes de N6 | **propia del grafo** | Search-on-Graph, CatRAG |
| 6 | **Estrategia** | lo propio del grafo: los 3 ejemplos de navegación, de las 3 preguntas de ejemplo de N3 (decisión 10), y las instrucciones de sus herramientas. Nunca de B6.3 ni de EV2. La parte que vale para los dos brazos (descomponer la pregunta y revisar las condiciones y las excepciones antes de responder) no es de esta familia: va a la plantilla común desde N6 (decisión 9) | la generación como clase modal; las remisiones y las condiciones no revisadas; el tope alcanzado en C1 a C5 | las de la mezcla de varios puntos | **propia del grafo.** Si sus ejemplos entran en N7, el brazo de fragmentos lleva los mismos 3, resueltos con su herramienta, declarado (decisión 10) | RAGSearch, Search-on-Graph, GraphWalk, GraphSearch |

- **Las salidas son compactas, en tablas de texto y no en JSON.** Cada familia fija en N2 su tamaño máximo por llamada.
- **El tope de llamadas** (P2 de la v5) no es una familia: es el corte común de los dos brazos (R5), y no se ablaciona.
- **De dónde viene cada familia** (las filas de la v5): la 1, de la herramienta 1; la 2, de la 4, la 5, la 6 y la vista compuesta (7);
  la 3 y la 5, de la 2; la 4, de la 3; y la 6, de las instrucciones (P1).
- **N2 queda abierto a candidatas nuevas que salgan de N1** (cambio de la autora del 18/10/2026, de la v5):
  - cada una entra en la familia que le toca, con su necesidad medida y su marca;
  - lo que el relevamiento sugiere y N1 no mide queda como hipótesis de N2, declarada, y no entra a N6 por sí solo;
  - **el tope de N6 no cambia,** y las configuraciones siguen siendo 8: una candidata nueva no suma una configuración.
- **Las herramientas de las familias 1 a 5 son herramientas MCP** de un módulo nuevo del servidor del grafo, con su selftest. La familia
  6 es texto del bloque de herramientas del brazo del grafo, y la parte común de la decisión 9, texto de la plantilla (§5). No cambian el harness congelado, el cuarteto sellado ni las tres herramientas de
  hoy.
- **La firma de cada herramienta** (entradas, salida y tamaño máximo), su costo en tokens por llamada y lo que exige del índice o de Neo4j
  van en el documento de N2, como en el borrador.
- **Lo que pide exportar a Neo4j:** las propiedades de las aristas (las marcas de la cola, `no_verificada_e3` y la del sujeto derivado),
  para las aristas que muestran las familias 2, 3 y 5. Decisión 6.

## 4. Las etapas

**Parte 1, sin costo, fuera del repo y en paralelo con la tanda final.** No entra en la fila de las ejecutoras del repo: lee lo commiteado
con `git show` y trabaja sobre copias, como el sorteo de las preguntas.
- **N1. Diagnóstico sobre las trazas que ya existen,** las de C1 a C5. Es el del borrador, con sus cuatro clases y sus mediciones.
  Suma cuatro mediciones por script, a USD 0, sobre el acumulado de las tandas 0 y 1 sin cola (las tres de la v5 y los hubs, de la v6):
  1. **la entrada:** para las anclas de EV2 (`data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json`) y de las 20 de la
     tanda 0 (`data/experiment/ev2_tanda0/preguntas/preguntas_tanda0.json`):
     - en qué posición sale el nodo del ancla con `buscar_nodos`;
     - en qué posición sale su pasaje con el BM25 del brazo de fragmentos (`banco_mcp/mcp_vector/bm25_fragmentos.py`);
     - las dos, a 1, 5 y 10 resultados;
  2. **el techo:** para cada ancla, si lo que piden sus criterios está en algún nodo o solo en el texto de la unidad;
  3. **la navegabilidad:**
     - a cuántos pasos del nodo de entrada están los nodos que pide el gold;
     - cuántos contenedores tienen hijos alcanzables;
     - cuántas `remite_a` llegan a un punto con nodos;
  4. **los hubs** (cambio de la autora del 18/10/2026, de la v6):
     - un hub es un nodo del acumulado sin cola con un grado (aristas entrantes más salientes) en el 1 % más alto; el 5 % va como
       sensibilidad. El umbral queda fijado acá, antes de mirar las trazas;
     - cuánto ocupan, en resultados y en caracteres, en las respuestas de `buscar_nodos` y `ver_vecinos`: en las trazas de C1 a C5, sobre
       el grafo de cada una, que se declara, y en las de la medición 1, sobre el acumulado;
     - la regla que dice qué preguntas de N3 pasan por un hub, para la familia 5 (§3), se escribe con esta medición y se fija en N4.
  - **EV2 y las 20 de la tanda 0 se usan solo para este diagnóstico,** nunca para ajustar (regla 1 del §7).
- **N2. El diseño de las seis familias** del §3, con el relevamiento como antecedente.
- **N3. Las preguntas de desarrollo,** por una instancia aparte:
  - 30 preguntas, con gold por criterios y anclas en el molde de EV2;
  - las genera a ciegas una instancia aparte, solo desde los PDF, con registro de generación y el sha256 de cada PDF. No lee el grafo,
    las trazas, EV2, las preguntas de la tanda 0, el diseño de N2 ni nada de B6.3;
  - **sobre los 14 TOs del acumulado que no entran en las preguntas de B6.3** (`decisiones_153_mesa/unav/tos_de_N3_mesa.py`, en el
    paquete de la mesa). La fuente de cada uno es `data/experiment/esq/documentos_excluidos_evaluacion_final.json`:

    | TOs | Tanda | Fuente en el registro de excluidos |
    |---|---|---|
    | cap, cla, ext, pro, ric | 0 (desarrollo) | `regla`, punto (i): «los cinco del subset de desarrollo». No están en `documentos` |
    | ctacte, lingob, polcre, pagjub, docvig | 0 | `documentos`, origen «tanda 0 (preregistro_tanda0.md:65-66; L-ESQ-R2 4ef7650)» |
    | ayccef, expaef, opefci, adrei | 1 | `documentos`, origen «ESQ-2 (documentos_excluidos_esq.json)» |

    - Los otros 6 excluidos (actgar, cryl, ctacor, lavdin, prevmi y traval) no están en el acumulado y no entran;
  - **el generador se escribe para que sirva igual a las preguntas de B6.3** (cambio de la autora del 18/10/2026):
    - el mismo molde: el de EV2, con gold por anclas y criterios (`docs/diseno_ev2.md`, §5), y el procedimiento de las 20 de la tanda 0
      (`data/experiment/ev2_tanda0/preguntas/registro_generacion_tanda0.md:43-44`);
    - **la mezcla de tipos** (cambio de la v6). El tipo de cada pregunta se fija desde la norma, leyendo el PDF y sin mirar el grafo,
      antes de redactarla, y queda en el registro de generación:
      - **dato directo:** la respuesta está en un punto;
      - **varios puntos,** en cuatro subtipos: una remisión, una excepción en un hijo, una condición, y una definición en otro punto. Una
        de varios puntos exige contenido de dos puntos que no son subpuntos uno del otro;
      - **abstención:** el texto no fija lo que se pregunta, verificado en el PDF antes de redactarla;
    - las cuotas: al menos una por documento, al menos una de varios puntos por cada documento con dos unidades usables o más, y las
      abstenciones en la proporción de la tanda 0 (2 de 20). Cada subtipo de varios puntos, al menos 3 veces; si uno no llega, se
      declara y se completa con otro. Las demás, de dato directo;
    - solo cambian los TOs. El mandato de la generación de las preguntas de B6.3 lo reusa;
    - **las de cupo por necesidad van aparte,** cada una con la necesidad del §3 que la pide, y declaradas. No cuentan para la mezcla.
      Son 7, una por necesidad, con las 23 de la mezcla (decisión 8, (a));
    - **las 3 de ejemplo de la familia 6** van aparte, selladas aparte, y nunca se miden (decisión 10);
  - se sellan con su sha256 antes de que las lea esta unidad. Nunca EV2 ni B6.3, y nunca para evaluar;
  - la revisión cruza después sus anclas con las de EV2 y declara las coincidencias.
- **N4. El protocolo de medición** (§6). Se escribe en la parte 1 y **se sella después del diagnóstico de A2.2, antes de N6.** El
  diagnóstico puede sumar o sacar una candidata dentro de una familia del §3, y lo declara; las familias y las 8 configuraciones no
  cambian.
- **N5. La implementación de las seis familias,** que entran todas a N6, sobre una copia: las 1 a 5 en el módulo nuevo, con selftest, y
  la 6 como texto del bloque de herramientas del grafo, con sus 3 ejemplos (decisión 10). La parte común de la decisión 9 entra en la
  plantilla de los dos brazos en el mismo cambio, para que N6 corra con ella. Su commit va en la fila de las ejecutoras del repo, después del sello de la tanda final. En el mismo cambio:
  - **el cargador de Neo4j exporta las propiedades de las aristas** (decisión 6): las marcas de la cola, `no_verificada_e3`, la del sujeto
    derivado y `alcance` (hoy, solo `orden` y `provenances_json`; borrador, CONTEXTO);
  - **`cargar_neo4j_tanda0.py` deja de filtrar las claves por «KG_Tanda0_»** (`CLAVES_TANDA0`, `:55`, que usa `--grafo` en `:122`). Así el
    acumulado y el grafo evaluado se cargan sin envoltorios; hoy la tanda 1 se carga con uno en memoria;
  - **con su selftest y la paridad** cargador = Neo4j, en los grafos que ya están cargados (los re-sellados) y en el acumulado. Los
    sellados dan lo mismo que antes del cambio.

**Después de A2.2 (USD 0).**
- **N5b. El diagnóstico de A2.2,** sobre sus trazas, con las cuatro clases de N1. No vuelve a correr A2.2: A2.2 se mide una sola vez.
  Su FRENO y la lectura de la autora van antes del sello de N4.

**Lo pago, en el carril, en secuencia.**
- **N6. Las ablaciones** del protocolo sellado, en el brazo del grafo (§6) y en el de fragmentos (§6 bis), con el tope de la decisión 1.
  Va después de A2.2, de N5b y de N5, en el orden del carril que dé el calendario.

**Antes del corte.**
- **N7. El pre-registro de la configuración elegida** (herramientas, instrucciones, tope, índices y analizador), sellado con su sha256
  antes del corte del sábado 24/10 a las 12:00 y antes del pre-registro de B6.3, que lo declara. Lo que vale para fragmentos se aplica a
  ese brazo en el mismo pre-registro. Si los ejemplos de la familia 6 entran, el brazo de fragmentos lleva los mismos 3, resueltos con
  su herramienta, declarado (decisión 10).

## 5. El texto del prompt

- **Es la misma plantilla para los dos brazos** (`data/experiment/banco_mcp/agentes/plantilla_prompt.txt`). Solo cambia `{{BLOQUE_TOOLS}}`
  (`config_agentes.json`, «diferencia_entre_brazos»; el diff, en `agentes/resultados/diff_prompt_brazos.txt`). Los dos brazos de fragmentos
  de A2.1 usan la misma (`a2_1/config_agentes_a2_1.json`).
- **Hoy nombra los cinco TOs de desarrollo:** «(Textos Ordenados: capitales mínimos, clasificación de deudores, exterior y cambios,
  protección de usuarios de servicios financieros y régimen informativo contable mensual)».
- **El texto propuesto,** el mismo para los dos brazos, decidido sin mirar ninguna pregunta de B6.3 (la mesa no vio ninguna):
  > Sos un agente que responde preguntas sobre la normativa del BCRA (sus Textos Ordenados), usando EXCLUSIVAMENTE la evidencia que
  > recuperes con las tools disponibles en esta sesión.
  - Solo sale el paréntesis con los cinco nombres. Todo lo demás de la plantilla queda igual.
- **Decidido por la autora el 18/10/2026: va este texto, el mismo para los dos brazos, y entra antes de A2.2,** en la configuración común
  que fija su pre-registro: «lo común a los brazos: el agente, el modelo, la versión del CLI, el prompt con su diff entre brazos» (mandato
  de A2.1, §5, `:135`).
  - A2.2, N6 y B6.3 usan el mismo prompt;
  - el tramo 2 de A2.1 (H-B2 y la humo), que todavía no corrió, valida la plantilla nueva;
  - **el sha de la configuración sellada del banco (R10) cambia, y se declara** en el pre-registro de A2.2 y en el de B6.3.
  - Este mandato no cambia la plantilla de A2.2: el cambio del texto va con el tramo 2 de A2.1, en su despacho.
- **La parte común de la estrategia entra a la plantilla desde N6** (decisión 9): descomponer la pregunta y revisar las condiciones y las
  excepciones antes de responder.
  - Es la misma para los dos brazos, como el texto del prompt antes de A2.2, y no se mide aparte en ninguno: se declara que no se midió
    en fragmentos;
  - A2.2 corre sin ella; N6 y B6.3, con ella;
  - entra con N5, después de A2.2. El sha de la configuración sellada del banco (R10) cambia otra vez, y se declara en el pre-registro de
    B6.3.
- **La familia 6 del grafo** va en `{{BLOQUE_TOOLS}}` del brazo del grafo: sus ejemplos y las instrucciones de sus herramientas.

## 6. El protocolo de N4 y su costo

- **El grafo de N6** (decisión 5): el acumulado de las tandas 0 y 1 sin cola, sellado con los commits de T3.
- **Las configuraciones** (decisión 3): 8, la base, todas, y todas menos una familia, por cada una de las seis del §3. La base se repite
  para medir la variación entre corridas (decisión 4). Todas llevan la parte común de la plantilla (decisión 9).
- **Lo que se mide** (como en el borrador): fidelidad por criterio, precisión de citas, costo por pregunta, llamadas y respuestas al tope,
  y las cuatro clases de N1 sobre las fallas, con lo verificado y lo no verificado aparte.
- **La regla de decisión,** escrita antes de medir (cambio de la autora del 18/10/2026):
  - se elige la configuración de mayor fidelidad por criterio entre las medidas, con la comparación pareada por pregunta;
  - **por familia** (cambio de la v6): cada familia se informa también en las preguntas de su necesidad (§3). «Todas menos una familia»
    solo es elegible si, en las preguntas de la necesidad de esa familia, no baja la fidelidad por criterio frente a «todas» más que la
    variación entre corridas de la base. Así ninguna familia se descarta porque otra la compensa en el total;
  - si dos quedan dentro de la variación entre corridas de la base, gana la que llega menos veces al tope de llamadas, y después la más
    barata;
  - la configuración que se pre-registre tiene que pasar el caso obligatorio de la jerarquía, como antes.
  - La regla de la híbrida en el brazo de fragmentos (§6 bis) no cambia.
- **El costo:**
  - el agente, con el R9 medido en el brazo del grafo del banco: USD 0,0571 por sesión de media, de 0,0363 a 0,0785, en las 4
    sesiones de pregunta de la fase B;
  - el alto, 2 veces el máximo, porque las herramientas nuevas devuelven más texto (NO VERIFICADO). Las salidas compactas de la v6 no
    lo bajan en esta cuenta;
  - el juez, el de EV2: USD 0,0126 por llamada y 3 llamadas por respuesta;
  - fuente: `decisiones_152_mesa/costo_n6/costo_N6_mesa.py` y su salida, en el paquete de la mesa; las 8 configuraciones de la v6, con
    `decisiones_166_mesa/unav/costo_N6_v6_mesa.py`.

| Opción | Corridas | Central (USD) | Alto (USD) |
|---|---:|---:|---:|
| A: 6 familias (8 configuraciones), la base 3 veces, 30 preguntas | 300 | 28,49 | 58,45 |
| B: la base 2 veces | 270 | 25,64 | 52,61 |
| C: 20 preguntas | 200 | 19,00 | 38,97 |

- **Rige la A** (decisión 3). Las opciones D a F de la v5 (4 familias) salen: la v6 trae seis.

## 6 bis. La híbrida en el brazo de fragmentos se mide

- **Lo que se mide** (F1, decisión 7): en el brazo de fragmentos y sobre N3, la configuración BM25 de A2.2, repetida 3 veces, contra la
  misma con la forma de fragmentos de la familia 1: la híbrida (BM25 más el denso), con los filtros por TO y por punto, como en el grafo.
  Las dos configuraciones de F1 llevan la parte común de la plantilla (decisión 9), así que F1 mide solo la híbrida. El denso no cambia,
  así que no se mide contra la híbrida.
- **La regla:** la híbrida entra a ese brazo solo si no le baja la fidelidad por criterio más que la variación entre corridas de su base.
  Si no, el brazo queda con su búsqueda de A2.2, y se declara.
- **El sistema por fragmentos tiene dos configuraciones principales,** BM25 y denso, que difieren solo en la afinidad, con Holm sobre las
  dos comparaciones (mandato de A2.1, `:12-14`; D1 del 07/10/2026; laudo 2 del 20/09/2026). Si la híbrida pasa, reemplaza a BM25 y el
  denso queda: siguen dos comparaciones principales con Holm (decisión 7, (a)).
- **El costo,** con el R9 medido en el brazo vectorial del banco (USD 0,0419 por sesión de media, de 0,0248 a 0,0787; alto, 0,1575) y el
  juez de EV2 aparte (0,0379 por respuesta). Fuente: `decisiones_153_mesa/unav/costo_N6_fragmentos_mesa.py` y su salida.

| Opción | Corridas | Fragmentos, central | Fragmentos, alto | N6 entero, central | N6 entero, alto |
|---|---:|---:|---:|---:|---:|
| F1: una configuración de A2.2 (3 veces) contra la misma con la híbrida | 120 | 9,58 | 23,44 | 38,07 | 81,89 |
| F2: BM25 y denso (3 veces cada una) contra la híbrida | 210 | 16,76 | 41,02 | 45,25 | 99,47 |

- **Decidido: F1, sobre BM25** (decisión 7). La fila de F2 queda como referencia.
- **El total contra 341** (`decisiones_153_mesa/unav/salida_presupuesto_v9_F1.md`): central USD 334,18, 6,82 por debajo, con GraphRAG
  adentro; alto, 443,30. Con F2 eran 341,36 y 460,88 (`_F2.md`).
- **El tope de N6, entero** (decisión 1): USD 85, con freno en 64. Con la decisión 9 como la tomó la autora, las cifras de esta sección
  no cambian.

## 7. Las reglas

1. **El ajuste se hace solo con N3,** nunca con las preguntas de B6.3 ni con EV2.
2. **A2.2 se mide una sola vez.** El diagnóstico (N5b) lee sus trazas y no la vuelve a correr.
3. **Lo que mejora la búsqueda se aplica igual al sistema por fragmentos,** si pasa su medición en ese brazo (§6 bis); lo propio de la
   navegación por aristas, y el índice del TO (familia 4), quedan como diferencia declarada entre los brazos. La parte común de la
   estrategia va a los dos brazos por la plantilla, sin medirla aparte (decisión 9), y los ejemplos de la familia 6, si entran, van a los
   dos (decisión 10).
4. **N6 y N5b no se recortan.** Si el total proyectado pasa de USD 341, sale primero GraphRAG y después lo GC.
5. **El cegamiento por U-MED-VERIF** (cambio de la autora del 18/10/2026): todo FRENO, traza o material de esta unidad que muestre
   contenido de una extracción de la tanda 1 sigue la regla del §7 bis de U-PROC-HERENCIA, con la exclusión de las FICHAS (mandato firmado
   de U-MED-VERIF-FICHAS, `c0d3ab17`, §3):
   - ninguna cifra ni lista por estado de E3 ni de los reintentos de E3;
   - un nodo de la tanda 1 va con su unidad, su código (los primeros 12 caracteres del sha256 de su id), su punto y su rol, sin el label,
     la descripción ni el tramo;
   - antes de mostrar contenido de una extracción de la tanda 1, la regla de exclusión de las FICHAS: si la muestra no está sorteada, esas
     unidades entran a la lista de exclusión antes del sorteo; si ya lo está, el caso de una unidad de la muestra espera a que cierre la
     lectura de U-MED-VERIF;
   - vale para N1 a N7 y para la revisión de la mesa;
   - en la medición 4 de N1, un hub de la tanda 1 va con su código, nunca con su label.

## 8. Las decisiones de la autora al firmar

Las siete primeras las eligió la autora el 18/10/2026: las seis primeras, con las recomendaciones de la v2 (recibido a las 10:31:44), y
la 7, con la recomendación de la v3 y la medición F1 (recibido a las 10:45:54). La 8 la trajo la v5, y la autora eligió la (a) el
18/10/2026 (recibido a las 17:34:23); el mismo mensaje cambió la 3. La 9 y la 10 las trajo la v6, y la autora las tomó al firmar
(recibido a las 18:18:43). Se firman con este mandato.

1. **El tope de N6:** USD 60 con freno en 45 para el grafo. **Con la medición en fragmentos** (F1, §6 bis), USD 85 en total, con freno
   en 64.
2. **El tamaño de N3:** 30 preguntas, con cupos por necesidad.
3. **Las configuraciones:** las seis familias del §3 y 8 configuraciones (la base, todas, y todas menos una familia), la opción A, con el
   mismo tope de la decisión 1 (cambio de la autora del 18/10/2026, recibido a las 17:34:23). Una candidata nueva de N2 entra en su
   familia y no suma configuraciones.
4. **Las repeticiones de la base:** 3, en el grafo y en fragmentos.
5. **El grafo de N6:** el acumulado de las tandas 0 y 1 sin cola, sellado con los commits de T3. N3 va sobre sus 14 TOs excluidos de B6.3.
6. **Las propiedades de las aristas en Neo4j:** sí, con las marcas y con `alcance`, en el mismo cambio que saca el filtro «KG_Tanda0_» del
   cargador (N5).
7. **Qué reemplaza la híbrida en el brazo de fragmentos, si pasa** (§6 bis). Toca D1 del 07/10/2026 y el laudo 2, que fijan dos
   configuraciones principales con Holm:
   - (a) **la híbrida reemplaza a BM25,** la configuración que se aparea con el grafo para aislar la representación, y el denso queda.
     Siguen dos comparaciones con Holm. Alcanza F1 sobre BM25: el denso no cambia, así que no se mide contra la híbrida;
   - (b) la híbrida se suma como tercera configuración: tres comparaciones con Holm, y el N de B6.3 cambia;
   - (c) la híbrida reemplaza a las dos: queda una sola comparación, y D1 cambia.
   - En cualquiera, si el grafo no pasa a la híbrida en N7, el brazo de fragmentos queda como en A2.2.
   - **Decidido: (a),** con F1 sobre BM25 (la autora, el 18/10/2026; recibido a las 10:45:54). El tope de N6 entero queda en USD 85 con
     freno en 64, y GraphRAG sigue adentro (total central 334,18).
8. **Las de cupo por necesidad, en las 30 de N3** (§4):
   - **(a)** 7 de cupo, una por cada necesidad de las filas 1 a 7 de la v5, y 23 con el molde y la mezcla. Las 23, sobre los 14 TOs: al
     menos una por TO, al menos una de varios puntos por cada TO con dos unidades usables o más, y 2 abstenciones;
   - **(b)** las 30 con el molde y la mezcla, sin cupo: las necesidades se miden solo en las que las toquen;
   - **Decidido: (a)** (la autora, el 18/10/2026; recibido a las 17:34:23). Las 7 necesidades y la familia de cada una van en el §3
     (columna «Preguntas de su necesidad en N3»); las familias 5 y 6 toman las suyas de la mezcla.
9. **La parte de la familia 6 que vale para fragmentos** (descomponer la pregunta y revisar las condiciones y las excepciones). La v6
   proponía tres opciones (fuente de las cifras: `decisiones_166_mesa/unav/costo_N6_v6_mesa.py` y su salida):
   - **(a)** se mide aparte en ese brazo: F1 más una configuración, BM25 con esa parte, una vez (150 corridas en fragmentos). N6 entero,
     central USD 40,46 y alto 87,75, que pasa el tope de 85; el total contra 341, central 336,57;
   - **(b)** no se mide en fragmentos: queda como diferencia declarada entre los brazos, y las cifras del §6 bis no cambian;
   - **(c)** va con la híbrida en la configuración que F1 compara. Si pasa la regla del §6 bis, las dos entran al brazo de fragmentos; si
     no, el brazo queda como en A2.2 y la parte queda como diferencia declarada. Las cifras del §6 bis no cambian. No separa el efecto
     de cada una, y se declara;
   - en la (a) y la (c), si entra, va a las dos configuraciones principales del brazo, para que sigan difiriendo solo en la afinidad (D1);
   - la v6 recomendaba la (c): tiene el mismo costo y el mismo tope, y evita una diferencia de estrategia entre los brazos de B6.3 cada
     vez que no le baja la fidelidad al de fragmentos. La (a) separa los efectos, pero su alto pasa el tope de N6, que no se recorta
     (regla 4);
   - **Decidido: ninguna de las tres** (la autora, el 18/10/2026; recibido a las 18:18:43), tal cual: «Ninguna de las tres: la parte de la familia 6 que vale para los dos brazos (descomponer la pregunta y revisar las condiciones y las excepciones antes de responder) va a la plantilla común de los dos brazos desde N6, decidida ahora y sin medirla aparte, como el texto del prompt antes de A2.2 (§5: la plantilla es la misma y solo cambia el bloque de herramientas). F1 compara BM25 contra BM25 con la híbrida, las dos con esa parte, así que mide solo la híbrida. La familia 6 del grafo queda con lo propio del grafo: los ejemplos de navegación y las instrucciones de sus herramientas. Se declara que esa parte no se midió en fragmentos. El costo no cambia.»
10. **De dónde salen los ejemplos de la familia 6** (de N3; la v6 decía de 2 a 3):
    - **(a)** N3 genera 3 preguntas más, solo de ejemplo, con el mismo generador y selladas aparte. Nunca se miden, y las 30 quedan para
      medir. USD 0;
    - **(b)** salen de las 30, y esas no se miden en N6: quedan 27 o 28, y se declara;
    - la v6 recomendaba la (a): un ejemplo que se mide le muestra al agente la navegación de esa misma pregunta, y la (b) achica el N y
      puede dejar sin pregunta el cupo de una necesidad;
    - **Decidido: (a)** (la autora, el 18/10/2026; recibido a las 18:18:43), tal cual: «La (a): 3 preguntas más en N3, solo de ejemplo, nunca medidas. Si los ejemplos entran a la configuración del grafo en N7, el brazo de fragmentos lleva los mismos 3 ejemplos resueltos con su herramienta, declarado, para que ningún brazo tenga ejemplos que el otro no tiene.»
    - Como N3 genera 3, la familia 6 usa los 3, y el brazo de fragmentos, si entran, los mismos 3.

## 9. Escrituras, prohibiciones y requisitos

- **Escrituras:**
  - parte 1: fuera del repo, en su carpeta, y el paquete de revisión;
  - la instancia de N3, solo su carpeta, con las 30 y las 3 de ejemplo (decisión 10);
  - N5: el módulo nuevo del servidor y su selftest, sobre una copia, y su commit en la fila;
  - N6: en el carril pago, con su carpeta nueva en el banco.
- **Prohibido:**
  - el cuarteto sellado de evaluación, las trazas, los eval sets y los grafos sellados;
  - usar EV2 o material de B6.3 para ajustar;
  - usar N3 para evaluar;
  - correr algo pago en paralelo con una extracción;
  - commitear y la memoria.
- **Requisitos:**
  - CLAUDE.md §4, de a a l;
  - copias sin enlaces y sin `.env` ni `NO_ABRIR_`;
  - el cegamiento de la regla 5 del §7;
  - la cláusula v2 de las carpetas vedadas (registro, §31), con `lectura_calibradores_desamb/`;
  - los heredocs, con el delimitador entre comillas;
  - toda cifra del FRENO, por script desde sus archivos;
  - cero nombres de personas.
- **FRENO** al final de N1 a N4, de N5, de N5b, de N6 y de N7, cada uno con su revisión de la mesa.

## Firma

**FIRMADO por la autora el 18/10/2026,** por mensaje recibido a las 18:18:43 (hoja de ruta de la mesa, §168): «U-NAV-DISENO: firmo la v6
(decisiones_166_mesa/unav/UNAV_DISENO_navegacion_agente_v6_PARA_FIRMAR.md), con el mínimo de 3 por subtipo de varios puntos que
agregaste, y con las decisiones 9 y 10 así:» (las dos van tal cual en el §8). El texto firmado es el de la v6 (sha256
`998ba8fc27e3ffa0f0ced023be117980e236d092c5fffc58d5e6d36b53d2ee41`), con las dos decisiones aplicadas donde tocan el texto, con este encabezado y esta
sección.
