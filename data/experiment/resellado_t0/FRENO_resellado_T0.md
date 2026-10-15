# Re-sellado único de los grafos r2b de la tanda 0 — FRENO (15/10/2026; USD 0, sin API; sin commit)

**Entrada.** Mandato `docs/mandatos/URESELLADO_T0_resellado_unico_grafos_r2b.md`, leído en `67fe5b14`: el texto firmado (líneas 1 a
254, antes de «## Firma») da `9ba837df727beae806a66018984be22ffdc9e4409e7557e1622b82011e44499b` en el commit y en el árbol. HEAD
`96d7d1ab`. Salida completa del paso 0 y de las precondiciones: `salidas/paso0_y_precondiciones.txt`
(`scripts/paso0_precondiciones.sh`). Comandos, en el orden en que corrieron: `scripts/comandos_resellado_t0.sh`.

## Paso 0 (§1 y §1 bis)

```
$ pwd
$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg
$ git rev-parse --abbrev-ref HEAD
main
$ git log --oneline -3
96d7d1ab Segmentacion oficial: la segunda parte de la etapa siguiente, revisada, con las cifras y lo abierto decidido
5f02ace4 Alcance de la primera tanda: el sucesor entra con el rol reutilizado de su regimen
67fe5b14 Grafos de la tanda 0: el mandato del re-sellado unico, firmado
$ git log --format=%s -5
Segmentacion oficial: la segunda parte de la etapa siguiente, revisada, con las cifras y lo abierto decidido
Alcance de la primera tanda: el sucesor entra con el rol reutilizado de su regimen
Grafos de la tanda 0: el mandato del re-sellado unico, firmado
Evaluacion final: la cuota de preguntas de varios puntos, el gold del juez en dos mitades y el orden de las ejecutoras
Evaluacion final: el mandato de la comparacion con fragmentos firmado, y las reglas de las preguntas y del juez
$ git status --porcelain -- data/experiment/segmentacion_oficial_e0r2/s2
(vacío)
$ git status --short -- data/experiment/tanda0 data/experiment/reextraccion_v2/corpus_v2 scripts data/experiment/neo4j
(vacío)
```

El primero de los cinco es el commit del FRENO S2-b de U-SEG-OFICIAL y `s2/` no tiene cambios: ninguna otra ejecutora escribía.

## Precondiciones a–e: las cinco pasan

- **a.** `ded41d50`, `1d690df3` y `2d0f5277` están en la historia de HEAD; `git diff --stat ded41d50 HEAD` sobre las ocho rutas del
  §1.a da vacío.
- **b.** `git diff --quiet 9f6361e HEAD -- …/salida_tanda0_r2b/`: rc 0; 57 archivos rastreados.
- **c.** Los cuatro sellados dan `a9631a64…`, `6e756043…`, `e22fae1a…` y `2922b72d…` en el árbol y en `bbc38dc` y `dde9f44`; cada sha
  está una vez en `grafos.py` y una vez en la fixture; `git status` de sus cuatro carpetas, vacío.
- **d.** Los 23 `*.jsonl` de `salida_r2b/{ext,docvig}/` son los de `2d0f5277`, y los 8 del anexo dan el sha256 entero que declara R0
  (`r0/corrida/anexo_r0.json`).
- **e.** `git status --short` vacío en `tanda0/`, `corpus_v2/`, `scripts/` y `neo4j/` (arriba).

## Cómo trabajé

- **Ningún generador corrió sobre el repo.** Todo corrió sobre una copia hecha con el `rsync` de la cláusula, más
  `--exclude=/data/experiment/neo4j/volumen` (la base de Neo4j, que no es insumo de nada que corra en la copia). En la copia: 0
  archivos de entorno o `NO_ABRIR_`, 0 enlaces y 0 `.pyc`; 22.037 archivos, igual a la foto del repo menos lo excluido, byte a byte
  (`salidas/control_copia_vs_foto_antes.json`: excluidos `.venv` 27.758, `__pycache__` 243, enlaces 336, `.DS_Store` 12, volumen 181 y
  8 registrados sin abrir).
- Dos variantes de control, como clones de la copia: **sin R0** (los 8 archivos del anexo en su versión de `1d690df3`) y **sin O2**
  (además, los 10 archivos de código de `ded41d50` en su versión de `ded41d50^`).
- El repo recibió después los mismos bytes, archivo por archivo, con control previo (cada archivo que cambia es el de HEAD; cada ruta
  nueva no existía) y posterior (275 de 275 iguales a la copia; `scripts/escribir_en_el_repo_rs1.py`, `salidas/escrituras_en_el_repo.json`).
- La excepción es Neo4j: su base vive en `data/experiment/neo4j/volumen/` (fuera de git). El cargador corrió desde la copia.
- `PYTHONDONTWRITEBYTECODE=1` y `-B` en todo; `ANTHROPIC_API_KEY` sin definir en las cadenas.

## Las cadenas (§2.1)

| grafo | sellado | antes de O2 (repro.) | O2 (repro.) | re-sellado, dos corridas | nodos / aristas |
|---|---|---|---|---|---|
| diez | `a9631a64` | `40c54830` | `710664e9` | `fda6c07d` | 8.788 / 27.430 |
| diez sin cola | `e22fae1a` | `8d747e57` | `a50210b4` | `61dd1b69` | 8.491 / 25.976 |
| desarrollo | `6e756043` | `6e756043` | `18a2747d` | `acb26dca` | 6.962 / 23.311 |
| desarrollo sin cola | `2922b72d` | `2922b72d` | `9f49d62d` | `66e745f5` | 6.711 / 21.996 |

- sha256 enteros: diez `fda6c07dbb95602f5992f7e1ad9bf148ff1c2a72b9f69ff2ebbce891c15740ea`, desarrollo
  `acb26dca0885e9ea83ab02637f15c1dac57885f0cf017c5fb16173ac7dfcac31`, diez sin cola
  `61dd1b69ba03e40499845c40a6a8bec4c22d892ebe95823c7d5a569110f08738`, desarrollo sin cola
  `66e745f57397ab754cde09eb641e9f0d9ef6259ea7e6445d086ecbf1c36dcc6c`.
- **r2a, byte a byte:** `70d51e42…` y `fa4c1043…`.
- **Doble corrida:** la segunda, en otro proceso, da los mismos 36 (diez) y 26 (desarrollo) archivos byte a byte, salvo
  `reporte_ensamblado_r2.json`, que guarda las rutas de su salida y de la raíz (igual con las rutas normalizadas); la doble corrida
  interna del ensamblado da `true` en todas (`salidas/doble_corrida_rs1.json`, `salidas/cadenas_sha256_rs1.tsv`).
- **O2 y la línea de base de O2, reproducidas byte a byte** con los manifiestos `_rs1`: el nombre del manifiesto no entra en el
  `kg.json`. Entre O2 y el re-sellado cambia solo la entrada de R0.
- Las 20 unidades de R0 (los renglones anexados a `finales.jsonl`) son la lista sellada de O3 (`cc6b0cd6…`; `salidas/unidades_r0.json`).

## El diff contra O2 (§2.2): todo viene de R0

`salidas/diff_contra_O2/diff_declarado_contra_O2_<grafo>.json`, en el formato de O2, más `unidades_r0` y `via` por fila. **0 filas sin
causa en los cuatro, y ninguna que no venga de R0: no hay freno por la decisión 3.**

| | filas | nodos sale / entra / cambia | aristas sale / entra / cambia | regla: procedencia / extremo |
|---|---|---|---|---|
| diez y desarrollo (cada uno) | 541 | 60 / 35 / 22 | 262 / 135 / 27 | 527 / 14 |
| los dos sin cola (cada uno) | 565 | 60 / 51 / 6 | 258 / 189 / 1 | 551 / 14 |

- «procedencia»: el objeto tiene procedencia en una unidad de R0, en uno de los dos grafos. «extremo»: las 14 son `remite_a` que
  salen, desde nodos ajenos a R0 hacia destinos anclados en `ext::3.3.3.1`, `3.3.3.2`, `3.5.6.2` y `3.5.6.7`, que cambian de id.
- Tienen filas 19 de las 20 unidades en los completos (todas menos `docvig::3.3.2`) y 18 en los sin cola (tampoco `ext::3.18.1.1`, que
  sigue en la cola). Los 22 nodos que cambian en diez: 17 pierden la marca de la cola (uno, además, cambia su procedencia); 2 la
  conservan y cambian la lista de unidades de la marca (`cola_chunks`); 2 cambian solo su procedencia y 1 su descripción. Todos tienen
  procedencia en R0.

## El diff contra los sellados (§2.3)

`salidas/diff_contra_sellado/diff_declarado_contra_sellado_<grafo>.json`: cada fila con `causas_por_campo`, el paso de la cadena que
cambió cada campo: «R2-3», «O2:<grupo>» (el de la fila de `omisiones_cod/o2/salidas/diff_declarado_<grafo>.json`) o «R0». **0 sin causa.**

| | filas | solo O2 | solo R0 | O2 y R0 | solo R2-3 |
|---|---|---|---|---|---|
| diez | 12.385 | 11.833 | 539 | 2 | 11 |
| diez sin cola | 11.457 | 10.881 | 563 | 2 | 11 |
| desarrollo | 11.336 | 10.795 | 539 | 2 | 0 |
| desarrollo sin cola | 10.462 | 9.897 | 563 | 2 | 0 |

**Contradicción con el mandato (CLAUDE.md §4.d):** el §2.3 dice «por causa: O2 … o R0», pero en diez hay una tercera, R2-3 (`803623a`):
los sellados de diez no la tienen y la línea de base de O2 sí (`FRENO_O2.md`, «Línea de base»). Son 11 filas en cada grafo de diez (un
propuesto que entra, un Sujeto que cambia de procedencia, 4 `aplica_a` que cambian de destino y 1 `padre_sugerido`), las mismas que
`omisiones_cod/o1/salidas/diff_a9631a64_vs_head_diez.json`. Las declaro con su causa.

## La cola (§2.4)

- **De 74 a 69 de 2.439** unidades de la E0 (`finales.jsonl` tiene 2.440 entradas: `cap::4.2.1.2` va en dos partes). Por estado, de 43,
  29 y 2 a 42, 25 y 2. **Salen 5 y no entra ninguna:** `ext::2.6.1.1`, `ext::3.5.6.1`, `ext::3.6.1.1` y `ext::3.6.4.2` (de `cola_humana`)
  y `ext::3.13.1.10` (de `cola_humana_veredicto_inutilizable`); todas quedan aceptadas.
- **Los grafos dan lo mismo:** el sin cola de diez descarta 69 y el de desarrollo 54, iguales a la lista de `finales.jsonl`; en los
  completos llevan la marca 317 nodos y 385 aristas (diez, 69 unidades) y 264 y 312 (desarrollo, 54). `salidas/cola_y_poblacion_rs1.json`.

## Shapes, suite, `grafos.py` y la vista (§3.1 a §3.3)

- **Shapes** (perfil r2, fase r2b, con `--registro-dir`, `--excepciones` y `--e0`): PASA en los cuatro, 22 PASS, 2 FAIL y 4 WARN, 0
  bloqueantes en FAIL. **Ninguna shape cambia de resultado** contra O2 ni contra los sellados; cambian solo conteos
  (`salidas/tablas_gate_rs1.json`).
- **Suite:** 68 ítems; 3 regresiones, las declaradas de siempre (RT-C5-3, RT-C6-1, RT-C6-2); **0 regresiones nuevas**; ningún ítem
  cambia de estado contra O2 ni contra los sellados (diez 48/11/9, desarrollo 45/11/12). LN-6 da «resuelto», como el sellado y O2; el
  «persiste» de O2 era el del grafo con el código de antes de O2. `selftest_regression_kg` 184/184 en dos corridas (las salidas
  difieren solo en el orden de impresión de un conjunto, renglón 1); `selftest_shapes_congelado` 84/84.
- **Fixture** (`scripts/editar_fixture_grafos_rs1.py`, +1.696/−0 renglones): cuatro entradas nuevas al final, copias de su entrada
  sellada con las expectativas sin cambiar, el `kg`, el `kg_sha256` y el `registro_dir` nuevos: `KG-Tanda0-Diez-r2b-rs1`,
  `KG-Tanda0-Desarrollo-r2b-rs1`, `KG-Tanda0-Diez-r2b-sincola-rs1` y `KG-Tanda0-Desarrollo-r2b-sincola-rs1`. Las selladas, iguales
  (texto canónico).
- **`grafos.py`** (+62/−0): `KG_Tanda0_Desarrollo_r2b_rs1`, `KG_Tanda0_Diez_r2b_rs1`, `KG_Tanda0_Desarrollo_r2b_sincola_rs1` y
  `KG_Tanda0_Diez_r2b_sincola_rs1`, con label, índice fulltext (`nodos_fulltext_kg_tanda0_<…>_rs1`) y `ev2_key` propios, nombre canónico
  con `-rs1` y `commit_sellado` «PENDIENTE». Las selladas, iguales.
- **La vista:** `registro_vista_r2b_rs1.py`, con el patrón de `sincola_t0/registro_vista_r2b_sincola.py`. Su desglose de «punto sin
  nodos»: diez sin cola, 212 de 540 irresolubles del registro, 0 con destino en una unidad excluida, 212 netas (completo: 213, 0, 213);
  desarrollo sin cola, 174 (completo: 175). El 0 es K de O2: esas citas ya tienen su causa propia, `destino_en_unidad_excluida`.
- **Corrida en seco** (`scripts/dry_registro_rs1.py`, por el camino de imports del cargador): OK (`salidas/dry_registro_copia.json`).

## Neo4j (§3.4)

- Docker Desktop no corría: lo abrí, levanté el contenedor del repo (`docker compose up -d --wait`), cargué y, al terminar, detuve el
  contenedor y cerré Docker Desktop. Al abrirse, Docker levantó por su cuenta contenedores de otros proyectos de la máquina; no los
  toqué y se detuvieron al cerrarlo.
- `cargar_neo4j_tanda0.py --grafo <clave> --out-dir …/salidas/neo4j/<clave>`, una vez por grafo, con el control del sha antes de
  cargar. **Gate 5 OK en los cuatro:** dos cargas con la misma huella, conteos iguales, 0 aristas colgantes, 0 hacia otro grafo,
  `KG_Meta.kg_sha256` igual al archivo (con `commit_sellado` «PENDIENTE») y paridad cargador = Neo4j en los 147 casos donde rige.
- `control_cola_neo4j_rs1.py`: **0 nodos con la marca de la cola en los dos sin cola**; en los completos llegan las 317 y 264 marcas.
- Observación: en Neo4j, el `KG_Meta` de los dos sin cola de U-SINCOLA-T0 sigue con `commit_sellado` «PENDIENTE» (se cargaron antes de
  su sello). Con los cuatro nuevos va a pasar lo mismo después del segundo commit, salvo que se recarguen.

## Los controles del §4 (`salidas/controles_s4_rs1.json`, salvo donde se dice)

- **U-CONF-MATRIZ:** 59 de las 60 aristas leídas siguen en `61dd1b69…` con los mismos extremos. **F49 no:** es de `ext::3.16.2.1`,
  unidad de R0 aceptada tras un reintento nuevo con otra extracción; ya no están ni su origen ni su destino (la unidad pasa de 7 a 10
  `condicion_de` hacia una Potestad, que es otro nodo). Ninguna sale por el retiro de → Potestad.
- **Pre-registro de tripletas:** el sha que habilita el sorteo de la etapa V es `66e745f5…` (KG-Tanda0-Desarrollo-r2b-sincola-rs1),
  una vez sellado. No lo corrí.
- **Laudo B2.4:** en los puntos de los ocho patrones (la consulta del control o de T3, con `ext::7.9.6` para BKL-0015) **ninguna arista
  de sujeto se mueve** de `a9631a64…` al re-sellado, y las de los tres límites siguen: 3, 2 y 1. Fuera del punto del patrón, en
  `ext::7.9.4`, O2 (f′) lleva 4 `aplica_a` del propuesto «la entidad» al rol colectivo de Exterior. El laudo recibe la nota del §6 con
  esto.
- **Enmienda 7, §1.5:** A3r del selftest de claves, OK (1.034 ítems ajenos a R0 ausentes, las 20 de R0 y los 1.386 no ítems presentes;
  A3r_v1 y A3r_v2 dan DISCREPANCIA, como deben); VEREDICTO OK, y su JSON es byte a byte el del repo (`salidas/selftests/`). El control
  lee las salidas de E1 y E3 y las bases, que son la entrada de los grafos, no el `kg.json`. Población de U-LECTURA-ACEPTADAS: 2.371
  (1.008 ítems y 1.363 no ítems). Cola: arriba. Línea de base del pre-registro de la tanda 1: **74 de 2.439** en r2b y **69 de 2.439**
  en el grafo re-sellado. Las notas de `docs/insumos_escritura.md` §7 (ítems 4 y 6) no están entre mis escrituras: quedan PENDIENTES.
- **Condición 10:** pasa en los cuatro, igual que en los sellados (la Excepcion de `cla::5.1.1.1`; `5.1.1.1` y `5.1.1.2` por la
  jerarquía; X17 con 2 `remite_a` hacia `cla::3.7`).
- **Figuras** (`salidas/figuras_rs1.json`): los cuatro generadores que citan los sha sellados, corridos sobre clones de la copia,
  reproducen las figuras commiteadas byte a byte con los sellados y también con los re-sellados (la 4.5, además, con el de desarrollo).
  **Ninguna figura cambia**; sus cuatro LEEME reciben la nota.
- **Tablero de correcciones, condición 4:** va en su unidad. Los sha quedan arriba.

## Las notas del §6

`git grep -l -E 'a9631a64|e22fae1a|6e756043|2922b72d' -- docs scripts data/experiment/neo4j` da hoy 32 archivos: los 31 del mandato y
el mandato mismo.
- **Con nota fechada al final, en el formato de su última nota (16 firmados):** enmienda 1 al pre-registro de tripletas, enmienda 5,
  laudo B2.4, laudo D-f, pre-registro de tripletas, protocolo de los dos grafos y los mandatos de A2.1, U-APLICA-ROL-ALCANCE,
  U-CASI-DUPLICADOS, U-CONF-MATRIZ, U-LECTURA-ACEPTADAS, U-OMISIONES-COD, U-REEXT-T0, U-RERESOL-CAT, U-SINCOLA-T0 y U-UNION-ESTRECHA.
  Lo anterior a la nota queda byte a byte igual. Más los 4 LEEME de las figuras (§4). Texto de cada una: `salidas/notas_s6_rs1.json`.
- **Sin nota:** el laudo de la release r2, que es BORRADOR y tiene «A COMPLETAR» en la fila de estos grafos (`:40`); la fe de erratas
  de la forma A («aprobada», no firmada); `insumos_escritura.md`, `plan_tesis.md`, `tablero.md` y `tablero_correcciones.md`, que no
  están firmados; los tres generadores de figuras (código); `grafos.py` y la fixture (solo entradas nuevas); y este mandato.

## Escrituras (todas sin commit)

- Nuevas: `reextraccion_v2/manifiestos/tanda0_ens_{diez_r2b,desarrollo_r2b,diez_r2b_sincola,desarrollo_r2b_sincola}_rs1.json`;
  `corpus_tanda0/ens_{diez_r2b,diez_r2b_sincola,desarrollo_r2b,desarrollo_r2b_sincola}_rs1/` (el ensamblado y las salidas del gate);
  esta carpeta.
- Cambian: `scripts/regression_kg_esperado.json` y `data/experiment/neo4j/grafos.py` (solo entradas nuevas), y los 20 documentos con nota.
- **Para los commits de la autora (PENDIENTES), por la decisión 4:** el primero lleva todo salvo los 20 documentos con nota; el segundo
  pone su hash en el `commit_sellado` de las cuatro entradas nuevas de `grafos.py`; el tercero, los 20 documentos con nota
  (`salidas/notas_s6_rs1.json` los lista). No preparé mensajes de commit.

## Para la autora y la mesa

1. La tercera causa del §2.3 (R2-3), arriba.
2. F49 de U-CONF-MATRIZ: sale por R0. El mandato de U-CONF-MATRIZ dice que la cifra no se recalcula salvo que cambie el resultado del
   criterio; eso queda para la autora.
3. Las notas: interpreté que «el material sellado de U-SINCOLA-T0 y de O2» son sus salidas y sus carpetas, así que sus mandatos
   firmados reciben la nota; este mandato no la recibe. El borrador del laudo de la release r2 necesita los cuatro sha en su
   «A COMPLETAR». Para `insumos_escritura.md` §7, ítems 4 y 6, las cifras están arriba (cola 74 → 69; población 2.371).
4. Los nombres de la suite: tomé el sufijo como `-rs1`, el de los nombres canónicos, porque las entradas de la suite se llaman como
   ellos.
5. Los reportes de los generadores (`reporte_ensamblado_r2.json`, y los `.md` y `.json` de shapes y suite) guardan la ruta absoluta de
   la copia donde corrieron, en los mismos campos en que los sellados guardan la del repo. No los edité. En mis salidas auxiliares de
   esta carpeta, las rutas van como `<SCRATCHPAD>` y `<REPO>`.

## Errores propios, con su causa

1. **El control de la precondición d** mostró «declarado: False» en mi primera corrida: el script comparaba el sha entero declarado
   con 16 caracteres. Lo rehíce con el sha entero: los 8 coinciden.
2. **El diff contra los sellados** dejó primero 156 filas sin causa en diez: mi script seguía los nodos que G-r cambia de id a través
   del cambio, y no veía el paso. Ahora la presencia se mide sobre la clave literal; quedan 0.
3. **Las notas, primera versión** (solo en la copia): el título repetía «re-sellado único» y la nota del LEEME de 4.5 nombraba el grafo
   de desarrollo sin haberlo probado. Restauré los 20 archivos desde HEAD en la copia, corrí la 4.5 también con el de desarrollo y volví
   a aplicar. Al repo llegó solo la versión final.
4. **`salidas/cola_y_poblacion_rs1.json`** salió de la versión del script anterior a un ajuste: en los completos, el campo
   `descartadas_igual_a_la_cola_de_sus_tos` daba `false` donde no aplica. Lo regeneré con el script vigente (cambia solo ese campo, a
   `null`) y lo actualicé en la copia y en el repo después de la escritura; `salidas/escrituras_en_el_repo.json` guarda el sha anterior
   de ese archivo, y el control final, el nuevo.
5. **Un desglose de este FRENO no cerraba** en el borrador: puse «16» nodos que pierden la marca de la cola, de memoria. Al
   recontarlo contra el diff son 17, y el resto se reparte en 2, 2 y 1 (22). Lo corregí antes de cerrar.

## Cierre

La foto del repo después, su comparación con la de antes, los `.pyc`, el grep de convenciones y el paquete van en el mensaje del FRENO:
este archivo entra en la foto. Nada commiteado, ningún mensaje de commit preparado y nada escrito en la memoria.

**FRENO.**
