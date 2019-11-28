# Semana 04 - Exercício 1 - fatorial.py

# Escreva um programa que receba um número natural n na entrada e imprima n! (fatorial) na saída.

import math;
num = int(input('Digite o valor de n: '));
if num < 0:
    print('O número inserido não é natural.');
else:
    fatorial = math.factorial(num);
    print(fatorial);
