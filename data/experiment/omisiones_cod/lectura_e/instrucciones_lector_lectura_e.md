# Lectura de casos de campos y notas

Tu tarea es leer 16 casos y clasificar cada uno. USD 0, sin API. Trabajás solo con los archivos de esta carpeta: no abras nada fuera de
ella y no busques otras fuentes.

## Qué es cada caso

Cada caso es un campo (la descripción o la etiqueta) de una entidad extraída de una norma del Banco Central de la República Argentina,
junto con:
- el texto de la unidad de la norma de la que sale, propio y heredado, y sus páginas renderizadas en `paginas/`;
- las notas del verificador que el extractor leyó antes de escribir ese campo;
- las ventanas de tres palabras (normalizadas) que el campo comparte con esas notas;
- una ayuda: las palabras de contenido de las ventanas que no están en el texto de la unidad, y las de metalenguaje del verificador.

## Las clases

Rige la primera que se cumple:
1. **Copia real.** Las ventanas en común llevan metalenguaje del verificador: «falta», «faltante», «no representado», «omite» u
   «omitido», «la extracción», «el extractor», «el chunk», «la unidad», «nodo», «entidad», «debería».
2. **Coincidencia legítima.** Cada palabra de contenido de las ventanas está en el texto de la unidad, y la frase es una reformulación
   de la norma que cualquier descripción fiel escribiría así: el mismo orden de ideas, con cambios de flexión, de orden o de nexos.
3. **Copia real.** Las ventanas introducen una palabra de contenido que no está en el texto de la unidad: un término que trajo la nota,
   o una paráfrasis propia de la nota que la entidad reproduce.
4. **Dudosa.** No se puede decidir con los textos solos. Por ejemplo, la frase es genérica (una fórmula de remisión o de alcance) y está
   a la vez en la nota y, con otras palabras, en la norma.

**Palabras de contenido:** las que no son artículos, preposiciones, conjunciones, pronombres ni formas de «ser», «estar» y «haber».
La ayuda es solo una ayuda: lo que decide es el texto.

## La planilla

`planilla.jsonl` tiene una fila por caso. Completá `clase` (1, 2, 3 o 4), `razon` (una línea, siempre) y `paginas_vistas` (las
páginas que miraste, con los nombres de `paginas_render`). Si cambiás una clase antes del sello, dejá en `razon` la anterior y el motivo.
No calcules cifras ni cuentes clases.

## El sello

Cuando estén los 16, corré `python3 -I -B sellar_planilla.py` desde esta carpeta. Controla que estén los 16, con una clase válida y una
razón, y escribe `sello_planilla.txt` con el sha256 de la planilla y la hora. Después del sello no se cambia nada.

## Al terminar

FRENO, con la ruta de la planilla y de su sello y la salida del script. Nada más.
