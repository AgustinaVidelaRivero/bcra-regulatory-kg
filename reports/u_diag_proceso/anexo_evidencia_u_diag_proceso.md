# U-DIAG-PROCESO — anexo de evidencia

Acompaña a `reporte_u_diag_proceso.md`. Solo lectura, USD 0, sin API ni Neo4j. HEAD `ebd7b1e`. Todo número sale
de un archivo de `salidas/`, producido por un script de `code/` con el comando del §6.

## 1. Fuentes firmadas, leídas en su commit (regla k)

| documento | commit | sha256 del texto en ese commit |
|---|---|---|
| `data/experiment/esq/cobertura/tabla_resultados_esq2.md` | `bbac990` | `0599ffe4…` |
| `data/experiment/esq/prerregistro_esq2.md` | `2240c9c` | `ad3a24f8…` |
| `data/experiment/esq/laudo_ESQ-3a_retoques.md` | `0a76549` | `ff8c5d8a…` |
| `data/experiment/esq/laudo_esquema_congelado.md` | `2593d4d` | `64c5da88…` |
| `data/experiment/esq/enmienda2_L-ESQ-R2_remite_a_2026-10-02.md` | `5f9a731` | `e779bd70…` |
| `data/experiment/esq/enmienda_uso_ventana_2026-09-30.md` | `30f106c` | `f2dbec98…` |
| `docs/protocolo_entre_tandas.md` | `a304b89` | `b23d37c5…` |
| `docs/mandatos/UPROMPT_R2_prefijo_nuevo.md` | `b901f6d` (nota fechada en `ebd7b1e`) | `80020edc…` |

El worksheet de ESQ-2 (`data/experiment/esq/cobertura/fichas/worksheet_fichas_esq2.json`, último commit `b2e9e90`,
sin cambios en el árbol) y `desvios_lectura_esq2.md` se citan del árbol, idéntico a `bbac990`.

## 2. Las diez fichas, pieza por pieza (tareas 1 y 2)

Grafo: el grafo r2a de U-MED-R2A NO está commiteado (`data/experiment/medicion_r2a/` y
`corpus_tanda0/ens_*_r2a/` figuran sin rastrear en `git status`). El más reciente commiteado es KG-Tanda0-Diez-r1
(`corpus_tanda0/ens_diez/r1/kg.json`, sha `dd42d6d9…`, commit `1b8916c`), que cubre los diez TOs de la tanda 0 y
ninguno de los seis TOs de las fichas (ayccef, expaef, adrei, prevmi, lavdin, actgar). La persistencia en un grafo
no es decidible con material commiteado. La decido por pieza: E0 e0-r2 y herencia (corrida de control en copia,
`salidas/fichas_e0r2.json`), remisiones r2 con las reglas (a) a (i) (`salidas/menciones_fichas.txt`), el prefijo
vigente del perfil `v3_b54` (sha `35e88c2dd0a2`, hash `54a111e2175f`, el de la tanda 0) y E3.

En las diez: id, texto propio y herencia de e0-r2 idénticos a los del worksheet (`fichas_e0r2.txt`); el detector
r2 no encuentra ninguna cita al destino; solo toma la línea «Sección N. …» del tramo heredado de la sección como
cita de esa misma sección, que la regla «el propio punto nunca es destino» descarta
(`data/experiment/reextraccion_v2/corpus_v2/r1_referencias.py:1178-1225`).

| ficha | origen | chunk | problema y forma | texto (worksheet) | por qué no lo cubre el proceso | estado con el pipeline actual |
|---|---|---|---|---|---|---|
| 11 | azarosa | ayccef::4.2.7.2 | F1 (a): el encabezado vive en la línea de título de 4.2.7, sin unidad propia | propio `:1222`; encabezado `:1242`; nota `:1282` | E0 no emite mini-chunk sin segmento de prosa (`e0_lib.py:1584-1591`, `:1773-1774`); el título viaja como tramo `encabezado` (`:1630`); el prefijo prohíbe extraer del heredado (`prompt_e1.py:52`, `:122`; mensaje `:479-481`) | PERSISTE por construcción: e0-r2 sigue sin mini-chunk de 4.2.7; en la tanda 0, 8 de 10 encabezados-título sin nodo anclado (`f1a_tanda0.txt`) |
| 13 | azarosa | expaef::6.6.2 | F1 (b): composición parcial, se pierde «a la SEFyC» | encabezado `:1405`; nota `:1468` | la regla (i) del prefijo permite interpretar el encabezado, no manda componer | NO DECIDIBLE en grafo (TO no corrido); la causa del prefijo sigue |
| 48 | azarosa, contaminada | ayccef::3.4.1 | F1 (b): inciso vacío | encabezado `:5868`; nota `:5908` | ídem | NO DECIDIBLE; la forma «vacía» bajó en la tanda 0 (§3) |
| 52 | azarosa | expaef::1.1.2.5 | F1 (b): sin composición, operación inventada | encabezado `:6230-6235`; nota `:6322` | ídem | NO DECIDIBLE |
| 64 | azarosa | adrei::4.3.1::intro | F1 (c): encabezado con unidad propia, extraído vacío | texto `:7811`; nota `:7866` | E1 no extrajo el deber cuyo objeto está en los incisos; la guarda LAUDO B de E3 no bloquea el faltante que cita la cláusula ordenadora (`ratchet_e3.py:43-53`) | NO DECIDIBLE; forma rara en la tanda 0 (§3); la guarda no eximió ningún mini sin contenido en la tanda 0 (`censo_estructural.json`, `guarda_laudoB_en_minis_sin_contenido` vacío) |
| 18 | dirigida | prevmi::1.3.3 | VU forma B: exclusión → regla de la unidad hermana prevmi::1.2 | propio `:2115`; encabezado «1.3. Exclusiones.» `:2125` | E1 ve solo el chunk; E3 excluye otras unidades (`prompt_e3.py:85`); el ensamblado une solo por cita | PERSISTE por construcción |
| 39 | azarosa, contaminada | lavdin::3.3.4.3 | VU forma A: condición → excepción de lavdin::3.3.4::intro (y esta → regla de lavdin::3.1) | propio `:4664`; encabezado `:4679-4684`; nota `:4742` | `condicion_de` «del mismo chunk» (`prompt_esq3b_v2.py:197-200`) | PERSISTE por construcción |
| 61 | dirigida | actgar::1.3.1::intro | VU forma B: no alcanzadas → limitación legal de actgar::1.1 | propio `:7448`; encabezado `:7463` | ídem 18 | PERSISTE por construcción |
| 72 | dirigida | ayccef::3.5.1.1 | VU forma A: condición → autorización de ayccef::3.5::intro y 3.1 | propio `:8742`; encabezados `:8757`, `:8762` | ídem 39 | PERSISTE por construcción |
| 44 | dirigida (nota) | lavdin::3.3.5 | VU forma B: excepción → regla de lavdin::3.1 | nota `:5412` | ídem 18 | PERSISTE por construcción |

Origen y contaminación: `salidas/prevalencia.txt`; contaminadas azarosas 23, 39, 48 y 65
(`desvios_lectura_esq2.md@bbac990:48-50`).

Destinos de VU leídos en la E0 e0-r2 de la copia: prevmi::1.2 («Las pautas de previsionamiento … deberán aplicarse
sobre las financiaciones comprendidas…»); actgar::1.1 («…no podrán afectar sus activos en garantía sin previa
autorización del BCRA»); ayccef::3.1 («La fusión … quedará sujeta a la autorización del BCRA»); lavdin::3.1
(desembolsos superiores a $ 50.000 acreditados en cuenta). Predicados para cada par en la matriz r2
(`data/experiment/pyd_r2/code/modelos_r2.py:131-139`): Condicion → Excepcion u Operacion, `condicion_de`; Excepcion
→ Restriccion, `exceptua`; Excepcion → Obligacion, `exceptua_obligacion`. Ninguno falta.

## 3. Tanda 0 como población análoga (indicadores mecánicos, no lectura)

Entradas commiteadas: E0 legada `e0_chunking/salida_tanda0/` (`47c9283`); extracción final E1 + E3 y veredictos de
E3 `corpus_tanda0/salida/*/` (`ad6d5ad`).

- Unidades sin entidades de contenido (`vacios_esq_vs_t0.txt`; ÍTEM = punto cuyo último tramo heredado termina en
  «:»; MINI ORDENADOR = intro que termina en «:»):

  | | ESQ-2, E1 solo, prefijo de producción | tanda 0, primera pasada de E1 `v3_b54` | tanda 0, tras E3 |
  |---|---|---|---|
  | ítems vacíos | 20 de 264 | 6 de 706 | 1 de 690 con salida final (16 sin salida final) |
  | minis ordenadores vacíos | 14 de 77 | 9 de 212 | 3 de 202 con salida final (10 sin salida final) |

  TOs distintos y sin pareo: la baja no se atribuye a una pieza. La mayor parte ya aparece en la primera pasada de E1.
- Encabezados en línea de título sin unidad propia: 10 en la tanda 0, con 39 hijos; 2 de los 10 tienen algún nodo
  anclado en su unidad (`f1a_tanda0.txt`). Partición: 87 unidades, 330 hijos; ESQ-2: 6 y 20 (`censo_estructural.json`).
- Composición dispar dentro de una misma lista, lectura mía sobre `extracciones_finales_*.jsonl`, NO MEDIDA su tasa:
  ctacte::2.3.4.1 sale como Definicion sin «Se deberá especificar» y ctacte::2.3.4.2 como Obligacion compuesta;
  cap::8.3.3.2 sale como Condicion sin el deber de «deberán observar los siguientes requisitos» y cap::8.3.3.1 como
  Obligacion compuesta; cap::10.2.1.1 y 10.2.1.2, Definicion sin «Serán ECAI elegibles».
- E3 (`censo_estructural.json`, `e3_faltantes`; «heredado» = el primer token de `ubicacion` es una unidad del
  contexto heredado del chunk, regla mía): en la primera verificación, 537 faltantes con ubicación heredada, 121
  bloqueantes; en la re-verificación, 91 y 16.
- Vínculo entre unidades (`vu_tanda0.txt`, `vu_b_alcance.txt`): 458 Condicion en ítems; 250 con `condicion_de`
  hacia un nodo del mismo chunk que la matriz congelada rechazó (r2a la recupera); 56 sin ninguna `condicion_de`.
  De esas 56, 36 tienen como último tramo heredado el intro de un ancestro con nodos de un tipo destino admitido
  (forma A, alcance de VU-B), 3 un encabezado de título, 17 otro caso. 12 Excepcion bajo encabezados de salvedad,
  7 sin `exceptua*`: ninguna con destino determinable en un ancestro.
- Escala del vínculo: 247 de 2.434 unidades de la tanda 0 y 415 de 9.324 de la partición tienen un encabezado de
  salvedad o de condición en su herencia (`censo_estructural.json`; criterio en el docstring del script). Es la
  población donde puede ocurrir, no la prevalencia.

## 4. Bases de las estimaciones de costo

- Precios de E1 (Haiku 4.5): entrada 1,00, salida 5,00, escritura de caché 1,25, lectura de caché 0,10 USD por
  millón de tokens (`data/experiment/reextraccion_v2/corpus_v2/runner_corpus.py:90-92`).
- Unidad completa E1 + E3 de la tanda 0: USD 40,35 / 2.434 = USD 0,0166 (`docs/plan_tesis.md@ebd7b1e:400`; mandato de
  U-PROMPT-R2, `b901f6d:196`).
- E1 por unidad sin E3: USD 4,1079 / 762 = USD 0,0054 (corrida de ESQ-2, mensaje del commit `a7788c1`).
- F1-A: +250 tokens de prefijo (SUPUESTO, NO VERIFICADO: depende del texto que se apruebe) × 2.434 unidades × 0,10 /
  10⁶ = USD 0,061, más la escritura de caché de la primera unidad de cada corrida secuencial (decisión 2 de
  `docs/decisiones_caching_extraccion.md`), del orden de USD 0,003; +15 tokens de salida por ítem o mini ordenador
  (SUPUESTO, NO VERIFICADO) × 918 (706 + 212) × 5 / 10⁶ = USD 0,069. Total ≈ USD 0,13 dentro de U-REEXT-T0. En P4:
  5 chunks × 2 brazos × USD 0,0054 ≈ USD 0,05, dentro del tope de USD 2 (decisión 18).
- VU-A: +150 tokens de prefijo (SUPUESTO) × 2.434 × 0,10 / 10⁶ ≈ USD 0,04.
- F1-B: 10 unidades nuevas × USD 0,0166 = USD 0,17 (tanda 0); 87 × 0,0166 = USD 1,44 (partición).
- A1.8: corrida del agente ≈ USD 0,022 (USD 0,064962 por tres corridas, U-MED-EJEMPLO-2, `docs/plan_tesis.md@ebd7b1e:327`).
- VU-B y la lectura de precisión: USD 0 (código sobre lo guardado y lectura asistida).

## 5. Observación lateral (fuera del mandato)

La regla (i) lee el tramo heredado `encabezado` de una sección («Sección 4. Transformación de…») como cita de esa
sección. En las diez fichas la descarta la regla del propio punto, sin arista. Si el mismo efecto entra en las
2.870 «menciones en texto heredado» de `data/experiment/r2_codigo/reglas_remisiones_postR3.md:102`, ese conteo
incluye autocitas de encabezado: NO VERIFICADO, no lo medí.

## 6. Comandos

Espejo copiado (regla l), sin enlaces: `e0_chunking/{correr_e0,e0_lib,e0_tablas}.py`, `corpus_v2/{r1_comun,r1_referencias}.py`,
`escalado_prep/{inventario_tos.csv,inventario_resumen.json}` y los diez PDF de `escalado_prep/pdfs/` (sha 10/10
contra `manifest_pdfs.sha256`), bajo `<espejo>/data/experiment/…`. Desde la raíz del repo, con
`PYTHONDONTWRITEBYTECODE=1` y `.venv/bin/python -B`:

```
code/correr_e0r2_esq.py <espejo> <salida_e0r2>                          → salidas/e0r2_conteos.txt (doble corrida: chunks idénticos)
code/comparar_fichas_e0r2.py . <salida_e0r2> salidas/fichas_e0r2.json    → salidas/fichas_e0r2.txt
code/menciones_fichas.py <espejo> salidas/fichas_e0r2.json <salida_e0r2> → salidas/menciones_fichas.txt
code/censo_estructural.py . <salida_e0r2> salidas/censo_estructural.json
code/f1a_tanda0.py salidas/censo_estructural.json                       → salidas/f1a_tanda0.txt
code/prevalencia.py <salida_e0r2> salidas/censo_estructural.json        → salidas/prevalencia.txt
code/vacios_esq_vs_t0.py <salida_e0r2>                                  → salidas/vacios_esq_vs_t0.txt
code/vu_tanda0.py                                                       → salidas/vu_tanda0.txt
code/vu_b_alcance.py                                                    → salidas/vu_b_alcance.txt
```

Las rutas `code/` y `salidas/` son relativas a `reports/u_diag_proceso/`.
