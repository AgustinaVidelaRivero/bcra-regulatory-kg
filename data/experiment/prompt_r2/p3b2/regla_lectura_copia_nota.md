# Regla de lectura de los casos de copia de la nota de E3 (P3b-2)

04/10/2026. La fijé antes de abrir los casos. Su sha256 y la hora quedaron en el registro de la corrida (paquete de
revisión, `registro_regla_copia_nota.txt`), antes de que se generara la lista para leer.

**Población.** Los 45 casos de `p3b/salida/lazo_e3_p3b.json` (clave `k.copia_nota.casos` de cada corrida, con
duplicados entre corridas quitados): una entidad del reintento, un campo (descripción o etiqueta) y las ventanas de 5
tokens de R-NORM que están en la nota del faltante y no en el texto de la unidad ni en las citas.

**Qué leo en cada caso,** lado a lado: el texto de la unidad (propio y heredado), la nota o notas de E3, el texto de la
entidad y las ventanas en común. Como ayuda, el script lista las palabras de contenido de las ventanas que no están en
el texto de la unidad y las de metalenguaje del verificador.

**Clases, por orden: rige la primera que se cumple.**
1. **Copia real.** Las ventanas en común llevan metalenguaje del verificador: «falta», «faltante», «no
   representado», «omite» u «omitido», «la extracción», «el extractor», «el chunk», «la unidad», «nodo»,
   «entidad», «debería».
2. **Coincidencia legítima.** Cada palabra de contenido de las ventanas está en el texto de la unidad, y la frase
   es una reformulación de la norma que cualquier descripción fiel escribiría así: el mismo orden de ideas, con
   cambios de flexión, de orden o de nexos.
3. **Copia real.** Las ventanas introducen una palabra de contenido que no está en el texto de la unidad: un término
   que trajo la nota, o una paráfrasis propia de la nota que la entidad reproduce.
4. **Dudosa.** No se puede decidir con los textos solos. Por ejemplo, la frase es genérica (una fórmula de remisión
   o de alcance) y está a la vez en la nota y, con otras palabras, en la norma.

**Palabras de contenido:** los tokens de R-NORM que no están en una lista cerrada de palabras vacías del español
(artículos, preposiciones, conjunciones, pronombres y las formas de «ser», «estar» y «haber»). La lista está en el
script de la lectura.

**Qué reporto:** cuántos casos hay en cada clase, cuántas unidades tienen al menos una copia real, y una línea con la
razón de cada caso.
