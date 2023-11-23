import random

class perinola:

    def __init__(self):
        opciones = ["Pon 1", "Pon 2", "Toma 1", "Toma 2", "Todos Toman", "Ponen Todos"]
        self.cara_visible = random.choice(opciones)

    def tirar(self):
        opciones = ["Pon 1", "Pon 2", "Toma 1", "Toma 2", "Todos Toman", "Ponen Todos"]
        self.cara_visible = random.choice(opciones)
        return self.cara_visible

    def __str__(self):
        return f"Salio: {self.cara_visible}"
