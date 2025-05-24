import pandas as pd
from sklearn.neighbors import NearestNeighbors

class Recomendador:
    def __init__(self, historial_path):
        self.historial = pd.read_csv(historial_path)
        self.modelo = NearestNeighbors(n_neighbors=3)

    def entrenar(self):
        matriz = pd.crosstab(self.historial['usuario'], self.historial['libro'])
        self.modelo.fit(matriz)

    def recomendar(self, id_usuario):
        matriz = pd.crosstab(self.historial['usuario'], self.historial['libro'])
        if id_usuario not in matriz.index:
            return []
        distancias, vecinos = self.modelo.kneighbors([matriz.loc[id_usuario]])
        similares = matriz.index[vecinos[0]].tolist()
        recomendados = set()
        for vecino in similares:
            libros_vecino = self.historial[self.historial['usuario'] == vecino]['libro']
            recomendados.update(libros_vecino)
        ya_leidos = self.historial[self.historial['usuario'] == id_usuario]['libro']
        return list(recomendados - set(ya_leidos))
