# Tabla de resultados de ESQ-2 — APROBADA POR LA AUTORA (02/09/2026)

Propuesta de mesa revisada por la autora con dos ajustes aplicados: fusión F2
(hechos con valor + criterios de parámetro) RECHAZADA — quedan separadas —, y
ternario E3/ESQUEMA/EXTRACTOR-PIPELINE ADOPTADO.

Salida del §6 del pre-registro `data/experiment/esq/prerregistro_esq2.md`
(`2240c9c`). Insumos: worksheet adjudicado
`cobertura/fichas/worksheet_fichas_esq2.json` (75/75 fichas), selección
`cobertura/orden/seleccion_muestra_esq2.json`, y el documento de desvíos
firmado `cobertura/desvios_lectura_esq2.md` (`685fc8a`) — **ESQ-3 lee esta
tabla junto con la doble tabla de sensibilidad de ese documento** (regla
conservadora: las 10 fichas del sorteo paralelo se tratan como contaminadas;
ninguna medida cambia de banda al excluirlas). Aritmética recomputada
independientemente por mesa y autora, coincidente. Alcance declarado del §6:
con n=38 los intervalos son anchos — **magnitudes gruesas**, no diferencias
finas. Todo se lee como **cota superior**: extracción E1-solo, sin E3 (§1).

## 1. Medidas globales

**Muestra azarosa (n=38 — la única que generaliza), Wilson 95 %:**

| medida | valor | sin las 4 contaminadas (n=34) |
|---|---|---|
| representación parcial o nula (cota superior) | 28/38 = 74 % [58 %, 85 %] | 24/34 = 71 % [54 %, 83 %] |
| no representado | 5/38 = 13 % [6 %, 27 %] | 4/34 = 12 % [5 %, 27 %] |
| firma de deformación real (a–g) | 16/38 = 42 % [28 %, 58 %] | 13/34 = 38 % [24 %, 55 %] |

**Muestra dirigida (n=37 — no generaliza, sin Wilson, se reporta aparte):**
q1: 10 sí_completo / 25 parcial / 2 no. Firma real: 21/37 = 57 % (a=14, e=4,
d=3; duda=1). Los disparadores **enriquecieron** (57 % dirigida vs 42 %
azarosa de firma real): la búsqueda dirigida encontró más deformación que el
azar, como el diseño esperaba. DUDAS (no cuentan para ningún lado, §6):
q2 — 2 azarosas + 1 dirigida.

## 2. Firmas de deformación (q2) — frecuencia azarosa con Wilson, dirigida aparte

| firma | azarosa (n=38, Wilson 95 %) | dirigida (n=37) | TOs (ambas) |
|---|---|---|---|
| (a) re-tipado semántico | 8/38 = 21 % [11 %, 36 %] | 14 | 10 |
| (d) potestades/facultades | 6/38 = 16 % [7 %, 30 %] | 3 | 5 |
| (e) hechos con valor aplastados | 0/38 = 0 % [0 %, 9 %] | 4 | 4 |
| (c) inconsistencia entre repeticiones | 1/38 = 3 % [0 %, 13 %] | 0 | 1 |
| (g) otro | 1/38 = 3 % [0 %, 13 %] | 0 | 1 |
| (b) nominalización | 0/38 | 0 | 0 |
| (f) omisiones | — se releva por q3 (§3), no como firma | — | — |

## 3. Familias de omisión (q3) — vocabulario normalizado, con criterio declarado

**Criterio de normalización (auditable).** Las 15 etiquetas crudas de la
autora se conservan casi todas (ya eran cuasi-controladas; una normalización
propia de la autora al cierre de la tanda 1 está declarada en la ficha 7).
La mesa propuso tres fusiones; la autora aprobó **dos** y rechazó una,
cada decisión fundada en si las etiquetas comparten LA MISMA capacidad
faltante:

- **F1 «pérdida de contenido del chapeau»** ← «pérdida en la composición con
  el chapeau heredado» (fichas 11, 13, 48, 52) + «chapeau de lista no
  extraído» (ficha 64). Mismo contenido perdido (el del encabezado/chapeau);
  causas hermanas documentadas en las propias fichas: troceo sin unidad
  propia (11) vs unidad propia vacía (64).
- **F2 «predicado faltante en la matriz dominio/rango»** ← «excepción sin
  predicado hacia la operación exceptuada» (fichas 44, 62, 65) + «documento
  sin predicado hacia la operación que instrumenta» (ficha 74). Mismo
  faltante (un predicado que la matriz no tiene), pares distintos —
  sub-etiquetas conservadas en la tabla.
- **Fusión RECHAZADA por la autora** (registrada para auditoría): «hecho con
  valor perdido» (f. 35) + «criterios de determinación de un parámetro»
  (f. 14) NO se fusionan. Comparten el paraguas de `fe1fe36` pero no la
  capacidad faltante — una pide **cardinalidad** (varios valores donde el
  modelo admite uno), la otra **estructura** (criterios que determinan un
  valor); fusionarlas sugeriría a ESQ-3 un remedio único que probablemente
  no alcance.

Las 11 etiquetas restantes pasan sin fusión. **Columna E3** (la que ESQ-3
necesita), con tres valores anclados en las notas de las fichas:
**E3** = la resuelve el ensamblado (aristas `referencia`/composición);
**ESQUEMA** = no se resuelve sin ampliar el esquema;
**EXTRACTOR/PIPELINE** = deuda de extracción o troceo (resoluble sin tocar
el esquema, pero no por E3).

| familia normalizada | az (Wilson, n=38) | di | TOs | E3 | ancla en fichas |
|---|---|---|---|---|---|
| remisión normativa sin arista posible | 11/38 = 29 % [17 %, 45 %] | 9 | 9 | **mixta**: intra-TO la resuelve E3 (f. 71: «punto 11.4»); la variante hacia otra norma carece de predicado Obligacion→TextoOrdenado (f. 10) o de tipo de destino (f. 7) | 7, 10, 71 |
| pérdida de contenido del chapeau (F1) | 5/38 = 13 % [6 %, 27 %] | 0 | 3 | **EXTRACTOR/PIPELINE** (f. 11: «no es hueco de esquema», troceo; f. 64: unidad propia vacía) | 11, 64 |
| potestad omitida | 2/38 = 5 % [1 %, 17 %] | 3 | 4 | **ESQUEMA** (sin categoría deóntica de permiso/facultad; tres reacciones distintas documentadas: forzar, no emitir, evaporar el modal — f. 26) | 2, 24, 26, 53, 66 |
| definición sin fuerza deóntica | 2/38 = 5 % [1 %, 17 %] | 2 | 4 | **ESQUEMA** (refinada en f. 37: el hueco no es la forma definitoria sino lo definido — clases, conjuntos, conceptos, parámetros — sin caja) | 8, 21, 25, 46 (+37, 20 como contraste) |
| hecho con valor perdido | 1/38 = 3 % [0 %, 13 %] | 0 | 1 | **ESQUEMA** (`fe1fe36`, vertiente de **cardinalidad**: dos hechos temporales, un solo campo `plazo`) | 35 |
| criterios de determinación de un parámetro | 1/38 = 3 % [0 %, 13 %] | 0 | 1 | **ESQUEMA** (`fe1fe36`, vertiente de **estructura**: criterios i–v que determinan un valor, sin dónde vivir) | 14 |
| predicado faltante en la matriz dominio/rango (F2) | 1/38 = 3 % [0 %, 13 %] | 3 | 3 | **ESQUEMA** (f. 44: «falta el predicado en el esquema»; ni E3 puede emitir lo que la matriz no admite) | 44, 62, 65, 74 |
| consecuencia sin vínculo a su condición | 1/38 = 3 % [0 %, 13 %] | 2 | 3 | **ESQUEMA** (f. 38 parte la familia en dos según naturaleza — insumo directo para decidir si hace falta un tipo de consecuencia/sanción; f. 63: ni nodo ni arista) | 38, 43, 63 |
| vínculo normativo cross-unidad | 1/38 = 3 % [0 %, 13 %] | 3 | 4 | **E3** (f. 39: «la cross-unidad la resuelve E3») | 18, 39, 61, 72 |
| atributo de operación sin campo donde alojarse | 1/38 = 3 % [0 %, 13 %] | 1 | 2 | **ESQUEMA** (Operacion es el único tipo sin `descripcion`) | 32, 47 |
| vínculo entre cláusulas — arista con firma válida no emitida | 1/38 = 3 % [0 %, 13 %] | 0 | 1 | **EXTRACTOR** (f. 3: las dos aristas tenían firma válida en la matriz y no se emitieron) | 3 |
| texto de reproducción obligatoria no preservado | 1/38 = 3 % [0 %, 13 %] | 0 | 1 | **EXTRACTOR** (la literalidad cabía en `descripcion` y se recortó) | 28 |
| contenido explicativo no prescriptivo | 0/38 = 0 % [0 %, 9 %] | 1 | 1 | **ESQUEMA** (contenido meta-normativo sin tipo; emparentada con el trío de tratamientos improvisados de la f. 46) | 19 |

Nota: esta tabla NO aplica el criterio §6 a las familias de q3 ni recomienda
tratamiento — provee las columnas (az, TOs, E3) para que **ESQ-3** lo
aplique y decida. La distinción E3/ESQUEMA/EXTRACTOR viene de las notas
contemporáneas de las fichas, no de una relectura.

## 4. Aplicación del criterio sellado §6 a las firmas (resultado explícito)

Criterio (verbatim del §6, NO CALIBRADO): candidata a ampliación si ≥3
fichas azarosas o ≥3 TOs contando ambas muestras; residuo documentado si ≤2
y ≤2; **la dirigida corrobora pero nunca promueve por sí sola**; las dudas
se listan y no cuentan; ESQ-3 solo se aparta con laudo declarado.

| firma | azarosas | TOs (ambas) | resultado |
|---|---|---|---|
| (a) re-tipado semántico | 8 | 10 | **CANDIDATA** (por ambas vías; robusta a la sensibilidad: ≥3 azarosas limpias) |
| (d) potestades/facultades | 6 | 5 | **CANDIDATA** (por ambas vías; robusta a la sensibilidad) |
| (e) hechos con valor | 0 | 4 | **NO PROMUEVE por criterio**: sus 4 fichas son todas dirigidas y la dirigida nunca promueve sola. Llega a ESQ-3 por material propio e independiente: hallazgo `fe1fe36` y entrada 5 de la cola |
| (c) inconsistencia entre repeticiones | 1 | 1 | **residuo documentado** |
| (g) otro | 1 | 1 | **residuo documentado** |
| (b) nominalización | 0 | 0 | sin apariciones en lectura (el disparador d1 la buscó; ninguna ficha la confirmó como deformación) |

**La firma (a) aparece en los DIEZ TOs del universo** — es el hallazgo más
disperso de la medición: el re-tipado semántico no es una patología de
ningún documento particular sino un comportamiento transversal del par
esquema-extractor sobre todo el corpus medido.

## Reproducibilidad

Todos los números de este documento se recomputan desde
`worksheet_fichas_esq2.json` + `seleccion_muestra_esq2.json` (marcas q1/q2/q3
cruzadas con el origen persistido; Wilson 95 % estándar). Verificación
cruzada mesa/autora por recomputo independiente: coincidente en la totalidad.
