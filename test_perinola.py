import pytest
from perinola import perinola

class TestPerinola(pytest):
    
    def test_tirar_cambia_cara_visible(self):
        perinola = perinola()
        cara_inicial = perinola.cara_visible
        perinola.tirar()
        nueva_cara = perinola.cara_visible
        self.assertNotEqual(cara_inicial, nueva_cara)

    def test_str_muestra_correctamente(self):
        perinola = perinola()
        self.assertEqual(str(perinola), f"Salio: {perinola.cara_visible}")
