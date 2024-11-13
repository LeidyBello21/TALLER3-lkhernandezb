from abc import ABC, abstractmethod

class IAnimal(ABC):

    def __init__(self, especie: str, edad: int, sexo: str):
        self.especie = especie
        self.edad = edad
        self.sexo = sexo

    @abstractmethod
    def comer(self, kilos):
        pass

    @abstractmethod
    def obtener_kilos_comidos(self):
        pass

    @abstractmethod
    def hacer_sonido(self):
        pass