"""U-E3-LISTAS, O5: los dos valores del candado del mensaje de E3 con la NOTA nueva, recomputados en procesos aparte y
desde cero sobre UNA COPIA (nunca el repo), y sus controles. La fixture no cambia (19 casos).
  calcular: cada proceso ejecuta prompt_e3.py de la copia sin la llamada final al candado, y da el sha256 de la fixture
            y el de los mensajes de sus casos; dos procesos tienen que dar lo mismo. Con --escribir, pone en la copia el
            valor nuevo del mensaje (el de la fixture tiene que seguir igual).
  controles (después de escribir): (1) importar prompt_e3 de la copia no frena y da el valor nuevo, en dos procesos;
            (2) el código de la copia de HEAD, sobre la misma fixture, da el valor de hoy (66bc8656…), distinto;
            (3) un espacio al final de NOTA_E3_ITEM_CASOS (y de NOTA_E3_ITEM_LISTA) cambia el sha; restaurado, vuelve.
Uso: python ue3_o5_candado.py <copia_o5> <copia_head> <salida.json> [--escribir]"""
import json, subprocess, sys
from pathlib import Path
C, H, OUT = (Path(x).resolve() for x in sys.argv[1:4])
ESCRIBIR = "--escribir" in sys.argv
E3 = lambda c: c / "data/experiment/reextraccion_v2/e3_verificador"  # noqa: E731
CALC = r'''
import hashlib, json, sys, types
d = sys.argv[1]; sys.path.insert(0, d)
src = open(d + "/prompt_e3.py", encoding="utf-8").read()
fin = "\n_candado_mensaje_e3()\n"
assert src.endswith(fin)
m = types.ModuleType("prompt_e3"); m.__file__ = d + "/prompt_e3.py"; sys.modules["prompt_e3"] = m
exec(compile(src[: -len(fin)] + "\n", m.__file__, "exec"), m.__dict__)
b = open(d + "/candado_mensaje_e3.json", "rb").read()
casos = json.loads(b)["casos"]
modo = sys.argv[2]
if modo:
    setattr(m, modo, getattr(m, modo) + " ")
print(json.dumps({"fixture": hashlib.sha256(b).hexdigest(), "mensaje": m.sha256_mensajes_e3(casos), "casos": len(casos)}))
'''
IMPORTA = r'''
import json, sys
sys.path.insert(0, sys.argv[1])
import prompt_e3 as P
casos = json.loads(open(sys.argv[1] + "/candado_mensaje_e3.json", encoding="utf-8").read())["casos"]
print(json.dumps({"mensaje": P.sha256_mensajes_e3(casos), "esperado": P.MENSAJE_E3_SHA256_ESPERADO,
                  "fixture_esperada": P.CANDADO_MENSAJE_E3_JSON_SHA256_ESPERADO}))
'''
ENV = {"PYTHONDONTWRITEBYTECODE": "1", "PATH": "/usr/bin:/bin"}


def corre(codigo, *args):
    r = subprocess.run([sys.executable, "-B", "-c", codigo, *map(str, args)], capture_output=True, text=True, env=ENV)
    if r.returncode != 0:
        return {"error": (r.stderr.strip().splitlines() or [f"rc={r.returncode}"])[-1]}
    return json.loads(r.stdout.strip().splitlines()[-1])


res = {}
a, b = corre(CALC, E3(C), ""), corre(CALC, E3(C), "")
res["calculo"] = {"proceso_1": a, "proceso_2": b, "iguales": a == b}
assert a == b and "error" not in a
src = (E3(C) / "prompt_e3.py").read_text(encoding="utf-8")
import re  # noqa: E402
viejo_f = re.search(r'^CANDADO_MENSAJE_E3_JSON_SHA256_ESPERADO = "([0-9a-f]{64})"$', src, re.M).group(1)
viejo_m = re.search(r'^MENSAJE_E3_SHA256_ESPERADO = "([0-9a-f]{64})"$', src, re.M).group(1)
res["valores_de_hoy"] = {"fixture": viejo_f, "mensaje": viejo_m}
res["propuestos"] = {"CANDADO_MENSAJE_E3_JSON_SHA256_ESPERADO": a["fixture"], "MENSAJE_E3_SHA256_ESPERADO": a["mensaje"]}
res["fixture_sin_cambio"] = a["fixture"] == viejo_f
res["mensaje_cambia"] = a["mensaje"] != viejo_m
if ESCRIBIR:
    assert res["fixture_sin_cambio"]
    l_v, l_n = f'MENSAJE_E3_SHA256_ESPERADO = "{viejo_m}"\n', f'MENSAJE_E3_SHA256_ESPERADO = "{a["mensaje"]}"\n'
    assert src.count(l_v) == 1
    (E3(C) / "prompt_e3.py").write_text(src.replace(l_v, l_n), encoding="utf-8")
    i1, i2 = corre(IMPORTA, E3(C)), corre(IMPORTA, E3(C))
    res["1_importa_sin_frenar"] = {"proceso_1": i1, "proceso_2": i2, "iguales": i1 == i2,
                                   "da_el_propuesto": i1.get("mensaje") == i1.get("esperado") == a["mensaje"]}
    hh = corre(IMPORTA, E3(H))
    res["2_codigo_de_HEAD_misma_fixture"] = {"resultado": hh, "da_el_de_hoy": hh.get("mensaje") == viejo_m,
                                             "distinto_del_propuesto": hh.get("mensaje") != a["mensaje"]}
    sens = {}
    for modo in ("NOTA_E3_ITEM_CASOS", "NOTA_E3_ITEM_LISTA"):
        x = corre(CALC, E3(C), modo)
        sens[modo] = {"sha": x.get("mensaje"), "cambia": x.get("mensaje") != a["mensaje"]}
    sens["restaurado"] = corre(CALC, E3(C), "").get("mensaje") == a["mensaje"]
    res["3_sensibilidad"] = sens
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(res, ensure_ascii=False, indent=1))
