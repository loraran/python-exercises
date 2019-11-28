# Exercício 3 - dezenas.py
# Faça um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas.

numero = input('Digite um número inteiro: ');
zero = '0';
inteiro = zero + numero;
dezenas = inteiro[-2];
print('O dígito das dezenas é',dezenas);
