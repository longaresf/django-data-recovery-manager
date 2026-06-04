# Django Database Migrations & Data Recovery Manager

Este repositorio contiene un proyecto especializado en el desarrollo Backend con **Django**, enfocado en la gestión avanzada del ciclo de vida de bases de datos a través de su ORM. El sistema implementa estrategias robustas para el control de versiones de esquemas mediante **migraciones**, automatización de llenado de datos (*data seeding*), y flujos seguros de respaldo y **recuperación de información** en un entorno controlado.

## 🚀 Características y Capacidades Técnicas

* **Control de Versiones de Base de Datos:** Uso avanzado del sistema de migraciones de Django para la creación, modificación y evolución estructural de tablas sin pérdida de consistencia.
* **Estrategia de Recuperación de Datos:** Implementación de mecanismos de respaldo (*backup*) y restauración (*restore*) de estados de la base de datos mediante comandos nativos de Django (`dumpdata` y `loaddata`).
* **Modelado de Datos Avanzado:** Definición de esquemas relacionales, restricciones de integridad, relaciones (One-to-Many / Many-to-Many) y optimización de consultas a través del ORM.
* **Sembrado de Datos (Seeding):** Automatización del proceso de carga de datos iniciales o de prueba utilizando archivos de configuración estructurados (JSON/YAML).

## 🛠️ Stack Tecnológico

* **Framework Principal:** Django 4.x / 5.x (Python)
* **ORM:** Django ORM
* **Base de Datos:** [Ejemplo: PostgreSQL / SQLite]
* **Formatos de Serialización:** JSON

## ⚙️ Arquitectura del Proyecto y Solución de Problemas

El núcleo de este desarrollo consistió en simular un escenario real de mantenimiento y contingencia en servidores de producción:

1. **Evolución del Esquema (Migraciones):** Se gestionaron flujos de cambios estructurales en los modelos de Django, garantizando que el paso de esquemas antiguos a nuevos se realizara de forma fluida mediante los comandos `makemigrations` y `migrate`.
2. **Consistencia en la Recuperación:** Se diseñó una arquitectura donde el estado completo del sistema de base de datos puede ser serializado a un archivo JSON plano, permitiendo una recuperación ante fallos (*Disaster Recovery*) inmediata que restaura la integridad de las relaciones entre tablas.
3. **Aislamiento de Entornos:** Configuración orientada a la separación de datos de desarrollo y producción para ejecutar pruebas de migración seguras.

## 📌 Comandos Clave Utilizados

* `python manage.py makemigrations` - Generación de los archivos de migración basados en los cambios del modelo.
* `python manage.py migrate` - Aplicación e impacto de los cambios estructurales en el motor de base de datos.
* `python manage.py dumpdata > backup.json` - Serialización y respaldo de la base de datos completa.
* `python manage.py loaddata backup.json` - Proceso de recuperación, parseo e inyección de datos respaldados.

## 🔧 Instalación y Configuración Local

Sigue estos pasos para desplegar el entorno de pruebas localmente:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/longaresf/django-database-migrations.git](https://github.com/longaresf/django-database-migrations.git)
   ````
2. Ingresar al directorio:
   Bash
   cd django-database-migrations

3. Crear y activar un entorno virtual (Recomendado):
   Bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa: venv\Scripts\activate

4. Instalar dependencias:
   Bash
   pip install -r requirements.txt

5. Ejecutar migraciones y restaurar datos:
   Bash
   python manage.py migrate
   python manage.py loaddata [nombre_del_archivo_de_respaldo].json

6. Iniciar el servidor de desarrollo:
   Bash
   python manage.py runserver

   ✒️ Créditos y Autoría

    Francisco Longares - Desarrollador Backend Python - longaresf

    Este proyecto representa la resolución de los hitos avanzados prácticos del programa de formación Full Stack Python en Desafío Latam.
