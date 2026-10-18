# U-MED-DESAMB: diseño sellado de la medición de la desambiguación

**FIRMADO por la autora el 17/10/2026, en el mensaje recibido a las 11:31:33** (firma por mensaje; hoja de ruta de la mesa, §140). Es su
respuesta al informe de la mesa (§139, `decisiones_139_mesa/informe/informe_UMEDDESAMB_desambiguacion_mesa.md`, en el paquete de la
mesa), con sus 13 decisiones. La mesa lo sella con su sha256 y la hora **antes del sorteo**:
`sello_diseno_med_desamb_2026-10-17.txt`.

Lo redacté yo, la mesa, desde esas decisiones. Lo que va entre comillas es tal cual del mensaje de la autora.

## 1. Qué se mide y qué decide cada cosa

- **La lectura de la autora,** 52 ítems, decide S1 y S2 y alimenta S3. Lleva además 12 calibradores mezclados, que no deciden nada.
- **C1** se decide con el censo de todas las colisiones que une la regla, sin piso (§6).
- **O1 no se decide con la lectura:** va al grafo corregido del cap. 6 (salida (c)). Lo que den la parte 2 y O1 sobre el grafo sin cola diez
  rs1 queda como cifra descriptiva para la tesis.
- **El juez de modelo** da solo la cifra descriptiva de sujetos por estrato. No decide ningún cambio del grafo (§8).
- **P1** va solo como script de diagnóstico, sobre los grafos sellados y sin tocar el ensamblado. Lo que eso no alcanza va al cap. 6.
- **P2 y P3:** sí. P3 es un requisito de implementación (§6).

## 2. La población

- El grafo: KG-Tanda0-Diez-r2b-sincola-rs1. Archivos de `data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2b_sincola_rs1/r2/`:

  | Archivo | sha256 |
  |---|---|
  | `kg.json` | `61dd1b69ba03e40499845c40a6a8bec4c22d892ebe95823c7d5a569110f08738` |
  | `resolucion_sujetos.jsonl` | `61fa22aef857eb29793a76574caa98562dc686559c4302a9cf3c5313a1c2b695` |
  | `no_mapeados_sujetos.jsonl` | `ac68949ed911f3314ccd609b4a1c76b7ad5f05d6a9176accbfd42868e6d73517` |

- **Unidad:** la relación de sujeto, una fila de `resolucion_sujetos.jsonl`.
- **Los estratos** salen de la función `estrato` de `parte2/tamanos_desamb_mesa.py`, sobre la regla de decisión de
  `data/experiment/reextraccion_v2/corpus_v2/r1_e4.py:435-444`:

  | Estrato | Vía | N |
  |---|---|---:|
  | E1 | R1 sin desacuerdo | 365 |
  | E2 | R1 con desacuerdo | 168 |
  | E3 | R4, la regla del texto da el mismo id | 1.010 |
  | E4 | R4, la regla da otro id | 277 |
  | E5 | R4 sin regla, con mención verificada | 334 |
  | E6 | R4 con mención no verificada | 200 |
  | E7 | R2 | 8 |
  | E8 | calificador | 16 |
  | E9 | R3 | 20 |
  | E10 | R4 sin mención | 0 |
  | — | cuarentena | 148 |

  Recuento de la mesa: `decisiones_139_mesa/verificacion/salida_verificar_mesa_de_apoyo.txt`.

## 3. El criterio de sujetos

Firmado tal cual (informe, §5.2):
- **correcta:** en esa norma, el texto se refiere a ese sujeto, con ese alcance y en ese papel;
- **genérica:** el texto nombra un sujeto más específico que está en el catálogo debajo de la entrada;
- **incorrecta:** es otro sujeto, la entrada es más específica que lo que dice el texto, o el sujeto no cumple ese papel en la norma;
- **no decidible:** el texto, con su herencia, no lo identifica.

Y con él:
- «"acierta" es solo "correcta", la genérica no acierta y, en E4, las no decidibles salen del McNemar, declaradas.»
- **El análisis de sensibilidad, declarado:** «la misma cuenta con "correcta o genérica" como acierto. Se informa y no decide.»

## 4. Las reglas de decisión

Código: `parte4/estimadores_desamb_mesa.py`.

- **S1** (firmada tal cual): la regla del texto acierta más que el modelo en E4 (b > c), con McNemar exacto de dos colas, p < 0,05.
  - **Unidad:** el par de clases (la de la entrada de la regla y la del modelo) de cada uno de los 26 ítems de E4. Salen los que tienen
    alguna no decidible, declarados.
  - «La decisión de S1 vale para las tres reglas» (calificador, R2 y R3). «El resultado se informa también por regla, como descripción,
    declarando cuántos casos de R2 y de R3 cayeron en la muestra» (`describir_E4_por_regla`).
- **S2:** «aplica si aciertan 7 o menos de 16», y se informa su intervalo de Wilson.
  - Con n = 16, la condición del límite superior de Wilson menor que 0,75 es redundante, y así se declara: con este umbral solo excluye
    algún caso con n de 1, 3 o 5 (`decisiones_140_mesa/verificacion/salida_s2_cuando_pesa_wilson.txt`, en el paquete de la mesa).
  - **S2 es solo cuarentena:** la relación va a cuarentena con la sugerencia del modelo guardada. «El rol, al grafo corregido.»
- **S3** (firmada tal cual): si 3 errores o más comparten el mismo par mención → entrada, ese par es candidato a alias.
  - **PRECISIÓN DE LA MESA, no estaba en la firma;** la autora la confirma o la corrige antes de leer:
    - **error** es una clase incorrecta o genérica de la entrada que está en el grafo, y la no decidible no es error;
    - **la mención** se normaliza como la lee R1: sin el artículo inicial y con `r1_comun.norm` (`r1_e4.py:346`).
  - **El alta** sigue el procedimiento de la enmienda 4: lectura contra el texto, aprobación de la autora, solo el catálogo de
    resolución y la re-resolución por script.
- **No se decide con la lectura:** O1 (§1).

## 5. Los tamaños y la regla de la semilla

**Los tamaños:**

| Grupo | Composición | Total |
|---|---|---:|
| La lectura | E4 26, E6 16 y el control fijo: E1 4, E3 3, E5 3 | 52 |
| Los calibradores | de E1 a E9, sin las filas de la lectura | 12 |
| La muestra del juez | 50 por estrato de E1 a E6 y censo de E7, E8 y E9, sin los 12 calibradores | 344 |

- **La muestra del juez es independiente de la lectura:** un ítem de la lectura puede caer también en ella, y se declara.
- **El juez también clasifica los 52 ítems de la lectura,** para el acuerdo.

**La semilla:** `u-med-desamb-17102026`.

**El sorteo** (`parte4/planilla_desamb_mesa.py sortear`):
1. Se ordenan todas las filas por (to, chunk_id, indice_relacion, predicado). En la clave de orden, los enteros van con 9 dígitos y el
   nulo como cadena vacía.
2. Por estrato, en este orden, `random.Random(f"{semilla}:{estrato}").sample(filas_del_estrato, n)`, o el estrato entero si tiene n o menos
   filas, declarado:
   - E4, E6, E1, E3 y E5;
   - `calibracion`, sobre E1 a E9 sin las filas ya elegidas;
   - `juez:E1` a `juez:E9`, sobre cada estrato sin los calibradores.
3. La lista (solo claves) y su sello (sha256, hora, semilla, el sha256 del registro de resolución y el del código) se escriben antes de
   armar nada.

**La planilla:**
- los 64 ítems van en el orden de `random.Random(f"{semilla}:orden").shuffle`;
- se numeran D001 a D064;
- en E4, las dos entradas van en el orden de `random.Random(f"{semilla}:entradas:{ítem}").shuffle`.

## 6. C1 y P3

- **C1:** «censo de todas las colisiones que une la regla, sin piso», con las tres condiciones del informe, §4.4:
  1. la normalización se sella antes de contar;
  2. es un censo, no una muestra;
  3. una sola colisión mal unida frena la regla o la corrige con una excepción declarada, y el censo se relee en el acumulado.
- **La normalización** es `codigo_normalizado` de `parte2/tamanos_desamb_mesa.py`, sellada con el sha256 de ese archivo (§10):
  - la Comunicación del BCRA va por letra y número;
  - lo demás va por el código sin acentos ni puntuación;
  - nunca se unen las que no tienen número, los marcadores («sin especificar», número 0) ni las de tipo «referencia» o «TO».
- **El código preparado de C1:** `parte3/codigo_preparado/`, con el parámetro `codigo_comunicacion` de la guarda.
- **P3:** toda regla de sujetos entra a la vez en las tres funciones de la regla de decisión, con un selftest que las compare sobre las
  mismas filas:
  - `resolver_relaciones_r2` y `reresolver_registro` (`r1_e4.py`);
  - `reresolver_catalogo.decidir`.

## 7. La planilla y el control de las normas

- **Antes de la planilla**, cada ítem de la lectura y de la calibración busca su norma en el registro validado del runner
  (`data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b/<to>/extracciones_finales_r2_<to>.jsonl`): la relación de igual
  `indice_crudo` y predicado.
  - Si alguna no se encuentra o no es única: **FRENO**, sin planilla.
  - La mención y su verificación salen de la fila de resolución; del registro, solo la norma.
- **La planilla** (`planilla_lectura.md`, un ítem por sección, y `hoja_clases.csv`, una fila por entrada para cargar la clase) lleva:
  - el ítem, sin la vía, el estrato ni la marca de calibrador;
  - el documento y el punto;
  - la norma (tipo, etiqueta y descripción);
  - el predicado y la mención;
  - el texto propio y el heredado de la unidad: E0 de `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b/`, con las partes de
    `particiones_por_corte.json`;
  - cada entrada, con su id, etiqueta, alias, definición y padre (`data/experiment/catalogo_unico/catalogo_sujetos_r2.json`, `c3ad1581…`;
    roles de `generados_r2/rol_por_to_r2.json`, `07cdb7af…`).
- **La clave** va en su archivo aparte. «No la abro hasta cerrar mi lectura.»
- **No se copia nada de E3.**

## 8. El juez de modelo

- **Modelo:** `claude-opus-5-5`. Precio por millón de tokens: entrada USD 4 y salida USD 20. «El precio lo verificó la mesa de apoyo en la
  página oficial de precios.» Los supuestos de tokens siguen NO VERIFICADOS.
- **Cómo trabaja:** clasifica cada entrada (correcta, genérica, incorrecta, no decidible o requiere adjudicación) y el código computa.
  - **N = 3**, con llamadas independientes y sin caché compartida entre repeticiones.
  - El veredicto es el modal; si no hay moda, va a adjudicación de la autora.
  - **Los calibradores** son los 12 ítems mezclados en la planilla, con la clase que les dé la autora.
- **La validez,** fijada antes: el acuerdo binario (correcta o no) con las 78 clasificaciones de la autora (E4 52, E6 16 y control 10)
  tiene que ser de 68 o más. Si no llega, la cifra del juez no se usa y valen las de la autora.
- **La muestra:** la del §5. La cifra es Wilson al 95 % por estrato y la ponderada por N, con Wilson sobre el n efectivo de Kish (§9).
- **Antes de correr:** una prueba de humo de 5 llamadas, con los tokens reales.
- **El tope:** USD 40, autorizado por la autora.
- **La ventana:** entre el sello de la tanda final y el martes 27/10/2026, nunca a la vez que una extracción. Lleva su propio registro de
  uso y su propia cuenta, fuera del repo.
- «Si el miércoles 21/10 a las 18:00 no terminé mi lectura, el juez no corre y se declara.»

## 9. Los estimadores

- Wilson al 95 % con z = 1,959963984540054.
- La ponderada por N con el n efectivo de Kish: n_ef = (Σw)² / Σw², con w = N_h / n_h (la forma de T4 de la tanda 1,
  `docs/preregistro_tanda1.md:586-590`).
- McNemar exacto de dos colas: p = min(1, 2 · P[X ≤ min(b, c)]), con X ~ Bin(b + c, 1/2).

## 10. El calendario y el recorte

- «Mi lectura cierra el jueves 22/10 a las 12:00.»
- «Orden de recorte: el juez, S3, y S1 y S2; C1 al final.» Lo que no llegue al corte del grupo 2 (sábado 24/10/2026, 12:00; enmienda
  8, §4) va al grafo corregido del cap. 6, declarado.
- **Tripletas:** el solapamiento con la etapa V y con el control de T se declara y no se excluye, y T informa las tres cifras del
  informe, §7. Va por una enmienda al pre-registro de tripletas, que la autora firma antes del sorteo de T.

## 11. El código sellado

Los sha256 son de los archivos que van con este diseño, en `data/experiment/med_desamb/`.

| sha256 | Archivo |
|---|---|
| `428a3cce394111a078a71f06918e90da5bb014a7111426476054a481429ca5d3` | `parte2/tamanos_desamb_mesa.py` (los estratos, los tamaños y la normalización de C1) |
| `6a20a7ba3cb38dbef36e3b388cf07110a83362210cecc0c767072bcd276c8037` | `parte2/selftest_tamanos_desamb_mesa.py` |
| `d53b7551ec9d645cf12923dfcc3427d43c024718353b0ac053352ae83aa7ac4e` | `parte3/armar_parches_mesa.py` |
| `4f39df7d003b30a309137dc2437b566d2a95fb1a093f9b030ee3ea3dede48731` | `parte3/mismo_acto_o1_mesa.py` |
| `f48b2aad22b8600749f3bfa02637d3499c2c9a2bf1c8ac48f4b7f96cff1456f6` | `parte3/selftest_reglas_candidatas_mesa.py` |
| `cebbb95f3116872a08b05d06e7caee292559fae930ba09b3f7942df528fe6845` | `parte3/codigo_preparado/base_y_parchados_sha256.txt` (los parches de S1, S2 y C1 contra HEAD `ca5b39fd`) |
| `cd7b12a62c47ff64bd067c9d3b509eb03ddf75f1aeb936c92f2457ed9a873043` | `parte4/planilla_desamb_mesa.py` |
| `f225c03ae0f21b086c8fb7ec6a1e8a0485f9b5983d59df8813f54de4e18d748b` | `parte4/estimadores_desamb_mesa.py` |
| `889d3a431fcb525054645c7d8b1049c83a44b327619a4e559aca05dd5d252738` | `parte4/selftest_o1_y_planilla_mesa.py` |
| `25090a4db1a5e33f8f66a36a3d429828dfb836cfe35c955c8f27ce9153e2a4cc` | `parte4/costo_juez_mesa.py` |
| `5779dccb60bb8b68d9c0b0a5205b87bfa67e33361f842b205b236142a8e2a39a` | `p1/p1_diagnostico_conflictos_aristas_mesa.py` |

## Firma y sello

- **FIRMADO por la autora el 17/10/2026, a las 11:31:33** (por mensaje; hoja de ruta de la mesa, §140).
- **La mesa lo selló** con su sha256 y la hora antes del sorteo: `sello_diseno_med_desamb_2026-10-17.txt`.
- **El orden después del sello:**
  1. la parte 2 y O1 sobre el grafo sin cola diez rs1;
  2. el sorteo, con su sello;
  3. el control de las normas;
  4. la planilla y la lista del censo de C1.
