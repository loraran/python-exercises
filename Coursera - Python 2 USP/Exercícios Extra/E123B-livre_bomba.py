# Introdução à Computação com Python - Parte II - IME/USP
# Funções com Matrizes - Exercício 12.3B - CAMPO MINADO

BOMBA = -1
A = [[0, -1, 0, 0], [-1, 0, -1, 0], [-1, 0, -1, -1], [-1, -1, -1, 0]]

def livre_bomba(A):
    ''' (matriz) -> list
    A função lê uma matriz A de 0's (posições livres) e -1's (bombas),
    computa e imprime a quantidade de bombas ao redor de cada posição livre (0).
    '''

    print('Posição Livre\tBombas')
    
    for lin in range(int(dim[0])):  # varrendo cada elemento de A
        for col in range(int(dim[-1])):
            if A[lin][col] != BOMBA:  # se temos uma posição livre...
                num_bombas = conta_bomba(A,lin,col)
                print(' (',lin,',',col,')\t ',num_bombas)

# Função conta_bomba() e Auxiliares ----------------------

def conta_bomba(A,lin,col):
    ''' (matriz, int, int) -> int
    A função recebe uma matriz inteira A e uma posição (lin,col), e retorna
    o número de bombas ao redor da posição (lin,col).
    '''
    
    # aplicar restrições: posição nos vértices, posição nas arestas
    if lin == 0:
        if col == 0:
            num_bombas = vertice_upleft(lin,col)  # caso 1
        elif col == int(dim[-1])-1:
            num_bombas = vertice_upright(lin,col)  # caso 2
        else:
            num_bombas = aresta_up(lin,col)  # caso 7
    elif col == 0:
        if lin == int(dim[0])-1:
            num_bombas = vertice_downleft(lin,col)  # caso 3
        else:
            num_bombas = aresta_left(lin,col)  # caso 5
    elif lin == int(dim[0])-1:
        if col == int(dim[-1])-1:
            num_bombas = vertice_downright(lin,col)  # caso 4
        else:
            num_bombas = aresta_down(lin,col)  # caso 8
    elif col == int(dim[-1])-1:
        num_bombas = aresta_right(lin,col)  # caso 6
    else:
        num_bombas = middle(lin,col)  # caso 9
    return num_bombas

def vertice_upleft(lin,col):  # caso 1 (lin,col) = (0,0)
    '''(int, int) -> int
    A função verifica a quantidade (int) de bombas no entorno de uma dada
    coordenada (lin,col) da matriz A.
    Caso 1: célula superior esquerda -> (lin,col) = A[0][0].
    '''
    num_bombas = 0
    if A[lin+1][col] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin][col+1] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin+1][col+1] == BOMBA:
        num_bombas = num_bombas + 1
    return num_bombas

def vertice_upright(lin,col):  # caso 2 (lin,col) = (0,num_col(A))
    '''(int, int) -> int
    A função verifica a quantidade (int) de bombas no entorno de uma dada
    coordenada (lin,col) da matriz A.
    Caso 2: célula superior direita -> (lin,col) = A[0][col(A)].
    '''
    num_bombas = 0
    if A[lin+1][col] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin][col-1] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin+1][col-1] == BOMBA:
        num_bombas = num_bombas + 1
    return num_bombas

def vertice_downleft(lin,col):  # caso 3 (lin,col) = (num_lin(A),0)
    '''(int, int) -> int
    A função verifica a quantidade (int) de bombas no entorno de uma dada
    coordenada (lin,col) da matriz A.
    Caso 3: célula inferior esquerda -> (lin,col) = A[lin(A)][0].
    '''
    num_bombas = 0
    if A[lin-1][col] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin][col+1] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin-1][col+1] == BOMBA:
        num_bombas = num_bombas + 1
    return num_bombas

def vertice_downright(lin,col):  # caso 4 (lin,col) = (num_lin(A),num_col(A))
    '''(int, int) -> int
    A função verifica a quantidade (int) de bombas no entorno de uma dada
    coordenada (lin,col) da matriz A.
    Caso 4: célula inferior direita -> (lin,col) = A[lin(A)][col(A)].
    '''
    num_bombas = 0
    if A[lin-1][col] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin][col-1] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin-1][col-1] == BOMBA:
        num_bombas = num_bombas + 1
    return num_bombas

def aresta_left(lin,col):  # caso 5 (lin,col) = (lin,0)
    '''(int, int) -> int
    A função verifica a quantidade (int) de bombas no entorno de uma dada
    coordenada (lin,col) da matriz A.
    Caso 5: células da aresta esquerda -> (lin,col) = A[lin][0].
    '''
    num_bombas = 0
    if A[lin-1][col] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin+1][col] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin][col+1] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin-1][col+1] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin+1][col+1] == BOMBA:
        num_bombas = num_bombas + 1
    return num_bombas
  
def aresta_right(lin,col):  # caso 6 (lin,col) = (lin,num_col(A))
    '''(int, int) -> int
    A função verifica a quantidade (int) de bombas no entorno de uma dada
    coordenada (lin,col) da matriz A.
    Caso 6: células da aresta direita -> (lin,col) = A[lin][col(A)].
    '''
    num_bombas = 0
    if A[lin-1][col] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin+1][col] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin][col-1] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin-1][col-1] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin+1][col-1] == BOMBA:
        num_bombas = num_bombas + 1
    return num_bombas

def aresta_up(lin,col):  # caso 7 (lin,col) = (0,col)
    '''(int, int) -> int
    A função verifica a quantidade (int) de bombas no entorno de uma dada
    coordenada (lin,col) da matriz A.
    Caso 7: células da aresta superior -> (lin,col) = A[0][col].
    '''
    num_bombas = 0
    if A[lin][col-1] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin][col+1] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin+1][col] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin+1][col-1] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin+1][col+1] == BOMBA:
        num_bombas = num_bombas + 1
    return num_bombas

def aresta_down(lin,col):  # caso 8 (lin,col) = (num_lin(A),col)
    '''(int, int) -> int
    A função verifica a quantidade (int) de bombas no entorno de uma dada
    coordenada (lin,col) da matriz A.
    Caso 8: células da aresta inferior -> (lin,col) = A[lin(A)][col].
    '''
    num_bombas = 0
    if A[lin][col-1] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin][col+1] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin-1][col] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin-1][col-1] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin-1][col+1] == BOMBA:
        num_bombas = num_bombas + 1
    return num_bombas

def middle(lin,col):  # caso 9 (lin,col) = (lin,col)
    '''(int, int) -> int
    A função verifica a quantidade (int) de bombas no entorno de uma dada
    coordenada (lin,col) da matriz A.
    Caso 9: células interiores -> (lin,col) = A[lin][col].
    '''
    num_bombas = 0
    if A[lin-1][col] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin+1][col] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin][col-1] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin][col+1] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin-1][col-1] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin-1][col+1] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin+1][col-1] == BOMBA:
        num_bombas = num_bombas + 1
    if A[lin+1][col+1] == BOMBA:
        num_bombas = num_bombas + 1
    return num_bombas

# Funções Complementares ---------------------------------

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

dim = dimensoes(A)  # formato 'iXj'
##lin = 1
##col = 2
##conta_bomba(A,lin,col)
livre_bomba(A)
