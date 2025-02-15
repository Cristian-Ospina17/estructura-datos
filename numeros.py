numeros = list()

def agregar(numero: int) -> None:
    numeros.append(numero)

def eliminar(numero: int) -> None:
    if numero in numeros:
        indice = numeros.index(numero)
        numeros.pop(indice)
    else:
        print("El número no está en la lista.")

while True:
    print("Menú de operaciones:")
    print("1. Agregar número")
    print("2. Eliminar número")
    print("3. Ver lista de números")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == '1':
        numero = int(input("Ingrese el número a agregar: "))
        agregar(numero)
        print("Lista actualizada:", numeros)
    
    elif opcion == '2':
        numero = int(input("Ingrese el número a eliminar: "))
        eliminar(numero)
        print("Lista actualizada:", numeros)
    
    elif opcion == '3':
        print("Lista actual de números:", numeros)
    
    elif opcion == '4':
        break
    
    else:
        print("Opción no válida.")

