# Lectura de T4 de la tanda 1, primer tramo: cómo leer

Pre-registro firmado (`docs/preregistro_tanda1.md`, firma en `95b18217`), §5.4: lectura asistida con revisión de la autora (D2), como en
la tanda 0. Cada planilla trae, por elemento, mi propuesta y una justificación que cita el texto. La propuesta no es la lectura:
adjudica la autora.

## Qué se lee, en este orden

| # | muestra | planilla | material (fichas `.md`) | elementos | pregunta | respuestas válidas |
|---|---|---|---|---:|---|---|
| 1 | cola | `cola.csv` | `t3/muestras/material/cola/fichas_cola.md` | 30 | ¿la unidad tiene error? | `con error`, `sin error`, `dudosa` |
| 2 | aceptadas ítems | `aceptadas_items.csv` | `t3/muestras/material/aceptadas_items/fichas_aceptadas_items.md` | 30 | ¿la unidad tiene error? | `con error`, `sin error`, `dudosa` |
| 3 | aceptadas no ítems | `aceptadas_no_items.csv` | `t3/muestras/material/aceptadas_no_items/fichas_aceptadas_no_items.md` | 30 | ¿la unidad tiene error? | `con error`, `sin error`, `dudosa` |
| 4 | vigilancia (2) | `vigilancia_2.csv` | `t3/muestras/material/vigilancia_2/fichas_vigilancia_2.md` | 30 | ¿vaciamiento? | `vaciamiento`, `no vaciamiento`, `no decidible` |
| 5 | vigilancia (7) | `vigilancia_7.csv` | `t3/muestras/material/vigilancia_7/fichas_vigilancia_7.md` | 4 | ¿la arista `ejecuta` desde el rol de alcance tiene apoyo textual? | `con apoyo`, `sin apoyo`, `no decidible` |
| 6 | vigilancia (1) | `vigilancia_1.csv` | `t4/muestras/material/vigilancia_1/fichas_vigilancia_1.md` | 30 | ¿la Condicion lleva un deber explícito que el texto formula como obligación? | `sí`, `no`, `no decidible` |
| 7 | vigilancia (3) | `vigilancia_3.csv` | `t4/muestras/material/vigilancia_3/fichas_vigilancia_3.md` | 30 | ¿los nodos del grupo repiten el mismo contenido normativo? | `duplicación`, `distintos` |
| 8 | observación (12) | `observacion_12.csv` | `t4/muestras/material/observacion_12/fichas_observacion_12.md` | 30 | ¿la arista es correcta contra el texto? | `correcta`, `no decidible`, `incorrecta (<capa>)` |

Las rutas del material son relativas a `data/experiment/tanda1/`. La columna `ficha` de cada planilla da la ruta completa y, tras «#»,
el número de la ficha: es el del encabezado «## n.» del `.md`.

**Las reglas de cada pregunta:**
- **Cola y aceptadas:** una unidad tiene error si al menos un nodo o una relación no lo sostiene el texto de la unidad (propio o
  heredado). Las omisiones van aparte (enmienda de la cola humana, `:26-28`). En la cola, el material es el primer intento; en las
  aceptadas, la extracción final del grafo evaluado.
- **Vigilancia (2):** vaciamiento es que el texto porta contenido normativo y la unidad no tiene relaciones.
- **Vigilancia (1):** la definición del FRENO T3, sección 6, con el agregado de la decisión de la autora del 18/10/2026 (punto 1.4): `no decidible` queda fuera de la tasa
  y se declara con su cuenta.
- **Vigilancia (3):** la definición del FRENO T3, sección 6, con el agregado de la misma decisión (punto 1.4): el grupo es de nodos con la misma unidad
  y el mismo tramo, así que no ve duplicaciones con tramos distintos.
- **Observación (12):** en las incorrectas va la regla implicada con el vocabulario `capa_pipeline` (enmienda de la observación 12,
  §2.1): `E0`, `E1-prompt`, `E1-validador`, `catálogo`, `E2`, `E3` o `ensamblado`. Se escribe, por ejemplo, `incorrecta (E1-prompt)`.
- **La observación (12) que vale es la de `t4/`** (`t4/muestras/observacion_12.json`, con el universo de la decisión de la autora del 18/10/2026, punto 1.2), **nunca la de
  `t3/`**, que queda sin leer.

## La propuesta

- **Quién la hizo:** Claude Opus 5.5 (`claude-opus-5-5`), la ejecutora de T4, leyendo las fichas en su sesión. Sin API y a USD 0.
- **Los criterios que apliqué** están en `../lectura_asistida/lectura_asistida_t4_tramo1.json` (`criterios_de_la_propuesta`). Por ejemplo,
  en la cola y las aceptadas, un tipo cercano con la descripción fiel es lectura laxa (sin error, como en la lectura de las aceptadas de la
  tanda 0), y un contenido que viene de otro punto del documento y no está en el texto de la unidad es `dudosa`.
- **Lo que va aparte del veredicto** (omisiones y observaciones, incluidas las `remite_a` que no sostienen su destino):
  `../lectura_asistida/omisiones_y_observaciones_t4_tramo1.md`. No cambia ninguna propuesta.

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
2. Desde esta carpeta, correr:

   ```
   python3 -I convertir_lectura_T4.py <muestra> <exportación.csv>
   ```

   con `<muestra>` en `cola`, `aceptadas_items`, `aceptadas_no_items`, `vigilancia_2`, `vigilancia_7`, `vigilancia_1`, `vigilancia_3` u
   `observacion_12`.
3. Si todo cierra, escribe `<muestra>_marcada.csv` y da la cuenta de los veredictos y de los que cambian la propuesta. Si algo no
   cierra, no escribe nada y lista los problemas: se corrigen en Numbers, se exporta de nuevo y se vuelve a correr. No pisa una marcada
   que ya exista.

## El sello

Lo hace la autora, con las ocho marcadas: el sha256 y la hora de cada una en `sello_lectura_T4.txt`, en esta carpeta. Por ejemplo:

```
for f in *_marcada.csv; do echo "$(shasum -a 256 "$f" | cut -d' ' -f1)  $f  $(date -r "$f" '+%Y-%m-%d %H:%M:%S %z')"; done > sello_lectura_T4.txt
```

Después, la mesa controla las marcadas contra el sello y contra este material. Las tasas, la atención y la ampliación son del segundo
tramo, con la adjudicación de la autora.
