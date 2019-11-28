# Semana 04 - Exercício 3 - soma_digitos.py

# Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída.

num = input('Digite um número inteiro: '); # num é tipo STRING
i = 0;
soma = 0;
while i < len(num):
    soma = soma + int(num[i]);
    i = i + 1;
print(soma);
