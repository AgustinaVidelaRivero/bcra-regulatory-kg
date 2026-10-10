# U-SEG-OFICIAL — FRENO S1-ter-b2 (10/10/2026)

Las fichas de las dos etapas muestran ahora el número que E0 le asignó a la unidad; la etapa 2 tiene las imágenes que faltaban de la
unidad que sigue, y el script de la adjudicación queda fijado antes de la lectura. Seguí las decisiones de la autora sobre el FRENO
S1-ter-b (texto copiado en el paquete). USD 0, sin API; Python 3.10.13.
- Escribí solo `s1ter/tramo_b2/`, 5 scripts nuevos en `s1ter/scripts/`, el scratchpad y, en la carpeta de la lectora, lo autorizado.
- Nada commiteado y ninguna cifra de lectura. No toqué `fichas_S1ter.py`, `tramo_b/`, `cifras_lectura_S1ter.py` ni
  `lista_para_la_autora_S1ter.py`.
- sha256 de lo escrito: `tramo_b2/manifest_tramo_b2_S1ter.json` (`86a1a40a…`, todo salvo este freno).

**Foto de partida** (17:08:45, 49.599 archivos; `control_declarados_foto_partida_S1ter_b2.txt`): contra mi foto final del tramo b,
solo los 7 archivos nuevos y el cambiado de `ed0fcd0b` y `785cca7c`, los 8 con el sha256 del texto. HEAD `785cca7c`. Ningún
`.DS_Store` cambió.

**Las fichas** (`scripts/fichas_numero_S1ter.py`, sobre una copia de la carpeta en el scratchpad; después copié a la carpeta solo
lo autorizado):
- Cada ficha lleva un renglón nuevo, el primero después de su encabezado: `- número que le asignó la segmentación: <n>` o `… sin
  número`. El número sale del campo `unidad` del chunk de E0 de la unidad que se califica, con la regla del punto 3.
- **Conteos del punto 4**, iguales a los esperados (`controles_fichas_numero_S1ter_b2.txt`):
  - etapa 1: 90 renglones, 78 con número y 12 sin número;
  - etapa 2: 101 renglones, 96 con número y 5 sin número;
  - en la etapa 1, la ficha que es una parte y las 8 introducciones o cierres muestran el número de su punto;
  - en la etapa 2, la ficha cuya unidad está partida en 3 partes muestra el del punto partido.
- **Comparación del punto 5:** sin los renglones nuevos, cada archivo de fichas es, byte a byte, el que listan los `manifest.txt`
  `b3606f03…` y `6692fbea…`. Cambian solo los dos archivos de fichas y los dos `manifest.txt`. En la etapa 1 no hay archivos nuevos y
  las 137 imágenes quedan iguales. En la etapa 2, los únicos nuevos son las 8 imágenes del punto 6, y las 171 de antes quedan iguales.
- **Las imágenes de la unidad que sigue:** agregué las 8 páginas del punto 6 (en `E2-003`, `E2-049`, `E2-055`, `E2-057`, `E2-085` y
  `E2-099`), con el mismo comando y el mismo tipo de nombre. Ahora toda página de la unidad que sigue tiene su imagen: **104 de 104**.
  La etapa 2 pasa de 171 a 179 imágenes.
- **Control a ciegas,** sobre la copia y sobre la carpeta (`control_ciego_carpeta_lectora_S1ter_b2.txt`): fuera del texto de la norma,
  en las dos etapas, 0 «::», 0 ids de unidad, 0 TOs y 0 términos de población, regla, tanda o límite.
- **Los `manifest.txt` nuevos,** con el formato de antes, verificados en la carpeta (`verificacion_carpeta_lectora_S1ter_b2.txt`):
  - etapa 1: `305bf339e45897b1d92d759ea63b985dfc294f2405b3aacf54c8bb5f25f1359f`, 138 de 138;
  - etapa 2: `feff1c085178803a857390b61e6ce1d8aac3a7dbc3b5d74d3cba474117f1f244`, 180 de 180.

  Copia de los dos en `tramo_b2/`. Nada sin listar y ningún `.DS_Store`.

**El script de la adjudicación,** `scripts/aplicar_adjudicacion_S1ter.py`, con las dos reglas de la autora fechadas en su docstring
(el cierre y la herencia). Valida con las funciones de `cifras_lectura_S1ter.py`, sin editarlo, y su planilla adjudicada tiene las
mismas columnas que la de la lectora.
- Cuando el error de la fila y el del cierre coinciden en una lista de (b), prevalece `corte`. El de limpieza que pierde pasa a la
  columna `limpieza`, y un segundo error de corte, a `subclase_adicional`. Así ninguno se pierde y `cifras_lectura_S1ter.py` cuenta los
  dos.
- `nota` queda la de la autora si trae una; si no, la de la lectora.

**Prueba con datos sintéticos** (`scripts/prueba_aplicar_adjudicacion_S1ter.py`; salida en `prueba_aplicar_adjudicacion_S1ter_b2.txt`,
sin ids). Corre el script por su línea de comandos y da **26 de 26** controles bien:
- **Listas de (b):**
  - un cierre con error de corte deja la fila como corte; cuenta y revierte;
  - un cierre con error de limpieza deja la fila como limpieza; cuenta y no revierte;
  - una fila con error de limpieza y un cierre con error de corte queda como corte; el JSON registra las dos clases.
- **Otras fichas:** un error en la unidad que sigue en una ficha de (a), en una de la regresión, en `ri_oc::S2` y en la de la sección 3
  no cuenta, y la fila no cambia.
- **Herencia:** en la unidad de la sección 3 cuenta como falla de la corrección y la marca no cambia; en otras dos fichas, una por
  etapa, se registra y no cuenta.
- **Sin adjudicación,** las planillas quedan byte a byte iguales a las de la lectora, y `cifras_lectura_S1ter.py` lee las planillas
  adjudicadas.
- **Mal formados:** 8 archivos distintos se rechazan sin escribir nada. Controlé a mano que cada uno falla por su motivo.

**Convivencia** (foto de partida y final; `convivencia_S1-ter-b2.txt` del paquete): 16 archivos nuevos, todos míos: 11 en
`s1ter/tramo_b2/` (con este freno) y 5 scripts en `s1ter/scripts/`. Ninguno cambiado ni borrado, ninguna escritura de otra mano y
ningún `.DS_Store` cambiado. HEAD `785cca7c`; 2.213 `.pyc`.
**Grep de convenciones** (script de S0-4, control positivo 16 de 16; `grep_convenciones_S1-ter-b2.txt` del paquete): 0 coincidencias
en los 14 archivos de texto que escribí, en los 2 JSON y en la copia del texto del despacho. En las fichas de la lectora, las mismas 11
de antes, todas en el texto de la norma.
**Paquete:** `<scratchpad>/revision_USEG_OFICIAL_FRENO_S1-ter-b2/`, 27 archivos más `manifest.txt`: este freno, la copia del texto del
despacho, el registro de `tramo_b2/`, los 5 scripts, un tar.gz de la carpeta de la lectora como quedó, las fotos, el grep y los logs.
**Copia permanente** con `ditto` en
`~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/64082b65-8548-487d-9ff4-27e8bb6283c5/scratchpad/revision_USEG_OFICIAL_FRENO_S1-ter-b2/`,
verificada contra su `manifest.txt`: 27 de 27 iguales por sha256 y bytes, ninguno sin listar. El tar.gz, extraído, da 138 y 180 archivos
iguales a los `manifest.txt` nuevos.

FRENO S1-ter-b2. Espero la revisión.
