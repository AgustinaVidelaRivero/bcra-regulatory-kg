# U-DIAG-PROCESO — comandos que reproducen cada número (sesión a7ef8581)

Todos los scripts son USD 0, no llaman a la API y no usan Neo4j. Leen el repo y escriben solo en el directorio de salida que reciben. En este paquete van con el sufijo `_udiag_a7ef8581`; los comandos de abajo usan el nombre corto con que se corrieron. `R` es la raíz del repo, `S` un directorio de trabajo fuera del repo y `M` el espejo, dentro de `S`. Todo Python corre con `PYTHONDONTWRITEBYTECODE=1` y `.venv/bin/python -B`.

## 1. Espejo copiado (regla l) y e0-r2 sobre los seis TOs de las fichas

Copias sin enlaces (`find "$M" -type l` da 0):
- `data/experiment/reextraccion_v2/e0_chunking/*.py`;
- `data/experiment/r2_codigo/r5_escalera_particion.py`;
- `data/experiment/escalado_prep/pdfs/{ayccef,expaef,prevmi,lavdin,actgar,adrei}.pdf`;
- `data/experiment/segmentacion_84/b584_particion/{conteos_b584.json, los seis directorios}`;
- `data/experiment/reextraccion_v2/corpus_v2/{r1_comun.py,r1_referencias.py}`;
- `data/experiment/escalado_prep/{inventario_tos.csv,inventario_resumen.json}`;
- el worksheet;
- y, para materializar el prefijo, los `*.py` de `esq/code`, `b54_catalogo_v3/code`, `reextraccion_v2/e1_extractor` y `grafo_v2/code`, más `grafo_v2/esquema_v2_clases.json`.

```bash
cd "$M" && PYTHONDONTWRITEBYTECODE=1 "$R/.venv/bin/python" -B data/experiment/r2_codigo/r5_escalera_particion.py --correr --salida "$S/e0r2_seis" --tos ayccef,expaef,prevmi,lavdin,actgar,adrei
```

```bash
cd "$M" && PYTHONDONTWRITEBYTECODE=1 "$R/.venv/bin/python" -B estado_fichas_e0r2.py "$S" > estado_fichas_e0r2.json
```

```bash
cd "$M" && PYTHONDONTWRITEBYTECODE=1 "$R/.venv/bin/python" -B prefijo_v3.py "$M"
```

Salida de `prefijo_v3.py`: sha256 del prefijo v3 `35e88c2dd0a2920302c29005b08ab9689405606d4bd5fcf8fb7ce807b1a3c512`. Las tres frases (`prompt_e1.py:52`, `:122` y `:133`) aparecen una vez cada una, y la cabecera del mensaje con «NO extraigas contenido normativo de estos bloques» está presente.

## 2. Censos y cruces sobre material commiteado

```bash
PYTHONDONTWRITEBYTECODE=1 "$R/.venv/bin/python" -B censo_encabezados.py "$R/data/experiment/segmentacion_84/b584_particion" "$S/censo_particion.json"
```

```bash
PYTHONDONTWRITEBYTECODE=1 "$R/.venv/bin/python" -B censo_encabezados.py "$R/data/experiment/reextraccion_v2/e0_chunking/salida_tanda0" "$S/censo_tanda0.json" --plano
```

```bash
PYTHONDONTWRITEBYTECODE=1 "$R/.venv/bin/python" -B troceo_en_grafo.py "$R/data/experiment/reextraccion_v2/e0_chunking/salida_tanda0" "$R/data/experiment/reextraccion_v2/corpus_tanda0/ens_diez/r1/kg.json" "$S/troceo_en_grafo_diez.json"
```

```bash
PYTHONDONTWRITEBYTECODE=1 "$R/.venv/bin/python" -B bloques_lista_en_grafo.py "$R/data/experiment/reextraccion_v2/e0_chunking/salida_tanda0" "$R/data/experiment/reextraccion_v2/corpus_tanda0/ens_diez/r1/kg.json" "$S/bloques_lista_en_grafo_diez.json"
```

```bash
PYTHONDONTWRITEBYTECODE=1 "$R/.venv/bin/python" -B cruce_p_f1.py "$R" "$S/cruce_p_f1.json"
```

```bash
PYTHONDONTWRITEBYTECODE=1 "$R/.venv/bin/python" -B prevalencia.py "$R" "$S/prevalencia.json"
```

```bash
PYTHONDONTWRITEBYTECODE=1 "$R/.venv/bin/python" -B vinculo_cla.py "$R/data/experiment/reextraccion_v2/corpus_tanda0/ens_diez/r1/kg.json" "$S/vinculo_cla.json"
```

```bash
PYTHONDONTWRITEBYTECODE=1 "$R/.venv/bin/python" -B costos.py "$S" "$S/costos.json"
```

`costos.py` lee del directorio que recibe `censo_tanda0.json`, `censo_particion.json`, `troceo_en_grafo_diez.json` y `bloques_lista_en_grafo_diez.json`, con su nombre corto.

## 2b. Los mismos controles sobre r2a, leído en su commit (regla k)

```bash
cd "$R" && git show "f8dedd4:data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2a/r2/kg.json" > "$S/r2a/kg_diez_r2a.json"
```

```bash
cd "$R" && for f in $(git ls-tree --name-only f8dedd4 data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2/ | grep chunks_); do git show "f8dedd4:$f" > "$S/r2a/e0r2_t0/$(basename "$f")"; done
```

Después, `censo_encabezados.py` (con `--plano`), `troceo_en_grafo.py`, `bloques_lista_en_grafo.py` y `vinculo_cla.py`, con `$S/r2a/e0r2_t0` y `$S/r2a/kg_diez_r2a.json` como entradas. `costos.py` corre sobre un directorio con los dos censos y las salidas de r2a. El sha de `kg_diez_r2a.json` es `99fe2bfa0de05704e4c636bdf9b0455a30e29b378e3b0e61eadc49dad3f7c649`, igual al del archivo del árbol.

## 3. Sha de las entradas

- KG-Tanda0-Diez-r2a: `99fe2bfa…` (`f8dedd4`).
- KG-Tanda0-Diez-r1: `data/experiment/reextraccion_v2/corpus_tanda0/ens_diez/r1/kg.json`, `dd42d6d9c0c8379da90ec4ed4e4659157a960a0d1ceaf8af5a008bdd9cad9010` (`1b8916c`).
- Mandato: `docs/mandatos/UDIAG_proceso.md`, `9da456b810c773828d46f6b5c70a26dea6e4af260f8e9b7616ef66c443f6881a`, igual en `f8cf89a`.
- L-ESQ-R2 firmada: `git show 4ef7650:data/experiment/esq/enmienda_L-ESQ-R2_2026-09-30.md`, `66c4a1b9…`.
