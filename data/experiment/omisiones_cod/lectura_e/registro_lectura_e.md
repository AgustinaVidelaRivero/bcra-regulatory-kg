# U-OMISIONES-COD, (e): la lectura de las 16 detecciones fuera de T4 (mesa, 10/10/2026)

Lectura a ciegas de la precisión del clasificador de copia de la nota de E3, el ítem (e) de la v7
(`docs/mandatos/UOMISIONES_COD_release_codigo_ensamblado.md`), con la regla de sus notas al pie del 10/10/2026 (`3c5f003` y `521e220`).
USD 0, sin API.

## La muestra y la carpeta del lector

- **Las 16 detecciones** del clasificador fuera de las 64 unidades de copia de nota que leyó T4, en 15 unidades. Salen de la lista
  sellada de O1, `o1/salidas/e_lista_sellada/detecciones_e_copia_nota_diez.json` (sha256 `4c385529…`). Se leen las 16 (nota de
  `3c5f003`, decisión 5).
- **La carpeta del lector** (`~/INGENIERIA IA/TESIS/fuera_del_repo/lecturas_ciegas/lectura_campos_nota/`) la armó la mesa con
  `armar_paquete_lector_e_mesa.py`: los casos (`casos_lectura_e.jsonl`), sus páginas, las instrucciones, la planilla vacía y el script del
  sello, con su manifiesto (`manifest_carpeta_lector_lectura_e.txt`). Los casos no llevan la clase del clasificador. El mapa de cada caso
  a su detección quedó fuera de la carpeta (`control_paquete_lector_e_mesa.json`).
- **Las clases** (`instrucciones_lector_lectura_e.md`): 1 y 3, copia real; 2, coincidencia legítima; 4, dudosa. Una detección es correcta
  si el caso es una copia real (clases 1 y 3), incorrecta si es una coincidencia legítima (clase 2), y dudosa con la clase 4.

## Las sesiones

- **La primera sesión se abrió por error en `fuera_del_repo/`,** no en la carpeta del lector, y la autora la cerró. Su transcripción
  (sesión `ed2f95b0…`, sha256 `8ee65055efce490d8346a088346b01e0ea8507baaa514ed00186d0268bba5e70`) tiene 2 llamadas, de 00:54:22 a
  00:54:41 del 10/10/2026, las dos fuera de la carpeta de la lectura:
  1. `ls -la` de `fuera_del_repo/` y `shasum -a 256 -c manifest.txt`, que falló porque ahí no hay manifiesto;
  2. un `find` de profundidad 3 que buscó cuatro nombres de archivo y devolvió 7 rutas, en las dos carpetas de `lecturas_ciegas/`.

  Vio nombres; no abrió ningún archivo ni escribió nada. Frenó en el paso 1 y declaró que no elegía carpeta por su cuenta. Sus llamadas
  están en `llamadas_sesion_abierta_por_error_lectura_e.txt`, armado con `llamadas_sesion_mesa.py`. Efecto sobre la lectura: ninguno que
  se pueda medir.
- **La lectura** la hizo una sesión nueva, abierta en la carpeta del lector.

## El sello

- `planilla_lectura_e_sellada.jsonl`: sha256 `b43abf6178946e1873bfc4ea2e8dfedf0e03f67af0fa899c2e76966a17f05b90`, igual al de
  `sello_planilla_lectura_e.txt`; 16 filas, selladas el 2026-10-10T01:01:26-03:00.
- La carpeta del lector: los 19 archivos de partida que no son la planilla siguen iguales a su manifiesto, y se agrega el sello
  (`calcular_e_mesa.py` lo controla antes de contar).
- **El orden:** la autora decidió cómo cuentan las dudosas antes de despachar la lectura. La nota que lo asienta se escribió en el árbol de
  trabajo a las 00:58:37, antes del sello (01:01:26), y se commiteó en `521e220a`, a las 07:50, después. La mesa abrió la planilla recién
  con `521e220a` en el log.

## La cifra

`python3 -I -B calcular_e_mesa.py <carpeta del lector> control_paquete_lector_e_mesa.json resultado_e.json` (`resultado_e.json`):

| clase | casos |
|---|---:|
| 1, copia real (metalenguaje del verificador) | 0 |
| 2, coincidencia legítima | 3 |
| 3, copia real (palabra ajena a la unidad) | 10 |
| 4, dudosa | 3 |
| total | 16 |

- Correctas, 10; incorrectas, 3; dudosas, 3, excluidas. Decididas, 13.
- Límite inferior de Wilson al 95 %: 10 de 13 da **0,4974**. El piso es 0,75; con 13 decididas hacían falta 13 de 13.
- **No llega al piso.**

## Lo que sigue

- **(e) queda como límite declarado** (v7, nota del 09/10/2026 sobre el umbral: «Si no pasa, (e) queda como límite declarado»). Su
  código no se aplica en O2. La revisión de las incorrectas por la autora rige solo si pasa, así que no corre.
- **Caso por caso** (planilla, con la razón del lector en cada fila):
  - **las 10 copias reales** que el clasificador detectó quedan en el grafo sin corregir: `cap::2.12.10::intro` e1 descripción,
    `cap::2.12.11` e1 descripción, `cap::2.2.2` e1 descripción, `cla::10.4` e3 etiqueta, `cla::2.2.3` e1 descripción, `docvig::2.2.3` op1
    descripción, `docvig::3.3.1` e3 descripción y etiqueta, `ext::10.3.3` e1 descripción y `ric::5.1.2` e4 etiqueta;
  - **las 3 coincidencias legítimas** (detecciones falsas): `cap::12.3` e1 etiqueta, `ext::7.11.2::intro` e2 descripción y
    `lingob::6.2.3` e1 etiqueta;
  - **las 3 dudosas** (fórmulas de remisión que la norma dice con otras palabras): `ext::3.6.4.1` e4 etiqueta, `ext::7.9.2.1` e3
    descripción y `ext::9.3.3::intro` e5 descripción.
