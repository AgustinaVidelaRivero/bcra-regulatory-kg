# U-UNION-ESTRECHA — FRENO U2: la cifra del censo de las 29 uniones

08/10/2026. Redactado por la mesa, con la adjudicación de la autora del mismo día. USD 0, sin API. Commit PENDIENTE de la autora.

## 1. Las dos lecturas, selladas antes de comparar

- Fichas y criterio, sellados a las 10:54:03 (`sello_fichas_u2.txt`): `criterio_u2.md` `86c7724c…`, `fichas_u2.json` `888d0b76…`,
  `fichas_u2.md` `7ab2812e…`. Los sha256 actuales coinciden.
- Primera lectura, de una sesión aparte que no diseñó la regla (U2-a, `freno_u2a.md`): `lectura1_u2.json` `8b23d250…`, sellada a las
  10:58:04 (`sello_lectura1_u2.txt`).
- Segunda lectura, a ciegas, de una sesión nueva de la mesa (U2-b, `freno_u2b.md`): `lectura2_u2.json` `7d7cda3a…`, sellada a las 14:25:18
  (`sello_lectura2_u2.txt`), antes de abrir la primera (14:25:30, declarado en su FRENO); la hoja de las divergencias es de las 14:28:26.
  Los sha256 actuales coinciden con los sellos.
- Acuerdo: 29 de 29 (`divergencias_u2.json`). Kappa no definido: las dos lecturas usan una sola categoría en las 29 fichas.

## 2. La adjudicación de la autora (08/10/2026)

No hubo divergencias. La hoja dejaba a la autora dos fichas, U28 y U29, porque las dos lecturas declararon que el tramo de la Condicion no
está en el texto propio del ítem (`ext::10.4.2.9` y `ext::10.4.2.5`) sino en la intro de 10.4.2 que hereda la unidad. **Decisión:** se
juzgan por la arista, como hicieron las dos lecturas, por la precisión 1 del criterio (se juzga la arista, no la paráfrasis): quedan con el
veredicto de las dos lecturas, correctas.

## 3. La cifra

| | uniones |
|---|---:|
| correctas | 29 |
| incorrectas | 0 |
| no decidibles | 0 |
| total (censo) | 29 |

Límite inferior de Wilson al 95 %: **0,883** (z = 1,959964; superior 1,000). Piso: 27 de 29 (límite inferior 0,780 ≥ 0,75; nota del
mandato del 08/10/2026). **U2 PASA.**

**Límite de la medición:** las 29 uniones son de ext; la cifra mide la precisión de la regla en ext. En los otros TOs, el control antes de
sellar el grafo evaluado (§5).

## 4. Hallazgo de la extracción, no de la unión

En U28 y U29 la Condicion tiene la procedencia mal atribuida: su tramo está en la intro heredada de `ext::10.4.2`, no en el ítem
(`ext::10.4.2.9` y `ext::10.4.2.5`). La unión es correcta por la arista; el defecto es del nodo extraído: E1 tomó la cláusula del bloque que
abre la lista y la atribuyó al ítem. Se declara aparte, como hallazgo de la extracción; no cambia la cifra de U2.

Notas coincidentes de las dos lecturas, sin decisión pendiente: en U24, el tramo del destino es el encabezado heredado de 5.8.2; en U25, la
Condicion es solo el inciso final de 2.7.3 («considerando los límites…»), leído con el cierre de 2.7.

## 5. Cómo sigue

- **U3, la implementación** (mandato, U3), después de U-OMISIONES-COD, que toca el mismo archivo (`ensamblar_tanda0.py`), y antes del armado
  que precede al sello del grafo evaluado: la regla en el ensamblado (fila F15, solo código sobre lo guardado), con su selftest por rama;
  el diff de los grafos r2b con la lista exacta de aristas nuevas (esperadas, por la pre-medición de U1: las 40 de `a9631a64` y las 37 de
  `e22fae1a`); selftest de claves OK, sin claves movidas; nota en la tabla de reprocesamiento. El `rol_fuente` pasa a valor cerrado, con
  invariantes para las aristas derivadas, en un solo cambio de `pyd_r2/code/modelos_r2.py` compartido con B3 de U-APLICA-ROL-ALCANCE (lo
  hace la primera de las dos que llegue a implementar). Entra en el próximo armado de todas las tandas.
- **El control en los TOs de la tanda 1**, antes de sellar el grafo evaluado (nota del mandato del 08/10/2026, punto 4): con la tanda 1
  extraída y ensamblada con U3, una muestra de las uniones de la regla en sus TOs, leída con el mismo `criterio_u2.md` (con sus ocho
  precisiones), en dos lecturas a ciegas y con la adjudicación de la autora. Tamaño, semilla y piso, sellados antes de leer (propuesta de
  la mesa: 30, o el censo si son menos; límite inferior de Wilson ≥ 0,75).

## 6. Controles

USD 0. La mesa verificó los sha256 de las fichas, del criterio y de las dos lecturas contra sus sellos, y recontó el acuerdo y la cifra con
un script propio sobre `lectura1_u2.json` y `lectura2_u2.json`. Escrituras de este FRENO: este archivo y la copia de `freno_u2b.md` (el
FRENO de U2-b, igual al `manifest.txt` de su paquete), en `u2/`; la nota al pie del mandato.
