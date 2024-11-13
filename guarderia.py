

# Guarderia.py
from Boa_Constrictor import Boa_Constrictor
from Huron import Huron

class Guarderia:
    def __init__(self):
        self.boas = [Boa_Constrictor("Boa 1", 5, 25.0, "Colombia", 150.0),
                     Boa_Constrictor("Boa 2", 6, 28.0, "Perú", 180.0)]
        self.hurones = [Huron("Huron 1",7, 4.0, "Chile", 45.0),
                        Huron("Huron 2",8, 5.5, "Ecuador", 55.0)]

    def alimentar_boa(self, boa):
        if boa is None:
            return "Esta Boa no existe!"
        try:
            boa.comer_ratón()
            return "Éxito"
        except ValueError:
            return "La boa está llena"

# Prueba de la clase Guarderia
if __name__ == "__main__":
    guarderia = Guarderia()
    
    for _ in range(10):  # Alimentar a la boa 10 veces
        print(guarderia.alimentar_boa(guarderia.boas[0]))  # Imprime "Éxito" cada vez

    print(guarderia.alimentar_boa(guarderia.boas[0]))  # Debería imprimir "Éxito" o "La boa está llena"
    print(guarderia.alimentar_boa(None))               # Debería imprimir "Esta Boa no existe!"
