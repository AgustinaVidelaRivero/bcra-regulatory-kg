# U-R2-CODIGO-2 — FRENO C2: implementación y controles

Implementación de C2, 04/10/2026, sobre HEAD `5c58f38` (trae P3b-2 de U-PROMPT-R2, `c8c3970`, y el caso de la arista
de la cadena de P3, `f3922d8`). USD 0: ninguna llamada a la API; Neo4j no se usa. Antes de empezar, `git status` no
mostró cambios sin commit en mis archivos ni en `prompt_r2/p3/`. Todo corrió sobre copias armadas copiando (regla l,
0 enlaces); al repo copié el código, la E0 nueva y las salidas. Sin commit.

Mandato firmado en `95dfd98` (sha256 `fda61dca…`); lo leí con sus notas fechadas del 04/10/2026. L-ESQ-R2, en
`4ef7650` (sha256 `66c4a1b9…`).

**Correcciones de la revisión (04/10/2026, sobre `75003eb`).** «O no» fuera de la negación y «más del» y «menos del»
como formas (enmienda 5 a L-ESQ-R2, borrador pendiente de firma); los dos casos de la cadena de P3b-2 que cambia (t);
el docstring de `reglas_comparacion.py` con la regla final. Este freno queda actualizado con eso. Durante el
trabajo entró `bb472b1`, de la autora: solo toca documentos (la enmienda 5, mandatos, plan y checklist).

## Diferencias entre el mensaje del «seguí» y los archivos, y decisiones mías a revisar

1. **(i) y (j) frente al texto firmado de L-ESQ-R2 §1.3.** La negación invierte el sentido «con hasta tres palabras en
   el medio» (`4ef7650:…enmienda_L-ESQ-R2_2026-09-30.md:277`) y la precedencia es «primero coeficiente» (`:294`). (i)
   y (j) cambian las dos cosas y van por la enmienda 5
   (`data/experiment/esq/enmienda5_L-ESQ-R2_negacion_y_comparador_pegado_2026-10-04.md`, borrador pendiente de
   firma). Su §1 coincide con el código, con dos precisiones que no cambian ninguna cifra:
   - en 1.b, «otra forma de comparación» son las simples y las compuestas; no entran la adyacencia de «mínimo» y
     «máximo» ni «o más»;
   - en el punto 2, «pegado» incluye «o más» y «o menos» con un paréntesis en el medio (la regla de calibración P3
     los admite así) y los marcadores que la detección de la cuantía exige o incluye: el de un ordinal y el «o más»
     entre el paréntesis y la unidad del punto (c).

   De las cifras de su §2 cambia una: la fila del comparador pegado da 26 y 26, no 25 y 25, porque `cap::3.1.11.2`
   deja `coeficiente` por «más del» pegado y cuenta en esa fila y en la de 3.b. `cap::6.2.2.3` estaba entre los 25
   y cuenta también en la de 1.d. Las otras tres filas se confirman (13 y 11, 1 y 1, 4 y 4), como las cuantías del
   texto (2 de «o no» y 7 de «más del» y «menos del»). Las filas suman 44 y 42; los elementos distintos son 42 y 40.
2. **(m), selftest.** El mensaje habla de «los cuatro casos» que esperan la marca. En `selftest_pyd_r2.py` son nueve
   las expectativas que codifican la regla anterior: las cuatro de la marca y cinco filas que esperan
   `maximo_inclusivo` para el mismo plazo sin marcador. Pasan todas a `no_determinada`.
3. **(l) quedó en una lista de páginas, como (f).** Aplicada a toda página, la regla (`continua_titulo`) recupera texto
   de la norma en 7 TOs de la partición de 152, pero mueve ids. En `snp_cheq` cambian 179 chunks (13 de ellos por el recorte de h) y
   aparece `snp_cheq::7.1::intersticial::290`; en `fabcra` la tabla002 deja de serializarse. Esos cambios no entran a C2.
   Rige en las pp. 15, 30, 54 y 59 de ric (`correr_e0.COLA_TITULO_ESTRICTA_E0_R2`), con el mismo resultado en la
   tanda 0. La medición de la regla general queda para S0 de U-SEG-OFICIAL (`c2_e0.json`,
   `particion_152_cola_en_toda_pagina`).
4. **(f), ABL.** Implementé solo la lista de renumeraciones, sin el padre sintético de AL: con la renumeración, el 4.4
   se abre en la p. 16 y el 4.4.3 y el 4.4.4 encuentran su padre. Los 5 rechazos de encabezado de 4.3 y 4.4 pasan a 0
   (`c2_e0.json`, `f.rechazos_header_en_4_3_y_4_4`).
5. **(s) y (t), cadena sintética de P3b-2.** Actualicé sus dos casos que (t) cambia (`cadena_sintetica_p3b2.py:260`
   y `:289`: `vistos_por_e3` lleva las tres marcas, y `unidades_con_marca_e3` cuenta copia 1, lectura 1 y reintento
   1) y su resumen. Da 20 de 20, con doble corrida idéntica. En el resumen cambia además el sha256 del ensamblado:
   el único cambio del grafo es la materia del TextoOrdenado de cla (punto n).
6. **(c) «o más».** Admite el paréntesis opcional, como toda cuantía. De los 4 elementos nuevos de diez, 2 vienen de
   una descripción sin paréntesis («46 o más días hábiles»). «o menos» en esa posición no entra: el mensaje nombra
   solo «o más».
7. **Escrituras.** Sumé en `r2_codigo2/` los scripts de control de esta etapa (`c2_*.py`), como en C1. No son código
   de la cadena.

## Tabla de controles

Diez y desarrollo son KG-Tanda0-Diez-r2a y KG-Tanda0-Desarrollo-r2a. «r2a» es la cadena con el código de C2 y la fase
de los sellados; «r2b» es el mismo crudo con las reglas de r2b (`c2_cadena.json`).

| Punto | Control | Resultado |
|---|---|---|
| a | 18 filas «detector» de M3.b | patrón 1: 9 de 9 externas; NIIF 9, «norma fuera del inventario»; B07 y B08 → `ctacte::9.2.1.1` y `9.2.2.1`. Patrón 2: 4 de 4 con la causa propia, y 10 citas en `citas_a_puntos_de_anexo`. Patrón 3: 5 de 5 internas e irresolubles |
| a | `remite_a` | diez −11 y +10 (14.000 → 13.999); desarrollo −11 (12.833 → 12.822). Iguales al contrafáctico de C1 |
| b | cliente simulado, 4 unidades (las 3 de desarrollo son las mismas) | con el perfil r2, reintento con el request idéntico y namespace `…-rforma1`; bien formado, la unidad valida; agotado, error declarado en el resumen. Sin el perfil r2, 1 llamada y el registro de siempre. Clave base en la db con el mismo crudo; la del reintento, no (`c2_sinteticos.json`, 23 de 23) |
| c | elementos que cambian, diez | +1 «hs.» (`ctacte::7.3.1.5`); +2 ordinales (`cap::7.4`, `pagjub::2.5.2`); +4 «o más»; 3 «hábil» en singular; 2 plazos dejan `frecuencia`. Base del 25 % de `cap::6.11`, igual. Desarrollo: +1, +4, 3 |
| d | contador | 3.801 → 1.261 (2.540 autocitas); 2.993 → 1.134 (1.859). 7 autorreferencias salen del registro en cada grafo. Ninguna `remite_a` por (d) |
| e | pasada residual | la clave queda con `retirada`; `e4_pasada_residual_medida.json` ya no se escribe; el grafo no cambia |
| f | ric | +5 ids; `ric::4.3.3`, de 7.651 a 806 caracteres; 3 avisos `renumerado_por_lista`; número impreso en los flags; las 8 citas de ric a 4.4.x tienen unidad. 152: ningún id cambia |
| h | `ric::11.2.3` | herencia de 15.170 a 3.940 (11.322 omitidos, `herencia_recortada`). Citas de la regla (i) que dejan de atribuirse: 0 (el bloque heredado no tiene citas de puntos). 152: 93 unidades en 9 TOs, 7 de ellas partes; 0 con la herencia sobre U (el tope de h). Por tamaño completo quedan 57 unidades sobre 13.091 caracteres (46 por su texto propio), que no son tema de (h) (`c2_e0.json`, `particion_152`) |
| i | diez / desarrollo | negación e «igual o superior» (enmienda 5, 1.a a 1.c y 3.a): 13 / 11 elementos (11 + 2 y 9 + 2), todos corregidos: en diez, las 12 de la revisión y `ctacte::1.5.2.12` («no podrán registrar una antigüedad superior a…»). «O no» (1.d): 1 / 1, `cap::6.2.2.3`, «3 %»: con la regla anterior quedaba en mínimo inclusivo, ahora en máximo estricto (`simple:menor`); frente al sellado, que lo daba coeficiente, cuenta también en (j). En el texto propio de las 2.439 unidades de `salida_tanda0_r2b/`, 2 cuantías, las dos de `cap::6.2.2.3` |
| j | diez / desarrollo | comparador pegado (enmienda 5, 2): 26 / 26 dejan `coeficiente`. «Más del» y «menos del» (3.b): 4 / 4: `cla::6.3.2` («no menos del 50%») pasa a mínimo inclusivo, `cap::8.4.2.1` y `cla::6.5.4.7` a máximo estricto, los tres desde `no_determinada`, y `cap::3.1.11.2` («más del 5%») de `coeficiente` a mínimo estricto (también cuenta en los 26). En el texto propio de las unidades, 7 cuantías: `cap::3.1.11.2`, `cap::8.4.2.1`, `cap::8.4.2.2`, `cla::6.3.2` (2), `cla::6.5.4.7` y `cla::7.2.4`. De las 28 de la revisión, 2 son dobles conteos de su script (mismo tramo dos veces en la descripción; el segundo no está pegado) |
| k | sintético | la cuantía del ítem toma «mínimos» del encabezado (`encabezado:compuesta:adyacencia_minimo`); 0 cambios en r2a |
| l | renglones | 6 recuperados en ric: p. 15 (2) → `ric::4.3.1.2`; p. 30 → `6.1.2`; p. 54 → `11.2::intro`; p. 59 (2) → `12.4`. Otros 9 TOs y 152: 0 ganados y 0 perdidos |
| m | r2b | diez 176 y desarrollo 157 elementos → `no_determinada` (126 → 302 y 122 → 279); `comparacion_asumida`, 0 |
| n | diez | los 10 TextoOrdenado con versión y materia (`c2_cadena.json`, `n_texto_ordenado`); 8 de 8 con la carátula; páginas: 617 legibles, 119 sin pie, 0 ilegibles |
| o | sintético | en r2b la lista conserva el límite relativo y suma la cuantía; en r2a se reemplaza |
| p | cadena de P3 | LN-7 sobre el ensamblado → resuelto; 27 de 27 |
| q | r2b | 788 en diez (778 `remite_a` y 10 `establecida_en`) y 763 en desarrollo (757 y 6); lista en `aristas_derivadas_cola_humana.json` |
| r | bases | 0 cambian (15/4/141 y 15/3/136); `cla::5.1.1.1` → `cla::3.7` |
| s, t | cadena de P3b-2 | total del ensamblado = suma de los E2 r2; las tres marcas contadas; 20 de 20 |
| P3b, aparte | Operacion | diez 2.047 → 2.136; desarrollo 1.555 → 1.607 |

Grafos r2a con el código de C2: diez `70d51e42…`, desarrollo `fa4c1043…`. Frente a los sellados cambian solo los
umbrales de 50 y 46 nodos (54 y 48 elementos) y las `remite_a` de (a). Por regla, los elementos suman 56 y 50:
`cap::6.2.2.3` y `cap::3.1.11.2` cuentan en (j) y en su corrección. Los puntos (m) a (t) no actúan en r2a. Las cifras por regla y la
lista de cada elemento están en `c2_cadena.json` (`umbrales.elementos_por_regla`, `correcciones_de_la_revision` y
`cuantias_en_texto`).

## Controles de siempre (`c2_control_repro.json`, sobre una copia nueva)

- E0 legada de la tanda 0: 34 de 34. Los tres ensamblados sellados, con `--entrada` absoluta: 13 de 13 cada uno, 3 con
  la ruta normalizada.
- Suite del perfil r2: ningún ítem cambia de estado (diez contra `estado_esperado`; desarrollo contra M2). Shapes,
  fase r2a: ningún shape cambia (S7, S12 y S18 en FAIL antes y después).
- `salida_tanda0_r2b/`, doble corrida: 57 de 57 iguales. Los 9 TOs, iguales byte a byte a `salida_tanda0_r2/`. En ric,
  solo los cambios declarados. En los agregados, solo la entrada de ric. Hay 10 `pies_<to>.json` nuevos.
- Doble corrida idéntica de `c2_cadena.json`, `c2_sinteticos.json`, `c2_e0.json` y de los resúmenes de las cadenas de
  P3 (27 de 27) y de P3b-2 (20 de 20).
- Selftests: los mismos resultados que HEAD salvo los ampliados, `selftest_pyd_r2` (385/385; G15 nuevo, 42 casos) y
  `selftest_r3` (109/109; T8 nuevo). Fallas previas, iguales en HEAD:
  - `selftest_canal_abierto_e1`: 1;
  - `selftest_manifiesto`: las 5 de P5 en una copia;
  - `selftest_gate6` y `selftest_muestra_aristas_obs12`: no corren en una copia.
- Repo igual antes y después del control.

## Errores propios, con su causa

- La primera doble corrida de `c2_cadena.json` dio distinto: volcaba conteos tomados de conjuntos, cuyo orden cambia
  entre procesos. Ahora se ordenan, y las corridas dan igual.
- El control de rechazos de 4.x de `c2_e0.py` filtraba por una clave que esos registros no tienen, así que daba vacío
  por construcción. Lo corregí: ahora lee el número del texto del encabezado.
- Las dos fallas se encontraron antes de este reporte y no tocan la cadena.

## Lo que U-REEXT-T0 hereda

- La E0 `salida_tanda0_r2b/`: actualizar los manifiestos r2b es su primer paso. Cambian las claves de E1 y E3 de las 5
  unidades nuevas y de las 6 con texto o herencia nuevos.
- `selftest_prompt_r2b.py` exige que ninguna unidad lleve `herencia_recortada`. Sobre la E0 r2b falla por
  `ric::11.2.3`.
- El reintento por forma cuesta una llamada de E1 por unidad mal formada: 4 de 2.434 en la tanda 0.
- (i), (j) y las correcciones de la revisión aplican la enmienda 5 a L-ESQ-R2, cuya firma está PENDIENTE.
- La medición de la cola de título en toda página, para S0 de U-SEG-OFICIAL.
- Los scripts de `medicion_r2a/` que importan `reglas_comparacion` o `r1_referencias` (m2, m3) darían otras cifras si
  se corren con este código. No los corrí.

## Comandos (desde la raíz de una copia del repo, `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B`)

```
data/experiment/reextraccion_v2/e0_chunking/correr_e0.py --version-e0 e0-r2 --manifiesto data/experiment/reextraccion_v2/manifiestos/tanda0_10tos.json --salida data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b
data/experiment/r2_codigo2/c2_cadena.py --pies data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b --out data/experiment/r2_codigo2/salidas/c2_cadena.json
data/experiment/r2_codigo2/c2_sinteticos.py --out data/experiment/r2_codigo2/salidas/c2_sinteticos.json
data/experiment/r2_codigo2/c2_e0_152.py --salida <dir> [--cola-en-toda-pagina]
data/experiment/r2_codigo2/c2_e0.py --nueva data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b --doble <segunda corrida> --p152-base <c1f_ric44.py --correr-tos todos --variante base, sobre 5c58f38> --p152-nuevo <dir> --p152-regla-general <dir> --out data/experiment/r2_codigo2/salidas/c2_e0.json
data/experiment/r2_codigo2/c2_control_repro.py <repo> <dir de trabajo fuera del repo>
data/experiment/prompt_r2/p3/cadena_sintetica_p3.py --salida <dir>
data/experiment/prompt_r2/p3b2/cadena_sintetica_p3b2.py --salida <dir>
```
