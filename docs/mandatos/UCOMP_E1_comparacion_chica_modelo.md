# Mandato U-COMP-E1 — comparación chica del modelo de E1 antes de la tanda 1

**VERSIÓN PARA FIRMAR (06/10/2026) — PENDIENTE DE FIRMA DE LA AUTORA.** Re-redacción del borrador postergado P6 de U-PROMPT-R2
(`docs/mandatos/UPROMPT_R2_P6_exploracion_modelo_E1.md`, 05/10/2026), por decisión de la autora del 06/10/2026: la comparación se
adelanta antes de la tanda 1, acotada a las dos fallas mayores que dejó T4 de U-REEXT-T0 y a unidades ya leídas, con un gasto de API
de hasta USD 25. Toda llamada al modelo respeta `docs/decisiones_caching_extraccion.md` (cinco decisiones vinculantes).

QUÉ PREGUNTA. Con el prefijo congelado de la release r2b (`322c5a23e9b7`) y `claude-haiku-4-5` a temperatura 0, T4 midió dos fallas
(`data/experiment/reext_t0/reporte_u_reext_t0.md` §2, `0a3ac81`; `t4/salida/tasas_t4.json`, `889b2f9`): (1) el supuesto de una norma
casi nunca sale como Condicion con su relación hacia ella: 43 de 137 supuestos (Wilson al 95 % [0,242; 0,396]), 77 dentro de la norma;
(2) las omisiones `meta_normativo` tienen contenido normativo: 19 de 30 sin marca del contador y 27 de 30 con marca (46 de 60 leídas),
entre 400 y 525 en el tramo propio de la tanda 0. La pregunta es si esas fallas son del modelo o del diseño: ¿un modelo más grande, con
el mismo prefijo y un pedido adaptado, las corrige?

QUÉ NO DECIDE. El modelo de E1 de la release r2b sigue siendo `claude-haiku-4-5` con temperatura 0 (decisión de la autora del 05/10/2026,
`1d8fe9f`; plan `:400`). Esta unidad mide y aplica el criterio de abajo; si un brazo cambia el cuadro, la autora abre, aparte, la
decisión de una release nueva con sus costos; si ninguno lo cambia, las dos fallas se declaran límite del diseño con las cifras de los
tres modelos. El experimento completo de B6.4 (plan `:778`) queda para después del escalado.

LÍNEA DE BASE. `claude-haiku-4-5`, perfil r2b, con las salidas de U-REEXT-T0 (`corpus_tanda0/salida_r2b/`, bases selladas) y las lecturas
de T4 adjudicadas por la autora (`04cec96`, `c9d4c40`): no se paga de nuevo ni se vuelve a leer.

UNIDADES. Las 87 unidades ya leídas en T4: las 30 del grupo c (`t4/salida/fichas_punto7_grupo_c.json`, `mas_de_un_supuesto`; 137
supuestos clasificados) y las 59 unidades de las 60 omisiones leídas (`fichas_punto8_omisiones.json`; dos unidades están en los dos
grupos). Por TO: cap 15, cla 13, ctacte 7, ext 29, lingob 7, pagjub 2, polcre 3, pro 4, ric 7. Lista sellada en `comp_e1/unidades.json` con su sha256 en C0.

BRAZOS (los de P6, sin el brazo F). En los dos: el prefijo de la release r2b con su punto de caché, el mismo mensaje por unidad que armó
E1 en U-REEXT-T0 (perfil r2b, E0 r2b de `salida_tanda0_r2b/`), el mismo tool schema (sin `strict`), dos corridas en S y una en O (para caber en el tope; ver COSTO y la decisión 3 al
firmar), cada una en su base propia y en un namespace que no es el del pipeline.

| brazo | modelo | qué cambia del pedido de E1 (los modelos nuevos rechazan el pedido de r2b tal cual; P6, consulta del 05/10/2026) | corridas |
|---|---|---|---|
| H | `claude-haiku-4-5` | nada; las salidas de U-REEXT-T0, sin pagar | 1 (la de r2b) |
| S | `claude-sonnet-5-5` | sin `temperature`; `tool_choice` `auto`; `thinking` `between_tools`; `max_tokens` 16.384 | 2 |
| O | `claude-opus-5-5` | sin `temperature`; `tool_choice` `auto`; `output_config.effort` `low`; `max_tokens` 16.384 | 1 (2 si el tope sube a USD 35; decisión 3) |

Reglas del pedido, como en P6: si corta, un reintento a 40.960 con transmisión; respuesta sin llamada a la herramienta o mal formada, un
solo reintento igual en un namespace aparte; cada corte, reintento y rechazo se registra; lo que se compara es «modelo más pedido». E3:
la primera verificación del verificador vigente (`claude-sonnet-5`, prompt de E3 sin cambios), sobre cada salida de S y O, sin el ciclo de
reintentos.

MEDICIONES, por brazo y por corrida, sobre las mismas fichas de T4:
M1. Los 137 supuestos del grupo c, clasificados con las cinco clases de T4 (Condicion con su relación hacia la norma; dentro de una
    norma; fusionado; omitido; sin relación), por el mismo lector y con el mismo criterio con que se clasificaron las salidas de Haiku.
M2. Las 46 omisiones normativas de T4 (y las 14 no normativas, aparte), en cuatro clases: extraída como contenido tipificado con tramo
    verificado por E3; extraída sin tramo verificado; registrada otra vez como omisión (con su categoría); ausente.
M3. Variación entre corridas en S (dos corridas): unidades iguales byte a byte con la misma clave; en O solo si tiene dos corridas, si no
    se declara no medida. Cortes, respuestas sin herramienta y rechazos, en los dos brazos.
M4. Veredictos de E3 por brazo (completo, bloqueantes, residuales) y costo real por unidad y por brazo, con tokens de entrada y salida.

LECTURA. Fichas por unidad, brazo y corrida con un código y sin el nombre del brazo (cegada en lo que se pueda; se declara qué la
descubre, por ejemplo el estilo). Primera lectura de la instancia; segunda lectura completa de la mesa; adjudicación de la autora
sobre las divergencias, como en T4. Ninguna lectura usa la API.

CRITERIO, ESCRITO ANTES DE CORRER (sellado en C0 con su sha256 y su hora; no se cambia después de la primera llamada paga). Un brazo
«cambia el cuadro» si, en la peor de sus corridas (dos en S; una en O, salvo la decisión 3 al firmar), cumple al menos una:
C1. Condicion con su relación en al menos 113 de los 137 supuestos (límite inferior de Wilson al 95 % ≥ 0,75; Haiku: 43).
C2. Al menos 41 de las 46 omisiones normativas extraídas como contenido tipificado con tramo verificado (límite inferior ≥ 0,75;
    Haiku: 0, por definición).
Si un brazo lo cumple: la autora abre la decisión de una release nueva, con lo que implica (el modelo entra en la clave de caché y en el
pedido: toda la tanda 0 se re-extrae; la reproducibilidad declarada cambia, porque el pedido adaptado no fija temperatura ni fuerza la
herramienta; costo del escalado multiplicado por 2,6 con S o 5,2 con O; enmienda a la decisión del 05/10/2026 y al laudo de release r2).
Si ninguno lo cumple: las dos fallas se declaran límite del diseño en `docs/insumos_escritura.md` §7, con las cifras de los tres modelos,
y B6.4 queda hecho en su parte esencial. M3 y M4 son descriptivos: no entran al criterio.

QUIÉN LO EJECUTA Y CÓMO CONVIVE. Una instancia nueva, en su propia sesión; ni la de S0-2 de U-SEG-OFICIAL ni la de SC1 de U-SINCOLA-T0.
Es la única de las tres que usa la API: necesita la clave en el entorno (no se lee ni se imprime; las otras dos la tienen prohibida).
Escribe solo en `data/experiment/comp_e1/` (código, bases de caché propias, salidas, fichas, frenos) y en su scratchpad. Lee la E0 r2b
(`salida_tanda0_r2b/`, archivos), el perfil y el prefijo (`e1_extractor/`, `prompt_r2/p3c`), las fichas y tasas de T4 (`reext_t0/t4/`),
el verificador de E3 y los generados del catálogo; nunca las bases del pipeline (`salida_r2b/`, solo para leer las claves de Haiku en
C0, en modo solo lectura). No toca `e0_chunking/` (S0-2), `corpus_tanda0/ens_*`, `manifiestos/`, la fixture ni `grafos.py` (SC1 y SC2).
`git status --short` completo al inicio: lo ajeno se lista y no se toca. Copia sin enlaces para toda corrida; `PYTHONDONTWRITEBYTECODE=1`;
2.213 `.pyc` al inicio, declarados si difieren.

COSTO. Estimación con la tarifa observada en U-REEXT-T0 (E1 Haiku 0,010135 y E3 0,010226 por unidad; `0a3ac81`), el factor de tamaño de
las 87 unidades respecto de la media de la tanda 0 (1,78: 2.069 contra 1.165 caracteres completos; son listas largas), los precios por
token de la página de cada modelo (Sonnet 5.5 el doble de Haiku 4.5; Opus 5.5 el cuádruple) y un 30 % más de tokens por el tokenizador
nuevo: cada corrida de E1 cuesta ≈ USD 4,08 en S y ≈ 8,16 en O, y cada verificación de E3 ≈ 1,58. Diseño que cabe en el tope: S dos
corridas (8,16), O una (8,16), E3 tres (4,75): **≈ USD 21,1; con un 15 % de margen por cortes y reintentos ≈ 24,2**. Con O a dos
corridas: ≈ USD 30,8 y 35,4 con margen, fuera del tope autorizado (decisión 3 al firmar). **Tope: USD 25**, con freno duro antes de cada
llamada (presupuesto propio en `data/experiment/comp_e1/presupuesto.json`). Si el control previo (C0) estima más que el tope con el
conteo real de tokens, se frena sin gastar y se propone el recorte antes de seguir.

ETAPAS.
C0. Control previo, USD 0: (a) las claves de E1 de las 87 unidades con el perfil r2b son las de las bases de `salida_r2b/` (lectura
    `mode=ro`); (b) los dos modelos están disponibles para la cuenta, y el conteo de tokens con el pedido adaptado de cada brazo da la
    estimación de costo recomputada (≤ 25 o freno); (c) sellos con sha256 y hora, antes de la primera llamada: la lista de unidades, las
    fichas de T4 que se usan de base, el texto del criterio y el de las reglas de lectura. FRENO C0 (corto; la autora da el «seguí»).
C1. E1 de S (dos corridas) y de O (una, o dos según la decisión 3), en serie, con el freno duro del presupuesto; E3 sobre cada salida. Registro de cortes, reintentos
    y rechazos. Si el presupuesto llega al tope, parada ordenada y freno con lo que haya.
C2. Fichas de M1 y M2 (instancia), M3 y M4 por script. FRENO C2: segunda lectura de la mesa y adjudicación de la autora.
C3. Cifras finales con la adjudicación, criterio aplicado tal cual, tabla por brazo y corrida, costo real. FRENO final.

CRITERIOS DE ACEPTACIÓN. Sellos de C0 anteriores a la primera llamada paga; gasto real ≤ 25 con su desglose; las tres corridas (cuatro con la decisión 3) con su
base y su registro; M1 sobre los 137 supuestos y M2 sobre las 60 omisiones en cada corrida; divergencias de lectura adjudicadas; el criterio
aplicado sin cambios; doble corrida de los scripts de cifras byte a byte; el repo sin cambios fuera de `comp_e1/` (sha256 antes y
después); grep de convenciones.
ESCRITURAS: `data/experiment/comp_e1/` (se crea) y el scratchpad. Paquetes `revision_UCOMP_E1_FRENO_C0/`, `_C2/`, `_C3/` con `manifest.txt`.
PROHIBIDO: tocar el código del pipeline, el prefijo, el mensaje, el tool schema, el perfil, el verificador, las bases del pipeline, los
grafos, la fixture, `grafos.py`, EV2; usar los brazos en cualquier corrida del pipeline; leer o imprimir la clave de la API; commitear.
REQUISITOS: CLAUDE.md §4 (a a l).
DECISIONES DE LA AUTORA AL FIRMAR: (1) el nombre de la unidad; (2) si la lectura se hace cegada con códigos o abierta y declarada;
(3) si el tope sube a USD 35 para que el brazo O también tenga dos corridas (estimación ≈ USD 31 sin margen y 35 con margen; con el
tope de 25, O corre una vez y su variación queda sin medir).
