from utils import print_header, press_enter
from storage import ver_historial, pop_historial, buscar_en_historial
from db import obtener_clientes, obtener_reservas, obtener_hospedados, calcular_ingresos


def handle_ver_ingresos():
    """Muestra los ingresos totales (calculado recursivamente)."""
    print_header("Ingresos Totales")
    total = calcular_ingresos()
    print(f"Ingresos totales (recursivo): S/ {total}")
    press_enter()


def handle_ver_historial():
    """Muestra el historial de operaciones con filtros."""
    while True:
        print_header("Historial de Operaciones")
        historial = ver_historial()
        
        if not historial:
            print("No hay operaciones registradas.")
            press_enter()
            return
        
        print("Ultimas operaciones (LIFO - Pila):\n")
        for i, op in enumerate(historial, 1):
            print(f"  {i}. {op}")
        
        print("\n--- Opciones ---")
        print("[1] Filtrar por Reservas")
        print("[2] Filtrar por Check-outs")
        print("[3] Buscar por texto")
        print("[D] Deshacer ultima operacion")
        print("[Enter] Volver al menu")
        
        opcion = input("\nOpcion: ").strip().lower()
        
        if opcion == "1":
            mostrar_historial_filtrado("Reserva")
        elif opcion == "2":
            mostrar_historial_filtrado("Check-out")
        elif opcion == "3":
            texto = input("Buscar: ").strip()
            if texto:
                mostrar_historial_filtrado(texto)
        elif opcion == "d":
            eliminada = pop_historial()
            if eliminada:
                print(f"\nOperacion eliminada: {eliminada}")
                press_enter()
        else:
            return

def mostrar_historial_filtrado(filtro):
    """Muestra historial filtrado por texto."""
    resultados = buscar_en_historial(filtro)
    
    print_header(f"Historial - Filtro: '{filtro}'")
    if resultados:
        print(f"Encontrados: {len(resultados)} resultados\n")
        for i, op in enumerate(resultados, 1):
            print(f"  {i}. {op}")
    else:
        print("No se encontraron resultados.")
    press_enter()


def handle_reporte_diario():
    """Genera y muestra el reporte diario."""
    print_header("Reporte Diario")
    
    clientes = obtener_clientes()
    reservas = obtener_reservas()
    hospedados = obtener_hospedados()
    ingresos = calcular_ingresos()
    
    por_tipo = {}
    for r in reservas:
        tipo = r.get('tipo', 'Otro')
        por_tipo[tipo] = por_tipo.get(tipo, 0) + 1
    
    print(f"  Total clientes: {len(clientes)}")
    print(f"  Total reservas: {len(reservas)}")
    print(f"  Hospedados actualmente: {len(hospedados)}")
    print(f"\n  Reservas por tipo:")
    for tipo, cantidad in por_tipo.items():
        print(f"    - {tipo}: {cantidad}")
    print(f"\n  Ingresos totales: S/ {ingresos}")
    press_enter()


def handle_salir():
    """Muestra mensaje de despedida."""
    print_header("Hasta Pronto")
    print("Cerrando sesion...")
