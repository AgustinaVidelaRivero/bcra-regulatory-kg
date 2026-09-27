# Lo que NO está en el inventario — U-B2.1 fase 1 (re-diagnóstico), pieza c

Entradas de `data/backlog/backlog.jsonl` (sha256 `d8473501b442432ec7b2f698cbb4d2d618e3db1f0947698407b311ac1a07e2a4`)
cuyo estado efectivo NO es `aplicado` ni `verificado`. Solo se cuentan y se listan
por id; no entran al inventario de la pieza a.

Regla de estado efectivo (mandato, decisión 2.i): última línea del id, en orden
de archivo, que trae el campo `estado`. Reconstrucción y salida completa:
`reports/revision_UB21_diag/estado_backlog_B21_fase1.py` →
`estado_backlog_B21_fase1_salida.txt`. Comando:

```
PYTHONDONTWRITEBYTECODE=1 python3 reports/revision_UB21_diag/estado_backlog_B21_fase1.py
```

## Conteo

| Estado efectivo | Ids | Fuente |
|---|---|---|
| `triaged` | **17** | `estado_backlog_B21_fase1_salida.txt`, línea «estado efectivo por valor: {'triaged': 17, 'verificado': 12}» |
| `nuevo` | 0 | ídem (todo `nuevo` tiene un `cambio_estado` a `triaged` posterior: BKL-0023/0024/0025) |
| sin estado en ninguna línea | 0 | ídem (los 29 ids tienen al menos una línea con `estado`) |
| **Total fuera del inventario** | **17** | 29 ids − 12 cerrados = 17 |

## Lista por id (estado efectivo `triaged`, con la línea del archivo que lo fija)

| Id | Línea que fija el estado | Líneas del id | Observación (solo del propio archivo) |
|---|---|---|---|
| BKL-0001 | 1 | 2 | evento `retriage_v3` (línea 23) sin `cambio_estado` posterior |
| BKL-0002 | 2 | 2 | evento `retriage_v3` (línea 24) sin `cambio_estado` posterior |
| BKL-0008 | 8 | 2 | `retriage_v3` (línea 30) |
| BKL-0009 | 9 | 2 | `retriage_v3` (línea 31) |
| BKL-0010 | 10 | 2 | `retriage_v3` (línea 32) |
| BKL-0011 | 11 | 2 | `retriage_v3` (línea 33) |
| BKL-0012 | 12 | 2 | `retriage_v3` (línea 34) |
| BKL-0013 | 13 | 2 | `retriage_v3` (línea 35) |
| BKL-0014 | 14 | 2 | `retriage_v3` (línea 36) |
| BKL-0015 | 15 | 2 | `retriage_v3` (línea 37) |
| BKL-0016 | 16 | 2 | `retriage_v3` (línea 38) |
| BKL-0018 | 18 | 1 | sin eventos posteriores |
| BKL-0020 | 20 | 1 | sin eventos posteriores |
| BKL-0021 | 21 | 1 | sin eventos posteriores |
| BKL-0022 | 22 | 3 | dos eventos `nota` (líneas 55 y 72), ninguno con `estado` |
| BKL-0024 | 57 | 2 | entrada `nuevo` (56) → `triaged` (57) |
| BKL-0025 | 59 | 2 | entrada `nuevo` (58) → `triaged` (59) |

Recuento de la lista: 17 filas (2 + 9 + 1 + 3 + 2 = 17; verificado contra la
línea «NO CERRADOS: 17» de la salida).

## Notas de alcance

- **BKL-0024 y BKL-0025** están en esta lista (estado efectivo `triaged`, líneas
  57 y 59) aunque la fila B2.1 del plan los nombra entre los «BKL cerrados»
  (`git show HEAD:docs/plan_tesis.md | grep -n "cada BKL cerrado (C1–C7, BKL-0024/0025, RT-\*)"`
  → `:324`). Es una de las dos contradicciones esperadas por la decisión 5 del
  mandato; se asienta como «coincide» en `tabla_resumen_B21_fase1.md` y su
  sondeo de anclas (fuera del inventario) está en
  `sonda_anclas_C1_C7_UB21_salida.txt`, filas `X.BKL-0024_ext_3_9_usd200` y
  `X.BKL-0025_pro_1_1_1_usuario`.
- **Ids `RT-`**: ninguno en el backlog (`grep -c '"id": "RT-' data/backlog/backlog.jsonl`
  → 0; salida del script: «ids con prefijo RT-: 0»). Las 12 preguntas RT del
  inventario viven en las propuestas y en el retest C7 (pieza a, grupo i-RT).
- Los 17 ids de esta lista no se reclasifican ni se juzgan acá: el mandato
  pide solo contarlos y listarlos.
