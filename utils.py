import os

# ============================================
#              FUNCIONES DE UX
# ============================================

def clear_screen():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_separator():
    print("=" * 40)

def print_header(titulo):
    clear_screen()
    print_separator()
    print(f"  {titulo.upper()}")
    print_separator()

def press_enter():
    input("\nPresione Enter para continuar...")

# ============================================
#                  LOGIN
# ============================================
usuarios = {
    "admin": {"clave": "1234", "rol": "admin"},
    "recepcion": {"clave": "2025", "rol": "recepcion"}
}

def login():
    """Login con maximo 3 intentos. Retorna el rol o None."""
    intentos = 3
    
    while intentos > 0:
        print_header("Sistema de Reservas - Login")
        print("(Escribe 'salir' para cerrar)\n")
        usuario = input("Usuario: ").strip().lower()
        
        if usuario == "salir":
            print("\nHasta pronto!")
            return None
        
        clave = input("Contraseña: ").strip()
        
        user_data = usuarios.get(usuario)
        if user_data and user_data["clave"] == clave:
            rol = user_data["rol"]
            print(f"\nAcceso concedido. Bienvenido, {usuario}!")
            print(f"Rol: {rol.upper()}")
            press_enter()
            return rol
        
        intentos -= 1
        if intentos > 0:
            print(f"\nCredenciales incorrectas. Intentos restantes: {intentos}")
            press_enter()
    
    print_header("Acceso Denegado")
    print("Has agotado los intentos permitidos.")
    return None

