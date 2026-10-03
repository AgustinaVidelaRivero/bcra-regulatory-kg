import sys, hashlib
from pathlib import Path
M = Path(sys.argv[1])
sys.path.insert(0, str(M / "data/experiment/b54_catalogo_v3/code"))
import prompt_v3_b54 as v3
t = v3.PREFIJO_SISTEMA_V3
print("sha256_prefijo_v3", hashlib.sha256(t.encode("utf-8")).hexdigest())
for frase in ("Extraés SOLO del texto del punto; el contexto heredado orienta y ancla, pero NO se extrae de él",
              "**EL CONTEXTO ANCLA, LA UNIDAD EXTRAE.**",
              "**Las relations son SOLO entre entidades del MISMO chunk.**"):
    print(t.count(frase), "|", frase)
import prompt_e1
print("cabecera_mensaje_herencia", "NO extraigas contenido normativo de estos bloques" in prompt_e1.build_user_message({"archivo": "x.pdf", "to": "x", "unidad": "1.1", "titulo": "t", "tipo": "punto_terminal", "texto": "a", "herencia": [{"tipo": "intro", "unidad_origen": "1", "texto": "b"}], "flags": {}}))
