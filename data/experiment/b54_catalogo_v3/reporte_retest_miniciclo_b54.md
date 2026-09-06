# Retests del mini-ciclo (laudo de cierre) — resultados contra predicciones selladas

Predicciones: `predicciones_retest_miniciclo_b54.md`, sha256
`553007f58cf9c64a9023c5edcb4c7ae5fd39b5de2fbb959f3af3a9c799d7a05a`, selladas
ANTES de la corrida (constancia horaria en la transcripción de la sesión).
Prefijo bajo prueba: `35e88c2dd0a2…` (namespace `54a111e2175f`). Corrida:
3/3 `stop=tool_use`, modelo resuelto `claude-haiku-4-5-20251001`, gasto
USD 0,0512 (tope 0,2098), cruce db==jsonl 3/3/3. Crudos en
`resultados_retest_miniciclo_b54.jsonl` y en la db (namespace nuevo).

**RESULTADO: 1 PASA / 2 FALLAN.** Por la regla del laudo de cierre («si un
retest FALLA su predicción, FRENAR sin iterar: la vuelta es con laudo, no con
retoque»), NO se aplicó ningún cambio adicional.

## R2 — `ayccef::2.1` (H4a def dirigida): **PASA** (3/3 cláusulas)

- `Sujeto_sector_publico_no_financiero`: AUSENTE ✓
- Cobertura: `Sujeto_entidad_financiera` + `sujeto_propuesto` «entidades
  públicas o mixtas de la Nación, provincias, municipalidades y CABA» ✓ —
  exactamente la resolución por válvula que la def dirigida buscaba.
- BCRA: fuera de los sujetos alcanzados ✓

## R1 — `cap::3.1.14::intro` (H1a rename): **FALLA** (0/2 cláusulas)

- «El originante de securitización NO se emite con el id renombrado»: NO SE
  CUMPLE — queda **1** emisión de `Sujeto_entidad_originante_de_transferencia`
  (`aplica_a` sobre la Obligación «Determinación de cumplimiento para
  posiciones retenidas», contexto de titulización). Mejora direccional
  observada y declarada (antes del rename: 2 emisiones; ahora 1, y la válvula
  recuperó «originante/fiduciario» e «inversores y tenedores de posiciones de
  titulización» como propuestos — esto último también en línea con H3), pero
  la predicción sellada pedía CERO y no se alcanzó.
- «El fiduciario se mantiene»: NO SE CUMPLE — `Sujeto_fiduciario_de_
  fideicomiso_financiero` no aparece como id; quedó subsumido en el propuesto
  «originante/fiduciario».

## R3 — `cryl::1.3` (H2a guarda del mensaje): **FALLA** (1/2 cláusulas)

- «El BCRA conserva sus `ejecuta`»: ✓ (2 `ejecuta` + 2 `aplica_a` de
  potestades de custodia).
- «El rol de alcance NO aparece en `ejecuta`»: NO SE CUMPLE — 2 `ejecuta` de
  `Sujeto_rol_alcance_cryl` (Operaciones «Registro de fideicomisos
  financieros» y «Aceptación de depósito en custodia»), idéntico patrón al de
  la ficha 4 adjudicada correcto-antes. La guarda del mensaje (H2a) no cambió
  la conducta en esta unidad; la vigilancia (7) de tanda 1 (H2c, ya laudada)
  queda como el instrumento que mide si el fenómeno es sistemático.

## Estado

FRENADO sin iterar. Los dos fallos quedan para laudo de la autora; los
insumos direccionales (2→1 en R1 con válvula recuperada; n=1 persistente en
R3 con BCRA intacto) constan arriba y en los crudos.
