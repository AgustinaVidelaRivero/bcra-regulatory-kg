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
