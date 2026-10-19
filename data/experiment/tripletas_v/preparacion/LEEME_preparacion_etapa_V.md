# La preparación de la etapa V de la evaluación por tripletas

Copia del paquete de revisión de la unidad (`revision_U-TRIP-V/`, `manifest.txt` con sha256 `61978e22…`), commiteada antes de la primera
lectura del gold, para que el sello del sorteo quede anclado en git. Las cifras y los controles están en `FRENO_U-TRIP-V.md`.

- **Lo que no está acá:**
  - `salidas/copia.rsync.log`, que excluye el `.gitignore` de la raíz (`*.log`). Su sha256 está en `manifest.txt`;
  - las hojas de la autora, que se commitean selladas, con sus resultados. Sus sha256 vacías están comentadas en `manifest.txt`.
- **`lectura/sellar_hoja.py`** es la copia del script que sella cada hoja (mismo sha256 que la de la carpeta de lectura).
- **Los scripts** leen y escriben en la carpeta de trabajo fuera del repo (`comun_v.py`, `RAIZ`). Se reproducen sobre una copia, nunca
  desde acá.
- **La semilla, N = 3.967 y el estrato «otros»** van en la nota al pie del 19/10/2026 de `docs/preregistro_evaluacion_tripletas.md`.
