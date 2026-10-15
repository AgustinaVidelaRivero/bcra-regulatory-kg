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
