# U-R9-FREQ — Frecuencia del subtipo de Obligacion

Analisis de frecuencia para el retoque R9 del laudo ESQ-3a: que valores
merecen entrar al enum de `Obligacion.properties.tipo`
(`data/experiment/reextraccion_v2/e1_extractor/prompt_e1.py:77`).

Reproduce todos los numeros de este documento: `python3 data/experiment/esq/code/frecuencia_subtipos_r9.py`
Selftest del agrupador: `python3 data/experiment/esq/code/frecuencia_subtipos_r9.py --selftest`
Costo de API: USD 0 (el script no hace ninguna llamada LLM).

## 0. Base de datos leida

- Archivos: 10 (`data/experiment/esq/cobertura/*/extracciones_e1_*.jsonl`)
- Extracciones: **762** (con error: 0)
- Entidades `Obligacion`: **977** en `validacion.entidades`
- Control: `tool_input_crudo.entities` da 977 — coinciden: si

Los sha256 de los diez archivos de entrada estan en el JSON companero, campo
`meta.sha256_archivos`. El script no escribe nada bajo `cobertura/` salvo sus
dos propias salidas.

## 1. Distribucion de `Obligacion.properties.tipo` (las 977)

| valor | n | % de Obligacion | unidades | TOs | en enum vigente |
|---|---:|---:|---:|---:|---|
| `otra` | 545 | 55.8 % | 363 | 10 | si |
| `presentacion_informativa` | 300 | 30.7 % | 201 | 10 | si |
| `comunicacion_a_cliente` | 60 | 6.1 % | 56 | 9 | si |
| `calculo` | 41 | 4.2 % | 24 | 6 | si |
| `asignacion` | 29 | 3.0 % | 22 | 6 | si |
| `registro_contable` | 2 | 0.2 % | 1 | 1 | **NO** |
| **total** | **977** | 100 % | | | |

- Valor fuera del enum vigente: `registro_contable` (2), TOs ['prevmi'].

### 1.b Verificacion del 76 % de `otra` medido en la lectura

- Sobre las **75 fichas** leidas en U-ESQ-2: `otra` en **68 de 89** = **76.4 %**.
- Sobre el corpus completo de 977 `Obligacion`: **55.8 %**.

El 76,4 % es el numero de la lectura y se reproduce exactamente sobre el
subconjunto de las fichas; la cifra del corpus completo es mas baja. La
nota contemporanea que registra ese 76,4 % (68/89) esta en la observacion
de la **ficha 12** del worksheet, y la **ficha 17** la vuelve a citar; el
mandato de esta unidad la atribuye a la ficha 39, cuya observacion trata
otro asunto. Se reporta la discrepancia sin resolverla: manda el archivo.

## 2. Agrupacion mecanica de las `otra`

Regla del agrupador (sin LLM, todas las reglas visibles en el codigo):

1. Normalizacion: minusculas, sin diacriticos, solo letras, espacios colapsados.
2. Nucleo, en este orden: (i) primera palabra de contenido **posterior al primer
   marcador deontico o copulativo** (`deberan`, `podra`, `sera`, `queda`, ...);
   (ii) si no hay marcador, la primera forma finita de **futuro o condicional**
   —se prueba sobre el token con tildes, que es lo que la separa de sustantivos
   en -era/-ara—; (iii) si tampoco la hay, la primera palabra de contenido. Las
   palabras funcionales (articulos, preposiciones, pronombres, conjunciones,
   demostrativos, auxiliares de pasiva) se saltean por lista cerrada.
3. Raiz = nucleo menos enclitico pronominal, menos **un** sufijo de la lista
   ordenada, menos vocal tematica final; con raiz minima de 4 caracteres.
4. Un grupo = una raiz. **No hay tabla semantica de sinonimos**: verbos distintos
   con el mismo sentido caen en grupos distintos, y los grupos imperfectos quedan
   a la vista (columna `formas de superficie`).

- `otra` agrupadas: **545**
- Grupos formados: **236**
- Suma de los grupos: **545** (consistente: si)

## 3. Criterio de corte aplicado

Criterio **sellado en el mandato antes de mirar distribucion alguna** (no
calibrado): un grupo merece valor propio si aparece en **>= 15 unidades**
y en **>= 4 de los 10 TOs**. Orden entre los que pasan: conteo descendente.

Grupos que pasan: **3** de 236.

### 3.a Grupos que PASAN

| # | raiz | etiqueta | n | unidades | TOs | formas de superficie |
|---:|---|---|---:|---:|---:|---|
| 1 | `cont` | contar con la | 22 | **20** | **7** | contar, contarse |
| 2 | `cumpl` | cumplir las siguientes | 18 | **15** | **4** | cumplir, cumplirse, cumpla, cumplimiento, cumplido |
| 3 | `observ` | observarse las normas | 17 | **15** | **7** | observarse, observar, observaran, observados, observadas |

**`cont`** — TOs: actgar, adrei, ayccef, cryl, expaef, prevmi, traval

- `actgar::2.3.4` — "contar con la previa autorización de la Superintendencia de Entidades Financieras y Cambiarias (SEFyC)"
- `adrei::1.4.1` — "Las entidades deben contar con políticas y procesos para tales casos excepcionales."
- `adrei::S2::chapeau_seccion` — "las entidades financieras alcanzadas deben contar con un marco de gobierno"

**`cumpl`** — TOs: adrei, ayccef, expaef, opefci

- `adrei::1.4::intro` — "Las entidades financieras alcanzadas deben cumplir con todas las disposiciones previstas en las presentes normas en forma simultánea, es decir que el cumplimiento de unas disposiciones no debe ir en detrimento de otras."
- `adrei::2.1.2::intro` — "Las capacidades de agregación de datos sobre riesgos deben cumplir con los requisitos que a continuación se detallan"
- `adrei::4.2.1::intro` — "Los informes de gestión de riesgos deben [cumplir requisitos a detallar en incisos siguientes]"

**`observ`** — TOs: ayccef, ctacor, expaef, lavdin, opefci, prevmi, traval

- `ayccef::2.2` — "Los requisitos establecidos para la autorización de entidades financieras deberán ser observados en forma permanente."
- `ctacor::2.2::cierre` — "La entidad local requirente deberá observar esos requisitos a través de, por ejemplo, la obtención de constancias de información pública, copia del certificado global de la 'USA Patriot Act' o suscripción a los Principios Wolfsberg por parte de la entidad del exterior"
- `expaef::1.5.1.2` — "En el local donde funcionará la sucursal deberá observarse lo dispuesto en las normas sobre 'Medidas mínimas de seguridad en entidades financieras' y en las demás disposiciones legales vigentes"

### 3.b Grupos que NO pasan (los 30 mayores)

| raiz | etiqueta | n | unidades | TOs | falla por |
|---|---|---:|---:|---:|---|
| `conten` | contener como minimo | 19 | 6 | 3 | unidades 6 < 15; TOs 3 < 4 |
| `establec` | establecer procedimientos integrados | 17 | 13 | 4 | unidades 13 < 15 |
| `entidad` | entidades financieras locales | 13 | 12 | 4 | unidades 12 < 15 |
| `aplic` | aplicacion a los | 12 | 11 | 5 | unidades 11 < 15 |
| `realiz` | realizar las operaciones | 12 | 12 | 6 | unidades 12 < 15 |
| `consider` | considerar el posible | 10 | 8 | 4 | unidades 8 < 15 |
| `manten` | mantenerse en la | 9 | 9 | 4 | unidades 9 < 15 |
| `constitu` | constituir previsiones por | 8 | 8 | 2 | unidades 8 < 15; TOs 2 < 4 |
| `liquid` | liquidacion mediante la | 8 | 6 | 2 | unidades 6 < 15; TOs 2 < 4 |
| `evalu` | evaluara la informacion | 7 | 7 | 5 | unidades 7 < 15 |
| `integr` | integrar con las | 7 | 7 | 4 | unidades 7 < 15 |
| `sujet` | sujetas a la | 7 | 7 | 3 | unidades 7 < 15; TOs 3 < 4 |
| `tener` | tener calificacion o | 7 | 4 | 3 | unidades 4 < 15; TOs 3 < 4 |
| `efectu` | efectuara a la | 6 | 6 | 5 | unidades 6 < 15 |
| `tomar` | tomar en consideracion | 6 | 6 | 4 | unidades 6 < 15 |
| `certific` | certificadas por el | 5 | 4 | 2 | unidades 4 < 15; TOs 2 < 4 |
| `conserv` | conservar por los | 5 | 5 | 3 | unidades 5 < 15; TOs 3 < 4 |
| `cuent` | cuenta de registro | 5 | 5 | 4 | unidades 5 < 15 |
| `inclu` | incluir por la | 5 | 5 | 4 | unidades 5 < 15 |
| `indic` | indicar conyuge y | 5 | 3 | 2 | unidades 3 < 15; TOs 2 < 4 |
| `asegur` | asegurarse de que | 4 | 3 | 1 | unidades 3 < 15; TOs 1 < 4 |
| `capac` | capaces de generar | 4 | 4 | 1 | unidades 4 < 15; TOs 1 < 4 |
| `enunc` | enunciar las medidas | 4 | 1 | 1 | unidades 1 < 15; TOs 1 < 4 |
| `habilit` | habilitar formalmente a | 4 | 4 | 3 | unidades 4 < 15; TOs 3 < 4 |
| `librement` | libremente se convenga | 4 | 4 | 1 | unidades 4 < 15; TOs 1 < 4 |
| `pact` | pactara libremente entre | 4 | 4 | 1 | unidades 4 < 15; TOs 1 < 4 |
| `recib` | recibiran por la | 4 | 3 | 2 | unidades 3 < 15; TOs 2 < 4 |
| `solicit` | solicitara autorizacion para | 4 | 4 | 2 | unidades 4 < 15; TOs 2 < 4 |
| `utiliz` | utilizar los mismos | 4 | 4 | 3 | unidades 4 < 15; TOs 3 < 4 |
| `acompan` | acompanada de su | 3 | 3 | 2 | unidades 3 < 15; TOs 2 < 4 |

Los 233 grupos que no pasan estan completos, con sus ejemplos
verbatim y sus TOs, en `frecuencia_subtipos_r9.json`, campo `grupos`.

### 3.c Sensibilidad del umbral (informativa — NO se aplica)

El criterio aplicado es el sellado. Esta tabla solo muestra cuan cerca del
borde quedo el resultado; no reemplaza ni recalibra el corte.

| umbral unidades | umbral TOs | grupos que pasarian |
|---:|---:|---|
| 10 | 3 | 7: `cont`, `cumpl`, `establec`, `observ`, `entidad`, `aplic`, `realiz` |
| 10 | 4 | 7: `cont`, `cumpl`, `establec`, `observ`, `entidad`, `aplic`, `realiz` |
| 15 | 3 | 3: `cont`, `cumpl`, `observ` |
| 15 **(sellado)** | 4 | 3: `cont`, `cumpl`, `observ` |
| 20 | 4 | 1: `cont` |
| 15 | 5 | 2: `cont`, `observ` |

## 4. Alcance

Este documento entrega la medicion. **No propone ni decide** la lista final de
valores del enum: el laudo ESQ-3a fija el maximo en 3 valores adicionales sobre
`reporte_al_supervisor`, ya anclado, y la seleccion es de la autora con la mesa.

Limitaciones conocidas del agrupador, declaradas antes de leer la tabla:

- Sin tabla de sinonimos: raices semanticamente vecinas quedan separadas, de modo
  que los conteos por grupo son **cota inferior** de la frecuencia del contenido.
- El nucleo se toma tras el **primer** marcador deontico: en una descripcion cuya
  primera copula pertenece a una relativa del sujeto, el nucleo cae en el sujeto y
  no en el predicado. Esos casos forman grupos nominales visibles.
- El recorte morfologico es de un solo sufijo con raiz minima de 4: pares como
  `pago` / `pagar` no se funden. Se deja asi, no se fuerza.
