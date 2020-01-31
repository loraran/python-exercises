# Introdução à Computação com Python - Parte II - IME/USP
# Funções com Matrizes - Exercício 12.2A

def acha_max(A):
    '''(matriz real) -> int, int, int
    A função recebe uma matriz real A e devolve 3 inteiros:
    k - o maior valor presente na matriz;
    lin - sua posição (linha);
    col - sua posição (coluna).
    '''

    dim = dimensoes(A)
    k = A[0][0]
    for i in range(len(A)):  # para cada linha de A...
        j = 0
        while j < int(dim[-1]):
            if A[i][j] > k:
                k = A[i][j]
                lin = i
                col = j
            j = j + 1
    print('O maior número da matriz é',k,', localizado na linha',lin,'e coluna',col,'.')
    return k, lin, col

#---------------------------------------------------------

def dimensoes(matriz):
    '''(matriz) -> string
    A função dimensoes() retorna as dimensões (linhas e colunas) de uma matriz
    inserida pelo usuário, no formato 'iXj'.
    Exemplo: dimensoes([[1, 2, 3] , [4, 5, 6]]) = 2X3
    '''
    if type(matriz) == int:  # há apenas uma linha
        i = 1
    elif type(matriz) == list:  # há mais de uma linha
        i = len(matriz)  # número de colunas

    if type(matriz[0]) == int:  # há apenas uma coluna
        j = 1
    elif type(matriz[0]) == list:  # há mais de uma coluna
        j = len(matriz[0])  # número de colunas
    
    return (str(i)+'X'+str(j))  # formato iXj

#---------------------------------------------------------

A = [[3, 7, 1], [1, 2, 8], [5, 3, 4]]
acha_max(A)
