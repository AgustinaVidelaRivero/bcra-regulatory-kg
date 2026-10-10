# U-OMISIONES-COD — FRENO O1 (09/10/2026)

**Entrada.** HEAD `1e13cbd`. Están la firma de la v7 (`c90d3d9`) y las notas al pie (`c52255f`, el único commit posterior que toca
el mandato; el despacho no daba su hash y lo identifiqué por `git log` sobre la ruta). El texto firmado da `6c8914a0…` en los dos
commits y en HEAD. Leí el mandato en `c52255f`, el §29 de la hoja de ruta de la mesa y, de ese paquete, solo las pre-mediciones de
B y L. Para g1 leí, además, el script de reglas que la v7 cita (`UDIAGLIMITES_l1_clasificar_relativas.py`, sha `7ae07f52…`), en su
paquete fuera del repo. Foto del repo al empezar: 48.977 archivos (salvo `.git`), 2.213 `.pyc`.

**Cómo trabajé.** Todo corrió sobre dos copias del repo hechas con rsync, sin `.git`, sin `.venv` y sin enlaces: `copia` (el
código de HEAD) y `copia_o2` (el código de este diseño, en `parche/`). USD 0, sin API.

**Línea de base.** El código de HEAD no reproduce `a9631a64` sino `40c54830` (diez), y `8d747e57` en vez de `e22fae1a` (sin cola).
Es el cambio de R2-3 (`803623a`), sin re-sellar: +1 propuesto de docvig, 4 `aplica_a` y 1 `padre_sugerido`
(`salidas/diff_a9631a64_vs_head_diez.json`). Mido cada grupo contra HEAD y doy la cifra sobre `a9631a64` donde difiere.

Detalle de cada cambio y de su selftest: `diseno_O1.md`. Límites, caso por caso: `limites_O1.md`.

## Cifras de la v7

| Ítem | v7 | O1 | |
|---|---|---|---|
| A, a | 390 de las 1.137 `meta_normativo` | 390 de las 1.882 omisiones (317 `meta_normativo`, 50 `relacion_sin_predicado`, 23 `fuera_de_tipos`) | **base distinta**: el contador del validador cuenta todas las categorías. 8 más en orden de lectura, sin marca. T4: 22/22 heredadas marcadas y 38/38 propias sin marca (una, `ric::6.1.2`, sin pareja automática por una diferencia de la ficha; controlada a mano) |
| A, b | 404 + recomendación (NO MEDIDA) | 404; 40 de recomendación, todas con marca del contador → 404 | T4: 6/6 recomendaciones detectadas |
| A, c | ≥ 2; total NO MEDIDO | 179 (100 `meta_normativo`, 50, 28, 1); los dos de la v7, detectados | una sola marca: los dos ejemplos son ítems con extracción |
| A, d | NO MEDIDO | 1.567 entidades en 877 unidades | T4: cobertura 52/62 (Wilson 0,728–0,910); precisión aproximada 52/109 |
| A, e | — | 57 detecciones: 41 dentro y 16 fuera de las 64 de T4 (15 unidades) | lista sellada, abajo |
| B, f | hasta 51 pasan | 47 pasan (257 → 210 sin verificar); cambian 5 decisiones, 1 de destino | el conjunto de 51, reconstruido, da 64; quedan 17 (`limites_O1.md`) |
| B, f′ | 19; 435/401; 15 marcas; 17+2; 98 → 95; 294 → 275 (164 → 145) | iguales; con HEAD, atribuido por fila: 99 → 96; 298 → 279 (168 → 149); docvig 0 | — |
| B, desacuerdos | 150 → 165 | 430 → 445 (f′) → 447 (con f) | el +15 se reproduce; **150 no**: el reporte y LN-4 dan 430 |
| C | 11/96/157 → 11/177/76; cambian 160 (76, 78+3, 1, 2) | iguales; sin cola: 10/94/150 → 10/173/71, cambian 153 | las 7 correctas, iguales; `cap::2.3.1` marcada |
| L | 761; 759 + 2; 45; mediana +20, máx. 249, 22.119; tramo 34/252 | 759 del ensamblado + 2 del validador; 753 toman el tramo (622 cambian el campo, 131 ya eran iguales), 6 conservan la cuantía; 45 (22 tramos); +19, 249, 21.915; 34/252; «no» = 1 | los 2 de `cap::1.2` y los 6, abajo |
| h | 13.301 / 13.380 / 746 | iguales en `a9631a64`; con el código nuevo 13.296 / 13.388 / 746 | — |
| i | 43 y 22 | 43 y 22 (grado entrante + saliente, solo `remite_a` / sin `remite_a`); con la ventana del agente, 49 y 20; código nuevo 44/22 y 49/20 | definición, abajo |
| G-r | 22 (9/8/4/1); 173 de rol; 0 fusiones | iguales (173 por la procedencia principal; 182 por alguna; 194 entidades) | además, `remite_a` +145/−137 |
| H | 34 → 8 / 26 / 0; desarrollo 24 | iguales; desarrollo 24 → 6 / 18 / 0 | — |
| I | 331 de 1.952, 18 (8 + 10) | iguales; r2a diez 232/1.409; r1 diez 884/1.383 | va junto a M9, abajo |
| J | 13.380; cuántas cambian NO MEDIDO | 13.388 (con G-r): 9.824 por el tramo del propio origen, 97 con la marca sin tramo, 1 en otros campos; 9.966 con `provenances` distinto | origen, destino y evidencia iguales en las 13.388 |
| K | 0; 43 de 255 → 212; 41 de 215 | iguales (desarrollo sin cola, 174) | — |

- **Los 2 de `cap::1.2`** («5.000» y «2.500»): no son elementos del ensamblado. Son límites relativos del validador cuyo tramo ya es
  el de E1 (la celda); el paso del rótulo de T3-bis les dio valor y unidad (`originales.regla_comparacion` relativa). L no tiene
  nada que cambiarles.
- **Los 6 que conservan la cuantía**: el tramo de E1 con cuantía no lo verifica el validador, y 5 de estos tramos no son literales.
  Con la regla literal de la v7, los «no» pasaban de 1 a 5, contra la aceptación. Por eso agregué al diseño el paso «si no
  verifica, conserva la cuantía», contado en el reporte.
- **G-r cambia `remite_a`**: la cita a un punto apunta a los nodos de ese punto, y 22 nodos cambian de punto.

## (e): la lista sellada

Archivo `salidas/e_lista_sellada/detecciones_e_copia_nota_diez.json`, sha256
`4c3855292349a75d675216fd7ae772a948777dd76e226eaa1f32bcf67cda3efd`, sellado a las 16:59:27 (−0300) del 09/10/2026. Tiene 57
detecciones, 41 dentro y 16 fuera de las 64 unidades de T4. No la abrí, y una segunda corrida da el mismo sha.

- **Hallazgo.** La marca del ratchet existe en diez solo en las 64 unidades que leyó T4. El clasificador mira las 216 unidades
  aceptadas tras reintento, con ventanas de 3 tokens compartidas con la nota y la tolerancia de flexión de T4.
- **Sobre los 86 de diseño de T4**: 26/30, contra el 29/37 del cotejo, que reproduzco.
- **Para la lectura.** Con 16 fuera de las 64 se leen todas, y solo 16/16 pasa el piso (Wilson 0,806; con 15/16 da 0,717).

## Ítem (i)

43 y 22 en `a9631a64`, con la definición que las reproduce: más de 40 aristas entre entrantes y salientes, contando solo
`remite_a` / todas menos `remite_a`. La ventana real del agente corta por dirección (`ver_vecinos(limite=40)`): 49 con `remite_a` y
20 sin ella. Con el código nuevo: 44/22 y 49/20. Listas en `salidas/h_i.json`.

## Prueba en seco de lo que O2 va a correr (`copia_o2`)

- **Las seis cadenas.**
  - r2a de diez y de desarrollo: byte a byte (`70d51e42`, `fa4c1043`). No hace falta acotar f y f′ a r2b.
  - r2b: diez `6be0a6b2`, sin cola `6f3d5c7e`, desarrollo `d41275a6`, desarrollo sin cola `a6570b1a`.
  - Con HEAD, la copia reproduce los seis grafos de referencia.
  - La doble corrida interna da byte a byte en todas, y las dos de diez, corridas otra vez en otro proceso, salen iguales.
  - Diferencias por etapa y por campo: `salidas/diff_*.json`.
- **Ningún campo ajeno.** C y L no cambian ningún otro campo de los elementos (0). J no cambia aristas ni nodos. A, h y K no tocan
  `kg.json`.
- **Shapes**: PASA en los cuatro r2b, sin bloqueantes en FAIL, y ninguna cambia de resultado.
- **Suite**: 0 ítems empeoran; LN-6 pasa de «persiste» a «resuelto» en los cuatro.
- **Casos de la v7**: 58/58 (`salidas/casos_v7.json`).
- **Selftests, HEAD → nuevo.**
  - `selftest_pyd_r2`: 398 → 396 (los dos de P3b, l, por H).
  - Sin cambios: `selftest_r3` 140/140, `selftest_e2` 41/41, `selftest_regression_kg` 184/184, `selftest_reresolver_catalogo`
    66/66, `selftest_prompt_r2b` 55/55, `pruebas_t3bis` 17/17 (JSON igual), `selftest_catalogo_unico` 60/60 (con el `.git` del
    repo solo para lectura), `selftest_comparador_P` 23/23 y `gate6` (ii) 15/15.
- **Claves de caché**: VEREDICTO OK, y el JSON es igual al del repo con los dos códigos.
- **Fichas del lote 1**: byte a byte sobre `e22fae1a` y sobre el grafo con L.
- **Métricas**: `--gen3` da la medida de I en r2b, r2a y r1.

## Contradicciones y decisiones para la autora (§4.d)

1. **H contra P3b, l.** `selftest_pyd_r2.py:1180` y `:1341` afirman que en r2 el tipo no se deriva del código. H lo reemplaza: el tramo
   va primero y el código, después. Los dos casos se reescriben en O2.
2. **I contra la spec sellada.** «En lugar del grado 0» cambiaría M9 y rompería `selftest_gate6`. Por eso la puse junto a M9, en
   `adaptador_gen3`.
3. **El §5 no autoriza** que `ensamblar_tanda0.py` reciba (h), K y la línea que activa J, ni dice dónde van los selftests nuevos
   (propongo `omisiones_cod/`). Hace falta autorizarlo en el despacho de O2.
4. **L**: el paso «conserva la cuantía» (6 elementos) no está en la v7.
5. **(i)**: cuál de las dos definiciones rige.
6. **(e)**: la lectura de 16 solo pasa con 16/16. La población y la regla son mías.
7. **G-r**: el efecto sobre `remite_a` no está en la v7.
8. **Errores de cifra de la v7 o de la mesa**: «150 → 165» (es 430 → 445), la base de las 390 y el «51» de f, que no reconstruyo
   igual.

## Límites medidos (`limites_O1.md`, caso por caso, con unidad, páginas y mecanismo)

- L: 6 conservan la cuantía.
- f: 17 menciones siguen sin verificar: 8 «las entidades» y 9 con «la», «los» o «el Directorio».
- a: 8 omisiones en orden de lectura, sin marca.
- d: 10 positivas de T4 sin detectar.
- e: 3 copias reales de T4 sin detectar y 4 detecciones que T4 no leyó como copia.
- H: 26 con `tipo_no_derivable`.
- C: 177 marcadas y 76 sin base (`ext::13.4.6` → `ext::4.4` resuelta, sin leer).

Ninguno sale de los grupos de la v7, y no propongo excepciones al §29.

## Cierre

- **Foto sha256 del repo, sin `.git`** (`scripts/foto_repo.py`).
  - Antes: 48.977 archivos, a las 16:38:10. Después: 49.097, a las 18:15:31.
  - Míos: 115 archivos nuevos en `data/experiment/omisiones_cod/o1/`. Fuera de esa carpeta no cambio ni quito nada.
  - De otras sesiones, por ruta (no los toqué):
    - nuevos, 5 en `segmentacion_oficial_e0r2/s0_5/bis/` (`parche/` 3, `scripts/` 2);
    - cambian 3 en esa misma carpeta (`DISENO_S0-5a-bis.md`, `aceptacion_S0-5a-bis.py`, `limites_S0-5a-bis.py`) y 3 en `docs/`
      (`checklist_pre_escalado.md` y los mandatos de U-CONF-MATRIZ y de S0-5a).
  - Tomé la foto antes de escribir esta sección: después cambian solo este archivo y `diseno_O1.md` (la ruta de la lista
    sellada), dentro de `o1/`.
- **`.pyc`**: 2.213 antes y después, con la misma lista.
- **Grep de convenciones**: vacío en las tres búsquedas (nombres de personas, con los tokens de `user.name` y una lista de nombres
  de pila; fuentes conversacionales; rutas con el nombre de usuario). Control positivo: coincide la línea 2 del archivo de control.
- **Paquete** `revision_UOMISIONES_COD_O1/` en el scratchpad, con `manifest.txt`. La ruta de la copia permanente y la verificación de
  su manifiesto van en el reporte de cierre: no caben en este archivo, que entra al manifiesto.
- **El mensaje de commit**, probado en un clon descartable: el título sale solo en `git log --oneline`.

**Mensaje de commit preparado** (PENDIENTE de la autora, sin la línea de coautoría):
`git add data/experiment/omisiones_cod/o1 && git commit -m "Etapa de diseno con medicion previa" -m "Diseno de los cambios de codigo con su medicion sobre copias, la prueba en seco y una lista sellada para una lectura aparte. USD 0, sin API; solo se agrega la carpeta de la etapa."`

**FRENO O1.**
