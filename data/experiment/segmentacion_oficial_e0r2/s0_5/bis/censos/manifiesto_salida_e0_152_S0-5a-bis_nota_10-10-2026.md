# Nota del 10/10/2026 al manifiesto de la salida final de S0-5a-bis (mesa)

`manifiesto_salida_e0_152_S0-5a-bis.json` (salida `176cbdc0…`) declara en `codigo_sha256` el `selftest_e0.py` `789630b5…`. La corrida
FINAL de la segunda vuelta, la que dio esa salida, corrió con otro: `9921eae1d57c7dc045a17f4417c9d1e18281dad74d3632be25b33e12b9b5c175`.
El manifiesto no se modifica; esta nota corrige su declaración.

- **Cuál corrió.** La raíz de la corrida FINAL (`raices/final/`, en el scratchpad de la sesión de S0-5a-bis) tenía:
  - `e0_lib.py` `bd2190ad…` y `correr_e0.py` `68bd74b5…`, los declarados;
  - `selftest_e0.py` `9921eae1…`.
  Los tres tienen fecha de modificación 09/10/2026 16:48:59 (`stat`), y el log de la corrida (`trabajo/logs/c_FINAL.log`, «listo 152 TOs,
  0 con error») se modificó por última vez a las 16:55:15. Ancla: `sha_codigo_vuelta2_S0-5a-bis.txt`, renglones 3, 9 y 14, en el paquete
  de revisión de la sesión (sha256 `98b49b54c822c71fb59f32d802f4bc4f9565deb0b97ef4e905c11c343fdad083`), en la copia permanente
  `fuera_del_repo/scratchpads/0c0c6584-4c87-4d3c-b3b4-425c9ab87db2/scratchpad/revision_USEG_OFICIAL_FRENO_S0-5a-bis/`. El scratchpad de la
  sesión se borra a los tres días: los dos `selftest_e0.py` y su diff están copiados en el paquete de la mesa
  (`hoja_de_ruta_tanda1_mesa/revision_S0-5a-bis/evidencia_selftest/`).
- **Qué cambia entre los dos.** Un renglón del docstring, el 123: «corriendo e0-r2 sobre 21 TOs» en `9921eae1…` y «sobre 22 TOs» en
  `789630b5…` (`diff`, 1 renglón de cada lado).
- **Efecto sobre la salida: ninguno.** `correr_e0.py` y `e0_lib.py` no importan `selftest_e0`
  (`grep -n -E "^\s*(import|from)\s.*selftest"` sobre los dos, rc 1). La revisión de la mesa corrió los 152 con `selftest_e0.py`
  `789630b5…` y dio 768 de 768 archivos iguales al manifiesto (paquete de la mesa, `revision_S0-5a-bis/`, §3).
- **El selftest.** El 188/188 de `selftest_e0_S0-5a-bis.txt` corrió con `789630b5…`, dentro de la copia
  (`sha_codigo_del_selftest_e0_S0-5a-bis.txt`). El archivo que deja el parche, y que aplica S0-5b, es `789630b5…` (`parche/LEEME.md:17`).
