# El gold de Q12, mitad de ajuste: acta de la lectura y del cruce con el juez de EV2 (mesa, §145, 17/10/2026)

## El diseño y el sorteo

- **El diseño:** el gold en dos mitades (registro de decisiones, §9, `:294-303`).
  - Las 20 de ajuste salen de las respuestas base de EV2.
  - Las 20 de verificación saldrán de la muestra simétrica de A2.2.
- **El sorteo** (`sorteo/`):
  - la regla (`ba9a1489…`) y el script (`5f16ad34…`) quedaron sellados el 16/10/2026 a las 13:37:02, y el sorteo corrió una sola vez, a
    las 13:37:12;
  - la semilla es `gold-q12-ajuste-ev2-v1`, sobre 108 respuestas base (120 menos las 12 de la muestra simétrica de EV2), con 20 preguntas
    distintas;
  - dio 20 respuestas y 82 criterios;
  - la clave (`clave/`) se abrió después de la lectura.
- **Lo que leyó la autora** (`para_leer/`, manifiesto en `manifest_gold_q12_ajuste_mesa.txt`):
  - la regla de lectura y cómo se mide el juez;
  - las 20 respuestas con sus criterios, sin ningún veredicto ni el sistema de origen.
  - Los cinco PDF fuente no entran al repo: están en `data/experiment/subset/`, que el `.gitignore` deja fuera.
- **Cómo se mide el juez,** con las dos propuestas que la autora confirmó el 16/10 a las 14:04:04 y otra vez el 17/10 (registro, §27):
  - el «dudoso» del juez cuenta como desacuerdo, con la cifra sin esos pares al lado;
  - la cifra principal va sobre los 82 pares, con la cifra sin «necesita experto» ni «criterio mal planteado» al lado.
  - La cifra sin las respuestas que llegaron a su adjudicación en EV2 está fijada en `asiento_medicion_gold_q12_mesa.md`.

## La lectura

- La leyó la autora el 17/10/2026, a ciegas. Le llevó unas 1 h 25 min, según su cuenta.
- **Sus planillas están en `lectura/`,** selladas el 17/10/2026 a las 17:14:03 (`sello_gold_q12_ajuste.txt`):
  - `planilla_criterios_gold_q12_ajuste.csv`, `e4787250…`;
  - `planilla_respuestas_gold_q12_ajuste.csv`, `5875f24f…`;
  - sus exportaciones de Numbers, con punto y coma, `ad8d9ac0…` y `48f92a8b…`.
- El paso a comas fue mecánico, según la autora. El control lo confirma.

## El control de la mesa

Lo hace `data/experiment/segmentacion_oficial_e0r2/control_lecturas_1710/controlar_lecturas_1710_mesa.py`. Da 0 fallas:
- los sha256 son los del sello;
- las cabeceras son las de la plantilla, con 82 y 20 filas;
- las columnas `ficha` y `criterio` son iguales fila por fila;
- las exportaciones tienen el mismo contenido.

Cuatro observaciones de formato, leídas sin tocar las planillas:
- en G11-1, «criterio mal planteado» trae « no», con un espacio de más: lo leo como «no»;
- la clasificación trae «abstención» con tilde, 3 veces, y el código de la plantilla es «abstencion»: lo leo igual;
- «sí» va escrito «si»: lo leo igual;
- la columna «minutos» está vacía en las 20.

## Lo que marcó la autora

- **Por criterio:** 35 cumplidos y 47 no cumplidos.
- **Sus marcas:** «dudosa para mí» en 4 (G07-3, G13-2, G14-2 y G15-3); «necesita experto», ninguna; «criterio mal planteado», 1 (G10-4).
- **Por respuesta,** con la regla de EV2 (`ev2_juez/mapping.py:40-54`): 2 correctas, 12 parciales y 6 incorrectas.
- **Clasificación:** 17 de contenido y 3 de abstención.
- **Errores fuera de los criterios:** 12 de 20.

## El cruce

Lo hace `cruce/cruce_gold_q12_ajuste_mesa.py`, con los veredictos del juez de EV2, que ya existían y no se pagan
(`claude-sonnet-4-6`, prompt v1). Sus salidas están en `cruce/`.

| Cifra | Valor |
|---|---|
| Acuerdo por criterio, los 82 pares | 79 de 82 (0,9634; Wilson al 95 %, 0,8979 a 0,9875) |
| Dirección A (el juez acredita lo que la autora no) | 0 |
| Dirección B (el juez no acredita lo que la autora sí) | 2 (G13-3 y G14-3) |
| «Dudoso» del juez, contado como desacuerdo | 1 (G02-3) |
| Sin los dudosos del juez | 79 de 81 (0,9753; 0,9144 a 0,9932) |
| Sin «necesita experto» ni «criterio mal planteado» | 78 de 81 (0,963; 0,8967 a 0,9873) |
| Acuerdo por respuesta, las 20 | 18 de 20 (0,9; 0,699 a 0,9721) |
| Dirección A, por respuesta | 0 |
| Dirección B, por respuesta | 1 (G14) |
| «requiere_adjudicacion» del juez, contado como desacuerdo | 1 (G02) |
| Abstención o contenido | 20 de 20 |

**La cifra que pidió la autora** (asiento de la §129):
- **por vía:** 1 de las 20 llegó a su adjudicación en EV2 por la vía `adjudicacion_base` (G02). Otras 2 van aparte, por
  `adjudicacion_s7` (G07 y G13);
- **sin G02:** por criterio, 76 de 78 (0,9744; 0,9112 a 0,9929); por respuesta, 18 de 19 (0,9474; 0,7536 a 0,9906).

**Lo que esta mitad no decide:**
- no tiene umbral: sirve para ajustar el juez;
- el criterio de aceptación (Wilson inferior de al menos 0,85 por criterio y 18 de 20 por respuesta) rige en la mitad de verificación,
  la de A2.2 (registro, `:298-299`).
- **Solo como referencia:** aquí el Wilson inferior por criterio es 0,8979 y el acuerdo por respuesta, 18 de 20.
- **Si el juez se ajusta o queda como está** lo decide la autora antes de firmar el pre-registro de A2.2.
