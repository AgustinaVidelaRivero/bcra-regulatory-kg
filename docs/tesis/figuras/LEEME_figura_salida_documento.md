# Figura fig:salida_documento

## Qué muestra

Una barra por cada uno de los 128 documentos del grafo evaluado (las 3 tandas), de mayor a menor, en escala
logarítmica. Cada barra es la salida del extractor sumada para todas las unidades del documento, con la medida
principal: la respuesta final de la primera extracción de cada unidad (`usage.output_tokens` del último registro de
`extracciones_e1.jsonl`). Una unidad partida durante la extracción cuenta por sus partes.

- La barra oscura es Clasificación de deudores (`cla`, tanda 0): 184.462 tokens, lugar 15 de 128.
- La línea continua marca 64.000, el máximo de una respuesta de claude-haiku-4-5. Superan esa línea 55 de los 128
  documentos.
- La línea punteada marca 20.446, la respuesta completa más larga de una unidad entera (`manori::Sbloque5`, tanda 1,
  pedida con techo 40.960).
- La figura no tiene ningún nombre ni id de documento.

## De dónde salen los datos

- Commit fijo del repositorio de la tesis: `3b6f63c1d6523e97ec9efac9b36b2d7ade064265`.
- `datos_figura_salida_documento.json` lo escribe `salida/recuento/recuento_salida.py`, que lee:
  - `data/experiment/reextraccion_v2/manifiestos/{tanda0_10tos_r2b,tanda1_20tos_r2b,tanda_final_98tos_r2b}.json`
    (`orden_corrida`);
  - de cada documento, `data/experiment/reextraccion_v2/corpus_{tanda0,tanda1,tanda_final}/salida_r2b/<documento>/`
    `extracciones_e1.jsonl` y `particiones_por_corte.json`;
  - `data/experiment/reextraccion_v2/e0_chunking/salida_<tanda>_r2b/chunks_<documento>.json`;
  - para la medida de control, `salida/trabajo/pedidos.jsonl`, que escribe `salida/recuento/pedidos.py` desde las 3
    bases de caché de la re-extracción.
- Las cifras y sus cotejos están en `salida/salida_documento.md`, S2 a S4.

## Cómo se regenera

Desde la carpeta de la unidad:

```
PYTHONDONTWRITEBYTECODE=1 python3 -B salida/recuento/pedidos.py
PYTHONDONTWRITEBYTECODE=1 python3 -B salida/recuento/recuento_salida.py
cd salida/figura && PYTHONDONTWRITEBYTECODE=1 /opt/homebrew/bin/python3.10 -B fig_salida_documento.py
```

Con `--medida control`, el script dibuja la medida de control (todos los pedidos pagados de la primera extracción) en
`figura_salida_documento_control.png`. Esa variante no se generó.

## Estilo y entorno

- PNG de 1889 × 779 px: 16 × 6,6 cm a 300 dpi.
- Cuerpo de 9 puntos y leyenda de 8.
- `lmroman10-regular.otf` no está en ninguna de las 3 rutas que busca el script (`/Library/TeX/Root/…`,
  `/usr/share/texlive/…` y `/usr/share/texmf/…`), así que la figura usa la serif por defecto de matplotlib.
- Generada con `/opt/homebrew/bin/python3.10` (Python 3.10.18, matplotlib 3.8.4). El `python3` por defecto no tiene
  matplotlib, y no se instaló nada.
- Eje vertical logarítmico de 1.000 a 5.000.000:
  - 1.000 es la potencia de 10 menor o igual a la barra más baja, que tiene 2.351;
  - 5.000.000 deja la barra más alta, de 1.079.760, debajo del borde y lugar arriba a la derecha para la leyenda;
  - las marcas son 1.000, 10.000, 100.000 y 1.000.000, sin marcas menores.
- Sin marcas en el eje horizontal y sin los bordes de arriba y de la derecha.
- El script corrido 2 veces dio el mismo sha256 del PNG.

## sha256

| archivo | sha256 |
|---|---|
| `figura_salida_documento.png` | `9ce6684b3cf22e6d7270ed1be1bea88ca26463ff294ce3e1ee4614df55bcf8eb` |
| `fig_salida_documento.py` | `96510489da0804494de414ecb12925cb282660780358ce1a67adf8aa98a61c41` |
| `datos_figura_salida_documento.json` | `c986f1e2a4728a70d4d3e95b6fb06e11a2be6f91b127a5463645d93d09195b2b` |
