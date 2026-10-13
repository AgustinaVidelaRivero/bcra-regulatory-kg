# U-SEG-OFICIAL, S0-6a-bis: las decisiones de la autora sobre el FRENO (registradas por la mesa, 12/10/2026)

USD 0, sin API.
- **Qué es:** el registro de las decisiones de la autora del 12/10/2026 sobre el FRENO de S0-6a-bis, tomadas sobre la revisión de la
  mesa (hoja de ruta de la mesa, §81 y §82). Entra con la línea nueva del backlog (decisión 6).
- **Lo que no cambia:** ningún archivo de la ejecutora ni de la mesa ya commiteado (`cf9b7e27`).
- **Ids de unidades:** no lleva ninguno.

## 1. Lo que se acepta

- **Las cuatro unidades leídas en S1-ter que cambiaban por otra cosa que lo de la primera corrida** (decisión 1): se aceptan los
  veredictos de la mesa. Dos mejoran, una queda corregida y una queda neutra.
- **Las decisiones de diseño de la ejecutora** (decisión 2): se aceptan, y se declaran tres cosas.
  - **El grupo y la tabla de C:** la regla de C que no mueve un grupo que arrastra un párrafo que no comparte columna, ni un grupo seguido
    de una tabla, extiende la decisión 2 de la autora del §79, que pedía solo el párrafo. La extensión sale de casos leídos en S1-ter.
  - **El tope de la carátula de A:** el 8 viene del tope de J (`MAX_RENGLONES_CARATULA_J`, de S0-6a) y no tiene derivación escrita. Los
    dos casos, ceninf (el de J) y ri_ii_31_12_19 (el de A), tienen 4 renglones en su página 1.
  - **El efecto marginal de L y M:** la medida se agregó después del censo. La mesa lo reprodujo: es el que declara la ejecutora.

## 2. Lo que se corrige después

- **Las anclas de F19b** (decisión 4): las corrige S0-6b, junto con la fila F19d, y corre el control de las 27 citas de la tabla de
  reprocesamiento al código de E0. Hoy una no se encuentra entera en el código parcheado (`correr_e0.py:140-210`).
- **El control de las leídas** (decisión 9): en S0-6b lleva el texto de las unidades a un archivo `NO_ABRIR_`, fuera del repo, y deja en
  el archivo abierto solo ids y cuentas. Los archivos abiertos del registro de S0-6a y de S0-6a-bis muestran texto de unidades que no
  son de diseño; esas unidades salen de S1-quater por la adenda 4 a su diseño.

## 3. Lo que queda como límite declarado

- **Las divisiones que A abre en las tablas de códigos de ri_ii_31_12_19** (decisión 5): límite declarado. S1-quater mide la E0 con
  ellas.
- **Las cadenas de 10 o más títulos heredados** (decisión 6): 247 unidades de 7 documentos.
  - **Para la tanda 1:** límite declarado (opción 1). Ninguno de los 7 documentos está en el ejemplo de la tanda 1.
  - **Después:** la corrección por rasgo (opción 2) entra al grupo 2 como corrección obligatoria antes de extraer cualquiera de los 7
    documentos. Se diseña solo con cuentas y tiene su propia medición sobre unidades que no se usen para diseñarla. Está en el backlog
    como BKL-0044.
  - **S1-quater mide la E0 con las cadenas.**

## 4. La bolsa de la evaluación final (decisión 7)

- **Salen 40 documentos por el código de E0:** toda constante por documento cuenta como corrección hecha para ese documento, sea de
  S0, S0-4, S0-5, S0-6a o S0-6a-bis. La lista, con la causa de cada uno, está en la revisión de la mesa del FRENO de S0-6a-bis (§12).
- **Los cortes a mano y los laudos de casos** se suman al sortear, como dice `docs/plan_tesis.md:782`.

## 5. Lo que va en la adenda 4 al diseño de S1-quater

Decisiones 3, 8, 9 y 10. Las trae `s1quater/diseno/adenda_4_diseno_S1quater.md`:
- la regla única (sale toda unidad que no sea fila ni leída en S1-ter cuyo texto haya visto la mesa o una ejecutora antes del sorteo,
  medida por script);
- la cobertura (opciones 1 y 2);
- las unidades que muestran los archivos del registro;
- la memoria de la mesa, que se limpió con respaldo y se declara ahí.
