# U-PROMPT-R2 — FRENO P4b (la prueba corta)

04/10/2026. HEAD `91c6a24`. Tope USD 1,5; gasto real **USD 0,8111**. Sin commit. El detalle está en `p4b/` y en el paquete
de revisión.

**Fuentes.** Las notas del mandato hasta la última (`docs/mandatos/UPROMPT_R2_prefijo_nuevo.md:890-913`, `91c6a24`) y
`docs/decisiones_caching_extraccion.md`. El «seguí» coincide con los archivos: P3c-2 en `66cde30` (padre `44c6e1b`) y
la corrección de la clase modalidad en `bb212f1`.
- **Error propio, con su causa.** En el turno de la corrección de modalidad tomé «P3c-2 quedó commiteada en
  `599b304`» sin contrastarlo con `git log`. `599b304` es la nota del mandato; P3c-2 es `66cde30`. Quedó escrito en
  `freno_p3c2_modalidad.md` («HEAD `599b304` (P3c-2 commiteada por la autora)»), ya commiteado en `bb212f1`. No lo
  edito: lo corrige una nota, si la autora lo decide.

## 1. Release contra release

Cada brazo corrió desde una copia del repo en su commit, hecha con `git archive` (sin enlaces), con el código de ese
commit: prefijo, mensaje y lista de tablas forzadas. La e0-r2 es la misma: la de C2, `e0_chunking/salida_tanda0_r2b/`.

| Brazo | Commit | Prefijo | Namespace de E1 |
|---|---|---|---|
| anterior | `44c6e1b`, padre de `66cde30` | `3817de475c93` | `e1_extraccion\|cv=e1-extractor-v1-p3817de475c93\|think=0` |
| P3c | `bb212f1` | `322c5a23e9b7` | `e1_extraccion\|cv=e1-extractor-v1-p322c5a23e9b7\|think=0` |

- **El camino de E1** es el de `runner_corpus.fase_e1` con el perfil r2 de cada release (`p4b/correr_p4b.py`). El tercer
  escalón solo existe en `bb212f1`. Las particiones por corte no se corren, como en P4.
- **Las dos salidas se validan con el validador de `bb212f1`** (`p4b/analisis_p4b.py`), así el contador es el mismo
  en los dos brazos.
- No hubo errores, cortes ni reintentos por forma en los 54 pedidos.

## 2. Las unidades, elegidas por lectura y selladas antes de correr

`p4b/seleccion_p4b.md` y `p4b/salida/seleccion_p4b.json` (sha256 `e2551cf3…`). Lo sellé a las 23:01 y la corrida
empezó a las 23:07. Hay **27 unidades, no 29**:
- **a:** `ext::13.1.4` (régimen de transición con condiciones), `ext::6.1.1`, `cap::10.3.3.1` y `cap::11.4`.
- **b1:** `ctacte::3.2.2`, `3.2.5` y `3.2.4`. **b2:** `ext::3.5.3.4`, `3.5.3.5` y `3.5.3.1`. **Encabezados de b**,
  2 y no 4: `ctacte::3.2::intro` y `ext::3.5.3::intro`.
- **c:** `cap::5.3.1.3`, `cla::6.5.4.5`, `ext::10.4.2.5` y `ext::10.3.6`.
- **d:** `ext::10.4.3.6`, `ext::4.1.4.7`, `polcre::2.1.15` y `cap::10.2.2.4`.
- **e:** `cap::6.3.2::intro`, `cap::3.2::intro`, `cap::6.3.2.1` y `polcre::5.3`.
- **El ejemplo** y **f**, fijos.
- **La pata de E3** tiene 5 unidades y no 6: los 2 encabezados de b, el del ejemplo (`cla::5.1.1::intro`) y dos de a.
- **b1 en otra forma, con lectura dudosa.** De las 29 listas leídas, `ctacte::3.2` («no valdrá como cheque») es la única
  que leo como lo que queda afuera de una clase. Las demás listas de b de la tanda 0 se leyeron en U-DIAG-VINCULO o en
  P3b, y están excluidas. Los dos brazos leen `ctacte::3.2` como una Restriccion con sus supuestos: apoya la otra
  lectura. Si la autora la descarta, b1 se mide solo con el ejemplo.
- **Una corrección antes de correr:** el script excluía también los ids de los documentos de P4b, y re-corrido desde el
  repo se habría excluido a sí mismo. Ahora salta `p4b/`; la salida es la misma, byte a byte.

## 3. Costo y caché

| | USD |
|---|---:|
| Proyección (`p4b/salida/proyeccion_p4b.json`) | 0,7411 central / 1,2994 alta |
| E1, brazo anterior (27 llamadas) | 0,3680 |
| E1, brazo P3c (27) | 0,3487 |
| Llamada del tercer escalón (1) | 0,0068 |
| Pata de E3 (6 verificaciones) | 0,0740 |
| Reintento de E1 de la pata (1) | 0,0136 |
| **Total** (`p4b/salida/costo_p4b.json`, presupuesto compartido) | **0,8111** de 1,5 |

- **Caching:** el system con breakpoint, armado por cada perfil (D1); el gasto, con la fórmula de caching (D2); una
  línea de usage por respuesta real (D3: 27 en la copia de `44c6e1b` y 35 en la de `bb212f1`, en el paquete); todo en
  serie (D4), con una escritura de prefijo por brazo, de 26.309 y 27.840 tokens; la evaluación no se toca (D5).
- **Bases:** propias de P4b, en el scratchpad (`p4b/trabajo/cache/`). Como la de P4, no se reutilizan en U-REEXT-T0.
- **Claves** (`claves_antes_*.json` y `claves_despues_*.json`):
  - antes, ninguna de las 54 estaba en la base de P4b ni en la de la tanda 0;
  - 3 del brazo anterior (el ejemplo y f) estaban en la de P4, con el mismo pedido, y se pagaron igual en la base
    propia;
  - después, las 54 están en la de P4b.

## 4. a. Por grupo y por brazo (lectura asistida, PENDIENTE de revisión de la autora)

Marcas y razones: `p4b/marcas_p4b.py` y `p4b/salida/marcas_p4b.json`. Fichas cegadas, sin grupo ni origen, en el orden de
la semilla `U-PROMPT-R2:P4b:2026-10-04:fichas`: `p4b/salida/fichas_p4b.md`.

| Grupo | Lo que mide | Anterior | P3c |
|---|---|---|---|
| a, transición | ninguna omisión meta_normativo con contenido normativo; ese contenido, extraído | uno de uno | ninguno de uno |
| a | lo mismo | tres de tres | dos de tres |
| b1, ítems | Excepcion del miembro, con la norma exceptuada | ninguno de tres | ninguno de tres |
| b2, ítems | Condicion del supuesto, con el cuantificador y la norma exceptuada | ninguno de tres | ninguno de tres |
| b, encabezados | Definicion de la clase (b1); norma y excepción unidas (b2) | ninguno de dos | ninguno de dos |
| c | una Condicion por supuesto, coherente | dos de cuatro | uno de cuatro |
| d | la norma del encabezado no se emite aparte | cuatro de cuatro | cuatro de cuatro |
| e | sin relación de sujeto si el texto no lo nombra | uno de cuatro | tres de cuatro |
| el ejemplo | ver §5 | uno de dos | uno de dos |
| f | ver §9 | ninguno de uno | uno de uno |

- **a.** El brazo P3c falla dos veces por la misma vía. En `cap::11.4` registra como `meta_normativo` «A los efectos de
  la determinación de la RPC», que por la prueba del prefijo es alcance. En `ext::13.1.4` extrae bien el régimen de
  transición, pero registra el encabezado heredado de 13.1, una facultad con condiciones.
- **b1 y b2.** Ningún brazo da la forma que pide la regla.
  - En b1, Restriccion en lugar de Excepcion.
  - En b2, las Condicion no nombran la norma exceptuada. El brazo P3c la nombra en una Excepcion compuesta, que la regla
    deja en la unidad del encabezado, porque este tiene unidad propia.
  - En los encabezados, sin Definicion (b1), y la norma y la excepción sin relación válida (b2).
- **c.** El brazo P3c gana en `ext::10.3.6` (una Condicion por supuesto) y pierde en `cap::5.3.1.3` y en
  `cla::6.5.4.5`, donde deja supuestos en la Operacion, la Excepcion o la descripción de la Potestad.
- **e.** Las fallas del brazo anterior son «las entidades», que el texto no nombra. La del brazo P3c es
  «Las participaciones en fondos», que verifica en el texto pero no es un sujeto.

## 5. b. El ejemplo

| Unidad | Lo que se espera | Anterior | P3c |
|---|---|---|---|
| `cla::5.1.1::intro` | la Definicion de alcance | no: una Operacion, y la frase entera como `meta_normativo` | **sí**: Definicion «Cartera comercial — alcance» |
| `cla::5.1.1.1` | la Excepcion | sí | **sí** |
| | la Operacion de clasificar | sí («Inclusión en cartera comercial») | **sí** |
| | una Condicion por cada condición | sí (monto y repago) | **no**: solo el repago; el monto va como umbral de la Excepcion |

Además, en el brazo P3c el `exceptua` de la Excepcion hacia la Operacion se rechaza por la firma, y la unidad registra
como `meta_normativo` el encabezado heredado («Abarca todas las financiaciones comprendidas, con excepción de las
siguientes:»). Con este resultado, la autora decide la condición 10 de la tanda 1.

## 6. c. Normas con relación de sujeto

| | Normas con `aplica_a` (en el crudo) |
|---|---|
| Referencia de P4, prefijo sellado | 129 de 143 |
| Referencia de P4, prefijo de P3b-2 | 111 de 157 |
| P4b, brazo anterior | 36 de 54 |
| P4b, brazo P3c | 19 de 42 |

- La referencia se reproduce con la misma cuenta (`analisis_p4b.py`, `normas_con_sujeto`).
- **Menciones de sujeto en la salida validada:** en el brazo P3c verifican las 26. En el brazo anterior no verifican 10
  de 45: «las entidades» o «los bancos», que el texto no nombra.
- **Menos normas en el brazo P3c:** 12 Obligacion contra 18, 22 Restriccion contra 27 y 8 Potestad contra 9. Parte son
  deberes que pasa a Operacion (`cap::6.3.2::intro`, el canje de `cap::6.3.2.1`) o deja dentro de una Condicion
  (`ext::10.4.2.5`).

## 7. d. El contador de omisiones `meta_normativo` (primera medición fuera de muestra)

Con el validador de `bb212f1`, en los dos brazos (`analisis_p4b.json`, `resumen`; lectura en `marcas_p4b.json`).

| | Anterior | P3c |
|---|---|---|
| Omisiones `meta_normativo` | 10 | 12 |
| Con marca | 6 | 7 |
| deber / prohibición / facultad | 0 / 1 / 1 | 1 / 1 / 2 |
| condición / excepción / alcance | 2 / 2 / 1 | 2 / 1 / 2 |
| modalidad (opción / consejo / forma) | 1 (0 / 0 / 1) | 0 (0 / 0 / 0) |
| Solo por la subclase forma | 0 | 0 |
| Con el tramo solo en el texto heredado | 5 | 6 |

- **Lectura:** las 10 y las 12 son contenido normativo, con dos lecturas dudosas en cada brazo: el cuantificador
  «enumeradas taxativamente» y una remisión de aplicabilidad temporal en `ext::10.3.6`.
- **Sin falsos positivos, con faltantes:** las 6 y las 7 marcadas son normativas. Quedan sin marca 4 normativas en el
  brazo anterior y 5 en el de P3c. Las formas que se escapan:
  - «requerirá» sin «se»;
  - «A los efectos de»;
  - «no valdrá como»;
  - «o en su defecto»;
  - «en el marco de lo previsto en»;
  - «con más el porcentaje»;
  - «enumeradas taxativamente».
  P4b no edita código: lo dejo para decidir.
- **Prohibición y facultad** dan sus primeros casos fuera de muestra (1 y 1, y 1 y 2), todos normativos. Consejo no
  aparece. Forma aparece una vez (`ext::4.1.4.7`, «en forma directa o indirecta»), junto con una condición.
- **El brazo P3c no registra menos `meta_normativo`** (12 contra 10). Seis de sus 12 copian texto heredado de un
  encabezado o un cierre, que P3C-a6 dice no registrar.

## 8. e. Salida

| | Anterior | P3c |
|---|---|---|
| Tokens de salida (27 unidades) | 45.855 | 40.626 |
| Por carácter de texto propio (22.166 caracteres) | 2,069 | 1,833 |
| Mediana por unidad | 1.318 | 1.274 |

P3c sobre anterior: salida 0,886; entrada sin caché 1,026. Lo uso en §10, como cota: las unidades se eligieron por
lectura.

## 9. f. `cap::6.2.2.6`

- **Brazo P3c:** no copia ninguno de los porcentajes de `cap::tabla037` que no están en la prosa (40 %, 30 % y 100 %), y
  declara la omisión `tabla`.
- **Brazo anterior:** los copia en la descripción y en los umbrales. En su release la tabla no estaba forzada a residual.

## 10. g y h. La llamada del techo completo y el costo

- **g** (`p4b/salida/escalon3_p4b.json`): la API aceptó `max_tokens` 40.960.
  - Unidad: `ctacte::3.2.4`, la más corta, por el cliente con transmisión (pasa el límite de 21.333).
  - `stop_reason` «tool_use»; usage: 1.058 de entrada, 582 de salida y 27.840 leídos de la caché, sin escritura.
  - USD 0,0068.
- **h:** costo real en §3. **U-REEXT-T0 con la salida medida** (`costo_p4b.json`) es la re-estimación de P4 con el
  prefijo de P3c y los cocientes de P4b encima:

| Base de P4 | Central | Con el tercer escalón | Con el escalón máximo, ×1,4 |
|---|---:|---:|---:|
| salida sin ponderar | 47,49 | 47,85 a 48,45 | 67,83 |
| salida ponderada por estrato | 43,85 | 44,21 a 44,81 | 62,74 |

El tope de USD 72 alcanza. Con un reintento del ratchet al techo, el peor caso del escalón da 49,52 y 45,88.

## 11. La pata de E3 (las NOTAS nuevas)

- `ctacte::3.2::intro`, `cla::5.1.1::intro`, `ext::13.1.4` y `ext::6.1.1`: `completo_ok` directo.
- **`ext::3.5.3::intro`: `aceptado_tras_reintento`.** E3 señaló que el extractor declaró como `meta_normativo` la
  exigencia de conformidad previa y que «no lo es» (la NOTA de las omisiones). El reintento la recuperó como Potestad y
  quedó un residual de severidad media: la carga sobre el deudor. La marca `reintento_con_menos_elementos` pasó de 8 a 5
  entidades.
- **En `ext::13.1.4`, E3 no señaló** la omisión del encabezado heredado (una facultad con condiciones).

## 12. Controles

`p4b/salida/control_p4b.txt`, con el script de control en el paquete.
- **Doble corrida** de los 5 scripts de USD 0 (selección, proyección, análisis, marcas y costo) sobre una copia sin
  enlaces de `bb212f1` con `p4b/` del repo. Las 7 salidas son iguales entre corridas y a las de `p4b/salida/`. La
  selección se reproduce desde el repo con el mismo sha256.
- **El repo** no cambió durante el control (12.899 archivos) ni durante la corrida con API. En ese lapso cambiaron
  solo dos scripts que escribí en `p4b/`.
- **`.pyc`:** sin nuevos.
- **Escrituras:** `p4b/` (6 scripts, `seleccion_p4b.md` y `salida/` con 16 archivos más `pata_e3/`) y este freno. Ningún
  código del pipeline.

## 13. Para la autora

- **La condición 10 de la tanda 1** se decide con §5. El brazo P3c da la Definicion de alcance y, en el ítem, la
  Excepcion y la Operacion de clasificar, pero una sola de las dos Condicion.
- **`ctacte::3.2` como b1:** decidir si cuenta o si b1 queda solo con el ejemplo.
- **El contador:** las siete formas que se escapan (§7), y si se suman.
- **Hallazgos para un ajuste del prefijo,** si lo hay:
  - el brazo P3c sigue registrando como `meta_normativo` contenido normativo, sobre todo el texto heredado de
    encabezados (6 de 12) y el alcance con «A los efectos de»;
  - b1 y b2 no salen en ningún brazo con la forma de la regla;
  - c empeora en dos de cuatro unidades.
- **El error propio** del encabezado: la nota sobre `599b304` en `freno_p3c2_modalidad.md`.
- **PENDIENTE:** la revisión de la lectura asistida y el commit de P4b.
