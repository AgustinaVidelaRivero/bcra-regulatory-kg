# Tabla de resultados de ESQ-3b — PROPUESTA DE MESA (revisión de autora pendiente)

Salida del §6 del pre-registro `prerregistro_esq3b.md` (`01bf046` + Adenda 1
`f1fe0d8`). Insumos: worksheet adjudicado sellado en `a5bdbd4` (43/43, 0
DUDA), extracciones pareadas (`58595bc6…`), selección sellada (`9cb15ecf…`),
desvíos declarados pre-lectura (`desvios_lectura_esq3b.md`). Aritmética
recomputada por mesa desde disco. **Los veredictos por retoque son
propuestos**: la adjudicación de las marcas es de la autora y ya está
sellada; lo que la autora aprueba acá es la agregación y el mapeo
marca→veredicto. Las decisiones que la regla sellada deja abiertas van en
§7, sin resolver.

**Spot-checks (dos, cada uno con su semilla; la marca de la autora manda
en todos los casos).**
— **Mesa**: 8/43 re-leídas (semilla `20260902:spotcheck_esq3b`:
adrei::1.2, adrei::4.1.1.4, ayccef::2.11, expaef::1.1.1, expaef::1.2.1,
opefci::6.3, prevmi::2.3, traval::1.1.1.1) — **0 discrepancias formales**;
una observación registrada en la fila R3 de §2.
— **Mesa revisora**: 8/43 re-leídas (semilla
`20260903:spotcheck_mesa_revisora_esq3b`: expaef::1.2.1, opefci::2.1,
opefci::1.3, lavdin::3.3.5, prevmi::1.2, ctacor::1.2::cierre,
ayccef::5.2.4.4, prevmi::2.3) — **0 discrepancias, acuerdo pleno**;
conteos mecánicos reproducidos exactos (q2 global 21/16/6; regresión
8/13/5; objetivo 13/3/1; q3 3/13/27); **citas de q2/q3 verificadas contra
el texto fuente en las 43** (los no-match automáticos eran guiones de
corte de línea y comillas anidadas; inspección manual sin fabricaciones).

**Notas de instrumento y registro (verificadas por mesa revisora).**
(i) El campo `que_cambio` de expaef::1.1.1 contiene un volcado del render
de la propia ficha (~4 KB, bug de pegado del instrumento); marcas y demás
campos intactos, sellado así en `a5bdbd4`. **El arreglo del bug de pegado
entra como prerrequisito de la próxima lectura.** (ii) La anotación de
conocimiento previo en las observaciones de las cinco fichas del desvío
(b) no se hizo durante la lectura; lo cubre el desvío declarado
pre-lectura (`desvios_lectura_esq3b.md`), consta como nota.

## §1. Resumen global por brazo

| brazo | n | q1 cambió | q2 fidelidad (mejora/igual/empeora) | q3 migración (no_hay/correcta/incorrecta) |
|---|---|---|---|---|
| objetivo | 17 | 17 sí / 0 no | 13 / 1 / 3 | 5 / 12 / 0 |
| regresión | 26 | 21 sí / 5 no | 8 / 5 / 13 | 22 / 1 / 3 |
| total | 43 | 38 / 5 | 21 / 6 / 16 | 27 / 13 / 3 |

(DUDA: 0 en las tres preguntas.)

## §2. Brazo OBJETIVO — veredicto por retoque (predicciones selladas del §2 del pre-registro)

| retoque | predicción | mecánico | marcas de la autora | veredicto propuesto |
|---|---|---|---|---|
| **R1** Potestad | f. 26 produce Potestad; f. 15 facultad deja Obligacion→Potestad | ✓ / ✓ | f. 26 (`opefci::6.3`) mejora+correcta; f. 15 (`ctacor::1.1`) mejora+correcta | **objetivo: PASA · regresión: SE REVISA** (atrajo 1 vez, §3; regla sellada) |
| **R2** Condicion + `condicion_de` | f. 39 produce Condicion, no deber autónomo | ✗ (sigue Obligacion; sin Condicion; agravante: se lava con `requisito_de_estructura`) | f. 39 (`lavdin::3.3.4.3`) empeora, con causa diagnosticada en la ficha | **NO PASA su principal** — la caja funciona en otras unidades (f. 44, ayccef::2.11, expaef::1.1.1, opefci::6.3) pero no donde fue diseñada |
| **R3** Definicion | f. 25 y f. 46 producen Definicion con término; contraste f. 37: atesoramiento SIGUE en Operacion | ✓ / ✓ / ✓ literal (la Operacion sigue) | f. 25 (`adrei::1.3.1`) mejora+correcta; f. 46 (`cryl::1.2`) mejora+correcta («paga en navegabilidad real») | **objetivo: PASA · regresión: SE REVISA** (atrajo 2 veces, §3; regla sellada). **Agujero de la delimitación no cubierto por la predicción** (verificado por mesa y mesa revisora en el jsonl): en f. 37 (`traval::1.1.1.1`) la extracción nueva conserva la Operacion — la predicción de contraste PASA mecánicamente — Y emite además una Definicion sobre el mismo contenido, que la delimitación sellada excluía y que la autora adjudicó correcta contra el texto, con la **duplicación entre cajas como mecanismo**. El conflicto delimitación-vs-adjudicación es el insumo central de la decisión (b′) de §7 |
| **R4** regla de omisión | f. 46 y f. 19 no generan nodo prescriptivo | f. 19 ✓ (omisión total; adjudicada mejora: «una representación vacía no puede ser infiel y la vieja lo es en cuatro puntos») / f. 46 ✗ (la cláusula interpretativa salió otra vez como Restriccion-prohibición) | f. 19 mejora; f. 46 mejora (por R3, pese al residuo R4) | **PASA 1 de 2** — decisión abierta §7(e) |
| **R5** partición (sin tipo nuevo) | f. 63 revocación → Potestad; f. 38 prohibitivas siguen Restriccion | ✓ / ✓ | f. 63 (`ayccef::2.11`) mejora+correcta («el uso más extenso del vocabulario nuevo… ninguna caja forzada»); f. 38 (`ctacor::1.2::cierre`) empeora por causas ajenas a R5 (RE mal aplicado, §5) | **PASA** |
| **R6a** `exceptua_operacion` | f. 44: las 3 Excepcion lo emiten hacia las 3 Operacion | ✗ (0 emisiones en las 43; la unidad ancla se reestructuró vía R2: 3 Excepcion + 1 Condicion + 3 `condicion_de`, sin Operacion) | f. 44 (`lavdin::3.3.5`) igual+correcta — la autora adjudicó la estructura alternativa como «tercer caso completo de caja nueva + relación nueva + destino correcto» | **NO PASA su predicción** — decisión abierta §7(c): la necesidad que lo motivó quedó cubierta de otro modo en su ancla |
| — corroboración R6a (fila aparte, NO cuenta para el veredicto — Adenda 1 §3) | f. 62 y f. 65 | — | f. 62 (`actgar::1.3.1.1`) mejora+correcta; f. 65 (`actgar::2.3.5`) mejora+correcta | corroboran la dirección, sin peso |
| **R7** `descripcion` en Operacion | f. 32: el atributo se aloja en la descripcion de la Operacion | ✗ literal (la unidad se reestructuró: la delegación es ahora Potestad; no quedó Operacion) — colateral ✓: la Operacion de f. 37 y la de f. 26 llevan descripcion | f. 32 (`expaef::9.1`) mejora+correcta («mejor caso del retoque») | **NO PASA literal / cumplida en espíritu** — decisión abierta §7(d) |
| **R8** dominio de `aplica_a` | las `aplica_a` descartadas se emiten válidas (4 unidades) | por unidad: `ayccef::1.1.1.2` ✓ (emite desde Operacion); `expaef::1.1.1` cubierta por reestructuración (el contenido migró a Potestad y la `aplica_a` sale de ahí); `expaef::9.1` ídem; `opefci::2.1` ✗ (extracción nueva VACÍA — la unidad aporta cero) | 3 mejora+correcta / `opefci::2.1` **empeora** (omisión total de contenido habilitante) | **PASA 3 de 4** — el caso fallido es vaciamiento, no firma: cruza con §4 (hipótesis R4) |
| **R9** enum | f. 67: el reporte a la SEFyC no vuelve a `comunicacion_a_cliente` | ✓ (5/5 `presentacion_informativa`) | f. 67 (`ayccef::5.2.4.4`) mejora | **PASA su predicción, con matiz**: el valor emitido en f. 67 es `presentacion_informativa` (la predicción solo exigía no-`comunicacion_a_cliente`); la ÚNICA emisión de `reporte_al_supervisor` está en `lavdin::1.3.1::intro` (regresión). El matiz acompaña al 5/10 de `requisito_de_estructura` (§5): decisión abierta §7(f) |

## §3. Brazo REGRESIÓN — veredicto por la regla sellada

**FALLA formal**: 3 migraciones a caja nueva adjudicadas incorrectas
(umbral: ≥1). Atribución verificada por mesa en las extracciones:

| unidad | atrajo | retoque | ficha ESQ-2 | ¿conocida (desvío b)? | ¿contaminada (desvío a)? |
|---|---|---|---|---|---|
| `actgar::1.3.1::intro` | Potestad («Exención de previa autorización») | **R1** | f. 61 | SÍ | no |
| `prevmi::1.2` | Definicion («Financiaciones comprendidas…») | **R3** | f. 40 | SÍ | no |
| `actgar::2.11.3` | Definicion («Activos afectables…») | **R3** | f. 20 | SÍ | no |

La cuarta unidad de regresión con tipo nuevo (`opefci::7.2.3`, Condicion)
fue adjudicada **correcta**. Las 2 unidades contaminadas del desvío (a) —
`lavdin::1.1::intro` (mejora, sin migración) y `ayccef::3.4.1` (igual, sin
migración; ambos brazos vacíos) — **no migran ni empeoran por migración**:
la contaminación no interviene en la falla.

**REGLA SELLADA aplicada**: «si el brazo de regresión falla, el retoque se
revisa aunque el objetivo pase» → **R1 y R3 SE REVISAN** (delimitación,
re-sellado de predicción, re-corrida de sus pares bajo el mismo tope;
remanente USD 0,7529). El alcance de esa re-corrida es la decisión abierta
§7(a).

**Diagnóstico disponible para la revisión** (de las fichas de la autora):
para R1, la hipótesis falsable del par f. 17/f. 18 — «Potestad podría estar
disparándose por LÉXICO de autorización y no por la modalidad deóntica»
(mismo vocabulario, polaridad opuesta, misma caja) — que la falla de
`actgar::1.3.1::intro` («no requiere» → Potestad) confirma en dirección.
Para R3, las dos fallas son encabezados con forma definitoria sobre
contenido no definitorio: la delimitación necesita la cláusula «que el
CUERPO defina, no que el encabezado lo sugiera».

### §3.b Doble tabla de sensibilidad — CON ADVERTENCIA

| escenario | incorrectas | veredicto regresión |
|---|---|---|
| completa (26) | 3 | FALLA |
| sin las 5 conocidas del desvío (b) | 0 | (pasa) |
| sin las 2 contaminadas del desvío (a) | 3 | FALLA |

**ADVERTENCIA EXPLÍCITA (fijada por la autora): la fila «sin las 5» es
vacía POR CONSTRUCCIÓN.** Las otras 22 unidades de regresión no emitieron
ningún tipo nuevo (verificado por mesa desde el jsonl) y por lo tanto no
podían migrar: excluir las conocidas excluye exactamente las unidades donde
la migración ocurrió, porque se las conocía POR haber migrado (conocimiento
y resultado comparten causa). Esa fila NO es evidencia de que la regresión
pase: **el peso de la evidencia son los fundamentos textuales de la
autora**, que son específicos y citables en las tres fallas. La regla 2 del
desvío (b) se cumple: la falla se detectó en fichas no ciegas y este laudo
lo declara a la vista.

## §4. Fidelidad en regresión (métrica NO sellada — sección informativa)

8 mejora / **13 empeora** / 5 igual. Sin línea de base del ruido de
re-extracción (P1″), la tasa no es atribuible per se; las conductas, una
por unidad (etiqueta desde las observaciones de la autora):

| unidad | nodos viejo→nuevo | conducta anotada |
|---|---|---|
| `actgar::1.2` | 7→6 | `aplica_a` malformada (sujeto_id y target a la vez) |
| `actgar::1.3.1::intro` | 1→1 | migración aislada R1 (la incorrecta de §3) |
| `actgar::2.11.3` | 3→1 | migración R3 + pérdida de salvedad (límite de esquema anotado: Definicion sin campo para salvedades) |
| `ayccef::4.3::intro` | 2→1 | inversión de criterio sobre el mismo valor de enum |
| `ayccef::5.1.1` | 1→1 | sobre-aplicación de `requisito_de_estructura` (constancia documental ≠ estructura) |
| `cryl::1.3` | 6→5 | doble regresión en properties.tipo (pierde `asignacion` apto, gana RE mal aplicado) |
| `cryl::4.1` | 2→1 | sujeto gramatical tomado como sujeto normativo |
| `cryl::8.1` | 2→1 | campo estructurado llenado con contenido de otra semántica |
| `ctacor::2.2::intro` | 2→2 | sobre-aplicación de RE (condición de elegibilidad ≠ estructura); mejora estructural anotada aparte |
| `expaef::9.6.2` | 1→1 | RE afirma clase que el texto no sostiene («otra» no afirmaba nada) |
| `opefci::7.2.3` | 2→3 | empeora por otros ejes; el cableado nuevo correcto anotado a favor |
| `prevmi::1.2` | 3→2 | migración R3 (la incorrecta de §3) |
| `traval::3.1` | 3→3 | tipado inconsistente de contenidos paralelos; décima RE «del lado equivocado» |

**Cruce con la regla 9 (R4) — hipótesis «el brazo nuevo se vacía en
unidades no prescriptivas», verificada unidad por unidad**: extracciones
nuevas VACÍAS (solo TO): 5 en total — 2 con vieja también vacía (ambos
brazos: `adrei::4.3.1::intro`, `ayccef::4.2.7.2` — chapeaux ya vacíos en
ESQ-2, no atribuible al retoque; también `ayccef::3.4.1`) y **2 vaciamientos
nuevos**: `adrei::1.2` (finalidad — R4 operando como se diseñó, adjudicada
MEJORA) y `opefci::2.1` (habilitación de entidades — adjudicada EMPEORA:
R4 se llevó contenido habilitante que Potestad debía capturar). La
hipótesis se sostiene en dirección (ambos vaciamientos son unidades no
conductuales) con un caso a favor y un caso en contra: **R4 y R1 compiten
por el contenido habilitante**, insumo directo de §7(e).

## §5. `requisito_de_estructura` — las 15 emisiones, contra las notas de la autora

Clasificación de mesa desde los campos de la autora (auditable: cada fila
cita su ficha); **5 avaladas / 10 objetadas / 0 sin pronunciamiento**:

- **AVALA (5)**: `adrei::2.1.2::intro` ×2 («agrega información correcta
  donde la vieja no aportaba ninguna»), `adrei::4.1.1.4` (dentro de una
  ficha mejora), `expaef::9.1` ×2 (requisitos de forma jurídica y sede).
- **OBJETA (10)**: `ayccef::5.1.1` (constancia documental), `cryl::1.3` ×2
  (regresión desde `asignacion`, que describía bien), `cryl::4.1` («del
  lado equivocado del criterio»), `ctacor::1.2::cierre` (aprobación por el
  órgano de gobierno — «un cuarto tipo de cosa»), `ctacor::2.2::intro`
  (condición de elegibilidad), `expaef::1.1.2.4` («afirmación falsa» sobre
  requisito de autorización previa), `expaef::9.6.2` («afirma una clase que
  el texto no sostiene»), `lavdin::3.3.4.3` (lava la deformación de R2),
  `traval::3.1` («la más significativa para el laudo»).

Lectura de mesa, sin adjudicar: el valor discrimina bien su clase nuclear
(disponer de políticas/procesos/sistemas/forma jurídica) y **sobre-aplica
2:1 fuera de ella** (constancias, condiciones de elegibilidad,
aprobaciones, autorizaciones previas) — el patrón exacto contra el que se
rechazó `cumplimiento_normativo`. Con `reporte_al_supervisor` no hay señal
equivalente (1 emisión, avalada por contexto). Decisión abierta §7(f).

## §6. Hallazgos transversales de la lectura (para el laudo, más allá de los retoques)

1. **Las dos mitades del retoque**: «el vocabulario de nodos se adopta con
   bastante consistencia y el de relaciones no» (cinco conductas distintas
   frente a las relaciones nuevas, catalogadas por la autora). El caso
   f. 26: Potestad y Condicion correctas, cableadas con la relación VIEJA
   (`condiciona`) al destino equivocado.
2. **Riesgo de fusión de nodos TO al ensamblar**: el brazo nuevo rotuló el
   TO de expaef con el nombre exacto de OTRO TO real («Exterior y
   Cambios», 3 variantes) y el de prevmi con la materia de otro
   («Clasificación de deudores»). Si el ensamblado unifica por rótulo, dos
   TOs se funden. → B5 (ensamblado del escalado) con entrada trazable.
3. **Duplicación de contenido entre cajas** (5 casos): al elevar contenido
   a caja nueva, el brazo nuevo lo copia en vez de repartirlo — tres nodos
   con el mismo texto y ninguno autoritativo (f. 37: el texto de la unidad
   escrito tres veces).
4. **Efecto reproducible a favor**: la Operacion deja de ser huérfana del
   TO en el brazo nuevo (4.º caso anotado) — ataca los 8/213 huérfanos de
   ESQ-2.
5. Candidato a verificación mecánica $0 (propuesta de la autora en ficha):
   conteo de nodos Obligacion por unidad en ambos brazos — la vieja
   multiplica deberes al partir complementos coordinados; la nueva no.

## §7. DECISIONES ABIERTAS PARA LA AUTORA (la tabla no las resuelve)

- **(a) Alcance de la re-corrida de R1/R3** tras el ajuste de delimitación:
  ¿solo las unidades que fallaron + sus principales, o un brazo de
  regresión fresco? Caveat de circularidad: re-correr SOLO las unidades que
  motivaron el ajuste mide que el parche tapa el caso conocido, no que no
  atraiga en otro lado; la ventana de la tanda 1 de B6 queda como test de
  generalización de lo que esta re-corrida no cubra. Presupuesto: 0,7529
  del tope.
- **(b′) Delimitación de R3 ante la f. 37** (del spot-check de mesa +
  verificación de mesa revisora): al revisar R3, la autora decide si la
  delimitación SE MANTIENE (los actos definidos no van a Definicion, y la
  emisión de f. 37 cuenta como sobre-emisión a corregir) o SE AJUSTA (una
  definición de término de un acto es legítima, siempre sin duplicar el
  contenido entre cajas). La adjudicación `correcta` de la ficha y la
  delimitación sellada no pueden quedar ambas en pie sin esta decisión.
- **(b) R2**: no pasó su principal con causa diagnosticada (la unidad es
  condición-de-excepción cross-unidad; la caja funcionó en condiciones
  intra-unidad). ¿Se revisa la definición, se re-ancla la predicción, o se
  acepta con alcance reducido (condiciones intra-chunk)?
- **(c) R6a**: 0 emisiones y su ancla cubierta por una estructura R2 que la
  autora adjudicó correcta. ¿Re-anclar la predicción a otra unidad,
  mantener el predicado en el esquema sin predicción cumplida, o
  rechazarlo (la matriz queda sin Excepcion→Operacion)?
- **(d) R7**: predicción literal no cumplida porque la unidad ancla se
  reestructuró para mejor; el campo funciona donde hay Operacion. ¿Se da
  por cumplido en espíritu con la evidencia colateral, o se re-ancla?
- **(e) R4 parcial**: pasó en finalidad (f. 19) y falló en cláusula
  interpretativa (f. 46); además compite con R1 por contenido habilitante
  (`opefci::2.1`, §4). ¿Se refuerza la regla, se acota su enumeración, o se
  acepta parcial con el residuo declarado?
- **(f) [EMERGENTE de esta tabla — la autora puede tacharla]
  `requisito_de_estructura`**: sobre-aplicación 2:1 fuera de su clase
  nuclear (§5). ¿Se afina la definición del valor en el enum (mismo
  tratamiento que la delimitación de R3), se acepta con el ruido declarado,
  o se retira el valor?

## Reproducibilidad

Todos los números se recomputan desde `worksheet_pareado_esq3b.json` +
`seleccion_brazos_esq3b.json` + `pareado_esq3b.jsonl` (marcas cruzadas con
brazos y `mapa_ficha_retoque`; conteos de tipos/valores desde el jsonl).
Verificación cruzada mesa/disco: coincidente en la totalidad.
