import unittest
from apuesta import apuesta

class TestApuesta(unittest.TestCase):

    def test_ponerFicha_agrega_correctamente(self):
        apuesta = apuesta()
        apuesta.ponerFicha(3)
        self.assertEqual(apuesta.fichas, 3)

    def test_tomarFicha_quita_correctamente(self):
        apuesta = apuesta()
        apuesta.ponerFicha(5)
        apuesta.tomarFicha(3)
        self.assertEqual(apuesta.fichas, 2)

    def test_tomarTodas_devuelve_correctamente(self):
        apuesta = apuesta()
        apuesta.ponerFicha(7)
        todas = apuesta.tomarTodas()
        self.assertEqual(todas, 7)
        self.assertEqual(apuesta.fichas, 0)

    def test_tieneFicha_funciona_correctamente(self):
        apuesta = apuesta()
        apuesta.ponerFicha(4)
        self.assertTrue(apuesta.tieneFicha(2))
        self.assertFalse(apuesta.tieneFicha(6))

    def test_estaVacia_devuelve_correctamente(self):
        apuesta = apuesta()
        self.assertTrue(apuesta.estaVacia())
        apuesta.ponerFicha(2)
        self.assertFalse(apuesta.estaVacia())

    def test_str_muestra_correctamente(self):
        apuesta = apuesta()
        apuesta.ponerFicha(5)
        self.assertEqual(str(apuesta), "Apuesta: 5 fichas")

if __name__ == '__main__':
    unittest.main()
