# Semana 04 - Exercício Adicional 2 - digitos_adjacentes.py

# Escreva um programa que receba um número inteiro na entrada e verifique se o número recebido possui ao menos um dígito
# com um dígito adjacente igual a ele. Caso exista, imprima 'sim'; se não existir, imprima 'não'.

num = input('Digite um número inteiro: ')

adjacente = False
i = len(num) - 1 # Número total de letras na string: vai de 0 a len-1

while i > 0:
    if int(num[i]) == int(num[i-1]):
        adjacente = True
        i = i - 1
    else:
        i = i - 1
if adjacente:
    print('sim')
else:
    print('não')
