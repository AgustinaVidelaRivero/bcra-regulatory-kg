# U-REVISION-LIBRE — reporte final (FRENO B)

Revisión independiente del grafo KG-Tanda0-Diez-r2a y de su proceso de construcción, antes del escalado a los 152 TOs. USD 0, sin API ni Neo4j, solo lectura. Fase A a ciegas sobre HEAD `95dfd98`; fase B sobre `20b7f60`, con los diffs de `395fc0b` y `c448e42`. Detalle de cada hallazgo en `freno_a.md`; cruce de las gravedades 1 y 2 en `freno_b1.md`.

## Resumen

1. Encontré 46 hallazgos: 18 de gravedad 1 (afirmación falsa en un campo estructurado), 18 de gravedad 2 (contenido perdido o deformado) y 10 de gravedad 3 (ruido o costo).
2. El cruce contra plan, tablero, checklist, backlog, protocolo, mandatos y frenos los reparte así: 1 ya resuelto, 11 ya declarados, 12 conocidos y pendientes, 10 nuevos enteros y 12 nuevos en parte (el proyecto conoce el mecanismo o un caso, no la regla ni la medida).
3. De 15 preguntas de cumplimiento escritas desde los PDF, el grafo responde bien 8, en parte 2, algo falso 3 y no puede responder 2 (`freno_a.md`). La búsqueda fue una emulación propia de BM25, no el Lucene del agente.

**Lo nuevo que pesa antes de U-REEXT-T0.** Un cambio de prefijo, de mensaje o de lazo de extracción después de re-extraer obliga a pagar otra vez (protocolo entre tandas, §2 y §6); por eso estos van primero.

4. **La composición con el encabezado no alcanza a un tercio de los ítems.** El mensaje marca como ítem solo el punto cuyo último bloque heredado termina en «:» (`prompt_r2b.py:245-249`). Cuando E0 hereda además los párrafos de cierre del padre, el ítem queda sin marca: 347 puntos en la tanda 0, contra 706 marcados. `cap::8.5.1` a `8.5.3`, los límites mínimos de capital, están entre ellos.
5. **Recomendación tipada como deber.** 141 Obligacion de `lingob` salen de unidades que el PDF enuncia como buena práctica. El prefijo r2b no tiene regla para esa modalidad.
6. **Consecuencias de un incumplimiento.** El prefijo dice que no son un límite y no dice dónde van. Hoy se fuerzan en Restriccion; con r2b caerían a `omisiones` y saldrían del grafo.
7. **Excepcion sin instrucción de conectar.** 130 de las 221 Excepcion sin arista tienen la norma en su misma unidad.
8. **Mini-chunks que empiezan a mitad de oración.** 125 de 376; su primera mitad va en una línea rotulada «NO es contenido a extraer».
9. **El lazo de E3.** 25 veredictos con `faltantes` como texto mandan la unidad a la cola aunque 24 se leen; y el reintento reemplaza la extracción sin comparar (18 de 220 quedan con menos entidades).
10. **E0 borra texto de la norma al tope de página.** De las 73 «colas de título» que el proyecto contó sin leer, 6 son norma, todas en `ric`.

**Lo nuevo que es código sobre lo guardado** (se puede aplicar entre tandas, a USD 0).

11. Reglas de comparación: 12 de 79 umbrales de reglas simples son falsos y 28 de 140 `coeficiente` tienen un comparador pegado a la cuantía. El plazo asumido máximo es regla firmada; por patrón, 63 de 176 no son un máximo.
12. `derivar_comunicacion('A-39')` devuelve «A»: una ley escrita como Comunicación pasa la derivación.

**Lo nuevo que la tanda 0 no deja ver.**

13. E0 fuera de la tanda 0: sección escrita de otra forma («Seccón 3.» en `opecam`), rótulos de punto falsos y páginas de norma fuera de toda unidad (`ri_cc` empieza en la p. 49; `fimipyme` pierde su sección de alcance). Cambian ids de la partición: van antes de U-SEG-OFICIAL, no en C2.

**Límites a declarar.**

14. El linaje no está en el grafo: 0 aristas `modificada_por`, y el pie de cada página (versión, Comunicación, vigencia) no pasa de E0. Llevarlo a la procedencia cambia el modelo: lo reporto y no lo recomiendo.
15. 188 nodos tienen una cuantía en la descripción y son de tipos sin `umbrales` (Potestad 24, Definicion 67, Operacion 97). Es decisión de esquema.
16. `cap::8.5`: aun compuesta, la comparación da `no_determinada`. El sentido «mínimos» del encabezado no llega al campo.

**Lo que el proyecto ya tenía.** `cap::1.2` invertido (`BKL-0006`), las 4 unidades mudas y la cita a otra norma leída como interna (C2 de U-R2-CODIGO-2), el reparto de `remite_a` entre nodos (mandato propio tras U-REEXT-T0), el sujeto sin mención (r2b), la fusión por etiqueta (`checklist:129`), los TOs no segmentables (U-NOSEG-LIMITE) y la cola humana (decisión en el FRENO P3).

**Propuestas que cambian el esquema.** Las reporto y no las recomiendo: un tipo para consecuencias o para recomendaciones, `umbrales` en Potestad, Definicion u Operacion, relaciones Potestad–Operacion y Excepcion–Operacion, y campos de linaje en la procedencia.

## Tabla de hallazgos

Cruce: R = ya resuelto; D = ya declarado como límite; P = conocido y pendiente; N = nuevo; Np = nuevo en parte. Cuándo: «antes» = antes de U-REEXT-T0; «entre tandas» = por código, según el protocolo; «límite» = límite declarado. [A] = cifra de una lectura delegada que no recomputé.

| # | Hallazgo | G | Evidencia | Cruce | Dónde se corrige | Cuándo |
|---|---|---|---|---|---|---|
| 1.2 | Ítems que el mensaje no marca; límites mínimos de capital como cálculo | 1 | `prompt_r2b.py:245-249`; 347 puntos; `cap::8.5.1`–`8.5.3`, PDF p. 168 | N | Mensaje de E1 (`es_item`); la comparación, en `reglas_comparacion.py` o límite | Antes (P4) |
| 1.3 | Recomendación tipada como deber | 1 | `lingob::2.1.2`; 141 Obligacion en 102 unidades; partición 181 unidades | N; único rastro: tipo «Recomendacion» rechazado 2 veces (`prueba_crudo_t0.md:70`) | Prefijo de E1 | Antes, o límite |
| 1.9 | Comparación invertida o de borde | 1 | 12 de 79; `ext::4.2::cierre`, `cla::3.4.4` | N | `reglas_comparacion.py` | Antes (C2) o entre tandas |
| 1.15 | Rótulos de punto falsos | 1 | `rdbcra::2.3.1`, `ri_niif::21.526`, `ri_tsa::1.1`, `ri_dsf::10.x` | N | `e0_lib.py` | Entre tandas, antes de U-SEG-OFICIAL |
| 1.16 | Cierre de lista dentro del último ítem | 1 | `pro::1.1.2.7`, PDF p. 3; 1 caso | N | `e0_lib.py` | Medir primero; entre tandas |
| 1.18 | Lista dentro de una unidad | 1 | `pro::3.2.1.3`; 1 de 27 leídas | N | Prefijo de E1 | Antes, o medir en P4 |
| 2.2 | Veredicto de E3 mal formado manda a la cola | 2 | 25 veredictos, 24 legibles; `ratchet_e3.py:169-172` | N | `ratchet_e3.py` | Antes |
| 2.3 | E0 borra renglones al tope de página | 2 | 6 de 73 colas de título; `ric` pp. 15, 30, 54, 59; `e0_lib.py:644-654` | N; el proyecto contó las 73 sin leerlas (`r2_freno.md:98`) | `e0_lib.py` (e0-r2) | Antes (C2); cambia el texto de 4 unidades de `ric` |
| 2.14 | El reintento reemplaza sin comparar | 2 | De 220: 18, 27 y 12; `ratchet_e3.py:422` y siguientes | N | `ratchet_e3.py` | Antes, o límite |
| 3.2 | Tres predicados Obligacion–Operacion sin definición | 3 | `regula` 521, `requiere` 450, `condiciona` 89; 7 `regula` desde Restriccion | N | Prefijo de E1 | Antes, o límite |
| 1.4 | Consecuencia forzada en Restriccion | 1 | `pagjub::2.9.2`, `ctacte::6.5.1`; 4 de 6; 38 de 2.434 unidades | Np; la sanción es concepto fuera de esquema (`plan:545`) | Prefijo de E1 | Antes, o límite |
| 1.10 | «Ponderador» pisa al comparador | 1 | 28 de 140 | Np; un caso anotado (`freno_c1.md:212`) | `reglas_comparacion.py` | Antes (C2) o entre tandas |
| 1.12 | Comunicacion que no lo es | 1 | 11 de 22; `derivar_comunicacion('A-39')` → «A» (`validador_r2.py:262-268`) | Np; el prefijo ya deriva tipo y número | `validador_r2.py` | Antes (P3) o entre tandas |
| 1.14 | Sección escrita de otra forma | 1 | `opecam`, `garopt`, `snp_dd` | Np; el síntoma lo mira la vigilancia (6) (`plan:765`) | `e0_lib.py` | Entre tandas, antes de U-SEG-OFICIAL |
| 2.4 | Páginas de norma fuera de toda unidad | 2 | `ri_cc`, `ri_tsa`, `snp_mep`, `venliq`, `fimipyme` | Np; `ri_tsa` y `fimipyme` registrados (`plan:738`) | `e0_lib.py` | Entre tandas, antes de U-SEG-OFICIAL |
| 2.6 | El linaje no llega al grafo | 2 | 0 `modificada_por`; pie de página fuera de E0 | Np; versionado temporal como trabajo futuro (`plan:243`); tabla de origen sin lector (`plan:401`) | Modelo de procedencia | Límite |
| 2.7 | Alcance en la cadena de títulos | 2 | `docvig::2.1.1.1`; 228 de 2.052 puntos | Np; jerarquía en U-NAV-DISENO (borrador) | Navegación; prefijo | Límite, o antes |
| 2.8 | Excepcion sin la norma que toca | 2 | 221 de 411; 130 con la norma en la unidad | Np; los 221 medidos (`m1_freno.md:145`); otra unidad, en U-DIAG-VINCULO | Prefijo de E1 | Antes |
| 2.10 | Tipos sin `umbrales` | 2 | Potestad 24, Definicion 67, Operacion 97 | Np; decisión de esquema (`checklist:171`) | Esquema | Límite |
| 2.13 | Remisiones que no llegan | 2 | 205 por punto sin nodos (`m1_freno.md:86`); formas fuera de la tanda 0 [A] | Np; «normas de X» ya en C2 | `r1_referencias.py` | Entre tandas |
| 2.16 | Mini-chunks a mitad de oración | 2 | 125 de 376; `prompt_r2b.py:290` | Np; mecanismo anotado (`r3_ajustes_freno.md:12-13`) | Mensaje de E1 o E0 | Antes |
| 3.4 | E3 no conoce las omisiones nuevas | 3 | `lingob::6.1`; 1 unidad | Np; E3 de completitud es diseño | NOTA de E3 | Antes, o medir en P4 |
| 1.1 | Valores de tabla cruzados | 1 | `cap::1.2`, PDF p. 4 | P; `tablero:62`, `BKL-0006` | Re-extracción | U-REEXT-T0 |
| 1.5 | Sujeto por defecto | 1 | 4.026 de 4.086 sin mención | P; `tablero:65`, `BKL-0033` | Prefijo r2b | U-REEXT-T0 |
| 1.6 | `remite_a` repartido entre nodos | 1 | 14.000 aristas, 1.316 pares | P; `plan:400` | `r1_referencias.py` | Mandato propio tras U-REEXT-T0 |
| 1.7 | Cita a otra norma como interna | 1 | `ext::10.4.4`, 11 aristas | P; `freno_c1.md:79-81` | `r1_referencias.py` | C2 |
| 1.11 | Operacion fundida por etiqueta | 1 | 64 con más de una procedencia | P; `checklist:129`, `:148` | E2 | Sin unidad nombrada |
| 1.13 | Datos del TextoOrdenado | 1 | `version` «actual» en 10 | P; decisión 16 (`freno_p2.md:148`) | Código | P3 |
| 1.17 | Indicador tipado como deber | 1 | `cla::6.5.3.10` | P; R30 lo tipa Condicion; vínculo en U-DIAG-VINCULO | Prefijo r2b | U-REEXT-T0 |
| 2.1 | Unidades mudas | 2 | 4 de 2.434 | P; punto (b) de C2, sin reparación determinística | `runner_corpus.py` | C2 |
| 2.12 | Tablas sin serializar a escala | 2 | 22,4 % contra 4,0 % [A] | P; cifras de U-SEG-OFICIAL (borrador) | E0 | U-SEG-OFICIAL |
| 3.3 | Cola humana marcada | 3 | 71 unidades, 291 nodos | P; nota del 04/10 al mandato de U-PROMPT-R2, punto e | Procedimiento | FRENO P3 |
| 3.7 | Mantenimiento | 3 | 969 `remite_a` cruzan de TO | P; `tablero:85`, `plan:401-402` | Procedimiento | U-SUBGRAFO |
| 3.8 | Ids de unidad repetidos | 3 | `adfsp`, `ceninf`, `cirmo3`, `ri_niif` | P; `BKL-0037`, `tablero:70` | E0 | — |
| 1.8 | Plazo asumido máximo | 1 | 176; por patrón, 63 no lo son y 16 sí | D; regla firmada (`plan:396`); la medida es nueva | `reglas_comparacion.py` | Decisión de la autora |
| 2.5 | Fichas fuera de toda unidad | 2 | 2.281 páginas | D; `plan:728`, adenda 2 | — | Límite |
| 2.9 | Relaciones que el esquema no admite | 2 | 1.039 rechazos; 679 admitidos por r2 | D; `plan:749` | Esquema | Límite |
| 2.11 | Fórmulas y subíndices | 2 | «COn1» → «CO» + «n1» | D; `reglas_remisiones_postR3.md:161` | — | Límite |
| 2.17 | TOs sin estructura numerada | 2 | 61 de 152 por otros caminos | D; `r4_freno.md:44`, U-NOSEG-LIMITE | — | Límite; tanda 1 |
| 2.18 | Vigencias sin campo | 2 | 355 nodos con fecha en la descripción | D; `plan:243`, `tablero:68` | — | Límite |
| 3.1 | Operacion.tipo libre | 3 | 1.301 valores en 2.047 nodos | D; `ULISTAS_NOMAP_diseno.md:67` | Navegación | U-NAV-DISENO |
| 3.5 | Costo | 3 | USD 0,0166 por unidad | D; protocolo §6 | — | — |
| 3.6 | Reproducibilidad | 3 | Sin `temperature`; ids por hash del texto | D; `plan:855`, `plan:751` | — | Límite |
| 3.9 | Unidades «n1»; herencia inflada | 3 | `cap::8.2.2::intro`; herencia [A] | D el subíndice; la herencia, no encontrada | E0 | — |
| 3.10 | Roles de TOs ajenos | 3 | 29 de 35 | D; esqueleto del catálogo (`plan:769`) | — | — |
| 2.15 | Cortes de salida | 2 | 3 unidades de `cap` | R (`r4_freno.md:89-93`); nuevo el censo: 77 unidades de 10.981 caracteres o más en 37 TOs | `runner_corpus.py`; E0 | U-SEG-OFICIAL |

## Método y declaraciones

- Fase A: leí el prompt y 27 de 40 unidades sorteadas (semilla 20261003) contra sus nodos; delegué tres lecturas (E0 sobre los 152 TOs en una copia, ensamblado, escala) y recomputé sus cifras principales.
- Fase B: delegué la búsqueda en los registros y verifiqué cada cita que uso. Recomputé las cifras delegadas que pesan en la clasificación (1.8, 1.9, 1.10, 1.14, 1.15, 2.3, 2.4).
- Contaminación de la fase A: el índice de memoria del proyecto y los mensajes de los últimos commits entraron a mi contexto al abrir la sesión; leí `diseno_prefijo_r2.md` §4.3–4.5 y §10. No leí preguntas de EV2 ni de la evaluación final.
- El árbol de trabajo y HEAD cambiaron durante la sesión por otras unidades. No commiteé nada; escribí solo en `reports/u_revision_libre/` y en el scratchpad.

## Errores propios

- FRENO A1: «1 de 28 unidades leídas»; son 27. Corregido.
- FRENO A, 2.1: generalicé a las 4 unidades mudas la forma de `ext::6.5.3`; son 2 de 4 (`freno_c1.md:109-112`).
- FRENO A, 1.14: 5 TOs tomados de la lectura delegada; confirmé 3. En 1.7, 13 aristas; son 11.
- Una cifra de la lectura delegada de escala no se reproduce y no la usé (17 de 24 veredictos sin faltante de severidad alta; mi recuento da 0).
