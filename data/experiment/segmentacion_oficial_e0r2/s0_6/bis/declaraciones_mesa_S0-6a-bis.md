# U-SEG-OFICIAL, S0-6a y S0-6a-bis: declaraciones de la mesa revisora (12/10/2026)

USD 0, sin API.
- **Qué es:** una nota de la mesa revisora que entra con el registro de S0-6a-bis, por decisión de la autora del 12/10/2026 (hoja de
  ruta de la mesa, §81, decisiones 15 y 16).
- **Lo que no cambia:** ningún archivo de la ejecutora; los de S0-6a ya commiteados tampoco se editan.
- **Los ids:** de unidades que no son de las 40 filas ni de las 286 leídas en S1-ter no lleva ninguno.

## 1. La escritura en la memoria compartida, en S0-6a (decisión 15)

- **Qué escribió:** la ejecutora de S0-6a (sesión `3affae38-5acf-4382-b2ca-6d7f152ddb34`), el 12/10/2026 a las 14:40:
  - creó un archivo en la memoria compartida del proyecto, `~/.claude/projects/<proyecto>/memory/useg_oficial_s06a_freno_estado.md`
    (sha256 `482cb1f82507b177ed0b97241e00e3d4761da54e5096c50341d513ecad9efc8b`);
  - le sumó un enlace al índice `MEMORY.md`.
- **Por qué no correspondía:** no estaba entre las escrituras de su mandato. El archivo no traía cifras ni unidades.
- **Qué hizo la mesa,** por decisión de la autora del 12/10/2026 (hoja de la mesa, §79, decisión 10):
  - copió el archivo y el fragmento del índice a su paquete, fuera del repo
    (`~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/d0348a29-aaa4-4292-82f3-0c0149e3787e/scratchpad/hoja_de_ruta_tanda1_mesa/preparacion_S0-6a-bis_mesa/memoria_retirada/`);
  - respaldó el índice en `~/INGENIERIA IA/TESIS/fuera_del_repo/respaldo_memoria/MEMORY_md_20261012_182456.md`;
  - después sacó de la memoria compartida el archivo y su enlace.
- **Desde entonces:**
  - todo despacho o «seguí» de una ejecutora dice que no escribe en la memoria. El «seguí» de S0-6a-bis lo dijo;
  - la ejecutora de S0-6a-bis no escribió en la memoria ni en `.claude/`. Lo controló la mesa en el registro de su sesión, desde el
    «seguí»: ninguna escritura de Write o Edit fuera de su scratchpad y de su paquete, y ningún comando que escriba en la memoria.

## 2. Los logs de controles que `.gitignore` deja fuera (decisión 16)

- `.gitignore` ignora `*.log` (renglón 47). Por decisión de la autora, estos logs entran al repo con `git add -f`, sin tocar
  `.gitignore`:

  | log | sha256 | lo cita |
  |---|---|---|
  | `s0_6/controles/lote_controles_S0-6a.log` | `f86cedfcf499147dbc83a33b9e599eb2b9bab967b7d4aaaf8f09177ce3359dca` | `s0_6/REPORTE_S0-6a.md:33` |
  | `s0_6/bis/controles/lote_controles_S0-6a-bis.log` | `bb20f070288318593e93902214ad379a316fbbde3a64121aa0aa4ca90b124d23` | `s0_6/bis/REPORTE_S0-6a-bis.md`, §3 |
  | `s0_6/bis/controles/lote_configuraciones_S0-6a-bis.log` | `aabcc2013b991b19552fe00a94879f42b26a0cc42021738c02e34346ed8e5434` | `s0_6/bis/REPORTE_S0-6a-bis.md`, §3 |

- **El tercer log lo sumó la mesa:** la decisión pide los logs de controles, y este también es un log de la etapa citado como
  evidencia.
- **Si vuelven a correr:** los comandos de commit controlan los tres sha256 antes de agregarlos.
- **Ningún manifiesto commiteado lista estos logs.** Los dos de S0-6a-bis están también en el paquete de la ejecutora, con el mismo
  sha256.

## 3. Ids que no existen en el informe y en el FRENO de S0-6a (propuesta de la mesa, punto 8 del §81)

- **Qué pasa:** en el commit `d32f6db8`, `s0_6/REPORTE_S0-6a.md`, renglones 221 y 222 (§11), y `s0_6/FRENO_S0-6a.md`, renglones 71 y
  72, nombran dos ids de ri_ccna que no existen en la salida final de S0-6a.
  - Vienen de una corrida intermedia: son las dos entradas de A de dos formularios.
  - Lo declaró la ejecutora en `s0_6/bis/REPORTE_S0-6a-bis.md`, §13.
  - Los ids que corresponden están en su paquete, fuera del repo (`NO_ABRIR_errores_de_regla_S0-6a-bis.json`).
- **Lo que no es error:**
  - `REPORTE_S0-6a.md:226` y `FRENO_S0-6a.md:73` nombran un prefijo de claves, no una clave;
  - `REPORTE_S0-6a.md:178` y `FRENO_S0-6a.md:57` nombran una unidad leída en S1-ter que en la salida de S0-6a pasa a la herencia: su
    id es el de la E0 de S1-ter.
- **Cómo se lee:** los archivos de S0-6a no se editan. Esta nota es su fe de erratas, y quien los lea los lee con ella.
