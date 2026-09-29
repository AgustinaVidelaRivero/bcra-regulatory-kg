FIRMADO por la autora — 2026-09-29

ANEXO E5.c AL MANDATO U-TANDA0-2A — ADJUDICACIÓN CIEGA DE LAS CELDAS C2 A
C5, ANTES DE E6.
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar. Anexo en TRES
ETAPAS con FRENO obligatorio al final de cada una: reporte corto (no más de
40 líneas) y espera de la revisión y del «seguí» escrito de la autora;
ninguna etapa arranca sin él. Costo de API: USD 0 en las tres etapas; ninguna
llamada a la API.

CONTEXTO. Este anexo se inserta en el mandato U-TANDA0-2A
(docs/mandatos/UTANDA0_2A_corrida.md, e738cdd, sha256 ff5a001d…) entre el
FRENO de E5 y E6. E5 corrió las celdas C2, C3, C4 y C5 con juez v1 N=3 y §7;
su tabla quedó antes de adjudicar (reports/tanda0/tabla_celdas_E5.json):
25 pares con veredicto final requiere_adjudicacion en total. Leé completos,
antes de escribir una línea: el molde de la adjudicación de C1
(data/experiment/ev2_r1/code/worksheet_r1.py, selftest_nofuga_r1.py y
cierre_r1.py, 774acac; su molde de origen
data/experiment/ev2_adjudicacion/code/, 03ebe83);
data/experiment/ev2_r1/adjudicacion/nota_episodios_adjudicacion.md;
data/experiment/ev2_encadenamiento/code/agregacion_enc.py (regla sellada
9044a04); data/experiment/ev2_juez/mapping.py (mapping fijo §2); y
data/experiment/ev2_tanda0/code/celdas_tanda0.py (gold de C5 y los tres
criterios sin cita, :76-85).
Base: el pre-registro de la tanda 0 fija para C2 a C4 el protocolo de C1
«incluido el encadenamiento §7 y la adjudicación ciega»
(docs/preregistro_tanda0.md:308-309), y el mandato de 2a, al enumerar ese
protocolo (UTANDA0_2A_corrida.md:37-41), no incluye la adjudicación ni le
da etapa. Rige el pre-registro (CLAUDE.md §4 d). Decisión de la autora del
29/09/2026: la adjudicación de C2 a C5 va antes de E6.

PRECONDICIÓN. E5 commiteada por la autora (trazas, juez_out, registro de
modelos y tabla_celdas_E5.json). Pegá la salida de
git log --oneline -1 -- data/experiment/ev2_tanda0/juez_out
Si no hay commit, FRENO sin escribir nada.

DECISIONES YA TOMADAS. No se re-deciden.
1. Protocolo de C1 por celda, sin cambios de regla: población A = los pares
   con final requiere_adjudicacion; un par heredado de la base (no
   re-corrido) genera una ficha sobre la respuesta base; un par pendiente
   del §7 genera una ficha por cada voto requiere_adjudicacion de sus
   re-corridas, y dos re-corridas con texto idéntico comparten ficha; el
   par decidido por invariancia no genera ficha (worksheet_r1.py:6-12).
   Muestra de control (población B) sobre los finales post-§7:
   ceil(10 %) del estrato correcto y ceil(10 %) del estrato parcial más
   incorrecto, con generador nuevo por estrato sobre ids ordenados; par
   re-corrido → la re-corrida de menor rep cuyo veredicto coincide con el
   final; no re-corrido → la base (worksheet_r1.py:13-19 y :201-239). Una
   semilla propia por celda, declarada en el código. La muestra mide la
   tasa de error del juez y no reemplaza veredictos.
2. Regla de C5 (decisión de la autora del 29/09/2026). Los tres criterios
   sin cita (T0F-008 criterios 1 y 3, T0F-013 criterio 1;
   CRITERIOS_CITA_VACIA_AUTORIZADOS, celdas_tanda0.py:84-85) quedan fuera de
   la muestra de control: T0F-008 y T0F-013 se excluyen del marco de
   muestreo de la población B de C5 (la ficha es la unidad de la muestra y
   el acuerdo exacto por ficha exige todos sus criterios). Si alguna de las
   dos cae en la población A, la marca de la autora es definitiva por
   diseño. La exposición de sus veredictos en el FRENO de E5, por la
   decisión (a), se declara como episodio, con el precedente del episodio 1
   de C1. Declaración de la autora del 29/09/2026: no abrió los archivos
   SOLO_MESA.
3. Dos planillas, sin nada que revele celda, grafo ni veredicto del juez
   (decisión de la autora del 29/09/2026):
   a. planilla_mezclada reúne las fichas de C2, C3 y C4; planilla_c5 lleva
      las de C5, aparte. La pertenencia de cada ficha a su celda se escribe
      solo en adjudicacion_SOLO_MESA/. Cada celda sigue su propio protocolo
      (decisión 1): las fichas se comparten por texto idéntico solo dentro
      de un par de la misma celda, nunca entre celdas, así que la misma
      pregunta con el mismo texto de respuesta en dos celdas da dos fichas.
   b. Cada ficha muestra solo: número, id de ficha opaco (prefijo neutro
      FT0-, derivado con sal propia por planilla de la celda, la pregunta y
      el sha de la respuesta, sin que ninguno se lea en el id), TO y nombre
      del TO, ancla del gold,
      pregunta, respuesta completa y sin editar, criterios con su cita
      textual y un campo de observaciones. En los tres criterios sin cita
      de C5, en lugar de la cita, el texto «el criterio no trae cita
      textual en el gold».
   c. Nunca aparecen: celda, grafo, backend, label de corrida, rep,
      veredicto o modales del juez, fragmentos del juez, origen de la ficha
      (A o B), ids opacos del juez (prefijos T0C<n>B- y T0C<n>E- y sus
      sufijos), ids de pregunta (EV2F-, T0F-), sha256 de respuestas
      (completos o sus primeros 12 hex), sha de los grafos (0226e947,
      eab2fdd0, dd42d6d9, completos o abreviados), nombres de grafo o de
      backend (KG-, KG_, r1, desarrollo, diez, Neo4j, memoria, GraphIndex,
      fulltext) ni rutas. Los textos de pregunta, respuesta, criterio y
      cita se muestran tal cual: dentro de ellos se buscan solo los
      marcadores inequívocos (ids, sufijos, sha, labels de corrida, KG- y
      KG_), porque palabras como «desarrollo», «diez» o «memoria» pueden
      ser parte del texto de la norma o de la respuesta; el resto de la
      lista se busca en todo lo demás.
   d. En cada planilla, las fichas de A y B van mezcladas en un único orden
      aleatorio con semilla declarada; en planilla_mezclada ese orden sale
      de un solo sorteo sobre la unión de las fichas de C2, C3 y C4, nunca
      agrupado por celda.
   e. El censo ciego publica solo el número de fichas y de criterios por
      planilla. La pertenencia de cada ficha a su celda, el censo por celda
      y el censo por origen van solo a adjudicacion_SOLO_MESA/.
   f. Límites que no se corrigen y se declaran en la nota de episodios: la
      planilla de C5 se reconoce por ir aparte y por sus preguntas (los
      cinco documentos nuevos); en planilla_mezclada, una misma pregunta de
      EV2 puede aparecer más de una vez, con respuestas de celdas distintas;
      y una respuesta que cite un punto presente en un solo grafo puede
      insinuarlo.
4. Marcas: por criterio, cumplido o no_cumplido (dominio del molde,
   cierre_r1.py:83-91), volcadas en planilla_mezclada_marcas.csv y
   planilla_c5_marcas.csv, que la E5.c.1 genera vacíos con columnas
   id_ficha, indice, veredicto y observacion. El veredicto humano por ficha sale del mapping §2 en
   código (mapping.veredicto_pregunta), nunca a mano.
5. Sesión de marcado (E5.c.2): es de la autora, ficha por ficha, en el
   orden de la planilla, contra el PDF del TO y la cita del gold. Esta
   ejecutora no participa, no propone, no completa ni comenta marcas. Si
   una instancia asiste, solo presenta fichas y transcribe marcas; no tiene
   acceso a juez_out/, trazas/, adjudicacion_SOLO_MESA/ ni al código de este
   anexo, y no se usa ningún documento de veredictos propuestos
   (precedente: episodio 3 de C1). La autora no abre el código de este
   anexo ni los directorios SOLO_MESA antes de sellar sus marcas. Las
   marcas se sellan por commit de la autora antes del cierre.
6. Cierre por celda con la lógica de cierre_r1.resolver_definitivos
   (cierre_r1.py:110-159); las marcas de planilla_mezclada se reparten por
   celda con la tabla de pertenencia de adjudicacion_SOLO_MESA/. Lo no
   adjudicado conserva su final (vías
   juez_base y juez_enc); un heredado toma el veredicto humano (vía
   adjudicacion_base); un pendiente del §7 reemplaza cada voto
   requiere_adjudicacion por el veredicto humano de su ficha y re-agrega
   con agregar_par (vía adjudicacion_s7); si un par sigue en
   requiere_adjudicacion, error y FRENO.
7. E6 toma las tablas definitivas de este anexo: la tabla de celdas del
   reporte de 2a (E6 c) y la lectura de cada respuesta parcial o incorrecta
   (fila B6.0 fase 2a del plan, LECTURA DE E6, punto 3) usan los
   definitivos. La tabla pre-adjudicación queda en tabla_celdas_E5.json y
   no se reescribe.

E5.c.1 — Instrumentos y planillas en blanco. USD 0.
a. Módulos nuevos en data/experiment/ev2_tanda0/code/: planillas_tanda0.py
   (poblaciones A y B y fichas por celda; las dos planillas), selftest_nofuga_tanda0.py
   y cierre_adj_tanda0.py con selftest_cierre_adj_tanda0.py. Reusá por
   import lo que el molde tenga sin constantes de r1 (agregar_par, mapping,
   la construcción de fichas por texto idéntico); lo que tenga constantes o
   rutas de r1 se replica parametrizado por celda. No se edita nada de
   ev2_r1/, ev2_adjudicacion/, ev2_encadenamiento/ ni ev2_juez/. El gold de
   C5 se lee de preguntas_tanda0.json con su sha verificado (celdas_tanda0.py:71-73).
b. Insumos solo lectura: juez_out/C<n>/ (base, enc, orden y
   desanonimizacion_SOLO_MESA) y trazas/. Las poblaciones se verifican
   contra un recómputo propio desde los veredictos del juez con agregar_par,
   no se asumen. Totales esperados, recomputados por la mesa el 29/09/2026:
   25 pares en requiere_adjudicacion; hasta 29 respuestas objetivo en la
   población A antes de compartir fichas por texto idéntico; 14 fichas en
   la población B (una del estrato correcto y una o tres del estrato
   parcial más incorrecto por celda). Una diferencia es FRENO.
c. Escribí: data/experiment/ev2_tanda0/adjudicacion/ (planilla_mezclada y
   planilla_c5 en .json y .md, sus dos CSV de marcas vacíos y
   censo_planillas_ciego.md) y data/experiment/ev2_tanda0/adjudicacion_SOLO_MESA/
   (pertenencia de cada ficha a su celda; tabla de fichas con su origen,
   par, respuesta, veredictos y modales del juez; poblaciones; censo por
   celda y por origen).
d. Selftest no-fuga OBLIGATORIO sobre los archivos publicables, con el
   molde de selftest_nofuga_r1.py: marcadores de la decisión 3 c con su
   regla para los textos mostrados tal cual (las apariciones de palabras
   comunes dentro de esos textos se cuentan y se reportan, no fallan), sufijos
   opacos de las cuatro celdas buscados sin prefijo, ids de pregunta, sha de
   respuestas y de grafos, claves ciegas exactas por ficha y por criterio,
   consistencia de criterios contra el gold de cada pregunta, ningún campo
   de planilla_mezclada que permita separar sus fichas por celda (orden de
   un solo sorteo sobre la unión), y provocación (inyectar un marcador y un
   sufijo en una copia debe disparar la detección). Selftest del cierre con marcas sintéticas, sin tocar las
   planillas reales. Doble corrida byte-idéntica de las planillas.
FRENO E5.c.1: salida completa de los selftests; por planilla (mezclada y
C5) solo el número de fichas y de criterios; sha256 de cada archivo
escrito. NO reportes el censo por celda ni por origen, ni la pertenencia de
ninguna ficha a su celda. La autora sella las planillas en blanco y
SOLO_MESA por commit antes de marcar.

E5.c.2 — Sesión de marcado de la autora. USD 0. Esta ejecutora no actúa.
La autora completa los CSV de marcas según la decisión 5 y los sella por
commit. El «seguí» de E5.c.3 lleva el hash de ese commit.

E5.c.3 — Cierre. USD 0.
a. Verificá el sha de cada CSV de marcas contra el commit de la autora y
   su completitud: cada (id_ficha, indice) de la planilla, una sola vez,
   con veredicto en el dominio de la decisión 4. Una falta es FRENO, no se
   completa.
b. Definitivos por celda (decisión 6), con conteo de vías; tabla definitiva
   de C2, C3 y C4 al lado de la definitiva de C1 (774acac, 6/26/8) con
   intervalo de Wilson al 95 % para correcto e incorrecto; C5 en tabla
   aparte, sin cruzar con C1 a C4.
c. Tasa de error del juez desde la población B, con el molde de
   cierre_r1.evaluar_muestra (cierre_r1.py:194-224): acuerdo exacto por
   ficha, acuerdo por criterio, sobre-acreditación y sub-acreditación,
   caída de correctos; por celda y agregada para C2 a C4; C5 aparte.
d. Nota de episodios data/experiment/ev2_tanda0/adjudicacion/nota_episodios_adjudicacion_tanda0.md:
   el episodio de C5 (decisión 2), los límites de la decisión 3 f y todo
   lo que ocurra en la sesión que la autora declare.
e. Escribí reports/tanda0/tabla_celdas_definitiva_E5c.json y .md. Doble
   corrida byte-idéntica salvo el campo de fecha.
FRENO E5.c.3: tablas definitivas, vías, tasa de error del juez con sus
salvedades, sha256 de los archivos escritos. Commit de la autora antes de
E6; E6 arranca con su «seguí».

REQUISITOS TRANSVERSALES (CLAUDE.md §4 a–j), en todas las etapas.
- Escrituras: solo las rutas de E5.c.1 c, E5.c.3 d y e, los módulos nuevos
  de E5.c.1 a y tu scratchpad. Nada sellado se edita; juez_out/, trazas/,
  cache/ y las preguntas son solo lectura. No commitees.
- PYTHONDONTWRITEBYTECODE=1 y .venv/bin/python -B en todo Python. Ningún
  __pycache__ ni .pyc nuevo: línea de base al inicio y control al cierre.
- Toda afirmación con path:línea o comando; conteos recomputados antes de
  escribirse (§4 i); lo que no esté en un artefacto es NO ENCONTRADO. Los
  mentores solo por rol; cero nombres propios.
- Ninguna salida visible (reporte, stdout pegado, paquete) muestra un
  veredicto por pregunta, un id de pregunta junto a un veredicto, ni la
  pertenencia de una ficha a su celda: eso va solo a
  adjudicacion_SOLO_MESA/.
- Paquete de revisión revision_TANDA0_2A_E5c<n>/ por etapa, con
  manifest.txt; checkpoint checkpoint_TANDA0_2A_E5c.md en el scratchpad,
  actualizado al cierre de cada etapa y antes de cualquier compactación,
  con etapa, piezas hechas y rutas.

CRITERIO DE ACEPTACIÓN por etapa: el reporte corto con las salidas pedidas;
git status --short con solo las rutas de la etapa como nuevas; sha de los
sellados iguales al inicio y al cierre; selftests en verde; grep de
convenciones pegado aunque dé vacío. Criterio final: las tablas definitivas
de C2 a C5 reproducibles por comando desde las marcas selladas de la
autora, y ningún archivo publicable con información de celda, grafo o
veredicto del juez.

FRENO al final de cada etapa.
