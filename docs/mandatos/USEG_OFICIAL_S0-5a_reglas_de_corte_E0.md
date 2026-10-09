# Mandato de S0-5a de U-SEG-OFICIAL: reglas de corte de E0 antes de la tanda 1

**LISTO PARA DESPACHAR (mesa, 09/10/2026; corregido el mismo día con la revisión de la autora). Despacho PENDIENTE de la autora.** Etapa del mandato FIRMADO de U-SEG-OFICIAL
(`docs/mandatos/USEG_OFICIAL_segmentacion_e0r2.md`, `e543cb2`), por la decisión de la autora del 09/10/2026: el código de E0 cambia una
vez más antes de la tanda 1 (nota al pie del mandato del 09/10/2026). Para la sesión de S0-4 y S1-bis. USD 0, sin API. **Este archivo
nombra unidades con error de corte: ninguna lectura a ciegas lo abre.**

## 0. De dónde sale

- **La lectura de cortes de S1-bis, adjudicada por la autora:**
  - acta `s1bis/lectura_cortes/acta_adjudicacion_S1bis.md`, sellada en `sello_adjudicacion_S1bis.txt`;
  - las 41 marcas de la mesa, confirmadas: 16 errores y 25 correctas;
  - el piso no se cumple: 85 de 90 sin error de corte, Wilson 0,8765;
  - el censo del hallazgo 1.16 da 8 de 35 en la tanda 1.
- **Los errores de corte y su mecanismo** (evidencia de la mesa del 09/10/2026, con los scripts en su paquete):
  1. **El cierre de una lista absorbido por el último ítem (1.16).** Casos:
     - `adfsp::1.1.10`, `cajasc::11.4.4`, `cajasc::4.2.2.3`, `depaho::3.11.5.5`, `manori::1.4.1.3`, `manori::3.4.1.3` y
       `ri_oc::B.1.28`;
     - sin leer, `ri_oc::B.2.4` y `ri_oc::B.3.4`: su cierre está en el texto propio del ítem, porque el detector de S1-bis no lo vio
       (§2.6).
  2. **El título de un bloque siguiente absorbido por el último ítem.** `ri_oc::C.11` termina con «Criterios de validación» y «Validación
     del Apartado A – Operaciones de cambios», los títulos del bloque de validaciones de las pp. 19-21. El cuerpo de ese bloque es hoy
     `ri_oc::SC::cierre` (5.313 caracteres), que heredan C.1 a C.11. Es el límite declarado (d) de S0-4a-ter: el FRENO de S0-4a-ter,
     `:31`, y el de S0-4b, `:36`.
  3. **Bloques intersticiales partidos.**
     - `snp_dd::S7::intersticial::13` y `::14`: la fila R95 de la tabla de códigos.
     - `::7`, `::8` y `::9`: la fila R02.
     - `::17` y `::18`: el rótulo de un campo y su descripción.
  4. **Título de sección de dos renglones,** cuyo segundo renglón queda como chapeau. `ri2_ae::S2::chapeau_seccion` es solo
     «de Auditores":», y los de ri_spi, `SB` y `SC`, son el segundo renglón del título.
  5. **Una remisión al principio de un renglón leída como encabezado.** `ri_rml::1.2.3` se corta en «…descripto en el punto» y el
     renglón que sigue, «1.3. “Integración” de las presentes normas…», abre una unidad fantasma, `ri_rml::1.3` (pp. 6-10, 12.345
     caracteres). Esa unidad se lleva esos dos renglones, el punto 1.2.4 entero (no existe `ri_rml::1.2.4`) y el 1.3 verdadero
     («1.3. Integración del período»).

     Lo mismo en `snp_tr` (tanda 1). El renglón «1.6. “Transacciones” y 1.7. “Diseño de registros”.», que sigue a «…definidos en los
     puntos», es hoy el encabezado del 1.6, y `snp_tr::1.3.3` queda cortada. `snp_tr::1.6::intro` (pp. 11-18, 14.563 caracteres) se
     lleva los puntos 1.4 a 1.4.4, 1.5 a 1.5.2.2 y el encabezado del 1.6 verdadero («1.6. Transacciones.»).
  6. **Las letras de un rótulo vertical.** La «C» al final de `ri_ccna::D1F3::S0` es la primera letra del rótulo vertical «CODIGO» del
     formulario siguiente; las otras letras quedan intercaladas en `ri_ccna::D1F4::S0`. Es corte, no limpieza (decisión de la autora).

## 1. Escrituras y prohibiciones

- **Escrituras:**
  - `data/experiment/segmentacion_oficial_e0r2/s0_5/` (se crea);
  - el scratchpad;
  - el código de E0, solo en una copia: el parche se aplica al repo en S0-5b, una sola vez, después de la revisión.
- **PROHIBIDO:**
  - la API;
  - el repo fuera de `s0_5/`;
  - la salida sellada de la tanda 0;
  - las planillas, el acta y la población del censo ya leído de S1-bis;
  - cambiar el criterio de la lectura de cortes;
  - commitear.
- **Reglas:** CLAUDE.md §4 (a a l).

## 2. Las reglas

Cada regla lleva su interruptor, su caso positivo y sus casos negativos en `selftest_e0`, y vale solo dentro de su alcance. Para cada una,
el FRENO trae el censo de las unidades que cambian en los 152, por TO, con el antes y el después.

**R5-a `cierre_al_margen` (mecanismo 1).**
- **Alcance:** las listas que marca el detector corregido del §2.6.
- **La regla:** después del último ítem, cada párrafo cuyo primer renglón está más cerca de la columna de los rótulos de los ítems que de
  la del texto del ítem pasa al cierre del padre (`<padre>::cierre`). Se evalúa **cada párrafo**, no solo el primero: en
  `cajasc::4.2.2.3` el párrafo al margen es el segundo. Usa las coordenadas de `e0_lib.extraer_lineas`.
- **Tolerancia de columna:**
  - se fija antes de correr el censo;
  - es una sola para los 152;
  - va en el FRENO;
  - no se ajusta después.
- **Evidencia de la mesa:** con las columnas de `pdftotext -layout`, la regla coincide con la lectura en 33 de los 35 candidatos de la
  tanda 1. Los dos que no:
  - `cajasc::4.2.2.3`, que entra si se evalúa cada párrafo;
  - `ri_rml::1.2.3`, que es el mecanismo 5.
- **Aceptación:**
  - los 9 casos del mecanismo 1 quedan con el cierre fuera del ítem;
  - **ninguno de los 27 candidatos marcados correctos cambia**.

**R5-a′ `titulo_de_bloque` (mecanismo 2).**
- **La regla:** si lo que sigue al último ítem empieza con un renglón con forma de título de bloque (corto, sin puntuación final y seguido
  de cuerpo), no va al cierre del padre: abre una unidad nueva con el bloque que encabeza, hasta el próximo encabezado de igual o mayor
  nivel.
- **Alcance:**
  - **Por lista, ri_oc** (tanda 1): el bloque de validaciones de las pp. 19-21 pasa a ser una unidad propia, con sus dos títulos, y ya no
    lo heredan C.1 a C.11. El límite declarado (d) de S0-4a-ter deja de serlo para ri_oc, y se declara.
  - **El resto** (decisión 3 de la autora, 09/10/2026). La mesa encontró 27 candidatos con un renglón así después del primer párrafo
    del último ítem (heurística, con falsos positivos, como filas de tabla o fórmulas).
    - S0-5a los lista con su página y su lectura: si el renglón es el título de un bloque y adónde iría con la regla.
    - S0-5a no aplica R5-a′ fuera de ri_oc.
    - Cuáles entran por lista lo decide la autora en la revisión del FRENO de S0-5a, y se aplican en S0-5b.
- **Aceptación:**
  - el FRENO muestra adónde va cada renglón de `ri_oc::C.11` y del bloque de validaciones, y no quedan como cierre de C;
  - **C.1 a C.11 ya no heredan el bloque de validaciones:** ninguna de sus herencias tiene tramos de ese bloque.

**R5-b `intersticial_continuado` (mecanismo 3).**
- **Alcance:** por lista, snp_dd y snp_cheq; son los dos únicos TOs con unidades intersticiales, 110 en los 152. snp_cheq está en la
  tanda 1.
- **Cómo están hoy** (texto propio en la salida de S0-4b; el FRENO lo muestra igual):
  - `snp_dd::S7::intersticial::13`: «R95 Reversión de En- Este código podrá ser utilizado por el banco originante en caso que la entidad
    receptora presente una». Es un solo renglón con las tres columnas de la fila: el «En-» está a mitad del renglón, en la columna de la
    descripción, y la unidad termina en «presente una».
  - `::14`: «tidad receptora reversión de banco receptor fuera del término» / «presentada fuera» / «de término».

  Por eso la versión anterior de la condición, la palabra partida al final de la primera unidad, no los unía.
- **La regla:** dos intersticiales consecutivas de la misma página se unen si se cumple alguna de estas condiciones, y las uniones se
  encadenan:
  - (i) la segunda empieza con minúscula y la primera no termina en «.», «:» ni «;», porque continúa una celda o una oración;
  - (i′) la segunda es solo un código de la tabla (una letra y dos dígitos, como «R02») y la primera no termina en «.», «:» ni «;»;
  - (ii) la primera es un solo renglón de rótulo numerado («N. Texto.») y la segunda no empieza con otro rótulo numerado.
- **Evidencia de la mesa** (censo de los pares sobre las 110 intersticiales; `r5b_pares_mesa.py`, en el paquete de la mesa):
  - (i) une 13+14 y 8+9;
  - (i′) une 7+8, la fila R02 de la p. 45 («Cuenta cerrada… recae la transacción» / «R02» / «se encuentre cerrada o suspendida.»); con
    (i), queda 7+8+9;
  - (ii) une 19 pares de rótulo y descripción: 15 en snp_dd, 17+18 entre ellos, y 4 en snp_cheq;
  - no une ningún otro par.
- **Declarado:** esas filas (pp. 45 y 49) son de la tabla de códigos que `e0_tablas` no detectó; las de las pp. 46 a 49 sí quedaron como
  tabla. R5-b las deja en una unidad por fila, no como tabla serializada.
- **Aceptación:**
  - quedan unidas 13+14, 7+8+9 y los 19 pares de rótulo y descripción;
  - la lista de uniones del FRENO es la del censo de la mesa, o cada diferencia, explicada;
  - ninguna otra intersticial se une.

**R5-c `titulo_seccion_envuelto` (mecanismo 4), corregida.**
- **La regla:** el chapeau de un solo renglón es la continuación del título si se da al menos una de estas condiciones:
  - (a) el título termina en una palabra partida con guion;
  - (b) el título termina en una palabra funcional (artículo, preposición o conjunción);
  - (c) el título deja abierta una comilla o un paréntesis;
  - (d) el chapeau empieza con minúscula.

  No une un chapeau que es una oración completa con mayúscula inicial después de un título completo.
- **Evidencia de la mesa** (censo de los chapeaux de un renglón con encabezado sin puntuación final): 13 candidatos.
  - **9 son títulos de dos renglones:**
    - `manual::S2`, `ri2_ae::S2`;
    - en ri_ccna, `D1A1::S2`, `D1A3L2::S26`, `D1A3L2::S29`, `D1F2::S3` y `D1F6::S3`;
    - en ri_spi, `SB` y `SC`.
  - **4 son chapeaux de verdad:** `inspag::S3`, `pfmipyme::S3`, `ri_cr::S3` y `snp_psp::S3`.
  - La versión anterior de la regla (el chapeau cierra una comilla o un paréntesis, o termina en «:») unía bien 6, dejaba afuera 3 (`manual::S2`
    y los dos de ri_spi) y unía mal 3 chapeaux de verdad.
  - Las condiciones (a) a (d) cubren los 9 y no tocan los 4.
  - El censo no ve los títulos cuyo segundo renglón quedó en otra parte, que no sea un chapeau de un renglón: se declara.
- **Aceptación:**
  - los 9 títulos quedan enteros en la herencia y sin chapeau;
  - los 4 chapeaux de verdad no cambian;
  - el título de C de ri_spi queda entero. Es la condición de la reclasificación de ri_spi como reconocido pleno (decisión de la autora,
    punto 5).

**R5-d `numero_en_referencia` (mecanismo 5), con guarda de columna.**
- **La regla:** un renglón que empieza con un número de punto no es encabezado si se cumplen las dos condiciones:
  - el renglón anterior termina en una palabra de referencia («punto», «puntos», «sección», «capítulo», «apartado», «inciso», «numeral»,
    «anexo», «artículo», «ley», «comunicación», «nº», o un artículo o una preposición), y no en una conjunción («y», «o»);
  - el renglón empieza en la columna del cuerpo del texto, no en la de los rótulos de sus hermanos, y sin huecos de columna
    (`ngaps` = 0).
- **Evidencia de la mesa** (censo sobre los renglones de los 152): 263 renglones empiezan con un número de punto después de un renglón que
  termina en una palabra de referencia, y E0 tomó 66 como encabezado.
  - 41 de esos 66 siguen a «y» u «o»: son enumeraciones de verdad.
  - 19 son filas de tabla, con `ngaps` mayor que 0.
  - Quedan 6, leídos en su página:
    - remisiones: `ri_rml` p. 6 («…el punto» / «1.3. “Integración”…») y `snp_tr` p. 11 («…los puntos» / «1.6. “Transacciones” y
      1.7. …»);
    - encabezados de verdad: `gerc` p. 19 (2.4.2), `rdbcra` p. 41 (11.12), `ordcom` p. 7 (1.6.2) y `pimf` p. 2 (4.18).
  - La regla como estaba escrita (solo «punto» o «puntos», sin guarda) suprimía también gerc 2.4.2 y rdbcra 11.12, que son
    encabezados. Con la guarda de columna, suprime solo las dos remisiones.
- **Aceptación** (a mostrar en el FRENO con la salida):
  - los dos renglones vuelven a `ri_rml::1.2.3`, que termina en «…estadounidenses-.»;
  - existen `ri_rml::1.2.4` y el 1.3 verdadero;
  - **ninguna unidad queda formada solo por esos renglones**;
  - en `snp_tr`, lo mismo:
    - la unidad que perdió el renglón, `snp_tr::1.3.3`, lo recupera y termina en «…definidos en los puntos 1.6. “Transacciones” y 1.7.
      “Diseño de registros”.»;
    - **ninguna unidad queda formada solo por ese renglón**;
    - existen 1.4, 1.4.1 a 1.4.4, 1.5, 1.5.1, 1.5.2, 1.5.2.1 y 1.5.2.2;
    - el 1.6 abre en «1.6. Transacciones.»;
  - los 4 encabezados de verdad no cambian.

**R5-e `rotulo_vertical` (mecanismo 6), por lista: los formularios de ri_ccna** (decisión de la autora, punto 3).
- **La regla:** los renglones de una sola letra mayúscula que forman, en la misma columna, un rótulo vertical se juntan en la palabra y van
  al formulario de la página en que están. No quedan en el anterior ni intercalados.
- **Aceptación:** `ri_ccna::D1F3::S0` termina en «Fórm. 4368 C (II-2006)», sin la «C» suelta, y `D1F4::S0` no tiene letras sueltas.

**2.6 El detector del 1.16, corregido antes de S1-ter** (pregunta b2 de la autora).
- **El de S1-bis** (`s1bis/scripts/censo_renglones_S1bis.py:57-95`): una lista es un nodo con dos o más puntos hijos, todos hojas. Es
  candidata si el último ítem tiene un corte de párrafo (renglón con mayúscula después de uno que termina en «.» o «:») y ninguno de los
  anteriores lo tiene. Así no ve:
  - las listas cuyos ítems tienen un título sin punto final. En `ri_oc::B.2.4` y `ri_oc::B.3.4` el cierre sigue al título
    («…de moneda extranjera» / «La información solicitada en los puntos…»);
  - los campos numerados leídos como secciones. En ri_secoexpo, el párrafo que sigue al ítem 17 está en la columna de los rótulos
    (columna 0), explica el campo 16 y quedó en el texto propio de `ri_secoexpo::S17`, junto con todo el bloque A.2 que sigue
    (5.271 caracteres, pp. 3-8).
- **Corrección** (`detector_116_corregido_mesa.py`, en el paquete de la mesa):
  - (i) el renglón del título del ítem cuenta como párrafo propio, y la lista es candidata si el último ítem tiene más párrafos que
    cualquiera de los anteriores;
  - (ii) se recorren también como lista las secciones sin puntos consecutivas cuyo texto empieza con «N.»;
  - el detector final es la **unión** con el de S1-bis, porque la corrección sola pierde un candidato original.
- **Sobre la salida de S0-4b:** 121 candidatos con el de S1-bis, 316 con la corrección y 317 con la unión. Son 196 nuevos, 70 de la tanda
  1, y entre ellos `ri_oc::B.2.4` y `ri_oc::B.3.4`.
- **ri_secoexpo** queda fuera también con la corrección: su lista de secciones termina en `S19`. Su problema es otro: la numeración
  vuelve a empezar en el bloque A.2. Queda como límite declarado y va al grupo 2, porque no está en la tanda 1 (decisión 1 de la autora,
  09/10/2026). Si una de sus unidades sale en el sorteo de S1-ter, cuenta como error.
- **La cifra del censo de S1-bis** (8 de 35) se declara con esa salvedad: el detector no veía 70 candidatos de la tanda 1, que no se
  leyeron.
- **Para S1-ter:**
  - el detector corregido corre sobre la salida de S0-5b;
  - los 30 candidatos del 1.16 se sortean entre los del detector corregido sobre la salida de S0-5b (decisión 2 de la autora,
    09/10/2026):
    - incluida la tanda 1;
    - menos los 35 ya leídos y los casos usados para diseñar las reglas (`adfsp::1.1.10`, `ri_oc::B.2.4` y `ri_oc::B.3.4`);
    - con la semilla `U-SEG-OFICIAL:1_16:S1-ter`, sellada en la nota del 09/10/2026, que no cambia;
  - los 35 se releen como prueba de regresión, sin cifra.

## 3. Lo que queda como límite declarado (criterio del punto 4 de la autora: tanda 1, regla por lista en S0-5; si no, límite y grupo 2)

- **Limpieza de documentos que no están en la tanda 1, en el grupo 2:**
  - el tercer renglón del recuadro de encabezado leído como texto del preámbulo, en `ri_iepsp::S0` y `ri_ieccm::S0`;
  - los encabezados de columna repetidos dentro de `ri_icpipsp::A1C3::S2`.
- **ri_secoexpo:** la numeración que vuelve a empezar en el bloque A.2 (§2.6). Grupo 2; si sale en el sorteo de S1-ter, cuenta como error.
- **La intro de 2.2 de ri_mmsef no es un error de corte.** `ri_mmsef::2.2::intro` es una sola unidad de 465 caracteres. La herencia de sus
  descendientes la muestra en cuatro tramos `intro`, partidos a mitad de oración, pero unidos dan su texto propio. No cambia nada.

## 4. Controles duros (los de S0-4)

- **Por regla, antes de aplicar:** el censo de los 152, con su interruptor apagado y prendido.
- **La tanda 0, fuera:** 57 de 57 archivos byte a byte iguales a `salida_tanda0_r2b/`, con el script secuencial.
- **Los 152 dos veces,** iguales entre sí; y la diferencia contra la salida de S0-4b (`61ed4bc9…`), explicada unidad por unidad por las
  reglas.
- **Selftests:**
  - `selftest_e0` y los de las reglas anteriores (b52, b581, b582 y b583);
  - un caso positivo por regla, tomado de la lectura;
  - casos negativos: los 27 candidatos correctos del 1.16, los 4 chapeaux de verdad y los 4 encabezados de verdad de R5-d.
- **Claves.** R5-a, R5-a′, R5-b, R5-c y R5-d crean, quitan o unen unidades. Lo que pasa con las claves:
  - las de las unidades que ninguna regla toca no cambian;
  - una unión conserva la clave de la primera unidad y no renumera las siguientes (`::13`+`::14` queda como `::13`, y `::15` sigue
    siendo `::15`);
  - las claves nuevas siguen la convención de E0: `<to>::<numero>`, `::intro`, `::cierre`, con el prefijo de sub-documento donde lo
    haya;
  - el FRENO lista toda clave creada, quitada o cambiada, con la regla que la causa;
  - el selftest de claves compara contra esa lista y da OK solo si los cambios son exactamente esos.
- **Tabla de reprocesamiento:** una fila nueva (cambio del código de E0 antes de la tanda 1).
- **Repo:** sha256 antes y después; solo cambia `s0_5/`.
- **Convenciones:** 2.213 `.pyc` y grep de convenciones.

## 5. FRENO S0-5a

Lleva:
- el diseño aplicado, con lo que cambió de este mandato y por qué;
- el parche;
- los censos por regla;
- los controles, con sus salidas;
- la evidencia de cada aceptación del §2;
- la lista de los 27 candidatos de R5-a′, con su página y su lectura, para la decisión de la autora;
- la lista de las claves creadas, quitadas o cambiadas, con su regla;
- la tolerancia de columna de R5-a.
- los límites declarados del §3, con su cifra.

Cierre:
- paquete `revision_USEG_OFICIAL_FRENO_S0-5a/` con `manifest.txt`, copiado con `ditto` a
  `~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/<sesión>/scratchpad/revision_USEG_OFICIAL_FRENO_S0-5a/` y verificado contra su
  `manifest.txt` (CLAUDE.md §4.g);
- el mensaje de commit PREPARADO, sin nombres de unidades, documentos ni mecanismos;
- nada commiteado.

FRENO.

Después (no es de esta sesión):
- la revisión de la mesa;
- S0-5b, con el parche aplicado una sola vez;
- S1-ter: tramo a; sorteo con las semillas selladas; lectura a ciegas por una sesión nueva de la mesa, abierta fuera del repo, que no
  abre este mandato, el acta de la adjudicación ni las notas del mandato; la revisión de la autora.

---

**[09/10/2026] Nota de la mesa antes del despacho: control de continuidad de la numeración** (decisión de la autora del 09/10/2026).
Es un control, no una regla: no cambia ninguna unidad. Se suma a lo que S0-5a corre y entrega.

- **Qué lista.** Sobre los 152, antes y después de las reglas, por TO, cada salto de numeración: un punto cuyo hermano anterior o padre
  no existe como unidad.
  - «Existe como unidad» se lee en el árbol de puntos de E0 (`estructura_<to>.json`), por subdocumento: el punto es una unidad o el
    encabezado que heredan sus unidades.
  - Esa definición sola no ve `ri_rml::1.2.4`: es el último punto de su lista, ningún hermano lo sigue y no deja hueco. Por eso el
    control suma la cola: el sucesor del último hijo de un punto, y los que siguen mientras aparezcan, si aparece al principio de un
    renglón del texto propio de alguna unidad.
  - Un rótulo pegado al título, sin espacio («2.8.Código 11»), cuenta como rótulo.
- **La clase de cada salto:**
  - (i) el PDF salta: el rótulo no aparece al principio de ningún renglón de las páginas del TO con alguna unidad (el índice no cuenta;
    se marca si aparece solo ahí);
  - (ii) punto tragado: el rótulo aparece al principio de un renglón dentro del texto propio de otra unidad. Se dan la unidad que lo
    tiene, el renglón y el final del renglón anterior, con la marca `posible_referencia` si ese renglón termina en «punto» o «puntos»,
    o si el resto del renglón está vacío o empieza en minúscula;
  - (iii) otra.
  - En las tres clases, los descendientes del rótulo que aparecen al principio de un renglón de alguna unidad y no son puntos de E0.
- **Aceptación:**
  - antes de las reglas salen como (ii), en la unidad que hoy los tiene:
    - `ri_rml::1.2.4`, en `ri_rml::1.3`;
    - en snp_tr, 1.3.4, 1.3.5, 1.3.6, 1.4 y 1.5, en `snp_tr::1.6::intro`, con sus descendientes: 1.3.4.1, 1.3.4.2, 1.3.5.1 a
      1.3.5.3, 1.3.6.1, 1.3.6.2, 1.4.1 a 1.4.4, 1.5.1, 1.5.2, 1.5.2.1 y 1.5.2.2;
  - después de las reglas, ninguno es un salto.
- **Corrección del §0 (mecanismo 5) y de la aceptación de R5-d en snp_tr. Error de la mesa.**
  - `snp_tr::1.6::intro` se lleva también 1.3.4 a 1.3.6.2, y cinco renglones de 1.3.3: desde «A los efectos de que no se produzcan
    retrasos…» hasta «El siguiente gráfico presenta el esquema de compensación entre CEC:» (salida de S0-4b,
    `s1bis/e0/chunks_snp_tr.json`).
  - La causa: armé la lista del §0 y la aceptación con los puntos de número mayor que 1.3 (1.4 y 1.5, con sus hijos), sin recorrer el
    texto de la unidad renglón por renglón. Lo encontró el prototipo de este control, que sí lo recorre.
  - La aceptación de R5-d en snp_tr queda así:
    - `snp_tr::1.3.3` recupera el renglón de la remisión y los cinco que lo siguen, y termina en «El siguiente gráfico presenta el
      esquema de compensación entre CEC:», no en «…“Diseño de registros”.»;
    - existen 1.3.4, 1.3.4.1, 1.3.4.2, 1.3.5, 1.3.5.1 a 1.3.5.3, 1.3.6, 1.3.6.1 y 1.3.6.2, además de los que ya nombra;
    - lo demás no cambia.
  - En ri_rml la aceptación está bien: el renglón anterior a «1.2.4.» es «…estadounidenses-.».
- **Lo que S0-5 no arregla.** Los saltos (ii) y (iii) que quedan después de las reglas van al FRENO, para la decisión de la autora,
  con el criterio de siempre: en un TO de la tanda 1, regla por lista en S0-5; fuera de la tanda 1, límite declarado y grupo 2. Los (i)
  van como información, salvo los que tienen descendientes tragados, que se tratan como (ii).
- **Control fijo de E0.**
  - En S0-5a vive en `s0_5/scripts/`, con su selftest:
    - los casos de la aceptación, como (ii);
    - un (i): pimf, donde el PDF salta de 2.1.3 a 2.1.3.5;
    - una remisión con `posible_referencia`: 1.3.1.9 de ctacte, en `ctacte::1.5.2.8`.
  - En S0-5b entra a `reextraccion_v2/e0_chunking/` como script propio, con su selftest, sin cambiar la salida de E0.
  - Corre en el tramo a de S1-ter y en el E0 de cada tanda, y su lista va al FRENO.
- **El FRENO de S0-5a** trae, además, la salida del control antes y después de las reglas, la evidencia de su aceptación y la lista para
  la autora.
- **El control que ya existía, y por qué no vio estos casos** (pregunta de la autora).
  - **Uno parcial:** el censo del punto 7 de S0-1 sobre lo que la regla no alcanza (`s0_1/scripts/censo_p7_resto.py:1-2`, en
    `3920323`). Lista los rótulos con título en mayúscula que E0 rechazó por «padre no abierto», con el padre existente.
  - **Vio parte de los dos casos.** En `s0_1/censos/censo_p7_resto_base.json` y `_final.json` están 1.2.4 de ri_rml y 1.3.4, 1.3.5 y
    1.3.6 de snp_tr. El diseño de S0-1 los dejó como límite medido entre los 70 que la regla no alcanzaba, y explicó solo el mecanismo
    de manori, que eran 58 (`s0_1/DISENO_S0-1.md:271-276`). S0-1 bis resolvió manori: de 70 a 12 (`s0_1bis/DISENO_S0-1bis.md:110-111`,
    en `d9d2212`). Los otros 12 no se leyeron uno por uno.
  - **Sobre la salida de S0-4b** el censo sigue dando esos 12 (corrida de la mesa con una copia del script). Cinco son puntos tragados,
    que este control da como (ii): 1.2.4 de ri_rml, 1.3.4 a 1.3.6 de snp_tr y 1.8.1 de ri_cc. Los otros siete no son saltos:
    - tres repiten el rótulo de un punto que existe (cirmo3, dos; depaho, uno). Los dos de cirmo3 («1.2.16.1.» y «1.2.18.1.») están
      en `cirmo3::1.2.13::intro` y `cirmo3::1.2.15::intro`, en las pp. 11 y 13, donde faltan 1.2.13.1 y 1.2.15.1: el PDF los numera
      mal, y este control los da como (i);
    - tres son filas de tabla (snp_tr_nc);
    - uno es un rótulo mal numerado en el PDF («2.2.5.8. Provincia.», dentro de `ri_mmsef::2.5.5.7`; 2.5.5.8 no existe).
  - **No ve 1.4 ni 1.5 de snp_tr.** Su padre, la sección 1, está abierto: E0 los rechaza porque no siguen al último hermano visto (el
    1.6 falso ya estaba aceptado), no por «padre no abierto».
  - **No era un control fijo:** corrió en S0-1 y S0-1 bis, no en S0-2 a S0-4b ni en S1 y S1-bis.
  - **E0 registra, además, los saltos** entre encabezados aceptados y cada candidato rechazado, con su motivo (`e0_lib.py:21-25`). El
    de snp_tr está registrado (`salto_hermano`, padre 1, de 3 a 6, p. 11, en `s1bis/e0/estructura_snp_tr.json`). El de ri_rml no es un
    salto, porque el «1.3.» falso sigue a 1.2.3. Ningún script de U-SEG-OFICIAL lee los saltos.
- **Prototipo de la mesa.** Es solo de referencia: la cifra que vale es la de S0-5a. Está en el paquete de la mesa
  (`fuera_del_repo/scratchpads/d0348a29-aaa4-4292-82f3-0c0149e3787e/scratchpad/hoja_de_ruta_tanda1_mesa/S0-5_evidencia_control_continuidad/`,
  `control_continuidad_numeracion_mesa.py`).
  - Sobre la salida de S0-4b: 25 saltos en 9 TOs, 12 (i), 13 (ii) y 0 (iii). Uno de los (ii) es la remisión de ctacte.
  - En la tanda 1: 10 saltos en 5 TOs, 4 (i) y 6 (ii). Los 6 (ii) son los de la aceptación. De los (i), 3.3.6 de snp_cheq tiene un
    descendiente tragado, 3.3.6.2, en `snp_cheq::3.3.5.1`.
  - Fuera de la tanda 1: 15 saltos en 4 TOs, 8 (i) y 7 (ii). Cinco de esos (ii) son rótulos pegados al título, en ri_cc y snp_dd,
    un mecanismo que S0-5 no trata.

---

**[09/10/2026, noche] Nota de la mesa: revisión del FRENO de S0-5a, decisiones de la autora para S0-5a-bis, y S1-ter.**

- **La revisión de la mesa, sobre copias.** El paquete `fuera_del_repo/scratchpads/0c0c6584-…/scratchpad/revision_USEG_OFICIAL_FRENO_S0-5a/`
  da 82 de 82 en sus dos lugares. Se reproducen:
  - el parche, con los tres sha256 finales;
  - los 152 con el código final, 2.361 archivos iguales byte a byte a la salida del paquete;
  - la tanda 0, 57 de 57;
  - los selftests de E0 (169, 39, 34, 59 y 33);
  - el control de claves, OK con 75, 35 y 343;
  - la aceptación, byte a byte;
  - y la de R5-d de la nota anterior, vista sobre la salida.

  Las 343 claves cambiadas son unidades que conservan su id y cambian algún campo: 250 solo lo heredado, 9 lo heredado y su recorte,
  y 84 su texto propio. Ninguna es de la tanda 0. Detalle en el paquete de la mesa, `hoja_de_ruta_tanda1_mesa/revision_S0-5a/`.
- **Corrección del §2, R5-b. Error de la mesa.** Donde dice «19 pares de rótulo y descripción: 15 en snp_dd», son **18: 14 en snp_dd y 4
  en snp_cheq**, como da el censo de la mesa que el mandato cita. La salida de S0-5a está bien.
- **Decisiones de la autora del 09/10/2026, para S0-5a-bis:**
  1. **R5-a, por lista.** Entran **41 listas:** los 9 casos y 32 cierres que la mesa confirmó contra la página. La lista, con la página
     de cada caso, está en `revision_S0-5a/lista_R5a_por_lista_mesa.json` del paquete de la mesa.
     - Son: `adfsp::1.2.2.2`, `adfsp::2.6.3.2`, `apnf::1.3.1.2`, `cedin::7.1.3.2`, `consyr::3.4.4`, `cryl::4.2.2`, `ctacor::1.3.2`,
       `ctavis::8.2.1.4`, `depinv::1.7.2.2`, `depinv::1.9.2`, `efemin::2.3.2`, `evacre::2.1.2`, `fimipyme::4.3.3`, `fimipyme::5.1.2`,
       `finsec::5.1.2`, `finsec::5.2.5`, `garant::1.2.8.2`, `garant::1.2.9.4`, `gracre::6.7.2`, `manori::1.1.6.5`, `ratio::5.2.1.5`,
       `ri2_pm::1.6`, `ri_rml::1.4.2`, `seguef::2.1.6.2`, `seguef::2.9.2`, `snp_cec::9.1.3.3`, `snp_mep::3.1.1.2`, `snp_mep::3.1.2.2`,
       `snp_mep::4.6.2`, `snp_psp::1.3.2.2`, `snp_tr_nc::5.2.3.2` y `tasint::3.3.2`.
     - En `ri_rml::1.4.2` el cierre de 1.4 empieza en «Para el punto 1.4.1.», un párrafo antes de lo que movía S0-5a.
     - `seggar::5.3.5` no entra: su texto es el de «6. Instrumentación.», un encabezado que E0 no abrió. Es límite declarado y va al
       grupo 2, PENDIENTE de la autora.
     - `ri_cc::R5::2.2.1.2` es dudosa y la adjudica la autora. Hasta entonces, no entra.
     - Las demás listas no se tocan.
  2. **R5-a no toca filas de tabla.** Excluye los renglones que serializa `e0_tablas`, y las 468 tablas siguen serializándose.
  3. **R5-a′ sigue solo para ri_oc, con la clave `ri_oc::Sbloque1`** (aceptada).
     - `ri_rml::1.2.3` no es un caso real: «Plazos residuales» es un subtítulo dentro de 1.2.3 (p. 3). No entra.
     - Los otros 23 candidatos de afuera quedan declarados, y van al grupo 2 si se confirman.
  4. **Los saltos de la tanda 1, por lista:**
     - ri_ccna: los rótulos pegados de D1A1 (2.1.1 a 2.1.8, 5.1 y 8.1) y de D1A2 (5.1) abren su punto;
     - snp_cheq: «3.3.6.2. Instrucciones operativas.» (p. 38) abre como unidad colgada de 3.3, porque el PDF salta 3.3.6 y 3.3.6.1.
       El salto se declara.
  6. **Toda heurística de un censo de la mesa** queda en el paquete con su script. Los 27 candidatos de R5-a′ de la mesa no se
     reprodujeron por eso: error de la mesa.
- **Decisión 5, S1-ter.** La lectura del 1.16 tiene que poder ver los errores de R5-a, así que su sorteo cubre también las listas que R5-a
  modificó. Dos poblaciones:
  - **(a) Las candidatas que quedan:** el detector corregido sobre la salida de S0-5b, incluida la tanda 1, menos los 35 ya leídos y los
    tres casos de diseño (`adfsp::1.1.10`, `ri_oc::B.2.4` y `ri_oc::B.3.4`). Son 30, con la semilla `U-SEG-OFICIAL:1_16:S1-ter`, ya
    sellada, como estaba.
  - **(b) Las listas que R5-a modificó por lista en S0-5b,** menos los tres casos de diseño y los 6 de los 35: los 32 cierres
    confirmados.
    - **Propuesta de la mesa:** 15 sorteadas, con su propia cifra.
    - **Semilla, sellada por esta nota antes de sortear:** `U-SEG-OFICIAL:1_16:S1-ter:R5-a`.
    - **La pregunta, la misma del 1.16:** si la unidad empieza y termina donde empieza y termina su punto, lo que en (b) incluye que el
      cierre no lleve de más ni de menos.
    - **PENDIENTE de la autora:** el tamaño de (b), o un sorteo único de 30 sobre (a) y (b) juntas.
  - Los 35 se siguen releyendo como prueba de regresión, sin cifra.
