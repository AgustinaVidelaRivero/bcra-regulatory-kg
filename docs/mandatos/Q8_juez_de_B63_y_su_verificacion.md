# Mandato Q8: el juez de B6.3 y su verificación

**FIRMADO por la autora el 19/10/2026** (por mensaje recibido a las 13:46:19; hoja de ruta de la mesa, §180), con las cuatro decisiones
del §5. Rige desde esta firma. La versión para firmar está en el paquete de la mesa (`decisiones_179_mesa/q8/`, sha256 `17dc3db8…`).
El texto firmado son las líneas anteriores a «## Firma»: no se edita después y recibe notas fechadas debajo de esa sección.

Va antes del pre-registro de A2.2, que congela el juez (nota del 15/10/2026 al pie del mandato de A2.1,
`docs/mandatos/A2_1_sistema_por_fragmentos_preregistro_A2_2.md:239-251`). Q8 es «la unidad de calibración del juez antes de B6.3»
(`docs/checklist_pre_escalado.md:205`).

## 1. Lo que ya está decidido y hecho

- **El gold, en dos mitades** (registro, §9, Q12, tal cual): «Las 20 para ajustar el juez salen de respuestas de EV2 que ya existen […].
  Las 20 para verificarlo salen de las respuestas de A2.2 y sirven también como su muestra simétrica. Las leo a ciegas, antes de ver
  cualquier veredicto.»
- **El criterio de aceptación** (registro, §9): en la mitad de verificación, Wilson inferior de al menos 0,85 por criterio y al menos 18 de
  20 por respuesta. «Si no se cumple, frenás y decido.»
- **A2.2 y B6.3 usan el mismo juez,** congelado por sha antes de firmar el pre-registro de A2.2. Si el ajuste no está antes de esa firma,
  A2.2 corre con el juez de EV2 y el ajustado se verifica después, sobre las mismas 20 (nota al pie del mandato de A2.1).
- **La mitad de ajuste, leída y cruzada** (`data/experiment/ev2_juez/gold_q12_ajuste/acta_gold_q12_ajuste.md`, `674f1a4b`), con los
  veredictos del juez de EV2 (`claude-sonnet-4-6`, prompt v1), que ya existían:

| Cifra | Valor |
|---|---|
| Acuerdo por criterio, los 82 pares | 79 de 82 (Wilson al 95 %, 0,8979 a 0,9875) |
| El juez acredita lo que la autora no (dirección A) | 0 |
| El juez no acredita lo que la autora sí (dirección B) | 2 criterios (G13-3 y G14-3) |
| «Dudoso» del juez, como desacuerdo | 1 (G02-3) |
| Acuerdo por respuesta | 18 de 20 (0,699 a 0,9721) |
| Sin G02 (la que llegó a su adjudicación en EV2) | 76 de 78 por criterio, 18 de 19 por respuesta |

- **Esta mitad no tiene umbral:** sirve para ajustar. El acta lo dice. La autora decidió que el juez queda como está (decisión 1).

## 2. El juez queda como está (decisión 1)

- **El juez de B6.3** es el de EV2 tal cual: `data/experiment/ev2_juez/juez.py`, prompt `fd446f8e…`, N = 3, como en EV2. El pre-registro de
  A2.2 lo congela con su sha.
- **Por qué:**
  - no acredita nada que la autora no acredite (la dirección A es 0). El error que tiene es de más estricto, el que menos sesga a favor
    de un brazo;
  - los dos desacuerdos de la dirección B son dos criterios. Ajustar el prompt con 2 casos de 82 arriesga sobreajustar a esta mitad, y la
    mitad de verificación es la que decide;
  - no se paga ninguna corrida de calibración, y se ahorran las horas de la autora de la iteración del ajuste.
- **Lo que sigue igual:** la mitad de verificación mide el acuerdo del juez antes de B6.3 (§4).

## 3. Si el juez se ajustara (la alternativa, que no rige)

- **Cómo:** con casos resueltos de la mitad de ajuste (los dos de la dirección B y, si hace falta, el dudoso), como en la calibración del
  juez de EV2 y de tripletas (pre-registro de tripletas, §4.3 y §4.7):
  - el prompt lleva el candado: «Este prompt no se modifica sin decisión escrita de la autora. Todo cambio se justifica con evidencia del
    texto de la norma, nunca con la etiqueta esperada de un caso.»;
  - una sola recalibración, declarada;
  - después del cambio, se re-corren las 20 de ajuste (60 llamadas, unos USD 0,76 con los USD 0,0126 por llamada del juez de EV2, NO
    VERIFICADO), y se informa el acuerdo nuevo al lado del viejo.
- **El sha del ajustado** se congela antes de firmar el pre-registro de A2.2. Si no llega, A2.2 corre con el de EV2, y el ajustado se
  verifica después sobre las mismas 20.
- **El costo en horas:** la decisión de cada caso resuelto, unas 0,5 a 1 h de la autora, más la lectura del acuerdo nuevo.

## 4. La mitad de verificación (las dos ramas)

- **La muestra:** 20 de las 120 respuestas de A2.2 (7, 7 y 6 por brazo), estratificadas también por el veredicto del juez, como la
  muestra simétrica de EV2. Su semilla, `gold-q12-verificacion-a22-v1` (decisión 2), va en el pre-registro de A2.2, fijada antes de
  correrlo.
- **El material:** las fichas de la mitad de ajuste (`codigo/armar_fichas_gold_q12_mesa.py`), sin ningún veredicto ni el brazo de origen.
  Lo arma la mesa después de A2.2, y lo deja en una carpeta de lectura de la autora. La clave queda aparte hasta que la autora selle.
- **La lectura de la autora,** a ciegas: en la mitad de ajuste le llevó unas 1 h 25 min para 20 (`acta_gold_q12_ajuste.md`, según su
  cuenta).
- **El cruce,** después del sello de la autora, con el script de la mitad de ajuste. El criterio de aceptación, el del §1.
- **Si no se cumple** (decisión 3), tal cual: «B6.3 se juzga con el juez, la cifra se informa con su acuerdo medido y todo lo dudoso va a
  mi lectura».
- **Cuándo:** después de A2.2 y antes del pre-registro de B6.3, que declara el juez y su verificación.

## 5. Las decisiones de la autora al firmar (19/10/2026, 13:46:19), tal cual

1. «el juez queda como está;»
2. «la semilla de la verificación es gold-q12-verificacion-a22-v1;»
3. «si la verificación no pasa, B6.3 se juzga con el juez, la cifra se informa con su acuerdo medido y todo lo dudoso va a mi lectura;»
4. «un agregado: el juez se verifica con respuestas de EV2 y de A2.2, que no son de varios puntos, y en B6.3 la mayoría lo son. La muestra
   de control de B6.3 (36 respuestas, 12 por brazo) se estratifica también por tipo, y el acuerdo del juez se informa por tipo. Proponé el
   criterio para el acuerdo en varios puntos y qué se declara si no llega, y decime si 36 alcanzan o hace falta otro tamaño, con las
   horas. Va en el pre-registro de B6.3.»
   - El criterio, el tamaño y lo que se declara los propone la mesa (§180) y los fija el pre-registro de B6.3.

## 6. Lo que cambia en el calendario (v9c)

- **Sale** la corrida de Q8 del carril (0,5 a 2 h), porque el juez queda como está, y la iteración del ajuste.
- **«Q8: la parte de la autora» estaba mal ubicada en el v9 y en el v9c:** iba antes de A2.2, y la mitad de verificación sale de las
  respuestas de A2.2. Pasa a ser la lectura de la autora de las 20 de A2.2, de 1,5 a 2 h, después de A2.2 y antes del pre-registro de
  B6.3. El calendario lo corrige en el modelo del punto 6.
- **USD 0** para Q8: los veredictos de las 20 de verificación salen de la corrida de A2.2, que ya los paga.

## Firma

FIRMADO por la autora el 19/10/2026 a las 13:46:19 (por mensaje; hoja de ruta de la mesa, §180), con las cuatro decisiones del §5.
Rige desde esta firma.
