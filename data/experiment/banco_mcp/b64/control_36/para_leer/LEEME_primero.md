# La muestra de control del juez de B6.4: qué hay en esta carpeta (mesa, §383, 01/11/2026)

Para leer a ciegas, después de tu adjudicación (pre-registro de B6.4, §13, punto 6). Antes de abrir nada más, la regla:
`regla_de_lectura_control_36_B64.md`.

- **`regla_de_lectura_control_36_B64.md`:** cómo se lee cada ficha, qué se anota y cuánto lleva.
- **`fichas/C01.md` a `fichas/C36.md`:** las 36 fichas. Las mismas, todas juntas, en `fichas_C01_a_C36.html`, para leer en el navegador,
  y en `fichas_C01_a_C36.md`.
- **`planilla_criterios_control_36_B64.csv`** (135 renglones, uno por criterio) y **`planilla_respuestas_control_36_B64.csv`** (36, uno
  por ficha): las dos planillas, vacías.
- **`estructura_planillas.json`:** las columnas y los renglones de las dos planillas, que controla el sellador. No se edita.
- **`como_se_mide_el_juez_control_36_B64.md`:** con qué cifras se mide el juez contra lo que anotes, y el piso.
- **`sellar_planillas_control_36_B64.py`:** el sello de tus dos planillas, al terminar.

**No abrís, hasta sellar las planillas:**
- nada de `fuera_del_repo/banco_b64/`: las sesiones de cada sistema, los juicios del juez y la población;
- de `fuera_del_repo/analisis_b64_corr/salidas/`, nada más que las consolas que ya leíste;
- la clave del sorteo, que dice de qué sistema sale cada ficha: `fuera_del_repo/banco_b64_control_36/clave_para_despues/`. Tampoco la de
  tu adjudicación.

**Lo demás de `banco_b64_control_36/`:** `copia_vacia/` trae la copia de las dos planillas vacías y el sha256 de cada archivo de esta
carpeta, anotados por el armado antes de que empieces. No la tocás.
