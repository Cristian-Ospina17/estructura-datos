class Empleado:
    def __init__(self, nombre, salario, departamento):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

    def trabajar(self):
        print(f"{self.nombre} está trabajando.")


class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento, equipo):
        super().__init__(nombre, salario, departamento)
        self.equipo = equipo

    def trabajar(self):
        print(f"{self.nombre} supervisa al equipo: {', '.join(self.equipo)}.")


class Desarrollador(Empleado):
    def __init__(self, nombre, salario, departamento, lenguaje):
        super().__init__(nombre, salario, departamento)
        self.lenguaje = lenguaje

    def trabajar(self):
        print(f"{self.nombre} escribe código en {self.lenguaje}.")


tipo = input("¿Eres Gerente o Desarrollador? ").strip().lower()

nombre = input("Nombre: ")
salario = float(input("Salario: "))
departamento = input("Departamento: ")

if tipo == "gerente":
    equipo = input("Escribe los nombres del equipo separados por coma: ").split(",")
    g = Gerente(nombre, salario, departamento, equipo)
    g.trabajar()
elif tipo == "desarrollador":
    lenguaje = input("Lenguaje de programación: ")
    d = Desarrollador(nombre, salario, departamento, lenguaje)
    d.trabajar()
else:
    print("Tipo no válido.")
