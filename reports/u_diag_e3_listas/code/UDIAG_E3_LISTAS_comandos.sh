#!/bin/zsh
# U-DIAG-E3-LISTAS: reproduce las cifras del FRENO sobre una copia de 723680e armada con git archive (sin enlaces
# simbólicos; no escribe en el repo). Uso: UDIAG_E3_LISTAS_comandos.sh <repo> <paquete> <dir_trabajo>
# La hora del sorteo de fase2_resumen.json sale nueva: los ids sorteados son los mismos (semilla fija).
set -eu
REPO="$1"; PAQ="$2"; W="$3"
REV=723680e
C="$W/copia_head"; O="$W/salida"
mkdir -p "$C" "$O"
evpy=($(git -C "$REPO" ls-tree -r --name-only "$REV" data/experiment/evaluacion | grep -E '^data/experiment/evaluacion/[^/]+\.py$'))
gv=($(git -C "$REPO" ls-tree -r --name-only "$REV" data/experiment/grafo_v2/code | grep -E '^data/experiment/grafo_v2/code/[^/]+\.(py|json)$'))
paths=(data/experiment/reextraccion_v2/e1_extractor data/experiment/reextraccion_v2/e3_verificador
       data/experiment/reextraccion_v2/e0_chunking data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b
       data/experiment/b54_catalogo_v3 data/experiment/catalogo_unico data/experiment/pyd_r2 data/experiment/reext_t0
       data/experiment/mantenimiento docs/mandatos data/experiment/reextraccion_v2/corpus_v2 data/experiment/esq
       data/experiment/grafo_v2/esquema_v2_clases.json "${evpy[@]}" "${gv[@]}")
git -C "$REPO" archive "$REV" "${paths[@]}" | tar -x -C "$C"
echo "enlaces simbólicos en la copia: $(find "$C" -type l | wc -l | tr -d ' ')"
for f in fase1_items_e3.py fase2_candidatos_y_generalidad.py escribir_adjudicacion.py fase3_efecto.py \
         ubicar_citas_29.py fase4_29_y_costo.py control_por_to.py ficha.py; do
  cp "$PAQ/udiag_e3_listas_$f" "$W/$f"
done
export PYTHONDONTWRITEBYTECODE=1
PY="$REPO/.venv/bin/python"
cd "$W"
"$PY" -B fase1_items_e3.py "$C" "$O"
"$PY" -B fase2_candidatos_y_generalidad.py "$C" "$O"
"$PY" -B escribir_adjudicacion.py "$O"
"$PY" -B fase3_efecto.py "$C" "$O"
"$PY" -B ubicar_citas_29.py "$C" "$O"
"$PY" -B fase4_29_y_costo.py "$O"
"$PY" -B control_por_to.py "$C" "$O"
for f in fase1_resumen.json fase1_unidades.json fase1_candidatos.json fase2_candidatos_extra.json fase2_indicador.json \
         adjudicacion_candidatos.json adjudicacion_muestra.json fase3_efecto.json ubicacion_citas_29_items.json \
         fase4_29_y_costo.json control_por_to.json; do
  if cmp -s "$O/$f" "$PAQ/UDIAG_E3_LISTAS_$f"; then echo "igual $f"; else echo "DIFIERE $f"; fi
done
