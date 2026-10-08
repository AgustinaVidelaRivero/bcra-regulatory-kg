# FRENO A1 — U-ALCANCE-E1: el registro de alcance por tanda en el mensaje de E1

08/10/2026, HEAD `7788e52`. Mandato FIRMADO (`docs/mandatos/UALCANCE_E1_cableado_registro_alcance.md`; versión para firmar en
`9e84741`, firma en `21e55a0`, sin cambios después: `git log -- <mandato>` da esos dos commits). Precisión al despacho: la firma está en
el commit de las firmas (`21e55a0`), no en el de los asientos. USD 0, sin API. Nada commiteado. El código del repo no se tocó: todo corrió
sobre copias sin enlaces y el cambio queda como parche, que A2 aplica una sola vez.

## Qué hice (`parche_UALCANCE_E1_A1.diff`: 5 archivos, +657 −13; `git apply --check` limpio sobre HEAD)
1. **Derivado.** `catalogo_unico/code/derivar_registro_alcance_r2b.py --tandas 1` lee el registro (`ce402aad7c84…`) con el lector de R2-2
   (`reresolver_catalogo.py:159` y `:199`, las funciones del ensamblado) y frena si su salida no es la de `registro_legible` (`:235`).
   Nueve entradas: de una clase, ri_ccna, ri_dcpc y manori; de dos clases, snp_cheq y nmcief; de rol reutilizado, ri_rml, ri_gerc y ri_pgn
   (`Sujeto_rol_entidad_comprendida_reginf`) y snp_tr (`Sujeto_rol_alcance_snp_tr_nc`). ri_oc, ceninf y cirmo3, sin entrada. sha256
   `68ac5c084a17…`, dos corridas iguales byte a byte (`salidas/bateria_a1.log`, paso 1; `salidas/reporte_derivado_tanda1.json`).
2. **`prompt_r2b.py`.** Lee el derivado al importar, con `_leer_con_candado` y su sha como literal (`:476-478`). La regla está en
   `alcance_del_documento` (`:481-487`): primero `ROL_POR_TO_R2`; si el archivo no está, el derivado; si no, sin línea. En
   `build_user_message_r2b` cambia solo `:409`, y sigue siendo función pura del chunk. Puse el bloque nuevo después de `:463`, para que las
   45 anclas a `prompt_r2b.py` de la tabla de reprocesamiento sigan en su línea.
3. **Candado del mensaje.** La fixture pasa de 13 a 17 unidades: cuatro copias de `cap::1.4.1`, con ri_ccna, snp_cheq, ri_rml y ri_oc
   (`scripts/sinteticos_fixture.py`). Los dos valores, calculados en dos procesos desde cero (`scripts/sellar_a1.py`), quedan PROPUESTOS:
   `CANDADO_MENSAJE_JSON_SHA256_ESPERADO` pasa de `4d69f7f4c8a5…` a `6b758517cee0…`, y `MENSAJE_R2B_SHA256_ESPERADO`, de `a9cb702c0d24…`
   a `eeb11b9a3bf6…`. Con el código nuevo, las 13 unidades de P3c-2 siguen dando `a9cb702c0d24…`. El sha del derivado también queda
   PROPUESTO: se fija en A2.
4. **`selftest_prompt_r2b`.** 11 casos nuevos (9 en la sección I y 2 en la G); dos de la G, reescritos para mirar las 13 primeras de la fixture.

## Controles (`scripts/bateria_a1.sh`, log en `salidas/`; reproducidos desde cero con el parche y estos scripts)
- **Tanda 0, por el camino del runner** (`runner_corpus.configurar` → `perfil_e1.perfil("r2b")`; `scripts/mensajes_runner_a1.py`). De las
  2.439 unidades de `salida_tanda0_r2b/`, 0 mensajes distintos. El sha de los mensajes es `48fdec197658…` con HEAD y con el nuevo, el de
  R2-2 (`reresolucion_catalogo/salidas/r2_2_controles_parte_a_y_mensaje.json`).
- **`selftest_prompt_r2b`:** 66/66 en la copia; HEAD sobre HEAD, 55/55. El selftest nuevo con el código y la fixture de HEAD da 55 ok y
  11 FAIL, exactamente los nuevos (`salidas/control_negativo_selftest_prompt_r2b.json`): 4 fallan por el mensaje o la fixture y 7 porque al
  módulo de HEAD le falta el derivado. En esos 7 (sin alcance, release primero, tanda 0, candado, regeneración, solo agrega, freno con el
  derivado alterado), la parte de comportamiento también se cumple con HEAD.
- **`selftest_clave_cache --salida-r2b`:** OK. A1r (OK, 2.449 claves) y A3r iguales a los de HEAD, 44 variaciones con los mismos tokens,
  contraste OK. Con HEAD, el JSON es el del repo byte a byte (`923dd900…`). El nuevo difiere en 6 líneas: el derivado aparece en dos
  inventarios y cambia el sha del texto de error de R29 y R29b (`salidas/diff_selftest_clave_cache_head_nuevo.txt`).
- **Repo:** foto sha256 de todos los archivos antes y después de cada batería, iguales; 2.213 `.pyc`.

## Tanda 1: documentos cuyo mensaje cambia (ejemplo del §7 del protocolo, con ri_pgn)
En la partición vigente (`segmentacion_84/b584_particion/`), los 20 documentos suman 3.275 unidades: las 3.292 del ejemplo
(`a304b89:docs/protocolo_entre_tandas.md:284`), menos 36 de ri_cc, más 19 de ri_pgn. Cambian 892, solo en la línea de alcance. Por
documento, las unidades y, entre paréntesis, las de la salida de S1, en disco y sin commit: ri_ccna 22 (31), ri_rml 32 (27), ri_gerc 15
(15), ri_pgn 19 (19), ri_dcpc 129 (116), snp_cheq 528 (362), snp_tr 89 (89), manori 18 (145) y nmcief 40 (40). No cambian los 8 con
entrada en la release, ni ri_oc, ceninf y cirmo3. Tokens y costo, en A2, con la lista final que sale de S2
(`salidas/comparacion_mensajes_head_nuevo.json`).

## Contradicciones y hallazgos (para la autora)
1. **Ruta del derivado.** El mandato lo pone en `catalogo_unico/generados_r2/`, pero K2 de `selftest_catalogo_unico.py:387-392` exige ahí
   solo los generados del catálogo: con el archivo en esa carpeta, K2 falla (`scripts/k2_generados_r2.py`). Por §4.d lo puse en
   `catalogo_unico/registro_alcance_r2b.json`, y K2 pasa.
2. **F13c y el contraste.** El texto propuesto está en `f13c_texto_propuesto.md`, sin aplicar. La variante A («cambia», como F12) frena el
   contraste de `selftest_clave_cache`, porque necesita una variación nueva (R34) en un archivo que no está entre las escrituras; la B
   («no cambia», con R20) pasa (`salidas/contraste_f13c.json`). Recomiendo A, con R34 y `selftest_clave_cache.json` regenerado en A2.
   El JSON hay que regenerarlo igual, porque su inventario cambia.
3. **Pasajes de la tabla que quedan desactualizados con A2,** fuera de F13c: el inventario del §1 (`:73-80`), «No los abre…» (`:86-88`),
   la lista de F11b (`:163`) y la nota de F13 (`:253-261`).
4. **Perfil y manifiesto.** `perfil_e1.py:236` expone `rol_por_to = ROL_POR_TO_R2`, que valida `manifiesto_corpus.py:162` y usa
   `armar_manifiesto_S1.py:55`: el manifiesto de la tanda 1 va a declarar `rol_alcance` null para los 9, aunque su mensaje lleve la
   línea. No rompe nada.
5. **Tandas del derivado.** ri_cc, de la tabla «Tanda 3 (anticipada)» del registro, queda fuera por `--tandas 1`. snp_tr hereda de
   snp_tr_nc `miembros_ids` vacío, como en la release; la línea usa las etiquetas.

## Errores propios, corregidos antes de este FRENO
- La primera versión ponía el código nuevo arriba y corría las 45 anclas. La descarté; no llegó al repo.
- La comparación por id juntaba los ids repetidos de la partición legada (ceninf 43 de 47, cirmo3 188 de 240). Ahora cuenta por posición.
- `sellar_a1.py` buscaba marcadores que ya no estaban (rc=1 en la primera batería), y `mensajes_runner_a1.py` se contaba a sí mismo al
  correr desde el repo. Corregí los dos y repetí la batería entera.

Grep de convenciones sobre los 33 archivos escritos (esta carpeta y los cinco del parche): 0 nombres de personas, 0 rutas absolutas y
0 referencias al origen de una decisión; el control positivo da 1. Paquete `revision_UALCANCE_E1_FRENO_A1/`. Commit PENDIENTE de la
autora; A2 espera la lista final de la tanda 1. FRENO A1.
