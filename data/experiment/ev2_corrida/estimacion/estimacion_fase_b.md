# Estimación parametrizada — fase B corrida EV2 (sin precios)

Generado: 2026-08-13T19:12:22. Alcance: fase B de esta unidad: corrida del agente, N=1, ambos ejes, tres grafos. NO incluye: re-corridas N=3 sobre 'parcial', auditoría del 10%, ni juez de fidelidad (etapas posteriores con su propia autorización).

| grafo | fid | nav (2×presentes) | corridas | T_in | T_out | T_cw | T_cr | fuente |
|---|---|---|---|---|---|---|---|---|
| v2 | 40 | 88 | 128 | 4790 | 1598 | 11966 | 45310 | proxy conservador: máximo por campo entre posthoc_run/summary_escalon1b_r3_reensamblado_v3.json, posthoc_run/summary_off_run_3.json, posthoc_run/summary_u6_exploracion_reensamblado_v3.json (v2 no tiene corrida histórica) |
| v3 | 40 | 128 | 168 | 3007 | 1200 | 9603 | 33793 | posthoc_run/summary_escalon1b_r3_reensamblado_v3.json |
| run_3 | 40 | 120 | 160 | 4790 | 1361 | 11285 | 45153 | posthoc_run/summary_off_run_3.json |

**Total corridas: 456.** Tokens totales estimados: in 1,884,696 / out 623,904 / cache_write 4,950,552 / cache_read 18,701,384.

```
USD_total = ( Tot_in  × P_in
            + Tot_out × P_out
            + Tot_cw  × P_cache_write
            + Tot_cr  × P_cache_read ) / 1e6
```

Precios (USD/MTok) como variables, a resolver en la autorización: P_in, P_out, P_cache_write, P_cache_read.

el selftest offline usa cliente falso: sus tokens no son medición; los T_* salen de las corridas históricas citadas en fuente_tokens.
