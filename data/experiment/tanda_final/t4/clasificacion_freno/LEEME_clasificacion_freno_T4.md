# La clasificación del freno de T4 de la tanda final: cómo clasificar

En el tercer tramo de T4 saltó el freno por la atención sobre las 60 en las aceptadas no ítems (`t4/FRENO_T4_tramo3.md`): 16 de 60 con
error. La autora decidió (registro de decisiones, §89) clasificar por tipo esas 16 antes de seguir:
- si ninguna tiene una falla de esquema, el freno se acepta y se declara como residuo, con su tasa;
- si alguna la tiene, se ve antes de seguir. Una «no_se» cuenta como una «sí».

Las 16 son las de tus dos lecturas con «con error» (no hay «dudosa»). La planilla las trae en el orden de tus marcadas.

## Qué se escribe en la planilla

`clasificacion_freno_T4.csv`, en esta carpeta. Las siete primeras columnas no se tocan: `n`, `id`, `celda`, `tramo`, `muestra`, `ficha`
(la ruta de la ficha, relativa a `data/experiment/tanda_final/`, y tras «#» su número) y `nota_de_la_lectura` (tu nota de la lectura, tal
cual). Se completan las cinco últimas:

| columna | qué va | respuestas válidas |
|---|---|---|
| `capa` | dónde nace el error, con el vocabulario `capa_pipeline` que usaste en la observación (12) | `E0`, `E1-prompt`, `E1-validador`, `catálogo`, `E2`, `E3`, `ensamblado`, `no_se`; dos o más, unidas con «+» |
| `falla_de_esquema` | «sí» solo si el esquema no tiene cómo decir lo que dice el texto, y por eso un campo estructurado queda falso: el umbral del procedimiento (c) del protocolo entre tandas (§6), «una falla de esquema que produzca falsedad en campo estructurado en material fresco» | `sí`, `no`, `no_se` |
| `campo` | qué parte está mal | `sujeto`, `relacion`, `valor`, `calificador`, `modalidad`, `tipo_de_nodo`, `otro`; dos o más, unidas con «+» |
| `se_repite` | si el mismo patrón aparece en otra de las 16 | `sí`, `no` |
| `nota_clasificacion` | la razón; obligatoria con `falla_de_esquema` «sí» o «no_se» | texto libre |

Las respuestas van tal cual, en minúsculas salvo las capas. La nota la lees solo vos: la mesa cuenta las otras columnas por código, sin
abrir la planilla.

## Cómo se convierte

1. Abrir `clasificacion_freno_T4.csv` en Numbers, completar las cinco columnas y exportar como CSV (UTF-8) a esta carpeta, con otro
   nombre (por ejemplo, `clasificacion_freno_T4_exportada.csv`).
2. Desde esta carpeta, correr
   `python3 -I convertir_clasificacion_freno_T4.py clasificacion_freno_T4_exportada.csv`.
3. Si todo cierra, escribe `clasificacion_freno_T4_marcada.csv` y da la cuenta por capa, la de las fallas de esquema y lo que sigue. Si
   algo no cierra, no escribe nada y lista los problemas: se corrigen en Numbers, se exporta de nuevo y se vuelve a correr. No pisa una
   marcada que ya exista.

## El sello

Lo hace la autora, con la marcada: el sha256 y la hora en `sello_clasificacion_freno_T4.txt`, en esta carpeta (en zsh):

```
for f in clasificacion_freno_T4_marcada.csv; do echo "$(shasum -a 256 "$f" | cut -d' ' -f1)  $f  $(date -r "$f" '+%Y-%m-%d %H:%M:%S %z')"; done > sello_clasificacion_freno_T4.txt
```

Después, la mesa controla la marcada contra el sello y contra esta planilla y la cuenta por código, y el TF4d commitea esta carpeta con
el tercer tramo de T4. Mientras T5 corre en el repo, esta carpeta queda fuera de su foto, y no corre ningún commit.
