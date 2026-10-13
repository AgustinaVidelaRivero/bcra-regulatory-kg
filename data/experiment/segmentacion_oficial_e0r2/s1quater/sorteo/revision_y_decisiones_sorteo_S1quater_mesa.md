# U-SEG-OFICIAL, sorteo de S1-quater: revisión de la mesa, decisiones de la autora y tres aclaraciones (13/10/2026)

USD 0, sin API.
- **Qué es:** una nota de la mesa revisora que entra con el registro del sorteo, por pedido de la autora (hoja de ruta de la mesa, §86).
- **Lo que no cambia:** ningún archivo de la ejecutora en `s1quater/sorteo/`.
- **Ids de unidades:** no lleva ninguno. Las fichas que nombra son del orden de S1-ter.

## 1. Decisiones de la autora del 13/10/2026 (§86), tal cual

- a. «La muestra y el orden quedan fuera del repo hasta que cierre mi adjudicación, no solo la lectura. En el repo quedan sus sha256 y
  la hora del sello (sello_sorteo_S1quater.txt). Se declara que en S1-ter el orden sí entró al repo.»
- b. «Los dos despachos sellados de la lectora no se tocan: siguen pidiendo pegar el paso 0 tal cual. La mesa reemplaza la carpeta
  personal por $HOME al registrar sus FRENOs, y lo declara.»
- **Lo que declaro por la decisión a:**
  - en S1-ter el orden de lectura entró al repo (`s1ter/tramo_b/orden_lectura_S1ter.json`);
  - en S1-quater, la muestra y el orden quedan en el paquete de la ejecutora del sorteo, fuera del repo, con su sha256 y su hora en
    `sello_sorteo_S1quater.txt`;
  - las poblaciones y la regresión, también con ids, quedan igual, con sus sellos.

## 2. La revisión del sorteo

- **El paquete de la ejecutora:** 32 de 32 archivos iguales a su `manifest.txt`. Sus copias de los 15 archivos de `s1quater/sorteo/`
  son iguales a las del repo.
- **Lo que no se abrió:** los cuatro `NO_ABRIR_`. La mesa los leyó solo por script, para comparar.
- **La reproducción, sobre copias:**
  - **la E0 de `2374968a`:** 768 de 768 archivos con el sha256 del manifiesto de S0-6b, 10.478 unidades;
  - **las poblaciones, la regresión, la muestra y el orden:** iguales clave por clave a los de la ejecutora, sin la hora del sello;
  - **el sorteo corrido sobre las poblaciones y la regresión de la mesa:** da la misma muestra y el mismo orden.
- **El registro de la sesión de la ejecutora** (desde el despacho; 71 llamadas a herramientas, ninguna en subagentes):
  - **carpetas vedadas:** ninguna mención;
  - **el paquete de la mesa:** solo los seis archivos del despacho, controlados con `shasum -a 256 -c` y pasados como argumentos;
  - **escrituras:** en el repo, solo en `s1quater/sorteo/`. Nada en `.claude/` ni en la memoria;
  - **esperas programadas:** ninguna. Una corrida en segundo plano;
  - **archivos `NO_ABRIR_`:** ninguno abierto. Las salidas de los scripts pasaron por un filtro que reemplaza las cadenas con forma de
    id;
  - **ids en las salidas:** 4 cadenas con forma de id, ninguna de una unidad.
- **Las unidades vistas en la sesión, con el criterio de la adenda 4:** ninguna, ni antes del sorteo ni después.
  - La medición de siempre, sobre las entradas y salidas de las herramientas, no ve ninguna.
  - La misma medición sobre todo el texto de la sesión (mensajes, texto del modelo y adjuntos) tampoco.
  - No hace falta una adenda 5, y el sorteo no se repite.

## 3. Tres aclaraciones

### a. Las fotos del repo

- **La diferencia es de método, no del repo.** La foto de la mesa del cierre del §85 (09:40, 50.387 archivos;
  `snapshot_repo_completo.py`) y la de la ejecutora antes de escribir (09:48, 50.045; `find . -type f` con `shasum`) difieren en dos
  cosas.
- **Los enlaces simbólicos:** las 342 rutas que solo están en la de la mesa son enlaces a archivos. `find -type f` no los lista. Son:
  - 336 de `data/experiment/ev2_corrida/navegabilidad/`;
  - 3 de `.venv-app/bin/`;
  - 3 de `.venv/bin/`.
- **Las bases de datos:** la foto de la mesa registra 305 archivos `.db`, `.db-wal` y `.db-shm` por tamaño y fecha, no por sha256. Por
  eso su valor difiere del de la ejecutora.
- **Lo demás:** las otras 49.740 rutas dan el mismo sha256 en las dos fotos.
- **Fuera de `s1quater/sorteo/`, nada cambió:**
  - en las fotos de la ejecutora, de antes a la final, hay 15 archivos nuevos, todos en `s1quater/sorteo/`, sin borrados ni cambios;
  - en las de la mesa, del cierre del §85 a las 10:12, lo mismo.
- **Un límite de la medición:** las fotos son listas de rutas, y algunos nombres de archivo del repo coinciden con texto de unidades.
  - Las coincidencias están en los nombres de los PDF de `data/raw/01_textos_ordenados/actuales/` y de la caché de chunks de un run
    viejo.
  - Ninguna sesión las mostró: la medición de las sesiones no las encuentra. Se declara.

### b. Los errores de la regresión: 41 contra 40

- **S1-ter cerró con 40 errores confirmados, contados por pregunta** (las 40 filas):
  - 13 de la unidad (12 de corte y 1 de limpieza);
  - 4 de la unidad que sigue (de corte);
  - 23 de herencia.
  - Por clase: 16 de corte (12 + 4), 1 de limpieza y 23 de herencia.
- **La regresión los cuenta por origen, con la regla del diseño** (`diseno_S1quater.md`, §6; `regresion_S1quater.py`): la marca
  `error` de la planilla adjudicada, los cierres confirmados y las herencias confirmadas. Da 41: 14 por marca, 4 por la que sigue y
  23 por herencia.
- **La diferencia es una sola ficha: la E2-033 del orden de S1-ter.**
  - Su error confirmado es uno, de corte, en la unidad que sigue.
  - La planilla adjudicada de la etapa 2 lo lleva también como marca `error` de la ficha, con la misma clase y subclase.
  - El registro de la adjudicación lo lleva como cierre confirmado.
  - La regresión lo cuenta dos veces: por la marca suma las unidades calificadas de la ficha, y por el cierre, la unidad que sigue.
  - Así, 14 = 13 + 1 por marca, y 41 = 40 + 1.
- **El efecto:**
  - entran 1 unidad vieja de más, sin error propio confirmado (de las 44), y 1 unidad nueva (de las 60);
  - la lista queda como está, sellada. La regresión no entra en la cifra;
  - cuando se informe la regresión (diseño, §6), ese error se cuenta una vez: 40 errores.

### c. La semilla del sorteo

- **La muestra:** `random.Random("U-SEG-OFICIAL:cortes:S1-quater:{estrato}").sample(sorted(ids), n)`.
  - La cadena base, `U-SEG-OFICIAL:cortes:S1-quater`, la selló la nota de la mesa del 10/10/2026 al mandato de S0-5a
    (`docs/mandatos/USEG_OFICIAL_S0-5a_reglas_de_corte_E0.md`, renglones 528 y 529; commit `521e220a`, 10/10/2026 07:50:46 -0300).
  - La misma nota selló la cadena `:revision`, que queda sin uso.
- **El orden y la forma:**
  - el sufijo por estrato es la forma de S1-ter (`s1ter/scripts/sorteo_S1ter.py`);
  - la cadena del orden, `U-SEG-OFICIAL:cortes:S1-quater:orden`, la selló el diseño (`diseno_S1quater.md`, §4);
  - el diseño también selló `sorteo_S1quater.py` (commit `3a52987f`, 11/10/2026 10:02:33 -0300).
- **Todo quedó fijado antes de que se conociera la población:**
  - la primera E0 corregida es la de S0-6a, corrida el 12/10/2026 desde las 14:13:54 (`s0_6/manifiestos/manifest_salida_e0_152_S0-6a.json`);
  - la población del sorteo depende de la E0 de `2374968a` y de las adendas 1 a 4, del 12 y el 13/10/2026.
- **Nadie corrió el sorteo antes que la ejecutora:**
  - el diseño lo probó solo con una población inventada (`prueba_S1quater.py`);
  - la mesa, en el §85, también, con ids inventados;
  - de las transcripciones de las sesiones abiertas en el repo, solo la de la ejecutora corre el sorteo sobre una población real.
    En otra sesión el nombre del script aparece dos veces, en resultados de listados de archivos.

## 4. Declaraciones

- **El commit del código de E0:** el JSON de las poblaciones dice «PENDIENTE (lo fija el commit de la autora)» en
  `commit_codigo_e0_corregida`, copiado del manifiesto de S0-6b. El commit es `2374968a`, como declara el FRENO.
- **Los FRENOs de la lectora:** por la decisión b, cuando entren al repo, la mesa reemplaza la carpeta personal por `$HOME` y lo
  declara en el registro.
