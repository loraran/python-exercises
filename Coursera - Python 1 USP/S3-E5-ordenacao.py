# Semana 03 - Exercício 5 - ordenacao.py

# Receba 3 números inteiros na entrada e imprima 'crescente' se eles forem dados em ordem crescente.
# Caso contrário, imprima 'não está em ordem crescente'.

num1 = int(input('Informe um número: '));
num2 = int(input('Informe outro número: '));
num3 = int(input('Informe mais um número: '));
if (num1 < num2) and (num2 < num3):
    print('crescente');
else:
    print('não está em ordem crescente');
