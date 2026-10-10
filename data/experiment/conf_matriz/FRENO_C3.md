# U-CONF-MATRIZ — FRENO C3

09/10/2026. Lectura de confirmación de la matriz ampliada, sobre KG-Tanda0-Diez-r2b-sincola (`e22fae1a…`). USD 0, sin API.
Nada commiteado: el commit es de la autora y queda PENDIENTE. La cifra final es la de C4 (revisión y adjudicación de la autora).

## 1. Entrada

- Commit de la firma: `90addb35` (`git log --format=%h -n 10`, y `-- docs/mandatos/UCONF_MATRIZ_lectura_confirmacion.md`).
  En ese commit, el mandato tiene sha256 `7e20861b…3988` y el texto firmado (líneas anteriores a «## Firma») `1d92fbd6…6d7d`,
  igual al asentado. Las seis semillas, recalculadas con el comando de la sección «Firma», dan las asentadas.
- Protocolo del 28/09: `c671b52:reports/u_estudio_matriz/lectura/resultado_lectura_matriz.md`, sha256 `74626029…d824`. Leí solo
  la sección «Protocolo, tal como está asentado» (16 líneas; su sha256 está en el acta): la extraje desde su encabezado hasta el
  siguiente y borré la copia del archivo entero sin abrirla.
- Grafo copiado con `git show HEAD:<ruta>`; sha256 `e22fae1a…34fb`, igual al de `grafos.py:172` y al del commit `dde9f44`.
- Foto del repo antes: 25.273 archivos fuera de `.git/` y `.venv/`; 2.213 `.pyc` fuera de `.venv/`.

## 2. Ceguera: lo que declaro

1. **La sesión no se abrió fuera del repo:** su directorio de trabajo es el repo, y el arnés cargó el índice de la memoria del
   proyecto y los mensajes de los últimos cinco commits. Revisé ese contexto: ninguna línea da un resultado de la matriz. No abrí
   archivos de la memoria ni corrí `git log` con mensajes.
2. **El mandato firmado da la cifra original de → Potestad** (§0: «27 de 30, piso de Wilson 0,744»). La leí al leer el mandato,
   que es entrada obligatoria.
3. **Contradicción del mandato:** el §3 dice que el lector no ve el par, y el §4 pone en la ficha el tipo del nodo de destino, que
   es el par. Seguí el §4, porque el protocolo pide anotar el mal tipado y para eso hace falta el tipo. El orden de lectura mezcla
   los pares, como pide el §3.
4. La misma sesión armó el acta y las fichas y leyó (§6, C1).

## 3. C1

- Población: 643 → Operacion y 264 → Potestad, como el §1. sha256 de las listas: `d1a5b999…` y `87ad91c0…`.
- Sorteo a las 16:08:34 (−03), con Python 3.10.13. sha256 de la muestra: `ddd60723…`.
- Orden de lectura: lo decidí yo, porque el mandato no fija semilla. La derivé del texto firmado
  (`int(sha256("U-CONF-MATRIZ|orden|<sha>")[:16], 16)`).
- Sellos:
  - acta `f5990dff…`, a las 16:08:43;
  - fichas `e3a9017a…` (md) y `ebe7dd72…` (jsonl), a las 16:10:14.
- Render: 87 páginas, con `pdftoppm -r 110`. Hubo avisos «optional content group», que no impidieron el render. Los PNG suman 23 MB.
- Ninguna arista de la muestra sale de una parte partida por corte. En las 907 aristas, los dos extremos tienen procedencia en la
  unidad de la arista.
- **Solapamiento con la etapa V del pre-registro:** V todavía no tiene acta de sorteo, así que no se puede declarar. De las 60
  aristas, 53 están también en el grafo de V (`2922b72d`); la lista está en el acta.

## 4. C2

- Planilla sellada a las 16:22:10, con sha256 `bd282413…` (jsonl).
- 60 filas. Cada una lleva nota, anotaciones y las páginas que vi. La página de cada ficha la miré contra el texto de E0.
- En el encabezado de `c2/planilla_c2.md` están las seis reglas con que apliqué el protocolo a casos que no nombra. No lo cambian.
- **Cambio antes del sello:**
  - F27 y F34 son dos aristas → Operacion de la misma unidad, `ext::2.2.3`. En el borrador estaban «incorrecta» por circulares:
    el destino tiene el mismo tramo que la Condicion.
  - Al revisar la consistencia, las pasé a «correcta» con anotación «circular». El motivo: F23, F45 y F60 también reformulan
    parte de la definición del destino, y estaban correctas.
  - Hice el cambio sin haber calculado ninguna cifra. Pero sabía el par de las dos (el tipo está en la ficha) y el umbral del §2
    (28 correctas de 30).
  - **El cambio lleva → Operacion de no cumplir a cumplir.**
  - El borrador previo está en el paquete: `uconf_matriz_planilla_borrador_previo_c2.jsonl`, sha256 `ff9158e0…`.

## 5. C3: cifras de la planilla sellada

Comando:
`PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/conf_matriz/c3_cifras.py --salida <copia>/c3`.

| par | correctas | incorrectas | no decidibles | Wilson 95 % | cumple (piso 0,75) |
|---|---|---|---|---|---|
| → Operacion | 29 | 1 (F15) | 0 | [0,8333; 0,9941] | sí |
| → Potestad | 29 | 1 (F57) | 0 | [0,8333; 0,9941] | sí |

- **Lista para la autora** (§5), con cada ficha, en `c3/lista_autora_c3.md`:
  - → Operacion: F15, más F51, F33, F31, F53 y F04, sorteadas con la semilla `3317428300167781795`;
  - → Potestad: F57, más F12, F37, F54, F59 y F14, sorteadas con la semilla `9868107349525416484`.
- **Sensibilidad, decisiva para C4** (`c3/clases_c3.md`, comando `c3_clases.py`). Es informativa: no cambia el criterio. Si la
  autora adjudicara incorrectas:
  - las «circulares» F27 y F34, → Operacion quedaría en 27/30, con Wilson 0,7438: no cumpliría;
  - además las de «alcance» (F23, F24, F60), quedarían → Operacion en 26/30 y → Potestad en 27/30. Ninguno cumpliría.
- **Las fichas que deciden el resultado no entran en la lista del §5**, salvo F33: son F23, F24, F27, F34 y F60, más F33 y F45. Van
  completas en `c3/anexo_sensibilidad_c3.md`. Recomiendo que la autora las lea en C4; la decisión es suya.

## 6. Propuesta de clases (§7)

La propuesta se adjudica en C4. Las señales se midieron sobre las 907 aristas, sin leer.

- **F15 → Operacion: una regla que fija un parámetro, tomada como condición.**
  - La Condicion lleva su propio consecuente: qué plazo rige si el pago mezcla bienes de capital y otros. No restringe el acceso.
  - La señal la armé sobre el caso y solo lo encuentra a él. No hay evidencia de que sea una clase sistemática.
- **F57 → Potestad: una cláusula de indiferencia («cuenten o no»), tomada como condición.**
  - La señal marca 7 aristas: 6 → Operacion y 1 → Potestad. De las 7, 6 están sin leer.
  - Si se adjudica como clase, se puede corregir con código, filtrando la fórmula en la Condicion.
- **Correctas con anotación** (20 fichas: 13 → Operacion y 7 → Potestad). Llevan 24 anotaciones, porque algunas fichas tienen
  más de una:
  - circular: 2;
  - alcance: 3;
  - Condicion vacía (5) o trunca (1): 6;
  - tipo: 5;
  - otras: 8 (parcial 2, consecuencia fuera de la arista 2, indicador 1, contenido de una declaración jurada 1, texto
    heredado 1 y requisito como obligación de la entidad 1).
  - La señal de la clase «circular» marca 22 aristas: 19 → Operacion y 3 → Potestad. Están sin leer 20.

## 7. Límites, caso por caso

- Las 30 aristas de las tres señales (22 + 7 + 1) están en `c3/clases_c3.md`, cada una con su unidad, sus páginas, la señal que la
  marca y si fue leída en C2. Hay 4 leídas (F15, F27, F34 y F57) y 26 sin leer.
- No hay no decidibles.

## 8. Lo que queda (no es de esta sesión)

- La revisión de la mesa y C4: la revisión y la adjudicación de la autora, y la cifra final.
- El control después del re-sellado (§1): las 60 aristas están en el acta.
- El solapamiento con V, cuando exista su acta de sorteo.

## 9. Escrituras

`data/experiment/conf_matriz/`, 107 archivos:

| lugar | archivos |
|---|---|
| raíz | 5 scripts y este FRENO |
| `c1/` | acta, fichas (md y jsonl), insumos, 2 sellos y 87 PNG |
| `c2/` | planilla (jsonl y md) y sello |
| `c3/` | cifras, lista para la autora, clases (json y md) y anexo |

Los PNG se reproducen con `c1_fichas.py`, y su sha256 está en `c1/insumos_fichas_c1.json`. La autora decide si van al commit.

## 10. Controles de cierre

- **Foto del repo después:** 25.380 archivos (antes 25.273). Hay 107 nuevos, todos en `data/experiment/conf_matriz/`; 0 quitados;
  339 enlaces, como antes. Los scripts son `foto_repo.py` y `comparar_fotos.py`, en el paquete.
- **Cambiaron 5 archivos de `docs/` que esta sesión no escribió:** los modificó otro proceso mientras corría la unidad.
  - Son `checklist_pre_escalado.md`, `mandatos/UOMISIONES_COD_release_codigo_ensamblado.md`, `plan_tesis.md`,
    `protocolo_entre_tandas.md` y `tablero.md`.
  - Sus mtime van de 16:08:19 a 16:18:09, y están en el paquete.
  - No los leí ni los toqué. Quedan para que la autora los reconozca.
- **`.pyc`:** 2.213, sin cambios. La copia en el scratchpad no tiene `.pyc` ni enlaces.
- **Grep de convenciones** sobre los 20 archivos de texto de `conf_matriz/` y sobre el paquete: vacío. Lo único que aparece es la
  línea del patrón dentro del propio script, y el control positivo da lo esperado. El resultado está en el paquete.
- **Commit PENDIENTE de la autora.** Preparé el comando y no lo probé (probarlo exigiría escribir el índice):

  ```
  git -C "<repo>" add data/experiment/conf_matriz
  git -C "<repo>" commit -F <mensaje> -- data/experiment/conf_matriz
  ```

  El mensaje está en el paquete, en `uconf_matriz_mensaje_commit_preparado.txt`, sin unidades, documentos ni mecanismos.
- **Paquete:** `revision_UCONF_MATRIZ/`, en el scratchpad de la sesión, con su `manifest.txt`. Lo copié con `ditto` a
  `~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/<sesión>/scratchpad/revision_UCONF_MATRIZ/`. La verificación de los sha256 en la
  copia va en el FRENO de la sesión.
