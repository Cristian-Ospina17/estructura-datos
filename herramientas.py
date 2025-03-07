import math

def solicitar_float(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: Ingresa un número válido.")

def calcular_distancia():
    print("\nCalculando distancia entre dos puntos en R³")
    x1 = solicitar_float("Ingresa x1: ")
    y1 = solicitar_float("Ingresa y1: ")
    z1 = solicitar_float("Ingresa z1: ")

    x2 = solicitar_float("Ingresa x2: ")
    y2 = solicitar_float("Ingresa y2: ")
    z2 = solicitar_float("Ingresa z2: ")

    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    print(f"\nLa distancia entre los puntos es: {distancia}")

def solicitar_datos():
    print("¿Qué componentes tienes del vector? (Responde con 'si' o 'no')")
    tiene_x = input("¿Tienes componente X? ").strip().lower() == 'si'
    tiene_y = input("¿Tienes componente Y? ").strip().lower() == 'si'
    tiene_z = input("¿Tienes componente Z? ").strip().lower() == 'si'

    x = solicitar_float("Ingresa el valor de X: ") if tiene_x else None
    y = solicitar_float("Ingresa el valor de Y: ") if tiene_y else None
    z = solicitar_float("Ingresa el valor de Z: ") if tiene_z else None

    magnitud = None
    print("\n¿Conoces la magnitud del vector?")
    if input("¿Tienes la magnitud? (si/no): ").strip().lower() == 'si':
        magnitud = solicitar_float("Ingresa la magnitud: ")

    print("\n¿Tienes algún ángulo?")
    angulos = {}
    if input("¿Tienes ángulos de dirección? (si/no): ").strip().lower() == 'si':
        for eje in ['x', 'y', 'z']:
            if input(f"¿Tienes ángulo respecto a {eje.upper()}? (si/no): ").strip().lower() == 'si':
                angulo = solicitar_float(f"Ingresa el ángulo respecto a {eje.upper()}: ")
                if 0 <= angulo <= 180:
                    angulos[eje] = angulo
                else:
                    print(f"Ángulo inválido para {eje.upper()}. Debe estar entre 0° y 180°.")
    return x, y, z, magnitud, angulos

def calcular_faltantes(x, y, z, magnitud, angulos):
    if magnitud is None:
        magnitud = 1
    
    cos_alfa = math.cos(math.radians(angulos.get('x', 0))) if 'x' in angulos else None
    cos_beta = math.cos(math.radians(angulos.get('y', 0))) if 'y' in angulos else None
    
    if len(angulos) == 2:
        eje_faltante = {'x', 'y', 'z'} - set(angulos.keys())
        eje_faltante = list(eje_faltante)[0]
        angulos[eje_faltante] = math.degrees(math.acos(math.sqrt(1 - cos_alfa**2 - cos_beta**2)))
        
    if x is None and 'x' in angulos:
        x = magnitud * math.cos(math.radians(angulos['x']))
    if y is None and 'y' in angulos:
        y = magnitud * math.cos(math.radians(angulos['y']))
    if z is None and 'z' in angulos:
        z = magnitud * math.cos(math.radians(angulos['z']))
    
    return x, y, z

def calcular_resultante(x, y, z):
    return math.sqrt(x**2 + y**2 + z**2)

def calcular_angulos(x, y, z, R):
    alfa = math.degrees(math.acos(x / R))
    beta = math.degrees(math.acos(y / R))
    gamma = math.degrees(math.acos(z / R))
    return alfa, beta, gamma

def main():
    print("¿Qué deseas calcular?")
    print("1. Magnitud y ángulos de un vector")
    print("2. Distancia entre dos puntos")
    opcion = input("Selecciona una opción (1 o 2): ").strip()

    if opcion == '2':
        calcular_distancia()
        return

    x, y, z, magnitud, angulos = solicitar_datos()
    x, y, z = calcular_faltantes(x, y, z, magnitud, angulos)
    
    R = calcular_resultante(x, y, z)
    print(f"\nComponentes del vector: X = {x}, Y = {y}, Z = {z}")
    print(f"\nMagnitud resultante (R): {R}")

    alfa, beta, gamma = calcular_angulos(x, y, z, R)
    print(f"\nÁngulos de dirección:")
    print(f"Ángulo con X (α): {alfa}°")
    print(f"Ángulo con Y (β): {beta}°")
    print(f"Ángulo con Z (γ): {gamma}°")

if __name__ == "__main__":
    main()
