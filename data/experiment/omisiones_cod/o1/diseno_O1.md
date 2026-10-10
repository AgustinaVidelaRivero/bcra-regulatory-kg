# U-OMISIONES-COD, O1 — diseño de cada cambio y de su selftest (09/10/2026)

Mandato firmado en `c90d3d9` (v7), con las dos notas al pie de `c52255f`; texto firmado `6c8914a0…`, verificado en los dos commits
y en HEAD. USD 0, sin API. Todo corrió sobre dos copias del repo sin `.git` ni `.venv` y sin enlaces: `copia` (el código de HEAD)
y `copia_o2` (el código de este diseño). El código vive en los parches de `parche/` (un diff por archivo, y el completo); al repo
entra en O2. Las cifras salen de `salidas/` y cada una dice qué script la produce.

**Línea de base.** El código de HEAD no reproduce `a9631a64` sino `40c54830` (diez) y `8d747e57` (sin cola): es el cambio de R2-3
de U-RERESOL-CAT (`803623a`), sin re-sellar. La diferencia es 1 nodo (`Sujeto_propuesto_las_entidades`), 4 `aplica_a` de docvig que
pasan a ese propuesto y 1 `padre_sugerido` (`salidas/diff_a9631a64_vs_head_diez.json`; sin cola, `diff_e22fae1a_vs_head_sincola.json`). Las omisiones, las remisiones, las
comunicaciones y los umbrales son byte a byte los de `a9631a64`. Por eso mido cada grupo contra el grafo de HEAD y doy la cifra de
la v7 sobre `a9631a64` donde difiere.

**Corrida por etapas** (`scripts/cadenas_base_head.sh`, la cadena r2b de diez con y sin cola; cada etapa suma un grupo al
anterior): HEAD `40c54830`/`8d747e57` → B `1bb1205a`/`4e579e42` → B+C+L `422f4bac`/`c5660864` → +G-r `dff28f12` (diez) → +H
`912ee95c` (diez) → completa (J, A, h, K) `6be0a6b2`/`6f3d5c7e`. La diferencia de cada etapa con la anterior es la de
su grupo (`salidas/diff_*.json`). La corrida completa, repetida en otro proceso, da los mismos archivos (el reporte, igual salvo las
rutas de salida de `redirecciones`). Doble corrida interna byte a byte en todas.

---

## Grupo A — registro de omisiones (sin cambios en `kg.json`)

**Dónde.** `ensamblar_tanda0.py`, cadena r2 con la fase r2b, donde hoy se arma `omisiones.jsonl` (punto p de U-R2-CODIGO-2). Las
marcas van en las filas de `omisiones.jsonl` y en el resumen `omisiones` del reporte; (d) va a un registro propio,
`supuestos_en_norma.jsonl`, con su resumen. Funciones: `marcar_omision`, `donde_tramo_omision`, `supuestos_en_norma`.

- **(a) `tramo_en_heredado`.** Reproduce, sin el registro, la ubicación que `validador_r2.verificar_tramo_omision` ya cuenta
  (primero el texto propio; si no, el completo; en un mini-chunk a mitad de oración, el orden de lectura), con el tramo que vio el
  validador (`tramo_modelo` si el guardado es el literal). Marca «heredado»; el «orden de lectura» se cuenta aparte y no se marca.
  El reporte da la pérdida propia por categoría sin las marcadas.
- **(b) `revisar`.** En `meta_normativo`: los motivos `contador:<clase>` (`validador_r2.marcas_meta_normativo`, sobre el mismo
  tramo) y `recomendacion:<patrón>` (lista cerrada RECOMENDACION_OMISION: cópula + «deseable/conveniente/recomendable/aconsejable»,
  «se recomienda/aconseja/sugiere», «debería(n)», «buena(s) práctica(s)»; decisión 3 de la autora sobre el FRENO T4).
- **(c) `texto_propio_entero`.** El tramo cubre todo el texto propio, sin la numeración inicial (secuencia de tokens de R-NORM
  igual). Una sola marca, en cualquier categoría, con dos atributos descriptivos: `es_item` y `con_extraccion`. Los dos ejemplos de
  la v7 son ítems con extracción, así que «unidad entera» e «ítem» no se separan por esas propiedades: los dos llevan la misma marca.
- **(d) `supuesto_en_norma`.** Entidad de contenido no Condicion (Obligacion, Restriccion, Potestad, Excepcion, Operacion,
  Definicion) cuya descripción o tramo (`provenance.tramo`) lleva un conector condicional de la lista cerrada CONECTORES_SUPUESTO
  (cuando, siempre que, en tanto, mientras, en la medida que, en caso de, a condición de, de no, si). Mide y no corrige.
- **(e) clasificador de la copia de la nota de E3.** Ver abajo; no entra al código de O2 hasta que la lectura apruebe su precisión.

**Selftest (prototipo verificado en `salidas/casos_v7.json`, 58/58).** (a) positivo, una omisión de T4 con el tramo en el
heredado (`ctacte::3.2.1.2`); negativo, una con el tramo propio (`ric::4.1.1.5`). (b) positivo, una con marca del contador
(`ext::13.3.9`); negativo, una sin marca ni recomendación (`ric::4.1.1.5`). (c) positivos `ext::5.8.2.2` y `ctacte::2.1.1.4`;
negativo `pro::1.1.1` (una omisión entre nodos extraídos). (d) positivo `ext::10.5.5.2` e7 Obligacion (supuesto de T4 dentro de la
norma); negativo `ext::10.5.5.2` e2, una Condicion con su relación. En O2 van como casos de un selftest del ensamblado, con
sintéticos para cada regex y el control de que `omisiones.jsonl` solo agrega claves.

### (e) El clasificador de `copia_nota_e3`

**Hallazgo de diseño.** En diez, la marca del ratchet (`ratchet_e3.copias_nota`, ventana de 5 tokens) aparece solo en las 64
unidades que leyó T4: T4 leyó todas. Un clasificador que solo filtre la marca no tiene ninguna detección fuera de esas 64, y la
lectura decidida (30 fuera de las 64) quedaría vacía. Por eso el clasificador mira toda la población que pudo copiar la nota.

**Población.** Las entidades de la extracción final de las unidades `aceptado_tras_reintento` (216 en diez: 64 con la marca, 152
sin ella). Son las únicas extracciones del grafo escritas después de leer las notas: la cola humana entra con el crudo del primer
intento (`runner_corpus.entrada_r2`). Dos campos por entidad: descripción y etiqueta (2.133 campos).

**Regla elegida (`ventana3+flexion`).** Las ventanas de 3 tokens de R-NORM del campo que están en una nota del feedback (la
verificación anterior al último reintento) y no en el texto de la unidad ni en las citas de esos faltantes. Sobre las palabras de
esas ventanas: clase 1 si hay metalenguaje del verificador; clase 3 si hay una palabra de contenido ausente de la unidad que no es
una flexión de una palabra de la unidad (la ayuda de lectura de T4). Las listas VACIAS y METALENGUAJE se importan de la regla de
lectura de P3b-2. Código de diseño: `scripts/clasificador_copia_nota.py`; corrida: `scripts/medir_e.py`.

**Calibración sobre el conjunto de diseño** (los 86 casos de T4, ya leídos y adjudicados; `salidas/e_calibracion_T4.json`). No es
la medición de precisión de la v7, que se hace fuera de esas 64 unidades. Variantes:

| variante | sobre los 86 de T4 | copias reales cubiertas | detecciones en diez | fuera de las 64 |
|---|---|---|---|---|
| ventana 5 (marca + cotejo de T4) | 29/37 | 29/29 | 38 | 0 |
| ventana 5 + flexión | 26/26 | 26/29 | 27 | 0 |
| ventana 4 + flexión | 26/28 | 26/29 | 34 | 3 |
| **ventana 3 + flexión (elegida)** | **26/30** | **26/29** | **57** | **16 (15 unidades)** |
| palabra suelta | 29/55 | 29/29 | 358 | 218 |

La variante de 5 reproduce la referencia de T4 («29 de 37»). Elegí la de 3 con flexión: es la de mayor alcance con una precisión de
diseño igual a la de las variantes de 4 y 5 con flexión; la palabra suelta cae a 29/55. El filtro del primer intento (palabras que
el modelo ya escribió antes de la nota) no mejora la precisión de diseño y pierde copias reales; no entra.

**Consecuencia para la lectura decidida.** Fuera de las 64 hay 16 detecciones (< 30): por la nota del §6 se leen todas, con el
mismo piso de Wilson 0,75. Con n = 16, solo 16/16 da un límite inferior ≥ 0,75 (0,806); 15/16 da 0,717. Con menos de 12
detecciones el umbral sería inalcanzable aun sin errores. La decisión de despachar la lectura así es de la mesa y la autora.

**Lista sellada.** `salidas/e_lista_sellada/detecciones_e_copia_nota_diez.json`, sha256
`4c3855292349a75d675216fd7ae772a948777dd76e226eaa1f32bcf67cda3efd`, sellada el 09/10/2026 a las 16:59:27 (−0300)
(`salidas/e_lista_sellada/sello_lista_e.txt`); 57 filas (41 dentro y 16 fuera de las 64 unidades de T4), con chunk_id, TO, entidad, tipo, campo, texto,
palabras y ventanas. No la abrí: la escribió el script sin imprimir filas; una segunda corrida da el mismo sha256.

**Si entra (O2, solo con la lectura aprobada).** En el ensamblado, un registro `copias_nota_clasificadas.jsonl` y su resumen; no toca
`kg.json` ni la marca del ratchet.

---

## Grupo B — menciones de sujeto

- **f (`validador_r2.py`).** `verificar_tramo(…, contracciones=False)`: con `contracciones=True`, «del» → «de el» y «al» → «a el» en
  la mención y en el texto (cada parte conserva el span). Solo la llamada de la mención de sujeto (`:1250` de HEAD) pasa `True`: las
  demás verificaciones (tramos, omisiones, umbrales, términos) no cambian.
- **f′ (`r1_e4.py`, opción (ii)).** `EXPRESIONES_COLECTIVAS_R3` suma «entidad»; `EXPRESIONES_SINGULARES_R3 = ("entidad",)`. En
  `resolver_mencion_r2`, sin rol, el singular no toma el motivo `colectivo_sin_sujeto_por_defecto` y cae en `sin_match`: la parte A
  no lo alcanza. La lista también la lee `reresolver_catalogo.py:282`, que rechaza una ampliación del catálogo con label o alias
  colectivo: con el cambio, «entidad» queda rechazada también ahí (coherente con A.1.6); no regenero el catálogo.

**Selftest.** f: positivos «el cuentacorrentista» contra «Obligaciones del cuentacorrentista» y «el Comité de auditoría» contra «…
del Comité de auditoría» (verifican con `contracciones=True` y no sin él); negativo, una mención ausente sigue en «no». f′: positivos
`ext::7.9.4` (4 relaciones, al rol de exterior), `cap::6.7.2.2` (3, al rol de cap) y `ctacte::1.5.2.9` (1, a `Sujeto_banco`);
negativos por relación: `ext::4.4.2#8` («la/s entidad/es encargada/s…»), `ext::11.1.1.10#1`, `ext::7.3.7#6`, `ext::4.4.2#16` («la
mencionada entidad») y los sintéticos «la entidad financiera» (R1) y «esta entidad» (`sin_match`); opción (ii): en un documento sin
alcance, «la entidad» con sugerencia → R4, sin sugerencia → cuarentena `sin_match`, «las entidades» → cuarentena
`colectivo_sin_sujeto_por_defecto`. Todos pasan en `casos_v7.json`. **Precisión del negativo de la v7:** `ext::4.4.2` tiene cinco
relaciones en cuarentena; dos «la entidad» cambian (son de las 19) y el negativo es la relación 8.

---

## Grupo C — la base de los umbrales (`ensamblar_tanda0.py`, solo r2b)

- **g1** va en el ensamblado, antes de g, sobre los elementos del validador (no en `validador_r2.elemento_umbral_relativo`): así el
  validador cambia solo por f y H. `REGLAS_BASE_RELATIVA` son las reglas de U-DIAG-LIMITES en su orden
  (`UDIAGLIMITES_l1_clasificar_relativas.py`, sha256 `7ae07f52…`, leído en su paquete fuera del repo), sobre la base plegada; con
  fecha, periodicidad, cantidad o evento/plazo la base queda vacía, sin marca; el recorte que empieza mal la conserva.
- **g** (`_base_del_validador`): el elemento del límite relativo con base y sin destino ni marca pasa por `resolver_base` con el
  detector de `remite_a`, y escribe `base_destino`, `base_via` o `base_no_resuelta`. El reporte cuenta por origen
  (`base_por_origen`, `base_del_validador`, `base_no_resuelta_por_motivo`).
- **g2** (`resolver_base`, `puntos_citados_de_otra_norma`): la remisión a un punto N no resuelve si el texto de E0 de la unidad
  (propio y heredado de las unidades del nodo) cita ese N como «punto(s) N…» seguido, tras la enumeración, de «del TO sobre», «de
  las normas sobre», «del Texto Ordenado», «de la Ley», «del Decreto» o «de la Comunicación»; motivo `cita_a_otra_norma`.
- **g3**: con dos o más Definicion del mismo término en el TO, la vía definición no resuelve; motivo `definicion_homonima`.
  `ElementoUmbral` no cambia: los motivos van al reporte, no al elemento.

**Selftest.** g: positivos `ext::3.8`, `ext::14.2.2`, `ext::3.18.3`; negativo `cla::6.5::intro`. g1: positivos «04/07/24»
(`ext::3.3.3.4`), «una vez al año» (`pro::3.2.1.3`), «"AA"» (`polcre::5.2`), «fecha de entrega…» (`docvig::3.5`); negativos
`ext::8.4.4` y `cla::6.5::intro`. g2: positivo `cap::2.3.1`; negativos, las 4 de `cla::3.7` (con `cla::5.1.2.3`). g3: positivo, las
dos «APR» de `cap::8.3.2.12`; negativos la EPF (`cap::4.2.1.2::parte1`), el ponderador (`cap::3.2.1.1`) y la capacidad de préstamo
(`polcre::2.1.9`). Todos pasan; en O2, además, sintéticos de cada regex y de la enumeración «N. y M.».

---

## Grupo L — el tramo literal del elemento (`ensamblar_tanda0.py`, solo r2b)

`tramo_de_e1`: el elemento de origen e1 armado por el ensamblado guarda el tramo de E1 del que sale su cuantía, **después** del paso
del rótulo de T3-bis (que busca la cuantía entre las celdas de la tabla por el campo `tramo`; si el cambio fuera antes, la unidad
heredada del rótulo se perdería). Verificación contra el texto de E0 del nodo: con «exacta», el tramo de E1; con «tokens», el
literal mínimo del texto si conserva la cuantía (mismo valor y unidad); si no verifica, o el literal pierde la cuantía, **el elemento
conserva la cuantía y su verificación**, contado en el reporte (`tramo_de_e1.conservan_la_cuantia`). Este último paso no estaba en
la v7: los tramos de umbral de E1 con cuantía no los verifica el validador, y 5 no son literales (con la regla literal de la v7 los
«no» pasaban de 1 a 5, contra la aceptación).

Herramientas del piloto (`comun_P.py`, `armador_fichas_P.py`): `cuantia_del_elemento(el)` toma la cuantía de las detectadas en el
tramo por valor y unidad (o solo valor); en un grafo anterior devuelve el tramo. La usan `_alinear_e1` (`:343` de HEAD), `ubicar`
(`:386`) y el resaltado del armador (`:75`).

**Selftest.** Positivos `cap::12.3` (el 17 %, «El 17% en el caso de entidades del grupo B») y `cla::6.5.4.7` (el 5 % y el 20 % con
el mismo tramo); negativos, los de origen descripción y los del validador, sin cambio. Herramientas: las 20 fichas del lote 1 y el
formulario, rearmados sobre `e22fae1a` y sobre el grafo sin cola con B, C y L, salen byte a byte iguales a `p/lote1/` (metadatos
incluidos) (`salidas/fichas_L/*/comparacion.json`). En O2, `selftest_comparador_P.py` suma `cuantia_del_elemento` con un tramo de
una cuantía, uno compartido, uno de validador y uno anterior al grupo L.

---

## Grupo G — G-r (`ensamblar_tanda0.py`, solo r2b)

`corregir_procedencia_g_r` sobre los registros de `entrada_r2`, después de descartar la cola y antes de la resolución y de E2.
`ubicar_tramo_g_r` reproduce `udiag_b_procedencia.ubicar` con `validador_r2.verificar_tramo` (la función, no su copia por AST) y
`comun_e1.es_mini_chunk`. Solo entidades de contenido con `punto` en un ancestro de su unidad. Registro `procedencia_g_r.json` y
resumen en el reporte.

**Selftest.** Positivos `ctacte::2.1.1.4` (tramo compuesto, al ítem) y `ext::3.16.3.4` (tramo simple en el texto propio); negativo,
la Excepcion de `ctacte::2.1.1.6` con punto en su unidad (en ese chunk sí cambia otra entidad, e4, solo de rol). La «suite de
procedencia» de la aceptación no está definida en ningún archivo: propongo el invariante I5 de `r1_invariantes` (corre en la
cadena) y el ítem I5 de la suite, los dos en verde en la corrida.

---

## Grupo H — `Comunicacion.tipo` (`validador_r2.py`, forma r2)

El tramo verificado sigue primero (P3b, l). Si no da el tipo y el modelo no lo trajo: A/B/C desde el código o la etiqueta
(`derivar_comunicacion`), o «externa» con el léxico de la política más `LEXICO_EXTERNA_CODIGO` (dec, código, decisión, disposición);
la lista vive en el validador porque `politica_campos_r2.json` está sellada por su sha (`r1_e4.py:536`, que el §5 no deja tocar).
Si tampoco, `properties_no_definidas.tipo_no_derivable = true`; la clave entra a la lista de claves del código que el modelo no
puede escribir.

**Selftest.** Positivos «Decreto 28/23» → externa y «A-7000» → A; negativo, una Comunicación A con tipo de hoy, sin cambio. **Dos
casos de `selftest_pyd_r2.py` fallan con el código nuevo** (396/398): «Comunicacion con tramo sin verificar: con la forma r2 no se
deriva del código ni del label (P3b, l)» y «l: tramo verificado sin norma → no se deriva, contado». Afirman la regla de P3b, l que
H reemplaza; O2 los reescribe con la regla nueva (tramo primero, código después, marca al final).

---

## Grupo I — «Condiciones sin regla» (`scripts/metricas_intrinsecas.py`)

`condiciones_sin_regla(kg)` en `adaptador_gen3`, junto a M9: Condicion sin ninguna arista fuera de `establecida_en` y la remisión
(`remite_a`, o `referencia` con rol_fuente referencia_cruzada en r1), con la variante «sin `condicion_de` saliente». **M9 no
cambia**: es de la spec sellada, y `selftest_gate6` controla las claves de primer nivel y el valor de M9. Con el código nuevo, el
caso (ii) del selftest pasa (15/15).

**Selftest.** Una Condicion con solo `establecida_en` cuenta; una con `condicion_de` no (sintético, en `casos_v7.json`). El selftest
de la métrica no tiene lugar autorizado en el §5: propongo un archivo en `data/experiment/omisiones_cod/`.

---

## Grupo J — la procedencia de `remite_a` (`r1_referencias.py`)

`detectar_y_resolver_r2(…, procedencia_propia=False)`; el ensamblado pasa `procedencia_propia=r2b` (una línea en
`ensamblar_tanda0.py`). Con la opción, cada arista lleva la procedencia de su propio nodo de origen con la misma clave (to, punto,
rol, chunk), con su tramo; la cita del texto heredado lleva la procedencia del bloque heredado con `tramo_verificado = "ausente"`,
la marca explícita que el modelo ya admite. La detección, la atribución D1, los destinos y la evidencia no cambian.

**Selftest.** Dos orígenes del mismo punto y la misma cita con tramos distintos dan dos procedencias; una cita heredada lleva la
procedencia de su unidad con la marca. Los dos pasan en la corrida; en O2, un sintético en el selftest de remisiones.

---

## Grupo D — (h) e (i)

- **(h)** `aristas_por_origen(kg)` en el reporte (`aristas_por_origen`), con la clasificación de la observación 10 del tablero
  (`t3/medicion_tablero_r2b.py`, `obs10`). Selftest: un grafo sintético con una arista de cada clase (pasa).
- **(i)** medida, sin código del ensamblado (`scripts/medir_h_i.py`). Dos definiciones: la de la v6 (grado entrante más saliente
  mayor que 40, contando solo `remite_a` / todas menos `remite_a`) y la ventana real del agente (`ver_vecinos`, `limite=40` por
  dirección, `evaluacion/harness.py:197-235`), con y sin `remite_a`. Cuál rige es decisión de U-NAV-DISENO o de la autora.

---

## Grupo K — la causa «destino en unidad excluida» (ENS-05)

`irresolubles_en_unidad_excluida` en el ensamblado, solo sin la cola: la cita «punto_sin_nodos» cuyo destino es una unidad
descartada (o la contiene; la regla de `sincola_t0/registro_vista_r2b_sincola.py:87-88`) pasa a `destino_en_unidad_excluida`, en
el registro de remisiones y en `irresolubles_por_causa` del reporte (recontado con la unidad de cita del detector). No cambia
aristas. Selftest: positivo, una cita a una unidad de la cola en el sin cola; negativo, la cita a un punto inexistente conserva su
causa (pasan los dos).

---

## Dónde va cada escritura en O2 (y lo que el §5 no cubre)

| Archivo | Grupos | §5 |
|---|---|---|
| `tanda0/code/ensamblar_tanda0.py` | A, g–g3, L, G-r | sí |
| `tanda0/code/ensamblar_tanda0.py` | (h) en el reporte, K, y la línea que pasa `procedencia_propia` (J) | **no lo nombra** |
| `pyd_r2/code/validador_r2.py` | f, H | sí («donde viva hoy esa derivación») |
| `pyd_r2/code/selftest_pyd_r2.py` | los dos casos de P3b, l y los nuevos de f y H | sí («y su selftest») |
| `corpus_v2/r1_e4.py` | f′ | sí |
| `corpus_v2/r1_referencias.py` | J | sí |
| `scripts/metricas_intrinsecas.py` | I | sí |
| `med_umbrales/p/code/comun_P.py`, `armador_fichas_P.py`, `selftest_comparador_P.py` | L | sí |
| selftest del ensamblado (A, C, G-r, L, K, h) y de la métrica (I) | — | archivo nuevo: «y su selftest» no dice dónde; propongo `omisiones_cod/` |
