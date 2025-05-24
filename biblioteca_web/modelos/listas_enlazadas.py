class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo = Nodo(dato)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def buscar(self, condicion):
        actual = self.cabeza
        while actual:
            if condicion(actual.dato):
                return actual.dato
            actual = actual.siguiente
        return None

    def eliminar(self, condicion):
        actual = self.cabeza
        previo = None
        while actual:
            if condicion(actual.dato):
                if previo:
                    previo.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True
            previo = actual
            actual = actual.siguiente
        return False

    def listar(self):
        actual = self.cabeza
        datos = []
        while actual:
            datos.append(actual.dato)
            actual = actual.siguiente
        return datos
