def mcd(a, b):
    """
    Función para calcular el Máximo Común Divisor (MCD) de dos números.
    Utiliza el algoritmo de Euclides.
    """
    while b != 0:
        a, b = b, a % b
    return a

def mcd_cuatro_numeros():
    """
    Función para calcular el MCD de cuatro números ingresados por el usuario.
    """
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    c = int(input("Ingrese el tercer número: "))
    d = int(input("Ingrese el cuarto número: "))
    
    mcd_ab = mcd(a, b)
    mcd_cd = mcd(c, d)
    return mcd(mcd_ab, mcd_cd)

# Ejemplo de uso
resultado = mcd_cuatro_numeros()
print(f"El Máximo Común Divisor de los cuatro números ingresados es: {resultado}")
