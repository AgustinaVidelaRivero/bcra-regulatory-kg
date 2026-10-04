# U-RERESOL-CAT — FRENO R1: diagnóstico y diseño (04/10/2026)

Mandato: `docs/mandatos/URERESOL_CAT_reresolucion_catalogo.md`, texto firmado leído en `f87ec4a` (105 líneas, sha256
`c8ee1382…`, igual a las primeras 105 líneas del archivo actual) y sus dos notas del 04/10/2026. Precondición
cumplida: HEAD `9f6361e`, cierre de C2 de U-R2-CODIGO-2. USD 0; sin API ni Neo4j; nada se implementó.

Mediciones: `r1_medicion.py`, corrido desde la raíz de una copia del repo (rsync con `--copy-links`, 0 enlaces), sobre
el crudo de r2a, que es el que existe hoy (mandato, R1.5). Salida `salidas/r1_medicion.json`, sha256 `6cdf86ee…`;
doble corrida en dos directorios, byte a byte idéntica. Tomé el sha256 de todos los archivos del repo (salvo `.git`
y `.venv`) antes de empezar (21.993) y al cierre (22.001): ningún archivo existente cambió ni desapareció. Los 8
nuevos son los 3 de esta unidad y 5 de otras sesiones en paralelo: 4 en `data/experiment/prompt_r2/p4/` (P4 de
U-PROMPT-R2) y `data/experiment/mantenimiento/freno_utabla_reproc.md` (U-TABLA-REPROC). Cada cifra de abajo lleva
su clave en la salida.

## 0. Diferencias entre el mandato y los archivos (regla d)

1. Las líneas de `ensamblar_tanda0.py` que cita el CONTEXTO (`:813`, `:824`, `:825`) son las de `f87ec4a`, anterior a
   C2. En `9f6361e` son `:935` (`catalogo_r2()`), `:955` (`resolver_relaciones_r2`) y `:956` (`SUJETOS_R2_SET` a
   E2). `:587` no cambió.
2. Control de R2.3, «los ensamblados sellados se reproducen con el catálogo vigente». Con el código de HEAD, la cadena
   r2a da `70d51e42…` (diez) y `fa4c1043…` (desarrollo): `camino_b.*.b0_igual_a_la_cadena_de_head` = true,
   `b0_igual_al_kg_en_disco` = false. Los sellados `99fe2bfa…` y `93a7af72…` se reproducen desde `f8dedd4`
   (asiento `bb472b1`). Propongo leer el control así: con el catálogo vigente, el script reproduce byte a byte la
   cadena de HEAD, y los sellados se citan con `f8dedd4`.
3. «integrantes de la Alta Gerencia» no pide un id nuevo. `Sujeto_alta_gerencia` existe (label «Alta Gerencia», sin
   alias, en el bloque del prefijo). La mención no resuelve porque no empieza con el label, y la regla del
   calificador exige que empiece. La operación que la resuelve es un alias. Un id nuevo duplicaría uno que ya existe.
   Para la prueba de R2 propongo «cuentacorrentista» como id agregado (T1) e «integrantes de la Alta Gerencia» como
   alias agregado (T2). El crecimiento necesita las dos operaciones.
4. Las cifras del registro que da el mandato se reproducen todas (`registro`): diez, 48 = 40 + 8; de las 40, 25
   exactas, 2 por tokens y 13 sin verificar. Desarrollo, 33 = 26 + 7; 16, 1 y 9. Las 66 filas en cuarentena de los dos
   registros tienen `sujeto_id_modelo` nulo (`cuarentena_con_sugerencia_del_modelo` = 0).

## 1. Inventario: qué lee el catálogo en cada paso (R1.1)

Hoy todo sale de un archivo, `catalogo_sujetos_r2.json` (`c3ad1581…`, `bd2122d`), vía `generar_desde_catalogo.py`.

| Paso | Lee | Dónde | Candado |
|---|---|---|---|
| Prefijo de E1 | `bloque_catalogo_r2.txt` | `prompt_r2b.py:57`, `:111` | `:65` (`c4005485…`); prefijo armado `:74-75` |
| Tool schema de E1 | `enums_tool_schema_r2.json` → `SujetoIdR2` → `pyd_r2/generados/tool_schema_r2.json` | `modelos_r2.py:62-63`, `:843`; `prompt_r2b.py:60`, `:123` | `modelos_r2.py:64-65` y `:90`; `prompt_r2b.py:68` (`0c391f2b…`); G9 de `selftest_pyd_r2` |
| Mensaje de E1 (línea de alcance) | `rol_por_to_r2.json` | `prompt_r2b.py:58`, `:124`, `:328-330`, `:356` | `:66` (`07cdb7af…`) |
| Perfil r2b (labels del E2 del perfil) | `labels_e2_r2.json` | `prompt_r2b.py:59`, `:125`, `:403`; `perfil_e1.py:237` | `prompt_r2b.py:67` |
| Manifiesto de corrida | `rol_alcance` de cada TO contra el `rol_por_to` del perfil | `manifiesto_corpus.py:140-187` | el de `rol_por_to_r2.json` |
| Validador r2 | `SUJETOS_R2_SET`: sugerencia y padre del modelo | `validador_r2.py:1143`, `:1154`; `modelos_r2.py:537-540` | `modelos_r2.py:80-91` (catálogo y enum) |
| E4, resolución por relación | `indice_e4_r2.json`, `rol_por_to_r2.json` | `r1_e4.py:522-541`; `ensamblar_tanda0.py:935`, `:955`; `runner_corpus.py:1110`, `:1114` | `manifest_generados_r2.json` contra `CATALOGO_R2_SHA256` (`r1_e4.py:528-534`) |
| E2 | `labels_e2_r2.json`; `SUJETOS_R2_SET` (rechazo `sujeto_id_fuera_de_catalogo`, `e2_lib.py:1053`) | `ensamblar_tanda0.py:956`; `runner_corpus.py:1116` | los dos de arriba |
| Merge cross-TO | `INV.SUJETOS_CATALOGO_SET` ← `SUJETOS_R2_SET` | `ensamblar_tanda0.py:587`; `r1_invariantes.py:100-101`, `:124` | `modelos_r2.py` |
| Esqueleto | `entrada_esqueleto_r2.json` (`C.CATALOGO_PATH` y `assemble.CATALOGO_PATH`) | `ensamblar_tanda0.py:585-586`; `assemble.py:118-186` | manifiesto de generados |
| Shapes r2 | `ids_s19_r2.json` (S19, S29); `entrada_esqueleto_r2.json` (S15) | `shapes_validator.py:215-217`, `:1395-1402`; sin opción de línea de comando (`:1461`) | `enums_r2.json`, `:220` (su `sujeto_id` no se usa, `:1100`) |
| Suite del perfil | `--catalogo catalogo_suite_r2.json`; LN-6: `indice_e4_r2.json`, `rol_por_to_r2.json` y el sha del JSON; LN-8: bloque contra JSON | `regression_kg.py:1745-1772`, `:1809-1830` | ninguno propio |
| Selftests | `reresolver_registro` | `selftest_r3.py:241`, `:245`, `:250`; `selftest_catalogo_unico.py:582` | — |

Con un solo archivo, cualquier alta cambia el request. Si genero los nueve archivos desde el catálogo de prueba
(T1 + T2), cambian ocho, entre ellos `bloque_catalogo_r2.txt` y `enums_tool_schema_r2.json`. Solo
`rol_por_to_r2.json` queda igual (`catalogo_prueba.un_solo_archivo_cambia`). Desde el catálogo del repo, los nueve
salen byte a byte iguales a los de `generados_r2/` (`generados_desde_el_request_iguales_al_repo`).

## 2. Dos catálogos (R1.2)

Sí se puede crecer sin cambiar el request: el crecimiento pasa de la clase F11 a la F13 de la tabla de
reprocesamiento (`tabla_reprocesamiento.md:94`, `:97`). La prueba b2 de abajo re-resuelve y rehace el grafo desde el
crudo guardado, sin abrir el request: con esta separación, la tesis puede afirmar que la re-resolución corre sin
re-extraer, sobre el catálogo de resolución.

- **Catálogo del request, fijo por release.** `catalogo_sujetos_r2.json` y lo que entra al request: el bloque, el
  enum y el tool schema, más `rol_por_to_r2.json` para los documentos que cubre la release (§4). Ningún candado
  existente cambia. `SUJETOS_R2_SET` conserva el sentido de «lo que el modelo pudo sugerir». Lo leen
  `validador_r2.py:1143` y `:1154`, `RelacionR2` (`modelos_r2.py:537-540`), `SujetoIdR2` (`:843`) y
  `perfil_e1.py:223`.
- **Catálogo de resolución, que crece entre tandas.** Es el del request más una lista de ampliaciones que solo
  agrega: `alta_id`, `alta_alias` y, si la autora lo aprueba (§4), `alta_alcance_de_resolucion`. Cada ampliación
  lleva su evidencia (claves del registro) y la aprobación de la autora. Propongo que la lista viva en
  `catalogo_unico/ampliaciones_resolucion_r2.json` y que se cree con el primer crecimiento aprobado, no en R2.
  - El catálogo compuesto se serializa como el del request: `json.dumps(indent=1, ensure_ascii=False)` reproduce
    el archivo del request byte a byte (`serializador_reproduce_el_archivo_del_request` = true). Sin ampliaciones,
    el compuesto ES el del request (sha `c3ad1581…`), y el grafo y el registro salen iguales por construcción.
  - Sus generados (índice de E4, labels, esqueleto, ids de S19, catálogo de la suite, `rol_por_to`) se arman con
    `generar_todo`, importado. El bloque y el enum se generan solo desde el del request.
  - El candado nuevo es el sha del catálogo del request (el de `modelos_r2`), el de la lista y el del compuesto. Va
    al manifiesto de los generados de resolución y al reporte del ensamblado.
- **Qué lee el conjunto de ids de resolución** (uno nuevo, no `SUJETOS_R2_SET`): el `sujetos_set` de E2
  (`ensamblar_tanda0.py:956`), `INV.SUJETOS_CATALOGO_SET` (`:587`), S19 y S29 de las shapes, y la suite. Medido con
  el catálogo de prueba sobre diez:
  - b1, con el catálogo de prueba solo en los generados de E4: E2 rechaza las 3 relaciones de T1
    (`sujeto_id_fuera_de_catalogo`). Salen del grafo (`b1_rechazos_e2`, `b1_contra_b0`) y, por código, sin fila en
    el registro, que solo recibe las relaciones sin resolver o resueltas a clase (`r1_e4.py:438-446`).
  - b2, con el catálogo de prueba también en los dos conjuntos: 0 rechazos, 0 elementos fuera del modelo r2, y la
    diferencia con b0 es exactamente la que se predice (`b2_contra_prediccion.no_explicado` vacío).
  - Por código, sin medición: un id nuevo que aparece en más de un TO y falta en el conjunto del merge se renombra
    con `__<to>` (`r1_invariantes.py:124`).
- **Cómo queda registrada la versión.** Lo medido: la arista que se muda cambia solo `target` y
  `metodo_resolucion` (`cuarentena` → `R1_alias_exacto`). Propongo G1, que no toca `modelos_r2`:
  - `resolucion_sujetos.jsonl`, una fila por relación, lleva en `catalogo_sha256` el sha del catálogo de resolución
    usado (sin ampliaciones, el mismo valor de hoy);
  - el registro guarda la historia (§3);
  - en `kg.json`, el nodo de un id nuevo lleva como procedencia del esqueleto la ampliación que lo dio de alta (el
    nodo de prueba tomó la suya de `provenance_esqueleto`);
  - el reporte del ensamblado lleva los tres sha.
  La alternativa G2 es una marca `ampliacion_catalogo` en las aristas de sujeto. Exige editar `AristaR2`,
  `MARCAS_ARISTA_R2` (`e2_lib.py:801-803`), el manifiesto de `pyd_r2/generados` y la constante de G9
  (`selftest_pyd_r2.py:94`). Además se pierde al fusionar aristas, porque las marcas las fija la primera relación.

## 3. El script y la verificación entre caminos (R1.3)

Medido con T1 + T2 sobre r2a:
- (a) `reresolver_registro`: 6 filas resuelven en diez (3 de T1, en `ctacte::9.2.1.1`, y 3 de T2, en
  `lingob::S3::chapeau_seccion`) y 0 en desarrollo. Es idempotente con el mismo índice.
- (a+), la regla de decisión re-aplicada a todas las relaciones de `resolucion_sujetos.jsonl`: reproduce la decisión
  guardada en 4.147 de 4.147 (diez) y 3.108 de 3.108 (desarrollo). Con el catálogo de prueba cambian 6, las 6 del
  registro: 0 fuera de él.
- (b) contra (a): diferencias del grafo, todas explicadas:
  - las 6 procedencias se mudan;
  - desaparecen los 2 nodos en cuarentena y sus 2 aristas `padre_sugerido`;
  - entran el nodo de T1 y su `subclase_de`;
  - `Sujeto_alta_gerencia` gana el alias y 1 procedencia.
  En desarrollo, solo el esqueleto: 1 nodo, 1 arista y el alias.

Tres huecos que el diseño tiene que cerrar, medidos:
1. **El registro de (b) no es igual a la salida de (a).** (b) rehace el registro desde cero: 42 filas, sin las 6 que
   resolvieron, y pone el sha nuevo en `catalogo_sha256` de las 42. (a) da 48 filas, con las 6 en `resuelto`, y
   conserva el sha de origen. Las 42 comunes son iguales salvo los dos campos de versión
   (`registro_b2_contra_a`). Propuesta: el registro es acumulativo. `catalogo_sha256` es la versión con la que la
   fila entró y no cambia; `catalogo_sha256_resolucion` es la versión con la que resolvió. El script escribe el
   registro anterior actualizado por (a), más las filas que (b) agregue (por ejemplo, una clave que pasa a ambigua).
   Controla tres cosas:
   - las filas sin resolver de ese registro son iguales a las de (b), salvo la versión;
   - el destino de cada fila resuelta es el de su relación en el `resolucion_sujetos` de (b);
   - (b) no tiene filas fuera del registro anterior, o se listan y se leen.
   `id_nodo` conserva el nodo en cuarentena que tuvo la fila. S28 no se afecta, porque coteja nodos contra filas y
   no al revés (`propuestos_en_grafo_sin_fila` y `cuarentena_sin_nodo` en 0, en b2).
2. **El método no se escribe igual.** `reresolver_registro` escribe `R1` y la cadena escribe `R1_alias_exacto`: 6 de
   6 difieren. Propongo alinearlo en `r1_e4.py:484-486`.
3. **(a) solo mira la cuarentena.** Una ampliación también puede:
   - mudar relaciones que resolvió el modelo, cuando la mención verificada coincide con el label o el alias nuevo
     (R1 gana, L-ESQ-R2 §3.3, punto 5);
   - cambiar filas `resuelto_a_clase` (calificador);
   - volver ambigua una clave.
   El script suma (a+) y el control de claves del índice (`indice_claves_que_pasan_a_ambiguas` y
   `indice_claves_que_cambian_de_id`, 0 y 0 con T1 + T2). Lo que explica cada camino va en columnas
   separadas, y lo que ninguno explica frena.

Además, el script corre LN-6, las shapes r2 y la suite del perfil con los generados de resolución. Las shapes se
importan sin editarse: `evaluar_perfil_r2` ya recibe `ids_s19_ruta` y `excepciones_ruta`. LN-6 lee rutas fijas
(`regression_kg.py:1758-1765`) y necesita una opción. LN-8 sigue sobre el request.

## 4. Alcance de los documentos nuevos (nota del 04/10/2026, punto a)

- **`rol_por_to_r2.json` se separa por documento, no por archivo.**
  - El alcance de un documento entra a su request desde la primera extracción y queda fijo para ese documento.
  - Las entradas de clase de los documentos nuevos (paso de lectura antes de cada tanda) no van a
    `catalogo_sujetos_r2.json`, porque romperían `modelos_r2.py:64` y `prompt_r2b.py:66`. Van a un registro de
    alcance por tanda que solo agrega. El mensaje y R3 lo leen junto con el de la release, con un control: el
    mensaje de toda unidad ya extraída sale byte a byte igual, así que su clave de caché no cambia.
  - Esto toca `prompt_r2b.py` (candados de E1), que está fuera de esta unidad. Va con la enmienda del protocolo.
  - Lo que se usó queda en dos lugares. Para la extracción, en el manifiesto de la tanda (su `rol_alcance` ya se
    controla contra el perfil, `manifiesto_corpus.py:162-187`) y en el request guardado. Para la resolución, en el
    sha del catálogo de resolución. Propongo que el reporte del ensamblado muestre las dos por TO y marque si
    difieren.
- **Alcance de la tanda 0** (`alcance`): 71 entradas, 35 con rol y 36 con clase. En la tanda 0, 6 TOs tienen rol, 3
  tienen clase y docvig no tiene.
- **docvig, 31 unidades.**
  - Si recibe alcance después de extraído, hay dos caminos: (i) re-extraer sus 31 unidades (fila F12, E1 y E3, con
    costo de API); (ii) alcance solo de resolución, que R3 aplica en código a sus menciones colectivas guardadas, sin
    re-extraer, aunque el modelo las sugirió sin ver el alcance.
  - Hay además una ventana: U-REEXT-T0 (borrador) re-extrae docvig con el prefijo r2b. Un alcance de clase decidido
    antes de su extracción entra sin extracción adicional, pero cambia el catálogo del request, es decir, es un
    cambio de release.
  - Decide la autora.

## 5. Colectivo sin alcance (nota del 04/10/2026, decisión 2)

- **Diseño.** En `resolver_relaciones_r2`, antes de `elif modelo:` (`r1_e4.py:418`), entra una rama nueva. Si la
  regla devolvió el motivo `colectivo_sin_sujeto_por_defecto` (`:377`, el TO no tiene alcance), la sugerencia no se
  aplica: la fila va a cuarentena con ese motivo y guarda `sujeto_id_modelo` (el registro ya lo guarda, `:451`).
  Cuando el documento recibe alcance, `reresolver_registro` la resuelve por R3 sin cambios.
- **Restricción para el crecimiento.** Ningún label ni alias puede igualar una expresión colectiva, porque R1 se
  evalúa antes. Hoy no hay ninguna clave «entidad», «entidades» ni «sujetos obligados». La clave
  singularizada «sujeto obligado» es ambigua y no resuelve: la comparten `Sujeto_rol_sujeto_obligado_proteccion` y
  `Sujeto_rol_alcance_rmrtsd`, los dos con label «Sujetos obligados (…)».
- **Qué cuenta como colectivo.** La lista de R3 (`r1_e4.py:306`) cubre 231 de las 1.088 apariciones de una forma
  colectiva en el texto propio de E0 de los diez TOs (`colectivos`). Dejé fuera las formas seguidas de
  «financiera(s)» o «cambiaria(s)», que nombran una clase. Lo que la lista no cubre son sobre todo singulares:
  «la entidad» aparece 806 veces y «el sujeto obligado», 33. Es una aproximación por texto, no una medición de
  menciones.
  - Recomiendo una sola lista para R3 y para la regla nueva, con el singular y con «cada», «esta(s)», «dicha(s)» y
    «tal(es)». Dejaría fuera «restantes» y «demás», que nombran una parte del colectivo.
  - L-ESQ-R2 ya prevé ampliar la lista con las menciones de r2b (`4ef7650:593-594`, decisión del 30/09): la lista
    se fija con U-REEXT-T0.
  - Ampliarla cambia R3 también en los TOs con alcance. Es un cambio declarado.
- **docvig en r2a.** Cambiarían 0 filas, por construcción: sus 17 relaciones resueltas por el modelo no traen
  mención, y las 3 con mención ya están en cuarentena (`docvig`). Como cota por texto, 5 de esas 17 están en una
  unidad cuyo texto propio dice «las entidades» (`docvig::3.4`; el modelo sugirió `Sujeto_entidad_financiera` 4
  veces y `Sujeto_cliente` 1). Además, el modelo sugirió 3 veces `Sujeto_rol_alcance_lavdin`, el rol de otro TO. La
  cifra real sale de U-REEXT-T0.
- **Firma.** Toca L-ESQ-R2 §3.2 y §3.3: va por enmienda firmada antes de implementarse, fuera de R2.
- **Volumen en el escalado.** En la tanda 0, la regla actúa solo sobre docvig. En el escalado actuaría sobre los 86
  documentos sin alcance: todas sus menciones colectivas irían a cuarentena, con un nodo por TO, porque el merge
  renombra los propuestos repetidos.

## 6. Regla de crecimiento (nota del 04/10/2026, punto b)

- **Registro de r2a, diez** (`frecuencias`): 27 filas en cuarentena con la mención verificada, en 18 claves. Ninguna aparece
  en 2 TOs. Solo «inversor» y «originante/fiduciario» llegan a 2 unidades, ambas en cap. «cuentacorrentista» e
  «integrantes de la Alta Gerencia» tienen 3 filas cada una, pero en 1 unidad. La cuarentena de r2a sale de
  `sujeto_propuesto` (62 menciones en 4.147 relaciones), así que no representa a r2b.
- **Propuesta.** Una clave es candidata cuando su mención verificada está en cuarentena en al menos 2 unidades
  distintas del registro acumulado. Con r2a, eso da 2 claves; con 3 unidades, 0. Es el criterio de admisión
  «anclaje textual + población» (`docs/esquema_v2_diseño.md:348`, citado en L-ESQ-R2 `:861`).
  - Las candidatas se leen (lectura asistida, declarada, con revisión de la autora, como `categoria_no_mapeo`).
  - Cada una entra, con aprobación de la autora, como alias de un id existente o como id nuevo con su padre.
  - Por debajo del umbral, una clave entra solo por decisión expresa y declarada de la autora.
  - El número y un techo de lectura por tanda se fijan con el registro de U-REEXT-T0, antes del primer
    crecimiento.
- **Convivencia con L-ESQ-R2 §7** (`4ef7650:862-864`):
  - lo agregado solo al catálogo de resolución actúa por las reglas sobre la mención guardada, y el modelo no lo
    sugiere;
  - alcanza la cuarentena con mención verificada y las relaciones del modelo con mención exacta (R1). Estas se
    cuentan aparte, como reasignadas;
  - una mención no verificada nunca resuelve por crecimiento: son 13 de las 40 filas en cuarentena de diez;
  - en la release siguiente, las ampliaciones pasan al catálogo del request (F11, dentro de la release) y la lista
    vuelve a cero.
- **Fuera del diseño.** El retiro de un id «en la resolución en código» que prevé L-ESQ-R2 (`4ef7650:585-586`) no es
  aditivo. Si la tanda 1 lo pide, es otra operación que hay que diseñar.

## 7. Escrituras que pide R2 (las aprueba la autora en el «seguí»)

En `data/experiment/reresolucion_catalogo/`:
- el script `reresolver_catalogo.py`: compone y genera; corre (a), (a+) y (b); contrasta; escribe el ensamblado y
  el registro acumulado; corre LN-6, las shapes y la suite;
- su selftest, con casos sintéticos y los controles de R2.3;
- el procedimiento (una página);
- `freno_r2.md` y `salidas/`.

Fuera del directorio, a aprobar una por una:
- **W1.** `tanda0/code/ensamblar_tanda0.py`: el catálogo de resolución como parámetro opcional de
  `plan_redirecciones_r2`, `correr_cadena_r2` y `ensamblar_manifiesto_r2`, más su opción de línea de comando. Sin el
  parámetro, la salida es byte a byte la de hoy (cadenas r2a `70d51e42…` y `fa4c1043…`). La alternativa es no
  editar y que el script sustituya en memoria lo mismo que la prueba b2. Así, el ensamblado normal no ve el
  crecimiento.
- **W2.** `corpus_v2/r1_e4.py`: el nombre del método en `reresolver_registro` (§3, hueco 2) y el cargador del
  catálogo de resolución junto a `catalogo_r2()`. El cargador puede vivir en el script.
- **W3.** `scripts/regression_kg.py`: una opción para que LN-6 lea los generados de resolución. Sin ella, se
  comporta como hoy.

No van en R2: la regla del colectivo sin alcance (§5, enmienda a L-ESQ-R2), el alcance por documento en el mensaje
(§4, `prompt_r2b.py`), la ampliación de la lista de R3 (con U-REEXT-T0) y G2.

## 8. Cierre de R1

- **Escrituras de R1.** En el repo, solo `data/experiment/reresolucion_catalogo/`: `r1_medicion.py`,
  `salidas/r1_medicion.json` y este archivo. Fuera del repo, la copia y el paquete de la revisión, en el scratchpad.
- **Grep de convenciones** sobre `data/experiment/reresolucion_catalogo/`, corrido antes de escribir esta sección:
  - nombres propios conocidos del proyecto, «mentor», «tutor», «profesor», «reunión», «slack», «mail», «correo» y
    «whatsapp» (los nombres no se transcriben): vacío (exit 1);
  - primera persona del plural («nosotros», «hicimos», «tenemos», «nuestro/a», «decidimos», «corrimos», «vamos a»,
    «encontramos», «medimos», «proponemos»): vacío (exit 1);
  - origen conversacional («como dijo», «según dijo/pidió», «pedido por», «me/nos pidió»): vacío (exit 1).
- **Commit.** PENDIENTE de la autora.
