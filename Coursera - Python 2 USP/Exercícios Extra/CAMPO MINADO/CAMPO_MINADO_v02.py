# Introdução à Computação com Python - Parte II - IME/USP
# Funções com Matrizes - Projeto - CAMPO MINADO

import random

def partida():
    diff = dificuldade()
    
    print('\n Escolha o tamanho da matriz.')
    num_lines = int(input('  No. de linhas: '))
    num_columns = int(input('  No. de colunas: '))
    while num_lines <= 1 or num_columns <= 1:
        print('   ⚠ A dimensão da matriz deve ser de, no mínimo, 2X2.')
        num_lines = int(input('  No. de linhas: '))
        num_columns = int(input('  No. de colunas: '))

    campo_minado = gera_campo(num_lines,num_columns,diff)
    campo_oculto = gera_campo_oculto(num_lines,num_columns)

    imprime_matriz_oculta(campo_minado)    
    jogada(campo_minado,campo_oculto)
    

def jogada(campo_minado,campo_oculto):
    dim = dimensoes(campo_minado)  # formato [lin,col]

    fim = False
    while not fim:        
        print(' Escolha uma célula.')
        lin = int(input('  Linha: '))
        col = int(input('  Coluna: '))
        while lin < 0 or col < 0 or lin >= dim[0] or col >= dim[-1]:
            print('   ⚠ As coordenadas devem respeitar a dimensão do campo.')
            lin = int(input(' Linha: '))
            col = int(input(' Coluna: '))

        abre = input(' Escolha entre revelar [R] ou salvar [S] a célula: ')
        while not abre == 'R' and not abre == 'r' and not abre == 'S' and not abre == 's':
            print('   ⚠ Sua escolha deve se limitar a R ou S.')
            abre = input(' Escolha entre revelar [R] ou salvar [S] a célula: ')
        
        if abre == 'S' or abre == 's':
            campo_oculto[lin][col] = '⚑'
            imprime_matriz_prog(campo_oculto)
        else:
            if campo_minado[lin][col] == BOMBA:
                campo_oculto[lin][col] = '✹'
                imprime_matriz_perdeu(campo_minado)
                print(' ☠ BUM! Você ativou uma bomba. ☠\n Fim de jogo!\n')

                fim = True
                novo_jogo()
            else:
                num_bombas = conta_bomba(campo_minado,lin,col)
                if num_bombas == 0:
                    campo_oculto[lin][col] = '-'
                   # abrir demais casas?
                   
                    imprime_matriz_prog(campo_oculto)
                else:                
                    campo_oculto[lin][col] = num_bombas
                    imprime_matriz_prog(campo_oculto)
            
        
def novo_jogo():
    print(' Deseja jogar novamente?')
    decisao = input(' Digite [1] para uma nova partida, ou [0] para encerrar: ')
    while decisao != '1' and decisao != '0':
        print('   ⚠ Sua escolha deve se limitar a 1 ou 0.')
        decisao = input(' Digite [1] para uma nova partida, ou [0] para encerrar: ')
    decisao = int(decisao)
    if decisao == 1:
        partida()
    

# Função conta_bomba() e Auxiliares -------------------------------------------

def conta_bomba(A,lin,col):
    ''' (matriz, int, int) -> int
    A função recebe uma matriz inteira A e uma posição (lin,col), e retorna
    o número de bombas ao redor da posição (lin,col).
    '''
    dim = dimensoes(A)  # formato [lin,col]
    
    # aplicar restrições: posição nos vértices, posição nas arestas
    if lin == 0:
        if col == 0:
            num_bombas = vertice_upleft(A,lin,col)  # caso 1
        elif col == (dim[-1])-1:
            num_bombas = vertice_upright(A,lin,col)  # caso 2
        else:
            num_bombas = aresta_up(A,lin,col)  # caso 7
    elif col == 0:
        if lin == (dim[0])-1:
            num_bombas = vertice_downleft(A,lin,col)  # caso 3
        else:
            num_bombas = aresta_left(A,lin,col)  # caso 5
    elif lin == (dim[0])-1:
        if col == (dim[-1])-1:
            num_bombas = vertice_downright(A,lin,col)  # caso 4
        else:
            num_bombas = aresta_down(A,lin,col)  # caso 8
    elif col == (dim[-1])-1:
        num_bombas = aresta_right(A,lin,col)  # caso 6
    else:
        num_bombas = middle(A,lin,col)  # caso 9
    return num_bombas

def vertice_upleft(A,lin,col):  # caso 1 (lin,col) = (0,0)
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

def vertice_upright(A,lin,col):  # caso 2 (lin,col) = (0,num_col(A))
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

def vertice_downleft(A,lin,col):  # caso 3 (lin,col) = (num_lin(A),0)
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

def vertice_downright(A,lin,col):  # caso 4 (lin,col) = (num_lin(A),num_col(A))
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

def aresta_left(A,lin,col):  # caso 5 (lin,col) = (lin,0)
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
  
def aresta_right(A,lin,col):  # caso 6 (lin,col) = (lin,num_col(A))
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

def aresta_up(A,lin,col):  # caso 7 (lin,col) = (0,col)
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

def aresta_down(A,lin,col):  # caso 8 (lin,col) = (num_lin(A),col)
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

def middle(A,lin,col):  # caso 9 (lin,col) = (lin,col)
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

def gera_campo(num_lines,num_columns,diff):
    '''(int,int,float) -> matriz (lista de listas)
    A função matrix() cria e retorna uma matriz com um dado número de
    linhas e colunas, com posições 0 e -1 escolhidas aleatoriamente.
    '''
    if diff == 1:
        cell = random.choices([BOMBA,0],[1,100],k=1)[0]
    elif diff == 2:
        cell = random.choices([BOMBA,0],[10,100],k=1)[0]
    elif diff == 3:
        cell = random.choices([BOMBA,0],[7,10],k=1)[0]
    
    matrix = []  # lista vazia
    for i in range(num_lines):
        line = []  # lista vazia
        for j in range(num_columns):  # para cada linha i, adicionamos j colunas
            line.append(random.choices([BOMBA,0],[7,10],k=1)[0])            
        matrix.append(line)  # adiciona cada linha à matriz inicial
    return matrix

def gera_campo_oculto(num_lines,num_columns):
    '''(int,int,float) -> matriz (lista de listas)
    A função matrix() cria e retorna uma matriz com um dado número de
    linhas e colunas, com posições 0 e -1 escolhidas aleatoriamente.
    '''
    matrix = []  # lista vazia
    for i in range(num_lines):
        line = []  # lista vazia
        for j in range(num_columns):  # para cada linha i, adicionamos j colunas
            line.append('☐') #✕
        matrix.append(line)  # adiciona cada linha à matriz inicial
    return matrix


# Funções de Impressão --------------------------------------------------------

def imprime_matriz_oculta(matriz):
    '''(list(list)) -> imprime_matriz()
    A função recebe o campo minado e o imprime como uma matriz de 'X'.
    '''
    print()
    print('    \\COL',end='')
    for j in range(len(matriz[0])):  # para cada coluna da matriz
        print(' [',j,']\t',end='')
    print('\n  LIN\\')

    for i in range(len(matriz)):  # número de linhas
        print(' [',i,']\t ',end='')
        for j in range(len(matriz[i])):  # número de colunas
            print('  ☐',end='\t') #✕
            if not j == len(matriz[i]) - 1:
                print(' ',end='')
        print('\n')

def imprime_matriz_prog(matriz):
    '''(matriz) -> imprime_matriz()
    A função recebe o campo oculto e as coordenadas [lin][col], e
    revela as posições [lin][col] da solução na matriz oculta.
    '''
    print()
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

def imprime_matriz_perdeu(matriz):
    '''(list(list)) -> imprime_matriz()
    A função recebe o campo minado e o imprime como solução, linha por linha.
    '''
    print()
    print(' SOLUÇÃO:\n')
    print('    \\COL',end='')
    for j in range(len(matriz[0])):  # para cada coluna da matriz
        print(' [',j,']\t',end='')
    print('\n  LIN\\')

    for i in range(len(matriz)):  # número de linhas
        print(' [',i,']\t ',end='')
        for j in range(len(matriz[i])):  # número de colunas
            if matriz[i][j] == -1:
                print(' ','✹',end='\t')
            else:
                print(' ','-',end='\t')
            if not j == len(matriz[i]) - 1:
                print(' ',end='')
        print('\n')

def imprime_matriz_resposta(matriz):
    '''(list(list)) -> imprime_matriz()
    A função recebe o campo minado e o imprime como solução, linha por linha.
    '''
    print()
    print(' SOLUÇÃO:\n')
    print('    \\COL',end='')
    for j in range(len(matriz[0])):  # para cada coluna da matriz
        print(' [',j,']\t',end='')
    print('\n  LIN\\')

    for i in range(len(matriz)):  # número de linhas
        print(' [',i,']\t ',end='')
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

    dim = [i,j]
    return dim  # formato [lin,col]

def dificuldade():
    print('\n Escolha a dificuldade do jogo.')
    diff = input(' [1] Fácil, [2] Médio, ou [3] Difícil: ')
    while diff != '1' and diff != '2' and diff != '3':
        print('   ⚠ Sua escolha deve se limitar a 1, 2 ou 3.')
        diff = input(' [1] Fácil, [2] Médio, ou [3] Difícil: ')
    diff = int(diff)
    return diff

#------------------------------------------------------------------------------

print('\n[ Campo Minado v02 ]')
print('\n*:･ﾟ✧ BEM-VINDO(A) AO CAMPO MINADO! ✧ﾟ･:*')
BOMBA = -1
partida()
