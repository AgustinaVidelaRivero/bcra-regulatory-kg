# Tu lectura de los casos de la última clase de la atribución de B6.3

Qué abrís: las fichas, de F01.md en adelante, en su orden. Cada una trae la pregunta, sus criterios con la marca final del juez,
la respuesta, el ancla y los pasos de la traza que la vieron o la consultaron. Todas son de la clase generacion: el agente
consultó el ancla y la respuesta igual salió parcial o incorrecta.

Qué marcás: en planilla_atribucion_b63.csv, una fila por ficha.
- la_clase_se_sostiene: sí, no o no decidible.
- comentario: libre.
No cambies las columnas, el orden de las filas ni el nombre del archivo.

Cómo sellás, desde la Terminal y en esta carpeta, cuando termines todas:
1. shasum -a 256 estructura_planilla_atribucion_b63.json
   tiene que dar 76def9bc9ae402bae15dbaa73d94f7f58cb9db130bb77cd5319563b4b838d06e. Si no da, no selles y avisá a la mesa.
2. RUNNER="$HOME/INGENIERIA IA/TESIS/fuera_del_repo/atribucion_nav/copia/data/experiment/ev2_reporte/code/atribucion_b63.py"
   shasum -a 256 "$RUNNER"
   tiene que dar dcf13ae1bdec5bef5e06cb2fa01cba2bf088d5acdf311099da9f7a55d3476fef.
3. "$HOME/miniforge3/bin/python3" -I -B "$RUNNER" sellar --planilla planilla_atribucion_b63.csv \
     --estructura estructura_planilla_atribucion_b63.json --sello sello_atribucion_b63.txt
El sello registra el sha256, los bytes y la hora de la planilla. Se sella una sola vez. Si el sellador frena por un valor o
una fila, corregí la planilla y volvé a correrlo.
