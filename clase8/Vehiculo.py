from Automovil import Automovil

class Vehiculo(Automovil):
    def __init__(self, color, marca, aceleracion, velocidad, anio):
        super().__init__(color, marca, aceleracion, velocidad, anio)

    def datos(self):
        print(f"Marca: {self.marca} y tiene {self.ruedas} ruedas" )
    
    