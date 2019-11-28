# Semana 03 - Exercício Adicional 2 - bhaskara.py

# Escreva um programa que calcula as raízes de uma equação do segundo grau.
# O programa deve receber os parâmetros a, b, e c da equação ax^2 + bx + c, respectivamente, e imprimir o resultado da seguinte maneira:
# - Quando não houver raízes reais, imprima: 'esta equação não possui raízes reais'.
# - Quando houver apenas uma raiz real, imprima: 'a raiz desta equação é X', onde X é o valor da raiz.
# - Quando houver duas raízes reais, imprima: 'as raízes da equação são X e Y', onde X e Y são os valores das raízes.
# - Além disso, no caso de existirem 2 raízes reais, elas devem ser impressas em ordem crescente.

import math;
print('Equação de segundo grau: ax + by + c = 0');
a = float(input('Informe o valor de a: '));
b = float(input('Informe o valor de b: '));
c = float(input('Informe o valor de c: '));
delta = b**2 - 4*a*c;
# Se a equação tiver raízes reais, elas serão dadas por:
# x = (-b +- sqrt(delta)/2a) , delta = (b^2 - 4ac)
if delta < 0:
    print('esta equação não possui raízes reais');
else:
    X = (-b + math.sqrt(delta))/(2*a);
    if delta == 0:
        print('a raiz desta equação é',X);
    else:
        Y = (-b - math.sqrt(delta))/(2*a);
        if X < Y:
            print('as raízes da equação são',X,'e',Y);
        else:
            print('as raízes da equação são',Y,'e',X);
