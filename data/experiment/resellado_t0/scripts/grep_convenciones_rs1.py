"""Re-sellado único de la tanda 0: el grep de convenciones (CLAUDE.md §5) sobre lo que escribió la etapa. Solo lee.
  - lo escrito por mí: la carpeta de la etapa entera y los cuatro manifiestos nuevos; de los 22 archivos que cambian, solo los
    renglones agregados (git diff HEAD);
  - aparte, las salidas de los generadores (los cuatro ensamblados nuevos), que no edito.
Términos: los tokens de `git config user.name` y los nombres de pila de la variable de entorno NOMBRES_EXTRA (no se escriben
en ningún archivo), con límites de palabra; fuentes conversacionales; la cuenta del sistema en rutas. Las coincidencias se
dan por archivo y término, con el número de renglón y sin transcribir el texto. Control positivo: un archivo con un renglón por
término, que tiene que dar todos.
Uso, desde la raíz del repo: python3 -I -B grep_convenciones_rs1.py <archivo de control positivo (se escribe)> <salida.txt>
"""
import getpass
import os
import re
import subprocess
import sys
import unicodedata
from collections import Counter
from pathlib import Path

CTRL, SAL = Path(sys.argv[1]), Path(sys.argv[2])


def norm(s: str) -> str:
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()


usuario = subprocess.run(["git", "config", "user.name"], capture_output=True, text=True).stdout
nombres = sorted({norm(t) for t in re.findall(r"\w+", usuario) if len(t) > 2}
                 | {norm(t) for t in os.environ.get("NOMBRES_EXTRA", "").split(",") if t.strip()})
conversacion = ["slack", "whatsapp", "mail", "correo", "reunion", "como dijo", "segun el mail", "pedido por", "me dijo",
                "mensaje de", "por chat"]
cuenta = [getpass.getuser().lower()]
terminos = [("nombre", n, re.compile(rf"\b{re.escape(n)}\b")) for n in nombres] \
    + [("conversacion", t, re.compile(rf"\b{re.escape(t)}")) for t in conversacion] \
    + [("cuenta", t, re.compile(re.escape(t))) for t in cuenta]
CTRL.write_text("\n".join(f"control {t}" for _, t, _ in terminos) + "\n", encoding="utf-8")


def buscar(lineas: list[tuple[int, str]]) -> Counter:
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
X = "data/experiment/reextraccion_v2"
propios = sorted(p.as_posix() for p in Path("data/experiment/resellado_t0").rglob("*") if p.is_file())
propios += [f"{X}/manifiestos/tanda0_ens_{g}_rs1.json" for g in ("diez_r2b", "desarrollo_r2b", "diez_r2b_sincola", "desarrollo_r2b_sincola")]
cambian = subprocess.run(["git", "diff", "--name-only", "HEAD"], capture_output=True, text=True).stdout.split()
generados = sorted(p.as_posix() for g in ("diez_r2b", "diez_r2b_sincola", "desarrollo_r2b", "desarrollo_r2b_sincola")
                   for p in Path(f"{X}/corpus_tanda0/ens_{g}_rs1").rglob("*") if p.is_file())


def informe(titulo: str, archivos: list[str], solo_agregados: bool) -> None:
    out.append(f"\n## {titulo}: {len(archivos)} archivos")
    total = Counter()
    for a in archivos:
        if solo_agregados:
            d = subprocess.run(["git", "diff", "-U0", "HEAD", "--", a], capture_output=True, text=True).stdout
            lineas, n = [], 0
            for l in d.splitlines():
                m = re.match(r"^@@ -\d+(?:,\d+)? \+(\d+)", l)
                if m:
                    n = int(m.group(1)); continue
                if l.startswith("+") and not l.startswith("+++"):
                    lineas.append((n, l[1:])); n += 1
        else:
            try:
                lineas = list(enumerate(Path(a).read_text(encoding="utf-8").splitlines(), 1))
            except UnicodeDecodeError:
                continue
        c = buscar(lineas)
        if c:
            por = Counter((cl, t) for cl, t, _ in c)
            reng = sorted({n for _, _, n in c})
            out.append(f"{a}: " + ", ".join(f"{cl}:{'<nombre>' if cl == 'nombre' else ('<cuenta>' if cl == 'cuenta' else t)}={v}"
                                            for (cl, t), v in sorted(por.items()))
                       + f" | renglones {reng[:12]}{' …' if len(reng) > 12 else ''}")
            total.update(cl for cl, _, _ in c)
    out.append(f"total por clase: {dict(total)}")


informe("Lo escrito por la etapa (archivos enteros)", propios, False)
informe("Los 22 archivos que cambian (solo los renglones agregados)", cambian, True)
informe("Salidas de los generadores (los cuatro ensamblados nuevos; no se editan)", generados, False)
SAL.write_text("\n".join(out) + "\n", encoding="utf-8")
print("\n".join(out))
