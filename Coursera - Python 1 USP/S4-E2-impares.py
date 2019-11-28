# Semana 04 - Exercício 2 - n_impares.py

# Receba um número inteiro positivo na entrada e imprima os n primeiros números ímpares naturais.

n = int(input('Digite o valor de n: '));
i = 1;
while i <= n:
    impar = 1 + 2*(i-1);
    print(impar);
    i = i + 1;
