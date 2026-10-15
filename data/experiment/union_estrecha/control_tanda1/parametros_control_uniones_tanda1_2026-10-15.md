# U-UNION-ESTRECHA: tamaño, semilla y piso del control de las uniones en los TOs de la tanda 1 (sellados el 15/10/2026, antes de leer)

USD 0. Decisión de la autora del 15/10/2026, recibida a las 13:00:14 (hoja de ruta de la mesa, §102): «Sellá ya el tamaño, la semilla y
el piso del control de las uniones (los de U2).» El control lo aprobó la autora el 08/10/2026 tal como lo propuso la mesa:
- `docs/mandatos/UUNION_ITEM_ENCABEZADO_regla_estrecha.md:168-171`;
- `docs/plan_tesis.md:784`;
- `data/experiment/union_estrecha/u2/freno_u2.md`, §5.

Este archivo fija solo lo que el control dejaba para sellar antes de leer.

## Lo que ya estaba aprobado (no cambia)

- **Cuándo:** con la tanda 1 extraída y ensamblada con U3, antes de sellar el grafo evaluado.
- **Qué se lee:** las uniones de la regla de U3 en los TOs de la tanda 1.
- **Cómo:**
  - con el mismo `criterio_u2.md` y sus ocho precisiones (`data/experiment/union_estrecha/u2/criterio_u2.md`, sha256 `86c7724c…`,
    commiteado en `a91f95f3`);
  - con dos lecturas a ciegas y la adjudicación de la autora.

## Lo que se sella acá

1. **El tamaño:** 30 uniones, sorteadas, o el censo si son 30 o menos. Es la regla de U2 (`docs/plan_tesis.md:784`: «el censo si las
   uniones no llegan a 30»).
2. **La semilla:** `20261015`, nueva y distinta de las de U-UNION-ESTRECHA (`20261007` y `20261008`). U2 fue un censo de 29 y no usó
   semilla.
   - El sorteo es `random.Random(20261015).sample(sorted(ids), 30)`, donde `ids` son los ids de las uniones de la regla en los TOs de la
     tanda 1, ordenados.
   - La lista de `ids` se sella con su sha256 antes de sortear.
3. **El piso:** el de U2, el límite inferior de Wilson al 95 % ≥ 0,75, con z = 1,959964.
   - **Las no decidibles** se declaran y, para el piso, cuentan como no correctas, como en U2 (`criterio_u2.md`, punto 8).
   - **Con 30 uniones** hacen falta 28 correctas.
   - **Con un censo de n < 30,** las correctas mínimas son:

     | n | 12 a 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 |
     |---|---|---|---|---|---|---|---|---|---|---|---|---|
     | mínimo | n (todas) | 18 | 19 | 20 | 21 | 22 | 23 | 23 | 24 | 25 | 26 | 27 |

   - **Con menos de 12** el piso no se alcanza ni con todas correctas. El control se lee igual y su resultado se declara.

## Lo que no fija este sello

- Qué pasa con la regla si el control no llega al piso. El control no lo dice, y queda PENDIENTE de la autora (hoja §102).
