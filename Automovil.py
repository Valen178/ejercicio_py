from abc import ABC, abstractmethod

class Automovil(ABC):
    ruedas = 4
    def __init__(self,color,marca,aceleracion,velocidad):
        self.color = color
        self.marca = marca
        self.aceleracion = aceleracion
        self.velocidad = velocidad

    def acelera(self):
        self.velocidad = self.velocidad + self.aceleracion
        return self.velocidad

    def frena(self):
        self.velocidad = self.velocidad - self.aceleracion
        return self.velocidad

    # @abstractmethod
    # def conducir(self):
    #     pass

    def datos(automovil):
        print(f"Marca: {automovil.marca} y tiene {automovil.ruedas} ruedas" )
        