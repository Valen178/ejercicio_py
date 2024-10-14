import unittest
from Calculadora import Calculadora

class Test(unittest.TestCase):
    def test_suma_positiva(self):
        self.assertEqual(Calculadora.sumar(5, 5), 10)

    def test_suma_negativa(self):
        self.assertEqual(Calculadora.sumar(-5, -5), -10)

    def test_resta_positiva(self):
        self.assertEqual(Calculadora.restar(5, 5), 0)

    def test_resta_negativa(self):
        self.assertEqual(Calculadora.restar(-5, -5), 0)

    def test_multiplicacion(self):
        self.assertEqual(Calculadora.multiplicar(5, 5), 25)

    def test_division(self):
        self.assertEqual(Calculadora.dividir(5, 5), 1)

if __name__ == '__main__':
    unittest.main()