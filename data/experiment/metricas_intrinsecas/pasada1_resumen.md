# Pasada 1 — Métricas intrínsecas: baseline y cruce contra las predicciones §7

**Gobernada por:** `docs/spec_evaluacion_intrinseca.md` (sellada en commit `cdf90e6`).
**Script congelado:** `scripts/metricas_intrinsecas.py`,
sha256 `d5a88b798c0f3e76ab096eda1019c26248ef3012b38c32eeb510f09b40f96733`
(hash registrado en el log de la unidad ANTES de la primera corrida completa).
**RapidFuzz:** 3.14.5 (instalada en `.venv`; la etapa 1 de M1/M2 depende de ella).
**Custodia (método U0):** el ensamblador real reproduce los kg congelados —
grafo_v2 OK (3.872 nodos / 7.231 triples), reensamblado_v3 OK (4.458 / 8.044).
**Costo:** USD 0 (cero llamadas a API). **Fecha:** 2026-07-31.

Esta pasada es descriptiva y SIN umbrales (spec §8). Este documento contiene el
baseline y el cruce contra §7, sin lectura alguna más allá del cruce.

---

## 1. Tabla descriptiva — M1..M10 por grafo (numerador/denominador explícitos)

| Métrica | grafo_v2 (defecto) | reensamblado_v3 | run_3_ppf_core |
|---|---|---|---|
| M1 tasa_duplicacion_publicada | 0.600981 (2327/3872) | 0.637730 (2843/4458) | 0.672593 (2724/4050) |
| M2 tasa_duplicacion_gate | 0.380682 (1474/3872) | 0.401974 (1792/4458) | 0.417531 (1691/4050) |
| M3 tasa_conflacion | 0.281367 (1729/6145) | 0.265256 (1630/6145) | no_computable¹ |
| M4 average_degree | 3.735021 (14462/3872) | 3.608793 (16088/4458) | 3.276049 (13268/4050) |
| M5 avg_shortest_path | 3.795069 (53695988/14148882) | 3.754115 (69850114/18606282) | 3.605800 (50261326/13939022) |
| M6 grado_max | 1299 | 1512 | 1224 |
| M6 participacion_top1pct | 0.386254 (5586/14462) | 0.382832 (6159/16088) | 0.370892 (4921/13268) |
| M6 gini_grado | 0.557962 | 0.554714 | 0.580311 |
| M7 tasa_ruido_por_rol | 0.164514 (637/3872) | 0.129430 (577/4458) | no_computable² |
| M8 densidad | 0.00048244 (7231/14988512) | 0.00040485 (8044/19869306) | 0.00040455 (6634/16398450) |
| M9 nodos_aislados | 110 | 144 | 310 |
| M9 componentes_conexas | 111 | 145 | 314 |
| M9 fraccion_en_componente_mayor | 0.971591 (3762/3872) | 0.967699 (4314/4458) | 0.921975 (3734/4050) |
| M10 chunks_mudos | 0.144022 (53/368) | 0.000000 (0/368) | no_computable³ |
| M11 cobertura_CQ | no medida en esta unidad — régimen especial de la spec §6 (medición única separada) | ídem | ídem |

Motivos de no_computable (run_3, pipeline de la Fase 2.2):
¹ M3: sin caché de extracción en el formato de `cache_v2` — no hay conteo de
menciones pre-fusión atribuible.
² M7: `chunk_roles.py` reproduce el chunker de grafo_v2; los chunks de run_3 no
tienen rol documental atribuible.
³ M10: misma razón — sin roles ni atribución chunk→nodo replicable. (La unidad
solo eximía M3/M7 para run_3; M10 comparte exactamente la misma dependencia de
la spec §4 — `chunk_roles.py` + caché v2 — y se reporta igual de no computable.)

Notas de cómputo (convenciones de la spec §4, registradas en los JSON):
- M1/M2: 0 labels vacíos en los tres grafos. Conteos por tipo en cada JSON.
- M4: aristas repetidas removidas = 0, self-loops = 0, aristas con extremo
  inexistente (dangling) = 0 e ids de nodo duplicados = 0, en los tres grafos.
- M3: denominador compartido v2/v3 = 6.145 menciones de entidad extraídas en los
  508 resultados del caché (0 con error); menciones de tipo inválido excluidas
  del mapeo = 0 en ambos; nodos con fusión (≥2 menciones): 474 (v2) / 411 (v3).
- M10: denominador = 368 chunks de rol `cuerpo` de `chunks_all.json` (aguas
  arriba). Los 53 mudos de v2 son íntegramente chunks de articulado descartados
  por el desempate del ensamblado v2 (motivo `descartado_por_desempate` en el
  detalle del JSON).

## 2. M7 en grafo_v2 — nodos atribuidos a roles no normativos (conteo por rol)

| Rol no normativo | Nodos de v2 |
|---|---|
| `tabla_norma_origen` | 612 |
| `indice` | 25 |
| **Total (numerador M7)** | **637** |

(En reensamblado_v3: 577, todos `tabla_norma_origen`; el índice está excluido
del ensamblado v3 por diseño.) La lista completa de los 637 ids está en
`grafo_v2.json`, campo `metricas.M7_tasa_ruido_por_rol.notas.nodos`.

---

## 3. Cruce contra las predicciones pre-registradas (spec §7), una por una

| Pred. | Enunciado (mecanismo en la spec) | Dato | Resultado |
|---|---|---|---|
| P-a | aristas/nodos (M4) del grafo con el defecto MAYOR que el re-ensamblado | v2 3.735021 > v3 3.608793 | **CONFIRMADA** |
| P-b (CRUX) | M1 publicada IGUAL O MAYOR en el re-ensamblado (el corregido se ve PEOR en la métrica publicada) | v3 0.637730 > v2 0.600981 | **CONFIRMADA** |
| P-c | M6 mayor en el grafo con el defecto | participacion_top1pct: v2 0.386254 > v3 0.382832 → confirmada; gini_grado: v2 0.557962 > v3 0.554714 → confirmada; grado_max: v2 1299 < v3 1512 → refutada | **PARCIAL (2 de 3 componentes)** |
| P-d | dos ramas admisibles para M5, sin expectativa | v3 3.754115 < v2 3.795069 → menor en el corregido | **RAMA (ii)** |
| P-e | dos ramas admisibles para M9, sin expectativa | aislados 110→144, componentes 111→145 (v2→v3) → aumentan en el corregido | **RAMA (ii)** |

**VÁLVULA (spec §7):** P-b resultó en la dirección pre-registrada (v3 ≥ v2 en
M1). La válvula NO se activa: el trabajo no vuelve a discusión por esta vía.

Sin lectura adicional en este documento: las lecturas de resultados son una
etapa posterior (spec §8; los umbrales de la pasada 2 son otra unidad y otro
commit).
