# U-UNION-ESTRECHA, U1 — la regla estrecha de unión ítem–encabezado

Mandato: `docs/mandatos/UUNION_ITEM_ENCABEZADO_regla_estrecha.md`, leído en su commit de firma (`21e55a0`; versión
para firmar en `9e84741`). Texto sellado antes de toda medición: sha256 y hora en `sello_regla_u1.txt`, junto con los
del código que la implementa y la mide (`regla_u1.py`, `premedicion_u1.py`, `selftest_regla_u1.py`,
`comandos_u1.sh`). Estado: **PENDIENTE de aprobación de la autora** (FRENO U1). Si la autora cambia algo, la versión
aprobada se sella de nuevo antes de U2.

La regla une la Condicion de un ítem de lista que quedó sin `condicion_de` con la norma del bloque que abre esa
lista, solo cuando ese bloque anuncia condiciones o requisitos y la norma es única y compatible con el anuncio.
Todo término de código remite a `regla_u1.py`.

## 1. A qué nodos se aplica

Un nodo X entra a la regla si cumple las cuatro condiciones:
1. X es de tipo **Condicion**. La Excepcion queda fuera como nodo del ítem (decisión 1 de la autora al firmar).
2. X no tiene ninguna arista `condicion_de` saliente en el grafo.
3. El chunk de E0 de su procedencia principal (`provenance.chunk_id`; una parte `::parteK` cae en su unidad
   entera) no es un mini-chunk (`comun_e1.es_mini_chunk`).
4. Ese chunk es un ítem de lista: `prompt_r2b.bloque_lista` da el índice del bloque heredado que abre la lista
   (el último bloque que no es de cierre y termina en «:», seguido solo de cierres). Las dos funciones se usan tal
   como están en el código del extractor, sin reescribirlas.

## 2. El anuncio del bloque que abre la lista

Sobre el texto del bloque (palabras cortadas en fin de línea unidas, espacios colapsados):
- **F, la oración final**: lo que sigue a la última frontera de oración antes del «:» final. Frontera: «.», «;» o
  «:» seguidos de espacio y de mayúscula, comilla, paréntesis o «¿», salvo detrás de «Com», «Art», «Inc», «Pto»
  y «Nro».
- **G, el tramo que rige la lista**: lo que sigue a la última coma de F (F entera si no tiene coma).
- La búsqueda es en minúsculas y sin diacríticos.

El bloque anuncia condiciones o requisitos en una de dos formas:

**Forma S (subordinante).** Hay en G un subordinante de esta lista cerrada:

| subordinante | fuente (bloque que abre lista, diez TOs de la tanda 0) |
|---|---|
| «siempre que» | cla::2.2.4, cap::2.2.3, cap::3.1.4, ext::5.12 |
| «en la medida que» | ext::2.6.1, ext::2.7, ext::3.4, ext::3.8, ext::5.8.2, ext::8.5.14, ext::10.4.2, ext::13.1 (24 bloques, todos de ext) |
| «cuando» | ext::2.6.2, ext::3.3.3, ext::4.8.4, ext::7.6.3, ext::8.5.3, ctacte::6.2, ctacte::6.3, lingob::2.2 |
| «cada vez que» | cla::6.4 |
| «toda vez que» | pagjub::2.7 |

y además se da una de estas dos:
- **S1**: G termina en «las/los siguientes» + uno de: condiciones, requisitos, recaudos, situaciones,
  circunstancias, motivos. Fuentes de los tres últimos: «alguna de las siguientes situaciones» (ext::3.3.3,
  ext::7.6.3, lingob::2.2), «alguna de las siguientes circunstancias» (cla::6.4), «uno de los siguientes motivos»
  (pagjub::2.7). «recaudos» aparece solo en la forma N (pro::4.2.1); lo incluyo en S1 porque un nombre que anuncia
  sin subordinante también anuncia con él.
- **S2**: el subordinante no abre F (antes de él, en F, hay al menos una letra): la cláusula principal va antes y
  la lista completa la condición. Fuentes: ext::5.12 «… podrán realizar operaciones de arbitrajes y canjes en el
  exterior siempre que la contraparte sea:», ext::8.5.14 «… en la medida que la entidad cuente con la documentación
  debidamente certificada que acredite:», ctacte::6.3 «Deberá rechazarse la registración de los cheques de pago
  diferido presentados a registro cuando:».
  El subordinante que abre F sin un nombre de S1 no anuncia: en ext::10.3.1 («En la medida que corresponda a
  operaciones que cuenten con el registro de ingreso aduanero quedan comprendidos:») la lista es de la principal.

**Forma N (nombre, sin subordinante en G).** G termina en:
- «las/los siguientes» + uno de: condiciones, requisitos, recaudos. Fuentes: «en las siguientes condiciones»
  (ext::3.11.1, ext::3.11.2, ext::3.11.3), «estarán sujetas a las siguientes condiciones» (polcre::6.1.1,
  polcre::6.2.1), «deberá verificar los siguientes requisitos» (ext::4.6.2), «deberán cumplir los siguientes
  requisitos» (ctacte::12.10.1), «una presentación que cumpla los siguientes recaudos» (pro::4.2.1);
- o una de estas dos frases: «las condiciones especificadas a continuación» (ext::3.3), «las condiciones
  estipuladas en cada caso» (ext::3.4.4, ext::3.5.3, ext::3.6.4).

**Sin anuncio**: todo lo demás. Entre los casos que la regla deja fuera a sabiendas:
- un subordinante antes de una coma de inciso: ext::10.10.2 («cuando, en adición a los restantes requisitos
  aplicables, se verifique alguna de las siguientes situaciones:»), ext::13.3 («cuando adicionalmente a los restantes
  requisitos normativo, se verifique el encuadre en alguna de las siguientes situaciones:»), ext::10.11 y ext::13.4
  («excepto cuando, adicionalmente a los restantes requisitos aplicables, la entidad verifique que:»);
- situaciones, casos o circunstancias sin subordinante: ext::14.2 («podrán también dar acceso en las siguientes
  situaciones:»), ext::3.5.1 («este requisito se considerará cumplimentado en los siguientes casos:»), ext::7.5
  («… en las siguientes circunstancias:»);
- la condición en un inciso que precede a la principal: ctacte::3.2 («El título respecto del que se presentare
  alguna de las siguientes situaciones, enumeradas taxativamente a continuación, no valdrá como cheque:»).

Expresiones consideradas y no incluidas:
- «en tanto»: no abre ninguna lista de los diez TOs como subordinante; su única aparición en un bloque que abre
  lista es «en tanto por ciento» (ctacte::2.3.5). Como condicional está en textos propios (cla::6.5.4.7 «en tanto
  no hubiere sido declarada», cap::3.2.3 «en tanto se reúnan las condiciones»); si la autora la agrega, va con la
  guarda «no seguida de "por ciento" ni de "por uno"» (cap::2.1, cap::4.2.4 «en tanto por uno»).
- «si»: en un bloque que abre lista es «de si» (lingob::7.1 «dependiendo también de si la entidad cotiza o no en
  bolsas:»), que no anuncia condiciones.
- «en la medida en que»: sin fuente en un bloque que abre lista de los diez TOs; está en el texto propio de 40
  chunks (pro::2.2.2, cla::3.6, entre otros). Es variante de «en la medida que»: si la autora la agrega, entra a la
  forma S.
- «a condición de que»: sin fuente en los bloques que abren lista de los diez TOs.

La lista es cerrada: en las otras tandas, una expresión que no está acá no anuncia. Eso puede perder uniones (límite
de alcance), pero no agrega ninguna.

## 3. Los candidatos

- **H, el mini-chunk del encabezado**: el mini-chunk de E0 del mismo TO, con `unidad` igual a la `unidad_origen` del
  bloque, `rol_bloque` igual a su `tipo`, y cuyo texto contiene el del bloque (las dos normalizadas como en la
  referencia). Si el bloque es la línea de título (`tipo` «encabezado») no hay H. Si hay cero o más de un
  mini-chunk que cumple eso, la corrida se detiene con error (como el `assert` de la referencia).
- **Nodos de H**: los nodos del grafo con alguna procedencia (`provenances`, o `provenance` si no hay lista) en H o
  en una parte `H::parteK`.
- **Candidatos**: los nodos de H cuyo tipo está en el rango de `condicion_de` de la matriz r2
  (`modelos_r2.FIRMAS_R2`: Excepcion, Obligacion, Restriccion, Operacion, Potestad). Cuentan **todos los tipos del
  rango**, también los que no son compatibles con el anuncio (punto 4): si el encabezado extrajo dos normas, el texto
  solo no dice de cuál son las condiciones, y la regla no elige.

## 4. Compatibilidad del destino con el anuncio

| anuncio | tipos destino compatibles |
|---|---|
| F con marca de excepción (cualquier forma) | Excepcion |
| forma S | Potestad, Operacion, Obligacion, Excepcion |
| forma N | Potestad, Operacion, Excepcion |

**Restriccion no es compatible con ningún anuncio**, aunque la matriz la admita: bajo una prohibición, las
condiciones que se listan son las de la excepción que la levanta (ext::3.5.3: «… requerirá la conformidad previa
del BCRA excepto que el deudor encuadre en alguna de las siguientes situaciones y se cumplan la totalidad de las
condiciones estipuladas en cada caso:»; igual en ext::3.6.4), y unirlas a la Restriccion invertiría el sentido. La única lista de
los diez TOs donde las situaciones disparan la prohibición (ctacte::3.2) queda sin anuncio en esta regla.

**Marca de excepción en F** (lista cerrada). En bloques que abren lista: «excepto» (ext::3.5.3, ext::3.6.4), «no
resultará aplicable» (ext::3.3.3, ext::3.5.4, ext::3.5.6), «quedarán exceptuados» (ext::2.6.1, ext::7.8.4), «con
excepción de» (cla::5.1.1), «salvo» (ext::8.2). En el texto propio de los diez TOs: «a menos que» (cap::3.1.2.2),
«no será aplicable» (ext::5.14), «no será de aplicación» (cap::2.4), «se exceptúa» (cla::6.5.5.7), «quedan
exceptuados» (ext::12.1). Con la marca, las condiciones anunciadas son las de la excepción, no las de la
obligación o la prohibición de la misma oración: ext::3.5.4 «este requisito no resultará aplicable cuando se cumpla
la totalidad de las siguientes condiciones:», ext::7.8.4 «Quedarán exceptuados de la obligación de liquidación … y
se cumplan la totalidad de las siguientes condiciones:».

**Forma N sin Obligacion**: sin subordinante, la lista de condiciones o requisitos puede ser el objeto de la
obligación, lo que se verifica o se cumple, y no la circunstancia en que la obligación rige: ext::4.6.1 «deberá
verificar el cumplimiento de los siguientes requisitos», ext::7.5.5 «deberá verificar el cumplimiento de las
siguientes condiciones», ext::11.1.6 «se deberán verificar las siguientes condiciones», ext::3.3 «deberán verificar
que se cumplan las condiciones especificadas a continuación», ctacte::12.10.1 «deberán cumplir los siguientes
requisitos». En la forma S el subordinante pone la lista como condición de la principal, sea cual sea su tipo:
ctacte::6.3 (Obligacion: «Deberá rechazarse la registración … cuando:»), ext::13.1 (Potestad: «Las entidades podrán
dar acceso … en la medida que se cumplan las siguientes condiciones:»).

**Excepcion como destino**: sí (propuesta del mandato). La decisión 1 de la autora deja fuera a la Excepcion como
nodo del ítem; como destino, la Condicion del ítem puede ser condición de la excepción que abre la lista
(ext::3.5.4).

## 5. La decisión, en este orden

1. El bloque es la línea de título (no hay H): `sin_unidad_de_encabezado`.
2. El bloque no anuncia (punto 2): `sin_anuncio`.
3. Ningún candidato: `sin_candidato`.
4. Dos o más candidatos: `ambigua`.
5. Un candidato de tipo no compatible (punto 4): `destino_no_compatible`.
6. Un candidato compatible: `union`.

Solo el resultado 6 agrega una arista. Todos los demás quedan en el registro, sin unión.

## 6. La arista derivada y el registro

- Arista: `source` = X, `target` = el candidato, `relation` = `condicion_de`, `rol_fuente` =
  `union_item_encabezado`, `provenance` y `provenances` = la procedencia principal de X (la del ítem). Sin las marcas
  de E3 ni de una relación emitida por E1 (`no_verificada_e3`, `coherencia_tipo_predicado`, `properties`,
  `properties_no_definidas`), como la `establecida_en` derivada de la procedencia: E3 no la vio.
- Registro: una fila por cada nodo del punto 1, con el bloque (`TO::unidad[tipo]`), H, los candidatos con su tipo,
  el resultado y el destino; y, por bloque, la forma del anuncio, el subordinante, la marca de excepción, los
  compatibles y G.

## 7. Diferencias con la regla E del diagnóstico (implementación de referencia)

Referencia leída como código, sin sus veredictos: `reports/u_diag_cap3_grafo/scripts/udiag_a_union.py`
(`mini_de_bloque`, `medir`). Igual que ella: el ítem por `bloque_lista` sobre la procedencia principal, H como
mini-chunk con la misma unidad, rol y texto, nodos de H por cualquier procedencia, «un candidato» como condición de
unión, `rol_fuente = union_item_encabezado`. Distinto:
- solo Condicion (la regla E también unía la Excepcion);
- exige el anuncio del punto 2 (la regla E no miraba el texto del bloque);
- cuenta como candidatos todo el rango de `condicion_de` y después exige compatibilidad (la regla E contaba solo
  los tipos de su destino, que para la Condicion eran los cinco, y no exigía compatibilidad);
- cuenta también la procedencia en una parte `H::parteK` (la regla E miraba solo H).

## 8. Cómo la fijé (antes de sellar)

Leí el mandato firmado, la regla E como código y el código de `bloque_lista`, `es_mini_chunk` y la matriz r2. Para
las listas cerradas leí el texto de los 220 bloques que abren lista en los chunks de E0 r2b de los diez TOs (1.053
ítems), y verifiqué las fuentes citadas aplicando `anuncio` a esos 220 bloques (la forma de cada bloque, sin ítems
ni nodos). Para precisar los candidatos miré, en los 69 bloques que abren la lista de alguna Condicion de ítem sin
`condicion_de` en `a9631a64`, cuántas son y los tipos de los nodos de su mini-chunk (conteos). No leí el texto de
ningún ítem ni de ningún nodo, no conté las uniones de esta regla y no abrí ningún veredicto
(`reports/u_diag_cap3_grafo/lecturas/`). La pre-medición corre después del sello.

## 9. Implementación y selftest

`regla_u1.py`: la regla como funciones puras (`anuncio`, `compatibles`, `decidir`, `aplicar`). `selftest_regla_u1.py`:
casos sintéticos por rama (formas S1, S2 y N, sin anuncio, marca de excepción, palabra cortada, frontera de oración
y abreviatura; cada resultado de la decisión; un grafo sintético de punta a punta, con parte de mini-chunk y error por
dos mini-chunks). `premedicion_u1.py`: la pre-medición sobre `a9631a64` y `e22fae1a`.

## 10. Lo que aprueba la autora (FRENO U1)

El texto de la regla. En particular:
1. las listas cerradas del punto 2 (subordinantes, nombres y frases) y que «en tanto» y «en la medida en que» queden
   fuera;
2. la compatibilidad del punto 4: Restriccion fuera; Obligacion fuera en la forma N; con marca de excepción, solo
   Excepcion;
3. la Excepcion como destino;
4. contar todo el rango de `condicion_de` para «único candidato» (punto 3).
