# Guarda 2 — encaje del material del bloque A en el esquema congelado

Unidad U-COB-A, fase A.1. **Cotejo A MANO, sin extraer y sin API.**

## 1. Contra qué coteje

Esquema congelado del gate ESQ-3 (`docs/../data/experiment/esq/laudo_esquema_congelado.md`,
firmado 03/09), verificado en sesion contra su materializacion:

```
python3 -c "import sys;sys.path.insert(0,'data/experiment/esq/code');import prompt_congelado as p;\
print(len(p.ENTITY_TYPES_CONGELADO),len(p.PREDICATES_CONGELADO),len(p.OBLIGACION_TIPO_CONGELADO),p.PREFIJO_SHA256_CONGELADO)"
```
→ `9 13 6 e69feaaa04779bd6347cc9e3974d2c1749519f1230e70a0459e66f46517cd720`,
coincidente con el sha declarado en el laudo §4.

- **9 tipos**: Comunicacion, TextoOrdenado, Operacion, Restriccion, Excepcion,
  Obligacion, Potestad, Condicion, Definicion.
- **13 predicados**: establecida_en, referencia, modificada_por, aplica_a,
  regula, exceptua, exceptua_obligacion, prohibe, limita, ejecuta, requiere,
  condiciona, condicion_de.
- **enum Obligacion.tipo (6)**: presentacion_informativa, calculo, asignacion,
  comunicacion_a_cliente, reporte_al_supervisor, otra.

## 2. Regla de seleccion de la muestra (fijada ANTES de mirar el contenido)

Un bloque por cada uno de los DIEZ documentos = **el primer bloque de ≥150
caracteres de la primera pagina de clase `prosa` o `mixta`**. La regla cubre
los diez por construccion, toma el material en su forma mas favorable al
esquema (prosa, no planilla) y no permite elegir el pasaje: es el primero que
alcanza el largo minimo. Artefacto: `guarda2_muestra.json`; regenerable con
`python3 code/muestra_guarda2.py`.

## 3. Veredicto por muestra

| # | documento | veredicto | tipos y predicados que la cubren | salvedad |
|---|---|---|---|---|
| 1 | ri_con p.1 off.1 | **cabe** | Obligacion(presentacion_informativa) · Sujeto · aplica_a · Condicion · condicion_de · establecida_en | — |
| 2 | ri_spi p.1 off.1 | **cabe** | Obligacion(reporte_al_supervisor) · Sujeto · aplica_a · Operacion · regula | — |
| 3 | ri_tii p.1 off.0 | **cabe con salvedad** | Obligacion(presentacion_informativa) · Sujeto ×2 · aplica_a · Condicion · condicion_de | S1 (plazo sin campo) |
| 4 | ri_rem p.1 off.1 | **cabe con salvedad** | Obligacion(calculo / otra) · establecida_en | S2 (sujeto ausente) · S1 |
| 5 | ri_chr p.1 off.3 | **cabe con salvedad** | Obligacion(otra) · establecida_en | S3 (remision sin arista) |
| 6 | ri_fcem p.1 off.2 | **cabe con salvedad** | Definicion · Sujeto · aplica_a · establecida_en | S3 |
| 7 | ri_itme p.1 off.4 | **cabe con salvedad** | Obligacion(calculo) · Condicion · condicion_de | S2 |
| 8 | ri_pfmipyme p.1 off.1 | **cabe** | Obligacion(presentacion_informativa) · Sujeto · aplica_a · Operacion · regula | — |
| 9 | ri_pscpp p.1 off.0 | **cabe con salvedad** | Obligacion(presentacion_informativa) · establecida_en | S2 · S3 |
| 10 | ri_pspii p.1 off.1 | **cabe con salvedad** | Obligacion(presentacion_informativa) · establecida_en | S2 · S1 |

**Recuento (recomputado sobre la tabla): 10 = 3 cabe + 7 cabe con salvedad +
0 no cabe.** Ninguna muestra exigio un tipo o un predicado que el esquema
congelado no tenga. **NO hay pedido de reapertura del esquema.**

## 4. Las tres salvedades, y cual de ellas es nueva

**S1 — el valor del plazo no tiene campo.** «mensualmente», «el dia 22 del
mes siguiente», «el 31 de marzo» quedan dentro del texto de la Obligacion y
no como dato consultable. **NO es una salvedad nueva**: es el limite ya
declarado y diferido del propio esquema — «Hechos con valor / properties en
relaciones → ESQ-RI-3 y C1.7» (laudo del esquema congelado §2, «FUERA del
esquema congelado, con destino»). El bloque A la hereda; no la agrava mas que
cualquier otro documento de regimen informativo.

**S2 — la unidad no nombra a su sujeto obligado.** Es la salvedad
**cuantificada** de este cotejo, y la unica que el bloque A agrava de forma
medible. `aplica_a` necesita un Sujeto en el rango; el registro impersonal del
corpus («se expresaran», «se deberan presentar») deja el sujeto en el titulo
del documento o en una pagina anterior, fuera de una unidad cuya mediana es de
93,5 caracteres.

Medicion con el catalogo de sujetos del propio esquema congelado (70 entradas,
`prompt_congelado.SUJETOS_CATALOGO`), aplicada con el MISMO instrumento a los
dos corpus (`python3 code/senal_sujeto.py`; artefacto `senal_sujeto.json`):

| corpus | unidades | nombran sujeto | fraccion | mediana de caracteres |
|---|--:|--:|--:|--:|
| bloque A (prosa + mixta) | 147 | 41 | **27,9 %** | 93,5 |
| desarrollo (los 1.763 de E0, baseline) | 1.763 | 936 | **53,1 %** | 321 |

Lectura honesta de este par: **el sujeto ausente no lo inventa el bloque A** —
casi la mitad de las unidades del corpus sobre el que se valido el esquema
tampoco lo nombran, y el grafo vigente se construyo igual. Lo que hace el
bloque A es **duplicar la tasa de ausencia** (72,1 % contra 46,9 %). Es una
diferencia de grado con causa conocida (unidades 3,4× mas cortas), no una
incompatibilidad de esquema. Ambas cifras son **cota inferior por superficie
lexica**: cuentan menciones textuales, no resuelven anafora ni sujeto heredado
del encabezado.

**S3 — remision normativa sin arista.** «las disposiciones difundidas a traves
de la Circular RUNOR, Seccion 41…», «el punto 3.5.7.3 de las normas operativas
sobre…»: `referencia` va de TextoOrdenado a Comunicacion, y estas remisiones
apuntan a una seccion o a un punto de otro texto. **NO es nueva**: es la ultima
fila de la tabla de residuos del laudo del esquema congelado §3 —«Remisiones
intra-texto sin arista en E1», familia mayor de q3 en ESQ-2, 11/38 azarosas,
29 % [17, 45]— con destino «E3/ensamblado — B5 la hereda como criterio de
aceptacion». El bloque A la hereda tal cual.

## 5. Veredicto de la guarda 2

**EL MATERIAL CABE EN EL ESQUEMA CONGELADO.** 10 de 10 muestras se cubren con
los 9 tipos y los 13 predicados vigentes; ninguna pide vocabulario nuevo. De
las tres salvedades, dos (S1, S3) son limites ya declarados y con destino
asignado en el propio laudo del esquema, y una (S2) es una **diferencia de
grado medida** contra el corpus de validacion, no una incompatibilidad.

**No corresponde reabrir el esquema, y esta unidad no lo pide.** S2 se lleva a
la fase A.2 como prediccion verificable (§4 del diseno de A.2), que es donde
se puede medir con extraccion real cuantas unidades quedan sin `aplica_a`.
