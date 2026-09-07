# figura_esquema_partida (F1) — registro de generación

Figura F1 del capítulo del esquema: tipos de entidad y matriz dominio/rango
del **esquema de partida** de la extracción v2 — 6 tipos visibles al extractor
más el pseudo-tipo `Sujeto` (catálogo cerrado) y 12 relaciones.

GENERADA POR SCRIPT desde el artefacto sellado, nunca dibujada a mano: el
script IMPORTA `data/experiment/grafo_v2/code/schema.py` y dibuja exactamente
lo que declaran `ENTITY_TYPES` y `DOMAIN_RANGE`; si los conteos no son los
sellados (6 tipos, 12 firmas), el script FRENA con AssertionError antes de
escribir. Comparte script, layout y convenciones con la figura F1b
(`figura_esquema_congelado.svg`, mismo directorio), para que ambas se comparen
lado a lado.

## 1. Comando de generación

```bash
python3 docs/tesis/figuras/generar_figuras_esquema.py
```

Escribe `figura_esquema_partida.svg` (850 × 590) y también
`figura_esquema_congelado.svg` (un solo script para las dos figuras garantiza
el layout idéntico). El PNG se exporta aparte:

```bash
rsvg-convert -z 2 -f png -o docs/tesis/figuras/figura_esquema_partida.png docs/tesis/figuras/figura_esquema_partida.svg
```

`rsvg-convert` (2.62.3) es la única herramienta externa, y solo para el PNG
(1700 × 1180 px). El SVG se produce con Python de la biblioteca estándar, sin
dependencias.

## 2. Fuentes y sellos

Archivos leídos (importados) por el script:

| Archivo | sha256 |
|---|---|
| `data/experiment/grafo_v2/code/schema.py` | `cc98e4354cf2ad507954f7fa99f12b8445e6157c9a0bcb026a13908e63de7eab` |

(El script también importa la cadena del esquema congelado para F1b; esos
sellos constan en `LEEME_figura_esquema_congelado.md`.)

Salidas de esta corrida:

| Archivo | sha256 |
|---|---|
| `figura_esquema_partida.svg` | `6dce982cb5c2efc4c9249806a68b350d25e609e2573a374800f4b22aa3a8b174` |
| `figura_esquema_partida.png` | `af4adf1830ff9a073d7b5deb18fdbcffcd4f0cf8f90815e789e72ef8af7eb8e0` |
| `generar_figuras_esquema.py` (script, versionado junto a la figura) | `0bd21b660ac049d9c456d4ffb058deab104afcd63bb51cf04b18837496fc326b` |

Generación determinística verificada: dos corridas consecutivas y tres
corridas con `PYTHONHASHSEED` distinto (1, 2, 3) producen el mismo SVG
(sha256 `6dce982c…`); toda iteración sobre conjuntos pasa por `sorted()`.

## 3. Convenciones de dibujo (declaradas)

- **Una flecha por par (tipo del dominio → tipo del rango)** de cada relación
  — la convención «una flecha por tipo de origen» del mandato, no la de «una
  flecha desde la zona». Cada par es un `<path>` propio del SVG con atributos
  `data-pred`/`data-dom`/`data-ran`, contable mecánicamente.
- **Troncos compartidos**: las flechas de una misma relación que comparten
  destino confluyen en un tronco con UNA punta y UN rótulo (`establecida_en`
  hacia `TextoOrdenado`, por sus dos accesos: comb izquierdo desde la zona
  deóntica y acceso derecho desde `Operacion`; `aplica_a` hacia `Sujeto`). El
  tramo de origen de cada flecha (el «diente») es el trazo propio de ese par.
- **Zonas**: «contenido deóntico» (`Obligacion`, `Restriccion`, `Excepcion`),
  «acto regulado» (`Operacion`, al centro de la composición) y «anclaje
  documental» (`TextoOrdenado`, `Comunicacion`).
- **Sujeto**: caja de borde discontinuo con la nota «catálogo cerrado (no lo
  emite el extractor)» — es un pseudo-tipo: el extremo sujeto de
  `aplica_a`/`ejecuta` se resuelve por catálogo, no por un tipo de entidad
  que el extractor emita (comentario de `DOMAIN_RANGE` en `schema.py`).
- **Rótulos** de relación en monoespaciada (equivalente de `\texttt`);
  identificadores del esquema tal cual, resto del texto en castellano.
- **Cruces de línea**: 5, todos entre trazos finos de trenzas distintas
  (2 del tronco de `aplica_a` con dientes de `establecida_en`; 3 del codo de
  `exceptua_obligacion` con las diagonales `regula`/`prohibe`/`limita`).
  Ninguna flecha pasa por encima de una caja.
- Paleta por tipo y tipografía heredadas de `generar_figura_norma_a_grafo.py`
  (mismo directorio); `Comunicacion` no existía en esa paleta y recibe
  `#6c584c`, declarado en el script.

## 4. Cajas y flechas contra la matriz

Cajas: **7** = 6 tipos de `ENTITY_TYPES` + pseudo-tipo `Sujeto`. Recomputo:
`python3 -c "import sys; sys.path.insert(0,'data/experiment/grafo_v2/code'); import schema; print(len(schema.ENTITY_TYPES))"`.

Flechas: **17** = expansión dominio × rango de las **12 firmas** de
`DOMAIN_RANGE`, todas presentes y ninguna de más — el script lo asserta por
igualdad de conjuntos entre los paths emitidos y la expansión de la matriz, y
se recomputa sobre el SVG con:
`python3 -c "import re; print(sorted(__import__('collections').Counter(re.findall(r'data-pred=\"([^\"]+)\"', open('docs/tesis/figuras/figura_esquema_partida.svg').read())).items()))"`

| Firma | Dominio → Rango (matriz) | Flechas |
|---|---|---|
| `establecida_en` | {Excepcion, Obligacion, Operacion, Restriccion} → TextoOrdenado | 4 |
| `referencia` | TextoOrdenado → Comunicacion | 1 |
| `modificada_por` | TextoOrdenado → Comunicacion | 1 |
| `aplica_a` | {Obligacion, Restriccion} → Sujeto | 2 |
| `regula` | {Obligacion, Restriccion} → Operacion | 2 |
| `exceptua` | Excepcion → Restriccion | 1 |
| `exceptua_obligacion` | Excepcion → Obligacion | 1 |
| `prohibe` | Restriccion → Operacion | 1 |
| `limita` | Restriccion → Operacion | 1 |
| `ejecuta` | Sujeto → Operacion | 1 |
| `requiere` | Operacion → Obligacion | 1 |
| `condiciona` | Obligacion → Operacion | 1 |
| **Total** | **12 firmas** | **17** |

## 5. Composición y tamaño de letra impreso

| Magnitud | Valor |
|---|---|
| Ancho del SVG | 850 px |
| Alto del SVG | 590 px |
| PNG exportado | 1700 × 1180 px |

A 0,85`\linewidth` con 15 cm de ancho de texto: 0,85 × 15 cm × 28,3465 pt/cm
= **361,4 pt**, de modo que `N` px se imprimen a `N × 361,4 / 850` puntos:

| Elemento | Tamaño en el SVG | Tamaño impreso a 0,85\linewidth |
|---|---|---|
| Nombre de tipo (mono, bold) | 19 px | 8,08 pt |
| Rótulo de relación (mono) | 15 px | 6,38 pt |
| Rótulo de zona / nota de Sujeto | 15 px | 6,38 pt |

(Referencia: la figura `figura_norma_a_grafo` sellada imprime sus rótulos de
arista a 6,43 pt.)

## 6. Verificaciones ejecutadas (todas dentro del script; cualquier falla FRENA)

- 12 firmas y 6 tipos en la fuente importada; 17 pares en la expansión.
- Biyección exacta entre las rutas dibujadas y la expansión de la matriz
  (ni una flecha de menos ni de más), re-verificada sobre el marcado emitido
  vía los atributos `data-*`.
- Sin nombres internos en el texto visible del SVG: `sha`, `test`, `.py`,
  `.json`, `congelado`, `retocado` (por palabra completa) dan cero
  coincidencias sobre el contenido de los elementos `<text>`.
- Determinismo: 2 corridas consecutivas + 3 con `PYTHONHASHSEED` 1/2/3 →
  mismo sha256.
