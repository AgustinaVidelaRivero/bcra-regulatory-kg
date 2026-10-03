# figura_ficha — registro de generación (versión 2)

Figura «una ficha de la medición de cobertura» para la sección 3.8 de la tesis:
una ficha real del instrumento con el que se leyó la cobertura del esquema de
partida, con las respuestas de la lectura marcadas sobre el texto.

- **A la izquierda**, «Unidad de extracción del punto 7.2»: en gris, la cadena
  estructural de la unidad (el título de la sección 7); recuadrado en negro, el
  texto que se extrae, con su título y sus tres párrafos; debajo, «Lugar:
  Autorización y composición del capital de entidades financieras, punto 7.2».
- **A la derecha**, «Extracción cruda»: las seis entidades que produjo el
  extractor, cada una en su caja con su identificador local, su tipo (en
  negrita) y su etiqueta, y las nueve relaciones, cada una con su origen, su
  nombre y su destino, en el orden del registro. Sin la salida del validador.
  La entidad `e5` (Operacion, «Formación de grupo económico») lleva borde
  naranja.
- **Deformación, en naranja**: el tercer párrafo, el que la lectura registró
  como deformado, va sobre fondo naranja claro, y una flecha naranja sale del
  borde del texto a su altura, cruza la calle entre las dos columnas y llega a
  la entidad `e5`.
- **Omisión, en gris azulado**: el tramo «salvo las excepciones que determine
  el Superintendente», del primer párrafo, va sobre fondo gris azulado, sin
  flecha, porque nada de la extracción lo representa.
- **Abajo, la leyenda**, en dos líneas: un recuadro naranja con «Deformación:
  contenido representado con un tipo que no le corresponde» y un recuadro gris
  azulado con «Omisión: contenido que quedó sin extraer».

La figura no lleva números de ficha, identificadores de unidad ni del
documento, nombres de archivo ni commits; sí el documento y el punto, en el
lugar y en el título de la unidad.

## Versiones

- **Versión 1** (02/10/2026): las dos columnas, el párrafo deformado y la
  flecha, y abajo el bloque «Preguntas y respuestas registradas», con las tres
  preguntas de la ficha y los campos registrados, recortados donde llevaban
  números de ficha o referencias internas. Alto 22,56 cm. sha256: generador
  `9dcbe89d3be3ebfea4796412a3bd25a90f482ea81e3c1e5e89f8f74e972e0df5`, SVG
  `dcc13250307dee789c247a0b3ffc1ee890ced1ad25ece7bfcc0359a7be426e28`, PNG
  `3b10f8634b8acc4aa92bbbe69aaa4378e44d6daecf825fc39af5517a6f91eb85`, PDF
  `4842441b87eb459f1a29351030c77f78dec83802f0783587d88817acbc5ce5bc`, LEEME
  `5873b1389b789d77783a13bc9a57cb2405aae763d079f706e9de219e2600001c`.
- **Versión 2** (esta, 02/10/2026). Qué cambió:
  - sale el bloque «Preguntas y respuestas registradas» completo, con sus
    recortes (la cita de la deformación, «por qué no se representa» y la
    tercera pregunta) y su texto propio (título, números, rótulos de los
    campos, la raya de la firma);
  - entra el resaltado de la omisión sobre el tramo exacto de la cita
    registrada en la tercera pregunta, sin flecha;
  - entra la leyenda de dos líneas;
  - las dos columnas, sus datos, el recorte de la etiqueta de `to`, el párrafo
    resaltado en naranja y la flecha a `e5` quedan como en la versión 1, en la
    misma posición. Comparados línea a línea los dos SVG (sin las tres líneas
    de cabecera), de las 42 líneas de la versión 1 que no están en la 2, 40
    son del bloque de preguntas (y ≥ 599,9) y 2 son las líneas del primer
    párrafo que el resaltado de la omisión parte en textos separados
    (sección 4); las 11 líneas nuevas son esos cuatro textos, los dos
    resaltados de la omisión y los cinco elementos de la leyenda;
  - el alto baja de 22,56 cm a **13,67 cm**.

## 1. Cómo regenerar

Desde la raíz del repo (el script también corre desde otro directorio: sus
rutas salen de su propia ubicación):

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_ficha.py
```

Escribe `figura_ficha.svg`, `figura_ficha.png` y `figura_ficha.pdf` junto al
script; con `--salida <directorio>` los escribe en otro lugar. Los controles
corren siempre: el script frena antes de escribir si alguno falla.

Herramientas de la corrida registrada (02/10/2026): `rsvg-convert` 2.62.3
(cairo 1.18.4, pango 1.58.2), y en el `.venv` del repo (Python 3.10.13)
pdfplumber 0.11.10, Pillow 12.3.0 y pypdf 6.10.2. Las métricas reales de
Helvetica salen de `/System/Library/Fonts/Helvetica.ttc`
(`generar_figura_proceso_extraccion.py:625`); sin ellas el script frena, porque
los cortes de línea y la posición del resaltado de la omisión dependen de esas
métricas. Reutiliza por importación `generar_figura_norma_a_grafo.py`
(tipografía, escape, formato del SVG y la marca `[…]`) y
`generar_figura_proceso_extraccion.py` (ancho de 15 cm, paleta, exportación a
300 dpi con la densidad grabada y el medidor), como las figuras hermanas.

## 2. La ficha

**Ficha 53**, unidad `ayccef::7.2` (`worksheet_fichas_esq2.json:6329-6330`), la
misma de la versión 1: de la muestra al azar (`seleccion_muestra_esq2.json:32`,
dentro de la lista `azarosa`), fuera del sorteo paralelo de la lectura (las
diez fichas de `desvios_lectura_esq2.md:36-45`; sus azarosas son las 23, 39, 48
y 65), con deformación registrada (firma `a`) y re-tipado de una definición
(`laudo_ESQ-3a_retoques.md:113-115`). Leída a ciegas: no está entre las fichas
del sorteo paralelo, única fuente de lectura no ciega que declaran los desvíos.
La lectura calificó la unidad como `parcial` (`worksheet_fichas_esq2.json:6473`):
el epígrafe lo dice; la figura no lo dibuja.

El script comprueba en cada corrida que la ficha es de la muestra al azar, que
no está entre las diez del sorteo paralelo, que las azarosas de ese sorteo son
exactamente las 23, 39, 48 y 65 y que cada fila de esa tabla es la ficha del
mismo número en el worksheet.

## 3. Fuentes

| Clave | Archivo | sha256 | Ancla |
|---|---|---|---|
| worksheet | `data/experiment/esq/cobertura/fichas/worksheet_fichas_esq2.json` | `de933cb0b180b50787afadaa0415b709922cc1e2013649b621066a0f056bb7b6` | commit `b2e9e90` (lectura completa); el mismo sha cita `fe_erratas_desvios_lectura_esq2.md:22-24` |
| seleccion | `data/experiment/esq/cobertura/orden/seleccion_muestra_esq2.json` | `6c405e7c61e67b91857a5e2e5b30ce5a65ad13f3f1353e693b8fd7c8a0e0aec3` | commit `a7788c1` |
| desvios | `data/experiment/esq/cobertura/desvios_lectura_esq2.md` | `bb6db3e85d582466e83c1f57a237643af2f8f3c7b471133a2217024fe1815cb7` | firmado en `685fc8a`; versión actual con la adenda del desvío (c), commit `bbac990`, que solo agrega líneas al final: la tabla del §1 no cambió |
| extraccion | `data/experiment/esq/cobertura/ayccef/extracciones_e1_ayccef.jsonl` | `4c132a052d58e460878166975e0d4a212cb26bf289c7fe57230186825a420580` | commit `a7788c1`; registro de la unidad en la línea 186 (único) |
| unidades | `data/experiment/escalado_prep/e0_dry/ayccef/chunks_ayccef.json` | `a1e9a674ff95ecba7d4ee30c09b69a931b4164f37abb6ac56265269531de6796` | commit `111ed19`; el mismo sha declara `sellos_produccion_sha256.json:16` |
| sellos | `data/experiment/esq/cobertura/sellos_produccion_sha256.json` | `0e61230222958855c60572ac00e0c642ccc07000c4b38b4b0b4113dd4ef77869` | commit `a7788c1` |
| excluidos | `data/experiment/esq/documentos_excluidos_esq.json` | `6b4404367a08eddb8a7714bb69e8ab6ea0a16210da742bb9a8d049936fd44e1b` | commit `a7788c1`; declara el sha del PDF en la línea 10 |
| pdf | `data/experiment/escalado_prep/pdfs/ayccef.pdf` | `aa5e3e43a920c904d47e81526ea4a61ea6b683418a2d4890b3254a029e6de9c5` | fuera de git (`.gitignore:35`); el mismo sha en `escalado_prep/descarga_log.json:71` y `escalado_prep/manifest_pdfs.sha256:8` (commit `111ed19`); portada «Texto ordenado al 15/05/2025», última comunicación «“A” 8242» |

Los ocho archivos son, al correr, iguales a `HEAD` (`79a493c`). El instrumento
que generó las fichas es `data/experiment/esq/code/fichas_esq2.py` (commit
`a7788c1`, sha256
`d4d0341b827d8475f94e6815cf3a98017c50b1ba71de8cd2b8bec659e3603340`); el
generador no lo importa: lee su salida.

Qué comprueba el script con las fuentes, en cada corrida:

- el texto y la cadena estructural de la ficha son los del artefacto de
  unidades (`chunks_ayccef.json:9180`, texto en la línea 9190, cadena en la
  9197), y la ficha identifica la unidad como el artefacto (punto 7.2,
  `punto_terminal`);
- las entidades, las relaciones y las omisiones de la ficha son las del último
  (y único) registro de la corrida para la unidad, sin error;
- el PDF es el que declara la lista de documentos excluidos para ese
  documento, y el nombre del documento del lugar es el de las dos primeras
  líneas de la portada;
- cada línea del texto es una línea del PDF (página 34, líneas 45 a 51;
  página 35, líneas 4 a 12, contadas desde 1 en `extract_text_lines`), y la
  cadena estructural está en la página 31, línea 3;
- **los párrafos salen de la geometría del PDF**: una línea abre párrafo si la
  anterior del texto es corta (termina antes del 60 % del ancho de las líneas
  de la unidad) y, en la misma página, el salto es mayor que 1,5 veces la
  interlínea (12,6 pt). Resultado: comienzan en las líneas 1, 7 y 12 del texto
  (contadas desde 0, la 0 es el título), que son las fijadas en
  `INICIOS_PARRAFO`; si no coinciden, frena;
- ninguna línea del texto termina en guion ni tiene blancos de más, así que
  unir las líneas de un párrafo con un blanco no cambia el texto;
- **el párrafo resaltado en naranja** es el que coincide, salvo comillas
  tipográficas y blancos, con la cita textual registrada en la segunda
  pregunta (`worksheet_fichas_esq2.json:6478`; el texto usa “ ”, la cita
  registrada comillas rectas);
- **la entidad de la flecha** (`ENTIDAD_DEFORMADA = "e5"`) es la que nombra la
  respuesta registrada de la segunda pregunta (`:6479`): «qué produjo» empieza
  con `e5,` y contiene `Operacion llamada "Formación de grupo económico"`, el
  tipo y la etiqueta de `e5` en la extracción;
- **el tramo resaltado como omisión** (sección 5) es la cita textual
  registrada en la tercera pregunta, carácter por carácter; está una sola vez
  en un solo párrafo, empieza y termina en límite de palabra, no cae en el
  párrafo deformado, y ningún texto de la extracción la contiene ni dice
  «Superintendente»;
- ningún campo de las respuestas que usa la figura (`CAMPOS_USADOS`,
  `generar_figura_ficha.py:146`: la marca de la primera pregunta, la firma, la
  cita y «qué produjo» de la segunda, la familia y la cita de la tercera) mide
  entre 1020 y 1023 bytes, la banda de truncamiento que fija
  `fe_erratas_desvios_lectura_esq2.md:122` (commit `eafdb04`). De la ficha 53
  solo está truncado `observaciones` (`desvios_lectura_esq2.md:89`), que la
  figura no usa.

## 4. Qué texto sale de qué fuente

Los textos del documento y de la extracción se dibujan sin cambios, salvo el
recorte de la sección 6; el script los reconstruye desde lo dibujado y los
compara con su fuente. Los cortes de línea de la columna izquierda no son los
del PDF: el texto se vuelve a partir por palabras al ancho de la columna. En
las dos líneas del primer párrafo que toca la omisión, cada línea va partida
en textos separados (lo anterior al tramo, el tramo y lo posterior); al
reconstruir, se unen con un blanco donde el texto tiene un blanco y sin nada
donde no («Superintendente» y el punto que lo sigue).

| Parte | Texto dibujado | Fuente |
|---|---|---|
| izquierda | cadena estructural «Sección 7. Información especial.» | `worksheet_fichas_esq2.json:6342` = `chunks_ayccef.json:9197`; PDF p. 31, l. 3 |
| izquierda | título del punto y los tres párrafos | `worksheet_fichas_esq2.json:6337` = `chunks_ayccef.json:9190`; PDF p. 34, l. 45-51 y p. 35, l. 4-12 |
| izquierda | lugar «Lugar: Autorización y composición del capital de entidades financieras, punto 7.2» | texto propio (`generar_figura_ficha.py:497`); el nombre, de la portada del PDF (p. 1, l. 1-2); el punto, de la unidad |
| derecha | entidad `to`, TextoOrdenado, «Información especial — […]» | `worksheet_fichas_esq2.json:6350-6352`, recortada (sección 6) |
| derecha | entidad `e1`, Obligacion, «Requerimiento — elaboración estados financieros consolidados» | `:6361-6363` |
| derecha | entidad `e2`, Obligacion, «Presentación a SEFyC — estados financieros consolidados» | `:6372-6374` |
| derecha | entidad `e3`, Excepcion, «Excepción — accionistas entidad financiera con supervisión consolidada» | `:6383-6385` |
| derecha | entidad `e4`, Restriccion, «Exigencia de auditoría — grupos consolidados del exterior» | `:6392-6394` |
| derecha | entidad `e5`, Operacion, «Formación de grupo económico» | `:6402-6404` |
| derecha | relaciones 1 a 5: `e1` … `e5` establecida_en `to` | `:6413-6439` |
| derecha | relación 6: `e1` aplica_a Sujeto_entidad_financiera (campo `sujeto_id`) | `:6443-6445` |
| derecha | relación 7: `e3` exceptua_obligacion `e1` | `:6449-6451` |
| derecha | relación 8: `e4` aplica_a grupos del exterior (campo `sujeto_propuesto`) | `:6455-6457` |
| derecha | relación 9: `e1` regula `e5` | `:6462-6464` |
| abajo | leyenda «Deformación: contenido representado con un tipo que no le corresponde» y «Omisión: contenido que quedó sin extraer» | texto propio (`generar_figura_ficha.py:167-170`), el que fija la decisión 5 del mandato de la versión 2 |

Las rutas que empiezan con `:` son líneas de `worksheet_fichas_esq2.json`.

**Texto propio de la figura**, fijo en el generador
(`generar_figura_ficha.py:161-170` y `:497`): los títulos «Unidad de
extracción del punto 7.2» (el número sale de la unidad) y «Extracción cruda»;
los subtítulos «Entidades: identificador, tipo y etiqueta» y «Relaciones:
origen, nombre y destino»; el agregado «(sujeto propuesto)» detrás del destino
que viene en el campo `sujeto_propuesto`; las dos líneas de la leyenda; y el
lugar.

No se dibujan: las propiedades de las entidades (descripción, tipo, plazo,
materia, archivo, versión), el padre sugerido del sujeto propuesto
(`Sujeto_sujeto_regulado`), el punto de cada entidad y relación (todos «7.2»),
la lista de omisiones del extractor (vacía), las preguntas y respuestas de la
ficha ni las observaciones de la lectura.

## 5. El tramo omitido

| Qué | Ancla |
|---|---|
| cita registrada en la tercera pregunta: «salvo las excepciones que determine el Superintendente» | `data/experiment/esq/cobertura/fichas/worksheet_fichas_esq2.json:6485` (commit `b2e9e90`), campo `q3_omision.cita_textual` de la ficha 53; familia registrada «potestad omitida» en la línea 6484 |
| el tramo en el texto de la unidad | `data/experiment/escalado_prep/e0_dry/ayccef/chunks_ayccef.json:9190` (commit `111ed19`), líneas 6 y 7 del texto (contadas desde 1): «…semestres, salvo las excepciones que determine el» / «Superintendente.»; en el artefacto, entre «el» y «Superintendente» hay un salto de línea, que al unir las líneas del párrafo pasa a ser un blanco |
| el tramo en el PDF | `data/experiment/escalado_prep/pdfs/ayccef.pdf`, página 34, líneas 50 y 51 |

**Coincidencia carácter por carácter.** El script busca la cita registrada,
tal cual, en los párrafos ya unidos: está una sola vez, en el primer párrafo
(caracteres 417 a 471; la consola lo cuenta como «párrafo 2» porque el bloque
1 es la línea del título). Lo dibujado sobre los resaltados de la omisión,
reconstruido en orden, es `'salvo las excepciones que determine el
Superintendente'`, igual a la cita (`controlar_contenido`, `:882`); nada más va
sobre esos resaltados y ningún otro texto los toca. Verificación aparte, sobre
el SVG releído y con las métricas de Helvetica medidas de nuevo: los dos
rectángulos `#e1e7ee` contienen los textos «salvo las» y «excepciones que
determine el Superintendente», ningún otro texto los cruza, y unidos por un
blanco dan la cita de la ficha (`True`).

La omisión va en dos resaltados porque el tramo cruza un corte de línea de la
columna: «salvo las» al final de una línea y «excepciones que determine el
Superintendente» al comienzo de la siguiente; el punto final queda afuera.

## 6. Recortes

| Pieza | Lo cortado | Por qué |
|---|---|---|
| etiqueta de la entidad `to` | « ayccef» (al final) | identificador interno del documento |

El recorte está en `RECORTES` (`generar_figura_ficha.py:154`) como la lista de
tramos que se conservan; el script comprueba que cada tramo está en la fuente,
en orden, y que el comienzo y el final son los declarados. Los otros recortes
de la versión 1 eran del bloque de preguntas, que salió.

## 7. Controles

El script frena (`SystemExit`, antes de escribir nada) si:

- un candado de sha256 no coincide, o falla cualquiera de las comprobaciones
  de la sección 3;
- **contenido**: lo dibujado no reconstruye cada pieza desde su fuente (58
  piezas en 86 textos); un texto dibujado no tiene pieza; lo que va sobre el
  resaltado naranja no es exactamente el párrafo deformado; lo que va sobre
  los resaltados de la omisión no es, carácter por carácter, la cita
  registrada; un resaltado de la omisión no tiene texto encima; o un texto
  lleva algo de `PROHIBIDOS` (`:171`): «ficha», «ayccef», «::», extensiones de
  archivo, nombres de etapa como «E3», «pre-registro», un hexadecimal de 7 a
  40 caracteres, «chunk», «worksheet», «semilla» o «S7»;
- **textos**, con las métricas reales de Helvetica: un texto por debajo de 7 pt
  impresos a 15 cm, fuera del lienzo, fuera de la caja que lo contiene (a menos
  de 1,5 unidades más medio grosor de su borde) o del resaltado que lo
  contiene, superpuesto a otra caja o a otro resaltado, superpuesto a otro
  texto, o a menos de 1,5 unidades de la flecha o de su punta;
- **cajas**: dos cajas se cruzan, salvo los resaltados, que tienen que quedar
  dentro del texto que se extrae, y las muestras de color, dentro de la
  leyenda;
- **flecha**: un tramo de la flecha o su punta entra en el interior de una caja;
- **margen**: un texto, una caja, la flecha o su punta a menos de 2 mm
  (9,6 unidades) de un borde;
- **registro**: los elementos del SVG releído no son, uno a uno y en orden, los
  registrados por los controles.

Corrida registrada: 86 textos, 14 cajas (cadena, texto, resaltado naranja, dos
resaltados de la omisión, seis entidades, recuadro de la leyenda y dos
muestras), 1 flecha; 0 fallas en los seis controles. Distancias mínimas: texto
a texto 0,1 unidades («Superintendente» y el punto que lo sigue, partes
contiguas de la misma palabra sin superponerse), texto a la flecha 8,1, texto
al borde de su caja 5,0. Márgenes mínimos: izquierdo 2,16 mm, superior
2,29 mm, derecho 2,13 mm, inferior 2,19 mm. Verificación adicional con
`docs/tesis/figuras/verificar_geometria_svg.py` sobre el SVG: 86 textos, 0
nodos, 1 trazo con flecha, 0 fallas.

Pruebas negativas, fuera del repo (harness en el scratchpad que importa el
generador, muta en memoria y llama a la composición y a los controles, sin
exportar): las trece mutaciones frenan.

| Mutación | Resultado |
|---|---|
| calle de −40 (columnas superpuestas) | 118 fallas |
| contenido a 4 unidades del borde izquierdo | 6 fallas de margen |
| un texto sobre el tramo vertical de la flecha, en la calle | «lo toca el trazo» |
| un texto 3 unidades debajo de otro | superposición |
| un texto cortado por el borde de una entidad | superposición con la caja |
| sin el recorte de la etiqueta de `to` | «ayccef» |
| un tramo conservado que no está en la etiqueta | frena la resolución |
| `FICHA = 23` | frena («es del sorteo paralelo») |
| **omisión corrida 11 caracteres en el texto** (sobre «semestres, salvo…») | lo dibujado sobre el resaltado no es la cita registrada |
| **primer resaltado de la omisión movido 40 unidades a la derecha** | «salvo las» fuera de su resaltado |
| **segundo resaltado de la omisión bajado una línea** | 2 fallas: el tramo fuera de su resaltado y el resaltado sobre otra línea |
| **un tramo de la omisión dibujado fuera de su resaltado** | 3 fallas de contenido y de superposición |
| **cita de la omisión que no está en el texto** | frena la resolución («aparece 0 veces») |

## 8. Composición y medidas

Lienzo de 720 unidades para 15 cm (el de la figura de las unidades), con 11
unidades (2,29 mm) de margen. Columna izquierda de la unidad 11 a la 351;
calle de 36 unidades, por donde baja la flecha (en x = 369); columna derecha de
la 387 a la 709; las dos, como en la versión 1. Interlínea de 16; entre
párrafos del texto, 5 unidades más. Leyenda a 20 unidades debajo de la columna
más larga (la derecha, que termina en la 565), en un recuadro de 12 unidades
de aire, muestras de 24 × 16 y filas de 22, como la leyenda de
`generar_figura_experimento_estrategias.py:653-667`.

Resaltados: el del párrafo deformado, de 2,5 unidades arriba y abajo del texto
y de 3 a cada lado del ancho de texto de la columna (4 unidades adentro del
borde del recuadro); los de la omisión, ceñidos al
tramo, con 1 unidad arriba y abajo (menos que las 3 que separan dos líneas,
para que los dos resaltados no se toquen) y 1 a los lados, salvo a la derecha
de «Superintendente», que lo sigue el punto sin blanco.

| Qué | Lienzo | Impreso a 15 cm |
|---|--:|--:|
| títulos de las dos columnas y tipo de cada entidad (negrita) | 14 unidades | **8,27 pt** |
| todo lo demás | 13 unidades | **7,68 pt** |

**Alto: 13,67 cm** (lienzo 720 × 656; PDF 425,2 × 387,5 pt; PNG 1772 × 1615 px
a 300 dpi), dentro de los 14 cm buscados.

Colores, de la paleta compartida: cadena estructural con fondo `#f4f6f8`, borde
`#999999` y texto `#555555`; texto que se extrae con fondo blanco, borde
`#4a5a6a` (1,3) y texto `#1f1f1f`; entidades con borde `#999999` (1,0), la
deformada con borde `#e07b39` (1,6); flecha `#e07b39` (1,6). Los dos
resaltados usan los dos pares de la leyenda de
`generar_figura_proceso_extraccion.py:91-92` y `:137-138`: el naranja
(`#fbe3d3` de fondo, `#e07b39` de borde en la muestra) para la deformación y
el gris azulado (`#e1e7ee` de fondo, `#4a5a6a` de borde en la muestra) para la
omisión. Recuadro de la leyenda blanco, borde `#e2e2e2`, esquinas de 5.

## 9. Salidas y reproducibilidad

| Archivo | sha256 |
|---|---|
| `generar_figura_ficha.py` | `c1c77848b22c28c7bd448f7d6b047926721483d6aa8a10480f7367d80935442d` |
| `figura_ficha.svg` | `42064b88f733e356e198df3d412bc4fb80226273b25ce315cf495b0f5044b489` |
| `figura_ficha.png` (1772 × 1615 px, 300 dpi) | `a41e52399a3f45bdc1f6c68691c8ce5634efd13e65a6f5d695b96f8eed5b333c` |
| `figura_ficha.pdf` (425,2 × 387,5 pt) | `d8e6d5a153bf5a3d6d13d5279e16f2d5dde833f2668fab3be3c76e182d33fb98` |

Stream de contenido de la página del PDF, sha256
`1ccb19169bae421fd6239a3cd567f03f6d939c653a7cf44069357aa60408aa94`;
`/CreationDate` 01/01/1970, porque el script fija `SOURCE_DATE_EPOCH=0` al
llamar a `rsvg-convert`, como las figuras hermanas.

Corridas con `--salida` en el scratchpad, con `PYTHONHASHSEED` 0 y 1
(02/10/2026, 18:35), y una tercera con `PYTHONHASHSEED` 0 a las 18:38: el SVG,
el PNG y el PDF salieron idénticos byte a byte a los de la corrida en
`docs/tesis/figuras/`, y la consola también (salvo las rutas de salida).

Este LEEME cae bajo `.gitignore:180` (`docs/tesis/figuras/*`) sin excepción que
lo libere, como los LEEME hermanos: entra a git con `git add -f`. El generador,
el SVG, el PNG y el PDF entran por las excepciones `.gitignore:208`, `:187`,
`:186` y `:188`.

## 10. Epígrafe propuesto (pendiente de la autora)

> Ficha de la medición de cobertura para la unidad del punto 7.2 de
> Autorización y composición del capital de entidades financieras, tomada de
> la muestra al azar. A la izquierda, la unidad como la recibe el extractor,
> con la cadena estructural en gris y el texto que se extrae recuadrado; a la
> derecha, la extracción cruda, con cada entidad y cada relación. En naranja,
> la deformación: el párrafo que define cuándo dos o más personas forman un
> grupo económico con la entidad quedó representado como la operación
> «Formación de grupo económico», a la que apunta la flecha. En gris azulado,
> la omisión: la potestad del Superintendente de determinar excepciones no
> quedó en ningún elemento de la extracción. La lectura calificó la unidad
> como representada en parte.

## 11. Observaciones

- **Identificadores locales a la vista.** La figura muestra `to`, `e1` … `e5`
  porque las relaciones se listan como origen, nombre y destino. No son
  identificadores de unidad ni de documento.
- **La etiqueta de la entidad del Texto Ordenado** dice «Información especial»,
  que es el título de la sección 7 (PDF p. 31, l. 3), no el nombre del
  documento. Es lo que produjo el extractor y se dibuja así.
- **El gris azulado de la omisión** (`#e1e7ee`) es más claro que el naranja de
  la deformación; en pantalla se distingue del blanco y del gris de la cadena
  estructural (`#f4f6f8`), y la muestra de la leyenda lleva borde. Impreso:
  NO VERIFICADO.
