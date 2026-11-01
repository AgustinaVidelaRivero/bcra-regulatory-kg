# La regla del sorteo de la muestra de control del juez de B6.4: 36 respuestas (mesa, §382, 01/11/2026)

## Lo que fija el pre-registro

Lo fija el pre-registro de B6.4, §5 (`docs/preregistro_B6_4_evaluacion_confirmatoria_varios_puntos.md`, firmado en `55ee1a5a`), tal
cual: «La muestra de control: 36 respuestas, como en B6.3, de los tres brazos de las comparaciones principales (el cuarto queda fuera de
la muestra, declarado): 12 por brazo y 4 por tipo en cada brazo, estratificadas por el veredicto del juez, con la semilla
`B64:control_juez:v1`.» Y además:
- «El piso es el de varios puntos de B6.3: Wilson inferior de al menos 0,85 por criterio.»
- «Si no llega, la cifra va con el acuerdo medido al lado, y lo dudoso va a la lectura de la autora.»
- «La columna «error fuera de los criterios», a ciegas al brazo.» (D-8: «(a): sí, como en B6.3».)

## Lo demás

Lo fija esta regla. Es la de B6.3 (`data/experiment/banco_mcp/b63/control_36/sorteo/regla_sorteo_control_36_B63.md`, sellada con el
script v2: `f56e3299…` y `8738ba02…`), con lo que cambia B6.4, listado punto por punto al final. Se sella, con su script
(`sortear_control_36_B64.py`) y su prueba (`probar_sorteo_control_36_B64.py`), antes de correrlo sobre los datos reales, y entra al repo
en el mismo commit que la nota del pre-registro que la anuncia.

## La población

- **Las 1.152 sesiones de B6.4:** 96 preguntas por los cuatro brazos de la corrida (`kg`, `kg_n7`, `fragmentos_hibrida` y
  `fragmentos_denso`) por k = 3 (`banco_b64/resultados/real/estado_b63.json`, con el bloque, la pregunta y la repetición de
  `orden_b63.json`).
- **Salen las 6 `incompleta_otra`,** que no fueron al juez. Quedan las 1.146 `completa`, las que el juez juzgó.
- **De las 1.146, salen:**
  - **las que no tienen sus 3 juicios leídos por la lectura estricta:**
    - cada línea de `juez/veredictos_r{1,2,3}.jsonl` y de `juez/errores_r{1,2,3}.jsonl` se lee con `json.loads`; una línea que no se
      lee, o un id repetido dentro de un mismo archivo, frena;
    - un id sale si tiene alguna línea en `errores_r{1,2,3}.jsonl`, o si le falta su registro en alguno de los tres
      `veredictos_r{1,2,3}.jsonl`;
    - las que quedan tienen que ser, sin sobrar ni faltar, las de `agregados` de `juez/agregados_b63_ciego.json`, y las que salen, las
      de sus `incompletas`; si no, frena;
  - **las `requiere_adjudicacion`,** por su `veredicto_pregunta` en `agregados_b63_ciego.json`, como en B6.3: lo que el juez deja
    dudoso va a la lectura de la autora, y la muestra mide al juez en lo que decide solo;
  - **las de `kg_n7`,** el cuarto brazo, que el §5 deja fuera de la muestra.
- **Cuántas salen por cada causa no se imprime:** va solo en la clave.

## Las entradas y su control

- **Del repo,** cada una igual a la de HEAD (si no, frena):
  - la entrada sellada (`data/experiment/banco_mcp/b64/entrada_B64.json`);
  - la configuración de agentes que sella la entrada (`config_agentes`, con su sha256);
  - el código del juez de la corrida, que se importa: `banco_mcp/b64/v1/juez_b63.py` y `banco_mcp/b64/v1/comun_b63.py`, más
    `banco_mcp/comun_banco.py`, `ev2_juez/juez.py`, `ev2_juez/mapping.py`, `ev2_juez/prompt_juez_v1.md` y `evaluacion/llm_cache.py`.
- **El manifiesto de lo que queda fuera de B6.4** (`banco_b64/manifiesto_fuera_B64.json`):
  - lo escribe `corrida_manifiesto_fuera_B64.zsh`;
  - se pasa con el sha256 que esa corrida imprime; si no da, frena.
- **De `banco_b64/`,** cada archivo con el sha256 de ese manifiesto (si no está en él o no da, frena):
  - de `resultados/real/`: `estado_b63.json`, `orden_b63.json` y cada meta que se lee de `pasada1/` o de `pasada2/` (las 165 de la
    reanudación están en `pasada2/`);
  - de `juez/`: `agregados_b63_ciego.json`, `veredictos_r{1,2,3}.jsonl`, `errores_r{1,2,3}.jsonl` y `d10_b63.json`.
- **El archivo de las 96 preguntas:** el que nombra la entrada sellada (`preguntas.ruta`), con su sha256 (`preguntas.sha256`).
- No abre ninguna carpeta `desanonimizacion_SOLO_MESA/` ni las cachés del juez.

## El brazo de cada respuesta, sin la tabla de desanonimización

- **El id opaco:** es el de B6.3, que B6.4 reusa (D-4): `B63J-` + sha256(sal|pregunta|brazo|repetición|sha256(respuesta))[:10], con la
  sal `B63:id_opaco_juez:v1`.
  - El script lo recalcula con `id_opaco` y `sha256_texto` de `b64/v1/juez_b63.py`, importados sin editarlos, para cada sesión
    `completa` de los cuatro brazos.
  - Usa la pregunta y la repetición de su bloque, su brazo y la respuesta de su meta (`final_json_R4.respuesta`, la que vio el juez).
- **Los 1.146 ids recalculados tienen que ser los 1.146 de los veredictos,** sin sobrar ni faltar ninguno: la unión de los ids de
  `veredictos_r{1,2,3}.jsonl` y de `errores_r{1,2,3}.jsonl`, que es también la de `agregados` e `incompletas`. Si no, frena.
- **La marca de D-10 de cada respuesta** se recalcula con `marcas_d10` y `contar_d10` del mismo módulo, con la configuración de agentes
  que sella la entrada.
  - La cuenta por brazo, en los cuatro, tiene que dar la de `juez/d10_b63.json`; si no, frena.
  - La marca de cada ficha va solo en la clave.

## El tipo de cada pregunta

- El campo `tipo` (`agregacion`, `remision` o `condicion_excepcion`) del archivo de las 96, por código.
- Del mismo archivo salen el `to` de cada pregunta, para la clave, y su número de criterios, que tiene que ser el `n_criterios` del juez
  para cada id (si no, frena).

## Los estratos

- **Por brazo:** 12, en `kg`, `fragmentos_hibrida` y `fragmentos_denso`.
- **Por tipo, dentro de cada brazo:** 4 de `agregacion`, 4 de `remision` y 4 de `condicion_excepcion`. La celda es (brazo, tipo): nueve
  celdas.
- **Por veredicto, dentro de cada celda,** como en B6.3: «correcto» por un lado, «parcial» e «incorrecto» juntos por el otro
  (`parcial_o_incorrecto`; `data/experiment/ev2_juez/mapping.py:25`).
  - La cuota de cada clase es proporcional a cuántas respuestas elegibles de esa clase tiene la celda, por restos mayores; el empate de
    restos lo rompe la semilla.
  - Cada clase con alguna respuesta en la celda recibe al menos 1: si los restos le dan 0, toma 1 de la otra clase.
  - Si una celda tiene menos respuestas elegibles que su cuota, frena sin escribir.
- **El estrato** es (brazo, tipo, clase): dieciocho estratos, algunos con cuota 0 si su clase no tiene respuestas.

## Las respuestas

- **Las 36 preguntas son distintas.**
- **Los estratos se llenan** del que tiene menos respuestas elegibles al que tiene más; los empates los rompe la semilla.
- **Cada lugar** toma la primera respuesta de la permutación de la semilla de su estrato (sobre sus respuestas ordenadas por id opaco)
  cuya pregunta todavía no se usó.
- **Si un estrato se queda sin respuestas** con pregunta libre, su lugar pasa a la otra clase de la misma celda, y se anota en la clave.
  Si tampoco ahí, frena sin escribir.
- El TO no es un estrato. La clave da cuántas fichas tiene cada TO.

## El orden, los nombres y la clave

- Las 36 fichas van en un orden de la semilla, con ids `C01` a `C36`. Ni el id ni el orden dicen el brazo, el tipo, la clase ni el TO.
- **La clave, por ficha:** la ficha, el id opaco, la pregunta, el TO, el tipo, el brazo, la clase, la sesión y su repetición, el sha256
  de la respuesta, si trae una marca de D-10 y cuántos criterios tiene.
- **Además:**
  - cuántas elegibles y qué cuota tiene cada estrato;
  - el orden de llenado y las pasadas a la otra clase;
  - cuántas salen por cada causa (con las de `kg_n7`) y cuántas fichas tiene cada TO;
  - el sha256 de cada entrada y la hora del sorteo.

  No trae ningún texto.
- **Dónde va la clave:** a `fuera_del_repo/banco_b64_control_36/clave_para_despues/`. La autora no la abre hasta sellar su lectura.

## La semilla

`B64:control_juez:v1`. Cada paso usa su propio generador, `random.Random("B64:control_juez:v1|<paso>")`:
- `empate|<brazo>|<tipo>`: los empates de restos de cada celda;
- `estratos`: el empate en el orden de llenado;
- `permutacion|<brazo>|<tipo>|<clase>`: la de cada estrato;
- `orden`: el de las fichas.

## Lo que imprime

- **Solo:**
  - 36 fichas y 36 preguntas distintas;
  - 12 por brazo, y 4 de cada tipo en cada brazo;
  - cuántos criterios;
  - el control de los ids: los 1.146 recalculados, los mismos que los de los veredictos.
- **Quedan solo en la clave:** las cuotas por clase, cuántas salen por cada causa y la clase de cada ficha.

## Las pruebas, antes del sello

- **Con datos de juguete** (`probar_sorteo_control_36_B64.py`): el script corre entero sobre una población inventada, con el código del
  juez de la corrida importado sin editarlo. Los casos:
  1. una celda chica;
  2. una clase sin respuestas;
  3. una pregunta que se repite entre estratos;
  4. un id que no se recalcula y que frena;
  5. el empate de restos;
  6. `kg_n7`, con sus ids recalculados y fuera de la muestra;
  7. sesiones de la pasada 2.

  Corre dos veces, y las dos salidas tienen que ser iguales byte a byte.
- **La lectura de los datos reales, sin sortear** (`probar_lectura_real_sin_sortear_B64_mesa.py`, de la mesa).
  - Corre `leer_real` sobre `banco_b64/` con un manifiesto provisorio de la mesa, sin llamar a `sortear` ni escribir una clave.
  - Imprime solo las líneas de control.
  - Es lo que la v1 de B6.3 no probó y la hizo frenar en el sorteo real.

## Lo que se declara

- **Las respuestas van tal cual las vio el juez.** Si una nombra su fuente, D-10 la cuenta y no la edita.
- **Las `requiere_adjudicacion` no están en las 36:** la muestra no mide cuántas veces el juez duda, sino si acierta cuando decide.
- **La lectura tolerante no entra en la población,** como en B6.3: la muestra sale de la lectura estricta.
- **Las fichas de las 36 se arman después del sorteo,** con la regla de lectura y el sellador de las planillas, como en B6.3. Van sin
  ningún veredicto ni el brazo de origen, en una carpeta de lectura de la autora.

## Respecto de la regla de B6.3, punto por punto

| punto | B6.3 | B6.4 (esta regla) |
|---|---|---|
| tamaño | 36: 12 por brazo | igual, en los tres brazos de las comparaciones principales |
| población | 864 sesiones, 856 juzgadas | 1.152 sesiones, 1.146 juzgadas; salen también las de `kg_n7` |
| tipos | 9 de varios puntos y 3 de dato directo por brazo | 4 de cada uno de los tres tipos de B6.4 por brazo |
| celdas y estratos | 6 celdas, 12 estratos | 9 celdas, 18 estratos |
| ids | recalculados en 3 brazos, con el juez de B6.3 | recalculados en los 4, con el juez de la corrida de B6.4 (`b64/v1`), misma sal |
| metas | solo de `pasada1/` | de `pasada1/` o `pasada2/` (la reanudación) |
| manifiesto | el commiteado de B6.3 | el de lo que queda fuera de B6.4, con su sha256 como argumento |
| D-10 | controlada en 3 brazos | controlada en los 4 |
| semilla | `B63:control_juez:v1` | `B64:control_juez:v1`, el mismo método |
| pruebas | juguete, 5 casos, dos veces | juguete, 7 casos, dos veces; y la lectura real sin sortear |
| lo demás | | igual |
