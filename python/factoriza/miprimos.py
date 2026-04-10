
# -*- coding: utf-8 -*-

def es_miprimo(n):
    if n <= 1:
        return False
    #for i in range(2, n):
    for i in range(2, int(n**0.5 + 1)):
        if n % i == 0:
            return False
    return True

q =41
print(f"{q} es primo? {es_miprimo(q)}")

