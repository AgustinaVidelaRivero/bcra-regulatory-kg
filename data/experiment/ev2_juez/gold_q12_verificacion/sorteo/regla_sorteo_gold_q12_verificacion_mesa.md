# La regla del sorteo de la mitad de verificación del gold de Q12: las 20 de A2.2 (mesa, §276, 25/10/2026)

Lo que fija el pre-registro firmado de A2.2 (§4, `:191-194`) y Q8 (§4, `:61-65`), tal cual: «20 de las 120 respuestas de A2.2 (7, 7
y 6 por brazo), estratificadas también por el veredicto del juez, como la muestra simétrica de EV2. Su semilla,
`gold-q12-verificacion-a22-v1`», y el material «sin ningún veredicto ni el brazo de origen. Lo arma la mesa después de A2.2, y lo
deja en una carpeta de lectura de la autora. La clave queda aparte hasta que la autora selle.» Lo demás lo fija esta regla, que se
sella con su script antes de correrlo sobre los datos reales, como la de la mitad de ajuste (§128).

## La población

- Las 120 respuestas de N = 1 de A2.2: 40 preguntas de EV2 por tres brazos (el grafo, fragmentos con BM25 y fragmentos densos).
- Salen las que no tienen juicio del juez con sus tres repeticiones: la sesión incompleta por R3 y la respuesta con la salida mal
  formada (registro, §117). Quedan 118 (`juez/n1/agregados_n1_ciego.json`).
- Salen también las `requiere_adjudicacion`, como en la muestra simétrica de EV2, que es «del resto» (método de EV2, §6, `:80-84`):
  esas van todas a la adjudicación de la autora (A-D8). En B6.3, lo que el juez deja dudoso va a la autora (registro, §9), así que la
  verificación mide al juez en lo que decide solo. Cuántas salen no se imprime: es una cifra del juez.

## El brazo de cada respuesta, sin la tabla de desanonimización

- El id opaco es `A22J-` + sha256(sal|pregunta|brazo|repetición|sha256(respuesta))[:10] (`a2_2/juez_a2_2.py:113-114`). El script lo
  recalcula con las funciones congeladas del juez de A2.2 (`respuestas` y `id_opaco`, sobre las metas de `resultados/n1/`), y controla
  que los ids recalculados sean los 119 del orden del juez. No abre ninguna carpeta `desanonimizacion_SOLO_MESA/`.

## Los estratos

- **Por brazo:** 7, 7 y 6. El brazo que recibe 6 sale de la semilla.
- **Por veredicto, dentro de cada brazo,** como la muestra simétrica de EV2 (`:82-84`): «correcto» por un lado, «parcial» e
  «incorrecto» juntos por el otro.
  - La cuota de cada clase es proporcional a cuántas respuestas de esa clase tiene el brazo, por restos mayores; el empate de restos lo
    rompe la semilla.
  - Cada clase con alguna respuesta en el brazo recibe al menos 1, para medir el error en las dos direcciones (`:85-86`): si los restos
    le dan 0, toma 1 de la otra clase.

## Las respuestas

- **Una pregunta entra una sola vez:** 20 preguntas distintas, como en la mitad de ajuste.
- **Las celdas** (brazo, clase) se llenan de la que tiene menos respuestas elegibles a la que tiene más, y los empates los rompe la
  semilla. Cada lugar toma la primera respuesta de una permutación de la semilla de esa celda cuya pregunta todavía no se usó.
- **Si una celda se queda sin respuestas** con pregunta libre, su lugar pasa a la otra clase del mismo brazo, y se anota en la clave. Si
  tampoco ahí, el script frena sin escribir.
- El TO no es un estrato (el pre-registro no lo pide). La clave da cuántas fichas tiene cada TO.

## El orden y los nombres

- Las 20 fichas van en un orden de la semilla, con ids VG01 a VG20. Ni el id ni el orden dicen el brazo, la clase ni el TO.
- La clave (ficha → id opaco, pregunta, TO, brazo, clase, sesión, sha256 de la respuesta) va a `clave_para_despues/`, en el paquete de
  la mesa, aparte de lo que la autora lee.

## La semilla

- `gold-q12-verificacion-a22-v1`. Cada paso usa su propio generador de esa semilla (`random.Random("<semilla>|<paso>")`): el brazo con 6,
  los empates de cada brazo, el orden de las celdas, la permutación de cada celda y el orden de las fichas.

## Lo que imprime

- Solo cuentas que no dicen nada del juez: 20 fichas, 20 preguntas distintas, 7, 7 y 6 por brazo y cuántos criterios. Las cuotas por
  clase, cuántas respuestas salieron por `requiere_adjudicacion` y la clase de cada ficha quedan solo en la clave.

## La prueba en seco

- El script corre antes del sello sobre entradas sintéticas con la misma forma: 40 preguntas, 120 respuestas, 2 sin juicio y algunas
  `requiere_adjudicacion`. Tiene que dar 20 fichas con 20 preguntas distintas, 7, 7 y 6 por brazo, y al menos una de cada clase por brazo.

## Lo que se declara

- Las respuestas van tal cual las vio el juez. Si una nombra su fuente («el grafo», «los fragmentos»), el conteo de marcas del brazo
  (D-10) lo registra y no la edita, igual que en lo que leyó el juez.
- Las `requiere_adjudicacion` no están en las 20: la verificación no mide cuántas veces el juez duda, sino si acierta cuando decide.
