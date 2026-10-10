# U-SEG-OFICIAL, S1-ter: incidentes declarados de la lectura a ciegas (registro de la mesa, 10/10/2026)

La lectura terminó con las dos etapas selladas por `claude-opus-5-5`:
- etapa 1: `planilla_etapa_1.tsv`, sha256 `90b4e7aa1fcf3c38a34b3f141155a9e508e3f602e36888312077f0458eb2138b`, a las 17:58:13 (−03);
- etapa 2: `planilla_etapa_2.tsv`, sha256 `a06cdd0a8bff20824a82b4d60f61ec766c39e3173123427d5bf722bd47d03267`, a las 18:14:26 (−03).

Los controles de la mesa están en su paquete, `revision_lectura_S1ter/`. Se hicieron sin abrir marcas ni texto de la lectura: las
planillas, las carpetas y las sesiones, por su transcripción. Las dos sesiones se abrieron en su carpeta (`pwd` del paso 0) y no
escribieron en la memoria.

## Etapa 1 (sesión `5eb1d039-99cd-4202-8faf-d6f52e290c73`)

1. **Las imágenes de las primeras 19 fichas.** Según su FRENO, la lectora las perdió de vista y las volvió a mirar antes de escribir la
   planilla.
   - El control de la mesa sobre la transcripción cuenta solo lecturas de archivos de imagen, sin abrir resultados. Muestra que las
     imágenes de 11 de esas 19 fichas se leyeron otra vez antes de la primera escritura de la planilla (20:58:05 UTC).
   - Para las otras 8, la relectura queda NO VERIFICADA por la transcripción.
2. **Tres archivos de trabajo fuera de su carpeta:** `marcas.txt`, `marcas2.txt` y `merge.py`, en el scratchpad de su sesión. El
   despacho decía «no escribas fuera de esta carpeta». Se copiaron sin abrir al paquete de la mesa:
   `revision_lectura_S1ter/NO_ABRIR_scratchpad_sesion_lectora_etapa_1/`.

## Etapa 2 (sesión `69485c5b-25a9-4fd7-913b-9f3934a8f99b`)

1. **El paso 1, resumido.** La lectora resumió en su FRENO la salida del paso 1 en lugar de pegarla.
   - La salida real está en su transcripción: los dos comandos dieron 181 OK y ningún FAILED (el manifest de la carpeta y el de la
     planilla).
   - No nombró ninguna ruta fuera de su carpeta.
