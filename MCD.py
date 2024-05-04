def mcd(a, b):
    """
    Función para calcular el Máximo Común Divisor (MCD) de dos números.
    Utiliza el algoritmo de Euclides.
    """
    while b != 0:
        a, b = b, a % b
    return a

def mcd_cuatro_numeros(a, b, c, d):
    """
    Función para calcular el MCD de cuatro números utilizando la función mcd.
    """
    mcd_ab = mcd(a, b)
    mcd_cd = mcd(c, d)
    return mcd(mcd_ab, mcd_cd)

# Ejemplo de uso
num1 = 24
num2 = 36
num3 = 48
num4 = 60

resultado = mcd_cuatro_numeros(num1, num2, num3, num4)
print(f"El Máximo Común Divisor de {num1}, {num2}, {num3} y {num4} es: {resultado}")
