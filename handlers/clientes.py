from utils import print_header, press_enter
from reservation import validar_dni
from storage import quicksort
from db import obtener_clientes, busqueda_lineal, busqueda_binaria


def handle_consultar_clientes():
    """Muestra la lista de clientes ordenados por DNI."""
    print_header("Lista de Clientes")
    clientes = obtener_clientes()
    if clientes:
        clientes_ordenados = quicksort(clientes)
        print(f"Total: {len(clientes)} clientes (ordenados por DNI)\n")
        for c in clientes_ordenados:
            print(f"  {c['nombre']} - DNI: {c['dni']}")
    else:
        print("No hay clientes registrados.")
    press_enter()


def handle_buscar_cliente():
    """Busca un cliente por DNI usando busqueda lineal y binaria."""
    print_header("Buscar Cliente")
    dni_input = input("Ingrese DNI a buscar: ")
    dni, error = validar_dni(dni_input)
    if error:
        print(f"Error: {error}")
        press_enter()
        return
    
    clientes = obtener_clientes()
    
    print("\n--- Busqueda Lineal O(n) ---")
    resultado_lineal = busqueda_lineal(clientes, dni)
    if resultado_lineal:
        print(f"Encontrado: {resultado_lineal['nombre']}")
    else:
        print("No encontrado")
    
    print("\n--- Busqueda Binaria O(log n) ---")
    clientes_ordenados = quicksort(clientes)
    resultado_binaria = busqueda_binaria(clientes_ordenados, dni)
    if resultado_binaria:
        print(f"Encontrado: {resultado_binaria['nombre']}")
    else:
        print("No encontrado")
    
    press_enter()
