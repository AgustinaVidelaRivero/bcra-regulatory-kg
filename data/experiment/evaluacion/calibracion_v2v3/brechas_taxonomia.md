# Brechas de taxonomía — causas selladas de la familia v2/v3 vs catálogo v2.6.1 (U5-PREP)

**Fecha:** 2026-08-02. **Qué es:** cruce de los veredictos causales humanos sellados del
expediente (`expediente_material.md`) contra el catálogo cerrado v2.6.1 del verificador,
leído del archivo real que el prompt ensambla por referencia
(`.claude/skills/kg-refinement/references/taxonomia.md` — Capa 1 con precedencia, tablas
de Capa 2, árbol de decisión; el hash de ese archivo está sellado en
`posthoc_run/dev_set/extraccion_h2h_ciclo2.md` §Sello:
`fc9a4962a222867a9ff7bd66cfd5962285139352d50b257355e14bec803b34ad`).

**NADA de este documento modifica taxonomía alguna.**

**LAUDADO (destrabe de la adjudicadora, 2026-08-02): las tres brechas se resuelven por
LECTURA EXTERNA — cero cambios a `taxonomia.md`, al prompt, a los módulos o a los
umbrales:**
1. `perdida_en_ensamblado` — sub-especie de lectura externa de `completitud_kg` (§1).
2. `falla_de_juez` — clase de lectura externa con subtipos `abstencion_aprobada` y
   `varianza_de_tallado` (§2). El canal de detección de abstenciones-aprobadas queda
   FUERA de U5, como deuda explícita en `docs/protocolo_gate_u5.md` §7 y candidata de
   cola ("screening de aprobadas / re-calibración del juez").
3. `entierro_por_ranking` — sub-especie de lectura externa (la **Opción 1** de §3;
   acierto = la clave, precedente CQN2-015). La Opción 2 (re-anclar la definición en el
   contrato) queda descartada.

**Advertencia estructural que condiciona TODAS las propuestas:** el catálogo v2.6.1 no es
un documento suelto — es parte del prompt del verificador congelado (`verificador.py`
`taxonomia_section()` lo lee en runtime; el prompt v5.7 ensamblado tiene hash sellado
`d031913d580278df833c125df7d8469bc1dd19bc9775082d0b6cb64a77442659`). Agregar o redefinir
una clase en `taxonomia.md` CAMBIA el prompt del instrumento validado → invalida el sello
del ciclo 2 → exige un ciclo nuevo de dev + gate. Por eso cada brecha se propone en DOS
niveles: (a) como clase de **lectura externa** (vocabulario de la adjudicación humana y
del backlog, sin tocar el instrumento) y (b) como cambio del **contrato del verificador**
(solo si la autora decide abrir un ciclo de instrumento). El nivel lo lauda la autora.

---

## 1. Brecha: `perdida_en_ensamblado` (candidata anotada por la semana — evaluación)

**Casos que la motivan:** EV1-031 y EV1-042 ("dato de la clave nuevo en v3 desde chunk
recuperado" — el hueco de v2 lo produjo el ensamblado, no la extracción) y EV1-015 (el
criterio 1.1 ausente; BKL-0017 especie `ausencia`, restaurado por C1).

**Cruce contra v2.6.1:** los tres casos SÍ tienen casillero: `completitud_kg` ("Falta
información que el PDF sí tiene (nodo stub/vacío, extracción incompleta, dato ausente)").
El árbol resuelve limpio: pata sin dato → `context_recall` → portador no existe →
`completitud_kg`. **No es una causa sin clase: es un MECANISMO de producción del hueco**
(¿el dato se perdió al ensamblar, nunca se extrajo, o nunca estuvo en el chunk?), que
`completitud_kg` no distingue.

**Evaluación (no la doy por buena):**
- A favor de nombrarla: el proyecto ya demostró que la distinción PAGA — el 1b atribuyó
  +2 puntos netos al defecto de ensamblado, y el enrutamiento del arreglo es distinto
  (re-ensamblado vs re-extracción vs corrección puntual).
- En contra de meterla en el contrato del verificador: distinguir "perdido en ensamblado"
  de "nunca extraído" exige evidencia que las tools del verificador NO alcanzan (hay que
  mirar el caché de extracción y los chunks — `grafo_v2/code/cache*`, material sellado);
  el verificador solo ve grafo + PDF + traza. Una clase que el instrumento no puede
  evidenciar produciría atribuciones no verificables (el motivo exacto del flag R6b de la
  capa determinística).

**Propuesta para laudo:** NO crear clase de capa 2 en el contrato del verificador.
Crear **sub-especie de lectura externa** de `completitud_kg`:
- **Nombre:** `perdida_en_ensamblado`.
- **Definición (una oración):** el dato ausente del grafo existía en el caché de
  extracción y se perdió en el paso de ensamblado, verificable contra los chunks del
  caché congelado.
- **Caso que la funda:** EV1-031 (predicción sellada del mapeo `6c24009` §C: "dato de la
  clave nuevo en v3 desde chunk recuperado", verificada mecánicamente en la ficha delta).
- **Dónde vive:** en la adjudicación humana y en el backlog (campo especie), como ya pasa
  con `ausencia`/`quimera` en `data/backlog/backlog.jsonl` — el verificador sigue
  emitiendo `completitud_kg` y el comparador externo anota el mecanismo.

## 2. Brecha: `falla_de_juez` con subtipos (candidata anotada por la semana — evaluación)

**Casos que la motivan:** los dos del expediente del juez (`docs/lectura_escalon1b.md`
§5): (i) abstención-aprobada (EV1-029, réplicas r1 de ambos brazos; precedente sellado
run_3/EV1-007, `acta_adjudicacion_EV1.md`); (ii) varianza de tallado (EV1-035, la misma
familia de claims tallada central-falsa / no-central / no tallada según la réplica).

**Cruce contra v2.6.1:** el catálogo solo conoce UN modo de error del juez: el falso
positivo por claim, cubierto por `sin_defecto` (lado ninguno, "posible falso positivo del
juez"). Ninguno de los dos casos cabe ahí:
- **(i) Abstención-aprobada es un falso NEGATIVO:** el juez aprueba una no-respuesta.
  SIN CLASE, y además fuera del universo de entrada del instrumento: el verificador
  recibe fallas (veredicto incorrecta); una réplica aprobada jamás llega. Ninguna clase
  de salida puede arreglarlo — es un problema de COBERTURA del pipeline, no de
  vocabulario.
- **(ii) Varianza de tallado es un defecto de ESTABILIDAD del instrumento:** el veredicto
  final depende de cómo la descomposición talló los claims, no de qué dice el sistema.
  `sin_defecto` por claim nombra el efecto en una réplica, pero no existe categoría que
  diga "el flip de mayoría lo produjo el tallado" — eso hoy solo se ve comparando
  réplicas, cosa que el verificador (aislamiento por falla, decisión de diseño de
  `verificador.py`) no hace ni debe hacer.

**Evaluación (no la doy por buena):**
- La clase ES necesaria en el vocabulario del PROYECTO: dos casos sellados y un
  precedente (EV1-007) la instancian, y el hallazgo rector (grounded ≠ correct) tiene su
  simétrico en el instrumento (aprobado ≠ correcto).
- Meterla en el contrato del verificador es la opción CARA y de bajo rendimiento: (a)
  rompe el sello del instrumento (advertencia de cabecera); (b) para el subtipo (i) es
  además inútil — el caso no entra a la bandeja; (c) para el subtipo (ii) el verificador
  aislado por falla no tiene la evidencia inter-réplicas que define el subtipo.

**Propuesta para laudo:** clase de **lectura externa** (adjudicación humana + backlog +
protocolo del gate), NO del contrato del verificador:
- **Nombre:** `falla_de_juez`, con subtipos `abstencion_aprobada` y
  `varianza_de_tallado`.
- **Definición (una oración):** el veredicto de correctitud que definió el caso lo
  produjo un error o inestabilidad del instrumento juez (aprobar una no-respuesta, o
  tallar la misma familia de claims de forma distinta entre réplicas), no un defecto del
  grafo ni del agente.
- **Casos que la fundan:** (i) EV1-029 r1×2 + precedente run_3/EV1-007;
  (ii) EV1-035.
- **Relación con el gate U5:** las reglas de acierto del gate se escriben en el
  vocabulario v2.6.1 QUE EL INSTRUMENTO SÍ PUEDE EMITIR (para EV1-035: exoneración —
  ninguna primaria de sistema), y la etiqueta `falla_de_juez` la pone la lectura externa.
  Así el gate mide al instrumento actual sin pedirle vocabulario que no tiene.
- **Consecuencia de diseño que excede esta unidad (se deja registrada):** el subtipo (i)
  exige, si se quiere DETECTAR y no solo nombrar, un canal nuevo (muestreo de aprobadas o
  screening de abstenciones sobre veredictos `correcta`) — eso es re-calibración DEL JUEZ
  y/o ampliación del pipeline, otra unidad y otro laudo.

## 3. Brecha: ¿`alcanzabilidad_kg` cubre EV1-029 con la evidencia de ranks? (candidata a re-examen — evaluación)

**El caso:** el laudo de válvula selló "caso de ALCANZABILIDAD, la tercera clase
taxonómica del proyecto (existe pero inalcanzable)" con esta evidencia de ranks: bajo las
11 queries reales del agente v2 el portador `…997afd` nunca entró al corte de 10 (mejores
ranks 16 y 19); una query razonable de la trayectoria v3 ('responsable consultas reclamos
deudor cedido') lo rankea 6 en v3 **y habría rankeado 7 sobre el índice de v2**.

**Cruce contra la definición v2.6.1 (leída del archivo):** `alcanzabilidad_kg` exige que
el portador sea "inalcanzable por la búsqueda léxica: […] ninguna búsqueda razonable
desde los términos de la pregunta lo devuelve", con evidencia de que "los términos
plausibles del vocabulario ex ante NO lo alcanzan y que solo se alcanza con palabras del
propio nodo". **La evidencia de EV1-029 contradice la letra de la definición:** existe
una búsqueda razonable del vocabulario de la pregunta que SÍ lo devuelve dentro del corte
(rank 7 en el propio índice de v2). Bajo lectura estricta del árbol, "existe y las
búsquedas razonables del agente lo alcanzaban → navegación" tampoco cierra: las 11
queries que el agente v2 efectivamente hizo eran razonables y dejaron el portador FUERA
del corte (16/19) — match léxico positivo, nunca visible.

**Conclusión del cruce: EV1-029 cae en la laguna B′ (entierro-por-ranking), ya
documentada dos veces:** pre-registrada en la vara del gate CQN (caso CQN-009) y
materializada en CQN2-015 (`docs/casos_gate_cqn2.md`: "D2 no distingue el
entierro-por-ranking de la inalcanzabilidad léxica, y ninguna columna emite 'B′'";
`docs/lectura_ciclo2.md` titular (v)). La familia v2/v3 aporta el TERCER ejemplar y el
primero con contrafáctico 2×2 de índices. No es que `alcanzabilidad_kg` no exista: es que
su definición decide por corte binario y no nombra el mecanismo intermedio
(alcanzable-en-principio, enterrado-en-la-práctica).

**Propuesta para laudo (dos opciones, excluyentes):**
- **Opción 1 — sub-especie de lectura externa (recomendada por costo):**
  - **Nombre:** `entierro_por_ranking` (alias del mecanismo B′ ya usado en las varas).
  - **Definición (una oración):** el portador matchea léxicamente las queries razonables
    del agente pero queda consistentemente fuera del corte top-N del índice, de modo que
    es alcanzable en principio e invisible en la práctica.
  - **Caso que la funda:** EV1-029 (ranks 16/19 bajo las 11 queries reales; rank 7 bajo
    la query decisiva), con precedentes CQN-009 y CQN2-015.
  - El verificador sigue emitiendo `alcanzabilidad_kg` (o `navegación`, según su
    evidencia) y la lectura externa anota B′ — igual que hizo la vara CQN2-015 ("acierto
    = la clave, no el mecanismo").
- **Opción 2 — precisión del contrato (solo si se abre ciclo de instrumento):** re-anclar
  la definición de `alcanzabilidad_kg` al corte operativo del índice ("ninguna búsqueda
  razonable lo devuelve DENTRO DEL CORTE top-N con el que operó el agente") y agregar la
  constancia de ranks al campo `busquedas`. Cubre EV1-029 sin clase nueva, pero cambia el
  prompt sellado (advertencia de cabecera) y re-abre la frontera con `navegación`
  calibrada en los gates previos.

**Regla de acierto derivada para el gate U5 (cualquiera sea el laudo):** en EV1-029 se
acepta `{context_recall, alcanzabilidad_kg}` como acierto de clave (el casillero que el
laudo humano usó), se registra aparte si el instrumento nombra el mecanismo, y
`{context_recall, navegación}` se pre-registra como rama de lectura (evidencia de la
misma laguna, no acierto ni miss silencioso) — la letra exacta queda en
`docs/protocolo_gate_u5.md` y la lauda la autora.

## 4. Causas selladas restantes — verificación de que NO abren brecha

- **"varianza de trayectoria" (EV1-029, la conversión v2→v3):** no es una causa de falla
  — es la explicación de una conversión a acierto. No requiere clase: se registra como
  lectura (ya lo está, en el veredicto sellado).
- **"no-respuesta / evasivas" (EV1-018, EV1-031):** conducta del agente ante el hueco,
  no causa; la causa sellada de ambos mapea (alcanzabilidad_kg / completitud_kg). El
  patrón "abstención disciplinada" ya está caracterizado en la vara CQN2 (§(a).6) sin
  clase propia.
- **"sobre-ampliación" (nota del laudo run_3/EV1-035: 'excepción enunciada sin sus
  condiciones esenciales'):** en la familia v2/v3 el defecto de borde de las seis
  respuestas quedó registrado pero SIN adjudicación fina de lado (el laudo exonera al
  grafo del FLIP, no adjudica el borde). Si la autora lo adjudica alguna vez, el árbol
  v2.6.1 tiene casilleros candidatos (`alucinacion_agente` / `contenido_kg` según dónde
  viva el recorte); hoy no hay brecha que declarar, solo un pendiente anotado.
- **6 fichas sin causa (EV1-005, 011, 028, 039 + las v2 de 029/042):** sin causa no hay
  cruce posible; no abren ni cierran brechas.

## 5. Resumen — con el nivel LAUDADO por brecha (2026-08-02)

| Brecha | ¿SIN CLASE hoy? | **Nivel laudado** | Propuesta de contrato (descartada) | Caso fundante |
|---|---|---|---|---|
| `perdida_en_ensamblado` | No (es `completitud_kg`); sin nombre el MECANISMO | **LECTURA EXTERNA** — sub-especie de `completitud_kg` en adjudicación/backlog | descartada (inevidenciable con las tools del verificador) | EV1-031 |
| `falla_de_juez` / `abstencion_aprobada` | SÍ (falso negativo; fuera de la bandeja del verificador) | **LECTURA EXTERNA** — subtipo de `falla_de_juez`; canal de detección FUERA de U5 (deuda en protocolo §7, candidata de cola) | descartada (inútil sin canal nuevo) | EV1-029 r1×2 (prec. run_3/EV1-007) |
| `falla_de_juez` / `varianza_de_tallado` | SÍ (solo el efecto por claim cae en `sin_defecto`) | **LECTURA EXTERNA** — subtipo de `falla_de_juez`; el gate exige exoneración al instrumento | descartada (exige evidencia inter-réplicas que el diseño aislado no ve) | EV1-035 |
| B′ / `entierro_por_ranking` | A medias (colapsa en `alcanzabilidad_kg`↔`navegación`; laguna documentada ×2) | **LECTURA EXTERNA** — sub-especie con nombre; acierto = la clave (Opción 1, precedente CQN2-015) | descartada (re-anclar `alcanzabilidad_kg` re-abre frontera calibrada) | EV1-029 (prec. CQN-009, CQN2-015) |

Con los laudos tomados, el instrumento sellado queda intacto: el split, los calibradores
(`calibradores_v2v3.md`) y el protocolo del gate (`docs/protocolo_gate_u5.md`) operan
con el vocabulario v2.6.1 tal como está, y las etiquetas nuevas viven en la lectura
externa (adjudicación humana, backlog, protocolo).
