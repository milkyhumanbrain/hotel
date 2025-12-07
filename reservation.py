import datetime
from storage import categorias, contar_disponibles_por_tipo
from utils import print_separator, print_header

# ============================================
#         VALIDACIONES CON STRINGS
# ============================================

def validar_dni(dni_str):
    """Valida DNI usando metodos de string."""
    dni_str = dni_str.strip()
    if not dni_str.isdigit():
        return None, "El DNI debe contener solo numeros."
    if len(dni_str) != 8:
        return None, "El DNI debe tener 8 digitos."
    return int(dni_str), None

def formatear_nombre(nombre):
    """Formatea nombre usando metodos de string."""
    nombre = nombre.strip()
    nombre = " ".join(nombre.split())
    nombre = nombre.title()
    return nombre

def mostrar_disponibilidad():
    """Muestra disponibilidad de habitaciones."""
    print("\n--- Disponibilidad de Habitaciones ---")
    conteo = contar_disponibles_por_tipo()
    idx = 1
    for tipo, data in categorias.items():
        disponibles = conteo.get(tipo, 0)
        print(f"{idx}. {tipo} - S/ {data['precio']}/noche - Disponibles: {disponibles}")
        idx += 1

def mostrar_resumen_reserva(cliente, tipo, numero, dias, costo):
    """Muestra resumen de reserva con formato."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print_header("Resumen de Reserva")
    print_separator()
    print(f"Fecha: {timestamp}")
    print(f"Cliente: {cliente['nombre']}")
    print(f"DNI: {cliente['dni']}")
    print(f"Habitacion: {numero} ({tipo})")
    print(f"Dias: {dias}")
    print(f"Costo Total: S/ {costo}")
    print_separator()
