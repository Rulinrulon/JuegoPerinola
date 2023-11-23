import unittest
from ronda import ronda
from jugador import jugador

class TestRonda(unittest.TestCase):

    def test_agregarJugador_funciona_correctamente(self):
        ronda = ronda()
        jugador = jugador("Franco", 5)
        ronda.agregarJugador(jugador)
        self.assertIn(jugador, ronda.jugadores)

    def test_agregarJugador_tira_error_sin_fichas(self):
        ronda = ronda()
        jugador = jugador("Martina", 0)
        with self.assertRaises(ValueError):
            ronda.agregarJugador(jugador)

    def test_sacarJugadoresSinFichas_elimina_correctamente(self):
        ronda = ronda()
        jugador1 = jugador("Julian", 3)
        jugador2 = jugador("Enzo", 0)
        ronda.agregarJugador(jugador1)
        ronda.agregarJugador(jugador2)
        ronda.sacarJugadoresSinFichas()
        self.assertIn(jugador1, ronda.jugadores)
        self.assertNotIn(jugador2, ronda.jugadores)

    def test_jugadorEnTurno_devuelve_correctamente(self):
        ronda = ronda()
        jugador1 = jugador("Joaco", 4)
        jugador2 = jugador("Facu", 6)
        ronda.agregarJugador(jugador1)
        ronda.agregarJugador(jugador2)
        self.assertEqual(ronda.jugadorEnTurno(), jugador1)

    def test_pasarTurno_funciona_correctamente(self):
        ronda = ronda()
        jugador1 = jugador("Marcelo", 3)
        jugador2 = jugador("Fran", 5)
        ronda.agregarJugador(jugador1)
        ronda.agregarJugador(jugador2)
        ronda.pasarTurno()
        self.assertEqual(ronda.jugadorEnTurno(), jugador2)

    def test_quedaUnSoloJugador_devuelve_correctamente(self):
        ronda = ronda()
        jugador = jugador("Ariadna", 2)
        ronda.agregarJugador(jugador)
        self.assertTrue(ronda.quedaUnSoloJugador())
        ronda.agregarJugador(jugador("Tiago", 4))
        self.assertFalse(ronda.quedaUnSoloJugador())

    def test_str_muestra_correctamente(self):
        ronda = ronda()
        jugador1 = jugador("Agostina", 3)
        jugador2 = jugador("Matias", 7)
        ronda.agregarJugador(jugador1)
        ronda.agregarJugador(jugador2)
        self.assertEqual(str(ronda), f"{jugador1}\n{jugador2}")

if __name__ == '__main__':
    unittest.main()
