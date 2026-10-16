#!/usr/bin/env python3
"""sonda_auditoria.py — Corre un servidor del banco bajo un audit hook de Python (PEP 578) y
registra lo que hace el proceso: módulos importados, archivos abiertos, sockets (creación,
connect, bind, resolución de nombres, envíos) y subprocesos (solo el nombre del ejecutable).
Es la parte dinámica de (b) y (c) del aislamiento de A2.1 para la configuración BM25.

El servidor corre con su propio código, sin cambios: `runpy.run_path(<servidor>,
run_name="__main__")` con el `sys.argv` que tendría lanzado directo. El registro se escribe
al salir el proceso (atexit; el servidor sale normal cuando el cliente cierra stdin).

Uso: <python> -B sonda_auditoria.py <registro.json> <servidor.py> [args del servidor...]
"""
import atexit
import json
import os
import sys

_SALIDA = os.path.abspath(sys.argv[1])
_SERVIDOR = os.path.abspath(sys.argv[2])
_ARGS = sys.argv[3:]
_REG = {"imports": [], "open": [], "socket": [], "subprocess": []}
_SOCKET = {"socket.__new__", "socket.bind", "socket.connect", "socket.connect_ex", "socket.getaddrinfo",
           "socket.gethostbyname", "socket.gethostbyaddr", "socket.sendto", "socket.sendmsg", "socket.getnameinfo"}
_PROC = {"subprocess.Popen", "os.system", "os.exec", "os.posix_spawn", "os.spawn"}


def _hook(evento, args):
    if evento == "import":
        _REG["imports"].append(args[0])
    elif evento == "open":
        if not isinstance(args[0], int):                  # un int es un descriptor ya abierto
            _REG["open"].append(str(args[0]))
    elif evento == "socket.__new__":
        _REG["socket"].append({"evento": evento, "familia": args[1], "tipo": args[2]})
    elif evento in _SOCKET:
        _REG["socket"].append({"evento": evento, "args": [repr(x) for x in args]})
    elif evento in _PROC:
        _REG["subprocess"].append({"evento": evento, "ejecutable": os.path.basename(str(args[0]))})


def _volcar():
    import socket
    for s in _REG["socket"]:
        if s["evento"] == "socket.__new__":
            for k, enum in (("familia", socket.AddressFamily), ("tipo", socket.SocketKind)):
                try:
                    s[k] = enum(int(s[k])).name
                except (TypeError, ValueError):
                    s[k] = repr(s[k])
    mods = sorted(sys.modules)
    with open(_SALIDA, "w", encoding="utf-8") as f:
        json.dump({"servidor": os.path.basename(_SERVIDOR), "args": [os.path.basename(a) if os.path.exists(a) else a for a in _ARGS],
                   "python": sys.version.split()[0], "imports": sorted(set(_REG["imports"])),
                   "sys_modules_al_salir": mods, "open": _REG["open"], "socket": _REG["socket"],
                   "subprocess": _REG["subprocess"]}, f, ensure_ascii=False, indent=1)


sys.addaudithook(_hook)
atexit.register(_volcar)
sys.argv = [_SERVIDOR] + _ARGS
sys.path.insert(0, os.path.dirname(_SERVIDOR))
import runpy  # noqa: E402

try:
    runpy.run_path(_SERVIDOR, run_name="__main__")
except SystemExit:
    pass
