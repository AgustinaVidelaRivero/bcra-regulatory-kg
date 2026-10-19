"""heredocs_sin_comillas_t1.py — B6.1, tanda final, «seguí» de T2, parte 1: cuenta, en la transcripción de la sesión, los heredocs
sin comillas y con comillas (el operador `<<` precedido por un espacio y seguido del delimitador EOF, sin o con comillas simples) de
los comandos de la consola, con la hora local de cada uno sin comillas. Una mención del operador entre comillas invertidas, en un
docstring o en un patrón, no cuenta. Solo lee la transcripción que se le pasa; no imprime los comandos. Uso: python3 -I -B heredocs_sin_comillas_t1.py <transcripción.jsonl>"""
import json, re, sys
from datetime import datetime, timedelta, timezone
sys.dont_write_bytecode = True
sin, con, horas = 0, 0, []
for linea in open(sys.argv[1], encoding="utf-8"):
    try:
        d = json.loads(linea)
    except ValueError:
        continue
    for b in (d.get("message") or {}).get("content") or []:
        if isinstance(b, dict) and b.get("type") == "tool_use" and b.get("name") == "Bash":
            c = b.get("input", {}).get("command", "")
            k = len(re.findall(r"(?<=\s)<<\s*EOF\b", c))
            sin += k
            con += len(re.findall(r"(?<=\s)<<\s*'EOF'", c))
            if k:
                t = datetime.fromisoformat(d["timestamp"].replace("Z", "+00:00")).astimezone(timezone(timedelta(hours=-3)))
                horas.append(t.strftime("%Y-%m-%d %H:%M:%S %z"))
print(json.dumps({"heredocs_sin_comillas": sin, "heredocs_con_comillas": con, "horas_locales_sin_comillas": horas}, ensure_ascii=False, indent=1))
