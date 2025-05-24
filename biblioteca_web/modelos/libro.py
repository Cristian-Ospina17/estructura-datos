class Libro:
    def __init__(self, id_libro, titulo, autor, genero, disponible=True):
        self.id = id_libro
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.disponible = disponible
