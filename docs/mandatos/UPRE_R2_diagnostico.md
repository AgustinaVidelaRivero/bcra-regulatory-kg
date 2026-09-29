BORRADOR — PENDIENTE DE FIRMA DE LA AUTORA

MANDATO — U-PRE-R2-DIAG: DIAGNÓSTICO PREVIO A LA FIRMA DEL LAUDO DE r2.
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar. Unidad en DOS
ETAPAS con FRENO obligatorio al final de cada una: reporte corto (no más de
40 líneas) y espera de la revisión y del «seguí» escrito de la autora;
ninguna etapa arranca sin él. Costo de API: USD 0; ninguna llamada a la API;
Neo4j no se usa.

CONTEXTO. La fase 2a de la tanda 0 cerró con E6 (2399eb7; reporte
reports/tanda0/reporte_fase2a.md). El laudo de r2
(docs/laudo_release_r2_pipeline.md, aa7ee11, BORRADOR) tiene dos insumos
abiertos:
(i) La regression suite sobre KG-Tanda0-Desarrollo-r1 (eab2fdd0…), construido
    con el pipeline que r2 va a usar (perfil v3_b54, esquema congelado), da
    seis ítems que pasan de resuelto a persiste contra la entrada de
    KG-Reextraído-r1 en la fixture (scripts/regression_kg_esperado.json,
    sha256 696f3f94…): E4-a7, E4-a8, T2, T4, T5 y T7
    (reports/tanda0/lectura_e6_tanda0.md, tabla de la suite;
    reports/tanda0/regression_ens_desarrollo.json, cf6ca42). El gate de r2
    exige 0 regresiones contra una entrada de r2 que la autora sella antes de
    correrlo (laudo §3.1, punto 2).
(ii) El punto 3 de la lectura de E6 (plan, fila B6.0 fase 2a, «LECTURA DE
    E6») clasificó por clase A0.2 las respuestas parciales o incorrectas,
    pero no cruzó cada ausencia con los candidatos del laudo ni con los
    rechazos de la matriz (reporte de 2a, §4, punto 3).
Leé completos, antes de escribir una línea:
- el laudo de r2, §1 a §5;
- el reporte de 2a, §3 a §6;
- scripts/regression_kg.py (definiciones :1318-1352 y las funciones t_t2,
  t_t4, t_t5, t_t7, t_e4_a7 y t_e4_a8);
- data/experiment/reextraccion_v2/corpus_v2/r1_tests.py:30-82 y r1_e4.py
  :18-24 y :141-202;
- data/experiment/ev2_reporte/regla_atribucion.md;
- reports/tanda0/atribucion_tanda0.json;
- reports/u_estudio_matriz/uestmat_reporte_U-ESTUDIO-MATRIZ.md;
- reports/u_audit_tipos_v3/inventario_U-AUDIT-TIPOS-V3.md;
- reports/tanda0/obs12_lectura/decision_tests.txt.
Base: decisión de la autora del 29/09/2026 (plan, fila B2.10, unidad previa
a la firma; docs/checklist_pre_escalado.md, R27).

DECISIONES YA TOMADAS. No se re-deciden.
1. La unidad diagnostica y propone; no decide. La entrada de r2 en la
   fixture la sella la autora (laudo §3.1, punto 2); los candidatos que
   entran a r2 los elige la autora al firmar (laudo §5). Toda propuesta se
   rotula como propuesta.
2. EV2 y las trazas de C1 a C4 son material de desarrollo: se usan para
   diagnosticar y priorizar. r2 no se mide sobre EV2 (laudo §3.1, punto 7;
   principio 7 del plan). Nada de esta unidad se reporta como resultado
   sobre EV2.
3. Cada uno de los seis ítems se clasifica, parte por parte, en una de
   cuatro clases:
   (a) regresión real: el contenido o la estructura que el test verifica
       falta en el grafo de desarrollo;
   (b) efecto de direccionamiento: el test busca por id de nodo, por
       evidencia verbatim o por un artefacto propio de r1, y el contenido está
       presente con otra identidad;
   (c) efecto de diseño del perfil v3: el esqueleto v3 o el catálogo v3
       cambian lo que el test cuenta por una decisión sellada (por ejemplo,
       los seis ids del bloque v3 ausentes del catálogo JSON, plan, fila B6.0
       fase 2a, hallazgo E1);
   (d) no decidible con el material.
4. Cuando la hipótesis de un ítem sea (b), se re-verifica por contenido con
   una regla declarada en el reporte antes de aplicarla (por ejemplo, por
   chunk_id, relación, tipo de destino y texto, como propone
   decision_tests.txt), y se aplica la misma regla sobre r1 y sobre el
   desarrollo.
5. Puntos de partida, que son hipótesis de la mesa a verificar y no a
   asumir, tomados del detalle de regression_ens_desarrollo.json:
   - T5: 25 fallas de 30, 16 «presente con otra evidencia» y 9 «ausente»;
   - T4: faltan 0 nodos y 0 triplas del esqueleto de referencia, con 117
     aristas de esqueleto contra 82;
   - T7 y E4-a7: 4 Sujetos fuera del catálogo que no son propuestos;
   - E4-a8: alias_resueltos en 0 de 3 ids de catálogo de
     salida_r1/e4_propuestos.json;
   - T2: nodos separados de ext en cinco puntos con «125 %».
6. Población del cruce: los pares definitivos parciales o incorrectos de C1 a
   C4 cuya clase A0.2 es ausencia_kg: 8 en C1, 6 en C2, 8 en C3 y 9 en C4,
   31 en total (reports/tanda0/atribucion_tanda0.json, claves
   c1.lectura_plan_punto_3 y celdas.C<n>.pares_definitivos). El total se
   recomputa antes de clasificar; una diferencia es FRENO.
7. Categoría de cada ausencia: la primera etapa del pipeline donde se pierde
   la información, en este orden de precedencia, más las secundarias que
   apliquen:
   E. el chunk del ancla no se extrajo o se cortó (BKL-0030), o su contenido
      es una tabla linealizada (RX-10, laudo §1.3);
   G. E1 no lo emitió: no hay rastro en su salida cruda. Corregirlo toca el
      prompt y queda fuera de r2 («Qué no es» del laudo);
   B. E1 lo emitió en el chunk del ancla y la matriz lo rechazó por
      firma_invalida (población por chunk en
      reports/u_estudio_matriz/uestmat_poblacion_final.json; pares en
      reports/u_audit_tipos_v3/p4_resumen.json). Remite a la decisión sobre
      la matriz (checklist X1 y X11);
   F. quedó fundido o duplicado en otro nodo (H2 del §4; BKL-0031);
   C. está en el grafo pero sin la arista que lo conecta (candidato «nodos
      aislados» del §4);
   D. depende de una remisión no resuelta o falsa (H1 y H4, remisiones por
      paráfrasis y procedencia de las remisiones, §4);
   H. no decidible con el material.
   Para C1 y C2 (KG-Reextraído-r1) las etapas son las del pipeline de r1; el
   reporte declara qué registros de rechazo de r1 existen y marca NO
   ENCONTRADO los que no. Toda ausencia lleva además la columna «¿está en el
   grafo de la otra generación?» (r1 frente a desarrollo), que no es
   categoría.
8. Regla de presencia: la de A0.2 (regla_atribucion.md) para el ancla y sus
   descendientes; para ubicar el contenido en la salida cruda de E1 o entre
   los rechazados, una regla sobre la cita textual del criterio (números,
   porcentajes, plazos, fechas y términos definidos, normalizados),
   declarada en el reporte antes de aplicarla. Un caso que la regla no
   resuelve se marca «requiere lectura» y no se resuelve en esta unidad:
   quién lee lo decide la autora (checklist P15 y Q12).

D1 — Los seis ítems de la suite. USD 0.
a. Script nuevo reports/u_pre_r2/upre_d1_suite.py, de solo lectura, que
   corre las funciones de la suite por import, sin editarlas, sobre
   KG-Reextraído-r1 (0226e947…) y sobre KG-Tanda0-Desarrollo-r1
   (eab2fdd0…), y aplica las re-verificaciones de la decisión 4.
b. Por ítem: qué verifica (archivo:línea), su estado en r1 y en desarrollo,
   la clase de la decisión 3 por parte, la evidencia con su comando y una
   propuesta de estado esperado para la entrada de r2, con opciones cuando
   haya más de una (por ejemplo, re-direccionar el test en una unidad de la
   suite, o declarar el ítem no comparable entre generaciones).
c. Registrá además, sin diagnóstico, el detalle de los otros cuatro ítems que
   cambian (BKL-0006, BKL-0028, BKL-0029 y RT-C5-3) y la lista de los 36 que
   no cambian, para que la autora tenga los 46 al sellar la entrada.
d. Salidas: reports/u_pre_r2/d1_suite.json y d1_suite.md; doble corrida
   byte-idéntica.
FRENO D1: tabla de los seis ítems, con clase y propuesta; conteos con su
comando; sha256 de lo escrito.

D2 — Cruce de las ausencias con los candidatos. USD 0.
a. Script nuevo reports/u_pre_r2/upre_d2_ausencias.py, de solo lectura. Las
   dbs de caché se abren solo con file:…?immutable=1.
b. Una fila por ausencia: celda, pregunta, ancla, criterios no cubiertos,
   categoría primaria y secundarias (decisión 7), candidato del laudo (§1 o
   §4) o «fuera de r2», presencia en la otra generación, y evidencia con su
   comando o archivo:línea.
c. Tabla de prioridad: por candidato del laudo y por categoría, cuántas
   ausencias explica y en cuántas celdas. Aparte, la lista de «requiere
   lectura» y la de no decidibles.
d. Salidas: reports/u_pre_r2/d2_ausencias.json y d2_ausencias.md; doble
   corrida byte-idéntica.
FRENO D2, final: tabla de prioridad; conteos por categoría que sumen 31 o
la diferencia explicada; sha256 de lo escrito. Commit de la autora.

REQUISITOS TRANSVERSALES (CLAUDE.md §4 a–j), en todas las etapas.
- Escrituras: solo reports/u_pre_r2/ (se crea) y tu scratchpad. No se
  editan el plan, el laudo, la fixture, la suite, el backlog ni nada bajo
  data/experiment/. Nada sellado se toca. No commitees.
- PYTHONDONTWRITEBYTECODE=1 y .venv/bin/python -B en todo Python. Ningún
  __pycache__ ni .pyc nuevo: línea de base al inicio y control al cierre.
- Toda afirmación con path:línea o comando; conteos recomputados antes de
  escribirse (§4 i); lo que no esté en un artefacto es NO ENCONTRADO. Los
  mentores solo por rol; cero nombres propios.
- Si alguna clasificación requiere juicio sobre texto, la hace esta
  instancia y se rotula «clasificación asistida», lista para que la autora
  la revise; no se presenta como lectura de la autora.
- Paquete de revisión revision_UPRE_R2_D<n>/ por etapa, con manifest.txt;
  checkpoint checkpoint_UPRE_R2.md en el scratchpad, actualizado al cierre
  de cada etapa y antes de cualquier compactación.

CRITERIO DE ACEPTACIÓN por etapa: el reporte corto con las salidas
pedidas; git status --short con solo reports/u_pre_r2/ como nuevo; sha de
los sellados iguales al inicio y al cierre; doble corrida byte-idéntica;
grep de convenciones pegado aunque dé vacío. Criterio final: los seis ítems
clasificados con evidencia y propuesta; las 31 ausencias con su categoría o
marcadas; la tabla de prioridad reproducible por comando.

FRENO al final de cada etapa.
