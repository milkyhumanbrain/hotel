import json
import os

DATA_DIR = "data"
CLIENTES_FILE = os.path.join(DATA_DIR, "clientes.json")
RESERVAS_FILE = os.path.join(DATA_DIR, "reservas.json")
HOSPEDADOS_FILE = os.path.join(DATA_DIR, "hospedados.json")

def init_data():
    """Crea la carpeta data y archivos si no existen."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    
    if not os.path.exists(CLIENTES_FILE):
        guardar_json(CLIENTES_FILE, [])
    
    if not os.path.exists(RESERVAS_FILE):
        guardar_json(RESERVAS_FILE, [])
    
    if not os.path.exists(HOSPEDADOS_FILE):
        guardar_json(HOSPEDADOS_FILE, [])

def guardar_json(archivo, datos):
    """Guarda datos en archivo JSON."""
    with open(archivo, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=2, ensure_ascii=False)

def cargar_json(archivo):
    """Carga datos de archivo JSON."""
    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# ============================================
#              CLIENTES
# ============================================

def obtener_clientes():
    """Retorna lista de clientes."""
    return cargar_json(CLIENTES_FILE)

def guardar_cliente(cliente):
    """Agrega o actualiza un cliente."""
    clientes = obtener_clientes()
    # Buscar si existe
    for i, c in enumerate(clientes):
        if c['dni'] == cliente['dni']:
            clientes[i] = cliente
            guardar_json(CLIENTES_FILE, clientes)
            return
    # Si no existe, agregar
    clientes.append(cliente)
    guardar_json(CLIENTES_FILE, clientes)

def buscar_cliente(dni):
    """Busca cliente por DNI usando busqueda lineal."""
    clientes = obtener_clientes()
    return busqueda_lineal(clientes, dni)

def busqueda_lineal(lista, dni):
    """Busqueda lineal - O(n)."""
    for item in lista:
        if item['dni'] == dni:
            return item
    return None

def busqueda_binaria(lista_ordenada, dni):
    """Busqueda binaria - O(log n). Requiere lista ordenada por DNI."""
    inicio = 0
    fin = len(lista_ordenada) - 1
    
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista_ordenada[medio]['dni'] == dni:
            return lista_ordenada[medio]
        elif dni < lista_ordenada[medio]['dni']:
            fin = medio - 1
        else:
            inicio = medio + 1
    return None

# ============================================
#              RESERVAS (historial)
# ============================================

def obtener_reservas():
    """Retorna lista de reservas."""
    return cargar_json(RESERVAS_FILE)

def guardar_reserva(reserva):
    """Agrega una reserva."""
    reservas = obtener_reservas()
    reservas.append(reserva)
    guardar_json(RESERVAS_FILE, reservas)

def calcular_ingresos():
    """Calcula ingresos totales usando recursividad."""
    reservas = obtener_reservas()
    return _sumar_ingresos_recursivo(reservas, 0)

def _sumar_ingresos_recursivo(reservas, i):
    """Suma ingresos de forma recursiva."""
    if i >= len(reservas):
        return 0  # Caso base
    return reservas[i].get('costo', 0) + _sumar_ingresos_recursivo(reservas, i + 1)

# ============================================
#              HOSPEDADOS
# ============================================

def obtener_hospedados():
    """Retorna lista de hospedados."""
    return cargar_json(HOSPEDADOS_FILE)

def agregar_hospedado(hospedado):
    """Agrega un hospedado."""
    hospedados = obtener_hospedados()
    hospedados.append(hospedado)
    guardar_json(HOSPEDADOS_FILE, hospedados)

def eliminar_hospedado(num_habitacion):
    """Elimina hospedado por habitacion (check-out)."""
    hospedados = obtener_hospedados()
    hospedado = None
    for i, h in enumerate(hospedados):
        if h['habitacion'] == num_habitacion:
            hospedado = hospedados.pop(i)
            break
    guardar_json(HOSPEDADOS_FILE, hospedados)
    return hospedado

def habitaciones_ocupadas():
    """Retorna lista de numeros de habitacion ocupadas."""
    hospedados = obtener_hospedados()
    return [h['habitacion'] for h in hospedados]

# Inicializar al importar
init_data()
