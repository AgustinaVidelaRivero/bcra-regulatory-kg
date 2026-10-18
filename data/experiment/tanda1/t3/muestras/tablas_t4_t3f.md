#### Tabla T1. La población de cada muestra, por celda (`muestras/poblaciones_t4.json`, 2026-10-18T10:06:19-03:00)

| muestra | elemento | N | RI:sin_raiz | RI:resto | NG:sin_raiz | NG:resto | se lee entera, sin celdas |
|---|---|---:|---:|---:|---:|---:|---|
| cola | unidad | 42 | 6 | 5 | 0 | 31 | False |
| aceptadas:items | unidad | 1.136 | 147 | 13 | 25 | 951 | False |
| aceptadas:no_items | unidad | 2.116 | 144 | 143 | 69 | 1.760 | False |
| vigilancia:2 | unidad | 198 | 81 | 7 | 4 | 106 | False |
| vigilancia:7 | arista | 4 | 1 | 0 | 1 | 2 | True |
| observacion:12 | arista | 28.062 | 1.021 | 5.030 | 830 | 21.181 | False |

Unidades en `finales.jsonl`: 3.294; la cola, 42; las aceptadas (los tres estados juntos), 3.252. Las partes por corte de E1 que usan el chunk de su unidad: ri_rml::Sbloque14::parte1, ri_rml::Sbloque14::parte2, ri_rml::Sbloque14::parte3, ri_rml::Sbloque14::parte4, ri_rml::Sbloque14::parte5.

#### Tabla T2. Cuántos se sortean por celda, y lo que se declara (`celdas_t4_t3f.asignar`)

| muestra | RI:sin_raiz | RI:resto | NG:sin_raiz | NG:resto | total | notas |
|---|---:|---:|---:|---:|---:|---|
| cola | 6 | 5 | 0 | 19 | 30 | la clase RI tiene 11 de su cuota de 15: entran todos; faltan 4, que salen de la otra clase: 1 a NG:sin_raiz y 3 a NG:resto; la celda NG:sin_raiz tiene 0 de su cuota de 6: entran todos; NG:resto sortea 6 más |
| aceptadas:items | 10 | 5 | 5 | 10 | 30 | — |
| aceptadas:no_items | 10 | 5 | 5 | 10 | 30 | — |
| vigilancia:2 | 10 | 5 | 4 | 11 | 30 | la celda NG:sin_raiz tiene 4 de su cuota de 5: entran todos; NG:resto sortea 1 más |
| vigilancia:7 | 1 | 0 | 1 | 2 | 4 | 4 elementos: se lee entera, sin celdas |
| observacion:12 | 10 | 5 | 5 | 10 | 30 | — |

#### Tabla T3. Los pesos reales por celda (w_c = N_c / N de la población de cada muestra)

| muestra | RI:sin_raiz | RI:resto | NG:sin_raiz | NG:resto |
|---|---:|---:|---:|---:|
| aceptadas:items | 0,1294 | 0,0114 | 0,0220 | 0,8371 |
| aceptadas:no_items | 0,0681 | 0,0676 | 0,0326 | 0,8318 |
| cola | 0,1429 | 0,1190 | 0,0000 | 0,7381 |
| vigilancia:2 | 0,4091 | 0,0354 | 0,0202 | 0,5354 |
| vigilancia:7 | 0,2500 | 0,0000 | 0,2500 | 0,5000 |
| observacion:12 | 0,0364 | 0,1792 | 0,0296 | 0,7548 |
| proyección de la E0 (pre-registro) | 0,0903 | 0,0477 | 0,0286 | 0,8334 |

#### Tabla T4. Los umbrales, con los pesos reales (`muestras/umbrales_t4_reales.json`) y la proyección del pre-registro

| estrato | n efectivo | atención desde (p) | freno por intervalos desde | atención sobre las 60 desde | errores en una sola celda para la atención |
|---|---:|---|---:|---:|---|
| items (reales) | 13,912 | 0,383 (0,0489) | 0,627 | 0,331 | RI:sin_raiz no alcanza sola, RI:resto no alcanza sola, NG:sin_raiz no alcanza sola, NG:resto 5 de 10 |
| items (proyección) | 14,105 | 0,380 (0,0493) | 0,626 | 0,330 | RI:sin_raiz no alcanza sola, RI:resto no alcanza sola, NG:sin_raiz no alcanza sola, NG:resto 5 de 10 |
| no_items (reales) | 14,130 | 0,284 (0,0492) | 0,536 | 0,242 | RI:sin_raiz no alcanza sola, RI:resto no alcanza sola, NG:sin_raiz no alcanza sola, NG:resto 4 de 10 |
| no_items (proyección) | 14,105 | 0,286 (0,0497) | 0,535 | 0,242 | RI:sin_raiz no alcanza sola, RI:resto no alcanza sola, NG:sin_raiz no alcanza sola, NG:resto 4 de 10 |

- **Tasa ponderada total:** n efectivo 25,817 (proyección 27,572); pesos de los estratos ítems 0,3493 y no ítems 0,6507. La tanda 0 con el mismo método: 0,1616, Wilson [0.0888, 0.276].
- **Atención de RI** (447 unidades RI aceptadas): salta desde una tasa ponderada de RI de 0,291 (p 0,0500); bajo H0, 0,1572; n efectivo 23,906; potencia con la tasa de RI duplicada 0,5971. Proyección: 0,278, 0,1616, 29,301 y 0,6940.
- **La cola, regla del 25 %:** n efectivo 28,646; límite superior de Wilson con 0 errores 0,1182; con 1 error en cada celda sola: RI:sin_raiz 0,1570, RI:resto 0,1570, NG:resto 0,1793. Es cifra y vigilancia, no freno.
- **Los controles:** la importación del script de la mesa reproduce su JSON byte a byte: True; las tres cuentas con los pesos proyectados dan sus cifras: True.

#### Tabla T5. Los sorteos (`muestras/sorteos_t4.json`; base `33a3c34b…`; poblaciones `3dce23d7…`)

| muestra | archivo | elementos | sha256 | hora |
|---|---|---:|---|---|
| cola | `muestras/cola.json` | 30 | `89305f3ffa8bc22d60b46fcfecf35c6efe4eb01347277b1f47d5813f1852740b` | 2026-10-18T10:09:26-03:00 |
| aceptadas:items | `muestras/aceptadas_items.json` | 30 | `35622d640abb2d3997f2c39b321537a74025713ad1e5605b75d63eae790189d9` | 2026-10-18T10:09:26-03:00 |
| aceptadas:no_items | `muestras/aceptadas_no_items.json` | 30 | `41d2f3ea8a42c82db07cfa47c0b237014579b965ff994ccd462ad3dcbc36e3e1` | 2026-10-18T10:09:26-03:00 |
| vigilancia:2 | `muestras/vigilancia_2.json` | 30 | `68776dd00d4c49d4fee1a04837cafaf1de4312262f05b358121abd4c6f265d73` | 2026-10-18T10:09:26-03:00 |
| vigilancia:7 | `muestras/vigilancia_7.json` | 4 | `5e30a60b1c8c2fc076ef521217f8ec795921a880aefcf73b62d7681986e2b7d0` | 2026-10-18T10:09:26-03:00 |
| observacion:12 | `muestras/observacion_12.json` | 30 | `84151a2772d0edb87f79cadad91e5d3207d543b6d55eaf0761fb067ae58eb446` | 2026-10-18T10:09:26-03:00 |

La segunda corrida (`muestras/segunda_corrida_de_los_sorteos/`) da las seis muestras byte a byte iguales, y el índice igual salvo las horas (`consola_sorteos_corrida2.txt`). Las vigilancias (1) y (3) no se sortean; las cadenas de la ampliación no se usan.

#### Tabla T6. El material (`muestras/material/material_t4.json`, 2026-10-18T10:12:10-03:00)

| muestra | fichas | fichas (.jsonl) | fichas (.md) | planilla (.csv) |
|---|---:|---|---|---|
| cola | 30 | `5f348167cd038cf1…` | `0fe36f519804fe76…` | `05ca58fcc2a212f7…` |
| aceptadas:items | 30 | `c81f6f8cbc33a6ab…` | `7723ee4bf788d356…` | `15e7f9e21c98dbaa…` |
| aceptadas:no_items | 30 | `30a64bcfa1484b3b…` | `ac880d955f8af72a…` | `188fae5b29d329f4…` |
| vigilancia:2 | 30 | `eab2d878b510f4c7…` | `524f0c3abd1981c3…` | `760b7af10b75c6ed…` |
| vigilancia:7 | 4 | `4957839fd5aa97bc…` | `6975a645e75c5c4e…` | `11cb97845b9978bb…` |
| observacion:12 | 30 | `6075d991a2ce1ae4…` | `a4dd2d2eee6137b0…` | `fd04235baf84a33a…` |

#### Tabla T7. Las unidades a la vista (`muestras/unidades_a_la_vista_T4.json`, 2026-10-18T10:13:10-03:00)

| muestra | fichas | unidades a la vista | por versión | de ellas, solo por un TextoOrdenado o un Sujeto (información) |
|---|---:|---:|---|---:|
| cola | 30 | 30 | {'primera': 30} | 0 |
| aceptadas:items | 30 | 2.189 | {'final': 2189} | 2.155 |
| aceptadas:no_items | 30 | 2.579 | {'final': 2579} | 2.545 |
| vigilancia:2 | 30 | 2.161 | {'final': 2161} | 2.131 |
| vigilancia:7 | 4 | 156 | {'final': 156} | 152 |
| observacion:12 | 30 | 2.144 | {'final': 2144} | 2.110 |
| todas | — | 3.019 | {'primera': 30, 'final': 2989} | — |

#### Tabla T8. Las vigilancias (1) y (3): la población de la definición propuesta (información; no se sortean)

- (1): nodos Condicion del grafo evaluado: 1.401, por celda {'NG:resto': 1163, 'RI:sin_raiz': 94, 'NG:sin_raiz': 42, 'RI:resto': 102}.
- (3): grupos de 2 nodos o más de contenido con la misma unidad de procedencia primaria y el mismo tramo normalizado (espacios y mayúsculas): 181 grupos con 373 nodos, por celda del nodo de id menor {'NG:resto': 133, 'RI:resto': 42, 'RI:sin_raiz': 5, 'NG:sin_raiz': 1}.
