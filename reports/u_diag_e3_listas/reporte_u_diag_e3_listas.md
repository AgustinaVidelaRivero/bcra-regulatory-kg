# FRENO de U-DIAG-E3-LISTAS (06/10/2026; solo lectura, USD 0, sin API ni Neo4j; sin commit)

Leí HEAD `723680e` copiado con `git archive` al scratchpad (1.070 archivos, 0 enlaces) y corrí todo sobre esa copia, importando `prompt_r2b`, `prompt_e3` y `comun_e3` con sus candados en verde. HEAD avanzó a `f36b01d` durante la sesión; los tres commits nuevos no tocan ninguna ruta que leo (`git diff --name-only 723680e HEAD` sobre ellas: 0).

**1. Qué recibe E3 y qué sabe.**
- El fuente de E3 lleva solo los bloques heredados de tipo `encabezado` (`comun_e3.py:123-125`), y las citas se verifican contra lo mismo (`:226-227`).
- De 2.440 unidades verificadas, 1.054 llevan LINEA_ITEM. Su bloque que abre la lista es intro en 982, encabezado en 39, intersticial en 22 y chapeau_seccion en 11, y solo llega al «TEXTO FUENTE» del mensaje de E3 en los 39 (`fase1_resumen.json`). En `cla::5.1.1.1` es «[intro | punto 5.1.1] Abarca todas las financiaciones comprendidas, con excepción de las siguientes:», y no llega.
- Las instrucciones no conocen la composición: el prefijo de E3 (`21a836c7de6d`) no la menciona, y `NOTA_E3_ENCABEZADO_LISTA` (`prompt_e3.py:256-264`) va solo al mini-chunk del encabezado (`:315-316`): la llevan 0 de los 1.054 ítems.
- Contradicción: `prompt_e3.py:57` le dice a E3 que recibe «párrafos introductorios, intersticiales y de cierre», y el código no los manda (tabla de reprocesamiento, `:61`).
- Contradicción con el mandato: el ancla `prompt_r2b.py:287-290` son líneas del texto armado del prefijo, no del archivo (en el archivo son de `bloque_flags`). Las reglas están en `prompt_r2b_reemplazos.json:12`, `:108` y `:114`, y en `prompt_r2b_parche_p3c.json:48`.

**2. Reclamos sobre una Excepcion en los ítems.** Adjudiqué 96 reclamos de ítems que nombran una excepción, volcados a las 16:19:26, antes de computar: polaridad o sentido (P) 5, contenido que E3 no encuentra (C) 7, norma del encabezado pedida como entidad del ítem (B) 31, sujeto o condición del encabezado (B2) 3, modalidad 3, salvedad no representada 14 y otros 33.
- P son 5 reclamos en 5 unidades: 4 de severidad media y 1 alta. Hay 1 bloqueante (`ext::3.5.6.1`, en la re-verificación) y 4 residuales. Los 5 están en ítems cuyo bloque no llega a E3.
- Leí los 5 (censo) y ninguno es fundado. 3 son falsas alarmas por la lista: `cla::5.1.1.1`, `ext::3.5.6.1` y `ext::3.6.1.1`. Los otros 2 son una equivalencia lógica del texto propio («sólo será aplicable para…», en `ext::4.4.4` y `ext::4.5.3`).
- De los C, 5 de 7 son falsas alarmas por la lista. Los B piden en el ítem una norma que P3C-d1 y P3C-d2 prohíben emitir ahí (`prompt_r2b_parche_p3c.json:83` y `:90`); 16 de los 31 son bloqueantes.

**3. Efecto.**
- De los P, ninguno disparó un reintento: los 3 del intento 0 son de severidad media, y solo bloquea la alta (`ratchet_e3.py:98`). Los 2 de la re-verificación aparecieron tras reintentos que dispararon otros reclamos: un B en `ext::3.5.6.1` y un C en `ext::3.6.1.1`.
- Cola: 2 de las 74, las dos entre las 29. En `ext::3.5.6.1` persistió el propio P; en `ext::3.6.1.1`, un B. Copia real de la nota: 0, porque la copia solo se mide al aceptar tras un reintento (`ratchet_e3.py:520-524`).
- Con P, C, B y B2 juntos (40 unidades): 17 reintentos por esos reclamos y 7 unidades en la cola, 5 de ellas entre las 29. Hay 2 copias reales (`ext::2.6.1.2` y `ext::3.6.1.6`), las dos con la ventana tomada de una nota sobre el encabezado.
- De las 29, 17 son ítems. En 9 el reclamo persistente trata del encabezado: 5 son falsas alarmas, 2 errores reales de modalidad (`pro::4.2.1.4` y `lingob::7.1.7`) y 2 dudosos. En 4 trata de un cierre o del intro de un ancestro, que E3 ve solo por las omisiones del extractor. En los otros 4 no tiene relación.

**4. ¿Es general?** En la entrada de E3, sí: 1.015 de los 1.054 ítems no reciben el bloque, y ninguno recibe la regla. En la polaridad estricta, no: son 5 reclamos.
- La familia «agrega o invierte» aparece en 70 de los 1.015 ítems sin el bloque, en 1 de los 39 con el bloque y en 20 de las 1.386 unidades que no son ítems. En una muestra de 15 (semilla 20261006, sorteada a las 16:14:39), 9 son falsas alarmas por la lista (Wilson al 95 %: [0,357; 0,802]).
- Los ítems son 1.054 de las 2.440 unidades, pero 50 de las 74 de la cola. En ext son 35 de 577 contra 8 de 396 no ítems; en cap, al revés: 1 de 93 contra 9 de 370. La asociación no es uniforme; la causa la muestra la lectura.
- Propuesta (detalle en `UDIAG_E3_LISTAS_propuesta_punto4.md`): un cambio en el código del mensaje de E3, solo con la forma r2. (a) Sumar al fuente del ítem, y a sus citas, el bloque que abre la lista, sin los cierres. (b) Una NOTA del ítem con la regla, en espejo de `NOTA_E3_ENCABEZADO_LISTA`. No toca las instrucciones, los calibradores, `PREFIJO_HASH` ni el namespace, así que no es un cambio del prompt congelado.
- Tabla, para (b): es F23 (`:174`). Frena hasta re-sellar el candado del mensaje de E3; después corre E3 de los 1.054 ítems, USD 10,78 a 0,010226 por unidad (`:360`). E1 sale de la caché, y los reintentos cambian donde cambia el feedback.
- Tabla, para (a): NO ENCONTRADO. F02 y F03 (`:136-137`) cubren el texto de un bloque, no la regla de qué bloques entran; hace falta una fila nueva con su variación en el selftest de claves.
- Ninguna de las 6 unidades de `candado_mensaje_e3.json` es un ítem (medido): sin un caso de ítem en esa fixture, el cambio movería las claves sin que el candado frene.
- Ponerlo en las instrucciones sería F10 (`:150`): E3 de todas las unidades (USD 24,9403 en la tanda 0, `:361`), namespace nuevo, y choca con E3 congelado por el laudo (`ratchet_e3.py:32`). No lo recomiendo.

**Controles.**
- sha256 de todo el repo salvo `.git`, a las 16:08:24 y a las 16:28:05, después de todas las corridas. Cambiaron 18 archivos y aparecieron 2: 16 son de los tres commits, y los otros son `sincola_t0/freno_sc1.md` y tres `.DS_Store`. Ninguno lo escribí yo. Entradas `.pyc`: 11.236 antes y después.
- Las salidas se reproducen byte a byte con `UDIAG_E3_LISTAS_comandos.sh`; la única diferencia, declarada en el manifiesto, es el orden de las claves de un diccionario de `fase2_resumen.json`.
- Error propio: antes del sorteo vi, en una vista previa, cinco reclamos del indicador, y uno (`pro::3.2.3.7`) salió en la muestra. El sorteo tiene semilla fija, pero esa lectura no fue a ciegas.
- Grep de convenciones sobre el paquete (nombres propios, rutas absolutas, referencias a mensajes): 0 nombres y 0 rutas. Solo 8 «correo», todas en texto del corpus (`UDIAG_E3_LISTAS_grep_convenciones.txt`).

Paquete: `revision_UDIAG_E3_LISTAS/`, con `manifest.txt`. Commit PENDIENTE de la autora; espero la revisión.
