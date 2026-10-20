#!/bin/zsh
# B6.1, tanda final, T3, punto 4: shapes y suite sobre los ocho grafos, con gate_tf.sh, en la copia (nunca el repo), uno detrás de otro:
#   - shapes con la E0 de cada grafo y la suite: t3/gate/e0_del_grafo/<grafo>/;
#   - shapes con la E0 con las partes por corte (la que rige para S31; e0_partes_tf.py): t3/gate/e0_con_partes/<grafo>/.
# Todas las rutas, relativas a la raíz de la copia (gate_tf.sh corre desde ahí), para que las salidas no lleven la ruta de la copia.
# USD 0, sin API.
# Uso: zsh lote_gate_tf.sh <python> <copia> <gate_tf.sh> [<grafo> ...]   (sin grafos, los ocho; con ellos, solo esos)
set -u
PY="$1"; C="$2"; GT="$3"; shift 3; SOLO=("$@")
X=data/experiment/reextraccion_v2; T=$X/corpus_tanda_final; A=data/experiment/tanda_final/t3/acumulado
P=data/experiment/tanda_final/t3/e0_con_partes; G=data/experiment/tanda_final/t3/gate; EF=$X/e0_chunking/salida_tanda_final_r2b
corre() {  # <grafo> <ensamblado> <E0 del grafo> <E0 con las partes>
  (( ${#SOLO} == 0 )) || (( ${SOLO[(Ie)$1]} )) || return 0
  print -r -- "$1 inicio $(date '+%H:%M:%S')"
  bash "$GT" "$PY" "$C" "$2" "$3" "$G/e0_del_grafo/$1" ambas
  bash "$GT" "$PY" "$C" "$2" "$4" "$G/e0_con_partes/$1" shapes
  print -r -- "$1 fin $(date '+%H:%M:%S') | $(tail -1 "$C/$G/e0_del_grafo/$1/consola_shapes.txt") $(tail -1 "$C/$G/e0_del_grafo/$1/consola_suite.txt") $(tail -1 "$C/$G/e0_con_partes/$1/consola_shapes.txt")"
}
corre tf98 $T/ens_98_r2b $EF $P/tanda_final_corrida1
corre tf98_sincola $T/ens_98_r2b_sincola $EF $P/tanda_final_corrida1
corre tf_tramo1 $T/ens_tramo1_r2b $EF $P/tanda_final_corrida1
corre tf_tramo1_sincola $T/ens_tramo1_r2b_sincola $EF $P/tanda_final_corrida1
corre acum128 $A/ens_128_r2b $A/e0_acumulado_128_r2b $P/acum128_corrida1
corre acum128_sincola $A/ens_128_r2b_sincola $A/e0_acumulado_128_r2b $P/acum128_corrida1
corre acum60 $A/ens_60_tramo1_r2b $A/e0_acumulado_60_r2b $P/acum60_corrida1
corre acum60_sincola $A/ens_60_tramo1_r2b_sincola $A/e0_acumulado_60_r2b $P/acum60_corrida1
print -r -- "fin del lote $(date '+%H:%M:%S')"
