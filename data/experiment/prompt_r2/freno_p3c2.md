# U-PROMPT-R2 — FRENO P3c-2 (implementación)

04/10/2026. HEAD `1873962` al empezar y `97c21e4` al cerrar; ese commit, de otra unidad, toca solo la enmienda 6, el
plan y U-NAV-DISENO. Costo de API: USD 0,042, la llamada del tercer escalón (tope 0,20). Sin commit. Las salidas de
control están en `p3c2/salida/`.

**Corregido el 04/10/2026**, tras la revisión del freno (nota del mandato `:839-862`, `44c6e1b`), con HEAD `44c6e1b`.
Las cuatro correcciones de la revisión: el contador de `meta_normativo` con las siete clases de la enmienda 7 (§4), el
texto del §10 aplicado a la tabla de reprocesamiento (§10), el desvío de la llamada real aceptado (§5) y este freno.
Sin gasto de API en la corrección. No cambian el prefijo, el mensaje de E1, las NOTAS de E3 ni los candados.

**Fuentes.**
- Las notas del mandato hasta la última del 04/10/2026 (`docs/mandatos/UPROMPT_R2_prefijo_nuevo.md:776-838`); para la
  corrección, la nota de `:839-862` (`44c6e1b`).
- `docs/decisiones_caching_extraccion.md`.
- La enmienda 7 a L-ESQ-R2 (`data/experiment/esq/enmienda7_L-ESQ-R2_regla9_meta_normativo_2026-10-04.md`), FIRMADA
  por la autora el 04/10/2026: leída en el commit de la firma, `44c6e1b` (sha256 `81177f0c…`). Al implementar estaba en
  BORRADOR; la firma no cambió su §1.
- Los textos aprobados se tomaron del commit de P3c-1 (`438bbd5`).
- El «seguí» coincide con los archivos.

## 1. El prefijo re-congelado

- **Parche:** `e1_extractor/prompt_r2b_parche_p3c.json`, con los 15 reemplazos del borrador aprobado, iguales byte a
  byte a los de `438bbd5`. Se aplica sobre el prefijo de P3b-2, que ahora tiene candado propio, con su sha256.
- **Prefijo:** 59.909 caracteres, sha256 `ccffa4e3…`, hash canónico `322c5a23e9b7`. Es el borrador de P3c-1 byte a byte.
  - Revirtiendo los 15 reemplazos vuelve el de P3b-2.
  - El tool schema no cambia (`0c391f2b…`).
- **Namespace de E1:** `e1_extraccion|cv=e1-extractor-v1-p322c5a23e9b7|think=0`.
- **Tamaño medido:** 27.840 tokens, la escritura de caché de la llamada real. P3c-1 estimaba unos 28.603.
- **Candados del hash nuevo:** en `prompt_r2b.py`, `perfil_e1.py`, `selftest_prompt_r2b.py` y
  `selftest_manifiesto.py`.
- **Una cifra del manifiesto cambia por el punto f:** las unidades con tabla serializada confiable pasan de 37 a 36,
  porque `cap::6.2.2.6` no trae otra tabla.

**Coincidencia con la enmienda 7, §1.** El texto final coincide con los seis puntos del §1 (la firma, en `44c6e1b`,
trae la nota de esa verificación).
- **§1.1, lo que queda como meta-normativo:** el significado, el objetivo o finalidad, y la fecha de entrada en
  vigencia (P3C-a1, P3C-a2).
- **§1.2, lo que deja de serlo:** el alcance y la lista completa (P3C-a1, P3C-a3).
- **§1.3, adónde va:** la Definicion de la clase, la norma misma o `fuera_de_tipos` (P3C-a3).
- **§1.4, finalidad o alcance:** P3C-a3.
- **§1.5, el encabezado puro:** P3C-a3 y P3C-a6.
- **§1.6, la Definicion:** P3C-a5.
- **Un matiz:** «régimen de transición con condiciones» no aparece con esas palabras en el prefijo. Lo cubre la
  prueba de P3C-a3, porque un tramo con una condición no puede ser `meta_normativo`.

## 2. Mensaje de E1, NOTAS de E3 y lista forzada

- **La línea «Alcance de este TO»** es la de P3c, punto e (`prompt_r2b.LINEA_ALCANCE`).
  - Las tres líneas fijas que estaban escritas dentro de la función pasan a constantes.
  - Con la línea de alcance de P1 y la lista vacía, el mensaje es el del borrador de P3b-1 en las 2.434 unidades.
  - Con el texto nuevo, cambia solo la línea de alcance (todas las unidades menos docvig) y, en `cap::6.2.2.6`,
    además sus tablas (`selftest_prompt_r2b`, [E]).
- **Las dos NOTAS de E3** son las del borrador aprobado (`NOTA_E3_OMISIONES` y la constante nueva
  `NOTA_E3_ENCABEZADO_LISTA`).
- **`cap::tabla037`** está en `tablas_residuales_forzadas_r2b.json`, con motivo y fecha.

## 3. Los candados (F04b, F22, F22b y F23)

| Fila | Candado | Sello |
|---|---|---|
| F04b | la lista de tablas forzadas se lee con su sha256 | `98cc96b2…` |
| F22 y F22b | al importar `prompt_r2b`: el sha256 del mensaje de 12 unidades más una sintética (alcance por clase) | fixture `4d69f7f4…`, mensaje `a9cb702c…` |
| F23 | al final de `prompt_e3`, entero al importar (opción i): el sha256 del mensaje de E3 de 6 unidades, con y sin la marca r2, más un caso sintético (la NOTA de las omisiones) | fixture `e8fa5dc4…`, mensaje `da17c22e…` |

- **Cálculo y verificación:** `p3c2/sellar_p3c2.py` calcula los sellos sobre una copia y, con `--verificar`,
  controla que los módulos importen sin frenar (`salida/verificacion_sellos_p3c2.json`).
- **El prefijo de E3 y su candado** no cambian (`21a836c7de6d`).
- **Selftest de claves** (`mantenimiento/selftest_clave_cache.json`, regenerado):
  - R29, R29b, R30 y R32 dan «frena». R29, R29b y R30 pasaron a procesos hijos que importan una copia en memoria del
    módulo con el literal editado.
  - R13c: el techo del escalón cambia solo la clave de ese pedido.
  - Veredicto OK; contraste con la tabla OK (41 variaciones de r2b).
- **Ningún candado cambia una clave.** El anclaje del perfil sellado da 2.434 de 2.434 en E1 y 2.430 de 2.430 en E3.
  Las 25 variaciones del perfil sellado, el anclaje y la muestra son iguales a los del JSON commiteado.
- **Acoplamiento declarado (opción i):** importar `prompt_e3` importa `prompt_r2b` y corre sus candados, aun en el
  perfil sellado. El inventario del perfil sellado en el selftest de claves suma esos archivos.
- **La tabla** cambia en sus filas F04b, F22, F22b y F23, a «frena; re-sellado, …», y suma F08d.

## 4. g y el contador de `meta_normativo`

- **g:** el tramo de la omisión se verifica como el tramo simple de la entidad, con los contadores
  `omisiones.tramo_solo_heredado` y `omisiones.tramo_orden_de_lectura`. `modelos_r2.py` no cambia.
  - Re-validada la salida guardada de P4, verifican **56 de 70** omisiones: 7 del heredado y 1 en el orden de lectura
    (`salida/revalidacion_p4_p3c2.json`).
- **El contador** `omisiones.meta_normativo_con_marca` cuenta y no rechaza, con un contador más por clase
  (`meta_normativo_con_marca:<clase>`). Desde la corrección tiene las siete clases de la enmienda 7, §1.2: deber,
  prohibición, facultad, condición, excepción, alcance y modalidad. Los contadores no entran al mensaje de E3: con
  la corrección, las fixtures de los dos mensajes y el JSON del selftest de claves salen iguales a los del repo (§9).
  - **Las marcas** (`validador_r2.MARCAS_META_NORMATIVO`), sobre el tramo en minúsculas, sin tildes y con palabras
    enteras:
    - deber: debe, deben, deberá, deberán, debería, deberían, se requiere, se requerirá, se requerirán, obligado/a/s,
      tendrá que, tendrán que;
    - prohibición (nueva): un modal negado, «no», «ni» o «tampoco», con «se» o «está/estará» opcionales, delante de
      puede, pueden, podrá, podrán, podría, podrían, debe, deben, deberá, deberán, debería, deberían o facultado/a/s;
      prohib…, vedado/a/s, en ningún caso, abstener…, abstendr…; y «no (se) (está, será…) admit…, permit…, autoriz…»;
    - facultad: puede, pueden, podrá, podrán, podría, podrían, facultado/a/s;
    - condición: cuando, siempre que, en tanto, en la medida en que, en caso de, a condición de, condición,
      condiciones;
    - excepción: excepto, salvo, con excepción de, exceptu…, exclu…; y la aplicación negada: «no», «ni» o «tampoco»,
      con «se» y un verbo copulativo (es, sea, será, resulta, resulte, resultará, en singular o plural) opcionales,
      delante de «de aplicación», aplica(n), aplicará(n), aplicable(s), rige(n) o regirá(n);
    - alcance (nueva): abarca(n), abarcará(n), comprende(n), comprenderá(n), comprendido/a/s, incluye(n),
      incluirá(n), incluido/a/s, alcanzado/a/s, rige(n) para, regirá(n) para, se aplica(n), se aplicará(n),
      aplicable(s) a, y el verbo copulativo seguido de «de aplicación»;
    - modalidad (nueva): mediante, por medio de, a través de, por intermedio de, por escrito, en forma, en soporte,
      por vía, alternativa(s), alternativamente, modalidad(es).
  - **«No podrá» es una prohibición.** Un modal negado («no podrá», «no deberán», «no está facultada») cuenta como
    prohibición y no como facultad ni como deber: deber, facultad y alcance se buscan sobre el tramo sin lo negado.
    Por la misma regla, la aplicación negada («no será de aplicación», «no se aplica») es una excepción y no un
    alcance. Un tramo con «no podrá» y, aparte, «podrá» cuenta en las dos clases.
  - **Selftest** (`selftest_pyd_r2`, G16, 3 casos nuevos): una omisión por clase nueva y una de finalidad que no
    marca; «no podrán» y «no deberán» contra «podrán»; la aplicación negada contra la afirmada. Da 395/395.
  - **En P4** (`salida/revalidacion_p4_p3c2.json`): marca 15 de las 24 omisiones `meta_normativo`.
    - **Detecta las 9 normativas:** por deber, `ext::13.4.8` y `adrei::S5`; por condición, `ctacte::4.2.1` y
      `expaef::2.2.6.5`; por excepción, `ext::10.4.2.7`; por alcance, `cla::5.1.1::intro` y `ctacte::5.1.2.2`; por
      modalidad, `ctacte::8.3::intro` y `ctacte::8.4::intro`.
    - **6 marcadas no están entre las 9**, las mismas que con cuatro clases:
      - dos encabezados de lista: `adrei::4.3.1::intro` (deber) y `polcre::7.1::intro` (condición);
      - dos tramos del heredado: `cla::5.1.1.1` (excepción y alcance) y `adrei::4.3.1.2` (deber);
      - un tramo que cruza del título al cuerpo: `ctacte::6.4.7::intro` (condición);
      - `ric::3.1.8` (deber), cuya frase la autora leyó como alcance en el FRENO P3c-1 (decisión 1).
    - **Por clase,** el contador del validador da deber 5, prohibición 0, facultad 0, condición 4, excepción 2,
      alcance 3 y modalidad 2: 16 marcas en 15 omisiones, porque `cla::5.1.1.1` trae dos.
    - **Control:** con las cuatro clases de antes, la lista nueva da 11 de 24 y 5 de las 9, como antes de la corrección.
    - Con el texto nuevo, ninguna de las seis debería quedar como `meta_normativo`.
  - **Límite de la cifra:** escribí las marcas nuevas conociendo las 9 de P4, así que el 9 de 9 no es una medición
    fuera de muestra. En P4 no hay ningún caso de prohibición ni de facultad. La medición es la de P4b, por brazo, y
    la de U-REEXT-T0.
  - **Referencia de la revisión:** su lista de prueba detecta las 9 y marca otras 9 de las 15 restantes; esta marca
    6 de esas 15.

## 5. El tercer escalón (solo con el perfil r2)

- **La documentación oficial:**
  - `claude-sonnet-5` (E3) tiene 1 M tokens de contexto, así que un pedido de unos 50.000 entra
    (https://platform.claude.com/docs/en/models/sonnet-5/overview, consultada el 04/10/2026).
  - `claude-haiku-4-5` tiene 200 k de contexto y 64 k de salida (https://platform.claude.com/docs/en/models/overview,
    misma fecha).
- **`cliente_e1.py`:**
  - `AdaptadorTransmision` llama `messages.stream`, normaliza el mensaje final a `Message` (sin `parsed_output`) y queda
    debajo del `CachingClient` sellado, con el mismo namespace.
  - `ClienteE1Real(transmision=True)` despacha por él todo pedido de más de 21.333 tokens de salida. Proyecta el
    tope con el techo y lleva un componente propio en el log de usage.
  - `crear_con_reintento_corte(..., escalon_3=...)` hace la tercera llamada, a 40.960. Sin el parámetro, devuelve el
    par de siempre.
- **`runner_corpus.py`, solo r2:**
  - el escalón corresponde si la unidad es una parte o no se puede partir;
  - la marca `escalon_3` va al registro de E1 y la lista, al resumen de E1;
  - el error definitivo nuevo es `max_tokens_hit_tras_escalon_3`;
  - el ratchet de esas unidades usa el mismo techo, por el cliente con transmisión. `ratchet_e3.py` no cambia.
- **`selftest_ub53.py`:** 52/52, con P7 nuevo (12 casos con stubs y un SDK falso).
- **La llamada real** (`salida/llamada_escalon3_p3c2.json`), sobre `cla::5.1.1::intro`, en una base propia en el
  scratchpad:
  - sin transmisión, el SDK rechaza el pedido antes de enviarlo;
  - por transmisión, `tool_use` con `stop_reason` «tool_use»;
  - el crudo guardado tiene las mismas claves que uno sin transmisión de P4;
  - la repetición sale de la caché;
  - el corte forzado (64 tokens) da «max_tokens».
  - **Gasto:** USD 0,042. El log de usage de esas dos respuestas quedó en el de la copia desde la que corrió.
- **Desvío del diseño:** la llamada real transmitió con 24.576 tokens de techo, no con 40.960. Con 40.960, el peor
  caso (USD 0,20 de salida más la escritura del prefijo) pasaba el tope de USD 0,20. Como 24.576 pasa de 21.333, el
  despacho y la transmisión son los del escalón. El techo de 40.960 lo ejercita P7 con el SDK falso.
  **Aceptado en la revisión** (nota del mandato `:856-859`): la llamada no se repite y P3c-2 no tiene más gasto de API.

## 6. Los perfiles existentes, byte a byte

- **Cadena r2a con el código nuevo** (`r2_codigo2/c2_cadena.py`): diez `70d51e42…` y desarrollo `fa4c1043…`. Las
  cuatro corridas por grafo (sellado, r2a, r2b y r2b sin P3b) son iguales a las de C2.
- **Selftests de la cadena, sobre una copia:**
  - `selftest_prompt_r2b` 51/51 (era 34);
  - `selftest_e1` 80/80;
  - `selftest_pyd_r2` 395/395 (era 385; G16 nuevo, 10 con los 3 de la corrección);
  - `selftest_e3` 101/101 (era 95; M nuevo, 6);
  - `selftest_e2` 41/41;
  - `selftest_ub53` 52/52 (era 40);
  - `selftest_r3` 109/109;
  - `selftest_r4` 26/26;
  - cadenas sintéticas de P3, 27/27, y de P3b-2, 20/20;
  - `selftest_manifiesto` 44/49: los 5 fallos son los de P5 por la ruta del reporte, lo esperado sobre una copia.
- **Selftest de claves:** §3.

## 7. No-filtración, sobre el texto implementado

- **Corrida:** `p3c2/nofiltracion_p3c2.py`, con la regla y la población de P3c-1, contra el prefijo de P3b-2 y la
  línea de alcance anterior.
- **Población:** 7.815 chunks y 93 casos de control.
- **Ventanas nuevas:** 970 en el prefijo y 192 en los literales.
- **Resultado:** 0 choques, y 0 bigramas o trigramas de control.
- Los literales implementados son los del borrador aprobado.

## 8. Costo

**U-REEXT-T0, con el prefijo medido** (`salida/costo_p3c2.json`): +USD 0,49 sin contar la salida.
- Prefijo: +1.531 tokens, que dan +0,37 de lecturas y +0,01 de escrituras.
- Línea de alcance: +0,11.
- Tercer escalón: de 0,36 a 0,97, o de 0,79 a 2,03 con un reintento del ratchet al techo.
- La salida la mide P4b. El tope de USD 72 no cambia.

**P4b:** 29 unidades en dos brazos y E3 en 6: central USD 0,83, alto 1,09, bajo el tope de 1,5.

## 9. Controles

- **Doble corrida:** los 5 scripts de USD 0 de `p3c2/` (la llamada real no se repite), los 11 selftests de la cadena
  y el selftest de claves, dos veces sobre una copia sin enlaces (`salida/control_p3c2.txt`). Las 10 salidas comparadas son iguales entre sí.
  Las fixtures y `selftest_clave_cache.json` son iguales a las del repo.
- **El repo** no cambió durante el control (12.867 archivos con el mismo sha256 antes y después).
- **`.pyc`:** sin nuevos.
- **Mis escrituras:** 15 archivos modificados y 3 nuevos (las dos fixtures y el parche), más `p3c2/` (6 scripts y
  `salida/`, con 8 archivos desde la corrección) y este freno.

**Doble corrida de la corrección** (`salida/control_correcciones_p3c2.txt`).
- **Lo que cambia:** `validador_r2.py` (las marcas), `selftest_pyd_r2.py`, `p3c2/revalidar_p4_p3c2.py` y su salida, y
  `tabla_reprocesamiento.md`, que lee el contraste del selftest de claves. Corrí dos veces, sobre una copia sin
  enlaces, el mismo conjunto del control de arriba: lo que cambia y, como control, el resto.
- **Resultados, iguales en las dos corridas:**
  - `selftest_pyd_r2` 395/395 y la re-validación de P4 (15 de 24; 9 de 9);
  - selftest de claves: veredicto OK y contraste con la tabla OK; su JSON es igual al del repo, así que ninguna clave
    cambia;
  - las dos fixtures, iguales a las del repo: el mensaje de E1 y el de E3 no cambian, y los candados no frenan;
  - cadena r2a: diez `70d51e42…` y desarrollo `fa4c1043…`, los de C2;
  - el resto, como arriba: 51, 80, 101, 41, 52, 109 y 26 casos sin fallos, cadenas 27/27 y 20/20, manifiesto 44/49
    (los 5 de P5).
- **Las 10 salidas comparadas** son iguales entre corridas, y las cuatro de `p3c2/salida/` que se re-generan, iguales
  a las del repo.
- **El repo** no cambió durante el control (12.874 archivos). Ningún `.pyc` nuevo.
- **sha256 del repo** antes y después de la corrección: en el paquete de revisión. Cambian solo los archivos de la
  corrección, con este freno.

## 10. Para la autora

- **El texto de la tabla quedó aplicado**, autorizado en la revisión (nota del mandato `:854-855`), en sus tres
  lugares de `mantenimiento/tabla_reprocesamiento.md`:
  - el §1, donde decía «Sin candado:» (hoy `:88-90`): «Desde P3c-2 de U-PROMPT-R2 tienen candado: la lista de tablas
    forzadas (su sha256), las líneas del mensaje de E1 y las NOTAS de E3 (el sha256 del mensaje de un conjunto fijo de
    unidades). Un cambio frena hasta re-sellar (filas F04b, F22, F22b y F23).»;
  - la nota de F22, F22b y F23 (hoy `:239-242`), con el mismo sentido: tienen candado, un cambio frena hasta re-sellar
    (R29, R29b y R30) y, re-sellado, una línea de todo mensaje hace pagar E1 de todas las unidades, y una condicional,
    solo las que la llevan;
  - «Solo r2b» (hoy `:259`), con F08d.
  Nada más de la tabla cambió en la corrección.
- **Quedan viejos tres textos más del §1 de la tabla**, fuera de lo autorizado. Los dejo propuestos, sin aplicar:
  - `:79`, «Del perfil r2b, contra el congelado de P3b-2:» → «contra el congelado de P3c-2:»;
  - el inventario de archivos de datos (`:70` y `:72`) no nombra `prompt_r2b_parche_p3c.json`,
    `candado_mensaje_r2b.json` ni `candado_mensaje_e3.json`, que el inventario del selftest sí abre
    (`selftest_clave_cache.json:708-714`);
  - el reintento del ratchet (`:63`) dice `max_tokens` de 16.384 sin la excepción del tercer escalón: 40.960 en
    esas unidades (fila F08d).
- **Una diferencia entre textos firmados y decisiones:** la enmienda 7, §3 (`44c6e1b`), describe el contador de
  U-REEXT-T0 con cuatro marcas (deber, facultad, condición o excepción); la decisión de la misma fecha
  (nota del mandato `:850-853`) lo pasa a siete. Implementé las siete. El texto de la enmienda no lo toqué: una nota
  posterior a la firma lo alinearía, si la autora lo decide.
- **PENDIENTE:**
  - el commit de P3c-2;
  - el «seguí» de P4b, después de ese commit.
