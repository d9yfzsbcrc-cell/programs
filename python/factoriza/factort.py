# -*- coding: utf-8 -*-

# Benchmark con timeit

import time


def factorizar(n):
    global factores
    factores = []

    for divisor in range(2, int(n**0.5)+1):
        while n % divisor == 0:
            factores.append(divisor)
            n //= divisor

    if n > 1:
        factores.append(n)
    return factores

num = input ("Introduce un número: ")
numero = (int)(num)

inicio = time.time()

factorizar (numero)

fin = time.time()

print(f"{numero} = {'*'.join(map(str, factores))}")

#print(f"factorizar {numero} = {fin-inicio/ 10:.4f} segundos")

print(fin-inicio) 