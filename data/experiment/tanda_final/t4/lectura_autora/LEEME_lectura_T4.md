# Lectura de T4 de la tanda final: cómo leer

Pre-registro firmado (`docs/preregistro_tanda_final.md`, firma en `4de7f2a7`), §6: lectura asistida con revisión de la autora (D2), como
en el T4 de la tanda 1. Cada planilla trae, por elemento, la propuesta de la ejecutora y una justificación que cita el texto. La
propuesta no es la lectura: adjudica la autora.

## Qué se lee, en este orden

| # | muestra | planilla | material (fichas `.md`) | elementos | pregunta | respuestas válidas |
|---|---|---|---|---:|---|---|
| 1 | cola | `cola.csv` | `t3/muestras/material/cola/fichas_cola.md` | 30 | ¿la unidad tiene error? | `con error`, `sin error`, `dudosa` |
| 2 | aceptadas ítems | `aceptadas_items.csv` | `t3/muestras/material/aceptadas_items/fichas_aceptadas_items.md` | 30 | ¿la unidad tiene error? | `con error`, `sin error`, `dudosa` |
| 3 | aceptadas no ítems | `aceptadas_no_items.csv` | `t3/muestras/material/aceptadas_no_items/fichas_aceptadas_no_items.md` | 30 | ¿la unidad tiene error? | `con error`, `sin error`, `dudosa` |
| 4 | vigilancia (2) | `vigilancia_2.csv` | `t3/muestras/material/vigilancia_2/fichas_vigilancia_2.md` | 30 | ¿vaciamiento? | `vaciamiento`, `no vaciamiento`, `no decidible` |
| 5 | vigilancia (7) | `vigilancia_7.csv` | `t3/muestras/material/vigilancia_7/fichas_vigilancia_7.md` | 6 | ¿la arista `ejecuta` desde el rol de alcance tiene apoyo textual? | `con apoyo`, `sin apoyo`, `no decidible` |
| 6 | vigilancia (1) | `vigilancia_1.csv` | `t3/muestras/material/vigilancia_1/fichas_vigilancia_1.md` | 30 | ¿la Condicion lleva un deber explícito que el texto formula como obligación? | `sí`, `no`, `no decidible` |
| 7 | vigilancia (3) | `vigilancia_3.csv` | `t3/muestras/material/vigilancia_3/fichas_vigilancia_3.md` | 30 | ¿los nodos del grupo repiten el mismo contenido normativo? | `duplicación`, `distintos` |
| 8 | observación (12) | `observacion_12.csv` | `t3/muestras/material/observacion_12/fichas_observacion_12.md` | 30 | ¿la arista es correcta contra el texto? | `correcta`, `no decidible`, `incorrecta (<capa>)` |

Son 216 fichas. Las rutas del material son relativas a `data/experiment/tanda_final/`. La columna `ficha` de cada planilla da la ruta
completa y, tras «#», el número de la ficha: es el del encabezado «## n.» del `.md`.

**Las reglas de cada pregunta** (las de la tanda 1, con las decisiones del 18/10/2026; registro de decisiones, §29, §31 y §35):
- **Cola y aceptadas:** una unidad tiene error si al menos un nodo o una relación no lo sostiene el texto de la unidad (propio o
  heredado). Las omisiones van aparte. En la cola, el material es el primer intento; en las aceptadas, la extracción final del grafo.
  **Una unidad `dudosa` cuenta como error** para la tasa, la atención y el freno; la cuenta sin las dudosas va al lado y no decide nada.
- **Vigilancia (2):** vaciamiento es que el texto porta contenido normativo y la unidad no tiene relaciones (en la extracción final).
- **Vigilancia (1):** `no decidible` queda fuera de la tasa y se declara con su cuenta.
- **Vigilancia (3):** el grupo es de nodos con la misma unidad y el mismo tramo, así que no ve duplicaciones con tramos distintos. Un
  grupo es duplicación solo si un nodo repite el contenido normativo de otro: el par del deber y el acto que regula no es duplicación
  por sí mismo (§31).
- **Observación (12):** en las incorrectas va la regla implicada, con el vocabulario `capa_pipeline`: `E0`, `E1-prompt`, `E1-validador`,
  `catálogo`, `E2`, `E3` o `ensamblado`. Se escribe, por ejemplo, `incorrecta (E1-prompt)`. Su universo son las aristas de extracción de
  la (10), sin `remite_a` (24.949 en el grafo sin cola de la tanda).

## Qué se escribe en la planilla

Solo las dos últimas columnas:
- `veredicto_autora`: una de las respuestas válidas de su muestra, escrita tal cual figura arriba (con sus tildes y en minúsculas).
  Puede repetir la propuesta o cambiarla;
- `nota_autora`: si el veredicto cambia la propuesta, la razón va acá. Si la repite, puede quedar vacía.

Las demás columnas (`id`, `celda`, `ficha`, `propuesta`, `justificacion`) no se tocan: el convertidor las toma de la planilla original y
frena si una fila cambió de lugar.

## Cómo se convierte

1. Abrir `<muestra>.csv` en Numbers, completar las dos columnas y exportar como CSV (UTF-8) a esta carpeta, con otro nombre (por
   ejemplo, `cola_exportada.csv`).
2. Desde esta carpeta, correr `python3 -I convertir_lectura_T4.py <muestra> <exportación.csv>`, con `<muestra>` en `cola`,
   `aceptadas_items`, `aceptadas_no_items`, `vigilancia_2`, `vigilancia_7`, `vigilancia_1`, `vigilancia_3` u `observacion_12`.
3. Si todo cierra, escribe `<muestra>_marcada.csv` y da la cuenta de los veredictos y de los que cambian la propuesta. Si algo no
   cierra, no escribe nada y lista los problemas: se corrigen en Numbers, se exporta de nuevo y se vuelve a correr. No pisa una marcada
   que ya exista.

## El sello

Lo hace la autora, con las ocho marcadas: el sha256 y la hora de cada una en `sello_lectura_T4.txt`, en esta carpeta:

```
for f in *_marcada.csv; do echo "$(shasum -a 256 "$f" | cut -d' ' -f1)  $f  $(date -r "$f" '+%Y-%m-%d %H:%M:%S %z')"; done > sello_lectura_T4.txt
```

Después, la mesa controla las marcadas contra el sello y contra este material. Las tasas, la atención y el freno son del segundo
tramo de T4, con los umbrales que ya calculó T3 (tabla T4 de su FRENO).
