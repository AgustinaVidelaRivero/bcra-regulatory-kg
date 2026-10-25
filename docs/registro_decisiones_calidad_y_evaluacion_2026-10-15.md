# Registro de las decisiones de la autora del 15/10/2026 sobre la calidad del grafo evaluado y la evaluación (mesa)

USD 0. Las decisiones llegaron en el mensaje recibido a las 13:00:14 (hoja de ruta de la mesa, §102). Las propuestas sobre las que
decidió están en el paquete de la mesa:
- `decisiones_101_mesa/propuestas/propuestas_101_mesa.md`, sha256 `beb7ae92…`;
- `decisiones_101_mesa/calidad/lista_calidad_grafo_evaluado_mesa.md`.

Este registro copia lo aprobado tal cual. La enmienda 8 al protocolo entre tandas, firmada el mismo día, lleva las cuatro decisiones que
cambian el protocolo (`docs/enmienda8_protocolo_entre_tandas_2026-10-15_calendario_hacia_B6.3.md`).

## 1. U-EVAL-CLASES: O2

- **La decisión, tal cual:** «O2, con la caída que propusiste (si cae la tanda final, baja a lo que haya en la tanda 1, declarado).
  Antes de fijarla, confirmame cuántos documentos elegibles quedan en la bolsa por grupo con todas las exclusiones de hoy (...) y que
  alcanzan para 8 de régimen informativo. Si no alcanzan, frená y decido.»
- **O2:** 8 documentos de régimen informativo, 4 de normativa general «digerible» y 4 de «necesita reglas».
- **La cuenta de la mesa** (`data/experiment/esq/elegibles_B63_O2_2026-10-15/`; la elegibilidad de cada clase, de
  `data/experiment/escalado_prep/inventario_unidades.csv`):

  | Capa | Quedan | RI | NG digerible | NG necesita reglas |
  |---|---|---|---|---|
  | los 137 elegibles (`docs/plan_tesis.md:782`) | 137 | 53 | 53 | 31 |
  | sin los 15 documentos de la enmienda 8 (decisiones 1 y 2) | 122 | 42 | 52 | 28 |
  | sin ri2_pm ni lo que no entra al grafo (los no segmentables, manual y ri_ao) | 109 | 30 | 52 | 27 |
  | sin los que tienen una constante por documento en el código de E0 (39) | 78 | 26 | 36 | 16 |
  | sin los que saca la release de E0 (nmaeef y ri_niif, ya fuera) | 78 | 26 | 36 | 16 |

  - Las constantes por documento se tomaron del árbol sintáctico de los tres archivos de E0 del manifiesto de S0-6b, sin docstrings.
  - Las tres listas `TOS_TANDA0_*` son exclusiones de la tanda 0, que ya está fuera de B6.3, y no correcciones; no cuentan.
- **Alcanzan para O2:** quedan 26 de régimen informativo para los 8 que pide.
- **En la rama de caída** (solo la tanda 1, sin el sucesor de ri_oc, que fija S2) quedan 6: 3 de régimen informativo, 1 de normativa
  general «digerible» y 2 de «necesita reglas» (ceninf, lingeef, ri_dcpc, ri_gerc, ri_pgn y snp_tr). Por la decisión, O2 baja a lo que
  haya, declarado.
- O2 queda fijada con esa caída.

## 2. L-02 y L-04: quién lee, la pregunta, las clases, qué cuenta y los controles

- **La decisión, tal cual:** «apruebo tu propuesta tal cual (§1 de propuestas_101_mesa.md): quién lee, la pregunta, las clases, qué cuenta
  y los controles.»
- Cierra el pendiente 27 del pre-registro de la tanda 1.
- Lo aprobado, copiado de la propuesta:

Decisión de la autora del 15/10/2026: «una lectora a ciegas y mi adjudicación, como en S1-quater».

#### 1.1 Quién lee, en las dos

- **La lectora:** una sesión nueva de Claude Code con `claude-opus-5-5`, como las lectoras de S1-ter y de S1-quater
  (`data/experiment/segmentacion_oficial_e0r2/s1quater/lectura/registro_lectura_etapa_1_S1quater_mesa.md:12-13`).
  - **Dónde:** en su propia carpeta, fuera del repo (`fuera_del_repo/lecturas_ciegas/lectura_L02_L04/`). La instala la mesa, como en
    S1-quater.
  - **Paso 0:** `pwd`, con la carpeta personal como `$HOME`. Lleva la cláusula de carpetas vedadas, salvo su propia carpeta, y no toca el
    repo.
  - **Qué ve:** los casos sin el veredicto del clasificador ni la marca del validador, sin ids y en un orden sorteado.
  - **El sello:** sella su planilla con un script antes de que la mesa la abra.
  - **El control:** la mesa controla la sesión por script, como en los §89 y §90: que haya mirado las páginas de cada caso antes de
    marcarlo y que no haya abierto nada más.
- **Tu adjudicación, como en S1-quater:**
  - **pasada 1:** todos los casos, sin ver la marca de la lectora ni la del clasificador;
  - **pasada 2:** los casos que elija la regla, con la marca de la lectora a la vista:
    - a. tu marca y la de la lectora no coinciden;
    - b. las dos dicen lo mismo en lo que cuenta para el piso, pero con otra clase;
    - c. la lectora dejó una nota;
  - **la cifra:** decide la de tus marcas finales. Wilson inferior al 95 % ≥ 0,75 sobre las decididas, que con 30 es 28 de 30; las
    dudosas se excluyen y el piso se recalcula (§6.7 del pre-registro);
  - **los scripts** (`armar`, la cifra y el acuerdo) se sellan antes de tu pasada 1, como el 59.
- **Cuándo:** al cierre de la tanda en que el pozo llega a 30 (§5.4 d del pre-registro). Las semillas del sorteo se sellan antes de
  leer (pendiente 19).

#### 1.2 L-02: la precisión del clasificador de copia de la nota de E3 (ventana 5, con flexión, sobre las entidades `aceptado_tras_reintento`)

- **Los casos:** 30 detecciones del pozo, sorteadas si son más. Cada caso trae:
  - el campo (la descripción o la etiqueta);
  - el texto propio y heredado de la unidad, con sus páginas;
  - las notas de E3 que E1 leyó en el reintento, antes de escribir ese campo;
  - las ventanas de cinco palabras, normalizadas y con flexión, que el campo comparte con esas notas;
  - la ayuda de la lectura (e): las palabras de contenido de las ventanas que no están en la unidad, y las de metalenguaje del verificador.
- **La pregunta:** ¿el campo copia la nota del verificador, o dice con sus palabras lo que dice la norma?
- **Las clases:** las de la lectura (e), tal cual (`data/experiment/omisiones_cod/lectura_e/instrucciones_lector_lectura_e.md`). Rige la
  primera que se cumple:
  1. **copia real:** las ventanas llevan metalenguaje del verificador;
  2. **coincidencia legítima:** cada palabra de contenido está en la unidad, y la frase es una reformulación fiel de la norma;
  3. **copia real:** las ventanas traen una palabra de contenido que no está en la unidad;
  4. **dudosa:** no se puede decidir con los textos solos.
- **Qué cuenta:**
  - correcta, 1 o 3 (el clasificador acierta);
  - incorrecta, 2;
  - dudosa, 4, que queda fuera.
- **El único cambio respecto de (e):** las ventanas son de cinco palabras, no de tres, porque es la variante del código previsto
  (`omisiones_cod/o1/diseno_O1.md:69-74`).

#### 1.3 L-04: la marca `tipo_no_derivable` (nodos `Comunicacion` que no son comunicaciones)

- **Los casos:** 30 marcados del pozo, sorteados si son más, y 30 controles: nodos `Comunicacion` con `tipo` (A, B, C o externa) de las
  mismas tandas, con su propia semilla. Van mezclados, en un orden sorteado.
- **Lo que ve la lectora de cada caso:**
  - el nombre del nodo tal como lo escribió E1, sin `tipo`, sin la marca, sin ids y sin el grupo;
  - el texto propio y heredado de la unidad, con la oración donde aparece resaltada;
  - sus páginas.
- **La pregunta:** en esta unidad, lo que nombra el nodo, ¿es una comunicación (del BCRA o de otro emisor) o es otra cosa?
- **Las clases.** Rige la primera que se cumple:
  1. una comunicación del BCRA (A, B, C u otra serie del BCRA, con su número);
  2. una norma externa (ley, decreto, resolución u otra norma de otro emisor);
  3. un punto o una sección, de este texto ordenado o de otro;
  4. un texto ordenado u otro documento, nombrado por su título;
  5. un organismo o una entidad;
  6. dudosa: no se puede decidir con la unidad a la vista.
- **Qué cuenta en los marcados:**
  - correcta, 3, 4 o 5 (la marca acierta: no es una comunicación);
  - incorrecta, 1 o 2;
  - dudosa, 6, que queda fuera.
- **Los controles** no cuentan para el piso. Un control leído como 3, 4 o 5 es un nodo de clase equivocada que la marca no ve, y se
  reporta aparte, como dato del límite declarado (propuesta del 12/10, §2, punto 5).
- **Por qué cinco clases y no dos:** la cifra usa solo «comunicación o no». Las clases 3 a 5 dicen qué es cada error y alimentan la
  opción (ii) del cap. 6 (reapuntar los nombres de TOs). No cambian la cifra.

#### 1.4 El tamaño y tu tiempo

- **La lectora:** 90 casos, 30 de L-02 y 60 de L-04. Las lectoras de S1-quater tardaron de 11 a 12 minutos por 90 o 60 fichas.
- **Tu pasada 1:** los mismos 90 casos, de 2 a 3 h. El comparable es la pasada 1 de S1-quater: 90 fichas en 2 h 29 min, aunque los casos
  son más cortos (NO VERIFICADO).
- **Tu pasada 2:** de 30 min a 1 h (NO VERIFICADO).

## 3. Las sesiones que solo transcriben lo que dicta la autora

- **La decisión, tal cual:** «la opción A, con sus seis condiciones, desde mi próxima adjudicación. Las notas que dicto son mías, y se
  declaran como texto que la sesión vio.»
- Rige desde la próxima adjudicación de la autora. Lo aprobado, copiado de la propuesta:

Se permite, con estas condiciones fijadas antes de cada pasada:
1. **La carpeta:** la sesión corre en una carpeta propia, fuera del repo y fuera de tu carpeta de adjudicación. Tiene solo dos cosas, que
   instala la mesa:
   - una copia vacía de la planilla;
   - un script de escritura que recibe el id de la ficha y los valores, controla que sean de los permitidos, escribe esa fila y muestra
     solo esa fila.
2. **Qué no hace la sesión:**
   - no abre fichas, imágenes, notas de criterios ni ningún otro archivo;
   - no lee la planilla salvo por el script;
   - no propone, corrige ni comenta marcas ni notas.
3. **Qué dictás vos:** solo el id de la ficha y los valores, la nota incluida, que es tuya. No pegás texto de las fichas en el chat.
4. **Al terminar:** copiás la planilla a tu carpeta y la sellás como siempre.
5. **La medición es obligatoria** (no como en la pasada 2 de S1-quater). La mesa mide la sesión por script, solo con cuentas:
   - qué archivos abrió;
   - si apareció texto de fichas en el chat;
   - si escribió algo fuera del script o algo que no dictaste.
6. **Si la medición encuentra algo** (texto de fichas visto, o una escritura no dictada):
   - se declara;
   - esas fichas salen de una cifra de control, como las 26 de S1-quater;
   - vos decidís si la pasada vale.

## 4. Lo pendiente que afecta la calidad del grafo evaluado

Las decisiones, tal cual en lo esencial:
- **B′ y U3 con su control:** en el carril del grupo 2, desde el 16/10/2026, «sin demorar nada del camino a la tanda 1». El tamaño, la
  semilla y el piso del control de las uniones quedaron sellados el 15/10/2026
  (`data/experiment/union_estrecha/control_tanda1/parametros_control_uniones_tanda1_2026-10-15.md`).
- **L-01:** la mesa redacta su mandato recién cuando estén listos S2, el re-sellado, el laudo y el pre-registro v8. La autora decide si
  entra al leerlo. El mandato tiene que decir:
  - qué aristas saca el filtro (las 643 o una parte);
  - cuántas correctas se lleva junto con las falsas;
  - cuántas horas de la autora cuesta.
- **Al grafo corregido del cap. 6, declarados:** los casi duplicados, U-BLOQUE-A, el grupo C y U-PARES-REMITE-A.
- **La herencia en la E0 corregida:** declarada, con la señal de la regresión de S1-quater
  (`data/experiment/segmentacion_oficial_e0r2/s1quater/adjudicacion/cierre/registro_cierre_adjudicacion_S1quater_mesa.md`, §7).
- **El re-censo de la release de E0:** se suma a S2 solo si no demora la tanda 1. Si la demora, va en un despacho aparte, después.
- **L-02, L-04 y la etapa P de U-MED-UMBRALES:** según su regla.
- **La cola humana, la cuarentena y las formas A y B:** sin cambios.

## 5. B6.3: el N de la rama principal y el reparto en la rama de caída (agregado del 15/10/2026)

Las decisiones llegaron en el mensaje recibido a las 14:15:41 (hoja de ruta de la mesa, §104). La propuesta sobre la que decidió está en
el paquete de la mesa: `decisiones_103_mesa/potencia/propuesta_preguntas_rama_de_caida_mesa.md`, con su script y su salida.

- **El N de la rama principal, tal cual:** «El N de la rama principal sale de Q5, con las tasas de A2.2, para una potencia de 0,80, y no
  de las 4 preguntas por documento. Cuando lo propongas:
  - compará repartirlo en más documentos, con las proporciones de O2, contra hacer más preguntas por documento, con su efecto de diseño;
  - decime cuántas horas mías suma, entre aprobar las preguntas y adjudicar.

  Si ese N no entra en el calendario, frenás y decido, y lo que se use se declara con la potencia que alcanza.»
  - Las tasas son las de los pares discordantes que mide A2.2 (`docs/plan_tesis.md:340`, registro del 07/10/2026, D1). A2.2 corre
    después de la tanda 1 y necesita el pre-registro sellado de A2.1 (`:339`).
- **La rama de caída, la opción A, tal cual:** «Mantiene el N de la rama principal, con las proporciones de O2 por clase, dentro de cada
  clase en proporción a las unidades, con un piso de 4 y el tope de la mitad de las unidades. Si los topes no alcanzan para el N, el
  total baja a la suma de los topes. La pérdida por el agrupamiento se declara con su efecto de diseño, y los resultados por clase se
  informan como casos.»
  - **Los elegibles** son los 6 de la §1, más el sucesor de ri_oc si es elegible. Las unidades son las de la E0 corregida.
  - **Desde qué N llegan los topes** (`data/experiment/esq/elegibles_B63_O2_2026-10-15/reparto_rama_caida_mesa.py`, con su salida en
    `reparto_rama_caida.txt`): con los 6, régimen informativo llega a la suma de sus topes, 54 preguntas, con N > 108. Las otras dos
    clases llegan con N > 1.224 y con N > 280. Con el sucesor, el script se corre con `--sumar <id>`.
  - **Lo que la regla no dice** (PENDIENTE de la autora, antes de cualquier lectura): qué pasa cuando una clase llega a sus topes y las
    otras no. Con N = 125, uno de los N de la salida, hay tres lecturas:
    1. esa clase queda en sus topes y las otras siguen con su parte: el total baja a 116,5;
    2. el total baja hasta conservar 50 / 25 / 25: a 108;
    3. lo que falta pasa a las otras clases y el N se conserva: 125, con régimen informativo por debajo del 50 %.
  - El redondeo de las preguntas por documento se fija con la propuesta del N.
- **El re-censo de la release de E0 (§4):** no demora la tanda 1, y va en S2 como tramo 3 (nota del 15/10/2026 al pie de
  `docs/mandatos/USEG_OFICIAL_segmentacion_e0r2.md`).
- Las secciones anteriores no se editan.

## 6. B6.3 y el carril de la evaluación (agregado del 15/10/2026)

Las decisiones llegaron en el mensaje recibido a las 14:42:39 (hoja de ruta de la mesa, §105).

- **El reparto en la rama de caída: la lectura 3, tal cual:** «Cuando una clase llega a sus topes, lo que le falta pasa a las otras
  clases, en proporción a sus partes, y el N se conserva. El total baja solo cuando todas las clases llegaron a sus topes. Las
  proporciones que no se cumplan se declaran.»
  - Resuelve lo que la regla de la §5 no decía.
- **A2.1, tal cual:** «A2.1 arranca ya. Redactá su mandato, sin demorar nada del camino a la tanda 1.»
  - El mandato lo redacta la mesa, y la autora lo firma.
- **A2.2, tal cual:** «buscá en el registro del 07/10 por qué D1 la pone después de la tanda 1. Si no depende de nada de la tanda 1,
  corre apenas se selle A2.1. Si depende, decime de qué y decido.»
  - **Lo que encontró la mesa:**
    - el registro del 07/10/2026 da la razón de que vaya antes de las ablaciones de A1.8: «para que lo que muestre entre como insumo de
      la navegación» (`docs/plan_tesis.md:331`). No da ninguna para que vaya después de la tanda 1;
    - el grafo del brazo del grafo de A2 es el de desarrollo r2b (D5, `:339`);
    - la restricción ligada a la tanda 1 es la de A1.8: el agente queda fijo durante la tanda 1 (decisión del 01/10/2026, `:331`). A2.2
      no cambia el agente.
  - **Con eso, A2.2 corre apenas se selle A2.1.** Depende de qué versión del grafo de desarrollo fije el mandato de A2.1. Con la
    re-sellada, depende también del re-sellado único de la tanda 0.
- **La aprobación de las preguntas, tal cual:** «Sí a empezar la aprobación de las preguntas antes del N, con un orden sorteado y
  sellado antes de aprobar ninguna, que sirva para las dos formas de repartir el N (más documentos o más preguntas por documento).»
  - El diseño lo propone la mesa, y la autora lo decide antes de sortear.
- Las secciones anteriores no se editan.

## 7. El orden de las preguntas y el grafo corregido (agregado del 15/10/2026)

Las decisiones llegaron en el mensaje recibido a las 15:16:05 (hoja de ruta de la mesa, §106).

- **El orden para aprobar las preguntas, tal cual:** «sí a los puntos 1 a 5, tal como los proponés. Para el 6, proponeme la regla de qué
  unidad puede ser ancla, por escrito, con cuántas unidades deja afuera por clase. No sortees hasta que la decida.»
  - **Los cinco puntos,** del diseño de la mesa (en su paquete: `decisiones_105_mesa/preguntas/diseno_orden_aprobacion_preguntas_B63_mesa.md`,
    sha256 `79b82c3b…`):
    1. dos sorteos con semilla: los documentos por clase y las unidades por documento, como en EV2;
    2. el de documentos, estratificado por tanda, con los de la tanda 1 primero, como pide la regla de caída (punto 2);
    3. un orden aparte por tipo de pregunta, mientras las cuotas sigan abiertas;
    4. un núcleo de 64 preguntas, con las 4 primeras de cada uno de los 16 documentos de O2, y después olas alternadas de 16 (más
       documentos, o más preguntas por documento);
    5. las reglas de rechazo (la unidad siguiente del orden) y de documento agotado (lo que falta pasa al siguiente de su clase).
  - El punto 6 lo decide la autora antes de sortear.
- **El grafo corregido, tal cual:** «ri2_pm y las planillas de los nueve van ahí. L-01 va ahí si no entra al grafo evaluado, y eso lo
  decido al leer su mandato.»
  - Va también rdbcra, por su cobertura no exacta en la E0 corregida (nota del 15/10/2026 al pie de
    `docs/mandatos/USEG_OFICIAL_segmentacion_e0r2.md`).
- Las secciones anteriores no se editan.

## 8. La tanda 1, la regla del ancla, Q4, Q12 y el conteo de ri_spi y ri_con (agregado del 15/10/2026)

Las decisiones llegaron en dos mensajes, recibidos a las 15:54:12 y a las 15:59:03 (hoja de ruta de la mesa, §107).

- **El health-check de E0 de la tanda 1 (15:54:12), tal cual, decidido antes de ver el FRENO S2-b:** «las señales que no son cobertura ni
  ids repetidos (cid, páginas sin sección, unidades grandes) se registran y se declaran por TO, como en la tanda 0, y no excluyen. La
  cobertura no exacta y los ids repetidos frenan, como dice el «seguí».»
  - El precedente de la tanda 0 está en `docs/preregistro_tanda0.md:212-216`.
- **La regla del ancla (15:54:12), tal cual:** «sin mini_chunk y con al menos 60 caracteres de texto propio. Las tabulares y las de fórmula
  quedan, declaradas.»
  - Con esto queda decidido el punto 6, y con él el diseño del orden entero (§7).
- **Q4 y Q12 (15:59:03):** «Q4 y Q12 los decido yo, con lo que acordamos con los mentores al diseñar la evaluación (reuniones del 18 y el
  19/08). No los consulto ahora.»
  - **Q4, tal cual:** «preguntas de varios puntos, con una cuota por clase según lo que permita cada una, fijada antes de generar ninguna
    pregunta y con su regla escrita. Se informan aparte de las de dato directo. Sin preguntas de abstención: se declara como límite.»
    - La cuota de cada clase la decide la autora con los datos, antes de sortear.
  - **Q12, tal cual:** «el juez hace el grueso. Yo armo primero un gold propio, a ciegas, sin ver ninguna sugerencia de un modelo, y el juez
    se calibra contra ese gold antes de usarlo. Después leo lo que el juez deja dudoso y una muestra de control de tamaño fijado antes. Sin
    experto del dominio: lo que necesite uno se marca y se declara. En las tripletas rige su pre-registro firmado; si deja abierto quién
    adjudica algo, aplicá este mismo criterio.»
    - Los tamaños del gold y de la muestra los decide la autora.
    - Lo que el pre-registro de las tripletas deja abierto sobre quién adjudica (§6.4) va en una nota al pie de ese pre-registro.
- **ri_spi y ri_con (15:54:12), tal cual:** «confirmo la regla.»
  - La regla es la que propuso la autora: se cuentan una sola vez, por su razón vigente con la E0 corregida (las decisiones 1 y 2 de la
    enmienda 8), con una nota que dice que en la partición legada eran no segmentables.
  - Van notas al pie de la enmienda 8 y del protocolo entre tandas.
  - En la §1 de este registro, la capa «los no segmentables» son los otros 10. Sus cifras no cambian.
- **A2.1 (15:54:12), tal cual:** «Firmo el mandato de A2.1 (b311859c…) tal como está.» Está en
  `docs/mandatos/A2_1_sistema_por_fragmentos_preregistro_A2_2.md`.
- **Las ejecutoras en el repo (15:54:12), tal cual:** «S2, el re-sellado, A2.1 y B1 de B′ escriben en el repo. Armá el orden para que
  corra una sola por vez, con los commits entre una y otra».
  - El orden lo propone la mesa.
- Las secciones anteriores no se editan.

## 9. Q4, Q12, el orden de las ejecutoras y el re-sellado (agregado del 15/10/2026)

Las decisiones llegaron en el mensaje recibido a las 16:17:35 (hoja de ruta de la mesa, §108).

- **El orden de las ejecutoras, tal cual:** «aprobado, con B1 después de la tanda 1. Una condición: nada demora el despacho de la tanda 1.
  Si cuando estén firmados el laudo y el v8 todavía corren el tramo 3 de S2 o A2.1, la tanda 1 va primero y ellos siguen después.»
  - El orden, en el paquete de la mesa: `decisiones_108_mesa/orden/orden_ejecutoras_en_el_repo_v2_mesa.md`.
- **Q4, la cuota, tal cual:** «la cuota que proponés (10 %, 15 % y 15 %, dentro del N), que sigue la proporción real de unidades con
  remisión de cada clase. Las de varios puntos se informan aparte, como análisis descriptivo. Si los documentos sorteados de una clase no
  tienen candidatas suficientes, lo que falta va como preguntas de dato directo de esos mismos documentos, y se declara.»
  - **La regla de la cuota:** la proporción de unidades ancla de la clase con al menos una remisión interna resoluble, redondeada hacia
    abajo a un múltiplo de 5 %.
  - **De dónde sale:** el detector de B1.3 (`data/experiment/reextraccion_v2/corpus_v2/r1_referencias.py`, `detectar_menciones`), sobre la
    E0 corregida. Da 39 de 372 en régimen informativo, 296 de 1.920 en «digerible» y 93 de 535 en «necesita reglas» (paquete de la mesa,
    `decisiones_107_mesa/preguntas/`).
- **Q12, tal cual:**
  - «El gold: 40 respuestas, en dos mitades. Las 20 para ajustar el juez salen de respuestas de EV2 que ya existen, y las leo este fin de
    semana. Las 20 para verificarlo salen de las respuestas de A2.2 y sirven también como su muestra simétrica. Las leo a ciegas, antes de
    ver cualquier veredicto.»
  - «El criterio de aceptación, como lo proponés: en la mitad de verificación, Wilson inferior de al menos 0,85 por criterio y al menos 18
    de 20 por respuesta. Si no se cumple, frenás y decido.»
  - «Lo dudoso de B6.3, todo para mí. La muestra de control: 36 respuestas, 12 por brazo, estratificadas por clase, con semilla fijada
    antes.»
  - **Cómo se puede** (mesa): el juez se congela antes de firmar el pre-registro de A2.2, y ese pre-registro toma como su muestra
    simétrica las 20 de verificación. Va en una nota al pie de `docs/mandatos/A2_1_sistema_por_fragmentos_preregistro_A2_2.md`.
- **El re-sellado, tal cual:** «tomo las cuatro decisiones del §8 del v3. 1. Los nombres: los de U-SINCOLA-T0 con el sufijo _rs1. 2. Se
  re-sellan los cuatro grafos, completos y sin cola. 3. Si el diff contra O2 trae algo que no viene de R0, frena. 4. Las notas a los
  documentos firmados van en un commit propio, inmediatamente después de los dos del sello.»
  - El mandato, en su versión para firmar, está en el paquete de la mesa (`decisiones_108_mesa/resellado/`).
- Las secciones anteriores no se editan.

## 10. El alcance de dos documentos de la tanda 1, el conteo fijado, el S2-b y U-MED-VERIF (agregado del 15/10/2026)

Decisiones de la autora recibidas a las 18:34:38 (hoja de ruta de la mesa, §111), y las de U-MED-VERIF recibidas a las 17:45:44 (§110).

- **depaho, tal cual:** «tu (i) más tu (ii). El rol queda como está en la tanda 1, declarado en el v8. B1 mide, al lado de la regla
  firmada, la variante que deriva solo dentro de la sección del pasaje del alcance, y lo decido en B2 con la cifra. El alcance por
  sección entra a la lista del grafo corregido como corrección general para todos los roles, no solo para depaho.»
  - **Por qué:** el rol de depaho sale de las entidades intervinientes de la sección 1 (`depaho::1.1.1` a `::1.1.4`, p. 5). Las
    secciones 2 y 3 nombran otros conjuntos (`depaho::2.1`, p. 14; las aperturas de la sección 3, como `depaho::3.1.1`, p. 21).
    Las cifras por sección están en el paquete de la mesa (`decisiones_110_mesa/depaho/` y `decisiones_111_mesa/depaho/`).
  - **Cambiarlo ahora demoraba la tanda 1:** el registro no alcanza, porque E1 lee primero la tabla de la release y el lector saltea
    las filas sin alcance.
  - **Al grafo corregido:** el alcance por sección, como corrección general de todos los roles de alcance. Hoy no tiene formato en el
    registro ni en la tabla de la release.
  - **La nota al mandato de B′** (`docs/mandatos/UAPLICA_ROL_ALCANCE_derivada_Bprima.md`) con la variante que mide B1 va después del
    commit de las notas del re-sellado, que también anota ese mandato.
- **Otro documento con el mismo caso** (pedido de la autora, tal cual: «Si hay alguno, va al v8 como depaho, sin cambiar nada»): snp_tr.
  - Su rol sale de «Entidades alcanzadas por el servicio» (`snp_tr::1.1.3`, p. 5), en la sección 1, de transferencias en lote.
  - Las secciones 2 y 3 son otros servicios, con sus propios participantes (`snp_tr::2.3.1`, p. 50; `snp_tr::3.2.2.1`, p. 53).
  - En los otros 16 documentos de la tanda 1 con alcance, el pasaje vale para todo el documento o el rol es el del régimen informativo
    (regla §2.8 del registro de alcance). Las aperturas de cada sección, contadas, están en el paquete de la mesa
    (`decisiones_111_mesa/secciones/`).
- **El conteo fijado antes de la tanda 1, tal cual:** «Fijá ahora, antes de la tanda 1, un conteo por script para después de la tanda
  1: cuántas normas de depaho, por sección, salen con aplica_a hacia Sujeto_rol_alcance_depaho. Es una cuenta de aristas, no una
  lectura. El v8 cita el script sellado.»
  - El script: `data/experiment/controles_tanda1/conteo_aplica_a_rol_por_seccion.py` (sha256 `d8c1e06a3762579c502e8f303e13ba065e2f85f66d9e12bd2d5afd63cca79f34`).
  - Su selftest, sintético: 9 de 9 (`selftest_conteo_aplica_a_rol_por_seccion.py`, con su salida al lado). Un mutante que cuenta
    las operaciones como normas falla 5 de los 9.
  - Corre sobre el `kg.json` del grafo de la tanda 1 sellado, con los pares `depaho:Sujeto_rol_alcance_depaho` y
    `snp_tr:Sujeto_rol_alcance_snp_tr_nc`. No imprime texto, y no separa las unidades por su estado en E3.
- **La fila de ri_oc, tal cual:** «La fila de ri_oc queda en el registro de alcance como está.» El lector saltea las filas «sin alcance
  declarado», así que no tiene efecto.
- **El S2-b, tal cual:** «El S2-b queda aceptado. En el tramo 3, censo_sd_152_S2b.json se controla por su JSON con las claves
  ordenadas, como propusiste, y eso queda declarado en el repo con el commit del tramo 3.»
- **U-MED-VERIF**, la medición de lo que cambia cuando el verificador pide una nueva extracción y la acepta. Su diseño todavía no está
  sellado y no está en el repo.
  - Tal cual, a las 17:45:44:
    - «Va a la hoja de ruta, pero no puede demorar el despacho de la tanda 1. Si algo de esto compite con la tanda 1, gana la tanda 1, y
      me lo decís.»
    - «Hasta que yo selle el diseño, nadie mira las re-extracciones de la tanda 1, ni sus conteos ni sus marcas de copia. Eso incluye
      tus revisiones de los FRENOs de la tanda 1 y los informes de su ejecutora.»
  - Tal cual, a las 18:34:38: «tu respuesta va a la mesa de escritura y vuelve como versión final para que la selle. La cláusula de
    cegamiento va en el v8 y en el despacho de la tanda 1 aunque llegue a sellar el diseño antes.»
- Las secciones anteriores no se editan.

## 11. El alcance por sección en el v8, el piso de espacio de la tanda 1 y lo que dejó abierto el re-sellado (agregado del 15/10/2026)

Decisiones de la autora recibidas a las 19:02:53, 19:27:15 y 19:33:19 (hoja de ruta de la mesa, §112 y §113).

- **Las cifras del v8, en el repo** (19:02:53, tal cual): «Las cifras de depaho y de snp_tr que van al v8 tienen que tener artefacto en el
  repo: medir_por_seccion_Bprima_mesa.py y sus dos JSON entran con el commit del v8, y el v8 los cita desde ahí, no desde el paquete.» Van
  a `data/experiment/controles_tanda1/`, al lado del conteo fijado.
- **El piso de espacio de la tanda 1** (19:02:53, tal cual): «El despacho de la tanda 1 controla en su paso 0 el espacio libre, con un piso
  que fijás con tu estimación y un margen, y frena si no llega.» El piso es de 30 GB libres: los 14 GB del máximo de la estimación, que es
  NO VERIFICADA, más un margen de 16. Se controla con `df -k` en el paso 0 y antes de la corrida real.
- **snp_tr en el v8** (19:27:15, tal cual): «snp_tr: queda con su rol por decisión de la autora del 15/10/2026, como depaho. Su rol viene
  del registro de alcance, no de la release. Queda porque es correcto en la sección 1, que tiene la mitad de sus unidades, y sacarlo deja
  a E1 sin sugerencia también ahí. Se corrige con el mismo alcance por sección en el grafo corregido.» La sección 1 tiene 51 de sus 103
  unidades (50 y un bloque que hereda su título).
- **cirmo3 en el v8** (19:27:15): la autora pidió decidirlo con la evidencia. La mesa lo decidió así: su pasaje no da un alcance correcto
  para ninguna sección entera, y esa es la diferencia con depaho y snp_tr.
  - **El pasaje** (`data/experiment/catalogo_unico/registro_alcance_por_tanda.md:28`; `cirmo3::4.1::intro`, p. 30) nombra tres clases
    (entidades financieras, agencias de cambio y casas de cambio) y el rol de otro documento (las transportadoras de valores,
    `Sujeto_rol_alcance_traval`).
  - **Por qué no alcanza:** el registro admite una o dos clases, y un rol reutilizado solo entre secciones de un mismo régimen
    (`registro_alcance_por_tanda.md:6-12`). Además, el pasaje es del punto 4.1, y la sección 4 tiene también el 4.2.
  - **Las otras secciones abren con otros conjuntos:** los bancos y el BCRA en la 1 y la 6; los bancos y los clientes en la 3; las
    entidades financieras con las transportadoras de valores en la 5 (`cirmo3::5.1.1`, p. 33); el BCRA en la 7; y ninguno en la 2 y la 8.
  - **depaho y snp_tr,** en cambio, tienen un rol del catálogo correcto en su sección 1 entera.
- **Las filas de alcance de la tanda final** (19:27:15, tal cual): «Cuando armes las filas de alcance de la tanda final, controlás en cada
  documento lo mismo que en la §111 (las aperturas de cada sección contra el pasaje del alcance) y lo declarás como depaho y snp_tr, sin
  cambiar nada.»
- **Lo que dejó abierto el re-sellado** (19:33:19, tal cual):
  1. «F49: la cifra de U-CONF-MATRIZ no se recalcula. Se declara que se midió sobre el grafo sellado, que en el re-sellado 59 de las 60
     aristas leídas siguen con los mismos extremos, y que F49 cambió porque su unidad se re-extrajo en R0.» La nota va al pie del mandato de
     U-CONF-MATRIZ.
  2. «R2-3 como tercera causa del diff contra los sellados queda declarada como la declaró la ejecutora, si tu revisión confirma que son
     las mismas 11 filas que dejó O1 de ese paso.»
     - La revisión lo confirma en los dos grafos de diez: las 10 filas que entran o salen son las de
       `data/experiment/omisiones_cod/o1/salidas/diff_a9631a64_vs_head_diez.json`, y el nodo que cambia cambia los mismos 5 campos de
       procedencia.
  3. «Los nombres de la suite con -rs1 quedan como están.»
  4. «Las rutas con el nombre de la cuenta en los reportes de los generadores quedan como salieron, sin editarlas a mano, y se declaran.»
  5. «La nota de insumos_escritura.md §7, que no estaba en las escrituras de la ejecutora, la agregás vos en el commit de las notas, con
     el formato de las otras.»
  6. «Los cuatro sha nuevos van al «A COMPLETAR» del laudo de la release cuando me lo pases para firmar.» PENDIENTE: va con el laudo.
- Las secciones anteriores no se editan.

## 12. A2 confirmado, la revisión entre tandas, la tanda final en dos tramos y las horas de la autora (agregado del 15/10/2026)

Decisiones de la autora recibidas a las 21:05:39 y a las 23:23:47 (hoja de ruta de la mesa, §115 y §116).

- **La nota de B′** (21:05:39, tal cual): «La nota de B′ queda como la escribiste: B1 mide la variante en depaho y en snp_tr.» La nota está al
  pie de `docs/mandatos/UAPLICA_ROL_ALCANCE_derivada_Bprima.md` (`06b01b90`).
- **La condición 4 y el gate final del laudo** (21:05:39, tal cual): «La condición 4 y el gate final del laudo los hacés vos, sobre copias,
  sin turno en el repo. Dejá el script del gate, su salida y su sha256 en el paquete: antes de firmar el laudo los reviso.»
- **Los tres valores de A2** (23:23:47, tal cual): «Los tres valores de A2 quedan confirmados: e06933e7… (el derivado), 6b758517… (el
  candado) y eeb11b9a… (el mensaje de la fixture).»
  - Están en `data/experiment/reextraccion_v2/e1_extractor/prompt_r2b.py` desde `42823df0`.
  - La mesa los reprodujo sobre una copia (hoja §115).
- **La corrida en seco de la tanda 1** (23:23:47, tal cual): «La corrida en seco de la tanda 1 es T1 de su despacho.»
  - Cierra el pendiente 6 del pre-registro de la tanda 1.
  - El manifiesto de la tanda 1 se arma en T1, después de A2, y se carga con su validación antes de la corrida en seco. T2 no arranca sin
    que la autora revise el FRENO T1.
- **El costo de A2 en la tanda 1** (23:23:47, tal cual): «El costo de A2 en la tanda 1 (USD 0,19) se declara en el v8, dentro del margen,
  sin cambiar el tope.»
  - Son USD 0,190841: 190.841 tokens de entrada de E1, en las 1.029 unidades con línea de alcance
    (`data/experiment/alcance_e1/a2/freno_a2.md:68-84`).
- **La revisión entre la tanda 1 y la tanda final** (23:23:47, tal cual): «La revisión entre tandas (11a) va como la propusiste, con un
  cambio. El health-check controla solo la cobertura y los ids, así que no detecta un error de corte. Si la tanda 1 confirma un error de
  corte con un rasgo, los documentos de la tanda final se miden con un detector de ese rasgo, escrito como regla general y corrido sobre los
  98 antes del manifiesto, como el detector de 1.16 o el censo de sub-documentos. Antes de leer la tanda 1, proponeme qué pasa con los que
  den positivo (salir, declararse como riesgo o confirmarse con una lectura corta), con su costo. Si para un rasgo no se puede escribir y
  probar un detector antes del despacho, se declara como riesgo.»
  - La propuesta 11a está en el paquete de la mesa (`decisiones_115_mesa/escalado/escalado_hasta_el_sello_mesa.md`): qué se mide, las
    muestras de reparto igual por clase con un tercio de sin_raiz, y las tres salidas.
  - Va al pre-registro de la tanda 1 (v8).
- **La tanda final en dos tramos** (23:23:47, tal cual): «Los dos tramos de la tanda final (11b) van como los propusiste, con un cambio en
  los umbrales. El tramo 1 son regímenes informativos y sin_raiz, así que la proporción a la cola y el costo por unidad se comparan con los
  de las mismas clases en la tanda 1 (sus regímenes informativos y sus unidades sin_raiz), no con la tanda 1 entera. Los multiplicadores
  (1,3 y 1,5), el 1 % de salidas inválidas y los 0 errores quedan como los propusiste. Si alguna de esas clases tiene en la tanda 1 muy
  pocas unidades para dar una base estable, proponeme cómo resolverlo antes de leer la tanda 1.»
  - El tramo 1 tiene 30 documentos y 601 unidades, y el tramo 2, 68 y 4.350 (paquete de la mesa,
    `decisiones_115_mesa/escalado/tramos_tanda_final_mesa.json`).
  - Va al pre-registro de la tanda final.
- **T3 sobre el tramo 1** (23:23:47, tal cual): «T3 sobre el tramo 1 (11d): sí, si la corrida en seco de la tanda final prueba que el
  ensamblado de un subconjunto funciona. Si no, no se hace.»
- **Las horas de la autora** (23:23:47, tal cual): «Mis horas (11c): este fin de semana, después de las 20 del gold, empiezo la calibración
  del juez. Entre sumar horas y achicar el N decido el lunes 19 a la noche, con las tasas de A2.2 y el N que dé la potencia.»
- Las secciones anteriores no se editan.

## 13. Los positivos del detector, la regla de reemplazo de las preguntas y las bases del control entre tramos (agregado del 15/10/2026)

Decisiones de la autora recibidas a las 23:52:00 (hoja de ruta de la mesa, §117). Responden a las propuestas de la §116 (paquete de la mesa,
`decisiones_116_mesa/escalado/propuestas_detector_y_bases_antes_de_leer_la_tanda_1_mesa.md`).

- **Los positivos del detector** (tal cual): «Los positivos del detector no van con la lectura asistida (c′). La mesa diseña el detector,
  así que no lee sus resultados, y ningún modelo aplica el criterio a un corte. Va la (c): leo yo, con la regla de lectura, el tope de 30
  cortes y la semilla fijados antes de leer la tanda 1. El tope se reparte primero con un corte por documento, en el orden de la semilla, y
  si sobra, un segundo corte en los documentos con más positivos. Si un corte se confirma, el documento sale, declarado. Los que quedan
  fuera del tope no salen y se declaran como riesgo, porque sale solo lo confirmado.»
- **La regla de reemplazo de las preguntas de B6.3** (tal cual): «La regla de reemplazo de las preguntas de B6.3 va como la propusiste,
  con el documento siguiente de la misma clase en el orden del sorteo. Ponela en el mandato de la generación de preguntas antes de sellar
  el sorteo.»
  - Va en el mandato de la generación de preguntas, que todavía no está escrito, antes de sellar el sorteo.
- **Las bases del control entre tramos** (tal cual): «Las bases del control entre tramos van como las propusiste: una sola base con las
  548 unidades RI o sin_raiz de la tanda 1, el límite superior de Wilson si tiene menos de 10 en la cola, y el costo ponderado por la
  composición del tramo 1. La alternativa no va.»
- **Las fechas de `.git` durante A2** (tal cual): «Lo de .git se cierra como lo propusiste: renovación de fecha de objetos existentes, sin
  cambio de contenido, mecanismo no identificado.»
  - La evidencia está en el paquete de la mesa (`decisiones_116_mesa/git/`): `git fsck` y `git verify-pack` limpios.
- **Los tests finales de A2.1** (tal cual): «Los tests finales de A2.1 sobre una copia nueva, como en A2, de acuerdo. El FRENO lo declara como
  diferencia con el mandato.»
  - Es la regla d de CLAUDE.md: el mandato dice «con los tests corridos de nuevo en el repo», y CLAUDE.md §4.l pide que los selftests
    corran sobre una copia.
- Las secciones anteriores no se editan.

## 14. Sub-documento en la tanda 1, la señal cid y las salidas crudas de la segmentación (agregado del 16/10/2026)

Decisiones de la autora recibidas el 16/10/2026 a las 00:43:53 (hoja de ruta de la mesa, §118). Responden a los pedidos 9, 11 y 12 de la
§117 (paquete de la mesa, `decisiones_117_mesa/escalado/pedidos_8_a_12_antes_de_leer_la_tanda_1_mesa.md`).

- **Los límites de sub-documento de la tanda 1** (tal cual): «Sub-documento: la (a), como la propusiste. Leo los 14 de la tanda 1, con la
  regla de lectura de S1-bis, el sábado 17 o el domingo 18, mientras corre T2. Con un error de corte confirmado, el rasgo queda confirmado y
  los 33 de la tanda final van por la regla de la decisión 1. Preparame las fichas y decime cuándo están.»
  - Las fichas, la planilla vacía y las páginas están en el paquete de la mesa (`decisiones_118_mesa/lectura_subdocumento_tanda1/`), con
    su manifiesto. Salen de la E0 corregida y del censo de sub-documentos de la segmentación, sin ninguna marca.
- **La señal cid** (tal cual): «cid: como lo propusiste. El conteo por script va después de T5. Leo solo las unidades que lleguen al grafo
  con «(cid:», hasta 15, y después se hace lo mismo con las 3 de la tanda final. El límite que no se mide se declara.»
  - El límite que no se mide: si la señal hizo perder caracteres sin dejar `(cid:N)` en el texto.
- **Las salidas crudas de la segmentación** (tal cual): «Las salidas crudas de S2 quedan sin resguardo. Se regeneran cuando hagan falta.»
- **1.16 en la tanda final: abierto.** La autora decide entre declararlo y una lectura corta escalonada, después de ver la historia de 1.16
  con su fuente en cada paso (paquete de la mesa, `decisiones_118_mesa/historia_116/`).
- Las secciones anteriores no se editan.

## 15. La lectura corta de 1.16 en la tanda final, el tope por rasgo y el venv del servidor vectorial (agregado del 16/10/2026)

Decisiones de la autora recibidas el 16/10/2026 a las 08:15:55 (hoja de ruta de la mesa, §119). Responden a la propuesta de la §118
(paquete de la mesa, `decisiones_118_mesa/historia_116/historia_de_1_16_y_lectura_corta_mesa.md`).

- **1.16 en la tanda final** (tal cual): «1.16: va la lectura corta escalonada, con la regla que propusiste: la población de los 28
  documentos con candidatos sin leer, el orden y el corte de cada documento por semilla, el primer tramo de 10, la rama 0 y la rama 1, y el
  criterio de la lectura de cortes de S1. Sellá el orden y los cortes antes de armar las fichas. Armame las fichas de los 30 cortes del
  orden, no solo de los 10 primeros, para que la rama 1 no tenga que esperar. Leo el sábado 17 o el domingo 18, mientras corre T2.»
  - El orden y los cortes quedaron sellados el 16/10/2026 a las 08:19:19, antes de armar las fichas
    (`orden_y_cortes_116_tanda_final.json`, sha256 `3db5328f7fba7f79cd09e29bd468fb58ec25d054599c2530819e42c6f8764287`, en el paquete de
    la mesa, `decisiones_119_mesa/lectura_116_tanda_final/sello/`). Dan lo mismo con Python 3.10.13 y con 3.12.13.
  - Lo que la regla aprobada no escribía, fijado por la mesa antes del sello: el segundo corte de un documento sale de
    `random.Random(f"U-SEG-OFICIAL:1_16:tanda_final:{doc}:2")`, entre sus candidatos sin leer menos el primero.
  - Las fichas de los 30 cortes salen de la E0 corregida y del PDF, sin ninguna marca.
- **El tope de cortes** (tal cual): «El tope de 30 de la decisión 1 es por rasgo, no total.»
  - Para sub-documento en la tanda final, si los 14 de la tanda 1 confirman el rasgo: 30 cortes de sus 33 límites, en 18 documentos. El
    orden propuesto por la mesa quedó sellado el 16/10/2026 a las 08:20:10 (`orden_subdocumento_tanda_final.json`, sha256
    `a5aa300852f999679bf7d19dee3a129a7f988edf2c4ca56b0e95bd7afa9752d4`), antes de que exista ninguna salida de la tanda 1. Si la autora
    prefiere otra semilla, se rehace y se sella antes de que lea la tanda 1.
- **El venv del servidor vectorial,** que borró el limpiador de `/private/tmp`, se rearma fuera de él:
  - en `~/INGENIERIA IA/TESIS/venvs/banco_vector_py312`, con Python 3.12.13 de miniforge y exactamente `requirements_vector.txt`;
  - el modelo se carga desde la caché local, sin conexión;
  - si el índice viejo no da `12d284d5…`, A2.1 frena sin probar otras versiones;
  - su FRENO declara el `pip freeze` y el intérprete de cada script, también los del tramo 2.
- Las secciones anteriores no se editan.

## 16. La semilla de sub-documento, las ruedas del servidor vectorial, lo que vive fuera de /private/tmp, las seis decisiones de A2.1 y su etapa corta (agregado del 16/10/2026)

Decisiones de la autora recibidas el 16/10/2026 a las 08:47:38 (hoja de ruta de la mesa, §120) y a las 10:37:59 (§122). Las de las
10:37:59 responden a la revisión del FRENO A2.1-a (paquete de la mesa, `decisiones_121_mesa/`).

- **La semilla de sub-documento de la tanda final** (tal cual): «La semilla del orden de sub-documento de la tanda final queda como la
  sellaste (a5aa3008…).» Cierra lo que la §15 dejaba abierto: el orden sellado a las 08:20:10 rige tal como está.
- **Las ruedas del servidor vectorial** (tal cual): «Las ruedas y el pip freeze del venv nuevo: cuando frene A2.1, copialos a
  ~/INGENIERIA IA/TESIS/venvs/ruedas_banco_vector_py312/ con su sha256_ruedas.txt, verificá la copia contra esos sha256 y no borres nada
  del scratchpad de A2.1.»
  - Lo hizo la mesa el 16/10/2026 a las 09:51:45: las 62 ruedas, `sha256_ruedas.txt` y el `pip freeze`. La copia da 62 de 62 contra
    `sha256_ruedas.txt` (paquete de la mesa, `decisiones_121_mesa/revision/`).
- **Lo que vive fuera de /private/tmp** (tal cual): «La regla queda aprobada: lo que una etapa necesita después de su sesión va al repo,
  al paquete permanente o a ~/INGENIERIA IA/TESIS/, nunca a /private/tmp. Va en todos los despachos que vienen.»
- **Las seis decisiones abiertas de A2.1** (tal cual): «Las seis decisiones de la §14 de A2.1 quedan como están, como recomendaste. En la
  4 cambio mi inclinación: el plan quiere el BM25 como el rival más fuerte en lo literal (plan_tesis.md:339), y la Q2 permite declarar la
  diferencia. La asimetría con el grafo se declara en el pre-registro de A2.2, con tus cifras.»
  - **Las seis, como quedan** (FRENO A2.1-a, `data/experiment/banco_mcp/a2_1/FRENO_A2_1_a.md`, §2, §4 y §13):
    1. el servidor MCP se llama `fragmentos` en los dos brazos;
    2. la descripción de la tool nombra la medida;
    3. `limite` dice «(def. 5, máx. 5)»;
    4. la consulta del BM25 pasa por el mismo analizador que los documentos, sin la pre-tokenización del brazo del grafo;
    5. la norma de largo está cuantizada como en Lucene;
    6. el stream de init del aislamiento queda fuera del repo.
  - **Las cifras de la 4:** `data/experiment/controles_a2_2/consulta_pre_tokenizada_bm25_mesa.json`, de
    `medir_consulta_pre_tokenizada_bm25_mesa.py`, en la misma carpeta. Corren sobre el índice BM25 `6b5da8b0…`, fuera de git, que el
    script controla. Con la pre-tokenización del grafo:
    - 1.846 de los 8.378 términos del índice no saldrían de ninguna consulta: 111 llevan tilde o eñe y 1.735 son números con separador;
    - 1.763 de los 1.768 pasajes tienen al menos uno.
- **La etapa corta de A2.1** (tal cual): «La etapa corta de A2.1 va, a USD 0: que el test escriba sus logs con un nombre propio por corrida,
  que explique cómo corrió su copia final sin los logs viejos y que lleve a su paquete las siete salidas del aislamiento que faltan. Va
  el domingo 18 después de T5, antes del «seguí» del tramo 2. Armame su «seguí» para leerlo antes de pegarlo, y sumá al del tramo 2 tu
  nota sobre H-B2.»
- **Los índices en A2.2** (tal cual): «El despacho de A2.2 controla al empezar los sha de los índices de mcp_vector/indice/.»
  - Los dos índices nuevos quedan en el repo, fuera de git, como el viejo (`data/experiment/banco_mcp/.gitignore:10`).
  - Los dos logs de los tests del tramo 1 también quedan fuera de git (`:7`); el JSON de los tests guarda su sha256. El commit del
    tramo 1 (`5f0f29b5`) no los lleva.
- Las secciones anteriores no se editan.

## 17. El laudo de la release y el pre-registro de la tanda 1, firmados (agregado del 16/10/2026)

Decisiones de la autora recibidas el 16/10/2026 a las 11:14:51 (hoja de ruta de la mesa, §123), a las 11:53:36 (§124) y a las 12:05:12
(§125).

- **El laudo de la release r2** (tal cual): «Firmo el laudo de la release r2 (907b9a5a…) tal como está.» La firma está en el commit
  `94087a7f`, sobre la versión para firmar de `639f0498`.
- **El pre-registro de la tanda 1** no se firma todavía. La autora pidió una segunda versión para firmar del v8 «con estos cambios y nada
  más»:
  1. **El código del despacho** (tal cual): «Sellá la lista: las rutas del código de la cadena (E0, E1 a E3, el runner, el ensamblado,
     los validadores, los perfiles, shapes y la suite), con el sha256 de cada una en 47c9f1b3, calculado con git show, en un archivo que
     entre al repo con el pre-registro. El v8 lo cita y el despacho lo usa en su paso 0.»
     - Quedó en `data/experiment/controles_tanda1/codigo_de_la_cadena_47c9f1b3_mesa.json`: 78 rutas, iguales en HEAD.
  2. **Sub-documento en la tanda 1** (tal cual): «si confirmo un error de corte en uno de los 14 límites de la tanda 1, ese documento sale
     del grafo evaluado al sellarlo, declarado. El grafo de la tanda 1 se sella como corrió (D3). Es el mismo criterio que con ri_oc y con
     la tanda final. Si sale un documento con preguntas de B6.3, rige la regla de reemplazo.»
  3. **Las muestras de T4** (tal cual): «en cada muestra de 30: RI, 10 sin_raiz y 5 del resto; NG, 5 sin_raiz y 10 del resto; en las
     aceptadas, lo mismo en cada estrato (ítems y no ítems): 30 por estrato, 30 RI y 30 NG en total; si una celda tiene menos unidades que
     su cuota, entran todas y lo que falta sale de la otra celda de la misma clase, declarado; cada celda tiene su propia semilla; las
     tasas se ponderan por las unidades de cada celda, no solo por clase.»
     - La atención, el freno y el intervalo con este reparto, calculados por script:
       `data/experiment/controles_tanda1/umbrales_t4_por_celdas_mesa.json`.
  4. **La semilla** (tal cual): «Que la base sea el sha256 de la versión para firmar que entra con su commit. La versión firmada lo nombra
     y deja anotadas las cadenas de semilla de cada celda, como en U-CONF-MATRIZ.»
  5. **Las tablas forzadas a residual** (tal cual): «La PROPUESTA DE LA MESA del §7 (ninguna alta a la lista de tablas forzadas a residual
     durante la tanda): la adopto. Que quede como decisión mía del 16/10/2026.»
- **Además pidió,** y van en la misma versión:
  - la línea del §6.7 que cierra el pendiente 27;
  - el sha256 vigente del registro de alcance en el §1.4 (`06b8267a…`, desde `5f02ace4`);
  - el control por script de cada ruta y cada sha256 que cita el pre-registro
    (`data/experiment/controles_tanda1/control_citas_preregistro_tanda1_mesa.json`).
- **La tercera versión para firmar** (11:53:36). La autora revisó la segunda con la mesa de apoyo, no la firmó y pidió estos cambios y
  nada más:
  1. **T4, la opción b con un ajuste** (tal cual): «Además de la atención sobre la tasa ponderada de cada estrato, RI tiene su propia
     atención: junta los dos estratos: sus 30 unidades leídas (15 de ítems y 15 de no ítems), ponderadas por las unidades de sus celdas en
     cada estrato; es un test exacto unilateral al 5 % contra la tanda 0; bajo la hipótesis nula, cada celda tiene la tasa de la tanda 0
     de su estrato; si salta, se leen 30 unidades RI más (15 por estrato, con las cuotas de RI y las cadenas de la ampliación); NG no lleva
     atención propia: con NG resto en el 83 %, repetiría la atención general; las 94 sin_raiz de NG (ceninf y nmcief) se informan con su
     cifra por celda, sin umbral, declarado.»
     - Con los pesos proyectados (`umbrales_t4_por_celdas_mesa.json`, bloque `atencion_RI`):
       - la atención de RI salta desde una tasa ponderada de 0,278;
       - la probabilidad de que salte al menos una atención con todas las celdas en la tasa de la tanda 0 es 0,136;
       - la potencia de la atención de RI con su tasa duplicada es 0,694.
  2. **La celda de un elemento que no es una unidad** (tal cual): «adopto tu propuesta de la (12) y la extiendo a las vigilancias (1), (3)
     y (7). Un nodo va a la celda de su unidad (la de su procedencia primaria) y una arista, a la de su nodo de origen. Si la (3) cuenta
     grupos de nodos, la celda es la del nodo de id menor.»
  3. **Las clases y las poblaciones chicas** (tal cual): «Si una clase entera tiene menos elementos que su cuota, entran todos y lo que
     falta sale de la otra clase, declarado. Si la población tiene 30 o menos, se lee entera, sin celdas, como la cola.»
  4. **La base de las semillas** pasa a ser el sha256 de la tercera versión para firmar, la que entra con su commit.
- **La firma del pre-registro de la tanda 1** (12:05:12; tal cual): «Firmo la tercera versión para firmar del pre-registro de la tanda 1
  (33a3c34b…) tal como está.»
  - La tercera versión para firmar entró con `3b61f154`. La versión firmada entra con el commit del pre-registro firmado, que va antes
    del de este registro, y cambia solo la cabecera y la sección de la firma.
- **La propuesta de la mesa confirmada con la firma** (tal cual): «Con la firma confirmo la PROPUESTA DE LA MESA del §5.4 bis, punto 2: si
  una clase entera no llega a su cuota, lo que falta se reparte entre las dos celdas de la otra clase en proporción a sus cuotas, con el
  redondeo a favor de la de cuota mayor, y cada celda sortea con su propia cadena.»
  - Rige desde la firma. No queda ninguna otra PROPUESTA DE LA MESA abierta en el pre-registro (sección de la firma).
- Las secciones anteriores no se editan.

## 18. El despacho de la tanda 1, su corrida en seco y lo que decide la autora antes de la extracción (agregado del 16/10/2026)

Decisiones de la autora recibidas el 16/10/2026 a las 12:59:19 (hoja de ruta de la mesa, §127), a las 13:28:14 (§128) y a las 14:31:32
(§130).

- **El despacho de T1** (12:59:19; tal cual):
  - «Los tres valores quedan como los fijaste: el orden de menor a mayor por unidades, margen_unidad_usd = 0,35 y checkpoint_cada = 150 en
    lingeef y depaho.»
  - «La consulta de deprecaciones va dos veces: la ejecutora en T1, como está en el punto 2.1, y vos otra vez al revisar el FRENO T1, antes
    del «seguí» de T2.»
  - T2 queda preparada como un solo lanzador, que recorre los 20 TOs con la misma salida y corre el freno por id de modelo antes del primer
    TO y después de cada uno; y el FRENO T1 da el sha256 del manifiesto y de la E0 de los 20 para que el «seguí» de T2 los controle antes de
    gastar. Lo hizo T1: `data/experiment/tanda1/t2/lanzar_t2.py` y `data/experiment/tanda1/t1/sha256_para_T2.txt` (108 renglones).
- **Quién lanza T2** (13:28:14; tal cual): «la ejecutora, en segundo plano desde su sesión, como en la tanda 0. Si el lanzador se corta, lo
  relanzo yo desde mi terminal con el mismo comando. Ponelo así en el «seguí» de T2.»
- **Lo que el FRENO T1 deja para la autora** (14:31:32; tal cual; `data/experiment/tanda1/t1/FRENO_T1.md`, §12):
  - «el estimado por TO queda con 6 decimales, como está»;
  - «la diferencia de 2 tokens de la tabla de A2 se declara y no se toca». Es la de `data/experiment/alcance_e1/a2/freno_a2.md:68-80`: por
    documento suma 190.843 tokens y USD 0,190843, contra el total de 190.841 y USD 0,190841, porque cada documento redondea sus tokens;
  - «la interrupción manual del lanzador no se prueba en vivo antes de T2: se declara». El camino está en el código
    (`lanzar_t2.py:172-182`, `:194-196`).
- **Los `nombres_remision` de la tanda 1** (14:31:32): en el manifiesto de la tanda 1 quedaron vacíos, y en la tanda 0 están armados a mano,
  desde el título de portada más una variante corta (`docs/plan_tesis.md:765`, decisión 4). El ensamblado los usa para reconocer las
  remisiones a otros documentos: no cambian T2, pero sí el grafo. La mesa propone cómo fijarlos antes de T3, y la autora lo decide antes de
  T3. Las condiciones de la autora, tal cual:
  - «con una regla general, derivada del inventario y no a mano, diseñada y medida sobre las listas de la tanda 0»;
  - «en el manifiesto del ensamblado, sin tocar el de extracción, que el lanzador controla por su sha256»;
  - «con lo que cambia en cada tanda, la tanda 0 incluida».
- **La consulta de deprecaciones de la mesa** (16/10/2026, entre las 14:34:00 y las 14:34:26; `data/experiment/controles_tanda1/consulta_deprecaciones_mesa_161026.txt`):
  `claude-haiku-4-5-20251001` y `claude-sonnet-5` activos, sin fecha de deprecación y sin entradas en el historial; el aviso llega con al
  menos 60 días. Da lo mismo que la de la ejecutora (`data/experiment/tanda1/t1/consulta_deprecaciones_t1.txt`, 13:30:08). No hay retiro
  anunciado: no corresponde el freno del §4.2 del pre-registro.
- Las secciones anteriores no se editan.

## 19. Los `nombres_remision` desde la tanda 1 y la variante con la raya (agregado del 16/10/2026)

Decisiones de la autora recibidas el 16/10/2026 a las 15:48:10 (hoja de ruta de la mesa, §132), sobre la propuesta de la mesa de la
§131 (`c827ec2b…`). Las condiciones son las de la §18. La medición y el código están en `data/experiment/nombres_remision/`.

- **La regla** (tal cual): «Decido la a». Los `nombres_remision` de cada TO salen solos de su título oficial del inventario, con la regla
  de `data/experiment/nombres_remision/regla_nombres_remision_v2_mesa.py`. Tiene tres patrones generales:
  - las abreviaturas expandidas, con una tabla cerrada de las 10 que tiene el inventario;
  - «de los» y «de las» → «de»;
  - el corte antes de « por cuenta de ».
  Nunca recorta la cabeza del título.
- **La raya** (tal cual): «El grafo evaluado es el ensamblado acumulado (docs/protocolo_dos_grafos.md §2.1; enmienda 8, R3): la raya no
  queda para «si se arma un acumulado». La decido ahora, antes de que exista cualquier salida de la tanda final. Regla: en cada
  ensamblado desde la tanda 1, la variante con la raya se suma solo si, con los TOs de ese ensamblado, el contraste contra los 157 títulos
  da 0 resoluciones distintas de la referencia. Con tus cifras: en la tanda 1 sola (6 distintas), en la final sola (3) y en tandas 0 y 1
  por la regla de caída (8) no entra; en el acumulado de las tres entra (1.319 contra 1.279, 0 distintas).»
  - Las fuentes: el grafo evaluado es el ensamblado acumulado de todas las tandas (`docs/protocolo_dos_grafos.md:48-49`); la R3 está en
    `docs/enmienda8_protocolo_entre_tandas_2026-10-15_calendario_hacia_B6.3.md:50`; la regla de caída, en
    `docs/regla_de_caida_grafo_evaluado_2026-10-15.md`.
  - Las cifras son las de la medición del 16/10/2026, sobre la E0 y sin ninguna salida de extracción ni de evaluación
    (`data/experiment/nombres_remision/medicion/`).
  - La condición la aplica `data/experiment/nombres_remision/derivar_manifiesto_ensamblado_mesa.py`, con la variante
    `regla_nombres_remision_v2_con_raya_mesa.py`.
- **Los nombres en el grafo evaluado** (tal cual): «En el ensamblado acumulado del grafo evaluado, los nombres de los 128 TOs salen de la
  regla, la tanda 0 incluida: es la configuración que mediste. Los manifiestos sellados de la tanda 0 no se tocan.»
- **La corrección de la opción b de la propuesta** (tal cual): «con las listas a mano de la tanda 0 adentro, b también da 1.279 en el
  acumulado; la a se elige porque cumple la condición de la §18 (sin listas a mano en el grafo evaluado), no por las 9 menciones.»
- **La versión 1 de la regla**, como pidió la autora contarla:
  - era igual a las listas a mano en la tanda 0;
  - perdía 7 menciones en el acumulado de las tres tandas: 6 de ri_iepsp a pro y 1 de fabcra a pagjub;
  - la versión 2 sumó los patrones 2 y 3 después de ver eso. Se midió sobre texto de E0, sin salidas de extracción ni de evaluación;
  - la versión 1 y sus mediciones quedan en `data/experiment/nombres_remision/reemplazados/`.
- **La corrección del texto de la propuesta** (tal cual): «Corregí «los tres patrones … que cambian alguna resolución»: en la tanda 0 sola
  solo cambia el de las abreviaturas; los otros dos cambian en los acumulados.»
- **Lo que la regla no toma** (tal cual): «"Operaciones a contado" y "Efecti- vo" van al backlog con su capa_pipeline (el corte de fin de
  renglón es de E0).» Son BKL-0045 (capa ensamblado) y BKL-0046 (capa E0), en `data/backlog/backlog.jsonl`.
- **Los manifiestos de ensamblado de la tanda 1:** `data/experiment/reextraccion_v2/manifiestos/tanda1_ens_veinte_r2b.json` y su sin
  cola, `tanda1_ens_veinte_r2b_sincola.json`.
  - Son copias del de extracción (`tanda1_20tos_r2b.json`, `818a62cf…`, el del reparto del estimado, que el 94 no toca) con `nombre`, `descripcion` y los
    `nombres_remision` de la regla.
  - La variante con la raya no entra: su contraste en la tanda 1 da 6 resoluciones distintas de la referencia.
  - Suman nombres a 6 de los 20 TOs, los regímenes informativos.
- **El commit** (tal cual): «después del de T2 y antes de T3, con la regla (incluida la condición de la raya), el script, los dos
  manifiestos de ensamblado de la tanda 1, la medición (con la v1 en reemplazados) y el registro».
- Las secciones anteriores no se editan.

## 20. La prueba del prompt de extracción de GraphRAG y dónde se reporta U-COMP-E1 (agregado del 16/10/2026)

Decisiones de la autora recibidas el 16/10/2026 a las 16:05:25 y el 17/10/2026 a las 08:17:24 (hoja de ruta de la mesa, §132 y §137).

- **La condición de la prueba** (D1 de la autora, del 15/10/2026; tal cual): «la prueba corre solo si aparece una ventana que no compita
  con las tandas ni con las mediciones; si no, queda como trabajo futuro».
  - La prueba es U-PRUEBA-GRAPHRAG: el prompt de extracción de GraphRAG con el esquema congelado, sobre unidades de E0 de la tanda 0,
    contra la salida de E1 r2b de esas mismas unidades. Responde, sobre el propio corpus, por qué no se usó un extractor genérico.
  - Su diseño ajustado está anotado en el plan, debajo de la fila C0.4 (`docs/plan_tesis.md`). No reabre el descope de GraphRAG-MS de
    esa fila.
- **Cuándo se decide la prueba** (17/10/2026, 08:17:24; tal cual): «La decisión de correr U-PRUEBA-GRAPHRAG se toma el miércoles 28/10/2026
  a las 18:00. Corre el jueves 29 y el viernes 30/10 solo si los resultados de B6.3 están sellados y tengo 2,5 h libres entre esos dos días;
  la preparación, a USD 0, va el 29 a la mañana. Si no, queda como trabajo futuro.»
- **Dónde se reporta U-COMP-E1** (tal cual): «la comparación de modelos del extractor (U-COMP-E1) se reporta en un apéndice de la tesis y
  no en el capítulo 5».
  - Rige sobre lo que dicen hoy `docs/checklist_pre_escalado.md:228`, `docs/insumos_escritura.md` §8 («Dónde va») y
    `docs/plan_tesis.md:787` (fila B6.4), que este agregado no edita.
- Las secciones anteriores no se editan.

## 21. Los dos frenos de T2 de la tanda 1, el reparto del estimado y lo que dejan para registrar (agregado del 17/10/2026)

Decisiones de la autora recibidas el 16/10/2026 a las 23:34:55 y el 17/10/2026 a las 07:50:35 y a las 08:00:21 (hoja de ruta de la mesa,
§134 a §136).

- **El primer freno** (FRENO T2 parcial 1, sha256 `49e2dca8…`; copia en el paquete de la ejecutora `revision_tanda1_FRENO_T2/`, manifest
  `18315f8d…`):
  - T2 frenó por proyección al cerrar ri_pgn:e3, el 16/10/2026 a las 21:01:43, con USD 1,149063 gastados.
  - Los dos primeros TOs costaron 1,4987 veces su estimado: ri_gerc 1,1047 y ri_pgn 1,7801.
  - La proyección dio USD 104,0509 contra el tope de 100,7291 (§5 del FRENO).
- **El relanzamiento** (16/10/2026, 23:34:55; tal cual): «Decidí relanzar T2 con el mismo tope y el mismo comando, porque con el 1 % de la
  tanda la proyección no alcanza para decidir el tope. Lo relanzó la ejecutora desde su sesión, a pedido mío, a las 23:34: la decisión 5
  del §18 preveía mi terminal para un corte, no para un freno con su sesión viva.»
  - Lo que la §18 preveía, en «Quién lanza T2»: «Si el lanzador se corta, lo relanzo yo desde mi terminal con el mismo comando.»
- **El segundo freno** (FRENO T2 parcial 2, sha256 `144be679…`; paquete de la ejecutora `revision_tanda1_FRENO_T2_parcial_2/`, manifest
  `616dffed…`, con el parcial 1 adentro):
  - T2 frenó por proyección al cerrar ri_rml:e1, el 17/10/2026 a las 00:17:08, con USD 3,664724 gastados.
  - La proyección dio USD 122,7914 contra 100,7291.
  - La E1 de ri_rml costó 3,5976 veces su estimado; ceninf, 0,9814 veces (§5 del FRENO).
- **Las decisiones de la autora sobre el segundo freno** (17/10/2026, 07:50:35; tal cual):
  - «No aplico la regla del tope.»
  - «Decido corregir el reparto del estimado, no el tope.»
  - «El ls de la salida de ri_pgn no cambia U-MED-VERIF: la ejecutora vio solo nombres, no abrió ninguno y yo no vi nada. Queda declarado
    en la §21.»
- **Lo que sostiene el reparto,** con las cifras de la verificación de la mesa. La autora confirmó a las 08:00:21 que van al repo estas y
  no otras. Script: `decisiones_135_mesa/verificacion/verificar_medicion_mesa.py`, en el paquete de la mesa.
  - **El modelo:** un costo proporcional a los caracteres de la E0 completa, a la tarifa por carácter de la tanda 0 (0,021115 / 1.164,7).
    Explica los cuatro tramos pagados. Lo real sobre ese modelo es:
    - 0,8516 en ri_gerc;
    - 0,9721 en ri_pgn;
    - 0,6971 en ceninf;
    - 0,9787 en la E1 de ri_rml.
  - **Con el estimado plano por unidad:**
    - la proyección del runner pasa el tope desde el cierre de ri_rml:e3 con cualquier costo desde 0,9 veces el modelo;
    - entre 0,9 y 1,0 veces, el pico va de 143,58 a 155,65;
    - la regla del tope que había propuesto la mesa (140,67 con este freno) también frenaría ahí.
  - **Con el estimado repartido por caracteres y el mismo total,** la proyección no pasa el tope hasta 1,4 veces el modelo y lo pasa desde
    1,46: el tope sigue frenando un exceso real.
  - **Con qué se decidió:** solo con cifras de costo, sin ninguna salida de calidad de la tanda.
- **El cambio** entra antes del commit de T2. Lleva:
  - el manifiesto de extracción, con `limites.estimado_usd` repartido;
  - el lanzador, con `MANIFIESTO_SHA256`;
  - `sha256_para_T2.txt`;
  - una nota fechada al pie de `docs/preregistro_tanda1.md`, que declara el desvío del §3 y la lectura de C2.
  No cambian U, la tarifa, el total, el tope ni el margen por unidad.
- **Lo que los frenos dejan para registrar** (16/10/2026, 23:34:55; tal cual): «la doble cuenta de la fase que cierra en la proyección (al
  backlog, sin tocar el código sellado), logs/cache_usage.jsonl, que no estaba en la lista de lo nuevo del «seguí», y el ls que mostró
  nombres reservados por el cegamiento en la salida de ri_pgn, sin abrirlos».
  1. **La doble cuenta** es BKL-0047, en `data/backlog/backlog.jsonl`.
     - En el checkpoint de cierre de una fase, la fase que cierra entra dos veces en el estimado corrido
       (`data/experiment/reextraccion_v2/corpus_v2/runner_corpus.py:404-415`; `cerrar_fase` va antes del checkpoint, `:945-947`).
     - En el primer freno la proyección dio 104,0509, y sin la doble cuenta habría dado 104,3965.
     - El runner es código sellado y no se toca durante la tanda (pre-registro de la tanda 1, §7).
  2. **`logs/cache_usage.jsonl`** es el registro de uso de cada respuesta real. Lo escriben los clientes de E1 y E3 en la raíz del repo
     (`cliente_e1.py:53` y `cliente_e3.py:52`; decisión 3 de `docs/decisiones_caching_extraccion.md`).
     - Está ignorado (`.gitignore:48`), así que no entra en ningún commit.
     - Cambia con cada corrida y no se abre: sus renglones por componente cuentan los reintentos (cegamiento, pre-registro de la tanda 1,
       §7).
     - Va en la lista de lo que cambia T2.
  3. **El `ls`.** La ejecutora listó la carpeta de salida de ri_pgn y el listado mostró los nombres de archivos que el cegamiento reserva.
     No abrió ninguno (FRENO T2 parcial 1, §8, error 2). Por la decisión de arriba, no cambia U-MED-VERIF.
- **PENDIENTE para el pre-registro de la tanda final** (17/10/2026, 07:50:35; tal cual): «Anotá como pendiente para el pre-registro de la
  tanda final que su estimado se reparta igual desde el principio: su tramo 1 tiene los regímenes informativos y va primero.»
- Las secciones anteriores no se editan.

## 22. U-MED-DESAMB: la desambiguación del grafo, abierta sin medir sobre el grafo vigente (agregado del 17/10/2026)

Decisión de la autora del 17/10/2026, recibida a las 10:29:16 (hoja de ruta de la mesa, §139).

- **Qué abre** (tal cual): «Quiero investigar a fondo todo lo que une, separa o asigna entidades en el pipeline, medir dónde se equivoca y
  arreglar ahora lo que se pueda arreglar bien, con cada decisión justificada y medida, para que el grafo evaluado sea el mejor posible.»
- **Las condiciones** (del mismo pedido):
  - USD 0, sin API, fuera del repo;
  - ninguna medición sobre el grafo vigente y ningún sorteo hasta que la autora lo apruebe: el diseño, el mapa, los scripts y el código
    preparado se prueban sobre el grafo viejo de desarrollo r2a (`93a7af72…`);
  - nada de volver a extraer: el prompt, el esquema y los modelos no cambian (enmienda 8, §9);
  - ninguna cifra de U-MED-UMBRALES;
  - las reglas candidatas (S1, S2, S3, C1 y O1) se escriben antes de medir, y la lectura de la autora decide S1, S2 y O1;
  - un juez de modelo, si se aprueba, da solo la cifra descriptiva y no decide ningún cambio del grafo.
- **Lo que preparó la mesa** (fuera del repo, `decisiones_139_mesa/` del paquete de la mesa): el mapa de los mecanismos, la verificación
  de las cifras de la mesa de apoyo, el código de los tamaños, de las reglas candidatas, de la planilla y de los estimadores, con sus
  selftests, y el calendario contra el corte del grupo 2. Nada se aplicó.
- **Lo que la verificación deja registrado** (script `decisiones_139_mesa/verificacion/verificar_mesa_de_apoyo_mesa.py`, en el paquete de
  la mesa; cuenta las vías ya guardadas en `resolucion_sujetos.jsonl`, sin leer la corrección de nada):
  - en el grafo sin cola diez rs1 (`61dd1b69…`), 2.546 relaciones de sujeto: R1 533 (168 con desacuerdo del modelo), R4 1.821, R2 8,
    calificador 16, R3 20 y cuarentena 148;
  - dentro de R4: la regla del texto da el mismo id en 1.010, otro id en 277, no hay regla con la mención verificada en 334 y la mención
    no verifica en 200;
  - entre `e22fae1a…` y `61dd1b69…`, los dos sin cola, R3 pasa de 1 a 20 y la cuarentena de 164 a 148, por tres causas:
    - el singular «entidad» como expresión de R3 en los documentos con rol (U-OMISIONES-COD, ítem f′): 412 relaciones reciben la regla
      R3 y 19 pasan de cuarentena a R3;
    - las contracciones en la verificación de la mención (U-OMISIONES-COD, ítem f): cambian 48 verificaciones;
    - R2-3 de U-RERESOL-CAT: 4 relaciones de docvig pasan a cuarentena por la parte A
      (`data/experiment/reresolucion_catalogo/freno_r2_3.md:14`);
  - la cuarentena se cuenta en dos unidades: relaciones (`resolucion_sujetos.jsonl`) o filas del registro de no mapeados (LN-5 de la
    suite). Toda cifra de cuarentena dice cuál es.
- **Una contradicción, registrada:** la regla O1 es una arista nueva entre operaciones, y un predicado derivado nuevo cambia el esquema
  (`data/experiment/pyd_r2/code/modelos_r2.py:165`; `scripts/shapes_validator.py:1129-1135`), que la enmienda 8, §9, deja fijo. Sin una
  decisión de la autora, O1 no entra como arista al grafo evaluado.
- **PENDIENTE de la autora:** las decisiones del informe de la mesa (`decisiones_139_mesa/informe/`, §9), entre ellas el criterio de
  sujetos, las reglas de decisión y los tamaños, que se firman y se sellan antes de leer, y el juez de modelo con su tope.
- Las secciones anteriores no se editan.

## 23. U-MED-DESAMB: las decisiones de la autora, el diseño sellado y el sorteo (agregado del 17/10/2026)

Decisión de la autora del 17/10/2026, recibida a las 11:31:33 (hoja de ruta de la mesa, §140), sobre el informe de la mesa (§139). Firmó
el criterio, las reglas de decisión, los tamaños y el juez, con 13 decisiones.

- **El diseño sellado:** `data/experiment/med_desamb/diseno_sellado_med_desamb_2026-10-17.md`, sha256 `05445091…`, sellado a las
  11:41:19, antes del sorteo y antes de correr nada sobre el grafo (`sello_diseno_med_desamb_2026-10-17.txt`). Lleva:
  - el criterio de sujetos, con «acierta» solo para «correcta» y la sensibilidad con «correcta o genérica», que se informa y no decide;
  - S1 y S3 tal cual, y S2 como «aplica si aciertan 7 o menos de 16», con su Wilson informado;
  - los tamaños, la regla de la semilla, la normalización de C1 y el sha256 del código.
- **Las decisiones** (resumen; el mensaje está en la sesión de la mesa):
  - la lectura es de 52 ítems: E4 26, E6 16 y el control fijo (E1 4, E3 3, E5 3), con 12 calibradores mezclados;
  - S2 es solo cuarentena, y el rol va al grafo corregido;
  - O1 va al grafo corregido del cap. 6 (salida (c)), con su tamaño como cifra descriptiva;
  - C1 se decide con el censo de todas sus colisiones, sin piso;
  - el juez de modelo va con condiciones, y el gasto está autorizado hasta USD 40;
  - P2 y P3, sí; P1, solo como diagnóstico sobre los grafos sellados;
  - la lectura cierra el jueves 22/10/2026 a las 12:00. El orden de recorte es el juez, S3, y S1 y S2; C1, al final.
- **Las cifras descriptivas sobre el grafo sin cola diez rs1** (`61dd1b69…`; `data/experiment/med_desamb/salidas_rs1/`, USD 0):
  - Operacion: 66 grupos con la misma clave de texto en puntos distintos de un documento, con 148 nodos (el 8,41 %). 20 grupos tienen
    algún enlace: 18 conectados y 2 en parte;
  - en las normas, el 1,37 % o menos;
  - 2.505 aristas `aplica_a`;
  - C1: 2 colisiones entre documentos, con 6 nodos;
  - O1: 42 vínculos;
  - P1: 3 aristas con marcas distintas dentro de un documento y 0 aristas unidas entre documentos, en los cuatro grafos rs1 de la tanda 0.
- **El sorteo:** sellado a las 11:41:48, con la lista de sha256 `811bd20f…` (`data/experiment/med_desamb/sorteo/sello_muestra.json`).
  - El control de las normas dio OK: 64 ítems, 0 problemas.
  - La lista, la planilla y la clave quedan fuera del repo hasta que cierre la lectura, en el paquete de la mesa.
- **PENDIENTE:**
  - de la autora: la lectura, el censo de C1 y la firma de la enmienda 2 al pre-registro de tripletas antes del sorteo de T;
  - de la mesa: el código del juez, con su prueba en seco antes de la ventana.
- Las secciones anteriores no se editan.

## 24. U-MED-DESAMB: los calibradores nuevos, S3 confirmada y los requisitos del juez (agregado del 17/10/2026)

Decisión de la autora del 17/10/2026, recibida a las 12:29:34 (hoja de ruta de la mesa, §141), **antes de leer**. Va como nota 1 al
diseño sellado (`data/experiment/med_desamb/diseno_sellado_med_desamb_2026-10-17.md`), sellada a las 12:33:46
(`sello_nota1_diseno_med_desamb_2026-10-17.txt`). El texto sellado a las 11:41:19 no cambia.

- **S3:** la autora confirma tal cual las dos precisiones de la mesa: qué es un error y cómo se normaliza la mención.
- **Los calibradores cambian.** El motivo, tal cual: «Para que el juez aprenda las fronteras, los calibradores tienen que estar cerca de
  ellas.»
  - Los 12 de la planilla de lectura dejan de ser calibradores y se saltean.
  - La lectura de 52 y la muestra del juez no cambian.
  - Los nuevos son 5 de E4, 5 de E6 y 2 de E2, sin las filas de la lectura ni las de la muestra del juez, con la regla de la semilla del
    diseño. Se sortearon a las 12:34:05, con la lista de sha256 `547123b9…`
    (`data/experiment/med_desamb/sorteo/sello_calibradores_v2.json`).
  - Ninguno es un calibrador viejo, y el control de normas dio OK.
  - Van en una planilla aparte, que dice que son calibradores. La autora la lee solo si termina las 52 antes del miércoles 21/10 a las
    18:00, con una línea de porqué por cada entrada.
- **El código del juez:**
  - los calibradores entran al prompt como ejemplos resueltos, con el caso, la clase y el porqué de la autora;
  - el juez recibe la misma información que la autora, con el anexo de las entradas;
  - la salida «requiere adjudicación» la adjudica la autora;
  - el prompt dice que no se ajusta sin su decisión ni mirando sus clasificaciones de las 52;
  - sin 68 de 78, su cifra no se usa, sin segunda vuelta.
- **El anexo de las entradas**, agregado después del sello, queda declarado como está.
- **La enmienda 2 al pre-registro de tripletas:** la autora la firma más adelante, antes del sorteo de T.
- La lista de los calibradores, su planilla y su clave quedan fuera del repo hasta que cierre la lectura, en el paquete de la mesa.
- Las secciones anteriores no se editan.

## 25. U-MED-DESAMB: el código del juez de modelo y su prueba en seco (agregado del 17/10/2026)

Pedidos de la autora del 17/10/2026, recibidos a las 12:41:39 y a las 13:11:16 (hoja de ruta de la mesa, §142 y §143): el código del juez,
con los requisitos de la nota 1 al diseño sellado, USD 0 y sin ninguna llamada a la API.

- **El código:** `data/experiment/med_desamb/juez/juez_desamb_mesa.py`. Su selftest, con un cliente falso y sin red, da 42 controles en
  verde.
  - El prompt deja el lugar de los 12 ejemplos resueltos (el caso, la clase y el porqué de la autora), que se completa al cargar su hoja.
  - El juez recibe la misma información que la autora, con el anexo de las entradas, y no ve ninguna clasificación suya salvo las de los
    calibradores.
  - La salida «requiere_adjudicacion» existe y la adjudica la autora.
  - El prompt dice que el instrumento no se ajusta sin su decisión ni mirando sus clasificaciones de las 52, y que sin 68 de 78 la cifra
    no se usa, sin segunda vuelta.
  - En la herramienta, el porqué va antes de la clase: los campos van en el orden letra, porque y clase, y el porqué cita en una línea las
    palabras del texto que identifican al sujeto (decisión de la autora del §143).
- **La prueba en seco** (`juez/seco/`): 1.149 pedidos armados y no enviados, 383 ítems por 3 repeticiones (los 344 de la muestra del juez y
  las 52 de la lectura, con 13 filas en las dos).
  - Con la regla de caracteres / 3,5, NO VERIFICADA, el costo estimado es de USD 20,69 de los 40 del tope, y la humo tiene una cota de
    USD 0,47.
  - El SDK no se importó.
- **La prueba de humo, preparada y sin correr.** Se corre en la terminal de la autora, solo con su autorización. Frena:
  - sin los calibradores cargados;
  - sin la lectura cerrada a más tardar el miércoles 21/10/2026 a las 18:00;
  - sin el sello de la tanda final;
  - después del martes 27/10/2026;
  - con una extracción corriendo;
  - con la salida dentro del repo.
  - Hoy frena por cinco de esos controles.
- **Las ocho decisiones de implementación de la mesa, confirmadas por la autora (§143), con un cambio en la 7:**
  - una entrada que el juez manda a adjudicación, o sin moda, cuenta como desacuerdo en el acuerdo de validez;
  - una salida mal formada se reintenta una vez, y si vuelve mal, esa repetición no vota;
  - las salidas de la humo no entran a la cifra;
  - una fila que está en la lectura y en la muestra del juez se juzga una vez, con el formato de la planilla de la autora;
  - el juez no ve el número del ítem;
  - en la muestra del juez, las dos entradas de E4 van en el orden de `random.Random(f"{semilla}:juez:entradas:{ítem}")`;
  - **la 7, con el cambio de la autora:** la cifra principal va con la entrada que está hoy en rs1. Si S1 o S2 pasan, se informa además la
    cifra con las reglas aplicadas, descriptiva y declarada. En E4 sale de la misma corrida, porque el juez clasifica las dos entradas.
    Con S2, las relaciones de E6 van a cuarentena y salen de esa cifra; se informan aparte, con su N (precisión de la mesa);
  - el juez corre sin razonamiento extendido, con salida máxima de 1.024 tokens y la herramienta obligada.
- Las secciones anteriores no se editan.

## 26. Lo pago de la evaluación, en secuencia después de la tanda final, y las horas hasta el 31/10 (agregado del 17/10/2026)

Decisiones de la autora del 17/10/2026, recibidas a las 15:40:05 (hoja de ruta de la mesa, §144), al pedir el calendario v5.

- **El orden de lo pago, tal cual:** «la tanda final se despacha apenas estén sus condiciones. Lo pago de la evaluación (A2.2, Q8, las
  tripletas V, el juez de U-MED-DESAMB y GraphRAG) corre después, en secuencia: nada pago en paralelo con una extracción, ni en el repo
  ni fuera de él. Mi condición del mandato de A2.1 (:150-151) vale para todo lo pago.» Los pasos pagos de A2.1 van entre T5 de la tanda 1
  y el despacho de la tanda final, si entran, o después del sello de la tanda final. La propuesta de correr lo pago en un clon, en
  paralelo, queda descartada.
- **Sus horas, del 17 al 31/10:** 6 por día entre semana y 10 el fin de semana; el sábado 17, 6.
- **La escritura de la tesis** entra al calendario como una pieza más, con horas propias (estimaciones NO VERIFICADAS): de 11 a 13,5 h
  antes del sábado 24 y de 16 a 21 h del martes 27 al sábado 31. El recuento de las cifras sobre el grafo escalado lo corre una unidad
  de la mesa de escritura sobre una copia, sin turno en el repo.
- **La generación de las preguntas de B6.3** no espera turno en el repo: corre en una carpeta fuera del repo que tiene solo los
  documentos fuente, como la de EV2 (`data/experiment/exploracion/ev2_fidelidad/registro_generacion_ev2_fidelidad.md:8-21`). Si se hace
  como la de EV2, no paga API: el reporte de EV2 la deja fuera del total, «sin costo de API en el repo»
  (`data/experiment/ev2_reporte/reporte_ev2.md:401-402`). Si pagara, va en la secuencia de lo pago.
- **El sello del diseño de U-MED-VERIF** (con sus elecciones E2 y E3) vence antes del cierre de la tanda 1. Sin ese sello no se arma el
  pozo de L-02, que son las detecciones de copia de la tanda, vedadas hasta el sello (respuesta de la mesa sobre U-MED-VERIF, §110,
  `:99-101`; cláusula de cegamiento, `docs/preregistro_tanda1.md:900-909`).
- **El presupuesto:** rige el total de USD 341 (enmienda 8, `:98-105`). Sale de la tabla del plan de la mesa del 15/10/2026, que cuenta
  como «ya gastado en este tramo» a R0, USD 0,157948. Una fecha de inicio explícita no está escrita: NO VERIFICADO.
- **Un dato de la autora:** en la tesis, el grafo evaluado se presenta en la sección de las tandas (la 4.7 del texto vigente), no en la
  4.5 que dice `docs/plan_tesis.md:288`.
- **Una consecuencia, para que la autora la decida:** con A2.2 después del sello de la tanda final, el N no se puede decidir el lunes
  19 a la noche (§12 de este registro, `:437-438`); en el calendario v5 cae el miércoles 21.
- **El catálogo de resolución y la re-aplicación única.** Lo que suma el catálogo de resolución desde la cuarentena se decide y se mide
  al cierre de cada tanda (enmienda 4, firmada en `53bbd6fa`, `:40-42`, `:51-53` y `:156-158`; pre-registro de la tanda 1, firmado en
  `95b18217`, `:139`, `:724-727` y `:893`). La re-aplicación única de la enmienda 8 (R3, firmada en `54902301`, `:50-55`) habla solo de
  las correcciones de código, y no lo mueve.
- Las secciones anteriores no se editan.

## 27. El N, la caída con lo pago, U-MED-VERIF y las reglas de la lectura de 1.16 (agregado del 17/10/2026)

Decisiones de la autora del 17/10/2026, recibidas a las 18:42:59 (hoja de ruta de la mesa, §145), sobre el calendario v5 (§26).

- **El N:** se decide con las tasas de A2.2, el miércoles 21 en el escenario central, porque la tanda final se despacha primero. La
  aprobación de las preguntas empieza antes del N, como decidió el 15/10 (§6, `:219-221`).
- **La caída y lo pago, tal cual:** «si la tanda final no está sellada el viernes 23 a las 18:00 y su extracción sigue, se pausa entre
  documentos. La ejecutora termina el documento que esté corriendo, no lanza el siguiente hasta que terminen B6.3 y las tripletas T, y
  después retoma, para la versión corregida. Así nada pago corre en paralelo, y la regla de caída se cumple («corre igual después»).»
  Va al pre-registro y al despacho de la tanda final.
- **Los recortes:** por ahora, ninguno. La autora los decide el lunes 19 a la noche, con sus horas reales del fin de semana. Las tres
  lecturas del 17/10 le llevaron, según su cuenta, unas 1 h 25 min (el gold), unos 30 min (sub-documento) y unos 11 min (1.16).
- **La generación de las preguntas:** su mandato dice con qué cuenta corre la sesión, la suscripción de la autora o la clave de la API.
  Si usa la clave, va en la secuencia de lo pago (§26).
- **U-MED-VERIF, las elecciones de la autora.** El diseño para sellar lo arma la autora, y el sello llega antes del cierre de la tanda 1:
  - E1: si una unidad de la muestra cae también en L-02, se lee igual, y la superposición se declara con sus ids;
  - E2: una marca dudosa cuenta en contra de la unidad. Al lado va la cifra de sensibilidad, sin esa regla;
  - E3: lee una lectora a ciegas, y la autora adjudica en dos pasadas;
  - las unidades de la muestra que la autora lea en T4 entre las aceptadas de la tanda 1 salen de la muestra y se reemplazan por las
    siguientes del mismo sorteo, declaradas con sus ids.
- **Las reglas de la lectura corta de 1.16, fijadas por la autora el 17/10 a las 18:05, antes de leer** (según su mensaje):
  - una dudosa de corte entre los 10 primeros hace seguir hasta el 30, pero no saca el documento: sale solo lo confirmado, y la dudosa
    se declara. El «0 de 10» vale con 0 errores y 0 dudosas de corte;
  - cualquier error de corte confirmado hace seguir hasta el 30, no solo el de 1.16;
  - la columna `limpieza` sigue la convención de S1-quater
    (`data/experiment/segmentacion_oficial_e0r2/s1quater/adjudicacion/cifras_lectura_S1quater.py:16-17`, `:95` y `:104-105`). Si hay
    restos de encabezado y de pie juntos: con un error de corte, `limpieza` = `restos_encabezado` y «también restos de pie» en la nota;
    sin error de corte, clase `limpieza`, subclase `restos_encabezado` y subclase adicional `restos_pie`.
  - La lectura de sub-documento de la tanda 1 quedó sellada antes, a las 18:02:05, sin ninguna marca de limpieza.
- **El gold de Q12:** la autora confirma otra vez, para el cruce, las dos propuestas de cómo se mide el juez: el «dudoso» del juez cuenta
  como desacuerdo, con la cifra sin esos pares al lado, y la cifra principal va sobre los 82 pares, con la cifra sin «necesita experto» ni
  «criterio mal planteado» al lado.
- Las secciones anteriores no se editan.

## 28. El juez sin ajuste, el alcance de la tanda final y los errores fuera de los criterios (agregado del 17/10/2026)

Decisiones de la autora del 17/10/2026, recibidas a las 19:35:58 y a las 20:20:12 (hoja de ruta de la mesa, §146 y §147), sobre las tres
lecturas del día (§27) y el material del alcance de la tanda final.

- **Sub-documento:** la autora confirma la lectura de la rama sin error. Los 33 límites de la tanda final no se leen y quedan como los
  segmenta la E0. Se declara con la cifra de la tanda 1: 0 errores en 14 límites.
- **El juez de EV2 no se ajusta** por los 3 desacuerdos del gold de ajuste: queda el prompt v1 (`fd446f8e…`) tal cual.
  - Son 3 de 82 pares: 2 en la dirección B (G13-3 y G14-3) y ninguno en la A, más un «dudoso» del juez contado como desacuerdo (G02-3).
  - Con tan pocos, un ajuste sería acomodarlo a estas 20 respuestas.
  - Los 3 se declaran como límite conocido, con su dirección.
- **El alcance de la tanda final:** el material de la lectura se arma ya. Si T2 cierra antes, va primero su FRENO.
  - Se leen los 46 documentos sin fila en el registro ni rol en la tabla de la release.
  - Los otros 52 quedan como están, con el criterio del 15/10 para la tanda 1.
- **El sello de la release, tal cual:** «la opción 1, una nota fechada al laudo y a la enmienda 4. No es una regla nueva: la enmienda 4,
  §2, punto 3 (53bbd6fa:64-66), ya dice que la lectura de cada tanda "cambia solo el mensaje de sus unidades: el de toda unidad ya
  extraída sale byte a byte igual, y se controla". La nota deja escrito que el cambio de mecanismo del mensaje de E1 ocurrió una vez, con
  el cableado de la tanda 1 (42823df0), y que cada tanda suma sus filas por ese punto, con el derivado y el candado nuevos y el control
  byte a byte de lo ya extraído. La release sigue siendo r2.»
  - La nota va con el mandato de la etapa A3 de U-ALCANCE-E1, cuando se firme.
- **Un documento sin fila al despacho:** se espera hasta la última hora de arranque del cableado que todavía llega al despacho del
  miércoles 21 a las 18:00.
  - El calendario v6 de la mesa la calcula: el martes 20 a las 21:15 con el escenario lento, y el miércoles 21 a las 11:00 con el central.
  - La autora la fija al firmar el mandato del cableado.
  - Si a esa hora falta alguno, sale de la tanda final, declarado, al grafo corregido. Si tiene preguntas de B6.3, rige la regla de
    reemplazo (`:451-454`).
- **Los errores fuera de los criterios.** Hoy nada de B6.3 los mide:
  - el juez v1 juzga solo contra los criterios (`data/experiment/ev2_juez/prompt_juez_v1.md:31-33`);
  - el veredicto de la respuesta sale solo de ellos (`ev2_juez/mapping.py:40-54`);
  - las tripletas miden el grafo y la exactitud de cita no mira si lo citado es cierto (`docs/plan_tesis.md:778`).
  - **Decisión de la autora:** la columna «error fuera de los criterios (sí o no, y cuál)» entra en las 20 de verificación de A2.2 y en
    las 36 de control de B6.3, a ciegas al brazo, en sus pre-registros.
  - Un juez de afirmaciones aparte queda como trabajo futuro, declarado. El control determinístico de cifras no va.
  - Si el lunes 19 a la noche las horas no dan, la columna de las 36 de control es la primera que sale, declarada.
- Las secciones anteriores no se editan.

## 29. La tanda 1 de T2 a T4, el alcance de la tanda final, U-MED-VERIF, el agente y lo que se guarda (agregado del 18/10/2026)

Decisiones de la autora del 17/10/2026, recibidas de las 20:56:55 a las 22:40:14, y del 18/10/2026, recibidas de las 08:51:05 a las
11:45:00 (hoja de ruta de la mesa, §148 a §155). Las que ya están en un documento firmado se nombran con su commit.

- **El cableado (A3):** firmado con la opción (a): la última hora de arranque es el martes 20/10 a las 21:15 (`0c927ebb`, con su nota al
  laudo y a la enmienda 4). La columna de los errores fuera de los criterios va en los pre-registros de A2.2 y de B6.3, como dice la §28.
- **U-MED-VERIF:**
  - **el diseño** quedó sellado el 17/10 a las 19:17:36, fuera del repo (sha256 `5296703d…`). Reemplaza al borrador del 15/10;
  - **el mandato de las fichas,** firmado con (a), (a) y (a) (`c0d3ab17`);
  - **la lista de exclusión** suma toda unidad de la tanda 1 cuya extracción aparezca en el material de T4, en cualquier versión, la final o
    la primera (17/10, a las 22:06:54 y a las 22:40:14). Es una precisión del §2 del diseño, fijada antes del sorteo;
  - **la precisión de los nodos compartidos** (18/10, a las 11:45:00, con la recomendación de la mesa):
    - un nodo TextoOrdenado no suma unidades, ni un Sujeto cuya procedencia tiene más de una unidad;
    - suma la extracción propia de cada unidad, en cualquier versión: la unidad de cada ficha, y las unidades de procedencia de todo otro
      nodo que muestre una ficha, incluido un Sujeto con una sola unidad;
    - el texto firmado no cambia, porque dice «cuya extracción aparezca». Va al despacho de las fichas;
    - con ella quedan 30 unidades para la muestra, aun en el peor caso de las muestras de T4 que faltan. La mesa lo midió sin ver el tamaño
      de la población (hoja §154);
  - **la lectura de cid** muestra solo el texto de la unidad y la página del PDF. Si su material llegara a mostrar una extracción, esas
    unidades entran a la lista antes del sorteo.
- **Las cifras por script:**
  - en el despacho y en el pre-registro de la tanda final, toda cifra del FRENO sale por script desde sus archivos. El despacho lo pide
    como requisito, y la revisión de la mesa lo controla (17/10, a las 22:10:33);
  - las cuentas de E3 siguen en cegamiento hasta que la autora lo pida (17/10, a las 22:40:14).
- **T3 de la tanda 1, sobre su FRENO parcial** (18/10, a las 08:51:05):
  1. para S31 rige la E0 con las partes por corte, la que leen el runner, el ensamblado (`ensamblar_tanda0.py:1822-1828`, `_chunks_r2` con
     `chunks_con_partes`) y las intrínsecas. Se informan las dos corridas. Es una precisión del gate tomada con el resultado a la vista, y
     vale igual para la tanda final;
  2. E4-a1 y E4-a4 se declaran como regresiones de la tanda 1, con su entrada de backlog;
  3. la suite se juzga sobre el acumulado. En el grafo de una tanda sola, el ítem con todas sus anclas en TOs que el grafo no tiene se
     informa aparte, como «fuera del grafo», no cuenta y lo clasifica un script. Vale también para los tramos de la tanda final;
  4. los `nombres_remision` de la tanda 0 en el acumulado son los de la regla v2 (`222a0614`);
  5. las cuatro entradas nuevas de la fixture van al commit de T3;
  6. las salidas de shapes y de la suite de los dos grafos de la tanda 1 quedan donde están, como en el re-sellado;
  7. el clon de git con los `.env` y los `NO_ABRIR_` (el error propio 1 de la ejecutora) queda declarado.
- **E4-a1 y E4-a4, la opción (ii):** se declaran y se difieren (18/10, a las 10:31:44 y a las 11:45:00). La rama de los dos sujetos es la
  misma: una mención que no verifica y va a cuarentena, fuera de los estratos de U-MED-DESAMB. Es la entrada BKL-0048 (`eb0711a1`).
- **Los commits de T3** (18/10, a las 11:45:00):
  - los dos `kg.json` del acumulado de las tandas 0 y 1 quedan fuera de git, porque pasan de 100 MB, con su sha256 en el FRENO T3 final;
  - cómo se guarda y se publica el grafo evaluado, que va a ser varias veces más grande y es el recurso del cap. 6, lo propone la mesa
    antes del sábado 24/10/2026, con su costo y lo que cambia en el sello;
  - los 20 archivos generados que llevan el usuario de la máquina en las rutas del scratchpad van como los 264 de HEAD. **Antes de
    publicar el recurso,** esas rutas se limpian en la copia publicada, sin tocar lo sellado.
- **T4 de la tanda 1** (18/10, a las 11:45:00, con las recomendaciones de la mesa, tal como están en el «seguí» de T4):
  - **la observación (12):** el universo es el de las aristas de extracción de la (10): todas menos `referencia`, menos
    `rol_fuente = esqueleto`, menos las `establecida_en` derivadas por el ensamblado (`rol_fuente = derivada_de_procedencia`; tablero,
    `:49` y [c1]) y menos las `remite_a` (el instrumento del sorteo, `scripts/muestra_aristas_obs12.py`, R5.d). En el evaluado son 18.483.
    La muestra de T3, con A4.1 tal cual (28.062), no se lee y se rehace;
  - **la nota de equivalencia del §5.2** del pre-registro de la tanda 1 (`95b18217:517-520`) parte de una premisa que no se cumple: el
    universo de la (12) de la tanda 0 restó todas las `referencia`, también las 518 cruzadas, así que la tanda 0 no leyó remisiones. Con
    las `remite_a` fuera, la (12) de la tanda 1 queda comparable con la de la tanda 0;
  - **la vigilancia (2):** la población es la de la extracción final (198 unidades). La del primer intento no se sortea; su cuenta por TO
    va solo a un `NO_ABRIR_` de T4, por el cegamiento;
  - **las vigilancias (1) y (3):** las definiciones que propuso la ejecutora en el FRENO T3, §6. En la (1), «no decidible» queda fuera de
    la tasa, declarado con su cuenta; en la (3), se declara que el grupo por tramo igual no ve las duplicaciones con tramos distintos.
- **L-02 y L-04:** no se despachan todavía. Son GC y entran en los recortes que la autora decide el lunes 19 a la noche.
- **El agente y A1.8** (17/10, a las 22:40:14; 18/10, a las 09:09:32 y a las 10:31:44):
  - A2.2, su diagnóstico y las ablaciones de A1.8 (N6) van antes de N7, con lo pago en secuencia;
  - lo primero que sale es lo GC; el diagnóstico y N6 no se recortan. Si el total proyectado pasa de USD 341, sale primero GraphRAG y
    después lo GC;
  - las reglas no cambian: el ajuste se hace solo con preguntas de desarrollo; lo que mejora la búsqueda se aplica igual a los fragmentos;
    A2.2 se mide una sola vez;
  - **el prompt:** el texto de la mesa, el mismo en los dos brazos, entra antes de A2.2, en lo común de su pre-registro. Se declara el
    cambio del sha256 de la configuración del banco (R10);
  - **U-NAV-DISENO:** la autora lo firma el lunes 19/10 con las siete decisiones (hoja §153 y §154). La 7 es la (a): si la híbrida pasa,
    reemplaza a BM25 en el sistema por fragmentos y el denso queda, con dos comparaciones y Holm. Se mide con F1 sobre BM25. El tope de N6
    entero es USD 85, con freno en 64, y GraphRAG sigue adentro (total central USD 334,18);
  - **el calendario v8** va. Si se da el escenario lento, la autora decide ese día.
- **El alcance de la tanda final:** la lectura sellada de la autora y sus dos precisiones están en el registro de alcance (`764768a4`).
- Las secciones anteriores no se editan.

## 30. Cómo se guardan los grafos grandes, la lectura de cid y las claves del catálogo (agregado del 18/10/2026)

Decisiones de la autora del 18/10/2026, recibidas a las 12:19:47 (hoja de ruta de la mesa, §156), sobre las propuestas de la §155.

- **Los grafos que pasan de 100 MB,** con la recomendación de la mesa:
  - se guardan en git comprimidos de forma determinista, con `scripts/kg_gz.py` y el sello al lado (`kg.json.gz.sello.json`);
  - manda el sha256 del `kg.json` sin comprimir, que es el que controlan el cargador y la suite. El del `.gz` va al lado, con el
    compresor, sus parámetros y la versión de zlib;
  - el grafo evaluado se publica en un release de GitHub, con la copia limpia de las rutas del scratchpad (§29);
  - vale también para los dos `kg.json` del acumulado de las tandas 0 y 1 del T3 de la tanda 1, que el commit de T3 dejó fuera.
- **La lectura de cid** (hasta 15 unidades de la tanda 1) va después del despacho de la tanda final, como propuso la mesa. Las 3 de la
  tanda final, después de su T5 (§14).
- **Las claves del catálogo:** la propuesta de la §155 tenía una contradicción. La lectura iba después de la adjudicación de U-MED-VERIF,
  cuyas dos pasadas van del 24 al 27/10, y la re-aplicación única va antes del sello del sábado 24. Así, el catálogo no crecería en el
  grafo evaluado. La mesa propone otro camino (§156). Si no lo hay, la autora lo decide el lunes 19 a la noche con los recortes, sabiendo
  que sin la lectura el catálogo no crece en el grafo evaluado.
- **El pre-registro de la tanda final:** la autora revisa el borrador y lo firma el lunes 19 temprano.
- Las secciones anteriores no se editan.

## 31. La vigilancia (3), las carpetas de lectura, los bloques que ve E1 y no E3, y el cierre de la lectura de U-MED-DESAMB (agregado del 18/10/2026)

Decisiones de la autora del 18/10/2026, recibidas a las 12:55:50 y a las 14:05:06 (hoja de ruta de la mesa, §157 y §158).

- **La vigilancia (3), antes de leerla** (14:05:06):
  - el par Obligacion —`regula`→ Operacion queda en la población, sin sorteo nuevo. El esquema reserva `regula` para ese par
    (`data/experiment/prompt_r2/diseno_prefijo_r2.md:701` y `:719`), y los dos nodos se anclan en el mismo pasaje;
  - el criterio de la lectura, tal cual: «un grupo es duplicación solo si un nodo repite el contenido normativo de otro; que el esquema
    arme el par deber y acto regulado no es, por sí mismo, duplicación.»;
  - la definición de la (3) del §29 no cambia.
- **Las carpetas de lectura de la autora** (12:55:50):
  - `lectura_alcance_tf/`, `lectura_desamb/`, `gold_q12_ajuste/` y `lecturas_1710/`, en `fuera_del_repo/`, quedan entre las carpetas
    vedadas para toda ejecutora. La cláusula va en todo «seguí» y en todo mandato desde el 18/10;
  - el motivo: la ejecutora de T4 consultó una de ellas, porque el «seguí» de T4 le daba como modelo un archivo de esa carpeta, sin copia
    ni ruta. Fue un error de la mesa, con su causa en la hoja de ruta (§157). Desde ahora, un modelo así va como copia en el paquete de la
    mesa.
- **Los bloques heredados que ve E1 y no ve E3** (14:05:06):
  - el mensaje de E1 trae toda la herencia de la unidad (`prompt_r2b.py:395-438`), con la instrucción de no extraer de esos bloques salvo
    del que abre la lista (`:346` y `:357`). El texto de E3 trae solo los títulos, el bloque de la lista y el texto propio
    (`comun_e3.py:131-160`);
  - van a la revisión entre tandas, con una fila nueva en su hoja: lo medido en las tandas 0 y 1 y lo que se espera en la tanda final
    (hoja de ruta de la mesa, §158). En la tanda 1, 47 de las 1.276 unidades aceptadas cuyo mensaje de E1 trae uno de esos bloques tienen
    un nodo con un tramo literal que está solo ahí; en la tanda 0, 36 de 1.202. La cuenta ve solo el tramo literal;
  - la mesa propone una corrección por código para la re-aplicación única, sin tocar el prompt ni E3 (§158). La decisión de la autora
    está PENDIENTE;
  - la autora no recibe propuestas de marcas para T4.
- **Las claves del catálogo** (12:55:50): la autora decide el lunes 19 a la noche, con los recortes, si la lectura va. El despacho y su
  control quedan preparados, sin despachar (§157).
- **El segundo tramo de T4** (12:55:50): la autora lee en `data/experiment/tanda1/t4/lectura_autora/`, y lo que deje ahí entra al commit
  del segundo tramo, salvo lo que la mesa señaló que no va (§157): los documentos de Numbers, los temporales y las exportaciones fallidas.
- **U-MED-DESAMB, la lectura cerrada** (14:05:06):
  - la autora cerró y selló su lectura el 18/10/2026 a las 14:04:01, con las 78 entradas clasificadas, las 13 de los 12 ítems que se
    saltean vacías y las 2 colisiones del censo de C1 decididas;
  - el control de la mesa da 14 de 14 OK. La lectura, el control y el sello en la forma que pide el juez están en
    `data/experiment/med_desamb/lectura/` (su acta, `acta_cierre_lectura_desamb.md`);
  - las exportaciones de la autora pisaron las copias de las plantillas en su carpeta. Las plantillas válidas son las del paquete de la
    mesa, en `lectura/plantillas/`;
  - las claves aparte de la lectura y de los calibradores v2 siguen sin abrir y fuera del repo;
  - **los calibradores v2** (nota 1 al diseño sellado, §2): la autora los lee solo si le da el tiempo antes del miércoles 21/10/2026 a las
    18:00, y lo decide con los recortes del lunes 19.
- Las secciones anteriores no se editan.

## 32. C1 y C2 a la re-aplicación única, y la clave y los calibradores de U-MED-DESAMB (agregado del 18/10/2026)

Decisiones de la autora del 18/10/2026, recibidas a las 15:39:16 (hoja de ruta de la mesa, §159), sobre la propuesta de la mesa del §158.

- **Los bloques heredados que ve E1 y no ve E3:** C1 y C2 van a la re-aplicación única, como los propuso la mesa (§31; BKL-0049). Las
  condiciones, tal cual:
  - «La regla es una sola y se aplica igual a las tres tandas en la re-aplicación única. Nada se corrige a mano.»
  - «La medición antes y después, sobre el acumulado de las tandas 0 y 1, trae las remisiones de la (11), la suite, las shapes y los
    conteos. Si cambia alguna remite_a, si aparece una regresión no declarada o si cambia la cantidad de nodos o de aristas, la ejecutora
    frena y me muestra los casos antes de seguir.»
  - «Unir nodos con los de la unidad de origen espera a lo que encuentre la (3). Sacarlos, no.»
  - el mandato lleva la cláusula v2 de las carpetas vedadas.
- **El mandato U-PROC-HERENCIA** está PARA FIRMAR (§159):
  - C1 es G-r extendida a las entidades declaradas con el punto propio, con su misma función y su mismo localizador
    (`data/experiment/tanda0/code/ensamblar_tanda0.py:1367` y `:1410`);
  - C1 y C2 van detrás de un parámetro apagado por defecto, así que el grafo de cada tanda se sigue sellando sin la corrección
    (principio 9);
  - la fila de la tabla de reprocesamiento entra con el código.
- **El pre-registro de la tanda final:** C1 y C2 no figuran en él, porque deja fuera la re-aplicación única (borrador v2, §0, en el
  paquete de la mesa).
- **U-MED-DESAMB:**
  - la clave aparte de la lectura se abre cuando la autora decida los calibradores, el lunes 19 con los recortes;
  - la carpeta de la lectura de los calibradores v2 y su convertidor quedan preparados fuera del repo.
- Las secciones anteriores no se editan.

## 33. U-PROC-HERENCIA: las dos decisiones del mandato, su ventana y el pre-registro de la tanda final (agregado del 18/10/2026)

Decisiones de la autora del 18/10/2026, recibidas a las 16:11:07 (hoja de ruta de la mesa, §160), sobre la v1 del mandato (§159).

- **Los tipos de C1:** los de G-r (`TIPOS_G_R`, `data/experiment/tanda0/code/ensamblar_tanda0.py:1363`).
  - En el acumulado de las tandas 0 y 1 son 71 procedencias: 32 de la tanda 0 y 39 de la tanda 1 (medido por la mesa, §158).
  - Las Comunicacion quedan fuera de C1, y C2 las marca.
- **Los nombres:** `tramo_fuera_del_texto_de_e3` para la marca, y `punto_declarado_e1` y `rol_declarado_e1` para lo que declaró E1.
- **El mandato** va en su versión final con esas dos decisiones. La firma de la autora está PENDIENTE.
- **La ventana:** la ejecutora de U-PROC-HERENCIA corre con la extracción de la tanda final en marcha, sobre una copia y sin escribir en el
  repo. El código entra después del sello de la tanda final.
- **El pre-registro de la tanda final** no lleva la línea que la mesa ofreció para su §7. La cuenta del patrón en la tanda final sale de
  C2 en la re-aplicación única. El borrador queda en v2.
- Las secciones anteriores no se editan.

## 34. U-PROC-HERENCIA: el cegamiento por U-MED-VERIF (agregado del 18/10/2026)

Decisión de la autora del 18/10/2026, recibida a las 16:24:10 (hoja de ruta de la mesa, §161), antes de firmar el mandato.

- **El motivo,** tal cual: «Su FRENO va a listar nodos de unidades de la tanda 1, y puede llegar después del sorteo de las FICHAS,
  mientras leo esa muestra. Si veo la extracción de una unidad de la muestra, esa lectura deja de ser a ciegas para ella.»
- **La cláusula** (mandato, §7 bis):
  - el FRENO no da ninguna cifra ni lista por estado de E3, ni nada de los reintentos;
  - cada procedencia va con su unidad, el nodo, el punto y el rol, sin el label, la descripción ni el tramo;
  - antes de mostrar cualquier contenido de una extracción de la tanda 1, rige la regla de exclusión de las FICHAS (mandato firmado de
    U-MED-VERIF-FICHAS, `c0d3ab17`, §3). Si la muestra todavía no está sorteada, esas unidades entran a la lista de exclusión antes del
    sorteo. Si ya está sorteada y la unidad está en la muestra, el caso espera a que cierre la lectura de U-MED-VERIF;
  - si un caso que espera frena la corrección antes del corte del sábado 24, la ejecutora avisa sin mostrar la extracción, y se resuelve
    entonces.
- **Una precisión de la mesa, que la autora decide al firmar:** el id del nodo lleva un trozo de su texto, así que en la v3 va como
  código, con los primeros 12 caracteres de su sha256.
- **El mandato** queda en v3, para firmar. La firma de la autora está PENDIENTE.
- Las secciones anteriores no se editan.

## 35. Las dudosas del T4 de la tanda 1, la firma de U-PROC-HERENCIA y el pre-registro de la tanda final (agregado del 18/10/2026)

Decisiones de la autora del 18/10/2026, recibidas a las 17:01:45 (hoja de ruta de la mesa, §163).

- **Las dudosas en el T4 de la tanda 1** (la opción (a) del «seguí» del segundo tramo, punto 2):
  - en la cola y en las dos muestras de las aceptadas, una unidad «dudosa» cuenta como error para la tasa, la atención y el freno;
  - la cuenta con las dudosas fuera, sobre las decididas, va al lado como sensibilidad y no decide nada. Si diera otra decisión de
    atención o de freno, se declara y rige la primera;
  - **cuándo se fijó,** tal cual: la autora la fijó «después de cerrar mi lectura y antes de ver las tasas, con los umbrales calculados
    antes de leer» (`data/experiment/tanda1/t3/muestras/umbrales_t4_reales.json`). El pre-registro de la tanda 1 no lo decía para la cola
    ni para las aceptadas (§5.4 a y b). Su criterio para la lectura de la segmentación es el mismo (`95b18217:191`);
  - el segundo tramo de T4 corre con esta regla.
- **U-PROC-HERENCIA, FIRMADO** sobre la v3 (§34), con la decisión 3 como la puso la mesa: el id del nodo va como código. El mandato
  firmado entra en este commit, en `docs/mandatos/UPROC_HERENCIA_procedencia_de_tramos_heredados.md`. Su despacho va cuando la extracción
  de la tanda final ya corre (§33).
- **El pre-registro de la tanda final:** la autora revisó el borrador v2 y pidió una v3 para firmar el lunes 19 temprano, con trece
  cambios y sus cuatro decisiones del §9 escritas como suyas (hoja de ruta de la mesa, §163). La firma está PENDIENTE.
- Las secciones anteriores no se editan.

## 36. A3 en paralelo con T4 y T5 (agregado del 18/10/2026)

Decisión de la autora del 18/10/2026, recibida a las 17:34:23 (hoja de ruta de la mesa, §164 y §166), para acortar el camino al despacho
de la tanda final. La autora despachó A3 en una sesión nueva con esta precisión y con los agregados de la mesa, tal cual.

- **La precisión a la condición 1 del mandato de A3** (firmado en `0c927ebb`, §4, punto 1, «T3 a T5 cerrados: una ejecutora por vez en el
  repo»):
  - A3 arranca con T4 y T5 de la tanda 1 corriendo, sobre una copia sin enlaces, y no escribe nada en el repo;
  - sus escrituras entran solo por su commit, después del de T5 y entre ejecutoras;
  - el commit controla que cada archivo que A3 toca y cada archivo que leyó para sus valores (incluidas las 78 rutas del código de la
    cadena) siga en HEAD igual que en la base de su copia. Si alguno cambió, A3 se rehace;
  - si la revisión entre tandas cambia una fila de alcance, A3 se rehace. Si saca un documento, no se rehace: su costo por documento deja
    restarlo, y se declara;
  - lo demás del mandato no cambia: USD 0, sin API, y el FRENO con los tres valores propuestos y la confirmación de la autora.
- **Los agregados de la mesa,** aprobados por la autora: los archivos leídos en el control, la copia sin `t4/` ni `t5/`, el commit entre
  ejecutoras, el cegamiento y la regla del documento que sale.
- **La nota al pie del mandato de A3** entra en el mismo commit que esta sección. El mandato no es una entrada de los valores de A3, así que
  el control de su commit no lo cuenta entre los archivos leídos.
- Las secciones anteriores no se editan.

## 37. U-NAV-DISENO firmado, la causa de la cola, la unión de nodos, la exclusión de las FICHAS y una expresión en lo commiteado (agregado del 18/10/2026)

Decisiones de la autora del 18/10/2026, recibidas a las 18:18:43 (hoja de ruta de la mesa, §166 a §168).

- **U-NAV-DISENO, FIRMADO** sobre la v6 para firmar (sha256 `998ba8fc…`, en el paquete de la mesa, `decisiones_166_mesa/unav/`):
  - con el mínimo de 3 por subtipo de varios puntos que agregó la mesa a N3;
  - **la decisión 9,** tal cual: «Ninguna de las tres: la parte de la familia 6 que vale para los dos brazos (descomponer la pregunta y
    revisar las condiciones y las excepciones antes de responder) va a la plantilla común de los dos brazos desde N6, decidida ahora y sin
    medirla aparte, como el texto del prompt antes de A2.2 (§5: la plantilla es la misma y solo cambia el bloque de herramientas). F1
    compara BM25 contra BM25 con la híbrida, las dos con esa parte, así que mide solo la híbrida. La familia 6 del grafo queda con lo
    propio del grafo: los ejemplos de navegación y las instrucciones de sus herramientas. Se declara que esa parte no se midió en
    fragmentos. El costo no cambia.»;
  - **la decisión 10,** tal cual: «La (a): 3 preguntas más en N3, solo de ejemplo, nunca medidas. Si los ejemplos entran a la
    configuración del grafo en N7, el brazo de fragmentos lleva los mismos 3 ejemplos resueltos con su herramienta, declarado, para que
    ningún brazo tenga ejemplos que el otro no tiene.»;
  - el mandato firmado va en `docs/mandatos/UNAV_DISENO_navegacion_agente.md`, en el mismo commit que esta sección, y reemplaza al
    BORRADOR del 04/10/2026 (último cambio en `97c21e4d`). Las dos decisiones van aplicadas en su texto.
- **La causa de la cola de la tanda 1** (pre-registro de la tanda 1, `95b18217:634-635`): va la propuesta de la mesa tal cual (hoja de
  ruta de la mesa, §167), el lunes 19 temprano, antes del despacho de la tanda final:
  - la mesa mira, por script sobre una copia, la lectura de la autora de las 30 tal cual y los rasgos de E0 y de E1 de cada unidad,
    contra las muestras de las aceptadas. De las 12 de la cola que no se leyeron, solo su código, su punto, su rol y sus rasgos;
  - no mira nada de E3 ni de los reintentos, por el cegamiento de U-MED-VERIF;
  - la autora lee la salida, sin lectura nueva ni marcas, y decide qué se declara en el pre-registro de la tanda final y qué va al
    backlog. Unos 30 minutos: NO VERIFICADO;
  - no cambia ningún grafo. Una corrección por código va con su propio mandato.
- **La unión de nodos** (§32): no entra a la re-aplicación única, y se declara para el grafo corregido, con la contradicción que encontró
  la mesa:
  - la vigilancia (3) mide grupos de nodos de una misma unidad con el mismo tramo (`data/experiment/tanda1/t4/FRENO_T4_tramo2.md:223`),
    así que no contesta la unión entre unidades, con la unidad de origen, que el §32 dejó esperando;
  - en los 30 grupos leídos, las 9 duplicaciones son pares de tipos distintos, y las 9 tienen un nodo Operacion: ninguna regla por tipos
    las separa de los 21 distintos (hoja de ruta de la mesa, §167, `cifras_propuestas_167_mesa.py`);
  - C1 y C2 no cambian.
- **El cegamiento:** las 3 unidades de la tanda 1 cuyo contenido vio la mesa por error el 18/10/2026 se suman a la lista de exclusión del
  despacho de las FICHAS, antes del sorteo (mandato firmado de U-MED-VERIF-FICHAS, `c0d3ab17`, §3). Son `depaho::3.12.3.2`,
  `depaho::3.12.3.3` y `snp_tr::2.2.11` (`decisiones_167_mesa/cegamiento/unidades_a_la_vista_mesa_167.json`, en el paquete de la mesa;
  sha256 `d1331ceb…`).
- **Una expresión en lo commiteado:** la que nombra el origen de una revisión, que desde el 18/10/2026 no se escribe en nada persistido.
  - No se editan las secciones cerradas ni los documentos sellados;
  - va a la lista de lo que se limpia en la copia publicada del recurso, como las rutas del scratchpad (§29), sin tocar lo sellado;
  - son 8 líneas de 4 archivos, en `bd60f6c0`:
    - este registro, líneas 582 y 789;
    - `data/experiment/med_desamb/diseno_sellado_med_desamb_2026-10-17.md:151`;
    - `data/experiment/segmentacion_oficial_e0r2/s1ter/adjudicacion/metodo_adjudicacion_S1ter.md:8`, `:9` y `:11`;
    - `data/experiment/segmentacion_oficial_e0r2/s1ter/adjudicacion/registro_pasada_1_y_seleccion_S1ter.md:264` y `:266`.
- Las secciones anteriores no se editan.

## 38. A3: el control de su commit, el cegamiento, el selftest de la caché, las anclas corridas, la fixture y el despacho de la tanda final (agregado del 18/10/2026)

Decisiones de la autora del 18/10/2026, recibidas a las 18:42:24 (hoja de ruta de la mesa, §168 y §169), sobre el FRENO de A3
(`data/experiment/alcance_e1/a3/FRENO_A3.md`, que entra con el commit de A3).

- **Los tres valores de A3** siguen PROPUESTOS: la autora los confirma después de la revisión de la mesa.
- **El control del commit de A3** (§36): va la propuesta de la mesa del §168. Para el registro de decisiones, se comparan las líneas que
  leyó A3 y que el registro de HEAD empiece, byte a byte, con la versión de la base de A3. El mandato de A3 no cuenta (§36).
- **El cegamiento** (error propio 1 de A3):
  - la ejecutora vio en la consola de su sesión cuatro cuentas de claves de las bases de la caché, una de E3, que incluyen la tanda 1;
  - no están en el paquete: van como retiradas;
  - no tocan U-MED-VERIF mientras no lleguen a la autora ni a la lectora, y se declara. La autora no abre esa consola.
- **El criterio 6 y el §6 del mandato de A3** (hallazgo 1):
  - se acepta que A3 haya corrido `selftest_clave_cache`, porque lo pide el mandato firmado, con las cuentas retiradas, y se declara;
  - T1 de la tanda final también lo corre (pre-registro de la tanda final, §4.1, punto 3). Su despacho usa el mismo retiro de cuentas
    (`data/experiment/alcance_e1/a3/scripts/clave_cache_sin_cuentas_a3.py`) o manda las cuentas a un `NO_ABRIR_`.
- **Las anclas corridas** (hallazgo 2): se arreglan en el commit de A3 sin editar texto firmado:
  - una nota fechada al pie del laudo de la release y otra al pie de la enmienda 4: `:477` pasa a `:478`;
  - F11b de la tabla de reprocesamiento: `:476-478` pasa a `:477-479`.
- **`scripts/regression_kg_esperado.json`** (hallazgo 8):
  - la mesa verificó que difiere del sello de la lista de las 78 rutas (`47c9f1b3`) solo por las cuatro entradas que le sumó el T3 de
    la tanda 1 (`eb0711a1`): 1.136 claves nuevas bajo `estado_esperado`, ninguna quitada ni cambiada;
  - la precisión al pre-registro de la tanda final queda PREPARADA para la firma de la autora del lunes 19/10/2026, sin tocar la versión
    para firmar.
- **Para el despacho de la tanda final:**
  - el rsync de `lote_tramo1_S2.sh` (renglón 11) no excluye `tanda1/t4/` ni `tanda1/t5/` (hallazgo 3);
  - el manifiesto de la tanda final se arma con el perfil de A3, después de su commit (hallazgo 10).
- Las secciones anteriores no se editan.

## 39. Los valores de A3, el plan de esta noche, las filas 67 y 68, la exclusión de las FICHAS y la precisión de la firma (agregado del 18/10/2026)

Decisiones de la autora del 18/10/2026, recibidas a las 18:59:38 y a las 19:15:01 (hoja de ruta de la mesa, §169 y §170).

- **Los tres valores de A3, confirmados** (19:15:01): el derivado `c8dea08a2ffe…`, y el candado `6b758517cee0…` y el mensaje
  `eeb11b9a3bf6…`, iguales a los de HEAD. Entraron con el commit de A3 (`c66c7ecd`).
- **El plan de esta noche** (18:59:38): la tanda final se despacha esta noche, para que la extracción corra de madrugada. No se saca
  ningún control, revisión, lectura ni prueba en seco: solo se adelanta lo del lunes 19.
- **F04b, F22 y F22b** de la tabla de reprocesamiento, que citan «candado `:464-484`»: se corrigen después del despacho de la tanda final,
  en un commit aparte. No van en ninguno de esta noche.
- **Las filas 67 y 68 del tablero:** al escribir la columna «Tanda 1», van «no cumple, fuera del residuo declarado», con la lectura de la
  mesa (hoja de ruta de la mesa, §169).
- **La exclusión de las FICHAS:** van a la lista de exclusión del despacho de las FICHAS, antes del sorteo, con las 3 de la §37, las 4
  unidades que la mesa vio por error el 18/10/2026 (`decisiones_169_mesa/cegamiento/unidades_a_la_vista_mesa_169.json`, en el paquete de
  la mesa; sha256 `de07201b…`): `depaho::4.4.5.1`, `depaho::4.4.5.2`, `efemin::2.4::cierre` y `efemin::3.1.4`.
  - Desde ahora, ninguna consola de la mesa muestra contenido de nodos de la tanda 1: la mesa trabaja con códigos, conteos y sha256.
- **La precisión para la firma del pre-registro de la tanda final** (`decisiones_169_mesa/precision_tf/`): la autora acepta los tres
  puntos, y van con su firma.
- Las secciones anteriores no se editan.

## 40. La firma del pre-registro de la tanda final (agregado del 18/10/2026)

Decisión de la autora del 18/10/2026, recibida a las 19:40:51 (hoja de ruta de la mesa, §171).

- **El pre-registro de la tanda final, FIRMADO** (`docs/preregistro_tanda_final.md`), sobre la v3 para firmar (sha256 `0897d609…`,
  `5289b02f`), con la precisión de la firma de la §39: los tres puntos sobre la fixture de la suite, en la sección «Precisión de la firma».
  La cita de la firma, tal cual: «Firmo el pre-registro de la tanda final en la versión para firmar commiteada en 5289b02f (docs/preregistro_tanda_final.md), con mis cuatro decisiones del §9 y los tres puntos de la precisión del §169.»
- La versión derivada con los huecos de antes de T1 entra en el commit que sigue, con la revisión entre tandas de la autora.
- Las secciones anteriores no se editan.

## 41. La revisión entre tandas firmada, el checkpoint de T1 y lo que sigue a la re-aplicación única (agregado del 18/10/2026)

Decisiones de la autora del 18/10/2026, recibidas a las 19:40:51 (hoja de ruta de la mesa, §171), sobre la hoja de la revisión entre
tandas v4 (paquete de la mesa, `decisiones_166_mesa/revision_entre_tandas/`).

- **La revisión entre tandas, firmada,** fila por fila:
  - **dentro:** las shapes, la suite, (4), (5), (12), las aceptadas ítems y no ítems, la atención de RI y el tamaño de la cola;
  - **se declaran:** (10), (11), (8), (1), (7) y el costo;
  - **(9), dentro:** las 7 emisiones son de snp_tr («Sistema Nacional de Pagos - Transferencias»), el dominio de esa entidad;
  - **(2):** se declara y va al grafo corregido, con el análisis de abajo;
  - **(3):** como en la §37;
  - **la tasa de error de la cola, fuera,** porque se dispara la regla del 25 %. Por la investigación de la mesa (§170;
    `decisiones_170_mesa/cola/investigacion_causa_cola_mesa.md`, en su paquete), el error va con las unidades largas y con tabla o
    fórmula. Va la declaración para el pre-registro de la tanda final («en la tanda 1, el error de la cola va con las unidades más largas
    y con tabla o fórmula; la tanda final lee su cola con la misma regla, en su T4») y la propuesta al backlog de la hipótesis 1, con
    `capa_pipeline` E1-prompt. No es un rasgo de corte y no saca ningún documento;
  - **los rasgos de corte:** ninguno confirmado. **El alcance:** sin cambios. **Los bloques heredados:** como en la §32 y la §33.
- **Los textos de los huecos** de la revisión, tal cual:
  - los rasgos confirmados: «ninguno: sub-documento, 0 errores en 14 límites; 1.16, 0 de 10; la investigación de la cola no encontró un
    rasgo de corte»;
  - los documentos que salen: «ninguno»; la lista de documentos fuera, vacía.
- **El checkpoint de T1:** `checkpoint_cada` = 150 en ctavis, depinv y pimf.
- **La declaración del 126** sobre las fuentes de los huecos de A3, de T4 y de T5, aceptada.
- **Después del despacho,** en paralelo con la extracción, USD 0 y sin nada de E3, para la re-aplicación única:
  - las remisiones: cuántas menciones del acumulado quedan sin resolver y por qué clase de causa. Si una clase se corrige por código, la
    mesa propone su mandato, con su medición, para que entre antes del corte del sábado 24/10/2026 a las 12:00 (R5);
  - los vaciamientos de la (2): si alguna causa es de código (el validador o la reparación de forma), con cifras agregadas, sin mostrar
    extracciones. Si es de prompt, va al grafo corregido;
  - la lectura de las claves del catálogo no se recorta el lunes 19: es la que resuelve los sujetos propuestos de la (8).
- Las secciones anteriores no se editan.

## 42. El FRENO T1 de la tanda final: las decisiones de la autora antes de la extracción (agregado del 18/10/2026)

Decisiones de la autora del 18/10/2026, recibidas a las 22:57:41, a las 23:06:01 y a las 23:57:41 (hoja de ruta de la mesa, §173 y §174).

- **El FRENO T1** (`data/experiment/tanda_final/t1/FRENO_T1.md`; paquete de la ejecutora `revision_tanda_final_FRENO_T1/`) entró tal como lo
  entregó la ejecutora en `5052364f`. Lo revisaron la autora, solo leyendo, y la mesa, que reprodujo sus cifras sobre copias
  (`decisiones_173_mesa/revision_T1/`, en su paquete):
  - la versión derivada se regenera igual, y las 78 rutas dan 78 de 78;
  - la E0 de los 98 da 490 de 490, y sus agregados coinciden con los de una E0 independiente;
  - el manifiesto, con su estimado recalculado TO por TO, y `sha256_para_T2.txt`, con 499 de 499;
  - el lanzador: su sha256, el tope, el SDK, el piso y la pausa;
  - la copia con `tanda_final/preregistro/`, que es la línea que la autora agregó al despacho; la mesa la probó sobre un repo de juguete;
  - la consulta de deprecaciones dio lo mismo a las 19:58 y a las 23:00.
  - Los seis `.log` de T1 no entraron: los ignora `.gitignore:47`, y están en el paquete de la ejecutora.
- **El estimado por TO, repartido por caracteres** (23:06:01, tal cual): «Va como precisión declarada del pre-registro firmado, con su causa:
  el registro de decisiones, §21, lo había fijado, el texto firmado no lo recogió, y la tanda 1 frenó dos veces por proyección con el
  estimado plano. El total, el tope, la U y la tarifa no cambian.»
  - La nota va al pie de `docs/preregistro_tanda_final.md` en este commit, como la propuso la mesa (23:57:41), con:
    - la simulación de la proyección;
    - la comparación de T5 contra las cifras del §3, con el reparto al lado;
    - el tope con cuatro decimales.
  - El cambio lo aplicó la ejecutora de T1 antes de lanzar (FRENO T1, sección 15). Los tres archivos dan, byte a byte, los que la mesa
    había calculado antes:
    - el manifiesto, `e9993b9d…`;
    - el lanzador, `462dfeab…`;
    - la lista, `12f7e217…`, con 499 `OK`.
  - Con el manifiesto nuevo:
    - el control de entradas da 13 de 13;
    - el armado con el perfil anterior a A3 frena en ri_bdp;
    - las tres pruebas en seco del lanzador salen con 0: la de punta a punta, `--autorizado-tramo-2` con el control entre tramos en FRENO
      y `--retomar-tras-pausa` a las 18:00 del 23/10;
    - las bases de la caché quedan iguales.
  - La ejecutora corrigió la hora de fin de T1 (22:47:04, con su ancla) y declaró dos errores propios más. Sus salidas están en
    `data/experiment/tanda_final/t1/entradas_reparto/`.
- **El sello del tramo 1 como respaldo,** aceptado con la salida stub que suma el `TextoOrdenado`, declarado (23:06:01, tal cual): «El freno
  en I4 es del stub, y el mismo ensamblado armó la tanda 1 con salidas reales.»
- **La prueba del acumulado de las tandas 0 y 1 con el tramo 1** (23:57:41): sí, como la propuso la mesa (`revision_FRENO_T1_tanda_final_mesa.md`,
  §5.2):
  - corre apenas el control entre tramos dé OK, sobre una copia, a USD 0 y sin frenar T2;
  - la consola muestra solo códigos de salida, invariantes, totales y sha256;
  - si falla, T2 sigue, y el sello del tramo 1 como respaldo queda sin habilitar hasta que un mandato lo arregle.
- **Las 13 unidades de snp_dd con el mismo texto** (6 grupos, 7 pedidos que salen de la caché, en el tramo 2) y el tope con cuatro decimales
  quedan como están, declarados.
- **`--autorizado-tramo-2` y `--retomar-tras-pausa`** se quedan, y se usan solo con una decisión de la autora por escrito. La interrupción
  manual del lanzador no se prueba en vivo.
- **Quién lanza T2** (23:57:41): la ejecutora, desde su sesión, como en la tanda 1. Si se corta, lo relanza la autora desde su terminal, con
  los comandos de la mesa (`decisiones_173_mesa/segui_t2/comandos_para_la_autora_T2_mesa.md`, en su paquete). La Mac queda enchufada y con
  la tapa abierta durante toda la extracción, porque `caffeinate -i` no evita que se duerma con la tapa cerrada.
- **Los commits durante T2** (23:57:41): sí, solo de documentos y de archivos que T2 no lee ni escribe.
  - Cada script de esos commits controla antes de commitear que no entra nada de:
    - las 78 rutas, el manifiesto de la extracción ni la E0 de la tanda final;
    - `data/experiment/tanda_final/t2/` ni `data/experiment/reextraccion_v2/corpus_tanda_final/`;
    - las tres bases de la caché ni `logs/cache_usage.jsonl`.
  - Ese control reemplaza el freno por un lanzador corriendo.
  - Mientras corre T2, la autora no corre `git checkout`, `pull`, `stash` ni `reset`.
- **El incidente de Neo4j** del FRENO T1 (§11) cierra con el FRENO de la parte 1 de U-NAV, §3:
  - la sesión de U-NAV cargó el acumulado de 19:11:26 a 19:12:23 y paró el contenedor y Docker Desktop a las 20:00;
  - en el volumen, 35 entradas cambian entre la foto de antes y la intermedia, que son los 35 cambios de T1, y ninguna después;
  - la más nueva es de las 20:00:33.
- Las secciones anteriores no se editan.

## 43. El control entre tramos de la tanda final en FRENO, y el tramo 2 autorizado (agregado del 19/10/2026)

Decisión de la autora del 19/10/2026, recibida a las 08:43:22 (hoja de ruta de la mesa, §175).

- **El FRENO** (`data/experiment/tanda_final/t2/FRENO_T2_parcial_1.md`):
  - la ejecutora lanzó T2 desde su sesión el 19/10/2026 a las 00:08:43;
  - el lanzador cerró los 30 TOs del tramo 1, todos con salida 0 y con el freno por modelo en OK, y paró a las 02:35:20 con salida 11;
  - el gasto fue de USD 12,856189, contra un tope de 151,5835.
- **El control entre tramos dio FRENO en un criterio,** los errores definitivos: 1, con umbral 0. Los otros tres dieron OK:
  - el costo por unidad, 0,021391 (umbral 0,03423);
  - las salidas inválidas de E1, 1 de 601 (umbral 1 %);
  - la proporción a la cola, 13 de 601 (umbral 3,01 %).
- **La causa,** identificada por la ejecutora a pedido de la autora, sin gastar (`data/experiment/tanda_final/t2/identificacion_error_ri_transpa/`):
  - es `ri_transpa::Sbloque1::chapeau_seccion`, de 21.712 caracteres;
  - su primer intento de E1 salió mal formado sin cortar, y los dos reintentos por forma cortaron en 8.192 tokens, porque el reintento
    por forma no escala el max_tokens (`data/experiment/reextraccion_v2/corpus_v2/runner_corpus.py:683-685`);
  - la partición y el tercer escalón se disparan solo cuando corta el primer intento (`:741-750`);
  - en el tramo 2 hay 25 unidades expuestas al mismo camino. La mesa lo reprodujo en el código.
- **La decisión de la autora,** tal cual: «Decidí seguir con el tramo 2 sin tocar el código», y se lo dejó por escrito a la ejecutora.
- **Quién relanzó:** la ejecutora, desde su sesión, con `--autorizado-tramo-2`, como el lanzamiento 1. Fue el 19/10/2026 a las 08:42:24,
  con el pid 70654.
  - Para este relanzamiento cambia lo de la §42 sobre quién relanza, que allí era la autora desde su terminal.
  - El lanzador saltó las fases cerradas del tramo 1. El control entre tramos volvió a correr a las 08:43:31 y dio FRENO, que quedó en el
    registro de avance, y el lanzador siguió con el tramo 2, como lo prevé esa opción.
- **La prueba del acumulado de las tandas 0 y 1 con el tramo 1** (§42): la autora la pidió aunque el control haya dado FRENO, porque el
  tramo 1 está completo. La corrió la mesa el 19/10/2026, sobre un clon de HEAD (`27bfaeb5`), a USD 0 y sin frenar T2
  (`decisiones_175_mesa/acumulado/`, en su paquete):
  - con el mecanismo del T3 de la tanda 1: la E0 combinada, la entrada de los 60 TOs y los manifiestos de ensamblado del acumulado de la
    tanda 1 y del tramo 1 de T1, juntos;
  - el completo y el sin cola salen con 0, con la doble corrida byte a byte igual y 0 nodos y 0 aristas fuera del modelo;
  - el completo da 23.671 nodos y 67.006 aristas, y el sin cola, 22.930 y 59.354;
  - la consola mostró solo códigos de salida, invariantes, totales y sha256, y el repo quedó igual;
  - el sello del tramo 1 como respaldo tiene probado su segundo grafo. Los `nombres_remision` del acumulado con el tramo 1 los fija su
    T3 (pre-registro, §7).
- **Lo que queda para decidir,** con las propuestas de la mesa en su paquete (`decisiones_175_mesa/propuestas/`):
  - cómo se tratan, antes del sello, las unidades que terminen así: extraerlas en una pasada aparte, o declararlas como faltantes y
    extraerlas después del sello;
  - el alta en el backlog del arreglo del runner (BKL-0050, propuesta): que el reintento por forma escale el max_tokens cuando corta.
- Las secciones anteriores no se editan.

## 44. Las unidades del reintento por forma que corta, la BKL-0050, N5 y los análisis de la §41 (agregado del 19/10/2026)

Decisiones de la autora del 19/10/2026, recibidas a las 09:33:40 (hoja de ruta de la mesa, §176), sobre las propuestas de la mesa de la
§175 (`decisiones_175_mesa/propuestas/`, en su paquete).

- **Las unidades que terminen con `salida_mal_formada_tras_reintento` porque el reintento por forma corta,** tal cual: «B. Se declaran como
  faltantes en el grafo evaluado y se extraen después del sello, con el arreglo, para la versión corregida. Lo decido ahora, con el tramo 2
  corriendo y sin saber qué unidades van a fallar.»
  - Entran en «Se declaran» del pre-registro, §8, con su id, sus caracteres y su causa, en T5.
  - La primera es `ri_transpa::Sbloque1::chapeau_seccion` (§43).
- **La BKL-0050** entra al backlog como la propuso la mesa, en este commit: el reintento por forma de E1 escala el max_tokens cuando corta.
- **El error 8 de la parte 1 de U-NAV** (la instancia vio en su consola la cuenta de una marca de E3 del acumulado; no está en ningún
  archivo y la autora no la vio): no cambia U-MED-VERIF y queda declarado, como en la §21.
- **El respaldo del tramo 1 no se sella en paralelo con el tramo 2,** tal cual: «con el v9, la tanda final se sella el martes en los tres
  escenarios, y la prueba del acumulado ya dio verde. Si el tramo 2 se corta o se demora, me lo proponés de nuevo.»
- **«El punto H»** son los análisis de la §41:
  - las remisiones sin resolver del acumulado por clase de causa, con su mandato para R5;
  - los vaciamientos de la (2);
  - la propuesta al backlog de la cola (E1-prompt);
  - F04b, F22 y F22b de la tabla de reprocesamiento, en un commit aparte.
- **N5 de U-NAV,** despachado desde `fuera_del_repo/unav_n5/`, con una línea de la autora al final, tal cual: «La fusión de los dos rankings
  de la familia 1 es RRF con k = 60, la propuesta de N2, fija antes de medir: no la ajustás.»
- **El control en memoria del sorteo de las FICHAS** (pedido de la §173), corrido por la mesa con un script que lee el sorteo en memoria y
  dice solo «sí» o «no» (`decisiones_176_mesa/fichas/`, en su paquete):
  - la muestra recalculada tiene 30, tantas como las fichas;
  - `nmcief::A1P2::S4`, la unidad del error 7 de la parte 1 de U-NAV, no está en la muestra. No pasa nada;
  - ninguna de las cuatro unidades de los ejemplos N3-E2v2 (opefci) y N3-E3v2 (ayccef) está en la muestra: los dos ejemplos se resuelven
    en N5, y ninguno se rehace.
- **La forma de fragmentos de la familia 1** (§6 bis del mandato de U-NAV) y un índice de fragmentos sobre los 30 TOs del acumulado: no
  estaban en el despacho de N5, y los índices del banco cubren solo los 5 TOs de desarrollo. Van en un despacho aparte (N5-F), PREPARADO
  por la mesa y PENDIENTE de la autora, sobre otra copia y en paralelo con N5, con el mismo analizador, el mismo modelo denso y la misma
  fusión. Su commit va con el de N5, después del sello de la tanda final y de A2.2.
- Las secciones anteriores no se editan.

## 45. Las marcas de E3 de la familia 6, los calibradores de U-MED-DESAMB y las preguntas de B6.3 (agregado del 19/10/2026)

Decisiones de la autora del 19/10/2026, recibidas a las 10:02:22 y a las 10:09:22 (hoja de ruta de la mesa, §177), y lo que la mesa dejó
preparado el 18/10/2026 (§172 y §173) y la autora corrigió.

- **Las marcas de E3 en los ejemplos de la familia 6 no se omiten,** tal cual: «El bloque de la familia 6 es lo que ve el agente en N6 y en
  B6.3, y ese texto quedaría en su prompt; además, la instrucción de la familia 6 le pide citar las marcas. El cegamiento ya está cubierto:
  las cuatro unidades no están en la muestra, y en el FRENO el bloque va solo por su sha256 y sus caracteres. En el pre-registro de N7, el
  bloque de herramientas va por su archivo y su sha256, y yo no lo abro hasta que cierre la lectura de U-MED-VERIF.»
  - La autora pegó el «seguí» de N5 sin el agregado de la mesa que las omitía. Pegó N5-F y U-PROC-HERENCIA en sesiones abiertas desde
    `fuera_del_repo/unav_n5f/` y `fuera_del_repo/proc_herencia/`.
- **Los calibradores v2 de U-MED-DESAMB,** leídos y sellados por la autora el 19/10/2026 a las 09:55:23
  (`fuera_del_repo/lectura_calibradores_desamb/sello_calibradores.txt`):
  - la hoja marcada da `a824fda9121774c6646eda0a941db2a4b8d017a7d86f391b144b426d16d9d4d4`, y la exportación,
    `615d766c842c0b0ab9d156f9eb19aece1b13f0546c51cabeff4d00f6de89b086`. La mesa controló los dos contra la carpeta y contra el sello;
  - el convertidor dio 17 de 17 entradas con clase y porqué, de 12 ítems;
  - con los calibradores sellados, la mesa abrió la clave aparte de la lectura (§32) y computó S1, S2, S3 y C1 con los estimadores
    sellados y la precisión de la nota 1 del diseño (`decisiones_177_mesa/desamb/`, en su paquete). Los resultados van a la revisión de
    la autora y no se registran en esta sección;
  - la hoja marcada y su sello entran en este commit, en `data/experiment/med_desamb/lectura/calibradores/`;
  - **la carpeta del juez,** preparada por la mesa fuera del repo (`fuera_del_repo/juez_desamb/`):
    - los ítems y el anexo de la §143 de la mesa, iguales a su sha256;
    - los calibradores cargados con el subcomando `calibradores` del juez, con la hoja marcada;
    - sus controles frenan hoy solo por lo que levanta la ventana: la autorización de la autora, el commit del sello de la tanda final y la
      extracción corriendo;
    - la cota de la humo, recalculada con la plantilla real, es de unos USD 0,49 (antes, 0,47), con la fórmula del juez y sus supuestos de
      tokens, NO VERIFICADOS;
    - la humo corre en la terminal de la autora, con el comando de la mesa, después del sello de la tanda final y sin ninguna extracción
      corriendo (diseño sellado, §8).
- **El diseño de las preguntas de B6.3,** tal cual, «salvo que la consulta de hoy diga otra cosa»:
  - «una muestra estratificada por tipo (dato directo, varios puntos con sus cuatro subtipos, y abstención), con las cuotas de N3, cerca del
    60 % de varios puntos, fijadas y justificadas por escrito antes de generar»;
  - «el N de cada tipo por un cálculo de potencia, con su script»;
  - «el resultado por tipo y un total ponderado por la proporción de cada tipo en la normativa de los TOs de B6.3, medida desde los PDF o la
    E0 por una instancia que no mira el grafo, antes de generar»;
  - «una hipótesis secundaria pre-registrada: el grafo mejora más en las de varios puntos»;
  - las notas de la §172 de la mesa (`decisiones_172_mesa/b63/`, en su paquete) y la cuota de cada tipo justificada desde la normativa, sin
    mirar el grafo ni resultados del agente (18/10/2026, §173);
  - el mandato, en BORRADOR de la mesa (`decisiones_177_mesa/b63/`, en su paquete), PENDIENTE de la firma de la autora.
- **Lo preparado del 18/10/2026, con la corrección de la autora:**
  - **T1 de la tanda final** se despachó con una línea de la autora al final del bloque, tal cual: «La exclusión de
    data/experiment/tanda_final/ en las copias no alcanza a data/experiment/tanda_final/preregistro/: esa carpeta sí va a la copia, porque
    la usan el lanzador y el control entre tramos.»
  - **U-MED-VERIF-FICHAS** se despachó dos veces:
    - la primera sesión, abierta en el repo, frenó en el paso 0 sin escribir nada;
    - la segunda se abrió desde `fuera_del_repo/tesis_escritura/U-MED-VERIF/`, con una línea de la autora al final que lo dice;
    - **desde ahora, todo despacho dice desde qué carpeta se abre su sesión.**
  - **Los 3 ejemplos de N3 se rehicieron:** la instancia había tomado «familia 6» como la necesidad 6 del cupo, y la familia 6 es la
    estrategia de navegación. Van como preguntas de varios puntos, con el mismo generador, sellados aparte y nunca medidos:
    - M09, que coincide con un ancla de EV2, y M17, que coincide con una de la tanda 0, se declaran y se quedan;
    - si un ejemplo nuevo coincide con un ancla de EV2 o de la tanda 0, se rehace.
  - **Para el mandato de las preguntas de B6.3:** la regla del CLAUDE.md de leer `docs/tablero.md` no aplica a la instancia ciega; la
    mezcla de tipos se fija y se justifica por escrito, con el resultado por tipo y el N de cada tipo por potencia.
- Las secciones anteriores no se editan.

## 46. La enmienda 2 a tripletas firmada, C1 con la re-aplicación única, el censo de C1 y las horas de la autora (agregado del 19/10/2026)

Decisiones de la autora del 19/10/2026, recibidas a las 12:13:24 (hoja de ruta de la mesa, §178).

- **La enmienda 2 al pre-registro de tripletas, firmada tal cual:**
  `docs/enmienda2_preregistro_evaluacion_tripletas_2026-10-17_desambiguacion.md`. El pre-registro recibe una nota fechada al pie que
  remite a ella, y su texto firmado no cambia.
- **El mandato de las preguntas de B6.3,** firmado a las 12:13:24 con sus seis decisiones del §9. Su texto firmado entra con la §47,
  después de que la autora resuelva la contradicción con Q4 (§8 y §9) que encontró la mesa al pasarlo en limpio.
- **No hay consulta pendiente,** tal cual: «el diseño es decisión mía y queda sin condición». La condición «salvo que la consulta de hoy
  diga otra cosa» de la §45 no rige.
- **C1 de U-MED-DESAMB entra con la re-aplicación única, antes del sello del sábado,** tal cual. La mesa lo controló contra las fuentes:
  - la enmienda 2, §0: «Si pasan, entran al grafo evaluado con la re-aplicación única del código antes de su sello»;
  - la enmienda 8 al protocolo, R3 (`54902301`, `:50-56`): las correcciones de código se re-aplican una sola vez al acumulado, antes de
    sellar el grafo evaluado;
  - y su R5 (`:66-72`): entra lo del grupo 2 que a las 12:00 del sábado tenga mandato firmado, código listo y su medición hecha.
  - S1, S2 y S3 no aplican (resultados de la mesa, `decisiones_177_mesa/desamb/`, en su paquete).
- **La relectura del censo de C1** en el acumulado de las tres tandas la hace la autora después de la extracción y antes de la
  re-aplicación única. Tal cual: «El censo no me muestra nada de una unidad de la muestra de U-MED-VERIF: lo controlás en memoria, como con
  nmcief. Si una colisión no se puede decidir sin una de esas unidades, no se une y se declara.»
  - El script de la mesa arma el censo con el C1 sellado y la muestra en memoria (`decisiones_178_mesa/censo_c1/`, en su paquete).
  - PENDIENTE de la autora, la precisión de la regla:
    - un nodo con todas sus procedencias en la muestra no se muestra, no se une y se declara;
    - una colisión que sin esos nodos queda con menos de 2 nodos o en menos de 2 documentos no se une, y se declara.
  - En el acumulado de las tandas 0 y 1 sin cola (`0435d41f…`), como cifra descriptiva: 10 colisiones con 37 nodos, de hasta 8
    documentos, y ninguna toca la muestra.
- **Las horas de la autora:** 7 por día hábil, tal cual.
- Las secciones anteriores no se editan.

## 47. El mandato de las preguntas de B6.3 con Q4, el censo de C1, los hubs, la primera ola y el N (agregado del 19/10/2026)

Decisiones de la autora del 19/10/2026, recibidas a las 12:58:40 (hoja de ruta de la mesa, §179), sobre lo que la mesa encontró en la
§178.

- **Q4 y el mandato de las preguntas de B6.3,** tal cual: «La mezcla del mandato reemplaza a Q4 para B6.3, salvo en dos cosas que quedan de
  Q4: sin preguntas de abstención, declarado como límite. Las olas de 32 van con 19 de varios puntos y 13 de dato directo, y los pesos del
  total ponderado son esos dos tipos, medidos en la etapa 1, y suman 1; la regla de caída por clase: si los documentos de una clase no
  tienen unidades que sostengan varios puntos, el lugar va como dato directo de esos mismos documentos, declarado. El resto de mis seis
  decisiones queda igual.»
  - El mandato firmado entra con este commit: `docs/mandatos/UPREG_B63_preguntas_por_tipo.md`.
  - La contradicción la encontró la mesa al pasarlo en limpio: el borrador de la §177 de la mesa no había integrado Q4 (§8 y §9).
- **El reparto por encima de 64,** tal cual: «Para N > 64, las olas van en más documentos, con 4 preguntas por documento.» Resuelve lo que
  dejaban abierto la §5 y la §7, punto 4. Va en el mandato.
- **El censo de C1:** la regla de la mesa (§46) queda confirmada, con un agregado, tal cual: «De un nodo que se muestra, tampoco se
  muestran las menciones que vienen de unidades de la muestra. Lo que no se une por esto se declara y vuelve para el grafo corregido,
  cuando cierre U-MED-VERIF.»
- **Lo que queda decidido hoy,** tal cual:
  - «en el censo, una colisión mal unida no se une, se declara y el resto de C1 sigue»;
  - «en la re-aplicación, si la medición frena por algo no declarado, eso queda fuera del grafo evaluado, declarado y al grafo corregido, y
    el resto entra».
- **Los hubs:** van las dos propuestas de la mesa (§178):
  - N7 y el pre-registro de B6.3 declaran que N6 se midió sin C1, cuántos nodos une C1 en el grafo evaluado y cuántos son hub, con la
    cifra de un script;
  - la revisión del FRENO de N5 controla que la lista de hubs se calcule al cargar el grafo.
- **La primera ola de B6.3** empieza el viernes 23/10/2026, después de los casos de la re-aplicación, tal cual: «así las diez decisiones con
  juicio mío van antes de que lea una pregunta».
- **El N,** tal cual: «Con N = 64 la potencia es 0,42, y un resultado nulo no diría nada. Quiero llegar a N_Q5.»
  - La mesa modela la opción de seguir la revisión el sábado después del corte y el domingo, con el grafo ya sellado, y firmar el
    pre-registro de B6.3 después del corte y antes de correrlo. Con eso se fija la hora límite del pre-registro, y la regla del miércoles
    calcula N_max hasta esa hora.
  - Si hace falta recortar para llegar a N_Q5, antes de bajar el N se recorta primero el juez de U-MED-DESAMB y después las claves del
    catálogo.
- Las secciones anteriores no se editan.

## 48. El mandato de Q8 firmado, la precisión del solapamiento en V y los dos FRENOs que volvieron (agregado del 19/10/2026)

Decisiones de la autora del 19/10/2026, recibidas a las 13:46:19 (hoja de ruta de la mesa, §180).

- **Los despachos de V y de P1,** pegados con su semilla tal cual (`B4-TRIPLETAS-V:sorteo:2026-10-07` y `B63-ETAPA1:muestra:2026-10-19`), en
  sesiones abiertas desde `fuera_del_repo/tripletas_v/` y `fuera_del_repo/b63_etapa1/`.
- **El solapamiento con U-MED-DESAMB en la etapa V** (enmienda 2 a tripletas, §1): la precisión de la mesa, tal cual, declarada en el acta
  del sorteo. «La misma norma como extremo de contenido» se cuenta por la misma unidad, el mismo predicado y el mismo sujeto.
- **El mandato de Q8, firmado** (`docs/mandatos/Q8_juez_de_B63_y_su_verificacion.md`), con las cuatro decisiones de su §5, tal cual:
  1. «el juez queda como está;»
  2. «la semilla de la verificación es gold-q12-verificacion-a22-v1;»
  3. «si la verificación no pasa, B6.3 se juzga con el juez, la cifra se informa con su acuerdo medido y todo lo dudoso va a mi lectura;»
  4. «el juez se verifica con respuestas de EV2 y de A2.2, que no son de varios puntos, y en B6.3 la mayoría lo son. La muestra de control
     de B6.3 (36 respuestas, 12 por brazo) se estratifica también por tipo, y el acuerdo del juez se informa por tipo.» El criterio del
     acuerdo en varios puntos, lo que se declara si no llega y el tamaño los propone la mesa, y van en el pre-registro de B6.3.
- **El FRENO de U-PROC-HERENCIA:** frenó por dos de los cuatro casos de su §3, punto 4 (cambia la cantidad de nodos y de aristas, y cambian
  `remite_a`). La decisión es de la autora, con la recomendación de la mesa, y lo que decida entra en el mandato de la re-aplicación única.
- **El FRENO de N5-F:** la mesa lo revisa después de U-PROC-HERENCIA y antes de N6.
- **El orden:** los FRENOs de V y de P1 apenas vuelvan; después, U-PROC-HERENCIA; y el modelo del punto 6 antes de los sorteos de B6.3, con
  la lectura de la autora de las 20 de Q8 después de A2.2.
- Las secciones anteriores no se editan.

## 49. El control del juez por tipo, la segunda pasada de U-PROC-HERENCIA, N5-F, la preparación de la etapa V y lo que vuelve de N5 (agregado del 19/10/2026)

Decisiones de la autora del 19/10/2026, recibidas a las 15:04:50, con un agregado a las 15:15:02 (hoja de ruta de la mesa, §181).

- **La muestra de control del juez de B6.3, por tipo, como la propuso la mesa (§180):**
  - en varios puntos, el piso de Q12 por criterio: Wilson inferior de al menos 0,85;
  - el acuerdo por respuesta se informa sin umbral;
  - 36 respuestas, con 9 de varios puntos y 3 de dato directo por brazo;
  - si no llega al piso: la cifra de varios puntos va con el acuerdo medido al lado, la hipótesis secundaria se declara como medida con
    ese juez, y lo dudoso va a la lectura de la autora.
  - Va en el pre-registro de B6.3.
- **U-PROC-HERENCIA, la opción D:** C1 sin uniones, y el detector de remisiones lee y resuelve con el punto que declaró E1. La autora
  autoriza tocar `data/experiment/reextraccion_v2/corpus_v2/r1_referencias.py`, solo detrás de la bandera. Los criterios de la segunda
  pasada:
  - con la bandera apagada, los grafos sellados salen byte a byte;
  - con la bandera, los nodos, `establecida_en` y `aplica_a` quedan iguales al sello, y cada `remite_a` que cambia tiene un extremo en un
    nodo de C1, con la cuenta;
  - la suite y las shapes, sin cambios;
  - las entidades duplicadas que C1 ya no une (7 de la tanda 0 y 5 de cirmo3) se declaran y van al grafo corregido.
  - El despacho lleva la comparación por id de nodo: C1 cambia el id de los nodos que corrige, porque el punto va en el id.
  - La segunda pasada va antes de que se mida la re-aplicación única, y D entra en su mandato.
  - Las anclas de F13 a F16 se recalculan sobre el código final y van con el commit de U-PROC-HERENCIA, después del sello de la tanda
    final.
- **N5-F, las cuatro propuestas de la mesa, tal cual:**
  - la aritmética del desempate se declara en N4;
  - la diferencia de la salida con N2 va en N4 y en N7;
  - los pre-registros de A2.2 y de B6.3 fijan la ruta del venv y el sha256 de su `pip freeze` (`24f4c064…`);
  - N6 cuenta las llamadas largas por brazo, y los pasajes que solos pasan los 10.000 tokens se declaran como límite de los dos brazos.
- **La preparación de la etapa V de tripletas** (FRENO de U-TRIP-V):
  1. **Los campos de la ficha quedan:**
     - el tramo del sujeto en `aplica_a` y `ejecuta`;
     - los avisos de E0;
     - la lista de lo que no va.
     La condición era que la condición de literal de cada tramo saliera del código, y sale: la calcula el validador de E1
     (`data/experiment/pyd_r2/code/validador_r2.py:1146-1155` y `:1282-1291`). La mesa la recalculó igual en 191 de 191 tramos y 49 de 49
     menciones. Las fichas no se regeneran. Si el piloto muestra algo que estorba, se ajusta en su FRENO (§3.5).
  2. «otros» queda sin muestra (su cuota, 0,26, redondea a 0), y p̂_w se informa con las dos cotas de ese estrato.
  3. **La semilla va como desvío declarado:**
     - quedó fijada en el despacho que la autora pegó el 19/10/2026 a las 13:45:02, antes del sorteo, sellado a las 14:23:55;
     - el §3.2 dice «fijada en la firma», y el texto de la semilla lleva la fecha de la firma, el 07/10.
  4. N = 3.967 y no 3.983, como nota, con su causa en el diff del re-sellado.
  Las tres van en una nota al pie del pre-registro, con este commit.
- **Las líneas 582 y 789 de este registro** ya están en la lista de lo que se limpia en la copia publicada del recurso (§37, con 8 líneas
  de 4 archivos, en `bd60f6c0`). En HEAD la búsqueda da esas mismas 8 líneas y ninguna más. La expresión no se repite en nada que vaya al
  repo.
- **La etapa 1 de B6.3 (P1):**
  - el pre-registro de B6.3 informa el total ponderado también con los pesos en los extremos de su intervalo, y la sensibilidad de la
    herencia, porque es una sola lectura;
  - lo que la autora pide decidir con la propuesta de la mesa, antes de los sorteos:
    - «excepción en un hijo» fuera de B6.3, con sus lugares a remisión;
    - el otro punto en un documento del grafo evaluado;
    - los diez criterios de lectura en la definición de los tipos.
- **R5, ya decidido:** el mismo tope en los dos brazos (U-NAV, §3), justificado solo con datos de desarrollo. La propuesta de la mesa va
  antes de la firma del pre-registro de A2.2.
- **N5** (agregado de las 15:15:02):
  - **la autora acepta del §12 de su FRENO, tal cual:**
    - la base y «todas menos la 6» toman el prefijo de 3 líneas, y «todas menos una» de las familias 1 a 5 lo resuelve N4/N6;
    - la familia 1 usa `BANCO_VENV_VECTOR`, y los pre-registros fijan esa ruta y su `pip freeze`, como en N5-F;
    - los tokens son una estimación por caracteres;
    - «no verificada» queda como el texto de N2;
  - **su lectura de la muestra de control de B6.3, o de cualquier respuesta de B6.3, va después de que cierre U-MED-VERIF,** porque las
    respuestas pueden mostrar unidades de su muestra (7 de los 77 documentos son de la tanda 1);
  - **lo que pide a la mesa, con su propuesta y su costo, antes de N6:**
    - los índices por punto fuera del repo, como `mcp_vector/indice/`;
    - un `desde` en `buscar_puntos` y en `buscar_pasajes`;
    - el costo de N6 y de B6.3 con el bloque real y el tope de R5;
    - la decisión 10 en fragmentos;
    - el cegamiento, si su lectura no entra en el calendario;
    - el commit de N5.
- **El orden:** la etapa V primero, porque destraba el gold; después P1, la segunda pasada de U-PROC-HERENCIA y R5 con el modelo del punto
  6, antes del miércoles; y N5 antes de N6.
- Las secciones anteriores no se editan.

## 50. La nota de la etapa 1 al mandato de B6.3, R5, el plazo del pre-registro de B6.3, el tope de N6 y los índices por punto (agregado del 19/10/2026)

Decisiones de la autora del 19/10/2026, recibidas a las 16:28:50 (hoja de ruta de la mesa, §182).

- **Lo que hizo:** corrió el 136 (`7cb770bd`), con push, y pegó la segunda pasada de U-PROC-HERENCIA (desde `fuera_del_repo/proc_herencia/`)
  y el despacho de U-NAV-DESDE (desde `fuera_del_repo/unav_desde/`), que lleva el `desde` en `buscar_puntos` y en `buscar_pasajes`, con
  A2.2 sin él. Abre el piloto de la etapa V.
- **La etapa 1 de B6.3:**
  1. la nota al mandato de las preguntas de B6.3 que propuso la mesa, tal cual, con un punto más: «P2 lee el PDF y la E0 de los
     documentos del grafo evaluado que son otro punto, incluidos los de la tanda 0, solo para anclar el otro punto. Sigue sin leer el
     grafo, las trazas, EV2, N3 ni ningún resultado de la tanda 0.» Así el §4 del mandato no choca con la regla del otro punto. La nota va
     con este commit, debajo de la firma;
  2. el cruce de los ext:: lo hace la mesa, como lo propuso: solo la columna `otro_punto` y la lista de documentos del grafo evaluado, con
     la tabla escrita a mano y sellada antes de calcular los pesos;
  3. la definición de los tipos, con los diez criterios de la etapa 1, tal cual, para el despacho de P2, la revisión de la autora y el
     pre-registro de B6.3. Va en la misma nota.
- **R5 y el pre-registro de B6.3:**
  4. **R5:** 30 llamadas en el prompt, `--max-turns` 32 y `--max-budget-usd` 1,80, iguales en los dos brazos, en A2.2, N6 y B6.3. Si H-B2
     caracteriza otra cuenta, `--max-turns` queda en tope + 2 de esa cuenta, declarado antes de la firma de A2.2;
  5. **la regla de N6, tal cual:** si la configuración elegida llega al tope en más del 10 % de sus sesiones en cualquiera de los dos
     brazos, N7 sube a 45, 47 y 3,30 en los dos, antes del sello, sin volver a correr N6, y se declara;
  6. **lo que informa el pre-registro de B6.3** por brazo y por tipo, tal cual:
     - las sesiones al tope;
     - las cortadas, con su sensibilidad;
     - las llamadas por sesión;
     - el costo por pregunta;
     - el contexto máximo;
  7. **el plazo del pre-registro de B6.3:** el lunes 26 a las 12:00, como techo. La regla del miércoles va en su v2, con el techo por
     tiempo y por dinero;
  8. **el tope de N6:** USD 100, con freno en 75;
  9. **el orden de los recortes por dinero,** como lo propuso la mesa:
     1. U-PRUEBA-GRAPHRAG;
     2. F1 en N6;
     3. el N de B6.3, por la regla v2;
     4. la base de N6 dos veces.
- **N5:**
  10. la línea del `.gitignore` local del banco (`data/experiment/banco_mcp/.gitignore`) para los índices por punto, `mcp_kg/indice_puntos/`,
      con las tres condiciones de la mesa: el manifiesto de cada índice, versionado fuera de la carpeta ignorada; un respaldo fuera del
      repo; y la misma regla para el índice del grafo evaluado. La línea entra con el commit de N5.
- **El cegamiento de las cuentas de E3 de la tanda final:** el pre-registro de la tanda final (§4.1) dice «ninguna cifra ni lista por
  estado de E3», también para la tanda final, y rige hasta que la autora lo levante. Cuando la mesa lee un resumen de T2, filtra los campos
  de gasto antes de imprimir. La mesa confirmó, por búsqueda, que la cuenta que mostró su consola el 19/10 no está en ningún archivo de su
  paquete, de su copia permanente ni de su hoja.
- **Para la ronda siguiente:**
  - el borrador del mandato de la re-aplicación única, para firmarlo el martes. Lleva D, C1 de U-MED-DESAMB, las claves del catálogo, el
    orden en que se aplican y cómo se usa la tabla de id viejo a id nuevo de D en el censo de C1 y en los controles del cegamiento, que van
    por código de id;
  - el despacho del juez de la etapa V, para cuando la autora selle su pool;
  - lo que queda de N5: su commit, con el de N5-F y el de U-NAV-DESDE, y el choque previsible en `grafos.py`.
- Las secciones anteriores no se editan.

## 51. El presupuesto como techo de trabajo, la regla del N sin techo por dinero y el respaldo de los índices (agregado del 19/10/2026)

Decisiones de la autora del 19/10/2026, recibidas a las 17:09:20 (hoja de ruta de la mesa, §183). Cambian lo que dicen la §50 (puntos 7 a 9)
y la enmienda 8 sobre el presupuesto: rigen desde acá.

1. **El presupuesto de USD 341 deja de ser un techo duro.** El criterio es la mejor evaluación posible. Para los modelos de la mesa y para
   las guardas del banco, el techo de trabajo pasa a USD 500 en total, que cubre el alto del v10 con N = 160 (472,86).
2. **La regla del N y los recortes:**
   - la regla del miércoles v2 va sin techo por dinero. El N de B6.3 lo fijan el tiempo hasta el plazo del lunes 26 a las 12:00 y las
     horas de revisión de la autora, hasta N_Q5;
   - no se recorta nada por dinero: U-PRUEBA-GRAPHRAG y F1 quedan, y la base de N6 va tres veces;
   - el tope de N6 pasa a USD 130, con freno en 100;
   - el tope de B6.3 lo fija la mesa con el mismo criterio, sobre su alto, y va en su pre-registro.
3. **El respaldo de los índices del banco** va en `fuera_del_repo/indices_banco/<grafo>/`, con `ditto` y verificado contra su manifiesto:
   - los índices por punto, con el commit de N5;
   - el índice de fragmentos de A2.1 (`data/experiment/banco_mcp/mcp_vector/indice/`), antes de A2.2. La mesa lo copió el 19/10/2026 y
     lo verificó a las 17:13:35: 9 de 9 archivos iguales a la fuente, y los sha256 que declaran sus manifiestos y su config BM25, iguales.
     Está en `fuera_del_repo/indices_banco/fragmentos_e0_r2b_desarrollo_A2_1/`, con su `manifest_respaldo.txt`.
- **Lo que la autora pide a la mesa antes de firmar el pre-registro de A2.2:**
  - qué más mejora la evaluación sin usar B6.3 para ajustar nada, en particular k corridas por pregunta en B6.3 frente a más N;
  - la confirmación de que la vía de cobertura de la etapa V está en el calendario y en el presupuesto, con su extracción y su orden.
- **El 137** corre cuando vuelvan los FRENOs de la segunda pasada de U-PROC-HERENCIA y de U-NAV-DESDE. Lleva esta sección.
- Las secciones anteriores no se editan.

## 52. El piloto de la etapa V, el juez de V, k corridas en B6.3, la cobertura de V y la segunda pasada de U-PROC-HERENCIA (agregado del 19/10/2026)

Decisiones de la autora del 19/10/2026, recibidas a las 17:35:09 (hoja de ruta de la mesa, §184).

- **El FRENO del piloto de V** (pre-registro de tripletas, §3.5):
  - la autora selló el piloto a las 17:13:32 (`hoja_piloto.csv`, sha256 `637239bea88191d85c3f32968000e1a0d3cfdd5d06b457fdceae5829cea19759`);
  - **la ficha queda como está.** Las tres fricciones, que no cambiaron ningún veredicto, quedan como notas del piloto:
    1. la ficha no trae la definición de cada predicado del esquema;
    2. los nodos Sujeto llegan sin descripción, y en `aplica_a` el alcance se decidió por la etiqueta y por el catálogo;
    3. en un bloque de cierre, lo heredado no trae la introducción del punto al que pertenece, y una remisión hacia atrás se resolvió en el
       PDF.
- **El juez de V,** que ve la misma ficha (§4.1) y no puede ir al PDF:
  - su prompt lleva la definición de cada predicado del esquema congelado, tal como la recibe la extracción, y la del catálogo para los
    Sujetos, cada una con su fuente. Así juzga con la misma base que la autora, sin tocar la ficha;
  - una remisión hacia atrás en un bloque de cierre va a «requiere adjudicación» y llega a la lectura de la autora;
  - la autora pidió el catálogo v3. La mesa señala que el grafo de V se extrajo con el prefijo r2b, que lleva el bloque del catálogo r2.
    El despacho lleva el r2, salvo que la autora diga otra cosa antes de pegarlo.
- **k corridas en B6.3, con la regla de la mesa:**
  - k = 3 si la variación entre corridas que midan la base de N6 y F1 da w mayor que 0,03; si no, k = 1;
  - con 3 sesiones en paralelo;
  - la nota al mandato de las preguntas de B6.3, con la métrica y la prueba, va con este commit;
  - el tope de B6.3, en USD 295, con freno en 225;
  - el lanzador en paralelo deja cada sesión aislada como hoy: su propio servidor MCP, su propio registro R1 y nada compartido entre
    sesiones. El test de aislamiento corre sobre el lanzador en paralelo antes de B6.3.
- **La cobertura de V se mueve a después de la firma del pre-registro de B6.3,** con su unidad U-TRIP-V-COB, si llegan antes del miércoles
  28 los resultados de cobertura de V y de T en el central. La mesa lo confirmó con su modelo (§184): con N = 128 y N = 160 entra en el
  central (márgenes de 6,4 y 3,1 h en el peor caso de las horas estimadas), y no en el lento.
- **La segunda pasada de U-PROC-HERENCIA:**
  - la versión de la ejecutora es la buena;
  - la diferencia con lo que esperaba la mesa sale de un nodo de C1 leído como grupo propio en el detector, como en el prototipo de la
    mesa: le daría al nodo remisiones que sin la bandera no tiene, y contradice el criterio. La mesa la cruzó: son 13 sin cola y 17 con
    cola, todas con origen en un nodo de C1;
  - **D entra así en el mandato de la re-aplicación única:** las remisiones propias de un nodo de C1 quedan como en el sello, y solo
    cambian las citas que llegan al punto corregido.
- **El 137** corre cuando vuelvan los FRENOs de la segunda pasada y de U-NAV-DESDE. Lleva esta sección.
- Las secciones anteriores no se editan.

## 53. El catálogo del juez de V, la nota del pre-registro de la tanda final, la cobertura en el escenario lento y el aislamiento de los brazos en paralelo (agregado del 19/10/2026)

Decisiones de la autora del 19/10/2026, recibidas a las 18:20:38 (hoja de ruta de la mesa, §185).

- **El catálogo del juez de V es el r2,** el bloque del prefijo r2b con que se extrajo el grafo de V:
  - de los 173 Sujetos del grafo de V (`66e745f5…`), 110 están en el bloque r2 y 102 en el v3. Los 102 del v3 están todos en el r2, y 63
    no están en ninguno (`sujetos_V_contra_r2_y_v3_mesa.py`, en el paquete de la mesa, §185, sobre los dos bloques de HEAD);
  - los 63 sin definición se juzgan por su etiqueta, y se declara: el código del juez marca en cada ficha los Sujetos sin definición (la
    marca no entra en el pedido), y el informe de V da cuántas fichas tienen alguno.
- **La nota al pie del pre-registro de la tanda final por `r1_referencias.py`** va en este commit, el siguiente al de la §52, para no
  rearmar aquel. `r1_referencias.py` es una de las 78 rutas del código de la cadena y entra como `ensamblar_tanda0.py`: con el commit de
  U-PROC-HERENCIA, después del sello. No hace falta una release nueva, porque es un módulo «solo código» (R19).
- **La cobertura de V va después de la firma del pre-registro de B6.3,** como la modeló la mesa (§184): entra en el central y no en el
  lento. Si se da el lento, la autora decide ese día entre tres alternativas:
  - la cobertura después del miércoles 28, declarada;
  - más horas de lectura;
  - el recorte del pre-registro de tripletas (la presencia de 50 y no de 100), que la mesa no recomienda.
- **El lanzador en paralelo del banco:** la base Neo4j y los índices quedan compartidos, de solo lectura. El test de aislamiento prueba
  también que una sesión del brazo de fragmentos no alcanza Neo4j ni el índice del grafo, aunque corra al lado de una sesión del grafo.
- Las secciones anteriores no se editan.

## 54. El commit de la §52, y `desde` en las búsquedas del banco: el brazo de fragmentos, el pie de `buscar_puntos`, la regresión con Neo4j y el manifiesto del índice por punto (agregado del 19/10/2026)

Decisiones de la autora del 19/10/2026, recibidas a las 18:36:53 (hoja de ruta de la mesa, §186), sobre el FRENO de U-NAV-DESDE.

- **El commit de las secciones 50 a 52** corrió, con su push (`a92bddb0`).
- **`desde` en el brazo de fragmentos:**
  - en F1, como lo dejó U-NAV-DESDE: dentro de la forma de la familia 1, igual que los filtros. Solo la configuración híbrida de F1
    declara `parametro_desde`;
  - en N7 y en B6.3, todos los brazos de fragmentos (BM25 o la híbrida, y el denso) llevan `desde`, igual que el grafo;
  - A2.2 corre sin `desde` en ningún brazo, y se declara.
- **El pie de `buscar_puntos`:** cuando el tope corta filas, dice desde qué posición seguir (`desde` = la primera fila que no entró),
  para que el agente no saltee resultados.
  - Es el único cambio de la salida con `desde=0`, va declarado, y los selftests se actualizan. Va antes de N6.
  - El texto lo fija el seguí de la unidad (hoja de ruta de la mesa, §186). No es más largo que el de hoy, así que las filas que entran
    no cambian.
- **Los bloques de herramientas no cambian:** la descripción de la herramienta ya explica `desde`.
- **Antes de N6 corren:**
  - el selftest entero de N5 con Neo4j, en los dos modos, con los mismos casos que en N5 más T11, y las salidas iguales salvo el pie;
  - los grupos de F1 con el índice del acumulado, con un solo proceso denso por vez.
- **El manifiesto del índice por punto:**
  - su sha256 incluye los tiempos de construcción, así que ninguna reconstrucción lo reproduce, aunque los datos salgan iguales;
  - la corrección va antes del commit de N5;
  - la mesa propone sacar los tiempos de lo que se hashea; la otra opción es que la config fije el sha256 de los datos. Decide la
    autora.
- Las secciones anteriores no se editan.

## 55. Los commits de las §53 y §54, la corrección A del manifiesto, los minutos del piloto y del pool, el sello del pool y lo pago siempre en secuencia (agregado del 19/10/2026)

Decisiones y acciones de la autora del 19/10/2026, recibidas a las 19:29:14 (hoja de ruta de la mesa, §187).

- **Los commits de las secciones 53 y 54** corrieron seguidos, con su push: `86541475` y `9950be88`.
- **El manifiesto del índice por punto va con la opción A:** los tiempos de construcción, fuera de lo que se hashea. El seguí de
  U-NAV-DESDE, que la lleva, se pegó tal cual en la misma sesión, a eso de las 19:00 (hora de la autora, NO VERIFICADA).
- **Los minutos de la etapa V:**
  - el piloto llevó 24 minutos (de 16:45 a 17:09, las 10 fichas);
  - el pool llevó 83 (de 17:40 a 19:03, las 20 fichas por componentes);
  - el calendario de los nueve lotes de 10 (§3.5 del pre-registro de tripletas), recalculado por la mesa con esas cifras: 24 minutos por
    lote a la tasa del piloto (3,6 h los nueve) y 41,5 a la del pool (6,2 h) (`calendario_lotes_V_mesa.py`, en su paquete, §187).
- **El pool está sellado:**
  - `hoja_pool.csv`, sha256 `097998e8777608503e0805b9819b9f0c848b4590bd0baae9176c4cbb8653c1f7`, con el sello a las 19:21:53. Los dos
    datos están en `sello_hoja_pool.txt`;
  - la hoja y su sello están copiados en `fuera_del_repo/tripletas_v_juez/insumos/`, sin nada más. La mesa controló el sha256 de la copia;
  - el despacho v3 del juez de precisión se pegó en una sesión nueva desde esa carpeta.
- **Lo pago va en secuencia, nunca al lado de una extracción:**
  - los dos pasos pagos del juez corren con T2 terminada;
  - sus dos comandos, y el humo pago de U-BANCO-PARALELO, controlan al arrancar que no haya una extracción corriendo, y frenan si la hay.
    El del juez se pide al revisar su FRENO.
- **El orden que sigue:**
  - U-BANCO-PARALELO (v3, con ese control) se despacha cuando termine el seguí de U-NAV-DESDE, nunca a la vez;
  - el mandato de la re-aplicación única (v2) se firma el martes.
- Las secciones anteriores no se editan.

## 56. El juez de precisión de V antes de su primera corrida, y los lotes de V (agregado del 19/10/2026)

Decisiones y acciones de la autora del 19/10/2026, recibidas a las 22:28:02 y a las 22:53:30 (hoja de ruta de la mesa, §188 y §189),
sobre el FRENO de U-TRIP-V-JUEZ (prompt v1 `314c62ac…`).

- **El commit de la §55** corrió, con su push (`729dc565`).
- **El juez de V, antes de cualquier corrida** (nota al pie del pre-registro de tripletas del 19/10/2026, en este commit):
  - la calibración va fuera de muestra, con un caso afuera por vez. Cada ficha del pool se juzga, con N = 3, con un prompt que trae los
    otros casos, sin el suyo y sin las notas que lo citan. El prompt del gold lleva todos, y el análisis por componente sale de esa
    corrida;
  - las notas del pool entran al prompt como el porqué de cada caso, según una hoja de la autora, sellada. Las filas 9, 17, 18 y 19, que
    citan fichas del gold, no pueden entrar tal cual. Las referencias a otros casos del pool se traducen por código. Las notas solo las
    lee la autora;
  - el hueco de la regla del §4.2 (sin contradicho, sin marca y con el sujeto o el predicado en `no_consta`): la arista no es correcta, y
    en el acuerdo del §4.6 cuenta como incorrecta. El informe separa las incorrectas por vía;
  - la regla de los Sujetos sin catálogo sale del prompt (0 de 20 y 0 de 100), declarada con el conteo;
  - los tres casos de la remisión (R1 a R3) entran, resueltos por la autora en una hoja con el formato y el sello del pool;
  - el tope de V pasa de USD 35 a 50, declarado. A las 22:28:02 la autora lo había puesto en 45, y a las 22:53:30 lo subió a 50, porque
    el peor caso de la mesa con una recalibración da 46,84 (§188);
  - el gold va con tope 16 y freno en 13: el freno en 11 quedaba por debajo del escenario alto con notas (12,14). La calibración va con
    lo que recalculó la mesa: tope 8,5 y freno en 6,5 (§188);
  - los dos comandos pagos llevan el control de la extracción de la §55, con su prueba. El control de insumos compara el registro de
    decisiones por el sha256 de su §52 y su §53, y no por el archivo entero, para que un commit nuevo no lo haga fallar.
- **Los nueve lotes de V** van tres por día, del martes al jueves.
- **Lo pago del juez** corre después de que termine T2 y de que la autora revise el FRENO del juez v1.1. El avance de T2 a las 20:21 (61 de
  68, todos con rc 0) es el que informó la autora, NO VERIFICADO.

## 57. La segunda etapa de U-NAV-DESDE, los índices de fragmentos, la entrega al repo y el grep con UTF-8 (agregado del 19/10/2026)

Decisiones de la autora del 19/10/2026, recibidas a las 22:53:30 (hoja de ruta de la mesa, §189), sobre el FRENO de la segunda etapa de
U-NAV-DESDE.

- **Lo que controló la autora:**
  - el manifiesto del paquete da 84 de 84;
  - de las 277 llamadas de `buscar_puntos`, 210 dan igual byte a byte y 67 cambian solo en el pie; con el pie de N5 restituido, el
    sha256 es el de antes;
  - F1 da 2.885 diferencias contra N5-F, todas clasificadas, y 0 en «otras».
- **Los manifiestos de los índices de fragmentos** llevan la hora y los tiempos de construcción, como el del índice por punto antes de la
  corrección A.
  - El brazo de fragmentos no se toca antes de N6, y queda declarado.
  - En N6 y en B6.3, la procedencia de los índices de los dos brazos se controla por el sha256 de sus datos (el índice BM25 y la
    matriz), que ya está en las configs.
- **La entrega de U-NAV-DESDE al repo,** con N5 y N5-F, en un commit que prepara la mesa, después de la corrida de A2.2 y del sello de la
  tanda final (§44). U-BANCO-PARALELO no se despacha hasta que la mesa diga si espera ese commit o necesita otra versión.
- **El grep de convenciones corre con un locale UTF-8** (`LC_ALL=en_US.UTF-8`). Sin él, «reuni[oó]n» y «seg[uú]n» no encuentran las
  formas con tilde.
- **El commit de la §55** no cambia; **el de la §56**, que no había corrido, se rearma con el tope de V en USD 50 y el gold con tope 16 y
  freno en 13.
- El avance de T2 a las 22:50 (66 de 68, todos con rc 0) es el que informó la autora, NO VERIFICADO.
- Las secciones anteriores no se editan.

## 58. El FRENO T2 de la tanda final, lo pago después de T2 y el bloque de la familia 6 (agregado del 20/10/2026)

Decisiones y acciones de la autora del 20/10/2026, recibidas a las 08:08:06 (hoja de ruta de la mesa, §190).

- **El commit de la §56 y la §57** corrió, con su push (`98edf948`).
- **T2 de la tanda final terminó** el 20/10/2026 a las 00:11:16 (`data/experiment/tanda_final/t2/FRENO_T2.md`, `8b9e2041…`; paquete de la
  ejecutora `revision_tanda_final_FRENO_T2/`):
  - **dos lanzamientos:**
    - el 1 (19/10, de las 00:08:43 a las 02:35:20, 146,6 minutos) cerró los 30 TOs del tramo 1 y paró con salida 11 por el control
      entre tramos (§43);
    - el 2 (del 19/10 a las 08:42:24 al 20/10 a las 00:11:16, 928,9 minutos), con `--autorizado-tramo-2`, volvió a pasar el control,
      que dio FRENO otra vez con el mismo sha256, y terminó con salida 0;
  - **los 98 TOs**, con rc 0 y el freno por modelo en OK: `claude-haiku-4-5-20251001` en E1 y `claude-sonnet-5` en E3;
  - **4.951 unidades:**
    - 4.870 aceptadas;
    - 80 en la cola, 13 del tramo 1 y 67 del tramo 2;
    - 1 error definitivo, `ri_transpa::Sbloque1::chapeau_seccion` (§43 y §44);
    - 0 sin destino y 0 ids repetidos, con la cobertura completa y exacta de la E0 en los 98;
  - **el costo:** USD 97,5983, contra un tope de 151,5835;
  - **los dos `NO_ABRIR_`**, solo por su sha256, iguales a los del FRENO.
  - **Lo controló la autora:** el manifiesto del paquete (34 de 34), el registro de avance, los `NO_ABRIR_` por su sha256 y el resumen,
    que no desglosa E3.
  - **Lo reprodujo la mesa** desde los archivos, sin gasto por documento ni nada de E3 (`decisiones_190_mesa/revision_T2/`, en su
    paquete).
- **Lo pago corre de a uno desde que terminó T2,** nunca al lado de otra corrida paga ni de una extracción.
  - Va primero el juez de V, después de que la autora revise su FRENO v1.1.
  - El orden del resto lo propone la mesa (PROPUESTA, `decisiones_190_mesa/calendario/`, en su paquete).
- **La prueba del acumulado de las tandas 0 y 1 con el tramo 1** (§42) es la que corrió la mesa el 19/10/2026 (§43), y sigue valiendo:
  - de los 516 archivos de las 30 carpetas del tramo 1, el más nuevo es de las 08:43:29 del 19/10, de la pasada del lanzamiento 2;
  - la prueba los copió después, y ninguno cambió desde entonces.
- **El bloque de la familia 6** (`data/experiment/banco_mcp/agentes/bloque_tools_kg.txt`, `cccfcefd…`, que entra con la entrega de
  U-NAV-DESDE), clasificado por código y sin mostrar su texto (`decisiones_190_mesa/bloque_familia6/`, en su paquete):
  - **las partes fijas** (las tres líneas de antes, las instrucciones de las herramientas y la introducción de los ejemplos) son, byte a
    byte, las del script que lo armó;
  - **los tres ejemplos** traen la pregunta, la respuesta y las salidas de las herramientas tal cual:
    - texto de la norma: el texto, los títulos y los comienzos de los puntos de la E0;
    - salida de la extracción: los nodos, con su label, su tramo y sus umbrales; las relaciones, con sus marcas; y las remisiones;
  - **la salida de la extracción toca 15 unidades:**
    - 8 de la tanda 0, todas de `ext`;
    - 7 de la tanda 1: `ayccef::2.8.1`, `ayccef::2.8.2`, `ayccef::2.9.3.8`, `ayccef::2.9.4.1`, `opefci::7.1`, `opefci::7.3.1.1` y
      `opefci::7.3.1.2`;
  - **ninguna está en la muestra de U-MED-VERIF,** recalculada en memoria con 30 unidades, como en la §44.
    - Los nodos mostrados tienen además procedencias en otras unidades, y 8 de ellas están en la muestra.
    - Las 8 vienen de un solo Sujeto compartido, que el bloque muestra en otro punto, sin umbrales y sin relaciones ni remisiones de esas
      unidades.
- **La unidad `ri_transpa::Sbloque1::chapeau_seccion`** sigue la §44:
  - falta en el grafo evaluado y se declara en T5;
  - se extrae después del sello, con el arreglo de la BKL-0050, para la versión corregida;
  - su mandato aparte lo prepara la mesa (BORRADOR).
- Las secciones anteriores no se editan.

## 59. El intervalo de las tripletas, lo que va al pre-registro de B6.3, la cobertura de V antes de su firma y P16 del pool (agregado del 20/10/2026)

Decisiones de la autora del 20/10/2026, recibidas a las 08:36:59, a las 08:43:12 y a las 08:51:12 (hoja de ruta de la mesa, §191, §192 y
§193).

- **Lo que va a tripletas y al pre-registro de B6.3** (08:36:59):
  1. **el intervalo de la precisión ponderada** de las tripletas pasa de Wald a Wilson con el n efectivo de Kish, como las tasas ponderadas
     de la tanda 1, en V y en T, incluida la cifra sobre las esenciales. Va en la enmienda 3 al pre-registro de tripletas (§3.6), que la
     autora firma antes de que se calcule cualquier cifra de V (PENDIENTE; la versión para firmar está en el paquete de la mesa, §191);
  2. **la pregunta del préstamo** se corre una sola vez con el agente final sobre el grafo evaluado, después de sellar el pre-registro de
     B6.3. No entra en ninguna cifra: sirve para mostrar en la tesis su traza, sus criterios y la atribución. Va al pre-registro de B6.3
     como corrida ilustrativa, y no puede ser una de las preguntas de B6.3;
  3. **de las fallas de la última clase de la atribución,** la autora lee caso por caso hasta 10, sorteadas con una semilla fijada en el
     pre-registro de B6.3;
  4. **el tope de llamadas** es el mismo para los dos sistemas y sale de los datos de desarrollo (N7). Sube si en N7 más del 5 % de las
     sesiones de cualquiera de los dos sistemas llega al tope, en lugar del 10 % de la §50, punto 5. B6.3 informa, por sistema, cuántas
     respuestas llegaron al tope;
  5. **los 600 fragmentos de la cobertura de T** salen solo de documentos del grafo evaluado y de unidades que están en él: ni de documentos
     que no entraron, ni de unidades en la cola, ni de la unidad con error. Si no, faltan por construcción y bajan la cobertura sin decir
     nada del grafo. Va al pre-registro de B6.3.
  - Las preguntas y los pedidos de ese mensaje los contesta la mesa (§191, en su paquete). Lo que pide decisión queda PENDIENTE.
- **La cobertura de V se hace antes de la firma del pre-registro de B6.3** (08:43:12), para cumplir el §9 del pre-registro de tripletas sin
  desvío. Reemplaza lo de la §52 sobre la cobertura de V, que la movía a después de esa firma, y el punto 6 del mensaje de las 08:36:59.
  - Se mide sobre el grafo de V (`66e745f5…`), así que no depende del sello de la tanda final.
  - Su unidad, U-TRIP-V-COB, no tenía mandato ni código. Se despacha con prioridad sobre todo lo que no esté en el camino del sello.
  - **El orden:**
    - primero lo que no gasta: el sorteo de los 300 fragmentos y de los 20 del pool de presencia (§5), sellado antes de leer; los
      subgrafos de presencia; el código y la corrida en seco;
    - después, el piloto pago de 10 que pide el §8, para medir los tokens reales y rehacer el costo;
    - después, la extracción abierta y el puntaje;
    - al final, la calibración y la corrida del juez de presencia.
  - **Lo pago** va en secuencia con los pasos pagos del juez de V, nunca al lado de otra corrida paga, con el control de la extracción de
    la §55.
  - **La red de seguridad:** si al llegar a la firma la cobertura de V no está cerrada, el pre-registro de B6.3 lleva los dos casos escritos
    de antemano (el juez de presencia pasa en V o no pasa), y el desvío del §9 se declara.
- **P16 del pool** (08:51:12; nota al pie del pre-registro de tripletas del 20/10/2026, en este commit):
  - la hoja del pool sellada no se toca, ni su sha256;
  - P16 lleva una corrección registrada: su `comp_modalidad` pasa de «sostenido» a «contradicho», porque la unidad impone un deber de
    reintegro y no veda el cobro, y la tripleta afirma una prohibición que el texto no dice. Con la corrección, su veredicto derivado pasa
    de correcta a incorrecta, y la importancia no cambia. Se justifica con el texto de la norma y con la regla R25 del prefijo, no con una
    etiqueta esperada (§4.7). Entra al juez por una hoja sellada de la autora;
  - P16 no entra como caso resuelto en el prompt del juez, y su nota va «no entra». En la calibración con un caso afuera por vez se juzga
    igual y se compara contra la marca corregida;
  - la convención de la autora para `requiere` queda escrita en la nota. Si entra al prompt como definición lo decide la autora
    (PENDIENTE), con lo que dice el prefijo al lado;
  - ninguna otra marca del pool cambia;
  - la lectura de R25 es del 20/10/2026, posterior a los sellos del piloto y del pool. Cómo se declara para el piloto lo decide la autora
    (PENDIENTE).
- Las secciones anteriores no se editan.

## 60. `requiere` con el prefijo, el caso de `prohibe`, el piloto, `ver_punto` sin corte, la familia 6, un incidente y la cobertura que cede (agregado del 20/10/2026)

Decisiones de la autora del 20/10/2026, recibidas a las 09:25:49 (hoja de ruta de la mesa, §194).

- **El commit de la §58 y la §59 y el de T2** corrieron, con su push (`257641e5` y `b17746be`).
- **Tripletas, antes de la primera corrida del juez de V** (nota al pie del pre-registro de tripletas del 20/10/2026, en este commit):
  - `requiere` va con la definición del prefijo, la misma vara con que se corrigió P16, y la convención de la autora no entra al prompt;
  - la autora revisa con esa definición sus marcas de P04, P11 y P12. Si alguna cambia, va en la hoja de la corrección con su motivo, como
    P16;
  - los lotes del gold los lee con la definición del prefijo;
  - el piloto: el informe de V da la precisión y el acuerdo con las 100 y, como sensibilidad fijada antes de cualquier cifra, sin las 10
    del piloto; si las dos dan otra decisión del §4.6, se declara y rige la de las 100;
  - un caso resuelto de `prohibe`, con una arista fuera de la muestra, cerca de la frontera entre prohibición y deber, con su hoja.
- **Las hojas del juez:** la autora selló la de notas y la de la remisión con el sellador v1_1 a las 09:21 (`hoja_notas_pool.csv`,
  `b1fe25d4…`; `hoja_remision.csv`, `f60553e9…`, los sha256 que informó la autora). Las verifica con el v1_1c, que lee el mismo formato
  de sello. Si una no pasa, se corrige en una copia con `_v2` en el nombre, que se sella sin pisar el sello anterior.
- **`ver_punto` no puede cortar el texto propio por debajo de lo que trae la herramienta de fragmentos.** No va como límite: se arregla
  antes de N6, con un mandato corto que prepara la mesa (BORRADOR) y la misma regresión que U-NAV-DESDE. Entra con la entrega de
  U-NAV-DESDE.
- **La familia 6:** los documentos de sus ejemplos no son documentos de B6.3, controlado por código sin abrir ninguna pregunta. ayccef y
  opefci están entre los 15 excluidos de la evaluación final, ext es de desarrollo, y ninguno está entre los 77 de la etapa 1 ni entre
  los 78 elegibles de O2. Los ejemplos quedan.
  - El brazo de fragmentos no tiene hoy ningún ejemplo en su descripción. Si la familia 6 entra en N7, lleva los mismos 3 resueltos con su
    herramienta (mandato de U-NAV-DISENO, decisión 10).
- **Un incidente, declarado:** en la §190 la consola de la mesa mostró el gasto por documento de T2 y cuántos documentos de la tanda final
  tienen archivos de reintentos y de copias de nota de E3. No está en ningún archivo, y no cambia U-MED-VERIF: su diseño está sellado y a
  la autora no le llegó nada.
- **El calendario:** si algo no entra, cede la cobertura de V, con la red de seguridad, y nunca el N de B6.3.
  - Con esa regla, la firma del pre-registro de B6.3 no espera a la cobertura. Se decide si la cobertura entra cuando la mesa empieza a
    escribir el pre-registro: si para entonces no cerró, va la red.
  - Las fechas son de la mesa (calendario v11, NO VERIFICADAS).
- Las secciones anteriores no se editan.

## 61. T3 con tres correcciones, la re-aplicación única, la enmienda 3 y `ver_punto` firmados, los ejemplos de fragmentos, el calendario con la variante B y un incidente (agregado del 20/10/2026)

Decisiones de la autora del 20/10/2026, recibidas a las 10:01:39 (hoja de ruta de la mesa, §195).

- **El 145** corrió, con su push (`eb5ad14b`). Sus dos archivos son los que preparó la mesa.
- **T3 de la tanda final:** la autora pegó el «seguí» de la mesa (`decisiones_190_mesa/t3/`, en su paquete) en la sesión de la
  ejecutora, con tres correcciones al final que mandan sobre su texto, tal cual:
  1. «las poblaciones de las vigilancias (1), (2), (3) y (7) y de la (12) se arman sobre ens_98_r2b_sincola (KG-TandaFinal-r2b-sincola)
     y no sobre ens_98_r2b, como en la tanda 1, que sorteó sobre su grafo evaluado sin cola»;
  2. «el mecanismo de (1), (3) y la (12) es el del T4 de la tanda 1 (data/experiment/tanda1/t4/scripts/poblaciones_t4t1.py y
     sorteos_t4t1.py), no el de su T3, cuya (12) se descartó en la §29»;
  3. «el paso 0 acepta el 145 arriba de los tres commits que nombraba».
  - **El criterio de la cola,** tal cual: «30, con las 13 del tramo 1 enteras (8 RI y 5 NG sin_raiz) y 17 de NG resto sorteadas entre sus
    67».
  - **Los dos momentos de lectura van juntos,** con todos los umbrales calculados antes de leer, declarado en el FRENO.
  - **Las tres correcciones concuerdan con lo commiteado:** la muestra de la (12) del T3 de la tanda 1 «no se lee y se rehace» en T4 (§29),
    y las 13 del tramo 1 más las 67 de NG resto son las 80 de la cola (`decisiones_190_mesa/cola/`). La mesa las controla en la revisión
    del FRENO T3.
- **La re-aplicación única, firmada** sobre el borrador v2 (`65531aaf…`): `docs/mandatos/UREAPL_reaplicacion_unica.md`, en el commit de
  esta sección. Lleva las decisiones 1 y 2 del §9 como las recomendó la mesa, la 3 con la precisión 1, y cinco precisiones que mandan
  sobre su texto (su sección «Firma», tal cual).
  - **La unidad de código de C1** es U-UNION-C1. Su despacho lo PREPARÓ la mesa (`decisiones_195_mesa/c1_codigo/`), para pegarlo después
    de los commits de T3 y a más tardar el miércoles 21: su paso 0 pide lo rastreado limpio, y T3 modifica
    `data/experiment/neo4j/grafos.py`.
- **La enmienda 3 al pre-registro de tripletas, firmada** tal cual, con la regla del estrato sin esenciales, sobre `2458eb86…`:
  `docs/enmienda3_preregistro_evaluacion_tripletas_2026-10-20_wilson_kish.md`.
  - Rige desde las 10:01:39, antes de cualquier cifra de V.
  - Su commit va después de los de T3, y la calibración del juez puede correr antes de ese commit.
  - Su script entra con el mismo commit (`data/experiment/tripletas_v/analisis/wilson_kish_tripletas_mesa.py`).
- **U-VERPUNTO, firmado** sobre `38f6812f…` (`docs/mandatos/UVERPUNTO_texto_propio_ver_punto.md`), con estas decisiones:
  - D-1: la opción A;
  - D-2: el texto largo con sus saltos de línea, como el corto, porque los puntos largos son listas y tablas y la herramienta de
    fragmentos los devuelve con sus saltos. El control T12 sigue igual;
  - D-3: «su texto entero»;
  - D-4 a D-6: como las propuso la mesa.
  - **A2.2 no usa `ver_punto`:** su brazo del grafo es `data/experiment/banco_mcp/mcp_kg/servidor_mcp_kg.py`, que expone solo las tres
    herramientas del harness congelado (`:63`). Las familias, con `ver_punto`, entran con el 142, después de A2.2 (§57). El arreglo
    sigue siendo antes de N6.
  - **Los ejemplos del brazo de fragmentos** se arman ya, a USD 0, en la misma copia, como la etapa b de U-VERPUNTO: los mismos 3 casos
    de la familia 6, resueltos con la herramienta de fragmentos. Entran solo si la familia 6 entra en N7 (mandato de U-NAV, decisión 10).
    El 142 espera solo a la etapa a.
  - **El despacho de U-VERPUNTO** lo PREPARÓ la mesa (`decisiones_195_mesa/verpunto/`). Los pasajes de los ejemplos salen de los 14 TOs
    excluidos de B6.3 que usa N3: los excluidos de la evaluación final y los de desarrollo
    (`docs/mandatos/UNAV_DISENO_navegacion_agente.md:315`).
- **El calendario,** tal cual:
  - «el viernes 23 pongo 8 horas, para que N7 llegue antes del corte del sábado a las 12:00»;
  - «la cobertura de V va con la red, y lo doy por decidido hoy: el pre-registro de B6.3 lleva los dos casos y declara el desvío del §9,
    y la cobertura cierra igual antes de los resultados»;
  - «A2.1 y A2.2 van con la variante B, en el repo después del sello de la tanda».
  - **Con el calendario v12** (`decisiones_195_mesa/calendario/`, en el paquete de la mesa; central, variante B, N = 128), N7 vuelve a
    pasar el corte: el sábado 24 a las 15:49 sin las remisiones y a las 15:54 con ellas. La firma de B6.3 queda el domingo 25 a las 19:20
    o 19:25, antes del plazo. Lo ata el jueves 22 de la autora: con una hora más ese día, N7 llega a las 09:28 o 09:42 y la firma, el
    domingo 25 a las 17:01. Lo decide la autora (PENDIENTE).
- **Un incidente, declarado:** en la §191, la consola de una bifurcación de la mesa mostró un mensaje de commit del 06/10/2026
  (`be6b074f`) con cuentas de copias de nota de E3 de la tanda 0. No cambia U-MED-VERIF: es texto de la historia del repo, no es de la
  tanda 1 ni de la tanda final, y a la autora no le llegó nada. No está en ningún archivo.
- **Los commits de esta ronda van después de los de T3.** Mientras corre T3, la autora no commitea.
- **Dos pedidos, para decidir a tiempo** (las respuestas, en el paquete de la mesa, §195):
  - **Las remisiones sin resolver** del acumulado de las tandas 0 y 1 (`decisiones_195_mesa/remisiones/`, por código y sin contenido):
    - son 906 citas con cola y 889 sin cola, en cinco clases del resolvedor, más 165 y 218 que no se resuelven por diseño;
    - una sola clase se corrige por código: la cita a un punto padre o a una sección cuyos subpuntos tienen nodos (368 y 366);
    - su mandato, BORRADOR (U-REMISIONES-SUBPUNTOS), lo firma o lo descarta la autora el miércoles 21;
    - 251 y 246 citan un TO de la tanda final y se resolverían solas al entrar (NO VERIFICADO hasta el acumulado de las tres tandas).
  - **Lo que necesita sellado el grafo evaluado:**
    - lo necesitan solo los índices del grafo evaluado y el pre-registro de B6.3, que fija sus sha256;
    - A2.2 no lo necesita: su brazo del grafo es el de desarrollo re-sellado (mandato de A2.1, D-A);
    - el 142 tampoco;
    - N6 tampoco: corre sobre el acumulado de las tandas 0 y 1 sin cola (`docs/mandatos/UNAV_DISENO_navegacion_agente.md:224`);
    - N7 lleva la cuenta de C1 del censo (§47);
    - la primera ola que lee la autora va después de los casos de la re-aplicación (§47).
  - **Hasta cuándo puede esperar una pieza** (central, variante B; el barrido de la mesa llega hasta el corte del sábado 24 a las 12:00):
    - con lo decidido hoy, hasta el jueves 22 a las 18:00 sin mover la firma, y esperando hasta el corte la firma tampoco se mueve;
    - con una hora más el jueves 22, hasta el jueves 22 a las 22:30 sin las remisiones, o hasta el viernes 23 a las 17:30 con ellas.
      Esperando hasta el corte, la firma se mueve como mucho 54 min o 1 h 13 min, siempre antes del plazo.
- Las secciones anteriores no se editan.

## 62. U-UNION-C1 con la regla del censo, la cobertura de V después de la firma de B6.3, ri_transpa firmado y los hubs de las remisiones (agregado del 20/10/2026)

Decisiones de la autora del 20/10/2026, recibidas a las 10:49:30 (hoja de ruta de la mesa, §196).

- **U-UNION-C1,** dos cambios antes de pegarlo, tal cual:
  1. «Falta la regla del censo de la §46 y la §47: un nodo con todas sus procedencias en la muestra de U-MED-VERIF no se une, y una
     colisión que sin esos nodos queda con menos de 2 nodos o en menos de 2 documentos no se une. La lista de códigos que no se unen no
     alcanza para la primera parte, porque va por código y no por nodo.» La bandera lleva una segunda entrada: la lista de los nodos que no
     se unen, la que escribe el censo como `NO_ABRIR_nodos_que_no_se_unen_por_la_muestra.json`, pasada con su sha256. La ejecutora no la
     abre ni la imprime. Tiene su rama en el selftest, sobre datos armados a mano, y su control en el encierro de la medición;
  2. el rsync de la copia excluye también `data/experiment/neo4j/volumen/` y las bases de la caché de E1 y de E3, como el de U-TRIP-V.
  - El despacho v2 lo PREPARÓ la mesa (`decisiones_196_mesa/c1_codigo/`). La autora lo pega después de los commits de T3.
- **U-VERPUNTO:** la etapa a, de acuerdo. Para la etapa b, la configuración base no filtra por TO, así que sus búsquedas pueden traer
  pasajes de documentos fuera de la lista de permitidos. La mesa los contó por código, sin mostrar ninguna consulta ni pasaje.
  - Con la regla del despacho, la configuración base trae 1 pasaje de un documento de B6.3 (en el ejemplo 1) y deja una cita sin
    sostener (en el ejemplo 3). La híbrida da 0 pasajes no permitidos y sostiene las 9 citas (`decisiones_196_mesa/verpunto_b/`).
  - La mesa propone la regla A: cada cita da una sola llamada, con `limite` 1, y en la base la consulta es el título del pasaje citado y
    su unidad. Con ella, las dos configuraciones dan 0 pasajes no permitidos y sostienen las 9 citas, y la híbrida da las mismas
    salidas que con la regla del despacho. La decide la autora (PENDIENTE). El despacho v2 con la regla A está PREPARADO
    (`decisiones_196_mesa/verpunto/`).
- **U-TRIP-V-COB,** tal cual: «la cobertura de V va con la red, después de la firma del pre-registro de B6.3, cierra antes de los
  resultados y se declara el desvío del §9». Su prioridad es la última. Los seis puntos de la mesa quedan como estaban.
  - El despacho v2 lo PREPARÓ la mesa (`decisiones_196_mesa/despacho/`): su etapa (a), USD 0, corre al pegarlo. Lo pago y las lecturas de
    la autora van después de la firma del pre-registro de B6.3.
  - Con el calendario v12b (`decisiones_196_mesa/calendario/`, central), la cobertura cierra el miércoles 28 a las 12:01.
- **U-REINTENTO-FORMA, firmado** sobre el borrador de la §190 (`d3d89a8a…`), con D-1 a D-4 como las propuso la mesa:
  `docs/mandatos/UREINTENTO_FORMA_reintento_por_forma_que_corta.md`, en el commit de esta sección. La extracción de la unidad va sola en
  el carril pago, después de las corridas de B6.3 (D-4).
- **Para el pre-registro de B6.3,** tal cual: «la cifra aparte sin las preguntas cuyo gold cae en la cola deja afuera también las que caen
  en esa unidad, que falta en el grafo evaluado». Esa unidad es `ri_transpa::Sbloque1::chapeau_seccion` (§43 y §44). Se informa cuántas
  preguntas salen por cada causa (`decisiones_196_mesa/b63/`).
- **Los hubs de las remisiones,** que la autora pidió antes de decidir el mandato el miércoles 21 (`decisiones_196_mesa/remisiones_hubs/`;
  solo cuentas, USD 0):
  - la regla es la de la familia 5 (`familias_nav.py` del 142, `:33-36` y `:62`). Sin la bandera, el grafo sin cola da el umbral 38, 216
    hubs y el sha256 de sus ids que espera la configuración de N6;
  - sin cola, con B y con C: umbral 48 y 218 hubs; entran 89 y salen 87. Con E: umbral 68 y 209 hubs; entran 142 y salen 149, y 107 de
    los que entran lo hacen solo como orígenes de las `remite_a` nuevas;
  - de las citas que se resuelven, tienen el origen o algún destino entre los hubs 116 con B y 105 con E, sin cola;
  - con cola, sin la bandera, umbral 42 y 226 hubs; con B y con C, 218 hubs (entran 50, salen 58); con E, 218 (entran 140, salen 148).
    Con cola no hay valor esperado con qué comparar (NO VERIFICADO).
- **El calendario v12b,** central:
  - sin la unidad de las remisiones, N7 llega el sábado 24 a las 09:42, antes del corte, aun sin la hora del jueves, y la firma de B6.3
    queda el domingo 25 a las 17:01;
  - con esa unidad, N7 necesita la hora del jueves 22 (09:34); sin ella, queda a las 15:54, después del corte.
- Las secciones anteriores no se editan.

## 63. Las remisiones firmadas con B, la regla A de U-VERPUNTO, U-TRIP-V-COB pegado, la unión de las dos banderas y el jueves con 8 h (agregado del 20/10/2026)

Decisiones de la autora del 20/10/2026, recibidas a las 12:42:26 (hoja de ruta de la mesa, §197).

- **U-VERPUNTO, etapa b:** la regla A, como la propuso la mesa. La autora pega la v2 del despacho después de la carga en Neo4j de T3.
- **U-TRIP-V-COB v2:** la autora lo pegó en una sesión nueva, desde `fuera_del_repo/tripletas_v_cob/`.
- **U-REMISIONES-SUBPUNTOS, firmado** sobre el borrador `09bbcf57…`: `docs/mandatos/UREMISIONES_SUBPUNTOS_remision_a_punto_padre.md`, en el
  commit de esta sección. Sus decisiones:
  - D-1: corregir la clase, como quinto paso de la re-aplicación;
  - D-2: la opción B y no la E, tal cual: «porque ver_remisiones agrupa las remite_a por el punto citado, así que en esa herramienta el
    agente ve lo mismo con B que con E, y B lo hace con la mitad de las aristas y menos hubs nuevos (89 contra 142 en el sin cola)»;
  - D-3 a D-5: como las propuso la mesa;
  - las cuentas de la medición pasan a ser las de B: 368 y 14.049 con cola, 366 y 13.856 sin cola, sin D-3, o la diferencia explicada.
  - **El motivo de la D-2, contra el código** (`familias_nav.py` del 142):
    - en la dirección «cita», `ver_remisiones` agrupa por el `destino` de la arista, que es la unidad citada (`:640` y `:647`). Desde el
      origen, B y E muestran la misma fila, y cambia solo la cuenta de aristas;
    - en «lo_citan», desde un subpunto (`:606-613`), E suma filas en los subpuntos de las ramas que B deja afuera.
    - La decisión no cambia.
  - Su despacho lo PREPARÓ la mesa (`decisiones_197_mesa/remisiones/`): corre sobre una copia y no espera a T3.
- **La unión de las dos banderas,** tal cual: «U-UNION-C1 y las remisiones parten los dos del ensamblar_tanda0.py de D, y cada uno le
  suma su bandera. Decime quién junta las dos versiones, con qué prueba y cuándo, antes de la corrida de la re-aplicación del jueves.» La
  mesa lo resuelve así:
  - **quién:** la ejecutora de U-REMISIONES-SUBPUNTOS, en una etapa b con su FRENO, después de que la mesa revise los FRENOs de
    U-UNION-C1 y de la etapa a;
  - **cómo:** con `git merge-file`, con el `ensamblar_tanda0.py` de D (blob `58e736db`) como base. A mano, solo la plomería de las
    banderas; cualquier otro conflicto frena;
  - **con qué prueba,** en los dos grafos del acumulado de las tandas 0 y 1:
    - todo apagado da los sellos, y solo D, la segunda pasada;
    - D con C1 da la corrida 4 de U-UNION-C1, y D con las remisiones, la de la etapa a;
    - D con las dos da, en cada pieza, las cuentas de esa pieza sola contra D, y ninguna arista cambia por las dos. Si cambia, frena y
      decide la autora (precisión 2 de la re-aplicación);
  - **cuándo:** con el calendario v12c (central), revisada el miércoles 21 a las 12:34. Va antes de los commits del jueves 22 a las 08:15
    y de la corrida de las 10:30.
- **El jueves 22, con 8 h,** tal cual: «Pongo 8 horas el jueves 22, para que N7 llegue antes del corte del sábado con la unidad de las
  remisiones.» Con el v12c (central, con el juez en su v1.2), N7 llega el sábado 24 a las 08:28, y la firma de B6.3 queda el domingo 25
  a las 16:44.
- Las secciones anteriores no se editan.

## 64. El FRENO v1.1 del juez de V y su v1.2: el modal, el §4.6 (i) y el control de la extracción (agregado del 20/10/2026)

Decisiones de la autora del 20/10/2026, recibidas a las 12:45:29 (hoja de ruta de la mesa, §198).

- **El juez de V cerró su FRENO v1.1** (`revision_UTRIP_V_JUEZ_v1_1/`, sesión `539f236b`, manifiesto `5d3c6dd0…`). La autora le pegó un
  «seguí» v1.2 con tres decisiones, tal cual:
  1. «En el modal del veredicto, las dos vías de la incorrecta votan juntas, como incorrecta, igual que en el acuerdo de dos clases del
     §4.6: el modal sale de correcta, incorrecta y adjudicacion, con mayoría de 2 de 3, y la vía se informa aparte («mixta» si son una y
     una). Rige en la calibración y en el gold.»
  2. «El §4.6 (i) con un número de decididas distinto de 100 va en proporción, 0,84, con el límite inferior de Wilson al lado. Entre 80 y
     100 decididas coincide con exigir un límite inferior de Wilson de al menos 0,75, salvo con 98, donde la proporción es más
     exigente.»
  3. «El patrón del control de la extracción (§55) no ve un script lanzado con una ruta absoluta con espacios, como «INGENIERIA IA».
     Arreglalo en el control compartido, con su prueba, antes de la extracción de ri_transpa y de lo pago de la cobertura.»
- **La revisión de la mesa** (`decisiones_198_mesa/juez_v/`, en su paquete):
  - lo verificable se reproduce: el paquete (33 de 33), los sellos de las cuatro hojas, las secciones del prefijo, el sha256 del prompt
    (`4cf2e537…`), los 23 casos y las 23 notas, y el costo (13,01, bajo los topes de la §56);
  - el selftest, la corrida en seco y el armado del prompt leen `tripletas_v_juez/insumos/`, que es de lectura de la autora. La mesa no
    los corrió: sus resultados salen de las salidas del paquete (110 de 110, y `ok: true`);
  - la decisión 1 cabe en el texto firmado: el §4.4 agrega por veredicto modal sobre el veredicto computado, y la nota del 20/10/2026 ya
    cuenta la vía de `no_consta` como incorrecta en el acuerdo de dos clases;
  - **la decisión 2, controlada por script:** entre 80 y 100 decididas, las dos reglas coinciden en 17 de los 21 valores de n. Difieren
    en 82, donde es más exigente Wilson, y en 93, 98 y 99, donde es más exigente la proporción. La regla queda como la decidió la
    autora;
  - las otras tres lecturas del §4.6 que declara la ejecutora (la importancia en proporción, la ponderada sobre los estratos con
    decididas de los dos lados, y la (iii) sobre todas las incorrectas de la autora) quedan como lectura declarada (PENDIENTE de la
    autora).
- **El control de la extracción v2** (`decisiones_198_mesa/control_extraccion/`, en el paquete de la mesa):
  - acepta como primer argumento una ruta absoluta con espacios, mientras no siga una opción ni termine antes otro script;
  - con las líneas de la v1 da lo mismo que la v1, y su selftest pasa;
  - con un proceso de prueba en una carpeta con espacio, la v1 no lo ve (sale con 0) y la v2 lo frena (sale con 1).
  - **Desde ahora lo usa todo comando pago y toda extracción:** la v1.2 del juez, la etapa a2 de U-TRIP-V-COB y la extracción de
    ri_transpa. El control del juez de V (`control_extraccion_v.py:24`) llevaba el patrón de la v1, y sus comandos lanzan Python con la
    ruta absoluta de su carpeta, que tiene un espacio.
- **La calibración paga** corre después de las revisiones del FRENO v1.2, la de la mesa y la de la autora.
- Las secciones anteriores no se editan.

## 65. El juez de V en sus v1.2 y v1.3, y el §4.6 (i) en proporción (agregado del 20/10/2026)

Decisiones de la autora del 20/10/2026, recibidas a las 13:46:27 (hoja de ruta de la mesa, §199).

- **El juez de V pasó por dos rondas más,** las dos en FRENO, que revisó la autora:
  - **la v1.2** (`revision_UTRIP_V_JUEZ_v1_2/`, manifiesto `3df1a39d…`), tal cual: «el modal del veredicto con las dos vías de la
    incorrecta juntas, y la vía aparte («mixta» si son una y una). Para que la vía saliera bien, autoricé un cambio mínimo en
    correr_juez_v.py: la vía sale del modal de juez_v, incorrectas_por_via cuenta las tres, y sale el conteo «sin consenso con todos los
    votos incorrectos», que con el modal nuevo no puede darse.» Su selftest da 119 de 119;
  - **la v1.3** (`revision_UTRIP_V_JUEZ_v1_3/`, manifiesto `3f3b261f…`), tal cual: «el control de la extracción con tu patrón v2, que
    copié a sus insumos (ahora son 13 archivos); el control de insumos admite solo la fixture de la suite que modifica T3; y las lecturas
    del §4.6 sobre las fichas que el juez decide, como dice el texto firmado. La (ii), cruda y ponderada, compara las dos precisiones
    sobre las mismas fichas, las que deciden los dos, y la ponderada va estrato por estrato sobre esas fichas. La (iii) va entre las que
    el juez decide, con la cuenta sobre todas al lado como información. La importancia va en proporción, 0,60 y 0,90.» Su selftest da
    129 de 129, y el prompt, los 20 de la calibración y la corrida en seco dan igual que en la v1.1.
- **La revisión de la mesa** (`decisiones_199_mesa/juez_v/`, en su paquete):
  - los dos paquetes verifican (15 y 13 archivos);
  - el código del modal hace lo decidido, y ninguna rama sigue comparando con los cuatro valores viejos;
  - el patrón del control del juez es, por código, el de la v2 de la mesa, y su copia en `insumos/` lleva el sha256 de la mesa
    (`e3c41d93…`);
  - **el control de insumos admite solo la fixture, y T3 también modifica `data/experiment/neo4j/grafos.py`** al cargar Neo4j. No
    frena lo pago, porque los comandos pagos corren solo el control de la extracción. Si se vuelve a correr a mano después de esa carga,
    no pasa, y se lee como una modificación de T3 declarada;
  - T3 no es una extracción ni un paso pago: la calibración puede correr con T3 en marcha, de a un paso pago por vez;
  - ningún script del juez calcula el intervalo de la enmienda 3, que va en el informe de V, después del commit de esa enmienda.
- **El §4.6 (i),** tal cual: «tenías razón, la proporción y el Wilson de 0,75 difieren en 4 de los 21 valores entre 80 y 100. La regla
  queda en la proporción, 0,84, como la decidí.»
- **Lo pago:** la calibración del juez corre con esta revisión, y después el gold, de a uno. Entre los dos, la mesa propone mirar el
  análisis de la calibración. El §4.7 admite una sola recalibración, declarada, con casos del pool y nunca con las 100.
- Las secciones anteriores no se editan.

## 66. El FRENO T3 parcial de la tanda final: la R23, los manifiestos del tramo 1, el derivador de 60, los umbrales de T4 y lo que queda a la vista (agregado del 20/10/2026)

Decisiones de la autora del 20/10/2026, recibidas a las 13:50:10 (hoja de ruta de la mesa, §200).

- **T3 volvió con un FRENO parcial** (`revision_tanda_final_FRENO_T3/`, sesión `afadde2e`, manifiesto `07068d6f…`): el gate no pasó
  solo por la R23 del selftest de claves, cuyo TO (`snp_psp`) extrajo T2. Para no frenar el camino al sello, la autora le contestó, y T3
  sigue con los puntos 5 a 7 con cinco decisiones, tal cual:
  1. «la R23 y la V23, declaradas no aplicables después de T2, con la causa por script de su sección 3.4; el gate se juzga sin ellas»;
  2. «los manifiestos del tramo 1, con la raya, por la regla de la §19 y la enmienda 9, punto 8 (el kg.json es el mismo)»;
  3. «el derivador adaptado del acumulado de 60, declarado»;
  4. «los umbrales de T4, del script de la mesa sin cambios, con su tasa base de la tanda 0, como dice el §6; la tanda 1 al lado, como
     información»;
  5. «unidades_a_la_vista_T4.json, con la regla del seguí y la del T4 de la tanda 1 al lado».
- **La revisión de la mesa** (`decisiones_200_mesa/t3/`, en su paquete):
  - se reproduce: el paquete (268 de 268), los ocho ensamblados con su doble corrida, los diez sellados, el acumulado con el tramo 1
    contra la §43, el gate sin la R23 y la fixture (solo las ocho entradas nuevas);
  - **el punto 3 cierra:** el derivador adaptado hace lo mismo que el de la mesa, con la variante pasada con su fuente y el freno de la
    §19, y la medición del propio T3 da las mismas 23 distintas;
  - **el punto 4 cierra, y es la lectura del pre-registro:** los umbrales salen del script sellado (`f4723e5a…`), que mide contra la tasa
    de la tanda 0, con los pesos reales de la tanda final (`4de7f2a7:docs/preregistro_tanda_final.md:231-235`).
    - **Con una precisión:** el mismo §6 fija como línea de base de las lecturas la de la tanda 1, de su T4, con la tanda 0 al lado
      (`:239-244`).
    - En el informe de T4, cada tasa va contra la de la tanda 1, con la tanda 0 al lado.
    - Lo que decide la atención y el freno son los umbrales del script sellado. Los umbrales con la base de la tanda 1, si se calculan,
      van como información;
  - el punto 5 no pide nada: la regla del «seguí» es la del T3 de la tanda 1.
- **El cambio del TO de la R23,** tal cual: «El cambio del TO de la R23 en selftest_clave_cache.py (:132-133) ponelo en U-UNION-C1 v2,
  que ya toca ese archivo, así tiene un solo dueño, con un TO que no esté en ninguna tanda.»
  - Va en el despacho v3 de U-UNION-C1 (`decisiones_200_mesa/c1_codigo/`), con una regla fija: el primero, en orden alfabético, de los
    TOs de la partición b584 que no están en ninguna de las tres tandas. La mesa cuenta 29 de 152.
  - La salida del selftest de claves sin cuentas pasa a ser la referencia nueva, con su sha256.
- Las secciones anteriores no se editan.

## 67. La etapa a de las remisiones a un punto padre, revisada, y el acotamiento del subgrafo de la cobertura de V (20/10/2026)

Decisiones de la autora del 20/10/2026, recibidas a las 14:49:10 (hoja de ruta de la mesa, §201).

- **El FRENO de la etapa a de U-REMISIONES-SUBPUNTOS** (`revision_UREMISIONES_SUBPUNTOS_a/`, sesión `aab0e5be`, manifiesto `6564afbd…`)
  llegó sin casos de freno. La mesa lo revisó (`decisiones_201_mesa/remisiones/`, en su paquete):
  - el paquete da 63 de 63;
  - las cuentas de B y los hubs se reproducen con los scripts del paquete, sobre una copia, campo por campo: con D-3, 368 citas y 14.047
    `remite_a` nuevas con cola, y 366 y 13.854 sin cola, con 322 pares que ya eran `remite_a` en cada grafo; sin D-3, las firmadas (368 y
    14.049; 366 y 13.856); los hubs, de 226 a 218 con cola y de 216 a 218 sin cola, con los sha256 de la mesa;
  - la foto del repo da igual antes y después de la reproducción.
- **Lo que controló la autora, y queda así:**
  - **S30 y S31** se juzgan con la E0 con las partes por corte, la que rige en el gate de T3 de la tanda 1 (`veredicto_gate_t3f.md`,
    «E0 con las partes (rige)», acumulado `a9ff9b7b…`). Así dan PASS con 0 en las ocho corridas; con la E0 plana, S31 da FAIL igual que en
    el sello, y no cambia;
  - **el error propio 6 de la ejecutora** (dos salidas sobrescritas por el script de comparaciones revisado) **alcanza como está**: las
    salidas son deterministas y la mesa las reproduce; el cambio no movió ninguna cifra, y la salida entregada sigue mostrando S31 en FAIL
    con la E0 plana. Desde la etapa b, ninguna salida se pisa;
  - **la regresión sin entrada en la fixture** se computa como el §5.7 del FRENO de U-PROC-HERENCIA-2, con
    `regression_kg.computar_regresion` y la entrada del grafo sellado, y es lo que hace el script de la ejecutora (`:253-265`). El «seguí»
    de la etapa b nombra ese FRENO entre lo que puede abrir;
  - **S21 sube por construcción:** de 419 a 14.466 incoherentes con cola y de 388 a 14.242 sin cola, exactamente en las `remite_a`
    nuevas. La regla 1.5 deja como destino la unidad citada (el punto padre o la sección), no el subpunto en el que está anclado el nodo.
    En N7 y en la tesis no se lee como un defecto;
  - **con D,** las `remite_a` nuevas son 14.133 con cola y 13.940 sin cola (sin D, 14.047 y 13.854); 86 pares aparecen solo con D y 104
    con otra procedencia, todos con un extremo en un nodo de D, y ninguna arista cambia por las dos piezas;
  - **la cifra de N7 y del pre-registro de B6.3 (D-5) sale de la corrida 5 de la etapa b** (D, C1 y las remisiones), porque el grafo
    evaluado lleva las tres piezas.
- **La etapa b** va con el FRENO de U-UNION-C1 v3, que se pega después de los commits de T3 y del 146 (su foto del repo tiene que dar igual
  antes y después). Su «seguí» lleva los sha256 de U-UNION-C1 v3, que completa la mesa al revisar ese FRENO. En el escenario central del
  calendario v12d (`decisiones_202_mesa/calendario/`), las dos entran antes de los commits del jueves 22 a las 08:15; en el lento, no.
- **El subgrafo de la cobertura de V, acotado (U-TRIP-V-COB, FRENO a2, punto 4.2):** un subgrafo de los 300 (C253, el chapeau de una
  sección, 248.045 caracteres en la forma compacta) pasaba los 68.298 del §8. La autora decidió **P1, solo los hijos directos, para toda
  la vía de cobertura (V y T)**, como el acotamiento del §8, declarado antes de ver ninguna salida de un modelo. Con P1 quedan 0 de 300, 0
  de 330 y 0 de 1.491 sobre el umbral, y cambian 10 de los 300 (cifras del FRENO a2, que la mesa no revisó; NO VERIFICADAS por la mesa).
- **El dimensionado del §8 no se reproduce, y no se sabe con qué serialización se midió** (`decisiones_201_mesa/tripletas_cob/`):
  - el §8 da, para el subgrafo de presencia, mediana 21.126, media 30.196 y p90 68.298 caracteres, sobre el grafo `2922b72d…`, la E0 r2b de
    desarrollo y un sorteo provisorio con otra semilla, con «nodos y aristas de la unidad y sus descendientes». No dice la serialización,
    y el script que dio esas cifras no está en el repo (el commit que las trae, `865a5b2f`, solo cambia dos documentos);
  - la ejecutora mide, sobre las 1.491, la forma compacta (la que ve el juez) con mediana 4.879 y p90 11.218, y la completa con 192.080 y
    274.343 (FRENO a2; NO VERIFICADO por la mesa);
  - la mesa mide la población entera en ocho variantes (las dos formas, con los ancestros que heredan texto o solo la unidad y sus
    descendientes, y los dos grafos, el del §8 y el de V): ninguna da las cifras del §8. La compacta da medianas de 2.407 a 4.636, y la
    completa, de 181.525 a 191.694. El §8 queda entre las dos;
  - **lo que rige:** la vía de cobertura mide y declara los tamaños en la forma compacta, que es la que ve el juez, y el umbral de 68.298
    vale como el acotamiento que decidió la autora, con P1. El informe de V declara la diferencia;
  - **error de la mesa:** el docstring de su script de costo de la §192 decía que la forma completa era «la forma del dimensionado
    provisorio del §8», sin ancla, y las cifras lo contradicen (la completa es unas nueve veces la mediana del §8). El despacho de
    U-TRIP-V-COB comparó con ese umbral tamaños en la forma compacta. Queda corregido acá; el docstring, en el paquete de la mesa, no se
    edita.
- **Va una nota fechada al pie del pre-registro de tripletas** con P1 y la diferencia del dimensionado. El texto firmado no cambia.
- Las secciones anteriores no se editan.

## 68. El FRENO T3 final de la tanda final, sus commits y la lectura de T4 (agregado del 20/10/2026)

Decisiones de la autora del 20/10/2026, recibidas a las 14:54:11 (hoja de ruta de la mesa, §202).

- **El FRENO T3 final** (`data/experiment/tanda_final/t3/FRENO_T3.md`, `fae35662…`; paquete `revision_tanda_final_FRENO_T3/`, manifiesto
  `c9a0bbc6…`; el parcial quedó en `revision_tanda_final_FRENO_T3_parcial/`). La mesa lo revisó (`decisiones_202_mesa/t3/`, en su
  paquete): el paquete da 375 de 375, y sus controles por script dan:
  - `grafos.py` solo agrega las dos entradas de la tanda, con el sha256, los nodos y las aristas de su `kg.json`, y las 15 de HEAD siguen
    iguales;
  - la fixture conserva las 4.094 claves de HEAD, y las 2.272 nuevas son todas de los ocho grafos nuevos (el control del §9, punto 3, del
    pre-registro de la tanda final);
  - los cuatro `.gz` dan el sha256 de su `kg.json`, las ocho muestras dan el suyo y suman 216 fichas, y la versión derivada de T4 no tiene
    ningún hueco.
  - Las cinco decisiones de la §66 están aplicadas como se decidieron.
- **Los commits de T3, en dos, como en la tanda 1** (`eb0711a1` y `050940b0`), PREPARADOS por la mesa y PENDIENTES de la autora:
  - **el primero:** los archivos nuevos de T3, `grafos.py` y la fixture. Los cuatro `kg.json` de más de 100 MB no entran: van su `.gz` y su
    sello, como en la tanda 1 (§30);
  - **el segundo:** el hash corto del primero en el `commit_sellado` de las dos entradas nuevas de `grafos.py`, que T3 dejó en
    «PENDIENTE». Es lo que pide el §7 del pre-registro de la tanda final («con `commit_sellado` en el commit siguiente»,
    `4de7f2a7:docs/preregistro_tanda_final.md:257`). La base de Neo4j conserva «PENDIENTE» en `KG_Meta` hasta la próxima carga.
  - **El orden de la fila:** los dos de T3, el 146 v5, y después U-UNION-C1 v3, el «seguí» de T4 y la etapa b de las remisiones.
- **Lo que queda a la vista:** `unidades_a_la_vista_T4.json` deja 3.695 de las 4.951 unidades de la tanda final con la regla del «seguí»
  (la del T3 de la tanda 1), y 224 con la del T4 de la tanda 1. La causa: la regla del «seguí» suma las unidades de procedencia de los
  nodos TextoOrdenado y de los Sujeto con más de una unidad de procedencia que muestran las fichas, y la del T4 de la tanda 1 no. Las
  3.695 son de 93 TOs, todos de la tanda final y ninguno de la tanda 1 (lo controlaron la autora y la mesa, por código), así que no tocan
  la población de U-MED-VERIF-FICHAS (su mandato, §3).
- **Los dos momentos de lectura del §6, juntos en uno.** La atención y el freno se calcularon antes de leer nada, porque T2 siguió de
  corrido, en lugar de «se calculan después de leer las celdas del tramo 1» (`4de7f2a7:docs/preregistro_tanda_final.md:236-238`):
  - lo fijó el «seguí» de T3 de la mesa (punto 7.3), con una nota para la autora antes de pegar, y la ejecutora lo aplicó y lo declaró;
  - es un **desvío declarado**: no cambia ninguna cifra (los umbrales salen de los pesos de las poblaciones y de la tasa de la tanda 0, no
    de una lectura) y va del lado ciego;
  - la mesa propone que no necesita firma; lo decide la autora (PENDIENTE). Si lo firma, va como nota fechada al pie del pre-registro de la
    tanda final.
- **El contenedor de Neo4j salió con el código 137** al detenerlo, con la carga ya verificada (gate 5 OK, paridad 147 de 147):
  `docker compose stop` espera 10 segundos y después mata el proceso. Antes de usar ese volumen, la próxima carga controla que el
  contenedor arranque sano y que el log no dé errores de recuperación, corre `verificar_carga` de cada grafo que vaya a usar (el
  `kg_sha256` de `KG_Meta` contra `grafos.py`, y los nodos y las aristas), y se detiene con `docker compose stop -t 120`.
- **T4, primer tramo:** la lectura asistida de las ocho muestras, las planillas, el LEEME y el convertidor, con el «seguí» de la mesa
  (`decisiones_202_mesa/t4/`). La lectura de la autora va con ese LEEME. Su horario sale del calendario v12d: con la lectura de T4 la
  noche del martes 20 y los lotes 04 a 06 de V el miércoles 21, el sello de la tanda queda el miércoles 21 en el escenario central.
- Las secciones anteriores no se editan.

## 69. La calibración del juez de precisión de V, corrida (agregado del 20/10/2026)

Hechos de la autora del 20/10/2026, recibidos a las 15:01:10 (hoja de ruta de la mesa, §203).

- **La calibración corrió:** 60 de 60 llamadas, 0 errores, 0 reintentos, 0 cruces y USD 4,5227 (`comandos/calibracion_juez_v.sh 8.5 6.5`),
  con su análisis (`corridas/calibracion/analisis_calibracion_V.json`). El gold no corrió.
- **Lo que da, fuera de muestra:**
  - veredicto, 17 de 20, con 19 de 20 unánimes; las tres diferencias van para el mismo lado (P04, P10 y P15: la autora, incorrecta; el
    juez, correcta);
  - de las 7 incorrectas de la autora, el juez detecta 4; la precisión del pool da 16 de 20 con el juez y 13 de 20 con la autora;
  - modalidad, 17 de 20 (P08, P10 y P15, el juez diciendo sostenido); predicado, 18 de 20 (P04 y P16); valores, 19 de 20 (P11); los
    rasgos y la importancia, en P05 y P11.
- **La clasificación de la mesa** (`decisiones_203_mesa/juez_v/`, con el texto de cada ficha del pool y las razones del juez, sin las notas
  de la autora): de las 12 diferencias, que son 7 causas, 2 son de evidencia (P04, que no usa el tramo del requisito previo, y P15, que no
  confronta el «podrá» con el tipo Obligacion del nodo) y 5 de etiqueta (P05, P08, P10, P11 y P16).
- **La proyección al gold** (`proyeccion_criterios_46_gold_mesa.py`): con 3 de 7 incorrectas que pasan, el (ii) del §4.6 pasa solo si la
  autora marca 11 incorrectas o menos en las 100. Con las unas 15 que supone el §4.6 (iii), la diferencia esperada es 0,064 y la
  probabilidad de pasar, 0,318. El (iii) pasa en lo esperado (0,714 con 15).
- **La propuesta de la mesa:** usar ahora la única recalibración del §4.7, antes del gold, con la modalidad computada por el código: el
  juez cita la marca de modalidad de cada nodo normativo y su clase, el código controla que la marca esté en la evidencia y la compara
  con el tipo del nodo, con una tabla fija antes de correr. P04 y las cinco de etiqueta quedan como límite del instrumento. Si la
  recalibración da menos acuerdo de veredicto que la v1.3 en el pool, el gold corre con la v1.3, declarado. La decide la autora, por escrito
  (PENDIENTE). En el escenario central del calendario v12d, la recalibración atrasa el gold y N7, pero N7 sigue antes del corte del
  sábado 24 y la firma del pre-registro de B6.3, antes del plazo; en el lento, no llegan ni con ella ni sin ella.
- **El costo** (`decisiones_203_mesa/costo/`): la escritura de caché fue el 67 % de la calibración, porque cada caso lleva su prefijo. El
  gold, con un prefijo de 51.098 tokens, proyecta 9,11 central y 13,67 alto (tope 16, freno 13). **El tope de V es 50 desde el 19/10/2026**
  (nota al pie del pre-registro de tripletas, `:347-351`; §56), y no 35. V entera, con las dos recalibraciones (la de precisión y la de
  presencia), proyecta 32,93 central y 43,36 alto: entra.
- Las secciones anteriores no se editan.

## 70. La recalibración única del juez de precisión de V, decidida, y los dos momentos de lectura del §6, sin firma (20/10/2026)

Decisiones de la autora del 20/10/2026, recibidas a las 16:27:56 (hoja de ruta de la mesa, §204).

- **La recalibración del juez de precisión de V** (§69; análisis de la mesa en `decisiones_203_mesa/juez_v/`), tal cual: «sí, ahora, antes
  del gold, como la propusiste […], §3: la modalidad la computa el código, el juez solo cita la marca y su clase, y el código controla que
  esté literal y la compara con el tipo del nodo con la tabla fija. Es la única recalibración del §4.7.»
  - **La tabla fija:** Obligacion, deber; Restriccion de tipo prohibición, prohibición; Restriccion de tipo límite (cuantitativo o
    cualitativo), **prohibición o deber** (decisión de la autora); Potestad, permiso; Condicion, condición.
  - **Fijado antes de correr:** «si la v1.4 da menos acuerdo de veredicto que la v1.3 en el pool (17 de 20), el gold corre con la v1.3,
    declarado».
  - **Límite del instrumento:** P04 (de evidencia) y las cinco de etiqueta (P05, P08, P10, P11 y P16) quedan documentadas como tales.
  - **Cómo, según el §4.7:** con esta decisión escrita, con los casos resueltos del pool y nunca con las 100, re-corriendo la calibración
    entera fuera de muestra (60 llamadas, tope 8,5 y freno 6,5). La v1.4 va detrás de una bandera: apagada, es la v1.3 byte a byte, para
    que la regla pueda mandar el gold a la v1.3. Su «seguí» está en `decisiones_204_mesa/juez_v/`.
  - **El freno del gold** (tope 16, freno 13) no cambia: el código proyecta con la mediana del costo por llamada (`juez_v.py`,
    `GuardaGasto`), no con el p90 del alto de la §69 (13,67). Con los tokens reales de la calibración, la mediana proyecta 8,63 con la
    v1.3 y 9,30 con la salida un 30 % más larga, y el freno se dispararía con una salida mediana de 1.518 tokens (la real es 522)
    (`decisiones_204_mesa/costo/`). El análisis de la recalibración lo vuelve a proyectar con los tokens de la v1.4.
  - Va una nota fechada al pie del pre-registro de tripletas que declara la recalibración. El texto firmado no cambia.
- **Los dos momentos de lectura del §6 del pre-registro de la tanda final, juntos en uno** (§68): no necesitan la firma de la autora.
  Quedan como desvío declarado, con su origen en el «seguí» de T3 de la mesa (punto 7.3), que la autora pegó con una nota previa. La
  atención y el freno de T4 se calcularon antes de leer nada, porque T2 siguió de corrido, en lugar de «se calculan después de leer las
  celdas del tramo 1» (`4de7f2a7:docs/preregistro_tanda_final.md:236-238`). Lo declaran el FRENO T3 (sección 7.7) y el informe de T4.
- Las secciones anteriores no se editan.

## 71. U-VERPUNTO, sus dos etapas revisadas, y la salida del brazo de fragmentos por encima del tope de MCP (20/10/2026)

Hechos y precisiones de la autora del 20/10/2026, recibidos a las 16:58:57 (hoja de ruta de la mesa, §205).

- **Lo que hizo la autora,** por su confirmación: el push de los tres commits de T3 (`71cb9305`, `5aae4fe0` y `7cbf3525`) y el pegado del
  «seguí» de la v1.4 del juez de V.
- **U-VERPUNTO terminó sus dos etapas,** cada una en FRENO (sesión `130328f7`). La etapa b corrió con cuatro precisiones de la autora:
  - D-5 con la fuente del FRENO de T3 (`fae35662…`);
  - el cambio del docstring de `familias_nav.py` (línea 12), declarado fuera de la lista;
  - las llamadas con comillas dobles;
  - el control de los contenedores de otro proyecto.
- **La revisión de la mesa** (`decisiones_205_mesa/verpunto/`): las dos etapas cierran.
  - La a da 72 de 72 (`276b7838…`): el texto propio entero en `ver_punto` con su tope por punto, la regresión contra U-NAV-DESDE y N5 por
    sha256, y la salida más larga en 53.687 caracteres.
  - La b da 40 de 40 con el manifiesto `9dd1f32c…`, que no es el `1c1da173…` que dio la autora: la ejecutora rearmó el paquete a las 16:52,
    después del borrado del archivo del harness, con su error declarado. Sus siete controles pasan.
  - El código (`familias_nav.py` `c27bc888…`, `selftest_familias_nav.py` `7b7c753c…`) y los dos bloques con los ejemplos de fragmentos
    (`c08073f1…` y `37ae9130…`) entran con el 142 rearmado, después del sello de la tanda.
- **La salida del brazo de fragmentos por encima del tope de MCP** (D-6; `decisiones_205_mesa/d6/`):
  - un resultado de más de 25.000 tokens (el `MAX_MCP_OUTPUT_TOKENS` por defecto, que el banco no fija) no llega cortado: se guarda en disco
    y el agente recibe una referencia a un archivo (`banco_mcp/README.md:137-141`). Los agentes del banco solo tienen las herramientas MCP,
    así que lo pierden entero;
  - con `limite` 5 (el `limite_max` de las dos configs), la cota de `buscar_pasajes` es de 143.463 caracteres (≈ 51.605 tokens con 2,78
    caracteres por token, una estimación). Ya con `limite` 2 pasa los 25.000. Las salidas medidas en los ejemplos llegan a 8.193;
  - la de `ver_punto` queda por debajo en su peor caso (53.687 caracteres, ≈ 19.312 tokens), con poco margen si la razón real es menor;
  - **la propuesta de la mesa,** para decidir antes de los pre-registros de A2.2 y de B6.3 (PENDIENTE de la autora): el mismo
    `MAX_MCP_OUTPUT_TOKENS` en los dos brazos, 70.000, por encima del peor caso de los dos; un control por código de los resultados que
    llegan como referencia a un archivo, por brazo, que tiene que dar 0; y una sesión real corta antes de las corridas, paga y con tope de
    la autora, que muestre que con la variable puesta el resultado llega entero.
- **El contenido de los ejemplos que mostró la ejecutora** venía de un archivo de la mesa: `decisiones_195_mesa/verpunto/
  salida_estructura_bloque_familia6_mesa.json` (`11263a03…`) trae las palabras de las consultas de los ejemplos del grafo en sus 14
  `formas_de_las_llamadas`. La mesa no debía tener ese texto; es un error de la mesa de la §195. La ejecutora borró la copia del harness y lo
  declaró. La propuesta de la mesa es renombrar ese archivo a `NO_ABRIR_` en las dos copias de su paquete, con los mismos bytes (PENDIENTE
  de la autora).
- Las secciones anteriores no se editan.

## 72. La salida del brazo de fragmentos, decidida, el JSON de la §195 cerrado y el gold de V sellado (20/10/2026)

Decisiones y hechos de la autora del 20/10/2026, recibidos a las 17:16:20 (hoja de ruta de la mesa, §206).

- **La D-6, decidida** (§71), tal cual: «MAX_MCP_OUTPUT_TOKENS en 70.000 en los dos, declarado como cambio respecto de la base; el control
  por código, por brazo, de los resultados que llegan como referencia a un archivo, que tiene que dar 0 en A2.2 y en B6.3; y la sesión real
  corta, paga, con el tope que me propongas, que muestre que el resultado llega entero.»
  - **La sesión real corta, como la propone la mesa** (`decisiones_206_mesa/d6/`): tres sesiones de `claude-sonnet-5`, el modelo de los
    agentes del banco (`a2_1/config_agentes_a2_1.json:9`), cada una con una sola llamada a un servidor de prueba que devuelve un texto
    fijo, sin contenido de normas:
    - A, unos 40.000 tokens con la variable en 70.000: tiene que llegar entero;
    - B, los mismos sin la variable: el control de que se reemplaza por una referencia a un archivo;
    - C, unos 65.000 tokens con la variable: llega entero cerca del techo.
    Con los precios sellados del banco da USD 0,25 central y 0,46 alto (NO VERIFICADOS los tokens del sistema). **Tope propuesto, USD 1,0,
    con freno en 0,6** (PENDIENTE de la autora). Va antes de las corridas de A2.2, en el carril pago, de a uno.
  - **El control en N6 y en A2.1:** N6 no corrió todavía (va después del 142). El control queda como un paso de su análisis, por código,
    sobre sus logs: con 0, N6 no cambia; si no da 0, se informa por brazo antes de seguir. De A2.1 corrieron solo las sesiones de las
    pruebas de aislamiento: en ellas el agente no hizo llamadas, y las salidas registradas llegan a 5.253 caracteres, lejos del tope. **Da
    0** (`banco_mcp/aislamiento/resultados/`, en HEAD).
- **El JSON de la §195, cerrado** (§71), por decisión de la autora: `decisiones_195_mesa/verpunto/salida_estructura_bloque_familia6_mesa.json`
  pasó a `NO_ABRIR_salida_estructura_bloque_familia6_mesa.json`, con los mismos bytes (`11263a03…`), en las dos copias del paquete de la
  mesa.
  - El respaldo nocturno copia con `ditto` desde `/private/tmp` a esa misma copia permanente, y no corrió desde que ese archivo existe
    (su último manifiesto es de las 00:00 del 20/10): no hay otra copia.
  - Los despachos de U-VERPUNTO de la §195 y la §196 lo nombran por su nombre y su sha256 anteriores.
- **El gold de V, terminado:** la autora leyó y selló con `sellar_hoja.py` los nueve lotes, del 01 al 09, además del piloto. Los lotes 04
  a 09 no van el miércoles ni el jueves.
- **El calendario v12e** (`decisiones_206_mesa/calendario/`): con ese tiempo libre, la lectura de T4 de la autora desde las 18:20 de hoy y
  la recalibración del juez de V. En el escenario central, el sello de la tanda final queda el miércoles 21, N7 el viernes 23 y la firma del
  pre-registro de B6.3 el sábado 24, todo a tiempo; en el lento, la firma pasa el plazo.
- **La comparación del §4.6** (juez contra el gold de la autora), una vez que corra el gold del juez con la versión que dé la regla:
  - **el script:** `tripletas_v_juez/codigo/analisis_gold_juez_v.py`, por `comandos/analisis_gold_juez_v.sh <carpeta de las hojas>`, que
    corre la autora;
  - **sus entradas:**
    - el agregado del juez, `corridas/NO_ABRIR_agregado_gold_V.json`, que lee el código;
    - las 10 hojas del gold (`hoja_piloto.csv` y `hoja_lote_01…09.csv`), desde la carpeta de lectura de la autora, cada una con su sello
      (`sello_hoja_<lote>.txt`). El script controla el sha256 de cada sello, la cabecera y las filas de su lote del acta antes de leer, y no
      imprime ninguna nota;
    - el acta (los lotes, el orden y los pesos de los estratos) y las fichas, del repo;
  - **lo que da:** `corridas/analisis_gold_V.json`, solo con cifras: los tres criterios con las 100 y, aparte, sin las 10 del piloto, el kappa,
    la importancia y las que van a adjudicación. Si las dos dan otra decisión del §4.6, se declara y rige la de las 100;
  - **lo `NO_ABRIR_`:** los veredictos, el agregado y las bases del gold no los abre nadie antes del análisis; el análisis los lee por código.
    Como las 10 hojas ya están selladas, la lectura a ciegas del §4.5 está cumplida: si después hiciera falta mirar una ficha, la abre la
    autora, después de que el análisis corrió y su salida quedó guardada. La mesa no los abre nunca.
  - **Lo que falta, en orden:** el FRENO de la v1.4 y su revisión; la recalibración paga y su análisis, que escribe `regla_del_gold.json`;
    el gold pago (`gold_juez_v.sh 16 13 <versión>`); y el análisis. La revisión de la v1.4 controla que el análisis lea el agregado de la
    versión que corrió.
- Las secciones anteriores no se editan.

## 73. El primer tramo de T4 de la tanda final, revisado (agregado del 20/10/2026)

Hechos de la autora del 20/10/2026, recibidos a las 17:19:30 (hoja de ruta de la mesa, §207).

- **El FRENO T4, primer tramo** (`data/experiment/tanda_final/t4/FRENO_T4_tramo1.md`, `c7eab228…`; paquete
  `revision_tanda_final_FRENO_T4_tramo1/`, `0f2d428e…`). La mesa lo revisó (`decisiones_207_mesa/t4/`), sin abrir ninguna ficha, propuesta
  ni justificación:
  - el paquete da 81 de 81;
  - las 8 planillas dan su sha256 y suman 216 filas, con las dos columnas de la autora vacías;
  - el LEEME es el de la mesa (`9e224f09…`);
  - el convertidor es el de la tanda 1 salvo su docstring y los sha256 de las planillas, y su prueba da los 12 casos;
  - lo nuevo está solo en `tanda_final/t4/`.
- **Los cinco criterios que la ejecutora fijó por su cuenta** (su sección 8), contra el LEEME:
  - **dentro de sus reglas:**
    - U-tipo: un tipo que contradice la modalidad del texto es error, y el tipo cercano sigue siendo lectura laxa;
    - U-fuera-del-texto: el nodo sin pasaje en el texto que muestra la ficha es dudosa, que cuenta como error;
    - la (3) de una facultad o un límite y su acto, que sale del criterio general de la §31;
    - la (12) a «catálogo»;
    - y el dato a informar como vaciamiento, que fija una frontera de «contenido normativo» que el LEEME deja abierta;
  - **lo extiende uno:** en la (2), el bloque que abre una lista, sin relaciones, como «no vaciamiento» (10 propuestas). El LEEME define el
    vaciamiento sin esa excepción. La línea de base de la (2) es la del T4 de la tanda 1, así que se lee con el criterio que la autora usó
    ahí; si quiere la excepción como regla, es una precisión de la definición, escrita antes de leer y declarada.
- **La autora lee desde las 18:20, con las reglas del LEEME.** Las propuestas son una ayuda: en cada fila decide ella, y el convertidor le
  pide la razón cuando cambia la propuesta.
- Las secciones anteriores no se editan.

## 74. La sesión corta de la D-6, autorizada, la (2) de la vigilancia con el criterio de la tanda 1 y lo que frena a A2.2 y a N6 (20/10/2026)

Decisiones de la autora del 20/10/2026, recibidas a las 17:32:13 (hoja de ruta de la mesa, §208).

- **La sesión corta de la D-6, autorizada** (§72), tal cual: «OK a las tres sesiones (A, B y C) con tope USD 1,0 y freno 0,6, en el
  carril pago, de a una y antes de A2.2.»
  - **Sus comandos los arma una unidad USD 0, fuera del repo** (U-D6-TOPE-MCP; su despacho, en `decisiones_208_mesa/d6/` del paquete de la
    mesa): un servidor MCP de prueba que devuelve un texto fijo, sin contenido de normas, con un código en su última línea; el lanzador
    con las banderas del banco; los controles por código (si el resultado llega entero o como referencia a un archivo, si la respuesta es
    el código y el costo desde los tokens, con los precios sellados); el selftest y la corrida en seco.
  - **El comando pago** empieza con el control de la extracción v2 y con el conteo de los tokens de los dos textos, que no cobra. Corta
    antes de gastar si los conteos salen de su rango, y antes de cada sesión si el gasto pasaría el freno. Lo corre la autora, después
    de la revisión del FRENO de la unidad.
  - **Lo esperado:** A y C llegan enteros, y B, el control sin la variable, como referencia a un archivo. Si A o C no llegan enteros, es
    un FRENO antes de la firma del pre-registro de A2.2, que declara la variable.
- **La (2) de la vigilancia, con el criterio de la tanda 1** (§73), tal cual: «El criterio 3a de la ejecutora en la vigilancia (2) no lo
  adopto como regla: leo esas filas con el mismo criterio que usé en el T4 de la tanda 1, que es la línea de base, sin precisión nueva
  de la definición.» El vaciamiento sigue definido como en el LEEME de T4, sin la excepción del bloque que abre una lista. Las 10
  propuestas de esa clase son una ayuda, como las demás.
- **Lo que frena hoy al 142 rearmado, a A2.2 y a N6** (la autora pide adelantarlos para tener más margen antes de la firma de B6.3;
  calendario v12f, `decisiones_208_mesa/calendario/`, desde las 18:10 y con duraciones NO VERIFICADAS):
  - **el 142 rearmado:** su commit va después del sello de la tanda final y de A2.2 (§44 y §57, `:1516` y `:1960` de este registro), en
    la fila de las ejecutoras del repo (`docs/mandatos/UNAV_DISENO_navegacion_agente.md:173`). La mesa prepara el rearmado antes, sobre el
    HEAD de hoy, y lo rebasa al HEAD de ese momento. No frena a N6: N6 espera al sello de N4, que va después del diagnóstico de A2.2
    (`:168`, `:183` y `:187`), y el 142 llega antes que N4 en todos los escenarios del v12f. Adelantarlo antes de A2.2, con una prueba de
    identidad USD 0, no adelanta N6, y en el escenario lento lleva N7 después del corte;
  - **el pre-registro de A2.2:** lo arma el tramo 3 de A2.1, después del humo y de H-B2 del tramo 2, que con la variante B van en el
    repo, después del sello de la tanda final (decisión del 20/10/2026, 10:01:39, punto 7);
  - **la sesión de la D-6:** solo su unidad y la revisión de su FRENO. Si entra en el carril antes del humo de A2.1, en el escenario
    central el humo, el pre-registro y la corrida de A2.2 se corren 15 minutos, y N4, el 142, N6, N7 y la firma de B6.3 no se mueven;
  - **lo pago del juez de V:** la recalibración espera al 147, que trae su nota de pre-registro. Con la variante B, el gold termina antes
    de que empiece el humo de A2.1 en todos los escenarios: no lo frena;
  - **las horas de la autora** son el recurso que se agota primero. Con el orden del v12e, el censo de C1, el catálogo y la
    re-aplicación toman 4,23 de sus 7 horas del miércoles 21, y el humo de A2.1 pasa al jueves 22.
- **Lo que da el v12f** si las horas de la autora van primero a A2.1, A2.2 y su diagnóstico (el censo, el catálogo y la re-aplicación
  siguen antes del corte R5):
  - en el escenario central, N6 termina el jueves 22 a las 16:21, contra el viernes 23 a las 14:39;
  - de N6 al corte quedan 43,6 horas, contra 21,4;
  - la firma del pre-registro de B6.3 queda el sábado 24 a las 17:49;
  - en el escenario lento, todo queda a tiempo. Con el orden del v12e, N7 queda después del corte.
  - **La variante A** (A2.1 y A2.2 en una copia), con ese mismo orden, adelanta A2.2 2 h 18 min y N6 19 min en el central, y en el
    lento lleva N7 después del corte.
  - **PENDIENTE de la autora:** el orden de sus horas; la D-6 antes del humo de A2.1; y el humo y H-B2 con la misma variable que A2.2.
- Las secciones anteriores no se editan.

## 75. U-UNION-C1 v3, revisada: la regla extendida del TO de la R23, el rc del selftest de claves y la lista de nodos (20/10/2026)

Decisiones y hechos de la autora del 20/10/2026, recibidos a las 18:00:34 (hoja de ruta de la mesa, §209).

- **El FRENO de U-UNION-C1 v3** (paquete `revision_U-UNION-C1/`, sesión `da06600f`, manifiesto `1e530358…`, 50 archivos) dice que
  cumple 12 de 13 criterios. La mesa lo revisó (`decisiones_209_mesa/c1/`):
  - **el paquete y las salidas:** el paquete da 50 de 50, y las 90 salidas de la medición que quedan fuera dan su sha256;
  - **los diffs:**
    - `r1_invariantes.py` da +43 −1 contra HEAD, y +4 −4 contra el parchado, solo en comentarios, con el mismo árbol de sintaxis;
    - `ensamblar_tanda0.py` da +351 −16 contra HEAD y +188 −8 contra la segunda pasada;
    - `selftest_clave_cache.py` da +8 −5: las dos constantes de la R23 y la V23 y la lista de módulos;
  - **los selftests,** en un clon de HEAD de la mesa con lo entregado y con los cinco PDF del subset copiados (no están en git): el
    nuevo da 67/67, y el de C1, «FALLAS: 0»;
  - **el encierro,** recontado con un script propio sobre sus kg.json, da sus cuentas en los ocho pares. De 1 a 3 y de 2 a 4, en los dos
    grafos, cambian 10 nodos y salen 27, todos Comunicacion, y se re-apuntan 24 `referencia`; fuera de esos ids no cambia nada;
  - **el TO de la R23,** recontado desde HEAD:
    - de los 152 TOs con chunks en b584, 29 quedan fuera de las tres tandas;
    - el primero, dmrd, tiene sus 11 unidades de tipo `seccion_sin_puntos`;
    - con la regla extendida salen `gerc` y `gerc::1.1`, la primera de 114 unidades, 96 de ellas del tipo;
    - en las E0 de las tres tandas no hay chunks de `gerc`.
- **La regla extendida del TO de la R23 y de la V23,** decidida por la autora ante el caso de dmrd, que la regla del despacho no cubría,
  tal cual: «TO_NUEVO es el primero, en orden alfabético, de los TOs con chunks en b584 que no están en ninguna de las tres tandas y que
  tienen al menos una unidad punto_terminal con id to::punto; UNIDAD_TO_NUEVO es la primera de ese tipo en el orden de su
  chunks_<to>.json. Da gerc y gerc::1.1.»
- **El rc 0 del selftest de claves** (criterio 2):
  - **la contradicción es de la mesa:** el despacho excluía del rsync las bases de la caché y pedía el rc 0, que sin ellas no puede dar,
    ni con el código de HEAD;
  - **dónde se ve:** nunca en el repo, porque los selftests corren sobre una copia (CLAUDE.md, §4.l). Va en el arenero del armador del
    commit de U-PROC-HERENCIA, de C1 y de las remisiones, antes de ese commit, con el código final y con una copia (no un enlace) de las
    dos bases que lee, `e1_extraccion.db` y `e3_verificacion.db`;
  - **cómo:** R19 las abre solo para leer (`mode=ro&immutable=1`, `selftest_clave_cache.py:242` de HEAD), y el armador toma su sha256
    antes y después. Tiene que dar rc 0, con la R23 y la V23 en miss con `gerc`. Si no, el commit no se arma;
  - **la re-aplicación lo repite** como su primer control, en su copia con las bases.
- **El renombre previo de la guarda** (el hallazgo 3 de la unidad) queda donde está, en `preparar_union_c1` de `ensamblar_tanda0.py`:
  - no toca el parchado de `r1_invariantes.py`, que es el diseño sellado;
  - aplica antes de unir la regla de la guarda de `merge_grafos_guardado`, y deja el nodo de la lista como con la bandera apagada. De la
    corrida 1 a la 6, los tres nodos de las dos colisiones de la lista sintética no cambian;
  - la otra vía (que la unión no tome el id del nodo de la lista) dejaría un nodo de la lista de un TO posterior sin el sufijo de la
    guarda, distinto de la bandera apagada.
- **La lista de nodos de la re-aplicación** puede traer un nodo así: uno con todas sus procedencias en la muestra, en una colisión que
  sin él sigue en dos documentos o más, y que comparte el id con los que se unen.
  - En el acumulado de las tandas 0 y 1 la lista está vacía: ninguna colisión toca la muestra.
  - En el de las tres tandas, el censo no corrió.
  - **La propuesta de la mesa** (PENDIENTE de la autora): el censo de las tres cuenta en memoria esos nodos, sin mostrarlos, y la
    re-aplicación controla que su resumen dé el renombre previo cuando esa cuenta no es 0.
- **La regresión sin entrada en la fixture:** la autora controló que la unidad la computó con el método del §5.7 del FRENO de
  U-PROC-HERENCIA-2 (`computar_regresion`, con la entrada del grafo sellado). Da las 5 declaradas.
- **El «seguí» de la etapa b de las remisiones,** con sus cinco huecos llenos (`decisiones_209_mesa/remisiones/`). Cambia en tres cosas
  más:
  - su paso 0 pide el 147 v5;
  - el selftest de claves se controla por sus rutas, porque en la copia da rc 1;
  - la unión conserva el renombre previo.
- Las secciones anteriores no se editan.

## 76. El orden de las horas de la autora, el censo con el renombre previo y la v1.4 del juez de precisión de V, revisada (20/10/2026)

Decisiones y hechos de la autora del 20/10/2026, recibidos a las 18:26:41 (hoja de ruta de la mesa, §210).

- **El orden de las horas de la autora** (§74), tal cual: «el escenario 3b. Primero A2.1, A2.2 y el diagnóstico, con la D-6 antes del
  humo de A2.1. El humo y H-B2 corren con MAX_MCP_OUTPUT_TOKENS puesto en 70.000.» El censo de C1, las claves del catálogo y la
  re-aplicación van después, y siguen antes del corte R5. Con la variable también en el humo y en H-B2, A2.1 calibra el corte de A2.2 en
  las mismas condiciones en que A2.2 corre, y el «seguí» del tramo 2 la lleva, con el control de las referencias a un archivo.
- **El censo y el renombre previo** (§75), tal cual: «El censo cuenta en memoria los nodos de la lista que quedan dentro de una colisión
  que igual se une, y la re-aplicación controla su renombre.» La cuenta va con las demás del censo, sin mostrar ninguno. Si no es 0, el
  resumen de la cadena de la re-aplicación tiene que dar ids con el renombre previo.
- **Lo que hizo la autora,** por su confirmación:
  - corrió el 147 v5, con su push: está en HEAD como `7633ba9e`, con los dos archivos del paquete y sin Co-Authored-By;
  - pegó el «seguí» de la etapa b de las remisiones en su sesión;
  - pegó el despacho de la D-6 en una sesión nueva, abierta en `fuera_del_repo/d6_tope_mcp/`.
- **La v1.4 del juez de precisión de V, revisada** (paquete `revision_UTRIP_V_JUEZ_v1_4/`, sesión `539f236b`, manifiesto `b3fe19f8…`;
  la revisión, en `decisiones_210_mesa/juez_v/`):
  - el paquete da 35 de 35, la carpeta viva es la del paquete y `corridas/` tiene solo la calibración, con sus 7 sha256;
  - la tabla, recomputada desde el código, da `8490d5c4…`. Los dos límites admiten deber y prohibición, como se decidió (§70);
  - la regla del gold es la del §70: la v1.4 si da 17 de 20 o más, y si no, la v1.3;
  - **el análisis de la recalibración lee el agregado de la v1.4:** controla que cada ficha se haya juzgado con su prompt congelado de
    la v1.4;
  - **el análisis del gold lee el de la versión que corrió, pero no lo controla:** las dos versiones escriben el mismo agregado, y el gold
    solo corre con la versión de la regla. Pero el análisis no controla ni declara la versión.
  - **La propuesta de la mesa** (PENDIENTE de la autora): un «seguí» corto, USD 0, después del gold y antes de su análisis. El análisis
    frena si la versión del agregado, la del resumen y la de la regla no coinciden, y la escribe en su salida con sus sha256. Sin él, el
    control queda a mano, en el resumen del gold.
- **El orden de lo que corre la autora** (`decisiones_210_mesa/juez_v/ORDEN_DE_TUS_COMANDOS_JUEZ_V_mesa.md`):
  1. la recalibración paga (8,5 y 6,5);
  2. su análisis, que la mesa revisa antes del gold;
  3. el gold pago (16 y 13, con la versión de la regla);
  4. el «seguí» corto, si se acepta;
  5. el análisis del gold.
  Si la proyección del gold con los tokens reales no cabe en el freno, el gold no corre hasta revisarla.
- Las secciones anteriores no se editan.

## 77. La D-6, de nuevo: el tope en caracteres del CLI sellado, y el análisis del gold de V con su versión (20/10/2026)

Hechos y decisiones de la autora del 20/10/2026, recibidos a las 23:13:58 (hoja de ruta de la mesa, §211).

- **El FRENO de U-D6-TOPE-MCP** (paquete `revision_UD6_TOPE_MCP/`, sesión `2b4a5420`, manifiesto `44fc4a7f…`, 85 archivos). La unidad
  quedó armada a USD 0, y la autora le pidió que no corra las tres sesiones. Su hallazgo, verificado por la mesa con el script de la
  unidad (13 anclas, la misma salida byte a byte) y con su propia lectura del binario sellado (`decisiones_211_mesa/d6/`):
  - el CLI 2.1.241 tiene, además del tope en tokens que fija `MAX_MCP_OUTPUT_TOKENS`, un tope en caracteres por herramienta;
  - sin la anotación `_meta["anthropic/maxResultSizeChars"]`, el tope es de 50.000 caracteres, y con ella, el valor anotado, hasta
    500.000. Un valor remoto por nombre de herramienta puede reemplazarlo (NO VERIFICADO desde acá);
  - y un presupuesto por mensaje: si los resultados de un mismo mensaje suman más de 200.000 caracteres, los más largos se guardan en
    disco. Este lo encontró la mesa, y el FRENO no lo nombra; si está prendido en el modo `-p`, NO VERIFICADO;
  - con el contenido del banco, 50.000 caracteres son unos 21.000 a 23.000 tokens, así que la variable en 70.000 sola no cambia qué
    resultados llegan enteros.
- **Cuántas salidas pasan los 50.000 caracteres,** medidas por código sobre todos los pasajes y todos los nodos
  (`salidas_sobre_50000_por_brazo_mesa.py`):
  - **el brazo de fragmentos:**
    - en el índice de desarrollo de A2.1 y A2.2, ningún pasaje solo; la cota con `limite` 3, 4 y 5 da 63.104, 75.335 y 87.129;
    - en el del acumulado de las tandas 0 y 1 (N6), un pasaje solo (51.525) y hasta 144.878 con `limite` 5;
  - **el brazo del grafo:** ninguna salida de `ver_nodo`, `ver_vecinos` ni `buscar_nodos`, en los dos grafos. Se midió sobre el kg.json,
    no sobre Neo4j, así que es del orden (NO VERIFICADO que coincida). Con el 142, `ver_punto` tiene entre 1 y 6 salidas de más de
    50.000 en N6 (la más larga, 53.687);
  - **en las sesiones reales registradas,** ninguna.
  - Sin la anotación, el brazo que pierde salidas es el de fragmentos.
- **Las opciones para la igualdad** (`propuesta_igualdad_de_los_brazos_D6_v2_mesa.md`):
  - 1, la misma anotación, en 200.000, en todas las herramientas de los dos servidores, con la variable en 70.000;
  - 2, un tope del lado del servidor por debajo de 50.000, igual en los dos brazos;
  - 3, dejarlo como está y confiar en el control.
  - **La propuesta de la mesa,** la 1 (PENDIENTE de la autora). No cambia lo que ve el agente, porque la anotación no va en la
    definición que el CLI manda al modelo; se verifica con la petición capturada. Pide dos unidades cortas sin pago (la anotación en los
    servidores y el «seguí» de la sesión corta) y las tres sesiones rehechas, con el mismo tope y el mismo freno, antes del humo de A2.1.
  - El control por código de las referencias a un archivo, por brazo, que tiene que dar 0, sigue y cubre los tres mecanismos.
- **Las escrituras del modo init en `~/.claude`** (tres archivos de sesión, `~/.claude.json` y sus respaldos): por decisión de la
  autora, no se borran y quedan declaradas. La memoria no cambió. Son las escrituras del CLI al arrancar, y el `.claude/` vedado es el del
  repo. Para las próximas corridas en seco, el modo init puede usar `CLAUDE_CONFIG_DIR` en una carpeta de la unidad.
- **El «seguí» v1.4b del análisis del gold de V,** aceptado (§76): la autora lo pega después del gold y antes de su análisis.
- Las secciones anteriores no se editan.

## 78. La etapa b de U-REMISIONES-SUBPUNTOS, revisada: la unión de las dos banderas (20/10/2026)

Hechos y decisiones de la autora del 20/10/2026, recibidos a las 23:15:05 (hoja de ruta de la mesa, §212).

- **El FRENO de la etapa b** (paquete `revision_UREMISIONES_SUBPUNTOS_b/`, sesión `aab0e5be`). La autora dio la versión 1 (62 archivos,
  manifiesto `5f2cef76…`), con la unión sin casos de freno y un punto abierto: la rama 6 del selftest de U-UNION-C1 corre
  `armar_no_unir_c1.py`, que el «seguí» de la etapa b no nombraba.
  - **Decisión de la autora:** autorizó a la ejecutora a abrir solo ese archivo del paquete de U-UNION-C1
    (`armar_no_unir_c1_entregado_U-UNION-C1.py`, sha256 `08705913…`), a correr las 67 ramas y a rearmar su paquete.
  - **La versión 2** (67 archivos, manifiesto `13cb195c…`, con la versión 1 adentro, con su nombre) da el selftest de C1 en 67/67, rc 0.
- **La revisión de la mesa** (`decisiones_212_mesa/remisiones/`):
  - el paquete da 67 de 67;
  - la unión, recontada con un script propio sobre sus kg.json, es exacta en los dos grafos: lo que cambia de la corrida 2 a la 5 es lo
    de 2 a 3 (C1) más lo de 2 a 4 (las remisiones), con 0 objetos tocados por las dos piezas, y la 6 es la 5, byte a byte;
  - los otros dos selftests dan lo de sus paquetes, y R19 sin cuentas es la referencia de U-UNION-C1 v3.
  - **La cifra de D-5 para N7 y el pre-registro de B6.3,** de la 3 a la 5: 14.133 remite_a nuevas con cola y 13.940 sin cola.
- **El commit de U-PROC-HERENCIA, de C1 y de las remisiones** (después del sello de la tanda final y antes de la re-aplicación) suma
  `data/experiment/med_desamb/c1_cadena/armar_no_unir_c1.py`, por decisión de la autora. La lista de sus archivos, con el sha256 de cada
  uno y de dónde sale, está en `decisiones_212_mesa/remisiones/archivos_del_commit_UPROC_C1_remisiones_mesa.md`.
- Las secciones anteriores no se editan.

## 79. La D-6, decidida: la anotación en los dos servidores, con dos condiciones (20/10/2026)

Decisiones de la autora del 20/10/2026, recibidas a las 23:35:17 (hoja de ruta de la mesa, §213).

- **La D-6** (§77), tal cual: «la opción 1. La misma anotación anthropic/maxResultSizeChars en 200.000 en todas las herramientas de los
  dos servidores, con MAX_MCP_OUTPUT_TOKENS en 70.000. Con dos condiciones: que la petición capturada muestre que las definiciones de
  herramientas que recibe el modelo son las mismas, byte a byte, con y sin la anotación, en los dos brazos; y que las tres sesiones pagas
  rehechas (tope USD 1,0 y freno 0,6) corran antes del humo de A2.1. Si esas sesiones muestran que el presupuesto de 200.000 caracteres
  por mensaje está activo en el modo -p, decímelo antes de A2.1.»
  - **U-ANOT-MCP** (despacho en `decisiones_213_mesa/anot_mcp/`; USD 0, sobre una copia del repo): la anotación en el `_list_tools` de
    los dos servidores del banco, no en `harness.TOOLS`. Prueba que la lista de herramientas la trae y que el resto no cambia. Captura la
    petición que el CLI sellado manda a un servidor local, en las configs BM25, densa y del grafo en memoria, con y sin la anotación, y
    compara byte a byte el arreglo `tools`. Repite las pruebas de aislamiento. Su entrega va al repo con un commit de la mesa, entre
    ejecutoras, antes del tramo 2 de A2.1.
  - **La etapa b de U-D6-TOPE-MCP** («seguí» en `decisiones_213_mesa/d6/`; USD 0), las tres sesiones rehechas, todas con la variable:
    - A': 140.000 caracteres con la anotación, que tiene que llegar entera;
    - B': lo mismo sin la anotación, que es el control;
    - C': dos resultados de 110.000 caracteres en el mismo turno, con la anotación. Muestra si el presupuesto por mensaje está activo en
      el modo `-p`.

    Las corre la autora después de la revisión de su FRENO, en el carril pago y antes del humo de A2.1.
  - **El 142 rearmado** lleva la misma anotación en sus servidores y en `ver_punto`, y la mesa vuelve a correr ahí la captura de
    U-ANOT-MCP.
- **Lo que hizo la autora,** por su confirmación: corrió el 148 v2, con su push. Está en HEAD como `5304db37`, con el registro igual al
  del paquete y sin Co-Authored-By.
- Las secciones anteriores no se editan.

## 80. La recalibración del juez de precisión de V, hecha y descartada por la regla, y qué pasa si la v1.3 no cumple el §4.6 (20/10/2026)

Hechos y decisiones de la autora del 20/10/2026, recibidos a las 23:36:53 (hoja de ruta de la mesa, §214).

- **La recalibración única del §4.7, hecha** (§70), por la autora:
  - `recalibracion_juez_v1_4.sh 8.5 6.5`: 63 llamadas pagadas, 57 de 60 completas, 3 errores de forma (las tres repeticiones de P12, que
    quedó sin consenso en todas las dimensiones), 3 reintentos, 0 cruces y USD 4,6561;
  - su análisis: la v1.3, 17 de 20 en el acuerdo de veredicto; la v1.4, 12 de 20 (13 de 20 aunque P12 contara como acuerdo).
  - La mesa reprodujo las cifras desde el resumen y los dos análisis (`decisiones_214_mesa/juez_v/`).
- **Descartada por la regla fijada antes de correrla:** al gold va la v1.3 (`regla_del_gold.json`, `version_al_gold: v1_3`). No hay
  otra recalibración: el §4.7 admite una sola.
- **El hallazgo sobre el instrumento,** con la descripción de la autora, tal cual: «La v1.4 no mejoró la modalidad (16 de 20 contra 17
  de 20: P08 y P15 dejan de diferir, P03 y P16 pasan a diferir y P10 sigue igual) y movió componentes que el cambio no tocaba: el sujeto
  en P06 y P14 y el predicado en P11 y P19, casi todos unánimes, con tres falsas alarmas nuevas (P06, P11 y P14) donde la v1.3 no tenía
  ninguna.»
  - En las cuentas de la mesa, P12, sin consenso, es el cuarto que difiere en la modalidad.
  - De las cuatro diferencias nuevas en el sujeto y el predicado, tres son unánimes (3 de 3) y una es de 2 a 1.
  - Va al informe de V como límite del instrumento, junto con los desacuerdos residuales de la v1.3.
- **El gold, con la v1.3:** `gold_juez_v.sh 16 13 v1_3`. La proyección del gold con los tokens de la v1.4 da USD 8,8366, bajo el freno.
- **Qué pasa si la v1.3 no cumple el §4.6 en el gold,** escrito antes del gold
  (`decisiones_214_mesa/juez_v/si_la_v1_3_no_cumple_el_4_6_en_el_gold_mesa.md`). El bloque del §4.6 da el mismo sha256 en el commit de
  la firma (`4afbe511`) y en HEAD:
  - **las condiciones:** (i), (ii) y (iii) van a la vez. Si el (ii) falla, en la precisión cruda o en la ponderada, el juez no pasa
    aunque pasen las otras dos. La enmienda 3 no lo toca: el (ii) compara las estimaciones puntuales;
  - **si no pasa,** tal cual: «el juez no escala; la precisión de V queda con las 100 de la autora y la de T se mide con muestra humana
    (§7)». Si más de 15 de las 100 van a adjudicación, se declara esa frontera y las adjudicadas quedan como lectura humana;
  - **con las 100 o sin el piloto:** si las dos dan otra decisión, rige la de las 100;
  - **abierto, a decidir antes del análisis del gold** (PENDIENTE de la autora):
    - si el criterio de importancia es parte del «pasa». La mesa recomienda que sí, por ser la lectura más estricta;
    - el tamaño de la muestra humana de T si el juez no escala. El §7 fija solo el control a ciegas de 30.
- **La v1.4b** sirve con la v1.3 como está: sus controles traen los valores de las dos versiones.
- Las secciones anteriores no se editan.

## 81. La importancia en el «pasa» del juez, la muestra humana de T, la etapa T en el calendario y el sello de la tanda final (21/10/2026)

Decisiones y hechos de la autora del 21/10/2026, recibidos a las 07:39:46 (hoja de ruta de la mesa, §215).

- **El criterio de importancia entra en el «pasa» del juez (§4.6):** es la lectura más estricta, la que recomendó la mesa en la §80,
  decidida antes del análisis del gold. Si el juez no llega al acuerdo de importancia («exacto en al menos 60 de 100 y a un nivel de
  distancia en al menos 90 de 100»), no escala, tampoco para la precisión.
- **La muestra humana de T si el juez no escala,** por regla de la autora: «100, si entra en el calendario después de la firma de B6.3
  sin mover ningún plazo; si no entra, 30, declarado». Las cuentas de la mesa (`decisiones_215_mesa/muestra_t/`):
  - **las horas:** con 100 fichas, 4,00 h a 2,4 min por ficha y 6,92 h a 4,15; con 30, 1,20 h y 2,08 h. Son las tasas de las fichas
    de V (§55), NO VERIFICADAS para las de T;
  - **el ancho:** la mitad del ancho del Wilson con 0,85 es 0,0699 con 100 y 0,1219 con 30;
  - **con la etapa T antes de la cobertura de V,** que tiene la última prioridad: en el central, todo a tiempo con las dos muestras.
    En ninguno de los seis factores de escala, de 1,0 a 1,5, la de 100 deja fuera de tiempo algo que la de 30 no deje. Lo que la de 100
    corre es el cierre de la cobertura de V;
  - el tamaño lo cierra la autora antes del análisis del gold (PENDIENTE).
- **La etapa T no estaba en el calendario.** El §7 la pone dentro del pre-registro de B6.3, así que corre después de su firma; los
  calendarios de la mesa no la contaban desde el v9c. Con ella contada, la cobertura de V no cierra el miércoles 28 desde un factor de
  1,1, con cualquier tamaño de muestra: rige la red de la cobertura (cede la cobertura y nunca el N).
- **El 149** corrió con su push (`bb6dc713`). Su archivo da el mismo sha256 que el del paquete de la mesa.
- **T4:** la autora tiene 2 de las 8 planillas hechas, sin sellar, y lee las 6 que faltan el 21/10 a la mañana.
- **El calendario v12g** (`decisiones_215_mesa/calendario/`, desde las 08:45 del 21/10; duraciones NO VERIFICADAS):
  - **el sello de la tanda final:** el miércoles 21 a las 17:15 en el central, a las 14:59 en el rápido y a las 21:46 en el lento. En el
    v12f era a las 12:29 en el central;
  - **lo que se corre en el central:** A2.1, 6,0 h; la corrida de A2.2, 14,0 h; N6 y N7, 18,8 h; el sello del grafo evaluado, 23,6 h;
    la firma de B6.3, 14,2 h. En el central todo queda a tiempo;
  - **en el lento:** N7 y la re-aplicación quedan después del corte del sábado 24, y la cobertura de V cierra al límite, el
    miércoles 28 a las 16:24 (sin contar la etapa T);
  - **N6 primero** (PROPUESTA de la mesa): el lanzamiento de N6 toma las horas de la autora antes que el censo y el catálogo. Con eso, N7
    vuelve a quedar antes del corte en el lento. Con 10 h el jueves 22 y otras 10 el viernes 23 entra también la re-aplicación, y la
    cobertura de V pasa del miércoles 28.
- Las secciones anteriores no se editan.

## 82. La muestra de T, N6 primero, el entorno limpio, la D-6 y la anotación, el harness, los tokens, B6.3 y el costo por etapa (21/10/2026)

Decisiones y hechos de la autora del 21/10/2026, recibidos a las 10:43:18, 10:43:56, 10:47:55, 11:01:44 y 11:05:40 (hoja de ruta de la
mesa, §216 a §220).

- **La muestra humana de T, si el juez no escala: 100,** cerrado antes del análisis del gold, con la regla de la §81.
- **N6 primero:** el lanzamiento de N6 toma las horas de la autora antes que el censo y el catálogo. Su comando lo arma la ejecutora de
  U-NAV en el paso 0 de N6, después del 142 y del sello de N4.
- **El 150** corrió con su push (`3fd0ab58`). Su archivo da el mismo sha256 que el del paquete de la mesa.
- **El segundo tramo de T4:** su «seguí» está listo. Espera la lectura de la autora sellada, el control de la mesa y el commit del
  primer tramo con esa lectura (§73).
- **La etapa b de U-D6-TOPE-MCP, revisada:**
  - 94 de 94 archivos;
  - la mesa reprodujo en un arenero el selftest (149 de 149) y la cota del costo: USD 0,4274, y 0,5272 con el máximo de cada rango;
  - en el binario sellado, con la anotación la tool no pasa por el tope en tokens, y en `-p` el presupuesto por mensaje no actúa (lo
    mide C').
  - Las tres sesiones van desde la Terminal, después del entorno limpio y del gold de V, y antes del humo de A2.1.
- **U-ANOT-MCP, revisada:** 227 de 227 archivos. En las tres configs, el arreglo de tools de la petición al modelo es igual byte a byte
  con y sin la anotación: la primera condición de la §79 se cumple. Su commit, el 152, lleva el comentario de la constante corregido por
  la mesa (el CLI no le aplica a la tool anotada el tope en tokens), sin cambiar el código.
- **Las corridas pagas con agentes** (decisión de la autora), tal cual: «las corridas pagas con agentes (las tres sesiones de la D-6,
  A2.1, A2.2, N6 y B6.3) se lanzan desde la Terminal, nunca desde una sesión de Claude, y el lanzador arranca cada agente con el mismo
  entorno limpio en los dos brazos, sin las variables CLAUDE_*, MCP_* ni ANTHROPIC_* de una sesión de escritorio (salvo la clave), y lo
  deja registrado».
  - Hoy el lanzador del banco hereda el entorno entero (`agentes/lanzar_agente.py:112-141`).
  - El cambio es U-ENTORNO-LIMPIO (USD 0): la regla en `env_sesion`, con el registro de los nombres quitados y heredados. Después va la
    etapa c de la D-6.
- **Las banderas remotas del CLI:** en las 16 configuraciones que escribió para U-ANOT-MCP, `tengu_hawthorn_steeple` es falsa y
  `tengu_velvet_ibis` está vacía. Las trajo con una clave inválida, así que para las sesiones reales queda NO VERIFICADO: A' y C' lo
  miden, y si dan otra cosa se avisa antes de A2.1.
- **El harness, confirmado por el mentor del proyecto (21/10/2026):** `claude -p` con todas las herramientas propias deshabilitadas y solo
  el servidor MCP de cada brazo. La especificación de uso, desde la documentación oficial, la arma U-ESPEC-HARNESS (USD 0).
- **Los tokens en la tesis** (decisión de la autora): el costo se reporta en tokens, por caso, con el tokenizador de Anthropic sobre los
  registros, y aproximado desde los caracteres si falta el dato. El lanzador ya guarda el uso por caso (el `modelUsage` del resultado), el
  de cada llamada (el del stream, parcial), el stream entero y la copia de la sesión; para A2.2, N6 y B6.3 no hay que cambiarlo.
- **B6.3** (PROPUESTA de la mesa, PENDIENTE de la autora): la generación sigue ciega al grafo, como dice el mandato. Se suman:
  - la relevancia para un puesto o una decisión, juzgada desde el texto por una instancia ciega;
  - los nodos y las distancias de cada pregunta, calculados después de las corridas y solo para el análisis;
  - la validación de 20 preguntas por un experto, declarada.
  - Los pedazos siguen la estructura de la E0: elegirlos por la del grafo le daría ventaja.
- **El costo por etapa del pipeline,** para el capítulo 4 (decisión de la autora sobre las fuentes):
  - el orden: el uso que devolvió la API; si falta, el conteo del texto guardado con el contador de Anthropic; si tampoco está el texto,
    la estimación desde los caracteres, con la razón medida en esa etapa;
  - la caché va aparte (escritura y lectura), y cada número declara su nivel;
  - E3 va agregado por etapa, sin separar los reintentos.
  - **Hoy:** en las corridas r2b de las tres tandas, el uso de la API está completo en E1 y en E3, y los tiempos de E1 y E3 salen de los
    checkpoints del runner. E0, el validador y el ensamblado no tienen duraciones registradas y se re-miden en una copia. Las T5 de las
    tandas 0 y 1 traen solo USD por etapa. El script lo arma U-COSTO-ETAPAS (USD 0), y la T5 de la tanda final lleva su tabla.
- **El calendario v12h** (`decisiones_216_mesa/calendario/` del paquete de la mesa, desde las 12:00, con duraciones NO VERIFICADAS):
  - el sello de la tanda final, el 21/10 a las 19:18 en el central (17:29 en el rápido y 23:33 en el lento), con el control y el commit
    de la lectura de T4 que el v12g no contaba;
  - en el central, todo a tiempo;
  - en el lento quedan fuera la re-aplicación, la cobertura de V, la etapa T y la firma de B6.3.
- Las secciones anteriores no se editan.

## 83. El entorno de los agentes con una lista de permitidas, B6.3 aceptada, el gold de V corrido y la importancia en el código (21/10/2026)

Decisiones y hechos de la autora del 21/10/2026, recibidos a las 11:27:39 y a las 11:29:23 (hoja de ruta de la mesa, §221 y §222).

- **El entorno de los agentes** (decisión de la autora), tal cual: «El lanzador arranca cada agente desde un entorno vacío, con una lista
  cerrada de variables permitidas (las básicas del sistema que necesita el CLI, la clave y MAX_MCP_OUTPUT_TOKENS), igual en los dos
  brazos, y registra el entorno de cada sesión.»
  - Reemplaza la regla de los tres prefijos de la §82.
  - La aplica U-ENTORNO-LIMPIO en su etapa b, con cada básica del sistema medida.
- **B6.3, aceptada** (la propuesta de la mesa de la §82): la relevancia juzgada desde el texto, con la lista de puestos y la rúbrica de la
  autora, solo para el análisis; los nodos y las distancias después de las corridas, como exploratorio; los pedazos por la estructura de
  la E0; y 20 preguntas a un experto, con el contacto de la autora y la fecha que ella confirme.
  - Va como nota fechada al pie del mandato de las preguntas (`docs/mandatos/UPREG_B63_preguntas_por_tipo.md`), con la rúbrica tal cual.
  - **La corrección de la mesa:** en B6.3 hay tres subtipos de varios puntos, porque la excepción en un hijo salió el 19/10 (nota al pie
    de ese día, punto 1). Las 12 de varios puntos van en proporción a los subtipos del núcleo aprobado, con al menos una de cada uno.
- **El gold de V, con la v1.3:** 300 de 300 completas, 0 errores, 0 reintentos, 0 cruces y USD 9,1653 (tope 16, freno 13). La mesa lo
  controló en los contadores de su resumen, que dice las 08:52:26.
  - La v1.4b está pegada y la mesa revisó su FRENO: 11 de 11.
- **La importancia en el «pasa» del §4.6** (decisión de la autora): la computa el código.
  - El análisis del gold calculaba `decision_46` sin las dos condiciones de importancia, que salían al lado.
  - La v1.4c las suma con el texto firmado: exacto en al menos 60 de 100 y a un nivel de distancia en al menos 90 de 100.
  - El análisis del gold espera su FRENO revisado.
- **El 151 y el 152** corrieron con su push (`1df3b8ef` y `b72bb626`). Sus archivos dan los mismos sha256 que los del paquete de la
  mesa.
- **U-ENTORNO-LIMPIO,** pegada: su carpeta se creó a las 11:25:51, después del 152. Mientras corre, su foto del repo no admite commits.
- Las secciones anteriores no se editan.

## 84. HOME y el aislamiento de las sesiones del banco, el lanzador en el registro, la v1.4c del juez y el borde de (ii) (21/10/2026)

Decisiones y hechos de la autora del 21/10/2026, recibidos a las 15:24:09, a las 15:36:14 y a las 16:04:46 (hoja de ruta de la mesa, §224
a §226).

- **El 153 y el TF4a** corrieron con su push (`ded98223` y `abdc0998`). Sus archivos dan los mismos sha256 que los del paquete de la
  mesa. El TF4a trae la lectura de T4 de la autora, sellada (`tanda_final/t4/lectura_autora/sello_lectura_T4.txt`) y controlada por la
  mesa: 11 de 11 (`tanda_final/t4/control_lectura_mesa/`).
- **U-ENTORNO-LIMPIO, sus dos etapas revisadas:** 203 y 449 archivos, y el patch de la etapa b da el lanzador `09412fa8…`.
  - La lista medida es `("PATH",)`: sin `PATH` no se encuentra el CLI, y sin cada una de las demás de la candidata el servidor sigue
    `connected` con sus tools en los tres caminos.
  - **`DISABLE_AUTOUPDATER=1`** (agregado de la autora al «seguí» de la etapa b, 12:14:37): valor propio del lanzador, en los dos brazos
    y en las dos vías, registrado como las demás. Así el CLI no se actualiza en medio de una corrida paga.
- **`HOME` vuelve a la lista** (decisión de la autora): `ENTORNO_PERMITIDAS = ("PATH", "HOME")`.
  - El modo real copia la sesión desde `~/.claude/projects/` con el `HOME` del lanzador; sin `HOME` en la sesión, esa copia queda sin
    verificar en una corrida paga.
  - `HOME` es igual en los dos brazos, y la petición al modelo no cambia con él: las capturas de U-ANOT-MCP lo tenían y dan el mismo
    cuerpo.
  - `TMPDIR`, `USER`, `LOGNAME`, `SHELL`, `LANG` y las `LC_*` siguen afuera.
  - Lo aplica la etapa b2 (USD 0), pegada por la autora. El commit de la unidad lleva la versión final, la de su etapa c.
- **Lo demás de la etapa b queda como está** (decisión de la autora):
  - la vía bedrock, con los siete nombres de `ENTORNO_AWS` declarados como elegidos por la unidad, y sin ejercitar;
  - el diff de un bloque, con el lazo «limpiar vías» de HEAD que ya no cambia el entorno de la sesión;
  - las credenciales secretas de AWS, registradas por presencia como la clave.
- **La etapa c de la D-6** (decisión de la autora):
  - `MAX_MCP_OUTPUT_TOKENS` pasa del padre, así que el 70.000 sale de la terminal: lo ponen los comandos de las sesiones pagas, y el
    control de cada sesión mira que `entorno_de_la_sesion` lo traiga;
  - las sesiones pagas controlan lo que la etapa b no pudo medir: que se copie la transcripción de cada sesión, que en la sesión sin
    anotación se copien los resultados guardados en disco, y que los acentos de los resultados de las tools lleguen bien;
  - corre con el lanzador de la etapa c de U-ENTORNO-LIMPIO, así sus sesiones pagas prueban la condición del banco.
- **Lo que lee una sesión paga bajo `--bare`** (lectura de la mesa en el binario sellado, `decisiones_224_mesa/cli_bare/` del paquete de
  la mesa):
  - `--bare` no cambia qué archivos de configuración se leen: sin `CLAUDE_CONFIG_DIR`, el CLI lee `~/.claude/settings.json`, el de
    `<cwd>/.claude/`, el local de la raíz git del cwd y el administrado;
  - en `-p` copia a su entorno el bloque `env` de cada uno y el de `~/.claude.json`, y el servidor MCP lo hereda. `entorno_de_la_sesion`
    registra lo que pasa el lanzador, no lo que termina usando el CLI;
  - con el cwd dentro de un repo de git, el contexto de sistema trae el estado de git: la rama, `git status --short`, los cinco últimos
    commits y el nombre de git del usuario. El cwd de la D-6 está fuera de git; los del banco están dentro del repo. Que vaya en la
    petición al modelo es NO VERIFICADO.
- **Prevenir** (decisión de la autora). Lo hace una etapa c de U-ENTORNO-LIMPIO (USD 0), después del FRENO de la b2:
  1. cada sesión del banco corre con una carpeta de configuración nueva y vacía (`CLAUDE_CONFIG_DIR`), fuera del repo. El lanzador copia
     la transcripción y los resultados guardados en disco desde esa carpeta;
  2. el cwd de cada sesión va fuera del repo y fuera de cualquier repo de git. Su ruta tiene la misma forma en los dos brazos y no nombra
     el brazo;
  3. una captura a USD 0 con el lanzador nuevo, en los tres caminos, muestra que la petición al modelo no trae estado de git ni el nombre
     del brazo, y que fuera de eso es igual a la de U-ANOT-MCP;
  4. las sesiones que ya corrieron en el banco con el cwd dentro del repo quedan declaradas así. Son las 24 sesiones pagas de U-A2.0,
     fase B: 12 en `smoke/resultados/faseB/` y 12 en `smoke/resultados/faseB_corrida2/`, cada corrida con 6 en `smoke/cwd_kg` y 6 en
     `smoke/cwd_vector`. Que su contexto haya traído el estado de git es NO VERIFICADO;
  5. B6.3 corre entera con la condición nueva.
- **Qué lanzador corrió cada sesión** (decisión de la autora): la ruta y el sha256 de cada archivo del lanzador que corrió van en el
  comando y en la meta de cada sesión, aparte de `sha_identidad_pipeline`, que no cambia. Va en la misma etapa c.
- **La v1.4c del juez, aceptada** (decisión de la autora), con las dos cifras de importancia al final de la línea «decisión del §4.6».
  - La mesa revisó su FRENO: 10 de 10 archivos; selftest 198 de 198; `corridas/` sin cambios. Al revisarlo, antes de la v1.4d, el
    código de la carpeta viva daba los dos sha256 del paquete.
- **El borde de (ii)** (decisión de la autora): una diferencia de exactamente 0,05 pasa, como dice el texto firmado («difieren en 0,05 o
  menos»).
  - Hoy no pasa: `abs(0.875 - 0.925)` da `0.050000000000000044` en punto flotante, y (ii) cruda da «no pasa».
  - Las dos diferencias, la cruda y la ponderada, se redondean a 10 decimales antes de compararlas con 0,05. (i), (iii) y la importancia
    quedan como están.
  - Lo aplica la v1.4d (USD 0), pegada por la autora, antes del análisis del gold.
- **La importancia, en proporción** (decisión de la autora): se mide sobre los pares con una importancia válida del juez, igual que (i)
  se mide sobre las fichas que el juez decide.
- Las secciones anteriores no se editan.

## 85. El cwd compartido también en paralelo, la b2 y la v1.4d revisadas, el segundo tramo de T4 con su ampliación y el calendario v12i (21/10/2026)

Decisiones y hechos de la autora del 21/10/2026, recibidos a las 17:34:16 y a las 17:42:04 (hoja de ruta de la mesa, §227 y §228).

- **La b2 de U-ENTORNO-LIMPIO, revisada:** 205 de 205 archivos; el patch da el lanzador `66684615…` y el selftest `10546a14…`, que en un
  arenero de la mesa da 25 de 25. El comentario de la constante da la justificación técnica y el ancla, sin nombrar quién decidió
  (convención 5 del `CLAUDE.md` del repo).
- **El cwd compartido, también en paralelo** (decisión de la autora), tal cual: «un solo cwd para todas las sesiones de los dos brazos,
  también en paralelo, siempre que el CLI no escriba nada en él. La etapa c controla que el cwd siga vacío después de cada corrida del
  modo init y de la captura, y lo informa en su FRENO. U-BANCO-PARALELO usa ese cwd compartido y la carpeta de configuración por sesión
  de la etapa c, en lugar de su cwd por sesión, y su test de aislamiento en paralelo controla lo mismo con P sesiones a la vez.»
  - U-BANCO-PARALELO no corrió (no existe su carpeta, `fuera_del_repo/banco_paralelo/`), y su v4 de la §189 tampoco se pegó: su
    despacho pasa a la v5, que espera además el commit de U-ENTORNO-LIMPIO.
  - El «seguí» de la etapa c de U-ENTORNO-LIMPIO pasa a su v2, sin la nota de que las sesiones pagas van de a una: B6.3 está planeada con
    sesiones en paralelo.
- **La v1.4d del juez, revisada:** 12 de 12 archivos; el código de la carpeta viva es el del paquete; selftest 202 de 202, con las 198 de
  antes sin cambiar su esperado; `corridas/` sin cambios. El análisis del gold queda listo para que lo corra la autora (USD 0).
- **El segundo tramo de T4, revisado** (`tanda_final/t4/FRENO_T4_tramo2.md`): 73 de 73 archivos. La mesa corrió de nuevo, sobre una
  copia, las tasas, su verificación independiente y el sorteo de la ampliación: dan lo mismo.
  - La atención de las aceptadas no ítems se dispara, y la ampliación suma 30 unidades del estrato, sorteadas con `:ampliacion:`. La de
    ítems y la de RI no. Ningún freno.
  - La regla del 25 % de la cola se dispara: es cifra y vigilancia, no freno.
- **Sobre ese FRENO** (decisiones de la autora):
  1. para sellar la lectura de la ampliación, un convertidor y un LEEME con el sha256 de la planilla en blanco de la ampliación, sin
     cambiar lo que hacen con las 8 muestras del primer tramo. La mesa armó uno nuevo,
     `t4/ampliacion/lectura_autora/convertir_lectura_T4_ampliacion.py`, con `LEEME_lectura_T4_ampliacion.md`, probado en carpetas
     temporales (10 de 10). Entran con el commit del segundo tramo;
  2. la exclusión de `data/experiment/neo4j/volumen` en la copia del repo: aceptada, declarada;
  3. el texto «umbrales_t4_tf,json» de `tasas_t4_tramo2.json` se corrige cuando se rehagan las tasas en el tercer tramo;
  4. que la unidad haya abierto `tanda1/t3/scripts/celdas_t4_t3f.py` y calculado el sha256 de dos `kg.json` de `tanda1/t3/acumulado/`
     contra su sello: aceptado, declarado.
- **El calendario v12i** (`decisiones_227_mesa/calendario/` del paquete de la mesa, desde las 18:30, con duraciones NO VERIFICADAS):
  - entran el atraso de T4, la ampliación con la lectura de la autora de 30 unidades y su tercer tramo, y la etapa c de U-ENTORNO-LIMPIO
    antes de la D-6 y de A2.1;
  - el sello de la tanda final queda el 22/10 a las 10:00 en el central (08:10 en el rápido y 13:39 en el lento);
  - las corridas de B6.3, el domingo 25 de 13:42 a 21:48 en el central; en el rápido, del sábado 24 a las 18:20 al domingo 25 a las
    00:24; en el lento, del lunes 26 a las 17:04 al martes 27 a las 05:13;
  - después del corte del miércoles 28 a las 18:00 quedan:
    - en el central, el cierre de la cobertura de V (jueves 29, 09:03) y dos pasos sin plazo (U-ESPEC-HARNESS y U-MED-DESAMB);
    - en el lento, la cobertura de V entera, el final de la etapa T y U-MED-DESAMB;
    - en el lento, además, N7 pasa el corte del sábado 24 y la firma de B6.3 pasa su plazo.
- Las secciones anteriores no se editan.

## 86. La etapa c de U-ENTORNO-LIMPIO revisada, los selftests del banco antes del commit y Neo4j con la lista de permitidas (21/10/2026)

Decisiones y hechos de la autora del 21/10/2026, recibidos a las 23:30:21 (hoja de ruta de la mesa, §229).

- **El TF4b, el 154 v2 y el 155** corrieron con su push (`4cc8f857`, `9c016693` y `46070985`). Sus archivos dan los mismos sha256 que
  los del paquete de la mesa.
- **La etapa c de U-ENTORNO-LIMPIO, revisada:**
  - 234 de 234 archivos;
  - el patch, sobre los blobs de HEAD, da `lanzar_agente.py` `b5e2e912…`, `lanzar_agente_a2_1.py` `9553c6ef…`,
    `selftest_entorno_limpio.py` `97e5e8bb…` y `contrato_metadata.md` `891a3138…`;
  - el selftest da 36 de 36 en un arenero de la mesa (25 contra la b2 y 6 contra HEAD).
  - Según su FRENO, la captura no trae estado de git ni el nombre del brazo, el control positivo de git lo detecta y el cwd quedó vacío
    en las 15 tomas. La unidad terminó sus corridas a las 18:32, y el FRENO llegó a las 23:13 por un corte de conexión de esa sesión.
- **Los selftests del banco, antes del commit** (decisión de la autora), tal cual: «agentes/selftest_metadata.py y
  smoke/selftest_integrador.py tienen que pasar antes del commit de U-ENTORNO-LIMPIO, a USD 0, con el .venv del repo y Neo4j corriendo.»
  - Son la única prueba del brazo kg real con el lanzador nuevo antes de las sesiones pagas.
  - En la etapa c frenaron en el primer paso que lanza el servidor del grafo: la copia no tenía `.venv` y Neo4j no corría.
  - **Cómo** (PROPUESTA de la mesa, la etapa c2, PENDIENTE de la autora): el `.venv` del repo, clonado en la copia con `cp -c`, y Neo4j
    en un contenedor propio de la ejecutora, en el 7687, con la base de la copia; sin escribir en el repo ni tocar su contenedor.
- **El commit de U-ENTORNO-LIMPIO no depende de que HEAD siga siendo el de hoy** (decisión de la autora). Controla la base de cada
  archivo y que el 155 esté en la historia, así que corre también después del commit de la autora con tres figuras del cap. 4. Ese
  commit no corre mientras haya una ejecutora con foto del repo.
- **Neo4j con la lista de permitidas** (lectura de la mesa en el código: `data/experiment/neo4j/conexion.py:22-24` y los JSON de MCP del
  grafo, que no pasan ningún `NEO4J_*`):
  - con la lista, ningún `NEO4J_*` del padre llega al servidor del grafo, y este toma los valores por defecto: localhost:7687 y las
    credenciales de desarrollo;
  - los despachos de N5 y de U-NAV-DESDE ponen un Neo4j propio en otro puerto con `NEO4J_URI`, y la v5 de U-BANCO-PARALELO también.
    Con el lanzador nuevo, ese valor no llega al servidor.
  - **Qué hacer** (PROPUESTA de la mesa, PENDIENTE de la autora): sumar `NEO4J_URI` a la lista, que no es una credencial y es igual en
    los dos brazos; o que el Neo4j de cada corrida escuche en el 7687.
- **El calendario v12j** (`decisiones_229_mesa/calendario/` del paquete de la mesa, desde las 00:45 del 22/10, con duraciones NO
  VERIFICADAS), con la etapa c2 antes del commit de U-ENTORNO-LIMPIO:
  - el sello de la tanda final queda el 22/10 a las 15:30 en el central (13:40 en el rápido y 19:09 en el lento);
  - las corridas de B6.3, del domingo 25 a las 17:07 al lunes 26 a las 01:13 en el central; en el rápido, el domingo 25 de 09:43 a
    15:47; en el lento, el martes 27 de 08:41 a 20:50;
  - después del corte del miércoles 28 a las 18:00 quedan:
    - en el central, el final de la cobertura de V (jueves 29, 11:58) y U-MED-DESAMB, sin plazo;
    - en el lento, la cobertura de V entera y el final de la etapa T;
    - en el lento, además, N7 y la re-aplicación pasan el corte del sábado 24 y la firma de B6.3 pasa su plazo.
- Las secciones anteriores no se editan.

## 87. La ampliación de T4 leída, el gold de V que no pasa y el juez v2 como estudio exploratorio (22/10/2026)

Decisiones y hechos de la autora del 21/10/2026, recibidos a las 23:39:53 (hoja de ruta de la mesa, §230).

- **La lectura de la ampliación de T4:** la autora la selló el 21/10/2026 a las 23:38:02
  (`tanda_final/t4/ampliacion/lectura_autora/sello_lectura_T4_ampliacion.txt`; la marcada da `155e23dc…`), y la planilla original no
  cambió. La mesa la controló: 11 de 11, con la conversión corrida de nuevo byte a byte (`t4/ampliacion/control_lectura_mesa/`). Entra
  con el TF4c, y después va el tercer tramo de T4: las aceptadas no ítems sobre las 60 y el freno por la atención sobre las 60.
- **El análisis del gold** (`tripletas_v_juez/corridas/analisis_gold_V.json`), corrido por la autora con la v1_3 (la regla del gold,
  `32b03107…`) y el código de la v1.4d, y revisado por la mesa. La decisión del §4.6 es «no pasa» en las dos cifras, y las dos dan la
  misma; rige la de las 100.
  - **Con las 100:**
    - (i) 81 de 99, que no pasa: el Wilson inferior da 0,7308;
    - (ii) cruda 0,0202 y ponderada 0,0198;
    - (iii) 14 de 24;
    - 1 a adjudicación;
    - la importancia exacta, 57 de 100, no pasa; a un nivel, 94 de 100.
  - **Sin las 10 del piloto:**
    - (i) 77 de 90;
    - (ii) cruda 0,0333 y ponderada 0,0261;
    - (iii) 14 de 22;
    - 0 a adjudicación;
    - la importancia exacta, 51 de 90, no pasa; a un nivel, 84 de 90.
- **La consecuencia del §4.6** (decisión de la autora): el juez no escala; la precisión de V queda con las 100 de la autora, y la de T se
  mide con la muestra humana de 100 (§7).
- **El juez v2** (decisión de la autora), tal cual: «Quiero recalibrar el juez de precisión con una v2, en un estudio aparte y
  exploratorio que no cambia la decisión del §4.6 ni las cifras de V y de T»:
  - «el material de calibración son mi gold de V y el pool de 20. Las correcciones van como ejemplos resueltos en las fronteras de la
    importancia y de «correcta», no como reglas nuevas en el prompt»;
  - «antes de iterar, se fija cuándo se frena la calibración. Antes de probarla, la v2 se congela y su criterio de prueba queda escrito:
    el mismo del §4.6»;
  - «la prueba es fuera de muestra, contra mi lectura de la muestra humana de T, después de que la selle. El juez corre recién entonces,
    y yo no veo nada suyo antes de leer»;
  - «la v2 no se vuelve a medir contra el gold de V».
  - **El diseño** (PROPUESTA de la mesa, PENDIENTE de la autora; `decisiones_230_mesa/juez_v2/` del paquete de la mesa):
    - como máximo 3 iteraciones, con el freno antes si una no mejora en al menos 2 puntos;
    - tres pedidos por ficha, como el gold;
    - unos USD 42 con el máximo (NO VERIFICADO), con tope 60 y freno 50;
    - la última prioridad en el carril pago y en las otras colas;
    - una nota fechada al pie del pre-registro de tripletas, antes de la primera iteración, y el commit de la congelación antes de la
      prueba.
- **El calendario v12k** (`decisiones_230_mesa/calendario/` del paquete de la mesa, desde la 01:30 del 22/10, con duraciones NO
  VERIFICADAS):
  - el sello de la tanda final queda el 22/10 a las 13:54 en el central (12:27 en el rápido y 16:48 en el lento);
  - las corridas de B6.3, del domingo 25 a las 16:22 al lunes 26 a las 00:28 en el central;
  - la lectura de la autora de la muestra de T va después de la firma de B6.3: en el central, del domingo 25 a las 16:16 al martes 27 a
    las 09:23;
  - con el juez v2 o sin él, los hitos dan lo mismo;
  - después del corte del miércoles 28 a las 18:00 quedan, en el central, el final de la cobertura de V (jueves 29, 11:13), U-MED-DESAMB y
    la prueba de la v2.
- Las secciones anteriores no se editan.

## 88. NEO4J_URI en la lista, la etapa c2 revisada, el juez v2 con Opus 5.5 y la medición de T, la muestra de T y el freno de T4 (22/10/2026)

Decisiones, preguntas y hechos de la autora del 22/10/2026, recibidos a las 10:44:50, 11:19:29, 11:29:11, 11:32:26 y 11:57:03 (hoja de
ruta de la mesa, §231 a §235), y lo que revisó la mesa.

- **El 156 y el TF4c**, corridos con su push (`5b1d9082` a las 10:42:19 y `a4911b53` a las 10:42:34, git log). Sus archivos son, byte a
  byte, los del paquete de la mesa.
- **`NEO4J_URI` entra en la lista** (la §86 la traía como propuesta; decisión de la autora, la opción a), tal cual: «Es una dirección, no una credencial, y el
  servidor del grafo aborta si KG_Meta no da el sha256 sellado: un NEO4J_URI equivocado frena en vez de leer otro grafo.»
  - **La etapa c2 de U-ENTORNO-LIMPIO lo implementó** (FRENO de las 11:44; su llegada, en el mensaje de las 11:57:03; paquete de 387
    archivos, manifest `55acdcb4…`):
    - `ENTORNO_PERMITIDAS = ("PATH", "HOME", "NEO4J_URI")`, y ninguna otra `NEO4J_*` pasa;
    - el selftest del entorno da 37 de 37;
    - los dos selftests del banco, `selftest_metadata.py` y `selftest_integrador.py`, pasan con una copia del `.venv` del repo y un
      Neo4j propio en `127.0.0.1:37687`, a USD 0;
    - `NEO4J_URI` llega al servidor del grafo por el lanzador: en 7687 no escuchaba nada.
  - **La revisión de la mesa** (`decisiones_231_mesa/entorno_limpio/`, en su paquete):
    - reprodujo la etapa por código: el paquete, el patch sobre los blobs de HEAD y, contra la etapa c, un solo nodo distinto por AST, la
      lista;
    - cambió el ancla de los comentarios, de §86 a §88, sin cambiar el AST;
    - corrió el selftest en tres areneros: 37, 26 y 6 de 37, como la ejecutora.
  - **Un error propio de la ejecutora, declarado:** mostró la contraseña de desarrollo del grafo, la de `conexion.py`, en la salida de una
    herramienta de su sesión, no en un archivo.
  - **Lo que sigue:** el 157 se rearma con los cuatro archivos de la c2 y va después de este registro. U-BANCO-PARALELO pasa a la v6, que
    exporta `NEO4J_URI` al puerto de su contenedor. El «seguí» de la etapa c de la D-6 pasa a su v2.
- **La fecha del CLI y el orden de las corridas de B6.3** (pregunta de la autora, 11:57:03): el CLI escribe la fecha del día en el
  pedido, y la etapa c2 la enmascaró solo para comparar. Hoy nada fija el orden de las corridas de B6.3 entre brazos: está fijado el k, no
  el orden. La mesa propone que el pre-registro de B6.3 las fije intercaladas, por pregunta y por repetición, con los brazos de cada
  pregunta seguidos en un orden sorteado, y que cada sesión registre su fecha; el análisis declara cuántos bloques tienen fechas distintas
  entre brazos (`decisiones_231_mesa/b63/`). La v6 de U-BANCO-PARALELO registra la fecha de cada sesión. PENDIENTE de la autora.
- **El juez v2: lo decidido el 22/10 a las 10:44:50** (§231, punto 2), tal cual:
  - la regla de freno: «como máximo 3 iteraciones, y se frena antes si una no mejora en al menos 2 puntos ni el acuerdo de «correcta» ni
    el exacto de la importancia, o si no deja ningún ejemplo nuevo»;
  - «tope USD 60 y freno USD 50»;
  - «va en una sesión nueva, abierta en tripletas_v_juez»;
  - «los ejemplos resueltos los propone la ejecutora desde los desacuerdos, con la justificación sacada del texto del TO, y yo los apruebo
    antes de cada iteración paga»;
  - las 10 hojas del gold, en la carpeta de lectura de la autora: la ejecutora las lee en su lugar, por nombre, con la función del análisis
    del gold, que controla cada sha256 contra su sello y devuelve solo «correcta» e importancia. No las copia, no lista la carpeta y no lee
    otro archivo de ella.
- **El juez v2: lo decidido a las 11:19:29**, que reemplaza lo anterior sobre la medición de T. Tal cual:
  - «El modelo de la v2 es claude-opus-5-5, a temperatura 0, en lugar de claude-sonnet-4-6. Lo decido ahora y no se comparan modelos
    sobre el material.»
  - «Quiero que la T la mida el juez si la v2 lo demuestra sobre T»:
    - su lectura de la muestra humana de 100 de T se hace igual, «ciega al juez y sin propuestas de ningún modelo, como el gold de V»;
    - la v2, congelada, corre sobre esas 100 con el criterio del §4.6 «tal cual»;
    - «si pasa, la v2 mide la T con el diseño del §7: las 400 aristas del grafo evaluado, con la estratificación de 3.2 y los dos
      estimadores de 3.6, y esa es la medición de T. Mis 100 quedan como su validación»;
    - «si no pasa, la T queda con mis 100, como dice la §87»;
    - «la prueba de la v2 corre apenas selle T, con prioridad, no al final de las colas».
  - **Lo que encontró la mesa:** Opus 5.5 no acepta `temperature`: la API responde 400 con cualquier valor. Su razonamiento no se apaga, y
    el esfuerzo es su único control, `medium` por defecto (la referencia de la API, skill claude-api, tabla de razonamiento y esfuerzo por
    modelo). «A temperatura 0» no se puede cumplir tal cual. PENDIENTE de la autora; la mesa propone sin `temperature` y con el esfuerzo
    `medium`, fijado antes de iterar.
  - **Lo que la enmienda 4 declara como desvío** de textos firmados: el §4.1 (el modelo), el §4.3 y el §4.7 (los casos del gold y una
    segunda recalibración), el §7 (la validación con 100 en lugar de 30) y la letra del laudo D-f, §1 (el instrumento validado sobre el
    conjunto de desarrollo).
  - **El costo con Opus 5.5** (NO VERIFICADO; `decisiones_231_mesa/juez_v2/costo_juez_v2_opus55_mesa.py`, en el paquete de la mesa): con
    las 3 iteraciones, USD 85 a 255, y 146 en el central (las iteraciones 63, la prueba 21 y las 300 restantes de las 400, 62). El tope de
    USD 60 no cubre en el central las iteraciones y la prueba (84). Los topes por paso que propone la mesa (2, 42, 42 y 125) quedan
    PENDIENTES de la autora.
  - **El texto de la enmienda 4,** PREPARADO por la mesa (`decisiones_231_mesa/juez_v2/`); su firma, PENDIENTE. El despacho de la
    etapa a, escrito.
- **La muestra de T antes de la firma de B6.3** (pregunta de la autora, 11:29:11): «¿se puede sortear y armar sus fichas apenas se selle
  el grafo evaluado, sin esperar la firma del pre-registro de B6.3? [...] Si se puede, quiero empezar a leer el sábado.» La respuesta de
  la mesa:
  - el sorteo y las fichas, sí, apenas se selle el grafo evaluado: el diseño está en 3.2 y en el §7, y la enmienda 4 fija la semilla y las
    400 con las 100 adentro;
  - la lectura antes de la firma de B6.3 se aparta de la letra del laudo D-f, §5 («B6.3 incorpora las tripletas dentro de su pre-registro
    sellado»), y del §7 de este pre-registro: pide una nota firmada;
  - la lectura antes de la última ola de B6.3 deja de ser ciega para la revisión de sus preguntas, porque ve aristas del grafo evaluado
    sobre los documentos de test;
  - en el calendario v12l, leer desde el sábado pasa la firma de B6.3 de su plazo en el central (lunes 26 a las 16:45, contra las 12:00) y
    no adelanta las 400. Decisión PENDIENTE.
- **El freno de T4 de la tanda final** (FRENO del tercer tramo, 11:19:30; mensaje de la autora, 11:32:26): salta el freno por la atención
  sobre las 60 en las aceptadas no ítems.
  - Las cifras: 16 de 60, ponderada 0,3733, Wilson [0,2160; 0,5630], contra el umbral de 0,2437 (p 0,0009). El freno por intervalos no
    salta, y la verificación aparte da 62 de 62.
  - **La revisión de la mesa** (`decisiones_231_mesa/t4/`):
    - el paquete da 47 de 47, y la reproducción sobre una copia, 6 de 6;
    - por celda y por tramo: NG resto, que es el tramo 2, 8 de 20, el 93 % de la ponderada; el tramo 1, 8 de 40;
    - la diferencia entre tramos no es significativa con estas n (Fisher, p 0,1265), y los errores no se concentran en documentos.
  - **Lo que fijan las reglas:** los pre-registros de la tanda 1 (§5.4 a) y de la tanda final (§6) fijan cuándo hay freno, no qué sigue.
    El protocolo entre tandas (§6) y la regla de caída dan el marco. Las opciones y la recomendación de la mesa están en su paquete.
  - **Decisión PENDIENTE:** la autora no decide hasta leerlo, y ningún commit de T4 corre antes.
- **El calendario v12l** (`decisiones_231_mesa/calendario/`, desde las 13:30 del 22/10, con duraciones NO VERIFICADAS):
  - con la v2 después de B6.3 y las tres repeticiones en paralelo, la prueba y las 400 quedan revisadas el martes 27 a las 19:42 en el
    central (22,3 h antes del miércoles 28 a las 18:00), y no entran en el lento;
  - la v2 no mueve ningún hito de B6.3;
  - N7 pasa su corte en el central (sábado 24 a las 13:03, contra las 12:00), con la v2 o sin ella;
  - en el central, las corridas de B6.3 cruzan la medianoche del domingo 25 al lunes 26.
- Las secciones anteriores no se editan.

## 89. El freno de T4 por la clasificación de la autora, el tramo 1 sellado como respaldo, el orden de B6.3, la lectura de T, la enmienda 4 y N7 (22/10/2026)

Decisiones de la autora del 22/10/2026, recibidas a las 12:24:43 (hoja de ruta de la mesa, §236).

- **El 158 y el 157 v2,** corridos con su push (`368d50a3` a las 12:22:52 y `ca5d192f` a las 12:23:07, git log). Sus archivos son, byte a
  byte, los del paquete de la mesa. Los comandos de la mesa son scripts de zsh: se corren con `zsh`, no con `bash`.
- **El freno de T4** (decisión de la autora), tal cual: «la opción 2 y después la 1. Hoy clasifico por tipo las 16 unidades con error
  [...]. Si no aparece una falla de esquema, acepto el freno y se declara como residuo, con su tasa; si aparece, lo vemos antes de
  seguir. La opción 3 queda descartada: elegir el grafo por el resultado de su lectura sesga B6.3. El TF4d, cuando cierre la
  clasificación.»
  - **El material** (`decisiones_236_mesa/t4/clasificacion/`, en el paquete de la mesa): una planilla con las 16 y cuatro columnas para la
    autora:
    - `capa`, con el vocabulario `capa_pipeline` del protocolo entre tandas (§2);
    - `falla_de_esquema`, con el umbral del procedimiento (c) del protocolo (§6);
    - `campo` y `se_repite`.
  - Lo acompañan el preparador, el convertidor y el LEEME, y el sello va como el de las lecturas de T4. La prueba de la mesa da 17 de 17,
    y la planilla esperada da el sha256 `e45f6e70…`.
  - Una «no_se» en `falla_de_esquema` cuenta como una «sí»: se ve antes de seguir (propuesta de la mesa, escrita en el LEEME).
- **El tramo 1 se sella como respaldo antes del viernes 23 a las 18:00** (decisión de la autora). Ya están su E0 y sus ensamblados
  (`71cb9305`), su suite y sus shapes (T3) y las lecturas de sus celdas (T4). Lo que le falta va en T5, que corre ya, en paralelo con la
  clasificación: su costo, su columna del tablero y el registro de sus dos grafos en `neo4j/grafos.py`, con su vista. NO VERIFICADO:
  - el control de las carpetas de salida de sus 30 TOs al cerrar el tramo 1 (enmienda 9, punto 6);
  - si su columna del tablero sale de lo que contó T3;
  - y la carga en Neo4j, que no se hace, declarada.
- **El orden de las corridas de B6.3** (decisión de la autora): «por pregunta y por repetición, con los brazos de cada pregunta seguidos y
  en un orden sorteado, y la fecha de cada sesión registrada. Va en su pre-registro.»
- **La lectura de T** (decisión de la autora): «Leo T después de la firma de B6.3, como dice el §7. El sorteo y las fichas, apenas se selle
  el grafo evaluado.»
- **La enmienda 4** (decisiones de la autora sobre los seis puntos de la mesa), tal cual:
  - «el modelo: claude-opus-5-5, sin temperature y con el esfuerzo medium puesto explícito»;
  - «sin respaldo en otro modelo: el pedido rechazado queda sin voto y se cuenta»;
  - «la mejora de cada iteración se mide sin las fichas que son casos del prompt»;
  - «mis 100 de T van dentro de las 400»;
  - «los topes por paso que propusiste: 2 el humo, 42 cada iteración, 42 la prueba y 125 las 300 restantes»;
  - «la lectura de T, después de la firma de B6.3».
  - La firma es el commit que agrega la nota al pie del pre-registro de tripletas, con una nota al pie del laudo D-f por el desvío de su
    §1 (PENDIENTE de la autora).
- **N7** (pregunta de la autora, que ve en el calendario v12l N7 a las 13:03 del sábado, contra el corte de las 12:00):
  - **qué pasa si lo pasa:** el mandato de U-NAV pide N7 sellado antes del corte y antes del pre-registro de B6.3, que lo declara, y no
    escribe qué sigue si no llega. Lo que depende de N7 es ese pre-registro, que en el central empieza el domingo: pasar las 12:00 rompe la
    letra del mandato, y se declara, pero no mueve B6.3;
  - **lo que la mesa no había dicho en la §88:** en el mismo v12l central, la medición de la re-aplicación única también caía después del
    corte. Por R5 de la enmienda 8 al protocolo, lo del grupo 2 que a las 12:00 del sábado no tenga su medición hecha va al grafo corregido,
    no al evaluado. Es lo que más cuesta del corte;
  - **lo que se puede adelantar:** correr T5 ya, en paralelo con la clasificación. En el calendario v12m (desde las 14:30, con duraciones NO
    VERIFICADAS), en el central N7 cae el sábado a las 09:45 y la re-aplicación se mide el viernes a las 14:28, las dos antes del corte. Con
    T5 después del TF4d caen el sábado a las 16:18 y a las 13:33. Más horas el viernes no suman en el central. En el lento no alcanza.
- Las secciones anteriores no se editan.

## 90. T5 de la tanda final revisada, el freno de T4 aceptado como residuo, los sellos del tramo 1 y de la tanda, y lo que T5 deja abierto (22/10/2026)

Decisiones de la autora del 22/10/2026, recibidas a las 16:16:41 y a las 16:24:48 (hoja de ruta de la mesa, §237 y §238).

- **El 159,** corrido con su push (`fe80d354`, a las 13:31:54, git log). El preparador de la clasificación dio la planilla `e45f6e70…`,
  la que esperaba la mesa (§89).
- **T5** (su FRENO llegó a las 14:08, mensaje de la autora). La mesa lo reprodujo sobre una copia del repo, a USD 0:
  - los diez scripts de `t5/scripts/` que dan sus salidas, corridos de nuevo, dan cada salida y cada consola byte a byte: 32 de 32
    controles (`t5/control_mesa/reproduccion_T5_mesa.json`);
  - el costo, con código propio sobre `gasto_usd` de cada fase cerrada, da lo mismo, 6 de 6: real USD 97,598343, del que el tramo 1 es
    12,856189 y el tramo 2, 84,742154 (`t5/control_mesa/costo_independiente_T5_mesa.json`).
- **1. La copia de T5 sin `t4/clasificacion_freno/`:** aceptada (decisión de la autora).
- **El freno de T4, por la regla del §89.** La autora selló su clasificación a las 16:20:27 (`t4/clasificacion_freno/`, la marcada con
  sha256 `7ab3b335…`, en su sello). El control de la mesa, sin leer las notas ni imprimir ids (`t4/clasificacion_freno_control_mesa/`):
  - la planilla es la esperada, la marcada da su sello y sus 16 filas traen las siete columnas fijas de la planilla;
  - el convertidor, corrido de nuevo sobre una copia de la exportación, da la marcada byte a byte;
  - la cuenta: `falla_de_esquema` «no» en las 16. La capa es E1-prompt en las 16, y una lleva además ensamblado. En 12 de las 16, el mismo
    patrón aparece en otra de ellas.
  - **Sin falla de esquema, el freno se acepta y se declara como residuo, con su tasa:** 16 de 60, ponderada 0,3733, Wilson de Kish
    [0,2160; 0,5630] (`t4/tasas/tasas_t4_tramo3.json`, `aceptadas_no_items_sobre_60`). Entra al backlog como BKL-0056.
- **2. Los criterios del tablero y de las vigilancias** (PROPUESTA de la mesa, PENDIENTE de la autora;
  `decisiones_237_mesa/t5/revision_criterios_tablero_T5_mesa.md`, en el paquete de la mesa):
  - **fila 50:** la meta es de precisión y la lectura de la tanda final no la mide (la (12) va sin `remite_a`, pre-registro de la tanda
    final, §6). Va como hallazgo, «no medida», como en la tanda 1;
  - **fila 52:** la cuenta de la meta, cero nodos de contenido sin `establecida_en`, está en el reporte de cada ensamblado y da 0 en los
    ocho; T5 contó otra cosa. «El resto, declarado por causa» no se hizo: 331 Condicion sin regla y 34 aislados (32 Comunicacion y
    2 Sujeto) van sin causa, y eso va como hallazgo;
  - **fila 64:** 85 Comunicacion.tipo sin marca ni original. El residuo que la meta declara es el de dos grafos anteriores, con una
    corrección antes de escalar que la tanda final no tiene aplicada. En la tanda 1 la misma cuenta fue hallazgo (H17,
    `tanda1/t5/reporte_tanda1.md:214`): no cumple, hallazgo;
  - **fila 51:** «no aplica», como en la tanda 1, con la cuenta (0) declarada;
  - **las vigilancias:** el criterio de T5 no lo fija ningún pre-registro. La mesa propone el test de la atención de las lecturas: exacto,
    unilateral, al 5 %, contra la tasa de la tanda 1, crudo y ponderado por celda. Si las dos versiones no dan lo mismo, hallazgo
    (`t5/control_mesa/criterio_vigilancias_mesa.json`).
    - En la (1), p crudo = 0,0258 y p ponderado = 0,0832: las dos versiones no dan lo mismo, así que va como hallazgo, como la dejó T5.
    - (2), (3) y (7) no empeoran.
    - Las contadas sin leer no dan hallazgo: (4) y (5) cumplen su invariante; en (8), p = 0,6824; en (9), 0 emisiones fuera de los TOs de
      pagos.
- **3. El sello del tramo 1, con el control por fecha de la autora, reproducido por código** (solo lectura, sin nombres de archivos ni
  cuentas por carpeta; `t5/sello_tramo1_control_mesa/control_fechas_salida_tramo1_mesa.json`):
  - en `reextraccion_v2/corpus_tanda_final/salida_r2b/`, el último archivo de los 30 TOs del tramo 1 es del 19/10/2026 a las 08:43:29 y el
    primero de los 68 del tramo 2, de las 08:47:33. Da lo mismo con la hora de modificación y con la de cambio de estado;
  - las carpetas mismas del tramo 1, que cambian si se agrega o se borra un archivo, cambiaron por última vez a las 02:35:18;
  - desde `b17746be`, nada cambió en `salida_r2b/`: el diff y el status, con los sin rastrear, dan vacío, y git no ignora ningún archivo
    ahí;
  - **el sha256 de las carpetas del tramo 1 al cerrarlo no se tomó: se declara.** El de hoy es el que da T5 (`t5/salidas/carpetas_tramo1_t5.json`).
    La carga en Neo4j no se hizo y se declara.
- **4. La capa de las 6 incorrectas de ítems y de las 12 de la cola:** el protocolo entre tandas (§2) y el pre-registro de la tanda 1
  (§5.6) piden que lo diferido vaya al backlog con su `capa_pipeline`. El sello (§4) no incluye el backlog, y la tanda 1 se selló con
  «no dicha por la lectura». **No se pide antes del sello.** Por la decisión de la autora, van al backlog sin capa (BKL-0053 y BKL-0054),
  y la autora las clasifica después del corte del sábado.
- **5. La fila 67 y la observación (12):** ninguna tiene una corrección lista; las dos propuestas de T5 dicen «a diagnosticar». El mandato
  firmado de U-REAPL (§1) solo admite lo que llegue con mandato firmado, código y medición antes del corte.
  - Para entrar harían falta el diagnóstico, el código y la medición, NO VERIFICADO: unas 3 h de una ejecutora para una y 5,5 h para las
    dos, más la enmienda del mandato y su firma.
  - En el calendario v12n central, desde las 17:30, la re-aplicación medida pasa del sábado a las 08:04 a las 08:19, todavía antes del
    corte pero con un margen que se pierde con una hora de atraso; en el lento ya pasa el corte sin ellas.
  - **Se difieren, como propone T5** (decisión de la autora): BKL-0051 y BKL-0052.
- **6. Por qué el repartido del tramo 1 (USD 19,310012) se aparta del §3 (12,690115):** el repartido divide el mismo total por los
  caracteres de la E0 de cada TO, no por unidades. El tramo 1 tiene el 18,43 % de los caracteres y el 12,14 % de las unidades: son unidades
  más largas. El gasto real siguió a las unidades: 13,17 % del total (`t5/control_mesa/costo_independiente_T5_mesa.json`).
- **El backlog:** seis entradas nuevas, BKL-0051 a BKL-0056: las cinco propuestas de T5, con su texto, y las 16 del freno de T4.
- **El sello de la tanda final** (protocolo entre tandas, §4). Lo que pide:
  - la E0, en `5052364f`; la extracción, en `b17746be`; los `kg.json` con sus registros, la suite y los shapes, en los dos commits de
    T3 (`71cb9305` y `5aae4fe0`). La §89 ponía la E0 en `71cb9305`: es la de `5052364f` (git log de su carpeta);
  - el reporte con su costo real y la columna del tablero, en el commit de T5.
  - Este commit cierra la serie: va después del de la cuarta etapa (el tercer tramo con la clasificación), el de T5 y el sello de los
    grafos del tramo 1, y lo controla por sus títulos.
- **El calendario v12n** (`decisiones_237_mesa/calendario/`, desde las 17:30, el cierre de la ronda, con duraciones NO VERIFICADAS; el
  modelo es voraz):
  - en el central, el sello de la tanda queda el jueves 22 a las 18:00;
  - la re-aplicación medida, el sábado 24 a las 08:04, y N7 a las 10:49: las dos antes del corte de las 12:00;
  - eso pide correr los commits enseguida: con el cierre a las 18:30 las dos pasan el corte (sábado 13:45 y 16:30);
  - si las horas de la autora del viernes van primero al censo, al catálogo y a la re-aplicación, antes que a A2.1 y A2.2, la
    re-aplicación se mide el viernes con cualquier cierre (el 23 a las 14:37 desde las 17:30), y N7 pasa el corte (sábado 18:06).
- **El orden de los commits:**
  1. el de la cuarta etapa: el tercer tramo con la clasificación y su control;
  2. el de T5;
  3. el sello de los grafos del tramo 1, con el control por fecha;
  4. este;
  5. la firma de la enmienda 4 (el 160, PENDIENTE de la autora).
- Las secciones anteriores no se editan.

## 91. La tanda final sellada, los criterios del tablero fijados, la prioridad del viernes, el censo de C1 de las tres tandas y lo que sigue (22/10/2026)

Decisiones y hechos de la autora del 22/10/2026, recibidos a las 18:13:48 (hoja de ruta de la mesa, §239).

- **Los cuatro commits de la §90,** corridos con zsh, en orden, con su push (git log): el TF4d (`4d8adf0d`, 18:11:38), el TF5a (`aeaf0ec1`,
  18:11:44), el TF5b (`2a95f475`, 18:11:50) y el 161 (`2a7fd75d`, 18:11:56).
  - La mesa los controló contra su paquete, 19 de 19: sus títulos y su orden sobre el 159, sus archivos, byte a byte o por el sha256 de la
    lista revisada, sin Co-Authored-By, y `grafos.py` con `aeaf0ec` en los dos sellos del tramo 1
    (`decisiones_239_mesa/verificacion/verificacion_commits_TF4d_TF5_161_mesa.json`, en el paquete de la mesa).
  - **La tanda final queda sellada** (protocolo entre tandas, §4), con el tramo 1 como respaldo, antes de la regla de caída del viernes 23
    a las 18:00.
- **La etapa c de la D-6:** la autora pegó el «seguí» v2 en su sesión con una precisión suya al paso 0, tal cual: «en el diff contra
  bb6dc713 pueden aparecer además data/experiment/neo4j/grafos.py y data/backlog/backlog.jsonl, de los commits del sello de la tanda
  final, y esos dos no frenan». La D-6 trabaja fuera del repo: del repo lee su paso 0 y el lanzador del banco, y un commit del
  registro y del backlog no cambia nada de eso.
- **El 160** (la firma de la enmienda 4): PENDIENTE de la autora.
- **1. Los criterios del tablero y de las vigilancias** (decisión de la autora, sobre la propuesta de la §90): las filas 50, 52 y 64 van
  como hallazgos y la 51, «no aplica»; las vigilancias, con el test de la atención, crudo y ponderado, y la (1) como hallazgo. **Se
  declaran como criterios fijados con los resultados a la vista.** Entran al backlog como BKL-0057 (fila 50), BKL-0058 (fila 52) y
  BKL-0059 (fila 64); la (1) ya está como BKL-0055.
- **2. La prioridad del viernes** (decisión de la autora), tal cual: «El viernes, mis horas van primero al censo, al catálogo y a la
  re-aplicación, antes que a A2.1 y A2.2: que la re-aplicación se mida antes del corte pesa más que N7, que si pasa el corte se declara.»
  Cambia, para el viernes, el orden de la §76 (A2.1, A2.2 y el diagnóstico primero).
- **3. El calendario v12o** (`decisiones_239_mesa/calendario/`, con el sello a la hora del git log y esa prioridad, desde las 18:45, el
  cierre de la ronda; duraciones NO VERIFICADAS; el modelo es voraz). En el central, contra el miércoles 28 a las 18:00:
  - la re-aplicación medida, el viernes 23 a las 14:46, y el sello del grafo evaluado, a las 16:01: antes del corte;
  - N7, el sábado 24 a las 18:06: pasa el corte de las 12:00 y se declara;
  - la firma de B6.3, el domingo 25 a las 21:31 (plazo: lunes 26 a las 12:00);
  - sus corridas, del domingo 25 a las 21:37 al lunes 26 a las 05:43;
  - la etapa T, cerrada el miércoles 28 a las 12:37, 5 h 23 antes; las 400 de la v2, revisadas el martes 27 a las 18:27;
  - la cobertura de V, el viernes 30 a las 09:53, después del miércoles 28, como en los calendarios anteriores;
  - en el lento, la firma de B6.3 pasa su plazo (martes 27 a las 17:15) y la etapa T, el miércoles 28 (viernes 30 a las 15:36). En los
    dos, la re-aplicación se mide el viernes (en el lento, a las 20:41);
  - sin la prioridad, en el central, la re-aplicación caería el sábado a las 08:10, N7 a las 13:03 y la firma de B6.3 el domingo a
    las 17:38: la prioridad corre N7 unas 5 h y la firma unas 4 h, a cambio de una re-aplicación que no depende de la hora.
- **El censo de C1 de las tres tandas,** armado por la mesa para la relectura de la autora (U-REAPL, §1; registro, §46 y §47), con su
  script de la §178 sin cambios, sobre el acumulado sin cola (`ens_128_r2b_sincola`, sha256 `398459a8…`) y la muestra de U-MED-VERIF
  controlada en memoria:
  - 472 Comunicacion; 32 colisiones con 120 nodos, hasta 25 documentos por colisión; ninguna toca la muestra;
  - C1 no crea ningún hub al 1 % (umbral 40; el grado de un nodo unido, a lo sumo 21) y crearía uno al 5 % (umbral 16), que se declara;
  - la carpeta de lectura es `fuera_del_repo/censo_c1_tres_tandas/`, con su `LEEME`, un convertidor (6 de 6 en su prueba) y el sello en
    zsh. La mesa no la abre.
- **El material de las claves del catálogo:** el despacho preparado en la §157, con sus huecos llenos (el sello `2a7fd75d`, el sorteo de
  las FICHAS y su lista de exclusión, el registro de las tres tandas), listo para pegar. No escribe en el repo.
- **El orden, desde esta noche:** el 162; el despacho del material del catálogo; la v2-a; el censo; las tres revisiones de FRENOs que
  esperan a la autora (U-REMISIONES-SUBPUNTOS a, U-UNION-C1 v3 y la etapa b), que gatillan el commit de U-PROC-HERENCIA, de C1 y de las
  remisiones; la revisión de la D-6 y sus tres sesiones pagas. Mañana: la lectura del catálogo, ese commit, el despacho de la re-aplicación
  y su medición, y después A2.1 y A2.2.
- Las secciones anteriores no se editan.

## 92. El viernes sin la noche: la D-6 revisada, la fila 67 y la (12) diferidas, el 160 con la fecha de hoy, el commit de U-PROC-HERENCIA, de C1 y de las remisiones, y el censo de C1 sellado (23/10/2026)

Decisiones y hechos de la autora del 23/10/2026, recibidos a las 08:54:36, a las 09:03:32 y a las 09:43:10 (hoja de ruta de la mesa, §240
a §242).

- **El 162,** corrido con su push (`8bea2edb`, a las 08:50:25, git log): 7 de 7 contra el paquete de la mesa.
- **El material de las claves del catálogo:** el despacho, pegado en una sesión nueva abierta en `fuera_del_repo/claves_catalogo/`, con
  una precisión de la autora al paso 0, tal cual: «en el diff contra 2a7fd75d pueden aparecer además docs/preregistro_evaluacion_tripletas.md
  y docs/laudo_D-f_secuencia_tripletas.md, de la firma de la enmienda 4, y esos dos no frenan».
- **La etapa a del juez v2:** pegada en una sesión nueva abierta en `fuera_del_repo/tripletas_v_juez/`, tal cual, con las tres propuestas
  de la mesa aceptadas: hasta 10 casos nuevos por iteración, las tres repeticiones en paralelo y el humo con 2 fichas fuera del material y
  de T.
- **El 160 v2:** el 160 no se corrió el 22/10, y su nota decía «FIRMADA el 22/10/2026». El 160 v2 lleva la fecha de hoy en las dos notas
  al pie (la del pre-registro de tripletas y la del laudo D-f), sin cambiar el texto de la enmienda. La semilla de la muestra de T conserva
  su texto (`B4-TRIPLETAS-T:sorteo:2026-10-22`), fijado antes de ver nada de T. Correrlo es la firma (PENDIENTE de la autora); el 160 de la
  §236 no se corre.
- **La etapa c de la D-6,** en FRENO (paquete `revision_UD6_TOPE_MCP_c/`, `4dcd3d80…`, 109 archivos, bajo la sesión retomada `9516a1f1`),
  revisada y reproducida por la mesa (`decisiones_240_mesa/d6/`, en su paquete):
  - 109 de 109 contra su manifest; el lanzador del banco es el de HEAD (`2f007420…`);
  - el selftest, corrido de nuevo sobre una copia, da 203 de 203; el criterio 3 del comando pago, 17 de 17, y la cota del costo es la
    misma (la de la guarda, USD 0,4274; con el máximo de cada rango, 0,5272, debajo del freno de 0,6);
  - **la recomendación:** sus tres sesiones pagas, hoy y primeras en el carril pago, con el comando de la sección 6 de su FRENO (tope 1,0
    y freno 0,6), antes del humo de A2.1 y del de la v2.
- **La fila 67 y la (12)** (pregunta de la autora; cuentas de la mesa por código, a USD 0, sobre el acumulado sin cola de las tres tandas,
  `decisiones_240_mesa/cuentas/`):
  - **el patrón de la (12):** 416 `aplica_a` van al rol de alcance de otro TO, de las 1.820 que van a un rol (238 de la tanda 0, 113 de la
    tanda 1 y 65 de la tanda final). 410 se resolvieron por la sugerencia del modelo. Se concentran en documentos emparentados (237 de
    `cap` al rol de `capmin`), donde el rol del otro documento puede ser el correcto, y hay un solo caso leído;
  - **el patrón de la fila 67:** 24 nodos con cuantía y sin `umbral` ni `plazo`, de 2.683, la cifra de T3. La única corrección sin lectura
    es la marca que la meta admite, y no cambia ninguna respuesta posible del agente;
  - **lo que harían falta:** la (12), una lectura, la regla, la enmienda del mandato de U-REAPL, el código en E4 y su medición, unas 5 h
    (NO VERIFICADO); la marca, la enmienda, el código y su medición, unas 3 h. En el calendario v12p, con los dos FRENOs de afuera
    llegados (§93), con 3 h la re-aplicación medida pasa el corte en el lento (sábado 12:20), y con 5,5 h también; en el central queda
    antes;
  - **las dos quedan diferidas,** por la regla de la autora («si no entra con margen, queda diferida»): BKL-0051 y BKL-0052 siguen como
    están, y los 24 de la fila 67 se declaran como residuo, como en la tanda 1.
- **El calendario v12p** (`decisiones_240_mesa/calendario/`, desde las 09:45, con la prioridad de la autora del viernes; duraciones NO
  VERIFICADAS): con los ajustes de esta ronda (los commits después de los FRENOs de las ejecutoras de afuera, el censo sellado y los dos
  FRENOs llegados), sus cifras van en la §93.
- **Las tres revisiones de la autora** (decisión de la autora, recibida a las 09:03:32): aprueba U-REMISIONES-SUBPUNTOS a (63 de 63, manifest
  `6564afbd…`), U-UNION-C1 v3 (50 de 50, `1e530358…`) y U-REMISIONES-SUBPUNTOS b, versión 2 (67 de 67, `13cb195c…`). Ninguno tiene casos de
  freno, y las `remite_a` nuevas de la etapa a dan las de sus salidas (14.047 y 13.854; con D, 14.133 y 13.940). El rc 0 del selftest de
  claves va como se fijó en la §209 de la hoja de ruta de la mesa.
- **La relectura del censo de C1 de las tres tandas,** sellada por la autora a las 09:22:53 (`censo_c1_marcado.csv`, `11c56dee…`, en
  `sello_censo_c1.txt` de `fuera_del_repo/censo_c1_tres_tandas/`; recibida a las 09:43:10): 32 filas, 32 `une_bien` y 0 `une_mal`, así que
  la regla une las 32 colisiones tal cual. La mesa la controló por código, sin mostrar ninguna nota ni ningún código
  (`decisiones_242_mesa/censo/`, 13 de 13): el marcado da su sello; la colisión, el código y los nodos de cada fila son los del censo; los
  archivos que armó la mesa no cambiaron; y el armador del 163 da vacía la lista de los códigos que no se unen (`aa6aa007…`). Esa lista
  va al despacho de la re-aplicación como argumento de `--union-comunicaciones`, con su sha256.
- **El 163, el commit de U-PROC-HERENCIA, de C1 y de las remisiones,** armado por la mesa (`decisiones_241_mesa/`, en su paquete):
  - nueve archivos copiados de sus paquetes por sha256: el ensamblado unido, `r1_referencias.py`, `r1_invariantes.py`, el selftest de
    claves con la normalización, los tres selftests nuevos y el armador de los códigos que no se unen; más la tabla de reprocesamiento;
  - **la tabla:** la de HEAD con F15f, F15g y F15h, y las 118 anclas de las filas F13 a F16b y de las tres nuevas leídas del código final.
    85 cambian; 21 caen en líneas que el unido cambió, y cada una se eligió por el identificador de su fila y se revisó. Los cuatro
    controles del armador dan bien, y las fichas de texto de F15h, 20 de 20;
  - **en el arenero,** después del commit real: R19 da rc 0 con una copia de las dos bases de la caché (`e1_extraccion.db` y
    `e3_verificacion.db`, con el mismo sha256 antes y después), con «contraste con la tabla: OK» y la R23 y la V23 en `gerc`. Los otros
    tres selftests dan 66 de 66, 67 de 67 y 39 de 39. La re-aplicación repite R19 como su primer control (§209).
- **El orden de hoy:** en la §93, con los dos FRENOs de afuera llegados. La regla que lo arma: ningún commit cruza la foto del repo de
  una ejecutora que lee lo que cambia. El 163 cambia `ensamblar_tanda0.py`, que la ejecutora del material del catálogo importa desde su
  copia del repo (lo importa `r2_1_medicion.py`); el 160 v2 y el commit de esta sección cambian el pre-registro de tripletas y el
  registro, que la de la etapa a de la v2 lee con `git show HEAD`.
- Las secciones anteriores no se editan.

## 93. El viernes, más tarde: la etapa a del juez v2 y el material del catálogo, revisados; el control del SDK; y el calendario con los dos FRENOs llegados (23/10/2026)

Decisiones y hechos de la autora del 23/10/2026, recibidos a las 09:54:35 y a las 10:04:43 (hoja de ruta de la mesa, §243 y §244).

- **La etapa a del juez v2, en FRENO** (paquete `revision_UTRIP_V_JUEZ_v2_a/`, `67d3204a…`, 30 archivos), revisada por la mesa por
  código (`decisiones_243_mesa/v2a/`, 19 de 19):
  - el paquete y la carpeta de trabajo coinciden; la v1 no cambió; los cuatro diffs contra la v1 se rehacen igual;
  - la guarda usa los precios oficiales de `claude-opus-5-5`, como afirma la autora: 4, 20, 5 (la escritura de la caché de 5 minutos) y
    0,20 por millón (documentación de la API de la sesión, skill `claude-api` 2.1.308: `shared/models.md:79` y
    `shared/prompt-caching.md:144`), con la caché de 5 minutos (`ephemeral`, sin `ttl`). La cota del costo se rehace desde sus entradas
    (36 cifras, dentro de USD 0,02);
  - el selftest y la corrida en seco de la ejecutora no se corrieron en la mesa (leen `insumos/` y el material); sus consolas dan 85 de 85
    y OK;
  - el 162 cruzó la foto de la ejecutora, que lo declaró; no la afecta (la §88 que lee es la misma).
- **Las decisiones de la autora sobre lo que deja abierto** (recibidas a las 09:54:35), tal cual:
  1. «La iteración 1 corre con las tres repeticiones en paralelo, con la guarda que suma las tres bases, aunque el paralelo solo esté
     probado con el simulado.»
  2. «En la regla de freno, las fichas que el juez no decide cuentan como desacuerdo en el acuerdo de «correcta», y se informan aparte.
     Lo fijo antes de ver ninguna iteración.» Se fija acá: ninguna iteración corrió.
  3. «El humo corre con los casos propuestos, después de la firma de la enmienda 4 y de tu revisión.»
  4. «El texto de introducción del bloque de casos lo leo con los casos y lo apruebo o no en la misma hoja.»
  5. La hoja de aprobación pasa por un convertidor, como las otras lecturas: la exportación, la marcada y su sello; la iteración lee la
     marcada; la hoja suma una fila para el texto de introducción.
  6. El SDK del `.venv` del repo queda en anthropic 0.100.0 hasta que termine B6.3: con la API 2026-10-21, `temperature` da 400 aun en su
     valor por defecto, y el SDK 1.0 la quitó (`shared/api-version-migration.md:97` y `python/claude-api/sdk-upgrade.md:176`, de la misma
     documentación); el juez de B6.3 usa `claude-sonnet-4-6` con temperatura 0 y depende de la versión 2023-06-01.
- **El «seguí» de la etapa a-bis** (`decisiones_243_mesa/v2a/`): el convertidor, la fila del texto de introducción y la regla de la
  decisión 2, con sus pruebas. Va después del humo, que corre con el código de la etapa a; pegarlo es de la autora (PENDIENTE). La
  decisión 1 no cambia código: el comando de la iteración ya lanza las tres repeticiones en paralelo.
- **El control del SDK y de la versión de la API** (`scripts/control_sdk_anthropic_juez_y_banco.py`, el 165): frena si cambian el
  intérprete, el SDK, la versión que manda, o el modelo y la temperatura del pedido del juez de B6.3 (mandado a un transporte simulado,
  sin red); si cambia su cliente real; o si un módulo del juez, del banco o de la caché fija otra versión, cabeceras o betas. Los
  despachos de los pasos pagos del banco y del juez de B6.3 lo piden como primer control. El agente del banco no usa este SDK: corre con
  el CLI de Claude Code, cuya versión ya es variable sellada del banco. En un clon del repo con el `.venv` del repo, da 5 de 5, y frena
  en sus cuatro pruebas en contra.
- **El material de las claves del catálogo, en FRENO** (paquete `revision_claves_catalogo/`, `b98735b0…`, 22 archivos), revisado por la
  mesa por código (`decisiones_244_mesa/catalogo/`, 12 de 12), sin abrir la carpeta de lectura: 105 candidatas rehechas desde el sello,
  que son las 105 claves del material; 595 filas con 1.046 relaciones del registro; la planilla, con 12 alias, 36 ids nuevos y 57 que no
  entran; la tabla de ids del convertidor es la del catálogo de sujetos r2 del sello. **El material no cambia.** La autora lo lee desde
  que lo recibió, en paralelo con la revisión, con una vista suya en Markdown que no entra en la marcada ni en el sello.
- **El calendario v12p** (`decisiones_240_mesa/calendario/`; duraciones NO VERIFICADAS), con tres ajustes, cada uno controlado (con el
  ajuste apagado, las 17 corridas dan las de antes): los commits después de los FRENOs de afuera, el censo sellado (09:22:53) y los dos
  FRENOs llegados (la etapa a de la v2 a las 08:59:53 y el catálogo a las 09:16:32, por la hora de su archivo). Con la prioridad de la
  autora del viernes y la mesa desde las 11:00 a las 11:30:
  - la re-aplicación medida, hoy de 19:10 a 19:40, antes del corte también en el lento (de 23:13 a 23:43); el sello del grafo evaluado,
    de 20:25 a 20:55; N7, el sábado de 22:43 a 23:13, después del corte, y se declara;
  - la firma de B6.3: con N = 128, el lunes de 14:58 a 15:29, después de su plazo; con N = 96, el lunes de 08:18 a 08:49; con N = 64, el
    domingo de 20:08 a 20:38. La etapa T: con N = 128, el jueves de 09:45 a 10:16; con N = 96, el miércoles de 14:05 a 14:36;
  - sin la prioridad, la re-aplicación va de 22:48 a 23:18, y en el lento pasa el corte (sábado de 12:36 a 13:06).
  - Con la prioridad y la regla del N (registro, §51), N = 96 deja en plazo, en el central, todo salvo N7. El N lo fija la autora
    (PENDIENTE).
- **El orden de hoy:**
  1. las tres sesiones pagas de la D-6, sin ningún commit al lado;
  2. los cuatro commits, en cualquier orden (tocan archivos distintos, y cada uno se probó con otro encima): el 163, el 160 v2 si la
     autora firma, el 164 (esta sección y la anterior) y el 165;
  3. el humo de la v2, después del 160 v2;
  4. el «seguí» de la etapa a-bis, después del humo;
  5. la lectura del catálogo y su sello;
  6. el despacho de la re-aplicación, con la lista del censo y el catálogo de resolución de la marcada;
  7. el «seguí» del tramo 2 de A2.1, con el resultado de la D-6 y el control del SDK como primer paso.
- Las secciones anteriores no se editan.

## 94. El viernes al mediodía: los cuatro commits, la D-6 pagada con B' en FRENO, el N de B6.3 fijado y la primera pasada del catálogo sellada (23/10/2026)

Decisiones y hechos de la autora del 23/10/2026, recibidos a las 10:41:30 (hoja de ruta de la mesa, §245).

- **Los cuatro commits,** corridos con zsh, en orden, con su push (git log): el 163 (`0765be9a`, 10:39:00), el 160 v2 (`90cce828`,
  10:39:06; la enmienda 4 al pre-registro de tripletas queda FIRMADA hoy), el 164 (`e9481002`, 10:39:13) y el 165 (`896223dd`, 10:39:19).
  Contra el paquete de la mesa, 27 de 27 (`decisiones_245_mesa/verificacion/`).
- **Las tres sesiones pagas de la D-6,** con el comando de la sección 6 de su FRENO (`d6_tope_mcp/sesiones_c/registro_tope_mcp.json`, de
  10:38:43 a 10:39:35): gasto R9, USD 0,324651.
  - A' llegó entera (140.000 de 140.000) y C', con los dos resultados enteros en el mismo mensaje (`PRESUPUESTO_NO_ACTIVO`): las dos dan
    OK con la condición del banco;
  - B' llegó como referencia, como se esperaba, pero la condición del banco falla en tres controles: `tool_results_Bp/` no trae el
    archivo que nombra la referencia, y por eso fallan el sha256 del texto y la línea de acentos. Los controles dan FRENO. En
    `controles_tope_mcp.json`, el primero de los tres dice que el stream no nombra un archivo, la meta dice `copia_resultados_en_disco`
    «sí», y la respuesta de B' no trae su código (`respuesta.estado` «ausente»);
  - la autora pidió a la ejecutora un diagnóstico a USD 0, sin tocar el repo: dónde guardó el CLI el archivo, si la falla está en
    `LA.copiar_sesion`, en su control o en la expectativa, y un parche con su prueba si está en el lanzador del banco (PENDIENTE). Nada
    pago de la D-6 hasta la revisión de ese FRENO;
  - las sesiones corrieron al mismo tiempo que los cuatro commits (10:39:00 a 10:39:19). Ningún commit toca lo que lee la D-6: los 13
    archivos de `8bea2edb..896223dd` no son del banco ni de `d6_tope_mcp/`. Se declara.
- **Lo que cambia para el «seguí» del tramo 2 de A2.1:**
  - los dos servidores del banco declaran la anotación por herramienta en 200.000 caracteres, como A' (`mcp_kg/servidor_mcp_kg.py:68`
    y `:146`; `mcp_vector/servidor_mcp_vector.py:74` y `:280`): sus resultados llegan enteros hasta ese largo, y el camino de B', el del
    disco, solo se abre por encima;
  - A2.1 copia sus sesiones con la misma función del banco (`LA.copiar_sesion`, `banco_mcp/a2_1/lanzar_agente_a2_1.py:171`);
  - el «seguí» suma, en cada sesión, el largo de cada resultado y un control que frena si alguno llegó como referencia a disco;
  - si el diagnóstico pone la falla en el lanzador, su parche cambia el lanzador que usa A2.1: va con su commit antes del humo de A2.1;
  - cuántos resultados de A2.1 pasan los 200.000 caracteres: NO VERIFICADO.
- **El N de B6.3** (decisión de la autora, recibida a las 10:41:30), tal cual: «El N de B6.3, por la regla de la §51: el tope por
  calendario es 96. Si Q5 pide menos, va el de Q5; si pide más, 96, declarado con la potencia que alcanza. Si el domingo a las 20:00 la
  tercera ola no está revisada, el N es 64, declarado. Lo fijo hoy, antes de A2.2 y de B6.3.»
  - En el calendario v12p con N = 96 y la mesa desde las 11:00 a las 11:30 (duraciones NO VERIFICADAS), la tercera ola queda revisada el
    domingo de 17:38 a 18:08 en el central, antes de las 20:00, y el martes en el lento, donde la regla da 64.
- **La columna `nota` de la hoja de aprobación del juez v2:** sí, como viene en el «seguí» de la etapa a-bis.
- **Las claves del catálogo:**
  - la primera pasada, sellada a las 10:22:50 (`claves_marcada.csv`, `86194514…`), queda guardada tal cual, con su sello y su
    exportación, en `lectura_claves_catalogo/pasada1/`. La mesa controló por nombre su sha256 contra el sello, sin abrirla;
  - la autora hace una segunda pasada de los 48 alias e ids nuevos (12 y 36 en la planilla) antes de que la mesa use la lectura. Vale la
    segunda, sellada, y se declaran las dos.
- **Lo que sigue:**
  1. el humo de la v2 (el 160 v2 ya está) y, después, el «seguí» de la etapa a-bis;
  2. el FRENO del diagnóstico de la D-6, con su revisión;
  3. la segunda pasada del catálogo, sellada, y el despacho de la re-aplicación;
  4. el «seguí» del tramo 2 de A2.1, con el control del disco, y su humo después de la revisión del diagnóstico.
- Las secciones anteriores no se editan.

## 95. El viernes, después del mediodía: el diagnóstico de B' y el humo de la v2 (23/10/2026)

Hechos de la autora del 23/10/2026, recibidos a las 10:53:26 (hoja de ruta de la mesa, §246).

- **El diagnóstico de B' de la D-6,** hecho por la ejecutora a USD 0, solo leyendo, y verificado por la autora contra el código del
  paquete de la etapa c: la falla es del control, no del lanzador del banco.
  - El patrón de la ruta de la referencia (`d6_tope_mcp/code/controles_tope_mcp.py:281` y `lanzador_prueba.py:65`, con `/\S+?`) corta en
    el espacio de «INGENIERIA IA»: el control no encontró el nombre del archivo, y fallaron en cadena los tres controles de B';
  - `LA.copiar_sesion` (`banco_mcp/agentes/lanzar_agente.py:224-232`) copió la carpeta `tool-results` entera, con el archivo de 140.914
    bytes cuyo texto da el sha256 del log R1. Con el patrón corregido, los controles sobre la sesión guardada dan OK, sin FRENO, y su
    selftest, 208 de 208;
  - en B', después de la referencia, el agente intentó leer el archivo con Read y con Bash, que no tiene, y terminó por el límite de
    turnos: por eso costó USD 0,034 y no 0,012;
  - la mesa controló las líneas de `LA.copiar_sesion` en HEAD y el tamaño del archivo copiado;
  - el cierre de la ejecutora, con `FRENO_UD6_TOPE_MCP_c_bis.md` y su paquete, está PENDIENTE: dice cuándo guardaría el CLI un resultado
    en disco en B6.3, qué recibe el agente en ese caso, y si algún `.py` del banco o del análisis de B6.3 extrae rutas de una referencia
    con un patrón que no acepte espacios. Nada pago de la D-6 hasta su revisión.
- **Para el «seguí» del tramo 2 de A2.1:** no hace falta un parche del lanzador. Queda el control del disco: un resultado que llega como
  referencia frena la sesión, porque el agente no puede leerlo, como en B'.
- **El humo de la v2,** corrido por la autora con su comando a las 10:41:15, después del 160 v2 (HEAD `896223dd`; prompt `bf484381…`,
  bloque `5bdf4a42…`):
  - 6 de 6 completas, sin errores, rechazos, cortes ni reintentos; USD 0,7197, contra el tope de 2;
  - las medianas por pedido: entrada 1.838 tokens, salida 1.458 (con el razonamiento) y lectura de la caché 84.735, con una sola
    escritura de la caché; 14,2 segundos. El análisis sobre las respuestas reales, OK;
  - la cota con el humo (`v2/costo/cota_costo_v2_con_el_humo.json`): la iteración 1, USD 15,94; la 2, 15,40; la 3, 14,80; la prueba
    sobre T, 20,37; y las 300 restantes, 57,50. Cada una, debajo de su freno (35,70 por paso y 106,20 las 300);
  - la mesa lo rehízo por código desde el resumen: los 6 pedidos, su gasto, sus tipos y sus finales.
- **El «seguí» de la etapa a-bis,** pegado por la autora en la misma sesión, después del humo.
- **Lo que sigue:**
  1. el FRENO c_bis de la D-6, con su revisión;
  2. el FRENO a-bis de la v2, con su revisión, y la aprobación de los casos por la autora, con la hoja, el convertidor y el sello;
  3. la segunda pasada del catálogo, sellada, y el despacho de la re-aplicación;
  4. el «seguí» del tramo 2 de A2.1, con el control del disco.
- Las secciones anteriores no se editan.

## 96. El viernes, primera hora de la tarde: el cierre del diagnóstico de la D-6, el valor remoto por tool, el «seguí» del tramo 2 de A2.1 y la etapa a-bis del juez v2 (23/10/2026)

Decisiones y hechos de la autora del 23/10/2026, recibidos a las 11:12:58 y a las 11:14:27 (hoja de ruta de la mesa, §247 y §248).

- **El 166,** corrido con su push (`f619128d`, a las 11:11:48, git log): 5 de 5 contra el paquete de la mesa.
- **El FRENO c_bis de la D-6** (paquete `revision_UD6_TOPE_MCP_c_bis/`, `deb8a260…`, 25 archivos), revisado por la mesa por código
  (`decisiones_247_mesa/d6/`, 11 de 11):
  - el parche cambia los cuatro archivos de `code/` que nombra (los dos patrones de la ruta y la ruta de juguete, más el selftest) y suma
    `diagnostico_Bp.py`; con él, los controles sobre la sesión guardada dan OK (B', 12 de 12), el selftest 208 de 208 y el diagnóstico
    19 de 19; el archivo de B' tiene 140.914 bytes y el sha256 `22011bec…`; las huellas de antes y de después son iguales;
  - el punto 5: en B6.3, un resultado va a disco solo si su texto pasa los 200.000 caracteres (unidades UTF-16);
    `MAX_MCP_OUTPUT_TOKENS` y el presupuesto por mensaje no actúan; y el mayor resultado medido del banco es de 81.275 (`tope_mcp.json`
    de HEAD);
  - el punto 6: ningún `.py` de HEAD tiene «saved to»; lo único que toca la referencia (`gate/code/adaptador_cc.py:276` y `:360-361`)
    lee `persistedOutputPath` entero.
- **El valor remoto por tool,** `tengu_velvet_ibis` (la autora autorizó, a las 11:12:58, leer solo esa clave en los `.claude.json` de las
  tres sesiones de la D-6, por código y en memoria): en las tres, la clave existe y es un objeto vacío. Ninguna tool tiene un umbral
  propio, así que las cinco de los dos servidores del banco no están afectadas (`decisiones_247_mesa/tengu/`). El valor puede cambiar de
  una sesión a otra; el control del disco de A2.1 frena en cualquier caso.
- **El «seguí» del tramo 2 de A2.1** (`decisiones_247_mesa/a21/`), con lo que pidió la autora:
  - el control del disco en `correr_a2_1.py`, después de cada sesión: si un resultado llega como referencia a disco, la corrida frena sin
    lanzar otra; y el largo de cada resultado en unidades UTF-16;
  - en el paso 0, el control del SDK (el 165) y el sha256 del lanzador del banco de HEAD (`2f007420…`);
  - el commit de su código, armado por la mesa, antes de los pasos pagos;
  - **la etapa corta de A2.1** (decisión de la autora del 16/10/2026, registro, §16) no corrió: no hay `FRENO_A2_1_a_bis.md` ni su
    paquete, y su «seguí» de entonces ya no sirve tal cual, porque el entorno limpio (`ca5d192f`) cambió el lanzador de A2.1. El «seguí»
    la suma a su parte de USD 0; armarla aparte es la otra opción. La decisión es de la autora (PENDIENTE).
- **El FRENO de la etapa a-bis del juez v2** (paquete `revision_UTRIP_V_JUEZ_v2_a_bis/`, `c9a3b002…`, 44 archivos, sin ningún
  `NO_ABRIR_`), revisado por la mesa por código (`decisiones_248_mesa/v2/`, 11 de 11):
  - el paquete y la carpeta de trabajo coinciden; lo que dejó el humo no cambió; los siete diffs contra la etapa a se rehacen igual; no
    cambian la guarda, el simulado, el costo, el gold, la v1, los comandos, el bloque ni el prompt (`bf484381…`);
  - la hoja nueva (`38832f9d…`) tiene las 10 filas de los casos y la del texto de introducción, con `aprueba` y `nota` vacías;
  - en la regla de freno, una ficha que el juez no decide cuenta como desacuerdo en «correcta», y la importancia no cambia;
  - el convertidor exige «sí» o «no» y pasa las celdas a NFC, que es la misma palabra: la mesa lo acepta;
  - el selftest da 113 de 113 y la corrida en seco, OK, en sus consolas.
- **Los dos errores de la etapa a que declara la ejecutora:**
  - el selftest y el grep abrían sus propios `NO_ABRIR_` (los desacuerdos y el prompt), sin mostrar su contenido. No cambia ningún
    resultado, y ya no los abren;
  - para elegir los casos imprimió en su consola la tabla de los 50 desacuerdos, con la marca de la autora y lo de la v1.1. El despacho
    le pedía elegirlos desde esos desacuerdos, así que no supo nada que no debía saber, y no cambia la medición: las cifras de las
    iteraciones son internas y no cuentan los casos del prompt, y la precisión de T va contra la lectura de la autora de T. Lo que sí
    cambia: la transcripción de esa sesión (`176f814c…`) trae marcas del gold, y nadie la lee, como las carpetas de lectura de la autora.
- **La aprobación de los casos** (decisión de la autora): en paralelo con la revisión, después de su segunda pasada del catálogo, con el
  convertidor y el sello (PENDIENTE).
- **El comando de la iteración 1** (`decisiones_248_mesa/v2/`): antes de la clave controla que el código, el comando, los casos, el
  bloque, la hoja y el convertidor de la v2 sean los revisados (17 archivos, por sha256), que existan la marcada y su sello, y que no corra
  ningún otro paso pago; después corre la iteración con la clave por el envoltorio del banco, sin otra corrida paga al lado. Probado a
  USD 0 sobre una copia, en sus cuatro casos.
- **Lo que sigue:**
  1. la segunda pasada del catálogo, sellada, y el despacho de la re-aplicación;
  2. la aprobación de los casos, sellada, y la iteración 1 del juez v2;
  3. la decisión de la autora sobre la etapa corta, y el «seguí» del tramo 2 de A2.1.
- Las secciones anteriores no se editan.

## 97. El viernes, al mediodía: la segunda pasada de las claves sellada, el despacho de la re-aplicación y las decisiones sobre A2.1 y el juez v2 (23/10/2026)

Decisiones y hechos de la autora del 23/10/2026, recibidos a las 11:32:19 (hoja de ruta de la mesa, §249).

- **El 167,** corrido con su push (`4ee44c51`, a las 11:32:05, git log), contra el paquete de la mesa (`decisiones_249_mesa/verificacion/`).
- **La lectura de las claves del catálogo, segunda pasada, la que vale:** sellada a las 11:27:46 (`lectura_claves_catalogo/claves_marcada.csv`,
  `973654f0…`, en `sello_lectura_claves.txt`). La mesa la controló por código, sin mostrar ninguna clave, código ni nota
  (`decisiones_249_mesa/catalogo/`, 11 de 11):
  - la marcada da su sello; sus 105 filas traen la clave, las formas, la propuesta y la justificación de la planilla, en el orden del
    material; los códigos pasan los controles del convertidor entregado (el catálogo r2, los ids nuevos, los padres y los ciclos);
  - 12 alias, 35 ids nuevos y 58 que no entran; tres veredictos distintos de la propuesta, cada uno con su nota;
  - contra la primera pasada (sellada a las 10:22:50, `86194514…`, guardada tal cual en `pasada1/`), cambia una sola clave, de un id nuevo a
    «no entra».
  - Se declaran las dos pasadas: según la autora, la primera de 10:05 a 10:22 y la segunda, sobre los 48 alias e ids nuevos, de 10:31 a
    11:27. Sus dos vistas en Markdown no entran en la marcada ni en el sello.
- **Los veredictos para la re-aplicación** (`decisiones_249_mesa/catalogo/veredictos_claves_catalogo_segunda_pasada.json`, `e1be9926…`):
  la clave y su código, sin la nota, la justificación ni la propuesta, con el sha256 de la marcada de la que salen.
- **El despacho de la re-aplicación única** (`decisiones_249_mesa/reapl/`), con los dos mandatos firmados el 20/10/2026:
  - los cinco pasos, cada uno con y sin cola: el sello (que tiene que dar el sello byte a byte), + D, + las claves, + C1 y + las remisiones
    (la opción B);
  - las claves: el catálogo de resolución, armado por script desde los veredictos, con `componer`. El label de un id nuevo y el alias de
    un `alias:` son la forma de la clave más frecuente en el material: es una propuesta de la mesa (PENDIENTE de la autora);
  - C1: la lista del censo, vacía (`aa6aa007…`), y la de los nodos, vacía (`37517e5f…`);
  - los primeros controles: R19 con las dos bases de la caché, y los tres selftests del 163;
  - el cegamiento del §7 bis de U-PROC-HERENCIA, con la muestra de las FICHAS en memoria.
  - USD 0, sin API. Pegarlo es de la autora (PENDIENTE).
- **Los commits:** antes de que arranque, el de esta sección (el 168). Mientras corre, ninguno.
- **Las decisiones de la autora sobre A2.1,** tal cual:
  1. «La etapa corta va como la (b): sus tres tareas, en la parte de USD 0 del «seguí» del tramo 2, tal como viene en el bloque.»
  2. «Autorizo la misma lectura acotada de tengu_velvet_ibis en el .claude.json de cada sesión paga del banco: A2.1 y después A2.2, N6 y
     B6.3. Por código y en memoria, registrando por sesión solo si la clave existe y, si existe, los nombres de tool y sus números, sin
     ningún otro campo ni valor del archivo. El control del disco sigue frenando igual.»
  3. «A2.1 va después de la re-aplicación, por mi prioridad del viernes. Si estimás que su parte de USD 0 termina antes de que el
     despacho de la re-aplicación esté listo, decímelo y la pego antes. Si no, espera.»
  - La parte de USD 0 de A2.1 escribe en el repo y lleva horas: no termina antes de que el despacho esté listo, así que espera. El «seguí»
    v2 (`decisiones_249_mesa/a21/`) lleva las dos primeras decisiones.
- **El juez v2:** la autora aprueba los casos y corre la iteración 1 con el comando de la mesa, sin otra corrida paga al lado (PENDIENTE).
  Puede correr mientras corre la re-aplicación: es de USD 0, no llama a la API, y el control de la extracción de la v2 no la toma por
  una (busca `runner_corpus`, `lanzar_t*` y `correr_tanda*`).
- **Lo que sigue:**
  1. el 168; después, la re-aplicación;
  2. el sello de la aprobación de los casos y la iteración 1 del juez v2;
  3. el FRENO de la re-aplicación, con su revisión, y el sello del grafo evaluado;
  4. el «seguí» del tramo 2 de A2.1.
- Las secciones anteriores no se editan.

## 98. El viernes, primera hora de la tarde: la re-aplicación pegada, la regla del label con el artículo inicial, un caso fuera de la iteración 1 del juez v2 y los borradores de los pre-registros de B6.3 y de A2.2 (23/10/2026)

Decisiones y hechos de la autora del 23/10/2026, recibidos a las 11:52:35, a las 12:18:37 y a las 12:26:16 (hoja de ruta de la mesa,
§250 a §252).

- **El 168,** corrido con su push (`2db79462`, a las 11:51:08, git log).
- **La re-aplicación única,** pegada tal cual, en una sesión nueva abierta en `fuera_del_repo/reaplicacion_unica/` (según la autora).
  Mientras corre, ningún commit.
- **La regla del label y del alias** (decisión de la autora), tal cual: «la forma de la clave más frecuente en el material (la que más
  relaciones del registro reúne; si empatan, la primera en orden alfabético), con la primera letra en mayúscula.»
- **La misma regla, con el artículo inicial** (12:26:16). La ejecutora encontró que 32 de las 47 formas elegidas empiezan con artículo, y
  E4 lee la mención sin su artículo inicial antes de comparar (`data/experiment/reextraccion_v2/corpus_v2/r1_e4.py:343-344`; la
  sustitución en `:346`, con la expresión de `:319`). Con la regla literal, 16 ampliaciones no re-resuelven ninguna de sus filas y 3 solo
  algunas.
  - **La decisión de la autora:** el artículo inicial sale con la misma regla de E4, y la mayúscula va después. Así las 35 altas
    re-resuelven todas sus filas, y de los 12 alias, 10 todas y 2 algunas; el catálogo de resolución da `54147015…` en lugar de
    `d24e8283…`.
  - El FRENO de la re-aplicación lo declara como apartamiento del despacho, con las cuentas de las dos variantes. Es la regla aceptada,
    corregida para que las aprobaciones de la autora tengan efecto, y no mira ningún resultado de la evaluación.
  - Las cuentas son las que informó la ejecutora: la mesa las controla al revisar el FRENO (NO VERIFICADAS hasta entonces).
- **La iteración 1 del juez v2** (12:18:37):
  - la autora marcó y selló la aprobación de los casos: 10 «sí» y un «no», en el caso V005, con su nota. Los controles del comando dieron
    OK con `--solo-controles`, y al correrlo frenó antes de lanzar nada (USD 0), con «1 filas de la hoja de la iteración 1 no dicen «sí»
    en aprueba (V005)». Su exportación, su marcada y su sello quedaron aparte, en `tripletas_v_juez/v2/casos/aprobacion_1_con_un_no/`
    (según la autora);
  - **la decisión de la autora:** V005 sale sin reemplazo, y la iteración 1 va con los otros 9. Pidió a la ejecutora la etapa a-ter, a USD
    0: los casos, el bloque, el prompt y la hoja regenerados sin V005, sin leer su nota, con la hoja y el prompt anteriores renombrados, y
    nada más cambiado;
  - cuando llegue su FRENO, la mesa lo revisa y actualiza el comando de la iteración con los sha256 nuevos; la autora aprueba otra vez y
    la corre (PENDIENTE). La revisión controla también que V005 vuelva a las fichas que la v2 juzga, porque ya no es un caso de su prompt
    (pre-registro de tripletas, enmienda 4, punto 4).
- **Los pre-registros de B6.3 y de A2.2,** que la autora pidió avanzar mientras corre la re-aplicación, sin tocar el repo ni leer lo que
  ella cambia. La mesa los armó fuera del repo (`decisiones_250_mesa/`), desde las fuentes de `2db79462`, con 182 de 182 anclas
  controladas:
  - **el borrador v1 del pre-registro de B6.3,** con 17 huecos, cada uno con su fuente y su regla, y 9 decisiones de la autora. La regla
    del N de la §94 va en un script (`regla_del_N_B63_s94_mesa.py`): selftest 14 de 14, y reproduce sin diferencias las 18 filas de la
    tabla de k corridas de la mesa;
  - **el insumo del pre-registro de A2.2,** con 5 huecos del tramo 2 y 4 decisiones. El mandato firmado de A2.1 le da ese borrador a la
    ejecutora del tramo 3 (§5, `:128-154`, y §6, `:165`): la mesa no lo escribió, y quién lo escribe lo decide la autora (A-D0).
- **Lo que la mesa encontró al armarlos,** para decidir antes de las firmas:
  1. la ablación del texto de las omisiones `meta_normativo` (plan, `:778`, decisión del 06/10/2026) no tiene ninguna decisión posterior
     (0 apariciones en este registro y en el mandato de U-NAV, en `2db79462`);
  2. la etapa T de los umbrales entra en B6.3 (d) por la enmienda 1 al pre-registro de tripletas (`:311-316`), y ningún calendario de la
     mesa la contaba;
  3. el punto de diagnóstico posterior a A2.2 (plan, `:341`) corrige lo corregible antes de sellar el grafo evaluado, y con la prioridad
     del viernes (§91) el grafo evaluado se sella antes de A2.2;
  4. el orden de las corridas de B6.3 ya está decidido (§89), y no queda pendiente;
  5. ninguna fuente escribe la cobertura de T si el juez de presencia no pasa en V, y el pre-registro tiene que traer los dos casos (§61);
  6. la lectura de la autora de la muestra de control de B6.3 va después del cierre de U-MED-VERIF (§49).
- **El calendario v12q** de la mesa (duraciones NO VERIFICADAS): el commit del sello del grafo evaluado va antes de pegar el «seguí» de
  A2.1, porque no puede cruzar la foto del repo de su ejecutora (mandato de A2.1, §7). Con N = 96, en el central:
  - sin los borradores, la firma del pre-registro de B6.3 cae el lunes 26 a las 14:21, después de su plazo (§50);
  - con el borrador de B6.3, el lunes a las 11:21;
  - con las lecturas previas de la autora y el insumo de A2.2, el domingo 25 a las 19:37;
  - con los sorteos de B6.3 sin esperar al N, el domingo a las 16:37.
  - En el escenario lento, con todo lo anterior, la regla de la §94 da N = 64, y la firma cae el lunes a las 12:43, 43 minutos
    después del plazo.
- **Lo que sigue:**
  1. el FRENO de la re-aplicación, con su revisión;
  2. el commit de esta sección y el del sello del grafo evaluado, después de ese FRENO y antes de pegar el «seguí» de A2.1;
  3. el «seguí» v2 del tramo 2 de A2.1;
  4. el FRENO de la etapa a-ter del juez v2, con su revisión y el comando actualizado; la aprobación de la autora y la iteración 1.
- Las secciones anteriores no se editan.

## 99. El viernes, a media tarde: las decisiones de la autora sobre los borradores de los pre-registros de B6.3 y de A2.2 (23/10/2026)

Decisiones de la autora del 23/10/2026, recibidas a las 13:27:46 (hoja de ruta de la mesa, §253), sobre el borrador v1 del pre-registro de
B6.3 y el insumo del pre-registro de A2.2 (§98).

- **Las decisiones,** tal cual:
  1. «Los sorteos de B6.3: sí, apenas se selle el grafo evaluado, sin esperar al N, como dice el mandato de las preguntas (etapas 2 y 4). El
     N toma las olas en el orden sellado.»
  2. «A-D0: (a). El borrador de A2.2 lo escribe la ejecutora del tramo 3, con tu insumo en su «seguí».»
  3. «El orden de esta tarde: el 169 y el commit del sello del grafo evaluado, los dos después del FRENO de la re-aplicación y antes de
     pegar el «seguí» de A2.1.»
  4. «D-1: (a), el N no baja de 64.»
  5. «D-2: (a), dimensiona el mayor de los dos N_Q5.»
  6. «D-3: (a), el brazo del grafo es solo grafo, y la ablación de meta_normativo se declara como desvío del plan.»
  7. «D-4, D-5 y D-6: las semillas que proponés (B63:orden_corridas:v1; B63:control_juez:v1, por brazo, tipo y veredicto;
     B63:atribucion:ultima_clase:v1).»
  8. «D-7: (b). La etapa T de los umbrales queda fuera de esta evaluación, como desvío declarado de la enmienda 1, y va al capítulo 6. Que
     el borrador v2 diga con qué umbral queda la afirmación de (d) sin esa etapa, con su ancla.»
  9. «D-8: docs/preregistro_B6_3_evaluacion_final.md.»
  10. «D-9, ampliada: si el juez de presencia no pasa en V, o si la cobertura de V no cerró el miércoles 28 a las 18:00, la cobertura de T
      se informa con la presencia que yo decido en el control de 30, con su intervalo de Wilson y sin la cifra del juez, declarada como
      medición humana sobre 30. Si V cierra después de los resultados, la cifra del juez va al lado, como exploratoria, sin reemplazar la de
      las 30. La amplío porque tu calendario dice que la cobertura de V no cierra antes del miércoles a las 18:00 en ninguna corrida, y en
      la §61 del registro yo había dado por hecho que cerraba antes de los resultados.»
  11. «Al §8.1 le falta la regla de la afirmación principal, del plan (:339): «el grafo supera a los fragmentos» solo si supera a las dos
      configuraciones, cada comparación con su Holm y a favor del grafo. Si supera a una sola, se informa por configuración, sin la
      afirmación general. Agregala en el borrador v2.»
  12. «En el §8, agregá un chequeo de robustez declarado, fuera de Holm: la misma prueba con los signos permutados por documento, con las 4
      preguntas de cada documento juntas, y el intervalo de la hipótesis secundaria con bootstrap por documento. Si la versión por pregunta
      y la versión por documento no llegan a la misma conclusión, se informan las dos. La prueba principal no cambia.»
  13. «En el §7.1, que diga que el juez recibe solo la pregunta, sus criterios y la respuesta, sin el brazo, y controlalo en el código que
      arma la entrada del juez.»
  14. «A-D1: el orden de las corridas de B6.3 (registro, §89).»
  15. «A-D3: tu recomendación, con un agregado: lo que el diagnóstico atribuya al agente o a la búsqueda entra solo si pasa su medición en
      N6, con N3 (U-NAV, §7, regla 1: el ajuste se hace solo con N3, nunca con EV2), y A2.2 no se vuelve a correr. Lo que atribuya al
      contenido del grafo o a la segmentación va al grafo corregido o a una release posterior, declarado en los dos pre-registros.»
  16. «En el insumo de A2.2: si la verificación del juez sobre las 20 no pasa, el borrador cita mi decisión ya tomada, la 3 de Q8 (B6.3 se
      juzga con el juez, la cifra se informa con su acuerdo medido y lo dudoso va a mi lectura).»
  17. «A-D2: lo decido con tu propuesta, después del FRENO del tramo 2.»
  - «El resto del borrador y del insumo, como están.»
- **Lo que armó la mesa** (`decisiones_253_mesa/`, fuera del repo):
  - **el borrador v2 del pre-registro de B6.3,** con D-1 a D-9 decididas, la regla de la afirmación principal (§8.1), el chequeo de robustez
    por documento (§8.3), lo que recibe el juez (§7.1) y la contaminación del sorteo de documentos (§3.1). Queda abierta la D-10: que la
    respuesta del agente traiga marcas de su brazo, que el control del juez no cubre. La propuesta es contarlas por brazo y declararlas, sin
    editar ninguna respuesta;
  - **la afirmación de (d) sin la etapa T de los umbrales** (decisión 8): B6.3 no hace la afirmación de los umbrales, que pide un límite
    inferior de al menos 0,90 sobre la etapa T (enmienda 1, §8, `:214-216`; D5, `:342`). El umbral sigue siendo 0,90 para cuando la etapa T
    corra en el capítulo 6. El pre-registro de tripletas no fija un umbral de afirmación para la precisión ni para la cobertura;
  - **lo que recibe el juez** (decisión 13): un control a USD 0, con un transporte simulado y sobre una copia del juez de HEAD, de que al
    modelo viajan solo la pregunta, la respuesta y los criterios con su cita textual, y ninguna otra clave de un criterio. Da 10 de 10, y
    frena en sus dos pruebas en contra;
  - **el insumo v2 de A2.2,** con A-D0, A-D1 y A-D3 decididas y la decisión 3 de Q8 citada; A-D2 queda para después del FRENO del tramo 2;
  - **los sorteos de B6.3** (decisión 1): el script, con su selftest (13 de 13) y dos corridas en seco con semillas de prueba que dan los
    mismos bytes. Aplica al sortear la regla firmada del documento agotado, porque las anclas de cada documento se conocen;
  - **la contaminación por código** (plan, `:782`, punto 4), con el método de la §102 de la mesa extendido a los 87 .py del pipeline de
    HEAD: ningún elegible tiene una constante en el código del pipeline, y 23 aparecen solo en código de medir, que la regla deja elegibles
    con su exposición declarada.
- **Lo que decide la autora antes de la corrida real de los sorteos:** las tres semillas (propuestas `B63:sorteo:documentos:v1`,
  `B63:sorteo:unidades:v1` y `B63:sorteo:tipos:v1`); la forma de las olas, la rotación de los subtipos, el orden de los lugares y el
  documento agotado aplicado al sortear (propuestas P-1 a P-4); y la contaminación que no está en el código, como el laudo de un caso
  (PENDIENTE de la autora).
- **Los commits:** el 169 se rearma con esta sección y la §98, antes del FRENO de la re-aplicación, y reemplaza al anterior, que no corrió.
  Va después de ese FRENO, junto con el commit del sello del grafo evaluado y antes de pegar el «seguí» de A2.1 (decisión 3). Mientras corre
  la re-aplicación, ningún commit.
- Las secciones anteriores no se editan.

## 100. El viernes, a media tarde: el FRENO de la re-aplicación revisado, el sello del grafo evaluado, la etapa a-ter del juez v2 y los expertos de B6.3 (23/10/2026)

Decisiones y hechos de la autora del 23/10/2026, recibidos a las 14:11:25, a las 14:24:16 y a las 14:41:03 (hoja de ruta de la mesa, §254 a
§256).

- **El 169 v2,** corrido con su push (`c6565aa4`, a las 14:11:09, git log).
- **El FRENO de la re-aplicación única** (`revision_UREAPL/`, 161 archivos, manifiesto `30d34909…`): las cuatro piezas entran, sin casos de
  freno, y el grafo evaluado es el del paso 5: sin cola, `kg.json` `576c9725…`; con cola, `1bd5ffcd…`. Los grafos y su entrada quedan en
  `fuera_del_repo/reaplicacion_unica/copia_repo/`.
- **Las decisiones de la autora sobre ese FRENO,** tal cual:
  1. «Lo que declara en su §6.3 (20 relaciones sin cola y 21 con cola de claves sin un veredicto que entre, 3 de ellas de la clave del
     veredicto 99, «no entra», que se re-resuelven por el calificador o por el slug con los labels nuevos) queda en el grafo evaluado,
     declarado. Es la regla de E4 aplicada igual a todas las menciones con el catálogo nuevo, y no hago excepciones a mano en el grafo
     evaluado. Queda como pendiente para el grafo corregido.»
  2. «El cambio de scripts/regression_kg_esperado.json en las 78 rutas (commit 71cb9305 del T3): aceptado, declarado en el sello.»
- **La revisión de la mesa, por código** (`decisiones_254_mesa/reapl/`): el paquete da 161 de 161; el paso 1 da el sello de la tanda final
  byte a byte, en los dos grafos, salvo el reporte del ensamblado, igual con sus rutas normalizadas; el paso 5 y su segunda armada dan los
  mismos `kg.json` (los tres, 11 de 11); los nodos y las aristas de los cinco pasos son los de la tabla del FRENO; y cada pieza toca solo lo
  suyo: D, los nodos que salen y los que entran son los mismos en número por tipo (115 con cola y 99 sin cola); las claves, solo Sujetos,
  con toda arista que cambia en un Sujeto; C1, solo Comunicaciones; las remisiones, solo `remite_a` que entran (27.133 con cola y 24.301 sin
  cola). En el paso 3, una `aplica_a` pasa, con su misma procedencia, de un Sujeto que no cambia a un alta nueva del catálogo: es la
  re-resolución del FRENO, §6.2, y cumple la regla del mandato. La mesa rehizo además las ampliaciones con la regla del label (35 altas y 12
  alias, iguales; 32 de 47 formas con artículo), recompuso el catálogo de resolución con el `componer` de HEAD (10 de 10 archivos iguales,
  `54147015…`) y las 78 rutas sobre `2db79462` (las mismas, y cambian las 4 que declara el FRENO). R19 y los tres selftests, en las consolas
  del paquete. **Da el OK.**
- **El sello del grafo evaluado** (decisión 2): el 170, armado y probado en clones de HEAD (713 archivos, con 7 pruebas en contra). Entran
  en `data/experiment/reaplicacion_unica/` los dos ensamblados del paso 5 sin su `kg.json`, que pasa de 100 MB, con su `kg.json.gz` y su
  sello (`scripts/kg_gz.py`: sin cola `8a448e91…`, con cola `7202d58d…`); el paquete de la re-aplicación tal cual, con sus 8 NO_ABRIR_ por
  sus bytes; y `sello_grafo_evaluado.json`, con los sha256 de los dos grafos, las 78 rutas (`cfed608d…`), el catálogo de resolución y las
  dos declaraciones de la autora. Tres consolas del paquete que el `.gitignore` ignora por su extensión entran con `git add -f`, sin
  tocarlo, como en `fb685a79`. El registro en `grafos.py` y la carga en Neo4j van con la unidad de los índices del grafo evaluado.
- **Lo que sigue al sello,** tal cual (decisión 3): «Apenas se selle el grafo evaluado: los sorteos de B6.3 y el sorteo de la etapa T de
  tripletas (enmienda 4, punto 6), fuera del repo y sellados antes de que se lea nada.»
- **Los sorteos de B6.3** (decisión 4), tal cual:
  1. «las semillas que proponés: B63:sorteo:documentos:v1, B63:sorteo:unidades:v1 y B63:sorteo:tipos:v1;»
  2. «P-1 a P-4, como los proponés;»
  3. «la contaminación que no está en el código: armá la lista de candidatos con un criterio mecánico, desde el registro y los registros de
     cada lectura. Entra cada documento elegible que una decisión nombra y cuya extracción, segmentación, alcance o resolución se corrigió
     solo para ese documento, como el alcance de los dos de la tanda 1 (§10). Las correcciones que valen para todo el corpus por regla (el
     catálogo, C1, D, las remisiones) no cuentan. Mostrámela por documento, con la decisión que lo nombra; la apruebo yo antes de la corrida
     real, y ante la duda el documento sale.»
- **La lista de candidatos de la mesa** (`decisiones_254_mesa/sorteos/`): 49 de los 77 elegibles (régimen informativo, 23 de 26; normativa
  general «digerible», 13 de 35; «necesita reglas», 13 de 16), 35 por renglones de las decisiones de `docs/` y 31 por su fila en el registro
  de alcance que lee la cadena. Si salen todos, no alcanza el núcleo de O2 (quedan 3, 22 y 3); si salen solo los de renglones, alcanza el
  núcleo y no la tercera ola (quedan 11, 22 y 9), así que el N no pasa de 64. La aprueba la autora antes de la corrida real (PENDIENTE).
- **D-10,** tal cual (decisión 5): «D-10: tu propuesta. Antes del juez, un script cuenta por brazo las respuestas con marcas de su brazo, la
  cifra se declara y no se edita ninguna respuesta.» Va al borrador v3 del pre-registro de B6.3.
- **La etapa a-ter del juez v2** (14:24:16; `revision_UTRIP_V_JUEZ_v2_a_ter/`, 59 archivos, manifiesto `1687f327…`): V005 sale sin
  reemplazo, y los otros 9 van del 24 al 32; la iteración 1 juzga 91 fichas, una más que en la a-bis (90; las corridas en seco de los dos
  paquetes). La mesa la revisó (11 de 11) y armó el comando v2 de la iteración 1 con los sha256 nuevos (de 17 archivos cambian 8; sus cuatro
  pruebas dan lo del anterior). La cota de 10 casos no la lee el comando ni la iteración: el tope y el freno (USD 42 y 35,70) van en el
  comando, y la a-ter rehizo la cota con 273 pedidos en su corrida en seco. El comando de la §248 queda renombrado a
  NO_CORRER_REEMPLAZADO__.
- **Cuándo corre la iteración 1:** hoy, después de lo pago de A2.1 (su humo y H-B2), y no al lado: el comando frena si ve un proceso de
  A2.1. Si lo pago de A2.1 termina tarde, mañana a las 08:00. Las duraciones son NO VERIFICADAS.
- **La validación por expertos** (14:41:03), tal cual:
  1. «Las 20 se sortean de una vez, como dice la nota del 21/10, apenas quede revisado y sellado el núcleo aprobado (las olas 1 y 2), y van
     en un solo envío.»
  2. «Las mismas 20 van a cada experto, para medir también el acuerdo entre ellos.»
  3. «Lo que marquen los expertos no cambia ninguna pregunta ni ninguna cifra confirmatoria. Se informa por experto y en conjunto, con su
     Wilson, como acuerdo con P3 y como acuerdo entre expertos. Para la sensibilidad, una pregunta cuenta como «no respondible» si la marca
     la mayoría de los expertos que la respondieron (con dos, los dos).»
  4. «H-14: el envío sale el domingo 25, después de la ola 2, y la devolución es hasta el martes 27 a las 12:00; lo que no llegue, se
     declara.»
  5. «Armá ya el material: la planilla para el experto (la pregunta, su respuesta y el texto de su ancla; si se puede responder desde el
     texto, sí o no; si la respuesta es correcta, sí, parcial o no; la relevancia con la rúbrica del punto 1; y una columna de comentario) y
     las instrucciones, para que salga por script en minutos apenas se selle el núcleo aprobado. El mensaje a los expertos lo escribo yo.»
- **El material,** por script (`decisiones_256_mesa/experto/material_experto_B63_mesa.py`, selftest 14 de 14): las 20, con la semilla de la
  nota del 21/10; una planilla por experto, igual para todos; las instrucciones, con la rúbrica tal cual; y la clave de los códigos, aparte.
  Corre apenas se selle el núcleo aprobado. La respuesta de cada pregunta son sus criterios con su cita, porque el molde es el de EV2.
- **Lo que sigue:** el 170 y el commit de esta sección, antes de pegar el «seguí» v2 de A2.1; lo pago de A2.1 y después la iteración 1 de la
  v2; la aprobación de la lista de contaminados y los sorteos de B6.3, sellados; el despacho de la generación de las preguntas (P2) y el del
  sorteo y las fichas de la etapa T de tripletas (PENDIENTES de la mesa).
- Las secciones anteriores no se editan.

## 101. El viernes, a las 15:12: la regla del 09/10 para los contaminados de B6.3, la lista desde los registros de cada corrección y la exposición (23/10/2026)

Decisiones y hechos de la autora del 23/10/2026, recibidos a las 15:12:46 (hoja de ruta de la mesa, §257).

- **El 170 y el 171,** corridos con su push (`fde70c67`, a las 15:09:01, y `0a6374ba`, a las 15:10:00, git log; `origin/main` en
  `0a6374ba`). La autora pegó el «seguí» v2 del tramo 2 de A2.1.
- **La lista de contaminados,** tal cual: «el criterio de mi decisión 4.c de esta tarde estaba mal. Lo reemplaza mi regla del 09/10/2026,
  tal cual (plan, :782, puntos 4 y 5): salen del sorteo solo los documentos que recibieron una corrección hecha para ellos, es decir, una
  lista de R5-a (o de R5-a′), un corte a mano o el laudo de un caso que cambió su extracción, su segmentación o su resolución. Los que solo
  se leyeron para medir quedan elegibles, y su exposición se declara. La fila del registro de alcance no es contaminación: es el confusor
  del origen del alcance (catálogo o registro) del punto 5, que se declara en el informe. Cuenta solo si esa fila se corrigió después de una
  lectura que la encontró mal. Mi ejemplo de la §10 también estaba mal: el alcance de depaho y de snp_tr no se corrigió, quedó como estaba,
  declarado.»
  1. «Armá la lista de nuevo desde los registros de cada corrección (las listas de S0-5a, los cortes a mano y los laudos), no por
     palabras: por documento, con la corrección y su ancla. Aparte, los que solo se leyeron para medir, con su exposición.»
  2. «Si con esa lista no alcanza el núcleo de O2, frená y mostrame cuántos faltan por clase, sin relajar nada.»
  3. Sobre la frase nueva del §3.1 del borrador v3 del pre-registro de B6.3 («Si los que quedan no alcanzan para la tercera ola, el N no
     pasa de 64, declarado»): «de acuerdo».
  4. «Mientras corre el tramo 2 de A2.1, ningún commit: lo que registre esto va entre su FRENO y el «seguí» del tramo 3.»
- **La lista de la §100 queda reemplazada.** Sus 49 candidatos salían de palabras en las decisiones y de la fila de alcance, con el criterio
  de la decisión 4.c, que contradecía la regla del plan (`docs/plan_tesis.md:782`, punto 4). El borrador v2 de B6.3 ya citaba esa regla y la
  mesa no reportó la contradicción: es un error propio de la mesa (hoja, §257).
- **La lista nueva, desde los registros de cada corrección** (`decisiones_257_mesa/contaminacion/`): 0 de los 77 elegibles.
  - **Las listas de S0-5a y toda constante por documento del código:** 81 commits del pipeline, sin una constante propia de un elegible en
    ninguno. Las listas por documento de S0-5a-bis, en el `correr_e0.py` que aplicó S0-5b (`af7ffdd4`), son de 32 documentos (las de R5-a,
    de 29; la de R5-a′, de 1), y ninguno es elegible: los elegibles de O2 ya los sacaron por su constante en E0
    (`data/experiment/esq/elegibles_B63_O2_2026-10-15/`).
  - **Las listas y los registros que lee la cadena,** en cada versión de sus 31 archivos: los elegibles aparecen solo en lo que vale por
    regla (el catálogo, el esquema, el inventario, las ampliaciones del catálogo de resolución y el registro de alcance). Las listas de C1
    no traen ningún elegible, y ninguna de las 31 filas de alcance de un elegible cambió después de escrita.
  - **Los cortes a mano:** el de los dos mixtos (`docs/mandatos/USEG_OFICIAL_S0-5a_reglas_de_corte_E0.md:440`), de ri_spi y ri2_ae, que ya
    están fuera por la decisión 2.
  - **El alcance por tanda:** opecam y regpri estaban entre los candidatos a la regla del título no decididos y la lectura del 18/10/2026
    los decidió; no es una fila corregida.
- **Un caso para la autora, D-11:** ri_transpa. El laudo de las §43 y §44 declara faltante en el grafo evaluado la unidad
  `ri_transpa::Sbloque1::chapeau_seccion` y la extrae después del sello, para la versión corregida. La mesa recomienda que quede elegible:
  el laudo no cambió su extracción en el grafo evaluado, y las preguntas que caen en esa unidad ya salen de la cifra aparte (§62).
- **El núcleo de O2 alcanza:** quedan 26, 35 y 16 por clase (25, 35 y 16 sin ri_transpa), con seis olas posibles en las dos formas. El
  sorteo no frenó.
- **La exposición, aparte:** por documento y por lectura, las unidades que estuvieron a la vista, de las lecturas con registro en el repo
  (T4 de la tanda 1 y de la tanda final, las lecturas de cortes de S1 y S1-bis, la evidencia de las ampliaciones de las claves y las
  lecturas del alcance). 76 de los 77 tienen alguna. Las lecturas con registro en carpetas que la mesa no abre (S1-ter, S1-quater, S0-6a,
  U-MED-UMBRALES, U-COMP-E1 y las lecturas de la autora fuera del repo) van sin cifra.
- **El borrador v4 del pre-registro de B6.3** (`decisiones_257_mesa/b63/`): la regla del 09/10 en el §3.1, con la lista, la frase de la
  tercera ola aprobada y el freno del núcleo; la exposición y el confusor del origen del alcance en lo que se declara (§11); y la D-11
  abierta.
- **Lo que sigue:** la D-11 y los sorteos de B6.3, sellados fuera del repo antes de que se lea nada; el commit de esta sección y de la
  siguiente, después del FRENO A2.1-b (§102).
- Las secciones anteriores no se editan.

## 102. El viernes, a las 15:58: la D-11, la exposición sin cifra, las correcciones de E0 por regla general y los sorteos de B6.3 sellados (23/10/2026)

Decisiones de la autora del 23/10/2026, recibidas a las 15:58:21 (hoja de ruta de la mesa, §258), sobre la §101, tal cual:

1. «D-11: ri_transpa sigue elegible, con su exposición declarada. El laudo no cambió su extracción en el grafo evaluado, y las preguntas que
   caen en ri_transpa::Sbloque1::chapeau_seccion salen de la cifra aparte (registro, §62).»
2. «La exposición de las lecturas cuyo registro está en carpetas que no abrís (S1-ter, S1-quater, S0-6a, U-MED-UMBRALES, U-COMP-E1 y mis
   carpetas de lectura): no autorizo abrirlas ni contarlas por código. Se declaran por nombre, sin cifra, con el motivo: el cegamiento y
   las carpetas cerradas.»
3. «Agregá al §11 del borrador: las correcciones de E0 por regla general (S0-6a), diseñadas a partir de errores vistos en S1-ter, valen
   igual para los dos brazos, porque los dos usan la misma E0 del grafo evaluado; se declaran.»
4. «Corré los sorteos reales de B6.3 con contaminados_B63_v2_regla.json, fuera del repo, y sellalos antes de que se lea nada. Después, los
   despachos de P2 y de la etapa T de tripletas.»
5. «El 172 va después del FRENO A2.1-b, no en «LISTO PARA LOS PASOS PAGOS». Rearmalo con estas decisiones.»

Y: «Mientras corre el tramo 2 de A2.1, ningún commit.»

- **Los sorteos de B6.3, corridos y sellados** por la mesa, fuera del repo (`decisiones_258_mesa/sorteos/`, en su paquete):
  - `sorteo_B63.json`, sha256 `4e751e2350cd5e0571494383bc7d2cf5897b83313b36df4ee76da6c90abf8adb`, 104.738 bytes, sellado el 23/10/2026 a
    las 16:03:44 en `sello_sorteo_B63.txt` (`4d0a7c93…`), antes de que nadie leyera la salida; la mesa no la abrió;
  - sobre HEAD `0a6374ba`, con el script de la §254 (selftest 14 de 14), las semillas de la §100 y ningún contaminado; dos corridas, los
    mismos bytes;
  - quedan los 77 documentos (26, 35 y 16 por clase) y 6 olas de 32. Con el N de la §94, a lo sumo 96, se usan las olas 1 a 3.
- **Los dos despachos,** escritos por la mesa (`decisiones_258_mesa/despachos/`); pegarlos es de la autora (PENDIENTE):
  - **P2, la ola 1:** desde `fuera_del_repo/b63_p2/`, que la mesa armó con el sorteo sellado, la regla sellada de la etapa 1 y los ocho
    archivos del generador de N3, cada uno controlado por su sha256. Genera los 32 lugares de la ola 1 con la regla de rechazo aplicada
    al tipo, la sella y frena; las olas 2 y 3 van con otro «seguí»;
  - **U-TRIP-T:** desde `fuera_del_repo/tripletas_t/`, con los 64 ítems de U-MED-DESAMB. Sortea las 400 aristas de contenido del grafo
    evaluado y, dentro de ellas, las 100 de la autora, con la semilla de la enmienda 4; sella las dos listas juntas, arma las 400 fichas y
    las hojas, y frena. La mesa le agrega el conteo declarado de las aristas que son una de las 120 de V.
- **El borrador v5 del pre-registro de B6.3** (`decisiones_258_mesa/b63/`): la D-11 decidida, la exposición de las carpetas cerradas por
  nombre y sin cifra, las correcciones de E0 por regla general en el §11 y el sorteo sellado en el §3.3 (H-10). No queda ninguna decisión
  abierta.
- **El 172, rearmado:** lleva esta sección y la §101, que cambia solo en cuándo va su commit. Corre después del FRENO A2.1-b, no en
  «LISTO PARA LOS PASOS PAGOS». El 172 de la §257 no corrió y queda renombrado a NO_CORRER_REEMPLAZADO__.
- **Lo que sigue:** pegar los dos despachos; revisar sus FRENOs; y el 172, después del FRENO A2.1-b (PENDIENTE de la autora).
- Las secciones anteriores no se editan.

## 103. El viernes, a las 16:25: P2 pegado, el cegamiento de U-MED-VERIF en la etapa T y la prueba de la v2 sin los casos de su prompt (23/10/2026)

Decisiones y hechos de la autora del 23/10/2026, recibidos a las 16:25:16 (hoja de ruta de la mesa, §259).

- **P2:** la autora pegó el despacho de la ola 1 tal cual, en una sesión nueva abierta en `fuera_del_repo/b63_p2/`. El de U-TRIP-T
  todavía no.
- **Las decisiones,** tal cual:
  1. «P2: que frene después de la ola 1, como está. Cuando llegue su FRENO y lo revises por código, si está bien, el «seguí» de las olas
     2 y 3 va enseguida, sin esperar mi revisión de la ola 1. Las preguntas nuevas para las que rechace van en un «seguí» aparte.»
  2. Sobre U-TRIP-T, antes de pegarlo:
     a. «Le falta el cegamiento de U-MED-VERIF: no me muestran la extracción de una unidad de su muestra antes de que cierre esa lectura, y
        las fichas de T son extracciones. La ejecutora marca por código y en memoria, como en U-REAPL (§11 del despacho de la §249),
        cuáles de las 400 y de mis 100 vienen de una unidad de esa muestra, sin escribir la muestra ni dar su tamaño ni sus ids. Esas
        fichas van a un lote aparte, que leo recién cuando cierre U-MED-VERIF. El acta, el FRENO y la consola van sin contenido de nodos,
        solo con códigos.»
     b. «El agregado del punto 4.e (las coincidencias con V): sí. Y sumá al pre-registro de B6.3: si alguna de mis 100 coincide con un
        caso del prompt de la v2, la prueba de la v2 sobre T se informa también sin ella, al lado.»
  3. «Esto va al registro en el 172 v2 rearmado o en el commit siguiente, siempre después del FRENO A2.1-b.»
- **El despacho de U-TRIP-T, v2** (`decisiones_259_mesa/despachos/`), PREPARADO; pegarlo es de la autora:
  - la muestra de las FICHAS de U-MED-VERIF se arma en memoria con el procedimiento del censo de la mesa (§178, `:98-115`): el sorteo
    sellado (`e27796ce…`, el único `NO_ABRIR_` que abre la ejecutora), la lista de exclusión de `0c2befad` (`5ec9753d…`) y las 7 de la
    mesa. La ejecutora marca las fichas que vienen de una unidad suya solo en un `NO_ABRIR_`, por la referencia de la ficha, y las de las
    100 van a un lote aparte;
  - el acta, su sello, el FRENO y la consola llevan cada arista y cada nodo por su código (`sha256(id)[:12]`) y cuentas;
  - las coincidencias con las 120 de V, en el acta, declaradas y sin excluir.
- **El borrador v6 del pre-registro de B6.3** (`decisiones_259_mesa/b63/`): el lote aparte de U-MED-VERIF y la prueba de la v2 también sin
  las de las 100 que coincidan con un caso de su prompt, en el §10.1; y las coincidencias con V, en lo que se declara (§11, punto 14). La
  coincidencia con los casos la calcula la mesa por la clave de la arista, con el acta de T y los casos de la v2 congelada.
- **El «seguí» de las olas 2 y 3 de P2,** en BORRADOR (`decisiones_259_mesa/despachos/`): va apenas la mesa revise el FRENO de la ola 1,
  si la revisión da bien. P2 sella la ola 2, arma su paquete y sigue con la 3 sin frenar.
- **El 172, rearmado otra vez:** lleva la §101 v2, la §102 y esta sección, y corre después del FRENO A2.1-b. El 172 v2 no corrió y queda
  renombrado a NO_CORRER_REEMPLAZADO__.
- Las secciones anteriores no se editan.

## 104. El viernes, a las 16:54: el 173, U-TRIP-T pegado y U-MED-VERIF cerrada sin medir (23/10/2026)

Decisiones y hechos de la autora del 23/10/2026, recibidos a las 16:54:24 (hoja de ruta de la mesa, §262), sobre las §260 y §261 de la
mesa.

- **El 173,** corrido con su push (`6c6dcad9`, a las 16:53:24, git log; `origin/main` en `6c6dcad9`): los cinco archivos del tramo 2 de
  A2.1 que revisó la mesa (§261), con los mismos sha256.
- **U-TRIP-T:** la autora pegó el despacho v3 «SI SE CIERRA U-MED-VERIF» tal cual, en una sesión nueva abierta en
  `fuera_del_repo/tripletas_t/`, con el acta, el FRENO y la consola solo por código.
- **U-MED-VERIF,** tal cual: «la cierro sin medir, como desvío declarado (opción b de tu §260). La decido hoy, sin haber visto nada de
  ella. Va al capítulo 6 como medición diseñada que no se hizo, con su diseño sellado del 17/10 y sus fichas selladas del 18/10, y no se
  vuelve a medir a ciegas. Se levantan los cegamientos que dependen de U-MED-VERIF, los que listás en la §260; los demás siguen. Va al
  registro en el commit siguiente al 172 v3.»
  - **Lo que se levanta** (respuesta de la mesa, §260, punto 4):
    1. nada por estado de E3 ni de los reintentos, en las tandas 1 y final (pre-registro de la tanda 1, [v8], `:900-909`; pre-registro de
       la tanda final, `:142` y `:183`; U-PROC-HERENCIA, §7 bis, punto 1);
    2. la regla de exclusión antes de mostrar una extracción de la tanda 1 (U-PROC-HERENCIA, §7 bis, punto 3), y sus casos en espera;
    3. en el censo de C1, los nodos que no se unieron por la muestra, que vuelven para el grafo corregido (§47);
    4. el bloque de herramientas de N7 (§45);
    5. la lectura de la autora del control de B6.3 y de cualquier respuesta de B6.3 (§49);
    6. en T, el lote aparte, que ya no va: el despacho pegado es el que no lo lleva;
    7. los códigos en lugar del contenido de los nodos que impone U-PROC-HERENCIA (§7 bis, punto 2), en lo que salga de ahora en más.
  - **Lo que sigue:** la generación y la revisión de las preguntas de B6.3, a ciegas del grafo; la lectura de T de la autora después de la
    firma de B6.3, ciega al juez; el material del juez v2; U-MED-UMBRALES, las adjudicaciones de S1-ter y S1-quater, las demás carpetas
    vedadas y todo `NO_ABRIR_` que no sea de U-MED-VERIF; la validación por expertos; y, en T, el acta, el FRENO y la consola por código.
  - **El diseño, las fichas y la clave de U-MED-VERIF** quedan sellados como están, sin abrir.
- **Los dos pasos pagos de A2.1:** la autora los corre ahora, de a uno, según su mensaje. Su resultado llega con el FRENO A2.1-b.
- **El borrador v7 del pre-registro de B6.3** (`decisiones_262_mesa/b63/`): la lectura del control sin esperar a U-MED-VERIF (§7.3), la
  etapa T sin el lote aparte (§10.1) y U-MED-VERIF en los desvíos declarados (§15).
- **El orden:** el commit de las §101 a §103, después del FRENO A2.1-b, y el de esta sección, después de ese.
- Las secciones anteriores no se editan.

## 105. El viernes, a las 17:05: los pasos pagos del tramo 2 de A2.1 y la ola 1 de B6.3, sellada y revisada (23/10/2026)

Hechos de la autora del 23/10/2026, recibidos a las 17:05:00 (hoja de ruta de la mesa, §263), y la revisión de la mesa.

- **Los dos pasos pagos del tramo 2 de A2.1,** corridos por la autora de a uno. Según su mensaje:
  - el humo: 12 sesiones completas, USD 0,3051;
  - H-B2: 8 sesiones; las 4 que cortó el tope de turnos son las de tope chico del diseño;
  - el gasto del tramo 2: USD 0,5158, igual por R9 y por el CLI, sin ningún freno;
  - el control del disco no frenó en ninguna sesión, y el valor remoto quedó vacío en las 20;
  - H-B2 da «NO VERIFICADO | CARACTERIZADO: --max-turns acota n_mensajes_asistente» en las dos lecturas.

  La mesa todavía no verificó estas cifras (NO VERIFICADO): van con la revisión del FRENO A2.1-b. La autora le escribió «corridos» a la
  ejecutora.
- **La ola 1 de P2:** sellada a las 16:58:50 (`olas/ola_1.json`, `e1aeb116…`, y su registro de generación, `79600966…`), con su FRENO y
  su paquete (51 archivos, `manifest.txt` `a17aa2ad…`). La autora le pidió a P2 que espere la revisión de la mesa.
- **La revisión de la mesa** (`decisiones_263_mesa/p2/`), por código y sin leer ninguna pregunta ni ningún criterio: 20 de 20 controles.
  - «Grandes exposiciones al riesgo de crédito» es `gerc`, que no está entre los 128 documentos del grafo evaluado: los lugares 11 y 12
    quedan como están.
  - Los 14 reasignados, frente a lo que se esperaría con las tasas de P1:
    - dato directo: 5 de 13, contra 5,4;
    - remisión: 4 de 10, contra 5,9 a 7,9;
    - condición: 2 de 5, contra 5,0;
    - definición: 3 de 4, contra 3,9.

    La diferencia en condición y en definición viene de que P2 encuentra esos frentes mucho más seguido que P1. El tipo coincide con P1 en
    9 de las 11 unidades que juzgaron las dos.
  - La concentración de los lugares de `ceninf` en su punto 5.1 es la que da la regla de avanzar en el orden sorteado.
- **Cuatro decisiones para la autora, PENDIENTES** (la revisión, §5). En las cuatro, la mesa recomienda seguir como en la ola 1, y
  declararlo:
  - D1, el subtipo: el frente sobre el que se construye la pregunta, o la primera forma de P1;
  - D2, los frentes (c) y (d), que P2 encuentra mucho más que P1;
  - D3, una unidad en más de un lugar;
  - D4, dos criterios de lectura nuevos de P2.
- **El «seguí» de las olas 2 y 3:** PREPARADO por la mesa con esas recomendaciones (`decisiones_263_mesa/despachos/`). Pegarlo es de la
  autora.
- **El 172 y el 174, rearmados:** los títulos de las §101 a §104 llevan la hora de recepción en lugar de una franja del día, que no tenía
  ancla ni coincidía con esas horas, y la §104 va en el mismo commit que esta sección. Los dos anteriores no corrieron y quedan renombrados
  a NO_CORRER_REEMPLAZADO__.
- **El orden:** el commit de las §101 a §103, después del FRENO A2.1-b, y el de la §104 y esta sección, después de ese.
- Las secciones anteriores no se editan.

## 106. El viernes, a las 20:51: la ola 1 de B6.3 decidida, el FRENO A2.1-b con el cwd enmascarado, R5 y el tope de A2.2, y U-TRIP-T (23/10/2026)

Decisiones y hechos de la autora del 23/10/2026, recibidos a las 20:51:09, con dos agregados a las 20:54:27 y a las 21:01:34 (hoja de ruta
de la mesa, §264), sobre la §263 de la mesa y los FRENOs que llegaron.

- **La ola 1 de B6.3:** D1 (a), D2 (a), D3 (a) y D4 (a), como lo recomendó la mesa (§105):
  - D1: el subtipo de un lugar es el frente sobre el que se construye la pregunta, aunque no sea la primera forma de P1. En las olas 2 y 3,
    P2 anota en cada ancla de condición o de definición si aplica también un frente anterior;
  - D2: P2 encuentra los frentes (c) y (d) mucho más seguido que P1, y su lectura queda, sin cambios. En el pre-registro de B6.3 se declara
    como límite: los pesos salen de P1, y el tipo coincide con P1 en 9 de las 11 unidades que juzgaron las dos;
  - D3: una unidad puede ser ancla u otro punto de más de un lugar, declarado;
  - D4: los dos criterios de lectura nuevos de P2 rigen también en las olas 2 y 3, y van al pre-registro con sus lugares.
  - El «seguí» de P2 para las olas 2 y 3, pegado tal cual.
- **El 172 v4 y el 174 v2,** corridos con su push: `f7d7877d` (20:50:33) y `084499c6` (20:50:40), por git log; `origin/main` en `084499c6`.
- **El FRENO A2.1-b,** revisado por la mesa (`decisiones_264_mesa/a21b/`): se reproduce desde las salidas crudas, 13 de 13, y el análisis de
  la ejecutora da su JSON byte a byte. Quedan verificadas las cifras de la §105:
  - el gasto: USD 0,515819 (0,305127 del humo y 0,210692 de H-B2), igual por R9 y por el CLI;
  - las 20 sesiones, con los cuatro cortes de H-B2 (HB2-01, HB2-02, HB2-06 y HB2-07);
  - el control del disco, sin ningún freno, y el valor remoto, vacío en las 20;
  - `--max-turns` acota los mensajes del asistente: una sesión se corta si y solo si su mensaje número k pide tools.
- **El cwd de los 40, tal cual** (primer agregado): «En el repo van enmascarados: la carpeta personal reemplazada por $HOME, sin ningún otro
  cambio de bytes. Los originales quedan fuera del repo, donde propongas, y el commit lleva el sha256 de cada original y de su versión
  enmascarada, con el script que enmascara.»
  - **Lo que propone la mesa:** los originales, en `$HOME/INGENIERIA IA/TESIS/fuera_del_repo/banco_mcp_originales_A2_1/`, con las rutas
    del repo; en el repo, `a2_1/enmascarar_cwd_a2_1.py` y `a2_1/enmascarado_cwd_a2_1.json` (40 archivos, 171 reemplazos). El script saca
    la carpeta personal de los datos y no la escribe en ningún archivo. Lo aplica el 175.
  - **Lo que ya está en el repo con el nombre de la cuenta,** sin tocarlo en este commit (`nombre_de_la_cuenta_en_el_repo_mesa.py`, sin
    las rutas cegadas): 291 archivos rastreados. De ellos, 78 son salidas de sesiones (todas en `data/experiment/banco_mcp/`), 20 son otros
    archivos de `banco_mcp/` y 193 están fuera de él.
  - **El README del banco** (`data/experiment/banco_mcp/README.md:215-219`) dice que los streams traen el cwd y no se editan: queda corto
    para A2.1. Su cambio es PENDIENTE de la autora.
- **R5 y el tope de A2.2,** para la firma de A2.2 (`decisiones_264_mesa/r5/`):
  - **la regla del registro** (§50, punto 4) con la señal de H-B2 da `--max-turns` 32, sin cambio: 30 + 2, en mensajes del asistente.
    `--max-turns` no acota las llamadas, y el tope de 30 queda en el prompt y en el presupuesto de 1,80 por sesión;
  - **las opciones:** (1) R5 como está, con «al tope» contado en llamadas por el log R1; (2) lo mismo con un tope duro de 30 llamadas en
    los servidores, que es código nuevo; (3) lo mismo, excluyendo de la métrica las sesiones con más de 30 llamadas. La mesa recomienda la
    (1). La propuesta del FRENO de `--max-turns` 12 contradice R5;
  - **A-D2:** A2.2 cuesta (40 + 2P) × 0,2443, 0,3407 o 0,5334 (central, medio o alto), con P las preguntas que van a N = 3 parciales. La
    mesa recomienda el medio de ese P, redondeado al dólar de arriba, con freno en el 75 %;
  - las dos decisiones son PENDIENTES de la autora, al firmar A2.2.
- **U-TRIP-T,** revisado por la mesa (`decisiones_264_mesa/utrip_t/`): el sorteo de T se reproduce con código propio desde el `.gz` de
  HEAD, 21 de 21, con los mismos sha256 y los mismos solapamientos. En su §12 no hay nada para corregir.
  - **Su error 1, tal cual** (segundo agregado): «su error 1, que mostró en su consola parte de la clave de T001, del lote 01, sin
    etiquetas ni textos, lo acepto declarado. La muestra, el orden y las hojas no cambian, y yo no miro esa consola.»
- **El «seguí» del tramo 3 de A2.1, con el insumo v2:** PREPARADO por la mesa (`decisiones_264_mesa/despachos/`). Pegarlo es de la autora,
  después del 175 y del commit de esta sección.
- **El orden:** el 175 (lo del tramo 2 de A2.1, con los 40 enmascarados), el commit de esta sección y, después, el «seguí» del tramo 3.
- Las secciones anteriores no se editan.

## 107. El sábado, a las 09:46: R5, el tope y las sesiones de A2.2, la iteración 1 del juez v2 y las olas 2 y 3 de B6.3 (24/10/2026)

Decisiones y hechos de la autora del 24/10/2026, recibidos a las 09:46:49 (hoja de ruta de la mesa, §265), sobre la §264 de la mesa y los
FRENOs que llegaron.

- **El 175 y el 176,** corridos con su push: `7a9fe8ca` (09:46:09) y `af4dab8e` (09:46:16), por git log; `origin/main` en `af4dab8e`. El
  175 dejó los 40 originales fuera del repo, en `fuera_del_repo/banco_mcp_originales_A2_1/`, con su manifiesto (41 archivos).
- **El «seguí» del tramo 3 de A2.1,** pegado tal cual. La ejecutora escribe el borrador del pre-registro de A2.2 en el repo: ningún commit
  corre hasta su FRENO A2.1-c.
- **Las decisiones sobre la §264, tal cual,** para que el borrador de A2.2 llegue con ellas a la firma:
  1. «R5: tu opción (1). --max-turns 32 por la regla del §50, igual en los dos brazos, y se informa por brazo cuántas sesiones pasan de 30
     llamadas en el log R1. No se excluye ninguna sesión por eso.»
  2. «A-D2: el tope en el costo alto de tu cuenta, con el P que cite la ejecutora, redondeado al dólar de arriba, y el freno en el 75 % de
     ese tope. A2.2 se mide una sola vez, y un corte a la mitad no se puede repetir; el costo medio queda siempre adentro.»
  3. «A-D4: sí, las transcripciones y los streams de A2.2 van al repo enmascarados como los del tramo 2, con los originales fuera del repo
     y su sha256.»
  4. «La nota del README del banco (README.md:215-219): se actualiza. Desde el tramo 2 de A2.1, los streams y las transcripciones van al
     repo con la carpeta personal como $HOME, y los originales quedan fuera del repo con su sha256. Va en el commit siguiente, cuando no lo
     cruce ninguna foto.» Va en el commit de esta sección.
  5. «Los 291 archivos que ya están en el repo con el nombre de la cuenta: no se tocan ahora. Anotalos como pendiente para cuando se
     publique el repo, junto con la historia de git, que también los trae.» Queda PENDIENTE para la publicación del repo: los 291
     archivos rastreados (`nombre_de_la_cuenta_en_el_repo_mesa.py`, §264 de la mesa) y la historia de git.
- **La iteración 1 del juez v2,** según el mensaje de la autora: 273 de 273 completas, 0 sin voto, 0 rechazos, USD 14,7828 y sin corte. La
  mesa controló por código la marcada (`3a0734a1…`), el prompt (`cf40964d…`) y, de la regla de freno, solo que dice «frena: false», sin
  congelar. Lo que sigue es la etapa b: los casos nuevos de la iteración 2 desde los desacuerdos de la 1 (enmienda 4, puntos 3 y 4). Su
  «seguí» está PREPARADO por la mesa.
- **Las olas 2 y 3 de B6.3:** selladas a las 21:15:08 (27 preguntas) y a las 21:27:58 (24); los dos paquetes dan sus sha256 (42 de 42 y
  41 de 41). Las decisiones de la autora, tal cual:
  1. «Rige la regla: cada uno de esos 13 lugares pasa al documento siguiente de su clase en el orden sorteado, con su ola, su tipo y su
     subtipo, como la P-4 al sortear, y se declara.»
     - **La contradicción que reporta la mesa** (CLAUDE.md, §4.d): la P-4 tal cual deja 12 lugares en un documento y 7 en otro. El mandato
       firmado dice «Para N > 64, las olas van en más documentos, con 4 preguntas por documento».
     - **Lo que preparó la mesa:** el «seguí» de P2 lleva la versión que cumple las dos cosas, el documento siguiente de su clase con menos
       de 4 lugares y unidades sin lugar. Así quedan 4, 4, 2 y 3 en cuatro documentos de la ola 4 del sorteo. La P-4 tal cual queda sellada
       al lado. La elección es PENDIENTE de la autora.
  2. «Los ocho criterios de lectura nuevos de las olas 2 y 3: rigen en las tres olas, como en D4.» El control por código de la mesa marca
     dos candidatos en la ola 1, los lugares 6 y 23, frente al criterio 2 de la ola 2. P2 los vuelve a mirar sin cambiar ninguna ola
     sellada.
  3. «El criterio 5 de la ola 2 (la búsqueda de la unidad siguiente no vuelve al principio del orden): queda, y lo que deja sin unidad pasa
     al documento siguiente por el punto 1, como el lugar 28 de la ola 3.»
  4. **Los textos que P2 no identificó:** cuatro están entre los 128 con otro id (`ratio`, `finsec`, `ri_tsa` y `snp_psp`), y P2 vuelve a
     mirar los lugares donde los citó.
- **La hoja de revisión de la autora** de las tres olas (`fuera_del_repo/revision_b63_olas_1_a_3/`, manifiesto `ad6165de…`): 83 preguntas,
  armadas por script desde las olas selladas, sin que la mesa lea ninguna. Lleva las instrucciones, con las reglas citadas de su fuente, y
  el convertidor y el sello, probados sobre olas sintéticas (10 de 10).
- **El orden:**
  - el FRENO A2.1-c y, después, el commit de esta sección con la nota del README;
  - el «seguí» de P2 y el de la etapa b del juez v2 pueden pegarse ya: ninguno escribe en el repo.
- Las secciones anteriores no se editan.

## 108. El sábado, a las 10:17: la tabla de los 13 lugares, P2 y el juez v2 en marcha y la revisión de las tres olas (24/10/2026)

Decisiones y hechos de la autora del 24/10/2026, recibidos a las 10:17:05 (hoja de ruta de la mesa, §266), sobre la §265 de la mesa.

- **Los 13 lugares, tal cual:** «Los 13 lugares: la tabla del mandato (d62625d6…), con el documento siguiente de su clase que tenga
  menos de 4 lugares, y se declara que los 5 de la ola 2 caen en documentos de la ola 4 del sorteo.» Con esto se resuelve la elección que
  la §107 dejaba PENDIENTE. La P-4 tal cual queda descartada, sellada en el paquete de la mesa.
- **Los dos «seguí»,** pegados tal cual: el de P2, con los reubicados y los dos controles sobre las olas selladas, y el de la etapa b del
  juez v2. Los dos corren fuera del repo.
- **La revisión de las tres olas:** la autora la empieza, con su hoja (`fuera_del_repo/revision_b63_olas_1_a_3/`).
- **El 177:** la autora lo corre después del FRENO A2.1-c.
- **El FRENO A2.1-c:** ya está en el árbol, sin rastrear, como el borrador del pre-registro de A2.2 (modificados a las 10:16:41 y a las
  10:13:18). La mesa no los leyó: van en la ronda siguiente, con las decisiones de la §107 para ese borrador (R5, A-D2 y A-D4).
- **El borrador v8 del pre-registro de B6.3** (`decisiones_266_mesa/b63/`):
  - D1 a D4 de la ola 1 (§3.2, §11, §14 y §15);
  - R5 con la señal de H-B2 y las sesiones enmascaradas (§5);
  - la regla de los 13 lugares y su declaración (§3.3 y §11).

  No queda ninguna decisión abierta.
- **El orden:** el FRENO A2.1-c, su revisión y su commit; el 177; y el commit de esta sección.
- Las secciones anteriores no se editan.

## 109. El sábado, a las 10:36: el FRENO A2.1-c revisado, las decisiones de la autora para el borrador de A2.2 y la revisión de B6.3 por olas (24/10/2026)

Decisiones y hechos de la autora del 24/10/2026, recibidos a las 10:36:45 y a las 10:39:11 (hoja de ruta de la mesa, §267), sobre la
§266 de la mesa y el FRENO A2.1-c.

- **El 177 y el 178,** corridos con su push: `ecc7a02b` (10:36:25) y `9826b625` (10:36:31), por git log; `origin/main` en `9826b625`.
- **El FRENO A2.1-c y el borrador del pre-registro de A2.2** (`data/experiment/banco_mcp/a2_1/FRENO_A2_1_c.md`, `68b84b97…`, y
  `docs/preregistro_A2_2_sistema_por_fragmentos.md`, `c87b78f2…`), sin rastrear. La mesa los revisó por código y dan (30 de 30,
  `revisar_A2_1c_mesa.py`), y van al repo tal como los entregó la ejecutora, en el commit anterior a esta sección. El paquete de la
  ejecutora, `revision_A2_1_FRENO_c/`, da 31 de 31 por su manifest. `.claude/settings.local.json` lo ignora git (`~/.config/git/ignore`)
  y no entra; la mesa no lo abrió.
- **Las decisiones para el borrador de A2.2, tal cual** (además de R5, (1), y A-D4, (a), de la §107):
  1. «A-D2: el tope para el peor caso, P = 40 con tres re-corridas nuevas: USD 55, con freno en 41,25. La lectura de «re-corrida N = 3»
     (dos más la base o tres nuevas) es la que EV2 aplicó en la práctica: controlá en sus trazas cuántas sesiones corrió por pregunta
     parcial y traémelo con su ancla.» Corregida a las 10:39:11: «Corrijo A-D2: el freno del banco es un corte duro (FRENO A2.1-c, §7),
     así que tiene que quedar por encima del peor caso: P = 40 con tres re-corridas nuevas y el costo alto, USD 55. Tope 74 y freno 55,50,
     en lugar de 55 y 41,25.»
     - **La contradicción que reporta la mesa** (CLAUDE.md, §4.d): con la cuenta del borrador, el peor caso cuesta 39,09 central, 54,51
       medio y 85,34 alto (`tope_A2_2_AD2_mesa.py`). Los 55 son el medio redondeado, no el alto. Con tope 74 y freno 55,50, el freno
       queda por encima del medio y el alto pasa el tope; para que quede por encima del alto, el tope es 114 y el freno 85,50. La
       elección es PENDIENTE de la autora.
  2. «A-D5: (b). La plantilla nueva es la de HEAD sin los cinco TOs de desarrollo y con el tope de 30 llamadas de R5, igual en los dos
     brazos salvo el bloque de herramientas; la escribe la unidad que despacha A2.2, con su diff contra la de HEAD. La validan las
     primeras sesiones de A2.2, una de prueba por brazo sin pregunta de EV2, con freno si fallan R3 o R6.»
  3. «A-D6: (a). Sin fijar, como en el tramo 2, con la anotación de 200.000 caracteres como tope, declarado frente a la §72 y la §79.
     Alineá con esto el §5 del borrador de B6.3, que dice 70.000.»
  4. «A-D7: (b). Semillas propias con la forma de B6.3: A22:orden_corridas:v1, A22:auditoria:v1 y A22:orden_juez:v1.»
  5. «A-D8: (b). El disparo de N = 3 usa solo el veredicto del código, y las requiere_adjudicacion las adjudico al final, sin re-corrida,
     declarado.»
  6. «A-D9: (a). La medida y la prueba son las del pre-registro de B6.3.»
  7. «La lista de ids de la cola del grafo de desarrollo, que el borrador deja PENDIENTE: ubicala vos.»
- **Lo que aplicó EV2** (`contar_recorridas_ev2_mesa.py`, sobre HEAD): tres sesiones nuevas por cada par (pregunta, grafo) que fue a
  N = 3, y la base no vota. Son 66 pares, 63 parciales y 3 de auditoría, con 198 sesiones, y cada par tiene sus tres trazas, una por
  repetición (`data/experiment/ev2_encadenamiento/trazas/ev2_enc_<grafo>_r1` a `_r3`; `poblacion/poblacion_disparada.json`, `n_pares` y
  `n_corridas_agente`; `code/agregacion_enc.py:10`). El tamaño de la auditoría fue max(ceil(10 % · n), 1) por laudo
  (`code/comun_enc.py:180` y `:189`), y el disparador, solo `veredicto_base == 'parcial'` (`poblacion_disparada.json`, `regla`).
- **La lista de la cola:** no hay un archivo aparte. Es la regla del grafo re-sellado (`resellado_t0/registro_vista_r2b_rs1.py:80-87`)
  sobre los cinco `finales.jsonl` del commit del sello (`4fe6ece`), y da 54 unidades: las que marca el `kg.json` (`acb26dca…`) y las que
  descarta el grafo sin la cola. Va en `data/experiment/controles_a2_2/cola_grafo_desarrollo_r2b_rs1_mesa.json`, con su script; la lista
  ordenada da `85707ea9…`.
- **El borrador v2 del pre-registro de A2.2** (la mesa, con estas decisiones, en el mismo archivo de `docs/`). Lo que queda para la firma
  está en su §9:
  - el alto de A-D2 (punto 1);
  - la métrica de A2.2 con el veredicto final de cada pregunta, 1 o 0, como lectura de A-D9;
  - el tamaño de la auditoría y la agregación con un voto `requiere_adjudicacion`, como los aplicó EV2 (A-D10);
  - y, para la cifra sin la cola, una pregunta con anclas dentro y fuera de ella (A-D11).
- **El borrador v9 del pre-registro de B6.3** (paquete de la mesa): el §5 y el §11, punto 6, con `MAX_MCP_OUTPUT_TOKENS` sin fijar y la
  anotación de 200.000 caracteres como tope.
- **La revisión de B6.3 por olas:**
  - el convertidor y el sello de la §265 piden las 83 filas. La mesa armó la variante por olas (`--olas 1,2` y, después, `--olas 3`),
    probada sobre olas sintéticas (19 de 19). Frena si una pregunta cuyo tipo no se sostiene está aprobada, y si cambia una fila de una
    ola ya sellada. Su instalación en la carpeta de la autora queda PREPARADA;
  - la regla, confirmada por el mandato (UPREG, §4, `:89-91` y `:102-103`): el tipo que no se sostiene es un rechazo, y el lugar pasa a la
    unidad siguiente que lo sostenga;
  - las olas 1 y 2 de la hoja son 59 de las 64 del núcleo; las otras 5 son los lugares de la ola 2 que P2 reubica, en una hoja aparte.
- **El orden:**
  - el commit del FRENO A2.1-c y del borrador, tal como llegaron;
  - después, el de esta sección, con el borrador v2 y la lista de la cola.
- Las secciones anteriores no se editan.

## 110. El domingo, a las 11:06: la versión para firmar de A2.2, los reubicados y la revisión de las olas de B6.3, y la etapa b del juez v2 (25/10/2026)

Decisiones y hechos de la autora del 25/10/2026, recibidos a las 11:06:20, con tres agregados a las 11:18:27, a las 11:24:47 y a las
11:28:44 (hoja de ruta de la mesa, §268), sobre la §267 de la mesa y los FRENOs que llegaron.

- **El instalador de la hoja por olas, el 179 y el 180,** corridos con su push: `206c3f59` (11:02:44) y `3b6f63c1` (11:02:49), por git
  log; `origin/main` en `3b6f63c1`. En la carpeta de revisión de la autora están los dos scripts por olas y su nota, con el sha256 que
  probó la mesa (`4855e4ba…`, `082111e3…` y `6ee5f631…`).
- **Las decisiones para la firma de A2.2, tal cual:**
  1. «A-D2: que cubra el alto del peor caso, con el margen del presupuesto por sesión. El alto es 85,34, y el corte duro deja de lanzar
     pasado el freno menos 1,80, así que el freno va en 87,75 y el tope en 117. El gasto esperado es mucho menor; el tope solo evita
     cortar una medición que no se repite. Si el alto y lo que cuenta el freno no miden lo mismo (por ejemplo, si uno incluye al juez y el
     otro no), aplicá la misma regla con la cuenta correcta y decime el número.»
     - **No miden lo mismo** (`tope_A2_2_firma_mesa.py`): el alto de 85,34 suma el agente y el juez, y el corte duro del banco suma solo
       las metas del agente (`banco_mcp/a2_1/correr_a2_1.py:80-87` y `:214-215`); en EV2, el juez tuvo su tope propio
       (`ev2_encadenamiento/code/runner_enc.py:28-29` y `juez_enc.py:25-27`).
     - **El agente:** 161 preguntas-corrida (las 480 sesiones de EV2 y las 3 de prueba de A-D5) por 0,42 dan 67,62; más 1,80, 69,42.
       Tope 93 y freno 69,75.
     - **El juez:** 480 respuestas por 0,0378 dan 18,14; más una respuesta, 18,18. Tope 25 y freno 18,75.
     - **En total,** 118 de tope y 88,50 de freno.
  2. «A-D9: confirmo: 1 o 0 sobre el veredicto final de cada pregunta, como en B6.3.»
  3. «A-D10: confirmo: el tamaño de la auditoría y la agregación con un voto requiere_adjudicacion, tal como los aplicó EV2.»
  4. «A-D11: (a). Una pregunta sale de la cifra sin la cola si alguna de sus anclas cae en la cola. Alineá con esto la cifra aparte del
     borrador de B6.3.»
  - Y el pedido: «Con esto, armame la versión para firmar del pre-registro de A2.2, el commit de la firma y el despacho de A2.2, para
    correrlo hoy.»
- **La versión para firmar del pre-registro de A2.2** (`docs/preregistro_A2_2_sistema_por_fragmentos.md`, `2a75f400…`) entra al repo con
  esta sección, sin ninguna decisión abierta. Su prueba es de dos colas, con α = 0,05 y Holm sobre las dos comparaciones (la primera a
  0,025), como en el N de B6.3. La firma, en el commit siguiente, cambia solo la cabecera y el pie, con el commit de esta versión y la
  fecha: PREPARADA, la corre la autora. El despacho del tramo 1 de A2.2, USD 0, queda PREPARADO; los pasos pagos los corre la autora desde
  la Terminal (§82).
- **El FRENO de P2 de los reubicados,** revisado por la mesa por código, y lo que dejó abierto:
  - **el lugar 28 de la ola 3:** las normas sobre «Régimen disciplinario a cargo del BCRA…» son `rdbcra`, que está en el inventario y
    fuera de los 128 (va al grafo corregido: §7). El lugar queda en `opecam`, como condición, como lo dejó P2;
  - **las tres citas del 2.3 de `ri_tsa`:** están en la página del PDF de su unidad y, en la E0, todas sus palabras, con las celdas de la
    tabla en otro orden (`citas_ri_tsa_pagina_y_e0_mesa.py`, con la normalización del verificador de P2). No cambia nada;
  - **los cinco criterios de lectura nuevos de los reubicados:** coherentes con los que rigen. Su control contra las olas selladas da un
    candidato por huella, el lugar 26 de la ola 2, que no cambia: su otro punto es `seggar::8.1`, del mismo documento. Si rigen lo decide
    la autora; la mesa recomienda que sí;
  - dos textos que P2 no identificó sí están entre los 128 (`apnf`, con `ri_iepsp`, e `icmecma`); según P2, no deciden ningún lugar.
- **El agregado de las 11:18:27, tal cual:** «Leí sus dos controles sobre las olas selladas y los uso en mi revisión. Ninguna ola sellada
  cambia: si algo de tu revisión toca una pregunta de las olas, decímelo y lo decido yo.» Y la regla del N: «La regla del N: «la tercera
  ola revisada» es la ola 3 de mi hoja de revisión, sellada antes de las 20:00 de hoy. Los 8 reubicados de la ola 3 y las preguntas nuevas
  de las rechazadas cuentan como cualquier reemplazo: la regla de rechazo ya existía cuando fijé la regla del N. Lo fijo ahora.»
- **La hoja de revisión de los 13 reubicados** (`fuera_del_repo/revision_b63_reubicados/`, manifiesto `0c0d93b5…`), armada por script
  desde los reubicados sellados, con su convertidor y su sello por ola de origen, probados sobre reubicados sintéticos (14 de 14).
- **La etapa b del juez v2,** revisada por la mesa por código (16 de 16):
  - los 9 casos nuevos (33 a 41) y los 11 que quedaron afuera;
  - el prompt de la iteración 2, que sin el bloque nuevo es el de la iteración 1 byte a byte;
  - las 82 fichas de la comparación, la cota de USD 14,79 bajo el freno de 35,70 y los siete puntos de su §10.
  - Su error 3 no cambia nada: los cuatro asuntos que vio (los de `9826b625` y sus tres anteriores) no traen ninguna cifra ni contenido
    de T, de B6.3 ni de los brazos, y los nombres de `git status` son rutas de archivos.
  - El comando de la iteración 2 queda PREPARADO, como el de la 1, con su tope y su freno. No corre al mismo tiempo que los pasos pagos
    de A2.2.
- **La revisión de las olas 1 a 3 de B6.3,** sellada por la autora en dos partes: las olas 1 y 2 a las 11:26:32 y la ola 3 a las
  11:28:34, antes de las 20:00, así que la tercera ola quedó revisada. Las cuentas, por código y sin leer las marcas
  (`armar_rechazadas_B63_mesa.py`): 70 aprobadas y 13 rechazadas. Por tipo, se declaran 8 de remisión, 2 de condición, 2 de definición y
  1 de dato directo; en una, el tipo no se sostiene. La lista de las rechazadas, sin los motivos, va a P2 (`insumos/`, `81e67a5b…`), con
  el «seguí» de sus preguntas nuevas, PREPARADO.
- **El borrador v10 del pre-registro de B6.3** (paquete de la mesa): la cifra aparte con la regla de A-D11, la regla de «la tercera ola
  revisada» y lo que dio la revisión. Queda abierta D-12: qué pasa si al correr B6.3 un lugar no tiene su pregunta aprobada.
- **El orden:**
  - el commit de esta sección y de la versión para firmar;
  - la firma;
  - el despacho del tramo 1 de A2.2.
- Las secciones anteriores no se editan.

## 111. El domingo, a las 11:53: A2.2 firmado y la versión para firmar del pre-registro de B6.3 (25/10/2026)

Decisiones y hechos de la autora del 25/10/2026, recibidos a las 11:53:56 (hoja de ruta de la mesa, §269), sobre la §268 de la mesa.

- **El 181 y la firma de A2.2 (el 182),** corridos con su push: `562f1c55` (11:53:05) y `a78ead7b` (11:53:13), por git log;
  `origin/main` en `a78ead7b`. El pre-registro de A2.2 quedó FIRMADO el 25/10/2026.
- **Los despachos,** pegados: el del tramo 1 de A2.2, en su sesión, y el «seguí» de P2 de los reemplazos, con los cinco criterios y sin
  los motivos de la autora.
- **Las decisiones, tal cual:**
  1. «A-D2: los dos frenos por separado, como quedaron: el agente con tope 93 y freno 69,75, y el juez con tope 25 y freno 18,75.»
  2. «Los cinco criterios de lectura de los reubicados rigen como los demás criterios de P2, y van al pre-registro de B6.3 con sus
     lugares.»
  3. «P2 no ve mis motivos de rechazo: recibe solo la lista. Si un motivo mío es una regla general, lo planteo yo como criterio de lectura
     para todas las olas.»
  4. «D-12, ninguna de las tres: B6.3 no arranca sin las 64 aprobadas del núcleo (D-1). Las preguntas de la ola 3 que no estén aprobadas
     cuando lance la primera sesión paga de B6.3 salen, declaradas por lugar, tipo y clase, y el N queda en 64 más las aprobadas de la ola
     3, con la potencia que alcanza. Nunca corre una pregunta sin revisar.»
     - **Lo que reporta la mesa:** la regla para la ola 3 choca con el mandato firmado de las preguntas, que dice «si el N no entra en el
       calendario, se recorta manteniendo las cuotas» (UPREG, §9, decisión 5, `:151`) y pone las comparaciones principales sobre la
       muestra entera tal como sale de las cuotas (§5, `:107-108`). Por eso no se escribió: la versión para firmar lleva el resto del
       punto, y para la ola 3, la regla del mandato. Cómo seguir es PENDIENTE de la autora.
  5. «La prueba del §8.1: α de 0,05 de dos colas para la familia, con Holm (0,025 la primera comparación y 0,05 la segunda), como en
     A2.2. El estadístico es la media de d_q. Son 100.000 permutaciones de signos al azar con la semilla B63:permutacion:v1, y p = (1 + las
     permutaciones con |media| mayor o igual que la observada) / 100.001. Los intervalos de cada brazo, de cada comparación y del total
     ponderado van por bootstrap percentil por pregunta, con 10.000 remuestreos y la semilla B63:bootstrap:v1. El de la hipótesis
     secundaria, de una cola, es el percentil 5. El chequeo por documento del §8.3 usa las mismas cantidades con las semillas
     B63:permutacion:documento:v1 y B63:bootstrap:documento:v1.»
  6. «Las corridas cortadas de B6.3 (error_max_turns o el presupuesto): en el análisis principal cuentan como no correctas, sin pasar por
     el juez. La sensibilidad las saca; si una pregunta queda sin corridas en un brazo, sale de esa comparación. A2.2 queda como se
     firmó.»
  7. «Las fallas de infraestructura de B6.3 (la sesión termina sin resultado por un error de la API o de la red, no por --max-turns ni por
     el presupuesto), clasificadas por código desde el tipo de error, sin leer la respuesta: se re-corren en su mismo lugar del orden,
     hasta 3 intentos en total, y si ninguno termina cuentan como no correctas. Se declaran por brazo.»
  8. «El §12: el tope se recalcula al sellar N7, con la regla de la §51, sin decisión mía, y no se recorta nada por dinero (§11, punto 8).
     Sacá «lo decide la autora antes de la firma».»
  9. «El §13: lo que llegue después de la firma (las tasas de A2.2, Q8, el N, N6, N7 y la relevancia) se llena por su regla, declarado,
     sin decidir nada nuevo. Si Q8 llega después de la firma, va como desvío declarado de Q8 (:71), con su regla de consecuencias igual.»
  10. «Los expertos (H-14 y §9.3): el envío sale apenas se selle el núcleo aprobado, y la devolución es hasta el jueves 29 a las 12:00. Se
      declara como cambio de la fecha de la §100, porque el domingo 25 el núcleo no estaba completo. El mensaje que les voy a mandar les
      pide que respondan cada uno por su cuenta y que no compartan las preguntas.»
  11. «El §3.2, el §3.3 y el §11, con los reubicados como quedaron: los documentos finales (ri_tsa y opecam); el lugar 10 de la ola 2,
      que pasó de definición a remisión del mismo documento (hoy el §3.3 dice que cada lugar conserva su subtipo); los cinco criterios
      con sus lugares; rdbcra, apnf e icmecma; y los recuentos del punto 19 con los 13.»
- **La versión para firmar del pre-registro de B6.3** (`docs/preregistro_B6_3_evaluacion_final.md`, la ruta de D-8) entra al repo con
  esta sección. Sale del borrador v10 de la mesa con 23 reemplazos (17 tramos de diff), cada uno contra su punto (§269 de la mesa).
  La firma, en el commit siguiente, cambia solo la cabecera y el pie, con el commit de esta versión y la fecha: PREPARADA, la corre la
  autora.
- **Cuándo, tal cual:** «La firma la corro antes de ver cualquier cifra de A2.2, en un momento sin nada pago corriendo y sin una ejecutora
  con una foto del repo abierta. El techo es mañana a las 12:00.»
- **El orden:**
  - el commit de esta sección y de la versión para firmar;
  - la firma.

  Los dos van sin una ejecutora con una foto del repo abierta.
- Las secciones anteriores no se editan.

## 112. El domingo, a las 12:17: la ola 3 de D-12, el plazo de la firma y el §8.3 del pre-registro de B6.3 (25/10/2026)

Decisiones de la autora del 25/10/2026, recibidas a las 12:17:36 (hoja de ruta de la mesa, §270), sobre la §269 de la mesa y lo que la
§111 dejaba PENDIENTE.

- **El punto 4 de la §111:** la autora da razón al reporte de la mesa, porque su regla para la ola 3 rompe las cuotas del mandato firmado,
  y firma con el mandato, sin enmienda.
- **Las decisiones, tal cual:**
  1. «La ola 3 en D-12 (§3.4 y §14): «Si al lanzar la primera sesión paga de B6.3 a la ola 3 le falta alguna pregunta aprobada, la ola 3
     sale entera y el N es 64, declarado. Es el recorte que mantiene las cuotas (UPREG, §9, decisión 5).» Reemplaza la frase que remite al
     mandato sin decir cómo se recorta.»
  2. «El plazo de la firma va en el §15 como desvío declarado: el mandato de las preguntas la pone antes del sábado 24/10/2026 a las 12:00
     (§1, etapa 6, :47), y el registro la movió al lunes 26 a las 12:00 (§50, punto 7, :1760).»
  3. «En el §8.3, «las 4 preguntas de cada documento cambian de signo juntas» pasa a «las preguntas de cada documento cambian de signo
     juntas»: con los reubicados hay documentos con menos de 4.»
- **La versión para firmar del pre-registro de B6.3** queda rearmada sobre la de la §111 (`b58a91b2…`) con estos tres cambios, en 6 tramos
  de diff (§270 de la mesa). Es la que entra al repo con esta sección y la §111. Sin ninguna decisión abierta.
- **El 183 y el 184 de la §269** quedan reemplazados por el 183 v2 y el 184 v2: PREPARADOS, los corre la autora con las condiciones de la
  §111.
- Las secciones anteriores no se editan.

## 113. El domingo, a las 12:48: los reubicados sellados, la iteración 2 del juez v2 y el FRENO de P2 de los reemplazos (25/10/2026)

Hechos y pedidos de la autora del 25/10/2026, recibidos a las 12:48:23 (hoja de ruta de la mesa, §271), sobre la §270 de la mesa.

- **El FRENO §270:** da bien. El 183 v2 y la firma de B6.3 (el 184 v2) los corre la autora después del FRENO A2.2-a, que no llegó:
  PENDIENTES.
- **La revisión de los 13 reubicados,** sellada por la autora con su hoja (`fuera_del_repo/revision_b63_reubicados/`, sello
  `sello_hoja_revision_B63_reubicados_olas_2_y_3.txt`, de las 12:42:43): 13 aprobadas, 0 rechazadas, y en ninguna el tipo deja de
  sostenerse. Las cuentas, por código y sin leer los motivos (§271 de la mesa).
- **La iteración 2 del juez v2,** corrida por la autora: completas 246 de 246, sin voto 0 y cruces 0, con un gasto de USD 14,7746. La
  regla de freno frena y congela la iteración 1. La mesa lo controló por código contra la enmienda 4, punto 4, leída en el commit de su
  firma (`90cce828`): 17 de 17, sin informar ninguna cifra interna.
- **La congelación de la v2** (enmienda 4, punto 5; H-17 del pre-registro de B6.3): el commit siguiente a esta sección, PREPARADO.
  - Lleva el sha256 del prompt de la iteración 1 y de su bloque de casos, y el registro de las iteraciones y el código de la v2 por su
    sha256 (87 archivos).
  - El código del análisis sobre T con su selftest, la cuarta pieza del punto 5, no está escrito: entra con su propio commit antes de la
    prueba, declarado como desvío de la letra del punto 5.
  - Si se corre así o se espera al código lo decide la autora: PENDIENTE.
- **El FRENO de P2 de los reemplazos** (`fuera_del_repo/b63_p2/FRENO_P2_reemplazos.md`, paquete `c4f12d1a…`), revisado por la mesa por
  código (31 de 31, y los trayectos contra su registro):
  - los reemplazos y su registro dan su sello, de las 12:17:06, anterior a la armada del paquete (12:18:06); el plan de tipos se selló
    antes (12:11:18);
  - los cuatro que cambiaron de documento siguen el orden de su clase, y cada documento que tomaron tenía menos de 4 lugares. Ningún
    documento pasa de 4, salvo `ri_pspapt`, con los 5 que le da el sorteo, donde no entra ningún reemplazo;
  - B63-O3-L01-R1 conserva el subtipo de la lista (remisión); el del sorteo era definición;
  - las 4 citas que no están en el texto de la E0 están en la página del PDF de su unidad. En una, a la E0 de `ri_pgn` le falta una de
    las palabras de la cita;
  - en los paquetes de las olas 2 y 3 y de los reubicados, el `salidas/paquete_*.txt` vacío es lo único que difiere, y sus manifiestos
    verifican.
- **Los tres criterios de lectura nuevos de los reemplazos:** los decide la autora (PENDIENTE). Si los aprueba después de la firma de
  B6.3, tal cual: «van como nota fechada al pie del pre-registro firmado, con su commit también después del 184 v2.»
- **La hoja de revisión de los 13 reemplazos** (`fuera_del_repo/revision_b63_reemplazos/`, manifiesto `e97dba00…`), armada por script
  desde los reemplazos sellados, con su convertidor y su sello por ola, probados sobre reemplazos sintéticos (15 de 15).
- **El núcleo aprobado para el material de los expertos:** el armador de las 64 aprobadas de las olas 1 y 2, con su sello, probado sobre
  datos sintéticos (14 de 14). Está PREPARADO para correr apenas la autora selle su revisión de los reemplazos del núcleo. El material de
  los expertos pasa a su v2, que toma la E0 del grafo evaluado: la de la §256 la buscaba donde no están los documentos de la tanda 0.
- **El orden:**
  - el 183 v2 y el 184 v2;
  - el commit de esta sección;
  - la congelación.
- Las secciones anteriores no se editan.
