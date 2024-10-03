from Automovil import Automovil

class AutomovilVolador(Automovil):
    ruedas = 6

    def __init__(self,color,marca,aceleracion,velocidad, esta_volando,):
        super().__init__(color,marca,aceleracion,velocidad)
        self.esta_volando = True

    def vuela(self):
        self.esta_volando = True

    def aterriza(self):
        self.esta_volando = False
    
    def conducir(self):
        return "Esta volando"