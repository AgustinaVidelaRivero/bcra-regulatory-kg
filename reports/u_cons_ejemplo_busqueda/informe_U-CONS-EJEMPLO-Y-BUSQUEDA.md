# U-CONS-EJEMPLO-Y-BUSQUEDA — informe de la consulta

Hice solo lectura. No escribí en el repositorio, a Neo4j le hice solo consultas de lectura y no usé API ni modelos. `.pyc` sigue en 2.213. En `git status` aparecen `ev2_tanda0/trazas/` y `ev2_tanda0/juez_out/`: son salidas de E5.b, que está en curso, no mías.

**Lo principal, antes del detalle:**
- El 5.1.1.1 sirve como ejemplo en r1. En el grafo del esquema congelado no: ahí sus dos condiciones quedan como nodos sueltos y no hay arista de remisión al 3.7.
- Las dos causas son sistemáticas, no propias de este punto. Están en la sección A3.
- Ni el plan ni sus laudos fijan cómo analiza el texto el BM25 del sistema por fragmentos (A2.1). El índice del grafo en Neo4j usa el analizador `spanish`, que reduce a la raíz y quita palabras vacías.

---

## A1 — Qué responde a la pregunta, según el corpus congelado

Fuente: `data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_cla.json`.

**Contexto que hereda el 5.1.1.1:**
> Sección 5. Categorías de carteras. / 5.1. Categorías. La cartera se agrupará en dos categorías básicas: / 5.1.1. Cartera comercial. Abarca todas las financiaciones comprendidas, con excepción de las siguientes:

**`cla::5.1.1.1`**, que es el punto que responde la pregunta:
> 5.1.1.1. Los créditos para consumo o vivienda. Los créditos de esta clase que superen el equivalente a dos veces el importe de referencia establecido en el punto 3.7. y cuyo repago no se encuentre vinculado a ingresos fijos o periódicos del cliente sino a la evolución de su actividad productiva o comercial se incluirán dentro de la cartera comercial.

**`cla::3.7`:**
> 3.7. Importe de referencia. El importe a considerar será el nivel máximo del valor de ventas totales anuales para la categoría "Micro" correspondiente al sector "Comercio" que determine la autoridad de aplicación de la Ley 24.467 (y sus modificatorias).

**`cla::5.1.1.2`**, la opción de la entidad:
> 5.1.1.2. A opción de la entidad, las financiaciones de naturaleza comercial de hasta el equivalente a dos veces el importe de referencia establecido en el punto 3.7., cuenten o no con garantías preferidas, podrán agruparse junto con los créditos para consumo o vivienda, en cuyo caso recibirán el tratamiento previsto para estos últimos. Cuando el cliente mantenga financiaciones por ambos conceptos, los créditos para consumo o vivienda se sumarán a los de la cartera comercial para determinar su encuadramiento en una o en otra cartera en función del importe indicado, a cuyo fin los créditos con garantías preferidas se ponderarán al 50 %. De ejercerse, esta opción deberá aplicarse con carácter general a toda la cartera y encontrarse prevista en el "Manual de procedimientos de clasificación y previsión" y sólo podrá cambiarse con un preaviso de 6 meses a la Superintendencia de Entidades Financieras y Cambiarias (SEFyC).

**`cla::5.1.2.4`**, dentro de 5.1.2 («Comprende:»):
> 5.1.2.4. Las financiaciones de naturaleza comercial de hasta el equivalente a dos veces el importe de referencia establecido en el punto 3.7., cuenten o no con garantías preferidas, cuando la entidad haya optado por ello.

**`cla::3.3.3`**, dentro de 3.3, que abre con «Se volcarán en un "Manual de procedimientos de clasificación y previsión":»:
> 3.3.3. El ejercicio de la opción de agrupar las financiaciones de naturaleza comercial de hasta el equivalente a dos veces el importe de referencia establecido en el punto 3.7., cuenten o no con garantías preferidas, junto con los créditos para consumo o vivienda.

**Otros puntos del alcance:**
- **Qué financiaciones abarca 5.1.1:** las «financiaciones comprendidas», que define la Sección 2, «Financiaciones comprendidas», punto 2.1, «Conceptos incluidos». Tomé solo el encabezado.
- **`cla::10.1`**, para otros sujetos: los proveedores no financieros de crédito «deberán clasificar a los respectivos deudores en función de su mora, según los criterios aplicables para la cartera de "consumo o vivienda"».

**Qué necesita una respuesta completa.** Hechos del texto:
1. Las dos condiciones del 5.1.1.1 son conjuntivas: el monto supera dos veces el importe de referencia, y el repago no depende de ingresos fijos o periódicos sino de la actividad productiva o comercial.
2. El importe de referencia se define por remisión a una autoridad externa (Ley 24.467). El monto en pesos no está en el corpus.
3. El segundo párrafo del 5.1.1.2 establece otra regla de encuadramiento por suma, con ponderación del 50 % para las garantías preferidas.

**Opinión.** Ese segundo párrafo del 5.1.1.2 puede llevar créditos de consumo o vivienda a la cartera comercial por una vía distinta del 5.1.1.1: si la entidad ejerció la opción y el cliente tiene ambos tipos, decide la suma. Que ese párrafo rija solo con la opción ejercida es una lectura. Está dentro del 5.1.1.2, y el párrafo siguiente empieza «De ejercerse, esta opción…».

## A2 — ¿La pregunta tiene un problema como el de la Figura 1.2?

Esta sección es opinión.

No tiene el problema del 3.17.1.4. El 5.1.1.1 es la regla general de la división en carteras, no un régimen especial, y la pregunta no pide nada que el punto no dé.

Tiene dos riesgos menores:
1. **La vía de la opción.** «¿Cuándo… tienen que incluirse?» deja afuera la vía del 5.1.1.2, que depende de una opción de la entidad. Una respuesta que cite solo el 5.1.1.1 puede juzgarse completa o incompleta según cómo se escriba el gold.
2. **El vocabulario.** La pregunta usa las palabras de la norma («créditos para consumo o vivienda», «cartera comercial»), así que favorece a cualquier búsqueda léxica. Eso se conecta con B5.

**Redacciones posibles, sin cambiar el punto de origen:**
- **(a)** «Para una entidad financiera, ¿qué condiciones hacen que un crédito para consumo o vivienda deba clasificarse en la cartera comercial?» El gold lleva los dos criterios del 5.1.1.1, más la definición del 3.7 como tercero si se quiere.
- **(b)** La misma pregunta, con un criterio adicional en el gold para la vía de la opción del 5.1.1.2.

Elegir entre (a) y (b) es decisión de la autora.

## A3 — El grafo del esquema congelado y r1

### KG-Tanda0-Desarrollo-r1

| Dato | Valor |
|---|---|
| Ruta | `data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo/r1/kg.json` |
| sha256 | `eab2fdd01dec4dad026d596a793919e666920fab127d7efb14b5b00857ae64ef` |
| Tamaño | 6.378 nodos / 15.007 aristas |
| Documentos | capitales mínimos, clasificación de deudores, exterior y cambios, protección de usuarios, régimen informativo contable mensual |
| Remisiones entre puntos | resueltas: 4.256 aristas `referencia` con `rol_fuente` `referencia_cruzada` |
| Neo4j | label `KG_Tanda0_Desarrollo_r1`, índice `nodos_fulltext_kg_tanda0_desarrollo_r1`, entrada en `data/experiment/neo4j/grafos.py` con `commit_sellado` `1b8916c`; índice ONLINE según la consulta de B2 |

**`cla::5.1.1.1` da cuatro nodos:**

| Tipo | Etiqueta | Aristas |
|---|---|---|
| Condicion | «Monto supera dos veces importe referencia 3.7» | **ninguna** |
| Condicion | «Repago vinculado a actividad productiva/comercial» | **ninguna** |
| Definicion | «Cartera comercial — créditos consumo/vivienda» | solo `establecida_en` hacia el TextoOrdenado |
| Operacion | «Clasificación de crédito en cartera comercial» | `aplica_a` hacia `Sujeto_rol_obligado_a_clasificar_clasificacion` y `establecida_en` |

**`cla::3.7` da un nodo:** la Definicion «Importe de referencia», con `establecida_en` y 12 aristas `referencia` entrantes. Vienen de los puntos 3.3.3, 3.4.2, 3.5.2, 5.1.1.2, 5.1.2.3 (dos), 5.1.2.4, 6.3.2 (dos), 6.4 y 6.5.5.9 (dos).

**No hay ninguna arista de remisión del 5.1.1.1 al 3.7.**

**Las dos causas, verificadas:**
1. **E1 rechazó las aristas de las condiciones.** En `corpus_tanda0/salida_dirigida/cla/extracciones_e1.jsonl`, el extractor emitió `e2 condicion_de e4` y `e3 condicion_de e4`, las dos de Condicion a Operacion. El validador las rechazó por `firma_invalida`. La matriz congelada admite `condicion_de` solo de Condicion a {Excepcion, Obligacion, Restriccion}; es `DOMAIN_RANGE_CONGELADO` en `data/experiment/esq/code/prompt_congelado.py`, y el prompt congelado dice lo mismo.
2. **El resolvedor de remisiones no parte de los tipos nuevos.** Solo usa como origen los tipos del esquema v2: `TIPOS_ORIGEN = ("Obligacion", "Restriccion", "Excepcion", "Operacion")` en `data/experiment/reextraccion_v2/corpus_v2/r1_referencias.py:51`, aplicado en `:243`. En el grafo, 0 aristas `referencia` salen de Condicion, Potestad o Definicion.

**Alcance, recontado:**

| Medida | Valor |
|---|---|
| Rechazos por firma inválida en E1 de la tanda 0, diez TOs | 982 |
| de ellos, Condicion `condicion_de` Operacion | 424 |
| de ellos, Condicion `condicion_de` Potestad | 231 |
| Condiciones en KG-Tanda0-Desarrollo-r1 | 1.178 |
| Aristas `condicion_de` | 448 |
| Condiciones sin ninguna arista | 35 |

### KG-Reextraído-r1

`data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json`, sha256 `0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a`.

**`cla::5.1.1.1` da tres nodos:**
- la Operacion «Inclusión en cartera comercial — créditos consumo/vivienda»;
- la Restriccion «Créditos consumo/vivienda — monto supera dos veces importe referencia», que tiene `limita` hacia la Operacion y **`referencia` hacia la Obligacion del 3.7**, «Considerar importe de referencia — ventas anuales Micro Comercio»;
- la Restriccion «Crédito — repago no vinculado a ingresos fijos, vinculado a actividad productiva», con `limita` hacia la Operacion.

**`cla::3.7`** es esa Obligacion. Tiene `aplica_a` hacia `Sujeto_rol_obligado_a_clasificar_clasificacion` y 14 `referencia` entrantes, entre ellas la del 5.1.1.1.

**Opinión.** El ejemplo funciona en r1 y no en el grafo del esquema congelado. Ahí un agente que llegue a la Operacion del 5.1.1.1 no ve las condiciones ni la remisión al 3.7. Las dos causas afectan a toda la tanda 0 y conviene llevarlas a la lectura de E6 y al backlog de r2.

## A4 — De qué grafo salen las figuras, y el tipo Sujeto

- **Regla sobre de qué grafo salen las figuras: NO ENCONTRADO** en el plan. `docs/plan_tesis.md:771` dice solo «figuras y esquemas del grafo y del pipeline en cada capítulo donde aporten». La fila U-FIG (`:783`) nombra los generadores. El de la Figura 1.2 usa r1 (`docs/tesis/figuras/generar_figura_fragmentos_vs_grafo.py:51-65`).
- **El esquema congelado no tiene tipo Sujeto.** Sus nueve tipos son Comunicacion, TextoOrdenado, Operacion, Restriccion, Excepcion, Obligacion, Potestad, Condicion y Definicion (`ENTITY_TYPES_CONGELADO`).
- **Cómo representa a quién se aplica un punto:** con los predicados `aplica_a` y `ejecuta` hacia un sujeto del catálogo v3. En la firma, ese extremo se pasa como el pseudo-tipo «Sujeto» (`prompt_congelado.py:102-105`). En el grafo son nodos de tipo Sujeto con ids del catálogo y nivel clase, instancia, rol o propuesto: son 124 en KG-Tanda0-Desarrollo-r1. En el 5.1.1.1 es `aplica_a` hacia `Sujeto_rol_obligado_a_clasificar_clasificacion`.

## B1 — El BM25 del sistema por fragmentos (A2.1)

**Lo que fija el plan** (`docs/plan_tesis.md:328`, fila A2.1):
- BM25 sobre los chunks de E0, con unidades estructurales y herencia;
- top-k = 5;
- el mismo agente en los dos sistemas, con una sola herramienta de recuperación.

El laudo 2 del 20/09, en esa misma fila, agrega dos configuraciones que difieren solo en la afinidad: BM25 como comparación principal y el modelo denso `harrier-oss-v1-0.6b` como secundaria. D-h2 (`:975`) las lleva a B6.3 (f), y P-2 (`:1248`) las repite.

**Tokenizador, reducción a la raíz, palabras vacías y tildes: NO ENCONTRADO** en el plan ni en los laudos. A2.1 figura `[ ]`: su pre-registro no está sellado.

**Código del BM25 de A2.1: NO ENCONTRADO.**
- El banco `data/experiment/banco_mcp/` tiene solo `mcp_kg/` y `mcp_vector/`, que es el denso. Este último arma los pasajes de E0 con herencia (`mcp_vector/construir_indice.py:7-9`, `:54`).
- El único BM25 sobre fragmentos del repo es la réplica del bake-off (`data/experiment/bakeoff_embeddings/code/e3_medicion.py:51-90`): minúsculas, sin tildes, separación por no alfanuméricos, sin reducción a la raíz ni palabras vacías, k1 = 1,2 y b = 0,75. No está declarado como A2.1.

**Dato que corrige mi revisión anterior.** El panel «Recuperación por fragmentos» de la Figura 1.2 no sale de fragmentos. Sale de la búsqueda full-text de Neo4j sobre los nodos de r1, con el índice `nodos_fulltext_kg_reextraido_r1` y límite 10 (`generar_figura_fragmentos_vs_grafo.py:51-65`). El BM25 sobre chunks que corrí en esa revisión era una aproximación mía, no el sistema de la figura.

## B2 — El índice full-text de Neo4j

- **Laudo A1.6:** `docs/laudo_promocion_backend.md:14` fija el modo `fulltext` con Lucene/BM25, analizador `spanish`, sobre label, descripción e id.
- **Código:** `data/experiment/neo4j/indices.py`.
  - **Campos y analizador:** `:77-78`, `CAMPOS_FULLTEXT = ["label", "descripcion", "description", "id_texto"]` y `ANALYZER = "spanish"`.
  - **Creación:** `:95-97`, `CREATE FULLTEXT INDEX … OPTIONS {indexConfig: {`fulltext.analyzer`: 'spanish'}}`.
  - **Nombre del índice:** sale de la entrada del grafo en `grafos.py` (`:85-86`).
  - **Por qué `spanish`:** el comentario de `:35-37` dice que reduce a la raíz y quita palabras vacías castellanas, y que el analizador por defecto no reduce, así que «asociación mutual» no encontraría «asociaciones mutuales».
- **Consulta de solo lectura:**

```
SHOW FULLTEXT INDEXES YIELD name, state, labelsOrTypes, properties, options RETURN name, state, labelsOrTypes, properties, options.indexConfig.`fulltext.analyzer` AS analyzer ORDER BY name
```
```
nodos_fulltext_kg_reextraido | ONLINE | ['KG_Reextraido'] | ['label', 'descripcion', 'description', 'id_texto'] | analyzer=spanish
nodos_fulltext_kg_reextraido_r1 | ONLINE | ['KG_Reextraido_r1'] | ['label', 'descripcion', 'description', 'id_texto'] | analyzer=spanish
nodos_fulltext_kg_refinado | ONLINE | ['KG_Refinado'] | ['label', 'descripcion', 'description', 'id_texto'] | analyzer=spanish
nodos_fulltext_kg_tanda0_desarrollo_r1 | ONLINE | ['KG_Tanda0_Desarrollo_r1'] | ['label', 'descripcion', 'description', 'id_texto'] | analyzer=spanish
nodos_fulltext_kg_tanda0_diez_r1 | ONLINE | ['KG_Tanda0_Diez_r1'] | ['label', 'descripcion', 'description', 'id_texto'] | analyzer=spanish
```

## B3 — El índice en memoria de EV2 (GraphIndex)

Fuente: `data/experiment/evaluacion/harness.py`.
- **Tildes:** quita diacríticos con NFKD (`:98-100`).
- **Tokenización:** minúsculas y `[a-z0-9]+` (`:103`, `:106-107`).
- **Qué indexa:** la etiqueta y el id de cada nodo, no la descripción (`:136-139`).
- **Puntaje:** cantidad de tokens compartidos entre la consulta y el nodo, sin pesos. Desempata por largo de la etiqueta y después por id (`:148-157`).
- **Sin reducción a la raíz y sin palabras vacías.** El plan lo describe igual en `docs/plan_tesis.md:822`.

## B4 — ¿Se exige el mismo análisis de texto en las dos búsquedas?

**NO ENCONTRADO**, en ninguno de estos lugares:
- el plan;
- `docs/cola_mejoras_diferidas.md`, donde busqué analizador, reducción a la raíz, BM25, léxico y tokenización sin resultados;
- el pre-registro de B6.3, que no existe todavía en `docs/`.

**Registros relacionados, que no son esa exigencia:**
- `:822`: cada tabla de resultados declara qué índice de texto usó, y el grafo de B6.3 va sobre Neo4j por el laudo A1.6 §3.
- `:328` (a): hay una predicción de la asimetría entre texto crudo y representación comprimida.

**Opinión.** El grafo busca con `spanish` y el sistema por fragmentos todavía no tiene analizador fijado. La réplica del bake-off, sin reducción a la raíz, es la que no encontró «créditos» con «crédito». Si en B6.3 (f) los dos brazos analizan distinto el texto, la comparación mezcla dos efectos. El pre-registro de A2.1 y B6.3 debería fijar el mismo analizador, o declarar la diferencia.

## B5 — Con qué vocabulario se redactan las preguntas de la medición final

- **B6.3 (a)** (`docs/plan_tesis.md:745`) pide «preguntas nuevas con gold por criterios, selladas antes de correr», sobre documentos disjuntos. **Sobre usar el vocabulario de la norma o el del usuario: NO ENCONTRADO.**
- **La única regla escrita** es la del procedimiento de EV2 (`data/experiment/exploracion/ev2_fidelidad/registro_generacion_ev2_fidelidad.md:61-65`): «UNA pregunta natural de usuario profesional, auto-contenida, sin números de punto en el texto de la pregunta». Las preguntas de la tanda 0 se generaron con ese procedimiento, según la fila B6.0 fase 2b.
- **Lo pendiente para B6.3 (a)** es la cuota de tipos de pregunta, que decide la autora. No dice nada del vocabulario.

FRENO.
