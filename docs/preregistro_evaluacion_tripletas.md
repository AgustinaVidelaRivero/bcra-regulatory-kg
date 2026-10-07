# Pre-registro de la evaluación por tripletas (B4)

**BORRADOR — PENDIENTE DE DECISIÓN Y FIRMA DE LA AUTORA** (redactado el 07/10/2026 en la unidad RECONC-DISENO-EVAL; entrado al
repo como BORRADOR el 07/10/2026 por decisión de la autora, que lo firma después de leerlo, con las once decisiones del §10; no
sellado; ningún número de este documento es un resultado). Es el archivo que B4.1 nombra (`plan:416`). Su firma es, a la vez, el laudo D-b (`plan:961`: alcance, escala de
importancia, regla de presencia y umbral de acuerdo del juez), sin el cual B4 no arranca. Los puntos marcados
<DECIDE LA AUTORA> llevan una propuesta; se fijan al firmar.

## 0. De dónde sale

- Decisiones D9 a D12 de las reuniones del 18 y el 19/08/2026 (acta confirmada por la autora el 07/10/2026,
  `docs/registro_reunion_mentores_2026-08-18_19.md`).
- Bloque B4 del plan (`plan:412-459`), con los dos requisitos de B4.1: intervalos de Wilson en toda proporción
  (exigencia 4) y precisión desagregada por etapa E0–E5, además de por predicado y por TO (exigencia 5) (`plan:416-423`).
- Laudo D-f, FIRMADO el 27/08/2026 (`966253e:docs/laudo_D-f_secuencia_tripletas.md`, sha256 `85f48f14…`): el instrumento se
  valida en desarrollo y la medición que cuenta se corre una sola vez sobre el grafo escalado, dentro de B6.3 (`:8-18`). Este
  pre-registro declara el **doble rol** que pide su §5 (`:47-49`): **etapa V** (validación del instrumento, desarrollo) y
  **etapa T** (medición única sobre el grafo evaluado, componente (d) de B6.3, `plan:773`).

## 1. Qué mide, y en qué se diferencia de U-LECTURA-ACEPTADAS

Mide el contenido del grafo a nivel de tripleta: si cada relación que el grafo afirma es correcta según su texto
(precisión), si merece estar (importancia), y qué parte de lo más importante de los textos está en el grafo (cobertura).

| | U-LECTURA-ACEPTADAS (cerrada en `86324cc`) | esta evaluación |
|---|---|---|
| pregunta | tasa de unidades aceptadas con error: línea de base del pipeline y vigilancia por tanda (`9502ca4:docs/mandatos/ULECTURA_ACEPTADAS_tasa_error_tanda0.md:9-18`) | calidad del contenido del recurso: precisión, importancia y cobertura (promesa P-1, `plan:1278`) |
| unidad | la unidad de E0 (el chunk), con error si **al menos un** nodo o relación no se sostiene | la **tripleta** (nodo, relación, nodo) con su evidencia |
| población | 2.366 unidades aceptadas de los diez TOs de la tanda 0, sin la cola | aristas de contenido del grafo de validación (V) y del grafo evaluado (T) |
| lectores | instancia, mesa a ciegas y adjudicación de la autora | gold de la autora y juez LLM calibrado contra ella |
| importancia | no se juzga | se juzga (escala de tres valores) |
| omisiones | aparte, no cuentan | son el objeto de la vía de cobertura |
| resultado | ítems 6 de 30, no ítems 4 de 30, ponderada 0,1616 [0,0689; 0,2543] (`86324cc:…/reporte_l2.md`, §2) | — |

Las dos cifras no se comparan: una cuenta unidades con algún error y la otra relaciones correctas. Se reusan el formato de
ficha (texto propio y heredado, tramo), el sorteo sellado con semilla antes de abrir (patrón `lectura_aceptadas/l0_sellos.py`)
y el Wilson con z = 1,959964 (`reext_t0/t4/tasas_t4.py:244-249`). Si una unidad de la muestra de U-LECTURA-ACEPTADAS aporta
una tripleta a la muestra de V, se declara el solapamiento; no se excluye.

## 2. Grafos

- **Etapa V** <DECIDE LA AUTORA>. Propuesta: **KG-Tanda0-Desarrollo-r2b-sincola** (`2922b72d…`; 6.723 nodos y 22.084 aristas;
  sello `dde9f44`/`235a295`), porque tiene el esquema congelado y la cadena r2b del escalado: la escala de importancia y la regla
  de presencia se validan sobre el vocabulario que después se mide. La letra del laudo D-f dice KG-Reextraído-r1 (`0226e947…`,
  `966253e:…:8-12`), de una generación de esquema anterior; elegir r2b pide una nota fechada al laudo D-f (cambia el objeto de
  la validación, no la secuencia).
- **Etapa T**: el grafo evaluado, el escalado sellado antes de B6.3 (laudo 3 del 20/09, `plan:284`), sin la cola humana
  (enmienda 5, `ccd8fad`, §1). La cola tiene su propia lectura (T4: 12 de 30).

## 3. Vía de precisión (D9)

**3.1 Unidad.** Una arista emitida por la extracción entre dos nodos de contenido, con su evidencia. Las aristas que arma el
código (`remite_a`, las del esqueleto, las de cuarentena, y las demás que la cadena derive) quedan fuera de las 100: su
corrección la controlan el código y lecturas propias (`remite_a`: 0 de 167 no sostenidas, `86324cc:…/reporte_l2.md`, §2 (ii)).
La lista exacta de predicados derivados se fija al sellar, leyendo la cadena de ensamblado (NO VERIFICADA en este borrador).
Aristas del grafo de desarrollo r2b sin cola, por predicado (recuento propio sobre su `kg.json`, 22.084): `remite_a` 11.374,
`establecida_en` 6.480, `aplica_a` 1.770, `condicion_de` 1.379, `limita` 267, `regula` 169, `requiere` 117, `condiciona` 85,
`exceptua_obligacion` 69, `subclase_de` 69, `padre_sugerido` 66, `exceptua` 62, `prohibe` 54, `referencia` 54, `miembro_de` 51,
`ejecuta` 11, `instancia_de` 5, `parte_de` 1, `modificada_por` 1.

**3.2 Muestra.** 100 aristas, estratificadas por predicado (asignación proporcional, con un mínimo de 3 por predicado que
tenga 30 aristas o más) y al azar dentro de cada estrato; el TO se reporta como covariable. Semilla fijada en la firma; lista
de la población, hora y sha256 de la muestra sellados antes de abrir una ficha.

**3.3 Ficha.** Nodo de origen (tipo, etiqueta, descripción, propiedades), predicado, nodo de destino; evidencia: texto propio y
heredado de la unidad de procedencia, tramo literal si lo hay, páginas, ruta del PDF y número de página. Sin ninguna salida de
un modelo (§4.2).

**3.4 Juicios.** *Correcta*: sí / no / no decidible por la autora; criterio de B4.1 (a): la evidencia sostiene la relación entre
esos dos nodos, con sus sujetos, valores, calificadores y modalidad. *Importancia* <DECIDE LA AUTORA>, propuesta de tres
valores: **esencial** (una respuesta de cumplimiento sobre esa unidad la necesita), **útil** (agrega contexto), **accesoria**
(no merece estar en un grafo regulatorio).

**3.5 Procedimiento.** Lote piloto de 10; FRENO para ajustar la ficha, no el juez (`plan:445-447`); después nueve lotes de 10
con la ficha fija. Si la ficha cambió en algo que el juicio usa, las 10 del piloto se vuelven a etiquetar.

**3.6 Estimadores.** Precisión = correctas / decididas, con Wilson al 95 % (con 100 y una precisión cercana a 0,85, unos ± 0,07,
cómputo propio). Por predicado y por TO, fracción cruda «n de N» donde N < 20. Por etapa E0–E5, por la procedencia de la arista
(`chunk_id`, `estado_e3`). Las no decidibles se reportan aparte, con las dos cotas (todas correctas, todas incorrectas).
Ponderada por importancia <DECIDE LA AUTORA: pesos 3/2/1, o precisión sobre las esenciales>.

## 4. Juez y calibración (D10)

**4.1 Juez** <DECIDE LA AUTORA el modelo>. Propuesta: `claude-sonnet-4-6` a temperatura 0, el del juez de fidelidad de EV2
(`plan:1282`), por continuidad y porque admite fijar la temperatura; alternativa, `claude-sonnet-5-5` con pedido adaptado y
sin temperatura (`plan:778`). Por la API con captura íntegra y caché; prompt congelado por sha256; N = 3 con voto modal; ciego al
grafo de origen y a las etiquetas de la autora (`plan:435-436`); la misma ficha que ve la autora.

**4.2 Gold a ciegas.** La autora etiqueta las 100 sin ver ninguna propuesta del modelo. D9 y D10 juntos lo piden: el acuerdo
juez–autora solo mide algo si las dos etiquetas son independientes; si la autora viera la propuesta, mediría cuánto la acepta.
El modo asistido de D12 se usa en lo que no es gold (§6).

**4.3 Criterio de acuerdo** <DECIDE LA AUTORA; va al laudo D-b>. Propuesta, para «correcta», las tres condiciones a la vez:
(i) acuerdo en al menos 84 de 100 decididas (límite inferior de Wilson 0,7558, cómputo propio; el piso de 0,75 es el del
criterio de U-COMP-E1, `cbcb823:docs/mandatos/UCOMP_E1_comparacion_chica_modelo.md:70-72`); (ii) la precisión según el juez y según la autora difieren en
0,05 o menos, para que el juez no corra la cifra que escala; (iii) de las que la autora marca incorrectas, el juez marca
incorrecta al menos la mitad, reportado como fracción cruda (con unas 15 incorrectas, esta tasa no se estima con precisión, y se
declara). Para importancia: acuerdo exacto en los tres valores en al menos 60 de 100 y a un nivel de distancia en al menos 90 de
100. Si no pasa: el juez no escala; la precisión de V queda con las 100 de la autora y la de T se mide con muestra humana
(§7). El prompt del juez se ajusta, si hace falta, con otras tripletas y no con las 100; una sola recalibración, declarada.

## 5. Vía de cobertura (D11)

**5.1 Fragmentos.** Unidades terminales de E0 con texto propio de 80 a 1.500 caracteres, que es el tamaño de párrafo de D11
(en la E0 de desarrollo de la enmienda 01: 1.492 de 1.763; mediana 321 y percentil 90 1.231; recuento propio; se recomputa
sobre la E0 r2b al sellar). Se excluyen las anclas de EV2 y de los pares sintéticos v3 y v4 con sus descendientes (B4.1 (g)).

**5.2 Tamaños** <DECIDE LA AUTORA>. V: 300 fragmentos; T: 600. Las primeras 100 tienen que ser una selección (un tercio en V, un
sexto en T); el ancho del recall@100 no depende del tamaño del conjunto, y una tripleta más por fragmento cuesta poco.

**5.3 Extracción.** Un modelo distinto del extractor del grafo (E1 es `claude-haiku-4-5`) <propuesta: `claude-opus-5-5`>, con
un prompt de extracción abierta, sin el esquema: sujeto, relación y objeto en las palabras del texto, una por fragmento, «la
más importante, la que no puede faltar en un grafo de regulación», con el tramo literal que la sostiene. El código verifica el
tramo contra el texto; sin tramo verificado, la tripleta se descarta y se cuenta. Mismo modelo y mismo esquema que E1 darían
sesgos compartidos y una cobertura inflada.

**5.4 Orden.** Otro modelo <propuesta: `claude-sonnet-5-5`> puntúa la importancia de cada tripleta de 1 a 5 con una rúbrica
fija, N = 3, y se ordena por el puntaje medio, con desempate por sorteo. Ordenar cientos de tripletas en un solo pedido no es
confiable; puntuar y ordenar es la forma operativa de «ordenarlas de la más importante a la menos importante».

**5.5 Calibración del orden.** La autora marca la importancia (escala de 3.4) de las 100 primeras y de 30 sorteadas entre las
posiciones 101 y 300, mezcladas y sin ver la posición. Propuesta: el orden pasa si al menos 80 de las 100 primeras son
esenciales o útiles y si esa proporción supera a la de las 30 de control. Si no pasa, el recall se reporta sobre las que la
autora marcó esenciales, sin ranking.

**5.6 Presencia: cómo se decide que una tripleta está en el grafo.** En dos pasos. (1) Subgrafo candidato, determinístico: los
nodos cuya procedencia es la unidad del fragmento, sus ancestros (herencia) o sus descendientes según la política de
descendientes declarada (frontera ancla/chunk, B4.1 (b)), con las aristas entre ellos. (2) Un juez de presencia (N = 3, voto
modal, ciego al ranking) recibe la tripleta abierta y el subgrafo y responde presente, parcial o ausente, nombrando la arista o
los nodos que la expresan; el código controla que lo nombrado exista. Una regla solo de cadenas no alcanza: la tripleta abierta
está en las palabras del texto y el grafo en el esquema. La autora decide la presencia de las 100 primeras con el subgrafo a la
vista; el juez escala si acuerda en al menos 84 de 100. **Se aparta de la letra de B4.1 (b)** («match de sujeto/objeto
normalizados + relación», `plan:433-434`) y se declara.

**5.7 Recall@k** con k = 10, 50 y 100 (`plan:450-451`): presentes / k, con Wilson; «parcial» aparte.

**5.8 Revisión de las ausentes** (B4.1 (e)). La autora revisa cada ausente de las 100 primeras: si la tripleta es correcta según el
fragmento (si no, error del gold: sale del denominador y se cuenta), si está en el grafo y el juez no la vio (error de presencia:
se corrige y se cuenta) y si es importante. Recall crudo y depurado, los dos con sus conteos. Las ausentes importantes van al
backlog con su `capa_pipeline` (B4.4): son insumo del grafo corregido, nunca del evaluado.

## 6. Etiquetado asistido y experticia (D12)

**6.1 Asistente.** Claude Code (`claude -p --bare`, solo lectura sobre el paquete de fichas) arma cada ficha y, donde se usa, una
propuesta de etiqueta con el tramo que la sostiene y la información para comprobarla: texto propio y heredado, ruta del PDF y
página, y la dirección del TO en el sitio del BCRA si el manifiesto la tiene.

**6.2 Dónde se usa la propuesta (la autora confirma sí o no).** En la revisión de las ausentes (5.8), en la clasificación por
experticia (6.3) y, si el juez no pasa, en la ampliación de la muestra de precisión, declarada como asistida; en 20 de esas
tripletas se toma además la etiqueta a ciegas, para medir cuánto cambia la propuesta la respuesta. No se usa en el gold (§4.2)
ni en las calibraciones de 5.5 y 5.6.

**6.3 Clasificación por experticia.** El asistente marca cada tripleta como «la decide la autora» o «necesita un experto del
dominio», con el motivo; la autora confirma sí o no **después** de etiquetarla, para no sesgar el juicio. Las confirmadas como
«necesita experto» quedan como no decidibles por la autora (3.6).

**6.4 Vía al experto.** U-PREP-CONTACTO (`plan:1174-1178`) y el registro del 04/09, §3: anotación experta de una submuestra en
modo literal (`docs/registro_reunion_mentores_2026-09-04.md:77-97`). Quién adjudica (checklist P15 y Q12, `:105` y `:209`; F-7 y
C-8) se decide con los mentores. Sin experto, la evaluación corre igual y declara las no decidibles con su conteo.

## 7. Etapa T, dentro del pre-registro de B6.3

- Precisión: el juez calibrado sobre 400 aristas del grafo evaluado, con la estratificación de 3.2 (unos ± 0,035 con 0,85,
  cómputo propio); control a ciegas de la autora sobre 30 sorteadas entre ellas. Si el acuerdo es menor que 26 de 30 (límite
  inferior de Wilson 0,7032), la cifra del juez se declara no validada en el escalado y se reporta la de las 30.
- Cobertura: 600 fragmentos de los TOs del conjunto de test (disjuntos de los 15 y de los 5 de la tanda 0, checklist Q10, `:207`),
  con 5.3 a 5.8 iguales y control de 30 en la presencia.
- B6.3 (d) incorpora todo esto en su pre-registro sellado (laudo D-f §5, `966253e:…:52`; checkbox del plan `:977-978`).

## 8. Costo y tiempo (ESTIMACIÓN NO VERIFICADA)

Costo por llamada = tokens de entrada × precio + tokens de salida × precio. Supuestos, no medidos: juez 2.000 / 200 tokens
(Sonnet 4.6 a 3 y 15 USD por millón, `plan:775`); extracción 1.500 / 300 (Opus a 5 y 25, precio de `claude-opus-5` en
`banco_mcp/agentes/precios_sellados.json`; el de `claude-opus-5-5`, NO VERIFICADO); puntaje 300 / 50; presencia 3.000 / 200.
V: unos USD 10–15; T: unos USD 20–30. Tiempo de la autora: gold de 100, orden de 130, presencia de 100, ausentes de hasta 100 y
controles de T; unas 8 a 12 horas. Se re-estima con un conteo de tokens real antes de firmar.

## 9. Q7 (B4.2 contra B6.3 (d))

Propuesta: B6.3 (d) pasa a decir «con el instrumento validado en desarrollo (B4.2 y B4.3), cerrado antes de sellar el
pre-registro de B6.3»; B4.2 y B4.3 quedan como precondición de ese pre-registro. Resuelve la inconsistencia de `plan:445` y
del checklist Q7 (`:204`).

## 10. Lo que se decide al firmar

1. Grafo de la etapa V (r2b de desarrollo o r1) y, si es r2b, la nota al laudo D-f. 2. Lista de predicados derivados que salen
de la muestra. 3. Escala de importancia y ponderación. 4. Modelo del juez. 5. Criterio de acuerdo (4.3) y de orden (5.5).
6. Tamaños (100 / 300 en V; 400 + 30 / 600 en T). 7. Modelos de extracción y de puntaje. 8. Regla de presencia en dos pasos y su
desvío de B4.1 (b). 9. Gold a ciegas y usos del modo asistido. 10. Vía al experto. 11. Tope de costo de V y de T.

## Comandos de los recuentos de este borrador (regla i)

```
# aristas por predicado del grafo de desarrollo r2b sin cola (22.084)
python3 -c "import json,collections;kg=json.load(open('data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo_r2b_sincola/r2/kg.json'));print(len(kg['edges']),collections.Counter(e['relation'] for e in kg['edges']).most_common())"
# unidades de la E0 de desarrollo (enmienda 01) con texto propio de 80 a 1.500 caracteres (1.492 de 1.763)
python3 -c "import json,glob;L=[u['chars_propio'] for p in glob.glob('data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_*.json') for u in json.load(open(p))];L.sort();print(len(L),sum(80<=x<=1500 for x in L),L[len(L)//2],L[int(.9*(len(L)-1))])"
# Wilson al 95 % (z = 1,959964): 84/100 -> 0,7558; 26/30 -> 0,7032; ancho con 0,85: n=100 0,0699, n=400 0,0350
```
