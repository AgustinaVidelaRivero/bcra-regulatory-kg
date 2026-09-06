# B5.8.1 — corrida del modo de lectura sin raíz de sección

Reporte regenerable con:

```bash
python3 data/experiment/segmentacion_84/b581_sin_raiz/code/correr_b581.py
python3 data/experiment/segmentacion_84/b581_sin_raiz/code/generar_reporte_b581.py
```

Objetivo (recomputado de `censo_84.json`, familias a/c con veredicto que REMITE a B5.8.1): **41 TOs** (39 plenos + 2 parciales: manual, ri2_pm). Control adicional declarado: ri_acsf (familia a sin espina utilizable, vía B5.8.3; se espera que NO rinda). La fila del plan de reglas del censo dice 42 porque su corte es «familia a/c y no candidato», que suma ri_acsf y no remite a B5.8.1 — discrepancia declarada, no ajustada.

## 1. Resultado agregado

- **Rinden 41/41** (unidades > 0 y ≥1 raíz de lectura), 923 unidades de extracción en total.
- Health-check 'sano': 30/41; el resto declara señales (detalle §2).
- Control ri_acsf: rinde=NO (raíces 0, unidades 1) — esperado NO, vía B5.8.3.

## 2. Tabla por TO

| TO | fam | pág | roles (cuerpo/registro) | raíces (impl.) | unid. (term.+mini) | sub-chunk | rechazos | cob. | salud | rinde |
|---|---|--:|---|--:|--:|---|--:|---|---|---|
| asomut | c | 7 | 3/0 | 3 (0) | 8 (7+1) | — | 0 | sí | sano | sí |
| cedin | c | 22 | 16/0 | 14 (0) | 65 (54+11) | — | 0 | sí | sano | sí |
| ceninf | a | 23 | 20/0 | 10 (4) | 47 (37+10) | — | 9 | sí | cid | sí |
| dmrd | a | 72 | 72/0 | 6 (0) | 11 (11+0) | 1p/0np | 2 | sí | cid,unidades_anomalas_por_tamano | sí |
| manual | a | 2037 | 207/1830 | 2 (1) | 19 (16+3) | — | 84 | sí | cid | sí |
| micemp | c | 8 | 1/0 | 3 (0) | 7 (5+2) | — | 0 | sí | cid | sí |
| nmcief | c | 36 | 35/0 | 3 (0) | 40 (10+30) | — | 36 | sí | sano | sí |
| ri2_ae | c | 44 | 41/0 | 10 (1) | 18 (18+0) | 2p/0np | 135 | sí | unidades_anomalas_por_tamano | sí |
| ri2_cs | a | 31 | 31/0 | 3 (0) | 7 (7+0) | 1p/0np | 7 | sí | unidades_anomalas_por_tamano | sí |
| ri2_pm | a | 376 | 31/345 | 5 (2) | 27 (26+1) | — | 19 | sí | cid | sí |
| ri_ao | a | 1 | 1/0 | 3 (1) | 5 (5+0) | — | 0 | sí | sano | sí |
| ri_bdp | a | 3 | 3/0 | 3 (0) | 3 (3+0) | — | 10 | sí | sano | sí |
| ri_ccna | c | 60 | 58/0 | 8 (0) | 22 (17+5) | 1p/0np | 139 | sí | unidades_anomalas_por_tamano | sí |
| ri_ccpnp | a | 11 | 11/0 | 6 (0) | 6 (6+0) | — | 29 | sí | sano | sí |
| ri_cr | a | 5 | 5/0 | 3 (0) | 6 (5+1) | — | 5 | sí | sano | sí |
| ri_dsf | a | 31 | 31/0 | 19 (9) | 51 (48+3) | — | 503 | sí | sano | sí |
| ri_esd | a | 3 | 3/0 | 2 (0) | 3 (3+0) | — | 4 | sí | sano | sí |
| ri_icpipsp | a | 13 | 13/0 | 8 (0) | 9 (9+0) | — | 11 | sí | sano | sí |
| ri_ieccm | a | 1 | 1/0 | 3 (0) | 3 (3+0) | — | 0 | sí | sano | sí |
| ri_iepsp | a | 9 | 9/0 | 6 (0) | 6 (6+0) | — | 7 | sí | sano | sí |
| ri_iesinap | a | 6 | 6/0 | 6 (0) | 6 (6+0) | — | 5 | sí | sano | sí |
| ri_ii_31_12_19 | a | 21 | 21/0 | 6 (0) | 86 (76+10) | — | 2 | sí | sano | sí |
| ri_laft | a | 45 | 18/27 | 2 (1) | 7 (6+1) | — | 17 | sí | sano | sí |
| ri_mmsef | a | 9 | 9/0 | 2 (0) | 90 (56+34) | — | 82 | sí | sano | sí |
| ri_nge | a | 3 | 3/0 | 30 (0) | 30 (30+0) | — | 5 | sí | sano | sí |
| ri_niif | a | 86 | 86/0 | 7 (3) | 13 (13+0) | 1p/0np | 7 | sí | unidades_anomalas_por_tamano | sí |
| ri_oc | a | 28 | 28/0 | 6 (2) | 128 (124+4) | — | 20 | sí | sano | sí |
| ri_ot | a | 6 | 6/0 | 13 (0) | 30 (30+0) | — | 0 | sí | sano | sí |
| ri_pnp | a | 44 | 44/0 | 8 (0) | 23 (21+2) | 1p/0np | 126 | sí | unidades_anomalas_por_tamano | sí |
| ri_pspapt | a | 5 | 5/0 | 12 (0) | 13 (13+0) | — | 2 | sí | sano | sí |
| ri_psprca | a | 6 | 6/0 | 10 (0) | 12 (12+0) | — | 8 | sí | sano | sí |
| ri_rcl | a | 2 | 2/0 | 2 (0) | 3 (3+0) | — | 2 | sí | sano | sí |
| ri_saofe | a | 3 | 3/0 | 2 (0) | 25 (23+2) | — | 21 | sí | sano | sí |
| ri_secoexpo | a | 21 | 21/0 | 19 (0) | 20 (20+0) | — | 77 | sí | sano | sí |
| ri_sef | a | 10 | 10/0 | 14 (0) | 27 (27+0) | — | 29 | sí | sano | sí |
| ri_tar | a | 7 | 7/0 | 1 (0) | 2 (1+1) | — | 27 | sí | sano | sí |
| ri_transpa | c | 23 | 19/3 | 1 (0) | 2 (2+0) | 1p/0np | 28 | sí | unidades_anomalas_por_tamano | sí |
| ri_tvf | a | 5 | 5/0 | 2 (0) | 2 (2+0) | — | 18 | sí | sano | sí |
| ribspc | a | 2 | 2/0 | 4 (0) | 5 (5+0) | — | 1 | sí | sano | sí |
| seggar | c | 26 | 14/0 | 6 (1) | 33 (29+4) | — | 1 | sí | sano | sí |
| verac | c | 5 | 1/0 | 1 (1) | 3 (3+0) | — | 1 | sí | sano | sí |
| ri_acsf | a | 3 | 3/0 | 0 (0) | 1 (1+0) | — | 0 | sí | paginas_sin_seccion | NO |

## 3. Verificaciones transversales

- Cobertura exacta (cero pérdida) en 42/42 TOs.
- Activación por cero unidades vigentes: 42/42 (todos los TOs de la corrida entraron al modo tras comprobar cero unidades por el camino vigente).
- Sub-chunking de U-B5.3 sobre unidades nuevas: interviene en 7 TOs (dmrd, ri2_ae, ri2_cs, ri_ccna, ri_niif, ri_pnp, ri_transpa); detalle en `<to>/sub_chunking_<to>.json`.

