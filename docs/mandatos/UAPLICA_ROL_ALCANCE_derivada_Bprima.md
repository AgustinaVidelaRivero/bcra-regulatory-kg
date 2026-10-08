# Mandato U-APLICA-ROL-ALCANCE — `aplica_a` derivada hacia el alcance del documento, solo si la norma no nombra otro sujeto (B′, BKL-0040)

**FIRMADO por la autora el 08/10/2026** (firma por mensaje de la autora; versión para firmar en `08ccdfa`; redactado por la mesa el 08/10/2026,
por decisión de la autora del mismo día sobre el
barrido de los límites declarados, fila ENS-07, grupo 2 (paquete de la mesa
`hoja_de_ruta_tanda1_mesa/barrido_limites_declarados_0810_mesa.md`, §3, fuera del repo); asentada en el plan, fila B6.3, nota del
08/10/2026). No va antes de la tanda 1 (`BKL-0040`: «No frena la tanda 1»): corre en paralelo con el escalado, como
corrección del ensamblado. Si pasa su piso, se aplica a todas las tandas en el próximo armado, antes de sellar el grafo evaluado (el de
B6.3, `docs/protocolo_dos_grafos.md`, §2). USD 0, sin API. «B′» nombra acá el rediseño de la parte B de la enmienda 6; no es el «mecanismo
B′» del gate de CQN2 (`docs/casos_gate_cqn2.md:355`).

DE DÓNDE SALE.
- **La parte B de la enmienda 6 a L-ESQ-R2 no se adoptó.** Derivaba `aplica_a` hacia el rol de alcance para toda norma (Obligacion,
  Restriccion, Potestad) de un documento con alcance sin relación de sujeto con mención verificada (§B.1, `:196-197`; texto firmado en
  `0737497`, sha256 `ddccd7af…`, igual al del árbol). Población: 1.592 de 3.603 normas de unidades aceptadas, 1.362 sin ninguna `aplica_a`
  y 230 con una que no verifica (`:227-229`). Su lectura (R2-1 de U-RERESOL-CAT, 30 fichas, semilla 20261006) dio 18 correctas, 5
  incorrectas y 7 dudosas: Wilson al 95 % 0,42 a 0,76, bajo el piso de 28 de 30 (`:3-5`, `:231`).
- **El rediseño está en el backlog.** `BKL-0040` (`data/backlog/backlog.jsonl:93`): derivar el rol solo cuando la norma no nombra otro
  sujeto, ni en la mención del modelo ni, por léxico de labels y alias del catálogo, en su texto. Condición de cierre: una lectura de 30
  sobre la población de B′ con Wilson inferior ≥ 0,75 (28 de 30), adjudicada por la autora, o la decisión de la autora de declararlo
  límite definitivo. Origen: decisión 4 de la firma de la enmienda 6 (`:9-11`) y nota del 06/10/2026 del mandato de U-RERESOL-CAT
  (`docs/mandatos/URERESOL_CAT_reresolucion_catalogo.md:258-262`).
- **La pre-medición ya existe, sin lectura.** R2-2 de U-RERESOL-CAT
  (`data/experiment/reresolucion_catalogo/salidas/r2_2_premedicion_b_prima.json`, `a079275`, sha256 `6ef1d536…`): de las 1.362 normas sin
  `aplica_a` de los nueve documentos con alcance de la tanda 0, 986 nombran otro Sujeto en el texto propio o heredado de su unidad (968
  sin contar la raíz del catálogo; 946 fuera de los miembros del rol), y B′ daría el rol a 376. «Palabra entera» está implementada como
  «rodeada de espacios»; con límite de palabra (`\b`), 1.056 y 306 (`URERESOL_CAT_reresolucion_catalogo.md:291-293`, `:313-316`).
- **Recomputado por la mesa al redactar** (copia sin enlaces, USD 0; script y salida en el paquete de la mesa, fuera del repo; NO
  VERIFICADO en el repo hasta B1): 376 y 306 se reproducen. Con `\b`, 1.043 sin la raíz y 1.015 fuera de los miembros (B′ daría 319 y
  347). Las 306, por TO: cap 113, ctacte 112, ext 37, polcre 14, ric 12, lingob 8, cla 7, pagjub 3, pro 0; por tipo: Obligacion 163,
  Restriccion 112, Potestad 31.
- **Lo que NO cuenta como evidencia.** Las 5 incorrectas de la parte B eran normas cuyo texto nombra a otro sujeto (`BKL-0040`, campo
  `causa`). Esa observación motivó B′, pero es posterior al resultado: B′ se mide desde cero, con semilla nueva. De las 30 fichas de la
  parte B, 7 caen en el marco de B′ (6 con `\b`; cuenta de la mesa, solo por ids): se excluyen del sorteo.

QUÉ TOCA.
- **Documentos con un destino único.** La entrada del documento en `rol_por_to` (tabla de la release, o registro de alcance por tanda
  leído al ensamblar, fila F13c) tiene `rol_id`: un rol, o la clase cuando es una sola
  (`reresolucion_catalogo/reresolver_catalogo.py:229`). Con dos clases, `rol_id` es nulo y no hay destino único (enmienda 6, §B.4,
  `:248-249`): ri2_ci en la release; snp_cheq y nmcief en el registro. Los documentos sin alcance siguen con la parte A.
- **Tanda 0:** los nueve TOs con alcance (todos salvo docvig), seis con rol y tres con clase (ctacte → `Sujeto_banco`; lingob y polcre →
  `Sujeto_entidad_financiera`).
- **Tanda 1** (ejemplo del §7 del protocolo entre tandas, `docs/protocolo_entre_tandas.md:282-284`, con ri_pgn en lugar de ri_cc; la lista
  real sale de U-SEG-OFICIAL): 15 de 20 documentos. Ocho por la tabla de la release: cinco con clase (ayccef, expaef, opefci, lingeef,
  cajasc) y tres con rol (adrei, depaho, efemin). Siete por el registro: tres con clase (ri_ccna, ri_dcpc, manori) y cuatro con rol
  reutilizado (ri_rml, ri_gerc, ri_pgn, snp_tr). Fuera: snp_cheq y nmcief (dos clases); ri_oc, ceninf y cirmo3 (sin alcance declarado).
  Fuentes: `catalogo_unico/generados_r2/rol_por_to_r2.json` (sha256 `07cdb7af…`; 71 entradas: 35 con rol, 35 con clase, 1 con dos clases)
  y `catalogo_unico/registro_alcance_por_tanda.md:16-35` (sha256 `ce402aad…`).
- **La tanda 1 no lo necesita para extraerse:** es código sobre lo guardado. Pero B2 mide solo documentos con alcance de la release; los
  siete con alcance por el registro, decidido por la lectura de un pasaje, no entran en la muestra (decisión 4).

LA REGLA. Se fija por escrito en B1 y se sella (sha256 y hora), con el código que la implementa y la mide, antes de cualquier cuenta.
Propuesta de la mesa, para que B1 la precise contra el código:
- solo normas (Obligacion, Restriccion, Potestad) de un documento con destino único y sin ninguna `aplica_a` saliente. Las 230 que ya
  tienen una `aplica_a` con una mención que no verifica quedan fuera: tienen sujeto por R4, con su marca, y `BKL-0040` no deriva cuando
  la mención del modelo nombra a alguien;
- la norma «nombra otro sujeto» si el texto propio o heredado de su unidad, normalizado como `r1_comun.norm`, contiene con límite de
  palabra una clave no ambigua del índice de E4, de criterio `label_exacto`, `alias_exacto` o `label_singularizado`, de un Sujeto distinto
  del destino. Es el criterio de R2-2 (`reresolucion_catalogo/r2_2_medicion.py:153-205`), con `\b` en lugar de espacios y con la raíz y
  los miembros según la decisión 1;
- si no nombra otro sujeto: arista `aplica_a` derivada hacia el destino, con `rol_fuente` y `metodo_resolucion` iguales a
  `derivada_de_alcance`, la procedencia de la norma, sin mención y sin las marcas de E3. Todo va al registro
  `aplica_a_derivada_de_alcance.jsonl`: la norma y el destino y, para las que no la reciben, la clave y el Sujeto que la bloquearon;
- `ejecuta`, Excepcion y Operacion quedan fuera (§B.1, punto 4, y §B.4);
- solo en el ensamblado y en la fase r2b, como la parte A (`tanda0/code/ensamblar_tanda0.py:1278`); r1 y r2a no cambian. Los artefactos
  por TO del runner (`grafo_r2_<to>.json`) no la llevan, declarado.

ETAPAS.
- **B1. La regla y su pre-medición, sin leer** (sobre una copia).
  - El texto de la regla con sus listas cerradas, en `data/experiment/aplica_rol_alcance/regla_b1.md`, sellado con su código.
  - Pre-medición en `a9631a64` (diez), `e22fae1a` (sin cola diez) y los dos de desarrollo (`6e756043`, `2922b72d`): por TO y por tipo de
    norma, cuántas normas reciben la derivada, cuántas bloquea cada Sujeto (las diez claves más frecuentes) y cuántas quedan fuera por
    destino no único.
  - Unidad de conteo: nodos del grafo. La mesa cuenta 1.358 normas sin `aplica_a` en `a9631a64` (1.296 en `e22fae1a`) contra las 1.362 de
    R2-2, que cuenta normas del crudo; B1 concilia las dos cifras, con la lista de las diferencias.
  - Cuántas del marco estaban entre las 30 fichas de la parte B, solo por ids y sin abrir sus veredictos: se excluyen del sorteo.
  - Control: ninguna derivada en un documento sin alcance ni en uno con dos clases.
  - FRENO B1: la autora aprueba el texto de la regla.
- **B2. La medición.**
  - Muestra de 30 del marco en `a9631a64`, sin las fichas de la parte B. Semilla nueva, distinta de toda semilla ya usada en el repo
    (entre ellas 20261006, 20261007 y 20261008), fijada y sellada antes de sortear; lista sellada antes de leer.
  - Fichas sin veredicto: la norma (tipo, label, descripción, tramo), el texto de su unidad y el heredado, y el destino con su label y sus
    miembros.
  - Criterio de «correcta», sellado antes de leer: el destino es a quien se aplica esa norma según el texto de la unidad y su heredado (el
    de la parte B, §B.2, `:216-217`). Las no decidibles se declaran y cuentan como no correctas.
  - Lectura en tres pasos, cada una sellada antes de comparar: primera, de una sesión aparte que no diseñó la regla (FRENO B2-a, sin la
    cifra); segunda, a ciegas, de la mesa; adjudicación de la autora de las divergencias.
  - Piso: 28 correctas de 30 (Wilson inferior al 95 %: 0,787 con 28; 0,744 con 27). El piso de L-ESQ-R2 §6.3, como en U-UNION-ESTRECHA.
  - FRENO B2 con la cifra, por TO y por tipo.
- **B3. Si pasa: la implementación** en el ensamblado (fila F15d de la tabla de reprocesamiento, solo código sobre lo guardado).
  - Selftest con casos por rama: rol, clase única, dos clases, sin alcance, norma con `aplica_a`, norma que nombra otro sujeto, raíz,
    miembro del rol y `ejecuta`.
  - Diff de los cuatro grafos r2b armados con el código de la base de B3 y con el código nuevo. No se compara contra los sha sellados: el
    código de HEAD ya da `40c54830…` y `8d747e57…` en diez y sin cola diez (`reresolucion_catalogo/freno_r2_3bis.md:14-15`). Salen la
    lista exacta de aristas nuevas y ninguna otra diferencia; `resolucion_sujetos.jsonl` y `no_mapeados_sujetos.jsonl`, byte a byte; r2a,
    `70d51e42…` y `fa4c1043…` byte a byte.
  - Shapes, perfil r2 y fase r2b: bloqueantes en PASS, con el cambio declarado de la cuenta de normas sin `aplica_a` (§B.3).
  - Suite: 0 regresiones no declaradas, con LN-3 según la decisión 2.
  - Selftest de claves OK, sin claves movidas.
  - Nota en F15d, y las anclas de la tabla que corran, en cualquier fila, corregidas (precedente: R2-3 de U-RERESOL-CAT).
  - Entra en el próximo armado de todas las tandas, antes de sellar el grafo evaluado.
- **Si B2 no pasa:** el límite queda declarado con las dos cifras (parte B y B′), `BKL-0040` se cierra como límite definitivo si la autora
  lo decide, y la unidad cierra en B2.

CRITERIOS DE ACEPTACIÓN. Cada uno con su comando y su salida:
- la regla sellada antes de la primera cuenta (sha256 y hora, y los mtimes de las salidas, posteriores);
- el criterio, la semilla y la lista, sellados antes de leer;
- las tres lecturas selladas antes de comparar;
- doble corrida de la pre-medición y, en B3, de las cadenas, byte a byte;
- en B3, que `kg.json` cambie solo por las aristas de la regla y que los registros de sujetos queden iguales;
- `selftest_r3`, `selftest_regression_kg` (si se toca la suite) y `selftest_clave_cache --salida-r2b`, en verde;
- sha256 del repo antes y después de cada corrida;
- 2.213 `.pyc`;
- grep de convenciones (nombres de personas, referencias a mensajes o correos), pegado aunque dé vacío.

ESCRITURAS:
- `data/experiment/aplica_rol_alcance/` (se crea) y el scratchpad;
- en B3, además: `data/experiment/tanda0/code/ensamblar_tanda0.py` (la derivada, solo r2b), `data/experiment/r2_codigo/selftest_r3.py`
  (casos nuevos), la nota de F15d y las anclas que corran en `data/experiment/mantenimiento/tabla_reprocesamiento.md`; con la decisión 2
  (a), `scripts/regression_kg.py` (solo LN-3) y `scripts/selftest_regression_kg.py`.

PROHIBIDO: el prefijo y el mensaje de E1, E3, los validadores (`validador_e1`, `validador_r2`), `modelos_r2.py` (salvo la decisión 3), el
catálogo y sus generados, `rol_por_to_r2.json`, el registro de alcance (solo se lee), `runner_corpus.py`, los grafos sellados y sus
registros, la fixture, `grafos.py`, la API, commitear. Tampoco se abren los veredictos de la lectura de la parte B
(`reresolucion_catalogo/salidas/r2_1_lectura_parte_b.json` y la segunda lectura de la mesa): de sus fichas, solo los ids.

REQUISITOS: CLAUDE.md §4 (a a l). Por la regla l, las corridas y los selftests van sobre una copia sin enlaces, con el sha256 del repo
antes y después.

CONVIVENCIA:
- B1 y B2 son de solo lectura sobre lo guardado: pueden correr en cualquier momento después de la firma.
- B3 toca `ensamblar_tanda0.py`, igual que U-OMISIONES-COD (BORRADOR v5 de la mesa, fuera del repo) y U3 de U-UNION-ESTRECHA. Va después
  de las dos y antes de la fusión de U-CASI-DUPLICADOS, que re-apunta todas las aristas. Orden en la cadena: G-r, U3, B3, fusión.
- El grupo B (f) de U-OMISIONES-COD (contracciones en `verificar_tramo`) cambia la verificación de 51 menciones. No cambia la población de
  B′, que son las normas sin ninguna `aplica_a`.
- La marca tiene que llegar al agente y a la exportación: lo diseña U-NAV-DISENO (BORRADOR,
  `docs/mandatos/UNAV_DISENO_navegacion_agente.md:148-154`).
- No entra al re-sellado único de la tanda 0 previo a la tanda 1: entra en el armado que precede al sello del grafo evaluado.

DECISIONES DE LA AUTORA AL FIRMAR, con la recomendación de la mesa:
1. **Tres puntos de la regla** (cifras sobre las 1.362; NO VERIFICADAS en el repo hasta B1).
   - (a) Límite de palabra o espacios. **Recomendación: `\b`.** Es la «palabra entera» que pide la regla; con espacios se pierden las
     claves seguidas de puntuación (986 contra 1.056 que nombran otro sujeto).
   - (b) La raíz del catálogo (`Sujeto_sujeto`, «sujeto(s)»). **Recomendación: no cuenta.** La palabra aparece en «sujetos obligados», que
     es la expresión colectiva de R3 y nombra el rol (`r1_e4.py:306`), y en «sujeto a», donde no nombra a nadie. Con `\b`, B′ pasa de 306
     a 319.
   - (c) Los miembros del rol. **Recomendación: cuentan como otro sujeto.** Una norma que nombra a un miembro (las entidades financieras,
     en un rol que incluye también a las cambiarias) se aplica a ese miembro, no al rol entero. Excluirlos daría 347.
2. **LN-3 de la suite.** La derivada no lleva mención, y LN-3 exige mención en toda arista de sujeto fuera del esqueleto
   (`scripts/regression_kg.py:1747-1771`; «resuelto» en `a9631a64`, 2.616 de 2.616). Opciones: (a) LN-3 cuenta las derivadas aparte, con
   su marca, como ya hace con las del esqueleto; (b) declarar la regresión de LN-3; (c) ponerles mención, que sería falsa.
   **Recomendación: (a).** La fila 65 del tablero de correcciones cuenta igual que LN-3 ([c12], `docs/tablero_correcciones.md:165-166`):
   su texto lo pone al día la mesa, fuera de esta unidad.
3. **`modelos_r2.py`.** `AristaR2` acepta el `rol_fuente` nuevo como texto libre (`pyd_r2/code/modelos_r2.py:632`); los invariantes de
   `:650-659` corren solo para `derivada_de_procedencia`. Opciones: (a) no se toca y el selftest controla las marcas; (b) invariantes para
   las derivadas nuevas. **Recomendación: (a), decidida junto con U3 de U-UNION-ESTRECHA**, que tiene la misma pregunta abierta; si es
   (b), un solo cambio para las dos.
4. **Control en la tanda 1 antes de sellar el grafo evaluado.** **Recomendación: sí**, como el de U-UNION-ESTRECHA (plan, fila B6.3,
   `docs/plan_tesis.md:783`): una muestra de las derivadas en los TOs de la tanda 1, separada por el origen del alcance (registro o
   release), con el criterio de B2. Tamaño, semilla y piso, sellados antes de leer.

**Decididas al firmar (08/10/2026):**
1. La regla: **`\b`**; **la raíz del catálogo no cuenta**; **los miembros del rol cuentan como otro sujeto.**
2. **(a)**: LN-3 de la suite cuenta las derivadas aparte, con su marca.
3. **(b)**, no la recomendación de la mesa: el código valida `rol_fuente` como valor cerrado, con invariantes para las aristas
   derivadas. Motivo: los valores cerrados se controlan por código (`docs/registro_reunion_mentores_2026-09-30.md`, puntos técnicos,
   punto 2), y con dos tipos nuevos de derivadas (esta y la unión de ítems de U-UNION-ESTRECHA) un error en la marca pasaría sin
   control. **Un solo cambio para B3 y para U3 de U-UNION-ESTRECHA**: lo hace la primera de las dos que llegue a implementar, con los
   valores de las dos, y la otra lo usa. `pyd_r2/code/modelos_r2.py` (`AristaR2.rol_fuente` como valor cerrado, `:632`, y los
   invariantes de `:650-659` extendidos a cada derivada) y su selftest entran en las ESCRITURAS de esa etapa; antes de cambiarlo, la
   etapa mide que ninguna salida guardada (E1, ensamblados r2b de la tanda 0) cambie de validez, con la fila de la tabla de
   reprocesamiento que corresponda y el selftest de claves sin claves movidas.
4. **Sí**: control en la tanda 1 antes de sellar el grafo evaluado, separado por el origen del alcance.

## Firma

FIRMADO por la autora el 08/10/2026 (versión para firmar en `08ccdfa`), con sus cuatro decisiones. Rige desde esta firma: B1 puede
empezar.
