# Scoping de B5.6 — módulo de extracción tabular y destino del bloque de régimen informativo

Unidad **U-B5.6-0**. Diagnóstico puro: **USD 0**, cero llamadas a API, cero
implementación, cero cambios de comportamiento. Ningún archivo del pipeline fue
tocado (E0, cuarteto de evaluación, `kg.json` y `reextraccion_v2/` intactos: se
abrieron en modo lectura y se importaron regex sin modificarlas).

Esta unidad responde la condición que el laudo ESQ-1 §D10 pone sobre la dirección
de validar el esquema sobre el corpus completo: *«cuántos de los 53 TOs tienen
tablas parseables, qué unidad de extracción produce el parser sobre una muestra,
si esa unidad es compatible con el esquema vigente o exige tratamiento propio, y
cuánto trabajo es construir el módulo»* (`docs/laudo_ESQ-1_diseno.md`, D10, *Lo
que este laudo NO compromete*). **No decide el alcance**: entrega el número con
el que esa decisión se lleva a los mentores.

Anclas verificadas contra el árbol de trabajo en `HEAD = 94bb7a7`. Durante la
unidad HEAD avanzó a `38be6e5` (pre-registro de ESQ-1, sellado por la autora en
paralelo); se re-verificó contra ese HEAD que las zonas selladas siguen
byte-intactas (`git diff --stat HEAD -- data/experiment/reextraccion_v2/
data/experiment/grafo_v2/ data/experiment/evaluacion/` sin salida) y que
`kg.json` conserva su sha `0226e947…`. Todo número lleva el archivo:línea o el
comando que lo reproduce. Lo no verificable se marca como supuesto, no se
infiere.

---

## 0. Resumen ejecutivo

*Nota de sincronía:* mientras corría esta unidad se selló el pre-registro de
ESQ-1 (`38be6e5`), cuyo mensaje registra como observación no predicha el mismo
material que §3.2 mide acá. Los dos conteos concilian exactamente (§3.2).

1. **El censo desmiente el diagnóstico de una sola causa.** El bloque son 53 TOs
   y 3.435 páginas, y produce **105 unidades en 5 TOs**; 48 producen cero. Pero la
   causa proximal del cero **no es la estructura tabular**: es la compuerta de rol
   de página de E0. **47 de 53 TOs tienen el 100 % de sus páginas clasificadas
   `portada`** porque no existe una página que matchee `RE_MARCA_INDICE`
   (`e0_lib.py:101`, aplicada en `:206-207`), y `parsear_cuerpo` saltea todo lo que
   no es `ROL_CUERPO` (`e0_lib.py:343`). Sin índice no hay cuerpo; sin cuerpo no
   hay nada que chunkear, haya o no haya tablas (§1.3).
2. **La estructura tabular es real pero minoritaria.** Sólo el **12,4 %** de las
   palabras del bloque cae dentro de una tabla de contenido (69.543 de 562.622), y
   **21 de 53 TOs no tienen ni una sola**. Las tres piezas más grandes del bloque
   —`manual` (2.037 pág.), `ri2_pm` (376) y `plandecuentas` (77), el **72,5 %** de
   las páginas— no son grillas: son **fichas de cuenta contable** (encabezado
   clave-valor + prosa de valuación) y **listas de código-denominación** (§1.4).
3. **El bloque tiene cinco familias estructurales, no dos.** Íntegramente
   tabulares: **5 TOs / 150 pág.** Prosa mezclada con tablas: **18 TOs / 596 pág.**
   Fichas: **3 TOs / 2.436 pág.** Lista de códigos: **1 TO / 77 pág.** Prosa lisa
   sin tabla: **26 TOs / 176 pág.** (§1.4, tabla completa).
4. **`extract_tables` funciona bien donde hay grilla dibujada y falla donde no la
   hay.** Sobre `ri_laft` devuelve 43 tablas limpias de 2 columnas (código →
   descripción) con 1,8 % de celdas vacías; sobre `ric::3.1.4` —la tabla de
   ponderadores del único TO de régimen informativo que el pipeline sí digirió—
   **colapsa los 19 ponderadores en una sola celda** (§2.2).
5. **Y donde falla, dos reglas de alineación igualmente razonables discrepan en
   17 de 20 filas.** Medido sobre las coordenadas reales de esa página: la columna
   de ponderadores es un bloque tipográfico independiente, con paso vertical
   distinto al de los conceptos. El emparejamiento fila↔valor **no está
   determinado por la geometría** (§2.3). Esto no es una objeción teórica: es la
   forma general de RX-10 (`docs/backlog_reextraccion.md:267-292`), el defecto que
   ya invirtió dos montos en el grafo.
6. **El esquema vigente NO alcanza para una tabla de ponderadores, y la evidencia
   ya está paga.** `ric::3.1.4` produjo **2 nodos y ningún ponderador** en el grafo
   vigente, y el propio extractor lo declaró por escrito en `omisiones_no_prosa`.
   Faltan dos cosas distintas: un **tipo de entidad** para la fila informativa
   (los 6 tipos son todos deónticos) y un **predicado con atributo** (`RelationOut`
   no tiene campo `properties`: `schema.py:220-235`). Reparar sólo el parser sin
   tocar el esquema mueve el problema, no lo resuelve (§3).
7. **B5.6 tal como está escrito en el plan no desbloquea el bloque.**
   `plan_tesis.md:358` lo define como «módulo de tablas (pdfplumber
   `extract_tables` con provenance, sin LLM) […] decide el destino del bloque RI».
   Un módulo de tablas resuelve como mucho el 12,4 % de las palabras del bloque.
   Lo que desbloquearía las familias PROSA y MIXTO (44 TOs, 772 pág.) es un **modo
   estructural sin raíz de sección** en E0 —hay 2.522 labels de punto numerados
   contra sólo 237 headers `Sección N.` (§1.5)—, y lo que desbloquearía la familia
   FICHA (2.436 pág.) es un **tercer parser**, de registro, que no es ni prosa ni
   tabla (§4).
8. **Recomendación: partir B5.6 en tres piezas con gates independientes y llevar
   a los mentores una frontera, no un todo-o-nada** (§6). La pieza barata y de
   mayor rendimiento **no es el módulo de tablas**.

---

## 1. Censo del bloque de régimen informativo

### 1.1 Qué son los 53 y de dónde sale la categoría

La categoría no es una heurística: viene de la sección del índice oficial del
BCRA de la que se descargó cada PDF
(`escalado_prep/code/construir_inventario.py:42-45`, `CATEGORIAS = [(…),
("regimen_informativo", "regimenes_informativos")]`). El inventario congela 152
TOs, 99 de normativa general y 53 de régimen informativo
(`escalado_prep/inventario_resumen.json`, clave `por_categoria`).

```bash
python3 -c "import json; print(json.load(open('data/experiment/escalado_prep/inventario_resumen.json'))['por_categoria'])"
```
→ `{'normativa_general': 99, 'regimen_informativo': 53}`

### 1.2 Los conteos duros

Sobre `escalado_prep/inventario_unidades.csv` (152 filas, producido por el E0 en
seco de `escalado_prep/code/correr_e0_seco.py`):

| | régimen informativo | normativa general |
|---|--:|--:|
| TOs | **53** | 99 |
| páginas | **3.435** | 3.322 |
| páginas de cuerpo (rol `cuerpo` de E0) | **235** | 2.251 |
| secciones detectadas | **27** | 488 |
| chunks terminales | **96** | 6.574 |
| mini-chunks | **9** | 1.331 |
| **unidades de extracción** | **105** | **7.905** |
| caracteres propios | 291.211 | 4.173.260 |
| veredicto `digerible` | **0 de 53** | 68 de 99 |
| TOs que producen **cero** unidades | **48** | 14 |

```bash
python3 - <<'PY'
import csv, collections
rows=list(csv.DictReader(open('data/experiment/escalado_prep/inventario_unidades.csv')))
ri=[r for r in rows if r['categoria']=='regimen_informativo']
print(len(ri), sum(int(r['paginas']) for r in ri), sum(int(r['paginas_cuerpo']) for r in ri),
      sum(int(r['unidades_extraccion']) for r in ri),
      collections.Counter(r['veredicto'] for r in ri),
      sum(1 for r in ri if int(r['unidades_extraccion'])==0))
PY
```
→ `53 3435 235 105 Counter({'necesita reglas': 53}) 48`

Los cinco que producen algo:

| id | páginas | pág. cuerpo | secciones | unidades |
|---|--:|--:|--:|--:|
| `ri_cc` | 118 | 68 | 6 | 33 |
| `ri_rml` | 77 | 76 | 6 | 27 |
| `ri_pgn` | 19 | 18 | 7 | 19 |
| `ri_gerc` | 8 | 7 | 3 | 15 |
| `ri_ai` | 9 | 8 | 5 | 11 |

### 1.3 Por qué producen cero — con archivo:línea

**La causa proximal es el rol de página, no la tabla.** El laudo ESQ-1 §D10
atribuye el cero a *«la estructura tabular de esos documentos, que la etapa E0 no
procesa»*. Los archivos dicen algo más preciso, y se reporta la diferencia
(CLAUDE.md §4.d).

La cadena es esta:

1. `clasificar_paginas` (`e0_lib.py:179-211`) sólo marca `ROL_CUERPO` **después**
   de haber visto una página de índice. La rama que decide es
   `e0_lib.py:206-207`:
   ```python
   elif not visto_indice:
       rol = ROL_PORTADA
   ```
   y `visto_indice` sólo se enciende con `RE_MARCA_INDICE`
   (`e0_lib.py:101`): `^-\s*[ÍI]ndice\s*[-–]?\s*$`.
2. `parsear_cuerpo` (`e0_lib.py:342-343`) descarta toda página que no sea cuerpo:
   ```python
   if rol != ROL_CUERPO:
       continue
   ```
3. Sin páginas de cuerpo no hay secciones; sin secciones, `construir_chunks`
   (`e0_lib.py:1030`) recorre una lista vacía. Cero unidades.

Medición sobre la corrida en seco ya persistida
(`escalado_prep/e0_dry/conteos_e0_dry.json`, clave `roles_pagina`):

```bash
python3 - <<'PY'
import json, csv, collections
c=json.load(open('data/experiment/escalado_prep/e0_dry/conteos_e0_dry.json'))
cat={r['id']:r['categoria'] for r in csv.DictReader(open('data/experiment/escalado_prep/inventario_unidades.csv'))}
ri=[k for k in c if cat[k]=='regimen_informativo']
agg=collections.Counter()
for k in ri: agg.update(c[k]['roles_pagina'])
print(dict(agg))
print('con paginas_cuerpo==0:', sum(1 for k in ri if c[k]['paginas_cuerpo']==0))
print('con 100% portada:', sum(1 for k in ri if set(c[k]['roles_pagina'])=={'portada'}))
PY
```
→ `{'portada': 3191, 'cuerpo': 235, 'indice': 9}`
→ `con paginas_cuerpo==0: 47`
→ `con 100% portada: 47`

**47 de 53 TOs tienen el 100 % de sus páginas en rol `portada`.** No llegan
siquiera a la etapa donde una tabla podría estorbar.

Y no es una variante de escritura del marcador: esos documentos **no tienen
página de índice**. Verificado sobre las primeras 12 páginas de cuatro casos:

```bash
python3 - <<'PY'
import pdfplumber, re
for ident in ('ri_laft','ri_pnp','ri_dcpc','ri_ccna'):
    with pdfplumber.open(f'data/experiment/escalado_prep/pdfs/{ident}.pdf') as pdf:
        hits=[(pi,[l for l in (pg.extract_text() or '').split('\n') if re.search(r'[íÍiI]ndice',l)][:1])
              for pi,pg in enumerate(pdf.pages[:12],1) if re.search(r'[íÍiI]ndice', pg.extract_text() or '')]
    print(ident, hits)
PY
```
→ `ri_laft []` · `ri_pnp []` · `ri_dcpc [(10, ['para aquellos que sean actualizables por algún índice.'])]`
→ `ri_ccna [(1, ['- Indice-'])]`

Consecuencia para el plan: **B5.2 no alcanza.** `plan_tesis.md:354` propone
relajar el regex («`Índice` sin guiones con guarda»). En estos documentos no hay
nada que relajar: la palabra no está. `ri_dcpc` es el caso que lo muestra en
negativo —la única aparición de «índice» en sus primeras diez páginas es prosa
sobre índices de actualización, y un regex más laxo lo tomaría como marcador—.

**El segundo modo de falla, separado del primero.** `ri_ccna` sí tiene índice
(`- Indice-`, que sí matchea `RE_MARCA_INDICE` porque el regex es
`re.IGNORECASE` y admite la falta de acento) y por eso llega a **58 páginas de
cuerpo**. Produce igual **cero** unidades: tiene **0 líneas** que matcheen
`RE_SECCION` (`e0_lib.py:104`), y sin sección abierta ningún punto numerado puede
colgarse —`parsear_cuerpo` rechaza todo label cuyo primer componente no coincida
con el número de la sección vigente (`e0_lib.py:412`,
`motivo = f"fuera_de_seccion_{seccion.numero}"`)—.

Los dos modos de falla y sus poblaciones (medido sobre los 53):

| modo | condición | TOs |
|---|---|--:|
| A — sin página de índice | `paginas_con_marca_indice == 0` | **47** |
| B — con índice pero sin `Sección N.` | índice sí, `headers_seccion == 0` | **1** (`ri_ccna`) |
| C — llega a producir unidades | — | **5** |

### 1.4 Íntegramente tabulares vs. prosa mezclada — con la regla declarada

El mandato pide distinguir los dos grupos con su conteo. Para hacerlo hace falta
una medida de tabularidad que no dependa de E0 (que no llega a mirar estos
documentos). Se midió con `pdfplumber.find_tables()` **sobre las 3.435 páginas,
sin muestreo**, y se descartaron las «tablas» que son el banner `B.C.R.A.` y el
pie `Versión / Comunicación / Vigencia / Página` —que `find_tables` detecta como
tablas de 1 fila en todas las páginas del corpus—.

**Regla de tabla de contenido (declarada):** ≥3 filas, ≥2 columnas, y bbox no
contenido íntegramente en el 12 % superior ni en el 10 % inferior de la página.
Script: `censo_ri2.py` del paquete de revisión.

Totales del bloque con esa regla:

| medida | valor |
|---|--:|
| tablas de contenido | **536** |
| páginas con ≥1 tabla de contenido | **418** de 3.435 (12,2 %) |
| filas de tabla | **8.304** |
| celdas | 56.699 (40.392 vacías, 71,2 %) |
| palabras dentro de tabla de contenido | **69.543** de 562.622 → **12,4 %** |
| TOs con **cero** tablas de contenido | **21** de 53 |

Sobre esa medida más tres señales léxicas —línea de código de cuenta, línea de
campo de ficha contable, línea de prosa larga: reglas y cortes en
`familias_ri.py`— el bloque se parte en **cinco** familias. Los cortes son
convencionales y se declaran como tales: sirven para contar grupos, no para
decidir nada por sí solos.

| familia | criterio | TOs | páginas | % pág. | filas de tabla | labels de punto | headers `Sección` | unidades hoy |
|---|---|--:|--:|--:|--:|--:|--:|--:|
| **TABULAR** | ≥40 % de palabras en tabla | **5** | 150 | 4,4 % | 3.266 | 92 | 8 | 0 |
| **MIXTO** | ≥15 % de palabras en tabla | **18** | 596 | 17,4 % | 4.564 | 1.794 | 222 | 105 |
| **FICHA** | ≥2 % de líneas de campo de ficha | **3** | **2.436** | **70,9 %** | 252 | 29 † | 5 † | 0 |
| **LISTA_CODIGOS** | ≥30 % de líneas de código | **1** | 77 | 2,2 % | 0 | 0 | 0 | 0 |
| **PROSA** | resto | **26** | 176 | 5,1 % | 222 | 607 | 2 | 0 |

† `manual` (2.037 pág.) y `ri2_pm` (376 pág.) **no fueron sondeados** por la
probe de espina numérica (§1.5) para acotar el tiempo de cómputo; su fila de
labels/headers sólo cuenta a `ri_transpa`. Se marca como no medido.

Respuesta directa al mandato: **íntegramente tabulares son 5 TOs (150 páginas);
con prosa mezclada con tablas, 18 TOs (596 páginas); y 30 TOs (2.689 páginas,
78 % del bloque) no son ninguna de las dos cosas** — son fichas, listas de
códigos o prosa lisa.

Detalle por TO en `censo_ri_familias.csv` del paquete de revisión.

**El punto que más pesa sobre la decisión de alcance:** las tres piezas más
grandes del bloque no son tablas.

- `manual.pdf` — 2.037 páginas, **0,3 %** de palabras en tabla, 12 tablas de
  contenido en total. Su estructura es un **registro clave-valor + prosa**:
  ```
  Capítulo            Activo
  Rubro               Otros Créditos por Intermediación Financiera
  Moneda/Residencia   En Pesos – Residentes en el País        Código
  Otros Atributos     Capitales                               141112
  Imputación          Otras Compras a Término
  Incluye los derechos emergentes de las compras a término no previstas en otras cuentas. …
  ```
  (`manual.pdf` p. 501, `pdfplumber.extract_text()`). El 30,6 % de sus líneas
  abren un campo de ficha.
- `ri2_pm.pdf` — 376 páginas, **0,0 %** en tabla, misma estructura de ficha
  (30,4 % de líneas de campo).
- `plandecuentas.pdf` — 77 páginas, **0,0 %** en tabla; el **79,9 %** de sus
  líneas es `código denominación` en texto plano:
  ```
  311106 Cuentas corrientes sin interés
  311112 Cuentas corrientes con interés
  ```
  (p. 31). Es una jerarquía de cuentas, no una grilla.

### 1.5 ¿Hay espina estructural que enganchar si se abre la compuerta?

Probe determinística sobre 51 de los 53 (se excluyeron `manual` y `ri2_pm` por
costo de cómputo; se declara): cuántas líneas serían **label de punto** para E0
(`RE_NUM_TOKEN` / `RE_NUM_TOKEN_SIN_PUNTO` como primer token, con resto no vacío)
y cuántas **header de sección** (`RE_SECCION`). Script `espina_ri.py`.

| medida | valor |
|---|--:|
| TOs con ≥1 label de punto | **42** de 51 sondeados |
| TOs con ≥1 header `Sección N.` | **10** de 51 |
| TOs con página de índice (sobre los 53) | **6** |
| labels de punto totales | **2.522** |
| headers de sección totales | **237** |

Lectura: la numeración jerárquica de puntos **sí existe** en la gran mayoría del
bloque; lo que no existe es la **raíz de sección** sobre la que E0 cuelga todo.
El modelo estructural de E0 es `Sección N.` → `N.x.y`, y rechaza por construcción
cualquier punto sin sección abierta (`e0_lib.py:412`). Ésa —y no la tabla— es la
pieza que le falta a la mayor parte del bloque.

---

## 2. Muestra de parseo con `pdfplumber.extract_tables`

Exploración de lectura. Ningún archivo del pipeline se tocó. Script
`muestra_parseo.py`; salida íntegra en `muestra_parseo_salida.txt` (365 líneas)
del paquete de revisión.

**Criterio de selección de los 3 (declarado):** un TO por extremo del eje de
tabularidad más el dominante de volumen.
- `ri_laft` — extremo tabular (86,1 % de palabras en tabla, 45 pág.).
- `ri_cc` — prosa mezclada, y el TO del bloque que **más** unidades produce hoy
  (33), con índice y secciones (118 pág.).
- `manual` — dominante de volumen: 2.037 de las 3.435 páginas del bloque.

### 2.1 Lo que devuelve, por documento

| | `ri_laft` | `ri_cc` | `manual` |
|---|--:|--:|--:|
| páginas | 45 | 118 | 2.037 |
| páginas con ≥1 tabla de contenido | 41 (91,1 %) | 46 (39,0 %) | **12 (0,6 %)** |
| tablas de contenido | 43 | 52 | 12 |
| filas por tabla (mín / mediana / máx) | 5 / 31 / 45 | 3 / 9 / 43 | 3 / 12 / 12 |
| columnas (nº → nº de tablas) | `{2: 43}` | `{2:11, 3:10, 4:3, 5:3, 7:4, 8:3, 9:5, 10:5, 11:2, 12:1, 13:2, 15:1, 21:2}` | `{3:11, 4:1}` |
| celdas vacías | 43 / 2.418 (**1,8 %**) | 3.664 / 4.851 (**75,5 %**) | 155 / 408 (38,0 %) |
| celdas con salto de línea interno | 311 (12,9 %) | 211 (4,3 %) | 44 (10,8 %) |
| tablas tocando borde superior / inferior | 38 / 35 | 20 / 13 | 0 / 0 |

Tres lecturas:

- **`ri_laft` sale limpio.** 43 tablas, todas de 2 columnas, 1,8 % de celdas
  vacías. Son tablas de código de reporte:
  ```
  ['TABLA FORMA JURIDICA', '·']
  ['Código', 'Descripción']
  ['3005', 'Sociedad de Responsabilidad Limitada']
  ['3006', 'Sociedad Anónima']
  ```
- **`ri_cc` sale sucio pero recuperable.** El 75,5 % de celdas vacías no es
  ruido: son **planillas de presentación** de hasta 21 columnas, esparcidas por
  construcción. Sus tablas densas sí salen bien (§2.2).
- **`manual` no tiene tablas que extraer.** 12 en 2.037 páginas. Un módulo de
  tablas aplicado al 71 % del bloque devolvería casi nada. Además las 12 son
  **la misma tabla repetida**: la de previsiones mínimas por categoría de deudor,
  replicada idéntica en las páginas 256, 310, 356, 414, 454…

### 2.2 Las grillas: cuándo salen íntegras y cuándo salen partidas

**Sí salen íntegras cuando la grilla está dibujada.** El caso que importa —una
tabla de ponderadores en un documento de régimen informativo— sale **correcto**:

`ri_cc.pdf` p. 60 (`rects=190`), tabla de 11 filas × 3 columnas:
```
['CODIGO', 'DETALLE DE CONCEPTOS', 'PONDERADOR<NL>%']
['12100000', 'Operaciones con el BCRA y efectivo en caja.', '0']
['12200000', 'Disponibilidades en otras entidades financie…', '20']
['18510000', 'En efectivo y cauciones de certificados de d…', '0']
['18530000', 'Cupones de tarjetas de crédito.', '75']
['18600000', 'Financiaciones cubiertas con garantía hipote…', '50']
['18700000', 'Demás financiaciones', '100']
```
Cada fila trae su código, su concepto y su ponderador, alineados.

**No salen íntegras cuando la columna de valores no está encerrada.** El
contraejemplo es `ric::3.1.4`, el «Modelo de información» del único TO de régimen
informativo que el pipeline sí digirió (está en el subset congelado). Con los
settings por defecto, `find_tables` devuelve 24 filas × 3 columnas y **mete los 19
ponderadores en una sola celda**:

```bash
python3 - <<'PY'
import pdfplumber
with pdfplumber.open('data/experiment/subset/TO_regimen_informativo_contable_mensual_actual.pdf') as pdf:
    for r in pdf.pages[7].find_tables()[1].extract()[:6]: print(r)
PY
```
```
['', '', 'Factor de ponde-']
['Código', 'Concepto', None]
[None, None, 'ración (en %)']
['', '', None]
['11000000', 'Disponibilidades', '0\n2\n4\n10\n20\n30\n40\n45\n50\n60\n65\n75\n85\n100\n130\n150\n200\n250\n1250']
['11100000', 'Exposiciones a gobiernos y bancos centrales', None]
```

Los 19 valores del ponderador quedan pegados en la celda de la primera fila. La
estrategia `text` en ambos ejes es peor —parte palabras al medio (`['B.C.R.A. 4.',
'EXIGENCIA E INTEGR', 'ACIÓN DE CA', …]`)—; `lines_strict` devuelve **0** tablas.

**Grilla partida entre páginas: confirmada.** En `ri_laft`, 38 de 43 tablas
empiezan en el 20 % superior de la página y 35 terminan pasado el 80 %. El caso
literal: «TABLA FORMA JURIDICA» ocupa las páginas 5 (códigos 3001–3017) y 6
(3018–3027), y `extract_tables` devuelve **dos tablas independientes**, cada una
con su propio par de filas de encabezado repetido. Reunirlas es trabajo del
módulo, no del parser.

### 2.3 Encabezados, celdas fusionadas y notas al pie

**Encabezados.** Tres patologías distintas, las tres medidas:
1. *Encabezado repetido en la continuación.* `ri_laft` p. 5 y p. 6 repiten
   `['TABLA FORMA JURIDICA','·']` + `['Código','Descripción']`. Sin regla de
   fusión, entran dos veces como si fueran datos.
2. *Encabezado partido en varias filas por envoltura.* `ric::3.1.4`: `'Factor de
   ponde-'` en una fila y `'ración (en %)'` dos filas más abajo. El nombre de la
   columna no está en ninguna celda completa.
3. *Encabezado con celda fusionada vertical.* `manual` p. 256:
   ```
   ['·',          'Con garantías', 'Sin garantías']
   ['Categoría',  '·',             '·']
   ['·',          'preferidas',    'preferidas']
   ```
   `Categoría` abarca dos filas y `Con garantías preferidas` es un encabezado de
   dos líneas: el parser las devuelve como tres filas de datos con huecos.

**Celdas fusionadas.** Además del caso anterior, `manual` p. 256 muestra la
fusión *dentro* de una celda de datos: `['2. a) En observación y de riesgo
bajo<NL>b) En …', '3%<NL>6%', '5%<NL>12%']` — una fila visual que contiene dos
filas lógicas, empaquetadas con saltos de línea. En el bloque completo hay
**2.081 celdas con salto de línea interno** (3,7 % de 56.699). Cada una es una
decisión: ¿es texto envuelto o son dos filas?

**Notas al pie.** Caen **fuera** del bbox de la tabla y quedan huérfanas.
Verificado: `ri_niif` p. 20, la celda `'Patrimonio Neto atribuible a los
propietarios de la controladora (*)'` conserva el marcador, y la nota
`'(*) Total de Patrimonio Neto para Estados Financieros individuales o
separados'` queda afuera. Páginas con texto de nota al pie inmediatamente debajo
de una tabla: **12 en `ri_niif`, 5 en `ri_cc`, 0 en `ri_laft`**.

### 2.4 El hallazgo que decide el dimensionamiento: la geometría no determina la fila

En `ric::3.1.4` la columna de ponderadores es un **bloque tipográfico
independiente**, con su propio paso vertical. Medido sobre las coordenadas reales
de la página: los conceptos corren con paso ≈17,0 pt y los ponderadores con paso
≈13,8 pt, y arrancan desfasados. Hay **20 códigos y 19 valores**.

Dos reglas de alineación igualmente defendibles:
- **A — vecino más cercano por `top`** (lo que hace cualquier alineador
  geométrico).
- **B — ordinal**: el k-ésimo valor va a la k-ésima fila de datos, descartando la
  primera como encabezado de categoría (19 valores ↔ 19 códigos, cuadra exacto).

```bash
python3 - <<'PY'
import pdfplumber
with pdfplumber.open('data/experiment/subset/TO_regimen_informativo_contable_mensual_actual.pdf') as pdf:
    ws=[w for w in pdf.pages[7].extract_words() if 150<w['top']<500]
codes=[w for w in ws if w['x0']<120 and w['text'][:1].isdigit()]
vals=[w for w in ws if w['x0']>700]
dis=0
for i,c in enumerate(codes):
    near=min(vals,key=lambda v:abs(v['top']-c['top']))
    a=near['text'] if abs(near['top']-c['top'])<12 else '(vacio)'
    b=vals[i-1]['text'] if 1<=i<=len(vals) else '(vacio)'
    dis += (a!=b)
print(f"{len(codes)} codigos, {len(vals)} valores; discrepan {dis} filas")
PY
```
→ `20 codigos, 19 valores; discrepan 17 filas`

**17 de 20 filas reciben un ponderador distinto según qué regla se use.** Ejemplo:
`11300000 Exposición a entidades financieras del país y del exterior` recibe
**10 %** con la regla A y **4 %** con la regla B.

Esta unidad **no adjudica** cuál es la correcta: no tiene mandato ni forma de
verificarlo sin la norma a la vista. Lo que queda establecido es lo que importa
para dimensionar: **un módulo de tablas genérico no puede producir la tripleta
correcta acá sin una regla específica o un paso de verificación**. Es la forma
general de RX-10 (`docs/backlog_reextraccion.md:267-292`), que ya tiene daño
medido —bancos 5.000 / restantes 2.500 quedaron **invertidos** en el grafo, y la
precisión del 31-07 registra que el daño es **por instancia, no sistemático por
tabla**: *«toda tabla numérica del corpus requiere verificación individual»*
(`:289-292`)—.

---

## 3. La pregunta que decide todo: ¿qué unidad de extracción produce ese material?

### 3.1 Qué pasó la única vez que el pipeline vio una tabla de ponderadores

No hay que especular: está pago y persistido. `ric::3.1.4` recorrió el pipeline
completo. Su chunk llegó al extractor con el texto ya linealizado y desordenado
(`e0_chunking/salida/chunks_ric.json`, id `ric::3.1.4`, flag
`contenido_tabular: true`):

```
Factor de ponde-
Código Concepto
ración (en %)
11000000 Disponibilidades
Exposiciones a gobiernos y bancos centrales 0
11100000
2
Exposiciones a bancos multilaterales de desarrollo (BMD)
11200000
4
…
```

**Lo que el extractor produjo** (crudo íntegro en
`corpus_v2/salida/ric/extracciones_e1.jsonl`): 3 entidades —un `TextoOrdenado`,
una `Operacion` («Clasificación exposiciones crédito») y una `Obligacion`
(«Aplicar ponderaciones exposiciones riesgo»)— y 3 relaciones
(`establecida_en`, `aplica_a`, `regula`). **Cero ponderadores.**

**Y lo declaró por escrito**, en el canal `omisiones_no_prosa` del propio crudo:

> «Tabla de códigos de exposición (11000000 a 12800000) y factores de ponderación
> específicos […] Los valores numéricos (0, 2, 4, … 1250 %) no se extrajeron dado
> que la prosa no enunció en oraciones completas cuáles ponderadores aplican a
> cuáles conceptos específicos; la relación entre código-concepto-ponderador
> depende de la estructura tabular visual cuya integridad no es confiable
> post-extracción PDF.»

**Lo que quedó en el grafo vigente** (`corpus_v2/salida_r1/kg.json`,
sha `0226e947…`):

```bash
python3 -c "
import json; kg=json.load(open('data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json'))
s=[n for n in kg['nodes'] if (n.get('provenance') or {}).get('chunk_id')=='ric::3.1.4']
print(len(s)); [print(' ', n['type'], '|', n['label']) for n in s]"
```
→ `2` · `Obligacion | Aplicar ponderaciones exposiciones riesgo` ·
`Operacion | Clasificación exposiciones crédito`

**19 pares código→ponderador entraron al grafo como 2 nodos y ningún número.**

### 3.2 No es un caso aislado: el censo de omisiones declaradas

```bash
python3 - <<'PY'
import json, glob, collections, os
flags={}
for p in glob.glob('data/experiment/reextraccion_v2/e0_chunking/salida/chunks_*.json'):
    for c in json.load(open(p)): flags[c['id']]=c['flags']
tot=con=tab=0; por=collections.Counter()
for p in glob.glob('data/experiment/reextraccion_v2/corpus_v2/salida/*/extracciones_e1.jsonl'):
    to=os.path.basename(os.path.dirname(p))
    for line in open(p):
        d=json.loads(line); tot+=1
        if (d.get('tool_input_crudo') or {}).get('omisiones_no_prosa'):
            con+=1; por[to]+=1
            if flags.get(d['chunk_id'],{}).get('contenido_tabular'): tab+=1
print(tot, con, dict(por), tab)
PY
```
→ `1769 75 {'ric': 37, 'cap': 34, 'ext': 3, 'cla': 1} 28`

**74 de 1.769 unidades declaran haber dejado material afuera; 28 de ellas son
chunks que E0 marcó como tabulares.**

*Conciliación con el pre-registro de ESQ-1 (commit `38be6e5`), que reporta 74.*
El comando de arriba devuelve 75 porque su condición es de verdad-lógica y hay
una unidad —`cap::6.5.3.2`— cuyo `omisiones_no_prosa` es la cadena `'\n'`, sin
contenido. Con el criterio estricto (elemento no vacío) son **74**, y el conteo
de `cap` baja de 34 a **33**: los dos números del pre-registro. **Se adopta 74**
y se declara el descarte. Nota aparte: el pre-registro clasifica esas 33 por
contenido («tablas de ponderadores en Capitales Mínimos»); las 28 de acá se
clasifican por el flag `contenido_tabular` que E0 puso en el chunk. Son dos
medidas distintas del mismo material, no dos versiones del mismo número.

Las 28 declaraciones (transcriptas íntegras en
`omisiones_tabulares_U-B5.6-0.txt` del paquete de revisión) repiten el mismo enunciado: *«estructura
tabular no confiable, valores numéricos no extraídos»*. Cubren tablas de
ponderadores, de aforos, de CCF, de tramos de coeficientes, de bandas temporales
y de posiciones arancelarias.

Dato que corrige una intuición razonable: **el volumen extraído no baja en los
chunks tabulares**.

```
no_tabular: chunks=1453  ent=13277 (9,14/chunk)  rel=10027 (6,90/chunk)
tabular:    chunks=  30  ent=  290 (9,67/chunk)  rel=  391 (13,03/chunk)
```

El extractor produce **igual o más** nodos sobre un chunk tabular. Lo que pierde
no es el conteo: es el **contenido de la celda**. Un indicador de volumen jamás
habría detectado esto.

### 3.3 ¿Una fila o una tabla se puede tratar como las unidades actuales?

**No.** Las unidades actuales son puntos del articulado
(`e0_lib.construir_chunks`, tipos `punto_terminal` y `mini_chunk`), y su
supuesto de diseño es que el texto de la unidad es **prosa autocontenida con
herencia de ancestros**. Una fila de tabla viola tres cosas de ese contrato:

1. **No es autocontenida.** `['18530000', 'Cupones de tarjetas de crédito.',
   '75']` no significa nada sin el encabezado de columna (`PONDERADOR %`), sin el
   título de la tabla y sin el punto del articulado que la introduce. La herencia
   de E0 propaga *ancestros del árbol de puntos*, no *encabezados de columna*.
2. **No hay una granularidad que sirva para las dos cosas.** Una unidad =
   una tabla convierte 19 hechos en un blob de texto que el extractor ya demostró
   que no sabe desarmar (§3.1). Una unidad = una fila multiplica las llamadas por
   el número de filas: **8.304 filas medidas** en el bloque, contra 1.769 unidades
   de todo el corpus actual. A la tarifa E1+E3 del inventario (USD 0,019437 por
   unidad, `resumen_escalado.md` §1) eso serían **USD 161** sólo de filas de RI,
   y cada llamada vería tres celdas sin contexto.
3. **La cobertura de cero pérdida de E0 se define sobre el texto linealizado.**
   `verificar_cobertura` (`e0_lib.py:1192`) comprueba que todas las líneas del
   cuerpo terminen en algún chunk. Una tabla extraída como grilla **no es una
   línea de texto**: o entra por fuera de esa verificación o hay que redefinir la
   verificación. Es una decisión de diseño, no un detalle.

**Lo que la fila sí es: un registro tipado con provenance propia.** Una fila
tiene una clave (el código), N atributos con nombre (los encabezados), un origen
puntual (TO, página, tabla, índice de fila) y una relación de pertenencia con el
punto del articulado que la introduce. Ése es un objeto distinto de un punto de
prosa y **exige tratamiento propio**.

### 3.4 ¿Alcanzan los seis tipos y los doce predicados?

**No.** Y falta en dos lugares independientes, los dos verificables contra
`schema.py`.

**(a) No hay tipo de entidad para el sujeto de la fila.** Los seis tipos
(`schema.py:24-31`) son `Comunicacion`, `TextoOrdenado`, `Operacion`,
`Restriccion`, `Excepcion`, `Obligacion`. Los cuatro últimos son **objetos
deónticos**: lo que la norma manda, prohíbe, permite o exceptúa. Una fila de
`TABLA FORMA JURIDICA` —`['3006','Sociedad Anónima']`— no es ninguno de los
seis: es una **categoría de un vocabulario controlado de reporte**. Lo mismo la
partida `12100000 Operaciones con el BCRA y efectivo en caja`, que no es una
`Operacion` regulada sino un **concepto contable** al que se le imputan saldos.
Forzarla en `Operacion` es exactamente lo que el prompt prohíbe
(`prompt_e1.py:134`: «Es preferible no extraer algo a forzarlo en una caja
equivocada»).

El catálogo de sujetos (`schema.py:94`, 70 entradas) tampoco resuelve: cubre
*quién está alcanzado por la norma*, no *qué concepto se informa*. Y algunas
tablas del bloque son literalmente taxonomías de sujetos (`TABLA FORMA JURIDICA`,
27 códigos repartidos en dos páginas) mientras otras son taxonomías de productos
(`TABLA PRODUCTO DONDE SE REGISTRÓ LA INUSUALIDAD`, cuyo encabezado reaparece en
tres páginas de la muestra) — o sea que ni siquiera un único tipo nuevo alcanza
para todas.

**(b) No hay forma de que una relación lleve un valor.** Ésta es la falta dura,
y es estructural: `RelationOut` (`schema.py:220-235`) tiene exactamente
`source`, `target`, `predicate`, `sujeto_id`, `sujeto_propuesto` y
`sujeto_propuesto_padre_sugerido`. **No tiene `properties`.** Los doce predicados
(`schema.py:41-53`) son binarios sin atributo. `DOMAIN_RANGE`
(`schema.py:167-181`) fija pares dominio→rango, no valores.

Consecuencia sobre el ejemplo concreto: el hecho *«la partida 12100000 pondera al
0 %»* no tiene dónde vivir. Las tres vías posibles y por qué ninguna cierra:

| vía | qué exigiría | veredicto |
|---|---|---|
| `properties` de una entidad (`schema.py:190`, `dict[str,str]`) | aplanar 19 filas en el dict de un nodo | Cabe físicamente, pero deja de ser un grafo: el ponderador no es consultable por relación, no tiene provenance de fila y el agente no puede navegar hasta él. Es lo que ya pasó, con 0 valores guardados. |
| Reificar la celda como nodo | un **tipo nuevo** para el nodo-celda + **predicados nuevos** para engancharlo | Cambia el esquema: 1 tipo + ≥2 predicados + entradas de `DOMAIN_RANGE`. |
| Predicado calificado | agregar `properties` a `RelationOut` | Cambia el **contrato** de la relación, no sólo su vocabulario: toca `schema.py`, el tool schema (`prompt_e1.py:239-258`, con `additionalProperties: False`), el validador (`validador_e1.py`), el ensamblado y el cargador de Neo4j. |

**Conclusión de §3, en una línea:** el bloque de régimen informativo **exigiría
tipos propios**, y además —lo que no estaba en la pregunta y es más caro— un
**mecanismo de atributo en la arista** que el esquema hoy no tiene en ninguna
forma. Arreglar el parser sin esto produce grillas correctas que no se pueden
escribir en el grafo.

**Magnitud, para calibrar:** 8.304 filas de tabla medidas en el bloque. Si cada
fila fuera un nodo, el bloque agregaría más nodos que los **6.529** que tiene hoy
el grafo vigente entero — y de una especie que el esquema no declara.

---

## 4. Dimensionamiento de B5.6

### 4.1 Lo que el plan dice hoy, y por qué no cierra

`plan_tesis.md:358`: *«B5.6 (I, $0) Módulo de tablas (pdfplumber `extract_tables`
con provenance, sin LLM) — RX-10 y montos invertidos; decide el destino del
bloque RI.»*

Dos observaciones, ambas medidas:

1. **Como remedio de RX-10 está bien dimensionado.** RX-10 es un defecto de
   *correctitud* sobre documentos que el pipeline ya digiere: 30 chunks tabulares
   en el corpus actual, 28 con omisión declarada, 2 montos invertidos verificados.
   Un módulo de tablas los ataca de frente.
2. **Como llave del bloque RI, no.** Un módulo de tablas alcanza a lo sumo el
   **12,4 %** de las palabras del bloque y a **23 de 53** TOs. No toca el 70,9 %
   de páginas de la familia FICHA ni el 5,1 % de PROSA. Y las familias PROSA y
   MIXTO —44 TOs, 772 páginas— están bloqueadas por la compuerta de rol de página
   y la ausencia de raíz de sección (§1.3, §1.5), que son E0, no tablas.

### 4.2 Qué habría que construir, en tres piezas separables

**Pieza 1 — E0 sin raíz de sección** (habilita PROSA + MIXTO: 44 TOs, 772 pág.).
- Modo de rol de página que no dependa del marcador de índice, con guarda que
  evite tragarse portada e historial (`e0_lib.py:179-211`).
- Modo estructural «puntos sin sección»: raíz sintética por documento, para que
  los 2.522 labels de punto medidos tengan dónde colgarse sin chocar con
  `e0_lib.py:412`.
- Health-check por TO (ya pedido en `plan_tesis.md:354`) + paridad byte a byte
  sobre los 5 TOs del subset y selftest 57/57, que son el gate no negociable.
- **Archivos**: `e0_lib.py`, `selftest_e0.py`, `correr_e0.py` — todos fuera de las
  zonas selladas de CLAUDE.md §3, pero `e0_lib.py` gobierna los chunks del grafo
  vigente: **cualquier cambio exige demostrar paridad exacta sobre el subset**.

**Pieza 2 — Módulo de tablas** (habilita TABULAR: 5 TOs, 150 pág.; y remedia
RX-10 sobre el corpus actual).
- Detección de tabla de contenido con la regla de §1.4 (banner y pie excluidos).
- Elección de estrategia por página según haya o no grilla dibujada — medido: con
  grilla (`ri_cc` p. 60, `rects=190`) el default acierta; sin grilla
  (`ric::3.1.4`) no.
- **Reconstrucción de encabezado**: fusión de encabezado envuelto en varias filas,
  fusión vertical y repetición del encabezado en la continuación (§2.3).
- **Costura entre páginas**: 38 de 43 tablas de `ri_laft` tocan borde.
- **Notas al pie**: capturar el texto de nota que cae fuera del bbox y ligarlo al
  marcador de la celda (17 páginas medidas en dos TOs).
- **Guarda de alineación**: dado §2.4, el módulo **debe** detectar cuándo la
  geometría no determina la fila y **negarse a emitir** en vez de emitir mal. Es
  la lección directa de RX-10, cuyo daño es *por instancia*.
- Provenance de fila: TO, página, tabla, índice de fila, texto crudo.
- **Archivos**: módulo nuevo bajo `reextraccion_v2/e0_chunking/` (o
  `e0_tablas/`), con su selftest; punto de enganche en `construir_chunks`
  (`e0_lib.py:1030`) y en `verificar_cobertura` (`:1192`), que hoy se define sobre
  líneas de texto y no sabe qué hacer con una grilla.

**Pieza 3 — Esquema para el material informativo** (sin esto las piezas 1 y 2
producen material que no se puede escribir).
- ≥1 tipo de entidad nuevo para el concepto/partida informativa. La muestra ya
  sugiere que uno solo no alcanza: hay taxonomías de sujeto y taxonomías de
  producto en el mismo bloque (§3.4).
- Mecanismo de valor en la arista: o `properties` en `RelationOut`, o reificación
  con tipo de celda. **Es una decisión de esquema, no de código.**
- **Archivos**: `grafo_v2/code/schema.py`, `e1_extractor/prompt_e1.py` (tool
  schema, `:219-267`), `e1_extractor/validador_e1.py`, ensamblado E5 y
  `neo4j/grafos.py`. **Rota el prefijo cacheado de E1** — lo cual ya está aceptado
  y presupuestado por otra vía (`plan_tesis.md:356`, B5.4).
- **Prerrequisito de gobierno**: esto es exactamente lo que ESQ-3 tiene mandato
  de decidir (`plan_tesis.md:336-340`). Si se hace fuera de ESQ-3, hay dos lugares
  donde se retoca el esquema y el laudo de congelamiento pierde sentido.

*(Queda fuera de las tres piezas, y se declara: las familias FICHA —2.436 pág.— y
LISTA_CODIGOS —77 pág.— necesitarían una **cuarta** pieza, un parser de registro
clave-valor y de lista jerárquica de códigos. No se dimensiona acá porque no es
un módulo de tablas y porque su volumen obliga a que sea decisión de alcance,
no de implementación.)*

### 4.3 Estimación, con lo medido y lo supuesto separados

**Medido** (todo reproducible):

| ancla | valor | fuente |
|---|--:|---|
| tamaño del módulo E0 existente | 1.272 líneas (`e0_lib.py`) + 309 (`selftest_e0.py`) + 169 (`correr_e0.py`) = **1.750** | `wc -l` |
| alcance que cubre ese módulo | 5 PDFs de **una** familia estructural | `e0_chunking/INFORME_E0.md` §1 |
| commits de corrección posteriores a su primera entrega | 2 (`e287fe3`, `d082812`) | `git log -- data/experiment/reextraccion_v2/e0_chunking/` |
| familias estructurales del bloque RI | **5** | §1.4 |
| tablas de contenido a parsear | 536, 8.304 filas, 56.699 celdas | §1.4 |
| páginas con costura entre páginas (muestra) | 38 de 43 tablas en `ri_laft` | §2.1 |
| filas donde la geometría no decide (caso medido) | 17 de 20 | §2.4 |
| gate de no regresión que hay que pasar | paridad 1.763/1.763 unidades sobre el subset + selftest 57/57 | `plan_tesis.md:354`, `111ed19` |
| costo de API de las tres piezas | **USD 0** (E0 y el parser son determinísticos) | — |

**Supuesto** (declarado como tal; no hay serie histórica de esfuerzo en el repo
de la cual derivarlo, así que el rango se ancla en el único módulo comparable
—E0— y se ensancha por el número de familias):

| pieza | unidades de mandato | supuesto explícito |
|---|--:|---|
| 1 — E0 sin raíz de sección | **1–2** | que el modo nuevo se agrega sin romper la paridad del subset; si la rompe, se dispara a 3–4 porque hay que rehacer la calibración |
| 2 — módulo de tablas | **2–4** | 1 unidad de parser base + 1 de encabezados/costura/notas + 1 de guarda de alineación y provenance; la cuarta si el gate de cobertura obliga a redefinir `verificar_cobertura` |
| 3 — esquema informativo | **1–2** *dentro de ESQ-3* | supone que ESQ-3 absorbe la decisión; si va por fuera, hay que sumarle su propio laudo |
| 4 — parser de fichas (FICHA + LISTA_CODIGOS) | **2–4** | **no dimensionado con muestra propia**; el rango se declara por analogía con la pieza 2 y es el número menos confiable del documento |

**Rango total con las piezas 1+2+3: 4 a 8 unidades de mandato, USD 0 de API en
la construcción.** Con la pieza 4: 6 a 12. La corrida de extracción sobre lo que
se desbloquee **no está en este rango** y se estima en §5.3.

**Lo que esta estimación NO cubre y hay que decir en voz alta:** el riesgo caro no
es escribir el parser, es el **gate de verificación**. RX-10 dejó registrado que
*«toda tabla numérica del corpus requiere verificación individual»*
(`backlog_reextraccion.md:289-292`). Si eso se sostiene, 536 tablas del bloque RI
más las 30 del corpus actual necesitan una pasada de verificación humana o
adjudicada, y **eso no es tiempo de código**: es tiempo de la autora, y no está
dimensionado acá porque depende de una regla de muestreo que todavía no existe.

---

## 5. Consecuencia sobre la ruta crítica

### 5.1 La ruta vigente

`plan_tesis.md:563-564`: `ESQ-1 → ESQ-2 → ESQ-3 (retoques + esquema congelado) →
escalado (B5/B6) → evaluación final (B6.3)`.

El laudo ESQ-1 §D10 fija además dos condiciones: la frontera del régimen
informativo se lleva a mentores **antes** de laudar D5 (B5.5), y si B5.6 se
construye y produce unidades sobre régimen informativo, **esa familia corre su
propio ciclo ESQ antes de que el esquema se congele para ella**.

### 5.2 Qué unidades nuevas aparecen, y en qué orden

Si se construye el módulo, entre hoy y el escalado se intercalan estas unidades.
El orden no es negociable en tres puntos, señalados:

| # | unidad | depende de | por qué en ese lugar |
|--:|---|---|---|
| 1 | **B5.6-a** — E0 sin raíz de sección (pieza 1) | — | Es la más barata y la de mayor rendimiento por página. Va primera porque su resultado **cambia el número que se lleva a mentores**: si desbloquea las 772 páginas de PROSA+MIXTO, la frontera se discute con un bloque residual de 2.663 páginas, no de 3.435. |
| 2 | **B5.6-b** — módulo de tablas (pieza 2) | B5.6-a | Necesita chunks donde escribirse. Además cierra RX-10 sobre el corpus actual, valor que no depende de la decisión de alcance. |
| 3 | **B5.6-c** — re-corrida en seco de E0 sobre los 53 + censo | B5.6-a, B5.6-b | **Sustituye al número supuesto por uno medido.** Sin esto, D5 se lauda sobre extrapolación. USD 0. |
| 4 | **ESQ-RI-0** — muestra de extracción sobre régimen informativo | B5.6-c | Antes de comprometer un ciclo ESQ entero, una muestra chica y presupuestada que responda si el material extraído es representable. Es el mismo patrón de control de instrumento que D2 del laudo ESQ-1. |
| 5 | **ESQ-3** — retoques + esquema congelado | ESQ-1, ESQ-2, ESQ-RI-0 | **Punto duro**: la pieza 3 (tipos y valor en arista) **es** materia de ESQ-3. Si el bloque RI entra al alcance, ESQ-3 no puede laudarse antes de haber visto material informativo. |
| 6 | **B5.5 / D5** — laudo de corpus a escalar | 3, 4, y la reunión de mentores | **Punto duro**: el laudo ESQ-1 exige que la frontera vaya a mentores **antes** de D5. |

### 5.3 ¿El bloque RI necesita su propio ciclo ESQ? Sí, y por dos razones

**Razón 1 — la que el laudo ya anticipa.** ESQ-1 y ESQ-2 sortearon sus 20
documentos sobre los 68 digeribles, que son **todos** de normativa general
(`escalado_prep/scoping_esq1.md` §4.2, y verificado acá: los 68 digeribles no
incluyen ningún TO de categoría `regimen_informativo`). El esquema congelado por
ESQ-3 no habría visto una sola unidad de régimen informativo. Congelarlo así y
después escalar sobre RI es exactamente el sesgo que D10 quiere evitar.

**Razón 2 — la que sale de esta unidad y es más fuerte.** El material informativo
no sólo podría pedir tipos nuevos: la evidencia de §3.4 dice que **pide un
mecanismo que el esquema no tiene en ninguna forma** (valor en la arista). Un
ciclo ESQ sobre normativa general no puede descubrir esa falta, porque la
normativa general se expresa en prosa y sus valores caben en `properties` de una
entidad. La falta sólo aparece cuando el material es tabular. **El ciclo ESQ-RI
no es una repetición por prolijidad: mide una dimensión distinta.**

**Costo de ese ciclo — supuesto, con la aritmética a la vista.** Si B5.6-a+b
desbloquean las 772 páginas de PROSA+MIXTO, y suponiendo la densidad de unidades
por página de `ric` (1,4237 unid/pág., la única medida disponible sobre un TO de
régimen informativo, `resumen_escalado.md` §3.1), salen ~1.099 unidades →
**USD 21,4** a la tarifa E1+E3 de USD 0,019437/unidad. Un ESQ-RI de 10
documentos sobre ese universo costaría una fracción de eso.
**Los dos supuestos están declarados y ninguno está medido**: la densidad viene
de un solo TO, y el desbloqueo de las 772 páginas es precisamente lo que B5.6-c
mediría. Si además entrara la familia FICHA (2.436 pág.), la misma densidad daría
~3.469 unidades → **USD 67,4**, cifra con la que hay que ser especialmente
prudente porque una ficha de cuenta no se parece en nada a un punto de `ric`.

---

## 6. Recomendación

### 6.1 Recomendación única

**Partir B5.6 en las tres piezas de §4.2, ejecutar 1 y 2 antes de la reunión de
mentores, y llevar a la reunión una frontera con número medido en vez de un
todo-o-nada.**

El fundamento es que el censo cambia la pregunta. La conversación que el laudo
D10 anticipaba era «¿escalamos una familia o dos?». El censo dice que el bloque no
es una familia: son cinco, con costos y rendimientos muy distintos, y **la más
barata no es tabular**.

Concretamente, lo que se recomienda llevar a mentores es esta partición, no un
sí/no:

| tramo | TOs | páginas | qué lo desbloquea | costo de construcción |
|---|--:|--:|---|---|
| PROSA + MIXTO | 44 | 772 | pieza 1 (E0 sin raíz de sección) | 1–2 unidades, USD 0 |
| TABULAR | 5 | 150 | piezas 1 + 2 + 3 | +2–4 unidades + decisión de esquema |
| FICHA + LISTA_CODIGOS | 4 | 2.513 | pieza 4 (parser de registro) — **no dimensionada con muestra** | 2–4 unidades, el número menos confiable |

Y las razones por las que las piezas 1 y 2 se recomiendan **con independencia de
lo que decidan los mentores**:

- **La pieza 2 no es opcional aunque el bloque RI quede afuera.** RX-10 es un
  defecto de correctitud sobre el corpus que **ya** está en el grafo: 28
  omisiones declaradas y 2 montos invertidos verificados. Si el bloque RI se
  descarta, el módulo de tablas sigue haciendo falta, sólo que para normativa
  general. Es el único ítem de este documento que no depende de la decisión de
  alcance.
- **La pieza 1 cuesta poco y mejora el insumo de la decisión.** Su resultado
  cambia la magnitud de lo que se discute (3.435 páginas vs. 2.663).

### 6.2 Alternativas y sus costos

| alternativa | qué gana | qué cuesta | por qué no se recomienda |
|---|---|---|---|
| **A — No construir nada; declarar el bloque RI fuera de alcance** | Cero trabajo nuevo; ruta crítica intacta; ESQ-3 lauda ya | Deja RX-10 abierto sobre el corpus que **sí** se escala; deja en pie la objeción metodológica de D10 (validar el esquema sólo donde funciona); las 3.435 páginas quedan como limitación declarada | Ahorra menos de lo que parece: la pieza 2 hace falta igual por RX-10 |
| **B — Construir B5.6 completo tal como está en el plan (sólo tablas)** | Cierra RX-10; habilita 5 TOs | 2–4 unidades; **no** desbloquea el 78 % del bloque; obliga igual a decidir el esquema | Es la opción que el censo desmiente: paga el módulo de tablas y sigue sin poder decir que validó el esquema sobre el corpus completo |
| **C — Recomendada: piezas 1+2 ahora, 3 dentro de ESQ-3, 4 a decisión de mentores** | Cierra RX-10; desbloquea 44 TOs por la vía barata; lleva a mentores una frontera con número | 3–6 unidades antes de D5; retrasa ESQ-3 lo que tarde ESQ-RI-0 | — |
| **D — Todo, incluida la pieza 4 (fichas)** | Cobertura real del corpus completo | 6–12 unidades + un ciclo ESQ propio + ~USD 67 de extracción supuestos sobre una densidad no medida para ese material | El volumen (2.436 pág. de `manual`) es de otro orden y su rendimiento en tripletas es **desconocido**: una ficha de cuenta es prosa de valuación, no normativa deóntica. Comprometerlo hoy repite el error que D10 quiso evitar, con el signo cambiado |
| **E — Delegar las tablas a un modelo multimodal en vez de a un parser** | Resolvería §2.4 (alineación) sin reglas por documento | Costo de API distinto de cero, no presupuestado; rompe el «sin LLM» de `plan_tesis.md:358`; introduce un componente no determinístico en E0, que hoy es determinístico puro | No se recomienda **ahora**, pero se deja anotada como la salida natural si la guarda de alineación de la pieza 2 rechaza demasiadas tablas. Es la única alternativa que ataca la causa raíz de §2.4 |

### 6.3 Lo que queda explícitamente para la reunión de mentores

Esta unidad **no decide** nada de lo siguiente. Lo entrega dimensionado:

1. **Si el bloque de régimen informativo entra al alcance del corpus a escalar**,
   y con qué tramos de los tres de §6.1. Toca D5/B5.5 y compromisos del PPF.
2. **Si la familia FICHA (2.436 páginas, 71 % del bloque) entra o queda declarada
   fuera.** Es la decisión de mayor impacto de calendario y la de evidencia más
   débil: no hay muestra de parseo propia ni densidad medida para ese material.
3. **Si se acepta retrasar ESQ-3** el tiempo de un ciclo ESQ-RI, dado que
   congelar el esquema sin haber visto material informativo lo dejaría sin
   validar en la familia donde hay razones medidas para dudar (§5.3, razón 2).
4. **Si el mecanismo de valor en la arista** —`properties` en `RelationOut` o
   reificación de celda— se abre como decisión de ESQ-3. Es un cambio de contrato
   del esquema, no de vocabulario, y toca `schema.py`, el tool schema, el
   validador, el ensamblado y Neo4j.
5. **Si se acepta la alternativa E** (parseo multimodal de tablas) como plan de
   contingencia declarado, con su tope de costo, para el caso de que la guarda de
   alineación rechace una fracción alta de las 536 tablas.

Lo que **no** hace falta llevar: la pieza 2 (módulo de tablas) por el lado de
RX-10. Ése es un defecto de correctitud sobre el corpus ya digerido y no depende
de ninguna decisión de alcance.

---

## 7. Contradicciones con documentos del repo, reportadas

Por CLAUDE.md §4.d, mandan los archivos. Se reportan tres.

1. **`docs/laudo_ESQ-1_diseno.md` §D10** dice: *«La causa no es el esquema sino la
   estructura tabular de esos documentos, que la etapa E0 no procesa.»* Los
   archivos dicen que la causa **proximal** es la compuerta de rol de página
   (`e0_lib.py:206-207` + `:343`): 47 de 53 TOs tienen el 100 % de sus páginas en
   rol `portada` y nunca llegan a la etapa donde una tabla podría estorbar. La
   estructura tabular es un obstáculo **posterior y minoritario** (12,4 % de las
   palabras). El resto del laudo —incluida la dirección de validar el esquema
   sobre el corpus completo y la exigencia de este scoping— no se ve afectado; lo
   que cambia es **qué** hay que construir.
2. **`docs/plan_tesis.md:354` (B5.2)** propone relajar el regex de índice
   («`Índice` sin guiones con guarda»). En los TOs de régimen informativo la
   palabra «índice» **no aparece** (verificado en `ri_laft`, `ri_pnp`); en
   `ri_dcpc` la única aparición es prosa sobre índices de actualización, que un
   regex más laxo tomaría como marcador. B5.2 no desbloquea el bloque.
3. **`docs/plan_tesis.md:358` (B5.6)** dice que el módulo de tablas *«decide el
   destino del bloque RI»*. Medido: alcanza a 23 de 53 TOs y al 12,4 % de las
   palabras. No decide el destino del bloque; decide el de una de sus cinco
   familias, y remedia RX-10 en normativa general.

---

## 8. Reproducibilidad

Los scripts de esta unidad viven en el scratchpad de la sesión y se entregan en el
paquete de revisión (no se agregaron al repo: la unidad autoriza un solo
documento de escritura). Ninguno modifica archivo alguno del repo.

| script | qué produce | tiempo |
|---|---|--:|
| `censo_ri.py` | censo estructural por TO: marcador de índice, headers de sección, tablas, palabras dentro/fuera | 3 min sobre las 3.435 páginas |
| `censo_ri2.py` | censo con la regla de tabla de **contenido** (banner y pie excluidos) | 4 min |
| `familias_ri.py` | señales léxicas (código, ficha, prosa) y asignación de familia | 4 min |
| `espina_ri.py` | labels de punto y headers de sección por TO (51 de 53) | 2 min |
| `muestra_parseo.py` | muestra de `extract_tables` sobre los 3 TOs (§2) | 30 s |

Verificación de que las zonas selladas quedaron intactas: `git status --porcelain`
al cierre de la unidad debe mostrar únicamente este documento y el archivo no
rastreado `adjudicar.py`, ajeno a la unidad.
