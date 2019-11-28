# Semana 03 - Exercício 3 - buzz.py

# Receba um número inteiro na entrada e imprima 'Buzz' na saída se o número for divisível por 5.
# Caso contrário, imprima o mesmo número que foi dado na entrada.

numero = int(input('Informe um número: '));
if numero % 5 == 0:
    print('Buzz');
else:
    print(numero);
