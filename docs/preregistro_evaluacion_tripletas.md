# Pre-registro de la evaluación por tripletas (B4)

**VERSIÓN PARA FIRMAR — PENDIENTE DE FIRMA DE LA AUTORA** (borrador del 07/10/2026 en RECONC-DISENO-EVAL, entrado al repo en
`93bebd2`; versión para firmar del mismo día con las once decisiones de la autora del §10 y sus siete ajustes; no sellado; ningún número
de este documento es un resultado). Es el archivo que B4.1 nombra (`plan:416`). Su firma es, a la vez, el laudo D-b (`plan:961`: alcance,
escala de importancia, regla de presencia y umbral de acuerdo del juez), sin el cual B4 no arranca. La firma se asienta al pie, con fecha;
el texto firmado no se edita después: recibe notas fechadas.

## 0. De dónde sale

- Decisiones D9 a D12 de las reuniones del 18 y el 19/08/2026 (acta confirmada por la autora el 07/10/2026,
  `docs/registro_reunion_mentores_2026-08-18_19.md`).
- Bloque B4 del plan (`plan:412-459`), con los dos requisitos de B4.1: intervalos de Wilson en toda proporción
  (exigencia 4) y precisión desagregada por etapa E0–E5, además de por predicado y por TO (exigencia 5) (`plan:416-423`).
- Laudo D-f, FIRMADO el 27/08/2026 (`966253e:docs/laudo_D-f_secuencia_tripletas.md`, sha256 `85f48f14…`): el instrumento se
  valida en desarrollo y la medición que cuenta se corre una sola vez sobre el grafo escalado, dentro de B6.3 (`:8-18`). Este
  pre-registro declara el **doble rol** que pide su §5 (`:47-49`): **etapa V** (validación del instrumento, desarrollo) y
  **etapa T** (medición única sobre el grafo evaluado, componente (d) de B6.3, `plan:773`). La nota del 07/10/2026 al pie del laudo
  D-f asienta que el grafo de la etapa V es el de desarrollo r2b sin cola y no r1 (decisión 1 del §10).
- Metodología de calibración de jueces del proyecto (la del juez de fidelidad de EV2, `evaluacion/02_calibracion_juez.md` y
  `ev2_juez/calibracion/registro_calibracion.md`): el LLM clasifica, el código computa el veredicto; calibradores como casos resueltos;
  N repeticiones que re-muestrean; salida «requiere adjudicación humana»; ningún ajuste del prompt sin decisión de la autora.

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

- **Etapa V (decisión 1): KG-Tanda0-Desarrollo-r2b-sincola** (`2922b72d…`; 6.723 nodos y 22.084 aristas; sello `dde9f44`/`235a295`;
  «grafo sin cola de la tanda 0», nombres D13), porque tiene el esquema congelado y la cadena r2b del escalado: la escala de importancia
  y la regla de presencia se validan sobre el vocabulario que después se mide. La letra del laudo D-f decía KG-Reextraído-r1 (`0226e947…`,
  `966253e:…:8-12`), de una generación de esquema anterior; la nota fechada al pie del laudo (07/10/2026) asienta el cambio del objeto de
  la validación, no de la secuencia. Si el grafo sin cola de la tanda 0 se re-sella antes de abrir la muestra (parte A y S19,
  `hoja_de_ruta_tanda1_mesa/borrador_resellado_grafo_evaluado_tanda0_mesa.md`), la etapa V corre sobre el sello vigente al sortear,
  con su sha en el acta de sorteo.
- **Etapa T**: el grafo evaluado, el escalado sellado antes de B6.3 (laudo 3 del 20/09, `plan:284`), sin la cola humana
  (enmienda 5, `ccd8fad`, §1). La cola tiene su propia lectura (T4: 12 de 30).

## 3. Vía de precisión (D9)

**3.1 Unidad y población (decisión 2).** Una arista emitida por la extracción entre dos nodos de contenido, con su evidencia. Quedan
**fuera** de la población las aristas que arma el código: `remite_a`, `establecida_en`, `subclase_de`, `miembro_de`, `instancia_de`,
`parte_de`, `modificada_por`, `padre_sugerido` y `referencia` (su corrección la controlan el código y lecturas propias; `remite_a`: 0 de
167 no sostenidas, `86324cc:…/reporte_l2.md`, §2 (ii)). Quedan **dentro** las diez relaciones de contenido del esquema, con `aplica_a`
incluida: en el grafo de V son 3.983 aristas (recuento propio sobre su `kg.json`): `aplica_a` 1.770, `condicion_de` 1.379, `limita` 267,
`regula` 169, `requiere` 117, `condiciona` 85, `exceptua_obligacion` 69, `exceptua` 62, `prohibe` 54, `ejecuta` 11. La lista se fija al
sellar la muestra leyendo la cadena de ensamblado del grafo que se mide: todo predicado que el código derive se agrega a la lista de
fuera; ninguno de contenido sale.

**3.2 Muestra.** 100 aristas, estratificadas por predicado (asignación proporcional, con un mínimo de 3 por predicado que
tenga 30 aristas o más; los de menos de 30 se agrupan en un estrato «otros») y al azar dentro de cada estrato; el TO se reporta como
covariable. Semilla fijada en la firma; lista de la población, hora y sha256 de la muestra sellados antes de abrir una ficha.
**Pool de calibración, aparte:** en el mismo sorteo se reserva un segundo conjunto de 20 aristas, disjunto de las 100, del que salen
los calibradores del juez (§4.2); se sella con la muestra y no entra a ninguna cifra.

**3.3 Ficha.** Nodo de origen (tipo, etiqueta, descripción, propiedades), predicado, nodo de destino; evidencia: texto propio y
heredado de la unidad de procedencia, tramo literal si lo hay, páginas, ruta del PDF y número de página. Sin ninguna salida de
un modelo (§6.2).

**3.4 Juicios (decisión 3).** *Correcta*: sí / no / no decidible por la autora; criterio de B4.1 (a): la evidencia sostiene la relación
entre esos dos nodos, con sus sujetos, valores, calificadores y modalidad. *Importancia*, tres valores: **esencial** (una respuesta de
cumplimiento sobre esa unidad la necesita), **útil** (agrega contexto), **accesoria** (no merece estar en un grafo regulatorio). Sin
pesos: la precisión sobre las esenciales se reporta como cifra aparte (3.6).

**3.5 Procedimiento.** Lote piloto de 10; FRENO para ajustar la ficha, no el juez (`plan:445-447`); después nueve lotes de 10
con la ficha fija. Si la ficha cambió en algo que el juicio usa, las 10 del piloto se vuelven a etiquetar.

**3.6 Estimadores (ajuste 1).** Dos cifras de precisión, siempre juntas:
- **cruda**: correctas / decididas sobre las 100, con Wilson al 95 % (con 100 y una precisión cercana a 0,85, unos ± 0,07);
- **ponderada por el tamaño de cada estrato de predicado**, que es la cifra del grafo (la muestra no es proporcional por el mínimo
  de 3): p̂_w = Σ_h W_h · p̂_h, con W_h = N_h / N (N_h aristas de contenido del predicado h en el grafo medido, N su total; en V, N = 3.983) y
  p̂_h la precisión cruda del estrato; varianza Σ_h W_h² · p̂_h (1 − p̂_h) / n_h e intervalo de Wald al 95 % (z = 1,959964), la misma
  construcción que la cifra ponderada de U-LECTURA-ACEPTADAS (`reporte_l2.md`, §5). Los estratos con n_h < 5 se reportan con su
  fracción cruda «n de N» y, para la varianza, se agrupan en «otros» (declarado).
- Las mismas dos cifras para la **precisión sobre las esenciales** (correctas / decididas entre las que la autora marcó esenciales; la
  ponderada con los mismos W_h, sobre las esenciales de cada estrato), que es la cifra aparte de la decisión 3.
- Por predicado y por TO, fracción cruda «n de N» donde N < 20. Por etapa E0–E5, por la procedencia de la arista (`chunk_id`,
  `estado_e3`). Las no decidibles se reportan aparte, con las dos cotas (todas correctas, todas incorrectas).

## 4. Juez de precisión y su calibración (D10; decisiones 4 y 5; ajustes 2, 3 y 5)

**4.1 Modelo y vía (decisión 4).** `claude-sonnet-4-6` a temperatura 0, el del juez de fidelidad de EV2 (`plan:1282`), por la API con
captura íntegra y caché (`CachingClient`, `evaluacion/llm_cache.py`); prompt congelado por sha256 y declarado; ciego al grafo de origen
y a las etiquetas de la autora (`plan:435-436`); la misma ficha que ve la autora.

**4.2 Qué clasifica el juez y qué computa el código (ajuste 2).** El juez no responde «¿es correcta?». Clasifica, **componente por
componente contra la evidencia**, cada uno en {sostenido, contradicho, no_consta}: (i) el **sujeto** (el nodo de origen o el sujeto de la
norma: que la evidencia hable de ese sujeto), (ii) el **predicado** (que la relación afirmada sea la que la evidencia establece entre
los dos nodos), (iii) los **valores** (cuantías, plazos, porcentajes, fechas), (iv) los **calificadores** (condiciones, excepciones,
alcances) y (v) la **modalidad** (deber, prohibición, permiso, condición); y marca **requiere adjudicación humana** cuando la evidencia
no le alcanza para clasificar un componente (por ejemplo, el tramo está en una tabla ilegible o la relación depende de una remisión
que la ficha no trae). Para la importancia, el juez clasifica tres rasgos en sí/no: la relación fija una conducta exigible
(deber/prohibición/condición), tiene un valor o plazo concreto, y es la relación principal de la unidad o una accesoria.
El **código** computa el veredicto con esta regla fija, escrita acá y en el script, que no cambia sin firma: *correcta* = los cinco
componentes sostenidos o no_consta sin ningún contradicho y con sujeto y predicado sostenidos; *incorrecta* = al menos un componente
contradicho; *adjudicación* = algún componente marcado «requiere adjudicación humana» sin ningún contradicho. Importancia: *esencial* =
conducta exigible y (valor concreto o relación principal); *accesoria* = ni conducta exigible ni valor concreto; *útil* = el resto.

**4.3 Calibradores (ajuste 2).** El prompt lleva una sección de **casos resueltos**: entre 10 y 20 aristas del **pool de calibración**
(§3.2), nunca de las 100 del gold, etiquetadas por la autora componente por componente antes de escribir el prompt, elegidas cerca de las
fronteras (modalidad ambigua, calificador que cambia el alcance, valor con redondeo, tabla). Ningún criterio problemático se escribe como
regla declarativa sin su caso resuelto. Cuando un tipo de error se repita en la calibración, la corrección es agregar un caso resuelto del
pool (o de una arista nueva fuera de la muestra), no una regla.

**4.4 Repeticiones que re-muestrean (ajuste 3).** N = 3 por ficha, con **un cliente, una base de caché y un namespace por repetición**
(`juez_tripletas_r1`, `_r2`, `_r3`, con la versión de código y la marca de thinking), como el juez de EV2 (`ev2_juez/juez.py:150-170`,
patrón `rt_c6_n3`): la clave de la caché es sha256(namespace + request), así que el mismo pedido en tres namespaces son tres llamadas
distintas y la caché no puede devolver tres copias; el driver verifica 0 cross-hits entre las tres bases antes de agregar. Agregación
por **veredicto modal** sobre el veredicto computado; empate = `sin_consenso`, que va a adjudicación. Se registra la distribución
completa (unanimidad, 2 a 1, sin consenso) por dimensión.

**4.5 Gold a ciegas (decisión 9).** La autora etiqueta las 100 sin ver ninguna propuesta del modelo. D9 y D10 juntos lo piden: el acuerdo
juez–autora solo mide algo si las dos etiquetas son independientes. El modo asistido de D12 se usa en lo que no es gold (§6). Se aparta
de la letra de D12 para la parte del gold; declarado a los mentores (§11).

**4.6 Criterio de acuerdo (decisión 5; ajuste 5; va al laudo D-b).** Para «correcta», las tres condiciones a la vez, sobre las fichas que
el juez decide (las que manda a adjudicación se cuentan aparte, con su proporción): (i) acuerdo en al menos 84 de 100 (límite inferior de
Wilson 0,7558; el piso de 0,75 es el del criterio de U-COMP-E1, `cbcb823:docs/mandatos/UCOMP_E1_comparacion_chica_modelo.md:70-72`);
(ii) la precisión según el juez y según la autora difieren en 0,05 o menos (cruda y ponderada), para que el juez no corra la cifra que
escala; (iii) de las que la autora marca incorrectas, el juez marca incorrecta al menos la mitad, reportado como fracción cruda (con unas
15 incorrectas no se estima con precisión, y se declara). **Cifra reportada, no umbral: el kappa de Cohen** entre juez y autora para
«correcta» (dos clases, sobre las decididas por los dos) y, para la importancia, el kappa de Cohen sobre los tres valores y su variante
ponderada lineal. Para importancia, el acuerdo exigido es exacto en al menos 60 de 100 y a un nivel de distancia en al menos 90 de 100.
Si no pasa: el juez no escala; la precisión de V queda con las 100 de la autora y la de T se mide con muestra humana (§7). Si más de 15
de las 100 van a adjudicación, el instrumento se declara con esa frontera y las adjudicadas quedan como lectura humana.

**4.7 Candado de ajuste (ajuste 2).** El prompt del juez lleva escrita esta prohibición: *«Este prompt no se modifica sin decisión
escrita de la autora. Todo cambio se justifica con evidencia del texto de la norma, nunca con la etiqueta esperada de un caso.»* Una
sola recalibración, declarada, con casos resueltos del pool y nunca con las 100; después de cada cambio se re-corre todo el conjunto de
calibración. Los desacuerdos residuales se clasifican (de evidencia o de etiqueta) y quedan documentados como límite del instrumento.

## 5. Vía de cobertura (D11; decisiones 6, 7 y 8)

**5.1 Fragmentos.** Unidades terminales de E0 con texto propio de 80 a 1.500 caracteres, que es el tamaño de párrafo de D11 (en la E0
r2b de desarrollo: 1.491 de 1.768, recuento propio; mediana del texto propio con herencia 979 caracteres, percentil 90 2.078; se
recomputa sobre la E0 del grafo medido al sellar). Se excluyen las anclas de EV2 y de los pares sintéticos v3 y v4 con sus descendientes
(B4.1 (g)).

**5.2 Tamaños (decisión 6).** V: 300 fragmentos; T: 600. Las primeras 100 tienen que ser una selección (un tercio en V, un sexto en
T); el ancho del recall@100 no depende del tamaño del conjunto, y una tripleta más por fragmento cuesta poco.

**5.3 Extracción (decisión 7, con condición; ajuste 4).** Un modelo **distinto del extractor del grafo** (E1 es `claude-haiku-4-5`):
`claude-opus-5-5`, con un prompt de extracción abierta, sin el esquema: sujeto, relación y objeto en las palabras del texto, una por
fragmento, «la más importante, la que no puede faltar en un grafo de regulación», con el tramo literal que la sostiene. El código
verifica el tramo contra el texto; sin tramo verificado, la tripleta se descarta y se cuenta. **Condición:** si el resultado de
U-COMP-E1 lleva a cambiar el extractor del grafo a `claude-opus-5-5`, el extractor del recall pasa a `claude-sonnet-5-5` y el modelo
de puntaje (5.4) a `claude-sonnet-4-6`; la regla es que el extractor del recall nunca sea el modelo que extrajo el grafo medido. Mismo
modelo y mismo esquema que E1 darían sesgos compartidos y una cobertura inflada.

**5.4 Orden (decisión 7).** `claude-sonnet-5-5` puntúa la importancia de cada tripleta de 1 a 5 con una rúbrica fija, N = 3 con el
mismo mecanismo de re-muestreo de 4.4, y se ordena por el puntaje medio, con desempate por sorteo. Ordenar cientos de tripletas en un
solo pedido no es confiable; puntuar y ordenar es la forma operativa de «ordenarlas de la más importante a la menos importante».

**5.5 Calibración del orden.** La autora marca la importancia (escala de 3.4) de las 100 primeras y de 30 sorteadas entre las
posiciones 101 y 300, mezcladas y sin ver la posición. El orden pasa si al menos 80 de las 100 primeras son esenciales o útiles y si
esa proporción supera a la de las 30 de control. Si no pasa, el recall se reporta sobre las que la autora marcó esenciales, sin ranking.

**5.6 Presencia en dos pasos (decisión 8; ajuste 2).** (1) Subgrafo candidato, determinístico: los nodos cuya procedencia es la unidad
del fragmento, sus ancestros (herencia) o sus descendientes según la política de descendientes declarada (frontera ancla/chunk, B4.1
(b)), con las aristas de contenido entre ellos; su tamaño se registra por fragmento (en V, mediana unos 21.000 caracteres y percentil 90
unos 68.000, dimensionado provisorio del §8). (2) Un **juez de presencia** con la misma metodología del §4: `claude-sonnet-4-6` a
temperatura 0, por la API con caché; clasifica tres componentes de la tripleta abierta contra el subgrafo, {sujeto, predicado, objeto}
en {expresado, parcial, ausente}, nombrando el nodo o la arista que lo expresa; el **código** controla que lo nombrado exista y computa:
*presente* = los tres expresados; *parcial* = sujeto y objeto expresados con el predicado parcial, o dos expresados y uno parcial;
*ausente* = el resto; *requiere adjudicación humana* cuando el juez lo marca. Calibradores: casos resueltos por la autora sobre fragmentos
del pool de calibración (20 fragmentos reservados en el sorteo, disjuntos de los 300), nunca sobre las 100 primeras; N = 3 con el
re-muestreo de 4.4; veredicto modal; la misma prohibición de ajuste de 4.7. La autora decide la presencia de las 100 primeras con el
subgrafo a la vista; el juez escala si acuerda en al menos 84 de 100, con el kappa de Cohen reportado. Una regla solo de cadenas no
alcanza: la tripleta abierta está en las palabras del texto y el grafo en el esquema. **Se aparta de la letra de B4.1 (b)** («match de
sujeto/objeto normalizados + relación», `plan:433-434`); declarado a los mentores (§11).

**5.7 Recall@k** con k = 10, 50 y 100 (`plan:450-451`): presentes / k, con Wilson; «parcial» aparte.

**5.8 Revisión de las ausentes** (B4.1 (e)). La autora revisa cada ausente de las 100 primeras: si la tripleta es correcta según el
fragmento (si no, error del gold: sale del denominador y se cuenta), si está en el grafo y el juez no la vio (error de presencia:
se corrige y se cuenta) y si es importante. Recall crudo y depurado, los dos con sus conteos. Las ausentes importantes van al
backlog con su `capa_pipeline` (B4.4): son insumo del grafo corregido, nunca del evaluado.

## 6. Etiquetado asistido y experticia (D12; decisiones 9 y 10)

**6.1 Asistente.** Claude Code (`claude -p --bare`, solo lectura sobre el paquete de fichas) arma cada ficha y, donde se usa, una
propuesta de etiqueta con el tramo que la sostiene y la información para comprobarla: texto propio y heredado, ruta del PDF y
página, y la dirección del TO en el sitio del BCRA si el manifiesto la tiene.

**6.2 Dónde se usa la propuesta (la autora confirma sí o no).** En la revisión de las ausentes (5.8), en la clasificación por
experticia (6.3) y, si el juez no pasa, en la ampliación de la muestra de precisión, declarada como asistida; en 20 de esas
tripletas se toma además la etiqueta a ciegas, para medir cuánto cambia la propuesta la respuesta. No se usa en el gold (4.5), en
el pool de calibración ni en las calibraciones de 5.5 y 5.6.

**6.3 Clasificación por experticia.** El asistente marca cada tripleta como «la decide la autora» o «necesita un experto del
dominio», con el motivo; la autora confirma sí o no **después** de etiquetarla, para no sesgar el juicio. Las confirmadas como
«necesita experto» quedan como no decidibles por la autora (3.6).

**6.4 Vía al experto (decisión 10).** U-PREP-CONTACTO (`plan:1174-1178`) y el registro del 04/09, §3: anotación experta de una submuestra
en modo literal (`docs/registro_reunion_mentores_2026-09-04.md:77-97`). Quién adjudica (checklist P15 y Q12, `:105` y `:209`; F-7 y C-8)
se decide con los mentores. Sin experto, la evaluación corre igual y declara las no decidibles con su conteo.

## 7. Etapa T, dentro del pre-registro de B6.3

- Precisión: el juez calibrado sobre 400 aristas del grafo evaluado, con la estratificación de 3.2 y los dos estimadores de 3.6 (unos
  ± 0,035 con 0,85); control a ciegas de la autora sobre 30 sorteadas entre ellas. Si el acuerdo es menor que 26 de 30 (límite inferior
  de Wilson 0,7032), la cifra del juez se declara no validada en el escalado y se reporta la de las 30.
- Cobertura: 600 fragmentos de los TOs del conjunto de test (disjuntos de los 15 y de los 5 de la tanda 0, checklist Q10, `:207`),
  con 5.3 a 5.8 iguales y control de 30 en la presencia.
- B6.3 (d) incorpora todo esto en su pre-registro sellado (laudo D-f §5, `966253e:…:52`; checkbox del plan `:977-978`).

## 8. Costo y topes (decisión 11; ajuste 6)

**Dimensionado sobre datos reales** (grafo de V `2922b72d…` y E0 r2b de desarrollo; sorteo provisorio con otra semilla, solo para medir
tamaños, que no es la muestra): ficha de precisión (los dos nodos con sus propiedades, el predicado y la evidencia con herencia) mediana
2.044 caracteres, media 2.152, percentil 90 3.435; fragmento con herencia mediana 979, media 1.127, p90 2.078; subgrafo de presencia
(nodos y aristas de la unidad y sus descendientes) mediana 21.126, media 30.196, p90 68.298. Conversión a tokens con la razón marginal
medida en los pedidos de E1 (3,06 caracteres por token, ajuste sobre 2.438 pedidos; `data/experiment/e3_listas/freno_o1.md:21`): ficha 703 tokens (p90 1.123),
fragmento 368 (p90 679), subgrafo 6.904 (p90 22.320). **Los tokens no están contados con el tokenizador de la API: el lote piloto de 10
mide los tokens reales de cada pedido (`usage`) y re-ajusta esta tabla antes de seguir.**

Precios por millón de tokens (entrada / salida / escritura de caché / lectura de caché): `claude-opus-5-5` 4 / 20 / 5 / 0,2 y
`claude-sonnet-5-5` 2 / 10 / 2,5 / 0,2, los medidos en C1 de U-COMP-E1 (`comp_e1/c1/comun_c1.py:34-35`); `claude-sonnet-4-6` 3 / 15
(`plan:775`), con escritura 3,75 y lectura 0,30 (regla general de 1,25× y 0,1×, NO VERIFICADA contra la tarifa publicada). Supuestos de
prefijo fijo cacheado (instrucciones y calibradores): juez 3.000 tokens, extracción 1.000, puntaje 600; salidas: juez 300, extracción
150, puntaje 50, presencia 200.

| componente | llamadas V | USD V (mediana / p90) | llamadas T | USD T (mediana / p90) |
|---|---|---|---|---|
| juez de precisión (Sonnet 4.6, N = 3) | 300 | 2,44 / 2,82 | 1.290 | 10,47 / 12,10 |
| extracción abierta (Opus 5.5) | 300 | 1,41 / 1,78 | 600 | 2,81 / 3,55 |
| puntaje de importancia (Sonnet 5.5, N = 3) | 900 | 0,78 | 1.800 | 1,55 |
| juez de presencia (Sonnet 4.6, N = 3, 100 primeras) | 300 | 7,53 / 21,40 | 300 | 7,53 / 21,40 |
| **total** | | **12,2 / 26,8** | | **22,4 / 38,6** |

**Topes (decisión 11): V USD 35 y T USD 55.** El margen cubre el percentil 90 del subgrafo de presencia, que es el término que más varía
(si los subgrafos salen más grandes que el p90, se acota la política de descendientes antes de seguir, declarado), más la recalibración
única del §4.7. Freno duro por presupuesto en el script, con registro de gasto por llamada, como en C1 de U-COMP-E1. Tiempo de la autora:
gold de 100, pool de 20, orden de 130, presencia de 100 (más 20 del pool), ausentes de hasta 100 y controles de T; unas 10 a 14 horas.

## 9. Q7 (B4.2 contra B6.3 (d))

B6.3 (d) pasa a decir «con el instrumento validado en desarrollo (B4.2 y B4.3), cerrado antes de sellar el pre-registro de B6.3»; B4.2 y
B4.3 quedan como precondición de ese pre-registro (asentado en el plan el 07/10/2026). Resuelve la inconsistencia de `plan:445` y del
checklist Q7 (`:204`).

## 10. Lo decidido al firmar (decisiones de la autora del 07/10/2026)

1. Grafo de la etapa V: el de desarrollo r2b sin cola (`2922b72d…`), con la nota al laudo D-f. 2. Predicados derivados fuera de la
muestra: la lista del §3.1, fijada al sellar; `aplica_a` dentro. 3. Importancia en tres valores (esencial, útil, accesoria); la
precisión sobre las esenciales como cifra aparte, sin pesos. 4. Juez: `claude-sonnet-4-6` a temperatura 0, por la API. 5. Criterio de
acuerdo: las tres condiciones del §4.6, con el kappa de Cohen reportado y no como umbral. 6. Tamaños: 100 y 300 en V; 400 + 30 y 600 en
T. 7. Extracción `claude-opus-5-5` y puntaje `claude-sonnet-5-5`, con la condición del §5.3. 8. Presencia en dos pasos, declarada como
desvío de la letra de B4.1 (b). 9. Gold a ciegas, con los usos del modo asistido del §6.2. 10. Vía al experto del §6.4. 11. Topes: V USD 35
y T USD 55, re-estimados con el piloto.

## 11. Desvíos declarados (van a la lista para los mentores)

- El gold de 100 se etiqueta sin ver la sugerencia del modelo: se aparta de la letra de D12 para la parte del gold (la sugerencia con
  sí/no sigue en ausentes, experticia y ampliación).
- La presencia de una tripleta la decide un juez calibrado en dos pasos sobre el subgrafo de su unidad, no una regla de cadenas: se
  aparta de la letra de B4.1 (b).
- El instrumento se valida sobre el grafo de desarrollo r2b y no sobre r1: se aparta de la letra del laudo D-f (nota al pie del laudo).
- Los jueces corren por la API, no con Claude Code (ya en la lista por D2).

## Comandos de los recuentos de este documento (regla i)

```
# aristas por predicado del grafo de desarrollo r2b sin cola (22.084; contenido 3.983)
python3 -c "import json,collections;kg=json.load(open('data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo_r2b_sincola/r2/kg.json'));print(len(kg['edges']),collections.Counter(e['relation'] for e in kg['edges']).most_common())"
# unidades de la E0 r2b de desarrollo con texto propio de 80 a 1.500 caracteres (1.491 de 1.768)
python3 -c "import json,glob;L=[len(u.get('texto') or '') for p in glob.glob('data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b/chunks_*.json') for u in (lambda d: d['chunks'] if isinstance(d,dict) and 'chunks' in d else d)(json.load(open(p)))];print(len(L),sum(80<=x<=1500 for x in L))"
# Wilson al 95 % (z = 1,959964): 84/100 -> 0,7558; 26/30 -> 0,7032; ancho con 0,85: n=100 0,0699, n=400 0,0350
# dimensionado del §8: sorteo provisorio random.Random("DIMENSIONADO_PROVISORIO_NO_ES_LA_MUESTRA").sample(...) sobre las 3.983 aristas de contenido y 1.491 fragmentos; caracteres de ficha, fragmento y subgrafo como se describe; conversión a 3,06 caracteres por token; costos con los precios de arriba
```

## Firma

PENDIENTE DE FIRMA de la autora.
