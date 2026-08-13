"""Descarga los PDFs del inventario a ../pdfs/ y registra el resultado.

Idempotente: si el destino ya existe con tamaño > 0, no toca la red.
Sin dependencias de red del pipeline sellado: usa urllib de la stdlib.

Salidas:
  ../pdfs/<id>.pdf
  ../descarga_log.json   (por id: url, http, bytes, content-type, sha256, estado)
"""

from __future__ import annotations

import csv
import hashlib
import json
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

AQUI = Path(__file__).resolve().parent
PREP = AQUI.parent
PDFS = PREP / "pdfs"

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 " \
     "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
REINTENTOS = 3
ESPERA = 2.0


def normalizar_url(url: str) -> str:
    """Percent-encoding del path. El índice publica al menos un archivo con
    guion largo en el nombre (t-RI–SPI.pdf, U+2013): urllib no puede poner ese
    carácter en la línea de request y aborta antes de tocar la red."""
    p = urllib.parse.urlsplit(url)
    return urllib.parse.urlunsplit(
        (p.scheme, p.netloc, urllib.parse.quote(p.path, safe="/%"), p.query, p.fragment))


def descargar(url: str, destino: Path) -> dict:
    ultimo = ""
    for intento in range(1, REINTENTOS + 1):
        try:
            req = urllib.request.Request(normalizar_url(url), headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=120) as resp:
                datos = resp.read()
                ctype = resp.headers.get("Content-Type", "")
                http = resp.status
            destino.write_bytes(datos)
            return {"estado": "descargado", "http": http, "bytes": len(datos),
                    "content_type": ctype, "intentos": intento,
                    "sha256": hashlib.sha256(datos).hexdigest()}
        except urllib.error.HTTPError as e:
            ultimo = f"HTTPError {e.code}"
        except Exception as e:                    # noqa: BLE001 — se reporta textual
            ultimo = f"{type(e).__name__}: {e}"
        time.sleep(ESPERA * intento)
    return {"estado": "error", "error": ultimo, "intentos": REINTENTOS}


def main() -> None:
    PDFS.mkdir(parents=True, exist_ok=True)
    filas = list(csv.DictReader((PREP / "inventario_tos.csv").open(encoding="utf-8")))
    log: dict[str, dict] = {}
    log_path = PREP / "descarga_log.json"
    if log_path.exists():
        log = json.loads(log_path.read_text(encoding="utf-8"))

    for i, f in enumerate(filas, 1):
        ident, url = f["id"], f["url_pdf"]
        destino = PDFS / f"{ident}.pdf"
        if destino.exists() and destino.stat().st_size > 0 and log.get(ident, {}).get("estado") in ("descargado", "ya_en_disco"):
            continue
        r = descargar(url, destino)
        r["url"] = url
        log[ident] = r
        print(f"[{i:3d}/{len(filas)}] {ident:28s} {r['estado']:11s} "
              f"{r.get('bytes', r.get('error', ''))}", flush=True)
        log_path.write_text(json.dumps(log, ensure_ascii=False, indent=1), encoding="utf-8")
        time.sleep(0.4)

    ok = sum(1 for v in log.values() if v["estado"] == "descargado")
    print(f"\nOK={ok}  ERROR={len(log) - ok}  archivos_en_disco={len(list(PDFS.glob('*.pdf')))}")


if __name__ == "__main__":
    main()
