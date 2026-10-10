# U-MED-UMBRALES, etapa P: FRENO del lote 1 (mesa, 10/10/2026)

El FRENO del §9.3 de la enmienda 1 (`a0f9815`): ajustar la regla y la ficha, con la lista de clases de error que aparecieron, antes del
lote 2. USD 0, sin API. No trae datos del acta del sorteo ni del diagnóstico por elemento, que siguen vedados para la autora hasta
cerrar el paso 1 del lote 2. Las cifras son de validación de diseño (§9.1): no son cifras del capítulo 5, y si aparecen en la tesis van
en fracción cruda.

## 1. Lo que se leyó, con sus sellos

| paso | archivo (fuera del repo) | sha256 | sellado |
|---|---|---|---|
| paso 1 | `lectura_lote1/formulario_paso1_lote1_v2.md` | `58a56fb5386a334a28d9b911e90b4fb44c003f75b581311d0a4017244ba21f92` | 09/10/2026 17:57:54 |
| lecturas provisionales de la v0 | `lectura_lote1_paso2/lecturas_provisionales_v0_paso2_lote1.md` | `e389b9119f2b2972aa2c337d4c5867416e8ee69d50d590816c98ecdfba98c6dd` | 10/10/2026 12:00:02 |
| paso 2, clases | `lectura_lote1_paso2/diferencias_paso2_lote1_autora.md` | `dc5ea3edd9ebd5402f000148e34344ba3036e79d77693e79fb45251a48064e20` | 10/10/2026 14:00:10 |
| paso 2, notas | `lectura_lote1_paso2/notas_paso2_lote1.md` | `d3f2b4c8cd00af7dc0d7f8ff6a45c37d9e5e0dd390a30304a77bae2a3124fcec` | 10/10/2026 14:00:10 |

- Los cuatro dan su sha256 en la carpeta. El formulario del paso 2 que preparó la mesa (`c19f5e60…`) quedó intacto: la autora trabajó
  sobre una copia.
- **El paso 2 aplicó la regla v0 (`22eb6a78…`) con las lecturas provisionales de la autora,** fijadas antes de abrir las diferencias
  (L1 a L8 y los puntos menores). Esas lecturas son la propuesta de la autora para la v1 (§5).
- Los archivos de la autora quedan fuera del repo, de solo lectura, como el formulario del paso 1. El repo los cita por su sha256.

## 2. Cifras del lote 1

Script: `cifras_lote1_paso2_mesa.py`, sobre el archivo sellado de clases; salida `cifras_lote1_paso2.json`.

- **Fichas:** 20 = 17 que cuentan + L1-01 (excluida, ficha contaminada) + 2 vacías (L1-09 y L1-13).
- **Vacías (§2.5), aparte:** las dos, «no es un umbral».
- **Filas del paso 2:** 48. Las de L1-01 son 9, así que cuentan 39 = 17 diferencias + 11 marcas + 11 sin llenar.
  - **Diferencias (17):** 13 omitidas, 2 parciales, 1 contradicha y 1 espuria.
    - Por campo: unidad, 4 omitidas; base, 4 omitidas, 2 parciales y 1 espuria; comparación, 1 contradicha y 2 omitidas; valor, 1
      omitida; destino, 2 omitidas.
    - Las dos parciales cuentan como incorrectas, por la regla del §2.2 aplicada con la nota de L7: con la base guardada se calcula otro
      monto.
  - **Comparaciones omitidas, clase del §2.4:** 1 de implementación (L1-20.2) y 1 de la definición (L1-10.2).
  - **Marcas (11) y sin llenar (11):** no decidibles. Sobre cómo se cuentan 6 de las sin llenar, ver el §6, punto 1.
  - **Correcciones del paso 1:** ninguna de campo. Hay una corrección de redacción del motivo, en L1-01.9 (fuera de la cifra), que no es
    corrección de campo del §5.3.
- **Veredictos del elemento (§2.5),** sobre los 17:

  | veredicto | correctos | incorrectos | no decidibles | cotas | sobre los decididos |
  |---|---:|---:|---:|---|---|
  | núcleo | 4 | 6 | 7 | 4 a 7 de 17 | 4 de 10 |
  | núcleo contra la definición | 4 | 6 | 7 | 4 a 8 de 17 | 4 de 10 |
  | completo | 4 | 6 | 7 | 4 a 7 de 17 | 4 de 10 |

  - **Los 7 no decidibles** lo son por la pertinencia (decisión de la autora: no decidibles en el lote 1, a resolver en la v1).
    - 3 no tienen otra fila incorrecta (L1-06, L1-12 y L1-17).
    - 4 sí la tienen (L1-10, L1-16, L1-18 y L1-20). L1-10 sería correcto contra la definición, porque su única diferencia es una
      comparación omitida de la definición.
  - **Incorrectos:** L1-05, L1-07, L1-11, L1-14, L1-15 y L1-19.
  - **Correctos:** L1-02, L1-03, L1-04 y L1-08.
- **El destino no mueve ninguna cifra en este lote.** Los dos omitidos (L1-19.2 y L1-20.3) son informativos por el §2.2, y el único destino
  guardado con error (L1-15.2) quedó no decidible por estar sin llenar en el paso 1 (hallazgo de la autora).

## 3. Clases de error que aparecieron (para el §10)

Cada una con sus casos del lote 1 y su naturaleza. «Implementación» quiere decir que el código no aplicó una regla que existe;
«definición», que la regla o el esquema no la expresa.

1. **El sentido sale del tramo recortado y no de la cláusula** (H-L1-6 y H-P2-1). Implementación, con un caso de control ya formado: L1-07
   (contradicha) y L1-18, puntos hermanos con la misma redacción; el tramo de uno excluye la negación y el del otro la incluye.
   Corrección: derivar el sentido de la cláusula de E0, como el §2.2 se lo exige al lector.
2. **Contracción «del» no reconocida en la tabla del §2.4** (L1-20.2: «no menos del»). Implementación: «no menos de» está en la tabla.
3. **Formas de la letra que la tabla no tiene** (L1-10.2, «un máximo mensual equivalente al»; H-L1-7, «antelación mínima»). Definición: van
   a la tabla de la v1.
4. **Base vacía con base en la letra** (L1-05.3, L1-16.2, L1-18.4 y L1-19.1).
5. **Base cortada antes de sus calificadores** (L1-11.1 y L1-15.1), las dos con otro monto.
6. **Base espuria: lo contado guardado como base de un conteo** (L1-14.3).
7. **Cuantía en letras no tomada como valor** (L1-14.1, «dos», en un elemento del validador).
8. **Unidad vacía en una magnitud monetaria** (L1-05.1, L1-07.1 y L1-18.2, «monto» o «fondos»), y una unidad fuera de la lista no guardada
   con la marca `fuera_de_lista`, que el esquema admite para cualquier campo de lista cerrada (L1-14.2; `pyd_r2/code/modelos_r2.py:36-37`,
   `:288`, `:302-307`).
9. **Remisión externa resuelta contra el TO propio** (L1-15.2: `cap::6.5.1` por `cla::6.5.1`). Va como clase aunque la fila quedó no
   decidible.
10. **La cuantía de un cierre heredado atribuida a la unidad hija** (H-L1-13, L1-17). Su predicción se confirmó: los campos coinciden con la
    lectura y lo único mal es el nodo.
    - El mecanismo, medido por la revisión de la mesa: la regla del cierre se extrajo dos veces, una en el padre y otra en la hija, con
      `punto_propio` aunque su tramo está en el heredado.
    - **Nombre de la clase:** «cuantía de un cierre heredado atribuida a la unidad hija», decidido por la autora (§7, ítem 2).

Qué va a código en el grupo 2 se decide con el lote 2, cuando las clases se confirmen. Cada clase que entre lleva un test con sus
casos positivos y negativos (§10 de la enmienda 1).

## 4. Hallazgos sobre el instrumento

- **H-L1-1 y H-L1-2:** la cabecera y la ficha v1 filtraban campos del grafo. Ya corregido fuera del repo en el instrumento v2 (D-L1-4),
  pero el generador del repo sigue igual: la ficha muestra etiqueta, descripción y tramos, y la cabecera es el id con la cuantía.
- **H-L1-9:** el resaltado se ubica por coincidencia de cadena y no por el tramo del elemento.
  - En L1-12 cae en la aparición con el sentido inverso.
  - En L1-16 resalta nueve apariciones, entre ellas los dígitos del número de punto.
- **H-L1-10:** dos fichas del mismo lote caen en la misma unidad de E0, y la segunda lectura queda informada por la primera.
- **H-L1-4:** la regla v0 trae ejemplos resueltos que coinciden con el texto de fichas del lote.
- **Los ids opacos del instrumento v2** no se reproducen con el generador del paquete de P-b (`generar_formulario_opaco_Pb.py`): da
  `"e" + sha256[:6]` donde el mapa sellado dice otra cosa. El mapa se validó contra otras tres fuentes y es correcto, pero el
  procedimiento que lo produjo no queda reproducible.
- **El formulario del paso 2 no tiene columna de nota** (hallazgo de la autora). Las notas de L4, L7 y L8 tuvieron que ir a un archivo
  aparte.
- **H-L1-3:** con el texto de E0 en el canal (D-L1-5), 0 no decidibles por ilegibilidad: la señal sobre la decisión D3 queda despejada en
  este lote.

## 5. La v1 de la regla

Borrador en el paquete de la mesa (`hoja_de_ruta_tanda1_mesa/umed_lote1_freno/regla_calificacion_v1_BORRADOR.md`). La v1 es la v0 con cambios numerados, cada uno con su fuente:
- las ocho lecturas provisionales de la autora, como propuesta suya;
- las resoluciones de los hallazgos;
- la contradicción del §5.2 con el §2.2, con una propuesta de la mesa.

Se sella antes del lote 2, que se lee con la regla fija (§9.3). La regla del §5.4 se sella al cerrar el piloto, después del lote 2.

## 6. Lo que decide la autora

1. **Contradicción entre la decisión del 10/10/2026 sobre los campos sin llenar y las notas selladas del paso 2.**
   - La decisión dice que los 19 campos sin llenar quedan «sin respuesta», y se reafirmó al pedir este FRENO.
   - Las notas selladas (§«Enmienda a la decisión 2») distinguen: 6 son de pertinencia; 7 son de L1-01, sin responder de verdad; y 6
     (las monedas de L1-05, L1-07 y L1-18, y los destinos de L1-05, L1-11 y L1-15) se declararon no decidibles con motivo en el paso 1, y
     ese motivo es la lista cerrada (H-L1-5).
   - Ningún veredicto del §2 cambia con una u otra lectura: los 6 están en elementos ya incorrectos o en campos que no mueven la cifra.
     Cambia cómo se cuenta el hueco de las listas cerradas.
   - **¿Cuál rige?**
2. **El nombre de la clase de H-L1-13.**
   - Propuestas: «cuantía de un cierre heredado atribuida a la unidad hija» (la de H-L1-13) o «regla heredada extraída como nodo de la
     unidad hija» (la de la revisión de la mesa, por el mecanismo).
   - Recomiendo la primera para el §10 (describe lo que ve la lectora) y la segunda como mecanismo en la ficha de la clase.
3. **El generador del instrumento para el lote 2.**
   - Opciones: corregir el generador del repo (después del FRENO de S1-ter-b, como commit) o regenerar fuera del repo, como el v2.
   - Corregirlo implica: la ficha sin campos del grafo; el resaltado por el tramo del elemento; los ids opacos de una semilla, con el mapa
     sellado aparte y reproducible; la columna de nota en los dos formularios; y el control de que dos fichas del lote no compartan
     unidad.
   - Recomiendo corregirlo en el repo, porque es el mismo generador que alimentaría los 240 de T.
4. **Los cambios de la v1** (borrador), en particular la propuesta para la pertinencia: juzgarla en el paso 2, con la etiqueta y el tramo
   del nodo a la vista, después de sellar el paso 1.
5. **L1-01: la declaración NO VERIFICADA** de cinco campos respondidos el 09/10 (notas, §«Declaración sobre L1-01»). Queda así hasta que
   llegue el artefacto fechado. No cambia ninguna cifra: L1-01 está fuera.
6. **Qué entra al repo y cuándo:** el comando 29, para correr después del FRENO de S1-ter-b. Lleva este FRENO, el script de las cifras y
   su salida, y una nota al pie de la enmienda 1 con los sellos del paso 2 y de las lecturas provisionales.

## 7. Decisiones de la autora del 10/10/2026, sobre este FRENO

1. **Los campos sin llenar:** rige el formulario del paso 1 sellado (`58a56fb5…`). Verificado campo por campo: los 6 que separan las notas
   del paso 2 están en blanco, y el campo `no_decidible` de su ficha los nombra con su motivo. Quedan no decidibles:
   - **L1-05, moneda y destino:** la cláusula no nombra moneda, y la remisión es genérica, sin punto ni término;
   - **L1-07, moneda:** la cláusula no la nombra, y la única mención, en el heredado, es genérica y sin código;
   - **L1-18, moneda:** igual que L1-07;
   - **L1-11, destino:** remite a una fuente de información, no a un punto ni a un término definido;
   - **L1-15, destino:** remite a dos puntos de otro TO y a un término definido en otra norma, y el formato admite un solo destino.

   Con el mismo criterio, la pertinencia sin llenar de L1-01, L1-06, L1-10, L1-12, L1-16 y L1-18 también figura como no decidible con
   motivo; la decisión anterior ya las deja no decidibles, a resolver en la v1. Los 7 campos restantes de L1-01 están en blanco y sin
   motivo propio. **Confirmado por la autora:** «sin respuesta» son los 7 campos de L1-01; los otros 12 quedan no decidibles, con su
   motivo del paso 1.
2. **La clase de H-L1-13** se llama «cuantía de un cierre heredado atribuida a la unidad hija», con el mecanismo en su ficha.
3. **El generador del instrumento para el lote 2** se corrige en el repo, como commit después del FRENO de S1-ter-b.
4. **La v1:** se acepta en principio juzgar la pertinencia en el paso 2, con la etiqueta y el tramo a la vista. Los 28 cambios se aprueban
   después de leer el borrador entero, y la v1 se sella antes del lote 2.
5. **Declaración para el registro del lote 2:** la autora vio las cifras de validación y las clases de error del lote 1 (este FRENO)
   antes del paso 1 del lote 2. Desde el 10/10/2026 y hasta cerrar ese paso, los FRENOs de U-MED-UMBRALES le traen solo lo que tiene que
   decidir, sin cifras ni clases.
6. **L1-01:** no hay ni va a haber artefacto fechado que verifique la declaración de la autora sobre sus cinco campos (punto 5 del §6).
   Queda excluida porque su referencia no es humana, como declaró la autora, y la declaración queda NO VERIFICADA de forma definitiva.
7. **Ejemplos resueltos de la v0 en la muestra:** los elementos de cada lote cuyo texto contiene un ejemplo resuelto de la v0 quedan
   marcados «coincide con un ejemplo resuelto de la v0» en el registro de su lote, sin decirle a la autora cuáles ni cuántos (la autora
   tuvo la v0 a la vista desde el lote 1). Lote 1: `NO_ABRIR_marcas_ejemplos_v0_lote1_mesa.json`, en esta carpeta. Lote 2: en el paquete de
   la mesa, hasta su registro (sha256 `791b79d4d995a46785c098fc6aa5fe53e911faa1eeaafe486e368030f6f1b1a3`). Cada archivo es un JSON de un
   solo renglón, para que el número de renglones del commit no diga cuántas marcas hay.

8. **La v1 sellada:** el texto consolidado se sella tal cual el 10/10/2026 a las 14:32:01 (-0300), sha256
   `70b8dcce5ad0f75eb0befffb3724d278679abd7780b03b352bb46a64fb7dc893`, 152 renglones (`sello_regla_calificacion_v1.txt` del paquete de la
   mesa). Rige para el paso 1 del lote 2. Entra al repo después del FRENO de S1-ter-b, en el mismo commit que una nota fechada al pie de
   la enmienda 1 por los cambios al §5, que la autora autorizó.
