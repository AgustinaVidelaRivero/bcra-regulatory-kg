# Preparar `run_3_refinamiento/` — prerrequisito del Paso 2

Procedimiento para crear la copia de trabajo del grafo ganador. El Paso 2 de la
skill da la copia por existente; **al estado verificado abajo, NO existe** — hay
que crearla una única vez con este procedimiento.

> **Estado verificado:** citas `archivo:línea` y ausencia de la copia verificadas
> contra el repo el 2026-07-06 (HEAD `454bd9d`, 2026-06-28, más working tree sin
> commitear).

> **⚠ Dependencia entre skills:** el paso 3 de este procedimiento delega en una
> reference de OTRA skill:
> `.claude/skills/llm-capture/references/extender-run-files.md`.
> Vive allá porque el sub-procedimiento "agregar una clave a `RUN_FILES` +
> implicancias sobre `code_version`/caché" se repite para cualquier fuente de
> datos nueva, no solo para esta copia. Si la skill `llm-capture` se renombra o
> mueve, actualizar este path — y viceversa: si este archivo se mueve, revisar
> las menciones cruzadas en aquella skill.

## Aprobación previa (bloqueante)

El paso 3 requiere editar `loader.py`, que solo se modifica **una sola vez y con
aprobación explícita de la autora** (regla del non-goal de `llm-capture`, porque
`loader.py` integra el hash `code_version` que invalida toda la caché automática).
**No arrancar sin esa aprobación.**

## Procedimiento

1. **Crear la carpeta y copiar SOLO el `kg.json`.**
   Origen: `data/experiment/run_3_ppf_core/kg.json` (la ruta que consume el
   pipeline, `data/experiment/evaluacion/loader.py:60`).
   Destino: `data/experiment/run_3_refinamiento/kg.json`.
   Los demás archivos de `run_3_ppf_core/` (`code/`, `kg_visual.html`,
   `report.md`, `schema.md`) NO se copian: el pipeline solo consume el `kg.json`.

2. **Registro de creación** (auditable, dentro de la carpeta nueva, p. ej.
   `run_3_refinamiento/ORIGEN.md`): sha256 del origen y de la copia (**deben
   coincidir** — la copia nace byte-idéntica), fecha, y commit del repo al
   momento de crearla.

   ```bash
   shasum -a 256 data/experiment/run_3_ppf_core/kg.json data/experiment/run_3_refinamiento/kg.json
   ```

3. **Cablear el loader** siguiendo
   `.claude/skills/llm-capture/references/extender-run-files.md` (procedimiento
   completo + las 4 implicancias sobre caché). Datos específicos de ESTA copia:
   - Clave nueva en `RUN_FILES`: `"run_3_refinamiento"` →
     `EXPERIMENT_DIR / "run_3_refinamiento" / "kg.json"`
     (`data/experiment/evaluacion/loader.py:57-64`).
   - Entrada en `ADAPTERS`: **la misma config que `run_3`**, porque la copia
     tiene el mismo schema:
     `{"node_extra": ("top", "additional_provenance"), "edge_extra": None}`
     (`data/experiment/evaluacion/loader.py:73-74`).

4. **Validar:** desde `data/experiment/evaluacion/`, con el venv de la raíz:
   `python runners/validate_loader.py`. La clave nueva entra sola al barrido (itera
   `RUN_KEYS`, `data/experiment/evaluacion/runners/validate_loader.py:180`)
   y debe pasar C1–C8 con **conteos idénticos a `run_3`** (misma cantidad de
   nodos y edges: es una copia byte-idéntica). Exit code 0.

5. **Entender el estado de la caché antes de correr nada:** mientras la copia no
   difiera del original ni en un byte, comparte `graph_fingerprint` (y por lo
   tanto namespace de caché) con `run_3` — correr sobre ella replaya gratis, y un
   "side-by-side original vs copia" no compara nada real. El namespace separado
   que necesita el Paso 5 nace recién con el primer cambio de contenido. Detalle:
   implicancia 4 de `extender-run-files.md`.

## Qué NO hace este procedimiento

- **NO aplica ningún cambio al grafo.** Poblar nodos, crear aristas, corregir
  provenance es el Paso 4–5 de la skill, con su enrutamiento por riesgo.
- **NO toca los otros 4 grafos** ni el `run_3` original (baseline inmutable).
- **NO promueve la copia** al lugar del original — eso es una decisión explícita
  y registrada de la autora, si algún día un refinamiento la amerita.
- **NO commits** — los maneja la autora.

## Self-check

```bash
cd data/experiment/evaluacion
python runners/validate_loader.py        # C1–C8 en verde para run_3_refinamiento, exit 0
python runners/run_posthoc.py --selftest # 14 checks; loader + cadena de caché sanos tras la edición
```

Y confirmar en el output de `runners/validate_loader.py` que `run_3` y
`run_3_refinamiento` reportan conteos idénticos de nodos y edges.
