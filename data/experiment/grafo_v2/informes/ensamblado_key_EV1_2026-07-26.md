# Informe — Ensamblado de la answer key EV1 (2026-07-26)

**Resultado: `answer_key_EV1.json` ensamblada (36 entradas = 36 originales − EV1-009/014/033 + EV1-037/038/039), todas con `key_adjudicada` y `estado: "verificada"`; acta escrita en `evaluacion_escalon1/acta_adjudicacion_EV1.md`; mini anti-solapamiento de las 3 nuevas corrido y reportado — con UNA observación que requiere tu laudo (EV1-037).** Sin API, sin commits.

## 1. Ensamblado

- Base: `EV1_preguntas.json` (36) menos los 3 descartes del laudo del 26/07 (EV1-009 ↔ CQ-008 score 0.574; EV1-014 ↔ CQN-008/CQ-018 0.622/0.400; EV1-033 ↔ CQ-033 0.356) más las 3 adicionales.
- Cada entrada: campos originales + `key_adjudicada` (= texto de `respuesta_propuesta`, adjudicación aceptada contra PDF/TO el 26/07) + `estado: "verificada"`.

## 2. Mini anti-solapamiento de las 3 nuevas (mismo método; top 3 c/u)

| Nueva | top1 | top2 | top3 |
|---|---|---|---|
| EV1-037 | **CQ-024 · 0.358** | CQN2-010 · 0.290 | CQN-004 · 0.218 |
| EV1-038 | CQN-003 · 0.369 | CQ-040 · 0.205 | CQN2-010 · 0.186 |
| EV1-039 | CQN2-004 · 0.268 | CQN-012 · 0.264 | CQ-010 · 0.260 |

**⚠ EV1-037 vs CQ-024 — candidato a solapamiento real pese al score moderado:** CQ-024 (quemada, CQ_v1) pregunta la periodicidad mínima de clasificación del deudor comercial con financiaciones ≥5% de la RPC; EV1-037 pregunta la periodicidad de revisión de la clasificación del cliente comercial ≥5% RPC — y su `respuesta_propuesta` abre con "En el curso de cada trimestre calendario…": **el mismo dato puntual** (además territorio de la pata (b) de CQN2-010, "la central del trimestre calendario", quemada en el gate CQN2). Bajo el criterio del informe anti-solapamiento (misma pregunta/mismo dato = real), este par califica. No lo descarté — el veredicto es tuyo; queda pre-registrado en el acta.
- EV1-038 vs CQN-003: mismo territorio (cesión sin responsabilidad), distinto interrogante (categoría de clasificación vs sujeto de imputación) → temática.
- EV1-039 vs CQ-010: solapamiento parcial de una celda (la exigencia básica de Bancos) dentro de una pregunta de alcance mayor (tabla completa + transitoria 12.1) → limítrofe-bajo, registrado.

## 3. Acta

`evaluacion_escalon1/acta_adjudicacion_EV1.md` contiene: tandas ratificadas por TO (RegInf 7 · Clasif 8 · Exterior 7 · Protección 7 · CapMin 7, con ids), los 3 descartes con scores y causa, los 3 reemplazos con su verificación y lecturas, y la observación pre-corrida textual sobre EV1-039 y el nodo con emparejamiento cruzado (restantes↔5.000) del 1.2 de CapMin en el grafo v2 (control P3), copiada verbatim del mandato.

## 4. Verificaciones

```
[OK] 36 entradas exactas
[OK] ids únicos
[OK] todas con key_adjudicada no vacía
[OK] todas con estado=verificada
```

**Mezcla real por familia (calculada de los archivos): puntual 10 · enumerativa 12 · condicional 8 · sujeto 6.** No coincide con la anticipada en el mandato (11/11/7/7): los reemplazos restituyeron exactamente las familias de los descartes (salieron 2 puntuales + 1 sujeto, entraron 2 puntuales + 1 sujeto), por lo que la mezcla real es **idéntica a la mezcla sellada del protocolo §2** (10/12/8/6).

## Git status (delta)

```
?? data/experiment/evaluacion_escalon1/answer_key_EV1.json
?? data/experiment/evaluacion_escalon1/acta_adjudicacion_EV1.md
?? data/experiment/grafo_v2/informes/ensamblado_key_EV1_2026-07-26.md
```

**FRENO acá.** Pendientes tuyos: laudo sobre EV1-037/CQ-024 (si se descarta, regenerar y re-chequear), y el commit de sellado del protocolo §7.3 (protocolo con hash + EV1 + key).
