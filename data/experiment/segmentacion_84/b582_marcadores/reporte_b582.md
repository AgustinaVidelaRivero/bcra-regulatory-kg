# B5.8.2 — corrida de las reglas de marcador por familia

Reporte regenerable con:

```bash
python3 data/experiment/segmentacion_84/b582_marcadores/code/correr_b582.py
python3 data/experiment/segmentacion_84/b582_marcadores/code/generar_reporte_b582.py
```

Objetivo (recomputado de `censo_84.json`, familias b_idx/b_sec con veredicto que REMITE a la regla de marcador de B5.8.2): **7 TOs**. El octavo TO de la familia b_idx del censo (ri_tsa, veredicto «regla vigente (B5.2)») corre como CONTROL declarado: produce unidades por el camino vigente y se espera que JAMÁS entre a las etapas nuevas; su re-corrida adjudicada es de B5.8.4.

## 1. Resultado agregado

- **Rinden 7/7** (unidades > 0 y ≥1 raíz de lectura), 317 unidades de extracción en total.
- Por etapa que produjo la lectura: marcadores 5 (reqcac, ri_dcpc, ri_msrl, ri_psp, seguef); sin_raiz sobre roles de marcadores 2 (consyr, nmaeef).
- Health-check 'sano': 4/7; el resto declara señales (detalle §2).
- Control ri_tsa: modo=vigente, activado_por_cero=NO — esperado modo vigente sin activación (un TO que produce unidades jamás entra a las etapas nuevas).

## 2. Tabla por TO

| TO | fam | pág | modo | roles (índice/cuerpo) | secciones/raíces | unid. (term.+mini) | sub-chunk | rechazos | saltos | cob. | salud | rinde |
|---|---|--:|---|---|---|--:|---|--:|--:|---|---|---|
| consyr | b_idx | 11 | sin_raiz | 1/6 | 1,2,3 | 32 (28+4) | — | 1 | 0 | sí | cid | sí |
| nmaeef | b_idx | 69 | sin_raiz | 1/68 | 1,2,3,4,5,6,7,8,9,10,… | 39 (38+1) | 1p/0np | 198 | 2 | sí | unidades_anomalas_por_tamano | sí |
| reqcac | b_sec | 10 | marcadores | 1/8 | A,B,C | 3 (3+0) | — | 0 | 0 | sí | paginas_sin_seccion | sí |
| ri_dcpc | b_idx | 44 | marcadores | 2/42 | 1,2,3,4,5,6,7 | 129 (61+68) | — | 16 | 0 | sí | sano | sí |
| ri_msrl | b_idx | 20 | marcadores | 1/19 | 1,2,3,4,5,6,7,8 | 11 (10+1) | — | 4 | 1 | sí | sano | sí |
| ri_psp | b_idx | 14 | marcadores | 1/13 | I,II,III,IV,VI | 5 (5+0) | — | 2 | 1 | sí | sano | sí |
| seguef | b_idx | 25 | marcadores | 1/16 | 1,2,3,4,5,6 | 98 (82+16) | — | 4 | 0 | sí | sano | sí |
| ri_tsa | b_idx | 92 | vigente | 1/30 | 1,2,3,4,5,1,2,3,4 | 15 (14+1) | — | 21 | 1 | sí | paginas_sin_seccion | sí |

## 3. Verificaciones transversales

- Cobertura exacta (cero pérdida) en 8/8 TOs.
- Activación por cero unidades vigentes en los 7 objetivo: 7/7 (todos comprobaron cero unidades por el camino vigente antes de entrar).
- Sub-chunking de U-B5.3 sobre unidades nuevas: interviene en 1 TOs (nmaeef); detalle en `<to>/sub_chunking_<to>.json`.
- Límite medido DECLARADO (sin regla nueva, territorio B5.8.4): nmaeef — reinicio de numeración por ANEXO (jerarquía alternativa): el marcador de índice se reconoce y el modo sin raíz abre 13 raíces, pero las raíces 1–11 provienen de la página-lista del Anexo I y el cuerpo de los anexos posteriores ancla bajo la última raíz abierta (198 rechazos registrados, señal C8 con partición de sub-chunking); mismo patrón que ri_tar/ri_transpa en B5.8.1.

