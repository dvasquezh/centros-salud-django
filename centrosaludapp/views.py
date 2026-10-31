from django.shortcuts import render

# Datos precargados de centros de salud para el prototipo (Entregable III)
CENTROS_SALUD = [
    {"nombre": "Hospital de Limache", "seguro": "FONASA", "comuna": "LIMACHE", "costo": 15000, "distancia": 2},
    {"nombre": "Clínica Los Leones", "seguro": "ISAPRE", "comuna": "LIMACHE", "costo": 50000, "distancia": 5},
    {"nombre": "Consultorio Viña del Mar", "seguro": "FONASA", "comuna": "VIÑA DEL MAR", "costo": 5000, "distancia": 12},
    {"nombre": "Hospital Gustavo Fricke", "seguro": "FONASA", "comuna": "VIÑA DEL MAR", "costo": 10000, "distancia": 10},
    {"nombre": "Centro Médico Reñaca", "seguro": "ISAPRE", "comuna": "VIÑA DEL MAR", "costo": 45000, "distancia": 8},
]

def index(request):
    # Capturamos los filtros enviados por el usuario desde el formulario
    seguro_seleccionado = request.GET.get('seguro', '')
    comuna_seleccionada = request.GET.get('comuna', '')
    prioridad = request.GET.get('prioridad', '')

    resultados = CENTROS_SALUD

    # 1. Filtrar por seguro si se seleccionó
    if seguro_seleccionado:
        resultados = [c for c in resultados if c['seguro'] == seguro_seleccionado]

    # 2. Filtrar por comuna si se seleccionó
    if comuna_seleccionada:
        resultados = [c for c in resultados if c['comuna'] == comuna_seleccionada]

    # 3. Ordenar según la prioridad elegida
    if prioridad == 'costo':
        resultados = sorted(resultados, key=lambda x: x['costo'])
    elif prioridad == 'distancia':
        resultados = sorted(resultados, key=lambda x: x['distancia'])

    contexto = {
        'resultados': resultados,
        'seguro_seleccionado': seguro_seleccionado,
        'comuna_seleccionada': comuna_seleccionada,
        'prioridad': prioridad,
    }
    
    return render(request, "centrosaludapp/index.html", contexto)