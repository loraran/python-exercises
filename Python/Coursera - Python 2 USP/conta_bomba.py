# Introdução à Computação com Python - Parte II - IME/USP
# Funções com Matrizes - Exercício 12.3A - CAMPO MINADO

BOMBA = -1

def conta_bomba(A,lin,col):
    ''' (matriz, int, int) -> int
    A função recebe uma matriz inteira A e uma posição (lin,col), e retorna
    o número de bombas ao redor da posição (lin,col).
    Nota: O uso de constantes é uma boa prática de programação...
    '''

    dim = dimensoes(A)  # 'iXj'

    # verifica se a posição (lin,col) existe na matriz A
    if not lin >= 0 or not lin < int(dim[0]) or not col >= 0 or not col < int(dim[-1]):
        print('As coordenadas [',lin,',',col,'] não são válidas.')
        print('A dimensão da matriz A é',dim)
    else:
        num_bombas = 0
        
        # aplicar restrições: posição nos vértices, posição nas arestas

        if lin == 0 and col == 0:
            
        if lin > 0:
            if A[lin-1][col] == BOMBA:
                num_bombas = num_bombas + 1
            
            
        
        if A[lin][col] != BOMBA:
        
        for i in range(int(dim[0])):  # para cada linha...
            for j in range(int(dim[-1])):  # para cada coluna...
                if A[i][j] != BOMBA
    
#---------------------------------------------------------

def casas_vertice_upleft(lin,col):  # caso (lin,col) = (0,0)
    '''(int, int) - int'''
    if A[lin+1][col] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin][col+1] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin+1][col+1] == BOMBA:
        num_bombas = num_bombas + 1
    return num_bombas

def casas_vertice_upright(lin,col):  # caso (lin,col) = (0,col(A))
    '''(int, int) - int'''
    if A[lin+1][col] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin][col-1] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin+1][col-1] == BOMBA:
        num_bombas = num_bombas + 1
    return num_bombas

def casas_vertice_downleft(lin,col):  # caso (lin,col) = (lin(A),0)
    '''(int, int) - int'''
    if A[lin-1][col] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin][col+1] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin-1][col+1] == BOMBA:
        num_bombas = num_bombas + 1
    return num_bombas

def casas_vertice_downright(lin,col):
    '''(int, int) - int'''
    if A[lin-1][col] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin][col-1] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin-1][col-1] == BOMBA:
        num_bombas = num_bombas + 1
    return num_bombas
        

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

A = [[3, -1, 1], [-1, 2, 8], [5, 3, -1]]
lin = 1
col = 1
conta_bomba(A,lin,col)
