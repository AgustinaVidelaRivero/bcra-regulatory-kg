# Lectura de la matriz congelada — resultado del protocolo

Aplicación del protocolo de lectura fijado por la autora el 28/09/2026, antes de
abrir la muestra (sub-fila «DECISIÓN ABIERTA DE LA AUTORA — ventana de
corrección posterior a la tanda 0: la matriz congelada frente al uso del
extractor», fila B6.0 fase 2a de `docs/plan_tesis.md`). Escrito el 29/09/2026.
Este documento **no decide la enmienda**: informa el resultado del criterio.

## Fuentes y verificación de las copias leídas

| Archivo | Commit | sha256 | Filas |
|---|---|---|---|
| `reports/u_estudio_matriz/uestmat_muestra_60.csv` (sellada sin leer) | `7e72051` | `09efc7e5…` | 60 (M01–M60) |
| `reports/u_estudio_matriz/uestmat_muestra_complementaria.csv` (sellada sin leer) | `22e124d` | `0e9b381c…` | 45 (C01–C45) |
| `reports/u_estudio_matriz/lectura/uestmat_muestra_60_leida.csv` | `bb90861` | `d0db41d9…` | 60 |
| `reports/u_estudio_matriz/lectura/uestmat_muestra_complementaria_leida.csv` | `bb90861` | `2870cb93…` | 45 |

Verificación del 29/09/2026: cada copia leída tiene las mismas 13 columnas que
su muestra sellada, las mismas filas en el mismo orden y **0 celdas distintas
fuera de `veredicto` y `nota`**; en las selladas esas dos columnas están vacías
en las 105 filas. Las dos selladas siguen iguales a su commit en el árbol
(`git diff --quiet 7e72051 -- …` y `git diff --quiet 22e124d -- …`). Las copias
del árbol son idénticas a `bb90861`.

## Protocolo, tal como está asentado

- Correcta: el texto del fragmento sostiene que el origen es condición (o
  excepción, o se aplica a, según el predicado) del destino; si el nodo parece
  mal tipado pero la relación es cierta, cuenta como correcta y se anota.
- Criterio: se amplía el rango de `condicion_de` a Operacion, y por separado a
  Potestad, si el límite inferior de Wilson al 95 % de su muestra de 30 es
  ≥ 75 %; las no decidibles se excluyen y se reportan; con más de 6 no
  decidibles, el par no se decide con esta muestra. Con 30 filas hacen falta al
  menos 28 correctas; si se excluyen no decidibles, el umbral se recalcula con
  el mismo piso de Wilson.
- Los otros nueve pares (5 filas cada uno) son informativos y no se amplían
  con esta evidencia.
- La decisión final combina esta lectura con E6 y va por la vía de enmienda
  del esquema congelado, con los mentores.

## Resultado del criterio

Wilson al 95 % sobre correctas / (correctas + incorrectas).

| Par | Filas | Correctas | Incorrectas | No decidibles | n | Wilson 95 % | Mínimo de correctas para piso ≥ 0,75 con ese n | ¿Piso ≥ 75 %? | ¿No decidibles > 6? | Resultado |
|---|---|---|---|---|---|---|---|---|---|---|
| Condicion `condicion_de` → Operacion | 30 | 27 | 2 | 1 | 29 | 0,780–0,981 | 27 de 29 | **sí** | no | **cumple el criterio** |
| Condicion `condicion_de` → Potestad | 30 | 27 | 3 | 0 | 30 | 0,744–0,965 | 28 de 30 | **no** | no | **no cumple el criterio** (le falta una correcta) |

Referencia del umbral (mínimo k con piso de Wilson ≥ 0,75): n 30 → 28 (piso
0,787; con 27, 0,744); n 29 → 27 (piso 0,780; con 26, 0,736).

**No decidible (excluida y reportada):**

| Id | Par | Chunk | Nota de la autora (textual) |
|---|---|---|---|
| C10 | → Operacion | `ext::3.17.3.1` | El destino es un concepto que se resta del tope de certificaciones, y su etiqueta («Registro de beneficios cedidos...») apunta al registro del primer parrafo, que es incondicional, mientras su descripcion apunta al monto neteado del 3.17.3.1, que si queda dentro del supuesto «en el caso de que el cliente sea un beneficiario directo»: el material no determina cual de las dos relaciones se afirma. |

**Incorrectas de los dos pares del criterio:**

| Id | Par | Chunk | Nota de la autora (textual) |
|---|---|---|---|
| M02 | → Operacion | `cap::8.4.1.13` | El punto define un concepto deducible («Diferencias por insuficiencia en el calculo de las previsiones») y el «con efecto al cierre del mes siguiente» fija cuando rige esa DEDUCCION, no condiciona el calculo de previsiones, que se rige por otras normas; ninguno de los dos nodos captura el concepto deducible y el origen ya esta contenido en la descripcion del destino. |
| C09 | → Operacion | `ext::3.15.2.2` | El punto enuncia el 3.15.2.2 como condicion del ACCESO de la entidad al mercado de cambios, no de la emision de la garantia: origen y destino son la misma oracion partida en dos (el origen es un fragmento del destino) y lo efectivamente condicionado no aparece como nodo. |
| C22 | → Potestad | `cap::5.1.2` | Origen y destino tienen la descripcion identica («El descalce de plazos de vencimiento se admitira siempre que se cumplan las disposiciones establecidas en el punto 5.4.5.»): el punto enuncia una sola regla y la arista la relaciona consigo misma. |
| C26 | → Potestad | `ext::10.11.2` | La direccion esta invertida: el parrafo del destino amplia que cuenta como operacion garantizada por una agencia oficial de credito a los efectos del 10.11.2, de modo que sirve para establecer el origen, no depende de el. |
| C38 | → Potestad | `ext::3.15.1` | Son dos reglas distintas con sujetos distintos: el destino condiciona el acceso de la ENTIDAD a que el deudor haya precancelado, y el origen exige conformidad previa del BCRA para el acceso de los CLIENTES; el deudor puede precancelar sin acceder al mercado de cambios, con lo que el origen no condiciona al destino. |

Correctas anotadas como mal tipadas (regla «cuenta como correcta y se anota»):
una búsqueda por patrón (`tipad|tipo|debería ser|es en realidad` sobre la
nota) encuentra M11 (→ Potestad: «el destino esta tipado como Potestad…»). La
búsqueda no es exhaustiva.

## Tabla informativa: los otros nueve pares

No se amplían con esta evidencia (5 filas cada uno; fracciones crudas, sin
porcentaje).

| Par | Correctas | Incorrectas | No decidibles | Wilson 95 % |
|---|---|---|---|---|
| Condicion `aplica_a` → Sujeto | 5 | 0 | 0 | 0,566–1,000 |
| Condicion `condiciona` → Operacion | 5 | 0 | 0 | 0,566–1,000 |
| Definicion `aplica_a` → Sujeto | 5 | 0 | 0 | 0,566–1,000 |
| Excepcion `exceptua` → Operacion | 5 | 0 | 0 | 0,566–1,000 |
| Excepcion `exceptua_obligacion` → Restriccion | 5 | 0 | 0 | 0,566–1,000 |
| Condicion `condicion_de` → Definicion | 4 | 1 (M39) | 0 | 0,376–0,964 |
| Excepcion `exceptua` → Condicion | 4 | 1 (M51) | 0 | 0,376–0,964 |
| Excepcion `exceptua_obligacion` → Operacion | 4 | 1 (M47) | 0 | 0,376–0,964 |
| Condicion `condicion_de` → Condicion | 1 | 4 (M56–M59) | 0 | 0,036–0,624 |

Total de la lectura: 105 filas, 92 correctas, 12 incorrectas, 1 no decidible.

**Observación de la mesa, informativa:** cinco de las doce incorrectas son
aristas entre dos nodos con la misma descripción, que la nota de la autora
describe como una arista del punto «consigo misma»: C22 y M56–M59. No es parte
del criterio.
Una sexta fila también tiene origen y destino con la misma descripción y está
leída como **correcta**: M50 (Excepcion `exceptua_obligacion` → Operacion,
`ext::8.5.17.25`, con etiquetas distintas). Una regla que retirara estas aristas
sin revisión habría retirado una correcta en esta muestra (agregado el
29/09/2026).

## Contexto, no criterio: precisión de la observación (12)

Desde `reports/tanda0/obs12_lectura/fila_obs12.md`: 25 de 30 aristas de
extracción correctas contra el texto en el ensamblado de la tanda 0 sola
(`ens_cinco/r1/kg.json`, `4097d4fd…`), Wilson al 95 % 0,664–0,927, 0 no
decidibles. No es comparable con esta lectura: (12) mide aristas **aceptadas**
por la matriz actual y verificadas en E3, y su muestra no contiene ninguna
arista `condicion_de`; esta lectura mide relaciones que E1 emitió y la matriz
**rechazó** por `firma_invalida`, antes de E3. El efecto medido por
U-ESTUDIO-MATRIZ (+627 aristas en KG-Tanda0-Desarrollo-r1) es una cota
superior porque supone que lo que pasa a válido entra sin re-verificar en E3.

## Pendiente de la decisión (no se decide aquí)

El prompt congelado declara el rango actual de `condicion_de`: la tabla de
firmas de `PREFIJO_SISTEMA_CONGELADO`
(`data/experiment/esq/code/prompt_congelado.py`, prefijo `e69feaaa…`) dice
«`condicion_de` | Condicion → {Excepcion, Obligacion, Restriccion}», y la
instrucción de Condicion manda conectarla «con `condicion_de` a la Excepcion,
Obligacion o Restriccion del mismo chunk». Si se amplía la matriz, el prompt
queda desalineado. Opciones:

1. **Cambiar el prompt.** Rota el prefijo de E1; los diez documentos de la
   tanda 0 se re-extraen, o se revalidan declarando la mezcla.
2. **Ampliar solo el validador.** El prompt sigue declarando el rango actual.

Es decisión de la autora con los mentores, junto con el choque entre las
incorrectas `E1-prompt` de la observación (12) (`BKL-0032`, `BKL-0033`,
`BKL-0035`, `BKL-0036`) y la §3.2 del laudo de r2, que prohíbe cambiar el
prefijo de E1 para preservar la caché. La incorrecta de capa `catálogo`
(`BKL-0034`) cae en el mismo prefijo.

## Reproducción

```bash
python3 -c "
import csv,math
from collections import Counter,defaultdict
z=1.959963984540054
def w(k,n):
    p=k/n; d=1+z*z/n; c=(p+z*z/(2*n))/d; h=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/d; return round(c-h,3),round(c+h,3)
by=defaultdict(Counter)
for f in ['reports/u_estudio_matriz/lectura/uestmat_muestra_60_leida.csv','reports/u_estudio_matriz/lectura/uestmat_muestra_complementaria_leida.csv']:
    for r in csv.DictReader(open(f,encoding='utf-8-sig')): by[r['par']][r['veredicto']]+=1
for p,c in by.items():
    n=c['correcta']+c['incorrecta']; print(p,dict(c),n,w(c['correcta'],n))
"
```
