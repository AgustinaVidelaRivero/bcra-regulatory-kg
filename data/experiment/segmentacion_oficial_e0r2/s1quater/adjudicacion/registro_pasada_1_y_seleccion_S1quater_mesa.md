# U-SEG-OFICIAL, S1-quater: la pasada 1 sellada, la sesión que la acompañó y la selección de la pasada 2 (registro de la mesa, 14/10/2026)

USD 0, sin API. Este registro no lleva ninguna cifra ni marca de la lectura ni de la adjudicación. Hoja de ruta de la mesa, §98 y §99.

## 1. La pasada 1, sellada

| Etapa | Planilla | sha256 | Sello |
|---|---|---|---|
| 1 | `adjudicacion_pasada_1_etapa_1.tsv` | `492fa1f43475e9b4564d0aa0d9f54ab49ec411ee56aecdd8cf12eda84fbbfc3c` | 13/10/2026 18:58:19 |
| 2 | `adjudicacion_pasada_1_etapa_2.tsv` | `2cd6933328f49bf9c63fa4251d7664ec4eb5c84c77d6d7ffb3092bf47c1aa1bc` | 14/10/2026 14:03:54 |

- Las dos planillas son de solo lectura.
- La mesa controló su sha256 sin abrirlas, el 14/10/2026, y leyó los dos archivos de sello. Traen esos sha256 y esas horas.
- La fecha de modificación de las planillas es 13/10 18:47:29 y 14/10 14:02:36.

## 2. La declaración de la autora y lo que midió la mesa

**La declaración, tal cual** (14/10/2026; reemplaza la que había dado ese mismo día):

> - lo que mediste: la sesión c0a11ec7 escribió en mis dos planillas, las leyó, vio el texto de 26 fichas de la etapa 1 y de 32 de la
>   etapa 2 (algunas porque se las pegué yo en el chat) y escribió notas en mi carpeta pasada_1/;
> - lo que declaro: yo le dictaba las marcas y las notas, y ella las escribía tal cual. No aplicó el criterio ni me sugirió marcas;
> - por decisión mía, eso último no se verifica con una medición: queda como mi declaración.

**La declaración anterior,** del mismo día: «En la etapa 2 usé una sesión de Claude Code (c0a11ec7-4b94-4967-9f79-2fd1325a0ccb) para
ubicar los documentos de algunas fichas y generar sus páginas vecinas. No aplicó el criterio a ninguna ficha ni me sugirió marcas. En
la etapa 1 no la usé. Las marcas son mías.» La medición de la mesa no la confirmó, y se cumplieron las dos condiciones de freno que había
fijado la autora: que la sesión hubiera abierto algo de la etapa 1 o tocado una planilla.

**Lo que midió la mesa,** por script, sobre la transcripción de la sesión, solo en cuentas, horas y nombres de archivo. Los scripts y sus
salidas están en el paquete de la mesa, `hoja_de_ruta_tanda1_mesa/decisiones_98_mesa/medicion_c0a11ec7/`.
- **La sesión:**
  - empezó el 09/10/2026 y también se usó para S1-ter, que tiene los mismos nombres de archivo y el mismo formato de id. Se separó por
    ruta completa y por hora;
  - escribió en su scratchpad un script, `marcar_q.py`, cuya ruta base es la carpeta de la pasada 1 de la autora y que escribe una fila
    de una planilla.
- **Etapa 1 (90 fichas):**
  - **la planilla:** la sesión escribió con ese script filas de las 90 fichas, entre las 17:23:38 y las 18:51:27 del 13/10. La planilla
    tiene fecha 18:47:29, y el sello es de las 18:58:19. Un intento del 14/10 a las 09:23:36 falló, porque la planilla ya era de solo
    lectura;
  - **las fichas:** el texto de 26 fichas entró a la sesión: 12 por comandos que leen el archivo de fichas y 19 que pegó la autora en
    el chat;
  - **las imágenes:** las abrió en pantalla para 71 fichas; el modelo no vio ninguna.
- **Etapa 2 (60 fichas):**
  - **la planilla:** la escribió con el mismo script, entre las 23:54:15 del 13/10 y las 14:02:35 del 14/10; 53 fichas aparecen como
    la ficha de una fila escrita (una cota). A las 10:16:35 reescribió la planilla entera para quitarle los acentos;
  - **las fichas:** el texto de 32 fichas entró a la sesión: 20 por comandos y 17 pegadas;
  - **las imágenes:** las abrió en pantalla para las 60; el modelo no vio ninguna;
  - **las páginas vecinas:** generó páginas para 33 fichas.
- **Los archivos que escribió en la carpeta de la autora,** en `pasada_1/`:
  - `nota_lectura_previa_E1_050.md` (13/10 17:00:53) y `pendientes_etapa_1.md` (13/10 18:51:06);
  - `nota_criterios_pasada_1_S1quater.md` (13/10 23:49:02), `…_adenda.md` (14/10 08:01:43) y `…_adenda_2.md` (14/10 10:29:39).
- **Lo pegado en el chat** se atribuye a S1-quater por la hora. Por contenido, NO VERIFICADO.

## 3. Las decisiones de la autora, selladas antes de la selección

`decisiones_autora_antes_de_la_pasada_2_S1quater.md` (sha256 `a253824560513144efa578517683f9724f836cf365ceb562cf4b81962ba713c3`,
sellado a las 15:12:18 del 14/10/2026, `sello_decisiones_autora_antes_de_la_pasada_2_S1quater.txt`):
- la pasada 1 vale tal como está sellada, en las dos etapas;
- la cifra que decide es la de las 90 fichas; se informa además, como control declarado, la cifra sin las 26 fichas de la etapa 1 cuyo
  texto vio el modelo;
- en la pasada 2 no usa ningún modelo, ni para escribir la planilla.

## 4. Las notas de criterios de la pasada 1

| Nota | sha256 | Sello | Quién la escribió |
|---|---|---|---|
| `nota_criterios_pasada_1_S1quater.md` | `8355e931f142a469fb00867d655088a3c94e3c1933a6c6463db09ec3db8b4049` | 14/10 14:09:26 | la sesión c0a11ec7 (13/10 23:49:02) |
| `nota_criterios_pasada_1_S1quater_adenda.md` | `dcde61ec52da1fcb24f1e10d8774bcbf7242a66143c550161eafb8e668449b3b` | 14/10 14:09:26 | la sesión c0a11ec7 (14/10 08:01:43) |
| `nota_criterios_pasada_1_S1quater_adenda_2.md` | `5f98b7d4d5412958014d9f3bee9c2669d37f01353bcb56d4601d9bfe45b7df72` | 14/10 15:08:17 | la sesión c0a11ec7 (14/10 10:29:39) |

- **La adenda 2,** por decisión de la autora: la escribió la sesión, y se selló después de la pasada 1. Su sello es de las 15:08:17,
  posterior a los dos sellos de las planillas.
- **Lo que hizo la mesa:** leyó solo los archivos de sello, con autorización de la autora. No abrió las notas ni calculó su sha256.
- **Los otros dos archivos que escribió la sesión,** `nota_lectura_previa_E1_050.md` y `pendientes_etapa_1.md`, no tienen sello conocido
  por la mesa.

## 5. La evidencia

La autora guardó en `fuera_del_repo/NO_ABRIR_evidencia_adjudicacion_s1quater/` una copia del scratchpad de la sesión c0a11ec7 y la
carpeta `traspaso_etapa2`. La mesa no la abre, y queda vedada en los despachos que siguen (cláusula de la mesa del 14/10/2026).

## 6. La selección de la pasada 2

A las 15:22:16 del 14/10/2026, después del sello de las decisiones, la mesa corrió `pasada_2_S1quater.py seleccionar` (`ac96ebf3…`,
sellado en el 59) con la regla a–d, sobre copias:

| Entrada | sha256 |
|---|---|
| pasada 1, etapa 1 | `492fa1f4…` (el de su sello) |
| pasada 1, etapa 2 | `2cd69333…` (el de su sello) |
| planilla de la lectora, etapa 1 | `5414ddf1d7365f9e00231e52811b248b6590d622f59c2d27ecee90597e6838dc` (`../lectura/sello_etapa_1_S1quater.txt`) |
| planilla de la lectora, etapa 2 | `bd11e4557a21218f4be2e7db8483adeb28ee2c382349caa0c4f9b974819456b0` (`../lectura/sello_etapa_2_S1quater.txt`) |

| Salida | sha256 |
|---|---|
| `adjudicacion_pasada_2_etapa_1.tsv` | `5a21efadbd0c896a0aee9a19fa0ac3828cf09e400b43c8206a247bb54ec0a2b0` |
| `adjudicacion_pasada_2_etapa_2.tsv` | `5b543060108664004b4cb05917790db675ff19773b6ae514e958fe668115e200` |

- **Las corridas:** dos corridas dieron los mismos bytes. Con un sha256 equivocado, el script frena sin escribir nada.
- **Dónde quedan las salidas:** fuera del repo, en el paquete de la mesa (`decisiones_99_mesa/seleccion/NO_ABRIR_seleccion_pasada_2/`).
  Traen las marcas de la autora y de la lectora de las fichas seleccionadas, y la mesa no las abrió.

## 7. El material de la pasada 2 y la cifra de control

- **`instalar_pasada_2_S1quater.py`:** arma el material de la pasada 2 en la carpeta de la autora. Lo corre ella con el comando de la
  mesa.
  - Por etapa: las fichas seleccionadas, con su bloque de la pasada 1, la condición que las trae y las dos filas; sus imágenes; la
    planilla de la selección, byte a byte; un LEEME y un `manifest.txt`.
  - Controla antes de escribir:
    - el `manifest.txt` de la pasada 1, contra el registro de la mesa del armado (`orden_pasada_1_S1quater.json`, `eb3291ad…`);
    - las planillas, contra sus sellos;
    - la selección, contra su sha256;
    - que la selección sea la de la pasada 1 y cumpla la regla a–d.
  - Prueba con datos sintéticos: 28 de 28 (`salida_prueba_instalar_pasada_2_S1quater.txt`).
- **`cifra_control_sin_vistas_S1quater.py`:** la cifra de control, PROPUESTA de la mesa sellada antes de la pasada 2.
  - Es la cifra del piso de `cifras_lectura_S1quater.py`, con sus mismas funciones y validaciones, sobre las fichas de la etapa 1 que
    quedan sin las de `fichas_vistas_por_el_modelo_S1quater.json`.
  - No decide: decide la de las 90.
  - Prueba con datos sintéticos: 13 de 13 (`salida_prueba_cifra_control_S1quater.txt`).
- **`fichas_vistas_por_el_modelo_S1quater.json`:** los ids opacos de las 26 fichas de la etapa 1 y de las 32 de la etapa 2 cuyo texto
  entró a la sesión c0a11ec7, con la definición de la medición. Las 58 están en el orden de la pasada 1.
- **El sello:** `sello_pasada_2_y_control_S1quater_mesa.txt`.

## 8. Lo que leyó la mesa fuera del repo (§98 y §99)

- **En `fuera_del_repo/adjudicacion_s1quater/pasada_1/`,** con autorización de la autora:
  - el sha256 y la fecha de las dos planillas;
  - el texto de cinco sellos: los de las dos etapas y los de las tres notas;
  - una copia de las dos planillas, con `cp -p`, a su scratchpad. La usó para la selección y para contar, por script, cuánto de ellas
    aparece en su sesión: ninguna nota de 12 caracteres o más y ninguna fila completa.
  - No listó la carpeta ni abrió nada más.
- **En `fuera_del_repo/lecturas_ciegas/`:** una copia de las dos planillas selladas de la lectora, con `cp -p`, para la selección, y el
  control de su sesión por script.
- **La transcripción de la sesión c0a11ec7,** solo por scripts.
  - Error propio de la mesa, del §98: dos salidas de esos scripts dejaron pasar fragmentos de texto, sin ids de ficha y sin marcas. La
    mesa los vio y borró esas salidas. En su sesión no aparece ninguna nota de 12 caracteres o más ni ninguna fila completa de las
    planillas.
- **No abrió:** el scratchpad de la sesión c0a11ec7, `traspaso_etapa2/` ni la carpeta de la evidencia.

## 9. Lo que sigue

1. La autora corre el comando de la mesa que instala la pasada 2 en `fuera_del_repo/adjudicacion_s1quater/pasada_2/`, después de este
   commit.
2. Hace la pasada 2, sin ningún modelo, y la sella como dice el LEEME de cada etapa.
3. La mesa corre `armar`, `aplicar_adjudicacion_S1quater.py`, `cifras_lectura_S1quater.py`, `acuerdo_etapa_1_S1quater.py` y la cifra de
   control, sobre copias, y los sella. Recién ahí se ven cifras.
