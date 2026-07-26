# Acta de adjudicación — Answer key EV1 (2026-07-26)

Ensamblada `answer_key_EV1.json` (36 entradas): las 36 de `EV1_preguntas.json` menos 3 descartes por solapamiento (laudo del 26/07) más las 3 de `preguntas_eval_EV1_adicionales.json`. Cada entrada porta `key_adjudicada` (el texto de `respuesta_propuesta`, aceptado contra PDF/TO el 26/07) y `estado: "verificada"`.

## Tandas ratificadas por TO

| TO | N | Ids |
|---|---|---|
| regimen_informativo | 7 | EV1-001 … EV1-007 |
| clasificacion_deudores | 8 | EV1-008, 010, 011, 012, 013, 015, **037, 038** |
| exterior_cambios | 7 | EV1-016 … EV1-022 |
| proteccion_usuarios | 7 | EV1-023 … EV1-029 |
| capitales_minimos | 7 | EV1-030, 031, 032, 034, 035, 036, **039** |

Mezcla real por familia: **puntual 10 · enumerativa 12 · condicional 8 · sujeto 6** — idéntica a la mezcla sellada del protocolo §2 (los reemplazos restituyeron las familias de los descartes: 2 puntuales + 1 sujeto salieron, 2 puntuales + 1 sujeto entraron).

## Descartes por solapamiento (laudo 26/07, sobre el informe anti-solapamiento)

| Id | Par quemado | Score (tok/tri) | Causa |
|---|---|---|---|
| EV1-009 | CQ-008 | 0.574 (0.467/0.681) | Misma pregunta (plazo de comunicación de la última clasificación) con apéndice |
| EV1-014 | CQN-008 / CQ-018 | 0.622 / 0.400 | La pata "criterio de clasificación de emisoras" es el mismo dato puntual, quemado ×2 |
| EV1-033 | CQ-033 | 0.356 (0.250/0.461) | Límites de exigencia por riesgo operacional del G2 — misma tabla como dato central |

## Reemplazos (EV1-037/038/039) y su verificación

Los 3 adjudicados contra PDF/TO el 26/07 (aceptados). Mini anti-solapamiento (mismo método: Jaccard tokens + trigramas, NFD, contra 61 quemadas únicas), top 3 por pregunta:

- **EV1-037** [puntual, Clasificación]: top1 **CQ-024 score 0.358** (0.276/0.441) · top2 CQN2-010 0.290 · top3 CQN-004 0.218.
  **⚠ Observación para veredicto humano:** el score léxico es moderado, pero CQ-024 pregunta la periodicidad mínima del deudor comercial ≥5% RPC y EV1-037 pregunta la periodicidad de revisión del cliente comercial ≥5% RPC — y la `respuesta_propuesta` de EV1-037 abre con "En el curso de cada trimestre calendario…", el mismo dato puntual de CQ-024 (territorio además tocado por la pata (b) de CQN2-010, "la central del trimestre calendario"). Bajo el criterio del informe anterior (misma pregunta/mismo dato = solapamiento real), este par califica como candidato a solapamiento real pese al score. Queda registrado; el laudo es de la autora.
- **EV1-038** [sujeto, Clasificación]: top1 CQN-003 0.369 (0.240/0.498) · top2 CQ-040 0.205 · top3 CQN2-010 0.186.
  Lectura: mismo territorio (cesión sin responsabilidad para el cedente, Clasificación) pero distinto interrogante — CQN-003 pide la categoría de clasificación de los firmantes; EV1-038 pide a qué sujeto se imputa la financiación. Coincidencia temática, no solapamiento.
- **EV1-039** [puntual, CapMin]: top1 CQN2-004 0.268 · top2 CQN-012 0.264 · top3 **CQ-010 0.260** ("¿Cuál es la exigencia básica de capital mínimo para un banco?").
  Lectura: solapamiento parcial de UNA celda — CQ-010 pregunta la celda Bancos de la tabla del 1.2; EV1-039 pide la tabla completa por clase más la transitoria del 12.1. Distinto alcance del interrogante; limítrofe-bajo. Registrado.

## Observación pre-corrida (textual, pre-registrada)

> "EV1-039 interroga la tabla de exigencia básica del 1.2 de CapMin; el grafo v2 contiene un nodo con el emparejamiento cruzado (restantes↔5.000) detectado durante la adjudicación — si el brazo v2 falla esta pregunta por esa vía, es un defecto de capa de contenido pre-registrado, consistente con el control P3 del protocolo."

## Verificaciones del ensamblado

```
[OK] 36 entradas exactas
[OK] ids únicos
[OK] todas con key_adjudicada no vacía
[OK] todas con estado=verificada
Mezcla real: condicional 8 / enumerativa 12 / puntual 10 / sujeto 6
Cobertura por TO (tos_fuente): CapMin 7 · Clasif 8 · Exterior 7 · Protección 7 · RegInf 7
```

---

## Adenda del cierre de la key (26/07, laudo registrado)

### Cuarto descarte: EV1-037

| Id | Par quemado | Score léxico | Causa |
|---|---|---|---|
| EV1-037 | CQ-024 / CQN2-010(b) | 0.358 / 0.290 | **Solapamiento real** — mismo dato puntual (periodicidad trimestral del deudor/cliente comercial ≥5% RPC; la respuesta propuesta abría con la key de CQ-024, territorio además quemado por la pata (b) de CQN2-010). |

### Laudo EV1-039: CONSERVADA

Limítrofe-bajo (una celda de la tabla del 1.2 vs la tabla completa + transitoria del 12.1) + sonda pre-registrada (observación pre-corrida del acta: nodo con emparejamiento cruzado restantes↔5.000 en el grafo v2; control P3).

### Reemplazo: EV1-040 (por EV1-037, misma familia: puntual)

Nota de adjudicación (textual): "verificada contra el 6.6; se registra que el corpus contiene el instituto hermano 6.4 (reconsideración, banda 20-<40%) — la pregunta sondea la distinción entre ambos".

Mini anti-solapamiento de EV1-040 (mismo método, contra 61 quemadas únicas), top 3: CQ-047 0.233 (tok 0.108/tri 0.358) · CQ-024 0.225 · CQN2-010 0.199.

**Registro del comparador (evidencia, sin veredicto — el laudo es de la autora):** la `cita_textual` sellada de **CQ-047** (CQ_v2 nuevas) contiene VERBATIM el dato de la key de EV1-040 — "discrepancia de más de un nivel … al menos otras dos entidades o fideicomisos … 40 % o más del total informado" (6.6) — y su primera pata pregunta el mismo interrogante (en qué casos hay recategorización obligatoria y cómo cambia la consecuencia según la proporción); CQ-047 cubre además el hermano 6.4.4 (banda 20-<40%) que la nota de adjudicación de EV1-040 declara como territorio de sondeo. Diferencias: EV1-040 pide SOLO los umbrales del 6.6 (subconjunto), CQ-047 la cadena completa (consecuencia, banda, caso categoría 2). Bajo el criterio del informe anti-solapamiento (mismo dato puntual = real), el par califica como candidato pese al score 0.233 — tercer caso consecutivo donde la paráfrasis vence al comparador léxico.

---

## Adenda del cierre FINAL de la key (26/07, laudo registrado)

### Quinto descarte: EV1-040

| Id | Par quemado | Score léxico | Causa |
|---|---|---|---|
| EV1-040 | CQ-047 | 0.233 (tok 0.108/tri 0.358) | **Solapamiento real** — el dato de la key (discrepancia >1 nivel + ≥2 entidades + 40% del total, Clasificación 6.6) aparece VERBATIM en la `cita_textual` sellada de CQ-047, cuya primera pata pregunta el mismo interrogante y que cubre además el hermano 6.4.4 declarado como territorio de sondeo. |

### Candidata NO adjudicada: EV1-041

Registrada como candidata no adjudicada. Causa: **mecanismo no verificado** (monto máximo USD 100 de no residentes por turismo y viajes + verificación en el sistema online del BCRA — la verificación del mecanismo contra el TO no se completó). No integra la key.

### Entrada definitiva: EV1-042 (por EV1-040; misma familia: puntual; Exterior)

Adjudicación: **verificada contra el 3.5.3, verbatim** ("acceso al mercado de cambios con anterioridad no mayor a los 3 días hábiles a la fecha de vencimiento del servicio de capital o interés a pagar").
Mini anti-solapamiento (top 3): CQ-017 0.217 · CQN2-013 0.209 · CQ-014 0.187 — todos bajo el umbral 0.30, ninguno del territorio.

### Episodio del gate pre-escritura (evidencia del funcionamiento del control)

1. **Disparo:** el Gate 2 (dato central en cita sellada) disparó — la sonda `"3 días hábiles"` matcheó la `cita_textual` de CQN2-003. Conforme al mandato, se frenó ANTES de escribir (key y acta intactas), con informe del disparo.
2. **Lectura registrada:** homónimo numérico entre institutos distintos — en CQN2-003 los "3 días hábiles" son el plazo de notificación del número de consulta/reclamo (RCCR, Protección); el dato de EV1-042 es la anterioridad de acceso al mercado de cambios (Exterior 3.5.3). Las sondas distintivas del dato real ("anterioridad no mayor", "3.5.3", "anterioridad a la fecha de vencimiento") dieron 0 hits en todo lo sellado.
3. **Laudo de la autora:** Gate 2 = falso positivo por homónimo numérico; lectura ratificada; EV1-042 adjudicada. El episodio queda como evidencia de que el control frena y el laudo decide.

### Verificaciones del cierre final

```
[OK] 36 entradas · ids únicos · todas con key_adjudicada + estado=verificada
[OK] mezcla 10/12/8/6 (puntual 10 / enumerativa 12 / condicional 8 / sujeto 6)
[OK] conteo por documento: Clasificación 7 · Exterior 8 · CapMin 7 · RegInf 7 · Protección 7 (todos ≥5)
     (esperado corregido por la autora: su "Clasificación 6" anterior fue error aritmético)
```
