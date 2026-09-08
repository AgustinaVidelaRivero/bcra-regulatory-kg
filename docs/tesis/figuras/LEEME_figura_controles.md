# figura_controles (F3) — registro de generación

Figura F3 del capítulo del esquema: **los cuatro controles del canal abierto**,
corridos en escalera antes de admitir ninguna medición. Generada POR SCRIPT
desde los artefactos sellados de los cuatro controles, nunca dibujada a mano,
como F1, F1b y F2.

La figura no repite la tabla `tab:controles`: la tabla da las nueve celdas
sueltas, y lo que la figura agrega es la **estructura causal** —la regla de
orden por la que ningún control se corrió sin que el anterior fallara de una
forma determinada— más el **cambio de papel del grupo de diez unidades
limpias** entre el tercer control y el cuarto.

## 1. Comando de generación

```bash
python3 docs/tesis/figuras/generar_figura_controles.py
```

Escribe `figura_controles.svg` (1144 × 1217,5 px). De ahí sale el PDF
vectorial, que es lo que entra al documento:

```bash
rsvg-convert -f pdf -o docs/tesis/figuras/figura_controles.pdf docs/tesis/figuras/figura_controles.svg
```

`rsvg-convert` (2.62.3) es la única herramienta externa, y solo para esa
exportación. El SVG lo produce Python de la biblioteca estándar, sin
dependencias.

**No se genera PNG.** F1 y F1b insertan `.png` explícito y F2 conserva uno de
respaldo; acá el `\includegraphics` va sin extensión, pdflatex resuelve `.pdf`
antes que cualquier otra cosa y el PNG no se usaría nunca. Si en algún momento
hace falta uno (una lámina, una presentación), sale del mismo SVG con
`rsvg-convert -z 2 -f png`.

| Archivo | Medida propia | Peso |
|---|---|---|
| `figura_controles.svg` (fuente) | 1144 × 1217,5 px | 15,6 KiB |
| `figura_controles.pdf` (vectorial) | 858,00 × 913,125 pt = 302,68 × 322,13 mm | 47,7 KiB |

**Sobre los 858,00 × 913,125 pt del PDF.** No son los 1144 × 1217,5 del SVG
porque el punto PDF y el píxel SVG no son la misma unidad: `rsvg-convert` lee
las unidades de usuario del SVG como píxeles CSS (1/96 de pulgada) y las
escribe como puntos (1/72), de modo que el número queda multiplicado por 0,75
—1144 × 0,75 = 858,00 y 1217,5 × 0,75 = 913,125, exacto—. El tamaño físico es
el mismo. Como el bloque LaTeX inserta con `width=\linewidth`, la figura se
escala a 150 mm venga de donde venga.

**El PDF es vectorial de verdad**: cero objetos `/Subtype /Image`, con las
fuentes embebidas y subsetadas. Recomputables:

```bash
pdfinfo docs/tesis/figuras/figura_controles.pdf | grep 'Page size'
pdffonts docs/tesis/figuras/figura_controles.pdf
```

**Reproducibilidad: el SVG sí, el PDF no, y el invariante que sí sirve.**

El **SVG es byte-reproducible**: corridas repetidas dan el mismo sha256
(`259986e9…`) —no hay fechas, ni aleatoriedad, ni rutas absolutas, y toda
iteración va sobre listas declaradas—. El script corre además desde cualquier
cwd (probado desde `/tmp`, con salida idéntica).

El **PDF no lo es**. Doce corridas de `rsvg-convert` sobre el MISMO SVG dieron
**cuatro sha256 de archivo distintos** (4 + 5 + 2 + 1), y el archivo que quedó
en el árbol es un quinto: no hay un sha «correcto» que verificar. La causa NO
es un sello de tiempo:
estos PDF no tienen `/CreationDate`, ni `/ModDate`, ni `/Producer`, ni `/ID`.
La divergencia está adentro de un objeto `/ObjStm` comprimido (`/N 4`, cuatro
objetos auxiliares empaquetados juntos), cuyo orden de empaquetado cairo no
fija; el archivo cambia de longitud en un byte y con eso cambia también la
tabla de referencias cruzadas, que es todo lo que `cmp` ve. Es el mismo
comportamiento y el mismo objeto en el PDF de F2.

El invariante que sí se sostiene es el **stream de contenido de la página**,
que es lo que efectivamente se imprime. Su sha256 es idéntico en las doce
corridas:

```
f50b86bd585764a9a8d9054c09ad86aa375a6bedf5810af48456093e7575dac0
```

```bash
python3 -c "from pypdf import PdfReader; import hashlib; print(hashlib.sha256(PdfReader('docs/tesis/figuras/figura_controles.pdf').pages[0].get_contents().get_data()).hexdigest())"
```

**Consecuencia práctica**: el sha256 del archivo PDF NO sirve como sello y no
debe usarse para verificar que la figura no cambió. Para eso está el sha256
del SVG, o el del stream de contenido de arriba.

## 2. Dos fuentes, con la frontera declarada

**Los NÚMEROS salen de los artefactos sellados, sin excepción.** Los seis
archivos se LEEN; ninguno se edita.

| Archivo leído | sha256 | Commit |
|---|---|---|
| `data/experiment/esq/control/resumen_control_esq.json` (primer control) | `47100a94b1119bd049080aa5e08fc3c88854f6c0cace98d1b3394feafd4aabf3` | `45e3752` |
| `data/experiment/esq/control/resumen_control_esq_p1bis.json` (segundo) | `0c5c5f256c2175745fd0da6a4d199fbe697ee8f9b52315620e898fc5e32031a8` | `c25273f` |
| `data/experiment/esq/control/resumen_control_esq_p1ter.json` (tercero) | `8b9d0745ceb1f9594fdd09b9ff2609ea3cbc784f498ad9ff051a404ec87cabdc` | `0e50e3d` |
| `data/experiment/esq/control/adjudicacion_descubrimiento_cal.md` (cuarto) | `e019875cc88b37af247842b90bf9faf7eb0a6fc9b27b67ff7a3ed9bd9e6cfb19` | `eadf4a5` |
| `data/experiment/esq/control/resumen_descubrimiento_cal.json` (cruce) | `05afe4170c3fea65dfc92abf3a3264af88267ab3de52eb9b2001e16cbf15068e` | `eadf4a5` |
| `data/experiment/esq/control/diagnostico_control_esq.md` (el 19/20) | `4e68999bdf9742dd4b00f10f7d38771a55c5eb09c6919efd60e44d0ff9d13146` | `d6527a6` |

**Los RÓTULOS DE TEXTO salen de la tabla `tab:controles`, transcrita en la
constante `TABLA_CONTROLES` del script — excepción de fuentes declarada.** La
versión de §3.5 que está hoy en el repo NO es la vigente: la subsección se
tunea fuera del repo y todavía no se commiteó, así que leerla daría el
vocabulario viejo. Por eso los nueve rótulos de grupo se tomaron de la tabla
vigente y no de `main.tex`. Cuando §3.5 se commitee, el cotejo es un `diff`
contra `TABLA_CONTROLES`.

**La frontera está cerrada por una guarda, no por confianza.** Antes de
dibujar, el script cotejea las nueve filas de la tabla transcrita contra los
artefactos —signo, exigencia, obtenido y denominador— y **frena** si alguna
discrepa, sin dibujar ninguno de los dos valores. Al cierre de esta unidad las
nueve coinciden.

**Por qué el cuarto control se lee de un `.md` y no del `.json` de su corrida.**
El `resumen_descubrimiento_cal.json` declara en su propia clave
`conteo_mecanico.nota` que es un conteo preliminar y que **NO computa P-cal**:
la validez de cada detección se adjudica fila por fila con la regla sellada del
pre-registro. El veredicto vive entonces en la tabla «Cómputo contra P-cal» de
`adjudicacion_descubrimiento_cal.md`, y de ahí lo parsea el script. El json se
lee igual, como **cruce**: la única dopada sin detección posible (cero
hallazgos) es `dop::tipo::pro::1.1.1`, que es exactamente la única fila marcada
NO VALE en la adjudicación. Son dos medidas distintas —«trajo hallazgos» contra
«la detección vale»— y el script verifica que no se contradigan.

**Las siglas internas (P1, P1′, P1″, P-cal) viven en el script y en este
LEEME, y no se muestran en la figura**: son el nombre de la predicción sellada
de cada control, útiles para rastrear el artefacto, y ruido para el lector del
capítulo.

## 3. Qué dibuja, pieza por pieza

1. **Los cuatro controles en secuencia vertical**, en el orden en que se
   corrieron, rotulados «Control primero» a «Control cuarto». Sin siglas y sin
   fechas de corrida.
2. **La regla de orden**, en el rótulo de cada flecha: el motivo por el que
   hubo un control más. El rótulo va EN la flecha —el trazo se interrumpe y el
   texto ocupa la interrupción—, nunca en un cuadro aparte.
3. **Exigencia declarada y resultado observado** por grupo, con marca de
   aprobado / no aprobado. Son 11 celdas: 7 en las tablas de los controles
   (2 + 1 + 1 + 3) y 4 en la columna de la derecha.
4. **El cambio de papel del grupo de diez unidades limpias**, que es lo que
   una tabla de resultados no puede mostrar: corre por la columna de la
   derecha cruzando los cuatro controles, con una espina que lo declara un
   mismo grupo, y la columna se **parte** entre el tercer control y el cuarto,
   que es donde el papel cambia. Arriba del corte acota escrituras indebidas
   en el canal y pasa las tres veces; abajo acota hallazgos falsos de la
   lectura, y es el grupo que falla.
5. **La flecha de salida** hacia la medición de cobertura por lectura.

Dos **bandas** separan los tres controles del canal abierto del cuarto, que
cambia de instrumento: «el canal abierto — extraer y de paso avisar» y «la
consulta separada — preguntar en una llamada aparte».

### Qué se sacó, y por qué

- **Las mitades de los controles segundo y tercero.** Cada uno tenía dos filas
  más, «las 5 que piden un tipo» y «las 5 que piden una relación», ambas
  `0 de 5`: son cuatro filas que no agregan nada al `0 de 10` de la fila de
  arriba, porque un total de cero obliga a que las dos mitades sean cero. El
  script **verifica que efectivamente sean 0 y 0** en los dos controles antes
  de omitirlas; si alguna dejara de serlo, el `assert` frena y la omisión deja
  de estar justificada.
- **Las mitades del cuarto control se conservan**: `4 de 5` y `5 de 5` no se
  deducen del `9 de 10`, y son la evidencia de que el instrumento no falla de
  un lado solo. Van marcadas «de ellas, …» porque son desglose de su fila, no
  grupos aparte, y por eso son los dos únicos rótulos que no salen de la
  columna «Grupo» de la tabla.
- **Las líneas «predicción X · FALSADA» y las fechas de corrida.**

## 4. De dónde sale cada rótulo de flecha

| Flecha | Rótulo | Ancla |
|---|---|---|
| 1 → 2 | «Ningún grupo medía el canal: uno midió la regla de omisión (19 de 20) y el otro se eligió por conducta previa. Falta contenido plantado.» | `diagnostico_control_esq.md:72` («**19/20 unidades re-declararon `omisiones_no_prosa`**») y `:101` («no mide el canal: mide la estabilidad de la regla NO-PROSA»); `adenda_prerregistro_esq1_P1bis.md` §2 (pool contaminado) y §3 (control positivo con contenido plantado). El 19/20 lo parsea el script del diagnóstico y frena si cambia. |
| 2 → 3 | «Corregida la descripción del canal, la única explicación en pie es el lenguaje de cierre del prompt. Declarado antes de correr.» | `adenda_prerregistro_esq1_P1bis.md` §4: «Si A′ falla con la description corregida, la hipótesis viva pasa a ser la competencia del lenguaje de cierre, y el paso siguiente declarado es neutralizar los tres cierres» — escrito ANTES de la corrida del segundo control. |
| 3 → 4 | «Los cierres neutralizados no movieron una sola unidad: el canal abierto queda cerrado sin un tercer retoque, escrito de antemano.» | `adenda_prerregistro_esq1_P1ter.md` §5(c): «el canal declarativo queda declarado inviable con este modelo y este prompt — **no hay tercer retoque de lenguaje**». El «no movieron una sola unidad» es la comparación pareada de `resumen_control_esq_p1ter.json`, que el script recomputa (20 de 20). |
| 4 → salida | «El instrumento ve lo plantado pero inunda de falsos el texto limpio: el censo automático queda cerrado.» | `adjudicacion_descubrimiento_cal.md`, nota de lectura (i) («**Un censo corrido con este instrumento habría sobrecontado la deriva**») y §Declaración de la rama, rama (b) del árbol sellado. |

## 5. Distinción sin color

El informe se imprime sin color, así que aprobado y no aprobado se separan por
**dos canales redundantes que no son el tono**:

- **relleno**: disco lleno contra disco hueco;
- **glifo**: tilde contra aspa, los dos dibujados como trazos, sin depender de
  ninguna fuente ni de ningún carácter Unicode.

El color (verde / granate) es acento redundante y no porta información. Las
dos bandas se separan igual por trazo —continua contra raya-punto—, no por
tono.

**Verificado, no supuesto.** El PDF se rasteriza en escala de grises a unos
600 dpi de la medida impresa y se mide la fracción de tinta dentro de cada
disco:

```bash
pdftoppm -gray -r 300 -singlefile docs/tesis/figuras/figura_controles.pdf /tmp/f3_gray
```

(Los 300 dpi del comando son sobre la página propia del PDF, de 302,68 mm de
ancho; escalada a los 150 mm de `\linewidth` eso son 605 dpi impresos.)

| clase | marcas | tinta mínima | tinta máxima |
|---|--:|--:|--:|
| aprobado (disco lleno) | 7 | 0,848 | 0,849 |
| no aprobado (disco hueco) | 6 | 0,394 | 0,404 |

Separación entre clases: **+0,444**, sin solapamiento. Las 13 marcas son las
11 celdas más las 2 de la leyenda.

## 6. Piso tipográfico, medido sobre el PDF

El piso es duro: **ningún texto por debajo de 8 pt impresos** con la figura a
`width=\linewidth` = 150 mm (a4 con los márgenes laterales de 3 cm de
`main.tex:9`).

El script tiene su propio `assert` sobre el lienzo, pero **la medición que
vale se hace sobre el PDF compilado**. cairo emite los `Tf` con cuerpo 1 y
pone el cuerpo real en la matriz de texto, así que se leen las matrices `Tm`
del stream de contenido y se multiplican por el factor con el que LaTeX
escala la figura, que es exacto por construcción de `width=\linewidth`:
425,197 pt / 858,00 pt = 0,495567.

| cuerpo en el PDF | apariciones | impreso a 150 mm |
|--:|--:|--:|
| 18,750 pt | 5 | **9,292 pt** |
| 16,500 pt | 45 | **8,177 pt** |

**Mínimo impreso: 8,177 pt.** No hay ningún otro cuerpo en el archivo: los dos
que aparecen son los dos que el script declara (25 y 22 px de lienzo, × 0,75).

**Alto impreso: 159,64 mm**, dentro del tope de 160 mm.

`main.tex` NO se compiló para esta medición: **no hay LaTeX instalado en el
entorno** donde se generó la figura (`pdflatex`, `xelatex`, `lualatex`,
`latexmk` y `tectonic` no existen). Lo medido es el PDF de la figura, que es
el objeto que `\includegraphics` embebe y escala; el factor de escala es
exacto y no depende de la corrida de LaTeX. Lo que queda sin verificar por
compilación es la **maqueta**: dónde cae el flotante en la página.

## 7. Guardas: qué frena el script antes de dibujar

Sobre la frontera entre las dos fuentes:

- las nueve filas de la tabla transcrita coinciden con los artefactos en
  signo, exigencia, obtenido y denominador — si alguna discrepa, no se dibuja
  ninguno de los dos valores;
- **todo rótulo de grupo dibujado es, carácter por carácter, una celda de la
  columna «Grupo»** de la tabla, o uno de los dos rótulos de desglose
  declarados aparte;
- las mitades omitidas de los controles segundo y tercero son efectivamente
  `0 de 5` y `0 de 5` en los dos.

Sobre los artefactos:

- primer control: 0/20 con exigencia `>=10 de 20`, 3/10 con `>=7 de 10`,
  10 limpias 0/10 con `<=1 de 10`, y los tres veredictos tal como están en el
  json;
- segundo y tercero: 0/10 con `>=7 de 10`, las dos mitades 0/5 con `>=3 de 5`,
  10 limpias 0/10 con `<=1 de 10`;
- tercero: la comparación pareada trae 20 unidades y las 20 tienen el mismo
  patrón de emisión que en el segundo;
- cuarto: la tabla adjudicada trae exactamente sus cinco condiciones, con
  9/10, 4/5, 5/5, 0 cruces y 7/10, la última marcada `NO pasa`, y el texto
  «P-cal FALSADA» presente;
- cuarto contra su conteo mecánico: 9 con hallazgos, 1 con cero hallazgos, y
  esa una es `dop::tipo::pro::1.1.1`;
- el diagnóstico sigue declarando 19 de 20.

Sobre la maquetación:

- ningún texto excede el ancho de su caja (medido con la tabla de anchos de
  Helvetica, la misma de F2);
- ninguna palabra suelta excede el ancho de su columna al envolver — el
  envolvedor FRENA en vez de recortar o achicar en silencio;
- los rótulos de flecha no pasan de dos líneas y los rótulos de grupo tampoco;
- el título de cada control y su nota entran en una línea;
- ningún bloque vertical se solapa con el siguiente;
- el corte de la columna cae entre el tercer control y el cuarto, y en
  exactamente un hueco entre filas — si dejara de caer ahí, la figura estaría
  afirmando otro cambio de papel;
- las dos glosas de papel entran enteras en el hueco del corte;
- la cabecera de la columna no invade su primera fila;
- la leyenda no pisa el pie;
- ningún cuerpo tipográfico cae por debajo de 8 pt impresos.

**Lo que el script NO garantiza, declarado.** No tiene la guarda general de F2
que prohíbe que un trazo entre en el interior de una caja o cruce el
rectángulo de un rótulo. Acá la geometría es una pila de rectángulos alineados
a una sola columna, y las dos colisiones posibles —la espina contra las glosas
y la espina contra el corte— se resolvieron **estructuralmente** (la espina se
dibuja solo en los huecos entre filas y salta el hueco donde cae el corte) con
su propio `assert`, no por una guarda genérica. Si alguien agrega un trazo
libre a la figura, esa guarda habría que escribirla.

## 8. Bloque de inserción

En `bloque_latex_figura_controles.tex`. Va **al final de §3.5**, después del
último párrafo de la subsección. **La inserción es de la autora**: esta unidad
no toca `main.tex`.
