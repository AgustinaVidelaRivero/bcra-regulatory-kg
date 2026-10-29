# La muestra de control del juez de B6.3: qué hay en esta carpeta (mesa, unidad C36_a, 29/10/2026)

Para leer a ciegas, apenas esté la muestra (pre-registro de B6.3, §7.3). Antes de abrir nada más, la regla:
`regla_de_lectura_control_36_B63.md`.

- **`regla_de_lectura_control_36_B63.md`:** cómo se lee cada ficha, qué se anota y cuánto lleva.
- **`fichas/C01.md` a `fichas/C36.md`:** las 36 fichas. Las mismas, todas juntas, en `fichas_C01_a_C36.html`, para leer en el navegador,
  y en `fichas_C01_a_C36.md`.
- **`planilla_criterios_control_36_B63.csv`** (130 renglones, uno por criterio) y **`planilla_respuestas_control_36_B63.csv`** (36, uno
  por ficha): las dos planillas, vacías.
- **`estructura_planillas.json`:** las columnas y los renglones de las dos planillas, que controla el sellador. No se edita.
- **`como_se_mide_el_juez_control_36_B63.md`:** con qué cifras se mide el juez contra lo que anotes, y el piso de varios puntos.
- **`sellar_planillas_control_36_B63.py`:** el sello de tus dos planillas, al terminar.

**No abrís, hasta sellar las planillas:**
- nada de B6.3 en el repo (`data/experiment/banco_mcp/b63/`): ahí están la entrada, las corridas y lo que dejó el juez;
- nada de `fuera_del_repo/banco_b63/`: las sesiones de cada sistema, los juicios del juez y la población;
- la clave del sorteo, que dice de qué sistema sale cada ficha. Está en el paquete de la mesa (`revision_C36_a/clave_para_despues/`), no
  en esta carpeta ni en ninguna otra de `control_36_b63/`.

**Lo demás de `control_36_b63/`:**
- **`../sorteo/`:** la regla, el script y el sello del sorteo, sin su resultado, y el script que armó estas fichas. Se selló antes de
  correrlo. Se puede leer.
- **`../copia_vacia/`:** la copia de las dos planillas vacías y el sha256 de cada archivo de esta carpeta, anotados por la mesa antes de
  que empieces. No la tocás.
- **`../cruce/`:** el script con que la mesa cruza tu lectura con los juicios del juez, después de tu sello, y su prueba con datos de
  juguete. No hace falta abrirlo para leer.
