# U-R2-CODIGO — FRENO R3 (con los ajustes K, L y M)

Fecha: 02/10/2026. Sin commit: los commits son de la autora (commit PENDIENTE). USD 0: ninguna llamada a la
API, Neo4j no se usó. Fuentes firmadas leídas en su commit: mandato `c60e89c` (sha256 `3c613315…`),
enmienda 1 al mandato y enmienda 2 de L-ESQ-R2 en `5f9a731` (`dcd0886c…`, `e779bd70…`), L-ESQ-R2 en `4ef7650`
(`66c4a1b9…`) con las dos notas posteriores a la firma del archivo actual.

Toda cifra sale de un artefacto de esta unidad o de un comando del §7. Los artefactos extensos están en el
paquete de revisión (`revision_UR2CODIGO_R3/`, fuera del repo).

## 1. Ajustes K, L y M

**K (regla aprobada, solo en e0-r2).** `e0_lib.titulos_mayusculas_repetidos` y `separar_encabezado_pie(...,
mayusculas_repetidas=)`; `correr_e0.lineas_conservadas_k` y `encabezados_conservados.json`.
- Tanda 0: se conservan exactamente las 5 líneas medidas; `pro::3.1.3` queda como caso negativo
  (`selftest_e0r2.py`, S11; 31/31).
- E0 legada 34/34 idéntica a `salida_tanda0`; e0-r2 doble corrida idéntica (47 archivos).
- V4 sin fallas, con tres chunks iguales salvo las líneas conservadas: `cap::2.12.2.6`, `ext::7.1.1.3` y `ric::S2`
  (`r1c_censo_serializacion.json`, `v4_iguales_salvo_lineas_conservadas_k`). `cap::2.12.2.6` aparece porque
  su tabla incluye la línea conservada entre sus líneas de E0; su bloque no cambia.
- Censo R1.d recomputado: 39 requests cambian (ric 21, cap 16, ext 2), USD 0,6474 (`r1d_censo_requests.json`).
- **Censo fuera de muestra** (`rk_fuera_de_muestra.json`): los 152 PDFs de `escalado_prep/pdfs` (`ls … | wc -l`)
  menos los 5 de la tanda 0 que están ahí y los dos de más de 300 páginas (`manual`, `ri2_pm`): 145 TOs. 218 líneas
  conservadas en 27 TOs; lectura (mía, sin revisión de la autora): 184 contenido, 34 encabezado de página. TOs con
  una sola página de cuerpo: `micemp` y `verac`.
- **Hallazgo: arrastre.** El recorrido de la zona de encabezado se detiene en la primera línea que queda
  (`e0_lib.py`, rama `else: break` de `separar_encabezado_pie`). Si esa línea es un título del TO partido distinto
  en esa página, las siguientes de la zona, «B.C.R.A.» y la línea de sección incluidas, quedan como contenido:
  17 de las 34 líneas de encabezado son arrastre, y en 7 páginas la línea «Sección N.» queda en el cuerpo
  (`adrei` p17, `cryl` p12 y p16, `lingeef` p43, `ri_ai` p7, `rmrtsd` p6, `snp_cheq` p23). En la tanda 0 no
  ocurre. Corregí el docstring de `titulos_mayusculas_repetidos`, que decía que esas ramas no cambiaban.
  Alternativa a decisión, no implementada: tratar como encabezado todo lo que precede a la última línea
  «B.C.R.A.» o de sección dentro de la zona, y aplicar la regla de repetición solo después.

**L (BKL-0037).** `e0_lib.desambiguar_ids`: conserva el id la aparición con más texto propio (empate: la
primera); las demás reciben `::rep<k>` en orden documental, con `id_e0_original`.
- Sobre la partición: en 69 de 69 el id queda en el chunk más largo (`selftest_r2.py`, A4/A4b; 18/18).
- `correr_e0 --version-e0 e0-r2` sobre adfsp, ceninf, cirmo3 y ri_niif, en el scratchpad: reproduce las colisiones
  de adfsp (9) y cirmo3 (52); `ids_desambiguados.json` = {adfsp: 9, cirmo3: 52}. ceninf y ri_niif dan 0 chunks por
  el camino vigente de E0 (necesitan el modo sin raíz de B5.8.1): sus 8 colisiones no se reproducen así.
- **La causa sigue sin corregir:** el índice se lee como cuerpo. Quedan 69 chunks de índice en la partición (61
  en la corrida de adfsp y cirmo3), renombrados `::rep<k>`, no eliminados.

**M.** Con `--version-e0 e0-r2`, `correr_e0` exige `--salida` (argparse, salida 2) y se niega a escribir en
`salida`, `salida_enm01` y `salida_tanda0` antes de leer un PDF (`SALIDAS_PROTEGIDAS`; `selftest_e0r2.py`, S12).

## 2. R3.a — conexión del perfil r2

Contradicción con los archivos (regla d): el perfil de un manifiesto es de `perfil_e1.py`, y ni ese módulo ni
`manifiesto_corpus.py` están entre las escrituras autorizadas. El perfil r2 entra entonces como opción de los
dos programas, sobre el crudo del perfil de E1 del manifiesto:
- `runner_corpus.py --perfil-r2`: E1 y E3 no cambian (sus prompts sellados leen la validación del perfil de E1);
  además del E2 de siempre, `cerrar_e2_r2` arma la entrada de E2 del perfil r2 (`entrada_r2`: crudo del intento
  que E3 aceptó, del archivo compañero de R2 o, en corridas anteriores, de `e1_reintentos.db` por la clave
  reconstruida), la valida con `validador_r2` y la política r2, resuelve los sujetos, escribe el registro del TO y
  corre `e2_lib.ensamblar_r2`. Archivos propios: `extracciones_finales_r2_<to>.jsonl`, `grafo_r2_<to>.json`,
  `reporte_e2_r2_<to>.json`, `resolucion_sujetos.jsonl` y `no_mapeados_sujetos.jsonl`.
- `ensamblar_tanda0.py --perfil-r2 [--tablas-e0-r2 DIR]`: la cadena r2 completa en `<salida>/r2/`, sin la cadena
  r1 ni el E5.
- Candados (decisión 10): catálogo r2 por sha256 (`modelos_r2`) y los cuatro generados que usa la cadena
  contra `manifest_generados_r2.json` (`r1_e4.catalogo_r2`); política con el sha de 57a8dd2
  (`82e8752a…`, `r1_e4.POLITICA_R2_SHA256`).
- Con los perfiles existentes nada cambia: los tres ensamblados sellados se reproducen con el código nuevo
  (`r1/kg.json` = `eab2fdd0…`, `dd42d6d9…`, `4097d4fd…`; de 13 archivos por ensamblado, los mismos 3 que en
  R2 difieren solo por la raíz de las rutas). `ensamblar_r1.py` no se editó: llama a `detectar_y_resolver(kg)`
  con el valor por defecto (`r1_referencias.py:200`).

## 3. R3.b y R3.c — sujetos por relación y registro

- `r1_e4.resolver_relaciones_r2`: R1 (label o alias exacto) gana siempre; con R2, el calificador o R3 gana la
  sugerencia del modelo si la hay; sin regla, la sugerencia del modelo (R4). Siempre se registran los dos ids
  (`resolucion_sujetos.jsonl`: regla, id de la regla, sugerencia, resuelto, desacuerdo). La mención se lee sin su
  artículo inicial. R3: lista cerrada `entidades`, `sujetos obligados` (de `prompt_e1.py:110`). Calificador: la
  mención empieza con el label o alias de una clase y sigue con texto → la clase, y el calificador queda en la
  resolución y en el registro como candidato (estado `resuelto_a_clase`).
- Registro (P-d1, P-d2): una fila por relación sin resolver, por TO y por ensamblado; E2 crea los
  `Sujeto_propuesto` desde el registro y la fila recibe el id del nodo.
- Re-resolución (P-d3): `r1_e4.reresolver_registro`, idempotente; con el mismo índice no resuelve nada y con un
  id nuevo resuelve la fila con el sha nuevo (`selftest_r3.py`, T4).
- **E4 posterior a la fusión, propuesta: retirar la pasada residual de propuestos** en el perfil r2 y dejar en
  E4 solo la canonización del TextoOrdenado y el filtro de conflictos. Evidencia: la pasada residual corre
  `resolver_label` sobre el label del propuesto, que es la mención, con el mismo índice que ya aplicó la
  resolución por relación, que además tiene el calificador y R3; en la prueba de cla, 1 propuesto y 0
  resoluciones (`e4_pasada_residual_medida.json`). La cadena la mide y no la aplica. Un catálogo nuevo se aplica
  por la re-resolución, no por E4.

## 4. R3.d — remite_a (con la enmienda 1)

- `r1_referencias.detectar_y_resolver(kg, perfil="r2")` → `detectar_y_resolver_r2`: siete tipos de origen,
  `termino`, detección sobre el texto de E0 del punto de cada procedencia (por `chunk_id`), con el corte de
  palabra al final de línea unido (`normalizar_e0`) y la evidencia mapeada al texto original
  (`evidencia_literal`), atribución D1, `alcance`/`destino`/`evidencia`, sin `rol_fuente`, `clase` ni `via`. Sin
  perfil, la cadena r1 sin cambios.
- Unir el corte de palabra fue necesario: sin eso, `cap::8.2.3.3` («de las nor-\nmas sobre “Clasificación de
  deudores”») seguía dando la remisión interna falsa.
- Variantes `::rep<k>`: la cita se resuelve al canónico; si más de una variante tiene texto de cuerpo, «destino
  ambiguo», sin arista, contada. Criterio declarado (`tiene_texto_de_cuerpo`): quitando cada rótulo de unidad y
  la línea que lo sigue, queda alguna línea con texto. Probado con casos sintéticos (`selftest_r3.py`, T1); en la
  tanda 0 no hay ids repetidos.
- Controles sobre los grafos sellados (`r3d_remisiones.json`):

| control | resultado |
|---|---|
| simulación de U-AUDIT-TIPOS-V3 (desarrollo): con 4 tipos, pares = 4.242 sellados | sí |
| con los 7 tipos: agregados / perdidos | +3.687 / 0 |
| pasos: `termino` / cada procedencia / texto de E0 con D1 | +0 / +11 / +4.383 y −656 pares |
| `cla::5.1.1.1` → `cla::3.7` (desarrollo, diez, r1), interna, evidencia con «punto 3.7» | sí, sí, sí |
| `cap::8.2.3.3` → `cla::6.5.1` y `cla::7.2.1` (desarrollo y diez), sin `cap::6.5.1` | sí |
| diez, 4 tipos y procedencia primaria: pares solo paráfrasis / solo E0 / ambos | 61 / 1.178 / 824 (707 orígenes cambian) |
| alcance de lo sellado con la regla nueva: r1, desarrollo, diez | 5.456/183/6; 4.118/120/4; 4.631/174/14 |
| clase externa que queda interna (r1) | `cap::1.4` 1, `cap::S2` 4 |
| 35 Condicion aisladas (desarrollo) con alguna remisión | 9 |
| los seis puntos de ext como procedencia de alguna cita (r1) | 6 de 6 |

- Atribución D1 (desarrollo): 923 menciones a los nodos que contienen la unidad, 155 a todos los nodos del
  punto. Citas resueltas (chunk, tramo, unidad citada): 1.093; por alcance 1.039 interna, 46 externa, 8
  to_entero; irresolubles 342 (norma fuera del inventario 134, punto sin nodos 171, punto inexistente en E0 28,
  autorreferencia 9). Aristas 11.667 (10.834 interna, 824 externa, 9 to_entero). Las firmas, en el JSON.
- Citas a Comunicaciones (registro sin arista; diez): 32 citas, 19 chunks, 15 Comunicaciones. Pies que E0 no
  recortó: `ctacte::6.1.2.3` (A 3244) y `ric::11.1.1` y `ric::11.1.4` (A 6561); la línea «Comunicación “C” 81129»
  de esos dos chunks de ric, debajo del pie, es probable resto de pie: NO VERIFICADO contra el PDF. El conteo
  preliminar de la enmienda 2 (31/19/14) queda reemplazado.

## 5. R3.e a R3.h

- **establecida_en derivada:** `derivar_establecida_en`, hacia el TextoOrdenado de cada TO de la procedencia,
  con `rol_fuente = derivada_de_procedencia`. Cla: 23 aristas (13 Operacion, 10 Condicion); 0 nodos de contenido
  sin `establecida_en`. Aislados que quedan: 12 roles del catálogo r2 sin miembros (`sin_miembro_adjudicable`).
- **Umbrales, par B:** `llenar_umbrales_r2` con `reglas_comparacion.analizar` de U-PYD sobre la descripción y los
  `campos_heredados_v3`; el tramo del elemento es la cuantía tal como está en esa fuente, verificada contra el
  texto de E0 de los chunks del nodo y, con `--tablas-e0-r2`, contra las celdas de las tablas de R1. Base por
  remisiones o por `termino` de una Definicion del mismo TO; si no, marca `base_no_resuelta`. El plazo heredado
  sin cuantía temporal va a `frecuencia`, con marca si no está en la lista. Cla: 99 elementos en 86 nodos; base
  resuelta 7, no resuelta 34; 17 plazos a frecuencia, 16 fuera de lista (casi ninguno es una frecuencia:
  «inmediata», «N/A», «previo a…»); rangos con la unidad repetida: 0.
- **Matriz ampliada:** E2 conserva `no_verificada_e3`; en cla, 50 (32 → Operacion, 18 → Potestad), contadas aparte.
- **Cómo muestra el agente la lista** (`r3h_lectura_umbrales.json`, en memoria, sin editar nada): `ver_nodo` del
  harness la devuelve en `properties`; la carga a Neo4j la guarda solo en `props_json` y `Neo4jIndex.ver_nodo`
  (y `ver_nodo_v2` de tools_v2) la devuelve igual; `umbrales` no es propiedad del nodo de Neo4j y el resumen de
  `buscar_nodos` muestra solo la descripción.

## 6. Modelo r2, brechas y corrida de prueba

- `modelos_r2.py`: `PREDICADOS_DERIVADOS`, `FIRMAS_DERIVADAS` (56), `ALCANCE_REMISION` e invariantes de
  `remite_a` en `AristaR2`. `selftest_pyd_r2.py` 273/273 (los 249 previos y 24 de G11). Tool schema y enums
  regenerados byte a byte iguales a 57a8dd2; política con el sha de la decisión 10.
- **Contradicción:** el caso de G9 «manifest: sha256 de la política y de modelos_r2 vigentes» compara el sha de
  `modelos_r2.py` del manifiesto generado con el del archivo; cualquier cambio autorizado del archivo lo rompe, y
  regenerar `pyd_r2/generados/` no está autorizado. Lo reformulé: compara con el sha de la generación
  (`43ae09fb…`, 57a8dd2), y G11 prueba que lo generado no cambia. Alternativa: autorizar la regeneración.
- **Brechas del modelo del grafo r2** (solo `remite_a` estaba autorizado en `modelos_r2.py`): base resuelta y
  verificación en tabla del elemento de umbral → `umbrales_r2.jsonl`; cola humana, colisión cross-TO y
  variantes del TextoOrdenado → `marcas_r2.json`; calificador del sujeto → `resolucion_sujetos.jsonl`; las
  aristas de esqueleto (`subclase_de`, `miembro_de`, `instancia_de`, `parte_de`) no están en `AristaR2` y se
  cuentan aparte.
- **Corrida de prueba sobre cla** (en el scratchpad): 595 nodos, 1.127 aristas, doble corrida idéntica, 0
  inválidos contra `NodoR2`/`AristaR2` (126 de esqueleto fuera del modelo). Casos de control:
  - las dos `condicion_de` Condicion → Operacion de `cla::5.1.1.1`, con `no_verificada_e3`;
  - `remite_a` desde los nodos de `cla::5.1.1.1` hacia la Definicion de `cla::3.7`, `alcance = interna`,
    `destino = cla::3.7`, evidencia «…establecido en el punto 3.7. …» (criterio §9 de la enmienda 2);
  - el elemento mínimo estricto, valor 2, unidad «veces», base «importe de referencia establecido en el punto
    3.7» resuelta a `cla::3.7` (`umbrales_r2.jsonl`);
  - sujeto: 183 relaciones, 182 por la sugerencia del modelo y 1 en cuarentena con su fila en el registro (motivo
    `sin_match`, «administradores de las carteras crediticias»); 0 desacuerdos (el crudo v3 no trae menciones
    fuera de `sujeto_propuesto`).
  - remite_a en cla: 29 citas resueltas (28 interna, 1 to_entero), 175 aristas (173 interna, 2 to_entero); 38
    de 40 irresolubles son normas fuera del inventario de esta prueba de un solo TO; Comunicaciones: 0.
  - 0 `referencia` con origen distinto de TextoOrdenado.

Los archivos de la corrida de prueba (kg, reporte, registro, resolución, remisiones, umbrales, marcas, E4) están
en el paquete con el sufijo `_prueba_cla_R3`; no se copian al repo porque llevan rutas del scratchpad.

## 7. Controles y doble corrida

- Ensamblados sellados con el código nuevo y los perfiles existentes (espejo en el scratchpad): `r1/kg.json`
  idéntico en los tres; los otros 3 archivos distintos de cada uno (`e5_esqueleto.json`,
  `reporte_ensamblado_r1.json`, `reporte_ensamblado.json`) difieren por la raíz de las rutas, como en R2.
- Runner: con `--stub`, los archivos del perfil de E1 son los mismos con y sin `--perfil-r2` (el reporte de E2,
  salvo la ruta); con la opción se escriben además los del perfil r2.
- Doble corrida: e0-r2 (47 archivos), `r1c` y `r1d`, `rk_fuera_de_muestra`, `r3d_remisiones`, `r3h_lectura_umbrales`
  y la cadena r2 de cla (todos los archivos idénticos salvo `reporte_ensamblado_r2.json`, que lleva la ruta de
  `--salida` de cada corrida).
- Selftests en el repo: `selftest_r3` 46/46, `selftest_pyd_r2` 273/273, `selftest_r2` 18/18, `selftest_e0r2` 31/31,
  `selftest_dirigida_tanda0` 28/28, `selftest_clave_cache` OK, `selftest_regression_kg` 85/85. En el espejo, con el
  código nuevo y con el de HEAD, los mismos resultados: E0 (57, 39, 34, 59, 33), U-B5.3 40/40, cable v3 45/45,
  corpus 21/21, E2 35/35; `selftest_manifiesto` 32/37 (P5, ruta absoluta en `reporte_e2`, conocido) y
  `selftest_dirigida_tanda0` 27/28 (A14, guarda de ruta: en el espejo los directorios son enlaces al repo; en el
  repo da 28/28) en los dos.
- Sin `.pyc` ni `__pycache__` nuevos respecto de la línea de base de R2.

## 8. Comandos

Espejo y batería: `hacer_espejo.sh`, `control_klm.sh` y `control_r3.sh` (paquete). Selftests: `selftest_r3.py`,
`selftest_pyd_r2.py`, `selftest_r2.py`, `selftest_e0r2.py`. Controles: `r3d_remisiones.py --out`,
`r3h_lectura_umbrales.py --kg --nodo --out`, `rk_fuera_de_muestra.py --max-paginas 300 --out`,
`ensamblar_tanda0.py --manifiesto … --entrada … --salida … --perfil-r2 --tablas-e0-r2 …`.
