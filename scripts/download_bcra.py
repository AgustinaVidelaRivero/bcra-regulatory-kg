"""
Descarga los Textos Ordenados del BCRA relevantes para el dominio
de credit risk / scoring crediticio.

Idempotente: saltea archivos ya descargados.
Tolerante a fallos: registra errores pero continúa con el resto.

Uso:
    python scripts/download_bcra.py

Output:
    data/raw/<nombre>.pdf
"""
from __future__ import annotations

import sys
from pathlib import Path

import requests


# Textos Ordenados del BCRA relevantes para credit risk.
# Fuente: https://www.bcra.gob.ar/SistemasFinancierosYdePagos/Ordenamiento_y_resumenes.asp
# URLs verificadas a abril 2026.
TEXTOS_ORDENADOS: dict[str, str] = {
    "marco_normativo": (
        "https://www.bcra.gob.ar/archivos/Pdfs/SistemasFinancierosYdePagos/marco%20normativo.pdf"
    ),
    "gestion_crediticia": (
        "https://www.bcra.gob.ar/pdfs/texord/t-gescre.pdf"
    ),
    "clasificacion_deudores": (
        "https://www.bcra.gob.ar/archivos/Pdfs/texord/t-cladeu.pdf"
    ),
    "grandes_exposiciones_riesgo_credito": (
        "https://www.bcra.gob.ar/Pdfs/Texord/t-gerc.pdf"
    ),
    # Espacio para sumar más:
    # "garantias": "...",
    # "capitales_minimos": "...",
    # "proteccion_usuarios_servicios_financieros": "...",
}


# Carpeta de output relativa a la raíz del proyecto.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = PROJECT_ROOT / "data" / "raw"

# Tamaño mínimo aceptable para considerar la descarga válida (en bytes).
MIN_VALID_SIZE = 10_000  # 10 KB

# User-Agent para evitar bloqueos por algunos servidores.
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (compatible; BCRA-KG-Thesis/0.1; "
        "academic research)"
    )
}


def download_one(name: str, url: str, out_dir: Path) -> tuple[bool, str]:
    """
    Descarga un Texto Ordenado.

    Returns:
        (success, message)
    """
    out_path = out_dir / f"{name}.pdf"

    if out_path.exists() and out_path.stat().st_size >= MIN_VALID_SIZE:
        return True, f"[skip] {name} ya existe ({out_path.stat().st_size // 1024} KB)"

    try:
        response = requests.get(url, headers=HEADERS, timeout=60)
        response.raise_for_status()
    except requests.RequestException as e:
        return False, f"[err]  {name}: {e}"

    content = response.content
    if len(content) < MIN_VALID_SIZE:
        return False, f"[err]  {name}: archivo demasiado chico ({len(content)} bytes)"

    out_path.write_bytes(content)
    return True, f"[ok]   {name} → {out_path.relative_to(PROJECT_ROOT)} ({len(content) // 1024} KB)"


def main() -> int:
    """Descarga todos los Textos Ordenados configurados."""
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Descargando {len(TEXTOS_ORDENADOS)} archivos a {OUT_DIR.relative_to(PROJECT_ROOT)}/")
    print("-" * 60)

    success_count = 0
    fail_count = 0
    for name, url in TEXTOS_ORDENADOS.items():
        ok, msg = download_one(name, url, OUT_DIR)
        print(msg)
        if ok:
            success_count += 1
        else:
            fail_count += 1

    print("-" * 60)
    print(f"Resumen: {success_count} OK, {fail_count} con error")

    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
