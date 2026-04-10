


def factorizar(n):
    factores = []

    for divisor in range(2, int(n**0.5)+1):
        while n % divisor == 0:
            factores.append(divisor)
            n //= divisor

    if n > 1:
        factores.append(n)
    return factores


while True:
    
    num = input ("Introduce un número (0 para salir): ")
    numero = (int)(num)
    if numero == 0:
        break

    factores = factorizar (numero)
    print(f"{numero} = {'*'.join(map(str, factores))}")


