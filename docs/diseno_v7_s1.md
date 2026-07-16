# Diseño de v7 — S1: segunda pasada con fuentes forzadas

**Fecha:** 2026-07-16. **Estado:** documento de diseño pre-implementación. Nada de lo aquí
descrito está implementado ni corrido.

**Evidencia base (relevamientos B1/B1b/B1c, copiados a zona trackeada):**
- `docs/evidencia_v7/reporte_b1_arquitectura_v7.md` — corpus, provenances, superficie del
  instrumento, tamaños.
- `docs/evidencia_v7/reporte_b1b_uso_tool.md` — censo de uso de `leer_pasaje_pdf` en las 54
  reps congeladas.
- `docs/evidencia_v7/reporte_b1c_lectura_conclusion.md` — trazado lectura→conclusión en los
  casos de frontera.

**Lecturas que motivan v7:** `docs/lectura_piloto_v6.md` y `docs/lectura_validacion_v61.md`.

---

## 1. Motivación por mecanismo

Tengo **dos motivaciones medidas**, no hipotéticas:

1. **La frontera semántica del piloto** (`docs/lectura_piloto_v6.md` §4a): los dos errores
   silenciosos del piloto (run_3/CQ-018 y CQ-033) caen en la frontera
   `contenido_kg ↔ sin_defecto ↔ jerarquía` — decidir si un contenido es general o scopeado
   exige leer el PDF, y esa frontera no es computable por la capa D.
2. **La no generalización entre esquemas** (`docs/lectura_validacion_v61.md` §4a): calibrado
   sobre material de run_1/run_3/run_5, el componente LLM dio **0/6** de precisión de
   atribución sobre los casos con síntoma de run_2/run_4, con los mismos modos de error del
   gate (sesgo a `navegación`, sobre-exoneración, lectura des-scoping).

El trazado B1c (`docs/evidencia_v7/reporte_b1c_lectura_conclusion.md`) desagrega el
**mecanismo en dos capas** — y es lo que define la forma de S1:

- **Capa 1 — fuera de la familia de calibración, el instrumento no llega a leer el pasaje
  decisivo.** En la validación, las reps de r2/CQ-018 **nunca abrieron el 10.1 de
  Clasificación** (leyeron 4.x/6.x/7.x) y las de r4/CQ-017 **nunca abrieron el 1.1 de
  Exterior** (solo Protección). El error de atribución se emite sin haber mirado la fuente
  que lo decidiría.
- **Capa 2 — dentro de la familia, lee el pasaje decisivo y no lo usa.** En el piloto, las
  reps de CQ-033 leyeron **ambos** pasajes — el 12.3 **con su encabezado de declaración de
  alcance** y el 7.3 — y emitieron `contenido_kg` primaria igual; el campo `razonamiento`
  persistido queda anclado en el **eco del nodo**, no en la comparación de alcances que tenía
  delante. Las reps de CQ-018 del piloto también leyeron el 10.1 y erraron igual.

Y un dato que descarta la explicación fácil: **el acceso a la fuente NO es el problema.**
Según B1b, `leer_pasaje_pdf` es la tool **más usada** del verificador (298/649 invocaciones,
45,9%, presente en las 54/54 reps de las tres corridas congeladas), y su backend
(`pdf_locate.localize`) ya devuelve pasajes que **arrancan en el encabezado con la
declaración de alcance**. El instrumento lee mucho y lee bien ubicado; lo que falla es (capa
1) *qué* elige leer fuera de su distribución de calibración y (capa 2) *usar* lo leído en el
juicio. Por eso v7 no agrega una tool de lectura más: **fuerza la comparación**.

## 2. Arquitectura — v7 = v6.1-D + S1

**S1 es un post-procesador CON LLM sobre los JSONs de salida de v6.1-D.** No toca el
verificador ni la capa D: corre después, sobre lo ya emitido.

**Gatillo.** S1 se dispara sobre:
- atribuciones cuya causa está en `{contenido_kg, aplicacion_erronea, estructural_kg,
  completitud_kg}`, y
- exoneraciones (`sin_defecto` / clave vacía) de casos **con síntoma**.

**Por cada atribución gatillada, EL CÓDIGO (sin juicio) prepara el material:**

1. Parsea la provenance del portador citado con `pdf_locate.parse_point` — 100% parseable
   en run_3 (4.064/4.064; B1 §3).
2. Recupera con `pdf_locate.localize`:
   - (a) el **pasaje del portador CON su encabezado**;
   - (b) los **pasajes comparativos**: el encabezado de la **sección madre** y el **punto
     hermano/general** cuando el parseo lo identifique, por regla determinística: mismo
     prefijo de sección, un nivel arriba (p. ej., para un portador en 12.3, la sección 12 y
     el punto general de la misma materia que el parseo resuelva un nivel arriba).
3. Inyecta portador + comparativos en **UNA llamada LLM de juicio acotado** cuyo esquema de
   salida **OBLIGA** a completar:
   - `alcance_declarado_en_fuente` — quote **verbatim** del encabezado leído;
   - `alcance_en_el_nodo` — quote del nodo;
   - `coinciden` — `sí` / `no` / `no_determinable`;
   - `causa_confirmada_o_corregida` + justificación breve.

El esquema forzado es la respuesta directa al mecanismo de capa 2: el fallo medido no es de
retrieval sino de uso — B1c muestra al instrumento con el encabezado de alcance delante y el
razonamiento anclado en el eco del nodo. S1 hace **imposible emitir el juicio sin transcribir
primero ambos alcances**.

**Anotación, nunca borrado.** S1 **NUNCA elimina la emisión de v6.1-D**: anota `capa_s1` al
lado de cada atribución juzgada (el mismo patrón de anotación que `capa_d`), y el voto se
recomputa como `voto_s1` **preservando** `voto_original`, `voto_pre_d6` y `voto_capa_d`.
Todo `no_determinable` y todo fallo de localización (`localizacion_pdf=fallida` — el trazado
B1c capturó un ejemplar real) van a **triage con motivo nuevo: `fuente_no_verificable`**.

**Lo que NO cambia:**
- el verificador v5.7 queda congelado (prompt incluido — es parte del instrumento);
- la capa D queda intacta (D1–D6, semánticas pre-registradas);
- la taxonomía sigue siendo v2.6.1;
- S1 **no re-investiga trayectorias**: juzga la atribución emitida contra la fuente. No es
  un segundo verificador; es un control de calidad acotado sobre la salida del primero.

## 3. Riesgos declarados

- **(a) Esquema forzado llenado por cumplimiento.** Un LLM obligado a transcribir quotes
  puede llenarlos ritualmente y confirmar igual la causa original. La mitigación **no** son
  más reglas de prompt (eso es iterar contra el riesgo sin medirlo): es el **gate sobre
  material fresco** del plan de calibración (§4), que mide si S1 corrige de verdad.
- **(b) Dependencia del formato de provenance por esquema de grafo.** run_2 y run_4 usan
  formatos distintos de run_3 ("Sección N > Punto X.Y"; "p.X-Y / Punto Z" con sufijos
  textuales — B1 §3). `parse_point` ya cubre el formato de run_2; la cobertura por esquema
  **se mide, no se asume** — un formato no parseado cae en `fuente_no_verificable`, nunca en
  juicio silencioso.
- **(c) Costo.** Una llamada LLM extra por atribución gatillada. Con los tamaños de B1 §5
  (pasajes de `localize` con ventana acotada; corridas medidas en 0,74–1,16M tokens de input
  por caso en régimen N=3), la llamada de S1 es corta (portador + 2 comparativos + esquema):
  el incremental estimado es una fracción menor del costo por caso, y se presupuesta con los
  números reales del dev antes del gate.

## 4. Plan de calibración (pre-registrado)

- **DEV:** la reserva pre-registrada — `run_2/CQ-021`, `run_4/CQ-008`, `run_4/CQ-021`,
  `run_4/CQ-028` — previa **adjudicación humana de sus GTs por el circuito de la vara**
  (expediente con evidencia determinística → adjudicación cerrada → vara commiteada antes de
  cualquier corrida). La iteración del prompt de S1 está permitida **SOLO contra ese dev**,
  con la **regla de frenado idéntica a v5.7**: lo que el dev motiva se valida sobre material
  que el dev no tocó.
- **GATE:** las fallas del **set de preguntas nuevas** (generación ciega en curso, protocolo
  con muestreo mecánico), **adjudicadas y selladas antes de correr** (sellado por
  inexistencia, guarda por commit en HEAD — el mismo circuito del piloto y la validación).
  **Head-to-head pre-registrado: v6.1-D vs v7 sobre el mismo material**, corrida única.
- **Timebox:** si implementación + calibración superan las **dos semanas**, freno con un
  checkpoint de calendario documentado (qué está hecho, qué falta, decisión de continuar o
  cerrar con lo medido).

## 5. Criterio de éxito pre-registrado

**v7 tiene éxito si reduce los errores de frontera semántica del canal automático respecto
de v6.1-D en el gate fresco, sin aumentar los errores silenciosos.** Si no lo logra, v7 se
documenta como intento con sus datos completos, y el sistema queda en **v6.1-D con su límite
de uso escrito** (`docs/lectura_validacion_v61.md` §4e: enrutador confiable dentro de la
familia de calibración, derivador conservador fuera de ella, canal automático sobre esquemas
nuevos condicionado a recalibración).
