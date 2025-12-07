from utils import print_header

# Opciones disponibles por rol
MENU_RECEPCION = {
    "1": "Registrar Reserva",
    "2": "Ver Habitaciones",
    "3": "Realizar Check-out",
    "4": "Consultar Clientes",
    "5": "Buscar Cliente por DNI",
    "0": "Salir"
}

MENU_ADMIN = {
    "1": "Registrar Reserva",
    "2": "Ver Habitaciones",
    "3": "Realizar Check-out",
    "4": "Consultar Clientes",
    "5": "Buscar Cliente por DNI",
    "6": "Ver ingresos totales",
    "7": "Ver historial",
    "8": "Reporte diario",
    "0": "Salir"
}

def get_menu_por_rol(rol):
    """Retorna el menu segun el rol."""
    if rol == "admin":
        return MENU_ADMIN
    return MENU_RECEPCION

def mostrar_menu_principal(rol):
    """Muestra el menu segun el rol y retorna la opcion elegida."""
    menu = get_menu_por_rol(rol)
    
    print_header(f"Menu Principal ({rol.upper()})")
    for key, value in menu.items():
        print(f"{key}. {value}")
    print()
    return input("Elija una opcion: ")
