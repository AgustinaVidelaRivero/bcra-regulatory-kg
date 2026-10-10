# U-SEG-OFICIAL, S1-ter: método de la adjudicación (registro de la mesa, 10/10/2026)

Decisiones de la autora del 10/10/2026, tomadas sin haber abierto nada de la pasada 1 ni de la lectura. Se registraron en la hoja de ruta
de la mesa a las 18:52:27 (§58), antes de que la autora abriera la pasada 1. Completan el diseño de `LEEME_adjudicacion_S1ter.md`.

## Quién pone la marca

- **Pasada 1:** ningún modelo le propone marcas a la autora. La lectora fue Claude Opus 5.5, el mismo modelo que la mesa de apoyo.
  - Las consultas de la autora a la mesa de apoyo son solo sobre cómo se aplica el criterio.
  - La marca la pone la autora, sobre la imagen.
- **Pasada 2:** la mesa de apoyo le señala a la autora qué regla del criterio está en juego en cada ficha, y la marca final la decide
  ella.

## El sello de la pasada 1

- Antes de correr `pasada_2_S1ter_v2.py seleccionar`, la mesa verifica la pasada 1 de la autora contra el sello de la autora: toma el
  sha256 del archivo de sello, no lo calcula del TSV, y se lo pasa al script, que lo controla.
- `armar` usa ese mismo archivo, con el mismo sha256.
- Si la pasada 1 no da el sello, la mesa frena sin correr nada.

## El acuerdo de la etapa 1

- Se informa sobre las 90 fichas y, además, sin las 19 primeras del orden de la lectura (`E1-001` a `E1-019`), por el incidente de las
  imágenes (`../lectura/incidentes_lectura_S1ter.md`).
- Lo calcula `acuerdo_etapa_1_S1ter.py`, aparte de los scripts v2. Está fijado, sellado y probado con datos sintéticos
  (`sello_acuerdo_etapa_1_mesa.txt`; prueba en `prueba_acuerdo_etapa_1_S1ter.py`, salida en `salida_prueba_acuerdo_etapa_1_S1ter.txt`).
- Se corre después de la adjudicación. Ninguna de las dos cifras decide nada.
