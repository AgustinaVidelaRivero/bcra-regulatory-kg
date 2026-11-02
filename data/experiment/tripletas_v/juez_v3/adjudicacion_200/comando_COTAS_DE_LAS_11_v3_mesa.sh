#!/bin/bash
# Las dos cotas de las 11 (mesa, §405, 02/11/2026; nota del 257 en el pre-registro de tripletas): la cifra de las 400 del análisis
# de la v3 con las 11 adjudicadas todas correctas y todas incorrectas. USD 0; lo corre la autora.
# Corre dos veces el texto del comando sellado del análisis (v3/comandos/analisis_400_juez_v3.sh), con todos sus controles tal
# cual y tres cambios: sus dos renglones de PENDIENTE, llenos con un sello sintético, y --salida en analisis_400_cotas/<caso>/ al
# final del renglón de la llamada. Llama al mismo analisis_400_v3.py. No toca analisis_400_v3.json, el lanzador, el comando ni
# el análisis.
#
# Frena, sin escribir nada, si:
#   - no va la entrada de las 400 (64);
#   - están las variables de prueba del sello del comando, que pisarían el sello sintético (64);
#   - una variable de prueba corre fuera de su arenero (64);
#   - el lanzador de HEAD no da dfa9fb74…, o el del árbol de trabajo no es el de HEAD;
#   - analisis_400_v3.json no está o no da 2b16f8ac…;
#   - la lista de la etapa d de HEAD no nombra una sola vez el comando o el análisis, la local no es la de HEAD, o el comando o el
#     análisis no dan su sha256 de la lista;
#   - el comando no trae una sola vez cada renglón de PENDIENTE y el de la llamada, o su texto leído no da su sha256;
#   - analisis_400_cotas/ ya existe.
# Si una de las dos corridas frena, sale con lo que dé el comando sellado (1 un freno). Lo escrito hasta ahí queda: para volver a
# correrlo, la carpeta analisis_400_cotas/ se mueve antes.
# Qué deja, en corridas/analisis_400_cotas/: hojas_sinteticas/<caso>/ (la hoja y su sello) y <caso>/analisis_400_v3.json, con <caso>
# todas_correctas y todas_incorrectas. La consola no da ninguna cifra.
# Salida: 0 las dos escritas; 1 un freno; 2 el análisis dice que hay adjudicaciones pendientes (no debería pasar); 64 uso o
# variables de prueba.
#
# Uso:  bash comando_COTAS_DE_LAS_11_v3_mesa.sh <el JSON de las 400 de la mesa>
# Solo para la prueba, dentro de un arenero ($HOME en */areneros_v3_*/home): COTAS_SALIDA_400_SHA256_SOLO_PRUEBA (el sha256 del
# analisis_400_v3.json de juguete), COTAS_SELLO_MAL_SOLO_PRUEBA (sha o refs: arma mal el sello sintético) y V3_SALIDA_SOLO_PRUEBA
# (las corridas de juguete). Las demás V3_*_SOLO_PRUEBA las lee el comando sellado.
set -euo pipefail
if [ $# -ne 1 ]; then
  echo "uso: bash $0 <el JSON de las 400 de la mesa>"
  exit 64
fi
ENTRADA_400="$1"
REPO="$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg"
V3="$HOME/INGENIERIA IA/TESIS/fuera_del_repo/tripletas_v_juez/v3"
COMANDO="$V3/comandos/analisis_400_juez_v3.sh"
LANZ_REL="data/experiment/tripletas_v/juez_v3/adjudicacion_200/lanzar_analisis_400_con_la_hoja_v3.sh"
LANZ_SHA="dfa9fb7497f7dea6044820573ef28bcb6bdac9bf7e1d0fc5ce90857872fa0380"
LISTA_REL="data/experiment/tripletas_v/juez_v3/etapa_d_juez_v3_sha256.txt"
SAL400_SHA="2b16f8acee3c2b5854da62ae68a633e0bf9ac09be2377eaf1a99766349a8dad3"
CORRIDAS="$V3/corridas"
MAL=""
REFS="T105 T109 T150 T152 T195 T196 T203 T208 T250 T261 T273"
LLAMADA='  --sello-lectura-v3-sha256 "$SELLO_V3_SHA" --registro "$AQUI/congelacion/regla_de_freno_congelacion_v3.json" '
LLAMADA+='${ADJ[@]+"${ADJ[@]}"}'   # el renglón 90 del comando sellado, tal cual, en dos partes
NL='
'
# 0. las variables de prueba
if [ -n "${V3_SELLO_ADJ_SOLO_PRUEBA:-}${V3_SELLO_ADJ_SHA256_SOLO_PRUEBA:-}" ]; then
  echo "FRENO: las variables de prueba del sello del comando pisarían el sello sintético"; exit 64
fi
if [ -n "${COTAS_SALIDA_400_SHA256_SOLO_PRUEBA:-}${COTAS_SELLO_MAL_SOLO_PRUEBA:-}${V3_SALIDA_SOLO_PRUEBA:-}" ]; then
  [[ "$HOME" == */areneros_v3_*/home ]] || { echo "FRENO: las variables de prueba no corren fuera de su arenero"; exit 64; }
  SAL400_SHA="${COTAS_SALIDA_400_SHA256_SOLO_PRUEBA:-$SAL400_SHA}"
  MAL="${COTAS_SELLO_MAL_SOLO_PRUEBA:-}"
  CORRIDAS="${V3_SALIDA_SOLO_PRUEBA:-$CORRIDAS}"
fi
COTAS="$CORRIDAS/analisis_400_cotas"
SAL400="$CORRIDAS/analisis_400/analisis_400_v3.json"
case "$COTAS" in
  *'"'*|*'$'*|*'`'*|*'\'*|*"$NL"*) echo "FRENO: la ruta de las cotas trae comillas, \$, acento grave, barra invertida o un salto"; exit 1 ;;
esac
# 1. lo que existe no cambió
[ "$(git -C "$REPO" --no-optional-locks show "HEAD:$LANZ_REL" | shasum -a 256 | cut -c1-64)" = "$LANZ_SHA" ] || {
  echo "FRENO: el lanzador de HEAD no es el del 255"; exit 1; }
[ "$(shasum -a 256 "$REPO/$LANZ_REL" | cut -c1-64)" = "$LANZ_SHA" ] || {
  echo "FRENO: el lanzador del árbol de trabajo no es el de HEAD"; exit 1; }
[ -f "$SAL400" ] && [ "$(shasum -a 256 "$SAL400" | cut -c1-64)" = "$SAL400_SHA" ] || {
  echo "FRENO: analisis_400_v3.json no está o cambió"; exit 1; }
LISTA="$(git -C "$REPO" --no-optional-locks show "HEAD:$LISTA_REL")"
cmp -s "$V3/lista_etapa_d.txt" <(git -C "$REPO" --no-optional-locks show "HEAD:$LISTA_REL") || {
  echo "FRENO: la lista local de la etapa d no es, byte a byte, la de HEAD"; exit 1; }
for N in comandos/analisis_400_juez_v3.sh codigo/analisis_400_v3.py; do
  [ "$(printf '%s\n' "$LISTA" | awk -v n="$N" '$2 == n {c++} END {print c + 0}')" = "1" ] || {
    echo "FRENO: la lista de la etapa d de HEAD no nombra $N una sola vez"; exit 1; }
  ESP="$(printf '%s\n' "$LISTA" | awk -v n="$N" '$2 == n {print $1}')"
  [ "$(shasum -a 256 "$V3/$N" | cut -c1-64)" = "$ESP" ] || { echo "FRENO: $N no da el sha256 de la lista de la etapa d"; exit 1; }
done
ESP_CMD="$(printf '%s\n' "$LISTA" | awk '$2 == "comandos/analisis_400_juez_v3.sh" {print $1}')"
ORIGINAL=""
N1=0
N2=0
N3=0
while IFS= read -r L || [ -n "$L" ]; do
  ORIGINAL+="$L$NL"
  if [ "$L" = 'SELLO_ADJ="PENDIENTE"' ]; then N1=$((N1 + 1)); fi
  if [ "$L" = 'SELLO_ADJ_SHA="PENDIENTE"' ]; then N2=$((N2 + 1)); fi
  if [ "$L" = "$LLAMADA" ]; then N3=$((N3 + 1)); fi
done < "$COMANDO"
[ "$N1" = "1" ] && [ "$N2" = "1" ] && [ "$N3" = "1" ] || {
  echo "FRENO: el comando no trae una sola vez cada renglón de PENDIENTE y el de la llamada"; exit 1; }
[ "$(printf '%s' "$ORIGINAL" | shasum -a 256 | cut -c1-64)" = "$ESP_CMD" ] || {
  echo "FRENO: el texto leído del comando no da, byte a byte, su sha256"; exit 1; }
# 2. no pisa
[ ! -e "$COTAS" ] || { echo "FRENO: analisis_400_cotas ya existe: no se pisa"; exit 1; }
echo "los controles de antes pasan: el lanzador, analisis_400_v3.json, la lista de la etapa d, el comando y el análisis"
# 3. las dos corridas, cada una con su hoja sintética y su sello
for CASO in todas_correctas todas_incorrectas; do
  VER="${CASO#todas_}"
  VER="${VER%s}"
  D="$COTAS/hojas_sinteticas/$CASO"
  mkdir -p "$D"
  {
    echo "ref,veredicto"
    for R in $REFS; do
      if [ "$MAL" = "refs" ] && [ "$R" = "T273" ]; then continue; fi
      echo "$R,$VER"
    done
  } > "$D/adjudicacion_200.csv"
  HS="$(shasum -a 256 "$D/adjudicacion_200.csv" | cut -c1-64)"
  if [ "$MAL" = "sha" ]; then HS="$(printf '%064d' 0)"; fi
  printf '# sello sintético de las cotas de las 11 (mesa, §405): %s\n%s  adjudicacion_200.csv\n' "$CASO" "$HS" \
    > "$D/sello_adjudicacion_200.txt"
  SS="$(shasum -a 256 "$D/sello_adjudicacion_200.txt" | cut -c1-64)"
  TEXTO=""
  while IFS= read -r L || [ -n "$L" ]; do
    if [ "$L" = 'SELLO_ADJ="PENDIENTE"' ]; then
      L="SELLO_ADJ=\"$D/sello_adjudicacion_200.txt\""
    elif [ "$L" = 'SELLO_ADJ_SHA="PENDIENTE"' ]; then
      L="SELLO_ADJ_SHA=\"$SS\""
    elif [ "$L" = "$LLAMADA" ]; then
      L="$L --salida \"$COTAS/$CASO\""
    fi
    TEXTO+="$L$NL"
  done < "$COMANDO"
  RC=0
  bash -c "$TEXTO" "$COMANDO" "$ENTRADA_400" || RC=$?
  [ "$RC" = "0" ] || { echo "FRENO: la corrida de $CASO salió con $RC; lo escrito hasta ahí queda en analisis_400_cotas/"; exit "$RC"; }
  [ -f "$COTAS/$CASO/analisis_400_v3.json" ] || { echo "FRENO: la corrida de $CASO no dejó su salida"; exit 1; }
  echo "cotas: $CASO escrito | sha256 $(shasum -a 256 "$COTAS/$CASO/analisis_400_v3.json" | cut -c1-64)"
done
# 4. lo que existía, igual
[ "$(shasum -a 256 "$SAL400" | cut -c1-64)" = "$SAL400_SHA" ] || { echo "FRENO: analisis_400_v3.json cambió"; exit 1; }
echo "FIN: las dos cotas, escritas en analisis_400_cotas/; analisis_400_v3.json igual; la consola no da ninguna cifra"
