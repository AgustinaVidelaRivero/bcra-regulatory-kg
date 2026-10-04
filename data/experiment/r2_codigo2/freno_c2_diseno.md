# U-R2-CODIGO-2 — FRENO C2-diseño: puntos (h) y (n)

Diseño sin implementar, 04/10/2026. Medí sobre HEAD `8d01b04`; durante el freno entró `0b98045`, que solo toca
documentos (mandatos, plan y protocolo) y no cambia ninguna medición. USD 0. No edité el código de la cadena. Medí sobre una copia
del repo armada copiando (regla l) y copié al repo solo los scripts y sus salidas (`c2d_herencia.py`, `c2d_pies.py`,
`salidas/c2d_*.json`).

## Diferencias entre el mensaje del «seguí» y los archivos

- **Hashes.** El mensaje dice «P3 de U-PROMPT-R2 commiteada en `8d01b04`» y «enmienda 3 … firmada en `4aa92c7`».
  Según `git log`, es al revés: P3 está en `4aa92c7` y la firma de la enmienda 3 en `8d01b04`
  (`git log -- data/experiment/esq/enmienda3_L-ESQ-R2_plazo_sin_marcador_2026-10-04.md` y
  `-- data/experiment/prompt_r2/freno_p3.md`). La nota del mandato de `0b98045` ya los asienta así.
- **Cifras de control de (n).** La revisión da 608 pies legibles, 119 páginas sin pie y 9 pies que no se leen
  (cla 5, lingob 2 y polcre 2). Yo mido 617, 119 y 0 (`c2d_pies.json`, `totales`):
  - los 7 pies de cla y polcre se leen: traen «“A“», con la comilla de cierre al revés, que la expresión de la
    revisión no acepta;
  - en los 2 de lingob (p. 13 y 14) se leen la Comunicación y la fecha; lo ilegible es solo la versión de la hoja
    («(cid:21)a.»);
  - las 119 sin pie son 9 carátulas, 40 páginas de tabla de origen y 70 de historial; las páginas de índice sí
    tienen pie (20).
- **Materia.** `r1_referencias.titulos_de_inventario` devuelve el título normalizado, sin tildes y en minúsculas,
  que sirve para resolver citas y no como materia. Propongo leer el título oficial de las mismas dos fuentes que esa
  función (`inventario_tos.csv`, `inventario_resumen.json`), sin normalizar.

## (h) Tope de la herencia en e0-r2 (`c2d_herencia.py` → `salidas/c2d_herencia.json`)

**Regla.**
- Rige solo en e0-r2 y solo en la unidad cuya herencia (la suma del texto de sus tramos) pasa de U = 13.091
  caracteres (`correr_e0.py:75`).
- Los títulos de todos los ancestros (tramos `encabezado`) quedan siempre enteros.
- **Bloques.** Cada bloque de prosa heredado es la intro o el chapeau de un ancestro, su cierre, o sus intersticiales
  de un mismo lado de la unidad. De cada bloque se conserva:
  - el tramo más cercano a la unidad, siempre;
  - si ese tramo pasa B = 2.000 caracteres, sus renglones desde el extremo cercano hasta B, sin partir una tabla
    serializada;
  - desde ahí, tramos enteros hasta sumar B más.
- **Extremo cercano.** Es el final en la intro y el chapeau, que es donde está la cláusula que abre la lista, y el
  final en el intersticial que precede a la unidad.
- **Cierres.** Se conserva su comienzo, igual que el de un intersticial que sigue a la unidad: una salvedad que vale
  para todos los ítems («lo dispuesto precedentemente no rige…») va al principio del cierre.
- **Control de los cierres.** En las unidades sobre U, la búsqueda de frases de alcance en los cierres da 24
  coincidencias. Ninguna es una salvedad sobre los ítems: son citas («lo dispuesto por las normas sobre…») o texto
  descriptivo («mencionados precedentemente»), casi todo en el cierre de la Sección 2 de manual, fuera de las tandas.
- **Marcador.** En el lugar de lo omitido va un tramo de una línea: «[recorte de E0: no se transcriben N caracteres de
  este bloque heredado]». El chunk lleva `herencia_recortada`, con la unidad de origen, el rol, el lado conservado y
  los caracteres omitidos.
- **Qué no cambia.**
  - Los ids.
  - Los mini-chunks, que heredan solo títulos.
  - E3, que lee solo los títulos.
  - Las partes `::parteK`, que arman su herencia en `correr_e0._sub_chunks_de`, reciben el mismo recorte ahí.
  - La posición de cada intersticial sale de la línea de cada segmento. En la medición la tomé de las páginas, y en
    la partición quedan 59 casos ambiguos, que conté como «antes».
- **Qué sí cambia en la unidad recortada.** `chars_completo` y `sha256_completo`, el mensaje de E1 y la regla (i) de
  `remite_a`, que lee la herencia del chunk: una cita que estaba en lo omitido deja de atribuirse en esa unidad. C2 lo
  mide sobre la tanda 0.

**Medición.**

| Salida de E0 | Unidades sobre U | Cambian | Caracteres omitidos | Quedan sobre U |
|---|--:|--:|--:|--:|
| tanda 0, e0-r2 (`salida_tanda0_r2`) | 1 (`ric::11.2.3`) | 1 | 11.305 | 0 |
| partición de B5.8.4 (152 TOs) | 95, en 11 TOs (máx. 264.912); sin los 14 fuera de las tandas, 90 en 10 TOs | 95 | 3.569.250 | 0 |
| e0-r2 de los 152 TOs (corrida de `c1f_ric44.py`, base, fuera del repo) | 93, en 9 TOs (máx. 254.267); sin los 14 fuera de las tandas, 88 en 8 TOs | 93 | 3.615.710 | 0 |

- **`ric::11.2.3`.** Pasa de 15.170 a 3.940 caracteres heredados. Se omiten los cuadros 11.2.1 a) y b) y la tabla030;
  quedan «Cuadro 11.2.2. b)» con la tabla031, el marcador y los dos títulos.
- **Estrato de la pareada.** Con U = 13.091 no cambia ninguna unidad de ayccef, expaef, opefci ni adrei: ninguna pasa
  el umbral.
- **Otros B.** Con B = 1.000 o 4.000 cambian las mismas unidades. Con 4.000 quedan 6 unidades de la partición sobre U.

## (n) Versión y materia del TextoOrdenado (`c2d_pies.py` → `salidas/c2d_pies.json`)

- **Dónde se guarda.** Una función pura nueva de `e0_lib` lee el pie de cada página con el mismo criterio con que
  e0-r2 lo recorta: la línea de `RE_PIE_VERSION` entre las últimas tres y lo que la sigue, más los renglones de
  `RE_PIE` que quedan encima. De ahí saca la versión de la hoja, la Comunicación, la hoja y la fecha de vigencia.
- **Archivo.** Solo en e0-r2, `correr_e0` escribe `pies_<to>.json` por TO: el estado y los campos de cada página, la
  versión vigente y la línea de la carátula, si se lee.
- **Qué no cambia.** Ni los chunks, ni `conteos.json`, ni ningún archivo que ya existe. El texto de las unidades y el
  mensaje de E1 no cambian.
- **Versión vigente.** Entre las páginas legibles, la de fecha de vigencia más reciente; si empatan, la de mayor número.
  El mayor número a secas falla: en ctacte el mayor es B 9620, y la carátula dice A 8444.
- **Valor.** «Comunicación A 8378 (vigencia 20/12/2025)», en `version`, que `PropsTextoOrdenado` admite como texto.
- **Páginas sin pie.** Quedan con el estado `sin_pie` y no cuentan.
- **Pie que no se lee** (falta la Comunicación o la fecha). Queda con el estado `no_legible`, con sus renglones, y no
  cuenta.
- **Versión de hoja ilegible.** La página cuenta, con `version_hoja` en null.
- **Sin páginas legibles.** Si un TO no tiene ninguna, el TextoOrdenado queda sin `version` y el reporte del ensamblado
  lo declara.
- **Ensamblado r2b.** Pone `version` y `materia` (el título oficial del inventario) y lista los diez en su reporte, con
  el contraste contra la carátula.

**Medición, diez TOs.**
- Las cuentas de páginas están arriba. La versión vigente coincide con la carátula en 8 de 8; ric no tiene carátula y
  la de pagjub trae «(cid:25)386», compatible con A 6386.
- **Materias que salen.** Algunas están abreviadas en el inventario: ric, «RI Cont. Mensual - Exigencia e integración
  de capitales mínimos»; pagjub, «Pago de beneficios de la seg. soc. por cuenta de la Adm. Nacional de la Seguridad
  Social (ANSES)». Otra trae un punto final: ext, «Exterior y cambios.». Las uso tal cual; si la autora prefiere el
  título de la carátula, es otro cambio.

## Comandos

```
data/experiment/r2_codigo2/c2d_herencia.py --salida-e0 tanda0=data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2 --salida-e0 particion=data/experiment/segmentacion_84/b584_particion --salida-e0 e0r2_152=<e0-r2 de los 152, fuera del repo> --bloque 1000 2000 4000 --out data/experiment/r2_codigo2/salidas/c2d_herencia.json
data/experiment/r2_codigo2/c1f_ric44.py --correr-tos todos --variante base --salida <dir fuera del repo>
data/experiment/r2_codigo2/c2d_pies.py --out data/experiment/r2_codigo2/salidas/c2d_pies.json
```

Desde la raíz de una copia del repo, con `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B`.
