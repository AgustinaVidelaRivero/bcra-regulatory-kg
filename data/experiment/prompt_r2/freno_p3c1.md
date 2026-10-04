# U-PROMPT-R2 — FRENO P3c-1 (diseño)

04/10/2026. HEAD `2a857db` al empezar y `bd77541` al cerrar: durante la etapa la autora commiteó P4 (`2ed47a0`, con
la revisión a a d de la lectura) y sus decisiones (`bd77541`). USD 0, sin API y sin commit. Nada congelado ni implementado. El
detalle, con sus anclas, está en `p3c/diseno_p3c.md`; las salidas, en `p3c/salida/`.

**Fuentes.**
- **La etapa:** la nota del 04/10/2026 al pie del mandato (`docs/mandatos/UPROMPT_R2_prefijo_nuevo.md:695-747`,
  `bd77541`). Coincide con el pedido de la autora: puntos a a e, que la nota numera 1 a 5, y los agregados
  f, g y h.
- **El agregado a P3c-1 del 04/10/2026** (de la revisión del FRENO P4) está en una nota nueva del mandato
  (`:748-775`, en el árbol sin commit). Trae:
  - el encabezado puro de una lista;
  - cuatro casos de control;
  - el criterio de `cap::5.4.4` en los dos brazos;
  - el tercer escalón del reintento por corte.

## 1. La revisión de la lectura de P4, asentada

`p4/lectura_p4.md` queda como «revisada por la autora el 04/10/2026». Las correcciones a, a′, b y c están aplicadas
en sus secciones, y la sección «Revisión de la autora» las resume con el conteo de d.

**a. `cap::5.4.4`.** Su D6 pasa a «no emite» (`p4/marcas_p4.py`). Sola, no cambia la tabla: D6 sigue en 3/6 y 5/6.

**a′. El mismo criterio en los dos brazos.** Las seis `condicion_de` del sellado que su validador rechaza por la firma
pasan de «cumple» a «no emite»: `cap::2.5.7`, `cla::5.1.1.1`, `ctacte::5.1.2.2`, `ext::10.2.5`, `ext::3.3.3.3` y
`ext::3.5.6.9`.
- **La tabla pareada, regenerada dos veces sobre una copia:** D5 queda sin pares firmes en todos los grupos.
  - En los sorteados, de 1/1 y 1/1 a 0.
  - En los fijos, de 1/1 y 1/1 a 0.
  - En las listas, de 2/2 y 1/2 a 0.
  - Las demás dimensiones no cambian.
- **El brazo nuevo solo:** cumple en 5 de las 7 fichas en que emite la relación.
- **Archivos:** `p4/salida/marcas_lectura_p4.json` y `tabla_pareada_p4.json`, actualizados.
- **`freno_p4.md` no lo toqué:** su línea de D5 queda superada por la lectura revisada.

**b y c.** La fila de D5 de `cla::5.1.1.1` se corrigió: el monto está en el umbral de e2, y e2 funde dos condiciones.
En `cla::5.1.1::intro` quedan anotadas la Definicion de alcance perdida y la frase, que es normativa.

**d. Las 24 omisiones `meta_normativo` del nuevo,** una por ficha (`p3c/salida/insumos_p4_p3c.json`):

| Dónde está el tramo | Omisiones | Normativas |
|---|---|---|
| Texto propio | 16 | 8, las que confirmó la autora |
| Texto heredado | 6 | 1 (`ext::13.4.8`) |
| Cruza del título al cuerpo | 1 | 0 |
| No verifica | 1 | 0 |
| **Total** | **24** | **9** |

## 2. El texto nuevo

**Prefijo.** Son 15 reemplazos con ancla única sobre `3817de475c93`, reversibles byte a byte. Lado a lado en
`p3c/salida/lado_a_lado_p3c.md`.
- **Tamaño:** de 55.105 a 59.909 caracteres.
- **Hash del borrador:** `322c5a23e9b7`; el tool schema no cambia.

| Punto | Qué agrega |
|---|---|
| a, `meta_normativo` | Regla 9 sin «el alcance jurídico»; de la vigencia, solo la fecha. Una prueba antes de registrar: nunca deber, prohibición, facultad, condición, excepción, alcance ni modalidad; el alcance de una clase es Definicion; si no hay tipo, `fuera_de_tipos`. Una prueba entre finalidad y alcance: si quitar la frase hace que la norma valga para más casos, es alcance. Definicion: lo que una clase abarca o deja afuera sí la define |
| a, el encabezado puro (agregado 1) | La única excepción a «extraelo con su tipo»: lo que un encabezado de lista fija para cada ítem se extrae en el ítem, y en la unidad del encabezado no se extrae ni se registra; no es `meta_normativo` ni `fuera_de_tipos` (P3C-a3 y P3C-a6) |
| b, listas que exceptúan | Dos tipos. Lo que queda afuera: Excepcion, con la contra-excepción como POLARIDAD (la Operacion de clasificar y una Condicion por condición). Las condiciones de una sola excepción: Condicion con su cuantificador. En los dos tipos, la descripción nombra la norma exceptuada, y no hay `exceptua` si esa norma está en otra unidad. La unidad del encabezado extrae la norma y su excepción, o la Definicion de la clase |
| c, un nodo por condición | Una Condicion por supuesto; label, descripción, tramo y umbrales del mismo supuesto |
| d, la norma del encabezado | No se emite como entidad aparte en el ítem; ninguna relación a un `local_id` no emitido |
| e, sin mención inventada | Si ni la unidad ni el heredado nombran al sujeto, no hay relación; el colectivo del TO va solo con la expresión copiada del texto |

**Los cuatro casos de control del agregado** (diseño, §1). Los cuatro ya están en la no-filtración, porque son
unidades de P4.
- **`ayccef::2.4.8.1` y `ayccef::4.2.7.2`:** con el texto nuevo serían la Obligacion compuesta y la Condicion
  compuesta, sin omisión.
- **`cap::3.1.14::intro` y `ric::3.1.8`:** con la prueba entre finalidad y alcance, sus frases son alcance y van en
  la descripción de su norma. Es mi lectura; la decide la autora.

**Mensaje de E1 (e).** La línea «Alcance de este TO» pide la expresión copiada del texto y, si no hay sujeto
nombrado, que no haya relación. Cambia en 2.408 de 2.439 unidades.

**NOTAS de E3.**
- **a:** sin el alcance en `meta_normativo`, y con la lista completa de lo que no puede declararse así.
- **b:** el encabezado de lista suma la norma y su excepción cuando los ítems son sus condiciones (212 unidades).

## 3. f, g, h y el tercer escalón

- **f.** `cap::tabla037` va a la lista de tablas forzadas a residual. Solo la trae `cap::6.2.2.6`.
- **g.** El tramo de la omisión se verifica como el de la entidad. En P4 verifican 56 de 70 en vez de 48. No toca
  `modelos_r2.py` ni E3.
- **h, candados:**
  - F04b: la lista se carga con su sha.
  - F22 y F22b: el sha del mensaje de 12 unidades que cubren 29 ramas, al importar `prompt_r2b.py`. Propongo un chunk
    sintético para la rama del alcance por clase, que solo usa `ri2_ci.pdf`.
  - F23: 6 unidades que cubren 15 ramas, más una validación sintética, al final de `prompt_e3.py`. A decidir: (i)
    entero al importar o (ii) la parte r2, perezosa; recomiendo (i).
  - R32 frena en su proceso hijo. R29, R29b y R30 pasan a procesos hijos que editan el literal.
- **El tercer escalón** (diseño, §5b), solo con el perfil r2. El techo de 40.960 queda bajo el máximo de
  `claude-haiku-4-5`, 64.000, según la nota del mandato (`:770-771`):
  - **El adaptador** en `cliente_e1.py` llama `messages.stream` y devuelve el mensaje final, normalizado a
    `Message`. Va debajo del `CachingClient` sellado, con el mismo namespace de E1.
  - **Cuándo:** desde `crear_con_reintento_corte`, solo si el reintento de 16.384 corta y la unidad no se parte, o
    si corta una parte. El techo es 40.960.
  - **El ratchet** de esas unidades usa el mismo techo por el mismo cliente; `ratchet_e3.py` no cambia.
  - **Cuántas llegan en la tanda 0:** con la mediana de P4, 2 unidades y salida máxima de 17.691 tokens; con el
    máximo, 5 y 22.554. Ninguna llega al techo (`p3c/salida/escalon3_p3c.json`).
  - **Costo incremental:** USD 0,36 y 0,97; con un reintento del ratchet al techo en cada caso, 0,79 y 2,03.
  - **Su fila,** F08d («E1 y E3 de las afectadas»), y su variación R13c no están entre las escrituras autorizadas.
  - **E3 sobre 20.000 a 40.000 tokens:**
    - el mensaje queda por debajo de unos 50.000 tokens; que entre en el contexto de `claude-sonnet-5` está NO
      VERIFICADO en el repo;
    - el veredicto tiene techo de 4.096 tokens, sin transmisión;
    - cuesta unos USD 0,08 a 0,10 por unidad;
    - propongo que todas esas unidades vayan a la muestra de la cola humana.
  - **La confirmación en P3c-2** es una llamada real a `cla::5.1.1::intro`: mensaje final, crudo guardado, acierto
    de caché y un corte forzado. Cuesta unos USD 0,05; propongo un tope de 0,20.
  - **Fuera de la tanda 0** pesa más: el censo de U-SEG-OFICIAL tiene 14 unidades que no se parten y 15 con la
    parte mayor fuera. El escalón alcanza unos 34.860 caracteres con la mediana y 27.343 con el máximo.

## 4. No-filtración

Con la regla de P1 y P3b-1 (`p3c/nofiltracion_p3c.py`):
- **Población:** 7.815 chunks.
- **Casos de control:** 93.
- **Ventanas de 5 palabras nuevas:** 970 en el prefijo y 192 en los literales.
- **Resultado:** 0 choques, y 0 bigramas o trigramas de control en el texto agregado.

## 5. Costo y P4b

**U-REEXT-T0, sin la salida:** +USD 0,68 (`p3c/salida/proyeccion_p4b_p3c.json`).
- Prefijo: +2.294 tokens, que dan +0,56 de lecturas de caché y +0,01 de escrituras.
- Línea de alcance: +0,11.

**Tercer escalón:** de +0,36 a +2,03 (§3). El tope de USD 72 no cambia.

**P4b, propuesta.** Dos brazos (el prefijo vigente y el de P3c) sobre 29 unidades nuevas, más E3 en 6.

| Grupo | Unidades |
|---|---|
| a | 4 |
| b1, lo que queda afuera (ítems) | 3 |
| b2, las condiciones de una excepción (ítems) | 3 |
| encabezados de esas listas | 4 |
| c | 4 |
| d | 4 |
| e | 4 |
| el ejemplo (`cla::5.1.1::intro` y `cla::5.1.1.1`) | 2 |
| f (`cap::6.2.2.6`) | 1 |

- **Elección:** por lectura, después de congelar el texto, y sellada antes de correr.
- **Costo:** central USD 0,83, alto 1,09. Propongo un tope de USD 1,5.
- **Riesgo:** b1 puede ser escaso. Por forma léxica, no aparece en ninguno de los 210 contenedores no leídos de la
  tanda 0 ni de los 637 de la partición.

## 6. Controles

- **Corridas:** los siete scripts de `p3c/` corrieron dos veces sobre una copia sin enlaces (con la E0 fuera de
  muestra regenerada). Las 13 salidas dan lo mismo en las dos corridas y son iguales a las de `p3c/salida/`.
- **Marcas y tabla de P4:** regeneradas dos veces sobre una copia, iguales entre sí.
- **El repo** no cambió durante ninguna corrida de control. Otras sesiones escribieron entre corridas: los archivos
  rastreados pasaron de 12.837 a 12.853.
- **`.pyc`:** sin nuevos.
- **Mis escrituras:**
  - `p4/lectura_p4.md`, `p4/marcas_p4.py` y, en `p4/salida/`, `marcas_lectura_p4.json` y `tabla_pareada_p4.json`.
    `2ed47a0` ya trae la revisión a a d; contra ese commit, los cuatro cambian solo por a′;
  - `p3c/`: 7 scripts, `diseno_p3c.md` y `salida/` con 13 archivos;
  - este freno.

## 7. Pendiente de la autora

- **Aprobar el texto,** con la lectura de los dos dudosos.
- **Decidir:**
  - el contador de `meta_normativo` con marca;
  - la vigencia (P3C-a2);
  - P4b: grupos, tope y qué hacer si falta b1;
  - h: (i) o (ii), las dos fixtures nuevas y regenerar `selftest_clave_cache.json`;
  - el tercer escalón: techo, ratchet, muestra humana, F08d y R13c, la llamada de centavos con su tope, y su selftest
    (`selftest_ub53.py`).
- **El commit** de P3c-1 y de la revisión de la lectura de P4.
