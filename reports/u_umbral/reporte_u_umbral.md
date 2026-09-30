# U-UMBRAL — Opciones para modelar umbrales: evidencia en dos ejes

Reporte final de la unidad U-UMBRAL (plan, fila B2.11, unidad 3; mandato
`docs/mandatos/UUMBRAL_investigacion.md`, firmado en `30f106c`, con las precisiones
de la autora al aprobar U1 en `e81ed69`). Lo escribí el 30/09/2026. USD 0: sin API
y sin Neo4j.

**Qué es y qué no es.** Ordena la evidencia de U1 y U2 en dos decisiones
separadas (principio 11, `docs/plan_tesis.md:298`): **dónde vive el umbral**
(esquema) y **cómo se llena** (pipeline). La unidad mide y propone; no decide. La
elección es de la autora y va a L-ESQ-R2 (plan, B2.11, unidad 5). EV2 y las trazas
de C3 y C4 son material de desarrollo: la medición 5 es un diagnóstico, no un
resultado (principio 7). Ningún texto se leyó para juzgarlo: la planilla de la
medición 4 está sellada y sin leer.

## 0. Fuentes y comandos

Todas las cifras salen de dos comandos, desde la raíz del repo:

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_umbral/u_umbral_u1.py
```

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_umbral/u_umbral_u2.py
```

Abajo, `[U1: clave]` y `[U2: clave]` remiten a `u1_mediciones.json` y
`u2_muestra_trazas.json`. Salvo que diga otro grafo, las cifras son de
KG-Tanda0-Desarrollo-r1 (`eab2fdd0…`). Las de r1 (`0226e947…`) y diez
(`dd42d6d9…`) están en los mismos JSON.

El tool schema y las líneas del prefijo vigente (`v3_b54`) que cito como
«prefijo, línea N» los obtengo por import, sin editar nada. El comando imprime:
- las claves de `relations`;
- su `additionalProperties`;
- el tipo de las properties de `entities`;
- las líneas 22, 25, 28, 40, 263 y 269 del texto del prefijo.

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B -c "
import sys; sys.path.insert(0,'data/experiment/reextraccion_v2/e1_extractor'); import perfil_e1; perfil_e1.perfil('v3_b54'); import prompt_v3_b54 as v
s=v.TOOL_SCHEMA_V3['input_schema']['properties']; r=s['relations']['items']; e=s['entities']['items']['properties']['properties']
print(sorted(r['properties']), r['additionalProperties'], e['additionalProperties'])
L=v.PREFIJO_SISTEMA_V3.split('\n'); print([L[i-1][:60] for i in (22,25,28,40,263,269)])"
```

**Corrección de U1 sobre [c14].** En U1 atribuí al «€» la diferencia de un nodo
entre la prosa de [c14] y el total del tablero. Ese diagnóstico fue erróneo. La
diferencia es la cifra entre paréntesis del plazo: «diez (10) años», la Obligacion
de `pro::3.1.3`. La variante c14_eur llega al mismo total por coincidencia, porque
suma otro nodo, el de `cap::2.8.3.3`. Con la cifra entre paréntesis, el comando
siguiente da 287 de 606 en desarrollo, 218 de 639 en r1 y 323 de 683 en diez:

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B -c "
import sys,re,json; sys.path.insert(0,'reports/u_umbral'); import u_umbral_u1 as u
v=dict(u.VARIANTES['c14']); v['plazo']=re.compile(r'\b'+u._NUM_C14+r'\s*(?:\(\d+\)\s*)?'+u._UNID+r'\b|d[ií]as\s+(?:h[aá]biles|corridos)',re.I)
for g,_,r,_ in u.GRAFOS:
    N=[n for n in json.load(open(r))['nodes'] if n['type'] in u.TIPOS_CUANTIA and u.spans_cuantia(u.nfc(u.props(n).get('descripcion')),v)]
    print(g,sum(not u.con_campo(n) for n in N),'de',len(N))"
```

La prosa del tablero la corrige la mesa; esta unidad no la toca. En U2 uso c14
tal como está en el mandato. c14_eur queda como dato informativo, y declaré una
variante con nombre propio, c14_par, para las formas «2 (dos) años» y «diez (10)
años».

**Medición 5 en una línea.** De 164 criterios, 8 tienen cuantía según c14; c14_par
no agrega ninguno [U2: medicion_5.criterios_con_cuantia]. Los 8 tienen el valor
en algún nodo del ancla. El valor se pierde en la búsqueda en 4 de 8, tanto en C3
como en C4, y llega a la respuesta en 3 de 8 en cada celda [U2:
medicion_5.clases_c14]. Sin el agregado posterior A-P6PAR, uno de los 8 sale
«grafo»: es un límite del prototipo, no del grafo (§3). Con n = 8, la fracción
es cruda y no autoriza porcentajes.

## 1. Eje de esquema — dónde vive el umbral

| | **Propiedad del nodo** (vigente para Restriccion.umbral y Obligacion.plazo) | **Atributo de la relación** (`limita`, `condicion_de`, …) |
|---|---|---|
| **A favor** | Todo portador de valor tiene nodo. La vigente ya lleva 498 campos [U1: medicion_1.desarrollo.total]. El agente la ve completa con `ver_nodo` (`data/experiment/evaluacion/harness.py:179-190`; `data/experiment/neo4j/neo4j_index.py:206`). La suite ya la lee (`scripts/regression_kg.py:572`, `:615`). | Representa hechos con valor n-arios, un valor por par Restriccion–Operacion: es la limitación del modelo de datos (`docs/plan_tesis.md:697`). 6 Restricciones tienen más de una `limita` (51 en r1) [U1: limita.<g>.restricciones_con_mas_de_una_limita]; si sus valores difieren por destino es NO MEDIDO. El loader sellado ya conserva `Edge.properties` (`data/experiment/evaluacion/loader.py:95-100`, `:282`). |
| **En contra** | Un solo valor por nodo, aunque limite varias operaciones (las 6 de arriba). El campo no aparece en el resumen de `buscar_nodos`, que muestra `descripcion[:160]` (`harness.py:110-124`). El índice full-text no indexa `umbral` (`data/experiment/neo4j/indices.py:77`). En 157 de 605 nodos con cuantía, todas las cuantías empiezan después del carácter 160 (94 sin campo) [U1: medicion_3]. Condicion y Excepcion no tienen campo en el prefijo (líneas 40 y 25; comando de §0): 177 nodos con cuantía (134 + 43) no tienen dónde llevarla [U1: medicion_3]. | **Cobertura:** no hay arista portadora para 62 de 248 Restricciones con umbral sin `limita`, 77 de 134 Condiciones con cuantía sin `condicion_de` [U1: limita], 170 de 248 Obligacion con `plazo` sin `regula` ni `condiciona`, ni 21 de 43 Excepciones con cuantía sin `exceptua` [U2: cobertura_otros_portadores]. **Inestable entre generaciones:** hay 1.041 `limita` en r1 (670 desde `limite_cualitativo`, 653 Restricciones con `limita` y sin umbral) y 284 en desarrollo (76 y 92) [U1: limita]. El predicado depende de la generación del prompt, y el valor quedaría atado a él. ESQ-3a difirió las properties en relaciones a ESQ-RI-3 / C1.7 (`data/experiment/esq/laudo_ESQ-3a_retoques.md:22-27`, `:204-211`). |
| **Prompt de E1** | Solo si E1 llena el campo: definir el campo en Condicion y Excepcion. | Predicados con valor y su regla. |
| **Tool schema** | Sin cambio: `entities.properties` admite claves string libres (comando de §0). | Cambio: `relations` no tiene `properties` y declara `additionalProperties: false` (comando de §0). Cadena de copias: `data/experiment/b54_catalogo_v3/code/prompt_v3_b54.py:411` ← `data/experiment/esq/code/prompt_congelado.py:187` ← `data/experiment/esq/code/prompt_esq3b_v2.py:321-344`, que declara no agregar campos. |
| **E2** | Sin cambio. Al fundir nodos, un conflicto de properties conserva el primer valor (`data/experiment/reextraccion_v2/e2_reduce/e2_lib.py:344-350`). | Cambio: las aristas se identifican por (source, predicado, target), sin properties (`e2_lib.py:409-420`). Hace falta una regla de fusión. |
| **Herramientas del agente** | Sin cambio. | Ninguna `ver_vecinos` devuelve properties de aristas: la del harness (`harness.py:197-237`, sellada, CLAUDE.md §3), la de Neo4j (`neo4j_index.py:226-260`) y la de tools v2 (`data/experiment/agente_v2/tools_v2.py:175-210`). Sin cambiarlas, el valor sería invisible. La carga en Neo4j tampoco lo lleva (`data/experiment/neo4j/cargar_kg.py:153-174`). |
| **Suite y shapes** | Suite sin cambio. S18 está declarada (`docs/esquema_v2_diseño.md:323`) pero no implementada (`scripts/shapes_validator.py:160-163`). | Hay que cambiar los matchers de `BKL-0006` y `BKL-0023`, que leen el nodo. S18 se reescribe. |
| **Re-extraer (principio 12)** | Depende del método (§2). | Sí, si E1 emite el valor en la relación. No, si se deriva en código moviendo el umbral del nodo a su `limita`: pero pierde los 62 casos sin `limita` y duplica el valor en las 6 con más de una. |
| **`cap::1.2`** | Los montos siguen en las dos Restricciones. La representación no corrige ni empeora la inversión. | La inversión está en el par sujeto–monto (`aplica_a`), no en Restriccion→Operacion. Un atributo en `limita` no la corrige. |

Lo que las trazas dicen para este eje: en los 8 criterios, el valor ya está en
nodos del ancla, y se pierde en la búsqueda en 4 de 8 [U2: medicion_5]. El cuello
de botella observado es llegar al nodo. Un atributo en la arista agrega un paso de
`ver_vecinos` que hoy no lo mostraría. 437 de 605 nodos con cuantía la tienen
también en el label, que sí se ve en `buscar_nodos` y en `ver_vecinos` [U1:
medicion_3]. La planilla de la medición 4 (si el destino de `limita` es el objeto
del tope) está sellada y sin leer (`muestra_limita_30.csv`, sha256 `8e981817…`):
la semántica de la arista portadora es NO MEDIDA hasta que la lea quien la autora
designe (checklist P15 y Q12).

## 2. Eje de pipeline — cómo se llena

| | **E1 emite** (vigente) | **Paso posterior en código** | **Modelo sobre el subconjunto con cuantía** |
|---|---|---|---|
| **A favor** | Es el único paso, junto con E3, que lee el chunk. Llena hoy 498 campos. El prototipo coincide con el campo en 295 de 498 y no difiere en ninguno [U1: medicion_6]. | USD 0 y sin re-extraer (principio 12, `docs/plan_tesis.md:299`). Extrae un solo valor en 240 de los 287 nodos sin campo, y además encuentra 40 nodos con valor que c14 no ve («2 (dos) años») [U1: medicion_6]. Puede verificar contra E0 y contra el parser: en `cap::1.2` detecta la inversión en las 2 Restricciones [U2: cap_1_2_contra_tabla]. | Puede leer números en letras compuestos, bases relacionales y varios valores con su contexto. Para 605 nodos en 310 llamadas por chunk estimé ≈ USD 0,46; para los 287 sin campo, ≈ USD 0,25 (169 llamadas); en diez, ≈ USD 0,51. Todo es ESTIMACIÓN NO VERIFICADA (supuestos y tarifa en D-ESTIM; [U2: dim_modelo]). |
| **En contra** | **(i) Literalidad:** 219 de 498 campos están en la descripción y en E0 (D-N1). Restriccion.umbral: 141 de 248 (181 sin espacios). Obligacion.plazo: 76 de 248, 156 en ninguno de los dos textos y 28 con valor de relleno [U1: medicion_1]. **Huecos:** 287 de 605 nodos con cuantía no tienen campo, y 177 de ellos son de tipos sin campo [U1: medicion_3]. **(iii) Tablas:** copia valores de tablas linealizadas no marcadas. La regla contra copiar celdas solo rige con FLAGS E0 (prefijo, líneas 263-271). | **(ii) Copia a E1:** compara contra la descripción que escribió E1, así que en `cap::1.2` «coincide» con los montos invertidos [U1: medicion_6]. Solo detecta errores si verifica contra el texto de E0 o contra el parser de tablas. Detectar no es corregir. **Límites:** 34 de 287 nodos sin campo tienen varios valores (ambigüedad); 122 de 605 son relacionales y el triple pierde la base (§3); en 13 de 287 no extrae nada; no crea valores que falten en la descripción [U1: medicion_6; U2: dim_relacionales]. | Paso LLM nuevo: caché y crudo obligatorios (`data/experiment/evaluacion/llm_cache.py`) y un prompt a sellar. Lee el mismo texto linealizado de E0, así que el riesgo de copiar la inversión de `cap::1.2` sigue en pie (NO VERIFICADO: no se corrió). Necesita la misma verificación en código que E1. |
| **Prompt, schema, E2** | Prompt: campo en Condicion y Excepcion, tramo literal, y regla de tablas extendida a los chunks que detecte el parser (RX-10). Schema y E2 sin cambio. | Sin prompt ni schema. Un módulo nuevo sobre la salida guardada. | Prompt propio. E1 sin cambio. |
| **Agente, suite, shapes** | Sin cambio en el agente. La suite y las shapes pueden sumar un control «cuantía en la descripción ⇒ campo». | Igual. | Igual. |
| **Re-extraer** | Sí (r2b, dentro de U-REEXT-T0). | No. Se puede medir en r2a. | No re-extrae E1, pero paga. |
| **`cap::1.2`** | Persiste mientras E0 no marque la tabla. Con el parser cableado (RX-10), rige la regla de celdas. | La copia si solo lee la descripción; la detecta si verifica contra `e0_tablas`. | Igual que E1 si lee el texto linealizado; con la tabla parseada como insumo, NO VERIFICADO. |

## 3. Casos propios

- **(iii) Tablas que E0 no marca.** El patrón D-PTL dispara en 5 chunks no
  marcados, todos de cap: `cap::1.2` y cuatro de ponderadores, `cap::2.12.2.5`,
  `.2.6`, `.2.8` y `2.12.3.2`. A esos cuatro `e0_tablas` no les asigna tabla. Los 5
  chunks tienen 26 nodos con umbral en desarrollo [U1: medicion_2]. Hay además 12
  chunks no marcados en que `e0_tablas` detecta tabla y el patrón no dispara, entre
  ellos `ric::9.2.1` y `cap::4.2.1.1`. En desarrollo son 10 chunks con 9 nodos con
  umbral [U1:
  medicion_2.nodos_de_los_chunks_con_tabla_e0_tablas_sin_disparo_por_grafo_informativo].
  Ninguno de los dos métodos basados en el texto de E0 (E1 o modelo) queda a salvo
  sin la detección de tablas de U-R2-CODIGO.
- **(iv) Umbrales relacionales.** En desarrollo hay 122 de 605 nodos con cuantía:
  60 con campo y 62 sin campo. Por forma, que no son excluyentes: 93 son un
  porcentaje o «veces» seguido de «de», «del» o «sobre» y una base; 23 llevan
  «equivalente» antes de un monto; 7, «veces» seguido de artículo. En r1 son 135 de
  638 y en diez, 128 de 682 [U2: dim_relacionales]. Un triple (tipo, valor, unidad)
  no guarda la base («25 % de la RPC»). El tramo literal sí la conserva. Guardar la
  base en un campo aparte es una DECISIÓN ABIERTA de la autora.
- **`cap::1.2` contra el parser.** `e0_tablas` asigna a `cap::1.2` la tabla
  `cap::tabla000`: Bancos 5.000 y Restantes entidades 2.500. Las dos Restricciones
  del grafo tienen el monto de la otra columna: restantes 5.000 y bancos 2.500. La
  demostración marca «NO» en las dos [U2: cap_1_2_contra_tabla]. Es una prueba
  puntual, no un verificador general.
- **Límite del prototipo (A-P6PAR, agregado posterior y rotulado).** P6 no
  reconocía «180 (ciento ochenta) días», así que EV2F-015#3 salía «grafo» aunque el
  ancla tiene el nodo `Condicion_plazo_minimo_180_dias…`. Reporto la medición 5 con
  y sin el agregado (`u2_muestra_trazas.md`). Es el mismo tipo de hueco que c14 con
  «2 (dos) años».

## 4. Propuesta

**PROPUESTA (par A): propiedad del nodo, llenada por E1 con verificación en código.**
- **Representación:** propiedad del nodo en los cuatro tipos con cuantía
  (Restriccion, Obligacion, Condicion y Excepcion). El valor es el **tramo literal**
  de la cuantía.
- **Llenado:** E1 emite el tramo literal. Un paso en código lo normaliza a (tipo,
  valor, unidad) y lo verifica:
  - que sea subcadena del texto de E0;
  - en los chunks con tabla detectada, contra `e0_tablas`.
  Lo que no verifica queda marcado, no corregido.
- **Por qué.** Hoy el campo no es literal en buena parte de los casos (§2 i); hay
  177 nodos con cuantía en tipos sin campo; y la verificación contra el parser es
  la única de las opciones medidas que detecta `cap::1.2`. Cumple el principio 12:
  E1 guarda lo necesario para reprocesar en código, y la normalización y la
  verificación se re-aplican a USD 0.
- **Costo y dependencias:** la re-extracción de r2b (U-REEXT-T0, ya en el plan) y
  la detección de tablas de U-R2-CODIGO.

**ALTERNATIVA (par B): propiedad del nodo, llenada en código, sin re-extraer.**
- **Representación:** la misma que en A.
- **Llenado:** paso posterior en código sobre la descripción guardada, con la misma
  verificación contra E0 y `e0_tablas`. Los campos que hoy llena E1 se conservan y
  se verifican.
- **Qué cambia respecto de A:** es USD 0, se mide en r2a y llena un solo valor en
  240 de los 287 nodos sin campo. Pero hereda los errores de la descripción: solo
  los marca, no los corrige. Y no resuelve los 34 casos con varios valores ni la
  base de los 122 relacionales.

**Lo que no propongo:**
- **El atributo de la relación**, por la cobertura (62, 77, 170 y 21 portadores sin
  arista), porque ninguna herramienta del agente lo muestra (una de ellas está
  sellada) y porque reabre una decisión diferida a ESQ-RI-3 / C1.7.
- **El llenado por un modelo**, que queda dimensionado (≈ USD 0,25 a 0,51,
  ESTIMACIÓN NO VERIFICADA). No agrega verificación respecto de A y lee el mismo
  texto linealizado.

**Decisiones abiertas para la autora:**
- campo aparte para la base de los umbrales relacionales;
- tratamiento de los valores de relleno de `plazo` (28 en desarrollo);
- quién lee la muestra de 30 `limita` (P15, Q12);
- si los hechos con valor n-arios siguen como trabajo futuro (C1.7).
