# U-PROMPT-R2, P4b — las unidades de la prueba corta, elegidas por lectura (sellado antes de correr)

**Sello:** `salida/seleccion_p4b.json`, sha256 `e2551cf3c7dd110bf9e10bb4918f13c3d79a7320642843e61eb8ca88b8d9fd09`,
escrito el 04/10/2026 a las 23:01 (-0300), antes de toda llamada a la API de P4b. Script: `seleccion_p4b.py`
(sha256 `b6e4e595…`). E0: la e0-r2 de C2, `e0_chunking/salida_tanda0_r2b/`.
Corrección antes de correr: el script excluía también los ids de los documentos de P4b, así que re-corrido con este
documento en el repo se habría excluido a sí mismo. Ahora salta `p4b/` (era `58188b07…`). La salida es la misma, byte
a byte (sha256 de arriba).
Semilla: `U-PROMPT-R2:P4b:2026-10-04`.

## Cómo elegí

- **Excluidas:** 302 unidades.
  - Las 76 de P4.
  - Toda unidad nombrada en un documento de U-PROMPT-R2 (`data/experiment/prompt_r2/**/*.md`): son los diseños y frenos
    de P1 a P3c-2, con los casos de control de P1 y de P3b-1, el diseño de P3c y la lectura de P4. También, las
    nombradas en las lecturas de U-DIAG-VINCULO que P4 ya excluía, porque se leyeron al escribir la regla f.
  - Los contenedores y los ítems de las diez listas que leyó P4.
  - Es más de lo que pide el «seguí»: es por precaución.
- **Pools** (definidos en palabras en el script, armados por forma y sin leer): a_transicion 153, a 475, c 90, d 473,
  e 61 y listas 29.
- **La lectura.** Leí cada pool en su orden sorteado y tomé los primeros que cumplen la definición del grupo. Cada
  descarte va con su razón en `seleccion_p4b.json`, `lectura`.
  - Descartes: 6 en a_transicion, 0 en a, 5 en c, 1 en d y 7 en e.
  - Las 29 listas, con su tipo.

## Las unidades (27)

| Grupo | Unidades |
|---|---|
| a, régimen de transición | `ext::13.1.4` |
| a | `ext::6.1.1`, `cap::10.3.3.1`, `cap::11.4` |
| b1, ítems | `ctacte::3.2.2`, `ctacte::3.2.5`, `ctacte::3.2.4` |
| b2, ítems | `ext::3.5.3.4`, `ext::3.5.3.5`, `ext::3.5.3.1` |
| b, encabezados | `ctacte::3.2::intro`, `ext::3.5.3::intro` |
| c | `cap::5.3.1.3`, `cla::6.5.4.5`, `ext::10.4.2.5`, `ext::10.3.6` |
| d | `ext::10.4.3.6`, `ext::4.1.4.7`, `polcre::2.1.15`, `cap::10.2.2.4` |
| e | `cap::6.3.2::intro`, `cap::3.2::intro`, `cap::6.3.2.1`, `polcre::5.3` |
| el ejemplo | `cla::5.1.1::intro`, `cla::5.1.1.1` |
| f | `cap::6.2.2.6` |

**Pata de E3 (5):** `ctacte::3.2::intro`, `ext::3.5.3::intro`, `cla::5.1.1::intro` (el encabezado de b1 del ejemplo),
`ext::13.1.4` y `ext::6.1.1`. Son los encabezados de b y los dos primeros de a, el de transición y el primero del
pool.

## Lo que difiere del diseño, declarado

- **27 unidades, no 29.** De las 29 listas leídas, solo 2 son de b, y tienen unidad de encabezado propia: `ctacte::3.2` (b1)
  y `ext::3.5.3` (b2). Por eso los encabezados de b son 2 y no 4, y la pata de E3 tiene 5 unidades y no 6.
- **Las otras listas de b de la tanda 0 están excluidas:** `ext::3.13.1`, `ext::3.6.1`, `ext::3.6.4` y `ext::10.11`. Se
  leyeron en U-DIAG-VINCULO o en P3b.
- **b1 en otra forma, con lectura dudosa.** `ctacte::3.2` dice «El título respecto del que se presentare alguna de las
  siguientes situaciones (…) no valdrá como cheque». Lo leo como lo que queda afuera de una clase: la clase es el
  cheque, y cada ítem nombra una clase de títulos que queda afuera. También admite la lectura de supuestos de una sola
  exclusión, aunque sin una norma con su salvedad. Si la autora la descarta, b1 se mide solo con el ejemplo.
- **`ext::4.1.4.7` (d):** su encabezado se leyó antes, en U-DIAG-VINCULO. El ítem no se leyó; la exclusión es por
  unidad.
