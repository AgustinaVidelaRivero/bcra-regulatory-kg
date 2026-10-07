# Tarea e: condiciones aisladas, definición vigente y redefinición

Fuente: `aisladas_e.json` (`udiag_e_aisladas.py`). (A) Condicion sin ninguna arista de contenido: sin contar `establecida_en` ni la remisión (`remite_a`; en los grafos del perfil r1, `referencia` con `rol_fuente = referencia_cruzada`). (A-literal) sin esa última exclusión. (B) sin `condicion_de` saliente.

| columna | grafo | sha256 | Condicion | vigente: sin ninguna arista | aislados de todo tipo | (A) | (A-literal) | (B) |
|---|---|---|---:|---:|---:|---:|---:|---:|
| r1 | KG-Reextraído-r1 | `0226e947…` | 0 | 0 | 105 | 0 | 0 | 0 |
| tanda 0 (perfil r1) | desarrollo r1 | `eab2fdd0…` | 1178 | 35 | 94 | 783 | 560 | 783 |
| tanda 0 (perfil r1) | cinco r1 | `4097d4fd…` | 205 | 7 | 38 | 101 | 79 | 101 |
| tanda 0 (perfil r1) | diez r1 | `dd42d6d9…` | 1383 | 42 | 120 | 884 | 639 | 884 |
| r2a | diez r2a | `99fe2bfa…` | 1409 | 0 | 16 | 232 | 232 | 232 |
| r2a | desarrollo r2a | `93a7af72…` | 1203 | 0 | 15 | 199 | 199 | 199 |
| r2b | diez r2b | `a9631a64…` | 1952 | 0 | 18 | 331 | 331 | 331 |
| r2b | desarrollo r2b | `6e756043…` | 1668 | 0 | 19 | 300 | 300 | 300 |
| r2b sin cola | diez r2b sin cola | `e22fae1a…` | 1868 | 0 | 18 | 322 | 322 | 322 |
| r2b sin cola | desarrollo r2b sin cola | `2922b72d…` | 1588 | 0 | 19 | 292 | 292 | 292 |

# Grupo H: `Operacion.tipo`

Fuente: `tipo_operacion_h.json` (`udiag_h_tipo_operacion.py`).

| grafo | Operacion | distintos tal cual | en minúsculas | sin diacríticos | normalizados | con un solo nodo |
|---|---:|---:|---:|---:|---:|---:|
| diez | 1824 | 1050 | 943 | 942 | 942 | 704 |
| sincola | 1761 | 1023 | 916 | 915 | 915 | 684 |

Los diez más frecuentes, normalizados (diez): calculo 59; financiacion 39; presentacion informativa 29; compra de moneda extranjera 27; clasificacion de deudor 27; acceso al mercado de cambios 25; incremento de exigencia por riesgo de credito 24; calculo de exigencia regulatoria 19; pago de importacion 18; emision de certificacion 18