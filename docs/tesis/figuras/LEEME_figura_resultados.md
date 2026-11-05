# figura_resultados — registro de generación

Figura de los resultados de fidelidad, para el capítulo 5. Son 2 paneles de
barras, uno al lado del otro, con el eje vertical «Fidelidad» de 0 a 1. Cada
barra lleva su intervalo al 95 % por remuestreo de las preguntas, como barra de
error. La imagen no lleva título.

- Panel izquierdo, la medición final: los grupos «Dato directo» y «Varios
  puntos», con barras para «Grafo», «Fragmentos, combinada» y «Fragmentos,
  densa».
- Panel derecho, la segunda comparación: los grupos «Agregación», «Remisión» y
  «Condición o excepción», con barras para «Grafo con el cambio», «Grafo sin el
  cambio», «Fragmentos, combinada» y «Fragmentos, densa».

Las 18 barras son 6 del panel izquierdo (2 grupos × 3 sistemas) y 12 del derecho
(3 grupos × 4 sistemas).

## 1. Cómo se regenera

Desde la raíz del repositorio, con el commit como argumento:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -B <directorio>/fig_resultados.py 73f4bc4e8f94742c9fd99bd4531900a65424d1c6
```

`<directorio>` es donde esté el script. Escribe `figura_resultados.svg`,
`figura_resultados.png` y `control_valores.md` junto al script, o en otro lugar
con `--salida <directorio>`.

Herramientas, las de `fig_evaluacion.py` (`LEEME_figura_evaluacion.md:33-34`):
Python 3, solo la biblioteca estándar (lo corrí con Python 3.12.13), y
`rsvg-convert` 2.62.3 (cairo 1.18.4, pango 1.58.2; `rsvg-convert --version`). El
script usa además `git --no-optional-locks show`, solo para leer. No importa ni
ejecuta código del repositorio, no usa red ni API.

## 2. De dónde sale cada cifra

El script no tiene ninguna cifra de la figura escrita, salvo la tabla `ESPERADOS`
del control (§5). Cada barra sale de `git --no-optional-locks show <commit>:<archivo>`,
por la ruta de campos `confirmatorio.principal.por_tipo.<tipo>.por_brazo.<brazo>`,
y de ese brazo solo uso `media` (la altura de la barra) e `intervalo_95` (los 2
extremos de la barra de error). El renglón es el que abre el brazo en el commit
de §1; la ruta de campos es la que manda y el script informa si un renglón no
coincide. Los valores, sin redondear, están en `control_valores.md`.

- Archivo A: `data/experiment/banco_mcp/b63/analisis/c/analisis_B63.json`.
- Archivo B: `data/experiment/banco_mcp/b64/analisis/salidas/a/analisis/analisis_B64.json`.

| Panel | Sistema | `<tipo>` | `<brazo>` | Archivo y renglón |
|---|---|---|---|---|
| izquierdo | Grafo | `dato_directo` | `kg` | A:1179 |
| izquierdo | Fragmentos, combinada | `dato_directo` | `fragmentos_hibrida` | A:1172 |
| izquierdo | Fragmentos, densa | `dato_directo` | `fragmentos_denso` | A:1165 |
| izquierdo | Grafo | `varios_puntos` | `kg` | A:1221 |
| izquierdo | Fragmentos, combinada | `varios_puntos` | `fragmentos_hibrida` | A:1214 |
| izquierdo | Fragmentos, densa | `varios_puntos` | `fragmentos_denso` | A:1207 |
| derecho | Grafo con el cambio | `agregacion` | `kg` | B:261 |
| derecho | Grafo sin el cambio | `agregacion` | `kg_n7` | B:268 |
| derecho | Fragmentos, combinada | `agregacion` | `fragmentos_hibrida` | B:254 |
| derecho | Fragmentos, densa | `agregacion` | `fragmentos_denso` | B:247 |
| derecho | Grafo con el cambio | `remision` | `kg` | B:359 |
| derecho | Grafo sin el cambio | `remision` | `kg_n7` | B:366 |
| derecho | Fragmentos, combinada | `remision` | `fragmentos_hibrida` | B:352 |
| derecho | Fragmentos, densa | `remision` | `fragmentos_denso` | B:345 |
| derecho | Grafo con el cambio | `condicion_excepcion` | `kg` | B:310 |
| derecho | Grafo sin el cambio | `condicion_excepcion` | `kg_n7` | B:317 |
| derecho | Fragmentos, combinada | `condicion_excepcion` | `fragmentos_hibrida` | B:303 |
| derecho | Fragmentos, densa | `condicion_excepcion` | `fragmentos_denso` | B:296 |

El brazo `kg` no es el mismo sistema en los 2 paneles: a la izquierda es «Grafo» y
a la derecha, «Grafo con el cambio». Por eso el estilo de cada barra se asigna por
sistema (tabla `ESTILOS`) y no por brazo.

## 3. Formato: de dónde sale cada valor

`E` es `docs/tesis/figuras/fig_evaluacion.py` (sha256
`34b18970e3f282d0ba17e211e5bf0098c18d2c48b95dd5d60f694d14a63894cd`) y `T` es
`docs/tesis/figuras/generar_figura_tamano_tos.py` (sha256
`6a08d197d5ee912fce21d5afa7fc84cc546085988bd832809489417d0d5664e9`), los 2 en el
commit de §1.

| Valor | En esta figura | Fuente |
|---|---|---|
| Azul `#2a78d6` | «Grafo», «Grafo sin el cambio» y «Grafo con el cambio» | T:128 |
| Aguamarina `#1baf7a` | «Fragmentos, combinada» | T:128 |
| Pizarra `#4a5a6a` | «Fragmentos, densa» | E:175 |
| Liso | todas las barras, salvo «Grafo con el cambio» | |
| Rayado del mismo azul sobre blanco, a 45 grados | «Grafo con el cambio» | azul de T:128; rayado propio |
| `GRILLA = "#e1e0d9"`, grosor `0.8` | grilla | T:129, T:298 |
| `EJE = "#c3c2b7"`, grosor `1` | línea del 0 | T:130, T:301 |
| `TINTA = "#1f1f1f"` | rótulos de grupo, leyenda y barras de error | T:132 |
| `TINTA_SUAVE = "#555555"` | nombre del eje y marcas | T:133 |
| Nombre del eje arriba, 14 unidades sobre el tope | «Fidelidad» | T:302 |
| Marcas a 6 unidades del eje; línea de base a `0.36` del cuerpo | marcas del eje | T:299 |
| `W = 760` | lienzo para 15 cm | E:172 |
| `ANCHO_CM = 15.0` | 15,00 cm de ancho | E:195; `LEEME_figura_evaluacion.md:74` |
| `DPI = 300`, `-w 1772 -f png`, bloque pHYs | PNG a 300 dpi | E:196, E:215, E:1134-1151, E:1158; `LEEME_figura_evaluacion.md:90-91` |
| `TIPOGRAFIA = "Helvetica,Arial,sans-serif"` | `font-family` del SVG | E:173 |
| Cabecera del SVG y fondo blanco | `componer` | E:1067-1069 |
| `MARGEN = 12`, `MARGEN_MM = 2.0` | márgenes del lienzo | E:187, E:198 |
| `MUESTRA_W, MUESTRA_H, FILA_LEY = 24, 16, 22` | muestras y filas de la leyenda | E:189 |
| 9 unidades de la muestra a su texto | leyenda | E:586 |
| línea de base a `0.28` del cuerpo | leyenda | E:624 |
| `ASC, DESC = 0.78, 0.22` | caja de cada texto | E:203 |
| `PT_POR_CM = 72.0 / 2.54` | conversión a puntos | E:214 |
| Tabla de anchos AFM de Helvetica | medida de los textos | E:290, E:293-297 |
| Un decimal en las coordenadas | `f` | E:321-323 |

Medidas propias (no salen de otra figura): `PT_MINIMO = 8.0`, porque ningún texto
queda por debajo de 8 pt; `FS = 15`, un solo cuerpo para todos los textos;
`IL = 18`; `ALTO_GRAFICO = 250`; `BARRA = 28`; `SEP_BARRA = 2`; `SEP_GRUPO = 25`;
`GROSOR_BARRA = 1.0`; `RAYA = 2.4`; `PASO_RAYA = 5`; `GROSOR_ERROR = 1.4`;
`GROSOR_HALO = 3.4`; `TOPE_ERROR = 5`; `BAJO_EJE = 20`; `SOBRE_LEYENDA = 10`;
`SEP_COLUMNA = 20`.

El tercer color sale de `E` porque `T` tiene solo 2 colores de barras. Elegí el
pizarra y no el naranja `#e07b39` (E:174) porque `T:40-41` dice que las figuras de
la tesis reservan el naranja a las remisiones y al resaltado del ejemplo, y esta
figura tiene un grupo «Remisión». Lo elegí sobre el gris `#999999` (E:176) porque
ese gris tiene casi la misma luminosidad que el aguamarina: contra el blanco, por
la fórmula de luminancia relativa de WCAG, dan 2,85:1 y 2,82:1, y el pizarra da
7,09:1. `T:42-43` da 2,74:1 para el aguamarina porque el validador de paleta
mide contra su fondo claro por defecto, `#fcfcfb`; contra el blanco del lienzo,
el mismo validador da 2,82:1 (§7).

## 4. Composición

- Cada panel lleva su eje, su nombre de eje y su leyenda. La leyenda va debajo del
  panel, en el orden de las barras. Hay una por panel porque el panel izquierdo
  nombra «Grafo» a la muestra que el derecho nombra «Grafo sin el cambio».
- Los paneles no llevan rótulo, porque la imagen no lleva título. El epígrafe,
  que no forma parte de la imagen, tiene que decir cuál es cada panel.
- «Condición o excepción» va en 2 renglones: mide 150,9 unidades a este cuerpo y,
  en un renglón, su borde derecho llegaría a 752,0 unidades, más allá del límite
  de 749,9 que dejan los 2 mm de margen.
- Las barras de error llevan un halo blanco debajo, para que se lean sobre
  cualquier relleno.
- «Fragmentos, combinada» en «Dato directo» tiene el intervalo [1,000; 1,000]: su
  barra de error es solo un tope sobre el 1 del eje.
- El lienzo mide 760 × 418 unidades, impreso a 15,00 × 8,25 cm. El PNG mide
  1772 × 975 px a 300 dpi.

## 5. Controles del script

El script termina con error y no escribe la figura si falla uno.

1. Valores: cada media y cada extremo del intervalo se comparan con `ESPERADOS` y
   aprueban si difieren en 0,0005 o menos. La comparación se hace en `Decimal`, con
   la escritura del archivo, porque 2 de los 54 valores están a exactamente 0,0005
   (`0.8125` contra 0,813 y `0.6875` contra 0,688) y así ese límite no queda librado
   al redondeo binario. Aprueban las 18 barras (`control_valores.md`) y los 18
   renglones coinciden.
2. Letra: 15 unidades son 8,39 pt impresos a 15 cm (15 × 425,20 / 760), por encima
   del mínimo de 8 pt.
3. Composición: 27 textos y 55 marcas (barras, barras de error, líneas y muestras),
   sin ningún texto superpuesto a otro ni tocado por una marca.
4. Margen: izquierdo 2,37 mm, superior 2,43 mm, derecho 2,37 mm e inferior 3,10 mm;
   exigido 2,0 mm.

La consola del comando de §1 da estos números.

## 6. Revisión de la imagen

La revisé a tamaño completo y en recortes: ningún texto queda cortado, superpuesto
ni fuera de su lugar, y ninguna barra de error tapa una etiqueta. Las barras de
error de todas las barras se leen, también sobre el rayado.

## 7. Observaciones

- El «Grafo» del panel izquierdo es el mismo sistema que «Grafo sin el cambio», según
  `data/experiment/banco_mcp/b64/v1/config_agentes_b64.json:37`, y `kg` y `kg_n7`
  se corresponden con «Grafo con el cambio» y «Grafo sin el cambio» según las líneas
  36-37 de ese archivo, comprobado en el commit de §1: `kg` es «el brazo
  kg_N7c_amp (N7c+) […] el del grafo, el que adoptó la regla de B2» (:36) y
  `kg_n7`, «el grafo sin corregir (N7, D-10)» (:37).
- No hay etiquetas con los valores sobre las barras: la figura lleva solo las barras
  y sus intervalos.
- El validador de paleta de la guía de gráficos, el que cita `T:42` (con el par de
  `T` da los mismos ΔE 23,1 y 24,0 y el mismo 2,74:1), corrido sobre los 3 colores
  de esta figura en modo claro, contra el blanco del lienzo y con todos los pares:
  pasan la banda de luminosidad, la separación para daltonismo (peor par, pizarra
  y azul, ΔE 17,1, deuteranopía) y el piso de visión normal (ΔE 17,4). El pizarra
  `#4a5a6a` no pasa el piso de croma (0,033, contra un mínimo de 0,1: se lee como
  gris). El aguamarina queda en 2,82:1 contra el blanco, por debajo de 3:1, y por
  eso la leyenda y los rótulos van en tinta.
- El PNG es reproducible byte a byte con la misma versión de `rsvg-convert` y las
  mismas fuentes: 2 corridas dieron los mismos sha256 en el PNG, el SVG y
  `control_valores.md`. `Helvetica` resolvió a `Helvetica.ttc` en esas corridas
  (`fc-match Helvetica`).

## 8. Archivos

| Archivo | sha256 |
|---|---|
| `fig_resultados.py` | `fed52fdffb518cb452d21af05a26fcfe16c8bc27415bfd0cc64e987f9ddd6a90` |
| `figura_resultados.png` (1772 × 975 px) | `96aef14c85737d45491e4780e9445fae57ae7e67705fc3e6104acb6718ce5b78` |
| `figura_resultados.svg` | `eabe9351bfaacedf58c5feb64193a01c324ce55659393c03f10468824be68133` |
| `control_valores.md` | `38f510c5db857d0a2784911939316f8bb3ba3bef1ac82d80cf713a7d4f0b204a` |
