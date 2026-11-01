#!/bin/bash
# juez de tripletas v3 — el análisis de las 400 con la hoja de adjudicación de la autora (USD 0; lo lanza la autora después de
# las 200, solo si la v3 mandó alguna a adjudicación y la hoja ya tiene su sello). Le pasa el sello y su sha256 al comando
# sellado del análisis, v3/comandos/analisis_400_juez_v3.sh, sin cambiar ese archivo: corre su texto con sus dos renglones
# SELLO_ADJ="PENDIENTE" y SELLO_ADJ_SHA="PENDIENTE" llenos con los argumentos, y nada más cambiado. Su $0 es la ruta del
# comando sellado, así que lee sus listas, sus carpetas y su código como siempre. El comando hace todos sus controles (las
# listas de las etapas a, b, c y d, la congelación, las 200 corridas, la entrada de las 400 y los sellos de las dos lecturas)
# y llama al análisis con --sello-adjudicacion-200 y su sha256; el análisis controla el sello, la hoja y sus refs antes de
# leerla. Así nada sellado cambia después de que exista un veredicto de la v3.
#
# Frena, sin correr el comando, si:
#   - no van los tres argumentos; el sello no es un archivo; su sha256 no son 64 caracteres hexadecimales; o la ruta del sello
#     trae comillas, $, acento grave, barra invertida o un salto de renglón;
#   - están las variables de prueba del sello del comando, que pisarían el que va por argumento;
#   - la lista de la etapa d de HEAD no nombra el comando una sola vez, la lista local no es, byte a byte, la de HEAD, o el
#     comando no da el sha256 de la lista;
#   - el comando no trae una sola vez cada renglón de PENDIENTE, o su texto leído no da, byte a byte, el sha256 del archivo.
# Salida: la del comando (0 escrito; 1 un freno; 2 adjudicaciones pendientes); 64 uso o variables de prueba del sello.
#
# Uso:  bash data/experiment/tripletas_v/juez_v3/adjudicacion_200/lanzar_analisis_400_con_la_hoja_v3.sh \
#         <el JSON de las 400 de la mesa> <el sello de la hoja de adjudicación> <el sha256 del sello>
# Para la corrida en seco, dentro de un arenero, las variables de prueba del comando las lee el comando (no las del sello).
set -euo pipefail
if [ $# -ne 3 ]; then
  echo "uso: bash $0 <el JSON de las 400 de la mesa> <el sello de la hoja de adjudicación> <el sha256 del sello>"
  exit 64
fi
ENTRADA_400="$1"
SELLO="$2"
SELLO_SHA="$3"
REPO="$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg"
V3="$HOME/INGENIERIA IA/TESIS/fuera_del_repo/tripletas_v_juez/v3"
COMANDO="$V3/comandos/analisis_400_juez_v3.sh"
LISTA_REL="data/experiment/tripletas_v/juez_v3/etapa_d_juez_v3_sha256.txt"
NL='
'
# 1. los argumentos
if [ -n "${V3_SELLO_ADJ_SOLO_PRUEBA:-}${V3_SELLO_ADJ_SHA256_SOLO_PRUEBA:-}" ]; then
  echo "FRENO: las variables de prueba del sello del comando pisarían el sello que va por argumento"; exit 64
fi
[ -f "$SELLO" ] || { echo "FRENO: el sello de la hoja de adjudicación no es un archivo"; exit 1; }
[[ "$SELLO_SHA" =~ ^[0-9a-f]{64}$ ]] || { echo "FRENO: el sha256 del sello no son 64 caracteres hexadecimales"; exit 1; }
case "$SELLO" in
  *'"'*|*'$'*|*'`'*|*'\'*|*"$NL"*) echo "FRENO: la ruta del sello trae comillas, \$, acento grave, barra invertida o un salto"; exit 1 ;;
esac
# 2. el comando sellado: el de la lista de la etapa d de HEAD, que es, byte a byte, la local
RE_CMD='^[0-9a-f]{64}  comandos/analisis_400_juez_v3\.sh$'
N_CMD="$(git -C "$REPO" --no-optional-locks show "HEAD:$LISTA_REL" | grep -cE "$RE_CMD" || true)"
[ "$N_CMD" = "1" ] || { echo "FRENO: la lista de la etapa d de HEAD no nombra el comando del análisis una sola vez"; exit 1; }
ESP="$(git -C "$REPO" --no-optional-locks show "HEAD:$LISTA_REL" | grep -E "$RE_CMD" | cut -c1-64)"
cmp -s "$V3/lista_etapa_d.txt" <(git -C "$REPO" --no-optional-locks show "HEAD:$LISTA_REL") || {
  echo "FRENO: la lista local de la etapa d no es, byte a byte, la de HEAD"; exit 1; }
[ "$(shasum -a 256 "$COMANDO" | cut -c1-64)" = "$ESP" ] || { echo "FRENO: el comando del análisis no da el sha256 de la lista"; exit 1; }
# 3. su texto, con sus dos renglones de PENDIENTE llenos y nada más
TEXTO=""
ORIGINAL=""
N1=0
N2=0
while IFS= read -r L || [ -n "$L" ]; do
  ORIGINAL+="$L$NL"
  if [ "$L" = 'SELLO_ADJ="PENDIENTE"' ]; then
    L="SELLO_ADJ=\"$SELLO\""; N1=$((N1 + 1))
  elif [ "$L" = 'SELLO_ADJ_SHA="PENDIENTE"' ]; then
    L="SELLO_ADJ_SHA=\"$SELLO_SHA\""; N2=$((N2 + 1))
  fi
  TEXTO+="$L$NL"
done < "$COMANDO"
[ "$N1" = "1" ] && [ "$N2" = "1" ] || { echo "FRENO: el comando no trae una sola vez cada renglón de PENDIENTE"; exit 1; }
[ "$(printf '%s' "$ORIGINAL" | shasum -a 256 | cut -c1-64)" = "$ESP" ] || {
  echo "FRENO: el texto leído no da, byte a byte, el sha256 del comando sellado"; exit 1; }
# 4. el comando, con el sello
echo "el comando del análisis da el sha256 de la lista de la etapa d de HEAD; corre con sus dos renglones de PENDIENTE llenos"
RC=0
bash -c "$TEXTO" "$COMANDO" "$ENTRADA_400" || RC=$?
exit "$RC"
