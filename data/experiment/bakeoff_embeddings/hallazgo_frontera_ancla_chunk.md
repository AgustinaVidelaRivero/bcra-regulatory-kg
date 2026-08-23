# Hallazgo para la tesis — la frontera de ancla no coincide con la frontera de chunk

Registrado en U-A2.0b-bakeoff (entregable 1) por mandato del laudo. No es un
defecto de esta unidad: es una propiedad del corpus que toda medición
cross-capa tiene que declarar.

## Enunciado

Las anclas de *provenance* que el KG hereda de la norma (`punto` del Texto
Ordenado: `7.10`, `10.4`, `3.1`) y los límites de los chunks estructurales de
E0 **no delimitan las mismas unidades de texto**. Un ancla puede:

- coincidir con un chunk terminal (caso benigno);
- no tener chunk propio y existir solo repartida entre sus sub-puntos;
- tener chunk propio que es únicamente el arranque de prosa del contenedor
  (un `mini_chunk` de rol `intro`), con el contenido en los descendientes.

El tercer caso es el más traicionero porque **el match exacto no falla: da un
resultado, y el resultado es un fragmento sin la respuesta**. Un criterio de
cobertura que cuente "¿el ancla resolvió?" lo da por bueno.

## Cuarta aparición del mismo fenómeno

1. **Censo de EV2** — `data/experiment/ev2_corrida/censo/ausencias_diagnostico.json`,
   nota sellada: "crudo=0 y desc>0 => el punto existe solo como sub-puntos
   (patrón de extracción por bloques)". 23 anclas gold no resueltas en v2 bajo
   la regla de match exacto sin descendientes.
2. **Ausencias de KG-Reextraído (A0.4)** — `docs/plan_tesis.md` §A0.4: la
   sensibilidad por descendientes de la fase B de A0.2 cubre el análisis de
   las 20 "ausencias" de KG-Reextraído, distinguiendo *ausencia total* (en
   KG-Base/KG-Refinado) de *granularidad de ancla* (en KG-Reextraído).
3. **Sensibilidad por descendientes de A0.2 (H1/H4)** —
   `data/experiment/ev2_reporte/salida/atribucion_fallas.md` §5, sellada en
   `85d9fdb`: H4 "ausencia_kg es ausencia total en KG-Base/KG-Refinado (6/6,
   4/4) y granularidad en KG-Reextraído (8/10 + 2 contenedor; sensibilidad
   informativa con descendientes: 9 → 6 generacion + 2 alcanzabilidad +
   1 ausencia)"; H1 "KG-Reextraído por granularidad de ancla (4/9 ausencia_kg,
   3 de ellas con el contenido presente solo en sub-puntos)". La atribución
   causal CAMBIA DE CLASE según se incluyan o no los descendientes: lo que sin
   ellos se lee como falla del grafo, con ellos se lee como falla de
   generación.
4. **Este mapeo (U-A2.0b, entregable 1)** — sobre los chunks de E0 y no sobre
   nodos del KG: de 37 anclas gold distintas, 9 no tienen chunk exacto y solo
   existen como descendientes, y **18 tienen chunk exacto que es solo un
   `mini_chunk` de rol `intro`** — con fragmentos de hasta 26 caracteres
   (`ext:4.8`) que dejan afuera 19 descendientes. Testigo `ext:7.10`: texto
   propio completo `'del régimen de fomento de inversión para las
   exportaciones (Decreto 234/21).'`, 15 descendientes excluidos.

Las cuatro apariciones son sobre objetos distintos —dos grafos distintos, el
censo de cobertura y ahora el chunking— con la misma causa: la norma numera
por jerarquía y el contenido no respeta esa jerarquía de manera uniforme.

## Qué obliga a declarar

Toda medición que cruce la capa de anclas con la capa de texto (recall de
retrieval, cobertura de gold, atribución causal de fallas) debe declarar
**explícitamente y antes de medir** su política de descendientes, porque:

- la política cambia el resultado, no solo su presentación (A0.2 H4 es la
  prueba: cambia la clase atribuida);
- la política "match exacto" no es la opción neutra ni la conservadora: es la
  que produce silenciosamente gold degenerado en los contenedores con `intro`;
- reportar un único número sin la política es irreproducible.

En esta unidad la consecuencia práctica fue medir bajo dos reglas declaradas
(R2 subárbol completo, y un control de gold bien formado) sobre los mismos
índices, y leer el resultado solo si las dos coinciden en el orden.
