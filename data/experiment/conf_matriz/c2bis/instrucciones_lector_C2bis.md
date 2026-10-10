# Lectura de aristas `condicion_de`

Tu tarea es leer 60 fichas y marcar cada una. USD 0, sin API. Trabajás solo con los archivos de esta carpeta: no abras nada fuera de
ella y no busques otras fuentes.

## Qué es cada ficha

Cada ficha es una relación `condicion_de` de un grafo extraído de normas del Banco Central de la República Argentina, entre un nodo
Condicion (el origen) y un nodo de destino. La ficha trae:
- el origen: su tipo, su etiqueta, su descripción y su tramo;
- el destino: su etiqueta, su descripción y su tramo;
- la unidad de la norma de la que sale la relación, con su texto propio y su texto heredado;
- las páginas del PDF, renderizadas, en `paginas/`.

Las etiquetas, las descripciones y los tramos son salida del extractor, no texto de la norma. Lo que decide es el texto de la norma:
el de la unidad y el de las páginas.

## Las marcas

El criterio es este, y no hay otro:

> Correcta: el texto del fragmento sostiene que el origen es condición (o excepción, o se aplica a, según el predicado) del destino; si
> el nodo parece mal tipado pero la relación es cierta, cuenta como correcta y se anota.

Cada ficha lleva una de tres marcas:
- `correcta`: la de arriba;
- `incorrecta`: el texto no sostiene que la Condicion sea el antecedente del destino;
- `no_decidible`: el texto no alcanza para decidir.

Toda marca que no sea `correcta` lleva en `nota` su motivo. Si el nodo parece mal tipado y la relación es cierta, la marca es
`correcta` y el comentario va en `anotaciones`.

## La planilla

`planilla.jsonl` tiene una fila por ficha. Completá `marca`, `nota`, `anotaciones` y `paginas_vistas` (las páginas que miraste, con
los nombres de `paginas_render`). Si cambiás una marca antes del sello, dejá en `nota` la marca anterior y el motivo del cambio. No
calcules cifras ni cuentes marcas.

## El sello

Cuando estén las 60, corré `python3 -I -B sellar_planilla.py` desde esta carpeta. Controla que estén las 60, con una marca válida y con
nota donde hace falta, y escribe `sello_planilla.txt` con el sha256 de la planilla y la hora. Después del sello no se cambia nada.

## Al terminar

FRENO, con la ruta de la planilla y de su sello y la salida del script. Nada más.
