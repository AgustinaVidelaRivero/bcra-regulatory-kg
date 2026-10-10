# U-SEG-OFICIAL — FRENO S1-ter-b (10/10/2026)

Tramo b de S1-ter, con las decisiones de la autora sobre el FRENO S1-ter-a (texto copiado en el paquete). USD 0, sin API; Python
3.10.13 (`.venv` del repo). Escribí solo `s1ter/` (`tramo_b/` y 10 scripts), el scratchpad y la carpeta de la lectora. Nada
commiteado. Sin cifras de lectura. sha256 de lo escrito en `tramo_b/manifest_tramo_b_S1ter.json` (`e4ec36e8…`, todo salvo este freno).

**Foto de partida** (15:56:07, 49.567 archivos; `tramo_b/controles/control_declarados_foto_partida_S1ter_b.txt`): contra mi foto final
del tramo a, 9 archivos nuevos y 4 `.DS_Store` cambiados, nada más. Los 9 de `reports/tesis_mapa_1010/` y `reports/tesis_figuras_1010/`
dan los sha256 del texto. Tres `.DS_Store` también. `docs/tesis/.DS_Store` da otro (`696b4ec1…`, 15:49:58): volvió a cambiar
después de las 14:58:39; por la regla de los `.DS_Store`, se declara y no frena. HEAD `c080914`; 2.213 `.pyc`.

**Poblaciones finales, selladas antes de sortear** (`tramo_b/poblaciones_finales_S1ter.json`, `b47aee40…`, 16:00:45;
`scripts/poblaciones_finales_S1ter.py`, que se detiene si un valor no da). Dan los valores esperados del punto 3:
- cortes: `vigente` 8.063 (`733cd66b…`), `marcadores` 192 (`6637ad1d…`) y `sin_raiz` 1.313 (`1fec4bef…`); total 9.568;
- (a): 245 (`23a8f605…`);
- (b): 36. Son las 34 listas y `ri_oc::S2`, 35 fijos (`1df09dea…`), y una de las 51 de la sección 3 de ri_oc (`cb6fd691…`);
- regresión: 35 (`4aa927f6…`).

Controles: ninguna unidad de (b) está entre los 35; ninguna de las 51 está en (a); las 66 son 66 ids distintos.

**Lo que sale por el punto 3**, con motivo y ancla en `e82e22f` (lista completa en `salen`):
- cortes `sin_raiz`: las 11 unidades de ri_ao (derogado, Parte III, punto 2);
- (a): `manual::2.3.2` y `manual::S4::parte1` (histórico, Parte III, punto 1) y `ri_pspii::S2` (vía por página, Parte II.2, punto 1);
  además, por la decisión 1, las 9 listas de (b);
- (b): ninguna.

Ninguna otra unidad de optico, plandecuentas, los 9 TOs de vía por página o las 2 de ri2_pm que cruzan fichas estaba en las
poblaciones. Se quedan, declarados:
- ri_spi: sus 92 unidades en `sin_raiz` (Parte II.2, punto 2);
- las unidades por punto de ri2_pm (Parte II.2, punto 3, `:57`): 2 en (a) y `ri2_pm::1.6` en (b).

**Muestra y orden, sellados antes de la primera ficha** (16:01:37, `tramo_b/sellos_S1ter_b.txt`; las fichas se armaron desde las 16:06:31):
- `tramo_b/muestra_S1ter.json`, `9c865bfc…`;
- `tramo_b/orden_lectura_S1ter.json`, `acd57e37…`, la lista sellada con el id opaco de cada ficha.

Los reproduje con código aparte (`scripts/reproducir_sorteo_S1ter.py`): todo igual. Semillas, con su renglón:
- cortes: las tres cadenas exactas, `random.Random(cadena).sample(sorted(ids), n)`, 40 / 10 / 40 (mandato de la unidad `:845`,
  `:295` y `:300`). El orden de las 90 sale de `U-SEG-OFICIAL:cortes:S1-ter:orden`, sin agrupar por estrato;
- (a): `U-SEG-OFICIAL:1_16:S1-ter` (mandato `:847` y `:912`; mandato de S0-5a `:208` y `:394`), con la misma forma, 30;
- la unidad de la sección 3: `random.Random("U-SEG-OFICIAL:1_16:S1-ter:ri_oc").choice(sorted(ids))` (S0-5a `:473`);
- el orden de las 66: `random.Random("U-SEG-OFICIAL:1_16:S1-ter:R5-a").sample(sorted(ids_66), 66)` (S0-5a `:477`). Los 35 de
  regresión van después, en el orden de sus ids, sin semilla.

**Dos etapas:**
- 90 fichas en la etapa 1 y 101 en la etapa 2.
- **En las dos etapas cae 1 unidad**, que se califica en las dos. Otra unidad de la etapa 1 aparece en la etapa 2 como la que sigue,
  sin calificarse.

**Carpeta de la lectora:** `~/INGENIERIA IA/TESIS/fuera_del_repo/lecturas_ciegas/lectura_segmentacion_s1ter/`.
- `etapa_1/`: las 90 fichas, 137 imágenes y `manifest.txt` (`b3606f03…`).
- `etapa_2/`: las 101 fichas, 171 imágenes y `manifest.txt` (`6692fbea…`).
- Verificada (`scripts/verificar_carpeta_lectora_S1ter.py`): 138 de 138 y 172 de 172; nada sin listar; ningún `.DS_Store`.

Cada ficha muestra solo su id opaco, sus páginas (con su imagen, `pdftoppm -r 110`) y su texto: el heredado (los títulos, sin su
tipo) y el propio. Si la unidad es una parte de un punto partido por tamaño, lo dice.
- En la etapa 2, cada ficha muestra la unidad que se califica, con todas sus partes, y la que le sigue en el documento. En las 34
  listas de (b), la que sigue es su cierre. Así cumplo la decisión 5 con un formato igual para todas las fichas, sin marcar la
  población. `ri2_ae::14.3` sale con sus tres partes y el cierre.
- El único cambio sobre el texto de E0: el marcador de tabla `[TABLA <TO>::tablaNNN …]` sale sin el prefijo del TO, porque lo nombra.
- Control a ciegas (`scripts/control_ciego_fichas_S1ter.py`): en las dos etapas, fuera del texto de la norma, 0 renglones con
  vocabulario de población, regla, tanda o límite y 0 con un TO; en todo el archivo, 0 «::» y 0 ids de unidad.
- Las planillas vacías, solo con los ids opacos, quedan en `tramo_b/` y no en la carpeta, porque la decisión 7 deja adentro solo las
  fichas.

**Lista para la autora, vacía:** `tramo_b/lista_para_la_autora_S1ter_vacia.md`, con solo ids opacos. La llenan
`scripts/lista_para_la_autora_S1ter.py` y `scripts/cifras_lectura_S1ter.py`, fijados antes de la lectura. La lista suma, en las dos
etapas y con la misma regla, las correctas que traen una nota de la lectora: así llega a la autora una nota sobre la herencia de la
unidad de la sección 3 sin marcar esa ficha. Prueba con planillas sintéticas (`tramo_b/prueba_cifras_S1ter_b.txt`):
- 0, 3 y 4 errores de corte dan 0,9591, 0,9065 y 0,8912;
- 3 errores y una dudosa contada como error dan 4;
- una planilla mal formada se rechaza.

**Para la revisión:**
1. **Error propio, con su causa.** La primera versión de las fichas (16:06) mostraba el TO dentro del marcador de las tablas
   serializadas, que es texto de E0: armé las fichas sin revisar qué marcadores trae ese texto. Mi control lo encontró antes de copiar
   la carpeta (22 y 26 «::» en las dos etapas). La rehice con el marcador corregido y un control que se detiene si queda «::». La
   primera versión no llegó a la carpeta de la lectora.
2. **El bloque de regresión va después de las 66**, como está decidido. Para quien conozca esa decisión, el número del id opaco
   indica qué fichas son de la regresión (las últimas 35 de la etapa 2), aunque ninguna ficha ni la lista lo marquen.

**Convivencia** (foto de partida y final; `convivencia_S1-ter-b.txt` del paquete): 25 archivos nuevos, todos en `s1ter/` (los 14 de
`tramo_b/`, los 10 scripts y este freno); ninguno cambiado ni borrado; HEAD sin cambios; 2.213 `.pyc`, la misma lista. De otra mano,
solo `docs/tesis/.DS_Store`, que volvió a cambiar a las 16:14:31 (`42bc8ffa…`): se declara y no frena. Ningún `.DS_Store` entra en
un manifiesto ni en el paquete.
**Grep de convenciones** (script de S0-4, control positivo 16 de 16; `grep_convenciones_S1-ter-b.txt` del paquete): 0 coincidencias
en los 20 archivos de texto que escribí (este freno, los sellos, la prueba, la lista vacía, las planillas, los 4 controles y los 10
scripts), en los 5 JSON del tramo y en la copia del texto del despacho. En las fichas de la lectora, 11 coincidencias, todas en el
texto de la norma.
**Paquete:** `<scratchpad>/revision_USEG_OFICIAL_FRENO_S1-ter-b/`, 37 archivos más `manifest.txt`: este freno, la copia del texto del
despacho, lo de `tramo_b/` con sus controles, los 10 scripts, el tar.gz de la carpeta de la lectora, las fotos, el grep y los logs.
**Copia permanente** con `ditto` en
`~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/64082b65-8548-487d-9ff4-27e8bb6283c5/scratchpad/revision_USEG_OFICIAL_FRENO_S1-ter-b/`,
verificada contra su `manifest.txt`: 37 de 37 iguales por sha256 y bytes, ninguno sin listar. El tar.gz, extraído, da 138 y 172
archivos iguales a los `manifest.txt` de cada etapa.

FRENO S1-ter-b. Espero la revisión.
