class apuesta:

    def __init__(self):
        self.fichas = 0

    def ponerFicha(self, cuantas=1):
        self.fichas += cuantas

    def tomarFicha(self, cuantas=1):
        if cuantas > self.fichas:
            raise ValueError("No hay suficientes fichas para tomar.")
        self.fichas -= cuantas

    def tomarTodas(self):
        todas = self.fichas
        self.fichas = 0
        return todas

    def tieneFicha(self, cuantas=1):
        return cuantas <= self.fichas

    def estaVacia(self):
        return self.fichas == 0

    def __str__(self):
        return f"Apuesta: {self.fichas} fichas"
