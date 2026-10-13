# U-SEG-OFICIAL — FRENO de S1-quater, fichas, tramo 2 (13/10/2026)

El tramo 2, después del seguí de la mesa (hoja de ruta de la mesa, §87): completé lo que faltaba del paso 4 y el paso 5. Todo dio lo
que fija el seguí, sin ninguna condición de freno. USD 0, sin API. Todo con el `python` del `.venv` del repo, también las tareas
auxiliares. Ningún id ni texto de unidades en `s1quater/fichas/`. **Nada commiteado, ningún mensaje de commit preparado, nada escrito
en la memoria.** El FRENO del primer tramo (`FRENO_S1quater_fichas.md`) no cambió. El detalle está en la sección «Tramo 2, después
del seguí» del REPORTE.

## Lo hecho

| punto del seguí | qué dio | hora |
|---|---|---|
| 1. la carpeta, igual a su sello | `etapa_1/manifest.txt` `110565d7…` y `etapa_2/manifest.txt` `37580fbc…`, los del sello de las fichas; la carpeta seguía en el scratchpad. El registro y las planillas, controlados solo por sha256, dan los del sello | 13:12:27 |
| 2. `verificar_carpeta_lectora_S1ter.py` | rc 0; «96 de 96» y «105 de 105», nada sin listar, nada en la raíz | 13:12:42 |
| 2. comandos del paso 1 de la lectora | etapa 1: 96 OK y 0 no OK; etapa 2: 105 OK y 0 no OK | 13:12:42 |
| 3. el tar, rehecho | `86275bfd…`, el mismo sha256 que el de resguardo; 205 entradas | 13:13:09 |
| 3. el tar, extraído en una carpeta nueva | `verificar` igual byte a byte que sobre la carpeta; `diff -rq`, 0 renglones | 13:13:09 |
| 4. sello de los controles a ciegas | `sello_controles_ciegos_S1quater.txt`, con 7 archivos | 13:13:31 |

- **El control a ciegas no lo volví a correr.** Vale su salida de las 10:52:29 (`6a41c24c…`).
- **El sello de las fichas no lo toqué.** El sha256 del tar está en el sello de los controles a ciegas.

## Sello de los controles a ciegas (13:13:31)

| archivo | dónde | sha256 | hora de la salida |
|---|---|---|---|
| `NO_ABRIR_control_ciego_fichas_S1quater_completo.txt` | paquete | `6a41c24c55147d912dd6d79f4287e6e69e253a6eaf29b70a0a37e9506b93857d` | 10:52:29 |
| `controles/control_ciego_fichas_S1quater_cuentas.txt` | repo | `9ce27b048d0dbc1ca57ff74c69b6e5c8138c3f15b3629973d12c838acb3936bc` | 10:52:29 |
| `controles/verificar_carpeta_lectora_S1quater.txt` | repo | `a6f2b61e15afa4700ac13a88ef6b2ee13fb1d0f244fa94689bef64c8db5860f4` | 13:12:42 |
| `controles/paso1_lectora_S1quater_cuentas.txt` | repo | `4c3ad99fb395305407106f25b504007887fd95f4d9add44b3855aa0d61a90bd8` | 13:12:42 |
| `NO_ABRIR_paso1_lectora_S1quater_completo.txt` | paquete | `e1c105a68c0015bc864bdabe841e0a4fae8dc44f183d191fde32c8db165505e9` | 13:12:42 |
| `controles/verificar_carpeta_lectora_S1quater_tar.txt` | repo | `a6f2b61e15afa4700ac13a88ef6b2ee13fb1d0f244fa94689bef64c8db5860f4` | 13:13:09 |
| `NO_ABRIR_carpeta_lectora_S1quater.tar` | paquete | `86275bfd2c7f4c90351ce141bc59d9f681013fd1e94b09b18e0c9bceef435f82` | 13:13:09 |

Todas las horas son del 13/10/2026, -0300.

## Lo que declaro

- **El renglón del primer tramo:**
  - **dónde está:** en la etapa 1, en el rótulo del número que la segmentación le asignó a una ficha;
  - **qué lo marcó:** el término `1\.16`. Cae en el número, que viene de la E0, y no en la parte fija del rótulo. Según la E0, `1.16`
    está también en el texto propio y en la herencia de la unidad;
  - **qué se decidió:** falsa alarma, por la regla de la autora fijada antes del diagnóstico (§87). La mesa lo diagnosticó por script;
  - **lo que no verifiqué:** **el diagnóstico es de la mesa, NO VERIFICADO en esta sesión**, porque verificarlo exige leer el renglón
    o la ficha;
  - **nadie lo miró:** yo no lo miré ni lo busqué.
- **Los tres scripts del diseño que necesitó la prueba** (`sorteo_S1quater.py`, `poblaciones_S1quater.py` y `regresion_S1quater.py`):
  los copié de HEAD y dan los sha256 de `sello_diseno_S1quater.txt`. El despacho no los nombraba: la omisión es del despacho.
- **El `python3` del sistema** (3.12.13): lo usé en el primer tramo para cuatro tareas auxiliares fuera del repo. En este tramo, solo
  el del `.venv`.
- **El registro y las planillas vacías:** los trato como `NO_ABRIR_`, sin cambiarles el nombre. En este tramo solo los controlé por
  sha256.
- **El `sleep 60` del primer tramo:**
  - **qué pasó:** para esperar la E0 escribí un `sleep 60` seguido de un `cat`. Fue un error. La herramienta de la sesión lo bloqueó
    antes de correrlo: no hubo espera;
  - **contra el seguí:** el seguí lo describe como una espera activa. Fue un intento que no corrió;
  - **en este tramo:** ninguna espera.

## Repo, `.pyc` y convenciones

- **Foto sha256 del repo entero (sin `.git`),** con el mismo método:
  - **antes del tramo:** de 13:11:25 a 13:11:48, 50.073 archivos, igual a la foto final del primer tramo;
  - **después:** de 13:14:50 a 13:15:13, 50.077 archivos.
  - **La comparación** (`controles/comparar_fotos_S1quater_fichas_tramo_2.json`):
    - en `s1quater/fichas/`: 4 archivos nuevos (el sello de los controles a ciegas y tres salidas de `controles/`) y 1 cambiado, el
      REPORTE, con su sección nueva al final;
    - **fuera de esa carpeta:** 0 nuevos, 0 cambiados y 0 borrados.
  - **Lo que entró después de la foto:** este FRENO y la salida del grep. La comparación final va en el mensaje del FRENO.
- **`.pyc`:** 10.158 en todo el repo y 2.213 fuera de `.venv/`, antes y después.
- **Grep de convenciones** (`s0_4/scripts/grep_convenciones.py`, sobre los archivos de `s1quater/fichas/` sin contar las salidas del
  grep): en `controles/grep_convenciones_S1quater_fichas_tramo_2.txt` y en el mensaje del FRENO.

## Paquete

- **Lo nuevo:** `revision_USEG_OFICIAL_FRENO_S1quater_fichas/` suma la lista entera del paso 1 de la lectora, las fotos de este tramo
  y la copia actualizada de `s1quater/fichas/`.
- **Lo que cambia:** el tar rehecho reemplaza al de resguardo, con el mismo sha256.
- **Archivos con texto o ids,** escritos por `tar` y por los comandos, sin abrirlos:
  - `NO_ABRIR_carpeta_lectora_S1quater.tar`;
  - `NO_ABRIR_control_ciego_fichas_S1quater_completo.txt`;
  - `NO_ABRIR_paso1_lectora_S1quater_completo.txt`;
  - el registro y las dos planillas, que trato como `NO_ABRIR_`.
- **La copia permanente:** su ruta y su verificación van en el mensaje del FRENO.

FRENO.
