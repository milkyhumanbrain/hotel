# Sistema de Reservas de Hotel

Sistema para gestionar reservas de hotel desde la consola con persistencia de datos.

## Como funciona

**Inicio de Sesion:** Escribe 'salir' para cerrar. Hay dos roles:
- **admin** (contraseña: 1234) - Acceso completo
- **recepcion** (contraseña: 2025) - Operaciones básicas

**Menu Recepcion:**
- Registrar Reserva
- Ver Habitaciones
- Realizar Check-out
- Consultar Clientes
- Buscar Cliente por DNI

**Menu Admin (todo lo anterior mas):**
- Ver ingresos totales
- Ver historial (con filtros)
- Reporte diario

**Registrar Reserva:**
1. Seleccionas tipo de habitacion (Simple, Doble, Matrimonial)
2. Eliges numero de habitacion disponible
3. Ingresas dias de estadia
4. Ingresas DNI del cliente (se registra si no existe)
5. Confirmas y el cliente queda hospedado

**Ver Habitaciones:** Muestra todas las habitaciones por categoria, cuales estan ocupadas, por quien y cuantos dias.

**Realizar Check-out:** Seleccionas número de habitacion y se libera.

**Ver Historial:** Muestra operaciones con opciones de filtrar por Reservas, Check-outs, buscar por texto.

## Persistencia de Datos

Los datos se guardan en archivos JSON en la carpeta `data/`:
- `clientes.json` - Clientes registrados
- `reservas.json` - Historial de reservas
- `hospedados.json` - Clientes actualmente hospedados

Los datos persisten entre sesiones y cambios de usuario.

## Como ejecutar

```bash
python3 main.py
```

O usando Make:

```bash
make run    # Ejecutar con login
make admin  # Dev: entrar como admin
make rec    # Dev: entrar como recepcion
make setup  # Crear entorno virtual
make clean  # Limpiar
```

**Instalar Make:**
- **macOS:** Ya viene instalado
- **Linux:** `sudo apt install make`
- **Windows:** Usar [WSL](https://learn.microsoft.com/es-es/windows/wsl/install) o [Chocolatey](https://chocolatey.org/install) (`choco install make`)

## Estructura del Proyecto

- `main.py` - Punto de entrada
- `menu.py` - Menus por rol
- `utils.py` - Login y UX
- `reservation.py` - Validaciones
- `storage.py` - Habitaciones, algoritmos
- `db.py` - Persistencia JSON
- `handlers/` - Logica de cada opcion del menu
- `data/` - Archivos JSON de datos

## Conceptos del Curso

**Fundamentos:** Variables, I/O, estructuras de control

**Strings:** `.strip()`, `.lower()`, `.title()`, `.isdigit()`, `.split()`

**Estructuras de Datos:**
- Listas para habitaciones
- Lista Enlazada (`Nodo` + `ListaEnlazada`) para historial
- Pila (LIFO) con push/pop en historial

**Algoritmos de Busqueda:** Lineal y Binaria (en Buscar Cliente)

**Algoritmos de Ordenamiento:** Burbuja, Seleccion, Insercion, Quicksort

**Recursividad:** `quicksort()`, `_sumar_ingresos_recursivo()`

**Archivos:** Lectura/escritura JSON para persistencia
