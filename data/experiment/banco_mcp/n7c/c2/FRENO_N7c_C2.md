# FRENO de N7c, etapa C2

29/10/2026. USD 0: ninguna llamada a la API y ninguna sesión real. Del repo leí solo con `git -C <repo> --no-optional-locks`
(`log`, `show`, `diff --name-only`, `status`) y `git archive HEAD`. No escribí en el repo ni en el Neo4j y no commiteé. Rutas con
la carpeta personal como `$HOME`; `R` es `$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg` y la copia es `unav_n7c_c2/copia_head/`
(rutas relativas a `data/experiment/banco_mcp/` salvo aviso). El detalle de cada paso está en `checkpoint_C2.md`.

**Resultado:** pasos 0 y 1 en verde. El paso 2 frena con el diagnóstico (`b2/diagnostico_B2_N7c_C2.md`): los siete cambios se
pueden hacer, pero con ellos ninguna sesión de B2 ni del humo correría. El lanzador del lote no le pasa `--config-agentes` al
lanzador de cada sesión (`agentes/lanzar_lote_paralelo.py:291-293`), y `n6/lanzar_agente_n6.py` usa entonces siempre
`n6/config_agentes_n6.json` (`:31`, `:36`, `:58`), que no tiene los brazos `kg_N7` ni `kg_N7c`. Hace falta un octavo cambio, y el
mandato dice que no lo escriba. **No hay ningún comando PREPARADO.**

## Paso 0

```
pwd: $HOME/INGENIERIA IA/TESIS/fuera_del_repo/unav_n7c_c2   (ls -la: vacía, solo . y ..)
HEAD: 75166c725218a5cc6316a4c9068c5980c0edd1ac  Atribucion de B6.3: el runner sobre el brazo del grafo con la enmienda 1, su prueba, su sello, su corrida y el material de la lectura de la autora
el 238 (75166c72): HEAD mismo, renglón 1 de git log --format=%H
git diff --name-only 75166c72 HEAD: 0 renglones; en banco_mcp/ y neo4j/: 0
git status --porcelain --untracked-files=no, con las vedadas podadas: 0 renglones
sha256 de HEAD (12 primeros), los 19 OK:
  69aab27cc3be n6/correr_n6.py                       2d29389a2c7d n6/lanzar_agente_n6.py
  9f8d6caaef16 n6/config_agentes_n6.json             324b0a97d418 n6/corrida_en_seco_n6.py
  8c0d60e9fb23 n6/control_memoria_n6.py              951cb26d6abb n6/analizar_n6.py
  3d259a712ec1 n6/aplicar_lectura_tolerante_n6.py    21dab67f1450 n6/analizar_n6_con_lectura_tolerante.py
  6287d60f9724 paralelo/guardas_lote_n6.py           2f0074203832 agentes/lanzar_agente.py
  9e9f0ee5b9be n7/config_mcp_kg_n7_evaluado.json     4e3b9ccb062d n7/mcp_kg_n7_evaluado.json
  dd425094a287 n7/n7_configuracion_sellada.json      822aa4e72517 n7/plantilla_prompt_n7.txt
  7ced741bffce n7/bloque_tools_kg_n7.txt             4f4cdac85842 b63/v2/b2/control_neo4j_b63.py
  eaff32bbad93 b63/v2/b2/config_agentes_b63.json     b8d75629322d b63/v2/b2/comando_b63.zsh
  e6759185b0b6 data/experiment/ev2_reporte/code/atribucion_fallas_nav.py
lo de la C1 (8 primeros), los 12 OK:
  1b368333 mcp_kg/familias_nav_rel.py   ab799426 mcp_kg/servidor_mcp_kg_nav_rel.py   4fa93b17 mcp_kg/selftest_familias_nav_rel.py
  41b0a6db n7c/config_mcp_kg_n7c_evaluado.json   13a3ae62 n7c/mcp_kg_n7c_evaluado.json
  1cac0a49 b1/b1_n7c.py   31b6e628 b1/b1_n7c_resultado.json   b10a5a50 b2/diagnostico_B2_N7c_C1.md   91e97154 FRENO_N7c_C1.md
  2dc0d08d pruebas/selftest_familias_nav_rel_corrida1.json   dc5eafba pruebas/mutaciones_selftest_familias_nav_rel.json
  87d8e68f controles/mutaciones_selftest_rel.py
preguntas_N3.json: 6a92d18145e4957f39a0b87d9193a38ca592128c6e248fac0b8d1c9ecd82613b = SHA_PREGUNTAS_N3 (correr_n6.py:107)
Neo4j de B6.3: control_neo4j_b63.py (git show, sin editar) en una copia mínima del scratchpad, NEO4J_URI=bolt://127.0.0.1:47687,
  --huella-esperada 2645da6d…: código 0; kg_meta_sha256 576c9725…, 37.168 nodos, 128.552 aristas,
  huella de estado 4ace5d10…, de contenido 2645da6d…
pgrep -fl 'correr_juez_v3|corrida_cortada_v3|lanzar_agente|servidor_mcp|correr_n6|correr_b63': 0 renglones
procesos con la ruta del repo en su comando: 0; de claude -p, runners o jueces: 0
```

## Los criterios

1. **El paso 0:** arriba, todo como lo pide el mandato.
2. **La copia y su control.** `git archive HEAD` de las seis rutas de la C1 y de los ocho módulos de sus importaciones, con sus
   exclusiones: 2.638 archivos en el tar (2.630 más 8, como la C1), 0 enlaces, 0 vedados. Los tres de `b63/`, con `git show`.
   Encima, `preparado/`, con `cp`: 12 archivos, los de la C1, con los sha256 del paso 0. Control por código
   (`controles/control_copia_c2.py`), al empezar y al cerrar: **2.653 archivos, 0 enlaces, 0 vedados, `preparado/` igual a la copia
   archivo por archivo (12 de 12), 0 archivos de más**, y de `b63/` solo los tres (control positivo: 1 enlace, 4 vedados, 1 distinto
   y 1 de más, sembrados y detectados).
3. **Los siete cambios: FRENO.** No escribí `correr_n7c.py`. Los siete se pueden hacer como reasignaciones que se leen al llamar
   (§2 del diagnóstico, con las líneas). Con ellos, cada sesión frenaría con «brazo desconocido» antes de prepararse
   (`paralelo/lanzar_agente_n6_prueba.py:79-81`). Quedaría «falló el lanzador», con costo 0 y sin meta, y se re-correría una vez sin
   completarse (`correr_n6.py:411-415`, `:123`). La prueba, a USD 0 y sin lanzar nada (`controles/prueba_lanzador_sin_config.py`,
   dos corridas iguales byte a byte, `3aa5e5ae…`): el comando del lote trae 8 opciones y ninguna es `--config-agentes`; la sesión
   usaría `n6/config_agentes_n6.json`; `lanzar` frena con `brazo desconocido: kg_N7c`; y el control positivo, con la opción
   agregada, cambia la configuración. El precedente: el seco de N6 tiene su propio lanzador por esto mismo
   (`n6/seco/lanzar_agente_n6_seco.py:2-4`, `:19`, `:33`). Las dos salidas que veo, para la mesa (§3): **(a)** un lanzador
   `n7c/lanzar_agente_n7c.py` con la configuración de N7c fija, como el del seco de N6 (lo que recomiendo), o **(b)** una octava
   reasignación de `lanzar_lote_paralelo.Lote.lanzar` que agregue la opción. Lo que queda como en N6 no lo declaré en código.
   La familia 5: la nombran solo archivos de `n6/` y ninguno de `mcp_kg/` ni de `n7/` (`controles/campos_y_marcas.json`); el
   control por código del mandato queda para el seco.
4. **Las dos entradas: no** (FRENO en el paso 2). Lo que va a necesitar la del humo ya está visto: la regla de la pregunta da una.
   De las 5 de varios puntos de subtipo `remision`, 4 tienen todas sus anclas en la sección de la primera, dentro del tope, y la
   primera por id es la primera de ellas. El techo de las 17 da el de B1 (5 y 5). Corrió solo en lectura sobre el Neo4j de B6.3, con
   el índice por punto de la copia de la C1 leído en su lugar, y el Neo4j quedó igual (`controles/factibilidad_humo.json`). No elegí
   ni escribí la pregunta.
5. **Los controles de los servidores y del humo: no** (FRENO).
6. **El seco: no** (FRENO).
7. **El análisis: no** (FRENO).
8. **Los tres comandos: no PREPARADOS** (FRENO).
9. **La lista del 241: no**, porque el contenido del commit no está completo. Lo que hay en `preparado/` son los 12 de la C1,
   con su sha256 y su ruta (`controles/preparado_C2.txt`). **0 de las 12 rutas existen en HEAD** (`git show HEAD:<ruta>`; control
   positivo: una ruta de HEAD, detectada).
10. **Iguales antes y después** (`controles/foto_estado.py`, `foto_antes.json` a las 23:30:02 y `foto_despues.json`): HEAD; el
    status con `-uno`, 0 renglones; el status con los no rastreados, el mismo sha256; los 19 de HEAD; `unav_n3/`, 97 archivos, y
    `unav_n7c/`, 3.318, archivo por archivo. El Neo4j: la misma salida del control al empezar y al terminar (huella de estado
    `4ace5d10…`, de contenido `2645da6d…`; la segunda, desde `copia_head/`).
11. **Los tramos de 40 caracteres** (`controles/control_tramos40_c2.py`, el de la C1 con `--excluir`), sobre todo lo que escribí
    (este FRENO incluido), el scratchpad, la transcripción de la sesión y sus salidas guardadas, sin el `git archive` extraído:
    **0 tramos de las preguntas de N3** (control positivo: 1). Contra el texto de los puntos de los 14 TOs, 0 tramos con letras; los
    que coinciden no tienen ninguna letra (blancos y guiones). Resultado en `controles/control_tramos40_final.json`. No hay archivo de
    la pregunta del humo.
12. **El grep de convenciones** (`LC_ALL=en_US.UTF-8 controles/grep_convenciones_c2.py`, el de la C1): **0** en lo que escribí, sin
    contar el propio script, que cita el patrón y la regex de rutas (control positivo: 2). Resultado en
    `controles/grep_convenciones_final.json`.

## Los tres comandos

Ninguno PREPARADO: `n7c/comando_humo_b2_n7c.zsh`, `n7c/comando_b2_n7c.zsh` y `n7c/comando_analisis_b2_n7c.zsh` esperan la decisión
del octavo cambio.

## Decisiones mías, declaradas

- **El intérprete con Neo4j:** el python del `.venv` del repo, con `-B` y `PYTHONDONTWRITEBYTECODE=1`, como en la C1. Es el único de
  la máquina con el driver. Lo usé para el control del Neo4j y para `controles/factibilidad_humo.py`. 0 carpetas `__pycache__` en
  la copia.
- **La copia, sin la E0 ni el índice por punto** que la C1 regeneró: aquí el navegador real no arranca desde la copia.
- **Dos controles de lectura que el mandato no pide**, para que la mesa decida todo en una ronda: `controles/campos_y_marcas.py` y
  `controles/factibilidad_humo.py`, solo con cuentas. Este último lee el índice de la copia de la C1 (solo lectura) y corre 35
  consultas de lectura sobre el Neo4j de B6.3.
- **Docker:** `docker ps`, `docker inspect` (la salud del contenedor de B6.3) y `docker info` (la VM), de solo lectura, para ver si el
  cambio 6 pasaría hoy: `healthy` y 2.524.311.552 bytes, debajo de 2.684.354.560.
- **La transcripción:** el control de los tramos lee la de esta sesión y sus salidas guardadas en `~/.claude/projects/…`, solo en
  lectura, como la C1.

## Errores propios, con su causa

1. En el paso 0, el primer `find` sobre `unav_n7c/` no podó `copia_head/` e imprimió las 3.289 rutas de esa copia, solo los nombres.
   La herramienta guardó esa salida larga en un archivo dentro de `~/.claude/projects/…/tool-results/`, o sea, se escribió algo en
   `.claude/` por un comando mío. La causa: no acoté el `find` antes de correrlo.
2. El primer `ls -la` de la sesión listó la carpeta de arriba (`fuera_del_repo/`), con los nombres de las carpetas vedadas, sin
   entrar en ninguna. La causa: listé para ubicar el repo sin podar las vedadas.
3. En el paso 0, el control del Neo4j falló la primera vez en la copia mínima (`ModuleNotFoundError: harness`), porque no le había
   puesto los ocho módulos que pide `cargar_kg`. Con ellos dio 0. La causa: armé la copia mínima sin la lista de importaciones de la
   C1.
4. Los controles de campos y marcas del paso 2 los corrí primero en la consola, sin archivo. Después los escribí como
   `controles/campos_y_marcas.py`, con su salida. Imprimieron solo cuentas y nombres de campos. La causa: los corrí como exploración
   antes de decidir que iban al diagnóstico.
5. Dos lecturas de la consola salieron con código 1 por un `echo =====`, que zsh toma como una expansión de ruta. No cambió nada. La
   causa: el separador, mal elegido para zsh.

## El paquete

`revision_N7c_C2/`, con `manifest.txt` y nombres únicos, sin el archivo de la pregunta del humo (no existe). La copia con `ditto`
está en `$HOME/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/ef67b34b-12a6-4d09-86e7-7fb4ee3be814/scratchpad/revision_N7c_C2/`.
La verificación de la copia se informa en el mensaje del FRENO.

FRENO: espero la revisión de la mesa y su decisión sobre el octavo cambio (§3 del diagnóstico). El commit 241, el humo y B2 quedan
para después.
