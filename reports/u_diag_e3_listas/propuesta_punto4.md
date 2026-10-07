# U-DIAG-E3-LISTAS, punto 4: cómo darle a E3 el encabezado de la lista (propuesta, sin implementar)

Fuentes leídas en HEAD `723680e` (copia por `git archive`; `2c77050`, que llegó durante la sesión, no toca ninguna de
estas rutas). Las líneas citadas son de esos archivos en HEAD.

## 1. Por qué el problema es general

- La entrada de E3 no trae el bloque que abre la lista en 1.015 de los 1.054 ítems: el fuente de E3 lleva solo los
  bloques heredados de tipo `encabezado` (`comun_e3.py:123-125`; las citas se verifican contra lo mismo,
  `comun_e3.py:226-227`), y el bloque que abre la lista es `intro` en 982, `intersticial` en 22 y `chapeau_seccion`
  en 11 (`fase1_resumen.json`). En los 39 restantes el bloque es la línea de título del punto, que E3 sí ve.
- Ningún ítem lleva la regla: el prefijo de E3 (hash `21a836c7de6d`) no habla de composición, y
  `NOTA_E3_ENCABEZADO_LISTA` (`prompt_e3.py:256-264`) va solo al mini-chunk del encabezado
  (`prompt_e3.py:315-316`): 0 de 1.054 ítems.
- El texto del prefijo le dice a E3 que recibe «párrafos introductorios, intersticiales y de cierre»
  (`prompt_e3.py:57`), pero el código no los manda (`comun_e3.py:116-121`; tabla de reprocesamiento, `:61`).
- La polaridad estricta es rara (5 reclamos, todos falsas alarmas). Lo frecuente es la familia «lo extraído agrega o
  invierte contenido» y «falta la norma del encabezado»: muestra de 15, 9 falsas alarmas por la lista (Wilson al
  95 %, [0,357; 0,802]); 31 reclamos B piden en el ítem la norma del encabezado, que P3C-d1 y P3C-d2 mandan no emitir
  ahí (`prompt_r2b_parche_p3c.json:83`, `:90`); de los 17 ítems entre las 29 unidades de flag `cola_humana`, 9
  persistieron con reclamos sobre el encabezado (5 falsas alarmas, 2 errores reales de composición, 2 dudosos).

## 2. Propuesta: cambio en el código del mensaje de E3, solo con la forma r2

Dos piezas, las dos en el mensaje de usuario (después del breakpoint), nunca en el prefijo:

(a) **El bloque que abre la lista entra al fuente del ítem.** Para una unidad con `prompt_r2b.bloque_lista(chunk)`
distinto de `None` (y que no es mini-chunk), el TEXTO FUENTE del mensaje de E3 suma ese bloque, y solo ese (no los
cierres que lo siguen), con su rótulo de siempre (`[intro | punto X]`), y `fuente_para_citas` lo suma también, para
que una cita tomada de él verifique. La regla que elige el bloque es la misma que arma `LINEA_ITEM` en E1
(`prompt_r2b.py:306-320`, `:411-420`): E3 y E1 ven el mismo encabezado.

(b) **Una NOTA del ítem**, constante del módulo como `NOTA_E3_ENCABEZADO_LISTA`, con la regla vista desde E3. Texto
a fijar en la unidad que la implemente; contenido mínimo:
- esta unidad es un ítem de la lista que abre el bloque [tipo | punto X]; en esta extracción la norma del ítem se
  compone con ese encabezado: el sujeto, la modalidad, el cuantificador y lo que el encabezado fija para cada ítem
  (plazo, ámbito, condición) aparecen en el ítem, y eso no es contenido agregado;
- la norma que el encabezado enuncia no se emite como entidad aparte en el ítem (va nombrada en la descripción): que
  falte aquí no es faltante;
- si el encabezado anuncia lo que queda afuera de una clase, el ítem es una Excepcion; una contra-excepción del ítem
  va como la norma que vuelve a regir, con sus Condicion.

Las dos piezas deben ir condicionadas a la marca `forma_salida = "r2"` de la validación, como `notas_r2`
(`prompt_e3.py:334-335`): `fuente_integro` y `fuente_para_citas` son compartidas con la cadena r1, y sin la marca el
mensaje tiene que quedar igual byte a byte.

**No es un cambio del prompt congelado.** No toca `INSTRUCCIONES` ni los calibradores ni el tool schema; no cambia
`PREFIJO_HASH` (`prompt_e3.py:217`, sellado en `:385`) ni el namespace de E3. Ponerlo en las instrucciones sería F10.

## 3. Qué exige la tabla de reprocesamiento (`data/experiment/mantenimiento/tabla_reprocesamiento.md`)

- **(b) es F23** (`:174`): «NOTA del mensaje de E3 en la forma r2». Clave de E1, no cambia; clave de E3, frena por el
  candado del mensaje de E3 hasta re-sellarlo; re-sellado, E3 de las unidades que llevan la nota (los 1.054 ítems de
  la tanda 0), E1 de la caché, y los reintentos cambian donde cambia el feedback. Costo con la tarifa observada de
  E3, USD 0,010226 por unidad (`:360`): 1.054 × 0,010226 = USD 10,78, más los reintentos que no se pueden estimar
  sin correr.
- **(a) no tiene fila: NO ENCONTRADO.** F02 y F03 (`:136-137`) cubren un cambio del texto de un bloque heredado; la
  regla de qué bloques entran al fuente de E3 no está, y `:61` dice que E3 no recibe la prosa heredada. Necesita una
  fila nueva (clave de E1, no cambia; clave de E3, cambia en los ítems; E3 de las afectadas) y su variación en el
  selftest de claves, como R30 para F23. Además cambia qué reclamos tienen cita verificada y, con eso, qué unidades
  reintentan o van a la cola por `veredicto_inutilizable` (`ratchet_e3.py:553-560`): toca el lazo como F24 (`:175`).
- **Candado del mensaje de E3.** Ninguna de las 6 unidades de `candado_mensaje_e3.json` es un ítem de lista
  (medido: `fase1_resumen.json`, `candado_e3_unidades_con_linea_item = []`). Sin agregar a la fixture un ítem con el
  bloque `intro` y otro con el bloque `encabezado`, y re-sellar `MENSAJE_E3_SHA256_ESPERADO` (`prompt_e3.py:406`),
  (a) y (b) moverían las claves de E3 sin que el candado frene: el riesgo que el propio comentario del candado
  describe (`prompt_e3.py:394-401`).
- **La alternativa en el prefijo es F10** (`:150`): E3 de todas las unidades (USD 24,9403 observados en la tanda 0,
  `:361`), namespace nuevo, el candado del prefijo frena (F10b, `:151`), y choca con el laudo que declara E3
  congelado (`ratchet_e3.py:32`). No la recomiendo.

## 4. Lo que la propuesta no resuelve

- Los 2 errores reales de composición entre las 29 (`pro::4.2.1.4` y `lingob::7.1.7`, modalidad del encabezado mal
  compuesta) son del extractor: con el bloque a la vista, E3 los seguiría marcando, y está bien.
- 4 de los 17 ítems de las 29 persistieron con reclamos sobre un cierre o sobre el intro de un ancestro, que E3 ve
  solo porque el extractor los declaró en sus omisiones (`ubicacion_citas_29_items.json`). Pasar el bloque que abre
  la lista no los toca; es una decisión aparte.
- Los dos reclamos de polaridad de `ext::4.4.4` y `ext::4.5.3` son falsas alarmas por equivalencia lógica del texto
  propio; tampoco dependen de la lista.
- No medí si con (a) y (b) E3 deja de marcar: eso pide llamadas a la API, fuera del mandato (USD 0).
