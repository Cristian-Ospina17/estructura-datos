class Electrodomestico:
    def __init__(self, marca, modelo, consumo):
        self.marca = marca
        self.modelo = modelo
        self.consumo = consumo

    def encender(self):
        print(f"{self.marca} {self.modelo} encendido.")


class Lavadora(Electrodomestico):
    def __init__(self, marca, modelo, consumo, capacidad):
        super().__init__(marca, modelo, consumo)
        self.capacidad = capacidad

    def encender(self):
        print(f"La lavadora {self.marca} está encendida.")
        self.iniciarCicloDeLavado()

    def iniciarCicloDeLavado(self):
        print(f"La lavadora {self.marca} inició el ciclo de lavado de {self.capacidad} kg.")


class Refrigerador(Electrodomestico):
    def __init__(self, marca, modelo, consumo, congelador):
        super().__init__(marca, modelo, consumo)
        self.congelador = congelador

    def encender(self):
        print(f"El refrigerador {self.marca} está encendido.")
        self.regularTemperatura()

    def regularTemperatura(self):
        print(f"El refrigerador {self.marca} está regulando la temperatura.")
        if self.congelador:
            print("El congelador también está funcionando.")


# ✅ Prueba con input
tipo = input("¿Lavadora o Refrigerador? ").strip().lower()

marca = input("Marca: ")
modelo = input("Modelo: ")
consumo = input("Consumo energético: ")

if tipo == "lavadora":
    capacidad = float(input("Capacidad (kg): "))
    l = Lavadora(marca, modelo, consumo, capacidad)
    l.encender()
elif tipo == "refrigerador":
    congelador = input("¿Tiene congelador? (si/no): ").strip().lower() == "si"
    r = Refrigerador(marca, modelo, consumo, congelador)
    r.encender()
else:
    print("Tipo no válido.")
