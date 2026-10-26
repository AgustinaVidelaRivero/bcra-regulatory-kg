# El gold de Q12, mitad de verificación: acta de la lectura y del cruce con el juez de A2.2 (mesa, §277, 26/10/2026)

## El diseño y el sorteo

- **El diseño:** el gold en dos mitades (registro de decisiones, §9, `:294-303`). La de ajuste está en `../gold_q12_ajuste/`. Esta, la
  de verificación, sale de las respuestas de A2.2 y es también su muestra simétrica (Q8, §4; pre-registro de A2.2, §4).
- **El sorteo** (`sorteo/`):
  - la regla (`25058237…`) y el script (`697ade45…`) quedaron sellados por la mesa el 25/10/2026 a las 22:50:21, antes de correr sobre
    datos reales (`sello_sorteo_gold_q12_verificacion_mesa.txt`). Su prueba, con datos sintéticos, está en
    `probar_sorteo_gold_q12_verificacion_mesa.py`;
  - la semilla es `gold-q12-verificacion-a22-v1`. La población son las 118 respuestas de N = 1 de A2.2 con juicio, sin las
    `requiere_adjudicacion`. El sorteo tomó 7, 7 y 6 por brazo, estratificadas por la clase del juez, con 20 preguntas distintas;
  - dio 20 respuestas y 82 criterios. Corrió con el comando de la autora del 26/10/2026; el material de su lectura es de las 09:51:13;
  - la clave (`clave/`, `95151641…`) quedó en el paquete de la mesa y se abrió después del sello de la autora.
- **Lo que leyó la autora** (`para_leer/`): la regla de lectura, cómo se mide el juez y las 20 respuestas con sus criterios, sin ningún
  veredicto ni el brazo de origen.
  - La mesa volvió a armar las fichas con `codigo/armar_fichas_gold_q12_verificacion_mesa.py` y la misma clave. Los 28 archivos dan el
    mismo sha256 que los de la carpeta de lectura de la autora, y la consola da igual.
  - Las planillas de `para_leer/` son las vacías del armado. Los cinco PDF fuente no entran al repo: están en `data/experiment/subset/`,
    que el `.gitignore` deja fuera.

## La lectura

- **La leyó la autora el 26/10/2026, a ciegas.** Su declaración, tal cual: «Las marcas son mías, decididas a ciegas, sin ninguna salida
  de un modelo. La planilla de criterios la exporté dos veces, porque la primera vez se exportó la de respuestas encima; el sello es sobre
  la segunda exportación, y las dos planillas dieron sus columnas.»
- **Sus planillas están en `lectura/`,** selladas a las 10:48:47 con `sellar_planillas_gold_q12_verificacion.py`
  (`sello_gold_q12_verificacion.txt`):
  - `planilla_criterios_gold_q12_verificacion.csv`, `d5dddc24…`;
  - `planilla_respuestas_gold_q12_verificacion.csv`, `ec47fd29…`;
  - junto a ellas, `estructura_planillas.json`, la plantilla contra la que se controlan.
- **El control de la mesa** lo hace el cruce, antes de cruzar, y da bien:
  - el sha256 y los bytes son los del sello;
  - las columnas y los renglones son los de la plantilla, en su orden: 82 y 20;
  - cada valor obligatorio está en la plantilla.
- **El formato:** las dos planillas usan punto y coma y no traen BOM. Ninguna celda trae otra forma que la de la plantilla. Una trae un
  espacio de más al final (VG01-2, «criterio mal planteado»), y se lee sin él. Los minutos traen un número en las 20.

## Lo que marcó la autora

- **Por criterio:** 72 cumplidos y 10 no cumplidos.
- **Sus marcas:** «dudosa para mí» en 2 (VG12-1 y VG12-2); «necesita experto del dominio», ninguna; «criterio mal planteado», 4 (VG02-2
  a VG02-5).
- **Por respuesta,** con la regla de EV2 (`ev2_juez/mapping.py:40-54`): 15 correctas y 5 parciales.
- **La clasificación:** 20 de contenido.
- **Errores fuera de los criterios:** 2 de 20 (VG05 y VG07).
- **Los minutos:** 224 en las 20, según su cuenta.

## El cruce

Lo hace `cruce/cruce_gold_q12_verificacion_mesa.py`. Es el script de la mitad de ajuste, como pide Q8 (§4), con los juicios de N = 1 de
A2.2 (`banco_mcp/a2_2/juez/n1/agregados_n1_ciego.json`, `e22ee010…`, el sha256 que fijó la clave del sorteo). El juez es el de EV2 tal
cual: `claude-sonnet-4-6`, prompt v1, 3 repeticiones. Los juicios ya estaban: no se paga nada. Las salidas están en `cruce/`.

| Cifra | Valor |
|---|---|
| Acuerdo por criterio, los 82 pares | 82 de 82 (1,0; Wilson al 95 %, 0,9552 a 1) |
| Dirección A (el juez acredita lo que la autora no) | 0 |
| Dirección B (el juez no acredita lo que la autora sí) | 0 |
| «Dudoso» del juez | 0 |
| Sin «necesita experto» ni «criterio mal planteado» | 78 de 78 (1,0; 0,9531 a 1) |
| Acuerdo por respuesta, las 20 | 20 de 20 (1,0; 0,8389 a 1) |
| Direcciones A y B, por respuesta | 0 y 0 |
| «requiere_adjudicacion» del juez | 0 |
| Abstención o contenido | 20 de 20 |

- **Un control del cálculo:** las marcas de la autora contra el juez de otra ficha con el mismo número de criterios dan 61 de 77. El
  cruce no compara una cosa consigo misma.
- **El juez:** 72 cumplidos y 10 no cumplidos por criterio; 15 correctas y 5 parciales por respuesta.

## El criterio de aceptación

- **Tal cual** (Q8, §1; registro de decisiones, §9, `:298-299`): «en la mitad de verificación, Wilson inferior de al menos 0,85 por
  criterio y al menos 18 de 20 por respuesta. Si no se cumple, frenás y decido.»
- **Se cumple:** el Wilson inferior por criterio es 0,9552, y el acuerdo por respuesta, 20 de 20. La cifra que decide es la principal,
  con todas las marcas adentro.
- **Lo que sigue:** el juez queda como está (Q8, decisión 1). En B6.3, lo dudoso va a la lectura de la autora, como antes (registro de
  decisiones, §9, `:300`: «Lo dudoso de B6.3, todo para mí»).
- **Llegó después de la firma** del pre-registro de B6.3 (25/10/2026). Va como desvío declarado de Q8, que la ponía antes (`:71`), con su
  regla de consecuencias igual (pre-registro de B6.3, §13, punto 2). Es el resultado de su H-11.
