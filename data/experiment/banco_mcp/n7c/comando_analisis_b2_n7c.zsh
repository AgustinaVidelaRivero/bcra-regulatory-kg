#!/bin/zsh
# comando_analisis_b2_n7c.zsh — PREPARADO (N7c, etapa C2-bis). El análisis de B2 de N7c (n7c/analizar_n7c.py), que corre la
# autora desde su Terminal, desde el repo, después de B2. USD 0: ninguna llamada a la API (no pasa la clave).
#
# Qué tiene que estar: la salida de B2 (~/INGENIERIA IA/TESIS/fuera_del_repo/banco_n7c/, con su juez), el .venv del repo y el
# venv del codificador (~/INGENIERIA IA/TESIS/venvs/banco_vector_py312: el instrumento de citas y el lector de la enmienda 1 corren
# con su Python 3.12). No hace falta el Neo4j.
# Pasos y códigos de salida:
#   0. los sha256 de N7c y N7c+ (HEAD y árbol): 20 si alguno no da;
#   1. n7c/analizar_n7c.py: 0 terminó (imprime solo cuentas, fracciones y sí o no, y la configuración que adopta la regla);
#      8 si la entrada no da (cargar_entrada); 1 si algo aborta (el lector, el instrumento, una salida dentro del repo).
#      Salida: ~/INGENIERIA IA/TESIS/fuera_del_repo/banco_n7c/analisis/analisis_b2_n7c.json.
# Gasto: USD 0.
# Uso: zsh data/experiment/banco_mcp/n7c/comando_analisis_b2_n7c.zsh
set -u
D=${0:A:h}                                   # data/experiment/banco_mcp/n7c
R=${D:h:h:h:h}                               # la raíz del repo
PY="$R/.venv/bin/python"
FDR="$HOME/INGENIERIA IA/TESIS/fuera_del_repo"
frena() { print -r -- "FRENO (comando_analisis_b2_n7c): $1"; exit ${2:-20} }
[[ -x "$PY" ]] || frena "no está el Python del .venv del repo"
[[ ":$PATH:" == *":/usr/sbin:"* ]] || frena "el PATH no trae /usr/sbin (sysctl, para la memoria)"
# Paso 0: el sha256 de cada archivo de N7c y N7c+, en HEAD y en el árbol (si alguno no da, frena con 20 sin correr nada).
SHAS=(
  1b368333838b3d090b923e7d4b3db31751b7e06946ccc31038b4d41a30f125a7  data/experiment/banco_mcp/mcp_kg/familias_nav_rel.py
  ab799426a53484a70dd4adc2709acee70c973e6431f32fff3d1f5d69fa944079  data/experiment/banco_mcp/mcp_kg/servidor_mcp_kg_nav_rel.py
  d5e9aff19bd7d26143b0a9b7a7074844d90bac6405a2dd1a30bd119ff46f9022  data/experiment/banco_mcp/mcp_kg/familias_nav_rel_amp.py
  caf496311442469eafbf54b11320772b1950ff6fadbec6f23a79af23fb4de956  data/experiment/banco_mcp/mcp_kg/servidor_mcp_kg_nav_rel_amp.py
  41b0a6db1950877a23743d100f0ebc3e41e05430c472ad4484f09752e1220d81  data/experiment/banco_mcp/n7c/config_mcp_kg_n7c_evaluado.json
  13a3ae62a542478f2c4bb9261a979de5801ce90fc8fc441b0a695ddd35bb729c  data/experiment/banco_mcp/n7c/mcp_kg_n7c_evaluado.json
  31b39342c736720e5b002423b66453ff219b40daec8e9b73a461e8f8648ad666  data/experiment/banco_mcp/n7c/config_mcp_kg_n7c_amp_evaluado.json
  ef76623881b82478950319e07d4a790879b89390ce3fb99bc59b6a221d91a109  data/experiment/banco_mcp/n7c/mcp_kg_n7c_amp_evaluado.json
  ec1357011f87f4422d17963565de39bd885078dc35133592b39c801f77758fc9  data/experiment/banco_mcp/n7c/config_agentes_n7c.json
  3e0b4383a66be2763b773066c6c3604f6090d0f8a401f74ff0b964dad6060994  data/experiment/banco_mcp/n7c/config_agentes_n7c_humo.json
  5eec8ab3e3186bd0293d87c5ab42c463e03649be7766c3709e16cd7c27e68455  data/experiment/banco_mcp/n7c/correr_n7c.py
  3ce01b7388a777ca2eada2972407b9b612108ebbe9b935f4b0aa0e804a07c17b  data/experiment/banco_mcp/n7c/lanzar_agente_n7c.py
  78568a0215e4eadfc07242f0581b0930bfda39ee408c3e40508d499fea2bed13  data/experiment/banco_mcp/n7c/entrada_n7c_n3.json
  3e00a859a558b47a3915f9e75d8334d7e636e2e4f9893cbe4d72fe10e255bfed  data/experiment/banco_mcp/n7c/entrada_n7c_humo.json
  e5d78a8817b9ca15c9592e301f6a6b053913db14de621177c9de10a2d18e235b  data/experiment/banco_mcp/n7c/control_servidores_n7c.py
  a4892875a9359a09714dad65840e4073c86dd7edc4a65c7534290400a3a57243  data/experiment/banco_mcp/n7c/controlar_humo_n7c.py
  93d88a0385d1f16a9fe0dcda694089eb0bf5743696623b26e9f12e7c2128c81b  data/experiment/banco_mcp/n7c/analizar_n7c.py
  304eccaa411292ee8d5243ac7c87e83dde760589d1f8bc8bb69a537333e8fe3f  data/experiment/banco_mcp/n7c/lector_anclas_n7c.py
)
for (( i = 1; i <= $#SHAS; i += 2 )); do
  esp=$SHAS[i]; ruta=$SHAS[i+1]
  h=$(git -C "$R" --no-optional-locks show "HEAD:$ruta" 2>/dev/null | shasum -a 256 | cut -d' ' -f1)
  a=$(shasum -a 256 "$R/$ruta" 2>/dev/null | cut -d' ' -f1)
  [[ "$h" == "$esp" && "$a" == "$esp" ]] || frena "no da su sha256 en HEAD o en el árbol: $ruta"
done
print -r -- "comando_analisis_b2_n7c: los $(( $#SHAS / 2 )) sha256 de N7c y N7c+, iguales en HEAD y en el árbol"
ENV=(PATH="$PATH" HOME="$HOME" NEO4J_URI=bolt://127.0.0.1:47687 BANCO_VENV_VECTOR="$HOME/INGENIERIA IA/TESIS/venvs/banco_vector_py312")
ENT="$D/entrada_n7c_n3.json"
SHA_ENT=78568a0215e4eadfc07242f0581b0930bfda39ee408c3e40508d499fea2bed13
print -r -- "comando_analisis_b2_n7c: env -i con ${(j:, :)${(@)ENV%%=*}}"
exec env -i "${ENV[@]}" "$PY" -B "$D/analizar_n7c.py" --entrada "$ENT" --sha256-entrada $SHA_ENT \
  --salida-b2 "$FDR/banco_n7c" --salida "$FDR/banco_n7c/analisis/analisis_b2_n7c.json"
