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
