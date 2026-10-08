# U-UNION-ESTRECHA, U2: criterio de lectura de las uniones, escrito y sellado antes de leer

Rige la primera lectura (`lectura1_u2.json`) y la segunda lectura a ciegas, sobre las mismas fichas
(`fichas_u2.json` y `fichas_u2.md`). Una ficha por unión: la Condicion del ítem, el texto entero de la unidad del
ítem, el nodo destino y el texto entero del bloque que abre la lista (la unidad del encabezado).

## 1. El criterio del mandato

- **Correcta:** según el texto, la Condicion del ítem es condición de esa norma del encabezado (la del nodo destino).
- **Incorrecta:** el texto alcanza para decidir y la unión no es correcta.
- **No decidible:** el texto no alcanza para decidir.

Cada veredicto lleva el tramo literal que lo sostiene, copiado de la ficha.

## 2. Precisiones

Las escribo antes de leer la primera ficha y se sellan con este archivo. No agregan un cuarto veredicto: dicen cómo
aplico los tres.

1. **Qué se juzga: la unión, no la extracción de los nodos.** Se juzga la arista: si la Condicion, tal como la
   identifica su tramo, es condición de la norma que el nodo destino representa. Un defecto de paráfrasis en la
   descripción de uno de los dos nodos no hace incorrecta la unión cuando el tramo identifica sin duda el ítem y la
   norma del encabezado. Tampoco juzgo el tipo de los nodos (si el destino debió ser Potestad y es Operacion, por
   ejemplo).
2. **«Norma del encabezado».** Es la disposición del bloque que abre la lista a la que el texto subordina la lista:
   el acceso o la facultad que se otorga, la obligación que se impone, la operación que se habilita o la excepción
   que se concede. El nodo destino es «esa norma» cuando su tramo en la unidad del encabezado corresponde a esa
   disposición. Si el bloque contiene más de una disposición y el texto subordina la lista a otra distinta de la del
   nodo destino, la unión es incorrecta.
3. **«Condición de».** El texto hace depender la aplicación de esa disposición de lo que dice el ítem, sea de forma
   acumulativa («la totalidad de las siguientes condiciones») o alternativa («alguna de las siguientes»): las dos
   cuentan como condición. Un ítem que el texto enumera entre las condiciones o requisitos de la disposición cuenta
   como condición aunque esté redactado como obligación o como requisito documental, siempre que el texto lo
   presente como algo que debe cumplirse para que la disposición se aplique.
4. **Jerarquía.** Si, según el texto, el ítem pertenece a una sublista subordinada a otro ítem o a otra oración
   (y no a la disposición del nodo destino), o el ítem es una aclaración, una excepción o una nota de procedimiento
   dentro de la lista y no una condición de la disposición, la unión es incorrecta.
5. **La Condicion es la de su tramo.** Si el tramo de la Condicion recoge solo una parte del ítem y esa parte es,
   según el texto, condición de otra cosa (por ejemplo, de un requisito interno del ítem) y no de la disposición del
   nodo destino, la unión es incorrecta. Si el tramo de la Condicion no se puede ubicar en el texto del ítem, o el
   del nodo destino no se puede ubicar en la unidad del encabezado, y con eso el texto no alcanza, la unión es no
   decidible.
6. **Qué es «el texto».** Solo lo que trae la ficha: el texto de la unidad del ítem y el de la unidad del encabezado,
   con lo que cada una hereda de E0, y los tramos y descripciones de los dos nodos. No consulto el PDF, otras
   unidades, el grafo fuera de la ficha ni ningún campo de la regla. Si para decidir haría falta otra cosa (un texto
   cortado, una remisión a otro punto que decide la cuestión), la unión es no decidible y lo digo en la nota.
7. **Tramo que sostiene el veredicto.** Copia literal de un pasaje de la ficha (del ítem, del bloque del encabezado o
   de un tramo de nodo), con la unidad de donde sale. Para «correcta», el pasaje que subordina la lista a la
   disposición y, si hace falta, el del ítem; para «incorrecta», el pasaje que muestra a qué se subordina en cambio;
   para «no decidible», el pasaje que no alcanza o la remisión que haría falta seguir.
8. **Cuenta.** Las no decidibles se declaran y, para el piso, cuentan como no correctas (decisión de la autora del
   08/10/2026). La cuenta no la hago en la primera lectura: sale después de la adjudicación.

## 3. Formato de la lectura

`lectura1_u2.json`: una entrada por ficha, en el orden `U01` a `U29`, con `ficha`, `id_condicion`, `veredicto`
(`correcta`, `incorrecta` o `no_decidible`), `tramo` (literal), `unidad_del_tramo` y `nota` (breve; obligatoria para
`incorrecta` y `no_decidible`).
