class Animal:
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo
        self.next = None
    
    def __str__(self):
        return f"{self.tipo} - {self.nombre}, {self.edad} años"

class ListaEnlazada:
    def __init__(self):
        self.head = None
    
    def agregar_animal(self, nombre, edad, tipo):
        if self.existe_animal(nombre, tipo):
            print("Error: El animal ya está registrado.")
            return
        
        nuevo_animal = Animal(nombre, edad, tipo)
        if self.head is None:
            self.head = nuevo_animal
        else:
            actual = self.head
            while actual.next:
                actual = actual.next
            actual.next = nuevo_animal
    
    def existe_animal(self, nombre, tipo):
        actual = self.head
        while actual:
            if actual.nombre == nombre and actual.tipo == tipo:
                return True
            actual = actual.next
        return False
    
    def mostrar_animales_iterativo(self):
        actual = self.head
        while actual:
            print(actual)
            actual = actual.next
    
    def mostrar_animales_recursivo(self, nodo=None):
        if nodo is None:
            nodo = self.head
        if nodo is None:
            return
        print(nodo)
        if nodo.next:
            self.mostrar_animales_recursivo(nodo.next)

    def agregar_animales_manual(self):
        while True:
            nombre = input("Ingrese el nombre del animal (o 'salir' para terminar): ")
            if nombre.lower() == 'salir':
                break
            edad = int(input("Ingrese la edad del animal: "))
            tipo = input("Ingrese el tipo de animal: ")
            self.agregar_animal(nombre, edad, tipo)


zoologico = ListaEnlazada()
zoologico.agregar_animales_manual()

print("\nAnimales (iterativo):")
zoologico.mostrar_animales_iterativo()

print("\nAnimales (recursivo):")
zoologico.mostrar_animales_recursivo()
