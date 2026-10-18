"""U-ALCANCE-E1, A3: el grep de convenciones (CLAUDE.md §5) sobre lo que escribió la etapa (criterio 11). Solo lee. Sigue a
grep_convenciones_a2.py de A2; como A3 no escribe en el repo, mira el paquete:
  - todo lo que A3 escribe entero (la carpeta data/experiment/alcance_e1/a3/ del paquete, el JSON de lo leído, los diffs y
    el derivado nuevo), archivos enteros;
  - los tres archivos rastreados que A3 cambia y que tienen texto de otras etapas (prompt_r2b.py, selftest_prompt_r2b.py y
    tabla_reprocesamiento.md): solo los renglones agregados contra la copia de la base (diff -U0).
Términos: los tokens de `git config user.name` del repo, partidos también por mayúsculas, y los nombres de pila de la variable
de entorno NOMBRES_EXTRA (no se escriben en ningún archivo), con límites de palabra; fuentes conversacionales; la cuenta del
sistema en rutas. Las coincidencias se dan por archivo y término, con el número de renglón y sin transcribir el texto.
Control positivo: un archivo con un renglón por término, que tiene que dar todos.
Uso: python3 -I -B grep_convenciones_a3.py <repo> <paquete> <copia_head> <control positivo (se escribe)> <salida.txt>
"""
import getpass
import os
import re
import subprocess
import sys
import unicodedata
from collections import Counter
from pathlib import Path

REPO, PAQ, CH, CTRL, SAL = sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3]), Path(sys.argv[4]), Path(sys.argv[5])
CON_TEXTO_AJENO = {  # archivo del paquete → su ruta en el repo
    "para_el_repo/prompt_r2b_post_A3.py": "data/experiment/reextraccion_v2/e1_extractor/prompt_r2b.py",
    "para_el_repo/selftest_prompt_r2b_post_A3.py": "data/experiment/reextraccion_v2/e1_extractor/selftest_prompt_r2b.py",
    "para_el_repo/tabla_reprocesamiento_post_A3.md": "data/experiment/mantenimiento/tabla_reprocesamiento.md",
}


def norm(s: str) -> str:
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()


usuario = subprocess.run(["git", "--no-optional-locks", "-C", REPO, "config", "user.name"], capture_output=True,
                         text=True).stdout
tokens = set(re.findall(r"\w+", usuario)) | set(re.findall(r"[A-ZÁÉÍÓÚÑ][a-záéíóúñ]+", usuario))
nombres = sorted({norm(t) for t in tokens if len(t) > 2}
                 | {norm(t) for t in os.environ.get("NOMBRES_EXTRA", "").split(",") if t.strip()})
conversacion = ["slack", "whatsapp", "mail", "correo", "reunion", "como dijo", "segun el mail", "pedido por", "me dijo",
                "mensaje de", "por chat"]
cuenta = [getpass.getuser().lower()]
terminos = [("nombre", n, re.compile(rf"\b{re.escape(n)}\b")) for n in nombres] \
    + [("conversacion", t, re.compile(rf"\b{re.escape(t)}")) for t in conversacion] \
    + [("cuenta", t, re.compile(re.escape(t))) for t in cuenta]
CTRL.write_text("\n".join(f"control {t}" for _, t, _ in terminos) + "\n", encoding="utf-8")


def buscar(lineas):
    c = Counter()
    for n, l in lineas:
        ln = norm(l)
        for clase, t, rx in terminos:
            if rx.search(ln):
                c[(clase, t, n)] += 1
    return c


out = [f"términos: {len(nombres)} nombres (tokens de user.name y NOMBRES_EXTRA), {len(conversacion)} de conversación, "
       f"1 de la cuenta; ninguno se transcribe acá"]
ctrl = buscar(list(enumerate(CTRL.read_text(encoding="utf-8").splitlines(), 1)))
out.append(f"control positivo: {len({(c, t) for c, t, _ in ctrl})} de {len(terminos)} términos encontrados")


def informe(titulo, archivos):
    out.append(f"\n## {titulo}: {len(archivos)} archivos")
    total = Counter()
    for nombre, lineas in archivos:
        c = buscar(lineas)
        if c:
            por = Counter((cl, t) for cl, t, _ in c)
            reng = sorted({n for _, _, n in c})
            out.append(f"{nombre}: " + ", ".join(
                f"{cl}:{'<nombre>' if cl == 'nombre' else ('<cuenta>' if cl == 'cuenta' else t)}={v}"
                for (cl, t), v in sorted(por.items())) + f" | renglones {reng[:12]}{' …' if len(reng) > 12 else ''}")
            total.update(cl for cl, _, _ in c)
    out.append(f"total por clase: {dict(total)}")


enteros, agregados = [], []
for p in sorted(x for x in PAQ.rglob("*") if x.is_file()):
    rel = p.relative_to(PAQ).as_posix()
    if rel in CON_TEXTO_AJENO:
        d = subprocess.run(["diff", "-U0", str(CH / CON_TEXTO_AJENO[rel]), str(p)], capture_output=True, text=True).stdout
        lineas, n = [], 0
        for l in d.splitlines():
            m = re.match(r"^@@ -\d+(?:,\d+)? \+(\d+)", l)
            if m:
                n = int(m.group(1))
                continue
            if l.startswith("+") and not l.startswith("+++"):
                lineas.append((n, l[1:]))
                n += 1
        agregados.append((rel, lineas))
        continue
    try:
        enteros.append((rel, list(enumerate(p.read_text(encoding="utf-8").splitlines(), 1))))
    except UnicodeDecodeError:
        out.append(f"(no es texto, no se lee: {rel})")
informe("Lo que A3 escribe entero (el paquete, salvo los tres archivos de abajo)", enteros)
informe("Los tres archivos rastreados con texto de otras etapas (solo los renglones agregados)", agregados)
SAL.write_text("\n".join(out) + "\n", encoding="utf-8")
print("\n".join(out))
