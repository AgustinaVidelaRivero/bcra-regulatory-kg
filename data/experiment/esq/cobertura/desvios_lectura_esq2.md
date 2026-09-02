# Desvíos de la lectura de ESQ-2 — declaración para el análisis y para ESQ-3

**FIRMADO por la autora — 02/09/2026.** Este documento registra los dos desvíos ocurridos durante
la lectura de las 75 fichas de ESQ-2 (worksheet
`cobertura/fichas/worksheet_fichas_esq2.json`, sellado sin marcas en `a7788c1`;
lectura de la autora del 01/09/2026), gobernada por el pre-registro
`data/experiment/esq/prerregistro_esq2.md` (`2240c9c`) y su fe de erratas de
ranking (`930f289`). Las marcas de las 75 fichas quedan INTACTAS: acá no se
corrige nada — se declara, se dimensiona y se fija cómo debe leerse. ESQ-3 lee
este documento junto con la tabla de resultados.

## 1. Desvío (a) — lectura ajena visible durante la adjudicación de ~9 fichas

**Qué pasó.** Durante la lectura existió un sorteo paralelo de spot-check
(semilla `20260901:spotcheck`, 10 fichas — reproducido y verificado por la
mesa) cuya lectura estuvo **a la vista de la autora al marcar** la mayoría de
esas fichas. El §5 del pre-registro define el spot-check como re-lectura de
mesa **posterior e independiente**; adjudicar con una lectura ajena visible
desvía de esa regla y vuelve no-ciegas esas adjudicaciones. La autora lo
**declaró ficha por ficha durante la propia lectura** ("SPOT-CHECK
CONTAMINADO... no aporta dato de discrepancia"), que es el manejo correcto:
el desvío está en el registro primario, no reconstruido después.
**Atribución (declaración de la autora)**: la lectura ajena visible era de un
asistente LLM usado como apoyo durante la lectura, corrido **sin costo de
API** — el gasto declarado de la unidad (USD 4,1079) queda correcto y
completo.

**Las 10 fichas del sorteo paralelo** (el contador de la autora llega a
«nueve contaminadas» en la ficha 65; el final exacto del conteo se perdió por
el desvío (b), así que la identidad de la 9.ª —y una eventual 10.ª— entre las
fichas 48 y 66 queda **indeterminada**; los contadores siguen el orden de
lectura re-aleatorizado, no el orden n del worksheet):

| n | chunk_id | muestra | q1 | declaración propia en la ficha |
|---|---|---|---|---|
| 7 | lavdin::1.1::intro | dirigida | parcial | sí |
| 19 | adrei::1.2 | dirigida | parcial | sí |
| 23 | ayccef::1.1.3 | **azarosa** | parcial | sí («van tres») |
| 37 | traval::1.1.1.1 | dirigida | si_completo | no propia — adjudicada antes de que la contaminación se declarara; listada retroactivamente en la ficha 39 |
| 39 | lavdin::3.3.4.3 | **azarosa** | parcial | sí («van cinco») |
| 47 | cryl::1.1 | dirigida | parcial | sí («van seis») |
| 48 | ayccef::3.4.1 | **azarosa** | no | no (estado incierto) |
| 54 | ayccef::2.9.4.1 | dirigida | si_completo | sí (cola truncada) |
| 65 | actgar::2.3.5 | **azarosa** | parcial | sí («van nueve», lista truncada) |
| 66 | expaef::1.1.1 | dirigida | parcial | no (estado incierto) |

**Regla de lectura (conservadora, fijada acá):** ante el conteo incompleto,
todo análisis de sensibilidad trata a las **10** fichas del sorteo paralelo
como contaminadas — incluidas las dos de estado incierto. Eso excluye 4
azarosas (23, 39, 48, 65) y 6 dirigidas.

**Doble tabla de sensibilidad** (muestra azarosa, Wilson 95 %; recomputada por
la mesa desde el worksheet y la selección persistida — ESQ-3 debe leer las
dos):

| medida | azarosa completa (n=38) | azarosa sin las 4 contaminadas (n=34) |
|---|---|---|
| representación parcial o nula (cota superior, sin E3) | 28/38 = 74 % [58 %, 85 %] | 24/34 = 71 % [54 %, 83 %] |
| no representado | 5/38 = 13 % [6 %, 27 %] | 4/34 = 12 % [5 %, 27 %] |
| firma de deformación real (a–g) | 16/38 = 42 % [28 %, 58 %] | 13/34 = 38 % [24 %, 55 %] |

Ninguna magnitud cambia de banda: las conclusiones de ESQ-2 **no dependen**
de las fichas contaminadas. El criterio de decisión de ESQ-3 tampoco: las
candidatas (a) y (d) conservan ≥3 fichas azarosas fuera de las contaminadas.

**Efecto sobre el spot-check de mesa.** El spot-check del §5 lo ejecutó la
mesa después de la lectura, con semilla declarada `20260902`; 2 de sus 10
fichas cayeron sobre contaminadas del sorteo paralelo y se repusieron con
semilla `20260902:topup` sobre el pool limpio. Resultado: **12 fichas
re-leídas, 0 discrepancias**; en las contaminadas la coincidencia no cuenta
como evidencia de lectura independiente. La marca de la autora manda en todos
los casos (regla del §5).

## 2. Desvío (b) — truncamiento de 35 campos de texto a ~1024 bytes

**Qué pasó.** 35 campos largos del worksheet (observaciones y respuestas
extensas de q2) están cortados a mitad de palabra en longitudes agrupadas en
1001–1011 caracteres. El instrumento (`code/leer_fichas_esq2.py`) **no
trunca** — verificado sobre el código: no hay límite de longitud en ninguna
escritura. La causa es el límite de línea del modo canónico de la terminal
(~1024 bytes): `input()` descarta silenciosamente el excedente de una línea
pegada. Se perdieron las colas de esos 35 campos, incluido el conteo final de
contaminadas del desvío (a).

**Campos afectados** (ficha n · campo · longitud conservada):

| n | campo | len | | n | campo | len |
|---|---|---|---|---|---|---|
| 24 | observaciones | 992 | | 53 | observaciones | 1010 |
| 25 | observaciones | 1007 | | 54 | observaciones | 1008 |
| 26 | observaciones | 1000 | | 55 | observaciones | 1008 |
| 31 | q2.que_produjo | 1002 | | 56 | observaciones | 1002 |
| 37 | observaciones | 1003 | | 57 | observaciones | 1001 |
| 39 | observaciones | 1011 | | 58 | q2.por_que | 1008 |
| 40 | observaciones | 1006 | | 59 | observaciones | 1003 |
| 42 | observaciones | 1010 | | 59 | q2.por_que | 1008 |
| 43 | q2.por_que | 1004 | | 60 | observaciones | 1001 |
| 44 | observaciones | 993 | | 62 | observaciones | 1002 |
| 45 | observaciones | 1007 | | 63 | observaciones | 1003 |
| 46 | observaciones | 1000 | | 64 | observaciones | 998 |
| 46 | q2.por_que | 1001 | | 65 | observaciones | 1007 |
| 48 | observaciones | 997 | | 66 | observaciones | 998 |
| 52 | observaciones | 1002 | | 67 | observaciones | 1009 |
| | | | | 69 | observaciones | 1001 |
| | | | | 70 | q2.que_produjo | 1000 |
| | | | | 71 | observaciones | 1006 |
| | | | | 72 | observaciones | 1003 |
| | | | | 73 | q2.por_que | 1006 |

**Regla fijada: la pérdida se declara y NO se reconstruye de memoria.**
Reescribir esos análisis después de haber visto la tabla agregada de
resultados sería post-hoc: el texto repuesto no sería la lectura
contemporánea sino una racionalización posterior. Los 35 campos valen por lo
que conservan; sus colas se dan por perdidas. **Alcance de la pérdida**: las
MARCAS (q1, firma de q2, familia de q3) y las citas textuales están completas
en las 75 fichas — lo truncado es prosa de análisis complementario; ninguna
marca ni cita obligatoria depende de un campo truncado.

**Remedios diferidos** (registrados en `docs/cola_mejoras_diferidas.md`,
entradas 10 y 11): regla transversal de cegado para unidades de lectura, y
arreglo del instrumento para textos largos antes de la próxima unidad de
lectura.

## Firma

Firmado por la autora, 02/09/2026. Las reglas fijadas acá (lectura
conservadora de la sensibilidad, no-reconstrucción de campos truncados) son
vinculantes para el análisis de ESQ-2 y para la lectura que haga ESQ-3.

## Adenda — desvío (c): colisión de la tecla d en q2 (post-sello `685fc8a`)

**FIRMADA por la autora — 02/09/2026.**

El instrumento sellado en `a7788c1` tenía una colisión en P2: la tecla `d`
estaba en la lista de firmas (a–g) y en la rama de duda, y la rama de duda
ganaba — era imposible registrar la firma (d) por teclado. Detectado por la
autora en la **ficha 15**, el primer intento de marcar (d) de la lectura, y
declarado en sus observaciones contemporáneas; la marca de esa ficha se
corrigió por **edición directa del worksheet** (única edición manual de la
lectura, declarada acá: tras la edición, la ficha 15 quedó con **firma (d)**,
y el conteo de 9 firmas (d) de la tabla de resultados la incluye) y el código
se corrigió en el acto (`d`→`?` para duda; viaja con el commit de cierre del
análisis como arreglo de instrumento-roto, regla de la cola). **Alcance
verificado por mesa**: ventana de exposición fichas 1–14; única marca d/duda
en la ventana: la duda de la ficha 5, adjudicada NO sospechosa por doble
evidencia (nota de duda deliberada y auto-documentada sobre el rol
cuarentenado D5; el flujo de duda pide una nota que delata la colisión, como
ocurrió en la 15). Las 9 firmas (d) son todas post-detección. **Impacto sobre
los resultados: ninguno** — en el peor caso contrafáctico la candidata (d)
sumaría una azarosa (6→7); ninguna otra medida se mueve.
