# Resumen de población — adjudicación EV2 (SOLO_MESA: contiene grafo)

generado: 2026-08-16T22:30:19

## Tabla final pre-adjudicación por grafo (correcto / parcial / incorrecto / req.adj.)

| grafo | correcto | parcial | incorrecto | req.adj. | esperado |
|---|---|---|---|---|---|
| v2 | 3 | 20 | 7 | 10 | 3/20/7/10 |
| v3 | 4 | 17 | 7 | 12 | 4/17/7/12 |
| run_3 | 2 | 13 | 17 | 8 | 2/13/17/8 |

- tabla_final_ok: **True**
- heredados (base, final req.adj.): 21 (esperado 21); por grafo {'run_3': 6, 'v2': 7, 'v3': 8}
- pendientes §7: 9 (esperado 9); por grafo {'run_3': 2, 'v2': 3, 'v3': 4}
- votos requiere_adjudicacion dentro de los 9 pendientes: **17** (mandato esperaba 24); en pares decididos por invariancia: 7; total de respuestas §7 con veredicto req.adj.: 24
- fichas s7_pendiente: 15 (textos idénticos colapsados: 2)
- muestra correcto por grafo: {'v2': 1, 'v3': 1, 'run_3': 1} (esperado {'v2': 1, 'v3': 1, 'run_3': 1})
- muestra parcial+incorrecto por grafo: {'v2': 3, 'v3': 3, 'run_3': 3} (esperado {'v2': 3, 'v3': 3, 'run_3': 3}); muestra_ok: **True**
- fichas: 48; por origen {'heredado_base': 21, 's7_pendiente': 15, 'muestra_parcial_incorrecto': 9, 'muestra_correcto': 3}; respuestas cubiertas {'heredado_base': 21, 's7_pendiente': 17, 'muestra_correcto': 3, 'muestra_parcial_incorrecto': 9}

## Pendientes §7 (votos r1/r2/r3 y respuestas a adjudicar)

| id_pregunta | grafo | id_opaco_base | votos | ids ADJ | fichas |
|---|---|---|---|---|---|
| EV2F-019 | run_3 | EV2R-bf64c7e08b | requiere_adjudicacion/parcial/requiere_adjudicacion | EV2E-a8323388a6 (r1), EV2E-fa3396d9b7 (r3) | ADJ-6cc24f93, ADJ-8e4f2450 |
| EV2F-026 | run_3 | EV2R-0860d0b8a5 | requiere_adjudicacion/requiere_adjudicacion/requiere_adjudicacion | EV2E-99fa925de0 (r1), EV2E-1825eb24c9 (r2), EV2E-8b197ea030 (r3) | ADJ-80fa6a9d, ADJ-eef4a997, ADJ-f5b6657f |
| EV2F-009 | v2 | EV2R-566d06d654 | requiere_adjudicacion/parcial/requiere_adjudicacion | EV2E-097a21d570 (r1), EV2E-4df762be18 (r3) | ADJ-7d63cd1b |
| EV2F-013 | v2 | EV2R-86092f6789 | requiere_adjudicacion/requiere_adjudicacion/requiere_adjudicacion | EV2E-f108ccb3af (r1), EV2E-ffc38b04c3 (r2), EV2E-868a9dfcae (r3) | ADJ-169b5314, ADJ-ad64454a, ADJ-f6066492 |
| EV2F-014 | v2 | EV2R-c78b3683c5 | incorrecto/parcial/requiere_adjudicacion | EV2E-d78fa0b5a6 (r3) | ADJ-20edbe06 |
| EV2F-012 | v3 | EV2R-534c224349 | correcto/incorrecto/requiere_adjudicacion | EV2E-c420ad5a84 (r3) | ADJ-8fffa849 |
| EV2F-017 | v3 | EV2R-2e505e4272 | parcial/incorrecto/requiere_adjudicacion | EV2E-4062520de2 (r3) | ADJ-ac03b407 |
| EV2F-029 | v3 | EV2R-aeb1d5a938 | requiere_adjudicacion/requiere_adjudicacion/parcial | EV2E-5683ed3e2d (r1), EV2E-519119b6fe (r2) | ADJ-6b4b8444, ADJ-cbff1958 |
| EV2F-039 | v3 | EV2R-d25b8279f2 | parcial/requiere_adjudicacion/requiere_adjudicacion | EV2E-d616573dcc (r2), EV2E-96ff4d4967 (r3) | ADJ-b61bd355 |

## Muestra simétrica §6

| grafo | estrato | id_pregunta | final juez | fuente | respuesta en ficha |
|---|---|---|---|---|---|
| v2 | correcto | EV2F-028 | correcto | base | EV2R-df1f00c307 (base) |
| v3 | correcto | EV2F-002 | correcto | base | EV2R-7d9c9100a7 (base) |
| run_3 | correcto | EV2F-032 | correcto | base | EV2R-0d820c5f77 (base) |
| v2 | parcial_incorrecto | EV2F-004 | parcial | enc | EV2E-9d28df5dd1 (r1) |
| v2 | parcial_incorrecto | EV2F-021 | parcial | enc | EV2E-679f177086 (r1) |
| v2 | parcial_incorrecto | EV2F-038 | parcial | enc | EV2E-44d39e4f08 (r1) |
| v3 | parcial_incorrecto | EV2F-005 | parcial | enc | EV2E-9517115c3c (r1) |
| v3 | parcial_incorrecto | EV2F-016 | parcial | enc | EV2E-2aeb63e20b (r1) |
| v3 | parcial_incorrecto | EV2F-021 | parcial | enc | EV2E-9948ecb88e (r1) |
| run_3 | parcial_incorrecto | EV2F-005 | parcial | enc | EV2E-fff7cb04cd (r1) |
| run_3 | parcial_incorrecto | EV2F-017 | incorrecto | base | EV2R-d7a1118272 (base) |
| run_3 | parcial_incorrecto | EV2F-037 | parcial | enc | EV2E-5e73a40650 (r1) |

## Heredados (base, final req.adj.)

| grafo | id_pregunta | id_opaco_base | ficha |
|---|---|---|---|
| run_3 | EV2F-004 | EV2R-770383d684 | ADJ-aa52c12d |
| run_3 | EV2F-014 | EV2R-880b3bd1e3 | ADJ-26ff7058 |
| run_3 | EV2F-018 | EV2R-4cfdb0d556 | ADJ-f659fc57 |
| run_3 | EV2F-030 | EV2R-0e7df6e78b | ADJ-07343665 |
| run_3 | EV2F-033 | EV2R-19bfa9f3d4 | ADJ-db1cacfa |
| run_3 | EV2F-034 | EV2R-aa57ae7a53 | ADJ-bebfbbf4 |
| v2 | EV2F-010 | EV2R-49130626ed | ADJ-1188dd99 |
| v2 | EV2F-011 | EV2R-ab046e2162 | ADJ-cedaef17 |
| v2 | EV2F-018 | EV2R-92a92b1a02 | ADJ-0afe0c36 |
| v2 | EV2F-023 | EV2R-bc28232739 | ADJ-cd8b15da |
| v2 | EV2F-029 | EV2R-42b8a4d5b5 | ADJ-15450b19 |
| v2 | EV2F-034 | EV2R-da217a3f78 | ADJ-88b1d0af |
| v2 | EV2F-039 | EV2R-02e54578ef | ADJ-9e226344 |
| v3 | EV2F-009 | EV2R-c822b6fb54 | ADJ-4e8501c1 |
| v3 | EV2F-014 | EV2R-2c98b1dd2e | ADJ-b16a650e |
| v3 | EV2F-019 | EV2R-bedd1e124f | ADJ-154d5c45 |
| v3 | EV2F-026 | EV2R-d73e1114a9 | ADJ-40616ec6 |
| v3 | EV2F-030 | EV2R-48605998a9 | ADJ-61cfa2dc |
| v3 | EV2F-034 | EV2R-449017854e | ADJ-0f27d616 |
| v3 | EV2F-035 | EV2R-e6f1e5d37c | ADJ-5cef4061 |
| v3 | EV2F-036 | EV2R-7fd46d1c7d | ADJ-13f0a36d |
