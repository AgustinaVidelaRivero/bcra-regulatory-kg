# Checkpoint de sesión — preparación del escalado (fase A, USD 0)

Estado FINAL de la unidad. Todo lo listado en «Hecho» está en disco bajo
`data/experiment/escalado_prep/`.

## Hecho

1. **Inventario** — el índice oficial se releva desde el endpoint que alimenta
   la lista de https://www.bcra.gob.ar/ordenamiento-y-resumenes/ (la página la
   monta por JS; el JS de la vista, `Divi-BCRA/js/ordenamiento-y-resumenes-app.js`,
   la pide a `/api/endpoints/ordenamiento-y-resumenes.php?lang=es`). Respuesta
   cruda congelada en `indice_oficial_raw.json`
   (sha256 `91dc9f864f0822ce363eef6159869194c0c2f51ac878979ab62ff8b47f89fec4`).
   158 entradas → 157 URLs únicas (t-optico.pdf publicado dos veces) → 152 tras
   excluir los 5 del subset. Salidas: `inventario_tos.csv`,
   `inventario_resumen.json`.
2. **Descarga** — 152/152 PDFs en `pdfs/`, todos HTTP 200 y
   `application/pdf`, 158.912.833 bytes (`descarga_log.json`). Manifest
   `manifest_pdfs.sha256`, 152 líneas, `shasum -c` sin fallas.
3. **Referencia del subset** — `referencia_subset.json`: el driver de esta
   unidad corre el E0 sellado sobre los 5 TOs del subset y reproduce sus
   chunks byte a byte (5/5 `identicos: true` contra `salida_enm01`). Fija la
   banda de umbrales del reporte de generalización.
4. **E0 + censo en seco** — 152/152 TOs, 0 abortos. Salidas por TO en
   `e0_dry/<id>/`, agregados en `e0_dry/conteos_e0_dry.json` y
   `e0_dry/fallos_e0_dry.json` (vacío).
5. **Generalización** — `reporte_generalizacion.md` +
   `veredictos_generalizacion.json` + `causa_sin_estructura.json`.
   68 digeribles / 84 necesitan reglas; 62 de esos 84 no producen ninguna
   unidad, y 54 de los 62 por una sola causa (sin marca `-Índice-`, ninguna
   página alcanza rol `cuerpo`).
6. **Unidades y costo** — `inventario_unidades.csv`, `proyeccion_costo.json`.
   8.010 unidades visibles hoy; USD 155,70 centrales en E1+E3.
7. **Sujetos** — `catalogo_sujetos.json`, `catalogo_sujetos_resumen.csv`.
8. **Resumen legible de 6 y 7** — `resumen_escalado.md`.

## Decisiones abiertas (no se resuelven en esta unidad)

- **D5 — definición del corpus del escalado.** Los 152 TOs de
  `inventario_tos.csv` son el UNIVERSO publicado, no el corpus elegido. Qué
  subconjunto entra es decisión pendiente con los mentores.
- Qué hacer con los 84 TOs de veredicto «necesita reglas»: excluirlos,
  escribir reglas de parseo, o tratarlos como corpus de segunda vuelta. Los 53
  de régimen informativo son el bloque entero: ninguno resulta digerible.
- Ampliación del catálogo cerrado de sujetos
  (`data/experiment/grafo_v2/esquema_v2_clases.json`, 65 clases) antes de
  extraer TOs que nombran sujetos fuera de él.
- Persistencia de `e0_dry/` (≈65 MB de JSON derivado). Los PDFs quedan fuera
  de git por `.gitignore` (`data/experiment/**/*.pdf`); el registro durable de
  la descarga es `manifest_pdfs.sha256`.

## Invariantes de la unidad

- Gasto de API: **USD 0**. Ninguna llamada a LLM.
- Nada fuera de `data/experiment/escalado_prep/` se crea ni se modifica.
- El subset congelado y `reextraccion_v2/e0_chunking/` se leen; nunca se
  escriben. Los 5 PDFs del subset siguen byte-idénticos a los sha256
  registrados en `exploracion/generacion/insumos_generacion.md`.

## Cómo reproducir, en orden

```bash
cd data/experiment/escalado_prep
python3 code/construir_inventario.py
python3 code/descargar_pdfs.py
python3 code/referencia_subset.py
python3 code/correr_e0_seco.py
python3 code/reporte_generalizacion.py
python3 code/causa_sin_estructura.py
python3 code/reporte_generalizacion.py   # segunda pasada: incorpora las causas
python3 code/proyeccion_costo.py
python3 code/catalogo_sujetos.py
python3 code/resumen_escalado.py
```
