#!/usr/bin/env python3
"""sistema_falso_n6.py — El `vm_stat`, el `footprint` y el `docker` falsos de la corrida en seco de N6 y de la prueba en seco del
comando del paso pago: dan, desde un JSON de estado, lo que n6/control_memoria_n6.py lee de la máquina y de Docker,
con la forma de la salida de las herramientas reales. No tocan nada del sistema ni de Docker.

Estado (--estado <json>): {"en_uso_gb", "libre_gb", "huella_mb", "docker_mem_total", "docker_salud"}. La prueba lo cambia entre
ramas, y una sesión del CLI falso puede subir la memoria en uso a mitad de un lote (el plan `sube_memoria_gb`).
  vm_stat                                  las páginas activas (lo en uso), las libres y algunas inactivas, de 16.384 bytes;
  footprint -p <pid>                       «Footprint: <huella_mb> MB» para cualquier pid;
  docker info --format '{{.MemTotal}}'     docker_mem_total;
  docker inspect -f '{{.State.Health.Status}}' <contenedor>    docker_salud;
  docker stats --no-stream --format '{{json .}}' <contenedor>  una línea JSON con cifras sintéticas.
Cualquier otra invocación sale con 1 sin hacer nada.
Uso (lo llaman los envoltorios que arma la prueba en su carpeta de trabajo):
  python -B sistema_falso_n6.py <vm_stat|footprint|docker> --estado <json> [args...]
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

PAGINA = 16384


def main(argv: list[str]) -> int:
    if len(argv) < 3 or argv[1] != "--estado":
        return 2
    herramienta, estado, args = argv[0], json.loads(Path(argv[2]).read_text(encoding="utf-8")), argv[3:]
    if herramienta == "vm_stat":
        uso, libre = round(estado["en_uso_gb"] * 1e9 / PAGINA), round(estado["libre_gb"] * 1e9 / PAGINA)
        print(f"Mach Virtual Memory Statistics: (page size of {PAGINA} bytes)\nPages free:                               {libre}.\n"
              f"Pages active:                             {uso}.\nPages inactive:                           1000.\n"
              f"Pages speculative:                        0.\nPages wired down:                         0.\n"
              f"Pages occupied by compressor:             0.")
        return 0
    if herramienta == "footprint" and args[:1] == ["-p"] and len(args) == 2:
        print(f"proceso [{args[1]}]: 64-bit    Footprint: {estado['huella_mb']} MB ({PAGINA} bytes per page)")
        return 0
    if herramienta == "docker":
        if args == ["info", "--format", "{{.MemTotal}}"]:
            print(estado["docker_mem_total"])
            return 0
        if args[:2] == ["inspect", "-f"] and args[2] == "{{.State.Health.Status}}" and len(args) == 4:
            print(estado["docker_salud"])
            return 0
        if args[:4] == ["stats", "--no-stream", "--format", "{{json .}}"] and len(args) == 5:
            print(json.dumps({"Name": args[4], "MemUsage": "1.0GiB / 2.5GiB", "MemPerc": "40.00%", "CPUPerc": "1.00%",
                              "PIDs": "40"}))
            return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
