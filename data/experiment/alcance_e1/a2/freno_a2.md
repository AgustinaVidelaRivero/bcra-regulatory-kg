# FRENO A2 (final) — U-ALCANCE-E1: el registro de alcance por tanda en el mensaje de E1

15/10/2026, HEAD `29f0b713`. Mandato FIRMADO (`docs/mandatos/UALCANCE_E1_cableado_registro_alcance.md`): el texto firmado lo leí en
el commit de la firma, `21e55a07` (sha256 `617a4d2463a9…`), y las notas del 08/10/2026, en HEAD. USD 0, sin API. Nada commiteado,
ningún mensaje de commit preparado, nada escrito en la memoria, sin esperas programadas ni `sleep`. Todo corrió sobre copias sin
enlaces; el repo recibió las escrituras al final, iguales byte a byte a la copia probada, y una reproducción desde cero dio todo igual.

## Paso 0 (carpeta personal reemplazada por `$HOME`)
- `pwd`: `$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg`; rama `main`; `git status --porcelain --untracked-files=no`: vacío.
- `git log --format=%s -6`: el 81 («Registro de decisiones: el alcance por seccion para la primera tanda, el piso de espacio y lo
  abierto del re-sellado»), el 80 («… las notas del re-sellado unico …»), el 79 («… segundo commit del sello») y el 78 («… primer
  commit del sello»), y después `f4b07889` y `96d7d1ab`.

## Qué quedó en el repo (sin commit)
Siete archivos rastreados cambian y dos son nuevos (`git status`; sha256 en `salidas/sha256_escrituras_repo_a2.txt`, iguales a
los de la copia probada):
1. **El parche de A1**, aplicado una sola vez. Controles repetidos sobre mi copia: `git log 7788e52..HEAD -- <archivo>` vacío para
   `prompt_r2b.py`, `candado_mensaje_r2b.json`, `selftest_prompt_r2b.py` y `perfil_e1.py`; `git apply --check` rc 0
   (`salidas/control_parche_A1_sobre_HEAD_a2.txt`).
2. **El derivado** (`catalogo_unico/registro_alcance_r2b.json`), regenerado con `--tandas 1` desde el registro final (`06b8267a3004…`):
   10 entradas, las 9 de A1 byte a byte y ri_mmsef (rol reutilizado, `Sujeto_rol_entidad_comprendida_reginf`); el diff contra el de
   A1 son 10 renglones agregados y 0 quitados. Sin entrada: ri_oc, ceninf y cirmo3 (sin alcance declarado) y ri_cc (tanda 3).
3. **`prompt_r2b.py`**: el sha del derivado y el comentario de A2. En los renglones 1 a 463 cambian solo 95, 97, 98 y 409, como en
   A1, y ninguna de las anclas que la tabla ya tenía a este archivo pasa del 456.
4. **`perfil_e1.py:236`**, una línea: `rol_por_to` da a cada documento la entrada de `alcance_del_documento`, la tabla de la release
   primero y después el derivado (81 entradas: 71 y 10).
5. **`selftest_prompt_r2b.py`**: ri_mmsef en las ramas (10 del derivado, 5 de rol reutilizado) y un caso nuevo del perfil.
6. **`selftest_clave_cache.py`**: la variación R34 (una entrada del derivado para docvig, en memoria); su JSON, regenerado.
7. **`tabla_reprocesamiento.md`**: F13c en la variante A (principio 9, R34) y los pasajes viejos (renglones abajo).
Más esta carpeta, `data/experiment/alcance_e1/a2/` (este FRENO, `scripts/` y `salidas/`).

## PROPUESTOS (los confirma la autora)
- `REGISTRO_ALCANCE_R2B_SHA256_ESPERADO` = `e06933e77a1ae819229d5f2a4b5886f71f6129c809032e1e557932fb8cb69ff4`.
- `CANDADO_MENSAJE_JSON_SHA256_ESPERADO` = `6b758517cee0f2e36c26c54f0f6738b3d49d11d0cf3141c26cff166ce6820325`.
- `MENSAJE_R2B_SHA256_ESPERADO` = `eeb11b9a3bf699d5535fcf2bbe79541ba746ae7bdae3341af962840990a97362`.
Los dos del candado son los de A1: la fixture (17 unidades) y las tres entradas del derivado que usa no cambiaron. Dos procesos dan
lo mismo y el módulo importa sin frenar (`salidas/sellos_candado_a2.json`, `verificacion_sellos_candado_a2.json`); las 13 de P3c-2
siguen en `a9cb702c0d24…`.

## Criterios de aceptación (`scripts/bateria_a2.sh`, consola en `salidas/bateria_a2.txt`)
- **Tanda 0, igual:** por el camino del runner (`runner_corpus.configurar` → `perfil_e1.perfil("r2b")`), 2.439 unidades, 0 distintas;
  sha de los mensajes `48fdec197658…` con HEAD y con A2, el de R2-2.
- **Cambian solo los documentos con alcance en el registro:** en la lista final, 3.290 unidades; cambian 1.029, en los 10
  documentos del derivado y solo en la línea de alcance (el mensaje de A2 sin «línea + salto + salto» es el de HEAD).
- **`selftest_prompt_r2b`:** HEAD sobre HEAD 55/55; A2 67/67; el de A2 con el código de HEAD, 55 ok y 12 FAIL, exactamente los 12
  casos nuevos (11 de A1 y el del perfil; `salidas/control_negativo_selftest_prompt_r2b_a2.json`).
- **`selftest_clave_cache --salida-r2b`:** con HEAD, el JSON del repo byte a byte; con A2, OK en dos corridas iguales: 45
  variaciones (R00 a R34; la única nueva es R34, que cambia la clave de E1 de `docvig::3.3.1` y no la de E3), las otras 44 con los
  mismos tokens, A1r y A3r iguales, contraste OK en 45 filas. Comando de la cuenta: `python3 -I -c "import json;
  d=json.load(open('data/experiment/mantenimiento/selftest_clave_cache.json')); print(len(d['perfil_r2b']['variaciones']))"` → 45.
- **Derivado:** dos corridas iguales byte a byte, e iguales al archivo.
- **Foto sha256 del repo** antes y después de cada corrida (lote de la E0, batería, `selftest_catalogo_unico`, reproducción final):
  50.860 archivos, 0 cambiados en las tres primeras; 50.862 (con los dos nuevos) y 0 cambiados en la última. De la foto del inicio
  a la de antes de escribir: 0 cambiados. **2.213 `.pyc`** antes y después de la batería, de `selftest_catalogo_unico` y de la
  reproducción final; el lote no los cuenta aparte, y su foto, que incluye los `.pyc`, no cambia.
- **Vecinos sobre las dos copias, consolas iguales con HEAD y con A2:** `selftest_catalogo_unico` 60/60 (K2 pasa con el derivado
  fuera de `generados_r2/`), `selftest_reresolver_catalogo` 66/66, `selftest_cablev3` 45/45 y `selftest_manifiesto` 44/49 (los 5
  fallos de P5 que CLAUDE.md §4.l anticipa fuera de la raíz del repo).
- **Grep de convenciones:** `salidas/grep_convenciones_a2.txt`.

## Medición en seco sobre la lista final (`salidas/medicion_tanda1_a2.json`)
La E0 corregida, regenerada con `lote_tramo1_S2.sh` sobre mi copia: 768 de 768 iguales al manifiesto de S0-6b (`80adbd58…`; 152 TOs,
10.478 unidades). La lista que regenera es la commiteada salvo el sha del registro (`ce402aad…` → `06b8267a…`) y la fila de
ri_mmsef, que suma la decisión del renglón 85 (`salidas/comparacion_lista_tanda1_a2.json`). Tokens con la razón marginal de E1
(3,0598 caracteres por token, `data/experiment/e3_listas/o3/razon_tokens_e1.json`), a USD 1 por millón de entrada de
`claude-haiku-4-5` (`runner_corpus.py`, `P_E1`), una llamada por unidad:

| documento | unidades | caracteres por unidad | caracteres | tokens | USD |
|---|---|---|---|---|---|
| ri_ccna | 169 | 524 | 88.556 | 28.942 | 0,028942 |
| ri_rml | 46 | 559 | 25.714 | 8.404 | 0,008404 |
| ri_gerc | 15 | 559 | 8.385 | 2.740 | 0,002740 |
| ri_pgn | 21 | 559 | 11.739 | 3.837 | 0,003837 |
| snp_cheq | 265 | 614 | 162.710 | 53.177 | 0,053177 |
| snp_tr | 103 | 581 | 59.843 | 19.558 | 0,019558 |
| manori | 152 | 535 | 81.320 | 26.577 | 0,026577 |
| nmcief | 55 | 618 | 33.990 | 11.109 | 0,011109 |
| ri_dcpc | 75 | 535 | 40.125 | 13.114 | 0,013114 |
| ri_mmsef | 128 | 559 | 71.552 | 23.385 | 0,023385 |
| **total** | **1.029** | | **583.934** | **190.841** | **0,190841** |

Contra la tarifa de E1 de la tabla (USD 0,010135 por unidad, §5), es el 1,83 % del E1 de esas 1.029 unidades (USD 10,4288) y el
0,57 % del de la lista (3.290 unidades, USD 33,3441). Los reintentos de E1 (por corte, por forma y del ratchet) reenvían el mensaje y
suman lo suyo; no los estimo.

## Manifiestos de los 152 (`salidas/manifiestos_152_head.json` y `_a2.json`)
En S1 (`0957daf5…`) y en S1-bis (`98669cd6…`), **11 documentos** con alcance en el registro tienen `rol_alcance` null: los 10 de la
tanda 1 (manori, nmcief, ri_ccna, ri_dcpc, ri_gerc, ri_mmsef, ri_pgn, ri_rml, snp_cheq y snp_tr) y ri_cc (tanda 3). El desacuerdo
con el perfil de A2 es de **10** (ri_cc no está en el derivado); con el de HEAD, 0. Con el perfil de A2 no cargan
(`manifiesto_corpus.cargar` frena en el primero, manori); con el de HEAD, sí. Quedan como registro anterior a A2 (decisión 2 de la
nota del 08/10, tarde). De referencia, el de S1-ter (`f59cdea0…`), que cita la lista, da lo mismo.

## Tabla de reprocesamiento: los renglones (7788e52 → HEAD → A2)
Inventario del §1 `:73-80` → `:73-80` → `:73-81`; «No los abre…» `:86-88` → `:86-88` → `:87-88`; F11b `:163` → `:163`; F13c `:167` →
`:167`; nota de F13 `:253-261` → `:269-277` → `:269-278`; «R00 a R33b» `:361` → `:377` → `:378` (y R34 en `:385-386`); «44
variaciones» `:391` → `:419` → `:421-424`; pie `:401` → `:429` → `:432`. Las filas no se corren: del renglón 89 al 271 nada
cambia de lugar, y los renglones 77 a 85 de HEAD pasan a 78 a 86.

## Contradicciones y hallazgos (para la autora)
1. **El pie de la tabla ya estaba atrasado en HEAD.** Decía 44 filas, y el JSON de HEAD contrasta 45 desde F19d (`2374968a`); el
   de `604640c3`, el del pie de 44, tenía 44. Lo puse al día en el mismo pie.
2. **Anclas a `r1_e4.py` corridas en +5 desde `ded41d50`.** En F13c y en la nota de F13 las puse al día (`:417-423` → `:422-428`;
   `:593-642` → `:598-647`). Fuera de mis escrituras quedan el renglón 165 (F13, `:593-642`) y el 98 y el 290 (289 en HEAD;
   `r1_e4.py:536`, y el candado de la política está en `:541`). No las toqué.
3. **Los manifiestos: 11, no 10.** Las notas daban 9 más ri_cc; con ri_mmsef son 10 de la tanda 1 más ri_cc. El desacuerdo es 10.
4. **El código no dice «PROPUESTOS».** El parche de A1 lo decía en `:95` y `:472-475`. Como en `prompt_e3.py` (O2 de U-E3-LISTAS),
   el comentario dice cómo se calcularon («recalculados en U-ALCANCE-E1») y el estado de los valores va en este FRENO.
5. **F13c suma dos cosas al texto de la variante A:** el perfil (`perfil_e1.py:236`, decisión (c)) y que el manifiesto de una
   tanda ya armado frena al cargarse hasta volver a armarlo (medido: punto anterior). La marca `<commit de A2>` va como
   «A2 de U-ALCANCE-E1 (15/10/2026)»: el commit no existe todavía. En F11b, además de la lista, sumé F13c a «la fila del contenido» y
   el ancla `:476-478`.
6. **El candado del derivado** lo prueban los casos de la sección I de `selftest_prompt_r2b`; `selftest_clave_cache` no tiene una
   variación de archivo para él (R21 es la de `rol_por_to_r2.json`). Agregarla no estaba autorizado.
7. **`selftest_catalogo_unico` necesita git** (`git show` de commits viejos). Lo corrí desde las copias con
   `GIT_DIR=<repo>/.git GIT_OPTIONAL_LOCKS=0`, como O1 y O2 de U-OMISIONES-COD; 0 archivos de `.git` más nuevos que la marca previa.
8. **El control propio de `lote_tramo1_S2.sh` cuenta solo los `.env`.** Su rsync excluye los `NO_ABRIR_`. Sembré la copia con el
   rsync del despacho y conté los cinco patrones antes de que el lote corriera: 0; al final, 0 en copia, raíz mínima y salida.
9. **Ancla menor de la nota del 08/10:** `correr_e0.py:1627` (la carga del manifiesto) está en `:1881` en HEAD.

## Errores propios (corregidos antes de este FRENO; nada llegó al repo)
- Mi primera edición del §1 sumaba dos renglones y corría las filas; la reescribí con saldo cero antes de correr nada.
- En la batería, el paso 6 corrió `selftest_catalogo_unico` sin git y frenó igual en las dos copias; lo repetí con el `.git` del repo
  en solo lectura (`scripts/catalogo_unico_con_git_a2.sh`, `salidas/catalogo_unico_con_git_a2.txt`).

## Copias, carpetas vedadas y paquete
- Tres copias con el rsync del despacho (la de HEAD, la del lote y la de la reproducción final) y sus clones: 0 `.env`, `.env.*`,
  `*.env` y `NO_ABRIR_` en cada una y en toda la carpeta de trabajo (control por nombre, sin abrir nada); 0 enlaces simbólicos (el rsync saltea 336, todos en `ev2_corrida/navegabilidad/trazas_nav/`). La foto registra los 8 archivos de
  entorno y `NO_ABRIR_` del repo solo por tamaño y fecha.
- No abrí, listé ni copié nada de las carpetas vedadas, y nada de ellas apareció en una salida.
- Paquete `revision_UALCANCE_E1_A2/` en el scratchpad de la sesión, con `manifest.txt`, y su copia con `ditto` en
  `$HOME/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/`, con la misma ruta relativa. La verificación de la copia va en el mensaje
  del FRENO: este archivo viaja dentro del paquete.

Commit PENDIENTE de la autora. FRENO A2, final.
