# B2 de N7c: por qué no escribí el runner

USD 0. Rutas de la copia de trabajo (`copia_head/`, `git archive` de HEAD `75166c72`), relativas a `data/experiment/banco_mcp/`
salvo aviso. Las tres sustituciones que pide el mandato se pueden hacer sin editar `correr_n6.py`. El runner, aun así, tendría que
cambiar más cosas que esas tres, y la corrida real no podría arrancar desde la copia sin copiar más piezas. Las dos cosas están
fuera de lo autorizado, así que freno con este diagnóstico.

## 1. Las tres sustituciones: se pueden

- **Las configuraciones:** `armar_entrada` recibe la configuración de agentes como argumento (`n6/correr_n6.py:255`, y `--config-agentes`
  en `:1007`), pero guarda su ruta relativa a la carpeta del banco (`:269`, `config_agentes.relative_to(BANCO_DIR)`; `cargar_entrada`
  la relee en `:303` y `:317`). Por eso `config_agentes_n7c.json` tendría que vivir en la carpeta del banco de la copia (p. ej. en
  `n7c/`), no en la raíz de `unav_n7c/`.
- **El Neo4j y el control de las configuraciones:** los dos están en `precondiciones` (`:337-365`: `armar_configuraciones_n6` en `:340-346`
  y `control_neo4j_n6` en `:347-356`). `main` la llama por su nombre global (`:1059`), así que `correr_n7c.py` podría reemplazar
  `correr_n6.precondiciones` por una propia: sha256 de los archivos de N7 y de N7c, `control_neo4j_b63.estado` con la URI y la huella
  del paso 1, y la extracción y el otro paso pago como en N6 (`:357-364`).

## 2. Lo que, además, habría que cambiar

1. **El tope y el freno.** La entrada real exige USD 130 y 100 de N6: `TOPE, FRENO = 130.0, 100.0` (`:114`), y `cargar_entrada` frena
   con el código 8 si la entrada trae otros (`:309-311`). Con USD 25 y 20, la corrida real frenaría al cargar la entrada. Para evitarlo
   hay que reasignar `correr_n6.TOPE` y `correr_n6.FRENO`: una cuarta sustitución.
2. **La semilla del orden.** `armar_orden(ids, cfg_agentes, semilla=SEMILLA_ORDEN)` (`:203`) fija el valor por defecto al definirse la
   función, con `SEMILLA_ORDEN = "N6:orden_corridas:v1"` (`:115`). `armar_entrada` (`:259`) y `cargar_entrada` (`:319`) la llaman sin
   semilla. Reasignar `SEMILLA_ORDEN` no alcanza: para que la entrada lleve `N7C:orden:v1` hay que reemplazar `armar_orden` o sus
   `__defaults__`. Sería una quinta sustitución.
3. **El contenedor que controla la guarda de memoria.** `control_memoria_n6.CONTENEDOR = "neo4j-bcra-kg-n6"` (`n6/control_memoria_n6.py:41`).
   `docker()` controla la salud de ese contenedor (`:127-148`), y `correr_agente` frena con el código 14 si no está sano, al lanzar
   (`n6/correr_n6.py:667-678`) y antes de cada tanda (`:573-581`). El Neo4j de B6.3 es `neo4j-bcra-kg-indices-eval` (`docker ps`, el
   único levantado). O se cambia `CONTENEDOR` (una sexta sustitución), o hay que tener levantado el contenedor de N6, que B2 no usa.
4. **La guarda de otro paso pago** solo reconoce `correr_n6.py` (`paralelo/guardas_lote_n6.py:34-35`). Una segunda corrida de
   `correr_n7c.py` no la haría frenar. No impide correr, pero queda por debajo de la guarda de N6.

## 3. La corrida real no arranca desde la copia

`correr_n7c.py` importaría `correr_n6` de la copia. El lanzador calcula entonces la raíz del repo desde su propia ubicación
(`agentes/lanzar_agente.py:49-50`, `REPO_DIR = BANCO_DIR.parents[2]`, que es `copia_head/`) y se la pasa a cada sesión como
`BANCO_REPO` (`:123`). Con eso, el servidor del grafo de las dos configuraciones no llega a arrancar:

- el intérprete del JSON de MCP es `${BANCO_REPO}/.venv/bin/python` (`n7/mcp_kg_n7_evaluado.json:6`, el mismo en N7c), y la copia
  no tiene `.venv`. La regla l prohíbe enlazarlo, y copiarlo es copiar más que esas piezas;
- `servidor_mcp_kg.abrir_backend` controla el sha256 del kg.json en la ruta de `GRAFOS` (`mcp_kg/servidor_mcp_kg.py:85`;
  `data/experiment/neo4j/grafos.py:367` y `:391-394`), que bajo la copia no existe. El mandato prohíbe copiarlo;
- la config pide el denso (`denso.requerido: true`). El navegador carga entonces `embeddings_docs.npy` y controla su sha256
  (`mcp_kg/familias_nav.py:242-247` y `:337`). La matriz no está rastreada; regeneré los cuatro JSON del índice, iguales byte a
  byte, pero la matriz sale de correr el modelo denso y nada asegura que dé el mismo sha256.

Cada sesión quedaría como «un servidor MCP no llegó a connected» (`n6/correr_n6.py:432-433`), es decir, como falla de
infraestructura, con un reintento y después incompleta. Desde el repo tampoco sale: ahí están `.venv`, el kg.json y el índice, pero
no los archivos nuevos de N7c (`mcp_kg/familias_nav_rel.py`, `mcp_kg/servidor_mcp_kg_nav_rel.py`, `n7c/*.json`), porque no escribo
en el repo.

## 4. Lo que la mesa tendría que decidir

- Si `correr_n7c.py` puede cambiar, además de las tres, el tope y el freno, la semilla (`armar_orden`), el contenedor de la guarda de
  memoria y, si lo quiere, el patrón de la guarda de otro paso pago.
- Desde dónde corre B2: desde el repo, con los archivos de N7c commiteados antes por la autora (en ese caso `correr_n7c.py` importaría
  `correr_n6` del repo, no de la copia), o desde una copia que tenga el entorno del servidor, lo que hoy prohíben la regla l y el
  mandato.

Mientras esto no se decida, no escribí `correr_n7c.py`, `config_agentes_n7c.json`, la entrada, el seco, el comando ni el análisis.
