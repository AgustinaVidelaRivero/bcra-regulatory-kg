"""Figura fig:salida_documento: la salida del extractor sumada por documento, de mayor a menor, en escala logarítmica.

Lee solo datos_figura_salida_documento.json (lo escribe salida/recuento/recuento_salida.py), en esta misma carpeta.
Por defecto dibuja la medida principal (la respuesta final de la primera extracción de cada unidad) y escribe
figura_salida_documento.png; con `--medida control` dibuja la medida de control (todos los pedidos pagados de la
primera extracción) y escribe figura_salida_documento_control.png. Ningún nombre ni id de documento entra a la figura.
"""
import argparse
import json
import math
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402
from matplotlib.lines import Line2D  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402
from matplotlib.ticker import FixedLocator, FuncFormatter, NullLocator  # noqa: E402

AQUI = Path(__file__).parent
DATOS = AQUI / "datos_figura_salida_documento.json"
SALIDA = {"principal": AQUI / "figura_salida_documento.png",
          "control": AQUI / "figura_salida_documento_control.png"}

ANCHO_CM, ALTO_CM, DPI = 16.0, 6.6, 300
CUERPO_PT, LEYENDA_PT = 9, 8
FUENTES_LM = ("/Library/TeX/Root/texmf-dist/fonts/opentype/public/lm/lmroman10-regular.otf",
              "/usr/share/texlive/texmf-dist/fonts/opentype/public/lm/lmroman10-regular.otf",
              "/usr/share/texmf/fonts/opentype/public/lm/lmroman10-regular.otf")
BARRA, BARRA_DESTACADA = "#B4B2A9", "#444441"
LINEA = "#A32D2D"
TINTA, EJE, GRILLA = "#2C2C2A", "#5F5E5A", "#D3D1C7"
ANCHO_BARRA = 0.5
TOPE_EJE = 5_000_000        # valor redondo: deja la barra más alta debajo del borde y lugar para la leyenda


def miles(v: float) -> str:
    return f"{int(round(v)):,}".replace(",", ".")


def tipografia() -> str:
    for ruta in FUENTES_LM:
        if Path(ruta).exists():
            font_manager.fontManager.addfont(ruta)
            return font_manager.FontProperties(fname=ruta).get_name()
    return "serif"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--medida", choices=("principal", "control"), default="principal")
    medida = ap.parse_args().medida
    datos = json.loads(DATOS.read_text(encoding="utf-8"))
    dest = datos["documento_destacado"]
    docs = sorted(datos["documentos"], key=lambda d: (-d[medida], d["tanda"], d["documento"]))
    valores = [d[medida] for d in docs]
    destacada = [(d["tanda"], d["documento"]) == (dest["tanda"], dest["documento"]) for d in docs]
    maximo = datos["maximo_respuesta"]
    mas_larga = datos["respuesta_completa_mas_larga_unidad_entera"]

    plt.rcParams.update({"font.family": tipografia(), "font.size": CUERPO_PT, "text.color": TINTA,
                         "axes.labelcolor": TINTA, "axes.edgecolor": EJE, "xtick.color": EJE, "ytick.color": EJE,
                         "ytick.labelcolor": TINTA})
    fig, ax = plt.subplots(figsize=(ANCHO_CM / 2.54, ALTO_CM / 2.54), dpi=DPI)
    x = list(range(len(valores)))
    ax.bar(x, valores, width=ANCHO_BARRA, color=[BARRA_DESTACADA if e else BARRA for e in destacada],
           linewidth=0, zorder=2)
    ax.axhline(maximo, color=LINEA, linewidth=1.2, linestyle="-", zorder=3)
    ax.axhline(mas_larga, color=LINEA, linewidth=1.2, linestyle=(0, (4, 3)), zorder=3)

    ax.set_yscale("log")
    piso = 10 ** math.floor(math.log10(min(valores)))
    ax.set_ylim(piso, TOPE_EJE)
    ax.set_xlim(-0.75, len(valores) - 0.25)
    potencias = [10 ** k for k in range(int(math.log10(piso)), int(math.log10(TOPE_EJE)) + 1) if 10 ** k <= TOPE_EJE]
    ax.yaxis.set_major_locator(FixedLocator(potencias))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: miles(v)))
    ax.yaxis.set_minor_locator(NullLocator())
    ax.xaxis.set_major_locator(NullLocator())
    ax.xaxis.set_minor_locator(NullLocator())
    ax.grid(axis="y", which="major", color=GRILLA, linewidth=0.5)
    ax.set_axisbelow(True)
    for lado in ("top", "right"):
        ax.spines[lado].set_visible(False)
    ax.set_ylabel("Tokens de salida, sumados")
    ax.set_xlabel("Documentos del grafo evaluado, de mayor a menor salida")

    asas = [Patch(facecolor=BARRA, edgecolor="none"), Patch(facecolor=BARRA_DESTACADA, edgecolor="none"),
            Line2D([], [], color=LINEA, linewidth=1.2, linestyle="-"),
            Line2D([], [], color=LINEA, linewidth=1.2, linestyle=(0, (4, 3)))]
    rotulos = ["Salida sumada de un documento", dest["rotulo"], f"Máximo de una respuesta ({miles(maximo)})",
               f"Respuesta completa más larga de una unidad ({miles(mas_larga)})"]
    ax.legend(asas, rotulos, loc="upper right", frameon=False, fontsize=LEYENDA_PT)

    fig.tight_layout(pad=0.3)
    fig.savefig(SALIDA[medida], dpi=DPI, metadata={"Software": None})
    plt.close(fig)
    print("escrito", SALIDA[medida].name)


if __name__ == "__main__":
    main()
