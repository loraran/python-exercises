# Semana 8 - Exercício Adicional 2 - inverte.py

# Escreva um programa que recebe uma sequência de números inteiros e imprima
# todos os valores em ordem inversa. A sequência sempre termina pelo número 0.
# Note que 0 (ZERO) não deve fazer parte da sequência.

num = int(input('Digite um número: '))
seq = []
while num != 0:
    seq.append(num)
    num = int(input('Digite um número: '))

seq.reverse()

for i in range(len(seq)):
    print(seq[i])
