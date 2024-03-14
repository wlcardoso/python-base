#!/usr/bin/python3
"""Imprime a tabuada do 1 ao 10.
Tabuada 1
1
2
3
4
...
-------------
"""
__version__ = "0.1.0"
__author__ = "Washington"

#numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1, 11))

# Iteráveis
for numero in numeros:
    print("Tabuado do:", numero)
    for outro_numero in numeros:
        print(numero * outro_numero)
    print("----------")
