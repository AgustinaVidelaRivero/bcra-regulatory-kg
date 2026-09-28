# U-ESTUDIO-MATRIZ — efecto y muestra de las relaciones rechazadas por la matriz congelada

Solo lectura, USD 0, sin Neo4j. Salidas en `/tmp/u_estudio_matriz/` (sha256 en `manifest.txt`). Reproducción: `cd /tmp/u_estudio_matriz && PYTHONDONTWRITEBYTECODE=1 python3 uestmat_paso{1_control,2_variantes,3_muestra,4_reporte}.py` en ese orden.

## Controles

- E1 primera pasada re-validada desde el crudo con la matriz congelada SIN ampliar (`uestmat_paso1_control.json`): 2.434 de 2.434 registros con crudo reproducen la validación persistida (3 registros sin crudo, todos con error de API). Rechazos firma_invalida recomputados: 982; iguales a p4_filas (clave to/chunk_id/idx/par/línea): sí. Con la matriz sin ampliar, los 982 siguen inválidos.
- Población final (lo que ensambla r1), 10 TOs: 2.143 unidades con crudo de E1, 220 con crudo del reintento (`e1_reintentos.db`, immutable=1, un solo candidato por unidad) y 71 de cola (validación E1 del compact); reproducen su validación 2.143/220/71.
- Re-ensamblado en memoria de KG-Tanda0-Desarrollo-r1 (réplica de `ensamblar_tanda0.py`, sin escribir intermedios), sin envoltorio y con envoltorio sobre la matriz sin ampliar (1.763 unidades re-validadas): `eab2fdd01dec…` y `eab2fdd01dec…` = sha sellado `eab2fdd01dec…`.
- Grafo: 6.378 nodos / 15.007 aristas; aislados hoy 94 (Condicion 35, Operacion 30, Definicion 13, Sujeto 12, Comunicacion 3, Obligacion 1).
- Tarifa de E3 de la tanda 0: USD 0,009179 por unidad = 22,277978 / 2.427 (fase E3 completa de los 10 TOs, incluye reintentos E1; `salida_dirigida/estado_corpus.json`). Alternativa solo verificación: USD 0,007442 por llamada = 19,9529 / 2.681 (`<to>/resumen_e3.json`); con ella cada costo de la tabla se multiplica por 0,811. No incluye la re-extracción dirigida de tres unidades (presupuesto aparte).

## Tabla del punto 1

A = E1 primera pasada (población de los 982); B = población final (entrada de r1); aristas y aislados = KG-Tanda0-Desarrollo-r1 re-ensamblado con la ampliación; fragmentos = unidades de A ∪ B (las que cambian su entrada a E3). Pares de números: 10 TOs / 5 de desarrollo.

| id | ampliación en memoria | A rel. nuevas | B rel. nuevas | aristas nuevas en r1 | aislados que dejan de estarlo | fragmentos a re-verificar | costo USD (tarifa fase) |
|---|---|---|---|---|---|---|---|
| P01 | condicion_de: rango+Operacion | 424 / 383 | 434 / 388 | 388 | 21 (Condicion 20, Operacion 1) | 296 / 264 | 2,72 / 2,42 |
| P02 | condicion_de: rango+Potestad | 231 / 208 | 263 / 239 | 239 | 3 (Condicion 3) | 188 / 168 | 1,73 / 1,54 |
| P03 | aplica_a: dom+Condicion | 45 / 39 | 48 / 41 | 41 | 0 | 36 / 29 | 0,33 / 0,27 |
| P04 | exceptua: rango+Operacion | 27 / 26 | 25 / 18 | 18 | 5 (Operacion 5) | 16 / 13 | 0,15 / 0,12 |
| P05 | aplica_a: dom+Definicion | 23 / 20 | 23 / 20 | 20 | 0 | 23 / 20 | 0,21 / 0,18 |
| P06 | exceptua_obligacion: rango+Restriccion | 19 / 15 | 22 / 18 | 18 | 0 | 21 / 17 | 0,19 / 0,16 |
| P07 | condicion_de: rango+Definicion | 17 / 17 | 17 / 16 | 16 | 9 (Condicion 9) | 12 / 11 | 0,11 / 0,10 |
| P08 | condiciona: dom+Condicion | 15 / 8 | 14 / 7 | 7 | 1 (Condicion 1) | 15 / 8 | 0,14 / 0,07 |
| P09 | exceptua_obligacion: rango+Operacion | 12 / 10 | 14 / 12 | 12 | 1 (Operacion 1) | 14 / 12 | 0,13 / 0,11 |
| P10 | exceptua: rango+Condicion | 11 / 11 | 9 / 9 | 9 | 0 | 4 / 4 | 0,04 / 0,04 |
| P11 | condicion_de: rango+Condicion | 10 / 9 | 11 / 10 | 10 | 0 | 10 / 9 | 0,09 / 0,08 |
| G-condicion_de | condicion_de: rango+Condicion, rango+Definicion, rango+Operacion, rango+Potestad | 682 / 617 | 725 / 653 | 653 | 33 (Condicion 32, Operacion 1) | 482 / 430 | 4,42 / 3,95 |
| G-aplica_a | aplica_a: dom+Condicion, dom+Definicion | 68 / 59 | 71 / 61 | 61 | 0 | 58 / 48 | 0,53 / 0,44 |
| G-exceptua | exceptua: rango+Condicion, rango+Operacion | 38 / 37 | 34 / 27 | 27 | 5 (Operacion 5) | 20 / 17 | 0,18 / 0,16 |
| G-exceptua_obligacion | exceptua_obligacion: rango+Operacion, rango+Restriccion | 31 / 25 | 36 / 30 | 30 | 1 (Operacion 1) | 35 / 29 | 0,32 / 0,27 |
| G-condiciona | condiciona: dom+Condicion | 15 / 8 | 14 / 7 | 7 | 1 (Condicion 1) | 15 / 8 | 0,14 / 0,07 |
| G-condicion_de-ejemplo | condicion_de: rango+Operacion, rango+Potestad | 655 / 591 | 697 / 627 | 627 | 24 (Condicion 23, Operacion 1) | 462 / 412 | 4,24 / 3,78 |

- En todas las variantes: aristas perdidas 0, nodos nuevos 0, nodos perdidos 0; aristas nuevas = relaciones nuevas de B en desarrollo (ninguna colapsa con otra). Cada ampliación valida exactamente los pares buscados (asserto sobre 10 tipos × 13 predicados × 10 tipos): en los 11 candidatos ampliar dominio o rango equivale a agregar solo el par.
- Agrupadas con un solo par candidato (idénticas a su fila P): G-condiciona.
- A coincide con los conteos de p4 por par (asserto). B difiere de A porque en las unidades aceptadas tras reintento el grafo se construyó con la salida del reintento.
- Contraste externo: P01, P02, P07 y P08 desaíslan 20, 3, 9 y 1 Condiciones, los mismos conteos por par del punto 3 de U-AUDIT-TIPOS-V3.
- Supuesto: lo que pasa a válido entra al grafo sin nueva verificación E3 (cota superior). Efecto DESPUÉS de re-verificar: NO ENCONTRADO — requiere llamar a E3 (y eventualmente a reintentos), fuera del alcance USD 0.

## Muestra del punto 2

- Población: reports/u_audit_tipos_v3/p4_filas.json (982 rechazos firma_invalida de E1, 10 TOs); en los estratos candidatos: 834.
- Asignación: proporcional con mínimo 5, iterativa, restos mayores. Primera vuelta: nueve estratos con cuota < 5 quedan en 5; segunda vuelta reparte 15 entre los dos mayores (cuotas 9,71, 5,29).
- Sorteo: semilla 20260928; por estrato: lista ordenada por (to, chunk_id, idx); random.Random(20260928).sample(lista, k), instancia nueva por estrato. Filas M01..M60 por estrato (n descendente) y, dentro, por (to, chunk_id, idx).

| par | n población | n muestra |
|---|---|---|
| Condicion --condicion_de--> Operacion | 424 | 10 |
| Condicion --condicion_de--> Potestad | 231 | 5 |
| Condicion --aplica_a--> Sujeto | 45 | 5 |
| Excepcion --exceptua--> Operacion | 27 | 5 |
| Definicion --aplica_a--> Sujeto | 23 | 5 |
| Excepcion --exceptua_obligacion--> Restriccion | 19 | 5 |
| Condicion --condicion_de--> Definicion | 17 | 5 |
| Condicion --condiciona--> Operacion | 15 | 5 |
| Excepcion --exceptua_obligacion--> Operacion | 12 | 5 |
| Excepcion --exceptua--> Condicion | 11 | 5 |
| Condicion --condicion_de--> Condicion | 10 | 5 |
| total | 834 | 60 |

- Composición: 49 filas de los TOs de desarrollo y 11 de los cinco nuevos de la tanda 0 (`uestmat_paso3_muestra.json`, campo filas).
- 8 de las 60 filas son de unidades aceptadas tras reintento: la relación sorteada es de la primera pasada y puede no estar en la salida que entró al grafo (no cambia su verdad).
- CSV `uestmat_muestra_60.csv` (UTF-8 con BOM): columnas id_muestra, par, chunk_id, texto_fragmento_e0, origen_tipo, origen_etiqueta, origen_descripcion, predicado, destino_tipo, destino_etiqueta, destino_descripcion, veredicto, nota. Veredicto y nota vacíos. Texto del fragmento = herencia + texto propio de E0, verificado contra sha256_completo. Para el extremo Sujeto de aplica_a se transcribe el id emitido; la descripción queda vacía porque el extractor no la emite.

## Observaciones y desvíos

1. Desvío propio: la línea de base de `git status` y de `.pyc` se escribió primero en el scratchpad de la sesión (fuera de `/tmp/u_estudio_matriz/`), por el hábito de usarlo para temporales. Se movió acá (`uestmat_git_status_inicio*.txt`, `uestmat_pyc_inicio.txt`) antes de cualquier otra escritura; el scratchpad quedó vacío.
2. Contradicción CLAUDE.md §4.g (paquete de revisión en el scratchpad) vs mandato (escribir solo en `/tmp/u_estudio_matriz/`): el directorio del mandato ES el paquete (prefijo `uestmat_`, `manifest.txt` con sha256). No se armó paquete aparte.
3. «Variante agrupada por predicado»: se calcularon las dos lecturas — todos los pares candidatos del predicado (G-<predicado>) y el ejemplo literal del mandato (G-condicion_de-ejemplo: + Operacion y Potestad).
4. La regla «proporcional con mínimo 5» deja al segundo estrato (231) en el mínimo, igual que los estratos de 10 a 45: con 60 filas y 11 estratos la cuota proporcional solo supera 5 en los dos mayores. Otra regla requiere decisión de la autora; no se aplicó ninguna.
5. Trazabilidad de U-AUDIT-TIPOS-V3: su inventario declara la lectura de `e1_reintentos.db` con immutable=1, pero ningún script de `reports/u_audit_tipos_v3/` abre esa db (grep de `e1_reintentos|immutable` sobre sus .py: vacío). El paso 1 rehace esa ubicación con script conservado acá.
6. Criterio «git status igual al inicio»: NO se cumple literalmente. `git status --porcelain` de cierre tiene 10 líneas nuevas y 0 desaparecidas respecto del inicio, todas en `docs/tesis/figuras/`; además HEAD avanzó de `8cf8c23` a `791166d` (commit de reports de U-INV-CANDIDATOS, 16:56:52) y crecen los no rastreados de `data/experiment/ev2_tanda0/` (corrida en curso). Nada de eso es de esta unidad: sus únicas escrituras están en este directorio (`uestmat_cierre_controles.txt`: `.pyc` iguales, scratchpad vacío; fuera de esas rutas, lo único más nuevo que la línea de base es el log de Neo4j y la entrada de directorio `reports/`, con mtime 16:56:44, ocho segundos antes del commit ajeno, y sin archivos nuevos adentro), ningún módulo importado referencia `docs/tesis`, y git se usó solo con status, log y show.

