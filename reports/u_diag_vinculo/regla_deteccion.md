# U-DIAG-VINCULO — reglas fijadas antes de contar y antes de leer (04/10/2026)

Escribí este archivo antes de correr `code/censo_anuncios.py`, que imprime su sha256 al empezar. Las reglas
de derivación (§7) y de lectura (§9) también son anteriores a la corrida y al sorteo de la muestra.

## 1. Universo

- **Tanda 0:** E0 legada `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0/chunks_*.json` (10 TOs,
  2.434 unidades, `47c9283`). Es la E0 de los grafos r2a (redirección `E0_ENM01` en
  `reporte_ensamblado_r2.json`). Como control, la misma detección corre sobre `salida_tanda0_r2` (e0-r2, `f8dedd4`).
- **Partición:** `data/experiment/segmentacion_84/b584_particion/<to>/chunks_<to>.json` (152 TOs, 9.324 unidades,
  `07d29e4`). Cinco TOs de la tanda 0 (ctacte, docvig, lingob, pagjub y polcre) también están en la partición,
  con la E0 de B5.8.4. Las dos poblaciones se informan por separado y no se suman.

## 2. Contenedor (párrafo sin numerar)

Es un chunk con `tipo = mini_chunk` y `rol_bloque` igual a `intro`, `chapeau_seccion` o `intersticial`. Su
unidad U es el primer token de `unidad`.

## 3. Anuncia contenido de sus subpuntos

Normalizo el `texto` así: uno las palabras cortadas con guion al final de línea (`-\n` seguido de minúscula) y
colapso los espacios. El párrafo anuncia si se cumple una de estas dos:
- **A1:** el texto termina en «:»;
- **A2:** contiene una catáfora,
  `\b(los|las) siguientes\b|\blo siguiente\b|\ba continuaci[oó]n\b|\bseguidamente\b|\b(en|de) (los|las) (puntos|apartados|incisos) (siguientes|que siguen)\b`,
  y después de la última catáfora no hay «:» seguido de texto (eso es una lista dentro del propio párrafo, y se
  informa aparte como «lista en línea»).

Además, el contenedor tiene que tener al menos un subpunto (§4).

## 4. Subpuntos (hijos)

- Los hijos de U son las unidades V del mismo TO que son hijas directas de U por su número: V = U.k; si U es
  una sección `Sn`, V = n.k. Cada hijo abarca todos los chunks con esa unidad (punto, intro, cierre,
  intersticial y partes).
- Si el contenedor es `intersticial`, solo cuentan los hijos que tienen algún chunk cuya herencia trae un tramo
  `intersticial` con `unidad_origen = U`.
- Un par es (contenedor, hijo).

## 5. Tipo de anuncio

- **Cláusula anunciadora:** con A1, la última oración del texto; con A2, la oración que contiene la última
  catáfora. Corto oraciones con `(?<=[.;])\s+(?=[A-ZÁÉÍÓÚÑ¿«“"(])`.
- Clasifico la cláusula en minúsculas, en este orden; gana el primero que se cumple.
  1. **excepción:** primero quito de la cláusula los usos que no anuncian excepción,
     `sin excepci[oó]n|salvo (que|disposici[oó]n|lo (dispuesto|previsto|establecido|indicado)|indicaci[oó]n|expresa|autorizaci[oó]n|en (los|las|el|la) casos? (previst|indicad|establecid))`.
     Después busco
     `excepci[oó]n|excepto|exceptu|salvo|exclu[iy]|exclusi[oó]n|exim|no (se )?(alcanza|comprend|inclu|consider|computa|aplica)|no (ser[aá]n?|estar[aá]n?|quedar[aá]n?) (de aplicaci[oó]n|aplicables?|alcanzad|comprendid|incluid|considerad|computad|sujet)|quedan? (excluid|exceptuad|eximid|fuera)|no corresponder[aá]`.
  2. **condición, los ítems son los supuestos (c1):** se cumple una de estas cuatro:
     - `\b(siempre que|siempre y cuando|en la medida (en )?que|a condici[oó]n de que|en tanto que?)\b`;
     - `\b(siguientes|estos|tales) (casos|supuestos|situaciones|circunstancias|hip[oó]tesis)\b`;
     - `\b(cuando|si)\b[^.;:]{0,40}:\s*$`;
     - `\bsiguientes (condiciones|requisitos|exigencias|recaudos|extremos|par[aá]metros|criterios)\b`, sin
       `\bdeber[aá]n?\s+(observar|cumplir|reunir|satisfacer|contar con|contener|incluir|presentar|verificar)\b`.
  3. **condición, el encabezado condiciona a los ítems (c2):**
     `\bcuando\b|\ben (el|los) casos? (de|en) que\b|\ben caso de\b|\bsi\b|\bcondici[oó]n|\bsiempre que\b|\ben la medida\b`.
  4. **alcance:**
     `\babarca|\bcomprende|\bcomprender[aá]n?\b|\bincluye|\bincluir[aá]n?\b|\bse incluyen\b|\balcanza|\balcanzar[aá]n?\b|\bse (considerar[aá]n?|entender[aá]n?|entiende|consideran?)\b|\bcomprendid|\balcanzad|\bintegra|\bcompon|\bconforma|\bson (las|los) siguientes\b|\bser[aá]n? (elegibles|considerad)|\btales como\b|\ba saber\b|\bse (clasificar|agrupar)[aá]n?\b|\bcategor[ií]as?\b|\bse definen?\b|\bdefin[ei]|\bconceptos?\b|\bclases?\b|\btipos? de\b`.
  5. **enumeración:** todo lo demás.
- Control positivo: `cla::5.1.1::intro` tiene que salir como excepción. Si no sale así, la regla no se corrige
  después de contar: se informa la falla.

## 6. Muestra de 10 casos citados

La sorteo con `random.Random(20261004)` sobre los contenedores que anuncian, tomando juntas la tanda 0 y la
partición. Los ids se ordenan y, si un id está en las dos, uso el de la tanda 0. La estratificación es fija: 3
de excepción, 2 de c1, 1 de c2, 2 de alcance y 2 de enumeración. De cada caso cito el id, el texto del
contenedor y el primer hijo, con sus primeros 160 caracteres.

## 7. Derivación simulada de la dirección (a), solo en la tanda 0

- Grafo: KG-Tanda0-Diez-r2a (`99fe2bfa…`, `f8dedd4`), los diez TOs con crudo `v3_b54`.
- **Nodo anclado en una unidad:** nodo de contenido (Operacion, Restriccion, Excepcion, Obligacion, Potestad,
  Condicion o Definicion) con una procedencia cuyo `chunk_id` es un chunk de esa unidad y cuyo
  `rol_documental` no empieza con `herencia`.
- **(a-T), predicado tipado de la matriz r2** (`modelos_r2.py@HEAD:108-128`):
  - en un par de excepción, cada Excepcion del hijo sin `exceptua`/`exceptua_obligacion` saliente →
    Restriccion del contenedor (`exceptua`) u Obligacion del contenedor (`exceptua_obligacion`);
  - en un par c1, cada Condicion del hijo sin `condicion_de` saliente → Excepcion, Obligacion, Restriccion,
    Operacion o Potestad del contenedor (`condicion_de`);
  - **regla de destino único** (la que propongo): se deriva solo si el contenedor tiene exactamente un nodo de
    los tipos destino admitidos. Informo también cuántas habría sin esa regla (todos los destinos), pero no las
    leo;
  - los pares c2, de alcance y de enumeración no derivan arista tipada.
- **(a-R), `remite_a` desde la estructura:** en todo par que anuncia, cada nodo anclado en el contenedor →
  cada nodo anclado en el hijo, salvo que esa `remite_a` ya exista. Uso la regla D1 de la enmienda 2
  (`5f9a731`, §4): ningún nodo del contenedor contiene el número del hijo, así que la cita se atribuye a todos
  los nodos de contenido del punto.

## 8. Muestra de precisión

- (a-T): `random.Random(20261004).sample` de 15 pares, sobre la lista ordenada de pares de la tanda 0 con al
  menos una arista derivada por la regla de destino único; si hay menos de 15, los tomo todos.
- (a-R): igual, 15 pares, sobre la lista ordenada de pares que anuncian y tienen al menos una arista derivada.
- Leo todas las aristas derivadas de los pares sorteados.

## 9. Regla de lectura (fijada antes del sorteo)

Leo el texto de E0 del contenedor y del hijo (`salida_tanda0`), y el `label` y la `descripcion` de los nodos.
- **Arista tipada `src -p-> tgt`.** Es CORRECTA si se cumplen las tres condiciones:
  1. el texto del contenedor anuncia el contenido del hijo como excepción (si p es `exceptua*`) o como sus
     supuestos o condiciones (si p es `condicion_de`);
  2. `src` expresa el caso exceptuado o la condición que enuncia el hijo;
  3. `tgt` expresa la norma del contenedor que el anuncio exceptúa o condiciona, y no otra norma de esa unidad.

  Si falla alguna, es INCORRECTA. Es NO DECIDIBLE si el texto de E0 de las dos unidades no alcanza para decidir.
- **Arista `remite_a` estructural `src -> tgt`.** Es CORRECTA si se cumplen las tres condiciones:
  1. el contenedor anuncia contenido que está en el hijo, es decir, el hijo es uno de los anunciados;
  2. `src` expresa la cláusula que hace el anuncio, o la norma que la contiene;
  3. `tgt` expresa contenido del texto del hijo.

  Si falla alguna, es INCORRECTA. NO DECIDIBLE, igual que en la arista tipada.
- Cuento por arista y por par. Doy la fracción cruda y el intervalo de Wilson al 95 %.
