# U-MED-UMBRALES — propuesta: cómo medir si los campos de los umbrales son correctos

Unidad de diseño en una etapa, USD 0, sin API y sin ninguna lectura de umbrales. HEAD `1f9b262` al inicio y `18d9e05` al cierre: entraron
tres commits que no son de esta sesión (`293fe8d`, `33c43e9`, `18d9e05`), y ninguno toca un archivo que cito
(`git diff --name-only 1f9b262 HEAD`). No toqué el repo: escribí solo en el scratchpad. El texto normativo está en
`borrador_enmienda1_preregistro_tripletas_umbrales_U-MED-UMBRALES.md` (BORRADOR, sin firmar); acá van las razones, las opciones y lo que
decide la autora. Los recuentos de este documento son estructurales: cuántos elementos hay en cada estrato del marco de muestreo, sobre
copias de los `kg.json` en el scratchpad. No juzgan ningún campo (detalle en el FRENO).

## Resumen

- **Vehículo:** una enmienda al pre-registro de tripletas (la opción preferida del mandato), con una vía propia de umbrales. Es
  admisible porque la evaluación no sorteó nada todavía.
- **Unidad:** el elemento de umbral. **Cifra principal:** el *núcleo* (pertinencia, valor, unidad, moneda, comparación y base literal),
  con el *completo* y el *núcleo contra la definición* al lado.
- **Hallazgo del recuento:** 305 de los 1.306 elementos del grafo sin cola de la tanda 0 (23 %) están vacíos: son del validador, sin
  valor, sin base y con la comparación `no_determinada`. No afirman ningún monto, así que van aparte y no entran al núcleo.
- **Medición:** 240 elementos con contenido del grafo evaluado, en los TOs de test, más el censo de las bases resueltas y 30 vacíos. La
  mitad del ancho del intervalo da 0,0498 con p = 0,85.
- **Quién lee:** la autora, con una regla sellada y una lectura en dos pasos que no muestra los campos del grafo en el primero. USD 0;
  entre 8 y 13 horas suyas (estimación NO VERIFICADA).
- **Afirmación:** «el grafo guarda correctamente hasta qué monto…» solo si el límite inferior del núcleo y el de la comparación llegan a
  0,90 (decisión D5).
- **Piloto:** 40 elementos de la tanda 0, para fijar la regla y encontrar clases de error. Las clases se corrigen en código antes del
  sello (grupo 2), con un test por clase.

## Enmienda o pre-registro aparte

**Recomiendo la enmienda (decisión D1).** Razones:
1. **No corrió nada.** El sorteo de V espera el re-sellado único (`docs/laudo_release_r2_pipeline.md:53`), y el repo no tiene ninguna
   muestra, ficha ni etiqueta de tripletas (`git ls-files | grep -i tripleta`). Agregar una vía antes de sortear no usa ningún dato.
2. **Es el mismo objeto:** el contenido del grafo, en el componente (d) de B6.3 (`plan:778`). Usa los mismos grafos y sellos, el mismo
   armador de fichas, el mismo sorteo sellado y los mismos estimadores (`4afbe51:docs/preregistro_evaluacion_tripletas.md:67-71`,
   `:85-95`). Un pre-registro aparte sería un tercer instrumento en B6.3, con su propia lista de desvíos.
3. **Hay precedente.** Son tres enmiendas separadas al pre-registro firmado de la tanda 0. Ninguna de las once decisiones ni ninguno de
   los topes de tripletas cambia.

**Lo que habría hecho mejor un pre-registro aparte:** separar la etapa de desarrollo (el piloto y las correcciones de código), que no es
evaluación. La resuelvo con secciones propias (§9 y §10 del borrador), y la regla de no contaminación es la misma en los dos vehículos.

**Una nota sobre el mecanismo.** El pre-registro de tripletas no tiene una cláusula de enmienda. Solo dice que el texto firmado recibe
notas fechadas al pie (`4afbe51:…:6-7`). El de la tanda 0 sí la tenía («toda modificación posterior es enmienda separada», citado en
`docs/enmienda_preregistro_tanda0_2026-09-30_ventana.md`). La enmienda se apoya en ese precedente y vale por la firma de la autora;
lo dejo declarado.

## 1. Unidad y campos

Ver el borrador, §2. Lo esencial:
- **Unidad:** el elemento de `properties.umbrales`.
- **Referencia:** la letra de la norma (texto propio y heredado de E0, y el PDF si hace falta), leída con las definiciones firmadas:
  L-ESQ-R2 §1.3 (`4ef7650`), sus enmiendas 3 (`8d01b04`) y 5 (`3a4b980`) y la calibración P3 (`plan:401`). El código es lo que se mide,
  nunca la referencia.
- **Campos:** pertinencia (como precondición), valor, unidad, moneda, tipo de días, comparación, base literal y destino de la base.
  Cada uno con su definición de correcto y sus casos límite (tabla del §2.3).
- **«Mayor que» frente a «mayor o igual que»:** estricto por inclusivo es *contradicha*, porque L-ESQ-R2 §1.3, punto 2, dice que la
  distinción cambia la respuesta.
- **Dos lentes para la comparación.** Una *omitida* (el grafo dice `no_determinada` y la letra fija un sentido) puede ser de
  implementación (el código no aplicó una forma que la definición cubre) o de la definición («entre 30 días y 90 días», límite
  declarado en `plan:401`):
  - el **núcleo**, que es la cifra de la afirmación, cuenta las dos como error;
  - el **núcleo contra la definición**, que es el diagnóstico de las correcciones, cuenta solo la primera.
  - La diferencia mide lo que el esquema no expresa.
- **Los vacíos** (sección «Hallazgos»): contarlos como correctos inflaría la cifra, y contarlos como errores de monto mezclaría dos
  preguntas. Van aparte, con tres clases: oculta un umbral, límite sin cuantía en la letra, no es un umbral.
- **Por qué la lectura va en dos pasos:** primero la lectura sin los campos del grafo, después la comparación en código y la revisión
  de las diferencias. Con el campo a la vista, el lector tiende a confirmarlo, sobre todo en la comparación y en la base. Es el mismo
  principio del gold a ciegas del pre-registro (`:129-131`), aplicado a lo único que puede ocultarse (la cuantía resaltada ya muestra
  el valor y la unidad).

## 2. Población y muestra

- **Población de T (decisión D2):** los elementos del grafo evaluado sin cola, en los TOs que no están en
  `documentos_excluidos_evaluacion_final.json` (n = 15). Es la disjunción de B6.3 (a) y de la cobertura de T (`4afbe51:…:220-221`), y
  deja al piloto (la tanda 0) fuera de la medición.
- **Estratos:** autor × origen × base, como pide el mandato, más un estrato censal de bases resueltas y uno aparte de vacíos. Tamaños en
  el grafo sin cola de la tanda 0: 652 / 76 / 88 / 18 / 7 / 150, más 10 resueltas y 305 vacíos, que suman 1.306
  (`estratos_umbrales_salida_UMEDUMBRALES.txt`, `vacios_y_resueltas_salida_UMEDUMBRALES.txt`).
- **Tamaño (decisión D4).** La precisión objetivo declarada es una mitad del ancho de 0,05 al 95 % para el núcleo ponderado, con
  p = 0,85, el valor del pre-registro (`:86`). El cálculo está en `tamano_muestra_salida_UMEDUMBRALES.txt`:
  - con muestreo simple, n₀ = 196;
  - con un mínimo de 25 por estrato, el efecto de diseño es 1,21 con los pesos de la tanda 0, y 240 da 0,0498 (0,0557 con p = 0,80);
  - las alternativas: 180 da 0,0625 y 400 da 0,0360;
  - al sellar, la asignación se recalcula con los N_h reales; si la mitad del ancho pasa de 0,05, se agregan elementos hasta un tope
    de 300. Es una regla fijada antes de ver datos.
- **Concentración:** en la tanda 0, ext y cap tienen 926 de los 1.306 elementos, y los cinco TOs nuevos solo 143. Si el grafo
  evaluado repite el patrón, unos pocos TOs pesarán mucho en la cifra. Por eso el TO va como covariable y la frase de la tesis habla
  de la población, no de cada TO.

## 3. Quién juzga (decisión D3)

| opción | quién lee | USD | horas de la autora (NO VERIFICADO) | riesgo |
|---|---|---|---|---|
| **A (recomendada)** | la autora, con regla sellada y dos pasos | 0 | 8 a 13 | ninguno de instrumento; es la que más horas le pide |
| B | juez por la API (`claude-sonnet-4-6`, T = 0, N = 3, la maquinaria del §4 del pre-registro), calibrado en la tanda 0 | unos 13,8 (p90 15,9; tope propuesto 20) | 7 a 10 | si no pasa la validación o el control de 30, T vuelve a A y suma de 5 a 7 horas |
| C (descartada) | dos sesiones de Claude Code y adjudicación de la autora | 0 | 3 a 4 | el principio 8 pide que los jueces de las evaluaciones nuevas corran por la API, con captura y caché (`plan:272-279`) |

**Por qué A.** Con 240 elementos, el juez casi no ahorra horas: para validarlo, la autora igual lee unos 150 elementos (pool de 20,
validación de 100 y control de 30). Además agrega costo y un riesgo de no pasar. B conviene solo si se quiere bajar a ±0,036 con 400
elementos.

**Si se elige B, la calibración** (borrador, §6):
- los casos resueltos salen de un pool de 20 de la tanda 0;
- la validación es sobre otros 100 de la tanda 0, leídos a ciegas por la autora;
- pasa con al menos 90 de 100 en el veredicto del núcleo (Wilson 0,8256), con una diferencia de exactitud de 0,03 o menos y marcando
  al menos dos tercios de los incorrectos;
- **cuándo se deja de ajustar:** una sola recalibración, con casos del pool y nunca con las 100; si no pasa, el juez no escala;
- en T, la autora controla 30 a ciegas y exige al menos 27 de 30 (Wilson 0,7438).

El productor de los campos es código determinístico, no un modelo. Por eso un juez de modelo no comparte sus sesgos, salvo en los
elementos que salen de la descripción.

## 4. Qué se informa y qué umbral hace falta para afirmar

- **Qué se informa** (borrador, §7):
  - el núcleo, el completo y el núcleo contra la definición, cada uno en dos cifras (la cruda con Wilson y la ponderada con Wald), como
    en el §3.6 del pre-registro;
  - por campo, sobre los elementos donde aplica, con un estimador de razón para la ponderada;
  - por estrato, en fracción cruda si n < 20;
  - los vacíos, con su censo y sus tres clases;
  - las covariables, el inventario de clases de error, los no decidibles con sus dos cotas y el tiempo por ficha.
- **Umbral para la afirmación (decisión D5):**
  - **0,90 en el límite inferior del núcleo** (en las dos cifras) **y de la comparación**;
  - entre 0,80 y 0,90, la cifra con una frase acotada;
  - debajo de 0,80, límite declarado.
- **Por qué 0,90.** Con un umbral mal guardado, la norma se aplica o no se aplica al revés. Un error en diez es lo más que se puede
  tolerar para recomendar el campo como fuente de la respuesta, con el tramo citado.
- **Qué se puede esperar con 240** (n efectivo cerca de 198; `tamano_muestra_salida_UMEDUMBRALES.txt`, §4): la afirmación sale con
  probabilidad 0,70 si la exactitud real es 0,95, 0,98 si es 0,97 y 0,25 si es 0,93. Con 0,95 como umbral, la probabilidad es 0,43
  aun con una exactitud real de 0,98.
- **Qué no permite decir:** que el agente responda bien. Grounded no es correct. Recomiendo que el pre-registro de B6.3 informe aparte
  la fidelidad en las preguntas cuyo gold depende de un umbral (se decide al sellar B6.3).

## 5. El piloto y por qué no contamina la medición

- **Muestra:** 40 elementos del grafo sin cola de la tanda 0 vigente, 4 por estrato más 8 de los cinco TOs nuevos, en dos lotes con un
  FRENO entre ellos.
- **Para qué:** fija la regla y la ficha, que se sellan antes del sorteo de T, y produce el inventario de clases de error.
- **No da cifra para el capítulo 5.**
- **Por qué no contamina:**
  - los documentos son disjuntos: la tanda 0 está fuera de la población de T;
  - el orden es fijo: regla → correcciones → sello → sorteo → lectura, y nada de T vuelve al código ni a la regla (principio 9,
    `plan:281-288`);
  - lo que T mide es justamente si la regla y las correcciones generalizan.
- **El riesgo residual** es que la regla no prevea alguna forma de los TOs nuevos. Lo cubren el «no previsto» y las cotas de los no
  decidibles.

## 6. Dependencias y costo total

- **Dependencias:**
  - la firma;
  - el armador de fichas y el formulario de dos pasos (código, USD 0);
  - el grafo sin cola de la tanda 0 para P, y el grafo evaluado sellado para T;
  - la regla sellada, que entra al pre-registro de B6.3 como parte de (d).
- **No depende** de la etapa V ni del juez de tripletas con la opción A.
- **Calendario:** P apenas se firme, en paralelo con la tanda 1, para que las correcciones lleguen al grupo 2.
- **Costo de API:** USD 0 con la opción A. Con B, unos USD 13,8 (`costo_juez_umbrales_salida_UMEDUMBRALES.txt`), aparte de los topes
  de V y T.

## 7. Tiempo de la autora y trabajo compartido con tripletas

- **Tiempo:** con la opción A, entre 8 y 13 horas:

  | parte | horas |
  |---|---|
  | firma | 0,5 |
  | piloto | 1,5 a 2 |
  | decisiones de clases | 0,5 a 1 |
  | T, 240 elementos a 1,25–1,75 minutos | 5 a 7 |
  | 30 vacíos | 0,5 |
  | censo de bases resueltas | 0,3 a 2 |

  La estimación es NO VERIFICADA: el repo no tiene tiempos de lectura medidos, y el §8 del pre-registro supone unos 1,3 a 1,8 minutos
  por juicio. El piloto mide el tiempo real.
- **La misma ficha para las dos evaluaciones casi nunca se da.** La autora solo lee 30 aristas en T, y la muestra de umbrales es de
  elementos de otra población. Se esperan entre 0,35 y 2,0 fichas comunes (`solapamiento_tripletas_salida_UMEDUMBRALES.txt`).
- **Cuando se da:** una sesión, dos formularios y un orden fijo (primero la tripleta, cerrada; después el umbral). El solapamiento se
  declara y no se excluye, como en el pre-registro (`:41-42`).
- **Lo que sí se comparte:**
  - el armador de fichas, el sorteo sellado, los estimadores y el acta de T;
  - las sesiones de lectura;
  - opcionalmente (decisión D9), las observaciones de umbrales en las 24 aristas de 100 de V que se esperan con un extremo con
    umbrales (956 de 3.983 en `2922b72d`), sin cifra.
- **Por qué no rompe la independencia:**
  - ninguna etiqueta cruza de una vía a la otra;
  - las semillas son distintas;
  - la muestra de umbrales no se saca de las aristas de tripletas, porque eso sesgaría hacia los nodos con más aristas.

## 8. Errores sistemáticos: corrección de código antes del sello

Borrador, §10.
- **Qué es una clase:** el mismo campo, la misma regla y la misma forma de la letra, con dos o más casos en el piloto, o uno más su
  censo determinístico.
- **Qué se corrige:**
  - se corrigen en código solo los errores de implementación;
  - los de la definición, solo después de una enmienda firmada a L-ESQ-R2;
  - los de E1 o E0 no se corrigen por esta vía: van al backlog como límite.
- **Cada clase lleva:**
  - una ficha con su censo;
  - un test de regresión con el tramo real del piloto y una variante sintética;
  - el control negativo (fallan antes de la corrección y pasan después, y el resto de la suite sigue en verde);
  - el re-ensamblado sobre lo guardado (USD 0, principio 12), con la lectura de los elementos que cambian;
  - el gate de release antes del sello.
- **Por qué no contamina:** las correcciones salen de la tanda 0 y son reglas generales. La medición es de otros documentos, sobre el
  grafo sellado después. Los elementos que motivaron una corrección son casos de test y no evidencia de mejora.

## Decisiones de la autora (con la recomendación de la mesa)

| | decisión | opciones | recomendación |
|---|---|---|---|
| D1 | vehículo | enmienda; pre-registro aparte | enmienda |
| D2 | documentos de T | TOs fuera de los quince; todo el grafo evaluado sin los elementos del piloto | fuera de los quince |
| D3 | quién lee | A, la autora; B, el juez por la API | A |
| D4 | tamaño de T | 180; 240; 400 (solo con B) | 240 |
| D5 | umbral de la afirmación | 0,85; 0,90; 0,95 | 0,90 |
| D6 | piloto | 40 en dos lotes; 60 | 40 |
| D7 | semillas de P y de T | a fijar en la firma | — |
| D8 | tipo de días fijado por una regla general del TO | informativo; exigido | informativo |
| D9 | lectura adosada en V | opcional, sin cifra; no | opcional |
| D10 | corrección de clases antes del sello | en el grupo 2; ninguna (todo al grafo corregido) | en el grupo 2 |

## Hallazgos del recuento estructural (no son mediciones de corrección)

1. **Vacíos.** 305 de 1.306 elementos en el grafo sin cola de la tanda 0 y 314 de 1.373 en `a9631a64` son elementos sin valor, sin
   base y con la comparación `no_determinada`, todos del validador (`vacios_y_resueltas_salida_UMEDUMBRALES.txt`). Las cifras del tipo
   «1.373 umbrales» los incluyen.
2. **Comparación no determinada.** Afecta a 636 de 1.306 elementos (331 del ensamblado y 305 del validador;
   `estratos_umbrales_salida_UMEDUMBRALES.txt`). Cuántos son correctos por la letra y cuántos son omisiones es la pregunta que separan
   las dos lentes.
3. **Concentración por TO.** Los cinco TOs de desarrollo tienen 1.163 de los 1.306 elementos.

## Contradicciones y notas

- **Ninguna cifra del mandato contradice al repo.** 1.373 en 1.166 nodos, 895 (134 de la descripción), 478, 1.361, 264 y 11 (6 y 5) se
  reproducen. Re-corrí el script de VERIF-UMBRALES sobre una copia de `a9631a64` y la salida es idéntica a la de su paquete (`diff`
  vacío).
- **Me aparto de la letra del mandato en los estratos:** agrego el de vacíos dentro del validador. La razón es la de la sección 1.
- **El mecanismo de enmienda del pre-registro** se apoya en precedente y no en una cláusula propia (ver «Enmienda o pre-registro aparte»).
- **La opción C** del mandato («juez de modelo») queda limitada por el principio 8: solo un juez por la API es admisible para B6.3.

## Lo que no hice

- No corrí ninguna medición ni llamé a ningún modelo.
- No leí ni juzgué ningún campo de ningún umbral.
- No toqué el repo.
- No cuento como hechos el commit, la firma ni el despacho de nada de esto: son acciones de la autora y quedan PENDIENTES.
