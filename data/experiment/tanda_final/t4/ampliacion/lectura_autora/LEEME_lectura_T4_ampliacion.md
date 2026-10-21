# Lectura de la ampliación de T4 de la tanda final: cómo leer

Pre-registro firmado (`docs/preregistro_tanda_final.md`, firma en `4de7f2a7`), §6: la atención de las aceptadas no ítems saltó en el
segundo tramo de T4 (`t4/FRENO_T4_tramo2.md`, sección 7), y la ampliación suma 30 unidades más del mismo estrato, sorteadas con
`:ampliacion:` (`t4/ampliacion/muestras/`). Se leen como las del primer tramo (`t4/lectura_autora/LEEME_lectura_T4.md`): lectura
asistida con revisión de la autora. La propuesta no es la lectura: adjudica la autora.

## Qué se lee

| muestra | planilla | material (fichas `.md`) | elementos | pregunta | respuestas válidas |
|---|---|---|---:|---|---|
| aceptadas no ítems, ampliación | `aceptadas_no_items_ampliacion.csv` | `t4/ampliacion/material/aceptadas_no_items_ampliacion/fichas_aceptadas_no_items_ampliacion.md` | 30 | ¿la unidad tiene error? | `con error`, `sin error`, `dudosa` |

La ruta del material es relativa a `data/experiment/tanda_final/`. La columna `ficha` da la ruta completa y, tras «#», el número de la
ficha: es el del encabezado «## n.» del `.md`.

**La regla** es la de las aceptadas del primer tramo (registro de decisiones, §29, §31 y §35): una unidad tiene error si al menos un nodo
o una relación no lo sostiene el texto de la unidad (propio o heredado); las omisiones van aparte; el material es la extracción final del
grafo. **Una unidad `dudosa` cuenta como error** para la tasa, la atención y el freno; la cuenta sin las dudosas va al lado y no decide
nada.

## Qué se escribe en la planilla

Solo las dos últimas columnas:
- `veredicto_autora`: una de las respuestas válidas, escrita tal cual figura arriba (en minúsculas). Puede repetir la propuesta o
  cambiarla;
- `nota_autora`: si el veredicto cambia la propuesta, la razón va acá. Si la repite, puede quedar vacía.

Las demás columnas (`id`, `celda`, `ficha`, `propuesta`, `justificacion`) no se tocan: el convertidor las toma de la planilla original y
frena si una fila cambió de lugar.

## Cómo se convierte

1. Abrir `aceptadas_no_items_ampliacion.csv` en Numbers, completar las dos columnas y exportar como CSV (UTF-8) a esta carpeta, con otro
   nombre (por ejemplo, `aceptadas_no_items_ampliacion_exportada.csv`).
2. Desde esta carpeta, correr
   `python3 -I convertir_lectura_T4_ampliacion.py aceptadas_no_items_ampliacion aceptadas_no_items_ampliacion_exportada.csv`.
3. Si todo cierra, escribe `aceptadas_no_items_ampliacion_marcada.csv` y da la cuenta de los veredictos y de los que cambian la propuesta.
   Si algo no cierra, no escribe nada y lista los problemas: se corrigen en Numbers, se exporta de nuevo y se vuelve a correr. No pisa
   una marcada que ya exista.

## El sello

Lo hace la autora, con la marcada: el sha256 y la hora en `sello_lectura_T4_ampliacion.txt`, en esta carpeta:

```
for f in *_marcada.csv; do echo "$(shasum -a 256 "$f" | cut -d' ' -f1)  $f  $(date -r "$f" '+%Y-%m-%d %H:%M:%S %z')"; done > sello_lectura_T4_ampliacion.txt
```

Después, la mesa controla la marcada contra el sello y contra este material, y el tercer tramo de T4 hace las tasas sobre las 60.
