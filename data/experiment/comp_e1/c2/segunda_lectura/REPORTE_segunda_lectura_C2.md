# U-COMP-E1, C2 — segunda lectura a ciegas de la mesa: FRENO

07/10/2026. USD 0, sin API, solo lectura del repo; todo lo escrito está en este paquete. La adjudicación de las
divergencias es de la autora y queda PENDIENTE; C3 sigue después.

## Ceguera

- El archivo cerrado de códigos no se abrió: sha256 `065a272c…` al inicio (17:51), en la pausa, al sellar y al final.
- La lectura propia se selló a las 20:19:30 (-03), con `segunda_lectura_c2.jsonl` sha256 `04406c97…`
  (`sello_segunda_lectura_c2.txt`). Recién después abrí `lectura_c2.jsonl` (sha256 `f00a8b15…`, igual al inicio y al final).
- Leí solo `comp_e1/c2/material/`, `reext_t0/t4/salida/{fichas_punto7_grupo_c,fichas_punto8_omisiones,tasas_t4}.json`
  (las clases de T4 de los 137 supuestos sobre la extracción final de Haiku, como calibración), `c0/reglas_lectura_c0.md`
  y el mandato (texto firmado `cbcb823`, sha `89ce5508…`, y sus notas). No usé los PDF: el texto del material bastó.
- Contaminación, a declarar: antes de leer vi cifras agregadas de la primera lectura en el mensaje del commit `4e9a1fc` y en
  la nota del mandato posterior al FRENO C2. Eran los máximos de 96 de 137 en M1 y 22 de 46 en M2, las extraídas por código
  en el texto propio y el heredado, los «12 casos» solo en la descripción y las «5 anclas» de N. También vi un ítem: que
  `ext::14.5.7`, código K, traía una Excepcion anotada «a adjudicar». Ese ítem quedó en divergencia (n.º 12 de la hoja).
- Ayuda compartida con la primera lectura: el material trae, por código, una lista de candidatos por supuesto y un
  solapamiento entre tramos por omisión. Para M2 recalculé el solapamiento por mi cuenta (`segunda_lectura_c2_ver_m2.py`).
  En 29 líneas el material corta el tramo en «…», y ahí uso su solapamiento por código. Están marcadas en
  `cobertura_segun_solapamiento_del_material`.

## Reglas

Usé las selladas en `c0/reglas_lectura_c0.md`, las cinco clases de T4 y los tres subtipos de `tasas_t4.json` (punto 7), y
las cuatro reglas que la autora adjudicó el 07/10/2026 (nota `c957089`).

- **Desde cuándo apliqué las reglas:** las recibí por mensaje después de registrar `cap::3.1.11.3` y antes de leer
  `cap::3.1.14.1`. Eso ocurrió entre las 17:55:29 (creación del visor, antes de la primera unidad) y las 17:59 (última
  escritura antes de la pausa). La hora exacta NO VERIFICADA: la sesión no registra la llegada de los mensajes.
- **Líneas previas a las reglas:** 56 (`cap::2.1`, `cap::3.1.11.2` y `cap::3.1.11.3`). Las reclasifiqué con las reglas y las
  cuento aparte en `reclasificacion_lineas_previas_a_las_reglas.tsv`: 0 cambios y 0 divergencias con la primera lectura.
- **Regla (4) en otros códigos:** la regla nombra solo a N. En A, H, K y W apliqué la misma precedencia de la entidad sobre
  la omisión en 2 líneas (`ext::10.5::intro` K y W), marcadas en la hoja; coinciden con la primera lectura.
- **Pausa:** la autora pausó la lectura de 18:00 a 20:00. El estado quedó en `ESTADO_segunda_lectura_C2_pausa_0710.md`
  (raíz del scratchpad).
- **Cambios propios antes del sello:** 5 líneas, al precisar dos criterios (`cambios_propios_antes_del_sello.txt`):
  - `cla::6.5.3.10` H 1: FU → SR:nh;
  - `cla::6.5.4.5` K 1 y W 1: FU → DN;
  - `cla::6.5.5.9` W 4 y W 5: FU → DN.

  Contra la primera lectura, tres de las cinco quedaron en divergencia (`cla::6.5.3.10` H 1, `cla::6.5.4.5` K 1 y W 1) y dos
  coinciden (`cla::6.5.5.9` W 4 y W 5). Con las clases originales habría sido al revés.

## Cobertura

804 líneas = M1 559 (137 × 4 + 11 de N) + M2 245 (60 × 4 + 5 de N). Las tengo verificadas contra el material: 30 unidades del
grupo c y 59 de omisiones, sin faltantes ni duplicados. El cruce por (unidad, ítem, código) con la primera lectura da 804
pares, con las mismas claves de ambos lados.

## Acuerdo por código

Lectura del cuadro: «clase» es acuerdo en la clase; «fino» además pide el mismo subtipo de `sin_relacion` o la misma
categoría de `omision_otra_vez`. Las cifras salen de `acuerdo_c2.json`.

| medición | A | H | K | N | W | total |
|---|---|---|---|---|---|---|
| M1 clase | 134/137 | 134/137 | 134/137 | 11/11 | 136/137 | 549/559 |
| M1 fino | 132/137 | 133/137 | 132/137 | 11/11 | 134/137 | 542/559 |
| M2 clase = fino | 60/60 | 60/60 | 59/60 | 5/5 | 59/60 | 243/245 |

Kappa de Cohen (todos los códigos juntos):

- M1: 0,967 en la clase (po 0,9821; pe 0,4585) y 0,944 en fino.
- M2: 0,986 en la clase y en fino.

## Divergencias

Hay 19 (M1 17, M2 2): 12 de clase y 7 solo de subtipo. Por código: A 5, H 4, K 6, W 4, N 0. La nota del mandato estimaba
entre 40 y 80. Son cinco tipos de caso:

1. **`cla::6.5.3.10`, ítems 1 y 2 (8 líneas).** Siete son solo de subtipo de `sin_relacion`: la primera lectura dice
   `norma_presente` (el indicador está en la unidad) y la segunda `norma_en_heredado` (la clasificación «Con problemas», como
   la clasificó T4 para Haiku). La octava es H 1, donde la primera lectura dice FU y la segunda SR:nh.
2. **`polcre::7.1.2`, ítems 1 y 2, en A y H (4 líneas).** Primera lectura SR:nh, segunda FU: una sola Condicion junta los dos
   supuestos alternativos «y/o».
3. **`cla::6.5.4.5`, ítem 1, en K y W (2 líneas).** Primera lectura FU, segunda DN: «bienes en pago» aparece solo en la
   descripción de la Condicion del indicador.
4. **Condicion o Excepcion con relación (3 líneas).** La primera lectura dice CR en las tres:
   - `ext::14.5.7` A 4: segunda FU (la Condicion lleva su norma).
   - `ext::4.1.3.1` K 2: segunda FU (la Condicion lleva su consecuencia).
   - `ext::14.5.7` K 5: segunda DN (para la regla 2, «En caso de no disponerla» no es cláusula de excepción).
5. **`lingob::7.1.7`, M2, en K y W (2 líneas).** Primera lectura «extraída con tramo verificado», segunda «ausente»: el
   tramo cubre 0,58 y le falta el calificativo de proporcionalidad.

## Hoja de adjudicación

- `adjudicacion_c2_worksheet.json`: 19 entradas en orden de unidad, cada una con las dos lecturas, las dos anclas, el texto
  y `veredicto_autora` vacío.
- `adjudicacion_c2_worksheet.md`: la misma hoja en versión legible.
- El detalle de cada divergencia está en `divergencias_c2.jsonl`.

## Controles

- **Archivos leídos o vigilados (103):** sha256 iguales al inicio y al final, salvo el mandato, que cambió por la nota
  `c957089` (commit de la autora, 18:31; `controles/sha256_leidos_{inicio,pausa,reanudacion,final}.txt`).
  `git diff d007be8 HEAD` sobre `comp_e1/` y `reext_t0/t4/` está vacío.
- **HEAD:** pasó de `d007be8` a `1190a8a` por 9 commits de la autora (18:31 a 19:56). Las diferencias de `git status` son de
  esos commits y de otras sesiones, todas en rutas que no escribí.
- **`.pyc`:** 2.213 sin contar `.venv` al inicio, en la pausa y al final. La lista completa de `.pyc` y `__pycache__`, con
  `.venv`, es idéntica.
- **Doble corrida byte a byte** de `segunda_lectura_c2_armar_jsonl.py` (el jsonl) y de `segunda_lectura_c2_cruzar.py`
  (los cuatro archivos de salida).
- **Grep de convenciones** sobre el paquete (39 archivos con `manifest.txt`): 0 coincidencias de los tokens del
  `git user.name`. Las únicas otras coincidencias son las dos líneas de esta viñeta que enumeran los patrones buscados: «Users/», slack,
  mail, whatsapp, «como dijo», «según el mail» y «pedido por». El control positivo, sobre la ruta del scratchpad, encontró
  una coincidencia en la línea 1.
