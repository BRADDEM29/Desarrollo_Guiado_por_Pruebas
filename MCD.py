import unittest

def mcd(a, b):
    """
    Función para calcular el Máximo Común Divisor (MCD) de dos números.
    Utiliza el algoritmo de Euclides.
    """
    while b != 0:
        a, b = b, a % b
    return a

def MaximoComunDivisor(a, b, c, d):
    mcd_ab = mcd(a, b)
    mcd_cd = mcd(c, d)
    return mcd(mcd_ab, mcd_cd)

class TestMinimoComunDivisor(unittest.TestCase):
    def test_MaximoComunDivisor(self):
        """
        Prueba el caso del minimo comun divisor
        """
        resultado_esperado = 12
        self.assertEqual(MaximoComunDivisor(24,36,48,60), resultado_esperado)

if  __name__ == "__main__":
    unittest.main()
