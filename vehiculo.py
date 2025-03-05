import time

class Vehiculo:
    MARCAS_CARROS_PERMITIDAS = ["Chevrolet", "Toyota", "Renault", "Kia", "BMW", "Mazda", "Hyundai", "Peugeot", "Audi", "Volvo"]
    MARCAS_MOTOS_PERMITIDAS = ["Yamaha", "Suzuki", "Kawasaki", "Honda", "Ducati"]

    def __init__(self, marca, tipo, combustible):
        if tipo == "carro" and marca not in Vehiculo.MARCAS_CARROS_PERMITIDAS:
            raise ValueError(f"❌ La marca '{marca}' no está permitida para carros.")
        elif tipo == "moto" and marca not in Vehiculo.MARCAS_MOTOS_PERMITIDAS:
            raise ValueError(f"❌ La marca '{marca}' no está permitida para motos.")
        if combustible < 0 or combustible > 100:
            raise ValueError("❌ El nivel de combustible debe estar entre 0% y 100%.")
        self.marca = marca
        self.tipo = tipo
        self.combustible = combustible

    def encender(self):
        print("🔑 Intentando encender el vehículo...")
        time.sleep(1)
        if self.combustible < 10:
            print(f"⛽ URGENTE: El {self.tipo} {self.marca} tiene menos del 10% de combustible. ¡Ve a la gasolinera! 🚨")
        elif self.combustible < 19:
            print(f"⚠️ Advertencia: El {self.tipo} {self.marca} tiene bajo nivel de combustible.")
        else:
            print(f"✅ El {self.tipo} {self.marca} está encendido y listo para salir.")

    def arrancar(self):
        print("🚀 Preparando para arrancar...")
        time.sleep(1)
        print(f"🚗 Arrancando el {self.tipo} {self.marca}. Combustible actual: {self.combustible}%.")

    def conducir(self):
        print("🛣️ Iniciando trayecto...")
        time.sleep(1)
        while self.combustible > 0:
            print(f"⛽ Combustible restante: {self.combustible}%")
            self.combustible -= 1
            time.sleep(0.2)
            if self.combustible == 10:
                print(f"🚨 ¡Solo queda el 10%! Debes ir a una gasolinera pronto.")
        print(f"\n❌ Fin del trayecto. El {self.tipo} {self.marca} se apagó por falta de combustible.")
        print("💀 Te has quedado varado... Llama a una grúa o busca ayuda.")

class Moto(Vehiculo):
    def __init__(self, marca, combustible):
        super().__init__(marca, "moto", combustible)

class Carro(Vehiculo):
    def __init__(self, marca, combustible):
        super().__init__(marca, "carro", combustible)

def obtener_datos_vehiculo():
    marca = input("🔤 Introduce la marca del vehículo: ").capitalize()
    tipo = input("🚘 Introduce el tipo de vehículo (carro/moto): ").lower()
    try:
        combustible = int(input("⛽ Introduce el nivel de combustible (%): "))
        if combustible < 0 or combustible > 100:
            raise ValueError("❌ El nivel de combustible debe estar entre 0% y 100%.")
    except ValueError:
        raise ValueError("❌ Debes ingresar un número válido de combustible entre 0 y 100.")
    
    if tipo == "carro":
        return Carro(marca, combustible)
    elif tipo == "moto":
        return Moto(marca, combustible)
    else:
        raise ValueError("❌ Tipo de vehículo no válido.")

try:
    vehiculo = obtener_datos_vehiculo()
    vehiculo.encender()
    vehiculo.arrancar()
    vehiculo.conducir()
except ValueError as e:
    print(e)
