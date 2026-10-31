# Proyecto: Centros de Salud (Entregable III)

Aplicación web desarrollada en Django para permitir a los usuarios consultar, filtrar y priorizar centros de salud en la Región de Valparaíso según sus necesidades previsionales, de ubicación y costos.

## Prerrequisitos
- Python instalado (versión 3.10 o superior recomendada).
- Entorno virtual configurado.

## Instrucciones para ejecutar localmente

1. Clonar el repositorio:
   git clone https://github.com/dvasquezh/centros-salud-django.git
   cd Centros-Salud

2. Instalar dependencias (Django):
   pip install django

3. Entrar a la carpeta del proyecto y ejecutar el servidor:
   cd centrosalud
   python manage.py runserver

4. Probar la funcionalidad corazón:
   - Abre tu navegador web e ingresa a: http://127.0.0.1:8000/
   - Utiliza los selectores de seguro (ej. FONASA), comuna (ej. LIMACHE) y prioridad para verificar el procesamiento de los datos precargados.