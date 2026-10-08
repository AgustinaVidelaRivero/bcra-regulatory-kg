# FRENO U2-b — U-UNION-ESTRECHA, segunda lectura a ciegas de la mesa

08/10/2026, sesión `839a4403`. USD 0, sin API. Nada commiteado. Escrituras en el repo: los cuatro archivos nuevos de
`data/experiment/union_estrecha/u2/`; todo lo demás, en el scratchpad.

## 1. Lectura sellada antes de comparar

- Fichas y criterio controlados contra `sello_fichas_u2.txt` (10:54:03): `criterio_u2.md` `86c7724c…`,
  `fichas_u2.json` `888d0b76…`, `fichas_u2.md` `7ab2812e…`. Coinciden los tres.
- Mandato: texto firmado por `git show 21e55a0:docs/mandatos/UUNION_ITEM_ENCABEZADO_regla_estrecha.md` (`6959ca49…`) y,
  de las notas al pie, solo la primera (líneas 84 a 125 del archivo actual). Ubiqué sus límites por número de línea, sin
  imprimir contenido; la nota siguiente empieza en la línea 126 y no la leí.
- `lectura2_u2.json` (`7d7cda3a…`) quedó sellada en `sello_lectura2_u2.txt` (`13992d04…`) a las 14:25:18. Abrí
  `lectura1_u2.json` a las 14:25:30: su sha256 es `8b23d250…`, el de su sello (10:58:04).
- Antes del sello no abrí nada de la lista vedada, ni `fichas_u2.py` ni `comandos_u2a.sh` (código de U2-a), ni
  `regla_u1.md`, ni ninguna memoria del proyecto. El índice de memoria se carga solo al iniciar la sesión; su línea de
  U2-a dice «fichas 10:54:03, lectura 8b23d250 sellada; sin cifra, no abrir» y no trae veredictos.

## 2. Acuerdo

- Coinciden 29 de 29 (`divergencias_u2.json`, campo `acuerdo`).
- Kappa de Cohen: no definido. Las dos lecturas usan una sola categoría, la misma, en las 29 fichas. Entonces el acuerdo
  esperado por azar es 1 y kappa queda 0/0. Esta explicación ya deja inferir la distribución. Aun así, no escribo la
  cifra de correctas ni si pasa el piso: eso va en el FRENO U2, después de la adjudicación.
- Divergencias: ninguna. La hoja (`divergencias_u2.md` y `.json`) lleva igual dos fichas con el campo vacío «Veredicto
  de la autora: ______»: U28 y U29. Las dos lecturas declaran en la nota que el tramo de la Condicion no está en el texto
  propio del ítem (10.4.2.9 y 10.4.2.5), sino en la intro de 10.4.2 que hereda la unidad. Es decir, la Condicion es la
  cláusula que subordina la lista y no el contenido del ítem. Las dos aplicaron el criterio tal cual (precisiones 1, 5 y
  6). El despacho deja ese caso a la autora. Lo que hay que decidir es si «la Condicion del ítem» se juzga por su tramo,
  como hicieron las dos lecturas, o por el contenido del ítem.
- Hay dos notas coincidentes más, sin campo para la autora. U24: el tramo del destino es el encabezado heredado de 5.8.2.
  U25: la Condicion es solo el inciso final de 2.7.3, «considerando los límites…», y la leí con el cierre de 2.7; en mi
  nota declaro también la otra lectura posible.

## 3. Controles

- sha256 del repo (todo, menos `.git`, `.venv` y `.venv-app`). Antes: 19.795 archivos, 14:10:12, HEAD `1f9b262`.
  Después: 19.802 archivos, 14:28:50, HEAD `18d9e05`. Las diferencias están en `diff_sha_repo_U2b.tsv` (20 filas):
  - 4 archivos nuevos de esta sesión: los cuatro autorizados de `u2/`;
  - 15 de tres commits de la autora que entraron durante la sesión (13 cambiados y 2 nuevos): `293fe8d` (14:22:28),
    `33c43e9` (14:23:31) y `18d9e05` (14:26:38);
  - 1 archivo nuevo ajeno: `docs/tesis/.DS_Store`, metadato del Finder creado a las 14:21:54.

  `tabla_reprocesamiento.md` se sigue editando fuera de esta sesión (mtime 14:28:58). Los 22 archivos que había antes en
  `union_estrecha/` no cambiaron (ahora son 26).
- `.pyc`: 2.213 antes y después, sin contar `.git` ni `.venv`. Corrí Python siempre con `-I -B`.
- Reproducción sobre copias en el scratchpad, sin enlaces. `armar_lectura2_U2b.py` reproduce `lectura2_u2.json` igual
  byte a byte que la sellada. `comparar_lecturas_U2b.py` reproduce los dos archivos de la hoja igual byte a byte.
- Tramos: el script controla que los 29 tramos y los 8 `tramo_2` sean literales de su ficha, con espacios y comillas
  normalizados. Dónde se ubica cada tramo de nodo está en `ubicacion_tramos_U2b.txt`.
- Grep de convenciones: vacío (`grep_convenciones_U2b.txt`).

## 4. Pasos declarados y error propio

- Después del sello, les agregué el sufijo `_U2b` a los tres scripts del scratchpad. `armar_lectura2_U2b.py` conserva el
  sha256 que cita el sello (`0f93e41b…`). Regeneré la hoja, que no estaba sellada, para que su comando nombre el script
  con ese sufijo.
- Error propio: en el primer control posterior conté los `.pyc` sin `.venv-app` y me dio 243. La definición del
  principio solo excluye `.git` y `.venv`. Con esa misma definición da 2.213. Causa: usé un filtro distinto entre el
  control de antes y el de después. Lo corregí antes de este FRENO.

## 5. Pendiente (acciones de la autora, ninguna hecha)

La adjudicación sobre la hoja (U28 y U29), el FRENO U2 con la cifra (correctas de 29, Wilson, pasa o no pasa) y el commit
de `u2/`.
