class Vehiculo:
    MARCAS_CARROS_PERMITIDAS = ["Toyota", "Renault", "Kia", "Chevrolet", "BMW", "Mercedes Benz", "Volvo", "Audi", "Mini", "Porsche", "Land Rover", "Lexus", "Ds", "Cadillac"]
    MARCAS_MOTOS_PERMITIDAS = ["Honda", "Suzuki", "Yamaha", "BMW"]

    def __init__(self, marca, tipo_vehiculo, nivel_combustible):
        if tipo_vehiculo == "carro" and marca not in Vehiculo.MARCAS_CARROS_PERMITIDAS:
            raise ValueError(f"Marca {marca} no permitida para carros.")
        elif tipo_vehiculo == "moto" and marca not in Vehiculo.MARCAS_MOTOS_PERMITIDAS:
            raise ValueError(f"Marca {marca} no permitida para motos.")
        self.marca = marca
        self.tipo_vehiculo = tipo_vehiculo
        self.nivel_combustible = nivel_combustible

    def encender(self):
        if self.nivel_combustible < 19:
            print(f"El {self.tipo_vehiculo} {self.marca} necesita gasolina.")
        else:
            print(f"El {self.tipo_vehiculo} {self.marca} está encendido.")

    def arrancar(self):
        print(f"El {self.tipo_vehiculo} {self.marca} está arrancando con {self.nivel_combustible}% de combustible.")

    def conducir(self):
        while self.nivel_combustible > 0:
            self.nivel_combustible -= 1
            print(f"Conduciendo... Nivel de combustible: {self.nivel_combustible}%")
            if self.nivel_combustible < 19:
                print(f"Advertencia: El {self.tipo_vehiculo} {self.marca} necesita gasolina.")
            if self.nivel_combustible == 0:
                print(f"El {self.tipo_vehiculo} {self.marca} se ha detenido por falta de combustible.")
                break

class Moto(Vehiculo):
    def __init__(self, marca, nivel_combustible):
        super().__init__(marca, "moto", nivel_combustible)

class Carro(Vehiculo):
    def __init__(self, marca, nivel_combustible):
        super().__init__(marca, "carro", nivel_combustible)

def obtener_datos_vehiculo():
    marca = input("Introduce la marca del vehículo: ")
    tipo = input("Introduce el tipo de vehículo (moto/carro): ").lower()
    nivel_combustible = int(input("Introduce el nivel de combustible (%): "))

    if tipo == "moto":
        return Moto(marca, nivel_combustible)
    elif tipo == "carro":
        return Carro(marca, nivel_combustible)
    else:
        raise ValueError("Tipo de vehículo no válido.")

try:
    vehiculo = obtener_datos_vehiculo()
    vehiculo.encender()
    vehiculo.arrancar()
    vehiculo.conducir()
except ValueError as e:
    print(e)