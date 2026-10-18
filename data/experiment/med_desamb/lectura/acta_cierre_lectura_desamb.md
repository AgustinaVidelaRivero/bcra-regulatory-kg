# El cierre de la lectura de U-MED-DESAMB (mesa, §158)

- **La lectura:** la de la autora, sobre la planilla del sorteo sellado (diseño sellado, §5 y §7, y su nota 1). La cerró y la selló el
  18/10/2026 a las 14:04:01 (−03), en una carpeta fuera del repo. Leyó de 11:48 a 13:50: NO VERIFICADO, es el dato de su mensaje del
  18/10/2026, recibido a las 14:05:06.
- **Qué hay acá:**
  - **`sellada/`:** los nueve archivos de esa carpeta, byte a byte. Los nombres de `sello_desamb.txt` se resuelven en esta carpeta:
    - `hoja_clases_marcada.csv` y `censo_c1_marcado.csv` son la lectura, y mandan;
    - `hoja_clases.csv` y `censo_c1.csv` son las exportaciones de la autora, que pasó por `convertir_desamb.py`. Llevan el nombre de las
      plantillas porque las pisaron en esa carpeta;
    - `planilla_lectura.md`, `anexo_entradas.md` y `censo_c1.md` son el material que leyó, igual al del paquete de la mesa;
  - **`plantillas/`:** las plantillas en blanco que entregó la mesa (`hoja_clases.csv`, `ba317008…`, y `censo_c1.csv`, `08eda995…`) y la
    planilla en JSON (`planilla_lectura.json`), que lee el juez;
  - **`control/`:** el control de la mesa con su consola, el sello en la forma que pide el juez y su prueba.
- **El control de la mesa: 14 de 14 OK** (`control/consola_control_lectura_desamb.txt`):
  - el sello: los cuatro sha256 y la hora. Las dos marcadas, de solo lectura, con los sha256 del mensaje de la autora. La conversión;
  - las plantillas del paquete son las selladas, en la copia de trabajo y en la permanente. El material es igual;
  - los 12 ítems que se saltean (nota 1, §2) son los de la §141 y los de la conversión;
  - la hoja: la cabecera y 91 filas, con las columnas fijas iguales a las de la plantilla. Hay 13 entradas vacías, las de los 12 que se
    saltean, y 78 clasificadas, todas con una clase válida;
  - el censo: 2 colisiones, cada una con una decisión válida;
  - la conversión, corrida de nuevo sobre una copia, da las dos marcadas byte a byte, sin arreglos de forma;
  - el control no informa ninguna cuenta por clase.
- **El sello en la forma que pide el juez:**
  - el juez pide un JSON con «sellado» (`juez/juez_desamb_mesa.py:348-354` y `:578`), y el sello de la autora es texto;
  - `control/sello_cierre_para_el_juez.json` lo deriva por script, sin cambiar el sello;
  - lo probé con los controles del juez, importados desde un clon (`control/consola_probar_sello_con_el_juez.txt`, 3 de 3).
- **Lo que no está acá:**
  - las claves aparte de la lectura (la lista de la muestra y su clave) y las de los calibradores v2. Siguen sin abrir, en el paquete de
    la mesa;
  - la planilla de los calibradores v2 (nota 1, §2). La autora la lee solo si le da el tiempo antes del miércoles 21/10/2026 a las 18:00,
    y lo decide con los recortes del lunes 19.
- USD 0.
