# L2 — Regla que separa las unidades por punto de las que cruzan fichas

Escrita el 04/10/2026, ANTES de aplicarla a ninguna salida (U-NOSEG-LIMITE, L2). La aplica
`code/l2_parciales.py`; si el resultado no reproduce el 42 / 4 del mandato, se corrige la cifra y no
la regla.

## Objetos

- TOs: los dos parciales declarados, `manual` y `ri2_pm` (`particion_152.json`, clase
  `parcial_declarado`).
- Unidades: cada chunk de `chunks_<to>.json` (terminales y mini-chunks), primero los de la partición
  (`data/experiment/segmentacion_84/b584_particion/<to>/`) y después los de la corrida de e0-r2 en el
  scratchpad.
- Roles por página: los del camino que usó B5.8.4 para estos TOs (modo `sin_raiz`):
  `clasificar_paginas(paginas, marcadores_b582=True)` y luego `roles_para_modo_sin_raiz`, con
  `e0_lib` de HEAD corrido en el espejo del scratchpad. Control previo obligatorio: los conteos por
  rol tienen que dar los de `conteos_b584.json` (`manual` 1.830 de ficha y 207 de cuerpo; `ri2_pm`
  345 y 31). Si no dan, la regla no se aplica y se reporta.

## Regla

Para una unidad u, sea P(u) su lista `paginas` y [a, b] = [mín P(u), máx P(u)]. Sea F el conjunto de
páginas del TO con rol `ficha_registro`.

1. u es **por punto** si ninguna página de F cae en [a, b]: su texto propio está en un tramo
   continuo de páginas de cuerpo, sin fichas en medio.
2. u **cruza fichas** si al menos una página de F cae en [a, b]: su texto propio junta páginas de
   cuerpo separadas por fichas.

## Medidas que se reportan, sin cambiar la clase

- Páginas: la unión de P(u) por grupo (las páginas listadas, que son de cuerpo; las de ficha no
  figuran en P(u)) y, aparte, las páginas de ficha que quedan dentro de [a, b].
- Caracteres: `chars_propio` sumado por grupo; `chars_completo` aparte.
- Herencia: si la herencia de una unidad por punto trae texto cuyo origen es una unidad que cruza
  fichas (por ejemplo un `cierre` o una `intro` de sección). Se cuenta como «por punto con herencia
  que cruza fichas», con los caracteres heredados, porque ese texto viaja al modelo con la unidad.

## Lo que la regla no decide

Si el texto de las páginas de cuerpo entre fichas es prescriptivo o de registro: eso lo lee L4
(estrato «cuerpo entre fichas»).
