# B5.8.3 — corrida del parser de tablas (e0_tablas.py)

Reporte regenerable con:

```bash
python3 data/experiment/segmentacion_84/b583_tablas/code/correr_b583.py
python3 data/experiment/segmentacion_84/b583_tablas/code/generar_reporte_b583.py
```

Objetivo (recomputado — regla i): **30 TOs** = 27 con familia tabular d/d_dominante en el censo B5.8.0 ∪ 4 con páginas ficha_registro declaradas por B5.8.1 (solo por esta vía: manual, ri2_pm, ri_transpa). Control testigo aparte: capmin (dev, RX-10).

## 1. Resultado agregado

- **Rinden 29/30** (≥1 tabla lógica parseada): 559 tablas parseadas de 563 lógicas (4 declaradas con causa, no emitidas), 643 segmentos físicos, 80 costuras aplicadas, 9481 filas, 39 notas al pie asociadas, sobre 510 páginas con tabla de contenido.
- **ri2_pm NO rinde, declarado**: 0 tablas de contenido con contenido (descartes por regla: {'min_filas': 1077, 'sin_contenido': 1}); su material dominante es ficha de registro — parser de registro, fuera de B5.8.1-3 (censo B5.8.0), adjudicación en B5.8.4.
- **Testigo RX-10 (capmin 1.2): resuelto=True** — pares por columna {'Bancos': '5.000', 'Restantes entidades': '2.500'} (el chunk linealizado había invertido los montos en el grafo); pérdida de reconstrucción 0.0.

## 2. Tabla por TO

| TO | pág | pág c/tabla | lógicas | parseadas | declaradas | segmentos | costuras | cand. | filas | notas | títulos | rinde |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| ceninf | 23 | 9 | 12 | 12 | 0 | 14 | 2 | 0 | 103 | 4 | 0 | sí |
| dmrd | 72 | 52 | 53 | 53 | 0 | 55 | 2 | 6 | 812 | 3 | 1 | sí |
| manual | 2037 | 11 | 11 | 11 | 0 | 11 | 0 | 0 | 132 | 0 | 0 | sí |
| ri2_cs | 31 | 30 | 47 | 47 | 0 | 47 | 0 | 0 | 549 | 5 | 0 | sí |
| ri2_pm | 376 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | NO |
| ri_acsf | 3 | 2 | 1 | 1 | 0 | 2 | 1 | 0 | 34 | 0 | 0 | sí |
| ri_ai | 9 | 5 | 5 | 5 | 0 | 5 | 0 | 0 | 35 | 0 | 0 | sí |
| ri_cc | 118 | 46 | 51 | 51 | 0 | 52 | 1 | 2 | 694 | 3 | 2 | sí |
| ri_ccna | 60 | 11 | 6 | 6 | 0 | 11 | 5 | 1 | 162 | 0 | 0 | sí |
| ri_ccpnp | 11 | 8 | 15 | 15 | 0 | 15 | 0 | 0 | 251 | 0 | 0 | sí |
| ri_cr | 5 | 3 | 2 | 2 | 0 | 3 | 1 | 0 | 60 | 0 | 0 | sí |
| ri_dsf | 31 | 7 | 2 | 2 | 0 | 7 | 5 | 0 | 242 | 0 | 0 | sí |
| ri_esd | 3 | 2 | 2 | 2 | 0 | 2 | 0 | 0 | 40 | 0 | 0 | sí |
| ri_gerc | 8 | 3 | 4 | 4 | 0 | 4 | 0 | 0 | 21 | 0 | 0 | sí |
| ri_laft | 45 | 41 | 8 | 8 | 0 | 43 | 35 | 1 | 1209 | 0 | 8 | sí |
| ri_msrl | 20 | 7 | 5 | 5 | 0 | 7 | 2 | 0 | 151 | 0 | 2 | sí |
| ri_niif | 86 | 63 | 67 | 64 | 3 | 72 | 5 | 2 | 1712 | 10 | 8 | sí |
| ri_oc | 28 | 9 | 53 | 53 | 0 | 53 | 0 | 5 | 263 | 0 | 0 | sí |
| ri_pgn | 19 | 5 | 6 | 6 | 0 | 6 | 0 | 0 | 110 | 0 | 0 | sí |
| ri_pnp | 44 | 20 | 23 | 23 | 0 | 25 | 2 | 1 | 748 | 5 | 0 | sí |
| ri_psp | 14 | 6 | 9 | 9 | 0 | 9 | 0 | 1 | 146 | 0 | 0 | sí |
| ri_pspapt | 5 | 5 | 11 | 11 | 0 | 11 | 0 | 0 | 61 | 0 | 0 | sí |
| ri_psprca | 6 | 6 | 9 | 9 | 0 | 9 | 0 | 0 | 54 | 0 | 0 | sí |
| ri_rml | 77 | 40 | 39 | 39 | 0 | 46 | 7 | 4 | 533 | 0 | 1 | sí |
| ri_secoexpo | 21 | 7 | 7 | 7 | 0 | 7 | 0 | 2 | 77 | 0 | 0 | sí |
| ri_sef | 10 | 4 | 3 | 3 | 0 | 4 | 1 | 0 | 48 | 0 | 0 | sí |
| ri_transpa | 23 | 21 | 21 | 21 | 0 | 21 | 0 | 0 | 108 | 0 | 0 | sí |
| ri_tsa | 92 | 38 | 30 | 30 | 0 | 40 | 10 | 1 | 630 | 9 | 3 | sí |
| snp_dd | 68 | 18 | 18 | 18 | 0 | 18 | 0 | 1 | 133 | 0 | 0 | sí |
| snp_tr | 62 | 31 | 43 | 42 | 1 | 44 | 1 | 3 | 363 | 0 | 0 | sí |

## 3. Tablas declaradas (guardas: se declaran, no se emiten mal)

- `ri_niif::tabla013` (p.25): ['perdida_reconstruccion'] — pérdida de reconstrucción 52%.
- `ri_niif::tabla038` (p.53): ['perdida_reconstruccion'] — pérdida de reconstrucción 22%.
- `ri_niif::tabla063` (p.83): ['perdida_reconstruccion'] — pérdida de reconstrucción 55%.
- `snp_tr::tabla014` (p.24): ['perdida_reconstruccion'] — pérdida de reconstrucción 52%.

## 4. Costuras candidatas no fusionadas (geometría sin encabezado repetido — se declaran, jamás se cosen)

Total: 30. Detalle por TO en `<to>/resumen_<to>.json` (clave `costuras_candidatas`) y filas completas en `<to>/tablas_<to>.json`.

## 5. Verificación de reconstrucción (decisión 4)

- Caracteres perdidos declarados (todas las tablas, parseadas y declaradas): 646. Toda tabla parseada con pérdida > 20 % fue movida a declarada (regla R-VERIF); el detalle por segmento vive en `tablas_<to>.json` → `verificacion`.
