# U-REVISION-LIBRE — FRENO B1: cruce de los hallazgos de gravedad 1 y 2

Base: HEAD `20b7f60`, leído desde una copia de lo commiteado; durante el cruce entraron `395fc0b` y `c448e42`, de los que leí el diff (P3 va antes que C2; C2 escribe `salida_tanda0_r2b/`). Crucé los 36 hallazgos (`freno_a.md`, 1.1–1.18 y 2.1–2.18) contra plan, tablero, checklist, backlog, protocolo, mandatos, frenos y el prefijo r2b. La búsqueda la delegué; verifiqué cada cita que uso. Todo número de este freno lo recomputé yo (`cap85.py`, `recomp_umbrales.py`, `recomp_coef.py`, `colas_titulo.py`, `ver_e0b.py`), salvo donde dice [A].

**Clasificación (36).** Ya resuelto: 2.15 para los tres cortes de la tanda 0 (`r4_freno.md:89-93`). Ya declarado: 1.8, 2.5, 2.9, 2.11, 2.17, 2.18. Conocido y pendiente: 1.1 (`tablero:62`, U-REEXT-T0), 1.5 (`tablero:65`, `BKL-0033`), 1.6 (`plan:400`, mandato propio tras U-REEXT-T0), 1.7 y 2.1 (C2 de U-R2-CODIGO-2, puntos a y b), 1.11 (`checklist:129` y `:148`), 1.13 (decisión 16, P3), 1.17 (U-DIAG-VINCULO), 2.12 (U-SEG-OFICIAL). NUEVO entero: 1.2, 1.3, 1.9, 1.15, 1.16, 1.18, 2.2, 2.3, 2.14. NUEVO en parte (el proyecto conoce el mecanismo o un caso, no la regla ni la medida): 1.4, 1.10, 1.12, 1.14, 2.4, 2.6, 2.7, 2.8, 2.10, 2.13, 2.16.

**`cap::8.5.1` a `8.5.3`: el prefijo r2b no lo resuelve, por dos causas.**
1. El mensaje no los marca como ítems. `es_item` pide que el último bloque heredado termine en «:» (`prompt_r2b.py:245-249`), y tras «…límites mínimos:» E0 hereda los párrafos de cierre de 8.5. El punto recibe el rótulo «NO extraigas contenido normativo de estos bloques», y la R30 dice «si el contexto heredado termina en un encabezado así». Qué hace el modelo: NO VERIFICADO, sin API.
2. Aunque componga, la comparación da `no_determinada` con todo tramo que probé, incluido el de dos segmentos «…límites mínimos: […] … 6% por los APR». Deja de ser un `coeficiente` falso; el mínimo no llega al campo.
El punto ciego de `es_item` no es solo de `cap`: el mensaje marca 706 ítems en la tanda 0 y deja sin marcar otros 347 cuyo encabezado «:» va seguido solo de bloques de cierre (`ext` 231, `ctacte` 40, `cap` 36). El proyecto trabaja con los 706 (`plan:398`).

**Pieza 1 — prompt de E1 o de E3, antes de P4.** El prefijo r2b difiere del borrador B en tres líneas (R8 y R30, sobre la Condicion sin `condicion_de`, y R14, sobre la Comunicacion): lo del FRENO A1 vale.
- Mensaje, `es_item`: los 347 ítems (1.2). No toca el prefijo.
- Mensaje del mini-chunk (`prompt_r2b.py:290`): 125 de 376 empiezan a mitad de oración y su primera mitad va rotulada «NO es contenido a extraer» (2.16).
- Prefijo: recomendación tipada como deber, 141 Obligacion en `lingob` (1.3); destino de la consecuencia de un incumplimiento (1.4); conectar la Excepcion cuando la norma está en la misma unidad, 130 de 221 (2.8); alcance en títulos que no terminan en «:» (2.7); lista dentro de una unidad, 1 caso (1.18).

**Pieza 2 — archivos que edita C2 de U-R2-CODIGO-2.**
- `reglas_comparacion.py`: 12 de 79 umbrales de reglas simples son falsos, 10 invertidos por una negación fuera del alcance de la regla y 2 con «igual o superior» como estricto (1.9); 28 de 140 `coeficiente` tienen un comparador pegado a la cuantía (1.10). Son elementos hoy falsos: no chocan con el control de (c). El plazo asumido máximo es regla firmada (1.8); lo nuevo es la medida: por patrón, 63 de 176 no son un máximo y 16 sí.
- `e0_lib.py`, e0-r2: de las 73 «colas de título» que el proyecto contó sin leer (`r2_freno.md:98`), 6 son texto de la norma, todas en `ric` (pp. 15, 30, 54 y 59; `e0_lib.py:644-654`) (2.3). No cambia ids, pero sí el texto de `ric::4.3.1.2`, `ric::6.1.2`, `ric::11.2::intro` y `ric::12.4`: el control de la nota del 04/10 al mandato declara solo el cambio de `ric::4.3.3`.
- También en `e0_lib.py`, pero no para C2: sección escrita de otra forma (1.14: `opecam`, `garopt`, `snp_dd`), rótulos falsos (1.15: `rdbcra`, `ri_niif`, `ri_tsa`, `ri_dsf`) y páginas de norma fuera de toda unidad (2.4: `ri_cc`, `ri_tsa`, `snp_mep`, `venliq`, `fimipyme`). Cambian ids de la partición y chocan con el control de (f); van antes de U-SEG-OFICIAL.
- `r1_referencias.py`: las formas de cita fuera de la tanda 0 (1.7, 2.13) son [A]; no las recomputé y no las uso para decidir.
- `runner_corpus.py`: nada nuevo. 2.2 (25 veredictos con `faltantes` como string, 24 legibles; `ratchet_e3.py:169-172`) y 2.14 (el reintento reemplaza sin comparar; `:422` y siguientes) caen en `ratchet_e3.py`, que no está en la lista de C2.

**Pieza 3 — `validador_r2.py` y lectura del crudo nuevo (P3).**
- `derivar_comunicacion('A-39', …)` devuelve «A» (`validador_r2.py:262-268`): la derivación da por buena una ley escrita como Comunicación (1.12).
- `texto_completo` arma texto propio y después herencia (`:204-207`): un tramo encabezado→ítem o título→cuerpo solo verifica si P3 mira cada segmento por separado (1.2, 2.16).

**Fuera de las tres piezas.** Linaje (2.6) y cuantías en tipos sin `umbrales` (2.10): límite a declarar.

**Errores propios.** En el FRENO A, 2.1, generalicé a las 4 unidades mudas la forma de `ext::6.5.3`; son 2 de 4 (`freno_c1.md:109-112`). En 1.14 di 5 TOs [A]; confirmé 3. En 1.7 di 13 aristas [A]; son 11.
