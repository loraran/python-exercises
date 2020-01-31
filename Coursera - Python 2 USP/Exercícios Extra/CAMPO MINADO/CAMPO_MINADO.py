# Introdução à Computação com Python - Parte II - IME/USP
# Funções com Matrizes - Projeto - CAMPO MINADO

import random

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

# Função conta_bomba() e Auxiliares -------------------------------------------

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


# Função gera_campo() e Auxiliares --------------------------------------------

def gera_campo(num_lines,num_columns):
    '''(int,int,float) -> matriz (lista de listas)
    A função matrix() cria e retorna uma matriz com um dado número de
    linhas e colunas, com posições 0 e -1 escolhidas aleatoriamente.
    '''
    matrix = []  # lista vazia
    for i in range(num_lines):
        line = []  # lista vazia
        for j in range(num_columns):  # para cada linha i, adicionamos j colunas
            line.append(random.choices([-1,0],[7,10],k=1)[0])            
        matrix.append(line)  # adiciona cada linha à matriz inicial
    return matrix

def imprime_matriz_oculta(matriz):
    '''(list(list)) -> imprime_matriz()
    A função recebe o campo minado e o imprime como uma matriz de 'X'.
    '''
    print()
    print('    \\COL ',end='')
    for j in range(len(matriz[0])):  # para cada coluna da matriz
        print('[',j,'] \t ',end='')
    print('\n  LIN\\')

    for i in range(len(matriz)):  # número de linhas
        print('  [',i,']\t ',end='')
        for j in range(len(matriz[i])):  # número de colunas
            print('  X',end='\t')
            if not j == len(matriz[i]) - 1:
                print(' ',end='')
        print('\n')

def imprime_matriz_resposta(matriz):
    '''(list(list)) -> imprime_matriz()
    A função recebe o campo minado e o imprime como solução, linha por linha.
    '''
    print()
    print(' SOLUÇÃO:\n')
    print('    \\COL ',end='')
    for j in range(len(matriz[0])):  # para cada coluna da matriz
        print('[',j,'] \t ',end='')
    print('\n  LIN\\')

    for i in range(len(matriz)):  # número de linhas
        print('  [',i,']\t ',end='')
        for j in range(len(matriz[i])):  # número de colunas
            print(' ',matriz[i][j],end='\t')
            if not j == len(matriz[i]) - 1:
                print(' ',end='')
        print('\n')

# Funções Complementares ------------------------------------------------------

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

def imprime_matriz(matriz):
    '''(list(list)) -> imprime_matriz()
    A função recebe uma matriz como parâmetro e a imprime linha por linha.
    '''
    print()
    for i in range(len(matriz)):  # número de linhas
        print(' ',end='')
        for j in range(len(matriz[i])):  # número de colunas
            print(matriz[i][j],end ='\t')
            if not j == len(matriz[i]) - 1:
                print(' ',end='')
        print()

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

def main():
    print('\n*:･ﾟ✧ BEM-VINDO(A) AO CAMPO MINADO! ✧ﾟ･:*')

    print('\n Escolha o tamanho da matriz...')
    num_lines = int(input('  No. de linhas: '))
    num_columns = int(input('  No. de colunas: '))
    while num_lines <= 0 or num_columns <= 0:
        print('   ⚠ A dimensão da matriz deve ser, no mínimo, 1X1.')
        num_lines = int(input('  No. de linhas: '))
        num_columns = int(input('  No. de colunas: '))

    campo_minado = gera_campo(num_lines,num_columns)
    imprime_matriz_oculta(campo_minado)

    partida = True
    while partida:

    print('Fim de jogo!')

    
    
    #imprime_matriz(campo_minado)
    #imprime_matriz_oculta(campo_minado)
    #imprime_matriz_resposta(campo_minado)
    
    
dim = dimensoes(A)  # formato 'iXj'

##livre_bomba(A)

main()
