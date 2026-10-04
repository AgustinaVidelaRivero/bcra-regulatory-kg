# U-PROMPT-R2 — FRENO P3

04/10/2026. Base: `c448e42`. Durante la etapa HEAD avanzó a `54f57cd` por commits de otras sesiones (`7aed71c`,
`4019aa9`, `b0ee084`, `e82e22f` y `54f57cd`), que no tocan ninguno de mis archivos ni la cadena
(`git diff --name-only c448e42 HEAD`). USD 0: ninguna
llamada a la API. Sin commit: el commit es de la autora.

Fuentes:
- mandato: `git show b901f6d:docs/mandatos/UPROMPT_R2_prefijo_nuevo.md` (sha256 `80020edc…`), P3;
- sus notas fechadas, leídas en `c448e42`, en especial las dos del 04/10/2026: el agregado a P3 (`395fc0b`) y la de
  orden y control (`c448e42`).

Al pie del mandato hay una nota más, commiteada en `e82e22f` mientras corría esta etapa: la etapa P3b, que va
después del commit de P3. No cambia P3 y no la adelanto. Su punto g cambia `es_item`, y el tramo compuesto de `validador_r2`
toma `es_item` de `prompt_r2b`, así que el cambio le llega sin tocarlo.

## 0. Control previo (decisión 6)

`git status --short` sobre mis escrituras, antes de editar, salió vacío. Las escrituras eran `data/experiment/pyd_r2/`,
`e1_extractor/validador_e1.py` y `selftest_e1.py`, `corpus_v2/runner_corpus.py` y `r1_e4.py`, `selftest_manifiesto.py`,
`data/experiment/prompt_r2/`, `tanda0/code/ensamblar_tanda0.py` y `e2_reduce/`. Ninguna tenía cambios de otra sesión.

## 1. Parte 1: P3 del mandato, punto por punto

Todo rige solo con la forma «r2». Con la forma v3, `validador_r2` y `validador_e1` dan lo mismo que en HEAD: lo
controlé sobre el crudo guardado de la tanda 0, en 2.434 de 2.434 unidades (`validador_r2` con la forma v3, y
`validador_e1` con el perfil `v3_b54` y sin esquema).

| Punto (P3.a) | Dónde | Prueba |
|---|---|---|
| Tramos de umbral al llenado de la lista (par A), con la verificación de r2a | sin cambio: `validador_r2` los deja en `umbrales_tramos` y `llenar_umbrales_r2` los toma (`ensamblar_tanda0.py:699-700`) | ensamblado sintético: el elemento sale con `origen` e1, `tramo_verificado` exacta y la base resuelta a la Definicion |
| Mención a la resolución por relación (R1 a R4) | sin cambio (`r1_e4.resolver_relaciones_r2`) | S27 en PASS y LN-3 resuelto en los dos grafos sintéticos |
| Omisiones con categoría al registro; `fuera_de_tipos` y `relacion_sin_predicado` contados, con `source` y `destino` | `validador_r2.py:1158-1176`; `OmisionR2.source` y `destino` (`modelos_r2.py:568`); `omisiones.jsonl` en `cerrar_e2_r2` (`runner_corpus.py:1079`) | G13 y la cadena: LN-7 resuelto en el E2 r2 |
| Tramo de evidencia por entidad, verificado y con marca (decisión 15) | `verificar_tramo_entidad` (`validador_r2.py:248`); la marca va a la procedencia (`Provenance._evidencia`, `modelos_r2.py:429`) | G13: exacta, guion, tokens, no, ausente, anclada en un ancestro y TextoOrdenado |
| Tramo de dos segmentos (R11 y R30, FRENO P1): el primero contra el heredado, el segundo contra el propio | `validador_r2.py:248-282`; el nivel de cada segmento en `tramo_compuesto.encabezado.<nivel>` e `item.<nivel>` | G13: encabezado en dos bloques heredados, primer segmento del texto propio (no), fuera de un ítem, dos separadores |
| `termino` literal (decisión 16) | `termino_verificado` en la procedencia | G13: exacta y no |
| `Comunicacion.tipo` y `numero` derivados (decisión 16) | `validador_r2.py`, bloque de Comunicacion; `numero_desde_codigo` (`:325`) | G13: A 7825 da A y 7825; una ley da «externa», sin número |
| TextoOrdenado derivado (decisión 16) | el `archivo`, de la procedencia (E2, `e2_lib.py:980-981`, y E4, `r1_e4.py:228`) | cadena: el TextoOrdenado sin tramo y con su archivo |
| `otras_propiedades` de la relación como no definidas (decisión 17) | `validador_r2.py:957-968`; `RelacionR2` y `AristaR2.properties_no_definidas` | G13; en la arista, no llegan (límite 2 del §5) |
| Elemento sin valor del límite relativo (punto 5 del §10.1) | `elemento_umbral_relativo` (`validador_r2.py:285`), con los marcadores de U-PYD; va a `properties.umbrales` | G13 y el ensamblado: «no superen el importe resultante…» da máximo inclusivo, con su base |

**P3.b, crudo sintético.** `data/experiment/prompt_r2/p3/cadena_sintetica_p3.py` arma una corrida r2b de cinco
unidades de cla sobre la e0-r2 (un ítem, una Definicion, un límite relativo, un reintento y una cola humana). La
corre por `cerrar_e2_r2` y por el ensamblado r2b completo (`tanda0_ens_desarrollo_r2b`) y da 27/27 en doble
corrida idéntica (`p3/salida/resumen_cadena_sintetica_p3.json`, sha256 `dab1556e…`). El grafo ensamblado tiene 120
nodos y 146 aristas, con 0 fuera de `NodoR2` y `AristaR2`. La lectura del crudo de la tanda 0 como «v3» sigue igual
(arriba y §4).

**P3.c, shapes y suite.** P3 no las edita (decisión 5); las corrí sobre los dos grafos sintéticos.
- **Grafo del E2 r2:** S27 en fase r2b, bloqueante y en PASS (3 aristas de sujeto); LN-3 y LN-7, resuelto.
- **Grafo ensamblado:** las shapes de fase r2b dan PASA, con S18 y S27 en PASS y solo S11, informativa, en WARN.
  LN-3 da resuelto. LN-7 da no_aplicable, porque el ensamblado no escribe `omisiones.jsonl` (límite 4 del §5).

## 2. Parte 2: el agregado

### A1. Correcciones que pasan de `validador_r2` a `validador_e1`

Se aplican en `corregir_r2` (`validador_e1.py:186`), con el mismo código y la misma política. La política tiene
candado: sha `82e8752a…`, el de `r1_e4.POLITICA_R2_SHA256`.

| Corrección | Origen en `validador_r2` (HEAD) | En `validador_e1` |
|---|---|---|
| Tipo de entidad, por forma y por alias | `resolver_tipo`, `:217-231`, usado en `:514` | `corregir_r2` |
| Predicado, por forma y por alias | `resolver_predicado`, `:240-255`, usado en `:725` | `corregir_r2` |
| `sujeto_id` fuera del catálogo: la relación queda y va al registro | `:788-795` y `:818-829` | `:455-465`: el propuesto es la mención, o el id como texto |
| `sujeto_propuesto` suelto, que no es campo de la forma r2: no se lee | `:740-743` (a campos no definidos) | `corregir_r2`: se descarta |
| Mención en un predicado que no es de sujeto: rechazo (alineación) | `:831-834` | `:491` |
| Padre sugerido sin mención, con id: se descarta | `:765-770` | ya estaba en P2 (`proyectar_r2`, `:153-154` de HEAD) |
| Extremo sujeto mandado de más: se ignora | `:752-759` | ya estaba (`:376-379` de HEAD) |

Lo que pasa a E3 lleva `indice_crudo`, solo con la forma r2. `render_extraccion` (`comun_e3.py:140`) no lo lee, así
que el mensaje de E3 no cambia; lo prueba [I] de `selftest_e1`.

### A2. Con r2b, el ensamblado toma solo lo que pasó por E3

- `entrada_r2` (`runner_corpus.py:949`) lee los índices de la validación guardada del intento que E3 vio, con
  `vistos_por_e3` (`:936`): la validación final o, en la cola humana, la del primer intento.
- Se los pasa a `validador_r2.validar(..., vistos_e3=...)`, y lo demás no entra: queda en `no_vistos_e3`, sin fila
  en el registro de no mapeados.
- Una validación sin índices deja la unidad sin validación, con el error `validacion_e3_sin_indices_r2`.

### A3. `no_verificada_e3` por lo que pasó por E3

- **Modelo:** `RelacionR2` tiene `paso_por_e3` (`modelos_r2.py:516`). Si el campo es None, rige la regla de la forma
  v3, por la firma, que es la de los grafos r2a sellados. Si no, la marca es exactamente «no pasó por E3»
  (`:523-531`).
- **`EntidadR2`:** tiene `paso_por_e3` (`:471`).
- **Validador:** con `vistos_e3`, todo lo que entra lleva `paso_por_e3` True y ninguna marca.
- **Conteo:** está en el reporte del E2 r2, `reporte_e2_r2_<to>.json`, bajo `paso_por_e3` (`runner_corpus.py:1007`);
  da los elementos sin verificar, los excluidos y las unidades sin índices.
- **Ensamblado:** su reporte ya contaba las relaciones y aristas con la marca (`ensamblar_tanda0.py:841` y `:922`).
  Con r2b dan 0, en la cadena sintética.

**Especificación del control que exige cero** (no implementado; entra con los pedidos de suite previos al gate de
r2b, `docs/plan_tesis.md:400`):
1. **Ámbito:** perfil r2 y fase r2b. Con r2a da no_aplicable, porque los grafos sellados llevan la marca por la
   firma (697 y 627).
2. **Aristas de E1:** toda arista con predicado de E1 que no sea derivada lleva `no_verificada_e3` ausente o false.
   Son derivadas `rol_fuente` `derivada_de_procedencia`, `remite_a` y las del esqueleto. Esto se puede hacer como
   shape, sobre el grafo solo.
3. **Nodos:** todo nodo de los nueve tipos tiene al menos una procedencia de una unidad que E3 cerró. Si no, lleva la
   marca de la cola: esa es la excepción explícita (A5) y se cuenta aparte, con su tasa de error por muestra en cada
   tanda.
4. **Registro de la entrada:** fuera de la cola, 0 entidades con `paso_por_e3` distinto de true y 0 relaciones con
   la marca; la cola, aparte (`paso_por_e3.cola_humana`); `no_vistos_e3` se informa, no se exige.
5. **Exentos, declarados:** los elementos de umbral (llevan origen, regla y tramo verificado), los Sujeto del
   catálogo y los propuestos, el TextoOrdenado canónico y las aristas derivadas.
6. **Veredicto:** persiste con cualquier conteo mayor que 0.

Hoy el punto 3 se puede leer solo por `chunk_id` y la marca de la cola, porque el nodo no lleva el estado de E3.

### A4. La `establecida_en` derivada se declara derivada

**Lo nuevo de P3**, en `modelos_r2.py`:
- `ROL_FUENTE_DERIVADA_DE_PROCEDENCIA` y `PREDICADOS_DERIVADOS_DE_PROCEDENCIA` (`:190-191`);
- el invariante de `AristaR2` (`:650-660`): con ese `rol_fuente`, solo `establecida_en`, sin marcas de E1 y sin
  properties.
Las 536 de diez y las 372 de desarrollo lo cumplen. Los reportes reproducidos son iguales a los sellados, con 0
aristas fuera del modelo.

**Lo que ya cumplía:**
- `remite_a`: `PREDICADOS_DERIVADOS` (`:165`) y el invariante de `AristaR2` (`:670` y siguientes), con `alcance`,
  `destino` y `evidencia`, sin marcas de E1 ni `rol_fuente`;
- los umbrales: `ElementoUmbral` lleva `regla_comparacion`, `origen` y `tramo_verificado` (`:285-287`), que llena
  `llenar_umbrales_r2` (`ensamblar_tanda0.py:663-751`).

### A5. Unidades que E3 no terminó: entran marcadas (decisión de la autora, 04/10/2026)

La autora decidió que las unidades que E3 no terminó (ratchet agotado y cola humana) entran al grafo marcadas, como
hoy, y que en cada tanda se revisa una muestra con su tasa de error. Son la excepción explícita a «cero elementos sin
verificar» y se cuentan aparte. No toqué `ratchet_e3.py`: su comentario se alinea en el parche posterior a P3.

Verificado bajo la regla nueva:
- `entrada_r2` no cambia para ellas: entra el crudo del primer intento, con lo que E3 vio de él y `cola_humana`, y E2
  las marca (`e2_lib.flaggear_cola_r2`);
- sus relaciones entran sin `no_verificada_e3`, porque E3 las vio; la excepción la lleva la marca de la cola;
- el conteo las separa: `paso_por_e3.cola_humana` en el reporte del E2 r2 (`runner_corpus.py`, `conteo_paso_por_e3`),
  con las unidades por estado, las entidades y las relaciones; los elementos sin verificar se cuentan sin ellas;
- en la cadena sintética, `cla::3.5.1` entra con la marca en sus 2 nodos y su arista, en el grafo del E2 r2 y en el
  ensamblado, y el reporte la cuenta aparte (1 unidad, 2 entidades y 1 relación).

Cifras de la tanda 0 (`p3/a5_a6_tanda0.py` → `p3/salida/a5_a6_tanda0.json`):

| | Diez | Desarrollo |
|---|---|---|
| Unidades | 71: 35 con el ratchet agotado (`cola_humana`) y 36 con el veredicto inutilizable | 44: 24 y 20 |
| Nodos con la marca, en el grafo r2a sellado | 291 (263 solo de la cola, 28 mixtos) | 216 (194 solo de la cola) |
| Aristas con la marca, en el grafo r2a sellado | 466 (457 solo de la cola) | 343 (335 solo de la cola) |
| Elementos que entran con r2b (simulación de A6), contados aparte | 343 entidades y 466 relaciones, 0 con `no_verificada_e3` | 244 y 343, 0 |

**Hallazgo, fuera de mis escrituras.** Hay aristas derivadas que tocan un nodo que solo viene de la cola y no llevan
la marca: 788 en diez (778 `remite_a` y 10 `establecida_en` derivadas) y 763 en desarrollo (757 y 6).
- La causa: el ensamblado marca la cola (`ensamblar_tanda0.py:829`) antes de derivar (`:881` y `:892`).
- Para que la excepción quede completa en el grafo, hay que marcar también después de derivar, en
  `ensamblar_tanda0.py`.
- Lo dejo para quien tenga esa escritura autorizada.

### A6. Cuántos elementos cambian de estado

Sobre el crudo guardado de la tanda 0 (`p3/salida/a5_a6_tanda0.json`, sha256 `400fd1b8…`, doble corrida idéntica):

| | Primer intento, diez | Final, diez | Final, desarrollo |
|---|---|---|---|
| En r2a sin pasar por E3 (con marca + sin marca) | 667 (655 + 12) | 701 (697 + 4) | 630 (627 + 3) |
| Los ve E3 con el esquema r2b de P2 | 657 (655 de la matriz y 2 de sujeto) | 699 | 629 |
| Los ve E3 recién con A1 | 10 (2 entidades, sus 6 relaciones y 2 predicados) | 2 | 1 |
| Siguen sin pasar por E3 tras A1 | 0 | 0 | 0 |
| A2: se pierden (`validador_r2` los admitiría y E3 no los vio) | 0 | 0 | 0 |
| A2: E3 los vio y `validador_r2` los rechaza | 0 | 0 | 0 |
| A3: marcas por la firma que se retiran | 655 | 697 | 627 |
| Sin verificar tras A2 y A3 | 0 | 0 | 0 |
| Admitidos, entidades y relaciones (r2a = con A2) | 10.494 y 14.369 | 10.806 y 14.990 | 8.222 y 11.540 |

Las cifras de control de la revisión se reproducen. Ningún elemento se pierde.

**Límite:** E3 no se vuelve a correr. Si E3 viera más elementos, su veredicto y sus reintentos podrían cambiar: la
tabla cuenta qué le llegaría, no qué aceptaría.

## 3. Cambios en la cadena de lectura (escrituras)

| Archivo | Qué |
|---|---|
| `pyd_r2/code/modelos_r2.py` | `Provenance._evidencia`; `paso_por_e3` en `EntidadR2` y `RelacionR2`, y la marca por E3; `properties_no_definidas` en `RelacionR2` y `AristaR2`; `source` y `destino` en `OmisionR2`; la `establecida_en` derivada |
| `pyd_r2/code/validador_r2.py` | la forma r2 completa y `vistos_e3`; con la forma v3, igual a HEAD |
| `pyd_r2/generados/manifest_generados_r2.json` | regenerado: cambia solo el sha de `modelos_r2.py` (`e67f15ae…`); el tool schema (`0c391f2b…`) y los enums (`abd197ac…`), byte a byte |
| `pyd_r2/code/selftest_pyd_r2.py` | G13 (31 casos), el control del tramo de G9 y la constante de la generación |
| `e1_extractor/validador_e1.py` y `selftest_e1.py` | A1 e índices; [I] (15 casos) |
| `corpus_v2/runner_corpus.py` | `vistos_por_e3`, `entrada_r2` con la forma r2, `validador_perfil_r2`, `conteo_paso_por_e3` (con la cola humana aparte) y, en `cerrar_e2_r2`, `omisiones.jsonl` y el conteo |
| `prompt_r2/p3/` | `cadena_sintetica_p3.py`, `a5_a6_tanda0.py` y `salida/` |
| `prompt_r2/freno_p3.md` | este documento |

El prefijo (`14d6b63b508e`) no cambia.

## 4. Sellados reproducidos y selftests (sobre copias sin enlaces)

**Control de reproducción** (`control_reproduccion_p3.py`, en el paquete), sobre una copia nueva:
- `ens_diez_r2a` da `99fe2bfa…` y `ens_desarrollo_r2a` da `93a7af72…`, los sellados. Son 30 y 20 archivos byte a
  byte, y el reporte es igual con la ruta normalizada.
- Los tres ensamblados r1 dan 10 de 13 archivos byte a byte y 3 iguales con la ruta normalizada, como en P2.
- El repo cambió durante el control en 3 archivos, todos de otra sesión: `docs/plan_tesis.md`,
  `docs/protocolo_entre_tandas.md` y `docs/enmiendas_adendas_1_y_2_laudo_B5.5_2026-10-04.md`. El control escribe
  solo fuera del repo.

**Selftests**, sobre la copia `p3/copia`, en una corrida de cierre (`cierre_p3.sh`, en el paquete):
- la copia se arma sin enlaces;
- se toma el sha256 de los archivos del repo antes y después (12.671 y 12.674);
- se corren también la cadena sintética y A5/A6, que reproducen byte a byte los resúmenes de `p3/salida/`.

Durante la corrida cambiaron en el repo 4 archivos, todos de una figura de otra sesión: `docs/tesis/figuras/`,
`figura_ensamblado_ejemplo.pdf`, `.png` y `.svg`, y `generar_figura_ensamblado_ejemplo.py`. Ninguno es mío y
ningún selftest escribió en el repo.

| Selftest | Resultado |
|---|---|
| `selftest_manifiesto` | 44/49: P10 9/9 y P11 3/3; los 5 fallos son los de P5, por la ruta absoluta del reporte sellado de E2 |
| `selftest_pyd_r2` | 332/332 |
| `selftest_e1` | 80/80 |
| `selftest_prompt_r2b` y `selftest_e3` | 23/23 y 80/80 |
| `selftest_cablev3` | 45/45 |
| E0: `selftest_e0`, `b52`, `b581`, `b582` y `b583` | 57/57, 39/39, 34/34, 59/59 y 33/33 |
| `selftest_e0r2` y `selftest_ub53` | 48/48 y 40/40 |
| `selftest_corpus` y `selftest_e2` | 21/21 y 35/35 |
| `selftest_dirigida_tanda0` | 28/28 |
| `selftest_r2`, `selftest_r3` y `selftest_r4` (con `--e0-r2`) | 18/18, 96/96 y 26/26 |
| `selftest_regression_kg` y `selftest_shapes_congelado` | 147/147 y 79/79 |
| `cadena_sintetica_p3` | 27/27 |

## 5. Contradicciones y límites, para decidir

1. **TextoOrdenado.** La decisión 16 dice que `materia`, `archivo` y `version` «se derivan de E0 y del inventario, como
   ya hace la canonización de E4». Pero E4 deriva solo el `archivo` (`r1_e4.py:228`), y ni la E0 ni los manifiestos
   de la tanda 0 traen la materia o la versión del TO. Mandan los archivos. Con r2b, el TextoOrdenado queda sin
   `materia` y sin `version`. La fuente la decide la autora.
2. **`otras_propiedades` de la relación.** Llegan a la relación validada, pero E2 copia a la arista solo
   `MARCAS_ARISTA_R2` (`e2_lib.py:801-803`), y el mandato no autoriza editar E2. `AristaR2` ya admite el campo.
3. **Límite relativo junto a una cuantía en la misma entidad.** `llenar_umbrales_r2` reemplaza la lista
   (`ensamblar_tanda0.py:751`) y el elemento relativo se pierde. `validador_r2` lo cuenta como
   `umbrales.limite_relativo_con_cuantias_en_la_entidad`. Solo con el relativo, llega al nodo.
4. **LN-7 sobre el grafo de U-REEXT-T0.** El ensamblado no escribe `omisiones.jsonl`, así que LN-7 queda no_aplicable.
   El conteo de entidades sin verificar está en el reporte del E2 r2, no en el del ensamblado. Las dos cosas piden
   tocar `ensamblar_tanda0.py`, fuera del despacho por perfil.
5. **Tramo solo en el heredado.** Un tramo simple que solo está en el heredado no baja de nivel: la decisión 15 dice
   «texto propio o heredado». Se cuenta según dónde se ancla la entidad (`tramo_entidad.solo_heredado:<caso>`).
6. **Hallazgo de A5:** las aristas derivadas de nodos de la cola quedan sin la marca (788 y 763). Cerrarlo pide
   tocar `ensamblar_tanda0.py`.

## 6. Error propio, con su causa

Para iterar, corrí `selftest_e1` y `selftest_pyd_r2` sobre el repo, no sobre una copia, contra la regla l. También
corrí contra el repo los dos controles rápidos, de solo lectura, de la forma v3 y de la forma r2. Ninguno escribe:
- `git status` quedó igual, salvo mis escrituras y las de otras sesiones;
- no hubo `.pyc` nuevos (línea de base de 2.213 archivos).
Los resultados de este freno salen de las corridas sobre las copias.

## 7. Pendiente

- Commit de P3: PENDIENTE de la autora.
- Las decisiones de los puntos 1 a 4 y 6 del §5.
- C2 de U-R2-CODIGO-2 arranca sobre el commit de P3; después vienen P3b y P4.
