# Enmienda 1 a la regla de atribución: las herramientas de navegación del brazo del grafo de B6.3

Estado: **FIRMADA por la autora el 29/10/2026.** Lo preparé en la unidad ATRIB_NAV (vuelta b; la v1 es
la de la vuelta a). No edita `regla_atribucion.md`, que sigue sellado tal cual (sha256
`20040e94c383286cf1790f88684380d978a8613265c2148eb19da07700551aa1`,
`git show HEAD:data/experiment/ev2_reporte/regla_atribucion.md | shasum -a 256`; último commit que lo toca: `40603a99`,
`git log -n 1 --format=%h -- data/experiment/ev2_reporte/regla_atribucion.md`): lo enmienda. Rige desde el commit de
su firma. Hasta entonces, `code/atribucion_fallas_nav.py` no corre sobre B6.3.

Decisiones que implementa:
- la opción (a) (decisión de la autora del 27/10/2026, recibida a las 11:15:38; registro de decisiones, §134);
- el tratamiento del pedido a un nombre que no es una herramienta (decisión de la autora del 29/10/2026, recibida a
  las 10:19:04);
- el cierre de los dos puntos abiertos de la v1 y las interpretaciones del §6 (decisiones de la autora del 29/10/2026,
  recibidas a las 11:51:20): la presencia del ancla sobre el grafo evaluado de B6.3, con la misma regla y un lector de
  sus procedencias `{to, punto}` (§2); las v1 del banco, leídas del log R1 (§3); las interpretaciones a a h, tal cual.

---

## 1. Qué cambia

La regla de HEAD define «vista» y «consultada» para las tres herramientas de la firma v1 (§3). El brazo del grafo de
B6.3 tiene diez: las `tools_esperadas` del brazo `kg` de `data/experiment/banco_mcp/b63/v2/b2/config_agentes_b63.json`
(sha256 `eaff32bb…`), que son las tres v1 y las siete de navegación (`familias_nav.py` y `familias_nav_cand.py`). Para
las siete, la enmienda agrega:

- **Vista:** el punto del ancla, o un nodo que la porta, aparece en cualquier salida fuera de su cabecera: las filas de
  `buscar_puntos`, la lista de nodos de `ver_punto`, las filas de vecinos y de remisiones.
- **Consultada:** además de `ver_nodo` y `ver_vecinos`, `ver_punto` del punto del ancla cuando muestra su texto, y
  `ver_descendientes` cuando muestra el texto del punto del ancla.

| herramienta | familia | salida | vista | consultada |
|---|---|---|---|---|
| `buscar_nodos` | v1 | JSON (en el banco, del log R1) | §3, sin cambio (`resultados[*].id`) | no |
| `ver_nodo` | v1 | JSON (en el banco, del log R1) | no | §3, sin cambio (`id` sin error) |
| `ver_vecinos` | v1 | JSON (en el banco, del log R1) | no | §3, sin cambio (`vecino_id`) |
| `buscar_puntos` | 1 | texto | la clave de punto de cada fila y los ids de su columna de nodos | no |
| `ver_punto` | 2 | texto | la lista de nodos (ids) y, si muestra su texto, el punto pedido | el punto pedido, si muestra su texto |
| `ver_descendientes` | 2 | texto | la clave de cada descendiente | el descendiente que trae su texto |
| `ver_remisiones` | 3 | texto | la clave de punto de cada fila | no |
| `indice_to` | 4 | texto | solo lo que el lector lee (ver §6, c) | no |
| `tipos_de_relacion` | 5 | texto | la clave del punto del nodo (segunda línea) | no |
| `vecinos_por_relacion` | 5 | texto | el id y la clave de punto de cada fila de vecino | no |

## 2. Lo que no cambia, y la presencia del ancla en el grafo del banco

- La unidad (la traza), el veredicto contra el que se atribuye y los `correcto` fuera de la atribución (§1).
- El criterio de presencia y la definición de `ancla_presente` (§2): `ancla_index.resolver(to, punto)`, punto exacto,
  contenedores excluidos. El ancla puede venir como `to:punto` o como `to::punto`. En los grafos de EV2 el índice sigue
  siendo `resolucion.AnclaIndex`, sin cambios.
- «Vista» y «consultada» de las tres v1, con sus bordes heredados (§3): la misma regla, `metrica.evaluar_traza` (por
  `atribucion_fallas.navegacion_de_traza`) sobre los steps v1 de la traza. En las trazas del harness (EV2), con la
  re-ejecución y los dos replays de HEAD; en las del banco, con la salida del log R1 (el §3 de esta enmienda).
- Las cuatro clases, su precedencia y su tabla de verdad (§4): `atribucion_fallas.clasificar`, importado.
- Sobre una traza del harness que usa solo las tres v1, la salida de `atribucion_fallas_nav.atribuir_payload` es, byte a
  byte, la de `atribucion_fallas.atribuir_payload` (§8).

**La presencia del ancla en el grafo del banco** (`AnclaIndexBanco`, en `code/atribucion_fallas_nav.py`, con la interfaz
de `resolucion.AnclaIndex`: `resolver(to, ancla)` y `censo`, así `atribuir_payload` lo recibe sin cambiar). Cambia el
lector, no el criterio:

- **el grafo:** el `kg.json` del `kg_path` del manifiesto del índice por punto del grafo evaluado, con su sha256 contra el
  `kg_sha256` del manifiesto antes de leerlo (en B6.3, `576c9725…`);
- **las procedencias** de cada nodo: `provenances` o, si no está, `provenance`, como `indice_puntos.cargar_nodos`
  (`banco_mcp/mcp_kg/indice_puntos.py:171-175`);
- **la clave** de cada procedencia con `to` y `punto`: `indice_puntos.base_punto(f"{to}::{punto.strip()}")`. La del
  ancla, por el mismo `base_punto` (y el mismo `strip`);
- **presente:** algún nodo que no es contenedor porta la clave exacta del ancla;
- **los contenedores:** los nodos que portan más de 10 claves distintas (el umbral de `resolucion.py`) y los de tipo
  `TextoOrdenado` (`indice_puntos.TIPOS_FUERA_DE_PUNTO`, importado), por la interpretación i del §6.

En el grafo de B6.3, contra el índice por punto que sirvió el banco (`puntos.json`), en sus 11.814 claves que no son de
tipo `to` (`pruebas_atribucion_nav.py --presencia-b63`): el lector da los nodos del índice menos los contenedores del
§2 en las 11.814, en el mismo orden. El índice no excluye los nodos de más de 10 claves que no son `TextoOrdenado`: 84
(81 `Sujeto` y 3 `Comunicacion`), que aparecen en 5.484 claves. Con el índice tal cual, los nodos coinciden en 6.330
claves y la presencia (sí o no) en 11.812: las 2 restantes solo tienen nodos de esos 84, y con la regla del §2 su
ancla no está presente. El grafo tiene 212 contenedores: 196 de más de 10 claves y 16 `TextoOrdenado` de 10 o menos. El
lector encuentra 1 clave que el índice no tiene (procedencias fuera de la estructura E0), y 145 procedencias sin `to` o
sin `punto`, que no lee.

## 3. Cómo se lee cada salida: las de navegación y las v1 del banco

**Las v1 del banco, del log R1** (`atribuir_payload(..., log_r1=<log R1 de la sesión>)`, con `index` en None):

- la salida de cada step v1 es el `output_str` de su llamada reconciliada por R7 (el `n_log` que el adaptador del banco
  aceptó para ese step), leído como JSON;
- se controla con el `output_sha256` del log, con la salida de la sesión (igual a la del log, o más corta: un truncado
  del transporte, como en HEAD), con la herramienta y la entrada del step, y con que se lea como JSON
  (`controlar_v1_del_log`);
- la regla v1 de HEAD se aplica sin cambios: `metrica.evaluar_traza`, importada sin editarla, recibe un índice doble
  (`IndiceDelLog`) que devuelve, para la entrada de cada step v1, la salida del log ya controlada, y corre con
  `verificar_replay=False`. El control del log reemplaza a la re-ejecución: `replay_ok` sale de él, y sus fallas van a
  `replay_fallas`. `replay_fuerte_ok` compara, como en HEAD, `steps_full` con lo que da el índice;
- un step v1 cuyo control falla (el sha256, R7, la salida de la sesión, una salida que no se lee como JSON, o dos
  salidas distintas para la misma entrada) invalida la corrida entera (`corrida_valida`), como una re-ejecución que
  diverge (`regla_atribucion.md:138-140`);
- las trazas del harness (EV2) siguen con la re-ejecución de HEAD.

**Las de navegación:**

- **La fuente:** el texto que el servidor registró en el log R1 de la sesión (`output_str`), que el adaptador del banco
  (`banco_mcp/adaptador/adaptador_banco_nav.py`) guarda en `steps_full`. No se re-ejecuta (necesitaría Neo4j y el
  codificador de consultas): se controla que coincida con `output_truncado` y `output_chars` del mismo step
  (`metrica._check_replay`, sobre el texto; `navegacion_b63.consistencia_steps_full_ok`).
- **La cabecera** es la primera línea entera de la salida y repite lo que pidió el agente (el punto, el id, el TO o
  los filtros). Lo que aparece solo en la cabecera no cuenta.
- **Claves de punto:** las `to::unidad` del cuerpo, con el lector de `scripts/ucita2_indicadores_banco.py`
  (`leer_vista_nav`, sin editar), llevadas a su punto con `indice_puntos.base_punto`. Ese lector suma, además, el punto
  pedido de `ver_punto` cuando muestra su texto y, en `ver_descendientes`, la clave de cada descendiente (el TO de la
  cabecera y la unidad del bloque).
- **Ids de nodo:** cada palabra del cuerpo, partido por blancos, «|», «;» y «·», que es el id de un nodo del grafo
  (`nodos.json` del índice por punto). Es el lector nuevo, con el mismo criterio de cabecera, y corre sobre todas las
  salidas de navegación, también `indice_to`, `tipos_de_relacion` y `vecinos_por_relacion`.
- **Del punto a sus nodos:** cada clave leída lleva a los nodos de ese punto en el índice por punto (`puntos.json`,
  `nodos`). El ancla está vista si su punto es una de las claves leídas, si un nodo que la porta es uno de los ids
  leídos, o si es uno de los nodos de una de las claves leídas.
- **Texto mostrado:** en `ver_punto`, la tercera línea del cuerpo es `Texto (n caracteres):` (el criterio de
  `ucita2_indicadores_banco`); en `ver_descendientes`, la línea que sigue al bloque `#k · unidad · …` es
  `Texto (n caracteres):` o `Texto (n caracteres, cortado en m):`. Con `Texto: — (…sin texto propio…)` no hay texto.
- **Las salidas de error** de una herramienta (las que empiezan con `<herramienta>:` o con `herramienta desconocida:`)
  no muestran nada.

## 4. El pedido a un nombre que no es una herramienta

Un pedido del agente a un nombre que no es ninguna de las diez herramientas del servidor (en B6.3, `mcp__kg`, sin el
sufijo de ninguna) no llegó al servidor: el cliente lo rechazó y no hay una línea suya en el log R1. No es una consulta
ni una vista, y se cuenta aparte:

- en el adaptador, no es un step ni entra a la reconciliación R7 (con el adaptador de HEAD corría en uno el orden de
  todas las llamadas que le siguen); va a `banco.pedidos_sin_herramienta`, con su orden en la sesión. Su tool_result
  tiene que ser un error del cliente; si no lo es, el payload no es atribuible (R3);
- en la atribución, el bloque `navegacion_b63.pedidos_sin_herramienta` cuenta los del adaptador y cualquier step de la
  traza cuya herramienta no sea una de las diez.

## 5. Fuente de verdad y controles

- R7, con el log R1 como fuente de verdad: la k-ésima llamada a una de las diez en la sesión se reconcilia con la
  k-ésima `llamada` del log: la misma herramienta, la misma entrada, `n` del log igual a k, `output_sha256` del log
  igual al sha256 de su `output_str` y, si la sesión trae el texto entero, el mismo texto. Un texto de la sesión más
  corto que el del log es un truncado del transporte (como en HEAD: se registra y la salida sale del log).
- En las trazas del harness, `replay_ok` y `replay_fuerte_ok` cubren los steps v1, como hoy. En las del banco,
  `replay_ok` es el control del log de los steps v1 (§3) y `replay_fuerte_ok` compara su `steps_full` con la salida del
  log; los steps de navegación, con la consistencia del §3.
- El control del log de las v1 del banco: para cada step v1, una llamada aceptada en el mapa R7 del adaptador, con la
  misma herramienta y entrada, `output_sha256` igual al sha256 de su `output_str`, la salida de la sesión igual o
  truncada, y un `output_str` que se lee como JSON. Una falla invalida la corrida entera (§6, k).
- La presencia en el grafo del banco: el `kg.json` se lee solo si da el `kg_sha256` del manifiesto de su índice por punto.

## 6. Interpretaciones que fija la firma

Las a a h, tal cual, las aceptó la autora el 29/10/2026 (recibido a las 11:51:20). Las i, j y k son de esta v2.


a. **Texto cortado de `ver_descendientes`:** un descendiente que no entra solo en el tope va con su texto cortado
   (`Texto (n caracteres, cortado en m):`). Lo cuento como texto mostrado: el agente tuvo el texto del punto, cortado.
   La otra lectura (solo el texto entero) haría `vista_no_consultada` esos casos.
b. **Segunda línea de `tipos_de_relacion`:** trae `punto <to::unidad>` del nodo pedido. No es la cabecera, así que
   cuenta: `tipos_de_relacion` del nodo del ancla la hace vista (no consultada). El id del nodo, que está solo en la
   cabecera, no cuenta.
c. **`indice_to`** lista las unidades del TO sin el TO (`6.11 Título [n nodos]`), y la de `desde`, en la cabecera.
   El lector de claves de `ucita2_indicadores_banco` no las lee como claves, y no traen ids: con la regla tal cual,
   `indice_to` no hace vista a ningún punto.
d. **Ancestros e hijos de `ver_punto`** van como unidad y título, sin el TO: no cuentan. Su lista de nodos, sí.
e. **`vecinos_por_relacion`** hace vista, no consultada: la opción (a) suma como consultadas solo `ver_punto` y
   `ver_descendientes`. Es distinto de `ver_vecinos` de la v1, donde el `vecino_id` cuenta como consultado (§3, borde
   heredado).
f. **Un nodo del ancla que es nodo de otra clave leída** (un nodo con procedencias en dos puntos) hace vista el ancla,
   por la regla de «un nodo que la porta».
g. **Comparación de claves:** exacta, después de `base_punto` (`ext::6.11::intro` es `ext::6.11`). No normalizo
   `Sn` a `n`, como hace la cita en `ucita2_indicadores_banco`: así la sección 1 y el punto 1 de un TO no se confunden
   (el borde de la DV-01).
h. **Steps:** `vista_en_step` y `consultada_en_step` son el menor `n` entre la v1 y la navegación; `consultada_via`
   suma `ver_punto` o `ver_descendientes` a las vías v1. La consulta por texto es del ancla como punto: el
   `consultado` de cada nodo sigue siendo el de la v1.
i. **Los `TextoOrdenado` son contenedores**, además de los nodos de más de 10 claves. El criterio de contenedor del §2
   existe para que cruzar un nodo que porta todo un TO no haga vista ninguna de sus anclas
   (`exploracion/sinteticas/resolucion.py:20-26`). En los grafos de EV2 lo cumplía el umbral, porque sus `TextoOrdenado`
   portaban de 18 a 125 anclas; en el grafo de B6.3, 16 `TextoOrdenado` portan 10 claves o menos. Por eso son
   contenedores por su tipo, como en el índice por punto del banco (`banco_mcp/mcp_kg/indice_puntos.py:55` y
   `:245-248`).
j. **Las v1 del banco se leen del log R1**, no se re-ejecutan. El log guarda la salida entera que recibió el agente; la
   re-ejecución de HEAD existe porque las trazas del harness la cortan a 1.200 caracteres
   (`exploracion/sinteticas/metrica.py:16-22`). Y el servidor del banco no sirvió las v1 con `harness.GraphIndex`, sino
   con Neo4j en modo `fulltext`: en la única llamada v1 del humo, la re-ejecución con `harness.GraphIndex` no da sus
   mismos ids (`replay_v1_humo.py`, en el paquete de la vuelta a).
k. **Un control del log que falla invalida la corrida entera**, como una re-ejecución que diverge en el §3 de la regla
   (`regla_atribucion.md:138-140`).

## 7. Lo que queda abierto

**Nada queda abierto.** Los dos puntos de la v1 se cerraron con la decisión 2 de la autora del 29/10/2026 (recibida a
las 11:51:20):

1. **La presencia del ancla en el grafo de B6.3.** En la v1, `resolucion.AnclaIndex` no encontraba ninguna ancla en el
   crudo del grafo de B6.3 (procedencias `{to, punto, …}`, 128 TOs; `AnclaIndex` lee `{source_doc, location}` de los 5
   TOs de `sinteticas.comun.DOC2TO`). La decisión, tal cual: «la presencia del ancla se calcula sobre el grafo evaluado
   de B6.3, con la misma regla (punto exacto, contenedores de más de 10 anclas excluidos), con un lector de sus
   procedencias {to, punto}. Cambia el lector, no el criterio». Se cierra con `AnclaIndexBanco` (§2), y los
   `TextoOrdenado` como contenedores (§6, i).
2. **La re-ejecución de las v1 en B6.3.** En la v1, `harness.GraphIndex` no reproducía la salida del servidor del banco.
   La decisión, tal cual: «las v1 del banco se leen del log R1, como las de navegación: el output_str del servidor,
   controlado con su sha256 y con la salida de la sesión. No se re-ejecutan con harness.GraphIndex, porque el servidor
   del banco no las sirvió con él». Se cierra con el §3 (las v1 del banco, del log R1) y el §6, j y k.

## 8. Las pruebas que la respaldan

`python3 -I -B data/experiment/ev2_reporte/code/pruebas_atribucion_nav.py <banderas> --out <carpeta>` (Python 3.12,
sin API, sin Neo4j y sin el codificador). En la vuelta b corrieron todas juntas dos veces, con las salidas iguales byte
a byte (salvo el `generado` que escribe el selftest de HEAD):

- `--regresion-selftest`: el selftest de `atribucion_fallas.py`, con cada `atribuir_payload` de HEAD comparado con el
  nuevo (17 de 17 iguales) y con el nuevo en su lugar (24 de 24);
- `--regresion-ev2`: las 318 trazas de EV2 que atribuye `atribucion_fallas.py`, con anclas derivadas de cada traza:
  64.970 de 64.970 comparaciones iguales byte a byte (sha256 de las salidas `1ea32361…`);
- `--equivalencia-ev2`: las mismas 318 trazas, con un log armado con la re-ejecución de HEAD (el `output_str` es el
  `json.dumps` de `metrica._reejecutar_step`, con su sha256): la atribución que lee las v1 de ese log da lo mismo que
  HEAD, 64.970 de 64.970, con la misma huella `1ea32361…`;
- `--sinteticos`: 76 de 76: un caso por herramienta, con la cabecera, los del pedido a `mcp__kg`, los de la presencia
  con un grafo de juguete (punto exacto, `base_punto`, `strip`, contenedor de más de 10, `TextoOrdenado` de 10 o menos,
  las dos formas del ancla, ancla ausente) y los de las v1 del log (vista, consultada, error, mezcla, y los tres
  controles que invalidan la corrida);
- `--presencia-b63`: el §2 de esta enmienda, sobre el grafo de B6.3;
- `--v1-b63`: las 1.250 salidas v1 de los 288 logs R1 del brazo `kg` de B6.3 se leen como JSON, traen los campos de la
  regla v1 y dan su `output_sha256`;
- `--humo` (6 de 6, con `AnclaIndexBanco` y las v1 del log), `--nombres-b63` y `--lector-claves-b63`.

## Firma

FIRMADA por la autora el 29/10/2026, con el commit que agrega esta enmienda al repo. Rige desde esta firma.

Antes de firmar, y antes de ver cualquier cifra de B6.3, la autora confirmó la regla de contenedores del §2 (decisión
del 29/10/2026, recibida a las 13:45:28), tal cual: «La regla de contenedores queda como la escribió la vuelta b: los
nodos que portan más de 10 claves y los de tipo TextoOrdenado. Que el índice por punto del banco conserve los 84 nodos
genéricos no cambia la regla: verlos no dice que el agente vio un punto concreto.»
