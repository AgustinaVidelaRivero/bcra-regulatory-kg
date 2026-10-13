# U-SEG-OFICIAL, S1-quater: los scripts de la adjudicación, sellados antes de la pasada 1 (registro de la mesa, 13/10/2026)

USD 0, sin API. Decisiones de la autora del 13/10/2026, tomadas antes de abrir su pasada 1 y sin ver nada de la lectura. La mesa las
registró en su hoja de ruta a las 15:01:47 (§91), 15:48:44 (§92) y 16:09:56 (§93). Este registro no lleva ninguna cifra ni marca de
la lectura de S1-quater.

## Las reglas

- **La nota de reglas de la autora** (`reglas_adjudicacion_S1quater.md`, `5e96a764…`, fuera del repo):
  - la autora marca sola, y ningún modelo ve las fichas ni propone marcas;
  - rige el criterio final de S1-ter, el mismo en las dos etapas;
  - la cifra que decide cuenta las dudosas como error;
  - la regresión se adjudica con las mismas reglas y no entra en la cifra.
- **La pasada 1** lleva las dos etapas enteras (la etapa 2 es la regresión), cada una en el orden
  `random.Random(f"U-SEG-OFICIAL:adjudicacion:S1-quater:{etapa}").sample(sorted(ids), len(ids))`. Se arma desde el tar sellado de las
  fichas, sin nada de la lectora.
- **Qué rige de S1-ter.** Rige todo lo del criterio final de S1-ter que dice cómo se juzga una unidad o cómo se cuenta la cifra. No
  rige lo que dependía de poblaciones o de incidentes de S1-ter que S1-quater no tiene.
  - **Rige:**
    - las marcas, las clases y las subclases;
    - la regla a–d de la pasada 2;
    - el piso sin ponderar sobre las 90, con las dudosas de los dos modos (decide el de las dudosas como error);
    - la cifra del corpus, con los pesos de las poblaciones de S1-quater;
    - la limpieza, informada aparte;
    - «el límite declarado cuenta como error si lo es»;
    - un error confirmado en la unidad que sigue o en lo heredado se registra y no cuenta;
    - un error de corte en un TO de la tanda 0 se informa aparte.
  - **No rige:**
    - el recorte de las 19 primeras fichas en el acuerdo (era por un incidente de la lectura de S1-ter);
    - las listas de (b) de la 1.16, con el cierre que contaba como error de la lista y su reversión por lista;
    - los dos «mixtos» de esas listas;
    - las reglas especiales de las dos entradas de ri_oc de la 1.16: en S1-quater, una herencia confirmada se registra y no cuenta, como
      en cualquier otra ficha.
- **Los límites declarados:** S1-quater no tiene una lista propia. Se usa la de S1-ter (`s1ter/poblaciones_S1ter.json`,
  `cortes.limites_declarados`), comparada por id con las unidades de la muestra, y se declaran los que no se encuentran. La cifra no
  cambia por eso.

## Desvío del diseño, declarado

El diseño sellado de S1-quater (`../diseno/diseno_S1quater.md`, §8) dice que la cifra la calcula `s1ter/scripts/cifras_lectura_S1ter.py`.
Ese script no corre sobre S1-quater: exige las 30 y las 36 fichas de la 1.16 en la etapa 2 (`:131`), y la etapa 2 de S1-quater es
solo la regresión. La cifra la calcula `cifras_lectura_S1quater.py`, una copia adaptada que conserva todo lo que juzga una unidad o
cuenta la cifra. Por decisión de la autora del 13/10/2026, se declara como desvío del diseño, antes de su pasada 1.

## Los archivos

- `preparar_pasada_1_S1quater.py`: arma la pasada 1. Sale de `s1ter/adjudicacion/preparar_pasada_1_S1ter_v2.py`. Su prueba, con datos
  de S1-ter, es `prueba_preparar_pasada_1_S1quater.py`, con salida en `salida_prueba_preparar_pasada_1_S1quater.txt`: 29 de 29.
- `pasada_2_S1quater.py`: la selección de la pasada 2 y el TSV final, con el acuerdo de cada etapa. Sale de `pasada_2_S1ter_v2.py`.
  - El control de forma va adentro, no como un agregado.
  - Las planillas de la autora se leen por renglones y tabulaciones, y frenan si traen retornos de carro, otra cantidad de columnas o
    comillas dobles en sus columnas.
  - La pasada 2 se escribe sin comillas.
- `acuerdo_etapa_1_S1quater.py`: el acuerdo de la etapa 1, sobre las 90.
- `aplicar_adjudicacion_S1quater.py`: aplica la adjudicación a las planillas selladas de la lectora.
- `cifras_lectura_S1quater.py`: las cifras.
- `prueba_cierre_S1quater.py`: prueba los cuatro anteriores con datos sintéticos, con salida en `salida_prueba_cierre_S1quater.txt`:
  43 de 43.
- `sello_scripts_adjudicacion_S1quater_mesa.txt`: el sha256 de cada archivo de esta carpeta y la hora del sello.

## El paso a paso

1. La autora arma su pasada 1 con el comando que le prepara la mesa, que controla el sha256 de `preparar_pasada_1_S1quater.py`.
2. Marca, y sella su pasada 1 como en S1-ter: el `shasum -a 256` de cada TSV, con la fecha. Le pasa a la mesa el contenido de los
   archivos de sello.
3. La mesa corre `pasada_2_S1quater.py seleccionar` y le arma la pasada 2. Ahí aparece por primera vez la marca de la lectora, solo en
   las fichas seleccionadas.
4. La autora decide la marca final de cada ficha seleccionada y sella la pasada 2.
5. La mesa corre `armar`, `aplicar_adjudicacion_S1quater.py`, `cifras_lectura_S1quater.py` y `acuerdo_etapa_1_S1quater.py`, sobre
   copias, y los sella. Recién ahí se ven cifras.
6. Qué documentos entran en la tanda 1, llegue o no al piso, y qué pasa si no llega: la nota del 13/10/2026 al pie de
   `docs/mandatos/USEG_OFICIAL_segmentacion_e0r2.md`.
