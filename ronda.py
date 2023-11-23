from jugador import jugador

class ronda:

    def __init__(self):
        self.jugadores = []

    def agregarJugador(self, jugador):
        if not jugador.tieneFicha():
            raise ValueError("El jugador no tiene fichas para unirse a la ronda.")
        self.jugadores.append(jugador)

    def sacarJugadoresSinFichas(self):
        self.jugadores = [jugador for jugador in self.jugadores if not jugador.sinFichas()]

    def jugadorEnTurno(self):
        return self.jugadores[0]

    def pasarTurno(self):
        jugador = self.jugadores.pop(0)
        self.jugadores.append(jugador)

    def quedaUnSoloJugador(self):
        return len(self.jugadores) == 1

    def __str__(self):
        return "\n".join(str(jugador) for jugador in self.jugadores)
