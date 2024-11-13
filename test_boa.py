import unittest
from Boa_Constrictor import Boa_Constrictor
from Huron import Huron

class TestBoaConstrictor(unittest.TestCase):
    def setUp(self):
        self.boa = Boa_Constrictor("Boa Test",5, 30.0, "Brasil", 200.0)

    def test_hacer_sonido(self):
        self.assertEqual(self.boa.hacer_sonido(), "¡Tsss!")  # Verificar que el método imprime el sonido correcto

    def test_calcular_flete(self):
        flete = self.boa.calcular_flete()  # Método que se asume implementado en la clase base Animal_exotico
        self.assertGreater(flete, 0)

    def test_comer_raton(self):
        for _ in range(10):
            if self.boa.ratones_comidos < 10:
                self.boa.comer_ratón()
            else:
                with self.assertRaises(ValueError):
                    self.boa.comer_ratón()

if __name__ == "__main__":
    unittest.main()