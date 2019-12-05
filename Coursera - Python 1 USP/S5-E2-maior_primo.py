# Semana 05 - Exercício 2 - maior_primo.py

# Escreva a função 'maior_primo' que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função.

def primo(num): # Verifica se um número é primo
    isprime = True
    i = num - 1
    while not (i == 1): # Se i ainda não é 1...
        if num % i == 0: # Se a divisão é inteira...
            isprime = False
        i = i - 1
    return isprime

def maior_primo(num):
    if num < 2:
        print('O número deve ser maior ou igual a 2.')
    else:
        i = 1
        if primo(num):
            return num
        else:
            while i < (num-2):
                newnum = num - i
                primo(newnum)
                if primo(newnum):
                    return newnum
                else:
                    i = i + 1
            return newnum
