BORRADOR — PENDIENTE DE FIRMA

MANDATO — U-NOSEG-LIMITE: LOS NO SEGMENTABLES QUEDAN FUERA DEL GRAFO EVALUADO, COMO LÍMITE CON SU CIFRA; SU INGRESO SE ESPECIFICA PARA LA VERSIÓN POSTERIOR A LA EVALUACIÓN.
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar.
- Unidad chica, de solo lectura sobre lo existente, en UNA ETAPA con FRENO final. Reporte corto (no más de
  40 líneas) y espera de la revisión.
- Costo de API: USD 0. Ninguna llamada a la API; Neo4j no se usa.
- Opción que ejecuta, si la autora la firma: la (c) con la declaración de la (b). El grafo que se evalúa
  en B6.3 no incluye a los no segmentables ni a los parciales; el ingreso de las unidades de prosa del
  bloque A va a la versión del recurso posterior a la evaluación, con mandato propio.

CONTEXTO, con sus anclas (verificado el 03/10/2026).
- Cuántos son (data/experiment/segmentacion_84/b584_particion/particion_152.json, `agregados`; y
  `adjudicaciones_b584.json`, `e_no_segmentables`): 12 no segmentables, 161 páginas y 12 unidades en la
  partición; 2 parciales (`manual` y `ri2_pm`), 2.413 páginas y 46 unidades.
- De los 12, U-COB-A (data/experiment/cobertura_bloque_a/, `074a712`) extrajo 9, con 30 páginas:
  `chunks_a2.json` tiene 191 unidades de tipo `bloque_pagina` (ri_con 116, ri_tii 36, ri_rem 12, ri_itme
  11, ri_pspii 5, ri_chr 4, ri_fcem 4, ri_pfmipyme 2 y ri_pscpp 1), 77 de prosa y 114 de planilla o ficha.
  Los otros 3: optico (43 páginas) y plandecuentas (77), declarados referencia pura, y ri_spi (11), caso
  propio (docs/plan_tesis.md:729).
- Con qué se extrajeron (`a2_salida/resumen_corrida_a2.json`): perfil `v3_b54`, prefijo `54a111e2175f`,
  claude-haiku-4-5, solo E1, 191 llamadas, USD 0,739905 de tope 4. Sin E3, sin E2 y sin E4.
- Procedencia: cada unidad lleva `granularidad_procedencia: "pagina"` y `paginas` en `chunks_a2.json` y en
  `extracciones_a2.jsonl`. La procedencia de sus 363 entidades tiene solo `to`, `archivo`, `punto` (con
  la forma `pN.bM`) y `rol_documental`.
- Nada de eso llega a un grafo: ningún `.py` rastreado fuera de `cobertura_bloque_a/` menciona
  `granularidad_procedencia`, `chunks_a2`, `bloque_pagina` ni `extracciones_a2`; ninguno de los 17
  `kg.json` rastreados tiene nodos de esos TOs; la procedencia de KG-Tanda0-Diez-r2a lleva `paginas` y
  `chunk_id` y no tiene campo de granularidad.
- Decisión vigente sobre el bloque A (07/09/2026; `cifras_vigentes.md`; checklist P8): las 77 unidades de
  prosa entran al recurso con granularidad de página, y el ingreso es acto del ensamblado de la tanda. No
  se hizo. Las 114 de planilla quedan afuera. Si sus TOs entran, se retiran tres `aplica_a`
  (docs/plan_tesis.md:767; checklist P12).
- Protocolo entre tandas, firmado (`a304b89`), §5: los 14 quedan fuera de las tandas 1 a 3. Las dos
  decisiones están en tensión: esta unidad deja escrito cuál rige y desde cuándo.
- B6.3 (a): el protocolo cuenta 157 − 20 excluidos = 137 TOs elegibles «si se extraen todos»
  (docs/protocolo_entre_tandas.md:211). Ninguno de los 14 está entre los 10 de
  data/experiment/esq/documentos_excluidos_esq.json, ni entre los diez de la tanda 0. Sin ellos, el
  conjunto con contenido en el grafo baja a 123.
- Esquema: el texto firmado de L-ESQ-R2 (`git show 4ef7650:data/experiment/esq/enmienda_L-ESQ-R2_2026-09-30.md`,
  sha256 `66c4a1b9c5ed…`) no menciona procedencia ni página. La página como lugar citable no cambia tipos
  ni relaciones: cambia la procedencia. `Provenance` admite claves adicionales
  (`git show 95dfd98:data/experiment/pyd_r2/code/modelos_r2.py`, líneas 405 a 410).

L1. LA CIFRA DEL LÍMITE, recomputada contra los archivos, con el comando de cada una:
- los 14 TOs con su clase, sus páginas y sus unidades; las páginas sobre el total de los 152 y de los 157;
- de los 12, cuáles tienen contenido prescriptivo según la adjudicación de U-COB-A, y cuántas unidades
  de prosa y de planilla por TO;
- el conjunto elegible de B6.3 (a) con y sin los 14, contra `documentos_excluidos_esq.json` y los
  manifiestos de las tandas.

L2. LOS TEXTOS, como propuesta para que la revisión los asiente:
- la declaración del límite para la tesis: qué queda fuera del grafo evaluado, cuánto es y por qué;
- el requisito para el pre-registro de B6.3: ninguna pregunta ancla en los 14 TOs, con el comando que lo
  verifica;
- la nota de vigencia: el ingreso de las 77 unidades de prosa pasa a la versión posterior a la
  evaluación; P12 sigue condicionado a ese ingreso.

L3. LA ESPECIFICACIÓN DEL INGRESO POSTERIOR, sin implementarlo. Qué exige y cuánto cuesta:
- E0: una vía de páginas en el formato de e0-r2 (hoy las unidades salen del código de U-COB-A);
- extracción con el prefijo de la release y con E3, que nunca corrió sobre bloques de página ni sobre
  planillas. Referencia de costo: USD 0,0202 por unidad de E1 a E3 (censo de P1 de U-PROMPT-R2,
  `fca019d`): alrededor de USD 1,6 por las 77 de prosa y de USD 3,9 por las 191. ESTIMACIÓN NO VERIFICADA:
  los bloques de página son más cortos que la unidad media;
- ensamblado: la procedencia con su granularidad y el retiro de las tres `aplica_a`;
- `remite_a`: una unidad de página puede ser origen de una cita y no puede ser destino por punto;
- validador, suite y shapes: los ítems que suponen que `punto` resuelve a una unidad por punto;
- citas del agente y métrica de citas, que hoy trabajan por punto.
Cada renglón, con los archivos y las líneas que habría que cambiar, leídos y no editados.

ESCRITURAS: data/experiment/no_segmentables_limite/ (se crea) y el scratchpad.
PROHIBIDO: editar `cobertura_bloque_a/`, la partición, el ensamblado, el validador o cualquier código de
la cadena; correr extracción; commitear.

DECISIONES DE LA AUTORA AL FIRMAR.
1. La opción: (a) integrarlos antes de la tanda 1; (b) declararlos fuera, como límite; (c) dejarlos para
   la versión posterior a la evaluación. Este borrador ejecuta la (c) con la declaración de la (b).
2. Si la decisión del 07/09/2026 sobre las 77 unidades se mantiene con fecha nueva, como propone L2, o
   se revoca.
3. Si ri_spi y los 2 parciales (U-COB-B, sin empezar) entran en la misma declaración.

FRENO final: reporte con las cifras de L1, los textos de L2 y la tabla de L3.

REQUISITOS: los de CLAUDE.md §4 (a a l), con PYTHONDONTWRITEBYTECODE=1 y .venv/bin/python -B; todo conteo
recomputado contra su artefacto; toda afirmación con su ancla o NO ENCONTRADO; cero nombres de personas.
