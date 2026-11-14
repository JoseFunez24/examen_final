# Guía paso a paso: Odoo 20 en Windows + Docker

## 0. Preparación y seguridad

La instalación usada como referencia está en `C:\odoo20`, con `docker-compose.yml`, una base `odoo2026`, `odoo20-db-1` y `odoo20-odoo-1`. Si el nombre ha cambiado, compruébelo con `docker compose ps`.

**Haz una copia de seguridad antes de instalar:**

```powershell
cd C:\odoo20
docker compose ps
docker compose exec db pg_dump -U odoo -d odoo2026 -Fc -f /tmp/respaldo_odoo2026.dump
docker cp odoo20-db-1:/tmp/respaldo_odoo2026.dump C:\odoo20\respaldo_odoo2026.dump
```

El respaldo se crea primero dentro del contenedor y se copia a Windows para evitar problemas de codificación binaria de PowerShell. Verifica que el archivo tenga tamaño mayor a cero y guárdalo en un lugar seguro. No se incluye ninguna contraseña en este repositorio.

## 1. Copiar las carpetas

Extrae el ZIP de modo que las rutas finales sean:

```text
C:\odoo20\addons\examen_final\
    README.md
    tienda_unicah\__manifest__.py
    unicah_prestamos\__manifest__.py
```

La carpeta `examen_final` es **el repositorio Git**. **No** copiar la carpeta `examen_final` debajo de sí misma.

### Verificar estructura

```powershell
cd C:\odoo20\addons\examen_final
Get-ChildItem
```

## 2. Configurar addons_path para Docker

`C:\odoo20\addons` ya está montada en el contenedor como `/mnt/extra-addons` según la configuración conocida. Los módulos están dentro de una subcarpeta, por lo tanto hay que agregar `/mnt/extra-addons/examen_final` al addons_path.

Primero examina el archivo de configuración que realmente usa el contenedor:

```powershell
cd C:\odoo20
docker compose exec odoo cat /etc/odoo/odoo.conf
```

Si ya tienes un `odoo.conf` en Windows, haz una copia y edítalo. Si no tienes uno, **copia el existente desde el contenedor**:

```powershell
docker cp odoo20-odoo-1:/etc/odoo/odoo.conf C:\odoo20\odoo.conf
```

Dentro de `C:\odoo20\odoo.conf`, en la sección `[options]`, identifica el valor **actual** de `addons_path` y **agrega al final** `,/mnt/extra-addons/examen_final` conservando las rutas anteriores. Si la línea no existe, agrégala incluyendo `/mnt/extra-addons,/mnt/extra-addons/examen_final`.

En `C:\odoo20\docker-compose.yml`, dentro del servicio `odoo`, sección `volumes`, **conserva** el volumen `./addons:/mnt/extra-addons` y agrega:

```yaml
      - ./odoo.conf:/etc/odoo/odoo.conf:ro
```

**No dupliques** la línea si ya existe, y no reemplaces las otras opciones de red, base de datos o puertos.

Luego:

```powershell
docker compose up -d --force-recreate odoo
docker compose exec odoo cat /etc/odoo/odoo.conf
docker compose exec odoo ls /mnt/extra-addons/examen_final
```

**Importante:** `C:\...` es una ruta Windows; **dentro de Docker** se usa `/mnt/...`. Si `ls` no ve los módulos, revisar la carpeta y el volumen antes de continuar.

## 3. Instalar módulos

Asegura que la base de datos esté operativa y realiza la instalación sin dos procesos Odoo simultáneos:

```powershell
cd C:\odoo20
docker compose stop odoo
docker compose run --rm odoo odoo -c /etc/odoo/odoo.conf -d odoo2026 -i tienda_unicah,unicah_prestamos --stop-after-init --no-http
docker compose up -d odoo
```

Odoo debe terminar la instalación **sin traceback**. Después entra a <http://localhost:8069> y prueba con tu usuario existente. Si sale algún error, conserva el mensaje completo y ejecuta:

```powershell
docker compose logs --tail=100 odoo
```

Para aplicar cambios futuros, **actualiza** los módulos (no volver a instalarlos desde cero):

```powershell
docker compose stop odoo
docker compose run --rm odoo odoo -c /etc/odoo/odoo.conf -d odoo2026 -u tienda_unicah,unicah_prestamos --stop-after-init --no-http
docker compose up -d odoo
```

## 4. Revisar en la interfaz

1. **Contactos:** abre un contacto; pestaña **UNICAH** y verifica el tipo de cliente.
2. **Ventas / Configuración / Convenios UNICAH:** deberían figurar convenios de 15 % para estudiantes y 10 % para docentes. Si el menú no aparece, revisa que tu usuario tenga rol de administrador de Ventas.
3. **Ventas / Cotizaciones:** con un cliente estudiante, dos productos y una sección, pulsa **Aplicar convenio** y verifica los descuentos y el chatter. Activa descuentos en Configuración de Ventas si hace falta.
4. **Validaciones:** prueba datos inválidos como se describe en `PRUEBAS_Y_CAPTURAS.md`.
5. **Ventas / Cotizaciones:** comprueba el ahorro, el filtro y la agrupación.
6. **Préstamos UNICAH / Préstamos de equipos:** registra un préstamo, devuélvelo y revisa su pestaña en el contacto.

## 5. GitHub: mínimo 3 commits

Ejecuta los comandos desde `C:\odoo20\addons\examen_final`, que **tiene su propio `.git`**:

```powershell
cd C:\odoo20\addons\examen_final
git init
git add .gitignore README.md GUIA_INSTALACION.md PRUEBAS_Y_CAPTURAS.md
git commit -m "docs: instrucciones y casos de prueba"

git add tienda_unicah
git commit -m "feat: convenios y validaciones de tienda UNICAH"

git add unicah_prestamos JUSTIFICACION_EXAMEN.md
git commit -m "feat: prestamos de equipos y justificacion"
```

Si el documento de justificación está fuera de la carpeta, omítelo del último `git add`. Antes de publicar, completa tu **número de cuenta real** en `README.md`, añade el PDF definitivo con capturas (si lo solicita el docente) y realiza un commit adicional.

Crea un repositorio **vacío** en GitHub, por ejemplo `examen-odoo-unicah`, sin inicializar README, y copia la URL que GitHub te muestre (no hay que inventarla). Luego:

```powershell
git branch -M main
git remote add origin https://github.com/TU_USUARIO/examen-odoo-unicah.git
git push -u origin main
```

Sustituye `TU_USUARIO` y comprueba que el repositorio sea **público**. Si `origin` ya existe usa `git remote -v` antes de cambiarlo.

## 6. Entrega final

- Pegar las **seis capturas reales** en el documento de justificación editable y exportar a PDF.
- Completar nombre, número de cuenta y enlace público GitHub.
- Verificar el historial de al menos tres commits: `git log --oneline`.
- Confirmar que GitHub contiene ambos módulos y el README.

## Observaciones

- El enunciado describe el comando `python odoo-bin -c odoo.conf -i tienda_unicah`, propio de una instalación directa. En Docker se ejecuta mediante `docker compose run` contra la base `odoo2026`.
- **Odoo 20 usa `security/ir.access.csv`**, distinto del nombre y formato de permisos de versiones anteriores.
- El proyecto se entrega como código preparado, **sin afirmar que se probó en tu contenedor**; el paso de instalación y las capturas debe realizarse en tu equipo.
