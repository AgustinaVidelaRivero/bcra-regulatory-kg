# Cómo se mide el juez con la muestra de control de B6.4 (mesa, §383, 01/11/2026)

Fijado antes de que la autora lea. Es el de B6.3
(`data/experiment/banco_mcp/b63/control_36/para_leer/como_se_mide_el_juez_control_36_B63.md`), con lo que fija el pre-registro de
B6.4 (§5, firmado en `55ee1a5a`, renglones 201 a 207).

## Qué se compara

- **Del lado del juez:** sus juicios de B6.4 sobre estas mismas 36 respuestas, ya hechos, por id opaco
  (`fuera_del_repo/banco_b64/juez/agregados_b63_ciego.json`):
  - el modal de sus tres repeticiones por criterio (`modales`);
  - el veredicto de la respuesta (`veredicto_pregunta`);
  - la clasificación modal (`clasificacion_respuesta_modal`).

  Es el juez de EV2, como en B6.3 (§5 del pre-registro de B6.4).
- **Del lado de la autora:** las dos planillas de esta carpeta, selladas.
- **El cruce:** lo hace la mesa después del sello, con un script que se prueba con datos de juguete antes de abrir la clave.
  - Controla primero el sello, las planillas y que los demás archivos de esta carpeta sigan con el sha256 anotado antes de empezar
    (`../copia_vacia/sha256_para_leer_control_36_B64.txt`).
  - Recién después abre la clave del sorteo y los juicios del juez. Si algo no da, frena sin abrirlos.
- **Ninguna de las 36 es una `requiere_adjudicacion`** (la regla del sorteo): ningún criterio del juez es «dudoso».

## Las cifras

Los tres tipos de B6.4 son de varios puntos: las cifras principales van sobre las 36 juntas (135 pares de respuesta y criterio). Al lado,
por tipo (12 respuestas cada uno), sin piso.

1. **Acuerdo por criterio:** mismo veredicto del juez y de la autora, sobre todos los pares (respuesta, criterio), con su Wilson al 95 %.
2. **Acuerdo por respuesta:** mismo veredicto de la respuesta (correcto, parcial o incorrecto). El de la autora sale de sus criterios con
   la misma regla del juez (`data/experiment/ev2_juez/mapping.py:40-54`). Se informa sin umbral, como en B6.3.
3. **Las dos direcciones del error,** por criterio y por respuesta:
   - A: el juez acredita lo que la autora no (juez «cumplido», autora «no_cumplido»);
   - B: el juez no acredita lo que la autora sí (juez «no_cumplido», autora «cumplido»).
4. **La clasificación abstención o contenido:** acuerdo sobre las 36.
5. **El error fuera de los criterios:** cuántas respuestas lo tienen, por brazo (de 12 cada uno) y por tipo, con sus fichas. No entra en
   las cifras de acuerdo.
6. **Lo que se informa aparte,** con su lista de pares:
   - los criterios marcados «dudosa para mí», «necesita experto del dominio» o «criterio mal planteado»;
   - los minutos.
- **Las marcas de la autora:** la cifra principal va sobre todos los pares, con todas las marcas adentro. Al lado va la misma cifra sin
  los pares marcados «necesita experto del dominio» o «criterio mal planteado».

## El piso

- Tal cual (§5): «El piso es el de varios puntos de B6.3: Wilson inferior de al menos 0,85 por criterio.»
- Se compara sin redondear, sobre la cifra principal de las 36 juntas, con todas las marcas adentro. Las cifras por tipo no tienen piso.
- Si no llega, tal cual (§5): «Si no llega, la cifra va con el acuerdo medido al lado, y lo dudoso va a la lectura de la autora.»
