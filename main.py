from utils import login, press_enter
from menu import mostrar_menu_principal, get_menu_por_rol
import handlers

OPCIONES = {
    "1": handlers.handle_registrar_reserva,
    "2": handlers.handle_ver_habitaciones,
    "3": handlers.handle_checkout,
    "4": handlers.handle_consultar_clientes,
    "5": handlers.handle_buscar_cliente,
    "6": handlers.handle_ver_ingresos,
    "7": handlers.handle_ver_historial,
    "8": handlers.handle_reporte_diario,
}

def main(rol):
    menu_disponible = get_menu_por_rol(rol)
    
    while True:
        opc = mostrar_menu_principal(rol)
        
        if opc == "0":
            handlers.handle_salir()
            break
        elif opc in menu_disponible and opc in OPCIONES:
            OPCIONES[opc]()
        else:
            print("Opcion no disponible.")
            press_enter()

if __name__ == "__main__":
    rol = login()
    if rol:
        main(rol)
    else:
        print("\nAcceso denegado.")
