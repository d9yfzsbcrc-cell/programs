


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
    print ("\n", "Opciones: ")
    print ("-----------------")
    print ("1 Factorizar")
    print ("2 Salir\n")
    
    opcion = input ("Introduce opción: ")
    
    if opcion == "2":
        break
        
    elif opcion == "1":
        num = input ("Introduce un número: ")
        numero = (int)(num)
        factores = factorizar (numero)
        print(f"{numero} = {'*'.join(map(str, factores))}")


