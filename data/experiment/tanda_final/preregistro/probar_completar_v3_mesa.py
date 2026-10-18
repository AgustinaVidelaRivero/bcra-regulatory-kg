"""Mesa, §163: la prueba en seco del completador v3 del pre-registro de la tanda final, con fuentes inventadas en un paquete temporal
(nada del repo ni de T4). Sobre el texto real de la v3 y con el JSON de huecos real, cambiando solo las fuentes. USD 0.
Uso: python3 -I -B probar_completar_v3_mesa.py <salida.txt>"""
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

OUT = Path(sys.argv[1])
AQUI = Path(__file__).resolve().parent
PRE, HJ, COMP, CIF = (AQUI / n for n in ("preregistro_tanda_final_v3_PARA_FIRMAR.md", "huecos_preregistro_tanda_final.json",
                                         "completar_preregistro_tanda_final_mesa.py", "salida_cifras_preregistro_tanda_final.json"))
huecos = json.loads(HJ.read_text(encoding="utf-8"))
sal, mal = [], 0


def correr(T, hj, momento, pre=PRE):
    return subprocess.run([sys.executable, "-I", "-B", str(COMP), str(pre), str(T), str(hj), str(T / "derivada.md"), "--momento", momento],
                          capture_output=True, text=True)


def paquete(T, cambiar=None):
    """Una fuente inventada por hueco, en el paquete temporal: cada valor es «valor de <id>»."""
    h = json.loads(json.dumps(huecos))
    for k, v in h.items():
        if k.startswith("_") and k != "_cifras_derivadas":
            continue
        if k == "_cifras_derivadas":
            (T / "cifras.json").write_bytes(CIF.read_bytes())
            v.update({"fuente": "paquete: cifras.json"})
            continue
        (T / f"{k}.json").write_text(json.dumps({"v": f"valor de {k}"}), encoding="utf-8")
        v.update({"tipo": "json", "fuente": f"paquete: {k}.json", "clave": "v"})
        v.pop("commit", None)
    if cambiar:
        cambiar(h)
    p = T / "huecos.json"
    p.write_text(json.dumps(h, ensure_ascii=False), encoding="utf-8")
    return p


def caso(nombre, momento, debe_ok, cambiar=None, control=None, pre=None):
    global mal
    with tempfile.TemporaryDirectory(prefix="compl_") as t:
        T = Path(t)
        hj = paquete(T, cambiar)
        r = correr(T, hj, momento, pre(T) if pre else PRE)
        ok = (r.returncode == 0) == debe_ok
        if ok and debe_ok and control:
            ok = control(T, hj)
        mal += not ok
        sal.append(f"{'OK ' if ok else 'MAL'} {nombre}: rc {r.returncode} | {(r.stdout + r.stderr).strip().splitlines()[-1][:120]}")


def ctl_T1(T, hj):
    d = (T / "derivada.md").read_text(encoding="utf-8")
    quedan = set(re.findall(r"⟦([A-Za-z0-9_.]+)⟧", d))
    j = json.loads((T / "derivada.huecos.json").read_text(encoding="utf-8"))
    return (quedan == {k for k, v in huecos.items() if not k.startswith("_") and v["momento"] != "T1"}
            and "valor de A3.derivado_sha256" in d and j["huecos_json_sha256"] == hashlib.sha256(hj.read_bytes()).hexdigest()
            and f"`{j['huecos_json_sha256']}`" in d and "U = 4951" in d and "documentos fuera: ninguno" in d)


def ctl_T5(T, hj):
    d = (T / "derivada.md").read_text(encoding="utf-8")
    return "⟦" not in d.replace("⟦…⟧", "") and "valor de T5.costo_real_tanda1" in d and "Los que esperan a un momento posterior:** ninguno" in d


caso("al momento T1: completa los de T1, deja los de T4 y T5, y nombra el sha256 del JSON y las cifras", "T1", True, control=ctl_T1)
caso("al momento T1, con un hueco de T4 todavía PENDIENTE: no frena (no le toca)", "T1", True,
     cambiar=lambda h: h["T4.cola"].update({"fuente": "PENDIENTE: las tasas"}), control=ctl_T1)
caso("al momento T1, con un hueco de A3 PENDIENTE: frena", "T1", False, cambiar=lambda h: h["A3.candado_sha256"].update({"fuente": "PENDIENTE"}))
caso("al momento lectura_tramo1, con un hueco de T4 PENDIENTE: frena", "lectura_tramo1", False,
     cambiar=lambda h: h["T4.cola"].update({"fuente": "PENDIENTE: las tasas"}))
caso("al momento T5: no queda ningún hueco", "T5", True, control=ctl_T5)
caso("un hueco sin momento: frena", "T1", False, cambiar=lambda h: h["T4.cola"].pop("momento"))
caso("un hueco del texto que no está en el JSON: frena", "T1", False, cambiar=lambda h: h.pop("revision.rasgos_confirmados"))
caso("sin las cifras derivadas: frena", "T1", False, cambiar=lambda h: h.pop("_cifras_derivadas"))
caso("un momento que no existe: frena", "T2", False)


def con_sin(T):
    c = json.loads(CIF.read_text(encoding="utf-8"))
    c["documentos_fuera"] = ["ribspc"]
    (T / "cifras.json").write_text(json.dumps(c), encoding="utf-8")
    return PRE


def ctl_sin(T, hj):
    return "documentos fuera: ribspc" in (T / "derivada.md").read_text(encoding="utf-8")


caso("con un documento fuera en las cifras: la derivada lo dice", "T1", True, control=ctl_sin, pre=con_sin)
with tempfile.TemporaryDirectory(prefix="compl_hoy_") as t:
    T = Path(t)
    r = correr(T, HJ, "T1")
    ok = r.returncode != 0 and "PENDIENTE" in r.stdout + r.stderr and not (T / "derivada.md").exists()
    mal += not ok
    sal.append(f"{'OK ' if ok else 'MAL'} con el JSON de huecos de hoy, al momento T1: frena por las fuentes PENDIENTE, sin escribir | "
               f"{(r.stdout + r.stderr).strip().splitlines()[-1][:90]}")
sal.append(f"RESULTADO: {'PASA' if not mal else 'MAL'} ({len(sal) - mal} de {len(sal)})")
OUT.write_text("\n".join(sal) + "\n", encoding="utf-8")
print("\n".join(sal))
sys.exit(1 if mal else 0)
