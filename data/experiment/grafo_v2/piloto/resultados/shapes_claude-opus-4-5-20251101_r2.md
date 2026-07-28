# Shapes v2 — kg_claude-opus-4-5-20251101_r2.json

- Grafo: `../piloto/resultados/kg_claude-opus-4-5-20251101_r2.json`
- Fecha: 2026-07-26
- Nodos: 227 | Aristas: 369

| Regla | Resultado | Resumen |
|---|---|---|
| S1 | PASS | 369/369 válidas; 0 violaciones. |
| S2 | PASS | 0 aristas colgantes sobre 369. |
| S3 | PASS | 369/369 conformes; 0 violaciones. |
| S4 | PASS | Nodos OK: 227/227. Aristas OK: 369/369. Violaciones: 0. |
| S5 | PASS | Nodos OK: 227/227. Aristas OK: 369/369. Violaciones: 0. |
| S6 | PASS | Conjunto válido: 5 TOs + esquema. Violaciones: 0. |
| S7 | PASS | 0 grupos violatorios (0 nodos). |
| S8 | WARN | 1 grupos cross-type. |
| S9 | PASS | 0 nodos con ambas keys. |
| S10 | PASS | Sin establecida_en: Obligacion=0, Restriccion=0, Excepcion=0 (total 0). |
| S11 | PASS | Sin aplica_a: Obligacion=0, Restriccion=0 (total 0). |
| S12 | FAIL | 8 Excepciones huérfanas. |
| S13 | PASS | 76/76 Sujetos con nivel válido; 0 violaciones. |

## S8 — detalle

```
'clasificacion de deudores': [TextoOrdenado] TextoOrdenado_to_clasificacion_deudores_actual_pdf, [Operacion] Operacion_clasificacion
```

## S12 — detalle

```
Excepcion_la_entidad_que_consolide_podra_adicionar_el_importe_registrado_en_la_partida_esp
Excepcion_se_podra_adicionar_el_importe_correspondiente_a_la_llave_de_negocio_negativa_reg
Excepcion_los_creditos_para_consumo_o_vivienda_estan_excluidos_de_la_cartera_comercial
Excepcion_no_se_consideraran_dentro_de_ese_concepto_las_refinanciaciones_otorgadas_a_produ
Excepcion_las_facilidades_adicionales_que_se_otorguen_respecto_de_los_margenes_vigentes_ac
Excepcion_las_renovaciones_periodicas_de_credito_para_capital_de_trabajo_ni_las_nuevas_fin
Excepcion_quedan_exceptuadas_las_importaciones_realizadas_por_empresas_que_presten_servici
Excepcion_las_entidades_podran_dar_acceso_al_mercado_de_cambios_para_cursar_pagos_de_servi
```
