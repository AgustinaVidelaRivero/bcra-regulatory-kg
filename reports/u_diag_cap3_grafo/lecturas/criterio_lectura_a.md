# U-DIAG-CAP3-GRAFO — criterio de lectura de la tarea a (escrito antes de leer)

Grafo: KG-Tanda0-Diez-r2b, `a9631a64…`. Población leída: los nodos Excepcion sin `exceptua` ni
`exceptua_obligacion` saliente y los Condicion sin `condicion_de` saliente cuya relación hacia la regla NO
está en el crudo aceptado (el que entra a E2) y cuya unidad tiene, en su extracción validada, al menos un
nodo de un tipo que podría ser el destino (Excepcion: Restriccion u Obligacion, o solo una Operacion;
Condicion: Obligacion, Restriccion, Operacion, Potestad o Excepcion). En esos casos el código no distingue
si la regla está en otra unidad o si el modelo no unió dos elementos de su misma unidad.

Por cada nodo leo: el texto propio de la unidad, su herencia (en el ítem, el bloque que abre la lista), el
label, la descripción y el tramo del nodo, las demás entidades de la unidad y las relaciones del crudo
aceptado. Asigno un código:

- **I-ENC**: la regla a la que el nodo se une está en un bloque heredado de la unidad (el bloque que abre la
  lista, el párrafo o el título de un ancestro). Es la causa (i) del despacho, en el encabezado.
- **I-OTRA**: la regla está en otra unidad no heredada (una hermana, otro punto, otro TO), o el texto de la
  unidad la presupone sin enunciarla. Causa (i), fuera del encabezado.
- **II-OP** (solo Excepcion): la regla exceptuada es una Operacion extraída en la misma unidad. Causa (ii).
- **IV-OMI**: la regla está en la unidad y se extrajo como nodo de un tipo que la matriz admite como
  destino; la relación no se emitió. Causa (iv).
- **IV-NOEXT**: la regla está en el texto propio de la unidad, pero no se extrajo como nodo de un tipo
  admisible (no se extrajo, o se extrajo como Definicion u otro tipo sin firma). Causa (iv), variante.
- **V-DEF**: el nodo acota o califica una Definicion (lo que una clase abarca), no una norma. Causa (v).
- **V-OTRA**: otra causa (el nodo no califica a una regla: procedimiento, aclaración, enunciado de alcance,
  norma mal tipada como Excepcion o Condicion), con la razón. Causa (v).

Reglas de desempate, fijadas antes de leer:
1. Si la regla está a la vez en la unidad (como nodo admisible) y en el encabezado, manda la unidad:
   IV-OMI, porque el modelo tenía a dónde unirlo.
2. Si el nodo es una contra-excepción (devuelve a la regla una parte de lo exceptuado) y la regla que vuelve
   a regir está en la unidad como nodo admisible, IV-OMI; si es una Operacion y el nodo es Excepcion, II-OP.
3. En una Excepcion cuya unidad solo tiene una Operacion, II-OP solo si esa Operacion es la regla
   exceptuada; si la Operacion es otra cosa (p. ej. lo que queda afuera), I-ENC o I-OTRA según dónde esté
   la regla.
4. Si dudo entre dos códigos, anoto el primero que la ficha sostiene y marco `duda` con el otro.

Lectura asistida: la hace una instancia de modelo (esta sesión) y la revisa la autora. Los códigos se
vuelcan en `lectura_a.json` antes de contar.

Controles aparte, con la semilla 20261007:
- 30 nodos sorteados de los que el código asigna a (i) sin leer (unidad sin nodo de tipo admisible): leo si
  la regla está de verdad fuera de la unidad. Wilson al 95 %.
- Las 41 relaciones `(Excepcion, exceptua, Operacion)` rechazadas: leo si la Operacion es la regla
  exceptuada (correcta / incorrecta). Wilson al 95 %.
- 30 uniones propuestas por la regla E (tarea a.2): leo si la unión es correcta. Wilson al 95 %; referencia,
  el piso de 0,75 de L-ESQ-R2 §6.3 (con 30, 28 correctas).
