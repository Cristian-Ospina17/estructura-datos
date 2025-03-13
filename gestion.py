from datetime import datetime

class Tarea:
    def __init__(self, descripcion, prioridad, fecha_vencimiento):
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.fecha_vencimiento = datetime.strptime(fecha_vencimiento, "%Y-%m-%d")
        self.next = None
    
    def __str__(self):
        return f"{self.prioridad} - {self.descripcion}, vence el {self.fecha_vencimiento.strftime('%Y-%m-%d')}"

class ListaTareas:
    def __init__(self):
        self.head = None

    def agregar_tarea(self, descripcion, prioridad, fecha_vencimiento):
        nueva = Tarea(descripcion, prioridad, fecha_vencimiento)
        if not self.head or (self.head.prioridad > prioridad or 
                             (self.head.prioridad == prioridad and self.head.fecha_vencimiento > nueva.fecha_vencimiento)):
            nueva.next, self.head = self.head, nueva
        else:
            actual = self.head
            while actual.next and (actual.next.prioridad < prioridad or 
                                   (actual.next.prioridad == prioridad and actual.next.fecha_vencimiento <= nueva.fecha_vencimiento)):
                actual = actual.next
            nueva.next, actual.next = actual.next, nueva
        print(f"Tarea '{descripcion}' agregada.")

    def eliminar_tarea(self, descripcion=None, posicion=None):
        if not self.head:
            print("Lista vacía.")
            return
        
        if descripcion:
            actual, anterior = self.head, None
            while actual and actual.descripcion != descripcion:
                anterior, actual = actual, actual.next
            
            if actual:
                if anterior:
                    anterior.next = actual.next
                else:
                    self.head = actual.next
                print(f"Tarea '{descripcion}' eliminada.")
            else:
                print(f"Tarea '{descripcion}' no encontrada.")
            return
        
        if posicion is not None:
            if posicion == 0:
                self.head = self.head.next
                print("Tarea en posición 0 eliminada.")
                return
            
            actual, anterior, i = self.head, None, 0
            while actual and i < posicion:
                anterior, actual, i = actual, actual.next, i + 1
            
            if actual:
                anterior.next = actual.next
                print(f"Tarea en posición {posicion} eliminada.")
            else:
                print(f"No hay tarea en posición {posicion}.")

    def mostrar_tareas(self):
        actual = self.head
        print("\nLista de tareas ordenadas:")
        if not actual:
            print("No hay tareas en la lista.")
        while actual:
            print(actual)
            actual = actual.next

    def buscar_tarea(self, descripcion):
        actual = self.head
        while actual:
            if actual.descripcion == descripcion:
                print("Tarea encontrada:\n", actual)
                return actual
            actual = actual.next
        print(f"Tarea '{descripcion}' no encontrada.")
        return None

    def completar_tarea(self, descripcion):
        tarea = self.buscar_tarea(descripcion)
        if tarea:
            self.eliminar_tarea(descripcion)
            print(f"Tarea '{descripcion}' marcada como completada.")

# 🔹 MENÚ INTERACTIVO
lista = ListaTareas()

while True:
    print("\n📌 MENÚ DE TAREAS:")
    print("1️⃣ Agregar tarea")
    print("2️⃣ Ver tareas")
    print("3️⃣ Eliminar tarea")
    print("4️⃣ Buscar tarea")
    print("5️⃣ Marcar tarea como completada")
    print("6️⃣ Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        d = input("Descripción: ")
        try:
            p = int(input("Prioridad (1 alta, 3 baja): "))
            f = input("Fecha (YYYY-MM-DD): ")
            lista.agregar_tarea(d, p, f)
        except ValueError:
            print("Error: Prioridad debe ser un número y la fecha debe estar en formato correcto.")

    elif opcion == "2":
        lista.mostrar_tareas()

    elif opcion == "3":
        tipo = input("¿Eliminar por descripción (D) o posición (P)? ").lower()
        if tipo == "d":
            desc = input("Ingresa la descripción de la tarea a eliminar: ")
            lista.eliminar_tarea(descripcion=desc)
        elif tipo == "p":
            try:
                pos = int(input("Ingresa la posición de la tarea a eliminar: "))
                lista.eliminar_tarea(posicion=pos)
            except ValueError:
                print("Error: La posición debe ser un número.")

    elif opcion == "4":
        desc = input("Ingresa la descripción de la tarea a buscar: ")
        lista.buscar_tarea(desc)

    elif opcion == "5":
        desc = input("Ingresa la descripción de la tarea completada: ")
        lista.completar_tarea(desc)

    elif opcion == "6":
        print("Saliendo del gestor de tareas. ¡Hasta luego! 👋")
        break

    else:
        print("Opción inválida. Inténtalo de nuevo.")
