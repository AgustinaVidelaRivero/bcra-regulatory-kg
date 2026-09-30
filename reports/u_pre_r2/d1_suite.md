# U-PRE-R2-DIAG — D1: los seis ítems de la suite

Mandato `docs/mandatos/UPRE_R2_diagnostico.md`. Solo lectura, USD 0, sin API ni Neo4j. Comando: `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_pre_r2/upre_d1_suite.py --out-dir reports/u_pre_r2`. Todo número de este archivo sale de `d1_suite.json` (misma corrida).

## 1. Reglas declaradas antes de aplicarse

- **R-T5**: fila x presente por contenido si existe una arista referencia con evidencia tal que: (1) su fuente ancla en x.source_ancla (todas las provenances); (2) su destino ancla en x.target_ancla y properties.destino == x.destino; (3) tipo del destino == x.target_type; (4) los números de punto de su evidencia y de x.evidencia_verbatim se intersecan. R-T5 sin tipo = (1), (2), (4).
- **R-E4a8**: la regla de t_e4_a8 leída sobre la tabla e4_propuestos.json del ensamblado del grafo bajo prueba
- **R-T4**: esqueleto de un catálogo = aristas de RELACIONES_ESQUELETO que build_skeleton construye sobre ese catálogo (ensamblar_corpus.inyectar_esqueleto_v3 sobre un grafo vacío, por import)
- **R-CAT**: catálogo JSON v3 más los ids del bloque v3 del perfil que no están en el JSON, en memoria; contrafáctico, no resultado de r2
- **SIM-H1**: resolvedor de remisiones re-corrido en memoria con TIPOS_ORIGEN + Condicion, Potestad y Definicion y las redirecciones del manifiesto de desarrollo; control con los tipos originales; no es resultado de r2
- **clase_T5_por_fila**: verbatim presente → sin clase; R-T5 → b; R-T5 sin tipo → b; ausente con la mención solo en nodos fuera de TIPOS_ORIGEN → a (H1); ausente sin mención en el texto que lee el resolvedor → a; otro caso → d

Clases de la decisión 3: (a) regresión real; (b) efecto de direccionamiento; (c) efecto de diseño del perfil v3; (d) no decidible con el material.

## 2. Entradas y controles

| clave | ruta | sha256 |
|---|---|---|
| kg_r1 | `data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json` | `0226e9477baee02d…` |
| kg_desarrollo | `data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo/r1/kg.json` | `eab2fdd01dec4dad…` |
| kg_refinado_esqueleto_referencia | `data/experiment/grafo_v2/reensamblado_v3/kg.json` | `26fac8b49f6c08c1…` |
| fixture | `scripts/regression_kg_esperado.json` | `696f3f941e0d64c3…` |
| suite | `scripts/regression_kg.py` | `87a57b6d80d443a3…` |
| catalogo_v2 | `data/experiment/grafo_v2/esquema_v2_clases.json` | `2672af5216e095be…` |
| catalogo_v3 | `data/experiment/esq_v3_miembros/esquema_v3_clases.json` | `dad88cc92afc53e9…` |
| muestra30_T5 | `data/experiment/reextraccion_v2/corpus_v2/salida_r1/referencias_muestra30_inspeccionada_A2.json` | `4dbc2d306df867de…` |
| e4_propuestos_r1 | `data/experiment/reextraccion_v2/corpus_v2/salida_r1/e4_propuestos.json` | `ad8e2ef78fb2db73…` |
| e4_propuestos_desarrollo | `data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo/r1/e4_propuestos.json` | `1c664faef4bb1f50…` |
| linea_base_E6_desarrollo | `reports/tanda0/regression_ens_desarrollo.json` | `0745a9dc2ec80bfa…` |
| e1_finales_ext_desarrollo | `data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/ext/extracciones_finales_ext.jsonl` | `d92c36b2ea8fe344…` |
| manifiesto_ens_desarrollo | `data/experiment/reextraccion_v2/manifiestos/tanda0_ens_desarrollo.json` | `bfe7c7b0912c9909…` |
| sim_h1_u_audit | `reports/u_audit_tipos_v3/p2_referencias_sim.json` | `0e044879764afb58…` |
| (registrado) | `data/experiment/reextraccion_v2/corpus_v2/salida/ext/extracciones_finales_ext.jsonl` | `c477948f6eabbb16…` |
| (registrado) | `data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo/r1/reporte_ensamblado_r1.json` | `6b76f5d38ef04e04…` |
| (registrado) | `data/experiment/reextraccion_v2/corpus_v2/r1_referencias.py` | `3cc00b2306411d1d…` |
| (registrado) | `data/experiment/reextraccion_v2/corpus_v2/r1_tests.py` | `fe1c747652820ac9…` |
| (registrado) | `data/experiment/reextraccion_v2/corpus_v2/r1_e4.py` | `179db09c2e87dd73…` |
| (registrado) | `data/experiment/reextraccion_v2/corpus_v2/ensamblar_corpus.py` | `7e5d190eae7bfa79…` |
| (registrado) | `data/experiment/reextraccion_v2/e1_extractor/perfil_e1.py` | `3f734038fe2af201…` |
| (registrado) | `data/experiment/reextraccion_v2/e2_reduce/e2_lib.py` | `75aba6e4248f7a6d…` |
| (registrado) | `data/experiment/grafo_v2/code/assemble.py` | `29fd8f427a7c7287…` |

- r1 (`data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json`, catálogo v2, flaggeada): {'no_aplicable': 9, 'persiste': 10, 'resuelto': 27}; contra su entrada de la fixture: 0 diferencias, 46 coinciden.
- desarrollo (`data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo/r1/kg.json`, catálogo v3, flaggeada): {'no_aplicable': 8, 'persiste': 16, 'resuelto': 22}; contra la línea de base de E6: estado igual 46/46, detalle igual 46/46.
- E0 de los cinco TOs de desarrollo idéntico entre `salida_tanda0` y `salida_enm01` (byte a byte): {'pro': True, 'cla': True, 'ric': True, 'cap': True, 'ext': True}.
- Transiciones r1 (fixture) → desarrollo: {'no_aplicable → no_aplicable': 7, 'no_aplicable → persiste': 2, 'persiste → no_aplicable': 1, 'persiste → persiste': 8, 'persiste → resuelto': 1, 'resuelto → persiste': 6, 'resuelto → resuelto': 21}.

## 3. Tabla de los seis ítems

| ítem | verifica | r1 (fixture / medido) | desarrollo | clases por parte | propuesta recomendada |
|---|---|---|---|---|---|
| T2 | `scripts/regression_kg.py:961-968` | resuelto / resuelto | persiste | P1=a, P2=— | A: esperado r2 = persiste, como regresión conocida con causa documentada (fusión por descripción idéntica en E2). r2 no toca el prefijo de E1 ni entity_slug_v3: la… |
| T4 | `scripts/regression_kg.py:982-1001` | resuelto / resuelto | persiste | P1=—, P2=—, P3=c | A: re-direccionar T4 en una unidad de la suite: comparar el esqueleto del grafo con el que build_skeleton construye desde el catálogo pasado por --catalogo (R-T4);… |
| T5 | `scripts/regression_kg.py:1024-1043` | resuelto / resuelto | persiste | P1…P30=por fila | A: re-direccionar T5 en una unidad de la suite por contenido (R-T5) sobre la misma muestra sellada; esperado r2 = persiste: en desarrollo faltan 9 de 30 (6 por H1 … |
| T7 | `scripts/regression_kg.py:1057-1083` | resuelto / resuelto | persiste | P1=—, P2=—, P3=—, P4=—, P5=c | A: si entra a r2 el ítem de la §1.6 que completa esquema_v3_clases.json con los ids del bloque v3: esperado r2 = resuelto (verificado en memoria con R-CAT sobre de… |
| E4-a7 | `scripts/regression_kg.py:1199-1212` | resuelto / resuelto | persiste | P1=—, P2=—, P3=c | A: igual que T7: resuelto si se completa el catálogo JSON (verificado con R-CAT); P3 de E4-a7 es la P5 de T7.… |
| E4-a8 | `scripts/regression_kg.py:1215-1236` | resuelto / resuelto | persiste | P1=b, P2=— | A: re-direccionar E4-a8 en una unidad de la suite para que lea la tabla e4_propuestos.json del ensamblado bajo prueba (R-E4a8); esperado r2 = resuelto si la tabla … |

## 4. Ítem por ítem

### T2

Verifica: `scripts/regression_kg.py:961-968`; `data/experiment/reextraccion_v2/corpus_v2/ensamblar_corpus.py:251-265 (origen)`.
Estado: r1 en la fixture **resuelto**, r1 medido **resuelto**, desarrollo **persiste**.

| parte | r1 | desarrollo | clase | motivo |
|---|---|---|---|---|
| P1 al menos 5 nodos de ext con «125 %» | 6 | 4 | a | dos puntos (ext::7.5.3 y ext::7.8.5.1) quedan en un solo nodo: la estructura separada que el test protege falta en desarrollo |
| P2 al menos 4 puntos distintos | 5 | 5 | — | cumple en las dos generaciones (sin clase) |

Evidencia (`d1_suite.json`, `analisis.T2`): nodos con «125 %» por punto — r1 {'3.11.3.2': 1, '7.11.5': 1, '7.5.3': 2, '7.8.5.1': 1, '7.9.5': 1}, desarrollo {'3.11.3.2': 1, '7.11.5': 1, '7.5.3': 1, '7.8.5.1': 1, '7.9.5': 1}; ocurrencias de «125%» en el texto propio de E0 por punto {'3.11.3.2': 1, '7.11.5': 1, '7.5.3': 1, '7.8.5.1': 1, '7.9.5': 1}.
- Nodo fundido `Restriccion_esta_opcion_estara_disponible_hasta_alcanzar_el_…` en ['7.5.3', '7.8.5.1']: 2 entidades de E1 con «125», 1 descripción distinta y 1 slug de `entity_slug_v3` (`e2_lib.py`: Restriccion/Obligacion/Excepcion se deduplican por descripción); el id del nodo termina en ese slug: True.
- En la salida de E1 que ensambló r1, las mismas unidades tienen 3 entidades con «125» y 3 slugs distintos: no se funden.
- Clasificación asistida (lectura de texto de esta instancia, para revisión de la autora): en r1, los dos nodos con «125 %» de `ext::7.5.3` parafrasean la única ocurrencia de E0 en ese punto; sin la fusión, desarrollo tendría 5 nodos en 5 puntos y P1 cumpliría.

**PROPUESTA — la entrada de r2 la sella la autora (laudo §3.1, punto 2).** Recomendada: A.
- (A) esperado r2 = persiste, como regresión conocida con causa documentada (fusión por descripción idéntica en E2). r2 no toca el prefijo de E1 ni entity_slug_v3: las dos unidades salen de la caché con la misma descripción y se funden igual.
- (B) esperado r2 = resuelto solo si la autora decide, fuera de los candidatos del §1, que la clave de fusión de Restriccion/Obligacion/Excepcion no una descripciones idénticas de puntos distintos (se relaciona con la decisión abierta de H2 del §4); cambia ids y exige actualizar la fixture.

### T4

Verifica: `scripts/regression_kg.py:982-1001`; `scripts/regression_kg.py:1004-1015`; `data/experiment/reextraccion_v2/corpus_v2/r1_tests.py:30-42 (origen)`.
Estado: r1 en la fixture **resuelto**, r1 medido **resuelto**, desarrollo **persiste**.

| parte | r1 | desarrollo | clase | motivo |
|---|---|---|---|---|
| P1 los nodos de esqueleto de la referencia están | sí | sí | — | cumple en las dos generaciones (sin clase) |
| P2 las triplas de esqueleto de la referencia están | sí | sí | — | cumple en las dos generaciones (sin clase) |
| P3 cantidad de aristas de esqueleto igual a la de la referencia | 82 = 82 | 117 ≠ 82 | c | el esqueleto de desarrollo es exactamente el que build_skeleton construye desde el catálogo v3 (R-T4); las aristas de más tienen algún extremo fuera del catálogo v2 |

Evidencia (`analisis.T4`, R-T4): aristas {'referencia_kg_refinado': 82, 'r1': 82, 'desarrollo': 117, 'build_skeleton_catalogo_v2': 82, 'build_skeleton_catalogo_v3': 117}; r1 = build_skeleton(v2): sí; desarrollo = build_skeleton(v3): sí; referencia contenida en desarrollo: sí. Las 35 de más: {'miembro_de': 34, 'subclase_de': 1}, con algún extremo fuera del catálogo v2 35, con ambos extremos en el catálogo v3 35.

**PROPUESTA — la entrada de r2 la sella la autora (laudo §3.1, punto 2).** Recomendada: A.
- (A) re-direccionar T4 en una unidad de la suite: comparar el esqueleto del grafo con el que build_skeleton construye desde el catálogo pasado por --catalogo (R-T4); con eso desarrollo da 117 = 117 y r1 82 = 82; esperado r2 = resuelto. Absorbe además el cambio de esqueleto si entra el ítem de la §1.6 que completa el catálogo JSON.
- (B) sin cambio de la suite: declarar T4 no comparable entre generaciones (el 82 es el esqueleto del catálogo v2) y sellar esperado r2 = persiste, con el detalle faltan 0 / 0 como condición de lectura.
- (C) sin cambio de código: sellar en la entrada de r2 un --esqueleto-referencia de generación 3 construido con el catálogo que use r2; exige re-sellar esa referencia si el catálogo JSON cambia (§1.6).

### T5

Verifica: `scripts/regression_kg.py:1024-1043`; `data/experiment/reextraccion_v2/corpus_v2/r1_tests.py:44-54 (origen)`.
Estado: r1 en la fixture **resuelto**, r1 medido **resuelto**, desarrollo **persiste**.

| parte | r1 | desarrollo | clase | motivo |
|---|---|---|---|---|
| P1…P30 una parte por fila de la muestra sellada | verbatim 30/30 | verbatim 5/30 | por fila | por_clase {"a": 9, "b": 16, "verbatim": 5}; ausentes_por_causa {"H1": 6, "mencion_fuera_del_texto_del_resolvedor": 3} |

Control de SIM-H1 (`analisis.T5.control_sim_h1`): {'tipos_origen_original': ['Obligacion', 'Restriccion', 'Excepcion', 'Operacion'], 'aristas_existentes': 4242, 're_detectadas_con_tipos_originales': 4242, 'identicas': True, 'adicionales_con_tres_tipos_nuevos': 3687, 'perdidas_con_tres_tipos_nuevos': 0, 'adicionales_segun_p2_referencias_sim': 3687, 'coincide_con_p2_referencias_sim': True}.
Resumen: {"ausentes_por_causa": {"H1": 6, "mencion_fuera_del_texto_del_resolvedor": 3}, "ausentes_recuperadas_en_sim_h1": {"arista_origen_con_destino": 6, "rt5_completa": 4, "rt5_sin_tipo": 5}, "desarrollo": {"arista_origen_destino_presente": 21, "rt5_completa": 20, "rt5_sin_tipo": 21, "verbatim": 5}, "n_muestra": 30, "por_clase": {"a": 9, "b": 16, "verbatim": 5}, "r1": {"rt5_completa": 30, "rt5_sin_tipo": 30, "verbatim": 30}}.

| n | origen → destino | tipo destino r1 | r1 verbatim / R-T5 | desarrollo verbatim / R-T5 / sin tipo | clase | motivo | SIM-H1 R-T5 / sin tipo / arista al destino |
|---|---|---|---|---|---|---|---|
| 1 | ext::7.5.2 → ext::9.3.5 | Obligacion | sí / sí | no / no / no | a | arista ausente; la mención al destino está en un nodo de tipo Condicion, excluido como origen por TIPOS_ORIGEN (H1) | sí / sí / sí |
| 2 | ext::3.5.6.5 → ext::14.2.1 | Restriccion | sí / sí | no / no / no | a | arista ausente; ningún nodo de contenido anclado en el origen tiene la mención en el texto que lee el resolvedor; E0 la tiene en el texto propio | no / no / no |
| 3 | ext::3.3.2 → ext::14.2.1 | Excepcion | sí / sí | sí / sí / sí | — | verbatim presente en las dos generaciones | — |
| 4 | ext::3.6.1.3 → ext::3.5 | Operacion | sí / sí | sí / sí / sí | — | verbatim presente en las dos generaciones | — |
| 5 | ext::3.16.3.5 → ext::3.16.3.1 | Obligacion | sí / sí | no / no / no | a | arista ausente; ningún nodo de contenido anclado en el origen tiene la mención en el texto que lee el resolvedor; E0 la tiene en el texto propio | no / no / no |
| 6 | ext::14.2.1 → ext::3.3 | Operacion | sí / sí | no / sí / sí | b | presente por contenido (R-T5) con otra evidencia verbatim | — |
| 7 | ric::3.1.2 → cap::2.13 | Operacion | sí / sí | no / sí / sí | b | presente por contenido (R-T5) con otra evidencia verbatim | — |
| 8 | cap::3.1.3 → cap::3.1.12 | Operacion | sí / sí | no / sí / sí | b | presente por contenido (R-T5) con otra evidencia verbatim | — |
| 9 | pro::2.3.5.1 → pro::3.1.6 | Operacion | sí / sí | sí / sí / sí | — | verbatim presente en las dos generaciones | — |
| 10 | ext::14.2.1.9 → ext::3.6 | Operacion | sí / sí | no / no / no | a | arista ausente; ningún nodo de contenido anclado en el origen tiene la mención en el texto que lee el resolvedor; E0 la tiene en el texto heredado | no / no / no |
| 11 | ext::8.5.19.2 → ext::8.5.6 | Obligacion | sí / sí | sí / sí / sí | — | verbatim presente en las dos generaciones | — |
| 12 | ext::8.5.20.3 → ext::8.5.10 | Restriccion | sí / sí | no / no / no | a | arista ausente; la mención al destino está en un nodo de tipo Condicion, excluido como origen por TIPOS_ORIGEN (H1) | no / sí / sí |
| 13 | ext::3.16.3.6 → ext::3.16.3.2 | Obligacion | sí / sí | no / no / sí | b | presente por contenido (R-T5 sin tipo): el nodo destino tiene otro tipo | — |
| 14 | cap::2.8.3.2 → cap::S5 | Obligacion | sí / sí | no / sí / sí | b | presente por contenido (R-T5) con otra evidencia verbatim | — |
| 15 | ext::S3 → ext::3.14 | Obligacion | sí / sí | no / sí / sí | b | presente por contenido (R-T5) con otra evidencia verbatim | — |
| 16 | cap::2.9.1 → cap::2.12.8.1 | Restriccion | sí / sí | no / sí / sí | b | presente por contenido (R-T5) con otra evidencia verbatim | — |
| 17 | cap::2.9.1 → cap::2.12.8.2 | Restriccion | sí / sí | no / sí / sí | b | presente por contenido (R-T5) con otra evidencia verbatim | — |
| 18 | pro::2.3.4 → pro::2.3.2.1 | Obligacion | sí / sí | no / sí / sí | b | presente por contenido (R-T5) con otra evidencia verbatim | — |
| 19 | cap::3.1.11.3 → cap::3.1.14 | Obligacion | sí / sí | sí / sí / sí | — | verbatim presente en las dos generaciones | — |
| 20 | cla::7.2.5 → cla::6.5.5.8 | Excepcion | sí / sí | no / no / no | a | arista ausente; la mención al destino está en un nodo de tipo Definicion, excluido como origen por TIPOS_ORIGEN (H1) | sí / sí / sí |
| 21 | ext::13.4.6 → ext::4.4 | Operacion | sí / sí | no / sí / sí | b | presente por contenido (R-T5) con otra evidencia verbatim | — |
| 22 | cap::3.1.14 → cap::3.1.14.1 | Obligacion | sí / sí | no / sí / sí | b | presente por contenido (R-T5) con otra evidencia verbatim | — |
| 23 | ext::9.3.8 → ext::9.3.1 | Operacion | sí / sí | no / no / no | a | arista ausente; la mención al destino está en un nodo de tipo Condicion/Potestad, excluido como origen por TIPOS_ORIGEN (H1) | no / no / sí |
| 24 | ext::10.10.1 → ext::10.6.6 | Obligacion | sí / sí | no / no / no | a | arista ausente; la mención al destino está en un nodo de tipo Condicion/Potestad, excluido como origen por TIPOS_ORIGEN (H1) | sí / sí / sí |
| 25 | cap::5.3.2.2 → cap::5.3.1.2 | Restriccion | sí / sí | no / no / no | a | arista ausente; la mención al destino está en un nodo de tipo Definicion, excluido como origen por TIPOS_ORIGEN (H1) | sí / sí / sí |
| 26 | ext::4.8.3 → ext::4.4 | Obligacion | sí / sí | no / sí / sí | b | presente por contenido (R-T5) con otra evidencia verbatim | — |
| 27 | ext::4.8.3 → ext::4.5 | Obligacion | sí / sí | no / sí / sí | b | presente por contenido (R-T5) con otra evidencia verbatim | — |
| 28 | ext::3.5.1.10 → ext::7.11.1.3 | Operacion | sí / sí | no / sí / sí | b | presente por contenido (R-T5) con otra evidencia verbatim | — |
| 29 | ext::4.3.2.3 → ext::4.5 | Obligacion | sí / sí | no / sí / sí | b | presente por contenido (R-T5) con otra evidencia verbatim | — |
| 30 | ext::8.5.21 → ext::14.1.1 | Restriccion | sí / sí | no / sí / sí | b | presente por contenido (R-T5) con otra evidencia verbatim | — |

SIM-H1 es evidencia sobre la causa, no un resultado de r2. «Arista al destino» = alguna arista referencia de la simulación con fuente en el origen y properties.destino igual al de la fila, sin condición sobre el ancla del nodo destino: donde da sí y R-T5 da no, la diferencia está en la condición (2) de R-T5 (ancla primaria del nodo destino de r1), no en la mención.

Clasificación asistida (lectura de texto de esta instancia, para revisión de la autora) de las ausencias sin mención en el texto del resolvedor: n=2, la descripción de la Excepcion termina en «comprendidos en este punto 3.5» y deja afuera «en el marco de lo previsto en el punto 14.2.1»; n=5, las Excepciones de `ext::3.16.3.5` parafrasean «Lo previsto en los puntos 3.16.3.1. al 3.16.3.4.» como «la declaración jurada»; n=10, la mención está solo en el texto heredado del chunk y E1 no la llevó a ningún nodo.

**PROPUESTA — la entrada de r2 la sella la autora (laudo §3.1, punto 2).** Recomendada: A.
- (A) re-direccionar T5 en una unidad de la suite por contenido (R-T5) sobre la misma muestra sellada; esperado r2 = persiste: en desarrollo faltan 9 de 30 (6 por H1 y 3 cuya mención no llegó al texto que lee el resolvedor, que r2 no cambia porque no toca E1). Si H1 entra a r2, la simulación en memoria recupera 4 de las ausentes con R-T5 (5 sin tipo) y T5 sigue en persiste; pasaría a resuelto solo si las ausencias de E1 se resuelven en una release que toque el prefijo.
- (B) declarar T5 no comparable entre generaciones (la muestra y su evidencia verbatim son de r1) y sellar esperado r2 = persiste; reemplazarla por una muestra sobre r2 con direccionamiento (chunk_id, relación, tipo de destino), como anticipa reports/tanda0/obs12_lectura/decision_tests.txt.
- (nota) la fixture guarda solo el estado del ítem: con cualquier opción, un «persiste» esperado no detecta que las ausencias crezcan; registrar el conteo como criterio exige un cambio de la suite.

### T7

Verifica: `scripts/regression_kg.py:1057-1083`; `scripts/regression_kg.py:1086-1093`; `data/experiment/reextraccion_v2/corpus_v2/r1_tests.py:63-82 (origen)`.
Estado: r1 en la fixture **resuelto**, r1 medido **resuelto**, desarrollo **persiste**.

| parte | r1 | desarrollo | clase | motivo |
|---|---|---|---|---|
| P1 propuestos con cuarentena=true (normalizada) | sí | sí | — | cumple en las dos generaciones (sin clase) |
| P2 ningún propuesto con id de catálogo | sí | sí | — | cumple en las dos generaciones (sin clase) |
| P3 toda padre_sugerido apunta a un id del catálogo | sí | sí | — | cumple en las dos generaciones (sin clase) |
| P4 ninguna subclase_de desde un propuesto (flaggeada) | sí | sí | — | cumple en las dos generaciones (sin clase) |
| P5 ningún Sujeto fuera del catálogo que no sea propuesto | sí | no | c | los Sujetos fuera del catálogo JSON están en el bloque v3 del perfil (hallazgo E1, decisión pre-registrada del 27/09) |

Evidencia (`analisis.T7_E4-a7`): bloque v3 del perfil 102 ids, catálogo JSON 101; en el bloque y no en el JSON: ['Sujeto_banco_central_del_exterior', 'Sujeto_entidad_depositaria', 'Sujeto_entidad_girada', 'Sujeto_entidad_originante_de_transferencia', 'Sujeto_entidad_receptora', 'Sujeto_fmi']; los Sujetos fuera de catálogo de desarrollo están todos ahí: sí (['Sujeto_banco_central_del_exterior', 'Sujeto_entidad_originante_de_transferencia', 'Sujeto_entidad_receptora', 'Sujeto_fmi']). Contrafáctico R-CAT: {'T7_pass': True, 'T7_malos': 0, 'T7_fuera': 0, 'E4-a7_estado': 'resuelto', 'E4-a7_detalle': 'propuestos=19 sin_cuarentena_true=0 con_id_de_catalogo=0 sujetos_fuera_catalogo_no_propuestos=0'}.

**PROPUESTA — la entrada de r2 la sella la autora (laudo §3.1, punto 2).** Recomendada: A.
- (A) si entra a r2 el ítem de la §1.6 que completa esquema_v3_clases.json con los ids del bloque v3: esperado r2 = resuelto (verificado en memoria con R-CAT sobre desarrollo).
- (B) si no entra: esperado r2 = persiste, con los ids fuera de catálogo documentados (misma causa que el FAIL conocido de S19).

### E4-a7

Verifica: `scripts/regression_kg.py:1199-1212`; `data/experiment/reextraccion_v2/corpus_v2/r1_e4.py:18-19, :141-147 (origen)`.
Estado: r1 en la fixture **resuelto**, r1 medido **resuelto**, desarrollo **persiste**.

| parte | r1 | desarrollo | clase | motivo |
|---|---|---|---|---|
| P1 propuestos con cuarentena=true (normalizada) | sí | sí | — | cumple en las dos generaciones (sin clase) |
| P2 ningún propuesto con id de catálogo | sí | sí | — | cumple en las dos generaciones (sin clase) |
| P3 ningún Sujeto fuera del catálogo que no sea propuesto | sí | no | c | mismos cuatro ids que T7 P5 |

Evidencia (`analisis.T7_E4-a7`): bloque v3 del perfil 102 ids, catálogo JSON 101; en el bloque y no en el JSON: ['Sujeto_banco_central_del_exterior', 'Sujeto_entidad_depositaria', 'Sujeto_entidad_girada', 'Sujeto_entidad_originante_de_transferencia', 'Sujeto_entidad_receptora', 'Sujeto_fmi']; los Sujetos fuera de catálogo de desarrollo están todos ahí: sí (['Sujeto_banco_central_del_exterior', 'Sujeto_entidad_originante_de_transferencia', 'Sujeto_entidad_receptora', 'Sujeto_fmi']). Contrafáctico R-CAT: {'T7_pass': True, 'T7_malos': 0, 'T7_fuera': 0, 'E4-a7_estado': 'resuelto', 'E4-a7_detalle': 'propuestos=19 sin_cuarentena_true=0 con_id_de_catalogo=0 sujetos_fuera_catalogo_no_propuestos=0'}.

**PROPUESTA — la entrada de r2 la sella la autora (laudo §3.1, punto 2).** Recomendada: A.
- (A) igual que T7: resuelto si se completa el catálogo JSON (verificado con R-CAT); P3 de E4-a7 es la P5 de T7.
- (B) persiste si no se completa.

### E4-a8

Verifica: `scripts/regression_kg.py:1215-1236`; `data/experiment/reextraccion_v2/corpus_v2/r1_e4.py:18-24, :141-202 (origen)`.
Estado: r1 en la fixture **resuelto**, r1 medido **resuelto**, desarrollo **persiste**.

| parte | r1 | desarrollo | clase | motivo |
|---|---|---|---|---|
| P1 alias_resueltos en los ids de catálogo de la tabla de r1 | 3/3 | 0/3 | b | lee un artefacto propio de r1 (salida_r1/e4_propuestos.json); con la tabla del propio ensamblado (R-E4a8) desarrollo cumple |
| P2 los propuestos resueltos no quedan en el grafo ni con aristas | 3/3 | 3/3 | — | cumple en las dos generaciones (sin clase) |

Evidencia (`analisis.E4-a8`): tablas {'r1': {'filas': 44, 'por_estado': {'cuarentena': 41, 'resuelto': 3}}, 'desarrollo': {'filas': 22, 'por_estado': {'cuarentena': 19, 'resuelto': 3}}}; R-E4a8 r1 con su tabla: alias 3/3, ausentes 3; desarrollo con su tabla: alias 3/3, ausentes 3. Los tres ids de catálogo de la tabla de r1 en desarrollo: Sujeto_entidad_de_contraparte_central presente=sí, provenances de extracción 0, alias_resueltos None; Sujeto_importador presente=sí, provenances de extracción 6, alias_resueltos None; Sujeto_vpu_rigi presente=sí, provenances de extracción 17, alias_resueltos None. Un id con provenances de extracción y sin alias_resueltos fue emitido por E1 con el id de catálogo (en desarrollo E4 solo resolvió las filas de su propia tabla); un id con 0 provenances de extracción está solo como nodo de esqueleto. Lo que E4-a8 verifica es la mecánica del merge de E4, que R-E4a8 cumple en las dos generaciones.

**PROPUESTA — la entrada de r2 la sella la autora (laudo §3.1, punto 2).** Recomendada: A.
- (A) re-direccionar E4-a8 en una unidad de la suite para que lea la tabla e4_propuestos.json del ensamblado bajo prueba (R-E4a8); esperado r2 = resuelto si la tabla de r2 tiene filas resueltas, no_aplicable si no tiene.
- (B) sin cambio de la suite: declarar E4-a8 no comparable (lee un artefacto de r1) y sellar esperado r2 = persiste.

## 5. Los otros cuatro ítems que cambian (sin diagnóstico)

| ítem | r1 fixture | r1 medido | desarrollo | detalle r1 | detalle desarrollo |
|---|---|---|---|---|---|
| BKL-0006 | persiste | persiste | no_aplicable | invertido: tabla=False; sin Excepcion de cajas en cap 1.2 (sub-check no aplicable); Restriccion:Restriccion_exigencia_basica_para_bancos_salvo_caj clase=bancos montos=['2.500'] umbral='2.500 millones  | sin nodos anclados en cap 1.2 con «exigencia básica»: tabla del 1.2 no extraída |
| BKL-0028 | no_aplicable | no_aplicable | persiste | catálogo 2.0: el defecto se registró sobre el catálogo v3 de b54 y su remedio exige ids nuevos en ese catálogo y un grafo extraído con perfil v3_b54 (inventario_B21_fase1.md:109); defecto confirmado,  | catálogo v3: alias «del exterior» en ['Sujeto_entidad_financiera', 'Sujeto_banco', 'Sujeto_entidad_cambiaria']; ids separados []; presentes en el grafo []. defecto confirmado, no corrección aplicada. |
| BKL-0029 | no_aplicable | no_aplicable | persiste | el grafo no cubre convca (ninguna provenance ni TextoOrdenado de convca; el rol Sujeto_rol_alcance_convca no tiene miembro_de entrantes); defecto confirmado, no corrección aplicada. | ids candidatos en catálogo=[]; miembro_de del rol=['Sujeto_entidad_financiera']; residuo colectivo_operativo_sin_id=True. defecto confirmado, no corrección aplicada. |
| RT-C5-3 | persiste | persiste | resuelto | sin N5 (nodo del 6.5.2.2): el gold no está en el grafo | N5 ['Definicion_en_negociacion_o_con_acuerdos_de_refinanciacion_83b87e']: gold 2/2 |

## 6. Los 36 ítems que no cambian

| ítem | r1 fixture | r1 medido | desarrollo |
|---|---|---|---|
| BKL-0003 | persiste | persiste | persiste |
| BKL-0004 | persiste | persiste | persiste |
| BKL-0005 | resuelto | resuelto | resuelto |
| BKL-0007 | persiste | persiste | persiste |
| BKL-0017 | persiste | persiste | persiste |
| BKL-0019 | persiste | persiste | persiste |
| BKL-0023 | no_aplicable | no_aplicable | no_aplicable |
| BKL-0026 | no_aplicable | no_aplicable | no_aplicable |
| BKL-0027 | no_aplicable | no_aplicable | no_aplicable |
| E4-a1 | resuelto | resuelto | resuelto |
| E4-a2 | resuelto | resuelto | resuelto |
| E4-a3 | resuelto | resuelto | resuelto |
| E4-a4 | resuelto | resuelto | resuelto |
| E4-a5 | resuelto | resuelto | resuelto |
| E4-a6 | resuelto | resuelto | resuelto |
| E4-b | resuelto | resuelto | resuelto |
| E4-c | no_aplicable | no_aplicable | no_aplicable |
| I1 | no_aplicable | no_aplicable | no_aplicable |
| I2 | no_aplicable | no_aplicable | no_aplicable |
| I3 | resuelto | resuelto | resuelto |
| I4 | resuelto | resuelto | resuelto |
| I5 | resuelto | resuelto | resuelto |
| RT-C5-1 | persiste | persiste | persiste |
| RT-C5-2 | persiste | persiste | persiste |
| RT-C5-4 | persiste | persiste | persiste |
| RT-C5-5 | no_aplicable | no_aplicable | no_aplicable |
| RT-C6-1 | resuelto | resuelto | resuelto |
| RT-C6-2 | resuelto | resuelto | resuelto |
| RT-C6-3 | resuelto | resuelto | resuelto |
| RT-C6-4 | resuelto | resuelto | resuelto |
| RT-C7-1 | resuelto | resuelto | resuelto |
| RT-C7-2 | resuelto | resuelto | resuelto |
| RT-C7-3 | resuelto | resuelto | resuelto |
| T1 | resuelto | resuelto | resuelto |
| T3 | resuelto | resuelto | resuelto |
| T6 | resuelto | resuelto | resuelto |

## 7. Conteos

- items: 46
- cambian: 10
- no_cambian: 36
- seis_mas_cuatro_igual_a_cambian: True
- transiciones_suman_46: True
- t5_filas_suman_30: True
- resuelto_a_persiste: ['E4-a7', 'E4-a8', 'T2', 'T4', 'T5', 'T7']
