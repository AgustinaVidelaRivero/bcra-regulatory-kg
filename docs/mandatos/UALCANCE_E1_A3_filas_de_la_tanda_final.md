# Mandato U-ALCANCE-E1, etapa A3 — las filas de alcance de la tanda final en el mensaje de E1

**FIRMADO por la autora el 17/10/2026** (firma por mensaje de la autora, recibida a las 20:56:55; hoja de ruta de la mesa, §148), con
la opción (a) de su decisión al firmar. La versión para firmar la redactó la mesa el 17/10/2026 (§147; sha256 `38a1a948e44d…`, en el
paquete de la mesa). El commit de esta firma suma la nota del punto 1 al pie del laudo de la release y de la enmienda 4. Rige desde esta
firma. USD 0, sin API.

**De dónde sale:**
- la enmienda 4 al protocolo entre tandas, §2, firmada en `53bbd6fa` (`:58-86`): la lectura del alcance antes de cada tanda;
- el mandato de U-ALCANCE-E1, firmado en `21e55a07`, y su decisión 1 al firmar: el candado del derivado va en el código, y «el derivado
  crece por tanda, con un cambio declarado entre tandas (F13c)»;
- el laudo de la release r2, firmado en `94087a7f` (`:33`);
- las decisiones de la autora del 17/10/2026: §146, decisión 1 (el material del alcance); §147, decisiones 1 (la nota) y 2 (un documento
  sin fila al despacho).

## 1. La nota, tal cual (va al pie del laudo y de la enmienda 4 con el commit de este mandato firmado)

> **17/10/2026 — Las filas de alcance de cada tanda y el mensaje de E1** (decisión de la autora del 17/10/2026, recibida a las 20:20:12;
> hoja de ruta de la mesa, §147). El mecanismo del mensaje de E1 cambió una sola vez, con el cableado de la tanda 1 (A2 de U-ALCANCE-E1,
> `42823df0`). Después, cada tanda suma sus filas al registro de alcance por la enmienda 4, §2, punto 3 (`53bbd6fa:64-66`): la lectura
> «cambia solo el mensaje de sus unidades: el de toda unidad ya extraída sale byte a byte igual, y se controla». Con cada tanda se
> regeneran el derivado del registro (`catalogo_unico/registro_alcance_r2b.json`) y su sha en
> `reextraccion_v2/e1_extractor/prompt_r2b.py` (`:477`), y se recomputan los dos valores del candado del mensaje (`:97-98`), con el control
> byte a byte de los mensajes de lo ya extraído. Es lo que previó la decisión 1 del mandato de U-ALCANCE-E1 al firmar (`21e55a07`). La
> release sigue siendo r2. Los valores nuevos los confirma la autora antes de la extracción de la tanda. El texto firmado no cambia.

- En el laudo, la nota se refiere al renglón «Mensaje de E1» del §1 (`:33`).
- En la enmienda 4, precisa el «No congela» del §6 (`:130-131`).

## 2. Lo que falta

La tanda final tiene 98 documentos.
- 52 tienen rol o clase en la tabla de la release (`catalogo_unico/generados_r2/rol_por_to_r2.json`) y quedan como están.
- 46 no tienen ni fila en el registro ni rol (paquete de la mesa, §146, `recuento_alcance_tanda_final_v2.json`). La autora los lee con
  la enmienda 4, §2, y sus filas van a una tabla «## Tanda final» del registro de alcance
  (`catalogo_unico/registro_alcance_por_tanda.md`), en un commit propio.
- Sin esta etapa, el mensaje de E1 de la tanda final no lleva esas líneas: el derivado de hoy sale de `--tandas 1` (`e06933e7…`).

## 3. Lo que cambia

1. **El derivado.** `catalogo_unico/code/derivar_registro_alcance_r2b.py --tandas 1,final` lo regenera desde el registro con las filas de la
   tanda final. Las entradas de la tanda 1 salen byte a byte iguales; se suman solo las de la tanda final con clase, dos clases o rol
   reutilizado. Una fila «sin alcance declarado» no tiene entrada.
2. **El candado del derivado.** `REGISTRO_ALCANCE_R2B_SHA256_ESPERADO` (`prompt_r2b.py:477`), con un renglón de comentario de A3 en el
   bloque que lo precede (`:470-475`).
3. **El candado del mensaje.**
   - Se recomputan `CANDADO_MENSAJE_JSON_SHA256_ESPERADO` y `MENSAJE_R2B_SHA256_ESPERADO` (`:97-98`), con el método de `sellar_a2.py`.
   - Si la fixture no toca ninguna entrada nueva, salen iguales, y se dice.
   - Los tres valores quedan PROPUESTOS hasta la confirmación de la autora.
4. **El selftest.** `selftest_prompt_r2b.py` suma un caso: una fila de una tabla «## Tanda final» entra con `--tandas 1,final` y no con
   `--tandas 1`.
5. **La tabla de reprocesamiento.** La fila F13c suma un renglón: el derivado de la tanda final, desde A3, sin reprocesamiento, porque la
   tanda final no está extraída.

## 4. Las condiciones para empezar

1. El commit de T2 de la tanda 1, y T3 a T5 cerrados: una ejecutora por vez en el repo.
2. El commit de las filas de la tanda final en el registro, con la planilla sellada de la autora y el control de la mesa.
3. Este mandato firmado, y su commit con la nota del punto 1.
4. **La hora de arranque, a más tardar el martes 20/10/2026 a las 21:15** (decisión 1 al firmar, abajo). Si a esa hora falta la fila de algún
   documento:
   - A3 corre con las filas que hay;
   - el documento sale de la tanda final, declarado, al grafo corregido;
   - si tiene preguntas de B6.3, rige la regla de reemplazo (registro de decisiones, `:451-454`; decisión de la autora del 17/10, §147).
   - Sacarlo no es parte de A3: lo hace la mesa en el pre-registro y en el manifiesto de la tanda final.

## 5. Los criterios de aceptación

Cada uno con su comando y su salida, en `data/experiment/alcance_e1/a3/`:
1. **La tanda 0, igual:** por el camino del runner (`runner_corpus.configurar` → `perfil_e1.perfil("r2b")`), las 2.439 unidades con 0
   distintas, y el sha de los mensajes `48fdec197658…`, el de A2.
2. **La tanda 1, igual:** sus 3.290 unidades, con 0 distintas contra HEAD.
   - Los mensajes se arman desde la E0 y el código, regenerada la E0 en la copia con el lote de A2.
   - Sin leer ninguna salida de T2 de la tanda 1.
3. **La tanda final:**
   - cambian solo los documentos con fila nueva de clase, dos clases o rol reutilizado, y solo en la línea de alcance (el mensaje nuevo,
     sin «línea + salto + salto», es el de HEAD);
   - por documento: unidades, caracteres y tokens agregados y su costo a la tarifa de E1, medidos en seco;
   - la lista de los documentos de la tanda final sin fila ni rol, que tiene que ser vacía o los que la mesa sacó, con su id.
4. **El derivado:** dos corridas iguales byte a byte, e iguales al archivo. Contra el de HEAD, solo renglones agregados, ninguno quitado.
5. **`selftest_prompt_r2b`:**
   - HEAD sobre HEAD, en verde;
   - A3, en verde;
   - el selftest de A3 con el código de HEAD falla exactamente el caso nuevo.
6. **`selftest_clave_cache --salida-r2b`:** OK en dos corridas iguales, con A1r y A3r sin cambios.
7. **Los vecinos, en las dos copias,** con consolas iguales con HEAD y con A3: `selftest_catalogo_unico`, `selftest_reresolver_catalogo`
   (66/66), `selftest_cablev3` y `selftest_manifiesto` (44/49 fuera de la raíz del repo, como anticipa CLAUDE.md §4.l).
8. **Los tres valores PROPUESTOS,** con `--verificar` sobre la copia final.
9. **La foto sha256 del repo** antes y después de cada corrida, y el conteo de `.pyc`.
10. **La corrida en seco** importa `prompt_r2b` por el mismo camino que el runner (CLAUDE.md §4.l, último párrafo).
11. **El grep de convenciones.**

## 6. Escrituras, prohibiciones y requisitos

- **ESCRITURAS:**
  - `catalogo_unico/registro_alcance_r2b.json`;
  - `reextraccion_v2/e1_extractor/prompt_r2b.py`: `:477`, su comentario y, si cambian, `:97-98`;
  - `selftest_prompt_r2b.py`;
  - la fila F13c de `data/experiment/mantenimiento/tabla_reprocesamiento.md`;
  - `data/experiment/alcance_e1/a3/` (se crea: el FRENO, los scripts y las salidas);
  - el scratchpad.
- **PROHIBIDO:**
  - el registro de alcance: solo se lee, porque lo escribe la autora con la mesa;
  - el prefijo de E1 y sus parches, y el tool schema;
  - `bloque_catalogo_r2.txt`, `rol_por_to_r2.json` y `catalogo_sujetos_r2.json`;
  - `candado_mensaje_r2b.json`, salvo que un caso de la fixture lo pida, y entonces se frena y se pregunta;
  - E3, el ensamblado y los grafos sellados;
  - las salidas de T2 de la tanda 1, sus conteos y sus marcas de copia (cegamiento de U-MED-VERIF, pre-registro de la tanda 1, `:900-909`);
  - la API, commitear y la memoria.
- **REQUISITOS:**
  - CLAUDE.md §4, de a a l;
  - copias sin enlaces, y una ejecutora por vez en el repo;
  - USD 0, sin API.
- **TIEMPO:** de 0,5 a 1 día (comparable de A2; hoja de la mesa, `:156`; NO VERIFICADO).
- **FRENO:** «FRENO A3», con los valores PROPUESTOS. La mesa lo revisa sobre una copia, y la autora confirma los valores. El commit lo
  prepara la mesa y lo corre la autora.

## 7. Decisión de la autora al firmar

1. **La última hora de arranque de A3** (decisión 2 de la autora del 17/10; calendario v6 de la mesa, §147). Opciones:
   - (a) la del escenario lento, el martes 20 a las 21:15: 10 h de A3, y el despacho más tarde que todavía sella el viernes 23 a las
     18:00, el miércoles 21 a las 16:15. Es la recomendación de la mesa, porque la duración real no se sabe hasta que corra;
   - (b) la del central, el miércoles 21 a las 11:00, con 6 h de A3.
   - **Decidido: (a), el martes 20/10/2026 a las 21:15** (la autora, al firmar, el 17/10/2026; recibido a las 20:56:55).

## Firma

FIRMADO por la autora el 17/10/2026 (por mensaje, recibido a las 20:56:55; hoja de ruta de la mesa, §148), con la opción (a). Rige desde
esta firma. A3 empieza cuando se cumplen las condiciones del §4.
