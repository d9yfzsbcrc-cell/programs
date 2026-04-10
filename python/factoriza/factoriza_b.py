
# -*- coding: utf-8 -*-

# Benchmark con timeit
from timeit import timeit


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
t_f = timeit(lambda: factorizar (numero))

print(f"{numero} = {'*'.join(map(str, factores))}")

print(f"factorizar {numero} = {t_f / 10:.4f} segundos")


