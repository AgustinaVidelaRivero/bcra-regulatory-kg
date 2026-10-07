# Protocolo de los dos grafos: el evaluado y el corregido

**FIRMADO por la autora el 07/10/2026** (firma por mensaje de la autora; BORRADOR redactado el 07/10/2026 en la unidad
RECONC-DISENO-EVAL y entrado al repo en `93bebd2`). Rige desde esta firma, con dos decisiones al firmar: la propuesta del §3, punto 4,
aceptada, y la ubicación en la tesis según la estructura vigente (§2, punto 4; §3, punto 3; §5, punto 3). Será una sección del protocolo
del ciclo de refinamiento de B2.6 (`docs/protocolo_ciclo_refinamiento.md`, hoy NO ENCONTRADO, `plan:382` y checklist W3 `:217`) cuando ese
protocolo exista. Los nombres del §1 quedaron DECIDIDOS por la autora el 07/10/2026 (D13).

## 0. De dónde sale

- D13 de las reuniones del 18 y el 19/08/2026 (acta confirmada el 07/10/2026, `docs/registro_reunion_mentores_2026-08-18_19.md`): la versión científica reporta el grafo tal como se evaluó; el
  entregable puede corregirse después, declarado como posterior; dos contribuciones, el método y el grafo.
- Principio 9 (`plan:277-283`, plan v6 en `87db24c`, 23/08/2026) y laudo 3 del 20/09/2026 sobre nombres y capítulos
  (`plan:287`, asentado en `e58d41d`).
- Laudo D-f, §5, último ítem (`966253e:docs/laudo_D-f_secuencia_tripletas.md:53-54`).
- B6.3, regla dura: si el resultado obliga a tocar el pipeline, el arreglo produce una release posterior y no se re-corre la
  evaluación para mejorar el número (`plan:773`).
- Protocolo entre tandas, FIRMADO (`a304b89`), decisión D3 (§10), y su enmienda 5, FIRMADA (`ccd8fad`): desde la tanda 1, el
  grafo de cada tanda que se evalúa es el ensamblado sin la cola humana, sellado junto con el completo (§1); una unidad de la
  cola vuelve solo por una corrección registrada que el verificador acepta, en la release siguiente (§3).
- Enmienda del uso de la ventana (`30f106c`, citada en `plan:741`): los cambios de esquema, prefijo o formato de salida de E1
  posteriores al ciclo B2.11 van a la versión posterior a la evaluación.

## 1. Nombres (DECIDIDOS por la autora el 07/10/2026)

| nombre en la prosa | qué es | dónde está definido |
|---|---|---|
| **el grafo evaluado** | el grafo escalado, sellado antes del pre-registro de B6.3; el que mide el capítulo 5 (Evaluaciones) | laudo 3 (`plan:287`) |
| **el grafo corregido** | la release posterior a los informes de B6.3 y de B4, declarada como tal; el entregable del capítulo 6 (Recurso) | laudo 3 (`plan:287`) |
| **grafo sin cola de la tanda N** (decidido el 07/10/2026) | el ensamblado de una tanda sin las unidades de la cola humana; el que miden las vigilancias y lecturas de la tanda | hoy la enmienda 5 lo llama «grafo evaluado de cada tanda» (`ccd8fad:…:27`) |
| **grafo completo de la tanda N** (decidido el 07/10/2026) | el ensamblado de la tanda con la cola adentro y marcada | enmienda 5, §1 («sellado junto con el completo») |
| KG-Reextraído-r1, r2, r2b… | nombres de release del ciclo B2.6 | se quedan en el plan; en la tesis, en una tabla del capítulo 4 (Construcción) (`plan:287`) |

Para la tanda 0: «grafo sin cola de la tanda 0» = KG-Tanda0-Diez-r2b-sincola (`e22fae1a…`) y KG-Tanda0-Desarrollo-r2b-sincola
(`2922b72d…`), sellados en `dde9f44` y `235a295`; el mandato de U-SINCOLA-T0 los llama «grafo evaluado de la tanda 0»
(`docs/mandatos/USINCOLA_T0_grafo_evaluado_sin_cola.md`). Por qué cambiar: el laudo 3 reserva «el grafo evaluado» para el
escalado sellado antes de B6.3, y la tanda 0 se publica como validación de diseño (`plan:746`); con el mismo nombre en los dos
niveles, la tesis diría que un grafo de desarrollo es el evaluado. Alternativas que descarto: «grafo medido de la tanda N»
(la tanda 0 no es una medición de la tesis) y «grafo de control» (choca con las muestras de control).

**Los textos firmados no se editan.** «grafo evaluado» aparece 67 veces en 33 archivos de HEAD (`git grep -c "grafo evaluado"
HEAD -- docs data`), entre ellos la enmienda 5 y los mandatos firmados de U-SINCOLA-T0 y U-LECTURA-ACEPTADAS. Una nota fechada al
pie de cada documento firmado declara la equivalencia («donde dice “grafo evaluado de la tanda”, léase “grafo sin cola de la
tanda”»); los textos nuevos usan los nombres nuevos; la tesis, solo «el grafo evaluado» y «el grafo corregido».

## 2. El grafo evaluado

1. **Composición.** El ensamblado acumulado de todas las tandas en la última release del pipeline anterior al pre-registro de
   B6.3, sin la cola humana (enmienda 5, §1), con su grafo completo sellado al lado.
2. **Sello.** Antes de sellar el pre-registro de B6.3: sha256 del `kg.json`, manifiesto de E0 y su sha, release del pipeline
   (prefijo de E1 y código), catálogo, registro en `data/experiment/neo4j/grafos.py` y carga con su gate. Su etiqueta de
   release se asigna al sellarlo (`plan:995`). El pre-registro de B6.3 cita ese sha, y el índice de fragmentos de B6.3 (f) se
   construye sobre el mismo manifiesto de E0.
3. **Qué no se hace.** No se corrige en el lugar; no se vuelve a correr B6.3 sobre otra versión para mejorar una cifra
   (`plan:773`). Todo defecto que muestre la evaluación va al backlog con su `capa_pipeline` y el id del hallazgo.
4. **Qué se reporta.** Todo lo de B6.3, (b) a (f), sobre este grafo y tal como salió, con la cifra de la cola al lado (unidades
   fuera y su tasa de error leída). Va al capítulo 5 (Evaluaciones).

## 3. El grafo corregido

1. **Qué entra.** (a) Las correcciones motivadas por la evaluación: hallazgos de B6.3 y ausencias importantes de B4 (B4.4,
   `plan:454-456`), cada una como entrada de backlog; (b) las unidades de la cola que vuelven por la regla de la enmienda 5, §3;
   (c) los cambios de esquema, prefijo o formato de E1 diferidos por la enmienda de la ventana (`plan:741`); (d) lo que quedó
   fuera del evaluado por calendario y esté declarado (por ejemplo, U-BLOQUE-A si no llegó, `plan:772`).
2. **Cómo.** Hallazgo → entrada de backlog con `capa_pipeline` → test de regresión que falla sobre el grafo evaluado → cambio en
   el pipeline, en código antes que en reproceso (principio 12, `plan:299`) → re-corrida con caché → gate de release (suite de
   regresión, shapes, intrínsecas; `plan:382`) → sha nuevo → release declarada.
3. **Qué se reporta.** La lista de correcciones con su origen (hallazgo, qué cambió, qué test lo prueba), el gate de release,
   la diferencia de tamaño contra el evaluado (unidades, nodos, aristas) y el costo. Va al capítulo 6 (Recurso), como
   entregable, y a la publicación (C2), con los dos grafos y sus sha. El laudo 3 lo ubicaba en las conclusiones; la estructura
   vigente de la tesis lo lleva al capítulo 6 (decisión de la autora del 07/10/2026).
4. **Qué no se reporta como evaluación.** Ninguna cifra sobre el conjunto de test de B6.3 se presenta como si fuera la evaluación.
   **Decidido por la autora el 07/10/2026, con la firma:** el grafo corregido no se mide sobre ese conjunto; su mejora se demuestra
   con los tests de regresión nacidos de cada hallazgo (cada uno falla en el evaluado y pasa en el corregido). Si se midiera, se
   reporta como análisis exploratorio posterior y nunca en la misma tabla (regla de admisibilidad de B6.3, `plan:773`).

## 4. Lo que no es el grafo corregido

Las releases r2, r2a y r2b del ciclo B2.11 son anteriores al grafo evaluado: corrigen lo que mostró la tanda 0, que se publica
como validación de diseño (`plan:746`). Lo mismo vale para toda release entre tandas declarada antes de sellar el pre-registro de
B6.3 (`plan:741`). Ninguna de ellas es «el grafo corregido».

## 5. Lo que falta para cerrarlo

1. El protocolo del ciclo de refinamiento de B2.6, del que este documento sería una sección (W3, `checklist:217`).
2. ~~La decisión de nombres y las notas al pie de los documentos firmados.~~ Hecho el 07/10/2026: nombres decididos; notas al pie
   en el mandato de U-SINCOLA-T0 y en la enmienda 5 al protocolo entre tandas.
3. ~~La numeración de capítulos (F-4).~~ **Cerrada el 07/10/2026 (decisión de la autora, con la firma).** Estructura vigente de la
   tesis: 1 Introducción, 2 Marco, 3 Esquema, 4 Construcción, 5 Evaluaciones, 6 Recurso, 7 Conclusiones. La medición del grafo
   evaluado va en el capítulo 5; el grafo corregido, como entregable, en el capítulo 6. El laudo 3 (`plan:287`) los ubicaba en el
   capítulo 8 y en las conclusiones; la nota fechada en el plan asienta el cambio.
4. Mencionarlo a los mentores: la enmienda 5 deja fuera del grafo evaluado las unidades que el verificador no aceptó (74 en la
   tanda 0, `plan:400`), y eso cambia qué es «el grafo que se evalúa» respecto de lo conversado el 19/08.

## Firma

FIRMADO por la autora el 07/10/2026 (BORRADOR en `93bebd2`). Rige desde esta firma. Decisiones al firmar: (a) la propuesta del §3,
punto 4: el grafo corregido no se mide sobre el conjunto de test de B6.3, y si se midiera va como análisis exploratorio posterior,
nunca en la misma tabla; (b) la ubicación en la estructura vigente de la tesis: la medición del grafo evaluado en el capítulo 5 y el
grafo corregido, como entregable, en el capítulo 6 (F-4 cerrada). Siguen abiertos el §5, puntos 1 y 4.
