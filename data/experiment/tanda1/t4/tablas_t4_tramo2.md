Salida: `tasas/tasas_t4_tramo2.json` (2026-10-18T17:15:57-03:00, sha256 `ac6e48a238226833053387cdcd7cf70397db18cdacefc22c92ee99557ff826a2`), de `scripts/tasas_t4t2.py`. Rutas relativas a `data/experiment/tanda1/t4/`.

#### Tabla 1. Las cifras para la hoja de la revisión entre tandas (filas que esperan a T4)

| fila | tanda 1 | línea de base | decisión | script y clave de la salida |
|---|---|---|---|---|
| aceptadas, ítems | 9 de 30 (5 con error y 4 dudosas); ponderada 0,2196, Wilson [0,0784; 0,4822] (n ef. 13,912); sin las dudosas, 5 de 26, 0,1209 [0,0285; 0,3916] | 6 de 30, Wilson [0,0951; 0,3731] | atención: no (p 0,3618); freno: no | `scripts/tasas_t4t2.py`, `tasas/tasas_t4_tramo2.json`, `aceptadas.items` |
| aceptadas, no ítems | 3 de 30 (2 con error y 1 dudosa); ponderada 0,0968, Wilson [0,0214; 0,3446] (n ef. 14,130); sin las dudosas, 2 de 29, 0,0907 [0,0192; 0,3374] | 4 de 30, Wilson [0,0531; 0,2968] | atención: no (p 0,6454); freno: no | `scripts/tasas_t4t2.py`, `tasas/tasas_t4_tramo2.json`, `aceptadas.no_items` |
| aceptadas, ponderada total | 0,1397, Wilson [0,0532; 0,3196] (n ef. 25,817); sin las dudosas, 0,1013 [0,0322; 0,2759] | 0,1616, Wilson [0,0888; 0,2760] (mismo método) | sin umbral | `scripts/tasas_t4t2.py`, `tasas/tasas_t4_tramo2.json`, `aceptadas.total` |
| atención de RI | 7 de 30; ponderada de RI 0,1747, Wilson [0,0715; 0,3680] (n ef. 23,906); sin las dudosas, 3 de 26, 0,0842 | bajo H0, 0,1572 (umbral de T3: 0,2913) | atención: no (p 0,3510) | `scripts/tasas_t4t2.py`, `tasas/tasas_t4_tramo2.json`, `atencion_RI` |
| tasa de error de la cola | 14 de 30 (12 con error y 2 dudosas); ponderada 0,4386, Wilson [0,2751; 0,6166] (n ef. 28,646); sin las dudosas, 12 de 28, 0,3984 [0,2376; 0,5847] | 12 de 30, Wilson [0,246; 0,577] (reext_t0/t4/salida/tasas_t4.json) | regla del 25 %: se dispara (cifra y vigilancia, no freno) | `scripts/tasas_t4t2.py`, `tasas/tasas_t4_tramo2.json`, `cola` |
| observación (12) | 27 correctas de 30 (0 no decidibles, en el denominador; 3 incorrectas: E1-prompt 3); Wilson [0,7438; 0,9654]; ponderada por celda 0,8916 [0,6467; 0,9737] | 25 de 30, Wilson [0,664; 0,927], con el perfil anterior (pre-registro, §5.2) | sin umbral | `scripts/tasas_t4t2.py`, `tasas/tasas_t4_tramo2.json`, `observacion:12` |
| vigilancia (1) | 3 sí de 30 (0 no decidibles, fuera de la tasa); cruda 0,1000, Wilson [0,0346; 0,2562]; ponderada por celda 0,1043 [0,0242; 0,3532] | no se midió en la tanda 0 | sin umbral | `scripts/tasas_t4t2.py`, `tasas/tasas_t4_tramo2.json`, `vigilancias.vigilancia:1` |
| vigilancia (2) | 15 vaciamientos de 30; cruda 0,5000, Wilson [0,3315; 0,6685]; ponderada por celda 0,5276 [0,3354; 0,7120] | en la tanda 0 se midió la población, sin leer la muestra | sin umbral | `scripts/tasas_t4t2.py`, `tasas/tasas_t4_tramo2.json`, `vigilancias.vigilancia:2` |
| vigilancia (3) | 9 duplicaciones de 30; cruda 0,3000, Wilson [0,1666; 0,4788]; ponderada por celda 0,3199 [0,1665; 0,5255] | no se midió en la tanda 0 | sin umbral | `scripts/tasas_t4t2.py`, `tasas/tasas_t4_tramo2.json`, `vigilancias.vigilancia:3` |
| vigilancia (7) | 2 sin apoyo de 4; cruda 0,5000, Wilson [0,1500; 0,8500]; leída entera, sin celdas | en la tanda 0 se midió la población, sin leer la muestra | sin umbral | `scripts/tasas_t4t2.py`, `tasas/tasas_t4_tramo2.json`, `vigilancias.vigilancia:7` |

- **La ampliación:** salta la atención de ítems, no; la de no ítems, no; la de RI, no. Hay ampliación: no. Con las dudosas fuera: aceptadas:items no, aceptadas:no_items no, RI no.
- **Los controles de la entrada** (`scripts/tasas_t4t2.py`): 37 de 37 pasan.

#### Tabla 2. Las aceptadas por celda (`aceptadas.<estrato>.por_celda`; pesos de `t3/muestras/umbrales_t4_reales.json`)

| estrato | celda | N | peso | leídas | con error | sin error | dudosa |
|---|---|---:|---:|---:|---:|---:|---:|
| items | RI:sin_raiz | 147 | 0,1294 | 10 | 1 | 7 | 2 |
| items | RI:resto | 13 | 0,0114 | 5 | 1 | 3 | 1 |
| items | NG:sin_raiz | 25 | 0,0220 | 5 | 2 | 3 | 0 |
| items | NG:resto | 951 | 0,8371 | 10 | 1 | 8 | 1 |
| no_items | RI:sin_raiz | 144 | 0,0681 | 10 | 1 | 8 | 1 |
| no_items | RI:resto | 143 | 0,0676 | 5 | 0 | 5 | 0 |
| no_items | NG:sin_raiz | 69 | 0,0326 | 5 | 0 | 5 | 0 |
| no_items | NG:resto | 1.760 | 0,8318 | 10 | 1 | 9 | 0 |

#### Tabla 3. Las tasas de las aceptadas, la regla y la sensibilidad (`aceptadas.<estrato>.regla` y `.sensibilidad_sin_dudosas`)

| estrato | cuenta | errores | leídas | tasa ponderada | n ef. | Wilson | p de la atención | atención | freno por intervalos | atención de T3 desde | freno de T3 desde |
|---|---|---:|---:|---:|---:|---|---:|---|---|---:|---:|
| items | regla (dudosa = error) | 9 | 30 | 0,2196 | 13,912 | [0,0784; 0,4822] | 0,3618 | no | no | 0,3827 | 0,6274 |
| items | sensibilidad (dudosas fuera) | 5 | 26 | 0,1209 | 12,486 | [0,0285; 0,3916] | 0,7330 | no | no | 0,3827 | 0,6274 |
| no_items | regla (dudosa = error) | 3 | 30 | 0,0968 | 14,130 | [0,0214; 0,3446] | 0,6454 | no | no | 0,2836 | 0,5365 |
| no_items | sensibilidad (dudosas fuera) | 2 | 29 | 0,0907 | 14,120 | [0,0192; 0,3374] | 0,7180 | no | no | 0,2836 | 0,5365 |

items: la sensibilidad da otra decisión de atención, no; de freno, no. La distribución bajo H0: 3.636 valores, suma 1,000000 (`tasas/distribuciones_bajo_H0_t4_tramo2.json`, `aceptadas:items:regla`).

no_items: la sensibilidad da otra decisión de atención, no; de freno, no. La distribución bajo H0: 3.366 valores, suma 1,000000 (`tasas/distribuciones_bajo_H0_t4_tramo2.json`, `aceptadas:no_items:regla`).

#### Tabla 4. La ponderada total y la atención de RI (`aceptadas.total` y `atencion_RI`)

| cifra | cuenta | errores de leídas | tasa | n ef. | Wilson | p de la atención | atención |
|---|---|---|---:|---:|---|---:|---|
| ponderada total | regla | — | 0,1397 | 25,817 | [0,0532; 0,3196] | — | sin umbral |
| ponderada total | sensibilidad | — | 0,1013 | 25,152 | [0,0322; 0,2759] | — | sin umbral |
| atención de RI | regla | 7 de 30 | 0,1747 | 23,906 | [0,0715; 0,3680] | 0,3510 | no |
| atención de RI | sensibilidad | 3 de 26 | 0,0842 | 21,868 | [0,0223; 0,2703] | 0,8262 | no |

Atención de RI: 447 unidades RI aceptadas; pesos items:RI:sin_raiz 0,3289, items:RI:resto 0,0291, no_items:RI:sin_raiz 0,3221, no_items:RI:resto 0,3199; por celda, con la regla, items:RI:sin_raiz 3 de 10, items:RI:resto 2 de 5, no_items:RI:sin_raiz 2 de 10, no_items:RI:resto 0 de 5.

#### Tabla 5. NG `sin_raiz`, por celda y sin umbral (`NG_sin_raiz`)

| estrato | N | leídas | con error | sin error | dudosa | tasa con la regla | tasa sin las dudosas |
|---|---:|---:|---:|---:|---:|---:|---:|
| items | 25 | 5 | 2 | 3 | 0 | 0,4000 | 0,4000 |
| no_items | 69 | 5 | 0 | 5 | 0 | 0,0000 | 0,0000 |

#### Tabla 6. La cola por celda y su tasa (`cola`)

| celda | N | peso | leídas | con error | sin error | dudosa |
|---|---:|---:|---:|---:|---:|---:|
| RI:sin_raiz | 6 | 0,1429 | 6 | 2 | 3 | 1 |
| RI:resto | 5 | 0,1190 | 5 | 4 | 1 | 0 |
| NG:sin_raiz | 0 | 0,0000 | 0 | 0 | 0 | 0 |
| NG:resto | 31 | 0,7381 | 19 | 6 | 12 | 1 |

| cuenta | errores | leídas | tasa ponderada | n ef. | Wilson | la regla del 25 % se dispara |
|---|---:|---:|---:|---:|---|---|
| regla (dudosa = error) | 14 | 30 | 0,4386 | 28,646 | [0,2751; 0,6166] | sí |
| sensibilidad (dudosas fuera) | 12 | 28 | 0,3984 | 26,895 | [0,2376; 0,5847] | sí |

La sensibilidad da otra decisión de la regla del 25 %: no.

#### Tabla 7. Las vigilancias (1), (2), (3) y (7), por celda (`vigilancias.<muestra>.por_celda`)

| muestra | celda | N | leídas | respuestas |
|---|---|---:|---:|---|
| vigilancia:1 | RI:sin_raiz | 94 | 10 | sí 1, no 9, no decidible 0 |
| vigilancia:1 | RI:resto | 102 | 5 | sí 1, no 4, no decidible 0 |
| vigilancia:1 | NG:sin_raiz | 42 | 5 | sí 0, no 5, no decidible 0 |
| vigilancia:1 | NG:resto | 1.163 | 10 | sí 1, no 9, no decidible 0 |
| vigilancia:2 | RI:sin_raiz | 81 | 10 | vaciamiento 10, no vaciamiento 0, no decidible 0 |
| vigilancia:2 | RI:resto | 7 | 5 | vaciamiento 3, no vaciamiento 2, no decidible 0 |
| vigilancia:2 | NG:sin_raiz | 4 | 4 | vaciamiento 0, no vaciamiento 4, no decidible 0 |
| vigilancia:2 | NG:resto | 106 | 11 | vaciamiento 2, no vaciamiento 9, no decidible 0 |
| vigilancia:3 | RI:sin_raiz | 5 | 5 | duplicación 1, distintos 4 |
| vigilancia:3 | RI:resto | 42 | 10 | duplicación 2, distintos 8 |
| vigilancia:3 | NG:sin_raiz | 1 | 1 | duplicación 1, distintos 0 |
| vigilancia:3 | NG:resto | 133 | 14 | duplicación 5, distintos 9 |
| vigilancia:7 | RI:sin_raiz | 1 | 1 | con apoyo 0, sin apoyo 1, no decidible 0 |
| vigilancia:7 | RI:resto | 0 | 0 | con apoyo 0, sin apoyo 0, no decidible 0 |
| vigilancia:7 | NG:sin_raiz | 1 | 1 | con apoyo 0, sin apoyo 1, no decidible 0 |
| vigilancia:7 | NG:resto | 2 | 2 | con apoyo 2, sin apoyo 0, no decidible 0 |

#### Tabla 8. Las tasas de las vigilancias, la cruda y la ponderada por celda (`vigilancias.<muestra>`)

| muestra | se vigila | por respuesta | fuera de la tasa | cruda | Wilson (cruda) | ponderada por celda | n ef. | Wilson (ponderada) |
|---|---|---|---|---|---|---:|---:|---|
| vigilancia:1 | sí | sí 3, no 27, no decidible 0 | no decidible 0 | 3 de 30, 0,1000 | [0,0346; 0,2562] | 0,1043 | 14,164 | [0,0242; 0,3532] |
| vigilancia:2 | vaciamiento | vaciamiento 15, no vaciamiento 15, no decidible 0 | — | 15 de 30, 0,5000 | [0,3315; 0,6685] | 0,5276 | 23,179 | [0,3354; 0,7120] |
| vigilancia:3 | duplicación | duplicación 9, distintos 21 | — | 9 de 30, 0,3000 | [0,1666; 0,4788] | 0,3199 | 22,658 | [0,1665; 0,5255] |
| vigilancia:7 | sin apoyo | con apoyo 2, sin apoyo 2, no decidible 0 | — | 2 de 4, 0,5000 | [0,1500; 0,8500] | — | — | leída entera, sin celdas |

Vigilancia (3): el grupo es de nodos con la misma unidad y el mismo tramo, así que no ve las duplicaciones con tramos distintos (decisión de la autora del 18/10/2026, punto 1.4; registro de decisiones, §29).

#### Tabla 9. La observación (12), por celda (`observacion:12`; pesos de `muestras/poblaciones_t4_tramo1.json`)

| celda | N | peso | leídas | correcta | no decidible | incorrecta |
|---|---:|---:|---:|---:|---:|---:|
| RI:sin_raiz | 960 | 0,0519 | 10 | 10 | 0 | 0 |
| RI:resto | 1.743 | 0,0943 | 5 | 4 | 0 | 1 |
| NG:sin_raiz | 770 | 0,0417 | 5 | 4 | 0 | 1 |
| NG:resto | 15.010 | 0,8121 | 10 | 9 | 0 | 1 |

Cruda: 27 correctas de 30, 0,9000, Wilson [0,7438; 0,9654]. Ponderada por celda: 0,8916, n ef. 14,631, Wilson [0,6467; 0,9737]. Las incorrectas, por `capa_pipeline`: E1-prompt, 3 (fichas `fichas_observacion_12.md#13`, `fichas_observacion_12.md#20`, `fichas_observacion_12.md#30`).
