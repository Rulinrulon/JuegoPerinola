import pytest
from jugador import jugador

class TestJugador(pytest):
    
    def test_darFicha_agrega_correctamente(self):
        jugador = jugador("Franco", 8)
        jugador.darFicha(3)
        self.assertEqual(jugador.fichas, 11)

    def test_sacarFicha_quita_correctamente(self):
        jugador = jugador("Facu", 6)
        jugador.sacarFicha(2)
        self.assertEqual(jugador.fichas, 4)

    def test_tieneFicha_funciona_correctamente(self):
        jugador = jugador("Joaco", 10)
        self.assertTrue(jugador.tieneFicha(5))
        self.assertFalse(jugador.tieneFicha(12))

    def test_sinFichas_devuelve_correctamente(self):
        jugador = jugador("Tiago", 3)
        self.assertFalse(jugador.sinFichas())
        jugador.sacarFicha(3)
        self.assertTrue(jugador.sinFichas())

    def test_str_muestra_correctamente(self):
        jugador = jugador("Martina", 7)
        self.assertEqual(str(jugador), "Martina, 7 fichas")

