# Boa_Constrictor.py
from Animal_exotico import Animal_Exotico

class Boa_Constrictor(Animal_Exotico):
    def __init__(self, nombre: str, edad: int, peso: float, pais_origen: str, impuestos: float):
        super().__init__(nombre, edad, peso, pais_origen, impuestos)  # Asegúrate de pasar todos los argumentos requeridos
        self.ratones_comidos = 0

    def hacer_sonido(self):
        return("¡Tsss!")

    def comer_ratón(self):
        if self.ratones_comidos >= 10:
            raise ValueError("Demasiados Ratones!")
        self.ratones_comidos += 1
        print(f"La boa ha comido {self.ratones_comidos} ratones.")
