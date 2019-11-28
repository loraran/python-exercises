# Semana 03 - Exercício 5 - ordenacao.py

# Receba 3 números inteiros na entrada e imprima 'crescente' se eles forem dados em ordem crescente.
# Caso contrário, imprima 'não está em ordem crescente'.

numero = int(input('Informe um número: '));
if (numero % 3 == 0) and (numero % 5 == 0):
    print('FizzBuzz');
else:
    print(numero);
