# ============================================
#           LISTA ENLAZADA (LinkedList)
# ============================================

class Nodo:
    """Nodo para lista enlazada."""
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    """Lista enlazada simple."""
    def __init__(self):
        self.cabeza = None
        self.tamanio = 0
    
    def agregar(self, dato):
        """Agrega un elemento al final."""
        nuevo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo
        self.tamanio += 1
    
    def agregar_inicio(self, dato):
        """Agrega un elemento al inicio (como pila)."""
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tamanio += 1
    
    def eliminar_inicio(self):
        """Elimina y retorna el primer elemento."""
        if not self.cabeza:
            return None
        dato = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        self.tamanio -= 1
        return dato
    
    def buscar(self, clave, campo):
        """Busca un elemento por campo."""
        actual = self.cabeza
        while actual:
            if actual.dato.get(campo) == clave:
                return actual.dato
            actual = actual.siguiente
        return None
    
    def recorrer(self):
        """Retorna lista con todos los elementos."""
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos
    
    def __len__(self):
        return self.tamanio

# ============================================
#         ESTRUCTURAS PRINCIPALES
# ============================================
historial_lista = ListaEnlazada()  # Historial como Lista Enlazada (Pila) 

# ---------- CATEGORIAS DE HABITACION ----------
categorias = {
    "Simple": {"precio": 80},
    "Doble": {"precio": 110},
    "Matrimonial": {"precio": 150}
}

# ---------- HABITACIONES INDIVIDUALES ----------
habitaciones = [
    # Simples (101-106)
    {"numero": 101, "tipo": "Simple"},
    {"numero": 102, "tipo": "Simple"},
    {"numero": 103, "tipo": "Simple"},
    {"numero": 104, "tipo": "Simple"},
    {"numero": 105, "tipo": "Simple"},
    {"numero": 106, "tipo": "Simple"},
    # Dobles (201-210)
    {"numero": 201, "tipo": "Doble"},
    {"numero": 202, "tipo": "Doble"},
    {"numero": 203, "tipo": "Doble"},
    {"numero": 204, "tipo": "Doble"},
    {"numero": 205, "tipo": "Doble"},
    {"numero": 206, "tipo": "Doble"},
    {"numero": 207, "tipo": "Doble"},
    {"numero": 208, "tipo": "Doble"},
    {"numero": 209, "tipo": "Doble"},
    {"numero": 210, "tipo": "Doble"},
    # Matrimoniales (301-304)
    {"numero": 301, "tipo": "Matrimonial"},
    {"numero": 302, "tipo": "Matrimonial"},
    {"numero": 303, "tipo": "Matrimonial"},
    {"numero": 304, "tipo": "Matrimonial"},
]

def get_habitaciones_disponibles(tipo=None):
    """Retorna habitaciones disponibles, opcionalmente filtradas por tipo."""
    from db import habitaciones_ocupadas
    ocupadas = habitaciones_ocupadas()
    disponibles = [h for h in habitaciones if h["numero"] not in ocupadas]
    if tipo:
        disponibles = [h for h in disponibles if h["tipo"] == tipo]
    return disponibles

def get_precio(tipo):
    """Retorna el precio por noche de un tipo de habitacion."""
    return categorias.get(tipo, {}).get("precio", 0)

def contar_disponibles_por_tipo():
    """Cuenta habitaciones disponibles por tipo."""
    conteo = {}
    for tipo in categorias:
        conteo[tipo] = len(get_habitaciones_disponibles(tipo))
    return conteo

# ----------------------------------------------------
#                   ORDENAMIENTOS
# ----------------------------------------------------

def burbuja(lista):
    arr = lista.copy()
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j]["dni"] > arr[j+1]["dni"]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def seleccion(lista):
    arr = lista.copy()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j]["dni"] < arr[min_idx]["dni"]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insercion(lista):
    arr = lista.copy()
    for i in range(1, len(arr)):
        clave = arr[i]
        j = i - 1
        while j >= 0 and arr[j]["dni"] > clave["dni"]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j+1] = clave
    return arr


def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    menores = [x for x in lista[1:] if x["dni"] < pivote["dni"]]
    mayores = [x for x in lista[1:] if x["dni"] >= pivote["dni"]]
    return quicksort(menores) + [pivote] + quicksort(mayores)

# ----------------------------------------------------
#                   HISTORIAL (PILA - LIFO)
# ----------------------------------------------------

def push_historial(operacion):
    """Agrega al historial usando Lista Enlazada (LIFO)."""
    historial_lista.agregar_inicio(operacion)

def pop_historial():
    """Elimina y retorna la ultima operacion (LIFO)."""
    return historial_lista.eliminar_inicio()

def ver_historial():
    """Retorna todo el historial."""
    return historial_lista.recorrer()

def buscar_en_historial(texto):
    """Busca operaciones que contengan el texto."""
    historial = historial_lista.recorrer()
    return [op for op in historial if texto.lower() in op.lower()]
