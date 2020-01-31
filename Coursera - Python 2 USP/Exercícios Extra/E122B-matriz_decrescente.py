# Introdução à Computação com Python - Parte II - IME/USP
# Funções com Matrizes - Exercício 12.2B

def matriz_decrescente(A):
    '''(matriz) -> lista
    A função recebe uma matriz nl x nc e imprime uma tabela onde os elementos
    são listados em ordem decrescente, acompanhados da indicação da linha e
    coluna a que pertencem. Havendo repetições de elementos, a ordem é irrelevante.
    Exemplo:
    Para a matriz A(3X3) = [[3, 7, 1], [1, 2, 8], [5, 3, 4]], a função devolve:
    Elem   Linha  Coluna
      8      1      2
      7      0      1
      5      2      0
      4      2      2
      3      0      0
      3      2      1
      2      1      1
      1      0      2
      1      1      0
    '''

    dim = dimensoes(A)    
    numel = int(dim[0])*int(dim[-1])

    print('Elem\tLinha\tColuna')
    while numel > 0:  # varre o número total de elementos de A
        max_num = acha_max(A)
        print(' ',max_num[0],'\t ',max_num[1],'\t ',max_num[2])
        A[max_num[1]][max_num[2]] = 0
        numel = numel - 1

#---------------------------------------------------------

def acha_max(A):  # funcional apenas para matrizes com inteiros positivos.
    '''(matriz real) -> int, int, int
    A função recebe uma matriz real A e devolve 3 inteiros:
    k - o maior valor presente na matriz;
    lin - sua posição (linha);
    col - sua posição (coluna).
    '''

    dim = dimensoes(A)
    k = 0 #A[0][0]
    for i in range(len(A)):  # para cada linha de A...
        j = 0
        while j < int(dim[-1]):  # ...cheque cada elemento
            if A[i][j] > k:
                k = A[i][j]
                lin = i
                col = j
            j = j + 1
            
    return [k, lin, col]  # formato [valor máximo, linha, coluna]


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
    
    return (str(i)+'X'+str(j))  # formato STR 'iXj'

#---------------------------------------------------------

A = [[3, 7, 1], [1, 2, 8], [5, 3, 4]]
matriz_decrescente(A)
