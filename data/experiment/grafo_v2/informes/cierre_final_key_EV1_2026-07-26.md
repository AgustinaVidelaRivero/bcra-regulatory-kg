# Informe — Cierre FINAL de la key EV1 (2026-07-26)

*(Antecedente en esta misma unidad: el gate pre-escritura disparó en su primera invocación — sonda "3 días hábiles" en la cita sellada de CQN2-003 — y se frenó sin escribir. Laudo de la autora: falso positivo por homónimo numérico, lectura ratificada, EV1-042 adjudicada. El episodio completo quedó registrado en el acta como evidencia del funcionamiento del control.)*

**Resultado: cierre ejecutado — EV1-040 fuera (quinto descarte: su dato aparece verbatim en la cita sellada de CQ-047), EV1-042 dentro en la misma posición con `key_adjudicada` y `estado: "verificada"`; EV1-041 registrada como candidata no adjudicada (mecanismo no verificado); acta actualizada con todo, incluido el episodio del gate. Todas las verificaciones OK.** Sin API, sin commits.

## Swap y verificaciones

```
swap OK en posición 33: sale EV1-040, entra EV1-042 [puntual, Exterior]
[OK] 36 entradas exactas
[OK] ids únicos
[OK] todas con key_adjudicada + estado=verificada
[OK] mezcla 10/12/8/6 — real: condicional 8 / enumerativa 12 / puntual 10 / sujeto 6
[OK] conteo por documento — real: CapMin 7 · Clasificación 7 · Exterior 8 · Protección 7 · RegInf 7
[OK] todos los TOs ≥5
```

El conteo por documento coincide con el esperado corregido por la autora (Clasificación 7 / Exterior 8 / resto 7; el "Clasificación 6" del mandato original fue error aritmético, verificado contra archivos).

## Mini anti-solapamiento de EV1-042 (top 3)

CQ-017 0.217 (tok 0.154/tri 0.280) · CQN2-013 0.209 · CQ-014 0.187 — todos bajo 0.30, ninguno del territorio de endeudamientos con el exterior. Sondas del dato central ("anterioridad no mayor", "3.5.3", "anterioridad a la fecha de vencimiento"): 0 hits en citas/keys selladas.

## Acta

`acta_adjudicacion_EV1.md` actualizada con la adenda final: quinto descarte (EV1-040 ↔ CQ-047, dato verbatim en cita sellada), candidata EV1-041 no adjudicada (causa: mecanismo no verificado), entrada de EV1-042 (verificada contra el 3.5.3, verbatim) con su top 3, el episodio del gate (disparo → lectura de homónimo → laudo) y las verificaciones del cierre.

## Estado de la key

`answer_key_EV1.json` cerrada: 36 entradas, historial completo de la depuración = 5 descartes por solapamiento (EV1-009, 014, 033, 037, 040) + 1 candidata no adjudicada (EV1-041) + reemplazos EV1-038/039/042 y los originales. **Pendiente tuyo: el commit de sellado del §7.3 (protocolo con hash + EV1 + key + actas).**
