FIRMADO por la autora el 04/10/2026

MANDATO — U-NOSEG-LIMITE: LOS 14 TOs FUERA DE LAS TANDAS (2 PARCIALES Y 12 NO SEGMENTABLES). PESO, CONTENIDO, ALTERNATIVAS Y RECOMENDACIÓN, PARA LA DECISIÓN DE LA AUTORA.
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar.
- Unidad de diagnóstico, de solo lectura, en UNA ETAPA con FRENO final. Reporte corto (no más de 40
  líneas), con lo extenso en el paquete de revisión.
- Costo de API: USD 0. Ninguna llamada a la API; Neo4j no se usa.
- No ejecuta ninguna salida. La autora no aceptó la exclusión: decide en el FRENO, con L1 a L5 a la vista.

CONTEXTO, con sus anclas (verificado el 04/10/2026, HEAD `6927ce6`).
- Dos documentos firmados en tensión. Se leen en el commit de su firma (regla k).
  - Adenda 2 al laudo B5.5 (`git show 1ae387e:docs/adenda2_laudo_B5.5_cobertura.md`, sha256
    `7baf6ee0fa4c…`, 07/09/2026): §2, la cobertura se amplía a los dos bloques excluidos; §4, el bloque A
    va antes del escalado y el bloque B queda como release posterior declarada; §3, guarda 3,
    procedencia con `granularidad_procedencia`. Registros posteriores a la firma (§6 y §7, `074a712`):
    el desacople es de calendario y no de fondo, y hay tres destinos: nueve documentos del bloque A,
    ri_spi como caso propio y el bloque B.
  - Protocolo entre tandas (`a304b89`, 03/10/2026), §5: fila «fuera, 14». No da un motivo propio: cita la
    partición (docs/plan_tesis.md:738).
- Peso sobre el universo de 152 (`b584_particion/particion_152.json`, `por_to`):

  | | TOs | páginas | unidades de la partición |
  |---|--:|--:|--:|
  | universo | 152 | 6.757 | 9.324 |
  | 2 parciales | 2 | 2.413 (35,7 %) | 46 (0,5 %) |
  | 12 no segmentables | 12 | 161 (2,4 %) | 12 (0,1 %) |
  | los 14 | 14 (9,2 %) | 2.574 (38,1 %) | 58 (0,6 %) |

  Las unidades de la partición no miden el contenido excluido: en 30 páginas de nueve no segmentables,
  U-COB-A sacó 191 unidades por página. El bloque ficha no tiene volumen medido (docs/plan_tesis.md:730).
- Los 2 parciales (`conteos_b584.json`, `roles_pagina`): manual, 2.037 páginas = 1.830 de ficha y 207 de
  cuerpo; ri2_pm, 376 = 345 y 31. De sus 46 unidades, 42 están en 16 páginas (manual 1 a 6; ri2_pm 1 a 3
  y 35 a 41) y suman 25.569 caracteres. Las otras 4 (`manual::2.3.2`, `manual::S2::cierre`,
  `ri2_pm::2.2::intro` y `ri2_pm::S5`) listan 226 páginas y 303.395 caracteres: son páginas de cuerpo
  entre fichas, pegadas al último punto abierto. `manual::S2::cierre` sola tiene 266.075 caracteres.
- Los 12 no segmentables: U-COB-A (data/experiment/cobertura_bloque_a/, `074a712`) extrajo 9, con 30
  páginas y 191 unidades `bloque_pagina` (77 de prosa, 114 de planilla), con el perfil `v3_b54`, solo E1,
  USD 0,739905. optico (43 páginas) y plandecuentas (77) son referencia pura; ri_spi (11) es caso propio.
  Ningún `kg.json` rastreado tiene nodos de esos TOs y ningún código de la cadena lee esas unidades.
- Contenido ya adjudicado (adenda 2, §1 firmado y §6 posterior a la firma): lectura a ciegas de 32
  páginas, 23 prescriptivas y 9 de referencia. Bloque A: 14 leídas, 10 prescriptivas, una por cada uno
  de diez documentos y todas de prosa. Bloque ficha: 18 leídas, 13 prescriptivas (manual 8, ri2_pm 5).
  La lista de las 32 páginas no aparece como archivo rastreado con el nombre de su unidad: NO ENCONTRADO.
- Censo de forma (`cobertura_bloque_a/censo_forma.json`): en los diez documentos con prescripción, 41
  páginas: 17 de prosa, 3 mixtas y 21 de planilla o ficha.
- El grafo de hoy no los nombra: KG-Tanda0-Diez-r2a tiene 10 TextoOrdenado, los de sus TOs; las 30
  `remite_a` de alcance `to_entero` van a ellos; 189 citas quedan irresolubles por «norma fuera del
  inventario», sin desglose por norma (`ens_diez_r2a/r2/reporte_ensamblado_r2.json`).
- B6.3 (a): 137 TOs elegibles «si se extraen todos» (docs/protocolo_entre_tandas.md:211); sin los 14, 123.
- Esquema: L-ESQ-R2 firmada (`git show 4ef7650:data/experiment/esq/enmienda_L-ESQ-R2_2026-09-30.md`) no
  menciona procedencia ni página. `Provenance` admite claves adicionales (`modelos_r2.py` en `95dfd98`,
  líneas 405 a 410).

L1. EL PESO COMPLETO, recomputado, con el comando de cada cifra.
- Documentos, páginas y unidades de los 14 sobre los 152, por clase y por TO, con el total de páginas del
  universo como denominador.
- Las páginas por rol (ficha, cuerpo, historial, índice) de cada uno de los 14.
- Las páginas de ficha dentro de TOs que sí entran (ri_laft 27 y ri_transpa 3, docs/plan_tesis.md:728).
- El volumen en unidades que traería cada alternativa, medido o declarado NO MEDIDO.

L2. LOS 2 PARCIALES CON SU PARTE POR PUNTO ADENTRO, Y ri_spi.
- Regla, escrita antes de aplicar, que separa las unidades por punto de las que cruzan fichas. Reproducir
  42 y 4, o corregirlo.
- Qué da e0-r2 sobre los dos TOs (corrida en el scratchpad, con el código del commit): ids, partición por
  tamaño de las unidades grandes, tablas, health-check.
- Qué exige: la entrada del manifiesto con el alcance declarado; qué se hace con las 4 que cruzan
  fichas; si cambia algo de E1 a E4 o del ensamblado. Costo de referencia: 42 unidades a USD 0,0202
  (`fca019d`), alrededor de USD 0,85. ESTIMACIÓN NO VERIFICADA.
- Consecuencias: el TO entra al grafo con 16 de sus 2.413 páginas; qué declara el grafo sobre el resto;
  si el TO es elegible para B6.3 y sobre qué parte; en qué tanda entra.
- Por qué el protocolo los dejó enteros afuera: los motivos que estén escritos en las fuentes, con su
  ancla, y NO ENCONTRADO para lo demás.
- ri_spi (adenda 2, §7: tiene espina y el parser de entonces no la reconocía): qué da la escalera de
  e0-r2 sobre él. Si segmenta por punto, entra por el camino normal, y en qué tanda; si no, qué
  necesita, y si eso pide una unidad propia (decisión 2).

L3. LOS 12 NO SEGMENTABLES CON SU TEXTO AL ALCANCE DEL AGENTE (diseño; sin código).
El texto por página como fuente de la herramienta de texto fuente de U-NAV-DISENO (N2, herramienta 4),
con la página como lugar citable y sin nodos nuevos.
- Qué exige:
  - el texto por página con su sha256, desde los PDF congelados;
  - cómo llega el agente a un documento que el grafo no nombra: índice de búsqueda fuera del grafo, o
    un nodo por documento, que sí cambia el grafo;
  - la forma de la cita por página y qué hacen con ella la métrica de citas y el juez;
  - cómo se reportan esas respuestas: aparte, como respondidas desde el texto y no desde el grafo;
  - qué pasa con el sistema por fragmentos, que también lee páginas.
- En qué unidad entra: el párrafo propuesto para el borrador de U-NAV-DISENO (N2, N5, N6 y N7).
- Si el grafo evaluado queda igual: en qué variantes `kg.json` no cambia un byte.
- Lo mismo para las 2.175 páginas de ficha de los parciales: volumen y costo en tokens por página leída.

L4. QUÉ CONTIENEN LAS PÁGINAS EXCLUIDAS.
- Partir de lo adjudicado: adenda 2 (§1 y §6), `censo_forma.json`, `censo_referencia.md` y las
  adjudicaciones de U-COB-A.
- Muestra declarada ANTES de leer, con semilla, estratos y tamaños. Estratos: ficha de manual; ficha de
  ri2_pm; cuerpo entre fichas (las 4 unidades que cruzan); planilla de los nueve; optico; plandecuentas;
  ri_spi. Tamaños: 20, 10, 10, 10, 3, 3 y 3 páginas (decisión 1).
- Clases, con regla escrita antes de leer: tabla de códigos; formulario o planilla; ficha de cuenta con
  criterio de imputación; prosa normativa; historial o índice; otro. Lectura asistida, con la columna
  `revision_autora` vacía. Conteos crudos por estrato.
- Preguntas plausibles de un oficial de cumplimiento que solo se responden con esas páginas: hasta 10,
  cada una con su página. El «solo» se verifica buscando sus términos en el resto del corpus; no se
  supone. No son material de evaluación.
- Cuántas citas de las normas ya extraídas apuntan a estos 14 documentos: desglose por norma de las 189
  irresolubles por «norma fuera del inventario».

L5. RECOMENDACIÓN FINAL: CÓMO Y CUÁNDO SE CUMPLE LA ADENDA 2 EN LA RELEASE r2.
La adenda 2 al laudo B5.5 está firmada (`1ae387e`). La pregunta no es si se excluye el bloque A, sino
cómo y cuándo se cumple la adenda en la release r2. La recomendación responde, con costo y calendario:
a. la parte por punto de los 2 parciales por el camino normal, y en qué tanda;
b. qué se hace con las 4 unidades que cruzan fichas, y si van con el bloque B;
c. el ingreso del bloque A con procedencia por página:
   - lo que exige en la cadena (vía de páginas en E0, re-extracción con el prefijo de la release y E3,
     ensamblado, `remite_a`, validador, suite, shapes y citas), con los archivos y las líneas leídos y
     no editados;
   - si conviene con la tanda de los regímenes informativos (protocolo, tanda 3) en lugar de antes del
     escalado, como desacople de calendario (adenda 2, §6);
d. la declaración del bloque B como release posterior, con su cifra en páginas, y si su texto queda al
   alcance del agente mientras tanto (L3).
Salidas que entran a la comparación:
1. exclusión total de los 14. Se compara declarada como lo que es: exigiría una enmienda a la adenda 2,
   con su motivo;
2. exclusión con la parte por punto de los 2 parciales adentro;
3. la 1 o la 2 con el texto al alcance del agente;
4. las unidades de prosa del bloque A adentro, antes del escalado o con la tanda 3 (decisión 3).
Para cada salida: costo; qué cambia de la cadena; si cambia el grafo evaluado; si llega antes de la
tanda 1; la cifra que declara la tesis; y si es compatible con la adenda 2 (§2 y §4) y con el protocolo
(§5), o qué documento firmado pide una nota fechada o una enmienda.

ESCRITURAS: data/experiment/no_segmentables_limite/ (se crea) y el scratchpad. Toda corrida de e0-r2,
en el scratchpad.
PROHIBIDO: editar `cobertura_bloque_a/`, la partición, E0, el ensamblado, el validador o cualquier código
de la cadena; correr extracción; leer las preguntas de EV2 o material de B6.3; commitear.

DECISIONES DE LA AUTORA (04/10/2026).
1. La muestra de L4 va con los tamaños 20, 10, 10, 10, 3, 3 y 3, y con hasta 10 preguntas.
2. ri_spi se trata en esta unidad, salvo que el diagnóstico muestre que necesita una propia.
3. La salida 4 de L5 entra a la comparación.

FRENO final: las cifras de L1, las tablas de L2 y L3, la planilla de L4 y la recomendación de L5.

REQUISITOS: los de CLAUDE.md §4 (a a l), con PYTHONDONTWRITEBYTECODE=1 y .venv/bin/python -B; todo conteo
recomputado contra su artefacto; toda afirmación con su ancla o NO ENCONTRADO; copias para verificar
armadas copiando archivos; cero nombres de personas.
