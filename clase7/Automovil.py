from abc import ABC, abstractmethod

class Automovil(ABC):
    __ruedas = 4

    def __init__(self,color,marca,aceleracion,velocidad, anio):
        self.color = color
        self.__marca = marca
        self.aceleracion = aceleracion
        self.velocidad = velocidad
        self.__anio = anio

    def acelera(self):
        self.velocidad = self.velocidad + self.aceleracion
        return self.velocidad

    def frena(self):
        self.velocidad = self.velocidad - self.aceleracion
        return self.velocidad

    #@abstractmethod
    # def conducir(self):
        #pass

    def getMarca(self):
        return self.__marca
    
    def getAnio(self):
        return self.__anio
    
    def setMarca(self, marca):
        self.__marca = marca
    
    def setAnio(self, anio):
        self.__anio = anio