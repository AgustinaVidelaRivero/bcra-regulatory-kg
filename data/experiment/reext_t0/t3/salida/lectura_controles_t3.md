# U-REEXT-T0, T3, punto 3: controles a–r, cifras y lecturas

Cifras: `controles_t3.json` (de `data/experiment/reext_t0/t3/controles_t3.py`, sobre una copia del repo), en KG-Tanda0-Diez-r2b
(`12c5cfc3…`) y KG-Tanda0-Desarrollo-r2b (`6de41495…`). Las lecturas «contra el chunk» son mías, sobre la evidencia del
mismo JSON (nodos, aristas, menciones y texto de E0 r2b). Donde las cifras de los dos grafos coinciden, doy una.

- **a. Cero sin verificar, cola aparte.** `paso_por_e3.total`: 0 entidades y 0 relaciones sin verificar, en los dos grafos;
  `aristas_no_verificadas_e3.total` 0; SIN-VERIF-E3 «resuelto». Cola humana: 74 entradas en diez (73 unidades y la parte 1;
  29 `cola_humana`, 43 `veredicto_inutilizable` y 2 `reextraccion_invalida`), 59 en desarrollo; nodos con la marca: 334 en
  diez y 281 en desarrollo; de ellos, los de la parte 1: 54. Reparadas, aparte: `cap::3.1.1.2` 2 nodos (aceptada) y
  `cap::4.2.1.2::parte1` 54 (en la cola).
- **b. Remisión del ejemplo.** 2 aristas `remite_a` desde nodos anclados en `cla::5.1.1.1` hacia `cla::3.7`, en los dos grafos;
  ítem EJ-cla-5.1.1.1 «resuelto». Cumple.
- **c. Condición 10.** El nodo de la Excepcion de `cla::5.1.1.1` existe («Los créditos para consumo o vivienda quedan exceptuados
  de la cartera comercial, salvo…»). Los nodos de los dos hijos de `cla::5.1.1` con nodos (`5.1.1.1`, 8; `5.1.1.2`, 14) llevan
  todos `5.1.1` entre sus ancestros de procedencia: desde el intro se llega a ellos por la jerarquía. `cla::5.1.1::intro` no
  dejó la Definicion de alcance («Cartera comercial — alcance»). `cla::5.1.1.1` tiene 2 Condicion. Lectura: cumple la
  condición como está definida; además, la arista `exceptua` de la Excepcion hacia la Operacion la rechazó el validador por
  firma (`Excepcion --exceptua--> Operacion`), así que la Excepcion queda sin vínculo a lo que exceptúa.
- **d. BKL-0035 y BKL-0039** (solo en diez: desarrollo no tiene ctacte). `ctacte::8.3::intro` y `ctacte::8.4::intro`: sin nodos
  de contenido; BKL-0035 cierra. `ctacte::6.4.7::intro`: una Obligacion, «Observar proceso de modificación de comunicaciones»,
  cuya descripción es la cláusula («Cuando sea necesario modificar las comunicaciones … se observará el siguiente proceso»);
  lectura: su contenido es solo el encabezado de la lista. **BKL-0039 no cierra**; vuelve a la autora.
- **e. Forma A.** Sobre la validación final r2 y la E0 r2b, con el método de `reports/u_diag_proceso/code/vu_tanda0.py` y
  `vu_b_alcance.py`: 601 Condicion de ítem; 114 sin `condicion_de` (39 con la relación rechazada); de las 75 restantes,
  **42 en forma A** (encabezado de un ancestro con nodos de destino), 2 bajo un título y 31 en otro caso. Con la matriz
  congelada: 36 de 56, sobre 458.
- **f. Umbrales.** 0 elementos con `comparacion_asumida` (de 1.373 en diez y 1.225 en desarrollo); plazos sin marcador
  (`sin_marcador_plazo`), contados aparte: 207 y 183.
- **g. TextoOrdenado.** Los 10 de diez y los 5 de desarrollo con `version` y `materia`; 0 sin una de las dos.
- **h. Omisiones.** `omisiones.jsonl`: 1.882 filas en diez y 1.422 en desarrollo; `tramo_verificado` en diez: exacta 1.808,
  no 66, tokens 7, ausente 1; LN-7 «resuelto».
- **i. Aristas derivadas que tocan un nodo solo de la cola.** 1.092 en diez (`remite_a` 1.004, `establecida_en` 86,
  `padre_sugerido` 2) y 1.023 en desarrollo; de ellas tocan nodos de la parte 1: 212 en cada grafo.
- **j. Operacion.** 0 de 1.824 (diez) y de 1.440 (desarrollo) juntan más de un punto.
- **k. `properties_no_definidas`.** 153 nodos con la clave en diez y 77 en desarrollo. Las cuatro: modalidad 65 / 9,
  consecuencia 0 / 0, modalidad_clasificada 65 / 9, copia_nota_e3 78 / 57; las demás, una por una, en el JSON.
- **l. Mini-chunks a mitad de oración.** 122 de 377 mini-chunks empiezan a mitad de oración (`prompt_r2b.mini_a_mitad`); 0 tienen
  una entidad con tramo de dos segmentos (separador de `validador_r2`). El límite de P3b-2 no tiene casos en esta salida.
- **m. BKL-0032, BKL-0033 y BKL-0036.** `docvig::3.3::cierre`: la Excepcion dice que «la exención … no aplica» ante un cambio del
  número de documento, que es la polaridad del texto, y se vincula por `exceptua_obligacion` a la Obligacion de la exención;
  **cierra**. `ctacte::7.3.1.5`: la Obligacion de la baja en la Central tiene `aplica_a` hacia `Sujeto_entidad_financiera`
  («la entidad financiera interviniente»), no hacia el banco; la que va al banco es la de informar al BCRA, bajo el
  encabezado «Obligaciones a cargo del banco»; **cierra**. `lingob::2.3.2.2`: el calificador «en condiciones más favorables
  que las acordadas de ordinario a la clientela» se conserva, en una Restriccion; el chunk no tiene Operacion y la
  condición de cierre habla de una Operacion: **vuelve a la autora**.
- **n. BKL-0038.** `limita`: 312 coherentes y 1 incoherente en diez, 274 y 0 en desarrollo; `prohibe`: 86 y 56, todas
  coherentes. Los tres chunks de las aristas de r2a (`cap::6.2.1.4`, `ext::3.5.6.6`, `cap::4.3.3.1`) ya no tienen
  `limita` ni `prohibe`. La incoherente es de `ctacte::13.1`: «Prohibición de distinción entre clientes y no clientes»
  (tipo `prohibicion`) `limita` la extracción en cajeros. Lectura: el texto pide extraer «sin distinción alguna entre clientes
  y no clientes»; la Restriccion prohíbe la distinción, no la extracción, y con respecto a la extracción `limita` es el
  predicado correcto: está mal el tipo para esta arista, no el predicado. Está marcada por el control en código, así que
  la condición de cierre («o cada caso registrado con marca») se cumple.
  Las 4 aristas de r2a (`aristas_n_r2a.json`, de `data/experiment/reext_t0/t3/aristas_n_r2a.py`; las mismas 4 en los dos
  grafos r2a), leídas contra el texto de E0 r2 de su chunk: `cap::6.2.1.4` («ningún lado de la operación estará sujeto a
  exigencia de capital por riesgo específico») es una exención, no una prohibición: **está mal el tipo** (el elemento es
  una Excepcion). `ext::3.5.6.6`, sus dos aristas (los fondos «no podrán ser computados» en otros mecanismos cambiarios):
  la prohibición es real; **está mal el predicado**, que es `prohibe`. `cap::4.3.3.1` («No se aplicará el plazo mínimo
  de veinte días hábiles…» si se cumplen las condiciones): es una excepción al plazo mínimo; **está mal el tipo**.
- **o. Patrones de sujeto (BKL-0009 a BKL-0016).** Aristas `aplica_a` y `ejecuta` extraídas en el subárbol del punto de
  cada caso (procedencia de la arista), con mención y sujeto, en el JSON. T1 (`cap::2.5`), T2 (`ext::14.5`) y T3
  (`ric::3.1`): ningún «banco» donde el texto dice entidad; no reaparecen. En T3, la mención «las operaciones» quedó
  asignada al rol de alcance: un defecto de otra clase. T4 (`ext::13.4`): ningún usuario de servicios financieros; no
  reaparece. T5 (colectivo en Exterior): «la entidad» va al rol colectivo `Sujeto_rol_entidad_autorizada_exterior` en
  casi todos los casos; queda 1 arista hacia `Sujeto_entidad_financiera` (`ext::3.17.2::intro`, sugerencia del modelo),
  residuo del estrechamiento. T6 (`ext::14.1`): el VPU va a `Sujeto_vpu_rigi`, no a exportador. T7 (`ext::3.17`): ninguna
  `persona_humana`. T8 (`ext::3.18`): «los clientes…» va a `Sujeto_cliente`. T6 a T8 no reaparecen. Insumo del laudo de
  B2.4.
- **p. BKL-0028 (ctacor).** ctacor no está en la tanda 0. El grafo trae del catálogo `Sujeto_rol_alcance_ctacor` con un
  `miembro_de` desde `Sujeto_casa_de_cambio`, sin procedencia de chunk. El alcance de `ctacor::1.1` (partición b584) son
  «las entidades financieras del país». Lectura: el miembro del catálogo no es el del texto. La re-adjudicación contra el
  texto de ctacor no se puede hacer sobre estos grafos: **vuelve a la autora**.
- **q. BKL-0021.** El registro de no mapeados de r2b trae «la entidad nominada» (`ext::11.1.1.10`, cuarentena, `sin_match`),
  y el grafo tiene el propuesto `Sujeto_propuesto_la_entidad_nominada`. El chunk es el de las certificaciones que la
  entidad emite «a pedido del importador». Lectura: la mención reaparece, como «la entidad nominada»; no se cierra como «no
  reaparece».
- **r. BKL-0031.** Detector de casi duplicados sobre los dos grafos r2b: `r4_detector_casi_duplicados_r2b.json` (lo corre
  `data/experiment/reext_t0/t3/detector_casi_duplicados_r2b.py`, con el criterio del detector y los grafos r2b, y una
  variante que cuenta `remite_a` como enlace entre documentos). Pares candidatos: 4.109 en diez y 3.841 en desarrollo
  (variante con `remite_a`: 4.363 y 4.056); en los r1 de la tanda 0 eran 2.429 y 2.096
  (`data/experiment/r2_codigo/r4_detector_casi_duplicados.json`, 26d274d). Es un dato para la revisión de fusionados;
  esta unidad no lo adjudica.
