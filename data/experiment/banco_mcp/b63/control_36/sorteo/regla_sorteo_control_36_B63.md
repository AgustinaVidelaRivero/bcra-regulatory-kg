# La regla del sorteo de la muestra de control del juez de B6.3: 36 respuestas (mesa, unidad C36_a, 29/10/2026)

Lo que fija el pre-registro de B6.3 (§7.3, `docs/preregistro_B6_3_evaluacion_final.md:406-418`, HEAD `5dea3134`), tal cual:
«36 respuestas, 9 de varios puntos y 3 de dato directo por brazo»; «en varios puntos, el piso de Q12 por criterio: Wilson inferior de al
menos 0,85»; «el acuerdo por respuesta se informa sin umbral»; la columna «error fuera de los criterios (sí o no, y cuál)», «a ciegas al
brazo»; «La semilla y el estrato […]: `B63:control_juez:v1`, estratificada por brazo, por tipo y, dentro de cada celda, por el veredicto
del juez, como la muestra simétrica de EV2»; y «Cuándo la lee la autora: apenas esté la muestra.» De Q8 (§4,
`docs/mandatos/Q8_juez_de_B63_y_su_verificacion.md:64-65`): el material va «sin ningún veredicto ni el brazo de origen», en una carpeta de
lectura de la autora, y «La clave queda aparte hasta que la autora selle.»

Lo demás lo fija esta regla. Es la de la mitad de verificación de Q8 en A2.2
(`data/experiment/ev2_juez/gold_q12_verificacion/sorteo/regla_sorteo_gold_q12_verificacion_mesa.md`, sellada con `25058237…`) con los
cambios que pide B6.3, listados punto por punto al final. Se sella con su script (`sortear_control_36_B63.py`) antes de correrlo sobre
los datos reales.

## La población

- Las 864 sesiones de B6.3: 96 preguntas por tres brazos (`kg`, `fragmentos_hibrida` y `fragmentos_denso`) por k = 3
  (`banco_b63/resultados/real/estado_b63.json`, con el bloque, la pregunta y la repetición de `orden_b63.json`).
- Salen las 8 `incompleta_otra`, que no fueron al juez. Quedan las 856 `completa`, las que el juez juzgó.
- De las 856, salen:
  - **las que no tienen sus 3 juicios leídos por la lectura estricta:** cada línea de `juez/veredictos_r{1,2,3}.jsonl` y de
    `juez/errores_r{1,2,3}.jsonl` se lee con `json.loads`; una línea que no se lee, o un id repetido dentro de un mismo archivo, frena.
    Un id sale si tiene alguna línea en `errores_r{1,2,3}.jsonl` (las 25) o si le falta su registro en alguno de los tres
    `veredictos_r{1,2,3}.jsonl`. Las que quedan tienen que ser, sin sobrar ni faltar, las de `agregados` de
    `juez/agregados_b63_ciego.json`, y las que salen, las de sus `incompletas`; si no, frena;
  - **las `requiere_adjudicacion`** (el `veredicto_pregunta` de `agregados_b63_ciego.json`), como en A2.2: lo que el juez deja dudoso va
    a la lectura de la autora, así que la muestra mide al juez en lo que decide solo.
- **Cuántas salen por cada causa no se imprime:** es una cifra del juez. Va solo en la clave.

## Las entradas y su control

- **Del repo,** cada una igual a la de HEAD (si no, frena): la entrada sellada (`data/experiment/banco_mcp/b63/entrada_B63.json`); el
  manifiesto commiteado de las salidas de B6.3 fuera del repo (`data/experiment/banco_mcp/b63/real/manifiesto_fuera_resultados_y_juez_B63.json`);
  la configuración de agentes que sella la entrada (`config_agentes`, con su sha256); y el código del juez que se importa:
  `banco_mcp/b63/v2/b2/juez_b63.py`, `banco_mcp/b63/v2/b2/comun_b63.py`, `banco_mcp/comun_banco.py`, `ev2_juez/juez.py`,
  `ev2_juez/mapping.py`, `ev2_juez/prompt_juez_v1.md` y `evaluacion/llm_cache.py`.
- **De `banco_b63/`,** fuera del repo, cada archivo con el sha256 de ese manifiesto (si no está en él o no da, frena):
  `resultados/real/estado_b63.json`, `resultados/real/orden_b63.json`, cada meta que se lee de `resultados/real/pasada1/`, y de `juez/`:
  `agregados_b63_ciego.json`, `veredictos_r{1,2,3}.jsonl`, `errores_r{1,2,3}.jsonl` y `d10_b63.json`.
- **El archivo de las 96 preguntas:** el que nombra la entrada sellada (`preguntas.ruta`), con su sha256 (`preguntas.sha256`).
- No abre ninguna carpeta `desanonimizacion_SOLO_MESA/` ni las cachés del juez.

## El brazo de cada respuesta, sin la tabla de desanonimización

- El id opaco es `B63J-` + sha256(sal|pregunta|brazo|repetición|sha256(respuesta))[:10], con la sal `B63:id_opaco_juez:v1`
  (`data/experiment/banco_mcp/b63/v2/b2/juez_b63.py:50-51`). El script lo recalcula con `id_opaco` y `sha256_texto` de ese módulo
  (`:103-108`), importados sin editarlos, para cada sesión `completa`: la pregunta y la repetición de su bloque (`orden_b63.json`), su
  brazo, y la respuesta de su meta en `pasada1/` (`final_json_R4.respuesta`, la que vio el juez: `correr_b63.py`, `respuesta_de`).
- **Los 856 ids recalculados tienen que ser los 856 de los veredictos,** sin sobrar ni faltar ninguno: la unión de los ids de
  `veredictos_r{1,2,3}.jsonl` y de `errores_r{1,2,3}.jsonl`, que es también la de `agregados` e `incompletas` de
  `agregados_b63_ciego.json`. Si no, frena. (Los veredictos solos no alcanzan: una respuesta con error en sus tres repeticiones no tiene
  ningún registro en ellos.)
- **La marca de D-10 de cada respuesta** (si trae alguna marca de su brazo) se recalcula con `marcas_d10` y `contar_d10` del mismo
  módulo, importados sin editarlos, con la configuración de agentes que sella la entrada. La cuenta por brazo tiene que dar la de
  `juez/d10_b63.json`; si no, frena. La marca de cada ficha va solo en la clave.

## El tipo de cada pregunta

- El campo `tipo` (`varios_puntos` o `dato_directo`) del archivo de las 96, por código. Del mismo archivo salen el `to` de cada pregunta,
  para la clave, y su número de criterios, que tiene que ser el `n_criterios` del juez para cada id (si no, frena).

## Los estratos

- **Por brazo:** 12.
- **Por tipo, dentro de cada brazo:** 9 de `varios_puntos` y 3 de `dato_directo`. La celda es (brazo, tipo): seis celdas.
- **Por veredicto, dentro de cada celda,** como la muestra simétrica de EV2 y como en A2.2: «correcto» por un lado, «parcial» e
  «incorrecto» juntos por el otro (`parcial_o_incorrecto`). Son las clases de la regla de EV2 (`data/experiment/ev2_juez/mapping.py:25`).
  - La cuota de cada clase es proporcional a cuántas respuestas elegibles de esa clase tiene la celda, por restos mayores; el empate de
    restos lo rompe la semilla.
  - Cada clase con alguna respuesta en la celda recibe al menos 1, para medir el error en las dos direcciones: si los restos le dan 0,
    toma 1 de la otra clase.
  - Si una celda tiene menos respuestas elegibles que su cuota, frena sin escribir.
- **El estrato** es (brazo, tipo, clase): doce estratos, algunos con cuota 0 si su clase no tiene respuestas.

## Las respuestas

- **Las 36 preguntas son distintas.**
- **Los estratos se llenan** del que tiene menos respuestas elegibles al que tiene más; los empates los rompe la semilla.
- **Cada lugar** toma la primera respuesta de la permutación de la semilla de su estrato (sobre sus respuestas ordenadas por id opaco)
  cuya pregunta todavía no se usó.
- **Si un estrato se queda sin respuestas** con pregunta libre, como en A2.2: su lugar pasa a la otra clase de la misma celda (mismo
  brazo y mismo tipo), y se anota en la clave. Si tampoco ahí, frena sin escribir.
- El TO no es un estrato (el pre-registro no lo pide). La clave da cuántas fichas tiene cada TO.

## El orden y los nombres

- Las 36 fichas van en un orden de la semilla, con ids `C01` a `C36`. Ni el id ni el orden dicen el brazo, el tipo, la clase ni el TO.
- **La clave,** por ficha: la ficha, el id opaco, la pregunta, el TO, el tipo, el brazo, la clase, la sesión y su repetición, el sha256
  de la respuesta, si trae una marca de D-10 y cuántos criterios tiene. Además: cuántas elegibles y qué cuota tiene cada estrato, el orden
  de llenado, las pasadas a la otra clase, cuántas salen por cada causa, cuántas fichas tiene cada TO, el sha256 de cada entrada y la hora
  del sorteo. No trae ningún texto: la respuesta se identifica por su sesión y su sha256, y el texto va solo en las fichas.
- La clave va a `clave_para_despues/`, en el paquete de la mesa, fuera de la carpeta de la autora.

## La semilla

- `B63:control_juez:v1`. Cada paso usa su propio generador de esa semilla, `random.Random("B63:control_juez:v1|<paso>")`:
  `empate|<brazo>|<tipo>` (los empates de restos de cada celda), `estratos` (el empate en el orden de llenado), `permutacion|<brazo>|<tipo>|<clase>`
  (la de cada estrato) y `orden` (el de las fichas).

## Lo que imprime

- Solo: 36 fichas, 36 preguntas distintas, 12 por brazo, 9 y 3 por tipo en cada brazo, cuántos criterios, y el control de los ids (los
  856 recalculados, los mismos que los de los veredictos). Las cuotas por clase, cuántas salen por cada causa y la clase de cada ficha
  quedan solo en la clave.

## La prueba con datos de juguete

- Antes del sello, el script corre entero (la población con el recálculo de los ids, los estratos y las respuestas) sobre una población
  inventada, con el código del juez de B6.3 importado sin editarlo. Los casos: una celda chica; una clase sin respuestas; una pregunta que
  se repite entre estratos; un id que no se recalcula y que frena; y el empate de restos. La prueba corre dos veces, y las dos salidas
  tienen que ser iguales byte a byte.

## Lo que se declara

- Las respuestas van tal cual las vio el juez. Si una nombra su fuente («el grafo», «los nodos», «los fragmentos»), D-10 la cuenta y no
  la edita, igual que en lo que leyó el juez.
- Las `requiere_adjudicacion` no están en las 36: la muestra no mide cuántas veces el juez duda, sino si acierta cuando decide.
- El archivo de las 96 preguntas que nombra la entrada sellada está en la carpeta de trabajo de otra sesión, fuera del repo. El script
  lee solo ese archivo, por su ruta y con el sha256 sellado, y no lista ni abre nada más de esa carpeta.

## Respecto de la regla de A2.2, punto por punto

| Punto | A2.2 (mitad de verificación de Q8) | B6.3 (esta regla) | |
|---|---|---|---|
| Tamaño | 20: 7, 7 y 6 por brazo; el brazo con 6, de la semilla | 36: 12 por brazo | cambia |
| Población | las 120 de N = 1 de A2.2 | las 864 sesiones; las 856 que el juez juzgó | cambia |
| Sin sus tres juicios | salen (la sesión incompleta y la salida mal formada) | salen: las 25 con alguna línea en `errores_r{1,2,3}.jsonl`, o sin alguno de sus tres registros | cambia la fuente; igual la idea |
| Las que no fueron al juez | la sesión incompleta por R3 | las 8 `incompleta_otra` | cambia la fuente; igual la idea |
| `requiere_adjudicacion` | salen | salen | igual |
| Cuántas salen | no se imprime; va en la clave | no se imprime, por causa; va en la clave | igual |
| Brazo sin la tabla | id `A22J-`, `juez_a2_2.py` (`respuestas`, `id_opaco`), metas de `resultados/n1/` | id `B63J-`, sal `B63:id_opaco_juez:v1`, `juez_b63.py` (`id_opaco`, `sha256_texto`), metas de `pasada1/` | cambia el módulo; igual el método |
| Control de los ids | los recalculados = los del orden del juez | los 856 recalculados = los de veredictos ∪ errores = agregados ∪ incompletas | cambia el conjunto de control |
| Entradas | iguales a HEAD | las del repo iguales a HEAD; las de `banco_b63/`, con el sha256 del manifiesto commiteado; las preguntas, con el sha256 de la entrada | cambia (las salidas están fuera del repo) |
| Estrato por brazo | sí | sí | igual |
| Estrato por tipo | no | sí: 9 `varios_puntos` y 3 `dato_directo` por brazo, del campo `tipo` | nuevo |
| Estrato por veredicto | dentro de cada brazo | dentro de cada celda (brazo, tipo) | cambia la unidad; igual la regla |
| Clases | «correcto» / «parcial» e «incorrecto» juntos | lo mismo (`mapping.py:25`) | igual |
| Cuotas por clase | restos mayores; empate de la semilla; al menos 1 por clase presente | lo mismo, por celda | igual |
| Pocas respuestas | frena si un brazo tiene menos que su cuota | frena si una celda tiene menos que su cuota | cambia la unidad |
| Preguntas distintas | 20 | 36 | igual la regla |
| Orden de llenado | de la celda (brazo, clase) con menos elegibles a la de más | del estrato (brazo, tipo, clase) con menos elegibles al de más | cambia la unidad |
| Cada lugar | primera de la permutación de su celda con pregunta libre | lo mismo, en su estrato | igual |
| Sin respuestas | pasa a la otra clase del mismo brazo; si no, frena | pasa a la otra clase de la misma celda; si no, frena | cambia la unidad |
| TO | no es estrato; la clave da fichas por TO | lo mismo | igual |
| Ids y orden | `VG01` a `VG20`, orden de la semilla | `C01` a `C36`, orden de la semilla; no dicen brazo, tipo, clase ni TO | cambia el nombre |
| Clave | ficha, id opaco, pregunta, TO, brazo, clase, sesión, sha256 | lo mismo, más el tipo y la marca de D-10; sin ningún texto | se agregan dos campos |
| Semilla | `gold-q12-verificacion-a22-v1`, un generador por paso | `B63:control_juez:v1`, un generador por paso (`random.Random("B63:control_juez:v1\|<paso>")`) | cambia la semilla; igual el método |
| Lo que imprime | 20, 20 distintas, 7-7-6, criterios | 36, 36 distintas, 12 por brazo, 9 y 3 por tipo, criterios y el control de los 856 ids | cambia |
| Prueba previa | entradas sintéticas con la forma de las reales | población inventada, con cinco casos nombrados, dos veces iguales byte a byte | se amplía |
| D-10 | declarada; las respuestas tal cual | lo mismo, y la marca de cada ficha en la clave, recalculada y controlada contra `d10_b63.json` | se amplía |
