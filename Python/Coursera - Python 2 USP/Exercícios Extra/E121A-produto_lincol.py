# Introdução à Computação com Python - Parte II - IME/USP
# Funções com Matrizes - Exercício 12.1A

def produto_lincol(lin,A,col,B):
    '''(int, matriz real, int, matriz real) -> float
    A função recebe um inteiro 'lin', uma matriz 'A', um inteiro 'col' e uma
    matriz 'B', e devolve a soma do produto entre os elementos da linha 'lin'
    referente a A e os elementos da coluna 'col' referente a B.
    Nota: o número de colunas de A deve ser igual ao número de linhas de B.
    '''

    # pré-condição: num_colunas(A) == num_linhas(B)
    if multiplicaveis(A,B) == True:
        soma = 0
        for i in range(len(A[lin])):  # para cada elemento da linha/coluna...
            soma = soma + (A[lin][i]*B[i][col])
        # print(soma)
        return soma
        
    elif multiplicaveis(A,B) == False:
        print('As matrizes não são multiplicáveis.')
    

def multiplicaveis(m1,m2):
    ''' (list,list) -> bool
    A função recebe duas matrizes como parâmetro e devolve True se elas
    forem multiplicáveis (na ordem dada), ou False caso contrário.
    Matrizes são multiplicáveis se num_colunas(m1) = num_linhas(m2).
    '''
    
    dim_m1 = dimensoes(m1)  # formato iXj
    dim_m2 = dimensoes(m2)  # formato iXj

    if dim_m1[-1] == dim_m2[0]: # dim[-1] = j ; dim[0] = i
        return True
    else:
        return False


def dimensoes(matriz):
    '''(matriz) -> dimensoes()
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

###########

A = [ [1, 2, 1],
      [2, 2, 2],
      [1, 3, 2]]
B = [ [1, 2],
      [2, 2],
      [0, 2] ]

lin = 1
col = 1
produto_lincol(lin,A,col,B)
