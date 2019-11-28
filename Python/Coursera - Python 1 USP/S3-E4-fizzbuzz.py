# Semana 03 - Exercício 4 - fizzbuzz.py

# Receba um número inteiro na entrada e imprima 'FizzBuzz' na saída se o número for divisível por 3 e por 5.
# Caso contrário, imprima o mesmo número que foi dado na entrada.

numero = int(input('Informe um número: '));
if (numero % 3 == 0) and (numero % 5 == 0):
    print('FizzBuzz');
else:
    print(numero);
