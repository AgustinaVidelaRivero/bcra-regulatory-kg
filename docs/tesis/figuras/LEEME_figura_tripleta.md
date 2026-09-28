# figura_tripleta — registro de generación (Figura 2.1)

Figura «anatomía de una tripleta» para el marco teórico (§2.1.1), con el
ejemplo del préstamo: la Restriccion del monto del punto 5.1.1.1 del Texto
Ordenado de Clasificación de deudores —`limita`→ la Operacion del mismo punto.
Dos nodos con su etiqueta del grafo, completa, y «punto 5.1.1.1»; la arista con
el nombre de la relación tal como está en el grafo; tres llamadas en gris
(«nodo de origen · tipo Restriccion · punto 5.1.1.1», «relación · nombre y
dirección», «nodo de destino · tipo Operacion · punto 5.1.1.1»). Sin leyenda.

Historia: generada el 2026-09-28 en U-FIG-EJEMPLO, que reemplazó la versión con
el ejemplo de los dividendos (Restricción —limita→ Operación del punto 3.17.1.4
de Exterior y Cambios: generador, SVG y PNG del commit `952b78a`). En
U-FIG-EJEMPLO-AJUSTE (mismo día) la figura no cambió: SVG y PNG siguen idénticos
(sha256 de §4); cambiaron solo las rutas de las fuentes que cita este LEEME. La
versión de U-FIG-EJEMPLO no llegó a commitearse: al cierre del ajuste,
`git status` mostraba estos archivos como modificados respecto de `952b78a`.

## 1. Comandos de generación

```bash
PYTHONDONTWRITEBYTECODE=1 python3 docs/tesis/figuras/extraer_datos_ejemplo_prestamo.py
PYTHONDONTWRITEBYTECODE=1 python3 docs/tesis/figuras/generar_figura_tripleta.py --verificar
```

El generador escribe `figura_tripleta.svg` (lienzo 720 × 224) y exporta el PNG
con `rsvg-convert` 2.62.3 (1506 × 469 px, 300 dpi). Con `--verificar` mide cada
texto con las métricas reales de Helvetica: 11 textos medidos, 0 fallas.

## 2. Grafo, pregunta y fuentes

- Grafo: KG-Reextraído-r1,
  `data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json`, sha256
  `0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a` (candado
  `KG_SHA256`; el script exige además que el JSON del ejemplo se haya extraído
  de ese mismo archivo).
- Pregunta del ejemplo (no aparece en esta figura; es la de la Figura 1.2): «Para
  una entidad financiera, ¿qué condiciones hacen que los créditos para consumo o
  vivienda deban clasificarse en la cartera comercial?»

Los dos nodos y la arista se leen de `ejemplo_prestamo_datos.json` (sha256
`25ab7b4c0d76fd735244fe0fecc17ceaba1b0e8bfd2312e7aa3cbd5c849672a2`, escrito por
`extraer_datos_ejemplo_prestamo.py`, sha256
`4c3a441972d27304b6d58d0664dbc15b893bce7ad3e7d2d49afad947f51eeea7`) y se
comprueban en `kg.json`:

| Clave | Nodo (clave en el JSON) | Tipo | Punto | Etiqueta en el grafo (dibujada completa) | id |
|---|---|---|---|---|---|
| R | restriccion_monto | Restriccion | 5.1.1.1 | Créditos consumo/vivienda — monto supera dos veces importe referencia (69 caracteres) | `Restriccion_los_creditos_para_consumo_o_vivienda_que_superen_el_equivalente_a_dos_veces_el_i_f682b1` |
| OP | operacion | Operacion | 5.1.1.1 | Inclusión en cartera comercial — créditos consumo/vivienda (58 caracteres) | `Operacion_inclusion_en_cartera_comercial_creditos_consumo_vivienda_2644e8` |

Arista: `kg['edges'][15772]`, R `limita` OP, única con ese origen, relación y
destino; índice igual al que declara el JSON; firma (Restriccion, limita,
Operacion) admitida por la matriz de dominio y rango del esquema congelado; sin
`rol_fuente` (es de extracción, no de la resolución de remisiones); procedencia
`cla::5.1.1.1`, página 16; ninguna arista en sentido inverso.

Qué está escrito a mano: ningún dato del ejemplo; solo los textos fijos de las
llamadas, con tipo y punto tomados de lo resuelto.

Las mediciones del ejemplo que el JSON resume están versionadas en
`reports/u_inv_ejemplo/` (commit `24e0116`), `reports/u_med_ejemplo/` (commit
`200462f`) y `reports/u_inv_candidatos/` (commit `791166d`); antes estaban en
`/tmp/u_inv_ejemplo/`, `/tmp/u_med_ejemplo/` y `/tmp/u_inv_candidatos/`.

## 3. Composición

- Etiquetas completas del grafo, sin abreviar, envueltas a 40 caracteres por
  línea y hasta tres líneas (`LINEAS_ETIQUETA` = 3); el script comprueba que lo
  dibujado, unido, es la etiqueta del grafo.
- Tipos en las llamadas escritos como en el código, sin tildes.
- El índice de la arista se lee del JSON y se coteja con `kg.json`.
- Tamaños: nodos y rótulo 17 → 8,53 pt; llamadas 15 → 7,53 pt, a 12,75 cm.
- Verificación geométrica adicional (script fuera del repositorio, en el
  paquete de revisión de U-FIG-EJEMPLO-AJUSTE): 11 textos, 2 nodos, 1 trazo con
  flecha; ningún texto se superpone con otro ni pisa un nodo, ningún trazo
  atraviesa un nodo.

## 4. Salidas

| Archivo | sha256 |
|---|---|
| `generar_figura_tripleta.py` | `0bd7ba14c8460d8c033f57511b4ccefef051f7b81743309cea49ef9809ba5c4f` |
| `figura_tripleta.svg` | `709f1e30e7588742d9a41b6bb0b0e73fa46442acbdda9221866ee2cd50785b80` |
| `figura_tripleta.png` | `bb97e7b6dc295abda2fed97df60acc36b1c58a4b06b8ddaa27f0d9cb32edd503` |

Generación determinística verificada: mismo SVG y mismo PNG con
`PYTHONHASHSEED` 0, 1, 2 y 3.

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
