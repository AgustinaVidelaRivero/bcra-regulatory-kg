# FRENO de N7c, etapa C1

29/10/2026. USD 0: ninguna llamada a la API. No escribí en el repo ni en el Neo4j y no commiteé. Rutas con la carpeta personal
como `$HOME`; `R` es `$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg` y la copia es `unav_n7c/copia_head/` (rutas de la copia,
relativas a `data/experiment/banco_mcp/` salvo aviso). El detalle de cada paso está en `checkpoint_C1.md`.

**Resultado:** pasos 0 a 6 en verde. El paso 7 frena con el diagnóstico: el runner de B2 no se puede armar cambiando solo tres
cosas, y desde la copia la corrida real no arranca (`b2/diagnostico_B2_N7c_C1.md`). No hay comando de B2 PREPARADO.

## Paso 0

```
pwd: $HOME/INGENIERIA IA/TESIS/fuera_del_repo/unav_n7c   (ls -la: vacía)
HEAD: 75166c725218a5cc6316a4c9068c5980c0edd1ac  Atribucion de B6.3: el runner sobre el brazo del grafo con la enmienda 1, su prueba, su sello, su corrida y el material de la lectura de la autora
el 238: HEAD mismo, por el título (git log --format='%H %s' | grep -n: renglón 1); «238» no figura en git (grep -c '#238': 0)
git status --porcelain --untracked-files=no, con las vedadas podadas: 0 renglones
sha256 de HEAD (12 primeros), los 17 OK:
  c27bc8882240 mcp_kg/familias_nav.py               b8a2e828314a mcp_kg/familias_nav_cand.py
  78a2dfaf02c4 mcp_kg/servidor_mcp_kg_nav.py        1eaacadb6485 mcp_kg/servidor_mcp_kg_nav_cand.py
  f8b8de7a587c mcp_kg/servidor_mcp_kg.py            9e9f0ee5b9be n7/config_mcp_kg_n7_evaluado.json
  4e3b9ccb062d n7/mcp_kg_n7_evaluado.json           dd425094a287 n7/n7_configuracion_sellada.json
  822aa4e72517 n7/plantilla_prompt_n7.txt           7ced741bffce n7/bloque_tools_kg_n7.txt
  69aab27cc3be n6/correr_n6.py                      d6a5a0a367ee n6/entrada_n6.json
  324b0a97d418 n6/corrida_en_seco_n6.py             9f8d6caaef16 n6/config_agentes_n6.json
  2d29389a2c7d n6/lanzar_agente_n6.py               4f4cdac85842 b63/v2/b2/control_neo4j_b63.py
  e6759185b0b6 data/experiment/ev2_reporte/code/atribucion_fallas_nav.py
preguntas_N3.json: 6a92d18145e4957f39a0b87d9193a38ca592128c6e248fac0b8d1c9ecd82613b = SHA_PREGUNTAS_N3 (correr_n6.py:107)
grafo evaluado (sin rastrear), al empezar: 576c97256185a0d5741cb2c35a2a85e91412f3e1119ad7a85d960b7d60c35ad3 = kg_sha256_esperado
procesos: ninguno de correr_n*, lanzar_agente, claude -p ni runner; ninguno con la ruta del repo; descriptores sobre .git, de lectura
```

## Los criterios

1. **Paso 0:** arriba, todo como lo pide el mandato.
2. **La copia y el Neo4j.** `git archive HEAD` de las seis rutas del mandato, con sus exclusiones: 2.630 archivos. Más lo que
   pidieron las importaciones: `evaluacion/{harness,loader}.py`, `ev2_corrida/code/{comun_ev2,metrica_ev2}.py`,
   `exploracion/validar_anclas.py` y `exploracion/sinteticas/{comun,metrica,resolucion}.py`. Más `control_neo4j_b63.py`, escrito con
   `git show`. Con eso, 0 módulos cargados desde fuera de la copia (`controles/sondeo_imports_v1..v5.json`). Además, el índice por
   punto, que no está rastreado: lo regeneré desde la E0 rastreada que declara su manifiesto (640 archivos) y el grafo evaluado leído
   en su lugar, y los 4 archivos dan, byte a byte, los sha256 del manifiesto rastreado `ef036b67…`
   (`controles/regenerar_indice_puntos_salida.json`). El control de la copia, por código: al cerrar, **3.289 archivos, 0 enlaces, 0
   vedados**, y de `b63/` solo `control_neo4j_b63.py` (`controles/control_copia_final.json`; control positivo: 4 vedados y 1 enlace
   sembrados, detectados). El Neo4j: `NEO4J_URI=bolt://127.0.0.1:47687 control_neo4j_b63.py --huella-esperada 2645da6d…`, desde la
   copia y sin editar, **código 0** (`controles/control_neo4j_b63_salida.json`).
3. **Los `diff`.** `servidor_mcp_kg_nav_rel.py` contra `servidor_mcp_kg_nav_cand.py`: el import de `familias_nav_rel`,
   `VERSION_SERVIDOR = "1.0-nav-rel"` y `FNR.NavegadorRel(` en `abrir_navegador`. `n7c/config_mcp_kg_n7c_evaluado.json`: `"version":
   "1.0-nav-rel"`. `n7c/mcp_kg_n7c_evaluado.json`: el servidor y la ruta de su config. sha256: `familias_nav_rel.py` `1b368333…`,
   `servidor_mcp_kg_nav_rel.py` `ab799426…`, `config_mcp_kg_n7c_evaluado.json` `41b0a6db…`, `mcp_kg_n7c_evaluado.json` `13a3ae62…`.
4. **Las pruebas** (`mcp_kg/selftest_familias_nav_rel.py`; juguete de 51 puntos más el TO y 55 nodos, con un doble del driver): **35
   de 35** en cada corrida, y las dos salidas iguales byte a byte (`2dc0d08d…`). Control negativo: 8 mutaciones en memoria, las 8
   hacen fallar casos.
5. **B1** (`b1/b1_n7c.py`, `b1/b1_n7c_resultado.json`), sobre los 3.194 puntos de los 14 TOs de N3:
   - prefijo **3.194 de 3.194**; lista igual a la calculada aparte desde el kg.json **3.194 de 3.194**. Lo calculado aparte coincide
     con el navegador: 212 contenedores, 376 hubs y las aristas de los siete tipos;
   - remisiones: 3.146 comparables, 2.576 iguales a las de `ver_remisiones` a un salto (1.710 de ellas, las dos vacías);
   - tamaño de la sección: mediana 29 caracteres (10 tokens), p95 652 (235), máximo 1.134 (408); la lista se corta en 41 puntos;
   - **techo en N3: 5 de las 17** de varios puntos tienen todas sus anclas unidas al primer punto, y las 5 dentro del tope.
6. **B2:** no escribí el runner. El diagnóstico, con las líneas, está en `b2/diagnostico_B2_N7c_C1.md`:
   - las tres sustituciones se pueden hacer sin editar `correr_n6.py`;
   - además habría que cambiar el tope y el freno reales, que se exigen de 130 y 100 (`n6/correr_n6.py:114` y `:309-311`), la
     semilla, fijada en el valor por defecto de `armar_orden` (`:115`, `:203`, `:259` y `:319`), y el contenedor de la guarda de
     memoria (`n6/control_memoria_n6.py:41`; el Neo4j de B6.3 es otro contenedor);
   - desde la copia, el servidor no arranca: `BANCO_REPO` sale de la ubicación del lanzador (`agentes/lanzar_agente.py:49-50` y
     `:123`), y la copia no tiene el `.venv` del JSON de MCP, ni el kg.json, ni la matriz densa.

   No escribí la configuración de agentes, la entrada, el seco ni el análisis. **No hay comando de B2.**
7. **Iguales antes y después** (`controles/control_final_despues.txt`): HEAD; el status con `-uno`, 0 renglones; los 17 sha256; los
   ignorados de `mcp_kg/`, los mismos 2; el grafo evaluado, `576c9725…` al empezar y al terminar; `preguntas_N3.json`, el mismo
   sha256, y 0 de los 97 archivos de `unav_n3/` modificados después de las 19:37; el Neo4j, la misma salida del control al empezar y
   al terminar (huella de estado `4ace5d10…`, de contenido `2645da6d…`), y en B1 todas las sesiones fueron de lectura.
8. **Los tramos de 40 caracteres** (`controles/control_tramos40.py`), sobre todo lo que escribí, el scratchpad, la transcripción de
   la sesión y sus salidas guardadas: **0 tramos de las preguntas de N3** (control positivo: 1). Contra el texto de los puntos de
   los 14 TOs: 0 tramos con letras; los únicos que coinciden son 3 tramos distintos sin ninguna letra (líneas de guiones). Resultado
   final en `controles/control_tramos40_final.json`.
9. **El grep de convenciones** (`LC_ALL=en_US.UTF-8 controles/grep_convenciones_n7c.py`): **0** en lo que escribí, sin contar el
   propio script, que cita el patrón y la regex de rutas (control positivo: 2). Resultado final en
   `controles/grep_convenciones_final.json`.

## Decisiones mías, declaradas

- **El índice por punto, regenerado en la copia** (criterio 2): sin él, el navegador no arranca, y no hay otra forma de tenerlo sin
  leer el repo por fuera de git. No regeneré la matriz densa: B1 corre sin el denso, y `ver_punto` no la usa.
- **Los intérpretes:** el python del `.venv` del repo, con `-B` y `PYTHONDONTWRITEBYTECODE=1`, para todo lo que usa Neo4j (es el
  único de la máquina con el driver); el venv 3.12 de `venvs/banco_vector_py312`, solo para sondear el lector de la atribución.
- **La regla de la sección:** un contenedor o un hub, en cualquiera de las dos puntas, no une puntos. Los puntos de un nodo son los
  que lo listan en `puntos.json`, y un punto que no existe da el aviso heredado, sin sección.
- **Lo que dejé igual para que el `diff` muestre solo el cambio:** el docstring del servidor nuevo y la `nota` de la config de N7c,
  que todavía nombran a `servidor_mcp_kg_nav_cand.py`.

## Errores propios, con su causa

1. En el paso 0, un comando hizo `cd` a la carpeta del repo y volvió. No leyó ni escribió nada. La causa: un renglón de prueba que
   quedó en el comando.
2. En el paso 0 corrí `lsof +D` sobre `.git` del repo, para ver si había escritores. Lee metadatos de archivos fuera de git (no su
   contenido). La causa: elegí esa herramienta sin pensar en la regla.
3. Imprimí en mi consola la contraseña por defecto del Neo4j local, que está en `data/experiment/neo4j/conexion.py`: hice un grep
   que incluía los renglones con `environ`, que traen esos valores por defecto. No quedó escrita en ningún archivo. La causa: un
   patrón de búsqueda demasiado amplio.
4. En el archivo de control escribí primero «46 puntos» para el juguete. Al recontarlo en sus archivos dio 51 más el TO, y lo
   corregí antes de cerrar. La causa: escribí la cuenta sin recomputarla (regla i).
5. No tomé al empezar una foto completa de `unav_n3/`, solo el sha256 de `preguntas_N3.json`. Para compensarlo controlé al cerrar
   ese sha256 y que ningún archivo de la carpeta tuviera fecha de modificación posterior al inicio de la sesión.
6. En B1, el driver imprimió 9.362 avisos 01N52 en la consola (propiedades de arista que el grafo no tiene, de la consulta heredada
   de `ver_punto`). Traen el texto de la consulta y no datos. La causa: no apagué las notificaciones del driver.

## El paquete

`revision_N7c_C1/`, con `manifest.txt`. La copia con `ditto` está en
`$HOME/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/21c32730-0a93-4b1c-8e0a-4eb3bd60978f/scratchpad/revision_N7c_C1/`.
Verificación de la copia, sin este FRENO: 33 de 33 sha256 del manifiesto. El FRENO se agrega después al paquete y al manifiesto;
esa segunda pasada se informa en el mensaje del FRENO.

FRENO: espero la revisión de la mesa. B2 queda para después de que la mesa decida lo del §4 del diagnóstico.
