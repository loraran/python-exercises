# Semana 7 - Exercício Adicional 1 - conta_primos.py

# Escreva a função n_primos que recebe como argumento um número inteiro maior
# ou igual a 2 como parâmetro, e devolve a quantidade de números primos que
# existem entre 2 e n (incluindo 2 e, se for o caso, n).

def prime(num):
    if num == 1: # 1 é primo
        isprime = True
    else:
        isprime = True
        i = num - 1
        while not (i == 1): # Se i ainda não é 1...
            if num % i == 0: # Se a divisão é inteira...
                isprime = False
            i = i - 1
    return isprime

def n_primos(n):
    count = 0 # número de primos
    if n >= 2:
        num = n
        while num > 1:
            if prime(num) == True:
                count = count + 1
            num = num - 1
    return count
