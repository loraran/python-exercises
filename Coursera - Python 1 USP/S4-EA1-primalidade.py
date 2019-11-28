# Semana 04 - Exercício Adicional 1 - primalidade.py

# Escreva um programa que receba um número inteiro positivo na entrada e verifique se é primo.
# Se o número for primo, imprima 'primo'. Caso contrário, imprima 'não primo'.

num = int(input('Digite um número inteiro: '))
if num <= 0:
    print('O número deve ser inteiro e positivo.')
else:
    if num == 1: # Se num = 1...
        isprime = True
    else: # Se num > 1...
        isprime = True
        i = num - 1
        while not (i == 1): # Se i ainda não é 1...
            if num % i == 0: # Se a divisão é inteira...
                isprime = False
            i = i - 1
if isprime:
    print('primo')
else:
    print('não primo')
