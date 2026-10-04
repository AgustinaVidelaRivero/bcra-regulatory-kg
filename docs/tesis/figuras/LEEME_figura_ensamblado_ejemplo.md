# figura_ensamblado_ejemplo — registro de generación (versión 2)

Figura «el ejemplo después del ensamblado» para la sección 4.5 de la tesis:
el fragmento de grafo del punto 5.1.1.1 de Clasificación de deudores que
muestra la figura de la salida del extractor (sección 4.2, versión 2), leído
ahora del grafo ensamblado, con lo que el ensamblado le agrega.

- **Lo que ya estaba** en la figura del extractor (seis cajas y cinco flechas
  rotuladas) conserva disposición, estilo y rótulos: baja entero 134 unidades,
  sin otro cambio, para dejar arriba una franja nueva. Un solo texto cambia,
  porque cambió en el grafo: la etiqueta del Texto Ordenado (§4).
- **Lo nuevo**:
  - la caja del nodo de destino de la remisión al punto 3.7 (`Definicion`,
    «Importe de referencia»), en la franja de arriba;
  - las dos `remite_a` que llegan a ella, en línea discontinua gris y
    rotuladas;
  - el umbral de la condición del monto, arriba de su caja, con la marca «≤» y
    sus campos valor, unidad, comparación y base. La comparación va leída en
    castellano (§3).
- **Excluidas a propósito**: las dos `establecida_en` que el ensamblado deriva
  de la procedencia para las dos condiciones. No se dibujan; el inventario las
  descuenta (§3).
- **Sin color ni leyenda.** Nada marca lo nuevo; el epígrafe lo explica.

Alto impreso a 15 cm de ancho: **8,93 cm** (lienzo 850 × 506, la escala de la
figura del extractor; PDF 425,2 × 253,1 pt; PNG 1772 × 1055 px a 300 dpi).
Cruces entre flechas: **0**.

La figura **no es provisional por la versión del grafo**: el grafo está
versionado (§1). Se regenera con el grafo del escalado pasándole su ruta y su
sha256 (§11).

## Versiones

- **Versión 1** (04/10/2026, sin commit, aprobada con 2 correcciones):
  - dibujaba también las dos `establecida_en` derivadas, una por debajo de
    toda la figura y otra con un cruce sobre la `establecida_en` de la
    operación;
  - mostraba la comparación con su valor interno, `minimo_estricto`;
  - alto de 9,35 cm;
  - sha256: generador
    `4d8c9064776e6708252ac3635ff9ca98058604aa52a5a29060c72904ae2d0cb9`, SVG
    `f676a09d975151f551ac15e942fdf780b86180e38581ac7d78039b795e78daee`, PNG
    `5b270954d33948fb1d8530ddc973e82b91c22df66029c35c9f49dd994ecd91ae`, PDF
    `9f6337ba7833df9d6054080474bc7523a435356c721a8aebfb652cf640985c5b`, LEEME
    `a852afd89992d09e87eb9471701a1d49cc732cab228269a9925ab6bee2c4a88d`;
  - los archivos quedaron en el paquete de revisión de esa versión, fuera del
    repo.
- **Versión 2** (04/10/2026). Qué cambió (además, se corrige la cita de
  `derivar_establecida_en`, que la versión 1 daba en `:590-608` y empieza en
  `:592`):
  - la comparación se lee en castellano con la tabla `LECTURA_COMPARACION`,
    tomada de las definiciones de `reglas_comparacion.py`, que entra como
    fuente con candado (§3);
  - las dos `establecida_en` derivadas se excluyen a propósito
    (`EXCLUIR`, `EXCLUIDAS`). El inventario las descuenta, y el script frena
    si las que cumplen la regla no son exactamente esas dos;
  - sin esas dos flechas desaparece el único cruce: los cruces declarados
    pasan de 1 a 0 y el alto, de 9,35 a 8,93 cm;
  - entra una prueba negativa, la relación excluida dibujada (10 en total);
  - el resto queda igual: las cajas, las dos `remite_a`, el panel del umbral
    y la conservación de lo que ya estaba.

## 1. Fuente: el grafo

`data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo_r2a/r2/kg.json`,
sha256 `93a7af7279a415ee72cfec547bcd080d4c85a96746e219ed94dea4239007e8dd`.
**Versionado**: lo commitea `f8dedd4` (03/10/2026, U-MED-R2A M1, que lo nombra
KG-Tanda0-Desarrollo-r2a), y el archivo del árbol tiene ese sha. Tiene 6.470
nodos y 24.728 aristas.

Su reporte de ensamblado,
`data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo_r2a/r2/reporte_ensamblado_r2.json`,
declara `"perfil": "r2"`, `"grafo": "tanda0_ens_desarrollo/r2"`,
`"perfil_e1_del_crudo": "v3_b54"` y como entrada
`data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida`. Es la misma
corrida de E1 que dibuja la figura del extractor (su LEEME §1: los registros
de la unidad en `salida/` y en `salida_dirigida/` son byte-idénticos).

**Por qué este grafo.** Es el único del conjunto de desarrollo construido con
el perfil r2. Los otros dos, `corpus_tanda0/ens_desarrollo/kg.json` y
`corpus_tanda0/ens_desarrollo/r1/kg.json`, son del 28/09 (`1b8916c`), y
ninguno declara el perfil r2. Ningún `kg*.json` del repo (sin `.git` ni
`.venv`) es posterior al 03/10/2026 09:00, salvo este y su par de diez
documentos, `ens_diez_r2a/r2/kg.json`.

```
for f in $(find data/experiment -name kg.json -path '*desarrollo*' | sort); do echo "$f $(git log -1 --format='%h %ad' --date=iso -- "$f")"; done
find . \( -path ./.git -o -path ./.venv \) -prune -o -name 'kg*.json' -newermt '2026-10-03 09:00' -print | sort
shasum -a 256 data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo_r2a/r2/kg.json
```

**El vecindario.** Lo forman las aristas que tienen a `cla::5.1.1.1` entre sus
procedencias y sus extremos: **7 nodos y 9 aristas**. De esas 9 aristas se
dibujan 7: las 2 excluidas se cuentan en §3. El destino de la remisión al 3.7
entra como extremo de sus dos `remite_a`. El generador frena en estos casos:

- un nodo que viene solo de la unidad tiene una arista fuera del vecindario
  (hoy, ninguno de los cuatro);
- un nodo con la unidad entre sus procedencias no tiene aristas;
- un extremo ajeno a la unidad no es solo destino de una `remite_a` cuyo
  `destino` es su procedencia;
- las aristas que cumplen la regla de exclusión no son las declaradas.

| Rol | Nodo | Procedencias |
|---|---|---|
| `e1` | `Definicion` «Cartera comercial — créditos consumo/vivienda» | 1, solo la unidad |
| `e2` | `Condicion` «Monto supera dos veces importe referencia 3.7» | 1, solo la unidad |
| `e3` | `Condicion` «Repago vinculado a actividad productiva/comercial» | 1, solo la unidad |
| `e4` | `Operacion` «Clasificación de crédito en cartera comercial» | 1, solo la unidad |
| nodo del 3.7 | `Definicion` «Importe de referencia» | 1, `cla::3.7` |
| sujeto | `Sujeto` «Obligados a clasificar deudores (Clasificación)» | 91 |
| `to` | `TextoOrdenado` «Clasificación de Deudores» | 143 |

Los roles `e1` … `e4` y `to` son los identificadores locales de la figura del
extractor. El generador empareja cada caja de esa figura con su nodo por tipo
y etiqueta; si la etiqueta cambió, la empareja con el único nodo de la unidad
de ese tipo. Los nodos nuevos llevan un rol declarado (`NUEVOS`).

## 2. Fuente: la figura del extractor

El generador recompone la figura del extractor con su propio generador,
`generar_figura_extractor_ejemplo.py` (sha256
`7cc8cc1106412e79c99a23c70887d46cf5b5e85354766f8c734d1fcb021bd5a5`), que lee
su registro y su catálogo con sus candados (su LEEME, §1 y §2). El SVG
recompuesto tiene que ser byte a byte el registrado en su LEEME §10,
`46e6cb24bd397eaa8d6d6a1ba3a83ba329ff8a0739e2cf319bd10feea6e9fac5`; si no lo
es, el generador frena. De esa composición salen las cajas, las flechas y los
rótulos de lo que ya estaba.

**No versionados**: `generar_figura_extractor_ejemplo.py` y
`figura_extractor_ejemplo.{svg,png,pdf}` están sin commitear
(`git status --short docs/tesis/figuras/`: `??`). El commit de esa figura es
una acción de la autora, PENDIENTE. Esta figura depende de ese generador: si
cambia, el candado del SVG la frena.

## 3. Qué agrega el ensamblado, qué se dibuja y qué se excluye

De las 9 aristas del vecindario:

- **5** son las de la figura del extractor, conservadas;
- **2 son nuevas y se dibujan**: las `remite_a`;
- **2 son nuevas y se excluyen a propósito**: las `establecida_en` derivadas.

| Relación | Atributos en el grafo | En la figura |
|---|---|---|
| `e2` `remite_a` nodo del 3.7 | `properties`: `alcance` `interna`, `destino` `cla::3.7`, `evidencia` | discontinua, rotulada |
| `e1` `remite_a` nodo del 3.7 | ídem | discontinua, rotulada |
| `e2` `establecida_en` `to` | `rol_fuente` `derivada_de_procedencia` | **excluida** |
| `e3` `establecida_en` `to` | ídem | **excluida** |

**Las relaciones excluidas.** Las dos `establecida_en` las deriva el
ensamblado de la procedencia, no el extractor:

- código: `data/experiment/tanda0/code/ensamblar_tanda0.py@b0ee084:592-608`,
  `derivar_establecida_en`, con `rol_fuente` = `derivada_de_procedencia`;
- el reporte de ensamblado cuenta 372 en el grafo, 84 de ellas desde una
  `Condicion`.

Están en el grafo y la figura no las dibuja, por decisión de la revisión de
la versión 1. Cómo lo maneja el generador:

- `EXCLUIR` es la regla: `relation` = `establecida_en` y `rol_fuente` =
  `derivada_de_procedencia`;
- `EXCLUIDAS` declara las aristas que tienen que cumplirla, por rol:
  `(e2, establecida_en, to)` y `(e3, establecida_en, to)`;
- si las que la cumplen no son exactamente esas, o si una es de la figura del
  extractor, el script frena;
- el inventario compara la figura con las 7 aristas restantes, y la consola
  las informa como `excluida`;
- la prueba negativa `excluida_dibujada` comprueba que dibujar una haga fallar
  el inventario.

**El umbral** de `e2`, la única entrada de `properties.umbrales` del
vecindario:

| Campo en el grafo | Rótulo en la figura | Valor interno | En la figura |
|---|---|---|---|
| `valor` | valor | `2` | 2 |
| `unidad` | unidad | `veces` | veces |
| `comparacion` | comparación | `minimo_estricto` | mayor que |
| `base` | base | `importe de referencia establecido en el punto 3.7` | ídem, en dos líneas |

Los otros seis campos del elemento no se dibujan: `tramo` («dos veces»),
`regla_comparacion` (`simple:raiz_super`), `origen` (`descripcion`),
`tramo_verificado` (`exacta`), `base_destino` (`cla::3.7`) y `base_via`
(`remision`). Una clave fuera de esas diez frena el generador.

**Tabla de equivalencias de la comparación** (`LECTURA_COMPARACION`). Cubre
los 7 valores del enum
(`data/experiment/pyd_r2/code/modelos_r2.py@b0ee084:203-204`,
`COMPARACION`). La lectura sale de las definiciones del docstring de
`data/experiment/pyd_r2/code/reglas_comparacion.py`: sha256
`0cd2afbf7356e3674cbe54daf367ea5c55353b8be326551fea28ed1ece3db821`, último
commit `57a8dd2`, sin cambios en el árbol. El generador lo lee con ese
candado y frena si alguno de los 7 valores no figura en él como literal.

| Valor interno | Lectura en la figura | Definición (`reglas_comparacion.py`) |
|---|---|---|
| `minimo_estricto` | mayor que | :14-17, «super-», «exced-», «más de», «mayor(es) a» |
| `maximo_estricto` | menor que | :17, «inferior(es) a», «menos de», «menor(es) a» |
| `minimo_inclusivo` | mayor o igual que | :26-28, «igual o superior/mayor», «al menos», «como mínimo» |
| `maximo_inclusivo` | menor o igual que | :28-29, «igual o inferior/menor», «como máximo», «hasta» |
| `igual` | igual a | :35-36, «igual(es) a/al», «equivalente(s) a/al» |
| `coeficiente` | coeficiente | :10-11, «pondera…», «ponderador», «coeficiente», «factor» |
| `no_determinada` | no determinada | :44-45, cuantía sin marcador que no es un plazo |

Un valor de comparación sin lectura en la tabla frena el generador.

## 4. Qué cambió de lo que ya estaba

- **La etiqueta del Texto Ordenado.** En la salida del extractor es
  «Clasificación de deudores»; en el grafo, «Clasificación de Deudores». El
  ensamblado unió el Texto Ordenado de la unidad con el nodo único del
  documento (`TextoOrdenado_to_clasificacion_deudores_actual_pdf`, 143
  procedencias, 491 aristas, 4 de ellas de la unidad), y la etiqueta es la de
  ese nodo. Se dibuja la del grafo, en el mismo lugar y en una línea, como
  antes. De esas 4 aristas de la unidad se dibujan 2: las otras 2 son las
  excluidas.
- **El sujeto** es el nodo del catálogo
  (`Sujeto_rol_obligado_a_clasificar_clasificacion`, 91 procedencias, 167
  aristas, 1 de la unidad), con la misma etiqueta que la figura del extractor
  toma del catálogo. No cambia nada en la figura.
- **Las dos `condicion_de`** están en el grafo con `no_verificada_e3: true`.
  La figura del extractor las dibuja de la salida cruda; el validador de la
  corrida `v3_b54` las había rechazado por firma
  (`corpus_tanda0/salida/cla/finales.jsonl:61`, `validacion_final.rechazos`: 2
  `firma_invalida`, `Condicion --condicion_de--> Operacion`). El ensamblado r2
  las conserva. La figura no marca el atributo.
- **`aplica_a`** lleva en el grafo `mencion_verificada: ausente` y
  `metodo_resolucion: R4_sugerencia_modelo`; tampoco se marca.
- **Ninguna relación retirada** y ningún nodo de la figura del extractor sin
  nodo en el grafo.
- **Lo que no se dibuja** del nodo del 3.7: sus otras 21 aristas (20
  `remite_a` que llegan desde otras unidades y 1 `establecida_en` hacia el
  Texto Ordenado, de `cla::3.7`). Del Texto Ordenado y del sujeto, solo se
  dibujan sus aristas de la unidad que no están excluidas.

```
sed -n 61p data/experiment/reextraccion_v2/corpus_tanda0/salida/cla/finales.jsonl | PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B -c "import json,sys;print(json.loads(sys.stdin.read())['validacion_final']['rechazos'])"
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B -c "import json;from collections import Counter;k=json.load(open('data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo_r2a/r2/kg.json'));D='Definicion_importe_de_referencia__el_importe_a_considerar_sera_el_nivel_maximo_del_valor_de_bd1e8e';ch=lambda x:[p['chunk_id'] for p in (x.get('provenances') or [x['provenance']])];print(Counter((e['relation'],'cla::5.1.1.1' in ch(e)) for e in k['edges'] if D in (e['source'],e['target'])))"
```

## 5. Estilo

Lo que ya estaba conserva el estilo de la figura del extractor (su LEEME §3),
que su generador lee de `figura_esquema_final.svg` (versión 3, sha256
`dfdb16d471bb93c6351aa03b1e609452b75c428baa354c52354ce1dfe9797bb3`). De ese
mismo SVG, con el mismo candado, este generador lee lo nuevo:

- **`remite_a`**: `#8a8a8a`, grosor 1,6 y discontinuo `7 5`, el único estilo de
  sus caminos `data-pred="remite_a"`. Las puntas son las de las demás flechas.
  El rótulo va en el gris de los demás (`#6f6f6f`), no en el magenta que lleva
  en la figura del esquema final.
- **La marca de umbrales**: cuadro de 18 × 18, esquinas de 3, `#3d3d3d`, con
  «≤» en Helvetica negrita de 15, blanco. El generador comprueba que sea la de
  `generar_figura_esquema_final.py` (`MARCA`, `COLOR_MARCA`) y la dibuja con su
  función `marca_svg`.
- **El panel del umbral**: nombres de campo en Menlo de 15 (7,50 pt), en el
  gris de los rótulos; valores en Helvetica de 15, en la tinta de las
  etiquetas.

La caja del nodo del 3.7 tiene el estilo de su tipo (`Definicion`: `#f8e8f5`,
`#b5179e`, 2,6) y el tamaño común, 230 × 76.

## 6. Disposición

**Lo que ya estaba baja `DY` = 134** (el alto de caja, 76, más la calle entre
filas de la figura del extractor, 58). Arriba quedan:

- **el nodo del 3.7**, en (606, 14), sobre la definición de la cartera
  comercial (`LUGAR_NUEVOS`);
- **el panel del umbral**, arriba de la condición del monto. Empieza con la
  marca en (14, 27), a la altura de la primera fila. Los nombres van en x = 40
  y los valores en x = 149,33, a 10 del nombre más largo; la base se envuelve
  en 185 de ancho y ocupa dos líneas. La última línea queda a 35 del borde
  superior de la caja: el panel queda a 31,7 de su caja, entre x = 14 y
  x = 328,6, y avanza 18,6 sobre el ancho de la columna del medio (§13).

Rutas nuevas (`rutas_nuevas`, calculadas de los rectángulos de las cajas):

| Relación | Puntos | Rótulo |
|---|---|---|
| `e1` `remite_a` 3.7 | (721, 148) → (721, 90) | a la derecha |
| `e2` `remite_a` 3.7 | (244, 168) → (277, 168) → (277, 130) → (640, 130) → (640, 90) | arriba del tramo largo |

- La `remite_a` de la definición sube recta hasta el nodo del 3.7.
- La `remite_a` de la condición del monto sale por su lado derecho y sube por
  el hueco entre las dos condiciones. Corre 18 por encima de la fila de
  arriba y entra por abajo al nodo del 3.7.
- **Cruces: 0** (`CRUCES_DECLARADOS` vacío). El único cruce de la versión 1
  era el de la `establecida_en` derivada de la condición del repago, que ya
  no se dibuja. Su ruta de la versión 1 queda en el generador solo para la
  prueba negativa de la relación excluida dibujada
  (`ruta_excluida_de_prueba`).

## 7. Controles

Salida de la corrida que escribió las salidas del repo (extracto):

```
INVENTARIO (releído del SVG): 7 cajas y 7 relaciones contra 7 y 7 del vecindario (9 aristas, 2 excluidas a propósito); fallas: 0
CONTENIDO: 36 textos, 30 piezas; fallas: 0
TEXTOS: 36 textos contra 7 cajas y 7 flechas; distancias mínimas texto-texto 3.0; rótulo-su flecha 4.0; rótulo-otra flecha 59.5; texto-borde de su caja 9.0; fallas: 0
CAJAS: 7 cajas; fallas: 0
TRAZOS: 10 tramos en el SVG; fallas: 0
FLECHAS: 7 flechas; fallas: 0
CRUCES: 0 cruce(s) entre flechas, declarados 0; fallas: 0
MARGEN: 50 elementos y la marca del umbral; mínimo a cada borde izquierdo 12.7 u = 2.24 mm, superior 12.7 u = 2.24 mm, derecho 12.7 u = 2.24 mm, inferior 13.0 u = 2.29 mm; marca 14.0 u; exigido 2.0 mm (11.3 u); fallas: 0
CONSERVACION: 37 de 38 elementos de la figura del extractor iguales (bajados 134); cambios declarados 1; fallas: 0
REMISIONES: 2 flechas discontinuas; fallas: 0
UMBRAL: campos [['valor', '2'], ['unidad', 'veces'], ['comparación', 'mayor que'], ['base', 'importe de referencia establecido en el punto 3.7']]; a 31.7 de su caja; a 13.7 de la flecha más cercana; fallas: 0
REGISTRO: 48 elementos de primer nivel del SVG; fallas: 0
LETRA 15 unidades -> 7.50 pt impresos a 15 cm
LETRA 19 unidades -> 9.50 pt impresos a 15 cm
```

- **Ocho controles de la figura del extractor**, reutilizados por
  importación sobre el registro de elementos de esta figura: inventario,
  contenido, textos (con la letra mínima), cajas, trazos, flechas, margen y
  registro.
  - El inventario relee el SVG solo desde su geometría y lo compara con el
    vecindario del grafo, sin las relaciones excluidas.
  - El margen suma la marca del umbral.
  - El de cruces se reescribe solo para comparar con los cruces declarados de
    esta figura (ninguno); usa el conteo de la figura del esquema final.
- **Conservación.** Cada elemento de primer nivel del SVG de la figura del
  extractor, bajado 134, tiene que estar en este SVG con los mismos atributos
  y el mismo texto. La excepción son los cambios que trae el grafo: una
  etiqueta cambiada va en el mismo lugar con el texto nuevo, y una relación
  retirada no se dibuja. Hoy: **37 de 38** iguales; el que falta es la
  etiqueta del Texto Ordenado, que está en su lugar con el texto del grafo.
- **Remisiones.** Las flechas discontinuas tienen que ser exactamente las que
  tienen el rótulo `remite_a` más cerca, con el discontinuo, el gris y el
  grosor de la figura del esquema final.
- **Umbral.** El panel se relee del SVG. Sus filas tienen que dar los cuatro
  campos del grafo, en orden y con el nombre en castellano, y la comparación
  con su lectura de la tabla. La marca tiene que estar a la izquierda de la
  primera fila. Su caja es la que está debajo del centro del panel, a 40 o
  menos; ningún texto del panel ni la marca pueden quedar a menos de 9 de una
  flecha.
- **Conteos.**
  - 38 elementos de la figura del extractor = 5 caminos + 5 puntas + 6 cajas
    + 22 textos.
  - 48 elementos de primer nivel = 7 caminos + 7 puntas + 7 cajas + 26 textos
    (7 tipos, 12 líneas de etiqueta, 7 rótulos) + el grupo del umbral.
  - 36 textos controlados = esos 26 + los 10 del panel (la marca, 4 nombres y
    5 líneas de valor).
  - 30 piezas = 7 tipos + 7 etiquetas + 7 rótulos + la marca + 4 nombres + 4
    valores.
  - 10 tramos = 5 de las flechas que ya estaban + 1 de la `remite_a` de la
    definición + 4 de la `remite_a` de la condición.
  - 50 elementos del margen = 36 textos + 7 cajas + 7 flechas.

## 8. Pruebas negativas

Cada corrida planta diez defectos antes de componer la figura y frena si
alguno no hace fallar su control. Las cinco primeras son las de la figura del
extractor, adaptadas; la entidad de menos quita la caja del nodo del 3.7.

```
PRUEBAS NEGATIVAS: 10 de 10 hacen fallar su control
  relacion_de_mas -> inventario: rótulo 'regula' sin una flecha que sea, sin ambigüedad, la más cercana (fallan también: remisiones, textos)
  entidad_de_menos -> inventario: flecha de (721.0, 148.0) a (721.0, 90.0): 1 caja(s) de origen y 0 de destino (fallan también: contenido, flechas)
  rotulo_sobre_caja -> textos: 'aplica_a': se superpone con la caja de sujeto:Sujeto_rol_obligado_a_clasificar_clasificacion (fallan también: conservacion)
  tramo_diagonal -> trazos: tramo diagonal de (277, 358) a (307, 416) (fallan también: conservacion, textos)
  cruce_de_flechas -> cruces: 1 cruce(s) entre flechas, declarados 0: [(('e2', 'condicion_de', 'e4'), ('e3', 'condicion_de', 'e4'))] en (203.0, 253.0) (fallan también: conservacion, inventario, textos)
  remite_continua -> remisiones: camino 7 (M 244 168 L 277 168 L 277 130 L 640 130 L 640 90): discontinuo None, rótulo ['remite_a']
  umbral_campo_de_menos -> umbral: campos del panel [...] ≠ del grafo [...] (fallan también: contenido)
  umbral_lejos -> umbral: el panel no está junto a su caja: debajo de su centro [(31.7…, ('Definicion', 'Cartera comercial — créditos consumo/vivienda'))], esperada ('Condicion', 'Monto supera dos veces importe referencia 3.7') a 40 o menos (fallan también: margen, textos)
  caja_movida -> conservacion: elemento de la figura del extractor que no está (bajado 134): rect '' {... 'x': '310', 'y': '148'}
  excluida_dibujada -> inventario: relación de la figura que no está en el grafo o está excluida: (('Condicion', 'Repago vinculado a actividad productiva/comercial'), 'establecida_en', ('TextoOrdenado', 'Clasificación de Deudores')) (fallan también: cruces)
```

Con `--perturbar <caso>`, sobre una copia, los diez casos terminan con «FALLA:
la figura tiene defectos; no se escribe nada», código de salida 1 y ningún
archivo en el directorio de salida.

## 9. Reproducibilidad

Tres corridas sobre una copia de los nueve archivos que usa el generador en
el scratchpad (copiados, sin enlaces), con `PYTHONHASHSEED` 0, 1 y 4242. Las
tres dan los mismos SVG, PNG y PDF, iguales a los del repo, y la misma salida
salvo la ruta. Los sha256 de los archivos del repo (sin `.venv` ni `.git`)
son iguales antes y después de esas corridas y de las diez perturbaciones. La
corrida que escribió en el repo cambió solo los tres archivos de la figura.

Los nueve archivos:

- este generador y los de la figura del extractor, del esquema final y del
  proceso de extracción;
- `figura_esquema_final.svg`;
- el registro de E1 y el catálogo de la figura del extractor;
- el grafo;
- `reglas_comparacion.py`.

## 10. Salidas (versión 2)

| Archivo | sha256 |
|---|---|
| `generar_figura_ensamblado_ejemplo.py` | `77801c9598efd1e3ec53602c0742f7bfe5b8db23a2ee96d3b2bfe7c695b1d434` |
| `figura_ensamblado_ejemplo.svg` | `c1078dc3716b1aaf70a75146d807b56f9fc9a886663250a8c0ccd53a20e0f67b` |
| `figura_ensamblado_ejemplo.png` | `0b487134f3f251c344994879226e0d727aecb8024ccb8be31ce3a4fbe8d468c0` |
| `figura_ensamblado_ejemplo.pdf` | `c10295ed83e3c686edd7ed4e87b43a15f0d7fa48ca6ea58a548919d0669899f4` |

PDF con `/CreationDate` fijada por `SOURCE_DATE_EPOCH=0`; stream de contenido
sha256 `fde2d7a6dc5a2c9737534c30108b5aaba77e078a088cbd89e3d1eedf5473e2e9`.

```
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_ensamblado_ejemplo.py
```

Este LEEME cae en `.gitignore:180` y entra solo con `git add -f`.

## 11. Regenerar con otro grafo

```
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B docs/tesis/figuras/generar_figura_ensamblado_ejemplo.py --grafo <kg.json> --sha256-grafo <sha256>
```

Una ruta distinta de la de omisión sin su sha256 frena. El generador frena
también en estos casos:

- el vecindario no cumple lo de §1;
- las relaciones que cumplen `EXCLUIR` no son las de `EXCLUIDAS`;
- una caja de la figura del extractor no tiene nodo en el grafo, o un nodo
  nuevo no tiene rol en `NUEVOS`;
- una etiqueta cambiada ocupa otra cantidad de líneas;
- las relaciones nuevas que se dibujan no son exactamente las de
  `rutas_nuevas`;
- otro nodo lleva umbrales, la condición del monto lleva más de uno, el umbral
  trae una clave desconocida o una comparación sin lectura en la tabla;
- `reglas_comparacion.py` cambió;
- los cruces no son los declarados (ninguno).

Con el grafo del escalado, lo esperable es declarar de nuevo roles, rutas,
relaciones excluidas y cruces; los controles comprueban lo que se declare.
Los conteos de este LEEME y del epígrafe son de este grafo.

## 12. Epígrafe propuesto

> Fragmento de grafo del punto 5.1.1.1 de Clasificación de deudores después
> del ensamblado, en el grafo de la tanda 0 sobre el conjunto de desarrollo.
> Lo que muestra la figura de la salida del extractor conserva su lugar y su
> forma, salvo la etiqueta del Texto Ordenado, que pasa a ser la del nodo
> único del documento. El ensamblado agrega la definición del importe de
> referencia del punto 3.7 con las dos remisiones que llegan a ella, en línea
> discontinua, y, arriba de la condición del monto, su umbral con la marca ≤ y
> sus campos. Las demás relaciones del Texto Ordenado, del sujeto y de la
> definición del punto 3.7 no se dibujan.

La remisión a la figura de la sección 4.2 va con su `\ref` en el `.tex`. Si el
capítulo 4 nombra la tanda 0 de otra manera, el epígrafe toma ese nombre.
Respecto de la versión 1, sale «la relación establecida_en de las dos
condiciones», que ya no se dibuja: esas relaciones del Texto Ordenado quedan
dentro de la última oración.

## 13. Observaciones

- **Impreso**: NO VERIFICADO. La letra mínima (7,50 pt) y el margen (2,24 mm)
  se controlan sobre la geometría.
- **El panel del umbral** avanza 18,6 sobre el ancho de la columna del medio,
  porque la segunda línea de la base mide 179,3. Su centro (x = 171,3) cae
  sobre la condición del monto, que es la caja que el control le asigna.
- **Las relaciones excluidas siguen en el grafo**: la figura las omite por
  decisión, y un lector del grafo las encuentra.
- **La figura del extractor no está commiteada** (§2); esta depende de su
  generador.
