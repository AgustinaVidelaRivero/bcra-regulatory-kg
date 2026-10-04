# U-DIAG-VINCULO — reporte (FRENO V2)

**Condiciones de la corrida.** USD 0, sin API ni Neo4j, solo lectura.
- Mandato firmado en `8744a5c`. El FRENO V1 está en `freno_v1.md` y fue revisado por la autora (04/10/2026).
- HEAD al cierre: `395fc0b`.
- Corridas sobre una copia copiada en el scratchpad (regla l).
- Detalle, fuentes firmadas con sha, bases de costo y comandos: `anexo_u_diag_vinculo.md` (anexo).
- Salidas en `salidas/`. Las reglas de detección, derivación y lectura están en `regla_deteccion.md` (sha
  `f912176c…`), escrito antes de contar y de sortear.

## 1. Tarea 1, el ejemplo: ninguna arista

- **Grafo y unidades.** KG-Tanda0-Desarrollo-r2a (sha `93a7af72…` verificado, `f8dedd4`).
  - `cla::5.1.1::intro` tiene 1 nodo de contenido: Definicion «Cartera comercial — alcance».
  - `cla::5.1.1.1` tiene 4: Definicion de la contraexcepción, 2 Condicion y Operacion.
- **Aristas entre ellos: 0.** El único camino tiene 2 saltos y pasa por el TextoOrdenado de cla
  (`establecida_en`; ese nodo tiene procedencia en 143 unidades). Sin TextoOrdenado ni Sujeto, no hay camino
  (`salidas/tarea1_ejemplo.txt`).

## 2. Tarea 2: qué cubre el prefijo nuevo y los dos faltantes del ejemplo

Leí el prefijo r2b congelado en `20b7f60`, con los ajustes del FRENO P1.
- R8: la Condicion de un ítem cuya norma está en otra unidad se emite «sin condicion_de»
  (`prompt_r2b_reemplazos.json:60-63`).
- R30, composición con el encabezado: `:114-117`.
- R16, regla 1: `:120`.
- La regla 3 del prefijo sellado sigue diciendo «Las relations son SOLO entre entidades del MISMO chunk»
  (`prompt_e1.py:133`).

**Faltante A, la relación entre el encabezado de 5.1.1 y el 5.1.1.1.**
- El prefijo no puede crearla. Por la regla 3, E1 no relaciona fuera del chunk, y R8 deja la Condicion del
  ítem sin `condicion_de` a propósito.
- Lo que R30 sí aporta: el ítem compone el contenido del encabezado, así que leído solo ya dice la excepción.
- Queda para el ensamblado toda la arista, o el límite declarado (§4).

**Faltante B, el nodo de la excepción principal** (los créditos para consumo o vivienda, fuera de la cartera
comercial).
- En r2a no existe. El crudo `v3_b54` del 5.1.1.1 trae solo la contraexcepción
  (`corpus_tanda0/salida_dirigida/cla/extracciones_e1.jsonl:61`), y E3 dio `completo_ok` (`veredictos.jsonl:66`).
- La causa: `v3_b54` prohibía extraer del bloque heredado (`prompt_e1.py@20b7f60:52`, `:122`), y la línea de título «Los créditos para consumo o
  vivienda.» solo nombra la clase.
- R30 lo puede resolver: el mensaje r2b del 5.1.1.1 avisa que el último bloque abre la lista y manda componer
  (`request_cla__5.1.1.1.json@20b7f60:897`). La rama CONTENIDOS cubre «los miembros de una clase que el
  encabezado nombra».
- Pero R30 no nombra las listas de excepciones. Qué rama toma el modelo, y si el nodo sale como Excepcion o
  como Definicion, NO es DECIDIBLE sin correrlo. Lo muestra P4 en `cla::5.1.1.1`, que es caso fijo.
- El ensamblado no puede crear ese nodo, porque no crea contenido.
- E3 r2b no lo reclamaría: excluye el «contenido de otras unidades» (`prompt_e3.py@20b7f60:85`), y su NOTA
  nueva es solo para la unidad del encabezado (`:242-248`).

## 3. Tarea 3: censo (regla declarada antes de contar; `salidas/censo_anuncios.txt`)

| | párrafos candidatos | no anuncian (en línea) | anuncian sin hijos | contenedores / pares | excepción | c1 | c2 | alcance | enumeración |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| tanda 0 (2.434 unidades) | 301 | 80 (5) | 0 | 221 / 1.096 | 18 / 96 | 64 / 295 | 19 / 102 | 21 / 112 | 99 / 491 |
| partición (9.324) | 1.377 | 727 (31) | 13 | 637 / 2.864 | 19 / 80 | 78 / 293 | 32 / 164 | 82 / 443 | 426 / 1.884 |

- **Qué es c1 y qué es c2.**
  - c1: los ítems son los supuestos («siempre que…», «en los siguientes casos:»).
  - c2: el encabezado condiciona a los ítems. R30 ya resuelve este caso dentro del ítem.
- **Controles.**
  - `cla::5.1.1::intro` sale como excepción, con hijos 5.1.1.1 y 5.1.1.2.
  - La E0 e0-r2 da lo mismo que la legada en la tanda 0.
  - Los 212 intro y chapeau con «:» coinciden en número con los 212 encabezados del diseño del prefijo
    (`diseno_prefijo_r2.md@fca019d:1075`); no comparé los dos conjuntos.
- **Muestra de 10** (citada en `censo_anuncios.txt`, leída en el anexo §3).
  - El anuncio y los hijos están bien detectados en 10 de 10.
  - El tipo léxico está bien en 5, dudoso en 1 y mal en 4.
  - Los conteos por tipo son indicativos, no medidos.

## 4. Tarea 4: direcciones (tabla completa en el anexo §6)

- **(a-T), predicado tipado de la matriz, derivado en el ensamblado.**
  - En KG-Tanda0-Diez-r2a, con la regla de destino único, deriva 35 aristas en 23 pares: 22 de ext y 1 de
    ctacte (112 si se aceptan todos los destinos).
  - No cubre el ejemplo: ningún predicado tipado llega a una Definicion.
  - No cambia el esquema ni E1, y cuesta USD 0.
  - Pide enmienda a L-ESQ-R2, porque predicados que hoy emite solo E1 tendrían instancias derivadas, marcadas
    como `establecida_en` (`ensamblar_tanda0.py@395fc0b:592-608`) y sin `no_verificada_e3`.
- **(a-R), `remite_a` derivada de la estructura.**
  - Deriva 6.630 aristas en 1.056 pares (KG-Tanda0-Diez-r2a tiene 14.000 `remite_a`), y cubre el ejemplo: 4
    aristas al 5.1.1.1.
  - Se declara como `remite_a` (enmienda 2, §3 y §4, `5f9a731`): `evidencia` = la cláusula anunciadora literal
    de E0, procedencia del contenedor, sin `rol_fuente` ni `no_verificada_e3`, y la forma en el registro de
    remisiones.
  - Pide enmienda a la enmienda 2, §1 y §4: una nota no alcanza, porque cambia lo que el predicado afirma.
- **(b), referencia del extractor por punto y tipo.** Cambia el prompt y el tool schema (`target` es un
  `local_id`, `tool_schema_r2.json@20b7f60:550`), además del validador, E3 y la resolución. Reabre P2 y P4.
  No es viable antes del escalado.
- **(c), pasada de modelo sobre pares.** USD 1,09 a 3,07 en la tanda 0 y 1,04 a 8,02 en la partición, con
  tokens SUPUESTOS, más la verificación y la calibración. Es una etapa nueva y sigue limitada por la matriz.
  No es viable antes del escalado.
- **Otras.** (d) navegación en A1.8, que no toca el grafo y es complemento; (e) límite declarado.
- **Contenedor tipado como Definicion** (anexo §4).
  - O1, `remite_a` con `alcance = interna`: enmienda a la enmienda 2.
  - O2, un valor de `alcance` propio: enmienda al §3. Contradice su regla, «el alcance se decide comparando
    textos ordenados» (`5f9a731:84`); no la recomiendo.
  - O3, no unirlos y declararlo.
  - O4, un predicado Excepcion → Definicion: cambia la matriz, queda excluida.
  - O5, que E1 tipe el contenedor de otro modo: cambia el prompt.
  - **Si ampliar lo que afirma `remite_a` es cambio de esquema:** según la letra de la decisión 1, no, porque
    los tipos, los predicados y las 56 firmas no cambian. Sí cambia la definición firmada de un predicado del
    esquema final. Si la autora lo cuenta como cambio de esquema, O1 queda excluida y queda O3.
- **Precisión de (a)** (lectura asistida, regla fijada antes del sorteo; `salidas/lectura_precision.md`).
  - (a-T): 13 de 23 aristas correctas, Wilson [0,368; 0,744], y 12 de 15 pares. Las 10 incorrectas son de
    `ext::3.16.3::intro`: hijos por número que no son ítems de la lista anunciada.
  - (a-R): 45 de 76, Wilson [0,480; 0,696]. El anuncio está bien atribuido en 14 de 15 pares. Las 31
    incorrectas se reparten en 20 por un hijo no anunciado, 8 por un origen que no hace el anuncio (la regla
    D1 atribuye la cita a todos los nodos) y 3 por un destino que repite el encabezado.
  - Ninguna llega al piso de Wilson 0,75 del criterio de L-ESQ-R2 §6.3 (`4ef7650:788-789`).
  - Tienen arreglo candidato en código, NO MEDIDO: el origen por `tramo`, que r2b exige en toda entidad
    (`tool_schema_r2.json@20b7f60:51-55`); un filtro de hijos; y el segundo segmento del `tramo` en el destino.

## 5. Tarea 5: recomendación

(a-R) en código del ensamblado sobre la salida de U-REEXT-T0, con origen por `tramo` y filtro de hijos; no toca
E1 ni P4. Entra antes de la tanda 1 solo con la enmienda a la enmienda 2 firmada y 30 aristas leídas con piso
de Wilson 0,75; si no, O3: el vínculo del ejemplo queda como límite declarado. (a-T): no; no cubre el ejemplo.

## 6. Controles y errores propios

Los resultados de los controles al cierre están en el FRENO V2 y en el paquete de revisión.
- **Error propio, ancla de V1.** V1 citó `tool_schema_r2.json@HEAD:538`. El «HEAD» era `966c2bc`; desde
  `20b7f60`, esa línea es la `:550`, con el mismo texto. La causa: una ancla relativa a HEAD mientras otra
  unidad commiteaba. Lo dejé como nota fechada al pie de `freno_v1.md`.
- **Error propio, ancla del anexo.** En el borrador del anexo escribí `:870-873` para la llamada a
  `REF.detectar_y_resolver`; la línea es `:881`, y la corregí antes de entregar.
- **Ancla de la regla.** `regla_deteccion.md` cita `modelos_r2.py@HEAD`, donde HEAD era `395fc0b`; esas líneas
  no cambiaron. No la edito, para no mover su sha.
