# B2 de N7c, etapa C2: por qué no escribí el runner

USD 0. Rutas de la copia de trabajo (`copia_head/`: `git archive` de HEAD `75166c72` más `preparado/`), relativas a
`data/experiment/banco_mcp/` salvo aviso. Los siete cambios del paso 2 se pueden hacer como reasignaciones que se leen al llamar
(§2). Con los siete, igual, ninguna sesión de B2 ni del humo llegaría a correr: el lanzador de cada sesión no recibe la configuración
de agentes de la entrada. Arreglarlo es un octavo cambio, fuera de lo autorizado, así que freno con este diagnóstico.

## 1. El obstáculo: la sesión no recibe `--config-agentes`

- **El lote no lo pasa.** `agentes/lanzar_lote_paralelo.py:291-293` arma el comando de cada sesión con `--brazo`, `--id`,
  `--pregunta`, `--out`, `--modo`, `--via`, `--sesiones` y `--timeout-s`, y nada más. El `config_agentes` que le pasa el runner
  (`n6/correr_n6.py:722`, el de la entrada) solo se usa para leer la versión sellada del CLI (`lanzar_lote_paralelo.py:189-192`).
- **El lanzador de N6 se queda con la suya.** `n6/lanzar_agente_n6.py` toma `CONFIG = n6/config_agentes_n6.json` (`:31`) como
  valor por defecto de `lanzar` (`:36`) y de `--config-agentes` (`:58`). Corre en otro proceso, así que una reasignación en el
  proceso de `correr_n7c.py` no le llega.
- **Esa configuración no tiene los brazos de N7c.** Sus brazos son los diez de N6 (`kg_B`, `kg_T`, `kg_T-F1` a `kg_T-F6`,
  `fragmentos_bm25` y `fragmentos_hibrida`). `paralelo/lanzar_agente_n6_prueba.py:79-81` carga la configuración y frena con
  «brazo desconocido» antes de preparar la sesión y antes de escribir su comando (`:110`).
- **Lo que pasaría en B2 y en el humo.** Cada sesión queda «falló el lanzador», sin meta (`lanzar_lote_paralelo.py:331-332`). Sin
  meta y sin comando, correr_n6 la clasifica como de infraestructura, «sin meta», con costo 0 (`correr_n6.py:411-415`); la re-corre
  una vez como `-i2` (`:123`, `:452`) y queda incompleta. Gasto del agente, USD 0, pero 0 sesiones completas: 360 lanzamientos en
  B2 y 4 en el humo, y el juez con 0 respuestas. El humo lo mostraría a USD 0; B2 no serviría.

**La prueba** (`controles/prueba_lanzador_sin_config.py`, salida `controles/prueba_lanzador_sin_config.json`, `3aa5e5ae…`; dos
corridas, iguales byte a byte). Corre sobre la copia, con `subprocess.Popen` del lote, `preparar_sesion` y el `lanzar` de
lanzar_agente_n6 reemplazados por registradores en memoria. No lanza nada:
- el comando que arma `Lote.lanzar` para `kg_N7c` con `n6/lanzar_agente_n6.py` y `config_agentes` `n7c/config_agentes_n7c.json` en
  el lote: 8 opciones, y ninguna es `--config-agentes`;
- leído por el `main` de lanzar_agente_n6, la sesión usaría `n6/config_agentes_n6.json`, sin `kg_N7` ni `kg_N7c`. Control
  positivo: el mismo comando con `--config-agentes` agregado sí cambia la configuración;
- `lanzar_agente_n6_prueba.lanzar` con esa configuración: `SystemExit: brazo desconocido: kg_N7c`, antes de preparar la sesión.

**El precedente.** El seco de N6 se encontró con lo mismo y lo resolvió con un lanzador propio: `n6/seco/lanzar_agente_n6_seco.py`
dice que el lote le pasa solo las entradas de lanzar_agente.py y que por eso fija su configuración ahí (`:2-4`). Llama a
`lanzar_agente_n6.lanzar` tal cual, con `CONFIG_SECO` (`:19`, `:33`), y la entrada seca lo nombra como su lanzador
(`n6/corrida_en_seco_n6.py:156`). En N6 real no hacía falta, porque la configuración de la entrada era la misma que el lanzador ya
tenía fija.

## 2. Los siete cambios: se pueden

Cada uno es una reasignación en su módulo, y el módulo la lee en el momento de la llamada:
1. **Las configuraciones:** la entrada guarda la ruta relativa al banco (`correr_n6.py:269`) y la relee en `:303` y `:317`; el
   valor por defecto de `--config-agentes` se lee al llamar a `main` (`:1007`).
2. y 3. **El Neo4j y el control de las configuraciones:** `main` llama a `precondiciones` por su nombre global (`:1059`).
4. **El tope y el freno:** `cargar_entrada` compara con los globales (`:310`); `main` los toma como valor por defecto al llamarse
   (`:1009-1010`).
5. **La semilla:** `armar_entrada` y `cargar_entrada` llaman a `armar_orden` por su nombre global (`:259`, `:319`).
6. **El contenedor:** `control_memoria_n6.docker` lee `CONTENEDOR` al llamarse (`n6/control_memoria_n6.py:133-134`, `:147`). Hoy
   pasaría: `neo4j-bcra-kg-indices-eval` está `healthy` y la VM de Docker tiene 2.524.311.552 bytes, debajo de 2.684.354.560.
7. **La guarda de otro paso pago:** `guardas_lote_n6` lee `PATRON_PAGO` al llamarse (`paralelo/guardas_lote_n6.py:48`, `:53`);
   la entrada guarda `PATRON_PAGO_REAL` y lo compara (`correr_n6.py:271`, `:305`); el lote y la guarda de la tanda llegan a la
   misma función (`correr_n6.py:99`, `:565-566`; `lanzar_lote_paralelo.py:430`).

## 3. Lo que la mesa tendría que decidir: el octavo cambio

- **(a) Un lanzador de una sesión de N7c** (lo que recomiendo): `n7c/lanzar_agente_n7c.py`, `lanzar_agente_n6.lanzar` tal cual con
  `ruta_cfg = n7c/config_agentes_n7c.json` fija, con la forma de `lanzar_agente_n6_seco.py`. La entrada lo nombra como su lanzador
  (`--lanzador`), con su sha256. Lo que lanza sigue siendo `lanzar_agente_n6.py` (importado sin editarlo), y la meta registra la
  configuración de N7c (`lanzar_agente_n6.py:41`). El humo necesitaría el suyo (o el mismo con la config del humo), porque la config
  del humo es otro archivo. Es un archivo más y no toca el lote de HEAD; es lo que ya hicieron el seco de N6 y el de R5
  (`lanzar_agente_n6_seco.py:4`).
- **(b) Una octava reasignación en `correr_n7c.py`:** `lanzar_lote_paralelo.Lote.lanzar` reemplazado por uno que agregue
  `--config-agentes <la de la entrada>` al comando. La entrada seguiría nombrando `n6/lanzar_agente_n6.py`, más cerca del texto del
  mandato, pero cambia, en el proceso, un método del lote de HEAD que hoy no se toca.

Con cualquiera de las dos, el seco tiene que probar, además de los siete cambios, que cada sesión corre con la configuración de su
entrada.

## 4. Lo demás que encontré, para decidirlo en la misma ronda

Ninguno de estos traba la corrida. Los controles son de lectura y solo con cuentas: `controles/campos_y_marcas.py` (salida
`controles/campos_y_marcas.json`) y `controles/factibilidad_humo.py` (salida `controles/factibilidad_humo.json`).
1. **`config_agentes_b63.json` no trae `R5`** (sus campos: `base`, `brazos`, `claude_code_version_sellada`, `corte_R5`,
   `env_por_sesion`, `fuentes`, `modelo`, `modo_harness`, `por_que`, `prompt`, `sha256_de_cada_archivo` y `unidad`). correr_n6
   exige `R5` igual a la forma de `corte_R5` (`correr_n6.py:260-264`). Armado desde el `corte_R5` de B6.3 da 30, 32 y 1,80, el mismo
   `R5` de `config_agentes_n6.json` y el primero de `R5_ADMITIDOS` (`agentes/lanzar_lote_paralelo_r5.py:54-55`). Propongo
   declararlo así: «sale del `corte_R5` de config_agentes_b63.json».
2. **El lanzador lee también `base`** y la controla por su sha256 (`paralelo/lanzar_agente_n6_prueba.py:44-48`). La de B6.3
   (`a2_2/config_agentes_a2_2.json`) da la suya. Va con las demás, desde config_agentes_b63.json.
3. **La pregunta del humo.** `n7c/c1/b1_n7c_resultado.json` trae solo cuentas, sin ids, así que elegirla exige recalcular la
   sección: NavegadorRel sobre el Neo4j de B6.3, en lectura, con el índice por punto, que no está rastreado. La copia de la C2 no lo
   tiene; la de la C1 sí, regenerado y verificado contra el manifiesto rastreado. Con ese índice, leído en su lugar: de las 17 de
   varios puntos, el techo da 5 y 5, como B1; de las 5 de subtipo `remision`, 4 tienen todas sus anclas en la sección de la primera,
   dentro del tope, y la regla da una pregunta (la primera de remisión por id). El Neo4j quedó igual antes y después (35 consultas,
   todas de lectura). Falta decidir de dónde lee el índice la etapa siguiente: la copia de la C1, en su lugar, o regenerarlo.
4. **Las marcas de ceguera del juez** suman `N7`, `N7c`, `kg_N7` y `kg_N7c` (`correr_n6.py:824`). Ninguna aparece en las 30 de
   N3 (pregunta, criterios y citas): el juez no frenaría por fuga.
5. **El control de memoria con el lote sin codificador vacío.** Las dos configuraciones cargan el codificador, así que el primer
   lote no corre ninguna sesión y no mide ninguna huella. `control_lote_con(1, 0.0)` (`correr_n6.py:660-661`, `:696`) da 4,565 GB
   por sesión y deja pasar si lo fijo llega a 9,935 GB como mucho (`n6/control_memoria_n6.py:71-80`). Es el mismo umbral de P = 1 al
   lanzar (`:39`, `:64-66`), pero sin sumar la huella del CLI, como lo hacía N6. Antes de cada tanda, la guarda usa
   `max(4,565 + 0, lo medido)` (`correr_n6.py:663-665`): desde la segunda tanda, la huella medida.
6. **La lista de la familia 5 de N6** la nombran solo `n6/analizar_n6.py`, `n6/correr_n6.py`, `n6/entrada_n6.json`, la lista y su
   generador. No la nombra ningún archivo de `mcp_kg/` ni de `n7/`. El control por código del mandato queda para el seco.

## 5. Lo que no escribí

`correr_n7c.py`, `config_agentes_n7c.json` y la del humo, las dos entradas, `humo/preguntas_humo_N7c.json`, los controles de los
servidores y del humo, el seco, el análisis y su prueba, los tres comandos y `lista_preparado_241.txt`. `preparado/` tiene solo los
12 archivos de la C1 (paso 1).
