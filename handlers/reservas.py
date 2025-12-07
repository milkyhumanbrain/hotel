import datetime
from utils import print_header, press_enter
from reservation import mostrar_disponibilidad, validar_dni, mostrar_resumen_reserva, formatear_nombre
from storage import categorias, habitaciones, get_habitaciones_disponibles, get_precio, push_historial
from db import guardar_cliente, buscar_cliente, guardar_reserva, agregar_hospedado, eliminar_hospedado, obtener_hospedados


def mostrar_wizard(paso, tipo=None, num_hab=None, dias=None, cliente=None, precio=None):
    """Muestra el estado actual del wizard de reserva."""
    print_header("Nueva Reserva")
    
    if tipo or num_hab or dias or cliente:
        print("--- Resumen ---")
        if tipo:
            print(f"  Tipo: {tipo} (S/ {precio}/noche)")
        if num_hab:
            print(f"  Habitacion: {num_hab}")
        if dias:
            costo = precio * dias if precio else 0
            print(f"  Dias: {dias}")
            print(f"  Total: S/ {costo}")
        if cliente:
            print(f"  Cliente: {cliente['nombre']} (DNI: {cliente['dni']})")
        print()


def handle_registrar_reserva():
    """Maneja el flujo completo de registrar una reserva."""
    tipos = list(categorias.keys())
    tipo = None
    num_hab = None
    dias = None
    cliente = None
    precio = None
    
    mostrar_wizard(1)
    mostrar_disponibilidad()
    print()
    
    while True:
        try:
            opcion = int(input("Seleccione tipo de habitacion (1-3, 0 para cancelar): "))
            if opcion == 0:
                print("Reserva cancelada.")
                press_enter()
                return
            if opcion < 1 or opcion > 3:
                print("Opcion invalida. Intente de nuevo.")
                continue
            tipo = tipos[opcion - 1]
            precio = get_precio(tipo)
            break
        except ValueError:
            print("Debe ingresar un numero. Intente de nuevo.")
    
    disponibles = get_habitaciones_disponibles(tipo)
    if not disponibles:
        print(f"\nNo hay habitaciones {tipo} disponibles.")
        press_enter()
        return
    
    mostrar_wizard(2, tipo=tipo, precio=precio)
    print(f"Habitaciones {tipo} disponibles:")
    for h in disponibles:
        print(f"  - Habitacion {h['numero']}")
    print()
    
    while True:
        try:
            num_hab = int(input("Numero de habitacion (0 para cancelar): "))
            if num_hab == 0:
                print("Reserva cancelada.")
                press_enter()
                return
            hab_seleccionada = None
            for h in disponibles:
                if h["numero"] == num_hab:
                    hab_seleccionada = h
                    break
            if not hab_seleccionada:
                print("Habitacion no disponible. Intente de nuevo.")
                continue
            break
        except ValueError:
            print("Debe ingresar un numero. Intente de nuevo.")
    
    mostrar_wizard(3, tipo=tipo, num_hab=num_hab, precio=precio)
    
    while True:
        try:
            dias = int(input("Dias de estadia: "))
            if dias < 1:
                print("Debe ser al menos 1 dia. Intente de nuevo.")
                continue
            break
        except ValueError:
            print("Debe ingresar un numero. Intente de nuevo.")
    
    mostrar_wizard(4, tipo=tipo, num_hab=num_hab, dias=dias, precio=precio)
    print("--- Datos del Cliente ---")
    
    while True:
        dni_input = input("DNI (8 digitos, 0 para cancelar): ")
        if dni_input.strip() == "0":
            print("Reserva cancelada.")
            press_enter()
            return
        dni, error = validar_dni(dni_input)
        if error:
            print(f"Error: {error} Intente de nuevo.")
            continue
        break

    cliente = buscar_cliente(dni)

    if not cliente:
        print("Cliente no registrado.")
        nombre = input("Nombre del cliente: ")
        nombre = formatear_nombre(nombre)
        cliente = {"dni": dni, "nombre": nombre}
        guardar_cliente(cliente)
        print(f"Cliente registrado: {cliente['nombre']}")
    else:
        print(f"Cliente encontrado: {cliente['nombre']}")

    costo = precio * dias
    mostrar_wizard(5, tipo=tipo, num_hab=num_hab, dias=dias, cliente=cliente, precio=precio)
    
    print("--- Confirmar Reserva ---")
    print(f"Total a pagar: S/ {costo}\n")
    confirmar = input("Confirmar reserva? (s/n): ")
    
    if confirmar.lower() not in ("s", "si", "1", "y"):
        print("Reserva cancelada.")
        press_enter()
        return

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    reserva = {
        "cliente": cliente["nombre"],
        "dni": cliente["dni"],
        "habitacion": num_hab,
        "tipo": tipo,
        "dias": dias,
        "costo": costo,
        "fecha": timestamp
    }
    guardar_reserva(reserva)
    
    hospedado = {
        "nombre": cliente["nombre"],
        "dni": cliente["dni"],
        "habitacion": num_hab,
        "tipo": tipo,
        "dias": dias,
        "costo": costo
    }
    agregar_hospedado(hospedado)
    push_historial(f"[{timestamp}] Reserva: {cliente['nombre']} - Hab {num_hab} - S/ {costo}")
    
    mostrar_resumen_reserva(cliente, tipo, num_hab, dias, costo)
    print(f"\nCliente hospedado en habitacion {num_hab}.")
    press_enter()


def handle_ver_habitaciones():
    """Muestra todas las habitaciones con su estado."""
    print_header("Estado de Habitaciones")
    
    hospedados = obtener_hospedados()
    ocupadas = {}
    for c in hospedados:
        num = c.get('habitacion')
        if num:
            ocupadas[num] = c
    
    for tipo in categorias:
        precio = get_precio(tipo)
        print(f"\n--- {tipo} (S/ {precio}/noche) ---")
        
        for h in habitaciones:
            if h['tipo'] == tipo:
                num = h['numero']
                if num in ocupadas:
                    cliente = ocupadas[num]
                    dias = cliente.get('dias', '?')
                    print(f"  [{num}] OCUPADA - {cliente['nombre']} ({dias} dias)")
                else:
                    print(f"  [{num}] Disponible")
    
    total = len(habitaciones)
    ocupadas_count = len(ocupadas)
    disponibles_count = total - ocupadas_count
    print(f"\n--- Resumen ---")
    print(f"Total: {total} | Ocupadas: {ocupadas_count} | Disponibles: {disponibles_count}")
    
    press_enter()


def handle_checkout():
    """Realiza check-out de un cliente por numero de habitacion."""
    print_header("Realizar Check-out")
    
    hospedados = obtener_hospedados()
    if not hospedados:
        print("No hay clientes hospedados.")
        press_enter()
        return
    
    print("Habitaciones ocupadas:\n")
    for c in hospedados:
        num_hab = c.get('habitacion', 'N/A')
        tipo = c.get('tipo', '')
        print(f"  Hab {num_hab} ({tipo}) - {c['nombre']}")
    
    while True:
        print()
        try:
            num_input = int(input("Numero de habitacion para check-out (0 para cancelar): "))
            if num_input == 0:
                print("Check-out cancelado.")
                press_enter()
                return
            
            cliente_encontrado = eliminar_hospedado(num_input)
            
            if cliente_encontrado:
                print(f"\n--- Check-out ---")
                print(f"Cliente: {cliente_encontrado['nombre']}")
                print(f"DNI: {cliente_encontrado['dni']}")
                print(f"Habitacion: {num_input} ({cliente_encontrado.get('tipo', '')})")
                print(f"Dias: {cliente_encontrado.get('dias', 'N/A')}")
                print(f"\nHabitacion {num_input} liberada.")
                print("Gracias por su estadia!")
                
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                push_historial(f"[{timestamp}] Check-out: {cliente_encontrado['nombre']} - Hab {num_input}")
                break
            else:
                print("Habitacion no encontrada o no ocupada. Intente de nuevo.")
        except ValueError:
            print("Debe ingresar un numero. Intente de nuevo.")
    
    press_enter()
