# Censo del gate CQN2 — corrida agente + juez sobre run_3 (15 preguntas)

Fecha: 2026-07-19. **Material del gate del ciclo 2** (head-to-head a tres columnas,
diseño `docs/diseno_ciclo2.md` §1). **Ni el verificador (ninguna versión), ni las capas,
ni S1 corrieron sobre nada de esto — el sellado por inexistencia de la futura vara CQN2
arranca con esta corrida.** Censo MECÁNICO de los veredictos del juez, sin interpretación.

## Guarda paso 0 (verificada antes de correr)

1. `git status` LIMPIO.
2. Commit del sellado `df295255dad7202c39931e8e79eb7def688f1c04` = HEAD (y es el último
   que toca el set).
3. SHA-256 del set = `f3de487a…b15485d` y del runtime = `18e178c8…1468084` — idénticos a
   los del sellado; blobs git working = HEAD (`9edd9bcc…` / `285224f6…`), sin deriva.

## Corrida

`run_posthoc.py --run run_3 --queries queries/eval_set_cqn2_runtime.json --reps 1
--label gate_cqn2` — config idéntica al gate CQN (Haiku temp 0, máx. 15 tool calls, juez
v2.1.1, thinking OFF; selftest 14/14 previo; validación offline 15/15 con referente).
**15/15 trazas, cero failed; hit_rate agente 0.0 (todo fresco).** Trazas congeladas en
`posthoc_run/traces/gate_cqn2/run_3/`.

## Censo por caso

| CQN2 | estrato | respuesta | correctitud | completitud | claims reprobados | patas no cubiertas | síntoma | costo USD |
|---|---|---|---|---|---|---|---|---|
| CQN2-001 | primaria | respondida | correcta | completa | 0 | 0 | **vacío** | 0.0354 |
| CQN2-002 | primaria | respondida | correcta | completa | 3 (0 centrales) | 0 | **NO VACÍO** | 0.0583 |
| CQN2-003 | primaria | respondida | correcta | completa | 0 | 0 | **vacío** | 0.0339 |
| CQN2-004 | primaria | respondida | correcta | completa | 5 (3 centrales) | 0 | **NO VACÍO** | 0.0645 |
| CQN2-005 | primaria | ABSTENCIÓN | correcta | parcial | 0 | 2 | **NO VACÍO** | 0.0569 |
| CQN2-006 | primaria | ABSTENCIÓN | correcta | parcial | 0 | 1 | **NO VACÍO** | 0.0555 |
| CQN2-007 | primaria | respondida | correcta | completa | 4 (0 centrales) | 0 | **NO VACÍO** | 0.0548 |
| CQN2-008 | primaria | respondida | correcta | completa | 0 | 0 | **vacío** | 0.0319 |
| CQN2-009 | primaria | respondida | correcta | completa | 0 | 0 | **vacío** | 0.0339 |
| CQN2-010 | solapada | ABSTENCIÓN | correcta | parcial | 0 | 2 | **NO VACÍO** | 0.0637 |
| CQN2-011 | primaria | ABSTENCIÓN | incorrecta | parcial | 5 (4 centrales) | 6 | **NO VACÍO** | 0.0793 |
| CQN2-012 | solapada | ABSTENCIÓN | correcta | parcial | 2 (0 centrales) | 2 | **NO VACÍO** | 0.0629 |
| CQN2-013 | solapada | ABSTENCIÓN | incorrecta | completa | 3 (1 centrales) | 0 | **NO VACÍO** | 0.0738 |
| CQN2-014 | primaria | respondida | correcta | parcial | 0 | 1 | **NO VACÍO** | 0.0514 |
| CQN2-015 | primaria | ABSTENCIÓN | correcta | parcial | 0 | 2 | **NO VACÍO** | 0.0583 |

**Costo total (agente+juez): $0.8146**

**Candidatos a la vara (síntoma NO vacío): 11/15** — por estrato: primaria: 8 · solapada: 3

## Detalle de síntomas (verbatim del juez, para la adjudicación externa)

### CQN2-002 (primaria)
- claim secundario `no_soportado`: "Las normas del país donde esté situada la casa matriz o entidad controlante deben abarcar la supervisión sobre base consolidada de las filiales o subsidiarias locales."
- claim secundario `no_soportado`: "Los datos de clasificación de deudores se informan sobre base individual con código de consolidación 0 ó 1."
- claim secundario `no_soportado`: "Los datos de clasificación de deudores se informan sobre base consolidada trimestral con código de consolidación 3."

### CQN2-004 (primaria)
- claim CENTRAL `no_soportado`: "Para el cálculo de la exigencia de capital por riesgo general de mercado se utiliza el método de plazos residuales."
- claim CENTRAL `no_soportado`: "El método de plazos residuales obtiene la exigencia como la suma del valor absoluto de la posición ponderada neta, un porcentaje de desestimación vertical, porcentajes de desestimación horizontal y el cambio neto en opciones."
- claim CENTRAL `no_soportado`: "La exigencia por riesgo de mercado se determina computando el mayor valor entre los códigos de cálculo 70810000 y 70820000."
- claim secundario `no_soportado`: "Para posiciones en opciones, las entidades pueden utilizar un método simplificado si cumplen ciertos límites."
- claim secundario `no_soportado`: "Las entidades pueden informar la exigencia por posiciones en opciones mediante cálculos de Gamma y Vega como alternativa al método simplificado."

### CQN2-005 (primaria)
- pata NO CUBIERTA: "Ante quién nomina originalmente el importador a la entidad responsable del seguimiento de la oficialización en SEPAIMPO"
- pata NO CUBIERTA: "Bajo qué condición puede el importador cambiar luego esa entidad por otra"

### CQN2-006 (primaria)
- pata NO CUBIERTA: "Valor que toma el multiplicador de pérdida interna (ILM)"

### CQN2-007 (primaria)
- claim secundario `no_soportado`: "La metodología debe ser rigurosa y sistemática."
- claim secundario `no_soportado`: "La metodología debe estar sujeta a algún tipo de validación basada en la experiencia histórica."
- claim secundario `no_soportado`: "Las evaluaciones deberán ser objeto de un control constante."
- claim secundario `no_soportado`: "Las evaluaciones deben responder a los cambios en la coyuntura financiera."

### CQN2-010 (solapada)
- pata NO CUBIERTA: "Si el fiduciario de un fideicomiso financiero acreedor de créditos de cartera comercial cedidos por un banco es sujeto obligado en materia de protección de usuarios de servicios financieros"
- pata NO CUBIERTA: "Si los deudores cedidos revisten carácter de usuarios aunque no hayan sido notificados de la cesión"

### CQN2-011 (primaria)
- claim CENTRAL `falso`: "Una entidad financiera que proyecta no alcanzar la integración de la exigencia básica de capital debe presentar un plan de regularización y saneamiento."
- claim CENTRAL `falso`: "El plazo para presentar el plan de regularización y saneamiento es dentro de los 30 días corridos siguientes al último día del mes al que corresponda el incumplimiento."
- claim secundario `no_soportado`: "La posición arancelaria NCM 8802 incluye las subpartidas 8802.11.00, 8802.12.10, 8802.12.90, 8802.20.10, 8802.20.21, 8802.20.22, 8802.20.90, 8802.30.10, 8802.30.21, 8802.30.29, 8802.30.31, 8802.30.39, 8802.30.90, 8802.40.10 y 8802.40.90."
- claim CENTRAL `falso`: "La posición arancelaria NCM 8802 está sujeta a arancel."
- claim CENTRAL `falso`: "Para operaciones embarcadas después del 14/04/25, existe una excepción que permite que el pago a la vista se concrete a partir de la fecha estimada de embarque más 15 días corridos cuando corresponde a porción de operación con pagos a la vista."
- pata NO CUBIERTA: "(a) Qué debe presentar la entidad financiera que proyecta no alcanzar la integración de la exigencia básica de capital"
- pata NO CUBIERTA: "(a) Ante quién debe presentarlo"
- pata NO CUBIERTA: "(a) En qué plazo debe presentarlo"
- pata NO CUBIERTA: "(a) Cuál es la duración máxima del instrumento a presentar"
- pata NO CUBIERTA: "(b) Si la posición arancelaria NCM 8802 permite el pago a la vista con registro de ingreso aduanero pendiente para importaciones embarcadas después del 14/04/25"
- pata NO CUBIERTA: "(b) Qué excepción subjetiva existe para ese tipo de bienes (aeronaves NCM 8802) en relación con MiPyMe"

### CQN2-012 (solapada)
- claim secundario `no_soportado`: "La RPC se calcula en función de saldos de partidas admitidas al último día del mes."
- claim secundario `no_soportado`: "La integración diaria de capital se determina considerando la RPC del último día del mes anterior y cambios de valor del portafolio."
- pata NO CUBIERTA: "Qué importe puede adicionarse a los efectos de la determinación de la RPC tras una fusión de entidades financieras"
- pata NO CUBIERTA: "Cómo se calcula el total de integración (RPC) que la entidad informa como total de control en el régimen informativo sobre exigencia e integración de capitales mínimos"

### CQN2-013 (solapada)
- claim secundario `no_soportado`: "Para servicios no comprendidos en los puntos 13.2.1 a 13.2.5, el plazo para acceder al mercado de cambios con contrapartes no vinculadas es de 90 días"
- claim CENTRAL `falso`: "Para un servicio de asesoramiento prestado a partir del 14/04/25 por una contraparte vinculada del exterior, el plazo requerido desde la prestación o devengamiento para acceder al mercado de cambios es de 180 días corridos"
- claim secundario `no_soportado`: "Los servicios de asesoramiento no comprendidos en los conceptos con tratamiento especial no están incluidos en los puntos 13.2.1 a 13.2.5"

### CQN2-014 (primaria)
- pata NO CUBIERTA: "Límites que tiene ese tratamiento excepcional"

### CQN2-015 (primaria)
- pata NO CUBIERTA: "Piso del ponderador de riesgo para exposiciones con deudores no calificados en el capital mínimo por riesgo de crédito"
- pata NO CUBIERTA: "Exposiciones exceptuadas de ese piso"

## Summary de la corrida

```json
{
 "n_preguntas": 15,
 "n_reps_total": 15,
 "n_failed": 0,
 "costo_usd": 0.81458,
 "code_version": "aa15d9c9b5b7",
 "graph_fingerprint": "98d3ee73a23c214b"
}
```

## Sello

- Fecha: 2026-07-19 · HEAD: `df295255dad7202c39931e8e79eb7def688f1c04` (= commit del sellado df29525).
- Checks del paso 0: los 3, impresos arriba.
- La adjudicación de la vara CQN2 es externa y posterior; hasta su commit, ningún
  instrumento puede ver este material.
