# U-SEG-OFICIAL — FRENO S0-5b (10/10/2026)

S0-5b aplica al repo, una sola vez, el código de E0 de S0-5a-bis y corre sus controles. USD 0, sin API.
**Nada commiteado** y ningún mensaje de commit preparado: el commit lo arma la mesa. S0-5b no agrega reglas.
- Detalle: `REPORTE_S0-5b.md`.
- Salidas: `controles/` y `manifiestos/`.

**Entrada** (`controles/precondiciones_S0-5b.txt`):
- `97a54a5c` y `3c5f0034` están en el log; HEAD es `3c5f0034`.
- La nota del 10/10/2026, leída en `3c5f0034` (mandato `a6c7de69…`).
- E0 del repo = S0-4b (`65a8c3b8…`, `94d35349…`, `ec186071…`), y el parche da `421ee913…`.
- Foto a las 00:53:39 (48.589 archivos) y 2.213 `.pyc`.

**El parche, una sola vez** (`controles/parche_aplicado_S0-5b.txt`), desde `e0_chunking/`:
- la prueba en seco da rc 0, con los tres archivos y sin offset ni fuzz;
- `patch -p1` a las 00:54:01 da rc 0, sin `.orig` ni `.rej`;
- los tres sha finales: `e0_lib.py` `bd2190ad…`, `correr_e0.py` `68bd74b5…` y `selftest_e0.py` `789630b5…`;
- `git diff --stat` muestra solo esos tres, +1.167 −23;
- el interruptor del prototipo no se aplicó: `S0_5_REGLAS` y `S0_5_TANDA0` dan 0 en los tres archivos.

**Controles.** Corrieron con el código del repo y escribieron las salidas en una copia hecha con `rsync`, sin enlaces. El
código es el mismo en el repo, la copia y la raíz mínima.
- **Los 152, dos veces:**
  - 768 de 768 iguales entre sí;
  - iguales al manifiesto de S0-5a-bis `176cbdc0…`, y a la salida final de su segunda vuelta;
  - **9.665 unidades**; manifiesto en `manifiestos/manifiesto_salida_e0_152_S0-5b.json`.
- **Tanda 0:** 57 de 57 iguales a `salida_tanda0_r2b/`; los 25 de la tanda 0 dentro de los 152, 25 de 25.
- **Selftests sobre la copia:** `selftest_e0` **188/188**; b52 39/39, b581 34/34, b582 59/59 y b583 33/33.
- **Claves de la caché:** VEREDICTO OK; la salida es igual byte a byte a `923dd900…`.
- **Continuidad: 88 saltos**, con el JSON y la lista iguales byte a byte a los de S0-5a-bis. La cuenta es
  104 − 11 − 6 + 1 = 88:
  - R5-f cierra 11 de ri_ccna;
  - R5-d cierra 6: ri_rml 1.2.4 y 5 de snp_tr, con 15 descendientes tragados;
  - aparece 1: snp_cheq 3.3.6.1, de clase (i).

  El selftest del control da 14/14.
- **La diferencia sin efecto que anota la mesa** (`9921eae1…`) no se repite: todo corrió con `789630b5…`, y la
  salida es la del manifiesto.

**Límite medido, sin tocar porque no está autorizado** (`controles/anclas_e0_tabla_S0-5b.txt`):
- La tabla de reprocesamiento cita el código de E0 por número de renglón. Busqué cada bloque citado, entero, en el código
  aplicado.
- **14 de las 17 citas se corren:** F16b 2, F18a 2, F18b 1, F19b 5, F20 2, F21 1 y la nota de F18a 1. El destino de
  cada una está en ese archivo; ninguna queda sin encontrar.
- Quedan donde estaban F01 `correr_e0.py:86-94`, F19b `:95-100` y F21 `:77-80`.
- Para la mesa:
  - corregir las 14;
  - decidir si F19b cita también las reglas de S0-5.
- En la salida no hay ningún límite nuevo: es la de S0-5a-bis, byte a byte, y sus 209 límites siguen.

**Repo** (`controles/comparacion_fotos_S0-5b.txt`):
- La foto de las 01:20:31 da 48.619 archivos y HEAD sigue en `3c5f0034`.
- **De S0-5b:** solo los 3 archivos de E0 y los 29 nuevos de `s0_5/b/`.
- **De otra mano, 4 archivos**, sin commitear; no los escribí:
  - la nota de la mesa en `s0_5/bis/censos/manifiesto_salida_e0_152_S0-5a-bis_nota_10-10-2026.md` (00:57:59);
  - tres mandatos de `docs/mandatos/` con notas nuevas al pie (+14, +21 y +25; 0 renglones quitados).
- `.pyc`: 2.213, la misma lista.
- Grep de convenciones sobre los 29 archivos de `s0_5/b/` (control positivo 16 de 16): **0 coincidencias**. No hay nombres de personas, referencias al origen de una decisión ni rutas absolutas (`controles/grep_convenciones_S0-5b.txt`).

**Paquete:** `revision_USEG_OFICIAL_FRENO_S0-5b/`, 44 archivos más `manifest.txt`. Lleva:
- el FRENO y el informe;
- el registro de `s0_5/b/`;
- los tres archivos de E0 del repo aplicado y el parche;
- las fotos y los logs;
- la salida de E0 en `e0_salida_S0-5b.tar.gz` (`c152_1/` y `t0/`).

La copia permanente se hizo con `ditto` en
`~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/0c0c6584-4c87-4d3c-b3b4-425c9ab87db2/scratchpad/revision_USEG_OFICIAL_FRENO_S0-5b/`:
**44 de 44 iguales a su `manifest.txt`** (sha256 y bytes), ninguno sin listar. El tar.gz, extraído, da 768 de 768 y 57 de 57 iguales a sus manifiestos.

FRENO S0-5b.
