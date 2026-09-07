# figura_esquema_congelado (F1b) — registro de generación

Figura F1b del capítulo del esquema: tipos de entidad y matriz dominio/rango
del **esquema congelado** del gate ESQ-3 — 9 tipos más el pseudo-tipo `Sujeto`
y 13 relaciones (`condicion_de` nuevo; `establecida_en` y `aplica_a` con
dominio ampliado). Mismo script, layout y convenciones que F1
(`figura_esquema_partida.svg`), para compararlas lado a lado; lo agregado en
la validación va resaltado.

GENERADA POR SCRIPT desde los artefactos sellados, nunca dibujada a mano. El
script IMPORTA `prompt_congelado.py`; esa importación ejecuta los candados de
la cadena sellada (hash del prefijo v2 `2c1b76d1685d`, anclas únicas de los
reemplazos, remoción completa de `requisito_de_estructura`): si la cadena no
es la sellada, la corrida FRENA antes de dibujar.

## 1. Comando de generación

```bash
python3 docs/tesis/figuras/generar_figuras_esquema.py
```

Escribe `figura_esquema_congelado.svg` (850 × 810) y también
`figura_esquema_partida.svg` (un solo script para las dos figuras garantiza el
layout idéntico). El PNG se exporta aparte:

```bash
rsvg-convert -z 2 -f png -o docs/tesis/figuras/figura_esquema_congelado.png docs/tesis/figuras/figura_esquema_congelado.svg
```

`rsvg-convert` (2.62.3) es la única herramienta externa, y solo para el PNG
(1700 × 1620 px). El SVG se produce con Python de la biblioteca estándar, sin
dependencias.

## 2. Fuentes y sellos

Archivos leídos (importados) por el script:

| Archivo | sha256 |
|---|---|
| `data/experiment/esq/code/prompt_congelado.py` | `a5a4ba330a02b2b8ce885716e242dafabb84f62463d25c046dc6ff7d40f40710` |
| `data/experiment/esq/code/prompt_esq3b.py` | `c66aa6aa578322214d197fe4855b56455fb25d39b4d20db2f96c3b432ad606bf` |
| `data/experiment/esq/code/prompt_esq3b_v2.py` | `a3201ced14be6ecc00f6208f5e28c5777e5b1c9a2ff2a07c58a242dd3faa5a83` |
| `data/experiment/grafo_v2/code/schema.py` | `cc98e4354cf2ad507954f7fa99f12b8445e6157c9a0bcb026a13908e63de7eab` |

Derivación de la matriz (asertada por el script): la matriz retocada vive
como literal en `prompt_esq3b.py` (`DOMAIN_RANGE_RETOCADO`, 14 firmas);
`prompt_esq3b_v2.py` la toma sin la fila `exceptua_operacion` (R6a rechazado,
14 → 13) y `prompt_congelado.py` toma la del v2 sin cambio alguno. El script
asserta `DOMAIN_RANGE_CONGELADO == DOMAIN_RANGE_RETOCADO − exceptua_operacion`
— el vínculo entre la fuente operativa (congelado) y el literal retocado.

Salidas de esta corrida:

| Archivo | sha256 |
|---|---|
| `figura_esquema_congelado.svg` | `4be96296a64f7243b1b47facf80bbee678668fb302be2b5225110c2477edd30a` |
| `figura_esquema_congelado.png` | `90259a388fa146bcd80e8bf22b97200d47c19bd5f38027d14dfb5e54be110995` |
| `generar_figuras_esquema.py` (script, versionado junto a la figura) | `0bd21b660ac049d9c456d4ffb058deab104afcd63bb51cf04b18837496fc326b` |

Generación determinística verificada: dos corridas consecutivas y tres
corridas con `PYTHONHASHSEED` distinto (1, 2, 3) producen el mismo SVG
(sha256 `4be96296…`).

## 3. Convenciones de dibujo (declaradas)

Las de F1 (`LEEME_figura_esquema_partida.md` §3) más las propias de F1b:

- **Resalte «agregado en la validación»** (magenta `#b5179e`, ausente de la
  paleta de tipos; trazo 2,6 px vs 1,6 px del base): los 3 tipos nuevos
  (`Potestad`, `Condicion`, `Definicion` — borde y relleno tintado), las 3
  flechas de `condicion_de`, y las 6 ampliaciones de dominio (3 de
  `establecida_en`: Potestad/Condicion/Definicion; 3 de `aplica_a`:
  Operacion/Excepcion/Potestad). Leyenda al pie.
- **Resalte en troncos compartidos**: cuando una flecha nueva confluye en el
  tronco de una relación preexistente, el TRAMO DE ORIGEN (diente) porta el
  resalte y el tronco compartido conserva el color base — la relación no es
  nueva; su ampliación sí. `condicion_de` es relación nueva y va resaltada
  entera. El acceso `aplica_a` desde `Operacion` es un trazo propio completo
  (resaltado entero, con rótulo propio).
- **Zona propia para `Definicion`** («contenido definitorio»): la prosa
  sellada NO la clasifica como acto regulado — la delimitación de R3 en
  `prompt_esq3b.py` dice que `Definicion` «es SOLO para definienda que no son
  actos ni prescripciones — clases, conjuntos, conceptos y parámetros» y que
  si el definiendum es un acto regulado «va en **Operacion**». Tampoco es
  contenido deóntico (por sí sola no prescribe). Ante ese texto, va en zona
  propia, como manda el mandato para el caso no claro, y acá queda declarado.
- **Layout idéntico a F1 con altura mayor**: las 6 cajas compartidas, las
  zonas y todas las rutas comunes conservan posición y convención; F1b agrega
  `Potestad` y `Condicion` como filas nuevas al pie de la zona deóntica,
  `Definicion` en su zona (columna derecha), y por eso `Sujeto` y la banda
  inferior bajan (590 → 810 px de alto; el ancho, 850 px, es el mismo).
- **Cruces de línea**: 13, todos entre trazos finos de trenzas distintas
  (4 del tronco de `aplica_a` con dientes de `establecida_en`; 5 de los
  dientes de `condicion_de` con los troncos de `establecida_en`/`aplica_a`;
  1 de la salida de `condicion_de` con el tronco de `aplica_a`; 3 del codo de
  `exceptua_obligacion` con las diagonales `regula`/`prohibe`/`limita`).
  Ninguna flecha pasa por encima de una caja.

## 4. Cajas y flechas contra la matriz

Cajas: **10** = 9 tipos de `ENTITY_TYPES_CONGELADO` + pseudo-tipo `Sujeto`.
Recomputo: `python3 -c "import sys; sys.path.insert(0,'data/experiment/esq/code'); import prompt_congelado as pc; print(len(pc.ENTITY_TYPES_CONGELADO))"`.

Flechas: **26** = expansión dominio × rango de las **13 firmas** de
`DOMAIN_RANGE_CONGELADO`, todas presentes y ninguna de más (assert de
biyección del script, recomputable sobre el SVG con el one-liner del §4 del
LEEME de F1, cambiando el nombre de archivo). De las 26, **9 son nuevas**
respecto de F1 (assert del script) y van resaltadas.

| Firma | Dominio → Rango (matriz) | Flechas | Nuevas |
|---|---|---|---|
| `establecida_en` | {Condicion, Definicion, Excepcion, Obligacion, Operacion, Potestad, Restriccion} → TextoOrdenado | 7 | 3 (Potestad, Condicion, Definicion) |
| `referencia` | TextoOrdenado → Comunicacion | 1 | — |
| `modificada_por` | TextoOrdenado → Comunicacion | 1 | — |
| `aplica_a` | {Excepcion, Obligacion, Operacion, Potestad, Restriccion} → Sujeto | 5 | 3 (Operacion, Excepcion, Potestad) |
| `regula` | {Obligacion, Restriccion} → Operacion | 2 | — |
| `exceptua` | Excepcion → Restriccion | 1 | — |
| `exceptua_obligacion` | Excepcion → Obligacion | 1 | — |
| `prohibe` | Restriccion → Operacion | 1 | — |
| `limita` | Restriccion → Operacion | 1 | — |
| `ejecuta` | Sujeto → Operacion | 1 | — |
| `requiere` | Operacion → Obligacion | 1 | — |
| `condiciona` | Obligacion → Operacion | 1 | — |
| `condicion_de` | Condicion → {Excepcion, Obligacion, Restriccion} | 3 | 3 (relación nueva) |
| **Total** | **13 firmas** | **26** | **9** |

## 5. Composición y tamaño de letra impreso

| Magnitud | Valor |
|---|---|
| Ancho del SVG | 850 px |
| Alto del SVG | 810 px |
| PNG exportado | 1700 × 1620 px |

Mismo ancho que F1, así que los tamaños impresos a 0,85`\linewidth` son los
de la tabla del §5 del LEEME de F1 (nombre de tipo 8,08 pt; rótulos 6,38 pt).

## 6. Verificaciones ejecutadas (todas dentro del script; cualquier falla FRENA)

- Candados de la cadena sellada, ejecutados por la importación de
  `prompt_congelado.py`.
- 13 firmas y 9 tipos en la fuente importada; conjunto de tipos == el de F1
  ∪ {Potestad, Condicion, Definicion}; 26 pares en la expansión; 9 nuevos
  respecto de F1; las 17 flechas de F1 contenidas en las 26 de F1b.
- `DOMAIN_RANGE_CONGELADO == DOMAIN_RANGE_RETOCADO − exceptua_operacion`.
- Biyección exacta entre las rutas dibujadas y la expansión de la matriz,
  re-verificada sobre el marcado emitido vía los atributos `data-*`.
- Sin nombres internos en el texto visible del SVG (`sha`, `test`, `.py`,
  `.json`, `congelado`, `retocado`, por palabra completa: cero coincidencias
  en `<text>`).
- Determinismo: 2 corridas consecutivas + 3 con `PYTHONHASHSEED` 1/2/3 →
  mismo sha256.
