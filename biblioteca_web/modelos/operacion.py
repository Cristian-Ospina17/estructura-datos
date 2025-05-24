class Operacion:
    def __init__(self, id_usuario, id_libro, tipo, fecha):
        self.id_usuario = id_usuario
        self.id_libro = id_libro
        self.tipo = tipo  # 'prestamo' o 'devolucion'
        self.fecha = fecha
