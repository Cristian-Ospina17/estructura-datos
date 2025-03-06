class Usuario:
    def __init__(self, nombreDeUsuario, contraseña):
        self.nombreDeUsuario = nombreDeUsuario
        self.contraseña = contraseña

    def iniciarSesion(self):
        usuario = input("Ingrese su nombre de usuario: ")
        clave = input("Ingrese su contraseña: ")
        if usuario == self.nombreDeUsuario and clave == self.contraseña:
            print("Inicio de sesión exitoso.")
            return True
        else:
            print("Credenciales incorrectas.")
            return False


class Administrador(Usuario):
    def gestionarUsuarios(self):
        print(f"{self.nombreDeUsuario} está gestionando usuarios.")


class Cliente(Usuario):
    def realizarCompra(self):
        print(f"{self.nombreDeUsuario} está realizando una compra.")


# ✅ Prueba con input
tipo = input("¿Eres Administrador o Cliente? ").strip().lower()

nombreDeUsuario = input("Crea tu nombre de usuario: ")
contraseña = input("Crea tu contraseña: ")

if tipo == "administrador":
    admin = Administrador(nombreDeUsuario, contraseña)
    if admin.iniciarSesion():
        admin.gestionarUsuarios()
elif tipo == "cliente":
    cliente = Cliente(nombreDeUsuario, contraseña)
    if cliente.iniciarSesion():
        cliente.realizarCompra()
else:
    print("Tipo de usuario no válido.")
