class FiguraGeometrica:
    def calcularArea(self):
        pass


class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return (self.base * self.altura) / 2


class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def calcularArea(self):
        return self.lado ** 2


# ✅ Prueba con input
figura = input("¿Quieres calcular el área de un Triángulo o Cuadrado? ").strip().lower()

if figura == "triangulo":
    base = float(input("Base: "))
    altura = float(input("Altura: "))
    t = Triangulo(base, altura)
    print("Área del triángulo:", t.calcularArea())
elif figura == "cuadrado":
    lado = float(input("Lado: "))
    c = Cuadrado(lado)
    print("Área del cuadrado:", c.calcularArea())
else:
    print("Figura no válida.")