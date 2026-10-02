FIRMADA por la autora — 2026-10-02

ENMIENDA 1 AL MANDATO U-R2-CODIGO: LA REMISIÓN ENTRE PUNTOS COMO `remite_a`.
Repo bcra-regulatory-kg. Se lee junto con el mandato firmado
(`git show c60e89c:docs/mandatos/UR2CODIGO_correcciones_en_codigo.md`), que no se edita.
- Extiende R3.d y R5, y suma escrituras. No cambia R1, R2 ni R4. Costo de API: USD 0.
- Rige junto con la enmienda 2 de L-ESQ-R2
  (data/experiment/esq/enmienda2_L-ESQ-R2_remite_a_2026-10-02.md, FIRMADA el 02/10/2026): esa es la
  fuente de esquema de todo lo que sigue, y se lee en su commit de firma (regla k).
- **Si la unidad llega a R3 y las dos enmiendas no están commiteadas, FRENO.** El complemento de R1
  y R2 no dependen de esta enmienda y siguen.

CONTEXTO.
- La remisión entre puntos no está declarada en ningún esquema: el ensamblado la escribe como
  `referencia` con `rol_fuente = referencia_cruzada` (`corpus_v2/r1_referencias.py:227-237`) y el
  validador la admite por `rol_fuente` (`scripts/shapes_validator.py:624-626`).
- La autora decidió que es una relación propia, `remite_a`, para todos los tipos de contenido como
  origen y como destino, declarada por enmienda y controlada por firma.
- El mandato ya tiene, en R3.d y en la decisión 11: los tipos de origen nuevos y `termino`, la
  detección sobre el texto de E0, la resolución desde cada procedencia y los casos de control. Esta
  enmienda no los repite: agrega el nombre, la firma, el alcance y los lectores.

Leé completos, además de lo que pide el mandato:
- la enmienda 2 de L-ESQ-R2, en su commit de firma;
- docs/plan_remite_a.md;
- data/experiment/pyd_r2/code/modelos_r2.py (`PREDICADOS` :92, `FIRMAS_CONGELADAS` :99-102,
  `_matriz_r2` :122-130, `RelacionR2.predicate` :384, `AristaR2` :490-515) y selftest_pyd_r2.py
  (:112-130);
- scripts/muestra_aristas_obs12.py (:22-25, :111-112) y su selftest;
- scripts/shapes_validator.py (:95-116, :150, :612-660, :836-862).

DECISIÓN 12 (nueva; no se re-decide).
- Con el perfil r2, la remisión se emite como `remite_a`, con la firma, las propiedades y la
  procedencia de la enmienda 2 de L-ESQ-R2 (§2 a §4).
- Con los perfiles existentes (`produccion_dev` y `v3_b54`), el ensamblado sigue emitiendo
  `referencia` con `rol_fuente = referencia_cruzada`, byte a byte como hoy. El control global del
  mandato no cambia: los tres ensamblados sellados se reproducen.
- La cita de un nodo de contenido a una Comunicación no genera arista: va a un registro contado.
- El agente leerá `remite_a` donde leía `referencia`; no hay alias en la carga a Neo4j. La
  exportación de `alcance` a Neo4j es de A1.8, no de esta unidad.

R3.d — SE AGREGA (el texto firmado de R3.d sigue rigiendo).
1. **Nombre del predicado.** En `r1_referencias.py`, la clave de la tripla (:228) y la arista
   (:231-236) dependen del perfil: `remite_a` con el perfil r2, `referencia` con los demás. El perfil
   llega por un parámetro de `detectar_y_resolver` (:200) con el valor de hoy por defecto, que pasan
   `ensamblar_r1.py:164-165` y `data/experiment/tanda0/code/ensamblar_tanda0.py:408`.
2. **Forma de la arista `remite_a`** (enmienda 2, §3): `alcance`, `destino`, `evidencia` y la
   procedencia desde la que se resolvió la cita. No lleva `rol_fuente`, `clase` ni `via`: la forma de
   la cita queda en el registro de remisiones del ensamblado.
3. **`alcance`:** `to_entero` si el destino es un TextoOrdenado; si no, `interna` cuando la unidad
   citada es del mismo texto ordenado que la procedencia de resolución, y `externa` cuando es de
   otro. No se copia la clase de la mención (`r1_referencias.py:159`, `:171`, `:185`, `:194`).
   - **Caso de control:** sobre KG-Reextraído-r1, la regla aplicada a las 5.645 remisiones de hoy da
     5.456 `interna`, 183 `externa` y 6 `to_entero`; las 5 de clase externa dentro de `cap`
     (`cap::1.4` y `cap::S2`) quedan `interna`.
4. **Destinos.** Todo nodo de contenido anclado en la unidad citada, de cualquiera de los siete
   tipos, y el TextoOrdenado cuando la cita nombra solo la norma. Reportá las aristas por firma.
5. **Atribución de la cita a los nodos del punto de origen** (enmienda 2, §4): a los nodos del
   punto cuyo texto guardado contiene la unidad citada; si ninguno la contiene, a todos los nodos de
   contenido del punto. Reportá cuántas citas caen en cada rama.
6. **Registro de citas a Comunicaciones,** por TO y por ensamblado: citas, chunks y Comunicaciones
   distintas, sin arista. Declarás los pies de página que E0 no recortó y que el patrón toma por
   cita (caso conocido: `ctacte::6.1.2.3`).
7. **Conteos de salida,** en citas resueltas y en aristas: por alcance y por firma; irresolubles
   por causa.
8. **Casos de control** que se suman a los de R3.d:
   - `cla::5.1.1.1` → `cla::3.7` existe como `remite_a`, con `alcance = interna`, `destino =
     cla::3.7` y una `evidencia` que contiene «punto 3.7»;
   - con el perfil r2 no queda ninguna `referencia` con origen distinto de TextoOrdenado;
   - los casos de R3.d (`cap::8.2.3.3`, la simulación de U-AUDIT-TIPOS-V3) se leen sobre `remite_a`.

R3 — MODELO DEL PERFIL r2 (escritura nueva, sobre una unidad cerrada).
U-PYD está cerrada (`57a8dd2`). Esta enmienda autoriza un cambio acotado en
data/experiment/pyd_r2/code/modelos_r2.py y en selftest_pyd_r2.py, y nada más de pyd_r2/:
- `PREDICADOS` (:92) y `FIRMAS_CONGELADAS` (:99-102) no cambian: el selftest los compara contra el
  prompt sellado (selftest_pyd_r2.py:114 y :119);
- `RelacionR2.predicate` (:384) no cambia: E1 no puede emitir `remite_a`;
- se agregan `PREDICADOS_DERIVADOS = ("remite_a",)`, su firma y la lista cerrada de `alcance`;
- `AristaR2.relation` (:496) admite además los predicados derivados, y sus invariantes (:509-515)
  controlan en `remite_a`: `alcance` en la lista, `evidencia` y `destino` presentes, y ninguna
  marca de relación emitida por E1 (`no_verificada_e3`, campos de sujeto, coherencia).
- **Controles:**
  - los 249 casos del selftest (249/249 en `57a8dd2`) siguen en verde y se suman los de `remite_a`;
  - el tool schema de E1 que sale del modelo es byte a byte el de `57a8dd2`;
  - `politica_campos_r2.json` no cambia y su sha sigue siendo el de la decisión 10.

R5 — SE AGREGA.
a. **Función de reconocimiento.** Un módulo nuevo, solo con stdlib, `scripts/remisiones.py`, con una
   función que reconoce la remisión en las dos formas: `remite_a`, o `referencia` con `rol_fuente =
   referencia_cruzada`. La usan regression_kg.py, el perfil r2 de shapes_validator.py y
   muestra_aristas_obs12.py. Si importarla rompe una garantía de alguno de los tres, FRENO con la
   alternativa.
b. **Suite** (scripts/regression_kg.py):
   - T5 (:1028) lee las remisiones con la función;
   - el test del ejemplo `cla::5.1.1.1`, parte (ii): sobre un grafo del perfil r2 exige `remite_a`;
     sobre los sellados, la remisión en su forma de origen. Los estados esperados del mandato no
     cambian;
   - censo informativo de remisiones por firma y por alcance.
c. **Shapes del perfil r2** (scripts/shapes_validator.py):
   - S3 del perfil r2: `remite_a` por su firma; una `referencia` con origen distinto de
     TextoOrdenado es violación, con o sin `rol_fuente`. La tolerancia de :624-626 queda solo en el
     perfil congelado;
   - una shape nueva: `alcance` en la lista cerrada y coherente con los extremos;
   - una shape nueva: `evidencia` es un tramo literal del texto de E0 del `chunk_id` de la arista;
     sin el directorio de E0, da «no computable»;
   - S21 (:836-862) lee las remisiones con la función.
   Los números de las shapes nuevas siguen a S29.
d. **scripts/muestra_aristas_obs12.py** (:111): el universo excluye toda remisión, en cualquiera de
   las dos formas, además de `referencia`. Así su composición no cambia con el nombre nuevo.
   - **Control:** sobre KG-Reextraído-r1, la muestra es byte a byte la de hoy.
   - La nota fechada de equivalencia en el pre-registro de la tanda que use la observación 12 la
     asienta la autora (enmienda 2, §7). No es de esta unidad.
e. **No se tocan** los scripts de la tanda 0 y de r1 que leen `referencia` sobre grafos sellados:
   data/experiment/tanda0/code/lectura_e6_tanda0.py (:144, :363),
   data/experiment/ev2_tanda0/code/atribucion_tanda0.py (:188) y
   data/experiment/ev2_r1/code/selftest_r1.py (:129). Listás en el FRENO R5 qué mediciones de la
   tanda 1 van a necesitar la función.
f. **Neo4j:** sin cambio de código en esta unidad.

FRENO R3, se agrega:
- las remisiones por firma y por alcance, en citas y en aristas, sobre la prueba de r2;
- el registro de citas a Comunicaciones;
- el control del tool schema de E1 y el selftest de pyd_r2;
- el caso `cla::5.1.1.1` → `cla::3.7` como `remite_a`.

FRENO R5, se agrega:
- las shapes y el test sobre la prueba de r2 y sobre los grafos sellados;
- la muestra de la observación 12 reproducida sobre KG-Reextraído-r1.

ESCRITURAS. A las del mandato se suman, y solo estas:
- data/experiment/pyd_r2/code/modelos_r2.py y selftest_pyd_r2.py;
- scripts/remisiones.py (nuevo), scripts/muestra_aristas_obs12.py y
  scripts/selftest_muestra_aristas_obs12.py.
Lo demás de «No se editan» sigue igual.

Los requisitos transversales y el criterio de aceptación son los del mandato.

FIRMADA por la autora el 02/10/2026.
