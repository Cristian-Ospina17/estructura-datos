import pandas as pd


datos = pd.read_csv("excel_hospital/Hospital.csv", encoding="latin-1", sep=";")
datos["Número NIT"] = datos["Número NIT"].str.replace(",", "").str.replace('"', "").astype(int)


class RegistroHospital:
    def __init__(self, nit, nombre_org, sede, ciudad):
        self.nit = nit
        self.nombre_org = nombre_org
        self.sede = sede
        self.ciudad = ciudad
        self.izq = None
        self.der = None


class DirectorioSalud:
    def __init__(self):
        self.inicio = None

    def añadir_hospital(self, actual, nit, nombre_org, sede, ciudad):
        if not actual:
            return RegistroHospital(nit, nombre_org, sede, ciudad)
        if nit < actual.nit:
            actual.izq = self.añadir_hospital(actual.izq, nit, nombre_org, sede, ciudad)
        else:
            actual.der = self.añadir_hospital(actual.der, nit, nombre_org, sede, ciudad)
        return actual

    def mostrar_en_orden(self, nodo, lista=None):
        if lista is None:
            lista = []
        if nodo:
            self.mostrar_en_orden(nodo.izq, lista)
            lista.append({
                "NIT": nodo.nit,
                "Organización": nodo.nombre_org,
                "Sede": nodo.sede,
                "Ciudad": nodo.ciudad
            })
            self.mostrar_en_orden(nodo.der, lista)
        return lista

    def filtrar_por(self, nodo, tipo_busqueda, valor, encontrados=None):
        if encontrados is None:
            encontrados = []
        if nodo:
            if tipo_busqueda == "nit" and nodo.nit == valor:
                encontrados.append(nodo)
            elif tipo_busqueda == "sede" and nodo.sede.lower() == valor.lower():
                encontrados.append(nodo)
            elif tipo_busqueda == "ciudad" and nodo.ciudad.lower() == valor.lower():
                encontrados.append(nodo)
            self.filtrar_por(nodo.izq, tipo_busqueda, valor, encontrados)
            self.filtrar_por(nodo.der, tipo_busqueda, valor, encontrados)
        return encontrados


base = DirectorioSalud()
for _, fila in datos.iterrows():
    base.inicio = base.añadir_hospital(
        base.inicio,
        fila["Número NIT"],
        fila["Razón Social Organización"],
        fila["Nombre Sede"],
        fila["Nombre Municipio"]
    )


print("\n=== Lista Completa de Hospitales (Ordenados por NIT) ===")
hospitales = base.mostrar_en_orden(base.inicio)
for h in hospitales:
    print(f"{h['NIT']} - {h['Organización']} | {h['Sede']} ({h['Ciudad']})")


def ver_resultados(lista):
    if not lista:
        print("No se encontraron resultados.")
        return
    for item in lista:
        print(f"\nNombre: {item.nombre_org}\n  Sede: {item.sede}\n  Ciudad: {item.ciudad}")


def menu():
    while True:
        print("\n-- BÚSQUEDA DE HOSPITALES --")
        print("1. Buscar por NIT")
        print("2. Buscar por Sede")
        print("3. Buscar por Ciudad")
        print("4. Salir")

        eleccion = input("Opción (1-4): ")

        if eleccion == "1":
            try:
                codigo = int(input("Ingrese el NIT: "))
                resultados = base.filtrar_por(base.inicio, "nit", codigo)
                ver_resultados(resultados)
            except ValueError:
                print("NIT inválido. Debe ser un número.")
        elif eleccion == "2":
            nombre_sede = input("Nombre de la sede: ")
            resultados = base.filtrar_por(base.inicio, "sede", nombre_sede)
            ver_resultados(resultados)
        elif eleccion == "3":
            ciudad = input("Ciudad o municipio: ")
            resultados = base.filtrar_por(base.inicio, "ciudad", ciudad)
            ver_resultados(resultados)
        elif eleccion == "4":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida.")


menu()
