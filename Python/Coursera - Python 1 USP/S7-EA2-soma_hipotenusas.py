# Semana 7 - Exercício Adicional 2 - soma_hipotenusas.py

# Escreva uma função 'soma_hipotenusas' que receba como parâmetro um número
# inteiro positivo 'n' e devolva a soma de todos os inteiros entre 1 e n
# que são comprimento da hipotenusa de algum triângulo retângulo com catetos
# inteiros.

# Em outras palavras, n é uma hipotenusa se existem inteiros i e j tais que:
# n^2 = i^2 + j^2

def hipotenusa(x,y,niter):
    if x*x + y*y == niter*niter:
        return True
    return False

def soma_hipotenusas(n):
    x = 1
    y = 1
    niter = 1
    count = 0
    while niter <= n:
        while x <= niter:
            while y <= niter:
                if hipotenusa(x,y,niter):
                    count = count + niter
                    y = niter
                    x = niter
                y = y + 1
            y = 1
            x = x + 1
        x = 1
        niter = niter + 1
    print('n =',count)
    return count
        
