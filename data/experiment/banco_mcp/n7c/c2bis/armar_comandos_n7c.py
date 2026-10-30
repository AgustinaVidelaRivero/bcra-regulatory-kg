"""N7c, C2-bis: arma los tres comandos PREPARADOS de B2 de N7c (n7c/comando_humo_b2_n7c.zsh, n7c/comando_b2_n7c.zsh y
n7c/comando_analisis_b2_n7c.zsh) con el patrón de b63/v2/b2/comando_b63.zsh: `env -i` con una lista cerrada (PATH, HOME,
NEO4J_URI del Neo4j de B6.3, BANCO_VENV_VECTOR y, solo donde se lanza una sesión, ANTHROPIC_API_KEY si está en el entorno de la
Terminal, que pasa sin imprimirse). Cada uno arranca controlando el sha256 de cada archivo de N7c y N7c+ (CONTROLADOS), en HEAD
(`git show`) y en el árbol, con los valores que este script mide al armarlos; dice qué tiene que estar arriba, qué códigos
esperar y cuánto puede gastar. Con --verificar no escribe: dice si los tres son los que arma.
Uso: python3 -I -B data/experiment/banco_mcp/n7c/c2bis/armar_comandos_n7c.py [--verificar]
"""
import hashlib
import json
import sys
from pathlib import Path

BANCO = Path(__file__).resolve().parents[2]
N7C = BANCO / "n7c"
P = "data/experiment/banco_mcp/"
CONTROLADOS = ["mcp_kg/familias_nav_rel.py", "mcp_kg/servidor_mcp_kg_nav_rel.py", "mcp_kg/familias_nav_rel_amp.py",
               "mcp_kg/servidor_mcp_kg_nav_rel_amp.py", "n7c/config_mcp_kg_n7c_evaluado.json", "n7c/mcp_kg_n7c_evaluado.json",
               "n7c/config_mcp_kg_n7c_amp_evaluado.json", "n7c/mcp_kg_n7c_amp_evaluado.json", "n7c/config_agentes_n7c.json",
               "n7c/config_agentes_n7c_humo.json", "n7c/correr_n7c.py", "n7c/lanzar_agente_n7c.py", "n7c/entrada_n7c_n3.json",
               "n7c/entrada_n7c_humo.json", "n7c/control_servidores_n7c.py", "n7c/controlar_humo_n7c.py",
               "n7c/analizar_n7c.py", "n7c/lector_anclas_n7c.py"]


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


COMUN = r'''set -u
D=${0:A:h}                                   # data/experiment/banco_mcp/n7c
R=${D:h:h:h:h}                               # la raíz del repo
PY="$R/.venv/bin/python"
FDR="$HOME/INGENIERIA IA/TESIS/fuera_del_repo"
frena() { print -r -- "FRENO (__NOMBRE__): $1"; exit ${2:-20} }
[[ -x "$PY" ]] || frena "no está el Python del .venv del repo"
[[ ":$PATH:" == *":/usr/sbin:"* ]] || frena "el PATH no trae /usr/sbin (sysctl, para la memoria)"
# Paso 0: el sha256 de cada archivo de N7c y N7c+, en HEAD y en el árbol (si alguno no da, frena con 20 sin correr nada).
SHAS=(
__SHAS__
)
for (( i = 1; i <= $#SHAS; i += 2 )); do
  esp=$SHAS[i]; ruta=$SHAS[i+1]
  h=$(git -C "$R" --no-optional-locks show "HEAD:$ruta" 2>/dev/null | shasum -a 256 | cut -d' ' -f1)
  a=$(shasum -a 256 "$R/$ruta" 2>/dev/null | cut -d' ' -f1)
  [[ "$h" == "$esp" && "$a" == "$esp" ]] || frena "no da su sha256 en HEAD o en el árbol: $ruta"
done
print -r -- "__NOMBRE__: los $(( $#SHAS / 2 )) sha256 de N7c y N7c+, iguales en HEAD y en el árbol"
ENV=(PATH="$PATH" HOME="$HOME" NEO4J_URI=bolt://127.0.0.1:47687 BANCO_VENV_VECTOR="$HOME/INGENIERIA IA/TESIS/venvs/banco_vector_py312")
'''

HUMO = r'''#!/bin/zsh
# comando_humo_b2_n7c.zsh — PREPARADO (N7c, etapa C2-bis). El humo de B2 de N7c, que corre la autora desde su Terminal, desde
# el repo y después del commit 241: el control de los tres servidores, el humo y su control.
#
# Qué tiene que estar arriba: Docker con el contenedor neo4j-bcra-kg-indices-eval sano (el Neo4j de B6.3, bolt://127.0.0.1:47687,
# con el grafo evaluado cargado); el .venv del repo; el venv del codificador (~/INGENIERIA IA/TESIS/venvs/banco_vector_py312, que
# también corre el instrumento de citas); ANTHROPIC_API_KEY en el entorno de la Terminal (solo para el paso 2, sin imprimirse); y
# ningún otro paso pago corriendo. El PATH tiene que traer /usr/sbin.
# Pasos y códigos de salida:
#   0. los sha256 de N7c y N7c+ (HEAD y árbol): 20 si alguno no da;
#   1. n7c/control_servidores_n7c.py (USD 0; salida en ~/INGENIERIA IA/TESIS/fuera_del_repo/banco_n7c_humo/control_servidores/):
#      0 todo da; 1 algo del control no da; 7 otro paso pago; 8 una precondición. Si no da 0, el comando frena con ese código;
#   2. n7c/correr_n7c.py todo con n7c/entrada_n7c_humo.json (3 sesiones, una por configuración, P = 1 en los dos lotes; salida en
#      ~/INGENIERIA IA/TESIS/fuera_del_repo/banco_n7c_humo/, que crea el corredor): 0 terminó; 2 freno del gasto; 7 otro paso pago;
#      8 precondición; 13 memoria; 14 Docker; los demás, los de correr_n6. Si no da 0, el comando frena con ese código;
#   3. n7c/controlar_humo_n7c.py: 0 las tres pasan; 1 alguna no pasa; 2 ninguna falla y alguna no es concluyente. Es el código
#      con que sale el comando.
# Gasto: como mucho USD 5,40 del agente (3 sesiones por el corte de R5 de USD 1,80) más el juez (3 respuestas por 3 repeticiones;
# la reserva del corredor es de USD 0,0378 por respuesta). La entrada lleva el tope de USD 45 y el freno de 38.
# Uso: zsh data/experiment/banco_mcp/n7c/comando_humo_b2_n7c.zsh
''' + COMUN.replace("__NOMBRE__", "comando_humo_b2_n7c") + r'''SAL="$FDR/banco_n7c_humo"
ENT="$D/entrada_n7c_humo.json"
SHA_ENT=__SHA_HUMO__
print -r -- "comando_humo_b2_n7c: env -i con ${(j:, :)${(@)ENV%%=*}}"
env -i "${ENV[@]}" "$PY" -B "$D/control_servidores_n7c.py" --salida "$SAL/control_servidores"; c=$?
(( c == 0 )) || frena "el control de los servidores dio $c" $c
[[ -n "${ANTHROPIC_API_KEY:-}" ]] || frena "falta ANTHROPIC_API_KEY en el entorno de la Terminal"
env -i "${ENV[@]}" ANTHROPIC_API_KEY="$ANTHROPIC_API_KEY" "$PY" -B "$D/correr_n7c.py" todo --entrada "$ENT" \
  --sha256-entrada $SHA_ENT --salida "$SAL" --P-sin-codificador 1 --P-con-codificador 1; c=$?
(( c == 0 )) || frena "el humo frenó con $c" $c
env -i "${ENV[@]}" "$PY" -B "$D/controlar_humo_n7c.py" --entrada "$ENT" --sha256-entrada $SHA_ENT --salida "$SAL"
exit $?
'''

B2 = r'''#!/bin/zsh
# comando_b2_n7c.zsh — PREPARADO (N7c, etapa C2-bis). B2 de N7c, que corre la autora desde su Terminal, desde el repo, después
# del commit 241 y del humo: `controles` y después `todo`, con P = 1 en los dos lotes.
#
# Qué tiene que estar arriba: lo mismo que para el humo (Docker con neo4j-bcra-kg-indices-eval sano, el .venv del repo, el venv
# del codificador, ANTHROPIC_API_KEY en el entorno de la Terminal solo para `todo`, ningún otro paso pago, /usr/sbin en el PATH),
# y el humo con su control en 0 (~/INGENIERIA IA/TESIS/fuera_del_repo/banco_n7c_humo/control_humo_n7c.json). Si el control del
# humo no dio 0 y la mesa lo revisó, el primer argumento --humo-revisado lo deja pasar.
# Pasos y códigos de salida:
#   0. los sha256 de N7c y N7c+ (HEAD y árbol): 20 si alguno no da; 21 si no está el control del humo o no dio 0;
#   1. n7c/correr_n7c.py controles (USD 0, sin la clave): imprime lo fijo, el swap, las dos P y Docker; 13 memoria, 14 Docker.
#      Además, el comando frena con 13 si lo fijo pasa de 9,70 GB: 14,5 menos 4,565 (el servidor con el codificador) menos 0,234
#      (la huella de CLI que midió N6 en su lote 1), porque el lote sin codificador de B2 está vacío y no mide ninguna;
#   2. n7c/correr_n7c.py todo con n7c/entrada_n7c_n3.json (270 sesiones: las 30 de N3 en N7, N7c y N7c+, 3 veces cada una; y
#      el juez), salida en ~/INGENIERIA IA/TESIS/fuera_del_repo/banco_n7c/: 0 terminó; 2 freno del gasto; 7 otro paso pago;
#      8 precondición; 11 freno del juez; 12 tres formas desconocidas; 13 memoria; 14 Docker; los demás, los de correr_n6. Si
#      frena, retomar es correr el mismo comando: ninguna sesión terminada se repite.
# Gasto: el tope de USD 45 y el freno de 38 de la entrada (D-B2-8), para el agente y el juez juntos.
# Uso: zsh data/experiment/banco_mcp/n7c/comando_b2_n7c.zsh [--humo-revisado]
''' + COMUN.replace("__NOMBRE__", "comando_b2_n7c") + r'''SAL="$FDR/banco_n7c"
ENT="$D/entrada_n7c_n3.json"
SHA_ENT=__SHA_B2__
HUMO="$FDR/banco_n7c_humo/control_humo_n7c.json"
if [[ "${1:-}" != "--humo-revisado" ]]; then
  [[ -f "$HUMO" ]] || frena "no está el control del humo: el humo va antes de B2" 21
  ch=$(env -i PATH=/usr/bin:/bin "$PY" -I -B -c 'import json, sys; print(json.load(open(sys.argv[1], encoding="utf-8"))["codigo"])' "$HUMO")
  [[ "$ch" == 0 ]] || frena "el control del humo dio $ch (con la revisión de la mesa, --humo-revisado)" 21
fi
print -r -- "comando_b2_n7c: env -i con ${(j:, :)${(@)ENV%%=*}}"
out=$(env -i "${ENV[@]}" "$PY" -B "$D/correr_n7c.py" controles --entrada "$ENT" --sha256-entrada $SHA_ENT --salida "$SAL" \
  --P-sin-codificador 1 --P-con-codificador 1); c=$?
print -r -- "$out"
(( c == 0 )) || frena "controles dio $c" $c
fijo=$(print -r -- "$out" | env -i PATH=/usr/bin:/bin "$PY" -I -B -c 'import json, sys; print(json.loads(sys.stdin.read().strip().splitlines()[-1])["lo_fijo_gb"])') \
  || frena "no se leyó lo fijo de la salida de controles" 13
env -i PATH=/usr/bin:/bin "$PY" -I -B -c 'import sys; sys.exit(0 if float(sys.argv[1]) <= 9.70 else 1)' "$fijo" \
  || frena "lo fijo da $fijo GB: pasa de 9,70 (14,5 − 4,565 − 0,234)" 13
print -r -- "comando_b2_n7c: lo fijo, $fijo GB (9,70 o menos)"
[[ -n "${ANTHROPIC_API_KEY:-}" ]] || frena "falta ANTHROPIC_API_KEY en el entorno de la Terminal"
exec env -i "${ENV[@]}" ANTHROPIC_API_KEY="$ANTHROPIC_API_KEY" "$PY" -B "$D/correr_n7c.py" todo --entrada "$ENT" \
  --sha256-entrada $SHA_ENT --salida "$SAL" --P-sin-codificador 1 --P-con-codificador 1
'''

ANALISIS = r'''#!/bin/zsh
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
''' + COMUN.replace("__NOMBRE__", "comando_analisis_b2_n7c") + r'''ENT="$D/entrada_n7c_n3.json"
SHA_ENT=__SHA_B2__
print -r -- "comando_analisis_b2_n7c: env -i con ${(j:, :)${(@)ENV%%=*}}"
exec env -i "${ENV[@]}" "$PY" -B "$D/analizar_n7c.py" --entrada "$ENT" --sha256-entrada $SHA_ENT \
  --salida-b2 "$FDR/banco_n7c" --salida "$FDR/banco_n7c/analisis/analisis_b2_n7c.json"
'''


def armar() -> dict:
    shas = "\n".join(f"  {sha(BANCO / r)}  {P}{r}" for r in CONTROLADOS)
    fill = lambda t: (t.replace("__SHAS__", shas).replace("__SHA_HUMO__", sha(N7C / "entrada_n7c_humo.json"))  # noqa: E731
                      .replace("__SHA_B2__", sha(N7C / "entrada_n7c_n3.json")))
    return {"comando_humo_b2_n7c.zsh": fill(HUMO), "comando_b2_n7c.zsh": fill(B2), "comando_analisis_b2_n7c.zsh": fill(ANALISIS)}


def main(argv: list[str]) -> int:
    t = armar()
    if "--verificar" in argv:
        iguales = {k: (N7C / k).is_file() and (N7C / k).read_text(encoding="utf-8") == v for k, v in t.items()}
        print(json.dumps({"iguales_a_lo_que_se_arma": iguales}, ensure_ascii=False))
        return 0 if all(iguales.values()) else 1
    for k, v in t.items():
        (N7C / k).write_text(v, encoding="utf-8")
        print(f"{hashlib.sha256(v.encode('utf-8')).hexdigest()}  n7c/{k}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
