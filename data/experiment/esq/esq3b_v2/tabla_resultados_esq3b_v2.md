# Tabla de resultados de la VUELTA 2 de ESQ-3b — PROPUESTA DE MESA (revisión de autora pendiente)

Salida del §8 del pre-registro v2 (`40493c9`). Insumos: worksheet adjudicado
sellado en `444b7f9` (27/27, q4 10/10, 1 DUDA), jsonl pareado
(`cb86c627…`), selección sellada (`e5236825…`). Recomputo mecánico de
P1–P14 por mesa desde el jsonl; la adjudicación es de la autora y manda.
**Spot-check de mesa**: 6/27 re-leídas (semilla `20260903:spotcheck_esq3b_v2`:
cryl::1.2, lavdin::3.3.4.3, opefci::2.1, opefci::7.2.1.2, prevmi::2.5.1,
traval::3.1) — **0 discrepancias**; el spot-check de la mesa revisora, con
semilla propia, se reporta aparte.

## §1. Resumen por brazo

| brazo | n | q2 fidelidad (mejora/igual/empeora/duda) | q3 migración (no_hay/correcta/incorrecta) |
|---|---|---|---|
| objetivo | 15 | 7 / 3 / 5 / 0 | 12 / 2 / 1 |
| regresión fresca | 12 | 4 / 3 / 4 / 1 | 10 / 1 / 1 |
| total | 27 | 11 / 6 / 9 / 1 | 22 / 3 / 2 |

q4 (`requisito_de_estructura`): 10/10 adjudicadas — **5 avala / 5 objeta**
(objetivo 3a/2o; fresca 2a/3o). DUDA: 1 (q2 de `ayccef::4.2.9`, empate
declarado entre una afirmación falsa y una verdadera de peso comparable —
listada, no cuenta).

## §2. P1–P14 — recomputo mecánico + adjudicación

| P | unidad | mecánico | adjudicación | lectura |
|---|---|---|---|---|
| P1 | actgar::1.3.1::intro | **PASA** (sin tipo nuevo) | q2 **empeora** | **PASA con asterisco grave: anti-atracción por VACIAMIENTO** — la Potestad espuria no volvió, pero la unidad quedó VACÍA (la base v1 portaba contenido); el parche redirigió a omisión, no a la caja correcta |
| P2 | prevmi::1.2 | PASA | q2 mejora | PASA limpio |
| P3 | actgar::2.11.3 | NO (emite Definicion) | q3 **correcta**, q2 mejora | la predicción cae y la adjudicación aprueba: bajo la delimitación revisada, el cuerpo que da la extensión SÍ define — la predicción era más estricta que la delimitación que la autora terminó aplicando; se resuelve por la marca |
| P4 | opefci::6.3 | PASA | mejora (v1) | re-confirmada |
| P5 | ctacor::1.1 | PASA | — | re-confirmada |
| P6 | adrei::1.3.1 | PASA | — | re-confirmada |
| P7 | cryl::1.2 | PASA (Definicion «cuentas de registro») | q2 **empeora** | la caja sobrevive, el **definiens se truncó a la mitad** — «la estabilidad de la emisión no garantiza la estabilidad de su calidad» (obs. de la autora) |
| P8 | traval::1.1.1.1 | **NO** (Definicion duplicada persiste) | q2 igual, q3 no_hay | la cláusula de no-duplicación NO operó en su caso ancla; sobre-emisión de f. 37 sigue — residuo de R3 |
| P9 | lavdin::3.3.4.3 | **NO** (idéntica a v1: Obligacion + RE) | q1 no, q4 objeta | **dispara la CONDICIÓN DE SALIDA SELLADA**: R2 con alcance reducido (condiciones intra-chunk), f. 39 residuo con destino E3/r2, sin tercera corrida |
| P10 | cryl::1.2 | **NO** (Restriccion-prohibición otra vez) | q2 empeora | segunda falla consecutiva de la regla 9 sobre la MISMA cláusula interpretativa |
| P11 | opefci::2.1 | **parcial** (no vacía ✓; sin Potestad ✗) | q2 **mejora** | la omisión total se revirtió y el contenido habilitante quedó representado por Operacion + `aplica_a` (estructura válida sin Potestad); cumplida en espíritu, a laudo |
| P12 | ayccef::5.1.1 | PASA (sin RE) | q2 mejora | reversión correcta |
| P13 | traval::3.1 | PASA (sin RE) | q2 mejora | reversión correcta + uniformación de paralelos |
| P14 | 3 unidades avaladas | **NO** (adrei 3/3 conservan; expaef::9.1 fusionó 2→1, q4 objeta) | q3 de expaef::9.1: **incorrecta** (obj) | conservación parcial 3/5; la fusión de contenidos heterogéneos es el mecanismo |

## §3. Strikes y veredicto por retoque (reglas selladas §4 del pre-registro v2)

- **R1 (Potestad): segunda regresión LIMPIA** (0 Potestad incorrectas en
  fresca) → **no hay segundo strike → ENTRA al congelado**, con dos
  residuos declarados: (i) P1 cumplida por vaciamiento (la unidad ancla
  quedó vacía, empeora); (ii) un caso objetivo nuevo (`expaef::9.1`,
  q3 incorrecta: contenido que la base tenía como Restriccion absorbido
  bajo el vocabulario nuevo, con fusión). Ninguno es falla de regresión
  por la regla; ambos van al laudo como límites conocidos.
- **R2 (Condicion + condicion_de): la condición de salida sellada DECIDIÓ**
  (P9 falló de nuevo): **alcance reducido declarado — condiciones
  intra-chunk — y f. 39 residuo con destino E3/r2, sin tercera corrida.**
  Además: **strike 1 de regresión** (fresca `opefci::7.2.1.2`: Obligacion
  de verificación migrada a Condicion, incorrecta por modalidad) con el
  contrapeso exacto de `prevmi::2.5.1` (Condicion **correcta** en fresca,
  y además el primer contraejemplo de la hipótesis léxica: disparador en
  el chapeau, no en el texto propio — el patrón chapeau-deber ejecutado
  completo por primera vez). Balance fresca 1-1. El laudo de congelado
  declara si R2 entra con el alcance reducido sellado (y el strike + el
  caso incorrecto como residuo) o cae — la mesa nota que la salida sellada
  ya fijó el alcance; lo abierto es solo la declaración del strike.
- **R3 (Definicion): segunda regresión LIMPIA** (0 Definicion incorrectas
  en fresca) → **no hay segundo strike → ENTRA**, con tres residuos: la
  duplicación de f. 37 persiste (P8), el definiens puede degradarse entre
  iteraciones (P7), y P3 se resolvió por adjudicación (la delimitación
  revisada avala lo que la predicción prohibía — se registra la tensión y
  manda la marca).
- **R4 (regla 9): estado mixto, a laudo.** P10 falló por segunda vez en la
  misma cláusula interpretativa; P11 se cumplió en espíritu (reversión del
  vaciamiento, sin Potestad); en fresca: 1 sobre-omisión meta-normativa
  adjudicada **empeora** (`traval::S5`, transitorias), 1 **omisión
  DECLARADA** (el brazo nuevo emitió una declaración estructurada del
  vacío — conducta nueva y deseable, `lavdin::3.2.1::intro`), 1 vacío
  simétrico. La regla produce tanto su mejor conducta (declarar) como su
  peor (comerse contenido con costo).
- **`requisito_de_estructura` (R9 segunda mitad): FALLA su regla sellada**
  (≥1 objetada en fresca: hubo **3** — encuadre en otro cuerpo normativo,
  firma de formularios, inscripción registral) → **strike 1**. El parche
  funcionó donde apuntaba (P12/P13, reversiones correctas) y NO generalizó
  — exactamente el escenario que la declaración de alcance del §3
  anticipaba. Por la regla, «se revisa»; la decisión práctica (tercera
  vuelta para un valor de enum, o retiro a r2 conservando
  `reporte_al_supervisor` y el núcleo) es del laudo de congelado (§6).
- **Ya adjudicados en v1 (sin cambio)**: R5 ENTRA · R7 ENTRA (espíritu) ·
  R8 ENTRA (3 de 4) · R9-núcleo (`reporte_al_supervisor`) ENTRA — en v2
  emitió 3 veces (todas en fresca, las 3 fichas mejora, mencionadas
  favorablemente en observaciones; sin canal q4 propio — ver §5). R6a y
  R6b: residuos para r2.

## §4. Balance de `requisito_de_estructura` (10 emisiones + reversiones)

- q4: avala 5 (adrei::2.1.2::intro ×2, adrei::4.1.1.4, adrei::4.3.1.1 ×2)
  / objeta 5 (ayccef::4.2.9, cryl::7.4, ayccef::2.9.3.1, expaef::9.1
  -fusión-, lavdin::3.3.4.3 -persistente-).
- **Punto ciego del instrumento, declarado por la autora**: q4 no registra
  REVERSIONES (emisiones de v1 que v2 abandonó). Columna armada desde
  observaciones: 2 reversiones correctas (constancia documental,
  cumplimiento por remisión) + 1 persistencia objetada (legajo). «La
  corrección de mis-aplicaciones entre iteraciones no es sistemática:
  algunas revierten y otras sobreviven, sin patrón visible».
- Lectura de mesa: el núcleo del valor (procesos/estructuras internas de
  la entidad: las 5 avaladas son todas de esa clase) discrimina; fuera del
  núcleo sigue atrayendo contenido con forma de requisito en material
  fresco, con la delimitación negativa ya puesta.

## §5. Hallazgos de la vuelta 2 (para el laudo y C1.7)

1. **La hipótesis del disparador léxico de Condicion se degrada de regla a
   tendencia** (contraejemplo `prevmi::2.5.1`: emisión correcta sin
   conjunción condicional en el texto propio).
2. **Patrón chapeau-deber ejecutado completo por primera vez**: el deber
   del encabezado entra como nodo con procedencia honesta y la condición
   se cablea contra él — lo que las fichas de ítems dependientes venían
   pidiendo.
3. **Vaciamiento como modo de falla del parche**: 2 omisiones totales
   nuevas en v2 (una es la unidad ancla de P1) + 1 declarada + 1
   simétrica. Curar atracción redirigiendo a omisión no es curar.
4. **Calidad no monotónica entre iteraciones**: definiens truncado (P7),
   fusión de contenidos (P14), hub de cableado desmantelado con 12 aristas
   (la mayor pérdida estructural de las dos lecturas,
   `opefci::7.2.1.2`) — todo en unidades cuyo tipado mejoraba o quedaba
   igual.
5. `reporte_al_supervisor` emitió 3 veces en material fresco, las 3 en
   fichas mejora — la primera señal de generalización positiva de R9.

## §6. Decisiones abiertas para el LAUDO DE ESQUEMA CONGELADO (no las resuelve esta tabla)

- (i) **`requisito_de_estructura`**: la regla exige revisión tras su
  strike; ¿tercera vuelta acotada (solo RE, predicciones nuevas, dentro
  del remanente) o retiro a r2 conservando el núcleo avalado como
  evidencia? La mesa nota: es un valor de properties, no una caja — su
  retiro no toca la matriz.
- (ii) **R2**: la salida sellada ya fijó alcance reducido; el laudo
  declara el strike de fresca y el balance 1-1, y confirma si entra
  reducido o cae.
- (iii) **R4**: ¿se acota la enumeración de la regla 9 (transitorias
  fuera, para no comerse contenido con costo), se acepta con los residuos
  declarados, o se re-anida en C1.7 como limitación?
- (iv) **P1 por vaciamiento**: cómo lo declara el laudo dentro de R1
  (la mesa propone: R1 entra; el vaciamiento de su ancla se registra como
  límite conocido, hermano del hallazgo 3).
- (v) **`reporte_al_supervisor` sin canal de adjudicación formal** (q4 es
  solo de RE): ¿bastan las 3 fichas mejora + observaciones, o el laudo
  pide adjudicación explícita de esas 3 emisiones antes de congelar?

## Reproducibilidad

Todo se recomputa desde `worksheet_pareado_esq3b_v2.json` (444b7f9) +
`seleccion_brazos_esq3b_v2.json` + `pareado_esq3b_v2.jsonl`. Recomputo
mecánico de P1–P14: mesa; marcas: autora (mandan); spot-check de mesa 6/27
con 0 discrepancias.
