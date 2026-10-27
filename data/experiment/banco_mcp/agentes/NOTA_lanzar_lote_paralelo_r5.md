# NOTA — `lanzar_lote_paralelo_r5.py` en el runner de B6.3 (U-BANCO-R5-a)

Escribo esta nota para la etapa b del runner (`b63/correr_b63.py` y `b63/comun_b63.py`). No edito ninguno de los dos: digo qué
llamada cambia y por qué. Las líneas citadas son las de HEAD `a9636f37`.

## 1. Qué es el lanzador r5

`agentes/lanzar_lote_paralelo_r5.py` importa `agentes/lanzar_lote_paralelo.py` de HEAD sin editarlo. Lo llamo BASE. Sobre él
cambia tres cosas:

- **R5.** Lo toma de la entrada sellada: `entrada` (la ruta) y `sha256_entrada`, con la clave «R5», el campo que
  `comun_b63.cargar_entrada` exige y lee (`comun_b63.py:112` y `:155`). Admite solo los dos R5 del pre-registro
  (`R5_ADMITIDOS`):
  - A: `{"tope_tool_calls_prompt": 30, "max_turns": 32, "max_budget_usd": 1.8}`;
  - B: `{"tope_tool_calls_prompt": 45, "max_turns": 47, "max_budget_usd": 3.3}`.

  Con otro R5, `Lote.correr()` devuelve el 5 (`AISLAMIENTO`) sin lanzar ninguna sesión y deja escrito el registro. Una sesión
  cuyo R5 no es el de la entrada también frena con el 5: lo hace el control de `BASE.Lote.control_aislamiento`, con el R5 de la
  entrada en lugar de `BASE.R5_ESPERADO`.
- **`presupuesto_sesion`.** Sale del `max_budget_usd` del R5 de la entrada. Si se pasa uno distinto, el lote no se arma: el
  constructor levanta `SystemExit` con texto.
- **La guarda de otro paso pago.** Es `paralelo/guardas_lote_r5.py`: el patrón de `guardas_lote.py` más `correr_b63\.py`, con
  el mismo filtro. `BASE.G` pasa a ser ese módulo en el proceso que importa el lanzador r5.

Una entrada que no existe, que no da su sha256 o que no trae R5 también levanta `SystemExit` con texto en el constructor.

## 2. Lo que cambia en `b63/correr_b63.py`

1. **Imports (`correr_b63.py:65-66`).**

   ```python
   import lanzar_lote_paralelo_r5 as LOTE       # en lugar de lanzar_lote_paralelo
   import guardas_lote_r5 as G                  # en lugar de guardas_lote
   ```

   El lanzador r5 re-exporta los nombres de BASE que usa el runner: `LA`, `ahora`, `cli_del_path`, `LOTE_INVALIDO` y los demás
   códigos, y `Lote`. Las carpetas `agentes/` y `paralelo/` ya están en el `sys.path` del runner (`:60-62`). Así `G` es el mismo
   módulo que el lote usa como `BASE.G`, y un patrón de prueba fijado en `G` vale también dentro del lote.
2. **La llamada al lote (`correr_b63.py:245-248`).** El `Namespace` suma dos campos:

   ```python
   a = Namespace(..., entrada=<la ruta de --entrada>, sha256_entrada=self.e["_sha256"], ...)
   ```

   - `presupuesto_sesion` puede quedar como está (`self.e["R5"]["max_budget_usd"]`), porque el lote controla que sea igual, o
     ir en `None`, y entonces sale de la entrada.
   - Hoy la ruta de la entrada no queda en `e`: `cargar_entrada` devuelve `_rutas`, `_cfg` y `_sha256`, pero no la ruta. La
     etapa b la tiene que llevar hasta `CorridaB63`, desde el `a.entrada` de `main` o en un campo de `e`.
3. **Los códigos.** El `except SystemExit` de `:255` sigue igual. Una entrada que no existe, otro sha256, una entrada sin R5 o
   un presupuesto distinto llegan como `SystemExit` con texto y dan el 3, igual que un lote inválido. Un R5 no admitido **no**
   llega como `SystemExit`: `L.correr()` devuelve el 5, con registro y con `L.motivo_freno`.
4. **`fijar_patron_de_prueba` (`:89-100`).** Con `G = guardas_lote_r5`, el runner fija `G.PATRON_PAGO` y `G.PATRON_EXTRACCION`
   en el módulo que usa el lote. `guardas_lote_r5.extraccion_corriendo` lee el `PATRON_EXTRACCION` de su propio módulo, no el
   de `guardas_lote`, así que el patrón de prueba de la extracción también vale. Su control del token,
   `re.search(PATRON_REAL, token)`, pasa a buscar también `correr_b63\.py`.
5. **`control_patron` (`:77-86`).** `PATRON_REAL` termina en `correr_b63\.py`. `trae_el_renglon_16` y
   `trae_correr_prueba_T_v2` siguen en `True`, pero `patron_igual_al_renglon_16_mas_T`
   (`PATRON_REAL == f"{pat}|{piezas[-1]}"`) da `False`: es informativo y no frena. Propongo compararlo con
   `f"{pat}|correr_prueba_T_v2\.py|correr_b63\.py"` y sumar `trae_correr_b63`.
6. **Las guardas del runner.** `guarda_otro_paso_pago` (`:103-106`) corre antes de cada bloque y antes de la primera sesión.
   Con `guardas_lote_r5` también ve otro `correr_b63.py` que corra al mismo tiempo, y no se ve a sí mismo: excluye el proceso
   propio, sus ancestros y los descendientes del lote.

## 3. Lo que cambia en `b63/comun_b63.py`

`cargar_entrada` (`comun_b63.py:153-162`) compara el R5 de la entrada con `LOTE.R5_ESPERADO` de `lanzar_lote_paralelo`. Con
el R5 B frena antes de llegar al lote. El cambio:

```python
import lanzar_lote_paralelo_r5 as LOTE                  # en lugar de lanzar_lote_paralelo
if not LOTE.admitido(r5):
    frena(f"R5 de la entrada {r5} no es uno de los admitidos {list(LOTE.R5_ADMITIDOS)}")
```

El control contra `config_agentes` (`:157-159`) queda como está. Por eso una entrada con el R5 B pide una `config_agentes` con
`corte_R5` 47, 45 y 3,30. La de hoy trae la A.

## 4. Los comandos que pueden correr mientras corre B6.3

Todo comando que hoy llame a `paralelo/guardas_lote.py pago` (o que espere con `pgrep -f` y el patrón de `guardas_lote.py`)
pasa a `paralelo/guardas_lote_r5.py pago`, o a `guardas_lote_r5.pgrep()` para esperar. Así ve `correr_b63.py` también
mientras corre el juez encadenado, cuando no corre ninguna sesión del lote.

## 5. Un hallazgo en BASE

El `main` de `lanzar_lote_paralelo.py`, corrido como proceso, sale con **1** y no con el 3 ante un lote inválido. La causa:
`validar` levanta `SystemExit` con texto, y `main` no lo captura. El runner no lo sufre, porque importa `Lote` y captura el
`SystemExit` (`:255`). El `main` del lanzador r5 lo captura y da el 3. Lo controla el T10 de
`agentes/selftest_lanzar_lote_paralelo_r5.py`.
