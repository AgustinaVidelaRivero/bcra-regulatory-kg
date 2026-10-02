# Plan — la remisión entre puntos como relación propia (`remite_a`)

Redactado el 02/10/2026 sobre HEAD `7741e88`. Unidad de planificación: no cambia código ni esquema. Ítem
nuevo de la cola de mejoras previas al escalado (checklist, X17 y W15).

**Estado al 02/10/2026.** La autora tomó las decisiones D1 a D5 y firmó las dos enmiendas; sus commits
están PENDIENTES. Los asientos de la última sección están aplicados, sin commit.

Enmiendas que acompañan este plan, las dos FIRMADAS por la autora el 02/10/2026:
- `data/experiment/esq/enmienda2_L-ESQ-R2_remite_a_2026-10-02.md` (punto a y agregados 5 a 7);
- `docs/mandatos/UR2CODIGO_enmienda1_remite_a.md` (punto b y agregados 9 y 10).

## Decisiones ya tomadas por la autora

1. La remisión entre puntos es parte del grafo y existe en el grafo escalado para todos los tipos de
   contenido, como origen y como destino.
2. Se declara en el esquema como relación propia, con firma; el validador deja de admitirla por `rol_fuente`.
3. Se llama `remite_a`. `referencia` queda solo para TextoOrdenado → Comunicacion.
4. Criterio obligatorio: en el grafo del perfil final existe `remite_a` del 5.1.1.1 al 3.7 de Clasificación
   de deudores.
5. La deriva el código desde el texto de E0; E1 no la emite y E3 no la verifica; su ancla es el tramo de la
   cita.
6. El alcance es una propiedad de la arista: interna, externa o a un texto ordenado entero.
7. La cita a una Comunicación queda fuera de alcance en r2, con registro contado y sin arista.
8. El agente lee `remite_a` en lugar de `referencia`; se acepta y se declara, sin alias en la carga. La
   exportación de `alcance` a Neo4j queda para A1.8.
9. U-R2-CODIGO se extiende por enmienda a su mandato (R3.d y R5, más `modelos_r2.py` y su selftest), con
   una función de reconocimiento para los lectores de grafos sellados, incluido `muestra_aristas_obs12.py`.

## Hechos verificados

- **Remisiones de hoy** [m1]:

  | Grafo | Remisiones | `interna` | `externa` | `to_entero` | TextoOrdenado → Comunicacion |
  |---|--:|--:|--:|--:|--:|
  | KG-Reextraído-r1 | 5.645 | 5.456 | 183 | 6 | 35 |
  | KG-Tanda0-Desarrollo-r1 | 4.242 | 4.118 | 120 | 4 | 14 |
  | KG-Tanda0-Diez-r1 | 4.819 | 4.631 | 174 | 14 | 17 |

  El alcance es el de la regla de la enmienda 2 (texto ordenado de la procedencia de la arista
  contra el de `properties.destino`). Por la clase que guarda hoy la arista, r1 da 5.451 internas, 188
  externas a nodos y 6 a un texto ordenado.
- **Origen.** En los tres grafos solo hay cuatro tipos de origen: `TIPOS_ORIGEN`
  (`data/experiment/reextraccion_v2/corpus_v2/r1_referencias.py:51`, aplicada en `:243`).
- **Destino.** No se filtra por tipo: en la tanda 0 ya hay 1.349 (desarrollo) y 1.488 (diez) remisiones
  hacia Condicion, Definicion o Potestad [m1].
- **El ejemplo.** En KG-Reextraído-r1 la remisión es `edges[15773]`, Restriccion → Obligacion, con
  `destino = cla::3.7` (`docs/tesis/figuras/ejemplo_prestamo_datos.json:135-138`). En los dos ensamblados de
  la tanda 0 no existe: el 5.1.1.1 se extrae como Condicion (`docs/laudo_release_r2_pipeline.md:329`, `:334`).
- **Agente.** El prompt de `data/experiment/evaluacion/harness.py` no nombra ninguna relación;
  `data/experiment/neo4j/neo4j_index.py:240-253` y `data/experiment/agente_v2/tools_v2.py:206` devuelven el
  tipo de la arista sin filtrar. Nada del agente depende del nombre `referencia` ni de `rol_fuente`.
- **Exportación.** `data/experiment/neo4j/cargar_kg.py:153-171` crea el tipo de relación desde `relation` y
  exporta solo `orden` y `provenances_json`.

## a. Texto de la enmienda

En `data/experiment/esq/enmienda2_L-ESQ-R2_remite_a_2026-10-02.md`. En resumen:
- **Nombre:** `remite_a`.
- **Firma:** origen, los siete tipos de contenido; destino, los mismos siete o TextoOrdenado. Son 56 firmas.
  Comunicacion y Sujeto quedan fuera.
- **Remisión a un texto ordenado entero:** destino TextoOrdenado, `alcance = to_entero`.
- **Remisión a otro texto ordenado:** destino nodos de contenido, `alcance = externa`.
- **Interna o externa:** por comparación de textos ordenados, no por la forma de la cita.

## b. Cambios de código, con archivo y línea

Los aplica U-R2-CODIGO por la enmienda 1 a su mandato. Todo dentro de `data/experiment/` salvo `scripts/`.

| Qué | Dónde | Cambio |
|---|---|---|
| Tipos de origen | `reextraccion_v2/corpus_v2/r1_referencias.py:51`, `:243` | suma Condicion, Potestad y Definicion (ya está en R3.d del mandato) |
| Nombre del predicado | `r1_referencias.py:228`, `:231` | `remite_a` con el perfil r2; `referencia` con los perfiles existentes |
| Forma de la arista | `r1_referencias.py:231-236` | `alcance`, `destino`, `evidencia` literal y procedencia de resolución |
| Paso del perfil | `r1_referencias.py:200`; `ensamblar_r1.py:164-165`; `tanda0/code/ensamblar_tanda0.py:408` | parámetro con el valor de hoy por defecto |
| Modelo del perfil r2 | `pyd_r2/code/modelos_r2.py:92`, `:99-102`, `:384`, `:496`, `:509-515` | `PREDICADOS` y `RelacionR2` sin cambio; `PREDICADOS_DERIVADOS`, su firma y `AristaR2` |
| Selftest del modelo | `pyd_r2/code/selftest_pyd_r2.py:114`, `:119` | las comparaciones con el prompt sellado siguen; casos nuevos |
| Validador, firma | `scripts/shapes_validator.py:99`, `:114` | perfil r2: firma de `remite_a`; `referencia` solo TextoOrdenado → Comunicacion |
| Validador, tolerancia | `scripts/shapes_validator.py:150`, `:624-626` | la tolerancia por `rol_fuente` queda solo en el perfil congelado |
| Validador, coherencia | `scripts/shapes_validator.py:836-862` (S21) | lee la remisión en las dos formas |
| Suite | `scripts/regression_kg.py:1028` (T5) y el test del ejemplo de R5.a | leen la remisión en las dos formas; sobre r2 exigen `remite_a` |
| Universo de la observación 12 | `scripts/muestra_aristas_obs12.py:111` | excluye toda remisión, en cualquiera de las dos formas |
| Función común | `scripts/remisiones.py` (nuevo) | reconoce `remite_a` o `referencia` con `rol_fuente = referencia_cruzada` |

**Lo que se deja de tolerar por `rol_fuente`:** en el perfil r2, una `referencia` entre nodos de contenido es
una violación de firma, tenga o no `rol_fuente = referencia_cruzada`.

**Sin cambio de código:** la carga a Neo4j y las herramientas del agente.

**No se tocan,** porque leen grafos sellados: `tanda0/code/lectura_e6_tanda0.py:144` y `:363`,
`ev2_tanda0/code/atribucion_tanda0.py:188` y `ev2_r1/code/selftest_r1.py:129`. Las mediciones equivalentes de
la tanda 1 tienen que usar la función común.

## c. Unidades, en orden

1. **Firma de la enmienda 2 de L-ESQ-R2:** hecha por la autora el 02/10/2026; commit PENDIENTE.
2. **Firma de la enmienda 1 al mandato de U-R2-CODIGO:** hecha por la autora el 02/10/2026; commit
   PENDIENTE. Las dos enmiendas tienen que estar commiteadas antes de que la unidad llegue a R3. El
   complemento de R1 y R2 no dependen de ellas.
3. **U-R2-CODIGO, R3 y R5** (plan, B2.11, unidad 8, `docs/plan_tesis.md:397`): el cambio de b.
4. **Medición r2a** (unidad 9, `:398`): primera medición de d, sobre la salida guardada de la tanda 0.
5. **U-PROMPT-R2** (unidad 10, `:399`): control de que `remite_a` no está en el tool schema ni en las listas
   de predicados de E1.
6. **U-REEXT-T0** (unidad 11, `:400`): el grafo del perfil final de la tanda 0. Acá se cumple el criterio 4.
7. **Tanda 1** (unidad 15, `:404`): corre con el criterio 4 cumplido y repite la medición de d sobre el
   grafo escalado.
8. **A1.8,** posterior a la tanda 1 (`docs/plan_tesis.md:327`): exportación de `alcance` a Neo4j y vista del
   agente.
9. **Mesa de escritura:** los artefactos de e, cuando exista el grafo del perfil final.

No hace falta una unidad nueva de código.

## d. Qué se vuelve a medir

Sobre el grafo de la tanda con el perfil final, y antes sobre r2a:
- remisiones por firma (tipo de origen, tipo de destino) y por alcance, en citas resueltas y en aristas;
- citas irresolubles, por causa;
- el registro de citas a Comunicaciones: citas, chunks y Comunicaciones distintas;
- el criterio 4, con el test del ejemplo de la suite;
- en el tablero (`docs/tablero_correcciones.md`), las filas «Aristas `referencia` por tipo de origen» (`:51`),
  «Remisiones falsas por paráfrasis» (`:53`) y «Test del ejemplo `cla::5.1.1.1`» (`:54`), con el nombre nuevo.

La línea de base es la tabla de «Hechos verificados».

## e. Artefactos de la tesis

- **Figura 1.1** (`docs/tesis/figuras/generar_figura_norma_a_grafo.py:73`) y **Figura 1.2**
  (`generar_figura_fragmentos_vs_grafo.py:66`): dibujan la arista con el rótulo «referencia» y la leen de
  KG-Reextraído-r1 a través de `ejemplo_prestamo_datos.json:135-138`.
- **Figura 1.3** (`generar_figura_proceso_extraccion.py:170-171`) y **Figura 2.1**
  (`generar_figura_tripleta.py:126`): también dibujan la remisión con `rol_fuente = referencia_cruzada`. El
  mandato de esta unidad no las nombra.
- Con el grafo del perfil final, los extremos del ejemplo cambian además de tipo: hoy son Restriccion →
  Obligacion (r1); en la tanda 0 el 5.1.1.1 es Condicion y el 3.7 es Definicion.
- **Corrección de `docs/plan_tesis.md:360`** (aceptada por la autora el 02/10/2026 y aplicada como fe de
  erratas en esa fila). Decía «5.645 aristas `referencia` nuevas (188 cross-TO + 6 al
  TO)». Lo medido [m1]: 188 aristas entre elementos con cita de clase externa, de las que 183 van a otro
  texto ordenado y 5 quedan dentro de Capitales mínimos; y 6 a un texto ordenado. Texto de la fe
  de erratas: «188 entre elementos por citas que nombran una norma (183 hacia otro texto ordenado y 5 dentro
  del mismo) + 6 a un texto ordenado».

## Criterio 4: condición para escalar

La tanda 1 no corre si, en el grafo de la tanda 0 construido con el perfil final (U-REEXT-T0), no existe
al menos una arista `remite_a` desde un nodo anclado en `cla::5.1.1.1` hacia un nodo anclado en `cla::3.7`.
Se comprueba con el test del ejemplo de la suite, que entra en la fixture que sella la autora. Se vuelve a
comprobar sobre el grafo de cada tanda que incluya Clasificación de deudores.

## Decisiones D1 a D5

Tomadas por la autora el 02/10/2026. Todas cuestan USD 0.

- **D1. A qué nodos del punto de origen se atribuye una cita detectada en el texto de E0.** A los nodos
  del punto cuyo texto guardado contiene la unidad citada; si ninguno la contiene, a todos los nodos de
  contenido del punto. Se reporta cuántas citas caen en cada rama. La regla hacía falta porque la detección
  pasa del texto de cada nodo al texto del punto (decisión 11 del mandato), y ni el mandato ni el laudo de
  r2 (`:330`) decían qué nodos del punto remiten.
- **D2. Forma de la arista.** Clave `evidencia` para el ancla; sin `rol_fuente`, `clase` ni `via`. La
  forma de la cita queda en el registro de remisiones.
- **D3. Universo de la observación 12.** Su definición pre-registrada dice «menos relation ==
  'referencia'» (`scripts/muestra_aristas_obs12.py:22-25`; `docs/preregistro_tanda0.md` y
  `docs/enmienda_preregistro_tanda0_2026-09-27_observacion12.md`). El pre-registro de la tanda que use la
  observación 12 lleva una nota fechada de equivalencia: `remite_a` queda fuera del universo igual que
  `referencia`. PENDIENTE hasta que exista ese pre-registro (checklist, X17).
- **D4. Figuras y texto de la tesis.** Las Figuras 1.1, 1.2, 1.3 y 2.1 se regeneran desde el grafo del
  perfil final, con el rótulo «remite a». El texto de los capítulos 1 y 2 que describe el ejemplo también
  se actualiza, porque los extremos cambian de tipo. Es de la mesa de escritura (checklist, W15).
- **D5. Nombre de la propiedad `alcance`.** Se mantiene en la arista y se declara. Los nodos de contenido
  ya tienen una propiedad `alcance`, que el resolvedor lee (`r1_referencias.py:52`); son objetos distintos
  y no chocan.

## Contradicción con el mandato de esta unidad

El mandato de esta unidad de planificación dice que los 188 de `docs/plan_tesis.md:360` «incluyen 5 de las 6 aristas al Texto Ordenado».
Los archivos dicen otra cosa [m1]: las 188 son todas entre elementos, y las 6 a un texto ordenado se cuentan
aparte. La diferencia entre 188 y 183 son 5 aristas de clase externa cuyo destino está en el mismo texto
ordenado (`cap::1.4`, una, y `cap::S2`, cuatro; índices 2579 y 5115 a 5118 de KG-Reextraído-r1). La cifra
183 del mandato es correcta; cambia su explicación.

## Asientos aplicados el 02/10/2026 (sin commit)

- **Checklist** (`docs/checklist_pre_escalado.md`): ítem X17 en la sección 2 y W15 en la sección 5; el
  criterio 4 dentro de la condición 2 de «Orden y condiciones de la tanda 1».
- **Plan** (`docs/plan_tesis.md`): unidad 7 (`:396`), cambio acotado en `modelos_r2.py` autorizado por la
  enmienda 1; unidad 8 (`:397`), R3.d y R5 extendidas; unidad 10 (`:399`), `remite_a` fuera del tool schema
  de E1; `:360`, fe de erratas de la cifra.
- **Tablero** (`docs/tablero_correcciones.md`), filas `:51`, `:53` y `:54`: nota del nombre nuevo; en la
  `:54`, el criterio 4 como condición para escalar.

## Comandos

**[m1]** Remisiones por clase guardada. El alcance por la regla de la enmienda, las firmas y los índices
salen del script `remite_a_conteo_por_alcance.py` del paquete de revisión.

```bash
python3 -c "
import json, collections
for r in ('corpus_v2/salida_r1', 'corpus_tanda0/ens_desarrollo/r1', 'corpus_tanda0/ens_diez/r1'):
    kg = json.load(open('data/experiment/reextraccion_v2/' + r + '/kg.json'))
    c = collections.Counter((e['properties']['clase'], e['properties']['via']) for e in kg['edges'] if e['relation'] == 'referencia' and e.get('rol_fuente') == 'referencia_cruzada')
    print(r, sum(c.values()), dict(c))
"
```
