import math

class Persona:
    def __init__(self, nombre, edad, genero):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
    def presentarse(self):
        print(f"Hola, soy {self.nombre}, tengo {self.edad} años y soy {self.genero}.")

class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    def depositar(self, cantidad):
        self.saldo += cantidad
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Fondos insuficientes.")
        else:
            self.saldo -= cantidad
    def mostrarSaldo(self):
        print(f"Saldo actual: ${self.saldo}")

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura
    def perimetro(self):
        return 2 * (self.base + self.altura)

class Circulo:
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return math.pi * self.radio ** 2
    def circunferencia(self):
        return 2 * math.pi * self.radio

class Libro:
    def __init__(self, titulo, autor, genero, año):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.año = año
    def mostrar(self):
        print(f"{self.titulo} de {self.autor}, Género: {self.genero}, Año: {self.año}")

class Cancion:
    def __init__(self, titulo, artista, album, duracion):
        self.titulo = titulo
        self.artista = artista
        self.album = album
        self.duracion = duracion
    def reproducir(self):
        print(f"🎶 '{self.titulo}' de {self.artista}, Álbum: {self.album}, Duración: {self.duracion} min")

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    def total(self, cantidad):
        return self.precio * cantidad

class Estudiante:
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso
        self.calificaciones = []
    def agregar(self, nota):
        self.calificaciones.append(nota)
    def promedio(self):
        return sum(self.calificaciones) / len(self.calificaciones)

persona = Persona(input("Nombre: "), int(input("Edad: ")), input("Género: "))
persona.presentarse()

cuenta = CuentaBancaria(persona, float(input("Saldo inicial: ")))
cuenta.depositar(float(input("Depositar: ")))
cuenta.retirar(float(input("Retirar: ")))
cuenta.mostrarSaldo()

rect = Rectangulo(float(input("Base rectángulo: ")), float(input("Altura rectángulo: ")))
print(f"Área: {rect.area()}, Perímetro: {rect.perimetro()}")

circulo = Circulo(float(input("Radio círculo: ")))
print(f"Área: {circulo.area():.2f}, Circunferencia: {circulo.circunferencia():.2f}")

libro = Libro(input("Título libro: "), input("Autor: "), input("Género: "), int(input("Año: ")))
libro.mostrar()

cancion = Cancion(input("Título canción: "), input("Artista: "), input("Álbum: "), float(input("Duración (min): ")))
cancion.reproducir()

producto = Producto(input("Producto: "), float(input("Precio: ")))
print(f"Total a pagar: ${producto.total(int(input('Cantidad: ')))}")

estudiante = Estudiante(input("Nombre estudiante: "), int(input("Edad: ")), input("Curso: "))
for _ in range(3):
    estudiante.agregar(float(input("Calificación: ")))
print(f"Promedio: {estudiante.promedio():.2f}")
