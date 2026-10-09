# U-SEG-OFICIAL — S1-bis-b: acta del sorteo de la lectura de cortes

Escrita el 08/10/2026 antes del sorteo. Su sha256 y su hora quedan en `sellos_S1bis_b.txt`; lo que se agregue después del
sorteo va al final, como nota fechada, sin editar lo de arriba.

Fuentes: el mandato FIRMADO en `e543cb2` (texto firmado `44cf30ca…`) con sus notas al pie: el criterio, la muestra y el
piso de la lectura de cortes (`2faff14`), las precisiones de `26c6502`, las semillas de S1-bis (`a757b32`) y la revisión
del FRENO S1-bis-a por la mesa (`2abb346`). La población es la de `poblacion_muestra_S1bis.json` (`ded01f23…`, tramo a),
con el sha256 de la lista de ids de cada estrato.

## 1. Decisiones de la autora sobre el FRENO S1-bis-a (08/10/2026), registradas a las 17:30

1. **ri_spi, opción (b): sigue no segmentable.** Se leen 10 de sus 93 unidades aparte, con el criterio del primer grupo y
   fuera del piso. Con esa lectura se decide si se reclasifica para las tandas siguientes. Sorteo:
   `random.Random("U-SEG-OFICIAL:cortes:S1-bis:ri_spi").sample(sorted(ids), 10)`, la forma de S1 (`{semilla}:ri_spi`) con la
   semilla de S1-bis.
2. **ri_pspii, opción (a): el juicio es correcto.** e0-r2 reconoce sus dos apartados numerados; la clase no segmentable
   descansa en lo corto del documento. **ri_tii, opción (b): límite declarado.** Los apartados en romanos (I a VI) no son
   numeración de puntos y el documento sigue por página (U-COB-A). Queda como **candidato a una regla por lista en la release
   de E0 antes de la tanda en la que caiga**. Los dos entran al tercer grupo con ese resultado y no se vuelven a juzgar: se
   leen los otros 9 juicios.
3. **ri2_pm, opción (c): sale entero de esta lectura**, con `3.5.3` y `1.6`, porque está en el bloque B (release posterior) y
   no entra en el grafo evaluado. El segundo grupo queda vacío. Su vía y esos dos casos quedan pendientes de una lectura
   propia antes de la release que lo incluya. El manifiesto de S1-bis-a no cambia: la vía por punto de ri2_pm queda en él
   como registro de S1-bis-a, pendiente. **ri_tar, opción (a):** el renglón 10 de la p. 1 («…vigente al cierre de las
   operaciones del último día hábil del mes bajo informe») es la regla de conversión al tipo de cambio, no una marca de
   vigencia; ri_tar sigue vigente en el manifiesto.

## 2. Las 21 unidades `::intro` de la tanda 0 fuera de 4a y 4b: regla decidida antes de leer, registrada a las 17:30

Son los puntos de la tanda 0 que quedaron fuera de las reglas 4a y 4b (límite declarado de S0-4b) que están en los 152:
los casos de `s0_4/censos/censo_4ab_sobre_S0-3.json`, clave `tanda0_limite_declarado`, de los TOs de la tanda 0 que son de la
partición (ctacte 14, pagjub 3, lingob 2 y polcre 2; docvig ninguno), cada uno en su unidad `<to>::<unidad>::intro`, todas
en el estrato vigente.
- Si cae alguna en la muestra, se lee con el mismo criterio que las demás y cuenta según el criterio: **si es un error de
  corte, es error para el piso.**
- En el reporte se marca aparte, como límite declarado de la tanda 0.
- No se informa si cayó alguna hasta después de la lectura.

## 3. Cómo se sortea

- **Primer grupo:** por estrato, con el rótulo literal de `modo_lectura` de `conteos_b584.json` (vigente, marcadores,
  sin_raiz), `ids` = la lista ordenada de la población (se controla su sha256 contra `poblacion_muestra_S1bis.json`) y
  `random.Random(f"U-SEG-OFICIAL:cortes:S1-bis:{estrato}").sample(ids, n)`, con n = 40, 10 y 40.
- **Segundo grupo:** vacío (decisión 3).
- **Tercer grupo:** los 11 juicios, uno por no segmentable salvo ri_spi: 9 para leer, y ri_pspii y ri_tii con el resultado
  de la decisión 2.
- **ri_spi:** 10 unidades (decisión 1).
- **Censo del hallazgo 1.16 de la tanda 1:** los 35 candidatos (`comparacion_censos_S1bis.json`, `hallazgo_1_16.tanda1.ids_s1bis`),
  todos, sin sorteo, leídos con el mismo criterio de cortes, con cifra aparte del piso. Un candidato que también salga en la
  muestra se lee en los dos y cuenta en los dos.

## 4. Lectura a ciegas

La muestra sellada y las fichas de lectura llevan, de cada unidad, su id, su TO, su grupo, sus páginas, su tipo, su
herencia y su texto propio, y las páginas renderizadas. **No llevan ninguna marca de límite declarado** (las 13 de corte
del FRENO S0-4b, las 4 de tamaño o de herencia, `ri2_ae::3.3` y `5.3`, las 21 intros de la tanda 0), ni de TO de la tanda
0, ni de candidato del hallazgo 1.16 en la muestra. Esas marcas las calcula `scripts/cifras_lectura_S1bis.py` después de la
lectura, desde sus listas de origen.

## 5. Después de la lectura (fijado antes del sorteo)

- **Marcas**, en las planillas del paquete del freno, con el vocabulario de S1: marca `correcta`, `error` o `dudosa`; de un
  error, su clase (`corte` o `limpieza`) y su subclase (corte: `empieza_fuera`, `termina_fuera`, `falta_texto_propio`,
  `trae_texto_de_otro_punto`, `numero_equivocado`; limpieza: `restos_encabezado`, `restos_pie`).
- **Lista para la autora** (`scripts/lista_para_la_autora_S1bis.py`): los errores y las dudosas del primer grupo y de ri_spi;
  los juicios dudosos de los 9; 20 correctas, `random.Random("U-SEG-OFICIAL:cortes:S1-bis:revision").sample(sorted(c), 20)`,
  con `c` = las unidades correctas del primer grupo y de ri_spi; del 1.16, los marcados y los dudosos y 5 correctos,
  `random.Random("U-SEG-OFICIAL:1_16:S1-bis:revision").sample(sorted(c116), 5)`, con `c116` = los candidatos correctos.
- **Cifras** (`scripts/cifras_lectura_S1bis.py`), las de la nota de `2faff14`: la del piso, el límite inferior de Wilson al
  95 % sobre las 90 sin ponderar (pasa con 3 errores de corte o menos), con las dudosas como correctas y como error; por modo
  de lectura, como fracción; la del corpus, ponderada por los pesos de la población, con el intervalo de Wilson y el tamaño
  efectivo 1 / Σ(peso² / leídas), declarada como aproximación; ri_spi, aparte; los juicios; los errores de limpieza por grupo;
  las unidades con error de un TO de la tanda 0, aparte; los límites declarados que caigan en la muestra, con su lista; el
  censo del 1.16, con su cifra aparte del piso; y los candidatos del 1.16 que caigan en la muestra.
- **`ri2_ae::3.3` y `ri2_ae::5.3`:** el despacho los da como límite conocido si salen. Si sale alguno, la cifra del piso se da
  contándolo según el criterio y, aparte, sin contarlo; cuál vale lo decide la autora.

## Nota del 08/10/2026, después del sorteo (el texto de arriba, sellado a las 17:30:31, da `fdf6704f…`)

- Sorteo hecho a las 17:31:16 con `scripts/muestra_cortes_S1bis.py`, como fija el §3: `muestra_cortes_S1bis.json`, sha256
  `33b24c0b95ea821acb98f01a0155cae9fc52e70d004661fe7bd2f7f184f499e2` (`sellos_S1bis_b.txt`). La población de los tres estratos y la
  de ri_spi se controlaron contra `poblacion_muestra_S1bis.json` (lista y sha256): iguales. Repetido en otro archivo: igual byte
  a byte.
- 90 unidades del primer grupo (40, 10 y 40), 10 de ri_spi, los 11 juicios (9 para leer) y los 35 candidatos del 1.16; el
  segundo grupo, vacío. 301 páginas renderizadas, en el paquete del FRENO S1-bis-b.
- Las cifras y la lista para la autora quedan fijadas en `scripts/cifras_lectura_S1bis.py` y
  `scripts/lista_para_la_autora_S1bis.py`, probadas con datos sintéticos (`scripts/prueba_cifras_S1bis.py`: con 90 leídas, 0, 3 y
  4 errores de corte dan 0,9591, 0,9065 y 0,8912 de límite inferior). Las 21 intros de la tanda 0 están en la salida de E0 (21
  de 21); si alguna cayó en la muestra no se calculó: lo dice `cifras_lectura_S1bis.py` después de la lectura.

## Nota del 08/10/2026, 18:12, después del sorteo y antes de la lectura: decisión de la autora sobre `ri2_ae::3.3` y `ri2_ae::5.3`

Registrada por la mesa, con lo que decidió la autora antes de leer. Si en la muestra sale `ri2_ae::3.3` o `ri2_ae::5.3`, vale la
misma regla que para las 21 intros de la tanda 0 (§2):
- se lee con el mismo criterio que las demás;
- si es un error de corte, cuenta para el piso: la cifra que vale es la del piso contándolo según el criterio;
- la otra cifra, sin contarlo, va aparte en el reporte.

Esto resuelve lo que el §5 dejaba a la autora. El texto de arriba no cambia; el sellado sigue dando `fdf6704f…`.
