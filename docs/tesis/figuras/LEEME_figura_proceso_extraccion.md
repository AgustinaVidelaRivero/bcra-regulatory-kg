# figura_proceso_extraccion — registro de generación (Figura 1.3)

Figura «del documento al grafo» para la Introducción: el Texto Ordenado de
entrada, las cinco etapas del proceso y el grafo de salida, en dos filas, con la
leyenda al pie. El recuadro «Grafo» muestra el ejemplo del préstamo (punto
5.1.1.1 del Texto Ordenado de Clasificación de deudores, que remite al punto
3.7): Restriccion punto 5.1.1.1 —`referencia`→ Obligacion punto 3.7, y
—`limita`→ Operacion punto 5.1.1.1.

Historia: U-FIG-EJEMPLO (2026-09-28) cambió solo el recuadro «Grafo», que antes
mostraba el ejemplo de los dividendos (Exterior y Cambios, Restricción y
Operación del punto 3.17.1.4 y Obligación del 3.4.2; generador, SVG y PNG del
commit `952b78a`, verificados en `reports/verificacion_figura_proceso.md`).
U-FIG-EJEMPLO-AJUSTE (mismo día) cambió solo el texto de la leyenda de la
remisión (§3). La versión de U-FIG-EJEMPLO no llegó a commitearse: al cierre del
ajuste, `git status` mostraba estos archivos como modificados respecto de
`952b78a`.

## 1. Comandos de generación

```bash
PYTHONDONTWRITEBYTECODE=1 python3 docs/tesis/figuras/extraer_datos_ejemplo_prestamo.py
PYTHONDONTWRITEBYTECODE=1 python3 docs/tesis/figuras/generar_figura_proceso_extraccion.py --verificar
```

El generador escribe `figura_proceso_extraccion.svg` (lienzo 720 × 665) y
exporta el PNG con `rsvg-convert` 2.62.3 (1506 × 1392 px, 300 dpi grabados en
el bloque pHYs). Con `--verificar` mide cada texto con las métricas reales de
Helvetica (PIL 12.3.0 y la fuente del sistema): 42 textos medidos, 0 fallas.

## 2. Grafo, pregunta y fuentes

- Grafo: KG-Reextraído-r1,
  `data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json`, sha256
  `0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a` (candado
  `KG_SHA256` del generador; el script además exige que el JSON del ejemplo se
  haya extraído de ese mismo archivo).
- Pregunta del ejemplo (no aparece en esta figura; es la de la Figura 1.2): «Para
  una entidad financiera, ¿qué condiciones hacen que los créditos para consumo o
  vivienda deban clasificarse en la cartera comercial?»

Los tres nodos se toman por su clave en `ejemplo_prestamo_datos.json` (sha256
`25ab7b4c0d76fd735244fe0fecc17ceaba1b0e8bfd2312e7aa3cbd5c849672a2`, escrito por
`extraer_datos_ejemplo_prestamo.py`, sha256
`4c3a441972d27304b6d58d0664dbc15b893bce7ad3e7d2d49afad947f51eeea7`); el
generador comprueba en `kg.json` que cada uno exista con su tipo y con su punto
como procedencia `punto_propio`, y que cada arista exista exactamente una vez.

| Clave | Nodo (clave en el JSON) | Rótulo dibujado | id |
|---|---|---|---|
| R | restriccion_monto | Restriccion / punto 5.1.1.1 | `Restriccion_los_creditos_para_consumo_o_vivienda_que_superen_el_equivalente_a_dos_veces_el_i_f682b1` |
| O | obligacion_3_7 | Obligacion / punto 3.7 | `Obligacion_el_importe_a_considerar_sera_el_nivel_maximo_del_valor_de_ventas_totales_anuales_7f1ae2` |
| OP | operacion | Operacion / punto 5.1.1.1 | `Operacion_inclusion_en_cartera_comercial_creditos_consumo_vivienda_2644e8` |

| Índice en `kg['edges']` | Arista | Clase | Comprobación |
|---|---|---|---|
| 15772 | R `limita` OP | extracción | firma (Restriccion, limita, Operacion) en la matriz del esquema congelado; sin `rol_fuente` |
| 15773 | R `referencia` O | remisión (acento) | `rol_fuente = referencia_cruzada` |

Los tipos se escriben como en el código, sin tildes, y los rótulos de arista con
el nombre de la relación tal como está en el grafo.

Qué está escrito a mano: ningún dato del ejemplo. Son decisiones de la figura
qué tres nodos del JSON se dibujan y en qué posiciones.

Las mediciones del ejemplo que el JSON resume están versionadas en
`reports/u_inv_ejemplo/` (commit `24e0116`), `reports/u_med_ejemplo/` (commit
`200462f`) y `reports/u_inv_candidatos/` (commit `791166d`); antes estaban en
`/tmp/u_inv_ejemplo/`, `/tmp/u_med_ejemplo/` y `/tmp/u_inv_candidatos/`.

## 3. Leyenda

La leyenda de la remisión dice «remisión de un punto a otro», el mismo texto que
las leyendas de las Figuras 1.1 y 1.2 (ajuste U-FIG-EJEMPLO-AJUSTE; antes decía
«remisión resuelta entre puntos»). En el SVG cambió solo esa línea de texto.

## 4. Salidas

| Archivo | sha256 |
|---|---|
| `generar_figura_proceso_extraccion.py` | `6a91931abeb9927842f76fa50471497e926c69fc56617c62ef7f05ddf6c010d6` |
| `figura_proceso_extraccion.svg` | `168700921fa74b6b5449989408f09551372e5aee8ba0af9b4bcd44d70fe8ee5c` |
| `figura_proceso_extraccion.png` | `edb4db9ee37d05f96d33bdfff6a7103e802c16caa462ce159ade8332733bc7db` |

Generación determinística verificada: mismo SVG y mismo PNG con
`PYTHONHASHSEED` 0, 1, 2 y 3. Tamaños: rótulos 19 → 9,54 pt; subtextos, nodos y
leyenda 18 → 9,04 pt, a 12,75 cm de ancho. Verificación geométrica adicional
(script fuera del repositorio, en el paquete de revisión de
U-FIG-EJEMPLO-AJUSTE): 42 textos, 3 nodos, 11 trazos con flecha; ningún texto se
superpone con otro ni pisa un nodo, ningún trazo atraviesa un nodo.

## 5. Búsquedas del ejemplo (contexto, no dibujadas en esta figura)

Copiadas en `ejemplo_prestamo_datos.json` desde `reports/u_med_ejemplo/`
(commit `200462f`):

- Fragmentos, variante A (recalculada por el extractor): 5.1.1.1 en el puesto 2,
  3.7 en el 1.523; reproduce `umed2_analista_paso1_resultado.json` (sha256
  `a69c44b00a7f4920d1a4e5224167e6edacf4b7153d004d2185050cb2387f5408`, línea 11
  de `umed_manifest.txt`).
- Fragmentos, variante B, del mismo archivo: 5.1.1.1 en el puesto 5; 3.7 sin
  puntaje.
- Nodos, de `umed2_analista_paso3_resultado.json` (sha256
  `047e6f6e80b6b88e300cfb090bd2223ea967de8c9cbea9e10f9c04a9c168a3cd`, línea 18
  de `umed_manifest.txt`): nodos de 5.1.1.1 en los puestos 2, 4 y 156 de 2.346;
  ningún nodo de 3.7 con coincidencia.
