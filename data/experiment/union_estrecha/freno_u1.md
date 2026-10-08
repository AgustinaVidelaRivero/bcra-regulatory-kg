# U-UNION-ESTRECHA — FRENO U1 (la regla y su pre-medición, sin leer ninguna unión)

08/10/2026. USD 0, sin API. HEAD al abrir y al cerrar: `7788e52`. Mandato leído en su commit de firma
(`git show 21e55a0:docs/mandatos/UUNION_ITEM_ENCABEZADO_regla_estrecha.md`, sha256 `6959ca49…`, igual al del árbol;
versión para firmar en `9e84741`). Nada commiteado: el commit es de la autora, PENDIENTE.

## 1. La regla, sellada antes de medir

`regla_u1.md` (sha256 `9f5028d1…`), sellada a las **08:04:06** del 08/10/2026 (`sello_regla_u1.txt`) junto con el
código que la implementa y la mide: `regla_u1.py` `f192663b…`, `premedicion_u1.py` `a4c8c894…`,
`selftest_regla_u1.py` `0a4d2026…`, `comandos_u1.sh` `3072ff66…`. La primera corrida de la pre-medición escribió sus
salidas a las 08:04:14–15. Antes del sello: selftest sintético 44/44 y la reproducción de los 30 ids del control; ni
una cuenta de uniones de esta regla.

En breve (el texto completo, con cada fuente, es `regla_u1.md`):
- solo **Condicion** de ítem sin `condicion_de` saliente (la Excepcion, fuera como nodo del ítem: decisión 1);
- **anuncio** en el tramo de la oración final que rige la lista: forma S, un subordinante de la lista cerrada
  («siempre que», «en la medida que», «cuando», «cada vez que», «toda vez que») que gobierna la lista; forma N, sin
  subordinante, «las/los siguientes condiciones/requisitos/recaudos» o dos frases fijas. Cada expresión con su
  fuente en un bloque que abre lista de los diez TOs; «en tanto» y «en la medida en que», fuera (sin fuente en un
  bloque que abre lista);
- **candidatos**: los nodos del mini-chunk del encabezado con tipo en el rango de `condicion_de` de la matriz r2 (los
  cinco); unión solo con uno;
- **compatibilidad**: forma S → Potestad, Operacion, Obligacion, Excepcion; forma N → sin Obligacion (la lista puede
  ser el objeto de la obligación: «deberá verificar el cumplimiento de los siguientes requisitos», ext::4.6.1); con
  marca de excepción en la oración → solo Excepcion; Restriccion, nunca;
- arista derivada `condicion_de` con `rol_fuente = union_item_encabezado`, la procedencia del ítem y sin marcas de
  E3; todo al registro.

Lo que miré antes de sellar, sin texto de ítems ni de nodos ni veredictos: el texto de los 220 bloques que abren
lista (1.053 ítems) y, en los 69 bloques de alguna Condicion de ítem sin `condicion_de` en `a9631a64`, cuántas son y
los tipos de los nodos de su mini-chunk (`regla_u1.md`, sección 8).

## 2. Pre-medición

Fuente: `salida/premedicion_u1.json` (tablas en `salida/premedicion_u1.md`, filas en `salida/registro_u1_*.json`).

| | `a9631a64` (diez) | `e22fae1a` (sin cola) |
|---|---:|---:|
| Condicion de ítem sin `condicion_de` | 165 | 161 |
| unión | **40** | **37** |
| sin anuncio | 82 | 80 |
| ambigua (2 o más candidatos) | 25 (17 con 2, 3 con 3, 5 con 4) | 25 (17, 3, 5) |
| sin candidato | 14 | 15 |
| sin unidad de encabezado (línea de título) | 4 | 4 |
| destino no compatible | 0 | 0 |

- **Por tipo de destino** (diez): Potestad 21, Operacion 10, Excepcion 9; Obligacion 0, Restriccion 0. Sin cola:
  20, 9, 8.
- **Por TO**: las 40 (y las 37) son de **ext**, en 19 bloques (17 sin cola). Ningún otro TO de la tanda 0 tiene una
  Condicion de ítem sin vínculo bajo un bloque que anuncie, con un solo candidato.
- **Por forma** (diez): S1 26, S2 8, N 6; con marca de excepción 5, todas hacia Excepcion.
- **Sin anuncio por candidatos** (diez): 30 con 0, 21 con 1, 31 con 2 o más.
- **Contra la regla E** (mismo dominio de 165 Condicion): sus 61 uniones de Condicion son las 40 de esta regla más 21
  de un solo candidato sin anuncio (19 hacia Obligacion y 2 hacia Potestad; comparadas fila a fila con
  `union_e.json`, con el mismo candidato). Las compatibilidades
  no excluyen nada en estos grafos: todo el estrechamiento viene del anuncio.
- **Lectura de control del diagnóstico** (30 ids, semilla 20261007, reproducidos y comparados uno a uno con
  `muestra_union_e.md`; 16 Condicion y 14 Excepcion): de las 16 Condicion, la regla une **11** (las 11 con el mismo
  destino que la regla E) y 5 quedan sin anuncio. Esas 11 se excluyen del sorteo de U2.

## 3. Hallazgo para U2: el marco tiene 29 uniones, una menos que la muestra

Marco de U2 en `a9631a64`: 40 − 11 = **29** (`salida/marco_u2_diez.json`). El mandato pide una muestra de 30 «con
semilla nueva» sobre las uniones de la regla, sin las del control: con esta regla no alcanza. La decisión es de la
autora. Opciones, sin recomendar ninguna sobre las otras:
- **U2 como censo de las 29.** Con el criterio del mandato (Wilson inferior ≥ 0,75), el piso con 29 es **27 de 29**
  (0,780; con 26, 0,736). Con 30 era 28 (0,787). No hay sorteo: la semilla deja de hacer falta.
- **Cambiar la regla** para agrandar el marco. Lo que la amplía de verdad (por ejemplo, el subordinante antes de una
  coma de inciso, ext::10.10.2 y ext::13.3) se decide viendo esta cuenta, no los veredictos, pero ya no sería una
  regla fijada antes de medir: habría que sellarla de nuevo y declararlo.
- **Volver a meter las del control**: el mandato las excluye porque ya tienen veredicto; no lo propongo.

## 4. Otras cosas a la vista de la autora

1. **Alcance de la medición**: las 40 uniones son de ext. U2 mide la precisión de la regla en ext; en las otras tandas
   la regla se aplica con la misma lista cerrada, que puede perder uniones pero no agregarlas.
2. **El despacho dice** que la firma está «en el commit de los asientos del 07/10/2026 (noche)»: la firma y sus dos
   decisiones están en `21e55a0` («Firmas de la autora del 07/10/2026 (noche)»); los asientos de `9e84741` traen la
   versión para firmar. El texto que rige es el de `21e55a0`, igual al del árbol.
3. **El despacho no repite «sin las marcas de E3»**; lo tomé del mandato.
4. **Defecto cosmético** en `salida/premedicion_u1.md`: la tabla del cruce lleva «|» dentro de las celdas
   («con_anuncio|0») y se desarma al verse. Es del código sellado; no lo toco. La fuente es el JSON.
5. **Para U3** (no es de U1): `modelos_r2.AristaR2` acepta este `rol_fuente` como texto libre, sin los invariantes de
   la derivada de procedencia (`modelos_r2.py:650-659`). Si U3 los quiere iguales, toca `modelos_r2.py`, fuera de sus
   escrituras.

## 5. Controles

- Copia sin enlaces, armada con `git show 7788e52:<ruta>` (`comandos_u1.sh`): 0 enlaces, 0 `.pyc`. Selftest 44/44.
  Dos corridas por reproducción, byte a byte iguales, y dos reproducciones desde cero; la segunda, igual a
  `salida/` del repo en los 6 archivos.
- Repo: sha256 de todos los archivos salvo `.git` antes (07:46:46, 47.361 archivos) y después (08:07:30): ningún
  archivo existente cambió. Hay 20 archivos nuevos: los 13 míos de `data/experiment/union_estrecha/` y 7 de
  U-COMP-E1 C3, que corre en paralelo (`data/experiment/comp_e1/c3/`, 6, y `comp_e1/freno_c3.md`); los atribuyo
  por ruta. `.pyc` fuera de `.venv`: 2.213 antes y después; la lista de `.pyc` y `__pycache__`, igual.
- No abrí nada bajo `reports/u_diag_cap3_grafo/lecturas/`. Del diagnóstico usé `scripts/udiag_a_union.py` y
  `scripts/udiag_comun.py` como código y, de `salidas/union_e.json` y `salidas/muestra_union_e.md`, los ids, los
  conteos de la regla E y los encabezados `## U`.
- Grep de convenciones sobre `data/experiment/union_estrecha/` y el paquete: en el paquete de revisión.

Escrituras: `data/experiment/union_estrecha/` (`regla_u1.md`, `sello_regla_u1.txt`, `regla_u1.py`,
`premedicion_u1.py`, `selftest_regla_u1.py`, `comandos_u1.sh`, `freno_u1.md` y `salida/` con 6 archivos) y el
scratchpad. Paquete: `revision_UUNION_ESTRECHA_FRENO_U1/`, con `manifest.txt`.

FRENO U1: la autora aprueba el texto de la regla (puntos de `regla_u1.md`, sección 10) y decide el marco de U2
(sección 3). Hasta entonces no sigo.
