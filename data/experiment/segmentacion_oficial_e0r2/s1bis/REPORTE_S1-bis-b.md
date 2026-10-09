# U-SEG-OFICIAL — S1-bis-b: sorteo sellado, fichas de lectura y procedimiento de la lectura, sin leer

Tramo b de S1-bis del mandato FIRMADO en `e543cb2`, con las notas al pie de `2faff14` (criterio, muestra y piso), `26c6502`,
`a757b32` (semillas) y `2abb346` (revisión del FRENO S1-bis-a por la mesa), y las decisiones de la autora sobre el FRENO
S1-bis-a, registradas en `acta_sorteo_S1bis.md`. USD 0, sin API. Código de E0: el de `18d9e05`, que no se volvió a correr.
Escribí solo `s1bis/` y el scratchpad; nada commiteado. **No leí ni marqué ninguna unidad**, y la cifra de la lectura no
existe todavía: sale de la lectura de la mesa.

## 1. Entrada

- HEAD `2abb346` (la revisión de la mesa del tramo a, con su nota al pie del mandato). Foto sha256 del repo (48.154
  archivos, 17:29:22) y 2.213 `.pyc`. `s1bis/` del tramo a: 792 de 792 contra `manifest_salida.json`; el FRENO S1-bis-a,
  `dcecf45e…`, el revisado.
- La nota de `2abb346` suma, fuera de la lista de límites del tramo a, las 21 intros de la tanda 0 que quedaron fuera de 4a
  y 4b, en el estrato vigente (0,10 esperadas). Su regla la decidió la autora antes de leer (acta, §2).

## 2. El acta, sellada antes del sorteo (`acta_sorteo_S1bis.md`, 17:30:31, `fdf6704f…`)

- §1, las decisiones de la autora: ri_spi sigue no segmentable, 10 unidades aparte y fuera del piso; ri_pspii, juicio
  correcto; ri_tii, límite declarado y candidato a una regla por lista en la release de E0 antes de la tanda en la que
  caiga; ri2_pm sale entero de esta lectura (con `3.5.3` y `1.6`), pendiente de una lectura propia antes de la release que lo
  incluya; ri_tar sigue vigente.
- §2, la regla de las 21 intros de la tanda 0: se leen con el mismo criterio; un error de corte cuenta para el piso; en el
  reporte, aparte, como límite declarado de la tanda 0; no se informa si cayó alguna antes de la lectura.
- §3, el sorteo; §4, la lectura a ciegas; §5, lo que se calcula después de leer, incluida la cifra del piso con `ri2_ae::3.3` y
  `5.3` contados y sin contar si salen (cuál vale lo decide la autora).
- Después del sorteo, una nota fechada al final del acta, sin tocar el texto sellado (el archivo da ahora `c6943e21…`).

## 3. El sorteo (`muestra_cortes_S1bis.json`, 17:31:16, `33b24c0b…`; `scripts/muestra_cortes_S1bis.py`)

- Primer grupo: `random.Random(f"U-SEG-OFICIAL:cortes:S1-bis:{estrato}").sample(ids, n)`, con los ids de la población
  recalculados desde `e0/` y controlados contra `poblacion_muestra_S1bis.json` (lista y sha256 iguales en los tres
  estratos): 40 de 8.034 (vigente), 10 de 190 (marcadores) y 40 de 1.222 (sin raíz).
- ri_spi: `random.Random("U-SEG-OFICIAL:cortes:S1-bis:ri_spi").sample(sorted(ids), 10)`, 10 de 93 (ids controlados contra
  la población).
- Segundo grupo: vacío. Tercer grupo: 11 juicios, 9 para leer; ri_pspii y ri_tii llevan el resultado decidido.
- Censo del 1.16 de la tanda 1: los 35 candidatos, en 11 TOs, 50 páginas y 34.284 caracteres propios.
- La repetición del sorteo en otro archivo da el mismo byte a byte.
- A ciegas: la muestra lleva, de cada unidad, id, TO, grupo, páginas, tipo, rol, herencia y texto propio; ninguna marca de
  límite declarado, de TO de la tanda 0 ni de candidato del 1.16 en la muestra.

## 4. Fichas de lectura (en el paquete del freno)

- `fichas_lectura_S1-bis-b.md` (`scripts/fichas_lectura_S1bis.py`): 100 fichas de unidades (90 y 10), 11 de juicios (9 para
  leer, con todas las páginas del documento) y 35 del censo del 1.16 (con la lista y el cierre candidato), cada una con el
  nombre de la imagen de cada página.
- `paginas_S1-bis-b/`: 301 páginas renderizadas con `../s1/scripts/renderizar_muestra_S1.py`, sin cambios
  (`pdftoppm -r 110`), 0 errores; sha256 de cada imagen en `renders_S1bis_b.json`.
- `planilla_marcas_S1-bis-b.tsv` (111 filas: 90, 10 y 11; los dos juicios decididos ya cargados) y `planilla_1_16_S1-bis-b.tsv`
  (35 filas), vacías, con las columnas de la lectura de S1.

## 5. Lo que se calcula después de leer, fijado ahora

- `scripts/cifras_lectura_S1bis.py`: valida las planillas y da la cifra del piso (Wilson inferior al 95 % sobre las 90, con las
  dudosas de las dos maneras), por modo, la del corpus ponderada con su tamaño efectivo, ri_spi, los juicios, la limpieza, la
  tanda 0 aparte, los límites declarados que caen en la muestra (las 13 de corte, las 4 de tamaño o herencia, `ri2_ae` y las 21
  intros), el censo del 1.16 con su cifra aparte y los candidatos del 1.16 en la muestra. Controla que las 21 intros estén en la
  salida (21 de 21).
- `scripts/lista_para_la_autora_S1bis.py`: errores y dudosas; juicios dudosos; 20 correctas con
  `U-SEG-OFICIAL:cortes:S1-bis:revision` sobre las correctas del primer grupo y de ri_spi; del 1.16, marcados y dudosos y 5
  correctos con `U-SEG-OFICIAL:1_16:S1-bis:revision`.
- `scripts/prueba_cifras_S1bis.py`, con datos sintéticos (no toca la muestra): con 90 leídas, 0, 3 y 4 errores de corte dan
  0,9591, 0,9065 y 0,8912 (pasa con 3, no con 4, como la nota de `2faff14`); las dudosas de las dos maneras, la limpieza, un
  límite en la muestra, `ri2_ae` sin contar, el 1.16 y la lista, reproducibles; una marca mal escrita invalida la planilla.
  Salida: `prueba_cifras_S1bis_b.txt`.

## 6. Quién lee y qué queda pendiente

- La sesión que revise este freno (la mesa) lee la muestra entera y el censo del 1.16 con las fichas y llena las planillas; la
  autora revisa la lista; las divergencias las adjudica la autora.
- Pendiente para después de la lectura: con `ri2_ae::3.3` o `5.3` en la muestra, cuál de las dos cifras del piso vale.
- Fuera de esta lectura, registrados en el acta: la vía de ri2_pm, `3.5.3` y `1.6`, a una lectura propia antes de la release
  que lo incluya; ri_tii, candidato a una regla por lista; la reclasificación de ri_spi, con su lectura.
