# Enmienda 2 al protocolo entre tandas — el catálogo de sujetos no crece sin el script de re-resolución

**FIRMADA por la autora el 04/10/2026.**

Enmienda con fecha al protocolo entre tandas (`docs/protocolo_entre_tandas.md`, FIRMADO en `a304b89`; texto
firmado: las primeras 398 líneas, sha256 `b23d37c5396a…`). El protocolo no se edita: esta enmienda vive al lado
y se lee junto con él y con la enmienda del 04/10/2026 sobre la cola humana (`8d01b04`). Reemplaza la nota del
04/10/2026 sobre el crecimiento del catálogo de sujetos durante el escalado (asentada en `8d01b04`), que queda
sin efecto.

## 0. Qué enmienda y por qué

- **Lo que dice el protocolo.** No fija ninguna condición para que el catálogo de sujetos crezca durante el
  escalado. La tabla de reprocesamiento clasifica el cambio: fila F13, el catálogo que leen E4, el esqueleto y
  S19, sin abrir el armado del request; se rehace E4, el esqueleto y lo que sigue del ensamblado, en código
  (`data/experiment/mantenimiento/tabla_reprocesamiento.md:97`).
- **Lo que dice el esquema.** L-ESQ-R2 §4.2, P-d3 (`4ef7650:649`): «re-resolución por programa cuando cambia el
  sha256 del catálogo, y re-ensamblado de E2 a E5 a USD 0».
- **Lo que hay hoy.** La función que re-resuelve existe (`r1_e4.reresolver_registro`,
  `data/experiment/reextraccion_v2/corpus_v2/r1_e4.py:469-489`), pero ningún script la aplica y rehace el
  grafo: solo se usa en la suite (LN-6, `scripts/regression_kg.py:1766`) y en
  `data/experiment/r2_codigo/selftest_r3.py`. `data/experiment/catalogo_unico/code/reresolver_tanda0.py`
  calcula la re-resolución y no escribe nada. En la tanda 0 hay 40 filas en cuarentena en el registro de
  KG-Tanda0-Diez-r2a y 26 en el de KG-Tanda0-Desarrollo-r2a (`no_mapeados_sujetos.jsonl`, campo `estado`).
- **Por qué una enmienda.** Agrega una obligación nueva a un texto firmado.

## 1. Qué decide

1. Antes del primer crecimiento del catálogo de sujetos durante el escalado tiene que existir, con su prueba,
   el script que:
   - toma el catálogo nuevo;
   - re-resuelve el registro de sujetos en cuarentena;
   - rehace el grafo desde el crudo guardado, a USD 0;
   - y lo verifica.
2. La prueba incluye un id agregado al catálogo que resuelve una mención hoy en cuarentena.
3. Mientras el script no exista y su prueba no pase, el catálogo no crece.
4. Lo construye una unidad propia, de USD 0, sobre el commit de C2 de U-R2-CODIGO-2
   (`docs/mandatos/URERESOL_CAT_reresolucion_catalogo.md`; BORRADOR — PENDIENTE DE FIRMA al 04/10/2026).

## 2. Qué no cambia

- El texto del protocolo, sus demás notas y la enmienda sobre la cola humana.
- El catálogo de sujetos de r2 y sus candados: esta enmienda no agrega ningún id.
- El criterio de admisión de ids de L-ESQ-R2 §7 (`4ef7650:861`).

## Firma

FIRMADA por la autora el 04/10/2026. Rige desde esta firma.
