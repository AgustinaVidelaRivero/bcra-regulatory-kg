# U-CONS-ARCO-EJEMPLO — informe de la consulta

Hice solo lectura: leí los `kg.json` y los archivos del ensamblado, sin consultas a Neo4j, sin API y sin escribir en el repositorio. `.pyc` sigue en 2.213.

En `git status` aparecen modificados siete archivos de `docs/tesis/figuras/` que no son míos, además de las salidas de E5.b en `ev2_tanda0/`. HEAD es `791166d`: su mensaje dice que trae la fuente de «los seis puntos de ext que nunca son origen». Con eso se puede resolver el NO VERIFICADO del ítem 4 del asiento anterior; no lo toqué.

**Lo principal, antes del detalle:**
- **A:** a Clasificación de deudores llegan remisiones desde capitales mínimos y, en el grafo de diez, desde `polcre::2.1.7`. Esa remisión quedó resuelta, pero al nodo del documento, no a un punto.
- **Hallazgo nuevo en A:** en el grafo de diez, la remisión de `cap::8.2.3.3` a los puntos 6.5.1 y 7.2.1 de Clasificación de deudores se resolvió como interna. Sus nueve aristas llegan a nodos de riesgo de mercado de capitales mínimos.
- **B:** ninguna pregunta de EV2 toca el 5.1, el 3.7 ni el 3.3.3.
- **C:** en r1, la Operacion del 5.1.1.1 no tiene `aplica_a`.
- **D:** el grafo no guarda una cita textual en la procedencia de los nodos, solo la dirección del texto.

---

## A — Remisiones de otros documentos hacia Clasificación de deudores

Criterio: aristas `referencia` cuyo origen no tiene ninguna procedencia en `cla` y cuyo destino tiene alguna.

| Grafo | Aristas | Origen | Destino |
|---|---|---|---|
| KG-Tanda0-Diez-r1 (`dd42d6d9…`) | 11 | 9 de `cap::2.3.1`, 1 de `cap::3.1.3.2`, 1 de `polcre::2.1.7` | 2 al nodo TextoOrdenado de cla; 9 a nodos de los puntos 6.5.1 y 7.2.1 |
| KG-Reextraído-r1 (`0226e947…`) | 31 | 15 de `cap::8.2.3.3`, 15 de `cap::2.3.1`, 1 de `cap::3.1.3.2` | 1 al TextoOrdenado; 30 a nodos de 6.5.1 y 7.2.1 |

**Los extremos de cada arista.** Los orígenes son siempre Obligacion, Operacion o Restriccion; ninguno es Condicion, Potestad ni Definicion.
- `cap::3.1.3.2`: una Obligacion («Información incluir — clasificación promedio deudores» en el grafo de diez; «Incluir información de clasificación promedio deudores» en r1) hacia el TextoOrdenado «Clasificación de Deudores», con `via=texto_ordenado`.
- `cap::2.3.1`, en el grafo de diez: la Restriccion «Exclusión de deducción 100% previsión cartera normal» hacia 1 Condicion, 3 Definicion, 2 Excepcion, 2 Obligacion y 1 Potestad de `cla::7.2.1` y `cla::6.5.1`, con `via=nodos_del_punto`. En r1, la misma Restriccion tiene 15 aristas hacia Excepcion, Obligacion, Operacion y Restriccion de esos puntos.
- `cap::8.2.3.3`, solo en r1: la Obligacion «Previsiones por incobrabilidad — deudores en situación normal», con 15 aristas hacia nodos de `cla::6.5.1` y `cla::7.2.1`.

**`polcre::2.1.7`.** El texto de E0 (`salida_tanda0/chunks_polcre.json`) dice: «Financiaciones a clientes de la cartera comercial y de naturaleza comercial que reciben el tratamiento de los créditos para consumo o vivienda –de acuerdo con las disposiciones establecidas en las normas sobre “Clasificación de deudores”–, cuyo destino sea la importación de bienes de capital […]».
- **Nodos en el grafo de diez:**
  - la Operacion `Operacion_financiacion_de_importacion_de_bienes_de_capital_3c985a`, «Financiación de importación de bienes de capital», con `aplica_a` hacia «Entidades financieras» y **`referencia` hacia el TextoOrdenado «Clasificación de Deudores»**;
  - la Definicion `Definicion_bk_bienes_de_capital_nomenclatura_mercosur_e4eb4b`, que no nombra Clasificación de deudores.
- **Estado: resuelta** en `ens_diez/r1/referencias_remisiones.json`: `clase` externa, `norma_nombrada` «Clasificación de deudores», `puntos` vacío, `destinos` `["cla::TO"]`. No figura en `referencias_irresolubles.json`.
- **H1:** no aplica. El origen es una Operacion, y la Definicion no contiene remisión.
- **Opinión:** la remisión llega al documento y no a los puntos que tratan el tema, el 5.1.1.2 y el 5.1.2.4, porque el texto nombra la norma sin punto. Es lo que el texto permite.
- `polcre` no está en r1, que tiene solo los cinco documentos de desarrollo.

**Remisiones sin detectar por H1.** Busqué, fuera de cla, nodos cuyo texto nombre «Clasificación de deudores», mirando los campos que escanea el resolvedor más `termino`. Hay cuatro: `cap::3.1.3.2`, `polcre::2.1.7`, `cap::8.2.3.3` y `cap::2.3.1`. Los cuatro son Obligacion, Operacion o Restriccion, y los cuatro son origen de alguna remisión. **Ninguno es Condicion, Potestad o Definicion:** hacia cla, H1 no deja remisiones sin detectar.

**Hallazgo: `cap::8.2.3.3` mal resuelta en el grafo de diez.**
- **El texto de E0:** «(puntos 6.5.1. y 7.2.1. de las normas sobre “Clasificación de deudores”)».
- **La descripción extraída en r1** conserva «de las normas sobre "Clasificación de deudores"», y la remisión llega al cla.
- **La descripción extraída en el grafo de diez** dice «(conforme puntos 6.5.1 y 7.2.1 de normas de Clasificación de deudores)».
- **Por qué falla:** el patrón del resolvedor reconoce «normas sobre», «T.O. sobre/de» y «Texto Ordenado sobre/de», no «normas de» (`RE_NORMA`, `data/experiment/reextraccion_v2/corpus_v2/r1_referencias.py:63-65`). Los puntos que no tienen norma reconocida se tratan como del mismo documento (`:180-187`).
- **Resultado:** en `ens_diez/r1/referencias_remisiones.json` la remisión figura como `clase` interna, `to_destino` cap, `estado` parcial, con destino `cap::6.5.1`. En el grafo son nueve aristas desde la Operacion «Previsiones por riesgo incobrabilidad» hacia nodos de riesgo de tasa y de productos básicos de `cap::6.5.1`, por ejemplo «Exposición a riesgo de base».
- **Opinión:** son remisiones falsas en el grafo. La causa es que el resolvedor lee la paráfrasis del extractor y no el texto del punto. Es un candidato para r2, en la misma familia que el ítem 4 del laudo.

## B — Preguntas de EV2 sobre 5.1, 3.7 o 3.3.3

Crucé `data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json` (40 preguntas) por ancla, y por la cita textual de cada criterio buscada en el texto propio y en la herencia de los chunks de `cla` de esos puntos.

**NO ENCONTRADO:** ninguna pregunta tiene ancla ni criterio en `cla::5.1` o sus subpuntos, en `cla::3.7` ni en `cla::3.3.3`. Las seis preguntas de Clasificación de deudores anclan en otros puntos:

| Pregunta | Ancla |
|---|---|
| EV2F-025 | `cla:2.1` |
| EV2F-026 | `cla:3.5` |
| EV2F-027 | `cla:6.1` |
| EV2F-028 | `cla:3.1` |
| EV2F-029 | `cla:4.1` |
| EV2F-030 | `cla:10.3` |

## C — Sujetos

**En KG-Reextraído-r1, la Operacion del 5.1.1.1 no llega a ningún sujeto:** «Inclusión en cartera comercial — créditos consumo/vivienda» no tiene `aplica_a` ni `ejecuta` (NO ENCONTRADO). Sus dos Restriccion tampoco. El nodo del ejemplo que sí llega a un sujeto es la Obligacion del 3.7, con `aplica_a` hacia `Sujeto_rol_obligado_a_clasificar_clasificacion`, «Obligados a clasificar deudores (Clasificación)», de nivel rol.

En KG-Tanda0-Desarrollo-r1, en cambio, la Operacion del 5.1.1.1 sí llega a ese rol.

**Desde ese rol**, recorriendo `miembro_de` y hacia abajo por `subclase_de` e `instancia_de`, se alcanza lo mismo en los dos grafos:
- **Miembros:** `Sujeto_entidad_financiera`, `Sujeto_fiduciario_de_fideicomiso_financiero`, `Sujeto_fondo_de_garantia_publico`, `Sujeto_proveedor_no_financiero_de_credito`, `Sujeto_pscpp` y `Sujeto_sociedad_de_garantia_reciproca`. Los seis son de nivel clase.
- **Por subclase:** `Sujeto_banco`, `Sujeto_banco_comercial`, `Sujeto_caja_de_credito`, `Sujeto_caja_de_credito_cooperativa`, `Sujeto_compania_financiera` y `Sujeto_empresa_no_financiera_emisora_de_tarjetas`.
- **Instancias:** ninguna.

**`cla::10.1` en KG-Reextraído-r1:**
- La Obligacion «Clasificación de deudores por mora — consumo/vivienda» tiene:
  - `aplica_a` hacia `Sujeto_proveedor_no_financiero_de_credito` y `Sujeto_empresa_no_financiera_emisora_de_tarjetas`;
  - `regula` hacia la Operacion «Clasificación de deudores por mora»;
  - cuatro `referencia` hacia nodos de recategorización del 7.3.

  Su descripción dice «según los criterios aplicables para la cartera de "consumo o vivienda"».
- **No hay ninguna arista** que una esos sujetos con los nodos del 5.1.2 ni con los del 5.1.1.1: la relación con los criterios de consumo o vivienda está solo en el texto de la descripción.

## D — Lo que el grafo guarda para las figuras

En KG-Reextraído-r1, la procedencia de cada nodo guarda la dirección del texto: `to`, `archivo`, `punto`, `rol_documental`, `chunk_id`, `paginas` y `ancestros`. **No guarda una cita textual: NO ENCONTRADO.** El texto disponible es la `descripcion` extraída en `properties`.

| Nodo | Procedencia | Descripción guardada |
|---|---|---|
| Operacion «Inclusión en cartera comercial — créditos consumo/vivienda» | `cla::5.1.1.1`, página 16, ancestros S5 > 5.1 > 5.1.1 | ninguna; solo `tipo` «clasificación de crédito en cartera» |
| Restriccion «Créditos consumo/vivienda — monto supera dos veces importe referencia» | `cla::5.1.1.1`, página 16 | «Los créditos para consumo o vivienda que superen el equivalente a dos veces el importe de referencia establecido en el punto 3.7.»; `umbral` «2x importe referencia punto 3.7» |
| Restriccion «Crédito — repago no vinculado a ingresos fijos, vinculado a actividad productiva» | `cla::5.1.1.1`, página 16 | «Créditos cuyo repago no se encuentre vinculado a ingresos fijos o periódicos del cliente sino a la evolución de su actividad productiva o comercial.» |
| Obligacion «Considerar importe de referencia — ventas anuales Micro Comercio» | `cla::3.7`, página 14, ancestros S3 | «El importe a considerar será el nivel máximo del valor de ventas totales anuales para la categoría "Micro" correspondiente al sector "Comercio" que determine la autoridad de aplicación de la Ley 24.467 (y sus modificatorias).» |

**La arista de remisión** del 5.1.1.1 al 3.7 guarda como evidencia «ente a dos veces el importe de referencia establecido en el punto 3.7. | 2x importe refere», que es una ventana de caracteres cortada. Además guarda `clase` interna, `destino` `cla::3.7`, `via` `nodos_del_punto` y `rol_fuente` `referencia_cruzada`.

**Opinión:** para citar en una figura, el texto de la norma tiene que salir de E0 (`chunks_cla.json`) por el `chunk_id`, no de la descripción. La descripción del 3.7 coincide con la norma, pero la del repago agrega «Créditos» al principio y la de la Operacion no existe.

FRENO.
