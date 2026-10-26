# FRENO A2.2-b: el análisis de A2.2 con las adjudicaciones de la autora

Tramo 2 de A2.2, 26/10/2026, desde las 15:34:14 (el paso 0). USD 0, sin API y sin Neo4j. Rige el pre-registro FIRMADO,
`docs/preregistro_A2_2_sistema_por_fragmentos.md`, en su commit de firma `a78ead7b`. Lo leí con `git show`; su sha256 ahí es
`b113ed439679ae7b…` y en HEAD es el mismo, porque ningún commit posterior lo toca (`git log a78ead7b..HEAD -- <ruta>`: 0).
No commiteé nada. Espero la revisión de la mesa.

En este FRENO no hay ningún veredicto, tasa, diferencia, p ni predicción. El análisis los escribe en
`data/experiment/banco_mcp/a2_2/analisis/analisis_a2_2.json`; no los abrí ni los imprimí. El paquete no lleva el JSON: lleva su sha256.

## 1. Lo que hice

1. El paso 0 dio todo lo esperado. No faltaba nada en la carpeta temporal y no restauré nada (§2).
2. Corrí el selftest de A2.2 en una copia del repo: 34 de 34, con el repo igual antes y después (§3).
3. Corrí el análisis en el repo con el comando del despacho. Escribió `analisis/analisis_a2_2.json`, con 40 preguntas y 3 pares sin
   veredicto final (§4).
4. Hice los controles por código, que imprimen solo cuentas, nombres de claves y sí o no (§5):
   - aplica las 8 adjudicaciones y las 8 llegan al veredicto final de su par;
   - de los 3 pares sin veredicto final, 2 son por R3 y 1 es una respuesta sin juicio; por falta de adjudicación, 0;
   - el JSON trae las dos comparaciones del §5.
5. El repo: lo único nuevo es `analisis/`, y después este FRENO, en la ruta que le da el despacho (§6).

## 2. Paso 0

Lo corrí a las 15:34:14, con la carpeta personal reemplazada por `$HOME` (salida: `paso0_A2_2_b_A2_2b.txt` del paquete):

```
scratchpad: presente; foto_repo.py, armar_manifest.py, enmascarar_paquete.py y comparar_fotos_a22.py con el sha256 que tienen en el manifest.txt de la copia permanente de revision_A2_2_FRENO_a/ (a377b766…, 5a7db724…, 65eaf9a2…, 358c6c82…): no faltaba nada y no restauré nada
pwd: $HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg
rama: main
git status --porcelain --untracked-files=no: []
HEAD: 8c064ad3
asunto entre los 10 últimos: c630204b
veredictos_adjudicacion_a2_2.json en HEAD: a62498b6a5a3937845f5eaee27302f63e6e4adfcc29359ed7118989b23fc8c2e
en el árbol: a62498b6a5a3937845f5eaee27302f63e6e4adfcc29359ed7118989b23fc8c2e; git diff HEAD: sin cambios
analizar_a2_2.py: árbol 230f0c897fcafd838712256442ae543c71056ac8b9bd416952c68e909031b6d2, HEAD 230f0c897fcafd838712256442ae543c71056ac8b9bd416952c68e909031b6d2, último commit 40152be0
comun_a2_2.py: árbol 81dcc23c7121186bf2df03361eace0a4b480d657f4926dd3bd643f33816fb64e, HEAD 81dcc23c7121186bf2df03361eace0a4b480d657f4926dd3bd643f33816fb64e, último commit 40152be0
poblacion_a2_2.py: árbol c74ac60bf0bcf7531384ae54b7e500aadfb7b4cf2af43973f038fce51359f2c3, HEAD c74ac60bf0bcf7531384ae54b7e500aadfb7b4cf2af43973f038fce51359f2c3, último commit 40152be0
analisis/: no existe
sin rastrear en a2_2/ (antes de empezar): 3: a22_juez_r1.db a22_juez_r2.db a22_juez_r3.db
Neo4j: neo4j-bcra-kg-compose Up 27 hours (healthy)  (levantado desde el tramo 1; este tramo no lo usa)
```

- El asunto del despacho está, tal cual, en `c630204b`, el segundo de los 10 últimos (`git log -10 --format='%h %s' | grep -F`).
- Las tres bases sin rastrear son la caché del juez, en `a2_2/juez/cache/`. Ya estaban antes de empezar y no las toqué: las fotos no
  muestran ningún cambio fuera de `analisis/` (§6).

## 3. El selftest, en una copia

- **La copia:** a las 15:34:43, con el `rsync` de la cláusula más `--exclude=/data/experiment/neo4j/volumen`, en la carpeta temporal
  (salida: `selftest_copia_A2_2_b_A2_2b.txt`).
  - `rsync` dio 0 y saltó 336 enlaces (`--no-links`); su log va en el paquete.
  - En la copia hay 0 archivos `.env`, 0 `NO_ABRIR_`, 0 `*_SOLO_MESA*` y 0 enlaces.
  - En la copia, `shasum -c` de `sha256_tramo1_a2_2.txt` da OK.
- **El selftest:** corrió de 15:35:39 a 15:35:40, con
  `env -i PATH HOME <repo>/.venv/bin/python -B data/experiment/banco_mcp/a2_2/selftest_a2_2.py` desde la raíz de la copia. Dio
  «selftest A2.2: 34 de 34 en PASS», con rc 0. Son las mismas 34 pruebas que en la copia final 2 del tramo 1, en el mismo orden
  (`diff` de sus nombres: vacío).
- **El repo, antes y después** (`foto_repo.py`; `comparar_fotos_a22b.py`): la foto de las 15:34:15 y la de las 15:35:45 tienen 60.902
  entradas cada una. Entre las dos: 0 nuevos, 0 borrados, 0 cambiados y 0 fuera de lo autorizado. Los `.pyc` son 10.158 en las dos
  fotos, y fuera de los venvs, 243 en las dos.

## 4. El análisis, en el repo

Corrió a las 15:36:11, desde la raíz del repo (salida: `analisis_en_el_repo_A2_2_b_A2_2b.txt`):

```
comando: .venv/bin/python -B data/experiment/banco_mcp/a2_2/analizar_a2_2.py --adjudicaciones data/experiment/banco_mcp/a2_2/adjudicacion/veredictos_adjudicacion_a2_2.json
análisis escrito (40 preguntas; 3 pares sin veredicto final) -> data/experiment/banco_mcp/a2_2/analisis/analisis_a2_2.json
rc=0
```

Lo que imprime es lo que el despacho pide: cuántas preguntas tiene el análisis y cuántos pares quedan sin veredicto final. El código del
análisis es el de HEAD, sin editar (§2).

## 5. Los controles

Los hace `controles_analisis_a22b.py`, por código. Lo corrí a las 15:38:57 con el python del `.venv` del repo, con `-I -B` y
`env -i` (salida: `controles_analisis_A2_2_b_A2_2b.txt`). Antes lo había corrido dos veces. La primera fue a las 15:37:52; la hora de
la segunda no la tengo, porque la tercera sobrescribió su salida. Entre las corridas agregué el punto 3b y la cuenta previa a aplicar.
Las tres solo leen; vale la última.

1. **El JSON:** sha256 `a909247453e13563db36750b9488aee6e64cfc37d048a0c006ffe601fa1a8485`, 17.298 bytes.
2. **Las claves de primer nivel:** `que`, `n_preguntas`, `finales`, `sin_veredicto_final`, `n_sin_veredicto_final`, `principal`,
   `principal_sensibilidad_sin_final_como_0`, `sin_la_cola`, `c_agente_y_latencia`, `observado`, `predicciones`, `r5_por_brazo` y
   `no_comparabilidad_con_EV2`.
   - Las dos comparaciones del §5, `fragmentos_bm25` y `fragmentos_denso`, están en `principal`, en
     `principal_sensibilidad_sin_final_como_0` y en `sin_la_cola`, cada una con su Holm.
3. **Las adjudicaciones:** el JSON de la autora trae 8 ids, todos con un valor del vocabulario de la pregunta salvo
   `requiere_adjudicacion` (`mapping.VEREDICTOS_PREGUNTA` de EV2). Para cada uno:
   - aparece una sola vez entre las respuestas agregadas: 8; las 8 son de N = 1 y ninguna de las re-corridas;
   - era `requiere_adjudicacion`: 8;
   - toma el valor adjudicado con `aplicar_adjudicaciones`: 8;
   - llega al veredicto final de su par en el JSON escrito, con el origen «N = 1»: 8. Ninguna es la respuesta de N = 1 de un par de la
     población, cuya base no vota.

   La correspondencia entre id opaco y (pregunta, brazo, repetición) sale de `poblacion_a2_2.veredictos_por_par`, la función con que el
   análisis lee la tabla de la mesa. La tabla no la abrí ni la imprimí.
4. **La respuesta que sigue pendiente:**
   - Entre las respuestas agregadas había 9 en `requiere_adjudicacion` antes de aplicar las adjudicaciones, y queda 1 después.
   - Esa 1 es un voto de las re-corridas. Su par tiene veredicto final en el JSON, y ese final es el mismo con cualquiera de las tres
     resoluciones del voto (`agregacion_enc.detalle_par`, recomputado por código).
   - Es lo que fija el pre-registro firmado: «con un voto `requiere_adjudicacion` entre las tres re-corridas, el par queda decidido solo
     si el resultado no depende de cómo se resuelva ese voto» (`a78ead7b:docs/preregistro_A2_2_sistema_por_fragmentos.md:165-166`). Por
     eso ese voto no necesita adjudicación, y las 8 adjudicadas cubren todo lo que el análisis necesita.
   - Lo declaro porque el registro (`89370cc2`, §121) habla de 8 ids sin mencionar ese voto. La cuenta 9 → 1 es la única cuenta de una
     categoría del juez que imprimí, sin brazo ni pregunta. Si la mesa la prefiere fuera del FRENO, la saco.
5. **Los pares sin veredicto final:** son 3, los mismos que da `n_sin_veredicto_final` del JSON. Por causa:

   | causa | pares | de dónde sale |
   |---|---|---|
   | R3 en N = 1 | 1 | la sesión está en `juez/n1/faltantes_n1.json` con el motivo «incompleta por R3» |
   | R3 en las re-corridas | 1 | un par de la población con un voto ausente; esa re-corrida está en `juez/recorridas/faltantes_recorridas.json` con el motivo «incompleta por R3» |
   | sin juicio | 1 | una sesión de N = 1 que no está en `faltantes_n1.json` (fue al juez) y no tiene agregado. El asunto de `012cb030` habla de «la respuesta sin juicio de la comparacion con los fragmentos»; que sea esta, NO VERIFICADO |
   | sin adjudicación | 0 | — |
   | **total** | **3** | suma por causa: 3 |

   - Por origen, en el JSON: «N = 1 sin veredicto», 2; «re-corridas incompletas», 1.
   - Los faltantes del agente, en todas las sesiones: en N = 1, 1 incompleta por R3; en las re-corridas, 1 incompleta por R3.
   - Ninguno de los 3 pares queda pendiente de una adjudicación.

## 6. El repo

| foto | hora | entradas | contra la de antes |
|---|---|---|---|
| antes | 15:34:15 | 60.902 | — |
| después del selftest | 15:35:45 | 60.902 | 0 nuevos, 0 borrados, 0 cambiados |
| después del análisis | 15:37:18 | 60.903 | 1 nuevo: `analisis/analisis_a2_2.json` |
| después de los controles | 15:38:57 | 60.903 | el mismo 1 nuevo; nada más |
| antes de escribir este FRENO | 15:42:07 | 60.903 | el mismo 1 nuevo; nada más |

- En las cinco fotos: 0 fuera de lo autorizado; el volumen de Neo4j, 0 nuevos, 0 borrados y 0 cambiados; los `.pyc`, 10.158, y
  fuera de los venvs, 243.
- `git status --porcelain --untracked-files=no` sigue vacío.
- Después de escribir este FRENO en el repo tomo la foto final. Su comparación con la de antes va en el paquete
  (`comparacion_antes_vs_al_frenar_A2_2_b.json`); lo esperado es un archivo nuevo más, este FRENO, y nada fuera de lo autorizado.
- Sin rastrear en `a2_2/`, antes de escribir este FRENO, había dos carpetas: `analisis/`, la nueva, y `juez/cache/`, que ya estaba.
  Con el FRENO se suma `FRENO_A2_2_b.md`.
- **Una contradicción del despacho, que declaro:**
  - el despacho dice «En el repo escribís solo en `data/experiment/banco_mcp/a2_2/analisis/`», y el criterio 4 pide «el repo, con
    solo `analisis/` nuevo»;
  - pero «Cómo terminás» pone el FRENO en `data/experiment/banco_mcp/a2_2/FRENO_A2_2_b.md`, fuera de `analisis/`;
  - puse el FRENO en esa ruta, que el despacho nombra, y el comparador de fotos la autoriza aparte (`comparar_fotos_a22b.py`);
  - al terminar los controles, a las 15:38:57, lo único nuevo era `analisis/`; al frenar, son `analisis/` y este FRENO.

## 7. Lo que no hice

- No imprimí ni escribí ningún veredicto, tasa, diferencia, p ni predicción, ni ningún qid o brazo de un par.
- No abrí ninguna tabla `*_SOLO_MESA*`: la leen por código `poblacion_a2_2.veredictos_por_par`, cuando la usa el análisis, y mi control,
  que llama a esa misma función. La copia del selftest las excluye.
- No abrí EV2 ni lo imprimí. El análisis lo carga por código (`comun_a2_2.cargar_preguntas`); el control no lo carga.
- No abrí el JSON de las adjudicaciones ni el del análisis. Solo los leí por código, en el control, y solo imprimí cuentas.
- No corrí nada pago y no usé Neo4j. El contenedor sigue levantado desde el tramo 1, y su volumen no cambió.
- No escribí en `.claude/`, en la memoria ni en `.gitignore`. Para recuperar mis propios comandos del tramo 1 (el grep de convenciones y
  la copia del selftest), busqué por código en la transcripción de esta sesión. Imprimí solo entradas de mis propias herramientas de
  esa sesión: comandos, y un script que había escrito.
- No usé `sleep`. Todos los heredocs llevan el delimitador entre comillas.
- No entré en ninguna de las carpetas vedadas ni en las de lectura de la autora.
- No commiteé nada.

## 8. Errores propios, con su causa

1. **Una búsqueda falló.** Busqué `mapping.py` de EV2 con dos patrones de ruta que adiviné mal (`exploracion/ev2_juez/` y `*/ev2_juez/`).
   zsh cortó el comando, porque un glob sin coincidencias da error. Está en `data/experiment/ev2_juez/mapping.py`. No tuvo efecto: era
   una lectura.
2. **Corrí el control tres veces.** Lo extendí dos veces mientras lo corría, para explicar la respuesta que sigue pendiente (§5, punto 4).
   Debí escribir el punto 3b antes de la primera corrida. Las tres solo leen, y la foto de después de los controles no muestra ningún
   cambio.

## 9. Grep de convenciones

- Corrí `data/experiment/segmentacion_oficial_e0r2/s0_4/scripts/grep_convenciones.py`, con `LC_ALL=en_US.UTF-8`, sobre copias de
  4 archivos: el borrador de este FRENO, el JSON del análisis y mis dos scripts del tramo (`comparar_fotos_a22b.py` y
  `controles_analisis_a22b.py`). Dio: control positivo, 16 de 16; total, 0
  (`grep_convenciones_borrador_A2_2_b_A2_2b.txt`).
- Después de escribir el FRENO en el repo lo corrí otra vez, sobre él y sobre los 28 archivos del paquete ya enmascarados: 29
  archivos en total. El control positivo dio 16 de 16, y el FRENO, 0. En el paquete hay 118 coincidencias, ninguna con un nombre de
  persona ni con el origen conversacional de una decisión:
  - 114 están en las 6 fotos, 19 en cada una. Todas son claves de la foto, es decir, rutas de archivos del repo: archivos de
    `.venv/lib/` y cuatro documentos de `docs/` cuyos nombres contienen los términos 6.º, 8.º y 13.º de la lista de
    `grep_convenciones.py`. En los valores de la foto, 0.
  - 2 están en el checkpoint: son notas mías del tramo 1 que nombran el literal de la carpeta temporal (el término 16.º).
  - 2 están en `enmascarar_paquete_A2_2b.py`: es el patrón con que el enmascarado reconoce la carpeta temporal (el término 16.º).
  - La salida está en `grep_convenciones_final_A2_2_b_A2_2b.txt`, con las cuentas por archivo y por término.

## 10. El paquete

- **El paquete:** `revision_A2_2_b/`, en la carpeta temporal de la sesión, con su `manifest.txt`.
  - No lleva el JSON del análisis; lleva su sha256, en `sha256_analisis_a2_2_A2_2b.txt`.
  - Tampoco lleva el JSON de las adjudicaciones, que está en HEAD; su sha256 está en el §2.
- **La copia:** con `ditto`, en
  `~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/94968c98-6fa5-449c-954b-42ee7ee26062/scratchpad/revision_A2_2_b/`, verificada
  contra su `manifest.txt` (`armar_manifest.py --verificar`).
