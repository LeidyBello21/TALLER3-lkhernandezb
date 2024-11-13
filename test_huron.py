import unittest
from Boa_Constrictor import Boa_Constrictor
from Huron import Huron

class TestHuron(unittest.TestCase):
    def setUp(self):
        self.huron = Huron("Huron Test",8, 5.0, "Argentina", 50.0)

    def test_hacer_sonido(self):
        self.assertEqual(self.huron.hacer_sonido(), "¡Eek Eek!")

    def test_calcular_flete(self):
        flete = self.huron.calcular_flete()  # Método de la clase base
        self.assertGreater(flete, 0)

if __name__ == "__main__":
    unittest.main()
