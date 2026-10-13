# U-SEG-OFICIAL — FRENO de S1-quater, sorteo (13/10/2026)

Las poblaciones (versión 5), la regresión y el sorteo con el orden: el paso 3 del §9 del diseño, sus tres primeros puntos, cada
salida sellada antes de la siguiente. **Todo dio lo que fija el despacho y ningún script frenó.** USD 0, sin API. Ningún id ni texto
de unidades en `s1quater/sorteo/`: las cuatro salidas con ids son archivos `NO_ABRIR_` del paquete, escritos por los scripts, y no
las abrí. **Nada commiteado, ningún mensaje de commit preparado, nada escrito en la memoria.** El detalle y los comandos están en
`REPORTE_S1quater_sorteo.md`.

## Paso 0 (con `$HOME`), 09:47:17

```
$ pwd
$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg
$ git log --oneline -1
2374968a Segmentacion oficial: la correccion de E0 aplicada al codigo, con sus controles y el registro de reprocesamiento
$ git status --porcelain -- data/experiment/reextraccion_v2/e0_chunking data/experiment/segmentacion_oficial_e0r2/s1quater data/experiment/segmentacion_oficial_e0r2/s1ter
?? data/experiment/segmentacion_oficial_e0r2/s1ter/e0/
$ shasum -a 256 data/experiment/reextraccion_v2/e0_chunking/e0_lib.py data/experiment/reextraccion_v2/e0_chunking/correr_e0.py data/experiment/reextraccion_v2/e0_chunking/selftest_e0.py
d89aab1a578252cd6296f03e8e8859644f008740cd493ef6d82e86c5009db298  data/experiment/reextraccion_v2/e0_chunking/e0_lib.py
78c54c4cd7dc47d592a2f9dcadc1bf97535af2d6ea0f67d67c8021010650cb5e  data/experiment/reextraccion_v2/e0_chunking/correr_e0.py
eb4f11e61981476957aceadb67bfbf80934c8f903c11760b41fc2530bbe38282  data/experiment/reextraccion_v2/e0_chunking/selftest_e0.py
$ ls data/experiment/segmentacion_oficial_e0r2/s1quater
diseno
```

- **Contra el despacho:** todo igual. Los tres sha256 son los «después» de `s0_6/bis/parche/LEEME.md`.
- **Lo que rige, en HEAD:** el diseño y las cuatro adendas dan el sha256 del despacho, y también los cuatro scripts del diseño, que
  copié de HEAD al scratchpad.
- **El paquete de la mesa:** los seis archivos dan OK con `shasum -a 256 -c`. No los abrí.

## Paso 1: la E0 contra su manifiesto

- **La copia:** con `rsync -a --no-links`, sin `.git` ni `.venv`, con 0 enlaces (se saltearon 339, ajenos a E0). De ella armé la raíz
  mínima con `raiz_minima.sh`, también con 0 enlaces, con el código de E0 de `2374968a`.
- **La corrida:** `correr_152.py --workers 8`, de 09:50:45 a 09:54:53, con rc 0, 152 TOs y 0 con error.
- **El control** (09:55:11): `manifest_salida_e0_152_S0-6b.json` da `80adbd58…`. **Están sus 768 archivos `e0/…`, los 768 dan su
  sha256**, sin faltantes ni sobrantes, con **10.478 unidades** y 152 TOs, y ningún TO con otra cuenta.
- **La E0 no se guarda:** no va al paquete.

## Sellos

| sello | archivo | sha256 | hora |
|---|---|---|---|
| `sello_poblaciones_S1quater.txt` | `NO_ABRIR_poblaciones_S1quater.json` | `f77bf6adc34d9258ed80edd5e4a7ba6e97ae052c814cd156ea20ccdc743faed5` | 09:55:48 |
| `sello_regresion_S1quater.txt` | `NO_ABRIR_regresion_S1quater.json` | `57b0436de9a0879773880417282c647e9491482e04d29c08a38f437d95315c87` | 09:56:30 |
| `sello_sorteo_S1quater.txt` | `NO_ABRIR_muestra_S1quater.json` | `90ae1225699cec939f05379a9fce3dbdcf44935b2faddc2f156fc431a95470ab` | 09:57:01 |
| `sello_sorteo_S1quater.txt` | `NO_ABRIR_orden_lectura_S1quater.json` | `b794f85f75a0dc12e5f5b849cc21469358316b8802056a0a3d0c79950cc6431a` | 09:57:01 |

Todas las horas son del 13/10/2026, -0300. Cada script corrió después del sello de su entrada y recibió su sha256 como argumento.

## Cuentas

**Poblaciones** (`controles/control_poblaciones_S1quater_sorteo.json`). Las tres dan el despacho:

| estrato | unidades | sha256 de los ids ordenados |
|---|---|---|
| vigente | 6.746 | `e6ebad8abe0fe88c3a8f75026f12074d10c031a9766f0863242b7904ec843758` |
| marcadores | 86 | `dea0af647f282d675b0a201a119d69240775eaf1653f18a42480e9cf5d9d553b` |
| sin_raiz | 897 | `6752a7205f4ce83f5e77a10b423dccd98827acf142b0b7043a846105a14a7078` |

- **Total:** 7.729.
- **Las adendas:** salen por la adenda 4 978 unidades (460 / 82 / 436), las de la adenda 4, §3.
- **La cobertura:** 4 documentos quedan bajo el umbral y van por la exclusión sin orden, sin frenar: ri2_ae 0,660, ri_spi 0,700,
  ri_sef 0,816 y ri_ccpnp 0,897. Salen solo por ella 27, 8, 2 y 0.
- **`commit_codigo_e0_corregida`:** el JSON dice «PENDIENTE (lo fija el commit de la autora)». **Declaro el commit `2374968a`**
  (`s0_6/b/decisiones_adenda_4_y_S0-6b_mesa.md`, §3, archivo que entró en ese commit). No toqué el JSON.

**Regresión** (`controles/control_regresion_S1quater_sorteo.json`):
- **la lista:** 60 unidades, con sha256 `57e904461ab0f5b6cfbc8baae0cac870a2b6ddb92fddc24197cfa2621f7f5cb8`, el del despacho;
- **de dónde salen:** de 41 errores confirmados de S1-ter (14 por marca, 4 por la que sigue y 23 por herencia), con 44 unidades
  viejas;
- **sin unidad nueva que las solape:** 3, como prevé el despacho: 2 de un documento bajo el umbral de cobertura y 1 de otro.

**Muestra y orden** (`controles/control_sorteo_S1quater_sorteo.json`):
- **la muestra:** 40 / 10 / 40, 90 unidades distintas, cada una de su población y ninguna de la regresión. sha256 de los 90 ids
  ordenados: `4fe6b0da6d28817a28de2e16970f10a3a5f96e6bb8f07c4069803fba587f08d6`;
- **la etapa 1:** 90 fichas, de `E1-001` a `E1-090`;
- **la etapa 2:** 60 fichas, de `E2-001` a `E2-060`, las de la regresión en el orden de sus ids;
- **el sorteo rehecho:** mi control lo rehízo por su cuenta, con las semillas del diseño, y da la misma muestra y el mismo orden.

## Repo, `.pyc` y convenciones

- **Foto sha256 del repo entero (sin `.git` y sin otra exclusión),** con `find … | shasum -a 256`:
  - antes, de 09:48:54 a 09:49:17: 50.045 archivos;
  - después, de 10:01:42 a 10:02:05: 50.060 archivos.
  - **Comparación** (`scripts/comparar_fotos_S1quater_sorteo.py`): **15 archivos nuevos, todos en `s1quater/sorteo/`. Fuera de esa
    carpeta, 0 nuevos, 0 cambiados y 0 borrados.**
  - Este FRENO entra en la foto. Lo completé después de la foto de las 10:02, así que la comparación final, hecha después de
    escribirlo, va en el mensaje del FRENO. Las dos fotos enteras están en el paquete.
- **`.pyc`:** 10.158 en todo el repo y 2.213 fuera de `.venv/`, antes y después. Todo corrió con `-B` y
  `PYTHONDONTWRITEBYTECODE=1`, desde el scratchpad y la copia.
- **Grep de convenciones** (`s0_4/scripts/grep_convenciones.py`, sobre los 14 archivos de `s1quater/sorteo/` sin contar el suyo;
  `controles/grep_convenciones_S1quater_sorteo.txt`):

  ```
  control positivo: 16 de 16 términos encontrados
  archivos revisados: 14
  total por término: {} — total 0
  ```

  - La primera pasada dio 1 hallazgo: `ruta_tmp`, en el REPORTE, por mencionar la carpeta temporal del sistema. Lo corregí y la
    segunda pasada dio 0.
  - Además, 0 cadenas con forma de id (`<documento>::…`) en `s1quater/sorteo/`.

## Archivos `NO_ABRIR_` (en el paquete, fuera del repo; escritos por script, sin abrirlos)

- `NO_ABRIR_poblaciones_S1quater.json` `f77bf6adc34d9258ed80edd5e4a7ba6e97ae052c814cd156ea20ccdc743faed5`
- `NO_ABRIR_regresion_S1quater.json` `57b0436de9a0879773880417282c647e9491482e04d29c08a38f437d95315c87`
- `NO_ABRIR_muestra_S1quater.json` `90ae1225699cec939f05379a9fce3dbdcf44935b2faddc2f156fc431a95470ab`
- `NO_ABRIR_orden_lectura_S1quater.json` `b794f85f75a0dc12e5f5b849cc21469358316b8802056a0a3d0c79950cc6431a`

## Escrituras

- **En el repo:** solo `s1quater/sorteo/`, que es nueva. Tiene este FRENO, el REPORTE, los tres sellos, cinco scripts en `scripts/`
  y los controles en cuentas en `controles/`.
- **Fuera del repo:** el scratchpad de la sesión y el paquete `revision_USEG_OFICIAL_FRENO_S1quater_sorteo/`, con su copia en
  `fuera_del_repo/scratchpads/`. La ruta de la copia y su verificación van en el mensaje del FRENO.

FRENO.
