from abc import abstractmethod
from IAnimal import IAnimal

class Animal(IAnimal):
    
    def __init__(self, nombre:str, edad:int, peso:float) -> None:
        self.nombre = nombre
        self.peso = peso
        self.edad = edad        
        self.kilos_comidos =0

    #Metodos
    def comer(self, kilos: float) -> None:
        self.kilos_comidos += kilos

    def obtener_kilos_comidos(self):
        return self._kilos_comidos

    @abstractmethod
    def hacer_sonido(self):
        pass
    
    def obtener_nombre(self):
        return self._nombre
    
    def obtener_peso(self):
        return self._peso
    
    def obtener_edad(self):
        return self._edad



    