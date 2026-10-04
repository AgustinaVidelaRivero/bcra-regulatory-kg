# U-DIAG-VINCULO — anexo de evidencia (04/10/2026)

USD 0, sin API ni Neo4j, solo lectura. Las corridas van sobre una copia copiada del repo en el scratchpad, sin
enlaces (regla l). Las rutas `code/` y `salidas/` son relativas a `reports/u_diag_vinculo/`.

## 1. Fuentes firmadas y commits leídos (regla k)

| documento | commit | sha256 del texto | uso |
|---|---|---|---|
| L-ESQ-R2 (`data/experiment/esq/enmienda_L-ESQ-R2_2026-09-30.md`) | `4ef7650` | `66c4a1b9…` | §1 (retiro, `:100-101`), §6.3 (piso 0,75 y retiro en código, `:784-795`) |
| Enmienda 2 de L-ESQ-R2 (`…/enmienda2_L-ESQ-R2_remite_a_2026-10-02.md`) | `5f9a731` | `e779bd70…` | §1 `:54-55`, §2 `:61-73`, §3 `:77-102`, §4 `:107-123`, §10 `:178-186` |
| Mandato de U-PROMPT-R2, notas al pie | `10629b3` (igual en HEAD) | — | ajuste de R8, `:411-413` |
| Diseño del prefijo, P1 | `fca019d` | — | R8 `:274-288`, R30 `:470-501`, R16 `:503-517`, 212 encabezados `:1075` |
| Prefijo r2b congelado, P2 | `20b7f60` | hash del prefijo `14d6b63b508e`; tool schema `0c391f2b` | R8 `prompt_r2b_reemplazos.json:60-63`, R30 `:114-117`, R16 `:120`; regla 3 `prompt_e1.py:133`; mensaje del 5.1.1.1 `request_cla__5.1.1.1.json:897`; `tramo` requerido `tool_schema_r2.json:32`, `:51-55`; E3 `prompt_e3.py:85`, `:242-248` |
| Mandato de esta unidad | `8744a5c` (firma) | — | texto igual al mandato pegado |
| U-DIAG-PROCESO | `93ce4b7` | — | forma A, VU-B, costos de referencia |

## 2. Tarea 1, salida completa

Está en `salidas/tarea1_ejemplo.txt`, generada por `code/tarea1_ejemplo.py` sobre la copia de
`ens_desarrollo_r2a/r2/kg.json` (sha `93a7af72…`).
- Del crudo de E1 (`corpus_tanda0/salida_dirigida/cla/extracciones_e1.jsonl:60-61`):
  - `cla::5.1.1::intro` emite solo la Definicion «Cartera comercial — alcance»;
  - `cla::5.1.1.1` emite la Definicion de la contraexcepción, dos Condicion y una Operacion; sus dos
    `condicion_de` → Operacion caen por firma en la matriz congelada (`extracciones_finales_cla.jsonl:61`, `rechazos`).
- E3 da `completo_ok` en las dos unidades (`veredictos.jsonl:65-66`).

## 3. Tarea 3, muestra de 10, con mi lectura del tipo

La regla y el sorteo están en `regla_deteccion.md` (sha `f912176c…`, tomado antes de correr; el script lo
imprime en la primera línea de `salidas/censo_anuncios.txt`). En los 10 casos, el anuncio y los hijos están
bien detectados. El tipo léxico:

| # | contenedor | tipo asignado | mi lectura | veredicto del tipo |
|---|---|---|---|---|
| 1 | efemin::1.3.17::intro | excepción | «excluidos los vinculados…» es interno a la cláusula; los ítems son contenidos | mal (enumeración) |
| 2 | cap::3.1.4::intro | excepción | «opción de exclusión» es un término; los ítems son requisitos conjuntos | mal (c1) |
| 3 | ext::3.13.1::intro | excepción | «excepto para las operaciones de:» | bien |
| 4 | gracre::5.1.1::intro | c1 | «que reúnan los siguientes requisitos mínimos:» | bien |
| 5 | ext::7.9.1::intro | c1 | «en los siguientes casos:» | bien |
| 6 | ext::8.5::intro | c2 | «alguna de las situaciones detalladas a continuación»: los ítems son los supuestos | mal (c1) |
| 7 | depaho::3.9.2::intro | alcance | modalidades admitidas: alcance o enumeración | dudoso |
| 8 | tasint::4.1::intro | alcance | «tales como» es interno; los ítems son contenidos de un deber | mal (enumeración) |
| 9 | pro::2.3.6::intro | enumeración | «deberán:» | bien |
| 10 | pimf::4.12::intro | enumeración | «las IMFs deberán:» | bien |

El tipo está bien en 5, dudoso en 1 y mal en 4: los conteos por tipo son indicativos, no medidos. El error
típico es una marca léxica interna a la cláusula que no gobierna la catáfora. La detección del anuncio no
depende del tipo.

## 4. Opciones para unir una Excepcion con un contenedor tipado como Definicion

El esquema fijo es: tipos, predicados y matriz, del congelado más L-ESQ-R2 y su enmienda 2.

| opción | documento firmado que pide | riesgo | ¿cambia el esquema según la decisión 1? |
|---|---|---|---|
| O1. `remite_a` derivada de la estructura, `alcance = interna`; la forma («anuncio estructural») va al registro de remisiones, como pide D2 (`5f9a731:101-102`) | enmienda a la enmienda 2: §1 (qué afirma: hoy «cita un punto», `:54-55`) y §4 (garantía y atribución: el destino sale de la estructura, no del número citado, `:109-123`); una nota no alcanza, porque cambia texto firmado | mezcla citas y anuncios bajo el mismo predicado y el mismo alcance, y el agente los distingue solo por `evidencia`; agrega 6.630 `remite_a` a las 14.000 de KG-Tanda0-Diez-r2a (`censo_anuncios.txt`); `ver_vecinos` corta en 40 (`neo4j_index.py@395fc0b:226`); precisión medida 45 de 76 (§5) | en la letra, no: los tipos, los predicados y las 56 firmas no cambian. Sí cambia la definición firmada de un predicado del esquema final; si la autora lo cuenta como cambio de esquema, la opción queda excluida |
| O2. `remite_a` con un valor de `alcance` propio (p. ej. `estructural`) | enmienda a la enmienda 2: §3, la lista cerrada de tres valores (`:77-82`), y §1; además `ALCANCE_REMISION` (`modelos_r2.py@395fc0b:169`) y las shapes (§8) | contradice la regla del propio §3, «El alcance se decide comparando textos ordenados, no por la forma de la cita» (`:84`): mezcla dos ejes en un campo. Es más fácil de distinguir para el agente | en la letra, no. Es un valor nuevo en una lista cerrada del esquema: lo trato como cambio de vocabulario y no la recomiendo |
| O3. No unirlos y declararlo | ninguno sobre el esquema; un límite declarado en el laudo de la release r2 (`docs/laudo_release_r2_pipeline.md`, en borrador; NO VERIFICADO que tenga sección de límites) | el ejemplo de la tesis queda sin la arista regla → excepción. Desde la regla, el agente ve «con excepción de las siguientes» sin vecino al que ir; desde el ítem, ve la excepción compuesta, si R30 la produce | no |
| O4. Predicado tipado Excepcion → Definicion | cambia la matriz | — | sí: excluida por la decisión 1 |
| O5. Que E1 tipe el contenedor como Obligacion o Restriccion | cambia el prompt de E1 (P2 congelado en `20b7f60`) | tipar contra la definición de Definicion; el r1 vigente lo tipó así (Operacion + Restriccion, `corpus_v2/salida_r1/kg.json`) y la tanda 0 no | no cambia el esquema, pero sí el prompt: fuera de lo que admite el FRENO V1 |

## 5. Lectura de precisión

Está en `salidas/lectura_precision.md`, sobre las fichas de `salidas/muestra_precision_fichas.md`.

## 6. Direcciones: tabla completa

| | pieza | esquema | prompt / tool schema de E1 | re-extraer | costo USD (base en §7) | medición | antes del escalado |
|---|---|---|---|---|---|---|---|
| (a-T) predicado tipado | ensamblado (`ensamblar_tanda0.correr_cadena_r2`, después de `REF.detectar_y_resolver`, `@395fc0b:881-882`) | no cambian tipos, predicados ni matriz; pide enmienda a L-ESQ-R2 (los 13 predicados «emitidos por E1», `5f9a731:182-183`, pasan a tener instancias derivadas) | no | no | 0 | 13 de 23 aristas correctas en r2a, Wilson [0,368; 0,744]; no cubre el ejemplo (contenedor Definicion) | sí en lo técnico (código sobre lo guardado); la precisión medida no llega al piso |
| (a-R) `remite_a` estructural | ensamblado (regla nueva junto al detector, `r1_referencias.py`) | O1: no en la letra; enmienda a la enmienda 2 | no | no | 0 | 45 de 76 aristas en r2a, Wilson [0,480; 0,696]; cubre el ejemplo (4 aristas al 5.1.1.1) | sí, con la condición de pasar el piso en r2b |
| (b) referencia del extractor por punto y tipo | E1 (prompt y tool schema), validador de E1, E3, resolución en el ensamblado | no | sí: `target` es un `local_id` del chunk (`tool_schema_r2.json@20b7f60:550`), y la regla 3 dice «Las relations son SOLO entre entidades del MISMO chunk» (`prompt_e1.py@20b7f60:133`) | no, si entra en U-REEXT-T0; reabre P2 (prefijo `14d6b63b508e`, tool schema `0c391f2b`) y P4 | ≈ 0,14 dentro de U-REEXT-T0 | P4 rehecha; lectura de resolución (destino único o ambiguo); E3 no puede verificar lo que no ve | no |
| (c) pasada de modelo sobre pares | etapa nueva entre E3 y el ensamblado, con prompt, schema, caché (`llm_cache`) y verificación propios | no (emite predicados de la matriz) | no (otro prompt) | no | tanda 0: 3,07 (1.096 pares) o 1,09 (391 de excepción y c1); partición: 8,02 o 1,04; sin verificación ni calibración | calibración contra lectura; misma lectura de precisión; sigue limitada por la matriz (el ejemplo no tiene predicado) | no: es una etapa nueva, con diseño y calibración |
| (d) navegación (A1.8, vista de los nodos de un punto y de sus hijos) | agente | no | no | no | ≈ 0,022 por corrida del agente (anexo de U-DIAG-PROCESO, §4, `93ce4b7`) | capa 3 de A1.8 sobre preguntas ancladas en contenedores | no aplica (no toca el grafo); es complemento |
| (e) límite declarado | laudo de la release r2 y tesis | no | no | no | 0 | — | sí |

**Cómo se declaran las aristas de (a).**
- (a-R), como `remite_a`:
  - la deriva el código del ensamblado desde E0, con `evidencia` = la cláusula anunciadora literal del texto de
    E0 del contenedor y `destino` = la unidad hija;
  - procedencia: la del contenedor, con su `chunk_id`;
  - sin `rol_fuente` (D2) y sin `no_verificada_e3`: E3 no la verifica (`5f9a731:113`);
  - la forma («anuncio estructural») va al registro de remisiones (`:101-102`), contada aparte.
- (a-T): son predicados que emite E1, así que la instancia derivada necesita una marca que la distinga.
  - Precedente: `establecida_en` con `rol_fuente = derivada_de_procedencia` (`ensamblar_tanda0.py@395fc0b:592-608`).
  - Tampoco lleva `no_verificada_e3`.
- Las dos variantes piden enmienda, no nota, porque cambian texto firmado: (a-T) cambia L-ESQ-R2 §10 tal
  como lo lee la enmienda 2 (`5f9a731:182-183`); (a-R) cambia la enmienda 2, §1 y §4.

**Medición propuesta para (a).**
- Test de suite del ejemplo: existe al menos una `remite_a` desde el nodo de `cla::5.1.1::intro` cuyo `tramo`
  contiene «con excepción de las siguientes» hacia un nodo de `cla::5.1.1.1`.
- Lectura de 30 aristas derivadas sobre la salida de U-REEXT-T0, con la regla del §9, y el piso de Wilson 0,75
  del criterio de L-ESQ-R2 §6.3. Si no lo alcanza, se retira en código sin re-extraer, como prevé para → Potestad
  (`4ef7650:795`).
- Control de cuántos nodos superan el corte de 40 de `ver_vecinos` por las aristas nuevas.

## 7. Bases de costo

- Precios de E1 (Haiku 4.5): 1,00 entrada, 5,00 salida, 1,25 escritura de caché y 0,10 lectura de caché, en
  USD por millón de tokens (`corpus_v2/runner_corpus.py@395fc0b:90-91`).
- (c), por par: 1.500 tokens de entrada sin caché (SUPUESTO: dos textos de unidad y dos listas de nodos; como
  referencia, las unidades del ejemplo llevaron 883 y 1.047 tokens sin caché, `extracciones_e1.jsonl:60-61`),
  3.000 de prefijo en caché (SUPUESTO) y 200 de salida (SUPUESTO).
  - Cálculo: 1.500 × 1,00 + 3.000 × 0,10 + 200 × 5,00 = 2.800 USD por millón de pares = USD 0,0028 por par.
  - Tanda 0: 1.096 × 0,0028 = 3,07; los 391 pares de excepción y c1, 1,09.
  - Partición: 2.864 × 0,0028 = 8,02; los 373 de excepción y c1, 1,04.
  - Sin verificación (a la tarifa de E3, 2,00 y 10,00, `:93-94`) ni calibración.
- (b), en U-REEXT-T0:
  - prefijo: 300 tokens más (SUPUESTO) × 2.434 unidades × 0,10 / 10⁶ = 0,073;
  - salida: 20 tokens más (SUPUESTO) × 706 ítems × 5,00 / 10⁶ = 0,071;
  - total ≈ 0,14, sin contar rehacer P4 (tope USD 2).
  - Los 706 ítems salen de `censo_p1.json`, citado en `diseno_prefijo_r2.md@fca019d`, §4.5.
- (a): USD 0, código sobre lo guardado; la lectura asistida también es USD 0.

## 8. Comandos

Copia en el scratchpad (sin enlaces, `find <espejo> -type l` da 0): `ens_desarrollo_r2a/r2/kg.json`,
`ens_diez_r2a/r2/kg.json`, `e0_chunking/salida_tanda0`, `e0_chunking/salida_tanda0_r2` y
`segmentacion_84/b584_particion`, bajo `<espejo>/data/experiment/…`. Desde la raíz del repo, con
`PYTHONDONTWRITEBYTECODE=1` y `.venv/bin/python -B`:

```
code/tarea1_ejemplo.py <espejo>/…/ens_desarrollo_r2a/r2/kg.json                 → salidas/tarea1_ejemplo.txt
code/censo_anuncios.py <espejo> regla_deteccion.md <dir>                         → salidas/censo_anuncios.{txt,json}, salidas/muestra_precision_fichas.md
```

`salidas/lectura_precision.md` es lectura mía sobre las fichas, con la regla del §9.
