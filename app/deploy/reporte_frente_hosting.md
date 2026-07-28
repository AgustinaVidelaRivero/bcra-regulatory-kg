# Reporte final — Frente de hosting de la app en AWS (H1-H7)

> Convención de este documento: `<IP>` es la Elastic IP del server y
> `<código>` el código de invitación vigente. Ninguno de los dos se
> escribe acá (el repo puede ser público): la IP está en la consola AWS
> (Elastic IPs → `finreggraph-app-eip`) y el código en
> `/etc/finreggraph.env` del server.

## Estado de las unidades

- **H1** — Reconocimiento y diseño: arquitectura EC2+rol IAM+Bedrock elegida sobre Lightsail; sin tocar zonas congeladas. APROBADA.
- **H2** — Backend Bedrock inyectable (`app/llm_backend.py`, `ModelOverrideClient`), sesiones por usuario/sesión con turno persistente. APROBADA.
- **H3** — Auth Bearer por token (archivo o env), usuario en cada línea del registro, UI con auth. APROBADA.
- **H4** — Aprovisionamiento AWS (rol, SG, key pair, t4g.micro, EIP); invoke a Bedrock desde el rol verificado. APROBADA.
- **H5** — Deploy: rsync selectivo (`app/deploy/sync.sh`), venv, systemd en :80 sin root, reboot-safe. APROBADA.
- **H6** — Registro autoservicio por código de invitación (`POST /register`, UI con localStorage consciente, rate limit 10/h). APROBADA.
- **H7** — Cierre: micro-fixes de UI deployados, verificación final del server, este reporte. (Pendiente de revisión.)

## Inventario AWS (para el teardown)

Región `us-east-1`, cuenta de la autora.

| Tipo | ID | Nombre |
|---|---|---|
| IAM Role | `AROARVR5QKZIFJZ4Q4KQ5` | `finreggraph-app-role` (inline policy `finreggraph-bedrock-invoke`) |
| IAM Instance Profile | `AIPARVR5QKZILU35R4MWZ` | `finreggraph-app-profile` |
| Security Group | `sg-07a3ff5fbf33b5106` | `finreggraph-app-sg` (`sgr-017c2837278750dc2` :80 público; :22 restringido por IP de la autora — dos reglas conviviendo: `sgr-02fef41c95f22b403` casa y `sgr-0ef86adc1905df6f2` VPN del trabajo) |
| Key Pair | `finreggraph-app-key` | pem local: `~/.ssh/finreggraph-app-key.pem` (400) |
| Instancia EC2 | `i-0cc48c5e336aea5fb` | `finreggraph-app` (t4g.micro, us-east-1c, AMI `ami-02c4144237becae44` Ubuntu 24.04 ARM, EBS gp3 10 GB DeleteOnTermination) |
| Elastic IP | `eipalloc-08496d6c2e555a5cd` (assoc `eipassoc-0ab637d0a3ed8977f`) | `finreggraph-app-eip` → `<IP>` |

En el server: `/home/ubuntu/finreggraph/` (código + grafos + `.venv` + `tokens.txt` 600), `/etc/finreggraph.env` (600, root), unit `finreggraph.service` (enabled).

## Runbook operativo

Todas las llamadas SSH usan `-i ~/.ssh/finreggraph-app-key.pem` y el user `ubuntu`.

**Deploy de un cambio:**
```bash
./app/deploy/sync.sh <IP>
ssh -i ~/.ssh/finreggraph-app-key.pem ubuntu@<IP> 'sudo systemctl restart finreggraph'
```

**Ver logs:**
```bash
ssh -i ~/.ssh/finreggraph-app-key.pem ubuntu@<IP> 'sudo journalctl -u finreggraph -f'
```

**Resetear el rate limit de registro** (contador en memoria): reiniciar el servicio (mismo comando del deploy).

**Rotar el código de invitación:**
```bash
ssh -i ~/.ssh/finreggraph-app-key.pem ubuntu@<IP> \
  "sudo sed -i 's/^APP_INVITE_CODE=.*/APP_INVITE_CODE=<código-nuevo>/' /etc/finreggraph.env && sudo systemctl restart finreggraph"
```

**Revocar un usuario** (borra su línea del archivo de tokens; el mapa en memoria se recarga con el restart):
```bash
ssh -i ~/.ssh/finreggraph-app-key.pem ubuntu@<IP> \
  "cd /home/ubuntu/finreggraph && grep -v ':USUARIO$' tokens.txt > t && mv t tokens.txt && chmod 600 tokens.txt && sudo systemctl restart finreggraph"
```

**Bajar los jsonl de sesiones a la máquina local:**
```bash
rsync -avz -e "ssh -i ~/.ssh/finreggraph-app-key.pem" \
  ubuntu@<IP>:/home/ubuntu/finreggraph/app/sessions/ ./sessions_server/
```

**Alta de una IP nueva para SSH** (el :22 está restringido por IP; hoy
conviven dos reglas — casa y VPN del trabajo. Si el `sync.sh` da timeout
de SSH, casi seguro cambió tu IP de salida):
```bash
curl -s https://checkip.amazonaws.com   # tu IP de salida actual
aws ec2 authorize-security-group-ingress --region us-east-1 \
  --group-id sg-07a3ff5fbf33b5106 --protocol tcp --port 22 --cidr <IP-nueva>/32
```
(las reglas que dejen de ser tuyas se dan de baja con
`revoke-security-group-ingress`, mismos parámetros)

**Stop/start de la instancia** (la EIP sobrevive y sigue siendo la misma; detenida se sigue pagando EBS + EIP, no la instancia):
```bash
aws ec2 stop-instances  --region us-east-1 --instance-ids i-0cc48c5e336aea5fb
aws ec2 start-instances --region us-east-1 --instance-ids i-0cc48c5e336aea5fb
```

**Teardown completo (día final, en este orden):**
```bash
aws ec2 terminate-instances --region us-east-1 --instance-ids i-0cc48c5e336aea5fb
aws ec2 wait instance-terminated --region us-east-1 --instance-ids i-0cc48c5e336aea5fb
aws ec2 release-address --region us-east-1 --allocation-id eipalloc-08496d6c2e555a5cd
aws ec2 delete-security-group --region us-east-1 --group-id sg-07a3ff5fbf33b5106
aws ec2 delete-key-pair --region us-east-1 --key-name finreggraph-app-key
rm ~/.ssh/finreggraph-app-key.pem
aws iam remove-role-from-instance-profile --instance-profile-name finreggraph-app-profile --role-name finreggraph-app-role
aws iam delete-instance-profile --instance-profile-name finreggraph-app-profile
aws iam delete-role-policy --role-name finreggraph-app-role --policy-name finreggraph-bedrock-invoke
aws iam delete-role --role-name finreggraph-app-role
```
(El volumen EBS se borra con la instancia por `DeleteOnTermination`. Al final, quitar del user CLI la policy de aprovisionamiento desde la consola.)

## Pendientes conocidos

- **Sesión de aceptación de la autora**: al cierre de H7 el registro autoservicio de su usuario existe en `tokens.txt`, pero todavía no hay ninguna sesión de chat bajo ese usuario en `app/sessions/` del server. Verificación pendiente de que la autora complete su checklist manual desde el celular.
- **TLS y dominio por Cloudflare** — fuera de este frente; hasta entonces los tokens y el código viajan en claro (limitación documentada en el README).
- **Costo real** — el desglose estimado (~USD 10.6/mes: instancia + IPv4 + EBS) quedó sin verificar por API (`pricing:GetProducts` denegado); confirmar en Billing con la primera factura.
- **Quitar la policy de aprovisionamiento** (`finreggraph-provisioning`) del user CLI cuando el deploy esté estable — el server no la necesita (usa su rol) y reduce la superficie del user.
- **A2 (fusión feedback/kg-refinement)** — frente futuro: NO arranca sin prompt explícito de la autora.
