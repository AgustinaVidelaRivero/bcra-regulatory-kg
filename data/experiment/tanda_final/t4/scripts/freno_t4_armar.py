"""B6.1, tanda final, T4, primer tramo: arma el FRENO (t4/FRENO_T4_tramo1.md) y el resumen de las fotos (t4/resumen_fotos_T4.json).
Las cifras salen de los archivos: la salida del paso 0 (t4/paso0/), las tablas (t4/tablas_freno_t4.md, de tablas_freno_t4.py), la
lectura asistida, la prueba del convertidor, el resumen de la foto (foto_t4.py) y el grep de convenciones (t3/scripts/
grep_convenciones_tf.py). El diff de los dos convertidores sale de difflib. La prosa es mía.
Uso: python3 -I -B freno_t4_armar.py <repo> <resumen_foto_T4.json> <grep_t4.json>
"""
import difflib
import hashlib
import json
import sys
from pathlib import Path

R, RF, GR = Path(sys.argv[1]).resolve(), Path(sys.argv[2]), Path(sys.argv[3])
T4 = R / "data/experiment/tanda_final/t4"
L = lambda p: json.loads(Path(p).read_text(encoding="utf-8"))  # noqa: E731
mil = lambda n: f"{n:,}".replace(",", ".")  # noqa: E731
la = L(T4 / "lectura_asistida/lectura_asistida_t4_tramo1.json")
pr = L(T4 / "prueba_convertidor/prueba_convertidor_t4.json")
fc = L(T4 / "paso0/foto_contra_commits_T4.json")
sm = L(T4 / "paso0/sha_muestras_T4.json")
rf, gr = L(RF), L(GR)
paso0 = (T4 / "paso0/paso0_T4_salida.txt").read_text(encoding="utf-8").rstrip("\n")
tablas = (T4 / "tablas_freno_t4.md").read_text(encoding="utf-8").rstrip("\n")
c1 = (R / "data/experiment/tanda1/t4/lectura_autora/convertir_lectura_T4.py").read_text(encoding="utf-8").splitlines()
c2 = (T4 / "lectura_autora/convertir_lectura_T4.py").read_text(encoding="utf-8").splitlines()
diff = "\n".join(difflib.unified_diff(c1, c2, "tanda1/t4/lectura_autora/convertir_lectura_T4.py",
                                      "tanda_final/t4/lectura_autora/convertir_lectura_T4.py", n=0, lineterm=""))
hl = la["hora_de_la_lectura"]["toda"]
cu = la["cuentas"]
nuevos = rf["nuevos_en_t4"]
grupos = {}
for r in nuevos:
    g = r.split("/")[0] + "/" if "/" in r else "t4/ (raíz)"
    grupos[g] = grupos.get(g, 0) + 1
w = f"""# FRENO T4 de la tanda final, primer tramo (B6.1): la lectura asistida, las planillas, el LEEME y el convertidor

20/10/2026. Pre-registro firmado (`docs/preregistro_tanda_final.md`, firma en `4de7f2a7`), §6: «Quién lee: lectura asistida con revisión
de la autora (D2), como en el T4 de la tanda 1». USD 0, sin API. Nada commiteado y ningún mensaje de commit preparado. Todo lo nuevo está
en `data/experiment/tanda_final/t4/`.

## 1. Paso 0

La salida, con la carpeta personal reemplazada por `$HOME` (`t4/paso0/paso0_T4_salida.txt`, de `t4/scripts/paso0_t4.sh`):

```
{paso0}
```

El bloque de la foto sale filtrado: sin los sha256 de las dos fotos y sin las llaves que cierran. El JSON entero está en
`t4/paso0/foto_contra_commits_T4.json`.

Todo da lo esperado:
- el log tiene los tres commits en el orden pedido, y el `status` (sin los no rastreados) está vacío;
- los dos `commit_sellado` de la tanda final en `grafos.py` son `71cb930`, el hash corto del primero de los tres commits;
- las ocho muestras, los ocho `fichas_*.jsonl` y los ocho `fichas_*.md` tienen el sha256 de las tablas T5 y T6 del FRENO T3, y la
  versión derivada de la lectura, `{sm['derivada']['sha256']}`;
- la foto nueva tiene {fc['nuevos']} archivos nuevos, {fc['borrados']} borrados y {fc['cambiados']} cambiados contra la de después de T3. Los
  {fc['nuevos'] + fc['cambiados']} son rutas de los tres commits (eb5ad14b..7cbf3525, {mil(fc['rutas_en_los_commits'])} rutas), con el sha256 de su
  blob en HEAD (`paso0_foto_contra_commits_t4.py`);
- no corre ninguna extracción, y `pgrep -fl ensamblar_tanda0.py` no muestra procesos.

## 2. Lo decidido sobre el FRENO T3 final

Lo aplico como lo recibí: las cinco decisiones cierran; las 3.695 unidades a la vista son todas de TOs de la tanda final; los dos momentos
de lectura juntos quedan como desvío declarado del §6, sin firma nueva (FRENO T3, sección 7.7). Va a la §68 del registro de decisiones,
que no escribo.

## 3. La lectura asistida (punto 3)

- **Quién lee:** {la['modelo']['nombre']} (`{la['modelo']['id']}`), la ejecutora de esta sesión de Claude Code. Leí ficha por ficha y
  escribí cada propuesta, sin API ni otro modelo. La lectura va de las {hl['primera_propuesta'][11:19]} a las {hl['ultima_escritura'][11:19]}
  del {hl['primera_propuesta'][:10]} (el `st_birthtime` y el `st_mtime` de los borradores).
- **Cómo leí:** cada ficha en su `.jsonl` del material de T3, con `t4/scripts/ver_fichas_t4.py`, que solo la compacta (el mismo contenido
  que el `.md` de la autora, sin el estado de E3 ni sus marcas). Juzgué contra el texto que muestra la ficha. Las propuestas las fui
  escribiendo en borradores, una por ficha, con `t4/scripts/anotar_t4.py`, que controla las respuestas válidas del LEEME. Los borradores
  quedan en `t4/lectura_asistida/borradores/`.
- **Lo que queda:**
  - `t4/lectura_asistida/lectura_asistida_t4_tramo1.json`: el modelo, la hora, los criterios (`criterios_de_la_propuesta`), las reglas
    usadas y las {la['total']['fichas']} propuestas, cada una con su regla y una justificación que cita el texto;
  - `t4/lectura_asistida/omisiones_y_observaciones_t4_tramo1.md`: lo que va aparte. No cambia ninguna propuesta.
  - Los dos los arma `t4/scripts/armar_lectura_t4.py`, que controla los ids, las celdas y el orden contra las planillas en blanco de T3,
    la muestra y el material (sección 7).
- Sin tasas, sin umbrales, sin atención, sin freno y sin ampliación: son del segundo tramo.

Cuántas propuestas hay de cada respuesta, por muestra, y las reglas que usé (`t4/tablas_freno_t4.md`, de `t4/scripts/tablas_freno_t4.py`):

{tablas.split('#### Tabla 3.')[0].rstrip()}

## 4. Las planillas, el LEEME y el convertidor (puntos 4 a 6)

- **Las planillas** (`t4/lectura_autora/<muestra>.csv`): UTF-8 sin BOM, «;» y «\\n», con las columnas `id`, `celda`, `ficha`,
  `propuesta`, `justificacion`, `veredicto_autora` y `nota_autora`, las dos últimas vacías. Los ids y las celdas son los de las planillas
  en blanco de T3, en su orden. La columna `ficha` da la ruta del `.md` desde la raíz del repo y, tras «#», el número de su encabezado.
  Ninguna celda empieza con «=», «+», «-» ni «@».
- **El LEEME:** lo copié de la copia permanente de la mesa (solo ese archivo) a `t4/lectura_autora/LEEME_lectura_T4.md`. Su sha256 es
  el del «seguí». Sus rutas y nombres coinciden con lo armado: las ocho planillas `<muestra>.csv`, el material
  `t3/muestras/material/<m>/fichas_<m>.md`, las 216 fichas, los nombres de muestra del convertidor y los 24.949 elementos del universo de
  la (12) (la N de `poblaciones_t4t1_tf.json`). No lo cambié.
- **El convertidor** (`t4/lectura_autora/convertir_lectura_T4.py`) es el de la tanda 1 con el nombre de la tanda y los sha256 de las
  planillas nuevas. Este es todo el diff:

```diff
{diff}
```

{('#### Tabla 3.' + tablas.split('#### Tabla 3.')[1]).rstrip()}

- **Cómo controla los ids:** como el de la tanda 1, controla que el id y la celda de cada fila de la exportación sean los de la planilla,
  y que la planilla tenga su sha256. Los ids de cada planilla son los de su muestra: `armar_lectura_t4.py` lo controla contra
  `t3/muestras/<m>.json` antes de escribirla.
- **La prueba** (`t4/scripts/prueba_convertidor_t4.py`) corre sobre una copia sin enlaces armada en el scratchpad, con exportaciones de
  juguete. Los veredictos de juguete son las propuestas, salvo los cambios de cada caso; no son una lectura. La salida está en
  `t4/prueba_convertidor/`, y la copia con las exportaciones va en el paquete.
- **El sello** lo hace la autora, con las ocho marcadas (LEEME).

## 5. El cegamiento

- El material no trae el estado de E3 ni sus marcas: el control de T3 (`t3/muestras/control_material_tf.json`) da 0 claves vedadas.
- No abrí `n_reintentos`, `reintentos_e3.jsonl`, `copias_nota_e3.jsonl`, las `marcas_e3` ni el gasto de los reintentos.
- Ninguna cifra de esta unidad los usa, así que no escribí `t4/NO_ABRIR_conteos_t4.json`: no hay nada que poner. Si la mesa lo quiere
  igual, vacío, lo agrego.
- **De la tanda 1** abrí solo dos cosas:
  - el convertidor (`tanda1/t4/lectura_autora/convertir_lectura_T4.py`; listé solo los `.py` de esa carpeta);
  - la sección 6 de `tanda1/t3/FRENO_T3.md`, por las definiciones de (1) y (3), que son «las que propuso la ejecutora en el FRENO T3, §6»
    (registro, §29).
  - No abrí sus muestras, su material, sus planillas ni su lectura asistida.
- No abrí ninguna carpeta vedada ni ningún `NO_ABRIR_`. No hice copias del repo: la prueba copia solo `t4/lectura_autora/`, sin `.env`, `NO_ABRIR_` ni `_SOLO_MESA` y sin enlaces (el control
  está en `control_final_T4.json` del paquete).

## 6. La foto del repo, los .pyc y el grep de convenciones

La foto del paso 0 y la de después (`t1/foto_repo_tanda_final_t1.py`, corrido desde su copia del scratchpad, con el mismo sha256,
`3220cf3c…`) quedan fuera del repo y del paquete, porque nombran todas las rutas del repo; su sha256 y su resumen están en `t4/resumen_fotos_T4.json` (de `t4/scripts/foto_t4.py`).

- **La foto.**
  - Paso 0: {rf['foto_antes']['inicio'][11:]} a {rf['foto_antes']['fin'][11:]}, {mil(rf['foto_antes']['n'])} entradas.
  - Después: {rf['foto_despues']['inicio'][11:]} a {rf['foto_despues']['fin'][11:]}, {mil(rf['foto_despues']['n'])} entradas,
    {rf['foto_despues']['sin_abrir']} sin abrir y {rf['foto_despues']['enlaces']} enlaces.
  - **{len(nuevos)} nuevos, todos en `tanda_final/t4/`:** {'; '.join(f'{v} en `{k}`' for k, v in sorted(grupos.items()))}.
  - **Nuevos fuera de `t4/`:** {len(rf['nuevos_fuera_de_t4'])}. **Borrados:** {len(rf['borrados'])}. **Cambiados:** {len(rf['cambiados'])}.
  - Este FRENO, `t4/resumen_fotos_T4.json` y el script que los arma (`t4/scripts/freno_t4_armar.py`) se escriben después de la foto;
    el control final del paquete (`control_final_T4.json`) confirma que son los únicos nuevos desde ella.
- **Los `.pyc`:** {mil(rf['pyc']['antes'])} líneas en el paso 0 y {mil(rf['pyc']['despues'])} después; listas iguales: {rf['pyc']['iguales']}. Todo
  corrió con `-B`.
- **El grep de convenciones** sobre los {gr['archivos']} archivos nuevos de `t4/`, sin los `NO_ABRIR_`:
  - {gr['coincidencias']} coincidencias de los tokens del nombre y de los términos, y {len(gr['con_rutas_absolutas'])} archivos con rutas absolutas;
  - control positivo, {gr['control_positivo']}; tokens dentro de rutas absolutas, {gr['tokens_dentro_de_rutas_absolutas']};
  - el script es `t3/scripts/grep_convenciones_tf.py`, sin cambios, con `LC_ALL=en_US.UTF-8`.
  - El grep del FRENO va en el control final del paquete.

## 7. El script de cada cifra

| cifra | script | salida |
|---|---|---|
| el paso 0 (log, status, `commit_sellado`, sha256, foto contra los commits, procesos) | `t4/scripts/paso0_t4.sh`, `paso0_sha_muestras_t4.py`, `paso0_foto_contra_commits_t4.py` | `t4/paso0/` |
| las propuestas por respuesta y las reglas (tablas 1 y 2) | `t4/scripts/tablas_freno_t4.py` (desde la lectura asistida) | `t4/tablas_freno_t4.md`, `t4/consola_tablas_freno_t4.txt` |
| la lectura asistida, las omisiones y las planillas, con sus controles | `t4/scripts/armar_lectura_t4.py` | `t4/lectura_asistida/`, `t4/lectura_autora/*.csv`, `t4/lectura_asistida/consola_armar_lectura_t4.txt` |
| los sha256 de las planillas, del LEEME y del convertidor (tabla 3) | `t4/scripts/tablas_freno_t4.py` | `t4/tablas_freno_t4.md` |
| la prueba del convertidor (tabla 4) | `t4/scripts/prueba_convertidor_t4.py` | `t4/prueba_convertidor/` |
| la foto y los `.pyc` | `t1/foto_repo_tanda_final_t1.py`, `t4/scripts/foto_t4.py` | `t4/resumen_fotos_T4.json` |
| el grep de convenciones | `t3/scripts/grep_convenciones_tf.py` | `t4/resumen_fotos_T4.json` («grep») |
| este FRENO | `t4/scripts/freno_t4_armar.py` | `t4/FRENO_T4_tramo1.md` |

## 8. Para la autora

- **Las planillas están listas para leer.** Cada fila trae mi propuesta, su justificación y la ruta de la ficha. Los criterios están en
  `criterios_de_la_propuesta`; los que más pueden pesar en la adjudicación son interpretaciones mías, fijadas antes de tu lectura:
  1. **U-tipo:** cuento como error de la unidad un tipo que contradice la modalidad del texto. Por ejemplo, un deber tipado Condicion o
     Excepcion, un permiso tipado Obligacion o un deber tipado Potestad, y el futuro normativo lo leo como deber. Son {la['reglas_usadas']['cola'].get('U-tipo', 0)} de la cola
     y {la['reglas_usadas']['aceptadas_no_items'].get('U-tipo', 0)} de las aceptadas no ítems. Es la misma lectura que la «sí» de la (1).
  2. **U-fuera-del-texto:** un nodo sin pasaje en el texto que muestra la ficha lo propongo como dudosa. Vendría de la herencia que E1 ve y
     E3 no (§31). Son {la['reglas_usadas']['cola'].get('U-fuera-del-texto', 0)} de la cola.
  3. **La (2):**
     - el bloque que abre una lista lo propongo como «no vaciamiento», porque su deber y su sujeto pasan a cada ítem
       (`V2-marco-de-lista`, {la['reglas_usadas']['vigilancia_2'].get('V2-marco-de-lista', 0)});
     - un dato que el régimen pide informar, sin nodo, como «vaciamiento» (`V2-dato-a-informar`,
       {la['reglas_usadas']['vigilancia_2'].get('V2-dato-a-informar', 0)}).
  4. **La (3):** el par de una facultad o de un límite y el acto lo trato como el par del deber y el acto (`V3-par-modalidad-acto`,
     {la['reglas_usadas']['vigilancia_3'].get('V3-par-modalidad-acto', 0)}).
  5. **La (12):** la única incorrecta va a «catálogo»: un sujeto resuelto al rol de alcance de otro TO.
- **La marca de cada fila es tuya:** el convertidor exige la razón en `nota_autora` cuando el veredicto cambia la propuesta.

## 9. Errores propios, con su causa

1. **El paso 0 dio un código de salida que no era el del script.** En la primera corrida de `paso0_t4.sh`, el `rc` del bloque de la foto
   era el del `grep` que filtraba la salida, no el del script, porque faltaba `pipefail`. Lo agregué y volví a correr el paso 0 entero
   antes de escribir nada; la salida de la sección 1 es la segunda.
2. **Dos justificaciones de la (3) no citaban el texto.** La 10 citaba el deber con otras palabras («se deberá considerar» por «se deberá
   tener en cuenta»), y la 26, la descripción del nodo («no podrá ser inferior al 25%») en lugar del texto. La causa: escribí esas
   justificaciones mirando solo las líneas de los nodos del grupo, sin el texto. Las encontré al releer contra el texto completo los
   grupos que propongo como duplicación, y las corregí en el borrador antes de armar las planillas.
3. **La regla de la ficha 12 de la cola no era la de los casos iguales.** Primero la anoté con la regla `U-dudosa`. Al ver que las fichas
   14 y 18 tenían el mismo caso (nodos sin pasaje en el texto que muestra la ficha), la pasé a `U-fuera-del-texto`. La propuesta, «dudosa»,
   no cambió.
4. **Un control de forma de las planillas dio un falso positivo.** El control de que ninguna celda empiece con «=», «+», «-» o «@» marcó
   las celdas vacías, por cómo tomaba el primer carácter. Lo corregí y lo volví a correr: 0 celdas.
5. **El control final falló la primera vez.** Corrí el grep con un entorno sin `HOME`, y git no encontró el nombre del usuario. Le pasé
   el entorno completo y volví a correr el control entero.

## 10. Lo que no hice

- **Las cifras del segundo tramo:** no calculé tasas, umbrales ni atención, y no sorteé ninguna ampliación.
- **Commits y escrituras ajenas:**
  - no commiteé ni preparé mensajes de commit;
  - no escribí en la memoria, en `.claude/` ni en `.gitignore`.
- **Lo que no toqué:** los grafos, los manifiestos, la E0, el código del pipeline, la fixture, `grafos.py`, Neo4j ni nada de `t3/`. De
  `t3/` solo leí, y corrí sin cambios su grep de convenciones.
- **El scratchpad:** nada que se necesite después queda solo en él. El paquete y su copia permanente llevan los borradores de origen,
  la copia de la prueba y las salidas.

FRENO T4, primer tramo: espero la revisión de la mesa y la lectura de la autora.
"""
(T4 / "FRENO_T4_tramo1.md").write_text(w, encoding="utf-8")
res = {"resumen_foto": rf, "grep": gr,
       "freno": {"ruta": "data/experiment/tanda_final/t4/FRENO_T4_tramo1.md",
                 "sha256": hashlib.sha256((T4 / "FRENO_T4_tramo1.md").read_bytes()).hexdigest()}}
(T4 / "resumen_fotos_T4.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(res["freno"])
