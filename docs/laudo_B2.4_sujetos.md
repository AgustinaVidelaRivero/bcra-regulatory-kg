# Laudo B2.4 — asignación de sujeto: los ocho patrones y las entradas BKL-0001, 0002, 0018, 0020 y 0021

**BORRADOR — PENDIENTE DE DOS LECTURAS Y DE LA FIRMA DE LA AUTORA** · Redactado por la mesa el 07/10/2026 (noche), con las decisiones de la
autora del mismo día sobre la ficha de decisión de la mesa. Fila B2.4 del plan (`docs/plan_tesis.md:383`); condición 13 de la tanda 1
(`docs/checklist_pre_escalado.md`, línea de las condiciones) y fila X9 del checklist: se firma antes de la tanda 1.

## 1. Qué decide

- Cierra las entradas del backlog que la autora asignó a este laudo el 04/10/2026 (`plan:383`, decisión 1): BKL-0001, 0002, 0018 y 0021.
- Cierra los ocho patrones de asignación de sujeto, BKL-0009 a BKL-0016, con su lectura sobre el grafo de U-REEXT-T0 (`plan:383`,
  decisión 3).
- Suma BKL-0020, del mismo origen que BKL-0021: los sujetos de cuarentena de v3 sin padre (`data/backlog/expediente_retriage_v3.md:182-196`).
- Fija la meta de los sujetos resueltos del tablero (fila de la mención del sujeto y los sujetos no mapeables).
- No corrige el grafo: lo que no se corrige se declara.

## 2. Sobre qué grafo se lee

El diez r2b completo, KG-Tanda0-Diez-r2b, `a9631a64…` (sellado en `bbc38dc`; `data/experiment/neo4j/grafos.py`), por decisión de la autora.
El re-sellado único posterior no toca los puntos de los ocho patrones. R2-3 (`803623a`) y R2-3 bis (`dac7d57`) cambian solo `docvig::3.4`
(`data/experiment/reresolucion_catalogo/freno_r2_3.md:13-18`), y ninguno de los ocho puntos está en docvig. U-OMISIONES-COD cambia la
procedencia (grupos G y J), las menciones (grupo B) y las bases de los relativos (grupo C), no el destino de las aristas de sujeto. Si
alguno de esos cambios moviera una arista de estos puntos, la re-medición posterior al re-sellado lo dice, y el laudo recibe una nota.

## 3. Decisiones de la autora (07/10/2026), por entrada

| entrada | decisión | evidencia |
|---|---|---|
| BKL-0009 a BKL-0016 (los ocho patrones) | Se cierran con la lectura de T3 (control o de U-REEXT-T0, lectura asistida de la instancia), más una **segunda lectura a ciegas de los 8 puntos**. Esa lectura la hace una sesión nueva de la mesa, la misma de la segunda lectura de las 41 de la enmienda 8, después del 08/10/2026 a las 18 h. Las divergencias las adjudica la autora. Se declara el cambio de verificación: lectura asistida y a ciegas, en lugar de chunk contra PDF. | `data/experiment/reext_t0/t3/salida/lectura_controles_t3.md:60-68`; despacho de la mesa |
| BKL-0001 y BKL-0002 | Se cierran con el test por punto de la suite r2b, declarando el cambio de verificación: test de la suite en lugar de chunk contra PDF. | `data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2b/suite_perfil_r2.md:70-71`: BKL-0001 resuelto (7 nodos anclados en 2.8.3.3, uno con «75 veces SMVM»); BKL-0002 resuelto (35 anclados en 3.5.3, 2 con la ventana de 3 días hábiles) |
| BKL-0018 | Límite declarado, junto con BKL-0004, que persiste como falla conocida sellada. | `suite_perfil_r2.md:18` |
| BKL-0021 | Se cierra como **cuarentena declarada**. Los dos propuestos («la entidad nominada», `ext::11.1.1.10` y `ext::3.18.2::intro`; «la entidad nominada por el exportador», `ext::7.3::intro` y `ext::7.3.7`) quedan en cuarentena con sus 4 `aplica_a`. El rol nuevo, si corresponde, entra por el procedimiento de crecimiento de la enmienda 4 al protocolo (FIRMADA el 07/10/2026, §1) al cierre de la tanda 1: la clave llega al umbral de 2 unidades. Antes de firmar, la misma sesión nueva lee si las 4 filas «entidad(es) encargada(s) del seguimiento de la(s) oficialización(es)» (`ext::4.4::intro`, `ext::4.4.2`, `ext::10.8`, `ext::11.1.5::intro`) designan el mismo sujeto; si lo designan, entran a la misma clave. **Esta decisión reemplaza la decisión (c) del 06/10/2026** (un rol nuevo por U-RERESOL-CAT; mandato de U-REEXT-T0, `:585-588`), que ninguna unidad ejecutó. | control q de T3: la mención reaparece como «la entidad nominada» (`lectura_controles_t3.md:73-76`); la condición de cierre del 04/10 («no reaparece») no se cumplió |
| BKL-0020 | Cuarentena declarada: 1 fila en r2b, «una entidad originante» (`cap::3.1.3::cierre`), por debajo del umbral. | registro de no mapeados del diez r2b |
| Meta de resueltos (tablero) | Sin meta numérica: dependen del crecimiento del catálogo (enmienda 4). La cuarentena se declara con su cifra: 294 filas en el registro del diez r2b (164 en cuarentena, 128 resueltas a clase, 2 descartadas) y 98 nodos `Sujeto_propuesto_*`. | `docs/tablero_correcciones.md`, fila de la mención del sujeto |

**Cómo queda el estado de las entradas.**
- La máquina de estados del backlog (`docs/spec_backlog_refinamiento.md`, §2 y §5) no tiene un estado de «límite declarado» ni de
  «cuarentena declarada».
- Propuesta de la mesa, a confirmar al firmar: BKL-0018, 0020 y 0021 quedan en `triaged`, con un evento `nota` que dice que el laudo las
  cierra como límite o cuarentena declarados y que no se corrigen en esta versión.
- La alternativa, `descartado`, diría que la entrada no era un defecto, y no es así.
- BKL-0001, 0002 y 0009 a 0016 pasan a `verificado` (los ocho, si la segunda lectura y la adjudicación no cambian el veredicto).

## 4. Qué falta para firmarlo

1. La segunda lectura a ciegas de los 8 puntos, y la adjudicación de la autora sobre sus divergencias con T3.
2. La lectura de las 4 filas de «entidad(es) encargada(s) del seguimiento».
3. La confirmación de la convención de estado del §3.

Las dos lecturas van en el despacho de la mesa para una sesión nueva después del 08/10/2026 a las 18 h, junto con la segunda lectura de
las 41 de la enmienda 8.

## 5. Lote de eventos del backlog (se agrega a `data/backlog/backlog.jsonl` con el commit de la firma)

El backlog es append-only (`docs/spec_backlog_refinamiento.md`, §5). Los cambios de estado dependen de la firma y de las dos lecturas
pendientes: el lote se escribe acá y se agrega al archivo con la firma, con la fecha de la firma en `ts`. Si la segunda lectura muestra
que un patrón reaparece, su línea `cambio_estado` se reemplaza por una `nota` con el resultado, y la entrada queda en `triaged`.

```jsonl
{"evento": "cambio_estado", "id": "BKL-0001", "estado": "verificado", "aplicado_en": null, "ts": "<FECHA_FIRMA>", "nota": "laudo B2.4: resuelta en r2b por el test por punto de la suite (7 nodos anclados en 2.8.3.3, uno con «75 veces SMVM»; suite_perfil_r2.md:70); cambio de verificación declarado: test de la suite en lugar de chunk contra PDF", "evidencia": "docs/laudo_B2.4_sujetos.md"}
{"evento": "cambio_estado", "id": "BKL-0002", "estado": "verificado", "aplicado_en": null, "ts": "<FECHA_FIRMA>", "nota": "laudo B2.4: resuelta en r2b por el test por punto de la suite (35 nodos anclados en 3.5.3, 2 con la ventana de 3 días hábiles; suite_perfil_r2.md:71); cambio de verificación declarado", "evidencia": "docs/laudo_B2.4_sujetos.md"}
{"evento": "cambio_estado", "id": "BKL-0009", "estado": "verificado", "aplicado_en": null, "ts": "<FECHA_FIRMA>", "nota": "laudo B2.4: el patrón no reaparece en a9631a64 (cap::2.5), por la lectura de T3 y la segunda lectura a ciegas adjudicada; cambio de verificación declarado", "evidencia": "docs/laudo_B2.4_sujetos.md"}
{"evento": "cambio_estado", "id": "BKL-0010", "estado": "verificado", "aplicado_en": null, "ts": "<FECHA_FIRMA>", "nota": "laudo B2.4: el patrón no reaparece en a9631a64 (ext::14.5), por la lectura de T3 y la segunda lectura a ciegas adjudicada; cambio de verificación declarado", "evidencia": "docs/laudo_B2.4_sujetos.md"}
{"evento": "cambio_estado", "id": "BKL-0011", "estado": "verificado", "aplicado_en": null, "ts": "<FECHA_FIRMA>", "nota": "laudo B2.4: el patrón no reaparece en a9631a64 (ric::3.1), por la lectura de T3 y la segunda lectura a ciegas adjudicada; cambio de verificación declarado", "evidencia": "docs/laudo_B2.4_sujetos.md"}
{"evento": "cambio_estado", "id": "BKL-0012", "estado": "verificado", "aplicado_en": null, "ts": "<FECHA_FIRMA>", "nota": "laudo B2.4: el patrón no reaparece en a9631a64 (ext::13.4), por la lectura de T3 y la segunda lectura a ciegas adjudicada; cambio de verificación declarado", "evidencia": "docs/laudo_B2.4_sujetos.md"}
{"evento": "cambio_estado", "id": "BKL-0013", "estado": "verificado", "aplicado_en": null, "ts": "<FECHA_FIRMA>", "nota": "laudo B2.4: el patrón no reaparece en a9631a64 (colectivo de ext), por la lectura de T3 y la segunda lectura a ciegas adjudicada; cambio de verificación declarado", "evidencia": "docs/laudo_B2.4_sujetos.md"}
{"evento": "cambio_estado", "id": "BKL-0014", "estado": "verificado", "aplicado_en": null, "ts": "<FECHA_FIRMA>", "nota": "laudo B2.4: el patrón no reaparece en a9631a64 (ext::14.1), por la lectura de T3 y la segunda lectura a ciegas adjudicada; cambio de verificación declarado", "evidencia": "docs/laudo_B2.4_sujetos.md"}
{"evento": "cambio_estado", "id": "BKL-0015", "estado": "verificado", "aplicado_en": null, "ts": "<FECHA_FIRMA>", "nota": "laudo B2.4: el patrón no reaparece en a9631a64 (ext::3.17), por la lectura de T3 y la segunda lectura a ciegas adjudicada; cambio de verificación declarado", "evidencia": "docs/laudo_B2.4_sujetos.md"}
{"evento": "cambio_estado", "id": "BKL-0016", "estado": "verificado", "aplicado_en": null, "ts": "<FECHA_FIRMA>", "nota": "laudo B2.4: el patrón no reaparece en a9631a64 (ext::3.18), por la lectura de T3 y la segunda lectura a ciegas adjudicada; cambio de verificación declarado", "evidencia": "docs/laudo_B2.4_sujetos.md"}
{"evento": "nota", "id": "BKL-0018", "ts": "<FECHA_FIRMA>", "nota": "laudo B2.4: límite declarado junto con BKL-0004, que persiste como falla conocida sellada en la suite r2b (suite_perfil_r2.md:18); no se corrige en esta versión; queda en triaged", "evidencia": "docs/laudo_B2.4_sujetos.md"}
{"evento": "nota", "id": "BKL-0020", "ts": "<FECHA_FIRMA>", "nota": "laudo B2.4: cuarentena declarada (1 fila en r2b, «una entidad originante», cap::3.1.3::cierre, por debajo del umbral de la enmienda 4); queda en triaged", "evidencia": "docs/laudo_B2.4_sujetos.md"}
{"evento": "nota", "id": "BKL-0021", "ts": "<FECHA_FIRMA>", "nota": "laudo B2.4: la mención reaparece en r2b como «la entidad nominada» (control q de T3); cuarentena declarada, con el rol nuevo por el procedimiento de crecimiento de la enmienda 4 al cierre de la tanda 1; reemplaza la decisión (c) del 06/10/2026, que ninguna unidad ejecutó; resultado de la lectura de las 4 filas «entidad(es) encargada(s) del seguimiento»: <RESULTADO>; queda en triaged", "evidencia": "docs/laudo_B2.4_sujetos.md"}
```

## 6. Contradicciones de la ficha de la mesa, corregidas en este asiento

1. **«R2-1 está en `c98093a`»: no está en ningún documento del repo.** El repo cita `c98093a` como R1, que es correcto (la tabla de
   reprocesamiento, `:139`; la enmienda 4, `:28`; el mandato de U-RERESOL-CAT, `:187`), y R2-1 y R2-1 bis en `0737497`. La atribución
   errónea estaba en el pedido de la mesa al agente que juntó los hechos: es un error propio de la mesa, sin nada que corregir en el repo.
2. **Anclas corridas a la fila B2.4.** `plan:380` pasa a `:383` en el checklist (línea de las condiciones y fila X9), en
   `docs/tablero.md:324`, en `data/backlog/clasificacion_backlog_2026-10-04.md` (con una nota fechada al pie) y en `plan:403`. `:376` pasa
   a `:379`.
3. **Los conteos de la fila B2.4** (15, 16 y 17). Los 15 del título eran las entradas `triaged` de entonces, y suman 2 + 2 + 8 + 1 + 2 = 15:
   - BKL-0001 y 0002 (ausencias);
   - BKL-0008 y 0022 (alcanzabilidad, a A1.8 y U-NAV-DISENO);
   - BKL-0009 a 0016 (ocho de asignación de sujeto);
   - BKL-0018;
   - BKL-0020 y 0021 (sujetos de cuarentena sin padre).

   El «17» de `:379` suma BKL-0024 y 0025, ausencias resueltas por el pipeline que no entran a este laudo. Nota fechada en la fila del plan.
4. **BKL-0021:** la condición de cierre falló (la mención reaparece), y ni el plan ni el backlog lo registraban. Queda en la nota de la
   fila del plan y en el lote de eventos.
5. **BKL-0021 y BKL-0028 se pasaron a U-RERESOL-CAT, que no los tomó.** BKL-0021 queda resuelta por la decisión de este laudo, que
   reemplaza la (c) del 06/10. **BKL-0028** (el miembro del rol de ctacor; nota en `backlog.jsonl` del 01/10/2026) queda sin unidad:
   PENDIENTE de la autora, anotado en la fila del plan.
6. **«Re-sellado del grafo evaluado de la tanda 0»** (mandato de U-RERESOL-CAT, nota del 07/10, `:325`) contra los nombres D13, que
   reservan «el grafo evaluado» para el escalado (`docs/protocolo_dos_grafos.md`, §1, FIRMADO el 07/10/2026). Se agrega al pie de ese
   mandato la nota de equivalencia que el protocolo prescribe: donde dice «grafo evaluado de la tanda 0», léase «grafo sin cola de la
   tanda 0».

## Firma

BORRADOR — PENDIENTE de las dos lecturas del §4 y de la firma de la autora.
