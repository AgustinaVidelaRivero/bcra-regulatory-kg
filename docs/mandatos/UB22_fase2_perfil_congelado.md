FIRMADO por la autora — 2026-09-26 (redactado 15/09; revisado por la mesa el 26/09 contra el pre-registro de la tanda 0, c80b03f)

MANDATO — U-B2.2 FASE 2: PERFIL «CONGELADO» EN scripts/shapes_validator.py.
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar.

CONTEXTO (dos líneas). La fase 1 (paquete revision_UB22_diag/, diagnóstico
diagnostico_UB22_fase1.md, huecos D1–D12) mostró que ningún validador de
shapes conoce el esquema congelado ni el formato de provenance de la
generación 3, y que el ítem «CHECKLIST DEL GATE — Esqueleto v3 inyectado y S15 en
verde» de B6.1 (hoy :680; el ancla es el id de la fila) reportaría FAIL por construcción. Esta fase implementa el instrumento del gate.

DECISIONES YA TOMADAS (autora, 15/09). No se re-deciden.
1. Opción A: se extiende scripts/shapes_validator.py (v0) detrás de un
   perfil nuevo. Sin perfil, el comportamiento es byte-idéntico al actual:
   la prueba es el reporte sobre data/experiment/run_3_ppf_core/kg.json
   contra reports/shapes_run_3_v0.md. CLÁUSULA DE ESCAPE: si extender v0
   exige reescribir su núcleo (por ejemplo, si su modelo de provenance no
   puede alojar los campos de la generación 3 sin tocar S1–S12), FRENÁS y
   lo declarás como desvío con la evidencia; no reescribís.
2. El vocabulario del perfil se LEE de data/experiment/esq/code/
   prompt_congelado.py (ENTITY_TYPES_CONGELADO, PREDICATES_CONGELADO,
   DOMAIN_RANGE_CONGELADO, enum de Obligacion.tipo, sha del texto
   e69feaaa…); nada de eso se copia en el validador. El validador verifica
   el sha al cargar y FRENA si no coincide. El catálogo de sujetos se lee
   del artefacto de --excepciones (esquema_v3_clases.json), como S15.
3. Tolerancia: referencia nodo→nodo (rol_fuente=referencia_cruzada) y
   padre_sugerido (rol_fuente=cuarentena_flaggeada) se ADMITEN en S1/S3 del
   perfil y no se exigen; su coherencia interna se mide y se reporta.
4. Severidad en el perfil, en dos secciones del reporte y con veredicto
   global PASA / NO PASA: BLOQUEANTES = S1, S2, S3, S4, S5, S6, catálogo
   (S13 ampliada), S15 y residuo del enum = 0. INFORMATIVAS con conteo =
   S7, S8, S10, S11, S12, coherencia de referencias nodo→nodo, coherencia
   de padre_sugerido, y aplica_a hacia sujetos en cuarentena. Sin perfil no
   cambia nada del reporte actual.
5. aplica_a hacia cuarentena: informativo (conteo), nunca bloqueante.

TAREA (una sola unidad): agregar a scripts/shapes_validator.py la opción
--perfil congelado, con este contenido, y su selftest.
a. S1: relaciones admitidas = las 13 de PREDICATES_CONGELADO ∪ las 4 de
   esqueleto (subclase_de, miembro_de, instancia_de, parte_de) ∪
   padre_sugerido. Toda otra relación es violación.
b. S3: firmas = DOMAIN_RANGE_CONGELADO (Sujeto como pseudo-tipo, igual que
   firma_valida de prompt_congelado.py) ∪ esqueleto solo Sujeto→Sujeto ∪
   referencia nodo→nodo solo si rol_fuente=referencia_cruzada ∪
   padre_sugerido solo de Sujeto nivel propuesto a Sujeto nivel clase o
   rol. La referencia TextoOrdenado→Comunicacion sigue por la matriz.
c. S4/S5 (provenance generación 3): en nodos y aristas, provenance es un
   dict con al menos {to, archivo, punto, rol_documental}; punto no vacío;
   provenances es lista no vacía y provenance == provenances[0]. Para
   rol_documental=esqueleto se admite to nulo, chunk_id nulo y paginas
   vacía; para cualquier otro rol_documental, to y archivo no vacíos.
d. S6: archivo ∈ {properties.archivo de los nodos TextoOrdenado del
   grafo} ∪ {archivo de las provenances con rol_documental=esqueleto}.
   Nada codificado a mano.
e. Catálogo (S13 ampliada): todo Sujeto tiene nivel ∈ {clase, instancia,
   rol, propuesto}; si nivel ≠ propuesto, su id está en el catálogo del
   artefacto de --excepciones; si nivel = propuesto, tiene
   properties.cuarentena y properties.padre_sugerido. Bloqueante.
f. Enum: para todo nodo Obligacion, properties.tipo ∈ enum congelado de
   6. Se reportan dos conteos separados: valores retirados (los que
   prompt_congelado.py declare como retirados, con requisito_de_estructura
   entre ellos) y otros valores fuera del enum. Bloqueante si cualquiera
   de los dos es distinto de 0 (vigilancia (5) del laudo de congelado).
g. Informativas nuevas: (i) referencias nodo→nodo cuyo properties.destino,
   sin el prefijo to::, no está en {p.punto for p in provenances} del nodo
   destino — comparado contra el CONJUNTO, nunca contra provenance[0];
   desglosado por properties.via; (ii) aristas padre_sugerido cuyo destino
   ≠ properties.padre_sugerido del origen, o cuyo origen no está en
   cuarentena; (iii) aplica_a cuyo destino es Sujeto nivel propuesto.
h. S7, S8, S10, S11, S12: mismo cómputo que hoy, rotuladas INFORMATIVAS en
   el perfil. S10 y S11 extienden sus tipos a los del dominio congelado de
   establecida_en y aplica_a respectivamente. S15 sin cambios.
i. Numeración: antes de nombrar una shape nueva, mostrá el enunciado que
   v0 declara para S13, S14, S16 y S17 (SHAPES_NO_IMPLEMENTADAS y su
   documentación, si existe); reutilizá un número SOLO si su enunciado
   declarado coincide con lo que implementás, y si no, numerá desde S18.
   Reportá la tabla número → enunciado.
j. Salida: además del reporte .md, un .json junto a él con los conteos de
   cada shape y el veredicto global, para que B2.3 compare grafos sin
   parsear markdown. En el perfil, el código de salida es distinto de 0
   cuando el veredicto es NO PASA; sin perfil, el código de salida no
   cambia.
k. Selftest nuevo scripts/selftest_shapes_congelado.py, solo stdlib,
   sobre fixtures sintéticos mínimos escritos en el propio selftest: por
   cada shape del perfil, un caso que pasa y un contraejemplo que falla,
   y un caso que verifica que el candado del sha frena.

BATERÍA DE NO REGRESIÓN (corrida completa antes de frenar; todo --out al
scratchpad, nunca al default):
1. Sin perfil, run_3_ppf_core/kg.json → reporte byte-idéntico a
   reports/shapes_run_3_v0.md (cmp; pegá la salida y los dos sha256).
2. Sin perfil, con --excepciones esquema_v3_clases.json, sobre el vigente
   data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json (sha
   0226e947…, verificalo y mostralo). ANTES de editar el validador, corré
   v0 sin perfil sobre el vigente con --out al scratchpad y anotá su
   sha256; debe dar 1350cd37…. Si no da, FRENÁS: el árbol no está donde la
   fase 1 lo dejó. Después de tus cambios, la corrida sin perfil debe ser
   byte-idéntica a esa.
3. Con --perfil congelado y --excepciones, sobre
   data/experiment/reextraccion_v2/corpus_v2/salida/kg.json (sha
   8e2eadee…; esqueleto v3; 6.178 nodos / 11.415 aristas): S15 PASS,
   S4–S6 PASS; el resto se reporta tal como dé, sin ajustar.
4. Con --perfil congelado y --excepciones, sobre el vigente r1: se reporta
   tal como dé (S15 FAIL esperado por esqueleto v2; las 5.645 referencias y
   las 41 padre_sugerido admitidas en S1/S3; informativa (i) debe dar 6,
   todas con via=texto_ordenado, e informativa (iii) 57). Ese .json es la
   línea de base de r1 para B2.3.
5. selftest_shapes_congelado.py en verde, con la cuenta de casos.
Cualquier diferencia en 1 o 2 es FRENO, no ajuste.
Un FAIL bloqueante en la corrida 3 es HALLAZGO y FRENO, no ajuste de la
shape: reportá qué regla, cuántos casos y tres ejemplos con path.

REQUISITOS TRANSVERSALES (CLAUDE.md §4 a–j).
- Escrituras permitidas: scripts/shapes_validator.py,
  scripts/selftest_shapes_congelado.py (nuevo) y tu scratchpad. Nada más:
  ni reports/, ni docs/, ni el plan, ni ningún kg.json. No commitees.
  Costo de API: 0.
- Zonas selladas de CLAUDE.md §3 intactas; todo kg.json es solo lectura.
- Toda afirmación con path:línea o comando; conteos recomputados antes de
  escribirse (§4.i); lo que no esté en un artefacto es NO ENCONTRADO.
- Paquete de revisión revision_UB22_fase2/ con manifest.txt (sha256 y una
  línea por archivo): los cinco reportes de la batería con sus .json, la
  salida del selftest, el diff completo del validador y el estado del
  árbol de trabajo (archivos modificados y nuevos, con el comando que uses
  y su salida pegada). Reporte al frenar de no más de 40 líneas; lo largo
  va al paquete.
- Cero nombres propios; decisiones por justificación técnica.
- PYTHONDONTWRITEBYTECODE=1 en todo Python que corras; ningún __pycache__
  nuevo en el repo.
- Si tu contexto se acerca al límite o vas a compactar, ANTES escribí en
  el scratchpad checkpoint_UB22_fase2.md con qué piezas (a–k) están
  hechas, cuáles faltan, qué archivos tocaste y qué puntos de la batería
  ya corriste, y reportá la ruta.

CRITERIO DE ACEPTACIÓN. Batería 1–5 completa con salidas pegadas; los dos
byte-idénticos demostrados con cmp y sha256; la tabla número → enunciado
de la pieza i; el .json de la corrida 4; el estado del árbol con solo los
dos archivos de scripts/ modificados o nuevos (más lo preexistente,
enumerado); grep de convenciones sobre el paquete, pegado aunque dé vacío.

FRENO al terminar. La autora revisa el diff antes de que nada se use en
el gate.
