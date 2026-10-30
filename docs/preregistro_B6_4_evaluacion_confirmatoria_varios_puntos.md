# Pre-registro de B6.4, la segunda evaluación confirmatoria: preguntas que juntan varios puntos

**FIRMADO por la autora el 30/10/2026** (recibida a las 00:25:13): el borrador v5 de la mesa (§350, `e4c2c42b…`), commiteado tal
cual en el commit anterior, con las decisiones de su §14. No sellado como medición: ningún número de este documento es un resultado.
Desde esta firma es el pre-registro de B6.4. La v5 era la v4 (§349) con D-1 (b), D-6 (b) y las demás decisiones; la v4, la v3 (§344)
con el alcance de la corrección ampliado (N7c+); la v3, la v2 (§343) con C-1 a C-3 y D-10; la v2, la v1 (§340) con la corrección de
las 19:04:03.
De la mesa (29/10/2026, §340 y §343). Ningún número de este documento es un resultado de B6.4. Lo firma la autora y
se sella con su commit; la ruta propuesta en el repo es `docs/preregistro_B6_4_evaluacion_confirmatoria_varios_puntos.md` (D-9).

- **Lo que la mesa leyó para armarlo:**
  - del resultado de B6.3, solo el ancho del intervalo bootstrap de d_q de cada comparación y su número de preguntas, en el total y en
    varios puntos, para la potencia (§3.4). Ninguna media, ningún extremo de intervalo, ningún p;
  - de las 96 preguntas de B6.3, solo el TO de cada ancla, por código, para los documentos elegibles (§3.1);
  - ninguna pregunta, ningún criterio, ninguna respuesta, ningún veredicto y ninguna traza.
- **Las fuentes:**
  - el pre-registro de B6.3, leído en el commit de su firma (`adf20f3b`; regla k);
  - su sorteo sellado (`sorteo_B63.json`, `4e751e23…`) y el resumen de su corrida (`data/experiment/banco_mcp/b63/real/resumen_b63.json`);
  - los scripts de la mesa de `decisiones_337_mesa/` y `decisiones_340_mesa/`, con sus consolas.
- **Una marca,** la de los borradores firmados del proyecto: «HUECO H-n», un valor que todavía no existe, con la regla que lo llena.
  Las decisiones D-n ya están tomadas: cada una dice cuál, y la tabla del §14 las junta.

## 0. Los huecos

| hueco | qué | de dónde sale | regla |
|---|---|---|---|
| H-1 | el sorteo de B6.4 y su sello | `sortear_B64_mesa.py` (autoprueba 31 de 31), con las semillas del §3.3, al firmar | su sello |
| H-2 | las olas selladas, lo aprobado y las rechazadas por tipo | la generación y la revisión de la autora (§3.3) | sus sellos |
| H-3 | la entrada de B6.4 y su sha256 | la de B6.3 con las preguntas aprobadas, sus ids y su orden | se copia del commit de las preguntas |
| H-4 | el seco del runner con la entrada de B6.4 | su FRENO revisado | §6 |
| H-5 | lo gastado hasta la firma | el registro de gastos de la autora | si con el tope del §12 pasa el techo, decide la autora |
| H-6 | el código del análisis y el de la exactitud de cita, su prueba y su sello | la etapa del código, antes de la corrida | §8.4, §9 |
| H-7 | la corrección: servidores y configs de N7c y N7c+, con sus sha256 | el 241, antes de ver ninguna pregunta | §4 |
| H-8 | B2 en N3 y la configuración que adopta su regla (D-B2-9) | B2 y su análisis | si no adopta ninguna, el grafo es N7 |

## 1. Qué es B6.4

Las tres decisiones de la autora, tal cual («tomadas antes de generar ninguna pregunta»; 29/10/2026, recibidas a las 16:35:20):
1. «B6.4 es una segunda evaluación confirmatoria, con su propio pre-registro: mide si el grafo supera a los dos sistemas por fragmentos
   en preguntas que necesitan juntar información de varios puntos o documentos. Se informa junto con B6.3, sea cual sea su resultado, y
   B6.3 no se toca. Se declara que B6.4 se diseñó después de ver el resultado de B6.3.»
2. «Todo lo demás como en B6.3: el mismo agente con la configuración de N7, los mismos dos sistemas por fragmentos, el mismo juez de EV2
   con la lectura tolerante, k = 3, la prueba pareada por permutación con Holm sobre las dos comparaciones, una muestra de control con
   mi lectura y el código del análisis de B6.3, reusado sin cambios en lo que se pueda.»
3. «Las preguntas se generan como siempre: una instancia nueva de Claude Code, sin contexto de la tesis, con solo los documentos fuente,
   de documentos que no estén en las 96 de B6.3. Las reviso una por una y se sellan antes de correr.»

Y el tamaño (29/10/2026, recibida a las 17:09:15), tal cual: «B6.4 va con 96 preguntas, 32 por tipo, para detectar una diferencia de 10
puntos con una potencia de alrededor de 0,85: 48 no alcanzan.»

Y la corrección del sistema del grafo (29/10/2026, recibida a las 19:04:03), tal cual: «Para B6.4 corrijo el sistema del grafo antes de
correrla. Lo decido con el detalle por ancla de la salida de la atribución (fec4a204…), que miré después de sellar: de las 25 sesiones
de generación de varios puntos, en 12 el agente consultó las dos anclas; en 9 la segunda estaba en el grafo y el agente nunca la vio ni
la consultó; en 2 la vio y no la consultó; en 2 la segunda no está en el grafo. La corrección apunta a que el agente siga los puntos
relacionados con el que abre. Las instrucciones del agente no se tocan, para que sigan iguales en los tres sistemas, y los dos sistemas
por fragmentos quedan como se eligieron en N7, declarado como límite. La corrección se diseña y se prueba con preguntas de desarrollo,
nunca con las de B6.3 ni con las de B6.4, y queda fija antes de que yo vea ninguna pregunta de B6.4.»

Y su alcance (29/10/2026, recibida a las 23:49:29), tal cual: «Quiero arreglar todo lo que se pueda del sistema del grafo
antes de B6.4, con desarrollo y sin tocar las instrucciones del agente, los sistemas por fragmentos ni el contenido del grafo
evaluado.»

- **Su familia:** B6.4 es una familia de pruebas aparte, con su α. No se combina con B6.3 en ninguna prueba.
- **El diseño, después del resultado de B6.3:** la hipótesis y los tipos se eligieron después de ver el resultado de B6.3, y así se
  declara en la tesis, junto a los dos resultados (§10).

## 2. Lo que no se hace

- Nadie ve el grafo ni resultados del agente sobre preguntas de B6.4 antes de sellar el sorteo, las olas y lo aprobado.
- No se cambia una cuota ni un tipo después de generar.
- Nunca corre una pregunta sin revisar, y B6.4 no arranca sin las 96 aprobadas (D-3).
- B6.3 no se toca: ni sus preguntas, ni su análisis, ni su informe.

## 3. Las preguntas

### 3.1 Los documentos

- **Los elegibles:** los 77 de B6.3 (§3.1 de su pre-registro, con las mismas exclusiones: los 15 de la evaluación final, los 5 de la
  tanda 0 y los 14 de N3, sin contaminados), menos todo documento que aparezca en alguna ancla de las 96 de B6.3. Las anclas de B6.3
  tocan 37 documentos, 31 de ellos entre los 77. Quedan 46 (`decisiones_337_mesa/documentos/elegibles_B64.json`, `be47abcc…`):
  - **RI (10):** ri_esd, ri_tar, ri_ieccm, ri_iesinap, ri_secoexpo, ri_dsf, ri_ot, ri_msrl, ri_psp y ri_iepsp;
  - **NG_digerible (28):** ratiofn, fabcra, pfmipyme, icmecma, snp_atm, pognme, secfin, fgarcp, cescar, snp_debin, pscpp, fclef,
    supcon, gescre, incuca, osapsa, snp_spd, ordcom, rmrtsd, graloc, raapal, ccbcra, coltit, repefe, pimf, servco, convca y afiltr;
  - **NG_necesita_reglas (8):** cateloc, micemp, inspag, reqcac, horari, garopt, venliq y jafip.
- **Las anclas** (D-1, decidida: (b)): la unidad del lugar está en uno de los 46, y el otro punto, en cualquiera de los 128 documentos
  del grafo evaluado, como en B6.3. Lo que sigue de eso:
  - la carpeta de la generación lleva los PDF y la E0 que la regla necesita: los de los 46 y, para el otro punto, los de los 128;
  - una remisión a otro documento cuenta para el tipo remisión (§3.2);
  - B6.4 no queda disjunta de B6.3 en lo que lee. El otro punto puede caer en un documento con anclas de las 96 de B6.3 (37), en uno
    de los 14 de N3 (el desarrollo de la corrección), en uno de los 15 de la evaluación final o en uno de los 5 de la tanda 0. Después
    de la revisión de la autora se cuentan por código, por esas clases, las anclas que caen en cada una, y se declaran (§10, punto 4).
    Ninguna se descarta por eso.
- **La exposición:** la de cada documento sorteado, declarada como en B6.3 (§11, punto 11 de su pre-registro).

### 3.2 Los tipos y las cuotas

Tres tipos, que se excluyen entre sí. Cada pregunta necesita al menos dos unidades distintas de la E0, y la de agregación, al menos tres.
- **Agregación:** la pregunta pide todas las obligaciones o requisitos de un sujeto dentro de un TO, repartidos en tres o más puntos.
  - Sus anclas son de 3 a 5 unidades del mismo TO, y sus criterios, de 3 a 5, uno por punto, cada uno con su cita textual.
  - El conjunto tiene que estar completo en el alcance que nombra la pregunta: el TO entero, o una sección suya que la pregunta nombra.
    El generador busca en la E0 del TO las demás obligaciones de ese sujeto y deja la búsqueda en su registro.
  - Si son más de 5 en el TO, la pregunta acota el alcance a una sección donde sean de 3 a 5.
- **Remisión:** la respuesta exige seguir una remisión a otro punto, del mismo TO o de otro (con D-1). Es el frente (a) de la regla de
  tipos de B6.3 (`regla_P1.md`, `4b55ff66…`, §5, paso 2). Al menos un criterio sale del punto remitido.
- **Condición y excepción:** una regla con sus condiciones o excepciones, que están en otros puntos. Son los frentes (b), la excepción
  en un hijo, y (c), la condición en otro punto, de la misma regla. Los criterios traen la regla y al menos una condición o excepción de
  otro punto.
- **Lo que no es un tipo de B6.4:** la definición en otro punto, el frente (d), se declara.
- **Los criterios de lectura de B6.3** (su §3.2) rigen donde hablan de remisión y de condición. Rige también la regla del ancla de B6.3:
  las unidades candidatas de su sorteo.
- **Las cuotas:** 32 por tipo, en seis olas de 16. Cada ola tiene cuatro documentos con 4 lugares cada uno: 1 RI, 2 NG_digerible y
  1 NG_necesita_reglas (D-2). Los tipos van 6, 5 y 5, y el de 6 rota entre olas.
- **La clase de los documentos** (D-2, decidida: (a)): 1, 2 y 1 por ola, el 25, el 50 y el 25 %. B6.3 usó el 50 % de RI, pero solo
  10 RI son elegibles, y 12 harían falta.

### 3.3 El sorteo, la generación y la revisión

- **El sorteo,** apenas se firme y antes de que nadie lea nada (H-1):
  - con `sortear_B64_mesa.py` y las semillas `B64:sorteo:documentos:v1`, `B64:sorteo:unidades:v1` y `B64:sorteo:tipos:v1`;
  - los documentos por clase y las unidades de cada documento, en un orden sorteado;
  - las seis olas de 16, y el tipo de cada lugar, de una permutación con semilla;
  - un documento con menos de 4 unidades candidatas se salta, declarado;
  - lo que queda de cada clase es la reserva, en su orden.
- **La generación,** como P2 de B6.3:
  - a ciegas, desde los PDF y la E0, una pregunta por lugar, en el orden sellado;
  - una instancia nueva de Claude Code, abierta en una carpeta fuera del repo, sin el contexto de la tesis: solo lee sus insumos, los
    PDF y la E0;
  - cada ola sellada con su sha256, sus bytes y su hora antes de que nadie la lea;
  - en dos bloques (olas 1 y 2, y olas 3 a 6), con la revisión de la mesa entre medio;
  - USD 0.
- **Si la unidad de un lugar no sostiene su tipo:** el lugar pasa a la unidad siguiente del orden de ese documento que lo sostenga y no
  ancle otro lugar. Si ninguna lo sostiene, el lugar pasa al documento siguiente de su clase en la reserva, con su tipo, como la regla
  de los 13 reubicados de B6.3 (su §3.3). Las dos cosas se declaran. El tipo de un lugar no cambia.
- **La revisión de la autora:**
  - una por una, contra su PDF, en el orden de las olas;
  - una rechazada pasa a la unidad siguiente por la regla de arriba, con una pregunta nueva;
  - las rechazadas se cuentan y se declaran por tipo;
  - la generación no ve los motivos de la autora, solo la lista, como en B6.3.

### 3.4 El N y su potencia

- **N = 96,** 32 por tipo (decisión de la autora del §1).
- **La potencia de la afirmación del §8.1**, con Δ = 0,10 y el desvío de d_q de B6.3 estimado del ancho de sus intervalos:
  - con el desvío de varios puntos, el de las preguntas que más se parecen a las de B6.4: de 0,83 a 0,86;
  - con el del total: de 0,93 a 0,94.

  El rango va según la correlación entre las dos comparaciones (de 0 a 0,8). Usa el Holm del §8.1 y un efecto de diseño de 1,15, por las
  4 preguntas por documento con ρ 0,05, como B6.3 (`decisiones_337_mesa/potencia/`, `potencia_B64_mesa.py` y su consola).
- **48 y 64, como dato del diseño** (pedido de la autora), con Δ = 0,10:
  - 48: de 0,41 a 0,53 con el desvío de varios puntos, y de 0,61 a 0,67 con el del total;
  - 64: de 0,59 a 0,68, y de 0,77 a 0,81.

  Con Δ = 0,15: 48, de 0,88 a 0,90 y 0,96; 64, 0,96 y 0,99 (`decisiones_340_mesa/b64/potencia_B64_delta_015_mesa_consola.txt`).
- **Si al lanzar la primera sesión paga no están las 96 aprobadas** (D-3, decidida: (a)): B6.4 no arranca hasta que estén, sin corte
  por calendario.

## 4. Los brazos, lo común y las corridas

Como en B6.3, §4 a §6 de su pre-registro:
- el agente, el prompt, R5, la salida de las herramientas, el entorno de cada sesión, las 3 en paralelo, k = 3;
- el orden por pregunta y por repetición, con los brazos de cada pregunta seguidos;
- las corridas cortadas y las fallas de infraestructura.

Cambia lo que nombra B6.4: las preguntas, la entrada (H-3) y las carpetas de salida, fuera del repo (`fuera_del_repo/banco_b64/`). Y el
brazo del grafo:
- **El brazo del grafo es el que adopte B2 por su regla** (H-7 y H-8; D-B2-9), fijada antes de correr B2:
  - **N7c+,** si cumple (i) a (iii) frente a N7 y no baja su fracción de sesiones con cita fundada. Es la configuración de N7 con tres
    agregados al final de la salida de `ver_punto`:
    - la sección de C1, «Puntos relacionados»: los puntos unidos por remisión, condición o excepción;
    - «Puntos de la misma familia»: los cercanos en el árbol de la E0, hasta 10, sin texto;
    - la línea «Para citar este punto», con el PDF y la unidad en la forma que lee el instrumento de citas;
  - **si no, N7c,** solo con la sección, si cumple (i) a (iii);
  - **si no, N7** tal cual.

  Se fija antes de que la autora vea ninguna pregunta de B6.4. Los criterios son los de B2: (i) la fracción de sesiones de varios puntos
  que consultan todas las anclas sube; (ii) la fidelidad no baja más de 5 puntos, ni en el total ni en dato directo; (iii) las sesiones
  al tope de 30 llamadas no pasan del 5 %.
- **Los dos sistemas por fragmentos,** como en N7, declarado como límite.
- **La corrección, como la decidió la autora** (29/10/2026, recibida a las 19:16:04), tal cual: «C-1 (a): la descripción de ver_punto no
  cambia; la sección de puntos relacionados aparece solo en su salida.», «C-2: los tipos de relación de tu propuesta, remisión,
  condición y excepción, sin aplica_a.» y «C-3: hasta 10 puntos.»
- **El grafo sin corregir como cuarto brazo** (D-10, decisión de la autora, ídem), tal cual: «D-10, sí: el grafo sin corregir (N7) corre
  en B6.4 como cuarto brazo, fuera de Holm, para medir en preguntas nuevas qué aporta la corrección.» Son 288 sesiones más, con el mismo
  orden por pregunta y por repetición, ahora de cuatro brazos. Si B2 adopta N7, el brazo del grafo ya es N7: B6.4 corre con tres brazos,
  y se declara.
- **El runner,** el de B6.3 en HEAD (`data/experiment/banco_mcp/b63/v2/b2/correr_b63.py`), sin cambios en su código, con la entrada
  de B6.4 y un `config_agentes` de cuatro brazos: el del grafo adoptado, N7, el híbrido y el denso. El de B6.3 tiene tres. Si el
  runner corre los cuatro sin cambios en su código lo muestra el seco (H-4). Si no, el cambio se hace con su prueba, su seco y su
  sello, y se declara. El código de B6.3 fija tres etiquetas: la semilla del orden (`B63:orden_corridas:v1`), el prefijo del id de
  sesión (`B63-…`) y la sal del id opaco del juez (`B63:id_opaco_juez:v1`). D-4, decidida: (a), se reusan tal cual, declaradas: el
  orden y los ids salen distintos porque llevan el id de la pregunta de B6.4, y nada del runner cambia.
- **Antes de la corrida:** el seco del runner con la entrada de B6.4 (H-4) y, además (D-5, decidida: (a)), un humo pago de 1 pregunta
  por los 4 brazos, unos USD 0,35 (NO VERIFICADO), que prueba el entorno de ese día.

## 5. El juez y su control

- **El juez de EV2,** como en B6.3 (su §7.1), con el control de su entrada corrido otra vez sobre el código de B6.4 antes del paso pago.
  La lectura tolerante, con su código sellado de la etapa A de B6.3, sin cambios. Lo que la lectura no resuelve va a la adjudicación de
  la autora, como en B6.3.
- **La verificación del juez (Q8)** es la de B6.3: el mismo juez, sin ajuste. Se declara.
- **La muestra de control:** 36 respuestas, como en B6.3, de los tres brazos de las comparaciones principales (el cuarto queda fuera de la
  muestra, declarado): 12 por brazo y 4 por tipo en cada brazo, estratificadas por el veredicto del
  juez, con la semilla `B64:control_juez:v1`.
  - El piso es el de varios puntos de B6.3: Wilson inferior de al menos 0,85 por criterio.
  - Si no llega, la cifra va con el acuerdo medido al lado, y lo dudoso va a la lectura de la autora.
  - La columna «error fuera de los criterios», a ciegas al brazo.

## 6. El orden de lo pago

- Una sola corrida paga por vez: ni al lado de la ilustrativa ni de un paso pago de la v3 del juez de tripletas.
- La lanza la autora desde la Terminal, con el tope del §12.

## 7. Lo que se cuenta antes de la corrida

- **Las marcas del brazo dentro de la respuesta,** contadas por brazo y declaradas, sin editar ninguna (D-10 de B6.3).
- **Las sesiones,** enmascaradas como en B6.3 (su §5).

## 8. El análisis confirmatorio

### 8.1 Las comparaciones principales

- **La métrica por pregunta:** la proporción de sus 3 corridas juzgadas correctas. d_q es la diferencia por pregunta entre el grafo y
  cada brazo de fragmentos.
- **La prueba:** pareada, por permutación de signos sobre d_q, con Holm sobre las dos comparaciones, sobre las 96. Las cantidades son las
  de B6.3, con sus semillas propias:
  - α de 0,05 de dos colas para la familia, 0,025 la primera y 0,05 la segunda;
  - el estadístico es la media de d_q, con 100.000 permutaciones de signos y la semilla `B64:permutacion:v1`;
  - p = (1 + las permutaciones con |media| mayor o igual que la observada) / 100.001;
  - los intervalos, por bootstrap percentil por pregunta, con 10.000 remuestreos y la semilla `B64:bootstrap:v1`.
- **La afirmación principal,** la regla de B6.3: «el grafo supera a los fragmentos en preguntas que juntan varios puntos» solo si supera a
  las dos configuraciones, cada comparación con su Holm y a favor del grafo. Si supera a una sola, se informa por configuración, sin la
  afirmación general.

### 8.2 Al lado, fuera de Holm

- **Por tipo:** cada brazo y cada comparación, con su intervalo, en los tres tipos.
- **Lo operativo, por brazo y por tipo,** como en B6.3 (su §8.2).
- **El cuarto brazo, exploratorio** (D-10): la diferencia por pregunta entre el brazo del grafo adoptado y N7, con su intervalo
  bootstrap por pregunta (10.000 remuestreos, semilla `B64:bootstrap:correccion:v1`); y N7 contra cada brazo de fragmentos, con su
  intervalo, sin prueba. Se informan al lado, nunca como afirmación principal.
- **Sin total ponderado:** las 96 no representan al corpus.
- **Sin hipótesis secundaria.**

### 8.3 El chequeo de robustez por documento

Como en B6.3 (su §8.3), con las semillas `B64:permutacion:documento:v1` y `B64:bootstrap:documento:v1`.

### 8.4 El código

`analizar_b64.py`, que importa sin editar las funciones del código sellado de B6.3
(`data/experiment/banco_mcp/b63/analisis/codigo/analizar_b63.py`, `9a9d0491…`): las métricas, la permutación, Holm, la afirmación
y el bootstrap. Cambian los tipos, las semillas y las entradas. Lleva su prueba sobre datos de juguete y se sella antes de la corrida
(H-6), junto con el código de la exactitud de cita del §9.

## 9. Lo exploratorio

D-6, decidida: (b), la exactitud de cita, con el código del punto 4 de B6.3 adaptado a B6.4. Nada más: ni la atribución ni la
relevancia, declarado.
- **Por qué** (la autora, al anunciarla): la corrección incluye la línea de la cita, y B6.4 tiene que poder medir lo que aporta.
- **El código:**
  - `exactitud_de_cita_9_4_b64.py`, adaptado de `data/experiment/banco_mcp/b63/analisis/codigo/exactitud_de_cita_9_4_b63.py`
    (`5207941b…`);
  - importa sin editar las funciones de `analizar_b64.py` (§8.4) y el instrumento de citas, `scripts/ucita2_indicadores_banco.py`
    (`3a58e5be…`);
  - cambian los cuatro brazos, las anclas y las entradas de B6.4;
  - lleva su prueba sobre datos de juguete y se sella antes de la corrida (H-6). USD 0.
- **La regla de las anclas,** la de B6.3 (decisiones de la autora del 29/10/2026, 13:45:28 y 14:01:46): las anclas se leen con la lectura
  de anclas del código sellado, y una cita da en el punto de referencia si da en cualquiera de las unidades del ancla. Una pregunta cuyas
  anclas no se pueden leer sale de la medida, declarada.
- **Lo que se informa, por brazo y por tipo,** en fracción cruda «n de N», como en B6.3:
  - los indicadores del instrumento: cita fundada, cita existente y cita al ancla;
  - la columna informativa, cada ancla con su cita.
- **Lo que aporta la línea de la cita:** si B2 adopta N7c+, se lee en la cita fundada del brazo del grafo al lado de la de N7, el cuarto
  brazo, que no la tiene. Si adopta N7c o N7, ningún brazo la tiene, y se declara. Sin prueba ni intervalo: es exploratorio y no entra en
  la afirmación principal.

## 10. Lo que se declara

1. B6.4 se diseñó después de ver el resultado de B6.3. Se informa junto con él, sea cual sea su resultado, como otra familia.
   Además, el sistema del grafo de B6.4 tiene una corrección que sale de la atribución de B6.3. Se diseñó y se probó solo con preguntas de
   desarrollo (N3 y los documentos de desarrollo), y quedó fija antes de que la autora viera ninguna pregunta de B6.4. Los dos por
   fragmentos no recibieron ninguna corrección después de B6.3. B6.3 mide el sistema sin corregir.
2. Lo que la mesa leyó de B6.3 para el diseño (encabezado).
3. La definición en otro punto no es un tipo de B6.4.
   Además, sobre la corrección (§349):
   - su alcance sale de un diagnóstico de desarrollo, por código: N3 y las sesiones de N6 sobre N3;
   - su techo se midió en N3, y B2 también corre sobre N3. La familia es una regla del árbol, fijada antes de B2;
   - la línea de la cita es una ayuda que solo recibe el brazo del grafo. En N6, sin los ejemplos de la familia 6, el agente del grafo
     no copiaba la forma de citar (29 de 93 citas que no se leen); los dos por fragmentos ya citaban bien (5 de 282 y 11 de 91). La
     exactitud de cita de B6.4 (§9) se lee sabiendo eso;
   - lo que el diagnóstico no pudo arreglar sin tocar las instrucciones, declarado: en desarrollo, casi siempre el contenido que pedía
     un criterio no cumplido estaba a la vista del agente.
4. Lo que hagan las decisiones, y los lugares que cambian de unidad o de documento, con su conteo. Por D-1, las anclas que caen fuera
   de los 46, contadas por clase de documento (§3.1).
5. El juez, sin ajuste; Q8, la de B6.3.
6. La exposición de cada documento sorteado (§3.1).

## 11. El costo

Lo sacó la mesa de B6.3: USD 41,81 del agente y 29,77 del juez en 864 sesiones (`resumen_b63.json`). Con 96 preguntas, 3 brazos y 3
corridas son 864 sesiones: unos USD 71,58, NO VERIFICADO para estos tipos, que pueden pedir más llamadas. El humo de D-5 suma unos 0,25.

Con el cuarto brazo (D-10), 1.152 sesiones: unos USD 95,45, NO VERIFICADO.

## 12. El tope

USD 144, con el freno en 115, para los cuatro brazos: una vez y media y 1,2 veces el estimado del §11, con el criterio
de B6.3 de fijarlo sobre el alto. Si lo gastado hasta la firma (H-5) más este tope pasa el techo de la evaluación, decide la autora
antes de la corrida.

## 13. El orden

1. La firma de este pre-registro, con su commit.
2. El sorteo y su sello (H-1), y la carpeta de la generación.
   Además, la corrección: la etapa C2-bis, el commit 241, el humo de B2, B2 con N7, N7c y N7c+, su análisis y la configuración que
   adopta su regla (H-7, H-8), al lado de la generación, que no depende del sistema. La revisión de la autora empieza después del commit
   de la corrección.
3. La generación en dos bloques, con la revisión de la mesa, y la revisión de la autora, ola por ola; los reemplazos.
4. Lo aprobado, sellado; la entrada y el seco (H-3, H-4); el commit de las preguntas.
5. El código del análisis y el de la exactitud de cita, y su sello (H-6).
6. El humo (D-5); la corrida paga; la lectura tolerante y la adjudicación; la muestra de 36; el análisis, la exactitud de cita y su
   commit.

El calendario va aparte (`decisiones_340_mesa/calendario/`).

## 14. Las decisiones de la autora

Las que la autora anunció para la firma (30/10/2026, recibidas a las 00:12:41), tal cual: «Firmo B6.4 con D-1 (b) y D-6 (b): la
exactitud de cita, con el código del punto 4 de B6.3 adaptado, porque la corrección incluye la línea de la cita y B6.4 tiene que poder
medir lo que aporta. Las demás, como las recomendás.» Rigen con su firma.

| | decisión | lo decidido |
|---|---|---|
| D-1 | dónde pueden estar las anclas | (b): la unidad del lugar en los 46; el otro punto, en los 128 |
| D-2 | la clase de los documentos por ola | (a): 1, 2 y 1 |
| D-3 | si no están las 96 aprobadas | (a): no arranca hasta que estén |
| D-4 | las etiquetas del runner de B6.3 | (a): tal cual, declaradas |
| D-5 | el humo pago | (a): sí, además del seco |
| D-6 | lo exploratorio | (b): la exactitud de cita, con el código del punto 4 de B6.3 adaptado |
| D-7 | la generación, al lado de las ejecutoras del repo | (a): sí, como P2 de B6.3, que corrió al lado del tramo 2 de A2.1 |
| D-8 | la columna «error fuera de los criterios» de la muestra | (a): sí, como en B6.3 |
| D-9 | la ruta en el repo | la del encabezado |
| D-10 | el grafo sin corregir como cuarto brazo | sí, fuera de Holm (29/10/2026, 19:16:04) |
| C-1 a C-3 | la descripción de `ver_punto`, los tipos de relación y el tope de la corrección | (a), los tres grupos, 10 (ídem) |
| D-B2-6 a 9 | el lanzador de B2, N7c+ como tercera configuración, el tope y la regla de adopción | como los recomendó la mesa |

Las de B2, tal cual (30/10/2026, recibidas a las 00:12:41): «D-B2-6 a D-B2-9, como las recomendás: el lanzador propio (a); N7c+ como
tercera configuración de B2; tope USD 45 y freno 38; y la regla de adopción de la §349, fijada antes de B2.»

## Firma

FIRMADO por la autora el 30/10/2026 (recibida a las 00:25:13), tal cual: «Firmo el pre-registro de B6.4, el borrador v5 de la §350
(BORRADOR_preregistro_B6_4_v5_PARA_FIRMAR_mesa.md, e4c2c42b…), tal cual, con las decisiones de su §14.» Rige desde esta firma.

## Notas al pie

- **30/10/2026 — La revisión de expertos de B6.4, decidida antes de ver ninguna pregunta ni ningún resultado de B6.4** (decisiones de la
  autora recibidas a las 14:51:57 y a las 15:01:23; registro de decisiones, §197 y §198):
  - **La decisión, tal cual** (con un nombre propio omitido): «Una muestra de 20 de las 96 preguntas aprobadas de B6.4, sorteada con
    semilla y estratificada por tipo (7, 7 y 6), va a la revisión de expertos [nombre propio omitido], con el material y las
    instrucciones de la de B6.3. Se manda el sábado, después de sellar lo aprobado, con devolución pedida para el martes 3/11 al
    mediodía. Si vuelve, se informa como control de calidad de las preguntas, fuera del análisis principal, con una sensibilidad que
    excluye las que los expertos marquen como incorrectas. La revisión de expertos de B6.3 queda declarada como no realizada.»
  - **Lo que fija la autora sobre la lectura de la mesa** (15:01:23): el orden 7, 7 y 6 por los tipos del §3.2; la semilla con el
    sha256 de lo aprobado sellado; «incorrecta» solo con «no», por mayoría de los que respondieron; y las cifras en «n de 20», sin
    intervalo.
  - **La muestra:** 20 de las 96 aprobadas, 7 de agregación, 7 de remisión y 6 de condición o excepción, sorteadas con
    `random.Random(f"b64:experto:{sha256 de lo aprobado sellado}")`, en un orden sorteado con la misma semilla.
  - **El material:**
    - el de B6.3 (su pre-registro, §9.3, «El material»): la planilla, con la pregunta, su respuesta de referencia (sus criterios con
      su cita) y las columnas de B6.3, y las instrucciones de B6.3;
    - una sola planilla, igual para todos los expertos: se reenvía a cada uno, y cada uno devuelve su copia;
    - el texto que acompaña cada fila es el de todos los puntos de la pregunta, el ancla primero, desde la E0 del grafo evaluado;
    - la planilla y las instrucciones las arma un script de la mesa, con su prueba (`material_experto_B64_mesa.py`). El PDF y la
      planilla para enviar los arma la autora, como en B6.3, y también el mensaje a los expertos.
  - **Las fechas:** el envío, el sábado 31/10, después de sellar lo aprobado; la devolución, pedida para el martes 3/11 a las 12:00. Lo
    que no llegue se declara, y nada espera a la devolución.
  - **Cómo se informa:**
    - como control de calidad de las preguntas, fuera del análisis confirmatorio (§8) y de lo exploratorio (§9), y sin cambiar
      ninguna pregunta ni ninguna cifra;
    - por experto y en conjunto, en fracción cruda «n de 20»: si se puede responder desde el texto, si la respuesta es correcta (sí,
      parcial, no) y la relevancia;
    - **la sensibilidad:** las comparaciones del §8.1, repetidas sin las preguntas que los expertos marquen como incorrectas, fuera de
      Holm y como descriptiva. Una pregunta es incorrecta si tiene «no» en si la respuesta es correcta; con más de un experto, si la
      marca así la mayoría de los que la respondieron (con dos, los dos).
  - **B6.3:** su revisión de expertos queda declarada como no realizada, con una nota al pie en su pre-registro.
  - El texto firmado no cambia.
