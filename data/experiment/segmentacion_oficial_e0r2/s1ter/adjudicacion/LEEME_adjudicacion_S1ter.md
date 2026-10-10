# U-SEG-OFICIAL, S1-ter: adjudicación de la lectura a ciegas en dos pasadas (registro de la mesa, 10/10/2026)

USD 0, sin API. Decisiones de la autora del 10/10/2026, tomadas sin haber abierto nada de la lectura ni del material de la pasada 1. Se
registraron en la hoja de ruta de la mesa a las 18:22:47 (§54) y a las 18:35:16 (§56).

## Diseño

- **Pasada 1:** la autora califica sin ver la marca, la clase, la subclase ni la nota de la lectora. Cada ficha va con sus imágenes y
  con una planilla vacía con las columnas del TSV de adjudicación. En la etapa 2 califica también la unidad que sigue y lo heredado.
  Sella su pasada 1 antes de ver nada de la lectora.
  - **Etapa 1:** las 90 fichas, todas, en el orden
    `random.Random("U-SEG-OFICIAL:adjudicacion:S1-ter:etapa_1").sample(sorted(ids), len(ids))`.
    - Motivo: el tamaño de una lista armada con las marcas de la lectora deja ver si el piso está en riesgo. Así, además, ninguna ficha
      que la lectora dio por correcta queda sin que la mire una persona, y el acuerdo se mide sobre las 90.
    - La semilla de las 20 correctas de la etapa 1 (`U-SEG-OFICIAL:cortes:S1-ter:revision`) queda registrada y sin uso.
  - **Etapa 2:** la lista de `scripts/lista_para_la_autora_S1ter.py`, en el orden
    `random.Random("U-SEG-OFICIAL:adjudicacion:S1-ter:etapa_2").sample(sorted(ids), len(ids))`. La lista está formada por los errores, las
    dudosas, las correctas con nota y las 5 correctas de control.
    - **Declarado:** la lista es casi toda de fichas señaladas por la lectora (solo 5 de control), y su acuerdo se mide sobre una
      muestra elegida según esas marcas.
- **Pasada 2:** va toda ficha en la que se da al menos una de estas condiciones:
  - a. la marca de la autora y la de la lectora no coinciden;
  - b. las dos marcaron error, pero una lo clasificó como de corte y la otra como de limpieza;
  - c. la lectora dejó una nota, en cualquiera de las dos etapas, aunque la marca coincida;
  - d. en la etapa 2, la autora marcó `la_que_sigue` o la herencia como error.

  La subclase no se compara: queda la de la pasada 1. Las notas de la lectora no se clasifican: van tal cual.
- **El TSV de adjudicación** es la pasada 1 corregida por la pasada 2. Lo lee `scripts/aplicar_adjudicacion_S1ter.py` sin cambios.
- **El acuerdo** entre la lectora y la pasada 1 se calcula después de la adjudicación, como dato para la tesis.

## Archivos

- `preparar_pasada_1_S1ter_v2.py` y `pasada_2_S1ter_v2.py`, con su prueba sobre datos sintéticos
  (`prueba_adjudicacion_dos_pasadas_S1ter_v2.py`, salida en `salida_prueba_adjudicacion_dos_pasadas_S1ter_v2.txt`: 30 de 30).
  - Están sellados en `sello_scripts_adjudicacion_v2_mesa.txt` a las 18:38:13, antes de armar la pasada 1 nueva de la etapa 1.
  - La versión 1, sellada a las 18:26:49, no entra al repo: tenía la etapa 1 armada con la lista y la regla de la pasada 2 que
    reemplazó la decisión del §56. Está archivada en el paquete de la mesa, `adjudicacion_S1ter/reemplazados_20261010_1835/`, con el
    material de su etapa 1 marcado `NO_ABRIR_`.
- `orden_pasada_1_S1ter_v2.json`: el orden de cada etapa (ids opacos), las semillas y el sha256 del `manifest.txt` de cada etapa, sin
  marcas.
- **Material de la pasada 1,** fuera del repo, en `~/INGENIERIA IA/TESIS/fuera_del_repo/adjudicacion_s1ter/pasada_1/`:
  - `etapa_1/manifest.txt` `52b4bf7b72da2ba67cdf4fa9e2cdbfee685e4a07fafa6d7c640ae785ad8a94ab`;
  - `etapa_2/manifest.txt` `4ffbd002e8778ad13e36e02696507d8ca06d70ae9a15eff08b7c87e9c0c3aa72`.
- **La lista con las marcas de la lectora** (`NO_ABRIR_…`) queda en el paquete de la mesa hasta después de la adjudicación.
