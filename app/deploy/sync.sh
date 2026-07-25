#!/usr/bin/env bash
# Sincroniza al server SOLO lo que la app necesita, preservando las rutas
# relativas que app/main.py espera (REPO_ROOT del server = /home/ubuntu/finreggraph):
#   - app/ completo (sin sessions/ local ni caches de Python)
#   - data/experiment/evaluacion/{loader.py,harness.py} (únicos módulos que
#     la app importa de evaluacion/; verificado por sus imports)
#   - data/experiment/*/kg.json (los grafos)
# Uso: app/deploy/sync.sh <IP-del-server>
set -euo pipefail
IP="${1:?Uso: sync.sh <IP-del-server>}"
KEY="${HOME}/.ssh/finreggraph-app-key.pem"
cd "$(dirname "$0")/../.."   # raíz del repo local
exec rsync -avzR -e "ssh -i ${KEY}" \
  --exclude='app/sessions' --exclude='__pycache__' --exclude='*.pyc' \
  app \
  data/experiment/evaluacion/loader.py \
  data/experiment/evaluacion/harness.py \
  data/experiment/*/kg.json \
  "ubuntu@${IP}:/home/ubuntu/finreggraph/"
