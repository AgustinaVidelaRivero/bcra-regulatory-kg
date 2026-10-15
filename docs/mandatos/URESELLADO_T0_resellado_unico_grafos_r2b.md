# Mandato del re-sellado único de los grafos r2b de la tanda 0 (versión para firmar, 15/10/2026)

Versión para firmar, de la mesa (hoja de ruta, §101 y §108), con las cuatro decisiones de la autora del 15/10/2026, recibidas a las
16:17:35 (§8). R0 está cerrada (`1d690df3` y `2d0f5277`). USD 0.

Reemplaza al borrador v3 del 15/10/2026 (`decisiones_101_mesa/resellado/borrador_mandato_resellado_unico_tanda0_v3_mesa.md`), que a su vez
reemplazaba al v2 del 13/10/2026 y al borrador del 07/10/2026.

## Lo que cambia respecto del v3

- **Las cuatro decisiones del §8,** tomadas: los nombres con el sufijo `_rs1`, los cuatro grafos, frenar si el diff contra O2 trae algo
  que no viene de R0, y las notas en un commit propio.
- **La enmienda 8 al protocolo entre tandas está FIRMADA** (15/10/2026, 13:00:14; commit `54902301`;
  `docs/enmienda8_protocolo_entre_tandas_2026-10-15_calendario_hacia_B6.3.md`).
  - No es la enmienda 8 a L-ESQ-R2 (`data/experiment/esq/enmienda8_L-ESQ-R2_exceptua_operacion_2026-10-07.md`), que quedó NO FIRMADA el
    09/10/2026 y es la que deja fuera VAL-03b.
  - Este texto distingue las dos.
- **Su lugar en el orden de las ejecutoras** (§1 bis): va segundo, después del FRENO S2-b de U-SEG-OFICIAL y su commit, y corre sola.
- **El grafo de desarrollo re-sellado** (`KG_Tanda0_Desarrollo_r2b_rs1`, la versión posterior de `6e756043…`) es el brazo del grafo de
  A2.2, si está sellado al despachar el tramo 3 de A2.1 (mandato de A2.1, `docs/mandatos/A2_1_sistema_por_fragmentos_preregistro_A2_2.md`,
  D-A).
- **La cláusula de copias,** en su versión 2, con `NO_ABRIR_*` (§7).
- **Las precondiciones a a e,** medidas de nuevo por la mesa el 15/10/2026 con HEAD en `c2b6cb60`: dan lo esperado (§1).

## Lo que cambia respecto del v2

- **R0, cerrada:**
  - la fase 1 está en `1d690df3` y la fase 2 en `2d0f5277`, con USD 0,157948 de 1,50;
  - la cola de la tanda 0: 74 de 2.439 medida en r2b, y 69 en las salidas de E3 después de R0, para el grafo re-sellado, que todavía no
    se ensambló (`data/experiment/reextraccion_v2/r0/revision_fase_2_R0_mesa.md`, «Para el pre-registro de la tanda 1»). El re-sellado
    la mide sobre los grafos nuevos.
- **El control A3r** del selftest de claves ya lo dejó redefinido R0 (`2d0f5277`). Acá solo se corre.
- **La tanda 0 queda en su E0** en el grafo evaluado, por decisión de la autora del 15/10/2026 (nota al pie de
  `docs/mandatos/USEG_OFICIAL_S0-6a_correccion_E0.md`). Coincide con el §0 de abajo.
- **La enmienda 8 al protocolo entre tandas** (FIRMADA el 15/10/2026, `54902301`) pasa la re-aplicación del código a una sola vez,
  antes del sello del grafo evaluado (R3). No cambia este re-sellado, que es la release r2 aplicada a la tanda 0. Lo piden la enmienda
  7, los sellos del laudo de la release y el sorteo de la etapa V de tripletas.
- **El paso 0 y las dos cláusulas** de todo despacho desde el 13 y el 14/10/2026: la carpeta personal como `$HOME`, las copias sin `.env`
  y las carpetas vedadas (§1 y §7).
- **Las precondiciones a y b, medidas por la mesa el 15/10/2026** (§1).

## Lo que cambiaba el v2 respecto del borrador del 07/10

- **La precondición:**
  - ya no es R2-3: es el código de U-OMISIONES-COD (`ded41d5`) más R0 cerrada;
  - la «opción II o III» del 07/10 quedó resuelta: el re-sellado es uno solo, después de U-OMISIONES-COD (tablero, §0, «Grafos»).
- **Qué grafos cambian:**
  - el borrador decía que cuatro cadenas no cambian; con el código de O2 cambian las cuatro r2b (`omisiones_cod/o2/FRENO_O2.md:76-83`);
  - solo las dos r2a quedan iguales.
- **Las unidades:** el borrador decía que el re-sellado «no agrega ni quita unidades». Con R0 sí cambia el conjunto: las aceptadas que
  salen de la cola entran a los grafos sin cola (enmienda 7, §1.5).
- **El estado de las firmas:** la enmienda 7 está FIRMADA (`4a33ce9`), y por su nota al pie (`0c516af`) R0 corre solo E3-01; VAL-03b no
  corre (la enmienda 8 a L-ESQ-R2 quedó NO FIRMADA).
- **Los grafos sellados:** no se reescriben en `grafos.py`. Por el principio 9, el re-sellado agrega versiones posteriores, como hizo
  U-SINCOLA-T0 (abajo, decisión 1).

## 0. Qué es

- **Qué hace:** produce, sella y registra la versión posterior de los cuatro grafos r2b de la tanda 0 (diez y desarrollo, completos y
  sin cola).
- **Con qué código:** el del ensamblado de U-OMISIONES-COD, sobre las salidas de E1 y E3 de la tanda 0 tal como las deja R0.
- **Dónde corre:** es una etapa propia, como SC2 de U-SINCOLA-T0, y nunca dentro de la unidad que cambia la regla.
- **USD 0:** ninguna llamada a la API.
- **Lo que no cambia:** la E0 de la tanda 0, porque la corrección de E0 con reglas generales la deja fuera
  (`segmentacion_oficial_e0r2/s0_6/b/FRENO_S0-6b.md:38`: 57 de 57).

## 1. Paso 0 y precondiciones

**Paso 0.** `pwd`, `git rev-parse --abbrev-ref HEAD` (tiene que dar `main`), `git log --oneline -3` y `git status --short` de las carpetas
de abajo. Pegás la salida en el FRENO con la carpeta personal reemplazada por `$HOME`. Si no estás en la raíz del repo, frenás.

Se pega la salida de cada precondición en el FRENO. Si una falla, frenás sin escribir.

- **a. El código:** `git log` contiene `ded41d50` y los dos commits de R0, `1d690df3` y `2d0f5277`.
  - `git diff --stat ded41d50 HEAD -- data/experiment/tanda0/code data/experiment/reextraccion_v2/corpus_v2 data/experiment/reextraccion_v2/e2_reduce data/experiment/reextraccion_v2/e1_extractor data/experiment/reextraccion_v2/e3_verificador data/experiment/pyd_r2/code scripts/shapes_validator.py scripts/regression_kg.py`
    da vacío.
  - La mesa lo midió el 15/10/2026, con HEAD en `aabe6986` y de nuevo en `c2b6cb60`: da vacío. R0 no cambió código de esas rutas.
- **b. La E0 de la tanda 0:** `git diff --quiet 9f6361e HEAD -- data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b/` vacío, con
  57 archivos rastreados. La mesa lo midió el 15/10/2026, también con HEAD en `c2b6cb60`: da vacío y 57.
- **c. Los grafos sellados, intactos:**
  - `a9631a64…` (diez) y `6e756043…` (desarrollo) en `bbc38dc`;
  - `e22fae1a…` (diez sin cola) y `2922b72d…` (desarrollo sin cola) en `dde9f44`;
  - en `grafos.py` y en `scripts/regression_kg_esperado.json`.
- **d. Las salidas de R0:** los sha256 de `corpus_tanda0/salida_r2b/{ext,docvig}/*.jsonl` son los que declara el FRENO de la fase 2 de R0
  (`data/experiment/reextraccion_v2/r0/FRENO_R0_fase2.md`), y están commiteados en `2d0f5277`.
- **e. `git status --short`:** vacío en `tanda0/`, `corpus_v2/`, `scripts/` y `neo4j/`.

## 1 bis. Su lugar en el orden de las ejecutoras (decisión de la autora del 15/10/2026)

- Las ejecutoras que escriben en el repo corren de a una, con los commits entre una y otra
  (`docs/registro_decisiones_calidad_y_evaluacion_2026-10-15.md`, §8).
- **Este re-sellado va segundo:** se despacha cuando estén el FRENO S2-b de U-SEG-OFICIAL y su commit, y la firma de este mandato.
- **En el paso 0, además:**
  - `git log --format=%s -5` muestra el commit del FRENO S2-b de U-SEG-OFICIAL;
  - `git status --porcelain -- data/experiment/segmentacion_oficial_e0r2/s2` no da nada.
  - Si no, otra ejecutora todavía escribe en el repo, y frenás.
- **Nada demora el despacho de la tanda 1** (decisión de la autora del 15/10/2026). Este re-sellado está en su camino: el laudo de la
  release y el sorteo de la etapa V de tripletas lo esperan.

## 2. Las cadenas (sobre una copia sin enlaces, con dos corridas)

1. **Las seis cadenas:**
   - las dos r2a, byte a byte: `70d51e42…` y `fa4c1043…` (laudo de la release r2, §3);
   - las cuatro r2b, con sha nuevo y doble corrida byte a byte.
2. **El diff contra O2:**
   - O2 dio, con su código y sin R0: `710664e9` (diez), `a50210b4` (diez sin cola), `18a2747d` (desarrollo) y `9f49d62d` (desarrollo sin
     cola) (`FRENO_O2.md:80-83`);
   - todo lo que difiera de esos cuatro tiene que venir de las unidades de R0;
   - se lista por campo, con su causa, con el formato de `omisiones_cod/o2/salidas/diff_declarado_*.json`. Una fila sin causa frena;
   - **si el diff trae algo que no viene de R0, frenás** (decisión 3), sin sellar.
3. **El diff contra los sellados** (`a9631a64`, `6e756043`, `e22fae1a`, `2922b72d`):
   - se declara por campo y por causa: O2 (los grupos del FRENO de O2) o R0;
   - a ninguna fila le falta la causa.
4. **La cola de la tanda 0:** la de antes (74) y la de después, con la lista de las unidades que salen o entran y el estado final de cada
   una (enmienda 7, §1.5). Después de R0, las salidas de E3 dan 69. Si los grafos nuevos dan otra cifra, se declara la diferencia con su
   causa.

## 3. Shapes, suite, `grafos.py` y Neo4j

1. **Shapes, con perfil r2 y fase r2b, sobre los cuatro grafos nuevos:** ninguna bloqueante en FAIL, y la tabla de lo que cambia contra O2
   y contra los sellados.
2. **Suite:**
   - entradas nuevas en la fixture, una por grafo, editadas con un script como `sincola_t0/sc2/editar_fixture_grafos_sc2.py`;
   - las selladas no se tocan;
   - `selftest_regression_kg` en verde, con doble corrida;
   - 0 regresiones no declaradas: las que haya se listan para que la autora las acepte por escrito (laudo de la release r2, §3, punto 2).
3. **`grafos.py`:**
   - cuatro entradas nuevas, con label, índice fulltext y `ev2_key` propios;
   - `commit_sellado` en «PENDIENTE» hasta el segundo commit del sello;
   - las entradas selladas no se tocan;
   - el registro de la vista sigue el patrón de `sincola_t0/registro_vista_r2b_sincola.py`.
4. **Neo4j:**
   - `cargar_neo4j_tanda0.py --grafo <clave>`, una vez por grafo, con el control del sha antes de cargar;
   - el gate 5, OK;
   - ningún nodo cargado con la marca de la cola en los sin cola.
5. **El sello va en dos commits de la autora:** el primero con todo lo anterior, y el segundo pone su hash en `commit_sellado`, como
   `bbc38dc` y `c9540c0` (U-REEXT-T0) o `dde9f44` y `235a295` (U-SINCOLA-T0).
6. **Las notas a los documentos firmados** van en un commit propio, inmediatamente después de los dos del sello (decisión 4).

## 4. Los controles que esperan este re-sellado (cada uno con su comando y su salida)

- **U-CONF-MATRIZ** (`docs/mandatos/UCONF_MATRIZ_lectura_confirmacion.md:35-38`): las 60 aristas leídas siguen en el grafo re-sellado con
  los mismos extremos. Ninguna sale por → Potestad, porque confirmó en C4 (`conf_matriz/c2bis/c4_C2bis.json`, `d2f24cb`). Las que cambien
  se listan y se declaran.
- **Pre-registro de tripletas:** el sorteo de la etapa V espera este re-sellado
  (`docs/enmienda1_preregistro_evaluacion_tripletas_2026-10-08_umbrales.md:22`). No se corre acá: se deja dicho el sha que lo habilita.
- **Laudo B2.4** (`docs/laudo_B2.4_sujetos.md:25-28`): la re-medición dice si se movió alguna arista de los puntos de los ocho patrones. Si
  se movió, el laudo recibe una nota.
- **Enmienda 7, §1.5:**
  - el control A3r del selftest de claves, redefinido por R0 (`2d0f5277`): se corre sobre los grafos nuevos y se pega su salida;
  - la población de U-LECTURA-ACEPTADAS;
  - la cola;
  - las dos cifras de la línea de base del pre-registro de la tanda 1;
  - las notas de `docs/insumos_escritura.md` §7.
- **Condición 10 del checklist,** sobre los grafos nuevos, como en U-SINCOLA-T0:
  - Excepcion presente;
  - el alcance por jerarquía a `cla::5.1.1.1` y `cla::5.1.1.2`;
  - X17 con al menos una `remite_a` hacia `cla::3.7`.
- **El ejemplo de la tesis (figura 4.5):** `generar_figura_ensamblado_ejemplo.py` corre sobre una copia.
  - Si `cla::5.1.1.1` no cambia, la figura no cambia, pero su LEEME recibe una nota con el sha vigente y por qué.
  - Lo mismo vale para las otras figuras que citan los sha sellados.
- **La re-medición r2b del tablero de correcciones (condición 4):** va después, en su propia unidad. Acá se deja el sha.

## 5. El alcance: qué entra y qué no (alcance congelado, tablero §0, «Grafos»)

- **Entran:** el código de U-OMISIONES-COD (`ded41d5`) y las salidas de R0. Nada más.
- **No entran, salvo una decisión de la autora antes del despacho:**
  - **U3 de U-UNION-ESTRECHA:** va antes del armado que precede al sello del grafo evaluado (su mandato, `:71`);
  - **U-PARES-REMITE-A:** está en versión para firmar (`c080914`). Su §7 prevé que la opción (b) entre al re-sellado como única
    excepción, si el resultado llega antes. Hoy no hay resultado;
  - **el retiro de → Potestad:** no aplica, porque confirmó;
  - **casi duplicados y B′:** son del grupo 2, antes del sello del grafo evaluado;
  - **la enmienda 8 a L-ESQ-R2** (`data/experiment/esq/enmienda8_L-ESQ-R2_exceptua_operacion_2026-10-07.md`): NO FIRMADA, así que
    VAL-03b no corre. No es la enmienda 8 al protocolo entre tandas, que está firmada.

## 6. Los documentos que citan los sha sellados

- Hoy son 31 archivos: `git grep -l -E 'a9631a64|e22fae1a|6e756043|2922b72d' -- docs scripts data/experiment/neo4j` (mesa, 15/10/2026,
  con HEAD en `c2b6cb60`; eran 30 el 13/10).
- **Los firmados no se editan:** reciben una nota fechada debajo de su firma, con el sha nuevo y por qué. La lista exacta se arma con ese
  comando al despachar. Esas notas van en un commit propio, inmediatamente después de los dos del sello (decisión 4).
- **La fixture y `grafos.py`:** solo reciben las entradas nuevas.
- **El material sellado de U-SINCOLA-T0 y de O2:** no se toca.

## 7. Escrituras, prohibiciones y requisitos

- **ESCRITURAS:**
  - manifiestos nuevos en `reextraccion_v2/manifiestos/`, uno por grafo;
  - las salidas nuevas de los cuatro ensamblados en `corpus_tanda0/`, en carpetas nuevas;
  - una carpeta propia de la etapa en `data/experiment/`, con su FRENO, sus scripts, el registro de la vista y sus salidas;
  - en el sello: la fixture y `grafos.py`, solo las entradas nuevas;
  - las notas fechadas del §6;
  - el scratchpad y el paquete `revision_<etapa>/`.
  - Los nombres, por la decisión 1 (§8).
- **PROHIBIDO:**
  - cambiar código: el ensamblado, los validadores, las shapes, la suite, E0, E1 y E3;
  - tocar las salidas selladas (`ens_diez_r2b/`, `ens_desarrollo_r2b/`, `ens_*_sincola/`), `salida_r2b/`, `salida_tanda0_r2b/`,
    `e0_chunking/` y `segmentacion_oficial_e0r2/`;
  - tocar las entradas selladas de la fixture y de `grafos.py`;
  - EV2, la API y commitear.
- **REQUISITOS:**
  - CLAUDE.md §4, de a a l: la copia sin enlaces con el sha256 del repo antes y después; nunca un generador sobre el repo;
    `PYTHONDONTWRITEBYTECODE=1`; todo conteo recomputado;
  - ninguna acción de la autora como hecha;
  - el grep de convenciones;
  - el paquete con su `manifest.txt` y su copia permanente verificada.
- **Carriles** (`docs/plan_tesis.md:927-930`): la etapa escribe en `reextraccion_v2/` y `scripts/` (carril B) y en `neo4j/` (carril A).
  Corre sola, como U-SINCOLA-T0.

### Las dos cláusulas de todo despacho

**Copias del repo sin `.env` ni `NO_ABRIR_`.** Ninguna copia del repo lleva un `.env` ni un archivo cuyo nombre empiece con `NO_ABRIR_`.
La copia se hace así:

```
rsync -a --no-links --exclude=/.git --exclude=/.venv --exclude=/.venv-app --exclude=.DS_Store --exclude=__pycache__ \
  --exclude='.env' --exclude='.env.*' --exclude='*.env' --exclude='NO_ABRIR_*' <repo>/ <copia>/
```

- Justo después, y antes de correr nada sobre la copia:
  `find <copia> \( -name '.env' -o -name '.env.*' -o -name '*.env' -o -name 'NO_ABRIR_*' \) | wc -l` tiene que dar 0. Si no da 0,
  frenás. Los encontrados se borran por nombre, sin abrirlos, y se declaran en el FRENO con su ruta (con la carpeta personal reemplazada
  por `$HOME`).
- Nunca abrís, mostrás, copiás ni imprimís un `.env`: ni con `cat`, `head`, `less`, `grep` o `sed`, ni con Read, ni desde un script.
  La clave la carga el runner, solo en la corrida real en el repo.
- La copia queda sin el `.env.example` rastreado de `run_2_papers/code/` y sin el `NO_ABRIR_` del repo
  (`data/experiment/med_umbrales/p/lote1/freno/`). Si un control compara la copia con el repo archivo por archivo, lo declara.

**Carpetas vedadas.** No abrís, no listás ni copiás nada de estas carpetas, salvo que el despacho autorice un archivo por su ruta:
- en `~/INGENIERIA IA/TESIS/fuera_del_repo/`: `adjudicacion_s1ter/`, `adjudicacion_s1quater/`, `correccion_E0/`, `lecturas_ciegas/`,
  `lectura_lote2/`, `respaldo_memoria/` y `NO_ABRIR_evidencia_adjudicacion_s1quater/` (la evidencia de la adjudicación de S1-quater:
  una copia del scratchpad de una sesión y la carpeta `traspaso_etapa2`);
- `~/Desktop/traspaso_etapa2/`;
- ningún archivo cuyo nombre empiece con `NO_ABRIR_`, esté donde esté.

Si una búsqueda (`find`, `grep -r`, `rsync`, un script) puede recorrerlas, las excluye. Si algo de ellas aparece en una salida, lo
declarás en el FRENO, con su ruta y sin copiar su contenido.

## 8. Las decisiones de la autora (15/10/2026, pedido recibido a las 16:17:35; hoja de la mesa, §108)

Tal cual: «tomo las cuatro decisiones del §8 del v3.»
1. **«Los nombres: los de U-SINCOLA-T0 con el sufijo _rs1.»** Se aplica a los cuatro:
   - las claves de `grafos.py`: `KG_Tanda0_Diez_r2b_rs1`, `KG_Tanda0_Desarrollo_r2b_rs1`, `KG_Tanda0_Diez_r2b_sincola_rs1` y
     `KG_Tanda0_Desarrollo_r2b_sincola_rs1`;
   - los labels y los índices fulltext, con el mismo sufijo; los nombres canónicos, con `-rs1`;
   - las carpetas de salida en `corpus_tanda0/`: `ens_diez_r2b_rs1/`, `ens_desarrollo_r2b_rs1/`, `ens_diez_r2b_sincola_rs1/` y
     `ens_desarrollo_r2b_sincola_rs1/`;
   - las entradas de la suite, con el sufijo sobre sus nombres de hoy.
   - Los nombres de los dos completos vienen de U-REEXT-T0, y los de los dos sin cola, de U-SINCOLA-T0. El sufijo es el mismo.
2. **«Se re-sellan los cuatro grafos, completos y sin cola.»**
3. **«Si el diff contra O2 trae algo que no viene de R0, frena.»**
4. **«Las notas a los documentos firmados van en un commit propio, inmediatamente después de los dos del sello.»**

FRENO.

## Firma

FIRMADO por la autora el 15/10/2026 a las 16:40:26 (por mensaje: «Firmo el mandato del re-sellado (9ba837df…) tal como está»; hoja de
ruta de la mesa, §109). El texto firmado es el de arriba, hasta antes de esta sección, y su sha256 es
`9ba837df727beae806a66018984be22ffdc9e4409e7557e1622b82011e44499b` (la versión para firmar de la mesa, `decisiones_108_mesa/resellado/`).
Rige desde esta firma. Se despacha según el orden de las ejecutoras (§1 bis): cuando esté el commit del FRENO S2-b de U-SEG-OFICIAL.
