from clase7.Automovil import Automovil

class Vehiculo(Automovil):
    def __init__(self, color, marca, aceleracion, velocidad, anio):
        super().__init__(color, marca, aceleracion, velocidad, anio)
    
    