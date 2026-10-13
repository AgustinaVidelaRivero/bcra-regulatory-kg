# U-SEG-OFICIAL, S0-6b: decisiones de la autora y declaraciones de la mesa (13/10/2026)

USD 0, sin API.
- **Qué es:** una nota de la mesa revisora que entra con el registro de S0-6b, por decisión de la autora (hoja de ruta de la mesa, §83
  y §84).
- **Lo que no cambia:** ningún archivo de la ejecutora en `s0_6/b/`, ni lo ya commiteado.
- **Ids de unidades:** no lleva ninguno.

## 1. Decisiones de la autora del 13/10/2026 (§83), tal cual

- a. «Acepto los dos agregados del §82: la parte de S0-6a de la sesión de la ejecutora (las 450 unidades nuevas) en la adenda 4, y la
  exclusión sin orden extendida a ri_sef y ri_ccpnp.»
- b. «No se miden las sesiones anteriores a la corrección (de S0-1 a S0-5b y de S1 a S1-ter). Se declara el corte: S1-ter midió la E0
  sin corregir sin sacar esas unidades, y así las dos lecturas siguen comparables.»
- c. «Apruebo la celda R24 de F19d, como la trae el despacho: la misma que F19b, porque sin variación el selftest de claves de la caché
  frena.»

## 2. La aprobación de las celdas de F19d (§84)

- **Qué aprobó:** las celdas de las claves E1 y E3 de F19d que empiezan con «cambia», como en F19b. La autora lo aprobó el 13/10/2026,
  antes de despachar S0-6b.
- **Por qué hacía falta:** el selftest de claves de la caché compara la primera palabra de esas celdas con lo que da la variación de la
  fila. R24 da «cambia» en E1 y en E3, y con «no cambia en la tanda 0», como las proponía el REPORTE de S0-6a-bis, frena. Lo encontró
  la mesa al probarlo, después de afirmar en el §82 que R24 bastaba sin haberlo corrido.
- **Con esas celdas:** VEREDICTO OK. El JSON cambia contra el de S0-6a-bis solo por la fila F19d (`controles/comparar_clave_cache_S0-6b.json`).

## 3. Declaraciones de la mesa sobre S0-6b

- **El código de E0 de este commit** es el que aplicó S0-6b. El manifiesto de la salida (`manifiestos/manifest_salida_e0_152_S0-6b.json`)
  dice «PENDIENTE (lo fija el commit de la autora)» en `commit_codigo`, porque se escribió antes del commit: el commit es este.
- **El control de anclas por contenido** (`scripts/control_anclas_contenido_S0-6b_mesa.py`, de la mesa) pide Python 3.10 o posterior:
  con el 3.9 del sistema falla al leer la anotación `int | None`. Corrió con el `python` del `.venv` del repo (3.10).
- **El control de las leídas** corrió con un TSV de solo encabezado y sin `--regla`, porque el TSV de las 40 filas está en el paquete de
  la mesa, que la ejecutora no podía leer.
  - Eso no cambia lo que se controla: el corte, la herencia y los campos de cada leída no dependen del TSV.
  - Sí cambia, en el JSON `NO_ABRIR_`, más que el campo `al_freno`: el veredicto, la clase y la subclase de cada pregunta de S1-ter; y
    en el resumen, `al_freno`, `al_freno_por_lo_que_cambia`, `fuera_del_freno_por_fila_del_tsv` y `filas_del_tsv_sin_unidad_leida`.
  - Sin `--regla`, `reglas_solas` e `igual_a_la_regla_sola` quedan vacíos.
  - El archivo abierto (`censos/control_leidas_S0-6b.json`) no copia ninguno de esos campos.
- **El paso 0** muestra `$HOME` en lugar de la ruta expandida que pedía el despacho, para no escribir el usuario de la máquina en el
  repo.
- **El log de los controles** (`controles/lote_controles_S0-6b.log`): la regla `*.log` de `.gitignore` lo deja fuera, y entra con
  `git add -f`, sin tocar `.gitignore`, como los de S0-6a y S0-6a-bis (decisión 16 de la autora, §81).

## 4. S1-quater: lo que mide esta etapa y un límite

- **Las unidades vistas en S0-6b:** ninguna.
  - La mesa midió la sesión de la ejecutora desde el despacho de S0-6b con el criterio de la adenda 4 (el de la adenda 3), y no aparece
    ninguna unidad.
  - Los archivos de `s0_6/b/` no traen texto de unidades; sus únicos ids son los de las 286 leídas.
  - No hace falta una adenda 5 por S0-6b.
- **El JSON abierto del selftest de claves de S0-6a-bis** (`s0_6/bis/controles/selftest_clave_cache_S0-6a-bis.json`, commit 49, igual
  al de S0-6a):
  - no trae texto de unidades;
  - trae ids: de la tanda 0, que sale de S1-quater por construcción, de una leída, de una fila y de una unidad más, que el código del
    propio selftest nombra como unidad de una de sus variaciones;
  - ningún id es texto, y la regla única de S1-quater cuenta el texto visto. Queda como está y se declara.
- **Límite de la medición:**
  - la medición cuenta una unidad como vista si aparece un tramo distintivo de 6 tokens de su texto, o su texto entero si tiene de 3 a 5
    tokens;
  - una cita más corta que no es el texto entero de una unidad no cuenta;
  - el caso a la vista: un comentario viejo del código de E0 (`e0_lib.py`, la ampliación de la regla 3 de S0) trae seis citas cortas, de
    1 a 5 tokens, que aparecen en 5 unidades de la E0 de S1-ter. Una sale por las adendas; las otras 4 siguen en la población de
    S1-quater. Se declara como límite de S1-quater.
