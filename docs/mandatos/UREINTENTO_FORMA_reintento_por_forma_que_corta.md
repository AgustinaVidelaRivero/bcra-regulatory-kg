# Mandato U-REINTENTO-FORMA: el arreglo de la BKL-0050 y la extracción de `ri_transpa::Sbloque1::chapeau_seccion` (firmado el 20/10/2026)

**FIRMADO por la autora el 20/10/2026** (por mensaje recibido a las 10:49:30; hoja de ruta de la mesa, §196), sobre el borrador de la §190
(sha256 `d3d89a8a…`, en el paquete de la mesa, `decisiones_190_mesa/ri_transpa/`), con D-1 a D-4 del §6 como las propuso la mesa (sección
«Firma»). El texto firmado es el del borrador, con este encabezado y esa sección. No se despacha antes del sello del grafo evaluado. USD 0
hasta el paso pago del §4, que corre la autora en su terminal.

## 0. Por qué

- **La unidad** `ri_transpa::Sbloque1::chapeau_seccion` (`mini_chunk`, 21.712 caracteres) es el único error definitivo de la tanda final
  (registro de decisiones, §43; FRENO T2, `data/experiment/tanda_final/t2/FRENO_T2.md`, `8b9e2041…`).
  - Su primer intento de E1 salió mal formado, sin cortar.
  - Los dos reintentos por forma cortaron en 8.192 tokens: el reintento por forma usa el mismo `max_tokens` del pedido que produjo la
    salida mal formada (`data/experiment/reextraccion_v2/corpus_v2/runner_corpus.py:683-685` en HEAD).
  - La partición y el tercer escalón se disparan solo cuando corta el primer intento (`:741-750`): un reintento por forma que corta
    termina en `salida_mal_formada_tras_reintento`.
- **La decisión de la autora** (registro, §44, tal cual): «B. Se declaran como faltantes en el grafo evaluado y se extraen después del
  sello, con el arreglo, para la versión corregida.» La BKL-0050 dice el arreglo: el reintento por forma de E1 escala el `max_tokens`
  cuando corta.
- **En el tramo 2** había 25 unidades expuestas al mismo camino, y ninguna falló (FRENO T2, sección 2). La unidad es una sola.

## 1. Qué hace

1. **El arreglo, en el código de la cadena,** después del sello del grafo evaluado:
   - cuando un reintento por forma de E1 termina con `stop_reason = max_tokens`, se repite una vez con el `max_tokens` del tercer escalón
     (`cliente_e1.MAX_TOKENS_ESCALON_3_R2`, 40.960; `data/experiment/reextraccion_v2/e1_extractor/cliente_e1.py:90`), con la temperatura
     del reintento y en un namespace propio (un sufijo nuevo de la caché, como `-rforma1` y `-rforma2`, `:76` y `:80`);
   - si ese pedido también corta, la unidad sigue el camino de corte de hoy: el error `max_tokens_hit_tras_reintento` y la partición
     (`:741-750`), sin cambiar ese camino (D-1, §6);
   - **ningún otro pedido cambia:** el de toda unidad que no tomó el camino nuevo sale byte a byte igual, con su misma clave de caché.
2. **La extracción de la unidad,** E1 y E3, con el código arreglado, en una salida propia de la versión corregida (D-3, §6). No entra
   al grafo evaluado ni a ninguna cifra de B6.3.
3. **Su lugar en el grafo corregido:** la entrada de su extracción para el ensamblado de la versión corregida, sin ensamblarla todavía.

## 2. Lo que no cambia

- El prompt, el esquema, los modelos (E1 `claude-haiku-4-5`, que tiene que devolver `claude-haiku-4-5-20251001`; E3 `claude-sonnet-5`),
  las temperaturas, el SDK (`anthropic==0.100.0`) y la caché sellada.
- El grafo evaluado y lo que se midió con él. La unidad queda declarada como faltante en T5 de la tanda final, con su id, sus caracteres y
  su causa (pre-registro de la tanda final, §8; registro, §44).
- Las 78 rutas del código de la cadena hasta el sello. Después del sello, la lista se re-sella con el arreglo, con
  `data/experiment/controles_tanda1/sellar_codigo_de_la_cadena_mesa.py`.

## 3. Las pruebas, a USD 0, antes del paso pago

1. **El caso de la unidad, con un cliente stub** que da lo mismo que dio la API: el primer intento mal formado sin cortar y el reintento
   por forma cortado. Con el arreglo, el pedido escalado sale con el `max_tokens` del tercer escalón y su namespace nuevo.
2. **El caso en contra:** el pedido escalado también corta y la unidad va a la partición, como hoy.
3. **Nada más cambia:**
   - el control de entradas de T1 de la tanda final (`data/experiment/tanda_final/t1/`, su modelo) sobre las 2.439 unidades de la tanda 0,
     las 3.290 de la tanda 1 y las 4.951 de la tanda final: todos los mensajes de E1 y sus `kwargs`, byte a byte iguales;
   - `selftest_clave_cache` da OK, con el retiro de cuentas de A3; el control R19 sigue igual.
4. **La corrida en seco del camino real** (CLAUDE.md, §4.l): importa el runner y recorre las ramas de corte, reintento, partición, tercer
   escalón, salida mal formada y la rama nueva, sin tocar el `sys.path` por fuera.
5. **El estimado del paso pago,** con los clientes stub y la tarifa sellada.

## 4. El paso pago

- **Lo corre la autora en su terminal,** con un comando de la ejecutora que:
  - controla al arrancar que no haya una extracción corriendo y frena si la hay (registro, §55;
    `ninguna_extraccion_corriendo_mesa.py`, con su patrón);
  - corre solo esta unidad, con el runner y el código arreglado, sobre una copia y con su salida fuera de las carpetas selladas;
  - lleva el tope y el freno de D-2, con `--autorizado-tope`.
- **Va solo en el carril pago:** nunca al lado de otra corrida paga ni de otra extracción (registro, §58). Cuándo: D-4.
- **El cegamiento de U-MED-VERIF:** la salida de pantalla de E3 va a un `NO_ABRIR_` de la unidad, y el FRENO da solo si quedó aceptada,
  en la cola o con error, el gasto y el sha256 de lo que escribió. No es una unidad de la tanda 1, ni de la muestra de las FICHAS.

## 5. El FRENO

- El paso 0 (HEAD con el sello del grafo evaluado y el commit de U-PROC-HERENCIA; las 78 rutas como en la lista re-sellada).
- El diff del arreglo, sus pruebas con su salida, el estimado y, después del paso pago, el resultado de la unidad.
- La foto del repo antes y después, los `.pyc` y el grep de convenciones con `LC_ALL=en_US.UTF-8`.
- El paquete `revision_UREINTENTO_FORMA/`, con su copia permanente verificada. Nada commiteado.

## 6. Las decisiones al firmar

- **D-1, el diseño del arreglo.** La mesa propone el del §1: el reintento por forma que corta se repite una vez con el techo del tercer
  escalón, y si vuelve a cortar va a la partición. Es lo que dice la BKL-0050 y reusa el camino de corte que ya está probado. La otra
  opción, mandar el reintento cortado directo al camino de corte (reintento por corte, tercer escalón y partición), cambia más ramas.
- **D-2, el tope y el freno del paso pago.** La mesa propone USD 1,00 con freno en 0,60, NO VERIFICADO: una unidad de 21.712
  caracteres, con hasta tres pedidos de E1 y su E3. El estimado del §3, punto 5, puede bajarlo antes de correr.
- **D-3, dónde queda la salida.** La mesa propone una carpeta nueva de la versión corregida, en el repo, que se commitea con el FRENO.
- **D-4, cuándo.** Después del sello del grafo evaluado, que es lo que fija la §44. Como es una extracción, no puede ir al lado de
  ninguna corrida paga. La mesa propone que vaya después de las corridas pagas de B6.3 y antes del ensamblado de la versión corregida, en
  el hueco que deje el carril pago. Si se quiere antes, va entre dos pasos pagos, con el carril vacío.

## 7. Lo que se declara

- La unidad falta en el grafo evaluado (T5 de la tanda final).
- El arreglo es un cambio del código de la cadena después del sello, con su re-sello de la lista.
- Si con el arreglo la unidad tampoco se extrae, se declara con su causa y queda para la versión corregida, como está.

## Firma

**FIRMADO por la autora el 20/10/2026,** por mensaje recibido a las 10:49:30 (hoja de ruta de la mesa, §196), tal cual: «Firmo el mandato
de ri_transpa (decisiones_190_mesa/ri_transpa/UREINTENTO_FORMA_ri_transpa_mandato_BORRADOR_mesa.md, sha256
d3d89a8acee276fad6e91f28f1e6fa239c7a6d373f542f918ba8c0c34f9f5626) con D-1 a D-4 como los proponés.»

En el mismo mensaje, para el pre-registro de B6.3, tal cual: «la cifra aparte sin las preguntas cuyo gold cae en la cola deja afuera
también las que caen en esa unidad, que falta en el grafo evaluado.»
