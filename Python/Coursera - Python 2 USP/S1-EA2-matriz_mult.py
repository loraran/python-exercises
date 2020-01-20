# Semana 01 - Exercício Adicional 2 - matriz_mult.py

def sao_multiplicaveis(m1,m2):
    ''' (list,list) -> sao_multiplicaveis()
    A função recebe duas matrizes como parâmetro e devolve True se elas
    forem multiplicáveis (na ordem dada), ou False caso contrário.
    Matrizes são multiplicáveis se o número de num_colunas(m1) = num_linhas(m2).
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
